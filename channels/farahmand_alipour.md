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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 05:41:06</div>
<hr>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRbyyzVzzGHh1SjsTobh4tHDu692ZSyaH1cW3n2FHDLPTFOdABa-RjYGcpnpE14y8onsGHSlhwBv4ReOFFxpLUOcznmU8hR4OqhgZdT4Z1DUS8OzeuOIx05Zr8sPNtdkJ_xH-tFcdJ6LcVj7FzzRhdswxprFHLTfndYyYA8-ieKyt2oU_dUSU3BQOI1W8SmFVc2FMPMMWINK8nns79H7uCbYTiinpgbM7auq1nQbk46VTc9BBy32casJ1zkksN3AhQaXiGpHUcL4U2Huj51mIiYpKkGjItiH5WK5cYwop2BMEMerv9YNWEsxepi6FBlY7bAlXakEddg5sYjeuioPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNoQadWKgIlK7VSJd1Av_ejbN5BprScbz_EOi_QQ6HD7AqLB1jaWTed1ajaDWkd1-qHsu336wsyILSs38f1j6J2F9CT6Or_7rWWb4MyevKBWc8BOudV25pcosXMRJ2cCbK85I9UaM-wTTK6hL8hNu-idruvk92TUt4rXbxR531zeAuFQiVFj7iG57cW3L20fDSrqmu3eXTlLHyH58jYwxekuXBy14wEHFTi2IS7NJ54T3WFIs2Yv91xeSQWSiLDEn9zx5Lvvu9myjE-VlR0NlPV0us04DJzBpnCiuWLrT8zd7wBdSsPRnrXlllohDu47MqL1pq-In7uxAIhHSExUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=iBpsDQ0KZCSrJq2IpGYfvJlH2uUOQlRc9mbpE52Z09XiZt8nZGTvIyHC0-qdurBrwlorKxa8PAAKNmuKQeVMRLDJxm9zbmN2PyJie7CAegHWZjzntTFX_68cEiB4f_cu0RsXxbO_aptz4a_KjjpY1eWJkDBcwE4IRiWICESEVb7oAflSl-kpB2Bth5OcONeOcibNO53FYO2ehTvR8JavQg8WwgW_hNv0suDG1E6EvcfmihS3P5DRsj6spXPyNaUjhKrmTWCpvcQTitJHdwOlGipfJw0StOfsFgofwb2_ey-UM8xEAapN0iZa__1fXy0O4xlDfFNiuW8Db9j_fAZgRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=iBpsDQ0KZCSrJq2IpGYfvJlH2uUOQlRc9mbpE52Z09XiZt8nZGTvIyHC0-qdurBrwlorKxa8PAAKNmuKQeVMRLDJxm9zbmN2PyJie7CAegHWZjzntTFX_68cEiB4f_cu0RsXxbO_aptz4a_KjjpY1eWJkDBcwE4IRiWICESEVb7oAflSl-kpB2Bth5OcONeOcibNO53FYO2ehTvR8JavQg8WwgW_hNv0suDG1E6EvcfmihS3P5DRsj6spXPyNaUjhKrmTWCpvcQTitJHdwOlGipfJw0StOfsFgofwb2_ey-UM8xEAapN0iZa__1fXy0O4xlDfFNiuW8Db9j_fAZgRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=q2xcH3mLVErsm3o-ao71vLqzK1nF__AOg34OCQfviIHlJ4AeltA02UzVmWNxQgzyyLbbOZ0MdQuaUESloRRX4e3c61GMrJB7c9TeJgnESDHUwGv4LxVdrdPlVomMW_6gzo_NQHPSUBti7W6KEzkIkQKLyc5k_YvIsU22OMJhuAODPVJlrHVddv7uUqKGLrp_b938H7BnAtrPgR2f4zeDlKWt4nh0_QewXky_mqvRlkudQtHgDAFFP8ifE7CSAsrsUijVivxNTWT3mWas4fbXzhfpVJs2jtNqjd5ZDvem1kJcClFZ1KQcTtdxAjyg1o4wqnCITpSSd28jJELJsHD4yj1y2zzmikWtm700mPJfMksdvaOIvqBAGtAUgC2ckhf24ll5AvjIqHfJSTQ_DImoxLAK1IZlx4XnKafk9fUdL8g8RtEilc1waRStMF8Z9n0Jlv9R3EDWm2t09UdZv6D-TBJJhbtWQ3pKuxFwpYLXfie0ORP-LdFkQPjxSz0B6KBuH9TsdLrjpyDC27mcgZ76TJQoEPIR55kGcxGjRlsMZVpQD9dnTvopo2TPQz3ZE3HoFr42D6aOdsRVCvUcbgcfVqDaePJCQDM0vYCD1pcZDVZKA_PbYe6vSdmjUPvyWHzfSoFdRzSG_uye_h9nFftviAEjrEgTuXvQW_AXIYJl7hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=q2xcH3mLVErsm3o-ao71vLqzK1nF__AOg34OCQfviIHlJ4AeltA02UzVmWNxQgzyyLbbOZ0MdQuaUESloRRX4e3c61GMrJB7c9TeJgnESDHUwGv4LxVdrdPlVomMW_6gzo_NQHPSUBti7W6KEzkIkQKLyc5k_YvIsU22OMJhuAODPVJlrHVddv7uUqKGLrp_b938H7BnAtrPgR2f4zeDlKWt4nh0_QewXky_mqvRlkudQtHgDAFFP8ifE7CSAsrsUijVivxNTWT3mWas4fbXzhfpVJs2jtNqjd5ZDvem1kJcClFZ1KQcTtdxAjyg1o4wqnCITpSSd28jJELJsHD4yj1y2zzmikWtm700mPJfMksdvaOIvqBAGtAUgC2ckhf24ll5AvjIqHfJSTQ_DImoxLAK1IZlx4XnKafk9fUdL8g8RtEilc1waRStMF8Z9n0Jlv9R3EDWm2t09UdZv6D-TBJJhbtWQ3pKuxFwpYLXfie0ORP-LdFkQPjxSz0B6KBuH9TsdLrjpyDC27mcgZ76TJQoEPIR55kGcxGjRlsMZVpQD9dnTvopo2TPQz3ZE3HoFr42D6aOdsRVCvUcbgcfVqDaePJCQDM0vYCD1pcZDVZKA_PbYe6vSdmjUPvyWHzfSoFdRzSG_uye_h9nFftviAEjrEgTuXvQW_AXIYJl7hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuAfiKIbvHYyixTh-5B1UHgnpn9g2TdTcj_cIfwkcD8WaM_NhThnJgKIQpTn1Q-GYpflBjSoyqxAND0xUr2okZUlxmPiJY1IVEVJAV4eIa7dKpid8Ag1lzWp6jWeiSouALVuM2QskCHdnRSq6XK8tpYknPn256tQ-MVsDz2aH-E6VjdX2tJnGhkxIA-EtW6gnv8S7FoJPUtuATQWMUCs4kEM1FfojExvLoh0-q6JLsEuc4qFITamcjIQRPS_hBMN7gxrCadDlgjY9_Kk7CWhTtq506Rz9OVLodgVw_zAabMKU3EhyTeGpTOs2JvILdLT_99gIqSIXP3i2heRWpgTVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1zOjeQHetoHjoxbhpK-tRubTwSQxm5q53W5nmwalYWlE2BXKOZ0A4ZjhjUPXHCKld2lFyVZi5IuPBHE-BwefcB3Zv0oLjW2sXJA4b4TruLoCFL0TX9ct9iHsWOkLepjdCiITVh7DooMqKp0wvOTNz5HJNHz9h5MsYTOPxS629WlvSJU8Gpns5dT8jegKVlNJ-hw7l5HEwfXeHB71YOyvcz5qrCQm8FH_LbTTiZml3yphSdiBdXTvKZCLY9rDhvD2jEVKzsgDT0qh10wJZGzGEl3suFzy3pNG9Oq08V0rNuQnbT6D0_NDGS7JD6gk3iF8yjbedutvPFHjDTowhh-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/euRQ4T3JX4-7IQKl7IxTv64pwyrSfSWTsGmF5R7V4ANC2w12CKQC5iH6Zm-aZKQMmRm6VHTz-bb1JeHtMp1_wYzU1p6zIbfPf98C54-1skbx7dpWz_L-jtbeFvsS4YhyOgmRcw_tlzleq4XU4Pr5Q1e-CgouhiccsxMZhpYXtORs5HmK18xefWHXQlCfbTr-hEx8OKLw4pnG0khjewtnDiOU2wd3xLQM43fukCK9oUdyyuHyRPyiS6YrEbFx1NOxI8H1fAAFFaSeku6ctOR0efH7QVllwSi7o4rMw9O6G5uNChBF8x4Eu7E-xg0pz5mV8UeSVby10yUlYriG1-WDrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=Yqr0_haEZ6gf8iHYwwjdSememnL8onRY4AyxHL9Ld3DItiHcLaz554Yen-B647uzLL5PyW-HibDfcPCI3XAq1HnKAnyLEsXgXZeuCdAxe6iG-71Oy0VfVx0Kj0sCXkf_H92jgUWQ6tkT2UUP0Zr4SdayfiM5HSceJ6dw3C1ZpFNv5qiINZ1Y99SC5esfdEi_IX_vzL4Gz6wZ9V2z75g_r9WeJ-6xoEz7giUkz6_l_mD687VPSSajORkYc86nnaDWSar_OoHxZqGf6-3Qq7Yg3sCMpkECSS2tpQhSeG-N2IeEUrrLZ8Habo2mUlEjekBk7lBJVa7wnTvehXU_2Gpnkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=Yqr0_haEZ6gf8iHYwwjdSememnL8onRY4AyxHL9Ld3DItiHcLaz554Yen-B647uzLL5PyW-HibDfcPCI3XAq1HnKAnyLEsXgXZeuCdAxe6iG-71Oy0VfVx0Kj0sCXkf_H92jgUWQ6tkT2UUP0Zr4SdayfiM5HSceJ6dw3C1ZpFNv5qiINZ1Y99SC5esfdEi_IX_vzL4Gz6wZ9V2z75g_r9WeJ-6xoEz7giUkz6_l_mD687VPSSajORkYc86nnaDWSar_OoHxZqGf6-3Qq7Yg3sCMpkECSS2tpQhSeG-N2IeEUrrLZ8Habo2mUlEjekBk7lBJVa7wnTvehXU_2Gpnkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=V5Bkta3_rpeoLlEpykARePi9OV_-3ThKpEHPY9Nc2AzptXK80lHqFW6baeaGSUXAR53akB1tgr_DuHND9saSCrMPxQ-yzCXxmDPe5zK_pKqzjwyL1ZCDSjzph8EgD7YAV9rSXx9f-2FCWjD5SvafxIt0ue61LAw47R5HsBRzvWa7Vol_KZ_RRFv2Egry6HBURpenCigjPprkHxRwIqLJbpH4Pvgesrtkj98lKdYyK-S31oqERKRpSMyudOCqFrZxfeUy540iolhGMeatAAR4-hamiqshZT7NE2sRCvvxRgQfJnB_MaduX1ZGeiMt0WOReZW7Kn_AbDkFEHm0LwaEHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=V5Bkta3_rpeoLlEpykARePi9OV_-3ThKpEHPY9Nc2AzptXK80lHqFW6baeaGSUXAR53akB1tgr_DuHND9saSCrMPxQ-yzCXxmDPe5zK_pKqzjwyL1ZCDSjzph8EgD7YAV9rSXx9f-2FCWjD5SvafxIt0ue61LAw47R5HsBRzvWa7Vol_KZ_RRFv2Egry6HBURpenCigjPprkHxRwIqLJbpH4Pvgesrtkj98lKdYyK-S31oqERKRpSMyudOCqFrZxfeUy540iolhGMeatAAR4-hamiqshZT7NE2sRCvvxRgQfJnB_MaduX1ZGeiMt0WOReZW7Kn_AbDkFEHm0LwaEHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aapkrx7fRsJKEn2XHhzQpjqMC6gDPBEigI2yejjFQ5s2DDIoshWMeJLVq5BKsgKdV1SmYwtBIRX5ensAekVVLFUAKJR053qsoj8DfO9Nsab7P6-PyR_L3rceHSxK-gMdK2RYUwwJf8GelR2shQpIHv3AbafNgGDa7jVbkx4y3hZIPzBB5FYIf-NRUXc3lRJH6WWyMS_eSTfsXh2JkXYZYW5jWh3BVZRMWjHa6tP2H1fpww2CMOlbZCjpXnjPtEbHWk3GajA8PID8Bhni6lAvUFMSxUnf3xPzts6jcpqsQthThOdg25SDUbos3rXe2517os6JxYtsqg_4HwxUPgFgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=SwzXo8sjG85U9tQ9lWnIU0lSDDWrzvR2e2-HzZNZWem2yAIK5aI81ncEF9xsHWFyn4_ezUrhZEMF8OyIhre3WuvXKMeY2EfIMc8GiJ4WVcAtiuHKBimJSRUxMZ5-hTHW9E0c8mufkHOOna79KlOa4LPAu0hxtWy_V-t-KOW0aeS8h3rIbO_wTxjyQFNJzIKva2C2SbK5p-xWlhhL69MAGfiygPYh-0m4sIECtAdvP9rPNJtqDthvN_1OUif9Epj9W79NLAvs88l7sTAjMZUgkTaBBDOAauUdA7TB0d0KvdcnR5EGE0RZm1kdQxYVe3mUodHpRViEzkDoQmHdA84sGRpy8jQDmYU4k7jbqpl4b-kwDRKJXJqhMZICid18MSCWXQfNdb9h9tuxshVmsT4S-U-fecRhIPHaPc-89OKs2ffkg40cr_c4aAiVYl4fKnBYYdS8ebpEqy3V77481Yhdg8ds6Ty_oJZ2mV43oUWmR4a0t8X9ldn36M25jVrGyRScZ06P-CZa-GTZy7Lk_Fsxkcv9EjMqDfG6qfY9XuORr4SuI8QOi6C4OLlAfEQampYWQ-0QXw8VFblhza21V74qMX4KBaMnY88peC_VGCVg9Gzr-x2vHQt-0dzXzP3Cgf2RW2lxiI_EvRUlJZcc2wTYDn0l-NPsiWTIPO9FVSPRa7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=SwzXo8sjG85U9tQ9lWnIU0lSDDWrzvR2e2-HzZNZWem2yAIK5aI81ncEF9xsHWFyn4_ezUrhZEMF8OyIhre3WuvXKMeY2EfIMc8GiJ4WVcAtiuHKBimJSRUxMZ5-hTHW9E0c8mufkHOOna79KlOa4LPAu0hxtWy_V-t-KOW0aeS8h3rIbO_wTxjyQFNJzIKva2C2SbK5p-xWlhhL69MAGfiygPYh-0m4sIECtAdvP9rPNJtqDthvN_1OUif9Epj9W79NLAvs88l7sTAjMZUgkTaBBDOAauUdA7TB0d0KvdcnR5EGE0RZm1kdQxYVe3mUodHpRViEzkDoQmHdA84sGRpy8jQDmYU4k7jbqpl4b-kwDRKJXJqhMZICid18MSCWXQfNdb9h9tuxshVmsT4S-U-fecRhIPHaPc-89OKs2ffkg40cr_c4aAiVYl4fKnBYYdS8ebpEqy3V77481Yhdg8ds6Ty_oJZ2mV43oUWmR4a0t8X9ldn36M25jVrGyRScZ06P-CZa-GTZy7Lk_Fsxkcv9EjMqDfG6qfY9XuORr4SuI8QOi6C4OLlAfEQampYWQ-0QXw8VFblhza21V74qMX4KBaMnY88peC_VGCVg9Gzr-x2vHQt-0dzXzP3Cgf2RW2lxiI_EvRUlJZcc2wTYDn0l-NPsiWTIPO9FVSPRa7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=jc2pVM_OkBS0qRObvQn9NQJdIE48L22A4hsQvV9FXsEJojE8ltkCYAl3OkvZm1IzchvuGlIlkspYIyn86mXSOHa3V4_VJKTLqHdUmIgq9at-Nv3DZGLl9N5Rzv9cwLgycSzqy60lMxA31lT__aYadcR3NZNy9INPUfwqYkwAaAJ5XAMtC5LwfmtYb3luICbjPPmGog8iR_nZP4CdHYwHiC429YAWaCZ3OjLa8lNb0aMYcrUs8JO9_5u3lnk5ywDVWUbQD8qY8qZFVFxoUqjJfbUJQz2jkeIeeLEqNNXM1jSsi4HfWl_Imol4BpoSrm4VVf4IaIgrfAsI50g_CBr_YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=jc2pVM_OkBS0qRObvQn9NQJdIE48L22A4hsQvV9FXsEJojE8ltkCYAl3OkvZm1IzchvuGlIlkspYIyn86mXSOHa3V4_VJKTLqHdUmIgq9at-Nv3DZGLl9N5Rzv9cwLgycSzqy60lMxA31lT__aYadcR3NZNy9INPUfwqYkwAaAJ5XAMtC5LwfmtYb3luICbjPPmGog8iR_nZP4CdHYwHiC429YAWaCZ3OjLa8lNb0aMYcrUs8JO9_5u3lnk5ywDVWUbQD8qY8qZFVFxoUqjJfbUJQz2jkeIeeLEqNNXM1jSsi4HfWl_Imol4BpoSrm4VVf4IaIgrfAsI50g_CBr_YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smtYqsdiCE2e6a7jWwD_FLZPG0Hbg_Mix3DJzv3QgwuO-pPZUJ0KDhCeeKW8YIYPHSV9j-3PBgEvnkmBC2CH85H9MR57H1s2WT21JqIPgMZoj-DWsflaUIY5mhjxuvEllBp1Y_yznPMVHYfNhuINOvyoAmg7aSI-KyFKlTbU7y85KJS6PNld445aZinQieE7LkxR19RXFWLnIm_9_ihikKqi_S0Ssr8wQgdiJC8NMxnqDTYVB2Vxe1Vlo2OvEIJICL5jIHYMVHVohh-35oh8t19GuKzFmzmc07e37_pt6TjjG2j25ij3fsIRBc4iQ38LYOYJ1bgRqB5fYApMCV7faA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=DQyj7jDaFaVSRbZMMOcIbZpkBdQK31mOiHH7QZsQFx0c3sOC4hWEXMKwLmzAlkvtWHFQvrLrfTcLjn8pyzwAdYXkg1gc598wSZu9ymiXRHRHLLbRhjtL8toQHyVgdcktEA_NN7Cjo3Uhno8cZ3vQ0QOiguzzO2XmX6WwMAJnLmjmUl0GO96H1bm9eJHfXIA8GF5llcEzOC7wxWlY9S2RMirq4_EueUNcYmximWHrZKM1NGzN6fHLKktQ2uB2TAtFIWassWs_PDlaC77TJ--xcgKzmk_T7-fkBqR5Dbcld8CYS69eGYAyu0CU4KiYvhzVfITCqwAWL7m1aKioP7Bpaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=DQyj7jDaFaVSRbZMMOcIbZpkBdQK31mOiHH7QZsQFx0c3sOC4hWEXMKwLmzAlkvtWHFQvrLrfTcLjn8pyzwAdYXkg1gc598wSZu9ymiXRHRHLLbRhjtL8toQHyVgdcktEA_NN7Cjo3Uhno8cZ3vQ0QOiguzzO2XmX6WwMAJnLmjmUl0GO96H1bm9eJHfXIA8GF5llcEzOC7wxWlY9S2RMirq4_EueUNcYmximWHrZKM1NGzN6fHLKktQ2uB2TAtFIWassWs_PDlaC77TJ--xcgKzmk_T7-fkBqR5Dbcld8CYS69eGYAyu0CU4KiYvhzVfITCqwAWL7m1aKioP7Bpaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr14Ts5uWlWMOBqCnHEVRdsBnQ9slJcZaohYc5PBrbUP9wKvoUpNMPmDzAyL0c66o2BivIgJstI6Xbea9oHy9xN6d7Uzca0gvmyRmPO59XEEb135eNxtmntwH0XLfonA1EKvCF1U8B10Zca_oVatr5a0MbpHp7ZeBU_tQhVvgMVu7ad8uP-1L81YbENDYlCe-mDxaUUPPZ-Z6fBjMSuAzLPayNS7waUz1qhoI0tG3AZuB-USwC_v9ke7LkOo5laaQIJG1KfpUS894ep4ZXGIL14Pt7hA8aGE9mNBVd_GypEZ5YnHKsfjkjIHvPxiVHQHgIRb-yUwKFSbvgEXCN_vDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-sBrcBLI5FoQXi3CqO60NX-iEWaM-6HKGbnv39yIvk-ZZoUvZ8QVcstV6Nk-xiVdkCSKJ6GQC-ksYvmx9rrqaMAPlIKC2jSkE5Xu56_NKvh_gL5hy4qxQMioMy3XBJNmEPx7NqgSUAiOww2e-zF-ejkXcD1BHCNNOPuOOB75LEEsPkL2JuwJz3LbezvGConjAOS_nbZ98bMFIK9oW26AX6XlqUKlVVduLgkSC2J4akr5zpaxiC7ENy4xf3aHZUlj8AYS-njnRMFiPBB83hojyP2fi0QjCuGBfBEnyR55iHy1LFvyAobnFl_3sTvc6RZOY2CgWkSXk0sdMxoz7JDEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=aLLXCva2UG0ih4ubbNoyTEMHcoRv1le-vvMdBcfQCTFW3mka4g5K_l-70IhECM6lQlsoplYrfA-UC7sReEuTXZZyWu5oIKVs1Fz3zuvzX10nbZhSahuXb65GuTS6HYyRyhibxfAhACX0ziKaIFETPO5Qg7_f2y1VNkmgED2GaZcPrk7Zrs_UuZ4eW_Ob0H7RpwUjjIhsHbm1m9ujXgk2ORyFDENaUtfn05BN79t05iNxrux_Wt476B4tI4ji8q6HSW2TbFS1yrzB3shCaPujS1RmAFd1tJ7p4uW_lJ86IX0o-kksmrc7wVCIJS3ms4ISJ0lPT1AthC1TMk-ot7U-sntcW7dlmSwiogMnzne_G0_mPuU4tmRCpvf-E9cSJk-1hPHc09tLbShXB22Tf8x0ehlvLSTeHbuX7jB1xrWMvWgOlvrDz5yD9j1m5rWFmIyzXseZ0tE4bUFv0S36tXbHCWY34B81Xl_WtXYNIYBZipyS8fl8tmNrSjeKPTNFR0RqTqHfgPlgZAbX8lUbeE_eq7Vx7a1aur2yUVs_rvRcrIGya44btvkkzPkDdseL6mvclSpBCdYARwhuFIq3R3spGuzCrcxxNhaSyO4BE8GrWHRIKk9tZVqKvg-jmYr_oDTkSM08JAYXRG_tp59MQAtmlcbthiqyeXy7HgxCg5-926A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=aLLXCva2UG0ih4ubbNoyTEMHcoRv1le-vvMdBcfQCTFW3mka4g5K_l-70IhECM6lQlsoplYrfA-UC7sReEuTXZZyWu5oIKVs1Fz3zuvzX10nbZhSahuXb65GuTS6HYyRyhibxfAhACX0ziKaIFETPO5Qg7_f2y1VNkmgED2GaZcPrk7Zrs_UuZ4eW_Ob0H7RpwUjjIhsHbm1m9ujXgk2ORyFDENaUtfn05BN79t05iNxrux_Wt476B4tI4ji8q6HSW2TbFS1yrzB3shCaPujS1RmAFd1tJ7p4uW_lJ86IX0o-kksmrc7wVCIJS3ms4ISJ0lPT1AthC1TMk-ot7U-sntcW7dlmSwiogMnzne_G0_mPuU4tmRCpvf-E9cSJk-1hPHc09tLbShXB22Tf8x0ehlvLSTeHbuX7jB1xrWMvWgOlvrDz5yD9j1m5rWFmIyzXseZ0tE4bUFv0S36tXbHCWY34B81Xl_WtXYNIYBZipyS8fl8tmNrSjeKPTNFR0RqTqHfgPlgZAbX8lUbeE_eq7Vx7a1aur2yUVs_rvRcrIGya44btvkkzPkDdseL6mvclSpBCdYARwhuFIq3R3spGuzCrcxxNhaSyO4BE8GrWHRIKk9tZVqKvg-jmYr_oDTkSM08JAYXRG_tp59MQAtmlcbthiqyeXy7HgxCg5-926A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc8YoR-9EpeR65vKGoRg2ijhv22UWecrmmmvYRGn1AjQlsj9uwFqFKBSdlYMZF5ejnxdDYsOjfk_0BUBTC9NOBh9UwmePnuNVCWiY0YfoE_pbztY4DqmVDfVki_EILHOAbLVhINOIT_STRFylwy88yOg-lj3mW2NR4rM_1d_EXNXuRp78X0shhEacOe2Z-5MquHh28TTl474HVBQap4e_xYQ_TnTd2KnU9ozG3-zygWlkAycLLQWAKRSUN4x1Whi6IVn_ZMtf4D3doy56gKgXnWdFyH0EC3wMxvaRbu7skEgZeh2yIRuQvldN8tLBpRgJqt42Tebxgvg1J4aPJClsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfFBsEsBBEhgEGLhFAVREz9KvT7KXYk_c1kR8x0WAYPrO93RRvCJFRZxBXyF3Fbtf6-HQes0iOPtL9cZ-7OdTiM5i4TPqJ0ShXkp6GbgcUfR7jvmpJGvU6aaSmgOgBJZT9JMbaKl1HOwFMxU2BLWWIJIoyux-4778Z5UbCsjNkEnjZYd6HHWkD4hztLhaTu1u26cc6gOQMstmIjuHduHFzh4_qphf6INqHoqnTUYpXRTSOFHyR-KI8Bw4oHHPKb54ihH4Zge-D4Emmm12ismbaYgheBFZqus9tTisVq5MSr35lKZdVWe0D6TYxGV3XW7pWaN778kNlBULRvDCh3K0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=G3z3Tj-84N-ulsW0Zcsl1wtQW9TPQRrwwHmcELrHmeBDN40LarSRhSOZEzpX1G5NadZu-tx3VumBqG-HLq--cYRWjDz59iZiwn-xsbCFboU4gxsTx2eYj7B5z3ZfQHhpxjSsy15PLdT0vUEvyDR6XuVBYdJgO03TSH3dMQ0ZZzMgJf3Nt3eCyh1ca758qmULaMNwSZ-6xpS_1-1eYY5AB5u3z5LTzqwB39pDY9KYEHEPzmKhZc-PypBcIXbtiLXETpZPXUzhYduOT0j-YsiwbS0qsVyfXk6eoOgIaV2OVFh0ZHfCsggUYeqniKn2nV6Tk0BOhfuDwPvImUrTk9JQHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=G3z3Tj-84N-ulsW0Zcsl1wtQW9TPQRrwwHmcELrHmeBDN40LarSRhSOZEzpX1G5NadZu-tx3VumBqG-HLq--cYRWjDz59iZiwn-xsbCFboU4gxsTx2eYj7B5z3ZfQHhpxjSsy15PLdT0vUEvyDR6XuVBYdJgO03TSH3dMQ0ZZzMgJf3Nt3eCyh1ca758qmULaMNwSZ-6xpS_1-1eYY5AB5u3z5LTzqwB39pDY9KYEHEPzmKhZc-PypBcIXbtiLXETpZPXUzhYduOT0j-YsiwbS0qsVyfXk6eoOgIaV2OVFh0ZHfCsggUYeqniKn2nV6Tk0BOhfuDwPvImUrTk9JQHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=KpykItr7J3Plbc7Ym3bo6lxI2hiBD36QqK2yBU7-5TDqJPTomH9JunVnro8VCev9p-ETf42aYFRl6-6GZWumMet1B8xLbXd0vxJPdqRnnpxdz2IBDMyD3JQ74c6FtdBqUUqhTyhT26lw4HCWFzdXnWxuoJYKkMUGzr915oZP9JBLjeNWZHEXsp9xPfpQfAPv_SKezVrx0dSJ3dSgqWKxwvHucEzHeoLKvNW-xmYMbdGjq-QkxJFAMx3eRyUn6HNnBcDNpvZVUdBGpGAxncLh2JYcuRoo5UE79D5eUGD5FNN3CtDKefRzq2YZ3y5cG3Gzs-UJDWLkApu_EGz1af2fvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=KpykItr7J3Plbc7Ym3bo6lxI2hiBD36QqK2yBU7-5TDqJPTomH9JunVnro8VCev9p-ETf42aYFRl6-6GZWumMet1B8xLbXd0vxJPdqRnnpxdz2IBDMyD3JQ74c6FtdBqUUqhTyhT26lw4HCWFzdXnWxuoJYKkMUGzr915oZP9JBLjeNWZHEXsp9xPfpQfAPv_SKezVrx0dSJ3dSgqWKxwvHucEzHeoLKvNW-xmYMbdGjq-QkxJFAMx3eRyUn6HNnBcDNpvZVUdBGpGAxncLh2JYcuRoo5UE79D5eUGD5FNN3CtDKefRzq2YZ3y5cG3Gzs-UJDWLkApu_EGz1af2fvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=DlgHy_ZWDAjU2XN_ERqV8bZzlEuamPygY2BQVhvSmfi9oogC4MmgZz2WzTAM9Aolyf0NCVK9PeDx4zU7YDWA0JTBIqI5N_aVR831Yn-GpkEQ5BaVCn1M4K46l200dUY4h4LQRtH8rIiB-d14BIEDbhF9kh29b39WMl073JTj2jgHEWS0QVCbSJLFjxV77EA4cDLW5YOHEW-Ytc36ebjXRrUmlorxnwK2O4nP8gIHrof_mIRlcjMVT7PJtVSVu4qkxHLGXIZsmHNzo89x9Ow7Sc7MZBwloRBu0OF5HB9JJFjDKrsr5FHSr9fPCEeR5Aaro5FcpaAg4S1HAqA5C350ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=DlgHy_ZWDAjU2XN_ERqV8bZzlEuamPygY2BQVhvSmfi9oogC4MmgZz2WzTAM9Aolyf0NCVK9PeDx4zU7YDWA0JTBIqI5N_aVR831Yn-GpkEQ5BaVCn1M4K46l200dUY4h4LQRtH8rIiB-d14BIEDbhF9kh29b39WMl073JTj2jgHEWS0QVCbSJLFjxV77EA4cDLW5YOHEW-Ytc36ebjXRrUmlorxnwK2O4nP8gIHrof_mIRlcjMVT7PJtVSVu4qkxHLGXIZsmHNzo89x9Ow7Sc7MZBwloRBu0OF5HB9JJFjDKrsr5FHSr9fPCEeR5Aaro5FcpaAg4S1HAqA5C350ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8vbvd4r-LjDbQbpWO_QepgCBt1n82NXyF2kBh7A40ObopqPz8xL2e9jxNnJ0RyImbkggM9I2ShSKrpadjkLCgndhnMZWsD65dK8NjHE9TBeP7K10ic0O67AZpcsiY1D1e6eozPDI1MReP2PszRkQcFVaInNaYJpcFu3ZInnEU8dbw-APHDoGssYP52UWJKuJq91B2PGPWgF-whT9Laq_Fw94NxrvquLYQ0LuaeaWX0etOoZcpHVaYzCBJY0bPGbWYcnkR-wbqzJRXpiKWJfJY0RjqwGviKwupKikFee9xZ_Ttw1UArevSnwfn_EDIFZytVJCGXa3K5Rx1nevR9lJw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8HkWRdGe6dYDKCuEhmULu-nKVZJ4cLLOneSv0SjbEVmyGMzynv-mX7_RQcA0Qn6PgdLuFpPcUqg_UzZmDt6ZgBCTpP0RJvG_5USi0dd_eNZ4gCUOQCKQzDLjxKzUKFt4m0FQklIFkxFZSBp6WVr3xJj97aBPK9pFQJK1xo4kkYFAkvld0LYUrtrkmaGLEZlUEKn8zxpWlH8eC5ttC9cjKi2Nn5hhysx4-aSqCMWFk-bYySMbUuIYNIS0q8kW48XtnQEmVBB2h7KzyQo4usZmWkKZPhUWxP29jmPx0H6vFjcdTmt2GlLATBmgyaouVv85Jhs3MKGUh5ZNjxzBJ8We5DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8HkWRdGe6dYDKCuEhmULu-nKVZJ4cLLOneSv0SjbEVmyGMzynv-mX7_RQcA0Qn6PgdLuFpPcUqg_UzZmDt6ZgBCTpP0RJvG_5USi0dd_eNZ4gCUOQCKQzDLjxKzUKFt4m0FQklIFkxFZSBp6WVr3xJj97aBPK9pFQJK1xo4kkYFAkvld0LYUrtrkmaGLEZlUEKn8zxpWlH8eC5ttC9cjKi2Nn5hhysx4-aSqCMWFk-bYySMbUuIYNIS0q8kW48XtnQEmVBB2h7KzyQo4usZmWkKZPhUWxP29jmPx0H6vFjcdTmt2GlLATBmgyaouVv85Jhs3MKGUh5ZNjxzBJ8We5DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=HPtdzn8lPyN1K12a9ScMCtpbxhbN4wUym678WbHXV-bAmDhvXPYGT9etK3-F0--KctB4uJG7YABuLKp6brFiFJ8Zm1b4mDruxV-RH_pd5YklFT3ujujyt_ABYIiL5tMglAVZGb1ETHaCFFQTYItFri8aWWQGLKOem9CZNreTxS1_jfynjpOfhJs1H5zTloMPVy2mZqpO2POc7LJgN4MHclA5D2XmDz41-lhx0FmYpgomJ1Zb8DUhRtuBQFMFHOjznblFHPBr4CddCRiBYFLBWeT75eYYGtpdFMSOpqiR2yxPUmpvQ1HqyMPi1JZGcwYKg2xKNbncvtHT-KNA9pxyaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=HPtdzn8lPyN1K12a9ScMCtpbxhbN4wUym678WbHXV-bAmDhvXPYGT9etK3-F0--KctB4uJG7YABuLKp6brFiFJ8Zm1b4mDruxV-RH_pd5YklFT3ujujyt_ABYIiL5tMglAVZGb1ETHaCFFQTYItFri8aWWQGLKOem9CZNreTxS1_jfynjpOfhJs1H5zTloMPVy2mZqpO2POc7LJgN4MHclA5D2XmDz41-lhx0FmYpgomJ1Zb8DUhRtuBQFMFHOjznblFHPBr4CddCRiBYFLBWeT75eYYGtpdFMSOpqiR2yxPUmpvQ1HqyMPi1JZGcwYKg2xKNbncvtHT-KNA9pxyaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHhLuch1bGtoM7RLVtW_oBUw4QP2IFLzpyX6OjHhPSClZoeoDmDrTx8UQBLU8xnEXkcu8tcbWXsQAZZiWH58VPMmbSUL6shpuhaeYsgdgj62Cg56VF66FySmw3N9jS2_95kNUp1cGDxWi1OLhk8rFjfTC86wHEt6hh35MyvqkkdObIEyb3PO4I6Uy7SWUyFDJOtW2tamXbKNWFitCNRi-WBVf7s55NlSwUU-woMcEDEq2i07NdvIKQD_-H-2UrjrjsHz3Rz9QsyX9DTTNxCBZTGXZvLlNSSsv2FSXnhzkkAzkkQn0-yYWVtrmKEXMRgVsIVOU2PDWIXbpysrLf2eSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=CzXgN8T4OOK40wq9VVrHLRMjcJX5Ofyrjmnd_1Uuam-AR8Cdi9oUwArYGaTBjFZzlCW3a_mAzqsjqg3ha5fQOaFM4ZiDvXoX3zxh5lMBPKZYGJDq_8iIKQgUVfm07JS9utMZZU9XuSUkfHP1tFf14jjSjOYRHmb0qHjfIi_L-F4p_y21uXcqpwoxf56HSDmYhdmsEFoIVvo22dS50U71VxyVMlW6HFeCBpMPk9c8HaWOXEwdg2GRM2Rpl-0z_QPmg5zdvQiF99BmUiSQ2HpkUPWsmC0Dunqr92KxUO3-ml6RUgcg8EPGdwqXFCei7jV864UoLDtUG9RT3x1Ui2Q7IZWDn8nvzGbmW6KsEjO6AmAwe1jZRtt6-7x2Hjb3QwSM8504FHAK8aFFSG1cwIers9-Qi8a73CYWfq_4c4K4ZgPISVpQBxUcsX86XiW7OqJDnPIFB1gaNO8l7VCU4EpFM3LgFG-GJLmiRdavLz-U9p0Xjsq3IImMc3Q_I_yTC30oUCeHJjLhEvxXJ9CADbq46zuKX7DaXvxGclqUCvlWFkOc_lPxqmGiDfSR8jp9WMTAVJbgAhXISC6h5i1pGJyhldi89AGgYzj_5b4dEoGVynEjkUIGsuI_3iugWvTT1GxajZv54HVndbWjHZRiti9w5Gn_gKDimYZ7sY_NiaOmOfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=CzXgN8T4OOK40wq9VVrHLRMjcJX5Ofyrjmnd_1Uuam-AR8Cdi9oUwArYGaTBjFZzlCW3a_mAzqsjqg3ha5fQOaFM4ZiDvXoX3zxh5lMBPKZYGJDq_8iIKQgUVfm07JS9utMZZU9XuSUkfHP1tFf14jjSjOYRHmb0qHjfIi_L-F4p_y21uXcqpwoxf56HSDmYhdmsEFoIVvo22dS50U71VxyVMlW6HFeCBpMPk9c8HaWOXEwdg2GRM2Rpl-0z_QPmg5zdvQiF99BmUiSQ2HpkUPWsmC0Dunqr92KxUO3-ml6RUgcg8EPGdwqXFCei7jV864UoLDtUG9RT3x1Ui2Q7IZWDn8nvzGbmW6KsEjO6AmAwe1jZRtt6-7x2Hjb3QwSM8504FHAK8aFFSG1cwIers9-Qi8a73CYWfq_4c4K4ZgPISVpQBxUcsX86XiW7OqJDnPIFB1gaNO8l7VCU4EpFM3LgFG-GJLmiRdavLz-U9p0Xjsq3IImMc3Q_I_yTC30oUCeHJjLhEvxXJ9CADbq46zuKX7DaXvxGclqUCvlWFkOc_lPxqmGiDfSR8jp9WMTAVJbgAhXISC6h5i1pGJyhldi89AGgYzj_5b4dEoGVynEjkUIGsuI_3iugWvTT1GxajZv54HVndbWjHZRiti9w5Gn_gKDimYZ7sY_NiaOmOfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6nMIwOR4GxuxeiaLm0Vg27QgjbBS_4HesMehth0D22VJu5HcYBL-H6f1CG8hnSLkkQ_XJXLkDZ8w6ZdDoDLqvzZBbbTDalp8e3ClzzAKoSpc1BanZ6ulKLXVaUoTBRppNxB-M5VrElFZyBgvdLbXAT7lI7o1iFXNfvcPobW19j2k1daDYKcxGRQD0mJvD7VxIKgvrXveIn29q7I3I868NaHjkzuik4tcP8gIHrPLPvfZisXHJHzDvh-1hMf57PV6gMy8TNv5Vo9IkAkj1RTDj8BeIGYJrtqTbvLCiyFBEKhCs5z1mlXRUV0E3mFix-yoArp1l6sqLViESkW5Xw81g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=S1fGx9Tp-_hyWy221RNK7H5DGwmjkPipJ6T66pRSv5J-zW5a2zieZi3WalwD6R2pmxXM838PTrPjnn8n0PyDj36ERv-_VI9MQ08efp-6HyG7NGTiWg9klV3YApvXKc1t0EXTM6NsizHGHE46p-O9UCAaM2wbpy_HFc9Eda0x0uvzybwvWw8MhsGu3qrgrJlDzGl7Jq3UracjXDJ3dtyuFpUYeh9Oz8e0uSMxrw0SsXqAflqI_ZlVh43Ddfahgwj0iqoFfTeBkO5mSIj8XvrTVzDthoXFhzXLaipb3bE7xCj-jtRUmy-linD-6Jsb6ma0Z8MWFslxlg31Mael9vDYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=S1fGx9Tp-_hyWy221RNK7H5DGwmjkPipJ6T66pRSv5J-zW5a2zieZi3WalwD6R2pmxXM838PTrPjnn8n0PyDj36ERv-_VI9MQ08efp-6HyG7NGTiWg9klV3YApvXKc1t0EXTM6NsizHGHE46p-O9UCAaM2wbpy_HFc9Eda0x0uvzybwvWw8MhsGu3qrgrJlDzGl7Jq3UracjXDJ3dtyuFpUYeh9Oz8e0uSMxrw0SsXqAflqI_ZlVh43Ddfahgwj0iqoFfTeBkO5mSIj8XvrTVzDthoXFhzXLaipb3bE7xCj-jtRUmy-linD-6Jsb6ma0Z8MWFslxlg31Mael9vDYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRBgUmPZWtuilmyTwxPD4O9jqpfFaVNZ42JkPe9UbUpb08Hid22Xcx45LVKD592FU-ytSR1tTNvIYsPlDFCFK3eykIyIhsKeu3bka6P5luA67eHKCXbDrsV1NNvYkk3SsQz6c2YoUBIPtyditVusdx-EE17du4E9JI6A4qSi2hS8-WEJIW6YVGONTn-3c63rxWf6ju9Y2NfZvGZ8HFMGiwSz8PRNuR4zjyahgajRMcklsJvfIRcWkMU76pCdrLP2EqPv1LeDkbTHD7CYsUeyf_Q9YM2ONNiPYX2WZKfSL5o5vFi2MA8XBM7UHYDgJa_4zmZs-b4Zy46KImCod1sO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGCOwAuGwkPdraIRWh2hd3-wLz8P66VgzaFMDVlA5oaAJoP_bo458c7bU6NgxRRvniecACMgFcJwy9me39FIMa0Prm5a_MWywGGSI4nsI9DdWpaohAJLT0VjCfXqpe6OrwLFBtXPybkv2XP_yuehiG45_AdaiG6Tzl0JnQmr1OklHoXyVBJIsPhrQqHt7Fvxh85n92YWxaaEz0OUdXX31ejEqD0KZn7sPjmBgbTFf-HkWwTF6U_4epIl_bBvU0pOQ1sqrbt4YiwHnnpPuxAC4dU8D5JnnVxCkbLDGuMsZb6OvdJCF3aSCb8nC7XEOYeJ5sLoizkXQnLtH5VvN-K-dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VabNQ-pfCr65QZH4HniCabIErZmoUsQEBMuqwYu34bVqnHuEmx0qqXkeKnuQZIw-aT5nQUSoniZ2fH5oMpmxIJVNbqeXlMMEmsc-Q0W4W_BCqy4SF3PHTI3_uljtum2wpsVI2beXfu0WU_fw5a6OuaVRyhI6ExZ-78tfUrsFeT-48bShlAGnRtkyJNwy1qY02PjyRUAa1HaDyydJMCxWefdrl2cD5h-KGmQHpR4tADuXzSPW9hBBPTXkJUM8NKt11Hcf4Ji3c-SsWfSQ4Q395cagz3_JmwJF8vaLwNcn9NUHlqKK8ZQLMpoEVtCgONhajBqRbI8jbp0_i34TOqo7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ufaQV8-uwrEcVTghzSYNzEnJVdc26u73sILLzyVStKk8Ru6bd7I7thJmZerRlQVt9mr1BrcAZQC07KfDgUUtwndpZt8_s6MLfKFQEHaWSM4hm9HJqdCme_--n6nVqjRQl0m4YIqMeedGzvyZBNMRI3JhEnWlpOQg_IVt7ce82ZLA-LKa1AracQ6faC4HgYYbHY-FkOmxrjnyPLnPf8kEEa0xuW4JSeGIK-S2chF6FkjMQ93z5_y0FpVvMXFHETAW259V7lYkt0Cu50SdQKKe2KfcU_nFlyIjw5B7BMkI_IqMk6dPPXGqWNGE6Hpe-eW0GwBy3sFgynCygke5k22jxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ufaQV8-uwrEcVTghzSYNzEnJVdc26u73sILLzyVStKk8Ru6bd7I7thJmZerRlQVt9mr1BrcAZQC07KfDgUUtwndpZt8_s6MLfKFQEHaWSM4hm9HJqdCme_--n6nVqjRQl0m4YIqMeedGzvyZBNMRI3JhEnWlpOQg_IVt7ce82ZLA-LKa1AracQ6faC4HgYYbHY-FkOmxrjnyPLnPf8kEEa0xuW4JSeGIK-S2chF6FkjMQ93z5_y0FpVvMXFHETAW259V7lYkt0Cu50SdQKKe2KfcU_nFlyIjw5B7BMkI_IqMk6dPPXGqWNGE6Hpe-eW0GwBy3sFgynCygke5k22jxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8B7sIoUw-HQ5UMuaMmfdyCVFmEZ6aRSRDz1wxbP2TFiXZddW6TXn_2q9RUEhnIHWy8BN4HdGOKtcKaUVS0XtNGpaVtZnbY5fNm59AGA_0BokAqFQe15ylEDs7jalep4UM4wy2EaXikcL2WmdT54AXUjdZ5Cnvv7SoS1UUa44ZS9NF4tVBXO6igO-4Z-YNsnf2gjAra_jgNG6b63WxxKEow77F9fspYT90PHCBLSRLRmS4ogevFXWnvOJ-ddCXXbWt4niUeyyJPr5TWklX648Q_sR1xfrWUO-bwA2P0JGuN2zP7qVVdrX-S3lpR0xDxbfyWBl6zUDMCt7cwv3kTRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFKPMLZDJs9hCtn4bW4KBrC36QTNOOKhQDXfbMlZiSO0-euGt47w4QHQhZxvjof8_Sq8ql2-eO3CvhUhjmgduQemXjwpuGTBfetnDCVYGlyeAWUQsVwgIXRIWiqY29LhURCbRd1cPV6vMKaolbooIY8azbZd-rhfNc4ITYKv4d0n8hbOXacu8hMs57itOuwlmjaf8b6uy3d2V4FAcCkO8e5sGIH7MgapCYQtnryPFdGidjnjH0FUc2GsjIVF2AmLQoiw222k6szKGaMLaGR6VHlDkIViqIHcydNFbll7C4yXfFS9G2WsBdhaYtOeisibB5v0AbWfojg5T74-An7sOZPc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFKPMLZDJs9hCtn4bW4KBrC36QTNOOKhQDXfbMlZiSO0-euGt47w4QHQhZxvjof8_Sq8ql2-eO3CvhUhjmgduQemXjwpuGTBfetnDCVYGlyeAWUQsVwgIXRIWiqY29LhURCbRd1cPV6vMKaolbooIY8azbZd-rhfNc4ITYKv4d0n8hbOXacu8hMs57itOuwlmjaf8b6uy3d2V4FAcCkO8e5sGIH7MgapCYQtnryPFdGidjnjH0FUc2GsjIVF2AmLQoiw222k6szKGaMLaGR6VHlDkIViqIHcydNFbll7C4yXfFS9G2WsBdhaYtOeisibB5v0AbWfojg5T74-An7sOZPc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=r9WcUEiEMC86sBIZAIQQIBvosg7ktKl5RSI8QCaS4jAuKgNAm3CkrBi1BzqTh_sT3SobKEyxHgo_ZNz2okkT49ms0CWNBhCF6eDczlbf_EEsCnEjbWF-xK857j7doZ7lxwR75aPOd2-eXckZkAl3MYVnszkahSM5u8n9FE52gBg6vJgF2lRgPMAqjRF_9yqtPPhcJa1aUoCsMi-t1o5i47PaLQPaQcLnkJbDNuMLBLt9tUR10xc8CxP54SGXbSN8qJdGilEq4DBGAcQHA-1CJFO61QFZMQontSoOreOA1gzt0i4OBSuY5owJU7c5E9z48tTBG_DdGPq_bZOkzEa7Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=r9WcUEiEMC86sBIZAIQQIBvosg7ktKl5RSI8QCaS4jAuKgNAm3CkrBi1BzqTh_sT3SobKEyxHgo_ZNz2okkT49ms0CWNBhCF6eDczlbf_EEsCnEjbWF-xK857j7doZ7lxwR75aPOd2-eXckZkAl3MYVnszkahSM5u8n9FE52gBg6vJgF2lRgPMAqjRF_9yqtPPhcJa1aUoCsMi-t1o5i47PaLQPaQcLnkJbDNuMLBLt9tUR10xc8CxP54SGXbSN8qJdGilEq4DBGAcQHA-1CJFO61QFZMQontSoOreOA1gzt0i4OBSuY5owJU7c5E9z48tTBG_DdGPq_bZOkzEa7Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=q97iTR_-2Yta2Bjy5GOXjw0o5DbDJgtCRvpXmqO6ypTaLmJZUg_Ioieru_yGYbf1jdyxXpdyx8glrnh3-8I07rT65kZzMj_sGri8VJhCJWoYQGct6cuFjDEK1CaEaNeqacgDhoSrWfm9aVtHgmZbxne_sxgwBtc_O23-6La8uZDgtXhR7SMGY6Dea0xBbEXSI0_HRr9ASVQavEvC6Est0CT6fLhF7iOKL8_rPBdwCTGDdacao_JL6pOfHi5173epTcxXPKr362JFRyrvyKGMbjwOdSxODr_TpTRc1o1zv16RWEFx8mleoXDYd0w9pqXIxUThdb8_2nWojrN5_K7FDG8DuYNJXPR0GyrOkOTHw3w3Wlg2B9C6YCRfOZn7mJjOJHD-_Bb78OqTceXQJ4hWbABOdGFtod2YKpwGzN-stdMSGlHc3FQF7Lcn4BidgeZOzoTY1rmzwXsKjJrnQ-qG-d_WuZACWVnzDsRqt-2g_PvSjxwBKhG5RgYHKfVPSFzHk4hKoZzWF0AoGTQ8Ia2CNsHTGmrdZalM33Kk5bMLEWgb2Wk7dWBi-xoCtfr4PpJKEegq58P2bBASeM33o4BUosjnC1KnQl8xxGwzXI6X6QYcnu8beM2eE0RDZ3OkV1tuM0ji99whHJ9ku0qk1-JfhSIrB6jBiiLI6ImFiSNFguY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=q97iTR_-2Yta2Bjy5GOXjw0o5DbDJgtCRvpXmqO6ypTaLmJZUg_Ioieru_yGYbf1jdyxXpdyx8glrnh3-8I07rT65kZzMj_sGri8VJhCJWoYQGct6cuFjDEK1CaEaNeqacgDhoSrWfm9aVtHgmZbxne_sxgwBtc_O23-6La8uZDgtXhR7SMGY6Dea0xBbEXSI0_HRr9ASVQavEvC6Est0CT6fLhF7iOKL8_rPBdwCTGDdacao_JL6pOfHi5173epTcxXPKr362JFRyrvyKGMbjwOdSxODr_TpTRc1o1zv16RWEFx8mleoXDYd0w9pqXIxUThdb8_2nWojrN5_K7FDG8DuYNJXPR0GyrOkOTHw3w3Wlg2B9C6YCRfOZn7mJjOJHD-_Bb78OqTceXQJ4hWbABOdGFtod2YKpwGzN-stdMSGlHc3FQF7Lcn4BidgeZOzoTY1rmzwXsKjJrnQ-qG-d_WuZACWVnzDsRqt-2g_PvSjxwBKhG5RgYHKfVPSFzHk4hKoZzWF0AoGTQ8Ia2CNsHTGmrdZalM33Kk5bMLEWgb2Wk7dWBi-xoCtfr4PpJKEegq58P2bBASeM33o4BUosjnC1KnQl8xxGwzXI6X6QYcnu8beM2eE0RDZ3OkV1tuM0ji99whHJ9ku0qk1-JfhSIrB6jBiiLI6ImFiSNFguY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=hMy5NvoQ0td6X9ajsp9e8OFyuXcGO7ifUmIdDHMGDHToB4LwP3enBwmz6g_SihyS3n91dSOHh-WmT79AGtdn5RQ0L649tvyJgM8fvRuqEm3ZCLYNZKNik9MVJkhOLD0_HuLggGVazSmDld0C121g56BwZ-BYEFwztnRr2ef9LOLGE1PFKV74q6b2PADpxlOBgDlbZSTRs_nls7tvnyrOVXvFbVbb4woribEpNq0sGzH4xfosYN0myEX5fLoLbcdggM9LMBxfQYj5GMlu1PsB-K04mn6U20jBSuQeCOTf-mDZvcw_vE-Vz_JJ3rGSbYug33n9_9PWwal0PxflSXhHDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=hMy5NvoQ0td6X9ajsp9e8OFyuXcGO7ifUmIdDHMGDHToB4LwP3enBwmz6g_SihyS3n91dSOHh-WmT79AGtdn5RQ0L649tvyJgM8fvRuqEm3ZCLYNZKNik9MVJkhOLD0_HuLggGVazSmDld0C121g56BwZ-BYEFwztnRr2ef9LOLGE1PFKV74q6b2PADpxlOBgDlbZSTRs_nls7tvnyrOVXvFbVbb4woribEpNq0sGzH4xfosYN0myEX5fLoLbcdggM9LMBxfQYj5GMlu1PsB-K04mn6U20jBSuQeCOTf-mDZvcw_vE-Vz_JJ3rGSbYug33n9_9PWwal0PxflSXhHDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCG-Qjcp0wt8iz6huZRoHQzuEkNopUPJ6V868JFUVwR_h1ELlqLBLMAr-OfpGm_stcsBSQuTaJm2deg-XuutSzMZKrNO7Rhv3oPkGLWP1TO__siusjJWjMnzz4XrLlo3RraS2fuupsd4B5svPdVnV2IFM5g1w0bPXl4silSBL-swZ1FzXTQCwklHnNE5B7-bv7Mkt5c3oRY9_rdceVenTx1XPEJFF_Srep2jnZzogCsOu_7JlliokRWT8K4ouTqqM5ZklvhGSvZj4DgxdDLIuL6i_ZQjO9Qw_MNnuSE4tk92rVFLGtUzZpKaAS02qkPvxBQO7gdp24epA6pmZvb8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=dz2oCnggFbXIgi0sRvdMatsk07XjRvlM5QU6woS4IXH1e1DzObeJcyunUExITfTkJ7AAd4vpJ_hocr3s0cirYkc1yJx0WcBtWKgMHQEVtQB9wvNkTXUn_5Xv0IiB89n5I4ehrk3DC-SLsV_X7rIacNdALmTFraz-Sjway2fPRo-eMxZf0D5lz000g667pM3Z_gb1lIM8-Zy3dH-7uWedteQfdoiU3SKm3Gl-nkHhlhykWnJLuzFgkKa1TNRd46DlSD_7vi9IxIA9IVbUzcrbW4gYn6i6VzrbXEj_EnsqlewOJLwAMUk4-g95us5OtFQPiTZ6A0tm7bbqhnro6lRsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=dz2oCnggFbXIgi0sRvdMatsk07XjRvlM5QU6woS4IXH1e1DzObeJcyunUExITfTkJ7AAd4vpJ_hocr3s0cirYkc1yJx0WcBtWKgMHQEVtQB9wvNkTXUn_5Xv0IiB89n5I4ehrk3DC-SLsV_X7rIacNdALmTFraz-Sjway2fPRo-eMxZf0D5lz000g667pM3Z_gb1lIM8-Zy3dH-7uWedteQfdoiU3SKm3Gl-nkHhlhykWnJLuzFgkKa1TNRd46DlSD_7vi9IxIA9IVbUzcrbW4gYn6i6VzrbXEj_EnsqlewOJLwAMUk4-g95us5OtFQPiTZ6A0tm7bbqhnro6lRsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=UI2Nt-4Mr8jSEv8wK4I4OKMg0ap50TExvNujSx3yauzGEBOOQ2fUw6uXFfcaQNLmgFGPUb-O_aIcn8WZbd7XH7Go_S0BqbN8GRlzx6JtdQv-RKivX3HrAuph6OjFy6L7l0I0hIXjbW7IbKV4t__SmZ9f5rXrDp4Ut43-m5tVBNo3sPb-BtoPkok76VoW8qCM_xdlM_3zk4GL8gpF2MmuV0rgOn12mQrQ9VMipUx7onTt6PdAiuqsNolFowLTaJl6QJTAPKxAUjtwMSfFjqpsb3ftpWyR800BBz8ZxE7oX_qR0E7K5rqUEhHHl5Vif5NjDd83TQHo_etIhqufTjkRZVt6xWS3QS8YNjA97akSeP3pfDKBmSUv1GFPMR8ACg3WuaOgxfbz2NkXcZO3R3MiHS7z0c7H0J3R3JtZVwECIewUpJwfvgMDliq7esJhv2gum7mlzGL4VzxzUl63e1edUuG_X4UMRU_IYCYK5qAkXEiQJk6xfhyfTDGopsEqryYiPXpF4jdQGmRhMnOunbsvi9v66-jU9myc41sZVv2Gn0IQipKvrv2C9BTEnJcgWE2rl70SRkfNMxAgD7FnIbanpvpaJ8TMSlCmoEk2u_QcI94cjwUSWiZIuYY5169IiVE7t4ScxW5ffYMbq4S9cI3FXCfBVoAqIL_CoQeSFrlxKho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=UI2Nt-4Mr8jSEv8wK4I4OKMg0ap50TExvNujSx3yauzGEBOOQ2fUw6uXFfcaQNLmgFGPUb-O_aIcn8WZbd7XH7Go_S0BqbN8GRlzx6JtdQv-RKivX3HrAuph6OjFy6L7l0I0hIXjbW7IbKV4t__SmZ9f5rXrDp4Ut43-m5tVBNo3sPb-BtoPkok76VoW8qCM_xdlM_3zk4GL8gpF2MmuV0rgOn12mQrQ9VMipUx7onTt6PdAiuqsNolFowLTaJl6QJTAPKxAUjtwMSfFjqpsb3ftpWyR800BBz8ZxE7oX_qR0E7K5rqUEhHHl5Vif5NjDd83TQHo_etIhqufTjkRZVt6xWS3QS8YNjA97akSeP3pfDKBmSUv1GFPMR8ACg3WuaOgxfbz2NkXcZO3R3MiHS7z0c7H0J3R3JtZVwECIewUpJwfvgMDliq7esJhv2gum7mlzGL4VzxzUl63e1edUuG_X4UMRU_IYCYK5qAkXEiQJk6xfhyfTDGopsEqryYiPXpF4jdQGmRhMnOunbsvi9v66-jU9myc41sZVv2Gn0IQipKvrv2C9BTEnJcgWE2rl70SRkfNMxAgD7FnIbanpvpaJ8TMSlCmoEk2u_QcI94cjwUSWiZIuYY5169IiVE7t4ScxW5ffYMbq4S9cI3FXCfBVoAqIL_CoQeSFrlxKho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqaj_RBfqmoolvUU6a4gOfjcXvHmmgSgUFK2vGKswxR84gG1PMG5s5VImWx9FdFFwebmo2ePsfiqyxPo_JC0UmQ-xUS4HIsexqrUHnACw6iFVJJXhTb03M51PzXZmaRrqmqWy2hhOpIfDR7j_40kW3gdZjWdHkXqfF1eac3osFDVSLR0tGsCPWBYyde9RUpAiO_igP3YZ2W4XvqV8rk78WmCr6iWbdwX7fjFmWXQ6MgMsicHWBcq2bgWfcY3-YEfQdRcwJrqWXR_3oyk2MomUMitMYP-ZVrbPotQXtOVBq6U694H05e6ZmOuYmZATGEA0oBbig4JD2teh5ufIp-rgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=i5-9rls-TCp2mVH5dGFUvUCMaO49KGCEpZTT33tBNA4FPVqpp48tcqrjS7ytabpShgmJZXpsfSQPm5yIBhgjwMtIi3-plE0WGuru_NUqGW6bUcWUX6wFZtTDReawd5nKnI08wzQx29E6YhzShZvYPQZpfi1iH40XeEoXwIZZ50rCM_WXsdrQEp3xWWcXvWc7B31ehHGDlU9fT1k-1_MMUz0J7zcgdCwpkO_GixpZolkb5cJAUmP-hC4LzK0rp4V4xZeVO6cmC-5LqhoDzLCG1ZxlN__slNzPAof2LTNOc3qz4EAVKvDxlpySEI7Qi8WzffKTnWQaMJfpk0X9DZhQbkDHAPdV7_B3pTylJZ4SAN_Mv6YssBKpDaIm2fB83TYodlrIR05Jd00DRjLZcEM82A9jS8O5D_yCrjSRLQMKc28j-NkPW7FMPpf9b-c183teVZf14Tge4ZiY6ieq_CjoRpO_WOP-DkXNOS2uEOHuuDBsvcmYxnubwENOiLmkONFo8cfU2CJEAwd78BOyIWo9CDZ9yKtDIupYHXDcMId_MAo-VvhXVj_KjDn-6r-eS5ua2QwYdQUH47QfMjhFRUb1-g0OLajYqheq40fB9PljpGf66TXrd3z3nSxWgDlKWpiUa_XFQkTLzfZcgwhCbDf7AwevsRuTyUyMVBJx4FUjZFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=i5-9rls-TCp2mVH5dGFUvUCMaO49KGCEpZTT33tBNA4FPVqpp48tcqrjS7ytabpShgmJZXpsfSQPm5yIBhgjwMtIi3-plE0WGuru_NUqGW6bUcWUX6wFZtTDReawd5nKnI08wzQx29E6YhzShZvYPQZpfi1iH40XeEoXwIZZ50rCM_WXsdrQEp3xWWcXvWc7B31ehHGDlU9fT1k-1_MMUz0J7zcgdCwpkO_GixpZolkb5cJAUmP-hC4LzK0rp4V4xZeVO6cmC-5LqhoDzLCG1ZxlN__slNzPAof2LTNOc3qz4EAVKvDxlpySEI7Qi8WzffKTnWQaMJfpk0X9DZhQbkDHAPdV7_B3pTylJZ4SAN_Mv6YssBKpDaIm2fB83TYodlrIR05Jd00DRjLZcEM82A9jS8O5D_yCrjSRLQMKc28j-NkPW7FMPpf9b-c183teVZf14Tge4ZiY6ieq_CjoRpO_WOP-DkXNOS2uEOHuuDBsvcmYxnubwENOiLmkONFo8cfU2CJEAwd78BOyIWo9CDZ9yKtDIupYHXDcMId_MAo-VvhXVj_KjDn-6r-eS5ua2QwYdQUH47QfMjhFRUb1-g0OLajYqheq40fB9PljpGf66TXrd3z3nSxWgDlKWpiUa_XFQkTLzfZcgwhCbDf7AwevsRuTyUyMVBJx4FUjZFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=CY-6SmROkmOJp1lz05XZqXsxIMKVLMZFKabco9XcBQpqCB3SMqbfZcOma_kbn3zDio6qimkaOKrvH7kNLNG5FPh_wmQMfJBgiWBDS6oZMCqw7sUPRPk_sAS3DaVrp8485LRQQJ5QdgfK5z_zzGTfcqJc07JKaaRPNB8h-lFxC6YC0Gq6MOwAN1QUoL7yKXJIM9I0Vz_o47bUYKuokPfuG2wniFBRhXsGanjkdhfFBf2sVYmzpu8PqTanyCWXzV4uDJlQQb-Y0ydUGqoW2XzfQHupob-FkZq1MOWMW_EXBc1CSaH76mgtGHzZsriXhAQhV8ylZT3K1owyfcxDht7AUXMv8Iu3cBjy0kqeGX7Ym_66TGa__IGcXB5CY6Rco0pcHfJeQj-mC3aOUTxeiJ_a288rINHd4KAB_5KV6gpzfbhOh7hfKirL7NE1CVJ1UmFdW0AnUrfbZCLJorWF1qB0TcKMK007SSpqRSxH8SE6FsidsApRFyfM_C3K50Ei4qmuSRIxEwG7rScHvOQR7RBVUH3gKcicSXtinEBYv23Tq892oFbypxeD6_IRyQ0dQCwQyFFQiBYZ_9K9Q-GpwwV2Tl09NrVMkIWV3pGuKGzYUQecjGExFDg2FkNTYAv0SaqmGf7fmkZqQZ0LXDrZztLDmzToGdPodpHRF9UpLVqW_MY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=CY-6SmROkmOJp1lz05XZqXsxIMKVLMZFKabco9XcBQpqCB3SMqbfZcOma_kbn3zDio6qimkaOKrvH7kNLNG5FPh_wmQMfJBgiWBDS6oZMCqw7sUPRPk_sAS3DaVrp8485LRQQJ5QdgfK5z_zzGTfcqJc07JKaaRPNB8h-lFxC6YC0Gq6MOwAN1QUoL7yKXJIM9I0Vz_o47bUYKuokPfuG2wniFBRhXsGanjkdhfFBf2sVYmzpu8PqTanyCWXzV4uDJlQQb-Y0ydUGqoW2XzfQHupob-FkZq1MOWMW_EXBc1CSaH76mgtGHzZsriXhAQhV8ylZT3K1owyfcxDht7AUXMv8Iu3cBjy0kqeGX7Ym_66TGa__IGcXB5CY6Rco0pcHfJeQj-mC3aOUTxeiJ_a288rINHd4KAB_5KV6gpzfbhOh7hfKirL7NE1CVJ1UmFdW0AnUrfbZCLJorWF1qB0TcKMK007SSpqRSxH8SE6FsidsApRFyfM_C3K50Ei4qmuSRIxEwG7rScHvOQR7RBVUH3gKcicSXtinEBYv23Tq892oFbypxeD6_IRyQ0dQCwQyFFQiBYZ_9K9Q-GpwwV2Tl09NrVMkIWV3pGuKGzYUQecjGExFDg2FkNTYAv0SaqmGf7fmkZqQZ0LXDrZztLDmzToGdPodpHRF9UpLVqW_MY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Tau67IyCTTxSDgOM3clxd2HKoSd60mrXjUKaBY_KefYq--8pzXcUP9S9wb5RrQRvueB9puseAFWm4tSIcz_8bVUIp10q_PckO1yaJZkTg-dfqWvR9lCjGZIwS3pOC6f_--JlMQMJ6F68mSwItrJd4cz3ewn4QJOP8Dg4tdy6VjxHN5pvFntLfIDPBdFm7CoJ1pCa7CYgNu_yP9zUIKKiIQo_-w2UNzM35E1NoBR2T5rTYUinZe_pph2cxUapeJFnDaU_FwkU7uWt1yghIY6b2zpCFX1Ltr87Ih9wpvfELdDg4JKG7Br6WzNdRLTflH5SuXXvBiQwphygoMlCrDdxxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Tau67IyCTTxSDgOM3clxd2HKoSd60mrXjUKaBY_KefYq--8pzXcUP9S9wb5RrQRvueB9puseAFWm4tSIcz_8bVUIp10q_PckO1yaJZkTg-dfqWvR9lCjGZIwS3pOC6f_--JlMQMJ6F68mSwItrJd4cz3ewn4QJOP8Dg4tdy6VjxHN5pvFntLfIDPBdFm7CoJ1pCa7CYgNu_yP9zUIKKiIQo_-w2UNzM35E1NoBR2T5rTYUinZe_pph2cxUapeJFnDaU_FwkU7uWt1yghIY6b2zpCFX1Ltr87Ih9wpvfELdDg4JKG7Br6WzNdRLTflH5SuXXvBiQwphygoMlCrDdxxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=J_40XVUCcqnKoxbyRAV8IldAJLq5tfGWx1tEOBJ4r8sVkTPOhwYL9-nfi_vI0IuFm8YTGtBbKBYBgzFoMUXl0Pmqhmt42pS_cjFTQySLyj8Rm8QE1kWczagx5FXqqwK9U8BEf5SrCE62HrNVvqUranSgNYgI615_TrUQCGlVeugEb36FE5VO-LX8dGOcYYjhCrua0yaS_wgiC0s8QyXiXt7ggx7Kc8KCGL4HKEswtkS0NQ5qok5TGtHvttxWQX0wcqfiH3zwxsI3x4x9heuZOTOn45aqY93mtYijABxobLPgkYKORD3ER4nSPl_WBn6Qq0PV8ajLAZE53CmaSM9jIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=J_40XVUCcqnKoxbyRAV8IldAJLq5tfGWx1tEOBJ4r8sVkTPOhwYL9-nfi_vI0IuFm8YTGtBbKBYBgzFoMUXl0Pmqhmt42pS_cjFTQySLyj8Rm8QE1kWczagx5FXqqwK9U8BEf5SrCE62HrNVvqUranSgNYgI615_TrUQCGlVeugEb36FE5VO-LX8dGOcYYjhCrua0yaS_wgiC0s8QyXiXt7ggx7Kc8KCGL4HKEswtkS0NQ5qok5TGtHvttxWQX0wcqfiH3zwxsI3x4x9heuZOTOn45aqY93mtYijABxobLPgkYKORD3ER4nSPl_WBn6Qq0PV8ajLAZE53CmaSM9jIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=jgGevW9_Ww6pTUNaOTBX9cmAK_bIAC2dZSUm2Jhj1aaHVM_We5QTikS7HE8-T9c5drH_RT6PrnQIgDJg6hUTsTE6rg1Vkz_uqO8x3Pas0urbYON3gsZA1RqqFRxob6gvigvG7uJWbRP1Ge3viFnKMK4amJczBzw8wMF7eHVkqVyGVrNFoNU9seFOLDTqcT477_JhKymiGu1JHZzesRQ6fd0pGFhPhG3QGPljAw1HVW51DC1BLOaU0gmlr_mgXkEzBImllVyD8H1Voei9kmigmorMgJWJo5-i0UYxqDtK7PDRObbAs6YtS136REUwtc-k_Fh1zjFyz4breYIxw91Etg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=jgGevW9_Ww6pTUNaOTBX9cmAK_bIAC2dZSUm2Jhj1aaHVM_We5QTikS7HE8-T9c5drH_RT6PrnQIgDJg6hUTsTE6rg1Vkz_uqO8x3Pas0urbYON3gsZA1RqqFRxob6gvigvG7uJWbRP1Ge3viFnKMK4amJczBzw8wMF7eHVkqVyGVrNFoNU9seFOLDTqcT477_JhKymiGu1JHZzesRQ6fd0pGFhPhG3QGPljAw1HVW51DC1BLOaU0gmlr_mgXkEzBImllVyD8H1Voei9kmigmorMgJWJo5-i0UYxqDtK7PDRObbAs6YtS136REUwtc-k_Fh1zjFyz4breYIxw91Etg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=mwlcUsZXmlDsdOuoXpeOsj2SGgdvOo0L7RnPmw3i_yXG0hqJBsVVy6n3HC2LBW4ZR_OOzvmFhN0zkxUpGj9o1Btrcvc3rfW7tYer0UHBBxLAFD4qVZZ_rCx3wrcb9gV5RgURNVp-_8-prmB4XB1AmXREg4moveflog8M_idz3zHthtd3w9GBFcWykAzaSayN0Jg1SsI7nbLZc_blctaN2YkwXGok5LqAld5f1VHxZmL5-3kmTbdzSPQjQu3n50FG-ridJQobsOnvV4o3rqysoyViAIlR4jbCWf61EOaStMraYdz_jXTL_kvHN3MY3i8XybLMrRwOdx4mezSmClsuUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=mwlcUsZXmlDsdOuoXpeOsj2SGgdvOo0L7RnPmw3i_yXG0hqJBsVVy6n3HC2LBW4ZR_OOzvmFhN0zkxUpGj9o1Btrcvc3rfW7tYer0UHBBxLAFD4qVZZ_rCx3wrcb9gV5RgURNVp-_8-prmB4XB1AmXREg4moveflog8M_idz3zHthtd3w9GBFcWykAzaSayN0Jg1SsI7nbLZc_blctaN2YkwXGok5LqAld5f1VHxZmL5-3kmTbdzSPQjQu3n50FG-ridJQobsOnvV4o3rqysoyViAIlR4jbCWf61EOaStMraYdz_jXTL_kvHN3MY3i8XybLMrRwOdx4mezSmClsuUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=lylTQ09ZSg_UYVIw0qZv0Tfc-KlmCW6SMUftUDgfff1dJfKDK2vrre8eIYks7ZTTyuDmN6p6K09SycYABSTiX6wctCYtWN5ACyoC-W-3OzexYgBXJgCqvssgNl2MniJyN0iKsgjYm2PNGzWdKD8TcfxhRsU6AFV_B1QvpPtOiaELYPSdP1BIQfeZcBjCGyMWngHF9vmJRHqKa-_OSV2Mbis8h0suKoSxIMOqIbFOXiYAx_poxJagxxCklIOxEUy8F0pdvMTtKSAmchmBd7bnP_D8aCt1XKU7ORVc1Ko0-G49bkH9EqR2F8jNWzufL_liprIOO7swHF1jS-Uip0zOuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=lylTQ09ZSg_UYVIw0qZv0Tfc-KlmCW6SMUftUDgfff1dJfKDK2vrre8eIYks7ZTTyuDmN6p6K09SycYABSTiX6wctCYtWN5ACyoC-W-3OzexYgBXJgCqvssgNl2MniJyN0iKsgjYm2PNGzWdKD8TcfxhRsU6AFV_B1QvpPtOiaELYPSdP1BIQfeZcBjCGyMWngHF9vmJRHqKa-_OSV2Mbis8h0suKoSxIMOqIbFOXiYAx_poxJagxxCklIOxEUy8F0pdvMTtKSAmchmBd7bnP_D8aCt1XKU7ORVc1Ko0-G49bkH9EqR2F8jNWzufL_liprIOO7swHF1jS-Uip0zOuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=RvEjigMvG-miz4Z7IW1b6bNnTukHnFBCX6uG1hNGGkIMywX7Uqa-b4Cs57hf9qdq-kML-cOiEimszL8WKDfhIeaO-hrvSHpoc94xai50g5PCdT1EWcNshgWp4BnDUfTp-NkCy__pANGDWnBSv4bVYABHZsRu_2XOlS2vPVW66YD9Y9GWu_haOP207-ekUkqWhVa11ux4GJ2ExLyuHPgusbubSIX7sti_9-QHDj6dLl-YACYAMDC05R62sIv6Gnb68P84jmTQOgvzbdSOYRrx2itdHUDVG-Q3GMu7FxmItITpsrmjU0dgkPHkGWoyf8hIK9mBcsAHWupmsDSEqV74fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=RvEjigMvG-miz4Z7IW1b6bNnTukHnFBCX6uG1hNGGkIMywX7Uqa-b4Cs57hf9qdq-kML-cOiEimszL8WKDfhIeaO-hrvSHpoc94xai50g5PCdT1EWcNshgWp4BnDUfTp-NkCy__pANGDWnBSv4bVYABHZsRu_2XOlS2vPVW66YD9Y9GWu_haOP207-ekUkqWhVa11ux4GJ2ExLyuHPgusbubSIX7sti_9-QHDj6dLl-YACYAMDC05R62sIv6Gnb68P84jmTQOgvzbdSOYRrx2itdHUDVG-Q3GMu7FxmItITpsrmjU0dgkPHkGWoyf8hIK9mBcsAHWupmsDSEqV74fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=rgKx0XIML-vY6mBhuoPXLqEZP8NNrbLv-hbKDtsTp8tzSI_6ZLUIV1fWT4Bp2_i-JgCqC4tpOWv93zeask82JF5-Fo9krwAagbMyIGel9OTGlns5iCRG9qJDZBpfVHWa2EIvNg5yyT1D6GeyN5Nd73jEww6hlYuX7kLqo-CqrnTq6VQFpycuuT-zabqs1b-kbx1fJwfyKy98ARwtBJ8kvTvJEzmZ0e8LelWyD9IZBpm7lin3UHLLoN-jTwkJC1Hp3ibhQM8ohPTHff1a6cFbmKU_8Ar-VEipigXLXTt0eBgr5MuFir9BNzaUEKmR9Ab3uM2H4QAM7jsegr7ZKJs9jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=rgKx0XIML-vY6mBhuoPXLqEZP8NNrbLv-hbKDtsTp8tzSI_6ZLUIV1fWT4Bp2_i-JgCqC4tpOWv93zeask82JF5-Fo9krwAagbMyIGel9OTGlns5iCRG9qJDZBpfVHWa2EIvNg5yyT1D6GeyN5Nd73jEww6hlYuX7kLqo-CqrnTq6VQFpycuuT-zabqs1b-kbx1fJwfyKy98ARwtBJ8kvTvJEzmZ0e8LelWyD9IZBpm7lin3UHLLoN-jTwkJC1Hp3ibhQM8ohPTHff1a6cFbmKU_8Ar-VEipigXLXTt0eBgr5MuFir9BNzaUEKmR9Ab3uM2H4QAM7jsegr7ZKJs9jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSiZBfechbMi3sZpes2t8gcVpHmzW9tt59ihWNq94x_h2YxGhDo82fpQNzpyhkpHpNT0nOEPb36-1_mft_y78EW3XeGs2HRQ2hW1Nyb7p_f8u1ICzbMkkk3fmRg_qkvLFGFH1SRJECg3plPx7aZQRTNw222X88QZuOfmrLmD2SqsyDm1LmI-sn1hjuagH_e7hKdjPDdMwCeOdxJ_94vc9LviSOYgxlwiCLyqdnnG-8n1igdJgLKGja5c_FkoFMsWr_F_eHuQJDJ7D4UyyBSPpjz0BL_ucsAwC-mYXd1t5wJXfmMvi1Bo-uTRy1MELrjZGXH49w0lPHgxyuvAAr4nPA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=YsiGEy0J7eEwofXsy776CTOgem36BKZ2h4WbJj3fV_x3Z1KpRLQ9jUZkz6fBOBDk84elIZAZWTN_ZQAqbA9euMUTeGWCOzx6Le573VzazpWaexUdR4Mt11VPTuJ0xqEg_H-DGNV9zjPyvs-PNjAdxIkp6dof6fN0Is8JLIBJTmZTsj1j7_2uQ5tO92lodLGt7mEvZtID7UKBqN1JVcmCmCi-j5fhRsPBwtrHscEkSKfH2iWdptsIfHqUbuIXrbk72LfX4d94bBO79b6IUAVvyQENJF2rDvRj7cjwtkJufacF2AcnmYUY2BGdmRSopLTs-G4dybFF21UVa3oQSI960g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=YsiGEy0J7eEwofXsy776CTOgem36BKZ2h4WbJj3fV_x3Z1KpRLQ9jUZkz6fBOBDk84elIZAZWTN_ZQAqbA9euMUTeGWCOzx6Le573VzazpWaexUdR4Mt11VPTuJ0xqEg_H-DGNV9zjPyvs-PNjAdxIkp6dof6fN0Is8JLIBJTmZTsj1j7_2uQ5tO92lodLGt7mEvZtID7UKBqN1JVcmCmCi-j5fhRsPBwtrHscEkSKfH2iWdptsIfHqUbuIXrbk72LfX4d94bBO79b6IUAVvyQENJF2rDvRj7cjwtkJufacF2AcnmYUY2BGdmRSopLTs-G4dybFF21UVa3oQSI960g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=UR2A-vEyt3Y-zEv8bJ2Mqiw5Dwqmee_egrSMwAvp0PVAPH8ie9c_3eEsn8Z9A1TUwl9MGDhWcDYzYiJB8dtj4zjPtv57BM4eD39bW2GE3C8fcmoTXWBvdDOwW9xZuomd0e5QohDfOo7RWMFwLCu0j1QaWxAFBZGuseOE7LSEqxTh9cnSMQYh3-nKuBeUpwHIxgJmnVdQvJ-0EX_R8Whoz-3j1ucnq9pwKVdejvpHSZhmug7cgCgzICKCAaaDKD5ukWS5FDpcl_tjb0PeFkLEj-NzuBw9BQIS4bsodfvMBOCeie-16kuTaVd8PNSki70dXruJCRbqRWQsM0ZmFoiaOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=UR2A-vEyt3Y-zEv8bJ2Mqiw5Dwqmee_egrSMwAvp0PVAPH8ie9c_3eEsn8Z9A1TUwl9MGDhWcDYzYiJB8dtj4zjPtv57BM4eD39bW2GE3C8fcmoTXWBvdDOwW9xZuomd0e5QohDfOo7RWMFwLCu0j1QaWxAFBZGuseOE7LSEqxTh9cnSMQYh3-nKuBeUpwHIxgJmnVdQvJ-0EX_R8Whoz-3j1ucnq9pwKVdejvpHSZhmug7cgCgzICKCAaaDKD5ukWS5FDpcl_tjb0PeFkLEj-NzuBw9BQIS4bsodfvMBOCeie-16kuTaVd8PNSki70dXruJCRbqRWQsM0ZmFoiaOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=j_H9dDAiAx3FZFDj3d7v4K5A958xB_LtgEY7G4XpPuuTUZZEAwUzEMfQ3CR5vnv8ZXDHqWLRMYPXu9g0Lh7grNEbSc4GXq-qVM775DDFi5wOc4gScnTiBazkvdxdknZ2rSbsECBIGNs784yAfY4ZyUPaHNFFtBEFGfA86EravCsvvRmAZkD8rBUVZT2rLwo8l9cf8-5P-2BrObEtsiKY2x3bQDBMuq48JqiejM2R0j7suU0MYRMzL77RvrVppLrY0p8cUvs7KrOhLoUgSzVpFMEXJitedl-Mg0qntqkeR2WrsMWIS4Um7UwcGtGfjFLp2mZYL0rYCdvUtz5iSWh8Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=j_H9dDAiAx3FZFDj3d7v4K5A958xB_LtgEY7G4XpPuuTUZZEAwUzEMfQ3CR5vnv8ZXDHqWLRMYPXu9g0Lh7grNEbSc4GXq-qVM775DDFi5wOc4gScnTiBazkvdxdknZ2rSbsECBIGNs784yAfY4ZyUPaHNFFtBEFGfA86EravCsvvRmAZkD8rBUVZT2rLwo8l9cf8-5P-2BrObEtsiKY2x3bQDBMuq48JqiejM2R0j7suU0MYRMzL77RvrVppLrY0p8cUvs7KrOhLoUgSzVpFMEXJitedl-Mg0qntqkeR2WrsMWIS4Um7UwcGtGfjFLp2mZYL0rYCdvUtz5iSWh8Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=IvAZ7T5idScQ-ppp19XDc0Wd7NX6jwpmd5kRQI0JdT3TW96XBaPPq_sBwU2-VUkPQdan5ONAjOht5eBcA_Qj5pqJ4upOvDienlz3U0m-sY2g6Xw1cJ_KLxtTsjWfMvmdlpLbIoZaWTpOgM4XLsKWXcuUBS1fqFmp7OUvN_il_rSZfvunqGp-tqvbwdKAPsFTXHIE2nWEX97N3ObZPmKtJZB3wqxZcnzE0bjJ43e8A2dKWmL4Fg_i3adrL9Ri_aERzNYB6A0LxAaXnliCZg83Q94DKBxI_OHWXBdIBaCkxFy8nPDvIq474GUyk8yHAidOFA3HdYNCxE5eqGannYzlJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=IvAZ7T5idScQ-ppp19XDc0Wd7NX6jwpmd5kRQI0JdT3TW96XBaPPq_sBwU2-VUkPQdan5ONAjOht5eBcA_Qj5pqJ4upOvDienlz3U0m-sY2g6Xw1cJ_KLxtTsjWfMvmdlpLbIoZaWTpOgM4XLsKWXcuUBS1fqFmp7OUvN_il_rSZfvunqGp-tqvbwdKAPsFTXHIE2nWEX97N3ObZPmKtJZB3wqxZcnzE0bjJ43e8A2dKWmL4Fg_i3adrL9Ri_aERzNYB6A0LxAaXnliCZg83Q94DKBxI_OHWXBdIBaCkxFy8nPDvIq474GUyk8yHAidOFA3HdYNCxE5eqGannYzlJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvOVS5U_pdawHO0aWeDduwwlG8kFUQtQSppHArdr0gOVC619VhYwASFiOpIuUKAyBzOJqfNFw7ENXB5BuX-HXaIIPnraPX-LjHTjXcUVVfqidxl0T5xY7sisAegWnVZ0WhsFCEvfQHwpVN6y4GBH-XH6EhuW1DBWCpB_qwQY4kEoQ2r13gvFqAhvhMWoVq7nrzy1nZPXOPkN7RUVA3habwDFyBL9ZAysqgHqzk-uV2JcukIU3bX2_TikIgcY2IiZkGPsyExn-tEdNGiV6fBAdvS93eC1PgN9SXg6nQjtIxFDi2GHxXhi4Qf-jGAmMCxH--IYuzYawpYntzGuu-WdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=t29cB3664co_tNN5AjdL6HlcITk-B-7MKpvodWbKQ9ehHf_ocY8EU5sHP4A6TJ-3HZ1vqeK6OolTDnX4Uqg_1F_F8uQKKLuvdx8516C4vhG53cWVXdZVglH7P5IFSd3eUCk9-_o7BxAGw3b7dOZ_ly8CJ50-2kE5gVj81YlEuJfT_AltM_7rpltWFG7fG5O6x-loO4fgAWXbcG3eX3w86gSAr_Iu9hJMeQs7Lclshgmco4YXxbP11MLHaqQY9Qzu-MjgoarjbrKY2M050akMRfJ6J3QnKlh-ghGBLoB9bVJRf-RDFoVa27_9ubO-IiJ3K0ZYei0n2_bGu56n8U3d8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=t29cB3664co_tNN5AjdL6HlcITk-B-7MKpvodWbKQ9ehHf_ocY8EU5sHP4A6TJ-3HZ1vqeK6OolTDnX4Uqg_1F_F8uQKKLuvdx8516C4vhG53cWVXdZVglH7P5IFSd3eUCk9-_o7BxAGw3b7dOZ_ly8CJ50-2kE5gVj81YlEuJfT_AltM_7rpltWFG7fG5O6x-loO4fgAWXbcG3eX3w86gSAr_Iu9hJMeQs7Lclshgmco4YXxbP11MLHaqQY9Qzu-MjgoarjbrKY2M050akMRfJ6J3QnKlh-ghGBLoB9bVJRf-RDFoVa27_9ubO-IiJ3K0ZYei0n2_bGu56n8U3d8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=DxZrSBCFsdgIYF9pwBoD4BNVHBFUCDxtTNMPBefo0lja6z9hQ7xY4p3KniqQ9_UcW0MuFxB7rL_Kr2OEoZFSJL2beVpAluZGtI96zDHAoTzfaBi_vVgyFZRHlv8DWfhVu1gXbVzCHZQa5XUjHdRZcOvuJkyBZPYUdWxlJvIK409JrqEE45mz2vaUU1jdSu1ZrVL1LmDXfThicc26IN98VQOa9bdLEaHtIhfuunMnF_cCkClqcx59mXW26XV0eAVmK3UYWA0rDk3ARUIgtLSDWns8kvKhoaa_1uE7TQWimlB7LkFS_-izPsZt5mdGyJSGi-vRRmUtMr6PqoWC0L7m4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=DxZrSBCFsdgIYF9pwBoD4BNVHBFUCDxtTNMPBefo0lja6z9hQ7xY4p3KniqQ9_UcW0MuFxB7rL_Kr2OEoZFSJL2beVpAluZGtI96zDHAoTzfaBi_vVgyFZRHlv8DWfhVu1gXbVzCHZQa5XUjHdRZcOvuJkyBZPYUdWxlJvIK409JrqEE45mz2vaUU1jdSu1ZrVL1LmDXfThicc26IN98VQOa9bdLEaHtIhfuunMnF_cCkClqcx59mXW26XV0eAVmK3UYWA0rDk3ARUIgtLSDWns8kvKhoaa_1uE7TQWimlB7LkFS_-izPsZt5mdGyJSGi-vRRmUtMr6PqoWC0L7m4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-juQ0GpnrmIZMOp4Y0NTL1-ZM0Z0FGq0z886PuNRlN1kNpQW-i9Dm9IvUUqItrsbJc4-M6xKRxvxYdSUqr_alYzWOikazIZFncpsZa7KY1ZkzC6zO4vqf8qonWWLOVc8KLFz2bBArrSE5O37lFl2HfXjXK8NFmPVoR0-wZdivK7uG7UOczXHO3lmm5-7I6B9mpRHnW8_22vun7BL1m4w9VLA5Fsoco5ovB9S2KZwJ6fgqcLg6s70XAu9jf-4tx3hUO7i1RQakbTHTKjgzw9-uwzn9duzR5nBejEdO0xCVYzReNUvuOFEnoLeXahAPC-rBTDCkP-wlppHBxCjEC7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GpdRz9f-t-7r_PIf-n8jZ4smoqZ78Wbj7A60Rp3PJyLyKsW0-WdSX7oYXSnsdDEeF5Xbh3GrynXv3rUVKjocoI8t0FiO1XyLAfa3AZirWncxPDUKxt-dWVHFr5EglJVaLT66o7HELLW9ygUrT8zyuRKCl2KhBitNxlve39kt_DZ4GpLpqbcCuOGd8OMBrj-L786DmW88_FNGJFwAFwKk4E7WltUgbJ2dYtEG_aJJjKvxUh86okfZRode_QXnPYBk4dGtSGT1RsrM82PvWZLyXXVSAFMbe44nz0bO28_0PgI3vPpvApmFOKorBz2U_dOXLnEC5zt2YBb4etBDYY6fbw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=BP-tCDMgYNHMFHfXTgZTACLYo7rqzONMr6azXA3TJG5z84bAhdhKDqzc8N7C0OuZzExmN-aSNXxhSb409aDHo_eRj5AQ-MKjys1S6tYqqT0OApn3FWOHowCrYrhifbiW---Th8BqjDOhz_ypO5v2inDY7-RQGsw21Q8Wd7TIpAm1VwjzHHPiTIkvRFoW_dwmNLwRBaVMQntqZVUzYmAjKajTT7EryV8IAZz-R5s8-UkNn-0AxzsvL-XCvtTv2PdUiUomuS7ba1mpa_09D2p0KTj1rumA4zor3hl4f13ynGX0yXJBD1OwqGrTJSrQdmJQY_pfPSVfQDAKqT47fUolKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=BP-tCDMgYNHMFHfXTgZTACLYo7rqzONMr6azXA3TJG5z84bAhdhKDqzc8N7C0OuZzExmN-aSNXxhSb409aDHo_eRj5AQ-MKjys1S6tYqqT0OApn3FWOHowCrYrhifbiW---Th8BqjDOhz_ypO5v2inDY7-RQGsw21Q8Wd7TIpAm1VwjzHHPiTIkvRFoW_dwmNLwRBaVMQntqZVUzYmAjKajTT7EryV8IAZz-R5s8-UkNn-0AxzsvL-XCvtTv2PdUiUomuS7ba1mpa_09D2p0KTj1rumA4zor3hl4f13ynGX0yXJBD1OwqGrTJSrQdmJQY_pfPSVfQDAKqT47fUolKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwtsSte1_KlpA4levIrWALKPrGZ0zhmFu6iaRoAfp1eV3ISdl_jubs_HeeFkZtcWc4KRc9P8sBKv-b340HhZIFwEDjuJFFanQAS0QeSN42g8L_UU5YLWskPYh5WCPvmGYvuvqaIFJEEE0FsFzXgixEsw48JtVozS40WFGpkrqArvjS7QGHSQPFQGcR1NdFmIdIUsuAvaSPRYbfIVEde6JKXviSOcJibcSb9mm0CxUEl6NA61dZjIf7YbK2pmxbMqChJTnK0O3ulYW2FXh0Iuml8ptqRWDyk2TdFKAsyJrAutcWGfFLzrk8Frc0tpjAA7E0yx8uONkm1nwmKdJ077HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP89UNFzBq3w8WeosdR4myGgiJDbveAcF6u23hjZ8FvpOU6MBKqnbqW17jwdWdzy7vbwTZSRJtW8IyFzuA1HoCRfh_riYMBigj1ofaCBe4Q3Cuc-3WAewkFNxjhFwz6iYhM5WTaGWhG96ckrQw1jYuwZO5ExRO1_vWoN_7tT9ziGGRuP2wTUagh4J7sOu6Ls5iNcVKDbmL_h42bDv8VPY6QdkKJ6Et-jvu1ff9rmd2jctArl46Voc9_062GTjaRgVgqhR2Y_V5yhJmUwDenq8CCMoq1jlNuOYsVwRnbl9HO2nnbBqn2IQ1JdAr2VTNKM3HT9_IoSeA3oTzByKJsYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPjRnWwBzRFTjI7LcBxQJTAcA8G569mFvlz0zwoThMw1odRGk0d8Cj4iydMJEnkjlxrppzXmVcbwPNLxtLdB8NUtXeXJwlTzkmWh2-sknefetFTYZ1AcB-z6eoej0QITQ0gX519mjs0TOYjZmXegj1O57LmoXBbMK3Xjinkw9Hs41C6yhGkL7GcyDV6lwveRuG0GVUViZNNm73RVPqj-csG8-gxwNLL4p0Q5n1nF5A9Jz4b4pHllJGUaKMH5Jw0Vj8gK3U6jjkHndPqdJEcxnZg82chjZfz10mJH7SUvs6-6fBFzeFOYsW-H4kRfgYc97MRBuZRRLwngW51QxcYuCA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ijZvsvct2tJVRBXf7AkdYu2QnPwMpoib8PcncxBOL5jLmAa9iXpMHb6Gh_p-7k6UZDLV23lR7HFk2KHamkIzvLk45ZeAAEjSQ_t3IT0gAq_rEqV9M6g6nMWzN4vm2PpTGPTR2AfL4YBBSr-6RHi6130hCwObixjS14OPDgl51IVdVCZfrzFUyf0Av7wJNzNMViNU_wX1yaZmdjUf9v2EvCGuFRV8YHB6uk7t5mi1zO7a2sU_28JKAxlLfZ2dOHpCtzUtSN0UPkC1sL5ZA30SVTUZbUyZ-Qc9xt1SuPX98Il4lx8HhdJCTmp-9y6tfralf0jR2EMyJPYfvKmX7SSgug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ijZvsvct2tJVRBXf7AkdYu2QnPwMpoib8PcncxBOL5jLmAa9iXpMHb6Gh_p-7k6UZDLV23lR7HFk2KHamkIzvLk45ZeAAEjSQ_t3IT0gAq_rEqV9M6g6nMWzN4vm2PpTGPTR2AfL4YBBSr-6RHi6130hCwObixjS14OPDgl51IVdVCZfrzFUyf0Av7wJNzNMViNU_wX1yaZmdjUf9v2EvCGuFRV8YHB6uk7t5mi1zO7a2sU_28JKAxlLfZ2dOHpCtzUtSN0UPkC1sL5ZA30SVTUZbUyZ-Qc9xt1SuPX98Il4lx8HhdJCTmp-9y6tfralf0jR2EMyJPYfvKmX7SSgug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=FIwqc8MYuf2VoH-VsS-JcBA0sSLR4sd_1HveysqJ-cjaR9Bs_m4RS8g7cZIKsz-k2aNRlsZoPw-tBu7yErWfdDWYhZ2QutRNeZVwIEfhcr0I5DvMKFV9_KjZdZXyNXrVcZK1kI95mHv0Qi9F8eUGIB9liw-68UxH-QGoPskPcb6jq8PSaQJDCpFLdF4gdm6JZjg28D7M-yCGuVB_JygKRd9jXTG2pqm8yOIT98wiU57aNXUvXHEEseh5k9al8CmalqvT1RFpNjWSMTuXW_mGJ41Qd8h0OQCf27BOWsOV4TZAlQG-1OehaaGkEdJ2WRKcFDPJCs0kXqfEVC6MmHuxAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=FIwqc8MYuf2VoH-VsS-JcBA0sSLR4sd_1HveysqJ-cjaR9Bs_m4RS8g7cZIKsz-k2aNRlsZoPw-tBu7yErWfdDWYhZ2QutRNeZVwIEfhcr0I5DvMKFV9_KjZdZXyNXrVcZK1kI95mHv0Qi9F8eUGIB9liw-68UxH-QGoPskPcb6jq8PSaQJDCpFLdF4gdm6JZjg28D7M-yCGuVB_JygKRd9jXTG2pqm8yOIT98wiU57aNXUvXHEEseh5k9al8CmalqvT1RFpNjWSMTuXW_mGJ41Qd8h0OQCf27BOWsOV4TZAlQG-1OehaaGkEdJ2WRKcFDPJCs0kXqfEVC6MmHuxAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=R_ExmxrP9qYQliNacUGMDH4rTLe1U8IuWfloOH65N6l66BeRNG0O5DdFQpUcxIQie0hZEeVVJS3CMyYsdUD6nzfdrFpUZYyJt7d8vcP3RSHi_CpTXqfTbDWFV04qhOx100Colwn-z09cohBha_pnaTvRIQTd9MahAdzTmGgJmldJedKTSah5AKFEsArky5BkHZoqVp5LYmlzke2gX9_4NrJJt_dzJz44Mb8pq29xmiirT1MbgxQt-T8hZQWxidjy0G8hVKCMAohFu3kaob5sBjGu_GNNdEPryw5iAudl_o1kRouEx_6Kpu7GwMoC9MkizuWm_PBWlvNMRjAM1u8uXSiIt0L6WGX33ziEiAbA7KO0hMpMlQcRQ0i0QsepC9yoUE9E0un6SeFQJmmsmUF6GO9XTtCWpVqZiXjRYpGa6yk8CYG8QWDZa89fj00czQ2kaZPOa_AVuL1KBexezl2y5BDb2yCunWswgVOlyh_PDFugwv4Y_SSpDLlPe_lkOqXTv_bDqnwKuoDdEWn1jXPOKszHtw-iieLb3ugT58PV767r65rCaGFu7-DZSg_FWgnr6e-e8n7F5msTRbDTZbaw80jomCNSBzaylCZcpFYthU_6Bn6vuAawMJErfYodUX1pEGsE2MMVkq2ojtdtf39mzr3OrmwT1rY7WV_a-HOPoLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=R_ExmxrP9qYQliNacUGMDH4rTLe1U8IuWfloOH65N6l66BeRNG0O5DdFQpUcxIQie0hZEeVVJS3CMyYsdUD6nzfdrFpUZYyJt7d8vcP3RSHi_CpTXqfTbDWFV04qhOx100Colwn-z09cohBha_pnaTvRIQTd9MahAdzTmGgJmldJedKTSah5AKFEsArky5BkHZoqVp5LYmlzke2gX9_4NrJJt_dzJz44Mb8pq29xmiirT1MbgxQt-T8hZQWxidjy0G8hVKCMAohFu3kaob5sBjGu_GNNdEPryw5iAudl_o1kRouEx_6Kpu7GwMoC9MkizuWm_PBWlvNMRjAM1u8uXSiIt0L6WGX33ziEiAbA7KO0hMpMlQcRQ0i0QsepC9yoUE9E0un6SeFQJmmsmUF6GO9XTtCWpVqZiXjRYpGa6yk8CYG8QWDZa89fj00czQ2kaZPOa_AVuL1KBexezl2y5BDb2yCunWswgVOlyh_PDFugwv4Y_SSpDLlPe_lkOqXTv_bDqnwKuoDdEWn1jXPOKszHtw-iieLb3ugT58PV767r65rCaGFu7-DZSg_FWgnr6e-e8n7F5msTRbDTZbaw80jomCNSBzaylCZcpFYthU_6Bn6vuAawMJErfYodUX1pEGsE2MMVkq2ojtdtf39mzr3OrmwT1rY7WV_a-HOPoLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=v6I4XajZuyzaVf--BmUOHSv8yqw70dDLjz-QbCdRVQnkkCi8POK2SDZuvHd7Me5wCp98Kz_vaw7p80hSEOs_piGnx4JwCjPZefeUMDDKvHMSWeh7Ubzuz1weky4qB_Ez-yma39Ek0oEOGJu8uofAs4saAysPqfrAZv_SgL6XFzLaite3Bnahc4NsFdgX9hk9aURaK72rsTC1makg40L9BP31BqpuEP-YoRaNmFrRyRgfcRUup3kgbpdT1ByCRGjgvLFn9IVG4fsUldVPo_nBNbCtNPkAIRHhTNgR_7-iUCptsmt12ZaSO5hyxigScYg6b2k-on_MjvtziYFbAqa7C7d_l80O1Z9C0RIRcHLY7xzII-a9dy0ecek5y2GYfkq7CUSBHKjEanzmwDGDqNlqX69O7zK1IJmetByUKgYnYsykDfP6Jc1MGzHHZWQqzBMPOZBhRzHxXscSdfFl4rtpkBtoEDK-TQEdaaLMBeJbDlWP-5epBdtkfj6gy_ErphaSmU4R-FO6G5dvkfw5bjgeRuk74s-x0arHjq4pGUlUUnaFrh-Z74l7gTjI2z9U2nbkVFG0kYrfDDMO5uhhvOifnEwvBYtbn75BR2xIldZ7sGDJKd9pFN-3IJUfV3yYPVp2d2HTrib8P8vnWQ42UevASLnzzM-7l_t8VNXMWqLu8aM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=v6I4XajZuyzaVf--BmUOHSv8yqw70dDLjz-QbCdRVQnkkCi8POK2SDZuvHd7Me5wCp98Kz_vaw7p80hSEOs_piGnx4JwCjPZefeUMDDKvHMSWeh7Ubzuz1weky4qB_Ez-yma39Ek0oEOGJu8uofAs4saAysPqfrAZv_SgL6XFzLaite3Bnahc4NsFdgX9hk9aURaK72rsTC1makg40L9BP31BqpuEP-YoRaNmFrRyRgfcRUup3kgbpdT1ByCRGjgvLFn9IVG4fsUldVPo_nBNbCtNPkAIRHhTNgR_7-iUCptsmt12ZaSO5hyxigScYg6b2k-on_MjvtziYFbAqa7C7d_l80O1Z9C0RIRcHLY7xzII-a9dy0ecek5y2GYfkq7CUSBHKjEanzmwDGDqNlqX69O7zK1IJmetByUKgYnYsykDfP6Jc1MGzHHZWQqzBMPOZBhRzHxXscSdfFl4rtpkBtoEDK-TQEdaaLMBeJbDlWP-5epBdtkfj6gy_ErphaSmU4R-FO6G5dvkfw5bjgeRuk74s-x0arHjq4pGUlUUnaFrh-Z74l7gTjI2z9U2nbkVFG0kYrfDDMO5uhhvOifnEwvBYtbn75BR2xIldZ7sGDJKd9pFN-3IJUfV3yYPVp2d2HTrib8P8vnWQ42UevASLnzzM-7l_t8VNXMWqLu8aM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=OGDtY4_O1Up3P93ZRHdqB8L-Raqvoo9DZ_FTy-r2NZcmffTBu9XPWApqwVDf8LshHHQx_AlRk73UvHv09N1nvcihMjwyLL_Hp2d7CzgAQD5E7HBvbgMVHLC8bzreX2-h0QXOF8cyJVs-U1S_hBa53XXfSNvwcsQAa5-mqaCt6GpJ8S51zo5VpW3Jwq4yA1CNRGT993Yudq9poNrQR4YTfRL3VpDMU7TAfy7MGQq9fNMwNxNdHL8-ueBwTEIllbbXgIFFKP9vU90zYeEksqN8s3obU0HvINNt01m2OSlG0l58EQpc519qwRgq-MKD_Jp6h4yjHJTxevmgkA5qJTEW3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=OGDtY4_O1Up3P93ZRHdqB8L-Raqvoo9DZ_FTy-r2NZcmffTBu9XPWApqwVDf8LshHHQx_AlRk73UvHv09N1nvcihMjwyLL_Hp2d7CzgAQD5E7HBvbgMVHLC8bzreX2-h0QXOF8cyJVs-U1S_hBa53XXfSNvwcsQAa5-mqaCt6GpJ8S51zo5VpW3Jwq4yA1CNRGT993Yudq9poNrQR4YTfRL3VpDMU7TAfy7MGQq9fNMwNxNdHL8-ueBwTEIllbbXgIFFKP9vU90zYeEksqN8s3obU0HvINNt01m2OSlG0l58EQpc519qwRgq-MKD_Jp6h4yjHJTxevmgkA5qJTEW3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUCTtlOLAWDJ1hH2MSFU8eEk5XeGXeZZJR1r2rHtaZSH5UjY9rG_L0-G5PI82BjUrwgwy1gQ6pkyi67jF_mIjolff5pnH77ZIciuuEpVlmjsbqR3KXMMF70fORi3dToFn0TfR2Jkm_OluQNuVm1z5GKsbd8uX7rl7sGAFrl6a60EJciFZpbSc2WVlaUTuaMAA6U4SOS20ceAjD_F3lp0wPeEh6IccRJ1e-7q-CVDONNHcTjTnGFkxXPCigHutpKVdQVtIqIlz8ZH4oWEYDRgArm6D7z1Pxk0SfNJwnVmyzXpurVieqi5JaFGJxiwes-tw_x7cpqcmjtWgwKlLN9LeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
