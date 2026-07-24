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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 02:24:00</div>
<hr>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=Q6CXGZnjn2KI5q9SEU-v89Ae7-dXLHQCiXQLDMaJwdGKmsKUMT7mwmuYMNvapNrEJEI87CM1pEjQJaxhHaBGiOfJi9GeuqXDjQxEIZ_bcUlUZGfhi_ynxQiJi3LKR2Htom5x2TLa6Z56PX5nSsEGja37pGCrxYsMihCaATM22JT_JyCxNiqmzqBMXzEe2SgCVMS6ktxD_56qI6IJFZmF9DoH6gu6_IdqNV6DDSXYVQyJv2uq_OIhig_YalVRtApTlg2C5Yt9p4RHLw4zbn3lSccLliWf4vuAlIUSQ3rbdhHFgiP5SAhXdru178-TBXLoQHMfsd53D4D4ory_yJt7rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=Q6CXGZnjn2KI5q9SEU-v89Ae7-dXLHQCiXQLDMaJwdGKmsKUMT7mwmuYMNvapNrEJEI87CM1pEjQJaxhHaBGiOfJi9GeuqXDjQxEIZ_bcUlUZGfhi_ynxQiJi3LKR2Htom5x2TLa6Z56PX5nSsEGja37pGCrxYsMihCaATM22JT_JyCxNiqmzqBMXzEe2SgCVMS6ktxD_56qI6IJFZmF9DoH6gu6_IdqNV6DDSXYVQyJv2uq_OIhig_YalVRtApTlg2C5Yt9p4RHLw4zbn3lSccLliWf4vuAlIUSQ3rbdhHFgiP5SAhXdru178-TBXLoQHMfsd53D4D4ory_yJt7rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFX74a6nsStoFi_KitK4iAhz0dtkBtd2r4JhvNDxvW7yt81r7YPOTVMT2ABqCiTIxEWUhDdt2V1sbTtTx4ibwP7jl29ujqeo3JUozzbXM27h3S6lSW8NB9alT8KY9f1K6V25OIkitHbYn58j07rQqfcIHWFmeFF2kkz3eC_mUnIEYhMa587qV6dOEGmhavkVUuvzEOO4n9s1IisZZWccxBhs7hu2PCxQtTSv6coBbLX0JsMXJ4Vrxa-KB-AqpWc71x5k_X--BSVRNQvq3H3-gfFBNZBGBVVssPEdelyVxJki9RRXJbddR6Qz1KVEXTYXiRcFdRKKj5TcDO3BNhqCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqWa70UuXvYgm82q4WeB5gldwDWB5ClQHPmwXBrE9yLirAFDO8IRtphWIuQnI-DJlGJgio9FCHztlSkzIGlwzwDFYTgCTOZktFtBnPJhUSyN0bQXatKmqFJIZ7cHOhW7MJAQBkR86PBrhtq2H2d0HtfqehXRFmrudeDVfLoX0x0Lh_C5m5ACEMTa4Pligf8NTyC6iwKGWkRiBCOMNI1J6wDvvZ7EedzqBR4dpQpZr5ks6Gja87kAQYgyroQJ2NWD2HEcsehKynWin5It9wU7gW9jJRipjlAhzPR1nx7H0gSFvbXFB-FkxpIFXStH49YPNAKP-AbUWCovJ1ScAqaseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=IlCvjUfAFBmLg1zWWPt2p7YF1VRmiFKFzrXtog9v7YUcyJG7l939vJSi88DNd3BL_vMZqOMtcTrjApJs5nHrzlzL_Uib85wUPh7iG47x7o7NbvTu6Ai-aMkrkhCnnbMHLrOdSk1ahWgZHQ5Vy1SoJUyJj0QYGgj6IHaGA2yFZxLod2fE6dpfXZKFt_ix0fQZ0CZuhifAk6ve0n9CZSaE5N7HplG4qsC_VQxzCJ-Ah67bxDp0qs4EIi8HROI3ZXUBJ4dag3p6hjLuszd1-TgZURRg5W5__z-TXJjy1_uWeMZsWtA0-2QZzKSUin07GZyTo7Zb9zZp51sCUcAVQwgIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=IlCvjUfAFBmLg1zWWPt2p7YF1VRmiFKFzrXtog9v7YUcyJG7l939vJSi88DNd3BL_vMZqOMtcTrjApJs5nHrzlzL_Uib85wUPh7iG47x7o7NbvTu6Ai-aMkrkhCnnbMHLrOdSk1ahWgZHQ5Vy1SoJUyJj0QYGgj6IHaGA2yFZxLod2fE6dpfXZKFt_ix0fQZ0CZuhifAk6ve0n9CZSaE5N7HplG4qsC_VQxzCJ-Ah67bxDp0qs4EIi8HROI3ZXUBJ4dag3p6hjLuszd1-TgZURRg5W5__z-TXJjy1_uWeMZsWtA0-2QZzKSUin07GZyTo7Zb9zZp51sCUcAVQwgIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMTx5dkGl32RMhG-1Hg_CtPAzpfVN27SicsOysr20M_aNLCquCTAtN-gFSbLC-onlxVwNmJMrlK0xifEzyk2wsUcaZW0pUF5FTYD0dJeuty-EFwUlZw5PYG9eQ6oyuaCWjKTQ9tOF4xI8uVayMzIWJhXhpZVLc3Zgi0V1mtIuxuGNfkk3n2KFE5zQBIix0FYskm02ZBXZ4FHoogqjFTyyp8KW2riGk3IG3Q6J98oEE0zNPingE_KCVaCHOXuCMLV4YEta8rNetg-zCZ18LGrjZPGH-NrrFfxsBJlvjhpVY46okXIEx12oo17GXcpQYvzP67av4_q4eoNs3lJ5O83Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=jQVwvBt-Gg36-ImaRhFkJG19AoF5GId86iTJQicWMttR4Lo4fPfDyg-qG6YR6hwF3-WorPCmpbP5tjxsohTRe5SdXWu4M0o4f-Q89fOvPZAHU_BW8qspxMbO3bJk-mFfvhiKDfvwQms5Gd5thxNmwElZ-W8GVJuhbBnyBUhN-eUHnZbUIMP62Rn5rBgxf8wkNaiO59Q0eecC_EM_a2gfbOkopzNv-MSnspIICWKlWIVuLZcjBbKVKjVobUfD3gDgPgennwFPUpWBmtMD1UBLjaapDW_OItAZj_k3-AmH2w83mnhciuon9uttn1Z96Le7Rw8KafJouVPkQldo-mcR-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=jQVwvBt-Gg36-ImaRhFkJG19AoF5GId86iTJQicWMttR4Lo4fPfDyg-qG6YR6hwF3-WorPCmpbP5tjxsohTRe5SdXWu4M0o4f-Q89fOvPZAHU_BW8qspxMbO3bJk-mFfvhiKDfvwQms5Gd5thxNmwElZ-W8GVJuhbBnyBUhN-eUHnZbUIMP62Rn5rBgxf8wkNaiO59Q0eecC_EM_a2gfbOkopzNv-MSnspIICWKlWIVuLZcjBbKVKjVobUfD3gDgPgennwFPUpWBmtMD1UBLjaapDW_OItAZj_k3-AmH2w83mnhciuon9uttn1Z96Le7Rw8KafJouVPkQldo-mcR-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzWj-RHZcQYNuZhc6T5HSsYm9HMfRp9bPL51m_SxFRKW2BYnEnWpZ37TpPxZ5JsRBtZR7egTrulWoCFlTZlLN1k8L5hXHU5ClfTavw5T9kjaEekOYOGwVzyS22GneLpDR5zoqXxqY1LBC_DaD_6QRKssMlqfN3byCqf_jJRJgM7rd34UunS8MiY6Ql_PYWWuspShadOJLwFLFbwBRl1ovm_h_im-qcvpcg_yIXnd2zxwefRIIJfLjzcj3x2d6IhRIBCPXE0yjOtonxshRabg06s5mMFAUwztxoqn1rLuSwyO6cN4hLq4bMG1t1rna3cXFjOj5cQajqvCx97xQaGMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn9dKMR5fvO-ZWasFVV_OK6igM-n0w6wX1OpSzI48_9QIoIen65pjxBjJiihTePxpwbPVveeVwqyzIclJCOUX19f0pfVQrGJHKFk06NJmFAushBiClWeu671ijcb71tHvXBQ6jaQLNjMj0fDr1e0BL8pLnZAkpJqCQzSMkAyTcnoDFD2tlvRx61mpk2g3oGl6m9q9M9d5GP6Tppno5BujExI3MJjjqpXhasILhUE_fwtg08Z28UNSM6i7p2Etp8fmI2MFt_ExcRu_hl2GHUt4No43rRpWPZKVzxJFTKBsbIF_RdTzSNdI_DYZb1WDSUFItlLmUfi177tELCd-l7ElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_hUx6gbujC3qprdCt_6yC_b_CSMG6P-1sFP4dQpKW1CBMD5UtFXrQvNYkIg3MaHL9_pfH6lyMvxH0bVbgf3ajT6Nnz4tEwxeMaimbWGiw6NEoaqMJTG2ongqb1lFDn2PwUu8X3G7NKJDBHCSxUnCdiFCgIZuvGQKtPvWQJsTvhOdDL08GL4lRtnPP9x50JaheMvmkr4vJhsO5KBqWtbZf0MVoRB429qaoOKVHm_zKn0D6Avy_wa6-rCzMs9bUK5Z7XbA_b5CWvZ_ybXEYc1avItcosduJkz1eTk6f7Xaq0dw7szeOmaqSIlVqCrwW0J2Qt5BbElHSHnmR6nVXjSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpDfhuwUVA7D_vukw--punel5VYWFSWuPlGiBExSYEj--tTFv4eUzPBUX0LQiX_fcPh8G6V9z2nEac9WJzaC-FmE6hFPbLv43Yiz958Qjro4DN7VGFAjTLJh_m8JyODFYYmxAs7Ndio3phyQMKwfIaVFo0lPOpakaRQHWbniwzOfmhex0vrgFyLGvu78C3MAiXupDtA3e6yVXnIQBemQInE5mcqzH3YzNUVZD_CDhL8rHsNCw5YvKr_1CHbf5ul3PDzMktrqT8yKnXB1auS38vTfuLTb8DhGMTPAl9U3pCZCAGfh6NTHF8O5OxL_cAKFcZvZo6m3fU6jmjZQZDl0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfKoV0gTyaCZcUulO6eoMt__181eK1aDzHb7BK9cGQS99Dg907jlT9LXBT2HG0ku32WOusIa_Pj6dOzPabVq0SfCCFquY8ER9KrYh324K6YBX5lYyOKj1HW1lWw_7FEn0AMO4JDzgK7cl5GEUfqMbOGfeVT950G2Psl81WBmNQKy46XVCzBREiCoZfDQ6MmCBPATf_YeGfNcCo6ZvsTK47L9NQG_udQkI37tJ58L1Dk1963XZFgpe1B43bixT7i3WLbQ3efeJBeJlNkR4GhgNJoudo35qIxr7QOSJTo3tdK_D9i6QF-1ZxU09Fig_NlegPDytC2Gz2ULTFlUicMwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5e6gqbtaiqMLDiAyunn8kGz9PU50p1SfNlg_8YwUXnAziW7g5Lp7WuEV5a9co26Z1tjMHKfOd-jvlLsX8k-g9ROoEIsGtRNc8Lf83BK5pGAMM5BjkAYVVc56kJcvr6IuD5E8uZuuhLcs32NzfDixg3y5JIWR4Wa_dsb817afol8ynVHpT446yvtiN5t3dmmIpcgmITUX8IlNT7DC3coSXOIowRxQ6s5-Z6deNba7QHPuacfbzo5xMwFImI4EegyokZOGZs4S7x5pZK9_0PgJ33_0M3hNeKd44zIQrwHj0SqAvil4VCQxf2oNAvbm3b-c2hApfwDttlBIIRhs4SVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTHIgkHMBtosxPvZiC3SVLcM4JjB-s1SDYb-XL-Ut7EOn7x75dLWeHsHWUiGWxgqIoJZMiuAbduDLB1Q2J985B2rW8Mdk-vNnCPkRGMBU8jZDKPeLPvKCqYs9qHetJNk9rJXT42fqdTTsZrhVyu_wadx2ZjeLwGxzXVxP5EVVOU2UbWvCnRwJTjNKaDhuGdRRrH7hjLv37_aZBIT7ipigvoYTU9BOoOJA1-K1Bd_fuFDItzT8RkC3kazTAZrQpsMtZrSA7YjU7huf9dSGPJvhn0373xlQtfz3NDETvkfeHGVkTTGxPC9bD_t1zg3m4vSNZkUZyNUxh1aG9gL88yrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=hqCeW6_UYuFFGSfwGrPsJ2dkkRdOObUpztbXNogp9Q6SVwtITz-4pSb9dHIlQOid8OEdqbg0kx8O8WcgxMCTMi-F0i3E9hW9N8pHy9Yy4jvI22TnmaOU0mbcIuWqW_B-E_9E52gKtat0S2fMnz1MoAKLtC-KS7M-R3rXNshsx_R49-pv1jsOCce2R3xr3gUuFqUIHKGwpK-BXAvs2rdeKX9dF_407f5tg-OU0usyJhKj1W2y1w43uhXDI9Rs2snaNtohtFchERal8BFiUQhLAsalRQFU-gtju8WlaGuIv0napYwyW5QCswQ5a69vM5oBg9yRWH4c5nbrCoXO2zDQLkC44f5BWO1a1bcWkcQiv5Iby_KzImJ7qVn9omRAhzXg6OGPSnrryKkxhypOccvvf0XMY1IvEIib1o3YcdNZu65L_IWoN0iiiVYYanPfUsm0Gako9rC6zuwQMNj3dEhsXfSrVQTNnSd9s1O7Rd6qBzuvi9svEz0ASPL5Rv5x24GZw_s8TT5Jhb1Zwy8r1brBn7X_63CHQoNlMaQ2zdS2u9opSYU4p3doY41HwWTdGq6sYJjIsovT9dNLYyoRhMCrgiHPzJ3_0sFxuu-N4KRikBStMUngrNslonOLm09Cd9-GUWOddEV9Z4g2hB64dj17g72OF1_8uv4kP2td77Vdl7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=hqCeW6_UYuFFGSfwGrPsJ2dkkRdOObUpztbXNogp9Q6SVwtITz-4pSb9dHIlQOid8OEdqbg0kx8O8WcgxMCTMi-F0i3E9hW9N8pHy9Yy4jvI22TnmaOU0mbcIuWqW_B-E_9E52gKtat0S2fMnz1MoAKLtC-KS7M-R3rXNshsx_R49-pv1jsOCce2R3xr3gUuFqUIHKGwpK-BXAvs2rdeKX9dF_407f5tg-OU0usyJhKj1W2y1w43uhXDI9Rs2snaNtohtFchERal8BFiUQhLAsalRQFU-gtju8WlaGuIv0napYwyW5QCswQ5a69vM5oBg9yRWH4c5nbrCoXO2zDQLkC44f5BWO1a1bcWkcQiv5Iby_KzImJ7qVn9omRAhzXg6OGPSnrryKkxhypOccvvf0XMY1IvEIib1o3YcdNZu65L_IWoN0iiiVYYanPfUsm0Gako9rC6zuwQMNj3dEhsXfSrVQTNnSd9s1O7Rd6qBzuvi9svEz0ASPL5Rv5x24GZw_s8TT5Jhb1Zwy8r1brBn7X_63CHQoNlMaQ2zdS2u9opSYU4p3doY41HwWTdGq6sYJjIsovT9dNLYyoRhMCrgiHPzJ3_0sFxuu-N4KRikBStMUngrNslonOLm09Cd9-GUWOddEV9Z4g2hB64dj17g72OF1_8uv4kP2td77Vdl7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=Ycrn3m6omBBPFEHKhgsngJbUH3NeztndNpe0B_mpcE0EZEl6ib2XBSxw9fmX0vfMPv9KZ6N4ltwSdyvTTxbJr8DPXgP9yOpQ2uXfIPpce_J9nYCTuU5f189LoZdpU1BIRdEsTLIPIsHv_x82LrG3r6pXj-0aKwqVS1s0VMzXpMzleum63f5tbdqLEixYuMnUfkmHfPbTsWXDsjxJ4sRcSO2vsj7iqFk7dSqbrpa8PhiK_gtrTyFm5s4allCA-8BU3am35l3TL1Fz25Pj6s1VzFD_hY-rGWlzPY_H1koIzQHZMlBwLh2DKLmZWdpYgWyuhNk2l88PfK95mNB-QhaPcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=Ycrn3m6omBBPFEHKhgsngJbUH3NeztndNpe0B_mpcE0EZEl6ib2XBSxw9fmX0vfMPv9KZ6N4ltwSdyvTTxbJr8DPXgP9yOpQ2uXfIPpce_J9nYCTuU5f189LoZdpU1BIRdEsTLIPIsHv_x82LrG3r6pXj-0aKwqVS1s0VMzXpMzleum63f5tbdqLEixYuMnUfkmHfPbTsWXDsjxJ4sRcSO2vsj7iqFk7dSqbrpa8PhiK_gtrTyFm5s4allCA-8BU3am35l3TL1Fz25Pj6s1VzFD_hY-rGWlzPY_H1koIzQHZMlBwLh2DKLmZWdpYgWyuhNk2l88PfK95mNB-QhaPcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIgfmTfet8L_JGOeUkewvS2z4DE7OFntzTdqTF8qg65Ko5O5btHMvUw0fcDmb9kfDXzWpT4WhKqf928ZP6i_QrKwK8celJRk-EYCrrUrU8jJLVzjxisdedbMC7wg7tPt-1WgRPg-5PtHHqlU1goTXyL3QdRYEYp6QDmjlE3TzRhFgxJ5sGHkQW0u7z-kY1rT_p5yOcZ2RdCD1qCFrKfPQuBd51B8kZCeWZaUCHgGFP6sFrWTm2qUtLo1Iz7_atr_SZAnI3mINRdozPF46BmWdIJNNN_obTWzeig2QB0D-rJ_ZygCnvhtSmrdcSOBR5IrCgRkM3Teh7KfGU54wAW6Ft3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIgfmTfet8L_JGOeUkewvS2z4DE7OFntzTdqTF8qg65Ko5O5btHMvUw0fcDmb9kfDXzWpT4WhKqf928ZP6i_QrKwK8celJRk-EYCrrUrU8jJLVzjxisdedbMC7wg7tPt-1WgRPg-5PtHHqlU1goTXyL3QdRYEYp6QDmjlE3TzRhFgxJ5sGHkQW0u7z-kY1rT_p5yOcZ2RdCD1qCFrKfPQuBd51B8kZCeWZaUCHgGFP6sFrWTm2qUtLo1Iz7_atr_SZAnI3mINRdozPF46BmWdIJNNN_obTWzeig2QB0D-rJ_ZygCnvhtSmrdcSOBR5IrCgRkM3Teh7KfGU54wAW6Ft3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TR1Dsu1OdJ56XmkI2XEFRhIlQEwfgfYaUnl6Bx2A1z-_ADE-pi85up3KicoIGCrzozIRsleNWyywF5kUwcXLVMHIrB6L7u6KOPLePMIpxc5Hb_aGt578VUZDrhUYDrmQ59xfMLLrb9rwvgt0UnPyDNmKephVgZEYjU-KStGthAaq79wVWS0GrhunU_FWPCCQqZDmMy7s1MS_u7DdTP7lu5gIEqYyab_FuWn6sYgJnJfAekDDwNzm9H1fK34IJAxYRLQzAOylXCKdi-soJ2D0eu-o1rT-rBz82WLVL5V4trlzY1BgTTxB7rBfmDbtmdVAagz3uV2z6txfGhBfa6I0Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeJ_5dpeE22ybiS3l4yIJmAai69Zb_KnYnTj_K-pAQDvA-gcPXsH64eDPwfuo2wLG9ppf6eUEofTwXrHqMi2_S7PG6kJ4jcNxeUtdf7b1nH1-CtN4kFTu2c3NFgPCmenQNdbp__4ROnBMh-i6-5hsixo2Nxs5yGQjPTufwsdENiji4brTMlzsTl2QeliVDkCjort9o60W66Bn0vBVhKezG1zYZxf-9mAo8VUEbvbIcS_G4IqduqzaTxJofgoGdUBE-FIEsQizpnzcdCuAaAD7JtAGfAEEG0hNxe4mzCimBTKoxZ3BxF-hI7K-A-Vy86YiL_bmRyoVcF-OIloitU5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJfT6BES8FIBr50Abmn9zmyTvQ_ScUCeyWG_a2c4zkVwrdB6cZaUDZElLP1g177OTaWgyOZPQ7S5VDyWkJ53YlxULEGwzNY7_kQYhyEtBjfh-dg7i7kMfC9x1st-mO-70wBxutNw966x30QhmCpIJh826FFq8N651ksjJusY5FK4CdrrQdtddYSnRfVyYbZEe2AzkK85aoYq0WE5FxolZDZdz5QQiE8I13S_j0_h6S3tpdfsXmL_thmBn0ScgSsuF1z8vDgYF4dU0F6v8n8bhlfl1ZqZmxKa2qgNuEnKpRgZbsjTcv0IxnppvY5sXl9zqMJL0CmIWEKryTrW3VT6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=afvRhydoL9qwFzu3Oz7_LRSzU-mWx7qLbHUEZbs5_QEZxmGT4o0EdnTIFP8r5DwxXYgjL8QlBjLfwLoUFuwfL1BbiuafD6h_v5Js9rv9ueLbsiG7QQ-z_jjzJKU2URUHFAjs1UuW4tE7rkugiKQpJqXOXqhTkk_lPIVbhExbhWYqa4M7DXgSivEj_WkK2h7oEji9rVFzDslHqiE0BjKfzPf1xAnzo8FeQhohAgmJaNjpV2p7Sm1vlqADiJQNZgMJgERWmc-5pWZmvTe64-IJgpC1AL2qBt_hRj1zWqDGh0cAZsOjtlmSUTy_33ijnjq1ApcJBg5dF_MKbheiISZRIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=afvRhydoL9qwFzu3Oz7_LRSzU-mWx7qLbHUEZbs5_QEZxmGT4o0EdnTIFP8r5DwxXYgjL8QlBjLfwLoUFuwfL1BbiuafD6h_v5Js9rv9ueLbsiG7QQ-z_jjzJKU2URUHFAjs1UuW4tE7rkugiKQpJqXOXqhTkk_lPIVbhExbhWYqa4M7DXgSivEj_WkK2h7oEji9rVFzDslHqiE0BjKfzPf1xAnzo8FeQhohAgmJaNjpV2p7Sm1vlqADiJQNZgMJgERWmc-5pWZmvTe64-IJgpC1AL2qBt_hRj1zWqDGh0cAZsOjtlmSUTy_33ijnjq1ApcJBg5dF_MKbheiISZRIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8xjFSqNtoy7qzQA30muVphYK0mqvsLnVMkLFUs90ZUt_VqxwVEKA_9GZ5BD15vGfNvYD4uYpceXdOy5rooVcFDKleJTxEUzyYbg6D8Qgd10N170lJhMY5kd0QjcgtMATv_QbMGGR7S1eu-SijLptrdogkfNLuXqG3SwBz8ml77Rj4RBB0DJxJJEqKXAYq16IcOFMyaB9IO6d-RdgxSs6ujNU1myTbVdioBo_AF4dUC3Bmtl1-s0ueAOLLWLZZL0aJ5-pxo2fARFAjmTI7qx3w_VDhZtMbqVdWnid_hlLN7VC6UblTKUjdmp7ojKDKL3YWGX2Ca78Th22Eja84BlFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUj6eizRxxRGHqDGs9t445bi3rfsWOsWq28TaYJRu1F9Aj1qqq3P57DlLpkrDDh7m5ShiJy3qPv5TsTRrqDky6gs09cJA9kdrL5cDyFwuY1UaDjsI9FF56GK4CncpufKTXyTHEZiXy5G4vncPMA_udtYSoelxHkIydsQsQslSa3cuBmn39odCAsDVfUJ1QuRLOV52vpL-vV_v87ew5ecdEsAUg7EjXS6yzGUjwwy44lF4qoidpWR2UvwVNysL97uvObZ6Ox1cf0bd46gH3pyu2Z-hvWvU41gouX-9Eiq9sdRJdZgurCUAKZsfnwo5zQ3EFVvXpVglm6Rblwk5u948g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8YXSOacRlweBnsDw3MNx-D-ffqJY6nQKqncoP54_bgUGRhkaew80P1Q4MnSXJ5OJRA2jTtVe4KDx-vQSIwPt0Y9NjVViizXJ_WXf5PLZU5KQLJ2qAu7VOWARY0MJc5m_tZdBny1N0G_FM6963sNIOhZgVhRQwsyLsBXr9WpIT0i_FFxkEhwVPSI0Nt6uYT-HUe8Nvgmuje97_S58oxBDM7vTSo7ERU0x2L-nFgAgeM32J0Uoxfjb6nGepsSV7TRTtrIvgobit0V_0kMwtjYY3YqL1O7HwmU5vf2zalSPTYE0AfqgCuhZpwcaNVo5mixZKIG1X684t0DUZNDJ3gO0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMq0uwDJDjFWqBxFyuD2WeLOnJ9-Re5aNglVvcc39c-6PkwwB7Zjc6d73LZF-9oz5_-GK7uGuLEzZRdYzuG2b8HjeJlzaJ9mdsJSrh-Ugri8nlz4PO3itdLdeZFJfPSW-BgjXDxC92avB4_UdbhaLu82zRJZC534BEf3_uG-EVWe2UJWJBXH7XWUueT8LAhJf3_gH0s8LAxtPOq2nwuAVGGQ-uDs__OmZv-4fkC36Ru9J62IdJu5dI8EyQPoFe2gK9XCwsWsTpSeGGVBru9FAHntxZ8XoRNNK7JdgGw6miaNuvaA1jmMaimBfCgo-0peBQlbSF_q5tJ-4zAO2RPB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=jZPdS553Cb_FbrutW7gFchXXQfg9nIFYmaCGsi90xI6PupNI5VC2OuzpU4V_w3iZ33i0co5I-MWuwBdp3W7f0nj0TS2ie9aAm9p-hbV0HM9_x-F6tE1uWTK0RQCGqkQv24cayPv4181LlH4V6_VWaZ0ZEg0kIejcKexLxz-XH93YRyCpDLz8eSZwPQD_S8lGeGAb55IzhVaRnkGhSkYb3RXwHMNaX-bTYZnhnjGpI-YJs65QbMpJrzDkpuVbEDhddcLHAnc6YDtEsuZnu31aakGiNghcEtcpg9CQ5ZQCOE3UZWBbgA7vzZlzv0qng_hEjZzxWPVtrXf0xIlekIpjAzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=jZPdS553Cb_FbrutW7gFchXXQfg9nIFYmaCGsi90xI6PupNI5VC2OuzpU4V_w3iZ33i0co5I-MWuwBdp3W7f0nj0TS2ie9aAm9p-hbV0HM9_x-F6tE1uWTK0RQCGqkQv24cayPv4181LlH4V6_VWaZ0ZEg0kIejcKexLxz-XH93YRyCpDLz8eSZwPQD_S8lGeGAb55IzhVaRnkGhSkYb3RXwHMNaX-bTYZnhnjGpI-YJs65QbMpJrzDkpuVbEDhddcLHAnc6YDtEsuZnu31aakGiNghcEtcpg9CQ5ZQCOE3UZWBbgA7vzZlzv0qng_hEjZzxWPVtrXf0xIlekIpjAzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=oCPlOteOZG2Uw4s81Hz1rBY6VGjrYmRGfM-zLUVeFsp3UPXlFnGixO8l0zK6RZCZW2G_loPtFPTQnPMfGI8QwPwF2Gv4eXgfcSBTLK1lN9XdqAeyFiNVHsiVPInneQQA3_ngdIZaPQ2vX8uW9HzdS2li8l7mbYIL01AZxX64snJ4hTNU-pMSb30HlVTGuZcUbBa6K-GlkxXi47X2AkU2DYOQLwoiSApO_vFcoYP17j_K8HXhz3kSQT27Wzs1nBtfR6zVKxHWbbKkfLYEX3E9BPErQZHLYdERWLqyPhStsBUi0H-uphFVUx2J694JLb436sjFuYU-h8-jOfDQkT3h5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=oCPlOteOZG2Uw4s81Hz1rBY6VGjrYmRGfM-zLUVeFsp3UPXlFnGixO8l0zK6RZCZW2G_loPtFPTQnPMfGI8QwPwF2Gv4eXgfcSBTLK1lN9XdqAeyFiNVHsiVPInneQQA3_ngdIZaPQ2vX8uW9HzdS2li8l7mbYIL01AZxX64snJ4hTNU-pMSb30HlVTGuZcUbBa6K-GlkxXi47X2AkU2DYOQLwoiSApO_vFcoYP17j_K8HXhz3kSQT27Wzs1nBtfR6zVKxHWbbKkfLYEX3E9BPErQZHLYdERWLqyPhStsBUi0H-uphFVUx2J694JLb436sjFuYU-h8-jOfDQkT3h5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=rYvH3Avmqtg7mP0qbMKkrJ7GgwI7JM9NyEkvS2zWlCGk9wHYdB9fw21IBvBA-MKBJGiLMpBTHGBoOT2DCdt84IIAmwBktUXWmrT0TgK9nUJ1xVHoPxruIgBQ9O6NGTNYQGnd0CyJJkDAyOJpOJUBO_Vz8OgC_WaesaB4uGQWLvIVlNYe5_GgO7COCm9N_JbnN1SNqBJxIWdIHkufFGMXwGCE3AZdd2f2HSJ-fSfMxAhYkgOETZSrP1J5gl6YcjAAXdz4vtdUbmLD_o5XLEx1c7yd1FKW27sazmH0GwHbdvAC1F06ek2zYaz1HgZ3qMi6UZwHb6RMj2RH90E4UMay7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=rYvH3Avmqtg7mP0qbMKkrJ7GgwI7JM9NyEkvS2zWlCGk9wHYdB9fw21IBvBA-MKBJGiLMpBTHGBoOT2DCdt84IIAmwBktUXWmrT0TgK9nUJ1xVHoPxruIgBQ9O6NGTNYQGnd0CyJJkDAyOJpOJUBO_Vz8OgC_WaesaB4uGQWLvIVlNYe5_GgO7COCm9N_JbnN1SNqBJxIWdIHkufFGMXwGCE3AZdd2f2HSJ-fSfMxAhYkgOETZSrP1J5gl6YcjAAXdz4vtdUbmLD_o5XLEx1c7yd1FKW27sazmH0GwHbdvAC1F06ek2zYaz1HgZ3qMi6UZwHb6RMj2RH90E4UMay7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIxESWVWb5iAUSQmDAK8hi1pwizmc3H6s95WmGcxSdeED0nyJU7a7kQrbzFAaJRwgKv9DzL9YmTGVmFQ0mIvDwFnLjbJ4DAa36FvbHx46YPjQZboPycqdupPNXJjsYhNaC4f__t78kP9cGjzxyFw8P_UfofbpY4hiTJSaGru3HaPy0kBIulX4A3JAfSo-AnA6YHXN-cVNhSlPvkuRGF7h3tPt9fKhJ-uhhmVb5J3zsQDMJgrMn1sF1Nr7JdwHJNLQJ_ZnBlsFnj1c_xL-2iYejCe8nHSX29spYoS7TMahYEI8UXGTblHKZR1Cw7CcIk24j7G83djfbjwmVvKAz167A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=FtkSSD09SDjQafJmFL5bbjldVwa29aAr1lYiRZ-QYcAAZorbboVXcs9l5zXA4F0I2ddVP1E1XLmU9RbhTjDXzn8Bqnn8iz7cT8XF6dIBo3gDN2cgrCx8jj-IjfKvuniOneiAIx-BmfQl90J2GJQ3aezZFPZOgLN8W9gp1f7eZORr2qs61xDTNNls-_4hQ5U-dyxt3UP0gArRQtc8CQLBMgHo2aPj1Ot1bZmT4DEPD0SBZGNZX736f44ut4xk3YUmeTZ_rwnrMsO1ZUlrGjdMQZO5u80igmZWQmo_W2CNndeu8QQKOHqbcVSuP2Suyg0UK5qO6Alvch9r0tNiuLLwzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=FtkSSD09SDjQafJmFL5bbjldVwa29aAr1lYiRZ-QYcAAZorbboVXcs9l5zXA4F0I2ddVP1E1XLmU9RbhTjDXzn8Bqnn8iz7cT8XF6dIBo3gDN2cgrCx8jj-IjfKvuniOneiAIx-BmfQl90J2GJQ3aezZFPZOgLN8W9gp1f7eZORr2qs61xDTNNls-_4hQ5U-dyxt3UP0gArRQtc8CQLBMgHo2aPj1Ot1bZmT4DEPD0SBZGNZX736f44ut4xk3YUmeTZ_rwnrMsO1ZUlrGjdMQZO5u80igmZWQmo_W2CNndeu8QQKOHqbcVSuP2Suyg0UK5qO6Alvch9r0tNiuLLwzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=dsT0Q4gB0Ek4V79ooPDo0V4bG9lPIZLgxU-ta8Z2Xl0dxgzd3PslCOIuQeNoxUKrUXTBl9vlfC1iOMrnoRmQ6bGuoC7TF6slEf0GfmhUSoVEfKvzPQZwR3QlOhWpLiI5ovFJVnCU6pe8Uz8jfbPOsvyXTLb17kfTSJnHKdyYflUr4IjzVlizWHD0MUIADGogHdbvaWaGh0mR3JpxB5-eIZvYYn6xlnGi5PVfSHYDbv5QsuGPqedgb_lhiTaJvZlAya2WAAueGwXSfxy7AtXfRoyrvylH4hVXsMLEdR7gNEBA1A6aLrbnxPWLt1X7cLFiuom0ztyOUA38htnYsjaGEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=dsT0Q4gB0Ek4V79ooPDo0V4bG9lPIZLgxU-ta8Z2Xl0dxgzd3PslCOIuQeNoxUKrUXTBl9vlfC1iOMrnoRmQ6bGuoC7TF6slEf0GfmhUSoVEfKvzPQZwR3QlOhWpLiI5ovFJVnCU6pe8Uz8jfbPOsvyXTLb17kfTSJnHKdyYflUr4IjzVlizWHD0MUIADGogHdbvaWaGh0mR3JpxB5-eIZvYYn6xlnGi5PVfSHYDbv5QsuGPqedgb_lhiTaJvZlAya2WAAueGwXSfxy7AtXfRoyrvylH4hVXsMLEdR7gNEBA1A6aLrbnxPWLt1X7cLFiuom0ztyOUA38htnYsjaGEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=RDhJoq2JOnkIbAXddYa1LRedrZ-tNoRFhWPcK-I9EU1l6AfR7B_wjZ6fOGUQIT7djnLbbw1hKrTyZwdgHnZbXtRGT-_ciX2Nkvcmv76oDUnMtrxLhNs6tEITkJRP7yBRgmNBgklFiyYUu6v5PyKKaSCfAqcpITO778mb7YqKJ_B6r21_A42VPYLR9DYi8M7fk4X3z4vZRpLbkHJGpNHmZZ26urnYLOkTfsIkogFkz2_k1RUqSqaNnOrw-pFFT0pnyRoshEh0hJSu0oN_rzZKdDKxictbzbcwE-886PpxBJycmb3fw0KZBADtIjWDoLgqthuj5Rtjh3ZOjN6slCwQPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=RDhJoq2JOnkIbAXddYa1LRedrZ-tNoRFhWPcK-I9EU1l6AfR7B_wjZ6fOGUQIT7djnLbbw1hKrTyZwdgHnZbXtRGT-_ciX2Nkvcmv76oDUnMtrxLhNs6tEITkJRP7yBRgmNBgklFiyYUu6v5PyKKaSCfAqcpITO778mb7YqKJ_B6r21_A42VPYLR9DYi8M7fk4X3z4vZRpLbkHJGpNHmZZ26urnYLOkTfsIkogFkz2_k1RUqSqaNnOrw-pFFT0pnyRoshEh0hJSu0oN_rzZKdDKxictbzbcwE-886PpxBJycmb3fw0KZBADtIjWDoLgqthuj5Rtjh3ZOjN6slCwQPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=AuIKLkbYizFhctSNo1lY9w8XVcIqJq0pNANkUN3R3NhyAt-Zyeh7DpC5IsN4SHNyOahEI8xIoFBsDsfYIyp7dJjUgYDA_Vh8SAqBvfjby7cDj-z1KDGN9zRLtCylpWEEKXmCLDRmpGKCXziCPGOd5CtuWku7vKnTt16QvOLW-LRbo8QxAp6dM4cuGv_u_iaPIYH_K1mcx7c4Q6C8fU8bUHxo4IRuVYuPK6PeLe2UXdsYQUipzD5zdefQXyg5BgGlI9i7L8oKfu1EzSD1UV_e3mM-SbEhUmAesTxZGh_dL95VVJzNbE1jjYJw3Q3y5NfjLtHcYJZaZPfLfLFA10wL05T58wSfXTrUshnKO1qze9EhzejuXYPBW43XEx7GPq7lXumbGFnzgraNad5KiWqliwyzX0K-r_6dg4iVXwLdaqc8b0oA-QO5_pk8WuESjnGOIZIGdm0PjWnKHgA6x5b2WTklWYi_a_J1gCWXr9kcbAayPkpVGsWFlHOJ95ydLafnQlwgkK1V78_vG3otMOWQIyklzQk0fRT8DPQjkKLG6n0YOGFqMyDIg_KEsjxXrHsQkUtf96x5KadtLonGjNMa6ZlZiuwwZjNn6JwxyaF9sf2r5sY4MpnPeVAX0FiSM4-Xvd7X-NsJLnbnxWPsQiTPDQ5E5F9rM3ikW2IEYmp7TZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=AuIKLkbYizFhctSNo1lY9w8XVcIqJq0pNANkUN3R3NhyAt-Zyeh7DpC5IsN4SHNyOahEI8xIoFBsDsfYIyp7dJjUgYDA_Vh8SAqBvfjby7cDj-z1KDGN9zRLtCylpWEEKXmCLDRmpGKCXziCPGOd5CtuWku7vKnTt16QvOLW-LRbo8QxAp6dM4cuGv_u_iaPIYH_K1mcx7c4Q6C8fU8bUHxo4IRuVYuPK6PeLe2UXdsYQUipzD5zdefQXyg5BgGlI9i7L8oKfu1EzSD1UV_e3mM-SbEhUmAesTxZGh_dL95VVJzNbE1jjYJw3Q3y5NfjLtHcYJZaZPfLfLFA10wL05T58wSfXTrUshnKO1qze9EhzejuXYPBW43XEx7GPq7lXumbGFnzgraNad5KiWqliwyzX0K-r_6dg4iVXwLdaqc8b0oA-QO5_pk8WuESjnGOIZIGdm0PjWnKHgA6x5b2WTklWYi_a_J1gCWXr9kcbAayPkpVGsWFlHOJ95ydLafnQlwgkK1V78_vG3otMOWQIyklzQk0fRT8DPQjkKLG6n0YOGFqMyDIg_KEsjxXrHsQkUtf96x5KadtLonGjNMa6ZlZiuwwZjNn6JwxyaF9sf2r5sY4MpnPeVAX0FiSM4-Xvd7X-NsJLnbnxWPsQiTPDQ5E5F9rM3ikW2IEYmp7TZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=B6fsEFXwtcMm1bY4Vt4GPakmhQhIY9rksapnvB4pcrOs6Q3W7t8NQjQSk1OxGoFS9Tf4jEMPnswagZv4balJ5HHHzoh1d8-4ODYEunQ5H7LI8CBEUjl4cRUm-Rv0EkRTqkPCbd3qh-t4V_EHW5IZOBZ4lJF873DPLB736RalbZFTqU346z-WDMiCgcRVexzmCmc2cdUUE_HYGmUQ6i1whnkO19MxGBnpXK6bT7H_MZlnllSfloSJH1-ajcZYLfG0e8X8fEU-YI6WUyT8m0dqMPtSsoMmv73Oa89Jb0BWXk_TTa5287E2TTSKvDRzSTmRptqxZg3ikAFS0ywE36v2rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=B6fsEFXwtcMm1bY4Vt4GPakmhQhIY9rksapnvB4pcrOs6Q3W7t8NQjQSk1OxGoFS9Tf4jEMPnswagZv4balJ5HHHzoh1d8-4ODYEunQ5H7LI8CBEUjl4cRUm-Rv0EkRTqkPCbd3qh-t4V_EHW5IZOBZ4lJF873DPLB736RalbZFTqU346z-WDMiCgcRVexzmCmc2cdUUE_HYGmUQ6i1whnkO19MxGBnpXK6bT7H_MZlnllSfloSJH1-ajcZYLfG0e8X8fEU-YI6WUyT8m0dqMPtSsoMmv73Oa89Jb0BWXk_TTa5287E2TTSKvDRzSTmRptqxZg3ikAFS0ywE36v2rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=UQsvHd8mR5Vmn8HggkLAOEnEo4vyRZf-5L5op7J1VyuB4T1jcjeJjVXWmlcmWo99ize0JWBkHJ-5FGjjoO6161JkZq7nNUf043ltmD9MkjRUqZwZiiPLs2lH3hCrA1c-patpjzTME-Hy2o3xM579QzSTr-nlnNoiZGM9Pqn3ldDmkJHPk4hLMc-7YVZ7qrrFY53sHUbAt3YjIij2_oyqfET2wn-q_8HOpu1rLvyZmcurSt6N6KGiqHWd4RpF9u87qRgrCZfWvXWLNpcrZ20qY8U-k1DPumX88X_uT2ZV-idIrpe_OnStzfJi87Zgf1REj6hKu7N9Hrcyi4N_bhnV3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=UQsvHd8mR5Vmn8HggkLAOEnEo4vyRZf-5L5op7J1VyuB4T1jcjeJjVXWmlcmWo99ize0JWBkHJ-5FGjjoO6161JkZq7nNUf043ltmD9MkjRUqZwZiiPLs2lH3hCrA1c-patpjzTME-Hy2o3xM579QzSTr-nlnNoiZGM9Pqn3ldDmkJHPk4hLMc-7YVZ7qrrFY53sHUbAt3YjIij2_oyqfET2wn-q_8HOpu1rLvyZmcurSt6N6KGiqHWd4RpF9u87qRgrCZfWvXWLNpcrZ20qY8U-k1DPumX88X_uT2ZV-idIrpe_OnStzfJi87Zgf1REj6hKu7N9Hrcyi4N_bhnV3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEYz8okERCnOnImgTHS_6XWvUZiJYVNQsjm9_pNJA1-B6IPTjaVYGzNByt6t5dM7OAj9a0V8v6AFY-LvWf3-dMPPT8zt06ph7OMIEypI1lBj1vu4J-tEGCMlvzh6dSbExPZk28J5xI2W1aXKPr4HoRRfyKcaYMNovWr7ClULPNXUC8bBlGsyQBGLak36ZRkl9CmJM8Yh11Xhv23s7LSVkeCCmqo01wEFyBSaojbgt2ZwSJyMP9uizwNQa9hBwZesvOKHW2Vc6ByfQ5jTaCv8gruxroYxafNNf3SOK6hTGLUpdrGmhTfvQrD2Iqa57A169rAahon0KzPKs3PEIUa2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDr2d_l-W36fv6ptBNusDQ1EPfuWrE15tZZpC_djqzuSDw4nHp36Ak66Kfqjx5EThYDivfbj2fMMNCXzzf5KyTdIDvnR42qpBAj8lu2FfVCeL2vrwkp3kQOuwsHd6obBs2SCgJE832y7CD2V24eJFhTU7q_QJ-0se7ZhBXdj05lBQcdoKfMPD3x5_8GGZUPndQmXd5NrquSbvGWdb8nOvpw3LxqhOlAVO73TfMSKoC_6dN1EAKpnbuwVhzIgBkO_aZDlrOJNGkGAScTxVklZ846Yu7y2zxfH5gU3W_ZYZ588SWfGtIGRbRsKnhPYl3_07ghA_QoO-Rwh4ZMaEB9emQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=elxULGkEw--6XMTPlDTeOJUUJLYRQTZqP0VFEXm5e6k88BoiEdOByvAJrqHV3pmp1grISVboTKZZ4QpuLYQGYWYMDm15HJZIhFxXcFtlpDuQFEjca6c095mZFLhYyt5HXoP8iMg_vC4EoRU5Qvprx3nJsiZT2zDgrCSUPtZkhOXi6v6U_I_5yDZKsP5GbCBBkBBk_eMMZ2B6BG9c6NMBm2mkY63I_FJD7ZJriQ8iy0iKqxLHvmczyCiNx2Vs37vGzNJUBK8aBtb-oAuHCyAB-jfTFis4p4IXhEnhBzjNLjFFfrIYbERJ29_qc0xQZeq7gwR4rkhEefhDTIqZTSilAkiPn6HX8btnHKdfezoC-YYzMhndSZB-6rjF2XpYZbYUKn2atP-7U6DxG0V6AuwHAHd4KRyyKUpD0PWxNd4-djdJ41EYcm3MByohzDXtRwS3K54oyYmbgAmumPiybK9SAmAUHFFjAiDeV7EF2SWp3wsaD2lXm0aCkhhXuY4dFvttgBH30s5llKizE8ggS43GY-CmtxxK4fLRsv9E0TBvJJr_QDauPPv3VpqXxkhUFedRZihKfzO-n1oSbPopHDwfiEbwYIp1Nlrq_-VjFWCL_4kkBnSm35NVAU66hU2pvODWk_JbT3Cbrfdkef9jBsfhkNYyqmz6VFFHKbF2tfVicUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=elxULGkEw--6XMTPlDTeOJUUJLYRQTZqP0VFEXm5e6k88BoiEdOByvAJrqHV3pmp1grISVboTKZZ4QpuLYQGYWYMDm15HJZIhFxXcFtlpDuQFEjca6c095mZFLhYyt5HXoP8iMg_vC4EoRU5Qvprx3nJsiZT2zDgrCSUPtZkhOXi6v6U_I_5yDZKsP5GbCBBkBBk_eMMZ2B6BG9c6NMBm2mkY63I_FJD7ZJriQ8iy0iKqxLHvmczyCiNx2Vs37vGzNJUBK8aBtb-oAuHCyAB-jfTFis4p4IXhEnhBzjNLjFFfrIYbERJ29_qc0xQZeq7gwR4rkhEefhDTIqZTSilAkiPn6HX8btnHKdfezoC-YYzMhndSZB-6rjF2XpYZbYUKn2atP-7U6DxG0V6AuwHAHd4KRyyKUpD0PWxNd4-djdJ41EYcm3MByohzDXtRwS3K54oyYmbgAmumPiybK9SAmAUHFFjAiDeV7EF2SWp3wsaD2lXm0aCkhhXuY4dFvttgBH30s5llKizE8ggS43GY-CmtxxK4fLRsv9E0TBvJJr_QDauPPv3VpqXxkhUFedRZihKfzO-n1oSbPopHDwfiEbwYIp1Nlrq_-VjFWCL_4kkBnSm35NVAU66hU2pvODWk_JbT3Cbrfdkef9jBsfhkNYyqmz6VFFHKbF2tfVicUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmH5br_AnuNSDd5qaDbord9Fzizuh1JyCxq_Bg2f63KQM_Cmvud8actlktoO69hHhS-Hq_C_Hn_A1JigttLZCgy8J9aEJKDbnMhyhtSO_Ty41WzqyYVjYYfF1M5jliCmACa9QSVDsZvIroR1z9Dtopx9vdOusaQC5v_pDuMu-xZZ94sPfeNu9xdJH1d98o9hf38OxQGpaNeWgizWSy_aQ7_qlBLSZYUdDrK8IOguF_Im74C2taE1MsJwbJQ3SqiqHdljzZ5jrZxSvHervLoUxW1A_HS1-Z36NG9TLYr77sb9lVoKPpxfmuJtNrU2kfu8HF0Xybe3QN5Jux7foPx2fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pk8AiCzbrKRXQ3HwzFseHQJkIQMDcV5UR59zLb9JDVSbg0hpAbYeSAPE0iSAqmYvyxU_kYXgI1C8QSs9oZDsaKWHW5xxn6u8bLLhkX5uA5Q7lcBgImsFGBjpPoYJKBPqghJi1srDUVq2koYHzlrCHtULR4JkPHxA4gkpx5cnozQX99pKp5q1mrNIcB65i3bTzHV5WTM5LSKu0amGF7f9pv4V1s4w-xA-2xCGYR66HZYadpbYyGE6oAfkcLq12i5aKCwJgVi5WZaUeuKRKHhq33qnAipO3pF85RGILgW_QbfKBXgiybQYeziAtF0Mj27G8J-i6cXSsMVtFRJDN2uZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAhjPrzeVlXCf0uYgyI7jSGzSu-93_PbK-5FSCi1R-TjNA_qAZLeCzFEUW7qML46Y5j14k5O5mDIoQ3rf9eYQnpXRzc-lj-5tevBq3CfmtYCAtGen_ctmFl6iH1m2SZEpllnoO-Q33rBOwKv_a4x52Nlq_x9gEmub5hB8AdjTTfcqKEpq2eLyyFIba1eL88LWfTdY-246XahNSD7TK3Im4xUvl9xXkekEpczXbTUbDKG-uUxEsKkJuLA2-QsIe1zRUdYMvG-50AuJZlCsrPRbm9whtQzuvmDDi5aQ_o_xE3Tpxb35rgJZtq2nKExKHCp2rVrMjCxRWtO6qTC8ECnvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1mJzrBabn9ua0d1sod6yC-rbNZYEr3t8LIF634U2FeEJeQ0jCrH6jilD9f3SUCS_wMULpamFrU5fRRG4uHSGldQvsoVezrp2C1HsWpz6beQqzsYC8t2HI83ngaTb8tVjzdZQVwfndlQQqwC_rVLMqJXbY7x_Zp9kkTkYaqSeD7KdcU8OFLZEiDpRfW6bMSYOPP6OPunDBtlwDtZ7q_YNQjXDjpsYI5k9gz3wWTlRty-XbhwxdO2FWnoUpfygp7Zxc6NY40yRZqyHKnoK6nXkize5Ld3tXTan2KVr1CFZVb-dd0KvhWgEf9aTwUqGqUiGuGT7yNyVh7Q_tfM-I7Caw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=PJuwWLqEsDjTpG0H-x-2Z0ENglwtCznucCDPlMqYxurs7ZKW8FCQiDy5mZv_YDAxyW57LcbZSGmDAiGSNv8OAvkMH71q_WbIJA9_hxeeHSznMvgl-32X5xtDk2nYw6ULf-lYvTT02-hHQXFkoQIWQaJGgDna74_xPu-YZ5ZO47lJMEGiYlMtBjNA7frzTp-4jBqJfQoAsOVJFaGrvxk43U6vhtJ3QUqBA0kuG04C3QaiFRqv339LNkxJFVrOGA_ZJBK8iMLxPs6Quniw7evvp_VR_z4p60l3m7ChVrJOTLTzhXa_viCWqVCSe0IJ43cNqlbjliB2iJdI8xMi0a4T-D_IRRCxSH32gfeIpelQrXAOIUyqhdHK88n_GpBrvzDCs3L1yx31l40suyHEOvGGRmkU_k1bdHVk2CJd7TjmXDfP7Sf-yFKKCrn8qfSa8HyCsOjIo1mhfocXNVx8EeEhXAHYu31DyOVUJFLTOwu-l8Ck2SGFk0Jog6vKgggCdKV3e_cubmJ_5JVuw7Cw0hvQGa9E_u2f08BqQ1gvgm9F5gZCwMNVM0Dr3gPxKSH7gyk3mhL-uGinEhbpTmPrsCk5CFW1fD8OZONSI4CDxeeWNPSlbgrlrKuF1twXLbrEyFxjCF_EhIyGRztqXyxk6GOUMi3QrcGUudWaUPkXHlWJq8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=PJuwWLqEsDjTpG0H-x-2Z0ENglwtCznucCDPlMqYxurs7ZKW8FCQiDy5mZv_YDAxyW57LcbZSGmDAiGSNv8OAvkMH71q_WbIJA9_hxeeHSznMvgl-32X5xtDk2nYw6ULf-lYvTT02-hHQXFkoQIWQaJGgDna74_xPu-YZ5ZO47lJMEGiYlMtBjNA7frzTp-4jBqJfQoAsOVJFaGrvxk43U6vhtJ3QUqBA0kuG04C3QaiFRqv339LNkxJFVrOGA_ZJBK8iMLxPs6Quniw7evvp_VR_z4p60l3m7ChVrJOTLTzhXa_viCWqVCSe0IJ43cNqlbjliB2iJdI8xMi0a4T-D_IRRCxSH32gfeIpelQrXAOIUyqhdHK88n_GpBrvzDCs3L1yx31l40suyHEOvGGRmkU_k1bdHVk2CJd7TjmXDfP7Sf-yFKKCrn8qfSa8HyCsOjIo1mhfocXNVx8EeEhXAHYu31DyOVUJFLTOwu-l8Ck2SGFk0Jog6vKgggCdKV3e_cubmJ_5JVuw7Cw0hvQGa9E_u2f08BqQ1gvgm9F5gZCwMNVM0Dr3gPxKSH7gyk3mhL-uGinEhbpTmPrsCk5CFW1fD8OZONSI4CDxeeWNPSlbgrlrKuF1twXLbrEyFxjCF_EhIyGRztqXyxk6GOUMi3QrcGUudWaUPkXHlWJq8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Xzl8Jf8YFBA0V_hETwIsFcw9S5Ie9uC9dKzHZuFi6r089PWG2gKQvj8NCZ3PGU4DyPimaXko_P5sOnq2QSh16e3P7YIuI45CE5_MOO0wACjqwcUh0ZrySJ2Wcz8sXsCPcmdTYQGcY-xpXj1-OswWsv4-1Jk02oqbyt0CJeDPMPLjXLyCpxveuaePOUS1PdM2ery1Dw4JDBnC0uxxbc_CPniAdEbwCsVU_xq9pMXvnPdF-eAOXadnBDEf6a60--rMnqIM3u__N4wl9qmrCK1P1Sd8-4HD-mJDDbyITUKw7WFOnMfwyqkhye897_bosGDJdFv4gkZ17E12hsyAueoL6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Xzl8Jf8YFBA0V_hETwIsFcw9S5Ie9uC9dKzHZuFi6r089PWG2gKQvj8NCZ3PGU4DyPimaXko_P5sOnq2QSh16e3P7YIuI45CE5_MOO0wACjqwcUh0ZrySJ2Wcz8sXsCPcmdTYQGcY-xpXj1-OswWsv4-1Jk02oqbyt0CJeDPMPLjXLyCpxveuaePOUS1PdM2ery1Dw4JDBnC0uxxbc_CPniAdEbwCsVU_xq9pMXvnPdF-eAOXadnBDEf6a60--rMnqIM3u__N4wl9qmrCK1P1Sd8-4HD-mJDDbyITUKw7WFOnMfwyqkhye897_bosGDJdFv4gkZ17E12hsyAueoL6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oss3iRf_H6iDDiFZZZqCHM3IP_VW53k316MoiJno0e-OZRcuj47x6Y-SbO3cGGizF0huYnwWmp1u3emQn29F57sO7XIavYtmgbqvVoGuYV8sEvMOUjYlwXCN1uopjXFHJZ-eyGryfjUoQMkjapl8QXaFrZCFDA-EC9ex4VYUk3VqtDZNwC2QzZ7uQFyZTUMzrI7-FGtDkagRziDyEaK5_79EmfEni-wCHzbp3F7kXAXEVkE_ozxkpLKZckX4fiuKNhcRIDGJ4sWieSAUt5g6HBWAM-vMP2JEIM-1l2UIsMk4-aTXFsgML30YPT8QmPw-UYAU-9fZG045wXnKouLFkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSGbbeQ8yIkBRe00qxLAbLu-njW0_5YpHpWg8T4qKHRVNrQ0vwUGHWhe2vGsSiSzxJaxlEOerWWudTMjTQeD6dPXYO25VhUqvanU9c0523R_UXrf-tr36Pn08l4VrbIyt6r-JJzLNWJWSR-JaW1kfxiLZxpLJd3ZyH4nyQ1C8fBZbcuQ2FeIbbzVuD6_rzTiVl91IHXhFau2BPIPamCnfRR3xiyTtF3W647gzQDK4rA18z3pJgz642M4qxk_-fA_z-T-g1RXOjkmodvlmBOhwFughVkS-ZXV0o4N--daotbYKHRuQmLLdq8BP9ICt90dggQ_cGEbEuLbmFUKBJjB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjCNboAwqpTmlrqr7LyMcP_neVeawuhY_eCU5KuLqNFHMoFqEdGWfETQp7HEy0ibMVsOG-9bcBpqkT8lwqQ9HhlY2tJVBwBDDA-VPQRr0MfeIEBoa4GJI_G3HSGcJoFJ5qOHNMJgE5TaOPKZAf_3C-WxhzzY7JkySAH-4ppt6UBSJq_ku7-852whNDAdGCWRl71pGTqGL_8mnJ8DRaaiD3IMWGmd1m-Ig7I1Y0CcuTCyROwkyOoJ9FGwpKmlS95AchefTvPTcjdV2lbwAW3Zc1Otj_JNVgaILNCSRL4fmQm-CNpgym0sRMgBQhWapUbyC2W6Z_f8AFFqvOoSlhFpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S-3AsAg6sXtjEo9Vp1xuDgLa4imsH-oE_Y0rPQBEqOgHMjrCEL2946NeSw2-LvIBLhH5zc9JgwD0Uv1FHLEKNch9dTU1iZ02qO3JhA78NOPiC_S8rnU5vf6RTihH_GuTsASQzyJsk43-34Lfs_N_pObiHosCythwVTMeuy04TRV0zEe4kC9HFAyCEvHFpWN-9Y7IexW68mu5VaG7TWVYLtZsJHwFoCyg5Xi3DPiEy7pnyuwdw05W85o8sScAJnaq9jwHZvxbZRWxzDyjKRH7lae0dqed3tJ2V_zDvs0dYpubOF4gWNyPA_fOamMRRLbk1wHNA_Q2lzNnLTw9bzFBmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mias679I4tA7gpBawj-SPHF7zLQG03dz_bstKfu8_Kezcx3ArLvbmdYXljgjXrIqJ7jT4iqyxMtzWqENmp87x6KmA9gKuiFh-oTjB2_zylX9LxMRg5nwWUvxk1uIYfuTJ5HKh7XqYGEic7M7-CAUFiNiPefzCMLXAkYUUF8lEFetEIfGnxS5ahTdZsuM0uO6cfKW5WREMs5CGSnL7Fh_Gs-3z6L7UFZEw1tQiRSKkWyoXJbfJQJE0f0GiQRLqqKQ3SpVRColEN3pbNpnCY10h0czItooHRVl-mP1zo3oU5sHnx6OrACjraG-tjnwOiuM-Ns1mUtvgCbh8qWfOVo8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk7PfLxBtcQDNWec06Cu_8EyUkUN-9vGv2z5cZOUaSn4UGMrW6BJYZnxscvOSx1YmEUkjVOoT8ZSCI0JlkbYDW7OKMROynJ_QJTDj9ntN2zYW-VOPq9J961ejWO33nqfJMOTO9WdFvB_A29Zil780EyA6OYcqwCWMNqG0E4QjNkO_Xdk1lP_3OXlVNMAYXARa-bfXj8ta2UrOK5mAJ-sLWg90qwpuHezKFnk0rC4MApHsrnc7EOiJ6_GO9njem4gmJHbdLbTqMNnB9IKRdH-wLIBL0epIHjn0teIXkmA4Y5emCiLiSf-lFVJO_KOpvWEuzU4ycPO0_924S7-OxmGkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVYsfpehtLBDSLUgi4WIZhyTCazvs2nCTj922Y9DWrOxapJo59kFCvyXKbqk4AmmYGRdpb3Bb1j3UJ_e_-9_l7EDgtO3x-pJe0O_Ip5TMIgxmNBgW7KamfmIXQf3rKOly3CZQ3xRJQ3v6LyarxkZ5uXd5eHSkk-57vCxHFUzIhOcbsc6qgCMot8MIJ-aZDPHI4a8ARcS-b9nRlzxCu3GcXxpWC4aO-SHGyvw5swCbocW9T1vxpktDPrtK7GXQ1KSxivfB-5itls4pwvGJeATUQPR2oY6iuzoLCtRBgWd3K-0bl7ooNfmRyD3OSpXagRA10aGUSVrU8s7EMRzgDTE7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=DHRujNKLdRhiyJH7zws1eL5BNVpWz2qJcnF6Yf5dEhOv0hj4j8MLguGmRWJrWwVwp5nyzAwtlvfru1f671WG5hIDDZxMulbEALRC01HzQZeIRc9xtg8D226PP1lnFNu_oBCrw_ZgEU987bZeU0mNlsYWEUqbYd-P-jFg3zJXnGNpog781EklRxvWbLMPgN586R6JG2lPyvqdX00rhQ738b9wvOH_PjVqoDNgGJMRwfmR0smXei2kU-d0sxEl8mxKriW61EYCesqjOpgs04G2xtbA2UO292A0OJj0iJgr6EUVKNV2SS-b3r6rGMpTsMYckEwY2uszoManQG3DE1Cx0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=DHRujNKLdRhiyJH7zws1eL5BNVpWz2qJcnF6Yf5dEhOv0hj4j8MLguGmRWJrWwVwp5nyzAwtlvfru1f671WG5hIDDZxMulbEALRC01HzQZeIRc9xtg8D226PP1lnFNu_oBCrw_ZgEU987bZeU0mNlsYWEUqbYd-P-jFg3zJXnGNpog781EklRxvWbLMPgN586R6JG2lPyvqdX00rhQ738b9wvOH_PjVqoDNgGJMRwfmR0smXei2kU-d0sxEl8mxKriW61EYCesqjOpgs04G2xtbA2UO292A0OJj0iJgr6EUVKNV2SS-b3r6rGMpTsMYckEwY2uszoManQG3DE1Cx0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq54ZwuyqerdkiwsInx35uXWv2b8ry6cHU7WtmoznJ0yV_6ESgrRg8XNe5Kr98F1xM2hNlWGB2QV3qFCe3JWWPqPjnoRMqNvwPoYfE5b-k94ML1xaT9ggu9i8t81iNn1MbaLaCcsfOfYLvCHYMrVQ-74UvTESK7pBaWc3xxVvlUOAVemFN7uWI59S6yyPcW8flJJkq-XHyULZQNd3vi8hA_rcSbqUvlyaQuiToijYJzvJQBluua2_7ZO0P5oSaK9BooqR-i3vAkwHmC9Xj47GMr4NHOZa1WsftSP5ZhOHXx5c8AtNdZ6XvkWNk1UNTmn6cP3fX5FmnBadvWtEdz1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=CAXXhqS_N-F5K0fHBQ-ELZEfyG3beXbLT93-BzTZwPWZs5Ye3KwBwhWHJR6X0lM77GpxemZf6AxY945ILnqf6gxcMni9UBIfejxNj-hLREgBeAlDMJROVF_f_I1n2BoE_w6ElSfEa9T6RwfZKOO4vf0RDPMR4x5jtSP-GTu3hMBufKJeBWVJcls8EbnPGyzb6Y74zO3NSJ8S6nHhhGcJzm3l6UMPeAVn1KbMFOM95ckuCPewqr0L64UnuTbnnSp8zMuYLr7nYo3Pf4LS5ln4ghG1SmXOW8XOJ9CExFClINFgdmNkQEs0ydNKWZmvAeBPOV-X8TSo2UHRUec8IO_Lfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=CAXXhqS_N-F5K0fHBQ-ELZEfyG3beXbLT93-BzTZwPWZs5Ye3KwBwhWHJR6X0lM77GpxemZf6AxY945ILnqf6gxcMni9UBIfejxNj-hLREgBeAlDMJROVF_f_I1n2BoE_w6ElSfEa9T6RwfZKOO4vf0RDPMR4x5jtSP-GTu3hMBufKJeBWVJcls8EbnPGyzb6Y74zO3NSJ8S6nHhhGcJzm3l6UMPeAVn1KbMFOM95ckuCPewqr0L64UnuTbnnSp8zMuYLr7nYo3Pf4LS5ln4ghG1SmXOW8XOJ9CExFClINFgdmNkQEs0ydNKWZmvAeBPOV-X8TSo2UHRUec8IO_Lfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7XlxFz0JrCJzdrI8UANH74Ez0TSk9iYOy7ojCM_ZATwZ-91_IqqPO1ynwQmqVQ2Kcyo89Qw4j0LlF3MD2OyScDJ9VduWRjC0ONwnQ1j-q_xZ-5B5zkNHo7F_FYUp4_Xg7bDqFtk_INmMUE09yVeS34_yiw9vfK1PtVTxJXC2f2c6-f0zTfqPX-t4EF4mGKtIfH2oopcY-hynKyLwAecyLsXMPog6HQKLvspfSFu_doZes1X2a-XwfkczVyUpPII3XaAU7S4Qn2VQ96CjRB1REoYBB77TkchcNuqm8OEctauZ0pOaRwQNCLWo870bWxhgo12sw9itgmZo-v2rCnuAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGGSTdW1N0-SrKoz3eU66Gl98X89J2dySrGsr5JJomuqdCLefZdfD2jGcX-0yOWA9aYKbZTBf4n_VtaJ4-2nCi3IW-CcH6Wsll20A4Q4Z8nPJFyal-P04iPeTg4ip-1IRyhgX6XHC8egca6kPDwLCZ6wEv-WQOE0bGDK7sxQfU5EgMe9Ckqr0X0J1b_cLfhGyjNtHPDJbMawJOF6e895PhhK0WqmOH4vnBezxth0DhFKovppFKgj9Gs_yYrSi8kL5Ug97H7tzN3tgQ4ij_BN1iKSAO6e9q5bUQCM25b-hCkFfog5BQ1C-vsQ33sLHUPQTGWiuMLGDCTfhsfjOsKZNjIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGGSTdW1N0-SrKoz3eU66Gl98X89J2dySrGsr5JJomuqdCLefZdfD2jGcX-0yOWA9aYKbZTBf4n_VtaJ4-2nCi3IW-CcH6Wsll20A4Q4Z8nPJFyal-P04iPeTg4ip-1IRyhgX6XHC8egca6kPDwLCZ6wEv-WQOE0bGDK7sxQfU5EgMe9Ckqr0X0J1b_cLfhGyjNtHPDJbMawJOF6e895PhhK0WqmOH4vnBezxth0DhFKovppFKgj9Gs_yYrSi8kL5Ug97H7tzN3tgQ4ij_BN1iKSAO6e9q5bUQCM25b-hCkFfog5BQ1C-vsQ33sLHUPQTGWiuMLGDCTfhsfjOsKZNjIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=YZzN8UBH-0cugGSoAH1qR175cCzX3lTKziej40d1hJYUNW8HN6-91V1i7rDLCQS8S83wX7cgrZ1_KjwcFwuaY7odkvomafG4OhLfjPX96ChRki823k-5UWPmUhTQTV3OyVRRylJF0Qtd3JdU0swSlniJnP_a_NKfPCuwihuDSRa-hjCCzrDFQLoDY82Gq2Qlkjd8_1k4vSdrFjrbC5cDjHTyK1kqTJGovphoO6xbzv12kqQXEApP__s69gJcW0n6Vitb5kKrAAVso_VH0jZfonUeM_3OuukvgPcTthfnI3H0kZKO-2qTCIRSmgZPYIYqazpc0gLFsSDLiiYcMXOfSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=YZzN8UBH-0cugGSoAH1qR175cCzX3lTKziej40d1hJYUNW8HN6-91V1i7rDLCQS8S83wX7cgrZ1_KjwcFwuaY7odkvomafG4OhLfjPX96ChRki823k-5UWPmUhTQTV3OyVRRylJF0Qtd3JdU0swSlniJnP_a_NKfPCuwihuDSRa-hjCCzrDFQLoDY82Gq2Qlkjd8_1k4vSdrFjrbC5cDjHTyK1kqTJGovphoO6xbzv12kqQXEApP__s69gJcW0n6Vitb5kKrAAVso_VH0jZfonUeM_3OuukvgPcTthfnI3H0kZKO-2qTCIRSmgZPYIYqazpc0gLFsSDLiiYcMXOfSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BZzCp4uU_zZWk_EHBt0Ss4Yr7J1Qd8LwMFq0NDehS5Q1108LD8pktZ8UUKndceusSbqA0FzyXEOvo8CDSC6ZzfIPLGbBOiIRQwYuna4GUbZSRwAmwqPpsu3mKVbB0S3VjPP4PeuaTewbdzSChrnuUXi4lPRQqMjtmPoHqkGigaLpSvOGR00il37SDbJbvCllesAgTVf51vaZGuFJIELSC8UIxi7wcR5TDCcNKCDJE0SGT-UTbg1MKt7lnFfBFlH5qYy_ibPV4vvQFI4DkzH6qzocpew61lZ7fJaxDoO2Ixbf6_uJNL9_kr_kWwZfqN6MIgUw7IdggNpjVWVp6hi3PFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BZzCp4uU_zZWk_EHBt0Ss4Yr7J1Qd8LwMFq0NDehS5Q1108LD8pktZ8UUKndceusSbqA0FzyXEOvo8CDSC6ZzfIPLGbBOiIRQwYuna4GUbZSRwAmwqPpsu3mKVbB0S3VjPP4PeuaTewbdzSChrnuUXi4lPRQqMjtmPoHqkGigaLpSvOGR00il37SDbJbvCllesAgTVf51vaZGuFJIELSC8UIxi7wcR5TDCcNKCDJE0SGT-UTbg1MKt7lnFfBFlH5qYy_ibPV4vvQFI4DkzH6qzocpew61lZ7fJaxDoO2Ixbf6_uJNL9_kr_kWwZfqN6MIgUw7IdggNpjVWVp6hi3PFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTqz_gkiRGpw-klfA5XCL4thsfUhTrdiVH3M_dfh0l37CAVHOVorx0GOaeNB01ZiwHQFAacBM43o58KK_-oh17RF0G4alOxQyNNKaO_qeyq6CzBWncfI2HRR6SCZVxCJ523-ELMKGfaL9N_aCb_SJ0r2eg1Iy0q-DLz2tGgr2LxyzH3uAQ0d8Qot_89PBVuQZQ1FbnLO-COqUZiTwLcnqbXq7m1iX9etnCbDZc89U_6YgfQJ-Mf2nWySdTfw_84Cw-DykqFAK4Hz6E26usVECrcNLRwcrnNXkWWxGHxbuEJSqFxcn7GjcNZW_uxur8NXhWqTW-khDkHsO6eAP-Aakw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgu1yE5aPBs7l2aH2BCcl-lIP0StX9KWzmNdG6jxeVO6NBYfY_iAFW9SgJQbFonwQOrOtvH3ggWBmEAW495D-ic6DvD4niovn7ZGZkPcYa-ehaGX0zh7Grdiyy-p4zCm6QXSmDqtmYBsESB5eL_Rg1Zz74t7r7ixAfv25nwenLH8j1ioiH6japuvF1m6mbyVQzT-TaQu20a6jKuJ05B7qa8vPk4PcaI1qrH0QAmrG0PsC3Pks-Gw3zVNx6EIdwYzqrzPAA7V1UB8K_MjGPytfdzKDMqWTngYhfFIf2YrpCHR8OVYTVKPQgatKDJj6DQtbcqBj4HEvWUcsR_dNYLc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXlz-IBvTyQKforP3nBUxA6wwUK6epob0DqYi4AJkwh1vEn15Rvh4t-eytAnZdgEovWxPXPF3NLLsTcvQ90xtpryKSoIqNf_-T176aM5mEFU29g4N4XtM-Kd5kVF8NVBRQLzuVuDfCG1mLplieE5IT47NJHNNkf2FoVW-JkgAf8cb_zZ8S4mKbT5ts-QeFf3DGBeAqYVM4kPPoDBBkL4yO7Oqzn13OdhQIa1h-UWD2jsQY3NK0QvcRh5Cunz1NWUURkK9L_Uco52N0Wo07l2BMKrfS-saWVcmHJbwyyPsS7eSEi9QBDohU5g5K6bkSzFYo8R3IiEym4h3P7tvhLVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
