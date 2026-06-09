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
<img src="https://cdn4.telesco.pe/file/ke3b3Gc471rX_h0QW-7LvCQQIhGdjPTTFbT9vtWB-DVPMhbzrA_OG7pX3TxZoD5X9oSv8QZX08TOIblWwfUkBhCNPxfOcP_QNoL5QIFWFJ1jA65qG9oiXk4bQgj56OsJJ9Ve-UraBGRC--1hu0jT0SjtvXkoMh63rKTXfiQ1-b6NotS6pE84nyHVC9JIF_GeHEtzy8ZgtQacCd0I8cpCQHwNAJDjesPJl76r_ifUpMbhGhTJEjTAQsxvuYkqvCuFA-MhGoyfLEeHmCBGkWOsTJpaQi19Y8ygkBFhCbLFin_yV4Fv2yqWtI-kOWTg4h6ybrqZYIQwC5Icfh2bhzMgEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 168K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 21:58:03</div>
<hr>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO843QxLpW9tiA2D_1aYkZQSz-6q--JIEMb9MuEYsEcD88nPOgh_egqKgwltuFc5u3eSpr_64VKHjTcm1L0h5ujTQKa5nRUAnV5A8PZ3DJtvu3UuPTHGhO1yo85y0dhAbklw0ElDDL4QMJo4zO-Z2OfH_oyM4nza-bSB08hV_EnhB2qHQZ_NE3mMtuQPITBMjS2SXTFfrN7FFuvlk94vvTbsFGF0laofJOTJ6yWyMqhRoKWj2D_JJUEB9Ng0aWoVLvVZrHkc3ZAZg3YyO5m4qgJBha916xzyl-4aQocxFK_iiDqtyVndLJZEqc8rO6xErWwyYNGgZpGTklWf92WqQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ آریا یوسفی مدافع راست سپاهان در بین نزدیکان و بستگان خود گفته که بعداز جام جهانی یا لژیونر خواهم شد یا به پیشنهاد باشگاه پرسپولیس پاسخ مثبت میدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/persiana_Soccer/23077" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER3FZL4ywMZE5rFgqrSGpx9UzGaiZhYSf2QEO4wG0u9x5YLaNGSNTdG5ImyJottFklcDg97tP9FIqDpu1nqzUOhNWRcrSVl_AvatwpeV0AqNUvJMOsYOOH8MKt3IroItqIstSk78PPTHeH2z8z9BgYaSfwLYIX8m--cSdxnvyb7WlzUggk9qSgwqv1-Wrg2PWE81q00lq16E-09H7x7ucSzLaewe24CWjKSU5fYAzLXI_96TQ7EVz9iL1WdLkxC-B6HFUKTyNThq2HmzYhXdGW4I9hAO3vY7b_OK_rZGfNcMQbU-6XH46yBdkeJtbZEJFW_wmbcxudXIVf5Pf22l7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/23076" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23075">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUXHXJennlwGp3PUUgx0uPtspOTR0zFxEoAoO1SyzDGDjS-7so32S50sYr_gr_Ct3wtIbEG5_1fHtrjYqn6qefPn9aQnxzasVsqGHqiw9ym2hyPAycB8ur25QfY9IaQgIJtFIGpe6R-t2NFr-gvkRvl6w_ZH4oHYEKuijfvgjl0r6XuMQdNlGZJ007XAbASiHr2EzF07x1AslMoT00UeFRLiBnKoWU_wRcHHCSRcephSHAH10rFrQgYb1nTsXijJO-8BedlqLLoAMI0a5rYjGjRZzavUfJbzeiS0ZW6qMYIp-q_JQwZ_B9t1J7Wbt0zKFJRTof5LMffTGfXdFrkuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتوجه به اینکه هوا داره روز به روز گرم و گرم تر میشه این جند مورد رو سعی کنید رعایت کنید تا همیشه خوش‌بو و تمیز باشید. در کنار اخبار فوتبالی چیزایی که بدونم مفیده رو براتون مبزارم
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/23075" target="_blank">📅 21:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAdZGmKire8HXQYUqgfjTNTsy4OXXxZKkKL2HjBuoywfYDXiUFBZnpxXzJhCwzBXgWFhNWr5venFSpinDQdNXmJxiLZQMjSrOTSIFYGcwnyVntyWcupoKFziboS72B6KwBWpgYpakn4LT819wTq5jpOvoR8FneF7AevmeLZivIx_CybHZaGkB8XSvanie9-77QG3nMEczBK8CJR6ZlIuaimIds2h_v5PsMRpQLkDt4kDvu3R0OqbHHAd5ppROymfsL-Da_Q5TukKm0tEOKM7_2NXi0l0Hc8AGRqZWrAYyC5WL0YO2ddgNocc3ITxXi7Bqjmtl9F0S9hmTQDuoh2p_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/23074" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23073">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ikw1YtQZ3l2N3Pgo9r4W_3I919zdAusA5RJ7zQYsLTEnH8cvADpN_99Q6SA9Cl2m5P1IRMZlb2ZAnJf0IDT5LDgdRM8ELEd0pTTA7YluswZhxE0aUcOWLFjgVIRhJQwXkG_sDRNiYY0tB-FIUeR-pE7e22j1-v-0hV5mVFb6Oe8o7fkFhhBci3OaYFiwxLjbRWDa2LVG0CoPJBnoJBSBZHyGNXiXYRTthXkmRU5ixMKyzmUEMpm--_qTw08HV9TombBx7AjtslgUby12OjsVetKUk8jlnl4E0z4qs7wsBUm5J-Ruund0FXxJoZSWiOJU4s0X4yxpL-NMxZUjZTkfTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/23073" target="_blank">📅 20:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJXhW5Hj9-nlvwYpTbquMS1InRozyf-0CvB1XlvZ-fZgyWM4ttc0bDcmDkhVfw-CjdEbz2l1PuAUkIrNi-DyH7UbADbNi1x4EaHn5Y79QR-sj3Fssv_SylujUg719Al3kh9_7e--KOYbKi5vDAIiOIsVknPYByPhTQVlcZ6eAlreD7ENHsG_A1fsLRgTSm-DAyrCGRgy6dovJi5zbgVS0XkWzAnG3GKD3GPvU_lCd1XcoGTryr3Qj0iOgwXCrTFbSDaPhHmTMYe3K39CQ3sFn83d7ZgCOkF0mnggkeQLLvdkkNcVNo3m3HA3e5XC5soCsQQ23AGrSEsAGxcd86tprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
7 زوج‌برادر درجام‌جهانی2026؛ دراین‌دوره جام جهانی 7 جفت برادر درتیم‌های‌مختلف حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/23072" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23071">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=psf6Pmx-bWHNrPV0sgSZ4-jGbRqV638OXJrHkfzR2RxDJJ2zcKyhY4DBFD0lB7hWDKLH-KHaVop8gu5CE8z0D7ns3gdEPbsvsqUtTbDOt10Bnr06wTJbzOIGa-ilmNVXrLCb-Jvg7AhZmKdb5hoFoT9wobT_j8BPNeT5BcyY__JUqTQXe_aeQeS96zrNjZWEkC7kA72jk2fvl_kW1Yl0T8k7MeaX2Zfo3stBC46MIlJoCaimrgYpYuYUbeNj7GupHhkxvuZEBkQl_yZDcedGBiwldd7ullCzvhmvA30nZOYr746SAXBe7rHrpImmW9K-9l2c6KxJ2CLAfSV89cW0yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=psf6Pmx-bWHNrPV0sgSZ4-jGbRqV638OXJrHkfzR2RxDJJ2zcKyhY4DBFD0lB7hWDKLH-KHaVop8gu5CE8z0D7ns3gdEPbsvsqUtTbDOt10Bnr06wTJbzOIGa-ilmNVXrLCb-Jvg7AhZmKdb5hoFoT9wobT_j8BPNeT5BcyY__JUqTQXe_aeQeS96zrNjZWEkC7kA72jk2fvl_kW1Yl0T8k7MeaX2Zfo3stBC46MIlJoCaimrgYpYuYUbeNj7GupHhkxvuZEBkQl_yZDcedGBiwldd7ullCzvhmvA30nZOYr746SAXBe7rHrpImmW9K-9l2c6KxJ2CLAfSV89cW0yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سوپرگل استثنایی کریس رونالدو به الخلیج بعنوان بهترین‌گل‌این‌فصل لیگ‌عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23071" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJhnBDPI5iIM6C5gm2rD-56UlQDdJazck37kZ0RqTrfnYlU_zCkG_6SkqwNRexll87dcUsmhz2tx7N7jqLQDgKyO9HMmm3Ew7fw-uKkhVcyYuhSEk0iisP3k1wxtMRZPiZz39JnSKi-NyNeB0ocThvxyQUng08q4j871VXJEDOBnpqsVGd2gkLVALslCAw2mebAmuC9Mprrwu-e62VAw11ig1wl13vNFOCd8PtMkM5KWAqolSMS5SH-2Ek8XDMYLsi6krvTGIFYkSCq9jq47c-bffgSQNkjKutKKTWCqH1BnnZA3-jI-1aOwduVbt8go9QhVAzmDeW574Y4UnemP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: برناردو سیلوا ستاره‌پرتغالی به یک باره‌نظرش رو تغییر داده و حالا هم میخواد برای انتخاب باشگاه بعدیش تا بعداز جام‌جهانی صبر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/23070" target="_blank">📅 19:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ؛ مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/23069" target="_blank">📅 19:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5NXqAl42yoLBK80Q-OdoGd1zuheAsu2yE5NE5Fnk5cUiioEx5_5dMH3l1SW-9IYeq-zMd-XWtAsLqQfT3bA0m-KeeReawGLj_My6sX51V63ctDoiw1F1bBpqNOWUBtvNh8Q5y0WmTswNzjmuAK6c3PrH7VjrwYjt7xbV_v6sHtZ4iGodVCauqUjcxBklRgglJu3FGFuZ-1Aqd52Artyl_tj-t67QRymBND8Bm87e0y-5eEq1IkQYvGi2WVy9rpZBqDvnSbl5z3OBG0qUhLpvNRN4vXkTgBIWzYcIbEqLerg5l_-tvXZTbFdjE514rV0vpPri99t519RRInyXIIWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا: فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/23068" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUpPcmgf9sxhx4C2q1xqYlGfzsohmO4roNTOku2X_UjcHcV98Q2QwaLs8_B0ZfrtK3AB2tKPV0hF514ySnVeuVFmWvnhDTwi1QoO5gAfbOvgZAvX-f2sGdj9pu3GZy3jF8W6o4faI6D7a8EZeIJZrmqaHYF0SsKkGhYZuCLUZlUgCHJIurWIOaXzZN5mFygP4Y-QKjuOcvNcvnzP5lhRikHTkSndB1UfEFlR4vdhatxoripJniLFQQ6-dyZ5t9pc61Q-cqP_Kngi7T_3mzldFMj0xTcIeopnX8eZUgdG6rTdkIPeln17IvTMKmx1pYcdud38FTLgKSz2YMxHqsG_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
با اعلام حجت کریمی عضو هیات رئیسه فدراسیون فوتبال: تا آخرخرداد اگه استیناف نتیجه ۳ صفر به سود گلگهر رو تایید کنه گل گهر مستقیم میره سطح دو. اگه تایید نشد، ۵ تیر پرسپولیس با چادرملو بازی میکنه برندشون با گل گهر، ۱۰ تیر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/23067" target="_blank">📅 19:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsF4ta2b8NiaVBaZC-7TS6WPMJR-E6kII_i4vCxRfpCj2CNJGt_8e15oEDLwgugjhZhqnWgRVw-beNAy90b9lD2-Oj_vCRE07wyV5lG1W-WEgJqu9n7cFZyo15zgJsKMwGIB8xjR8BMMk15BBQyOlLwX62SIWe2TJ00lQYiWFPmxt2coRQuwVrMTC3BL4jrqRixxAdFv5GWT2D6rMr9PIbKbYyQkzLwxLFGNRno2alOJWKjWBVX7bxx3b0uXZ1jO3enIr61cOApZV6qpnB4AsQfNXqgqiHwPsyQlD6oWQTvIQuUkhLz3KHEoIY32iM9_xrIaO9L7jezTQnVgEe84ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیست‌کامل‌بازیکنان حاضر در جام جهانی 2026 باتجربه‌قهرمانی‌شیرین و ارزشمند در این تورنمتت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/23066" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuPSBR8UKVCJIKtyEEEpY1w4aCTdP3HigiQ7ocSCETfcFhcAkRZqirq3lc3-ymZHRbIDR8_wGLtBAiys92v3xqeMIY7vVMLfUeXdeu0nFYKielemlVaxaENI1LNdV7-Gx8uYdygEIRyXcP7nHZ2uqSVEfOF4G3KwLywgzjuETXXaTMqYEe1r189wkMXzPXmje030u5xTmGpFXlc61KqZEVVrHq-I8bSpv7JcGPGsU061PLsn6O1d1OvxnzY8bsbEmHu-Irv0KN51i0AX0za3leA6MVhc5ovtYX1fPcBFJ3Bk2FQH2OVlsDSLfCUs9VypefPNlpx0GY5uW1tejYQJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/23065" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzLKiMLJ_AqxtovkpbuiiFgRVNKCT0ST644VGydxJPQdhHgTffwlmlYNPLsFNBGaRvvsUFgqWdvdSwjbjmkBjqh2T7SU9QhAM5DK-e0i_ehnIqhTB7-rfEpVXJT7qBVlPdkOP7229ykCFm1v2Jnl0pO2IL7t3i7b85U-NJyuTjNA3-U64gkrI2yiN9eUeul02bOrP_G0avFBJUnZ8anvKjx0kJsfUgNqmCZP78ulFbdT5ifMCgJgkH-Bx79n-RPDZRpNSqL3Nj-0S8K8ZoW9BCWZp7jxakwN0eWkbCXHV-x4pbSoX4mIt-yOOj08UiVhEl3a98jOuQwDpl71T7OhBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/23064" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23063">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbeo5SUk-3EwfvE7C2Bbd4GQRYCS4IH9oecbldJKVY6tuqiiXPOlLRp6jz75RWaP6JHNPYPIPpHjOOr8SWxNTpZn2gyErMSztHrE2FJIqowuNCtk7sKAf0dZCmgQQEyvccEAErhQH1E1QKveT_FQ4MsVV8xaeElO8CObW97kXVnSZ8UYZ-XX6qWimVFwqI0wW0TDMH6dNHIbIrSjhb3ordt31DbmJ6lG3WX21mw7AkLa7hoq2uK0sq4qZD5VZALAFSKON5Ak6bCORhjXJRk4Y08IDi-rpTm52GW5_Nc2S6xpDWlfkfZ3jlMXgXWPykxK90hu0aNRFYxsmqeeLmQrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg19
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/23063" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ucx_P6uuYS9GwoLfxMfV8GaKQ5oEwjO6zgbQn696GdCZyDK-nPze5mrRaS-RtWcP-6q8vOsnXYmkskb5aTy98lgM6gwoBCZEHAV6sP9deT2TdX7a45DOl48G6RSjCX9O9TKp0ATmGEVqrggrT8EGOiARRF1PS_1gz7-_lqTpT-QeT5AD-GEIkX8Dzw8z_6ZxUligHlMPYCl-mBtAI3_lPi2muQAdW9idtV9iVdttF4hMbbQuGTzJ6_Y0kEdM7TJNa81Ac7TAklVyLhHXv-Oh7xPGoUloENBqxIQXMus6H7SW1waFUznBR99s_V4DdJkg-U_QnzaQGqo5vsKJmjHHJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23062" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49850c982.mp4?token=b-yqmNC7_E8w8oSBhHwjAqYg_nUnjhoMRYBAZPWZ0uSsWfrLLtyyDsSxyA498W1EjZhJOge88vGzTfnKqNF36hZgbKvLgCFPqcqV91vQVQ_At9eWzIl-rYROHMHVejBalFS7LbF2_wNQTAzbzGrqLyrcINY3Cf9oALnhqV1waV1ZJerep3w55wBihPu3dQnuWAj0K45zlM7K_M60mGecAsV1_MQTJtcIZI4HfHxuQMvNBc0Y2FTKKBrQ2NBBiHKZB9Fh5r7LAOT80v0EquPGJFOwaHPCK2rn0XJRMtxt9xdKFiMr3M_bR_snWewMmxIl0-VOoKjWbz6epWSUcKReNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49850c982.mp4?token=b-yqmNC7_E8w8oSBhHwjAqYg_nUnjhoMRYBAZPWZ0uSsWfrLLtyyDsSxyA498W1EjZhJOge88vGzTfnKqNF36hZgbKvLgCFPqcqV91vQVQ_At9eWzIl-rYROHMHVejBalFS7LbF2_wNQTAzbzGrqLyrcINY3Cf9oALnhqV1waV1ZJerep3w55wBihPu3dQnuWAj0K45zlM7K_M60mGecAsV1_MQTJtcIZI4HfHxuQMvNBc0Y2FTKKBrQ2NBBiHKZB9Fh5r7LAOT80v0EquPGJFOwaHPCK2rn0XJRMtxt9xdKFiMr3M_bR_snWewMmxIl0-VOoKjWbz6epWSUcKReNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇧🇪
کم‌ ترین انتظاری که هوادارای رئال مادرید از دروازه‌بان‌‌ تیم‌شون یعنی تیبو کورتوا 34 ساله دارند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/23061" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qezj7_Z3PSIJ1sNta4cGAj4ZlyWUl7UULyV9Pv0tgR9hUMqY8OfFPaFeDw8HfRE9FJpCG8C3pHXN_e5FS5fhF3A6wJd6_zpiL8mmlsRBEQ0eGA_CbJmD6nkTvM8QzAcwY-848I78riRr68WJB-AjoBoWo8DxmLuuyc5ipXzJguvwihyoLnOil9hv1x3_3pO2eM9L7rxQfB6kBDu-QB0JAxhksXedi77105bH3G_EQ7oNAvg5L8z8WYMgZo8dRAU4JNHB8y7IgJoUwJDD8idkEETTM70xHe89KGH5my_mYEznOpyJaG3SXiO22gR2Ft5zREh8mtCibCyZIjnqQRsKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krzp-V8A87Zed2RpMmPp7WuEbhIxIlBYEDFPKz3u1DQDwhiTMbRW7qq5EEp-wJpvMhipGO_VwpfKtwjushNLiNyU9wXdNCDrNzsmQinfvCgbbmXHZU7RGiF0VNJIy7jYm29CTeHeBNg47TCGBxYNgDqntyMnv11HrZsXpr9mgdNlewNlDRnioJXUTFt0tK-UOVta_PMQAofYLea95JGZoaa6ybCbGsx-FBdd7GSSwLqxsfoh1Ex-Af_AtXSCjO__SaDfeSz0GyWwvr77sat6F23jLSCOGD0t3m_dgFtXv5Do4OL1Jso2fKfdDdmHuQnKlmSZKIytAlBRpKupGPqL3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نادیا خمز دختر خانوم پاکو سرمربی‌سابق تراکتور: از وصل شدن اینترنت مردم ایران بسیار خوشحالم. بسیاری از فالورهای من‌ایرانی هستند و در این مدت متوجه‌شدم که به اینترنت‌دسترسی ندارند. پدرم یک سال درایران بود که از مردم‌خوب ایران به نیکی یاد میکنه. برای همشون آرزوی…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23059" target="_blank">📅 17:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23058">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQnsRm5rKv9COKeHpnMyQNwud_ad1Z0Achnp2LNV_s6-MhJAtn89nf5_K36yW7D21Kcq2XCC5tj6UI3YeROKdn7-QTe74U13Ljztq0Pkn1k2envR6dHCNbMiYPylzdIr4YIf2Bi5kPQJ2y0w_iMJ1Ns0bfrbbWu4KcJ8nrb72OplKB2aVin6vuAhZdZWH2j5D5Ir_otB1m2yR0h4yxTEH0m1ywlo7qYaAzRjDfOtyytbfNi2-Rj7m9rGLhwRMFQ3scntLcziOej-tdNMzVi6B7Jo9jsk5MWJvVSXJ8NNDPI_fOTpHVx7Z5p_kItnz5-ScwEk0MrIp74mUapUVKkjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23058" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayxJpdm8AMWhSohTYBEIdc-Q1vgkVB40bKCycV275wQTnXxx8jf3NwlQO5JdISc9WadjB3oFDf570Vu_oGv2ssnSRy5ioAhsDDaHpwTDk54DUNsOqvvamyZ6YPf_Cn67dfud1RG6XFDP7pQPItlg4_vwg4U0obo_qrTIWsa74qPQbLCB7g4hsuyMVzO7aOP9QBj7Fweb70yIbTpcniGkVomKgPIWOseFA_XatrQ485hUu6dyMaXJMdh7PereL9hkjgt8Bd6ZGJjB-C_dBhXJLdquoSdWL-FqEndh_XJEwx5fuirLCpZZQlW-7ByCvnUtTI9gAATT1vaVe7FJmSsqKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بمناسبت شروع تورنمت داغ جام 2026؛ سریع ترین گل‌ها ور تاریخ این رقابت‌ها رو مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23057" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQxHKV6Ia_zKH58kfAd2YcFkDMEO2ZsfyYHIUuGYZrmE6bm1oOoGcxrehrWL9NV-KDrZz3PZEfXYAvv5CnHBJGDpMZVMbgwsPsn5N_MBNLWcwshUk8TeZrXrLYFXGsWFoJwQUOzXfp8SwenwlZL2dxkn1KvhrKp0t2XlAqle87r9C1Bmg6Kcr22euH9W-OVlh0XUhJGGNDWPc7lylD0mhmNI0WZHuxeBrPewJ9fy_Jeo0g-_YXVUgFfDEFq9PIuWA625T4JrDtEvScEi9B9KUaHCCnn7htSddlS__clhgdMCkA1uVK3fTXRP2WVbXo9Ph3xz1c67SS9im2o5CPTkFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فلورین‌پلتنبرگ‌خبرنگاراسکای: علی رغم تماس های تلفنی با هانسی فلیک؛ خولیان آلوارز ستاره 25 ساله اتلتیکو مادرید از پیوستن به تیم رئال مادرید استقبال کرده و گفته اماده این انتقال هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23056" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9MwsZGnibxUquhxbGl3NFi6qWZXNHB6OIcISwdTBnFbd_zVOf_-UwN-4vIflGfG2iSt1DZyyjgcMathPgB9-ZNshmoL7rGV0kUQWnax3lJWpgsd1wNtWmKbxBx_UwVtNcpfg9D59qbBq5h0cMmgsqhBgUWt_rQRFKis42UDcmK244M9JIKRhJGadD0j_KxLGu_nR6UJ9FvJKo7LTLjvzHd7PHcuhVW332nYy9mDn6WaIlsB0zijdy3Rh-whgmcxVaFoJQauBcU-Gk3LOw96kHFem_m3ZNEiykVifsvHMO4HFTdxpRg04eJhahgR6gPGo7tdnmBltOGDhnCcaJt5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
عدالت در میدان، هیجان در جهان؛ جام جهانی با بزرگ ترین تیم داوری تاریخ‌فناوری های پیشرفته VAR و قوانین جدید پا بمیدان میگذارد از شمارش معکوس‌برای‌اتلاف‌وقت‌تا اختیارات‌بیشترکمک داور ویدئویی؛ همه‌چیز برای‌تصمیم‌های‌دقیق‌آماده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23055" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tq1_ZVeFLnwqlfLideuB7NQqyb2yNzJujAV3AGRP84uQPOmuS86ZBiUOs3Zkf9SprMQRRt43pskOmf3tiTPT6VafZj2aMvSulZCCPghH9ZKjFwrjo4lssKfmINkjyS7q--KRVUPco1xqw6mXBFQvGGNQ6JtDIe1Up6sMkkqikuUgqdO4IFeS865iwJtBxepAfhtEdMg7dss4xD6ao6dQWRhlN3vbmH6-ELC4hD_DcptKj4g77cr5AJw7Xwp5cDGPTLEhOhuGgqWgGXKUyVHDHOT7GXmJOlRFFiWkQ3xOygfjXs2HxYMdcuEYgSo5MRNQjCSG3-wBAzxfQ-5jQFanHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23053" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=NzcHMK4QQzN8Hg_YQ52-U_W35kcq7UXQ6B5H5x8iWQGEfteFTCFjmKjoeqabDz164sCtrUvM1thQDej8Ws_2bl6am4vGiWK1uqIxvZdSQmo_D-sUFA9jWGlmYQA9kJ-nYpqCkNM_s0T-XBUc4AtIjOExTXUg3Zmtks66n-mLN3VMDhVj4n-LgP0E6SviPTRQRWBgoViqQfOIKq1Np-SVfyuWdil0fhSs_Zpu2pW5acGNYGZutbPxqBvf4wlcdhOJ4Q733WJN4Um9FKhA6O5oKHcyUx_lKE2Bmy3CG1tQR0WvclDmeCOogiXsrooGT0Q5uin1Mb9uvC1Iuwf7l6VBV7EfO22BOODjVktlSPLmuh31BPyKQ8uqenDFdc0bcjDEnHv1jKcOktVSULTWTiR0sFmNVzPb5rEsplpxKj-oi8EdfdCwEEx2m2zbpTVzCqagmhDW0YX6xM0JYieh7jffGjY8jV4e7onYblk1bq6tZ4N4Amol5SBAfUiBaGtADfzHGQc8ZnoIN4uhalIWsSZc1IkM0gX_-kTlUDmbBENRynYCVgwMsbVSNAgFts3iakepstbmekPGoannmpNhtSzz9I7CVqIGAhepVFEVKQVnY096epMy1M8C6996T7j38ylU1Imh3Fb5T6zPCSnY_IUomdATEUVxZvjWPvb_wljuYhs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=NzcHMK4QQzN8Hg_YQ52-U_W35kcq7UXQ6B5H5x8iWQGEfteFTCFjmKjoeqabDz164sCtrUvM1thQDej8Ws_2bl6am4vGiWK1uqIxvZdSQmo_D-sUFA9jWGlmYQA9kJ-nYpqCkNM_s0T-XBUc4AtIjOExTXUg3Zmtks66n-mLN3VMDhVj4n-LgP0E6SviPTRQRWBgoViqQfOIKq1Np-SVfyuWdil0fhSs_Zpu2pW5acGNYGZutbPxqBvf4wlcdhOJ4Q733WJN4Um9FKhA6O5oKHcyUx_lKE2Bmy3CG1tQR0WvclDmeCOogiXsrooGT0Q5uin1Mb9uvC1Iuwf7l6VBV7EfO22BOODjVktlSPLmuh31BPyKQ8uqenDFdc0bcjDEnHv1jKcOktVSULTWTiR0sFmNVzPb5rEsplpxKj-oi8EdfdCwEEx2m2zbpTVzCqagmhDW0YX6xM0JYieh7jffGjY8jV4e7onYblk1bq6tZ4N4Amol5SBAfUiBaGtADfzHGQc8ZnoIN4uhalIWsSZc1IkM0gX_-kTlUDmbBENRynYCVgwMsbVSNAgFts3iakepstbmekPGoannmpNhtSzz9I7CVqIGAhepVFEVKQVnY096epMy1M8C6996T7j38ylU1Imh3Fb5T6zPCSnY_IUomdATEUVxZvjWPvb_wljuYhs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی‌از آندرریتدترین‌مثلثهای‌تاریخ؛
شاید اگه بیل فکروذهنش گلف‌ نبود و ژوزه اخراج نمیشد، چن جام از جمله قهرمانی در پرمیرلیگ رو بدست میاوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/23052" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yew2zAadQ_MFxtB3ZcgHzWzgOoUVanpvxJBpD0sHHEQ_iDUx331AQaYHTvg0Z6GnxV0munlYb1TB6fTJ7lclcDbAAu5UisWzDvr8YULL3XXHpxe-kRNd-Xx0KOclgS6_c-sw1MOl_UCLqsQYX-F1TvLGq2zV28cSvjOLZK5WHe_ZSZBM8AonWoXE-H2oCx9Iuo1-llfdzpxNQLHUq6n2Mg0QL8AZfirnYKoOjFV6ZsgDxhRDavqGeJPoUr09O7fd_l9OoNfMgTrco3hRdvvqP56-rvjMLqTFRr8ifipwh-vJuUwXvByJNMdsPM0lDznRh6DEjYCc-_4G2bXOvH7l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23051" target="_blank">📅 14:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23050">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=buWMit-iRtLDuIvztztIzRbLd2mxJhl5DsgLzWy4PpLbR6FYjboe_6EJC3s20yqhcBxMG54fUr3JqPFLPDz6L-pnN-RtSVT3YgGGisTi2yrQSpEM_NyQDjJbegUsi6UsKipgxpyyuBSig7AtX-T35RN6ZiMQhnktvl6ruiWB5Tl1uAamHukx1sBtpdOaz2Os4B5HMHHZrVudBkzG-ZmYfCV100ONaS_BOWYjjsdjyWKK2P2uZofU1-HB1rqzYWsCwjrcc96AmKt9CTlnVtPp6Gx6iX5zFYm0wLctcnaUILlQTW6w4T2PFliZnI56kGGDwocgv_oPZG2D8aCD5JgBzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=buWMit-iRtLDuIvztztIzRbLd2mxJhl5DsgLzWy4PpLbR6FYjboe_6EJC3s20yqhcBxMG54fUr3JqPFLPDz6L-pnN-RtSVT3YgGGisTi2yrQSpEM_NyQDjJbegUsi6UsKipgxpyyuBSig7AtX-T35RN6ZiMQhnktvl6ruiWB5Tl1uAamHukx1sBtpdOaz2Os4B5HMHHZrVudBkzG-ZmYfCV100ONaS_BOWYjjsdjyWKK2P2uZofU1-HB1rqzYWsCwjrcc96AmKt9CTlnVtPp6Gx6iX5zFYm0wLctcnaUILlQTW6w4T2PFliZnI56kGGDwocgv_oPZG2D8aCD5JgBzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
تیم برزیل در جام جهانی ۲۰۲۶ با هدایت کارلو آنچلوتی و باترکیبی‌ازستارگان‌باسابقه و جوان، فقط با هدف پایان دادن به انتظار ۲۴ ساله برای ششمین قهرمانی‌جهان‌واردمسابقات شده. اندریک قبل از آغاز ماجراجویی‌هاش در اروپا، تمام دوران رشد و شهرت اولیه‌شو درکشور برزیل و بویژه در باشگاه پالمیراس سپری کرد. اون با درخشش در فوتبال برزیل به یک پدیده جهانی تبدیل شد. رسانه‌ها هم سر شوخی رو باهاش باز کردن و روز تولدش رو با پله که اونم ۲۱ جولای بود و ۱۷۳ سانت قد داشت مقایسه میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23050" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23049">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tsg2etBdzN4lX2AiQmYHts1zp0oFDD6-4C4Xwg3I8_LvQDtBqzrNkl-7TgmvSn6jt3oJ6z7U-hFsI7dsJlpcfXnh2rtZYKJvJ6WnUhmzxfLQ4wnVmupzplYzCNRId3hw4yujFdQZLJodt-kGUKu4NXQWznckh27FUgR5kZaW6HGteYZi1jfsVbRqUyBn-TYOYs6NXIdD8AlyxDueKA2ScI5ZokJvc0BBLNZNA59vNGP0PUkLXeMyrw8MhDfFuz2pBCN4m4De2MZAPLU7rJbQ7v7HffwAwz0FH6ww9V-N95egjMtMmd7qglWcClqoQl5LYvkOvFOmj-XT2T2d1m8YBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23049" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23048">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT7wmEM6szrPOtr-U-zQ6KrBqt9cEfo3eoA8hT5l6NSP6LtjVTWvI-A1ZMPDBvvCorO0sgvAov5UCavA--fkVdh6wRKP8Gfb7OYDj8LVwvUE_9kBqCcebB8gRj69FblmEsBbZlZbehnf26re4SQbtkb4C12kKGpOQJ6znB48h_o7WNwzB9GuuB6lCLmk5BGvj39pauOlYDKwm5dcKd7xrRcXHLs4b1M7P__PHeP6h_wVIg7ZoqUQzB9bnPDHZ4dz_aDJsIBLZO2xFNUeE8DBb2d_CeHIC0Hqt3BJ8VQtHWF56059pivj121jnB6Uw4YHOn0cjVLVGPFAF6Cz04Wezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/23048" target="_blank">📅 14:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2qe33IPj1kC7tjToouMyU-j_R7N0pq7ASENWGUfNcHrtpIbHaql1HPUdtBG8mcWlXTUZhC1t7GZaKeizMYvXSBAwJM4XaXRPBr89Vx8UMAPmzBT0RlIoJuPCaL6kSW5Hk9sJbizY1H3m_RwZrHviEzQ5YOdg52xs2LwDQzxf5QpKPOBYiP7iuAsUOvD2tLT6emHl3krhMEuyBZTuKd4fnhvgAqXKLQMuWr8Do2dLYiubRcQXv-sOayI7WiSLvekNyNV0mSddN5YSgjEYYqbAx-C8gFH_hyMT1hXsvzUEzgaRrMteZI22dpugQm-OCAa5ISnuWa77q9u2uXvwPvfJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
باشگاه استقلال مبلغ رضایت نامه عارف آقاسی مدافع 28 ساله‌خود را 80 میلیارد تومان اعلام کرده. گفتنیه باشگاه تراکتور به دنبال جذب این بازیکن هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23047" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMLc16rviNJ38l7Q40CCFvHXoVtGlwHt8iixuLDaUHv2ULvIFOAepM-jpZYRBDrno41t-bUYskQZf9e-V8t_A5cTl0f8uXSJmInT1eDG1yiLQpYWP3gZyEgIzNFFz4ZpiCMeGFKaZkMnCCfauvQEeodkqzusiJfJYI48JixwF4FrskME_oSl5APEu10fz5St2tY08_ps3uW3L1COXTF_2MTu50K97XD5PNAPwBPHB9t4oq9G_s7aW1TFDFET7gU9jc5digrLZOS-ftIXYaJWboU1zUnOgniHHo95usdaLwOBV3XxL42Dn-P0Zr5PMzM4L_4C4L9RZKiKSqbDtsFw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ‏گویا پیام‌رسان واتساپ در برخی نقاط کشور رفع فیلتر شد. از یوتیوب، توییتر یا تلگرام به عنوان هدف احتمالی بعدی نام برده می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23046" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=krlPoOcEYfklLDQ8a60NUu2DbF1fgL0a_h-FvqAJGI7LHemY8nGyB8x9Pj1Rp6xN8LaI8zyM9c5K99RMqcmT_jmcR9rxkXAIZzee6wzLv2ejiVJGxCCPsT5SQKr2Vxc7OrcSeA-sO3ngGPooZPP9RrYcP0AeZkVJZyPbQ6JHXXjcJC4wk7c5zlVpM0PzUMoJo06VTlaVSeV3O_gcC5ghNEm_LLFFywzATkXYPRwsAZSJY1D3pVy-Ugpip1oyEOL4XyCAu-zuueMzwkIYY3spdIaoqQ2i3aj5HkwEbGsLJZSTaePlMmoKgNGstCMH-l6ii-H6OEHRlQU1nr-BsKZKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=krlPoOcEYfklLDQ8a60NUu2DbF1fgL0a_h-FvqAJGI7LHemY8nGyB8x9Pj1Rp6xN8LaI8zyM9c5K99RMqcmT_jmcR9rxkXAIZzee6wzLv2ejiVJGxCCPsT5SQKr2Vxc7OrcSeA-sO3ngGPooZPP9RrYcP0AeZkVJZyPbQ6JHXXjcJC4wk7c5zlVpM0PzUMoJo06VTlaVSeV3O_gcC5ghNEm_LLFFywzATkXYPRwsAZSJY1D3pVy-Ugpip1oyEOL4XyCAu-zuueMzwkIYY3spdIaoqQ2i3aj5HkwEbGsLJZSTaePlMmoKgNGstCMH-l6ii-H6OEHRlQU1nr-BsKZKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
انتخاب آنتونیو رودیگر و لروی سانه بین کریس رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23045" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmbZLcXnc3z2dLT-Nj6eeDUZehMj7eOWysATl40qXTdtUMuEK6LldRKd68uyPC62jvU0gMx3dMhETN_D6HpWA4kImZZlfnhuV6KNLcSqckBH0AfNvgfcipwCeFom6AO2gkq4HZ9KhjTzQkwZmLmZHJhbZq45G3YCMQltClXRv52vrHd5yWbQPrGrl_XPc23p8GHX7UMhTSt2kEgZOrJsKpUb-V9W22ZKT0bb7njaaGFooNPuGJGkV5PfCx1Jsemy6BE96BU2G8cu88u9YOQZpfIILB0TJx4PXoyABBRnxp0gx-1IUdpwd8nnk4ye5ZEf_NqGSX1s6H-HoBNAs6lnnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: خوزه مورینیو از فلورنتینو پرز خواسته هرچه سریع تر از بین یوشکو گواردیول و ریکاردو کالافیوری یکی رو قطعی جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23044" target="_blank">📅 13:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAQ7DVWmQi-xpsbtMiqYZk7vvo06l3WF-hO2OxCSZUsoOAMXZES_B6esQWVo3rSB_c-C-5EqQia9s8RwZOFBSAJ9EJxGSbzJ54Zfb_Nqm3r9szzl51VoFu0CCPWfLNvpJXm4CrCBYV6fmiFEi0RVyRHeth1gy3YDV6-lNeyjekjjfS9XIuvrQXyNSUMqf7lKbKXSNqFy2qldWBsaZw0ksc-Bqf0u8Lgq5307wCUrpxhvXAbR4vVKMBZiTcjO7QekkFZ0uROCECJbhEtES3MmwZGLnlHzJNm3XvpiqqJvPgAjE_64Q_aaK6cOJxBf30TgLWp8ADRYoCTJx6OEvNK2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23043" target="_blank">📅 12:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LknVww9Df7rY128ET6TqIfQcmYZG8CeKReUxUjUjVHQwccTEgj3L94ETjWuHk2MvvQuTTrkMR9Sichg33SU5OzzxXJB--T1e7VH3qGK5UKkJlYEco5Aa2au7ahzOg3noMV0CRBHyg9ixn5XJ6UJBpLB6NHcUTuVa-u66WrQYDDnnXWyKSkUO-wFkoL44hIJCOjFfYuecHNd5_p7ZrOWg0jpx8jmWt9z-TgwkAkOKMsYHqSnmo5lYDwThrBbolRGxmHPMcHyOGVBY_xUYKMQLlliSGa-Keg_1E-KIIHVGjZiOE3UDGkQki9xHZ2bcGCUdhqVc86K4zKGfbfBFQnAT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23042" target="_blank">📅 12:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXWBv2UqgRD1JqoB54itNYpcBzCKDZD2JrGGPysBj3g6FTMCHFChL9N8LkLIIatpMDWAODsAcoSIplMhS6UCcr6QPnGqGxQ0lGk4zcom8UTzO4fsBpgowC_vh4fcpDhvp5MMETBuX4jd4E0LzRqEUT8UfOPMsjkShAnwlJsY3thvoAg6OjnpY5nKA3CRkFH1NHWsTLmU3K5yOxGODO_y3BmNjbOlDRrG-3wSUWKqtEYnY8sDTLFZSrb22eFxdadANeKBrenb971w13mQoA_zMZs6jnxMbGp9B1QpogVp8Rf_ASTfKCP3Smzd8t9UnhjRXphUWFQEfo8HY8jloUqPBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23041" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23040">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiWqMVfXBMKmOjRFgaJLfLdkqWw6Wm4RWeVZ_ALp-cEli-bSfSUVUshIv94mHqGimVJP8jKIwXleknD967Woe1hyKDZX7EnWdDz3tuYZ_BXiZYOGYtjmxzn-XiN0GYGBewRBB9-KtByaAkE6qB8dz3mXP_1b51QVlw9vHfqbFx8Ucb8h2qwa51uGqviVydxsSguzJU-PyODWVkucq-XEYyUR-RAOs6lWKAKc6HINLtSZyWTODgkarbQBS02oPYVZC2n78L3dXlIUY2yXGbt3BJhLfxyYeBTWqvVuF0q6MOII95R80Mk9OJEwL9KtRLpLlLS0HtIv23Bl8DE7N4Ti3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ ایجنت کسری طاهری به مدیران باشگاه روبین‌کازان‌اعلام‌کرده که این بازیکن برنامه‌ای برای بازگشت به لیگ روسیه نداره و قصد داره ادامه فوتبالش رو در لیگ برتر بگذرونه. باشگاه روسی‌ هم اعلام کرده هرباشگاهی یک‌میلیون دلار پرداخت کنه رضایت نامه طاهری رو…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23040" target="_blank">📅 12:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4860b42130.mp4?token=XKxvPm6p276SByxbf7prwu0_0Pxhdak5faqr-UQY2tSwIdBXI22xgwHzJYpVIjzqJkcZd6JqP53ctPar-w5Q7RQDh5BDsMnYuJa2jVVrX0xlYE2mCioGSO7ZFioFPsUCqPnQFvFx9VKQ6z9fgZLTht59PP8GsSc58hxTpQonQTZJ8ALs8T_pWTadyBxQWpRdILl84JEcGYNd1IwILWfq8qB1CFOAJTtDfNziaF9JZJv4g-HC4BjdMmxqy6S19-5WfvFb3GHt5ttQRtrFkUCODg337FCXb0XOS9hcn55FC1ayc0ukwn6ZKZwbF5oGg5bNjBUq4YTkoTlb69Qyzr5KNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4860b42130.mp4?token=XKxvPm6p276SByxbf7prwu0_0Pxhdak5faqr-UQY2tSwIdBXI22xgwHzJYpVIjzqJkcZd6JqP53ctPar-w5Q7RQDh5BDsMnYuJa2jVVrX0xlYE2mCioGSO7ZFioFPsUCqPnQFvFx9VKQ6z9fgZLTht59PP8GsSc58hxTpQonQTZJ8ALs8T_pWTadyBxQWpRdILl84JEcGYNd1IwILWfq8qB1CFOAJTtDfNziaF9JZJv4g-HC4BjdMmxqy6S19-5WfvFb3GHt5ttQRtrFkUCODg337FCXb0XOS9hcn55FC1ayc0ukwn6ZKZwbF5oGg5bNjBUq4YTkoTlb69Qyzr5KNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویژه برنامه جام جهانی با گذر زمان؛
از عادل به یک مجری وسطی بازی بدرد نخور رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23039" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmfoiyLAHzGcaOa8SkgH1-9JQxFmPIRo_2cWThvCRKHPxAyhFDpOCKKx1ySgZuOsXmNWI2XDLJRLTqTMwRU95RfDbSXXhBIWDXruNEDSUyZoov3i2QSyYq074s1n_4o_rgduoRim7GVHHNyiw3VioJEpNkOQjsZo91U_d5S0lIx_n6cE5dG1-Dn1Myish3AT9WE5-5LXm7363OpVMfaZsxnTFbdNA1GJhXeVQmTTuJ92iMSkqRyFfr-2qFKS7xJCjfo_ZrkQgNzQ10QGBmS6NLfp65oSf8Lk9fsbn6rPDG1keBZaIaYNCqAmN8Wtgy0hqvIdvOjvC5T6t4VILK4-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تیم‌های ملی رکوردار بیشترین تعداد پیروزی در تاریخ رقابت های جام جهانی؛ برزیل در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23038" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23037">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWijbUPh0K-U1W2b5o7u3FDjYm1SZhbDJe9uGyyKAkaUcENnNKxAAR5E8ruQZkkxVuI-2K4nLBwvKDMe-V9FdiTuKwTgIKXknmpSSzKcZ3kBxstmO3MoDGqMRwTyQ_8fMpafr8nSYRq-FZwK-0QPGZhWpwGlJiSDk86_xoPYHxWl1PciLcHx9603W6cZN80e6LursdMzdtC0ztNLXo45oUw_0KVXrZEqeUErQCiF6YNMvHu3MeVbEiORj4Rmk10liClIiqnsbNe_Y7AxCNYcvo7e7TMRKnCGewTA5H9q55MO4qt3NQL_4EfEMzg2oBd83Q1xb0CaNMUPJTRNbrjbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد.
معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس‌اضافه‌به‌ازای اولین واریز
💰
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا er19
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23037" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYRtMpGi7Mty7ObaJjk9FEmLAzAnvazpY0XjFlWliH9q8VoNJmx1LR1v9XLPt_XsyFEGE8y-O_9bh1DxTZQMNS5KNljdw5ZIFXs76x3GPgbQxvNXhaUMt-5nGw_OZXYjZVXgdKc0BM9j5WnBUF-CKPQ1ev8xTTa84kZ1uF-Zjf4bN7hkQQXBsVPVMi49iPuhPFHczn-ww4eDKFdJoMI5z_lsAMN6Fp5IjGQsvNII2Efxdwo2XM626PM-wk-AG-XBsKsHDE_RDCbhmKbRQodLltd02faz3rHX6GQAbYhp48jbvLch7VPEEynQVmgQtsHZy-4WSJrSphBx5XO8DnmePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23036" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0YVhUJXTU10uwXiky_KY0URhm5tDhRUvJYa7xvhdHPUD1Gw2h-9XkmerMmcnDci6JNpag7kqG4KNemJ1ty6Q5JjkzGmaRkT06116ZnaSLOzR7xAdUz7o2ZH2zIX7dV_Ttz_F-i6pcUNjMDJuSsiPzNtMQHcaJFQTaEcY7lDW9aqi0BGD6GdCTZcR9w-YIA4jIt-d5Am1GyPMYlkWu4fGFIbJ_lVGX-rXxGYcphgectLf6ieNy9j7ZHFhDkN6Bl8Ws6ryTxksolj2xF9cJma5WXERXlzgv_1giPhvWLuUsyQCjRlmETxEhvB_CxSa3H3y4m5anKSJx9me9OZBs8ufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23035" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fkg9zYenmye9UK2ZewhhA8J3Lf4cCllohQoqRj-8ukokFh5x8Uc6swzYFPHAjIzhBKqEblkKQ30RpHzKzGx9ASXyKDd--Q8AePQVoO3riC-ZEtRXIsSkVjPLCqXeG2wNEYm4oFo4C70rTjE8dzWeczIy4YvESPIaEZW674Bqb8NVue4ogizTYeQwV738dsCAVJd92VFVqCP5o8DPa1lZHUMXvuzlbDOqwVAqPBvBG5GmAmPx1D_bblIVjf1afjIfDTsCdyuRyuqIVx9nQYUSmCM92mRTZVSSVvYGcpC5v1VjP3LA6FYvwmxaoGHsE0xh_XXD6iVhOMOKAA4_Jc_xiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|دیمارتزیو:
فرانک کسیه پیشنهاد تمدید قرارداد 12 میلیون‌ یورویی الاهلی رو رد کرده و میخوادبه‌رقابت‌های‌سری‌آ ایتالیا برگرده‌. یوونتوس علاقمند به عقد قراردادی سه ساله با این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23034" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwMR3l4IW5sWy2RMEcSsryLXqh3wYpguqiZ3hejwZyaN6Ld-t_S2XZMCeRjDXHVabRbB9bzU7OQVf6Hv2zokP9W_Fg70emkkJp9I329zqtVt8LdS09CxFEGFrFY0wwA-hrcXe2-GW3YGVP14B9jySOtDXlZrjk4UvLIkuf85s8YFjMxJqt4BNQHtCkayi0G7xzGOi6tUwN0EjPHid7dg8e-AOEa5kJ8CdtF4N4_HklpYLrv-qbSIdRguLPvuAhTUshQ21QHFynIk19Y3yYalpBB5cLX0aaTDucx6yI03ZibNzNL5u6OZELB2WjhoklR3C5OC7bsdMeZUcSzq-MqRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23033" target="_blank">📅 09:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvW4IIxuUozh8nRLHPHUC895F-5jH7M1Sj4m09w1uCLnvXGjk92TMZfM-FhcYS-nQDx6qoyAeNZLCMRkYR2tovGqmOZPacPuxiWzNQ2gaA74pMKzqWrYtW9eaNhcCgo_s9o5_I8-jxMLz7J9cK7eFUZC7edFTwKcl1cHKp4OVG7i_G3gSD6iaix5HVU165UejnGZqkkoo10KmTFPuat48m7VRqe7J74dxhMm7Nl6q54gXRHQIpGtOz6PLpcGuwi3q__wUVPKgP479gb5MLbP2Xl34KtnVe46d2rHywjcqNk9_Hq1ANaxU-7ls6thu_y55dDU7yIj8blJK5yXD05wiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4rgduGVaTCA3AP1RhEsCRtFK67yOXh2C3bhnWRw65ecRbIV5GjBcPSU8JNfawjrBGF1dIjZKZk61PWrI9cePy6UapTRO-9Hlpdc3iH0tg-fz9p0ZAd3oXmQudpSvDROa1M8emXomeBBg4u82AUmzX6f7KRvUoqr4GHLGmPay9qnNcaOVGsSBpFJBiZUzyFScPgzi4x7mlkf1bnKuh1JnmhO4zIWzi2zVHKwbHKf50Zv12d9s4ZptqpJoc6VUUNbER81ujAIkcfBd3ox4YTASWEyzvU1bvTTRhMhZhx9OW1xiXyO7gZRKLhQb057P_wtSNEvepkE7M8r3B3aDWVDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNckUNxnBKykaaVRpH4MXv0fBqGWdekYyb9uXvN4QLH2pNf4ml2G1eCsmxlVwakXVDq48EMcro7rcOwuxjxV6GdZwHwnhmArOJ3E0hgr8uuYl6gifLB3XMdhrm49T_qt1-FmSN-UlFNO5nwWG91JEBT2ocDuY61FI47Va4fmmOQ6mgtm4voNNqJWKJBi7wWVCV82zNCPUuO8VfUZSPFspij6AYLeoqJG62IoMlpXubFjbXnmeoTA1pCF6oPOnU1UvaMfQeTJb_mVWuRa0E1M_CTzzvZDFKjvLOkqiRHTk7BcXRcuvXdkLyWp4Qoo4JyIWPIHPeSvUivP9F79pciIRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=hYwKf8tHsOb9gVYS0K7gv0VrJbnZeZh_EqfDBXA74tL-BBKnKxFJ4YDScS8Fpcu9GAjhQ6Cd6TX_K9Cdb-EUL4rbWox5Yq0aCsKzF4pTKH7SR3F8rzjio-lZwFxz_1pbWAVMU3u4YJYx5YIjIeCQJLJVONUQ7Gny_6N17mKWr7puIe9oyczCHPQrcRb_phqz7WrWZZ-qIVyFLxlC-cezVcIy4lQ3gAmVkqToYVN8bKk7R0aJ_lHr_f-wVx_F7QR-tjfXqW8C9q3e_jWQtEtfahpp37FQQ1iHTuFuWnzczTa6aFNtN4Z6oT8IlYS1tzCdntwsOZbmrbhgmvARZsnkkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=hYwKf8tHsOb9gVYS0K7gv0VrJbnZeZh_EqfDBXA74tL-BBKnKxFJ4YDScS8Fpcu9GAjhQ6Cd6TX_K9Cdb-EUL4rbWox5Yq0aCsKzF4pTKH7SR3F8rzjio-lZwFxz_1pbWAVMU3u4YJYx5YIjIeCQJLJVONUQ7Gny_6N17mKWr7puIe9oyczCHPQrcRb_phqz7WrWZZ-qIVyFLxlC-cezVcIy4lQ3gAmVkqToYVN8bKk7R0aJ_lHr_f-wVx_F7QR-tjfXqW8C9q3e_jWQtEtfahpp37FQQ1iHTuFuWnzczTa6aFNtN4Z6oT8IlYS1tzCdntwsOZbmrbhgmvARZsnkkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23029" target="_blank">📅 00:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23028">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQyxDiRAYWWpYPDb7K7csaA2bMTBcIfWfaMX6A-yswHgFlJJIlBPlaDEJeaPi6fhCSsHEYfGqyuIYTMHpvfpHQsKe79AfsXnQAgBG6dyKYSqQa_8jJb9RL-qSdWGXv1Knxdyem87Xkn0_AHSib7y031egL50ht5NhWwVSZCScb0CIswcdHue3cKd9CDnWggVSCo5R_GZYf4kQlkJKPx1tNyCYGmWIdxY6bYQtB4A0qP8AjBIeCYyt3j_HPshQSXz_oeYrlBxt4UbctvVnsTQ65xGnAnt8gTNAHnZV_joRLugqdz0HZyfpwztZBxd7ldsjhO19Qy0YJf8GYMqPpbwIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا:
فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23028" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=YYsFeJe6pxXJuAKv_HZ3ON1feKz51eoDrL5giFsCnYlPdD7SbjkBkxSl6vKzwcGtdnGcBITs-iooJ-5rdaLx4-bGJuOAea8W-gbF3_hDfulIyCSENvO8Yu7-ljSQqHMy9q2w7wvqKpNhlcyyS-9EKNzJ_M7YIhoQEwZFryHCFOtc9Ot-rrE2LoTiH3cBg2WN78qk5o3jKvI7ISmixhGVRdjXsWrtIi03RACd7jyvI9xYxhPc8RKCnHx2FEOLydnzKbLtkcS5WmBqNN_bLiIGZWBaSheIq7c_C6tbhrpFwCYOx_lMHqJhst8GBhxFbvIK1cNhisNGCyypSIx_b7XINQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=YYsFeJe6pxXJuAKv_HZ3ON1feKz51eoDrL5giFsCnYlPdD7SbjkBkxSl6vKzwcGtdnGcBITs-iooJ-5rdaLx4-bGJuOAea8W-gbF3_hDfulIyCSENvO8Yu7-ljSQqHMy9q2w7wvqKpNhlcyyS-9EKNzJ_M7YIhoQEwZFryHCFOtc9Ot-rrE2LoTiH3cBg2WN78qk5o3jKvI7ISmixhGVRdjXsWrtIi03RACd7jyvI9xYxhPc8RKCnHx2FEOLydnzKbLtkcS5WmBqNN_bLiIGZWBaSheIq7c_C6tbhrpFwCYOx_lMHqJhst8GBhxFbvIK1cNhisNGCyypSIx_b7XINQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
باتاییدرامون‌آلوارز؛
مورینیو سرمربی فصل جدید رئال‌ مادرید برای کنترل‌کامل رختکن تیم رئال، پپه رو بعنوان دستیار خودش انتخاب کرده تا بتونه حواشی بازیکن های داخل رختکن رو کنترل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23027" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=RmSC7yUJ_iE4P7Dc7upoOROJu4jqp6KECt18gEK_IYh_5BB6wMQazztH2755YYTCcInPXlmLKntaxUiA5pKwCk_rpisQxwDbp5n92Pxm3LnxW-4kahWPO1kiBiEkeuk1QytASFLG6A0PdREKCjQ4V7GWL8YGX3ikvvf4jO6Pnhc0aPP6RpoYnL3Mhqr5MZGEQkKDMWBgi-_VR6b5wZu2MG-Jq5NgBjN9FjLECMAZbRbd_rNnMamo-foY81AjkA0wxD8OZHfF3OoCh3SkBEGZb162x0PbaIZRvXJ5BT5Mz7Ybsv90w90dYIcAj6A_AKO8OYHQ8njIiuo2lVtSqzRvsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=RmSC7yUJ_iE4P7Dc7upoOROJu4jqp6KECt18gEK_IYh_5BB6wMQazztH2755YYTCcInPXlmLKntaxUiA5pKwCk_rpisQxwDbp5n92Pxm3LnxW-4kahWPO1kiBiEkeuk1QytASFLG6A0PdREKCjQ4V7GWL8YGX3ikvvf4jO6Pnhc0aPP6RpoYnL3Mhqr5MZGEQkKDMWBgi-_VR6b5wZu2MG-Jq5NgBjN9FjLECMAZbRbd_rNnMamo-foY81AjkA0wxD8OZHfF3OoCh3SkBEGZb162x0PbaIZRvXJ5BT5Mz7Ybsv90w90dYIcAj6A_AKO8OYHQ8njIiuo2lVtSqzRvsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
خوزه فلیکس: فلورنتینو پرز در کنار اینکه 150 میلیون یورو برای جذب مایکل اولیسه کنار گداشته؛ 150 میلیون یورو برای جذب یک فوق ستاره دیگهه کنار گذاشته. پرز میخواد این پنجره دو فوق ستاره به‌ارزش 300 میلیون یورو برای مورینیو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23025" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FkLn0NIDgC9Rm6Vyj4zQsElhpeNmHORgpkRj_TtE-CW1neayJP9O10-47qOEJcetYuKLUj2tlvBli4xWyCdi7adTnf4stClA4irXuhQtHfem2vYImmy-l2_-HXZXDMS6JS4K6fPOtaFewKo3QwteBLruSsBptgyrNQq-gdjk3KEV1MMCUDCXro2ru_QdPT-ni7DXl_xXY3GVTC8Gb_ErPnoFgkqrdKVnSkddI45kr18Hh94gr-6XZ7sYzHvkZWBygZqUIqjwuNqAPWjjSIaQIZTjyJmOpSJxL50SecRtn_50IZHxMyaJpirCq4MXrUQJil4HDmfvmaPL8KDNn5g3Eck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=Ha-ANJEzsPqUnyH8xRDjXq41zqJxGxt6zQYh8dFLtKmcmJXcxJnEcrXu5JVlVpi6nz2Y_dx5cxNIG4yk2cCrisyWZ4JkhIYfa_duePkp10hI_yN0BT2k8uT49_j0ANtXoT6aJZZLutyvMGe0ehSBSflDa3RFi6_00eFMjMYHcgw6ATf_ugGok3B2vcJuGzZFg1DhIcJKyN8Ut_kHM_y8-B5bMpyL2zHkEOSG7ljfFkyfeM0ocd9jolUs8DmT6WN-gp_1X5NLRa5Ep-HRXdD4k7W8v1RgKSQarGmUyuEG6XNjatNu9B0R5W0dt5qD3mO69F_iqUUShQKSgq-YBE59FkLn0NIDgC9Rm6Vyj4zQsElhpeNmHORgpkRj_TtE-CW1neayJP9O10-47qOEJcetYuKLUj2tlvBli4xWyCdi7adTnf4stClA4irXuhQtHfem2vYImmy-l2_-HXZXDMS6JS4K6fPOtaFewKo3QwteBLruSsBptgyrNQq-gdjk3KEV1MMCUDCXro2ru_QdPT-ni7DXl_xXY3GVTC8Gb_ErPnoFgkqrdKVnSkddI45kr18Hh94gr-6XZ7sYzHvkZWBygZqUIqjwuNqAPWjjSIaQIZTjyJmOpSJxL50SecRtn_50IZHxMyaJpirCq4MXrUQJil4HDmfvmaPL8KDNn5g3Eck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوخفن‌ببینید اززوج‌های‌مخوف‌حاضر در جام جهانی؛ مراحل‌حذفی‌قراره‌بازی‌های‌جذابی رو ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23024" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWMT36Q8WqBLSQKA-Fnxd8N_YDHVwArgsubjBY8sT2ZF_rUh9xnFHrd_SgqNrXnhmXOOftFrs8R5KPbBwBlOgJqyRJyGYMk8a0cKqQ8dtGGQ2Dq8oUVfnBkEocILpjkWo1YkrZbf6Pe4RISVRNDYqlsZDzHFE3e0aN7tFpZfGPNHIliFAJ70j-EFnxGmkyu38Zn-sWgtQzztoXYoEgFkIoHvBxSO65Sp3VMSKy_Bf-dLFkx7LFMNM0mbjWWnNBMJzB2ifZciA_8LPd6Mm6fRthr-8QQMqUos_g3tFUexg3RmWekw9YJ7QYgW2HbWG-HCtddYA4dSzqlMIUAno64-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqDuLfFSPZKFMGiFfIcW7yJ7q0DQ7X19Mt0nhZO9XYwZk-rIwaYt6lrLdv3HG6zy8LCOK9IzHJZ_3DB0F9gGqezjNFUnBQETsdsiycyZAu4tamAPsEUercOth1VNj0psxh8qoJotHqQCagdTsJfpYtrj14rYUioXrNDyn_mXqVSASTKGlmOrzMzwegpD1BJ6_qajaujKeJdJglpt2Ek9L7FXeWCRVeV6hFHkv9fCSx-6RUx3pmiSIyJt_gMXoxikKqY8E3rhlBypcKb7rNFoBl5YyimavqZjXJSL9mq2VRuaRgx8snDt528ZdQkNakXi32hNYrOsZOFrVpG34gz_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPPjfUVDhRxDJoa1nt8HE-x2TzpDV1cLLQ2L_6HoMZ8B029l2zgOqpUJ9DcXmLgz1yXfZWuNpUGGorKaADjhJoH3xJDiBqeCAXGj3EnKdDAhNIraOzzcZ--oCWTiDn6hpgztCnNDFJ9v7dP17wEvNWm5C7EijB_GTyxNJMtXBSaPL3GYPharoYVKRwwZJdhLFObI6CisC_SH3N393iZ6tIAX4quizi-MOHehHqrRX-JLy7MAKgJzpDmIsdF7kNhCJbK7qieBwmNMhfSqML7Ok-lU0YbSLUZ62npVwJxzFwYrjbInKYUNQXUjqaChWwj4LtRd3XjA2VzqVatSXfjylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=jBkfZY5yb_O4truTNMAe9FNwfoF4oUeLMemDIF_ffzd8aVTpzzv2Fr5Z9VQ3vHmBme2B7vhSRkz8buiG_vXlPZTRm1FMJW-ihIbWYgXcpEfofddxB8GqAbPAyWHqzLf-Tt5O0_jIYvodbMfgE3OB89-dF_PDYLcXv83QHrx9ey_vIP1F0_r8gaTk_VwPi96tMEBjneHdInpbwUT9avQTbT5DfaQO-9wl_oKTdJdwj5tOtO0W9IPgneHBW7n7P46q2Tsdn2sXKTdFrAEj1zdXU6_KcfCEA5SeR9eUVaK9v9PYtKJFLYH1A3WT3P8WHPEYy91KdiH8sOjjeIg5gyCpuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=jBkfZY5yb_O4truTNMAe9FNwfoF4oUeLMemDIF_ffzd8aVTpzzv2Fr5Z9VQ3vHmBme2B7vhSRkz8buiG_vXlPZTRm1FMJW-ihIbWYgXcpEfofddxB8GqAbPAyWHqzLf-Tt5O0_jIYvodbMfgE3OB89-dF_PDYLcXv83QHrx9ey_vIP1F0_r8gaTk_VwPi96tMEBjneHdInpbwUT9avQTbT5DfaQO-9wl_oKTdJdwj5tOtO0W9IPgneHBW7n7P46q2Tsdn2sXKTdFrAEj1zdXU6_KcfCEA5SeR9eUVaK9v9PYtKJFLYH1A3WT3P8WHPEYy91KdiH8sOjjeIg5gyCpuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی‌پرشیانا توسط علی تاجرنیا رئیس هیات مدیره استقلال: وکلای ما خبرهای بسیار خوبی درخصوص‌پنجره‌باشگاه به ما دادند و تا هفته آینده پنجره نقل و انتقالاتی باشگاه باز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23020" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC0EOqV5U7Qngkp3MgPgiJLPDynhSRWxAkmO2GEzJZRHA1GIHrd7BYObP0y4xGumjgJWPT7nxedN7Z7vydhodmeTGyqTHV85xLL0JL_T_lwvjqx6IcO4rKMEVYIchvEjRh6zq8DMNypzJOYyo5PURZv0cy8cKhfxRUhayoQuTvvl_9y_ZsItCawXWeu7CnV0jIBCjvVIoeDG_6hLLM9DnKMCmZxpsnsoLBejwagA9JIyoYkT0M9x7_ASoPzYm5i3fItNVjkWSiPM2Qdk14ek7s0fYW3R1r6deefMdUiHDCAP3vUiLHGdVSb80h1dQrkfc8IwPuz52rnk1XSWXMok3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛نشریه‌مارکا: فلورنتینو پرز عزمش رو برای جذب خولیان آلوارز در همین تابستون جزم کرده و میخواد بزودی 150 میلیون یورو به حساب باشگاه‌اتلتیکومادرید پرداخت کنه و این فوق ستاره آرژانتینی رو از چنگ فلیک و آبی اناری‌ها در بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23019" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5cOw2Zh3coO7fBVu76MwrZgU7QjiV81EuBbFTOThTyWac4dURXw8VPk32vgi7ev-VRgoTuD0E8v9ehDoW281_EhI4KC2wPaGmegHakiwDi2VYslhF5ThpRfI6TF5-TtHz2pt-jjGdSaSmrwJrnn9kIcnB1ViOCUdzZ2hjb7plWdPP3PanEyDuHlYde8MFZ-GonaZQHV60k8J_Z0Xh7_1CZG4Rxq5fYuzFy-LEjddGaP90YnWNLDACZW4tAp2u96zB64lBZ1DR3T8ydDFgLiCwDsJRtniN3YAEYiOn4I92l6OKjZZaKuUzzPEapk2qH_rvYg3SC4N0_-lvMvi9ZYIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23018" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XICG5sQCb3WdyMZqtgg6JOmkWydYcckqDuAsZsI4HE4lJ7IL2GScARfeQiuHrvGEiVFoLbjOAQyOHV839-9UdUJKxIcSWkatAjhV0Psl_GV-yZeyu6knePCjBHUdAaGLFF8YTuE1lPX9Gn37TdKzdbHakGO2VpgfRWs8ZjXYyWmgfEZq8b9uQeFaTZCqRI99NwLCvAqgbzFaQ8H91EvkoMXlcjiWi58AAQjwrreg3POTNK8P8GR9uyJkGsDgjIR2hDD7uvxJchakeMksNAquh-UXVk9f4XS0yl46jUEaLJ1OXWt2tKgAvxy9uNEwtNtNVrwKUcqKoop1vij51dFH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇷
جدول رکورداران کسب بیشترین تعداد جام دربین‌بازیکنان؛ لیونل‌مسی بااختلاف درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23017" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qv5RBiqvJ-ZHwj73nG7rPlrqFGVODoNnJ_e-uCmAQYILdYEeybMgelW-MY68KhwXD5RTfCWuaDliAUiA1cVLTmrNV9FNSTTvKnaM-S0JLur4h8oRqbftYFnOU4-AD4zHm2LBSDk7CwVLiFCoMCxHwWJ1vUM3FEFcvCKEZo0Dcei-o0tb7bSQHSN2wlSuMHBtZ92QlDlYLhe4EeH9q2TUDlcl0ND-i5_OH5fUluj5SKA9ej0DgND8fvrsi8cMzEbEbUuEJoB61VfZJfWXajwkOotdCl5wq0EEemaplbpGjYtme5gq-n61x27UKRd0MdaFjDtrFDKQo0GvvlnbrJwpIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNQwtD3DzgjAK02BVtkJy0tNSGXK-rvhNy9pEw1uhHNuJ9b9ZbSzQI5iY4Qa1dBjf1tUqrHrd20HZC3FVpbabVSSJDBJHlBSVYHNqHwEIWWv-lmNtF_o_wwnZxTISD_TR0I4pDLe_kgVm7pz7_-_f72SkDYEcflgNRBr04nwn34jLuofZnC65kc_VElEKWm_iUde-8A7Y-D_yVfERdV_yrC72zHlQqV3-T_2Zb-i2b9X_jnZ7TME59CjDZS_jIvgMCBzaa-p1OP6kmhUItxgVIvHmD_ba_8l8V4Ao9L6larWgJlfQM7SoXChXrSo4NC24guXXo4IZKAUAxnxbuatTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=IPi2d54kwOsaGvtkkulE3afaJBOseN4iIGp2KOakWc02e6eDSta2rZ0zwQSWMSP9PHlLTGyAMAN1fHFlztH4P2uh5bDW18IydkOYUg3r5idKN1e2iYndi2Du8pcdBwlC7kAMoGk9yX_1vQnS0BSlt0aX8NnH3rTUhDOPYCfSC1TIiLseRukCu_DbF2_PPQSA7VReAszFjSL5VaSqJb2kISCDUli6_jzsOR6UCA07qdQvNTqL9YR0ZndjL-_O88KVtbR_mSD81-grv3_uM1EBTD-Or73W3KSWP5dmlg1A0QyYRylVYn4cfnS8-FsPJf75v1Jb-kdUjtDILUz9oQhIPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=IPi2d54kwOsaGvtkkulE3afaJBOseN4iIGp2KOakWc02e6eDSta2rZ0zwQSWMSP9PHlLTGyAMAN1fHFlztH4P2uh5bDW18IydkOYUg3r5idKN1e2iYndi2Du8pcdBwlC7kAMoGk9yX_1vQnS0BSlt0aX8NnH3rTUhDOPYCfSC1TIiLseRukCu_DbF2_PPQSA7VReAszFjSL5VaSqJb2kISCDUli6_jzsOR6UCA07qdQvNTqL9YR0ZndjL-_O88KVtbR_mSD81-grv3_uM1EBTD-Or73W3KSWP5dmlg1A0QyYRylVYn4cfnS8-FsPJf75v1Jb-kdUjtDILUz9oQhIPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/El7bbU33GDjRWo0HJtBjCHpaeZX6rtTanYtQUvsgVowXJAnuhnkJf8qXB0G5t0zNoEG2wNLrdcHV-p0Q5UYoK-KktRj0Q_v1LMpu7vahRB-Loa25h0LKfF1Is1Wzi3Kqrgn-0nLRH5GAC7ArOoJSeum2bBquTftSOlibzDoLtQw4mvcQTjh2IeBO-R6qisPyVir7FFbF3VqsJR2K70ML4PIFLFan08C8ubLS0yZ7CBwKgeEZuekfVNBE3UFIUzo6neIB1xjmolPzivfynXIHJYwAi6XxnlMnwfw0SEW7QUsbmyAasnmS66Wv-fs58hr7YSccizRJkPaH1CKDWWlhSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eppTS0ADJFzFgZ0WmdM_8xt3flh2GMOMDBFPgLKFLzJ-_1d2noZ37KEWvPFnLC-x-eGmVSB97LpH9odEWkhIoIKI_OwPROfYdmuCxa-JfkvAJv4lrw8IynQmLdRLWv2Xz2nur0sJZqUaZ5WNkgZz639M_1wqMgKoIPYUcuvJwZCPXQk6g3IXWmnBpN57toQAh_mu3ofeZL46QzoVKKm8sMRlLepj4a6R9gXMuyZa0U2-oWPnpyGEEUet4BTUZd-ras0zs23I-eBQyTbjTD3GAsiglR4Kt2goqg8RmBr8fC0gnmyTKcY-uFjtGje5p9B8J0MPb4wxXfCv5qTmEl0Jyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29259cd165.mp4?token=h0Y0__d9Qx423i48PSrML495qNndoG_fcXZInJTSR9mN487j5mw2gieteXqVlHo3wJ9Wj6cXLMxLSSJ8mWKMHSxQ8uA-LotgcWZPe21YrTFljUGSgjk9DvJ7ZxTa_Zfsl6Zwm107-Jtq7EgH504pEBYOf_fc0iTsQhjBp6N3eHPZJZEpTYx6KtZgR0foWkFgwww7IFV55P4Ok0-ten2-mZRVgj9G5pmDyagQLd8vKBRHzqWaQKZV3b14IQHAN3iCUazMx0JONhADrfYWHwr6lhvORnpMGgCxY7S65gxaJZ8_px6jsO9Mv02smUwFHLwIIDYenXp4ngjzuQ4J-vBF-0-WCWaKs1coZZQ5x5_pe4DoR0FCGjdSxQc2I4XrFOQD-mCVR2L3vX9cYh32i6m8BLwGKB6bOnZNEyY1UhCPEF4TEdv2kcRRVDoctVLN7bY1Rmf6uI3QFHxgP6vDjr_yDe34m6OqQHjLI88NjzEeEUIPQw26JT1VcgK9Rjsoc31MFh2UX3hfD-PzxVo_5tm7nO3Y-dpg4V9eZYRFk3uYuWwPJ5jINrPbsl9d5HlpbQQ8EuhqmRb5rRMghD1ecidjTLaS0DaQbaCBTaEFcbAW_aklNiAOPiq68JPNDjLRgeaBZ7Y9Lh-R1ajpSK8SCE6_uDQIUXAEkrjR7TXCO8U_0Sc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29259cd165.mp4?token=h0Y0__d9Qx423i48PSrML495qNndoG_fcXZInJTSR9mN487j5mw2gieteXqVlHo3wJ9Wj6cXLMxLSSJ8mWKMHSxQ8uA-LotgcWZPe21YrTFljUGSgjk9DvJ7ZxTa_Zfsl6Zwm107-Jtq7EgH504pEBYOf_fc0iTsQhjBp6N3eHPZJZEpTYx6KtZgR0foWkFgwww7IFV55P4Ok0-ten2-mZRVgj9G5pmDyagQLd8vKBRHzqWaQKZV3b14IQHAN3iCUazMx0JONhADrfYWHwr6lhvORnpMGgCxY7S65gxaJZ8_px6jsO9Mv02smUwFHLwIIDYenXp4ngjzuQ4J-vBF-0-WCWaKs1coZZQ5x5_pe4DoR0FCGjdSxQc2I4XrFOQD-mCVR2L3vX9cYh32i6m8BLwGKB6bOnZNEyY1UhCPEF4TEdv2kcRRVDoctVLN7bY1Rmf6uI3QFHxgP6vDjr_yDe34m6OqQHjLI88NjzEeEUIPQw26JT1VcgK9Rjsoc31MFh2UX3hfD-PzxVo_5tm7nO3Y-dpg4V9eZYRFk3uYuWwPJ5jINrPbsl9d5HlpbQQ8EuhqmRb5rRMghD1ecidjTLaS0DaQbaCBTaEFcbAW_aklNiAOPiq68JPNDjLRgeaBZ7Y9Lh-R1ajpSK8SCE6_uDQIUXAEkrjR7TXCO8U_0Sc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23011" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WY1vWz-Qkv6KSdTbtkVUaU2SH7K9pNbetvr2AB2U4PjwKbj_fDukFpvvT4Ma_hR_I9Fnhc3t0Ww9LSpO-kL4r3E7duiYZuGPuHLBMeSILteHw_Q-3gE8cQFjwHWFVkxkOVdpN0TOC9XCrD7kt_RKWcq277UZ06Nn2qEvWdqD9PI-N6Xh9rBAKP-HrrOm_V3jUpJwJ8BGPNLNn5f7dG30ywk7GpRQgVD7tSCizQQt7WG_qYUm3rVDBw1pgliboUZjcRSmNrEofD_Jx2IBSXV8DRRGAsnKu-v6P0MmgtlRDiThq52FbDKaErrJXeakcrwW68nNzzpfxIQdrMQoldVpWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23010" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-6gYiQj7O9iucryc5gc-iN1Uxa9Av8dzbsbymknVxmKXLycn7FF-iiISBthBdlzi469qHJoaE65BOlMN1_X0zgd4Jbvaol-GL9oStmvAyihVkZpvO1SN5UWuvJv0IELGsk318CxmG_rPxrsPJgkK-2VJ9mbQ7rPiuKjWbTUjzrtlM3SJlqWmfYSmI5BOcgen3YxHBC7WWBo4u36SyqpsoWvCMh9tAgNyzcFTwz_CZo5ECitlH6QKx7DIm6fBdiDND7yPw-tOwG1eemqZdKPxcJFqlHu-2cXNEXA2GJ2RWqKLM5GbU1QBDCKcs7ccY9tj4hXX73ZXr3_-mg5A3U6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیست ورودی و خروجی مدنظر اوسمار ویرا برای فصل اینده رقابت‌ها به دستمون رسیده و بزودی کامل پوشش‌خواهیم‌داد. علت اینکه یه چند روز صبر کردیم این بود که همه دوستان عزیز کانال به اینترنت دسترسی پیداکنند. ویو کانال قبل‌جنگ 65 70 کا بود الان با وجود اینکه نت وصله…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23009" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=Aa6y7wioP1l8I0NtmfZUmlkJ7XaladkJ_4tbUBBMYFwETR-QchuBsLVPafxqaHTOMTDFff4fF7ahKjfVAbahPmNm0tVtgPm9qxyIDD1j04hd4CN2cMrER7M8Usf3bz_BeJeCbspyDDM-M5RFQHpLBD7os9KV290uISFMmkx9xei9vCgq3bXAPRKqN8180l82BRN9BA2SQadjpYIdOUaJg8UjDwjQHMS62YkWYQJkXERGASwthwrx6FXeNZE3w0hWVF17hAKBeX774BhluG-vOwvMQfZqupdO_fgr8M-lVpD0g_YTYmDyb1a2bI7FrsR20Jh0jY33yRhpcki6Qp-ZYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=Aa6y7wioP1l8I0NtmfZUmlkJ7XaladkJ_4tbUBBMYFwETR-QchuBsLVPafxqaHTOMTDFff4fF7ahKjfVAbahPmNm0tVtgPm9qxyIDD1j04hd4CN2cMrER7M8Usf3bz_BeJeCbspyDDM-M5RFQHpLBD7os9KV290uISFMmkx9xei9vCgq3bXAPRKqN8180l82BRN9BA2SQadjpYIdOUaJg8UjDwjQHMS62YkWYQJkXERGASwthwrx6FXeNZE3w0hWVF17hAKBeX774BhluG-vOwvMQfZqupdO_fgr8M-lVpD0g_YTYmDyb1a2bI7FrsR20Jh0jY33yRhpcki6Qp-ZYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23008" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOSYa-u9Gt2rBAvMQvmPQ4g5QHitdE8Gq1U7jl1vwpI9wSUiHIDe05iyrLplrVcI0jvIZWW-7yY1l73h-OESc-9VGv0tjz5WS3pRvWHtMAERNazCO2TZWf3Xfbfxz_9zSvR4ED1wedR9qZVx7aIQG9DT3u5yvqWX2cjc9VD4CVKRMQ2yfit2S1qEkJJZwhj7jN2B0c9lXh7LdiVijBesZpLjgEWxh7eT65wDL_d5fx6N5YA4XnDPb8jKejHIoLhFX10JX_2Au1WMjxuYM_y_irw3vXUXe2RmUrqd_bqd8gIpwhfGjYELnzy4VbZ4clcawF7yD1OCjW8xwjJkif7uug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دبل اولیویه ژیرو ستاره39ساله لیل در بازی شب گذشته این‌تیم‌درلوشامپیونه؛ ژیرو در این دیدار نمره 9.0 دریافت کرد و بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23006" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8LsG8Dr9x8i1qTsLO3hXTh9vQClRSKy_qLK0HTlUDnlvaEptsEM7LDNlk_IQyqn7EQoEgctfZe77nLdxVThM_K2WyrTk105A1D2i3Z_MLv3FeOWvkg91qoSLYrN28RzMgY31hMT8nai0A9hOi0WqKQnRfmH39YiZWcP7ThshiDjO-ZDk-Ax4Cm8ciq2I3EcUJ6rDEXnOuavDQqhZxEcj2KSywi4gjCYnn0dXgV9u-OGcRmDY5hi9bFATXima3Q-TcJXLZpWtx4vb0UqgQx2jSl1Csj9hseye0DcrGr9TzsjZg1WOAZ_gBA3N6J19Ygn2QDLImfJecx0DPV83W_OoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=V2InoWxLRp-QXt5AtKSPaOcaN8NelaGp3l7JAsS9aVzTMj-Y9oPI1d66Bum6ufNg5nVkZu-iRsTrz6YtVQVR9qWlHMj3vs80xtt4q-2ZURmFSGo3APW330KTBwM7fwJkbyxE067mq0MuWkaEnY0eL9aH510W9Y_8nXN77qFSd4KtrT5b24allZQuA5aQP1Xzmk7FCac2fxszTT47lJfH9UrUcfqWSxbuoAWnlP9ekJbDSsZjG1jhGrbKgXMsZPQYAzwl-eMfj1em1pFONYOEUgaoCiXQeu79QVdov8Ez7LNw5Zi7b-yqVIjuQWgmdAirUr8jEZGZcbKTeAR3mWP1NDnPp-dggRC1GV0bFp8T6RCpjhNXDoFGYB0XB_KcoMTXTLREjAPn0isgxoeU2PUFRZvhucNGRaLDrZoK0WzaSGPcC9rM-0kdO2Lr0_vyqWBzC9Nw5AivU-Gv6S-YZgSmLQfQ8oVT78qcnIEu1JjuwEeevP1XYocOcuZvYuUS3pwzdRjTmA9y831sba996YCvTe8waeqqCS3UxVCVygB7RMaqQcXi7_qh6GzKE2xHP70COTCXiy360GpDqU6KgGKoYpvX7yDASSV5Q02nOTu1hmlJJHFSWfBZ6NZpegTpdDzbZV3s0UajRY1kJu4v3IjpP9v_tfdye8hl6iUqPOQ_WaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=V2InoWxLRp-QXt5AtKSPaOcaN8NelaGp3l7JAsS9aVzTMj-Y9oPI1d66Bum6ufNg5nVkZu-iRsTrz6YtVQVR9qWlHMj3vs80xtt4q-2ZURmFSGo3APW330KTBwM7fwJkbyxE067mq0MuWkaEnY0eL9aH510W9Y_8nXN77qFSd4KtrT5b24allZQuA5aQP1Xzmk7FCac2fxszTT47lJfH9UrUcfqWSxbuoAWnlP9ekJbDSsZjG1jhGrbKgXMsZPQYAzwl-eMfj1em1pFONYOEUgaoCiXQeu79QVdov8Ez7LNw5Zi7b-yqVIjuQWgmdAirUr8jEZGZcbKTeAR3mWP1NDnPp-dggRC1GV0bFp8T6RCpjhNXDoFGYB0XB_KcoMTXTLREjAPn0isgxoeU2PUFRZvhucNGRaLDrZoK0WzaSGPcC9rM-0kdO2Lr0_vyqWBzC9Nw5AivU-Gv6S-YZgSmLQfQ8oVT78qcnIEu1JjuwEeevP1XYocOcuZvYuUS3pwzdRjTmA9y831sba996YCvTe8waeqqCS3UxVCVygB7RMaqQcXi7_qh6GzKE2xHP70COTCXiy360GpDqU6KgGKoYpvX7yDASSV5Q02nOTu1hmlJJHFSWfBZ6NZpegTpdDzbZV3s0UajRY1kJu4v3IjpP9v_tfdye8hl6iUqPOQ_WaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=aMnmpgKfC_LES7u9lG8Q2VfgBIVZSjEjpVtCoZDFlMHO2jRIkEZPGSt6iGaNn6UIrMGCmn_-MRw835KOzYGuZbBI5KeLdyRjXre_lMS3rGZwxq8L3zCy_I4HSqTzQ9AUH8W_Fbrm9-8cSt0-7p3iXvvSyMUWZYDXa_Rx0WV-xvg219CyYjSEdsTAhP8PD-vKTVAkzIyc6jUmEpBVAmnr2LKn04rtUN0q3JR73n_Si6haUcZF1zMm9TpqxL9PzNWW9o5RO5jD_ecj7SW1Z-nzYLo9yomBQZz7V_u39xGojTyFcld8d49FK5UtvlKnTn5K2noE5aNKgAvDgGv7Mv-Rmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=aMnmpgKfC_LES7u9lG8Q2VfgBIVZSjEjpVtCoZDFlMHO2jRIkEZPGSt6iGaNn6UIrMGCmn_-MRw835KOzYGuZbBI5KeLdyRjXre_lMS3rGZwxq8L3zCy_I4HSqTzQ9AUH8W_Fbrm9-8cSt0-7p3iXvvSyMUWZYDXa_Rx0WV-xvg219CyYjSEdsTAhP8PD-vKTVAkzIyc6jUmEpBVAmnr2LKn04rtUN0q3JR73n_Si6haUcZF1zMm9TpqxL9PzNWW9o5RO5jD_ecj7SW1Z-nzYLo9yomBQZz7V_u39xGojTyFcld8d49FK5UtvlKnTn5K2noE5aNKgAvDgGv7Mv-Rmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuqdtzcfSPjGruwpBJQwpktXGPTdiEcFHeBhGJSIAQFWJ5_QCW75a3ZYtPIe3maFqX34i4jv9Zk6EDoLmWjX9hjZ1tHpQimK2cDAcyoMy0Qc1sp_w22OAWe9YV-gjUlpk4vjkZ8_Q-UgUosjK33k6rAI0I-6A5yegdgiUxcnNv7GvPRqwpm2qydIlosfJYRxwzU19KYwTq3t5norArrVjmES7GTFaiQeoyFPs949SohcIKe07iJHOEe3Ngsx0Bgxsp6RoB-XIo6hhTWNSSgsPKh7exbG7qBcDaIH1-aAjHKI4Gm9Mqs7YKVAbq3AM6dJf9RJ5kGEwS49J0dgM3XZ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
پُردرامدترین بازیکنان حاضر در جام جهانی 2026؛
کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23002" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tx5zIw-OOFxfmgEb2iN6es5ElnwtKFoh8RfqRCEd4qBWmrPIxuRBwJjptTW0SgYQU5R9TgsK0G5UPV8qbOwllLsWTgLq7CBiOnxPb0uCGbs8PhchZ7UNDnL2lpxHAYiGhIGXb-PyIIq5q2wPRhSr5gSVZ8_Y33ejT19PQW5soIv-OqmlvRZETtVMksmzVHY-iyuOw5aDPdZmL6FlpOqjQqr0aZ56R5_GBVv7rD7_myJ3j37fPr_U1_s6_xLeP75oVU4XDHWoK0KUz25nI5r8O1LWP-GdashhFP903VaGj96Gd-QWQ6JO_ys2pJCsnF7umXTWfwQpY_hemMVXbs7m4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌پرسپولیس‌بزودی‌باانتشار بیانیه‌ای جدایی مجتبی فخریان و یاسین سلمانی رو اعلام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23001" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf3CILkbpeCiuhpYDdkJtVI2wuj3AGfY8rdg5KQa3NQUlXHNI6G2X8-vlHD65WW0iM6AakkPHFvq7WoEeMh6iZT095VPZBz75fXaWrFILlE9u9JSQF9RNdvoHH6GbwR_gfmb_S0dtCyUc8iRyL43uheMSlPVOkSfk00PsxF37gjJX2ncqE3DNIKrj9lDn12pnyCx1WVSlbHRC99ldURdRbjxiExrqTl8YirwEdhy9kliakpCK8EAl7O-YvzRUbWrlMyyfTeqfkpNwQEBc_aYw6rZHumzH6TUVnE1JlIAYWdUnl4v-VK6QvSYOS04j7TI7I3gmOTFvxEKIgN9YYPljQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در این تیم، همیشه جایی برای پیرمردها هست؛
ایران و پاناما پیرترین تیم‌های جام جهانی ۲۰۲۶
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23000" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjuvdyLBQmmr3dxvnXslvrXzKIivgC5z09F8CHBUBDc8hHTFYNQbpuYe1FLssD9gDybS56UI1Qe9hrjj97U2FtLUTRDVBaxVtzaEUvyCKR8-d8X463nHQPODZQToeuMTN015znpL5WbEWHKr_vSf_s7Ch-OLepgC4ZjmQXYYWjStee-fgmsCxmiXqnZbfgOiG22u0zC_j6hKP5LAPhsWMoK1y6Z_7WfgAxxReePcTcJTr---iSBPTbUEqJxThRvfNF-eW3qts1GH4W77KWiypu-2xRwP8A1JS7hYCz7yKUlUK4yPJ8ds3XdFNT6Yg264SDE6Yqff_PSkrzLzgxRnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22999" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeNdqlQ7dURzWRGdV0q-AOg9iSM53M7HEmihrKeob8JUJnQiDh1RPsMRu0I8J_7bp4Rbg-PD4SJF4mk7cf9cLfntdWkqasgTi35ygrpWlk2YbUVrsTzwHhA7C_bg8qFBzWgckldSB-AQNIAHudFQR_JX1pyE2sTIJlTH09oGBtWKXuw43df835uZ9HahP2yzr_VN4hPyMXcp61f6l45f5ypvPnhXpRR8ijIHVLtb7CoS3slUkTcDm0xot4Gim9p1ZCefRBGkcqZMvXn8jUiLGiNrmnVomRjteyholamwYolh5pYmP3s0NtAh4-_82qX9uLuL1t2Qb-KOaoPOBBgwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22998" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3TTxDNOBA9ZkNC2toqha3_F7B6dRXAws5sJXZSOwn_zwjSzduj6gHlbPWuYlBoSxdBBqa7lKohKl3V1xKPcxKJVF6_XG2VGM9CSxCmHMNzqzj_tkWU1PUywRQrO-5pLoyNDSvqQ5eHpYcL_Fn_JP_XVvzfkDyoUlMTW_sKHUNs8idaWbEg6y0X--vEMx-cUIu-3CMTWCJReYkWQfmRHjDHR5gkMAYNNpH5JxFnjpdhT7DAjfj1eLmPsu96JLdhYNGW-ID5sMlf6O8tTt5ghr9I_U26bCZg0YUntkseS9ntatIsrGwZMyYfgfIlWU56q-RSYYb6NOMNTwkZLLHG_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22997" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=ZMn3eT0nrx63pUZQHZ0dvUJbqlJTwHkWfWIYycP3JhNNpABxOginBcgof7hw0hPOqv07J4pik_mByf_VoihGXM-Vo2jym9DypHmW3Q1-NEajWekWmbUItdf1s1huHJDePaAQCbTPTH5nO1iPRKJTBAvTZlnGuc1Ntsy6k0qa7HFBKfY5Ef1Z8jOdfBsW4x6M4aEMM8bBq2KqYJa25_865uBQpPRVbqWJB6QrOy48-kuvs8JdZyiEwX-FCyPdJ-15lKSXzgR53uEyWcOdo-YDoOzKjiAJWN56GzbUfCu921t70fE1NY0r3AP8bP75VLzghq-MMMOBOttq2p2FpKg1AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=ZMn3eT0nrx63pUZQHZ0dvUJbqlJTwHkWfWIYycP3JhNNpABxOginBcgof7hw0hPOqv07J4pik_mByf_VoihGXM-Vo2jym9DypHmW3Q1-NEajWekWmbUItdf1s1huHJDePaAQCbTPTH5nO1iPRKJTBAvTZlnGuc1Ntsy6k0qa7HFBKfY5Ef1Z8jOdfBsW4x6M4aEMM8bBq2KqYJa25_865uBQpPRVbqWJB6QrOy48-kuvs8JdZyiEwX-FCyPdJ-15lKSXzgR53uEyWcOdo-YDoOzKjiAJWN56GzbUfCu921t70fE1NY0r3AP8bP75VLzghq-MMMOBOttq2p2FpKg1AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال ستاره تیم‌ملی اسپانیا و بارسلونا درباره دلیل بستن باند روی دستش در حین بازی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22996" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdI1zp7-Mh1SIfKdPHbwGFB2jXu9MjKASu5lOaOp4pmY_QmUANkA6sdwEeTieeVeb2gelSuRS1AsYKCbuasPV3tO21VdjMGdo6TO-MJVLwDP6tF3X3HhHk3SCVRWIGb-D4DQHsSPS0xTsq4oAVczMWD7D25covDM0WttC_XZVtA5ICEnWl6xRu3TzvuFCuu9W1-t2IbgX5gYE3VkLd7VWyrwsf-mL_2wn8AEDCJDxihnMrhnuKFSWVhgtUF25s_B2YopdsKwMwSkZNLGhYs9zUVKzZo3T4MvKfTZ1eoqNdRhVaNIa8Sc_QLT5pfNMqoiInTkmzRK0q7ERaN7Ap6u0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=O-cKgqFKoP8zO1nSZFvBYxflfHTHH1Kb7yAajyK6Rc-EKjRfIZzYS2CC8MRmqDyQK5sz5uwh7rgRTYgqLHcBrUxhsG8EI7HisHMrZDha7I46HiB19k8QoUG3aBAVQU-1C3nwOvKzve8E5gwUhAhUgzfckaSzib7hdE9Lk99U4cg0mdwx_KcO5_ueTY45GWa3bVj5AQQuczm3wYPyrzdKm1P8xSyoua8KwyfCVeJH3UfTQfdWb0UPVuOTQlHwPn5VvvO0ut-cXDMAq-jNJDH_5vuWja6Dg4M6t4t-ucFHN7OpMVIeZJF8aPBwtbUXvAOFTWYY4ZSctipNNVYSYb0eYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=O-cKgqFKoP8zO1nSZFvBYxflfHTHH1Kb7yAajyK6Rc-EKjRfIZzYS2CC8MRmqDyQK5sz5uwh7rgRTYgqLHcBrUxhsG8EI7HisHMrZDha7I46HiB19k8QoUG3aBAVQU-1C3nwOvKzve8E5gwUhAhUgzfckaSzib7hdE9Lk99U4cg0mdwx_KcO5_ueTY45GWa3bVj5AQQuczm3wYPyrzdKm1P8xSyoua8KwyfCVeJH3UfTQfdWb0UPVuOTQlHwPn5VvvO0ut-cXDMAq-jNJDH_5vuWja6Dg4M6t4t-ucFHN7OpMVIeZJF8aPBwtbUXvAOFTWYY4ZSctipNNVYSYb0eYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازیکنای تیم ملی فرانسه بعد دیدن اون عکس و ژست سمی رایان چرکی اداشو درمیارن
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/22994" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F099z8f8nBos5Pbgf-Jtxxq12J_A0edx-gQH03dE4Z1YRIm9CXQIFtQSeMNdF_ggAztezJ_ySLiLmvOzrUWDJqIbKlR_uFkVhwYFedsQBKPfPIR3LL-QLc5wifiDL1jeyupUgJaN8jMvAcQW4fk1PFyuCROHBQJe93fpJMMbJ4SQi-esbhCBGUM35aZMPDsHVgHIhwlQk1eGCPiyxxuwMrBa4gN_b5q7PTdlpNf7dlwxABWhvLblyXXWzCSK093WUrJ9pZ8Ttx0fYMGgU6l-JCpG5xV5rBryy7lg0Kgotv7DQTEuKGYY5J3q2Trpvs8ydsEYFb1INDmuhSKwoFOnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-4OhyUlyakU5ZHMuwka7uLtap9FHLKKLedErcNVJHmFf5iCU5S8KzpGlYDse-jxXoU1j042j5CrN8iYuflxzqP87NDXA6ciI3jnPVxzt3l9b0O_-Aua1YMN0sHfitJAVqzrJb562EyFUP5QoJKBUDnX72HevKWQ9eShWEE0BJW1R7t7s2awQMhHH7He9zc43VqEKcPanntnv4Lk0J2LwGs71shKZ2xlrYhUEVTYFHVdVHAVuzf-M8_shOlcPMTVF6K6BQG7IafV5woRLWuzDgJeKbVl0VVU8zmVTKai60-gSzJsMdllToMzrmOmFz33qp6rA-MXMhke-UliBmPzDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=ZnOHNnnPM9leByDPVH9uZusgbpN-FwNRMjlr1ljhOYUZDKQx2PuuiqjfA3nATShsoUcyAWzdOjywHS-T98RUvZyoQBVXB6kKJzu2vzd-3F82XAzRf1xzam927QIFRPy5-pkiynrZMmnyeYTzf4j6UuB9wOSTxebvzaqtnKBjudlbHdiwESTmxTwaOkQgbvlGiEhtD45CZF5P2SOc1fzuTOD4-FQ89IIWxCchH_j-poSGx3HyachRrhDL-P4IRhYH1ptJ4nXJJ5v5qRjWfj51qhW7nv51-r0kjzyJnPdDNOEEuziPXt1cFVWR4DSbue-9x3HzkuEVzcVVOncIRBpkEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=ZnOHNnnPM9leByDPVH9uZusgbpN-FwNRMjlr1ljhOYUZDKQx2PuuiqjfA3nATShsoUcyAWzdOjywHS-T98RUvZyoQBVXB6kKJzu2vzd-3F82XAzRf1xzam927QIFRPy5-pkiynrZMmnyeYTzf4j6UuB9wOSTxebvzaqtnKBjudlbHdiwESTmxTwaOkQgbvlGiEhtD45CZF5P2SOc1fzuTOD4-FQ89IIWxCchH_j-poSGx3HyachRrhDL-P4IRhYH1ptJ4nXJJ5v5qRjWfj51qhW7nv51-r0kjzyJnPdDNOEEuziPXt1cFVWR4DSbue-9x3HzkuEVzcVVOncIRBpkEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY3C0Rj0xnyCfJRtKwUFqHgDKmb59dWyRSRITrxFyv8DBtGXIqEuUNRRJxJJTiGCfNbic0iAwG32e3o3AHWFLZTqv2zgsVQkfoOyPRd4BtZ0Tgf0jIOQCxjQPxO8ku-iPJlrPEDw54bs4IexwzGudbzfMk4jmQUeWD79xdaEibr7LaHSJg3UcQk-e_cieoRWM8ryr6-ozjG7A-9BqtrsXCpO1JPRPngXRUASuHWXE53nGbRjH25F2c9LqkhkwqjSC0yWDHfYEdPUtsiMliBD5nPU1sA2jcamLW6NSQDRHlsQs4nYfSgpmArfCJytVtg_TNl12fE8qhwuwJ-NR1JPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه‌اتفاق‌خاصی‌رخ‌ندهد؛ اوسمار ویرا برزیلی چهارشنبه یااواخر همین‌هفته‌وارد تهران خواهد شد تا برنامه‌های‌آماده‌سازی‌پرسپولیس‌را از نزدیک دنبال‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/22989" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Li50UUVC_EI7syAAxmeED8oWUEruTDKXZ4NS25KFeGZhOgOjzeaULH4GWOazq_1vT5iRWfTAjKDQ6RTGbDtgLX9Wg7Ijh6sihfyRlwi6VuscCmzxkF0mhjALxYXy6uszlZqpagC6jSPfc27wdgfkJhCjsoPffpx8_a87vdd-oXO70s6Ox1AbHnBZFEKJcJRRO4-L-aHDyMp8dIcSjNeVFsmSPv1bNQLu68gWeDT_U7w0NeW4M-LJHbPD7dKj0T3VTmlXwV9JBWoiE-h_pAkIcYUFRMAumeJga-Z21-_EMxXn7zLzcEuX9FEH4B5Jj_CvRCrp_j7NcWH9AmkNU7me8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22988" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=SEKr_lV9Sv9Higib-oUy82B4P_GOthNzL03q1_BNgJupKxjmmRS35pUReFRJ5Q-JAEBlWzPR_7ebIgG9qYRjdHBYPoNY66h01G7xK7JHOpxRgv3-NYHQX3dtSfBvBq-d09jKTYw78vooFZTxkAxZ0prQuULSWaOsmXGxW88I97WtEHrREATuTIkRpkyGWBD-rotPJ8A3MoBhGPPv8qhfF7zuyPiQXNRKKHPNJiCVEZ-1i_vxiddC_cwNweaIIKmpdQ7Fmr_uHgbTvE3U_99XDtKLPFXdUwfzW6v1afl5JlSkWxzWhOB4CfHf_jw6FODE_dbxZ7VpziQBtxpl3vDYug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=SEKr_lV9Sv9Higib-oUy82B4P_GOthNzL03q1_BNgJupKxjmmRS35pUReFRJ5Q-JAEBlWzPR_7ebIgG9qYRjdHBYPoNY66h01G7xK7JHOpxRgv3-NYHQX3dtSfBvBq-d09jKTYw78vooFZTxkAxZ0prQuULSWaOsmXGxW88I97WtEHrREATuTIkRpkyGWBD-rotPJ8A3MoBhGPPv8qhfF7zuyPiQXNRKKHPNJiCVEZ-1i_vxiddC_cwNweaIIKmpdQ7Fmr_uHgbTvE3U_99XDtKLPFXdUwfzW6v1afl5JlSkWxzWhOB4CfHf_jw6FODE_dbxZ7VpziQBtxpl3vDYug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نه‌داداش جبر جغرافیایی توی پیشرفت آدما اصلا تاثیر نداره؛ محمدصلاح اگه تو مازندران بدنیا میومد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/22987" target="_blank">📅 10:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=DDRomNm8Fo2oV0uYM4cxjSLKQy-shT3uNg_6JiOagrjR-zjgXNNBwLzX5Gdf5jOB8C_QSpBGrlEPaOSKsbOiTHJ922_CGFWZO76XFlrKCdOWuU6CgewCNXBJCZDq4zg7ZHZO3azPmMW1gBCzykuzJ5DkDCoEGUBWkn-LbvWtvIjkVWS8nUuyJfDOOCiQk0wSy0wi3CZLAvXQOoKJ0vsM0wh9b2UpjrXfCByBnBp-Q_lYI-9ek8nDai_wEgfIynNBV7mbqslIb-CqPTYYMQx1_-TKZEu9CJgneOHIavMKE7kxcuHZRlvQrxM8zQZ0JnuoYbq9ZoAmJ7MhYDZZkJyVMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=DDRomNm8Fo2oV0uYM4cxjSLKQy-shT3uNg_6JiOagrjR-zjgXNNBwLzX5Gdf5jOB8C_QSpBGrlEPaOSKsbOiTHJ922_CGFWZO76XFlrKCdOWuU6CgewCNXBJCZDq4zg7ZHZO3azPmMW1gBCzykuzJ5DkDCoEGUBWkn-LbvWtvIjkVWS8nUuyJfDOOCiQk0wSy0wi3CZLAvXQOoKJ0vsM0wh9b2UpjrXfCByBnBp-Q_lYI-9ek8nDai_wEgfIynNBV7mbqslIb-CqPTYYMQx1_-TKZEu9CJgneOHIavMKE7kxcuHZRlvQrxM8zQZ0JnuoYbq9ZoAmJ7MhYDZZkJyVMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ
؛
مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/22986" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ctWTRwIf-YvtIFjDsUnRu_iZfmMduUso0C2uslj1Siz8MQPG8X-fdlZmD9-MsvhvQKE-tqExhmw0vqwhGzbc_yFoNkWfHIVxfBEn4ROr9hywzg-MkYBuXW-yEjIeiTweN3ZI53zb1jB5nwwOXVArK9R_ezLQu-4nFkJp4DMwmANcis8ZyvAPUKd9WbnMSpc_rrqjXebdO7JePQg055g4lIz16q6bjONOmBAt1YZ8TimLKuY911x_Io5qbfIxTvnqd1FxF2BBJsJiANPf-NyBCTgdCC-VdoWBct5Gl6YF3sMRFiaWM-1w2B63ke-YR-3qSWj94PKAsTOjzCHjlm6TIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dGMNkg9Gwd0rjGBszCKVpLPkQNvUjarBUHyLMm_50xFF6QDHaZNWihR_x-hUV0q_GAMHMPHG2rHxoYmHREHPLZ9yk7jlKkewX2kNFNS6usWo93tB-wJciK3Nx65TYwh-4-4NR8RaHyiink-N6z3jJYMTF7F_toJLv4Dq_IWjogGh2WGPG_x1gE7cvlORei4qtT5BiNt5N7lemAOOO3rvdLJ0DiZH6jR_pkEoq0AhMQt6W3FUijl6a5E4WXdLb6iORTsBJqhvlBqL9vaGqtH-9Z6Vm_uHRGQLSPfako7vK1UcFdm7Wk5l_apmyJNxbdup7Rc3UukDO6l8Tz4c8qE51A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.  مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22984" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=vu-_zYe4kPaPcWDTq7jVn3kCIcbekwdau1vSh1oIK_EEbpS7f1vYrHOJjgT7Fznsp8Dey-8z5RsJOs0o4Jy0PvPRKQXFLSR0rSh0_No57Mf9nLZdmAj-BYDDa689UbW1_cE_wCc8KW3bPXYXjUXor21Y5N2qy09D2xit4Own6fcr6h8-ETcQV291yk4L1kkwDmhF4jx1v58X0Tudmb9SEbTCEMGDiaOF7ym2agy2Jo8bTBI1DVT87062OyyEnU2aTHVOr4mjkMfnseLwc_Vcld7anxdDr4B0Pj_wOeln_w-nR9hhfLwvLUBGm_Ti8dWqWhkCPf2qb3DBncWx0WX4gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=vu-_zYe4kPaPcWDTq7jVn3kCIcbekwdau1vSh1oIK_EEbpS7f1vYrHOJjgT7Fznsp8Dey-8z5RsJOs0o4Jy0PvPRKQXFLSR0rSh0_No57Mf9nLZdmAj-BYDDa689UbW1_cE_wCc8KW3bPXYXjUXor21Y5N2qy09D2xit4Own6fcr6h8-ETcQV291yk4L1kkwDmhF4jx1v58X0Tudmb9SEbTCEMGDiaOF7ym2agy2Jo8bTBI1DVT87062OyyEnU2aTHVOr4mjkMfnseLwc_Vcld7anxdDr4B0Pj_wOeln_w-nR9hhfLwvLUBGm_Ti8dWqWhkCPf2qb3DBncWx0WX4gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCsVMK3DL5UWcIwARYzmVrkiMxCnFCGfS9l4Xu3zieLWY1mSjlvzCoa4eUVgi1__XKnLpqYRN0sdlGIrDjdVm8cz_Ueu6k7e043YXjsIA1FK7VCWcA7GBsh7aEGUMXOnAXPf607TT1eKZbzV2ZHO7kjbbjwY-2WJmf13YeOVwSvKFu2GY2_u76hVCjz4OUuOZxodjeWGx8wwg2nPCSgxgDCxPujMLw-UbN2Jp4P1CMWKJhMt-eviwD-6ZUzmCzqka7Iv7VvgeNo4hClPhvi3n6MSFSQAedLvZtY6DyJuYqxqtsO-StwrafckLVBLufCKNZjM-5M_sNz9_ViAoo8hbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22981" target="_blank">📅 10:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjUpRzZdv3nQV8azchvLYIqsoJRfV66v8Vd-K_gFYyyDlUglfKOfFP8yINSslILSjcdfeH7XI7b-uaDy0WpTJQ8GhgLa71L7hEYP7xEvJwTMTGYFW6VddqVYr4T3r0QLtNcnpJVdjqlMCQx5O9S-FAK4cA1LWsJH2LsQuH1ZOYuJoA06y0uXjH--CDphHuw6rZpiDtMe_sZEDmVhIlqf6KrpyRJmXz6cp81XmRxfKfxr6cjpQzZCndR2zgTeCdoZFIYl17HnNOsNnkQ3V6WoX9Jb7sGxx-d2Owek6ZTzFnxBlKmVdzMybyHjyazTReL51oFkKG6C3lGnfkvChy1yhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات
|موندو:
مارک‌کوکوریا به سران چلسی گفته که دراین‌تابستون‌میخواد از این تیم جدا شه. اولویت‌او بازگشت به بارساست. چلسی برای این انتقال حدود 50 میلیون یورو از بارسا میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/22980" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apLk2bPXPrHuskpuErvvDXAP2ucOhmAmGBZrydr3g7p74H_cyAW5DX-LZIXYsgA1wZmrE4cop8L0Fi58kK1Vz6XM14HIMwmooY6ojZml9jIw6a6BfUN75tLMCe_miAsVW9k57aXguCZrgRHyJFPcKxs6D2t3F8H4CjOoljGU--iXLkzCmDZR8JG-0kLrPV9oDV2PyuU0JD462Q5J0UFUa-IT9kkXcN67sEOoRgSfZgD11qTCGdIMEjkYaoxlIZa5LXt209TVvgjjZZTe6b7Src1W7oqzSIbeYqywLRVx8Mkr8j2EyZk7m6d8-vYADO9PZYKli09hNsBq_zSOXN1Dmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تموم شبکه‌ های ماهواره ای مختلف که قراره رقابت‌های جام جهانی رو با کیفیت پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/22979" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwX_9WZGYowYU-tX0oaCk9WR-J80J0J-BYgPUx2qzBFFKewnFDTxf67D8m6MY0Zu38u8IO5oFWXXof9lrhhk_DFSu72_Hb3-gfSbrTNYp_oWV26HwEOTgSMpApkeAGj6WhhduyIfAsJh7U8c-AC7J3yfN0rcVXFNCPE4gOSdep9dH0FtELbjwcyRR2P4TB4CboeAq51TpzxvVMv0FjKdkhdRh0yom39eYdIhXISghB_mjyTwZFF97DhALWLyiiD_IFJFHNSkXabFT4S_qB8LcPB6eWA_3KmzkqZvTRaTn5LvnIWHrQ15hW29XzkA5FXWIXLLCT-je3WVZnPBgpudoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/22978" target="_blank">📅 02:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX0EPMHlshLMLW_Ju08vwan7sYtOicizYMFOCV6nMZrdEwKcQeTEI3RNfr5j212Q4Y5NampCRZS1cw799jtnL4vF3_ORgFBygEWkCp4z6XMc2hbKvLdPlcaxyxQmE4uDCj7Q5GWa4UAf_U1H5fl7FwSJK2q7kIt1GVAfHnvZlJKPix8tjDGtx9AdW9cOsOCO3LtZaUgLEqVoRVyPdksgtqvcHmSaO3yXcE2JHF8TI1F0zIoQLtY0jS06Vo95dQ0n4eRTlE7Evos-U0KMhh6tjCybHI9qpjDXuWpDxfKxvUWH0dn-XI4He7VZCtlVNPiy4gA2Pfk5rliVv-JF4znzxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/22977" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdNKOyelfjwx1dH2Wn-1e4ZWYJ5dN1ddtyWSHQEMIYIGt3S_eKSJdrZ2r7xUfToz9yZroPy9H0FR9CZfER4BTNqjFzFciMKLtQXD8SQDo1sZXQenR1sR2Bbxkm5USYmZboeVtJn8VwlYdww-rxcDc9ZMB4TaPzxWNXs-nSCHN1Jk2qGX78_M0cNV1jsl--i_5hdDf6EQXcsAM8CnPUYCVl-UuWeBQ-VIdYLa-FbtIAWHiOX2dtwSTK-pqckTw2ABDM1DJsT5WtDUkHCeXvllYpui0ydMMsdqfnxnJSfF5b5ZGRUvpVvFUi7XptfOoFwHFhfUwDKg9CKg9Dy42G057A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛پرسپولیسی‌های‌حاضر دراردوی تیم ملی از آریا یوسفی مدافع‌راست سپاهان خواسته‌ اند که برای فصل بعد راهی این تیم شود. یوسفی از پرسپولیس آفر قابل توجهی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22976" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2xWr5XuXxxqau4pGWNFGXummUyDhYWOCWlzk_yYaFml7l4u9lJmt1sx1xju5dbhrAfNPKgZ0nUnl0ped3JXyUU-UBKbz8oobegCwI3qvQwLLe4egw_ZucoftpqrDe9V0_s7tmi2gIRmZddL_fRZIdxmEfgZISb2w74jsZy-U-AXzTwtxRatDftgTfpUD_XyFqX7nxDFGVZFA21zYLeilQBcJKbeEWKXPUhR80GPgTq0iZFZL60xqgwJEYW1lsCZjcgQD3Cdac6LGNclPc1_ityInU7YfrA9v9tjgfTZt84ipt_yTswp4OjyNIkNr82f__lXo1IEER7fpJmeBQk-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
از دوئل تدارکاتی شاگردان کومان و کاناوارو تا آخرین بازی فرانسوی‌ها پیش‌ از سفر به کشور آمریکا و جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/22974" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5Eo1dQY9bM0K_mm2DdGdM1nT0xtnTewbHF1pfd4llJ6akc55xKnpw_ArvVehgYhuVCf7MjvtIRFOKHqNKEO-MUgo_84_iUd5Aqfw1UwraAJ0lYIS0bmC8I4tcvBRuJ_Brn0dCWfeXvSrSfb9uY-TZlHbwioUt7UmqXp_6VekJ0D6ov0fWgkf0h1ArLe8m7kcGiVRwwrPxFMS1cLFjzNcBGvAgf_ClVnULAc14F90TfbsCpY9SyMJKyF27ZVbAecBa8YuRLVXMZYB-dL4hCSnF4Kr4z3tp2c30A8Mh-kBYwwbeh83N2-XDVFRKgiUGDbVCijbnLTon2NVevoNuA5hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از برد آرژانتینی‌ها در شب‌‌استراحت‌مسی‌تاتساوی درجدال نروژ و مراکش
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22973" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoU2DWzTM2hdIba6McXfRoi9D0a-A2aoFQEv8SaOxehUVxK3PAzO_8wYGZ1bHuYk941Wqwsc9KXiUS3o2K8cZk5tZAwBTRgmk7l0X2jqyiR8LVzQFVyjXRMT3CTZVRdETh4pwuPlOjUsrVjdHLIfDXFIHUAQYzbtw3m5ZldgO1_uGOoyQY7Wze22ZAxvo1UgRgipZDdj7ONBj2WmS5636_6XTpIuMPOENT1_BRDCLB6xv8CU4TIAXsqMlPcX0r4Xl83gtFBRGvSWNmHkq9v0xcfDZVXtrgovXsm0SXzQfIztQF1QI9WceJdHG1d7X8K16L-G69jJ6KMXDRUjLgy-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22972" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=k4eq8KIt1Eo-TV-AEnAgNQgfLuSXhzivJ4al3W3poimjc7s0aACXplHCMvSjg8MQZ_UT7ksjKckN5AihNzgHtnrd1Uw-Ek8yHGBzatoFRPILKyC5PZChqFadT3rrHQ6Jywgf5_Ai7lKRIyneHa77XU80f7y6__bfjErzwIAFH77mMAO2wS9n759wOGQhqElLc9CS8aMRdWLzn3LJaEiBoLeee0hFrGa7d_GqiOHqnHs991C3ejYOtQ8mmL_buO0r2b7UZw53f_ZV-b89z0qms7W3niZeV1VE7kzPqz94XKCdRBkWVFf2cuwht4A3NadCOcAkiLCfaaIzTbwODfvp-FspJsuiUVP6aa26j3WNMSV_J4dd4xKH7d4T1G8o8FNIj3TVv4qHpW4Cf2N_ySGIvt5c9Q8cgqldKhpi9cKTz97CccaEB0ru8OAwrcGLTs-x6DKaekXcc4HVbAva-Ue5wo28fxzmGU53gaZTWlkz-Swcu4yW_Ke-wDtABAf2txD9YokmbKVGdpuZ6Q1wjYU8r3CW_bOJzXpF_i-GfGs7Djeb1nxkC6lHLEvftGxD__LfWpVo-4RevJoxQ8zD0fY0WAEfRFV5Ta6puRxwUBmmgfifJAiJSWHU4XIQwa9E_VJYKNjDNvphIkZtJawLn4HQqZnFoUgWVZqZgMMPW9vxdW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=k4eq8KIt1Eo-TV-AEnAgNQgfLuSXhzivJ4al3W3poimjc7s0aACXplHCMvSjg8MQZ_UT7ksjKckN5AihNzgHtnrd1Uw-Ek8yHGBzatoFRPILKyC5PZChqFadT3rrHQ6Jywgf5_Ai7lKRIyneHa77XU80f7y6__bfjErzwIAFH77mMAO2wS9n759wOGQhqElLc9CS8aMRdWLzn3LJaEiBoLeee0hFrGa7d_GqiOHqnHs991C3ejYOtQ8mmL_buO0r2b7UZw53f_ZV-b89z0qms7W3niZeV1VE7kzPqz94XKCdRBkWVFf2cuwht4A3NadCOcAkiLCfaaIzTbwODfvp-FspJsuiUVP6aa26j3WNMSV_J4dd4xKH7d4T1G8o8FNIj3TVv4qHpW4Cf2N_ySGIvt5c9Q8cgqldKhpi9cKTz97CccaEB0ru8OAwrcGLTs-x6DKaekXcc4HVbAva-Ue5wo28fxzmGU53gaZTWlkz-Swcu4yW_Ke-wDtABAf2txD9YokmbKVGdpuZ6Q1wjYU8r3CW_bOJzXpF_i-GfGs7Djeb1nxkC6lHLEvftGxD__LfWpVo-4RevJoxQ8zD0fY0WAEfRFV5Ta6puRxwUBmmgfifJAiJSWHU4XIQwa9E_VJYKNjDNvphIkZtJawLn4HQqZnFoUgWVZqZgMMPW9vxdW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22971" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=UYJE3OzdbJ7ZsnRWo8R6qklVGGyKuL2US6WuJQdI8tHTT_fENFAXF1RwKvgXz-Y8yKIuMHI0g9NxgZQFiawTZocREaJc5HxyP8Xk3-lSw1xKem-xb2L5RVdkKOTiqP5Lmkydcs3U3vtuZWphdepmY5hImF9WBdV82OFQS7T-RcYgXh70U4RH-zsdMxFVQslE9tK-eQNwZRKv16nkKVbt6KTYK_qzxCXuPQNjBCvVs-BOVWv49u8Npw7nADvwFF9CddIvvZpjoRGVYHN4Vz4XnLs9d2AXa6HmdTY9E-HS6zaRv3nve5aiTfynEfX1JquwX32Mdhv0cIZoqWGNILgO3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=UYJE3OzdbJ7ZsnRWo8R6qklVGGyKuL2US6WuJQdI8tHTT_fENFAXF1RwKvgXz-Y8yKIuMHI0g9NxgZQFiawTZocREaJc5HxyP8Xk3-lSw1xKem-xb2L5RVdkKOTiqP5Lmkydcs3U3vtuZWphdepmY5hImF9WBdV82OFQS7T-RcYgXh70U4RH-zsdMxFVQslE9tK-eQNwZRKv16nkKVbt6KTYK_qzxCXuPQNjBCvVs-BOVWv49u8Npw7nADvwFF9CddIvvZpjoRGVYHN4Vz4XnLs9d2AXa6HmdTY9E-HS6zaRv3nve5aiTfynEfX1JquwX32Mdhv0cIZoqWGNILgO3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ایکرکاسیاس گلراسبق رئال‌مادرید در مصاحبه با روماریو: «مسی خواب‌وخوراک‌رو ازم گرفته بود.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22970" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
