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
<img src="https://cdn4.telesco.pe/file/oG5WN3DumIyYO2OzQsTg9uzPIveG2NN82nUPehypSDe7gISpQSNe3TuJ76BFTHNb7fKwnhcGlw1QJw48of9NQwERO1rGMMp98FuSPE_81nYlcC2FNfdVeS9CsILDNgyQ-vSw0wfvyWKbqcLWdM3CwxUlrwoRwlj11rj2vGVmSY3CC2As58x5rNo8w-M5MdtvKu4yfXPA69bllcSne9ds6eZ4qh0dj0lK2_F_DgKDiROuYvwmw1Igg3FAQDXKUj6a6-W_tH2DiKsHaLL0sitllotWzymx4U2Ga4hnON2gw12qYUoJPMkyLiwqvfI56RJqDccqVQlgOOiqLyELySSt-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 20:31:06</div>
<hr>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFX74a6nsStoFi_KitK4iAhz0dtkBtd2r4JhvNDxvW7yt81r7YPOTVMT2ABqCiTIxEWUhDdt2V1sbTtTx4ibwP7jl29ujqeo3JUozzbXM27h3S6lSW8NB9alT8KY9f1K6V25OIkitHbYn58j07rQqfcIHWFmeFF2kkz3eC_mUnIEYhMa587qV6dOEGmhavkVUuvzEOO4n9s1IisZZWccxBhs7hu2PCxQtTSv6coBbLX0JsMXJ4Vrxa-KB-AqpWc71x5k_X--BSVRNQvq3H3-gfFBNZBGBVVssPEdelyVxJki9RRXJbddR6Qz1KVEXTYXiRcFdRKKj5TcDO3BNhqCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqWa70UuXvYgm82q4WeB5gldwDWB5ClQHPmwXBrE9yLirAFDO8IRtphWIuQnI-DJlGJgio9FCHztlSkzIGlwzwDFYTgCTOZktFtBnPJhUSyN0bQXatKmqFJIZ7cHOhW7MJAQBkR86PBrhtq2H2d0HtfqehXRFmrudeDVfLoX0x0Lh_C5m5ACEMTa4Pligf8NTyC6iwKGWkRiBCOMNI1J6wDvvZ7EedzqBR4dpQpZr5ks6Gja87kAQYgyroQJ2NWD2HEcsehKynWin5It9wU7gW9jJRipjlAhzPR1nx7H0gSFvbXFB-FkxpIFXStH49YPNAKP-AbUWCovJ1ScAqaseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=KHqS3Swaw2IuvSvry2Fye_286TNAYmmZvcJFna1Eyow3spKgptg7ZIzjibbDCFap78aMo3b4rAtW9Oan-mtpCfHWYGnH44UODTWa7NAPS_qjbdmDtbkc6ixEhiczSU1hNZNj4fjlQbeC-GChL8J5W-hXv9Uyxbva-GABe2p6IoyGssNp-jJPStzR-UlY4LWesawHk7nNF3BW6u74urJ9GLQ2ng3sZXWg5GGaoDogce5ZtTU7q4ttDLRgxVFkcZFmxybYkOEIVLEvrvOkfecGQDcOGXdQu9lriiqDZBwepweHddC7SnDa5ZtG6qrXEUwY2zRGHWh9ECh9dbQlZ5Cd2WX96UuJNq7bizjZ2nbs5rJLS9VGs0NMOsxVJuLZteza5Mwn9iuz6tWPipy3bPoNUof5DFUOyVRXfJybKLwFzTLNwiAkaODAKJMxplalnJtpC5uYf5VCnkY_9i-oGk7hpClTQSOsbE3-W2ZqvTprpOToPJbAYmCdr__6MpSs19nIsoCurKvBlAkCnarGkWY8eyiItXKiz5sP-VxL0vjvJFUnZ7u2Z0zWrxS6J5FGysehPuPVGNDHvHtna15O6qUVSUh1LRCi0cnhQ0vr8EsfPA0PSu4gjqwTZoq3AVuto3xXXJdJhJY14EWMMqkDII0dY6i3YYZxrfZR7AN4zmcSvHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=KHqS3Swaw2IuvSvry2Fye_286TNAYmmZvcJFna1Eyow3spKgptg7ZIzjibbDCFap78aMo3b4rAtW9Oan-mtpCfHWYGnH44UODTWa7NAPS_qjbdmDtbkc6ixEhiczSU1hNZNj4fjlQbeC-GChL8J5W-hXv9Uyxbva-GABe2p6IoyGssNp-jJPStzR-UlY4LWesawHk7nNF3BW6u74urJ9GLQ2ng3sZXWg5GGaoDogce5ZtTU7q4ttDLRgxVFkcZFmxybYkOEIVLEvrvOkfecGQDcOGXdQu9lriiqDZBwepweHddC7SnDa5ZtG6qrXEUwY2zRGHWh9ECh9dbQlZ5Cd2WX96UuJNq7bizjZ2nbs5rJLS9VGs0NMOsxVJuLZteza5Mwn9iuz6tWPipy3bPoNUof5DFUOyVRXfJybKLwFzTLNwiAkaODAKJMxplalnJtpC5uYf5VCnkY_9i-oGk7hpClTQSOsbE3-W2ZqvTprpOToPJbAYmCdr__6MpSs19nIsoCurKvBlAkCnarGkWY8eyiItXKiz5sP-VxL0vjvJFUnZ7u2Z0zWrxS6J5FGysehPuPVGNDHvHtna15O6qUVSUh1LRCi0cnhQ0vr8EsfPA0PSu4gjqwTZoq3AVuto3xXXJdJhJY14EWMMqkDII0dY6i3YYZxrfZR7AN4zmcSvHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=IlCvjUfAFBmLg1zWWPt2p7YF1VRmiFKFzrXtog9v7YUcyJG7l939vJSi88DNd3BL_vMZqOMtcTrjApJs5nHrzlzL_Uib85wUPh7iG47x7o7NbvTu6Ai-aMkrkhCnnbMHLrOdSk1ahWgZHQ5Vy1SoJUyJj0QYGgj6IHaGA2yFZxLod2fE6dpfXZKFt_ix0fQZ0CZuhifAk6ve0n9CZSaE5N7HplG4qsC_VQxzCJ-Ah67bxDp0qs4EIi8HROI3ZXUBJ4dag3p6hjLuszd1-TgZURRg5W5__z-TXJjy1_uWeMZsWtA0-2QZzKSUin07GZyTo7Zb9zZp51sCUcAVQwgIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=IlCvjUfAFBmLg1zWWPt2p7YF1VRmiFKFzrXtog9v7YUcyJG7l939vJSi88DNd3BL_vMZqOMtcTrjApJs5nHrzlzL_Uib85wUPh7iG47x7o7NbvTu6Ai-aMkrkhCnnbMHLrOdSk1ahWgZHQ5Vy1SoJUyJj0QYGgj6IHaGA2yFZxLod2fE6dpfXZKFt_ix0fQZ0CZuhifAk6ve0n9CZSaE5N7HplG4qsC_VQxzCJ-Ah67bxDp0qs4EIi8HROI3ZXUBJ4dag3p6hjLuszd1-TgZURRg5W5__z-TXJjy1_uWeMZsWtA0-2QZzKSUin07GZyTo7Zb9zZp51sCUcAVQwgIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMTx5dkGl32RMhG-1Hg_CtPAzpfVN27SicsOysr20M_aNLCquCTAtN-gFSbLC-onlxVwNmJMrlK0xifEzyk2wsUcaZW0pUF5FTYD0dJeuty-EFwUlZw5PYG9eQ6oyuaCWjKTQ9tOF4xI8uVayMzIWJhXhpZVLc3Zgi0V1mtIuxuGNfkk3n2KFE5zQBIix0FYskm02ZBXZ4FHoogqjFTyyp8KW2riGk3IG3Q6J98oEE0zNPingE_KCVaCHOXuCMLV4YEta8rNetg-zCZ18LGrjZPGH-NrrFfxsBJlvjhpVY46okXIEx12oo17GXcpQYvzP67av4_q4eoNs3lJ5O83Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=tNU5uEPzoKYo-rrTKMF01kX7H1CATupCxPqAqeJjAWYQiko8IlcNMalrEX0yuOcyeNsf1RRMzUJu0ecZnTa4mmD_ZYwzONb-VAN-IirexBaCu1yzSQBSiPhScGYvyzGE_rjEmmnoMgewxQNiyDTecxkj_PL-3P26UNhbeqbcpAYhG2DHuc8CJS10lrbfEIpMIYnctv5DnE2VTXUSLKqxdqqyvsgSeilk8lLCW2FZ7MC_lkXJOljtGCwvvBYD8NEuo5M47uDsuTM9AQn1i6NSQjw_ep3r-UN53Lw1SKRRqA1YRFKgcaEGZ5mb7WyCfZRAqEp19v_C2IrHEhIU8WiXcYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=tNU5uEPzoKYo-rrTKMF01kX7H1CATupCxPqAqeJjAWYQiko8IlcNMalrEX0yuOcyeNsf1RRMzUJu0ecZnTa4mmD_ZYwzONb-VAN-IirexBaCu1yzSQBSiPhScGYvyzGE_rjEmmnoMgewxQNiyDTecxkj_PL-3P26UNhbeqbcpAYhG2DHuc8CJS10lrbfEIpMIYnctv5DnE2VTXUSLKqxdqqyvsgSeilk8lLCW2FZ7MC_lkXJOljtGCwvvBYD8NEuo5M47uDsuTM9AQn1i6NSQjw_ep3r-UN53Lw1SKRRqA1YRFKgcaEGZ5mb7WyCfZRAqEp19v_C2IrHEhIU8WiXcYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGDYdVfLT2yjxfrmqpU3DMHcE56lmQ4Mld9YSZbGVAIVUtXMrU8ZVIFHU9d4hVRalJIzgI9QwyDmxKzNbc3uksUYLSZUC3ZFuQB7CNKWcpA-__ZT4CidkjrGi88IY2s-qodYOScUyejpnkGisClSI7MwwXW1tHeAi6hDyoHQM2azpN0uHPKMMlZRbYwePfI35esvvmvEFIpC_jKSy2rb8ezcHOaXSwgRHqzUlF7ZRX44do5uAQ-XGaOU81xnSQscg7rHtmw3qv_VicMLhhiS3Ye5N6lxDd72wv7RgxAUfvFtaJRbmKy1J4FAZxX8p3WAmJMZoCb-SiaBio44sTsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn9dKMR5fvO-ZWasFVV_OK6igM-n0w6wX1OpSzI48_9QIoIen65pjxBjJiihTePxpwbPVveeVwqyzIclJCOUX19f0pfVQrGJHKFk06NJmFAushBiClWeu671ijcb71tHvXBQ6jaQLNjMj0fDr1e0BL8pLnZAkpJqCQzSMkAyTcnoDFD2tlvRx61mpk2g3oGl6m9q9M9d5GP6Tppno5BujExI3MJjjqpXhasILhUE_fwtg08Z28UNSM6i7p2Etp8fmI2MFt_ExcRu_hl2GHUt4No43rRpWPZKVzxJFTKBsbIF_RdTzSNdI_DYZb1WDSUFItlLmUfi177tELCd-l7ElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_hUx6gbujC3qprdCt_6yC_b_CSMG6P-1sFP4dQpKW1CBMD5UtFXrQvNYkIg3MaHL9_pfH6lyMvxH0bVbgf3ajT6Nnz4tEwxeMaimbWGiw6NEoaqMJTG2ongqb1lFDn2PwUu8X3G7NKJDBHCSxUnCdiFCgIZuvGQKtPvWQJsTvhOdDL08GL4lRtnPP9x50JaheMvmkr4vJhsO5KBqWtbZf0MVoRB429qaoOKVHm_zKn0D6Avy_wa6-rCzMs9bUK5Z7XbA_b5CWvZ_ybXEYc1avItcosduJkz1eTk6f7Xaq0dw7szeOmaqSIlVqCrwW0J2Qt5BbElHSHnmR6nVXjSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpDfhuwUVA7D_vukw--punel5VYWFSWuPlGiBExSYEj--tTFv4eUzPBUX0LQiX_fcPh8G6V9z2nEac9WJzaC-FmE6hFPbLv43Yiz958Qjro4DN7VGFAjTLJh_m8JyODFYYmxAs7Ndio3phyQMKwfIaVFo0lPOpakaRQHWbniwzOfmhex0vrgFyLGvu78C3MAiXupDtA3e6yVXnIQBemQInE5mcqzH3YzNUVZD_CDhL8rHsNCw5YvKr_1CHbf5ul3PDzMktrqT8yKnXB1auS38vTfuLTb8DhGMTPAl9U3pCZCAGfh6NTHF8O5OxL_cAKFcZvZo6m3fU6jmjZQZDl0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfKoV0gTyaCZcUulO6eoMt__181eK1aDzHb7BK9cGQS99Dg907jlT9LXBT2HG0ku32WOusIa_Pj6dOzPabVq0SfCCFquY8ER9KrYh324K6YBX5lYyOKj1HW1lWw_7FEn0AMO4JDzgK7cl5GEUfqMbOGfeVT950G2Psl81WBmNQKy46XVCzBREiCoZfDQ6MmCBPATf_YeGfNcCo6ZvsTK47L9NQG_udQkI37tJ58L1Dk1963XZFgpe1B43bixT7i3WLbQ3efeJBeJlNkR4GhgNJoudo35qIxr7QOSJTo3tdK_D9i6QF-1ZxU09Fig_NlegPDytC2Gz2ULTFlUicMwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=IHrIS2j9oi-GDX6x7kQMPO2zOsrv_dA8E1Nta0ZMkxTIVFFQB-sO-CjlMFIfoiyXS67LUuRmbeNzkkJh2lmxs3X-zhzchkngVYq501P5lGN4WDYFbqCqQDCCbFfoYJuVWvv5iQmc5eE8NOFqADL6sIGUgfF57pfRWxXDZzhaO7lzKGbyCz2Uw_nFaCFeSDQ90nmJLG-AjfkcB2eOXhbvO9XFCT8724TxT4qPlBPNfeGMUSTZAf-86xi_4aZmeEjsnmMmrMKgwO_d0dSmd61hFSJgWitr3Wn8NZw1kWpLl05E4JikLgZKb6fYeFH0gOiNxguEu2nWp6n_VDD80F4LqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=IHrIS2j9oi-GDX6x7kQMPO2zOsrv_dA8E1Nta0ZMkxTIVFFQB-sO-CjlMFIfoiyXS67LUuRmbeNzkkJh2lmxs3X-zhzchkngVYq501P5lGN4WDYFbqCqQDCCbFfoYJuVWvv5iQmc5eE8NOFqADL6sIGUgfF57pfRWxXDZzhaO7lzKGbyCz2Uw_nFaCFeSDQ90nmJLG-AjfkcB2eOXhbvO9XFCT8724TxT4qPlBPNfeGMUSTZAf-86xi_4aZmeEjsnmMmrMKgwO_d0dSmd61hFSJgWitr3Wn8NZw1kWpLl05E4JikLgZKb6fYeFH0gOiNxguEu2nWp6n_VDD80F4LqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5e6gqbtaiqMLDiAyunn8kGz9PU50p1SfNlg_8YwUXnAziW7g5Lp7WuEV5a9co26Z1tjMHKfOd-jvlLsX8k-g9ROoEIsGtRNc8Lf83BK5pGAMM5BjkAYVVc56kJcvr6IuD5E8uZuuhLcs32NzfDixg3y5JIWR4Wa_dsb817afol8ynVHpT446yvtiN5t3dmmIpcgmITUX8IlNT7DC3coSXOIowRxQ6s5-Z6deNba7QHPuacfbzo5xMwFImI4EegyokZOGZs4S7x5pZK9_0PgJ33_0M3hNeKd44zIQrwHj0SqAvil4VCQxf2oNAvbm3b-c2hApfwDttlBIIRhs4SVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTHIgkHMBtosxPvZiC3SVLcM4JjB-s1SDYb-XL-Ut7EOn7x75dLWeHsHWUiGWxgqIoJZMiuAbduDLB1Q2J985B2rW8Mdk-vNnCPkRGMBU8jZDKPeLPvKCqYs9qHetJNk9rJXT42fqdTTsZrhVyu_wadx2ZjeLwGxzXVxP5EVVOU2UbWvCnRwJTjNKaDhuGdRRrH7hjLv37_aZBIT7ipigvoYTU9BOoOJA1-K1Bd_fuFDItzT8RkC3kazTAZrQpsMtZrSA7YjU7huf9dSGPJvhn0373xlQtfz3NDETvkfeHGVkTTGxPC9bD_t1zg3m4vSNZkUZyNUxh1aG9gL88yrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=H4d63gkI9nhPoRMcMuhXuFWKketIErpk3CwsBSTLA9z2SFgJsWpSkIjnaFwlRiDwCxwAXaPzDppg32LufJxdsFYcrbVnIaPFDtn6uXK0XKD3fRl9ycuKCU75c8M02hiMdqxyfuRpy18p_sPIipygo90DaYZFboCreY-Kaxcoloqw8ym8F62ymKRkbTywm-3Va_XHNUpySqai4RYHi_ov4N4oMQ0edxe2Yn5wRWtqDW5YUkHHTWDWlG-hqDOD4cnbjK27gUdkMCABwDnkN_frdKZ0sADyvXZzbkXaItkk-sXkjr0fkDb2-z0NRyZ1A-ecGkVnxudOuqJf4XX4ReVKPwStqhkLix0zBJtFq1sTgD9UoqRjYUuDaD7EgmJyRZe_kF314bIXJPaIEdUMarKf1RkIf-I5gJevWH0DlddZl8o4hkMTtS8Dxh4jMeyf9I48n2I0VRSPjwsMwfZt_Qc0OalZ-QEMW04vAwQJo8WFizWXssfrskF7dAma9fieR985bvOhapekrsI_1EiVi5ZKyq6ibUE-OgHGNcHf0if__XC_BetnXxukuYGOdLRXZPbKfVKKJY8DEbhfFse4mFKJd-GzVGy8-R2bOb8Xufn6C4wDafCCiv0w-z4oMttp0UuS3PYD2XVAgFOK_fPcL8WisKZOScikcR_iDcyJZn0_83s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=H4d63gkI9nhPoRMcMuhXuFWKketIErpk3CwsBSTLA9z2SFgJsWpSkIjnaFwlRiDwCxwAXaPzDppg32LufJxdsFYcrbVnIaPFDtn6uXK0XKD3fRl9ycuKCU75c8M02hiMdqxyfuRpy18p_sPIipygo90DaYZFboCreY-Kaxcoloqw8ym8F62ymKRkbTywm-3Va_XHNUpySqai4RYHi_ov4N4oMQ0edxe2Yn5wRWtqDW5YUkHHTWDWlG-hqDOD4cnbjK27gUdkMCABwDnkN_frdKZ0sADyvXZzbkXaItkk-sXkjr0fkDb2-z0NRyZ1A-ecGkVnxudOuqJf4XX4ReVKPwStqhkLix0zBJtFq1sTgD9UoqRjYUuDaD7EgmJyRZe_kF314bIXJPaIEdUMarKf1RkIf-I5gJevWH0DlddZl8o4hkMTtS8Dxh4jMeyf9I48n2I0VRSPjwsMwfZt_Qc0OalZ-QEMW04vAwQJo8WFizWXssfrskF7dAma9fieR985bvOhapekrsI_1EiVi5ZKyq6ibUE-OgHGNcHf0if__XC_BetnXxukuYGOdLRXZPbKfVKKJY8DEbhfFse4mFKJd-GzVGy8-R2bOb8Xufn6C4wDafCCiv0w-z4oMttp0UuS3PYD2XVAgFOK_fPcL8WisKZOScikcR_iDcyJZn0_83s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=kdfB3218iGTvmwxdAfP6cGUS78O2qKKww2zX1UQPR5y5_BKnMpHptnjsuXJ14oSsHRX3-W-FvxsEWgdzhjVkxx80ZIanGMIq86Sm2qz7GEQDXyohJ6tpYXCUlhgacpL5mWBKeMzhJ-3uziTC2HzSSFCfu4jDG8GFPqYj3m5qP27-nuHBdSz5OPonhk8V9xUB5x_r6CV6xSe4xnpqbx-Oobv-Xhfwcbjgt86Zn6O-EvzjuJ5usHwKoeclSOFaD8_lLIXkFbgAtg8YYJFpA6toC9d0WuM3-2f1PXcnXGMHSpmvShmzG2Epph_M0GZLqZHMOnB5_6zmrnenPkuGoY_IyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=kdfB3218iGTvmwxdAfP6cGUS78O2qKKww2zX1UQPR5y5_BKnMpHptnjsuXJ14oSsHRX3-W-FvxsEWgdzhjVkxx80ZIanGMIq86Sm2qz7GEQDXyohJ6tpYXCUlhgacpL5mWBKeMzhJ-3uziTC2HzSSFCfu4jDG8GFPqYj3m5qP27-nuHBdSz5OPonhk8V9xUB5x_r6CV6xSe4xnpqbx-Oobv-Xhfwcbjgt86Zn6O-EvzjuJ5usHwKoeclSOFaD8_lLIXkFbgAtg8YYJFpA6toC9d0WuM3-2f1PXcnXGMHSpmvShmzG2Epph_M0GZLqZHMOnB5_6zmrnenPkuGoY_IyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCg2RZM4JwyljBxvTbfWEWzF3oUIZwfZ56iH8MUFLB78LydM6_BK6JZYTt3M9MiVNs_kmlD9pibHOxlujZjQ1zZrlZH6WpU0LCTN4kbkqJk1RQyrfw9DvHO1n3ZlIvlevIvOhzhK9r44QOchXrLCVRjJ9rdNDg4We6WmxpujBvQXOJnQIKi7nG2Q1y3psNBoJ0VeJyvwDhzUwIJMymC0PsmltW28BHoki3QEKpSyCln6MNWVi5RJz8YY40iAHLvpHNfBXmOGnLOQu1FDvx9U-fYo5eoVrx5djtQcMFLefYSiqu-wpGTyNeAherU0zrFPk_m7bizawIxZPWYyZ4y0JG3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCg2RZM4JwyljBxvTbfWEWzF3oUIZwfZ56iH8MUFLB78LydM6_BK6JZYTt3M9MiVNs_kmlD9pibHOxlujZjQ1zZrlZH6WpU0LCTN4kbkqJk1RQyrfw9DvHO1n3ZlIvlevIvOhzhK9r44QOchXrLCVRjJ9rdNDg4We6WmxpujBvQXOJnQIKi7nG2Q1y3psNBoJ0VeJyvwDhzUwIJMymC0PsmltW28BHoki3QEKpSyCln6MNWVi5RJz8YY40iAHLvpHNfBXmOGnLOQu1FDvx9U-fYo5eoVrx5djtQcMFLefYSiqu-wpGTyNeAherU0zrFPk_m7bizawIxZPWYyZ4y0JG3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrTpA85K93epxEn1VNYDgPZtffQk-r22KwWLMmcoLHZQtxw6IqwVlhKqt16GBvukN4tBcfyk-IM47abMoLau1id-pqCmYytzhVJcVgkr7_6Bc7Dz9cOdqXk5aEY1IC-FUbPIE-O-hLvpYs53G8D518npAdseAlXmZb5q8mWRE5p0r2-06yJzkR8gvBHBDRKmRSlNKYwWxkSbYx-ZBPw6vMh3XiJa6Aiu1mlve1JyTOF3BTdS1Y3iPVD-y9G1nuMIgQMxfys-Beld10h2ZzCvbDodelGqsLgauGRJifmN-psTps8NJfJgt2w2QSfOf9jkjzsYPOSfg7g73pWmpEvHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ_M8iKhdch2TCV7bXh-FWxys2Pq-KalBT49OfDfFJS1GnZ9_NtmEMzunFxjXgDmHdq2qwXruQ8no836zzg-dIdr_ypNbfMN5BMQtoJKjTc1duNKaikyN_Owm1P7Dsu81pV1QncJqEKo-uuTBNjLeI6R7tGtzShNb8SbnG7zejw6ckkiR054ZVuxt1BLDhJDhbKBYbN2Z5dPbanH6f1170lJXH5gxJCEJ4C08tZMjGGsgjL52jJW4YbiYxTxujRYNjz_iU4T5X0DtHQ5ybXVirTM9bGjr8WgBTeFCr0yi7M1AV4FAzimeaDpaEbArt9UqAn5JuDowjTZ4JZgKT3Z-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7tz3XFTH2NQPWvBhcK235vIro9DWlfMmHzN4V8vqH-XKA3WsF7t-erlCWkngLJfOgBRSCqVr9cljy9oSL7zUbZDSxgni6zVo9uxYCAgJUr24qiHIr1EGTdMKxpnWXOqijmTQD_QF0wNKOLVe5oV20_QqkH1dvTYoN1HJCTsq9AgKs1tuNrp2g0JGkaKeH3ONeYGC6TGiFk38DPoYs4KVcEHJhivMwcPiyIPTZNKxl_w3oKYZdY6zM-mSkfry97e_axG5zclxHWnW63MZsq0zhaiTkAa0JwriTsF30epsQw3FiM3UrUMK3foiKzutMMfpkg55djUGU3cwxBSB3LCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=LE7jmReUmw1dypkJxy1uMWVQWWRr0me8oLdiWvIZuu1cHGxtLV3pNqvrf2ibEccNSP4FqKutZqbaBk3HfX0cQYjT7RT8YG5h2IABK9Iy2SJKYpepc0uUUAZvRBgcUDTzr4r1W8EDUDktFb0ua2ToMC_e6Y2aUn25eHP2VmRy5ayVfK7xbziNCguKBPzMpFTlLmIGvPo0bAfsZXrJv4q-KEIxqG_tBwydZOinLweRc04cKXN4-jNGEa47hwWavS44-KTIDfzVMiPJv-ucMkHEN29tyZcNYE5Gt8jHZr_ebACo8xbv4YSpj_lXXQGEG3_V3nTbByaKyDm9mZhQ7mWBMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=LE7jmReUmw1dypkJxy1uMWVQWWRr0me8oLdiWvIZuu1cHGxtLV3pNqvrf2ibEccNSP4FqKutZqbaBk3HfX0cQYjT7RT8YG5h2IABK9Iy2SJKYpepc0uUUAZvRBgcUDTzr4r1W8EDUDktFb0ua2ToMC_e6Y2aUn25eHP2VmRy5ayVfK7xbziNCguKBPzMpFTlLmIGvPo0bAfsZXrJv4q-KEIxqG_tBwydZOinLweRc04cKXN4-jNGEa47hwWavS44-KTIDfzVMiPJv-ucMkHEN29tyZcNYE5Gt8jHZr_ebACo8xbv4YSpj_lXXQGEG3_V3nTbByaKyDm9mZhQ7mWBMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwnNfGM8izv7gE3GZjfAh1LZ_Qh10lnOXy741zMwkrXNPnFJhJ92SJzw7czc98kEo9wWjinmyfkXE5oUtDDsYlk8vYI2vwJoXp6gWkuMh3V9yog0qvJ9YcmTqT2_krSMV1dTzckT9_sL48th5nvGkVADSbPz-Hn1wEBZn0Sc_Csih-ir6ww83xZjryL2ooLANoAdwOb5ig89N_ZAqR9XWEEBu4fagAsJmHyi-sDHCPGXXHXbPoOVv4uGBSJWqstlknqOY661YRpirPYxwm__tGazRvPHHgFAG9LQ36aY57zBAVM3eetRUIig5gtnOesKR5If-M0pmzQvxG1tT_Z5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pchqpWxtiBmxeHOF_uYbB5NjsxRIUJjp3tQivLdh0lhbXtcyBOBHFgdh5Mn7JgxG7NVm0oWO_Qb2VlESWBOXgVNyjfj_7AdVhiTbVQoTn3tShmTfPfUY_Vv_3QHznB0mMwmhJ0KK14MI2X7MzHR5FIzMMQ1oRbjxPBIXIg3D-KNhqe-0N86V0NGaKLHMga9Jx9YIc8VSvXC3N8V5r52yrx6tdvZBB0WqdHZ0KuzI8YUwNNQULVzC_o7uyl57bvfmR_gc28SHooedefx747DGQnFOvBAjc1QgJn8yV5lZRG59TGRYzrgiagqx3-3S6W4KOvGkt9Gw5j35Kd1ncJMX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gotgkaird9-que74b9HClGHOoPIJ9xfmWzY7CVx1jvZPK7kWmsNW9BvePbKG6RG7eA-Si6901J_sTKmtG-pVAawPYZxeg9tqv_crInMbF0Asm8TfSK6jemt-N6oDPdT8aONWZt_slkGsYRlUoRtT6fpTQM3VSwOVyhIEIYaUvxKlsOdFcUPcD5lxKfgO5LSx3A-oe-S4-rD1Kk8XK7b3rAaG99gQ3xdLj779-H43LQYvIS8sDwPkA2u25o3rMiSVKpPrDT26lgj841bidQrVqRiwF1ef0unjoOoK0biuRUFqprlzSA1hOyPXytHH7mIsnf3-EPbyBElyKXM7YCd9FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHJzeLrK7uWbZSOInlD_kppZaxB6df1qeJYNrrxtVf1DAGnKVAbHKsy74TXY8RJYZTEPCScMScFFrpyZVB1_NwsnleRY44UqrBLCTMKaQ4l4bTaVodUp4U4vx7IKpveTN4ms7VWASCc6L18nJL-7vfPGfuNRYi-SDgDauo9txj1Zi7LhjcjGxXwVYptc-DztSosA7ozNLCTB59NyA9ltiBat8eD3reTEy9Q7FzhKA2qigWag_WTlCaBtw6cOE62zz_j34pCR4LmKgJFWpF7tsmgx8mpv_EjBlXNgKxUBgukYy18qxVP_TNQRBjrAbCyVHBkKBPu-uVrlutVbPfKKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=NT0-9aCv7XJ2qGIdF2NVOHc1DUB4bjbbD75Ps8q2phQ_pEE4WBSUTGjv25T9qMBWGpM2tpCEeV_3l_i31CFje7Oq1HseSn0q1eXF_YwPL1GgeBfBUSEPq9Qc9PizgiwvtYwpJKKaD8yrsPsf_7P9h3FTYi2Ify0hTUFPx8D51LmjTQnzzdW0jzht_hJbx5KtuaOUP-UIx1inpyU78Q5Fwvhdp-WEdByA5xwb6IRljXsYyvhPIsso4d6lBl4KJC4HfnGJ8zN0E5XAydlj_vWDt1pqhWMxhuJi-0mD9DddK8581B1JhHAqNq7GjwP---JG7peOs_uy93YerlCVAXmBxoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=NT0-9aCv7XJ2qGIdF2NVOHc1DUB4bjbbD75Ps8q2phQ_pEE4WBSUTGjv25T9qMBWGpM2tpCEeV_3l_i31CFje7Oq1HseSn0q1eXF_YwPL1GgeBfBUSEPq9Qc9PizgiwvtYwpJKKaD8yrsPsf_7P9h3FTYi2Ify0hTUFPx8D51LmjTQnzzdW0jzht_hJbx5KtuaOUP-UIx1inpyU78Q5Fwvhdp-WEdByA5xwb6IRljXsYyvhPIsso4d6lBl4KJC4HfnGJ8zN0E5XAydlj_vWDt1pqhWMxhuJi-0mD9DddK8581B1JhHAqNq7GjwP---JG7peOs_uy93YerlCVAXmBxoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=QFJE-A_EuhwjKbC6VMAVEzU1NuFKMEnyEb9NKV3QRNI7aLRxQaqH-62x8wGIvhPJRlkPMI8wZ3Oul6XsQXjISn7NvpZGkcr3wuNGnYJZZHA69mpQrheUrFwA7-8R9ngTCXbpNyryYr2uKlCfXaorrxRQ9TZumjbhe40AtnpZolEol3wCjdVWXknxXGUkE7WqqrkFLlutp4T8htaQ6yeF7nv_W1jiDzhp_OFRC6U0lAmUS-t73deC4_nMyIHYzzcf9JmC90OIFEudGCfgcA3rBu3LtkgMyx1TqjfY1pNYl8unRUTrEL9AmF0XWzw-oZ323JsLdMYP_TNxbEdUG9-P8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=QFJE-A_EuhwjKbC6VMAVEzU1NuFKMEnyEb9NKV3QRNI7aLRxQaqH-62x8wGIvhPJRlkPMI8wZ3Oul6XsQXjISn7NvpZGkcr3wuNGnYJZZHA69mpQrheUrFwA7-8R9ngTCXbpNyryYr2uKlCfXaorrxRQ9TZumjbhe40AtnpZolEol3wCjdVWXknxXGUkE7WqqrkFLlutp4T8htaQ6yeF7nv_W1jiDzhp_OFRC6U0lAmUS-t73deC4_nMyIHYzzcf9JmC90OIFEudGCfgcA3rBu3LtkgMyx1TqjfY1pNYl8unRUTrEL9AmF0XWzw-oZ323JsLdMYP_TNxbEdUG9-P8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=Lor15uFnI99N1QsN5xn7yN8BuAJTkG9-56W5TDaJdbRgUViEYbfD-_RT-l7NSZafneu6LtRTSxtpevCVOSmoy58Wqc5_y8bhcOTD_zhC4nwFqu0CvLHM5a-GIc7yW1AmSFofRpEg0Bi0ee7k6yM3jp-PYUOmt6VSrAfmhavDlkbSIv-NljQ3HKzPzBScMAD_1MjfKgL7ykDfGbhpHjnUTGhnaKB1-H3_zZ5ohKDswtZSRmVPmXPVxU3LrK4T8w_lUDGnCsJiL9mPcaW9azSU9koS4YqLFMdhXZ6Hn4j-LEFGDd9TSNMS1IBG4hPz4pp91_kwJ_nGO0Gda2sVBDbw-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=Lor15uFnI99N1QsN5xn7yN8BuAJTkG9-56W5TDaJdbRgUViEYbfD-_RT-l7NSZafneu6LtRTSxtpevCVOSmoy58Wqc5_y8bhcOTD_zhC4nwFqu0CvLHM5a-GIc7yW1AmSFofRpEg0Bi0ee7k6yM3jp-PYUOmt6VSrAfmhavDlkbSIv-NljQ3HKzPzBScMAD_1MjfKgL7ykDfGbhpHjnUTGhnaKB1-H3_zZ5ohKDswtZSRmVPmXPVxU3LrK4T8w_lUDGnCsJiL9mPcaW9azSU9koS4YqLFMdhXZ6Hn4j-LEFGDd9TSNMS1IBG4hPz4pp91_kwJ_nGO0Gda2sVBDbw-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYgzhmkx-ZmWQpljDbWAVb4xwMgFsVgNrffFF8bj1eOrFU7vVbTzRD-JYzebkreNm8LUJREFDS6KnSqCD0NyQCQSCRiamUeMbhAOcxZn_3fGGRiCAoOL81hdGnNz06wYXpQDmLSEeZjcmq2IOolEv8FpS7C6z-qGND7MBSWsbe8GmwhMIdY-eFELwnZHdc7zWwJUju0jZVl1edLaF_2f635Nn6CIVMdc_iTIKYFBXjBlNRMokM_p60D7u-OHnBtVQv_DbqVFD748-aqWoCd5CFJY-Qo0ivkij-YCsHf9ON6LWeFnS6KiUI3Uer2-tlDxunxw70FZeVoEnvboqMJfUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=ptpSpnwsJXhstrBUj6Jph86qlCagmCISjvgGOKPp6eW7byfIlq0wWHTn4mTFaVtHkeWf9qEH_L829LzAJ6QbSkCP-c1o2HeP8XRHpabAbORfkLFGJ_R9xbTDr_jheLKbbaCZFM0WFwft2izhOhrBP1ICL1Sf5pEm-p1a2dhcodXVHq5uvfN5BHwXQegSDUT20gH1a1YQ5MLfUW03zDDN33JvZAEEUmbpvtaGhwEbrlhvMmIc4heMXrGGYbD9GuLlorfGYfhAn-sc1uA6pPf8FC7P2vZOqsyGTkg43slebiyZIL3CeKqY4JhYSc58ljNNKGy4aiy53DO0-efL5J-jJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=ptpSpnwsJXhstrBUj6Jph86qlCagmCISjvgGOKPp6eW7byfIlq0wWHTn4mTFaVtHkeWf9qEH_L829LzAJ6QbSkCP-c1o2HeP8XRHpabAbORfkLFGJ_R9xbTDr_jheLKbbaCZFM0WFwft2izhOhrBP1ICL1Sf5pEm-p1a2dhcodXVHq5uvfN5BHwXQegSDUT20gH1a1YQ5MLfUW03zDDN33JvZAEEUmbpvtaGhwEbrlhvMmIc4heMXrGGYbD9GuLlorfGYfhAn-sc1uA6pPf8FC7P2vZOqsyGTkg43slebiyZIL3CeKqY4JhYSc58ljNNKGy4aiy53DO0-efL5J-jJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=t3ZvwJTIDosVAmNrNhGXpX_a0n85rW2L9sGLcrNZ-zDvId6gRADC6Ea2Lku5ZGTgFl68jdU0pEajT_oKAZkuxbheQsrlBLyX5IaK58fIwIqOLumKpxdMVR2OHiCYCJYcsG2MMgAOtxIJd3uZJGYe0xnze-SR-Y0q2-y0bk98XwCjTZUVJg060SfgxKRyaeHtPcm43W--nKCnAGpmYoIzql2A2YPqgtK4f31j8zMg-H56kMOFz0GVOgngZfYrAnKxwWUhdX_VKoV8nFgelXfv-bcA8_ibRjfKHNO8liOYrzmWL0jhiuQWLrqTSKO4Fe5Kk7TVePx2w7vRG1wHbWi0_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=t3ZvwJTIDosVAmNrNhGXpX_a0n85rW2L9sGLcrNZ-zDvId6gRADC6Ea2Lku5ZGTgFl68jdU0pEajT_oKAZkuxbheQsrlBLyX5IaK58fIwIqOLumKpxdMVR2OHiCYCJYcsG2MMgAOtxIJd3uZJGYe0xnze-SR-Y0q2-y0bk98XwCjTZUVJg060SfgxKRyaeHtPcm43W--nKCnAGpmYoIzql2A2YPqgtK4f31j8zMg-H56kMOFz0GVOgngZfYrAnKxwWUhdX_VKoV8nFgelXfv-bcA8_ibRjfKHNO8liOYrzmWL0jhiuQWLrqTSKO4Fe5Kk7TVePx2w7vRG1wHbWi0_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=sXqJVWcjFZCcQ_u7q7YPGJ1L20d3viANSdbsd3yQ41oxmMs_vg6iNvn2rQwsOgSbYzceNEMflod_coJlHavpDIv2AE5vWfvDdaQTN0_hHrQbXnUvvuyIDuNzVGm9AzOT4hNvEv3jC_eskrDlCwjiVwZhOOmC4KBgwql0JgSl5utKjwTDP1vMZ15t86YSvnCkZTdg7Ls-MlucgNCozOeGc1QwaJJlVSk4GsrmirYcPb1UY9QLAZfqr7J22BuxEXsZSWwgGzigG9u54Zq6j7qZO39M99TRfgb2kB7T25MR3zTr7b1PX115WpGpfLxqF6hKq70PmUq2NSHJ--BVfUz5ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=sXqJVWcjFZCcQ_u7q7YPGJ1L20d3viANSdbsd3yQ41oxmMs_vg6iNvn2rQwsOgSbYzceNEMflod_coJlHavpDIv2AE5vWfvDdaQTN0_hHrQbXnUvvuyIDuNzVGm9AzOT4hNvEv3jC_eskrDlCwjiVwZhOOmC4KBgwql0JgSl5utKjwTDP1vMZ15t86YSvnCkZTdg7Ls-MlucgNCozOeGc1QwaJJlVSk4GsrmirYcPb1UY9QLAZfqr7J22BuxEXsZSWwgGzigG9u54Zq6j7qZO39M99TRfgb2kB7T25MR3zTr7b1PX115WpGpfLxqF6hKq70PmUq2NSHJ--BVfUz5ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Ga079pVs29j4uJOXKcWNO2yT-zbVY9VNxNLGVaZjCpknIP5xz_EiWH3_SzAGwzmgPUaa2EwTXmS_SEKWrmLm8DPgmfWdjLtAsRfkMNEDwiNRltUtTew6dh_ap5B_joh0O9EiFrtnkpYZSGg8s2ZFtrKgG4m-Gw3uDcgnUuHQ0FSiQHozmruOHlqQYXtWMtHTDXRnmLLokMwKYrcyNSnXJf0ynM1EnBtgdm0b2y5voKcQ5Xk9SkqYDA0yo76TEpX9VsjnKFG-eOHbRiBprVSGrelYcNzOuS3hM91Hve7xihvYrp8U3R66-SgtUGN9mbRAuxNUr2jB7p_SjzBc9zhfebZrWsk6ry7B2cxFYNtqH47gM_aMj55uxqttLthtVDoYmp8-ZJZpbY49YBtIHjTVBf5nyiitdd4oNap1LpceKRtf5CqA7xXD3EltsQw0g52c--YQibbZUeJHY6_LzLoz03pf-eh8nbu_DX6AnS-S7v1J5TjhP5ZZ8P_caiSOyDjwHcwJ_DKzFUhfUTA0TF4UzAwon9algOw_o8qsAtDfRfaiVDKhestLiwd668kt4IUfhNEsXEYnYWnRYi3rsMCW3teHXCLOWpMyDJ9s8pHCVVRH0lDRcRw6XgAzW_hNcw57VspTcocjKpVc0ASfcJt6Ax4N0w_ZNthqOaRCP-aLzTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Ga079pVs29j4uJOXKcWNO2yT-zbVY9VNxNLGVaZjCpknIP5xz_EiWH3_SzAGwzmgPUaa2EwTXmS_SEKWrmLm8DPgmfWdjLtAsRfkMNEDwiNRltUtTew6dh_ap5B_joh0O9EiFrtnkpYZSGg8s2ZFtrKgG4m-Gw3uDcgnUuHQ0FSiQHozmruOHlqQYXtWMtHTDXRnmLLokMwKYrcyNSnXJf0ynM1EnBtgdm0b2y5voKcQ5Xk9SkqYDA0yo76TEpX9VsjnKFG-eOHbRiBprVSGrelYcNzOuS3hM91Hve7xihvYrp8U3R66-SgtUGN9mbRAuxNUr2jB7p_SjzBc9zhfebZrWsk6ry7B2cxFYNtqH47gM_aMj55uxqttLthtVDoYmp8-ZJZpbY49YBtIHjTVBf5nyiitdd4oNap1LpceKRtf5CqA7xXD3EltsQw0g52c--YQibbZUeJHY6_LzLoz03pf-eh8nbu_DX6AnS-S7v1J5TjhP5ZZ8P_caiSOyDjwHcwJ_DKzFUhfUTA0TF4UzAwon9algOw_o8qsAtDfRfaiVDKhestLiwd668kt4IUfhNEsXEYnYWnRYi3rsMCW3teHXCLOWpMyDJ9s8pHCVVRH0lDRcRw6XgAzW_hNcw57VspTcocjKpVc0ASfcJt6Ax4N0w_ZNthqOaRCP-aLzTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=oCFOCoC40P7McRsIeGD4_fBQzoN8eQ8klTVPObJRO60rhHSKuuuC0hDNS3Pd46Ij8msNDs326GGEqRnNTiJqD8X509t8isroxfNFzlOzCErZwlO1nA_z4dC2nR6v-ATOjQ7UkCgvNGWTGFwdlox0Q_K3KExRklF_jPbDgEb3TtJy2Epl93TK30J-24w9pYN92WvNfD5HXoZaQ2EJ9xavNG2h4xlL2IcOJg4hO-mxhvXuA9BnlVI1MXW1ZAOKmK0zUfyQH3dINP6K0QUdBX_csmhYhcDlpNp2ufX-eDRhiux03Uu9ghnZFMTq_0asZE766OQOfpY9AxZUQnT0eeBWiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=oCFOCoC40P7McRsIeGD4_fBQzoN8eQ8klTVPObJRO60rhHSKuuuC0hDNS3Pd46Ij8msNDs326GGEqRnNTiJqD8X509t8isroxfNFzlOzCErZwlO1nA_z4dC2nR6v-ATOjQ7UkCgvNGWTGFwdlox0Q_K3KExRklF_jPbDgEb3TtJy2Epl93TK30J-24w9pYN92WvNfD5HXoZaQ2EJ9xavNG2h4xlL2IcOJg4hO-mxhvXuA9BnlVI1MXW1ZAOKmK0zUfyQH3dINP6K0QUdBX_csmhYhcDlpNp2ufX-eDRhiux03Uu9ghnZFMTq_0asZE766OQOfpY9AxZUQnT0eeBWiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=kHGTyEW2_0xgAtlnguHnEzdIjklr53MScG9ffxd_liZ52SkJujj2bIGemF2Uan9UyNK_LkRTYuf29nKbkLNNTtYR1IJW6CcHEZr6pSeCefZ_yul9xTuTmp3IZZz3vL87qy1K5XgFjBKInj9fsIl3l1BW3Hz_rgs7g5rS_7UhiM2721n7RGfXSVYwzLuLPlbgjp-u4x4_clRyXI0olPuckIKRd0uAB_sAisqj2PYPTs0vHKMbYzcuGjBAMV_AVIpnIReILQ6xYkP-irFyvLQk4fw62MlBwD8zfdmwpuA1Z8d_Ma7xH_ESt7y5kd68BSCarDPVaUNFwMdxlnjyO9Wkfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=kHGTyEW2_0xgAtlnguHnEzdIjklr53MScG9ffxd_liZ52SkJujj2bIGemF2Uan9UyNK_LkRTYuf29nKbkLNNTtYR1IJW6CcHEZr6pSeCefZ_yul9xTuTmp3IZZz3vL87qy1K5XgFjBKInj9fsIl3l1BW3Hz_rgs7g5rS_7UhiM2721n7RGfXSVYwzLuLPlbgjp-u4x4_clRyXI0olPuckIKRd0uAB_sAisqj2PYPTs0vHKMbYzcuGjBAMV_AVIpnIReILQ6xYkP-irFyvLQk4fw62MlBwD8zfdmwpuA1Z8d_Ma7xH_ESt7y5kd68BSCarDPVaUNFwMdxlnjyO9Wkfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-IKWq1lC_FQC57XRQBL1m9UHEasbj5ixUWfSERVEoH9f4w5oWBcV3i75UsddGJGIEIBr1o8NCIKtRQdIcyY0FvtptlFTyHz75OcuCALp1u5X343-RJH0tMySFi-lgCDhTFKL0MRhhuq6rtR_kDkIK8jV-fe-A_wIyfeBjk-md0mJZSHiasr7fli5Na1ZfW0sTjD_V9C7FFt4qco-Y4ol5UQgxD2gW7eUx7tj5Vfcmj4YA3Bye1z5URfURHYgqS-c9-DDeshG5Q_ibrjPNnDJdtIhBdbjDdbco8qsgm-F-WKE_brtLi2VUV4jam4Ed_gz5wjbNfMRFri8XwN2sWlsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUsEoIoPCeFScq71p6A02HxVJlaPSR-Xw98nxfWsHFueJe7nrbZwJmiWRRDzmYasipd2N7QSHZPcwcH6VyUziRf60Tt07nUKZ9bEjQgrKVGI6X5mrLq-epH8eLgVK8XH2eQ0M9YwY7yleBD4_OLZ3KbTYnwow1VaGuHCz8uxF_K0vudIHXMvpIHfbHCI_umOHSMbA5LA6ITrKV9WFRA9Tkee6zwJZA5z6-H2XyoLlYeM31GZRCWwrLhsy7Xbr_EG5kJIEzn8wy4P0rlGbj5v1qCO4NSpxO2Bh3PfJRNL-qo97MX9dtb2FcMPknFlqtZuBu5KrIK66P1ndReXN2D1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=KA1rdmiwve-6G89xWxV2ytVdMG16r0xX5EyhVER2lusp_PglKKVa1VB1HMFms4nI2d7rePfRk_ulz4pH97HQrPzTme1YIummqtSLh6w5lf6DMsNbA64kx8ebk0BX5hWmfa5wjWUQKdqxyoZT7A9R5csWD-Z5-dE0QHat0-O3SCqiHl_neWF8CpUf_9i3774piNjLwevTFYf143fReqbHefEg5Kuf0JsN1KnZ1sRkjeI4mHjELEfFo8w4mvZ53I-pOTP9smkYxnSmH5ST3B5sZCw1cNbl4CsPBQh_rR1eEhBZs2BpinfTSGTQ50KFsuKhIjcS1wObhOnkR6E-FV1MqQlADOf7sUxgBIdDV_tvB8cE849yJ-m_VpI5BObcoM8WaS9Gkf92RadSSB4l6hQ8VMN6BY_Ga6-I0YDqILwaLk8GBc2QvKB_Sqq_RtYq2OwQs0E8oqbTROQNayTEolZ9uvkEr93Ym_SKiTic7zViKsS7-a3gkalBYkdlbRuWxFFzjLlihSDjY2pqou6R0CPt-E9ECeJCWSQMTcNZ6QxgA28Kjdnir1D-QVBDwLo-VaSbN-UJuobqAc4CPeOxXgaW5ytAoP-Ybwm0gGgY_auuorE7U-yUBTYB2GcOyV84eizQFsXXAtBrZhysnRglVAV-4s5Ov0SjoXLyvUTwUXm8-TM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=KA1rdmiwve-6G89xWxV2ytVdMG16r0xX5EyhVER2lusp_PglKKVa1VB1HMFms4nI2d7rePfRk_ulz4pH97HQrPzTme1YIummqtSLh6w5lf6DMsNbA64kx8ebk0BX5hWmfa5wjWUQKdqxyoZT7A9R5csWD-Z5-dE0QHat0-O3SCqiHl_neWF8CpUf_9i3774piNjLwevTFYf143fReqbHefEg5Kuf0JsN1KnZ1sRkjeI4mHjELEfFo8w4mvZ53I-pOTP9smkYxnSmH5ST3B5sZCw1cNbl4CsPBQh_rR1eEhBZs2BpinfTSGTQ50KFsuKhIjcS1wObhOnkR6E-FV1MqQlADOf7sUxgBIdDV_tvB8cE849yJ-m_VpI5BObcoM8WaS9Gkf92RadSSB4l6hQ8VMN6BY_Ga6-I0YDqILwaLk8GBc2QvKB_Sqq_RtYq2OwQs0E8oqbTROQNayTEolZ9uvkEr93Ym_SKiTic7zViKsS7-a3gkalBYkdlbRuWxFFzjLlihSDjY2pqou6R0CPt-E9ECeJCWSQMTcNZ6QxgA28Kjdnir1D-QVBDwLo-VaSbN-UJuobqAc4CPeOxXgaW5ytAoP-Ybwm0gGgY_auuorE7U-yUBTYB2GcOyV84eizQFsXXAtBrZhysnRglVAV-4s5Ov0SjoXLyvUTwUXm8-TM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7NV0Zmoxi0ZMAjREPXDUNhVkHJuE4o55Z97_TBXBJxB7oL-bwOlSJiuZXLavfzgj0kBetKIWS9v68IJThFDBGNnIkSnn1Y-fs9KxQWealtExKz7MLoL_VuWztWd0TOkRop_Bm6wcZkubkR27ypHP5PPe0nGCE7_0E4Z_SMEVxGb5s8BxUqN2_QIFqfrcGlOYzlxfdPzMBnFOtkn4fZhSesIIdXaF_4cbU__s-MVvvMKzMbOKEw8W2P5i-ni1h97OJ-DKHKxBM4VYFaCO9k7YvpfVTnbqAvldlOd3PLv6M2XuFAZYfwy3wnrGImL9d63__onQrWzSKBl1pjPpE99SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4I11Qz5VscgT2MF8ugKl1kEqXuMByRtR_pH5Z_SFozXwIWr3FrV8R0USw-W2z0SilqVw6n-iPfTQhYuqZ7GWLbbU1aKGftl6BxyTE_9_t1iIe4FtgKWl2VgkMaH5uIp8gI4smTfdu8-iyVOPAqCRgjcWj4QhNAzOK58vOZSoFwN1nZERCF_CLYUmv_G2Ckeo1YFnLpNJOJQ9uQ6H5hL54EExRMA4gAUsnlBP9I5ZTM0cc9-G9LuqHGDMkwN9BEIv1ndJhqmSqtlRBuxWyCZNFU2LPymMDJmRStpaqxnm2GEL0QHWMdfJXaOqAnUC8S5NT2lzwwrkRFbWVJmLLsWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDMV08icE5oPcXikdslpIbWRvUVD5fF6YdOHLU-BdP0XtV5_y2YGJikEIQIuULrOyQhwA6IYU0Qjuxr--n1CJMzCia6VpvRClUz6YVEz4aW0JBmYax2t6XUTBXhPcqIs7ns3tmsVGsidvZEhydHWD3c8H889cFCiFZxEHJJPQpq-NmiZik2PH4ztCg10eo9YKGp5YsnVkr_9c5TV01doQ1biEOTsmrsNcnSBGbVCh2y1GokhvLlp8wvAHlVJ_utR2xa_fHTS-dsAQccYW9ACXmSJmm1zpe7NgW6fCPH9sle-HdSBVqROsrEPHa4f05ax3pQbxDCLNbgUsLle88Jxcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0_EfF0ggLIbEb17w0F-i67GCKibUYhvm6qqyzAf5Ihurxc9kLQhRDoeYJMxmpv2TsYH3TrQBcnEl705CZoHBuCqTwd6vVcGnZ9l_Fu8-wgHlGqADThdgGwFHs9uUUPdPpPpWEGUnIWmMteHgZJmV_5CXIAy9nV_Oo25KEcmCTurMPvWEuyjAbRjwfdjC6ThURbelVWkRv0ImDtK44HyeFOU-pKVHFxlqBfxzWUhndnsuSohcntzWDYFQMyH7FVNg0P9Hst_313cfXzydOsgyKt5QAzDHXDlTUzzW4F9PGErmxLH51vi7iJ64JzPyK2TzLyaht17EqvuD19tno_bLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=nGfkWEnFNB7mHhgVUTz3yFIdnXzgz3EJj6dpVTqPATnjnkfmDDauKLveuXyW1VwJv0cjyl452lKgBsO3UxPd8AcmB5mfkvEs-apAUiA32jO0Qt2qVK6TVR6wzahcBecNjxauZRIvQFs6hvGNGjrkZqzhZzjrYAVDlgtry18EGscPUfL6L6Gg1N3gR-xsZLebfHK9XjVk-qgEWa4FiMBbrtsmPQxwrQq7tZxPu996rKTOo1vBxeWTMIdGbo-BvCj-WMnXntencYuzbyq0X0Lq3bixxpqfcApiOcwXgyPqXkvVH9ffmO87kQ0wgRYxsGDcg99Siyg-ykaCV2fSbJ3q9mqwjK0NJWhzidSaT9GRx9h4wdKYREq2NjDPemPtrVc0xsNMpPheSwvuGu_WOs9xu2C8R1J3vvmO-vCZSJLjZizn1l_rUyf-VtYCpaqy3tVHlw1VK_7_1fdiFMNxQZzAS2wPGX65-hvLzSwH4JhI8vCdjI52zmvROiilbuXWYGbUKN22qYyyL9Io27C2vlT3NDnGEJ5HaP4rctbDJtvjTAErbQy6OSirY0GprtdEsnIq6PHllYAziirMZMPcS3EMZvSutQHMA6vEB4G2Txw9Ha7DqM1i_SBaRbdynbVU6_97eTGiYnL6Jcaw_kt74hoHrkOzkGHc6w637gIvjuXsgs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=nGfkWEnFNB7mHhgVUTz3yFIdnXzgz3EJj6dpVTqPATnjnkfmDDauKLveuXyW1VwJv0cjyl452lKgBsO3UxPd8AcmB5mfkvEs-apAUiA32jO0Qt2qVK6TVR6wzahcBecNjxauZRIvQFs6hvGNGjrkZqzhZzjrYAVDlgtry18EGscPUfL6L6Gg1N3gR-xsZLebfHK9XjVk-qgEWa4FiMBbrtsmPQxwrQq7tZxPu996rKTOo1vBxeWTMIdGbo-BvCj-WMnXntencYuzbyq0X0Lq3bixxpqfcApiOcwXgyPqXkvVH9ffmO87kQ0wgRYxsGDcg99Siyg-ykaCV2fSbJ3q9mqwjK0NJWhzidSaT9GRx9h4wdKYREq2NjDPemPtrVc0xsNMpPheSwvuGu_WOs9xu2C8R1J3vvmO-vCZSJLjZizn1l_rUyf-VtYCpaqy3tVHlw1VK_7_1fdiFMNxQZzAS2wPGX65-hvLzSwH4JhI8vCdjI52zmvROiilbuXWYGbUKN22qYyyL9Io27C2vlT3NDnGEJ5HaP4rctbDJtvjTAErbQy6OSirY0GprtdEsnIq6PHllYAziirMZMPcS3EMZvSutQHMA6vEB4G2Txw9Ha7DqM1i_SBaRbdynbVU6_97eTGiYnL6Jcaw_kt74hoHrkOzkGHc6w637gIvjuXsgs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=oqi08djvlwBLWIkV1AQ3j_mTOjbTDpuqojBSmfTnKQSOSyFaxeoPnRC4jc-SFcKyz1FNq5cWJv3sINR1YOTZoXr7hJBA4XMDOjMkrw40xeRxzKkk26iZcSBsUoHORfV0wWi1OymTPLIX2Ue1ZqpOAUhAHbOES8RsoZxDRHVYg7S_KDbNt6DNjA9EOknZ6t1MBk3jW-Kik9HH4rCMcy6iNgLgdOB00HGerIaf6cLXZxq0yHk7kof7drB83P9nC23VDo09xtpsOSVAfxasKV7utz_5eyUraUzCmNV-hRbDNfub6am6hxu2RMJWQkk0yEf46fzMK3IMrkIn21t4fTwITw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=oqi08djvlwBLWIkV1AQ3j_mTOjbTDpuqojBSmfTnKQSOSyFaxeoPnRC4jc-SFcKyz1FNq5cWJv3sINR1YOTZoXr7hJBA4XMDOjMkrw40xeRxzKkk26iZcSBsUoHORfV0wWi1OymTPLIX2Ue1ZqpOAUhAHbOES8RsoZxDRHVYg7S_KDbNt6DNjA9EOknZ6t1MBk3jW-Kik9HH4rCMcy6iNgLgdOB00HGerIaf6cLXZxq0yHk7kof7drB83P9nC23VDo09xtpsOSVAfxasKV7utz_5eyUraUzCmNV-hRbDNfub6am6hxu2RMJWQkk0yEf46fzMK3IMrkIn21t4fTwITw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv17cS895H1MO9GzRZIppKKX90aZ9GgJ2qsIipiZC5JJ6oI_jdKGNIWYD4kIT-P3VUWSwE8aIAHNB9yfwdkCO4E9mfPOxLqsboFrnHk5FOOz76Z4avQonadwq9cG9mjLp4CfSvKvTQb8mqMzRRUYrj9VO9AQJ0sy9ZCUQ83kbbTsffAogZudPmR_Vtjr-lJokqHmmPrONcTIDySRjowX8M-OthCzb0HOoVxKjxjSfIGWGlyr0-QfkQJrj6Myj332DVDtOCV4cqVV57US1_zxscWgGox6oKzbJ3wjSjjUTD7DEDIGwaxPXi8vFXoWSDhSBm4dcyT_wE4wMhxkEkBayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM3g_n2ly5UgvcQ_rMCFxGIfk_Z-6iQUoAhr1TgPG0y7PCyF-n-7MMbHJlKpH9LYZLBjgLrFK3bXiS5V8ZaODtbpfwxrX6uZhB3Mcki2U5v6ga071e-lNpiYmgL2MyMSKkVt67ULWzRHkiEZVGfp2p7SvyR5QtULWrR46mfoWgh2XbFzE7ZVmtw3-m1lFe95myx7GCzz-hF-PRdkuRmEqAwFVB88IXzViWQ_xxJBuXoLu20cx2s0QiLoSa6yEZ0OZKdW9twTWuoqcoqNGiwjCocbuREaTiXNwZTWZbWYrs_-uiWoa-ILqa8ejiMtthg6HGf-gDqB-N_2S3YkeIoTIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqBxDZnBZU73AjRV7YLSzQNYwgScevYiyU91KqbGhRLq0QLTcYewJGXVGTF6JEza_whDFMKSkVQiHM1xZ12XcUInxA14UpqJk5XTlGNlXMxHQbQQOuByrVY3w1zmReLjcPWXszyzNCc1wAV18Gtae-XMVyyBnyplFdXf-FvffXISg6mCrDHHZwOz1o1932MCmdzABYuTtld9mCxYTRuU8yO0JT-p82XVpLgL3yWrtcVURwf4lzO5pehm7KCIvMzqzT-aLfH6JZCZz0niCXG5OYbY6D0cGiF1PWrm-UhABs7wYNvKKsrIIdBVeUBXZR33LLPy0JjvgkOtD7e9QOT2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BdDJEfrqF1c5T85FgSenL0ZDsup6YEF_ceWUNEDNxQvv81U7XxS5l8MedHMaw5bVDvIaKgJ-i8_dAdZIhdg0rXFJZLr_zzJAp-xG4e_pU2hlIsmg1J3DhY-DVZI3ufTRhaQDem5IawFCzdzW5GVnJrO-_5-G33iEpPVf5l0OSnND4GExkWohDvL1S5y5qHtHzn3oRNiSFKLNLaldbxAc0SfvUZjpfoTs0IRVO-75Xzs3NM2T5fdTm6ttXdagDDWFeJcUCrUZgFIOisCbwlewIlVJA7gNrYV2aoYrBAQ2MUdMH-JTTFWMNryHQzBNiWvV8UtFSLpWxQSWCNf-itonZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSnre96D_uhkdexGrk-xOyGsqk7hxFt0rv7_Av3FximoRvM_x7y7M-TOSBtLIxclOU_rJSSxVlbVIaNhdgtkl_lWKq0NAaGkxnNUNtTo20Z9lkfJhPymYPXI5nodo7aEAG-WKCuizc3Q_XRKWcNDB6dn_uh1fsIOOwFCItDljPW6ZbYi02CejrkRzGtzrF061Msl1mpVTQYWp4m4Bkt1xz0y-6q2zp1_SZ-J9EvIeGvrg-65vFVXpRNCF5OYv5ccadtGF2jHhMhPGijo2g2tFWFnnYwrJmvprVuvXZI29BHzK9J281Sq79g2VBzZpltCWGGCCg9mRuzQx6cQdgzdlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEJuJVh8pXCHm9QzfS-fR-iE47LS7s2MJDEl0jPCaact2ys3KfXomF4_ugrdm9Bvdi-zICiTCKOoQu6NXizUMO9-B5tbwxE1yHJcJoXLUQYdXoKCcOsn5rt9bBRV_aapzRm8Le6oAu9lJSF8FjswE0WO9GsQft_puuoc-JvJIo1qFiQ3NIleqs8U5vanhqlviHO1c4AN2lhKZL4bDUxCCmH3RNYt8jnR03QjciYz0ZbE5akih7XPR-C13NbRQ7IrpKMDM_6QghJ-3kTuCtVNQRwiSrG8Lw1XUUBUR0gVnyouzZzeaxpF1BwXodIFPNDYRTHp-AdtZ1ZF94BTLnRUdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulvaBKO1bBolYhz1XvKuE4uefPc091VacapGDW0z4vy3Q_yg3Bzwbmg9-JP8R_jDrc08Ss8YCzfdXVhrjqgCT41HSAIkZEHGnJvnWFARVT96tvvhbYAAEf2Gu81hLJLDvMCQeHRtS1wHN_amuQIF0yk71fenanWk19uKEimG5hSxEwfhJMH0M7sAKwGGryogsz8mUOozkEeern4R0SYwJ7l1rwpLxWgNy9VMOEdacIpdPKNttiSJsfI67ZamXH8cRUY1GqnTvuje97f4YC4TptYhcqxdl9uWoPwfGb1P_cdrmkvdlv_pfM_ucidAMTV9B5JsEWmP2Wm-4c_NbVq2gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Gj3uRXlONFMn2dKiW6GQbgLDwEEm3MKTT-xDuhqRwzTh9yudJZDAJBstzJ_poX77d3Nk40eg2YcRqf3GAXUl70qgtnipu6ZX8YbKiLXNzjKlffQlapG91pNnSbV_62iLKTuGO5UyZA5aI4KW9b7SXjXwlGnwVq-Z4t6oVTSNYKunknffrxzd8XwV0a5-qR_jRfwd_tD95NVFYRaIPPQwnMo8ccZRvTf4T7TTaEGKZeQq5AmZJS5J08E-lO28ooAf7s2RPLnj-pCidSIaMC17B6-LsPmKA0eB_p4iKZdBwvW8VL7QwZChuyMqRyiUd9Rx2QdG1OQecsUvv28hPu0izw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Gj3uRXlONFMn2dKiW6GQbgLDwEEm3MKTT-xDuhqRwzTh9yudJZDAJBstzJ_poX77d3Nk40eg2YcRqf3GAXUl70qgtnipu6ZX8YbKiLXNzjKlffQlapG91pNnSbV_62iLKTuGO5UyZA5aI4KW9b7SXjXwlGnwVq-Z4t6oVTSNYKunknffrxzd8XwV0a5-qR_jRfwd_tD95NVFYRaIPPQwnMo8ccZRvTf4T7TTaEGKZeQq5AmZJS5J08E-lO28ooAf7s2RPLnj-pCidSIaMC17B6-LsPmKA0eB_p4iKZdBwvW8VL7QwZChuyMqRyiUd9Rx2QdG1OQecsUvv28hPu0izw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngfQY2Y0Pwt7onQlEEkc97Ch1ZTCh9HW-eHfRgDrhs55cDjVUrlmaCHd4KSQ6mN8RE_0sNoB6bNoQwL4kY-yFedQFX6z2K6dVSerr03U_jZmK8EgGOznel-oNnWcEIr1_j7OIYKiX_25kjnay3sMPCLxnGIi5ts-0-wcVhSAV2kA7yAen0fyAaYwdz3TP5EPK9WDnbRCrkBh5YGOWP_XpElntv7ExXCYwgEJ_NZJbanFqF-PkZxk6rVJRUm5E1IU456_Q9JkJHoSBtW6Rwk37wWqajdsUq1eoAJYidTZehHwHNBNgTbWkQ9JIBg6JPmDbsG5FqgYKzoinxIefkplUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=Z3ZbJd-Ci7LgfxPFgV-lmbK92xvkhL0eYnJkQ_t5VQfWKBJNP9uPVeD8BgOvqDZKdDdMuFMeyBMtWS_OFpYK5IFixzNhKgIcqHv20fBaAwcdzvT0LRbG-ZhPfeNfsJ9gyogW8aQRfmNJyjiOqD_MdPxLt0MdbLp9ixgnDiGnindB3dbZX0tuSQmYWG4k-GIvf6AjR16viN660uVhtAunCGDeV6-pPGEDAQOSCIL2y-CT1z0GpASzxgKTYSHj02dBBLCvosB7J2CU1IGcqYjAnNphah3WaOcoYWOU0wuMQMnpf_6agyw2ULLlUbREBhCbdr9P2JXKMHaNByZQchS6ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=Z3ZbJd-Ci7LgfxPFgV-lmbK92xvkhL0eYnJkQ_t5VQfWKBJNP9uPVeD8BgOvqDZKdDdMuFMeyBMtWS_OFpYK5IFixzNhKgIcqHv20fBaAwcdzvT0LRbG-ZhPfeNfsJ9gyogW8aQRfmNJyjiOqD_MdPxLt0MdbLp9ixgnDiGnindB3dbZX0tuSQmYWG4k-GIvf6AjR16viN660uVhtAunCGDeV6-pPGEDAQOSCIL2y-CT1z0GpASzxgKTYSHj02dBBLCvosB7J2CU1IGcqYjAnNphah3WaOcoYWOU0wuMQMnpf_6agyw2ULLlUbREBhCbdr9P2JXKMHaNByZQchS6ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJP7ctrcBtLVtKO7KVObdHpIkcE90urpp4fCHmyo056nI0iz1WNTvaSoJ9YCzmg2RjsBFiD8wZZ50RN3f2Gva3vZzQonMc9mjMCDN2UVWlJ5qK5JTnmDu4Q2gKFd8rKx3uGpYmbyNf7geqyc8d5g7XB0Qn7la3R8AGVRel0Quoviu5km1tYb_maKH9WnhUs7cilHyrqsgBGhCRulomOBdnI5EgQO8Lg2vf7G1gtlkPzyLJ6OnrP0F5yv-AcLOoj1mJ8AO6sMG5lqoYW5D9orBe-KKvwXfaOn6-VhqIdZKc5_TG4tEyaB9HQq_r6VMiqJ5P5bRSX4ManyxZvg5kXaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=r7LkZBavyEC59LXEbFAY3F0pyRfkYsbinxtDLBK93-PSEnPsLkh6fOOZ7-YG2oVRhsc3FRCC9iqyTk4sLLz6Ll_gjw1nT_GzmXOrsBjRBLlvNdRdQlCEYw9_PLXTi76yf2jtIMa-UFGtVlyIUGy62GM27n4ElaTcD35CUbPU1XRemrgrVsw-eIpcc_5DOwS7oaBWPHdc-jzF_15-mfWjSVyS2vIG4FNQvlv7A99BKbSG5S8zIGsQnRSpb0d6MXIckN8PPZKX29otTZCunMYEoIK0gqPXOhaMR4ETqdgq5e_WPHYCSXvbezrXsmEUtYQFApE8PFcC4JM42Zlrnati7j8a4dJDth4-97JDy0H00e9nNfrrAvXi3_9w_sfbLo6fzFN1ewKFV9Kn7zQCoqJJbzyZYpWvWo6Ejtm2HXyAowbo68WXJMRl1HEkRCplPNbcJCORtFW32MSAcSmehX0E-r-6ba87HRwnGuiuHKCMfOgdkKXEw8DZlgBDeIEOaWUedF9AxAICguhQCw37f8sRjR7NnmslWm5oBVJiWXI_xKbme6WEO3ZQ37w3JSUIFN0sRPrjyHOPAIuuuZYy7s5MeSGdvbjO6ZEW6u_pbJW_FIhyDuqIKEUrMFSfLQq0Opoapn9oYUEnvBCCaQyGQ0OnRqphu3S1Yb-8Fuo08Lt9u3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=r7LkZBavyEC59LXEbFAY3F0pyRfkYsbinxtDLBK93-PSEnPsLkh6fOOZ7-YG2oVRhsc3FRCC9iqyTk4sLLz6Ll_gjw1nT_GzmXOrsBjRBLlvNdRdQlCEYw9_PLXTi76yf2jtIMa-UFGtVlyIUGy62GM27n4ElaTcD35CUbPU1XRemrgrVsw-eIpcc_5DOwS7oaBWPHdc-jzF_15-mfWjSVyS2vIG4FNQvlv7A99BKbSG5S8zIGsQnRSpb0d6MXIckN8PPZKX29otTZCunMYEoIK0gqPXOhaMR4ETqdgq5e_WPHYCSXvbezrXsmEUtYQFApE8PFcC4JM42Zlrnati7j8a4dJDth4-97JDy0H00e9nNfrrAvXi3_9w_sfbLo6fzFN1ewKFV9Kn7zQCoqJJbzyZYpWvWo6Ejtm2HXyAowbo68WXJMRl1HEkRCplPNbcJCORtFW32MSAcSmehX0E-r-6ba87HRwnGuiuHKCMfOgdkKXEw8DZlgBDeIEOaWUedF9AxAICguhQCw37f8sRjR7NnmslWm5oBVJiWXI_xKbme6WEO3ZQ37w3JSUIFN0sRPrjyHOPAIuuuZYy7s5MeSGdvbjO6ZEW6u_pbJW_FIhyDuqIKEUrMFSfLQq0Opoapn9oYUEnvBCCaQyGQ0OnRqphu3S1Yb-8Fuo08Lt9u3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=s8Z0DCFh0IzVVilhxTbahv-gAOMgHyW8FXhiaRwbcnJf9DHDKlb8i69X8p160gJ1Haj_bXaNvGJwb9nhyzO7m52jkAFrbjvvuzwRy5QOKNoFwiAr5KPMxYYzssnZ8PSH07yz7QzrPCnVh_U-MUkQCWoUUPLgRUq3cZW1yCLdV3q1LiCYaMSU-Ue93WuzmSTGp3wYFphDBArS8eSnpxCYzTGVVeCPcweTN5ZxZkFR71IIvCMkRw3rvDLWqyFQVbJEpD9hO7HYVynlrOoIwrtuZfmQm9cC3nlW5mg-pXy4LqseMYE19qIr_Tfbt1Jiw0HHMbwblPUU6UEjjvzUDDQHUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=s8Z0DCFh0IzVVilhxTbahv-gAOMgHyW8FXhiaRwbcnJf9DHDKlb8i69X8p160gJ1Haj_bXaNvGJwb9nhyzO7m52jkAFrbjvvuzwRy5QOKNoFwiAr5KPMxYYzssnZ8PSH07yz7QzrPCnVh_U-MUkQCWoUUPLgRUq3cZW1yCLdV3q1LiCYaMSU-Ue93WuzmSTGp3wYFphDBArS8eSnpxCYzTGVVeCPcweTN5ZxZkFR71IIvCMkRw3rvDLWqyFQVbJEpD9hO7HYVynlrOoIwrtuZfmQm9cC3nlW5mg-pXy4LqseMYE19qIr_Tfbt1Jiw0HHMbwblPUU6UEjjvzUDDQHUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BTnU8oDKotgkfOe58CdKhbbRWPDUTLFYO4APZ9rD2xDMOzZZU75ZpTudO83kBBDX45mZlfJzT5hWmt-jCuAUUvsGGmWfL_YcmwyvPlxH35huTRT5TxIOmlIcKZ8VFIw3uWaKB6hH3bti5xoOZvc-aPFwtLQrqnwGKuUgxD7pUpTrQs1hthSAYr0e0tLcqZseHDooU4Vl-PRgRG13d4l9_J2RZq9XRlKXX_NN1MQWX8KScr4BdK54brSWRX5gtfZUNwjYcA9NSdKI_LMklKEKmV-UrG0M6uTNaehBRrZBPpJi54wgWV2yd95TfOaIuOCyg4r1PI_wBa7ga6JHjBDBHS0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BTnU8oDKotgkfOe58CdKhbbRWPDUTLFYO4APZ9rD2xDMOzZZU75ZpTudO83kBBDX45mZlfJzT5hWmt-jCuAUUvsGGmWfL_YcmwyvPlxH35huTRT5TxIOmlIcKZ8VFIw3uWaKB6hH3bti5xoOZvc-aPFwtLQrqnwGKuUgxD7pUpTrQs1hthSAYr0e0tLcqZseHDooU4Vl-PRgRG13d4l9_J2RZq9XRlKXX_NN1MQWX8KScr4BdK54brSWRX5gtfZUNwjYcA9NSdKI_LMklKEKmV-UrG0M6uTNaehBRrZBPpJi54wgWV2yd95TfOaIuOCyg4r1PI_wBa7ga6JHjBDBHS0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAcLFWBaoFEnIBtyN5n-76CbdWeNcKBtnrSKeFNDcNwAcPMe5mTwfM2J-Z45s0hWpaYV8wR5B70FbSapZBsp5mzTxVvX82V-GSRHdk6bhTExdMBRhfBVqoLkzfAxhpKW-jaqs6nuqyP2lI2TeduM9JMwDs3DQj46AYFxO0WNmUYMuKt_Jg9zaMFmWSlQwGVsYU4DmnbeqrrVmrdh3Ia2hMje9eoVvoYSHKYXZNqhrjbFPota6xD5e80pytNFIfz2xKxXDBUF_RaOjlXiIq1TLSAlpXE8WkW1tDT3Y95e3TzjZsVUjfwiEdE3t_zcrJo98Oz1mRed6BsoX_MglFaxhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIz-cDUPD41Ds4v4Bp9y9-ZtWfcdp1sARhJ3mnswQjZT2ENanOQn6lR9ebfWIgnFeGPTFTsLsMwwNksucGtF8cCQPKyTzat9y6ydShEPcmVev_UwbJdWQr4EgIoaH1ljaeGpIas0QK9kE6j3FMfkwjnRytIhXjxujui2uwsYt-HwYJiqlptl61Qr7GpI9wbL2PdeaPfw5ZF5hXVXd1dKbwc5XKV9HZL6XYYdR3YQzaq6eHO9bO2nJnJY4k__MhjNdwfc-S2KydrlhVaJiKli11XOtapP82ViQXrJT2Me3vaa9LXQ7ESltA3DfGQ0qB_S6CKhDqGBFuoYaI7AdXpWvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC84w6A9ptMF-RxNN0ZHQ1cJYXUf17hNndmZmzL2BAj6IrI5y6EsKYMpzxuiAAwGve0tmY1WHiwHrjVQZ0kGPWITv4jNNrLqgJRiQCClwUw4oeT882AxrhNh8oDv0lfVCVpsoUbAE3ZiDknuebwW-PgKeg__lluQtX5lpF6CogbMBEUhHAjghBsFiHexw4WSAVzP53Pavs-ZAaqnzuKlDzof6myN-YvxmwWFdXy_mj7_ylPICWdUwJfZQq3LilvQzwK027HY2ZuFDGbDuTLQy8HMiyuuZdNlH3sUdm9x-EmEG3Cq6tuUnUJiVZTtytUhoAJGoYAVZuGpIWq0X-9InQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
