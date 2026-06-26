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
<img src="https://cdn4.telesco.pe/file/U3MfJiXJ6lyJ-mSvlAvGo1gTMsKafdfL3tuwCJ7tC-VfMv-0FYjL9mKoUssHD-f-3MuCsn4NpqaVjPueQshbAEk-Yusl9nt3V1fZxUk829e79LlE4n9rLyRtSnVuqkfg5B-5pb3ckDpVHxZmY5xCSHlGHB3qp3MgU_vpLuIH78fEt0GsJOM1dLOTvwo6rgI4MEf4q6bnBbNDbCahq61vvAsRUmTal4jdluFOZOCsMB1q4Q1WXcxMNOgdE9rartWPTf_Lctklo_p1EPwC_SVl4XD1dXmR50zZPLWLzcp4x5K6NDr1tHdY62clUBFrIq-87QNByfkggNtxY3YwQGhhyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 22:44:31</div>
<hr>

<div class="tg-post" id="msg-66885">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/66885" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66884">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GU1RBzQTBUbidDg2yMXAf_nMJck74b_xjwLmAP8MihLGmDwuJfXa7DeC9FybPRzttvU_7STN7_lKrj5HfP5B2ut2PHL2fi47qQL9Bq8BmqLSB8MX0LQZt1rqCYjh6dEbbyKkYBPbKBbRqbAOCKGOsF4XrMNi4JdXW76mTM3PNUM20VWI6MgNsgI_lhFyPLnkDdTCDYSMk7iQZijCKA0Zd8cIMzK2fQya-iEAg4Qu9u3cxZ3xQD38i6Suci1_7nKVMA3ix9wnB0JeZ_me7-5dmEqKulYDu493hkjAKheWG6tbEYm8XU0c87XXrQb6qz43Wf2_xhuzHYx1wPjFpNIQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رئیس کمیسیون امنیت ملی:
به سران شورای همکاری خلیج فارس هشدار می‌دهیم، قمار بر سناریوی آمریکا، ثبات و امنیت شما را بر باد خواهد داد.
دیدید که پایگاه‌های نظامی آمریکا در کشورهای‌تان چگونه به جای تامین امنیت، به منبع تهدید بدل شد.
قدرت موشکی، پهپادی و همچنین مدیریت تنگه هرمز، خط قرمز جدی ایران است.
تنها راه تامین امنیت منطقه، فاصله گرفتن از امریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/news_hut/66884" target="_blank">📅 22:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66883">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=q0Y2mkVuajJXQLghNY-3QjU5zTJRomKrXiR4hAJ54I3XXZPFv-VsMN_bOLyIXaB3js1hk-5ORxJwXcw-0xl7g7TYVFb64IXEA2EDE6QpBPZV8-dLTJVwZDZXFZ8xeofJgvzCUtPp-nB5agbl1os7YSn0WFIG1YsmTmKvJFDN6-4vO4VPUk_fH1UwUlJ5rTAB97sDssuEpTrzEgrBU0RyUv3xmNISgrkxNF78vFz_pfXkXh3uZRatWizx4cq_5EOzcshXmlEA5e1rHIjY9B_TqMPamkYcHIF6Lqth9HCJL1GarLEpDkpw005kdXHUUTh3eVi_X6GLUtDythEaYhnaaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=q0Y2mkVuajJXQLghNY-3QjU5zTJRomKrXiR4hAJ54I3XXZPFv-VsMN_bOLyIXaB3js1hk-5ORxJwXcw-0xl7g7TYVFb64IXEA2EDE6QpBPZV8-dLTJVwZDZXFZ8xeofJgvzCUtPp-nB5agbl1os7YSn0WFIG1YsmTmKvJFDN6-4vO4VPUk_fH1UwUlJ5rTAB97sDssuEpTrzEgrBU0RyUv3xmNISgrkxNF78vFz_pfXkXh3uZRatWizx4cq_5EOzcshXmlEA5e1rHIjY9B_TqMPamkYcHIF6Lqth9HCJL1GarLEpDkpw005kdXHUUTh3eVi_X6GLUtDythEaYhnaaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏نخست وزیر نتانیاهو: اسرائیل تا زمانی که حزب‌الله خلع سلاح نشود از لبنان عقب نشینی نخواهد کرد.
🔴
«شهروندان اسرائیل، پیش از آغاز شَبّات می‌خواهم خبر یک دستاورد بزرگ برای کشور اسرائیل را به شما بدهم. همان‌طور که می‌دانید، ما در واشنگتن مذاکراتی میان نمایندگان اسرائیل، لبنان و ایالات متحده در جریان داشتیم. این مذاکرات طولانی بود و امروز به نتیجه رسید.
🔴
مهم‌ترین نکته این است که اسرائیل در درجه اول در منطقهٔ امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و تا زمانی که حزب‌الله خلع سلاح نشده باشد و تا وقتی که خطری متوجه کشور اسرائیل باشد، این وضعیت را حفظ خواهیم کرد.
🔴
این همچنین ضربه‌ای بزرگ به ایران است. ایران تلاش می‌کند با زور ما را وادار به عقب‌نشینی از جنوب لبنان کند. اما در واقع اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند: این موضوع به شما ربطی ندارد. شما هیچ نقشی در لبنان ندارید؛ نه شما، نه حزب‌الله و نه هیچ سازمان تروریستی دیگری.
🔴
نکتهٔ دیگر این است که ما به ارتش لبنان اجازه می‌دهیم تا سازماندهی خود را برای در اختیار گرفتن برخی مناطق آغاز کند. ما دو منطقهٔ آزمایشی (پایلوت) ایجاد می‌کنیم که هر دو به توصیهٔ ارتش اسرائیل هستند. یکی از آن‌ها اصلاً خارج از منطقهٔ امنیتی و در جنوب رود لیتانی قرار دارد و دیگری در شمال رود لیتانی است؛ بخش کوچکی از آن در منطقهٔ امنیتی گسترش‌یافته‌ای قرار دارد که طی دو هفتهٔ گذشته به دست آورده‌ایم و ارتش اسرائیل به آن نیازی ندارد؛ ارتش این موضوع را کاملاً صریح اعلام کرده است.
🔴
ما همچنان منطقهٔ امنیتی اصلی را که خارج از برد موشک‌های ضدتانک قرار دارد حفظ می‌کنیم. اجازه نمی‌دهیم نه حزب‌الله و نه غیرنظامیان وارد آن شوند. این وضعیت حفظ خواهد شد. و مهم‌تر از همه، اسرائیل می‌گوید: امنیت ما بالاتر از هر چیز دیگری است.»
@News_Hut</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/news_hut/66883" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66882">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMbU3vzuDXvf5urw_4PfR-LOW4cQqHFWwCuZF9DCCxbpU9uFC-19MFjn7lTK8XXK0-UtHaxdXD-4XfLc79o_aQQkIaL-UyyTJefeWXqmxD1EyK56G6tZGJkPfKRHkIetetVbrmRv2DfMLKaPZVtJoDcr0tjIa1iA85bYscSauDcZ_gVIQ_0CcVIJkVuwnJmdcdPa00Nt_chS2CVYX-yFnATzbgGgRbWS35QlpoO1-szE8V8NkmIbyT4maIlveTtn-DySgNj7Lcbzjr80znWwNpFN6rZ7Z9rnZ8cuziX3y2nHkmIzm1pg8APYAT1ND673c8qBUYURMUMQAcY4gr6ChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و لبنان به تازگی در واشنگتن دی سی توافقنامه‌ای را امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/news_hut/66882" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66881">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
🇱🇧
حزب‌الله تصرف تپه «علی‌الطاهر» توسط نیروهای ارتش اسرائیل در جنوب لبنان را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/66881" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG-5sqZX1xQBmZW5c3NWWez7I749Bp0nnvfe30Prm4GleJehkcM6oPeUHhoLeM27sHa4g9pNOrDKt4CyjG0Ft5SvdJcnpUKSWQtgb63mcEDYGnrsd6RjFvY2U8iIK3SUTD-BQELaY4-cHq8wnvoRCZ9etkYCTF0eDnEy-kRIowWOWav_UkeJNCfU7Sm5PN6GYAvjSV4sUfLC6Zx1lBhpsiEml_gyIk8QFddUOKIyzbXMVz4AF4XL048NSe3MueZbL5zVBM2keDLXhO-jybmwJrEZ86eoGcG5S23zLeTt0UpxqnVJ0jRKgtgSxfJlaSaI7ESe5hV6T6lj0EfSa8TeWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsHKqb_La8m_yyO26AyQT6qASjMDPTr8_5eT-qtWr5WpFsdyE87azjqgXTAyZwsHgjpP4jIzN1SHCFCEvs1LUU2hpmZ5Wf18j03q-Y-MFtjl8n4cCyZ-CStrGXZs-Epacj7bd6eQpr0ar8-7023tYYx5S6TbacozT0jn2_uF5pOvw7Mj6_3KEl5KLQhwVOqKVOBusi2rkEND4gGbF8Qrko8RNZPVclWolU0BNkiCst9sxoP5BT0177BsivmWF8ThHlTc81Px6yxMCaqqsM70gjbww8o_Fb4wv1NZV62tsIjTwklc31zH3SVFSCiD88l9qij8S3gNVm9XkCy8RWtUcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FC5ZRQdOHVYFW6-raQ7qbkHYmgLrtVsDhur_vZGBjpii03a74u84a7BDTwyST3nLpqBEanB-AhUmMOj8AG6OXw58UttWDLsm3sDErD_l57t0SkOAlHXj8mk3XiTeLTaM18ZGSqfYLlde6yBDZVCdZ7F-QBJ3UwXk8a8d2gNZQltqHPy_EJ_3O20IG62TfX7HEtdr1AKMz90l5DyIqMSveEbhaQ6-UxYCb-iq5mm3f-3djA6x0BR4SvTmx81Xer5ElWwH3nApZijhVhTHc9enQVKSvGJ0plXHYghFf-qmUo_b6BRkLsF8CSvgQxUouKpAIvp7FtIvlBRJMeSvU3faiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jisNc-GuII3jgAhWpUFfEh8_DkmhJpAbVbNipvktTQPIMAGqKrsWTuoQpMX5cpxdAtQHguCkHWDcBXeZ3PdY9xI1DsafwKSvpzUBCNnAMP7kk4t6fHFBuw47VPVOw9D0ezIawTbIzlwT0vFBHBBKHxYLjS0uGDxp-l--z5zNuP9-U4-bIBg7WMX0f6mUvNNsH6pPCH5XCIEkUuqQGo-fHNDzsaEUnY3gnb8-86aAuMjhPPNjUkR6TGZT5qR4QIHo7ADouJUDoyG5eBn9G6jxFPqFzfN-CBYPXXsqScvd8kifQe5lgZVOzA2SCrIBVx8G1Z9bF0j1Bxxvbaj_d8ca9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد. ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66877" target="_blank">📅 19:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66876">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1yqSKDWR0Bv6ahAGlnWbRraAdHbTvkN_2842ibZPmSPE-06xgLfhpSxPY8hLHSFYnQYbzIxONNs5dsTmIrQ5esuEwNVycaLKgouKI9A6IpmNEPFzCLe2MW1XnVYY69kceI3B0I6aWNbNHS5tXnDRTQfFEBPHUYudvbqderK7WaRE0kkPrBSXQbid4MyTZihOwaK6SnnVxmvQmK-PY2hVEQ621bJ4CJwcDfqEr8d9SiqzXTcI20JgfqMSS7i885qe0DHyEfN8OM3dwtyBARgxWWHEpvJ67F1W57__8LKNi7Eb3CdvF58MN0cx2LVI1RIKzqOoS8PS2ODKoy4GWcX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66875">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYBRVtc_ofzWPFR4BTiR-rJwZcjIuU-eBXaVTO5I1cFhFZM49PNXO0UG9izG2sZpLZaQCOaZSNiXF4LB7NzOSW7DIG130sq_DPELtbsRyy_pQBnlkC7GESPJcBGwog0S0vJG5jvC8pwo-SAxaWsFGvAbvmc0ebJ3HGWjDAuw_gFUI072PTqNPArs0Q1ISRkkjasZhJEtpci9XebvHM858yMkatiqSpzafWbNZ5TIcSTln-o3uxa79mN935l80WF6wxj27giVqJO61FGtvHkeM7DXGgH3rE7IhjeL1Pz1cvYfgVtsdt9H6UIJXUg243q4e9yUHBal00NRUr7pMtEdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
رونالدو تو جام جهانی گریه می‌کنه؟
پلی مارکت می‌گه ۶۵٪ بله. احتمالاً آخرین تورنمنت ملیشه و دوربین‌ها منتظرن. البته رونالدو رو که می‌شناسی، شاید حتی با قهرمانی هم گریه کنه!
قبل از اولین اشک رونالدو، پیش‌بینی‌ات رو توی 30 ثانیه روی پلی مارکت از تلگرام ثبتش کن
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/66875" target="_blank">📅 19:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66874">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=qWd6rbHpA3Le4b9EHhBeSoJ1TAC9XTTczaAqSAI389W9YGwsR91vYig3uL4Sl3zySKlkuORY_QPOCfO7G8Zr0cYZwiWaLhX0a3YKop9pNUjZKEhQmCPnEszw3UoRLBRfe5XYJ9bPEyXU-uRS81tDet24k6lQEyhVo7rax7ZVlR-6EtItHk79uw9j2FyWrNFtSIpxKQNF34dBZweLo-Wjcv46_6M0yyVRUcohs1hIcFcUl0iwbLcioze-OnyjCg21MXIoIQ_hsitSbpB18EyEgbmiEaQ1rJzESdwLE3NxrHBYB5ggjw8pULAnAGsXbAl1dxg-1ClH-vsQUzPRipgyPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=qWd6rbHpA3Le4b9EHhBeSoJ1TAC9XTTczaAqSAI389W9YGwsR91vYig3uL4Sl3zySKlkuORY_QPOCfO7G8Zr0cYZwiWaLhX0a3YKop9pNUjZKEhQmCPnEszw3UoRLBRfe5XYJ9bPEyXU-uRS81tDet24k6lQEyhVo7rax7ZVlR-6EtItHk79uw9j2FyWrNFtSIpxKQNF34dBZweLo-Wjcv46_6M0yyVRUcohs1hIcFcUl0iwbLcioze-OnyjCg21MXIoIQ_hsitSbpB18EyEgbmiEaQ1rJzESdwLE3NxrHBYB5ggjw8pULAnAGsXbAl1dxg-1ClH-vsQUzPRipgyPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قاسمیان:
به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/66874" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU1OWhfM8N0SaZAh-Y5yeieVZjEdV3q65BCJIFksxXudlwziIFfTtAtfTRCh4c7U3BiXrPUYr8sfnuBNBaq2T5OeMeqDSLXM0vTbbshy93x_IKDiPJHfGFVMrxfOv2CnKJZYcd8S5aI3WbnBy1wjdC2XhuLO2WWwEjDz1qJ2IybUjrZNX7VZ6YjRc5Ae0TpRUxg5Yn7YV4EymSVg-se2SXlM9I5ymBW2w0bmmgxQ9iUZtJHD54VxXYOpljofOI04_BVoannKeyHgqtdBAJ9hMkzXjtjnOL91nhgV3sdx-Yfq2CU-nE7qR17k0Rk46slMBD7r9EQGZ3tRV2NR3nsofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
توییت کاتز وزیر جنگ اسرائیل که قالیباف و عراقچی و پزشکیان رو تگ کرده:
فرمانده نیروی قدس، قاآنی، این روزها مدام اسرائیل را تهدید می‌کند.
به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحکِ تهدید به او می‌آید.
در هر صورت اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.
نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان، هیچ‌‌چیز ما را متوقف نخواهند کرد.
نیروهای ما آماده‌اند تا کار را به پایان برسانند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66873" target="_blank">📅 18:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66872">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=CWIGrBnjgfKVpN8dm7e7jfnNgTP9MsuZh80R-B7582cc0sQ9u1UD3A0eEDEBBpiyQeyYbyG4IK4A4hVrmJB00A3peASuDuRVc5xpitSllP8SqBedv_VNaZooMsW_E6mpCTymdMhL8LYKX_FJQFFJ2X6BZstaGXPgtzp_Dp2WxBb7YVus-uKNsZMxfxS7zulp0yxL8JSVxWbF7SJxwEGYNbe4HOsX2OOMgRCLRBlx8JF_rjOTvs2yHPdFNwT8e_ZzCLE3GZeImVuiNTyc4ORpob6ViZOK-uJyvz70Qe48T_Vla2ZlqfWRq7Mwl5s8ky9mNL3GrObu7gbvQQa8TAvwVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=CWIGrBnjgfKVpN8dm7e7jfnNgTP9MsuZh80R-B7582cc0sQ9u1UD3A0eEDEBBpiyQeyYbyG4IK4A4hVrmJB00A3peASuDuRVc5xpitSllP8SqBedv_VNaZooMsW_E6mpCTymdMhL8LYKX_FJQFFJ2X6BZstaGXPgtzp_Dp2WxBb7YVus-uKNsZMxfxS7zulp0yxL8JSVxWbF7SJxwEGYNbe4HOsX2OOMgRCLRBlx8JF_rjOTvs2yHPdFNwT8e_ZzCLE3GZeImVuiNTyc4ORpob6ViZOK-uJyvz70Qe48T_Vla2ZlqfWRq7Mwl5s8ky9mNL3GrObu7gbvQQa8TAvwVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای وایرال شده‌ی یه آخوند تو یکی از هیئتای مملکت :
حضرت آدم دید هر عضوی از بدنش به درد یه کاری میخوره که یهو یه نگاه به وسط پاش کرد دید یه تکه گوشت اون وسط اضافه اس٬ گفت این دیگه چیه؟ هرچی دست بهش مالید دید اضافس بدرد نمیخوره؛
حضرت آدم خنجر یمنی رو کشید که کیر خودشو قطع کنه که یه دفعه حضرت حوا ظاهر شد گفت آی آدم چرا میخوای بیچاره‌مون کنی که یه دفعه آدم دید کیرش راست شد؛ بعد با خودش گفت این مال کس دیگه ایه٬ این تو اختیار ما نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5BhspcJvWsUHX1l_ZSYx4BLbOVS6NIKr1ZiUlW-0WrO697-hC_lJ-kpoKxfLSTVwjNOb0ik0kv_Ww3wN34HHUpC-OQ4KchX8LX8UzRbc-22AiW6Bh0BpXI1c0d25PVLjd8ObxX5aZoFyHsQc9aog595GIsCCEdzn7dGlbKrPxgI0L-6DS5AK8qI8X7RXR1-RGPHT5obwGalHPNNN-noqKQ5EvRTnFIhPxAgqR0PrTdjwXVcXht2R5JK-simj_R_EDkVafF6GOYIjgAyeBOIKkNG7jAdJynwVR4dH9tGMo_sWQLxWw6DQfwx__NyknA5UnevSAj0A4mU_MINzdII7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-wfIfJA9gB7FOkniKShwI1dK3lPW5NHbA0uBcFQzWeCE5VuU7STcl_P7r7n38nDIbXFDJdh8BfgOjgZCL5-IIe17uJz9hPeOfCDtzw4diMvPZqTbXByU39PdsNI-CELEbpXmudMQXDVQy-rsxXPj10tNeDouoUOGIWQT-K0fHRqqNSyjgIiaq-zia7Xoo_oTFxGLuijp5SaSUVX9j5QIVTTPNR1BqnHEkqSOARNN5lF23QPhOrvUSRRxT_gsqRy47M4l3yeqXO5be8v3mxr2pVXyvtCaZFVCIeWY3mDL4i7ZVKHG9NXvwL-nuZsLuC61tJq13ZPAXWyHRG13gB7NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
‏
بر اساس تصاویر ماهواره‌ای که روزنامه وال‌استریت ژورنال تحلیل کرده، حملات موشکی و پهپادی ایران خسارات گسترده‌ای به پایگاه نیروی دریایی آمریکا در بحرین، از جمله مقر ناوگان پنجم، تأسیسات ارتباطی، انبارها و ساختمان‌های پشتیبانی وارد کرده است .
با وجود اینکه پنتاگون اعلام کرده عملیات ادامه داشته و تلفات انسانی ناچیز بوده، این حملات آسیب‌پذیری قابل‌توجه پایگاه‌های آمریکا در خلیج فارس را آشکار کرده و موجب بازنگری گسترده در آرایش نظامی ایالات متحده در منطقه شده.
مقام‌های آمریکایی در حال بررسی انتقال یا بازطراحی تأسیسات کلیدی به نقاطی دورتر از برد موشک‌های ایران هستند. گزینه‌های مورد بررسی شامل پراکنده‌سازی نیروها، تقویت استحکامات پایگاه‌ها و گسترش استقرار در مکان‌هایی مانند اسرائیل است.
برآورد می‌شود هزینه بازسازی خسارات واردشده به پایگاه بحرین حدود ۴۰۰ میلیون دلار باشد و مجموع خسارات واردشده به پایگاه‌های آمریکا در منطقه از ۲ میلیارد دلار فراتر رود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66870" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66869">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=cEQC29bSzRPs-ULVhZ9NZ5GaHMCbloToKLv-FVQNLZwzjnq6GtcLh9xfgUd7fOtZJKzXpQSZS2RLjQHpTtJJTyyw-d7FSKnjy6_xU1x4TF7AwOjK25IBMC6MiS55ly-CC-G2sefcnF5MGQzK-Yr4WU3ze6ovX6lpdBS8mtkZBytGLiWHiNt1pq7KwfxCg0ueZnDhstltjUdoho1Ziv7Dikwj_I2N8PvjNqLQ6OiHawK-Mhc3lLmhl9FxENi8UO3UECtat9hwkEGD54vsROxMMJaKyr9fxmUEcWnh2E_YfUKuFJB9uUBFFHY-j6QA7sKTsHdSssheb0RPo9Nni8Ji7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=cEQC29bSzRPs-ULVhZ9NZ5GaHMCbloToKLv-FVQNLZwzjnq6GtcLh9xfgUd7fOtZJKzXpQSZS2RLjQHpTtJJTyyw-d7FSKnjy6_xU1x4TF7AwOjK25IBMC6MiS55ly-CC-G2sefcnF5MGQzK-Yr4WU3ze6ovX6lpdBS8mtkZBytGLiWHiNt1pq7KwfxCg0ueZnDhstltjUdoho1Ziv7Dikwj_I2N8PvjNqLQ6OiHawK-Mhc3lLmhl9FxENi8UO3UECtat9hwkEGD54vsROxMMJaKyr9fxmUEcWnh2E_YfUKuFJB9uUBFFHY-j6QA7sKTsHdSssheb0RPo9Nni8Ji7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
فاکس نیوز:
دبیر کل ناتو  فاش کرده در جنگ اخیر فقط ۵۰۰ جنگنده آمریکایی از مبدا ایتالیا به سمت ایران پرواز کرده اند؛
«اگر ایتالیا را به‌عنوان مثال در نظر بگیرید، ۵۰۰ جنگنده آمریکایی از پایگاه‌های آمریکا در ایتالیا برای پشتیبانی از عملیات “Epic Fury” به پرواز درآمدند.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66869" target="_blank">📅 16:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66868">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=Bno6dqFGbg5gGeG4E7PFD8BoIrQv_vhe_Cypp27SuEy9fEMJQhYuNmX10aRBHeKbN0Zs6Url_YSId55ruIKJCbeaiiydlY3HnT8lKeGQDIJh829ex6khDsWNxEaBp2ebA9ggwNzraHNLpPGEpdXOP8juueW51lV2GEI5NZRNhI6cXmJldmC2m4FDFhd4qx_xU63BdDvmkVP4Sktew7-JW5EUvXwGLokHRyefUiUYx31HDACdA1vD8Gw0WvZaeSNJuKjZEqG_MIGwfPRUWc8Q02kQOD7aj7sTMji5zpKPME6Qm5ZvuXEEJHtvbjCjuToeah_tnPvPqN4Wb-wJ1chpGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=Bno6dqFGbg5gGeG4E7PFD8BoIrQv_vhe_Cypp27SuEy9fEMJQhYuNmX10aRBHeKbN0Zs6Url_YSId55ruIKJCbeaiiydlY3HnT8lKeGQDIJh829ex6khDsWNxEaBp2ebA9ggwNzraHNLpPGEpdXOP8juueW51lV2GEI5NZRNhI6cXmJldmC2m4FDFhd4qx_xU63BdDvmkVP4Sktew7-JW5EUvXwGLokHRyefUiUYx31HDACdA1vD8Gw0WvZaeSNJuKjZEqG_MIGwfPRUWc8Q02kQOD7aj7sTMji5zpKPME6Qm5ZvuXEEJHtvbjCjuToeah_tnPvPqN4Wb-wJ1chpGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاسخ سخنگوی وزارت خارجه به دست ندادن تیم مذاکره کننده با ونس با شعر مولانا:
چون بسی ابلیس آدم روی هست
پس به هر دستی نشاید داد دست
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HmhlsvLs2aoaWWWlO_Bjy4uwWJE0N_9B2zpI0GlEO4awMfhyzwkE_WfjrfDvmc7yC3Tbmblb5xY9ZvvCLceNHreOe1n9p0yj240QWMUjpjQal0gGry0fCsMLHjCEy_VIp3Jt00IPq_CpBq4nQpu0kaRFBvLnH2uP4VtwTGGlKex-HDg6bysO57oj0W44j1zAqDRn_KKES-_VbJtNpKmzUizJggZfh2DNp2HN2fJcGIt5BX9Zgg-ItoI0JHAjk1J21ewIPxCTJbQywlueTeCzGuZUr5Gh0a1LT0Nj3cVC7MH3Kn_64wQHjC3EvxDrkrs82jB5qEqmCXE4LzFAocO0M3vwAMWhhoU7cMTb3rLXDCjujP9JRo4cNJvg1cgjUfoznE9VT6L8aMZstB6D25HkF8Q1GidzAcBKVCmGsolxazQ3iLdz5umakFZ2PgRtOtjQwcSFExaqnO4HJ8DZBwER34ohif9WDnDW5tisv_8oghDKCSU_EQ7Yv4la9o6ehbakaLnE_G38xCMTFBvFeFKs9djaI5_0Lhm1XW4PN2iIBOEW5461H4n0_R5aJRv9Kd5dFu8ujN9hTCHLyNfNSrqzfblG4_z48j9PDW0OlTVGu4fWMxL-tTY92Fgb3334oevBUF68QXXBqxvXbH_hJaHKlmF6M6udzaX3jrARA7y9JRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HmhlsvLs2aoaWWWlO_Bjy4uwWJE0N_9B2zpI0GlEO4awMfhyzwkE_WfjrfDvmc7yC3Tbmblb5xY9ZvvCLceNHreOe1n9p0yj240QWMUjpjQal0gGry0fCsMLHjCEy_VIp3Jt00IPq_CpBq4nQpu0kaRFBvLnH2uP4VtwTGGlKex-HDg6bysO57oj0W44j1zAqDRn_KKES-_VbJtNpKmzUizJggZfh2DNp2HN2fJcGIt5BX9Zgg-ItoI0JHAjk1J21ewIPxCTJbQywlueTeCzGuZUr5Gh0a1LT0Nj3cVC7MH3Kn_64wQHjC3EvxDrkrs82jB5qEqmCXE4LzFAocO0M3vwAMWhhoU7cMTb3rLXDCjujP9JRo4cNJvg1cgjUfoznE9VT6L8aMZstB6D25HkF8Q1GidzAcBKVCmGsolxazQ3iLdz5umakFZ2PgRtOtjQwcSFExaqnO4HJ8DZBwER34ohif9WDnDW5tisv_8oghDKCSU_EQ7Yv4la9o6ehbakaLnE_G38xCMTFBvFeFKs9djaI5_0Lhm1XW4PN2iIBOEW5461H4n0_R5aJRv9Kd5dFu8ujN9hTCHLyNfNSrqzfblG4_z48j9PDW0OlTVGu4fWMxL-tTY92Fgb3334oevBUF68QXXBqxvXbH_hJaHKlmF6M6udzaX3jrARA7y9JRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzAlNAuqqwSgXqo8NvmErGWn7enByHW8GRYhiXiKN-CS_a7OpbXtNvNyWBELH_und9x2t9cokX2yvYW7Yvkem9F2vconDE--oCR3eWK6u8CfR2AkJVXmmZGvL2910oOL-bQO0WEhjFP_KqDxrygyUN6KwWDDsdYcBO2LDWFXM33Aurf1u7vuvnVtWfADO1if9bj4GyKRatj3e87rxpFyk9UIQZJKONf4A3THfNahMwuCuQHCLck3lmPVyKjHceAcGjzCxAD8d3GpX7krns8nKSJhA6jH7ltD3PqVi0imRp4QDYbfYuKoUw3mMm8T5pC2CEgVGT1Qlib04rvIJwEe5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=KPtM095yvjM9Pwjpx4CyhhHGOw81HmTOOVTzD4M71YknlhG7iCn1wBvqkiGiQq_BhJ0mhqaIJn3IHSWJRPPojlrOVg4Bvgxe7GqqMX4rQcu_aFVIxKnKg0W6iVX48O_hfbFH8yfmxp6khNQ5dUTCUIKO44Mb2wscRgZfTNKqz3WUTMEmDIBX_kOhHkgIDJ4l5NDMvbGAJn1TEgovKlv7B65ULO-TfC_XHhGF8I7aztRq1nI6CYpNick5TDDPs4G3V0dkGvR6656aLP462Hede7_KHwjx2hZw1XClmLnIp1J1xfF2yf4NiQE85YkrZnZC4xpsfrZSrjeVZKq1Ni6fdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=KPtM095yvjM9Pwjpx4CyhhHGOw81HmTOOVTzD4M71YknlhG7iCn1wBvqkiGiQq_BhJ0mhqaIJn3IHSWJRPPojlrOVg4Bvgxe7GqqMX4rQcu_aFVIxKnKg0W6iVX48O_hfbFH8yfmxp6khNQ5dUTCUIKO44Mb2wscRgZfTNKqz3WUTMEmDIBX_kOhHkgIDJ4l5NDMvbGAJn1TEgovKlv7B65ULO-TfC_XHhGF8I7aztRq1nI6CYpNick5TDDPs4G3V0dkGvR6656aLP462Hede7_KHwjx2hZw1XClmLnIp1J1xfF2yf4NiQE85YkrZnZC4xpsfrZSrjeVZKq1Ni6fdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=pxiFAN8cwWtbMRTqhBvCcAfQZd_pzWsnMiVwHhZmcU_w1fq9EPKjULoaBGRoOaMePbH5QeF7XNQCU2P3BY2Mvg-Jeu2cf0ENPpJBDBzhZOi12ZCoROUG50k0aybB_xCxLLgP34aynjk4Y3_mRc36Qi9RgeI8Y2llLTprrCFyJjTv4Nz-oHpBNqIpMx5NPpOeSYIrC2gpCeTtvCI9bAiBr_BB_3QSMkozBwqLOnb__J35ZcYZuYuvqPegecvBfFv0780-h8f-tJu4nShuFN8tYxdQufbPLXYlBPR5lxQr9eAG4HjvGiRqIk_fVxvsaThoVthJXjCUntXR6_OoY6NcQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=pxiFAN8cwWtbMRTqhBvCcAfQZd_pzWsnMiVwHhZmcU_w1fq9EPKjULoaBGRoOaMePbH5QeF7XNQCU2P3BY2Mvg-Jeu2cf0ENPpJBDBzhZOi12ZCoROUG50k0aybB_xCxLLgP34aynjk4Y3_mRc36Qi9RgeI8Y2llLTprrCFyJjTv4Nz-oHpBNqIpMx5NPpOeSYIrC2gpCeTtvCI9bAiBr_BB_3QSMkozBwqLOnb__J35ZcYZuYuvqPegecvBfFv0780-h8f-tJu4nShuFN8tYxdQufbPLXYlBPR5lxQr9eAG4HjvGiRqIk_fVxvsaThoVthJXjCUntXR6_OoY6NcQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2LaRMVINU9n-llKrdoCbfS1m3_2tq5uO1GFpQ0bNpUFl0oh2xAIdoXP8y1IqlTkXQVpT3IK7_aGxuCLWRigy0iFk1uymY7BPvAeMRSeJa1PZR0OC3m4dsAHFZCvbYs9d1RtjQWCSCbAHlVbhoKSuU710Nb5Cmbiol5DneVaaHVt8m1RFSAbnbQuplONovDH3enS_CZefbreYtJI1CQY3OM8WC6IoGY8F3ES3cEBAc48QC0ETzF60td7LOPwtN6c8Bm8vQshjDRZODAePZLAA9h-yo2zeLSJcLUI7xKnvKFwokrB3sbSdA4dqJ16kd3oGr-MUqueCUDjVwJrEuypRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlYKvXcpx9Utnvx0hq3ftMymGIWxO_v6KNic31lK-A2YvERf4M8WjXGH1CXRZw5xdBZObA5ZKsPeAeRNz7cQIHQSRYyvjU-Z9weld-LEOfHQbDEg0aA3_fsMplpJ_9RUEuKfsUNDPDh9_sZP6xgelN-EPAioyivNbKaq_SNiNfS0E0o3ZE07Vk9h4mdTBa2NrlsDeSDyYVQzFe1V64amlnVfX1rqDzF9emghd55rEs0CWJteaiyEbOiEEciEEF0gWOC7m4AjNd5uMS0yIRW-ygeX470nPR_JuMYpLY9cH8CNXycI4Vp-ehFrj1I3K1A1Ti9jPCkiUeimMEJ-8WsR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqtWFRuh4BTN0Z-Wqr3pU-QPrUISnzI5PhA3AQH9NmeP9VbZTnJSEIfzw36tlS51FeJ8UQ-q230RFlkxnp7tIG6IhmYz0sJimycPlppZUqGs4c2-cChWIyNqIhWi0wnM93eC5eP9J5608kSYE0YZh1Gs7G-tHKoELJlxCMrY3L2N85odxLqzsC4eI2_aQ0fIHoq0He7EXAcVXNNvx7NR1i7QvKhuIBdU5B_StF7Ppu7Am9OT8EW67E8nOgjccUHyIcYJ0iOz4oeL-TQBaWlj1oalcsQQLndhbzsxwlgUHn_4PvQAUWt5bfc_E0GPls9Rwdl69ghsODDlPwEww5WHGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=ucCTgh3LVIJi1NMvytBy5nawrMKBQaUkhryqDAC01kPu859zo26u0SP4-LxAz3Ij7NI8DeK3u70DQAAoqzKe4ub5h3UhlrPxMXxLKNJtfW_HEpmdiQON8V4u61Fam8sS-xR-arhO0ofO5XT0z43PpISY6GTr_drPA_S_5E4gcrUO5fea8yyHwp8s8wAJoGNAWFYAao8G-0kWLwC_C2VWJutr4KosrHAVoD0N0hG4sdvN9bmcSghWvgJcxCwem7FLHBUWaE8U8ysYPGvTw-Tjv_pv_PbX9JB0jFqLeVfskb05THo1Nrp7qscR1xDcLo3741oOD0GmgssyYI-U26b15Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=ucCTgh3LVIJi1NMvytBy5nawrMKBQaUkhryqDAC01kPu859zo26u0SP4-LxAz3Ij7NI8DeK3u70DQAAoqzKe4ub5h3UhlrPxMXxLKNJtfW_HEpmdiQON8V4u61Fam8sS-xR-arhO0ofO5XT0z43PpISY6GTr_drPA_S_5E4gcrUO5fea8yyHwp8s8wAJoGNAWFYAao8G-0kWLwC_C2VWJutr4KosrHAVoD0N0hG4sdvN9bmcSghWvgJcxCwem7FLHBUWaE8U8ysYPGvTw-Tjv_pv_PbX9JB0jFqLeVfskb05THo1Nrp7qscR1xDcLo3741oOD0GmgssyYI-U26b15Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFnmOYJhvDyMYCt0_3xAQmib-d391PDP3RhV3Ao2yy7-bNNlD3rDho33RAAl_xQodTFWze__g6rIbDAgGmGQ9owI6JlfT3PV0Tgw5xOTEkJoa1geUIDdfMlVJ9L1-6Iv7g-hhXI-t5SL0Kb0O0D7ZhO3e73uH_xHWU5hs8lcPC_I43HUqQgPnMfo8SLHdFXFAUgvwQXLQD1sDkgs8QMBDtQMEZjt0ahgUwSZWgqq7mhErNanUbap-Ndt4j_R32Oa1O2TQk_AofZdZsY0AcrHsKvDcHU32c36vIyXQq6x9ngXFAnwl_jG9_WO5SGZvyau33mCZ4h2NhSppwbzsUlfFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=Xt32rYwSObWs3GW1P51MQcfaTqtS0STS5JizaF0BFIYwHxY9E9152UzI4GTwnMv0KflGDHsaNcuMlPsxaHCefMx2njLwSMVVVdIFnnxDlNh7TnF_AFeVtmKYxM51hUuXXOZoOzeXIiEYb3omAN9vK0b4I2K1oqCfgXDYGMjjgpWRmzmji3DSBH6prM8_xO23hT4_-lHcTwFfqU-sxgtFrfJkYxvXiJX5TQ7u4DYyJOZeDEVUqeIfOFV_wnsxASJetk4XEZNQ4cKpFzmiu7RRgXqZnu-8Wl5LcvbTI0ED4TIsfULfzfv-DOiW_NLU3R_v7F_Lq6vWcKUUrgr3tVXHSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=Xt32rYwSObWs3GW1P51MQcfaTqtS0STS5JizaF0BFIYwHxY9E9152UzI4GTwnMv0KflGDHsaNcuMlPsxaHCefMx2njLwSMVVVdIFnnxDlNh7TnF_AFeVtmKYxM51hUuXXOZoOzeXIiEYb3omAN9vK0b4I2K1oqCfgXDYGMjjgpWRmzmji3DSBH6prM8_xO23hT4_-lHcTwFfqU-sxgtFrfJkYxvXiJX5TQ7u4DYyJOZeDEVUqeIfOFV_wnsxASJetk4XEZNQ4cKpFzmiu7RRgXqZnu-8Wl5LcvbTI0ED4TIsfULfzfv-DOiW_NLU3R_v7F_Lq6vWcKUUrgr3tVXHSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=P3EM9G4rZBFrl0xReWyqkarOfCqPKWu8TyiPqQ3-7uJJxSFYVanM56z1maT546Dd7GMCPSLlROMkRIyrpoOKMCCCc8Z13bsT4p4aW1sWHWdYQXCphiK97RCAYy6fOH5onjqI5rZh5-kxUNU2ClUr5UKZPKuWKabh1UQiE67QESUxXKLtaeXSxIj5NgWos2r_3jX7ZIV_go2s6AS8Za54Dt9R7d8uQkoxOsyPMBaSKaErNit59jSVQoLMmxUj6EjcPq7vf9NgNySyloUj1mUvIdVjlEaIjLOM_pa4nB2TGa-CITRfnFLzzUsbf_-E3oxFyS82dzZgWXkAMTbksDNz3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=P3EM9G4rZBFrl0xReWyqkarOfCqPKWu8TyiPqQ3-7uJJxSFYVanM56z1maT546Dd7GMCPSLlROMkRIyrpoOKMCCCc8Z13bsT4p4aW1sWHWdYQXCphiK97RCAYy6fOH5onjqI5rZh5-kxUNU2ClUr5UKZPKuWKabh1UQiE67QESUxXKLtaeXSxIj5NgWos2r_3jX7ZIV_go2s6AS8Za54Dt9R7d8uQkoxOsyPMBaSKaErNit59jSVQoLMmxUj6EjcPq7vf9NgNySyloUj1mUvIdVjlEaIjLOM_pa4nB2TGa-CITRfnFLzzUsbf_-E3oxFyS82dzZgWXkAMTbksDNz3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=rOKAk3a69Mi4NkldxlrZ-RbRHeJNAMLTaxXb0R0ZUwasjlfiBV45GAwuAcwEhhrAQo7x31HUXeZB_kvaLkfsof2fPLamzrhcimFYB_kks4sA7cMfv43AaYRc5uLs0R5nHtnVMKcp4eA_MKUNQ-CR-6LDeTITghYTYQGqurt2sAK3t5BK4SPtaMtuAKN91I33SMJVEtObif5P9EyUrMInK8k9dVIQ1cUEiCRQCj3bt8_7RL5JwMoblNwLSCIl0_tar3-fmvGqbUHEQnf-hZvvPtMdXjTlMtQDL1DUu9TRn_Dq4fC21fdn_jc9H2OWtg74SWYzsm7JkzNi_-jykOz-cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=rOKAk3a69Mi4NkldxlrZ-RbRHeJNAMLTaxXb0R0ZUwasjlfiBV45GAwuAcwEhhrAQo7x31HUXeZB_kvaLkfsof2fPLamzrhcimFYB_kks4sA7cMfv43AaYRc5uLs0R5nHtnVMKcp4eA_MKUNQ-CR-6LDeTITghYTYQGqurt2sAK3t5BK4SPtaMtuAKN91I33SMJVEtObif5P9EyUrMInK8k9dVIQ1cUEiCRQCj3bt8_7RL5JwMoblNwLSCIl0_tar3-fmvGqbUHEQnf-hZvvPtMdXjTlMtQDL1DUu9TRn_Dq4fC21fdn_jc9H2OWtg74SWYzsm7JkzNi_-jykOz-cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swQLzdNfmOQlMmsaRFeje7VO6l6WJTu2NGodxZN8UjHbeQNanmQOuoH9K02XLcWMvi4LdbH3PgFq1ZzdJ9VO-6STs9mgI3-l8qqquNr2JCQfAIetfnHvTQn3lZU9H0emx38HXg2W9uJZrEV8mZ76i4lXUpcTPhYYvacaHjwJ_uZVtk9MxadoUbN8yU5u34bvhXXwGsIiykDYzw8MuzDEfayxZZuNEZD_rsh9STCWyzGdfDRkUm4bM9kegzl3vO5l0lxnXWOhFVqiQkb87nxMOoMhcSyZXFsmo3jZHUFsdUI3vFLwBMP0Fr6T7Z0E1q3LNRXnfemCu3EGgVMd-9ZUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn6FfIiFsd6pQTyYdnuLQBHEJxJ1Z7joKFgNZs5oUODjBlvDVSNKS1-FnXCHFbqawZPBZ5jyr136ePpHjvSeLABe-sWN71UaufmRXe4i9zqyRrULLleiQXUOQ_jMxxIXY8aveCnFu5p-3k7p5UzAwUxBN7RbICAuVfBENxdDYaXXTxfyt790EhDeHoixnoFZ7KalWFVtRHIC14V63bdT7LYW0ppZDdDB4a2KWhYNS1vWRseu4IH0hGGEXnaUFlcpmx0auxl4iIGCiigBPoDPfVcCr6NG65FxddBWdEkuyWNkdyIPjutoYbPSJSbbZnjcFcOKjDycmzRZMMeC7YBlaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paqjPutVVrs4IIpg_gnH6FyExvqFrt7bC3f7ZQoH3yeDMF4pNb4k1muMxE-GYc0sfd5D75XtMb3TheZL-Au30EIjpxcELkmVLIkS3vGMOZ0j9STAlDV9h5E3T_uN1HGUc6ihp7_Jynhn2yfbJRrypFTM7rvSDxholRpe92qWGcSJrfKTIKfDD-6VEUWL3jUzSyJ5SfOCs_tPnksU6qO6Fwgna5gti-uB1miPVnNLbY6QUsxO4BGd3OfnsKclKn8xWEhGcXwD_uwjsxDl4JgnyJuKjl-lWtivvFoqYgQH9V5o8AQtp1GZhr9YWS3ZVIje3LXlxpJ-pX1M30kDDSJUJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNQgrJLosXepIDKJggYJ5ZEMJvCzEvo2Q2thRPF5kv1In83WomK1PBxO4FP5uZzrpYH6TQ9VPa327rMzzTdxnl-alHcXCVINti5T3glFgNjfqPznCl3afuH89i9ilDuvWeteQQ1XDtPTdZ0LkEf6kQ_boAFjheobl1YL2DV6iOO2_GkYfOuAdnTCuowsZnqEvgJijgyl74ExV1ke3X06Ylk5r_hQdpMSbiaDlDVtURgxipJp3WWQFcwhriVcrdJN3CiAWLFMEdzTsryetMPH1V4dwMX7Lq2nvoDUhm0G_pdN6M_fitgzk0SCMHbcv_qsMNJDopodDaTrj_2ISCvhww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=GwNPq1CdfmFRVJWqzFZTOTm_xVvpl0LiyRUQOQrxHCPj0Si7lWUF98q5CcgCN_vy8_CsK0dPrlq45YPJflGvtTwMPIB488gPY2qNc300NTcTWPR-KyBXWLHmDp3VwXdJ_LhKLlUzoqEymVg-2H-Xaom2eJ3cjWMp--VyPd06Ddiyimpa7ZXxwnqS5GohdJJoBX2opN0KldfV90URXIEP1uJT-1ty1n9VhzDw_SQcrekwlabV5MMGPfbaIabKPLy6WmgOtw6CTgBJwcEa-wluaVJgn8E3aZciRQVpQ50Vkl1uxoF_MHNJM572HeW3d2Ruq8ydZX2c7_Lnd6zmOQ-h1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=GwNPq1CdfmFRVJWqzFZTOTm_xVvpl0LiyRUQOQrxHCPj0Si7lWUF98q5CcgCN_vy8_CsK0dPrlq45YPJflGvtTwMPIB488gPY2qNc300NTcTWPR-KyBXWLHmDp3VwXdJ_LhKLlUzoqEymVg-2H-Xaom2eJ3cjWMp--VyPd06Ddiyimpa7ZXxwnqS5GohdJJoBX2opN0KldfV90URXIEP1uJT-1ty1n9VhzDw_SQcrekwlabV5MMGPfbaIabKPLy6WmgOtw6CTgBJwcEa-wluaVJgn8E3aZciRQVpQ50Vkl1uxoF_MHNJM572HeW3d2Ruq8ydZX2c7_Lnd6zmOQ-h1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«شما قبلاً آن‌ها را «دیوانه‌های دین‌سالار مذهبی» می‌نامیدید. آیا هنوز هم فکر می‌کنید این توصیف دربارهٔ رهبری کنونی هم صدق می‌کند؟»
🔴
مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ببینید، موضوع این نیست که من باور دارم این‌طور است؛ واقعیت همین است. نظام ایران توسط روحانیون، یعنی روحانیون تندرو، اداره می‌شود. همیشه هم همین بوده است... البته در بخش‌های سیاسی حکومتشان هم افرادی هستند که ظاهراً انعطاف‌پذیرترند یا تمایل بیشتری برای همکاری با ما دارند. ما در حال مذاکره با همان افراد هستیم. باید ببینیم نتیجه چه خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66841" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66840">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345e633380.mp4?token=lt4dTll9Q-BnVSbH2MsHTEw2lZ_35Vz8UhhYSnGv9O6hr5B0qzzUz66MefiAUdL6I7RcU602e2Z0E1FHcm2-rP7dEJ1U3je_82SqkuDD9CR8uabIqyJpmov83_MeuJ8W2YT3ftW9uvbX_RAHw4bOtuYnSUcRWhNkwQOEsSg2NDqOGkvrx9cR7uivMbF4RQwZ7Q-ffhztK98J-jjctyCjmx8Y0mNt1Ty-WrKVeNMZMIIu6cSXbdtDY80WL2tbf1wvM4MwB4rKts9LCaHi6-HP_XlrkKiUBS2KlOu5s1wAptHm9pBnbUkIRVPo0yzSCr896LHQR8ip8bKZdfbh-RRQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345e633380.mp4?token=lt4dTll9Q-BnVSbH2MsHTEw2lZ_35Vz8UhhYSnGv9O6hr5B0qzzUz66MefiAUdL6I7RcU602e2Z0E1FHcm2-rP7dEJ1U3je_82SqkuDD9CR8uabIqyJpmov83_MeuJ8W2YT3ftW9uvbX_RAHw4bOtuYnSUcRWhNkwQOEsSg2NDqOGkvrx9cR7uivMbF4RQwZ7Q-ffhztK98J-jjctyCjmx8Y0mNt1Ty-WrKVeNMZMIIu6cSXbdtDY80WL2tbf1wvM4MwB4rKts9LCaHi6-HP_XlrkKiUBS2KlOu5s1wAptHm9pBnbUkIRVPo0yzSCr896LHQR8ip8bKZdfbh-RRQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری:‏بهای بسیار سنگینی.
رئیس‌جمهور ترامپ این جنگ را آغاز کرد،
و وعده‌های بزرگی دربارهٔ تغییر رژیم داد
و وعده‌های بزرگی به مردم ایران داد.
آیا ازنحوه‌ای که آن را به پایان رسانده،ناامید شده‌اید؟
شاهزاده رضا پهلوی:خب، نمی‌دانم هنوز تمام شده یا نه.چون همان‌طور که می‌دانید، هر چند ساعت یک‌بار ما یک توییت متفاوت از این
رئیس‌جمهور دریافت می‌کنیم و ناگهان موضع
از یک چیز به چیز دیگر تغییر می‌کند.
بنابراین من خیلی به هیچ اظهارنظری
که مطرح شده، وزن نمی‌دهم.
و در واقع، من فقط، می‌دانید،
کمی دنبال می‌کردم که
در به‌صورت زنده چه می‌گذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=nRIj5lgC73Y8DzNKmHYkhrzVt5lLopsH_p1XTuOFaAw_3ew9vYx8NhhXuzAf0fkLWQGPT6WAecQyly04GsrrJLCz61TVGbv0tTQ8K_9wnHKXaePVi0cG4YB2D68I7pXaiXtgY6i3f-_qCCP-53tDZe7RCrgvb9Cjb6fo_h5PSTYwcCuPUqOnoVT6baT2uFsXkb4o1YKBzXJ_JP100uYDrBse7H40sAN9I9EY6QYdufMDHNL0S7M5mJBAxzCFqkQYFg0SSs5BauLd-FkPpTHJjnAJkoyMRTzV5QLvpX6R9jap8j_zUbQAGOa5Dk8XQ8gRK-KZYQ3PSTNFfdP9myNqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=nRIj5lgC73Y8DzNKmHYkhrzVt5lLopsH_p1XTuOFaAw_3ew9vYx8NhhXuzAf0fkLWQGPT6WAecQyly04GsrrJLCz61TVGbv0tTQ8K_9wnHKXaePVi0cG4YB2D68I7pXaiXtgY6i3f-_qCCP-53tDZe7RCrgvb9Cjb6fo_h5PSTYwcCuPUqOnoVT6baT2uFsXkb4o1YKBzXJ_JP100uYDrBse7H40sAN9I9EY6QYdufMDHNL0S7M5mJBAxzCFqkQYFg0SSs5BauLd-FkPpTHJjnAJkoyMRTzV5QLvpX6R9jap8j_zUbQAGOa5Dk8XQ8gRK-KZYQ3PSTNFfdP9myNqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/affUCy0bMoRgwUj30q3oalwpZwsoj5YnGlUBYTT7-watKxkUrFWGl7tWkdvMqiz7XEvhc8eUF5PD0rx2t5PR_bwuStgPRyAn3lWGawYlXg6in_OeBJgpJJ2H3eR2cI6zRsWe98lv7BtfepMipa6G14urlSm5WL1CPMSeXi_SsBKTBOtUaJKieMGPkOrXU4jtBGxGEJ9vQSNcew-DrpoY5DlJpgE6m1hBXlYbAs-_QasaNu2f8MJuVpHvI3uP580vUODUqHdHjdXCyJ41kpzedjpF5iz5Y8T-nMnY1pXXQ-AI2VWJAzzxLKbw_b2bmLl64GSRgmTdhNZQYCt-dv_VhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=VY-T1zL_HnZP2C5vdsdw3yBJTrivZdfAdUWl4AD3vJWKmBzIsY6Go82bv2LjmKt6ACW6Wez7eG1bJPdQ4n_tcCbpqaoxvrVUOASp69t-0W42SfIM4eJ70MkH7dH3IjPMhhcC7Y-pEBeVL91lT7sIgAVG66-mUIYjOEIn_mgbRR01rKgRSnaVnxVXJ6W6xWNRuY4rag_Ya5tMyGl6dwTgm-5BTKlH3Oq-ELiAigaGQmq4F4mxKQ8tNBwetkRjKGzWcLL-jmR1YLUSwbruTRRDQqCVhNEzPFWSsG08vQcqeWTmkFTMRO_Y4xZ6Xy6uhaRRcjreReVQ1lOW-C_-sOqo2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=VY-T1zL_HnZP2C5vdsdw3yBJTrivZdfAdUWl4AD3vJWKmBzIsY6Go82bv2LjmKt6ACW6Wez7eG1bJPdQ4n_tcCbpqaoxvrVUOASp69t-0W42SfIM4eJ70MkH7dH3IjPMhhcC7Y-pEBeVL91lT7sIgAVG66-mUIYjOEIn_mgbRR01rKgRSnaVnxVXJ6W6xWNRuY4rag_Ya5tMyGl6dwTgm-5BTKlH3Oq-ELiAigaGQmq4F4mxKQ8tNBwetkRjKGzWcLL-jmR1YLUSwbruTRRDQqCVhNEzPFWSsG08vQcqeWTmkFTMRO_Y4xZ6Xy6uhaRRcjreReVQ1lOW-C_-sOqo2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=DQX-oJsOYESRm9cb5zAuOcISybsuqI_WzAS4raWfhOQksPVikn0YUQ8Y-F0xN9ozT4mY-PjfD_omqs91yRgxK4tjoARLd5ipHMQrDmjjlBiA_XH2fL1P_S1t_NzYqh7HpC2snVXi1a8K_dOmkiEchdvAYLwy1d01rcosY0jPPpjmjdyAivzA11Ku-1h399ryxgzN2A8355ZkI9W4rxDRYJKA_GuJyFnu4j_uys9noR7Dj7WyVet_tEjUkfN9lla77Jp-Bowi4XNdceq8Fu8KSa5myj1wX724JmRJMwVjXZ_BS2a4nPNTqDrmBDs1DM7PVmuT81srSsyVq8UwgrwmaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=DQX-oJsOYESRm9cb5zAuOcISybsuqI_WzAS4raWfhOQksPVikn0YUQ8Y-F0xN9ozT4mY-PjfD_omqs91yRgxK4tjoARLd5ipHMQrDmjjlBiA_XH2fL1P_S1t_NzYqh7HpC2snVXi1a8K_dOmkiEchdvAYLwy1d01rcosY0jPPpjmjdyAivzA11Ku-1h399ryxgzN2A8355ZkI9W4rxDRYJKA_GuJyFnu4j_uys9noR7Dj7WyVet_tEjUkfN9lla77Jp-Bowi4XNdceq8Fu8KSa5myj1wX724JmRJMwVjXZ_BS2a4nPNTqDrmBDs1DM7PVmuT81srSsyVq8UwgrwmaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7aGvUBnlyMfEtE2RnGVtFOkc_boG1nJ0t4AJMvYbwWBORoJsmtIgJYpTEH1kp-e2xm8_aVmtjSCsKcKup6kjJblPW2bEgHRRnalyqR2xtrCf6LeLWsNpT4VBZK2Sy2ohZ9eoMhcxvrJJOVWGmQmvUFEwm4lvqJvXm895tIDFFAvbNxGhSCdsl8lMo96FVPEu8KES1ZOed-F3LE4-2Wp0O1UJAgmEabGc5pTKiA288ZfE3xKlMQJ_c8Zlgrvb5mQR7z7lexCDGjrqubwyrs3qdDBeQqy7FnRQ0FHhANziQT5kW70pC5ldNyhrIA_gnvPazo433cEs8NCmDWMKysQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=TBY-USbBbdQs0QlV-J9MS_SdCESIEu7U5XXoKi__NeWIfVR4-lDAnGamgMBo52jeryimNJXDXd5393R3WzHxO5pYzDG-6xwZ3GmPgr5EFAeq2fOpgNLNJ_oMfjfEvYEmxofxN0yOQsEMQBQp3ZuYx88edG2woBYM6uy1xiYcQ-GWuBtqhqRJeab5h1GEU-f3aTMOC_tSuRfMVneb1mYp_Wm27Bt74lnWk52Uh7BWPwWtiyUJZUKj3nGPVWq7TlIhQEgzdsWlU9mwQf_bShtJnB5ax52bclwS9yWihq8Oa8ugfj0pJLt1FjvG5xcAaKJ6uf76LILTI_qJOoJD89p-ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=TBY-USbBbdQs0QlV-J9MS_SdCESIEu7U5XXoKi__NeWIfVR4-lDAnGamgMBo52jeryimNJXDXd5393R3WzHxO5pYzDG-6xwZ3GmPgr5EFAeq2fOpgNLNJ_oMfjfEvYEmxofxN0yOQsEMQBQp3ZuYx88edG2woBYM6uy1xiYcQ-GWuBtqhqRJeab5h1GEU-f3aTMOC_tSuRfMVneb1mYp_Wm27Bt74lnWk52Uh7BWPwWtiyUJZUKj3nGPVWq7TlIhQEgzdsWlU9mwQf_bShtJnB5ax52bclwS9yWihq8Oa8ugfj0pJLt1FjvG5xcAaKJ6uf76LILTI_qJOoJD89p-ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bp2nrIxNDBzwdPR6ldPbFF9ZM6NpdSwFJ5UaKm-rerB3ilIx5KgVwljkN_yBvOW4Al710yd5mPCEgJo43tIh727Y_2bJKPxfD1R8neZSJtD1Fbq-Wp2YKvBXEIULkL8VcapO7m6vP8HDXt2aY4DrUyYL4-49bsD4C8JmLZ-LlduBGep-pHVh6a9iHJaDxWMBL5kMSF-NHsWfokoOcaUjXtj_l_eCGOsFd_zgYZv3tbeeaiZN2_OCk7PrkbCAId2EJEtQJj_bfiC3KZISKTM8usiwr4tiMyf1dAg1b33tQSjwkMF66sVMgM-UfZ3pqj17lX9rqg1QECcbF1xywVWaRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQfuaqdwWfCyXNbKzDcL8ng8IMX8sqGa3F5IiLtVTGXc-vbgKpHi8dNgVYCKcjroJsNfr7M4YHT3f9MffsvlKJ_hRu2AE4o1DsrK79warEpxol0F7MJ4lf5LXEkTxJfU6RLVB6Z9kPDSFYeXjOkLASNYV2OhsRmkm8xYLKs1ZXRqvYpr4UijwRRVasEd6mmAzG0RdTIG2rR7_KEK0IKHGA60HwK8i8cAJDBdjGj79en3jmVVUnulv1sdTKmQ0dNkbMpeMBCidTcHMBOtvjOWhCBYNH_i6pKyZTc23xvkEIviTJJKb25f2gwzFpXT-z0ygsCAcA0wGr-0xIixxoEtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=N1DWkSegRm5EWYTBIrCok-0dYkMzEpbWrmDs19nA64Cv5t5dTWWPjVgYj6gJHLCyh3cTlntUNiiAf-fclW4Zpvhc4WYAnnDPBDtJ812OS9HWybBrnrXOrytBCa2Zbkn8N3TKUgd2OPS3-sfY63CTykim2LSzUEuZ2Rm8wzqQX6Vpl-wzGMUFJgimzU1Mw6ti3W4lOPj-inGFFV8MD8PUACLk1en8IHM7WsOubW6bEmh146dxelHryFmfaM5WI0iZx-_XyOQVcg_tKdWuK29Oran2kx2bl_D5b-XrFdR-tgwT3kVBknJI5CTiQL9JAo4WPOlxLzVkVOxJCpxnFvOLyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=N1DWkSegRm5EWYTBIrCok-0dYkMzEpbWrmDs19nA64Cv5t5dTWWPjVgYj6gJHLCyh3cTlntUNiiAf-fclW4Zpvhc4WYAnnDPBDtJ812OS9HWybBrnrXOrytBCa2Zbkn8N3TKUgd2OPS3-sfY63CTykim2LSzUEuZ2Rm8wzqQX6Vpl-wzGMUFJgimzU1Mw6ti3W4lOPj-inGFFV8MD8PUACLk1en8IHM7WsOubW6bEmh146dxelHryFmfaM5WI0iZx-_XyOQVcg_tKdWuK29Oran2kx2bl_D5b-XrFdR-tgwT3kVBknJI5CTiQL9JAo4WPOlxLzVkVOxJCpxnFvOLyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=d_AAJ-NR5_VlWyqyv9cbQpKFxdiZNDpnB16O3ZfIp_y_VVyfvFz7eiDTZvu73WhKilIcFXKKuKnvwpTVSoQdTuJoZ-z5fO4OqxLkb2OXNcTBRFe3OZaEan-SqSjWgIs9G_LpBRg4OQf7cRazudympyIL6eZou8oj8ChDZWeFqYxwTm8ZgGkf46V7LDy0OJx7lL4suxNCk2oLpOTEEPbEOvNLm0sAMFniXdqNWqT_ALtbepU1oUIsel1kkBRd-ekFJhn5SkQOenM_G3nPvfmse4_6FkpixaIiD2zKvMAx9tV0ARFKW-HcUzsUXGF7Ea_PI9pW1i1GYMh70tYTfSKwWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=d_AAJ-NR5_VlWyqyv9cbQpKFxdiZNDpnB16O3ZfIp_y_VVyfvFz7eiDTZvu73WhKilIcFXKKuKnvwpTVSoQdTuJoZ-z5fO4OqxLkb2OXNcTBRFe3OZaEan-SqSjWgIs9G_LpBRg4OQf7cRazudympyIL6eZou8oj8ChDZWeFqYxwTm8ZgGkf46V7LDy0OJx7lL4suxNCk2oLpOTEEPbEOvNLm0sAMFniXdqNWqT_ALtbepU1oUIsel1kkBRd-ekFJhn5SkQOenM_G3nPvfmse4_6FkpixaIiD2zKvMAx9tV0ARFKW-HcUzsUXGF7Ea_PI9pW1i1GYMh70tYTfSKwWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIt3VCCiTc-7i1wpyC1C4GEx8CsvvSWd7yKp0qoe4qLQWiAZME9IXDDttoPtYjnY5zWmJtpG4mAQki4jrwoaLePY1K7EnJMTz8I4WnrpFGfuNSgA_L86f_25H-ExfOiT6Ky4zXuoa3H5FU-3jbJx26yvJsYqpcPeWJvL1if2wOWXADuyE4XA-CSTrnoTMt0fwTZG2US7gEF4500dsIuBAk-8nQYQELM_zIK6XufDGNuOuxEql9b5NGyaCC8ps0RuUTpXgJ-lqqx8x-71XhLOloeqO6B25dUeqluhSz2j57omqIY8G2L2MKLVpmxx96LPexURMMM6XuAJIlqDTfP28Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQz78knMKK9kRjvPZ6iKqTxTEHAQP7s8HQEGZLtFSueWU5YopSfTKm8W1_RHf-JZ_ADTkjwjoT_7QLJmfrm-6m66FYnThIgmnuElqlyISO4aHCV4GtXclJORc0075fLiEsc9MhnjLQRq8AkiaC9x5t5IjlZ1Y8uuo8JzrHpNqQVK8OOj0IM2wvBee6rEj_gt0lMbMUaGRCLqsX4yIMdYBTWEhzspUmx2lfxMK1Zm43fFmDku21ieJkgjzA4QXx4a_dK3OiQ3RrQ-9P1l7PIsVNkZkvQ0NSrwm9e7YLuRR6FdV9b3_9zOlA9y_nkRdJlF-F4Y7WwxjXG7PaVF6HEMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=j7sCHSixM1O_KD_4rD0vU-2DJQiylXRsVfFwrfORTvV-zyqhF9ff_0uCggE0SgkW4x2MvSpkGTShLl6_mC-oINKNprj2m5s56bDhVmHDyyL4vRi1HeZVC221Rtt7ow6ZjjfHx2q-qfKyxN40-_QHitJJ1XlxMU53EFlYnOzc1BFjc6QqA4fpYNOfBvgAv2kEM5UjOUJFbvHxdEqOfiSPnGStZyH928RXJrKSU69aefk2bP6t8I2zoYZhF9TDC5fI2_xozRg7rQvJBx2bsLni63PCakZNCmCuqFbDWPXDoITA_JxQMUqPKwz7d6Fow1fz9GIuo8OTq_aDucmfE7HhcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=j7sCHSixM1O_KD_4rD0vU-2DJQiylXRsVfFwrfORTvV-zyqhF9ff_0uCggE0SgkW4x2MvSpkGTShLl6_mC-oINKNprj2m5s56bDhVmHDyyL4vRi1HeZVC221Rtt7ow6ZjjfHx2q-qfKyxN40-_QHitJJ1XlxMU53EFlYnOzc1BFjc6QqA4fpYNOfBvgAv2kEM5UjOUJFbvHxdEqOfiSPnGStZyH928RXJrKSU69aefk2bP6t8I2zoYZhF9TDC5fI2_xozRg7rQvJBx2bsLni63PCakZNCmCuqFbDWPXDoITA_JxQMUqPKwz7d6Fow1fz9GIuo8OTq_aDucmfE7HhcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=ullHqicAREgLyyskGJowKNDlVHoBAvD15MRPM_wOxfkXyLsbhT4ByPv5WbU4WnWW2T6G_etjChmLwaSFW85IuYBjM_eBviOYLjJ9ll45_vDGYdHJFhLJAmtrHHiWmH-7gEbRdA8q12p3NU4art9vpStztXL1lDX8kC80Fr_QajBU4nMuMSgHR3aHfK2U25vZtOoOdvMz62Hcc-ZQ7uc9Oh9kI22k9qHND4865HsMItBrMKGw6BWdhO55l4fnn3xu5SccwVYGMftVw15n5w2BPwdA0BqRN_k0bMm_R2CAkJ2FqPsYLGvPdJ9g3vVWo9TRzuwa_TU4Y-UMzdiClS8shg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=ullHqicAREgLyyskGJowKNDlVHoBAvD15MRPM_wOxfkXyLsbhT4ByPv5WbU4WnWW2T6G_etjChmLwaSFW85IuYBjM_eBviOYLjJ9ll45_vDGYdHJFhLJAmtrHHiWmH-7gEbRdA8q12p3NU4art9vpStztXL1lDX8kC80Fr_QajBU4nMuMSgHR3aHfK2U25vZtOoOdvMz62Hcc-ZQ7uc9Oh9kI22k9qHND4865HsMItBrMKGw6BWdhO55l4fnn3xu5SccwVYGMftVw15n5w2BPwdA0BqRN_k0bMm_R2CAkJ2FqPsYLGvPdJ9g3vVWo9TRzuwa_TU4Y-UMzdiClS8shg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=EDquoLnwNb-RPu12hFLAU2nixai9b8IwC_BC3uGilzUmlcoQlZslLPVmSX_qg7aURLLy8PNlhIZaPjdlOYYut69qg2iYHXLY3WCOJNso9c_w5aGiMgfNzxBME_RzIMTZx7NJs_ilE7nRPy-89HOLmmlHm-sAc7VWVS-_8u1zo8QuyHwAj15ly3UkM_PxTmTwYAIvKn58u_vZ4b-27-Cv24eE_Fuub4HwEAgElfbFujg1FNe_gE3e5SIfgpPaIYOkKrCqlswd3WEIWHaseDRourwmJpkGeDNbyO8s84159HSD4LzjMluczNKzksn3XCAATZP96hOB5sgtuDt3oy2usg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=EDquoLnwNb-RPu12hFLAU2nixai9b8IwC_BC3uGilzUmlcoQlZslLPVmSX_qg7aURLLy8PNlhIZaPjdlOYYut69qg2iYHXLY3WCOJNso9c_w5aGiMgfNzxBME_RzIMTZx7NJs_ilE7nRPy-89HOLmmlHm-sAc7VWVS-_8u1zo8QuyHwAj15ly3UkM_PxTmTwYAIvKn58u_vZ4b-27-Cv24eE_Fuub4HwEAgElfbFujg1FNe_gE3e5SIfgpPaIYOkKrCqlswd3WEIWHaseDRourwmJpkGeDNbyO8s84159HSD4LzjMluczNKzksn3XCAATZP96hOB5sgtuDt3oy2usg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=q13xUuJRuukKhmtZyk0cZTOXCsiEKUGTbuy1iKCdtHQPx-0ISCPHy5i37lMwcRIz9JdURM58Fj5LmRkGs63ZCkvTtwomjG2CZrzXry5Q0JUiZpLDLubcpH8dKU_Gau69z3QPhB844GhCJJih2CS54wu8EvWb8Enxi3W0Yy2KYD7v2Z6P_VuUt-qN1t0QWKIHO7iMnEm2plXqNU1UsBl0n_uRRnPG7ItV6sftQG-TxYFd9AUa_MIPB1L4Hzp7vJWah3xD1Ugqq1kBzZuF25hdSnczOBhqmCb2aMO7TKCGWpnqAp2YaSV3CGvNt9wrDPbvpCH68xnfy8qAV7muN9Q7cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=q13xUuJRuukKhmtZyk0cZTOXCsiEKUGTbuy1iKCdtHQPx-0ISCPHy5i37lMwcRIz9JdURM58Fj5LmRkGs63ZCkvTtwomjG2CZrzXry5Q0JUiZpLDLubcpH8dKU_Gau69z3QPhB844GhCJJih2CS54wu8EvWb8Enxi3W0Yy2KYD7v2Z6P_VuUt-qN1t0QWKIHO7iMnEm2plXqNU1UsBl0n_uRRnPG7ItV6sftQG-TxYFd9AUa_MIPB1L4Hzp7vJWah3xD1Ugqq1kBzZuF25hdSnczOBhqmCb2aMO7TKCGWpnqAp2YaSV3CGvNt9wrDPbvpCH68xnfy8qAV7muN9Q7cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR6HnCuBVPgrY7EG3QLSgOD8ajFYig9oD8crkdcknTe8VylEggELnsLr5x4UgaXBXjVvlUJpfN8umrflaTjO8Rm1d2lPNUZnsAq5fwNdg5lAnDMTdYROWwFpnhAFqfSywmdSA11oXhsl1Wz9NYZ886R_vgbgmIVF5mGg_-5yPc5m_blw9vgMWLJYifWQr8IIWtg25qQe75jxKSsaoPqi7fqXxxkehBbNWXT0_ZtDPLjmSRmsUaiIh0cS2PLSDTGqiYJ_P8xM0CnVmc_SfwTPCRu2e1FGsi9WRNkoVun-gXK0XtrcRxb0hXnUad_S9CzgZvs_69l6jI_b-QEMx0PmqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=u3oNq4_bXULJfrggjEGR7LZMsY4dmtFBKymSmgshke2G5PpksnpDQ1dGs0pGLkakhzJxlZsZ4T556ND9Totnf9ttNW4j5CMAg5SmUasDVnDDTg_uyv-zQogmOL3SECv1TGpaT3iIipszcGQINnN23z0PGQKjt8Y1jU1q1MFEX5Um0AQ4RlHflXnhZae5dvq1uxK_WgAVA7u2SCkpRrNlOneS3lSqBzQ--rg1KTq0-azBn_zfOu_ikQh3IuyQK-3IR1XBQVHnCHsf1qUv457JVGHZoqL3wm5HOA0w0VVVh44Qf0SizIBSemY8MSTFUbo9f0viVsTtR1blTLLK7KiuNzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=u3oNq4_bXULJfrggjEGR7LZMsY4dmtFBKymSmgshke2G5PpksnpDQ1dGs0pGLkakhzJxlZsZ4T556ND9Totnf9ttNW4j5CMAg5SmUasDVnDDTg_uyv-zQogmOL3SECv1TGpaT3iIipszcGQINnN23z0PGQKjt8Y1jU1q1MFEX5Um0AQ4RlHflXnhZae5dvq1uxK_WgAVA7u2SCkpRrNlOneS3lSqBzQ--rg1KTq0-azBn_zfOu_ikQh3IuyQK-3IR1XBQVHnCHsf1qUv457JVGHZoqL3wm5HOA0w0VVVh44Qf0SizIBSemY8MSTFUbo9f0viVsTtR1blTLLK7KiuNzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDzL7XZe_14X0sKk_cmFV4tSQnzQzQHchMRiRSVT1r4yx9CpTT8v7iJierVq1FHyagNFGHLh8ruQzMEUUdgAVn5RzBY-hTgFJTSJd0xX3-qly1H-sq-9ISrsxd0Dgw46M1B6HNxqMqwuadh-E_J39LdrO94ZM973XXG7yPulAkPaTxXN-EGoNeu1E2aPwG2tOjOZoKf4sYG2bA6rzpWMR-YAlLES70zCGvsGBZneIELWqZLo3Y0UYQfUp7i5-G8GCyvisLod73CsufA9J-c4lbK9fXst3aKFR9d2ntJ0tIvg3fjZ64H-znWZ4q_cuIMIeOKVbMFhBUShBHCtqOU_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=fTQSa2f6j64i_Nx_zIE6wGDxcdwxw6ZQ5FpARhif8GEE5XgyVL-FZriqQ9UTJSzS_DeNHgg16Yu22Uml32oeeQZhUHEvO2RoZktWHvpEmiOan-2GRwcE81WaxdQEg6nkNH0oZVLJb1Oe34VgWHcNlQjiAeVgNpOkn8eg4haD9GjfcIIjUqhkHFONdw6FqsM6qLt9meTFDsqSMnTp7OmXQ6qwhPTfa4syrQcXu6K1IgKPIkHqwB7iEHSWY-xLWNGMfv1udwwcBMG4JwTq_kqDlMF9K-KwzQfc4d1nMLLHSL-5_2LMU8Ta6Nvd7b20DsjxuvOYECI2dOJugyi7P90CJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=fTQSa2f6j64i_Nx_zIE6wGDxcdwxw6ZQ5FpARhif8GEE5XgyVL-FZriqQ9UTJSzS_DeNHgg16Yu22Uml32oeeQZhUHEvO2RoZktWHvpEmiOan-2GRwcE81WaxdQEg6nkNH0oZVLJb1Oe34VgWHcNlQjiAeVgNpOkn8eg4haD9GjfcIIjUqhkHFONdw6FqsM6qLt9meTFDsqSMnTp7OmXQ6qwhPTfa4syrQcXu6K1IgKPIkHqwB7iEHSWY-xLWNGMfv1udwwcBMG4JwTq_kqDlMF9K-KwzQfc4d1nMLLHSL-5_2LMU8Ta6Nvd7b20DsjxuvOYECI2dOJugyi7P90CJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORXJzMXjw1fnME12ZfazDqKbBBELxVdMLe5jih8b73MqYinvtaFXMqnM1aNimtUULRdGIP6fnG0qSjQgOtad93TuBSTAroSehzQJN7sllNmAihJ0ANCvjzkCSlGabYy4Rsps10FtJc0VnCZ7qqD2bS-JhfBYCyVFJQYIUuHl5PghWkIeO58llVe2GsNM3Jb25azgjhWU_Q2CVBS_YrBPCP3zy3T5LgCdTFmUmffm50VQqlHx5nMSq-HIFcZ82rlrNpxsenzeeheSDxbpHTjmO7nzQKDrWcYSazDto4hAhYo7qnA7gaIGp0vi_h4lPHmRsXB0NQ-fpzZYjG5o15dPrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=isDUqYaCeQ5rQRyfghvx-m81eA0zrf3f5KiyOIg1VcMxL_0IHkcWNowu-7cMUs3mSBTUX_iF-BDUI1o_DC0L59OLcE1G7gMvIIITqgvuY0hO0uaE12djzH6BJ6RbyUpbicpiwzVNrbMBgioXKgInnlP1aFT-EzdVzZIixZyxqyaKVUF4loTXmkVqk8V-xEZXkv8qZMMm1IjZEuRSJslRJB31nonrxOO897M-jATrbMh-k7Ym0Tlwb5k7POX600HDA5ih7IYrmOgwXV3cn2A9_bk_d3meN-N-El3Gh1C-OTfF8rkiJxIGWtbQREy2TvqIBhBtCPOttUe3emnDG-Nckg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=isDUqYaCeQ5rQRyfghvx-m81eA0zrf3f5KiyOIg1VcMxL_0IHkcWNowu-7cMUs3mSBTUX_iF-BDUI1o_DC0L59OLcE1G7gMvIIITqgvuY0hO0uaE12djzH6BJ6RbyUpbicpiwzVNrbMBgioXKgInnlP1aFT-EzdVzZIixZyxqyaKVUF4loTXmkVqk8V-xEZXkv8qZMMm1IjZEuRSJslRJB31nonrxOO897M-jATrbMh-k7Ym0Tlwb5k7POX600HDA5ih7IYrmOgwXV3cn2A9_bk_d3meN-N-El3Gh1C-OTfF8rkiJxIGWtbQREy2TvqIBhBtCPOttUe3emnDG-Nckg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9gC2qjhN8_beVCRUPl9bjJ-hHS3QpbCDdeumSpH7pjqIGdmypRNsPwCZqN6qQIlf47-U0tqgH9cKZsUPZ-9X5RKZSycB3uDLcKKeHpNeBZEzw_1Owy-l4QIbICv11zuHD4FcM0bedMw4mHD5a17Iepi6Z-hDPkMJzMWiVAUWtT3VIXnll9TOYrbgn0-zNgpqioL8a9ay2L3d_JhXGiXn3CeigHql0G9A4fuWVwgeafvcEnrgfaaZRWD8n5eY2JluiuZCNR-3aGGdb4YZNNesCmAjCoqBJaPwls8-fmM-nUxTw-O5Z8Bg86ILxvqDk5AxXlmqWXbIXpPXquGOcuxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=k6fcW1t24JRYYOAVz2PhfCO0c8lYYWrd1tV5-WS80ZDTZKlqB78oc41TIpVQBq1OZBYDDmzwPJ0TDQ7RZRJmzTRacqM2h0OQ0qK1HnSNdoBEV5shk1nu3e2kHYPo9kFxQ4SgLwKWF7IdXU97QBO84OzRJmdAHckX-PFcesxa-Im0uGKGzbjoNAFnF5cWhyw-gHqONNfLo-tUHpNAVQuqT7e4aTJSClyiXHuIqGIZurB8TrClp0LbnCJxT9PIfEtrDGdUjqPRuTOjEN_GiPSspBx-sv_O6v7c0Y7zdVB4_LN824O-GyLEplgqUE9qruIreZ9c4CKvT0X_Q1teo3WSAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=k6fcW1t24JRYYOAVz2PhfCO0c8lYYWrd1tV5-WS80ZDTZKlqB78oc41TIpVQBq1OZBYDDmzwPJ0TDQ7RZRJmzTRacqM2h0OQ0qK1HnSNdoBEV5shk1nu3e2kHYPo9kFxQ4SgLwKWF7IdXU97QBO84OzRJmdAHckX-PFcesxa-Im0uGKGzbjoNAFnF5cWhyw-gHqONNfLo-tUHpNAVQuqT7e4aTJSClyiXHuIqGIZurB8TrClp0LbnCJxT9PIfEtrDGdUjqPRuTOjEN_GiPSspBx-sv_O6v7c0Y7zdVB4_LN824O-GyLEplgqUE9qruIreZ9c4CKvT0X_Q1teo3WSAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=cn7DH-b8hfAUO7LtnHl0fhC5x8X4WSYA4mWShNK2VGfxCR9mmOLG_OWsHGf1VgCa5VCWMpWuL-9hqf9OIMlVtN74ChDl0kp0h0UisQkVnlbodHuWQRkfcXKRmmaJEj0NiNEGkdhKU5j9Oo2bzV2LTPQOHxtRb3te3SSyKFfpC5-u1WAXPLay92Wub0zY-Bvx_MhSFXU-2cYh-jmdWML51U_nPp9IR7qfKkvKIdJYg1m1NcHlwCQ0lxjOKO78w2lU9tj3h561djpHNIrXQgBuX8KRfpMiQcvF8PFQ4jB7tAw5QurvNV-cpXhMUVHHuWCFTZzxakUAy2dcmlgW3XHiog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=cn7DH-b8hfAUO7LtnHl0fhC5x8X4WSYA4mWShNK2VGfxCR9mmOLG_OWsHGf1VgCa5VCWMpWuL-9hqf9OIMlVtN74ChDl0kp0h0UisQkVnlbodHuWQRkfcXKRmmaJEj0NiNEGkdhKU5j9Oo2bzV2LTPQOHxtRb3te3SSyKFfpC5-u1WAXPLay92Wub0zY-Bvx_MhSFXU-2cYh-jmdWML51U_nPp9IR7qfKkvKIdJYg1m1NcHlwCQ0lxjOKO78w2lU9tj3h561djpHNIrXQgBuX8KRfpMiQcvF8PFQ4jB7tAw5QurvNV-cpXhMUVHHuWCFTZzxakUAy2dcmlgW3XHiog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml_AuEG8h3Sr0D0pamnsRVSCxU_Vz0Y6_jrUfgMB_Ndn8hvJ8lEOwveH3WTMeewVbh4hFSbFwJCS-S8ARpbWNrlwx7LEkoKcNqCiMwWGqPT1K4TBanPfn9zcyFQgZzsjKK5ea0uInLwNzt_sio7ePyn87iHIGUW7RhZQLAL4cHj2SIxmN97GeRfNkGuLGbCJmZ_Cqvvq79uiX40iXv6xVu2XJs5dUBvrqz9uu-pzi-XBzUfArPU4n66mqIecigBFPyjR-BifuRnud41YF6Moh75rB0A5Xsacy61M3kkPEh-LjTMQ64fFxk92b7oBhLlLPdjfWdW9kP40GQIRQofhsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=rDzPF_oedvpRuocId-FDZLod3F-3JFF_iZ-W-o7VKCoq3szKgq7e5z9Bz-pIYdm0oJI_QPkoWOUxrQCybkznqKullaFRbEeZeoedmwrgJFZAkUnNFsvdlNlon82nekDO3Jd5UcG2bPjBXz3suXxltiIXZ8_7tcT66bt2X0a446QuNm1KU06HT8Rq9HIi74N-EmoTbyWz-a-FJ5SmOLq2CaiSDrHgJ2cDq5Bd1eWaPUdXj_yIfMZCB4L3ZYJHnCMQmYa_G34QHG34Q5SAG6Y7mImZ2Ch80l1_voZtIYuv2T8JzcoIDtRlcx0cboREbyNQ7XBQv2VPSf-JfwpSf7u71Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=rDzPF_oedvpRuocId-FDZLod3F-3JFF_iZ-W-o7VKCoq3szKgq7e5z9Bz-pIYdm0oJI_QPkoWOUxrQCybkznqKullaFRbEeZeoedmwrgJFZAkUnNFsvdlNlon82nekDO3Jd5UcG2bPjBXz3suXxltiIXZ8_7tcT66bt2X0a446QuNm1KU06HT8Rq9HIi74N-EmoTbyWz-a-FJ5SmOLq2CaiSDrHgJ2cDq5Bd1eWaPUdXj_yIfMZCB4L3ZYJHnCMQmYa_G34QHG34Q5SAG6Y7mImZ2Ch80l1_voZtIYuv2T8JzcoIDtRlcx0cboREbyNQ7XBQv2VPSf-JfwpSf7u71Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=f-KjwH9wrfRInYrYQmlMcHxU3VSXBuf1M5NIZaj5I5f9kfv43WUTL_1ClmQUt1X4GalXScbxuSqseDwqYFJhtJUSPwhZjoCf2itBgQvkKKWa2LaZme-rOYGA5ZW7iQmSdgCZZ-9JlX_vqV0L9nV2ojm-Woc0IxstW28vEASmGT-fqtqCoo83EPJob3erZwl1iCRL1VujvChPPfQM35QiaZAq9JaTN92Hl84GXf80ULiv1VvgXhwBoXC-kiXykeTbJrT1K6FtK2SPaa-p9spsooaNPjy0e9Fi7WfBfYWveFlfFzLFklshjML16nXyi7rgTNdChpc9FDQmnoXtriZ-dDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=f-KjwH9wrfRInYrYQmlMcHxU3VSXBuf1M5NIZaj5I5f9kfv43WUTL_1ClmQUt1X4GalXScbxuSqseDwqYFJhtJUSPwhZjoCf2itBgQvkKKWa2LaZme-rOYGA5ZW7iQmSdgCZZ-9JlX_vqV0L9nV2ojm-Woc0IxstW28vEASmGT-fqtqCoo83EPJob3erZwl1iCRL1VujvChPPfQM35QiaZAq9JaTN92Hl84GXf80ULiv1VvgXhwBoXC-kiXykeTbJrT1K6FtK2SPaa-p9spsooaNPjy0e9Fi7WfBfYWveFlfFzLFklshjML16nXyi7rgTNdChpc9FDQmnoXtriZ-dDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=Rx7_hgO0YaTdW-aJYioAVgdA0nHwCbYtoISZHLYTBIwarGbh9qI5TlqhBPToZf3gIS7s5k6Llv9GpPJG5kVfEFuf08P7vARKccOLDZekFh4R7ixjucKbilKHwyphqy6DqBYtdYxCppuECVTdRMqwIgDvUI4u3l3QsrVlu1NSFh1aNdopGLiAJrkLt3jDQf15qY2a_AZ_ubp8rLNSqc6sdCRQj-j6TBO4FSFT3Mq8pXUNJ7QIX7fTuZaUQHzkrBn0NAxqm8EmKcECm4rUMNybfVTxatIrDk3Al-5ZC9eLVR0abhizM46TRUy1w2P_SLbFx3L5t93vTncBX65N08rQ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=Rx7_hgO0YaTdW-aJYioAVgdA0nHwCbYtoISZHLYTBIwarGbh9qI5TlqhBPToZf3gIS7s5k6Llv9GpPJG5kVfEFuf08P7vARKccOLDZekFh4R7ixjucKbilKHwyphqy6DqBYtdYxCppuECVTdRMqwIgDvUI4u3l3QsrVlu1NSFh1aNdopGLiAJrkLt3jDQf15qY2a_AZ_ubp8rLNSqc6sdCRQj-j6TBO4FSFT3Mq8pXUNJ7QIX7fTuZaUQHzkrBn0NAxqm8EmKcECm4rUMNybfVTxatIrDk3Al-5ZC9eLVR0abhizM46TRUy1w2P_SLbFx3L5t93vTncBX65N08rQ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=O-haDzmVU49rN-EES6SD7ZsHr57vlrmz4LyHf6LcqVsHWQFINC3sVfvu51lGxdiVPeLNcLxoGkHnhbb7ocbcz8B_Fky-TBsbBSgUku4rInqNCzeFOwVAtFADt7AYTj93xoSEfwxQRJeYxo5E5hr49cInF0LlJdMvbCvdIRAN_eDPNA3o70jH7Z1_MfGGKWw1t2r84MB0trxaIuLhX2q_LDMmx1HSGvPYe4u9B-HJ-9njkLZ-BzwMGrsJAC_asIFuk_agNuH2pX700B2vHyW_efQHGE6msLGzDefS_X3EDl21GKAVeMpl_vc47DrT-Ezb_ZNnKpUTm5o_CYdNBKLrEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=O-haDzmVU49rN-EES6SD7ZsHr57vlrmz4LyHf6LcqVsHWQFINC3sVfvu51lGxdiVPeLNcLxoGkHnhbb7ocbcz8B_Fky-TBsbBSgUku4rInqNCzeFOwVAtFADt7AYTj93xoSEfwxQRJeYxo5E5hr49cInF0LlJdMvbCvdIRAN_eDPNA3o70jH7Z1_MfGGKWw1t2r84MB0trxaIuLhX2q_LDMmx1HSGvPYe4u9B-HJ-9njkLZ-BzwMGrsJAC_asIFuk_agNuH2pX700B2vHyW_efQHGE6msLGzDefS_X3EDl21GKAVeMpl_vc47DrT-Ezb_ZNnKpUTm5o_CYdNBKLrEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=M7G3ZFgE2Gj40agLq5xWC84390CJBaWGQ3-qz5726SFbk2Ti5OvVn4KH36ex5Fi404kfC6kisDaQvzGP3DD3fqjKYb3xhivMyU5sgTjoNkaM-_q0yDTk9ZSdn0jQXYaZzCRnwEZgNgBNltVcB4R3ik7287ul2Wa3dk1tkQcTmTv3GvBzCd0aj2T_EH9zZIi6cIyefsUhDLTELZq3xM-qHKETLp59XO_AR15OqApf9Go_x2Fe-7oc2A4jCzN5rpMN6RB3JOgSiOyKssdZcD_64Sz4jsxWXCifHlY3cNWMhkm7O93Rthr9tQ7ScRseW2Ur4a2mFMkmUT90xekHL6ilRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=M7G3ZFgE2Gj40agLq5xWC84390CJBaWGQ3-qz5726SFbk2Ti5OvVn4KH36ex5Fi404kfC6kisDaQvzGP3DD3fqjKYb3xhivMyU5sgTjoNkaM-_q0yDTk9ZSdn0jQXYaZzCRnwEZgNgBNltVcB4R3ik7287ul2Wa3dk1tkQcTmTv3GvBzCd0aj2T_EH9zZIi6cIyefsUhDLTELZq3xM-qHKETLp59XO_AR15OqApf9Go_x2Fe-7oc2A4jCzN5rpMN6RB3JOgSiOyKssdZcD_64Sz4jsxWXCifHlY3cNWMhkm7O93Rthr9tQ7ScRseW2Ur4a2mFMkmUT90xekHL6ilRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=H9_ZoNT906O_B9g3W2LTei1tVeWQomB3DjxlrgYuC6GruPgEQFLJJjdRC1ATCRk99WSveXpTEcUf_v4hdjJSjIUBQkO377CNguLHZFcQhYSYZGvGCyY4Iqj006Bk-49FeIEaUbYeEFYKmPZhKVVpGpw4bU3mbQInhF9rwIeE3HXTua6at_9MZzpaztJtq1R7YMabcX5kcipiDV1iYDZOKSF1t1PhjTyMDwF5kmg4JnQPStgeJtQ8V4Xxykn5NgJxZ9D5z8BF14Q_zmN64_anmQVB07HEGV9TQpqnRxGR4V1xXH5gdYiaFed3O-VxbvYE0fFb6k1Nyn74F_sXSikurg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=H9_ZoNT906O_B9g3W2LTei1tVeWQomB3DjxlrgYuC6GruPgEQFLJJjdRC1ATCRk99WSveXpTEcUf_v4hdjJSjIUBQkO377CNguLHZFcQhYSYZGvGCyY4Iqj006Bk-49FeIEaUbYeEFYKmPZhKVVpGpw4bU3mbQInhF9rwIeE3HXTua6at_9MZzpaztJtq1R7YMabcX5kcipiDV1iYDZOKSF1t1PhjTyMDwF5kmg4JnQPStgeJtQ8V4Xxykn5NgJxZ9D5z8BF14Q_zmN64_anmQVB07HEGV9TQpqnRxGR4V1xXH5gdYiaFed3O-VxbvYE0fFb6k1Nyn74F_sXSikurg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghiHVi7WwD_EC5onxqpbBZiWR-UlN1kTZbnWPzS8fkYjNTSWQsLAsPA5CU-USZHAZiGo2Fmu2VSrLeWl4wp1k8qwwBYC-80vh3u1iODMX1-12h7r8-tKd8kXsDHqGZmkEEJ5DnVAn61oF2tQCkiB62du9DwoIGc9pGNlXLv77eLn_Re36oTcbkQwAwJRuzwWKbu3JX8o3OgGnYE7-rStvfrqMZpKGhi-Yxpd8XG4GYM5EHf3kced3YT5JJdL842FKWlFRlgah71C2SRk81lMhwmX3wC7cyKqWWFGDsdQJRTVESyLqhQJW9aIrUIBXlTDRbgiVyNSF98LMjNEKBxiYYes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghiHVi7WwD_EC5onxqpbBZiWR-UlN1kTZbnWPzS8fkYjNTSWQsLAsPA5CU-USZHAZiGo2Fmu2VSrLeWl4wp1k8qwwBYC-80vh3u1iODMX1-12h7r8-tKd8kXsDHqGZmkEEJ5DnVAn61oF2tQCkiB62du9DwoIGc9pGNlXLv77eLn_Re36oTcbkQwAwJRuzwWKbu3JX8o3OgGnYE7-rStvfrqMZpKGhi-Yxpd8XG4GYM5EHf3kced3YT5JJdL842FKWlFRlgah71C2SRk81lMhwmX3wC7cyKqWWFGDsdQJRTVESyLqhQJW9aIrUIBXlTDRbgiVyNSF98LMjNEKBxiYYes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=Qq23JBsxlS8OiL77ZfyDz-yAjpvfc0AXhXPadK41Jtrqy61rE89dl3Xyy5Qiz0RvRTeNy5RUpNLXkYI_SPyC2pNskTgY0YAYY8oABWp6McU_YP5V8HU19yoj7AluAyVBVdor_IAQOLnC386ZI9nlMDuV9OVZ8-hRH5-kCrMbdTk_oFfJMVlqIBXvYzTMvG6gtOcs-18IQJZFPSnYqZ3UmgKki1p8TsmCJ0q4_VrUU98_v2sLrhtsE5MU-lLUP-lqp3Eo8ofUsCEL1qq5rwAXTEsUJjeeKBcO0wEgQWKAtKMe4OFtv3noHNEriP9o4r0Ojtrx-Vm8bmekUeLNw9qmgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=Qq23JBsxlS8OiL77ZfyDz-yAjpvfc0AXhXPadK41Jtrqy61rE89dl3Xyy5Qiz0RvRTeNy5RUpNLXkYI_SPyC2pNskTgY0YAYY8oABWp6McU_YP5V8HU19yoj7AluAyVBVdor_IAQOLnC386ZI9nlMDuV9OVZ8-hRH5-kCrMbdTk_oFfJMVlqIBXvYzTMvG6gtOcs-18IQJZFPSnYqZ3UmgKki1p8TsmCJ0q4_VrUU98_v2sLrhtsE5MU-lLUP-lqp3Eo8ofUsCEL1qq5rwAXTEsUJjeeKBcO0wEgQWKAtKMe4OFtv3noHNEriP9o4r0Ojtrx-Vm8bmekUeLNw9qmgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCNg6lomeJjhsbyBk4A__fAZRI__UT3wbs44A9JnwmAC2W1WVm94v7wyeENZa4hHekaOt13BDYEL0qMFW95cmZiKGFSvY0hPOVugqmcU9926eT5-L9nxh2ZyXBsPOet2d_oyjyp2n2ujpPQ1iEKo40pWQWRD8czDir1u14kY3zGGTyz3fwCFSV6Q-DlfsYndJf0l1avfFjEHdp7wJ3hsR8CWfhNPVewbaxmBDu51oZ2j910cSyu9-CMGQEKXEPcDL9mY95fADl-cV8GQn-N9NFcN1007UdfoFUSDk0mpSUhYh19XR-_P9l2Kxrd4HxXCwt-Ub8VSIxxYD30ki2sxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66796">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66796" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AkTfnGtUjV-DmIb95DF670FhYurrKy7qARjAVSd8sUPanjjxi8b6fuERCnSuu-7C2H6fLBXhifeS6NkpnmyJOS9XILQyyxSvwnfemTxPAhTnBc3QOppT1emuNfZnzu6nrQ88tR61xz1j6DdKlzJa0JGR8EilyedTadLVkDZP9uGaWUHjtN9wngw9N0vAkEeMi12yl0O0yhXxzYd32YI6Yei40ZnEPQPHRnr39aOxDiKDwETkwnHjBtFPuQtE3VvIvK_OwB_PjZwikKwXn7sv9a6ZrLB0awQQPR_5CUARvTs7ZSVS6ILSDzno7AQBoJECnh25x6AP2_dvb5kIzFLvtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66792">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=HZRmQMRoILBjU02o0inhrWVtE9p-ohrlDz9enBdUkSekn0yJgepQeqDsdRM3aI_WtXdafJtqzMTuGf0NpxdHNYbqIZLBP80ij9IvpwRSRjVLT6fhPb1PWzAf_RUPU88HkPixWlgVTB-CIwCGr8tRVzrXM1Nn5eQlolGxqjhJHrG2-YUWiWSmkX4GoK9raUZkLdW_Y_ZU1LvuMBdKT8RiB6uEbwxqgJIC6lJiz6esl4ePz3_mXqUvmyUITktwqXGeou6Bg0iR8PV63C1PQSt8nzeM3zbhZbwPcUAAFurq8ux1-9aCPiVx7cmAbM8AM80ioFtEM3izbG9M54-uTo4Szg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=HZRmQMRoILBjU02o0inhrWVtE9p-ohrlDz9enBdUkSekn0yJgepQeqDsdRM3aI_WtXdafJtqzMTuGf0NpxdHNYbqIZLBP80ij9IvpwRSRjVLT6fhPb1PWzAf_RUPU88HkPixWlgVTB-CIwCGr8tRVzrXM1Nn5eQlolGxqjhJHrG2-YUWiWSmkX4GoK9raUZkLdW_Y_ZU1LvuMBdKT8RiB6uEbwxqgJIC6lJiz6esl4ePz3_mXqUvmyUITktwqXGeou6Bg0iR8PV63C1PQSt8nzeM3zbhZbwPcUAAFurq8ux1-9aCPiVx7cmAbM8AM80ioFtEM3izbG9M54-uTo4Szg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
درست در میانه یکی از مهم‌ترین مسائل، ناگهان خبر فوری منتشر می‌شود: “سنا رأی داده است که می‌خواهد ترامپ جنگ را متوقف کند.”
ایران این را می‌بیند و می‌گوید: این دیگر چیست
؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66792" target="_blank">📅 01:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66791">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=KLDK7C0MhQ0KhOO_QQijuZiu1GnY35ZrlVmNz-v0-c8SMZ2dDC4ZD1koYHVrq_ozM14DZ3TkUhNweVBgY--p-bxtrkeRF0d9UuHfPJ9NegLXtKHBeb_Y6R4ChHdeD1Z1H7FKLqVVRDuiyQPiR_irumGbDpt4vzCjccFSupaGg9C7FrU6tX6X3MhYPh00nQ_i9vBsaGZcxe4aYZ9Cv-7rNVhW3Xd7xwtedqDo-6PeqMTErJAMI2DWrqF5xTg4soWqaR3G2kxLQpaA0Eb5dRfhIE5kYbTrGKsgwssj9Sk9vzI7qk9IwrMXAiCk36ZSmR-dq1OJDSVFRvHqDhTEnIi9iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=KLDK7C0MhQ0KhOO_QQijuZiu1GnY35ZrlVmNz-v0-c8SMZ2dDC4ZD1koYHVrq_ozM14DZ3TkUhNweVBgY--p-bxtrkeRF0d9UuHfPJ9NegLXtKHBeb_Y6R4ChHdeD1Z1H7FKLqVVRDuiyQPiR_irumGbDpt4vzCjccFSupaGg9C7FrU6tX6X3MhYPh00nQ_i9vBsaGZcxe4aYZ9Cv-7rNVhW3Xd7xwtedqDo-6PeqMTErJAMI2DWrqF5xTg4soWqaR3G2kxLQpaA0Eb5dRfhIE5kYbTrGKsgwssj9Sk9vzI7qk9IwrMXAiCk36ZSmR-dq1OJDSVFRvHqDhTEnIi9iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره حمله به مدرسه میناب:
«نمی‌دانم که آیا آن‌ها هرگز خواهند توانست این مسئله را حل کنند یا نه.
موشک‌ها از هر طرف در حال پرواز بودند.
کسی گفت که آن موشک متعلق به ما بوده است. شاید بوده باشد، اما من هیچ چیزی ندیده‌ام که مرا به این باور برساند که واقعاً موشک ما بوده است.
موشک‌های فراوان دیگری هم توسط افراد و طرف‌های دیگر شلیک شده بودند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66791" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66790">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66790" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=qDD1060sLjNpgZa7aFhIOZsixTUr6oDk18wmkv5lWnsVhRjYaB9pXzWcWyyQv6wwD8mN5tNouYPncNA98ksv6n6LrTnkbDsCjn-CwQcsGqXxWWbgs4FGA_Cz8KU9sS3uRQs1Xqx7GAQT5s3pTkByowm616DnWgPZ_3yDycR4_yhyIv5JMtpA9H97q7j9g3lF5xyTt8yNhwesQi4-7BizQXdtC3ja3wT8ur8SgbMTrBgoe-hNpwzmgvMUeJ1vE7jp0QyL4OxVetozkgo85boLhaJck9N6TNM__H6KvWQYfgVoorLV6yPGDCLd3IJcHyKSQPdXTbqh3GbJhyxKmrabNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=qDD1060sLjNpgZa7aFhIOZsixTUr6oDk18wmkv5lWnsVhRjYaB9pXzWcWyyQv6wwD8mN5tNouYPncNA98ksv6n6LrTnkbDsCjn-CwQcsGqXxWWbgs4FGA_Cz8KU9sS3uRQs1Xqx7GAQT5s3pTkByowm616DnWgPZ_3yDycR4_yhyIv5JMtpA9H97q7j9g3lF5xyTt8yNhwesQi4-7BizQXdtC3ja3wT8ur8SgbMTrBgoe-hNpwzmgvMUeJ1vE7jp0QyL4OxVetozkgo85boLhaJck9N6TNM__H6KvWQYfgVoorLV6yPGDCLd3IJcHyKSQPdXTbqh3GbJhyxKmrabNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=YvxtLtK8k2VJWEYf5pIWuAqDsBz2EcksteArdkhbEr_6lsdDMLTpM18F_kJuLUBli_a9JHQ62reHQAu-68SJgSNhCK9PgAu1y2YM8oD0j36UNoparBwhwduSk9ljbH3XAGPI9WkxeUIrSCKc4gkG1cOITYplk_ZKRDwGwsxx6Yyi0eFV6ZBu7FpJYoY_jFkiRzlY5T8eWM6BiLjRO9Zk59jVaPqPxO-QKlz5b43HOOYiecTHjxK_4oPw6IJ0DNnjsw2MDMicPiBBCAKykvpTrOpXGEjP1peVJdvL4YHj5k7nqQC-6_ZQcS_h8yjbo_rBgJvLjMYzOll4cxfaNysFGjU7WhMTgwq7eRA5jlxdSd2rhYyTK32qGCwGkR4_XTi48ay7Ql6L4mEHqDwjxCm4X7SXnH5zbHNezMNnn-0kQFWC8opLrGwNu3y3nP23ypK_-hISd-9wmmwXsCSRV2aJoHZT9r62GuajvRmGxU3---WtMQ3nHZCUuHgSS8CjkGaRfq8xnv337onqurrYkpoXHMQ_Pcv99RlqcUkg4HcZd9bkTd2mWA28dyTPXWz253Ne39cj2IzBJ3LfMaF17xPQXGZPbtTpPxRkO8T13YLNqDfVOxBfkmbTb04837VU5R_7CgUorEJUEz7zUi-LH5IAHci1yBb1s12Al6blHRngmTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=YvxtLtK8k2VJWEYf5pIWuAqDsBz2EcksteArdkhbEr_6lsdDMLTpM18F_kJuLUBli_a9JHQ62reHQAu-68SJgSNhCK9PgAu1y2YM8oD0j36UNoparBwhwduSk9ljbH3XAGPI9WkxeUIrSCKc4gkG1cOITYplk_ZKRDwGwsxx6Yyi0eFV6ZBu7FpJYoY_jFkiRzlY5T8eWM6BiLjRO9Zk59jVaPqPxO-QKlz5b43HOOYiecTHjxK_4oPw6IJ0DNnjsw2MDMicPiBBCAKykvpTrOpXGEjP1peVJdvL4YHj5k7nqQC-6_ZQcS_h8yjbo_rBgJvLjMYzOll4cxfaNysFGjU7WhMTgwq7eRA5jlxdSd2rhYyTK32qGCwGkR4_XTi48ay7Ql6L4mEHqDwjxCm4X7SXnH5zbHNezMNnn-0kQFWC8opLrGwNu3y3nP23ypK_-hISd-9wmmwXsCSRV2aJoHZT9r62GuajvRmGxU3---WtMQ3nHZCUuHgSS8CjkGaRfq8xnv337onqurrYkpoXHMQ_Pcv99RlqcUkg4HcZd9bkTd2mWA28dyTPXWz253Ne39cj2IzBJ3LfMaF17xPQXGZPbtTpPxRkO8T13YLNqDfVOxBfkmbTb04837VU5R_7CgUorEJUEz7zUi-LH5IAHci1yBb1s12Al6blHRngmTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p26I5qY_796pVHo4mdO2FCOt4SoRcWPHRKpCbEtRrApZ7PLjq00CD7K2G2MCRuF2Lxx6_RsXj5ebAEE3d2-S2M4eFjvL2JaMyq5MHWYj8PAeI-1NO4-J7zQ9c2Gv1XBPIBsCkxLGgkT1JtzoqI2URTbbtG-S8YNzxn3DAbunMZjEcfyHxgJ3zra4HyyjXG3sHUyWr4tZO7lUg3kiEtIUKqB9mL7YU4P2hcOz_1G0SY8MJgargs02j07IYf-iSYrpoMoTDvkUqbq2sxe0qYfiUzc1qtSAUdOQGQ5JVSYP7Obe_fDrfDV-gkKTTIrt6Nh58EFV1xth0QLPBa0a1wXz8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66785">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XM7JGL1b7ucRovsf5MENbsAI0Ml4_KPGR9aReX04r28vrqKvuBA9FL0JzUYm5KLBtSTo3tNdJlYENVTCHI_ZI11K3ZYqlpk0T5T8jpslCGRcOUVkYZw27X5BUx2-JifE_zv3efE2iB0-iAZQgkgR-Avrm_6tSQdvjdAsaLOVsuVx_qrcNYLWFeqThP9pUWaFzAlDZ7Zzhm8LQ_gznp_AedCzkHAv1jAdV9DoMuV3D0KONMkCoMZJmqy5WiQW1OVfnIw9eqQ3FtFyUsu8UOmcSL9Rn_t-N4IkIrIkv3KVLIqElEIh0bBI3VTjCCyUJqd22twSibBLkzXoehIC8BTrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66785" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66783">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f56950043.mp4?token=jDRsFkwW9LwazA5vqFFgK0EyWkKJ_XMglUNPatoj96WMLLdVYQWZ7KD_ZZ5dxMFW_bbrqJ9l0LyVcZZ4AQYEqMEDsBnHaetHeduxowTsTiWAIRKK696V2FmYBJBuYQcyNOxX7knNLkdhtUFW2Hb0dEAKbsFqogo2HZn6Cv6ngzO_SVjdBFiPh155NrcuWsk21q6eMvnbckVQ9jkfI0dkpipYmcbouywMg5Zw6Wj5KFmD8vD5UpFk4C39OyzOsHo5Wd7DGdQOxp4B7kIlOXywrr1lcj3iXZYe0-nDn3heRUbvkwyYBLe7Exu3PS9inddLic3WZlHxqfFQwKDa631tiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f56950043.mp4?token=jDRsFkwW9LwazA5vqFFgK0EyWkKJ_XMglUNPatoj96WMLLdVYQWZ7KD_ZZ5dxMFW_bbrqJ9l0LyVcZZ4AQYEqMEDsBnHaetHeduxowTsTiWAIRKK696V2FmYBJBuYQcyNOxX7knNLkdhtUFW2Hb0dEAKbsFqogo2HZn6Cv6ngzO_SVjdBFiPh155NrcuWsk21q6eMvnbckVQ9jkfI0dkpipYmcbouywMg5Zw6Wj5KFmD8vD5UpFk4C39OyzOsHo5Wd7DGdQOxp4B7kIlOXywrr1lcj3iXZYe0-nDn3heRUbvkwyYBLe7Exu3PS9inddLic3WZlHxqfFQwKDa631tiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ازای شهادت مقام معظم رهبری چی از آمریکا گرفتید؟
قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66783" target="_blank">📅 23:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66782">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=UWJdcTut73IMump7YOHoDzjb_RHHWsCUyy78_Fs10IZ2Ybytn98ONU4qlmUgX-VjEu6Nu7MLNIMvf-0LMVJM9opyrMjDmLGFRtUX8j3TcVxeQqJ3DYcB4qhugawsIt5YDD90GCQJ5xFODt8XIainrBgeuqLI5hxxQa80yV-LnkSoqrU3uGJuWgmYK8S9Ezuf0Dgn8idZIpHGBg6myge265wJEWis8hWC6qjc1GyopUD9isrRvPmd2c6ECpo0prbz5iU-hwU7t7So0rHkiTjyoufhbq7iBlsnsnGlWAA7-Ln6ROA02oaYbnIkzPyQW6wku6YUBHuMYxBors2IAXUd7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=UWJdcTut73IMump7YOHoDzjb_RHHWsCUyy78_Fs10IZ2Ybytn98ONU4qlmUgX-VjEu6Nu7MLNIMvf-0LMVJM9opyrMjDmLGFRtUX8j3TcVxeQqJ3DYcB4qhugawsIt5YDD90GCQJ5xFODt8XIainrBgeuqLI5hxxQa80yV-LnkSoqrU3uGJuWgmYK8S9Ezuf0Dgn8idZIpHGBg6myge265wJEWis8hWC6qjc1GyopUD9isrRvPmd2c6ECpo0prbz5iU-hwU7t7So0rHkiTjyoufhbq7iBlsnsnGlWAA7-Ln6ROA02oaYbnIkzPyQW6wku6YUBHuMYxBors2IAXUd7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ایران خیلی خوب رفتار می‌کند. آنها با هر چیزی که من می‌خواهم موافقت می‌کنند و باید هم موافقت کنند.
در غیر این صورت، ما فقط برمی‌گردیم و کاری را که باید انجام دهیم، انجام می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66782" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=H0mBODrHv_BOVCbsMFSgxVM-KuNjSYdDgg5SZiiL54izOJBPvpc0SnaXDIIRwO32sHQ8_tmktdd-6M-VOYYpKHe9ip-bWUKiJKmooe69Bw_sELeBIti4DItzDi3nrYbQBy3pFKLyYERh_eaKNT685lL-Vj_jPoGDlCHaf5MGZtvR3BNlMrRirRaDjXdaGs9n_46YaqvWgf3lccOQAD7FNq9ZXtdz1L2N9fx3UquqeWTM70-YKbyQysGH0CpWwe-edUdCkRQs1P0VwP6ig5rZwZz05K7w0L1PwhgnkGituToxELmKaFw9ktghW2_SSHrv3EmR8ifuvsxJ8YgfyTSDyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=H0mBODrHv_BOVCbsMFSgxVM-KuNjSYdDgg5SZiiL54izOJBPvpc0SnaXDIIRwO32sHQ8_tmktdd-6M-VOYYpKHe9ip-bWUKiJKmooe69Bw_sELeBIti4DItzDi3nrYbQBy3pFKLyYERh_eaKNT685lL-Vj_jPoGDlCHaf5MGZtvR3BNlMrRirRaDjXdaGs9n_46YaqvWgf3lccOQAD7FNq9ZXtdz1L2N9fx3UquqeWTM70-YKbyQysGH0CpWwe-edUdCkRQs1P0VwP6ig5rZwZz05K7w0L1PwhgnkGituToxELmKaFw9ktghW2_SSHrv3EmR8ifuvsxJ8YgfyTSDyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=YXcwK-lF3AEdVubuPjzEIUcMRO-nY0drz-ImUQZIB5Go2RR-Mm8LnajR7zX6j_T_ZV9cNvgluqaccQYe7KNV1UyH61muQmO0eWuKX9jGL8DxFP5tIVBcARsgK5llUy5zm4wNlpLWCFiRAgONu_EZfXWOZrXEp9aiwNJSL-Ka78Q_Gd1cPO358ugdw1gzfXyXXXYulrlAy5SPIaZPa1BWXqVTsAYOQFNRq5lHLo3CFYX5nChz8NhnY-pFT2BLtNDwYg9DXKrcdEc7ZyvFQ5pl85y-JJ4AyESHdodMu_Ba2FO5NQV4BpOYI4zXGKwOCsq7Tiq3glmbq2TMbTuB5xiM5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=YXcwK-lF3AEdVubuPjzEIUcMRO-nY0drz-ImUQZIB5Go2RR-Mm8LnajR7zX6j_T_ZV9cNvgluqaccQYe7KNV1UyH61muQmO0eWuKX9jGL8DxFP5tIVBcARsgK5llUy5zm4wNlpLWCFiRAgONu_EZfXWOZrXEp9aiwNJSL-Ka78Q_Gd1cPO358ugdw1gzfXyXXXYulrlAy5SPIaZPa1BWXqVTsAYOQFNRq5lHLo3CFYX5nChz8NhnY-pFT2BLtNDwYg9DXKrcdEc7ZyvFQ5pl85y-JJ4AyESHdodMu_Ba2FO5NQV4BpOYI4zXGKwOCsq7Tiq3glmbq2TMbTuB5xiM5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHqkk2QnKEbp3Ujd2CUUm0GwM1GFUhSju5KMBLvNsFKXV7AmEVFQ0tJf4hPPXAt3vtI2k5ahXMjDYwTRFXN5ZJNsJHYpOzupgSrzbGDdGt_1168FJggR1yHZCb_32zKGOqKuAXet9JvzkcuwQuuFVHvLzGR4l5P4tkYa_jBPiwkBchVcSOhgQ3wXr5R1I8XC-xVYJi6DLERghCftjtpucsibQEc5j5VHTdsWm3uEZD8un7MrZb84E4IXaYO06uDgxu912m5n7HH48jcUb0wycAvp5oo5wJzGjmoFpEY6eWy2u4KJacYK5_R4R7GF_7ze51D_XE0fGwBwYKDDRCe7vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=fT4CJJc6pe1CQgAMqs5GT3vPuqN9d5j2np9Bvm1i0gZ_G0tobZ9ZJGZmwFyMBucmKF4yzohfi4RyJ6xF-gVGMq0S18C79OjYG0_L1lTjx09CJZmIkkv6V3eNlW8b28Tn0X8PM81tg8TcgMLkiJIarTyMSrhbPCRKiYhsFGYLWiTj4zTH-XI6fWpve0R1GnHlPNbNU8YpShYxVtXaQt1PTTGU5E67RC_XfCZ9NCzvotJwygwNf892Wt7OxZ9U46RJAa8-yc__TKzseOGkCJyWG7eI_P4YtNzI-nCNO53-kIg6VcSww7L6zW0pBH5Nqds31Cat8jDNhaX5NvtB1imnlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=fT4CJJc6pe1CQgAMqs5GT3vPuqN9d5j2np9Bvm1i0gZ_G0tobZ9ZJGZmwFyMBucmKF4yzohfi4RyJ6xF-gVGMq0S18C79OjYG0_L1lTjx09CJZmIkkv6V3eNlW8b28Tn0X8PM81tg8TcgMLkiJIarTyMSrhbPCRKiYhsFGYLWiTj4zTH-XI6fWpve0R1GnHlPNbNU8YpShYxVtXaQt1PTTGU5E67RC_XfCZ9NCzvotJwygwNf892Wt7OxZ9U46RJAa8-yc__TKzseOGkCJyWG7eI_P4YtNzI-nCNO53-kIg6VcSww7L6zW0pBH5Nqds31Cat8jDNhaX5NvtB1imnlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=dlJs7zSvr7-B4wm0eQjXxsgHbX5pWAtmnRR8VL1U2yGFjJ_gBPP3H43XtYninZxq5Dw6e5Ed2EgVnEGwlz9J6e4MWOweWR4hnPys_20_i8QuCM55LLzjqe-K63olnyiNylidGCwabY_bwU51HI0JCLU6d_moInI22463ZJjMC-zSpEzuN8DTOmBtoFXfnqXadImJYRWon-BPhJP7yFBCWtxkRTpaOcdiPSA2mdeVWgf2sLGl0Xzi4CnzpXgajnNcHQ99vNCzsNg8_ah3ZixjwJjqQADzxqk_Sv6ocaWbMarY1_oidzL77pCdck6o0TP0fLRtu2FjfBHJuPpo3UPIXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=dlJs7zSvr7-B4wm0eQjXxsgHbX5pWAtmnRR8VL1U2yGFjJ_gBPP3H43XtYninZxq5Dw6e5Ed2EgVnEGwlz9J6e4MWOweWR4hnPys_20_i8QuCM55LLzjqe-K63olnyiNylidGCwabY_bwU51HI0JCLU6d_moInI22463ZJjMC-zSpEzuN8DTOmBtoFXfnqXadImJYRWon-BPhJP7yFBCWtxkRTpaOcdiPSA2mdeVWgf2sLGl0Xzi4CnzpXgajnNcHQ99vNCzsNg8_ah3ZixjwJjqQADzxqk_Sv6ocaWbMarY1_oidzL77pCdck6o0TP0fLRtu2FjfBHJuPpo3UPIXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=sHof_uWJHCkDYw6CSjptrE9DKAg1kZwmwf_nyboc2pt5PDc5oyFu1-LfbhkhmaGdtNi7OWhDGn9zu449Vf-R7f7EV5SH7WGNcbpLhjvJxuU9W-6pjkYZs9t48PiyBjoxWlTwTJ1Xw7klocl64_F-V7PX78Y_bVWLmfJkwxfT8PLHcilvSGYVdPOwABV_ctsEpTWoYbdypl1tID0IE_O2yHQlRTg-BG76jaBOKEGZ_zTYAgJ48mMsAsLnD8Yd3nWoPDZyrpdWbza2lpvqhBvFJA0KjlBkgnd_KURAW-3f4eDL9oLmuneVHvJZviV4TJoVV3OU8jjG2OzpD2iaqRhlbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=sHof_uWJHCkDYw6CSjptrE9DKAg1kZwmwf_nyboc2pt5PDc5oyFu1-LfbhkhmaGdtNi7OWhDGn9zu449Vf-R7f7EV5SH7WGNcbpLhjvJxuU9W-6pjkYZs9t48PiyBjoxWlTwTJ1Xw7klocl64_F-V7PX78Y_bVWLmfJkwxfT8PLHcilvSGYVdPOwABV_ctsEpTWoYbdypl1tID0IE_O2yHQlRTg-BG76jaBOKEGZ_zTYAgJ48mMsAsLnD8Yd3nWoPDZyrpdWbza2lpvqhBvFJA0KjlBkgnd_KURAW-3f4eDL9oLmuneVHvJZviV4TJoVV3OU8jjG2OzpD2iaqRhlbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=Q6C6ZuSWoaGlWi3o9fJsQrER0fj_AojZa5nncrCL2rbbXPNBf3tvEvMMe5aniV-YUNXe-9-dMdrB7a_wAeefzjluT1tbnrFJVL68J-KZzNj32qf8t2-GhppgT7bQ6c5SSxWqSY2TY3xg2s16FWrbdodZCW_ZbCDj2TKQwtGSPiM9HS32jCIoVQzXwG8p44q-hRSrG72j7sYj8efPddxsTPY4SkCoabY8EKpOll8kis8coQsI6mtVGcLccOgabEgpz5ebS7JnlY9X5_oDfKxOYAt3-7b83SmFZ8EFE1wNTXhXb5qZEcwlQlRpD9lte0OFXjTLnWvkFLlRBwOpcm0DWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=Q6C6ZuSWoaGlWi3o9fJsQrER0fj_AojZa5nncrCL2rbbXPNBf3tvEvMMe5aniV-YUNXe-9-dMdrB7a_wAeefzjluT1tbnrFJVL68J-KZzNj32qf8t2-GhppgT7bQ6c5SSxWqSY2TY3xg2s16FWrbdodZCW_ZbCDj2TKQwtGSPiM9HS32jCIoVQzXwG8p44q-hRSrG72j7sYj8efPddxsTPY4SkCoabY8EKpOll8kis8coQsI6mtVGcLccOgabEgpz5ebS7JnlY9X5_oDfKxOYAt3-7b83SmFZ8EFE1wNTXhXb5qZEcwlQlRpD9lte0OFXjTLnWvkFLlRBwOpcm0DWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
