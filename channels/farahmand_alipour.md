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
<img src="https://cdn4.telesco.pe/file/c9IHvvgiUOql85Mp2U0LhY78Npxybz8jdvQEnceRas01p4Z9zjxt4QDJNn_c3z3gWUR1Xcvc8ZfE5fjv8w9kYzlp_ivXfSNSz6t1JuaMn1cKgYne0mZZkbNrRK299eCqe8zTq3Y5T3ey67EA0auh2FwX0eI3neHq9fy_fHXEfW4q5kMWXXpJPeeZVQi4n8HoXPMzpSCpdqsj9jAFOOzrV2Mks3I7OKcFz_zlqFpg7yxY-VObYj0slF826BQUGJX0OaVrRwrpnGQ_Sc9EsGkaN2sKzOFrmhb0p3_lbqb2x2CfcxxrSNSLScmS3vWfaQibLfg2a0Hz9wDST8Gt0BlQOQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 10:14:23</div>
<hr>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">می‌د‌ونید چرا جریان چپ اینقدر خودش رو
هم داستان و همراستا با آخوندِ جنایتکار دیده؟ می‌دونید چرا اینقدر چپ از جامعه ایران
متنفر و خشمگینه؟
چون همه هویت و هستی اینها مبارزه با آمریکاست!
ایران اگه یک پایگاه ضد آمریکایی و یک کوبا
و یک ویتنام بشه براشون ارزش داره!
ج‌ا، چپ‌ها رو قت@ل عام هم کنه براشون مهم نیست!
چون هدف و نقطه مرکزی آمریکاست.
همه هستی‌شون در این تعریف شده که جایی آمریکا
حمله کنه و اینها سریعا بیان وسط میدون
و ضد آمریکا شعار بدن،
در قضیه ایران ناراحتن که چرا آمریکا حمله کرد
و اکثر مردم ضد آمریکا نشدن؟
البته به جز اقلیت مزدور اسلامگرا و اقلیت بی‌آبروی چپ که هر دو اساس انقلاب ۵۷ رو داشتند.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید
که حامیان حکومت،
در دفاع از خودشون میگن :
بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل
شعار میدیم، ولی کدوم کشور به خاطر
شعار دادن و پرچم آتش زدن و حرف،
حمله کرده به یک کشور دیگه؟
البته که همین جا هم صادق نیستند،
چون اونها فقط شعار ندادند!
خامنه‌ای رسما در برنامه «گام دوم»
که سیاست‌ها و اولویت‌های جمهوری اسلامی
رو برای ۴۰ سال بعدی تعیین می‌کرد،
اخراج آمریکا از منطقه خاورمیانه
و مبارزه با اسرائیل رو رسما جزو برنامه‌های نظام قرار داد، بگذریم به اینکه در عمل و با افتخار و صدای بلند می‌گفتند ما به گروه‌های تروریستی حزب‌الله لبنان، حماس، جهاد اسلامی و….. موشک، سلاح و پول میدیم برای مبارزه با اسراییل و….!
هر گروه دیگه هم بخواد مبارزه کنه،
بهش پول و سلاح میدیم! اینو خامنه‌ای هم علنا گفت.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tghLNjJxIO0o3ncmker6bjFmgbro14X3_K8RK0e2R7KGACDzQ5vHiQ-Rx1Drvl1si6QtuNW4aGVDa4Wb2_Jw6xhhvMxCr3zrQbQWbwBSnmNvuz4fTBKEFs02v0veDD65FTIVtxifEhXaI7XgCca_VYQPtXdn_Nc14CGBMztgSLWQh4GI6tta4lqXTCtB4B33arxkM0gz5snFGdKLIxjx7LTN2-s5XnmdFrD_r0TjI8Uc4b6akVnM4qZ3vHNUzprrufb1evAfbMXTFtZrlnRUbraBNc_4eJGz7K15YWIqq2dXcI88WBThcaMxNQN8PaVC4qFb9cuF6eOAugMQZbBtNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورو شده ۳۰۰ هزار تومن!
و دلار تقریبا به ۲۷۰ هزار تومن رسیده.
ولی یادمون باشه که بزرگ‌ترین
فروشنده و عرضه کننده ارز در بازارهای ایران
خود حکومت و عوامل حکومت هستند!
ارز دست اونهاست!
صادرات دست اونهاست!
حکومت و عواملش خودشون دارند قیمت رو بالا
می‌برن، تا ارزهاشون رو به قیمتی بالاتر بفروشند
و سود بیشتری به جیب بزنند!
اساسا برخی از دامن زدن به جو جنگ و التهاب،
کار خود حکومته و مافیای حکومتیه، برای افزایش
قیمت‌ها و افزایش قیمت ارز
و افزایش درآمدهای خودش!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6lzOjye61X0dEEOwSAEF8aeWNNe080Bt6BDGKFbl4t4O_5sDZmnOKjTBjf7Qz7m8a9l3Ies2EZZTrPc_jRKk_pUMrd0pBWBQmt7Or7Ra178JNkOP3TzHz9wVRki1PWgvNJvuL24gWBZ_Rwerx8oZSW6lPV_PalVE2hskvGfM_lONV2TeigfVmzN3N-C9n64Fu-4OrsRKRoAtJAxxuZMR7c5sF5sgGnllg1A8JpFBtcJeSUIDQXY39QUrA4-D6Sv0LFRzeJFSGSpMSgKndxDjrpec9KIxjUWH3BWWy8T2nASHn7wLGmmAFBEUkaoO_eG1uNkdGD-FALx564kdDvpsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyncodHB0nc2-UTvdivoywSXWQxw-etVyaO24a_ilbv_uwMzhzJuYo7iKpYp6VAtKmA27i8Z-AmBJpGITxyvqgOEXFkSVdq-D2kLXJJfPaii-lY7l-q_CtSLzzfDYQ_m_94D22PDWUcXm-j7nCHpXfCRRE_3FfXdSTUY_VEgi_yv1FTQSGQ4iqGHhBwJxXpluWFpY-QvEZZlgR4L7RQV3LUVZyWngeuYjuYMfFe9jkKrYbj_BB1tLV_b77pBXiywgNEuXkXIMuput03jc0a2HSgn1-ndoVvJXeQLscxWYSN8Qo2S9wg6MiBe4ymGhfzr1lJkUKakozdvEHAVp6kjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=q8n5JPP-XA9clfAj68WeDE8SeHLnsL4s9DjgbgKfImT2pAOFoJbhmc7bLA0pm11MEch92s6KAxPl1o9MRumw7T4NmUrxJO9IZEJiEz75_sKV24LAcX1ahOKoYC1VB-a0XtL0EiZG-zlEdz_pTp7Pjiml2wMu5MdhBIan1yo3AOFxzpdjlA9JFzAaybrVx1aityOBxXubXLPfzHxP5zayMFYgULdehA2d03R6JWA2WpFws1KPAU2BK2uYLll2u2u97X3ctkDgI1NDlZYmhbKDzXM6ZiomYMU-HxEmJp9pd1UprCiTazcLvx7mwi_p8zr4t2-ylj0X87hAUWrx_Lh8zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=q8n5JPP-XA9clfAj68WeDE8SeHLnsL4s9DjgbgKfImT2pAOFoJbhmc7bLA0pm11MEch92s6KAxPl1o9MRumw7T4NmUrxJO9IZEJiEz75_sKV24LAcX1ahOKoYC1VB-a0XtL0EiZG-zlEdz_pTp7Pjiml2wMu5MdhBIan1yo3AOFxzpdjlA9JFzAaybrVx1aityOBxXubXLPfzHxP5zayMFYgULdehA2d03R6JWA2WpFws1KPAU2BK2uYLll2u2u97X3ctkDgI1NDlZYmhbKDzXM6ZiomYMU-HxEmJp9pd1UprCiTazcLvx7mwi_p8zr4t2-ylj0X87hAUWrx_Lh8zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=HaGqRzkeJEs9JFPXG-Cp3wQsF6iFX-qgy7DPOls7Q-C-Zz6F-79PjfNrayR90VNrJEn7YnZnvCXLceoJjN9zekeHjYUOnuO153mOxFQlVP--aQ5NtfRppbNWsEAcdILCIH2yaqklErMfu7XGZSXgCcfBrlbKwh1kQJZTEhvLiuxZDi7atXeLKvrS1d-QfQNR29SOTw2aBVap4ONxoCEQXbHs4ZQ0Z-3Pyy8s2M8oFZyZ9kV3wMDD2rNk1xAtVSNXFnA7OJ8cKEZi34HmTuPNM8yg0r7acC8vSRSWVAKR3qYiYdas96r8r09KsHMFoAvXuOkSliLoJCAlQ5f3YFuWlqAOMkw5AmIyJCMYOjIwyGyHgRnKqsLge6z9YWedA2LSXCLUcmgfm-P6YJHSXhfLPTgdr5JXTXmgcQQtoGJk0RezaDdWWhxPk9fCYEG8VKFYlZ_q5BeOfxopLVPLfKR1oEm--mI8rTZa1K2Rx3h0oK543_U4Ft1cRxUMALxwOjcgFlKcwfKRnebYhvvtGphhS4unUSAor68HZRYIfdj7C35XvOK0dIhRIxY17VO5afadRW846ePOPW70m3M9VmyOYM7av6_tgb30DKNJkuDzCFRRsgKmVmu_CfZZC_IzM6XxS8EnVoTc_RH2vqXPUgGetxnmXnzQsGyCesSkyuis_Lk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=HaGqRzkeJEs9JFPXG-Cp3wQsF6iFX-qgy7DPOls7Q-C-Zz6F-79PjfNrayR90VNrJEn7YnZnvCXLceoJjN9zekeHjYUOnuO153mOxFQlVP--aQ5NtfRppbNWsEAcdILCIH2yaqklErMfu7XGZSXgCcfBrlbKwh1kQJZTEhvLiuxZDi7atXeLKvrS1d-QfQNR29SOTw2aBVap4ONxoCEQXbHs4ZQ0Z-3Pyy8s2M8oFZyZ9kV3wMDD2rNk1xAtVSNXFnA7OJ8cKEZi34HmTuPNM8yg0r7acC8vSRSWVAKR3qYiYdas96r8r09KsHMFoAvXuOkSliLoJCAlQ5f3YFuWlqAOMkw5AmIyJCMYOjIwyGyHgRnKqsLge6z9YWedA2LSXCLUcmgfm-P6YJHSXhfLPTgdr5JXTXmgcQQtoGJk0RezaDdWWhxPk9fCYEG8VKFYlZ_q5BeOfxopLVPLfKR1oEm--mI8rTZa1K2Rx3h0oK543_U4Ft1cRxUMALxwOjcgFlKcwfKRnebYhvvtGphhS4unUSAor68HZRYIfdj7C35XvOK0dIhRIxY17VO5afadRW846ePOPW70m3M9VmyOYM7av6_tgb30DKNJkuDzCFRRsgKmVmu_CfZZC_IzM6XxS8EnVoTc_RH2vqXPUgGetxnmXnzQsGyCesSkyuis_Lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOKw8ijB58Abbrsc5QKUqBiESQKeAtDzFQeNwH5Z9h6RX0SXfDhH9dyFDseYZhaUXYe51n85gLalYss6-2AUiYA57vusRQWF75B0faQlO_GzzfkivtdYj3C7X9Z2ZbrPSQgriP6Y5DBsxQk7f-nsf-o_6S-b02IFSQWx-Nutehb4MCu4gaoNsozMNSBwMt_FlN8WK9pY0-FJQx49nXcjXHdGGGTfGbrngBNmG3rdtURYpgRz-EiaAxJ-eary5dS07PFNQJjpipjMRBSRtanZANh8gocTshSTwxXtlq469dMuAn0HjRdKwye7iKslPHdfb8D7tHh-c9X4rS4F2yxxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kh-rrEtfh-29E-YPRXV6AISOUPmnhVgquuZiBg7H5Q0zgAPOZKtwdX3byoaFgMqAjobd0VsiVDerX3v56LGch9xFmhiWQ0x0Yt64Y8HlAvvtNR9FYkmy5ubgZLguYnelxiyCGZPNQy1WRQMD7aE3CvMTOIjf2U0kK-LzIWuV4MGw3GV0VWM1UkxtYaGJ4fbZjI7R2gGLtJOEtUyqsAYDJ1S0LD_Nov4VPak6Fv26wYh8zpYzkZqKu-gLtPT3_nzOgY0qI8QDJiuxbcSYiEnCR3iix6We6JJXg0H02oGupNhm9jusrfVrot3Sh36g8mv1Uc2OdiY0VaRM7aUVxl8FYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBqWleY5vRtxMMtOjzHlLVNJueTfqeBsekosH2LxW9lfkyx0NyiKsRpvA2nO1WoOIWh6h4UIWSx7QRiFK-dh_3okmWSGRUSNkmUEue8OZit7SbEVuQgmxmChBLe1qGD7jBzRrN5SlmGMREXanr26RFQ_q2bN1irD-uJJH5FgHPnTMrANXumJEJTQVbkrMEM7xFg_iIojrDc444kYccMYRRp1eFoFFT5u2O8W4SYNbUFa1fWMHXSHZbcrBxelu0u-S7fdC-lPlgVAGTuKo5sqlqtbLG4XGJ4JY6xn6cGoJnIsFxJ7hpRTfy0k5CqDnNNen5hTkHLFaIQJts5QnYBpmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=RSfmNEpgsc0cftspoLRIA5dGWX6q-komNopJxeG1MyDBXqQdDYezLy5wYFhFHHc7ftg7q2L2o9Ige2aQrJm4Qj74sn35VoaKiF3NrTxgIE6HlQlyZuv97bNMIheV6FKPCHmHZDcscLgxLD7bIZ0BpnFTNRkLMn5IbiYA5JxKMJAqXR811hft_NqKrBRmjEODyMYuSUZg2BTiJ34fnGgqlzOQmLTVaPIb8RpEBkyFYE7_MtBuZQmfFByagpZeOPHvAwKOe6clOykAMHfAzLPyPArtUOumVNQm5seFH7zlm6CXn0Pj2ltsgEM8zWX3LGXo4dkYPqjzS7jsm0piOB4HmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=RSfmNEpgsc0cftspoLRIA5dGWX6q-komNopJxeG1MyDBXqQdDYezLy5wYFhFHHc7ftg7q2L2o9Ige2aQrJm4Qj74sn35VoaKiF3NrTxgIE6HlQlyZuv97bNMIheV6FKPCHmHZDcscLgxLD7bIZ0BpnFTNRkLMn5IbiYA5JxKMJAqXR811hft_NqKrBRmjEODyMYuSUZg2BTiJ34fnGgqlzOQmLTVaPIb8RpEBkyFYE7_MtBuZQmfFByagpZeOPHvAwKOe6clOykAMHfAzLPyPArtUOumVNQm5seFH7zlm6CXn0Pj2ltsgEM8zWX3LGXo4dkYPqjzS7jsm0piOB4HmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=ay0n1A29iO7kerFZTGnyFDq9oAQ117RvoiA_6_PNGuEP4jDM4zv_1dCRc8Mn5mh9752kdKA4P_bIscRG0V1fvMdkGtq8avj3OfwN-x0PnyWjKVLiTVgvG6Xemtog_3W3VqLfc0NLihQebB_1HesgGhLuV0yNyQLCPWPaWKATRjJcvZF8TbPKJr9ciiNsq9BJlaAAL6dRQIt-Gqe_F_vqdzV2db1In4Spr-jF4Fk_VxNiguXoHblpQWINvzfHGNZ6Ke_6Ws34gg3oAVMdMYFddtmz9xdB3RxjU2fOS8ZZeE7vh4R8eFBJUfHUdH8r610whxHbrKuf6jAjopub8ubiQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=ay0n1A29iO7kerFZTGnyFDq9oAQ117RvoiA_6_PNGuEP4jDM4zv_1dCRc8Mn5mh9752kdKA4P_bIscRG0V1fvMdkGtq8avj3OfwN-x0PnyWjKVLiTVgvG6Xemtog_3W3VqLfc0NLihQebB_1HesgGhLuV0yNyQLCPWPaWKATRjJcvZF8TbPKJr9ciiNsq9BJlaAAL6dRQIt-Gqe_F_vqdzV2db1In4Spr-jF4Fk_VxNiguXoHblpQWINvzfHGNZ6Ke_6Ws34gg3oAVMdMYFddtmz9xdB3RxjU2fOS8ZZeE7vh4R8eFBJUfHUdH8r610whxHbrKuf6jAjopub8ubiQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-1dVlVuyvhyavF41dk2EtqHjzdYgbDcPBlmWEQ5iI2vwe3vEQTCQB33KgrnAU-J5YPlbwM6V0hT0pT0dVimzVJVO9bMGgFtvHgx78VUoKWJSRjuWIVdkcJO3YLb5rakIVtkaTER4VLxU7CMVbiHJCMQKytRQCMihPlwNdAXdTYteOcicTkCn8O0x4rBG2CqnbAUVdCxcom3UxnpMioK9UOKARIvlDU94N-kgtx0p_8TS1ftbmoKa_tTSV_OzBEjOOI2euAiZAsgioSo1ZMEVLBzOH99q_wyZFC9-nfVUBDV_FOiRRMjdrD_UI0i9euW5D4-MD4NdVJ8VFwAmEmrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=UjQeIXNebqhTKuqLoNq87Fh3Qojrk3NJn9BjDazvjPYl9REtLDOcIAL_IKu27bdDRMQ2Vr1XxVSe6dkuyqQy0DCrAAADra9j39vPnyvvKjA3iST9K7edfT5XsAFKr56hiMy2YxFSZDFRJmr6ImZf1SiCAcweJYZcbsHPEdublqFDFXbHRM7JSnAAguQrCZRQKZl-vy2egoWyDazmXDDKEsq7j24CkPHlrsy17n3pDjG33I_v7PwXFLHUvu73axjYH9XfHFBfxhoWUqfRN3i5WVXw-V0T-N5DDJzMumcNtgJXXELM_iXygq0sGMKFGY08M7NbLlP4cHPDLwoqpiksv3WvpRShMsX9wrMZO8vEe_L3WogNVv4jg66KEriph6vVrICFTIBbNwd1B_DcmNdCwGd-DagoDZ6rmvhW6KVx5mLpAO_V0JeMswTHDdEcCrA136KViaqmZ9EXWW-anga6V4OpOHWg_UjoH8upNqoJjLdWICHDTU150-b-TwEZzmVmdlEcMtl2DjKHgYjP3P6FtTLy8LHa6yCnCGImzfiV-ZCSwBAoIdJSEQDI7ZigEptzAnX8G7aG3J6kptPRjqBGPXHLqNJLvY9fMtMm-tRVPgvGvYWngbCnyigevaFulRMBhkm76KDsGO03xBLaaXyiVMkekgHeuc-dOGcTPKtGXco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=UjQeIXNebqhTKuqLoNq87Fh3Qojrk3NJn9BjDazvjPYl9REtLDOcIAL_IKu27bdDRMQ2Vr1XxVSe6dkuyqQy0DCrAAADra9j39vPnyvvKjA3iST9K7edfT5XsAFKr56hiMy2YxFSZDFRJmr6ImZf1SiCAcweJYZcbsHPEdublqFDFXbHRM7JSnAAguQrCZRQKZl-vy2egoWyDazmXDDKEsq7j24CkPHlrsy17n3pDjG33I_v7PwXFLHUvu73axjYH9XfHFBfxhoWUqfRN3i5WVXw-V0T-N5DDJzMumcNtgJXXELM_iXygq0sGMKFGY08M7NbLlP4cHPDLwoqpiksv3WvpRShMsX9wrMZO8vEe_L3WogNVv4jg66KEriph6vVrICFTIBbNwd1B_DcmNdCwGd-DagoDZ6rmvhW6KVx5mLpAO_V0JeMswTHDdEcCrA136KViaqmZ9EXWW-anga6V4OpOHWg_UjoH8upNqoJjLdWICHDTU150-b-TwEZzmVmdlEcMtl2DjKHgYjP3P6FtTLy8LHa6yCnCGImzfiV-ZCSwBAoIdJSEQDI7ZigEptzAnX8G7aG3J6kptPRjqBGPXHLqNJLvY9fMtMm-tRVPgvGvYWngbCnyigevaFulRMBhkm76KDsGO03xBLaaXyiVMkekgHeuc-dOGcTPKtGXco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=BRYc3TlgTF9dMtqKcdkyY9I_8COKoIN11BJNt5FjF4vIDU6QombAWEnBuoGRmkAK-m7AIL_sA930Y6yMm9WlNYv3OHNzG_8S2YlUXcSJ_TsFEDv2tPKha_i92n5JKgmqbYjnswXHrpMuZJJ21XvfhbyDX7dP5W6g58yTO4Tx6JgTg6u0GPxQ6AskITyRmB0kr0gHf0vPfy1XGqBJ-gTzmO5_DRQ8WqGGBpVfvlyaQVXSgaevICSSYGge1BKstP2TPNUtMQ5nDtjp_joSjLa8WJ56WX-enmuNur4mVg4q7E6ucLLyCeWQrUhA4zrqaUp6iY_0zFCP42UUVTzzb76Uhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=BRYc3TlgTF9dMtqKcdkyY9I_8COKoIN11BJNt5FjF4vIDU6QombAWEnBuoGRmkAK-m7AIL_sA930Y6yMm9WlNYv3OHNzG_8S2YlUXcSJ_TsFEDv2tPKha_i92n5JKgmqbYjnswXHrpMuZJJ21XvfhbyDX7dP5W6g58yTO4Tx6JgTg6u0GPxQ6AskITyRmB0kr0gHf0vPfy1XGqBJ-gTzmO5_DRQ8WqGGBpVfvlyaQVXSgaevICSSYGge1BKstP2TPNUtMQ5nDtjp_joSjLa8WJ56WX-enmuNur4mVg4q7E6ucLLyCeWQrUhA4zrqaUp6iY_0zFCP42UUVTzzb76Uhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYOup_71OZDurpdVl4p_YSYnJpA_x31G4LeMSAs863nIqYidmRg73mNNN8rhlclBaZDbt3e-QXqPaMyMO5ADdhJLvIcPLkUa0kaSQeoucSvGTXxZ3tpqinDVvybKgGMguEepkP9hf7YrXF7cNWdHYmmdz9ykFgEzeyeyHTmKXQdUouvH_NuWkswkAqAWuwLQUij5piwsglqOSK3Z5W6p5HHH8yn7jlwK8HYYrK00rHzLDq6-T6JEnzPwxeIGrkM5S2iQ55gcGCi99PPbNVew-AHlBHiPEbrOQlihle_SKVnIeMzGD8Ycq3nDTxQC-KBN5HulrCzq-FSkbkIpHj3paA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=QwcVYu9yBKaJn3OuzkNxjI3s7apVAZyU_JEkArY5AmgrQ-oFxsRBuk47QJb1vNl1m-aZADNesMVlDuMmLfN-EVrp9sKMX6MnEmYC7DEzbV-4wDjtnhtoKvhpg5spUxwjAk6CjaIiDUHMkjqUT51qeUydjsCKOXgCB6IWB-N5B4T3auTcOHrKktkN9Q60OrsqLHiXsL4ewbyxdNHwMH1k5r4fctIeRz2UzCGLZrFM3RalPUq0OZnLDB4wD8mBLF4cAVAXVEyYBd8AtK-PQTQfdyTfJU8JilB2BpykJzF9XIwmzur_JDFxlOvYenrcCl_zuJb57_nzI34i62BZOK3fQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=QwcVYu9yBKaJn3OuzkNxjI3s7apVAZyU_JEkArY5AmgrQ-oFxsRBuk47QJb1vNl1m-aZADNesMVlDuMmLfN-EVrp9sKMX6MnEmYC7DEzbV-4wDjtnhtoKvhpg5spUxwjAk6CjaIiDUHMkjqUT51qeUydjsCKOXgCB6IWB-N5B4T3auTcOHrKktkN9Q60OrsqLHiXsL4ewbyxdNHwMH1k5r4fctIeRz2UzCGLZrFM3RalPUq0OZnLDB4wD8mBLF4cAVAXVEyYBd8AtK-PQTQfdyTfJU8JilB2BpykJzF9XIwmzur_JDFxlOvYenrcCl_zuJb57_nzI34i62BZOK3fQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owIURH0l8_--H7DP61mjf5O4-ZPEeInJutIAIUCjoKJP_42bwAYRYOlhE4GdZJ4Y3odHUKbgJuARJYxbQseNztv_B84QCdr8HSPo3xbF9Sj8qgZ-bXiD_qBBF7LdnRNUx-YRnpVSHSEShXI7pEabKtFENspFJuGWGGsWH2V-0pIZg_1bV6NoKn-9niRJJyFAdNlIEgBedYQufIR3TYpFw66HqOmhWCZCFsf2BjMumW-xosYGfms1YA_DhW2ez9axFTA8PuKUOfEcaXT4Jw-MFHtK2soUn1toSySMXuX1jFRWTb7Tf4Xdy1WS9Tc9qWsbtEm9G8xOHOCcR-Nsu5zPuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWKuga3Sp3ShN81RfvWtpZMHUam18yoiz8Lpt1oLug_IkXUUnGJZVoyqke0dT5eleRhp5lG9maiAkcHjncLfAkJdtDCIjVvYAxoiJ7vWDhkIEfSvQeRft_w8JrPETzsI4fwPUIdOBitzwcnQq1A9gdQiCHD5yItOK2Hlx-GrPLiTnzcuxH1-CwrMUB_e9p9bjkJHa6OKL4FVSQdMPs-u5b3wBtUddSMv8lfEu_j46719618yIAsGL4NYc2rFoDRQDWlED8Igfs-NAW5XEJVy5Rg9wbSfwxKRyi3fgTNs2MpTpS_gWRRW6Iv1Hd0EAQRsnsCFGZmXWZQlEk7OcChRyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=aVyHcA3FHhDZsbFXIYzmipmmFxMO6UJVJcIdIS8qib1yeqqZwI_e-HfP39W4nYr0QR4F4MRzIFyO-9QH8cHDN__4AFyMQ3mv_Uu56c-XaXmDWTtVFtaaxbbPvLcBExvYcLenPSr5wqaZQm1O_w3kNIIi9BmQvPg2J3eSdcNCI-6iAfRvVJElWyDEOHDAR9NLIZGE-nRDjsIVh0zgc1pu8ahhVlqKa3vRAIdjESdgIbeeC3qSnDVcwjDUcyYpmwfqMrQJZQt0rGm9uIQokUwvYl8uDNaVZW0TQ-1dD1d34z-1VqGvJ2pVZbD6DpmoPidcSRf2COOYTqj63NvZaB1iUWFoTEFynU3Q-rCoEX2iFaB5wqRO813kmyD1A4l1fGgC7rgFeB14g0RQtt5hlNqkP6oNM5vJGoIWgihK5iseARbd2-8pbTpeJbU3ZvDveAyBQ-ZsT-mV2GNIFp-xAdNO-XARfNCI9-tk9cQo4-GfyVxWIgMToz30WYEwd_OGx9vOQjdgd8YKxwhv0mKsOhTiAyxU9yeD942QZOwPOKjEi-8TC1parlYoLHv16jnnrOFA5sFjg9GtBie1kzSqXMkiPsDuDtR8u6KQUcyKYA_IR26CcZw53ChMvNWEsI7UIytEys9REV6wyuAT8YthyqHLLze-jWr619BKpchZ4fC_L4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=aVyHcA3FHhDZsbFXIYzmipmmFxMO6UJVJcIdIS8qib1yeqqZwI_e-HfP39W4nYr0QR4F4MRzIFyO-9QH8cHDN__4AFyMQ3mv_Uu56c-XaXmDWTtVFtaaxbbPvLcBExvYcLenPSr5wqaZQm1O_w3kNIIi9BmQvPg2J3eSdcNCI-6iAfRvVJElWyDEOHDAR9NLIZGE-nRDjsIVh0zgc1pu8ahhVlqKa3vRAIdjESdgIbeeC3qSnDVcwjDUcyYpmwfqMrQJZQt0rGm9uIQokUwvYl8uDNaVZW0TQ-1dD1d34z-1VqGvJ2pVZbD6DpmoPidcSRf2COOYTqj63NvZaB1iUWFoTEFynU3Q-rCoEX2iFaB5wqRO813kmyD1A4l1fGgC7rgFeB14g0RQtt5hlNqkP6oNM5vJGoIWgihK5iseARbd2-8pbTpeJbU3ZvDveAyBQ-ZsT-mV2GNIFp-xAdNO-XARfNCI9-tk9cQo4-GfyVxWIgMToz30WYEwd_OGx9vOQjdgd8YKxwhv0mKsOhTiAyxU9yeD942QZOwPOKjEi-8TC1parlYoLHv16jnnrOFA5sFjg9GtBie1kzSqXMkiPsDuDtR8u6KQUcyKYA_IR26CcZw53ChMvNWEsI7UIytEys9REV6wyuAT8YthyqHLLze-jWr619BKpchZ4fC_L4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ee4n8Z4q_pw1Ms5epf8nT1j8PflH86P5RWgKw02coZm71C40SfHTA8CK1ZBRkD6f5fLw_8mqpAgp-NnzSQbvddm8LdrXq00GPax_LEdBklw5MvDWdsONXXQkMWrkRjZe7tia-ul5rkBD8pC7NZSu1PlzSdcFDE6OzyGJWf8DoXwoutTJgupSvYILrBX7M-34VhGe7l1aqitL0LM0bgc-F1quuJM2hT1ngg6bAnk_7H_k70XTV_rWIDNZPSc8QvGzZRDylI1AMH4bqE0hfMOkYKpYP1PjZ_ADz68cIwu069NGY5g0F9yFarjg2_OPBPDQxDT-syKLL-SpNnq6_0iloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3H7Z8ta-OPHlIaxoG6ludJZsFc5kjiAOiOSlUvpd24dyDOSDCayUHC5--nmfC5K-hDqtMLDze9zHwnpAmBtx95JRUHbiYR79DaQWRrb50LcXPeHLyrSmqVIGLDFB817T4GuTLb1bgKOUS-Kn7Y6HR4o_P3gM0c-K_brknPLmSjSSzESvaNH2BIQKZ1F0z_kZNRhvOt3NI7DOXCzt3BQeU7O4wo6Mt5C-bawdLrDAJGUX3yHFn-rYq30tW4B2z2LMMQMpsOpKci8pe6YzW9sJpuAovGTh6ACOlnk6qckvRp-pa2s-Tb_izIashFHf1rMi_2pDEalTz9z3ylU_GCv3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=ZkAG80GvS9PS3_UwVn9TMpKypMI8pZkQyLe0Fsz-0yAItPuqb14PD7i0dZPVyFTziB-_j1inMse46MTKh74IeZf3bjPoYmWfmqNdrweQfq5vK9hO2Br1jQ_PSARM32kugQjtE9iYvohVVSz9QytpYmxFPBFouoGVUnksaNbreWngLDl7nMPoIT6DEtRzXrYi6B2R8QQEtlV-Yy8tTtV_Wi2oCHESc2rLN6WMvQxxQX0unGq8elfF10OF1S_SS7b2bKotQcSKC91ZHKRtRtNM97T5rYP-B4soSsSNB8VRWj_FOSJSDvF_QchxJDonDEyTjChyyxjdMQ8gAeGqkg0nqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=ZkAG80GvS9PS3_UwVn9TMpKypMI8pZkQyLe0Fsz-0yAItPuqb14PD7i0dZPVyFTziB-_j1inMse46MTKh74IeZf3bjPoYmWfmqNdrweQfq5vK9hO2Br1jQ_PSARM32kugQjtE9iYvohVVSz9QytpYmxFPBFouoGVUnksaNbreWngLDl7nMPoIT6DEtRzXrYi6B2R8QQEtlV-Yy8tTtV_Wi2oCHESc2rLN6WMvQxxQX0unGq8elfF10OF1S_SS7b2bKotQcSKC91ZHKRtRtNM97T5rYP-B4soSsSNB8VRWj_FOSJSDvF_QchxJDonDEyTjChyyxjdMQ8gAeGqkg0nqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=ZsNn8T4gLdbduGp_aQ4u2ocKhcFSAe25YqQpa-GR9QFGosU2qZydESBNN2WYs6QVt_m1Ujm6J6mKYtHtknv9mzpXGzZic5trX7m8h-Y08cjhLcRSQD3MQzMQFm2FIDuupu3aqJKZ7SQ2s7A11zXRXMhc2sCBzJbyM6cfKOJ3NQM1Nnb_EBT2i_BcsfoZBp84k-UKHg6qL28qJU392wyRTTgnZnmIR7WOVZQd_co28-n_bIryJoDFR16VM44QmmWP8aByiHNzqtsyB9HT4aSBp-vBDw76hpQObbfkyNxcMXU4m4SfcqF0mMAluQJIC1afd3HYlqCuW6x9ZWpqGid_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=ZsNn8T4gLdbduGp_aQ4u2ocKhcFSAe25YqQpa-GR9QFGosU2qZydESBNN2WYs6QVt_m1Ujm6J6mKYtHtknv9mzpXGzZic5trX7m8h-Y08cjhLcRSQD3MQzMQFm2FIDuupu3aqJKZ7SQ2s7A11zXRXMhc2sCBzJbyM6cfKOJ3NQM1Nnb_EBT2i_BcsfoZBp84k-UKHg6qL28qJU392wyRTTgnZnmIR7WOVZQd_co28-n_bIryJoDFR16VM44QmmWP8aByiHNzqtsyB9HT4aSBp-vBDw76hpQObbfkyNxcMXU4m4SfcqF0mMAluQJIC1afd3HYlqCuW6x9ZWpqGid_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=BpL5gFNVD6BNH9ak8Q5lzXseWPtlng-uxAF3ClEa2-dW4q7KWSoxlhWqOodJsxUvNsbY9kxchrfDesv-ED2xsLuLWZ5phQlHk_ZFsnO-36GEOr5QuHBjNtDYCo7QeBUKB7IOrKzJLoac4blTh-USTz7W-QZFm13B4B9N5gmbNkK9HVqv1I-uePiVwCIkhwoaJq5INR4PQTT5PKQ3sqNk4Uo0mWfP0drjifdKcKEEA0YU4NnFtQyTjjVvxgrLHjgP1tQOc0DDsOY6bmERFdYR-Fk2Nsm6jXxMBnnZDd_RozIcYleF5qRN9gHKV4rX8hTzhevyLQxFnC5NRoRbeFraRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=BpL5gFNVD6BNH9ak8Q5lzXseWPtlng-uxAF3ClEa2-dW4q7KWSoxlhWqOodJsxUvNsbY9kxchrfDesv-ED2xsLuLWZ5phQlHk_ZFsnO-36GEOr5QuHBjNtDYCo7QeBUKB7IOrKzJLoac4blTh-USTz7W-QZFm13B4B9N5gmbNkK9HVqv1I-uePiVwCIkhwoaJq5INR4PQTT5PKQ3sqNk4Uo0mWfP0drjifdKcKEEA0YU4NnFtQyTjjVvxgrLHjgP1tQOc0DDsOY6bmERFdYR-Fk2Nsm6jXxMBnnZDd_RozIcYleF5qRN9gHKV4rX8hTzhevyLQxFnC5NRoRbeFraRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0FJgOrcbwCoSZckjTEI-NJHqFUBK2q-RBJbgO_E1AJOORsON4p0TPOxzJogu9YJv4xrdTINMLukkn8OIIiKoVxUgLxRvBYTh9m9Wuk-UEv1C5SlQVSset2ScGtq2j8V2OQlEH4OJmWSCCpjSFkx5H4imvHramRqXRr-QHv4oKIrAi6KKNaQlcU-oJutxbZEBc63dONFsoD8RiDxEmXOK59gZA578XXkBOdexkbbDsqlRtqNTxk1U0VR8kIgBFzKms_J-ubGgJe6lWoq2AzO-zYFNPW-O1oYYAgVBFxlkcLeZl6BjolNymKSIGbzn1D9mtk0WQnjGqc28G0iSCFY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8Le8kAOHI1AVcd4QgfUwjOCHUT7CwCIRjBe0AbVAsMyGbFXfv9WZMvtZ2pa95jzxSvmQmYr4s6AFdi1WGWjbjFBYUCFzlyikBndlsaGgM2tAibsm3uTPvrGXwwCutldZcoL3ymo4CR73lLeQML-WxZaCwjz5OopQiFrZ3b6k_4mDzkuByGMlTqUh7Ics90vJBjU0iy0fJAKb_JCtsuCrM-z2eRieeBU58pDWS6PMZfDQqdobEJYUJ81DJhNz4ieV3p9cU4Rv7utupgzUp3AMaRTr-SqooQy8JntmmEjOyF_8N6Hh-7pkKSeGATOzN5VyfNv-KYgTiTPIofzQ4W1fR_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8Le8kAOHI1AVcd4QgfUwjOCHUT7CwCIRjBe0AbVAsMyGbFXfv9WZMvtZ2pa95jzxSvmQmYr4s6AFdi1WGWjbjFBYUCFzlyikBndlsaGgM2tAibsm3uTPvrGXwwCutldZcoL3ymo4CR73lLeQML-WxZaCwjz5OopQiFrZ3b6k_4mDzkuByGMlTqUh7Ics90vJBjU0iy0fJAKb_JCtsuCrM-z2eRieeBU58pDWS6PMZfDQqdobEJYUJ81DJhNz4ieV3p9cU4Rv7utupgzUp3AMaRTr-SqooQy8JntmmEjOyF_8N6Hh-7pkKSeGATOzN5VyfNv-KYgTiTPIofzQ4W1fR_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=QUfS5s5pyGKu6lIyLN6sdIL-07kMd9VFLTDvPTa8LceyepAChucVHBKcK8w0N397TymSR4jVYHwJhf6ugY5TpHgLkE5CLdc3kR3jkupUm9UeKHB2UDxKrwxZviKqJrN2EoaE-jNJmVHK0QzGAKhRMhRx7Tu5sIJPYFXaAC-JVmFpHX3GZc3d3eJ2kqhP40W9qZcj6w9Sfsn3fYbtqiBBxHQ9HyR4GE46lpuSjK76DmBfVlFgv7RXzM_z4Fq2zd3yxPp-DWv73e-SK-U33dHeKpkV4cFatGs1pnd9jVe6phW5PJ6HsKlL-gfQfrsl4IqslRCw70GvYKmLQ85r_l9eCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=QUfS5s5pyGKu6lIyLN6sdIL-07kMd9VFLTDvPTa8LceyepAChucVHBKcK8w0N397TymSR4jVYHwJhf6ugY5TpHgLkE5CLdc3kR3jkupUm9UeKHB2UDxKrwxZviKqJrN2EoaE-jNJmVHK0QzGAKhRMhRx7Tu5sIJPYFXaAC-JVmFpHX3GZc3d3eJ2kqhP40W9qZcj6w9Sfsn3fYbtqiBBxHQ9HyR4GE46lpuSjK76DmBfVlFgv7RXzM_z4Fq2zd3yxPp-DWv73e-SK-U33dHeKpkV4cFatGs1pnd9jVe6phW5PJ6HsKlL-gfQfrsl4IqslRCw70GvYKmLQ85r_l9eCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dl7F9Ib-L6QZPNvHd4OC2BKylo6-xGB-go9Wm6K4i9AvmkJb5CwTvjBaqLm6To8_uhBPLJcAHnW5gL6gYgS6zTq6c7jYvShQDgw9uDo6Pl0d4ReRtHkslmGg_ELs8V7M2UQVziSbWLGLML-6TlDWStRT9X5-Vw6QdHwZ7rLAbO1c1huE6eN0Q0fCM-RpdsewHGNQAanXD8Ozd1ao9GUd-sFT3AcOoIRv0MbbH-0KF3VHzclGQ1hm7oVW1am_jNh_410wvJ5GKSeqggEvum7cHmBUrLnYVX-PIAjdx243J_9sNQ6uFaFqc1GwJGKH0mbzRMS57b4O5MFh6aTQKAbLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=L52YHdeKVhAw_D1PK3G9pIn616EUsWSwe-Ij9saOV_nR09CIRqt36pn3RQwvN-xWVw83GU2aco8Aal_q1jYq0JigMlbtSQgPjy9cxY2yoSFVC-A9OxG7BuQkTcWOL37dxU4tMMopwR_noK63uzEeYSf-sqGD7R3yYSSuTGJEZVtFwZfBRU-NTsDIyrBQmgOSPqmSfZ_QZChTH9C7IZg_NU7e-DNPDv0kFxIIWv9g97IvN_GUKcn_5vgPA2qndEeW6xgliXv47gq8QoplN22Kjg_bSERCk-YZ97UI3HTJwTFbQuz88sFI07U9hNLx2ddvTX7rMvz9GGDUkldLGxa4eDwH5dz3CmzEhzuEQI0QHMZNK_QN3kX-mSC7l4fqPyAJj_J8UpoTKtU--kF_-1r6GDCko5eXEma3KMEu15Pk2gVLSZzt5uLG31KHxD9l8u5z_z7zUWCVmYPTVXZ_v4Omt-u11PzR_iPGwW28RPt3WOPDCKIrlQHdFcCtxu8zW1IxYc7MFjVwpdqop3G8KAZfvzf1QN5rCSYnPGNBMzcUvqLpBXKl0srPxhgbFAsKKZEyaAzYk-9E97keZcklgV96XiXyEWOp_yCeJ5N0POSb9PbQjr7so2PW_5OqI8qBoLtSq5jnBxbuDuTIKU26Yfg8VQyUpQk4TnbSBnEfT1uw0kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=L52YHdeKVhAw_D1PK3G9pIn616EUsWSwe-Ij9saOV_nR09CIRqt36pn3RQwvN-xWVw83GU2aco8Aal_q1jYq0JigMlbtSQgPjy9cxY2yoSFVC-A9OxG7BuQkTcWOL37dxU4tMMopwR_noK63uzEeYSf-sqGD7R3yYSSuTGJEZVtFwZfBRU-NTsDIyrBQmgOSPqmSfZ_QZChTH9C7IZg_NU7e-DNPDv0kFxIIWv9g97IvN_GUKcn_5vgPA2qndEeW6xgliXv47gq8QoplN22Kjg_bSERCk-YZ97UI3HTJwTFbQuz88sFI07U9hNLx2ddvTX7rMvz9GGDUkldLGxa4eDwH5dz3CmzEhzuEQI0QHMZNK_QN3kX-mSC7l4fqPyAJj_J8UpoTKtU--kF_-1r6GDCko5eXEma3KMEu15Pk2gVLSZzt5uLG31KHxD9l8u5z_z7zUWCVmYPTVXZ_v4Omt-u11PzR_iPGwW28RPt3WOPDCKIrlQHdFcCtxu8zW1IxYc7MFjVwpdqop3G8KAZfvzf1QN5rCSYnPGNBMzcUvqLpBXKl0srPxhgbFAsKKZEyaAzYk-9E97keZcklgV96XiXyEWOp_yCeJ5N0POSb9PbQjr7so2PW_5OqI8qBoLtSq5jnBxbuDuTIKU26Yfg8VQyUpQk4TnbSBnEfT1uw0kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7RTrFKhZ-v-S0vFEalOrfyfeKYIkwIZkfmkHoOjd0YnQrTbBmN2uubwur4YoocBjCokkRrNCH5DQ2EvVutytvP2BlBheI_HE0ukYgakzD23nxxrmh5AOQwKOepQu4Om6OX64RQ_WzDzHHQAhnxM22VjfKLJ_e-f7O2KkrN5syuU4dS9X8mggrgrtMAuSXco70uwuh_q-IJOsBet6753wEc2TgNZXi-5wo9HZZdqtCFIjJoEACiMi7pfQANacPMqcnh-2Kb0kbXfTuUKSbdP8hyQcGxR-TtCps1NUvoB25ei_iN6oQkFeHztTp52TLOqFdBLdkSIW91IXl1h-lvMTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=cYtchKJWcAT0la8oAR4g_ujGaX0h_IX4ORnyTLbMVQ5K5blOcpHFysLt0AYb9GNF3F2pCRP6d756k-4pG82nnHYDUxvYEgJcVuZCjK1PiJPVjokNAwjB3rUKpXxxGLJJrUJ6JytjktL5K0deFWZB98rHRVrUEtm53cecP23IJiA92c3ImR71Be4RsBPRZkct8v4CeTalrOY_dDge_HEwXxvHgUDkgTt-bUzWc89pDSLGDtdwYLcYfBZ2NE3cOdLFD0Z66gDhezYi30VTMnRk9C0j7w_gBmxhaa5kAf0FoO7r3Ew6NBAPU27xVBPOBq7Z42I0Xat4WH52oJxCD0C9BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=cYtchKJWcAT0la8oAR4g_ujGaX0h_IX4ORnyTLbMVQ5K5blOcpHFysLt0AYb9GNF3F2pCRP6d756k-4pG82nnHYDUxvYEgJcVuZCjK1PiJPVjokNAwjB3rUKpXxxGLJJrUJ6JytjktL5K0deFWZB98rHRVrUEtm53cecP23IJiA92c3ImR71Be4RsBPRZkct8v4CeTalrOY_dDge_HEwXxvHgUDkgTt-bUzWc89pDSLGDtdwYLcYfBZ2NE3cOdLFD0Z66gDhezYi30VTMnRk9C0j7w_gBmxhaa5kAf0FoO7r3Ew6NBAPU27xVBPOBq7Z42I0Xat4WH52oJxCD0C9BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7E3V1OpvcFtG7aqSYiGQPqZH1blKlXembjCxLPl4-nEj6veHbFxaAlidbYtQN0WlZ9MiiQi2IjJTzKRN7Sf7hyCp96uXrPR6TgozyyDlwzauF9_irTsuTSvn-QNEx9wLtuu78jl2lTl4uwB6kz0tV4_a9OLYUWs1i_0BMsESbGBWpQpbIReslvfVIymn1U7ta4GH1g-VH3dHGdZ-YPzylejlvz4LP80unEfwMO0Ft-LCq0Hz260rJB3RD4ZoP1kx2uPS3pb0RwKqPzfOTFEs4wE1dBvxD2b9kqiiFOYT1FIjzrJ7r_-7RFmBLSnVVcEick3RaR3m3P53eQ_Bc2wvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIa2_o_Kok9H9E0OczRhwe44dXUapF7F_jS9clz_S2JpqU5qjBVrvfbgfDalHNJrtbzLvsDdZzh8fvp_1xA-rctWl5Xp1wg2zpgQnEAzInEt54bs3Ni37bYPB0JEL0WFb6kavB4IKEzjmmECCeo01_OL8s2O4tqDMyooxKGNeq6P_hLf27wEnmG4RBJvilpJMvE95AlasgEVWeVGl-WTD3qJTX5gmm-9-EpnH-1gQjv7kDXjZky63nsanmJMWw4aSRStmDVxkLPz3b2tRPtq089BXZY-RHZ5MPrnkHZQewnPbNiJQFnSXIOchXQ6MPKEehwC5pWdi1zXGnXIAKbWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqTfw1wW6lUKMFTU0MdmJJoNC-d4FTO_hCNxUirejWbHw2DQUAJfKLjzr5TCPBjzKc5m56BgSguU0LzRNxdnUMhNT_nqrMzwBWB2nuT5LCwhfPRbanX6XIBawlEoiZblDy9vdI35954JgBY4l2VvztX5evifEL_rNwFGr5SbveYLSxtzlXwc1sV6DfW_3ZfPk1sB4v6ycxo-uDq6TS9NQwaMs281acIQNI7KV-49bM6FcF28UOnsVr4570MiPJfPP4yOJBsvo71UidFswt3B8UWydjVFtURIZBSyM09bgiFPEVLFeoJVPZh2oBnVZBkY1IB3843yXwZNG09KyA9Hlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=s_I0aGuinWjic3zWTe-2UKTjwKxC2ML_I-ZMzyv-rSFXDPOWtPFb8D-5vOayZXcla_mYdi8uPeuog_fhlGIIJ8QsWT_nu_eJ5dwHcyLwxexuWYeO5DYQSb6eKqUnBNN3G9Aal7uFtdH6EtlbWtwrjjZzroKtJ5r8M5IMA_oCuN6Lok_9qfZXu0jSyYVwdaVxbgn2UkTzAR77Icoq4ZVqGys9thBpGuAvpK6cpAAQRWZMrf278UGmD7NnhWK5LKPBSTL_pSNvaDrHs_bpzmtSItUTzGkKb9kFM9JzvBlaruT95rOVJSmAfxHjRORKitGKGsTE0B1EmuByZBrcSIp0zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=s_I0aGuinWjic3zWTe-2UKTjwKxC2ML_I-ZMzyv-rSFXDPOWtPFb8D-5vOayZXcla_mYdi8uPeuog_fhlGIIJ8QsWT_nu_eJ5dwHcyLwxexuWYeO5DYQSb6eKqUnBNN3G9Aal7uFtdH6EtlbWtwrjjZzroKtJ5r8M5IMA_oCuN6Lok_9qfZXu0jSyYVwdaVxbgn2UkTzAR77Icoq4ZVqGys9thBpGuAvpK6cpAAQRWZMrf278UGmD7NnhWK5LKPBSTL_pSNvaDrHs_bpzmtSItUTzGkKb9kFM9JzvBlaruT95rOVJSmAfxHjRORKitGKGsTE0B1EmuByZBrcSIp0zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1WWgkybIlrBe4qX_4gIK81gl7IiqkRG1G5r3v0qToDeNYh-dWPu1PCEGMovwdHJ7GK48gzsj1L4yXMubCSfuT2Q_jSYn66OnEAqBan77wBVgcmc7wFQaDIER2Xgk-ntrScB5Xe9TN3V4xKc0gWzwbCZC1nFdYpkwiqWfNrrI_xswGFEZEjnWVXYnvi1s-bqKQz1NO7JelTiaBnYgc_lqehBGA3T7NNX8yx4ALAezkaSKP-oNcs_ZldRg96GwsqIL13jAD_ONEuPesa7fu-UQOyqseZjMyn2vy1brkaXrF7f-0KgtmRMoByg9hSxyKBOXzrpb-QQNKOXZ-607B2wSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu47HAo9yTwLU1-sS_cHwm7Mq-5yWriMCup-wQppYltuqNN5sDT5T05HF708xNy-iXbudRO_owCWbffYUYINqa3oFrjIQcb0ZDDZVbxUW5v2hRhJJMX7hOUmW92oaxRHSDaruycGSh7t7Xo7rj3DJE80aOWm1hambd_NCmeCxHl0y3hPswRK27InavdM3iYxphRB2EmV8a7FXv3e3Dgnbi9A12SDXE1NMR9UPYvK3cCsXgip0_82ASPNNwEZU2dB_FlPKzPsGBLsoRVLUqWHKYIANDRYPfMWmMKZLprw7alDgHOAaLI5b4LQ-hZqMBn3UwlYC7RNwZ9cvjDfxO0Yf5_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu47HAo9yTwLU1-sS_cHwm7Mq-5yWriMCup-wQppYltuqNN5sDT5T05HF708xNy-iXbudRO_owCWbffYUYINqa3oFrjIQcb0ZDDZVbxUW5v2hRhJJMX7hOUmW92oaxRHSDaruycGSh7t7Xo7rj3DJE80aOWm1hambd_NCmeCxHl0y3hPswRK27InavdM3iYxphRB2EmV8a7FXv3e3Dgnbi9A12SDXE1NMR9UPYvK3cCsXgip0_82ASPNNwEZU2dB_FlPKzPsGBLsoRVLUqWHKYIANDRYPfMWmMKZLprw7alDgHOAaLI5b4LQ-hZqMBn3UwlYC7RNwZ9cvjDfxO0Yf5_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=t-hpjYlity8HnUseIf08RGN_oqEyzICOOzjxUQPuEPhnUdD1euH0djNncid0dDAob9yxHiIx4x5BcxZWc_mVjfnHHHhn0lV44t2R_qBd4eADjAlBOzMCIi2XJjf1xexC2XDKDcKE00SaLjsxNxMBlyVgNm2VEZci8MsV3PnU1wCtzDan6d0dGbmWPFAlTJALVbxognU4wZekAnf9sMSzqDdjKKN72jhXesTuWfYuKIbgvs2EUGSviKbbfBLNPYhk32Z0OIkZ6GLCh66pAmBnF7CkKUKAMTmuVPihVapVqRFQ55JLXsMgDNg12Iq5wtAGXNICjE7rhK4i1M_VaXUOIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=t-hpjYlity8HnUseIf08RGN_oqEyzICOOzjxUQPuEPhnUdD1euH0djNncid0dDAob9yxHiIx4x5BcxZWc_mVjfnHHHhn0lV44t2R_qBd4eADjAlBOzMCIi2XJjf1xexC2XDKDcKE00SaLjsxNxMBlyVgNm2VEZci8MsV3PnU1wCtzDan6d0dGbmWPFAlTJALVbxognU4wZekAnf9sMSzqDdjKKN72jhXesTuWfYuKIbgvs2EUGSviKbbfBLNPYhk32Z0OIkZ6GLCh66pAmBnF7CkKUKAMTmuVPihVapVqRFQ55JLXsMgDNg12Iq5wtAGXNICjE7rhK4i1M_VaXUOIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=t5Rkn_KTJOOJT2w4-3HOxOnk655V7pseaF-rfJsDnd5C_JHFXW4cu-6-VBp_GE5aSOBAL9e4zW9sQtss5DfKDuMK0i9VXG6rgXqQ__zSmGEkOOcFawbS2DmlHnr29B43inCNuM7iOUfHmWuEKQUlJKgKTUEHO4bRakhtNDU3C4CcLEcnaRe7pjJ0F48YLID16JgA0GV0dN9vNKJ_34W4W9MK2YAWEL2DyPi12XURpsS9T60s6XSQaMM3gZ96Y-mmFmJp3GlEQ32KDhLuWo4cbxrTUIdmiWRjFrF8XuiQqQkWzDNiJN-aVE7Z_eRk4NG5HbcZAJXtStXa2UXfnkN_tykWL3-hfjpH-YtqUZBqQPC7wJYm6OB0_5zsEKH72THuPdHT8Sq8M_q5_VYbypyb0nFbMFMK86BIYIYWNX8Qlxy4Q1PFN5xqgBoyYql3Dy6g00-d2RCK3ZfXJnjv01ktjJj4dLNwpmB1TCes1PCevBVMVBhdkIDhJW2Cl06sWg5WDe4At5tFVMYggGYyvAzghUGmbrOwuccFbKsLGZcHTI9T0GvxFGvLFxl-K8hC1Nm1JPwfW48aEVwGkTWKRNOtWENCizfZPmHnm9wmeo58wnNIJlfjsBaYhN731PDIOztzOTmAvwIByRlJACxQ8ueLPxTXecZZQZ81MiPgM97mSFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=t5Rkn_KTJOOJT2w4-3HOxOnk655V7pseaF-rfJsDnd5C_JHFXW4cu-6-VBp_GE5aSOBAL9e4zW9sQtss5DfKDuMK0i9VXG6rgXqQ__zSmGEkOOcFawbS2DmlHnr29B43inCNuM7iOUfHmWuEKQUlJKgKTUEHO4bRakhtNDU3C4CcLEcnaRe7pjJ0F48YLID16JgA0GV0dN9vNKJ_34W4W9MK2YAWEL2DyPi12XURpsS9T60s6XSQaMM3gZ96Y-mmFmJp3GlEQ32KDhLuWo4cbxrTUIdmiWRjFrF8XuiQqQkWzDNiJN-aVE7Z_eRk4NG5HbcZAJXtStXa2UXfnkN_tykWL3-hfjpH-YtqUZBqQPC7wJYm6OB0_5zsEKH72THuPdHT8Sq8M_q5_VYbypyb0nFbMFMK86BIYIYWNX8Qlxy4Q1PFN5xqgBoyYql3Dy6g00-d2RCK3ZfXJnjv01ktjJj4dLNwpmB1TCes1PCevBVMVBhdkIDhJW2Cl06sWg5WDe4At5tFVMYggGYyvAzghUGmbrOwuccFbKsLGZcHTI9T0GvxFGvLFxl-K8hC1Nm1JPwfW48aEVwGkTWKRNOtWENCizfZPmHnm9wmeo58wnNIJlfjsBaYhN731PDIOztzOTmAvwIByRlJACxQ8ueLPxTXecZZQZ81MiPgM97mSFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=Jw5DbkIlds4vkivu2Q7XjmHhqgyZE0XUS6Z5BDrRW3bp_EkfIPyzz1KFuhoDfB8gkomZF6uBIR4oDTPCpVx7enduPzZZGdFFH5aW6tyiMK7FLnU5DBNCd-JCwAVFwrMa-fHsV-kcD3t3qQwsT9j6r0rleoD8kpWfvmQcpUUiKWjjhTv2yW3hb6zBcvYSP6DWZQSGJpxljaWfiDe5aVYIet8nG3dZkBLdj4NRsdmSpH_YJA4Zlcp8rJoUK0mPqPhDrTFjLqkXYGpVSr7XA548OiSipmloca7HY-ESXaQhPC8Z0d5A801m6zmhJKUikFjBXyqTuR23D3xruzc55oZbHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=Jw5DbkIlds4vkivu2Q7XjmHhqgyZE0XUS6Z5BDrRW3bp_EkfIPyzz1KFuhoDfB8gkomZF6uBIR4oDTPCpVx7enduPzZZGdFFH5aW6tyiMK7FLnU5DBNCd-JCwAVFwrMa-fHsV-kcD3t3qQwsT9j6r0rleoD8kpWfvmQcpUUiKWjjhTv2yW3hb6zBcvYSP6DWZQSGJpxljaWfiDe5aVYIet8nG3dZkBLdj4NRsdmSpH_YJA4Zlcp8rJoUK0mPqPhDrTFjLqkXYGpVSr7XA548OiSipmloca7HY-ESXaQhPC8Z0d5A801m6zmhJKUikFjBXyqTuR23D3xruzc55oZbHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abxdvl2dqu9nozj_0PNgy4Hqytnsv52mi5E80rBd3FCQ-1JKs7gdAXyNdU7hvMPSypWh-AvSeK1XFcctYi32pwIG1vqufqm6CUB2w3J-P8oy0QkJ_uZvGNuSxsvO7AQOeVu1zuJer3xk06bFwSBpmcaARZsqU3gKQh5mY10sz2euHk8DWcXnolZT8FcZYp8nztcWH-rz5nfDBLujsPB6JenWTvsWg7H3beIUjaU4n5lxXrCxU7uMRjRxELQrUCRREvikl6bjHvQKvq5KLmw3RMQPxICGd5XlNO3nwYlHxta069rUOQTK_cgg8nDCT0VVyVnGUz6Vd6fgmLfJFcv16A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=tX_1GSAHVVOl2UEzzqZPpJckWvaZg7a3-IUjptWe5qdMP3_My1dNkkqkJDex8ZpnqdmSRE6fDSoFggf3ABJHfdE2pfVDATQVG1sjS6mNIJ7iBD27rn6jb4ykfErwYCSh0kI2Ap5eVA47lgdg6B9ifgMQbY8XRMB7_ogCvBmbKhdpuusR-pptFEj4uIZiw_Gu-ilP2qVSCzTWiVJIeXvbmU1vepnmsdqaz4gdVwtkABbpgu0FGN2uhZm05JMLBqyhh4phLNPx9cphevgO_jc6RTC-qDsMVvMyPG0nphIa-HO9pa-lhkgQDo1pxeT2y6tXF3rmUPDsOHCok2cuPLJn1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=tX_1GSAHVVOl2UEzzqZPpJckWvaZg7a3-IUjptWe5qdMP3_My1dNkkqkJDex8ZpnqdmSRE6fDSoFggf3ABJHfdE2pfVDATQVG1sjS6mNIJ7iBD27rn6jb4ykfErwYCSh0kI2Ap5eVA47lgdg6B9ifgMQbY8XRMB7_ogCvBmbKhdpuusR-pptFEj4uIZiw_Gu-ilP2qVSCzTWiVJIeXvbmU1vepnmsdqaz4gdVwtkABbpgu0FGN2uhZm05JMLBqyhh4phLNPx9cphevgO_jc6RTC-qDsMVvMyPG0nphIa-HO9pa-lhkgQDo1pxeT2y6tXF3rmUPDsOHCok2cuPLJn1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=b3oZhd4xZoPXyGEe99pJQe41Odfd2U8zSX2pOIHfHndhaBivyDX-65dHLIhx2omxyZN9M6UB4GZkOA5jSFyXChmW_PF4yZEdYMSXYZQoAyJ5DJf8vOaeRlx62gxP2LwinT_26QYbNFyfAUADOdifK4VuXkQk6ohSM1Xrv1L6ft_wPPxglHIz4sfzbhqrPTZLoKddVfmyJ77Jb67tF2ldmBpCEncHC5qodC3v88QCZ5ZwXcfBH2tSSrZ8gjtHb0XkPF8x1iog-g5gRkzAvGh9BBUjiif_jlPBt-fUHYsf5jUusUXYVq-DZLCGfzB6G-gvZA8-1esN2y9D7hfMSo-6K2x8nU1UVd1OiJ2cJyHePmFfwXtXETBKQsvVc8V5ENR-efFtpOd_WTUF6BezlbM9Y6a3WhexlAOWTOiK6iGrIhLplb0NcZKokeTMjJBWFLWkgbn7LbYmXQ--86v4KU5OLL-jA-7uy_JQJzJusUMeblGSnxZs0YS9ta2RXLUcWe0wfoXVBb5dF7jNOVTFzTv_H8r3aUolDciU3f-JqlT8ZFqBEkVC1PfyaagQDuWKQl1vYhJtYZ60ZmQakcywNb4ubITd4PQR9Jn7zOLrklPvCFN-LHpaZSSMbH2-Q9m4YY_2rYxM6mYDwZjCTfWMzbDxmIKIgvFneOaOMAKPahWmV_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=b3oZhd4xZoPXyGEe99pJQe41Odfd2U8zSX2pOIHfHndhaBivyDX-65dHLIhx2omxyZN9M6UB4GZkOA5jSFyXChmW_PF4yZEdYMSXYZQoAyJ5DJf8vOaeRlx62gxP2LwinT_26QYbNFyfAUADOdifK4VuXkQk6ohSM1Xrv1L6ft_wPPxglHIz4sfzbhqrPTZLoKddVfmyJ77Jb67tF2ldmBpCEncHC5qodC3v88QCZ5ZwXcfBH2tSSrZ8gjtHb0XkPF8x1iog-g5gRkzAvGh9BBUjiif_jlPBt-fUHYsf5jUusUXYVq-DZLCGfzB6G-gvZA8-1esN2y9D7hfMSo-6K2x8nU1UVd1OiJ2cJyHePmFfwXtXETBKQsvVc8V5ENR-efFtpOd_WTUF6BezlbM9Y6a3WhexlAOWTOiK6iGrIhLplb0NcZKokeTMjJBWFLWkgbn7LbYmXQ--86v4KU5OLL-jA-7uy_JQJzJusUMeblGSnxZs0YS9ta2RXLUcWe0wfoXVBb5dF7jNOVTFzTv_H8r3aUolDciU3f-JqlT8ZFqBEkVC1PfyaagQDuWKQl1vYhJtYZ60ZmQakcywNb4ubITd4PQR9Jn7zOLrklPvCFN-LHpaZSSMbH2-Q9m4YY_2rYxM6mYDwZjCTfWMzbDxmIKIgvFneOaOMAKPahWmV_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6TH__hBFfTGrrb0SuZyhT3ObxBxXx80ROj8kiWNGN2q4Lj_jyIIUF56iPQ6uDlID2b4xnqPQAwPohEzQnvR5RnM684ngrfGdGRrorLfRiV9THmxIYGbPpB0js3omNfrjeL1XTg-DJlAHy0tHiQrl6HdAvnSbxtNA3nfFLN5J-qLje9woIIlgVHk7IJx-mZcrSrsS7g9kYKb_Fvw1swDJkkrz19Y4mofLi8PS84IRpYuX3BgkPKFulATvzGL7iYOgOh45IUeSwk_hNwLX8DXYTIo3---Dqd8OjKMOB0v-HIfcGYzVVmwSz8gl-S25uL1UN5ZvXpR-_MljWndI1dTFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=dEMfCCr8IxjZ-QpdSZNT1D4acNLBmzyatS8V6gYKJX1_dHAwOOWuReX81ts_vNyRzPLjALgn8oJf9OT9jJWS6YymmxiqDUfGjeBRqoj8bHE4o4roVkCSLdbapjk19-MNbejBPAFaDB5DTXiBUIBpRAChJeMQPE4ZCz0DxaLpRLw1xQQtaQsPRF6UBeytQ-VDytsFkxa4g5CPpvfzHnxwE2aqLbohfPbdIuCde7JdKPH_zLY1egBjWTp-qkfX9D2vrwZbWnmZ8FbcV0Wb85PAKgjSrODPv-ICXN8us0Ezcvu9FqpAjNodBjMOm7gryqphizo0clCwpnNnznppTPEDd5d4PzOm6rHR8WvKiXyt1hLENfS7wMWoZXmbyHDOFeB7gKsnoBV-bParG4miXQAzJocjEFvMUX3usX47qpLUwHGDIeOzLm2ZNmGDhXHdbP_q8vFEAFoIKbYGAtTlnb2c1nStkxn-vsS6oAX20FIqsK5M_r1nA_mDDtGwlzgfsSymI_tj5FvnUXBckzV0apZlmOMkGxCVJ_A5QTQ3YxNxy0_gp78mXgToCwa-zeCbvbggtI0sUoA2CLwQwskHyd9S6VIdnFEsqn57LzJKVZGVxOyaCMB0ZNfPvoksTXN7m8LE0iIOh8yrA99_PV9nkXy2I1NsyMdwMTl3WOeTEHXpykU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=dEMfCCr8IxjZ-QpdSZNT1D4acNLBmzyatS8V6gYKJX1_dHAwOOWuReX81ts_vNyRzPLjALgn8oJf9OT9jJWS6YymmxiqDUfGjeBRqoj8bHE4o4roVkCSLdbapjk19-MNbejBPAFaDB5DTXiBUIBpRAChJeMQPE4ZCz0DxaLpRLw1xQQtaQsPRF6UBeytQ-VDytsFkxa4g5CPpvfzHnxwE2aqLbohfPbdIuCde7JdKPH_zLY1egBjWTp-qkfX9D2vrwZbWnmZ8FbcV0Wb85PAKgjSrODPv-ICXN8us0Ezcvu9FqpAjNodBjMOm7gryqphizo0clCwpnNnznppTPEDd5d4PzOm6rHR8WvKiXyt1hLENfS7wMWoZXmbyHDOFeB7gKsnoBV-bParG4miXQAzJocjEFvMUX3usX47qpLUwHGDIeOzLm2ZNmGDhXHdbP_q8vFEAFoIKbYGAtTlnb2c1nStkxn-vsS6oAX20FIqsK5M_r1nA_mDDtGwlzgfsSymI_tj5FvnUXBckzV0apZlmOMkGxCVJ_A5QTQ3YxNxy0_gp78mXgToCwa-zeCbvbggtI0sUoA2CLwQwskHyd9S6VIdnFEsqn57LzJKVZGVxOyaCMB0ZNfPvoksTXN7m8LE0iIOh8yrA99_PV9nkXy2I1NsyMdwMTl3WOeTEHXpykU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Emo312-sbkzBABsl5paCJdFa1f170Y96dZB0qeQwniSszSq6KJAVlXcnFFgkKSEFdt2XDGyCGK_4AONlxlbk8pAbSruLu8mGtg2VSn-y7r_3Xah--q1wKqroRNPG4h6ZIyUq_muf7_a3nJXOus9LfDv4Kqn5eObiBB2FvnBXzwQOJuLSOhJMPAloQ8jTTBJI9UT485AawEXBLTrnJoDEbXxwEI1DYApea5Yw3meWnhDd32yn2YLIfN5jto2yswXkfgbBYn3XVhwUepvNy9rPlxteXJ-PGtFyGhbMiyY_qh9WR24UQdKLJvfuosleImzcjTrG5_n8JPUW05L6u5SRNmIDIScx9J63RHB_CuIdByiNABmyuad-c8g5zEgtN_vZ01WW1BLAsLZ9Q83JnTeJdrsMaCOVD486pDNArzQ-P9Aw34HqUCNhzF1XJWmjSpS_YtW0yGitrUwMuaLpT9jr1TLbqX-z5R4iAQuGqRrzSit_E7Bq5STRDKSMncQMsAN-wwzM2jqgoNx3RdQhlx39w8joORkj3Q_aNJQLJhZYBeAY4xdLiiZqoSk7hZGUiOJswXRjD3up6okLa2hnzscXjjyGyIVL7_yFo_e9dbRrZ9B2ILBcazx7wiUz8uV7EO-euGZPnPQoU5dwFxR19jJfvQ4FBgGP1xiOdv8naevMIUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Emo312-sbkzBABsl5paCJdFa1f170Y96dZB0qeQwniSszSq6KJAVlXcnFFgkKSEFdt2XDGyCGK_4AONlxlbk8pAbSruLu8mGtg2VSn-y7r_3Xah--q1wKqroRNPG4h6ZIyUq_muf7_a3nJXOus9LfDv4Kqn5eObiBB2FvnBXzwQOJuLSOhJMPAloQ8jTTBJI9UT485AawEXBLTrnJoDEbXxwEI1DYApea5Yw3meWnhDd32yn2YLIfN5jto2yswXkfgbBYn3XVhwUepvNy9rPlxteXJ-PGtFyGhbMiyY_qh9WR24UQdKLJvfuosleImzcjTrG5_n8JPUW05L6u5SRNmIDIScx9J63RHB_CuIdByiNABmyuad-c8g5zEgtN_vZ01WW1BLAsLZ9Q83JnTeJdrsMaCOVD486pDNArzQ-P9Aw34HqUCNhzF1XJWmjSpS_YtW0yGitrUwMuaLpT9jr1TLbqX-z5R4iAQuGqRrzSit_E7Bq5STRDKSMncQMsAN-wwzM2jqgoNx3RdQhlx39w8joORkj3Q_aNJQLJhZYBeAY4xdLiiZqoSk7hZGUiOJswXRjD3up6okLa2hnzscXjjyGyIVL7_yFo_e9dbRrZ9B2ILBcazx7wiUz8uV7EO-euGZPnPQoU5dwFxR19jJfvQ4FBgGP1xiOdv8naevMIUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=uQqSVp8vyLSilhGReJI-sTq2O6S1NxcjkBpvdJvIklEjTJ6GOGKMaRIBz-IodOchnyoSI196bhL791c0dL9N5zrHYPTZC8Jt0PX15PaZhb_1G5eWCyZueuGquCsebKqvn5PhcUVCQq86icdljye1Z2_AyY7OC_3Qdy6L8mO-h1B-QzfrfBRp-m0SJOqARsNicL-cz-1bNNs1lYdBewJUikCNvPEsHtOAhBLiv20oAZBzVhWZweEcK0GbrVk2DHkI2JZ5Gde3KzTpjIutqJdAwzNKifM9PrZeO6Rey9TwvvRSfbKNUXlkWd3fPGalQMxoKF_Wc1fHJHDAfKsOVUg1tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=uQqSVp8vyLSilhGReJI-sTq2O6S1NxcjkBpvdJvIklEjTJ6GOGKMaRIBz-IodOchnyoSI196bhL791c0dL9N5zrHYPTZC8Jt0PX15PaZhb_1G5eWCyZueuGquCsebKqvn5PhcUVCQq86icdljye1Z2_AyY7OC_3Qdy6L8mO-h1B-QzfrfBRp-m0SJOqARsNicL-cz-1bNNs1lYdBewJUikCNvPEsHtOAhBLiv20oAZBzVhWZweEcK0GbrVk2DHkI2JZ5Gde3KzTpjIutqJdAwzNKifM9PrZeO6Rey9TwvvRSfbKNUXlkWd3fPGalQMxoKF_Wc1fHJHDAfKsOVUg1tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=macUqn3VI5N8yZYxlaWD8LpXTdSy0i73KTbn5J5DoyR-0LcdQohAtiw10dZneGJZMVnRpWegREgspm_ztE5J52BYi7nfRDLhpYW4vEC5veXTldDnUCBUTNNYHCDqcFMGRubnT3CfSWOINXBv37VKjPuyTurDZWckIRCB7KeltUsNaTHEm02QA0DfaIA488vfZUfh39La-P6Fc3xmW5pTEDhUsFmSNUtPGZdKoKNgO0RuEBMLJ7n1N9i3xIrME8_6ligY4zrhijtd9Q9iKQLfBpkSp2VlacjTiSYkUpcq0c4ScYO-rkifWoaAeNwwR3vuT_J2pOE5DMCc10E9cHvgiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=macUqn3VI5N8yZYxlaWD8LpXTdSy0i73KTbn5J5DoyR-0LcdQohAtiw10dZneGJZMVnRpWegREgspm_ztE5J52BYi7nfRDLhpYW4vEC5veXTldDnUCBUTNNYHCDqcFMGRubnT3CfSWOINXBv37VKjPuyTurDZWckIRCB7KeltUsNaTHEm02QA0DfaIA488vfZUfh39La-P6Fc3xmW5pTEDhUsFmSNUtPGZdKoKNgO0RuEBMLJ7n1N9i3xIrME8_6ligY4zrhijtd9Q9iKQLfBpkSp2VlacjTiSYkUpcq0c4ScYO-rkifWoaAeNwwR3vuT_J2pOE5DMCc10E9cHvgiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=k0IzLZw69H6EwA-h71TdwwwuTWEt-Y6CZp-PJvuTcQQT2GkXHVFaLNIoBJ8phZfuWeCLrhPucHP3oX8A_u5ewXQ0TYHvYtzdTvTC6bPVTJXz_9ISaiI5xe9jhyK3xXE1VMjRnGvZgBRtwtEY4UaaH357XAzq2_GX8ZjqUHged8m4Qt5kNx-puYbgriPFrVE77DOs_pJIan1-uog7Tjvyv0z4K4JdLcIcXj376GcYkBnQ80wt7oMIp5G-J4WY8Cpp-1-ArAYDX6YQE-o0EiU-QUPRjoZZ91uGCBARMH1p-QROSuuuclIWP9Wy7Fr5Ne33lBN41js3OWdTaymeiV1Mbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=k0IzLZw69H6EwA-h71TdwwwuTWEt-Y6CZp-PJvuTcQQT2GkXHVFaLNIoBJ8phZfuWeCLrhPucHP3oX8A_u5ewXQ0TYHvYtzdTvTC6bPVTJXz_9ISaiI5xe9jhyK3xXE1VMjRnGvZgBRtwtEY4UaaH357XAzq2_GX8ZjqUHged8m4Qt5kNx-puYbgriPFrVE77DOs_pJIan1-uog7Tjvyv0z4K4JdLcIcXj376GcYkBnQ80wt7oMIp5G-J4WY8Cpp-1-ArAYDX6YQE-o0EiU-QUPRjoZZ91uGCBARMH1p-QROSuuuclIWP9Wy7Fr5Ne33lBN41js3OWdTaymeiV1Mbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=BVvq7aX0v0ylXRGCVQDQb1NzSMD4YH3XquWhF66Gw9_ORg3axls-ZNl2WL2tc7OGvRhHKzEME3FMGC_Cacu7SlPiU-eEjjQoBb9G4ZBTvMx6gEEE2PQPuaRfWPBBXXESqabBN0Q0MikSdduWB9LivqFDh_2BGnTXw9bEdGIgiktTgL04ChMu1V1RDj7epVn2r60RKJG5RXIY_jNXDodel5NhBQWga1Bq_oCW9YaZkhuV2YJp3gvfN41nngj00PvUAizZyH_HmptUWlS-6IBzH3bDEyRxHZirxa093vlJWH_3NzNkVX-uVvxH2l1e1wC-K1AhQ6DcYH7PuQ5nIcGK4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=BVvq7aX0v0ylXRGCVQDQb1NzSMD4YH3XquWhF66Gw9_ORg3axls-ZNl2WL2tc7OGvRhHKzEME3FMGC_Cacu7SlPiU-eEjjQoBb9G4ZBTvMx6gEEE2PQPuaRfWPBBXXESqabBN0Q0MikSdduWB9LivqFDh_2BGnTXw9bEdGIgiktTgL04ChMu1V1RDj7epVn2r60RKJG5RXIY_jNXDodel5NhBQWga1Bq_oCW9YaZkhuV2YJp3gvfN41nngj00PvUAizZyH_HmptUWlS-6IBzH3bDEyRxHZirxa093vlJWH_3NzNkVX-uVvxH2l1e1wC-K1AhQ6DcYH7PuQ5nIcGK4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=ret1P1Kb0eJQ6NbXKMv475oGeZVAYvr9AIIANkX_JeaS6QkddmLkue1MqOWAKgbP5hKT9h7XHm9nZidFK6JLT6eB0VuCP6hAfe6pzYsSY0VuDLCv4vMdpuOUwsPhmTQ686OjWV4aPKyv08h1edwRzWI5zpFMVwgQ5EHBbZLZhCvvDtgzTpktEGPmQzi9GuRFLygX1yH1zsXU-WjWeRCKI_KknsgnO7yoU09Qfl7Yakt0REvxPlgJj2bPtPE9o0UuUxqpCqHPWVDMyi7MXCJtuT8TigXyBoZNcmYepJwBEqkzlw9t0-QuiOoL3-GyCfJT8Ka0-a1gBz2Fhqz_z0HFtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=ret1P1Kb0eJQ6NbXKMv475oGeZVAYvr9AIIANkX_JeaS6QkddmLkue1MqOWAKgbP5hKT9h7XHm9nZidFK6JLT6eB0VuCP6hAfe6pzYsSY0VuDLCv4vMdpuOUwsPhmTQ686OjWV4aPKyv08h1edwRzWI5zpFMVwgQ5EHBbZLZhCvvDtgzTpktEGPmQzi9GuRFLygX1yH1zsXU-WjWeRCKI_KknsgnO7yoU09Qfl7Yakt0REvxPlgJj2bPtPE9o0UuUxqpCqHPWVDMyi7MXCJtuT8TigXyBoZNcmYepJwBEqkzlw9t0-QuiOoL3-GyCfJT8Ka0-a1gBz2Fhqz_z0HFtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=ILT2ipZ9fUclv1tEaYipgYTqS0Bd_c8O9dkzqr2cbkQEPcXRChJ57odwCClNEM0r1M_C_ZLTb7zzBhFwa_tl0K176Lu_sHJf4tbYwldPzKQ70Wjh2TXsVpBkmgdWRqXqapDTl50Oiwpfnp-5WDXMQwQtjDq6Foj-_ykF__drweK04r8bxxzoS_eELh9zezjR1BLInd_y_qSWlqmDEuojOzcK98oMB5tMOedCSt_eDIEDPNHB7oZ2WQ418lLqcxVpk5hybvE7cVT-z8MXiXeUGm0t7dK6DA820mspUJDtmxVCJ2Guu6tpY7-nQxIHTjbcewQor9iA1COuEaIU02kMzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=ILT2ipZ9fUclv1tEaYipgYTqS0Bd_c8O9dkzqr2cbkQEPcXRChJ57odwCClNEM0r1M_C_ZLTb7zzBhFwa_tl0K176Lu_sHJf4tbYwldPzKQ70Wjh2TXsVpBkmgdWRqXqapDTl50Oiwpfnp-5WDXMQwQtjDq6Foj-_ykF__drweK04r8bxxzoS_eELh9zezjR1BLInd_y_qSWlqmDEuojOzcK98oMB5tMOedCSt_eDIEDPNHB7oZ2WQ418lLqcxVpk5hybvE7cVT-z8MXiXeUGm0t7dK6DA820mspUJDtmxVCJ2Guu6tpY7-nQxIHTjbcewQor9iA1COuEaIU02kMzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=nrg0ywiIeo2Lr2vfHm42vP4EW7x59CRyDrkOdDjO2oL7PHF22PCk39MFCbLFAdOGtGNQOcLJ5b-rlkGNu5dN18jlTi4NIe_u7uMjZz-rU6_xsAspg_7GPnrKZiop1EKjATQdI8Yj4pOjczRP3iEkqviHW7EWizC8KIBxF9Hb1hNbWt77JWHKk1uP9NzoDuviB6bNSnbuN5iuss0G4px0Tijk8-xXVxPDHOgvEx3E4ExA677m1lqXaG74mX9eKgukYYHaFFAA0I89-LhuYD39bRevt3MmQlVgGlqa9WYuqeeDuMFgShQuumzbBo9Oz5ej_9nTBVmp1uo1374I6Ys_Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=nrg0ywiIeo2Lr2vfHm42vP4EW7x59CRyDrkOdDjO2oL7PHF22PCk39MFCbLFAdOGtGNQOcLJ5b-rlkGNu5dN18jlTi4NIe_u7uMjZz-rU6_xsAspg_7GPnrKZiop1EKjATQdI8Yj4pOjczRP3iEkqviHW7EWizC8KIBxF9Hb1hNbWt77JWHKk1uP9NzoDuviB6bNSnbuN5iuss0G4px0Tijk8-xXVxPDHOgvEx3E4ExA677m1lqXaG74mX9eKgukYYHaFFAA0I89-LhuYD39bRevt3MmQlVgGlqa9WYuqeeDuMFgShQuumzbBo9Oz5ej_9nTBVmp1uo1374I6Ys_Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pasa0x4YRNp-Z2F1BLmD7JPfjZgVq1wYBvkFKuZLJ10XXEaqHoNF4ud8y0CNFTu46v1e-dQM5w976ZkyzC2GQ-NUjiWDMFAn12dAt07gjHVng4LwqyE9fCu51fi_JvHoLNtSjIEljL6iSt-Ccu9IIczRhxNJtRqSVXBWEIT9jkJxtLhdTK-uqqshrhpkc8qIsDpoEj4RmqXE4PMOJ-6mRoBfkUPkbqyPX39jCn71bR_5lEhk4ROklWjsDbKtprA92p28PexnCyPzSbUpKq4H_E0gSFPTiNzqMqiCCIDUvO6NEYaVnS5A8rifSPDR9wVPVMQzhl3X4sZtKcOrd_HPNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ayrah7for4QMX7dmrMLvMBf54JgEWK-H_Dbnd6vke3j6jO_v8td8LqrXbkoFzqY6-G6FQiUeKnY7iLrqkzs8TGcEhFlBBlC4B016inPF4KyoAISk-UGFgRcJM2Ypk9ny6SLo9p3Nh9UWVzYasQeMaZtlBGHwI2ShMbl-jFdFB3J7erDCmHhODhnA0LDZ1yO5O0Sp3Rm1pId0qyv1qxOpSSzaVrXlsXHL4yQi_FwrmJB7YL9raun1JcVq_7Qmr7T_6huoltqzqRVnHgSsUTktmUp_eW3Bqz0NEocF86vkHksh7pE3cBtqQyexpcebmdhOSXDs3vlUZxf-JVdH2mXXMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ayrah7for4QMX7dmrMLvMBf54JgEWK-H_Dbnd6vke3j6jO_v8td8LqrXbkoFzqY6-G6FQiUeKnY7iLrqkzs8TGcEhFlBBlC4B016inPF4KyoAISk-UGFgRcJM2Ypk9ny6SLo9p3Nh9UWVzYasQeMaZtlBGHwI2ShMbl-jFdFB3J7erDCmHhODhnA0LDZ1yO5O0Sp3Rm1pId0qyv1qxOpSSzaVrXlsXHL4yQi_FwrmJB7YL9raun1JcVq_7Qmr7T_6huoltqzqRVnHgSsUTktmUp_eW3Bqz0NEocF86vkHksh7pE3cBtqQyexpcebmdhOSXDs3vlUZxf-JVdH2mXXMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=UgIOFd16ZtswRpctEJ1ja0sfxeDuk6OFT2ozDzqn9kS3OChppu_xSXVQCOS0hfS69U4xaggsLg4S0zDjvqi-fHAK4mCzR4WHNK06MsA-sBtbztrfaqv9zsASmyVCQmu5OSspSmf1TLxOMVlZb5M2Nx1Ng0i-iaLxzsvr_LSndhOmxTFhiSl5RAVunalvgMsbbtMKbmkR3ZRtrsniLFrH2P6M8Xgi3NyLoqQteN6DGiovTFmCNo7ougrIih2KQdEX7tR2vjUrHgf-ooUPudR2tjSB0x88QxJJkaFTYJ00D8mfyfHwpStpyNnbSzIAAQS5bP7KKxmrpan6c7YuIQVf8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=UgIOFd16ZtswRpctEJ1ja0sfxeDuk6OFT2ozDzqn9kS3OChppu_xSXVQCOS0hfS69U4xaggsLg4S0zDjvqi-fHAK4mCzR4WHNK06MsA-sBtbztrfaqv9zsASmyVCQmu5OSspSmf1TLxOMVlZb5M2Nx1Ng0i-iaLxzsvr_LSndhOmxTFhiSl5RAVunalvgMsbbtMKbmkR3ZRtrsniLFrH2P6M8Xgi3NyLoqQteN6DGiovTFmCNo7ougrIih2KQdEX7tR2vjUrHgf-ooUPudR2tjSB0x88QxJJkaFTYJ00D8mfyfHwpStpyNnbSzIAAQS5bP7KKxmrpan6c7YuIQVf8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=GwZP0r-SXFtficXtxTd1JsKtRb70ui--BmZnE0718se2Eipl935t_k2hkrxLONApyOeatCBXHMhtEW50TWv9OoUOWTp36pCxnKpOkLzBrv_cVk6_V7v5HVpZSx2HpUdgvbKs1k7iLtRaor9KjuXi3beiN_-QmgrAJ3PKXlhw1Atya37ILeZeuIVKlOzQwBZoGC_xhHP5rTkPlW7FJ62JyoXzqQG5-w6d6dVzVZKjiUcLo7ms_gKc8sI9IZSKL9-hBrFbCoLyOouEfgU9yrL2gFGq7Zh0QdItKrNxly8gNuZBdx9EvcG7uptjEFgYG1T7ttQnaR-NKK1VR2Tys0d9ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=GwZP0r-SXFtficXtxTd1JsKtRb70ui--BmZnE0718se2Eipl935t_k2hkrxLONApyOeatCBXHMhtEW50TWv9OoUOWTp36pCxnKpOkLzBrv_cVk6_V7v5HVpZSx2HpUdgvbKs1k7iLtRaor9KjuXi3beiN_-QmgrAJ3PKXlhw1Atya37ILeZeuIVKlOzQwBZoGC_xhHP5rTkPlW7FJ62JyoXzqQG5-w6d6dVzVZKjiUcLo7ms_gKc8sI9IZSKL9-hBrFbCoLyOouEfgU9yrL2gFGq7Zh0QdItKrNxly8gNuZBdx9EvcG7uptjEFgYG1T7ttQnaR-NKK1VR2Tys0d9ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=EHbdX6ne9t_ejbnORXW7JHMdP_rPbOH00iT3fFsbHv_I_bH1BX_AFFMmbQzR_XwahfimmuYTnqsnUJd7jiek-RebfftAl1nHJO91mdBaUCyAsn9V_vPqD8fwwQKl6BY7VodzUjCJPZRmcwMLLEPj2RcmL7qNp_tEB9JIKI7as8DwuZVZiqpQh6eMnXmWUGslNn0MemIItyE_yPresbGdDJAjhwQk4IMMcGZ3Ku_tEFXDirNoEDRAbG_9JcEQ-4Zr3bPyqQdiQYcKGWZPUpcWYWytRfQwucJAjQHiv9lD2v0TkpNU638ZQEsGqj4PHjK40wBarMX7vXBTcWQm-K6fNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=EHbdX6ne9t_ejbnORXW7JHMdP_rPbOH00iT3fFsbHv_I_bH1BX_AFFMmbQzR_XwahfimmuYTnqsnUJd7jiek-RebfftAl1nHJO91mdBaUCyAsn9V_vPqD8fwwQKl6BY7VodzUjCJPZRmcwMLLEPj2RcmL7qNp_tEB9JIKI7as8DwuZVZiqpQh6eMnXmWUGslNn0MemIItyE_yPresbGdDJAjhwQk4IMMcGZ3Ku_tEFXDirNoEDRAbG_9JcEQ-4Zr3bPyqQdiQYcKGWZPUpcWYWytRfQwucJAjQHiv9lD2v0TkpNU638ZQEsGqj4PHjK40wBarMX7vXBTcWQm-K6fNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpr7lSM1D-HQX3f7EEiSRiMTilXxEYb-o2kO8jNpMLuLEyvfh8LlneJsluoZ-7UfEM_8FH6DHdJgMD6svmqZ3lTz42EJkfL8Pc3skdZrGB_p7Ag6rZGmGo_hQIjhHNRYGZX-V5R4C6cXJnR7MmiyIGTZger11dx5ZiYP7aGq7gscZbwvLpwK1y6EtB2MtB0NxcnC5So5_l1fItrWViT63cp0Q49cx7kchM4QTxuaMuCze5AbdDDx_0nXW4bL6LJD42L2JbuWevp_lnWSWGTK61Qto97iktVlZdyrP-AX2uAEn7LyNZTS3ldVQcxKWcCeqvr9ANEMVGKUaLgODg9Jhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=HEVXtbqKlpRCeR5BSHZyXpXwz0QZFX5kmlQLm8YYfse7IFK2e25utErFMOi8pgswYG--vq2fLrZSjZu84ZC38AbEpdulT3-6h4SwGdwMvRZFHjWbJawW4pprwW7TojCsUVnvVKly7NA7cuZgB_e5ccbdbmMXkaBbJwkPJwHXKu5hzGRjuGYkRRdjHHDDDsKi2NDrqifj51ocESq5F-q--mgJ6JUOpWrkANYwGDsrefSAj3lrzFuLEqJRkoT1_FTM7Snw3EW0SQS838_owDpEzs_rUy_adFotmt-mSUyJTwhxZmYgea8wjebfdwDRhci_rNSqs0da8PcY9PRf0WHT84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=HEVXtbqKlpRCeR5BSHZyXpXwz0QZFX5kmlQLm8YYfse7IFK2e25utErFMOi8pgswYG--vq2fLrZSjZu84ZC38AbEpdulT3-6h4SwGdwMvRZFHjWbJawW4pprwW7TojCsUVnvVKly7NA7cuZgB_e5ccbdbmMXkaBbJwkPJwHXKu5hzGRjuGYkRRdjHHDDDsKi2NDrqifj51ocESq5F-q--mgJ6JUOpWrkANYwGDsrefSAj3lrzFuLEqJRkoT1_FTM7Snw3EW0SQS838_owDpEzs_rUy_adFotmt-mSUyJTwhxZmYgea8wjebfdwDRhci_rNSqs0da8PcY9PRf0WHT84i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=T8f-NwKUGHs3uxGSAfWYEhjNl6vElypHHegc9jDDhCbhqbrtRB5Blu8AASjpdITGGrsmLEVfq99QSLugrp87J2dza8QcTxnKOCTJUGPxNsAw4s5Bm_GMYTfFHkU5S53TjxNnGxJuHM-vI3IsoHBWwmwhIesj7S7KFtFhXdC0Craviuj-2RtqAJODJCbYl1GaRVijqbfKusOKMAYArPpJDYOb97k1DipXI_XwYXTpUBye_cIGc4WCRFGWKgHnzqhzn6ziK3FxV510unRXCpXaKQK1bSvM7Msvt1729zKNJNoSQ2IUVl6foJQREr6zVBB6ZP4vmKA3787BFVnw8MxS7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=T8f-NwKUGHs3uxGSAfWYEhjNl6vElypHHegc9jDDhCbhqbrtRB5Blu8AASjpdITGGrsmLEVfq99QSLugrp87J2dza8QcTxnKOCTJUGPxNsAw4s5Bm_GMYTfFHkU5S53TjxNnGxJuHM-vI3IsoHBWwmwhIesj7S7KFtFhXdC0Craviuj-2RtqAJODJCbYl1GaRVijqbfKusOKMAYArPpJDYOb97k1DipXI_XwYXTpUBye_cIGc4WCRFGWKgHnzqhzn6ziK3FxV510unRXCpXaKQK1bSvM7Msvt1729zKNJNoSQ2IUVl6foJQREr6zVBB6ZP4vmKA3787BFVnw8MxS7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBo4gcnvN6C2xdVZnA_7T6e_EAma7z3XtnohvVAxBKEEC9krH-nJNc1iwbHXRyco1PEGlEanzJb2-aeUj7Veicl0dS_S3H4iAjmIfy2s0WtwVg70kDAWNHDMTFcCUw31zuf8p7FURAr7zh2mWkXYo2aIJFi3OJGoqbc-Ad7jqKzjl_AGmVKE4CsGMq5asuyeBozZ9PemcmiKLnI9kGKT00wXDxI6zjM60Xaxh4nwBqB47FsJkwlRXoZGp8ZjFg1JXGql8yBnf8BWKs076jISqXpW_XBNfjuyhdcPYhhltN1q_ua7S6lDlwpzs6As-aKot2ehrTtFpToEJRu4rUsY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uA_fwGy0pfr30h9aYJ2faBxvc93GNe8ZqTzcnGcNlxUo6PhV91FqPrsCn9Lak27JDQUmXXTve5ODDNSRL6EWOphE-_1TomgLYEN2IbgksOCwnUrjubjHNGCpO7O9odggF32lxQPU-P0b09zd0tPdVDkNaDA_6dHne128z88CTrEpN-D6Ejfjh18xe-Mcn_TbJcZsZhFvtZAuZU6EcuBXJm58qLSBc0j8Y02k0xV3TiuYAS6nzu3ejlo1TQXrNF2twLnLgxXOrz-3ww98plmXI3w8CgfKPfQzBHQ8WyqCR9VS9dTmvObyc8OuWRl7-Kxt_rLrrrbnkCRumS9cKdN5_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=WPDmaFBc-3nISSFDwuxkBK9kabd0Mguq76gTZ9gXZV--2GPGF9YwOtUP8PZnq3W6UQlUZnzBBEilOylznvN1Jk4N_CAb_ykK6NZMWPQTUranRMB8Yk_iBdPQXcvxm1N--ZfKfVhSBuoWSQ5Z1esbjSNPSw5Zh8W2oT37SLILNklVTlSNWB6o7skbjkD5PeI9ycMP5bi5OOEqnU14IxuxzbBP8Eb2nhf1eB5d5FzfLKK3gqOkzaviRUY3qprMN18jgB8bCdzUuCnvOAjbjXipAx4uq6x_62cwmxZHusmo6CgZmZ6kEPDGgZa-0kpBZLYCV6IZ0qYsqLRX6cEZb98ULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=WPDmaFBc-3nISSFDwuxkBK9kabd0Mguq76gTZ9gXZV--2GPGF9YwOtUP8PZnq3W6UQlUZnzBBEilOylznvN1Jk4N_CAb_ykK6NZMWPQTUranRMB8Yk_iBdPQXcvxm1N--ZfKfVhSBuoWSQ5Z1esbjSNPSw5Zh8W2oT37SLILNklVTlSNWB6o7skbjkD5PeI9ycMP5bi5OOEqnU14IxuxzbBP8Eb2nhf1eB5d5FzfLKK3gqOkzaviRUY3qprMN18jgB8bCdzUuCnvOAjbjXipAx4uq6x_62cwmxZHusmo6CgZmZ6kEPDGgZa-0kpBZLYCV6IZ0qYsqLRX6cEZb98ULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0faQJv2pkbf-DYeOhkx5PLQ6El3nt2yfy-PNvgGfgxlqbE0cGGjPf47HCmsYUuSFgy7h7Xe-qYdTEfHhmKEkr-RKYrz_Au7bkuvrKmf83Q0i-VAPi4sY1KmNLpyXzrbiJQzfWsv4xfuXqW47ul9WR8p_qMyRxDtxzY1iJkKIQtj64xjeUa5kCFYQ-_vv-Fje9Ia9h7OEwRMTcI8gRGcIqp2eQSx-usWeplo3QJsGMVoJ8k6jGQmTEJpHTb9lR2wwjLudaeRSaArctf_omGhXXlUcwn8WSa2U1UzyWSSmO-yOxHoyhSfHQvzPohZgXLXIFXcBs3zEGU2TvNVJces6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpYJcRUtkM6MTOQ9lneIQIfrDvO8IoOWPddM2F34w-qXabOF6DmDPENTa2Zaxhx7EnvEdZvtP9eceOjhzKj7l_lvQ1940oH8lQStastP9BFxwZqOs8zFZDzU93msY2pZJysZ4Wlf_7VsR1o0iS0hHMsJ1SfbiNVggYHysaEpHt2Xnkvmr-Gm95ktzFSfxOIkgRIkiPNu7RilKnr35DD9LWmOQrLGspkp_H1163mWjXHxJL4QINA9VUFctg3BbvoV-92KkMv__jC8DaLYBxveK5d45qhXTCChxqgi7_TWCVZHKU7yvZJ-0R7XK5In0tJdMGSU1rtTbokEJGyf7dEt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFe-OCBDX7RobgMVS2s-NLpbiqPus9_qJw6OV3N2yybNRxyUly-oml0f2jxn2tpHGiBfEvQUDwx9XPx4RPRqUksUpSiwPMkRmQ5njZA_qHqzAPbd7xK7C4Boc9MoAFmGIzRDoEQgJy0p6hg2copllLZt1x0Gjg5VPD_S_VQekxUbmdfY6OT92wIvA2E5opo_MJEkxIi4rmuc1rU8R-iqjioaItcv1KB0U7wb0sEq-4CG4dSmkbJslY32DEMvDZaPnl6Sl39cU8uJdlWQFsEVX61YWMGnPK1R9t8OoC7NpD9Z7l9MS09BoWdAdPwxvnhBk2cQJOYtdRPbUgwM4VL82Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=FAssNm56jCZxDRqgGdQZnXRsSNODS8_Mc3FpLarMb6niIDISyUMsDEmE8NmTBR3CYqdXXyvaMOecEvCvtY2IGIo-x_K7fGQBQ_wlW9_kcwNtNFGU4WEUFDexIM_5yY3lZTcVfTL3W6Dn7bE3G7t5ct0ccGuzGez4gp3lRmPe4zA7jEc71R5G6mehFK71f3KDDGy8RDJzJpb7k3XWMsU_6khVPzaXkpZ5T6FP6fLXc-Gi2NSaK4_5sbnVnaX7N5GokQ6Y5K0puMUSQOs5FJxNV8N1lAWeB4Udzvc2vyrDwkVB78trKpdxR1XUT4MYFqz42C-zPw8M4V-vLpbxaMtR-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=FAssNm56jCZxDRqgGdQZnXRsSNODS8_Mc3FpLarMb6niIDISyUMsDEmE8NmTBR3CYqdXXyvaMOecEvCvtY2IGIo-x_K7fGQBQ_wlW9_kcwNtNFGU4WEUFDexIM_5yY3lZTcVfTL3W6Dn7bE3G7t5ct0ccGuzGez4gp3lRmPe4zA7jEc71R5G6mehFK71f3KDDGy8RDJzJpb7k3XWMsU_6khVPzaXkpZ5T6FP6fLXc-Gi2NSaK4_5sbnVnaX7N5GokQ6Y5K0puMUSQOs5FJxNV8N1lAWeB4Udzvc2vyrDwkVB78trKpdxR1XUT4MYFqz42C-zPw8M4V-vLpbxaMtR-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=dMFBkix5UNLZ392Pjtvx1Z2ki8cp0dugV1Zh9UFc5wZuNZLP79XIedpJa486gwolDbDoGt2B6pRLHjdbpZLtFo7bPd3YxZW0lneFqbEO0JjpC1NaR02PyN_8dcGFNTwpERZ3LKO1p4HfAmF3neVU1NaqRkcwkhAJy5fdnm1uUerpu9B7759b8rTgY91YRMledu4HLVwaNZdDoI1GejJWJOiGnwfmSdM9S58QQhkHJ0kaCS9Yatc79yJ6bvph_teusYhx5kHMtvQLCCdUPpS9KATPrnr92xIY4i2FbdL74zMeZPHU71qDvlDhl54m23FeRolhmGHCBJubT79pkeVc1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=dMFBkix5UNLZ392Pjtvx1Z2ki8cp0dugV1Zh9UFc5wZuNZLP79XIedpJa486gwolDbDoGt2B6pRLHjdbpZLtFo7bPd3YxZW0lneFqbEO0JjpC1NaR02PyN_8dcGFNTwpERZ3LKO1p4HfAmF3neVU1NaqRkcwkhAJy5fdnm1uUerpu9B7759b8rTgY91YRMledu4HLVwaNZdDoI1GejJWJOiGnwfmSdM9S58QQhkHJ0kaCS9Yatc79yJ6bvph_teusYhx5kHMtvQLCCdUPpS9KATPrnr92xIY4i2FbdL74zMeZPHU71qDvlDhl54m23FeRolhmGHCBJubT79pkeVc1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Y0wsXQVGIQ0HEg4bYLvu0jukVczKlmx_1f9w77WPNkXhEEXigH0d5QlIFtgdsgRWqsOCCadSCGzWvkPUum5_hYsqvr9jgpSUfG-XYPuhZZ5jeNfrO7HU4OH50gXDJSKhPoqEXFDYmkogNdpVuatJ3ZwR2Xv85DQYj42Xdi6xuiNOonnL_pDacnnQjSmvZY9lvthjZFHxgYn8IGnfkpMGmSYZz7D25ilFxHvTuFIzSH-bnkgIVKQmUwTNauHfp5VSo9YYQqex1omXSEvZ44AaNP7DjXVtWtZUTOely-l_0D1nNVY-qirRqtJWm0sZxvtRXzlq-13erLVk2S1V-s96UQzw4XXLojRr885Kxw8Y-ZIrxlUQQEiv9Nh_pp9BaOjN9SHqLt2ZOzVCxrOlagiwz2GbC99euT1zHyC9-eON3xn62CDm6uRuOuecVsmIMwqVNREeazm8RTu61DBnlD2KWEX0eKt8PGki8Rwamzj32ydKzZ6RZzyObldAGxcA7UD0dD8y9xmSSA6PkiMVL1Lu6Ob65kFRqNiPX5HT2l2dTEeL6hm0BfryezRg_ekyvf00oLjgt7YGraT-uhTYImn55r1NSOTn4iSgfTvcSFHJCPECaJWxHAQ6R8wWVTfthzQ7XS2PotK0bUiL7R7xnI3efn0KUc0x0JGpaPWJMXa47lE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Y0wsXQVGIQ0HEg4bYLvu0jukVczKlmx_1f9w77WPNkXhEEXigH0d5QlIFtgdsgRWqsOCCadSCGzWvkPUum5_hYsqvr9jgpSUfG-XYPuhZZ5jeNfrO7HU4OH50gXDJSKhPoqEXFDYmkogNdpVuatJ3ZwR2Xv85DQYj42Xdi6xuiNOonnL_pDacnnQjSmvZY9lvthjZFHxgYn8IGnfkpMGmSYZz7D25ilFxHvTuFIzSH-bnkgIVKQmUwTNauHfp5VSo9YYQqex1omXSEvZ44AaNP7DjXVtWtZUTOely-l_0D1nNVY-qirRqtJWm0sZxvtRXzlq-13erLVk2S1V-s96UQzw4XXLojRr885Kxw8Y-ZIrxlUQQEiv9Nh_pp9BaOjN9SHqLt2ZOzVCxrOlagiwz2GbC99euT1zHyC9-eON3xn62CDm6uRuOuecVsmIMwqVNREeazm8RTu61DBnlD2KWEX0eKt8PGki8Rwamzj32ydKzZ6RZzyObldAGxcA7UD0dD8y9xmSSA6PkiMVL1Lu6Ob65kFRqNiPX5HT2l2dTEeL6hm0BfryezRg_ekyvf00oLjgt7YGraT-uhTYImn55r1NSOTn4iSgfTvcSFHJCPECaJWxHAQ6R8wWVTfthzQ7XS2PotK0bUiL7R7xnI3efn0KUc0x0JGpaPWJMXa47lE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=i5N4UtwoWdXlgg3cJqVuYgY1-aQBfSrWyFgRHEeECzf61j4ImVms9mxwQA1IbTrE8bydPQYLQJ2eMeqmIinmGoLoSm7hQxvmQ-2P3s96DqnIVNAX8ewvi8uuj2Mp18OpDKVqjpEufhWo8vewZWPMYbyO6yBF6-2IiTDZRJ8FWPMIyoFFad9F69PvcGD3ZkilfELoOMAAYub3lKwayJl3VNsWCvZBdT-OXKH1683JK2gUX-rXdUqj8oqd-uuZ5Zh_emO-ol2wJkmlQV0dwdXsUYbpkiicIEQztTaGB0O9AOxSHcwVUCMqnMCluOkBMdTsFO0OXFzUSgFtGhpf9WaCdLNBCAmSU4lJLQUyXZgQbGIi1vklxZij5EioQDCUyoSkV6ZaUjls6SaP3BXQtBGv79rdasDAS4E9xiGt1lTXMI9IEmH5nxiYA9GNHNbyAlowFiYBojI6XBoc-CqiE757pzG1OyBDhV2J63oBlTERJb-GQg7TwqZQe1ARh_n537CSiMSWVFO7hdu9FhzQKkGQe1isSnihRrilfXc5tNMgl-V2v7Er_NYUOLoZbOoYXgnu_96Z0xQSDiVsdirlJS6QNz2BHL1bKt_CftxEdPUHBf1PlSIJnl8rOefM4SH7cLqlCffffmwMCKNHU8dodjdUV-kQa3J_9Tgy9amoR1f8LYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=i5N4UtwoWdXlgg3cJqVuYgY1-aQBfSrWyFgRHEeECzf61j4ImVms9mxwQA1IbTrE8bydPQYLQJ2eMeqmIinmGoLoSm7hQxvmQ-2P3s96DqnIVNAX8ewvi8uuj2Mp18OpDKVqjpEufhWo8vewZWPMYbyO6yBF6-2IiTDZRJ8FWPMIyoFFad9F69PvcGD3ZkilfELoOMAAYub3lKwayJl3VNsWCvZBdT-OXKH1683JK2gUX-rXdUqj8oqd-uuZ5Zh_emO-ol2wJkmlQV0dwdXsUYbpkiicIEQztTaGB0O9AOxSHcwVUCMqnMCluOkBMdTsFO0OXFzUSgFtGhpf9WaCdLNBCAmSU4lJLQUyXZgQbGIi1vklxZij5EioQDCUyoSkV6ZaUjls6SaP3BXQtBGv79rdasDAS4E9xiGt1lTXMI9IEmH5nxiYA9GNHNbyAlowFiYBojI6XBoc-CqiE757pzG1OyBDhV2J63oBlTERJb-GQg7TwqZQe1ARh_n537CSiMSWVFO7hdu9FhzQKkGQe1isSnihRrilfXc5tNMgl-V2v7Er_NYUOLoZbOoYXgnu_96Z0xQSDiVsdirlJS6QNz2BHL1bKt_CftxEdPUHBf1PlSIJnl8rOefM4SH7cLqlCffffmwMCKNHU8dodjdUV-kQa3J_9Tgy9amoR1f8LYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=s_FCyL9vzsdj2ZjR2FpB7-LUkykbwK5cc92WL1RJ6M45IkjGx2enIL-JKjWXnoQX3voDQllP3-yeEyvu6CeUCC0qkl7v02d6baOD2tq3i92jyb4G5fltI_IJC9vPNLyg9mRWq66CWKhDHrnzTLkH8Gl6ocOx6etOpDODdXlK45BMBbtyiD-eRFeyPgR1Xnbw0I5iFrjT_RhmvZofQqhHepbciN0MHbWykbKIxqVFoeJXVklXAo2lR-lTsONqZ7L9yGPkZz-IV9F3TDVUodv4J9qgWZBq1aZf4d0P-Cr623YFk0Kci3J6whcoLVvBnFek7n5PBDJr2reuEQmIW-FYHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=s_FCyL9vzsdj2ZjR2FpB7-LUkykbwK5cc92WL1RJ6M45IkjGx2enIL-JKjWXnoQX3voDQllP3-yeEyvu6CeUCC0qkl7v02d6baOD2tq3i92jyb4G5fltI_IJC9vPNLyg9mRWq66CWKhDHrnzTLkH8Gl6ocOx6etOpDODdXlK45BMBbtyiD-eRFeyPgR1Xnbw0I5iFrjT_RhmvZofQqhHepbciN0MHbWykbKIxqVFoeJXVklXAo2lR-lTsONqZ7L9yGPkZz-IV9F3TDVUodv4J9qgWZBq1aZf4d0P-Cr623YFk0Kci3J6whcoLVvBnFek7n5PBDJr2reuEQmIW-FYHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
