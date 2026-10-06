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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 03:59:58</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUjY_AcGw6mGVJew1v4ystz7h45UjA7CQFItI05S8ggSL8GOW4GUYkn8Jg8thJcRd0FPkUNCCPwvIPpOxdR9ao26y3T14iH5bp32D1RabkfGJExT7dhr1u7KA--snPSI5Mfw7oXuP-dLCg_aniw-YojFC2bAUnlkG2IiN1A5H8py8GZ2YcVZ3-7uAXCzgZ97lnS2LElV-H-uwtTUpOii7Yh_ZDIyHyuilJChEIDI3NeMQUJ9cTYZPFdKdxJTnmJ9Q-cgfEjfK7v-dUNRyTDJWqdE5DF5_4fUno1ahBMn0oPraNSRQMOSHNZVfgK317Q339ZNeog3ldLuh5ckBOipeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVVoIyjXv9ZPlDB_pkDht-PG-DFJ1tYufv38pCzfo5346C9Re2zQ4tz-kSvFWW8XtI2RhFMO08QOm6a70SIH_LNLfLf8jVTwojtoRQULvVotHSgM3fZ3Xtg3_FGd6JbGFn_aPOOBgw0_Yc3vH1IJ2OPR_qYxqtgH6d0mVnIyIgbPJ3HT56dZqPhNQuyis8Gn_Csp0ffkQ8kaHhMxw9MKmevPBwMBgBJrzICYuxCEf2wMqpQqMP1Rxs1iUwi29xvxMoYTmqtohmfHwAk5-kbWecamfBtFAFA6JSubVtkuFj9GMdXtgYRgr_xtqyB-0cG506_V75M_AdoHveb2zmkVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=fYJok62jNbfXb7gwLEhdg1jvhA3ScVVlLLx-9i2JC1RT8UU720gdAelwA-39HQFk9kUslM4zubUXctXxXAAwIbGwYal2rj8lsiKFDIhkoAwRidgEgg3J0V3H0yel-t1G2bTGNj4ZniRwi7lOAk_C0Xg2XYlqtByoKIZfDodv9iGNXMdqwLl27UU1AXUYm4XAbSoPCPP8SuQN-hGqXTMrjkHZsJpbFn2ESMuMLtSBs1ePP9V9zyvEyePJHFCM7MA2C1xqd9D3sR7qxsTdKzXa29bKPgyhyzc8KXiu9EHSbt2GI34NADAtropXAxB-G2Tiwr6K7oQhgpnQ7Y6DSfFGfUrc-3rPbCI9f3uXrV8duDPRjartLstAS3JUSjXPRna5Qbe8vNbdCWzQDq7SoCB3WNkQwsAixVvD75kDCg8yziJ3Va-toGGXU1TIGtyLvlkRvLupl1D1cyTUSw3S98MdsGiAbtZ_m8OtJR3ceod2JZy4QCTjTHpBpXbC9EeoSwux8fJVkfrTVdFY1pC8IvrEDYZsyWgijIdK_PFJeHr9xbu-6khzATiQYC13Oe1RzdF_VrxBO4BmErdygT3toh_sQJxG1KGR6p5KR7ByAfFd3I8yhVZDv7ChYDD_VnwoMdeRAHjSZL49_G3n2EYD44npTbvMD21GLiGrxvV1Dgb_yoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=fYJok62jNbfXb7gwLEhdg1jvhA3ScVVlLLx-9i2JC1RT8UU720gdAelwA-39HQFk9kUslM4zubUXctXxXAAwIbGwYal2rj8lsiKFDIhkoAwRidgEgg3J0V3H0yel-t1G2bTGNj4ZniRwi7lOAk_C0Xg2XYlqtByoKIZfDodv9iGNXMdqwLl27UU1AXUYm4XAbSoPCPP8SuQN-hGqXTMrjkHZsJpbFn2ESMuMLtSBs1ePP9V9zyvEyePJHFCM7MA2C1xqd9D3sR7qxsTdKzXa29bKPgyhyzc8KXiu9EHSbt2GI34NADAtropXAxB-G2Tiwr6K7oQhgpnQ7Y6DSfFGfUrc-3rPbCI9f3uXrV8duDPRjartLstAS3JUSjXPRna5Qbe8vNbdCWzQDq7SoCB3WNkQwsAixVvD75kDCg8yziJ3Va-toGGXU1TIGtyLvlkRvLupl1D1cyTUSw3S98MdsGiAbtZ_m8OtJR3ceod2JZy4QCTjTHpBpXbC9EeoSwux8fJVkfrTVdFY1pC8IvrEDYZsyWgijIdK_PFJeHr9xbu-6khzATiQYC13Oe1RzdF_VrxBO4BmErdygT3toh_sQJxG1KGR6p5KR7ByAfFd3I8yhVZDv7ChYDD_VnwoMdeRAHjSZL49_G3n2EYD44npTbvMD21GLiGrxvV1Dgb_yoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPTMYsPn3-YdzyfXFAIuowwwEXg77qGB57xcZ46gNzzTf1Enu8kqLRgfjbEo9q45QOP-M9Ul5lpT5sYFIdp27iDFYfQ2paBOEuIGFbqNuqN1P9oZhZXKKxEQLX-EkhFidN0_-iif3g7B0KDI3kkNVgoifurPFtqXDs-Fl8NoJfIAUP9NzvYAeKRpoQcyykCPyQag0upCgXInLzOe38Hsfd8JNfPnr2D3PNjcPrLhqMXDJa4N-0pxZTkozmCRR3ZFbKG7jTouJZQBlY6yc0odYT94wzDKXyMn8hG5wQ83_5K779msf0MtLfhOiaowAHD4ConMlLYzbZL692XQmxc4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OHDEPRt8U4UYJFpTR6CLVn_ERgwxJ_UcPQviR4HxBziq2V8t6pU8AUmVNVH7TY-XAWJHBbTy1mVNECtxZ4rEJ08VCfwRjZ8TYBQ-4fDH0hafP4AUT_IkOIDis2u8tQep-_U-wvtgE2G8axx98pwuspmIC5XNbMcZYt12NPWDtZHQQPZlWUKus3VZRObGIEyqcQlf8E1xED6XP9XnF59v-1MD1xxvbd1siV4YuUWutOPB51FEisxnhgIQfDdGIN_Yb6y38eacaAy90rPCm_iHd5rTMyos64KnLKRTic4itNSb30QptApIjTpeMHu2tW-ZVMS0M9dZWAoBgJ4kwTEKYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wa3pIsRPixaMvIm8hA-8b80QmfabVm3jowMf02rCWa0KvFLoFlPSaSesm7f3i3i0mRmmXBY6w4lAcy5SR9osW_CcjksH0VNi8FbU43hvKQe2bv4oUGki4lHRRGgfPy1VmXAkQRky3nK8Z3vvBMreXeboYNKGZLHbIjbVV8qS-2hzBxaMrUzNGp2iJEReZIg1bdYI-28Do2qKugHBmkURCd2n69lPa1zBw_e8QCddMuGJEb9NEg53X-GgZFD-08aSVzynSEsFJ48UEEbrf9ZTzHOjnhmxkaylmf4OIVohn7NsdTxpkQQX-2fgGETaFt0pk1lrWmy_ViLx4qLG8_VotQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=ihj4BruzkWtl4SP-6O64_krjbwU1sqUSsJ8F__L1SXCc4WefGjSm8gb8Mz_7xHUGD8QpvZkueqqCcklhE26XwUyt6Z_47wfKi15MxdRxysUzfQpWP1ExzT4c81OrfzzA0oo1L1ruuOJSp4kVOOIHGQ65Wr-oGuJsrhFRUJhaVDnyPjwotksjK40IP-CMEmIu5a7jmZQ30mskbXCyJMFXU5h8pIvWP4m6ikpqWayQRH9BY-GpNIUJoxg5IIbji3j3Y7ZrgbOWMkJPVivAtKMLyvAskGIwr1s8AyOxUsLtbu2gBn7nMs8O5MfZ1FnUfatW2aNf3GHbgVVEbqGXobt0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=ihj4BruzkWtl4SP-6O64_krjbwU1sqUSsJ8F__L1SXCc4WefGjSm8gb8Mz_7xHUGD8QpvZkueqqCcklhE26XwUyt6Z_47wfKi15MxdRxysUzfQpWP1ExzT4c81OrfzzA0oo1L1ruuOJSp4kVOOIHGQ65Wr-oGuJsrhFRUJhaVDnyPjwotksjK40IP-CMEmIu5a7jmZQ30mskbXCyJMFXU5h8pIvWP4m6ikpqWayQRH9BY-GpNIUJoxg5IIbji3j3Y7ZrgbOWMkJPVivAtKMLyvAskGIwr1s8AyOxUsLtbu2gBn7nMs8O5MfZ1FnUfatW2aNf3GHbgVVEbqGXobt0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=jZkaKJZGqMKcwMo1Ve4rMS6XXDMs06856o16OKHYfILOl9trTuwhBen9s7iUUHL_vMQt1T23dj74Qah3lk-UfwkTm4ymO_8dKa-B0E7v6gFUbcaEdF-NiQNWv603DLdwArVHixZFX6i208lZDEsXFvgeADEIog-j_Wa1rfWkgRMtFWiL7O5upA7JIyMe82HRmOmNvVy1e-8u1vk-350g8-fjycAbvwS-xvGaRncfwTEajbJL276XctZq-pbxuTHuCxd8IyJgLZKH-OdQ6PFnbWF_YWRnDm9BCKSf5_4cc_fJVeXhgas-vqehMXV-xFIhWcAqwkei92IX5ZqcgOq7KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=jZkaKJZGqMKcwMo1Ve4rMS6XXDMs06856o16OKHYfILOl9trTuwhBen9s7iUUHL_vMQt1T23dj74Qah3lk-UfwkTm4ymO_8dKa-B0E7v6gFUbcaEdF-NiQNWv603DLdwArVHixZFX6i208lZDEsXFvgeADEIog-j_Wa1rfWkgRMtFWiL7O5upA7JIyMe82HRmOmNvVy1e-8u1vk-350g8-fjycAbvwS-xvGaRncfwTEajbJL276XctZq-pbxuTHuCxd8IyJgLZKH-OdQ6PFnbWF_YWRnDm9BCKSf5_4cc_fJVeXhgas-vqehMXV-xFIhWcAqwkei92IX5ZqcgOq7KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsPalskY3eZsj11pdRor-oESnKsOXeuaFZIaEswV54OHPYBf8t22J6XVIU3foOsafCw1vj7b_B8Ig7Sscgewj2NK1tHk_c7HokzbFK9_1fUnJZFIzld7PosO0b5Ur1ccT10Ea0nw-DOxBz4eT3nNhCyofOSB3iVElw3k5IMSHQVavnPRjWDttbwfV1qbxSj9pI-XMvTIg-BctbE0UPoByfgBppWUGxoTADYaH2DBJ-V14laH9sMWL3q_ka9QnsykQAVN-NhBCRfVc4Lboza-YpmzFd9_VNGGTBURAGCe7LPXlC-BxDZHMOdJb9XDU2ItmgcHpazxHuv-jHbJ_KY3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=BkJT5-W0GJypdfFzlRENwvryYbbX4OHEpzcj-C8n-yOkT9oiy0sXD1YuhxAPqu50GLYIQ4SJTd0yg7Iz6Zet0QFhqZn8LeAi3AY0n9mcqaKwJEl6DYXKM6p3XY0x5ahpeU9r-tXtc8vNjCfvAipOlK4EpT-kZ3evmbt2PkFDyMPFFUCx7ZCzKIfr6cIfILulHaVi-_M0XpVQDVz2emk5yqVZpwTmFdZwxI3Aw_i5AYx6xkI85_rEnpeeH-nxLzH5uhmSjPNFSzxumxb_HreDT0rzapYVzewJZvsE-GYotYEq265FQ8hA3ist9AjynuFiwAVwQrL_X4yQR1D1eNMDIESqBhIkFoKv9CbDvwd1aTtZyVADMTwIN685OBulAwGgvvNf_FFpZWV43npCL1khvDbyLKtPI7jO67AvFleEtkGj4UHYT_FA1mk5CQJ1aTOSGkU9wRfQVXUMbdquT7khX0cFJAXjaXVNcrX4sCYbfnu4k-sBRCh0rHukoxTodwxLtF4pnCW9iqGEcQ6n0M3TpOBjKLF_FWkk66eSV8gO5eSkR2ndeVm8YBqgoDj_pNs1u4wF2wp9iPYBobtv7LVI8pW1Cwnq0cFysE4jsbYOOsmA1SfDjiuB5XYbTJB_Yd0WVp1-1AWL-koYpuM6hqKO16OVzUHZYwjDzN-Qha3hqqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=BkJT5-W0GJypdfFzlRENwvryYbbX4OHEpzcj-C8n-yOkT9oiy0sXD1YuhxAPqu50GLYIQ4SJTd0yg7Iz6Zet0QFhqZn8LeAi3AY0n9mcqaKwJEl6DYXKM6p3XY0x5ahpeU9r-tXtc8vNjCfvAipOlK4EpT-kZ3evmbt2PkFDyMPFFUCx7ZCzKIfr6cIfILulHaVi-_M0XpVQDVz2emk5yqVZpwTmFdZwxI3Aw_i5AYx6xkI85_rEnpeeH-nxLzH5uhmSjPNFSzxumxb_HreDT0rzapYVzewJZvsE-GYotYEq265FQ8hA3ist9AjynuFiwAVwQrL_X4yQR1D1eNMDIESqBhIkFoKv9CbDvwd1aTtZyVADMTwIN685OBulAwGgvvNf_FFpZWV43npCL1khvDbyLKtPI7jO67AvFleEtkGj4UHYT_FA1mk5CQJ1aTOSGkU9wRfQVXUMbdquT7khX0cFJAXjaXVNcrX4sCYbfnu4k-sBRCh0rHukoxTodwxLtF4pnCW9iqGEcQ6n0M3TpOBjKLF_FWkk66eSV8gO5eSkR2ndeVm8YBqgoDj_pNs1u4wF2wp9iPYBobtv7LVI8pW1Cwnq0cFysE4jsbYOOsmA1SfDjiuB5XYbTJB_Yd0WVp1-1AWL-koYpuM6hqKO16OVzUHZYwjDzN-Qha3hqqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=lMUyC0ugXIJAa0Cyf0JptLuA1YUeXEssoMWaahSeOg4FzbaF1M5ONviQxfA8oGJCI-wR-totfnLsnpcPchUr14V01HFRvB1zarmdGdCX6jxvRKIuzr0RwgXOnq38a_av_ftacoSQdCBfoiwyJazdYSSGQpJbhjLFBZPRginpm5GYrxN5n8Wqy9mWaqzxRvobZdbniQwFmI0W4M_NRYDNvKIHufqfL1_oQQy4rek3OSFn9mp4rvm813cne-8bu_NJA98R6qeDHnViXs7W-mT-YvQNfmKGQg0OUohUM58Tnjnqy5ESZvuu4xprCXvLSJVVpGyfgvl-6bw5WcTgUtlZXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=lMUyC0ugXIJAa0Cyf0JptLuA1YUeXEssoMWaahSeOg4FzbaF1M5ONviQxfA8oGJCI-wR-totfnLsnpcPchUr14V01HFRvB1zarmdGdCX6jxvRKIuzr0RwgXOnq38a_av_ftacoSQdCBfoiwyJazdYSSGQpJbhjLFBZPRginpm5GYrxN5n8Wqy9mWaqzxRvobZdbniQwFmI0W4M_NRYDNvKIHufqfL1_oQQy4rek3OSFn9mp4rvm813cne-8bu_NJA98R6qeDHnViXs7W-mT-YvQNfmKGQg0OUohUM58Tnjnqy5ESZvuu4xprCXvLSJVVpGyfgvl-6bw5WcTgUtlZXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vg67qhFwCGsTRWIcM-upfAp3qbUX5vfpCaRl23-AbvLyngRg5_wDlnTQr738H9QwMtWbXtVHuiwz-H7Fvax4hq_7N9yhCJUAbxwQocEvjxxF8bPOtrXnwhVgayzjCkWtVUkQuSD-MGvWx5-z5pYvcFDgkHMbLo5eb_QLGnvTCIM5dpjERAqq8nAbHL2i43thnHh8MioNLC9sQP0HOGcmjGkqiAnD8-IHpmAwPb8F_0UMGVAjeyvm1GdfKN7wJa73RJkaSWWYl7MNFS5gqYYN0WfLCK72QgzynTpV8ulNuczapFF1nZUwJqYgrL51JFEIfwPQdkIxLuhlAWQfdjj6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=gGvmm3D6c1nSFAIBZwlKeEjLMJ3SOiaF2nZaTb9MbWgdB2Dy84HAtEszdbxKjafAD5cvm2U4A8EMe1B9WC6u_9nsQSB2zlsV6R_RhpOgFsjEg8cI16pE3hyq7FHKWyLj07PaVUpmB2kgHKkIuU9NTVQn5yJIj7rYiFanQkxj1-0XG-OxITiZmiEuhZ8KEfNk_347U7Jetr-aMdf0cB-r1o8VlCVeZGFw8YsKIeqrOiD93UChHKG23ynxI403iSmG_xfWXAiFewTpryzyJWX0ZjETmfclRpPv_j_DhBOeEwi8Q1Vbk7oeN4fKVVBsYKxi_X39LIdi5-tKOGod9S7oag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=gGvmm3D6c1nSFAIBZwlKeEjLMJ3SOiaF2nZaTb9MbWgdB2Dy84HAtEszdbxKjafAD5cvm2U4A8EMe1B9WC6u_9nsQSB2zlsV6R_RhpOgFsjEg8cI16pE3hyq7FHKWyLj07PaVUpmB2kgHKkIuU9NTVQn5yJIj7rYiFanQkxj1-0XG-OxITiZmiEuhZ8KEfNk_347U7Jetr-aMdf0cB-r1o8VlCVeZGFw8YsKIeqrOiD93UChHKG23ynxI403iSmG_xfWXAiFewTpryzyJWX0ZjETmfclRpPv_j_DhBOeEwi8Q1Vbk7oeN4fKVVBsYKxi_X39LIdi5-tKOGod9S7oag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmGhtUS-1-_q4EtYS3ejZztCFp02NTUI7M3HMklxdYd86RaIaeMQ_Hujob2gwgq7sTBTRa0Yq5BfMx1OxY8ziomhrskQq5DE3Ojb9t5TIR1QcSrFRkaCL72CE7wql-F5Eslbw3xlzzN7jHJhItMriyD3aAx-YDQm8nkbp0eJVOuLaS4L8LV6Dj41FLGMjZHdpun0h58n3FRiHAGMfk3ZVREZu9uUyA3T0lXJawxO6LxQy0o96YztQu5m5MRa5rC2ZVM6815NeCIrPLfAtfs_A08tV8oJTaFEPPRnbetb_k1yctjefEDPUAOsMFFzQY7fQjeVG6v4Y2LtzR-SHnjFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH-iOqxmhenMbPpDYcvZ1a4yvooOxAnsNc2yxyHwLk8V4LfwOYefFMgj-yCWYlQuup-5OBcFb7N6oohEG64Z0AUObmiJD0bEwh2iUhii4-rn6OLgVxDGpG0gv43WA7krsgLBZDLtoASkbsWOnyCyzF3dKjeaol3nhfO646jdVStOUNJhguiHKhOevTRNUEGWvg7Bohf7HUJbrVbTq_6vIPF9-1A-Ys6rrUKbdwVin4WD2uHiUWaaHUJL3fM5-k0rAZPaM2aj_mBFZhSvjR1NzydcVdW7rRTpnHIOz6RZR3mmHQALyikmR3w4xz6VDSaPP3vuupBOygxM1WHibA2SzQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=t_s1rCZ-jFBETOQaWkOqTImg0aetfDA647zwFW1g-iQ7zdGsIAQ05-wMdoA7AsURhnVKrOuUT767Twz_J3YYoESwUM4vrM6S6Yhzr8OI5fQ6GHv4b1LlgUVY5CrwET20OACh78udskXdGEY1q1vHpnDhBvCAzy_8OW07IEZ__sCD1ObX_vtmNPYtruO6S5kiV1agwQEa4W_TPIIfD9I3kXdaqmuadb0MuuZkfpvTtSRtOqCLpKxCrtTnnK8qz3sg-m_oQo35Xzzxi5fw5wktAUvBtclZCE0ja__17bY4BVcL_JezbzxPmYlrQz5Ku5rAgCuED9ODviYW487zBssymG90j_JYtf8JXQi3xpJJq-j23sRbPask2mnLi9Pqf7rmqJ9-b0b6b6emvuYHIyzw7fYxDH24rLK3TpzEL99k-b5gCIMxwjOzb7FTKPcEblvQfF6wdNvAxuyqPxpTvYFEK-yhJ0_Zyvof3rn2fSoPVgdqPgM9wze7V9EeQToYZKxZfsA7qiaNqamsd0HM4xP3xsKkww7NHNxKfMuyZcVTGc-1yNyFmUuRIMmCcmzmO-Snp31mhR59o6Mn1wQYj40A_H2m_Esv25LyVMNrSsB-C4f5SVHOfzxUO1rxHpdVISUZv4A3yfaTIB1Q0Jgh1FbJpcUCjqGWvvAdf1KyVjzxNho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=t_s1rCZ-jFBETOQaWkOqTImg0aetfDA647zwFW1g-iQ7zdGsIAQ05-wMdoA7AsURhnVKrOuUT767Twz_J3YYoESwUM4vrM6S6Yhzr8OI5fQ6GHv4b1LlgUVY5CrwET20OACh78udskXdGEY1q1vHpnDhBvCAzy_8OW07IEZ__sCD1ObX_vtmNPYtruO6S5kiV1agwQEa4W_TPIIfD9I3kXdaqmuadb0MuuZkfpvTtSRtOqCLpKxCrtTnnK8qz3sg-m_oQo35Xzzxi5fw5wktAUvBtclZCE0ja__17bY4BVcL_JezbzxPmYlrQz5Ku5rAgCuED9ODviYW487zBssymG90j_JYtf8JXQi3xpJJq-j23sRbPask2mnLi9Pqf7rmqJ9-b0b6b6emvuYHIyzw7fYxDH24rLK3TpzEL99k-b5gCIMxwjOzb7FTKPcEblvQfF6wdNvAxuyqPxpTvYFEK-yhJ0_Zyvof3rn2fSoPVgdqPgM9wze7V9EeQToYZKxZfsA7qiaNqamsd0HM4xP3xsKkww7NHNxKfMuyZcVTGc-1yNyFmUuRIMmCcmzmO-Snp31mhR59o6Mn1wQYj40A_H2m_Esv25LyVMNrSsB-C4f5SVHOfzxUO1rxHpdVISUZv4A3yfaTIB1Q0Jgh1FbJpcUCjqGWvvAdf1KyVjzxNho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfMNmUKTNQ_TmpTsCxKwj_U0pul_5ijepZEMB1U17sfBxexU0m6xA23CQvfiv2SeQmT8GTi-ivh0bja127ay0ICX0rX_XxFZ5LK6Bi8HmCCpZH-SKloSYOepzYc34oKwLOMboExFvPtPACDl_s28TSafvpJCAGF_Q4IVPHfJKleNcxAR28KPDtvzLUJB_wTigaWx8i2PVNHB8KNUEwLsBW06t7HsSdNc9xgJFIFCr-R9D8SE1FV0EUN8qIc83b2tQZAnaRg-cLa74WgNEvVnPVfinT4_jfQVbiRM-heSK119j_TuB9Zns_D40QYETez3rTdwqFq6KZ0ejdMrCmWA2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8FrYRlhckT3HMoXtnPMyMpy1Br3yLAz2poTPMt4teoRhSD4c5ZOFIvMEW9Xpib_X1ktCwb6u9m7lbf2ixEHQb92TmrDB-X2-3Bvjcry60_u4VjwTK_3N0HJnOgyAeQz0MV_h3Spl0IwN3VFNYpO7rkwn1reCfg75Org_oQ5t5pzRKegmMCgY1Ulih_-R_18vaa6pk2JXOBdxF_6QLCbZj9FZ1jzn9IxVHusaRuE4fljwAuygQSoUaPjbesoFe4KgQc3DE1mSqRIpBQraQvmXmnblb63OR2jhEmdDjZ0E8iY-qLXRqybykGj6gfpF64N9jCZtBQpnZm-y0JtZh7k0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=eNKCHYcyP3bC93Qsyp9y3KGugw6-hPguRGDv3cO2YC86BC5vdWBZY0i0aW2u_6XdSSIAaIo5qvPnrVYJzJ9f-3ofQrBCQA_O1jnsq6TorM4u5B30KbFp8m_fF4dfnS_PPbIisjjkgI5RfUCnopFXAfzzQUBPmZTMCcT1zx1I0jNnR9k90ksvQerKztmxF0kFM6sbGNfLKZHQTUdhlpCs_ntr6SIAwP_JA4D1WGMUTicTD10MEuzWLo6UY7uc5RNdphgMTox0j4ZbmZeX-9MeVZWukMAY30s6kf0uUPgLwONFwl3XyhQ_4JBbGDxQ2Bcyux5YSoLKHlBntHBuep7ryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=eNKCHYcyP3bC93Qsyp9y3KGugw6-hPguRGDv3cO2YC86BC5vdWBZY0i0aW2u_6XdSSIAaIo5qvPnrVYJzJ9f-3ofQrBCQA_O1jnsq6TorM4u5B30KbFp8m_fF4dfnS_PPbIisjjkgI5RfUCnopFXAfzzQUBPmZTMCcT1zx1I0jNnR9k90ksvQerKztmxF0kFM6sbGNfLKZHQTUdhlpCs_ntr6SIAwP_JA4D1WGMUTicTD10MEuzWLo6UY7uc5RNdphgMTox0j4ZbmZeX-9MeVZWukMAY30s6kf0uUPgLwONFwl3XyhQ_4JBbGDxQ2Bcyux5YSoLKHlBntHBuep7ryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=DhRXGoTp-kAdW1otoA2XfLXnxyzQRyoT4SiHBSXSdbOv0pKaoWLT5ezPxd7Ll1vHp93o3ZVa45vT0lM5a2eTlvUz9zr1q36RLtk0IQryeyIDd6PgsZR1_s0eG2qDiZ795s0R5GxncTNa0_lnkVOqL38lmcGTxi_DQsgG9NQ83kWo9lK8WiLuA-7fRvvO_6x1GKzzhoCY4mXak7CKQ1MsAreUIEwGB36qv4xSr0IdLDNZBan6PCkEnF7UjpIW_cEx10WkWQ_g7I-7eRKcDZ0ZXkat4tozgs_LZslazIsO8sKqImqPL7s_IkAtPf5NOXrK72bwmCTf6u5g3BRcwJbDxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=DhRXGoTp-kAdW1otoA2XfLXnxyzQRyoT4SiHBSXSdbOv0pKaoWLT5ezPxd7Ll1vHp93o3ZVa45vT0lM5a2eTlvUz9zr1q36RLtk0IQryeyIDd6PgsZR1_s0eG2qDiZ795s0R5GxncTNa0_lnkVOqL38lmcGTxi_DQsgG9NQ83kWo9lK8WiLuA-7fRvvO_6x1GKzzhoCY4mXak7CKQ1MsAreUIEwGB36qv4xSr0IdLDNZBan6PCkEnF7UjpIW_cEx10WkWQ_g7I-7eRKcDZ0ZXkat4tozgs_LZslazIsO8sKqImqPL7s_IkAtPf5NOXrK72bwmCTf6u5g3BRcwJbDxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=eSDXdUVwv0Zxte_LPJihoHg3rxwxl61FSWDNSRw6mbYl0xlk5R051Et83YHAEUrEN8HEqHFjoPrPTr--f4ozKlBbYIpLruGHFWTj5BvwW-nEtfbCedvz-_qn7hn3EKTddEfLgT6HILkKx5DVPCGfkA8-nYY-yDQQlNrHxKtqw7so-r6yCFUx6d1Oca3pwBxiC0D_nLwx8GWkjs364hydUH9E9NeBLpbeSUdsRrHTgIijJnByMOy4r6dt5OqwBcBew--quS9NRy7cSUMRcWaNHt_i4Kz9J1ZAqB14eIThc0fpaJ1UpXJLEdjKA5rkxiuOYcvuOGker1t51o-lv5UmTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=eSDXdUVwv0Zxte_LPJihoHg3rxwxl61FSWDNSRw6mbYl0xlk5R051Et83YHAEUrEN8HEqHFjoPrPTr--f4ozKlBbYIpLruGHFWTj5BvwW-nEtfbCedvz-_qn7hn3EKTddEfLgT6HILkKx5DVPCGfkA8-nYY-yDQQlNrHxKtqw7so-r6yCFUx6d1Oca3pwBxiC0D_nLwx8GWkjs364hydUH9E9NeBLpbeSUdsRrHTgIijJnByMOy4r6dt5OqwBcBew--quS9NRy7cSUMRcWaNHt_i4Kz9J1ZAqB14eIThc0fpaJ1UpXJLEdjKA5rkxiuOYcvuOGker1t51o-lv5UmTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPKKwXICD7BLSOgZuAhw5Z_CwUGNe53PgJBmAaIJfKItwQ4lOA7FU-NnmE0a1uLZDhJYsL7_rk6pJu3yDKCEOIts08Ds6na281HR7EU3EZrWdsB8dp0VaQKmJ1QsEvpmWJ35Pb9sjA1oJPGYzdsOwndRTFHC3HBYtqYTn0vEyxhKj2Zme8opxUtqKCqi2VHP7mN-mLj2Q4As_5u6YpgKfsUjY4kZ8Q5nc4U0FYwvy_5O1Yt6KNTdPtXiUdNNu3bIM445JXl5ItYQ8HhY94cfc8TGv3gklgdSDI9zpq-qDxelDf9ISTe4lPBZ3JAXruqtll1vyybYz5RtaIBqOxICpw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro0vO4aBG1qVcN0VfF2BPVh8VYtPzBMDK9hcUQup81UGvDJMgtFMqwGYRWzsOlaH5OJuqJV8Bit9rjhfyt7yKlVpyMj6H9-6hheRbzTwbbn3zhVFOuwo6BJ-xyATTOCIlmO4vkxv8nf_JY41Ae0LdwQ8AAV0O-fCgoBwU6GEjhw0sluQ7pVoDFKZNCi2stGjnGdZ_UH4bltmUt5p0nEY9A9_qg1mQH_G0k4NvyaHEE09TGw6uJKZoxRUluNwlrdJxvDhX3UsZzHCeobQWhGGpAetR7P9SfFWIwsyubfpl4LTfABv1dsGa4ninTYvtNyWU81DNyQ0MOEjFi4xMXncn0Bo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro0vO4aBG1qVcN0VfF2BPVh8VYtPzBMDK9hcUQup81UGvDJMgtFMqwGYRWzsOlaH5OJuqJV8Bit9rjhfyt7yKlVpyMj6H9-6hheRbzTwbbn3zhVFOuwo6BJ-xyATTOCIlmO4vkxv8nf_JY41Ae0LdwQ8AAV0O-fCgoBwU6GEjhw0sluQ7pVoDFKZNCi2stGjnGdZ_UH4bltmUt5p0nEY9A9_qg1mQH_G0k4NvyaHEE09TGw6uJKZoxRUluNwlrdJxvDhX3UsZzHCeobQWhGGpAetR7P9SfFWIwsyubfpl4LTfABv1dsGa4ninTYvtNyWU81DNyQ0MOEjFi4xMXncn0Bo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=tvcspP8716Jo2oM1OiezLJA62GVy6ntIb9tRZoJp8xGel09v07xDgrctX-_vzDzmO4bANny38MQ5MBaovjEerEwFOmWe-52E82DFYAKYebivq95J-0tvxEnwS-Jd_qhlozOn7TKn6Kb25oqFAJfaXBC-TPjqdHC6Hbge-PISXsVz0PD6RCxyYHOvPClAFX_33P3-Y4g0ryFXkGG-UpFnbmKuDUIX7sdnvEFGivcCBSWcNxKPwlK1HzIZBAXi20gGP76zMi-K3g0BjJRUl1nhHg-HYdLFee0T9v9nVSCpC22361dRiIk9MprkHKpfozLQvtApaKfEA826WwXK4tQJzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=tvcspP8716Jo2oM1OiezLJA62GVy6ntIb9tRZoJp8xGel09v07xDgrctX-_vzDzmO4bANny38MQ5MBaovjEerEwFOmWe-52E82DFYAKYebivq95J-0tvxEnwS-Jd_qhlozOn7TKn6Kb25oqFAJfaXBC-TPjqdHC6Hbge-PISXsVz0PD6RCxyYHOvPClAFX_33P3-Y4g0ryFXkGG-UpFnbmKuDUIX7sdnvEFGivcCBSWcNxKPwlK1HzIZBAXi20gGP76zMi-K3g0BjJRUl1nhHg-HYdLFee0T9v9nVSCpC22361dRiIk9MprkHKpfozLQvtApaKfEA826WwXK4tQJzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-A6_y8WhNGVNOrxZ7K2hEfh0PH-SJ2bwWH3dLkxvcx1-Sp-6LodCSNAkHLukV0Byai5z1SeMz3Nb1wgsNdd3pLIjAe2yvsBFvpFRzseyg9We2tc6z_cLaKhFt-avq48PrbY4Z9Vi7hlMyh7v6CmNEoAeV5Ni2By9Vx6WFDaLpSQ8DWaXTkYXZ7xcWZQxh7POzzHRdh-A0TDJbFc1DJBakPfxS1if3QluJMz_Rf6d1QOTD1TMVp_qiLVbdHvjloiu4fkCprbr3fD6gWWLc85FaAEBegJ7yLkymucS-t2U0pbW3QvhFDjblJO-beW-nGjRE78Iom3mqLpobBe6FpjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=m20RciPzXbjetMoSYqr5uA4mDE_Ly4p6lG-xajNLgnqy3k3LzrpLa5Q38ExTsgJyg5Pb469HADm4pbDrmXeT50ZP9bSRUhSzxxmLoPS1AQqaa3mmYC8lKDJqLUoYQntgQP-0_YpeNH01VUrsc4RM9s2DGpCQ989oM0WO2bdoXFPZW4GQrQcMNoHodkTJp21pLOptxYyIlz9Ry5VGWGgA7KRoCxCmxiAGHAsLAbBI-j7RQ4IK9lHYAnF67YQDfbOKnlNdjtuhn2Rwa1Lo7tA7QEJko7y2Fu5jBo7LL0yayIAsutSkMyYV_W22LrgPLXPgqFblCsD0OI_IIQlDrSnClX-koW9dxxpw5Z3_PD0kDJD-eliegqFhs8JvSH5NtMDhCrHz6ylJv7bqhQaALl6rEfMRj3gKw6ScQC1GYaRhFaLSmXDEuVd3pcXE3i5cBSTCI1fN9ueI3DN3CpSgDW51rsIeXrWBN2F4vIteLlCyl-6PaqZesNoSBLWquLbtfDEzp7aiNFgCCdJ-7czVzFDh2MAyhrhmb3KsYiMQ7EuAEs5GECcPJuZ5ZrSuKfWPe4JgHK2bzAhyZyIqsA4hpJMSrdRWC0CqeD6jpfpujEmEVK_qxvEYtDHY6va0z70RaZ9ReV2AzCJ9CdWv7ccz9OYiVo6IpZ7HC54qgsg6ZBQK9D8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=m20RciPzXbjetMoSYqr5uA4mDE_Ly4p6lG-xajNLgnqy3k3LzrpLa5Q38ExTsgJyg5Pb469HADm4pbDrmXeT50ZP9bSRUhSzxxmLoPS1AQqaa3mmYC8lKDJqLUoYQntgQP-0_YpeNH01VUrsc4RM9s2DGpCQ989oM0WO2bdoXFPZW4GQrQcMNoHodkTJp21pLOptxYyIlz9Ry5VGWGgA7KRoCxCmxiAGHAsLAbBI-j7RQ4IK9lHYAnF67YQDfbOKnlNdjtuhn2Rwa1Lo7tA7QEJko7y2Fu5jBo7LL0yayIAsutSkMyYV_W22LrgPLXPgqFblCsD0OI_IIQlDrSnClX-koW9dxxpw5Z3_PD0kDJD-eliegqFhs8JvSH5NtMDhCrHz6ylJv7bqhQaALl6rEfMRj3gKw6ScQC1GYaRhFaLSmXDEuVd3pcXE3i5cBSTCI1fN9ueI3DN3CpSgDW51rsIeXrWBN2F4vIteLlCyl-6PaqZesNoSBLWquLbtfDEzp7aiNFgCCdJ-7czVzFDh2MAyhrhmb3KsYiMQ7EuAEs5GECcPJuZ5ZrSuKfWPe4JgHK2bzAhyZyIqsA4hpJMSrdRWC0CqeD6jpfpujEmEVK_qxvEYtDHY6va0z70RaZ9ReV2AzCJ9CdWv7ccz9OYiVo6IpZ7HC54qgsg6ZBQK9D8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVg-mLwoE7ldlPJWCI2E4_agwbqnXs9cG3NT-pIbfNrgcyqecA5kt-5aKZF6aqKj_wt13zcMqY_yxqGtIzUEw0XChRNfDAbFPjbySt_srTq9NJ1I5-_ZIaSE-yLBpCH-ymW3EYnhb-2SceTsaAtDvXIdbIzIr2BkAmk6Qs7Phsuoz6XWIzD5vyS8xecOuHKbnwhtd6XPlYPhX5ajKsoE28RgYVBakps63nsm8iUquuc86-b4X8vRFP6wmsX_fmUFSEYdhJEoSuA9vg8aAjFdd5GJcQivdB4DH-BMoTp1GfDh4UVuMauBs2oZ6a-YRT_yEYnOKXwYI20_VcTKIzbA7A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=jnE7umpd0jwnDHd8WxIpWH1ookmXHYWyX0SAox8P-RT5sI8n1bS8Gx1KWTI9j9qX5DCTb0iwfUp9chNfZJOO5GcKX76kuMSQ_Kaek_NwlgYUjhSqDZ8sONItyWUjypsoKStB7sA1uuRno6uaHFmYJ0dLGI7i-L2B7a1KJTA2plav5ccUYR-m8KGLAGI_H4oSxrK2C9v9RYF3ctwhpshdI0stAYl2KGcD-FlKAXfmVVwJiI31ntMthtEaFUdRf5KISPdW4AnD5SGozMHKOoxahk1GQ_0GdmwpRmbRdYO4-a8ZmkVsDXTR8qMpQmHpUp2ZTCjO_1bFbG_lXE--p2EKkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=jnE7umpd0jwnDHd8WxIpWH1ookmXHYWyX0SAox8P-RT5sI8n1bS8Gx1KWTI9j9qX5DCTb0iwfUp9chNfZJOO5GcKX76kuMSQ_Kaek_NwlgYUjhSqDZ8sONItyWUjypsoKStB7sA1uuRno6uaHFmYJ0dLGI7i-L2B7a1KJTA2plav5ccUYR-m8KGLAGI_H4oSxrK2C9v9RYF3ctwhpshdI0stAYl2KGcD-FlKAXfmVVwJiI31ntMthtEaFUdRf5KISPdW4AnD5SGozMHKOoxahk1GQ_0GdmwpRmbRdYO4-a8ZmkVsDXTR8qMpQmHpUp2ZTCjO_1bFbG_lXE--p2EKkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpV7E17OEyeTrxsEJDvL4HBPwyG_MVWOP2F7aCrBUR3fpitnDyMel07mdklbeTlT-AGkWHA2-gveqMFDnrqYGPB91K1B3Q6aLdqYekbwoMoKIMSOQBQnYlcEToeJYsT6x8ROdR_8AjCQ3--RVFtt6cF599YbrPG4a8_OKU3qIDwRJwYmIdhR4Dab4AB5L4vxLQ8rPJqohozXN6sf4-_uHHrItn3xErA2-TJtMYifTUp34hDO_BLcu6ZlFBbrPn0yk0JH8TGvObJ9sRn0zA4eUtDuZEeTZHBGqwrM4E4MOOhZpfxi6atqafpFUCs7rn8FieThjlDreQy0mI498eiTlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGWANpn1OWP3k_wpPiQvKlJaGy3Ks0KppqzdlehIHzKZC150m7DSM5vHJPFtP8T4BqWSMrARJgYuLIX9gUHnaLnfzED2PxPVko97s9kgZrOk5W1UcAKKywk-H4VOW05T397harDwU3vyl5L-QzffDVM6Ak3WQV3x-S4AftaM9NcdmzYbmkDZboakDVic89HCfxklyOfTOqjCNOQWP6QGSn-y8cLfhMrWJy2j9JddNWMvJ-0qHN6jQGP15UTbsTCHcrZc0Hq2CzQN-_pCCW0CrAcoxOWRbrixkOaebAD2xdJlFDUWHOx4uJXNbZVxfuc8ifG1x0BUN9JTOf2zZ3HHUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbd6ZelJH-3yG7Wv25X4ehVFaLWy6BltzlZ99ToAT-NAXMyr0ze-3c4Nn292mI7yAUWwc3Ng-u-Ymy72bn5dl-6KzX1E419Tgq00zSWSArSBoriI9b7iLqA3A14D-lK1J3hRuvPVxGFEJBe1ykPEoSrq1jp9L-lloxAOUlvuMOpF7ZPjpC_tNN-4S2GRd7Hz3MSqbgWLQZ1OniOGCzBiXaltgtj_YhWAfldCkbLyXmJRp5gIXG4y1AZabKIvs_Lr04d9rMSxMKr-kt4EIJCBMlENGjLiYfM97VFLhKIgE9YLh-DozMm4jENRGcMI8bkH-wMWb0dV0UW3Mc5mzjtJ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=hhTKQy4tD6uzjFctY61uWDbKBAlHpyCz6Lch3tT4I7b27P95KcMoI6Rav1_TwkpooFoTR0E0iDa1gImvgTb20ZQxejmo7TBuUpNeJ_qfzjG5umNeSsJsWcTFAIG0u3OWbbMmubBTifgafPkPYEt8zAF0Uuh8rHqk17rqnwCj63bLsdwLhOVypuayKOvMHV7wjGST6uesX0j0f0IDZ37jvn3BjRCt-A41a3bb8OfSZNdKQPV656DIWL75dP9yTQhE8c5Qpg8xf44xhwCUQaFYY6KJ0RxscoxE95xiiRx3XWFGuMlE3-JXpFfGKKGDKSpPiAU7lsxDXxmGO4d-B0CfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=hhTKQy4tD6uzjFctY61uWDbKBAlHpyCz6Lch3tT4I7b27P95KcMoI6Rav1_TwkpooFoTR0E0iDa1gImvgTb20ZQxejmo7TBuUpNeJ_qfzjG5umNeSsJsWcTFAIG0u3OWbbMmubBTifgafPkPYEt8zAF0Uuh8rHqk17rqnwCj63bLsdwLhOVypuayKOvMHV7wjGST6uesX0j0f0IDZ37jvn3BjRCt-A41a3bb8OfSZNdKQPV656DIWL75dP9yTQhE8c5Qpg8xf44xhwCUQaFYY6KJ0RxscoxE95xiiRx3XWFGuMlE3-JXpFfGKKGDKSpPiAU7lsxDXxmGO4d-B0CfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrF78brhpJHaWcDDvsAHx4ljK-nlDYwU-oPeqtTfiAm7SU1IiSCFW0Eg4n17rMHJPuglqJUuMEQRQLpanIxf0oVuOJ_lDfhjk0J3s99pLNAwelLY9D23aujJeVggjGxjAhkAuV1KP6kg_NgY9MtwwXtLqvjniyLbOQAybWm5YO8239GBRXPt3s6jBO_cYEEZUKGdyJoUnXzPYjrKG4oZY4Rva1QcFxZrvJO5T3Vd95zWNLUSu0XIbyTFIC8wRSmWyCiuRy6ZjuhOLlqn8nFu9yU02-ahxKCfSk7DPyEaes_EviAvbKbW90Rq3PsAW9mh9QOnq7wQs2QxlNvbL7TWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu4eRL16sgwuMMQPiIQKzOQ9tMXPyZJkO4r8j-AXeXAGtbn4tXR39qbVQMh7R1yYrdYUDvkwQnKWl-9bYaRw1a_Ss-VDu58OQz6xX9fSzAgyVAkq2zde0DleBzvQvo8of7ORoVE0KI_jyunCPAOPJs705x0x-rmBm-SD4t1laTQjOkq2EFW6PD1YiM3VV-z45p3Dw98ue3OtdF4JoUQfSMZojnfkjOmhE2zcLHjzQTF05jy8WlwY7dtkqtIft5vJZWJfyjNYdGmnTxj3Dwokp2PIhvNkANpJiPRRvmyI4TX_qddFFnhSkQjSyEvIU34n9zIf_0khjLahj1O1jQf9wqas" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu4eRL16sgwuMMQPiIQKzOQ9tMXPyZJkO4r8j-AXeXAGtbn4tXR39qbVQMh7R1yYrdYUDvkwQnKWl-9bYaRw1a_Ss-VDu58OQz6xX9fSzAgyVAkq2zde0DleBzvQvo8of7ORoVE0KI_jyunCPAOPJs705x0x-rmBm-SD4t1laTQjOkq2EFW6PD1YiM3VV-z45p3Dw98ue3OtdF4JoUQfSMZojnfkjOmhE2zcLHjzQTF05jy8WlwY7dtkqtIft5vJZWJfyjNYdGmnTxj3Dwokp2PIhvNkANpJiPRRvmyI4TX_qddFFnhSkQjSyEvIU34n9zIf_0khjLahj1O1jQf9wqas" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=I6H-xhY8iIUpo635gpAGdHvLrjQu9nJjyLrD1-2gVAK65jddsVaXSktW1Bh2WdEuJxTUDPa8xCpJjhOliBXMSTCH5-6_wdIABD3W0GxlHUznq7r9uO-KERnfb8OrlRDP5msw2iR-lGz0iKtGICLb7DgCijVIg9iE9vs30i55Ivzrzq5uw7YY1tmwm9y1XDU0-_RssEEPXcGfhn7IvPFypqFhhPkw5kCcL-E9s2xOz-Iy7_t60sA5j5b3694qnflHu4XaiAMGQHoFs0VgzT-5vGWsFaAJE60Nv0306smJ1nL22L9wEU6Xcnrg-LA2QBziIfIaYDDmc8nUs4EGZxsAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=I6H-xhY8iIUpo635gpAGdHvLrjQu9nJjyLrD1-2gVAK65jddsVaXSktW1Bh2WdEuJxTUDPa8xCpJjhOliBXMSTCH5-6_wdIABD3W0GxlHUznq7r9uO-KERnfb8OrlRDP5msw2iR-lGz0iKtGICLb7DgCijVIg9iE9vs30i55Ivzrzq5uw7YY1tmwm9y1XDU0-_RssEEPXcGfhn7IvPFypqFhhPkw5kCcL-E9s2xOz-Iy7_t60sA5j5b3694qnflHu4XaiAMGQHoFs0VgzT-5vGWsFaAJE60Nv0306smJ1nL22L9wEU6Xcnrg-LA2QBziIfIaYDDmc8nUs4EGZxsAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=BBMEZcCiTfByA1JmjIoSkjxhFEL-_ZdTlsn7RMgNrLqV8Gxq4BhbIZb3RjlSd21U7TXEVlvJeMawNElqvRfUJson3dixFFkUOVASuAUjO7QSbO3Lkl-nX7nNxjYtS9sfMIJJw8X8qnDlOn7DGpiWKEqbzCmVT38jb_ZoGByl-MuOeyRhQr-d9VxoHdP9vV6YVstDAyW4PUsEDe32I6rqBcEo9m1cDAra8R39t8phD-RgaV5GuvP0hkNMx9_xDlnx3b1Xhw4ak_T1vHG8UBONvlUcnXm-daokoq4s0lWkMAH3f6Opn9ODQ2TQ8vbyL7m9r-FwUkxYeWm7f6CiqZm70SHvYnxW5NzamYTt0C1wQHBE4P-yr1gTxq2GqwMug1SRzhNRRVGN67vbhCxFuSFnyXGbv2TXbeBgRB5t9grUx5Ao1HCx5YIeVH89dDkqTVTgu0TunQCaN8yUQwr43WnxhzJw2RouZPpwMv98DNU28SLmDOqBr0YTmNt2bI3SsO-uAUHZ9SO79qEy_ePbChWk3Bz98cKoxLOu8mDUemPypfcnfkzi5XRn8p1WwjEclYL3zdqy2bZdMZeOvSTMUNXk9igx6AIq2ONBggCHfnPYnUjONnuod6e7WMwFLu5w9c3eyOprrF6D4ILlgcUygkP-yMmvGhesG3U5bTBEGZRHrAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=BBMEZcCiTfByA1JmjIoSkjxhFEL-_ZdTlsn7RMgNrLqV8Gxq4BhbIZb3RjlSd21U7TXEVlvJeMawNElqvRfUJson3dixFFkUOVASuAUjO7QSbO3Lkl-nX7nNxjYtS9sfMIJJw8X8qnDlOn7DGpiWKEqbzCmVT38jb_ZoGByl-MuOeyRhQr-d9VxoHdP9vV6YVstDAyW4PUsEDe32I6rqBcEo9m1cDAra8R39t8phD-RgaV5GuvP0hkNMx9_xDlnx3b1Xhw4ak_T1vHG8UBONvlUcnXm-daokoq4s0lWkMAH3f6Opn9ODQ2TQ8vbyL7m9r-FwUkxYeWm7f6CiqZm70SHvYnxW5NzamYTt0C1wQHBE4P-yr1gTxq2GqwMug1SRzhNRRVGN67vbhCxFuSFnyXGbv2TXbeBgRB5t9grUx5Ao1HCx5YIeVH89dDkqTVTgu0TunQCaN8yUQwr43WnxhzJw2RouZPpwMv98DNU28SLmDOqBr0YTmNt2bI3SsO-uAUHZ9SO79qEy_ePbChWk3Bz98cKoxLOu8mDUemPypfcnfkzi5XRn8p1WwjEclYL3zdqy2bZdMZeOvSTMUNXk9igx6AIq2ONBggCHfnPYnUjONnuod6e7WMwFLu5w9c3eyOprrF6D4ILlgcUygkP-yMmvGhesG3U5bTBEGZRHrAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=HCNYHasKv4yZctEsR2hynfU6l3JdI974CpRTTja7MErlF0Y6z6ddVBaJe6LmGOc2oJc5NZQT9n13JuSIFvYI_uT_-WGVYyclHu6I7y3CwBuAUS7wJaeNFtbZ4RMWhfL0HCK-xOlVPokkp-9Ge18jPVTBMLbrsd4cR4TUqtSDiuQm9e8veNZx7_WfiMWzl4u90wOsroNtqd2jvEB1JpDoqtFyoeuQRbmtfwKmRqpMkVYiECxyLhn-jdE-VTIhCOsbrCW3iHxVIo89gVaMQb_omJtINNl_8AkBGcXS2WB59R0CFVIymQNZDKIdC9quP3A_8zmUdr_5Wx4IOHgOHEs9_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=HCNYHasKv4yZctEsR2hynfU6l3JdI974CpRTTja7MErlF0Y6z6ddVBaJe6LmGOc2oJc5NZQT9n13JuSIFvYI_uT_-WGVYyclHu6I7y3CwBuAUS7wJaeNFtbZ4RMWhfL0HCK-xOlVPokkp-9Ge18jPVTBMLbrsd4cR4TUqtSDiuQm9e8veNZx7_WfiMWzl4u90wOsroNtqd2jvEB1JpDoqtFyoeuQRbmtfwKmRqpMkVYiECxyLhn-jdE-VTIhCOsbrCW3iHxVIo89gVaMQb_omJtINNl_8AkBGcXS2WB59R0CFVIymQNZDKIdC9quP3A_8zmUdr_5Wx4IOHgOHEs9_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZQTFcFl4XZSsfs8-Mwbcroc5Dcfohhuv5zp3C4ITj7uEhJHxTmTCKBEWEBvkjCRq_86Ib8TtUpSFHgWLM9_91nH_KrfFDbzhjgBdAu5pkkCEYx4qml1uqq4T1RWyQUJVzF1xatOeCD_906lY7EQtiOiBFZ8ankVh2cGZp5iQ3tSJ9Khgbq7RIfnpqY1YrnX8F0VQJ0ViN0EGND92P4mAg4bgZSVkYNelxiU856pSXFvgcSyvpDCvXeasXfkD6QnowZEFicWhptwZZRtc4qcUaGerndUseajugAoBfaI-4CiZu848yz7i3WWeWLJxeEaR-dgrYpi0EHbwpJn7lwusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=JphrKtf-3HyvrG_aM19yMIYx4p8VVNHtSajGYByVzrj3n4HNtOSwplcv0YTgebl4yH1KP1qZM-X_g1ro_Rf-5fvox8bMDPMKZciGqYipvFOClZWjrLIZepXQbbs3wVEC5_jnZZ_o312S0vIuLBFLmUsuBBiSdip4qxtB_0KeoeodX28soVVSYUEmIjH1N6c2hzbSZxuXMQcDCGzxr-AIoZcLbll-qweTN8UNxGAlaOOQfI_Npw3ePC27pytN6vU-vebxwtl4XO4tqikSp_SDO4m0scN2s9Dl0DeHwKo8EkFWbgHBeBD3nLBnVMEbqkFN5YGAbGRHzy7uol_MELYvIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=JphrKtf-3HyvrG_aM19yMIYx4p8VVNHtSajGYByVzrj3n4HNtOSwplcv0YTgebl4yH1KP1qZM-X_g1ro_Rf-5fvox8bMDPMKZciGqYipvFOClZWjrLIZepXQbbs3wVEC5_jnZZ_o312S0vIuLBFLmUsuBBiSdip4qxtB_0KeoeodX28soVVSYUEmIjH1N6c2hzbSZxuXMQcDCGzxr-AIoZcLbll-qweTN8UNxGAlaOOQfI_Npw3ePC27pytN6vU-vebxwtl4XO4tqikSp_SDO4m0scN2s9Dl0DeHwKo8EkFWbgHBeBD3nLBnVMEbqkFN5YGAbGRHzy7uol_MELYvIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=GY-ozxObt9LR_ta0CRDfO73h9vR3DxOnH218QP3-6aJUAuWLkeICULRXTQsm-uXD1abf1-t-Ad0xuugsTJhFrCEO12XQA4o2yn7k54ru5voVwBWX9BYdOb1htsbRWyVkZgomRi7MjZA-UUNdEvsyeOEz-ay0dztAvf2EiH4yI_qYhZNInOuObwbf4Fk_UmiEWnICFGug-4E2uWRiKXQbyGrNt-8xSfekDCAxxgV-gNBdFxK3AJhh0V-7v_Ggkmk7SWvJswRPXOgu88-ejkuZMCDzaIN1cg9wrZlNPr5z2LAkSHivbvEHL1J3LfNNkHJXlN5dGC0AwFfunYSYbyP2cb6UddGzMCD4iF5w3j8bJENjdg2ruShAOaiQw4debOzjxGicfGoZGqI1OA-V_VivBECbdQcJ4w7RpHq3_6jVI8xqIy0J27_iZxjWio4pTgLMJI0gm4yWBfwPQaPMdTNQcicQmxR_YgRzgTjNxsg0sokSr6zLXH9CPRWC1GrBa-8Ne1dhBjezFeRTgqEVjft0NoTIV2fPRhRIgKXt-2C0QTUTtkm1AkuaTKHEZ6hJz-Ylsy35iXq7eS2HOaUkR0QhyKAFxZnSntLUPccFQF6aPwSRY4eyzvDG0lpZjt2boaV2yxIMhg5ce9Kn-Jgthpqqk1oDtYlUcQx1JpVmNNncufg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=GY-ozxObt9LR_ta0CRDfO73h9vR3DxOnH218QP3-6aJUAuWLkeICULRXTQsm-uXD1abf1-t-Ad0xuugsTJhFrCEO12XQA4o2yn7k54ru5voVwBWX9BYdOb1htsbRWyVkZgomRi7MjZA-UUNdEvsyeOEz-ay0dztAvf2EiH4yI_qYhZNInOuObwbf4Fk_UmiEWnICFGug-4E2uWRiKXQbyGrNt-8xSfekDCAxxgV-gNBdFxK3AJhh0V-7v_Ggkmk7SWvJswRPXOgu88-ejkuZMCDzaIN1cg9wrZlNPr5z2LAkSHivbvEHL1J3LfNNkHJXlN5dGC0AwFfunYSYbyP2cb6UddGzMCD4iF5w3j8bJENjdg2ruShAOaiQw4debOzjxGicfGoZGqI1OA-V_VivBECbdQcJ4w7RpHq3_6jVI8xqIy0J27_iZxjWio4pTgLMJI0gm4yWBfwPQaPMdTNQcicQmxR_YgRzgTjNxsg0sokSr6zLXH9CPRWC1GrBa-8Ne1dhBjezFeRTgqEVjft0NoTIV2fPRhRIgKXt-2C0QTUTtkm1AkuaTKHEZ6hJz-Ylsy35iXq7eS2HOaUkR0QhyKAFxZnSntLUPccFQF6aPwSRY4eyzvDG0lpZjt2boaV2yxIMhg5ce9Kn-Jgthpqqk1oDtYlUcQx1JpVmNNncufg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7_0xH3p4OS9kCXDvJoWxPUsrHrVFESZZ4YqacdWrSg3mBLiQGLMdIkbz3D1fOy4V-bfXoG9rsNTE_UIF2XxPctlBDhOH6jYLPBwyXgFv1o_2HdmKg2b4JuXZSN6Ao-qeRl_eY9vrPgWDoSpnZ25KqYowsIOUCen7k0MQcdr93RQ_TFUDQSfkWbqpzvYC6gBihFDi8tjAdGWeiFCOCEI6u01ctagGT2jF9rJEwmFH04pffWCqDrgT79iz90SwOuHNYfwOIfC1dkk3shwRI3N9g4EwoUQKIr4fBjst-dhWITxizZtde19UwhgowRCX8cEz8HVCf2EAR_qJN2s6H8QxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=H5d1vSepRpo3iPqAhkkQy2gH9msem5QUCp6ouS_9hmvhyj--X4uyHnnE2XkASodO_YAI4Kq0nfTbXCvsUV_vYHoTQmPZi2DWqVtqTBLfj9bZy-qM0nDvwbNK24ALWuGcFiRpwwcIDVIZHns3cX3Y39fRtLrDQ-DYJoU5KygtP7RJ55Pw8s8pB_nbWNpTS6m-ZsQr88YhBg1yaq3-nktJmOMY9WZQi8HTgmmh3jLSFeq9t8m42sHrb95KobfUp4qEZS-zI-34JH_5k5Pm44f0d2w0zkhWr_tBxmDPmc7zzSLwH1WmXspAy7L7EngV-YId-xOSg_4KQfxTT2xXeBaFHULm9VZJvSlTW5qz_zcjS9U4TpB6PoT_B9160l6isUAbgbeJRaTUFivfWyiTCVxBsJTL8ctk0SF84JSpxPky-QVp71eKLm0cRiN-jl_p8v-DArzl_2almiX8Hy7wKu7b2xSwMteQw5_DJe5V75IunqTtgK751WLIph4fx7MTxIPnRO0j84o07gPh8w0lcnhZ3ECD2PFdJMoLJloEzbZfGMkWdxYWXG7FumwCVd0WSpSCUBXKAKNaBeFVO6h8-QjK1-DSfXW5Q3vHgiNAsmW3f0n9UViKeoEFLFHhQNjEoCjR88zE5-WDE-JYRFlgD7JZLFIT1Hg77W-qFAn1Z0mLG7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=H5d1vSepRpo3iPqAhkkQy2gH9msem5QUCp6ouS_9hmvhyj--X4uyHnnE2XkASodO_YAI4Kq0nfTbXCvsUV_vYHoTQmPZi2DWqVtqTBLfj9bZy-qM0nDvwbNK24ALWuGcFiRpwwcIDVIZHns3cX3Y39fRtLrDQ-DYJoU5KygtP7RJ55Pw8s8pB_nbWNpTS6m-ZsQr88YhBg1yaq3-nktJmOMY9WZQi8HTgmmh3jLSFeq9t8m42sHrb95KobfUp4qEZS-zI-34JH_5k5Pm44f0d2w0zkhWr_tBxmDPmc7zzSLwH1WmXspAy7L7EngV-YId-xOSg_4KQfxTT2xXeBaFHULm9VZJvSlTW5qz_zcjS9U4TpB6PoT_B9160l6isUAbgbeJRaTUFivfWyiTCVxBsJTL8ctk0SF84JSpxPky-QVp71eKLm0cRiN-jl_p8v-DArzl_2almiX8Hy7wKu7b2xSwMteQw5_DJe5V75IunqTtgK751WLIph4fx7MTxIPnRO0j84o07gPh8w0lcnhZ3ECD2PFdJMoLJloEzbZfGMkWdxYWXG7FumwCVd0WSpSCUBXKAKNaBeFVO6h8-QjK1-DSfXW5Q3vHgiNAsmW3f0n9UViKeoEFLFHhQNjEoCjR88zE5-WDE-JYRFlgD7JZLFIT1Hg77W-qFAn1Z0mLG7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=P6hRgTkhEvEAZnFqVk4jQqCG69G0u8K0AWIvy6_yp-5QUgDUKU6o3ZLF8on9qOkSFlvjvUIXX29VXXw9PfWLyhICJrh9pZo6Jb_SxnwE3k0JGxTZSAV24VHYcdQbfKqm88fYOmy8XTitacwQIUU2g7tpQJdGpoyh1JW0ErDuIFr7XJ_McqdMnrxMktseqKTETV1AQ9Z_PzvIndON2M52BjxQ_ni2lG7a6gBXdH_pWXzaqxGhAr4LXGXXrcts2SwAVR667nOFAbO8L5UGjX_ZchYtXKGpcWHm4H52vA5Zs9Mxbiki2IRZq2f-_KQsnNqv-_i6_RGFHjGZdL3k31zZkpOMMUeSOZfYClVXM8ERhmrbn9y_ksOGFNvlCdSsRPtODJOZ4b8q2PtxU0taGiW31Y7eK5JiG34VT9U35nFgz7LNevd-DDYjRpmlN_wtOCOYOeRB-BrhC4K149Xfo5GKv3VnGdWr1o9uRC7a3eYgmBrdvt8k0UFKZqIHllFCxjNWdEWs4W98XqJU5tPBsiRXCwHxCza6KHTT4kwlzCRNo6Md4Q19eOLCxffsCYTVezi2qPrRiBU3NC-X06mmqyntZj_uewh0OVdbxakRYmzL1-RudMffU5UvS4ARGjjCIEIch0orK8HOA58VC0uEwYQjf-NnTVy0jEcZk8WXFlr_vks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=P6hRgTkhEvEAZnFqVk4jQqCG69G0u8K0AWIvy6_yp-5QUgDUKU6o3ZLF8on9qOkSFlvjvUIXX29VXXw9PfWLyhICJrh9pZo6Jb_SxnwE3k0JGxTZSAV24VHYcdQbfKqm88fYOmy8XTitacwQIUU2g7tpQJdGpoyh1JW0ErDuIFr7XJ_McqdMnrxMktseqKTETV1AQ9Z_PzvIndON2M52BjxQ_ni2lG7a6gBXdH_pWXzaqxGhAr4LXGXXrcts2SwAVR667nOFAbO8L5UGjX_ZchYtXKGpcWHm4H52vA5Zs9Mxbiki2IRZq2f-_KQsnNqv-_i6_RGFHjGZdL3k31zZkpOMMUeSOZfYClVXM8ERhmrbn9y_ksOGFNvlCdSsRPtODJOZ4b8q2PtxU0taGiW31Y7eK5JiG34VT9U35nFgz7LNevd-DDYjRpmlN_wtOCOYOeRB-BrhC4K149Xfo5GKv3VnGdWr1o9uRC7a3eYgmBrdvt8k0UFKZqIHllFCxjNWdEWs4W98XqJU5tPBsiRXCwHxCza6KHTT4kwlzCRNo6Md4Q19eOLCxffsCYTVezi2qPrRiBU3NC-X06mmqyntZj_uewh0OVdbxakRYmzL1-RudMffU5UvS4ARGjjCIEIch0orK8HOA58VC0uEwYQjf-NnTVy0jEcZk8WXFlr_vks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=pngH0L1VM-HEHIvHzL1_6IWThHzm1JE5-e9Xqer7OXHG_kRzUYd72_SMeMAIo5Ow_Wo0jHq5sw6Qn1TFsQyl8eKulRZf40fBSr-W8x-GT8AMLLkriMdsHCBEpxogEWryFrW6FRvAv9p8ruLcZ5-rHJOqwBjr_HWIAgGG6gjAp4sSFEd_t1g5gkw963xMGIwyYhFklkpkLYB6JuseqLfLabVPuiAOq_FHV_vMFxhWMbxGu9LTW6ernpSe8hPrvNwi6LvfoAxUoRKetlgaErt52NpfkDHuGvz7IKzU1r3EoIygwrYoTKutR78xUrpo_jmjlESmEn5TyrYWLHrgyuyaCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=pngH0L1VM-HEHIvHzL1_6IWThHzm1JE5-e9Xqer7OXHG_kRzUYd72_SMeMAIo5Ow_Wo0jHq5sw6Qn1TFsQyl8eKulRZf40fBSr-W8x-GT8AMLLkriMdsHCBEpxogEWryFrW6FRvAv9p8ruLcZ5-rHJOqwBjr_HWIAgGG6gjAp4sSFEd_t1g5gkw963xMGIwyYhFklkpkLYB6JuseqLfLabVPuiAOq_FHV_vMFxhWMbxGu9LTW6ernpSe8hPrvNwi6LvfoAxUoRKetlgaErt52NpfkDHuGvz7IKzU1r3EoIygwrYoTKutR78xUrpo_jmjlESmEn5TyrYWLHrgyuyaCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=k8cu_yTM_BGb7k1vQAN83dnzR3zOHcizDXLfGESokWHI-6bgt4v--H8A-Ns7wsHrn_ICCBTx6vZf0xuLOTMBlb7NBihTBjyhSgWcu9tsUzqWKWrV_zFEe6rqWFRXk4HysZBFwRQOf_daxkoF_lpDoRA_caL9ztkrMYxj_2EcHa1fKmUa8vbVWN8qyZGqbuzcgh2G4Nz3945-gYvCdN7ro_3ICzHbLidRi1mc5vzROJzzF704_iUgLffss9LyFdkqWltFku6BuUCeFM9qWhMvh8WCE2F8eo1rkIIo4tFMzlxgE8xcSs1MrpgY45Kp4n7OCvu7VRkkGfW2K6VjSBt4aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=k8cu_yTM_BGb7k1vQAN83dnzR3zOHcizDXLfGESokWHI-6bgt4v--H8A-Ns7wsHrn_ICCBTx6vZf0xuLOTMBlb7NBihTBjyhSgWcu9tsUzqWKWrV_zFEe6rqWFRXk4HysZBFwRQOf_daxkoF_lpDoRA_caL9ztkrMYxj_2EcHa1fKmUa8vbVWN8qyZGqbuzcgh2G4Nz3945-gYvCdN7ro_3ICzHbLidRi1mc5vzROJzzF704_iUgLffss9LyFdkqWltFku6BuUCeFM9qWhMvh8WCE2F8eo1rkIIo4tFMzlxgE8xcSs1MrpgY45Kp4n7OCvu7VRkkGfW2K6VjSBt4aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=oL602BJW0lyXweLF65tdx3H86WrttXdnXwJWZSSjoBMieBRbbydu4_quJDTVyg-JJZLoJblREZYlkDpsUyYZypJERJqcp7E7_6NTH5mW-nZvdWvcjc4YFokDbe1xd8W_Kg_lkSgxGx0MSKPaMaAZA88e5rtcIvlyEuOlFAMHC42X8LFZKO5mHv2U9HbVVCR_EGJAM6oLjM7IVVFlsOI_f3xxmcEbBHCXyKtfTvCwxd1obCVFrfUc0uaw8v9CvcOt7wmFnrU5XKbE7BWTF3Biwb2kv_Ce56TwA9JiAS1rFtA38bXIOHjmxi_iJvz3wMllmA20JtbaJLnn8LMQVKkhwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=oL602BJW0lyXweLF65tdx3H86WrttXdnXwJWZSSjoBMieBRbbydu4_quJDTVyg-JJZLoJblREZYlkDpsUyYZypJERJqcp7E7_6NTH5mW-nZvdWvcjc4YFokDbe1xd8W_Kg_lkSgxGx0MSKPaMaAZA88e5rtcIvlyEuOlFAMHC42X8LFZKO5mHv2U9HbVVCR_EGJAM6oLjM7IVVFlsOI_f3xxmcEbBHCXyKtfTvCwxd1obCVFrfUc0uaw8v9CvcOt7wmFnrU5XKbE7BWTF3Biwb2kv_Ce56TwA9JiAS1rFtA38bXIOHjmxi_iJvz3wMllmA20JtbaJLnn8LMQVKkhwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=CUwIawZj-QA5GsksLeseV1MM5vgzdqBzZjMlF2_DSuhpEx_FwqUYFM4P3zWDK3LVGohqBXeu80cegu68twK6Migxmyu2uiw8s_49pF1c1fRbMBCrPazDKCi8KCrBMTDPHAkoBZgBXK1YG8dS4LXYp24KlArEnThjl9ta20NFJsUrfQqjV49pBwFOBxNMiZv0ITN5ARAIuFXflgzIAfMV0CsHskGQUhnMiFTME_MorLhIBnj_RSUaX8e9RpMrb1_r00hUoiRdf3pjJ8L67QaFVnHm6fynrL4Cg2zwzgdaHdBiwhP2viXhd1vsCTZFfQTfVvlw-81fBZDic58yYZSzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=CUwIawZj-QA5GsksLeseV1MM5vgzdqBzZjMlF2_DSuhpEx_FwqUYFM4P3zWDK3LVGohqBXeu80cegu68twK6Migxmyu2uiw8s_49pF1c1fRbMBCrPazDKCi8KCrBMTDPHAkoBZgBXK1YG8dS4LXYp24KlArEnThjl9ta20NFJsUrfQqjV49pBwFOBxNMiZv0ITN5ARAIuFXflgzIAfMV0CsHskGQUhnMiFTME_MorLhIBnj_RSUaX8e9RpMrb1_r00hUoiRdf3pjJ8L67QaFVnHm6fynrL4Cg2zwzgdaHdBiwhP2viXhd1vsCTZFfQTfVvlw-81fBZDic58yYZSzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=HYcOCHazYxt3lKRPUNYoCykbK-Z93mXx1n9qECmsL-3Ol0IL43kqu4R3to3wvx7p1_nPF1HC7wvcoG4PDuh6x8KGd8fQ7UScqtCVrL-8oNY-BZFdtZ2FUmCFXkAZUm3WiuDK52nj0_ZHEnrTgfgzQhUZcRJ-ks3UcIm_bs-pL21yN6piPNz0doxK7AGIfAU3ZQuThIA1vhm5nsM_KDMQrwBhBifhe322IbbK65FzhWOoa_ftQ-B8aZBRs56k6IDdEOFOlmA4FpahDwv2fa6zPI3QWiHAHeU-w4YniNq5Zt-jtXkIlT4hgqZBvYw8DQYSTSgyqOMY4iwI1Zkqkz1AXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=HYcOCHazYxt3lKRPUNYoCykbK-Z93mXx1n9qECmsL-3Ol0IL43kqu4R3to3wvx7p1_nPF1HC7wvcoG4PDuh6x8KGd8fQ7UScqtCVrL-8oNY-BZFdtZ2FUmCFXkAZUm3WiuDK52nj0_ZHEnrTgfgzQhUZcRJ-ks3UcIm_bs-pL21yN6piPNz0doxK7AGIfAU3ZQuThIA1vhm5nsM_KDMQrwBhBifhe322IbbK65FzhWOoa_ftQ-B8aZBRs56k6IDdEOFOlmA4FpahDwv2fa6zPI3QWiHAHeU-w4YniNq5Zt-jtXkIlT4hgqZBvYw8DQYSTSgyqOMY4iwI1Zkqkz1AXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=IloZrVe98yXFIKI5Rx-KrJPzLtc7XGLZev_wq3WBtNdTEI7zkPTTMTEHZgvliXYplQ3a9nUhiG3FmJ7hgRmU3oKnEQwpbfYFZDwxXmmSnMQEvTFFUsZX-Y9qMYjg_kn0mr6sbso7_Oo2lRPoCczKBvYehydjHy45wRZvnIdh8xzypc4WirGYohFt005aWr3fGSNVPjXPrLxD-Ayyq7nU98za4i9qoWDuC3SKqhey7ye-JtL3OJrdmq6sY0v16LcgvZqKydDCgdeEg8czwijO4WRIlGiL29Mkyj87ODLKtn8G3hFE3yLXoX3P0HQA-QlDpfzS3w9d8OTBuJpRas66-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=IloZrVe98yXFIKI5Rx-KrJPzLtc7XGLZev_wq3WBtNdTEI7zkPTTMTEHZgvliXYplQ3a9nUhiG3FmJ7hgRmU3oKnEQwpbfYFZDwxXmmSnMQEvTFFUsZX-Y9qMYjg_kn0mr6sbso7_Oo2lRPoCczKBvYehydjHy45wRZvnIdh8xzypc4WirGYohFt005aWr3fGSNVPjXPrLxD-Ayyq7nU98za4i9qoWDuC3SKqhey7ye-JtL3OJrdmq6sY0v16LcgvZqKydDCgdeEg8czwijO4WRIlGiL29Mkyj87ODLKtn8G3hFE3yLXoX3P0HQA-QlDpfzS3w9d8OTBuJpRas66-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=KUOQkbg0O5Bv-zduFVRJulggzhN-woL_IOJEYnOrlbc2Ukip4pFuWcKObhAbdmw1k41HqDAu2rBvnBk7ZO5YiKKyY7em9Bgw8gwJBrzpschIh04u2DvRUyBk4hTOmMcvaDItZBDffzr_pS9xtUfSyI3DeRLeLLY13k6tXJ6yA1oj24o5PYUmk_DDh7rjdTZek0mIY6oOXlVlCoM1n9RJ0tuc1ni41EMXM9Kr_TpraRJxaWmn2rtwdZKFhA3P8hh_ic0sz-w7LHdWavwhPkVByaEFQiFMN3dPsgGhj6-t3ZnD8KDUWWGnyJkdbkA9qqW_WMXvnUSFd0TePCcSr2N4KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=KUOQkbg0O5Bv-zduFVRJulggzhN-woL_IOJEYnOrlbc2Ukip4pFuWcKObhAbdmw1k41HqDAu2rBvnBk7ZO5YiKKyY7em9Bgw8gwJBrzpschIh04u2DvRUyBk4hTOmMcvaDItZBDffzr_pS9xtUfSyI3DeRLeLLY13k6tXJ6yA1oj24o5PYUmk_DDh7rjdTZek0mIY6oOXlVlCoM1n9RJ0tuc1ni41EMXM9Kr_TpraRJxaWmn2rtwdZKFhA3P8hh_ic0sz-w7LHdWavwhPkVByaEFQiFMN3dPsgGhj6-t3ZnD8KDUWWGnyJkdbkA9qqW_WMXvnUSFd0TePCcSr2N4KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJloxYDZRu8MdllckpRsAmLLS7Cm5jI3yFFq-v3z-36cLn87C1VVCN3ujjud7SzMWy67IVqULD8jv93XhA7LEPCV7CYCGwHZh3JXNYHhccWrTC4TaPg0fgFNxPhnxyptwHK73ejpbWQKpJUd6mGYeSdEwyIG3fmD4pGUL647j7i3and45WYkGluFpthBaRxatQ4mw2sabpbhcnYujTLG_eQ-CayMeOj7NydLIxI7sxcBnBSm1vtFNEvZsDq42v5uiJEPm_lrvvvwY1DfLCDR7FGRBWF7bMGHxoNOzn58NNvOveYTC2YLJhVZVi31JemaH7JYnLvZ4Fg2cfqbsEPBbQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=kYed-ReL09RoBuQuR3REQstSewvX9PqZ-JfSDzjf52mG-ptEWpuE3vthwle6qE9ncLO0Y10a1jzEGexBEi6-a3DIpNn5_0u-iMBL-L5jqQuoM7pXiD7qASKjz3JTQxdpPA1EgsKjQ1Ne7dKdt6CvHClR4glG0E4c5sGwhZi6TN_gonn3di41LJru6CpZnAnNICYm95gVfUwauqGoN6KBKkH8w75MjYCWERMQuJZG5DVSqk8n1zL52-7DRBBfw5BUvs0EY5_WbS7F7AKFgKitJsksf6FKe0PEEV6TwhhP372ldX0IvRvoULOvR_8t8jtA8RnR3QEMWYgf-EujQXOnmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=kYed-ReL09RoBuQuR3REQstSewvX9PqZ-JfSDzjf52mG-ptEWpuE3vthwle6qE9ncLO0Y10a1jzEGexBEi6-a3DIpNn5_0u-iMBL-L5jqQuoM7pXiD7qASKjz3JTQxdpPA1EgsKjQ1Ne7dKdt6CvHClR4glG0E4c5sGwhZi6TN_gonn3di41LJru6CpZnAnNICYm95gVfUwauqGoN6KBKkH8w75MjYCWERMQuJZG5DVSqk8n1zL52-7DRBBfw5BUvs0EY5_WbS7F7AKFgKitJsksf6FKe0PEEV6TwhhP372ldX0IvRvoULOvR_8t8jtA8RnR3QEMWYgf-EujQXOnmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=NMzUERWYQMTklY5stwOCDvD_qFTsuzu_uuJbr2qlpcdhqH_1pWO-Sc1OG7y-V09GKjog6hyXZ4oOaWHmxl14zQXDUbbpzvoPe-89ZM7qLv5WIKF5xgTTaIwFY648tM4WGinfumuIMQFakS3dCGHMfQmS9V4BSSeD35dXrKzuB52wOflhplvMlke6V_61zH-GaSQVzjUCTnQ0cbjgGfFrFUfFFWGYqL_O6GGbbcIdx3Rl_eThFOautf02q5BPGOiBU7mJYZBa1pfsxHwp-gbQyvWH2Ohp4pvqeqlrAR05euL0Vd5mQCyrV1_LpWRIt8NcP6zy-nZLI4EU-NHyO1ElhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=NMzUERWYQMTklY5stwOCDvD_qFTsuzu_uuJbr2qlpcdhqH_1pWO-Sc1OG7y-V09GKjog6hyXZ4oOaWHmxl14zQXDUbbpzvoPe-89ZM7qLv5WIKF5xgTTaIwFY648tM4WGinfumuIMQFakS3dCGHMfQmS9V4BSSeD35dXrKzuB52wOflhplvMlke6V_61zH-GaSQVzjUCTnQ0cbjgGfFrFUfFFWGYqL_O6GGbbcIdx3Rl_eThFOautf02q5BPGOiBU7mJYZBa1pfsxHwp-gbQyvWH2Ohp4pvqeqlrAR05euL0Vd5mQCyrV1_LpWRIt8NcP6zy-nZLI4EU-NHyO1ElhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=OU3KbQ8t-lN2z-2nbzI4x4pz-D4J2bUyOOxN4gya1DXugCz2ODX4qWMkck0-wkeG2Uq9mApWZyLigvyHjYdSDVSc62-ATiEbfhmynYjCVdaKKvS-Y10RUpOFZnE3lZ3-aRk6pGwiBLnw1_jv7jOdDKiBodDIZMZeOlZp7Bl2ck8Oq8fuMlMYEwUxECmAfaOMikHD59WDAcU5QDKsDj_8o9FIbaspL1v-DzuHt-qvR-KTP7ovgGKX9YlnYd1Yym8AhkFuMsGLvuj7p-4jvKyC_9hbJeNXLnQGQlDmhsbwEjWOgJpeIhc_9DR0jKrCJNgnclngBMLiIOwE_BAvzfhu3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=OU3KbQ8t-lN2z-2nbzI4x4pz-D4J2bUyOOxN4gya1DXugCz2ODX4qWMkck0-wkeG2Uq9mApWZyLigvyHjYdSDVSc62-ATiEbfhmynYjCVdaKKvS-Y10RUpOFZnE3lZ3-aRk6pGwiBLnw1_jv7jOdDKiBodDIZMZeOlZp7Bl2ck8Oq8fuMlMYEwUxECmAfaOMikHD59WDAcU5QDKsDj_8o9FIbaspL1v-DzuHt-qvR-KTP7ovgGKX9YlnYd1Yym8AhkFuMsGLvuj7p-4jvKyC_9hbJeNXLnQGQlDmhsbwEjWOgJpeIhc_9DR0jKrCJNgnclngBMLiIOwE_BAvzfhu3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=LPNHtMogEBdPeczoCGz13sSrhUgBtV4eSPCY5euIX7lCO-r-N-yyvYK8wp4WFwJD3_cNDwuWax3JAe4yJt5KiKKfEry-OdePerlGDjBbNk0C532pEN8mtjBTOOvBnFT2eOcFxMP0rJ9EvsPRur5IWsz_p3CojeVghomMPnBIY_p-jMuHw69LU2jZKaMRz917QvNthgeA9ERintE6VPuvED42_DbnpJVRSq7wPSwgeX9gMCDfobyOLhjwqFxgZ1jZ3jjbqlvS1dy-6YkZBgpM-Kla2f4BBHExokfTx8l75GMgHT2YQwlmLMVPgJCdcOq5zbo307UEeUHg3o_vOWoDXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=LPNHtMogEBdPeczoCGz13sSrhUgBtV4eSPCY5euIX7lCO-r-N-yyvYK8wp4WFwJD3_cNDwuWax3JAe4yJt5KiKKfEry-OdePerlGDjBbNk0C532pEN8mtjBTOOvBnFT2eOcFxMP0rJ9EvsPRur5IWsz_p3CojeVghomMPnBIY_p-jMuHw69LU2jZKaMRz917QvNthgeA9ERintE6VPuvED42_DbnpJVRSq7wPSwgeX9gMCDfobyOLhjwqFxgZ1jZ3jjbqlvS1dy-6YkZBgpM-Kla2f4BBHExokfTx8l75GMgHT2YQwlmLMVPgJCdcOq5zbo307UEeUHg3o_vOWoDXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apcd4vlaAoL7niIijfUUMiZx5xh7x5NJeFDe1MsEyrrrzQNd8M9EGdtTO9tFGg3T_sGrnEJIHxEe-Z2jBubsArALI0TQLmhsbOn1OalVAbl7R7EyNkd9KROX64ZBSSm-ALfif50iB5Thn7cxbpx-3UbIKOIEGa03Y9-J8QxlSkJWxWcIQE3AuMsdMSkIO0HwEM3K-0VC1sxtjrAecqXkCgsvnwHnRuONk4L_rM1a1_NLUTgozD-rmINuyoboKxewQQjG20GWtHPA-PSE5nnL2I2s1PS1j4OB-nEJTR5-QlKiU0wB6yyEfXpQFpLqMcHw7Qhs77ZOrSCI97HewYwXIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=LM2Uk91OqkAziGARP_Y_cXslMZXi8UaIDoYINZQHbQUoqJ_sj-BYW5nkLUV7NwEbrW22GxqA8wZCn637b3rUFGo6hmbJtid60p3nSPXrVDx8N-bjMHo0zraCbu0WeZRs_DfNT6zDXZWLBXvUl26u3AkawkHI3ut0bjFsAwrZ3SEZpDbdk7fBNHcmdLQYw1ZnxONsX9A16mU334U9lhGSkkfED9c3SyA2uV4RMFjMY7jl9pe-62xdthsG4dHxV2RWB1MEXT6xk1lUxycydIP1yU3roa8pcpSzS2wf6WtF92pIT2oo07LK312fWhHFJxGW2-ESUflB3KYRvFlXnxXRMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=LM2Uk91OqkAziGARP_Y_cXslMZXi8UaIDoYINZQHbQUoqJ_sj-BYW5nkLUV7NwEbrW22GxqA8wZCn637b3rUFGo6hmbJtid60p3nSPXrVDx8N-bjMHo0zraCbu0WeZRs_DfNT6zDXZWLBXvUl26u3AkawkHI3ut0bjFsAwrZ3SEZpDbdk7fBNHcmdLQYw1ZnxONsX9A16mU334U9lhGSkkfED9c3SyA2uV4RMFjMY7jl9pe-62xdthsG4dHxV2RWB1MEXT6xk1lUxycydIP1yU3roa8pcpSzS2wf6WtF92pIT2oo07LK312fWhHFJxGW2-ESUflB3KYRvFlXnxXRMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Gg6TrPm6CwDsrTJEd31YeOIgN1l9jrBzmTEfXGO_Jl_02sv7IyYbbnlXxzXzw83ynXSObaiP5kiYY2ENu1S4bVth8IPYFOxfnwPQ_iH4_Nw_EElnjdKC3hrMGIck1bBSRyM0KX30eS9eYWo0PUoSxt_6d86NwqrTfbcftiWStZzlwcGo5r8l4Oczy1EDrUqyryooLdqM7gWHelNliuymOWkSA8oJodbnpT22xLcqE-v54ZldxETv6QTUF3SWAgZd2lRSvXwpYtG0zSOsnZeZ7JMDysk4iqYPO50eUvUTN1JH3bP-rKdZLhaSHCaGy7GfkR6witafdkn2NhPwHRmeIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Gg6TrPm6CwDsrTJEd31YeOIgN1l9jrBzmTEfXGO_Jl_02sv7IyYbbnlXxzXzw83ynXSObaiP5kiYY2ENu1S4bVth8IPYFOxfnwPQ_iH4_Nw_EElnjdKC3hrMGIck1bBSRyM0KX30eS9eYWo0PUoSxt_6d86NwqrTfbcftiWStZzlwcGo5r8l4Oczy1EDrUqyryooLdqM7gWHelNliuymOWkSA8oJodbnpT22xLcqE-v54ZldxETv6QTUF3SWAgZd2lRSvXwpYtG0zSOsnZeZ7JMDysk4iqYPO50eUvUTN1JH3bP-rKdZLhaSHCaGy7GfkR6witafdkn2NhPwHRmeIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X37hXjxP98n_qfHQeKVthu0fok6JU0pO6UAt56f3uM0IgZaheti89Vt0VhLd2OA7vRSaw1GcbF8D7rJQY69ZUWJ3QVtqtzep8GVKOjyTvEyNGk674XoW9ws4q7fEHMNj9BGyibyZixWmFOefgiZbDp4RXtTIOhfgYF5v01KhHhOZ4fDcaDXYn4_QX_wfZjMV2wuoXpeQEjIPHYDnJDoP5BcEOi7gDPuIfYgfVXG4dGRehHYlrIc64bYbEvYkuelRUlBFaZPCCdxEHjo6M2iUdN1k9AiaQacEedfxunIxjX2ftTKLWOBJNsRLndm7d0wbamCUzvC-ESyRfDS1kIlisg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDY0aBiBPL8swQRV8bgmGBheAix3kja69GK2rOCH1v5C7_8RPZ_OFw9GeQTtlXj4bOO5gQJh0Lgak4FRkQu7IWSqt0nIypA4N5L5xSP1Mo4ooSE5gdVvR2ElV9YzPDwe_sZGaD6KrDk8bnpQbkZSXqf5bgMZ-nNWMC8rcuvkBQ4IAHD_AEnVWptEkNuv3rcBq9mMuFc3dvsd0vW-q07NP4uyjPvLug0eCtZb20IQnqjpNiFSgYhpu1byzHtCszOyCl7mcuZx8dBp6mtbDa_T_dZVYQl-iBNQZw9ugUGjrG-QfomxFh7HnVz_sGpw7HeygRRNDkREVIfhJST0Nj75Rg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=NLgCthBlOBbyK51Ca6ZBxvSANCECTpetOo5dUibJ0SkSwPSznBjWdOojx3UzLdKoXoY9DhQQlMv9hZqrWHKwy0UIiWT_O6g4FKolB15zdWang4bw2TkmkuuP0ZpTwtPF5K3hHmkZR2XpCxsv_wPk7Bd4M0mJJt2c5r9Xg_C97Cy6dYPVyrmRBEE15tMnD4qklLVElXYS0ltkDzKcbcgk1D1Bzg0avOrYDRqK30BD-xe6pQ_lDfvhE75XRyIAhEKo978OgA5BiXvePJoaHuUxzZNOZmQjEB9IrLD0G_HK-T0fl5e-a0JK7gBOfFTULkVW1IafC15rs8aZSlFv1aWiDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=NLgCthBlOBbyK51Ca6ZBxvSANCECTpetOo5dUibJ0SkSwPSznBjWdOojx3UzLdKoXoY9DhQQlMv9hZqrWHKwy0UIiWT_O6g4FKolB15zdWang4bw2TkmkuuP0ZpTwtPF5K3hHmkZR2XpCxsv_wPk7Bd4M0mJJt2c5r9Xg_C97Cy6dYPVyrmRBEE15tMnD4qklLVElXYS0ltkDzKcbcgk1D1Bzg0avOrYDRqK30BD-xe6pQ_lDfvhE75XRyIAhEKo978OgA5BiXvePJoaHuUxzZNOZmQjEB9IrLD0G_HK-T0fl5e-a0JK7gBOfFTULkVW1IafC15rs8aZSlFv1aWiDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK9CBvqSZvr09ZjhJ85ZFyK0PloedJKzBfSd5jqVwlhOF4Q5CRKWi-nYoV6qUKX_Aac1g49CxlPHLXWXGSboxr-06F3TrVLvCI4pCeVdXJCtPLWqtvmgKR-Am-btJ3PomqPoy-ybLRvaqpuJLV-JPa_at6_NdtJBB4S2V2w3WOTo3-8SBKqXnJK6GKaqMnovteb2BGz6rixeG1BYHQawBN7ZSBGDvJP-mijiaH3WA9XSIXqIHJ_PviL1wXBI8MiLztfiOLSwgBBctA9CUEKzpzASu1TqRHY2uoyOe6xSDbCCk8gwgkkejhYgTOl1bow8uKfoNwTiyXmWxF7CNxKJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1deKTKOWtrZiQivBj7qoRv8tTFNcMcCr4hk6CA4Yqe-S3tc312LBq31NgQcK-NvqcJT9mgTorA_l3Gtqr8oQl6NZckjKUNTaffhrROA4MsdDtZd3b_AC9OD2X5FfaEGPixlVXz095HrOkgq9RB8ySRaXUZ4gSY14CcgpNdqVz9VTaNhrRUYH6XzqfqxllkZESkc4GTwurMvbz82gj413lA6gmftjVeI1MreqdiPtmDhoyhUqr-Z6m1Jfpx6Q-TQUUnTqZ7FS7BmXl8UQZsHfWS2JU71iWwsIyUgYj0fXRlqcTGHOZR8C7mnieo89h_q9KnaMVopG1rn4HWjeAPMYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEag6RKe3cmosxP5lgnkEw2rIVGyRjRABKx9-JWrEgpDM2LdMomZsbCvA6alZx-p9jh2AUz4xoAduTz6RffTO8VIQepOhbV9oLpxWgzA3q4MPH38L9Y3LafdsJqEmCo9RNydbghi458zD8EEwg5Y-r-HlFOX_Y3V7AGl8Lc78RK3L3GMWKA8RHMO13gaLqvO-V4W3RqL6mJxRWU5gShqVmdFF4wIXUPtYPWOSs8tzG1HL9YtvbLtd0r60zV91VyUWiUiXsxey-D_kHo45wbzoYjtT4p21ct4s2jXiUK7X1osX5IarZlTk1bai9Vij1V5Zb0_LHp_ORUf_uzvoIwF6Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=VO0t_BAtBqdnmZg0x8bYI9tz4_bW9vYwGm4wIeQfW06Lsubqp_Tp9t-o7E3O4TnX-v1W5IJZGQM9lPShwdn08t1l57FijIE3NOYrtgPLKVWXJK7dJ5Y3XFvFzhjXbzBUA-JW0eYJ0t_YoeWoO4Pp4_WXxXv-Jsc4OKOc46qXhlynmQts52vGRr-cI3FboBwdEKYhKPm1zyytJcv7N897352QM3yuGpZyHFtBUn5NOnjEvKaw_pCWVIRN9bmTPp6zzkoyAJ9Lg5YJ-dABYERMcnjtC0_RtoNFhQ6L0NL07WW8N74AVKWnBTY2I0fXbArGKn2Y7hOMqz1_f2L71Qlbdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=VO0t_BAtBqdnmZg0x8bYI9tz4_bW9vYwGm4wIeQfW06Lsubqp_Tp9t-o7E3O4TnX-v1W5IJZGQM9lPShwdn08t1l57FijIE3NOYrtgPLKVWXJK7dJ5Y3XFvFzhjXbzBUA-JW0eYJ0t_YoeWoO4Pp4_WXxXv-Jsc4OKOc46qXhlynmQts52vGRr-cI3FboBwdEKYhKPm1zyytJcv7N897352QM3yuGpZyHFtBUn5NOnjEvKaw_pCWVIRN9bmTPp6zzkoyAJ9Lg5YJ-dABYERMcnjtC0_RtoNFhQ6L0NL07WW8N74AVKWnBTY2I0fXbArGKn2Y7hOMqz1_f2L71Qlbdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=KAEd-es2zTvY5PtT7dPAwtTg3u-e2JnFMsBlFZNoBHdMtJHXldStp3gXPcfan4lwcaS5Fx4HjiIJeAAP03K7pOuaiEO43c4DjwTxsSmE2hR7JJ2-asLaAhG4AhZ2dDuXlW9hwJsUA4o9wqNjrw7HeROnEBHsP5Q65LAQ-U-aWHn2EVaFv-pOpmOOpK6K09mAi9NRLZNAEvZix62H3ns1nbigqCHX-CeY7TN3vrefd-eLYMTm1UkKO3bhGVjzQDXj4Fdd09aNDUZyLlAbvjCq_Wd-kiQmRKNdzlZ1j_PNsMvUzPDQC2T8gIbR7mMbTKuZDkB50K92TBQwhFbrLs9FkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=KAEd-es2zTvY5PtT7dPAwtTg3u-e2JnFMsBlFZNoBHdMtJHXldStp3gXPcfan4lwcaS5Fx4HjiIJeAAP03K7pOuaiEO43c4DjwTxsSmE2hR7JJ2-asLaAhG4AhZ2dDuXlW9hwJsUA4o9wqNjrw7HeROnEBHsP5Q65LAQ-U-aWHn2EVaFv-pOpmOOpK6K09mAi9NRLZNAEvZix62H3ns1nbigqCHX-CeY7TN3vrefd-eLYMTm1UkKO3bhGVjzQDXj4Fdd09aNDUZyLlAbvjCq_Wd-kiQmRKNdzlZ1j_PNsMvUzPDQC2T8gIbR7mMbTKuZDkB50K92TBQwhFbrLs9FkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=FijgZwerQA8ITorQXiJhI1R4PtiZxvYNfJzvV4yfRzBDisijX-O8dJl3-kSk9Sjdyj6x1U_Jqr0cWc_edaDMaNt-JVysifODtat8BSKH26e-Q4yZy4T4lIz8H-5anyYtG2duCVfTJ8Lq3Nei-0I4zRA2BWmjQsMYOuxnJw1pVixBE3LtgruziRimhFsIgCepO12cwSNjH2qg1LHQdZ_m8k4vArWvM6B6oXVfJornu368T3ibxGnTWETOv7qcTZJymFLX3scAFO8FWsvw7e5mDhskB7oOaIT9A_niNoAjyR9AKX8lR-9_bzJsNMp4fVtPJATTMlxAGjA45WjcP5rUm7NlqmCrsu9CwI6iBSnkjuY6Vc-CmUs6RjWMY-6ZxJXLQ97wI_hDbN55vk8_lDRuB2bk_XLgMz6LzDOApQQiD9Nw2c3IX5A6kFdvkMxz8TfOI7DISpbV7VjgOPlLldBXOhsN4uaA7pVPdqTT4kw0PaNlwoYXR5YBMdc7hSgsKRTtVxn_L5gRJm6qso5ogUpt4PwXif4qTO3SEDolGrwi1td3TXdup588944lB_apVF5ieC6D2H-0Ovm2wtaaj8WyQ2Q3qAhlM954PA-0J3u5JVYoyYhV1ope_K-3pzToXSOXj3r-zFwGtysIyvEn_r35LaN5WGwy6Sz1U8Dvkl3v3ao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=FijgZwerQA8ITorQXiJhI1R4PtiZxvYNfJzvV4yfRzBDisijX-O8dJl3-kSk9Sjdyj6x1U_Jqr0cWc_edaDMaNt-JVysifODtat8BSKH26e-Q4yZy4T4lIz8H-5anyYtG2duCVfTJ8Lq3Nei-0I4zRA2BWmjQsMYOuxnJw1pVixBE3LtgruziRimhFsIgCepO12cwSNjH2qg1LHQdZ_m8k4vArWvM6B6oXVfJornu368T3ibxGnTWETOv7qcTZJymFLX3scAFO8FWsvw7e5mDhskB7oOaIT9A_niNoAjyR9AKX8lR-9_bzJsNMp4fVtPJATTMlxAGjA45WjcP5rUm7NlqmCrsu9CwI6iBSnkjuY6Vc-CmUs6RjWMY-6ZxJXLQ97wI_hDbN55vk8_lDRuB2bk_XLgMz6LzDOApQQiD9Nw2c3IX5A6kFdvkMxz8TfOI7DISpbV7VjgOPlLldBXOhsN4uaA7pVPdqTT4kw0PaNlwoYXR5YBMdc7hSgsKRTtVxn_L5gRJm6qso5ogUpt4PwXif4qTO3SEDolGrwi1td3TXdup588944lB_apVF5ieC6D2H-0Ovm2wtaaj8WyQ2Q3qAhlM954PA-0J3u5JVYoyYhV1ope_K-3pzToXSOXj3r-zFwGtysIyvEn_r35LaN5WGwy6Sz1U8Dvkl3v3ao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=KjBbja3fuTJXPTF75KTx5Bz9Y0YLLVO5O0Z0SMIgxZTxbwREXlKmAiqzejMIzrmi0fQdl9IARHiDpftz8KncANnm_8G1Mr1PfclZj3lm83gNg9Hp_D-C0vG979ACeOOz2mmKSLSYadFm5QvaLYiHyGOxpnIVV1_ow3xULc6R8i3LKc_ydE3Te0nNq-NJcGzHb2WmrVsMfxn5_UdJO8zqs7CfJ3o5006r7rX4u07bbBKoAWwMsWsXky7dsa9KNgdIheoXK2q7ZKRoLhO3U4WJrNLjo7CInda-4V60CxQ0kRODrse3d8-b8IWh2K4yneteEdtxxvFChUh2ofcKQe9YghCpeEJzJf8vlFfu1lWf7wlR5oufY7DhQVPJVrbUgpLDwv8z71BA9UyfIFX6y8CEPPxQBqbjB2DrMhanD3yM7prsNf_qr2Bw5n6XU96o0LYzjWT6Xumr1wZdFytkHesSZcgTYLyY2e6fasOBhbqXZrPZRHwwuqfVsKCcj-FBGhUyJQ-h__uT8BfJ_WUwxBVozCVN1RQvWxpb4FmEFyGJjzaqQ-5GdgLECTempH9Ai6cjcWc6_qAf1n8wCSjPOuqWgOLdYQU1yO9VFUdzEd_543dJy92aHQ3wmG1G_AhvzgjL61M0_-n8zWB3qGRyVdOAbZTYaMUYvWpT-yaE-sl5iXs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=KjBbja3fuTJXPTF75KTx5Bz9Y0YLLVO5O0Z0SMIgxZTxbwREXlKmAiqzejMIzrmi0fQdl9IARHiDpftz8KncANnm_8G1Mr1PfclZj3lm83gNg9Hp_D-C0vG979ACeOOz2mmKSLSYadFm5QvaLYiHyGOxpnIVV1_ow3xULc6R8i3LKc_ydE3Te0nNq-NJcGzHb2WmrVsMfxn5_UdJO8zqs7CfJ3o5006r7rX4u07bbBKoAWwMsWsXky7dsa9KNgdIheoXK2q7ZKRoLhO3U4WJrNLjo7CInda-4V60CxQ0kRODrse3d8-b8IWh2K4yneteEdtxxvFChUh2ofcKQe9YghCpeEJzJf8vlFfu1lWf7wlR5oufY7DhQVPJVrbUgpLDwv8z71BA9UyfIFX6y8CEPPxQBqbjB2DrMhanD3yM7prsNf_qr2Bw5n6XU96o0LYzjWT6Xumr1wZdFytkHesSZcgTYLyY2e6fasOBhbqXZrPZRHwwuqfVsKCcj-FBGhUyJQ-h__uT8BfJ_WUwxBVozCVN1RQvWxpb4FmEFyGJjzaqQ-5GdgLECTempH9Ai6cjcWc6_qAf1n8wCSjPOuqWgOLdYQU1yO9VFUdzEd_543dJy92aHQ3wmG1G_AhvzgjL61M0_-n8zWB3qGRyVdOAbZTYaMUYvWpT-yaE-sl5iXs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=ruXwy1dvB_J1wfnAgE8jkJlv5Txp68X2WEmI-no4QaU0pTyU1v9z8JOr5BXR9YjCzqmO1IIprjjyyw71DwKlnFw-ILJI53iwUPn-g0iC3FIWtA1J7zRIp6Gey2c3ZRbHNlrEINnHS2sVmr7HteQldcb3hAO8K_6FWWAZPifPq179cX87F72xWqH6U5lu3akScWFShw4RQPhzggbsrqzbKTM3Sy84pSiIroIXuhGxU0RtTJ7nK_BvAilUFLA5Wa-tMVaalT3c68WT9xS8ew5jNrxapQxXdUGEa0WTIP05qpBAVsXifab03bifd_bBKFPwI2SEhhPWEjZETB0U-wonug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=ruXwy1dvB_J1wfnAgE8jkJlv5Txp68X2WEmI-no4QaU0pTyU1v9z8JOr5BXR9YjCzqmO1IIprjjyyw71DwKlnFw-ILJI53iwUPn-g0iC3FIWtA1J7zRIp6Gey2c3ZRbHNlrEINnHS2sVmr7HteQldcb3hAO8K_6FWWAZPifPq179cX87F72xWqH6U5lu3akScWFShw4RQPhzggbsrqzbKTM3Sy84pSiIroIXuhGxU0RtTJ7nK_BvAilUFLA5Wa-tMVaalT3c68WT9xS8ew5jNrxapQxXdUGEa0WTIP05qpBAVsXifab03bifd_bBKFPwI2SEhhPWEjZETB0U-wonug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
