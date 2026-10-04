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
<img src="https://cdn4.telesco.pe/file/RHlV-kr9E5qoL-UY0XBkwTNOXCeq-UVgDJaUvdElrovPfmGHVOxFo4bgTtXuD6Tr6tvuyp7vGaLEYR0C9TGx_HWxOVXGBVrmOyUTutpCyKbnNEiWtq11N_gkWKfVL-T1hYdCeF79Nc4Y8CbLPCwpwSa5NXx0Kf5LAYyOySJ8lMREStww1WiDVQP64SBw7GBUrpKBCQXvv1RO9MRfMhpQwBU0g1qUBeDCc0E0qprhj2lzq_47yrBockwqjsfpQYNu0liNok6_dHrwHlhTtW6fFvdxD63H92SiV3IAVikx__fOOtznaFLcQY_fEWc7d9XpNDWp0ackYCWvoLVoRZb97A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 23:46:47</div>
<hr>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBtnZtxfvmkZljS1X5mmsoi_3aQ2dE63LF_VSvZ8cHrMjAr4it62ivKnNgr7jnYcgNCwMKplZNtMWhxiJVIVSzPwyfPynGJGfLtPliG6xfHO8hSeBiHSOlQr0LRiLrzWDPh4Yhg8-miQoTL8M21SFw47R6AIApFyJenct6mBDibvvcEADDa7AMS5Z0HZyfgNbQ7IPWzWxyWLtXUiDY0BOehBGwlwOwcKv3AKOUTCKZN4tbHXHyIX_7e0Qno8X-kuw7gOUTRudhpn8FOpR_g8mDHmSBtI_EuCrEXiBYvrZAwv2_K3PtWhKb1woeE05zJPoEQP4F19UVbJSPyGLkcxDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOmtq_A-ZzPwFW9FiLvnVKIGzRn8Ug09wbcoHUNSCThxmD2tdrpvre2KomG4oFgOWsKcZ8SCAni0I2IM1PdfBjJDIH-jXsqtzRY9oHh7lmu4CnWm-GNodxsl-eChF-2VLqYhJWGSsOTU6PsZc_odfBxAGaCxhFYmw5LieWpmKLl1Z15X5g9uW2DeDK5sRjfINE3RirJp1LEQTfQLdna8Rl6J1jeOD4LFEeidJtmEXiPaVwr_-XDggM5LBxpMmgbRO2vDOI08veo9iobajD-MUteMp9xmKYTVbWQaY2RQfD5YLKc5aIK66HIir5W4xC3ZCBl2jiaSy3jiqDfaE8kXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFKgBKLGvouATOEx3Eaxns9sfSVTpDiprwFH8mEJdw0dx6UQe8FoLmfr6-PPvySXOV9bYcJo6KjfWzjOb0zioST3Uk2NsfDh1eXie578hwaLsFjgNnbaMb4fVFrtlwM_ivYEBsDvoaiZ1kA-eXCwzwWwkf4nfIXhTjLBIogWkm0ePSi8Tk2eImNlrN4Fw6KEnuWp8hdvpUcjACelZev7gLdtSpBIRKc1-mItdUoMVQ-Wa6Fg1U-sbO-kCi1cifAq6KyZUj7G4GI0wJBobntguSyV7bn96l6yeNswgO8vVuvQFriveRrOIZvJbPhbtIEfbCht_Gmu5izandFwp2V-tA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=C37bBkT78mkzHTEn9kQzYP36ytkWExavbraGC1dQOCPxkHme-9xkvNxp_v8u7LC9alPhBpRBlrb1yY3pr27GDJkFdiq0xJhLDg1s7grOMO-NXOT_KAzq4lex6rqFhXCaBTRLpTNT7rCMfOuc9xWW04pUN8DYIaZhpe1oK8WOOm__Dp-8feljVeEJaz96zFNXSo1t9NT08g6jWjmyuIl_6U6jkLMSXhcJhpPIjcn-3vPJuKHCyORx7i6sj0xApNMjBQ8pO1E_Ae1Xf4DcVOAlJ-3HgXkxSrRU3f2YhqkP46DEgJsWBt8PIs5px8wIb8sFEWG8ZdZKOqzvom3w4uOjfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=C37bBkT78mkzHTEn9kQzYP36ytkWExavbraGC1dQOCPxkHme-9xkvNxp_v8u7LC9alPhBpRBlrb1yY3pr27GDJkFdiq0xJhLDg1s7grOMO-NXOT_KAzq4lex6rqFhXCaBTRLpTNT7rCMfOuc9xWW04pUN8DYIaZhpe1oK8WOOm__Dp-8feljVeEJaz96zFNXSo1t9NT08g6jWjmyuIl_6U6jkLMSXhcJhpPIjcn-3vPJuKHCyORx7i6sj0xApNMjBQ8pO1E_Ae1Xf4DcVOAlJ-3HgXkxSrRU3f2YhqkP46DEgJsWBt8PIs5px8wIb8sFEWG8ZdZKOqzvom3w4uOjfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=k1yIo3ftWQKLGxwEzWrvtP2wIHYsZI1izYUmx8mgzfwIfBakE5HZqnBGElMpaSdQ0bCFSAsaAFHHObYbZldb20vnGpG1VlPEfVdXVpBtNt2ZWZ6jAwWX0EDy9oxShOo_ZoEnRmZ7brTQgRdVNNVEP6oE5OCsAVTDFr3mjZnC9Vh96JgApjHedis9JT2OafNIjj5QK7XurSqFNbT9ruHxkdKeqMfyf7KQyX-1XVBuBM-y4o25XbrbT5EQZbKyS32cAqqywv8d8ysBkrlPS9divr1Cp4Ub7K1YtNTGBGw7zPbJt4qRySASFfZ4RP6xKDIklmQ7_r3nIwGvIsYwdEJGfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=k1yIo3ftWQKLGxwEzWrvtP2wIHYsZI1izYUmx8mgzfwIfBakE5HZqnBGElMpaSdQ0bCFSAsaAFHHObYbZldb20vnGpG1VlPEfVdXVpBtNt2ZWZ6jAwWX0EDy9oxShOo_ZoEnRmZ7brTQgRdVNNVEP6oE5OCsAVTDFr3mjZnC9Vh96JgApjHedis9JT2OafNIjj5QK7XurSqFNbT9ruHxkdKeqMfyf7KQyX-1XVBuBM-y4o25XbrbT5EQZbKyS32cAqqywv8d8ysBkrlPS9divr1Cp4Ub7K1YtNTGBGw7zPbJt4qRySASFfZ4RP6xKDIklmQ7_r3nIwGvIsYwdEJGfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvY6PIY5SNp8HEeP3JrhepOCwvSx-3zD9leKRasDt1Qf-uSBdMMEPq2wuIMjd7yNIIw_ex8tXDw9qEwcCVHF8sG4vE-qg0l-hsR03MdJB6ivuGTofviaaknUow4seTuLwbg2SU9xIFO4r4QC1WjWV8yRwhckrdzS_d14o0thFR6jQvGSmNrNrkCzDfKr3LPLDM9V4U4-RoWv9PYE886FgxHp1irZa8zfHNhv1kVVV2fc3jREEm48VpTBurpjeXE_2WAgUPHtjQ71RgNxvqnbRDhx5vHN0YYv5l3-p50veOxGxF_nmJxhJeGzuQze4Yfbh_5OrE9GoR6YStDE7EGEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=IFFCtrmWqSShuA_An0Gns2nBHy425nABxIASc1A5Gojam2xeT3NUrT4jiMfzS8Ra_1p1EuihWzsj26KbfGd0saeE5c-pBi5hkinjaAxwapBZdrA3gCUgU4O-0pserBUVP9oBGLDFzuTisOXfxdpTRLywtvgdEb6tHIH66PFlRU9MwFqXpCMWs2iYOwoI7MFZakifVTHfo7pgZuQSBOR08hvEfycmE_jWpxP87oDuk4fDL7sEVLsV7jZevMwI-1r8e6NBKG-pTx5KUXWL-DNuaKFvw45Ha1u_xzgu1SYKelGZKgvA_r5TWUEJPBvvHwDscoURPgil8ZdtIi4CgB-50Q7WlrnsGVXbJUMkY3BlvPFfYoGZ1bmkJXhYahRpmwtnJdAiVDua82qHpjw2oZRU2UwaXyCFRsHsW3NdE-Er3O_9uoJsA0UvK9sIWaNfY5r2d_UcYSq4mvylwKi8bEpWF1UydaPbqCtG2p_-xJjDp8ovKNgw0v1u7GFpCWYDYmq5H3gtDbxXToVD4GZAQc5F7WaDH_QtZCtPxVr-ncs0i7ytCigVbgR-LUcp4xiTstxz4Qw2FoFtGsEEyQZvy3nFvRN0MrlAD8KIig3MwlFTNCzvRRwM2dEGb5XDev9ahlxaJJ4GUKxlpcaZQKPDu_xvLJyYjy7tP9XAdaj9ekrlx1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=IFFCtrmWqSShuA_An0Gns2nBHy425nABxIASc1A5Gojam2xeT3NUrT4jiMfzS8Ra_1p1EuihWzsj26KbfGd0saeE5c-pBi5hkinjaAxwapBZdrA3gCUgU4O-0pserBUVP9oBGLDFzuTisOXfxdpTRLywtvgdEb6tHIH66PFlRU9MwFqXpCMWs2iYOwoI7MFZakifVTHfo7pgZuQSBOR08hvEfycmE_jWpxP87oDuk4fDL7sEVLsV7jZevMwI-1r8e6NBKG-pTx5KUXWL-DNuaKFvw45Ha1u_xzgu1SYKelGZKgvA_r5TWUEJPBvvHwDscoURPgil8ZdtIi4CgB-50Q7WlrnsGVXbJUMkY3BlvPFfYoGZ1bmkJXhYahRpmwtnJdAiVDua82qHpjw2oZRU2UwaXyCFRsHsW3NdE-Er3O_9uoJsA0UvK9sIWaNfY5r2d_UcYSq4mvylwKi8bEpWF1UydaPbqCtG2p_-xJjDp8ovKNgw0v1u7GFpCWYDYmq5H3gtDbxXToVD4GZAQc5F7WaDH_QtZCtPxVr-ncs0i7ytCigVbgR-LUcp4xiTstxz4Qw2FoFtGsEEyQZvy3nFvRN0MrlAD8KIig3MwlFTNCzvRRwM2dEGb5XDev9ahlxaJJ4GUKxlpcaZQKPDu_xvLJyYjy7tP9XAdaj9ekrlx1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=G3VG0Q3Rj7G7fMdVVPpQYXZFqv-O_9WcYptWNYJ4grj2i_akHR9YH6sW6Q1ON1HxjVFxMMYbCSiKTMpFxIClJx8b2UBtjJ3VlvqCAqU0y_zsNEM2qFm_J1emEGOhAKcENl-m4SaT6RtVYM4zxeGFVGZPxFqv9L0GN2RncwwMj-ScQnQ5dYDPUbZqrzZln35wUK9dPNwdBwIqg4Epx301FQr4sq7qcjyoqZ4Zzq3VxwQxdWcamP6tGg-EwUMPoww0v2s89MWUpPm-6gsddTkMwcdjYebqAtBmSr6awJMay30gnvKywLdlEhf6OgVPH9xz7bLBGAEXQqzIdFCtWF1wEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=G3VG0Q3Rj7G7fMdVVPpQYXZFqv-O_9WcYptWNYJ4grj2i_akHR9YH6sW6Q1ON1HxjVFxMMYbCSiKTMpFxIClJx8b2UBtjJ3VlvqCAqU0y_zsNEM2qFm_J1emEGOhAKcENl-m4SaT6RtVYM4zxeGFVGZPxFqv9L0GN2RncwwMj-ScQnQ5dYDPUbZqrzZln35wUK9dPNwdBwIqg4Epx301FQr4sq7qcjyoqZ4Zzq3VxwQxdWcamP6tGg-EwUMPoww0v2s89MWUpPm-6gsddTkMwcdjYebqAtBmSr6awJMay30gnvKywLdlEhf6OgVPH9xz7bLBGAEXQqzIdFCtWF1wEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mag6KkgPzWXaz7p-TLG-bZvSiYZ_EjfPfaSmE9onnsY_QVv5rDoK5RExe6KJbSR9U3wPMbLtwSXkLBwXbcT9zuoTVxEpO2bRv78FqP8czIgkgQwDbkLuRXuyLZ7mX26iS6FQdLoTYRbG3sptdJMYHCnMX5WxegNgSZmKwvtBOyMIfmpxZgTHm9At8tgcENtbxH5SBy8JZg3-8L4J1NgKbMrPz0qdZKH5Rf5Fo3aOyZW4hRIHj0sO8ea7M2bETY2N4c_lzSKKKG2qFWiIDDK6wzO9qED4d0vXZi4Riu8n-RTwX2YLsYTcUwsjqtaGb8wiUdwUdB635kKlKa1mLSSXDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=ux2nG-haaiT1Qi1ELtJHQpJ093uuZdtjK1cX5Nheitbly7arKaxZ_wq2QUYPtpsUz_RhpAaKl7FTx5dNaGhjtknC7X2350InwWSCk5Pi3UXVjq8WVhfL45qw_iALCuSNyFGzeJZSIXNRdxBH2lo8XO4xZBGmE7UfXHvPLXt0OCXkt-wwBntVF226YmVQP5JvPgUML-MUOi_jGdZU-qZg7pJkPUGk_1Tm98hDWGFF4AxPqWGwd7oY96NZy9B5y0BO1khNnx12adx0gNCCE8MMiOErr41KeSCSl0RXVO6_y_om-jAQZ6YIOysRhnqy-ZL7ALFgZyzQz5Uz_zQAaGQQ3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=ux2nG-haaiT1Qi1ELtJHQpJ093uuZdtjK1cX5Nheitbly7arKaxZ_wq2QUYPtpsUz_RhpAaKl7FTx5dNaGhjtknC7X2350InwWSCk5Pi3UXVjq8WVhfL45qw_iALCuSNyFGzeJZSIXNRdxBH2lo8XO4xZBGmE7UfXHvPLXt0OCXkt-wwBntVF226YmVQP5JvPgUML-MUOi_jGdZU-qZg7pJkPUGk_1Tm98hDWGFF4AxPqWGwd7oY96NZy9B5y0BO1khNnx12adx0gNCCE8MMiOErr41KeSCSl0RXVO6_y_om-jAQZ6YIOysRhnqy-ZL7ALFgZyzQz5Uz_zQAaGQQ3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ5XjSsxl6BKbANBCWqDVvGskzXhNd2GhIFEKtu6VXlzJOnLfUlPahDps8ddUnP149rEwSHBriGufJTLx9euxhdBwDjqRKdEnvQ2S6j9gxMFLPhdT_klqIPebWOl_bfbGmIpeTcsgedQl9yWiS1kN_3VKpUtZ9hDISxjffqjBWoMEa1GpQwGmEHyidyyRey_5WSfsIQuvmVcTm6KDvh00bn_hZ3Si2s3MQOnbVffdyeCMjT16Kt4QkWucfD7dLETyq7WfCyTXVJZpPLuXzN5CUV7PjThZDTsQhFp5UAah9zTF5davp9CtBvWuX3KFEpLdlPZB2_IKslq-whgeSZrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ic-nbcE8nzqe43gOX02pJVcSj1WzfVqbnkZfU2Ei38zJJMnESvdy0cjSR98-Kne5afjPLOtPB8PFZz7JqStr6p56r31HWAb-qoM024GmcREkGomANUdMo-2BMLk7MgzE3T3caUe-W8TMGwoxLMfRedSwHpOlnFh1K1hfP8B-wROyQnTtkS4Bo-kJ_9aosLMrSz2bk-J4lpUa5bgaT7I1nwdQIyhf-ettGXcrn1PUgeRqg-LC2bp2BHGtBGhxblxHVeorKnMuG4dHgE5hrGcXadRdmvDWpb0Ye3-zF8AUbzZ35bl2h6qiA7cwLeWWoeimkhaJey9jSU9NEWaNv6H-NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=dH9u35EGKe9qLR7UUtxjbTyd5sKOXjIkNP-qgIZ-mTLekBdQjwB3kUOs4rRMOeygLDLl4O53LR8qP6f1Dy_Ue1xUIk2sJkqVh5E5fO_g5gMNxC9RnnQbHpYVRGcySm7wNDywFpQK_0Sx_QpxRxts7lYKRaYHRK_jGWU7FsSmWbzBm6U1mwRY3SLOv_54MQTGOile2rO2YCKRUnkA0F_TzdrJL06K7LqHDa7LfdHzcZNNwVT6BayvoQX02juOnVpwaMQ9EtEWAmg2j4gsEKO8gZ2XaiTl-fdtfO21Lb1DM5Bj7XO8hXajlIoQhoCwOwohI7vhoi_xpLCZPcvKBQKjDlimkP1LwK6_l41TpItiyoSE6Vx8Em_c6x38Jua8574E7MCLVnqfIwE5crfwWJhYxBvWycidtbxcz49VuSLpK7bRQ4PTIaLtxpoqVeMGgDAZ0HlABFFpnZAZ6Cu-loTi2W9x12F5izCltZmabqNy5VnN1eDF3RND0S7JOb_FdYXtJBhi_570WzUAglkYIeLFI5u8ifnKxg2QVw8shB4SN6X7f8RnStGmKIJF1JucVpl3DyRBdKnTYflBguyKxMLR2xafwPI0q6axYT-EOEJlurWBo7sZfFlpLhqNLBj6i9IQ_Vrp2MoBFzGCPW4oqsyKbhiP1awX4Yx3oGuwQOOWXTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=dH9u35EGKe9qLR7UUtxjbTyd5sKOXjIkNP-qgIZ-mTLekBdQjwB3kUOs4rRMOeygLDLl4O53LR8qP6f1Dy_Ue1xUIk2sJkqVh5E5fO_g5gMNxC9RnnQbHpYVRGcySm7wNDywFpQK_0Sx_QpxRxts7lYKRaYHRK_jGWU7FsSmWbzBm6U1mwRY3SLOv_54MQTGOile2rO2YCKRUnkA0F_TzdrJL06K7LqHDa7LfdHzcZNNwVT6BayvoQX02juOnVpwaMQ9EtEWAmg2j4gsEKO8gZ2XaiTl-fdtfO21Lb1DM5Bj7XO8hXajlIoQhoCwOwohI7vhoi_xpLCZPcvKBQKjDlimkP1LwK6_l41TpItiyoSE6Vx8Em_c6x38Jua8574E7MCLVnqfIwE5crfwWJhYxBvWycidtbxcz49VuSLpK7bRQ4PTIaLtxpoqVeMGgDAZ0HlABFFpnZAZ6Cu-loTi2W9x12F5izCltZmabqNy5VnN1eDF3RND0S7JOb_FdYXtJBhi_570WzUAglkYIeLFI5u8ifnKxg2QVw8shB4SN6X7f8RnStGmKIJF1JucVpl3DyRBdKnTYflBguyKxMLR2xafwPI0q6axYT-EOEJlurWBo7sZfFlpLhqNLBj6i9IQ_Vrp2MoBFzGCPW4oqsyKbhiP1awX4Yx3oGuwQOOWXTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geaCMDGOAHzR6TDm9MZZDgYlwdsOPHY1CP-C-FIkRhgxonqCl-K0X8tNPwnYsnw04n53Vdjz4kVSassHn4IZsz731qsm3H_rwQ00LPHBPiy4Q7xdTowXEIsTdOtwT8qaBuHrK5kBKXuWCvTdLlX9p7r_tioR3q3uUXSAifq4fBIHLl_1PCs7vWYqrWYXX_OhjiSi4A4PBBLQtozXh4RWo-TzjBm0womShUOgNt7JySzrLrHVNEj0LwgwMlmbMk46HvWUR9M7dRcEDOf-RZKfuANoTRA_238Dy4cFzoo2XvvWBW8frp6ayBhO6aPFXdg8FWdyPIRi2582RQ0-xZCs5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn19F83eoRIBosRKx1XSiBb4BVSsV24A6lqLpFLnZ0QgP51LMFu0GMluN1XMNePHszFImQ4H-SQKRiETQFS9VKRWwg2le0B1rP9B2mV0Ey2Wuvk_WGU53wo3IJfrv6W4GHievzEVl-nMR4EoQl9J0PGEosk7--YCQOMEFI_l1nA3ukAdlsNXV-LSvGKWYjy3iEqZFlMnjBkQsxBXchW94xMlCYI4gpd9Z-KW0hBqjJkRTJ7JXgf1fQ0wu41rTdj6tliCgJPCpZvozih6A7nLbWbaoJ9dOqFynCUbGdfNdkEFX0QTdR4PxyR5Z5iXr2RPf1wuu4u7ivLkJ-56GIutKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=brb4hJgOgFRv2S4wM2RKedrDPGDTWud8sRyo4HU-GaTgNZFp0faM3xNjYG5WMNsIxo0CYwEtEUv-hslvoZuY7gYdYM314IG3EutjOzgTHQdRpJAdxs1rAw909spPhra5FEatm-33Qq_ilvhzquCtZ2lX9ihHDxek6C7JMHTkzIPtmXV26QlmhgmG-5Ht3rpxpuskXICnzxZr2fHaD_HiqYSwJoyKfG5B3DVNmCrzfs8K0GzlTWPNzJiF-3t2n6zx2kTxuIfrtYhUoZwbO-1dxJPCVcf1cPYgNX8rgYZGn-NJxzXZGn67QMBYRtwnKR_7gFEIX0DyXUTFDyllxk9djA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=brb4hJgOgFRv2S4wM2RKedrDPGDTWud8sRyo4HU-GaTgNZFp0faM3xNjYG5WMNsIxo0CYwEtEUv-hslvoZuY7gYdYM314IG3EutjOzgTHQdRpJAdxs1rAw909spPhra5FEatm-33Qq_ilvhzquCtZ2lX9ihHDxek6C7JMHTkzIPtmXV26QlmhgmG-5Ht3rpxpuskXICnzxZr2fHaD_HiqYSwJoyKfG5B3DVNmCrzfs8K0GzlTWPNzJiF-3t2n6zx2kTxuIfrtYhUoZwbO-1dxJPCVcf1cPYgNX8rgYZGn-NJxzXZGn67QMBYRtwnKR_7gFEIX0DyXUTFDyllxk9djA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=kiGeP3fcQMDeDYgntCRM_zQbojuhzhjMxUtWMtx0fGAyfyaj6HLUWDruqajsuC48F0Ep2NpBfreK_qMesBaFg4S9GbzsCFgGvVZgmkN-Zkw7Et2axmGx6SALk14VuBw6Pbn8r9ky9MCLMtayneMbGJB03rRUyXRdMlnjt_9wCu24c3xp_oIBoM6tr7uOlossljU26elxyU6U1ASbOziS8avoXj8TeBZiKzlJyPF1JPzbI0Bq3GTaBg_lQJUqXx7gtGGD5aW0o8GFrfhReOHJSx8Wx0CIW6xuzcdOwCQF6txq8wt9N8zFkNiH0Jpi7ZCKgT8dimsOUtoBYnZn8AbUfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=kiGeP3fcQMDeDYgntCRM_zQbojuhzhjMxUtWMtx0fGAyfyaj6HLUWDruqajsuC48F0Ep2NpBfreK_qMesBaFg4S9GbzsCFgGvVZgmkN-Zkw7Et2axmGx6SALk14VuBw6Pbn8r9ky9MCLMtayneMbGJB03rRUyXRdMlnjt_9wCu24c3xp_oIBoM6tr7uOlossljU26elxyU6U1ASbOziS8avoXj8TeBZiKzlJyPF1JPzbI0Bq3GTaBg_lQJUqXx7gtGGD5aW0o8GFrfhReOHJSx8Wx0CIW6xuzcdOwCQF6txq8wt9N8zFkNiH0Jpi7ZCKgT8dimsOUtoBYnZn8AbUfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=XgU1quOJ1W5h4OO9a4nWMINzRDdkGeq6U022yO5AkzKIGOSYXidyLoMkokIVMqqqft8r_TWxHc3kQu5yaqBv9_olFXBe8VDNNTLG9aa0tqmtLyLjkk4Zx3gRLPNzEJsZJJJ61jG4oIOr6bCURLGiiNo0RVzHGIbrWeB56_RU-wUHsyenDeERbtt3jyfxzxMn-HyfrYTZKisQeyxev7yiimQaOc7fxE9XzrFZUVK40PIcqT6OdMRo3nOMBJUn1iYsb0FxYcU-Dr402sPB1Xrzv0Q5SF-nlSM6wC32qbAtU3Vivn19hCMGPafZws9RRWFNJYGgmU-8kizmsRxwzb_VYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=XgU1quOJ1W5h4OO9a4nWMINzRDdkGeq6U022yO5AkzKIGOSYXidyLoMkokIVMqqqft8r_TWxHc3kQu5yaqBv9_olFXBe8VDNNTLG9aa0tqmtLyLjkk4Zx3gRLPNzEJsZJJJ61jG4oIOr6bCURLGiiNo0RVzHGIbrWeB56_RU-wUHsyenDeERbtt3jyfxzxMn-HyfrYTZKisQeyxev7yiimQaOc7fxE9XzrFZUVK40PIcqT6OdMRo3nOMBJUn1iYsb0FxYcU-Dr402sPB1Xrzv0Q5SF-nlSM6wC32qbAtU3Vivn19hCMGPafZws9RRWFNJYGgmU-8kizmsRxwzb_VYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUKuVKSdboCpPajwJGafg6yIXUE13OTnLfrsacOpWhaZT6CspZI1bQQxxQKz7usXraO5XI4Nnub0cT4edc3kJEm5ni5mraqF2NsiapIm-rmNLzmZ4LeqjkK3jKOnNZzanCElY3HJ9vVhkOB6OAVmGlWnBmjj2UlCMWNzrsvQw7BGIpP8PoCUCiGQ3bt359aMxyxNHvD-NO_nhnMmStLSITK0RyMorYMXx1wRWI09RREPbtgZJ35iIqWOu9on3zCOoBz-2raeOVZ5i0wehJTxVRXcWmJ1Jb4sv_c43jPzS_rNMt_bJNjJaJVw828bvfNWWoD8MYU5RgjxWKcC8WP3tw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOskDRISFyGRdQI9qgRJtybql0Fofh2AsESgq47aLsZsxOAPu__PEpNz3EW0YljtBKpP1tP4OOzxO6aHipSmM-MS6ixeL3k4x0Dyn2jgYF2M2cliVrpgtiRfYegHNh6ZEwCbKMtj2fzCt1FhSrhG2yBXOJuVDQd5dq2RykgIx4TIe0hwfNSRDhMggFfDwtBsykT_gj-EpkzXJJbfBTvsr8W49g8oikhkiMxKS0GcCUPZkv2b3IHNmR2I7uTKxTC2OWXw9qh4HyslQgaOWUAxjZTCFIKMbStgDK5UtU9Wp7ZfP9S0ZHfko_7AqIXs9lm53rN0ZJkS59lkMwBnzIcZiGf3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOskDRISFyGRdQI9qgRJtybql0Fofh2AsESgq47aLsZsxOAPu__PEpNz3EW0YljtBKpP1tP4OOzxO6aHipSmM-MS6ixeL3k4x0Dyn2jgYF2M2cliVrpgtiRfYegHNh6ZEwCbKMtj2fzCt1FhSrhG2yBXOJuVDQd5dq2RykgIx4TIe0hwfNSRDhMggFfDwtBsykT_gj-EpkzXJJbfBTvsr8W49g8oikhkiMxKS0GcCUPZkv2b3IHNmR2I7uTKxTC2OWXw9qh4HyslQgaOWUAxjZTCFIKMbStgDK5UtU9Wp7ZfP9S0ZHfko_7AqIXs9lm53rN0ZJkS59lkMwBnzIcZiGf3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=jxtmvDsevw2VloKmJnZdP443lJDv1BwlQDtHOtaJbwHRrknbULfwMJ9ityDLqxuaPuKN5mb6Q_d7HcAwxjvcSK5iMdBgNgjTVbP7T-t_ZPu2nTFt1UEu-ooIWUjOjyvMtvVi7Hw6FR-IIJbPEvOot22krbdDwc7C_rSNIjdFd3z-QOGt1BNg1It50eTZ8dPPAWa5I3HESgvCncYY-ae5QMV9axYHTJSNHaA4RHCzrUWIByr54BCoQ5rl2nR2AdVNYRxUQzvVO3rB5MpGwvtBKFCXmDmKl6gpG6cWhvU6h6T1W1U6yFMFI4LnVmHsW1Z9l-OyyiAlQGRpAWUAylh8Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=jxtmvDsevw2VloKmJnZdP443lJDv1BwlQDtHOtaJbwHRrknbULfwMJ9ityDLqxuaPuKN5mb6Q_d7HcAwxjvcSK5iMdBgNgjTVbP7T-t_ZPu2nTFt1UEu-ooIWUjOjyvMtvVi7Hw6FR-IIJbPEvOot22krbdDwc7C_rSNIjdFd3z-QOGt1BNg1It50eTZ8dPPAWa5I3HESgvCncYY-ae5QMV9axYHTJSNHaA4RHCzrUWIByr54BCoQ5rl2nR2AdVNYRxUQzvVO3rB5MpGwvtBKFCXmDmKl6gpG6cWhvU6h6T1W1U6yFMFI4LnVmHsW1Z9l-OyyiAlQGRpAWUAylh8Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c29cLmFnr7lFtOLhsZffz3WLTT2IABM_7UBRv_u5jzHZKMr5hgIUeU6tTGs9Ml2GASwPMbYWUjY3wcjLEnaIUZ5KrW2L4SjE8bQxmI6pHrJGzP8Ql84DevFSjhbIKPvLlF8CEZigZg9q2EeSuCYrnD8qz5PZC4NqfwasHHjTOwjvWlnU7lyiDWi5C3s2svtwNAhtNJYRO1NLCPJ7Gzw2niq-5OggLeTctMBYLrufw2cln9L8S0GJk7KI6uDkuIYNJTN7npEQLT42w-fdmxsQDKwuBH2KE1ApbKbob-Qzbxa4L8hxA31gj1ZljniLqR_bgdkFHxGXjiRm8e0P41uELw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=A3Ef4QYoOrBhyZzjKJuMNsYDXV3ujzoCZFL6-aBunvo5KKPC74enfgVFyQE3hbxumKjIEMLBprWAZ5TLbVrXIhO5HQfWMZ_A8fnerPbLGasoeekGvfTMRrEinEr5Yr6Vk8gxlr4HCmeg3p0uG38iNLM5UFzbtIr8NLg8kR9hM_y5H6ec2uvZVLHioGUv0fFEEOSXxVfQYOxR6hO1CRQFkNLCMe_bKQ1dhvnPlWhy33WeYCPlY47pvaEcubvLeHolSlZhRQbg81Q_mc0jdfynFLRbApIKj1c3Bup_fShqXxCj2qAS7i9_Z1-MZJ5hYm9KLng8QuMa5nqxtWr3Ps9gYCnzc0n44B1blJ_4dQYKpSebDlLKPWxEqAgrADXf6Kr9jOFmrqXpS4C2Fm9rnX3N2XjTk4-7icfnIxiwhWTab1-N5y-hd-_sFByhflMJnEZYxKoQ4whS7LTiIYZohxbkSdxTeqDmGsyX39enwi58R0beTMvFwPwmnocelj1Wmp2NsifL84OPFclQSYKqF0ucWhzab5aMqT8CxE4_IaIXMdMHhtWGkjb5QibKz0aTGa4236B80lQvJ2b6TH8BnBb5ZVenZ176-npbCvpvxKcQy9WtQcx-GyDszClJYBtRgv3JXlapvjbZyMSATdBQgkmzHFmaz09izrf-WzyJiUGYP08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=A3Ef4QYoOrBhyZzjKJuMNsYDXV3ujzoCZFL6-aBunvo5KKPC74enfgVFyQE3hbxumKjIEMLBprWAZ5TLbVrXIhO5HQfWMZ_A8fnerPbLGasoeekGvfTMRrEinEr5Yr6Vk8gxlr4HCmeg3p0uG38iNLM5UFzbtIr8NLg8kR9hM_y5H6ec2uvZVLHioGUv0fFEEOSXxVfQYOxR6hO1CRQFkNLCMe_bKQ1dhvnPlWhy33WeYCPlY47pvaEcubvLeHolSlZhRQbg81Q_mc0jdfynFLRbApIKj1c3Bup_fShqXxCj2qAS7i9_Z1-MZJ5hYm9KLng8QuMa5nqxtWr3Ps9gYCnzc0n44B1blJ_4dQYKpSebDlLKPWxEqAgrADXf6Kr9jOFmrqXpS4C2Fm9rnX3N2XjTk4-7icfnIxiwhWTab1-N5y-hd-_sFByhflMJnEZYxKoQ4whS7LTiIYZohxbkSdxTeqDmGsyX39enwi58R0beTMvFwPwmnocelj1Wmp2NsifL84OPFclQSYKqF0ucWhzab5aMqT8CxE4_IaIXMdMHhtWGkjb5QibKz0aTGa4236B80lQvJ2b6TH8BnBb5ZVenZ176-npbCvpvxKcQy9WtQcx-GyDszClJYBtRgv3JXlapvjbZyMSATdBQgkmzHFmaz09izrf-WzyJiUGYP08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYPa9GE0VNs-lhz4x9qXJ0g3XoW5Kuq-iWQcmqMJwH_RU7ohbH2Zc9J8nnd0wZW8Cm5QL5Nt61BbYXhgl28jlgnVOGlEG0zE7_AkHT0oJyTKgJW_WjKG9eri6LzCZZUWysyuMSvubV_oYw87Hb9OGrnJ30xXVeapYq8VfyW_ZYxYJBl7lljMuXiRnUPwDKQys_cXz55UzcFznnHheFRO97ypB3ZtsmvQE2LsG-Z2xSpHR6Q9uFXbc7d-kypMt0XjSmcLNNMF_6GSPcdOpeAm9JZzmW8wqpZT6uMm2aR4qip4FABuwvjMf97zMgtEOj-g1-RKTF6YgnEfL_Z1TU2ldA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=WBJ-JzthTHdZx6BJQSTq-GLcnp3cRZRh9qgSMOxI7mqToC5DTTjTsM9txcRuh2VkKnG2g4h-QY3hRpDbPko6z1DB1fgguWxEqbetK3XSp08c0WMs4RkOsAxMnSH4CVrbqivBhllqvdfxFrzy7W9lvnkMmuAcNIJak8bkH1jcQ9PW0IQYRg-Y88JZRpI8iFBS7tMIHnES1grA_7T8MX5b_PCKByl1yUwKYO-fxz9kr-OYYOFqK0LvQxPqRStnBNtm9IqW3iUrkpu4ofvl_ZC8Xb9XFfILQhwJoBtCQN-bvsUI8eVrEJrWOEx3_MgC6ZbNXGJz1XIleoSAFmHKM0cQ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=WBJ-JzthTHdZx6BJQSTq-GLcnp3cRZRh9qgSMOxI7mqToC5DTTjTsM9txcRuh2VkKnG2g4h-QY3hRpDbPko6z1DB1fgguWxEqbetK3XSp08c0WMs4RkOsAxMnSH4CVrbqivBhllqvdfxFrzy7W9lvnkMmuAcNIJak8bkH1jcQ9PW0IQYRg-Y88JZRpI8iFBS7tMIHnES1grA_7T8MX5b_PCKByl1yUwKYO-fxz9kr-OYYOFqK0LvQxPqRStnBNtm9IqW3iUrkpu4ofvl_ZC8Xb9XFfILQhwJoBtCQN-bvsUI8eVrEJrWOEx3_MgC6ZbNXGJz1XIleoSAFmHKM0cQ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYFQ2FxZXBWrOTh6ilILFhedR5w9qq7xz_ma1zF4fIVZ1GhfuJGYd9I9jzowh-JoROfqmQ27QYreA6gzxGTDlsGTgF4r7I4pSBP4ILzIUaBAfxzzoI0fGUU_aXDX_adQgtnzr99lWQCzA822j1kbu9nagJTULZ5pv6zUHX7Rq4eLSohR34rbIg3i4w9_04b509dlRpxvfJaH7SglQw-jAt2D2zAJ5pueBhtyDyekYWWK4l8AMAl6N4CQJ2iMfaOYHSO1ARNmb3ORYrOQSEdkFFrGYcQYOwopPf8FYXK7OB5npFsI29jLUQwbnHaQxSyeSACTJxx0UqsAQoiOrVEiBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5MdUUn7GeS5CK34EwA7zy2sym3pTpmmTVp_8w75pe8Q86eHhthnjhKDmwI8E4H8y8Kj5i1Wdiu5cI0gDfN91lddrkdPFQj4HrLHS5kejERami9F2mLoKvu-l3kKjbXPbnaIZ6HEcN4CWHlhdh-IpIkrLPICUOg2kk2BiwBIB6h2nBjD3FL5o5vanR9FjldwyPiZsKP3AqFctN_wyOMHdY4rQgQrp7w2EZhivQV9WQ-T55REKCWWL5YBb4_pMZZyw0LrawQgi_YSr5KGgYtFDLwTG08EW4Zk4N1SWZwT5UMqO3iIGB6-GFm3hpfSaq93XssVxeNnTi983-RltREfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFsnGAe4D4XpHTn_-rMJcRA1o4V46VO9iNe5_oAJKBsa8uBFQJQTC37HwyWY3w8fPel1vqS1mM4vvm7vGiRbBo_xfBSi-XurFGv-5_m1o8OrlAKvUMsV7J0CuJ-qI1hF86Xph-CaBhih247mYZW0xOX3HoCYmGKo8vv0gn7SmZWNMcjQUUFT6UXUVzxyXCLdusfX4LOfQvqfKWjQzx1b5xDYBB9d15FHa_a3F7AEz0MMx2DpAjIXDC5ThAp5n0l3GhfLUEcJBI83J2xUlF0W0MpDEOoRxjgzC6fHfyTbZZ-fcndQA_e331E5qqZjj53KiPunTu1mfZRSpVBbJ5k9Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXgJe3ReZ-41dsgFk1t6HVyvHG2wIGy-6YJeE9hcMb_pymATW-aNFeCJTb9ZgVrNrrNDhVs6E7hO9VUWz6Bxk3SUGbcKsw0FTDqQGzVbC0A1UnGaQloB0W0oaazN0qMihF7I-pGbiDtzREVc4GW_yTZ35E3G8S2O47d_2_5rw35yhLDjqZqRWgeUGrFcv3dV4lrfN4QU-MUiSTHHZgoS6BX0FbzcUwLsRQpa7JhpHUiCTiZuBgbPYP6SzJ3XwHRT0DAB7z_0vF-8OnSyF8lWydNvYAX4IpRSu1pXXI99EamsVX_IFagza3vhKyI3rTx59Sz8hY6hjpYLioOAp-2I6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu6uRR9S6gZa5jjMHvoL_7py3-1S9OBPwuWDmdMnZkcqt1rDTFbEq11Zb8KLaAUDKWLoySUR2Jlpqw9dSSV9GPfEARhMJiWM6wp7lZ6yulVfjkjE3wx4E46V89qDxTgAhX1ZvDbaV79dF9-OqfNSO4Gc-p_DA_EQhAuojOcOBZn5vczb8OORPiP8hojuoyl5-Ub9L3wAN3ouwyMz8-U4wOmmPeagh26vV_fJUOdZc4zVKIG8YSOOOqnqBdndbndkaOXnR6VAqd-VLnq3eInGk914BhXn7oH4mc3xSqSHyCuneuLcWYkuWrUS_N7XZFde1emS3JokwsI4gIpHgFD7NeLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu6uRR9S6gZa5jjMHvoL_7py3-1S9OBPwuWDmdMnZkcqt1rDTFbEq11Zb8KLaAUDKWLoySUR2Jlpqw9dSSV9GPfEARhMJiWM6wp7lZ6yulVfjkjE3wx4E46V89qDxTgAhX1ZvDbaV79dF9-OqfNSO4Gc-p_DA_EQhAuojOcOBZn5vczb8OORPiP8hojuoyl5-Ub9L3wAN3ouwyMz8-U4wOmmPeagh26vV_fJUOdZc4zVKIG8YSOOOqnqBdndbndkaOXnR6VAqd-VLnq3eInGk914BhXn7oH4mc3xSqSHyCuneuLcWYkuWrUS_N7XZFde1emS3JokwsI4gIpHgFD7NeLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=GznoA9ZoBNzlZ7XVRKINsIGXp7I7CLtd4XMNeni8nNgAgsap_vqU26-GCYowBzevT9R1XB6iqHxAf1XsvxKXxmLtNX8avkOUthklcb5oncKgakAf3J3BZKS5r1WEvn-uswyj0mQpvGxyPqp2v23yU6Bu5DMSSw-ntL2miR-6utFagoJGCgYagU7_YvtvtX2ky8pVzG4eSbXqzRK5Yqju5wExkCwSVOsOhO1C2Meo6c9pRBh8o58eD9R2VYDHDImLyddhcY1K8w1OKXCNUtkUp9M0Ykr_YED36Es55en-VUHVh7u9TL0_ot-NQ3cpXMP03GSlBK39A4AaO57QGemKpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=GznoA9ZoBNzlZ7XVRKINsIGXp7I7CLtd4XMNeni8nNgAgsap_vqU26-GCYowBzevT9R1XB6iqHxAf1XsvxKXxmLtNX8avkOUthklcb5oncKgakAf3J3BZKS5r1WEvn-uswyj0mQpvGxyPqp2v23yU6Bu5DMSSw-ntL2miR-6utFagoJGCgYagU7_YvtvtX2ky8pVzG4eSbXqzRK5Yqju5wExkCwSVOsOhO1C2Meo6c9pRBh8o58eD9R2VYDHDImLyddhcY1K8w1OKXCNUtkUp9M0Ykr_YED36Es55en-VUHVh7u9TL0_ot-NQ3cpXMP03GSlBK39A4AaO57QGemKpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=RCaU0Qp0TIud_2ONxCI4_LlnBIM5-rq4ye-XNMxIgpACYNKcktHucn4rVsJutHPu5j9dFGMW-sMNmC0wvZI0tfWBo-YpnNA2C1Ra9q_OxW4o2_DKLQI8-cP1xFJbk6PzwhQN5jFNDx58ZZs_HMmc4SZ0BWGVKpCL5fkRO44I7H6BFdnYsyAuot-ahDk5CvpPgINUq-7WS2xKTfmjloZU936auT56SCXIIo8111jLv4YfUEjRliXXvfIu5hNWrNERAPD8dStKrsdF34aQzYxL7hLNpzeKLFYALEJ0O6ty72n8CnxV06jHu0ReNgI6d9_rLgBpbwHcuSprn2bxHo1CiXiOTduaPn9G86k9NWlsTxmwaJ_MWRO_PgwEWv-A-PMC5SJDsNrH59f0Uy2EM0p3UG5RcIP-0oHPwqKbK4FwUSdQaGfKwsr4jXrs47lyInJDbhfKl-eIlyqXv1v0v0kiBqc9IdnXSkToF-425DDugfrWcg9u7_j8pkMAPPgHULGODVDH-rhQf9_4hZAv5ua3vfASc0hBAYKTA0gQzVj0EfIw4hD2_f8STLZa6-_dUh4srv8YxDxnta6OYxSsho6EIRjbiq0-MOCgNIhvp2wdpU8fcZ1LRCTLJV97nS17S2aqrska56W2bc147cHGSuqtoKAcLExue3MASRW3kDRDUGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=RCaU0Qp0TIud_2ONxCI4_LlnBIM5-rq4ye-XNMxIgpACYNKcktHucn4rVsJutHPu5j9dFGMW-sMNmC0wvZI0tfWBo-YpnNA2C1Ra9q_OxW4o2_DKLQI8-cP1xFJbk6PzwhQN5jFNDx58ZZs_HMmc4SZ0BWGVKpCL5fkRO44I7H6BFdnYsyAuot-ahDk5CvpPgINUq-7WS2xKTfmjloZU936auT56SCXIIo8111jLv4YfUEjRliXXvfIu5hNWrNERAPD8dStKrsdF34aQzYxL7hLNpzeKLFYALEJ0O6ty72n8CnxV06jHu0ReNgI6d9_rLgBpbwHcuSprn2bxHo1CiXiOTduaPn9G86k9NWlsTxmwaJ_MWRO_PgwEWv-A-PMC5SJDsNrH59f0Uy2EM0p3UG5RcIP-0oHPwqKbK4FwUSdQaGfKwsr4jXrs47lyInJDbhfKl-eIlyqXv1v0v0kiBqc9IdnXSkToF-425DDugfrWcg9u7_j8pkMAPPgHULGODVDH-rhQf9_4hZAv5ua3vfASc0hBAYKTA0gQzVj0EfIw4hD2_f8STLZa6-_dUh4srv8YxDxnta6OYxSsho6EIRjbiq0-MOCgNIhvp2wdpU8fcZ1LRCTLJV97nS17S2aqrska56W2bc147cHGSuqtoKAcLExue3MASRW3kDRDUGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=o5g9bRxK_CoyF_J3pzt2QUfjoXDYVg4RQLxpQbP1nnS6FPAXXz6pHpHf-tNfAJ_ROQmF9NtKIv5vr7HtQb0ZiyZoH-9NAxT8h3PZISaIKY85cW9-fko92a6997nFgbNza-wa9DUOxJQaFLGs8WXvLSEXrxvdcao9n0yzhfXNlpqwgNznHcC-NMhNE84YOZtCopW2TvBFPiRVEMHKeCAiLSW9oqsRWknQVK_-47IWn1Gf2a_IeVbuzldE_6iIvJgXqohHBfBszQO-1dq9ouWxgR3MXKc4icNwHrU49kaRjsoqHJXZrTYnaY2osmsH48bM_c6iC71De3L-GcNIOs2Nbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=o5g9bRxK_CoyF_J3pzt2QUfjoXDYVg4RQLxpQbP1nnS6FPAXXz6pHpHf-tNfAJ_ROQmF9NtKIv5vr7HtQb0ZiyZoH-9NAxT8h3PZISaIKY85cW9-fko92a6997nFgbNza-wa9DUOxJQaFLGs8WXvLSEXrxvdcao9n0yzhfXNlpqwgNznHcC-NMhNE84YOZtCopW2TvBFPiRVEMHKeCAiLSW9oqsRWknQVK_-47IWn1Gf2a_IeVbuzldE_6iIvJgXqohHBfBszQO-1dq9ouWxgR3MXKc4icNwHrU49kaRjsoqHJXZrTYnaY2osmsH48bM_c6iC71De3L-GcNIOs2Nbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5GR9Vba2N47l185f1X5W1piFpwbc8Q9YjK1DGOnyNBM0xERiMrJZo_jHYdX7vFv9r9lWMr__9ew1cRrjC1Nogbqs-SQ8Uv9QD8eotQw73eNDhcZeEu916gkOloL4mxnPddatCEd8LUaFXTTRZjdI97uq9TFe3g1kEphgh5qj-9FtcRVofVNCnYdOiChztADE-kuCO7LdRKepvK1Q5bW99-HVA8pxXKKwgjmrQJ_PHHF9SFlxBOxVp5sMj261CfH4W7F2iKAg_2wd-CdqDL6JTakfjP4EzzI0v0TE1xNDyZkErZFik9cFFYErOrzk5Hq_OMztnklemvUEmWhoVDRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=uDu_4RDO62Hd4KMeDFk9-EfBAfIql3swbMpfwHjQI1oMaO4tNsEGilMfbjR95QVLP7yVHFrJiLJahjAF3_ZUlbSJiKozsKNiMbLg_u0Byo1dcGzt4twTEkmBPg0P4z2K_GKa_5m13GA7bDg4SfE1vic0EnkgYwVPnbvDIaZWQRzmHh8aJHlq8MaZyXFJJqxRLCz9c6wEQNlbE-4fOWdL1vOZBUEB9u7ZqleWC-6oN0fInc9FsNNdeoDj8_rgabxOEwkGIAZkbdKyWGNxnIijhZH5WQEcMulGqLPc2FKaMOFbJwofUGKVKKPtvqy8nt379NmKU9SQuID545spl_-PeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=uDu_4RDO62Hd4KMeDFk9-EfBAfIql3swbMpfwHjQI1oMaO4tNsEGilMfbjR95QVLP7yVHFrJiLJahjAF3_ZUlbSJiKozsKNiMbLg_u0Byo1dcGzt4twTEkmBPg0P4z2K_GKa_5m13GA7bDg4SfE1vic0EnkgYwVPnbvDIaZWQRzmHh8aJHlq8MaZyXFJJqxRLCz9c6wEQNlbE-4fOWdL1vOZBUEB9u7ZqleWC-6oN0fInc9FsNNdeoDj8_rgabxOEwkGIAZkbdKyWGNxnIijhZH5WQEcMulGqLPc2FKaMOFbJwofUGKVKKPtvqy8nt379NmKU9SQuID545spl_-PeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=RR_X5UNSLDC72kI_LO8G2ZSZ4DJJfKLCGixPDTwdICIGqdxOKjgUwT78ZbiUDOxkvtRpqSJm0KzhWCOEFtONSrOrZLu0vp2dmMMdtibA9bd2y28M2LQd-jNexUUj1QjEFVRGDoe3apOAJOc20FUFLmvdZzN_OwfxZDmMM34VLbqKTErj_xTpOWi-oIDyE97WB3PvzX3SIKFcs_PJrp6U9g4pFTfvKuV5vKgdbNomUdXktS5nqI0p3Ke1UVmvCS6E7-WtjSlkZ_67oTAOPT_mZ0wj50amcqtk0UxjVr9eHpMEGuubDWXpIElqIqAuA8XG3Bx0DOfEPg7sCN9eWSoTDzu6DCtfQ53xhQhjxw6mRHFYw9FE9e8ogItYmk2wurid8H0FII0LM2hAWzQajbs4m3gVEwCHLMw0JFDSwzNhCdAQZTMPw2Lk2ajeKQiRZHk4IJQl-RcitRkLVXq8SU7cDLlwPmQ6N4myol6n8ut1wux5OoMhgrx_TYD_YVtr-NOcZsp6SA1t07I6wtItD9TlihvopcSGFYmbBsuRldmES7cq89b1wveYGB8DXk_WprUH-cmOUcOkaVdybBJedUv8DO_gSe4-OlMi5kiiE6BPEd0ig8OmsN_ZDAUs-zCVzVEBE6mNjLD_qsHE5g7Xlq0DWhFWpNfkvbKqrqKTEj_jTUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=RR_X5UNSLDC72kI_LO8G2ZSZ4DJJfKLCGixPDTwdICIGqdxOKjgUwT78ZbiUDOxkvtRpqSJm0KzhWCOEFtONSrOrZLu0vp2dmMMdtibA9bd2y28M2LQd-jNexUUj1QjEFVRGDoe3apOAJOc20FUFLmvdZzN_OwfxZDmMM34VLbqKTErj_xTpOWi-oIDyE97WB3PvzX3SIKFcs_PJrp6U9g4pFTfvKuV5vKgdbNomUdXktS5nqI0p3Ke1UVmvCS6E7-WtjSlkZ_67oTAOPT_mZ0wj50amcqtk0UxjVr9eHpMEGuubDWXpIElqIqAuA8XG3Bx0DOfEPg7sCN9eWSoTDzu6DCtfQ53xhQhjxw6mRHFYw9FE9e8ogItYmk2wurid8H0FII0LM2hAWzQajbs4m3gVEwCHLMw0JFDSwzNhCdAQZTMPw2Lk2ajeKQiRZHk4IJQl-RcitRkLVXq8SU7cDLlwPmQ6N4myol6n8ut1wux5OoMhgrx_TYD_YVtr-NOcZsp6SA1t07I6wtItD9TlihvopcSGFYmbBsuRldmES7cq89b1wveYGB8DXk_WprUH-cmOUcOkaVdybBJedUv8DO_gSe4-OlMi5kiiE6BPEd0ig8OmsN_ZDAUs-zCVzVEBE6mNjLD_qsHE5g7Xlq0DWhFWpNfkvbKqrqKTEj_jTUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CL7T3FiB5-nnWYwhdeG9OaaKFdv1oXTQJft36MnJadPECt4UH6j_IQEDb_AhbR1Id1yzropHAVq7afOLfoMbEsVCbY34nq6XGeF9BUP-NE-qUhrOdQ5S6U2kNUfSio9pKrPllnAm-PhH1NixIAXI17X8xIjZh4Ino35etc1Jh1iNAyBNrcVli1AQ9Fv0TM2ITe-B-RAX6wY1z1eXvag1YzU4qkfiK0KeSLWBQM_8ColPe5Z0B_Z_mpF6kFH_4AuFaH6hj34OpxxDdkvW0c9cj6TsZOM5BndlsfPJ8BCPjN6CtrvI5lV1QqR46lH9IhL-7TD3ayTV6u3pjZwYXACQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=sh8bj7lVvYQleHeWtQsdJWpe1S5UaEse87r0M7vU0gWPOvwb35g7Hv6RCWk25ycUvoNjbm8GAIldbbwiupoyBtr5bACR34IZ4l7q_KUQV9qYcWifwB2EOqwfFBtIeuXdJLIvJNsY1U_9bVFLEWzHEAMBZlASXV6MkgiAAGwaKuQ0qhIYj6lXaTMODeCQJJJMPa8rVsi_p83Zea2N-yr-OuJ23k6BSm4FxTlMPCW1VGUqZRejhJA58IAOoy-HN-cJhWaBrIZen9sZ4Aobx96QKFWYfuySsAszF83R9k7-ASnDAiP2L2tJKlx120GkfcnyM7IvXj_zDVQYrz54xeXeCy-E9HeTEIl8w8Nzms0dj6yPFxId3KuXvy5cuK3SbiMvK71zCHMptxOQtpPsGIcc5EubOzBb4jnJaRy1Ru9UaYbmJXRTd4I0I5WXADqGX5Y3AMLYBesFQrBawAOCRUBAxz7xvY3YK8bMwpPjnnJe7FuBJSdCRuhbQXZebIUGZLQYc-E_Jw41ETtMb9-y-2IQSXJuATAfn92EhZSFs77oR0i3ah5t3w4ikkPMXsmKyudlYMjHsW5VnSMN_-2refEtKeR6rHoivVYa-7R1zWx727BXnjm9n6OftE32ejgTUMRGlWNQVSQafi4CBLYaoB2jT-n5w9uzkqTsi9bmqkH0uF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=sh8bj7lVvYQleHeWtQsdJWpe1S5UaEse87r0M7vU0gWPOvwb35g7Hv6RCWk25ycUvoNjbm8GAIldbbwiupoyBtr5bACR34IZ4l7q_KUQV9qYcWifwB2EOqwfFBtIeuXdJLIvJNsY1U_9bVFLEWzHEAMBZlASXV6MkgiAAGwaKuQ0qhIYj6lXaTMODeCQJJJMPa8rVsi_p83Zea2N-yr-OuJ23k6BSm4FxTlMPCW1VGUqZRejhJA58IAOoy-HN-cJhWaBrIZen9sZ4Aobx96QKFWYfuySsAszF83R9k7-ASnDAiP2L2tJKlx120GkfcnyM7IvXj_zDVQYrz54xeXeCy-E9HeTEIl8w8Nzms0dj6yPFxId3KuXvy5cuK3SbiMvK71zCHMptxOQtpPsGIcc5EubOzBb4jnJaRy1Ru9UaYbmJXRTd4I0I5WXADqGX5Y3AMLYBesFQrBawAOCRUBAxz7xvY3YK8bMwpPjnnJe7FuBJSdCRuhbQXZebIUGZLQYc-E_Jw41ETtMb9-y-2IQSXJuATAfn92EhZSFs77oR0i3ah5t3w4ikkPMXsmKyudlYMjHsW5VnSMN_-2refEtKeR6rHoivVYa-7R1zWx727BXnjm9n6OftE32ejgTUMRGlWNQVSQafi4CBLYaoB2jT-n5w9uzkqTsi9bmqkH0uF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=upS3jVxdAopSihAJltsf6dVreBLEaEwYi8J9aTruncHDwkswdqTEqmQW4pVl677VYccmdaubjWvdMU_zUfwimmhu2RQ_T_10FPTRPV4Z9-tpmHdoKiV2jBYH1VHejiSJgr0tpswZnvxVU43EkG0tUc-7ZvRSPDvogre91yMHDOw1XiY0QXFJz-hZImszaQFqhpn8wG7Pcf0QQhKzE3Xf1rENRxTJxMxus1kr_IObyjH7tdEGmajlUv-KP9nKF4tG8LzKmkXTnrdqhk67bNZT9mPupmaxx9n4kwqZ6wbRKn9RkdyYB8wBBzDXWepqTmMdSJ0jzOAubrIuF7PeW1IiUTXxsInEja_zEtlLsMDzsV4hyLh91Oli-iUsbPs3fY0QyjHUxjC6nXFCRkbENhdKsUf-TXPWIClkKlshi65wVXWp6LQg-FeFrB-GCry46e4YiyIGnXacS5fnsamooWoqgpQxXcitEyEn-al1deTWp-0AiakbZDFV-Gu4kfvUw9YLp4aJ27i5WrrGZRYb6czmAwNRVXw5XJT_dXbhf-p3kqH3yDD4YCmuCmDZ2WmVzp-BroSlnlAZokJqScEAcNdcaV0uKHOlIQDGl9UB1D_K1R0_Mq3XF7iUeTLHEe6wGnOqBBrLayWs2gijTGkn-1qySYb9IVKlISfBC5nRvr8HdtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=upS3jVxdAopSihAJltsf6dVreBLEaEwYi8J9aTruncHDwkswdqTEqmQW4pVl677VYccmdaubjWvdMU_zUfwimmhu2RQ_T_10FPTRPV4Z9-tpmHdoKiV2jBYH1VHejiSJgr0tpswZnvxVU43EkG0tUc-7ZvRSPDvogre91yMHDOw1XiY0QXFJz-hZImszaQFqhpn8wG7Pcf0QQhKzE3Xf1rENRxTJxMxus1kr_IObyjH7tdEGmajlUv-KP9nKF4tG8LzKmkXTnrdqhk67bNZT9mPupmaxx9n4kwqZ6wbRKn9RkdyYB8wBBzDXWepqTmMdSJ0jzOAubrIuF7PeW1IiUTXxsInEja_zEtlLsMDzsV4hyLh91Oli-iUsbPs3fY0QyjHUxjC6nXFCRkbENhdKsUf-TXPWIClkKlshi65wVXWp6LQg-FeFrB-GCry46e4YiyIGnXacS5fnsamooWoqgpQxXcitEyEn-al1deTWp-0AiakbZDFV-Gu4kfvUw9YLp4aJ27i5WrrGZRYb6czmAwNRVXw5XJT_dXbhf-p3kqH3yDD4YCmuCmDZ2WmVzp-BroSlnlAZokJqScEAcNdcaV0uKHOlIQDGl9UB1D_K1R0_Mq3XF7iUeTLHEe6wGnOqBBrLayWs2gijTGkn-1qySYb9IVKlISfBC5nRvr8HdtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Lm5L0N6vBtpFkUOIRq5_FM8YY9TpiBDKGlrpygoQRdhTooegr2-4HUbjkinSEzlUe4SG_L8_ecGRW1t9iQRHDFRfeiRFy0N0yIbFr_Ak-WRf_n5kCx5_xhPQ9DulOV0nj2KCP2Tp9zNMc_DdOQtyM3cAAYsY45EbSJ6rus-Ql1S0JvKqbEUPRbY7knQ_EF1aQyrDsEX0Z4WE8k53uzjUsJYZk6_Ql47xaJc1m9mxNGxA9rSLMPESRSi9CawPlrvU9HPZPjrLul8EljTJjGsjaALeueRM9tNmqUJCMHNqgoaUO7fQ8lz-m_7_9mYAccnqlFktz1-yRbMpTEY9x3ogXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Lm5L0N6vBtpFkUOIRq5_FM8YY9TpiBDKGlrpygoQRdhTooegr2-4HUbjkinSEzlUe4SG_L8_ecGRW1t9iQRHDFRfeiRFy0N0yIbFr_Ak-WRf_n5kCx5_xhPQ9DulOV0nj2KCP2Tp9zNMc_DdOQtyM3cAAYsY45EbSJ6rus-Ql1S0JvKqbEUPRbY7knQ_EF1aQyrDsEX0Z4WE8k53uzjUsJYZk6_Ql47xaJc1m9mxNGxA9rSLMPESRSi9CawPlrvU9HPZPjrLul8EljTJjGsjaALeueRM9tNmqUJCMHNqgoaUO7fQ8lz-m_7_9mYAccnqlFktz1-yRbMpTEY9x3ogXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=nZEcgkYSsBAZtD-8JsWqIGO1qY_XfICICdgVZbSP-ndwYC84fgsx5cRHGslit2sSEptdaDDRd9OaTIN13eSULj5weG207pYCS2BlAWy2UnGsldxTVtbC_Wsj8yVPNqV3xRG-ZEssEjF4mgaBTp4lN5iiQ-FlP15tUPro23w8_-g2-oeSb-vVHduCAp4UAI_8C6WFlGOA5y2zh07i0t2HzN2Hi2kJYoLqJ_IMygcB3LEcljHii6RbHwe973JLJNdijw_VHJW_VzT_6o3p-d_ubg0xHde2TPE3MgWzN_g-rffOr6pHvXAukKCURB1CyER8bXTI3y7KrGN6fWctYn4Ygw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=nZEcgkYSsBAZtD-8JsWqIGO1qY_XfICICdgVZbSP-ndwYC84fgsx5cRHGslit2sSEptdaDDRd9OaTIN13eSULj5weG207pYCS2BlAWy2UnGsldxTVtbC_Wsj8yVPNqV3xRG-ZEssEjF4mgaBTp4lN5iiQ-FlP15tUPro23w8_-g2-oeSb-vVHduCAp4UAI_8C6WFlGOA5y2zh07i0t2HzN2Hi2kJYoLqJ_IMygcB3LEcljHii6RbHwe973JLJNdijw_VHJW_VzT_6o3p-d_ubg0xHde2TPE3MgWzN_g-rffOr6pHvXAukKCURB1CyER8bXTI3y7KrGN6fWctYn4Ygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=vcVjXkcf926qU1gREltiuz3L1lrqaJCCsY2NC3MY4yDw4DgYUTZuiplv8dk4jKxJBqqoLF1wqSMNgqNri4dbMY1u9iLbt7fFaWmQAXwYKJ17LkMa0svNKeGFLKsI2p5BURVNZn9iyn0uF2RsEfx779S_4dTYH6OaxmVE2pYTRW5WePIcPQSy-m7MI_KKgVDLoEgDADUwkGot7zjOxGAGoY-BDMdGNVE3H779FowqtMQVyjfR_CqCVREuAXYi-L1gUlznKgt8LpOelJodntTq58fysY1XGS8C3nVLkXGe6cHs3WGiW2l4BDwMVa3B5bpqb-mPg7VWnGDfqTx_9DPkqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=vcVjXkcf926qU1gREltiuz3L1lrqaJCCsY2NC3MY4yDw4DgYUTZuiplv8dk4jKxJBqqoLF1wqSMNgqNri4dbMY1u9iLbt7fFaWmQAXwYKJ17LkMa0svNKeGFLKsI2p5BURVNZn9iyn0uF2RsEfx779S_4dTYH6OaxmVE2pYTRW5WePIcPQSy-m7MI_KKgVDLoEgDADUwkGot7zjOxGAGoY-BDMdGNVE3H779FowqtMQVyjfR_CqCVREuAXYi-L1gUlznKgt8LpOelJodntTq58fysY1XGS8C3nVLkXGe6cHs3WGiW2l4BDwMVa3B5bpqb-mPg7VWnGDfqTx_9DPkqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=PYR75aLxnvt1dyJQkz-HcVPzKWkoLxFX2Xa4YP0O2zf5NpeB2EkTmD0ri25nxyGNJCcihwMDSI9skHJUoi0OAhp5ef9HjjycGE8h4uxdIso73hoHqZd2NGGKF8BdxX4QSdjNE7sMcG9veF5gh94mh8TTPcsUdzuzJW7X6hYWy8fCJ8QL0rqECq1kq30jpP5D1Jr57p8fFXfXto21qhFlY0m42Uod3Nr7Nj_ZbcFWeh8o4AycAh14NN16xIQd0WyTz-Gcj5D_golOZmXqXmMeNU7_cubUWIMbmDDP2dAwYoCimcZDkHMjcO3r2BRlYFeEWLYV8GW5SdFasU00gQOc2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=PYR75aLxnvt1dyJQkz-HcVPzKWkoLxFX2Xa4YP0O2zf5NpeB2EkTmD0ri25nxyGNJCcihwMDSI9skHJUoi0OAhp5ef9HjjycGE8h4uxdIso73hoHqZd2NGGKF8BdxX4QSdjNE7sMcG9veF5gh94mh8TTPcsUdzuzJW7X6hYWy8fCJ8QL0rqECq1kq30jpP5D1Jr57p8fFXfXto21qhFlY0m42Uod3Nr7Nj_ZbcFWeh8o4AycAh14NN16xIQd0WyTz-Gcj5D_golOZmXqXmMeNU7_cubUWIMbmDDP2dAwYoCimcZDkHMjcO3r2BRlYFeEWLYV8GW5SdFasU00gQOc2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=rq7m716-K-sjtw8CCDhGDPe9GdcXN-o0kGdkhykNB0LD5dvunEiz6e5Z0ikgvv3Mx1KI_iL4SghqwXUZWXD-aq-KLJJn9_LtwmHsEmGOlUsLRl0Xm49m-sopUR5-a3B-wjQl8rm1wgY5l5yveEsP0GzqupxD56RJgGfoTjLG5br-_ujuSvWynJ4sN94fzWvK-gYG-Qn9R56XVcWRjBz3WEitH1TLq3Wajq_3tL5F8_77zYmofaDJF69v-1eRuPxjlTU2JJQ-P5pSBc0YhDHUGb0_XNISVPOBqF2wp-ldXBezD8f3PyrkNxt9ZCWM8HGYQYADoYbBZXgqodAm76aYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=rq7m716-K-sjtw8CCDhGDPe9GdcXN-o0kGdkhykNB0LD5dvunEiz6e5Z0ikgvv3Mx1KI_iL4SghqwXUZWXD-aq-KLJJn9_LtwmHsEmGOlUsLRl0Xm49m-sopUR5-a3B-wjQl8rm1wgY5l5yveEsP0GzqupxD56RJgGfoTjLG5br-_ujuSvWynJ4sN94fzWvK-gYG-Qn9R56XVcWRjBz3WEitH1TLq3Wajq_3tL5F8_77zYmofaDJF69v-1eRuPxjlTU2JJQ-P5pSBc0YhDHUGb0_XNISVPOBqF2wp-ldXBezD8f3PyrkNxt9ZCWM8HGYQYADoYbBZXgqodAm76aYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=UcNMedgEKU7zrqknw2Q-uLNZKiKUmRU9BDlWZCyN9EuPqjWvjejcOa2rolTSZ8i7P0PZRaC6C6if-EkShspfMU0ft-3wU2Ox5xU7FKJFaAU3RcdB0eSU8LJRThrdGkD4HMibl-mANXgnHs-raG2C5XGEjKkXUTbChlLoMiAS07D-6x3Zfc6-Fs4Hgh0lxzlSxWl7IAIsu8_pxxTkh6uJj1QDBHc2RKM_rbQYSbRLYFs3deHJxTbjdKTev1Gs5vwuhUyS5VxdzOve_fAFGUuEuw0V_j6yfYqNhFVoFgT7d5U4RCTJ8-wFee2wRDFiTOGh6o9fRGjiJFmKKEE4JB7KvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=UcNMedgEKU7zrqknw2Q-uLNZKiKUmRU9BDlWZCyN9EuPqjWvjejcOa2rolTSZ8i7P0PZRaC6C6if-EkShspfMU0ft-3wU2Ox5xU7FKJFaAU3RcdB0eSU8LJRThrdGkD4HMibl-mANXgnHs-raG2C5XGEjKkXUTbChlLoMiAS07D-6x3Zfc6-Fs4Hgh0lxzlSxWl7IAIsu8_pxxTkh6uJj1QDBHc2RKM_rbQYSbRLYFs3deHJxTbjdKTev1Gs5vwuhUyS5VxdzOve_fAFGUuEuw0V_j6yfYqNhFVoFgT7d5U4RCTJ8-wFee2wRDFiTOGh6o9fRGjiJFmKKEE4JB7KvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Yx1fGVjdoCenW3Tk4ttLksMQe3XfCHfYsOEpHdc47AojDCQcKYuiGWe6YaDqMH6w-YRNSHwD0IoWIpWJAxKMSRiahL6F5VQi7acUXXtgGfNEKsJ7nafjWGuHKiKCKjKR3-Z6fSqiwoCvWgjTsKZa5XSTXb9Ll4Wg76oHIzbn9G-dx2jjXP6zb9ICI3b3IxzzmS2tkzfXIxhWRDByVOsEPTVLMvAmAXj80acje4zR7aITIv8Qd-v3I7ytk_6B87yO4ixhN1-14oK1eQLwtXLYcYQluY5-p8fsAgFuCvoj7F0fkA9Z4fZvG5iiXrRkchg8nQ2fexFIcUMzEyfhGHYe9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Yx1fGVjdoCenW3Tk4ttLksMQe3XfCHfYsOEpHdc47AojDCQcKYuiGWe6YaDqMH6w-YRNSHwD0IoWIpWJAxKMSRiahL6F5VQi7acUXXtgGfNEKsJ7nafjWGuHKiKCKjKR3-Z6fSqiwoCvWgjTsKZa5XSTXb9Ll4Wg76oHIzbn9G-dx2jjXP6zb9ICI3b3IxzzmS2tkzfXIxhWRDByVOsEPTVLMvAmAXj80acje4zR7aITIv8Qd-v3I7ytk_6B87yO4ixhN1-14oK1eQLwtXLYcYQluY5-p8fsAgFuCvoj7F0fkA9Z4fZvG5iiXrRkchg8nQ2fexFIcUMzEyfhGHYe9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfagXM5bQwmtDWdh779rBy2LiyO-Dj0oxJRPh7EtHUnQo-BISCoMfxZrMqaU4H2ZCEVMCyRmwIRa0bEYjYCVg6zAl22rPHTmHAWHjgyA9G6wy5dXSLvGB6_4348Wg0n7LBJ29z7nkKemZzn09w7Tbsra2iwFiiI7IDx2rFqZLXba1VLWbnTHQjRzGqGvQ8LRNzWy0a281oD6YRoBz068_UImOpAomz0ALI-949lhSVP_M31znAli13jj25ASipkfWfaOM9rHtsvTegVL9yt8nm4LUp6t64F2qEE2r-0P7RqMioVU2OGXI0_fps_09L4mARKJOxHtnszdJfnqvY6pmQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=HZ9YpAtkd2x9RBLhpgVTlB6O76a-HahFjZBDmbhJ1NwpxDqjfo20QoS2RJVmTw4yDQVK8hCySi_4hAvSkqdC4MpweIsMpTJRdZSciKYTcGjoiXe74ZHJZzT5vNCrnidik5rLiK6d3cHBWpMPc4vkrXOD0vdcyUTFsQcqa8mJ8x4a4nt8NdcIrGCM3O8TcdnFVENOT_SGErIONuqpjIjJkRTHW9u3Z0QJNUadW4VlYpM4cGAZuBHAySQIpdA77VGnMhLPtDIJ9a5X1KaHbXZBJLrp1I2zAWRVfzkgKQHIMgmz_8pgRO06742zpGy-qrua5nALlLunRAQNH5u3O_3XBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=HZ9YpAtkd2x9RBLhpgVTlB6O76a-HahFjZBDmbhJ1NwpxDqjfo20QoS2RJVmTw4yDQVK8hCySi_4hAvSkqdC4MpweIsMpTJRdZSciKYTcGjoiXe74ZHJZzT5vNCrnidik5rLiK6d3cHBWpMPc4vkrXOD0vdcyUTFsQcqa8mJ8x4a4nt8NdcIrGCM3O8TcdnFVENOT_SGErIONuqpjIjJkRTHW9u3Z0QJNUadW4VlYpM4cGAZuBHAySQIpdA77VGnMhLPtDIJ9a5X1KaHbXZBJLrp1I2zAWRVfzkgKQHIMgmz_8pgRO06742zpGy-qrua5nALlLunRAQNH5u3O_3XBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=HcOrdhNq7umGN60tewej-yk3W5Rf0I6g-3qhWlylu8Otd36Bm4TPzRhAWJZgnJOVq6kGG8vPuE8ZpI6JKxV2ovZWxaUNDIzotcJmJYoPhgbEscn-xt-BIk6jzvRKOig-yBto4SbyeZofo5yGSJcGBlAmgdBxYtLMejfdad_d-9DZYa6o_v0xwWkajmwtHvWlZAMNMsFcXToVnTg78eAMmDiAEq51PWRHhkB16pBtMl1-7xUSs58axwZkL1L7vSeBo5fGi_6fseGm00KhFt2OGe34jeqST-x7kN0PCCWda4yEqYCKoml70FoPqGjJWpSemvcUCyNx3x1_S0FDnIMgKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=HcOrdhNq7umGN60tewej-yk3W5Rf0I6g-3qhWlylu8Otd36Bm4TPzRhAWJZgnJOVq6kGG8vPuE8ZpI6JKxV2ovZWxaUNDIzotcJmJYoPhgbEscn-xt-BIk6jzvRKOig-yBto4SbyeZofo5yGSJcGBlAmgdBxYtLMejfdad_d-9DZYa6o_v0xwWkajmwtHvWlZAMNMsFcXToVnTg78eAMmDiAEq51PWRHhkB16pBtMl1-7xUSs58axwZkL1L7vSeBo5fGi_6fseGm00KhFt2OGe34jeqST-x7kN0PCCWda4yEqYCKoml70FoPqGjJWpSemvcUCyNx3x1_S0FDnIMgKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=otX-P5TKms_65XHLClja0LV66YeWUGSpA8FHBcIiK3eZ-a_OdVt5ZOiT6fpJAbwL92hMeBwWV3PWgEGM9KL-rvFfUqkpNeLaLJ5M_TdYVzyW8vhjxJ_xabElaM67tjcnwWMSK_nMfZgHcC31wqVwPhZJVO7k0j_rkXHmb0QqOGxkIIJ95-PBZ8n5mawI8LItDbxyTtRlTqWxLA49bXlwBghlR2H_F5sjmo28rB4vL4V5WbHnEoWtjQm_jrSOgTdfW2xuSuGcY0o3HCmYJI-pWtoRUpiTMSCMmbAuR5STMz_0KkkFPuUUfYP7OCeKxn4JYVTWJHwwUbK06MKsv5j8Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=otX-P5TKms_65XHLClja0LV66YeWUGSpA8FHBcIiK3eZ-a_OdVt5ZOiT6fpJAbwL92hMeBwWV3PWgEGM9KL-rvFfUqkpNeLaLJ5M_TdYVzyW8vhjxJ_xabElaM67tjcnwWMSK_nMfZgHcC31wqVwPhZJVO7k0j_rkXHmb0QqOGxkIIJ95-PBZ8n5mawI8LItDbxyTtRlTqWxLA49bXlwBghlR2H_F5sjmo28rB4vL4V5WbHnEoWtjQm_jrSOgTdfW2xuSuGcY0o3HCmYJI-pWtoRUpiTMSCMmbAuR5STMz_0KkkFPuUUfYP7OCeKxn4JYVTWJHwwUbK06MKsv5j8Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=WusB4TS_OAzNQqoAnJqBdVeOzd0Q3yfxrFIm4KS0F13CPqkNcOu-hQuJ6W0635DQ_fedrYWgwkGkHFZ51IdJbJ-EURVOrr7m3IhR9Sd_NDbljSIwYrp_jmFy64hO8cCCHqW0J_Q-rI1Ey64yj3Td1Lcf_1qL69P6zIZ0TM17zv31TYuj3Gz86IU3IqJ6D_bzVFQoPboHgs9r-CBYSYU334HnHbkhcucxWSA-f1s1iafwgizdMdB1XYcB8c0wy7BhWWYxFkkVNTsdS73-MwOoD0QsFjPwrbM1ICeNvwp3oLvGIL47VTy0kebCvrV86wYTuCPGYjc9L2LNTRDx6L7MTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=WusB4TS_OAzNQqoAnJqBdVeOzd0Q3yfxrFIm4KS0F13CPqkNcOu-hQuJ6W0635DQ_fedrYWgwkGkHFZ51IdJbJ-EURVOrr7m3IhR9Sd_NDbljSIwYrp_jmFy64hO8cCCHqW0J_Q-rI1Ey64yj3Td1Lcf_1qL69P6zIZ0TM17zv31TYuj3Gz86IU3IqJ6D_bzVFQoPboHgs9r-CBYSYU334HnHbkhcucxWSA-f1s1iafwgizdMdB1XYcB8c0wy7BhWWYxFkkVNTsdS73-MwOoD0QsFjPwrbM1ICeNvwp3oLvGIL47VTy0kebCvrV86wYTuCPGYjc9L2LNTRDx6L7MTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evJ-PlxwAQYHurNeoQ5FFigI3DZ-iqRbespQ-2OG37gu2yGxnLnoZajqt7Xl5FbBmz9I_sn0n8uIatsCQensOePK2x_-ZQX4csq_ywlpXZAYPGezngwvY5NpT0MhL9TUPQwj4femAhpq6bqOiB32PKRAxQF6RV-60kvtt9WcIqrCeLQixTMCkDqsE_oNGH2V4MVlUOOcPIqsUtVM9pTowN0W-qB5gBYvbUfNR09WMv9cqJSN-aeIz7USr69g5avw-APlo1IdFVoiUDLk8VsjFcwf4PRkcrYn_wLDvkNDJsDTm-ETFZgejQSSySFm_YfuuMZlr-BW9gDxj-F5_YL4ag.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=YWnQpjRJdQVnqpBl-YqELZE8QxLuYkG9belIDSjm_sI5cQ7DKrkdxFcy_JLPdMKNKtzc2H8rhbhSw5rgLwdsy-PNlvM061iqLt8j4L_NKiov4RPirEXcqW92nheTM3xuac9svlKS2AeDt3FIgptw_qmCdFky3QdRr9gDEhi-V68qQyj5Wflxl7bufzvMAee8P1esEL2yIkWf7lveNwL3seBiFSt-f9ZinFpfA3PDrOMXSzSA2mfQCae-ZeevSAvd0AklN1iSrpSo-KhehLcsycm4p4ncOnNc7o95znRFqJzR8YXLqrbPn-c8anjtYEScoYqq48wB5to9LiaIy9gE1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=YWnQpjRJdQVnqpBl-YqELZE8QxLuYkG9belIDSjm_sI5cQ7DKrkdxFcy_JLPdMKNKtzc2H8rhbhSw5rgLwdsy-PNlvM061iqLt8j4L_NKiov4RPirEXcqW92nheTM3xuac9svlKS2AeDt3FIgptw_qmCdFky3QdRr9gDEhi-V68qQyj5Wflxl7bufzvMAee8P1esEL2yIkWf7lveNwL3seBiFSt-f9ZinFpfA3PDrOMXSzSA2mfQCae-ZeevSAvd0AklN1iSrpSo-KhehLcsycm4p4ncOnNc7o95znRFqJzR8YXLqrbPn-c8anjtYEScoYqq48wB5to9LiaIy9gE1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Nu0zX6h6a5rGM9qVgvqaFmXY33XELWDFGgyXkHqwQVOC4AMEcDO6hR-geHqAVosOScJm8ek45HeXeILkTIF7nw_Q-jpZZTacFj-XKZ59-fyeNfIXWqE4clPn095ry0egCAn1sals8UVLiSJKHMZUnKbVnx6e2krNq1ifOQlji3HLcM3h3E6LhHhqaxEg8jCOYYoQ_9tCD0SznGUAptGSYStGnBHSs_GJ5RzEnMKNUUGHOUJRKwVtDihj5THHcgqP2Yd1TXyibeNQar6Yy1tOHyNlXck-LbgKRYRpMzI9rCbjRpb0gSAjnNNs04-AOqU3dyZiXIQYY27Cb-uD6lMXMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Nu0zX6h6a5rGM9qVgvqaFmXY33XELWDFGgyXkHqwQVOC4AMEcDO6hR-geHqAVosOScJm8ek45HeXeILkTIF7nw_Q-jpZZTacFj-XKZ59-fyeNfIXWqE4clPn095ry0egCAn1sals8UVLiSJKHMZUnKbVnx6e2krNq1ifOQlji3HLcM3h3E6LhHhqaxEg8jCOYYoQ_9tCD0SznGUAptGSYStGnBHSs_GJ5RzEnMKNUUGHOUJRKwVtDihj5THHcgqP2Yd1TXyibeNQar6Yy1tOHyNlXck-LbgKRYRpMzI9rCbjRpb0gSAjnNNs04-AOqU3dyZiXIQYY27Cb-uD6lMXMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aw9LmK1lp_qkpwu2JWxCcC8CfQd5tEI_Yp4wf8yskZ3a4_H5zeMuFwQYxAePNO0YcyROF70_fHfocVi_3UkDuZqP7-gy6dJgDGTtpNDW_WjC6jcrmBm11lI4JDMfVmfoHciIsMwRVxNqwCGxooZbXIltnwq7cKRJC1C9N01lBfOGa_pVUhPPZecaZ9fHeY1KbRhnwoU8_o32da9_A6m90_jpYHYqUchk0Vnpf9c5AHDfoZ1fas53zQ18oHav9cWJhK2FQ0L2axRj7sTuuT0DwT_DFCwkLvWBkOeSq_QQqXZGeufe8c1yIFQQhFR_Op3RoDBBrx3lBJIYGuD_XeEKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVMHfR7sWEzGrcRhJXhQmeJDjC-nTMuuGqpGssYZDL5-8dGc7LKxZATLtdjMhUf5JbhmjnMv1Ed8jblPzT2NbO4mRKb0CtqgX-yPhYGNtOlKbSMnkDSc2aBBYYFZ9beaIPtDqT2Q5OGgYFyKP6Fx4Y7pDNFzd73HWOV0l9oOfVHO3YWT473g4Owd91VUESRQs8-OHZd50_d3Cd2xZugj52SqePoyfx2meKGs5pBjF4dCPhGo7ZdQ1oHrf5pRjgpWyZu5WOxDve0acRTt517X-80MzUhGdacI-haC3mWhrT7bPB9MQTHY_UDQXLucGeWbQ7xB4mVnP4ho0VJiMVNDSw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=U3HdmOhoYVFkwZNkLltGvn99W6iPK3cmqS1m76-qJGAh44Xp7ZqOH6WK2yf_C0i8XzcNQ41vzhmLi7isf51SKOtpTVeDNr10u2U0ZZGEvM1KoyJyedt5t-hlWUNQbisxJ_WX9FlclRtuoukYgto0Hm6yw2AtWGazIzxLlGhWI1oNymU0lX8A__bDdVJqwARpk-XLURmI3BvVql5jNrNJz3DFPt3lA4Up7JItsO_5jMmK5ci2nUKEYiNs9qjb2H29-r_qNBVmoCKKp8ktKmTi6VGjdueWLppCHFnMQundbVjvBTYWTKszfdX-MGK5dj6GNLSL82tQTVTZdcG7FA6nlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=U3HdmOhoYVFkwZNkLltGvn99W6iPK3cmqS1m76-qJGAh44Xp7ZqOH6WK2yf_C0i8XzcNQ41vzhmLi7isf51SKOtpTVeDNr10u2U0ZZGEvM1KoyJyedt5t-hlWUNQbisxJ_WX9FlclRtuoukYgto0Hm6yw2AtWGazIzxLlGhWI1oNymU0lX8A__bDdVJqwARpk-XLURmI3BvVql5jNrNJz3DFPt3lA4Up7JItsO_5jMmK5ci2nUKEYiNs9qjb2H29-r_qNBVmoCKKp8ktKmTi6VGjdueWLppCHFnMQundbVjvBTYWTKszfdX-MGK5dj6GNLSL82tQTVTZdcG7FA6nlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH3l4wa7Net9LCL7B0jl9Zcho1xXYBSET54wMhCUq67HhVDClx_EhWjOnBCjIiUbvpkd2zgbaHJDsV_xjUPV6fETU_AXTnEYrdi4CIbonkMo_qXQUf55P8-C0CwJ_-BWLAbntPvh5qEXW9eYhNVaKOLG8k6JNh_n6f3MtjEoXKrDuWQ-06NGMPjwStktSEMAYrWX6yDRGywP3i790dH-AGdk_ZKtUaRWgafZxieZ1Uw7rvJQNg_i628PPD8z2U5kFfMohQFEcK7GoP_Da04-cuXsGZSukVaFe11ALEpW-D5BD8pmsLsAqpx6j26j6Fa_bHVWnAh3DZqbB2rXu6mxug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPaJUlCxH0l7Hr24I6VWamNbetGsWebt_71tgreC_fkUdtWFxT0rSADPHaWiakMNwAZfmW378_PpwGcAUl_-9mXiPUduwfcMC8qFCs8Cku2RNkKL94unwdzK_ZNv0sQWPoUGOEKA2KtVbiuakIxkItlVeC5vs7FwkJLu0F9ZAR72J3UgTskqP_c7Ia94uLWB_EFW883eyCwYGA0BLryp4kNYu2twToEW6YyeUgMui-gkV44FKmXC0SY2gLnFOSVfVG-6hIU7vrhAH-oTlu-9x1qWOERMQQ0hOFXGdB8X6a_1IKJlXTd0pBhbbVEvJZCDX-EKr7fZVdQIsReMHKVK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYMBtLpLsv4QAyASpopbQ9D3YncpWiLM9VOsmCBJZYFuueljlQspxGcuKPh-LAxs84WXRAY8Ty7AC4XI-xoF62aTNkqHmkACsGy07mJDH6jfqJK7OPqnEGH6XTwpkFIZja4VrbGGX6FZqU3hR7CUKYPqiPmjFYq9mMOP69eEezDYcsxhcFtTeKgT1DLaCLgPKsKInYYOPU7pE4uOYSpPlSyh_sT0Uqd18V88X-f6oOUUbGAPEHEEC9FZKlqGcBPx6uClzHvP3C56QStuXOmHOB8c4OCr0dA6fJSIFJm3ykN_KzB0MpM2x4jAhhEnk-jSegb9ImB4qtHmOD5o-9KlLw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=j5yCxyKdR-5bn3oA7wiEu7VwNvkwy75VfMUeOMNdvE0WnAtNrH3A7THFHU6CeBasFtd4v0E-b0CSnHYfX89yMi73Z4RsS1HZmpwrK2yH0Cqeafij7Y6GZwJWRRbRDHhbE8sFZc1aOmUFMB-c5NGIuCbZ6CVE9VsJpICDNagMiWTxUFRS10Jwk5By7vK1qy6gvO1u6zFFh9xIpMa5VSK49qaZTnG7Sjr55DJYhI6PSNV2tYql28uziddplxGEtrojbN49fI0NjqnTaE5UevjXylSJRZxoHhv8FOAOhJFtABEBrbxjaQaz7esUGN6Ot2L743AvO9Ba27rIpHjBqxG5-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=j5yCxyKdR-5bn3oA7wiEu7VwNvkwy75VfMUeOMNdvE0WnAtNrH3A7THFHU6CeBasFtd4v0E-b0CSnHYfX89yMi73Z4RsS1HZmpwrK2yH0Cqeafij7Y6GZwJWRRbRDHhbE8sFZc1aOmUFMB-c5NGIuCbZ6CVE9VsJpICDNagMiWTxUFRS10Jwk5By7vK1qy6gvO1u6zFFh9xIpMa5VSK49qaZTnG7Sjr55DJYhI6PSNV2tYql28uziddplxGEtrojbN49fI0NjqnTaE5UevjXylSJRZxoHhv8FOAOhJFtABEBrbxjaQaz7esUGN6Ot2L743AvO9Ba27rIpHjBqxG5-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=GaKmmtH3s969POJTEvi6CvOuNTgNU0i9xGbGnr3-HiIe3bf7o0wQixCc08mDuLuFjcUq80P-Lgl2Rf7kKiApLX1pLX77MsXGiTHifSTEfs4s9z_4xX53gXi9HI2VhJwn1DeiIHn2wixsuZEZcdsXNU2pd9IpYjpswh8VnKJCYlq4Bi5PCuECI_hDPvoxHiDIwltBiyPdSoCXbwh_bJ0f0H5hIIQbm6l3J_deMlrVBtDLwoSbq8FxTJFhtjCgJU9lO-LV8LJcGvpq0d-qeMVzBIDZvlj-gtB3dH_s4RzFwvNCHNeWki7R8qbi4wk7yHGpY1zvjukH_fsvLGuz2Xo1hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=GaKmmtH3s969POJTEvi6CvOuNTgNU0i9xGbGnr3-HiIe3bf7o0wQixCc08mDuLuFjcUq80P-Lgl2Rf7kKiApLX1pLX77MsXGiTHifSTEfs4s9z_4xX53gXi9HI2VhJwn1DeiIHn2wixsuZEZcdsXNU2pd9IpYjpswh8VnKJCYlq4Bi5PCuECI_hDPvoxHiDIwltBiyPdSoCXbwh_bJ0f0H5hIIQbm6l3J_deMlrVBtDLwoSbq8FxTJFhtjCgJU9lO-LV8LJcGvpq0d-qeMVzBIDZvlj-gtB3dH_s4RzFwvNCHNeWki7R8qbi4wk7yHGpY1zvjukH_fsvLGuz2Xo1hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=JcwFmRTMymMyJQH27F9ytc47Bcshx9IsX0B6OyAmM6v3gMcTkvsJO8fqe6cX3LWHMYShM08sHDZPHsJo7pgMUppULgOaN_TEnf0mOMqEyJdMUI0tDS6C1WPL9SFoEJe5GQhwZ4bbF13OppYS83buqj1951uMOOHUGcKAP2y9j-wZ2jLLnbqeQ7ZKr-CoHHDoN1GCkpE9gFOC-fu-1KmgGfDzEPBuqWdNYLZ75yEx7ScRquOi3Hrw0cI4hYl3ew4iUVqvFm7vIvzazioDlpBjLNgBcmsYFranQFNpS4NCAGO-DplJ8NboPKbwBT3pfW7y15-VIzmn3Z8sStzo3En9960sFZua2QHLW8tNI9gEiFqfLGpiSaMIUsPUUsQ2BzUKWUUlqi-T0M8X0aDyMJCBkiAEzf7Q9FnaUO7JDvTrZoANM_T3CED2am6KImhZF6_bUfPepP7qvyhTF8OKZKwk0D_sy4s_Gu32M_hUp4xkoCNiZ9HkSoV95Wn03lihNLNH0fbUMGHm1vQByCBHz0O7m-Lofno-UKmLsTdA62-Bo-8xfY-Xr3KAMGajmvWTSBwA-5LvyIOrzG0ftVJPq2f0BuwWfKvsOvm-PEOSQR_CenhXbt1RQxRCNn2VqKFI1aNjgXfUjAcXVIyRY7WdvjimXkn1iRsID-JBJ_qm8x8rfc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=JcwFmRTMymMyJQH27F9ytc47Bcshx9IsX0B6OyAmM6v3gMcTkvsJO8fqe6cX3LWHMYShM08sHDZPHsJo7pgMUppULgOaN_TEnf0mOMqEyJdMUI0tDS6C1WPL9SFoEJe5GQhwZ4bbF13OppYS83buqj1951uMOOHUGcKAP2y9j-wZ2jLLnbqeQ7ZKr-CoHHDoN1GCkpE9gFOC-fu-1KmgGfDzEPBuqWdNYLZ75yEx7ScRquOi3Hrw0cI4hYl3ew4iUVqvFm7vIvzazioDlpBjLNgBcmsYFranQFNpS4NCAGO-DplJ8NboPKbwBT3pfW7y15-VIzmn3Z8sStzo3En9960sFZua2QHLW8tNI9gEiFqfLGpiSaMIUsPUUsQ2BzUKWUUlqi-T0M8X0aDyMJCBkiAEzf7Q9FnaUO7JDvTrZoANM_T3CED2am6KImhZF6_bUfPepP7qvyhTF8OKZKwk0D_sy4s_Gu32M_hUp4xkoCNiZ9HkSoV95Wn03lihNLNH0fbUMGHm1vQByCBHz0O7m-Lofno-UKmLsTdA62-Bo-8xfY-Xr3KAMGajmvWTSBwA-5LvyIOrzG0ftVJPq2f0BuwWfKvsOvm-PEOSQR_CenhXbt1RQxRCNn2VqKFI1aNjgXfUjAcXVIyRY7WdvjimXkn1iRsID-JBJ_qm8x8rfc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=O_I2UP420oiQk_HJVdoV9PPt3FfZd_RpYE9-nWels1IZ8FD0uxhBdCk3TRPFkTmwKZTBk7QPeOLHpmHiq5MUs5Z8PjLIN0i4ns6Dmq5U4J4DxrpKGQ1XIHScH-zeVaCf70YbByxZUUzqE3yw67KBfCIZKUtmGUg7W3GIW_FJCvBhGcTyUnwyFaA17Mzk20AuYWtsHNk83PnV1nEUtj4J-iqH5rZzCl-Q01N_H9SCK7EA5V-O7nycS5I2HBz4t6TvZ8WJCzb7g3Xxhaq_LDQds-YpYod_K2KqySlEjNVwMX5ILA1gk6MP56zwSsFupM__SB9ey70ITpApQJlmCGJGOqxEvuC2VQOSGzNW_H26KGBZ7Ik5xbr__rDkCdMjEqK32z4o5wfKMAn6d9arhuxCxI_ODcO8qSpeRgb_Vw7yfaBuB8kOBwLDAMfgJbYvi3nAvn3A9wRwBOAvc36OLzr1hnGDIQpBt03toX6HXToR0mIJjuIj0nEcE1GRNZzGRUy006U1L6pD07ZK65SPIphV4NRHM6B27Md8wQ4P-gI7BtSbKfE3AQagdX5hEqxmNP5wIwqSnNwJfcKo0V6FDm6s0k-cIMXMgR81HtlszEJRFoBSLzEf09VueHeVPoWjkmfDSVvbAHhGvOaiPCPfe_DgtpYd60VKh2wEQemr9N6ZFUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=O_I2UP420oiQk_HJVdoV9PPt3FfZd_RpYE9-nWels1IZ8FD0uxhBdCk3TRPFkTmwKZTBk7QPeOLHpmHiq5MUs5Z8PjLIN0i4ns6Dmq5U4J4DxrpKGQ1XIHScH-zeVaCf70YbByxZUUzqE3yw67KBfCIZKUtmGUg7W3GIW_FJCvBhGcTyUnwyFaA17Mzk20AuYWtsHNk83PnV1nEUtj4J-iqH5rZzCl-Q01N_H9SCK7EA5V-O7nycS5I2HBz4t6TvZ8WJCzb7g3Xxhaq_LDQds-YpYod_K2KqySlEjNVwMX5ILA1gk6MP56zwSsFupM__SB9ey70ITpApQJlmCGJGOqxEvuC2VQOSGzNW_H26KGBZ7Ik5xbr__rDkCdMjEqK32z4o5wfKMAn6d9arhuxCxI_ODcO8qSpeRgb_Vw7yfaBuB8kOBwLDAMfgJbYvi3nAvn3A9wRwBOAvc36OLzr1hnGDIQpBt03toX6HXToR0mIJjuIj0nEcE1GRNZzGRUy006U1L6pD07ZK65SPIphV4NRHM6B27Md8wQ4P-gI7BtSbKfE3AQagdX5hEqxmNP5wIwqSnNwJfcKo0V6FDm6s0k-cIMXMgR81HtlszEJRFoBSLzEf09VueHeVPoWjkmfDSVvbAHhGvOaiPCPfe_DgtpYd60VKh2wEQemr9N6ZFUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=cPM8HVgezl4PS-1xmWReLzfSslJy_SQyl_W-c_YFObe95tbr_7oO5OpC8Z5HEMqMM_y_4v0quxXfjbTYakj3Sb5rRKESiY7pftJQxfZJy0p4ihG8zmwALtkwkGfs84EFfJNWcWaxK8H3y00B_2AG549xocRZlXkhFsMqq1YcWBVk3EJfTi-BUbOF0TKQ8oToXwEZKVROSvFZZQatcEe3yqJPhkkSKFDvVgpFBFTFuPtYOO-MP-G9LjRUXlGVOFdPETpVZQRIkQwTL2lVRYEjwJFp202jdC-whlSFUscmuEYOiEZbIV3rtCBqrjKJ45FcujprWxjnWUXqD3j2a_7HGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=cPM8HVgezl4PS-1xmWReLzfSslJy_SQyl_W-c_YFObe95tbr_7oO5OpC8Z5HEMqMM_y_4v0quxXfjbTYakj3Sb5rRKESiY7pftJQxfZJy0p4ihG8zmwALtkwkGfs84EFfJNWcWaxK8H3y00B_2AG549xocRZlXkhFsMqq1YcWBVk3EJfTi-BUbOF0TKQ8oToXwEZKVROSvFZZQatcEe3yqJPhkkSKFDvVgpFBFTFuPtYOO-MP-G9LjRUXlGVOFdPETpVZQRIkQwTL2lVRYEjwJFp202jdC-whlSFUscmuEYOiEZbIV3rtCBqrjKJ45FcujprWxjnWUXqD3j2a_7HGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmwZZg9fouJzf1xyXrN5XAoVR1opgPcPONbqfYkK_v80_KTyBSHwUyVO_vmdsD9gvTp6H6QfM4LW_amW3my7zj9ntz0qt4EeyCXWDV6o5jHclGeAlaPpyTuJlb5tlyEvX_SpLHegE3H7alM0dRYuZAMSH0Nvvp16DUSue5-bUn8c3cTeLUshtCLyN2xgD5lzgwPhS2hA5vM3eHWKG0avgDok_CTAx9qxio1tKKjt0gylSXN1OPxGfvmHmsgNuQgB2cyWPoiPMozw4LGxClTlEC28XF5jMVoxul0aFTMHB4bsDt6sB0zJTfvca0CMSZ3-4Y6VTbkQzXfeeO6S_okMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
