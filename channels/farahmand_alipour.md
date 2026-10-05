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
<img src="https://cdn4.telesco.pe/file/i_HFUeZeBCAjlNfZJ7u3LxR2ISndbFuY1VWXnCBoY94Ce2ntk7p1pDgj9xRmWMVGgb30ir64UFo2cmNf930A0_NuY8jmq-V1s8wvbCXxyi7_r9g5EHW7tffICPA7-lKtU3KT-B2b4WXz3gLFGTXK8cBBqCuwBVRuFRrEWuwjLtF_uT5iBeIzr7p5K4oYOgHZCib-RkTR1uoR_WMqXjoD9jckJOd8ldXVRajTefC-X2L5Y6omDzXQaHXWt417ZIq1lNQEpFB_td1oE5Z4E1nUV_BaK8YmiF_NxeP-_BYXexC5GfKU6YJkzYkxBf1mO_vTD5j9A_KuXuv9_kgtLwCskQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCUhNZ0ZYu3TyNvx1amHtHS-zehStrWkQQGDsZCZLVDki8Z9x-IMV3HRd6jPXKs6d703-lBNemxPUas1p0V830oXz6_fLpVwHsESMUIyg1fglsQCr6lGBvsYkaM-Bvdn1WnJdF-xQF3tr0RKc3bkQYEsnSw9alOXbq3MNAdmPASloNkLRlDwGsaDF0TPsJ3QYe9OIIwxs6A4Xv8CO47wZ5lQaOb_R4x5tY1izNxzYqZW1i_d6oL2PJclUUq5Ag4rGxdQPh_8XTEPsCX54l5Kf81gWMZMBtCHLOInnmrg8ZYLgEsyrdmR0FzE0c-DJmB0FaLxv6A7_55t073CFFiD_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hh0PzQLFm1UmpQhJyaAcTDplHAXLgHdi8hc6qnSyoFI7TeL78XmSBZg-j1KiqHLeUFvB3DAOwbKTTqTxmtqRjw2DPSlbneZkGAyIc7Qlhs9TEEZY5FUfVvViV-2TzQ8s-P-4AyzWtViZk3friXEHur0nfSAy2qIDGUxFVTA2gIU_NvD3dzqV5-QzH2LYptRFG8vI8_u-onZuv-xrwO3XDuvnoaZsqyyZ_LG05ut5zSXRteXlRuuNZL4BwW9oL8DZo1_ZJzRxqTtTyVR9Pb6Y_sz6OemN-VtfdUZ3QmssktQxCSMkAzo4PhktgoK27rJVHMKl7qa6ZjubGhC7zcjQhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RO_rduz-aPg-Zx07tk-yq0RSgO6evr2MtAhxblAHxy3knPEjnBgZxVGhsVCCrnXoOjWEnOpBr9BksSaYp4KlEJJOSzthEyoCuZFXdEhJdgbqxRdxPRfiMn57hEV90O7zjXEhn54YYEdfomHqwjnT1dtMqu_F-lI3xZodT7PfX53uE0-jhJHPpJVJYnM1oQGDMdQV7muLYHQqeJwskwPCg39R9HYZchOeESTxbuYiY9eHIazZljk9qbinfcjM6EhfFTSwFygNkvkjfOmjEQLfRzSJ10olgLBKGUVFiQ-2J6i8QqcUGdQiluqpWm3EG_bW-gxy7PTpSf3kktIlkCT39g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=ExTR1A5ZvXwcp0zzbe1H5TBpl8WdvtfkATBheBc-8Vvx4s9f9ONP2N9X07ZwdOTMPVJ26r20vG1YXJ3VbkIdw5JpavvdpFunjnWpy0hgvkhRNFA4yatPY-Tm0NeVwHIm8Qx4XoYpT-q3UrLkS5eUkeIOmjgh4R0tDgc7zhUjGGUFrFtNj2UN_h-uIFt02svnk0QMlYR8sTyE40SKPKWbuH5rbfWiRNPr64U422tLLLejrHM7hYEjGIsinAMbSBMswXciWF7xqM_d4AuhfdbpiXRqWwIa2ZUTqVaK00_3kHJuCSUWx3if7HYgJCxwT5pQrPugAGvi9i9ts_nOnkBuOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=ExTR1A5ZvXwcp0zzbe1H5TBpl8WdvtfkATBheBc-8Vvx4s9f9ONP2N9X07ZwdOTMPVJ26r20vG1YXJ3VbkIdw5JpavvdpFunjnWpy0hgvkhRNFA4yatPY-Tm0NeVwHIm8Qx4XoYpT-q3UrLkS5eUkeIOmjgh4R0tDgc7zhUjGGUFrFtNj2UN_h-uIFt02svnk0QMlYR8sTyE40SKPKWbuH5rbfWiRNPr64U422tLLLejrHM7hYEjGIsinAMbSBMswXciWF7xqM_d4AuhfdbpiXRqWwIa2ZUTqVaK00_3kHJuCSUWx3if7HYgJCxwT5pQrPugAGvi9i9ts_nOnkBuOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=Y0kdrF6ZqIhpqBOsHHqv_CWMsxDikbzQk8KjTbVHNE2mB6GgJi62IsfXBsQND0JB-RGKMrHEJEOdRzz3jBtQewtdtuCO94jzZ16eMaxjW5KC5M_HEyTdzZxhctqGa4PwD3N7zjUvHwMXXqWe6DHYyE9mdC3Oo5IsYAaLxmMKwV3bwCtRG1dAT7XGtR2eOPUIuMpDgYtq4EpmvHxbhIT9pxZiJjdGP3Z2dMYWDM6On4umBgZ_w_TWFBDuGSa5GmkzFmR90OFxveoTHvM0xI5OoTvE_iPQ8Al-BENBuyE_r5h64IA-lV4ExY_x8jT6rnKsKGXNNSYOJDb0Fj9KarQXxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=Y0kdrF6ZqIhpqBOsHHqv_CWMsxDikbzQk8KjTbVHNE2mB6GgJi62IsfXBsQND0JB-RGKMrHEJEOdRzz3jBtQewtdtuCO94jzZ16eMaxjW5KC5M_HEyTdzZxhctqGa4PwD3N7zjUvHwMXXqWe6DHYyE9mdC3Oo5IsYAaLxmMKwV3bwCtRG1dAT7XGtR2eOPUIuMpDgYtq4EpmvHxbhIT9pxZiJjdGP3Z2dMYWDM6On4umBgZ_w_TWFBDuGSa5GmkzFmR90OFxveoTHvM0xI5OoTvE_iPQ8Al-BENBuyE_r5h64IA-lV4ExY_x8jT6rnKsKGXNNSYOJDb0Fj9KarQXxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAb8k1vT3Fdz1H2Aqt6FNLTXGZ4HAX3Ka0t4yQvWiO1QhWxn7DLa-19WbQcg0m3Uq-BtR65DBMHidaSwoYNb2gQzcPiz18AwHob2zPu_H8w8_2onJbWaHcYI5oKFENusl38GTBOP4qxw3Kg7zUBXdXZjZ43qwXSuuC5bxH_SQVM6p4ffGikEFJ3RlY3PzD2AVf-qCVT_KIONJeiPdNeKHCN5cvwhVcQRdvKOi4S33Pmo24GfCKk3Y4GlmqKbkNvrBKU9-nr53qYfm8D7ofWWYY5gk60yLYiSMNa2d15FQI28mv6L17I90G5j4VZ_wGMhXC8yW42VkH3BrtSoOBWUIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=lViFTNiViojzh6InsOeMy9007ufP30eGWFuJC5FVKGsGZRrqcVGyds1McG9zFECdRaoHzh6AUqRZZJGSK23QoKurUBZhosyCJ1bYL8oTgYA8cnBrLjvtEiv5uJ5qTVkYORWOuH9bL2kQMhhcSLd2uQ1gaQYZTFvv4k7TlXAdDlsWmdlhXrDLIL2Ld3t-JEvBG4TnB7O1jAcr00LV45SUGdMuBAC1gLsInlc_R7x89dFRPmK1EAWh_HUpyAd55J6_S7mKJhx1vFoCUWdWvIk7IGKBganC8W4sKbCpsnBFikh80I-c3cwQaLwWL7JQ4eDxPYpo27EreWgoinEqmx__bHEIIBsBlYpscj3zrxc8YCZo7MVC_WbtejDRxyeq9SpFI5Tz3XH0KzxCt_8ikOJtUiKCYDVitl-5SnXFY2pgYdeUO0ZKzc0YkVA8MwhnQJdLDs9sskVXmG6aGf94y65f-wFtVidmQQNPPuka6drdorkonichsl95K3pDwZxdkIrGgi735qeg9a-W8KOqVuohLDXLxl6-3ta7KyT3vc77Pbpmzb6XwNsi7rUiWXE11XVAlZX_JwATXMn8fBa4DlvRVFk9BQr7__aVqwoD7ynFh88kr8raETJbKJUTrb5XRmVNbZupG0oaHaY7JgpoukzK5VWQAwiIODNqpLDzKff6GXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=lViFTNiViojzh6InsOeMy9007ufP30eGWFuJC5FVKGsGZRrqcVGyds1McG9zFECdRaoHzh6AUqRZZJGSK23QoKurUBZhosyCJ1bYL8oTgYA8cnBrLjvtEiv5uJ5qTVkYORWOuH9bL2kQMhhcSLd2uQ1gaQYZTFvv4k7TlXAdDlsWmdlhXrDLIL2Ld3t-JEvBG4TnB7O1jAcr00LV45SUGdMuBAC1gLsInlc_R7x89dFRPmK1EAWh_HUpyAd55J6_S7mKJhx1vFoCUWdWvIk7IGKBganC8W4sKbCpsnBFikh80I-c3cwQaLwWL7JQ4eDxPYpo27EreWgoinEqmx__bHEIIBsBlYpscj3zrxc8YCZo7MVC_WbtejDRxyeq9SpFI5Tz3XH0KzxCt_8ikOJtUiKCYDVitl-5SnXFY2pgYdeUO0ZKzc0YkVA8MwhnQJdLDs9sskVXmG6aGf94y65f-wFtVidmQQNPPuka6drdorkonichsl95K3pDwZxdkIrGgi735qeg9a-W8KOqVuohLDXLxl6-3ta7KyT3vc77Pbpmzb6XwNsi7rUiWXE11XVAlZX_JwATXMn8fBa4DlvRVFk9BQr7__aVqwoD7ynFh88kr8raETJbKJUTrb5XRmVNbZupG0oaHaY7JgpoukzK5VWQAwiIODNqpLDzKff6GXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Jw3-sD-fkdmg2UKAyPFxy5efHp-SjlCBwqxTY1BPJ0EXgyBMQlPDALdqLZOVPQFJUGUo87UOwl8ql1__upS7PrN5n69WxlQYPkF8_1lN49qk0Uhlfw04ic8_VrrhE3rGRhfYB9sKWwsjcLgt2qiRi5uZGzjfAgKLz9e-RVEZe_3Gti5uHnmn50p7SDfMtWnMH37OhtyPtaAgsEUOE3GqZluRyKrKts6b0FNw-Yyh-bCxe4kt92YXwYRDUdUTrMk7Z0YVOgrb-JdjUfzlC_3zESvfUShvbW3oiSj93S9UVX9IhI3KZ26K3dPM--zwKJdPk0ltwJjYBq246rlXUt2hoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Jw3-sD-fkdmg2UKAyPFxy5efHp-SjlCBwqxTY1BPJ0EXgyBMQlPDALdqLZOVPQFJUGUo87UOwl8ql1__upS7PrN5n69WxlQYPkF8_1lN49qk0Uhlfw04ic8_VrrhE3rGRhfYB9sKWwsjcLgt2qiRi5uZGzjfAgKLz9e-RVEZe_3Gti5uHnmn50p7SDfMtWnMH37OhtyPtaAgsEUOE3GqZluRyKrKts6b0FNw-Yyh-bCxe4kt92YXwYRDUdUTrMk7Z0YVOgrb-JdjUfzlC_3zESvfUShvbW3oiSj93S9UVX9IhI3KZ26K3dPM--zwKJdPk0ltwJjYBq246rlXUt2hoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evED0HRJI74dhxMMP8CSdpcQteZBounD0NgWt_TDibJtzmezLqGGm3lr2i6wROu-MQG38ZuW8PgGb5fRqhGZGCRlDuCUGCY2OHunV95gn9tWHdDpVXyHG_vsbdPMKo50j20UY1epq38_UBCDXiYeWRhab4x21infAqaG3FYglxblGG99aRwaPtkDZy5tW6vNn_opnD1aZ6rpzVZKW-NH3p1FK57A80ugD5doEs_AEI6iP5l6fNijZWe9ntpKaSQUXi9AKjeslXBcu9HMxQPivS_yQGdc-PVYF11OWTX_cElOyxPgFpxzGcfeyJCd7LgHaKSDlDSVL6HRS4ceB_657Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=qQ4LxX33qjT-ZQwXu40X3l3UAXJCzfTQX8b7BUZ5NYJPJP-TgVTp5C2D-qbhDAg9fe17LknX52VjT6oBqBSGQk5qw9sMC_BeeQMVqNC0ziQVoQJH8luW59H6rAYf4NtCnVrDuDGzH3jmCtTN1CzebbhAMZNwqTldg1EWLmvZeAB5h09CyO5xpavq3GHwqGyP1ONolQVMbBzF1y6t8nEkb_kiZB5NAqYqXIpXsIghe8qDdA2sBEo4x72IOsYldpjZph6lwnH4hlTVJ4bjtkyNbCIaMC73KQK2Teg3NIAS8gc3wLIkXzzo2hzH17ej8M_7bWTjDQUeXb4-WayDfDI88Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=qQ4LxX33qjT-ZQwXu40X3l3UAXJCzfTQX8b7BUZ5NYJPJP-TgVTp5C2D-qbhDAg9fe17LknX52VjT6oBqBSGQk5qw9sMC_BeeQMVqNC0ziQVoQJH8luW59H6rAYf4NtCnVrDuDGzH3jmCtTN1CzebbhAMZNwqTldg1EWLmvZeAB5h09CyO5xpavq3GHwqGyP1ONolQVMbBzF1y6t8nEkb_kiZB5NAqYqXIpXsIghe8qDdA2sBEo4x72IOsYldpjZph6lwnH4hlTVJ4bjtkyNbCIaMC73KQK2Teg3NIAS8gc3wLIkXzzo2hzH17ej8M_7bWTjDQUeXb4-WayDfDI88Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B59wONAQ9gqWjzRR4CKgfot9QAmcHA6Jqiy4fLfagihuB4ixIpfFAFR1SSaQG0H-c5Or6cjwNzN-2csHVDIqH9Mz_LAbLOCB3qyzHDPbGY_dAWxEotVioDkgcss_V8M-Q7eiZp7l2_O-iDLx9oIQDGebGhSN16b8jgyS7ctKef25D-2lCdHBkptSAAORbAIHXn7MZIINC-eYTbWfzCdZ-Zz8_aNtCGyQeCv1bW-1IJoEU8RmxvJbJ12BI6ZO2MyzNJmo913DuzMwT0wbulbWWJp-wAUFrS5PjDej1fInlEmYnUR56HH7_jGycUdz7DzUaf78iHrzQJs0vVXdbYr_mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lY-LiGdPYtB04lbkpeIKyBEXymGbNSUcKDBQzSTGaq71XM5y3JYjf5r7eZPS2Eucx4hf4MwUVT_Yg4KAWaurivSv8shhNJIBQRhR1uGHtoBMiAoMBXWMe6W1dRcJH7WLQmR2tX0khZVOWQwwwmf2Rdscyo01qurgVyvf3mBSltBLFWJPJNhQpfmI5HjqNvdZ0KXgPdZ7J4r55WmyHRp43TKelc_1Ie7bidDrudX3sc3bdRfb6adKIS9kxg5ZmBs_ujAtbxT22Bw2PULsi5JLtR3_awcWBRM748SWAC7758X_-k50HrXBpm8AqVBQ0yreiu-vePMYMgEMf8vaOIuvxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=FLdyCNvv1YBKp93rKErYNSuJN94IBm-FUYXDPokYbwWGzytawCRRgCsAtNwbGKu3x-atX2dAxKDlAmfdA1R1esClpFne0jxxr_S0ATkRNFIfYDjklUDEBdl2PudYTWhx7eQwq7OurOfmLspKsSCmqfDqpSGZrW44EtWBiRCnPgzfWfDEB1ptq9R71M3i82SR5YDxtbMVTVFoCSmN8vD4VsSo799ONv3ufCco-7fTNIXJB4Qixiiph3VIihfT-7X_3Aw96KuI4m2ebJIP5BG6pzRYbTqbxHMUuGxetol2N0x97KasixEHYlX4lW1TiAjnkgux6FVxKxfRat9xWxn8wBDgJPjk9R79dBWvjMZQhLqxnZVo8LmheGS9_N9oG4bpEN_yBR4WCmMqyzF5twSa6ae7yaj33uXlblQMkG4brOmgCHQeCWa94rATtNqwuPWCgFdbkz_vAbWlQvnF4tioXP_ePT2hhpS3XFgdUqTQK_PaEw51BdQA8ZJPgxMZMPNWIRLe_XjtOcl2GuJUlMD7SLYE3s-TT4Ex1oemijf3pMtA9bEL0epaYMSSE5F2IfEm_6PljVWBvDcJf01gxAup6xMbI8PXT77JaT1bHKXuzS-d-IOPRgmDYIjQyM-KXhMAjKP8F-PPihbWSJZB1ogE_YB5QwswzIWdicdzW0r43gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=FLdyCNvv1YBKp93rKErYNSuJN94IBm-FUYXDPokYbwWGzytawCRRgCsAtNwbGKu3x-atX2dAxKDlAmfdA1R1esClpFne0jxxr_S0ATkRNFIfYDjklUDEBdl2PudYTWhx7eQwq7OurOfmLspKsSCmqfDqpSGZrW44EtWBiRCnPgzfWfDEB1ptq9R71M3i82SR5YDxtbMVTVFoCSmN8vD4VsSo799ONv3ufCco-7fTNIXJB4Qixiiph3VIihfT-7X_3Aw96KuI4m2ebJIP5BG6pzRYbTqbxHMUuGxetol2N0x97KasixEHYlX4lW1TiAjnkgux6FVxKxfRat9xWxn8wBDgJPjk9R79dBWvjMZQhLqxnZVo8LmheGS9_N9oG4bpEN_yBR4WCmMqyzF5twSa6ae7yaj33uXlblQMkG4brOmgCHQeCWa94rATtNqwuPWCgFdbkz_vAbWlQvnF4tioXP_ePT2hhpS3XFgdUqTQK_PaEw51BdQA8ZJPgxMZMPNWIRLe_XjtOcl2GuJUlMD7SLYE3s-TT4Ex1oemijf3pMtA9bEL0epaYMSSE5F2IfEm_6PljVWBvDcJf01gxAup6xMbI8PXT77JaT1bHKXuzS-d-IOPRgmDYIjQyM-KXhMAjKP8F-PPihbWSJZB1ogE_YB5QwswzIWdicdzW0r43gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K97YvDdK7by9uOli3emQ3OK1hv8zgXvsW67rNIbNPn58fqt6UEZFSDKVm0E2qiRSneGE_B1taYP-Bs0i0HpwDLc-kLUm0OhCYomyutvsrNzUs7x9so1onofOZSd1FESPQvgJ--mN_pZTe_doJvazdwiqVC2MYodzkJ2ohhbSkWkSaNShL1BmjBFHU2VSZTLX5Js_HFVLjRb3QNvMta9wZDOY6hsc9IkiCkPDGZ_Sat5X7ZBMCN7_qYFtTJx17qTqV5jwPHqZS_Z28-xV-BEKEAJk_ySyqg9XmAt7YoX0yVtaezQNK8des-IiN9gkCYai1Er-H2dfPifliTK4mL3UEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CV7smx_8g9CAbf7QO2pB4_jkVMCmo2DFslixP0WzfCvS0bCEI24a1bj5i_0cZh7-EOxRMS34jbppmYFUAf1FYcDDtJ9xsgHGhyafINGJnsbAhK3E9V7KXVr2G-0xwR746VNoB9Lfl_86GDKBJcvyMuOgQ3YBvtVKkQxh7cZkuEnjv4x7dmbvlD-8tvLpqfXfuEugGilYlVEzEt9pfXBcaOk3egXZjaQz1TNFI2_OAZmOBigWACO_YAJJYH6_asEcvuDH7czwhdhPyOJJIMQx4nsCgXDkpBVQDgWe9pVQ7kTF9E4qIqepaLaKzW9HUxRvkiS51sdGeJ9Xu7nINZP_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=K5mnYXxQo0zl--_0uT6ZWFt_hnINhHdqYUX3rc6ZIPkf0H8NqXoCH-cth--ShcB2N_dl_Akij2-mApyvE8B7-ZnCW8OcmYeSTHqGYoM69S1tpj8YjXv263rovpxPs4y3-CJI_TBk77NB9TptpW2ZV9Wjie3ArKI21URpey0P9LqGL3GaZIKvFhgHp3CPRJN7O_u4oht_uyAFaXq0RDxoqn5AXDYvvfNalX2Gpipo2DzR_KB6thnE7hSWLbwf6Qj9ctJqaHr63XOnozbhRcdJWs3HLD-Y9ZDJlUlhhkBulVIDeLyhKrtd0hbeTUGxzE4CpSFCRIyE3nieAk5hGtDsuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=K5mnYXxQo0zl--_0uT6ZWFt_hnINhHdqYUX3rc6ZIPkf0H8NqXoCH-cth--ShcB2N_dl_Akij2-mApyvE8B7-ZnCW8OcmYeSTHqGYoM69S1tpj8YjXv263rovpxPs4y3-CJI_TBk77NB9TptpW2ZV9Wjie3ArKI21URpey0P9LqGL3GaZIKvFhgHp3CPRJN7O_u4oht_uyAFaXq0RDxoqn5AXDYvvfNalX2Gpipo2DzR_KB6thnE7hSWLbwf6Qj9ctJqaHr63XOnozbhRcdJWs3HLD-Y9ZDJlUlhhkBulVIDeLyhKrtd0hbeTUGxzE4CpSFCRIyE3nieAk5hGtDsuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=AA8oqbPOwkxXVD6UTAm-8k_jxpAFCv-mMmAGyUIDoeHzgm163G2FMjau4R5SWPZQJ_RQuYoPW7xr6Joqdh6DJIdDJyAI_3tegn-1n6pXGhSR0Jsn7e5ryECkA9ZwO1u1FpooHQ2yKxi9Oga-C85W93tJWIyRcDCFOisqGamB5JzLquBRT8mM3M1GlUF0WWf4T8Yq1-NeR_wFYI2lqyocr_P13h1hlBmfudH0uQs_txMjhPeCHEHzqN9b7402Da0L1o99RVQUIuEBcyPx0tT5RlTmXfSZBHV9UefTCjZ0fj-eokddrsiM-SO9lQkMlPU9RLcTUk7Aii5MQJRfNBaY0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=AA8oqbPOwkxXVD6UTAm-8k_jxpAFCv-mMmAGyUIDoeHzgm163G2FMjau4R5SWPZQJ_RQuYoPW7xr6Joqdh6DJIdDJyAI_3tegn-1n6pXGhSR0Jsn7e5ryECkA9ZwO1u1FpooHQ2yKxi9Oga-C85W93tJWIyRcDCFOisqGamB5JzLquBRT8mM3M1GlUF0WWf4T8Yq1-NeR_wFYI2lqyocr_P13h1hlBmfudH0uQs_txMjhPeCHEHzqN9b7402Da0L1o99RVQUIuEBcyPx0tT5RlTmXfSZBHV9UefTCjZ0fj-eokddrsiM-SO9lQkMlPU9RLcTUk7Aii5MQJRfNBaY0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=SQSIejn61qNboqOYZZaTX6jTGRufmOH1V9hZij5eUCa1Vhi-bUiWMIfCwEUVrkBIpEcFDWzNZjA1HHK-UioKzX42RWW4konkDqcW2RdovnpG_ZAZcKrbH_Wo4ABOx4lcD7goZI9ZQbFgdyCQ3KeDTiwFE8EYKb4TdYFwBut8NBP8XZMlc4UeKIj-ZEknFK3P_6SejQjhnH1HKg7i6WPImihd39jG9-hM2E3ewmgDTcQ-zyFUUxrO-dcFVhHhhOrbGhXK8EC4LSQtevdrFfHFEohXZMutYkmBlsI6df2ou9ri2ryitLr6ZOfCoir5zjS0wGLGb-icIq1phZf3vU3xSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=SQSIejn61qNboqOYZZaTX6jTGRufmOH1V9hZij5eUCa1Vhi-bUiWMIfCwEUVrkBIpEcFDWzNZjA1HHK-UioKzX42RWW4konkDqcW2RdovnpG_ZAZcKrbH_Wo4ABOx4lcD7goZI9ZQbFgdyCQ3KeDTiwFE8EYKb4TdYFwBut8NBP8XZMlc4UeKIj-ZEknFK3P_6SejQjhnH1HKg7i6WPImihd39jG9-hM2E3ewmgDTcQ-zyFUUxrO-dcFVhHhhOrbGhXK8EC4LSQtevdrFfHFEohXZMutYkmBlsI6df2ou9ri2ryitLr6ZOfCoir5zjS0wGLGb-icIq1phZf3vU3xSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQIbCTSDnyqCTHlgZOSfbMRCO4kzOL3N2J1Z33otXDUkkpTFQCOzKsbKTdZDtEoAWCPAGUPjnXCNeYg83Do-mzKzKgJo_wlvM0KJrAogzDE1Q82Cilw1G-7XogYauz0cMH02b8Ris2HLNDX3ysNd53AzLT1guQhlMRm5kFNF1DTjxMRZ8XhzFXmgNhOvctC1d1A64fs_BztEljFQrtOleqUtxj-ITyah3-DXWn0EGtXalRm_X-algd4iTzNIXIhFzq_EvRrOmE1hhyUSijhjbP7-V2tcKn6IHdvEOHwaMoUYykbpZ65Dgurwcwi0PplV-rFGAmPtDm_Z7EiNDotq4A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DgcNdBz2VAoB-N-c1ZtnXJ7yaxB13qPaIUNkTimNLiG0qzg23Xb3hvyGtyMhYrONUNrer_a4Cg3_ph2z1tSTay73HAmlm6yP_z4zPjSqoEc_EEuaRGdhopURJQ8b0zUDOfwyXBea6mwI-u4XXAMtbd9tiDHv8dr1Hzl40915ZioyH5iZVQlvBU_072ydurwlOLUtErJNoU-a3SIvsgqT3cKpFQ7l-WjKBQYf3EvdHgkkH8ZlYcXl0tm_AVTvyJHq3-Vme0YGSsY9KUJavD3Ul_BRWgcUAMoJjpyjKbPx_iW9Oit79gtcNdS2KJ3iSJXxmq7It3HgwPeK7XAfyP_pH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DgcNdBz2VAoB-N-c1ZtnXJ7yaxB13qPaIUNkTimNLiG0qzg23Xb3hvyGtyMhYrONUNrer_a4Cg3_ph2z1tSTay73HAmlm6yP_z4zPjSqoEc_EEuaRGdhopURJQ8b0zUDOfwyXBea6mwI-u4XXAMtbd9tiDHv8dr1Hzl40915ZioyH5iZVQlvBU_072ydurwlOLUtErJNoU-a3SIvsgqT3cKpFQ7l-WjKBQYf3EvdHgkkH8ZlYcXl0tm_AVTvyJHq3-Vme0YGSsY9KUJavD3Ul_BRWgcUAMoJjpyjKbPx_iW9Oit79gtcNdS2KJ3iSJXxmq7It3HgwPeK7XAfyP_pH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=rrPFzPbuU6opN81C90rsWbLrSdzGTf4meZWZ-e-oXIdklODk9B43JttgwVocPnlRITzqo8gMj2WAZ8ANu5xzlcRIf2Yq9zPToa-IvFME3Jq42eePav4Ytsq4FdPJMJ8B30lQzaNoHF1hovuREfttAHCJM_GxuSLoKqnwcqJCTOQPnrtey8oAKXNbUSMN-ysUDPQ5YmXriW2N0MvjUoVlJ0VSa5XVoSVR_6xq58D9S8Yy3bb7I6l3QIhX7kUSQ2WydSrN_awMr8f6XxrBSbj5yctoDldnBliPDTlleW4rYM4VPJRQb9gd0pP45OtotjAgk08xvEZYR5Adwso-lWwLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=rrPFzPbuU6opN81C90rsWbLrSdzGTf4meZWZ-e-oXIdklODk9B43JttgwVocPnlRITzqo8gMj2WAZ8ANu5xzlcRIf2Yq9zPToa-IvFME3Jq42eePav4Ytsq4FdPJMJ8B30lQzaNoHF1hovuREfttAHCJM_GxuSLoKqnwcqJCTOQPnrtey8oAKXNbUSMN-ysUDPQ5YmXriW2N0MvjUoVlJ0VSa5XVoSVR_6xq58D9S8Yy3bb7I6l3QIhX7kUSQ2WydSrN_awMr8f6XxrBSbj5yctoDldnBliPDTlleW4rYM4VPJRQb9gd0pP45OtotjAgk08xvEZYR5Adwso-lWwLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DulhNjwOdAEuel0Wsq4LPbS7seCxWB1BALXdd3DmIcTzKoVW1-mdPesoLEDqThIAqlonJuQCEFxVSdZXZoGUWmIjjE07aYBhiOWWxWjs-P7Wwt9jzzoPZuRnb-b0ki5pI2FxFfqnXSzHq-aItJeuNPb9NiL85lmAL-6cXGwPutmYIw9yHXGxF9_68PwH-KwHXHvmZioaTwaojUzXhZuox9rKL5iq2DHwsK3VxhJ4HBh-avg3GSJnH34iC1dj15UkAbDxJaxcC9aFwDtBmjprfyjN0r9o7dReg8pykL6ESihs48J-NblsQEcdueD0ro-tDIoyE7PDAhB3ZbdlCfsUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=aNE9UO_xZfnJu7J2qvJqcs22RzYO05eWfU20aTQwbQRGrBjtbkGXJOsD1oUe17F2Bl68B4B64jbb0wbHhKOeNVXC67f0NSrm2t4WSowJMNxVPJapltUo1JoTOWnd6iL1zeVtVApBhpd-PYTMG2ydcIovp6wx4-LJgxYe-TacsXYDifP0eRxLLQ2jkGrdxmRo5XCqQidJA2UDeDDK7_2t-siWKZuXckJVtYH9jebRrK1sxX3l3xq3wZTQZqQ1o-q24r_bsPGsWqbnnJkbmARYC6MlOTLZJ11s4VhyD8ihmNIMsObNVHbNP5W-qyHg-koimxoVIxuHyO2OooTZht2nGpURLknDIbMVD1maGf1rcssPHHTLP8NWOaKz7hIqurpygr2ddZWHlKqt5n81LnmFu2E-RZ5YqQcWJFu0CmGvFTxyODFyWESC6y8-c9ZNAoDm4AVrFG1JtEyawiaRZ95tE1wMu7Iouy8f9Aa35OWj9C6kT06VKZFvraJVRonhhLDD8BTAnfGNtzdkqRhhAchtk3eT7xt5Jh1p4nsq3xOmJy-Dft6oQKBqxiSevB22IUJxDBSmL7KheGL5FixfssJRtIiW_Y4hg6HIjMez8vxxO-cnFpASBv6MY4xysMEDShjEJ5Avc6u6mRbxqFOw-2AQwOj46aWBRLDBt6veIUfmXX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=aNE9UO_xZfnJu7J2qvJqcs22RzYO05eWfU20aTQwbQRGrBjtbkGXJOsD1oUe17F2Bl68B4B64jbb0wbHhKOeNVXC67f0NSrm2t4WSowJMNxVPJapltUo1JoTOWnd6iL1zeVtVApBhpd-PYTMG2ydcIovp6wx4-LJgxYe-TacsXYDifP0eRxLLQ2jkGrdxmRo5XCqQidJA2UDeDDK7_2t-siWKZuXckJVtYH9jebRrK1sxX3l3xq3wZTQZqQ1o-q24r_bsPGsWqbnnJkbmARYC6MlOTLZJ11s4VhyD8ihmNIMsObNVHbNP5W-qyHg-koimxoVIxuHyO2OooTZht2nGpURLknDIbMVD1maGf1rcssPHHTLP8NWOaKz7hIqurpygr2ddZWHlKqt5n81LnmFu2E-RZ5YqQcWJFu0CmGvFTxyODFyWESC6y8-c9ZNAoDm4AVrFG1JtEyawiaRZ95tE1wMu7Iouy8f9Aa35OWj9C6kT06VKZFvraJVRonhhLDD8BTAnfGNtzdkqRhhAchtk3eT7xt5Jh1p4nsq3xOmJy-Dft6oQKBqxiSevB22IUJxDBSmL7KheGL5FixfssJRtIiW_Y4hg6HIjMez8vxxO-cnFpASBv6MY4xysMEDShjEJ5Avc6u6mRbxqFOw-2AQwOj46aWBRLDBt6veIUfmXX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTpWyA1Um8UKE847zOAdPWmHTMCZQgJrZk4kSUth40Tv9Eb9-erApgWnwc1_M4qHFPvPz2jnmnsagewvlejDdahWt4hk4_uitdz9Jxjoei3ALTCeaPOzBYwfLTksrgRPFohBBUn3z_p-W082kzIbCEpJUBZL8OjRv_Y32tONk_N1ShOZvnK5miHDOKjyxjsg3XUqktTFeY_ONA7YyXRYhyjCI39B7sOnr182VEBWVO-Q3fysKba9HTNpHQOljnFhuQjJTJDqHSEO2y5ASha5s9aRAulu_dRHntROa3RxCqwENAteLwdkcUZy7GrOD3rB5rFdKlp5jCJocN22SSe8SQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=IsJIGt8rs_hSDseRdeAvq9JVclgNKaqEcW7dQSP0L9yTxQjqfTPHUMQx4uoseQ4QHmFFfSYa5SYvgLvAAiXw7g7x_06hWfOIa2a7b110TyudTNujHxbzKgIKU6T3ahg63z-b1FDlA2e1YiolAGMtuThr7xqYYzhdEWYd-WJgubBKlIqMmWAJRMqGr2xix-q5vsOwGEcySfKcSn7JZZyhrKV6Oq3m8svvCRmF660g1P2y25btePW_nClsTNvTfqQIytuDp4Z7vgt45BMRwoV_-dSyIA-srk4ZaUSwNYakiCSBMtNV5m5Ziye75oUIK9c1xTmQGboVMSpql0qzjvlyBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=IsJIGt8rs_hSDseRdeAvq9JVclgNKaqEcW7dQSP0L9yTxQjqfTPHUMQx4uoseQ4QHmFFfSYa5SYvgLvAAiXw7g7x_06hWfOIa2a7b110TyudTNujHxbzKgIKU6T3ahg63z-b1FDlA2e1YiolAGMtuThr7xqYYzhdEWYd-WJgubBKlIqMmWAJRMqGr2xix-q5vsOwGEcySfKcSn7JZZyhrKV6Oq3m8svvCRmF660g1P2y25btePW_nClsTNvTfqQIytuDp4Z7vgt45BMRwoV_-dSyIA-srk4ZaUSwNYakiCSBMtNV5m5Ziye75oUIK9c1xTmQGboVMSpql0qzjvlyBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtYFBByAZJLRyp1GiQspWPbmqVoftGfmtdHqkIq0jIdkb9m2cakZDjQIM-vF5dMhQeBx3zjom9trP0a3gYlVCPIG9pQO4OYCD6pEO2NPWg9Ud5G6B6k3EOdr_eg7g5LJB29PrtXqFpEYUsA9_z-r_-Gbve9klUQ0BHH5wuhGeNssKumowR0X-ymtNVT3fYaxc0CEswQ3bJOVydKv_71BUhQSW9xpUanHBEnliBTkoRlhT3T6nAnpy0GClgntWWHtJlWsNZW5Fn-WHUgsp0DBQx7ihHT8ArDGt-Wn4KiCMyXlKZX5Uc3ju4gTu32LfSzzIwVYupXiyKjFoG0X95urgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVr5V2-ivhh1vG0Dv9L0d4Lwa2Xc30m3YQka2L1erpaEGmJdIrCA45_e1rZqezx0g3pPtMd3Iy1wVFW69mWP1AB0z-lMXTVzKJXDNqysfp4FJk1ZE35ijXrRzj8FFg4lsV1kvPDbL57uJEknt_8_mkCVkFQT5epuVkol7YRhqCxqUDGHvoxCUK6jbKYm5rszsLIsJ3lFVhnNaWKlwsE3kK9W7GHCuH9t62cLeI3gqcipP6zcBv_aLiE2Tgme0RfLr-jp7SzAiWP3yQmKGMXvje5x0Z7EFu9nPTVJFT_325B6Yj-3qcUw3GGUute-0igjP4DtKsu4T6da6b0wdem32Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJy5ufIetx-pVUkhLWrG4t1IIMd56KBHGKtc42W6YvkTQOrhSaSYbz6pYIYX81Zd_UTynr3lKMCg5qKuPKbGoHU7zPjSMqYBBNLYBlGjLAg7sFy1Da2ae4i-us5dm31qUi88XaDqJLFnfPXfR_wU7cxCyu-PvVkW1KzhBfZ-xI7CHLJ1IGRJHpb85e3mnlL13uB9h1LjT9YeCQS3YzpTCUwPNPyaHbfy-XDbPjSQMTjBC-1duT1o1Be_hcLHc8XACqiA6Ozl6sFzVKcx_lp_eiDGpCbuSuPukyEeP7FjId6iFQDJ_5Q0-2Fl5_OYtCnyTqOHv0IpVpXOdlagtblmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=qfO40YqBHiXjjT1hWm02o48lL4KoqMzwI4HPNTQRFRESO00WcgTQtcExiS3r6JPyxGKjVqhZo_flq0ZbO4LWs7BNZClAHCjVnDR1W4dZIpXnSNkmD-JwVgX-pqXz1SLT3ZiGk4qMKIzu0p7odB-udUwArDzSyN6GlAcHmrEGrddhvJNaSjnC5nWjEb8WDgvzQkkP3AJaWjLdEJkQGMZS2tyEwyVdLDuVsvQwhiZatO6Qr5rFCx54ALMTsZii0yVphyxQX8_bILVVWWEk8TbRx64rQtVYfiGsr3aldPgkMojHMEskoqBVxyVZD5H8TlIZnAM9b_c74dU0sADAaW86SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=qfO40YqBHiXjjT1hWm02o48lL4KoqMzwI4HPNTQRFRESO00WcgTQtcExiS3r6JPyxGKjVqhZo_flq0ZbO4LWs7BNZClAHCjVnDR1W4dZIpXnSNkmD-JwVgX-pqXz1SLT3ZiGk4qMKIzu0p7odB-udUwArDzSyN6GlAcHmrEGrddhvJNaSjnC5nWjEb8WDgvzQkkP3AJaWjLdEJkQGMZS2tyEwyVdLDuVsvQwhiZatO6Qr5rFCx54ALMTsZii0yVphyxQX8_bILVVWWEk8TbRx64rQtVYfiGsr3aldPgkMojHMEskoqBVxyVZD5H8TlIZnAM9b_c74dU0sADAaW86SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqxgIMvdUTKAtIGFCnwCBT5xqdom5i4khISiCpqrAlcmtXEhC4QO1YPxDzX8KpPPqgxsFHEcntq5hd6XuamsR_XISyYs3TXYwtqBzrHx-FbLyM8IbQh6pnNMrKPwgDVO1mXJTsJG9CeKu6vArKVERG0E47LsVWGEXpsPxMFIWPHyXy7T0JUyZMi57NkVGLFdAWLNhCRkMaQiwazVi13uvc8-w7UVdi0DmGf-TTflcd-nOFPhtCGBATOCUTqoKhpxdjpETCq44JODSpRTmFS5RSaeSjDYVoFq-llYyAozwKV4iye_GrspIsVpUkzYHuPNe1oCEhpm_kt3sow1F6Nz6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFADaTMLwmXGvULs6OHXp-NSjZtq4ZupNKoCkwUfKgkUNllG4PdppqpYy5kWxgO9MvMw5fSov-Az8dvFgLAnpOzk9Jy7IVG5r8iJTdPHOJ4dj1Rv9-gUrrOBr6_gGtIcHJaRR31Qq-BbYb0a6OXhzCsWBjJ4h2ieUx1VLlnPN-_w1Bw2r8YmUO54gxRjEYQHCh-yv-pQuxlUxFNeU7QxqamDC-hnrFvi0xyF_jU32BwxZcQakwXvDZiiGGMETGePizk4SrAcuPk7sbngRYdNDgfeWvI5CS9G7hk-Peueb7eeUAByaTODWnyCHFT57ZL3XSrxzqYmeBBYjksThvw6dhnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFADaTMLwmXGvULs6OHXp-NSjZtq4ZupNKoCkwUfKgkUNllG4PdppqpYy5kWxgO9MvMw5fSov-Az8dvFgLAnpOzk9Jy7IVG5r8iJTdPHOJ4dj1Rv9-gUrrOBr6_gGtIcHJaRR31Qq-BbYb0a6OXhzCsWBjJ4h2ieUx1VLlnPN-_w1Bw2r8YmUO54gxRjEYQHCh-yv-pQuxlUxFNeU7QxqamDC-hnrFvi0xyF_jU32BwxZcQakwXvDZiiGGMETGePizk4SrAcuPk7sbngRYdNDgfeWvI5CS9G7hk-Peueb7eeUAByaTODWnyCHFT57ZL3XSrxzqYmeBBYjksThvw6dhnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=oxbIytVcXzbLH25hLeI04IV2wgEPs1ThpKcibQs4JNFoa6kPpHPZVVg3iLkoO3vjvQdPBADdZhhmArlbjIkHNR6CgAawbLhfTVBDdN03gVA96AFe4YIQQN7BoqMX5c7HypU3hos6QpO0bOwQpyR_C3zm4jXc6SfZVrcQvxzi1TQq451ELK0-QG9yiC_ajdhH3inJitWCWCeORaQc-OC5UJMCQ_zpm02MaLyRhbV55pyB5-DqrgT7yXBMWhvSC2EP4f-jCGkg6NHfGRcdegrAfVv6gYjeXyrqIMrjlqKtCuMXLeuVokQKwhzFiSXJqIJXnNpcRRzh1RzWbzfpM2zkhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=oxbIytVcXzbLH25hLeI04IV2wgEPs1ThpKcibQs4JNFoa6kPpHPZVVg3iLkoO3vjvQdPBADdZhhmArlbjIkHNR6CgAawbLhfTVBDdN03gVA96AFe4YIQQN7BoqMX5c7HypU3hos6QpO0bOwQpyR_C3zm4jXc6SfZVrcQvxzi1TQq451ELK0-QG9yiC_ajdhH3inJitWCWCeORaQc-OC5UJMCQ_zpm02MaLyRhbV55pyB5-DqrgT7yXBMWhvSC2EP4f-jCGkg6NHfGRcdegrAfVv6gYjeXyrqIMrjlqKtCuMXLeuVokQKwhzFiSXJqIJXnNpcRRzh1RzWbzfpM2zkhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=vDLyMe_L4XlMH08uAeGrtiGKlSIU_XH5CIR_bKPY0jFXnkCJdU_1qECuiAS9_gYZm6AkhsR6w83mIl5yJReHd8BSk26AkmkeUm3eyenIrFM-GPN0l3-mORkj3giDSagrw5hX7LdtCuu58LBgNz_2mLlqn2DMWH1PeAF8XmDpkQrakZNnN698sk2ZaEQi-3UzkUx1wJL2ASLSziK8D9BmbxY2hbLGsJ5XyxSgpewY9c3wTsERr08voSN1el9s21TfqtOuu2BGFj5Tu5p6CPIYbuG6yA5o_y9RoYrc38Dki0xkDaZiXVfNsrhVo-_MQE1wGIi83Gh0oBVvo2W7krr6PK6GNjin59kbeFypykPLp-U3t9fYfSnqvCJBT_vQKAplxrOkT68Y2_Lqwe_TNTsazVTL8YQEHHp5r_WtG2EZYk-LLDFc8ESNYiFByFtWt91fkCm9iFhRnDy-WgdAe24LzvAU0HvCD72Qo2fBA70ASCnJRE6SXJrOSITJwgC7mqaIfcKVKgw_nte0NSWJ2VvwfrXtpePgeJkEfMtHbPO7OGu9SlQ8z5Qlv2Ff_W1ADsnTpcDMY0Ce-xxPwqlWWnG1StLDNWGMkygNWO5CHQcVon5_oL_IK5Y0-RDFqNmTW3UJ4eOyX9aogFMh_IN9UcRFM6GapGxuMfWGOyP80U0NOLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=vDLyMe_L4XlMH08uAeGrtiGKlSIU_XH5CIR_bKPY0jFXnkCJdU_1qECuiAS9_gYZm6AkhsR6w83mIl5yJReHd8BSk26AkmkeUm3eyenIrFM-GPN0l3-mORkj3giDSagrw5hX7LdtCuu58LBgNz_2mLlqn2DMWH1PeAF8XmDpkQrakZNnN698sk2ZaEQi-3UzkUx1wJL2ASLSziK8D9BmbxY2hbLGsJ5XyxSgpewY9c3wTsERr08voSN1el9s21TfqtOuu2BGFj5Tu5p6CPIYbuG6yA5o_y9RoYrc38Dki0xkDaZiXVfNsrhVo-_MQE1wGIi83Gh0oBVvo2W7krr6PK6GNjin59kbeFypykPLp-U3t9fYfSnqvCJBT_vQKAplxrOkT68Y2_Lqwe_TNTsazVTL8YQEHHp5r_WtG2EZYk-LLDFc8ESNYiFByFtWt91fkCm9iFhRnDy-WgdAe24LzvAU0HvCD72Qo2fBA70ASCnJRE6SXJrOSITJwgC7mqaIfcKVKgw_nte0NSWJ2VvwfrXtpePgeJkEfMtHbPO7OGu9SlQ8z5Qlv2Ff_W1ADsnTpcDMY0Ce-xxPwqlWWnG1StLDNWGMkygNWO5CHQcVon5_oL_IK5Y0-RDFqNmTW3UJ4eOyX9aogFMh_IN9UcRFM6GapGxuMfWGOyP80U0NOLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=OwdP2rD7PXTYIMsq7RPlfhc0HgTxx7iK225bo5ptzGTIRbMvCbDU2jInN7z0DWuy_i4lJhjUPOAdFTpFtcDiV0aYblejpwBS1gWrR74LecT-KbOQ9L9BBsEtrezFdGfAhZ7V3Sa_0IxJNHTxAhchu5Cf91FEfIRVX-3M4XwDTY7RQjtpAeN05wSVwFn9I5mBPCtDhcrYrQ9H0O3eFHIpBwYOwSMYnOE4CZilbpd-dfrXRYKWIeCynfRNWPEdDT5NqikjmpGTp-EVkl1y0sGIS_I5_Z_VjE7hYnEHTLh10sVXYhI1RUtGp0hA7obz_n11va2rKTrtLfHnVcOH2snfLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=OwdP2rD7PXTYIMsq7RPlfhc0HgTxx7iK225bo5ptzGTIRbMvCbDU2jInN7z0DWuy_i4lJhjUPOAdFTpFtcDiV0aYblejpwBS1gWrR74LecT-KbOQ9L9BBsEtrezFdGfAhZ7V3Sa_0IxJNHTxAhchu5Cf91FEfIRVX-3M4XwDTY7RQjtpAeN05wSVwFn9I5mBPCtDhcrYrQ9H0O3eFHIpBwYOwSMYnOE4CZilbpd-dfrXRYKWIeCynfRNWPEdDT5NqikjmpGTp-EVkl1y0sGIS_I5_Z_VjE7hYnEHTLh10sVXYhI1RUtGp0hA7obz_n11va2rKTrtLfHnVcOH2snfLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gwnzj-KFBOCpwBySV_vKKfK4mzSFHL1HgpSQYBcRhxpjln4ITPt2n_HKvmk4SDTZwdB2DiIsPoHxqtGfNPLKnnw2mVw7ruX7CMu1Sb0mCFin7xJMhlYlqzgVjOdqj0c3vwjYHC7dDnErniSC4qVU3KQIWzNcbxA4ztVmtXJXRdB65Mnq3BmJjyCHfOw8ApAf_EbO8z9Ft21-Epl4kSRx1-I4eAyILkBZiX1W2JnJbH8hnq9xxMr3uT4W9bIph9C5_s5N1shIdEu2kEu_VqZt1ZgrP0B8Eig_9Y15Dadp111WyTQIcSvhmDyq7YRHAxtAVoiAIlpmH8vD7kA3FSLptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=t9x37qpmcLOjn7HrtWySrSkbsucP_V3q8VyWMMqbcgOSZ6bAAx8BE1hUIsQUxvFuLE-09rhZd4w_1LopV-k2F8AKn4YZW9y1E6haNq56zP0wESAZjSsvFs0neNBDxjKcPMFTMAKYf883COKtqQzqzvhnoN0huAjtJgStsInXPs4BgOyuVDXOZc5s8sN2a-UKqan7CImSG729gWFeLwUKmGXEWAyDzUir6vBnu74AJ6XGePKZw8wO91EFkBe384wlC7UBPctNycJ9zFW9wrRR8SJCDZVO0f4MiytHepdwmilir4dmddOz0DboJSGJ4NIIpGZ1VKHptd8U7B-5po7Acg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=t9x37qpmcLOjn7HrtWySrSkbsucP_V3q8VyWMMqbcgOSZ6bAAx8BE1hUIsQUxvFuLE-09rhZd4w_1LopV-k2F8AKn4YZW9y1E6haNq56zP0wESAZjSsvFs0neNBDxjKcPMFTMAKYf883COKtqQzqzvhnoN0huAjtJgStsInXPs4BgOyuVDXOZc5s8sN2a-UKqan7CImSG729gWFeLwUKmGXEWAyDzUir6vBnu74AJ6XGePKZw8wO91EFkBe384wlC7UBPctNycJ9zFW9wrRR8SJCDZVO0f4MiytHepdwmilir4dmddOz0DboJSGJ4NIIpGZ1VKHptd8U7B-5po7Acg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=N-h5iGT7kaKNjC2biZJ5cO1VhwQWYsblZG8G5lnY7i1gY2w2vElZqBoveOLXDnWOrlZ7YivG6ycijsvkYkvxnNA1DanJPjl0P0C8d-MzpSYRL4XaYvG6dPK48-dNa1MhDNnyc5k8ESvKJ2BdqtLnqQuV9SXu-_r8rvSFTeORZbaOgNMLpM1GKS2CE9Uyt4B4bKHCnNwx9Sw4IfhydRvhFvBl0lM-K6wnl02OSBLYu822p5JE9zejWwJeOX96D9_cH2oeoiTW-yELjuARsX0zrrzocNWkfP0ryadX-jFKQ0o5BbfDOCO_TjPMSL-HTskx6wvO0bTnEXiX0F8CTwXwzw4J6ZnMxzdoB2TltW6Ojk-PPvdo5Wfr0gkq9XZT-F5yHXB06JwRXlOmrhe9MThC6EC_-P8LFnvzG4raEO_Ac5WpHyvxAQ6twP2TRGICiUKu55z0wg2wo1S0D87Yvv_wOQO6TJcFgPhSGn1LX-mWnkSmqMdsNqLpama2P-u7vEb0X76BH0PBLBeiOxOsvbEAL4u3z1pURuT7MGJCvYscv6A9Y2Uc6dPqwKylNPkczulFyUmq8YNxybmvBhJrJbGNzuKW9kP5HtSX1A3ArjGWgIX7Kg3Ndv0xdO1WltuxwghiGWBTtNrrkCpZTBxwG38SSq3tK8wUApye6NmYl6I_G8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=N-h5iGT7kaKNjC2biZJ5cO1VhwQWYsblZG8G5lnY7i1gY2w2vElZqBoveOLXDnWOrlZ7YivG6ycijsvkYkvxnNA1DanJPjl0P0C8d-MzpSYRL4XaYvG6dPK48-dNa1MhDNnyc5k8ESvKJ2BdqtLnqQuV9SXu-_r8rvSFTeORZbaOgNMLpM1GKS2CE9Uyt4B4bKHCnNwx9Sw4IfhydRvhFvBl0lM-K6wnl02OSBLYu822p5JE9zejWwJeOX96D9_cH2oeoiTW-yELjuARsX0zrrzocNWkfP0ryadX-jFKQ0o5BbfDOCO_TjPMSL-HTskx6wvO0bTnEXiX0F8CTwXwzw4J6ZnMxzdoB2TltW6Ojk-PPvdo5Wfr0gkq9XZT-F5yHXB06JwRXlOmrhe9MThC6EC_-P8LFnvzG4raEO_Ac5WpHyvxAQ6twP2TRGICiUKu55z0wg2wo1S0D87Yvv_wOQO6TJcFgPhSGn1LX-mWnkSmqMdsNqLpama2P-u7vEb0X76BH0PBLBeiOxOsvbEAL4u3z1pURuT7MGJCvYscv6A9Y2Uc6dPqwKylNPkczulFyUmq8YNxybmvBhJrJbGNzuKW9kP5HtSX1A3ArjGWgIX7Kg3Ndv0xdO1WltuxwghiGWBTtNrrkCpZTBxwG38SSq3tK8wUApye6NmYl6I_G8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmSLhQGEYwUTUk7TStI50Nrp2jVHUPm4AMeopgwWze8WR_W5lxAo4ebw1MkCjHij9b5Pcg4CRl4fNndrTlSfFdZq1QUA6_Cj9sdUzeZFObGn9xD-yM2rcLQrbuZcmr9abQfOrEk4IP-zi8FKDQR-OolocxoMbzsHqb_yBnpsNy5LX2uj3J_3Y-YECGJpdYhoLixYJ2pwFhZXF0pcMhtw0BPcYDCrIIYQb1cagWV-jzLPTW9_KEnIdDOuBipiSSTrmWujyKVi75AEUr4qZ3S4KHrqhyEcoq-h8XMEboInuKLstQJIQKnGiqnxL8h2EcFlWXmJj-Z0R4qN6irErTmUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=XQ-1t3SJylKmzHChLY4hJMmdniMSPTHRZPryUE2MjDu_VxiMjj95uhCCw74E72RPWZ3nEomia2hRbphSIOPxT3fyb0X4Rr8esswk-qF_iCGAphfCF5nAEvr_dqT6spUbsOzPmfub5EEVnHV95A8ux89weIeX4JRblxr_1bZhE19dn_CKDOl2qQCkF3cAqzdf59_SmFXN4RWF5Zy5XOfE1WjaVOS17J6od78KNUGy2XefiMjiJy31I3aULFDa4gH8uQPAB0iUx-l_8a19tqjrMi_OH-PdOJ28AeYHtZAW_kNrQgKQJkbD9RCga1eCwwI5bTJ5Dw7AkYffwZbattdv6E8jMnmd17jMmoDUd_Pkml-1AJXYHvdePxP7eNzwv1gUhWIOKiHLsARBtb3OpqZiDBEp3FjqN7_d3xf1WgIfIgRAJIrW4DM8dxhAvf6ox-d8-psA4Dkj7-0-fQEkf8OdM3eVFkuRbUXrbOdPy7vA19OCcCdlT9clOetiZwQM0Oh9YduzYTVWU7W5MBwy2m0RrmaZ2y21o9-AhEkwyxbTQDWRofSjYSc9SA6n_SttkxLy9PTop1L_yG4sHmrXDWfiyEYRHLzx_jW3ShhVsJx_kGr4dzfE_ESeEf52xsjOAHDNL4RhkWUDqNIAsWGJS0Pg9Yp_Tx_7qWubUpOUM-2zSvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=XQ-1t3SJylKmzHChLY4hJMmdniMSPTHRZPryUE2MjDu_VxiMjj95uhCCw74E72RPWZ3nEomia2hRbphSIOPxT3fyb0X4Rr8esswk-qF_iCGAphfCF5nAEvr_dqT6spUbsOzPmfub5EEVnHV95A8ux89weIeX4JRblxr_1bZhE19dn_CKDOl2qQCkF3cAqzdf59_SmFXN4RWF5Zy5XOfE1WjaVOS17J6od78KNUGy2XefiMjiJy31I3aULFDa4gH8uQPAB0iUx-l_8a19tqjrMi_OH-PdOJ28AeYHtZAW_kNrQgKQJkbD9RCga1eCwwI5bTJ5Dw7AkYffwZbattdv6E8jMnmd17jMmoDUd_Pkml-1AJXYHvdePxP7eNzwv1gUhWIOKiHLsARBtb3OpqZiDBEp3FjqN7_d3xf1WgIfIgRAJIrW4DM8dxhAvf6ox-d8-psA4Dkj7-0-fQEkf8OdM3eVFkuRbUXrbOdPy7vA19OCcCdlT9clOetiZwQM0Oh9YduzYTVWU7W5MBwy2m0RrmaZ2y21o9-AhEkwyxbTQDWRofSjYSc9SA6n_SttkxLy9PTop1L_yG4sHmrXDWfiyEYRHLzx_jW3ShhVsJx_kGr4dzfE_ESeEf52xsjOAHDNL4RhkWUDqNIAsWGJS0Pg9Yp_Tx_7qWubUpOUM-2zSvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Ax8er2Jip8MPoYitz4es5YPuN-aHv_zzRhzaR1Q5KrqPZypbx4WtyeYFxMBNAMRiQJghxUbCZLjkhiMNJJsJyXSnS_sB4E5cfehfLaSBQZBAw-YQoSkSgmtATrj9O3lx3KMVBglTNBP9cR35n7Ym48snj9Eke-BFvX3BFUX1BlZ8ARQ3Eth9yGytDVY-qqApM5W7PTX8JoIB662AdFGJUQzGvc1QlG19YQ13wqLQ4GrJ4-DqPJJnTRx5I59z_Fii3WAg-89h32d0EZm3sSVhK7NZtSK0-esagPMQsnAnzoj80wzJy93HeTKADlpp_PyjU7NhfKQflXAAEJE6CSH3WpynWoz6BgnE5yLopChZMeXSClXpVjXcvlNLM1YoEMQpqkZAEiUKD3_Iw4WoonO4Xv00xPPdxzfSB7x-ZD8z5oIwIvMXb5I7W2WqR6qXkgowploETA_xakgAu1Fwc6pKiMkMB_nt-qDudTccld6oxnw0vb69WzeniWnly1AUyh0Wq9kX2Aroa5699BijcXY-NONN5xw_5_osFkkqKkT789uPplz-h7uH07X0EZxrYzPoLtuNyjLzbR35zwuHm1fRVutb2HOgfIcR5ronofKcAdnchtm5eQNjNjR36oYA5FszxGcvyXd0puAkwrYPmzQJn-S7d62xSZeM_uP0U6q9FFE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Ax8er2Jip8MPoYitz4es5YPuN-aHv_zzRhzaR1Q5KrqPZypbx4WtyeYFxMBNAMRiQJghxUbCZLjkhiMNJJsJyXSnS_sB4E5cfehfLaSBQZBAw-YQoSkSgmtATrj9O3lx3KMVBglTNBP9cR35n7Ym48snj9Eke-BFvX3BFUX1BlZ8ARQ3Eth9yGytDVY-qqApM5W7PTX8JoIB662AdFGJUQzGvc1QlG19YQ13wqLQ4GrJ4-DqPJJnTRx5I59z_Fii3WAg-89h32d0EZm3sSVhK7NZtSK0-esagPMQsnAnzoj80wzJy93HeTKADlpp_PyjU7NhfKQflXAAEJE6CSH3WpynWoz6BgnE5yLopChZMeXSClXpVjXcvlNLM1YoEMQpqkZAEiUKD3_Iw4WoonO4Xv00xPPdxzfSB7x-ZD8z5oIwIvMXb5I7W2WqR6qXkgowploETA_xakgAu1Fwc6pKiMkMB_nt-qDudTccld6oxnw0vb69WzeniWnly1AUyh0Wq9kX2Aroa5699BijcXY-NONN5xw_5_osFkkqKkT789uPplz-h7uH07X0EZxrYzPoLtuNyjLzbR35zwuHm1fRVutb2HOgfIcR5ronofKcAdnchtm5eQNjNjR36oYA5FszxGcvyXd0puAkwrYPmzQJn-S7d62xSZeM_uP0U6q9FFE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=GHIsUXvz1-wfZFATx_Flgb-z-hoeAXxK1Cb6czuQ5q_SG0i7Dr8RpKWfDk6BABL-ZBUe8fB8HtwNCquDA3BlvA8sEkoVjLZNiH4T-GrVVKctjmL3nkM35PlS4-tv8ybfY0mfcEUuxECVD1iFU-M8BmMsV233XrLoNISq4-cLXD_l9Xq0YbDwGGK_-j1xEfqliAY3R21vlbnwBsBXKJUEPWTZph-k5XY3HQVFacie6sMzdNRVaF5xnDVHxdiauUZhdCeNtbN15cqoIiFOFBg0FdPzEet7WJI9AIuJvPAWKq5ZuuL6X14ZFXr05Kl89pW8ngUmmU-9LHKARH6z_j-zaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=GHIsUXvz1-wfZFATx_Flgb-z-hoeAXxK1Cb6czuQ5q_SG0i7Dr8RpKWfDk6BABL-ZBUe8fB8HtwNCquDA3BlvA8sEkoVjLZNiH4T-GrVVKctjmL3nkM35PlS4-tv8ybfY0mfcEUuxECVD1iFU-M8BmMsV233XrLoNISq4-cLXD_l9Xq0YbDwGGK_-j1xEfqliAY3R21vlbnwBsBXKJUEPWTZph-k5XY3HQVFacie6sMzdNRVaF5xnDVHxdiauUZhdCeNtbN15cqoIiFOFBg0FdPzEet7WJI9AIuJvPAWKq5ZuuL6X14ZFXr05Kl89pW8ngUmmU-9LHKARH6z_j-zaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=qlWJ1Hpibtvvw5qjO5eiFgFoVAXc-HiCG0hYGsNeBvN9Vr_ulQwFOVmxR2U6DE_HhIOMDO-5cepvDYLrJ-0AATWfcp624RBejm55C_Q3gJDh9pkg6INsZe6ozz1QyBhI4ULz9NDKGpAZw0xbMDd31sk-al-cBUMHiQzFE6pJiqBQ5feHbITVMHr13v6LS0FtQXpjiXZEuqRdf6TdSXvYVdKpndMrP8LsmB0s6i6cwmQSEAKmg3ynh19glmo_vSCDp2GWvy5jVqNyhmiq3E69H0nF9vzUyli-ITzxMZ2P7p07c9sZI9EfmoxQQZU4Qf6qdlvACyMl9BfneIr21C9YHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=qlWJ1Hpibtvvw5qjO5eiFgFoVAXc-HiCG0hYGsNeBvN9Vr_ulQwFOVmxR2U6DE_HhIOMDO-5cepvDYLrJ-0AATWfcp624RBejm55C_Q3gJDh9pkg6INsZe6ozz1QyBhI4ULz9NDKGpAZw0xbMDd31sk-al-cBUMHiQzFE6pJiqBQ5feHbITVMHr13v6LS0FtQXpjiXZEuqRdf6TdSXvYVdKpndMrP8LsmB0s6i6cwmQSEAKmg3ynh19glmo_vSCDp2GWvy5jVqNyhmiq3E69H0nF9vzUyli-ITzxMZ2P7p07c9sZI9EfmoxQQZU4Qf6qdlvACyMl9BfneIr21C9YHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=R8VPlvlxzuO2aWRwUcaGgVhBiRmT-mYKuRZFzdzlm_EvySkJ6ozl2Jvmeg-jX_-vJGaHpI1U5vkhDNTfdLCs0vvke7iIBfUSSBd0_uUSJGbNPbmZ90CYUvknCdB6qLB0_GKKi2i8Fj8RIsy8jotP4DlGQGrhEGCIwMeQ76UMMSNJel1-JkONNQLhkuhyontGcRkHUKz9pNeH133iDezzLNWiSv-gZuXxU2fmM_1tbjvyvhrkgg9LFLk6PBbTM5ldc7ThpBLI4HLQW6QwxtPTzFjjZ2arI2zZZCp6ODs-4beIHJGXvGBRmUvFkSN8nlHQRVQb3hRG6jskhi22D6DcPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=R8VPlvlxzuO2aWRwUcaGgVhBiRmT-mYKuRZFzdzlm_EvySkJ6ozl2Jvmeg-jX_-vJGaHpI1U5vkhDNTfdLCs0vvke7iIBfUSSBd0_uUSJGbNPbmZ90CYUvknCdB6qLB0_GKKi2i8Fj8RIsy8jotP4DlGQGrhEGCIwMeQ76UMMSNJel1-JkONNQLhkuhyontGcRkHUKz9pNeH133iDezzLNWiSv-gZuXxU2fmM_1tbjvyvhrkgg9LFLk6PBbTM5ldc7ThpBLI4HLQW6QwxtPTzFjjZ2arI2zZZCp6ODs-4beIHJGXvGBRmUvFkSN8nlHQRVQb3hRG6jskhi22D6DcPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=uHt5CYTk2Rj2Y2pnPRil6A8mo7GGMZlz58Nm9sEmjPHY-X_NZreFQeXdC6oQq2r_KWT1tf_Ra42chpyCYT9HDgB_f8r44U0t3Tmz-HJvIeWF7JHxjyMHjLUqOIaxZQrWMcp8GLvgSfwL4yrUXJXphNqjtwiJRvqrfsrVRJLYtJB6ATVhONKn2u8gO8LfyjQbgJUBiAs-Yf4SnhNlRD_2zf8JhuArC9s4hqXVjSp7bBGn_30c3a2gDVY3CsDd5bC-CVsK_59nGUlWSOCWT1_8s80MGq-Oz0t-ZtY9nA88T61r1XbL0nxnm1vb8XRS56LNIrxXEZcFbVsBSng6DPTsvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=uHt5CYTk2Rj2Y2pnPRil6A8mo7GGMZlz58Nm9sEmjPHY-X_NZreFQeXdC6oQq2r_KWT1tf_Ra42chpyCYT9HDgB_f8r44U0t3Tmz-HJvIeWF7JHxjyMHjLUqOIaxZQrWMcp8GLvgSfwL4yrUXJXphNqjtwiJRvqrfsrVRJLYtJB6ATVhONKn2u8gO8LfyjQbgJUBiAs-Yf4SnhNlRD_2zf8JhuArC9s4hqXVjSp7bBGn_30c3a2gDVY3CsDd5bC-CVsK_59nGUlWSOCWT1_8s80MGq-Oz0t-ZtY9nA88T61r1XbL0nxnm1vb8XRS56LNIrxXEZcFbVsBSng6DPTsvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=PlPYTtJx_U79GyTY1Y4FL49O8vRVwchoJ4EwoMo8zGhhF_8Htldi-0djLnHPZBWWwa-sNIC8DHppUlPdc-1SHFzdQ6LJzYeaN5WZS12rItA3BfxEZw6-lTEb-fSCfBTpx773IrW9iNkwnElZBmCnqa8OJs5OLgrKlg9vpOVzvtiZmZYbEEDFXSojxxOsGYmb5NCy_OoIj6KLNpHK27my638PAWRWwA0DetiaE1WwhyZa6Db7MeNirh2oU77LXPl_jT5v31P25HZmWoBx90YpdmAs1U21TtAEfQTUItWgNy4_lb85ChCpEBFF5BomxaT9yv3mHTw03MkEH-oJyzCh5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=PlPYTtJx_U79GyTY1Y4FL49O8vRVwchoJ4EwoMo8zGhhF_8Htldi-0djLnHPZBWWwa-sNIC8DHppUlPdc-1SHFzdQ6LJzYeaN5WZS12rItA3BfxEZw6-lTEb-fSCfBTpx773IrW9iNkwnElZBmCnqa8OJs5OLgrKlg9vpOVzvtiZmZYbEEDFXSojxxOsGYmb5NCy_OoIj6KLNpHK27my638PAWRWwA0DetiaE1WwhyZa6Db7MeNirh2oU77LXPl_jT5v31P25HZmWoBx90YpdmAs1U21TtAEfQTUItWgNy4_lb85ChCpEBFF5BomxaT9yv3mHTw03MkEH-oJyzCh5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=KYE8XKjZSkC4JXLn9b14aRPVsZKcx9r00dUG2p5Af0mEHn4N7CoHjvPLpljLhqOgfD-KokJC7qWPso5nq5WyXkWcsLguEg_Xh6Nbh3FsRqZp6go2-CrTYp9U1Z_QZZ1BCxKTg7tRJuTl7797y5ROzmcrc8vsQK9zSNqcSIw0gHPSgX6BDybJLPty-0cgtz001vmrzJJPL2OcsakkQulgtrxNE4u-S8ch9kBgR_xxXoemsYnAluV7CEqI0f8PHfSz1PlrKtgJfMnHzbySiaJUeVL2VhaB1ytx0k2HiTR8kUBmiyGjvFqnFlEV8Ves8LdkqEWOk7dKHD6V9HsohnMTfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=KYE8XKjZSkC4JXLn9b14aRPVsZKcx9r00dUG2p5Af0mEHn4N7CoHjvPLpljLhqOgfD-KokJC7qWPso5nq5WyXkWcsLguEg_Xh6Nbh3FsRqZp6go2-CrTYp9U1Z_QZZ1BCxKTg7tRJuTl7797y5ROzmcrc8vsQK9zSNqcSIw0gHPSgX6BDybJLPty-0cgtz001vmrzJJPL2OcsakkQulgtrxNE4u-S8ch9kBgR_xxXoemsYnAluV7CEqI0f8PHfSz1PlrKtgJfMnHzbySiaJUeVL2VhaB1ytx0k2HiTR8kUBmiyGjvFqnFlEV8Ves8LdkqEWOk7dKHD6V9HsohnMTfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=QGh2EM38UOJtvzraQFmqXWEehDO1bdyr_HuMvxbgGCC331yiCILIzril6VOhV81CqcOsb_j_CgDbNJn9irfpYcip5v-dIx7EMSbwj1gTClEUP5eA6lv2iXQM2bEN62ikBo8EXFAXLEkTuYkvZZOLuB3l4oV_1ZEhxP-rNhOKwDia-A7BzYRqbfGldgrtht7uFSEqYXnssLHkTFyT0XYMBs-IRZhV1TbWYgVDkUfAexmy3gljRPDpJJwp1PJrF6be8OffcgwLQFV3Y-6av6A54QAh4iBpWEBPIzOS17IrP2YrjmS9T4pyhcg74KI9z7wjqUpjPm0jYbLW31kzHIK-oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=QGh2EM38UOJtvzraQFmqXWEehDO1bdyr_HuMvxbgGCC331yiCILIzril6VOhV81CqcOsb_j_CgDbNJn9irfpYcip5v-dIx7EMSbwj1gTClEUP5eA6lv2iXQM2bEN62ikBo8EXFAXLEkTuYkvZZOLuB3l4oV_1ZEhxP-rNhOKwDia-A7BzYRqbfGldgrtht7uFSEqYXnssLHkTFyT0XYMBs-IRZhV1TbWYgVDkUfAexmy3gljRPDpJJwp1PJrF6be8OffcgwLQFV3Y-6av6A54QAh4iBpWEBPIzOS17IrP2YrjmS9T4pyhcg74KI9z7wjqUpjPm0jYbLW31kzHIK-oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7grEX6M2uX0oSsbflK5dcjf-FcXas6Y7aCpHA4UIEJnrC6S1CHS8CI9EcWzQdtC3vg3mXCUOwlOId2NCnTnLPnGS9yQ1aJ_jDwFnMI0tqpiMvuNyo_fyMyhUj-8QI-01fWjZVLdpp0hLV1wb9Fx0jl6S3uOgVssSrFbtecTLg0p7YZdCkNxmWj0IT_OnjRoLBX_piJt4l_bFTlYXtxtuSqj6kOJELtmbrNGzHZAKwoVIRLcVDyXO7v3_EoQq05HuqchDZyfrzm5Uo8gzYuo_yIGdU-2iqQp_qXuIejIxsPLQmTTq3tGmdD1TL7RcFSwNF1XlLZatEtD_ZmpBwwguA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=enasZDPmkCuTidZYoiPr4bzTjgX9Gt6vN61pHY9TEYZSFGxa2tHJrMU2DssZUlFRMpVZHyhybLq-89M0v0GB8xgTMLBhckB2rHNKZ_SOg4BB_9Lzrdw0E9ekuprcumos7jKwseE_RdmHx6SEugH6W9aF7D-l0jd1_hd3ldIybaVQRThT3tu90LnBtMT8Dlqi0lBoYrp1dQ8EH9ThLw5naZy9rldjyiNczUA4ngg6lbv5Py2fzgu6XgYoYt-nKDG317nqgly3MyJv1T3p22zoo3tMnut6X2VXacsA2AZcJbCzDnv3Bfy5QgyLugzcB8rfM5dOtLWuEry2ENp8pzBC7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=enasZDPmkCuTidZYoiPr4bzTjgX9Gt6vN61pHY9TEYZSFGxa2tHJrMU2DssZUlFRMpVZHyhybLq-89M0v0GB8xgTMLBhckB2rHNKZ_SOg4BB_9Lzrdw0E9ekuprcumos7jKwseE_RdmHx6SEugH6W9aF7D-l0jd1_hd3ldIybaVQRThT3tu90LnBtMT8Dlqi0lBoYrp1dQ8EH9ThLw5naZy9rldjyiNczUA4ngg6lbv5Py2fzgu6XgYoYt-nKDG317nqgly3MyJv1T3p22zoo3tMnut6X2VXacsA2AZcJbCzDnv3Bfy5QgyLugzcB8rfM5dOtLWuEry2ENp8pzBC7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=VzNftd5oGzl-m8YpAQJH_BxloERpfQLDRmQ2Y9YY5Sgf_-D-XU6jp2fWa1TF1HLxZqJFdDV7XyMYGFV00by2pV_gMfTE6Dmi0LK4iQXQ547BxLankmt7HuV-zvDQacXyqdT415mZtsZ86db7tr2kfD3qb9oTW-KltCUVO5uykyZ0OFA0s-RefI9Hsxp1OUm51--KwrhOxAOpOglIcbre8HHcJyY5ZceW9s6NJvJNekLeYzz6KuQyzZ_b26u49mLDhRTsO2-XFFrOr0WFZ9PIUoK77ciPRDaIK1rz4GusWIfOEnmseHtdV9eAmvWX9CRq4-g7Yf-S9kXWrRbKAKWJZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=VzNftd5oGzl-m8YpAQJH_BxloERpfQLDRmQ2Y9YY5Sgf_-D-XU6jp2fWa1TF1HLxZqJFdDV7XyMYGFV00by2pV_gMfTE6Dmi0LK4iQXQ547BxLankmt7HuV-zvDQacXyqdT415mZtsZ86db7tr2kfD3qb9oTW-KltCUVO5uykyZ0OFA0s-RefI9Hsxp1OUm51--KwrhOxAOpOglIcbre8HHcJyY5ZceW9s6NJvJNekLeYzz6KuQyzZ_b26u49mLDhRTsO2-XFFrOr0WFZ9PIUoK77ciPRDaIK1rz4GusWIfOEnmseHtdV9eAmvWX9CRq4-g7Yf-S9kXWrRbKAKWJZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=i9saG3F1W4MuptLdeAvmhFCSl6SDmSacPOoY2l484rHL5YJPIva5EMO8fFS1ws0FgCoxd7wi5TNmn3bgcGGG9MR5uD7HkEKsd9ETEdIJHr_YKs4_isCni6WvOctgyZ3kIjcqTkibLXt1p6xlzYWkrb5q2DQF9Obu_J9d3Gi4HSqF0cFM7-knFO1i-VLQWPGM_B9drbOqoVwbjVVMskAx4ZNgrdiIjn5EPbPPlO15qKU8AqnJgQAmM817LsWHjQtIV0oJUbtipziOQlrutDpcmmQ4-xQ2weLFhIOwXY7PW_bdE_FW6Xx_B28_EEDWP-jrhLgONSDCaEzB100yQynGaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=i9saG3F1W4MuptLdeAvmhFCSl6SDmSacPOoY2l484rHL5YJPIva5EMO8fFS1ws0FgCoxd7wi5TNmn3bgcGGG9MR5uD7HkEKsd9ETEdIJHr_YKs4_isCni6WvOctgyZ3kIjcqTkibLXt1p6xlzYWkrb5q2DQF9Obu_J9d3Gi4HSqF0cFM7-knFO1i-VLQWPGM_B9drbOqoVwbjVVMskAx4ZNgrdiIjn5EPbPPlO15qKU8AqnJgQAmM817LsWHjQtIV0oJUbtipziOQlrutDpcmmQ4-xQ2weLFhIOwXY7PW_bdE_FW6Xx_B28_EEDWP-jrhLgONSDCaEzB100yQynGaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=nBMrzCEXZzJRGDyuX3JgzdgI6leMhZqRiHCGeWWOkp-c7WPVyQWrKPLR6t1ucrRi_3Kf71vnz5fd1mFETj1VI-Qla_r2DKmfIWo0i_ktVtsuqh1wkVQlmimE3f_rBP0TRVC8Hh3c4NHEzvrbOq87_37wQucq8qYJNQ6Db_UdMFC9_C5-fjIKXqVRGvtYsLq9IIyajN43YaEYTj_3ABZOx7Jv3VnvmBYHSeN7KjDlkAe3_PGZn7ZF-XSRxOWUph5LPiYi_67wDZsBwqdehj0-hkbKmNpyrP7vHv6uBqmT-Vam3UWTjX0N3FZZKzXamnxCFGs4bwcbxAj6KB985gcZqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=nBMrzCEXZzJRGDyuX3JgzdgI6leMhZqRiHCGeWWOkp-c7WPVyQWrKPLR6t1ucrRi_3Kf71vnz5fd1mFETj1VI-Qla_r2DKmfIWo0i_ktVtsuqh1wkVQlmimE3f_rBP0TRVC8Hh3c4NHEzvrbOq87_37wQucq8qYJNQ6Db_UdMFC9_C5-fjIKXqVRGvtYsLq9IIyajN43YaEYTj_3ABZOx7Jv3VnvmBYHSeN7KjDlkAe3_PGZn7ZF-XSRxOWUph5LPiYi_67wDZsBwqdehj0-hkbKmNpyrP7vHv6uBqmT-Vam3UWTjX0N3FZZKzXamnxCFGs4bwcbxAj6KB985gcZqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDPkQEeDZlXVNT0ReMUXAkzvl3J_71zmCVbzYlUKn0mGD7SQDbrMnvL445RlksvSUxC0nGIHNXBuO0uYq1TIDsJWjq3lGxicQ3IjfyueuSk-3hs5kaJybtHP4Pzs1hz3OdGy8rMjT4JCahEtWBd9jDWP_Vp-1kDGNXDPuPkcqffa2iGIygcwGFyQsun0KyNsxeYwlYmYBvdw-uZ_HPNNrR2Xdf4l2Oh5BOO8M0zfbfgjKa2vJFc-7tL3mbYQd_RRw7-w6ry8KSL-q30-_TUblePUjgI8ImPhDFeb_ilHtOAy30pFF_rkZYbfqzG4hAVIFtLsapwS1spLm99lCpNQdg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Z2wex04oQNOp1xqf6qy9SQ2LBmQXWMFYuCUVhi8l8pSrf0mojs8Q6-c7zvDO67k7xMYvgd7wIv-u5mqbig_UM0noE--66kTyy8i47Hs4AqWllKkEUjuQ5rYlS_1Tsqr05UyHc6yGwUJEsHD5rKb_6xQC-18KcCcpQLr9j0Ew6ifkMGjnpwma_DFkmpryUcIjVPdHPUjc58XaIP3aqCDLjBZ-VCd9XG0ThuydvpX-TsBrMk-zvPWs1hMFQlSLHoHmmEEWbrnbJGNuiHxk6LzG6OFYdsS6tuBzqZGGcdl5a2IyDrCWxBIK2_vw3k_kD4I9jfesCeLb7CjqNp4Fbd7NcTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Z2wex04oQNOp1xqf6qy9SQ2LBmQXWMFYuCUVhi8l8pSrf0mojs8Q6-c7zvDO67k7xMYvgd7wIv-u5mqbig_UM0noE--66kTyy8i47Hs4AqWllKkEUjuQ5rYlS_1Tsqr05UyHc6yGwUJEsHD5rKb_6xQC-18KcCcpQLr9j0Ew6ifkMGjnpwma_DFkmpryUcIjVPdHPUjc58XaIP3aqCDLjBZ-VCd9XG0ThuydvpX-TsBrMk-zvPWs1hMFQlSLHoHmmEEWbrnbJGNuiHxk6LzG6OFYdsS6tuBzqZGGcdl5a2IyDrCWxBIK2_vw3k_kD4I9jfesCeLb7CjqNp4Fbd7NcTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=V7A664_7AVTN-FU7KH6WX_DUy53Gq6KNI18kpgfACujgLNXgNTSy3rVx1gBkPn9S9zjVxt0K21z6zxP1kU0QBbcYbJM4Id7uWQ_r4E-5KCsuPUmUHvRwvIiBjx8npSZ4zDWYgF08algg2I1XXSw9tnVvsE-Y9hV_-psLUiM-ZLM4YdSt77T8S-InjPqEurm_boAgBJkgtaAqSsoaxvw9iW9vSb8HKh8T-CM3WmjmOzcfdeCeBn9VKzhOuQu3R3OnTfRAtcr--9YLR-w6BjhVtt_zgKn9EjzVh4UFUq0CM2aysB53cCjSoEIiW-sXeKJHA8eIz5M2nODwBA-ZyG94WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=V7A664_7AVTN-FU7KH6WX_DUy53Gq6KNI18kpgfACujgLNXgNTSy3rVx1gBkPn9S9zjVxt0K21z6zxP1kU0QBbcYbJM4Id7uWQ_r4E-5KCsuPUmUHvRwvIiBjx8npSZ4zDWYgF08algg2I1XXSw9tnVvsE-Y9hV_-psLUiM-ZLM4YdSt77T8S-InjPqEurm_boAgBJkgtaAqSsoaxvw9iW9vSb8HKh8T-CM3WmjmOzcfdeCeBn9VKzhOuQu3R3OnTfRAtcr--9YLR-w6BjhVtt_zgKn9EjzVh4UFUq0CM2aysB53cCjSoEIiW-sXeKJHA8eIz5M2nODwBA-ZyG94WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtzzB0DcfEexD5hM7JABulSdwbN8UoTxXBbLqfm3R6KlVheTJ-b3eiIFMkNo4Fku1--mrHbCPimVP-cHwGljrSYuwkMagrHgkVASdQRMvjCerirLH8njFpp82X6PI87To2G7qjdc15Gl63nHjPfjpDpBxpWi-Wz6S5t-YlQYIrvUKyZGlFkqtoDBRW_LouXfNiAGd744VYkdfj5nnubfskCItwIZEgKfgABP1-IS1sz0T36yjfrZ8nrecJ5RvV21Plcmb7D2EPA4wP8vCMzjgRgmbMflgENiDIxCuoA4IPT-a_JIjGLpC2Fi6qNNhRCPoBi0RwXq_T-_5zjattBVEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-99Ys3RgqXVF0HtMfcaZYkZOAYfljYynb3VLq4LRtWU0hvJyQgjLehuWi76s74YoP_1XCJiS0cQmnS96f9oOQ8UTNlxCz2J7ewm7EwmMSbbPv9FGkw_CEa4dGtHG2FpOfb0QqyJlVAzY223qMtI0JDR6pmYXxMVqB-m8MddBQm7r3aPEnfP6q84T4o7W_Wc4JUy-2uerjOSRVOeRxkpDqR9Xtp7xKA739x6MQL-fm6BhW3v27d7xJOdDuwwOD9B4No2Ibi-qltbdQDf8N5kbV0IFw3-0GcE5wad8O3N--hDWM1qWMrOzE2hUW19C_KjNlxIO0a6aMIGoQfKE-UJhQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=RbnpR-LBL_3rRU24lWI6MQuAlpUkpH6fYTEyCmh-QqJXZB2T0LSADSmPnam9yllbUX7IZMLB-uvYVG5h8-QD4IUdjLGjdTmUgQkEOjo5LjJhhLS2dGCpHWWPMftr6LRePXGTFM34FvnEp7CQLhdkr5azqsG11JGm_D2cKSq8ZD2RhuIYjV57IrsxQOZ9i7h8GxsJpqaBiO1X5UVHVXtybImkrMh-cOcqVpv51afgzPHqBvAeqyLx5BGNLS3TGrt08BZxd0IVRgbjxAWP5ffXQcf1lC_BfUncAm1OW1UqTvV2ElY6xe5ZDhJLG-Fn_DuxuycYVRCc87RxLiT2wrC01Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=RbnpR-LBL_3rRU24lWI6MQuAlpUkpH6fYTEyCmh-QqJXZB2T0LSADSmPnam9yllbUX7IZMLB-uvYVG5h8-QD4IUdjLGjdTmUgQkEOjo5LjJhhLS2dGCpHWWPMftr6LRePXGTFM34FvnEp7CQLhdkr5azqsG11JGm_D2cKSq8ZD2RhuIYjV57IrsxQOZ9i7h8GxsJpqaBiO1X5UVHVXtybImkrMh-cOcqVpv51afgzPHqBvAeqyLx5BGNLS3TGrt08BZxd0IVRgbjxAWP5ffXQcf1lC_BfUncAm1OW1UqTvV2ElY6xe5ZDhJLG-Fn_DuxuycYVRCc87RxLiT2wrC01Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIYILjGwhBJO1r_3y3UGUIjsKTH9kf9KvlHiYyGiE76UfdRdEAQYAJ3EhZfFy5HMY7wkFMHatm1z6QS1ovfwqpegwECtsMsGp4sMHlxdZk9lutBL2NQ5exXdKayY_8g7tR8C8DftBC8HfyvVES3-ncqgRW884DJsLmh4rdB2bidB3N3Oy0qE7ba6HwTZ6ocHPWAjY1nz5K9-VB22WQBDj3KABbZsFwp6PwWBVTORRx8Fbj2z39TRiA6x0-zwgk8qIJnHtGkyjkyDD4X_-CDHmXr1vhHA0czL4SOY1xyRSdxD7v2ngJ5hdznjhVzCn9QOXRN8dydLaxHk05TnCy3-zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koH-ERFGaSZDHZcotv5CT9JxW03cnajlVD7UY7B3qNQZmDawkGtq7Hr-nJnmxt1Rr5jcgpgYhYTcytGJS7QuW4mfA_oa-hga5okECdg8pYzWf5ZF2r50hWKAAohkTO1pLvG4nJInMBDvqgeIBU70b6BQ9rjEm_2wpx6gg7B3-58YHwi6OylDlBhrcQCojvIh-WJLvRRGl2lgq7B97uGp7Zn6nR3b7gJ38fkVuTy8j1WIBGgPiLg_l7b1yBE4Mz7K7LxCAc54zmHssqjVJo_QhbdO-KM7MmLQiZ0rPQiZ6MLUNwmJCGHcIYizqHPLKwGD73fnV8tfygWVWRvX-VGsOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJA0rNrxb9McGJFt03SlxfQdM-_RrJ3Dcr9xHCIYHs8XqdR_HSyX2ThrmBOFG42z_bkYnRtq9-9PfgiVoxTobf0UfL8lT8eaSqVUyCBCMo5VnL5fmmRtOi3JuYD3FQBAXg5fdHMrk0diD4x_OmGSim2WUNQbGSP1Xmj1sED1mfVuXJBqjm8B6ij01qj47UaNBHyrfevoSXaicLq16HLBSdKcmFI6CgoVckgdgD1O_zIO_vsgeNH6SRNiMnNZzGtEIUh0ro6x4FdoaPOp2bZtTKB98GY0aZS6FVfCGhO2_nl59BaRoC3Bfh14cg0Iw8DWpK-tGmXYrTAQG5BWU1soJg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=BJMI7fet89-NwcjENiMAAui8rDOT6oEsw332Sc744W2DRTidkVmz1qFQRjr_x7nIKw66bHoYeHaYagz3lvFU1iGJxmW2eltyelWoWBDNK1BcnJjwSHYUKC3tKp8ka3N-oOa-TEI-n9p4JEpwb9qpVtPgIbrD_mjZvmoWiP8w7paVpzV9smOVkZJFfF9NtuMaPfkbHD5EpjGOZKBpLjaVA7k_eLxdYfEmF_Qkvx6g3GUwy7YrtZiB5xZM7CE8P_-oL-M8SpeqGEFSgF8PFmZX2YCuUUwR6GOI6vvNwLTJvMr4YfUmSjhd-X1Y4yXYIHG5fmjLmqiH93COErQA8Pe0Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=BJMI7fet89-NwcjENiMAAui8rDOT6oEsw332Sc744W2DRTidkVmz1qFQRjr_x7nIKw66bHoYeHaYagz3lvFU1iGJxmW2eltyelWoWBDNK1BcnJjwSHYUKC3tKp8ka3N-oOa-TEI-n9p4JEpwb9qpVtPgIbrD_mjZvmoWiP8w7paVpzV9smOVkZJFfF9NtuMaPfkbHD5EpjGOZKBpLjaVA7k_eLxdYfEmF_Qkvx6g3GUwy7YrtZiB5xZM7CE8P_-oL-M8SpeqGEFSgF8PFmZX2YCuUUwR6GOI6vvNwLTJvMr4YfUmSjhd-X1Y4yXYIHG5fmjLmqiH93COErQA8Pe0Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=i6MG4Lfhf18oxvV66Z-q0lCEnvFfA3EEVcdMvSfI1KVLhyZQ7hd_eg71hX07nqcgXLhC8mOmPlvj0dxZgqfsBETVzmzH6twRwsNV4ZML_1Q1Wv2Py7YH1XqZCcqtDZIYlOu_H4aZXtRNKtRK0SjPNK_TSYwm_ZKArU8-z1gxXKPeKzhTCsWOI1Aep8-gGncix_WZ1B3Rwjl4gWTGgAynI7Ki80g0-WEGSNlm6gcpsYkTlrqbfmR7PbRiavr677n5BHpurOYpLoPh98BpJRJZxDXi828t73FHlkw9oJK7cWvoaFX7qpDu9bIRkqnscJXZkXHHyQRMhKSsjjOghNIuww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=i6MG4Lfhf18oxvV66Z-q0lCEnvFfA3EEVcdMvSfI1KVLhyZQ7hd_eg71hX07nqcgXLhC8mOmPlvj0dxZgqfsBETVzmzH6twRwsNV4ZML_1Q1Wv2Py7YH1XqZCcqtDZIYlOu_H4aZXtRNKtRK0SjPNK_TSYwm_ZKArU8-z1gxXKPeKzhTCsWOI1Aep8-gGncix_WZ1B3Rwjl4gWTGgAynI7Ki80g0-WEGSNlm6gcpsYkTlrqbfmR7PbRiavr677n5BHpurOYpLoPh98BpJRJZxDXi828t73FHlkw9oJK7cWvoaFX7qpDu9bIRkqnscJXZkXHHyQRMhKSsjjOghNIuww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=BwVr0Lp0SHIyMdqkS08g7uxqA20D6xIbh3SRml6YQbDvPV8eqkgo5LAKWO1DBtun3_dBEqrlDAB_K_yTM8fLH0oITtAwGyxUOpJy2O5vUhQY666PzERP2u17TB5tHrXAwuQZvLmbQKi6v00w0SAo8vo8r1hAQ2uwjcOB4M9jCeshRSii0rUGOvYec_h468FDjlTE-uqn8PA3HDcRtGss-xguquijvF4cI5Hle4uXzuAjeTTQeSXFK5WhfB7ppQnV9hNnkbBNUvx-6q146wPRl_doAFrqPpbz6r9bI2kSXYfoIbK5YFosVVKCxPRDQJZi7Q42eL-GkLai0BFN5HGYKCLF3_Z0Zny2fIJ_ZONCOPBOUhjTddqBnSLNgbfCA43siGaNFsTUwbQSghaRYfNtsuGuoQjjazQ2yc_Kdz-Vx_mI4N1PkIwZ2I_8oJomCc5oBBBxwvK-JW4XUVhYON5xwXLfbOE4gp5-wNO7vvTLrXTAE8bGe0dpXQsrhx3uaI6GPDrJf2RilOwORrUy6_KMDBEpak7Qg4JsaMZbj1sQnRkioLr65oyJN_UsKcr0-_UYKqeIojFTOpgBLx5H8hBttn40uyEie8jokzZketSW7S1ye5FMiTo0UUX6TF9xWPSfCGIWf_vi-0NDFJ7CjAXPGpse4gDl1u_-kR7L6GKlpFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=BwVr0Lp0SHIyMdqkS08g7uxqA20D6xIbh3SRml6YQbDvPV8eqkgo5LAKWO1DBtun3_dBEqrlDAB_K_yTM8fLH0oITtAwGyxUOpJy2O5vUhQY666PzERP2u17TB5tHrXAwuQZvLmbQKi6v00w0SAo8vo8r1hAQ2uwjcOB4M9jCeshRSii0rUGOvYec_h468FDjlTE-uqn8PA3HDcRtGss-xguquijvF4cI5Hle4uXzuAjeTTQeSXFK5WhfB7ppQnV9hNnkbBNUvx-6q146wPRl_doAFrqPpbz6r9bI2kSXYfoIbK5YFosVVKCxPRDQJZi7Q42eL-GkLai0BFN5HGYKCLF3_Z0Zny2fIJ_ZONCOPBOUhjTddqBnSLNgbfCA43siGaNFsTUwbQSghaRYfNtsuGuoQjjazQ2yc_Kdz-Vx_mI4N1PkIwZ2I_8oJomCc5oBBBxwvK-JW4XUVhYON5xwXLfbOE4gp5-wNO7vvTLrXTAE8bGe0dpXQsrhx3uaI6GPDrJf2RilOwORrUy6_KMDBEpak7Qg4JsaMZbj1sQnRkioLr65oyJN_UsKcr0-_UYKqeIojFTOpgBLx5H8hBttn40uyEie8jokzZketSW7S1ye5FMiTo0UUX6TF9xWPSfCGIWf_vi-0NDFJ7CjAXPGpse4gDl1u_-kR7L6GKlpFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=AN-5mZsiD3TXq1ArFUq1BPS4yUvRqWiAT4Ubtp0Pmn4Q_wLtPsxktB5ku1p-75iVsZEZ_x4bX3wJ6Zg59_ihlCk5SBc2Fw4yXyGtRNjleq1FuO-x8VqPc8fbm0YWSVONwhh7frYIqtSsRLSekJULgbMAMGEx959ipxtOnO9EVP6SE_6ZeGOqXjD2RVlkgTczMP7HRKEoWpUamYA7-A2GzNKAQt0JwTPzMyoy8cpnop-U5QmUnh1XOywHN43SZvCqGFZ8cJUaz5-46xALb74Lt2RKWThQEdzHaycgriH9Xm28YpNWMY_H_m0zVTzSXAPcMzFrW5SOA2FEwpQVEFjqtQsDsac9djYLp4YPfYaROYla_XZOzW6vgIUc9XUZBG8dPoam70w9VhYSc6JVCt5SW8WleP71uLBgSh8I5n8r-Gz9st9CPY05m8UdYghXq8m2OHouBGlDZf2tTiTfYbe1jqpIrTt57Gv9UMLDFaFRpWIFCGj5vXwJiM5_D378h4mI6iJnQVzQy2cqTQhC0WAlpvimEgojetOi4Cv2YAEE8X7Fpr3kHdv81Aa0Ho3MkPwuEZeTzRhup011iz45nCwPL7aF_Sxr6JDck79Xud_8VhdesOGjVFINzeLxp7uZy7-TOjUVWy7xMonHDHq13MvqFP5_u_Z-3gVKeObF1gOUyvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=AN-5mZsiD3TXq1ArFUq1BPS4yUvRqWiAT4Ubtp0Pmn4Q_wLtPsxktB5ku1p-75iVsZEZ_x4bX3wJ6Zg59_ihlCk5SBc2Fw4yXyGtRNjleq1FuO-x8VqPc8fbm0YWSVONwhh7frYIqtSsRLSekJULgbMAMGEx959ipxtOnO9EVP6SE_6ZeGOqXjD2RVlkgTczMP7HRKEoWpUamYA7-A2GzNKAQt0JwTPzMyoy8cpnop-U5QmUnh1XOywHN43SZvCqGFZ8cJUaz5-46xALb74Lt2RKWThQEdzHaycgriH9Xm28YpNWMY_H_m0zVTzSXAPcMzFrW5SOA2FEwpQVEFjqtQsDsac9djYLp4YPfYaROYla_XZOzW6vgIUc9XUZBG8dPoam70w9VhYSc6JVCt5SW8WleP71uLBgSh8I5n8r-Gz9st9CPY05m8UdYghXq8m2OHouBGlDZf2tTiTfYbe1jqpIrTt57Gv9UMLDFaFRpWIFCGj5vXwJiM5_D378h4mI6iJnQVzQy2cqTQhC0WAlpvimEgojetOi4Cv2YAEE8X7Fpr3kHdv81Aa0Ho3MkPwuEZeTzRhup011iz45nCwPL7aF_Sxr6JDck79Xud_8VhdesOGjVFINzeLxp7uZy7-TOjUVWy7xMonHDHq13MvqFP5_u_Z-3gVKeObF1gOUyvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tzwgcBrOypS7c7g6_rfo3wTIieasEEFlpLchnSjLt2Y_KL6-Meo9kxSALnGvfKgjMiQuWbZUW2eblfthWmyet79BwSalYu-OuBy2zAk0ATBvwpqaKg4p7NUwDukDKsEk1pwYwhhYKmnVcRnk3UvX5pThvqE0Mlf5IYBo9tJPLyZJ0VkEASPosjV0yIFDVK0KpnsYNeUP6TvV6scMXJDOPc4TpKUQUdi9iIYUuXMSiy6clXRzUOTAuwdToCB3HtnR92lACTonLCzVO8ll_7PNASzxy1BT8gnvAE_Fs-H80lzGkRuVtg5MP4jUvSFhTp8jO_VBXKRhoED61IxLRyqbKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tzwgcBrOypS7c7g6_rfo3wTIieasEEFlpLchnSjLt2Y_KL6-Meo9kxSALnGvfKgjMiQuWbZUW2eblfthWmyet79BwSalYu-OuBy2zAk0ATBvwpqaKg4p7NUwDukDKsEk1pwYwhhYKmnVcRnk3UvX5pThvqE0Mlf5IYBo9tJPLyZJ0VkEASPosjV0yIFDVK0KpnsYNeUP6TvV6scMXJDOPc4TpKUQUdi9iIYUuXMSiy6clXRzUOTAuwdToCB3HtnR92lACTonLCzVO8ll_7PNASzxy1BT8gnvAE_Fs-H80lzGkRuVtg5MP4jUvSFhTp8jO_VBXKRhoED61IxLRyqbKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
