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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 20:42:00</div>
<hr>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_1yyk0YnGgsxZzCqvwohCIFTAO9QROG3g-FsA05ozjHfmn9ji7_CpvXQdF87WUu7dfyNCLxK9ur2c7ec2fgyo-nb6RGEfjnhDc7U7YKAbWE4qQtlQNA-9rNV25kxx-w0BliM-BekUM-HBMobCEU7BSPBdjtSdfRmhCTnM525o4xdPCzR-7f-pd_PTeN8b9XzmwfmIkds255Zyij4Zb2zuA1yI5YhGjpcM8stVLIV4lheNtkVUPFiltne9U5EdtufSn0qF699kGThVHhvOAfnFYpI7asBsdyBVPIkGAN4TmunuF_PWiYLYz0OI2O4YoWXAgSsAIvOIbW1lIrUg-gzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fBmYnXekCoR-Kimg_xbN__OUz7qcBb6qVjEGaC1BayFjcgpeckAyCdhuf53i6dL5fKXQwWru6m-VTvkl_vDb71soTxG6lTlny8Rf-Pl2mgVaCpL8fqYC3IjMK3TjLp3xbgLRlFQ5H82H8lrir-mfd0f6jYlERIWjZ1SRnE7leHa4IkbLmOvj7lSYqnpB-8XXXTlBjPObQAaDMHZuQ6VgQz5RCFlk5_va_MLy_c8AyAwM2U5w4zJ3hWeQ5A95cduI78qkNUnSWJ-P5LeOu04pwnEzvzrcVnkMJTyPWvAa5_l9OC3AJSdFl4smydqJ1w-xU3ba3Wr4mdx4TGxP3_xqQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=LHUJhoCO0yZZLx58ywboooG86JoQAWgkexEex1xJ122b6GV00faOs51XEuCU7JWIyReV1feObG9bJqecm0U71E1xbEeBe4eai-A47NBlQApQ-HJiQHCZAgrgiU9WxeuUWUKuaWQWePQTxD6kn-42mc3l1AJ2Aateqcvni5tlnlQXU1QnbRUoRLjElUWyu8DUFFJHzLiEw5OGTPpZa2PvHPLd8KcmkQuDG8J-Qc569q0FCPVFqf8DzOEsZs3rOLn0dNOZrUKLZEC0CJB-KR6nwi2RAe5eYiLkPoo-exO2-IG6kn5dMIyzLRH-rHEnBZ5EfRr6Q3Nz46_3NHR27VdmVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=LHUJhoCO0yZZLx58ywboooG86JoQAWgkexEex1xJ122b6GV00faOs51XEuCU7JWIyReV1feObG9bJqecm0U71E1xbEeBe4eai-A47NBlQApQ-HJiQHCZAgrgiU9WxeuUWUKuaWQWePQTxD6kn-42mc3l1AJ2Aateqcvni5tlnlQXU1QnbRUoRLjElUWyu8DUFFJHzLiEw5OGTPpZa2PvHPLd8KcmkQuDG8J-Qc569q0FCPVFqf8DzOEsZs3rOLn0dNOZrUKLZEC0CJB-KR6nwi2RAe5eYiLkPoo-exO2-IG6kn5dMIyzLRH-rHEnBZ5EfRr6Q3Nz46_3NHR27VdmVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=GeazpC-gLp3kczbSU7t_LhQR-RJPD0pTfNNlaZ7xKUjtBJvwDHAoIK-C9VBF5RVXeaGOiGHsNuCjPuxcnbfEa3sk5JH0YBjAAP0ocq63-4vdnaNIMp27nzjzCXqfN5R0KJ17vZ__vpjYWTd3KrPVXGApdT0GVmFVukgOqsybBqZJaPxwy_hs37y6HEu0aUf2RxJK0Okw2uSxluMUo1CgkiWN0DeMMcXMmbBfIQcZUIP0UKlEsIOT4j0G0NufvypvqPnLkXIDiMq12HUf9OCxQHNwtbx9fPTVkKXq_iB3pLUFDDJ7JjXJxpkwK2cDPfW-0H-VOIN5MugdcizVuDUSFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=GeazpC-gLp3kczbSU7t_LhQR-RJPD0pTfNNlaZ7xKUjtBJvwDHAoIK-C9VBF5RVXeaGOiGHsNuCjPuxcnbfEa3sk5JH0YBjAAP0ocq63-4vdnaNIMp27nzjzCXqfN5R0KJ17vZ__vpjYWTd3KrPVXGApdT0GVmFVukgOqsybBqZJaPxwy_hs37y6HEu0aUf2RxJK0Okw2uSxluMUo1CgkiWN0DeMMcXMmbBfIQcZUIP0UKlEsIOT4j0G0NufvypvqPnLkXIDiMq12HUf9OCxQHNwtbx9fPTVkKXq_iB3pLUFDDJ7JjXJxpkwK2cDPfW-0H-VOIN5MugdcizVuDUSFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuoWWOCHm_kFfO-nv2tmld022BWTrALhgq00P8gxmv9XspOtfytdyfUNLw_wpkHJztTG3H17bf9bv2pE7aswkDe2rYvY7gkn7hAfD_FS8kidOEZmAw14K5EokZfHmm8uqBWfVfcfP2BfhkYYh_D4e-ovKM7ZHpfcNhnmn6egmCs_gR2w4-v-ukDfk-k88S_14eg_XU1ptDMoVtQk7TROIYZ_LXsqkZ-h53EVQQDQrBVWKDNR0_-G2HZSoxIRbOonItUbZADSHevifgU_ho5mJw0RJK3Taxsf_oDsDcxXNoxSMvey40UdnLtz0zftfGF5zrJdDQdyjcM866NVbguMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=O_YKwXdv0vI3UJgH2FLWsyyb2-nQrejm_wOBZDpgUnzpkjRYiJgnQ4yJVe3Qov9SgZSS-mPNtbvyGXpBA2qCOd5rxMurDLAUqy68JInthmChUOK8ipIyY_tURHPE7lLq8Nvk67HvVf_Dlz4Dij3mc39szSMtxJ6zN-4rHo5GtXuqIJYckJD9u-4pZSz3tQADhbEvXvNzffkaOAyMhIiFyT-4uXWYDFI9uJjOeYWbWnVu5YgPikNxWGT-UqVFilYGVM6MFc5lnfjEIT3HDmFxt-emL-qAmepkvBo7QROE6VipcLtCAn8zCX-xVA5YvM1ahrMD4yvk2UeD5RMotp5ylwhZMqO_2eTy2PMpFh5UDV8c_wBGlVs7lS_caGuCulPbOTPoPT4EZR1qTCikVoRT_YwvqzNEjgyayam-ht74Bx96tYjtQJkWrn6AwoNJnkH_x10JxnWyr_4OjlSSY1cJF4rbtfeG_cFkuxSihYYMlCIlfZCCxyEe6b9Ue5LhbGKzIinAYZKYbrEI1qOz3QSRvMeW2tzlt0fGxKViBAt7CPGFwHR9z6lWEwsc5Nznjv0_-Q0Z0yUFvTba5R7mEkHq3nr_ccPHnkIozUTS4QWDdAEFTXJLt47CJoIGwAGu-PW4WGIWL7QeM-2Sql2DYHFYkwYX-RkbEG6kra1gs9E3svk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=O_YKwXdv0vI3UJgH2FLWsyyb2-nQrejm_wOBZDpgUnzpkjRYiJgnQ4yJVe3Qov9SgZSS-mPNtbvyGXpBA2qCOd5rxMurDLAUqy68JInthmChUOK8ipIyY_tURHPE7lLq8Nvk67HvVf_Dlz4Dij3mc39szSMtxJ6zN-4rHo5GtXuqIJYckJD9u-4pZSz3tQADhbEvXvNzffkaOAyMhIiFyT-4uXWYDFI9uJjOeYWbWnVu5YgPikNxWGT-UqVFilYGVM6MFc5lnfjEIT3HDmFxt-emL-qAmepkvBo7QROE6VipcLtCAn8zCX-xVA5YvM1ahrMD4yvk2UeD5RMotp5ylwhZMqO_2eTy2PMpFh5UDV8c_wBGlVs7lS_caGuCulPbOTPoPT4EZR1qTCikVoRT_YwvqzNEjgyayam-ht74Bx96tYjtQJkWrn6AwoNJnkH_x10JxnWyr_4OjlSSY1cJF4rbtfeG_cFkuxSihYYMlCIlfZCCxyEe6b9Ue5LhbGKzIinAYZKYbrEI1qOz3QSRvMeW2tzlt0fGxKViBAt7CPGFwHR9z6lWEwsc5Nznjv0_-Q0Z0yUFvTba5R7mEkHq3nr_ccPHnkIozUTS4QWDdAEFTXJLt47CJoIGwAGu-PW4WGIWL7QeM-2Sql2DYHFYkwYX-RkbEG6kra1gs9E3svk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=JSTYAfIZTbByZ_HSYJLIESYObgKdw2oEZMvMGkbXnKtocH30T9hRwn8V50S1FUQoGIDHHlyByB2h1vR0sMInpBs3VuLzVRbccT51hUQKoEtSdVDQfxlVO8AP8KdvX20FEI-cRAhp7AtmOjyggqi-ee-UdwNfSwBabQdBprrT5k9O1z7FWhdnu4sm4BCR2ZYU7UN-TPJyocgf2vM_Zdiw7cLbIQDXn9I9I7AjI-hnaDsN1mk-q40H7QbdMX3YSpamhbriG09IBXuT3eOkAhnFE1D3YfCmJ5-2Q8f4mmEcxU_FtSGHU6bHlX8wxcHTOotVeYXIbRF3w8L8UTi5MpJ1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=JSTYAfIZTbByZ_HSYJLIESYObgKdw2oEZMvMGkbXnKtocH30T9hRwn8V50S1FUQoGIDHHlyByB2h1vR0sMInpBs3VuLzVRbccT51hUQKoEtSdVDQfxlVO8AP8KdvX20FEI-cRAhp7AtmOjyggqi-ee-UdwNfSwBabQdBprrT5k9O1z7FWhdnu4sm4BCR2ZYU7UN-TPJyocgf2vM_Zdiw7cLbIQDXn9I9I7AjI-hnaDsN1mk-q40H7QbdMX3YSpamhbriG09IBXuT3eOkAhnFE1D3YfCmJ5-2Q8f4mmEcxU_FtSGHU6bHlX8wxcHTOotVeYXIbRF3w8L8UTi5MpJ1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djQOrQD4O5Q_28O1SBDYehtqXFy4y_8hTGmGi-NrlTcjJ14E2WM8YXYoLP6gRu4pxaiXGhPmug4TOc-KbBv85v_tGV7rNurnOii9RkWX5lazsPiwfHa9GqKft0fNPAzIZ6loMCL_t5MVioRbnbNK1KEJo0nu6P6g16LyEo0l4lN_RXmqjgw604D4g9--hEkeIYxC7V0S_R8ZMraHguA7PGw5dk5PE29YPgopKFPJG3YC9ZrU4cn4iDwE0jSyreK7kD6tcmXoAOR_A5SQWCiJq81IdhYzDl6kdvlNnzCdBcsaZlrVDj8GqO0fFDnGwkMAisRVNnFZr-10no8eZKUUMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=E2A0so6MzmEb7EPWne290uwl2aFO9s1Az38JFdlx44nLIZ5JKECexSBqtDRWzKDycuDtKtu0RYoKuhr-vqYyvGT2KbgV9vKG7Xo-WrqwCtCBcjcq0T_lvvscT8r3V9CxxZIuO99RLWmYJVZBOfpwHXqyMLXktr3j0iVcOCHZ7NHJZjsK9BQZXBDvv8-pdHdtWlsI6EJm11lG3tbJmRxR5kICf9AOPpmkuSZCspVyzJfbfrHqUu4_KZSCXPd3AOy6VTKAbvWsQf-CP3_XAq0q0xYvoUK6s0BVfIF2C8hOOqSSxLs9_MLdgTBsN8lyv79dlEeWf8ln5dRvcEkxH6Z9vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=E2A0so6MzmEb7EPWne290uwl2aFO9s1Az38JFdlx44nLIZ5JKECexSBqtDRWzKDycuDtKtu0RYoKuhr-vqYyvGT2KbgV9vKG7Xo-WrqwCtCBcjcq0T_lvvscT8r3V9CxxZIuO99RLWmYJVZBOfpwHXqyMLXktr3j0iVcOCHZ7NHJZjsK9BQZXBDvv8-pdHdtWlsI6EJm11lG3tbJmRxR5kICf9AOPpmkuSZCspVyzJfbfrHqUu4_KZSCXPd3AOy6VTKAbvWsQf-CP3_XAq0q0xYvoUK6s0BVfIF2C8hOOqSSxLs9_MLdgTBsN8lyv79dlEeWf8ln5dRvcEkxH6Z9vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRTjV_mf3PDxlKJiYPTmQnqeElL6o_MXQI6oZ1PRO6w2UWmjN_0onaI-sDJ6GbYm1ZVEA-IAoCUic3qh6cc_auR78yt9L5qjaohgdMHf7etaBqLKYzNm8BtpGCQPENIack1uJVeeusNb3rg41pv31kYL4iUqQYJ6VIfXfVDNxiEyblNqfLiGq3RtUBoVNL7PpLu70YhsJKTAt0uVPLskMdlw1JUl3v3nqlrir0AMfjU_WjgngPec32f37QKmdGUIxzxKd0ty34WYIHFBY6CrqCq2Ktt1zoF423qjruNc6AUyWeHHDkVM_Gdg8rdAoUJ2apYi6Hyerm8EFzgUmAPZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJqycOJP7IgydSOgJh-93Krakvf0PDPiSqivkEO_trOaCr7CHlAYULWHHw2KblwMHjzLpUbmdDXy3az5dbRWAGLVG-8NZIHkGFIpqpQKXuzWEviDvaW8WStZgpfaaD1k96zwBaebGtfgyrrJUyoplJ1HlcxsVl6qsOWyXlB4eGaMOMI0H6JexL45E2jxqDYvDFKANGWKdeMTNIBHgD37ZEIHnbn_xjAz-4cy2Q7OgqKXPClFa7E_CvBLFeISpI8wVwNjmgBCVyMTCMm4W-IIEYN9kGb78L_1F8Kpiym8s_74rW9a7C_OMw7MpCKxQCU6ylGV1Qu1luCwy3WAJKJ_cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=RuRlJVmdfcaPWtSLA_jH6JukzD07dZ62SdXdlNNfEwn6I391c1w5Y4Qy-1j2abpj3Y_RmtDbRdmETZU0zx-adKCeStxtpllByV3HLTs9ndwLBbcYkIYzkwd3o0Uvwanpq7k5a0egD07vYa-Irv4AIrGmfoHu2rk-6xaAUhjngV2wwr-UzygjpKsPHJsZEXx0PUlIf8_Qwrb5rakyrXUPPZhnNMUfckpl2-R-5Opim_WIYTUB9deitaPZGBm3SqDduR0uishKm-5F_k4bewbSc-NStwEe-9gtuvVW1fOgmfwofsX_n2a8bA5d6CuD8uIUd90lTrpbsLA0G7gTQFOg_UsEbiu88FyqUp8EyDHkm3MvClw9NguT7mDGeiJLy4Ng-Kw9HT1IYP1s60M1T4NA1IztEoDGs6Qk0eKiRYfaGoipgfG3rmlMBygOkWXhGj2snZTkvj8Sh8uVEPBvWv6RwKlk838iPCHqCJ1DmY3Al5LTqC8s9vlbJmP_ifR4FmK-5sTSxmILfMu8C9Exh7hGoVvpKMLwmSEYahTn2GroPoqyPsQhdAga3UYw5LZl4Z4iuqD_0agzJonM1ccN18Kyq_p17MklhI5d5YEZODIaw9STtBnbC87xr544QEWgd2pZHLCtjldYH8268mZB1LrKqbQkqX0sgb_sb6Ni_4fv5IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=RuRlJVmdfcaPWtSLA_jH6JukzD07dZ62SdXdlNNfEwn6I391c1w5Y4Qy-1j2abpj3Y_RmtDbRdmETZU0zx-adKCeStxtpllByV3HLTs9ndwLBbcYkIYzkwd3o0Uvwanpq7k5a0egD07vYa-Irv4AIrGmfoHu2rk-6xaAUhjngV2wwr-UzygjpKsPHJsZEXx0PUlIf8_Qwrb5rakyrXUPPZhnNMUfckpl2-R-5Opim_WIYTUB9deitaPZGBm3SqDduR0uishKm-5F_k4bewbSc-NStwEe-9gtuvVW1fOgmfwofsX_n2a8bA5d6CuD8uIUd90lTrpbsLA0G7gTQFOg_UsEbiu88FyqUp8EyDHkm3MvClw9NguT7mDGeiJLy4Ng-Kw9HT1IYP1s60M1T4NA1IztEoDGs6Qk0eKiRYfaGoipgfG3rmlMBygOkWXhGj2snZTkvj8Sh8uVEPBvWv6RwKlk838iPCHqCJ1DmY3Al5LTqC8s9vlbJmP_ifR4FmK-5sTSxmILfMu8C9Exh7hGoVvpKMLwmSEYahTn2GroPoqyPsQhdAga3UYw5LZl4Z4iuqD_0agzJonM1ccN18Kyq_p17MklhI5d5YEZODIaw9STtBnbC87xr544QEWgd2pZHLCtjldYH8268mZB1LrKqbQkqX0sgb_sb6Ni_4fv5IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mz4MEN_qvMkjDTPsVTWkGWYrbwXPq58EJ-6UXCRB0DFV3lax9mqCzZflJSbOZG6BEwo_PZ0_8lSgC2qTbO1irsA_GliPbcAyUidP3Y7Sl4aWu8-l5p_B7_HVwYcApTZPoSMV8iqWHE0Rh-5wKAegPgOuOUWglEYVDAPqQkO6iLH5yYZcqIfIv8SiNZ-NEoi6Y1HX1Fn5qjQPLcfx2WxRJPS3WkriBIER1UM8tl1gZ2EcFqX7M9qrvb9Xc5aNOLuct_TpDIAwa7tmaZ2KB1wWDXZ_wyPW_qLBPpUWyPdMDrulDv-KCj4KDimvkgAtaxOPmdAMA9H0olcfyn7ZKBkeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDUmPVKgRippwILnJxVn7XgwieP8PmlXI3h47AZf6s3QZnZhdqbQygNhgOIxUIwW9mAej3jXAikT5okkzVqWduKi4rKg1SmyGW-5YR0CKChYoZIG2gvceCLFSB3_3fgh-FUsGgHtYvZahRGj76YXY7vqqlLeq6oiriXNmfKx5wf7mG-VuBAvSCg7C6mFYyqKM1I4A_fWCYvzBqM1R_rX2TAA8m0EuZzpvf4WAfyiXOCZq98Mko5Rp13PUKlI8vJEpRIeG12MVg0n_PChTRZIRD9cnmU74ofnl8Nn8EKBHAwI846JQuFRJ_V37LknOHULZDXS_rBo5LLMEha7q9sFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=PV8uNk9OikaSe9npJARKwex7iIP8HPqKtx5rdrJKaYDQOzGfRBYvNgKARKtE_k8PIQJZ5rud2CeK6bx5rmHIgcUUtgCFM3gLKJX1eyUmNK7kDoyBUgFE-XIS4S6PFFaW0xMf4lljdyz7baNjecvYGCj8jhUxFWFl0tjGfX7g3iQlx2ZLltkMwqy16MDNXIA5uW1yZ_-rJxsKx2bAzYLpA04V6B4M22PUdY2ijSsIPvqZ798CbZXTtJcWXH8S5wYfH9JvR_5pRh-S7wzVBYs38CfFsXEPAUpQBH_B-JeAJ3TVUJgKJma-Doxo80Mo54o9GicIuXoyLLBRbjtPZsleQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=PV8uNk9OikaSe9npJARKwex7iIP8HPqKtx5rdrJKaYDQOzGfRBYvNgKARKtE_k8PIQJZ5rud2CeK6bx5rmHIgcUUtgCFM3gLKJX1eyUmNK7kDoyBUgFE-XIS4S6PFFaW0xMf4lljdyz7baNjecvYGCj8jhUxFWFl0tjGfX7g3iQlx2ZLltkMwqy16MDNXIA5uW1yZ_-rJxsKx2bAzYLpA04V6B4M22PUdY2ijSsIPvqZ798CbZXTtJcWXH8S5wYfH9JvR_5pRh-S7wzVBYs38CfFsXEPAUpQBH_B-JeAJ3TVUJgKJma-Doxo80Mo54o9GicIuXoyLLBRbjtPZsleQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=GUlM2NrZJPDTNnPhElUiwiYQYz1xwg4RMagbxxtgJBcN2GXZWHRNrc8xggixcGnKaTjz1S-PjNdOgtONOeN2UKxKXo9ppdxHQVHaf7JnEpeNpqsH4aIamxHa3NTAY8Df0b9yDS7dXpW69MUy0cxC4yyfVE-clfENmSi3JiP0u1WbfG7L-hyWhRoGDOPDZxJLfIBeZluEnVDBUUrOudEPvcogBuQlKRT88omy027gScTnh3FUmlg6y50ZLEU9hiy3vsPxssL3UjrSeUDFzfLEd6RgomYUles4lelOGCv1asuU9qtBb2NraADdRRTezqamqD5N1j7aW8tcSmJjwj19Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=GUlM2NrZJPDTNnPhElUiwiYQYz1xwg4RMagbxxtgJBcN2GXZWHRNrc8xggixcGnKaTjz1S-PjNdOgtONOeN2UKxKXo9ppdxHQVHaf7JnEpeNpqsH4aIamxHa3NTAY8Df0b9yDS7dXpW69MUy0cxC4yyfVE-clfENmSi3JiP0u1WbfG7L-hyWhRoGDOPDZxJLfIBeZluEnVDBUUrOudEPvcogBuQlKRT88omy027gScTnh3FUmlg6y50ZLEU9hiy3vsPxssL3UjrSeUDFzfLEd6RgomYUles4lelOGCv1asuU9qtBb2NraADdRRTezqamqD5N1j7aW8tcSmJjwj19Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=ttm5adU34NOIIx3Zu1Q_ixXU-4w9OY7v8HmFkQySGGYi0MvGB_V7quKxTEbZjU7NiEnBenKcnLb1j9cTIIr6rMwWGp3l0a-l0aQm3Ug8ZA4Hz2lLC20DB7kqks0fIvEYT91_r0rMf_nubWseos9q21zR3UvFsqn-05aAIF8LtTfJrcMwU4kU_mXnbrGBVVcxsUpN_OW6fIny1O0YSpGkVn-OZRcjMAzH-De95AgWh4F7zXfXpPXQQvflLlnFPkjiehbmSAfT-PTOW8sFwfA3Vmpfnt6KGD1051P1JRzglXjqJ80vTsnelWQs7JmtXfnCTJIQrFjiGu_Kx4UaBO-bQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=ttm5adU34NOIIx3Zu1Q_ixXU-4w9OY7v8HmFkQySGGYi0MvGB_V7quKxTEbZjU7NiEnBenKcnLb1j9cTIIr6rMwWGp3l0a-l0aQm3Ug8ZA4Hz2lLC20DB7kqks0fIvEYT91_r0rMf_nubWseos9q21zR3UvFsqn-05aAIF8LtTfJrcMwU4kU_mXnbrGBVVcxsUpN_OW6fIny1O0YSpGkVn-OZRcjMAzH-De95AgWh4F7zXfXpPXQQvflLlnFPkjiehbmSAfT-PTOW8sFwfA3Vmpfnt6KGD1051P1JRzglXjqJ80vTsnelWQs7JmtXfnCTJIQrFjiGu_Kx4UaBO-bQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUpfxbFqyJu_cu6zQeA6Jmrx_8VD8IKcXVC1CiIbeHBi9VoyZGnH9E7MSPQp-DSsuHoiRkoAL0Mfzx4drkXYlfNFhWcS6H3ms6p1XW8mcBE2q_jZF6AIUSMy_59-Q7YBkXztUgnlYW-R6VDBh104NGaVzZ-wN4wcLCo5qrmJ4g5H8zJ5-yAgJxmdqLec_-NodhXR4uEZxxp6gyo7Q7U1yO8rLn734ObDp_OJYygcXH3q3pn8iC9DzM57uc1YIdlzUPMlCqbMq_Ov8BmNyUCT4NA-J_xgYqwjUU2CxubbL8LhfF0anIXjDfV1z4OUNZfg7HEi6Bi1B9JQrH6zFamnMA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8LMtPHzfAIcf9D5npx5AFzpj4ysn-iBNbyjPM7OwLR0FjGmYqIbp4xsEaA6fCr7ofqBfhXojYc07nA8Orx8OKjfTebmjwWf8wztB5W-0oVZK5jljZMBqZedt_2L8czEM2godrDFPhub2lmdBq4XTmgZAAlDX9tCItSPMAal9-X3fCE1EWzghV7JcjCtuktxwgvf3YDDFJ2dae7-v5o0Dd4SVQadLi2ToPbCHVbieD_s6TiUcTWw-X6JX91Z19HbQS6IvzOv4qbwmlC7dvS4-VzuQYXlaIturOcmYg_0oo4USI4Hh3r2--qlmKWhKPYRmA_DIuO6v2EuwJ68i-PhOZ74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8LMtPHzfAIcf9D5npx5AFzpj4ysn-iBNbyjPM7OwLR0FjGmYqIbp4xsEaA6fCr7ofqBfhXojYc07nA8Orx8OKjfTebmjwWf8wztB5W-0oVZK5jljZMBqZedt_2L8czEM2godrDFPhub2lmdBq4XTmgZAAlDX9tCItSPMAal9-X3fCE1EWzghV7JcjCtuktxwgvf3YDDFJ2dae7-v5o0Dd4SVQadLi2ToPbCHVbieD_s6TiUcTWw-X6JX91Z19HbQS6IvzOv4qbwmlC7dvS4-VzuQYXlaIturOcmYg_0oo4USI4Hh3r2--qlmKWhKPYRmA_DIuO6v2EuwJ68i-PhOZ74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=pQknscFEnEIdUQe6hO1FHpLLOwrSZ8uxieUsN-FqbrGxM2iX5bM0WxKNYaBLkR2Ktm8Cu70ZdFKojvamlKzmN2uE2-SUEOzMzqrqIJM54JUNV3SkGxbgxhaFrtuqupoKe2nnQlI22HO-tugzAQV-j4VFqtBaHLBAx3IxEgJMCrwxfmy0GVQ-rg9pmc1eoq7t9t151NT4ckw_YFdSoXTcbWLuTUuUEo4DCNYSy9OGdbR4pdWICkzy6FqDIi2KZ1LsxoD_3bUejFR9Sh1oV-A8TS1QkhdAlm7zgCQaXr2J8iMohdRonmtZcBZegCKPCbAq5qZil9ziIBQyn9NH5mItkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=pQknscFEnEIdUQe6hO1FHpLLOwrSZ8uxieUsN-FqbrGxM2iX5bM0WxKNYaBLkR2Ktm8Cu70ZdFKojvamlKzmN2uE2-SUEOzMzqrqIJM54JUNV3SkGxbgxhaFrtuqupoKe2nnQlI22HO-tugzAQV-j4VFqtBaHLBAx3IxEgJMCrwxfmy0GVQ-rg9pmc1eoq7t9t151NT4ckw_YFdSoXTcbWLuTUuUEo4DCNYSy9OGdbR4pdWICkzy6FqDIi2KZ1LsxoD_3bUejFR9Sh1oV-A8TS1QkhdAlm7zgCQaXr2J8iMohdRonmtZcBZegCKPCbAq5qZil9ziIBQyn9NH5mItkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtHbA9Om1jA6OFlrxfAHr--8jD68eojNwB-ygrAxu83RfhfJiHJiAocamP2l_vQ0mXuJIRO5-jtLI-P528fR9YlRqSsg5KaD4JxOP6kCdOH9mra9_17Uz2kbV_u5TltwnqcsleReHWuwFfSV58cZBVRYZjIyxiWMmWJFteOEYgTpijgR3cSRpmsXbt06t6CaTkXL9MztP_eHjDAYekfbMdGA4zwdDkKQ8Dx_BX_YMuSeA4mkT4aV0ICR3MA_ETfn6pdfCOXCgqA_bd_mmFdDHdUn_BN3HRVMzRps0ZBrF4O02JTv8SnyQENcrwCeXIiAWEpAUCr6fwVSt-oZ7U6VBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=L8tW4nu8SUsQp0CDptKTSVN9HSs4IsLpc2126WIq8GC3z1XY1LCwMEZzY5RnX49NckKKbQfYiD-FM_pXrcd4mt_hD9nyve8s-rMAFKEcI167Jp_dVBKMNLSdIstu8xuq7gKfCpJ5Wica0IXSf-leHUkvytreWC3NBOVyN84d2aKu-nX-t3UDxenJRHbQzFq47smaUNoaYw7JCZBX9nEoMyJmC6huGzSijVxuP3mUC-kVeRteXjUD0bQl8sPB2yUC2IiAy9cId6MHMbA1IuFvaIouUaHoFD_N46JaGI_2TJgE2UWMW2VRLeVn_5tXWY9EUcXgKZiAJTLFVHJ2YEtGXkCBprooKo-IIf9makhuhIMdBuRak2y30PCOj8lycpV4DVJqd1jN6NN9r8gUk9uSLrNVqd8WisfDtpelVOAC_u-LUtf6HT_IpeX-WX5Fuz1HlQd7FZytPE7cT0YOpYZ_oT0c73AlHJ1j68rEE3SPSiuDTZBrinYyjtUj6WC_fJgoAgGJUNB8Q07osCbhHmO8G3yfVIhTnHhSIaiT_OW36olmIeYxlbJon5q4SAicNAPlDV9M_fVj-3nNuYNhuOZdXYn892NT22CWyPAdceOKwhe4FRXq4wsCuu_Yn03JbGi4_D5NvPd-le9FB99kJuavlYK0QbR2g1eyLPNIlUSZv3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=L8tW4nu8SUsQp0CDptKTSVN9HSs4IsLpc2126WIq8GC3z1XY1LCwMEZzY5RnX49NckKKbQfYiD-FM_pXrcd4mt_hD9nyve8s-rMAFKEcI167Jp_dVBKMNLSdIstu8xuq7gKfCpJ5Wica0IXSf-leHUkvytreWC3NBOVyN84d2aKu-nX-t3UDxenJRHbQzFq47smaUNoaYw7JCZBX9nEoMyJmC6huGzSijVxuP3mUC-kVeRteXjUD0bQl8sPB2yUC2IiAy9cId6MHMbA1IuFvaIouUaHoFD_N46JaGI_2TJgE2UWMW2VRLeVn_5tXWY9EUcXgKZiAJTLFVHJ2YEtGXkCBprooKo-IIf9makhuhIMdBuRak2y30PCOj8lycpV4DVJqd1jN6NN9r8gUk9uSLrNVqd8WisfDtpelVOAC_u-LUtf6HT_IpeX-WX5Fuz1HlQd7FZytPE7cT0YOpYZ_oT0c73AlHJ1j68rEE3SPSiuDTZBrinYyjtUj6WC_fJgoAgGJUNB8Q07osCbhHmO8G3yfVIhTnHhSIaiT_OW36olmIeYxlbJon5q4SAicNAPlDV9M_fVj-3nNuYNhuOZdXYn892NT22CWyPAdceOKwhe4FRXq4wsCuu_Yn03JbGi4_D5NvPd-le9FB99kJuavlYK0QbR2g1eyLPNIlUSZv3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK65WyLGz31ksfga6RsfdvDymhu4eNxJ2nfKW2kbCJQyZ5oCFAUVykm9csG_FWYNWzu6HR8eJhFkv6TKa9Q-l3aS1uNh642XuEwhrVBzj62vr-SZb1HLnHMYm76biAlUZh342tWvOl8SbKiGas3rV1sdDMJtvSFsFcPq4GgsPx7j3_v-WM-6c1Q-P935fyVqxNRF25Qd5-KxdgPq05p8sQSfMnKZPfZktjvbTDOURopO0HbMVR-4gMxLa7wxfaUI2K9HVNNVhRq0I6CFaueaCMJYzfDMs5c5ezh1v0CWZAfLuGJhWaoSHU2xg1PLlPft9bw0YKHC4c58Oy3ZQShNQA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JrrpwgXatTXgBPqnBndVpXFQXhCiJo65HOF_YMqBRvviiNtfUVCCDKaCXo2hBoHaJNJfzak1wImTrAHb3jU9GKtoiWQ_yFkkh6utnEtZ0fHXqT5V4gT36jCzMpZMujV689WhUGlSpIJM7p2K76NNeZOT5OGEERaBJVnZOMM40byfi0pjQ-v9MvJIMwGnkITBVOMmXtLmf4VvBgc9Re0cDTparin0HmEInWRR4BYSSrjDt0_xCvou4ZLLrs9ULrIGyvJ8_QkPFGN5qik8lknZ_AHsyyk55mCU-GRF8hY2PKqtMhD1MuAllxHUvi6gKOGAOAdvlIpLPKNp5Aju5eammA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JrrpwgXatTXgBPqnBndVpXFQXhCiJo65HOF_YMqBRvviiNtfUVCCDKaCXo2hBoHaJNJfzak1wImTrAHb3jU9GKtoiWQ_yFkkh6utnEtZ0fHXqT5V4gT36jCzMpZMujV689WhUGlSpIJM7p2K76NNeZOT5OGEERaBJVnZOMM40byfi0pjQ-v9MvJIMwGnkITBVOMmXtLmf4VvBgc9Re0cDTparin0HmEInWRR4BYSSrjDt0_xCvou4ZLLrs9ULrIGyvJ8_QkPFGN5qik8lknZ_AHsyyk55mCU-GRF8hY2PKqtMhD1MuAllxHUvi6gKOGAOAdvlIpLPKNp5Aju5eammA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJhQQDhHDMg986lWt9nRNn0xmKXMfSWJuSVhESz0dDuT6cycLO0obJfxuYTw3djFTEcTY8Kg6zBK6a7EcvAhPZa7n1mFTlP0a6rmfPXWyuSeBFmHvwrbYpH-99xWGbDELR2OVG8zZtaEDlWr8pRtNKr861qHuDjIi6M_H59mNRqlh-SWCvsuc8KJ-PJWlHLK5duWjvglGuym1KYPApVuT-5vyRIQ2bv7Cb7HSsz5Igc1HE88r6fmJw8jj5EXf2Tx7RjTzr8abCw8pet1MG_yjxMLdoqQp41WxE_jLtkq2kd5D1UzsinxNdSHeHLeOHe57Ywa3jk3xo06EgiaUHXS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf1Kl70scUK6uN1v_K1aPvAGdcVZQJkNBqKnE9z6CLMTKmKyfXjrm7vQp2feMsYtb1Pfo3xUD4TONx26poKWbGd312uyrfN7gbF67XMS3JHQgTtiiEseG5kQgt-HFFIXfsdNEVudqgjU-qsSME504KKSdgv3X_2DqYaEeuPZW9nYL2xoRazRJC3vDxJW22Q73wJU6LXrnU76qhOmOPDPeerTIorBvSa-tKeIV8aj9T6kpXkHoQM39FNKFaGW3TWVgq5TBwPWCqWkHBR6Dzm7G3XlYV78H-oW8nn_ScVEzZ1Gg7xv3sQ1vhHNSYD7z3Y9UWd_wmGuh9XB3Dzl1M0_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ormgQt1WwwqBChtbF5czFMY-HUT7RNGx6oBUvvHwnWKqpb9lIf0Y5duKoEvqLbc0-xtnRuJUrpNs4vd58DoFcw70wSPdDQaCDX0FGYGpWwZ4InbY4GAaqcKIaFd9atXzBY6WghuN4eR14ForJriu3o1z1RYRuHrlFMhx9L9lzq-UZcf0PcxnxhUZaCOiFE6_ciAjIe69AAaBTn8pLvingkBkKeBrT1aEJTnm4t3wMfaMpyItQbIQXM1n3VedvmDk4C57DkudcrbWPKg0jsU_dkWBSk8ZwWTPnS3t8s7bFjQff6SCeVDshhH3gI3F28EOb31UMKOIzNEgCddtZVh7mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=vo3HxahNYfclaxtiUftt-vRL9B0E2XaakX4nDJi4kglgG8AFgBWheBmj9tQUO4njDnm9Izw3fg0e4ksHAH4qhlNT5_l9VJdrQBPV1vc3UrdHQA2KRhuGWS7sOe2CdyO4ynoIgVOZM4wIOZB_2siD44BW-efdjj0qTQx_SP_8lxogWxx__zjDGLp_cSp6VbYndPEtkcJOUeEiv1zx6j4W5MxmSvOmiQodIrcSOknA1itWw5AciGJXE8BUJ5rwRRp75qUXR9S56-g0yJog84_w-GIPzkkqHcSHMN7SH9s2db5LTJObvbV9fFvMaPRbFOFWVaBnZFO6xQ0_A3rZrS_oNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=vo3HxahNYfclaxtiUftt-vRL9B0E2XaakX4nDJi4kglgG8AFgBWheBmj9tQUO4njDnm9Izw3fg0e4ksHAH4qhlNT5_l9VJdrQBPV1vc3UrdHQA2KRhuGWS7sOe2CdyO4ynoIgVOZM4wIOZB_2siD44BW-efdjj0qTQx_SP_8lxogWxx__zjDGLp_cSp6VbYndPEtkcJOUeEiv1zx6j4W5MxmSvOmiQodIrcSOknA1itWw5AciGJXE8BUJ5rwRRp75qUXR9S56-g0yJog84_w-GIPzkkqHcSHMN7SH9s2db5LTJObvbV9fFvMaPRbFOFWVaBnZFO6xQ0_A3rZrS_oNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y116F5w-C4b2XfUjMF0QwmmyXu_j13zTM6MpZG5ojFkxOEybUqLaVgGUyMKsimp7oCBYSon_AevLOJtSqWXM8N81as2UQuCQjVkRhkANHDba33hPrQp-m8br4tOwi82CPb6GS0SztpiitVgonoC8Jc3XEi-loxLOcnkruYjIiH04gZzRDQhXqFfesb2QMrIAtuGygMJ8Kphb0qCSiU_xKkYAZ9QP94IXBwMQ0b8fGRTjDTUZaNVMGplgLGaiJIhmNZDcFi4g4nbnErZVXJmHcGIbft0uxcv9HYMbTY55MBaq4eEw0uM8S4jusxoe5Zd5RxDPWs1fJULFGqtt3MsW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFCihsO779ZRhtbBU5sDwPo350it4172fcN_Sso-wKnlxOhRhOaZm4ZjIHF3rJps7MTrj4aoefqaeXGQKHM-bv1rVGiX_g6YlZBduNlhm-6oQTK0lcRquWamadggVrAzg1EvmO7sqyc0tSvQ-ZtWYTH_pik84lZpy8vj_T5Th5P9PiQO97lp19nlC_PG8CcxAcrePCOXz_N-41y74ZGMyXhrnoyt7poNJtunYK13v5cpIrXGUzAeQ0_QH5oIrv0grVLifqmjnptS_o5Lx2cD0TAcgaWAhv8RE7LSDptyzloLusU6KDdz-lB7f8eLvPUeq93IziJb11CwLplBQ14h8sUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFCihsO779ZRhtbBU5sDwPo350it4172fcN_Sso-wKnlxOhRhOaZm4ZjIHF3rJps7MTrj4aoefqaeXGQKHM-bv1rVGiX_g6YlZBduNlhm-6oQTK0lcRquWamadggVrAzg1EvmO7sqyc0tSvQ-ZtWYTH_pik84lZpy8vj_T5Th5P9PiQO97lp19nlC_PG8CcxAcrePCOXz_N-41y74ZGMyXhrnoyt7poNJtunYK13v5cpIrXGUzAeQ0_QH5oIrv0grVLifqmjnptS_o5Lx2cD0TAcgaWAhv8RE7LSDptyzloLusU6KDdz-lB7f8eLvPUeq93IziJb11CwLplBQ14h8sUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=id8iQ7Hr3e2xMFozm2a182BcIZrxtc4_U73G158nQhyBC0JxjaGXbpLQY31LGomgenYCPQhL3LKoKXGSqfR3IsRLbIYRPhdbmEKJnwbP_qbU7QjaNoQxZ0zLwy8ukvbZneXrDeODLSvUgXT1OS5CnIwYsl6d8JEAyUlqW-EvWnnCbWdbj84ZIOO9sQb3dFm7iYXaV-RJP4IcxuxdBWLubbwaY5lCtYZYW_FDLf97Rwh67zDCji5O1RSVO_ZZ5cpS82J6ndblwgMOpipGmHko9XWVen7CbsmOG6ajkQRoQnxsyOVsoSFKj-7jI4y1nNmLt5ciDmRiXkCQ1QijQ3Qmnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=id8iQ7Hr3e2xMFozm2a182BcIZrxtc4_U73G158nQhyBC0JxjaGXbpLQY31LGomgenYCPQhL3LKoKXGSqfR3IsRLbIYRPhdbmEKJnwbP_qbU7QjaNoQxZ0zLwy8ukvbZneXrDeODLSvUgXT1OS5CnIwYsl6d8JEAyUlqW-EvWnnCbWdbj84ZIOO9sQb3dFm7iYXaV-RJP4IcxuxdBWLubbwaY5lCtYZYW_FDLf97Rwh67zDCji5O1RSVO_ZZ5cpS82J6ndblwgMOpipGmHko9XWVen7CbsmOG6ajkQRoQnxsyOVsoSFKj-7jI4y1nNmLt5ciDmRiXkCQ1QijQ3Qmnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=iU9eKTX9JOsiqE1v_SUIDYEvLprTwfoIf4RJc9e17IyDhe70xXrKozPPl9c7n-GC22zrMsLFQdOcIQU0u6JQZtrL6HdxFs2c6djomAK58IatMnEq4Zi1Q1Q1ZaVFC058cFbKoKe94iumQBcbgMcYX4p0DVTinfMIUgayg_AAUhXQAvMQ_jX6PyJtT-99A_vm7knHRLU3t2X6QuiMXIn4gC_fvBXOAJCS0JwauUHUILo0SmjgNMGNephHTLodsF5cTPd3sgUzIzRzCGIOH3-0PqsV_sHHh7IIlI3PVdT3CmS6mrF9sLMFJLy0u7PI3pkF_5WIlzJaYBlaqgqiiNzLGDa7r3CUsR-405MddU6r3AaDXluAPEa2Y_B_8m9uMB-muDGx4M2MxzTyYEqTNYGSvfNqfbh3Zrd6401eKNLWF1JbtpPVVgaBJT10xC-l_hE7g-tt9sYXDpkXiTG9HYXZl2pqljwb1dqdLgNIlh64BHl8NxbIR31tMRVQhJt7imuKJsydzCX9jU8M_fBTG2JOBQK0liq50G0WeqDjtwWAYkoXfbk2q3KiS6qZZ0YCT1PlZJynJVK9-H9Gq-1Mi6lA-3_02pmqfzr0WqybN7PB07fFH9BwNoBNPIZ57Le5ruj1UpNVeCnAMuISJynronLXifSYMZLOcb0TTPwbRc1M2Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=iU9eKTX9JOsiqE1v_SUIDYEvLprTwfoIf4RJc9e17IyDhe70xXrKozPPl9c7n-GC22zrMsLFQdOcIQU0u6JQZtrL6HdxFs2c6djomAK58IatMnEq4Zi1Q1Q1ZaVFC058cFbKoKe94iumQBcbgMcYX4p0DVTinfMIUgayg_AAUhXQAvMQ_jX6PyJtT-99A_vm7knHRLU3t2X6QuiMXIn4gC_fvBXOAJCS0JwauUHUILo0SmjgNMGNephHTLodsF5cTPd3sgUzIzRzCGIOH3-0PqsV_sHHh7IIlI3PVdT3CmS6mrF9sLMFJLy0u7PI3pkF_5WIlzJaYBlaqgqiiNzLGDa7r3CUsR-405MddU6r3AaDXluAPEa2Y_B_8m9uMB-muDGx4M2MxzTyYEqTNYGSvfNqfbh3Zrd6401eKNLWF1JbtpPVVgaBJT10xC-l_hE7g-tt9sYXDpkXiTG9HYXZl2pqljwb1dqdLgNIlh64BHl8NxbIR31tMRVQhJt7imuKJsydzCX9jU8M_fBTG2JOBQK0liq50G0WeqDjtwWAYkoXfbk2q3KiS6qZZ0YCT1PlZJynJVK9-H9Gq-1Mi6lA-3_02pmqfzr0WqybN7PB07fFH9BwNoBNPIZ57Le5ruj1UpNVeCnAMuISJynronLXifSYMZLOcb0TTPwbRc1M2Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=O_9DyHJsZ90wP-nArzVUg74xIRyBaW4xPafAygF9G5lFlp95E9FzjVGTzIuUbRwMIBb95S2BTnqiE1CBxY5N7zBBlZW7cUWnKUi6cF_9LgCI9G2YL-1neWzkcD0xAPDevLbFISI_PV74b9ujpD4XEn4P7ku7dcYQ8yje3LvYRwD4cLYj7aFvPcVqqFmOIFGQHd1HrVj7kgC1XvLnpcTugl41bnBURi0XJr71MOk4HiMY5h9f4fjNqyDXskwkQwycDOh-zxdLAarAIufzLTIWjcNREewg3LVclzByIPs4WUSn2InyGR0bQDcw9_pz6mB_pa6lsb-RJUHiQfsJ-mTHNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=O_9DyHJsZ90wP-nArzVUg74xIRyBaW4xPafAygF9G5lFlp95E9FzjVGTzIuUbRwMIBb95S2BTnqiE1CBxY5N7zBBlZW7cUWnKUi6cF_9LgCI9G2YL-1neWzkcD0xAPDevLbFISI_PV74b9ujpD4XEn4P7ku7dcYQ8yje3LvYRwD4cLYj7aFvPcVqqFmOIFGQHd1HrVj7kgC1XvLnpcTugl41bnBURi0XJr71MOk4HiMY5h9f4fjNqyDXskwkQwycDOh-zxdLAarAIufzLTIWjcNREewg3LVclzByIPs4WUSn2InyGR0bQDcw9_pz6mB_pa6lsb-RJUHiQfsJ-mTHNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOmBEWlaUmawWQwM8N4YHDzMLJ9KRoANCNtHQrgz6C9yjCuBUuT8fjUDrtKAzVnMa33HVD9VUMGTBUbWiPENyMLBl9a2AYSsFAqTXDjvi-XRTyvOH1DZ6q63brYRAA75HFZyb3ukNWgxuW7n44Q3v8NbgMCj8WBitr1E7jvX3K2N06tyD8i42e-_3wYgll5b3GvMbnvetDMlEh8u2MSP_Xqe-oRCwc-LDJpOV9LmnUU9bEeSJnEvGO08zhhbSteXHvMfaNuid5n_rZihP6f3g0jSMwuDJ44Lg021Zdj4mhttIZhuEgaPGabrh04EOp5BtuJxpHZvXwEjfOJX2XU4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=trK3_tp2YPU8UpWKVmlbVTbLsd4ZOXm2UisQ8-1fzLmUV2oj-AYJPHKBJYOuZASV2n_cXubYq2QrcHle1eruq2GtRlSePYgk7SPeS_FmqSR9ix-bb_csR4dJ0vDcJsYZ_iffyNF7ynuXXInM3fAtnR_auq-Rnxc-GCqFoRAJxiF6OHA-EKCdF2l4wcKaytHce4vmyS8GVL_pGa8ZjNRanI1h5oBQAF5qpMUi9XK1EzQVqpMAL7704u25q-iecsB4BqgGKCElxd_5iAVSqkiP8pfAWtcshWP13AzFWIzPuoudjt59a9DGEl69w2te_bI8yPXjapp-P_Y2LdZdvsXnQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=trK3_tp2YPU8UpWKVmlbVTbLsd4ZOXm2UisQ8-1fzLmUV2oj-AYJPHKBJYOuZASV2n_cXubYq2QrcHle1eruq2GtRlSePYgk7SPeS_FmqSR9ix-bb_csR4dJ0vDcJsYZ_iffyNF7ynuXXInM3fAtnR_auq-Rnxc-GCqFoRAJxiF6OHA-EKCdF2l4wcKaytHce4vmyS8GVL_pGa8ZjNRanI1h5oBQAF5qpMUi9XK1EzQVqpMAL7704u25q-iecsB4BqgGKCElxd_5iAVSqkiP8pfAWtcshWP13AzFWIzPuoudjt59a9DGEl69w2te_bI8yPXjapp-P_Y2LdZdvsXnQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=kzHdnOPaTXZsSqPZQg1yXDPqP0fz49ymYJ2vWKG-6cNqnWU2RBTHOFZ8A5ONgjRnzwh3d97irEoC3WzixfrG5pYzy_k2I3HizOXtUM2LNmDFmaeIgY_LAzTveIxFRD-6Vz8gOANME6tRRXr3MOoDAW7OihjjfK0fd-w9iQEmEqoriJ9_BeOCBbtipS-MKhJNK0m6Hs6ae6wzHbPPv4kl6-odirUHKlV3GSI1_-9ix_1NKU3qdTkM2zcsUv51Ci7XSQkc5aKJI-hoE_zDS1i3122g5_V5AMBnEnwqhJ5O9ZPgigxpzTcV8B1EI6h0WsXXDPETybyHSh4hmB73v8l45rK7XyW_nmk9SGPc19rX30GLI3I5dUS-Mv5vIwiEJBIPFRHqs_oQmTU6JDqdB5mFKc4ri6EUcdEJk0Fet-ql4UOhMfmVDVrhdnOUfHyYuYdt5x5PqZ3IXLJuSVesZcABbSdgpp-gYFuF2N3KWwywEBUVupmX68PHOMjX6JEm-TMlQioU-uEGBQnXNB-NKhc4u0zUg8yLa-fTI04eKTfnF57cAAQpewpMAqFlB9N17bruN5Z9SUHFqhCH3rA1g-FeJV-HVtsl4pyaJdaTVXdqF3G0CY9Sf1w3nBu_Ft7QLXI5nvSEpEKNkGNTtyooMZk_IFsHU9KWfZ7JVXXtp1t5cio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=kzHdnOPaTXZsSqPZQg1yXDPqP0fz49ymYJ2vWKG-6cNqnWU2RBTHOFZ8A5ONgjRnzwh3d97irEoC3WzixfrG5pYzy_k2I3HizOXtUM2LNmDFmaeIgY_LAzTveIxFRD-6Vz8gOANME6tRRXr3MOoDAW7OihjjfK0fd-w9iQEmEqoriJ9_BeOCBbtipS-MKhJNK0m6Hs6ae6wzHbPPv4kl6-odirUHKlV3GSI1_-9ix_1NKU3qdTkM2zcsUv51Ci7XSQkc5aKJI-hoE_zDS1i3122g5_V5AMBnEnwqhJ5O9ZPgigxpzTcV8B1EI6h0WsXXDPETybyHSh4hmB73v8l45rK7XyW_nmk9SGPc19rX30GLI3I5dUS-Mv5vIwiEJBIPFRHqs_oQmTU6JDqdB5mFKc4ri6EUcdEJk0Fet-ql4UOhMfmVDVrhdnOUfHyYuYdt5x5PqZ3IXLJuSVesZcABbSdgpp-gYFuF2N3KWwywEBUVupmX68PHOMjX6JEm-TMlQioU-uEGBQnXNB-NKhc4u0zUg8yLa-fTI04eKTfnF57cAAQpewpMAqFlB9N17bruN5Z9SUHFqhCH3rA1g-FeJV-HVtsl4pyaJdaTVXdqF3G0CY9Sf1w3nBu_Ft7QLXI5nvSEpEKNkGNTtyooMZk_IFsHU9KWfZ7JVXXtp1t5cio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOwgvNxrtc05b0zuVI6gBWDXVuOb_q2ZPrVVDfTQxkTpFLKesxxj2mv6twZ00aXgXgA3zM_7Dpch6Rmnu8-0HwnHqEDpsvh2dIJKtDQNFvtYDgV2UT-rV8VSall8W1FHQWiIpJTFDkNzBb-Yd1grDGOmnbT_XvzXoRSfGvEJD1iJalm0uaJwJiSHe5rfBFfzcsbXnL2HPkks44nwewkZnHLo6t2rfNUtnmTWCNrv84MWu8s3H0sYySjctxetT1M2-AOS6v05ziCSEzA3sVFAr6ML25M6OeJ6daBwDE6Z5p6O34-gUeCHjSG_KoMcOTH8t-E0IV2HAVfiKGOfYpDqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=YMd8gOoCSkYOHUMy3Ta9sKO7KccgiuftE7GeZFeD_gEDkzaXHEcivwdvXsS7XTlKIwxPXle8soPq1208FOkoBTh0GChC4FU8RG0ExkXaq_S4iQhA9hHAvJeLW16Z0YnaAyXV6-J9dWoNY9rbNk_mUWC841mTUtfR_1BItEUtdSPQsrXMmS4XcBhVQ7kksvec8OLPZJsdFm2ccHB80gbBpfI_C7oN9HAIbz7IoiIkmmotQsQ1a9mYjHAgNdq67L1FuPzNQk1cf8l1HJhSdsQHH6OgqoSXL6JsG_6XOzvvOr1CJqlrIJ0wmzzTWCcLyfZudOfL991lT4RG1VDeusAv-bMfx3ad2sU_ZScEH7pgZmc_SyPuM-MFxjNsx22BnQgEJ0H3hCe5p-OI1hH1e8s2XuN02cT58iSQbkkRtnHC6348jsJs4L7t-EgkKhdtbEAaTy1D3PqmHaQB6bhEVoos1rk33oRSF9btOfh7ZtigYcgmgjX2ePx8etLr9eSC_wJ0aolo2JU1DuzcQhJbw62gWiX9pM-CFaP9TnD2FLvqYDetP4vGi96JpqY2LOZX4IZHwkixdm7d0EG3IymNQSBmIG7cuApwdkOzxX01G4vavEPSlLccBQWzMSFwYOh7cJ5dAltKh19C8PAtUih6JaKyLZnHg35strpwKR71SKiAWgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=YMd8gOoCSkYOHUMy3Ta9sKO7KccgiuftE7GeZFeD_gEDkzaXHEcivwdvXsS7XTlKIwxPXle8soPq1208FOkoBTh0GChC4FU8RG0ExkXaq_S4iQhA9hHAvJeLW16Z0YnaAyXV6-J9dWoNY9rbNk_mUWC841mTUtfR_1BItEUtdSPQsrXMmS4XcBhVQ7kksvec8OLPZJsdFm2ccHB80gbBpfI_C7oN9HAIbz7IoiIkmmotQsQ1a9mYjHAgNdq67L1FuPzNQk1cf8l1HJhSdsQHH6OgqoSXL6JsG_6XOzvvOr1CJqlrIJ0wmzzTWCcLyfZudOfL991lT4RG1VDeusAv-bMfx3ad2sU_ZScEH7pgZmc_SyPuM-MFxjNsx22BnQgEJ0H3hCe5p-OI1hH1e8s2XuN02cT58iSQbkkRtnHC6348jsJs4L7t-EgkKhdtbEAaTy1D3PqmHaQB6bhEVoos1rk33oRSF9btOfh7ZtigYcgmgjX2ePx8etLr9eSC_wJ0aolo2JU1DuzcQhJbw62gWiX9pM-CFaP9TnD2FLvqYDetP4vGi96JpqY2LOZX4IZHwkixdm7d0EG3IymNQSBmIG7cuApwdkOzxX01G4vavEPSlLccBQWzMSFwYOh7cJ5dAltKh19C8PAtUih6JaKyLZnHg35strpwKR71SKiAWgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=jwMxCe0GVWkB46eZcb1-x8_VBD830n78PfhnkK_6G-f7Cs-6g0xXpH1QeTLIXgNcjeHe3UHBigPDQsfBv5Ccf41x5a87sewMq_pW3jYbef44gE38bEuruS1XxwSH8JRnhLvfGKSEqVJJMdhudylAqXK_Bj_9HSwj_mLIQiZngtqdBthmBid8DY9Staayyp_5cLSFdNFq0XAWLY1Tae33d_QtoEeaI1fTpeO2H1OQsQNl0G8L4J_BpMWalhg3lW2kZrXs5vY1lCg7lMwYYSme7gK1Pq_UMCbaqJvA2dZUOU58Lvu0vqPl9Nlzv9LoRgsNlxXdST5fMRgaAN2cEbMc5qszHj3NWlCVwAQZiSVwajCKqVA3zSa_-WUFz6ar8-3pCr9TxVt1cB0ACrnMM6uTbmfDG91h0lBA8VWcPMT6xd5ZPEebILnKI6sinoYY57X1KKHvY9KVqE2WICAcg66QEIKC-tYlH1ctRzx0cHexezghLkfhficMn8mepS6nZNhZM0e68T9vhm4kD0n8mcqH7MrXayLYOSKK9kSELU8jCAiP0qPvqJPAVI_rWt0Is6f1blGiJ-I9xyt0bS7RxusL6gmu9u4Q1LK4d6lbwR_90jbVPWxpo2eTY7TELuhnkErAyY5R_tskGxbKr4x2iARdRSUMz9ZZROIRdUb7kKv2-xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=jwMxCe0GVWkB46eZcb1-x8_VBD830n78PfhnkK_6G-f7Cs-6g0xXpH1QeTLIXgNcjeHe3UHBigPDQsfBv5Ccf41x5a87sewMq_pW3jYbef44gE38bEuruS1XxwSH8JRnhLvfGKSEqVJJMdhudylAqXK_Bj_9HSwj_mLIQiZngtqdBthmBid8DY9Staayyp_5cLSFdNFq0XAWLY1Tae33d_QtoEeaI1fTpeO2H1OQsQNl0G8L4J_BpMWalhg3lW2kZrXs5vY1lCg7lMwYYSme7gK1Pq_UMCbaqJvA2dZUOU58Lvu0vqPl9Nlzv9LoRgsNlxXdST5fMRgaAN2cEbMc5qszHj3NWlCVwAQZiSVwajCKqVA3zSa_-WUFz6ar8-3pCr9TxVt1cB0ACrnMM6uTbmfDG91h0lBA8VWcPMT6xd5ZPEebILnKI6sinoYY57X1KKHvY9KVqE2WICAcg66QEIKC-tYlH1ctRzx0cHexezghLkfhficMn8mepS6nZNhZM0e68T9vhm4kD0n8mcqH7MrXayLYOSKK9kSELU8jCAiP0qPvqJPAVI_rWt0Is6f1blGiJ-I9xyt0bS7RxusL6gmu9u4Q1LK4d6lbwR_90jbVPWxpo2eTY7TELuhnkErAyY5R_tskGxbKr4x2iARdRSUMz9ZZROIRdUb7kKv2-xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=cAwyHtRhfM0n0067xz8w9hGVv8EMzxTtdCvwHoapV6Bp1ORbANDYVvUd4247Usgt9S74pcLAxqDmHCCESqnGpJinzFXq8ep8O7mJ3fgTKmKUiaKHIezIkrdnBjHCKL6WlIKZ1BoYI5m2cfVkM0zlZhd_ipgMP4Zg71pVOERDSIim87Vbp7pqilZ_SkZ9fOgcm9AZGdzFpReI6BLHAkeqDQIZOXLVR520sM1rig2brLI7DLAKYPPsEDSu4dL4GLYDjcErpxalRYhJSyzCIMuCXkz_gd7MZ8eQ-wJlE7boGruIEQOpK5RXASBC5QjES2KRwZD6YZn7sl7ZPk5EpZDtTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=cAwyHtRhfM0n0067xz8w9hGVv8EMzxTtdCvwHoapV6Bp1ORbANDYVvUd4247Usgt9S74pcLAxqDmHCCESqnGpJinzFXq8ep8O7mJ3fgTKmKUiaKHIezIkrdnBjHCKL6WlIKZ1BoYI5m2cfVkM0zlZhd_ipgMP4Zg71pVOERDSIim87Vbp7pqilZ_SkZ9fOgcm9AZGdzFpReI6BLHAkeqDQIZOXLVR520sM1rig2brLI7DLAKYPPsEDSu4dL4GLYDjcErpxalRYhJSyzCIMuCXkz_gd7MZ8eQ-wJlE7boGruIEQOpK5RXASBC5QjES2KRwZD6YZn7sl7ZPk5EpZDtTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=IoKLxbMxzh_yYDP-Mg6fcbcXHr3ymejtQHtg_ebIlJGNV7rX7qEi8OyLPKREclow5h06zaTHrs3_jpiiqRvHZXDh4FGDzQoK6X0ICt6BqlBJJFye3SlJZbvj_iptu_r6ZZZZFF49WDrh3zTZ_06-tDthggnBFP4zdKZKUKvuAT3cubsdA-jlkb12f257SW0m9r5Vs7idH_SlDqPezYzR0lMMrkcshTQ0X2y_oAVpxPjMeZVbp30KjdfmQctMDTTKbZiVgOMfkj5sLZMat8TSH42MOU-S4nEnBEqFS7ahcq2F5lk2AZyco1Tgd6Wbgpo5uHFhvUuHiWxqtfPIFZDDgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=IoKLxbMxzh_yYDP-Mg6fcbcXHr3ymejtQHtg_ebIlJGNV7rX7qEi8OyLPKREclow5h06zaTHrs3_jpiiqRvHZXDh4FGDzQoK6X0ICt6BqlBJJFye3SlJZbvj_iptu_r6ZZZZFF49WDrh3zTZ_06-tDthggnBFP4zdKZKUKvuAT3cubsdA-jlkb12f257SW0m9r5Vs7idH_SlDqPezYzR0lMMrkcshTQ0X2y_oAVpxPjMeZVbp30KjdfmQctMDTTKbZiVgOMfkj5sLZMat8TSH42MOU-S4nEnBEqFS7ahcq2F5lk2AZyco1Tgd6Wbgpo5uHFhvUuHiWxqtfPIFZDDgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=LjQJ4PQr82FsBfaNjoCISs5TTDZJrLrjgU9sJTCWyGp2Hk4TxinyYLqgh6l_3Mgt32aQL4jfIV93WeLNpXosELzWSwYZsNkDbZH8deHmbjC0bNBJHm7fQUBRSkr6RFcPagFwWk1Oek9g_hfASb3hb_BOw0Xkkf-6y6AKbrSKllx6_ZmQrJMm-FLdE1TjKC6s3gl38Mx9dH1AIpM5Sy4bD4HJBEt50fBiUDZaUO9dfuK7R_pBKAwjZ-qIAEiDeer8AEb4upYiJI-H9TxopsRnmvRlmvvEzldefl4z2aP4Tz-fJ2fz-xGc3qtbSeM9vh5Jb1-ez2kU38JDtIBiFM-KlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=LjQJ4PQr82FsBfaNjoCISs5TTDZJrLrjgU9sJTCWyGp2Hk4TxinyYLqgh6l_3Mgt32aQL4jfIV93WeLNpXosELzWSwYZsNkDbZH8deHmbjC0bNBJHm7fQUBRSkr6RFcPagFwWk1Oek9g_hfASb3hb_BOw0Xkkf-6y6AKbrSKllx6_ZmQrJMm-FLdE1TjKC6s3gl38Mx9dH1AIpM5Sy4bD4HJBEt50fBiUDZaUO9dfuK7R_pBKAwjZ-qIAEiDeer8AEb4upYiJI-H9TxopsRnmvRlmvvEzldefl4z2aP4Tz-fJ2fz-xGc3qtbSeM9vh5Jb1-ez2kU38JDtIBiFM-KlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=qzfmhhbWd4hXImd-hFAHgfG4_D5fV7E5EQ3AUt8koYgPu7Hk12NRZyY0_vGcAwri_iHmqs2wq_3xMVu0Vj2g1vZ32jRtPxgza74uS9ehjubTa8xqmGuDzMhXciXPahy-SWDdmRDSUgJJZJZEivayW9sFlZ51bzbPvP3Ml9YON5E7Q0cJ6RePMjl4OW53v19U0moWWNEZcDuGPoY4t9qnGj73Mx2_jWL8hDXIxX0uMWWHm25qKo65-O78afbK1RgWueIBJsHb9bWngIL-hezkj9XirVtmL_stOLS-uEcFY9kJaniHUuk65tI-zOZALro7Fw6ntJ2dqwL2j6exYAcZkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=qzfmhhbWd4hXImd-hFAHgfG4_D5fV7E5EQ3AUt8koYgPu7Hk12NRZyY0_vGcAwri_iHmqs2wq_3xMVu0Vj2g1vZ32jRtPxgza74uS9ehjubTa8xqmGuDzMhXciXPahy-SWDdmRDSUgJJZJZEivayW9sFlZ51bzbPvP3Ml9YON5E7Q0cJ6RePMjl4OW53v19U0moWWNEZcDuGPoY4t9qnGj73Mx2_jWL8hDXIxX0uMWWHm25qKo65-O78afbK1RgWueIBJsHb9bWngIL-hezkj9XirVtmL_stOLS-uEcFY9kJaniHUuk65tI-zOZALro7Fw6ntJ2dqwL2j6exYAcZkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=OKiHRKBVeFDTA4_IhUTmQaJz2uZFNBFQgqW34Ir6ZXyUgIBHC-gDFEyT8vYPIlZfrFq2MnAEmRYatUEJBvi34KGeUBqURplp_ioArGao9Cf_YbGuVNXO0kf65GB7_6W9QD-79xByo8ZMCqWptJ4MlzhQO2WX4Z5yDsH9Pm6TQdc2_YHfKfm1UMyacIK5-9MrRJSzHEpC49KzsfSDKAyLwsyavu-QcGPLAeSf8W3gW33w8RSz-rKvUUjGDJDv08kPHIJmdyTKP3jhx2cDugDsr0ae6sNN6Xuv9GQCbRUzzAzqhdnZG2oQH__TtcndF8b4Y64kG1RedYF6JNrqLL5a_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=OKiHRKBVeFDTA4_IhUTmQaJz2uZFNBFQgqW34Ir6ZXyUgIBHC-gDFEyT8vYPIlZfrFq2MnAEmRYatUEJBvi34KGeUBqURplp_ioArGao9Cf_YbGuVNXO0kf65GB7_6W9QD-79xByo8ZMCqWptJ4MlzhQO2WX4Z5yDsH9Pm6TQdc2_YHfKfm1UMyacIK5-9MrRJSzHEpC49KzsfSDKAyLwsyavu-QcGPLAeSf8W3gW33w8RSz-rKvUUjGDJDv08kPHIJmdyTKP3jhx2cDugDsr0ae6sNN6Xuv9GQCbRUzzAzqhdnZG2oQH__TtcndF8b4Y64kG1RedYF6JNrqLL5a_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=G_cRhWts9Es2U2f6uUIYhmAOlZWWhiHvj3MruanYNMOThHIGh4nnivR539J84W5TY06URUV1hE2jzrPfXsLyGnNHQSRXoxUA4drGml00fOqHwoiKbATt1kswr-cvq82fjyiqRr_jj9fTLm41r6HUABFTEqk5TyFTlxmApeb8smQeaau8yOhEWKIeHq2OHeXi9cPh5hhGl9TA3nSusIAmfBW2QIJCy8ArPm1Rl23Ie2s8ufdVze3EsnrgmS6XvxJAVvoiomdPjoum-RnZNIVh_qUgu6ryhI_s6eWMUYDFu1TjdgWIygeLVGt8_QMKupOph7ph0-gVEivN90UWrTolFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=G_cRhWts9Es2U2f6uUIYhmAOlZWWhiHvj3MruanYNMOThHIGh4nnivR539J84W5TY06URUV1hE2jzrPfXsLyGnNHQSRXoxUA4drGml00fOqHwoiKbATt1kswr-cvq82fjyiqRr_jj9fTLm41r6HUABFTEqk5TyFTlxmApeb8smQeaau8yOhEWKIeHq2OHeXi9cPh5hhGl9TA3nSusIAmfBW2QIJCy8ArPm1Rl23Ie2s8ufdVze3EsnrgmS6XvxJAVvoiomdPjoum-RnZNIVh_qUgu6ryhI_s6eWMUYDFu1TjdgWIygeLVGt8_QMKupOph7ph0-gVEivN90UWrTolFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=vkzv86eptHAXPv8ms3s377wHiCGe--q6NxIZjyH_OceQc96T4dMwwueLeJjTPNrtr481Ru_aaUr1DIBLu6J6WWlRndse43OMh-wkiWizZyI0CiATrsKFifbnvrU7QGGB6CC67NAR2Tjgo6qBaP6sfvzx1uyX19oHK8d60_5AXKGuAGDalljewQgKy9TqaRCo80Llbe2uMkGUX8ygU6f4WIRwR7q3h1bHl7rnv-p6g4gVX-2J1QBWNtfy_4u4jABNvZS6z_JoF7dU-PCvsj3-YlPIC-7LsObW-ETjIuUzmGEbh3UZNpPNI2Z2NPK-gMuFIEueK61pwiR5CG-fUFqF8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=vkzv86eptHAXPv8ms3s377wHiCGe--q6NxIZjyH_OceQc96T4dMwwueLeJjTPNrtr481Ru_aaUr1DIBLu6J6WWlRndse43OMh-wkiWizZyI0CiATrsKFifbnvrU7QGGB6CC67NAR2Tjgo6qBaP6sfvzx1uyX19oHK8d60_5AXKGuAGDalljewQgKy9TqaRCo80Llbe2uMkGUX8ygU6f4WIRwR7q3h1bHl7rnv-p6g4gVX-2J1QBWNtfy_4u4jABNvZS6z_JoF7dU-PCvsj3-YlPIC-7LsObW-ETjIuUzmGEbh3UZNpPNI2Z2NPK-gMuFIEueK61pwiR5CG-fUFqF8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUc3HaJyOqqsx1LyJMoJekeX9E_fU_5qeVnm3L74uDsWk_AewTahJerbPweaHewssLZ5OVrOsi4LLcLN4xbej3uiJuQlViAMZdGSUdaVRoGysHVk7427kucGc-zDM2Zdk09_YWJdmBiH-5X3Z7WlCCi9wVaCp84mjg7fzbWnW2Fd8yPAZ0X_ceP1KAsMmy72VsctO5dh36sQlZfD9MQGO1I5V7limmcg4qkg5_d-xicM9x89L4enuiIcVX0SPWfmc0Ai838sp6HWy_-9ws36_KaOgMmQMg1XQpRrBPaZroZ2lfZEX6hI772MlfponHFR3oPJGLKxd7tzRdjEo4HbqA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Ea4TIlpmbC_v2l5OkI8yLyaHD50gC4VOhMbWAyetZ5tESSi5qsDySWEPJSQdwjJ8H6FZH73KYrYd1OeAQnpQZFE4w0f2dcGfIH2DDCD9VpTs6OCaTTNW-yRq1qv5c4R3qAeaeuGSwYH4aiPrQAiyuK9okjhmDFUd5zImLCW_6OHKOKXOyjSwVyIKpqySa4jMykL2L7FDGwf1P1fKDY7VK-hFzHItW6mrHL-XdbcGjBOPNPR3Q6Xgzpe_VYACVLcLnILv1GRu4xoAHyhMeo-TXYZyJLOabjthC22rOAjN1ErWqVHqeLKBdSSPkvbRPUQ3PNZAAGv8P5HXBNqXZmy6Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Ea4TIlpmbC_v2l5OkI8yLyaHD50gC4VOhMbWAyetZ5tESSi5qsDySWEPJSQdwjJ8H6FZH73KYrYd1OeAQnpQZFE4w0f2dcGfIH2DDCD9VpTs6OCaTTNW-yRq1qv5c4R3qAeaeuGSwYH4aiPrQAiyuK9okjhmDFUd5zImLCW_6OHKOKXOyjSwVyIKpqySa4jMykL2L7FDGwf1P1fKDY7VK-hFzHItW6mrHL-XdbcGjBOPNPR3Q6Xgzpe_VYACVLcLnILv1GRu4xoAHyhMeo-TXYZyJLOabjthC22rOAjN1ErWqVHqeLKBdSSPkvbRPUQ3PNZAAGv8P5HXBNqXZmy6Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=jVnXb6oNSvraZfRV9UJ9OK8QdfpLptYFPHjr5LYA0a_fpME5-Xz_9o7S2oU8lfN3NZcpzPePDFqIOFJDQcxwhj_sKdd-eAMPjCk82num2xxYlFtpN11oFMrSztgxGSXDUUSv5gSZK9JUTPVAkXApmd-aZo-vpgdV-EMFqkEDf2tO4YxF25pe1iSeol0_F85IeuW80AoJ-bc8FkUNz5kBF4qMZVO3i1phhgMgfzXlGWr4CDqYP7cU2bmeOGHusmS_aYfJrCGyoj8ptn3_nIew005npvXf_FdgT0Wgpe_zVRxVVzznwswDdNBSPN_j4AauNhsbNcxuI4fm10t48Hc4fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=jVnXb6oNSvraZfRV9UJ9OK8QdfpLptYFPHjr5LYA0a_fpME5-Xz_9o7S2oU8lfN3NZcpzPePDFqIOFJDQcxwhj_sKdd-eAMPjCk82num2xxYlFtpN11oFMrSztgxGSXDUUSv5gSZK9JUTPVAkXApmd-aZo-vpgdV-EMFqkEDf2tO4YxF25pe1iSeol0_F85IeuW80AoJ-bc8FkUNz5kBF4qMZVO3i1phhgMgfzXlGWr4CDqYP7cU2bmeOGHusmS_aYfJrCGyoj8ptn3_nIew005npvXf_FdgT0Wgpe_zVRxVVzznwswDdNBSPN_j4AauNhsbNcxuI4fm10t48Hc4fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=iMGsarP_iHi8KinND1VjBcUQzlqXZEVZyv1ziguciRBmCnUwjieizwSUJtML5sD5lZfuExfsuEx4Bq3hCtlOMN4n8rZWMCWh-5pt-Z7U3Ck8d2-28fqu0SmelQWE2t9r9fD_xS32lCc-wBWel-HDK8C4Dfp0zjxSL1RbN5Fd0MebTZgltkUVbxkJZFAFI3eCq73HAa4N3BPVf0j1dmj58yc66lPBmHzoi9hfLfG9sHlFSVGhgVs_CekyHZESA0kQE3rJysqaC1DgJG3zqITFD1-bsdI8DvXlNo7aKD3cHZWf1h524cOSOR6jYf9A_EI6tF9LuACOsNx3O-mAtS_ylw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=iMGsarP_iHi8KinND1VjBcUQzlqXZEVZyv1ziguciRBmCnUwjieizwSUJtML5sD5lZfuExfsuEx4Bq3hCtlOMN4n8rZWMCWh-5pt-Z7U3Ck8d2-28fqu0SmelQWE2t9r9fD_xS32lCc-wBWel-HDK8C4Dfp0zjxSL1RbN5Fd0MebTZgltkUVbxkJZFAFI3eCq73HAa4N3BPVf0j1dmj58yc66lPBmHzoi9hfLfG9sHlFSVGhgVs_CekyHZESA0kQE3rJysqaC1DgJG3zqITFD1-bsdI8DvXlNo7aKD3cHZWf1h524cOSOR6jYf9A_EI6tF9LuACOsNx3O-mAtS_ylw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=PtbEp4UG5JQejr6e4m8_ymj3GfSB-la8XUT0gebhrnnXJnoi6rDxcSdFcjphRYSUuduXUupz8IpO3UBDHdkpZpuge1c-V_Zo36512IkcQEuglmetOaQ25NMzuRe8QxW38Gf97j2iPLJRzKetLkJ9SCmWqDlSo0SIT0DpDlqmZ3NUxHLb7n7LwLVV4DWiU0gchPxAdqX1n0v9tVvCWKcUL9JioYKEvzSDFBwGpvb9CpZyI3HqIY-XBAEpu-RhObEOG1Ans7XogvZ0dLj0AAPNYimbsRgQtJwAWWZ48K6K-rhAze53dQky7Hs_fHTH6GGjCB3pqPYQrcSKpVQsl3580A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=PtbEp4UG5JQejr6e4m8_ymj3GfSB-la8XUT0gebhrnnXJnoi6rDxcSdFcjphRYSUuduXUupz8IpO3UBDHdkpZpuge1c-V_Zo36512IkcQEuglmetOaQ25NMzuRe8QxW38Gf97j2iPLJRzKetLkJ9SCmWqDlSo0SIT0DpDlqmZ3NUxHLb7n7LwLVV4DWiU0gchPxAdqX1n0v9tVvCWKcUL9JioYKEvzSDFBwGpvb9CpZyI3HqIY-XBAEpu-RhObEOG1Ans7XogvZ0dLj0AAPNYimbsRgQtJwAWWZ48K6K-rhAze53dQky7Hs_fHTH6GGjCB3pqPYQrcSKpVQsl3580A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ck2hp7IC0jM3RnIxGKx1T5vyveS9MHhnljN6SlrjNKhPHGbj68VuhSaqyPlLWdK4-Lv2T5dymLQDJxPmQRzohj-f8oz9kp_IF0fKkEEX2Cs3uht_MZZjNZEBN0-YEqr98kV_cmUuKbhKKUOsT1LOeUb7sNuvZZ7MSfn2JYYdviIwTTXuzZLpqfotFM_6i0t-ybQaRjjYHg4dExJlODQm-Gl6H1DOXUtAdr4wBwynsWut1gTu4BYWiaFCkfzWAiO4o5HlLfMMpdOBMYDjvivceGOSq2CA6FxDeOxpSPMNPmfdqyOUC5OPVAgwu_TN-gSsepmxF2zryDdIlwEZ5j07bg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=V1hsbkg7qxY7KaZCthV6lJIVOtGS6yeD64sgEC0OiiQrXgQPkc5syJcfbn-zGM8rpP99gBGv_Of2ZaUB_SOAQ9mWkc7rStxigyb8zjXcXlObPUzxiQxRe645niitJfJNoMVhrKlfca54ZR81mZpqFBwiTXOV_3uAYKg0sKwU71YV32Q_bU2Rt6GnR4mpLPXtcPYAA9-kHjKw0nCLnT2gOND9Xr-R8-8oMdcZ15qeXqEJomIinyQ_HCdkji4rN01L7glXViCuni5bUIBMwejmjyj35OXa_il5kncuuFBGE8ChGIvoXVCK-4_Qkw6kJ7SD3lwJ1Bcj7dB0JDIE-Ni0UTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=V1hsbkg7qxY7KaZCthV6lJIVOtGS6yeD64sgEC0OiiQrXgQPkc5syJcfbn-zGM8rpP99gBGv_Of2ZaUB_SOAQ9mWkc7rStxigyb8zjXcXlObPUzxiQxRe645niitJfJNoMVhrKlfca54ZR81mZpqFBwiTXOV_3uAYKg0sKwU71YV32Q_bU2Rt6GnR4mpLPXtcPYAA9-kHjKw0nCLnT2gOND9Xr-R8-8oMdcZ15qeXqEJomIinyQ_HCdkji4rN01L7glXViCuni5bUIBMwejmjyj35OXa_il5kncuuFBGE8ChGIvoXVCK-4_Qkw6kJ7SD3lwJ1Bcj7dB0JDIE-Ni0UTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=h1WW0KLswjj0Y3JRrGi4P9LyBotBYjY0s8iiWLCXhtbr3sFYqpBtViC0uP2vQEyOSsJz95FZvoYWSpi5xB5aZBj3ETjsrhUATvGtvK5-rd3ptm7oHSLe9Ob5-lCz-CRaMfBOC33JQeUJmwm6cV1iwE4cgBk3Mv_Fm32pIJfWyCqohs008zG_b37CkkMv2nuHV1Yrvr36sxbcqYfKh6GctaSGTMGOSk8K43T5n3K466qEJ-FTr7ZwcHiDt8AGELH4x1R-PamnGmPj3pIwMmj7MLzHRbZeGC38INlqUV5qhT9sGhr0RxeWGlh5BRmV4cy3800roCbN4Eo35lKrfezcXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=h1WW0KLswjj0Y3JRrGi4P9LyBotBYjY0s8iiWLCXhtbr3sFYqpBtViC0uP2vQEyOSsJz95FZvoYWSpi5xB5aZBj3ETjsrhUATvGtvK5-rd3ptm7oHSLe9Ob5-lCz-CRaMfBOC33JQeUJmwm6cV1iwE4cgBk3Mv_Fm32pIJfWyCqohs008zG_b37CkkMv2nuHV1Yrvr36sxbcqYfKh6GctaSGTMGOSk8K43T5n3K466qEJ-FTr7ZwcHiDt8AGELH4x1R-PamnGmPj3pIwMmj7MLzHRbZeGC38INlqUV5qhT9sGhr0RxeWGlh5BRmV4cy3800roCbN4Eo35lKrfezcXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/huNitD7gPLZ56PZL06dKCL3U8JyRG3J7_KEizMsrFkB4IvvkXYAO7FwrxiAyjqgq-h2H-jdEoA0EoUwjJ8n0uMITNOngoeAvJ869-szySyChB76rW2BZHkKcvSoDs1ksvSDGhFwN4eLgCxKKjvRXxn3rpEDt8R8OCU8mCLDlNA8Uv1jExrmCa3-vmhncRpdblAtasa0pbTqo6b4a8GJZoH97W8LfIBKOFhPa2W4b_wz00PJzKAz3hCf_LgwZgkp40neD6YgQR1PLq1_EWNa7nHaypj3R2hIfBSMpL4cCGZf7qu0azzbLpRedTBTXK2yS-czQkiLiAOYCONNAK-NZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YArgxcvXsX_7WpfeehQr40UgsK_DASPOeDe7E7CyMaNpeQ-gZVVMtfHMaGNBGN9Fjj3rL0P3Qt-BZ_OHSaHAiISGO_5YUwEzA9-njhnd1qz5hKCWO7TYdOQjGXu2ppgmyzPYf0iRg0NuuJFpMRhkTiK7AmwD9uQAjogufdxo0GR0DQTOxlY3McfviUK-ACUmWR01oZEOyi3wwJFFlqN4wzSoNt_0LjstykN0dn0G5aT2zdyD8Uh5iujiPHLeDPzZMaTW4fBQ_RboQysAQPZqnmtw13Lwnd4Zr3cXq-I1x00ORlJhsllaInjLf6L0VTr5RusQF4aJRuyL_aTODDotSA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Vglt5aZehbojJ5QYDGfCdvNu6YTD08aub01V41PoPsQaM7Zxy_z8ZiXtT6iop_aEV9Pv5etEnpKIjwO8gVVMynRfLeC88_kcAf2mLXdReNqLoFCJGwouwV0XSxtODuXVp2smlk1U8f4jfMxpeuWFh8q1B3nWQMelUnRSBNs4Ufdub8xwwBB1qF6Jm-XHQA4Fptm12xvTG_yPUAt-8K81mwix_gGUnHelvUZ6jSpGIIPrApKATxp1gp0quqwHeTzlH1VH_34EXpKJ61ZQUyyGBAsiFqscDZrvHCEgCuUv1chLTl1zu0ZRt-CaG0ELZjAa8y6vUnHQznN6xZS8VAGkyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Vglt5aZehbojJ5QYDGfCdvNu6YTD08aub01V41PoPsQaM7Zxy_z8ZiXtT6iop_aEV9Pv5etEnpKIjwO8gVVMynRfLeC88_kcAf2mLXdReNqLoFCJGwouwV0XSxtODuXVp2smlk1U8f4jfMxpeuWFh8q1B3nWQMelUnRSBNs4Ufdub8xwwBB1qF6Jm-XHQA4Fptm12xvTG_yPUAt-8K81mwix_gGUnHelvUZ6jSpGIIPrApKATxp1gp0quqwHeTzlH1VH_34EXpKJ61ZQUyyGBAsiFqscDZrvHCEgCuUv1chLTl1zu0ZRt-CaG0ELZjAa8y6vUnHQznN6xZS8VAGkyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHcVaOb83geEEo_sw11E6wVzJvxnSmwM3CFrxHvk0sT-XGoErAT-JTPPVukoXWyd6kH9OIoxt7SZdDD3PQbfD1HWiARAH2oULpXWp6NSPPUXbA96cD_cg0WmPeAR-LpgqlTCK6E57CVi0uqLJhpzKeitNalrxTAyRr-YJaFbImES9bsfXaT7omjsL1l5FZcyJvvK9s4tcVGLY0NIAYpgvwN5k7zqKpxAE9p75BX7z70mUWKs7zXKTBuRRGH9yxqVy3g8sPmpSvqpZwJiJ_Pk3bgeHIWVC-7mBM3HVwwO_faagcHJRWueiIKc863w6KNd4bHx4k58JFU79jKAvBS0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6raQPMaR7wQv3Tm9zjGW5UpgUyF8LhVckvx5vSLX_AKnnlwfdXdoljOXpv0jw74z_rWE7DGlMt5N9XKwG41r35Lf8wLPTrhISUzYX6AvuLN6gchs2t6kdVUUnrIkPAgsp1-uPagcdkOqJblqcyNZopiNGxz4YOSKXKoFcGi0LBxhfhzZ4o0FnRiXaMKCi65ZZSiTa7TbZ5zJyw0JgMgXABBiLGGQ4-PzAdnDkExTM8vn_GJrLfjzYSFy88pcRtP32gSRX70ro-s-6RkMEUe90UR5Gi29ewY9lubecrHK6nwKEKRzS_b1QNo9ZV3cb9wYbl-0a8OugZ4Zo13cNidlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ7XOw1k8WujwxQZMICib0pyA-w2Q9p1ZyU8GariiTsEUg5X3v3ikuWblPhFRciZskjHvnMA7hyRYBruFdkE_ri3dGp6ncExtA2l8UVxEV-m7nmKCbmoxIcXhyT7WPxCq2ILOYt6dRBSuMzkt8N5LzJsS5F90WZjgJJ6UNDOCiUVUCGhOdamkgBBfhNUrrjZloqJRrV_h0KJG9JTAyCV8x97MrBIjovAYTnosFuADIt07GHnn7d6IBkVhKMDd7A_7E8FXYMn-dJNEsP6bji5XY-naL3kbDAGb745W-LtIYd4feoQb6Ei2WRmT3fdIKBVps2OFIYw0BkJfiBqmsJKww.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=u9Oo2yZ-2KSKa-Axcthj8X-ri2JBwMKJ8m4kqvRdkCaPyHGdde8_Dv3sZi7Kr4QYT0Ag08rvs0oJ8ARA4IS3r_9YE68rp7qZKsPdNtjuHd_OekKYx-KLQ5hvpIrKi08eifSazoN_Ca3BXMqjrU3u4vqh-0bW5Sog3w23PbR1oX1AbtJMOrqssnX_-rR3jOhoudD1_9ox_BRaTs_GuyyuppR7JU9zMMpO7kv5N63vei_UGeO7p075QIKQf19SqaIe3k1w9jitrKw3_I2mWKO5gGcnj3tk67kAOqBqhubqq8ild60eZS2x1PrfUQvK969r23miX1fOx4KO7dLkij5naw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=u9Oo2yZ-2KSKa-Axcthj8X-ri2JBwMKJ8m4kqvRdkCaPyHGdde8_Dv3sZi7Kr4QYT0Ag08rvs0oJ8ARA4IS3r_9YE68rp7qZKsPdNtjuHd_OekKYx-KLQ5hvpIrKi08eifSazoN_Ca3BXMqjrU3u4vqh-0bW5Sog3w23PbR1oX1AbtJMOrqssnX_-rR3jOhoudD1_9ox_BRaTs_GuyyuppR7JU9zMMpO7kv5N63vei_UGeO7p075QIKQf19SqaIe3k1w9jitrKw3_I2mWKO5gGcnj3tk67kAOqBqhubqq8ild60eZS2x1PrfUQvK969r23miX1fOx4KO7dLkij5naw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=R3gM6_S-526LnUN2JuWMQAx87V9e4dPq3olaM9D8-fphSdz3r9hrzAgtEkpmR1pxGiMSTl3dcD3H7TqUB5hzRGHJDT1MCA_C0bRehdEuMg0gbA4Tpy4tYG6NVlbY4B9J6yO8BPx5H1PYGhXsZ0Y8a2qZNO1H5WryD2g_MbFwjhJs_QeMQwlurWe2xYWle8sUYZt8PsdnLbLvyE4pMr1C4gMeEP8-nyIEqDpNBNuqjxxM6mUG7nZDCdp1dQHK73w-zNN8hJRIwDgbzvv3V1XfLWdEOawMEL7g6Qn45XfSVUpyC2fWim8h8fCHwAvcRn4Fhi1v6-CNhOtH5ce4ibDdQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=R3gM6_S-526LnUN2JuWMQAx87V9e4dPq3olaM9D8-fphSdz3r9hrzAgtEkpmR1pxGiMSTl3dcD3H7TqUB5hzRGHJDT1MCA_C0bRehdEuMg0gbA4Tpy4tYG6NVlbY4B9J6yO8BPx5H1PYGhXsZ0Y8a2qZNO1H5WryD2g_MbFwjhJs_QeMQwlurWe2xYWle8sUYZt8PsdnLbLvyE4pMr1C4gMeEP8-nyIEqDpNBNuqjxxM6mUG7nZDCdp1dQHK73w-zNN8hJRIwDgbzvv3V1XfLWdEOawMEL7g6Qn45XfSVUpyC2fWim8h8fCHwAvcRn4Fhi1v6-CNhOtH5ce4ibDdQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=YRtExJZhOTvX03GplhPUyyJrxnhNFQtO2IcOnQloTUQu7uExOWJrUHkbWQeY5H4Rs1wVIcN2qcXlZuf5XT3NQbZMmeoJhnYtElm2myIEmautAkBkM9McJ2VjLfQGld_AjFvy8OLgqlHD-gjWKrrJc1mtGonnG5mfn7oHyjcDP_48U_nkzazZjjyBAkCZ1t0jGeZs4wugzG5OxkImdkH-NWxTl0G0QTluEJIun_FxAsPRlb5sRTeML1S-1okfHj2GWaI5HE03ngAdC_U4QkxyC5_rrqeTpzymj4ahjuZ0ymV4LxpD2bkP6D5azOOV5BI6DMXFUfxDv4d7YzNbKtAUu6Nz83IKLoaW9iZZHTisF9LQMkcCkLsu0XmQW_642nCoGsFEtDpIo-iDhfgrS8MudpZkhht-lEEZZQ8LTuquqo91Cf28ngACfrWheonPrXtNdMghiy1qv-RFnvWCc_KihjrQLpMKy_XSTZCpym8CNNeBaC5PnVeMzZlWFodB8TRMdAoLa56zrBJPtPCkKEH6KrUKrmIHBxAPxkS9KVtXgdeBmX9r-xqIp2Ny3UfA6GIBqLsEAal9pVIKp1JhvV3ykW3kwjbiaMrkRvnDg5QUXvXeqct8iHXrPRdxRrLUlq01urkJxycS_Vg1fW3qaHkYA3dC1-8hZ4oNeopLmiNi1NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=YRtExJZhOTvX03GplhPUyyJrxnhNFQtO2IcOnQloTUQu7uExOWJrUHkbWQeY5H4Rs1wVIcN2qcXlZuf5XT3NQbZMmeoJhnYtElm2myIEmautAkBkM9McJ2VjLfQGld_AjFvy8OLgqlHD-gjWKrrJc1mtGonnG5mfn7oHyjcDP_48U_nkzazZjjyBAkCZ1t0jGeZs4wugzG5OxkImdkH-NWxTl0G0QTluEJIun_FxAsPRlb5sRTeML1S-1okfHj2GWaI5HE03ngAdC_U4QkxyC5_rrqeTpzymj4ahjuZ0ymV4LxpD2bkP6D5azOOV5BI6DMXFUfxDv4d7YzNbKtAUu6Nz83IKLoaW9iZZHTisF9LQMkcCkLsu0XmQW_642nCoGsFEtDpIo-iDhfgrS8MudpZkhht-lEEZZQ8LTuquqo91Cf28ngACfrWheonPrXtNdMghiy1qv-RFnvWCc_KihjrQLpMKy_XSTZCpym8CNNeBaC5PnVeMzZlWFodB8TRMdAoLa56zrBJPtPCkKEH6KrUKrmIHBxAPxkS9KVtXgdeBmX9r-xqIp2Ny3UfA6GIBqLsEAal9pVIKp1JhvV3ykW3kwjbiaMrkRvnDg5QUXvXeqct8iHXrPRdxRrLUlq01urkJxycS_Vg1fW3qaHkYA3dC1-8hZ4oNeopLmiNi1NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=s8dNVEczgCgOQW0hfYyLQTMCtvJ5hh1rIRiiTamNrEUwgeWafs6GkWp46cC8X_XNFuT6DllQj-3UJRqVz91txPMyVhWNsHVXAkK4XHLG5UiPTEeC4anGaoAHqA8IuwJVUU6FGRt3wkeq70gPYxBvarvDOjYlOaNzQnDoe2o3zFeY-J8eEDZyK63GF9ig5tXamCbuknBS2VbCgxaH5e-xqU35bmMTrc5HbxHxHKNXhMnNnCz_3LReimpj7R5nRSZvVWYOkMNAo30cZwExy3BvVr3f3rP1ku9q40xi9D4ixGZzVFQyA88vzaI8IzbzjOYduyGgiq0Lqw4u5pWYvNXvppP_MWJpNktntJwaH946rzB5bq4-ZYXkl4GEIj1TPp3ZIYIS-zPcUH0HtJmGRwDyKPbkOPJuO_xyR1nWmJVIeV-xcWh-0If4HS4iegcB0E0wbl0aC5XvWSsGqnA2A9YA9Tz2O5-lpflmi4rEW4PNXqPP32stEZ36xNDxca4AUf_tpzucguUCATNJxEqyTulR4AW3F0pr6c5nyj6daSK9dV3XbfAZj7TieCBkIHP93g6N1A8wy34YZYhfe7KT72Nm2yfzbqLID8JtDhZb8oZE8ORt35b1aLuOlrTed3RZXAcYZP5ipJ5Asvs_hi79d5oUiEDl9kVYnhEBFYs--nMQ3Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=s8dNVEczgCgOQW0hfYyLQTMCtvJ5hh1rIRiiTamNrEUwgeWafs6GkWp46cC8X_XNFuT6DllQj-3UJRqVz91txPMyVhWNsHVXAkK4XHLG5UiPTEeC4anGaoAHqA8IuwJVUU6FGRt3wkeq70gPYxBvarvDOjYlOaNzQnDoe2o3zFeY-J8eEDZyK63GF9ig5tXamCbuknBS2VbCgxaH5e-xqU35bmMTrc5HbxHxHKNXhMnNnCz_3LReimpj7R5nRSZvVWYOkMNAo30cZwExy3BvVr3f3rP1ku9q40xi9D4ixGZzVFQyA88vzaI8IzbzjOYduyGgiq0Lqw4u5pWYvNXvppP_MWJpNktntJwaH946rzB5bq4-ZYXkl4GEIj1TPp3ZIYIS-zPcUH0HtJmGRwDyKPbkOPJuO_xyR1nWmJVIeV-xcWh-0If4HS4iegcB0E0wbl0aC5XvWSsGqnA2A9YA9Tz2O5-lpflmi4rEW4PNXqPP32stEZ36xNDxca4AUf_tpzucguUCATNJxEqyTulR4AW3F0pr6c5nyj6daSK9dV3XbfAZj7TieCBkIHP93g6N1A8wy34YZYhfe7KT72Nm2yfzbqLID8JtDhZb8oZE8ORt35b1aLuOlrTed3RZXAcYZP5ipJ5Asvs_hi79d5oUiEDl9kVYnhEBFYs--nMQ3Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=HDlxLpOoKaTAuDZQDOgDide3MIeRzkHJFtC-KSsufT_2e5Akg6h2ujvMYcU45w8pcO9L-RycSMyrpyX2wGpUkaZ5gyIKPSbQ_iWieK2Bwo030xAw9wr-1T2fmGPRH2rI2GxRS3oUmpJ-xZup_1_O9qBPKKYZCPvzHjd7d_tlR-gweEqeb5fdqwqbgReIMajQUpybPMvgjgJGa1eiSOf3k6PoAV8p-6GSa9sh8yIf5SLzTotF2yoMLUIt4iEvsH9Zw0x0_YRFrAp4sKWcwzFc1q9Ls_fZHMpbjXNS9n27lZWhKETwCWD3hZ8SnW577kHs-uttjriju_uY5AW1qTmngg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=HDlxLpOoKaTAuDZQDOgDide3MIeRzkHJFtC-KSsufT_2e5Akg6h2ujvMYcU45w8pcO9L-RycSMyrpyX2wGpUkaZ5gyIKPSbQ_iWieK2Bwo030xAw9wr-1T2fmGPRH2rI2GxRS3oUmpJ-xZup_1_O9qBPKKYZCPvzHjd7d_tlR-gweEqeb5fdqwqbgReIMajQUpybPMvgjgJGa1eiSOf3k6PoAV8p-6GSa9sh8yIf5SLzTotF2yoMLUIt4iEvsH9Zw0x0_YRFrAp4sKWcwzFc1q9Ls_fZHMpbjXNS9n27lZWhKETwCWD3hZ8SnW577kHs-uttjriju_uY5AW1qTmngg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-kC499938bRSYWx-txV6NPBD2e5ZEUyIwFZvo55EZ0PPrEsSpYK_-p4RXpt0gkNxCfSQ-CggjurgeuFHYRWLXghU_IvQe59MLQTS_59fNcVfyppL4t3Wzrdzy4i-iZZbybz_SAssZyLziG3FLBgcaf-qVoo83rmJZpqdAxqA4_lqdDdGTHmI3gpYRr1XmWxscJu5P01YvkU91nx04U6Jua1APrABKZvxZ2kGiJdi4fA0n2PXxO1NftJ-QHxkjpclitTSEBzBYRhytS65155mDNySxZGiL-Mru18a27YENdvFVjka1rk_R800aG0R3OMezP4u_ku8uJm8S1femqOag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
