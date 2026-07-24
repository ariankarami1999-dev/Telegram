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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 01:03:45</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMTx5dkGl32RMhG-1Hg_CtPAzpfVN27SicsOysr20M_aNLCquCTAtN-gFSbLC-onlxVwNmJMrlK0xifEzyk2wsUcaZW0pUF5FTYD0dJeuty-EFwUlZw5PYG9eQ6oyuaCWjKTQ9tOF4xI8uVayMzIWJhXhpZVLc3Zgi0V1mtIuxuGNfkk3n2KFE5zQBIix0FYskm02ZBXZ4FHoogqjFTyyp8KW2riGk3IG3Q6J98oEE0zNPingE_KCVaCHOXuCMLV4YEta8rNetg-zCZ18LGrjZPGH-NrrFfxsBJlvjhpVY46okXIEx12oo17GXcpQYvzP67av4_q4eoNs3lJ5O83Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzWj-RHZcQYNuZhc6T5HSsYm9HMfRp9bPL51m_SxFRKW2BYnEnWpZ37TpPxZ5JsRBtZR7egTrulWoCFlTZlLN1k8L5hXHU5ClfTavw5T9kjaEekOYOGwVzyS22GneLpDR5zoqXxqY1LBC_DaD_6QRKssMlqfN3byCqf_jJRJgM7rd34UunS8MiY6Ql_PYWWuspShadOJLwFLFbwBRl1ovm_h_im-qcvpcg_yIXnd2zxwefRIIJfLjzcj3x2d6IhRIBCPXE0yjOtonxshRabg06s5mMFAUwztxoqn1rLuSwyO6cN4hLq4bMG1t1rna3cXFjOj5cQajqvCx97xQaGMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpDfhuwUVA7D_vukw--punel5VYWFSWuPlGiBExSYEj--tTFv4eUzPBUX0LQiX_fcPh8G6V9z2nEac9WJzaC-FmE6hFPbLv43Yiz958Qjro4DN7VGFAjTLJh_m8JyODFYYmxAs7Ndio3phyQMKwfIaVFo0lPOpakaRQHWbniwzOfmhex0vrgFyLGvu78C3MAiXupDtA3e6yVXnIQBemQInE5mcqzH3YzNUVZD_CDhL8rHsNCw5YvKr_1CHbf5ul3PDzMktrqT8yKnXB1auS38vTfuLTb8DhGMTPAl9U3pCZCAGfh6NTHF8O5OxL_cAKFcZvZo6m3fU6jmjZQZDl0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfKoV0gTyaCZcUulO6eoMt__181eK1aDzHb7BK9cGQS99Dg907jlT9LXBT2HG0ku32WOusIa_Pj6dOzPabVq0SfCCFquY8ER9KrYh324K6YBX5lYyOKj1HW1lWw_7FEn0AMO4JDzgK7cl5GEUfqMbOGfeVT950G2Psl81WBmNQKy46XVCzBREiCoZfDQ6MmCBPATf_YeGfNcCo6ZvsTK47L9NQG_udQkI37tJ58L1Dk1963XZFgpe1B43bixT7i3WLbQ3efeJBeJlNkR4GhgNJoudo35qIxr7QOSJTo3tdK_D9i6QF-1ZxU09Fig_NlegPDytC2Gz2ULTFlUicMwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=vFISX10nprzOPR1HmYDt_rvUjeNTpkM-Js8EfwRv2Y8iSJ-jr4wbvTm40Ct7JXQ_I1yEhYwbvBxkMvs0CCYmdqsGaIpUHNUgKMOr6kf1kC-Jh5dq9EK2Cs7CLi6BiqvUpejTUKV0bXi9AvIm8abtda3aHY2ckGMK3RDsxA5GnIrp8EA6ZS0X7W9dHmCIQuGXvE3WxK5jA-ir5aXKyR0ozHkE4yoccEH913HxbLBI0YPWcS5gwP-wWqtONhTsToMsR5IEIOz0dNMclC1ITy7D7JJ9YB7qukFkaBaySeQUNCE3g5F8U7httjeb04J4awDVGXZEfedNwqJK517b9GiJsz0N73WV2wx312zyBJKdhyTI9D6VCJyyE8d4RVMoi-rviWxf8kc206bZtGn46nO4hH1XstKUAqieSvGxcoDsi3IAi6QZlQ5wUTRUsSbufHp-IpznHMDnL9IZVmY0wPBcNYy76UzuzS6_wUzG7L1hD3xiz6ofJVFUfuLdKSERERgQT2qJ15Ct2zuWIZwDvv1E8riVBm2PJeY8UuwbGyJmwTWosvEV-GWdT9giR-T6s3MoJGXsngsRSopJ4wCBYB4NUEQZr65jOkZaB-e7e2OFHEgANruGRxHdBl2lDbK9qX5816ZgKHacpdnL86SE354LB1DoUhWv_XlB-XsnYZSeL8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=vFISX10nprzOPR1HmYDt_rvUjeNTpkM-Js8EfwRv2Y8iSJ-jr4wbvTm40Ct7JXQ_I1yEhYwbvBxkMvs0CCYmdqsGaIpUHNUgKMOr6kf1kC-Jh5dq9EK2Cs7CLi6BiqvUpejTUKV0bXi9AvIm8abtda3aHY2ckGMK3RDsxA5GnIrp8EA6ZS0X7W9dHmCIQuGXvE3WxK5jA-ir5aXKyR0ozHkE4yoccEH913HxbLBI0YPWcS5gwP-wWqtONhTsToMsR5IEIOz0dNMclC1ITy7D7JJ9YB7qukFkaBaySeQUNCE3g5F8U7httjeb04J4awDVGXZEfedNwqJK517b9GiJsz0N73WV2wx312zyBJKdhyTI9D6VCJyyE8d4RVMoi-rviWxf8kc206bZtGn46nO4hH1XstKUAqieSvGxcoDsi3IAi6QZlQ5wUTRUsSbufHp-IpznHMDnL9IZVmY0wPBcNYy76UzuzS6_wUzG7L1hD3xiz6ofJVFUfuLdKSERERgQT2qJ15Ct2zuWIZwDvv1E8riVBm2PJeY8UuwbGyJmwTWosvEV-GWdT9giR-T6s3MoJGXsngsRSopJ4wCBYB4NUEQZr65jOkZaB-e7e2OFHEgANruGRxHdBl2lDbK9qX5816ZgKHacpdnL86SE354LB1DoUhWv_XlB-XsnYZSeL8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=YmNa5WPAKPv02tPk-G3hVkJ0wJXJ-Tk--j93SD052AEkLKLh88QMczSRC25Dj-ihLV0g7HKpomnCEL_FuAIhKFoRTZa8aF_2XyArkhY6uw8ELE-E5TS8MZWHf0SZfCwzAy89NJQLsJsOETRQcpge7G1eR_b0Iq_LRDCJ1pJciqaEv0_zTs5zqYyP8V5tw7w8H8a3fyys3E3FAfRqywCUNnH2FCHlFOzhqqiinG4cFj5uSSgrZ9YKPQ6bvxOp3hGDBZbTgH103OvEDeAfN159vuIznUQUFR--Bobb1ZMmjK8LAgBqxYQxj0XbcXVxbZtusR_ZG5Bbv2ZCRJ57cxK89g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=YmNa5WPAKPv02tPk-G3hVkJ0wJXJ-Tk--j93SD052AEkLKLh88QMczSRC25Dj-ihLV0g7HKpomnCEL_FuAIhKFoRTZa8aF_2XyArkhY6uw8ELE-E5TS8MZWHf0SZfCwzAy89NJQLsJsOETRQcpge7G1eR_b0Iq_LRDCJ1pJciqaEv0_zTs5zqYyP8V5tw7w8H8a3fyys3E3FAfRqywCUNnH2FCHlFOzhqqiinG4cFj5uSSgrZ9YKPQ6bvxOp3hGDBZbTgH103OvEDeAfN159vuIznUQUFR--Bobb1ZMmjK8LAgBqxYQxj0XbcXVxbZtusR_ZG5Bbv2ZCRJ57cxK89g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUBXLF-FE2nLrygXKmb68P4zdIsmKikbpAvPhF2SzbT85d0R0ZNWAVEftsFU22HT-o5PkbVK5n7MNJXAugtvqcAwCsbK5bU9VLNjc6EjL71rKFVGfWEClW2UGc5jj0NzrMi0PC7WpRLueldQfTp0n9umNXqTd8dEiXnLThU-jwjQafqk8PMGL792z07qjXcjSvDtuhe73HMDp15n_rrVrQ-Lhax9ES8OpH6K371JOAU7iryUzaNTHMi4qYLH6lzehjUgaEfHj19__yVNF9_VGIV5TDcHVZRFjhfpbF79NXmHS_YlL-BiAJ5wikKTbpI9pU9iJNpIRkc0f1wNoquNuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcwaFjBTK7BxGZ-0lP37wBe_n8iGjXIRY4T66Ki2Nja842pb4KPpQcm2pqo5GneOoqeMv6m9vm7TA4pGQ1Zow8PTNOjx0n8wWXTFDUVZcTQF4d7stSJOf2NU0XYjvO-erGurqb7f8pPHcSgAMsCWK-XR4OoZaUjtJJQIFccxbHgh2HS_rqXARHASv3ufquWGb5mNeZOCOPmOAviIk5xjcrtjWK6iUOKhaFjWKFT26Nx8SSHscJH-9ZrT5zmnDHPxdeV-kxqI-2pjrFsb1-tc4V3849ENGkx2WIa3ovBUP9R3o57qLE2seoulpddPHn1rZn9LJwvwiBQaIQlNLOAeHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6fI0xSFpwx6fRjlVzNYl_tt-TpO9d_2pJJYHwdBasc1pDUKIkc52DU6Jxob99QLvhYoMeCzrCnufXGMM4HDQLMXxEKnss9aioQgi4mzojDgr70ACiYhJLWw0AXUGbGLe8WWtVISzpasDkuNEJJU4HRCuQl6mAgLy8-zY5Ss-OaQHlkaom4yJhMHxm-HT9UXD1P-e4mnvDPOzbRvkW4Qa3-spmPqefSMnFti0WXyIvJrzWCzMS-G5dpq2QC5KnWz0W8Z4I9EXbWz1_N5TDMIlY491p2nmZ3_Hjk6kklugLMLQceaY1ZMCTTC02i6pzn2AHUuwWPr4DgwamLtMkTDWg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=rRQlgzPQtOX8517lCZiXh-T5-OJOYpKkz2bq6oDGuClC6CNWARU9RhhPXBZT0G0-Fhvz93mX7YMqjDF9j8eNfNjPJTtow_1W1TKYBH9jFdTk2vaLZ9dQq5C66CzeuWqXawqNdjbyjwt-xh5YhdVqtZi8YHJZPPuI30oAaA-rXZHW3DFxJZJmJrniphzdxusPLF9BzxjAi4Ou0V_xOwmsrorwFdCVlRDE1DqovQm_GwzRIpb4CfjAA5UhyfPivIMs8vsDmYZvCliixVu1WP30oDQ--IT0GD7RH5kuy4Yhqv4MRiCs4aHIc9VX52WCm-h7pUKRLXs6Irsi9L8JnJInNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=rRQlgzPQtOX8517lCZiXh-T5-OJOYpKkz2bq6oDGuClC6CNWARU9RhhPXBZT0G0-Fhvz93mX7YMqjDF9j8eNfNjPJTtow_1W1TKYBH9jFdTk2vaLZ9dQq5C66CzeuWqXawqNdjbyjwt-xh5YhdVqtZi8YHJZPPuI30oAaA-rXZHW3DFxJZJmJrniphzdxusPLF9BzxjAi4Ou0V_xOwmsrorwFdCVlRDE1DqovQm_GwzRIpb4CfjAA5UhyfPivIMs8vsDmYZvCliixVu1WP30oDQ--IT0GD7RH5kuy4Yhqv4MRiCs4aHIc9VX52WCm-h7pUKRLXs6Irsi9L8JnJInNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqPN2UDd3MRQ-Ak6I3IKH28PjouXfFfquD0Mqxz6_boTIUFrAcmxWYb5fdEQ3W63WM_GofVUl2o3pVLob4txh43rWeby7MGhaWJ0a-BEBy1t-pJUixqwsh0pdl5wkmFYh-lSDxVoUslMp9H1RH_fYcXqn0lxDLgqT_mxU1xxAjCg5yWrx1Wab1mo6H6D8Mdi5PQae2RaZbTUREVtOlWWeMKiMA9Sx0U128_OLJ_6kOnTHzzNEIcgw06ovta9_lh64KGt9nCVtjdqQVhrL-4_BptUjknTTPPYesgLLHwK-1RgMhsjdBgZ6gcubmSe3twxCIO1SsoOjA_27qK6LGCuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQS16lSqcxLpMTzX1zEVgYR1D3TRfbpkjL63gTSsyNTv8wYNEohDn8y57yNYXRRDY1fVKg9PWqnubBDyFlSqe0xgim7OJ0antTdYn9Zz1vT8FaP2_vuAuvEbxdg0SruaxXdy-5bXG-phSsYuDMy4QrjDEUbRwxzVw6DDkpwoSRi49iL_XHwtJQlkZo58SRDbOg5v_CEmlPsrVxNgrBGOcPPizDOVpRpm6pv9Kz-K-Zu3n8tXT6SL2nv-yor2xloluDTZIbMPIRxqCn2J-fVVG_v-NuDogYqReKplmw1w3KpZNwl0KbN-kG9SZh5QZ_yM0285ECKupy_knC6BbKCDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oykXOksgndXfDO6sJlCLTqkR-xFjwGpZBXo35cF1VBvf02sxp7-60yqzgoH8nvXFGYlUtZxKCetDIU6IzlyuYnaO-nAmi8jgzhUG4JRI_DSnejgQpZ8IfH1FSlgu58VWvd0zk-z9sZnY5V6ZMFEogBPQ8sL6AgQVjlXwiYruvDKzh2zEWYmKyUsDlmhe8bFymAMlYmWT7BwyLYw4_4o9bFOSC8uO-cQmKQtqatQffhhvRkxwwIBvSfdS7Djwm45ZIjMiPmpYUO9dGRWF3t7bq9Iw6W4ID6DjZUe3YlSjm0kFXjQH_KH4H1VIaD_a2FCJj0Fy9ZmdhQeH9N77lopI_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqUKxppAun8cAgjdJ1v6kduqjuRjH8lwW9wRuDj7IntZLM6WwVlLU71-oSp3JqZ4Xez65mXrYR5UhIFK0VZx8GBAbt1s2P4b2BhM_s9FwnKYf7FrTGnldsSqEweleNVwuspVDgTCkQljzr6tJtf7hIh9vZ71IwZigKju1OXPed3cgAqIHqYNCU7N6hh7sNAkzn7co-rS-TI14lUegGK-Bt7HrneYxr5dgdgfLQN8XLQ0Jy2IrnenTRzKXcRdf2OUzuLbzqy4JB7CJyhKfvlStEbFgjkFfjjgaa4V8ElGMuk9_4t74qY4JF_5Xi-rmhjp9O1BbboFHty5qUfMyR5Ypw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=PMPQYxTsTJgkNRiJO9DIPzEVHwQAkeUtj1wkP2Bl3ETgLD3KcpwJPqlzp6hw4cxaDQmhQy6tOcs5mO79_ctvsCt-hzxt_8uuoReE6lb_WcEgUTT6QfWAIY5ki6qIDLm2e_RBqnK3TtkxXdmVsWbH0ZPhFArDHriT4fg6sjYwn7ut2Ku7VAb2FgbgXjurTZ_ZS8ig1VM_Xd0_ReuyzZRvktLoRQux4Mk-2XxDqj82NcK9VJtjibEpjMmPp93Qwp0nz5bYlqVSX5Gi7AXNLepvzV61yHwmWQISQfjVmN01yxy06fzdsTXrgjtfyaKXiyIKz9wC-A5gIKtg-1KMnOv7ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=PMPQYxTsTJgkNRiJO9DIPzEVHwQAkeUtj1wkP2Bl3ETgLD3KcpwJPqlzp6hw4cxaDQmhQy6tOcs5mO79_ctvsCt-hzxt_8uuoReE6lb_WcEgUTT6QfWAIY5ki6qIDLm2e_RBqnK3TtkxXdmVsWbH0ZPhFArDHriT4fg6sjYwn7ut2Ku7VAb2FgbgXjurTZ_ZS8ig1VM_Xd0_ReuyzZRvktLoRQux4Mk-2XxDqj82NcK9VJtjibEpjMmPp93Qwp0nz5bYlqVSX5Gi7AXNLepvzV61yHwmWQISQfjVmN01yxy06fzdsTXrgjtfyaKXiyIKz9wC-A5gIKtg-1KMnOv7ejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=NM2vR5AjzdZt9hMtckCEtElXukc7PZFolJ3KfZFiCoH-tsJb-rxv6Q_58qDq_BBxe0YkKdd6f6Df5rxZgMKylngU0WPbX2bj67v-FpOH7DVKWoHdMmhipXQWOPL4WqztAodorbZR7d2rlXsmkXAnr1PKlbCjEI0Nl-o0B7jtnHdWkt3_DkS9PjkhRvk7KX0Cv15Obq6CA2Id5jrbPIhzuM_iZucEjgiKR2yqCvHrPPAOQbhh3_uyKACPWb5TZsX0mUaGp1PealCpQM9yEy-8g1g9IJgkjQLhEYPIVnWSizSla1OSlyf2Vkx00JNETnFhqEQ_vKqKLWsoerkcUdSpoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=NM2vR5AjzdZt9hMtckCEtElXukc7PZFolJ3KfZFiCoH-tsJb-rxv6Q_58qDq_BBxe0YkKdd6f6Df5rxZgMKylngU0WPbX2bj67v-FpOH7DVKWoHdMmhipXQWOPL4WqztAodorbZR7d2rlXsmkXAnr1PKlbCjEI0Nl-o0B7jtnHdWkt3_DkS9PjkhRvk7KX0Cv15Obq6CA2Id5jrbPIhzuM_iZucEjgiKR2yqCvHrPPAOQbhh3_uyKACPWb5TZsX0mUaGp1PealCpQM9yEy-8g1g9IJgkjQLhEYPIVnWSizSla1OSlyf2Vkx00JNETnFhqEQ_vKqKLWsoerkcUdSpoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=vJBVSRQjWttMvEADvlKMci1FYzTikW5_anVc66z__KXVs4hEG7bib5PxoIKegNtuMzojPPJA0dSWXuUZlQokTDfy3wRGMrgjpMRoHRAk4I4BXE9SUBca9krHssziJcSZImBTeF52vkJb5dKnOPwtdep7nDp0Vjf3zfwuZJ73jMycnse9fXhFwt1R2d0Hq0YJAW2Gsiota87cy1Im64YC6v23p9F70q9w4g1ugTzOHFZ2runyN6tZSaVwmOh3kCEfLgaMmIeDQ56QlvbgI4b_qpJ3KGdBvXGxnppJ2T52eQN4jrno-R_C9PqDq4Hfym95sWHXMsaajpHuQ3wzGpQ18w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=vJBVSRQjWttMvEADvlKMci1FYzTikW5_anVc66z__KXVs4hEG7bib5PxoIKegNtuMzojPPJA0dSWXuUZlQokTDfy3wRGMrgjpMRoHRAk4I4BXE9SUBca9krHssziJcSZImBTeF52vkJb5dKnOPwtdep7nDp0Vjf3zfwuZJ73jMycnse9fXhFwt1R2d0Hq0YJAW2Gsiota87cy1Im64YC6v23p9F70q9w4g1ugTzOHFZ2runyN6tZSaVwmOh3kCEfLgaMmIeDQ56QlvbgI4b_qpJ3KGdBvXGxnppJ2T52eQN4jrno-R_C9PqDq4Hfym95sWHXMsaajpHuQ3wzGpQ18w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=eTjNXC38FVZpC5PMPSLzFr5wDz1wbB12iEDDweXVqhNkZ1ViEQTb4-CazVe391nAk4jjJGMM4ErUywpcy7drWZjHkArnBnLr0KMO5Ve4-ZRIYKmObnaWEZoal8EkAnrvSP1KJNulsdeJUmljkNh7ljTeSfKSkLut8DZH3OUf_eLa_gaVFwwPNtwY1RQIg8s4MVprZqJSWrx6mHN4Q03M9blhZdOojJ5jPann6AvgTV7SI2fL1-bMYtXGh5tiUA_CPr-lEj2BTS2K4qECRpKjIg6AYZIV-3Bqt-xTdpMNNaNgjnmCtmm3qLbhyCUlfrRw00HuWbrcIfD7SZrozaHy6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=eTjNXC38FVZpC5PMPSLzFr5wDz1wbB12iEDDweXVqhNkZ1ViEQTb4-CazVe391nAk4jjJGMM4ErUywpcy7drWZjHkArnBnLr0KMO5Ve4-ZRIYKmObnaWEZoal8EkAnrvSP1KJNulsdeJUmljkNh7ljTeSfKSkLut8DZH3OUf_eLa_gaVFwwPNtwY1RQIg8s4MVprZqJSWrx6mHN4Q03M9blhZdOojJ5jPann6AvgTV7SI2fL1-bMYtXGh5tiUA_CPr-lEj2BTS2K4qECRpKjIg6AYZIV-3Bqt-xTdpMNNaNgjnmCtmm3qLbhyCUlfrRw00HuWbrcIfD7SZrozaHy6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=QlMH7KYdVrfMCM9UwPdlVJ0AP6f2-RQqMJyKV-scJK8vREcU4s55gCEzLE6u0qrFW4sDFXfcxNohuxMnwpIxjBI_SaiClXnjJxwfELBF_dZf0GpXPIvk5z2Vfnv_Vl9b0ogE35wuo7r5H_nmetSYgD7ktbhqvqardX0n-tUEJC9e2HpNnk_zZa0FQOJN1ytQ8CPtAezuSjK0DzRnA7sPznJujXqKO39Ak-dDMhNYnJyCO5DPYi9eDCIvC1F2W_wwm05S01vvJY4lPDuRnAZpgSvBc3OTB08uCrE-dDHLmE63IFM2V6OuBXUr4lCJPJO5zIV61ZHhmO6y4fq_tIr9GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=QlMH7KYdVrfMCM9UwPdlVJ0AP6f2-RQqMJyKV-scJK8vREcU4s55gCEzLE6u0qrFW4sDFXfcxNohuxMnwpIxjBI_SaiClXnjJxwfELBF_dZf0GpXPIvk5z2Vfnv_Vl9b0ogE35wuo7r5H_nmetSYgD7ktbhqvqardX0n-tUEJC9e2HpNnk_zZa0FQOJN1ytQ8CPtAezuSjK0DzRnA7sPznJujXqKO39Ak-dDMhNYnJyCO5DPYi9eDCIvC1F2W_wwm05S01vvJY4lPDuRnAZpgSvBc3OTB08uCrE-dDHLmE63IFM2V6OuBXUr4lCJPJO5zIV61ZHhmO6y4fq_tIr9GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=Ej6O-VfVozJYySobpHJEUDH1m5UvlQNsAkMldFL3gk6mq_2NSHW8kq2OtRsgkWdZoDXo7N0eQpVoy4dHQDILtASfyNBzGFntNPN0vTSiG6_UkHFKcgHO-iiGRwadQ1cmxaDfOENi_OpyQ7sBgRY6rPCox8djg2HJCj6jgnHSMaA9pmZ-bdXrALI8eNmEttMgnY2fGOvurzmDcA5gJtXM9NXsToQgBgKUCJkWi5eaDc4HLsjR2_ypEv7oNpopZmc13lB_UNFenr05q3GJV7_B52k1UqXL29x0cdjv-ipIlHtpDXrKFAIkKnS7AnBdgi6qIIhCie8B04Q-93dEr6s_iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=Ej6O-VfVozJYySobpHJEUDH1m5UvlQNsAkMldFL3gk6mq_2NSHW8kq2OtRsgkWdZoDXo7N0eQpVoy4dHQDILtASfyNBzGFntNPN0vTSiG6_UkHFKcgHO-iiGRwadQ1cmxaDfOENi_OpyQ7sBgRY6rPCox8djg2HJCj6jgnHSMaA9pmZ-bdXrALI8eNmEttMgnY2fGOvurzmDcA5gJtXM9NXsToQgBgKUCJkWi5eaDc4HLsjR2_ypEv7oNpopZmc13lB_UNFenr05q3GJV7_B52k1UqXL29x0cdjv-ipIlHtpDXrKFAIkKnS7AnBdgi6qIIhCie8B04Q-93dEr6s_iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=OUiqBhsQIPvzwlmT_Ebva--bjXildGba6r3lAKr9zLe2Gv4U86gddA2ZMEJCZD5vi4sVfl12rsbxdIWJlGSDFwgWTkFmzYPcq_vPMMb5AR_R2qQd_bJIBy17O3wDab3oyFBqoGnOcp3Nl1UMvZl3f0CqDVMb5zKcsWf670Q-t3zlf0kTT5k3Y2AJ_fVMCywWY-gUMvvYK81YzyXftntr14FTM2aRC2y3YzWbo5nxPKCHAk2gM60Opafm9DHnRfQwPFYOD1sHju9TDXXffaF7caHGtMbOwqxOm0woON2Vv4Aq5OCrrvXOsq3xHXSVyw2nrXOAVygAfoAzAk5nPfXBq4H9-1OeuoGF72m2Qdy55B1paapk2aXfTQx39-Khbanyc6IUQqtsHltF-H1mEySnqSKCxoVQWi5LBMBK5FgXhw3avCKs1--Z-rAwOmf-qqBp_7_dvXUVQVzOtv85iaCAwgRPdEei-mGLuPTItz_lvb-HMfOiEpXY-cXxCevn2_CfQ0LUMtGbscDhMQxykPaZjSrw8Rpl217_BCHZIh6Q2zCCoDBAkb3gJ6xKKGES-OKkA_T-F1iOwRCo0R1LIdfmyG3OUVjOQpJH1AzDSHCAOMtoFXIiM5FW_yb5I4lxEe8XVmouVGYpaOmnQqhq_eT3hscN4i_J7Crlc6upfqTyHu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=OUiqBhsQIPvzwlmT_Ebva--bjXildGba6r3lAKr9zLe2Gv4U86gddA2ZMEJCZD5vi4sVfl12rsbxdIWJlGSDFwgWTkFmzYPcq_vPMMb5AR_R2qQd_bJIBy17O3wDab3oyFBqoGnOcp3Nl1UMvZl3f0CqDVMb5zKcsWf670Q-t3zlf0kTT5k3Y2AJ_fVMCywWY-gUMvvYK81YzyXftntr14FTM2aRC2y3YzWbo5nxPKCHAk2gM60Opafm9DHnRfQwPFYOD1sHju9TDXXffaF7caHGtMbOwqxOm0woON2Vv4Aq5OCrrvXOsq3xHXSVyw2nrXOAVygAfoAzAk5nPfXBq4H9-1OeuoGF72m2Qdy55B1paapk2aXfTQx39-Khbanyc6IUQqtsHltF-H1mEySnqSKCxoVQWi5LBMBK5FgXhw3avCKs1--Z-rAwOmf-qqBp_7_dvXUVQVzOtv85iaCAwgRPdEei-mGLuPTItz_lvb-HMfOiEpXY-cXxCevn2_CfQ0LUMtGbscDhMQxykPaZjSrw8Rpl217_BCHZIh6Q2zCCoDBAkb3gJ6xKKGES-OKkA_T-F1iOwRCo0R1LIdfmyG3OUVjOQpJH1AzDSHCAOMtoFXIiM5FW_yb5I4lxEe8XVmouVGYpaOmnQqhq_eT3hscN4i_J7Crlc6upfqTyHu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=MC3MNGTMpoo_Y8FkC7f3OS4lDXgu1f5M8LAJyCna80jbj_MupMsw44uqpm7hUxUXxdrySlG0SbR0G34TBko_pKZWPcvuhkOIXxfLwANPOfpJ9VAj-kCi25LC4PuAx6khQVvK3Wh1-AWXbMEmG2PQorSBC6vU-gb7I0X22AIfNNVXxMg5uFeldPdSunWItC_QDVFrXLgder0DxBcBGsojV9yUbBuhUs9p49nu5kuAJy9qXSIPX1DqSjxANOlAlif0dkcCzZxcnK8D_nYYnLNVlA4pBrSfbKaF9Du3bcIUtvCyoY2MDgoa_E_3JFDLZ466D6JFcuxtoh2j_83bGCQZQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=MC3MNGTMpoo_Y8FkC7f3OS4lDXgu1f5M8LAJyCna80jbj_MupMsw44uqpm7hUxUXxdrySlG0SbR0G34TBko_pKZWPcvuhkOIXxfLwANPOfpJ9VAj-kCi25LC4PuAx6khQVvK3Wh1-AWXbMEmG2PQorSBC6vU-gb7I0X22AIfNNVXxMg5uFeldPdSunWItC_QDVFrXLgder0DxBcBGsojV9yUbBuhUs9p49nu5kuAJy9qXSIPX1DqSjxANOlAlif0dkcCzZxcnK8D_nYYnLNVlA4pBrSfbKaF9Du3bcIUtvCyoY2MDgoa_E_3JFDLZ466D6JFcuxtoh2j_83bGCQZQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejfABpTUin74cbqs3_LtEkMbGRVFqBiFNVV2wHypBwt2yqU26lczemrWLEBykDDF1QiA4cDE62ysSr09EA-GNVp6rYPJG7TalqqB4DJscqW5Rr0sxJLEl512f0xr1oZQ4VVEXd5oq5CwWpNfEBBusItpJePEldMIKZEQrzeRmPK-UEteANl4r31GvihrLm06-JsHD0qid6oOpAgiQgvSYepzy-B0lt9Jk4o0pTlSZ5T4ktyoZlsEJbGjquIR5bbkzyMy1m63bHt4HlXLaSzVVKx8iThUPL7Nl2NcQ7ghpG8_BiiIMnSf4EZuvMl2PpRIGIpP1ykFGS6sZ_Ls5h2xyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQudjiiSDTFAD-Xz_Dj2AAmd5WyWogp2_PcQNFbFjvm-XHgJBVk8GuLr7eOseFf21YAFKavEAXhRF7SCDyA3W4_IVrorC65sXg2Vfx-q3u-h5U1jv4iXqGBOf_776fL4sAGNOEZ5_6LYuJDY5nVg5TW3iT_dqpCKwM_v6VaFdPtjvEu8HJe2TYP57Mfwg6EPmdD0P0cE07ihGkSXd9etCwr9ClG_0KXcbJr8Z_QI0aDv8rIG7qvWFQ7teL9gAncIO4bo3PZvVjM_SZ1_tpkn3f0OHz1QEci0qqIFJusbNbymQMvWPtZGRlsm5HNYr_wKtrAUYcG-GZfDTYtdVrOEkg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=qBkkq7x3TiG-FsfepebegwonMnPe7eNOuR0mGTYePBvtREbDFIPuOM4UR59QtQArPBGMsk_VOqingZUxGAEVFnpXPqhLMjIVhCF1ENXT4BXg6B0DpnRjBuR539Jr0rEH_pRkq5SEyrrG6pjWOKI336muSJqRiym-d0Ol3nqq1gw1D5gUvDSzJryq5q6NOrV-dL1FxftmHOumYpiFaseBRGg0nsdlNN-TBzEg_5upEPasauQy6uTfAlJdaxbhxml-JNLI4Zj5E5bbfWUQBn-i3cbQvqAKOWO0cBT3-SvP52yjminU-GQxpNVPxBaIByiRVGQqYsuapKCFc7olGB4iTRqRnzF8l2JZ06AGEhM23wqIcZH3yrWYxy-HXyVjztDh_MdKxFUNh_UxOWAdPd7n8oZ6nhNRIzOZY7ueoVq6XTQ3q2c_jO8DFTLs646R8OdSAZw7x2oa0pAh5M6AiSFd1ADfAmxsMmZYsfcC_eTK811DozOtrjdemMUuylFjIS5m52jiabcbmgrSRVw-KhKtxL6QaE6qBypyD6Ifjpzgz--0jQf9G636n-E_qkxZMMi3fs9jAs9tdqEzfebFAKOz0__uo4a2EQwknVIuVjaV_OXs3kJn6mqDZfP5PeTsb1yAPKfJK5f8Ayd6si3OcFhqT6NpbR5VF71Z-7iRIUz_GUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=qBkkq7x3TiG-FsfepebegwonMnPe7eNOuR0mGTYePBvtREbDFIPuOM4UR59QtQArPBGMsk_VOqingZUxGAEVFnpXPqhLMjIVhCF1ENXT4BXg6B0DpnRjBuR539Jr0rEH_pRkq5SEyrrG6pjWOKI336muSJqRiym-d0Ol3nqq1gw1D5gUvDSzJryq5q6NOrV-dL1FxftmHOumYpiFaseBRGg0nsdlNN-TBzEg_5upEPasauQy6uTfAlJdaxbhxml-JNLI4Zj5E5bbfWUQBn-i3cbQvqAKOWO0cBT3-SvP52yjminU-GQxpNVPxBaIByiRVGQqYsuapKCFc7olGB4iTRqRnzF8l2JZ06AGEhM23wqIcZH3yrWYxy-HXyVjztDh_MdKxFUNh_UxOWAdPd7n8oZ6nhNRIzOZY7ueoVq6XTQ3q2c_jO8DFTLs646R8OdSAZw7x2oa0pAh5M6AiSFd1ADfAmxsMmZYsfcC_eTK811DozOtrjdemMUuylFjIS5m52jiabcbmgrSRVw-KhKtxL6QaE6qBypyD6Ifjpzgz--0jQf9G636n-E_qkxZMMi3fs9jAs9tdqEzfebFAKOz0__uo4a2EQwknVIuVjaV_OXs3kJn6mqDZfP5PeTsb1yAPKfJK5f8Ayd6si3OcFhqT6NpbR5VF71Z-7iRIUz_GUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBviaVhpLGsTP9ygh5X7rIa6yPM1FOWeO_Tp8e-NlGiNIb1caImRHmqm_fBHVFlasKMkd6VNmxwV8qBIGeCzI-iI_whP66KKPTSmz0R6xJ6lLl3EJYEGNfnxk2QnlOPtWhVtxA2oahFhhHfA9zmvxq-9KW-3osC0gquCrvI1QsjXtS-3HuwsXWNe6f1VtbU9Qz97P9cqLYxvcuMpoU537dQ0Zdwt48PfV_6E6YZZc7vH6q-hsoDyd4nxC8st5h4zhWl_srYUsZf6KpSbbAZTNbZrBD8eJ3-q5DDwoURHABwmtXofWT7ip4HKJMTsiyrjRI8IukhZU61TmRoGqqlIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOlbUX7wU9JJ6c_PDWYphcTr-TyxrS9e79iX5TEq_b1i0Z6N5Kh0NaUj6TGv-FM2hEvAhJE2jUa1vRxkfx97HSnxwbUj6JLbtfj8TqRjKqRmchInRPWA2ynkLMITE4aGL7AlhJUhLdPRNJXSeeFXQpftm2-Vp2Zbs5tdJr4UwRfhplPeBVKYypCPQvmoMtr5BDo50Co1zVWBsWC5OPv2KcJm8bS_42ZY8QbQxs-J-hmRiiLta6u7pXclFlJprT-aaN6VtFCLHeulyucK3nwHzB-7_-f9GMRQAaA2n_0EEmzpI6lQiloB2YNzmaTjiCrkpK8Zrr3g0qRGgf2cEmvXSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFjH920ctdsSE4sWJToBPf4pODfq48uv2SK4bBHsfX7qqXx3riZDmXP4q_yPLgWbyf8ovP02NAhgQAXdlTBXQYjsEh22CuIxM2Q_NO6VwQrCYGq8HxhyjMO8ExIWLkc_NKiKc1wuUPBdJ3-fbFM4Xw41vQOLsMeWIa24XtWmIK2_u80qWusfsosh753rb7Kc3A8i-kWarn5M6KKto3URt0z4w584lPBa3Es_t4rikOIt88PCfpnKBRsj96epnr-ggxMgKtExccl_vQQNU3VuzBfFk92p-xtBCGhIDAmGyt4YHMV-RxvqdW6Zs1bRZ3zbP8aqMzeILtSbEwPL3gbbmg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=W-hjz8RtvNtHXaJySKkhH8zOU1FMRsAoxtJgaf4Wf8qu966lf9iqWQoyGBFw3Kv0Sqe7KrbyN-b16K9_0z9LCWyCTpVphqOEcZna29SNNcsEDjJTRNcCZ30smwdjtAoNBv3MYjob5q0Hpt1JifdC68e95_ksaAzNY9d3MT2kVzd-uvJolrgnn_phbT0APFJSdOoo6lMRx2OaQbU03d2Z4u6tJ3Rt_2AnOJ7zrKGmffCh60e5KngvstaRIr8Rmk56T5Nuc9-fGtO-bmjOAyAowqd6QvvJsLEkgZK3_bZvAASpSupVr9vygHw0JQ2m6BsuvtY3zQqDsZpkuUVGTZSmdjoO4Gb0YgP60k9d1QPhSv69MbBe6fprqgkdOpBVG11nnSuyi15P5uhSHHblQ2HSoOOBi2FaWQTLbFWMUl0gfBMnZ33mVhgw6GDiyqCH_AZcrOpnGqift-edt_Jra8CwG2YRuwstb_oRGIlknLzyOiqmCEx-mz1KXaM6_trvxZh7kJ70qNM7Sf8HvKra_QhT8B7D-rnjJLAKxQbwxfMDoG5Uk9EmwpOxRYlBXo8MkvmGN79jU9qHY1cPfT_E2lhM16nfNYoTpRT8HOwZ8n8FYabrLFamPrwgLaWhpRCYevCVSDfhiQ2PSxIDB0zD2KRcNoA6ms310__h59x-oDGb7bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=W-hjz8RtvNtHXaJySKkhH8zOU1FMRsAoxtJgaf4Wf8qu966lf9iqWQoyGBFw3Kv0Sqe7KrbyN-b16K9_0z9LCWyCTpVphqOEcZna29SNNcsEDjJTRNcCZ30smwdjtAoNBv3MYjob5q0Hpt1JifdC68e95_ksaAzNY9d3MT2kVzd-uvJolrgnn_phbT0APFJSdOoo6lMRx2OaQbU03d2Z4u6tJ3Rt_2AnOJ7zrKGmffCh60e5KngvstaRIr8Rmk56T5Nuc9-fGtO-bmjOAyAowqd6QvvJsLEkgZK3_bZvAASpSupVr9vygHw0JQ2m6BsuvtY3zQqDsZpkuUVGTZSmdjoO4Gb0YgP60k9d1QPhSv69MbBe6fprqgkdOpBVG11nnSuyi15P5uhSHHblQ2HSoOOBi2FaWQTLbFWMUl0gfBMnZ33mVhgw6GDiyqCH_AZcrOpnGqift-edt_Jra8CwG2YRuwstb_oRGIlknLzyOiqmCEx-mz1KXaM6_trvxZh7kJ70qNM7Sf8HvKra_QhT8B7D-rnjJLAKxQbwxfMDoG5Uk9EmwpOxRYlBXo8MkvmGN79jU9qHY1cPfT_E2lhM16nfNYoTpRT8HOwZ8n8FYabrLFamPrwgLaWhpRCYevCVSDfhiQ2PSxIDB0zD2KRcNoA6ms310__h59x-oDGb7bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=KPQ8YnVZ3xHQIkovkiVokgFKXPq-kFGMFvMx52B9GKVj2wPa1VnCyEaQK3crm521dk2ETsThX_P4-KozW_ROrXRleQIMDDs9Ivni3Kk8W4YFIiHNq_VAYB_mjsfR2jwW6gIwMWhqMXYnyiAttTk0dv-3PZ1W6No9gSKEq8RiD7LUhyQ6DoJoatg66Ihrin8zNiOmnpuhaVYGbNJyFSmgAsH0AXYXrrbqEFPzjgi3Pl5cQVs7ol_bHxb6bSLSe0furbLRxUvTu7EUMvfcGI7u2wKBlCuslN4kCk2fbQqdBN1wM-o3F7GBSbb_1NWjfFpKOYKy8lhBOXQe7KgzeAxwuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=KPQ8YnVZ3xHQIkovkiVokgFKXPq-kFGMFvMx52B9GKVj2wPa1VnCyEaQK3crm521dk2ETsThX_P4-KozW_ROrXRleQIMDDs9Ivni3Kk8W4YFIiHNq_VAYB_mjsfR2jwW6gIwMWhqMXYnyiAttTk0dv-3PZ1W6No9gSKEq8RiD7LUhyQ6DoJoatg66Ihrin8zNiOmnpuhaVYGbNJyFSmgAsH0AXYXrrbqEFPzjgi3Pl5cQVs7ol_bHxb6bSLSe0furbLRxUvTu7EUMvfcGI7u2wKBlCuslN4kCk2fbQqdBN1wM-o3F7GBSbb_1NWjfFpKOYKy8lhBOXQe7KgzeAxwuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1WItR58KV9eMy22BQXmpjM3cSa8nJgu0EL2lQuJ2wK006sYGIVhnrZG3_JYuUShZQFVYbbJ07SwQPI1P8WA4zvrE8YrXosY7cglq-jgg_gEw4i9kxG-_dTjnlDC_NPlVC4X5CvSr5eiO8cTO65cHJqhHFXuu7lmpAAWEor5Lmtxfg4xu0AGCnGKijaPsDhhTxHgyJ2E4o5JMVH5s1dfqB-CrUn0OWu3ZjZ_ENL-X3Wie4tp0CxnwXwC-sO89c0qHBhuYaiH94-1x9pKkg4z-mEdB-w1X9C97C-TIH0b7aWKe8J4S5xLC5TRDOlW8o48lQZS8mDyBAJgGCX8XD6mVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXCaImuEOAYBBfgdh9wfBO8l_793RPzhX9e21_rx4gZpQhb3tm_wwu_DNfw_9_KfNj-CIx9CmbmQsXcztEDFDZm9NW3BWYRAkTVLP39Q-0mxxcQQwZ9U0LFqSWMxfyNGQzc1Nfdtg1g5Ugmu7ppih7a78vful9N83jLw3rPdogPBjC8mXUtKrlkc8oQBQGdUjUUMMWHsxJIl8U65Id83gyYYC8M_9-8TpnKB9fOacuwlC4ACiJutjVWJkhiOvq5oJq2GahBJvESkjo8rMjNPMBEjPwue3FmZLnm_wJE6VJ-m6nMN6fPzJqKlVO26ZGCH_LyD27tETKmV3nHElqrLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/amOjVel2NymCkFX3pIVPaNw-6BEamZUO69FWjFX7JWb2G2fPY7NyMAgGWaIe8E0M4XeDTPAqRyJyYuZx8M8iABUIKQA8ety6INf9eIHKjnFIdPCCz4NPDHQsKnsHIwEnf5frrHN2O0ZtQWtMQ5xkFkgoy0OWnu4xE_qtlyH7RtyFfHk3JPn-ogZL606qfPjgmpJg5TGZ8L_JZ8uBIHLnaA2XT9JHX0y8P0rQOTqaVxBAB_nLbx_DrrlTCg2WKiVYPrkKdvb2Av-zkM1iwS-3VwDBYiHNfKSv6VblpC_MYQs_rUgM-qYTSHXjZLhOu92gofbVIejJ2rsbEeUMVg71Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/scK1maJZ-2UI4-Ng38S7bMw5awxeXbkCWJyJUbZqPHfYwN6TomSAFYfyZzJgBY1qXn5qY0E7yrbrXyhVlnuwddBOpOrTAeUpDw1Z_5iGmSkjNWs8SVVoqI1L3dIXxe2bBGqCQlf9n6nNRYlnJyYoFVg0oeAfDzi4kVfcY2g2t6bk7_0xCZnS25AGGszNdvijsj1A5btoGSfVMnu-hD76Bh_YiWWepQ7FJcQBuxMFhtBuKd9gfMWw3xNjBkdaz3rP27c46Vxf5mFS-sfMnHEXuaDu1iuKA4wqepTdx1sv3m3-rJjYGc6MWTGo3JNutg_QBmv-EmqX1Q3upmk3AY39Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkJltOc2ckM6mnyFLFjiBvPBPfo_xGj8azEwaUjjbxGBrcJDCg3oJNN6BArdIg9KKpful74IxdRvBDh_oxPjtfLsNvkv9Dj4bntIMQuskFG6TOgFRk3MExdBupqAcnEy6QFnmrqmRF2-n1rcnzu6gAKU7qwFRRsUo1KnNGyA05PkA-cqlW3g8PItLRoKushh7TXc5Yd4b_QUYg6ADaGDh-I9SmO4YxIN0XsxB5Ka319N3n-Rk-XgFi8xKt2tfcwQ5X0lce_WJXjgehmPXJyzLOmbMaFogUCnr2XoG3om4Mk3Csk-dpyHE9GrR3ToPzCiadktBxMATiqlO6GlhLyPpw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=qoNs__LyntVu_QEe2vuzotZi2VpyrTJqmMTDnPK4grZl8TGll6F6VU6ktapYtdMzPP3eT_lQSPYrIAhnwHx6MPxLiGS1JZZoK_OcR5kBf84qRRZ_0vkYnGW_XA39TY7fWWsEa4Ym7MTfkHvfWQ_g0u7xRtO9uR_Nd6YbNnPMAHJ3o3GRjskmmHk-kl_nS0XOIEtidf0bwrhmIe-IOBuN8rycXun4vd05Q7z535noYR7B-qjL7VIkfUzrzy3ab70bu3nn11JHYMM07xCLRHJsfpbf7H4YPbgmacfK_Yb6W5kWa2oG0I_rUkk0-eiHJw6cEg1MkAOEX3P3OpuoH65Xyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=qoNs__LyntVu_QEe2vuzotZi2VpyrTJqmMTDnPK4grZl8TGll6F6VU6ktapYtdMzPP3eT_lQSPYrIAhnwHx6MPxLiGS1JZZoK_OcR5kBf84qRRZ_0vkYnGW_XA39TY7fWWsEa4Ym7MTfkHvfWQ_g0u7xRtO9uR_Nd6YbNnPMAHJ3o3GRjskmmHk-kl_nS0XOIEtidf0bwrhmIe-IOBuN8rycXun4vd05Q7z535noYR7B-qjL7VIkfUzrzy3ab70bu3nn11JHYMM07xCLRHJsfpbf7H4YPbgmacfK_Yb6W5kWa2oG0I_rUkk0-eiHJw6cEg1MkAOEX3P3OpuoH65Xyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdX7VQudYv8XsyIv6uzRpuNkwKCBH-ym_VTPH5OVX_TzgOfKGs9G1YxuG3xZuxnYGImqzU4iKkT9uxCgFqQZeA9bFCuBJoBfp2lIdz7nCc3OANPZReQDQa92laQrnpVLgM-rYy6NWl8iGGcsgWb4j49b829SMXSYsOEeNgOqElzgB-qXdt0o-oBAirelHtstoKh_wu0IfGoMNPiifnZE4Lmvo2pMAwkdfU0ypQ2EDHjklmOZhKfgrkWvci7uzi3LLK0RYSP6kOjEkXzZuDOIZnSi0B8eqcVWPVmVCqJ1_EkanRmobe_DSHLNGva3ewyCrGgTVtePkJN7KxsWBZhMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=gTnzphIdMiiV9ilP3khwa10bbjZ7Jk0QE0IqpsFP7F2vtlxG-xFT0waO7L0ZmVyjVA6XMj68uDitEqnlnGJW9PshCm_To6CjIf-CAU_rZDjAtFalNOWTGGHSnztep5TCCPdQHTVMyn0krra_wDgUsajKLlJs0zqJX0bw9ZZy2WEbr_Uoa5ebO8hCAainGammafyWhBKULktL-TYrOLdLQMTRiKzdSFJxxgHoln5jvihApXOOm4RLz_nszVjUP-tolRqr1nTdLD2v-IoADruqEahSkfJD3ZI2Kn-Wr_T5xStrWygaNxDoNu8mSNJrrSB_OHDsVmmskdfJTEGaZMJ-Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=gTnzphIdMiiV9ilP3khwa10bbjZ7Jk0QE0IqpsFP7F2vtlxG-xFT0waO7L0ZmVyjVA6XMj68uDitEqnlnGJW9PshCm_To6CjIf-CAU_rZDjAtFalNOWTGGHSnztep5TCCPdQHTVMyn0krra_wDgUsajKLlJs0zqJX0bw9ZZy2WEbr_Uoa5ebO8hCAainGammafyWhBKULktL-TYrOLdLQMTRiKzdSFJxxgHoln5jvihApXOOm4RLz_nszVjUP-tolRqr1nTdLD2v-IoADruqEahSkfJD3ZI2Kn-Wr_T5xStrWygaNxDoNu8mSNJrrSB_OHDsVmmskdfJTEGaZMJ-Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1WPYSjUbBm9Kk4hxZsNHBconJM2EAXPSOfvLLV3hcD4IgbOvt9NTvH4bCbAtdChRGVm1OIoouXPh3hg-pg7qCYBHzKSACHrPSK_6Entoupjbz1PBwCEdnej6z_bNDW9X0pr92kNhc-fhJLdfkc6mugDsoPZPb84gRkVSgPkgo1-8jWUqzoNgsYpKpULkqH4spv-G8UTCCLnfU64_oLzzTV_hHp68tt3gw1-iMaCitqim16uvsN_1pKQQHip26ttp4ecdwaqEAMdp8dCylBJz4hCaxF8fB5DpKWd81AlHG-DMoQYT7g9z8VyyqtI0wHLWwgDqwrV7AsSzu8t3b65PA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGJy9s7qXBKv-3mE9i5e4tEgZGXAxO9pHL_hTU_czRx1_Bh6PnUxXVUNCiUih5bgw4osXoKcN4Bo0yeUI5mPQAWBniRn6Azm2fjGQrIz-r_IKZLJrA7QC3FzA5LVLKK2dp_XkDQJiY3i6BF6Kuwfre3eXGr4bgDx4RVlKplc2_5ldd-qJkYhKYQWbk1gjGZmE8XsYJoH-ZZNycNXlnONmkBCQcRvTnL0dZ-0Yhlf6KUivQEkcuKXBfxUvcv-FvqFLrxXvTRv8xbfuj0rZaJIZBtZ9sC9Qj1tEh8HUwfCOTxIJzVw8ruie3CiZCbX7doNJT4Vq75WMmjT1Qxg5UK6qoaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGJy9s7qXBKv-3mE9i5e4tEgZGXAxO9pHL_hTU_czRx1_Bh6PnUxXVUNCiUih5bgw4osXoKcN4Bo0yeUI5mPQAWBniRn6Azm2fjGQrIz-r_IKZLJrA7QC3FzA5LVLKK2dp_XkDQJiY3i6BF6Kuwfre3eXGr4bgDx4RVlKplc2_5ldd-qJkYhKYQWbk1gjGZmE8XsYJoH-ZZNycNXlnONmkBCQcRvTnL0dZ-0Yhlf6KUivQEkcuKXBfxUvcv-FvqFLrxXvTRv8xbfuj0rZaJIZBtZ9sC9Qj1tEh8HUwfCOTxIJzVw8ruie3CiZCbX7doNJT4Vq75WMmjT1Qxg5UK6qoaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=wCXMjHXYE9lqENznFwzSonWTkG70X8oOXc2C5SO7oX11f-A_e9_WjoUEpksOYDXd2ErPnanJmWz8LB9wTfN2_fV7ZwR87nOk91hM-Ic8gQ-6OSEvzpRysbGKk9cQIXOOtZ0NnwlNh75gPMqq1hmFZTNPX_u0dF6gBvneLS2MYNRq4hUK1zna6VGpw_zbFhbW6GLWZ3n_Kr29JSOdAIHsu5L3DR__E6bZombqwVAM-cryeeekGWF2H00IYtpwRKWNd7oBz7UOya0zFYWDzwIbJ8spvxkTjnskF1D7TkmkZ2P8-I3gVQ0_ip_60kspDjTTjr_rry1_ih522yqysxKBWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=wCXMjHXYE9lqENznFwzSonWTkG70X8oOXc2C5SO7oX11f-A_e9_WjoUEpksOYDXd2ErPnanJmWz8LB9wTfN2_fV7ZwR87nOk91hM-Ic8gQ-6OSEvzpRysbGKk9cQIXOOtZ0NnwlNh75gPMqq1hmFZTNPX_u0dF6gBvneLS2MYNRq4hUK1zna6VGpw_zbFhbW6GLWZ3n_Kr29JSOdAIHsu5L3DR__E6bZombqwVAM-cryeeekGWF2H00IYtpwRKWNd7oBz7UOya0zFYWDzwIbJ8spvxkTjnskF1D7TkmkZ2P8-I3gVQ0_ip_60kspDjTTjr_rry1_ih522yqysxKBWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BUDQPPu1pAhgoAcxfiMsXFF9w6D8sBfLOrLCdVC54oDt3TaY09Agd8L4xiENZxghCneoiVNCSe-uMLo-Xzz3ZjQiUivrw9qbiA7y-5w91M5491gRrXtdl3GK9cY2vOJZWWIdGnJ8OsbqEZ-upXCHaWZ37Wf5QdteBYUZw0DnxlOAxmACAhabG0uuoFGref6NyB8hZ4SXHOqFdST-K8jRUL6-z8r5dGQLQdg1Bor-XpmdtDQ1h-8CcMjvskP0fz5qBC1pDhCsNixgQNBTmNnBseUTwUGxuxO7DsZSlB2VX1IrGKuDExjFmHTESI7yECQSM4dkxgjoRiYteVdcfTIlEFE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BUDQPPu1pAhgoAcxfiMsXFF9w6D8sBfLOrLCdVC54oDt3TaY09Agd8L4xiENZxghCneoiVNCSe-uMLo-Xzz3ZjQiUivrw9qbiA7y-5w91M5491gRrXtdl3GK9cY2vOJZWWIdGnJ8OsbqEZ-upXCHaWZ37Wf5QdteBYUZw0DnxlOAxmACAhabG0uuoFGref6NyB8hZ4SXHOqFdST-K8jRUL6-z8r5dGQLQdg1Bor-XpmdtDQ1h-8CcMjvskP0fz5qBC1pDhCsNixgQNBTmNnBseUTwUGxuxO7DsZSlB2VX1IrGKuDExjFmHTESI7yECQSM4dkxgjoRiYteVdcfTIlEFE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaRyb-kEk8UggcpSErtRR5bMDNMCmgRRs9HWeNHXBiL7SUUxRsLXWMfxXzia6Oc6HKbIbHMLvH0vsfSqZ61wmLkPkTZR-Udvu2aFUsB2PlTeB-jE5oJ7oKi2U2zKOKTeMrBC_GrWnkWsAPwnfvt6KAUPk7SDHsoetvTen09ZARIK7sFWT_J1DU81-wnSWxQKPXXZNcEwfgRPssFu4prw_k3rurOiuoTRcNhjCvupot4GLu4IGpgaquTY8gFZCFtasgFiK-7Cmoefz0ZM0Y0fXmHzk6Ya77ByOweqRYlZ98pBl-UL8goDtxvVMYZKIx2iU0TWxLORUr_H6iW49h_D0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1doAeJJcnPFKeIas23Fd1WaUgVES1SIaZiaLPbO3JEFk3XLQ-eaXQaS_SLOH1T4MtuFSZsaWBoSHpbnmUmIGLvfKXhpojfhTquiijoLv97VWJ1uPDD4ipMNS4L5GHGo_OLrX2L_oaT1saE78HBQvvzDUQq6JKCOPbAqka5K0eaXbbusRQxyUTUMxDPmVblWoLd5P8e-Ua84USrHhkylShamCd6jPFy3ozf2ID8XwNR7o4Yi6ebihoqNa944HjmJN66Vippq6La3_o0Fl6VZEWnI3MocE_T9NTBdpoaMQEu8EI7cOxv5F7Wwsw4h6E563qcABGPjoEd-GxeA5xFpWg.jpg" alt="photo" loading="lazy"/></div>
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
