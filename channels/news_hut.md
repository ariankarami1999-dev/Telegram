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
<img src="https://cdn4.telesco.pe/file/IAp0lxosLpzmXajifemzV0lrtYevhYkhQGChPvGRd57HMR6sMQyEfKw3DXyE_S3eZGf0Va4qqSIMv7NP-K8-C3ow_sT935BmghzcPtOE55Z3s4SOcXu7P7n1KufUFDmso8R3xzeWRIMcrqcRpAogN96pIKtsuKjPNtk47E45V1xMJz1uaS6BOUacuqHHSBeBRk1JjtC0HE2tcC7epAZGccZm86GOB-D1YMgnrIQdtjBNefKpek94QydNrHhYxhfu5jnGkGUYud-AIqdJ7zv6bjO2a4BJmesqIleKW24frv_jl8vD7-XK3ZdAzon2yb3Eh4wZfl3mTtmfLUdw1jPJKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 135K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 23:36:34</div>
<hr>

<div class="tg-post" id="msg-69541">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2gUsnoScekGBuB3xIyEGWpyXxTuJ3vrMza0p6ZNWbYTd8nYEdtYoVZq4Za6EaoKelFKI7xErkfUeBc7wYr3Xd-rO57hRviIDB-OVx4JVhhpPhp5-ZC0DGGBnOpQ59raprYEzqUGF9PGQysYq7JIcCvFxPnwAPSpGTlNeZHbeFTJDW0Ur2BTETECB_CA0lke89TN6lSK0boi6XeJmkZEeyTt_AOaJBRWIHELCsyN9RYy_k2YSXAEkBv__se80dCmOL1O2jnoHZA185Eft69x24JHKUtqTJYsEQEg3HpI9iCVwgGyENWooQj1Jahh9p_Q06dUHajpKBI5Wrqgj79kfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFovRvHGf1_DVMMjc8glAv_NEbhYR-RiDjY3GIkTeLRiq4ae4pruGKchs0fZfp6RThQLOqnptRW97U5ckxXK-zTC3iMf0QB1IVXCdhli5XYHrNAUu2YFUn-t1eSgVyp4h-Kyd3ATb0TZ4ZVAI5lr_IfuK0b56XONZhNIBQlVKP17ONZyOkcdElFgLXUcPpmiiadPUHAv2TzxOtwOtxnzZXopZY4xVyUTYnogPo2nCp6jfN-q2KYbQUvBZ6OfVgpDbuT1d9128s3R0SmTvsjw0EPqgue8islgSotS4iTT3O5cOF9c8uAotsyJuXpboyborIKAl9irqTIewz6zRaFfTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▪
🇺🇦
رونمایی اوکراین از ربات رزمی «Droid TW 40»
.
شرکت اوکراینی
DevDroid
از ربات زمینی تهاجمی
Droid TW 40
رونمایی کرد.
این سامانه با حداکثر سرعت
۱۳ کیلومتر بر ساعت
، برد عملیاتی
۵۰ تا ۷۰ کیلومتر
و ماژول رزمی
Wolly
مجهز به نارنجک‌انداز
Mk-19
کالیبر
۴۰ میلی‌متری
عرضه شده است.
برد مؤثر این ربات برای درگیری با اهداف
۱.۵ تا ۲ کیلومتر
اعلام شده و
Droid TW 40
می‌تواند در حالت آماده‌باش تا
۱۲۰ ساعت
در میدان نبرد باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/news_hut/69541" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69540">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHI8E_TBOW4RfK1tKAkRfJ-OUcVQA0Qcbr_49SxpYKjc1XzJ7xIxPNa8Rm5e9kPyxt9cwJlImMbHfu72BfMRbl4S0y-EFZ52AdrxksMk8uZAFn-QGRlyQeVgtfcov3_dtbZXak06BzkxkfiiWnvNKO5NJ_LMs09I5zMOs3lizdVI-3-eZ05HiKrStxQD4WSRkM2ckrYcVLW3odCAN_tj-26I479Rain2ZjDKn9TfHbG0uNDqp2EUm9z2QUJfjXU_laEs49yzrZuhmH6EUsicd4XJ3lMsMIXosMjMavnrWHEPN4eC5u591VWS7ltfn5JYdvhCiidmU3o13dZ5fIHKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
نقاشی وایرال شده از زمان قاجار:
در زمان قاجار زنان روی یک وسیله تاب مانند میشستن و یک زن قدرتمند، اونارو بالا و پایین میکرد.
شاه یا یکی از سران مملکت هم اون پایین دراز می‌کشیدن تا زن انقد روی آلتش فرود می آمد و بالا می‌رفت، تا ارضا میشد!
@News_Hut</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/news_hut/69540" target="_blank">📅 22:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69539">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=mG4diN1xeKWo1dnWhBe_ZkquCn_BiYiiMep_cXNY53DFXpMqPOxyLFn0CFkNKRi5QP-0HnLq4ZB1H_wb1PCZQbQIOt86q3GqTkE62UVJFtrZO4D7gBVT7WrKc17S-uDOwZIgf20xx73722vkJ83v30pKt9ANHLYwfrBcQTCDcChPZZ6vpEqx_wezZ8lxJYBH83RfkDfiC3EGHYt6TiHqor69PgUAD4ZoRKfLvWOdaUhTaRc2766afzmcs5okdHbCteAdW9dic0FGq5WvFUF9nBypyx6h-2FPe3HtWCO_ZolmyEhkC1hDK4WY7mSZDZmWZ-EQZAhSx9Rgke9QRaJ3tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=mG4diN1xeKWo1dnWhBe_ZkquCn_BiYiiMep_cXNY53DFXpMqPOxyLFn0CFkNKRi5QP-0HnLq4ZB1H_wb1PCZQbQIOt86q3GqTkE62UVJFtrZO4D7gBVT7WrKc17S-uDOwZIgf20xx73722vkJ83v30pKt9ANHLYwfrBcQTCDcChPZZ6vpEqx_wezZ8lxJYBH83RfkDfiC3EGHYt6TiHqor69PgUAD4ZoRKfLvWOdaUhTaRc2766afzmcs5okdHbCteAdW9dic0FGq5WvFUF9nBypyx6h-2FPe3HtWCO_ZolmyEhkC1hDK4WY7mSZDZmWZ-EQZAhSx9Rgke9QRaJ3tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای از یک پهباد روسی که یک شهروند اوکراین رو تهدید میکنه و در آخر هم خودشو میکوبه به طرف و منفجر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/69539" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69538">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3447971507.mp4?token=f-FXlXdJHTfLPe5DZ4R3dnI_LZbRW62GxCKQk8Qz4oTW5TVGeZwjuv3rstgZWBG8EarK8NDtaPQETSaM9C7lKK2Pz8GWk59p1NK7H9KRrkDOcPsEt93dsalz7ssDYvIfXCnXZgDKCtVyr-r-BrfV9BhuSFctOBFdgX73xSL-5uk_YajCvCoFSxtsnKEBCDHH3vLeWkKRHxjwhIwsWNafae_Rq40-tzPcp6uXBBIwvH5Bw4xyYiK33A9VYC9-yLEgA8bBRbdInQxkatRicl1ZKQekfb80_mZQ1AQABlCHJv43m-49HJ5Nu49Gu1XGrT3YgrLYm9DoHr1QiqxNyZuO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3447971507.mp4?token=f-FXlXdJHTfLPe5DZ4R3dnI_LZbRW62GxCKQk8Qz4oTW5TVGeZwjuv3rstgZWBG8EarK8NDtaPQETSaM9C7lKK2Pz8GWk59p1NK7H9KRrkDOcPsEt93dsalz7ssDYvIfXCnXZgDKCtVyr-r-BrfV9BhuSFctOBFdgX73xSL-5uk_YajCvCoFSxtsnKEBCDHH3vLeWkKRHxjwhIwsWNafae_Rq40-tzPcp6uXBBIwvH5Bw4xyYiK33A9VYC9-yLEgA8bBRbdInQxkatRicl1ZKQekfb80_mZQ1AQABlCHJv43m-49HJ5Nu49Gu1XGrT3YgrLYm9DoHr1QiqxNyZuO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
چهار سال پیش در چنین روزی، یعنی ۴ اوت ۲۰۲۰، انفجار بندر بیروت — بزرگ‌ترین انفجار غیرهسته‌ای در تاریخ معاصر — پایتخت لبنان را ویران کرد.
هزاران تن نیترات آمونیوم که به‌شکل نامناسبی در آشیانه شماره ۱۲ انبار شده بود، دچار حریق و انفجار شد و موج انفجاری ویرانگر ایجاد کرد که چهره بیروت را در عرض چند ثانیه دگرگون ساخت.
این انفجار دست‌کم ۲۱۸ کشته و بیش از ۷۰۰۰ مجروح بر جای گذاشت، حدود ۳۰۰ هزار نفر را آواره کرد و خسارتی بالغ بر ۱۵ میلیارد دلار به بار آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/69538" target="_blank">📅 21:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69537">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=YOQQ6dilprqXodFAGKIyuzDOwBOIhN4s79Y547pYekt160QvcAs7ZsG0k5hYO12eCnqFuqRfW5pQ95K_DKB4SeC0EB8GCHFz8GbSsqsatg3vhVB0Umri7o6f2armRpRfS4SnltP_1ynoF8JT2S_0-Lqmsee9kpBITAXJQyCg4RfMGDx8Q9QyAikQzFBHrLkZzJrFbbTtF0yYVwsZIoyMYfnGIX8BuFnJWNAhWfBgmnWp1nF6GUChyhwq1O2_dv5gPEOUxq8btmSK4XcMeaSVabsGb_ikICl8sqTFrzJcvluFNmZZBhlnIB0mYPDwC6tE_6_4D2IZ-5PQEJSVUvNqRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=YOQQ6dilprqXodFAGKIyuzDOwBOIhN4s79Y547pYekt160QvcAs7ZsG0k5hYO12eCnqFuqRfW5pQ95K_DKB4SeC0EB8GCHFz8GbSsqsatg3vhVB0Umri7o6f2armRpRfS4SnltP_1ynoF8JT2S_0-Lqmsee9kpBITAXJQyCg4RfMGDx8Q9QyAikQzFBHrLkZzJrFbbTtF0yYVwsZIoyMYfnGIX8BuFnJWNAhWfBgmnWp1nF6GUChyhwq1O2_dv5gPEOUxq8btmSK4XcMeaSVabsGb_ikICl8sqTFrzJcvluFNmZZBhlnIB0mYPDwC6tE_6_4D2IZ-5PQEJSVUvNqRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
ترامپ و تیمش تصور می‌کنند که می‌توانند حماس را به خلع سلاح و غیرنظامی‌سازی غزه وادار کنند.
آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم.
این پیش‌نویسِ ما نیست؛ ما نظرات خود را ارسال کردیم. ضمناً، ما نظراتمان را پیش از آنکه شاهد هیاهوی رسانه‌ای پیرامون این موضوع باشیم، ارائه داده بودیم. موضع ما همین است.
و ما بر سر منافع خود، هم با درایت و هم با قاطعیت، ایستادگی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/69537" target="_blank">📅 21:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69536">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnlMqZPkEipH3Ei7Pc_877aGmlHUxULYW0M7gKf2jeiefnzpg5T-tXh-cdSW5eeWLXwDadP-Qcg-_3Y5t-zt7-GkXVo6J9DoaWA_k4KzKYQvFaxck4awA3ZRGtKP2zxBKYyA64JJ_-LXePiBUR1dfvo4Nrd15bW-bfcX4GPvxRYBVVBa61U1TjSNwjPrroOVdAP2OEMABvpHx7ldciHS1SldLNHDRKyhngw2lUy2tyO2qLKxlNnn4qUmC83MNHGMDhtHNJtpB69j0pp5cwR46hylSmj5kl4Bzg39VOULxTxzNQkFAFgtFq640mVtfvJ8LdXyDoLjcw8vaP97tuP9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال‌استریت ژورنال: در حالی که دولت ترامپ بر نزدیک بودن احتمال دستیابی به توافق تأکید داشت، وقوع حمله‌ای جدید به یک کشتی در حال عبور از تنگه هرمز و بروز اختلاف بر سر مسئله عوارض در جریان مذاکرات برای بازگشایی این آبراه، چشم‌انداز این کریدور حیاتی انرژی را با ابهام مواجه کرد.
به گفته میانجی‌گران منطقه‌ای، بر اساس پیشنهادی که هم‌اکنون در دست بررسی است، کشتی‌های عازم خلیج فارس از مسیر آب‌های ایران وارد می‌شوند، در حالی که شناورهای خروجی از خلیج بدون پرداخت عوارض از آب‌های عمان عبور خواهند کرد.
میانجی‌گران اظهار داشتند که اگرچه دیپلمات‌های ایرانی در ابتدا از این پیشنهاد استقبال کردند (زیرا تا حدی کنترل بر تنگه را حفظ می‌کرد)، اما تهران خواستار حق دریافت عوارض ــ که احتمالاً با عمان تقسیم شود ــ و همچنین دریافت تضمین‌هایی در برابر حملات مجدد، پایان محاصره دریایی آمریکا و کاهش تحریم‌های نفتی شده است.
مقامات ارشد منطقه‌ای اعلام کردند که آمریکا و دولت‌های منطقه با درخواست دریافت عوارض مخالفت کرده و خواهان تضمین‌هایی هستند مبنی بر اینکه ایران و نیروهای نیابتی‌اش، قلمرو آن‌ها را تهدید نخواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/69536" target="_blank">📅 21:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69535">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMCFvIWC304sDYiVUeiAqqu48vTkkpWPWybnFg45im3YiYGirkW7yIkQudnqzBtZu-ewqqOklUdst3ogmMX5pyHIzQTPr250AfCh1xh4_a0YAlegKuZaPW7R7Ccyw33HfBd2RdpK4U90M6wrQn3w958VSL2JxLE_kBNpPYSor2idmCXaS_LFAmuC1lwvDsN5K5W4aMwoffFyiA-OI1fSlU3CdJyT1gxY6G_B86ATI22z3wMK-LQV1S7FPFA63_LpiuZyQ7pLxE3euXY-EugW_LLOShxGvxcC4mBL1g86KE76pwF-wrlog1aN7JtyqZ9-bu4DMy24gWYDWMXV3Yo1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:یک ملوان نیروی دریایی ایالات متحده در «مرکز اطلاعات رزمی» ناو «یو‌اس‌اس باکسر» (LHD 4) مشغول نگهبانی است؛
😃
این ناو تهاجمی-آبی‌خاکی در حالی که از محاصره اعمال‌شده توسط آمریکا علیه ایران پشتیبانی می‌کند، در آب‌های منطقه در حال حرکت است.
تا تاریخ ۴ اوت، نیروهای آمریکایی مسیر ۴۵ کشتی تجاری را تغییر داده، ۲ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی دیگر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/69535" target="_blank">📅 21:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69534">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=gVx5h7RhHn-5E15B8-Tbxjyyt-ceLzQErJqMc2wQA3BdjVA-_USs2pnPv1LNdrSH9osDcucIx305Nm1kQjltkg2U_GHJYSa-pEC2VduUN2EqaO3GgBAdEeze8cbNXZtcwyTW40xzA_G8YfXJIjIt7UYAFNAPqYn5DiRgi3IqPu-sDNFqBvkvU8Hr6setSLVcngk17wMhI6bF2wwOgauuTVh8kzGRTw6FN6rWsF7dQbgmfVN64xkmhcYGCtoBpWyeDgjBmzTkIL_9WU3nqMy9vLWEOESA6CldTRbVXAaML5r02FtK5n80BqLiQsrs9Y-Ket1jtfZKPJVeuYIfzRAgHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=gVx5h7RhHn-5E15B8-Tbxjyyt-ceLzQErJqMc2wQA3BdjVA-_USs2pnPv1LNdrSH9osDcucIx305Nm1kQjltkg2U_GHJYSa-pEC2VduUN2EqaO3GgBAdEeze8cbNXZtcwyTW40xzA_G8YfXJIjIt7UYAFNAPqYn5DiRgi3IqPu-sDNFqBvkvU8Hr6setSLVcngk17wMhI6bF2wwOgauuTVh8kzGRTw6FN6rWsF7dQbgmfVN64xkmhcYGCtoBpWyeDgjBmzTkIL_9WU3nqMy9vLWEOESA6CldTRbVXAaML5r02FtK5n80BqLiQsrs9Y-Ket1jtfZKPJVeuYIfzRAgHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
یک جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در آسمان خاورمیانه از یک هواپیمای سوخت‌رسان KC-135 Stratotanker سوخت دریافت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69534" target="_blank">📅 20:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69533">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBtL55xc8gGSLjref35PbQYBcVOJFFsX6tVUG7sZDRSySaFHLVSLDSaDdWdWMEEgBeXNqTVni4rZZC7Q7l5PVBuObFnj6SoPVB30J7pT_rI_OrrpbuTghNDlWC-tWbl5rQFWD8YLCfz_gHGZkubpwWa6k4Kq-LvDee4peLczt0QlW_uo2g4u1NZttKM6aT9OGtA8r2zKH3Jr9VK5iq1MsBGWixvB7jGwMl2uE3gxwB685XlCH52pz6Om9Pt-mNl5krcSBR9yLtafyd2nrgdJ5Z0nbr_hG7mQWmv_m-XcNzH3iMeG6LFT3zNLZPCl7s9lERJ7xpsgxkCGBqM9twl1DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ایران در حال بررسی امکان مشارکت کشورهای اروپایی در عملیات مین‌روبی در تنگه هرمز است؛ اقدامی که نشان‌دهنده احتمال تعدیل موضع پیشین این کشور بوده و می‌تواند به تلاش‌ها برای ازسرگیری کشتیرانی و پیشبرد مذاکرات با ایالات متحده کمک کند.
تهران پیش‌تر به‌طور علنی با هرگونه نقش‌آفرینی خارجی در مین‌روبی این آبراه راهبردی مخالفت کرده بود، اما در هفته‌های اخیر و در چارچوب گفتگوهای گسترده‌تر پیرامون عادی‌سازی تردد دریایی و کاهش تنش‌ها، انعطاف‌پذیری بیشتری از خود نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69533" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69532">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=OYY5hZPC7CRhvbvi8xLgevsUlc1YsfJ109kd86y7uApFHD3lWfkAHO1t-A7NUOhwxZK95rmm7NDsuXeUdhGsquON6GeI1REtaIOUaaG67V6fZMOwl6ukl9Auqs6a_HU0db-osGm3fbkinpoUcfhCRz7ugkCoNScsm_Mh8S8vwSsgclLrgTzicvF0Li1oY9a98Fih_pOjPAWIN-xpeKv6vYP9ehSBWLNJVCCnIKYZbE1dqexRntbcISa3G_YQEm0NnAuvM6tmvXEX1721QwmvBP3vUCe5iSyYjxE43yfXCy3wUoqpn6iywMxdy5Y65ITevHwkN97E0qmguH7TdwxTvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=OYY5hZPC7CRhvbvi8xLgevsUlc1YsfJ109kd86y7uApFHD3lWfkAHO1t-A7NUOhwxZK95rmm7NDsuXeUdhGsquON6GeI1REtaIOUaaG67V6fZMOwl6ukl9Auqs6a_HU0db-osGm3fbkinpoUcfhCRz7ugkCoNScsm_Mh8S8vwSsgclLrgTzicvF0Li1oY9a98Fih_pOjPAWIN-xpeKv6vYP9ehSBWLNJVCCnIKYZbE1dqexRntbcISa3G_YQEm0NnAuvM6tmvXEX1721QwmvBP3vUCe5iSyYjxE43yfXCy3wUoqpn6iywMxdy5Y65ITevHwkN97E0qmguH7TdwxTvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسن عباسی:
زیر جزایر و سواحل تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69532" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFTmJ08cQESAdPQK3DEgcoVqofsdFZZVOtvaeMdDieHscxsB6ViB93xDryqWlyF73occC6aJGqZn6K7AqwLE0RqtPKHiee8a1CUNT65xF5tDq8WONz4rPVQNfZpGAWbcc5Wm1Ij_SYvkSv-Ud1tNva2po6bhi69bncKqxVN8ldUJl5qJI29QmJxyi7NAd6vA46T7CifTOqam6S7ydHrl8CSlAj6XNaBhOfBOsVXNo1E2j8vhRGLXDvn1I8U6PaSmV6Sr6lmZoywdhgNa2QFXOvgKA7ePn00okyV2gm_dlpXJ0EOl1Z_suB6N3d7iNF-3kGB0AGmO3w8JH0IT0HATuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/69531" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69530">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=udYjkV5Q73nj2KLGQkgW5rKbuOfTEUojatsUKgNDDUH92ow0ekeyFdZZaYd4t1Au86sCjaM4pLVbuYPCKmiX72B769ICS9RO9h9sCdsAA4yxrSxxuIrEIShAf3FnZimlBLJLEr1c2nKDscBjE0wrS6ko-aPOQmmhSCtznb5FjtLEuuYBvvpLI3pBi7v5NH2Uzd2UkQlt4IG-PiQs-Ae5HF3nrUIVh7yial8Qfd-Wto4yYHzAB1PzOSdI6vI1UoEwa3nN6R5yHE5dGMNSLxUOCbme9pL6bUocrzV7GAQwFlZFAEdAeuSo4BHXQwQh-NSEyTfmmT0rV-9YgJqsX0lBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=udYjkV5Q73nj2KLGQkgW5rKbuOfTEUojatsUKgNDDUH92ow0ekeyFdZZaYd4t1Au86sCjaM4pLVbuYPCKmiX72B769ICS9RO9h9sCdsAA4yxrSxxuIrEIShAf3FnZimlBLJLEr1c2nKDscBjE0wrS6ko-aPOQmmhSCtznb5FjtLEuuYBvvpLI3pBi7v5NH2Uzd2UkQlt4IG-PiQs-Ae5HF3nrUIVh7yial8Qfd-Wto4yYHzAB1PzOSdI6vI1UoEwa3nN6R5yHE5dGMNSLxUOCbme9pL6bUocrzV7GAQwFlZFAEdAeuSo4BHXQwQh-NSEyTfmmT0rV-9YgJqsX0lBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
غنی‌سازی اورانیوم چطور انجام میشه؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/69530" target="_blank">📅 19:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69529">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj4oWJGfuT3lgY1BMLeyLdpNMPs5QMtrXd4uBoPBhfwGjCBjSvnkG55J3aAmxl5RRsp5LNeIHDvn_xliiC2DxmeTcTdhKlnllQ-3myQ1fPkhGEm2sSUMe-9yDn2s7hsxlDpzxGo2arzcCCOaQQisZIjL5W_JmAiZ5ALJ6pRbReOdGUmsbcCGkfFcJ8U7xdrM36D5gOahXXxhTjo41xRE_8rsUMcwzG-OZhF-5UR6sp4BWQ7shCwHtR1ZYiJ4dcmk4UE4pH_viYuGXm6HTcA9qYmg-csagYen7TTBQC-kUz4_CpCSd1MFobLqGH93jf_lzdG8Mk2pvEvenitPJbbErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
"توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران درباره خلع سلاح هسته‌ای و تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69529" target="_blank">📅 18:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:  کشتی‌هایی در حال عبور از تنگه هستند. هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است. تنگه باز است. ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69528" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69527">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=JpSG7mXjcGPV-kL5ijjm7Kvk4SBl0egzQx4zFsO6QqpO9Jnda8ydHlvZXC6BnVpwDu2qVlyZpsPxmkkrgs0gWtdxDLeDcNndcUth9T1lAChW8ts8LolIFPrxRHnIodSXhcZYVMZmEUvzIzvS_ED6wXU2hsHrHPEU3cO6mW1pA0pLQqi2CY5Qrpbqlh3HsEdDKbCBRwzKnLuawOjL1PnM-TuT_eJXTqCKEqyOruRR2H3mEF5eCiAzqwuCYz57msE5hd6vQnpvNxd-WtuJe4R-eZUbmJLi_kZ6jcAi0oN-TLNnzsewqv0H9aV3OrRAxPNCWrqVvT-GS1Anb9sVnbLZjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=JpSG7mXjcGPV-kL5ijjm7Kvk4SBl0egzQx4zFsO6QqpO9Jnda8ydHlvZXC6BnVpwDu2qVlyZpsPxmkkrgs0gWtdxDLeDcNndcUth9T1lAChW8ts8LolIFPrxRHnIodSXhcZYVMZmEUvzIzvS_ED6wXU2hsHrHPEU3cO6mW1pA0pLQqi2CY5Qrpbqlh3HsEdDKbCBRwzKnLuawOjL1PnM-TuT_eJXTqCKEqyOruRR2H3mEF5eCiAzqwuCYz57msE5hd6vQnpvNxd-WtuJe4R-eZUbmJLi_kZ6jcAi0oN-TLNnzsewqv0H9aV3OrRAxPNCWrqVvT-GS1Anb9sVnbLZjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:
کشتی‌هایی در حال عبور از تنگه هستند.
هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است.
تنگه باز است.
ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت و هم‌زمان با حرکت به سوی مذاکرات بلندمدت‌تر پیرامون خلع سلاح هسته‌ای، امکان عبور ایمن تعداد بیشتری از کشتی‌ها از تنگه هرمز را فراهم کنیم.
در مذاکرات برای بازگشایی تنگه پیشرفت‌هایی حاصل شده، اما هنوز توافق نهایی صورت نگرفته است.
ما امیدواریم که این توافق به‌زودی نهایی شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69527" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69526">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=ZGGgM-bfV7htQPE3RC4nuhPHIEVDepCabgepZp5RYX07Y90mfwzunpuhR2mxE-t4I5XL0drbPMXAYPScPxDbbeicu51F4GSqn6Wzb6QiehgAYyNVO2mv8qfBXm6ZI7_FxvUtdgTS11gQuG2bDrhapnk_WW-E3rAr5iboAIWMEQaVSXVs9vZQWcM2QeYjT5fVW1q7dzMyzFnh88GPulRUw-plBle3n7PE7z4Iauie_jG2XKmDrGJi6zbjKSkbfXW4X7dXmh2-0YOvHomWteD8FZF1pA1DOo_YcRgbvWZXSxWcorB7j2TYBdkSoBhwPCgEUWiY2mwkvUXIbYKbq-gdqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=ZGGgM-bfV7htQPE3RC4nuhPHIEVDepCabgepZp5RYX07Y90mfwzunpuhR2mxE-t4I5XL0drbPMXAYPScPxDbbeicu51F4GSqn6Wzb6QiehgAYyNVO2mv8qfBXm6ZI7_FxvUtdgTS11gQuG2bDrhapnk_WW-E3rAr5iboAIWMEQaVSXVs9vZQWcM2QeYjT5fVW1q7dzMyzFnh88GPulRUw-plBle3n7PE7z4Iauie_jG2XKmDrGJi6zbjKSkbfXW4X7dXmh2-0YOvHomWteD8FZF1pA1DOo_YcRgbvWZXSxWcorB7j2TYBdkSoBhwPCgEUWiY2mwkvUXIbYKbq-gdqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو پاکستان، یه تجمع ضد جنگ برگزار شده بود که وسطش یه گروه جنگی اومدن انتحاری زدن در رفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69526" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69524">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoLNxFjeTX0C1tbLnrdSFINayZ_ZZtb_95QG1_M1qOg-w60eisyV6mhV3v3C-YQJvl1KS1bctFzTCRlYi7IJKVmuaENoWjj6Zuyec5__VxC5m3m8p-ZxGuNFsaa3lrYQPyWRtG3pqwsRoBFqnces_7QzyLYTyw1iSO8tDU0527qUxB3EX3iAIZoFqI36bT-_Zz1YCywmrYgy2f2_xVYHnHk3UNrkH-xsR54wf29CrhEiRcEEAqEoIdvUm1-p9x0mb0GS0slxIdEsWRGXy_lMJ27JuIJiYrfFkbsbCMzSlq37b2AqIf5kN62pLdKfrURB4hnihJ_76UZ7Evw5gLI-fV7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoLNxFjeTX0C1tbLnrdSFINayZ_ZZtb_95QG1_M1qOg-w60eisyV6mhV3v3C-YQJvl1KS1bctFzTCRlYi7IJKVmuaENoWjj6Zuyec5__VxC5m3m8p-ZxGuNFsaa3lrYQPyWRtG3pqwsRoBFqnces_7QzyLYTyw1iSO8tDU0527qUxB3EX3iAIZoFqI36bT-_Zz1YCywmrYgy2f2_xVYHnHk3UNrkH-xsR54wf29CrhEiRcEEAqEoIdvUm1-p9x0mb0GS0slxIdEsWRGXy_lMJ27JuIJiYrfFkbsbCMzSlq37b2AqIf5kN62pLdKfrURB4hnihJ_76UZ7Evw5gLI-fV7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به انباری از Wildberries در منطقه کراسنی بور در منطقه لنینگراد روسیه حمله کردند.
انبار اکنون در شعله‌های آتش فرو رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69524" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69523">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523118296c.mp4?token=e2DZR1gISX9m_ZUjeH7sz3ugPakAYt-vdsNrws2x0dNiKy9pORgKyxS39FPfrbqj3WMQa41sMsujtdeLfvlcAy_L_lMr8z3FVIdHCzdJBq5iBs0meAwlUpeoXrjvLYX0ZEDWrVFNJrYJBCUFNszEnCBRfqg0xAIps2f02Glg9btGJgxgrZub-WXFI7BbF9H_hL9sNZlOSBZn25Frb_IawuSBoczcZxkAfBizR3NL9sKQuKOmlQz7EGuUKSCFBd7Mx6CBTIwXE_FdDhHnruDST23WAaaOuffcPIcsO6kTsZFXacJiaXdtjTHlVR6whHzxFhi3vXSji71WwLXmAhs5Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523118296c.mp4?token=e2DZR1gISX9m_ZUjeH7sz3ugPakAYt-vdsNrws2x0dNiKy9pORgKyxS39FPfrbqj3WMQa41sMsujtdeLfvlcAy_L_lMr8z3FVIdHCzdJBq5iBs0meAwlUpeoXrjvLYX0ZEDWrVFNJrYJBCUFNszEnCBRfqg0xAIps2f02Glg9btGJgxgrZub-WXFI7BbF9H_hL9sNZlOSBZn25Frb_IawuSBoczcZxkAfBizR3NL9sKQuKOmlQz7EGuUKSCFBd7Mx6CBTIwXE_FdDhHnruDST23WAaaOuffcPIcsO6kTsZFXacJiaXdtjTHlVR6whHzxFhi3vXSji71WwLXmAhs5Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
خرازی برادر همسر مسعود خامنه‌ای افشا کرد مجتبی از استعفا های پیاپی پزشکیان خسته شده بشدت و در صورت تکرار اونو برکنار میکنه.
این اظهارات نشون میده جنگ قدرت بی سابقه توی باند های مختلف سیاسی امنیتی رژیم بالا گرفته.
بحران بدجور یقه جمهوری اسلامی رو گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69523" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69522">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800e043d01.mp4?token=LHH6ynFz_ilf12iVJya2kV8dwPjiR9GgKyCUspzU0A_PQr7Q62xSwxo-u3mURa-on_91k1R1GsB3fRJyC1VYysoJFRXQfDLHHtlMwev7GQ-9XvGuWyWV2wziI7Qp1gMDdCOVqxO9hA9eL2NWMiHk82kqYrIFP-G7zm98XzS5YixufwxiqMuhlRwZKzXigJ8hGbOCO1JPyQMmbDJv4zibpmrUCduDxj5iru73ulHZaaRPzR1D0brVAMmJ6jGv9YaN2xWxXYKFiODtVd6iK-az9AiHJQwIgJjjESl4aoPTXD8mtWmZGh1FTIKx7R0RJ1dESk4qxCKO4X8uOA1IeSDU_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800e043d01.mp4?token=LHH6ynFz_ilf12iVJya2kV8dwPjiR9GgKyCUspzU0A_PQr7Q62xSwxo-u3mURa-on_91k1R1GsB3fRJyC1VYysoJFRXQfDLHHtlMwev7GQ-9XvGuWyWV2wziI7Qp1gMDdCOVqxO9hA9eL2NWMiHk82kqYrIFP-G7zm98XzS5YixufwxiqMuhlRwZKzXigJ8hGbOCO1JPyQMmbDJv4zibpmrUCduDxj5iru73ulHZaaRPzR1D0brVAMmJ6jGv9YaN2xWxXYKFiODtVd6iK-az9AiHJQwIgJjjESl4aoPTXD8mtWmZGh1FTIKx7R0RJ1dESk4qxCKO4X8uOA1IeSDU_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمدباقر خرازی درباره بمب اتم:
«در اقیانوس اطلس بمب بزنیم و سونامی ایجاد کنیم که موجش به سواحل آمریکا برسه!
تنها راه حل نجات ما ساخت بمب اتم و شلیک آن است!
«با اطلاع»! میگم ایناهایی که با بمب اتم مخالفت کردن اون دنیا در عذابند»
وقتی ازش پرسیدن که حاجی زاده گفته ما بهتر از بمب اتم رو داریم گفت: «جدی نگیرید این حرفها را»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69522" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69521">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqaPPRCVQtksZkDyjCQdbkCJ15gKpF5yC7JuQjgCy20Z8hwHPnSpMkBNzfHhzwc0RTb8DPRb1kpy3IZaQ9BfmvHhqjr9QLIJYJv3Y_lRO1pwd22OznSjO021CvnNPg4Xu0TNRzIH22oJAF2PzqJPXtSMCJkNIsXUUdEKgaQYazrEvNhXro97TzpdBL9WEMnfP6EegScJOXJL501FnGY7ZiSyYhtBrcRVeVizcJAcGrU6p7Bh7Tmifkb2vypPb9FZuk2XOsueZTNYD2DzVv1HKPFXns0-MOfqrCZQUiqHes_IE7BGszhn5ogdEYntnqqFzGR82jYwOt5oAxKMKXDVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69521" target="_blank">📅 14:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69520">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇺🇸
🇶🇦
🇮🇷
سخنگوی وزارت خارجه قطر:
تلاش‌ها برای دستیابی به یک راه‌حل کوتاه‌مدت میان ایالات متحده و ایران در جریان است و متن توافق احتمالی نیز تدوین شده است.
این پیش‌نویس هم‌اکنون میان طرفین در حال تبادل و بررسی است، اما هنوز دستور کار مشخصی برای مذاکرات مستقیم میان آمریکا و ایران تعیین نشده است.
تمرکز دیپلماتیکِ فوری، حل‌وفصل تمام اختلافات عمده نیست، بلکه هدف، دستیابی به کاهش تنش در کوتاه‌مدت است که بتواند راه را برای ازسرگیری مذاکرات هموار سازد.
برای بازارها، این تحول سیگنالی مثبت محسوب می‌شود؛ چرا که هرگونه توافقی می‌تواند خطر تشدید درگیری‌های نظامی را کاهش دهد، از تنش‌ها در تنگه هرمز بکاهد و فشار بر بازار نفت را تعدیل کند.
با این حال، همچنان باید جانب احتیاط را رعایت کرد: اگرچه پیش‌نویسی وجود دارد، اما هنوز مشخص نیست که آیا واشنگتن و تهران هر دو آن را خواهند پذیرفت یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69520" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69519">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRCDGSqHFHOsIQJexOV0TOW4bwAH1GPUr94KJyBdZh56BsqziA2GZARVtO82Y0yiYDfm_BHvS08_QgqoF2T8STuXHVjfKzMhQaMlKu0Gn0nuK8Hd7vIZ__qs5P0kzpvfMVjCVoVPUj6VCKS69jx-BidEjUWL7gBKnbwhPfHebYXJVpbAbpfWonc1Blao1OKEauslWC7qVlXhCewtAhtsWseOUMTvIPdtrdx_DOUVnSjfeN3oFUeSMcUtuH5iILMQCkKECqyxJf4JBVq1NTqckPQA292S9_xTNXR4PKYu00_3P1r1IqAJ079n9RWYOKD5e7GLu3-E_Ai_9xNxBlDjGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هیئت مدیره شهرک صنعتی شمس آباد:
دقایقی پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
هیچ حمله‌ای صورت نگرفته و مردم نگران نباشن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69519" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69518">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=rG04TriBqzoKWTf3jQieAQwSnnfSBVC5y9AAMt0dxWAHYzkNplfylTMM1YdmDgGZu0Af3ry7jPkQLczXOgF4RVeTKaEMXLMSSI-_SNMp7_0_MPhVrpimSbo_ogOX0JNn7bIFudeHWZN62zAcqqZ0AbkqKzxC-8UPLISTKM4x1sdY1c4GUdRxRFOs6xgSSE3RT3hVnXMg_BDWD6POwLSJDxWN76roZib_j8CjiLiZHqy8pPWz2MfT-QLkUfUnyPZ90tz0VptaLYmylEA52Xom47hM374ETVh-DpQpAFnp8FiwTYGhyYNGjqNr0vvTdQZu0gO22dXJgwjTxQp8bzzsmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=rG04TriBqzoKWTf3jQieAQwSnnfSBVC5y9AAMt0dxWAHYzkNplfylTMM1YdmDgGZu0Af3ry7jPkQLczXOgF4RVeTKaEMXLMSSI-_SNMp7_0_MPhVrpimSbo_ogOX0JNn7bIFudeHWZN62zAcqqZ0AbkqKzxC-8UPLISTKM4x1sdY1c4GUdRxRFOs6xgSSE3RT3hVnXMg_BDWD6POwLSJDxWN76roZib_j8CjiLiZHqy8pPWz2MfT-QLkUfUnyPZ90tz0VptaLYmylEA52Xom47hM374ETVh-DpQpAFnp8FiwTYGhyYNGjqNr0vvTdQZu0gO22dXJgwjTxQp8bzzsmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69518" target="_blank">📅 13:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69517">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⏺
یک مقام ارشد ایرانی به رویترز:
طرح پیشنهادی تهران به عمان در خصوص تنگه هرمز، اختیار کامل بر تمامی تردد دریایی ورودی را به ایران واگذار می‌کند.
علاوه بر این، بر اساس سازوکار پیشنهادی، عمان تنها پس از اطلاع‌رسانی به مقامات ایرانی اجازه عبور به کشتی‌های خروجی را خواهد داد؛ امری که تضمین می‌کند تهران همچنان بر وضعیت نظارت داشته و امکان مداخله را حفظ کند.
این مقام ارشد اظهار داشت که بعید است ایران جایگزینی برای این توافق جهت بازگشایی تنگه هرمز را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69517" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69516">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vpxbuh-htMt8OpmjI-GPiE0dPOnDUglsRBFehg_bd25InJfAJulPBA_15Y5eRXbqt3kQKAgGyEQNcUqXGCp-HQCPjBQBxowM_Dtam3CQQ1fxUK9J_2Msq05E80mnI0YPCSf-c2LYVTEKZh86iL10_teZagCym_1MKdkd-pj0Lo0pbBkDNJdSR6wa_KUCUy1Ppr9HSp3mFwA3zVDsFAEIZvk0OzRmJ-bO6bY34R2jMD2t16oLlILwGZGeJGgXYHCxHiV69dCI6PneZs35W4Z-B37cNc9P0IAhD7svZ6idzR_0F1dwZzj3z4tUzqDOPN32DxNe9juNd_PUXiKTzgxS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69516" target="_blank">📅 13:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69512">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkoH9_TRDVLZW6qMzWrEFvBOZ5YkAg9qcBiX_1PU0k9JHwLkDgZJOcJ7AAVlbJmKzvYkxovcLLg5TBKHxujG50Uh-1zsthBR7c6qqsFweTs4Vr5apwn1doBF0uCHhB4tiJiRvj6epgd9m-TSQKnB1v6aJq7ch7KvWfXJtkJ-cdoizMW2LXhHyIwzKOcQVNmUO-OkCERTPdL2cGGezNYozxyG7dj-rin_6rUESdpt2G_PvWTqrnxIPI63q6D0EbYq6w1rT7UeaV8onW5XdjZNI5nOGMANb-bWuUQG6isWsftZFK5lHO2l56Hz9Yjs7nxyJ5St8EcAuU6qb_xTHsekKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooYHgtVTW-v1bIoZTXazfeMT9xK9xbdwe7MnY0xS7QOmUa6icgIQGWVYe8XvA7vXssO2sbDrD5GjMgsXpz4FGM3RZLQQvody15gEh1QOc2JXDeBC1Fr5u-nPmw6vCgfZV8kaQCMsMF4jl25Tvb-37F0ot-rpEXpJ7bt9ibFPTkbLNA-ftbJLxIlddf5fH-_LRUXC40coa3slNcdD-XFGFGGLs3cf2cLDj2mWVgRoHFQ-b_W82rfYqhXxt-juFdCKkaUp5WGhSqm4DGjgUcLH61JtDmIEdizNx6xB1uJ6KxVrLq6AaIAF6sn5q2BEKLQjubph_wDUYJ-uohZvQp52ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uyUAoLMPt7fvCdj-pGXLv1r4PDI0g2Z8bwqspp7NqrPd_ZoDq__X9rRLaAhJK73gOyKt1UPaTlY8aILvnds52VbEUDHmkHdyygw-UJcxm-vjPAeZ668pUI8wkwEMAlJ4tk28m0RLK9aqH6SkJqxN-9QHIemZWbG2ZN0FYwMKD5E9qnZiKqXO3UrhIB5uLrLWi90XEE4RXH6WjbTyuuDa-W72ROA1fz1l353grhjaStLrDEqWJosbpWVgC_0m1fSCWGM0AVPtEb24AzxVpuO5AGPhH6PPxlyKsr5CIUowuCZiDSAR8dJXctTz5-3rvPWJc3rNGiXJrpTODVdVWpku_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDwVJDVbQkug5AXhm392jWwZ4hFVDBA3DRVPbuTyjtHhc11_cV5RfrBxAea5mTJHVcEjc6J0rHS1bPkgjiDHN0UaJ5dlcHICsOYH4l2o_BFnxqRaaXMiS0xR24zVTPrTF7WxTvhfLppUjh9K_K_ESMItItkN2aEDkmZUX1VzIK8CrWPuPdhyWjH_E2SqA0fpA-aQhbL-J5pqaEj7veO9tobdSKb2ALVRPhURiEB3ZGj2qzsPi1KUhZLToFuc950eDCnP-_FqG4QMltXazrbXypXOhGgmPtoC_yaEJowc2Wok7JonsfiHMBslbQgb098QYED_B5664gatYgFw__vZXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
شهرک صنعتی شمس‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69512" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69511">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=ThNpQ_RlgC07MgPrS1Ie-l-5sGwJcUP48JmI0pdgcf-B9BOjIH-BUSGV45p9XnbQrsypJNf45Caa3RF7ta-LyF_tTo5pRFOnQIKUwNAb9G9o58aLk1uEZFWkY31ljxDmdxSbU9YEOXcQ0IT99SlrWip28tZBrPB6PqiChTvTldRj2nnvEm7erEVEmO1UuzgRJHkATOZ2apCFgIChzzg3tl9QT8XMb3Jeei7SbGquaMwA9t6gBBG5G2ziOUlNQUfKuLN8LeVfT1az77kZ1nxfMSdma4_sb0zp47FrOzYQnsavLlZO3qSF7mBee8g1yc6ah8EjmwMrpz1h92KoN2eTcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=ThNpQ_RlgC07MgPrS1Ie-l-5sGwJcUP48JmI0pdgcf-B9BOjIH-BUSGV45p9XnbQrsypJNf45Caa3RF7ta-LyF_tTo5pRFOnQIKUwNAb9G9o58aLk1uEZFWkY31ljxDmdxSbU9YEOXcQ0IT99SlrWip28tZBrPB6PqiChTvTldRj2nnvEm7erEVEmO1UuzgRJHkATOZ2apCFgIChzzg3tl9QT8XMb3Jeei7SbGquaMwA9t6gBBG5G2ziOUlNQUfKuLN8LeVfT1az77kZ1nxfMSdma4_sb0zp47FrOzYQnsavLlZO3qSF7mBee8g1yc6ah8EjmwMrpz1h92KoN2eTcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ستون دود در شهرک صنعتی شمس آباد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69511" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69510">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
گزارش های اولیه از انفجار در شهرک صنعتی شمس‌آباد فشافویه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69510" target="_blank">📅 13:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69509">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=BqD7fjJVbxIXL1yDcnjNomvl7o0DzHi6j6meAoXmhWq6gZt0EDoWCFzb6rlTYq0waqs4TORqrCeysBYpnIU5Z56-gjCaZpvBg83zEFmpkgwMW-GMWJ7ZMa0OWzgS0B7BSj_Q7HOxq5l60FzpLuPH8lz0lQE5jA181NZWq7O9gT_JAarvN6udfGeQBiANWtd6gFmW8ZiJVoh0H1xK9OfotMyqYpCV-xYmHSm00qIMHHsVycBVbG77wm_IzRicmg_4iib5P3URohs7i_6mvPZyXrG9DfRh7Rswk1NfkkwCO9CQx4QXvM5rInFcsZ2E2DbmtC93UIFvw23fBZ5bqpYfkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=BqD7fjJVbxIXL1yDcnjNomvl7o0DzHi6j6meAoXmhWq6gZt0EDoWCFzb6rlTYq0waqs4TORqrCeysBYpnIU5Z56-gjCaZpvBg83zEFmpkgwMW-GMWJ7ZMa0OWzgS0B7BSj_Q7HOxq5l60FzpLuPH8lz0lQE5jA181NZWq7O9gT_JAarvN6udfGeQBiANWtd6gFmW8ZiJVoh0H1xK9OfotMyqYpCV-xYmHSm00qIMHHsVycBVbG77wm_IzRicmg_4iib5P3URohs7i_6mvPZyXrG9DfRh7Rswk1NfkkwCO9CQx4QXvM5rInFcsZ2E2DbmtC93UIFvw23fBZ5bqpYfkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرودگاه رامون ایلات اسرائیل، پر شده از هواپیماهای سوخت‌رسان آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69509" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69508">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=t0b4SYJ5n4R4nNTq89GHcfOr_sBuIXJiJVl_Y24Jzj5MjhthrAKOlRM9wXRASCEfitEr_MXm4koxBEXHmdct8e7CXL80_8QSaD-iyXTeSMVUtZMfKw9YJBBGtbjYjdtso3wR5fsOEgILKcVHwcp2XqhSLNGojfKvieSfr7fW6cbPXzz9CWdJg3yYn6hT68ERvnoZ6J-iwB_SEgaZzCL8qVzYjdtEu7l04CLfJmeWKGCkiwqr7alDvlfbyc75KiXU4fDm3TnMczte_gdbme3fL0WLKXq-CYSlep3HVBie8JVp6LotAJGRA7_-xfcYVweCICYMKZChxRZXvFEqvdBWzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=t0b4SYJ5n4R4nNTq89GHcfOr_sBuIXJiJVl_Y24Jzj5MjhthrAKOlRM9wXRASCEfitEr_MXm4koxBEXHmdct8e7CXL80_8QSaD-iyXTeSMVUtZMfKw9YJBBGtbjYjdtso3wR5fsOEgILKcVHwcp2XqhSLNGojfKvieSfr7fW6cbPXzz9CWdJg3yYn6hT68ERvnoZ6J-iwB_SEgaZzCL8qVzYjdtEu7l04CLfJmeWKGCkiwqr7alDvlfbyc75KiXU4fDm3TnMczte_gdbme3fL0WLKXq-CYSlep3HVBie8JVp6LotAJGRA7_-xfcYVweCICYMKZChxRZXvFEqvdBWzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی روسیه بدین شکل یهو یک پهباد اوکراینی اومد خورد وسط مردم لب ساحل و 6 نفر کشته و بیش از 40 نفر زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69508" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69507">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⏸
مستند از شب های تهران قدیم که در دهه ۵۰  تهیه شده:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69507" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69506">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu6J6aa_KTYz8RKJvRCnsdJKqPd7U9X7sWXXpo2QKJMRjECN3bHGBQcbgGKyLcUf-TTbSTeh8_bl6a19VQJ-gbez2dFx0SIvCWapl4NXT-9jR8wEv2ZmXw_TboS2NZW3cUmLVkqDkDZRR-OV4bt--Fj228AvG0IAEQ78ygGl8TiY8suLwuW_jVwavZOheeewb9P0dBpiyRS-C5Y3ZQy1Jz9tBnDmfMvGZUdYjReRSxvtMUUTDMsCqPvGKGr7i-OsUj6-viP7TDdX66tqT55kXObORdS9965lhgE1QTo603Rh6lkSx9yhV1pxojYQhf4O6Qfjo8quQXtMG15sYM52zFCo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu6J6aa_KTYz8RKJvRCnsdJKqPd7U9X7sWXXpo2QKJMRjECN3bHGBQcbgGKyLcUf-TTbSTeh8_bl6a19VQJ-gbez2dFx0SIvCWapl4NXT-9jR8wEv2ZmXw_TboS2NZW3cUmLVkqDkDZRR-OV4bt--Fj228AvG0IAEQ78ygGl8TiY8suLwuW_jVwavZOheeewb9P0dBpiyRS-C5Y3ZQy1Jz9tBnDmfMvGZUdYjReRSxvtMUUTDMsCqPvGKGr7i-OsUj6-viP7TDdX66tqT55kXObORdS9965lhgE1QTo603Rh6lkSx9yhV1pxojYQhf4O6Qfjo8quQXtMG15sYM52zFCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش‌هایی از گفتگوی ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69506" target="_blank">📅 10:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69505">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=vcTrgnrJxQv9m8CrPWE5k7Uq_-aBUn8lcFBl7qvcM69kBchXNNFwS4i-Eicf5h6Q6e3jIsIqzj-ENRP9NlXJElWMpKPAiBOdngZ6jayGEU0ds8q7iJF7umtjA2ixXI4l45d7Dbv_F9--Jm0rKVQR5wBOrtrSdlclybboo4xBF3zO6ljdUvEn3G_PzapJk6rbUz2w7GKLwDBE9m4l4tToF7zYyGjuKkvIX18gcZ8ciTVf5jcm1KfQs2wrpUCVGq0TOFnEPB6mqj1Vup4r98gzcP3jxPuKf5Daie9vkxS_N6LIHckYsT5EfQDOzCeNoVlVn0UOvrekDuHJ9zyFrGpsL6S9N3DRy-DYbi4fKBMO-8DMxnkZ6Uyy0eiWXgzX2vRh9clI4q3b4OoVoVDWS1L8P6wtzRGv7gK_wXa6P8d6hUCstMdODuCTacKq17pSZAx_r_CG4DdWtG3YHuKhzg2rgELMG6vlKVGFbQA8l3l7H0sLcwztBsiVk07YKvwp0Ts3_uQCFrd2YDh1guS5Bu37XjoQdvS0iTBTwoY2cuWjduqjiRXOmDs-GF5SKHJeX24R10PfRbc3rD9nDFniz8hZ-c5V5pi3qybmJrSLWC0ss5flznzBGHHhvxOWsaP2oTE7RQDqrZxsu79kl7hyFPgFI-7iOL1aRpxEjAeq1JZa8v0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=vcTrgnrJxQv9m8CrPWE5k7Uq_-aBUn8lcFBl7qvcM69kBchXNNFwS4i-Eicf5h6Q6e3jIsIqzj-ENRP9NlXJElWMpKPAiBOdngZ6jayGEU0ds8q7iJF7umtjA2ixXI4l45d7Dbv_F9--Jm0rKVQR5wBOrtrSdlclybboo4xBF3zO6ljdUvEn3G_PzapJk6rbUz2w7GKLwDBE9m4l4tToF7zYyGjuKkvIX18gcZ8ciTVf5jcm1KfQs2wrpUCVGq0TOFnEPB6mqj1Vup4r98gzcP3jxPuKf5Daie9vkxS_N6LIHckYsT5EfQDOzCeNoVlVn0UOvrekDuHJ9zyFrGpsL6S9N3DRy-DYbi4fKBMO-8DMxnkZ6Uyy0eiWXgzX2vRh9clI4q3b4OoVoVDWS1L8P6wtzRGv7gK_wXa6P8d6hUCstMdODuCTacKq17pSZAx_r_CG4DdWtG3YHuKhzg2rgELMG6vlKVGFbQA8l3l7H0sLcwztBsiVk07YKvwp0Ts3_uQCFrd2YDh1guS5Bu37XjoQdvS0iTBTwoY2cuWjduqjiRXOmDs-GF5SKHJeX24R10PfRbc3rD9nDFniz8hZ-c5V5pi3qybmJrSLWC0ss5flznzBGHHhvxOWsaP2oTE7RQDqrZxsu79kl7hyFPgFI-7iOL1aRpxEjAeq1JZa8v0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
مستند جزیره خارک(1345):
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69505" target="_blank">📅 10:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69504">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=JNj6H_U_N-UUz3wMeQuG8gkhSUqitJISUGNttY7Zfow6DSFNB1VlwL8iOSI2qRxAahZ8Q-CKfh7DSpcqOuCumBUpU33kB16a4uvrsu6bEHPbmAr-isMjy8KYa1MGKtuFEqSRBrfZZ_nrBlqrwlFcxJ_8NdyDsjGoMEcvoH9sMznKPYGmXD5weLZUiF6J7fSplv1qPp5BVuY0LBepPQmh35LGr-lMRNCQWES7gZJ-JEC69BqC09qRGgggS15A3E1kWBoXrA2NAOMrJa2VHUZ34pMmJ42ey6U0KZyKNLSBHgY7Qn4-EgTI04xttgSXNb1U1tAX7HWkkwwM_y-Zyn1e9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=JNj6H_U_N-UUz3wMeQuG8gkhSUqitJISUGNttY7Zfow6DSFNB1VlwL8iOSI2qRxAahZ8Q-CKfh7DSpcqOuCumBUpU33kB16a4uvrsu6bEHPbmAr-isMjy8KYa1MGKtuFEqSRBrfZZ_nrBlqrwlFcxJ_8NdyDsjGoMEcvoH9sMznKPYGmXD5weLZUiF6J7fSplv1qPp5BVuY0LBepPQmh35LGr-lMRNCQWES7gZJ-JEC69BqC09qRGgggS15A3E1kWBoXrA2NAOMrJa2VHUZ34pMmJ42ey6U0KZyKNLSBHgY7Qn4-EgTI04xttgSXNb1U1tAX7HWkkwwM_y-Zyn1e9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
محمد باقر خرازی:
اگه پزشکیان یک بار دیگه استعفا بده، مجتبی خامنه‌ای موافقت می‌کنه
.
مسعود پزشکیان تا حالا نزدیک به 28 بار یا استعفا داده یا تهدید به استعفا کرده!
قراره ذوالقدر رو از دبیرکلی شورای عالی امنیت ملی دربیاره و محسن رضایی رو جاش بذاره.
مجتبی به عراقچی هم گفته دیگه به هیچ عنوان حق دخالت تو مذاکرات رو نداری.
همه اینا همیشه تهدید به استعفا میکردن ولی از وقتی مجتبی خامنه‌ای تهدید کرده، دیگه فیتیله‌ها رو پایین کشیدن.
ماشالله مجتبی خامنه‌ای خیلی سفت و بی‌تعارفه ، پدرش یکم تعارف داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69504" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69503">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfsNwtIEECXRu3eyqLcUoOC9i6wVb2WN1m4-BmRm0G1RMWEEeM1ZQXqmo-AORSQy7TTeI7UwHMo7FRjJBnvl6bmBsBjx7izOM2pUBEuybFLZWggMJExqCq2AamH8Vhe1zIL4uc95B5i2aEyuKUckArclOQ3b88_Laso-iG1FXTrGxquAr51_cOjHVLPaZgocJa9Ug0L2vXKVUDeQTj2W5gXm42OBuuRXY3mZyVTncPhQumwlTYkGz2wHESppj_Uh__YvUZxnbUs5FUVzW1Nr4iAiiHTYf1ZkIolUPSv-zk4DIbPotbEPYsJz0ssntNvkWPUy0U_uKZ3U288XFavMdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک کشتی باری در فاصله ۲۰ مایل دریایی شمال شرقی «الخصب» عمان، از طریق کانال ۱۶ VHF پیام اضطراری مخابره کرده و مدعی شده است که مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69503" target="_blank">📅 03:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69502">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های حکومت از حمله به یک پایگاه آمریکایی در شمال کویت خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69502" target="_blank">📅 02:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69501">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db881c0183.mp4?token=ixtSiEJx8N8GdIb8Xe9h1mQ3D6KwUXN7eV8JK0LF9P6ZspGNRkSE2tyn630KHJMFok_62B8d86eEoWtJuseewZdvkLhumYtSZhzKn7oM15p2Xo8qxX0HSuuAc4DmTQwcFVk3oCpdyfkcl0dgjhfjutws6F4ulpAYUXoayqrm5VQrhan4ItirfES3sBeyu8QJNJTWDdHkOAukIxfB_fTLPddG-hRFHW2ugGEpr3a_u38M47-cFszM3HleAQb8pMtnpJ6x27C0gMbwyE6jhPxsGci_OsH0g2NN2z1txN82duyCVeebr0XAtn3417LNZdxp1S20TQGocDePXlDzNT6D_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db881c0183.mp4?token=ixtSiEJx8N8GdIb8Xe9h1mQ3D6KwUXN7eV8JK0LF9P6ZspGNRkSE2tyn630KHJMFok_62B8d86eEoWtJuseewZdvkLhumYtSZhzKn7oM15p2Xo8qxX0HSuuAc4DmTQwcFVk3oCpdyfkcl0dgjhfjutws6F4ulpAYUXoayqrm5VQrhan4ItirfES3sBeyu8QJNJTWDdHkOAukIxfB_fTLPddG-hRFHW2ugGEpr3a_u38M47-cFszM3HleAQb8pMtnpJ6x27C0gMbwyE6jhPxsGci_OsH0g2NN2z1txN82duyCVeebr0XAtn3417LNZdxp1S20TQGocDePXlDzNT6D_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69501" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69500">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
منابع عربی:
شنیده شدن صدای انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69500" target="_blank">📅 02:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69496">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCkqY-av2FRmDYXJQa6fXIG3jOr81zmJJKeBzBOsbnpRSes4DwcfQZvacBNDGQNuJhs3dC917oDSifAfxEMmLPUUgP-_CgRA9eApT13jWe8P2FMmCJO1VR68_HfbUVwpqGdCw2uUDeGDp7rOPmVrSxNBJTGQ9ZByvIrtX22TiCXsgrdtN4Viz0znpHfQ1wS59ZJmj5aacFVEnmhCrIzncP5iPe9XhNHsjV7zQ3gd2Vk9XPhaNDR5RAvdBq6rFCyYq_wgJZaEQR-yY45BXm8PXsvoSTcV0-TQQNvj-gAw7pF46gF_ycCmh2pgX7YmC0P3DW-LYiMwysoriwNgKhwZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=jXUF6AW_Tim2kVDP41_W8ldoZzOo5YvYlmeT9pP4L_cNP-IAAx6nr5MCIVCcJqnf6-e7M3kJvQy32NeYdCKuG6iaRhVvy3Cc5QtoN8QweXWWVYQH5yrbcHwfK1dE8gO4JyXeNVLoZPGUxvTbhJbYHoqknE25mciUvbX0I64-4YKm5LalJophBUjkq3a0wQ-0UG3YkBYFqgPsxXfyjF7jogcs2FVFNZ5n9n-x3u7RTnnKIJBfRcSgoB6GE8JZe4dh2wUcXvaCKMUqCGJ6Fg5lNGxQP9Wj2pnmXETljBeVvS5rm8rR5uLJ5KqhTEU2yOSQOPoS6C72wUkVmBi-5dXcDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=jXUF6AW_Tim2kVDP41_W8ldoZzOo5YvYlmeT9pP4L_cNP-IAAx6nr5MCIVCcJqnf6-e7M3kJvQy32NeYdCKuG6iaRhVvy3Cc5QtoN8QweXWWVYQH5yrbcHwfK1dE8gO4JyXeNVLoZPGUxvTbhJbYHoqknE25mciUvbX0I64-4YKm5LalJophBUjkq3a0wQ-0UG3YkBYFqgPsxXfyjF7jogcs2FVFNZ5n9n-x3u7RTnnKIJBfRcSgoB6GE8JZe4dh2wUcXvaCKMUqCGJ6Fg5lNGxQP9Wj2pnmXETljBeVvS5rm8rR5uLJ5KqhTEU2yOSQOPoS6C72wUkVmBi-5dXcDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقای سیاه‌پوستی که تو تصویر می‌بینید، رکورد ویوهای تیک‌تاک رو جابه‌جا کرده
👀
حالا کارش چیه؟ میره به شهرها و کشورهای مختلف و دخترها، زن‌ها و دوست‌دخترهای مردم رو بلند می‌کنه و باهاشون مثل دمبل وزنه می‌زنه!
جالب‌تر اینکه تو بعضی جاها، دخترا حتی صف می‌کشن تا نوبتشون بشه که ایشون بلندشون کنه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69496" target="_blank">📅 01:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69495">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b93335655.mp4?token=P2CHM4ja_hb22cG85x0hwWDEyoBo-s6ST6p8Mx3yXJG7dnHGZlGpKMd2Rb7N_HmHpGFw5vnODiTyB4qk89IuyseKhsa9S4xjR6mecYhtEduNFUiP-gOm-ATra2EbblPSpAbR6xsrg3Q04Qm-ANdmn2Qb5xo3TB6Z0dIWXZj74eUMpRXvwr4RclYiNGiKrkcvZ0Ms3k_Y1mq_oK5CvTA6wdr__MP3ehCnq3qWEMneT5yMmcuUhIFzfy2yAp0CqUTcwIanCeO63YDzzQ7xMvS9XVmWqXXsCjmPH8E8zckxJXRQcpWspyc44JXmsdQa3aMsGVT3bQvuff-ADh2dotozIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b93335655.mp4?token=P2CHM4ja_hb22cG85x0hwWDEyoBo-s6ST6p8Mx3yXJG7dnHGZlGpKMd2Rb7N_HmHpGFw5vnODiTyB4qk89IuyseKhsa9S4xjR6mecYhtEduNFUiP-gOm-ATra2EbblPSpAbR6xsrg3Q04Qm-ANdmn2Qb5xo3TB6Z0dIWXZj74eUMpRXvwr4RclYiNGiKrkcvZ0Ms3k_Y1mq_oK5CvTA6wdr__MP3ehCnq3qWEMneT5yMmcuUhIFzfy2yAp0CqUTcwIanCeO63YDzzQ7xMvS9XVmWqXXsCjmPH8E8zckxJXRQcpWspyc44JXmsdQa3aMsGVT3bQvuff-ADh2dotozIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دست فرمون پشم ریزون اوپراتور اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69495" target="_blank">📅 00:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69494">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0M1cRAVXXtOqrlJshwgt54Ng2XiK89459lgEJnig_yckuvEFuKAxMuMrwyz1KAp7HBx8YbjFzUjgQ-7GO3TPfvV5tZlF1kthJVTTdoOzHocvVbrYFWQm6PRVtdDbKZAIaoRdKa9aY8gHeiozH1fIox8pl9GWMHIcsTeU4a_2A8u2rylPh1lfBV1SoVwrHeKyTGkxyldaRzETJQS6O27wx1RzHaOh1ufRRzE-v4aHMY4i3JtdWbILfBV65mTP3ioqlvLBK85rzOQS0umhAtldpI1Q8rlh8qdpEF40jNKALAqxoEMsPaLBdQUEwFgdChQUJ0xek1e1FaWeUjBIft6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
ایران هیچ‌گونه قصدی برای مذاکره با رژیم ترامپ ندارد. هرگونه اقدام تجاوزکارانه با پاسخی کوبنده و قاطع از سوی جمهوری اسلامی مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69494" target="_blank">📅 00:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69493">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=Y3aV9uVSbwvcpcGym2d2tDlpLwRXf12-dtUOaRPAU7PIBA2cPG599uQ-wdhqrWj7k2ASATigdpg820MFYGn8objuRYp_AUurC7eLYOORFE0vkmWP5M5rqU1WrS9UcR7HmvbbwLxok18hcgacvfKx1MNXGjA0nMoXxddrPL4t8M6Den6Gd4K1UPI75wvgOagaeiYBagRU77rBBRQqEMIkzurYn3SkdxXldp0htiEagjP5GHnCsdfUtY_DuXsJ1lVFyc4ac2VcX2qcMuoGfJF-ECDPWpc3dGvQASXbXpwNB_RXdtka5IALPtqMeOBbSGWNjPxAklqPrIlHCkvIhQk-Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=Y3aV9uVSbwvcpcGym2d2tDlpLwRXf12-dtUOaRPAU7PIBA2cPG599uQ-wdhqrWj7k2ASATigdpg820MFYGn8objuRYp_AUurC7eLYOORFE0vkmWP5M5rqU1WrS9UcR7HmvbbwLxok18hcgacvfKx1MNXGjA0nMoXxddrPL4t8M6Den6Gd4K1UPI75wvgOagaeiYBagRU77rBBRQqEMIkzurYn3SkdxXldp0htiEagjP5GHnCsdfUtY_DuXsJ1lVFyc4ac2VcX2qcMuoGfJF-ECDPWpc3dGvQASXbXpwNB_RXdtka5IALPtqMeOBbSGWNjPxAklqPrIlHCkvIhQk-Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
آماده بودیم به ۳ نقطه از اوکراین حمله بکنیم ولی عذر خواهی کردن کنسل شد
پل های منتهی به هرمزگان رو آمریکا میزد که حمله زمینی بکنه ولی خب طرح هاشون ناپخته بود
تو ۱۷ روز با حملات شدید موشکی پهپادی ترامپ رو مجبور به شکست کردیم
آتش بسی وجود نداره داریم حملات معقولی انجام میدیم
تفاهم‌نامه با موافقت رهبری امضا شد
کویت رو ویران کردیم و فرماندهی سنتکام از قطر به اسرائیل منتقل شد
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69493" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69492">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571743cf02.mp4?token=Q8l4qBgMf4iGqgNppj6v-3Sz2xWxWvTrkhNNAn5rVlmUYh5c2q6XmPfvGGoT8JlHGoy-gK49tO4lO4NJxh71Yu2r5JzZsrT96hHdL3zuPN_0puJApZ4jkwDyuqj7hykb6FuTsgN-5s-iFPDqENALHFtRG_G63M7EY6OHU7_TpqDsePdLm3rdetN_MBnt6O9V_WhMiaMISSK4n7UeszHTOipB40lKJCSFCxEC12AqHCBgMT9b1lc5_vrWVT4W860tPOgXIhdcsJBw27EUdTv_kgYXOCN-FjXbw0MIDnBhRGppXwPUUzDFkf-fHEhtC4H7rnw1xKuIjPeh5MdoQFr4DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571743cf02.mp4?token=Q8l4qBgMf4iGqgNppj6v-3Sz2xWxWvTrkhNNAn5rVlmUYh5c2q6XmPfvGGoT8JlHGoy-gK49tO4lO4NJxh71Yu2r5JzZsrT96hHdL3zuPN_0puJApZ4jkwDyuqj7hykb6FuTsgN-5s-iFPDqENALHFtRG_G63M7EY6OHU7_TpqDsePdLm3rdetN_MBnt6O9V_WhMiaMISSK4n7UeszHTOipB40lKJCSFCxEC12AqHCBgMT9b1lc5_vrWVT4W860tPOgXIhdcsJBw27EUdTv_kgYXOCN-FjXbw0MIDnBhRGppXwPUUzDFkf-fHEhtC4H7rnw1xKuIjPeh5MdoQFr4DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی وایرال شده از موکب خدمه ام‌البنین که به زائرا آیفون ۱۷ و آیپد و گوشواره طلا میدن!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69492" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69491">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9Pl4aYF7ll96BbtIZ9g9CxfchwNsMF35BhJvB_aXoc9dtdOX_H1RWzFDnw7_1a7mDOJWry6UdiPEo8pu0m6NYZA9ku6TlqzFeOzi68voweCUucARuJR409-c1GwiXsVrFjqt0bHIb5omEaENofAdQ19iQjIVLHTGSIXwkaINgEjYKigQ1KdRIU3AIUU9lP-aea6rb46AhMLxshP4HNmxTxzf-F7G5wyVg0KTVE1IL2_-FFF9690Jrb7EU8JK_g-uG2WyxvhNyyDrAB3C5neDzM3VBJr0ijMiNUS9mAfanf1gu9d9nlKr95TocfIxZW7R_oh4X7UYdkv0zpb4Xqq9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتونی
ویتنامی و اروپا
رو از شهر مرزی
بانــه قسطی
💳
بدون ضـامن
بخر
👇
👩‍💻
https://t.me/doniakalacom
کانال تلگرام مجموعـــه بزرگ دنیاکالا
📱
https://tlgrm.in/doniakala
بزرگترین
واردکننده
🚚
کتونی در ایران با
سـ۳ـه شعبه فعال
💊
کاملاٰ
طبــی
ضـد زانودرد
🦵
کمردرد
🩻
اینستــاگرام
مجموعـــه دنیاکالا
📱
instagram.com/doniakala
✅
ضمانت
کیفیت
💸
قیمت
مناسب</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69491" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69488">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7ddVY7ZJdLy8RcgZlFpRtWDrmAd7cnsQdQqL0YNkaI1mkOI1B6FOYls0gluCL4prOWooWO6rQxeo6doeEMetYqKRY3N58JWxvnCjZeOlBzoTKfjo9QlfniyYS2yQcDQ8PYnCdzMpthmDLSRmJBstPS4lEFgUI7sMA3xngSZFgxm80ajRtXtc1MIFjQiD8EKpay01KW873lVdSVXlETE09S2nKBu_vG8oYjYyXYVhv-ilkqC-3JmrukMPQ3xPYSljMZoAOxrM6gMzbx95Vbra98yKQmGQh77Ifxkdhl8Jku1pcVqwbWQZ7VeSDGNYjGr7MQcOD_ayDZi-2ZwQ5xcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVOXxYhQBQaGx_6u2NTU6-tM1mEfq1lXmf0vl52aTbJx29K_uLsm7s70CUQ8m9amix4UjAT_wjeqsLIb1DFwiwgx2U3JwL7OfCCmTVXi2nzB0-V-q-dDaWG1tlUCDgw31l2dPuYPmCpbdGK_hFdS2eURNO1mLoFu33s_GFrTNB4-PHeFAhN_hYcLiU1UFBVuXPqTCTBXnnn-nLKyS-LRwrCZ9TMsJuScxJirsxDhlODn1uNraH3hYNwxsA3ryv3_6yRMTSLJW3vcozPTex4aFl-WfQTUNCYdVsq09vPZ9GB1q1HnyF71HrP_CCOfsHSAyGV-Tk-6Xe_-NlAV9m7KTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTg8sFH5hOz91J_p4ugKiAiRUuxSg0lRp-1kngXO2tqpwtmvO_WpshCI63DU9QXKP4uolNP_WCw2Eyxkv6Psypes1jYuxHfU5E9ncuxxfUgP_lCCtAjGzCSmP2tNH_7zuGoMj0BCsKs8RmIR17OxwTv2BJ7Hmhvq8iS7ksltHsOiqrPWrkOOkIPTTw8hgjvuvDOCD358f1tMoyDnVoD_8GvF9soZoO1VxYiUUqgfgIjErEoZi0Q8cZJunD1gQl6u0whymwCFJQgq5eeeg9cAXtGCYX0RD1PTieXa3WPr3l1SfH81BYYPDm_pYsNmH2UQXdwuKpx7r5OVtATpJVz0PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
کامنت های دردناک مردم زیر قیمت PS5 تو سایت دیجی‌کالا
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69488" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69487">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=OjCVPkMa2DpUq8RiJCfN85JHf0qhoEIYZCM_MxqCnYQ5K7PCq0L6DmfYT68p2F9bjQTRVVVW5m8iDigX8Bsq13eb7jWcvxojBw5ksZ44y4WI6-WnDwYsBsLh_Ocjo4AXwzH-RqgvnXvbG8Pxldnfa_tJP3ftI5gaPC0F2_yRxmqdxioiypWqZWor2l2Hir1Ds_5aR2NFs7ZP8pOUuJOQHgAIY4aXqh6YG_DAcdszV2h9-GdT7saXTOX4ERRhPdXk4okoPIylTey9zNE5B7QJAVSLXUiOGyOi38Qb5Yf4Xa0yJRXg8EnVyVVyRmxmjA2PyYWlz7ahx7BH_PMKEx4URQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=OjCVPkMa2DpUq8RiJCfN85JHf0qhoEIYZCM_MxqCnYQ5K7PCq0L6DmfYT68p2F9bjQTRVVVW5m8iDigX8Bsq13eb7jWcvxojBw5ksZ44y4WI6-WnDwYsBsLh_Ocjo4AXwzH-RqgvnXvbG8Pxldnfa_tJP3ftI5gaPC0F2_yRxmqdxioiypWqZWor2l2Hir1Ds_5aR2NFs7ZP8pOUuJOQHgAIY4aXqh6YG_DAcdszV2h9-GdT7saXTOX4ERRhPdXk4okoPIylTey9zNE5B7QJAVSLXUiOGyOi38Qb5Yf4Xa0yJRXg8EnVyVVyRmxmjA2PyYWlz7ahx7BH_PMKEx4URQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
✈️
یک جنگنده F-16 نیروی هوایی اوکراین، یک پهپاد انتحاری روسی (Geran-2) را با شلیک توپ ۲۰ میلی‌متری ولکان (M61 Vulcan) در آسمان اوکراین سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69487" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69486">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22887d7155.mp4?token=gGTRtTmuYiRsj3-gInBmYMuqRKGl_dgvOXoP_-lHXXcgVI9Z-NSh_lk13xTokFcztn_LAtCkpW1fACYGZKRHJ1rFuajlOh1W245PCmahaRlkORQYRAiIy_fLzQrk_YfCV_D5y7kIZkfkWMuvK-MWF4qLCV3fIl8MPNm9Z1bCDRaNXWfq1Gx5BQ6i2o6f44yHr8XStcJZT8pTwOv4pHKx5pZh5JyUNd--6JKg4Q8q_XLOmIc40o576tpMtIgcQLhvCfkiv9CeN7vI2vYBKm1BzzacvfxLeTgKf0HhNYx3nEmS3fIPZ5cbC-QHyTDiQ-OAHLxHmqo4On3xM-K7Y9JT-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22887d7155.mp4?token=gGTRtTmuYiRsj3-gInBmYMuqRKGl_dgvOXoP_-lHXXcgVI9Z-NSh_lk13xTokFcztn_LAtCkpW1fACYGZKRHJ1rFuajlOh1W245PCmahaRlkORQYRAiIy_fLzQrk_YfCV_D5y7kIZkfkWMuvK-MWF4qLCV3fIl8MPNm9Z1bCDRaNXWfq1Gx5BQ6i2o6f44yHr8XStcJZT8pTwOv4pHKx5pZh5JyUNd--6JKg4Q8q_XLOmIc40o576tpMtIgcQLhvCfkiv9CeN7vI2vYBKm1BzzacvfxLeTgKf0HhNYx3nEmS3fIPZ5cbC-QHyTDiQ-OAHLxHmqo4On3xM-K7Y9JT-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که میبینید ۱۲۶ سالشه و اهل کشور برزیلِ؛ در زمان پایان جنگ جهانی دوم تقریبا میانسال بود
این بدبخت نمرد تا جنگ جهانی سوم رو هم ببینه و دبل کنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69486" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69485">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
آن‌ها با من تماس گرفتند و گفتند: «لطفاً حمله نکنید. ما توافق خواهیم کرد.»
این حقیقت محض است و همه آن را می‌دانند. چه کسی تماس نمی‌گرفت؟
کسانی که اطلاعات را به بیرون درز دادند کمک کردند، چون شدت حمله را فاش کردند و ایران هم از آن آگاه شد.
آن‌ها می‌دانستند چه چیزی در راه است.
قرار بود دیشب [حمله] انجام شود و مدت زیادی هم ادامه یابد، و [در نهایت] چیزی باقی نمی‌ماند.
اگر فرصتی داشته باشم که به افراد زیادی اجازه زنده ماندن بدهم، می‌خواهم آن فرصت را فراهم کنم.
بنابراین، هیچ محدودیت زمانی‌ای ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69485" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69484">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20068f370b.mp4?token=HCnbcJ4uqycU6o9YEzz4_LKqyqNvE7ggyeVNaLxZtqyPaXX6wKnpW0p6pgXR98-9ABkwajRGgBO1RbcwK4DMF7mbwnOs0Y8rdfG0wPrHdJkbPrrrNzcp0yfAH-So52OhyD-FOlqmnAzGkzO-k4SJYLE82-WeuoSsrdb0IRx4zoiccDnB-afeIk6vGnImHsX7drY7LLUTBQIo8WPyQlnyPZRWlcdm43e3lOta6XHGuyo_7YOdtFEt-PaI8RFY7YHIIw_L1d4MuSFcPC3n5JZUiYj5_9vr-QtWZdukXTVEzv-0JgGqx_VjmU-wpq7-CUcHXWun83gFaXi0JTQhYxRmAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20068f370b.mp4?token=HCnbcJ4uqycU6o9YEzz4_LKqyqNvE7ggyeVNaLxZtqyPaXX6wKnpW0p6pgXR98-9ABkwajRGgBO1RbcwK4DMF7mbwnOs0Y8rdfG0wPrHdJkbPrrrNzcp0yfAH-So52OhyD-FOlqmnAzGkzO-k4SJYLE82-WeuoSsrdb0IRx4zoiccDnB-afeIk6vGnImHsX7drY7LLUTBQIo8WPyQlnyPZRWlcdm43e3lOta6XHGuyo_7YOdtFEt-PaI8RFY7YHIIw_L1d4MuSFcPC3n5JZUiYj5_9vr-QtWZdukXTVEzv-0JgGqx_VjmU-wpq7-CUcHXWun83gFaXi0JTQhYxRmAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در مورد ایران:
می‌خواهم قبل از نابودی کامل، آخرین فرصت را به ایران بدهم.
امیدوارم سر عقل بیایند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69484" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69483">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T7jFCGxqemU30TfobPChWCA27Dw_C3fFrOQo47J2U6XszILtLbPC9F0T-Ro-c98P6oS7j8rz2S1_9XYP3i86UHC1vH7jIkrGs1goztiX02EdBFrP9CLHksQtABFnAGo3RQfOph8AvMTHQ7ZiDRCP88YDUjIkcJGU1YH8sU_gr8Y5o1FT3KEkvGkm_RHjPtP7ftV6wjmkZEl1J3fcMA1vjyhIFiEKGGphmGjTW9bw15ppMm9rVL5fmTPi77uFwlRFePiMEoz0Z-LKDlhUAGJgmRvr4qf6dDdDEDL1-oEC8_8_LCWaEDh6izsdkEWJzQf3zo5H0kqQhNMU10A6a7mH7dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T7jFCGxqemU30TfobPChWCA27Dw_C3fFrOQo47J2U6XszILtLbPC9F0T-Ro-c98P6oS7j8rz2S1_9XYP3i86UHC1vH7jIkrGs1goztiX02EdBFrP9CLHksQtABFnAGo3RQfOph8AvMTHQ7ZiDRCP88YDUjIkcJGU1YH8sU_gr8Y5o1FT3KEkvGkm_RHjPtP7ftV6wjmkZEl1J3fcMA1vjyhIFiEKGGphmGjTW9bw15ppMm9rVL5fmTPi77uFwlRFePiMEoz0Z-LKDlhUAGJgmRvr4qf6dDdDEDL1-oEC8_8_LCWaEDh6izsdkEWJzQf3zo5H0kqQhNMU10A6a7mH7dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران حاضر است به وضعیت آزادی کامل کشتیرانی در تنگه هرمز بازگردد؟
🇺🇸
ترامپ:
اجازه نمی‌دهم آن‌ها [بابت عبور] هزینه دریافت کنند. اگر قرار باشد کسی هزینه‌ای دریافت کند، ما خواهیم بود. ما کنترل کامل را در اختیار داریم.
ما سازوکاری در نیروی دریایی داریم که نوعی محاصره محسوب می‌شود؛ آن‌ها به آن «دیوار فولادی ایالات متحده» می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69483" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=gtoKTEPrUeb-DXBK7fT6fX7pVKN2Ei52Lr7zFZpFUrMqmsX31hEVdH42oj6bFWAKScV7o7l6cHETjqOICcGkekkFLDhCs4wYW5dGxqWU9kZEf61jDGBmOjFiEFH9i2Rd3znsVsdbbrjf2rGwpibFKSdSQd3W28h54X1anRQ5WaVJbiNiIM4cRtTpKVrAK3viJOXOQv0j9t61nc1-XP_2QH0GqSI0jfJy_bnLJWhRz_1vxGnkFM1Zbb3vDbBk-BeEGFPpJfVDB1_ibrfxodk4yYRWeIhXZZ0RoJxwSATArhQ3uzJng5LY049b31qQEocoDb22x6GV8jqUziFIpRmWC5HROIGWtXLxbMGn3Q2TT6VXr0cbKD_D9UiwJz3Q5FwO2NcwRHIPWbuRUlFHpTd2F1Gi32_6c3nbw53FJcAwKuhUkrJgnOSfNxIHJpjK3TYgGXpe6AjyRpzr8WUIUcVNvMPJbgW8dFLbrU5EPZExGTIPN1Zo5a9T-NDg8cryu8ZS7IIXjNrvrXcwI_SzJN-njL1XIrHyURMfKVMjggUy_51pClPLCxrls49aZrTNIo0DRNuZnB8QJX7N6TSnm9UGXwvh9Y2H3fR16JK2gUdbrq5b7L5C0R2_zORNUsGSMoBQZJDbraSNhaRJtpKh0uTmx_VOjsVysX-nDxkNsNSn9_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=gtoKTEPrUeb-DXBK7fT6fX7pVKN2Ei52Lr7zFZpFUrMqmsX31hEVdH42oj6bFWAKScV7o7l6cHETjqOICcGkekkFLDhCs4wYW5dGxqWU9kZEf61jDGBmOjFiEFH9i2Rd3znsVsdbbrjf2rGwpibFKSdSQd3W28h54X1anRQ5WaVJbiNiIM4cRtTpKVrAK3viJOXOQv0j9t61nc1-XP_2QH0GqSI0jfJy_bnLJWhRz_1vxGnkFM1Zbb3vDbBk-BeEGFPpJfVDB1_ibrfxodk4yYRWeIhXZZ0RoJxwSATArhQ3uzJng5LY049b31qQEocoDb22x6GV8jqUziFIpRmWC5HROIGWtXLxbMGn3Q2TT6VXr0cbKD_D9UiwJz3Q5FwO2NcwRHIPWbuRUlFHpTd2F1Gi32_6c3nbw53FJcAwKuhUkrJgnOSfNxIHJpjK3TYgGXpe6AjyRpzr8WUIUcVNvMPJbgW8dFLbrU5EPZExGTIPN1Zo5a9T-NDg8cryu8ZS7IIXjNrvrXcwI_SzJN-njL1XIrHyURMfKVMjggUy_51pClPLCxrls49aZrTNIo0DRNuZnB8QJX7N6TSnm9UGXwvh9Y2H3fR16JK2gUdbrq5b7L5C0R2_zORNUsGSMoBQZJDbraSNhaRJtpKh0uTmx_VOjsVysX-nDxkNsNSn9_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره مذاکرات با ایران:
امروز یا فردا متوجه خواهید شد که وضعیت مذاکرات در چه مرحله‌ای است.
مذاکرات به هر طریقی که باشد، به‌سرعت پیش خواهد رفت؛ موضوع پیچیده‌ای نیست.
ما درباره بازگشایی تنگه [هرمز] در روز آینده صحبت می‌کنیم؛ بازگشایی کامل آن.
سپس درباره توانمندی هسته‌ای ایران گفتگو خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69482" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69481">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=EghnADsd7ERJBFD6s8W4kRNME94aW_E041xQsOiqV8I1D9ZHF0HhxVrqwfaXYByWYKQmnCuKplFmSEMoujtcsLb2w4DLcQ2C5rIyPeZSFC-BXuFldi0LylGIoWDnWlWv8mYhui42vYFif1J5nR9FKcz9BhjTmO-V4f945TaWeujWjccXTqYt5VympPEFdcmOH0m-ZIFVe4x2JFGwnEHzsJ2VvZSy9bEammtt2mTVgh1wYPvBgyphIUQkojN8EPXyulMS0qQRlduOh-r5fGvS5IRvfCEUFWzcbxVOxONWn5yjTuxnJch8Ear2ipU_r5Vleg8hSsEesc7ej3oT5xWhew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=EghnADsd7ERJBFD6s8W4kRNME94aW_E041xQsOiqV8I1D9ZHF0HhxVrqwfaXYByWYKQmnCuKplFmSEMoujtcsLb2w4DLcQ2C5rIyPeZSFC-BXuFldi0LylGIoWDnWlWv8mYhui42vYFif1J5nR9FKcz9BhjTmO-V4f945TaWeujWjccXTqYt5VympPEFdcmOH0m-ZIFVe4x2JFGwnEHzsJ2VvZSy9bEammtt2mTVgh1wYPvBgyphIUQkojN8EPXyulMS0qQRlduOh-r5fGvS5IRvfCEUFWzcbxVOxONWn5yjTuxnJch8Ear2ipU_r5Vleg8hSsEesc7ej3oT5xWhew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این آخرین فرصت آن‌ها برای امضای یک سند خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69481" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69480">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=oX3zPELLO0JUJzMvWca6l77yfMheSZohSt8OzbwzxIiLMuC19XownaBbqBJ9RXNm7MPYcX9_9QNIejf7o5fFyuLn2rAigmzsG134j2j8kSc7EZRd3_CGmLT3GzvrNfK_1TBBJMeDI6MKpA8gRzDgYdt5NB6-MrgSG4bA2e3yheFBPDJ1Hs4_kdzCcVUb0irr957z4rFNg-N133bc5DXXD2_wcdFCxYe_xGnpeQRaIo2emqUYN2YF1F3KVmmdO2q2l16Z2o7qnyo-oAeC-QKOdZt7HsvtLyY__tmkfGYM8fcMe7Ee9p2Z9qgQ40PRa0BpakoIOtU3FBuJXV2Q_AG9aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=oX3zPELLO0JUJzMvWca6l77yfMheSZohSt8OzbwzxIiLMuC19XownaBbqBJ9RXNm7MPYcX9_9QNIejf7o5fFyuLn2rAigmzsG134j2j8kSc7EZRd3_CGmLT3GzvrNfK_1TBBJMeDI6MKpA8gRzDgYdt5NB6-MrgSG4bA2e3yheFBPDJ1Hs4_kdzCcVUb0irr957z4rFNg-N133bc5DXXD2_wcdFCxYe_xGnpeQRaIo2emqUYN2YF1F3KVmmdO2q2l16Z2o7qnyo-oAeC-QKOdZt7HsvtLyY__tmkfGYM8fcMe7Ee9p2Z9qgQ40PRa0BpakoIOtU3FBuJXV2Q_AG9aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
قرار بود دیروز ضربه بسیار سختی به آن‌ها وارد کنیم؛ بسیار بسیار سخت.
سخت‌تر از هر حمله‌ای از زمان جنگ جهانی دوم. این اقدام بسیار بزرگی محسوب می‌شد و ما کاملاً آماده اجرای آن بودیم.
در حال حاضر، به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و بسیاری دیگر، مشغول گفتگو هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69480" target="_blank">📅 21:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69479">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=P1PJtyTdFw5xc3eIybZUGB6CkgLtpggIbvto9saB6VS9rD0jYQl9IyoQW3C08Rh73omwXBG1qKi5-hwQIdfpobDq_r3cPPJXe-OimKOCfCoYvsxVCrTWoZHzycwDIF6kZU7AMnoDweZ6VCfd8Egibusk12NGE7VeoeamIuKz5JVgRQamTSGPDqblw0bkcP16ICg1sr-Q6FeOn33xnuQape1_s86W_r1mnsMXkblM6y41l91qtNdu-6Gg6nkS4b9KQA4uGwjvhZWCXcphaGljqJe69x2Vxvbv6c3igOemPyRg5gCDOzOO1OP4-bDpFDLe7xjlU8IKsaPSilc5Q7_jak4sSGH8McI5N-EHojh77MQgqKsvDtjdEjvqot6uoBfphUp81nOxiB_1lPtkGY32fKLjKhduYeAbPWtzXXbEv-UVCn9Yzee5IEdbrd5J2VUhdLZTpvFMEfnQS6pw8Py5LrDs8-RpmXXCGxEBuqzwwPDwZ70OApUDFkHEe0vle1J_LS-LN-xlakYnPP1xT6bodW3yprJ3Bp_xeCqI4e3N_mYF_PlacjF8JKlgClN13ThOkfeEifi3EskA2a0XjtHZ6KzlPUmfvlrC4622uGNf3RfyILE_GsmqftXlgrzwCm6oYpK1zcaOXy0oMZXRIuxcNIoPnnD8Hz1F44omAyrUWFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=P1PJtyTdFw5xc3eIybZUGB6CkgLtpggIbvto9saB6VS9rD0jYQl9IyoQW3C08Rh73omwXBG1qKi5-hwQIdfpobDq_r3cPPJXe-OimKOCfCoYvsxVCrTWoZHzycwDIF6kZU7AMnoDweZ6VCfd8Egibusk12NGE7VeoeamIuKz5JVgRQamTSGPDqblw0bkcP16ICg1sr-Q6FeOn33xnuQape1_s86W_r1mnsMXkblM6y41l91qtNdu-6Gg6nkS4b9KQA4uGwjvhZWCXcphaGljqJe69x2Vxvbv6c3igOemPyRg5gCDOzOO1OP4-bDpFDLe7xjlU8IKsaPSilc5Q7_jak4sSGH8McI5N-EHojh77MQgqKsvDtjdEjvqot6uoBfphUp81nOxiB_1lPtkGY32fKLjKhduYeAbPWtzXXbEv-UVCn9Yzee5IEdbrd5J2VUhdLZTpvFMEfnQS6pw8Py5LrDs8-RpmXXCGxEBuqzwwPDwZ70OApUDFkHEe0vle1J_LS-LN-xlakYnPP1xT6bodW3yprJ3Bp_xeCqI4e3N_mYF_PlacjF8JKlgClN13ThOkfeEifi3EskA2a0XjtHZ6KzlPUmfvlrC4622uGNf3RfyILE_GsmqftXlgrzwCm6oYpK1zcaOXy0oMZXRIuxcNIoPnnD8Hz1F44omAyrUWFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: مذاکرات با ایران حالا دیگه متوقف شده.
🇺🇸
املاکی: نه، همین الان هم مذاکرات در جریانه. واقعاً اتفاق عجیبیه.
این بار دیگه اصلِ مذاکره رو انکار نمی‌کنن.
فقط نمی‌دونم چرا، هر وقت دارن مذاکره می‌کنن، دوست ندارن بگن که دارن مذاکره می‌کنن.
با ونزوئلا یه درگیری داشتیم که خیلی خوب جمع شد.
الان هم با ایران درگیر یه پرونده هستیم و اون هم داره خیلی، خیلی خوب پیش میره.
شما هم دارید فوق‌العاده کارتون رو انجام می‌دید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69479" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69478">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=nTwakU_UXHlsauhKijKHO9Ssxu1Nr34-CN_pJ8hszsRv5MG4_DICYpRm7EN86seiV9kmx24KJklECdfc7H2Nf3OZkCFjqNW8QKUsjkHfBUb9bh8El1WejMa9O7OhGlW9dlSnW4l4pOgXUNoYyPY3IcyRmRjtZSs8hJrVMD_2RRmXJgzaNPWYWgK7lKDOlQLr_FmAjSvRvyfh6Q3n2gUuxog6iN6kFjCgM1SKNMAkyhe1V5TEemiuL5huyIkbPc4DKa7yv5iGDspb8qMDdDH0jKYo5IWsjY7WU137Bwo4gAbKQj2NMjXAb2ZTiZGJY6dQI_rT2S5llU4RAD2Yp7Zx4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=nTwakU_UXHlsauhKijKHO9Ssxu1Nr34-CN_pJ8hszsRv5MG4_DICYpRm7EN86seiV9kmx24KJklECdfc7H2Nf3OZkCFjqNW8QKUsjkHfBUb9bh8El1WejMa9O7OhGlW9dlSnW4l4pOgXUNoYyPY3IcyRmRjtZSs8hJrVMD_2RRmXJgzaNPWYWgK7lKDOlQLr_FmAjSvRvyfh6Q3n2gUuxog6iN6kFjCgM1SKNMAkyhe1V5TEemiuL5huyIkbPc4DKa7yv5iGDspb8qMDdDH0jKYo5IWsjY7WU137Bwo4gAbKQj2NMjXAb2ZTiZGJY6dQI_rT2S5llU4RAD2Yp7Zx4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
ما با ونزوئلا اختلافاتی داشتیم که به خوبی حل و فصل شد.
ما با ایران نیز اختلافاتی داریم، و این موضوع نیز به خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69478" target="_blank">📅 21:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69477">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=t8vmp4s-JhHGEcWE8IKvxEAkVbngAvVyQbi3u4L9XeyOIWiofBkhSoBaCrWo_l-noYFC-qaqjfuOw2iyXP2W1cgUwu81nvu6DU_nntMINIzg82BR1pdPO4tLwWQs9FG4_HfSztx9SDo1ogJYW3I7Jdl6Mzd8hlORNXh5F5ujk-THStLGJ2RIyXom44TMBPaq7EqB5Rc1BJB5qDMoZD38MvftDSidAPGhxQH56PTn3aXpNo2Zfquj2gdkVMJubOlTsyU5Ja2nN6IvTeV3Dv3sYxtZHIbNeXTRD0AkX2CTAF0VRCQuBASt0JXW7pPL7WK2lVjOUCElrjWe9CkeDYm5rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=t8vmp4s-JhHGEcWE8IKvxEAkVbngAvVyQbi3u4L9XeyOIWiofBkhSoBaCrWo_l-noYFC-qaqjfuOw2iyXP2W1cgUwu81nvu6DU_nntMINIzg82BR1pdPO4tLwWQs9FG4_HfSztx9SDo1ogJYW3I7Jdl6Mzd8hlORNXh5F5ujk-THStLGJ2RIyXom44TMBPaq7EqB5Rc1BJB5qDMoZD38MvftDSidAPGhxQH56PTn3aXpNo2Zfquj2gdkVMJubOlTsyU5Ja2nN6IvTeV3Dv3sYxtZHIbNeXTRD0AkX2CTAF0VRCQuBASt0JXW7pPL7WK2lVjOUCElrjWe9CkeDYm5rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
فرماندهی مرکزی آمریکا (سنتکام) فایل صوتی مکالمه ناو آبی‌خاکی USS Comstock (LSD-45) با یک شناور ناشناس را منتشر کرده است. در این مکالمه که از طریق کانال ۱۶ رادیویی دریایی VHF (فرکانس بین‌المللی تماس و اضطرار) انجام شده، به شناور دستور داده می‌شود مسیر خود را تغییر دهد و هشدار داده می‌شود که در صورت عدم تبعیت، با استفاده از زور وادار به اجرای دستور خواهد شد.
ناو USS Comstock به‌عنوان بخشی از گروه آماده آبی‌خاکی USS Boxer (ARG) و همراه با یگان یازدهم اعزامی تفنگداران دریایی آمریکا (11th MEU) در منطقه مسئولیت سنتکام مستقر است و توانمندی اجرای عملیات آبی‌خاکی و واکنش سریع به بحران‌ها را در اختیار نیروهای آمریکایی قرار می‌دهد.
بر اساس آخرین اعلام سنتکام، نیروهای آمریکایی تاکنون ۴۴ کشتی تجاری را که به‌صورت داوطلبانه از دستورات محاصره تبعیت کرده‌اند، به مسیر تعیین‌شده هدایت کرده‌اند، دو شناور را برای اطمینان از رعایت دستورات بازرسی کرده‌اند و دو شناور متخلف را که با وجود هشدارهای مکرر از اجرای دستورات خودداری کردند، از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69477" target="_blank">📅 21:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69476">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDBuT9H8G3OmQ9PGw736w5YDMM-z6NxUbw8eoH9TI7SdT3NKwCl7i3rBCgwDPYYyAO6XfwSOkZMVxIxt1d8Bua7ZrUEx5vtR6tFOuDifgmwT1SVKAtZuISryypHXu0Y-VPuSsdcF4wcBwsUEnz1F37vRRMS_K7zhi2B6YhyRSlJySf2E5IWswl6axVrDF9Px9qhLy-f9zZarXyUhwZmCtE4VUI-szT0SzVdCGZE3EkE7xnsBmDbmwdsjRelXGGCnUzYLO0oWOOPxtdlUKvc1vccSyxmjLNSDHBIiidtvzrjezelCsIRGmgzoKkYC8ONz6dvhVuMujju6Vony7KXaSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مارک لوین:
من از اسرائیل حمایت می‌کنم.
من از اوکراین حمایت می‌کنم.
من از تایوان حمایت می‌کنم.
من از مردم ایران حمایت می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69476" target="_blank">📅 20:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69475">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlJgQN-uxCwMP-P5N_VfZt8EyjjdLWSsimdimvf5PcUISO4Hs03ZQvazO2ARSu5BiDRvcNHl6ybji4glMyN532BXQzCo9-DENygBa0UO34Pvl4ymGjJ-eT4CxVHS_RKJjrvgwTXRLEyi-IN6qDwM-PH-j6XyJWONLvCRMWoNW_9wRWLETNcjgZ7vh6SOSPWHh5aB25gBHixZyz7POXD-RHFrC_es0uwSr-7MJ8p_k3lY2ChR1cIJtOGs7M5LKUtSKCFtNSZmvu-md9_3NgvkW4HpYX9zPPIcg87KM4W6GPDFhaiNgThV0t_0_GKuDykkTvPFQSj2jYx9UMrf3ZM7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ : رهبری ایران واقعاً یه جورایی دو‌رو و ریاکاره که باورنکردنیه؛
خودشون می‌خوان مذاکره کنن، بعضی‌ها حتی میگن التماس می‌کنن، مذاکرات شروع می‌شه، جلسه بعدی هم قراره به‌زودی باشه، بعد علناً و با افتخار میگن که هیچ مذاکره‌ای در کار نیست، هیچ صحبتی نمیشه و فقط با «عمان» کار دارن!
بعدش هم همون چرت‌وپرت همیشگی‌شون رو تحویل می‌دن که می‌گن تنگه هرمز رو با قدرت خودمون اداره می‌کنیم، در حالی که از قبل کاملاً تحت کنترل نیروی دریایی آمریکاست و همون «محاصره» یا همون‌طور که بعضی‌ها می‌گن «دیوار فولادی ایالات متحده»!
هیچی به ایران نمی‌رسه مگر اینکه ما بخوایم، و هیچی هم نخواهد رسید مگر اینکه یه توافقی بشه یا اینکه کامل تسلیم بشن.
فرقی نمی‌کنه ایران بخواد قبول کنه یا نه، واقعیت اینه که ما داریم درباره‌ی راه‌حل مشکلی حرف می‌زنیم که خودشون دهه‌هاست ایجاد کردن، خیلی ساده‌ست:
ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69475" target="_blank">📅 20:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69472">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4129d878df.mp4?token=baeluIMUkuo7NaRJqfiCx2l0rE1-xiUxmvnsZ7s3bu1hl0EzxAVR2sXXCMr_8YYgwKy1-k9KHgvX0lmyQkOWzSFIfiwphmHiEbX32YGkRoyl3tCz8jyYdpWA3e3YGPn09PBrvxF85rbzeeRZxgakxQ1NcEzaRZnjUEt24-GbybYvq9CE3vP3rkBQdo6UVmUlsonH-sFtrQidkOlSES2MDIVArolSjEBakrJ6PiZGVAun3ujlhY_t9N9jkxfJjL6YDUaOaQ1fCwZxlC9nHDZg10SW3FVubRaQTvTvP91T0rnt2MaOx02d902Q-ill5yRqZlFI29-H8vceWjBQV-B8WA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4129d878df.mp4?token=baeluIMUkuo7NaRJqfiCx2l0rE1-xiUxmvnsZ7s3bu1hl0EzxAVR2sXXCMr_8YYgwKy1-k9KHgvX0lmyQkOWzSFIfiwphmHiEbX32YGkRoyl3tCz8jyYdpWA3e3YGPn09PBrvxF85rbzeeRZxgakxQ1NcEzaRZnjUEt24-GbybYvq9CE3vP3rkBQdo6UVmUlsonH-sFtrQidkOlSES2MDIVArolSjEBakrJ6PiZGVAun3ujlhY_t9N9jkxfJjL6YDUaOaQ1fCwZxlC9nHDZg10SW3FVubRaQTvTvP91T0rnt2MaOx02d902Q-ill5yRqZlFI29-H8vceWjBQV-B8WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
درگیری عرزشی ها و پلیس عراق در کربلا:
توی عراق یه روحانی به اسم صادق شیرازی، مخالف جمهوری اسلامی و خامنه‌ای هست، اون معتقده که فقط باید گفت لبیک یاحسین، نه لبیک یا خامنه‌ای.
حالا عرزشی‌ها دیشب افسار پاره کردن و هجوم بردن سمت موکب این روحانی و شعار مرگ بر آمریکا و لبیک یا خامنه‌ای سر میدادن.
عرزشی‌ها شروع کردن به کتک زدن مردم عراق تا اینکه پلیس وارد شد و با شوکر و باتوم عرزشی‌هارو کتک میزد.
طی این درگیری بیش از ۱۰۰ نفر به بیمارستان منتقل شدن و عراقی‌ها میگن دیگه نباید ایرانی‌هارو راه بدیم، غذای مفت میخورن و مارو کتک میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69472" target="_blank">📅 19:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69471">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=s1VRnUXgBtT2v_QhMyKSmQoHi042jTLnrJ3SGOzFauXlln3PZ8Z5RdZYqEtmseKCjlQSMyC-PlXSFM4IiedroCDVGzQ0MntZ0irzOJitytfEgV5kx6g_8UdQmJWM34HruApsTzqPKBmOKeRfm0VqW5qOlVWc3DqUGzQF2RUbaz05fv7Xho2O_J1ZxMQyau4se-gxcaZtITK7eOF41J72yG7djc2cV3IV4-0A3Ch9OnhhnO50LUPlG71mbhC0NCdXW8bRaql7d8LIPnFZQrOLG1nNoO7akL_xJbw_El9YWTMxH-nKAnpgVpxR8ztLgc-gcF3iqEtxJS2mqGMqTJ-S7bvSAHkZz37GzT2Actc6pFKFUXWBoOcGi1-z5a0Pkbk7nFbHj6wTHuhicFbilxgteYV5Kq8s2kEn01KNX4yXDdqrU2r9lqvaLaznfdZO6Ot1MIThk8MUpL_rdDkJGGAzQ7OKbhJHOQIpvw93L4ME5OPjKqWHR9buGqcJ_w4QpfZD3gjBtCJZ1POQMq9U9mOQyfww8tkjq64iljnDri9cNHJ6hYjkvyjiTiia8lWVoAU0fXKJt-cvqxP_AxT7_zta8CwltObUcgWjtoPoOyQ4gqCVDGFnTzNFLtny777pF0BsMCX5WPmq4bFFOExc_PswY5ji3vXclGi6nfNV8zB1-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=s1VRnUXgBtT2v_QhMyKSmQoHi042jTLnrJ3SGOzFauXlln3PZ8Z5RdZYqEtmseKCjlQSMyC-PlXSFM4IiedroCDVGzQ0MntZ0irzOJitytfEgV5kx6g_8UdQmJWM34HruApsTzqPKBmOKeRfm0VqW5qOlVWc3DqUGzQF2RUbaz05fv7Xho2O_J1ZxMQyau4se-gxcaZtITK7eOF41J72yG7djc2cV3IV4-0A3Ch9OnhhnO50LUPlG71mbhC0NCdXW8bRaql7d8LIPnFZQrOLG1nNoO7akL_xJbw_El9YWTMxH-nKAnpgVpxR8ztLgc-gcF3iqEtxJS2mqGMqTJ-S7bvSAHkZz37GzT2Actc6pFKFUXWBoOcGi1-z5a0Pkbk7nFbHj6wTHuhicFbilxgteYV5Kq8s2kEn01KNX4yXDdqrU2r9lqvaLaznfdZO6Ot1MIThk8MUpL_rdDkJGGAzQ7OKbhJHOQIpvw93L4ME5OPjKqWHR9buGqcJ_w4QpfZD3gjBtCJZ1POQMq9U9mOQyfww8tkjq64iljnDri9cNHJ6hYjkvyjiTiia8lWVoAU0fXKJt-cvqxP_AxT7_zta8CwltObUcgWjtoPoOyQ4gqCVDGFnTzNFLtny777pF0BsMCX5WPmq4bFFOExc_PswY5ji3vXclGi6nfNV8zB1-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
عملیات آزادی عراق؛
در ۱۷ مارس ۲۰۰۳، جورج بوش بزرگ رئیس جمهور آمریکا در یک سخنرانی تلویزیونی به صدام حسین و پسرانش (عدی و قصی) ۴۸ ساعت فرصت داد تا عراق را ترک کنند.
او هشدار داد که در غیر این صورت، حمله نظامی در زمان انتخابی آمریکا آغاز خواهد شد؛
پس از پایان اولتیماتوم، بوش در اتاق وضعیت کاخ سفید  او در آنجا دستور رسمی حمله را امضا کرد.
بیش از ۱۰۰۰ بمب که بعضی آنها ۱ تن وزن داشتند و ۵۰۰ موشک کروز تاماهاوک را به سمت مواضع ارتش صدام شلیک کردند، بین ۱۵۰۰ الی ۱۷۰۰ سورتی در ۲۱ مارس انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69471" target="_blank">📅 19:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69470">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=qu1hUINE_OjhoPPVFBSLviNJiuDEVzot2WvQjmOV64M_KEONy4rryZaY1z5CRbfayL8njaBxk3C0m623e1WuH_i9TzCgDBEb41aKZfROxHR89QkKbmyaYdszjGiYpnUvhH_rrCIEjqd6pqM8Rp2oPAFCNKCRfjWCutGWIQ5rMSdJxxLgOJ8UbkZMrM5r6RIydqJ4uX6mtwlYT4eLoQwzzV1L2XHbCGQcel6EdA6APRR57gFuJ7BWXRcQxi0rKbm8DrKwl-KlAQ0KGq6cKaZCnw1Jm1FPvy72YzuDyLQBeKF_VYnEO69DfWgEBt6L3fCquM0EtQTdtZkFcZ9fmOceQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=qu1hUINE_OjhoPPVFBSLviNJiuDEVzot2WvQjmOV64M_KEONy4rryZaY1z5CRbfayL8njaBxk3C0m623e1WuH_i9TzCgDBEb41aKZfROxHR89QkKbmyaYdszjGiYpnUvhH_rrCIEjqd6pqM8Rp2oPAFCNKCRfjWCutGWIQ5rMSdJxxLgOJ8UbkZMrM5r6RIydqJ4uX6mtwlYT4eLoQwzzV1L2XHbCGQcel6EdA6APRR57gFuJ7BWXRcQxi0rKbm8DrKwl-KlAQ0KGq6cKaZCnw1Jm1FPvy72YzuDyLQBeKF_VYnEO69DfWgEBt6L3fCquM0EtQTdtZkFcZ9fmOceQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
اکثریت قاطع ایرانیان، اسرائیل را تحسین می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69470" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69469">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=s6pcLgDnAsYuC-wIBLAK-aZ9X4i6ADatk5oSy5WDTWPZIGl-8rzBA5RT122pjc-AYB3wVQpR_599OywX0z5clTM4xmLizKhq-0yx8ClJtdpZKMwECztsrTcqJvTHYaw6dgctrMHG5v_gD_qHXSxDg8n9ZSamsgVXWX2cKyLhekrkgqQR9wVkpWbw1NoyvB4xdCJ5A2wi3NN6WgHzjsdBl_gNarQndSY6H0urz1zKu6q4RKAB9jVK4Nj1gW9FeZE1lQ4qXg3E94a4zaXq8BrUuLwgD9mOhNVv94P39GjZDYSU4aRRgc8HB9CFqMdWN4-S52meiSVt7HiLQ4B_bbi8Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=s6pcLgDnAsYuC-wIBLAK-aZ9X4i6ADatk5oSy5WDTWPZIGl-8rzBA5RT122pjc-AYB3wVQpR_599OywX0z5clTM4xmLizKhq-0yx8ClJtdpZKMwECztsrTcqJvTHYaw6dgctrMHG5v_gD_qHXSxDg8n9ZSamsgVXWX2cKyLhekrkgqQR9wVkpWbw1NoyvB4xdCJ5A2wi3NN6WgHzjsdBl_gNarQndSY6H0urz1zKu6q4RKAB9jVK4Nj1gW9FeZE1lQ4qXg3E94a4zaXq8BrUuLwgD9mOhNVv94P39GjZDYSU4aRRgc8HB9CFqMdWN4-S52meiSVt7HiLQ4B_bbi8Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
خاورمیانه دیگر آن خاورمیانه سابق نیست. ایران هم دیگر آن ایران سابق نیست. ضربات سنگینی به آن‌ها وارد شده است.
آن‌ها همچنان توانمندی‌هایی دارند، اما به یک ماه گذشته نگاه کنید؛ آن‌ها به سمت ما شلیکی نکرده‌اند.
چرا شلیک نکرده‌اند؟ چون می‌دانند ما می‌توانیم چنان ضربه سنگینی به آن‌ها بزنیم که بازدارنده باشد. اگر به ما حمله کنند، متحمل ضربه‌ای بسیار سخت خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69469" target="_blank">📅 18:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69468">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=NOsAFR7iNA-hc7F-kpCOH6gBNksQVDDaYRgoIZI3VWz0DhTM0Gpd3Z1BabOtGwiztdvE_YNFQruukM2pOomXyCgPqnamDwxgEcZcrC6DUJwPUd161etblzrFh6h-_kSLlHUGEp_WE9rs1hM4FJnaZHhKtByl8y4lBbX3O43o6Fw87WrVBsYyx7xdQwim2MOL9AaLDVJI4FPkX_UisAP_520FmgMJnX0r7cAq85eTihBv1HJQIAMz3Ji6_vCH3iuAyfFwiTJzkmOYN1tmMaYvWA5cQ669ePEfUzXMYmS_WOb4_lLprOyRCDQ4Y8-oPSxcZc22Rgrz-Ajfm3mDsTLWSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=NOsAFR7iNA-hc7F-kpCOH6gBNksQVDDaYRgoIZI3VWz0DhTM0Gpd3Z1BabOtGwiztdvE_YNFQruukM2pOomXyCgPqnamDwxgEcZcrC6DUJwPUd161etblzrFh6h-_kSLlHUGEp_WE9rs1hM4FJnaZHhKtByl8y4lBbX3O43o6Fw87WrVBsYyx7xdQwim2MOL9AaLDVJI4FPkX_UisAP_520FmgMJnX0r7cAq85eTihBv1HJQIAMz3Ji6_vCH3iuAyfFwiTJzkmOYN1tmMaYvWA5cQ669ePEfUzXMYmS_WOb4_lLprOyRCDQ4Y8-oPSxcZc22Rgrz-Ajfm3mDsTLWSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دیروز روسای دانشگاه تو جلسه‌ گله کردن که چرا حقوق اعضای هیئت علمی دانشگاه رو با تاخیر دادین؟
پزشکیان هم تو جلسه کلش خراب شد گفت:
نامه نمیخواد، اون گوشیو بده من بینم...
📞
«سلام؛ حقوق هیئت علمی دانشگاه‌ها رو ۱۰ روزه ندادین. خداوکیلی این درسته؟... بده دیگه... دستت درد نکنه، خداحافظ.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69468" target="_blank">📅 18:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69467">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04343db3da.mp4?token=lFqV57_bj6SmGOHN3RvUqR5b3Zb51YmdE9ZnkyVy5kJuLxOVid6JQhunf_UQaIu7kxng9T5TNSTl81PMOG5nod3dC5ttMIxTtGaXFx2CK61Mr2fYbGTWoNF-dubqb7-OugmO0qSQruz_o4kJk0ypAzU_eM_KDC_jAjiEHFaQ9SU2pn8UoXfqZcqP11Y30iKmR7NrCeUuZ060F9SkRYMasD-knMgfcAKUSGWZgnSPZt7ho87N9meqHWbM9nhqljfhmgSX7C2Cb-w5Ix0gROy9BVagF_iAN-YucHwWZiWiVqm4H_SPQvHrCJKGE55LgUCWjOoWuVlwqkB4v34UWrO-4oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04343db3da.mp4?token=lFqV57_bj6SmGOHN3RvUqR5b3Zb51YmdE9ZnkyVy5kJuLxOVid6JQhunf_UQaIu7kxng9T5TNSTl81PMOG5nod3dC5ttMIxTtGaXFx2CK61Mr2fYbGTWoNF-dubqb7-OugmO0qSQruz_o4kJk0ypAzU_eM_KDC_jAjiEHFaQ9SU2pn8UoXfqZcqP11Y30iKmR7NrCeUuZ060F9SkRYMasD-knMgfcAKUSGWZgnSPZt7ho87N9meqHWbM9nhqljfhmgSX7C2Cb-w5Ix0gROy9BVagF_iAN-YucHwWZiWiVqm4H_SPQvHrCJKGE55LgUCWjOoWuVlwqkB4v34UWrO-4oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو ای از یک طرفدار حکومت که میخاد ترامپ رو بکشه:
میرم خون رهبرمو از ترامپ بگیرم یه دهنی ازش سرویس بکنم از یادش نره
از لحاظ دفاعی یا هجومی همه جوره دهن ترامپ رو میارم پایین
حرکت های رزمی‌شو ببینید فقط
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69467" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69466">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLrnGoIUBFMXJtbDg8di_mZvslayfLBG04tk3jl7zj2bqob5ZrReiRdy6q84BcELURAXb8Id7NsdySbovfY-NcRbVKkpjaG3PMdoxmiCku6Emh65Wwop56bjoVT-EcI8mOIFo0iOCv6bUPw9fH36WvaEkY_OSlOZ2Bn9O2dA0lxHxCECEaT8hfsUhklQZncF9iZL4EqNbVMs8NyQXklL_ODE4c3KcoPwPYQbbZCWgiZNB6PkVq3xRbtYIf6S31VWjgxKl9h44I7G8IzPuwSJ-XW2ibrtCuiapBeRaGtGosMFKQiXHeUhCWIh6eu5QjkRRAuc38BEXKxV25wxBuNvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛المیادین به نقل از یک منبع ایرانی:
ایران در پاسخ به آخرین پیشنهاد آمریکا، با بازگشایی تنگه هرمز تا پیش از پایان کامل جنگ مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69466" target="_blank">📅 16:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69465">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V37ft6O6KMUHXbj2pX-FrQVxwR2fco0NhFG8UvI4cTFNSg70WvEql5hntMuLzgOZEJOGrwVwQKZnvoLM0dkjkx8n_BnmLWrmhM0XsdFZXN1pWCaTn1TYQSq8HDLRzh6FOnR6DjWA6ydJQPvA1w7G_CbWXQyOSHEVZlpC4zEcQEkEKhWhq5iyCb0lSGTpd8GGYBez5PMitI1sJsjSizywMynh5NOrxSuxQ-UZnf8RczlvdT4FSRnth7lMsTmHMJizGlLV2daYeeE0e3Q-wtWrTJ3Z0pWzlOMQTBMR8M2uDWehgDyaCEEUq9EvffjX8o1eqEzKcWGn0UsWzIykBe_0Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست میانگین IQ کشورهای مختلف تو سال 2026 هم منتشر شد
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69465" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69464">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863fff3357.mp4?token=u1tut6-6jYOEcHY0cJwniZp9dw3tK22MJadFNssMkRtX0fvGeujZNYfKDkdLcXsi20YFzinXbGHReKRe_XFK3O7DkZZp9tdeB38MtV6bm7q-K-2eLuovtlUwf8w4xwMFE6Ja5Gt5lqaU7Ss5m8Js0gaRx5EM9mNTM1KLs0k58dIQ2C3IXH3BpDDIXb8lyitmslty9rq9echtZ7wOh2BwozXh5KCs8K1VCxEH7AegLfL7ds7yaIxgRgJj9tTOkrEEFSAfoslBwciqMZpfJ_yN0QB-ZecTVVH4kYWEURtCNmEIibFHCT_wfhnephY5Ada9j-cT_EXKQgR2XzaklH7-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863fff3357.mp4?token=u1tut6-6jYOEcHY0cJwniZp9dw3tK22MJadFNssMkRtX0fvGeujZNYfKDkdLcXsi20YFzinXbGHReKRe_XFK3O7DkZZp9tdeB38MtV6bm7q-K-2eLuovtlUwf8w4xwMFE6Ja5Gt5lqaU7Ss5m8Js0gaRx5EM9mNTM1KLs0k58dIQ2C3IXH3BpDDIXb8lyitmslty9rq9echtZ7wOh2BwozXh5KCs8K1VCxEH7AegLfL7ds7yaIxgRgJj9tTOkrEEFSAfoslBwciqMZpfJ_yN0QB-ZecTVVH4kYWEURtCNmEIibFHCT_wfhnephY5Ada9j-cT_EXKQgR2XzaklH7-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مشهد یه دوره‌ی آموزشی گذاشتن برای افراد بالای 60 سال که توش مبانی اولیه‌ی استفاده از موبایل رو یاد میدن؛
موضوعات آموزش:
آشنایی مقدماتی با برنامه‌ی بله
آشنایی مقدماتی با اینستاگرام
وصل کردن فیلترشکن
ارسال لوکیشن
تماس تصویری
ویرایش متن تو واتساپ و بله
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69464" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69463">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda203069a.mp4?token=KbxRCqXAYGm2XpsTIEoDb9dgnZTv7ucynPwnDl4nKVtUhoILH14adlOmnltKVkDBeD2POt2eNsoi7Tc0pggJFi0P6lgAxZZ_tZbdtZDvUm-Xz6HRppsOCrcz-WiGHSN3Hyrq79j5Kx5ZmojR1PQ0RGhjN8Ny2wUAFpodC-uRViJoZj9F22kh4ApoEbgDXw6kMx0GsV4I1Zm7wEBqyM36cGkuoiq4zISLlXJu8SWhCf6hkr9zPVHLaMWODIdzIdIrzzF_1w4u4ijEqkmiInfOShEqnl41iSBugmGPEcp7P4JsVYeC0BLGmivFUQI2NWs__HKrutc3hztV16wzkhUtNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda203069a.mp4?token=KbxRCqXAYGm2XpsTIEoDb9dgnZTv7ucynPwnDl4nKVtUhoILH14adlOmnltKVkDBeD2POt2eNsoi7Tc0pggJFi0P6lgAxZZ_tZbdtZDvUm-Xz6HRppsOCrcz-WiGHSN3Hyrq79j5Kx5ZmojR1PQ0RGhjN8Ny2wUAFpodC-uRViJoZj9F22kh4ApoEbgDXw6kMx0GsV4I1Zm7wEBqyM36cGkuoiq4zISLlXJu8SWhCf6hkr9zPVHLaMWODIdzIdIrzzF_1w4u4ijEqkmiInfOShEqnl41iSBugmGPEcp7P4JsVYeC0BLGmivFUQI2NWs__HKrutc3hztV16wzkhUtNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
میزان شانس بقای جمهوری اسلامی از زبان مراد ویسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69463" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69462">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b293a286.mp4?token=HtKY_SSZA-nJLkdYQU62oeiBPkKuyHB_JDcYmAFZGfQsu8Nw6fpR6gq_g5NcRYIxUXBe7W4otecJ1fX5iYV3xMrpY3NFXA8M8sw9wRjUFmen77zdEWQtZkHS-pHlsCHYCUJJwhJTUuUK4ldxfNqsxMCdA9WYfiyKxxPM-RdmmIiZM22xEiL5tFFHIa_FLetn6BDJ8tdEfg0VIyI4Gt5WO__gO77A8A7UYMhnfiNi7od4E0s-d7yP8XApYqrQddDN7-MJXoihNhh4ZWY-JQpcf7p5ALEy0W3MXCypsSH7chKGOxSthyuIC9pfd1ud4_UQJYb5QhpDcoOynuposqea0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b293a286.mp4?token=HtKY_SSZA-nJLkdYQU62oeiBPkKuyHB_JDcYmAFZGfQsu8Nw6fpR6gq_g5NcRYIxUXBe7W4otecJ1fX5iYV3xMrpY3NFXA8M8sw9wRjUFmen77zdEWQtZkHS-pHlsCHYCUJJwhJTUuUK4ldxfNqsxMCdA9WYfiyKxxPM-RdmmIiZM22xEiL5tFFHIa_FLetn6BDJ8tdEfg0VIyI4Gt5WO__gO77A8A7UYMhnfiNi7od4E0s-d7yP8XApYqrQddDN7-MJXoihNhh4ZWY-JQpcf7p5ALEy0W3MXCypsSH7chKGOxSthyuIC9pfd1ud4_UQJYb5QhpDcoOynuposqea0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعترافات عبدالباری عطوان (تحلیلگر سرشناس جهان عرب) رو شنیدید؟ کسی که همیشه به مواضع خاصش معروف بوده، حالا لب به اعتراف باز کرده و از کابوس کشورهای عربی پرده برداشته!
عطوان در تحلیل اخیرش (مارس 2026 )به صراحت میگه:
اگر پسر شاه (شاهزاده رضا پهلوی) به ایران برگرده، با توجه به اتحاد استراتژیکی که با اسرائیل خواهد داشت ،ایران به چنان قدرتی تبدیل میشه که تمام کشورهای عربی منطقه باید جلوی عظمتش زانو بزنند و عملاً به نوکرهای ایران تبدیل میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69462" target="_blank">📅 14:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69461">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=t3buDM0YzUQZ9mxGHSNHe3jX1U-UG7KJtODzftusWj9PBRNnR98Kq7vRH4UxNEaox6ivaSvtrNOuyV68n_a_TKAhAowqv4N_RrXDLswP4KGqVsT91_v-LbSupfUGKvsjojjtQHK7C7Ug1Lf84EkP1xiwC7VWM-Y-bRCOEmzy8ALkBg4Vx8Gj28wic0d4Lj3hZaf4Z_AHkyNbzURFmkcxA-U_XawcbxH4j5XSuXaNbDGuHxJTvvznaihqKjixmuC4HlsnGDgzw3Ha64zDOMAXj0Xyub5DQID3VhZJF0BzpKG5ENW1wo2d1zBU9xTRGWbK8URcQFnf3aS3jtb3eDXGqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=t3buDM0YzUQZ9mxGHSNHe3jX1U-UG7KJtODzftusWj9PBRNnR98Kq7vRH4UxNEaox6ivaSvtrNOuyV68n_a_TKAhAowqv4N_RrXDLswP4KGqVsT91_v-LbSupfUGKvsjojjtQHK7C7Ug1Lf84EkP1xiwC7VWM-Y-bRCOEmzy8ALkBg4Vx8Gj28wic0d4Lj3hZaf4Z_AHkyNbzURFmkcxA-U_XawcbxH4j5XSuXaNbDGuHxJTvvznaihqKjixmuC4HlsnGDgzw3Ha64zDOMAXj0Xyub5DQID3VhZJF0BzpKG5ENW1wo2d1zBU9xTRGWbK8URcQFnf3aS3jtb3eDXGqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
عراقچی داره میره اربعین و ماهم توی تهرانیم.
دوشنبه مذاکره ای نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69461" target="_blank">📅 13:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69460">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
از فرصت تفاهم‌نامه و لحظه‌به‌لحظه آتش‌بس نهایت بهره‌برداری انجام شد
در این مدت، واردات تجهیزات جدید، تعمیر و بازسازی سامانه‌های آسیب‌دیده و همچنین تولید سامانه‌های جدید در دستور کار قرار گرفت.
پهپاد‌های جدیدی که اخیراً از آنها استفاده کردیم نیز حاصل بهره‌گیری از فرصت ایجادشده در دوره آتش‌بس بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69460" target="_blank">📅 13:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69459">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08375903ec.mp4?token=aouKHGGTRp_5MjRgawb5zy0RRE8DNdAOXiwIxnLP-Eyi_S_GiINogrxZ0baW86ja3k2Z3MGYl9_5JhO68z6lDp5i9MVTZIOKK54gHZMGs2TCitJANoxp21Y2S4Mo1TEOJnFA7O9aA7FicQUVRWqzUe4YjSEzFFeFK8tD9y8bYKydq2ZWf58-35I5VSGx-YTLBHuu0DstbqyVXmU5thjFi2kpYtLCMgwimF69Y_UN_t3uvsA7EQvxr_A8vy7wpxnz5N_wuIfALatm9pfdr_s7LN8kut4A3Lfwkp3iPDrjWWN4brMgJIHztl215VU-36ahe8aJNtlmpvAKz5DCSSf6DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08375903ec.mp4?token=aouKHGGTRp_5MjRgawb5zy0RRE8DNdAOXiwIxnLP-Eyi_S_GiINogrxZ0baW86ja3k2Z3MGYl9_5JhO68z6lDp5i9MVTZIOKK54gHZMGs2TCitJANoxp21Y2S4Mo1TEOJnFA7O9aA7FicQUVRWqzUe4YjSEzFFeFK8tD9y8bYKydq2ZWf58-35I5VSGx-YTLBHuu0DstbqyVXmU5thjFi2kpYtLCMgwimF69Y_UN_t3uvsA7EQvxr_A8vy7wpxnz5N_wuIfALatm9pfdr_s7LN8kut4A3Lfwkp3iPDrjWWN4brMgJIHztl215VU-36ahe8aJNtlmpvAKz5DCSSf6DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نیروی تفنگداران دریایی آمریکا ویدیویی از تمرین‌های تیراندازی نیروهای خود منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69459" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69458">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKW_3A21U6d2HuBkJDJhBhCn6d37gK165qc_J_TR0yHvd4KvtnNl5oI4rx_o5DapdIb0XsTg6iQMJdDAfcm21r6IC_x2Fp6MXCCQXpoBILmsNJsiB6sikjmIHVorRNMPRnGKQE89KZAGn-hNr1-mUYiAlWPeId1PWASuBuJaNPwaTXQSjlbSyylYx_RTVUvY34WmQlm18QGNT6qud6MSJNMBzcVPghEcePNazSelgpPFtS6-m68TRyhoIoA8pCMhMwJ6gl9wvZsePtsBNBLM5HiBRcfxLbiE7-_wIyyAiYWhJdkZbc7XhoXaQVYMdcEkjXl9301nzeAHYZMSsIz9jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی، سخنگوی وزارت خارجه:
ما در حال حاضر هیچ‌گونه مذاکره‌ای با ایالات متحده نداریم و مذاکرات با عمان بر دستیابی به توافقی پیرامون عبور ایمن کشتی‌ها از تنگه هرمز متمرکز است.
هدف، تعیین مسیری موقت است که ایمنی کشتیرانی در تنگه هرمز را تضمین کند.
تا زمانی که محاصره دریایی و اقدامات ایالات متحده ادامه داشته باشد، هیچ تحول قابل‌توجهی در وضعیت تنگه هرمز رخ نخواهد داد.
🇮🇷
اسماعیل بقایی، در واکنش به ادعای جلوگیری عربستان سعودی از حمله آمریکا به ایران:
اینکه همه کشورهای منطقه اذعان دارند که از تحولات و شرایط آتی منطقه متأثر  شد، امری مثبت است.
جنگ ایالات متحده علیه ایران، جنگی علیه کل منطقه است.
طی پنج ماه گذشته شاهد بوده‌ایم که حضور ایالات متحده در منطقه، موجب افزایش ناامنی و بی‌ثباتی شده است.
طبیعی است که کشورها برای جلوگیری از تشدید ناامنی تلاش کنند، اما تجربه نشان داده است که هیچ‌چیز جز قدرت و توان بازدارندگی ایران، مانع دشمن نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69458" target="_blank">📅 12:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69457">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=Eo7JKnuFAMfIxLBKO1jLXyyPccbdC-4HAmIY7weMSAzBUoeajoQZSOwJUgoJYZwqLmDYdi_3mHtp8YfVTD9KIClaChL6d2T7k8BoMaDLmks4X2s6Pgwixc57F1kA_xpie6dWqtNC2HiFS9E4yosV7U4F0r4lzwoDJmhUaRu45iuJCZ9mwKMUyKzjiSs49jdNUQPKVYAppabVx1aDGzWRPiJ4LXlZGLODjQSAT-natW8IcK0RogZKn48OSoMWvoOP2ln7HEqOsJY4WnNYCNsxBRT2whK8DO8v76eTghbuTAZgqqa9rAkp6ykPRRm3_Ef80eC-RXQ-ABT2syyZVo2ApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=Eo7JKnuFAMfIxLBKO1jLXyyPccbdC-4HAmIY7weMSAzBUoeajoQZSOwJUgoJYZwqLmDYdi_3mHtp8YfVTD9KIClaChL6d2T7k8BoMaDLmks4X2s6Pgwixc57F1kA_xpie6dWqtNC2HiFS9E4yosV7U4F0r4lzwoDJmhUaRu45iuJCZ9mwKMUyKzjiSs49jdNUQPKVYAppabVx1aDGzWRPiJ4LXlZGLODjQSAT-natW8IcK0RogZKn48OSoMWvoOP2ln7HEqOsJY4WnNYCNsxBRT2whK8DO8v76eTghbuTAZgqqa9rAkp6ykPRRm3_Ef80eC-RXQ-ABT2syyZVo2ApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله پهپادی روز گذشته به مرکز لجستیکی عظیم شرکت وایلدبریز (Wildberries) در نزدیکی سامارا.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69457" target="_blank">📅 11:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69455">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2O_pZ0kwDhlnov11cv0LgzWjFJtj-wM0-D7qq5S_G3EeLzB8MdHqssDFit5sZdHtIU5N3Q4kJvANnTj2MR32Ololm6dQ8JZ59VejngUyEgm7r8aGwwmegGP5UDqBEriM0Woc7AMBjCbyX6GF57NLOavM-LK5B9yA6PiDN8nlBUqFQU8Um_HMucWHmZQJST7hRAozCtP_mhV3Z5-VdhfmNPKo-6mW9rBJak0745wBE9BGPtJY_ssyBYAKNY-89xeF5iZzGtFnVKC8WZWmyA_b1fgZsYQUAK07N4vuniVlEQF1hbOi5grX-FfPLmRYU9iTJB91PxIILbSD1BItw3Ylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=HstWj4APLE6TsCiXhq-vx9QCgMCo1go23DEQ36xXjEmQsFw5lUHVDD_0ALQRRggGCO2kx-dSgzeuCOTeIdb6gihfEIb1EyjbSWRtMpGjnDLg68Q6datlyTPO9yGZsH3Wb4-BiyjpQFN180EnFVTjZjvN6gfZ_HHaJDyslq3IwBQUWCaguJZjVI-tXOnFexXRiDxKd48Qh9zuOlu0bMJ6WP1n-kytbPslSzzBu5rAArISgk6EjZBlA4vvwYlvkcMiLqfbhaeVjj95tUdjc6H9Pq8k2vas_3w__9-W_d9SR_PbZfcNwCms371m8Pw7VH7MAQAIOaxBkZkEEX4DMvL5cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=HstWj4APLE6TsCiXhq-vx9QCgMCo1go23DEQ36xXjEmQsFw5lUHVDD_0ALQRRggGCO2kx-dSgzeuCOTeIdb6gihfEIb1EyjbSWRtMpGjnDLg68Q6datlyTPO9yGZsH3Wb4-BiyjpQFN180EnFVTjZjvN6gfZ_HHaJDyslq3IwBQUWCaguJZjVI-tXOnFexXRiDxKd48Qh9zuOlu0bMJ6WP1n-kytbPslSzzBu5rAArISgk6EjZBlA4vvwYlvkcMiLqfbhaeVjj95tUdjc6H9Pq8k2vas_3w__9-W_d9SR_PbZfcNwCms371m8Pw7VH7MAQAIOaxBkZkEEX4DMvL5cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده مردم در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69455" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69454">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=X2fkOIOyA2BqHYP1MUCwVqD3X6SprHFHlGcEJe_M0XrEqRtbOsYnqvRAvnLvISVSsJwWzs-64Ho3t6R3qmijgXecHWWcZkAE7taK5WPRjd7vljyPcJ-UQcWe_ycKFyebbHy1uBE8qu0XLiNTUhPbv06wacZrbZ9sVTjooky2SSI1xfrQQvWjqNE3z0h-KqKNEPoHGIWyJAx0xXXimkmK2Ewzt-27MfIDAbh6Dk5FfFRCKr9Sw0ISI_uQwrfWONXUWaNDR6diMKbTKzgY1mcRyw9_ZPnvIc_Upz_2F3B9OcaykZmyyd9sNBzf8aI7_zyNlmQwG6_RmGwF5Ps53AByWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=X2fkOIOyA2BqHYP1MUCwVqD3X6SprHFHlGcEJe_M0XrEqRtbOsYnqvRAvnLvISVSsJwWzs-64Ho3t6R3qmijgXecHWWcZkAE7taK5WPRjd7vljyPcJ-UQcWe_ycKFyebbHy1uBE8qu0XLiNTUhPbv06wacZrbZ9sVTjooky2SSI1xfrQQvWjqNE3z0h-KqKNEPoHGIWyJAx0xXXimkmK2Ewzt-27MfIDAbh6Dk5FfFRCKr9Sw0ISI_uQwrfWONXUWaNDR6diMKbTKzgY1mcRyw9_ZPnvIc_Upz_2F3B9OcaykZmyyd9sNBzf8aI7_zyNlmQwG6_RmGwF5Ps53AByWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای ازجواد موگویی که توی برنامش داره خیلی شیک و مجلسی جای همه فرمانده‌ها و مسئولان رو لو میده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69454" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69453">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=Um6moJbZkUmOu6aWocqVrXBYNOE3G_XkiKLOQH3bJOre209_-X6POKSSGEH1uGzD7jjhUEEuaa3L7N--sQXYNXsKZuH3267z_BQonsIymkyopQQgLyTN5iOErUC4DhYmiM53IrXPNq9aG62EwIR0wifETmtPr0MlRQh07op1l9LgfdXQzfXcOHIkJ1jzXyWdJeEueq7OvcQxYFmxSfad8j1HtpsneA2rO7WydvhvWtPs9CQlxAuewMUHMvQhdK3WrzKOJ8PmcDV_UQ6jdN4SsGff_YJPXahAP3aIAqvG2fItce_n2NIHMFUW0fX-thpbpbr4jlqOEUi5T-cC3LPy8zKDKwJyBrDlPpRhQVXPPAb29K7NRs_MMnCRgspWRZ8kmjgTK8ySDFa2BGptOBIn-yfAaumvgLxoLlJ2XLaOfBQjLResd9CPS_ebM4buy7aiiZ7zKgDxMLroW-KQ8AXXYbMx34SzIIZaPQlTEel3EUwAjyXREij2iC6FJkBPgIDvlpkQcSbBqMf64v3BD_yIQUAMu_QaI4hUthjX_B7R3aZKmbP0N4QtDJmP1_Yr2i-b2DrtoutV5__DBMj30fndTXTj16qM97pW4c-gh5Xamw7hT79EkTm78UQ7kkpuSKhIMMFYJrD4NVcIKSH-4YyzoyeotvjipA0gsIF0kdQqjb0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=Um6moJbZkUmOu6aWocqVrXBYNOE3G_XkiKLOQH3bJOre209_-X6POKSSGEH1uGzD7jjhUEEuaa3L7N--sQXYNXsKZuH3267z_BQonsIymkyopQQgLyTN5iOErUC4DhYmiM53IrXPNq9aG62EwIR0wifETmtPr0MlRQh07op1l9LgfdXQzfXcOHIkJ1jzXyWdJeEueq7OvcQxYFmxSfad8j1HtpsneA2rO7WydvhvWtPs9CQlxAuewMUHMvQhdK3WrzKOJ8PmcDV_UQ6jdN4SsGff_YJPXahAP3aIAqvG2fItce_n2NIHMFUW0fX-thpbpbr4jlqOEUi5T-cC3LPy8zKDKwJyBrDlPpRhQVXPPAb29K7NRs_MMnCRgspWRZ8kmjgTK8ySDFa2BGptOBIn-yfAaumvgLxoLlJ2XLaOfBQjLResd9CPS_ebM4buy7aiiZ7zKgDxMLroW-KQ8AXXYbMx34SzIIZaPQlTEel3EUwAjyXREij2iC6FJkBPgIDvlpkQcSbBqMf64v3BD_yIQUAMu_QaI4hUthjX_B7R3aZKmbP0N4QtDJmP1_Yr2i-b2DrtoutV5__DBMj30fndTXTj16qM97pW4c-gh5Xamw7hT79EkTm78UQ7kkpuSKhIMMFYJrD4NVcIKSH-4YyzoyeotvjipA0gsIF0kdQqjb0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مارک لوین:
تداوم توقیف دارایی‌های متعلق به ایران
ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
هدف‌گیری مستمر فرماندهان نظامی
حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
حمله به بانک‌ها و مراکز مالی
دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69453" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69452">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998caf4317.mp4?token=Ot-HW5OCm5nb6Obf8jLbeKSKN9qt2RdY99Wx4bpSHuMB1-iKsIStiRFBWivD8u3ND8USoRhDQo5dede2yc-MH3vPsm1sT35JZtXa1eIHgzPVE7NV6RVr-t3TqCchYZcg2t8wXZAzKSwaLKX5Qbfx-7w6unzMkur4gWYREiA3-p_QIVn2qhd7c7gz5tmfiUhhxWJVuMntOh7BnXzSB0psibZNZOyCnLHV6z-T-Ss-F0RG75EDR93lrUdMX6DBxAg26nBi1YNnkjcn-s2x9UC63tiCvcVyK6UKIQ4V5RJrx3mSP1kSvH_aeOH9wUTbJuj6dcKV4MRfKCEHxqakI8Jc4r2-_lCf5JM61L8hKMJjGJeHOiCC6xjPmUNLkxDbdFoJSaOkvXLFaB2Gu1qE_3iihffxaQM0uZJAQusYbkzMINWyY1RlvIwnYq5MdQxWL_EMbHiNxkL0AnaSDqt7TTF7CsCVk85HVPBOe4OrAwS35jqIL5rtbC7JKCgcmQ4kqvM308jJtLzZguZHvCTeSgaysCdF9rrOnQrF58Or3z3kHcW77DtpSOq4yyMm2ON_pbIyDlN2Gw1AE-y9nXfd1kKmIPwySZdsdM8etUqF0AAcJDvXTKaO3yj6IDz1wKLXlzp5OMYYx5cTfC_K6pEAsfCrjlR9a3JtjAdXybdDCii9KME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998caf4317.mp4?token=Ot-HW5OCm5nb6Obf8jLbeKSKN9qt2RdY99Wx4bpSHuMB1-iKsIStiRFBWivD8u3ND8USoRhDQo5dede2yc-MH3vPsm1sT35JZtXa1eIHgzPVE7NV6RVr-t3TqCchYZcg2t8wXZAzKSwaLKX5Qbfx-7w6unzMkur4gWYREiA3-p_QIVn2qhd7c7gz5tmfiUhhxWJVuMntOh7BnXzSB0psibZNZOyCnLHV6z-T-Ss-F0RG75EDR93lrUdMX6DBxAg26nBi1YNnkjcn-s2x9UC63tiCvcVyK6UKIQ4V5RJrx3mSP1kSvH_aeOH9wUTbJuj6dcKV4MRfKCEHxqakI8Jc4r2-_lCf5JM61L8hKMJjGJeHOiCC6xjPmUNLkxDbdFoJSaOkvXLFaB2Gu1qE_3iihffxaQM0uZJAQusYbkzMINWyY1RlvIwnYq5MdQxWL_EMbHiNxkL0AnaSDqt7TTF7CsCVk85HVPBOe4OrAwS35jqIL5rtbC7JKCgcmQ4kqvM308jJtLzZguZHvCTeSgaysCdF9rrOnQrF58Or3z3kHcW77DtpSOq4yyMm2ON_pbIyDlN2Gw1AE-y9nXfd1kKmIPwySZdsdM8etUqF0AAcJDvXTKaO3yj6IDz1wKLXlzp5OMYYx5cTfC_K6pEAsfCrjlR9a3JtjAdXybdDCii9KME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇱
🇺🇸
ویدیویی جدید از لحظه بمباران خیابان فردوسی در زمان جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69452" target="_blank">📅 09:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69451">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu03Y1y6DKPQldOVZGdgiiTRuOsdV1dZQHsC7vpLwgGGuFORUZg2-FLzBB3nPrxM_ePZiXT0XP_QJkvnjpiOhs_2Kkp3Xx3fZoE34P2OXyUBA4ZN4XJCKepKOoufBcbJbQeSSUCWPd4tcm0wNVtx8bsnf8OGg-sOpLTHi8HNInVj6aq4jExGq2vRfphualz1zF-bKAvtOhTvRemheHeONMHKpukcckzmtMLkYcmykZ5ycMcbCTffWmOP3uFe0y-jSPw7eLinaiciPcnrAxnvQr4NnU22si02c8zBK6d5OH5jC3yXtK0JcbfwBkVchCnL-rdKjeQkSQW6bvRzcHE49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هگست وزیر جنگ آمریکا:
واقعیت.
وزارت جنگ آماده‌ی حمله بود - و همچنان آماده است - در سطحی که از جنگ جهانی دوم دیده نشده است.
قفل و بارگذاری شده(آماده اقدام).
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69451" target="_blank">📅 03:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69450">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VZIF0J7C-LlQGFz2r-nrJ_0fmBVusM3jhjMwuBh4rF2x3iq6-pNWUWCux7MdFlpFs38zHTHOG9t2csPuLzgytGfzYo0Uq1S4el3IVlN_zbWjdgksCGR_-ts65MxQ3GH8KOAgTs1iMzx6FDeV99tSErR3BWZOF9d0XumihF6OhKKVWGkbSy63D5tlsegyvcTkbg2mwjdLt_M93FN0FrRn4au8Pa1XyNh1RMzqZU6p-43T6AMsRDaowr2SKfhahjNEbuJ44mgOKGNbjAtLnIxskty6FRWnKNiG7fqNLNODHgzW0si0StQ2cSxRP67AhKFunGc9hxTTXEsJzMikz0FsRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پست جدید کاخ سفید:
به ترامپ اعتماد کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69450" target="_blank">📅 01:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69449">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eW9klWJTB8u5LamDK-3zkWsEUkln-3ogrOr2FyVupmYk4eu13uyfc3wjmEKdk2JYCVA47c0k0KJT5W7qfxlXtRhA-khLIgFiE9R_4Nf-2E6bLrTUXS_mIUQTDTfnyluVGi3-q-YswDqeZ8we-t4Tafb3-6OH4-C6895P9vwpHqo8gXBZMn9t_abqLLQCKSrL-2eBRsnEsVv7RhxgfKcWFgfiqxnk2ZOVV2CL7C6ICa4tfeiF5A-fGIqE89NCBQ92iaY9QRegCp52RcXTIPRvHNIq9S6WRh2kw4SWtgBZCu2k31-eeiiODQgTUI9M8ZRqPk4hujMTTWGM_4EEF-avEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرقی خصبِ عمان دریافت شده است. مقامات در حال بررسی موضوع هستند و به شناورهای حاضر در منطقه توصیه شده است که احتیاط کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69449" target="_blank">📅 01:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69448">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
وسط حرفای ترامپ یه کشتی تو تنگه هرمز هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69448" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69447">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=M_GSQmpG64TFbTSit4B1WRBeZTdgxI5YXGu1Milts92r7vQtVTfej8MhaWOIMmz8wyG03Omyt0M0DR4WjpPVnbYzqDIZMLTb3fVGlFQlH64Z2a6HCPm22NoU5RFwC88UMCT6-rcD3U6lK3BPRT6sKxcz8FCGbU1JWHk_m0t21xy1LBu5_ZNoYWjO2jo0hfDG7mmfWSHB1vGJm1ad0YG5rVOSHbJCq0ii19thZBLJj15VMj4G_DEwRXFbc6MpzdVPXjY5ip2bCVNLGHU9qalYMo7TUdeT9G3lHhCTyPjvVYtIIORarOi9UYTdafKB_IvvTeVNAMPLlmkuRlPcgT9hbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=M_GSQmpG64TFbTSit4B1WRBeZTdgxI5YXGu1Milts92r7vQtVTfej8MhaWOIMmz8wyG03Omyt0M0DR4WjpPVnbYzqDIZMLTb3fVGlFQlH64Z2a6HCPm22NoU5RFwC88UMCT6-rcD3U6lK3BPRT6sKxcz8FCGbU1JWHk_m0t21xy1LBu5_ZNoYWjO2jo0hfDG7mmfWSHB1vGJm1ad0YG5rVOSHbJCq0ii19thZBLJj15VMj4G_DEwRXFbc6MpzdVPXjY5ip2bCVNLGHU9qalYMo7TUdeT9G3lHhCTyPjvVYtIIORarOi9UYTdafKB_IvvTeVNAMPLlmkuRlPcgT9hbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
نمی‌دانید این حملات به کجا ختم می‌شود.
منظورم این است که آیا همسایگان ایران با هجوم سیل‌وار جمعیت به کشورهایشان مواجه خواهند شد؟
یک فاجعه. اتفاقات بد بسیاری ممکن است رخ دهد.
ترجیح می‌دهم توافق کنم. به دنبال کشتن آدم‌ها نیستم.
آدم‌ها می‌میرند؛ خیلی‌ها می‌میرند. ما چنین چیزی نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69447" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69446">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=FHgesSTjHfTW5PHtj94j2v5XZFBSE6yXaFy3isdUsETetRBgoahBUs_hiW5Zac_VL7GEwo97By6dAizkEN9fpGAbWWuiyeV7ENYCDTdY8lNzqfrmD-t3bcJDPH3TjCG-SOsUuqA_QPab6Xb6thdODwKjHNEwZdhzUkZwNb2xYhogTpOGtpfqVAkaV3t__rGMximXosXMm7jZbiMSTJ5AVCuKu8kVNYWA09XNmsxHjvkvCNAnE7UqA9gswSrbZeILWfkB3kyPhNroqV1F_mmx0fBQtFQ-D45XtpKBNy2FFPkf474Ks9l7_agu3RC7Q95ExidRpAAT5B7DEegMCRacAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=FHgesSTjHfTW5PHtj94j2v5XZFBSE6yXaFy3isdUsETetRBgoahBUs_hiW5Zac_VL7GEwo97By6dAizkEN9fpGAbWWuiyeV7ENYCDTdY8lNzqfrmD-t3bcJDPH3TjCG-SOsUuqA_QPab6Xb6thdODwKjHNEwZdhzUkZwNb2xYhogTpOGtpfqVAkaV3t__rGMximXosXMm7jZbiMSTJ5AVCuKu8kVNYWA09XNmsxHjvkvCNAnE7UqA9gswSrbZeILWfkB3kyPhNroqV1F_mmx0fBQtFQ-D45XtpKBNy2FFPkf474Ks9l7_agu3RC7Q95ExidRpAAT5B7DEegMCRacAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ما حمله‌ای داشتیم که می‌توانست بزرگترین حمله از زمان جنگ جهانی دوم باشد.
این حمله برای آنها فاجعه‌بار می‌بود و آنها نمی‌خواستند ما این کار را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم این را نمی‌خواست.
آنها فکر می‌کردند که توافق قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69446" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69445">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=uzrEDzVM8IDu1wFIUgVJw991DZLluWD_pfIP33RUdwS2LcrQGVj9cUTdHW6qr4zUBrnnHNYTJhc2_4scJa43oPKinz4qbds4MEzv93nLbxKkjYZ3i1ho0uivjijXoAe_SV8u5g082Fa1smH-UVrjEWihPPFG3pmgBEDFI0dlUC0-hhVBEOaDRM4QB48xFBjNBadnnMcGq0M94GAsti1eSp7oc1hq_8UwbRyW0SWkvy91Ydrc46yOneBKmxEHH7wlD71bpzSRqsoLUWhbAcjfwZwli3uRawWuXbvlEPzEYw4IqswwJF94USpo0mbfRrAQ4LtUb8mUEnwlkKL4bayHaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=uzrEDzVM8IDu1wFIUgVJw991DZLluWD_pfIP33RUdwS2LcrQGVj9cUTdHW6qr4zUBrnnHNYTJhc2_4scJa43oPKinz4qbds4MEzv93nLbxKkjYZ3i1ho0uivjijXoAe_SV8u5g082Fa1smH-UVrjEWihPPFG3pmgBEDFI0dlUC0-hhVBEOaDRM4QB48xFBjNBadnnMcGq0M94GAsti1eSp7oc1hq_8UwbRyW0SWkvy91Ydrc46yOneBKmxEHH7wlD71bpzSRqsoLUWhbAcjfwZwli3uRawWuXbvlEPzEYw4IqswwJF94USpo0mbfRrAQ4LtUb8mUEnwlkKL4bayHaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای گسترده باشد.
آنها از ما خواستند که این کار را نکنیم. گفتند: "لطفاً این کار را نکنید."
همسایه‌هایشان هم همین را گفتند.
ما فقط می‌خواهیم ببینیم که آیا می‌توانیم به توافق برسیم یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69445" target="_blank">📅 01:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69444">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=VzhbDhOZbvX7b8zvrYNIlVzxAp3NyOqrGqCo8IG4brLPOp0jlQ8oZX4QJFZ6-7LPqNlZYdmnBxsHM_mxXAjvOHBYwBLUZorAHHcjuPmGvyzDKzz_E79Kqy08Mre_cNOUg1D8aHQMfIoWvrcOWNlBkvER426jMdqJAGqIYxcmWXY0uznu1cbv35-5Wmk79JGTxROokerD6fHpvOBPZA1M1_7JDPqLogUxV9jsu0nXvVuBPDrXbG3ILPUNyHC5uWIUhn4FD6Jf8ZaPOu2O7iQrqNwE0M-82AWT4gqdVXYeRdhLIC1xTYi_AlOtKvCUVJAmeRNC13qvrv47brrKRNq9Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=VzhbDhOZbvX7b8zvrYNIlVzxAp3NyOqrGqCo8IG4brLPOp0jlQ8oZX4QJFZ6-7LPqNlZYdmnBxsHM_mxXAjvOHBYwBLUZorAHHcjuPmGvyzDKzz_E79Kqy08Mre_cNOUg1D8aHQMfIoWvrcOWNlBkvER426jMdqJAGqIYxcmWXY0uznu1cbv35-5Wmk79JGTxROokerD6fHpvOBPZA1M1_7JDPqLogUxV9jsu0nXvVuBPDrXbG3ILPUNyHC5uWIUhn4FD6Jf8ZaPOu2O7iQrqNwE0M-82AWT4gqdVXYeRdhLIC1xTYi_AlOtKvCUVJAmeRNC13qvrv47brrKRNq9Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره بمباران ایران:
گروهی از افراد هستند که خیلی دوست دارند من این کار را انجام دهم—صرفاً انجامش دهم—و گروه دیگری هم هستند که نمی‌خواهند من این کار را بکنم.
🎙
خبرنگار: آیا ایران برای دستیابی به توافق ضرب‌الاجلی دارد؟
🇺🇸
ترامپ:
خواهیم دید. من به دنبال کشتن مردم نیستم.
از ولیعهد عربستان سعودی پرسیدم: «ترجیح می‌دهید ما چه کار کنیم؟»
او گفت: «ما توافق را به حمله ترجیح می‌دهیم.»
🎙
خبرنگار: گزارشی وجود دارد که می‌گوید شما در حال خارج کردن نیروهای آمریکایی از کویت و بحرین هستید.
⏺
🇺🇸
ترامپ:
نمیخواهم در این باره اظهار نظر کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69444" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69443">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=t9wzSNHyaJObafBUapeGb5Oylr7Zoy4-xIbC_xLLEpiGJEKDChh1cAmmoT-68lFKae4ZfIV_bIibqkxJDfRRiSH2aW5RsbPndbSIebEc7p0pfLJegleWq8NIdd51wnYDIVEsvQzeKewxKx4OhrtsKrlngu0HZBlNtegzkyb_tKmHhmNiLMMHixtTDh3EU6jgbjsFWMPiUgcoHvpk4kMxrQP6IvTg0_blqtWtgeqjoim4xt51Ej-OEMqF-mzufhoGJAf_OUc2g-83kaJ9V6c2F3f98XnRI5FDt_V0ZHFcPkde_YLkgBgjLzA2mAqdmbrkYd8ooVBNk4w-QX7ZoTqQng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=t9wzSNHyaJObafBUapeGb5Oylr7Zoy4-xIbC_xLLEpiGJEKDChh1cAmmoT-68lFKae4ZfIV_bIibqkxJDfRRiSH2aW5RsbPndbSIebEc7p0pfLJegleWq8NIdd51wnYDIVEsvQzeKewxKx4OhrtsKrlngu0HZBlNtegzkyb_tKmHhmNiLMMHixtTDh3EU6jgbjsFWMPiUgcoHvpk4kMxrQP6IvTg0_blqtWtgeqjoim4xt51Ej-OEMqF-mzufhoGJAf_OUc2g-83kaJ9V6c2F3f98XnRI5FDt_V0ZHFcPkde_YLkgBgjLzA2mAqdmbrkYd8ooVBNk4w-QX7ZoTqQng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: در مورد ایران، حالا چه پیش می‌آید؟
🇺🇸
املاکی:
ما در حال گفتگو با آن‌ها هستیم. این گفتگوها از بعدازظهر فردا آغاز می‌شود. این کار جان‌های بسیاری را نجات خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69443" target="_blank">📅 01:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69442">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=AyjUuFWTQN_8MRo_TfJQl6HwlWPf0_9QV0v2dnqAp-qETd8lLyoON2kBRQSOdZ6I5JW4upyh-d_RjhauOJtULEUjBBB0n0fd3PiPYJ5O8DX5Gbxh-S_VXer6h29rlcBRggby6lomV6fTFljxrexoTb2msx1RirBDY7d-fwLji17GeOSQyFxe1nkZj-uHqdyvlPbQcqS6r59HIeJzBWydRVrWETfd5bAi2I52QVcVaeV3tDrrc9iQUHh3XIiiNPUV5Q03QE_rpo0KJz4KGl4yJx7KCQ5PiAnXKIDZERw73df2Zh4KQIKoQbJ68NtKeNIWsZSnCNxLEie3REWOwPMB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=AyjUuFWTQN_8MRo_TfJQl6HwlWPf0_9QV0v2dnqAp-qETd8lLyoON2kBRQSOdZ6I5JW4upyh-d_RjhauOJtULEUjBBB0n0fd3PiPYJ5O8DX5Gbxh-S_VXer6h29rlcBRggby6lomV6fTFljxrexoTb2msx1RirBDY7d-fwLji17GeOSQyFxe1nkZj-uHqdyvlPbQcqS6r59HIeJzBWydRVrWETfd5bAi2I52QVcVaeV3tDrrc9iQUHh3XIiiNPUV5Q03QE_rpo0KJz4KGl4yJx7KCQ5PiAnXKIDZERw73df2Zh4KQIKoQbJ68NtKeNIWsZSnCNxLEie3REWOwPMB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد ایران:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند که حملات را متوقف کنم.
حمله بزرگی می‌شد.
وقتی متحدان خواستند که آن را لغو کنیم، باید گفت: "خب، ببینیم چه می‌شود."
متحدان فکر می‌کنند که توافقی حاصل شده است. توافقی در مورد هرمز وجود دارد و توافقی در مورد هسته‌ای خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69442" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69441">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=Zl2tEPEjMtbNK8soxCSmhI13X5UAzKoXPOOzL27f-dsVXeQbkFtrpD3pA3Cm7a0YoTpuVW1grdycGw4ooGrcnXIqzNIAyEsJl78JzmRregJrSomf6-WF_o7vAFnavhTd9iJMu_Tf-UoKGKuu2l9lgCWAIapZm_WyylXBAuDw2-GWgRjNsSwlC0Ujp87nwJt-DIrYxTsJCVSQ_pP_-30y8s3iZtTh0Fv0bH5B6ZfhaeVAx0pRCz5HZB4KjcEVclZztKx9P_tNYW8WbHSH4OzOmypLkO2NERmjJbU-Y8cEiSQk5VM6usV1Vgf5PwRGP_ZsVvefn1B0i90NNLhWFJCidw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=Zl2tEPEjMtbNK8soxCSmhI13X5UAzKoXPOOzL27f-dsVXeQbkFtrpD3pA3Cm7a0YoTpuVW1grdycGw4ooGrcnXIqzNIAyEsJl78JzmRregJrSomf6-WF_o7vAFnavhTd9iJMu_Tf-UoKGKuu2l9lgCWAIapZm_WyylXBAuDw2-GWgRjNsSwlC0Ujp87nwJt-DIrYxTsJCVSQ_pP_-30y8s3iZtTh0Fv0bH5B6ZfhaeVAx0pRCz5HZB4KjcEVclZztKx9P_tNYW8WbHSH4OzOmypLkO2NERmjJbU-Y8cEiSQk5VM6usV1Vgf5PwRGP_ZsVvefn1B0i90NNLhWFJCidw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی وقتی می بینه دلار شده 190 هزار تومن و آب و برقم هر روز قطع میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69441" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69440">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93362f281c.mp4?token=A1kJ-Zw2pIDf1jdSUU_rwqKLqR9ByCGJzMjhgv1vFIIkZI0WoNMUC3RTGblaw8sAc_MuihtaRVfhn0cgGLEvF6KuNlknCEG40MzuZ6tZZoWgC84hb9Tes7SBTF769kAD2FeZrO0hskfyEBrQkHRZmltGF8uLLWNhvbw3az3LVPm8Q5x5LjBZc44qjxWPX135Scd2ncux-CrwojrXK3twDqVon5Ixtyfmt711J3TvCb03LN7L_bQnZePPf9sPB8vj3SaC8phKUlYHVU1j-LiFvwmXeKooMsJrHACGZfTkQV4iz90v0-3cIFPLtKg93wtOsueKfuHc96RMlxbvX-WldA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93362f281c.mp4?token=A1kJ-Zw2pIDf1jdSUU_rwqKLqR9ByCGJzMjhgv1vFIIkZI0WoNMUC3RTGblaw8sAc_MuihtaRVfhn0cgGLEvF6KuNlknCEG40MzuZ6tZZoWgC84hb9Tes7SBTF769kAD2FeZrO0hskfyEBrQkHRZmltGF8uLLWNhvbw3az3LVPm8Q5x5LjBZc44qjxWPX135Scd2ncux-CrwojrXK3twDqVon5Ixtyfmt711J3TvCb03LN7L_bQnZePPf9sPB8vj3SaC8phKUlYHVU1j-LiFvwmXeKooMsJrHACGZfTkQV4iz90v0-3cIFPLtKg93wtOsueKfuHc96RMlxbvX-WldA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
شوت برنده در مسابقات قهرمانی باشگاه بدمنستر! از تمام کسانی که شرکت کردند، بسیار سپاسگزارم.
من با امتیاز 70 برنده شدم و از این بابت بسیار مفتخرم، زیرا برخلاف سایر شرکت‌کنندگان، زمان بسیار کمی برای تمرین دارم، زیرا تمرکزم روی مسائل دیگری است.
این را "استعداد" می‌گویند و من آن را دارم، در حالی که آنها ندارند!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69440" target="_blank">📅 23:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69439">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjJMyNWdn_fRhbZutftv2Zql4L75n7eKZ65S8fSLcGqvklCQ5ZcvJgyu4cmrVmBia_sxKK0ov-n8yu_n_pS8sKv3hKi8emFPxgoCGbaQaFrAGYFIIAba8Ho6woVb8SztmViTeAp8237O0DXithzmktfqxGEqHae6GReRYJejyx29R004Hm43_n_8TwjyOsVNqQ7v0wD_p3k23bVxYctyUfEKIOtt7NHk1x9X2gMYdzzpW3Dzs-Q-rId6LeRMWK3lAMacgsyDRgqwde0Ia4MFIS5FM8AYb98R7gpfpw0fMVmUodv4JZqX27b-UklXIGhbpIk0lzQF4aDR6LtJGkzAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پزشکیان:
تفاهم نامه که امضا شد حاصل خرد جمعی اعضای شعام بود
این تفاهم نامه ثقل روابط خارجی ما توی آینده هستش و باید دشمن رو وادار کنیم بهش پایبند باشه
امنیت کشور و منطقه و هم‌پیمانان با این تفاهم نامه ارتقا پیدا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69439" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69438">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⏺
شکار و هدف قرار دادن ۶۷ سرباز روس توسط مولتی روتورهای اوکراینی در اطراف پوکروفسک
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69438" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69437">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=oBwdKuklu4iFB7Remeb3qMrxNvi5g2rFuUyAKgkwES4JIt2reZu-Oy3rWWklmTx7DNVY3kMuSGYOHG2ObWsUYkR1LgJZP9UJB_OcJCV5h3h_pnMFH2Phffjef9VK5XMFOAPYIRGQ83qYH-dkcR_DpNbTpYUbI_wwE_te_UF11kT3Lfk5ptmfjDj88uSLH3AGHJxqHNyCViWe9-hZcRx-AnsXhD6Q606lMWVwUcnmK2CjupTw0Bq6toN52H5ka0g5KZWLkldTuHG5Eg0MMr0Yu6GiPz4pQ1Gl59MaOL6Jh4IXx8oSuZ4CT_wdstg1SfBUZik7_7pn0n0NF40EBkN6woi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=oBwdKuklu4iFB7Remeb3qMrxNvi5g2rFuUyAKgkwES4JIt2reZu-Oy3rWWklmTx7DNVY3kMuSGYOHG2ObWsUYkR1LgJZP9UJB_OcJCV5h3h_pnMFH2Phffjef9VK5XMFOAPYIRGQ83qYH-dkcR_DpNbTpYUbI_wwE_te_UF11kT3Lfk5ptmfjDj88uSLH3AGHJxqHNyCViWe9-hZcRx-AnsXhD6Q606lMWVwUcnmK2CjupTw0Bq6toN52H5ka0g5KZWLkldTuHG5Eg0MMr0Yu6GiPz4pQ1Gl59MaOL6Jh4IXx8oSuZ4CT_wdstg1SfBUZik7_7pn0n0NF40EBkN6woi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌
‼️
روح الله قرهی رئیس حوزه علمیه:
«وقتی ماهواره به فضا می‌فرستیم، می‌توانیم سرش را کج کنیم و خود آمریکا را بزنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69437" target="_blank">📅 22:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69436">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRIj4NyudQTTNMpBdvVnTigf2BB7q7JcWEfVaGXTrdXwvt9POoDI3hqfLKqKvnna3u6ek4voPdOTHljkwRo2rqV-lIiAKfiMBUjsWd9-GudKeZcZrZYKnJAsyJUZercBfabcMdaTBEJOiXxOg3wgXjLLlMPsecLoJaybkbuMCREJtvqMZiNVyFHF-njo9qw0UogOqLumYFTMw6LI2CCQEa8-_UR3SY-jf1vCOeNDB2qF49xazAFxH49aPOLXgCRcnevRedR7UDKJLL57k-XVYgWYns0ZKGDOrazvyb72nlb2b7f1r3_ujFhWlGM7u5w1OAGrBQ4Tc-Qc7K6jkhEbNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کان‌نیوز به نقل از یک منبع امنیتی:
رفتار دونالد ترامپ — که منجر به لغو حمله گسترده به ایران شد — به توانمندی عملیاتی آسیب می‌زند و آن را تضعیف می‌کند.
این مقام امنیتی گفت: «این دومین بار در طول یک هفته است که ایالات متحده اسرائیل را در جریان حمله‌ای برنامه‌ریزی‌شده قرار می‌دهد که می‌توانست خاورمیانه را تکان دهد، اما آن حمله در آخرین لحظه و بدون هیچ توضیحی لغو شد.»
یک منبع اسرائیلی نیز افزود: «با وجود رفتار رئیس‌جمهور ترامپ، آماده‌سازی و تدوین جدی برنامه‌های آتی دشوار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69436" target="_blank">📅 21:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69433">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LpK1kBru7YDucXYs0_Yn1kgBEg62RqFSDSdpNqkgqNBqt8HZeDknWYTKMDid7eDpwuZHzPvHFYZ7adLKFYTKkgIMjeoKK6jbU03axLS0u6uoCYLi_aQTF3Vwf7pHN3JaNBCkwg1k5IJtD48Fy3Vy-CUFvtO7K_V6ZbxCtdwTwOVrToo9JFTaQANpfkFZMwsY1wynxovsETZBtT76BYVbttZs670gO5OWJ_XPeYBkc2dtFOQfUVDvJc0CmMMth6p1KfUuenJ_FwDKSij14LNFJoFj3ZwsN1eBkjEe4IFxHQECSdWfEydUu2v6Sr2DQghTWE5n2_EPoY842quFjXH0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=TDcOr2yAlJBNNqah9wCupJnBFe_Ep5eSLTs7iLKi1E-oTRH7vQ9sX4WiLnHE0BFj12qCKtuzXo94ISco7DKi59nPz3FcVGoExQOJcNr6vJRU-g4ZE6YhBDfqwLTQdYnMWH1vxFSGM-RbMne94Bu9DlkpdjuMlUOyDmoB1iGOx7I9MvyS00PhQ1pod3rS2pKlr0xUDxWol-Xm3Jq5oSXL_YibOhI2bxmOxrOzttdsRNLb_9a-nhbXlx1JnhZmaOAVmF176kbMz93heAHOLHg5nTm-k8QQ2A7VzMhOydB3Ab0MykX6Uny0C4YpDA6JWDt_49pWepNUXnLhPOiuqcBFMw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=TDcOr2yAlJBNNqah9wCupJnBFe_Ep5eSLTs7iLKi1E-oTRH7vQ9sX4WiLnHE0BFj12qCKtuzXo94ISco7DKi59nPz3FcVGoExQOJcNr6vJRU-g4ZE6YhBDfqwLTQdYnMWH1vxFSGM-RbMne94Bu9DlkpdjuMlUOyDmoB1iGOx7I9MvyS00PhQ1pod3rS2pKlr0xUDxWol-Xm3Jq5oSXL_YibOhI2bxmOxrOzttdsRNLb_9a-nhbXlx1JnhZmaOAVmF176kbMz93heAHOLHg5nTm-k8QQ2A7VzMhOydB3Ab0MykX6Uny0C4YpDA6JWDt_49pWepNUXnLhPOiuqcBFMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انبار شرکت Wildberries در منطقه سمارا دچار آتش‌سوزی شد، این اتفاق پس از حمله اوکراین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69433" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5208110eae.mp4?token=B8YUH8zB6YLaatk9OPl5z9JVX_prdrRFwfSOELtPiGK4NsS_rXqwPN7vYy0qP022oJMV8_9OsRzsco4w21ry21-E0H3LsMA5y8wtbksaM_L__rnRPBkHeIjMsw_xOqa6i6d6ptUqnWYjvJfObsFuwU2Ef4MsvCL9AgvSY9Md7unaJhK_z_7wbJfSxSHZPpyuEE-vFI5aW8ZwWOwWdNWWy5msJA6m4l4as7Zp68DMDQAPRkdz1Lfjv-QWWvL4mEFTvKWaHVIzjQae1v_B-X2wpbij5dy4SqoD9IZDgMorJfSuASnvChsyEkKL7Cg4P3jrmWFqqBT-twEe7aeX-67xlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5208110eae.mp4?token=B8YUH8zB6YLaatk9OPl5z9JVX_prdrRFwfSOELtPiGK4NsS_rXqwPN7vYy0qP022oJMV8_9OsRzsco4w21ry21-E0H3LsMA5y8wtbksaM_L__rnRPBkHeIjMsw_xOqa6i6d6ptUqnWYjvJfObsFuwU2Ef4MsvCL9AgvSY9Md7unaJhK_z_7wbJfSxSHZPpyuEE-vFI5aW8ZwWOwWdNWWy5msJA6m4l4as7Zp68DMDQAPRkdz1Lfjv-QWWvL4mEFTvKWaHVIzjQae1v_B-X2wpbij5dy4SqoD9IZDgMorJfSuASnvChsyEkKL7Cg4P3jrmWFqqBT-twEe7aeX-67xlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی امور خارجه، اسماعیل بقایی:
مدیریت آینده تنگه هرمز توسط ایران و با مشورت عمان انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69432" target="_blank">📅 20:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69431">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04acf28261.mp4?token=HPLcN-t8UlSY6Ir-UeJEiFH_sTo3Lr0BkxZsm4KmipLwX79I1vurw1Np5krwPUa_0RPvH2WEsku_BG50LjOIvbTZ-qMlUFWRqbPsssv2xVsV0VhJgwU9E4rNxV1BQVS42MduZnXkNzvq_yqMaobKwLhWTa945ZrT4qqCgTLXfqOmDXpzCY4hKnGpWByFSlX3Tl2awSTu__zY2cvqVNykulox8P6lAB9NqfowLmtsbWWk5tdzQhYjKgWrGZm5turw1N-M7JarBb-dkXKSQJEJWKs9_vq4FKZoR1W9J_n3PBE8Dsve2MBbHvhwlfjvO9-eVLuJjIn4A98kDBkZOGEkfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04acf28261.mp4?token=HPLcN-t8UlSY6Ir-UeJEiFH_sTo3Lr0BkxZsm4KmipLwX79I1vurw1Np5krwPUa_0RPvH2WEsku_BG50LjOIvbTZ-qMlUFWRqbPsssv2xVsV0VhJgwU9E4rNxV1BQVS42MduZnXkNzvq_yqMaobKwLhWTa945ZrT4qqCgTLXfqOmDXpzCY4hKnGpWByFSlX3Tl2awSTu__zY2cvqVNykulox8P6lAB9NqfowLmtsbWWk5tdzQhYjKgWrGZm5turw1N-M7JarBb-dkXKSQJEJWKs9_vq4FKZoR1W9J_n3PBE8Dsve2MBbHvhwlfjvO9-eVLuJjIn4A98kDBkZOGEkfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی وزارت خارجه اسماعیل بقایی:
توافق ایران و عمان بر سر مسیر جدید هیچ ارتباطی با بازگشایی تنگه هرمز یا حفظ بسته بودن آن ندارد.
مسیر جنوبی از طریق تنگه هرمز با ناامن کردن منطقه و آسیب رساندن به منافع ملی ایران همراه بوده است و تهران آن را نمی‌پذیرد.
مسیر مورد توافق نه مسیر شمالی و نه مسیر جنوبی فعلی خواهد بود. در عوض، مسیر جدیدی خواهد بود که هر دو طرف متقابلاً بر سر آن توافق دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69431" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69430">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=Zxk64gSd2so2V5NCX39w9ZIoBeivjL4G-DiayLtb_tr2dZcZULY96n4CUOHIJupeGZcOmaHFrORn9K-V2WAIGZhq25oWKZBjkNnn_wIXIotxOOE6Hhhnr6LO5bBYY_tJ0-_NKL74uYnYGaGIB_U6_aO3XNbQibGgyFsqmxxVkK_bwX9qKVyssFnDwNNTznJmfMKhgL99KKA5V6tQ7PEDBRiFJ3iddkT3Qp5xckjSMZioR803rkhgnCClrua-_mfpUhWPxvmCIPtKkkQRtuNb5_6M618n39aev_NLzyGNQUj4YfuDSCgF6EyixmSOnLOdQIAHiSIXJ17m3DaAvOsgLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=Zxk64gSd2so2V5NCX39w9ZIoBeivjL4G-DiayLtb_tr2dZcZULY96n4CUOHIJupeGZcOmaHFrORn9K-V2WAIGZhq25oWKZBjkNnn_wIXIotxOOE6Hhhnr6LO5bBYY_tJ0-_NKL74uYnYGaGIB_U6_aO3XNbQibGgyFsqmxxVkK_bwX9qKVyssFnDwNNTznJmfMKhgL99KKA5V6tQ7PEDBRiFJ3iddkT3Qp5xckjSMZioR803rkhgnCClrua-_mfpUhWPxvmCIPtKkkQRtuNb5_6M618n39aev_NLzyGNQUj4YfuDSCgF6EyixmSOnLOdQIAHiSIXJ17m3DaAvOsgLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کارشناس صداسیما:
مسعود رجوی (رئیس سابق مجاهدین خلق) فرد باسواد و کتاب‌خونده‌ای بود و قطعا خیلی باهوش‌تر از رضا پهلوی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69430" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69429">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=UFfKmtqkA6-6OB66h39JNCrd7HdxiTeWLQIP-Ht3b13KKj8bT_t3leh8YVV-Bh9IPvB1cFfxub1f-TUBXZK97fo4OXBzppNfiX8s7qrIK_w4hH34OFQZeBzH2Vsov6w6FhurKBvw7HS75LmOpHtAiGZwBS8lqZAlQ26xCUgQGfXoeyW9SibGAANbta5uCnopvXcnI2o5_vE4rMOH4hByOaxdN7Flz82MHHcEZzedC-xn77zfwfdcuYZXcDgmwfv09NWSAK8rQZz4iH_JE-yjqFC5xQlHaPHEuoDqrc-gml7b5GBn01a4TY-FrYOwWPwh2StR-Q1JueOLaL4el4yVPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=UFfKmtqkA6-6OB66h39JNCrd7HdxiTeWLQIP-Ht3b13KKj8bT_t3leh8YVV-Bh9IPvB1cFfxub1f-TUBXZK97fo4OXBzppNfiX8s7qrIK_w4hH34OFQZeBzH2Vsov6w6FhurKBvw7HS75LmOpHtAiGZwBS8lqZAlQ26xCUgQGfXoeyW9SibGAANbta5uCnopvXcnI2o5_vE4rMOH4hByOaxdN7Flz82MHHcEZzedC-xn77zfwfdcuYZXcDgmwfv09NWSAK8rQZz4iH_JE-yjqFC5xQlHaPHEuoDqrc-gml7b5GBn01a4TY-FrYOwWPwh2StR-Q1JueOLaL4el4yVPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
من یه مشکلی برام پیش اومد که گفتم نمی‌تونم در جلسه شورای دفاع در نهم اسفندماه شرکت کنم و غلامرضا رضاییان، رییس سازمان اطلاعات فراجا به جای من در جلسه شرکت کرد و کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69429" target="_blank">📅 19:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69426">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=IDrWo4PKojgNoi9KuT33prOpRPZpTBwthl5ZH0GObfzkxSuKVv5raTfAJoJrf3x7MLePdXhPhjHFwqEy-HipVs371K-LIVg45tWqO-u2bS26hIxqpeb1_5C_oOwXUpvKaAbr56MLXRSh7eR0hbizTg60ZxQz6et9F1vu09P8PAVblotAn53faYKVx9NSUYzA7FXOGa23nWWfbOiDAF8-qhBf5cPGbck3-QFyf4bgLwa78hGGpU1ycPWfxTwtc1IIl1gpPIMAZcmnf_3Tz2i1LJ-1afM4ePO0Xds5gaUhyCIMx7FU-N7M9H02jnAn0pLSKC1pdqVuGwacWMZWWN8gVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=IDrWo4PKojgNoi9KuT33prOpRPZpTBwthl5ZH0GObfzkxSuKVv5raTfAJoJrf3x7MLePdXhPhjHFwqEy-HipVs371K-LIVg45tWqO-u2bS26hIxqpeb1_5C_oOwXUpvKaAbr56MLXRSh7eR0hbizTg60ZxQz6et9F1vu09P8PAVblotAn53faYKVx9NSUYzA7FXOGa23nWWfbOiDAF8-qhBf5cPGbck3-QFyf4bgLwa78hGGpU1ycPWfxTwtc1IIl1gpPIMAZcmnf_3Tz2i1LJ-1afM4ePO0Xds5gaUhyCIMx7FU-N7M9H02jnAn0pLSKC1pdqVuGwacWMZWWN8gVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💋
🇮🇷
این جنده‌اینستاگرامی که خیلی ماجراش وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های
🔞
عجیب منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69426" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
