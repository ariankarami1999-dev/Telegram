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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBtnZtxfvmkZljS1X5mmsoi_3aQ2dE63LF_VSvZ8cHrMjAr4it62ivKnNgr7jnYcgNCwMKplZNtMWhxiJVIVSzPwyfPynGJGfLtPliG6xfHO8hSeBiHSOlQr0LRiLrzWDPh4Yhg8-miQoTL8M21SFw47R6AIApFyJenct6mBDibvvcEADDa7AMS5Z0HZyfgNbQ7IPWzWxyWLtXUiDY0BOehBGwlwOwcKv3AKOUTCKZN4tbHXHyIX_7e0Qno8X-kuw7gOUTRudhpn8FOpR_g8mDHmSBtI_EuCrEXiBYvrZAwv2_K3PtWhKb1woeE05zJPoEQP4F19UVbJSPyGLkcxDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IQLg7nuLygjfOtOuPEQlzE8bi3Hky6-lcp_cUjsNdhg61kGoOS4PGXVc_gmxF3ri6MCMffo3XKEMzdC6vE0BVmrjDFjuJX8DH12P7jYGabMznMTvfSBlmaLdzdx1enk07F-D7kwiIF8oOoFfRXHGGw7iCCPA6Rf6eZA-kQP34sKCAtEZSSIU5lnmcPFQ_0_tPpAxWOJ6Pat2eVN9VriVtdM6WgM3fB187zKzcqtECnpmLoqJ5kkv0CF63GIze9pT1CPVsXlWDxal0kmfZaG2UwmG99gO8mcdGuRVJbvdbcLmKht1nGvD3GP3CgIJMwxhOLE8GXUDNGNfRjS0zRHnbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HhVpbk_73WLwwQXYqv1f01kqTkz3uvRYVZnkR-44r5vePct9H49mNWY4ak9SqLy2JI4UFu02ZvkEkgGDIMTe4cAu5cslNypRfMiHObYP26xxoPaVV0sjUZkLo7yN7hFPdYapn539hJ81lh3F3K3kX5otmNGHDVxrnJijnrFphdOZJRJuHlodrRo4Bv6-W3d1drY-Em3rIrzKeyIwV38ErbeRiEqa4cOKwx_K9ZpnWUh841mnvfqwLRwjwbde9g2anuc7-vxRA4XJXyqBJuwfaCJK7RZgFFY-9aVPB0Q-HasUQeSrfo0khammozanrzuhiaSo5D58P66KnW5deZ_VMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=A5BDRlbYSvChxLkKxFdA1O6jKbPPlcUsfJ2iRMOxgyslryIjlTrwiSYrzCN0KHqh0aL6t1zAoVtb1sh1TsTr4Olit3on0byItieLsS2FRDCSvUi7azdER7KxMxoavvgmudeLo1iPKfHbiSV1Jxgp_mqsrIPLOkTiLDQBza2uooGStx_UEiCjSHX7s4m5U2MQcBHelL-0AtiQmxzehHK1fwYv6aEmOXEZb5aN5NYjmLVtnQHezk0gyDmXSWRIOfOFemdTnp-f4B8vde2hVsB00lvSGC60mVdnZ8tKiWAXD9nFmkeYmp_igbt7oAoCwOUKmSAdQLPgle7jEGW2jbg2Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=A5BDRlbYSvChxLkKxFdA1O6jKbPPlcUsfJ2iRMOxgyslryIjlTrwiSYrzCN0KHqh0aL6t1zAoVtb1sh1TsTr4Olit3on0byItieLsS2FRDCSvUi7azdER7KxMxoavvgmudeLo1iPKfHbiSV1Jxgp_mqsrIPLOkTiLDQBza2uooGStx_UEiCjSHX7s4m5U2MQcBHelL-0AtiQmxzehHK1fwYv6aEmOXEZb5aN5NYjmLVtnQHezk0gyDmXSWRIOfOFemdTnp-f4B8vde2hVsB00lvSGC60mVdnZ8tKiWAXD9nFmkeYmp_igbt7oAoCwOUKmSAdQLPgle7jEGW2jbg2Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=OUWOerXMY3raKuTBUr4wJWIKyH4j1YMa8znR6wNYVzMnV5NO1dlUQ_Ts-2chkfOV4QWSlTaj24fq9_5CZiQd_SmFqAq8hWa4-ZnfhADo7qz5SOCF2aD89KF3kX4Mlxvhe74mqePocOGsNhXny5GSEo00Aj3wAESFdQJ5sJbEs9cAVkh6jxWo7VJ0E8oNcGzyHq7XsrJn5A6VUynOZiiJd_8X4L2PDEg1A1GmBpb2Vz3a6GbrK-V0WRKuddRxt81UL6aIO1Soo8j5i4Sg3uDISAr3tjLO_d1Kbsz3A8fiuiUCtV28FRrSLFw4Z-gxab_2RReiIrlJl_dMu7HcRNnnfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=OUWOerXMY3raKuTBUr4wJWIKyH4j1YMa8znR6wNYVzMnV5NO1dlUQ_Ts-2chkfOV4QWSlTaj24fq9_5CZiQd_SmFqAq8hWa4-ZnfhADo7qz5SOCF2aD89KF3kX4Mlxvhe74mqePocOGsNhXny5GSEo00Aj3wAESFdQJ5sJbEs9cAVkh6jxWo7VJ0E8oNcGzyHq7XsrJn5A6VUynOZiiJd_8X4L2PDEg1A1GmBpb2Vz3a6GbrK-V0WRKuddRxt81UL6aIO1Soo8j5i4Sg3uDISAr3tjLO_d1Kbsz3A8fiuiUCtV28FRrSLFw4Z-gxab_2RReiIrlJl_dMu7HcRNnnfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtLlCM4hwdPLtGl43Gzoki7K8jPER7CvXORiBUj5o9EMTZc5nIPp-bNJZZgNOVPvFGEOm7A-FuLCqJwI48F8k1mkJ9-GhMrrtmp70Df6_s2Fq1OSM14jzGG5Oyvj88rMIZUP3rILfwLai5lKTPqXmZR5K99EmYDo9xT0B6Jv5EWuXRd4MNtP3urFpfFJ1IIpMvygpBNSF-WbbpSCnT7uC70Ahk0dsuzwf7Myh-S-yWvaG23DZtlQgYUNyxerKI7aEIA-ZU-KhXwBTzGFPigJdOr9zuORDtpzGAb0WDBbBwjUQnI0sWPaqBhqSYtBj2L8N_EpXRM54C8GE7ivIZvh1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=kMgv3tUjSSBuWRcJl-dgHYOg5tvzryStl1jvCmAzbtgAj4qYSX_2EG5rY-Nyy7iBxw4uV97rVyC5uMfYmzM7kT-9K9y3VSzEv2aDR1Zyzr098gZ8yCxSrtP1tCvkp-J1_OyqKYrmb_AKa2zE0gQxwHnaoqo7fvxld1Tu2aIE-Xf7LGkk_7jN3DQCxET-aGPnOHSJwowtRmSxSClXlYXfa8JnZ9mFPT5neMYICDW60CIsaPtkLLUOy2QWRHgCaWliPNDjVS-5Fr7-gJiIkwWX4qFh1vCEXo6MxuWDVCG1lhUQQxr1CHlBln1k4NV-5IlYcIYOc9IwkUQ1d-JCLHHSpjr9C1ZOB7izCbc-tF0C5nihFKPNCprBdcTM6ju2hwVbvHwh5Gs0BE0T2jJlBvbJ9D1mK58fx7UoLxjABSN-RLs8H0ExLhFgLf3e5JJw39b2PSIuOzer8uySwl_4BuxH7Z6BgKcw0VMMMD3LQZL8zyDqQZgCrqftBhXRHD7E6E0nnBgfqNIvUCEnzZzQkGZra3S2wEjURsuTkFJle-BrKn9aSYm0AvCbliactcebEXGAWcflsGQWFLg9RlVjVuDSVCCXZ_A_Qtce3knAjyJUID9n1kIIOJ5vtSLME2fL9qJwwcRjPOKpK0MCLmuFyD_7siH46el4SRbeVHz1Y8oQsdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=kMgv3tUjSSBuWRcJl-dgHYOg5tvzryStl1jvCmAzbtgAj4qYSX_2EG5rY-Nyy7iBxw4uV97rVyC5uMfYmzM7kT-9K9y3VSzEv2aDR1Zyzr098gZ8yCxSrtP1tCvkp-J1_OyqKYrmb_AKa2zE0gQxwHnaoqo7fvxld1Tu2aIE-Xf7LGkk_7jN3DQCxET-aGPnOHSJwowtRmSxSClXlYXfa8JnZ9mFPT5neMYICDW60CIsaPtkLLUOy2QWRHgCaWliPNDjVS-5Fr7-gJiIkwWX4qFh1vCEXo6MxuWDVCG1lhUQQxr1CHlBln1k4NV-5IlYcIYOc9IwkUQ1d-JCLHHSpjr9C1ZOB7izCbc-tF0C5nihFKPNCprBdcTM6ju2hwVbvHwh5Gs0BE0T2jJlBvbJ9D1mK58fx7UoLxjABSN-RLs8H0ExLhFgLf3e5JJw39b2PSIuOzer8uySwl_4BuxH7Z6BgKcw0VMMMD3LQZL8zyDqQZgCrqftBhXRHD7E6E0nnBgfqNIvUCEnzZzQkGZra3S2wEjURsuTkFJle-BrKn9aSYm0AvCbliactcebEXGAWcflsGQWFLg9RlVjVuDSVCCXZ_A_Qtce3knAjyJUID9n1kIIOJ5vtSLME2fL9qJwwcRjPOKpK0MCLmuFyD_7siH46el4SRbeVHz1Y8oQsdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=jKAtg2GQ1PmsV_ygY89p4EbtxGz2YikYhU_LhsBUdlZoJJd6xzuE-XxwCKsA3ZqLp7U2TgI6bffbY79ZKcGdVAi1x62gdf_K-Hs8CLB1nX-bh2cWihESuL0I8l6H_eP4PlhF_aYrQgM33LzOmJRanktSTCblsHfx92IoOXcPHJ-uQDtLjuddhECcWZG7IstMo_e8cc8DndVRJn3eJVH-TNNkiuduuoj4V275tqqlgOmjPxQLqNz6TYfb0nRdn0DZZq4lRIIQojXms_iJyqG33N9o7xqgrCAtH95xmiJyhn4fsLMm0D8-i9OQ8F7UoB2XSD_z6XvutL3r1MKNIw-08Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=jKAtg2GQ1PmsV_ygY89p4EbtxGz2YikYhU_LhsBUdlZoJJd6xzuE-XxwCKsA3ZqLp7U2TgI6bffbY79ZKcGdVAi1x62gdf_K-Hs8CLB1nX-bh2cWihESuL0I8l6H_eP4PlhF_aYrQgM33LzOmJRanktSTCblsHfx92IoOXcPHJ-uQDtLjuddhECcWZG7IstMo_e8cc8DndVRJn3eJVH-TNNkiuduuoj4V275tqqlgOmjPxQLqNz6TYfb0nRdn0DZZq4lRIIQojXms_iJyqG33N9o7xqgrCAtH95xmiJyhn4fsLMm0D8-i9OQ8F7UoB2XSD_z6XvutL3r1MKNIw-08Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKgYjiYrFdjQPIXlTt3ZHgDdUmQ4D2zqfg_CnO8hlRnq5HobmqStYMXNfqrKSltSAum5dpR2WmBxY3IBZBT58zc2J7VDA5Wskz4pVtuDCJ6Yebzq7-jshXfLCA_eWJgR7-9YFrO-F36vsd7lU4_GftoUQgvTR3vS68OIBPcQK9Uud0Z99gcjmcbmh0PcWv08xSdipZpXClAaoABlKIgxWV5fnElMO5o1dfxjgrRzVfsGhJkeBKXY2lcPyuEXGcML1kyOaeyr8-Uuts0C86PNd-JaU46Ib4Un0VOvCOTXHHOUXAg2W9u9fMiW8t0w95AIT3d78sDgCPJZTLM8C--2BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=DPMLM2R0GNHZfNTiebGuDEukHsSbSL41fGgPlgEEHRKwpkjeSNt8BlRc30iMqWWAmqWgtnoaChN07Pb0cUSOYTlaoXZ7Ug8HwH6HvBEV6usipvNseAL2_MI38Or2ari2DkxKWuIJ_U-BugSC44KYzR6ahpJB9ei8yLckZCb3hx83S2iOIUcxj9_aGdD3PxoyPtxkUbzOGQlLdWDssG3386m3dI9irmgQOBRBwm9JhONnEMiTb-zENmKVwTrmHuLH3eJHkpvOqM9ZiqXklj1trkrRsGwWpg4DSTNa5qy6jDE6oAP31HRAMRibCKmKdMwMsDPAtTOzvPZkfvVy9GyaaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=DPMLM2R0GNHZfNTiebGuDEukHsSbSL41fGgPlgEEHRKwpkjeSNt8BlRc30iMqWWAmqWgtnoaChN07Pb0cUSOYTlaoXZ7Ug8HwH6HvBEV6usipvNseAL2_MI38Or2ari2DkxKWuIJ_U-BugSC44KYzR6ahpJB9ei8yLckZCb3hx83S2iOIUcxj9_aGdD3PxoyPtxkUbzOGQlLdWDssG3386m3dI9irmgQOBRBwm9JhONnEMiTb-zENmKVwTrmHuLH3eJHkpvOqM9ZiqXklj1trkrRsGwWpg4DSTNa5qy6jDE6oAP31HRAMRibCKmKdMwMsDPAtTOzvPZkfvVy9GyaaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1GJ9skhKhUXEKerLOmDC0V9jXxQ7sv8k7hzEyqnHQmeGvgoFtr_Hkjnyxd3sra67O1yK5Wcl2Xn120g-d9SbiTiyEfBlxeNYI1VYHcHs7ctfRTjfwwwt2e1QlLUPU_6ZkZGSJO45S0lykk6Vu5pE6XU7S3rLGcUnHqYD9neS5GUtofDPCe491HwyGc8J-kvOzPWj1-WXx5ynORiiYtkVKeb6A_c8uavOFiOK-8Pv-DqXQNwlE6YF95_3Xte4QMojdrMuHNZiAUtG3cN5wEeFLIzK_W9DPdvexFCCJ4TlpJUKN1uA1oALYGicZqgNmaNBauBbh84yTzKkixPrIuAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KicrxsOPp0okgdkpTNXiOywH1xlFli8jbSZUgI4lGO8zXJkIHTMe3dgLA5dBh4SekLfMTkdoTaSVt4XhLYCoX_cQ5clVG334cDTJWMEUFxscuiHM4s0LF2LWd6d-jLqT4YYeRqOkN6wmadu8wcFLzxZgWUtQgBU9hJtCTFVYMiEy2kOfK-mkLVr3PIjW1uwuUASKH8jh5WXVYJ3T7NRW3gSFwO1GJ90Hwz6E6QKL4DEPFKnXaUMPQJFSEsNgydNEeyDo3Ry3bZ1fz8Ee-U79gBLsrTJyJ4oVDj1q3vLvLOfK4xGI6xtHgfFky-gKEQeBoBEhqqyfFpYBkRnAkhpk9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=JN-f6yWvVRR6H2T4NSbRMsqKmxv_N4kJxEIadZiqAs_ruE3xSu7d_OHW8CkveduWX-WsfhuA_jK_5GGtGfXvGUATJyZ_ok4LccVKe9SnxSTDKNE4zDQsIO7BjcLN2Yd2--xJtJc3LAZGBwum4uu4waM-stbOZ0OF5UpqhQo-CdQ1FspcjRsUQIiIze6Nroo1x_rieqbtrMV1ObQ-ueqMpK7ZJh9Hc0lg8q9rZLw78zRaECEhthrxL8kC300W_t6HDYCWECm_Glr7KPue2Jwql6iYf_Y1uCXsX-z-XOQ9UquhmyGSlsXak92HadPiQuGfoOJjaG_VbAKu3Vqf_rwOVUB0dkt88Z3XVhuzzLChtnpK-pc5Wng760ayzAwZkxkScpWb3axfDKK9pZTgDTJpufNvg1ZQ0yQjwkAWp0U8PFUapAFOcriQdzlbGe862AVWPqxkMat2AG2UuWMju0eGEjZlxLsfO_exgOotXxc6g62rXp7DjuK5idsXGjcr0bLzXXg6Irw2cJNaw9dEUhgjt6SOY3o44W8eMk-cMdxjlqvISlXhE_l6Mf-lj-xHNxThcPpP0dAMAwP10O530pr0XXaajU10wUFknef0Yt3iTJXvEt8_lsPM2jguUKT_2d8aTMqW53UlIH2WCIJqIK7ZMj8D6BAHLi20A-EevsVI9ZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=JN-f6yWvVRR6H2T4NSbRMsqKmxv_N4kJxEIadZiqAs_ruE3xSu7d_OHW8CkveduWX-WsfhuA_jK_5GGtGfXvGUATJyZ_ok4LccVKe9SnxSTDKNE4zDQsIO7BjcLN2Yd2--xJtJc3LAZGBwum4uu4waM-stbOZ0OF5UpqhQo-CdQ1FspcjRsUQIiIze6Nroo1x_rieqbtrMV1ObQ-ueqMpK7ZJh9Hc0lg8q9rZLw78zRaECEhthrxL8kC300W_t6HDYCWECm_Glr7KPue2Jwql6iYf_Y1uCXsX-z-XOQ9UquhmyGSlsXak92HadPiQuGfoOJjaG_VbAKu3Vqf_rwOVUB0dkt88Z3XVhuzzLChtnpK-pc5Wng760ayzAwZkxkScpWb3axfDKK9pZTgDTJpufNvg1ZQ0yQjwkAWp0U8PFUapAFOcriQdzlbGe862AVWPqxkMat2AG2UuWMju0eGEjZlxLsfO_exgOotXxc6g62rXp7DjuK5idsXGjcr0bLzXXg6Irw2cJNaw9dEUhgjt6SOY3o44W8eMk-cMdxjlqvISlXhE_l6Mf-lj-xHNxThcPpP0dAMAwP10O530pr0XXaajU10wUFknef0Yt3iTJXvEt8_lsPM2jguUKT_2d8aTMqW53UlIH2WCIJqIK7ZMj8D6BAHLi20A-EevsVI9ZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKThVmZerfqjT2vJowB4kuHfOC2i67W2rncq8QEilxp1dau90TN8p-m9DBGKa8bXIuf0IUeNU6WE5IqOq7qBVouzoWd2PMUrtjrxtAHlD2HllMKYYA_IcufnYTJDrEnnRMpzJgF8Fq4RCLe1yB0XGdqNkcLGusEwUCgxjgXfdZ_G-05v3fbR-xmNip1MaDpN36T4MmV_v9aPP-4_G4mc1xte3I0v2iS1Xp_IkVVvBGl9-S1uA3jUbUO_jZwMMwX0RExvU36SdNnQYAo7YnirnN_bTPZvT05QZARtW-AoVdbRDtZtsjX7xXey3DRwwJdMXs8Y-kZ7INv8xnM_NC9xBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9S1VRjHRSiicfuLvLWptIT8kdzKQ832NAi-K68P5Cr49Vmp_Gfe-O1sE74ty9krLm3rB0ITxFFNMPlfp7rNEWrsKN95rhKv8KovQPRPh4rf1AEwdkcZ7Wxe1_EpTo67ggHEyU2nO9fFTAZzLotyBeQLTX3mjgCm3ZaiS9-HT5Bz6vLr-ACj34fBMTxvZPe6Kwg8tYD0SF9dtdN2uxZcwLGV8-yfpHmiRfC9JBScwYBbV5rF_nNJXtWqUZmtomxWDCwFxP8wnuLlkZ6Nl_g_sG-ACarxmZq9L1M0xCqWshSNVx8jg2j_aQ5rk3TS5vIUf-Txggb1MjnnyXTD5tJVCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=PdmM-2CihgcHFwqU9JAx56IhePNSB-E6KRdpaU5Eb0nlx2JZZautbL-oCpFJ96OzTboxjGPPA2PmlNm9_zAG3O_a6eKEPkzbB9Q6OSvIrXJQQh2ceJmv7-7symSWUWSZKo5v9pn2OJwKBNi5sEI1DlSdYvmlHHlJ68wXeAsEw1yNGx2dDfieT9iei7mwgRx8GqneHluvEl9aCX_BtHmehey8wrJwyefHoO59fKKDACnWaKVAYcGgpp0velyRQqOK0J5HzmplcCc0az6y_SdB9MJqSGjDtNTO0e13JNxbkjv5ElV2VDZRmAObS7VDQhZKtdbD9Ff4SF9OBSajzWd4_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=PdmM-2CihgcHFwqU9JAx56IhePNSB-E6KRdpaU5Eb0nlx2JZZautbL-oCpFJ96OzTboxjGPPA2PmlNm9_zAG3O_a6eKEPkzbB9Q6OSvIrXJQQh2ceJmv7-7symSWUWSZKo5v9pn2OJwKBNi5sEI1DlSdYvmlHHlJ68wXeAsEw1yNGx2dDfieT9iei7mwgRx8GqneHluvEl9aCX_BtHmehey8wrJwyefHoO59fKKDACnWaKVAYcGgpp0velyRQqOK0J5HzmplcCc0az6y_SdB9MJqSGjDtNTO0e13JNxbkjv5ElV2VDZRmAObS7VDQhZKtdbD9Ff4SF9OBSajzWd4_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=cuLG18a4fk7oHlj8AQQrJQaGVQaFbzPgF-eyiN1SoeK9QxPkO_Mdd5_hFUbtkZlHZRg_8atH8aKFRTQNj1H99My7CVN49V8Yhyd6vDgCewGQZgSWpNgyyLfRUTGyxY00k5eRayycbhBE2HHQZYEWRlY6elYfknUa9Vj958PTr3GmKaoNJcqR2f8cPq0HCMcSB4H9QhjkmI5poJSFbSPcemajRhkPCV2Q2c3iptL2mRnVbGGTLKqs43E6bW5tBAk95Kji5pnZCB0LE_Hd4dIx6kJ8xyKNiZjkrNMSdCIRuA72w-GnCzSMPBDdQDsD7P1GgjEQl5ZBAXzvdtCAoAVIaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=cuLG18a4fk7oHlj8AQQrJQaGVQaFbzPgF-eyiN1SoeK9QxPkO_Mdd5_hFUbtkZlHZRg_8atH8aKFRTQNj1H99My7CVN49V8Yhyd6vDgCewGQZgSWpNgyyLfRUTGyxY00k5eRayycbhBE2HHQZYEWRlY6elYfknUa9Vj958PTr3GmKaoNJcqR2f8cPq0HCMcSB4H9QhjkmI5poJSFbSPcemajRhkPCV2Q2c3iptL2mRnVbGGTLKqs43E6bW5tBAk95Kji5pnZCB0LE_Hd4dIx6kJ8xyKNiZjkrNMSdCIRuA72w-GnCzSMPBDdQDsD7P1GgjEQl5ZBAXzvdtCAoAVIaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=LtIfOVAX5CfV03FLRVNqxQJxLTC5KK685N3ZCrgHCDBXmEOupmden5fjFeGJ9SHs81_t05WHkjKYbYqK_PUyAj7zaa3Esbvm9EsK0eE-S08M7a_QQGerx5kPb-FVf2obBqPzq96lB0ECRjDhffpXMxh4II6LOizEIMn5QfaR9G6bRRP1cLVynsVOmbEW2YRJXVRpBrU4LEO7vL-mlMyGawcJGKENSJWav8npvuzdDaJPKdpSBJU3-dJ8nrMSxiuyHomN_ApIrgoqWbKjp1gYYEnnZA5gx2t-7CVH6b67v8i2oL2Z2EsYpl_wHmy3MCOxSqC6BcendRyFC20ktA2t4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=LtIfOVAX5CfV03FLRVNqxQJxLTC5KK685N3ZCrgHCDBXmEOupmden5fjFeGJ9SHs81_t05WHkjKYbYqK_PUyAj7zaa3Esbvm9EsK0eE-S08M7a_QQGerx5kPb-FVf2obBqPzq96lB0ECRjDhffpXMxh4II6LOizEIMn5QfaR9G6bRRP1cLVynsVOmbEW2YRJXVRpBrU4LEO7vL-mlMyGawcJGKENSJWav8npvuzdDaJPKdpSBJU3-dJ8nrMSxiuyHomN_ApIrgoqWbKjp1gYYEnnZA5gx2t-7CVH6b67v8i2oL2Z2EsYpl_wHmy3MCOxSqC6BcendRyFC20ktA2t4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jduB-LiO3v5FVYiXHpj8SeEznX9WZgYH0Pd2MRxK8NJIwRilz4xd_Oh2ldeb-LLwjTTLoFfTnYerfNz3QTOWj2zJE01ufgvNIAGFc_atVbzru-Lmin5uWI4rXCuxoOwl7W8908Qt_03aExOLDuubQqwhUZRwUUeqLwseXf0qtKM0XHFEyFGFUNU4hsNcn7fIyH8dFwHkL_MVrhbxSbz9FLwWU35TrT4i_fw7vmpTDiOxAZqe1q9qCFrrLHtXahXu6Eown_-yrS8xoptX1Hjhr-72gLUImTr5QM2Cx-3EYbbqSsWfxYaF3dHd9bmk4u9QJdt6v6thaNFtX7CW23Ifbw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOspTjPxA7gDXsvhT75sXKndA0Nn-XGyOb3ecOZaXerqlbP3zV5sw4Duv_VC6EK9ShQjQhpvUVkxcYnLE_kHJGNfFAm3tvN7Mdygc9ZBnRzkMCcf790HuZGOMSc2IlT2mwCsBxOUB8rexDPjBUMxNAtZRx5-hI9zOt-iItWZpT-pO6iLqy15d6iNAFt7VYxwTyAo7lfcdXG0uqVezt8ZMGnp0piARVEEJNynEfQ-GW06HMM8YIStsBRsw-am2sZUl2WeM7nre17wZ4SGq5lgK4iXtPiiONHidOZLDEcfSWvQERRLs6SFYdO8IfONhV-4x_Tw-Cz_xBqsn7ji-Fh8-fKT4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOspTjPxA7gDXsvhT75sXKndA0Nn-XGyOb3ecOZaXerqlbP3zV5sw4Duv_VC6EK9ShQjQhpvUVkxcYnLE_kHJGNfFAm3tvN7Mdygc9ZBnRzkMCcf790HuZGOMSc2IlT2mwCsBxOUB8rexDPjBUMxNAtZRx5-hI9zOt-iItWZpT-pO6iLqy15d6iNAFt7VYxwTyAo7lfcdXG0uqVezt8ZMGnp0piARVEEJNynEfQ-GW06HMM8YIStsBRsw-am2sZUl2WeM7nre17wZ4SGq5lgK4iXtPiiONHidOZLDEcfSWvQERRLs6SFYdO8IfONhV-4x_Tw-Cz_xBqsn7ji-Fh8-fKT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=tnQOeX501jUBSLNZ8I5DtJqCWPApljzobNyeLS1Q_TjeoILhs4heT9Dqh4f3ZQePkBpY1o4DdrSCnzAu70SHKVVUSwZB3lKBUpi37QttWm9ZxIhrn6AFV9jRngCYbJjBv4tgWLhW4c5R9SU6EOE5S1CkOw_kTLsakVdoDOrwPlthCMPxU8Xw8iPb8Bd8fQB4iLMFN-V-m_HzLlALJxWR_OjZBUT4hzBpevUsAKQCqBgM1bvgcL6F90bZWMP4GfTIgOWFXytV5kC5UqJhLdgQ4RTvltioaUyr4drHhCTkN8k2rByjqgfdssgiHfWFx-Gw6BNUsCAHCwmP8t8gXHuqsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=tnQOeX501jUBSLNZ8I5DtJqCWPApljzobNyeLS1Q_TjeoILhs4heT9Dqh4f3ZQePkBpY1o4DdrSCnzAu70SHKVVUSwZB3lKBUpi37QttWm9ZxIhrn6AFV9jRngCYbJjBv4tgWLhW4c5R9SU6EOE5S1CkOw_kTLsakVdoDOrwPlthCMPxU8Xw8iPb8Bd8fQB4iLMFN-V-m_HzLlALJxWR_OjZBUT4hzBpevUsAKQCqBgM1bvgcL6F90bZWMP4GfTIgOWFXytV5kC5UqJhLdgQ4RTvltioaUyr4drHhCTkN8k2rByjqgfdssgiHfWFx-Gw6BNUsCAHCwmP8t8gXHuqsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8KkOy1Lp2hH_Gsz084KGnMgUjls_S9yf9iO2YHMM4B4z8wSKIFaNMFr0kscqm-fX35y2wkssR6dpdqg15Q2pDBHbe-XgO4CoQGIElCLBu1EcQDG1tG6jLXdmsaXPgbn59ZlXiwLkwiKSXCdKM6gpRZxG0PpdMREvGNbwPMvilrkCClKgfWeLwHazpPfZNiOwLlRxQI5zmW6PRxuVE8wV4VBC0xLlc3XBiJK25AelACfv8j6uT7N_ZWN1ey5fev7fUsJztBxQQjN3pfSPDa1p_2FGnhz8mKw7_lGvPkxC2Zn3V-SE4wpOI_d8UsZIAtdc-15m8DQetUEfPegYX-FnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=Mr2D9ntTCVTE0M6UBvG3rY5IWW_C3GdMia0gUV_SXuMZJU_gpMC_krRFUQtmiK78zhmYCX2QxiOVasc75G1Q1_t8XRGvtew37_HlRZrGnZMMjIxVm0mUZZ4bC8VQYUDLQg483y8yNxJ-GryEksyxCHzFQU8AUUgilYDYHF1uIXBP48NzkzZYUGwbQ_Rz3zBkCWtSu9hVTCBj_i1TDduE30-QLRN3NBnX2yvqdTM2C1PXPh4XxGHXgKUJlgh80xzvyueHbs8_bUpPc-dpva-uMyZg6yTX_r6W43kF925qfhtLgCtAFAIT6mVZoHV_SRaQqWr3x4flil2zuul2ebfCc5fjfOSTvSiG3llK1OhEV63KEV-Ko6lz23Jt1pYqZJQJMi-P_nPjCboZ818mQI1Sv7EetZ5gwplKqn6E9wrYgRSHD2haEfXsxD2Omds9V1W2lSa8_WUs8L_Xlp-ctj7PPC3bbBULjnkOFkZLBax5c63uJa5bW2m3rStbp_ja3Xwy_7WZDFUEdMVypiPgo3Gv6lrMlLruzmYpjxr1_ogOO_mAvv6y_A4wJyuFrozyj2XJDVY-oappvADBz7qFqmgbHZ_Jme38bILyezN4OU4N4FyvjJfJUYQErzkdCzvqeejqiDaCKVgoV9SlHDpW3ZQT27JjAqlX4yogDcMy6UfX5po" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=Mr2D9ntTCVTE0M6UBvG3rY5IWW_C3GdMia0gUV_SXuMZJU_gpMC_krRFUQtmiK78zhmYCX2QxiOVasc75G1Q1_t8XRGvtew37_HlRZrGnZMMjIxVm0mUZZ4bC8VQYUDLQg483y8yNxJ-GryEksyxCHzFQU8AUUgilYDYHF1uIXBP48NzkzZYUGwbQ_Rz3zBkCWtSu9hVTCBj_i1TDduE30-QLRN3NBnX2yvqdTM2C1PXPh4XxGHXgKUJlgh80xzvyueHbs8_bUpPc-dpva-uMyZg6yTX_r6W43kF925qfhtLgCtAFAIT6mVZoHV_SRaQqWr3x4flil2zuul2ebfCc5fjfOSTvSiG3llK1OhEV63KEV-Ko6lz23Jt1pYqZJQJMi-P_nPjCboZ818mQI1Sv7EetZ5gwplKqn6E9wrYgRSHD2haEfXsxD2Omds9V1W2lSa8_WUs8L_Xlp-ctj7PPC3bbBULjnkOFkZLBax5c63uJa5bW2m3rStbp_ja3Xwy_7WZDFUEdMVypiPgo3Gv6lrMlLruzmYpjxr1_ogOO_mAvv6y_A4wJyuFrozyj2XJDVY-oappvADBz7qFqmgbHZ_Jme38bILyezN4OU4N4FyvjJfJUYQErzkdCzvqeejqiDaCKVgoV9SlHDpW3ZQT27JjAqlX4yogDcMy6UfX5po" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4hmTsdOTvZ6-KOQIF_GO2bZto-QLKxTbgIg6HRrMrw8R3iRL6wAmQW-1n9_Vi29-fOQka6PB9TSyqvj6y70UevtuPzgnLBuyG1rU9OadHJrzmZIMqAN7KbFAP3tssi4g9aLrsp7QGU_75ZV3lnrGvHhIOuNplxHEwruQ9Ce6GTSJfi3QbrP7wAoozfYGsrn3zV4Bu2IpdnDvAj7SzNjK5JHaewIJDTyyOv9smxYT-Y8UnsB4jGxTE_sLN2KdGoolfxflp8Ng3b7K8nh2QymE2bg_gqMoA_YcHa_XmtKaec3p2JW2mR9GXuVRG65KWCIGpn-9P3Ykz7VwL1av6D_7w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=CsLiNC_O2AyojOnbDtzxrUmVG7VTcC76oBeSZTEdj3MfUfjUsESJcKx9wBfg7Ia-I-bK6a6WDlO83JSlymx8fgkC1D6_WUUI2e44o_sRArAyqkKvl2fKkotRyZC_tNLRzYOHjX01KrGeFPlrNio31D0J5sS3s76atT-gU3pTIgN1vscXdAyplcX47-dT0C6ZPX8uvB1V-X4ofsHpQD1fcpA2UyTpr43gW0l-ov3g3AJXOTf4MiDL30a8UWh7XGm6nflCrBdWXHTG2C0UXx86oG6aPyr2qclz6XavLRks4WSMO5gfOH-qhylBv_b9EFpOFzVH59-j4bPior-lrav38g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=CsLiNC_O2AyojOnbDtzxrUmVG7VTcC76oBeSZTEdj3MfUfjUsESJcKx9wBfg7Ia-I-bK6a6WDlO83JSlymx8fgkC1D6_WUUI2e44o_sRArAyqkKvl2fKkotRyZC_tNLRzYOHjX01KrGeFPlrNio31D0J5sS3s76atT-gU3pTIgN1vscXdAyplcX47-dT0C6ZPX8uvB1V-X4ofsHpQD1fcpA2UyTpr43gW0l-ov3g3AJXOTf4MiDL30a8UWh7XGm6nflCrBdWXHTG2C0UXx86oG6aPyr2qclz6XavLRks4WSMO5gfOH-qhylBv_b9EFpOFzVH59-j4bPior-lrav38g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJvM6ysUCyv1GQbmoGw4dvttpV7LMeID1c0rgRuvgtt86U9zJ7__KZ8rgaQ9j6zgBX4DQsORPTK74gec5GLY1RncvasGD_CjdC4MVUMgMWhb_dqfmNqxwYii4WGdFDx2BRngK2q1Il3l7Jt_PzPsOgwLw4TRK_vXeGzzZGLX6Bd2gMlP0UcZbV9HRew8kLmktxMLAucI9U11M7Tov6rQ2DLZfzd6Rv0kF218aX9E1YFoubRVjgYBySf20eWvn2wyz4x4KRB6RKVdDeGH2KGxjW387UwzXf5p1bzC3XINhC1gCMuWIg6Q97mQ4dzh4J7lVMLDE4uuuVvRiRITF6lNbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGIHHTDtc8MrGFzcq8zAMxR7Upsp9DL9rNwfMSoJbqhsyGqPQCY8MtQFHFFkY711JAD5rBElt_WS9JkHgAZ8cwcj_nbr1mRYN7JxgItMHyQLQocsgzSZ8B62nhZcXW6wjixxaZ88dhJXMcBlcGgSXKN7l_fdyVHGle48GNTWmd1zo5skK84ZdDVJCnPw7Z3rVob_u-uG8kX8eAJsP96XcrOCCswQwYzjlrqBrcVqnW12sm0QMCC3Lq2Is_scqvp08eh-MqT_51nBC2oXq1va4o2XqvrZ6KZ80l2XpUBO7xsnnngpNnlyzIlG6AkCZYMtlnJNXZ7DJ3eyvlO9Z2lXXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwCEyfm-TgR8efIEXLW__-6CKW-jJ0iDHaPT4UZJXUmUPonQpKkDq3WhaydLs71KHOUzbMMqTKv43CcF2OBZW01m0joF2Ga4OBstm2JyYfMomfUk6IIPujRwjGX8EKQVlcG9OuUtt3D2dikx7QU4enpDbpvZEHJ8zVq-vbWtdWgWOnIA9hJShORpM1gq9hOzLFX1NFdU07efaaaJDw97dfz2opNp6_2P22lP3HBBvDRpwUoPbhZdk8gu3pIS6OQg7DQfYClEvfuKiCwbj1N4UQfcZlHDYx9c4WUw7w5GDkY0soo5-0qhrwpWKSMBW-0QFwR8yScAXhq93k1VAgG2KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ZY9vWe6Av8ddmMbHz_F-90sISzom5GlWT1WR7Jr9p7DMcFlC42q5d5m4o8nOTbeAiR5C7a63TUFz5RZYIXHLaEJZQcahRzT1X6iA5GNAklWxc-5PWRsPPeu3Fx-TlvaPMfzKeCU522AqynHj4LdUJ3fHWgSvO0EpjtKzFgfc6lUlk334jIWQe7YTL76moXqfBPC_XfYIj8YjY8JsNolOywMXOb3d21R4CJGHUtIaQYE4xr7V_nWUEdIoAnXKg_1EdVxnZvldfqlwUmtfJ7cWVOBPFVz_pQLWbkkq1kI2fpcwGtFjcTL0ZPgG_Yeloapw9U0umczcPf96ROUn97qPaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ZY9vWe6Av8ddmMbHz_F-90sISzom5GlWT1WR7Jr9p7DMcFlC42q5d5m4o8nOTbeAiR5C7a63TUFz5RZYIXHLaEJZQcahRzT1X6iA5GNAklWxc-5PWRsPPeu3Fx-TlvaPMfzKeCU522AqynHj4LdUJ3fHWgSvO0EpjtKzFgfc6lUlk334jIWQe7YTL76moXqfBPC_XfYIj8YjY8JsNolOywMXOb3d21R4CJGHUtIaQYE4xr7V_nWUEdIoAnXKg_1EdVxnZvldfqlwUmtfJ7cWVOBPFVz_pQLWbkkq1kI2fpcwGtFjcTL0ZPgG_Yeloapw9U0umczcPf96ROUn97qPaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwarF4pQfn0QPpsTrMY-M8Hbn4LI4bDujeOosMJJF7ag9Ydf64d-YINfs0TjdajPzNe1PPPV6bXSmfReyeGmu0ysYTG5gsQ2bT3L_bT_OuN20kKJ_HH8cb0p_CFliIcs4dgeLEIv-GhSFm9lV6H5i7gC32bwAduVZ5VyYl33SFEpPSZ9h1UQLSVXHlZplVaWZb3mUBs9b3YxLf0_6PQJdgo9mpC9lLVgDUI0c6MYFfNEydP4icvqS5fZTzOTWeQtGuBXRMJvujv0aeZtKEFZ0wX5cipwPeqtSvRd_A-OJkZGncDD1kVAxGhqR9v0IS8WTj85D-43nNzEHUiiSOV1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuxCmvYcGeN6bxei9hmiLI4vd3kD9vaaUJkWncftpFMe4Gi6xkqtfPxz20GcEDfdi6dGZx3rQMug71LX7IrC3cDI-JrIj-dszhw213aw5ykNAWoWudDVGXzasmK1U-vB54L-jXkD1LxkRHcC1-_zPngljmoNm8B36UOElRWMtLouZPCwEVCH18WsrywYNY3G_9D9d9ClfuCcM_OX0hbEZRT8IX71pooFH37q0r304Fmd7TvaLmhAyeUNCMGrFZpmuwJsBh7b0_e5qaCiLk_PocMjym1FMEzfwKbVBKm-D__XT8riFPELP9B13zomOVopavKZX_Y7vfP41RK_mGbvWHeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuxCmvYcGeN6bxei9hmiLI4vd3kD9vaaUJkWncftpFMe4Gi6xkqtfPxz20GcEDfdi6dGZx3rQMug71LX7IrC3cDI-JrIj-dszhw213aw5ykNAWoWudDVGXzasmK1U-vB54L-jXkD1LxkRHcC1-_zPngljmoNm8B36UOElRWMtLouZPCwEVCH18WsrywYNY3G_9D9d9ClfuCcM_OX0hbEZRT8IX71pooFH37q0r304Fmd7TvaLmhAyeUNCMGrFZpmuwJsBh7b0_e5qaCiLk_PocMjym1FMEzfwKbVBKm-D__XT8riFPELP9B13zomOVopavKZX_Y7vfP41RK_mGbvWHeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=R9l6euvR9nD_0hy8Xrrb9J4A_lbS3St3ld-dfich13UWBPp-Lr3tbCCB21uLGFMQvdMuAcI3ZdohCzUzZxsF2EqYutyMyAs6ptRlQa4WEiFUNTWYUIHfvx8GmSs0gbXNvjwA-i1waZE6O2yGJGGPf6eBDtkE3b6RZqs-6_WuwpJpaBF28OKbs5S_aMB72antUno9CWlvnUtvylThYWkv_Lg4rAnjavzp1x1C_L6SbX-IJ-v5BSzMftGE2w7s4ZulzB4MQgXu-5Ev0L2KFtZldQAFueJGvDcA2CocmJqC1zlX4zzjF7M7N4cp90I1WEChR8aECrGGQkpJEVgHtyB06g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=R9l6euvR9nD_0hy8Xrrb9J4A_lbS3St3ld-dfich13UWBPp-Lr3tbCCB21uLGFMQvdMuAcI3ZdohCzUzZxsF2EqYutyMyAs6ptRlQa4WEiFUNTWYUIHfvx8GmSs0gbXNvjwA-i1waZE6O2yGJGGPf6eBDtkE3b6RZqs-6_WuwpJpaBF28OKbs5S_aMB72antUno9CWlvnUtvylThYWkv_Lg4rAnjavzp1x1C_L6SbX-IJ-v5BSzMftGE2w7s4ZulzB4MQgXu-5Ev0L2KFtZldQAFueJGvDcA2CocmJqC1zlX4zzjF7M7N4cp90I1WEChR8aECrGGQkpJEVgHtyB06g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=PCNB73E8mjs8q014jrRdvDh9sM1ghxI3YqKtRgi6NM-nBj-NOrPg_vQHjKDVM1OlH0QEg_ACauFWlEeo7NOkruKq9M6-DUQRV9puU_w96-MSxY5biSkdAJWuRrwl5B1BF9w-FNULLff7RHMYBpRg40vQESk8SpyCAQxNwT4om1tSCtsM_4ou4ia4hOix1l55-wetckb-7hoJQCjohzz4-Qbz4tPkQ3gLXvKY_nrBcCgpbsoGrkWGKM1pr5XrlKD-fOqqhvdFsupH4VVR-SAgmEwZXZkWxysznqqs3pFhMHqK8B86UJ7w7RQsWvxGfcO2eJ0MxduygrqeRVqMRv_sU3OZJgD-cIa6CZ2NV0ricMMD77QNVQOYKe9qg8l41hll8HvHiS1QEDKkZa9l9U1nha7YkAbBWU_2DDkTfym-T4K9vF1FM9T4Z9X3VAkwoXm5eywJzzhNOJr5A0IGyLbAtVcvuF_q06MAJ-Z4O6hO7LQYzQdSt_UgWyWym0SnouyLhSGdx2RpaQzD7d5szTpXpgiAUZ3cpeyrfhtBtxnJyHkpa9V0zqG4JI1igPEcjxHdzNhKU14JTbegSwTjStHlqrJwYlUIfIe9HI-Z3FUHKJSvKfBSNaC3--Aj6KL4eHFAw0CoI6h_hR5KWiKIAt9X73_OySsXChqs_AN3v5aZDgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=PCNB73E8mjs8q014jrRdvDh9sM1ghxI3YqKtRgi6NM-nBj-NOrPg_vQHjKDVM1OlH0QEg_ACauFWlEeo7NOkruKq9M6-DUQRV9puU_w96-MSxY5biSkdAJWuRrwl5B1BF9w-FNULLff7RHMYBpRg40vQESk8SpyCAQxNwT4om1tSCtsM_4ou4ia4hOix1l55-wetckb-7hoJQCjohzz4-Qbz4tPkQ3gLXvKY_nrBcCgpbsoGrkWGKM1pr5XrlKD-fOqqhvdFsupH4VVR-SAgmEwZXZkWxysznqqs3pFhMHqK8B86UJ7w7RQsWvxGfcO2eJ0MxduygrqeRVqMRv_sU3OZJgD-cIa6CZ2NV0ricMMD77QNVQOYKe9qg8l41hll8HvHiS1QEDKkZa9l9U1nha7YkAbBWU_2DDkTfym-T4K9vF1FM9T4Z9X3VAkwoXm5eywJzzhNOJr5A0IGyLbAtVcvuF_q06MAJ-Z4O6hO7LQYzQdSt_UgWyWym0SnouyLhSGdx2RpaQzD7d5szTpXpgiAUZ3cpeyrfhtBtxnJyHkpa9V0zqG4JI1igPEcjxHdzNhKU14JTbegSwTjStHlqrJwYlUIfIe9HI-Z3FUHKJSvKfBSNaC3--Aj6KL4eHFAw0CoI6h_hR5KWiKIAt9X73_OySsXChqs_AN3v5aZDgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=cQ8xDwirOljWK9xFC6-Ef20gXYORDU7irhKGrkiQCYS43k5X6niOpFDV3Mar6yZhwgmQrIdKslc_tak9nS9kupOWPYNC22anGKRi9YgYbqpHeeXLJW8XDaAkH6vHqZdjGqdFDaUV006GPKEKBxqvqPfa3b5tei_TUmxo21Ujg3h013_MvDbB481oVzbjM1izKv76thENmZCnYQeMbACtvFrsqyXedhjh5FREfpOnnUAsUUplhPlM50IzwXvao0WdSceXvIvZEXM0vhPB0AlmQfyErb8o6ovKs4v6UxMhlenziOgOmK2Ht9dSHCdWh_vlqwctY1CCiN04KwtKTtqUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=cQ8xDwirOljWK9xFC6-Ef20gXYORDU7irhKGrkiQCYS43k5X6niOpFDV3Mar6yZhwgmQrIdKslc_tak9nS9kupOWPYNC22anGKRi9YgYbqpHeeXLJW8XDaAkH6vHqZdjGqdFDaUV006GPKEKBxqvqPfa3b5tei_TUmxo21Ujg3h013_MvDbB481oVzbjM1izKv76thENmZCnYQeMbACtvFrsqyXedhjh5FREfpOnnUAsUUplhPlM50IzwXvao0WdSceXvIvZEXM0vhPB0AlmQfyErb8o6ovKs4v6UxMhlenziOgOmK2Ht9dSHCdWh_vlqwctY1CCiN04KwtKTtqUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBOK8Hdj63QmjEOcL3_dKOJbzAAYqkuv3CuIBwRzXW-q25xCw5ybQzMYFTwR-z8a7S91ZZC7duPZGZV4Op9K4JSsLsbcQa7HDvAaJlqc03XsMCwoyDVyjHwOFOer42I7p-XnzJS81pgNZTxQOmIWt0SynMMNoMBMqfhx8ra1dQUtgw27XAwDd29P4jwkjg8ibdPYoQrUbKA2CVoZpNKiCQnXWqTUznqC7LUXYdctuMLptlGjgR-SXX_gtRNMqEwwH5YUV5k1k0Ubsh-4RbpN-GtRjjOOkYU5h9LwW89Nx5Mwy_sMw1CIqCEd_ErFdI8BhkVRDSwZ2uoFRDKAYFQxZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=k3frD5et9fIIlbDEkxcdoW9YRmXAHWBGbZNuqu6Tj-ObsIess0EVeWY88pN_DZ5DQ7ub15JGgSwMlooLmxscpRS-AnXPJ1bCOPAO_xxaOQhdQfsDtdGxSAgrs-3mQGnzx9POjVubjSSkCoqYBRIvg5l9jy8cfHg0dwQhEiZE36MVSILFmPlBujh8yJQlqGMz5lr_hGMeBePvKrGAUzUd9cerGpmMsSQmZT-XuetTCzHEw--O4UlVWU2QOsaYVR8DAcRaHhbzmL4DrA10alR0LeMGKRQ0J8_Kb7hGebqUhp1I-ZbUhDyjgYi48j3wSdHf9D670jlhpYwDWBXMLkATaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=k3frD5et9fIIlbDEkxcdoW9YRmXAHWBGbZNuqu6Tj-ObsIess0EVeWY88pN_DZ5DQ7ub15JGgSwMlooLmxscpRS-AnXPJ1bCOPAO_xxaOQhdQfsDtdGxSAgrs-3mQGnzx9POjVubjSSkCoqYBRIvg5l9jy8cfHg0dwQhEiZE36MVSILFmPlBujh8yJQlqGMz5lr_hGMeBePvKrGAUzUd9cerGpmMsSQmZT-XuetTCzHEw--O4UlVWU2QOsaYVR8DAcRaHhbzmL4DrA10alR0LeMGKRQ0J8_Kb7hGebqUhp1I-ZbUhDyjgYi48j3wSdHf9D670jlhpYwDWBXMLkATaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=Iie7rlgQcg_KyVx9MMiXUhO8TsBkxKgoqxA-r3fwfJvGQMW5qVJ5jxlRbESQXbQJV65POUaL2FPyH8trNlJHeO1ALLD4MAdWJM5YyKaDurieip0glBirWIGSQ8CM5_e3Ld_Ng4ccRPMOxKrumETyV-KkFfIgrJ1I9PWAnX_1_fBiOO8EFHH23qRnvhoE1J5vCKQWfF8C9blt4j8ZMeKS8THJb4oUP6H3SIV5tinwSbU13YCBzCbsPGlYNlk0L0rKxNYndLFTsxC5JNs-kiJS2F0gxDeUh2HEe6_ZxSHHrwDMokMYKxq-z_PMdgEWat0-pdqfiWFrxnyABRmKxNfM-TYEkcz6XcGc836gGiKJosCEb35P35qmHoLyhlS2L17ilaVkAgibnJ5zGU9wBGDC_ndHfvwLI8yP7_F0vzlrpD3I7zXxSBLqSxoohkAxWm0c0thZSLPKja-HntOMi6CVcWkHgCAOBgnlsMSlkAR2Q-0w5DSphAPnLenDTS9v6bVJWnxB6yxMuD-Y50oIkA7AStgK2VOwzOxOi37E3GAkll3CzxH1fXA3cmzfGlCaUBz4MW7NQ5XF97dmSnDtq_Ob-WYD-n-z5IuJfq47GpXCOODd-cu_nfkCPqHCZiq-0Yrrs_z11FJqaIode-2uzRBMRX6Z58HOQyNEpLVVx5f9evA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=Iie7rlgQcg_KyVx9MMiXUhO8TsBkxKgoqxA-r3fwfJvGQMW5qVJ5jxlRbESQXbQJV65POUaL2FPyH8trNlJHeO1ALLD4MAdWJM5YyKaDurieip0glBirWIGSQ8CM5_e3Ld_Ng4ccRPMOxKrumETyV-KkFfIgrJ1I9PWAnX_1_fBiOO8EFHH23qRnvhoE1J5vCKQWfF8C9blt4j8ZMeKS8THJb4oUP6H3SIV5tinwSbU13YCBzCbsPGlYNlk0L0rKxNYndLFTsxC5JNs-kiJS2F0gxDeUh2HEe6_ZxSHHrwDMokMYKxq-z_PMdgEWat0-pdqfiWFrxnyABRmKxNfM-TYEkcz6XcGc836gGiKJosCEb35P35qmHoLyhlS2L17ilaVkAgibnJ5zGU9wBGDC_ndHfvwLI8yP7_F0vzlrpD3I7zXxSBLqSxoohkAxWm0c0thZSLPKja-HntOMi6CVcWkHgCAOBgnlsMSlkAR2Q-0w5DSphAPnLenDTS9v6bVJWnxB6yxMuD-Y50oIkA7AStgK2VOwzOxOi37E3GAkll3CzxH1fXA3cmzfGlCaUBz4MW7NQ5XF97dmSnDtq_Ob-WYD-n-z5IuJfq47GpXCOODd-cu_nfkCPqHCZiq-0Yrrs_z11FJqaIode-2uzRBMRX6Z58HOQyNEpLVVx5f9evA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmXJiU_66znCYKSxH4GZAuSGnmQ9xkjNuPq_U8i7klorodwm4AoLTorSF6LRdq5Ro1DEFZk0X3TU-dhwgjeLCV6NzflkL49NR3GGgxKN9-ru6LZT6F55paAmFBEs8B1VGbyT3iGfcDCn6vdUIJm7Ubfl0u0wktceJhFnAAkU6FUCesg55yddKwR-6w10oJLxFQBxgFQDWlb7_Frkg-vcLEa8_OX1dCVmFVbZn4Qo2Tn8W2HzytVoJfApYJygL3C8yDAvrj7EAsJ8Bji8syP3eKQa-K-ZYC7o3a95gq_Rj9idfRdHPfEzNFUX8MjM5-do_La4N-fVEt7jXx1ek8NBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=hIavXA1wj1nvzIfU3gHHta1FV3qXZzV-9sHVMhfcu5MuQrfDOpXDhXDGOknvpcgkh1WUSzWRVHlrpQ6zxqud5E3CrlzZjNvAgrAmYH9lSiWlj70tkMf7SU0IYVJnOVkjj9PeRbpzycT9lNMwafFtNQsiqANaSSrPTEcN7D7m8Hy4d2PRxZlgfdaU1j3Q0HT7vH_lZpyu5LHRcacERf9-epSdXU-6bsFHaZS6IzQIgtWzlvS747qVGYzYNenMde2RY623klSuX3I12eh3B3l6EuIw8eOCkufiQ6EYr2PGF4gR1gkmkRK3hhTvGw-b71J1muSasUi8ZryVdQwW2NIxlzfjQS0qF_PYR8Dp68kg7QZgxfuyD8IerjjEIUcjx0Z66Lp_KYQBh9IwZ0jQYKp5oWDg-dTaC5gQAVuYCagJDvseC--EEda_KjhIRyyhzQ4WCrI8eivTDDbp2mwO1WR_HGTN5VI7-8wVRPmgYZg7J5-L0BMYEKYH8zCxsmMDo1JkGZri5xjuYs5PguffiCdSBO07oD0J1DV4W2Mhoz-BdN2l42wsvIw9dE8W_h_-z-7K_NLIBvqoh-rOwJYMeAJGG5aGP0IJOkra6s4tQSS_QfYgunhjlnfyFyuNwGdpqNgUkSVrc7Fx2eF4SCrjZxuzxWu_3WrRQ9rvaqVrdF5QAJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=hIavXA1wj1nvzIfU3gHHta1FV3qXZzV-9sHVMhfcu5MuQrfDOpXDhXDGOknvpcgkh1WUSzWRVHlrpQ6zxqud5E3CrlzZjNvAgrAmYH9lSiWlj70tkMf7SU0IYVJnOVkjj9PeRbpzycT9lNMwafFtNQsiqANaSSrPTEcN7D7m8Hy4d2PRxZlgfdaU1j3Q0HT7vH_lZpyu5LHRcacERf9-epSdXU-6bsFHaZS6IzQIgtWzlvS747qVGYzYNenMde2RY623klSuX3I12eh3B3l6EuIw8eOCkufiQ6EYr2PGF4gR1gkmkRK3hhTvGw-b71J1muSasUi8ZryVdQwW2NIxlzfjQS0qF_PYR8Dp68kg7QZgxfuyD8IerjjEIUcjx0Z66Lp_KYQBh9IwZ0jQYKp5oWDg-dTaC5gQAVuYCagJDvseC--EEda_KjhIRyyhzQ4WCrI8eivTDDbp2mwO1WR_HGTN5VI7-8wVRPmgYZg7J5-L0BMYEKYH8zCxsmMDo1JkGZri5xjuYs5PguffiCdSBO07oD0J1DV4W2Mhoz-BdN2l42wsvIw9dE8W_h_-z-7K_NLIBvqoh-rOwJYMeAJGG5aGP0IJOkra6s4tQSS_QfYgunhjlnfyFyuNwGdpqNgUkSVrc7Fx2eF4SCrjZxuzxWu_3WrRQ9rvaqVrdF5QAJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=ZDZhrPwq_L8gDfDPnDLGGSfr5S1XPTdvdD619eQ1J2-fH8VwpFmHu-8i8bs9RdhGqnZzOr2eBsGTGDGVv4fcbG5UxIT0P-evD3xDY9Ne2BWRii5ZF562oRcvhsHI7WFomCmA4t21VWkAYry_bs9lsP1fm6CurJ88kbCqPK3Sj0C8WIzhnoU0OcZoRSmeSOnod1rz3XUKdAmDaEBVTrM6I2kMps7O1tmdhRD2NN-v4C_fFmulXDLnkRPnjhjVizJlsdrcf8TfaDYpDQECrmXryLccsaBDag6Xi8JUKk95VCaptqOipBlgsUOiWV4TgOAI4Ap1VqHgWeStjECOleS82xjmjrkUtcPUVFuGJNiLLZOCJUOAryteaCR6swu_jiuSh00Szh8xtCLsGu18C0qyRyay25NfNScPnMereKWVYF0ob5wDmz_BFq_TM9bj-QmmBVDej2zabnd29o34Psat0Z5Q1h93OndJtAwt4gQwx5lmTEs3vbCr1hMQfM00vAAVdWgSO_mUDmEGnkkkBlgjeZb1I3IwFRM7oUU5cGRnct1FgSwT9BCjpO3aRvyp_y80yqcSWhsp7g3XVUhjp1tgzvoJM-x3-7XYUlUS8gwANij9AmDNAu2-XVQjrQLNHCkva1mCMk7u0ppgNJOD85v5-LqAJ1qsfTKwtUyEWzffn7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=ZDZhrPwq_L8gDfDPnDLGGSfr5S1XPTdvdD619eQ1J2-fH8VwpFmHu-8i8bs9RdhGqnZzOr2eBsGTGDGVv4fcbG5UxIT0P-evD3xDY9Ne2BWRii5ZF562oRcvhsHI7WFomCmA4t21VWkAYry_bs9lsP1fm6CurJ88kbCqPK3Sj0C8WIzhnoU0OcZoRSmeSOnod1rz3XUKdAmDaEBVTrM6I2kMps7O1tmdhRD2NN-v4C_fFmulXDLnkRPnjhjVizJlsdrcf8TfaDYpDQECrmXryLccsaBDag6Xi8JUKk95VCaptqOipBlgsUOiWV4TgOAI4Ap1VqHgWeStjECOleS82xjmjrkUtcPUVFuGJNiLLZOCJUOAryteaCR6swu_jiuSh00Szh8xtCLsGu18C0qyRyay25NfNScPnMereKWVYF0ob5wDmz_BFq_TM9bj-QmmBVDej2zabnd29o34Psat0Z5Q1h93OndJtAwt4gQwx5lmTEs3vbCr1hMQfM00vAAVdWgSO_mUDmEGnkkkBlgjeZb1I3IwFRM7oUU5cGRnct1FgSwT9BCjpO3aRvyp_y80yqcSWhsp7g3XVUhjp1tgzvoJM-x3-7XYUlUS8gwANij9AmDNAu2-XVQjrQLNHCkva1mCMk7u0ppgNJOD85v5-LqAJ1qsfTKwtUyEWzffn7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ke4pba0Tu4S_dTYXbWb9wskpda9eSnOx1qfvIZ28Hl8fSDbMFEkTTK589qd46SGs194e8VOhelgdl6FV-uHu4FUdM9OxgMHr6qBw9Mk9FYDvIGf1uCOvdC0omx1FBdWbOJFzvKutjUCWZIFQL6C-u73ikKPkourrLZ0Zmglf_zi7jQwjjOdRjPzFGd0SicUK4fBxRWhvETrypfgBbc7KxTT3o8L04jn85coJ7LDivztAXxkoKgg_ZToVVTj4B3hHonCXCoZcF2SMvtC-WVutyp_JY97ih4q7VCAaORVVziyVX6cWIrMkhcMCkY_Sj_SO6EU5ioapflcgHIAI_SpjDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ke4pba0Tu4S_dTYXbWb9wskpda9eSnOx1qfvIZ28Hl8fSDbMFEkTTK589qd46SGs194e8VOhelgdl6FV-uHu4FUdM9OxgMHr6qBw9Mk9FYDvIGf1uCOvdC0omx1FBdWbOJFzvKutjUCWZIFQL6C-u73ikKPkourrLZ0Zmglf_zi7jQwjjOdRjPzFGd0SicUK4fBxRWhvETrypfgBbc7KxTT3o8L04jn85coJ7LDivztAXxkoKgg_ZToVVTj4B3hHonCXCoZcF2SMvtC-WVutyp_JY97ih4q7VCAaORVVziyVX6cWIrMkhcMCkY_Sj_SO6EU5ioapflcgHIAI_SpjDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=cVhEVCxNmdXpuRC34YcauBd8agWBsN28Z28ZXvDqVt4JjtR9G9aEE20Q-wqJTFBNv2DIuYG9qOPk7DO7JNFIkFzab_eiziYF7rG1gURTLD47ospWPKsKbYqt9CqEhGNsmS4ilFNJudX71AYG5kWyyDx23DZIOBaP0dI9Nky_vcIRKN3At-Zg7d3E4SS53ij6X0D4_9S0Fk1Vjv2XMyO5nMI8HgeFTHJ_0766epthnIlHyyn19IIHxK9BgXeHhRf_VnYI6t1TmncQ5Q00bCSk_0uLyff-33nk5e00gs4klcsw4maTSeiVdzSspUvRDlz3thBtzp4hqPmzBvyRGEYPnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=cVhEVCxNmdXpuRC34YcauBd8agWBsN28Z28ZXvDqVt4JjtR9G9aEE20Q-wqJTFBNv2DIuYG9qOPk7DO7JNFIkFzab_eiziYF7rG1gURTLD47ospWPKsKbYqt9CqEhGNsmS4ilFNJudX71AYG5kWyyDx23DZIOBaP0dI9Nky_vcIRKN3At-Zg7d3E4SS53ij6X0D4_9S0Fk1Vjv2XMyO5nMI8HgeFTHJ_0766epthnIlHyyn19IIHxK9BgXeHhRf_VnYI6t1TmncQ5Q00bCSk_0uLyff-33nk5e00gs4klcsw4maTSeiVdzSspUvRDlz3thBtzp4hqPmzBvyRGEYPnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=GDS_boc4BRQ299NzcAJbwM01bovrLs1rOMA5XwJcOsznYcMZbeCWegqwBb0nNdU_TpyooQuXyJ3jL4Fj-Ae75BbiPRNzueO-toWsqZCvpVFR31ATm8ccQB9ywca4IUvofcJKeR33FNUnjUizr26rZx5XfShOMcRRQ2jizPkP26VwKo6t4rYt4GQTdYJ0_dIQbZKPVO_REV4K-dCmFLHbje4VcX16VMhdkQbLsnzdJLaYDB4jOJTZdKfJUAuPnCO-mZ9ILWU_2KhI-inefdsSb7h7hgAWo_pWUmMkC2Udbo1DATareTzAnEtL5RWhhgHoDqi22UQe5QgcRE5VjdTKxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=GDS_boc4BRQ299NzcAJbwM01bovrLs1rOMA5XwJcOsznYcMZbeCWegqwBb0nNdU_TpyooQuXyJ3jL4Fj-Ae75BbiPRNzueO-toWsqZCvpVFR31ATm8ccQB9ywca4IUvofcJKeR33FNUnjUizr26rZx5XfShOMcRRQ2jizPkP26VwKo6t4rYt4GQTdYJ0_dIQbZKPVO_REV4K-dCmFLHbje4VcX16VMhdkQbLsnzdJLaYDB4jOJTZdKfJUAuPnCO-mZ9ILWU_2KhI-inefdsSb7h7hgAWo_pWUmMkC2Udbo1DATareTzAnEtL5RWhhgHoDqi22UQe5QgcRE5VjdTKxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=DS5H4VrEdfxj7bMYLAygcSbLAwEkZMZ4hq38bC6NBTpgZldHbRxz7qK74qiEpAZSmn-DkaKr7cZM45HWqRcEDvOvlmbf-IILBZZ8hq9szwAKaeQA_hqMX_7jSx6l8nHA9etjnoLmSSH1WWmp0mAaEzYKLOqVyG_kYKf3_wcgdTDI2z-yokcSvn7dyXYFGZK9dR9SjUH-5ZCXPlEfuS0cOy0Diz9afJ9wW6BDsVFwaLvNKzHSZc5JIsZ9jJjc0vYht_Q9XBDyd2ScwoaYNlJY_L_NP9cSFm2RPDgj6-7iTYcZsBP8io51Y6S3i_9gg0hkJPKMqN_zGdMPqDlLeBQ_uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=DS5H4VrEdfxj7bMYLAygcSbLAwEkZMZ4hq38bC6NBTpgZldHbRxz7qK74qiEpAZSmn-DkaKr7cZM45HWqRcEDvOvlmbf-IILBZZ8hq9szwAKaeQA_hqMX_7jSx6l8nHA9etjnoLmSSH1WWmp0mAaEzYKLOqVyG_kYKf3_wcgdTDI2z-yokcSvn7dyXYFGZK9dR9SjUH-5ZCXPlEfuS0cOy0Diz9afJ9wW6BDsVFwaLvNKzHSZc5JIsZ9jJjc0vYht_Q9XBDyd2ScwoaYNlJY_L_NP9cSFm2RPDgj6-7iTYcZsBP8io51Y6S3i_9gg0hkJPKMqN_zGdMPqDlLeBQ_uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=YEZd1Pktsdg89SotMgd5FTAJrsLUoUDVLbFHHHq1-N5jcq4tzi190OrVRkpL8sD_C7J1UjqLUcmizjbsqqq8e_AeZ6K0pHtq13SFPlhHjbmmXtWIMsr6yXqkZESjMOwcEiu76MODEIak1uAUDlThu6BID5qAjB3l9EHyoyhb96aQ0tbyEY2ULQj-wnq8lkennlRSwRxt6Uq6Qt5uxS5ohvI1cfGoAH7ojbwo2vjxP3owqFn6WJDwZuaVMDUUa87s1bpmehQcFrwwQ_8ToO90ESUDdos1kQztFqQzh9MLZTidNjhtpQewBZLth__Q-eJxM-9UCGXzuHyyZc03uZr4UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=YEZd1Pktsdg89SotMgd5FTAJrsLUoUDVLbFHHHq1-N5jcq4tzi190OrVRkpL8sD_C7J1UjqLUcmizjbsqqq8e_AeZ6K0pHtq13SFPlhHjbmmXtWIMsr6yXqkZESjMOwcEiu76MODEIak1uAUDlThu6BID5qAjB3l9EHyoyhb96aQ0tbyEY2ULQj-wnq8lkennlRSwRxt6Uq6Qt5uxS5ohvI1cfGoAH7ojbwo2vjxP3owqFn6WJDwZuaVMDUUa87s1bpmehQcFrwwQ_8ToO90ESUDdos1kQztFqQzh9MLZTidNjhtpQewBZLth__Q-eJxM-9UCGXzuHyyZc03uZr4UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=N8nwlauHKVcqkYpPX1gRV-s_avXh5iimoFYnyLEa87LT1nZ82OouECS-htxOylO2d8u9tQX6vV_IjCCjYbZMHygvcrYb4GO7WUHU8qe_Js_KdiqLR8ahvNToW7SRblT1iWou7G9IKHBqElRhTY21UYiv_ELeHqTy6K28q9UAtPzJdPnUDWVeV0yi3JHr62KO-qDN9SvQDSmlIXvUhlrzV0Jb9q08FxQWocfUMhoIbG5kUkLCsZrd7tCGsW_Y83mmSKOVvy7NAjkhlRmUwUwSLZgKYKLTB5i5fgyQaDrninJ_kPbARYQlszy1481trcO0Gc5k6GKPvoQyyYBzOA26xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=N8nwlauHKVcqkYpPX1gRV-s_avXh5iimoFYnyLEa87LT1nZ82OouECS-htxOylO2d8u9tQX6vV_IjCCjYbZMHygvcrYb4GO7WUHU8qe_Js_KdiqLR8ahvNToW7SRblT1iWou7G9IKHBqElRhTY21UYiv_ELeHqTy6K28q9UAtPzJdPnUDWVeV0yi3JHr62KO-qDN9SvQDSmlIXvUhlrzV0Jb9q08FxQWocfUMhoIbG5kUkLCsZrd7tCGsW_Y83mmSKOVvy7NAjkhlRmUwUwSLZgKYKLTB5i5fgyQaDrninJ_kPbARYQlszy1481trcO0Gc5k6GKPvoQyyYBzOA26xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=FtbgCfq_Vye2Qhx0Pb48lfCrdTpSI0Mv3GDDWi-qDKOFbQicuGuonk2FjXJDsLu10hJmZGoGnLVkbsRb_67NpD2Yvx5KjJzjD8kxwSPHOMIPxFUu9Dm9hJ5Gk2pJdn35gcprm3IOmvoGUqd_KQ6uZV6jH4olm9f9ux1w_wBXSU_xh-py4OwCnmZ0f0vhRIugxahqwEXufau9NEEHioBg2jJtmQp7qdODkjb-oCi3EHHwIhz4Gj1VBYeI3ZhtfaYJDthSKurPeOXeH-WYsv5rMN0dBUO_nLE5k3RjJg3zSjRkWt-lVKozAaaQVgrdqnpgvJDjTDb9G4xb4f2OVePzvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=FtbgCfq_Vye2Qhx0Pb48lfCrdTpSI0Mv3GDDWi-qDKOFbQicuGuonk2FjXJDsLu10hJmZGoGnLVkbsRb_67NpD2Yvx5KjJzjD8kxwSPHOMIPxFUu9Dm9hJ5Gk2pJdn35gcprm3IOmvoGUqd_KQ6uZV6jH4olm9f9ux1w_wBXSU_xh-py4OwCnmZ0f0vhRIugxahqwEXufau9NEEHioBg2jJtmQp7qdODkjb-oCi3EHHwIhz4Gj1VBYeI3ZhtfaYJDthSKurPeOXeH-WYsv5rMN0dBUO_nLE5k3RjJg3zSjRkWt-lVKozAaaQVgrdqnpgvJDjTDb9G4xb4f2OVePzvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM9Zfy-OxvtV-YZu5vaVhSjb_QVgppNPi4rM100xXPKKV927pwgfCHFE5puCvUpHnjZPTcLxJilGAidZTaWcVC0iuxFfpquDPLWtTpP99Nd7DXXBhyVzdibhoUeDs3TwETqc5U2_lEHZtTBKsWWlSq10dKaVQmkgQ3Cg6LXCUy-gs_EUWHptL3uvaCJPuBmT699VOueAJZT8Cj6co79nyPzphFJyXl83EIcjg8Od1doJLCiW8jrWtnbL4kDItnTk6NmzXOgY6DJvNfuDPb7qUWsX9nQhO3iNINxzebV3EZreyoIwzpcYwsBQaYF0uJ4VAq9uyX-1UMVZB1o416fjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=F0SIDAu71WwugJFEqPscRM1BnKaEdI0cLM4TefvWiUUJ1AAU3ENIbze4ftAg7_w0_xywQMxo4BgjxY_wPDoNtyP4Qi38HCUac4O7UXG9SKjRTdSsVvg3yMRjP7eQkxFhP270-1F3GY_QlDZudF3vGmf5fPCgQUI-k94pPCQoAr_5N0B_C_JeWHEqdZL0Wr93-LgO6FdVVC-wP_Ge09iiK62kwnwqd-nwiOiajuTYV-l9UjjpxmuKRztDf3iaBfzx1tqEvf7MZUQFLrxs1bhH9aNq8lUsG7eYHftqM28n_cAGjG0NTXIIPL5EpO7Mi36vFnPEKgJXVlUurjQLzwjolQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=F0SIDAu71WwugJFEqPscRM1BnKaEdI0cLM4TefvWiUUJ1AAU3ENIbze4ftAg7_w0_xywQMxo4BgjxY_wPDoNtyP4Qi38HCUac4O7UXG9SKjRTdSsVvg3yMRjP7eQkxFhP270-1F3GY_QlDZudF3vGmf5fPCgQUI-k94pPCQoAr_5N0B_C_JeWHEqdZL0Wr93-LgO6FdVVC-wP_Ge09iiK62kwnwqd-nwiOiajuTYV-l9UjjpxmuKRztDf3iaBfzx1tqEvf7MZUQFLrxs1bhH9aNq8lUsG7eYHftqM28n_cAGjG0NTXIIPL5EpO7Mi36vFnPEKgJXVlUurjQLzwjolQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=M-yIp34qgOfMPvNW1EClPyqjYcdR1BZOlhIkTulfUh1E_TTnxMYrARs3xbB85oErCJvUC0IiqqFljkhh3pzZSvZ2QI4w8XY20z57J21Bw_XmU-h9O62_jiFhNH8s5xETe3MZnT9TeXpJcbaDfrxLnBAw6gcwWq-Tqixk4IAVGVRUxiwtvL4BrRgzoYWHhkzG7YhZbLsww8oElP7vJWeFXCfncrSb6BNEZlp5_sWh7IpUzuNugIZpcqKous9gN_ZuqyGhtjsaWtSUgOBwOGZRJnVDELap8NxN8F9dYYnhwyQPOG3O_8MFs0crjo0Oq8cVf4cngMsN0HsMoax8VkCbKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=M-yIp34qgOfMPvNW1EClPyqjYcdR1BZOlhIkTulfUh1E_TTnxMYrARs3xbB85oErCJvUC0IiqqFljkhh3pzZSvZ2QI4w8XY20z57J21Bw_XmU-h9O62_jiFhNH8s5xETe3MZnT9TeXpJcbaDfrxLnBAw6gcwWq-Tqixk4IAVGVRUxiwtvL4BrRgzoYWHhkzG7YhZbLsww8oElP7vJWeFXCfncrSb6BNEZlp5_sWh7IpUzuNugIZpcqKous9gN_ZuqyGhtjsaWtSUgOBwOGZRJnVDELap8NxN8F9dYYnhwyQPOG3O_8MFs0crjo0Oq8cVf4cngMsN0HsMoax8VkCbKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=bZgxQLfXB1KvXJUu1R_7AEKipjB4wmuBXxAuye-ZvJ-sWoGzEe8EGqvljZXlb2Fs6TKaUDsdeldt_AYKHK4Wbl3BPV9etLPU8HhPieOj63cW_T9YmTFyEed9AB9vz7xHpl4AOvxXNsVC0LWnoYoQ3jqO_BVhxyO0TovusGY8B_Wgql7F5dyx1sc78Q1fQv9JoF9Ry0ANLa_nbqEaUGYQODwXrlqOmAeUCSffhXBI25v-z6bImwPQXhQ2ymDgaB1FGtcWkrgalk8V3N1nFAtdym6tkwJ6Wx3falHcUhaHeI3ZxKCdYqR3Eftb7js8uGJCoIMeVu2liucwKQPPXiDX7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=bZgxQLfXB1KvXJUu1R_7AEKipjB4wmuBXxAuye-ZvJ-sWoGzEe8EGqvljZXlb2Fs6TKaUDsdeldt_AYKHK4Wbl3BPV9etLPU8HhPieOj63cW_T9YmTFyEed9AB9vz7xHpl4AOvxXNsVC0LWnoYoQ3jqO_BVhxyO0TovusGY8B_Wgql7F5dyx1sc78Q1fQv9JoF9Ry0ANLa_nbqEaUGYQODwXrlqOmAeUCSffhXBI25v-z6bImwPQXhQ2ymDgaB1FGtcWkrgalk8V3N1nFAtdym6tkwJ6Wx3falHcUhaHeI3ZxKCdYqR3Eftb7js8uGJCoIMeVu2liucwKQPPXiDX7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=gbdT41O_32PwRI-xM0Q8nH5Xzbbm_KQ6yCIuDGWZROsEEFJC3ZQM3unhdl6LObqjRmLR1_hVZSwt0Hgl4fqLYqrTMfuZBBlgLAer31U4SdAfOnDReinq6_kVj0iEgBhRnJlKOQ6HbivVYT1zLxBYy_hiwfK0JH0esZU23wujit-HTZtM8L_ztCnHFORBrFUSbmf9XdA5fWdtUF8HNyvevZN_6uhgA-FgECvEEmEFQRSjJ-AUaBQvhE5ep6fG85-lMpFlJozOiAvUXdw_UNkKSH9-fazuYdqoUpGEowEUoULL296mjob-ED0if8ako767a3zQAYENCfAlSWPz0RUnRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=gbdT41O_32PwRI-xM0Q8nH5Xzbbm_KQ6yCIuDGWZROsEEFJC3ZQM3unhdl6LObqjRmLR1_hVZSwt0Hgl4fqLYqrTMfuZBBlgLAer31U4SdAfOnDReinq6_kVj0iEgBhRnJlKOQ6HbivVYT1zLxBYy_hiwfK0JH0esZU23wujit-HTZtM8L_ztCnHFORBrFUSbmf9XdA5fWdtUF8HNyvevZN_6uhgA-FgECvEEmEFQRSjJ-AUaBQvhE5ep6fG85-lMpFlJozOiAvUXdw_UNkKSH9-fazuYdqoUpGEowEUoULL296mjob-ED0if8ako767a3zQAYENCfAlSWPz0RUnRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg5lrLO_v9W7BKPfMP3zieQrzTc5ztU05hCJv0BjRBsAdHeut1VBBbgOUC9wjmmH_Xliz5TC6lTHeN7Aiuvcx4On9oYekMQr2WMIWOhVPdvRezPzJt71tNafv2AMyPMboshZVEGWulTLUVeU2C5BzOvWX7Hjq7u_5dgDljlIIkD-XZXZ6T6mWfe0RmztYqLA8bpugwTji2eINtNeeF84Qn9QgBws1ksGb9O0n-YJS_O-5UJ6NXYz6WJMc4JhN8NuE1NgSMrkCzlaCUlCylG6KfE2Uzc8orFWLojY46pcwqpFQc6gOl_TNOY8nL2rmzLUNJignhr6klDqyNuE2GJaqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=fvbx5T9JAPgQG7-tARhzpUwtRL5JbYX0z058qB0pk70hm_wMuE2kfLawqUrFwhsP0B2ImRn39fZT7NqzhxqWiciKkAjWAkIfNHcnZdU4pLdl3DgPvJ8kM2Q6d47e7N2882e9o1h5-SzeKlRqWL68V_G-cAgL_0UKFu7wdSwqeLO97fV7l2oSCY5KaTy_V5TArvLhGEYxDf-Vzb4600J2b-XQ5tgKD4JEVYzfE7hLB6nnrSk4r0beDPQEq4CP5b5M94jmZh-MDWqB0xCOaPSzpfsH54LwtB-onNJMMWcRCu5anFFgaMoJDFnRPMULMAadp1jDV4ubUTlijVqrhfB9sDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=fvbx5T9JAPgQG7-tARhzpUwtRL5JbYX0z058qB0pk70hm_wMuE2kfLawqUrFwhsP0B2ImRn39fZT7NqzhxqWiciKkAjWAkIfNHcnZdU4pLdl3DgPvJ8kM2Q6d47e7N2882e9o1h5-SzeKlRqWL68V_G-cAgL_0UKFu7wdSwqeLO97fV7l2oSCY5KaTy_V5TArvLhGEYxDf-Vzb4600J2b-XQ5tgKD4JEVYzfE7hLB6nnrSk4r0beDPQEq4CP5b5M94jmZh-MDWqB0xCOaPSzpfsH54LwtB-onNJMMWcRCu5anFFgaMoJDFnRPMULMAadp1jDV4ubUTlijVqrhfB9sDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=kNR49T_3HMzQyGMUwaPdA4QLbQQEuH-rRNf8GaTNHblPthVyqiQIi0eauSU_ueEAM-xlyOzggtRXrhNqYUt7Ru6NQ79D-b5ZeLSagSmZTNgzEd0rpvYSG6Kup7PoHXcuvi6Z_z1FoxNwLuR5zCLjp2q5Tj18nPLkp_FGDm5mwtKF8aYeOhVz6Xy_Fv6VI8LZaT5a44xFiC4EIa5zrd1C1vDlIOigriNugezGIvOJOp9W5hdCOVXGQ1JPLG9BtNA9MyjI9OCHHdtEFnCsS_jS5xLG2SL-WTaNWGzOVIzc7hDhAwK-wKHNRR9riNDM19s2Vv8JvzT_S4URHlxdeZDMpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=kNR49T_3HMzQyGMUwaPdA4QLbQQEuH-rRNf8GaTNHblPthVyqiQIi0eauSU_ueEAM-xlyOzggtRXrhNqYUt7Ru6NQ79D-b5ZeLSagSmZTNgzEd0rpvYSG6Kup7PoHXcuvi6Z_z1FoxNwLuR5zCLjp2q5Tj18nPLkp_FGDm5mwtKF8aYeOhVz6Xy_Fv6VI8LZaT5a44xFiC4EIa5zrd1C1vDlIOigriNugezGIvOJOp9W5hdCOVXGQ1JPLG9BtNA9MyjI9OCHHdtEFnCsS_jS5xLG2SL-WTaNWGzOVIzc7hDhAwK-wKHNRR9riNDM19s2Vv8JvzT_S4URHlxdeZDMpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FB6FlE1UdljTUKxbOD4D-0bQL8J60JE-BlTc-53J9WBAxEw3MDHI1QvhdgT7lmWC-IWosQBDTESkLWlZD9m4Sy8B_4FOgg1iD2Ira9Ps6D024nugWF8QylGVaE66AESYrXm4enWLypDlgbC9nXcQP2GcyQjCBqaKfpMdEEUWFScvAd1xJcx6gn1S24RlmkegSQKGfbeggZg4lvPmLht6Mu98_3kX4TJAUwvZPe6q8LrFNFCHxBZTHiUrhjEKDpYm7PztUpbjo8vOemlCKCNkkghLFL9JGTL6vmyxtdgQQeczSPsbL70McmMFWOjtpUm7YgN7mwNbWYH8I8HIhHymdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/If-M80DDFhXlOhBG0i14P-WZkT1yYwfI7c_-y7xPOa6wnK691Gui2JgeDwEZZjSHMMfxsg6sMEqUMlzBjjL1jX8bOJbelhpypnMVTlfLy8kPTq01aRqlwvWCfb86-iV3-zEA7_rh8G0nkkXsmpinwjpdAf3ngDEtiq2dUlviOlnkkOhhxggVOP_AW_PylWeYFAexg7X-v2f_-lcqdjrW9vtizIXxyNwLjGEMJ5t7aJ12TiLy9GUBorn53l1WMO5r5ZhjjHf2IOP2tg_Xbt3Jd_LYopl6sm2_x7lT7xQqdPCqQv67cWOMImwCRhsscrwNqsMWJ6sp7RUcl8kJflFb_Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=eGvTzCr1cpNjTvwnKc1eVb7_lqfh1ZQcIZun6FhopTEVBa0V5kqCaDw6Sl-D2IbxLpI00KY_KoP1DjXjXog3IajqQVa4VUs1dG8nXSXnIw1f2qXtcLLtse5s_k1hHG_xlAH0v1kGbGnHLWCdSY1mtD1nNOjxhufOTI8cGJlE4jCtiSbCRLkTscddsVk9T-wIV3BbSzFGf7HdYRP6ndmbXvn8KtpBC4_XbTghuuQGg59N_h4ELWhii_KYUqfMkrYoftz6zWfTjAW2PwzN4lDdgee7bVOAEMhfHeiP-mETbgJuz3bSfX_k3JLA2KwpCAaMk7K0lQBoN98-RGSEcbpquw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=eGvTzCr1cpNjTvwnKc1eVb7_lqfh1ZQcIZun6FhopTEVBa0V5kqCaDw6Sl-D2IbxLpI00KY_KoP1DjXjXog3IajqQVa4VUs1dG8nXSXnIw1f2qXtcLLtse5s_k1hHG_xlAH0v1kGbGnHLWCdSY1mtD1nNOjxhufOTI8cGJlE4jCtiSbCRLkTscddsVk9T-wIV3BbSzFGf7HdYRP6ndmbXvn8KtpBC4_XbTghuuQGg59N_h4ELWhii_KYUqfMkrYoftz6zWfTjAW2PwzN4lDdgee7bVOAEMhfHeiP-mETbgJuz3bSfX_k3JLA2KwpCAaMk7K0lQBoN98-RGSEcbpquw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbaH0-l0XkkQUuuRDYpo6qtkYIYsl57D1DJqxLmR_wHc_3m3qKZqhpOXamMtS6l_dTOiadE3Z7fsNAc53VebQXK2yCmm2gWAi1gXwLHHq_mV9XTEyBZFoN3TfGCJLkbCS4Loc5kTxBTjbrFt49krMUtZ6QJNi9ParourG_UefL0Wgj23RsF9P2fLHZUSN0FL8KwSI5sDkH-oTpM-0xh74uTqYKr2cDdbXDoaMZ5dlkyuIiJrK5l_QT62JGoicy0QcB1DvZZ-qRgyv-DPY0iJ25hjMu_br-JRY_arMUIRKjb5w8dayO8dP-Uf_rmDE9QPaL1-P2gayc_sF6-n9tJHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAWAFfoQwonU83PJCnHwloRqhuc6hms_5-QGwzBLP2XcskjS2wektfH96nRBeRiwPjiSnkWjyBxc0Z9cpNPux9rG_hR53DCBeidgZ5JhNGGyFVWOaEbeWNrj8tJNeiSyt0D2I_0XMI_GxQa9M9Gm3lds4UiZn-Kz5ZzPyIwmdyq4RK4jQQrkS8bGgPXhyJL_xVTRApg65-WTTJzBWt0MoSqaQzB9pmYABOu2o5VDMRpezQo_4CrtpRi_XcW9bDRWqu0veTrlvaOM55LcYZAk336dUAseYTr-f43dPepLSRdv-ouEAJ0qBqUn48745oRcHDLeFvBgQADtGgF2m6u9pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fodMt2J7YjlpH9ujBMP1EEaT4h-k8jNydpC5T6a8ljTFdWTvIogI8YzVwqHUovmVW5EJVMq41VlwBuaiKd_DvXICmZjcmY6FG-3QLiW8D0tec9if8WfT0zVRTNPWJvJb_kC22eljIQ74xHk9h5256Jn9L6RhONbPry5M3ihdeSpmxiZEE4AMFnagHlAdS2ilgfW1WGksY4m3hhHBGtRZnvafNesIjSwJgOfIDlRmA-_hIWiLCPN51W9QO7zHJHlsdt7B9USRZRQBM-DfGjwAwhwy6hky7HDA9Ho-U9aroNVq8NfNkEL0j7Xin3ddSv2ePnu70p0DAJ5ORkp0jIDSdw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=itYblf7Bt3RQlznF_z09-V7rAclbjLZD1LU3OYCh4zwk98M4kA2rKELopz9PAxDhg5ntWeN8QkPQeYprLrvl04kVJkxTs8LJX8fJhk1OUpxXzqOVVFyQ3baWJG3MEBTsPnd16gJfjlb3jTuos7m9US4Jo6HJrSdv7aq3HGqNZ3d9bb3pGNhtrt1mb4gTrZ2wMDcBySBkHTrtsteh3mqzY68FcWNkcYLGFqYQtYTiFtaz67EZHI2i0UPZBkzXGITTvJzweL-mcbKJWia9ZngGIPzPh9ApSKSlNAjSIc4r-ngWtBJGWBUnTvcYltZX7T3HDilc62u2DSvmQT39chDeaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=itYblf7Bt3RQlznF_z09-V7rAclbjLZD1LU3OYCh4zwk98M4kA2rKELopz9PAxDhg5ntWeN8QkPQeYprLrvl04kVJkxTs8LJX8fJhk1OUpxXzqOVVFyQ3baWJG3MEBTsPnd16gJfjlb3jTuos7m9US4Jo6HJrSdv7aq3HGqNZ3d9bb3pGNhtrt1mb4gTrZ2wMDcBySBkHTrtsteh3mqzY68FcWNkcYLGFqYQtYTiFtaz67EZHI2i0UPZBkzXGITTvJzweL-mcbKJWia9ZngGIPzPh9ApSKSlNAjSIc4r-ngWtBJGWBUnTvcYltZX7T3HDilc62u2DSvmQT39chDeaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Ekhkw-c7Cn7UYDXYP-hUxcDDR6XxzoPbPFkPHZgtcp2tsV5HIl-C1LRbdMXUA0SfuAlYpmYJV8XBNRsgXHtR5oQd2UGriVEZMMWNJe-lAvLj52AmyEVChdc-5XciXG16PVa0LLVKB7VDg2SVLcrEhiLkx6aVi0EeO9iuZ3NYK9huBKLytkMR_l0WD4oK1vUkj7PWXIbwplVJl6Ab37BKrf4lhyCe3iDVV9BIGFS8WP9yTLBWlzGKqvuXTmQSzFWSbEk0CdB9Ny9c2ApfVvDqRFWB1RmZ7o0z-9Hw6LmxK8-24c88Z511cJgBePMPyK-tMiWoih1yYCGol-N_YuA8Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Ekhkw-c7Cn7UYDXYP-hUxcDDR6XxzoPbPFkPHZgtcp2tsV5HIl-C1LRbdMXUA0SfuAlYpmYJV8XBNRsgXHtR5oQd2UGriVEZMMWNJe-lAvLj52AmyEVChdc-5XciXG16PVa0LLVKB7VDg2SVLcrEhiLkx6aVi0EeO9iuZ3NYK9huBKLytkMR_l0WD4oK1vUkj7PWXIbwplVJl6Ab37BKrf4lhyCe3iDVV9BIGFS8WP9yTLBWlzGKqvuXTmQSzFWSbEk0CdB9Ny9c2ApfVvDqRFWB1RmZ7o0z-9Hw6LmxK8-24c88Z511cJgBePMPyK-tMiWoih1yYCGol-N_YuA8Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=B4_jy1XzP2kF_U0RbBYPtahaesL2Ri42Vbwd3tOxZ86fSivEB6Eo5FKE8Y7nfcx-aRySuE13xS8chUQDCk1X4vc7UieYkVtj8XTkwZEe6HzbTclrkJpHTWPUnd1bvCqTd9vNx3j9SGXwAypchhuqmy8t9WkbElGIyETx1AA0xHq7pTHtarSDGxeNSdgtoAlwhlR7c1aICGGvTwQxC8k97bfrRBPzPeMYMu12WtDvXDJI4h6c2K-AiMLsKZdoocxVVqETYc3-j9p8-9cqdaYAbLuOA_AHo_ThySNtztXVrAxG_tKowWumtEqK1k3VOuWWl0s2_Uv1ak2seKFUKoiKcYLmpn0FXWixZuOIO5REBrUdiJ6sFHF9R3jNQt4gdnjpYyPpI4MyO_2ZbU03qunn-UgFKT8GggwNqF_5gXun_ychIt5m1h-N87K3E_Zzg8d3Spc-I6jUC3wqkKjNIJ83SJ7cy_hWDy5MhsEhCQsQbTDdFE8iqK6HjNx_iVIfXjlCwgBFIeN3ujo4gN95IScJHZ5CcxHWFyTO20WmGF-dk9zYjmNlzR8mNoxcM3FzxpXYNXQWKZjxOVdEqyaO65z7xdBOwpix1tMmu-E9lj6X5z62hGzU9ucRB7SrZJFPvg4_bGsPDF0d21IPRyt-mo_3tFG2Ge3H4wL3F4Z5v_BjntA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=B4_jy1XzP2kF_U0RbBYPtahaesL2Ri42Vbwd3tOxZ86fSivEB6Eo5FKE8Y7nfcx-aRySuE13xS8chUQDCk1X4vc7UieYkVtj8XTkwZEe6HzbTclrkJpHTWPUnd1bvCqTd9vNx3j9SGXwAypchhuqmy8t9WkbElGIyETx1AA0xHq7pTHtarSDGxeNSdgtoAlwhlR7c1aICGGvTwQxC8k97bfrRBPzPeMYMu12WtDvXDJI4h6c2K-AiMLsKZdoocxVVqETYc3-j9p8-9cqdaYAbLuOA_AHo_ThySNtztXVrAxG_tKowWumtEqK1k3VOuWWl0s2_Uv1ak2seKFUKoiKcYLmpn0FXWixZuOIO5REBrUdiJ6sFHF9R3jNQt4gdnjpYyPpI4MyO_2ZbU03qunn-UgFKT8GggwNqF_5gXun_ychIt5m1h-N87K3E_Zzg8d3Spc-I6jUC3wqkKjNIJ83SJ7cy_hWDy5MhsEhCQsQbTDdFE8iqK6HjNx_iVIfXjlCwgBFIeN3ujo4gN95IScJHZ5CcxHWFyTO20WmGF-dk9zYjmNlzR8mNoxcM3FzxpXYNXQWKZjxOVdEqyaO65z7xdBOwpix1tMmu-E9lj6X5z62hGzU9ucRB7SrZJFPvg4_bGsPDF0d21IPRyt-mo_3tFG2Ge3H4wL3F4Z5v_BjntA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Ypd0VIZZul0LNWn002Wiy9wdePHFWYc3-KEMONq29QeruLGBJF0hyrwtLcVhHQ1iKtywywp543LAi9vwZJI0GzDjyHG1B4QYbwfsYuVF4VghyuQrkYcMHKjW_LJWl2ve6lRwLv4SzdDhbT3PGxprTSfs5rzI-MFLDAlce0pamoFmeB0tsNjHmJ6XSZYzPUSC7SynOe_kDNgBAHuK4LNDPjILzTPUlQ_PWRvmsC9VO5EZ1GvxhB3eSGKf81ifZjfZyf7rw9RvlJQcBuXTpZVqNOy9M6M7eLp9c640TX_IfGjka7sgkVx1qU9myvjFTADvPp450W6s9N9GVrwWmoqeG0MocxAh11UY32h-07V7sJJd3ZQloDMgkw99J3Eboxj1k7yn74cSKPdihi_zRt2CKFPvZxdZdaXALE_wuuKq5SbRMQfrqK9iKJLogOVyffkGIheSCf2ZAM2v4a0DgMhFs_Zv2y3XzFKI_BOMenLNMd82J3RRD1oGCpwdmMcfQxpF8f5swQ_RelX07pv2vn6utrr24KWzu-w0804AP3wYeDAvA4YReFjml8rqelZT42Ttg87lZSMVOV4t2mZ7cPIlYxddv_oSg0-M73Px8_Ib0xQnQX1Oj9m6lqdgQHCN6OmcUIw_T7xiXY4bIRDekkc5eTpJTO1NHE_kvgNA_DQhOyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Ypd0VIZZul0LNWn002Wiy9wdePHFWYc3-KEMONq29QeruLGBJF0hyrwtLcVhHQ1iKtywywp543LAi9vwZJI0GzDjyHG1B4QYbwfsYuVF4VghyuQrkYcMHKjW_LJWl2ve6lRwLv4SzdDhbT3PGxprTSfs5rzI-MFLDAlce0pamoFmeB0tsNjHmJ6XSZYzPUSC7SynOe_kDNgBAHuK4LNDPjILzTPUlQ_PWRvmsC9VO5EZ1GvxhB3eSGKf81ifZjfZyf7rw9RvlJQcBuXTpZVqNOy9M6M7eLp9c640TX_IfGjka7sgkVx1qU9myvjFTADvPp450W6s9N9GVrwWmoqeG0MocxAh11UY32h-07V7sJJd3ZQloDMgkw99J3Eboxj1k7yn74cSKPdihi_zRt2CKFPvZxdZdaXALE_wuuKq5SbRMQfrqK9iKJLogOVyffkGIheSCf2ZAM2v4a0DgMhFs_Zv2y3XzFKI_BOMenLNMd82J3RRD1oGCpwdmMcfQxpF8f5swQ_RelX07pv2vn6utrr24KWzu-w0804AP3wYeDAvA4YReFjml8rqelZT42Ttg87lZSMVOV4t2mZ7cPIlYxddv_oSg0-M73Px8_Ib0xQnQX1Oj9m6lqdgQHCN6OmcUIw_T7xiXY4bIRDekkc5eTpJTO1NHE_kvgNA_DQhOyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=d6sYRqrszoJ8WSr1bBl5OJIXjkOkk58R7LF60u_p8Yj6xMYGWt7xLM75LBM6EFDbqGnIJr9Y3tf9DHTDPnwPfAg4r8ox0nKKPgMG-fL4TAk5rWm3H9m-FQFGOb7CQIStJe4x7F20h5flva-ZusP5I_n6wPUZmMAlG7kADLn0DMOuU5pUhj7rLM7kWU07oPhZmeRJ89CBFo2psXoezLMUyCXbSjy801avSByZkWo391UmtMCjlx0645e81RQgRWl_shftrKdAZ6BfxwJ9I8mN6jHAllacZtWOCbPrUGjGkHMsUTY68N0cBzSPKVaChjlvLKyVR896si98EaOL_dYL2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=d6sYRqrszoJ8WSr1bBl5OJIXjkOkk58R7LF60u_p8Yj6xMYGWt7xLM75LBM6EFDbqGnIJr9Y3tf9DHTDPnwPfAg4r8ox0nKKPgMG-fL4TAk5rWm3H9m-FQFGOb7CQIStJe4x7F20h5flva-ZusP5I_n6wPUZmMAlG7kADLn0DMOuU5pUhj7rLM7kWU07oPhZmeRJ89CBFo2psXoezLMUyCXbSjy801avSByZkWo391UmtMCjlx0645e81RQgRWl_shftrKdAZ6BfxwJ9I8mN6jHAllacZtWOCbPrUGjGkHMsUTY68N0cBzSPKVaChjlvLKyVR896si98EaOL_dYL2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZixQb8wr6Vh5s1yZtQv5iY_wRwB1Ia53azAeMXUG7Re0drP41iYWDj7v_Y0uQFFK5kd0IxH_4BCtA684w34DdPRD6rQKy-at9L__qnCNbH81fVC5wvfDJP7C-Wu_g0kZBUnGyC4N3MJwByPStiBlZRCmABk1cNhpk0glt1LHG1_SuAYw5STyeSgQ5w6ybJm5S3eBOmtI1aXQGq-NbW4S9o-KQD6K7K2bKvowaLWTIvfTP39iaAC0m9rA6oPNIoQymhRKGjRvO0iLawoIwVf6fi-XLVbDgdGvzkjf48uHR5Iyt9S5KbViFJLqADbwUl2ciYObj8rpAoL55BjPTQM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
