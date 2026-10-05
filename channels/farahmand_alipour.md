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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 12:49:28</div>
<hr>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exz_z8cucus4Te1ywrvQMw-8YAt9YD4Hyj3FrZVp5iomK5B-5bxuCQw5QMbcNDVx1c8TrLT-n7DNS1kHow7SsNv7270r7Tw8QDhhgr3WQumjq9GVWUvrtN8VlMzicOIqyTMkGJiWdnBusBs8AbmSb-1U9VZJMXb2ZRE28UjC4QXfopxE23Xp3MKncICjf94NhDmElncHwGMO9SiFHwSzFP0zHKC7dWQtbRMD1EM-ZB85KQNZKG8h0bdN9AxdGZcW51HwfykXec5QpJjp0LFcSw2PYBNGwx-ty0nknxo1dS-OzFsp1XD2xiQEDh2F6Ak3LQP6jyLY08aXJJuDoehYSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUjY_AcGw6mGVJew1v4ystz7h45UjA7CQFItI05S8ggSL8GOW4GUYkn8Jg8thJcRd0FPkUNCCPwvIPpOxdR9ao26y3T14iH5bp32D1RabkfGJExT7dhr1u7KA--snPSI5Mfw7oXuP-dLCg_aniw-YojFC2bAUnlkG2IiN1A5H8py8GZ2YcVZ3-7uAXCzgZ97lnS2LElV-H-uwtTUpOii7Yh_ZDIyHyuilJChEIDI3NeMQUJ9cTYZPFdKdxJTnmJ9Q-cgfEjfK7v-dUNRyTDJWqdE5DF5_4fUno1ahBMn0oPraNSRQMOSHNZVfgK317Q339ZNeog3ldLuh5ckBOipeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVVoIyjXv9ZPlDB_pkDht-PG-DFJ1tYufv38pCzfo5346C9Re2zQ4tz-kSvFWW8XtI2RhFMO08QOm6a70SIH_LNLfLf8jVTwojtoRQULvVotHSgM3fZ3Xtg3_FGd6JbGFn_aPOOBgw0_Yc3vH1IJ2OPR_qYxqtgH6d0mVnIyIgbPJ3HT56dZqPhNQuyis8Gn_Csp0ffkQ8kaHhMxw9MKmevPBwMBgBJrzICYuxCEf2wMqpQqMP1Rxs1iUwi29xvxMoYTmqtohmfHwAk5-kbWecamfBtFAFA6JSubVtkuFj9GMdXtgYRgr_xtqyB-0cG506_V75M_AdoHveb2zmkVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuAfiKIbvHYyixTh-5B1UHgnpn9g2TdTcj_cIfwkcD8WaM_NhThnJgKIQpTn1Q-GYpflBjSoyqxAND0xUr2okZUlxmPiJY1IVEVJAV4eIa7dKpid8Ag1lzWp6jWeiSouALVuM2QskCHdnRSq6XK8tpYknPn256tQ-MVsDz2aH-E6VjdX2tJnGhkxIA-EtW6gnv8S7FoJPUtuATQWMUCs4kEM1FfojExvLoh0-q6JLsEuc4qFITamcjIQRPS_hBMN7gxrCadDlgjY9_Kk7CWhTtq506Rz9OVLodgVw_zAabMKU3EhyTeGpTOs2JvILdLT_99gIqSIXP3i2heRWpgTVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Th0ndbTA_qwYLyDFHI0NwMUOeKVf1lmAEZgoDyivAhOnky0kXDH7XcC6jEGNb_B2Wik3PhBCRw1ewoTLIPwg-nnRIpUiylxWfsjGNeSUcR65xpMsZZIy-St1wYGPnU-rPpxMGfOj7vzwyvYhfEgJ5tuyk-hpVl65G_k2Wvs_SYZfeSo1jgHL9q4meEXPdfEAiCllWiEj7E5ge4JDSoTqSJNCTV-mXLv9D7tWigxnTcwsCpFgcA0eQ11wHQfyOnN2OrLhIzoGjhN8OFdtNNYm5p5EhU7tOrfEn0t2is3fcR4Oo38LPFWN9PEuqXj50ZoNg44NQSKH6QY93dgvOhE2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3q7JNQJcRPoLJ3_m3l5Lld7ztXPlExwW4HRstiq6Rn1TzF1xEPj-KOZKrBUmKpkuwfOE0XFFDNs2E9W2Ot8z5fE9QMZ3O0CJvmQNoT4WGHr_9DgoTPsP8_CocCL7uk3zlvfEEe8-9-Hh9_9JNeIhA3l4_SUcncqxSjHFlUSNj4-x31OHLLU-UNhv7gudfR_bZSjU7jOsjFnzBrKFxOIA70G7iV9SG1UK-CNH1FR-6wAxPhVaFDSwLX8Qf55ocE32WmZqXEt_1om5ou88_LBXYpwWgKKG1t_xkF45pS8DH_4b5GZtA3eQW8pdaHK_lzWPnYCvF_f6nfCC0Df0uJMqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=ebiTZYkLSoPcrbI0eSvWNNWFW1WqykbNtTGtEovF_0vr9g_wJq3WXUtaBNq2un2bI9xorJ49qNXZeWX9QZ5IGgYVaNxvCF9Wwl5u6jWEAVW63M7TdRRAnEEX3utSxDn4sTlw7-tL8nvmt6kDKhuCwbX44Wz7nNaz1l8wTAJ2F-VvL265tJDs568-KgMJ3wwEb6Tm51dhYex49VBa4oQmqDFkSbNG4xs4kEuD4wll9tD80jVge21_r1_uCoaENHe-5jU5Jq-Xx4qJANDl3HNoaKBKefrUwXOMMno4HnS6rSPTVMqFcHotHPdpg1-4YD88YNAlGPPif0uzV1AGPQEFuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=ebiTZYkLSoPcrbI0eSvWNNWFW1WqykbNtTGtEovF_0vr9g_wJq3WXUtaBNq2un2bI9xorJ49qNXZeWX9QZ5IGgYVaNxvCF9Wwl5u6jWEAVW63M7TdRRAnEEX3utSxDn4sTlw7-tL8nvmt6kDKhuCwbX44Wz7nNaz1l8wTAJ2F-VvL265tJDs568-KgMJ3wwEb6Tm51dhYex49VBa4oQmqDFkSbNG4xs4kEuD4wll9tD80jVge21_r1_uCoaENHe-5jU5Jq-Xx4qJANDl3HNoaKBKefrUwXOMMno4HnS6rSPTVMqFcHotHPdpg1-4YD88YNAlGPPif0uzV1AGPQEFuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=k_T0xT6DwDit5ef2uE60k78UKUKyKTMMaKjTQejU2x6p2PFhI96mxmeiISDvg1isquMlumKA3M_1pyuehUsf1cs1LXeFSOLz4z-tihg7_Bq1sKpFFZ2tRkQfImT7PHtEbem85ZBTSSF8ZefLEtPSRe0SiSRWFD5pBUwSPlqLo-OZKdMqpPVk2wHNB6el5Lt-4QzhwVwG0wwmrxIOb3ShAsL4tEbMm-NLM3ojyHvl5ZZ5RBfthvnwUOMN76W-mYrmARhXcDkdN5gP97HTsrlMiCcXOceIALA4qyZaRBrsMDi3-T35R8wF7Uk6X5C-9aV6ZMtXqq0MpfZmbF66Tq5diw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=k_T0xT6DwDit5ef2uE60k78UKUKyKTMMaKjTQejU2x6p2PFhI96mxmeiISDvg1isquMlumKA3M_1pyuehUsf1cs1LXeFSOLz4z-tihg7_Bq1sKpFFZ2tRkQfImT7PHtEbem85ZBTSSF8ZefLEtPSRe0SiSRWFD5pBUwSPlqLo-OZKdMqpPVk2wHNB6el5Lt-4QzhwVwG0wwmrxIOb3ShAsL4tEbMm-NLM3ojyHvl5ZZ5RBfthvnwUOMN76W-mYrmARhXcDkdN5gP97HTsrlMiCcXOceIALA4qyZaRBrsMDi3-T35R8wF7Uk6X5C-9aV6ZMtXqq0MpfZmbF66Tq5diw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOWtj7RgD5yZka4PNIQgaIyQrUw6YKXlXPKQvIpSktkkJwmR6XAmz6LQ2WbYMW0VP8KoReKT-iEP7TvllIVoXwffc9Wk5biGsauc9x6OKqTo19IfqvkWf4F1mZaBsXI96Lm-4MLLYQUwHqotQN1VSRRozEN8WjUFOpQY0ZKM3c1RUHN-eWmMtXd90BTBRFRO4ZKX0j09pGeu14v_pz7HRPTTKIUgOiUD7FfwMdhgc07gb-NhAecT9T8kepSJdQ6ysJ21ksh8llkaOBOpfNv95Ld5q_Bk3YRUyNnW3bmec1hNIlG37mMHLJMFB0b9-dIwTfieM7lWlOP1H5xQlcDp-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=mQfdQdTrWDFRrRf-989LMTU__uqYEua3YlKFZMINr7tNRQyArVA-L5mRhCA0lo05EvgfcfMIxbRISJ1tRg-CS_VGSj9x8a4aMeQGUFAAxt63oNXukMzTaV-WlT-BKBaYtWYIXVTSDOnQx9KVioMtDpuylQ9NzQVso2bdaS4a0didyQfqukAjffaFF1SaIwHVnK4crsZG76ObzTEqmwEpgjYG3Y3nYH37SS90_yhhbz9Ve3NuoY_hMm4BCbwksJWI9PjT1RtnYPGYQvpgRqLyyED3Pl3hoaSlDsOZ7aSRfbuGte_86isk3TbfQfwA8o99Ph77iYMhYwz9OMVK3w78CBfccItNtkiIAtWncpksESZNYsgb0d7rsq9yIfbFOyiSlPm9SJ0_ZPKGma7bXDMLSAsu5sXBwy99RbRlhvQm27PxplcNG9TmF6xi2meX_P4I8xEXY6_-No9hqmuUNoW8FPyT26CtTuaHO8EMAT74ME4Kos0z8c1cbeccL3w7eMbis839INEEgWx7YYYKM73pbEvl9FA7yaQIs303JtQhLjusPcUySYXH1fHZIN2bq1zaW0_d5GfYNj5EzeH4ok_mNsDGf0Z-m-7wr7cStTfwwYcpZgfsfUUzGEbele5Ha375SZWJgNDhPlYbUz6bMcOFrrSiHOS3ue3HAvknGekk6zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=mQfdQdTrWDFRrRf-989LMTU__uqYEua3YlKFZMINr7tNRQyArVA-L5mRhCA0lo05EvgfcfMIxbRISJ1tRg-CS_VGSj9x8a4aMeQGUFAAxt63oNXukMzTaV-WlT-BKBaYtWYIXVTSDOnQx9KVioMtDpuylQ9NzQVso2bdaS4a0didyQfqukAjffaFF1SaIwHVnK4crsZG76ObzTEqmwEpgjYG3Y3nYH37SS90_yhhbz9Ve3NuoY_hMm4BCbwksJWI9PjT1RtnYPGYQvpgRqLyyED3Pl3hoaSlDsOZ7aSRfbuGte_86isk3TbfQfwA8o99Ph77iYMhYwz9OMVK3w78CBfccItNtkiIAtWncpksESZNYsgb0d7rsq9yIfbFOyiSlPm9SJ0_ZPKGma7bXDMLSAsu5sXBwy99RbRlhvQm27PxplcNG9TmF6xi2meX_P4I8xEXY6_-No9hqmuUNoW8FPyT26CtTuaHO8EMAT74ME4Kos0z8c1cbeccL3w7eMbis839INEEgWx7YYYKM73pbEvl9FA7yaQIs303JtQhLjusPcUySYXH1fHZIN2bq1zaW0_d5GfYNj5EzeH4ok_mNsDGf0Z-m-7wr7cStTfwwYcpZgfsfUUzGEbele5Ha375SZWJgNDhPlYbUz6bMcOFrrSiHOS3ue3HAvknGekk6zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=p81s5X116QUNKygv-3B8gBlgr4VYz3rYIPLR2lFiWh49iNeu5tudn2jPES_4CnC8ZgiDNqUdjDbPKCHRY5wrZRKhrqNW_Y8A9SElAZxdB0zLvl-9py6PQE6BZyfJVDN_sbPhf80ipgBlN1EoeTomwvN0KDBLQMRp9o6jn_fwrfeBPxDPkEk5MqBSyL1P8iNzabVeuMGP_p4KF8JImQZn5eflpYEqadl6zi1wqopRrUjsYIoCSZlA53-kAOzEnPyQMSNRPhfqMxsw2MzeIued6qzMq4NUYSB_R4pgV9mTAQL-3_vyYno5yOaVkSTcIU-O53OjmW6T9yFizMXzv7OU9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=p81s5X116QUNKygv-3B8gBlgr4VYz3rYIPLR2lFiWh49iNeu5tudn2jPES_4CnC8ZgiDNqUdjDbPKCHRY5wrZRKhrqNW_Y8A9SElAZxdB0zLvl-9py6PQE6BZyfJVDN_sbPhf80ipgBlN1EoeTomwvN0KDBLQMRp9o6jn_fwrfeBPxDPkEk5MqBSyL1P8iNzabVeuMGP_p4KF8JImQZn5eflpYEqadl6zi1wqopRrUjsYIoCSZlA53-kAOzEnPyQMSNRPhfqMxsw2MzeIued6qzMq4NUYSB_R4pgV9mTAQL-3_vyYno5yOaVkSTcIU-O53OjmW6T9yFizMXzv7OU9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnPYI0g34zSMrTkspXW-HSxiqAiPFUGHXoUYTcZ5iVOj1wbpMLX3bVFl77DrjK6ROL5i-LHPnHNqRY5ACkUv5LGoyleVDH_S1GBqOr2qcX69gKRUFXkYX8pucC3NYFycYM68oC3K7RZDhpRBTmYLIIDTpeU1_O6DLsVnNnTe3wa1390XLI5GQOtLDN1w8DnARCubS7-V9bcPiauFEYBn-UFgUFj3JhRzv-Jkw_f6GEr9SGU-XgbJFLoMalEB6fQkUk13wUgwGTzhytgGTXCEdZu7jJ7efe-RJ1unKdqzgkzFE2j847yICBgv1CVYPoJDjzA0u7LCHJzvKlY52twTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=Lm_SUXYdL5mb5wTm0P9T1tDDHeANiDd1MZ91-doY93xDasJB6P1J0NkZuTXukprsjQqtpM1x9PdISJ9T8sPtac_5ilKm5EmnQASPpxLEdP0bW87fcv5rDW-SwgNu4bvHDlZCik8q1m_dTUfPJKdBPtlxNfbm_9VyKXkHjxisZGtwL_nixsl4VeFpbI7b2cTutTw0vqOZDJtOY0gnck67KAPgSfQ2s4sLbW8SgXJnpeHpvjMQ-W46Kwkm1b-YYAhEs-ulmA8yYSt2pX6nG3qthJr0LAkYI7QB3zKzDzR_YaEDwkk1r38aJX7pQ-uHUsv-CTKhgYPruZioILdDiBXBkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=Lm_SUXYdL5mb5wTm0P9T1tDDHeANiDd1MZ91-doY93xDasJB6P1J0NkZuTXukprsjQqtpM1x9PdISJ9T8sPtac_5ilKm5EmnQASPpxLEdP0bW87fcv5rDW-SwgNu4bvHDlZCik8q1m_dTUfPJKdBPtlxNfbm_9VyKXkHjxisZGtwL_nixsl4VeFpbI7b2cTutTw0vqOZDJtOY0gnck67KAPgSfQ2s4sLbW8SgXJnpeHpvjMQ-W46Kwkm1b-YYAhEs-ulmA8yYSt2pX6nG3qthJr0LAkYI7QB3zKzDzR_YaEDwkk1r38aJX7pQ-uHUsv-CTKhgYPruZioILdDiBXBkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyZRzuC8-7gt39uakmk1zLHm2aBizNf8d2LhJwllGUt2x1QX92TszJpl5SCbUYL60tcLk4_bwiUaA4rdZWpUBqlZ5p99sfpcKho8x1QJHgvu3CB3UnuH_nSYC-HAySA51h_IgiEZU_xTW2onZ1-IPu4ze1opXhQu6m36R_YzHTJ9h8xKzD1lH-YdDxod3XrM3OyT-tvUwCz8WWjlxXnC5FEPk1kKaInwZFl-y-d7TEJiv7JGmSKs7qskmm2FywI9WVWnumyGvm8RrNbWR5IvLFE2uS_ShxJQsMmek4lJhyhxKuYj77WqT1on4wQQM3Ux_esXMOQBTmG7ZdZ6AF4nfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl85U4e4C0VPgvQ-WnnPhv8Hi1sR4cJcxktwd-1d9kk_pOTl3qOhUTB9eA21FSbeThIXPMSJKskR40vSPBSue9-yEYLRMXyW0sh3wpV2PhkKbPQL4l1Cmw-v2CAlqE_LCkBS2V9YfU_GtlnYyasaFCGLuA1Lyv132oucosczSkZfl_07R0yTN1Lxp89Jd-MqySKi-oSCRnLjX0gI2hfREy23DsgVFyFfB-kWXlVzTxhlwKpjhC0gASPrCTqemlroa20fYiu2pIatnWrEyptKfS2YFdCb5-9LpAc0dbuSoR2khJlx1mlOwspGXKe9Wj-DAq-hV24nLPvHv7HEXr1_gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=j6fwzv-_oMP2_ZQFrpkomzpxiSn2VUt5ISKXzOq2K3QHqzeX_FOEIi_WkeuRgkLnfvWc2RfYp1tLkzvuC8LX61pT15YOnQT3MFRYOYW82yPzP0iEN9iA8V-QK6Wc948wYSypYYq3pDQph8OZ1RIAzFmrPtlKBA7Hn9Ns_JntWf9uVVmCOwNd7UEnpizOWeF4qzaxQO3eN9R1FVV-zU6zBGlnCeifWwpBs0KGdQNOY03G_HYotd037TUrO3GpMwyfIVJHM10s4MjCuj8qQvybfaQifdmHnK1u9w0_nmtCe3NPzW21SC31fH7TX5qLiuwqkPOzsDuEHO9zmLbymELjw5W2CoRrUuWMWPwnMRYpj18nOngkmVfmlurMgtWn7RB0zUgrwBenbulHFntfTtlwu7XrRGZ9QCVw4IMlvRasHUyRt6I7JUO9ZlroX61fT1LI-FFYmi3ETPwNZ2J8GruNXgwuFK8UjvSIRZkoX7C6M3X3WjryWlQvc2yqZf4WommMTorg3XEjn4bt29-il_XG2UNBQWesLdkA6mUk71Zbxk9fQnXEfl4ojtWFw13KFDGPvO3TS0tkTfAk2STbLobDN7HrqHdU1vlegKPFYHzETwiZRvd7gBB3i9YkRhlEp5LrAo5DTP-ZRpSUgXwFPm5oxznLzHWlHJEmCFI3l9zBMNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=j6fwzv-_oMP2_ZQFrpkomzpxiSn2VUt5ISKXzOq2K3QHqzeX_FOEIi_WkeuRgkLnfvWc2RfYp1tLkzvuC8LX61pT15YOnQT3MFRYOYW82yPzP0iEN9iA8V-QK6Wc948wYSypYYq3pDQph8OZ1RIAzFmrPtlKBA7Hn9Ns_JntWf9uVVmCOwNd7UEnpizOWeF4qzaxQO3eN9R1FVV-zU6zBGlnCeifWwpBs0KGdQNOY03G_HYotd037TUrO3GpMwyfIVJHM10s4MjCuj8qQvybfaQifdmHnK1u9w0_nmtCe3NPzW21SC31fH7TX5qLiuwqkPOzsDuEHO9zmLbymELjw5W2CoRrUuWMWPwnMRYpj18nOngkmVfmlurMgtWn7RB0zUgrwBenbulHFntfTtlwu7XrRGZ9QCVw4IMlvRasHUyRt6I7JUO9ZlroX61fT1LI-FFYmi3ETPwNZ2J8GruNXgwuFK8UjvSIRZkoX7C6M3X3WjryWlQvc2yqZf4WommMTorg3XEjn4bt29-il_XG2UNBQWesLdkA6mUk71Zbxk9fQnXEfl4ojtWFw13KFDGPvO3TS0tkTfAk2STbLobDN7HrqHdU1vlegKPFYHzETwiZRvd7gBB3i9YkRhlEp5LrAo5DTP-ZRpSUgXwFPm5oxznLzHWlHJEmCFI3l9zBMNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRBONBJJ3wbx3f5fqLg_VzUWVuAS9SBUJN-_z905vSS1u03S-LXtEKBRkLUBjH6uhocQ-ebLBdqp7fBUC-PHruubynp44BAjseAeNyY1FE_O65ZGyinPK_CyfzbWARTg03WUjtYEw9OJAM6f5UFXPqWxjX6T9DxLhTwsdP3K88627O-V7Yb0W1T64hmOSURvXZfcXGXKLMiShaWX1o_7LhqEXIv8stUWF-75-zHkHAja32A4FhyWjZtY40JNzz5EYobRayB-jL2UAxYe6yYon7FnxdgUrHrAQYQlIcegVh17ULZn8GolBxXw7SFXwh6DJd14wHJt2ofp8nULiyPwQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmrFwmr-XsTLJK8xr5BfM27iAMCVislFuX4QgXYRAbaOShlvTbhZQYHVQRKJpfmLuDIiMMMExaxeMJgmuRhcZIRQ9zJno7p-h-u3FM_P7Glm99yXPRLuKgG36VM6i1iGh3OFCn_ie8ZQ1M7L2lLwNIZEvh2r2DoT5AKrIG8zNaQ1AGR_XFFw8W5zyP2SgclGh1XsqndpOuUAMkkAkekfAMTqJJhhuTBZ8PeFq2xwGx0WiGvCyk8_DmgAOObL-wXmMYfFrfZPfvLQ_off23l0b3c9migDvHI2oYeroj-05_dehHCREK4jAAIs5Euy2b2qTqYFs0mW5IDXc3L0e2NIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=FQKWwiqxDiv0DpFygdVkmTgdTV63YOqtDNIGZmTpdjvQyV3FomT9g8xSB6ijlcoOYU9stNnJVus1EbYDrb9XsiiGsRhy86lhgEle5BDuQw6TFZdRIAc02Yz9QeKkbDf-cdSvnxToS9t6CzoFvu5abIMsLb9uysXkBYsDWF5dG8ce2h-OfjDHEvX7I5vhY9metuNYitdElCqEJ6-_hWzU8d7FP4L0HF8yuAzFxpevb0xJRCH4gj1LHVwkkXrpkQiOFVVzUgP1GBcdKaQg3DSEaEEEdqT1lMp2FEMEDqjKVykLYMtuA-r7CON4eW4RYSFHYicZpBTpO2xu85E7-qbH4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=FQKWwiqxDiv0DpFygdVkmTgdTV63YOqtDNIGZmTpdjvQyV3FomT9g8xSB6ijlcoOYU9stNnJVus1EbYDrb9XsiiGsRhy86lhgEle5BDuQw6TFZdRIAc02Yz9QeKkbDf-cdSvnxToS9t6CzoFvu5abIMsLb9uysXkBYsDWF5dG8ce2h-OfjDHEvX7I5vhY9metuNYitdElCqEJ6-_hWzU8d7FP4L0HF8yuAzFxpevb0xJRCH4gj1LHVwkkXrpkQiOFVVzUgP1GBcdKaQg3DSEaEEEdqT1lMp2FEMEDqjKVykLYMtuA-r7CON4eW4RYSFHYicZpBTpO2xu85E7-qbH4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=XYR0hE_a-YztWgZo2rU6lCZFUxinIIka7QiYn6s9tcPg50okUNzooeLbU9KDN1KkqgaxmN8RC_dABMvgMG7olSh68hPyiPu4o0OueOl55ymrFx6LSDTfwLYWDOS6bNLDIWZV15sjfVuTKz5KEDs8mxmrGeI03LRESc_pwxwNTywDGf33Vsc8sT3sDdTUqozDX65Q85q5OkWRK5o4EMgisufs4F283JmrJsBj9GBWb8_0_1Cy0YrHEYa6Oz0zDvnMRTs_aZ2eJAn_P-EyjSVEoo1J4yAvqSgaeAYgzY5pdJgAysvlp3Iq9t4gGbboUnM_iygGnzOZ346lEFStVIAGcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=XYR0hE_a-YztWgZo2rU6lCZFUxinIIka7QiYn6s9tcPg50okUNzooeLbU9KDN1KkqgaxmN8RC_dABMvgMG7olSh68hPyiPu4o0OueOl55ymrFx6LSDTfwLYWDOS6bNLDIWZV15sjfVuTKz5KEDs8mxmrGeI03LRESc_pwxwNTywDGf33Vsc8sT3sDdTUqozDX65Q85q5OkWRK5o4EMgisufs4F283JmrJsBj9GBWb8_0_1Cy0YrHEYa6Oz0zDvnMRTs_aZ2eJAn_P-EyjSVEoo1J4yAvqSgaeAYgzY5pdJgAysvlp3Iq9t4gGbboUnM_iygGnzOZ346lEFStVIAGcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=AUAdpMAzvTqbHY_VaHqF3mixL77pFqEAZySLCGTAODYrDgcC0p7tg3i07CJrIKJ-S4BaeCYqCUsxMiISRyBEC9vgQ4t0YXmIc_ij4Pk0l_CkoCgUbrQGzDZVJHZC0fjYttXkVlzM4iNZxJsBJKaYOYSl4_zy8c5McRR3m0R8kVV2sTeyMJXbmcB8aM1DqKPRljl8BqSdEuZ2nBmdNVu-dotjSBUsyXf5Bp-35zEqSMIqWIiGPz-gcSRDH89hNyXtwNaJQBGs5i0Bc7bsrV84b-4Ocd7LzYACDE-q5Atscp75O-T02iZYCEjIt4dzgMV3hQYTy_KpDYEBlVWMhQnYCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=AUAdpMAzvTqbHY_VaHqF3mixL77pFqEAZySLCGTAODYrDgcC0p7tg3i07CJrIKJ-S4BaeCYqCUsxMiISRyBEC9vgQ4t0YXmIc_ij4Pk0l_CkoCgUbrQGzDZVJHZC0fjYttXkVlzM4iNZxJsBJKaYOYSl4_zy8c5McRR3m0R8kVV2sTeyMJXbmcB8aM1DqKPRljl8BqSdEuZ2nBmdNVu-dotjSBUsyXf5Bp-35zEqSMIqWIiGPz-gcSRDH89hNyXtwNaJQBGs5i0Bc7bsrV84b-4Ocd7LzYACDE-q5Atscp75O-T02iZYCEjIt4dzgMV3hQYTy_KpDYEBlVWMhQnYCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUifC24IvNshZdzX51nSNAZUxT7Afy8GcYbI9e2KEJXkQb7zPHdscLQWP2e-rcnhd5kSYzBiTG7ZUwwk9wirf32S4YbVbCIXIZYMS9WWelWRl4MV87HF4mc8di7rRJ2nPR3lPY5F2vDCKwmlH5zEUPsjnGk6_R0xXb2yAsisGJMLavhMJEIpi__N5v_0MwKjV2vkCFD8Fi33fyYAqqeJuzBHyRTbpB2EfLGR82z4WaYo5ohEzCrPn9ZOwcUGwzxeyYJPBalFbwL7TIRHfGe66U_KBMei-KpN1VG-d5jI7yOXVYGufa9nvnZYvol2XnNABqQ6H5SWMesciYQwYjvYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8KK2h-hEEUoGA2s416n0IP_J9H13PvQrkHNjb6wlnVLamyaS5rRETpSbBoUEOS6TfcQZYkHbqgUMy8x41mpm58Wg2ExEoUWR8pY0TMCZiKf2uh0Tqj7FB0kKDs5De_JHX6voEM-eyCBIhWtmXd-PBa8yCAurBMSVaY6T4sP_Hq7XE9quv5B7MPihaSJjy0GiWJGsAOJwnypnMMLjYDwSjcB7ixWSXrNun3T5helZ9n2r3CqZqYNm1favsGp3HQFWflilslmABN-4WWoeaW3F408EV9AuS-fnar9xUcmf822alCxW8lcfOJ2jy_jOAtKQmykTxXmCDwtsZl16mMe_VVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8KK2h-hEEUoGA2s416n0IP_J9H13PvQrkHNjb6wlnVLamyaS5rRETpSbBoUEOS6TfcQZYkHbqgUMy8x41mpm58Wg2ExEoUWR8pY0TMCZiKf2uh0Tqj7FB0kKDs5De_JHX6voEM-eyCBIhWtmXd-PBa8yCAurBMSVaY6T4sP_Hq7XE9quv5B7MPihaSJjy0GiWJGsAOJwnypnMMLjYDwSjcB7ixWSXrNun3T5helZ9n2r3CqZqYNm1favsGp3HQFWflilslmABN-4WWoeaW3F408EV9AuS-fnar9xUcmf822alCxW8lcfOJ2jy_jOAtKQmykTxXmCDwtsZl16mMe_VVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=H_0q3Y2zrHYlGnibRiOE35Th4fbcnMLqWyHpFe22sK6ZFbXOXDRm0oQpQwQrukTpaLPwXivlFPvlYoLzcD2ivGJJakT3MYwHV24NS-ht2nsR_w-x07Fvqua1KopZufOZXYOMPrWaErjXfooAfDb2as4xdq2oQFIi0tzqZRQP_3i4bP-K8Hgq8vC-nnnvOoVOOLvSTGYEY3FBUWy_kLMF1K5W0xLVivbUcUQG0i4ber3wlpM9awsRC88ojURau2xW1BIacWKdIz4BSC1-TIfKWvGBMjytmHynH1hlDThFpoC3Fdsp6CnXhFy388BpExid-YTi6ytbb8Lm4srsNI_TBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=H_0q3Y2zrHYlGnibRiOE35Th4fbcnMLqWyHpFe22sK6ZFbXOXDRm0oQpQwQrukTpaLPwXivlFPvlYoLzcD2ivGJJakT3MYwHV24NS-ht2nsR_w-x07Fvqua1KopZufOZXYOMPrWaErjXfooAfDb2as4xdq2oQFIi0tzqZRQP_3i4bP-K8Hgq8vC-nnnvOoVOOLvSTGYEY3FBUWy_kLMF1K5W0xLVivbUcUQG0i4ber3wlpM9awsRC88ojURau2xW1BIacWKdIz4BSC1-TIfKWvGBMjytmHynH1hlDThFpoC3Fdsp6CnXhFy388BpExid-YTi6ytbb8Lm4srsNI_TBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STjX2rerBqCX9lWvd7Ga4OnQAhGm3c0R0rIIF7jtLxbtpHTcUA1WA3DjmtYHGpYyB7Re1RkQ3bOcICNphbjiNMSwHOQKT4rD4SeeXwHKhq5TghfMfjpASbXQXkM0LePmXPetDUoxnPnAo83052XoSf-aMg-2X4pnN6sidbT2d0zSv-T9UQw2EZZUickm1yueZp9LEE4EEQHgqJwKJS0UgdHQ8so9VFtg3X_68VYISqoV_do9mpl672Z4wmRfY-aepMzZdnaSU0VahRtQ4927XCPTGQklgKu_gX_U7nAt637UFWTXSgdUxFRB7SxFBDNXbaoWOCLkIw6ekaH91VH29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=MXy4jekKQ8-3tcAYBi86rqPp0kB7l7WG3XsVMy_qOXyauUoFT7lTwjYWIUOO_sU2Z07oVRRcKX0l5FXRzsDZiKx_Kw0FePBehC1m58dXLuDRofOoqMeSApEXlCttTh5n3lNSmYJxI9heCJsUcQKOwsjDb5DI7Rn2t9eqswvxvDBJVlEQASD3ia4LRzPKngbWju3DFVBxrtAUE3ufS_KICzd1373fhcDK8POHf3HfBZiSvChAmylGDOyd5Sx5B7A17_SIESSlfQFzNQxIKxf_zDHfZFJDPZOsX_GhE9pYcApXl-2AclO_lG0gIp-2Q8wRe4syUwATVpnUvNCNT-heKhNEmGm9RpoYCoRzq5Fu3Pi_XjdVDsLbWmwXbeXNjqeSnsYeLfYoHjrszgnnc-xweRF2JwGFKtasN1GcqnyUIu5-GSBNrm_ZA7f5lp12A2otIQ_GG3IfiGcfLzJxiKsYa1K73SfzbhP8Mky6-JVNPCBebhvNbfy9hJ58qAdZjl36Egkr0i8orqcINGE4kzAcCELqCT3ZGgyI-PQW0oao7DsU8SvxNuJeIGOPsqMUHVrUPAbOXtsnb2_shsO1LyLIJ7eKd-Jpr9F-pNfwNQQdi2L45AdIZDBIElHOFKRPaf2jWVdFOikqvMqTpk_tu3ezhwPL5hsTdGZBD96WW_MywPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=MXy4jekKQ8-3tcAYBi86rqPp0kB7l7WG3XsVMy_qOXyauUoFT7lTwjYWIUOO_sU2Z07oVRRcKX0l5FXRzsDZiKx_Kw0FePBehC1m58dXLuDRofOoqMeSApEXlCttTh5n3lNSmYJxI9heCJsUcQKOwsjDb5DI7Rn2t9eqswvxvDBJVlEQASD3ia4LRzPKngbWju3DFVBxrtAUE3ufS_KICzd1373fhcDK8POHf3HfBZiSvChAmylGDOyd5Sx5B7A17_SIESSlfQFzNQxIKxf_zDHfZFJDPZOsX_GhE9pYcApXl-2AclO_lG0gIp-2Q8wRe4syUwATVpnUvNCNT-heKhNEmGm9RpoYCoRzq5Fu3Pi_XjdVDsLbWmwXbeXNjqeSnsYeLfYoHjrszgnnc-xweRF2JwGFKtasN1GcqnyUIu5-GSBNrm_ZA7f5lp12A2otIQ_GG3IfiGcfLzJxiKsYa1K73SfzbhP8Mky6-JVNPCBebhvNbfy9hJ58qAdZjl36Egkr0i8orqcINGE4kzAcCELqCT3ZGgyI-PQW0oao7DsU8SvxNuJeIGOPsqMUHVrUPAbOXtsnb2_shsO1LyLIJ7eKd-Jpr9F-pNfwNQQdi2L45AdIZDBIElHOFKRPaf2jWVdFOikqvMqTpk_tu3ezhwPL5hsTdGZBD96WW_MywPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8bKHzoJmUk823C5dWLoW6FraqBThjG9hkkk2I1bNfaAE26wPkpAzKflFjsLl7Hvd8Dpi1NYIqYZ4OuMeWbrYEhISoVRVpTvOgc5P0WoXWdi3GhM7ab91JwGOL7iLWKifh-uv9ItQqXc66CepjxqjcTTCjgJlVHKhDKuyb1APUYzApxYAXTiMEZvmTrsuHRBEYWHyST-mL9kBRL8-_ZEnPmVNLGx7uSR19xeA6XopX9u46ehj5VPr17l06S4RSviKR-_p0snKpIWAGToTRL_mmk02A515h5teznWSORWO0AYvnzmQII5NoYCv5tqfxnNAvomhsb3RLmR6wO5o9M3kA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=BOBUKfk9Yn5nYqeYue7Otos2g3w-QEAzuqdFEhAx1XSXPE2dxDKJImkjjlzTFkIVU0kYunhB-s554v1NfDCiJqjUyKdPMhYSLqI8ZFb4cJjNOZVW8VqhoVTJJIwpThA5jpz3hVaWyAkmprCEJd1KBK6vwok09--RF4mtFOEaiCVpTJYiTWZFyVCH0G7JHIPQbcp_2T9VjRq5z8V2p1H4P3zlQRXCwTGJtzgXXPQYNPrFaXaRdPgJH_ipBrT2OJ-qtb2cBYfseJ0zeuhLoxd3u10GXvd2C4vjRyB1-_Fx5FZmuDt_BVoap8zqqPlBqomM_a55No-zkk4n76REIsNx8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=BOBUKfk9Yn5nYqeYue7Otos2g3w-QEAzuqdFEhAx1XSXPE2dxDKJImkjjlzTFkIVU0kYunhB-s554v1NfDCiJqjUyKdPMhYSLqI8ZFb4cJjNOZVW8VqhoVTJJIwpThA5jpz3hVaWyAkmprCEJd1KBK6vwok09--RF4mtFOEaiCVpTJYiTWZFyVCH0G7JHIPQbcp_2T9VjRq5z8V2p1H4P3zlQRXCwTGJtzgXXPQYNPrFaXaRdPgJH_ipBrT2OJ-qtb2cBYfseJ0zeuhLoxd3u10GXvd2C4vjRyB1-_Fx5FZmuDt_BVoap8zqqPlBqomM_a55No-zkk4n76REIsNx8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrPkStE-CdX7nhG8wjfuBcsAYsurNaLNwPwjApnX7Qto1_hnfuVErBi5juNA-gVgN9Sz5pNuDmU2tISfgGvA-V8--3n177JaeqyUxpNPO5tjxUwk1de-4MKkIwVY9FH7R3t3k9uPbW3KQdxRQEJFosnykR-L98lv8C8fUJTB0bjEaRMYzTVKOTjROBWfVvFXkvKUzS-MJqZHYc0jG-txj3cMsl2e98BnN3rtXsqSIQoXnIybMcoM8f6oDnTjCYrxMfK8fJQppL_hmXPWpPs44Rr-O3fwRqaOJeYgMYZZXeGRaAoIZAyqIb2gy8T6aXVdMxWEAvPden3as8KepRQ1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cpxp_juajZo_VS4bqAIuyXRp7PZP3NCXQSuHbGvWKmcltT_4q7AU_PxJ1n50arBgBEncwmJOaY5FISISmS66UI6pcxxHr20JSJLOaGJcT_heQy3KM2lc30Iv6m6g-dRhm4mPJ4H4iXvLCwHSM-bbSEEnAYM8OR0z11NogE-ELn69uuZxpjZAJK_owUNGV-zCTdRTAO-Z1Oa5rpMayaCYfZ43awq7twa5cGI7YLMzwBEEIAWtbHsk2NtBN75T8-bXgT_DKVQypm5TjwaVcgDY4pOBv-gTqzJv4dkCk9OEuuh8WB32Emgde_bUljdjXwqML16wG__48O2Y3bu9dsxLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjiIivTLJF4sHanj1i21PwIN3FbNnIQXbTtQ7gAH9FJV2GbLrK4JQ-Ab6OVf22EsQrsq6VNg9omZuAEes40KgcKkuygjrY_GgeHe6sypz9S6ATKZCqvUo6dJpQim7u-ttD7RycVZ_KIlLoFJAZbApMz-MNo7pulCtfjK8rzDTrxsuEh2L-70LB9iKlBGTRGR9PMnaMgQ7J02h_-LbA6s-_59PpICotr5NGsmeqqsQHgSbQ8cKTQmBpo5jvdmv7GHF3iZLr5CQXwqu9pUxkqdRwyBcAGJHPzeqW7CrU3TExs26DwGTW9YNwAsKnUL_VdBfWdDjiNazkvdxCfJNq6Now.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=nFvazvMOntlCekIDtpa03UyXj6fJY3Qby7X2wWZFc0HXHp_6QwfWolAemqWz5H4u52cbdReAhGrsnotQOMLbusYnewiP0tmEzvBC0Ov3OslUiYv2388dTd4onySzjXX5i3uN0ZhETIkd2cPxugGHqG_zDR6sgNvsH5Zryft2quQajuKqt8u0mQcJ2abS97Skn9gCkC2V6KCMsi9cV-dU2mvDIym2lq7y8XMYOaQg0U9FP4Y4VGXT1uD78NMTRbRrEZ9ODE1LtPpVzYNjYwNEoPlpWBouqZ9jHqdGzmuhVWPH5rOq0mUm03ZhYQbEqoYJvZBafFVLx8MX2-OIykYJTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=nFvazvMOntlCekIDtpa03UyXj6fJY3Qby7X2wWZFc0HXHp_6QwfWolAemqWz5H4u52cbdReAhGrsnotQOMLbusYnewiP0tmEzvBC0Ov3OslUiYv2388dTd4onySzjXX5i3uN0ZhETIkd2cPxugGHqG_zDR6sgNvsH5Zryft2quQajuKqt8u0mQcJ2abS97Skn9gCkC2V6KCMsi9cV-dU2mvDIym2lq7y8XMYOaQg0U9FP4Y4VGXT1uD78NMTRbRrEZ9ODE1LtPpVzYNjYwNEoPlpWBouqZ9jHqdGzmuhVWPH5rOq0mUm03ZhYQbEqoYJvZBafFVLx8MX2-OIykYJTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbmdzNjcV76XiaMtrprZ9Ulyd1i5fETinxr7KbbMmISY3O5vcgbrIansLJyF9EVp82blqyxAYi-Apqp6RVt38VBSYLpFar-TBiioTHoiCgdLTZwcoS72rRsHPJupUV0VkjvwGMwHZ5XjFh-4dgHXMum-UYPuegFcMjKFoV4m8thkFMOb_uSpApVK5PMW7WojQsQuIIPFxtcLGPU6LoiMDUt2Gw4T5C0tCtDpp0pQuix8aaUwBnJqExzjgZImXOr8P5ki0pr8jDFlpK1W_3pz1rpZZ7okxdPJWW9IxQp_hWfYGzlqCCCA7hYj_w_hn_Nn5XRSBIx483LcRmTyIIviKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuznGc-SH7r2YAgb-svSZSUZ4_CknOSO4yB7GaQzvolhtD_mEsuQ7cxlGMeeYuyAk6SmY9Z9erVDMUE55PiW9iHWL2zmLsB1A3zTCAjJjjarwB3flrtF0KU9RxHGwB-qi8DghA2_0Ux6iJDJDaxWiNof0z9X5EuHuQVzKkwRDQN8XA0mZ87uv302VGrANgpaEYZoV4uoJEfdUmqgic_8vznkMvq8zIX7dOKnWh6Q5ls4ZGLnmyB_sm2qCuflt6Z-GN94J5bhVyIehjs6eweiS010jIoNgfLnqH-a0JOd6dzRrEzxYZ54WHvM2C0rF32uNI2w9v9Qe7EMtVPE8xQIEvbM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuznGc-SH7r2YAgb-svSZSUZ4_CknOSO4yB7GaQzvolhtD_mEsuQ7cxlGMeeYuyAk6SmY9Z9erVDMUE55PiW9iHWL2zmLsB1A3zTCAjJjjarwB3flrtF0KU9RxHGwB-qi8DghA2_0Ux6iJDJDaxWiNof0z9X5EuHuQVzKkwRDQN8XA0mZ87uv302VGrANgpaEYZoV4uoJEfdUmqgic_8vznkMvq8zIX7dOKnWh6Q5ls4ZGLnmyB_sm2qCuflt6Z-GN94J5bhVyIehjs6eweiS010jIoNgfLnqH-a0JOd6dzRrEzxYZ54WHvM2C0rF32uNI2w9v9Qe7EMtVPE8xQIEvbM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Gt-U-3EwTp8KinO-22mwTtid6JfhKbxzfKp4mqjx8Ru8xQS7UJ4ZpEDSOPo09-60yNsf1JdWL4yvk39Qe-if2_CRxGPeYDJ2Ka4t1zA3y1SeqM0iQF2e6YlwNFPBadNIoJ6j2y9l5cHU5NImmavJrAkmeqA5g3CNzFtNsWd9YDUlrciha5ddD3oOIz-Uh_1OqHg-4vhlGOzeF7eOPm7P0mFPnhXv5QRHpWbRm-7Vh5HUItOHyFPSjea8nk4Fh6zzsp3E4nVFVEY49khwVIOMW156liyq0jLdgq6_p8PK3LhGix-q_yAJ8MjNviCfqkd6OXQYHACPIKyctmnSZj2gmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=Gt-U-3EwTp8KinO-22mwTtid6JfhKbxzfKp4mqjx8Ru8xQS7UJ4ZpEDSOPo09-60yNsf1JdWL4yvk39Qe-if2_CRxGPeYDJ2Ka4t1zA3y1SeqM0iQF2e6YlwNFPBadNIoJ6j2y9l5cHU5NImmavJrAkmeqA5g3CNzFtNsWd9YDUlrciha5ddD3oOIz-Uh_1OqHg-4vhlGOzeF7eOPm7P0mFPnhXv5QRHpWbRm-7Vh5HUItOHyFPSjea8nk4Fh6zzsp3E4nVFVEY49khwVIOMW156liyq0jLdgq6_p8PK3LhGix-q_yAJ8MjNviCfqkd6OXQYHACPIKyctmnSZj2gmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=WoaWjYSvr7hgBM8MYXZ4PEIK58WAZKr7emfJoKiffDBxyadJxy3V2WKJaensn4X9OgQGjuaexvfklSSc7H4Ob8dvcKV69MY10ImOKm4ZbdK-ciSt9a_19oAPQT91tkiQrZXTa0Z_0m92ADLBCRF7M_bWmvR1SjpklNXjCLCQc1CUK_wsIgaLWhayYErQHKzPUbSEi-cMpUcDMN0029TF0L6JLPhkFHE7I-H-jgZt31Izk7KASx3I3v_HnFywOBvGKGTKZW0d4TV621K6Oy6f2e3CK3a7kWyL33An5RdVsFXYc71NDwRGtTY4Clbirj4kFbtyX6oy0KiP85Ycg1x1TXZOM1Ty5XIbuWoTEcTieJ2xQ8aKu1LO5CLpU24a9O0e77GsMnHD0XtGeBycx8jI1W3yA22ULgtki0R0kvPNThBdbyaVude7x462FjMAXsa1uYkOWGAtGoYK51JdV4SSYxaJ-p-9z_B55uQFN7lMvg4nx3tTRBkQZXrUjuaP5TptzLYi6G-OX2eGXTKDMK9ZcW3ACX-5Vn2YsvokhJX-NuIR9c5-O4ONz9jfpr2d4sdqmRtsoKFQSHxrBKMgJ2B_4EvMiZG_-OQK3Ax34J8bku68-IUBHgyOWQWdeN7sZaFEMrBnXSP07SISAk-GCSqe2JWXTRXSACmk4OIL2aRp1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=WoaWjYSvr7hgBM8MYXZ4PEIK58WAZKr7emfJoKiffDBxyadJxy3V2WKJaensn4X9OgQGjuaexvfklSSc7H4Ob8dvcKV69MY10ImOKm4ZbdK-ciSt9a_19oAPQT91tkiQrZXTa0Z_0m92ADLBCRF7M_bWmvR1SjpklNXjCLCQc1CUK_wsIgaLWhayYErQHKzPUbSEi-cMpUcDMN0029TF0L6JLPhkFHE7I-H-jgZt31Izk7KASx3I3v_HnFywOBvGKGTKZW0d4TV621K6Oy6f2e3CK3a7kWyL33An5RdVsFXYc71NDwRGtTY4Clbirj4kFbtyX6oy0KiP85Ycg1x1TXZOM1Ty5XIbuWoTEcTieJ2xQ8aKu1LO5CLpU24a9O0e77GsMnHD0XtGeBycx8jI1W3yA22ULgtki0R0kvPNThBdbyaVude7x462FjMAXsa1uYkOWGAtGoYK51JdV4SSYxaJ-p-9z_B55uQFN7lMvg4nx3tTRBkQZXrUjuaP5TptzLYi6G-OX2eGXTKDMK9ZcW3ACX-5Vn2YsvokhJX-NuIR9c5-O4ONz9jfpr2d4sdqmRtsoKFQSHxrBKMgJ2B_4EvMiZG_-OQK3Ax34J8bku68-IUBHgyOWQWdeN7sZaFEMrBnXSP07SISAk-GCSqe2JWXTRXSACmk4OIL2aRp1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=bu17bok66QT19hlLBxavNKSndo94JiNb7Ooo6ySNnH2DtUUpJ0OlzBjSszLuVosWS81Mu8I7P-zw-wqyL0wuYJ9ff3c9I6mnN4NUKSva0cAL6Fwf5mBFE8k3OGjFocI6iNpsd5O6TDZqvG6Yew5zRCZ4gYJG2WX76IbZl-uK92a7isdyuKDgcXE23sAtOKrCFaLfaZ_STDvmcBdSFBXU2f1V30SgwRg9DA1U3PQGBa7eZFsk-oaW2pINtWp_GcHwTlOmtIGAKe1Znr3KdQP4ZLmaOIQB9XIElJETcKiHQP19-fSWz99rhJk_7kfv5O6tRTIazKsb8XdLEY3HSE3M2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=bu17bok66QT19hlLBxavNKSndo94JiNb7Ooo6ySNnH2DtUUpJ0OlzBjSszLuVosWS81Mu8I7P-zw-wqyL0wuYJ9ff3c9I6mnN4NUKSva0cAL6Fwf5mBFE8k3OGjFocI6iNpsd5O6TDZqvG6Yew5zRCZ4gYJG2WX76IbZl-uK92a7isdyuKDgcXE23sAtOKrCFaLfaZ_STDvmcBdSFBXU2f1V30SgwRg9DA1U3PQGBa7eZFsk-oaW2pINtWp_GcHwTlOmtIGAKe1Znr3KdQP4ZLmaOIQB9XIElJETcKiHQP19-fSWz99rhJk_7kfv5O6tRTIazKsb8XdLEY3HSE3M2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL5xScehMFNzoja5HEdurRJXsqJsk-cDO5rxEQjS0ii3X1aRC7-Up5SnsdUB-M-7a2bYYY2oPMoLcpucJg8U1snsWH8fHqEs9SB_JVPgW4BI41jBAbYFquHXIbkBZbfUVa-hAI-mhqxsXq9MWqbnG7Xq_gnClBgWNLLKmRAN2WW2LkqGjA7eBdXG2ElfwYeeC8NndWXoo0kU-IqNMuo8ScLLVTGpOYdfd3dARA_iTRrMA-plOf-hc5VA4VbT2xkMwm5SbJpviH7suoO9thyeHIMUw5hKyK1CiThyn6dQj1u5wwAy77G4PBdptqZNxjPVR8RaegVqQbUumnQjJod0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=JrEXgtPydNFxmKZIJUQLN_9EfOSxoDW2GJuvr_NR51D84yRQvEqQ2h1w449oFjJFuq-pE6SLu3f2DM5AF5FKPbkfIAzKuk8UpExauSFPBLo9dlJMZ-cCwBISvZRAcNnUlNMJejxPkK95OrDnhPipqxuRi-u5IVvsjclJi2KscnMbnnpyBP97u6wKo8XPDETg_d1lXoQ-xww7_fOjm3vragcIrTfQzl1RHKfHFkRh9bmYBbk61ntFD6sqWhPTQDOB_NBBW3JJ_edWI_DjuFe-xIMnu3k2SuVQiqZPXh9XdMvoYteu_HVVs9k4vgDGk9vbjUA_EkjUtiiK4rsagglQeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=JrEXgtPydNFxmKZIJUQLN_9EfOSxoDW2GJuvr_NR51D84yRQvEqQ2h1w449oFjJFuq-pE6SLu3f2DM5AF5FKPbkfIAzKuk8UpExauSFPBLo9dlJMZ-cCwBISvZRAcNnUlNMJejxPkK95OrDnhPipqxuRi-u5IVvsjclJi2KscnMbnnpyBP97u6wKo8XPDETg_d1lXoQ-xww7_fOjm3vragcIrTfQzl1RHKfHFkRh9bmYBbk61ntFD6sqWhPTQDOB_NBBW3JJ_edWI_DjuFe-xIMnu3k2SuVQiqZPXh9XdMvoYteu_HVVs9k4vgDGk9vbjUA_EkjUtiiK4rsagglQeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=HcwhB7pulVbGFVf99Zo1lxt-z_TkTvr5zyIkpks9PS_HT4DduNWeohqdZyQjbDVQ6NuF4JH9aR85wpCXaRKiH_rdLiVGsLtFHHNjcx11WOWej-sRsyZdT0ysLUx5QdKPzb_pCJOttRrsNA3qpqzQnGqyo9usQy1m9fHODwHWXEFCz4vcrWKrNQCYWoUWNfp3BZ7io86zQPJqYRiTzH0rfGsJ4C2acoSBpQVEaFXgCOf6gcGCCNIpd0mJZZovZ1MhFfdSPlWqjGo0_y6JH_clAvaXXJdm9GLJh3-KDj7pOTtK3m4YLL9WugwIAOnxFzFOAOTIf1tNBA1y--UvvzHDmoQ-O6jWkFlyaEe0xHEWiL0XrzX_XU8WsABzuIOxqG3XwMHrw-5AnPgsZ2Iv4Putd3l1e-kt5rXUVs9Ml7Y1xA0Chk8G_-s_JUhMHt3FSjwVsrcMgZMYTPK_9EtCqnQ3KDeY1OkfwfVl1OCB8ReEgxHQAHV9Y1FuUsE_U9jiX9bCj_ieQRrq7wwmxSgv4O3vFeOuy1rQL6z_u1yFt9Hr8mCkFuGW9pCqI3RD6pbZMRw2k606dmpAVz0KjKU72CfDd0uitKEiCoaP8E-0XaENBXWvxy77aAR_HKdPACnIPeDPTei3U9YCLwvAJiqfq68sHb24c5_hYA2qxXvn8afKXGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=HcwhB7pulVbGFVf99Zo1lxt-z_TkTvr5zyIkpks9PS_HT4DduNWeohqdZyQjbDVQ6NuF4JH9aR85wpCXaRKiH_rdLiVGsLtFHHNjcx11WOWej-sRsyZdT0ysLUx5QdKPzb_pCJOttRrsNA3qpqzQnGqyo9usQy1m9fHODwHWXEFCz4vcrWKrNQCYWoUWNfp3BZ7io86zQPJqYRiTzH0rfGsJ4C2acoSBpQVEaFXgCOf6gcGCCNIpd0mJZZovZ1MhFfdSPlWqjGo0_y6JH_clAvaXXJdm9GLJh3-KDj7pOTtK3m4YLL9WugwIAOnxFzFOAOTIf1tNBA1y--UvvzHDmoQ-O6jWkFlyaEe0xHEWiL0XrzX_XU8WsABzuIOxqG3XwMHrw-5AnPgsZ2Iv4Putd3l1e-kt5rXUVs9Ml7Y1xA0Chk8G_-s_JUhMHt3FSjwVsrcMgZMYTPK_9EtCqnQ3KDeY1OkfwfVl1OCB8ReEgxHQAHV9Y1FuUsE_U9jiX9bCj_ieQRrq7wwmxSgv4O3vFeOuy1rQL6z_u1yFt9Hr8mCkFuGW9pCqI3RD6pbZMRw2k606dmpAVz0KjKU72CfDd0uitKEiCoaP8E-0XaENBXWvxy77aAR_HKdPACnIPeDPTei3U9YCLwvAJiqfq68sHb24c5_hYA2qxXvn8afKXGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2nnL4WrRxdGPBn__jB6KyiFw8zAi9dQTmkIfeNuRF6yJx-iODnV0zn_BVgz-4iNDXf1iPOoL7XBH2jQtU_8UpkGtu74R44XyKd5g5UEey2Gg627orKFKidipCrQg_cdxn2Fhyj9Vk2L1gIzQFvx5h1Gz1Or7e7IRUJaZLXI0rcnBVVhz35vvHJmb30HG6tzs8wQf2v5RNRL8kMVDkjCzWZ4iFMwxuHmfIG6sO70TkFY4FEXnWbQkHZACNTLAGOHdym7QOIOg_S3ikYfa320hBy11aKbk7zsm0Hf6rvcvknoZxmXZ8N0qy9aXULmK4MSZHAS-dg85oP3i6srYLA4Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=jiF4ySV5P6SKb9pfXe1ZoGv6ElB0HSXaN3iCeQJ76-yTG7RZRnwQ3SzdVIf1B4ORnIO0aiv1LsM39Y7YUd0TKcWhwCymJSY7UNaPT9g1u59hLZieNxDlS_VcjkrYd5ftZSWRJ986idRDVi1jFE4bxADIx8T_EVwADceicGgvFRHgcN1Ja4sQeSOvSCFRcBOxqD4-e5wnRHtfpyIhugK7msz__E2brDpS5XBzE5ZxNhGGkcVEvuAr7XTsav6oDyqC51iQQlJDZDhc2QWG2yD_tG7fTMS5vLa1UUicQfw6hCUpfJzltp_RCa79P57UCdOuNoAsqQUSDEwuJa4r_jUBTSp3dXCqLJwiMGiqQoTHY9IchZAMWZbqiRRPVXOlxheIRILuF8jKVI9Po_66LxWdc9dfnfFHtkrSzA2K1X18VkQkiiJShH0i-wYyPfHDK9W4DIxUX5FSjjofGqj4wIQ0TTVEIbXXPXQ2ObTVL9Fl-MKklKKupdVwcv_gdvfVHWcASVTb26GGcTViiNd5p5PP_J5vX0WHmbd8SGUWIw2a6d80Zmg2bxTFqvymRCfxrAukqCKBl0mTvqOtBGqT1rkQZRxUUSyvdLVYs5D-A7Q6NrE_F2ZDPChkgfBg0pigZGIcDjhqP7I_StgHxyGI3k9EC4TP_8V7OoYpaQQZTCC3yyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=jiF4ySV5P6SKb9pfXe1ZoGv6ElB0HSXaN3iCeQJ76-yTG7RZRnwQ3SzdVIf1B4ORnIO0aiv1LsM39Y7YUd0TKcWhwCymJSY7UNaPT9g1u59hLZieNxDlS_VcjkrYd5ftZSWRJ986idRDVi1jFE4bxADIx8T_EVwADceicGgvFRHgcN1Ja4sQeSOvSCFRcBOxqD4-e5wnRHtfpyIhugK7msz__E2brDpS5XBzE5ZxNhGGkcVEvuAr7XTsav6oDyqC51iQQlJDZDhc2QWG2yD_tG7fTMS5vLa1UUicQfw6hCUpfJzltp_RCa79P57UCdOuNoAsqQUSDEwuJa4r_jUBTSp3dXCqLJwiMGiqQoTHY9IchZAMWZbqiRRPVXOlxheIRILuF8jKVI9Po_66LxWdc9dfnfFHtkrSzA2K1X18VkQkiiJShH0i-wYyPfHDK9W4DIxUX5FSjjofGqj4wIQ0TTVEIbXXPXQ2ObTVL9Fl-MKklKKupdVwcv_gdvfVHWcASVTb26GGcTViiNd5p5PP_J5vX0WHmbd8SGUWIw2a6d80Zmg2bxTFqvymRCfxrAukqCKBl0mTvqOtBGqT1rkQZRxUUSyvdLVYs5D-A7Q6NrE_F2ZDPChkgfBg0pigZGIcDjhqP7I_StgHxyGI3k9EC4TP_8V7OoYpaQQZTCC3yyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=jY57j301CHorWx_XjkgX1KWLpGKyRi-GSpl0yfqgW32QvZuiFpEzNcaDNik_g93fHQ4lSdba14U25J44Hi0yOPzSxIl3KO0SYWXLd1cgtxw2ASZlOt0UcGN4R1td23-JlZgTWFhRVPzH5kChqedIucWpxV9pu0hO1t-zdvCP7xcVu-Mjzu9A6fcUzINGoD5qh4GyqC-g9b9x0GOAKNj8UmWciBTyMsa4qYpGMnehxsyVWdLIl-Hsxze0GKFb3nCCQe7jlnsKX0kc5eEMK-4N5-Debj7oj7w7mxeORvfo_q_mWo1MXZM_ZLNvRD96EB-ZtCPGrRK_T5rtv34i4KVGloBP63RDpjO6B3i-3CZpK7_5TY2l6UcZTcyh9aU2lxU7DXp4TzgObnybKK5rDJXJ7TMdqcS7VH_1r8xeAn8ue53R-l_yJC-ODgI4i0NE96P3nhTFq8YfwwZBdF_Y15Qnn7OeqrPZyKxw5lsBn6_y_qL4MhxHUx8gGH8YdYvPMHZqK5BqL-OuBpeFlRzGk2xWY68GgNikdhFqucNxpPn0RcYaC15qFQq4lHXBqbn1__ptPXnC_jqmHq0vTL265Ga4mXh5B7YuGAvkzxiije0c58Liu8HQGmBi8LrdxNO6eOjcaAN1TZfC1HhffrLAEht_P42ozePhZoVUIMTfPBzFSq0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=jY57j301CHorWx_XjkgX1KWLpGKyRi-GSpl0yfqgW32QvZuiFpEzNcaDNik_g93fHQ4lSdba14U25J44Hi0yOPzSxIl3KO0SYWXLd1cgtxw2ASZlOt0UcGN4R1td23-JlZgTWFhRVPzH5kChqedIucWpxV9pu0hO1t-zdvCP7xcVu-Mjzu9A6fcUzINGoD5qh4GyqC-g9b9x0GOAKNj8UmWciBTyMsa4qYpGMnehxsyVWdLIl-Hsxze0GKFb3nCCQe7jlnsKX0kc5eEMK-4N5-Debj7oj7w7mxeORvfo_q_mWo1MXZM_ZLNvRD96EB-ZtCPGrRK_T5rtv34i4KVGloBP63RDpjO6B3i-3CZpK7_5TY2l6UcZTcyh9aU2lxU7DXp4TzgObnybKK5rDJXJ7TMdqcS7VH_1r8xeAn8ue53R-l_yJC-ODgI4i0NE96P3nhTFq8YfwwZBdF_Y15Qnn7OeqrPZyKxw5lsBn6_y_qL4MhxHUx8gGH8YdYvPMHZqK5BqL-OuBpeFlRzGk2xWY68GgNikdhFqucNxpPn0RcYaC15qFQq4lHXBqbn1__ptPXnC_jqmHq0vTL265Ga4mXh5B7YuGAvkzxiije0c58Liu8HQGmBi8LrdxNO6eOjcaAN1TZfC1HhffrLAEht_P42ozePhZoVUIMTfPBzFSq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=mJXPr49ONEbwCoyDbaypPpwxRLta4I8vtZXikBfpTf0yANYm1I_fqo59ZDAYd-t4JJG7BWN6D6OdcuUT8-21FMJ58mdgPSVsNDGsE37Mx5awr7NcXlIi7AD0HQ-40b625THBEMenPcveUBtI2ElJStUd5HTXry_L-q6SY1eA6WDeAJana-8Lv4mYsPGcpyWuvI2wGWJWIke3FsMztAVHPmF71NhCCahEv80dFaSegi881IvltZTMHVoa7v2QJX7NfAnDcXNplveXcBU3m6fbjmiSKGFurXJxcYWekKnUY49BGn1MRBBXxB5G44HkTNgepApSFU3aJks5UN_dH5Vu8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=mJXPr49ONEbwCoyDbaypPpwxRLta4I8vtZXikBfpTf0yANYm1I_fqo59ZDAYd-t4JJG7BWN6D6OdcuUT8-21FMJ58mdgPSVsNDGsE37Mx5awr7NcXlIi7AD0HQ-40b625THBEMenPcveUBtI2ElJStUd5HTXry_L-q6SY1eA6WDeAJana-8Lv4mYsPGcpyWuvI2wGWJWIke3FsMztAVHPmF71NhCCahEv80dFaSegi881IvltZTMHVoa7v2QJX7NfAnDcXNplveXcBU3m6fbjmiSKGFurXJxcYWekKnUY49BGn1MRBBXxB5G44HkTNgepApSFU3aJks5UN_dH5Vu8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=dnlZqDuElmZwRJgl3wNhTX5eGCZ54AENxlWYd0c1hSD8r6yqtP_VhihuYIHZxq7WNHlSA2YSbyNDSRVxDqXu0Di0ohiMUYHYJj6U1xMunmaG2-X6c7JZysx1eyZ8sZJTIWn4GiAlsTZy4tJIpZK9HKTa1sWSCHwJwH_Kjd2ufo9kIVsPU1hfZbZuERXxGY8-Nt3QdbRY18i_MGQiZBJHPf84_o-2vOw8d-PNw5IO29O22m3lkJ6fwok39_xAuIjwdqbKhHsVesyrAzlw6azg5tLU2syJ7mGZrwSZRcr23rc1wvHg2TNlClbx8T4plGAQtfUANH4ZYPxnAaYmTVNRKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=dnlZqDuElmZwRJgl3wNhTX5eGCZ54AENxlWYd0c1hSD8r6yqtP_VhihuYIHZxq7WNHlSA2YSbyNDSRVxDqXu0Di0ohiMUYHYJj6U1xMunmaG2-X6c7JZysx1eyZ8sZJTIWn4GiAlsTZy4tJIpZK9HKTa1sWSCHwJwH_Kjd2ufo9kIVsPU1hfZbZuERXxGY8-Nt3QdbRY18i_MGQiZBJHPf84_o-2vOw8d-PNw5IO29O22m3lkJ6fwok39_xAuIjwdqbKhHsVesyrAzlw6azg5tLU2syJ7mGZrwSZRcr23rc1wvHg2TNlClbx8T4plGAQtfUANH4ZYPxnAaYmTVNRKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=otvv4olf0m2Sbz5fbH5t0I2ioiO-RGz8DE6fnEry_vDmCBZoAwKZ8pMkOQI-VmOlyFarztbq5iDg2da7ZDPNh2m56wnK6e6ttQmIT12dd8wr-1h6aOUfVWz_7rzAAu7oaxtx3M_kXGHEulhTM-c1qdA4fpgLiDgpkR2XI71hWE4NMtma3FtXMDjFdrof31TYOChHZqICnC3g88nilvHhj9XIUxrWqItvqAUcbYrBCtOJJO2gqiG4CTXTPjfVsXfWW1EWVE6nq-Hn35CO-tMaSnliAFgz-tTGDD8BugwzVXrP5riEVWgqXls-OBetnxLYS_E-nbsQk60LHBbs9zV7vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=otvv4olf0m2Sbz5fbH5t0I2ioiO-RGz8DE6fnEry_vDmCBZoAwKZ8pMkOQI-VmOlyFarztbq5iDg2da7ZDPNh2m56wnK6e6ttQmIT12dd8wr-1h6aOUfVWz_7rzAAu7oaxtx3M_kXGHEulhTM-c1qdA4fpgLiDgpkR2XI71hWE4NMtma3FtXMDjFdrof31TYOChHZqICnC3g88nilvHhj9XIUxrWqItvqAUcbYrBCtOJJO2gqiG4CTXTPjfVsXfWW1EWVE6nq-Hn35CO-tMaSnliAFgz-tTGDD8BugwzVXrP5riEVWgqXls-OBetnxLYS_E-nbsQk60LHBbs9zV7vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ftffAWVbEZrWVCapSfFhijLSj1UGiDOkevSo6pdEyOfwLpX7UTlfM80B8_raaxoS_D8OMRtYt4Wm0xvTyyYHhNnpNxWOK1AjP57AHZsCFz4CzyYtQMf1uVLyltnNkSiWgl1viZlLBQAgZ3kpgIbiKZzJi0z5IjDfokoKYfALzc9-8D9FyHgmQpgueAyXVjGSlWScizAKFRxp-oQH_5KvkPlafUGcOxvcC4OMMI8BZXFk3Mx4X82Vrk9UOLfbwrc4RPzV9pL1VKFbW1dp2agY7fbxSxlYssLmQTMh7689cFcVQCIO3S1GSFTityl1kG03Ys-zOTkOWrPsyp--rFvpBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ftffAWVbEZrWVCapSfFhijLSj1UGiDOkevSo6pdEyOfwLpX7UTlfM80B8_raaxoS_D8OMRtYt4Wm0xvTyyYHhNnpNxWOK1AjP57AHZsCFz4CzyYtQMf1uVLyltnNkSiWgl1viZlLBQAgZ3kpgIbiKZzJi0z5IjDfokoKYfALzc9-8D9FyHgmQpgueAyXVjGSlWScizAKFRxp-oQH_5KvkPlafUGcOxvcC4OMMI8BZXFk3Mx4X82Vrk9UOLfbwrc4RPzV9pL1VKFbW1dp2agY7fbxSxlYssLmQTMh7689cFcVQCIO3S1GSFTityl1kG03Ys-zOTkOWrPsyp--rFvpBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=qcQXjaudgrENwIBCJ8CwWcijUr0ZppSwm1wPTRHBir9IBI3NKgZQ1SP5rfoaoKhz5X_N-tzdiGjrxthGimT3fniCIYgFhE-7l4gByqkMGwC0kfu--A7XpgXHWAYqBaIjJAAWN6kn1u67vzRb-tjnLf7LEMExhBAWFSU9UHrYRh2y-cSiYr9JRoUGCiTUQ3j9AgT9OW294O6SnDe2XiLo3ztQF9xURGJNCiWSjMMJdqSSxRThRxifCYpBuNEuiCkKIHKAFuNnz7O7O7VE2zgFUMe56RTkOac8WI7vY1AIIU_zxtXWRT28RVHrbh0Mur7k56lJ7LNNInERPhZfkirc7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=qcQXjaudgrENwIBCJ8CwWcijUr0ZppSwm1wPTRHBir9IBI3NKgZQ1SP5rfoaoKhz5X_N-tzdiGjrxthGimT3fniCIYgFhE-7l4gByqkMGwC0kfu--A7XpgXHWAYqBaIjJAAWN6kn1u67vzRb-tjnLf7LEMExhBAWFSU9UHrYRh2y-cSiYr9JRoUGCiTUQ3j9AgT9OW294O6SnDe2XiLo3ztQF9xURGJNCiWSjMMJdqSSxRThRxifCYpBuNEuiCkKIHKAFuNnz7O7O7VE2zgFUMe56RTkOac8WI7vY1AIIU_zxtXWRT28RVHrbh0Mur7k56lJ7LNNInERPhZfkirc7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=anacXpy3YfIR5AEBjgE1g5Kum_Y5kuNkD4hXKv8w1MocfS8E57OEXPJ6nffW_V1XdTHocyHUizheofi_CKEwFCdYnXl1W3fIlwx4f6Ow332zIeNyxI8N3rjFSjKark8uD085Quf31UY4iGLBPT4yl1F9awsi1lrZVEbDJ2MIUeaIrlAQEkzwDgjApq1AgeNbPNJYC4AugwGovdUc-ZSx28vj1mB2zKIM-mRZb4emmmQ8d3hpfOKvQlb4Wi9HCBB9h7q1Y3ctzJl86H9ezMaDz2zyEi3H4LeRdrWdHjwoLUBTl_szveb7fHcPXQ_m0dosw6bpwPQlqZx4DgGw0PGPHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=anacXpy3YfIR5AEBjgE1g5Kum_Y5kuNkD4hXKv8w1MocfS8E57OEXPJ6nffW_V1XdTHocyHUizheofi_CKEwFCdYnXl1W3fIlwx4f6Ow332zIeNyxI8N3rjFSjKark8uD085Quf31UY4iGLBPT4yl1F9awsi1lrZVEbDJ2MIUeaIrlAQEkzwDgjApq1AgeNbPNJYC4AugwGovdUc-ZSx28vj1mB2zKIM-mRZb4emmmQ8d3hpfOKvQlb4Wi9HCBB9h7q1Y3ctzJl86H9ezMaDz2zyEi3H4LeRdrWdHjwoLUBTl_szveb7fHcPXQ_m0dosw6bpwPQlqZx4DgGw0PGPHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=DfJVEsndpvMHqPcSZI5rt_X2kTYXd0ZR2g9HwS8oVVZ77TiZ1HOP3uo3Q7GHlwClNLeX5wyL50aBOrdYtJaXMZcTiBXHiGHgfpAhbuMwZ-zxvcxePizWmHFDGdN_seYaJXLIv5gWEYldor2OxRThvmc9VM4ye-BNIkM6Kz4ia_PvX3J6QReWZCkFTPLcEUP6c7YjqOSPlzMpCCVkFPwFxewmq5KagUcONjh6hry1K3xyK65fbe1EPeVCCki4lKWJcDeA8pPuBw7yDqIOt_9xVNr5jdGPsA4axHQ6RxKhMbJkjP4e3xx7yOIl30KkQyGCokl6rUKN8_8NS3CGI8rcyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=DfJVEsndpvMHqPcSZI5rt_X2kTYXd0ZR2g9HwS8oVVZ77TiZ1HOP3uo3Q7GHlwClNLeX5wyL50aBOrdYtJaXMZcTiBXHiGHgfpAhbuMwZ-zxvcxePizWmHFDGdN_seYaJXLIv5gWEYldor2OxRThvmc9VM4ye-BNIkM6Kz4ia_PvX3J6QReWZCkFTPLcEUP6c7YjqOSPlzMpCCVkFPwFxewmq5KagUcONjh6hry1K3xyK65fbe1EPeVCCki4lKWJcDeA8pPuBw7yDqIOt_9xVNr5jdGPsA4axHQ6RxKhMbJkjP4e3xx7yOIl30KkQyGCokl6rUKN8_8NS3CGI8rcyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiDn3OfABEvKUSz5hQ6RvG-pj-Fl9OjXLsp6YywpsQLtf596E4AdVIQzYfAa-oXcj9QY8No96vjxYEaBhF-8ewJWDSAgcTsKcWsqtYLIemUrxc2bBnMkFKZowKnBGsQkgc_vEsrbNImN3M0hcIyg8cgw2f7BTkWGyLR_1l-ekTwhCuHTNqNLFJN97UoVSkFpYIwkbBvYPS2iYM7ceJjG7jWJ8irz9NLOVk51fs5TCqSMhvhSJ-4cPL85qlbANdrEdYZONW1bP8pmkMBcxp-QQdSaFF-V-sOwPr1N838EOleIq4Ytj4Tj70OV8VMwXPJZlyFuRZ0lHFmC_IWsQpPxxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=gC1Cd2AeUeFpUfuw_pfNFN19qruOM_pgEuBfDYyQXLuMa2xgBWHbzzt2ZqkjdkptGK_PhSBTllBlHszRw6vO5WwM9EHHSlnNNM4SVimcWZa70XKBFgkhcyXfLklYI_MTkk68u6NpuwT4tcIT9xKgmt8d4bMoQhI_eDZC7NmqxG8qt6CcxZF9XVbmb3lDJWUGm2aq1lOXc5J8LiZBiTL-b1r402kvVBaT7HrMT_b3b7FZ-0YTuAQ11Vk1Tgfn698I9Ma91itZJsr7HHWL4Gju12dHsKmMg5VWOETiHEgul1L3mgR547pd0FFc2DUV3I_Gz4IK5Et97HmGzu_k8jXftQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=gC1Cd2AeUeFpUfuw_pfNFN19qruOM_pgEuBfDYyQXLuMa2xgBWHbzzt2ZqkjdkptGK_PhSBTllBlHszRw6vO5WwM9EHHSlnNNM4SVimcWZa70XKBFgkhcyXfLklYI_MTkk68u6NpuwT4tcIT9xKgmt8d4bMoQhI_eDZC7NmqxG8qt6CcxZF9XVbmb3lDJWUGm2aq1lOXc5J8LiZBiTL-b1r402kvVBaT7HrMT_b3b7FZ-0YTuAQ11Vk1Tgfn698I9Ma91itZJsr7HHWL4Gju12dHsKmMg5VWOETiHEgul1L3mgR547pd0FFc2DUV3I_Gz4IK5Et97HmGzu_k8jXftQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=tXcnxRAOnh1CylPTb5jLvQiIURO6yv4F9ybhukEnzpS1omCTxJjdKtRPlZgtdkej58mBTAjFt1n6FN6W2n5pOmrbgRFsCORgrgF0MKRNK4SD2CXFhCeHHmSr7x7EDOO7AsteVRBAm6xhlc3vmYAaY5eQAkBL5KJ3TWkmv0vNPJ4NJzdap9WpfiE_zdl7tvH9Kl5HSvnV36Cgd3fL56wsumN3IdMLGjxVPLb52VPT-3j19LG9BtY4c3dy_y1kVhMNsZUcBRBNHWOC66WJUmLpoj0chO-or9EIlTSS71sSgr2gBs_kDYiu_renlCLLCUrS_ffKzlKfV53oQuPC2k6GZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=tXcnxRAOnh1CylPTb5jLvQiIURO6yv4F9ybhukEnzpS1omCTxJjdKtRPlZgtdkej58mBTAjFt1n6FN6W2n5pOmrbgRFsCORgrgF0MKRNK4SD2CXFhCeHHmSr7x7EDOO7AsteVRBAm6xhlc3vmYAaY5eQAkBL5KJ3TWkmv0vNPJ4NJzdap9WpfiE_zdl7tvH9Kl5HSvnV36Cgd3fL56wsumN3IdMLGjxVPLb52VPT-3j19LG9BtY4c3dy_y1kVhMNsZUcBRBNHWOC66WJUmLpoj0chO-or9EIlTSS71sSgr2gBs_kDYiu_renlCLLCUrS_ffKzlKfV53oQuPC2k6GZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=s8S8Ve3_UUkAlMzUiFjAAD4MgEkYQELJP1yRVywr1LEoxi1uIBRxsGfSnG3l78EOYLD-F4KmpaamFPt5c6HAUv03rAEKluCRE_l7KCwXu7OI2wbXcJnuWcmfT4hxWc_Csh3jisG91VdYsNHjghqmRHjNBH0U1tpA0EiJQkSjXOLrr5_0qFGq7kk4NBbukkrF3wsNh4_rvbQKVGBTqVeiNB2_Yif7u3lls2CzWB8VpbXQbbMPZUEiRtzfA4iccIc82nZXYsCIixC7eUTX0wW4B90q8JQnb0riog0EjlQs7qcTN5unNRXRDIIspbCUldhGciTTxnDnqch_-xnlrZuN3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=s8S8Ve3_UUkAlMzUiFjAAD4MgEkYQELJP1yRVywr1LEoxi1uIBRxsGfSnG3l78EOYLD-F4KmpaamFPt5c6HAUv03rAEKluCRE_l7KCwXu7OI2wbXcJnuWcmfT4hxWc_Csh3jisG91VdYsNHjghqmRHjNBH0U1tpA0EiJQkSjXOLrr5_0qFGq7kk4NBbukkrF3wsNh4_rvbQKVGBTqVeiNB2_Yif7u3lls2CzWB8VpbXQbbMPZUEiRtzfA4iccIc82nZXYsCIixC7eUTX0wW4B90q8JQnb0riog0EjlQs7qcTN5unNRXRDIIspbCUldhGciTTxnDnqch_-xnlrZuN3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=icL2Iul07SBDnO9aYrU-8nxGk2aYrDLhOhrpdorU59UXn91QLgz5lcGqzc9vxdEK5GjV7Zfmkhh2zOtWQuET5sTALw30kO_j1UmuJwc49HqI1SlLuTJhi_cDdUsaWvGanP6fbU5lWIM2jSp6jnDdemDj6Wqaz-6NBV3pzcyKg0qbSqf2PgsS5nihp5eTtNce6HaXBhWXLDAifP0q8r4iTrLnEwJ-E8F3PazTMj6T8NgK28iyL2HyeGwkfnEIQgFMcMVpHazrFIX1q9l7PD9LMmwnLxlSMLlCuMhJY536dEdL-K8kDRLah4dpw0pRIjzLoRPLLTyDahTHmc2c6vf-Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=icL2Iul07SBDnO9aYrU-8nxGk2aYrDLhOhrpdorU59UXn91QLgz5lcGqzc9vxdEK5GjV7Zfmkhh2zOtWQuET5sTALw30kO_j1UmuJwc49HqI1SlLuTJhi_cDdUsaWvGanP6fbU5lWIM2jSp6jnDdemDj6Wqaz-6NBV3pzcyKg0qbSqf2PgsS5nihp5eTtNce6HaXBhWXLDAifP0q8r4iTrLnEwJ-E8F3PazTMj6T8NgK28iyL2HyeGwkfnEIQgFMcMVpHazrFIX1q9l7PD9LMmwnLxlSMLlCuMhJY536dEdL-K8kDRLah4dpw0pRIjzLoRPLLTyDahTHmc2c6vf-Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMvLm1e6-0rq0u201szLb7dPM2SCfHc-E8INpDtUVrj3r_4w19M8tbbR_DkS_rLI7LmxGOiVcj6Q0rRsZ6zyueOf1xeDQnVA-CWKNpwsvPWLoZo_M4K1v_ERBPRnZAOivKVfChcaQ82d8LnheRB1zGVkY75pdxf_af_TW5prvJ7Jz_lC8tM_rzgPCIHbdcpoJ24fwc5nypZsKv5ZzIaa-ySMithWI4itJsD20gjXD-DFFwFhyVM8VC0dO6AAafAyxkWNIWkmbiIZrStp59MKEKeHpgX63QQJiSucfYmDLs7hqvbwhEKwRZe6Rx-FVsZ6m5vwDoakZzHA9iCpg2ka4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=lJqc8fkFFln-CDvKsSumRwab4cSiu6epqTjwcHFgpCBsqyWbIes0O2IPDpp3U8-7r_SC3Mi3vIL7ThcUy4Ya7YY3L8sSviF6cPGi68zFDl7b7w0thrAsjExBiOk3MpIcEnIrwOcLDKgOC3NZbndKLr8DUlJRCxYq8WKXOZOhPleurWfvoo2UcLPvdwdIBNUYJIvVlt-IfzFRmcDc6w-tVwFGSa4aW5JJYhNzDTSyDmVNEhbjlPGMuDLixOgj1O-gGBWm-DEsyOeFzVTIgV0gTCqmtjYbtBV1YvZ2kZRgJ4KAPlUge7F2Uo4zuPkdauO17nK4GCQ_KVoHycU3FUDXtTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=lJqc8fkFFln-CDvKsSumRwab4cSiu6epqTjwcHFgpCBsqyWbIes0O2IPDpp3U8-7r_SC3Mi3vIL7ThcUy4Ya7YY3L8sSviF6cPGi68zFDl7b7w0thrAsjExBiOk3MpIcEnIrwOcLDKgOC3NZbndKLr8DUlJRCxYq8WKXOZOhPleurWfvoo2UcLPvdwdIBNUYJIvVlt-IfzFRmcDc6w-tVwFGSa4aW5JJYhNzDTSyDmVNEhbjlPGMuDLixOgj1O-gGBWm-DEsyOeFzVTIgV0gTCqmtjYbtBV1YvZ2kZRgJ4KAPlUge7F2Uo4zuPkdauO17nK4GCQ_KVoHycU3FUDXtTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=n9T7BqNilpbDodfsyjw70_DY60CTCZ5cOHURaB15wapPy4NpliHOAnhpAGit1gDBCw5ZWloDzNuNo_-m0xDfwt2x10_D6TX8Fu265l-VzTezsTEaiVXh-lMfSjggXbgk-Q-RwkoNyrM2b0ewff9CUFeDq4983nOH3Lyr2dSArDqjkYagNApK6JCCjcI5GeID5NfUsdez9fNyqzHYZfXyrku01No3bDigTe1OcRekbr7T5KloY4nWko0poU9p3Xes2WwlinURzMAeQXgr6FWesL12UwMNgYCjUFMHJVP01JfOwZRHK58DKhG73AYihLUJDgtljpySooZQPNl4XwGFpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=n9T7BqNilpbDodfsyjw70_DY60CTCZ5cOHURaB15wapPy4NpliHOAnhpAGit1gDBCw5ZWloDzNuNo_-m0xDfwt2x10_D6TX8Fu265l-VzTezsTEaiVXh-lMfSjggXbgk-Q-RwkoNyrM2b0ewff9CUFeDq4983nOH3Lyr2dSArDqjkYagNApK6JCCjcI5GeID5NfUsdez9fNyqzHYZfXyrku01No3bDigTe1OcRekbr7T5KloY4nWko0poU9p3Xes2WwlinURzMAeQXgr6FWesL12UwMNgYCjUFMHJVP01JfOwZRHK58DKhG73AYihLUJDgtljpySooZQPNl4XwGFpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bdwaWtt8_HbFycvrn3-cBkviMT_HJeWmTZJGpnyNXFBgNj19uoowk10qh--3UO28XNJz4sfczRSwUKVl4CcpuA2b7p_rO0PPl4IfAwrhM38y2dF_FX-VvDUwZUiaIMIhXpCOUxahCzWgwofj-7NmWg9QmH8L7iFGxo-RhcL42DdfnesYPj843aVMwHGHEW2NXJ7odLora4MTq0_GbNKiy8VVxqecWp3tN7EopvhZ89QVWGuRR2Xe2MRs5TFdwXLSGTuImavx7hDkFeOGwoxgxfxF2RzmIZHOr4AwVPdX-Y0iZAr8SjvRlgct80j-NKFvQU5WjBQSeRuwXIl2Jp-2Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMZdp_ZMKLbDMusVh7k_h0ZcnW07GXAYAK4C2A-aqdRjSQmIvi6EWtKeV3N3_5xQKdPU2uzjMmXy5xoo7_v-YRavE3Idoe38khBCbyWzuhE5-ibo1fWBeMKaMWCtTDynLsQeDE4s1sJnft0x7xKQemdlcGq2qf7SD2IIeAJvvCxb0tYbS39-FKjOCvESaE4PSBOR1bSPM-p_94Tm88NuHicevb9CDQ5J7ZkAR105uDlG7SKPtWT8oqbnZJ1pRpI9GQiw6o0zuh4bCoJrmvj-4Y14QLYwWLGq-wvDpxpe643Q5IR2WNJYtem7s_SvrM9LO8UONAMkYOzu1Zo8-cvWwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Oresnju2cydB8q9qrQJLGIrqKWxmaT0GCIIAuLoI-t0Z-d1AV-pN2yxLQDkW3rurdqpfjc3VPQ5PTfSvdUueetkXDSod-hZncpA-ZDTCb1m6ipGls8qZ-V50cpxyZ5iudt24ykIS5Bhjz5Q6hQRSqEOMyt0Qw7Zik8xmzIcjy6MhH-DRxtHcxVou2FgiRgno5pwUAYWzG4Y9wmmiL3KNYDxNDG0X_vb_mEMqpxowDnLIhI0NnmR6f4xW-TTkycJP0N7fA1R33B65uUQeKrxx0IHvOetWf7J3GcN1cusG0jeJBeEq0ljgOdw2rGv7_nEK5_DORoPMaPAJbW996KieyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Oresnju2cydB8q9qrQJLGIrqKWxmaT0GCIIAuLoI-t0Z-d1AV-pN2yxLQDkW3rurdqpfjc3VPQ5PTfSvdUueetkXDSod-hZncpA-ZDTCb1m6ipGls8qZ-V50cpxyZ5iudt24ykIS5Bhjz5Q6hQRSqEOMyt0Qw7Zik8xmzIcjy6MhH-DRxtHcxVou2FgiRgno5pwUAYWzG4Y9wmmiL3KNYDxNDG0X_vb_mEMqpxowDnLIhI0NnmR6f4xW-TTkycJP0N7fA1R33B65uUQeKrxx0IHvOetWf7J3GcN1cusG0jeJBeEq0ljgOdw2rGv7_nEK5_DORoPMaPAJbW996KieyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqESnJB9LvyZAetr5W6BzNZsIR8mgID5PwBrwyzkU6_viYgcmGSSEYXC9zgoS8geisiXMlHv5aKFn8qnhFkoF8GI_3iuy3ZuztK5t49N1XrYILZyCBQcrVHlQO-3EvZ5S1avjBFi9S2iPirBpMudfxVKn8ZXdOUJqc-LiG1offt0OyLZgQYVlFCvr6-tjp4DyajiVvnI0EdSgWkHbkQW4uEiuzz1m-V54Dyf08UtlvAXnCHdcyv-1eepPxVK4Kh_9O1YvkLQ5Fyqct2DINM8PJ7mJe0DIQJ5h0DTP-ixVKLgEa9Vhp65TIhZH2VypUMEb6yf73xAveBTnJbavy65VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rawCqjjTlNGNtnyRjoi7LTXdJLwzyorbtjVh3zDiy_5SUnLXsenhpmda-ktlX5hLMoXsVPFPyPY9o_wdCkI2XW1sgqdbC70_-FyPcO7CG2h2at-V3Wx7XmbBunrtXqQZAexl9OagHh_OYST_uYcBKIBWlKKto-mcfsU0QFv5krCVMglP5xmGvzWh5P3xdIEqlrNqGH824lU44nMWGfg2I44I9F4TQ8oA0mORXpCmCdPaC7W_1fi-NwBKrqVQy-HvlNAbwS7PYOxUwqXKEV2arhqkmyyiVotddqEf3aXs9Y5KDgrEzzcUHlZ0fpWdSo0rgkGcEcUPwRKvDS-k5HWxVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9qANxlhuM9ibNCdLcmPsNh_vO0Xi7q4RaXeOZ_xp0dbsnuGUcXCbxd2YGXs1PMXHwTXyy1ziLkH1UgVXKt1AedLDfViM2iYPQ2VAjwM3HTpjspzQiG1V_Pxgc6T6e5Ohxoz8nl3Dj2AvOGvxvjghZqFqm6fWgwHcqVXCLJHvME9IjqWO5oClb5RoT0P4YNk9POqV15aOoQaq6Od47J1VeEOd7BWPs3SIBZOkhyBgAdOLKP3Y1QdX8a9OYIid8HiGwYKgfMbZBXzQ9erIFevRng59OFR_FC1nEpDGMB-630KylERlvXKtg2ISo4W1M_8BOyW44M46-uq3UtZKjt6sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=MdvAsyKDcQpnwIhmxGCJMon-VeHTOOJpEZTmRNEZcMP8RduPVYEXeVd0Y_IkyujBPwuKps6xXuCNsvjozPA2OJ3E6t6WozCBBAR_Rr6qKUGm64I5j-Z_PkObT2h6CON3MQLWUJbojHzAf34M0IN8taw_LWsrJr7LK03SvrGGuQut0eR5_mXsodSLQBPNJ3GmMIvI_Tofi8dQy0zbtiR-OkCNlq4RJNvRCbbm3he0w9LXpfVwABDautEpPgbJwPKM095w-1XE9UN1SjpPVHKm0Fr6oMcSgNj2sStLs_Wh5FNOukKR-pMiGu8yqkd8M1HKhhCLxBUkeQ6JgOS1MDMkAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=MdvAsyKDcQpnwIhmxGCJMon-VeHTOOJpEZTmRNEZcMP8RduPVYEXeVd0Y_IkyujBPwuKps6xXuCNsvjozPA2OJ3E6t6WozCBBAR_Rr6qKUGm64I5j-Z_PkObT2h6CON3MQLWUJbojHzAf34M0IN8taw_LWsrJr7LK03SvrGGuQut0eR5_mXsodSLQBPNJ3GmMIvI_Tofi8dQy0zbtiR-OkCNlq4RJNvRCbbm3he0w9LXpfVwABDautEpPgbJwPKM095w-1XE9UN1SjpPVHKm0Fr6oMcSgNj2sStLs_Wh5FNOukKR-pMiGu8yqkd8M1HKhhCLxBUkeQ6JgOS1MDMkAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=O7YJL9_YPx0uas9z5xz_J6RBY4MbrucsyzZ_wjLDlQtzWnqxlMEAbZ1bJVJgfSsDbPKIu4avPGQLzg-c12iOEwcj5uflkJPB-nSbMBUzd1A9NzaivbO26l3_PyiPa8xhXBTgbPr1aJJwUgfOCETiCcKpiqV7uoPJ_TZsLV_JWXJo3nw8HwlJdjGlfnMxKM-csDRLrOcCICXF3X8PXAHEQO9nZodUTc6hA97gptd7obxIVSmzNgvBn4iE-gVu71x1iOpEPx1OFMLhDyKZm_o3snkHlToM-EdAP7X_bMmz93dCmzVlv79tkUJ3wVx6tGO1cPjK-b_E0QVatA10S_RZ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=O7YJL9_YPx0uas9z5xz_J6RBY4MbrucsyzZ_wjLDlQtzWnqxlMEAbZ1bJVJgfSsDbPKIu4avPGQLzg-c12iOEwcj5uflkJPB-nSbMBUzd1A9NzaivbO26l3_PyiPa8xhXBTgbPr1aJJwUgfOCETiCcKpiqV7uoPJ_TZsLV_JWXJo3nw8HwlJdjGlfnMxKM-csDRLrOcCICXF3X8PXAHEQO9nZodUTc6hA97gptd7obxIVSmzNgvBn4iE-gVu71x1iOpEPx1OFMLhDyKZm_o3snkHlToM-EdAP7X_bMmz93dCmzVlv79tkUJ3wVx6tGO1cPjK-b_E0QVatA10S_RZ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=t7Q0NBjnf5f46aGSvcyZFwBIOzUSh7orlIkOSjsoq4tSz70bSTzwRjVh1XlDMgW37FeTTncmqDCrEcdxGo3d__bJPyY2mYc9onLHAa0SzoNj1vEJjWHBS_5tnLrSMz4Me0idoIkrqOn6rTXR9P8TnVXvq0GyORt87QsmceaPKMGztnm16HQKbiu2SFwEdcGLdWhs1RWtObluUApoE-mpZr2BxRBMJVB8NK3Y0pIVF4T8FwD7ugGSsBgoK1FGNqu4yrWqHqTRo1r-grqmxFKlo9Lel-VXUCkbRrFvkG0GjgNXDGuX4fGsdSoCUUBL_P2zA-emkVpGIj8HnQqE25BGunqLp_UH_Jj2JWGVXK9sv8lqIU0p3W-3ESixJZtAHN_IpI6XhPxBTDcp7IuRk7lJ8n_Z-WWrA3njXqf9eKggj9d_PFst0xXaPcftGqwEwZAefKU9oENVvrhQIlMNtIuW6NxHbnvuBBSt_FwTWSUxJQWoHidaZjsfpDIe4htdBcn-tpgMULG8sbUmZdCNzk16xaRTwbfHLy7HNa18S7al8CGOkRjijjmjgZYeJAVb3EqTmvRAuRx9VPk-Ni9-OgVWqBQPs7LjajfOp_KIOOfi0CJaEoY8cgHBUh5GPmf3ApECUt73h4UFkGYj-kLkydGvUu9j58Zg_paAFw_py70vTZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=t7Q0NBjnf5f46aGSvcyZFwBIOzUSh7orlIkOSjsoq4tSz70bSTzwRjVh1XlDMgW37FeTTncmqDCrEcdxGo3d__bJPyY2mYc9onLHAa0SzoNj1vEJjWHBS_5tnLrSMz4Me0idoIkrqOn6rTXR9P8TnVXvq0GyORt87QsmceaPKMGztnm16HQKbiu2SFwEdcGLdWhs1RWtObluUApoE-mpZr2BxRBMJVB8NK3Y0pIVF4T8FwD7ugGSsBgoK1FGNqu4yrWqHqTRo1r-grqmxFKlo9Lel-VXUCkbRrFvkG0GjgNXDGuX4fGsdSoCUUBL_P2zA-emkVpGIj8HnQqE25BGunqLp_UH_Jj2JWGVXK9sv8lqIU0p3W-3ESixJZtAHN_IpI6XhPxBTDcp7IuRk7lJ8n_Z-WWrA3njXqf9eKggj9d_PFst0xXaPcftGqwEwZAefKU9oENVvrhQIlMNtIuW6NxHbnvuBBSt_FwTWSUxJQWoHidaZjsfpDIe4htdBcn-tpgMULG8sbUmZdCNzk16xaRTwbfHLy7HNa18S7al8CGOkRjijjmjgZYeJAVb3EqTmvRAuRx9VPk-Ni9-OgVWqBQPs7LjajfOp_KIOOfi0CJaEoY8cgHBUh5GPmf3ApECUt73h4UFkGYj-kLkydGvUu9j58Zg_paAFw_py70vTZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=CheQf7mv37YnMkvyP-T-85Crcoq6rgaxlS2uX6S3esYiDtbidJDXmXT87rIK5L6WcxUFjBPj5vzyo1rPGBEi3Br9NWUiLhhljBBATwU1I30ggunDlOZ94F0IW9oZ8x2F9OKhov44O2z9Ga_-zwdV-u2BknkWwOL8R2EaWe169xDcGcbCB_Ih9CsIFm8dWBzq5RgSAbspT2WMF8SMXFW81IrVhVFBedq0sKl8OQJOPr4jjFqBRmdwc8mBcNGedAqnRkmvIjacaBYgqcuo7Nk2WSC-EHPjnz6c94pkDM31fSEOjLZ3aWOgcE0AZ8v2GpyQqxNONXajJXhoPWqxGDdqarYgsUcFoDazqrP68NAtytv3-afKyH_YKgg7oIplZLaXMG-jdskl0XdyiAe4k9MEEygNHm3JlT1ZzFYucBTi7-oFbFog3uLeu3KWIe-O1R5VB4b5O97WTHGBXLI75MNtL9ohOyzhiJdjmbME5GXxbvL3cdwm5gBV-oYFpq-pA3m0i4_0i_qgORQu-4ARQK94kBGb3j_vnHGt7AbPD_dL3jZsoxxR5jGgJL4CF76Fjd5G7qJWQHsHTyO4s8x57hsn9A3dGYIt4noMT0SiffFDsg7d9pZgV8vR8MxTRpozl_FuisY1Hy_Fvm66tmdJjAUpLw020mGWLaASotcNgNPWNGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=CheQf7mv37YnMkvyP-T-85Crcoq6rgaxlS2uX6S3esYiDtbidJDXmXT87rIK5L6WcxUFjBPj5vzyo1rPGBEi3Br9NWUiLhhljBBATwU1I30ggunDlOZ94F0IW9oZ8x2F9OKhov44O2z9Ga_-zwdV-u2BknkWwOL8R2EaWe169xDcGcbCB_Ih9CsIFm8dWBzq5RgSAbspT2WMF8SMXFW81IrVhVFBedq0sKl8OQJOPr4jjFqBRmdwc8mBcNGedAqnRkmvIjacaBYgqcuo7Nk2WSC-EHPjnz6c94pkDM31fSEOjLZ3aWOgcE0AZ8v2GpyQqxNONXajJXhoPWqxGDdqarYgsUcFoDazqrP68NAtytv3-afKyH_YKgg7oIplZLaXMG-jdskl0XdyiAe4k9MEEygNHm3JlT1ZzFYucBTi7-oFbFog3uLeu3KWIe-O1R5VB4b5O97WTHGBXLI75MNtL9ohOyzhiJdjmbME5GXxbvL3cdwm5gBV-oYFpq-pA3m0i4_0i_qgORQu-4ARQK94kBGb3j_vnHGt7AbPD_dL3jZsoxxR5jGgJL4CF76Fjd5G7qJWQHsHTyO4s8x57hsn9A3dGYIt4noMT0SiffFDsg7d9pZgV8vR8MxTRpozl_FuisY1Hy_Fvm66tmdJjAUpLw020mGWLaASotcNgNPWNGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=D8XDvHTndaLswdg_z83uIkSw7A5VIct0gKaKyHc7cSw5UlKpw8IrFeF9yClJBBpioG0TrMD5a6i7GxZQkPQZ_KsdCcwHLOZQj426SpS0mm2FM3cvBIo2RjnP2rIQAX_qJFl-pFziE0oZAWCbLurXisqbv3geDtCMpsZcoONaVh9On9gyvja39YjIli33Q7fmpP_2Jd3NQwvO6P8CtligFHqN5NlS2RxkM3p31Yz_QY5z6-c1pbsyisaxpFh_eDDPEN4guWB3lCCux4qnfRQqPkdG8i58swhbOhB4EjXkQR9iCNTM6MbC0vXfcsefr81Km4hHrmh0YrcqGYeMplDXfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=D8XDvHTndaLswdg_z83uIkSw7A5VIct0gKaKyHc7cSw5UlKpw8IrFeF9yClJBBpioG0TrMD5a6i7GxZQkPQZ_KsdCcwHLOZQj426SpS0mm2FM3cvBIo2RjnP2rIQAX_qJFl-pFziE0oZAWCbLurXisqbv3geDtCMpsZcoONaVh9On9gyvja39YjIli33Q7fmpP_2Jd3NQwvO6P8CtligFHqN5NlS2RxkM3p31Yz_QY5z6-c1pbsyisaxpFh_eDDPEN4guWB3lCCux4qnfRQqPkdG8i58swhbOhB4EjXkQR9iCNTM6MbC0vXfcsefr81Km4hHrmh0YrcqGYeMplDXfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFIuBkon0D19xiYcDK4rwJOsv5PR_zKrRNlzE7QAhYt8E64xFbvev6CVmxupnS0xagoPmvGFKcy4ygnYG7Z8ZTaskaw1_QvBykwgqQr_HZRqBajHsx115XE8e7Xao0UFXIbzKuH23D9yhz-H9zDgZOQx3oszTc12HgscOsIilcxwYlsPzwSkHA7nt9SHhRFTL82AfuQoS-11GUh_jGO4RdTP06zk2VjWr0fj1KAZUqp3WXcMD9dhqyj-zZAP9w5eBfOtDdbnCqhmkoDo5M9wQOYq4QV53WI62vsBplxXDQRntMBrm_htdwH7ElyHd02yjk9nFk64JNnAQ7SI0tRLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
