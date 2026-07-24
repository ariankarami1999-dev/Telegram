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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 23:41:34</div>
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
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMTx5dkGl32RMhG-1Hg_CtPAzpfVN27SicsOysr20M_aNLCquCTAtN-gFSbLC-onlxVwNmJMrlK0xifEzyk2wsUcaZW0pUF5FTYD0dJeuty-EFwUlZw5PYG9eQ6oyuaCWjKTQ9tOF4xI8uVayMzIWJhXhpZVLc3Zgi0V1mtIuxuGNfkk3n2KFE5zQBIix0FYskm02ZBXZ4FHoogqjFTyyp8KW2riGk3IG3Q6J98oEE0zNPingE_KCVaCHOXuCMLV4YEta8rNetg-zCZ18LGrjZPGH-NrrFfxsBJlvjhpVY46okXIEx12oo17GXcpQYvzP67av4_q4eoNs3lJ5O83Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzWj-RHZcQYNuZhc6T5HSsYm9HMfRp9bPL51m_SxFRKW2BYnEnWpZ37TpPxZ5JsRBtZR7egTrulWoCFlTZlLN1k8L5hXHU5ClfTavw5T9kjaEekOYOGwVzyS22GneLpDR5zoqXxqY1LBC_DaD_6QRKssMlqfN3byCqf_jJRJgM7rd34UunS8MiY6Ql_PYWWuspShadOJLwFLFbwBRl1ovm_h_im-qcvpcg_yIXnd2zxwefRIIJfLjzcj3x2d6IhRIBCPXE0yjOtonxshRabg06s5mMFAUwztxoqn1rLuSwyO6cN4hLq4bMG1t1rna3cXFjOj5cQajqvCx97xQaGMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_hUx6gbujC3qprdCt_6yC_b_CSMG6P-1sFP4dQpKW1CBMD5UtFXrQvNYkIg3MaHL9_pfH6lyMvxH0bVbgf3ajT6Nnz4tEwxeMaimbWGiw6NEoaqMJTG2ongqb1lFDn2PwUu8X3G7NKJDBHCSxUnCdiFCgIZuvGQKtPvWQJsTvhOdDL08GL4lRtnPP9x50JaheMvmkr4vJhsO5KBqWtbZf0MVoRB429qaoOKVHm_zKn0D6Avy_wa6-rCzMs9bUK5Z7XbA_b5CWvZ_ybXEYc1avItcosduJkz1eTk6f7Xaq0dw7szeOmaqSIlVqCrwW0J2Qt5BbElHSHnmR6nVXjSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpDfhuwUVA7D_vukw--punel5VYWFSWuPlGiBExSYEj--tTFv4eUzPBUX0LQiX_fcPh8G6V9z2nEac9WJzaC-FmE6hFPbLv43Yiz958Qjro4DN7VGFAjTLJh_m8JyODFYYmxAs7Ndio3phyQMKwfIaVFo0lPOpakaRQHWbniwzOfmhex0vrgFyLGvu78C3MAiXupDtA3e6yVXnIQBemQInE5mcqzH3YzNUVZD_CDhL8rHsNCw5YvKr_1CHbf5ul3PDzMktrqT8yKnXB1auS38vTfuLTb8DhGMTPAl9U3pCZCAGfh6NTHF8O5OxL_cAKFcZvZo6m3fU6jmjZQZDl0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfKoV0gTyaCZcUulO6eoMt__181eK1aDzHb7BK9cGQS99Dg907jlT9LXBT2HG0ku32WOusIa_Pj6dOzPabVq0SfCCFquY8ER9KrYh324K6YBX5lYyOKj1HW1lWw_7FEn0AMO4JDzgK7cl5GEUfqMbOGfeVT950G2Psl81WBmNQKy46XVCzBREiCoZfDQ6MmCBPATf_YeGfNcCo6ZvsTK47L9NQG_udQkI37tJ58L1Dk1963XZFgpe1B43bixT7i3WLbQ3efeJBeJlNkR4GhgNJoudo35qIxr7QOSJTo3tdK_D9i6QF-1ZxU09Fig_NlegPDytC2Gz2ULTFlUicMwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5e6gqbtaiqMLDiAyunn8kGz9PU50p1SfNlg_8YwUXnAziW7g5Lp7WuEV5a9co26Z1tjMHKfOd-jvlLsX8k-g9ROoEIsGtRNc8Lf83BK5pGAMM5BjkAYVVc56kJcvr6IuD5E8uZuuhLcs32NzfDixg3y5JIWR4Wa_dsb817afol8ynVHpT446yvtiN5t3dmmIpcgmITUX8IlNT7DC3coSXOIowRxQ6s5-Z6deNba7QHPuacfbzo5xMwFImI4EegyokZOGZs4S7x5pZK9_0PgJ33_0M3hNeKd44zIQrwHj0SqAvil4VCQxf2oNAvbm3b-c2hApfwDttlBIIRhs4SVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=domW_DRolubZ6mYRbhUj6swp4i6D3KnyMZnqGXQxKRLTpBjmBymusiEqBri-eHk_jJzazMbWiFN4UXhY76Gqk_hRgrUPULn4_n5igXDX5dHdJ8KOaqEqVAmVIExm8zX-peRsJ80_9IYRnTBnM5zw-WcEUAuj2Kso_Og_Bh1aPNT37PJFKPJIoS-UeI5lcwudv_-iLQ6BAfBGT4C4_m4MUBxgHPAyaoC3C6QJyp9vrg-FaBEXrfIMG8PFYTs2pHb8Eor0xTXPDMlt3-Q_swJU9gD-7z_o59-mom9DN1y-YA60_LqCdEMyPeRTvLDCeMe0fct3esHVrZ3FqvYPOIkzjnKug__vY7AaoONtFVtPfj1pv7bnfkgkTZMzMmyPqSf8dSSMApc2TXl2UyividGkoz10pESq2KwbS3BFAkwkI9N9rok5YrlN2IFwUr_cRG-zXwY7ZSbwmzTMoJspZaJkBRh1VTf_u9YTTeiCIghkIwPwb3mblOFAmRrooeCcI3zufY817F_iy72aXRtCT5VRbhMTqO6vKVH0pn7S6v5kPfP5Urv3h8mHgsKEQxdbvXmXIxQ-BPtquDMUF9lrEUpdbnw_vb3j02yqK2P2cew0a1YI2kaovd3eII8yx82fRBAKJx9EG3GFJVZ72_owHCxhEji2wUBvv6YdJh6k15u4Yss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=domW_DRolubZ6mYRbhUj6swp4i6D3KnyMZnqGXQxKRLTpBjmBymusiEqBri-eHk_jJzazMbWiFN4UXhY76Gqk_hRgrUPULn4_n5igXDX5dHdJ8KOaqEqVAmVIExm8zX-peRsJ80_9IYRnTBnM5zw-WcEUAuj2Kso_Og_Bh1aPNT37PJFKPJIoS-UeI5lcwudv_-iLQ6BAfBGT4C4_m4MUBxgHPAyaoC3C6QJyp9vrg-FaBEXrfIMG8PFYTs2pHb8Eor0xTXPDMlt3-Q_swJU9gD-7z_o59-mom9DN1y-YA60_LqCdEMyPeRTvLDCeMe0fct3esHVrZ3FqvYPOIkzjnKug__vY7AaoONtFVtPfj1pv7bnfkgkTZMzMmyPqSf8dSSMApc2TXl2UyividGkoz10pESq2KwbS3BFAkwkI9N9rok5YrlN2IFwUr_cRG-zXwY7ZSbwmzTMoJspZaJkBRh1VTf_u9YTTeiCIghkIwPwb3mblOFAmRrooeCcI3zufY817F_iy72aXRtCT5VRbhMTqO6vKVH0pn7S6v5kPfP5Urv3h8mHgsKEQxdbvXmXIxQ-BPtquDMUF9lrEUpdbnw_vb3j02yqK2P2cew0a1YI2kaovd3eII8yx82fRBAKJx9EG3GFJVZ72_owHCxhEji2wUBvv6YdJh6k15u4Yss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=ejyAEmOKaGOudvo9-0DFdF1FV_rKFL2rHHYYVfJJ9lcWQs3xepbcf89RLR8M9CD7efNvDqhbUkzdaN5vw8Y_pu374subBBW_gd0BO6Vn0gl0468YeetJl_FkeYC6uW6SH8xDZUZm7AA4tBJCtMYnYJpF9AgHAcXzdA2HK4WMpiZYKF-O3r6ICH4BFG5xsukHSaw49am78IdxoXU043fR39bJ_EqzB5jKu8Zm0rN7lh0oVL-gcccAKRopUCMFHbLyQ4LHz4VUf8boG8cNmIEUo1L1UWQmQ0MnbZGEamkElylUxpUciUhh9cpz27YBFYh7CUrrsn8pA2kT4NSLwONgbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=ejyAEmOKaGOudvo9-0DFdF1FV_rKFL2rHHYYVfJJ9lcWQs3xepbcf89RLR8M9CD7efNvDqhbUkzdaN5vw8Y_pu374subBBW_gd0BO6Vn0gl0468YeetJl_FkeYC6uW6SH8xDZUZm7AA4tBJCtMYnYJpF9AgHAcXzdA2HK4WMpiZYKF-O3r6ICH4BFG5xsukHSaw49am78IdxoXU043fR39bJ_EqzB5jKu8Zm0rN7lh0oVL-gcccAKRopUCMFHbLyQ4LHz4VUf8boG8cNmIEUo1L1UWQmQ0MnbZGEamkElylUxpUciUhh9cpz27YBFYh7CUrrsn8pA2kT4NSLwONgbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIm5uTJRUfE-eLTruekny2KekVHsxN7g1gR2KOTVKFdFfPpyB-RK5dii8cR_sNng8AuIHJgQg0pv4Tw8Dw99CUX0DBzrvSrqv0t-XKMdvamiIsaqpuctTARX2YVkxuVlaE26m9gDzfAYEHjZ0v-H_y2qCglLXe0S7nBh47L0RE4RNWgHCxKTCha4IHUgFAXXy40Ce1dh2oP6fmVvp690ZEr8-MYsHMezROITfrW8g2mLMDo2os2WPmPBZxJG3cpHby5gLiQAuLcUwZUcbJM-T0FEFk_NuxLpBeN_fk4UayYbpfgfklCYObOZQ-iVBZVFhUVP0Cns_b2eyKUEe2cENVN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIm5uTJRUfE-eLTruekny2KekVHsxN7g1gR2KOTVKFdFfPpyB-RK5dii8cR_sNng8AuIHJgQg0pv4Tw8Dw99CUX0DBzrvSrqv0t-XKMdvamiIsaqpuctTARX2YVkxuVlaE26m9gDzfAYEHjZ0v-H_y2qCglLXe0S7nBh47L0RE4RNWgHCxKTCha4IHUgFAXXy40Ce1dh2oP6fmVvp690ZEr8-MYsHMezROITfrW8g2mLMDo2os2WPmPBZxJG3cpHby5gLiQAuLcUwZUcbJM-T0FEFk_NuxLpBeN_fk4UayYbpfgfklCYObOZQ-iVBZVFhUVP0Cns_b2eyKUEe2cENVN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCBo6eR4aUSGzD4_Uih2u5DeWfuOeP5L7lSD1CaK3rB229VQVwqJuwqn2ZhjPLVjFaAHaoIjY-b3I_0x7Tzp2D8WDDPbA5EyKjKPImNCZyZ8fGPPO_FHnby40YcD-34dBsUkayXbV4K1il-f9tRAnQQUtAfkF48K9CHdaSui4-HOFbuWwkvY1NuewpbDuBPZZsYX3INsdkQbnklBplz5hEEsZGWlc4Dz_yooD-2WroLaxbVycdxWn61lAYRHUFIWNoBL_qtyHUT1Xb85Nx4mhNcPJSIlokF6ChXeiju0hyxQ2z8RFvdaLstn7P7YfjiLS9GYppDrRWVwcDUDb_B6kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTnz6ez_dP-1uqPdNHnrYQCDov5b-jBZNBlHYu4O30PbXLgpxmHbNXYKBiJVizK3i0rDf77vcYLAn_yrX1mSZ-scWJ7-ndvjfHjGsSLR1m9At1tzwQZ6PbwlnRnjRcAuehLvr4ujGJUovg03RIutCn7U2ZE15WImUYlld-oEMkRg02fcH2QacoExIR8lt2D_D34GI7xR8YI0B5ppNGcPtX8u-fn6lEKq77_4XjB4laoQgQiVNX-Hs8B8vqcmYQs6VZSS6tHysa0BJnRnE1tb7m_uilBHMvZRcr57rj7wmz1okBfflx7Mn6-gTqUbmCrzSCZWA1jNvDdIKZHDCsosSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEGknHI96EV_6zCFevxziIv5rVq4D1i5XRvNJYuR7cTflisfuF3pNlRotnLR4Ab4otz8w6G_89sIKy76BQ0p6nShedmpuImSKVj6pwIVfPLGuURg4OSFZBCiMXG7CNhoqlIxtJuoVpvboAWDO0rgSfcbEwmLKh34uzb9wFRZMmVW5wBQVZS_vU4Z-0H58nH8tyVPxF8P_dle0J03tYyCxDHJ9BqtTpIq7kCzfbIUY2GJAjKJWxaJOw_NatswgDxSBbINOr3fh_y8LHyJjRmimKMwJ6NbhkSDe1fxDorRTuQZTSxn_wK6IwjOZEtkcmk3FV_N-wipgWm6m9fAObDM_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=ed2ZpkGT9RRQaBRKSoaeIe1BZA0hnzEqgU8199k6ftkOw7KL0gu-BTYudk43KW9WpSbAXX82uxmZ2Kj_Rt4HdXDFxEFXKlvU4yBzEuNzMPsdHrhTBDX2O0s9sNlmIiySBexRp8Yht2kG-e8Aj3DA4kVwsfrMlxHhvulhPCf5k7mgnvMZg4CvNtGDigA_eNa7pAoyaaR_ydfEWbBFWDksTwWgPh-wLvzyQfInEFzoSseTyo726fyKG11QeivpKQPW0MGtTZKNa5n881lsqNEfKPRLGriIDsPS4eFb7IV0bdVLUdevy2uNzOIjv9UKI2NCk8ml2FFgOMlL3u_W_qD6AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=ed2ZpkGT9RRQaBRKSoaeIe1BZA0hnzEqgU8199k6ftkOw7KL0gu-BTYudk43KW9WpSbAXX82uxmZ2Kj_Rt4HdXDFxEFXKlvU4yBzEuNzMPsdHrhTBDX2O0s9sNlmIiySBexRp8Yht2kG-e8Aj3DA4kVwsfrMlxHhvulhPCf5k7mgnvMZg4CvNtGDigA_eNa7pAoyaaR_ydfEWbBFWDksTwWgPh-wLvzyQfInEFzoSseTyo726fyKG11QeivpKQPW0MGtTZKNa5n881lsqNEfKPRLGriIDsPS4eFb7IV0bdVLUdevy2uNzOIjv9UKI2NCk8ml2FFgOMlL3u_W_qD6AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsJW8xGS3G5Ko-jFVQNZ5hLaPIV07Gyzo1ZmnXKOJJt4HNJ99X5ZaNNBEZQDUglnRkIkxPCaavf3Ba8ngtMfSIxp4tT8YLbg2Nhl-AvAWOejc70xHQpG1oyqvRzkGFT_yXgk7A4CIexnTWFNWnpa0Y_eYObxbfGHxsl2orDcBJSJ2CYwp9i10lEEhuuLaveLGFr7d14wjUaVKCHm3DJdb3vmNJANt2NMtGDMo-haLThvKfNTYM90dZIhMxSrIyUej4OYwNVIYc4TDW9D49ITuv4q_iJaC2eK5gm3krsLcwbNnr_65aFOUbcdEZ2xORZza9REJYt6aS11qf5m6Jao1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJHM1jrnP5R2j1M7EY2oDf4USjAdxJS1nNiUAp2-TkAePstf3LRGNvPDdFiqm40lIVcM5B6r1Q3F7J07xLy-ng-HI2_TOWUUGqr-w-t2yF1ADC_bJlpNdIRMSF-0Wp_laLiCsVVBtA4r22XZMmnRZ7f6J9vIrcP8YC9W59XgJti7oLOBIccl7H5t2Tjnu92n-pvTS-SwqA5ps75bod-lptiZX3RDAOBvl9G-jdVp4oEHSoEzFHP-LCH_fyeRQO6sVzB6UJ6TUc3QGmhMRwblCu3yo0K1h7JiTbRvC71sAjrtoENfGKOEGUqEG_9X9ydi6beiGBDiOI-RX9tULjumLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7NGa_c9ihoxe_-6LQDQcaOGHA1aJAvHOEyRKxt0CBEAEOevyCEVmgreSlX6_XdhQRLUclZlqZH41Z1e_woM2V1W2vGoqIVPcoqGeWoJhi38HsPU8vWQmP8JjLqqtAf7DCBOs45355pofWPXydwTBy-FgimgxwI5i-MZ011T6M0FP3U7RaEs89ZZts3ni2Ouk5Tvj8hslv-nJLAnIgez77HTlgiEmiSV1uN_MqG3fFYrRznUTajAAwloyFY8W1KAXGYfPx4099fvX0O2HbahKwrea55hvEtA1PGAkDfvS80hnL_zT6wPm8HH9L6nUNbJbfUHD43cD2N5an8B8WNFag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUCcSuJRm7F2S9T_45BWmGNHFtP8Aeizu2uJQTn3C7fkR-KhKg4cfxXg0oSoAZGKmAw5PWsCvOq1v502W-x-WkwxjHEd-g0xOVd0LnuQ_qR0sVELPGqh-OKNj7jAIDnZ25ctQFQQQS4oF3Dwy0KARAe3RJh7IFqKChQ2puObhurYvcEC6kmBWeH7NB9LYf8yIaQGdw_0AQEdfny1FlJAPqTbCdiyWIVk6iBe0UzSiQr8ZQeiGXA36GelkAU5lbPPo4ONtsluXrit25hG33QpdcDfaV49Z6nesOH7AEGg7hiDP9O75untA-8lCRhb5RO-lUAaeD-Z0IOS8h1Pzyjg4w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=cLZu-TcGBeT_ZJ2rJ_fNljHwS8iD2FucgPFJ5f2nBEArzWKFubc6lItLL9nFOCS1lmpiyML6s9auFB5uvgleWCV6ngOp1uV158QfWyKSSOshWiZ06hXMZkPKsQ_4jXju-oFddsGX-soUATRfliJ0QVIkze-QwLUNrevH-SrhxpG5tPY8T_NZeKp5WA6xwub1PGvuVEGx56zvMKNUUnHYdy1djcyxhzU1_87pHOdxMB7zj2hCd1Yq-X5Of6gNKKb19rzn_bQ3xGRWIGT6b_Sx05e_hbQ_pj9Nq3cdApdIWu6fUTWGg4yeuEYOI6Ef3KOUipOYHnS7TQgMW7rDgAyEnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=cLZu-TcGBeT_ZJ2rJ_fNljHwS8iD2FucgPFJ5f2nBEArzWKFubc6lItLL9nFOCS1lmpiyML6s9auFB5uvgleWCV6ngOp1uV158QfWyKSSOshWiZ06hXMZkPKsQ_4jXju-oFddsGX-soUATRfliJ0QVIkze-QwLUNrevH-SrhxpG5tPY8T_NZeKp5WA6xwub1PGvuVEGx56zvMKNUUnHYdy1djcyxhzU1_87pHOdxMB7zj2hCd1Yq-X5Of6gNKKb19rzn_bQ3xGRWIGT6b_Sx05e_hbQ_pj9Nq3cdApdIWu6fUTWGg4yeuEYOI6Ef3KOUipOYHnS7TQgMW7rDgAyEnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=fmIZLp8NPhwtiGbmBUYsOnfQzUm78unlb3FAIjtxXBqhr21D8lC6ZjkcTm9EebtvyET10-gFRu3L-yT5ioZr5dOuz7ttpUkhdDqqhTJKkD505iJmdyuHVAKGsksIk_wvLaMf9QR_hJeOz9lx6as_6Tnx08hzagsSIdIJa8TEsAB9m1E0rKB3HdQ_2xAwTwdkepuKv0irpbkarkge93L2RgxeyvF1NdPBYn_Yf0fbzWEX9J3gPZ_0RminU9I3tpaTRbvs_sBWpcR0v1Dmi9QhpAn9TmFHTw36QlVMQHeDl9m7_2GSCfM4BWjyKCTXqcyLAGeeBJ63lRU6fi21Ay1NTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=fmIZLp8NPhwtiGbmBUYsOnfQzUm78unlb3FAIjtxXBqhr21D8lC6ZjkcTm9EebtvyET10-gFRu3L-yT5ioZr5dOuz7ttpUkhdDqqhTJKkD505iJmdyuHVAKGsksIk_wvLaMf9QR_hJeOz9lx6as_6Tnx08hzagsSIdIJa8TEsAB9m1E0rKB3HdQ_2xAwTwdkepuKv0irpbkarkge93L2RgxeyvF1NdPBYn_Yf0fbzWEX9J3gPZ_0RminU9I3tpaTRbvs_sBWpcR0v1Dmi9QhpAn9TmFHTw36QlVMQHeDl9m7_2GSCfM4BWjyKCTXqcyLAGeeBJ63lRU6fi21Ay1NTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=ffY4p1vyfHS_6t1mP8_k8QJ6RMmh97nVPhGm13D3l6agsTGM0-pZeMaPZFv1ippE5IXtsTsM3uPuJ-tINDmJWP5KEBc4nmacO2H6m4cdCRqBUq9tptvi56gzQgXwYFFmLcRMru8UlSN1FbYEtRtS_orucBgIEu56noQTkCQatYOPjQ5rhc_BIw_LPTAfH3cNjcRNV2_pcfCwM9p6bD0W3NsNrAGpenvp95s_wvOayzpAFq4wX4fzXQP9F0MHaMesQJlC8Glajshgv_FlBIP89evpKpBRZ7UhPdDjcp0VqNLHOu7ZAh-9367fw5rNV_bWuIUOBIQYVS-2fqj7uKZcrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=ffY4p1vyfHS_6t1mP8_k8QJ6RMmh97nVPhGm13D3l6agsTGM0-pZeMaPZFv1ippE5IXtsTsM3uPuJ-tINDmJWP5KEBc4nmacO2H6m4cdCRqBUq9tptvi56gzQgXwYFFmLcRMru8UlSN1FbYEtRtS_orucBgIEu56noQTkCQatYOPjQ5rhc_BIw_LPTAfH3cNjcRNV2_pcfCwM9p6bD0W3NsNrAGpenvp95s_wvOayzpAFq4wX4fzXQP9F0MHaMesQJlC8Glajshgv_FlBIP89evpKpBRZ7UhPdDjcp0VqNLHOu7ZAh-9367fw5rNV_bWuIUOBIQYVS-2fqj7uKZcrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb1f-qciqr9m5iacI_D73McJLhTeTV_aWqHUhiylMlagUZn3JtG3pCCOJJRFOOuXCJq3ybA7c5OTjGmKo4u4y6QH_ou9_6aGo9g3SK_avleQ9AU0kH3pLNPqH9b6HChC3pXIKTX8UGqpNfoueWm2irgjClEzD9_3Cs3BxSSqAjFEApnxZIjLAfOTs_OgOnNHRhXbFkb2Gi9MuSxiUhRI1AYYuKTJGvKbjqcx6sosuJjBtk3MtCBMmS8kiPaMjQEzQE34ezkdgx9Ca8PBegV3dLqbS0jeiHTlJMh4m462fPHG3YgisG4FyI43vtut_SUF-hpTjPlnR77aOz9_XYvgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=cRJWhO7j6_rNIrG8Spr4bAWn0cKCSp8ETP8wJNaH2ye4d-T4kFZh9fCfQxdMZyw_4DGNfU88ydCgxxAyOHxymHhChcnRHZHzulwNIblqOyKuNinan_nvxMCJa5xzgsnOoYKZ2HpSihb2mjmoDo9VMzgXUA3-hxtCtS1wPppBVzgGAF1_NACOe9RtZsFwuK-oYidd2-9GUyH-hvCx_aC5oXFF4dXtZIp1pEG5_miZWi9p9R6cMYHyaPMFITyPaBzPMkXFnDxsco1P5hUK18gJVK2XHdAdBDc93YOVl2S48AEkccnEZpJJQUF9EimO1SzTUWofsuccEiV6dn_WQI2pBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=cRJWhO7j6_rNIrG8Spr4bAWn0cKCSp8ETP8wJNaH2ye4d-T4kFZh9fCfQxdMZyw_4DGNfU88ydCgxxAyOHxymHhChcnRHZHzulwNIblqOyKuNinan_nvxMCJa5xzgsnOoYKZ2HpSihb2mjmoDo9VMzgXUA3-hxtCtS1wPppBVzgGAF1_NACOe9RtZsFwuK-oYidd2-9GUyH-hvCx_aC5oXFF4dXtZIp1pEG5_miZWi9p9R6cMYHyaPMFITyPaBzPMkXFnDxsco1P5hUK18gJVK2XHdAdBDc93YOVl2S48AEkccnEZpJJQUF9EimO1SzTUWofsuccEiV6dn_WQI2pBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=BEIzAP2bTL_7E7_baRbtphIowHQg1J8wjHWNegTPyK_A0FwD6OhA6z0jujKkmp-e8-PdgQK6wjUt1gXTp6-xurLNbiqYS8pQgweCaFn_gVs_v5VNtRAWk2zSj_ws_Ufeev57XDk5HQK_m3-vOxo74YGA2g8otzws-bCcQUVXkCi18q1ioLK23evwEdeGtXs2Z4yaryrIuFA9l1ekUE-7Wy07q_tTnmYXnhzewrE0iNAwXc3TH9nnxGRPowwyeMei3aFh1AmA78iN4BX5hF1H0P257WxnDRFh6sq_IT-r0Hf7Sk-EEOU18Sbtoi9XV85rrQ7WtltIzKABI17grzziGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=BEIzAP2bTL_7E7_baRbtphIowHQg1J8wjHWNegTPyK_A0FwD6OhA6z0jujKkmp-e8-PdgQK6wjUt1gXTp6-xurLNbiqYS8pQgweCaFn_gVs_v5VNtRAWk2zSj_ws_Ufeev57XDk5HQK_m3-vOxo74YGA2g8otzws-bCcQUVXkCi18q1ioLK23evwEdeGtXs2Z4yaryrIuFA9l1ekUE-7Wy07q_tTnmYXnhzewrE0iNAwXc3TH9nnxGRPowwyeMei3aFh1AmA78iN4BX5hF1H0P257WxnDRFh6sq_IT-r0Hf7Sk-EEOU18Sbtoi9XV85rrQ7WtltIzKABI17grzziGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=qriWjWKS5Dts3PKo6u_-P4rs9TQG2jc-ZYnRotKbBPTqB4UogGd2ROVTpZrIwlFdEd_bdtbBeCvwvt3zKsgzysPyfCJ5vnXY1gw3sFWdJEPVYoVzop7PDgmuzOFhDmHgl7QTeqcbMxN4j_6WF_0uzQGqaatNXTRRTRzeZjTQZ9FfIB9DUyvvHUiYIdw4b0p-Xdfm8PtEtvoTzjqMmAhwvnQBiKO067OVq6sTAoSrJ5Et7LmnoF9txVYJvhILO0K8v77DO4LfWJOctqIo1g9HNNQTUIScYs5ovbsHUk8ucpVQQxdx0fwrXup4OggkbeRDymSwvxDoC7ibCOBxlPQ5DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=qriWjWKS5Dts3PKo6u_-P4rs9TQG2jc-ZYnRotKbBPTqB4UogGd2ROVTpZrIwlFdEd_bdtbBeCvwvt3zKsgzysPyfCJ5vnXY1gw3sFWdJEPVYoVzop7PDgmuzOFhDmHgl7QTeqcbMxN4j_6WF_0uzQGqaatNXTRRTRzeZjTQZ9FfIB9DUyvvHUiYIdw4b0p-Xdfm8PtEtvoTzjqMmAhwvnQBiKO067OVq6sTAoSrJ5Et7LmnoF9txVYJvhILO0K8v77DO4LfWJOctqIo1g9HNNQTUIScYs5ovbsHUk8ucpVQQxdx0fwrXup4OggkbeRDymSwvxDoC7ibCOBxlPQ5DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=H_MlkPrPd73FNI_20FAU7XYnTSB5u3YY3woZQ2evLlqPwSwkwYsYktLBIdxwX6SdFUx-Yf6AUCYlv30ARCSg2Ax4daiHzBa3WEs_ItMjpJCKxGVgi56oiEBD8AAZ0Jc5QJfHf6lpy5vx9hwJ7sb7In5UNtuibDFsxmlbMnlSoKltWZohk7UJdI8D8bGR2kmXGZvrgKK4D-pqzHxq5ue-Hz9bBnFuIFCX2N8QInNMTikzpw7ZvcjH25c9kG6OoONpw3j0HRaPZQBe3hO7Zxl27htogf5Zs1OYCa_kosXLkSGboLzdAHoxVptJtpQ933PaYYBgr6m9EsTOsTdUpu61qVODZRoDeAcTK5IXUIxDpn0_6Z_E9fI4ZCU6ronzWo8oXmbWAMsNw2NFk8qRJu55uuqrMnTJ1IRc029NzLwWAWAcO-qXKa8bPRuUoqvUS82nQsHa24H5zBwu37vnSKeS1El0fWMO1GDvRFrm-0wqPSIC2coXDqgRCve45vIw950wOPZM2jW3rylStYPbviyM6ItfTFZztlKt9TP7d9mGCS8iwx9dX8133fA0LeNiNlBjB5Yfhc0sQ59S9utypWDZsJOjkAAmy6vaTXzHBBlmrHUP_c8ixDx5YVL4gPTLHTzaxpnKQTWg0XS2n5jcwNgvE-tNwNolauQLBOBHn0r-A88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=H_MlkPrPd73FNI_20FAU7XYnTSB5u3YY3woZQ2evLlqPwSwkwYsYktLBIdxwX6SdFUx-Yf6AUCYlv30ARCSg2Ax4daiHzBa3WEs_ItMjpJCKxGVgi56oiEBD8AAZ0Jc5QJfHf6lpy5vx9hwJ7sb7In5UNtuibDFsxmlbMnlSoKltWZohk7UJdI8D8bGR2kmXGZvrgKK4D-pqzHxq5ue-Hz9bBnFuIFCX2N8QInNMTikzpw7ZvcjH25c9kG6OoONpw3j0HRaPZQBe3hO7Zxl27htogf5Zs1OYCa_kosXLkSGboLzdAHoxVptJtpQ933PaYYBgr6m9EsTOsTdUpu61qVODZRoDeAcTK5IXUIxDpn0_6Z_E9fI4ZCU6ronzWo8oXmbWAMsNw2NFk8qRJu55uuqrMnTJ1IRc029NzLwWAWAcO-qXKa8bPRuUoqvUS82nQsHa24H5zBwu37vnSKeS1El0fWMO1GDvRFrm-0wqPSIC2coXDqgRCve45vIw950wOPZM2jW3rylStYPbviyM6ItfTFZztlKt9TP7d9mGCS8iwx9dX8133fA0LeNiNlBjB5Yfhc0sQ59S9utypWDZsJOjkAAmy6vaTXzHBBlmrHUP_c8ixDx5YVL4gPTLHTzaxpnKQTWg0XS2n5jcwNgvE-tNwNolauQLBOBHn0r-A88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=LK9S1YPbCnjmsZOVaADXXeepoliu3go5iaLtOwib0xS1W7rizihYoxM2sx3yV-gtyyP9QR-SGjGERnIHWgPLdlv6kSxjdpa0Z7qL-t19vPtilc6hgd2152oaFfSlwtAMxLnJsh4ziUQ98O_ZzA7TZfvQugohVeSfWCdI6YKfgK1J8UBbInKiWMFYRTHerZo3N4HIOG1OgoLgbVbsokI2t2Vu20dqJSDZntPyZmzNKqI0ux9onWGAHwnMLaFFCzKQ1y5la1c-lnJGySDSrm_yW6H0mZanZy-nunlNIEwSlpzcd5ZTtueRvbSEZWb4qx0ZpduEoHyp26sBhy48nbcfOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=LK9S1YPbCnjmsZOVaADXXeepoliu3go5iaLtOwib0xS1W7rizihYoxM2sx3yV-gtyyP9QR-SGjGERnIHWgPLdlv6kSxjdpa0Z7qL-t19vPtilc6hgd2152oaFfSlwtAMxLnJsh4ziUQ98O_ZzA7TZfvQugohVeSfWCdI6YKfgK1J8UBbInKiWMFYRTHerZo3N4HIOG1OgoLgbVbsokI2t2Vu20dqJSDZntPyZmzNKqI0ux9onWGAHwnMLaFFCzKQ1y5la1c-lnJGySDSrm_yW6H0mZanZy-nunlNIEwSlpzcd5ZTtueRvbSEZWb4qx0ZpduEoHyp26sBhy48nbcfOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=pktpx8ZL7DgPLUo_M2HN4lCzkgdpGj-p76w3-qoOiiEjwCDTq5YPjRrcatc54NZ-5K-oUBl_8WFwoBQNSTvinXzsHuvyD2LcE30tD5JMwOe232WklwvZiN3ZaYQDRRZOtI0993YqNFtpc25L-SxnVjNncKLsZN9oV-HH05xIgpxdxX1gdioxneN7jBulB53L4LVubXAXEZ40VdquU4lILcS4vUZSTRrpBWUWh2GwfWbZ1pWos4Cp468XOsYd2D68fzw_Tr1RLvXwHnlR2SVEK5gVuz2BxpwUv5_ZUbP85Vi9PUKBM6HMMIhfgbjQIO9laYK7exS226fzPg5Q_1x0fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=pktpx8ZL7DgPLUo_M2HN4lCzkgdpGj-p76w3-qoOiiEjwCDTq5YPjRrcatc54NZ-5K-oUBl_8WFwoBQNSTvinXzsHuvyD2LcE30tD5JMwOe232WklwvZiN3ZaYQDRRZOtI0993YqNFtpc25L-SxnVjNncKLsZN9oV-HH05xIgpxdxX1gdioxneN7jBulB53L4LVubXAXEZ40VdquU4lILcS4vUZSTRrpBWUWh2GwfWbZ1pWos4Cp468XOsYd2D68fzw_Tr1RLvXwHnlR2SVEK5gVuz2BxpwUv5_ZUbP85Vi9PUKBM6HMMIhfgbjQIO9laYK7exS226fzPg5Q_1x0fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuhZup99FzEzwxIJQIWqqSoNcwCcgbaJXvsz24VnNFv7_vhm02HXqvsl-Li46HkQCkehfpz-IOn1UyUnLp-k3vMZ_j0DaKLu0c5ivtT0pQciFtpdhsHyNTIzCPcq70DVfzcy8W_ojeeMwLJ4lGaS1Z_ZqCA0inR7DnRY6LA1igB-WjtdWP5e-0MinHMc0EeJw-mnugDA56qCNtvnK4HHUcHAAEP6aGGqtJXwo_fC2Tlzc0-ogsbQwsLSttvcGYlDDn9-3GxelDorl6PQxzwWhkirkDOgH4JWiE6CbAEAKdbc_Q3kmOZgk9kO3Yv9ZoSLoMgtyywhh650HebZTp0Dyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJzt8nsuJpfvahcNvciSdUnM35cMR7qFuzYdFIsXO8v74MojE5C8Yi7ErV0FOwChhknhMha_ZcvhgjkbhNpwwu3S7O-o2QfwiuPIZP5fDHDSxJLQawIYQXyDa2yD7UkWfck5fWe6y6ZMz5HQkhlzQiHHcT0S5e5xi8GTBZDE4DK1v-agduNkvOUsLAEilKSvvU70wvUmO5ktKvEQoMGR5i1ao6s4Ha8L0-kd8oTXs8QFO76CddqioI9obiOOlVanfaMcPYVc8tdoScov3nAs_amHXSGDbllfLmgD7LvX5mhuzCdXzSM7gcBrEFXFNBmUI4lfdIkLYJJmupSdjBdfrg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=pQz2IylOR_u7pwfY09UW7kNbmCtW_pcWWQaS-hWdxAvW0UtxSUUTXUyc9Fnl9bMnUZGvTD6AmORrNNrAANoFfXnjbzkglwzbiJfypdV0sQuIjNGtieMIu2cK91zHy66Kdt_c_4jVzBLFJ-ZF4o9S0DYbk5fnCBcymueQ00w6BxEaEweTX0dYbwvKCp7exUggjDnloUPhjTLWpRDXf_yF1MzCEFJYSCdjibObAAZGeRrwHAk3zAkXdWuhwKLiZ6gJmwOndXwMb9z9m0XUwdj1KKd-PsPUkUlm5QyXPBxBGvewZifht6oqmxEUCKKvwPF8LDY1qqRHKobHwhDXdbI3_3bb-FSCfszTrcafE_paJzlXbqBPTgtS2YotlUhrj7qHbexvdV8mxKu6tJFjRnBhl1US41SUDWaNgtq55Dqv5NA-8k220kG-cPOHM4lE5qQav2aGNz-L7zNKjbmW9uEEfvO_Np0KldfhBgkYTRecQCFZlc_2Iawm-15ltFUAY5F3137UzM5THmSNEvD47e3ijFlP8lKvXbh9rIDuw6DU28X9OXdwQMdAtBsrDxQV4YKTxziBWNOMlLaNPasW8kBsR1xFVOtCN5KoerEufLo49DLYt5wMVlmIDTSnIlybkHliRb-hvByBdkUaEw6xq5yBMhyskla_T50BYQwBiYs5qGU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=pQz2IylOR_u7pwfY09UW7kNbmCtW_pcWWQaS-hWdxAvW0UtxSUUTXUyc9Fnl9bMnUZGvTD6AmORrNNrAANoFfXnjbzkglwzbiJfypdV0sQuIjNGtieMIu2cK91zHy66Kdt_c_4jVzBLFJ-ZF4o9S0DYbk5fnCBcymueQ00w6BxEaEweTX0dYbwvKCp7exUggjDnloUPhjTLWpRDXf_yF1MzCEFJYSCdjibObAAZGeRrwHAk3zAkXdWuhwKLiZ6gJmwOndXwMb9z9m0XUwdj1KKd-PsPUkUlm5QyXPBxBGvewZifht6oqmxEUCKKvwPF8LDY1qqRHKobHwhDXdbI3_3bb-FSCfszTrcafE_paJzlXbqBPTgtS2YotlUhrj7qHbexvdV8mxKu6tJFjRnBhl1US41SUDWaNgtq55Dqv5NA-8k220kG-cPOHM4lE5qQav2aGNz-L7zNKjbmW9uEEfvO_Np0KldfhBgkYTRecQCFZlc_2Iawm-15ltFUAY5F3137UzM5THmSNEvD47e3ijFlP8lKvXbh9rIDuw6DU28X9OXdwQMdAtBsrDxQV4YKTxziBWNOMlLaNPasW8kBsR1xFVOtCN5KoerEufLo49DLYt5wMVlmIDTSnIlybkHliRb-hvByBdkUaEw6xq5yBMhyskla_T50BYQwBiYs5qGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGNLo0d4J_m6m9CX5GZkDqjYTaKilJeeiDdD1HiFDBwyETml02vYwTqGec-H_Qztrp1FM2gfpTEmpsdDHnDEKORkswoeGRmHgKaXfaSO7DXvxc0gKgIyDXZHs-S34Fg0oEwQJRfVx7PSOmRvjD5HV3Kdp4caMCjCZMtRRyuCgXWt5EoIMFN3CHya6ZQvBMAtWP2F2U7Iw7oqb1Kums_pcEncoizK3uZFmeWa-n3zBySSd1Wg5lxa9Wmmkv1I1_qj2fGrxWEa48mTBJY9fAD7NPW-vXN9Sq5TcTPE-Jx0YCzy1UEPYtLOZUp8_P1_wRc3F6Hw9PgVpRmp3FK10yafpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNDiaZDBPPHTPbYGIbuLHoQ_zEctP08GRCwrsTi8hoj1iBBKg0gFySQ3JyjCgDTXmS1mX764lC1hUI3WBh679qnxCb4DVbvvTQSvOm6ONAiFsfIMow62rHNzIUtlMkN4X1GnrbJLvB_UA13CkNN-utLCfgaMOb5XATWODu1NKn1GsCeV-jQqqO_XyfVQbJLWax5Dh9yP2e1Mun43z_j81YrspPMrJtwbD8XgH5n_gzW-3orhvqB5Kyz-x8ypXpLCGU9KDqKFd2GwzDSUlYgnRYtW_1PR9OWaL9JYO6p36HeZvH4plYf_GuKruPyKGpFPNmQG3wVBeWoAmEQnZQrV3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q846zTjxpzzoXubv_c-vuIyOGOUlU7VeavGeyuA2zPGP3Y5h1P40JBzO7PCAWjoA_Uo5QFAXKT_WTIDQBMYREfjrqrvRELf_n_hB4Y3qwx-tsCxJhuxNXEGnyB1Q9szmnKKnH8KBd8DVMUkoXAdONj8MzgaJjRXJNXR7-rmKv5r4bFToMi3qFnZvCXxr39a09FnoI7K72yW77udLWXRhosH67hYgtrhMbAuNkFFORtvkg5DyuGJCikItHpNV-ZldBlsFjx1b9qRg6eQhinZt_LEesTLAt7uI2oWTnsYb6dtFmrIzlDJks5ax-qrv8-g0N66bEyyr0LeXnInsZV9YKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9Z6Y2A9yPxeN0dEEGdqu-oT6J4GQj6FQ9BlrQqjz0pGIyXxSMUiZW0fkomEEocVmLgv5mKbV2PoL0RDvKJxJlibo0lpNxLCAI7jorKBJGZq5WpR50rYCaAhBbvsdp4vA997PbdD7e2Zrl_2VSu9ZnKLpYLB9iQBzdx5XRvDd6UpdB19WbtkGk0YqjA1uLIBqWybDAIOrFzTIjOfFuv-8fTHThUcOzTaN5CP1ChTlbqKLBkJuIIHuzoblnMvJAy5DOkgVXCoDuefb3nTi36NYVqplCoFFouDa9X6nrBzXNoqKGpVXEvqOzKb_LDHpCsTx8Z7N69zi-LhyyjIQjlEhw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=eCY3OdxxRWxyAeo9PyJkh2b5LObKnNcv_zQOcyGckP-TT2pDDyYjqzZiYRT95cnmxoOKsLMoBm4vj2uqIHeTCRN5W5rC9VTubmSfxZGRaXqHKwd09q_FbVpj7DH7Vm4TEPZuyM3tXl49tsrmbfKBnL1GtNzPDNgB8Anh7TE4_utCmfMNqLGEWVTHI--T4VSBUUBUCCgh6WwcglSv2ZhqNKYrl-6CSZTJEnbgkc3xxuXhmVJBDiWBHHMmjjwEriQIIksOs16TNL7c4DDqLitcIKO04YFmDus9LaXv2KRGOwTqusuqGgIZJ_07w93eI3TIW0yqxhFjSLiiHtYTMSC1ZkFWhUbp482bvPhXJZ8SH9O5_S2gtBqC69WzPZiX7QOptrcMHFbkwr9-7oVw99zOtXHj4CNVk_iEpi7ebcmCF24bjMgos6XYXv4wwlS0o3kvWfXY9Mm1F5UdUjdHxtHmhH2DmngpZK88KqYS1L8qPAgHEfE-W-epXMKM-aMJREuwEIaATv6ywe7s8QJyIqLcEVLAv5_3GY7F2gGU9eLBwmrrRbof00fbwCLTfWYVU3-E2hjsr5XurW9KD2fAj5tMgKB4YcfuWVQ0OnbVbddOU3Jp8yHsO_60aKxcsdRopXrMblOOhflNXabpMIUc1sOVz0K6yISDrUfF-p8QETuouGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=eCY3OdxxRWxyAeo9PyJkh2b5LObKnNcv_zQOcyGckP-TT2pDDyYjqzZiYRT95cnmxoOKsLMoBm4vj2uqIHeTCRN5W5rC9VTubmSfxZGRaXqHKwd09q_FbVpj7DH7Vm4TEPZuyM3tXl49tsrmbfKBnL1GtNzPDNgB8Anh7TE4_utCmfMNqLGEWVTHI--T4VSBUUBUCCgh6WwcglSv2ZhqNKYrl-6CSZTJEnbgkc3xxuXhmVJBDiWBHHMmjjwEriQIIksOs16TNL7c4DDqLitcIKO04YFmDus9LaXv2KRGOwTqusuqGgIZJ_07w93eI3TIW0yqxhFjSLiiHtYTMSC1ZkFWhUbp482bvPhXJZ8SH9O5_S2gtBqC69WzPZiX7QOptrcMHFbkwr9-7oVw99zOtXHj4CNVk_iEpi7ebcmCF24bjMgos6XYXv4wwlS0o3kvWfXY9Mm1F5UdUjdHxtHmhH2DmngpZK88KqYS1L8qPAgHEfE-W-epXMKM-aMJREuwEIaATv6ywe7s8QJyIqLcEVLAv5_3GY7F2gGU9eLBwmrrRbof00fbwCLTfWYVU3-E2hjsr5XurW9KD2fAj5tMgKB4YcfuWVQ0OnbVbddOU3Jp8yHsO_60aKxcsdRopXrMblOOhflNXabpMIUc1sOVz0K6yISDrUfF-p8QETuouGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=QUnl5w6KaUNbeo7AnfU-csbd0e66G38IoP8Fk-SaGZAPtRxxDyVJdwfPwmkomxiCn5Jz5Mq_n8x2PoOOiZCvoH03aJ4Jx4P1z0sJV0l1rGVuqFdPKgRHCRaYGck5CbsnCWufymg7ZBU1-vtx90ppgoWYtMMfM207g-B7OsPr7nBcrIPYGFxAYmPD8LaMRO-xHH7fIpL02vRTnN_9oEcP7eTKB8yLIU1J5vxmOIGx3HIDmDTNc38YH2fLu-hd1DNlwQQ0RELZDORypzA9B2fow78qF-oEOdujAUHiCdHjemCL5SbVBfh_0h2DYt65xTbjqLf2hwAVGGyBI3hWbZ_DcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=QUnl5w6KaUNbeo7AnfU-csbd0e66G38IoP8Fk-SaGZAPtRxxDyVJdwfPwmkomxiCn5Jz5Mq_n8x2PoOOiZCvoH03aJ4Jx4P1z0sJV0l1rGVuqFdPKgRHCRaYGck5CbsnCWufymg7ZBU1-vtx90ppgoWYtMMfM207g-B7OsPr7nBcrIPYGFxAYmPD8LaMRO-xHH7fIpL02vRTnN_9oEcP7eTKB8yLIU1J5vxmOIGx3HIDmDTNc38YH2fLu-hd1DNlwQQ0RELZDORypzA9B2fow78qF-oEOdujAUHiCdHjemCL5SbVBfh_0h2DYt65xTbjqLf2hwAVGGyBI3hWbZ_DcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G29blScF0CvWqUUyE4wWrUtdtaM2oyTe7ME_y0qXjNCSisYZsRSrcnL6SjTLo8KshQ6ZPkK5XjlVMJIpIh49cLyO9GlBd15ahszPh4MW2fSIUb9Lzt5bA28ENRTltSX7Yw5sQA-aURUuTl5wpImL6uh8U23qDjM1S2lFZKZlFm9kB0-W_nkPMBYiY9PmV2ptWsck3Q6WJzQrSQAv7MfGf7L-CLbrjjpAaocqou1uACh2MJ8lpSUbKrqQoNbplrA6vTYbMJ0Md2qWrhfV1BwU4aIMW3B_vGfvhVLg7q2Yk8j7xy4ZvoDpeJiahG0vBEFO17kBXVwDupoEWI0VvA6hpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I57_JNYqpQcyX17eBwnZR21bhrEXJ6V7m30Mv4T9jhggiIab5pZA__9yQKd83siV2jyNr8LY8H3I6yaa5rzK_IrSwn3c7uua7Nr6TuhUbcTrMBekoH3kFSRvRv3avKtXIXLVJJGRcnoIMrPgGPon3FZOvTypmMG0WkcL2d-qmKRzd_RDBZTqPJRVNM1JodJmTu0L2BoRiFT9DvB6vgVfWRxwtqGV1NYPu7_AMi2D_NEADjxeBvKx13ZXjsAg32SG-XV1Jdtqv10FDBo-purVUtBSNsnhU0s27bKzqQOUf_CW0gBXsM4DZKljGQ9-DqOcrh1KHTMAtU8Rd_Bg0l3V4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TmN-2LpN1ptZ8tBi8GnczF0nPPlU7PKf_XN9Zu8Y9_wo2eQ111mJE7nNWAVkNUIx5ihxF350IxEqlIbTR0oyyjga0dXheLzHobti4JiONXmkPojaXVlCOVosD1vPCzXK9JXrNr739f3TtXlIJ-fHwghCRZO5WFLy1RV8v37fx8epSnmZderQhva_tUrtKAH3nhTWM8wNTekg9LFr77xWQX7QzcebpVPa1MMobgQUbh1STemM69ztGFxKIX4NKetOrBWXypepszNDtmCGnMwuLBejlgOE9U9xdQ5crPQw3HNBISpq8gK97tZL7Cif2MN2-VDVjwoQk392MfcNvrO_pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3NL9nC5V9LoYZxzmTh5dpBwXnsF3xwR7WliIV47cQF_gRkvqfHzd1fK9vTHhSoEzy1_2SBKgJs21kFHwaP3816JIi6m_pkcxoilX-vFqTwXyo3B3AZskjiiGKzZReOKNGjhQepV5FM_xJlMd7hgIso7M0rgNUDzJdz5Tu3_ownt0nlJCpXEOv_jn8ZWxc00mavVJilao6l6JJykrofAOgA4VMlTW3Gpr0fhNIiJ8UI1gQYMrTPzOKsUiZ9_AoudMHlVCEhCW0iJ7ac_U3LsyMi921KjlpM8x2ktTiFsVMIixgWC6MusbrqmTgUZ-E392IZOIuMCDeFSMviyV4BFmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJARMSRmTUThwkVrbQVHBOaY3AGfrA9IbcCNMA8bynnuIcALbxyNmYsfHBR-_wpi8nhhNncKPyJPcvf8D_uKpg79YPHb2ET_GCVKo2QXioS2gA7Fex67j0O-lWL5rGel0pWxLsh7LQ6UZo6GGLWU_d6KYNgG5l9OkLkNUr8gMCb9yj9AouhFtvpW3X-raQNYo4XZjqcHCT8FlJPekeF2wmHSGmPLGAPdQWClWDJB5nEn50I7RC6uH3Sud7UGRKUeqVOI7YZxdTZgIGqGUlR7tusQUj1FCfFE_P6TA2Kd2e5zZ_rM5SOdiC0D0aG7WaSBv8FA2FXmvRdwn9Y0KRmTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv5aFcK7C9rbY0RhrUZq_vPKSzn2DUYNq69hjiw-CZx5jzq-4bSBmTAAlLKGCaJjKbOKfW50Yl08Z3mDZ27Rvc4AhqvRXgxpFJdgondPcKrYNDjphy10q81JC6LPKWXMihicq39RRkRh13CA2yybup8R4v4HVlt9Sj8obldfOrZdzYTCAhN19Y02IgfqKWHnlB-4J2_-9D2486jozeI_0tFSZU5na9pVyPAI5rN0YgymlTOp3gCvDMepH2o29VatF6oyhrcXRAyQozWhBmUC6O3dB853kdSGzUldAhSl_4c56WxZcsiC236cYGe_Vota9WA-gUQCq1SBho7XbukyBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/netrDeT20CAAUWKN4gCajazN-hUqFpqEGi9_44lLNgfz29uC9HGvSPWe2AzQtfQGdeXkX0wUQZO_RHOLa_9grQCHtvtjH9EzczAhaStFbQ81VLQNobbSZV8nZwMrq4qJmvU6ze8GgMikLt5o0oX1ACuPFcRQMR5T46TvnfBHpb6jmmHCUToQvPhZdvTdHSo3vzcTrU-vr74Nh8K68hH7bGYeu97QTSNavD8RCEQylf0Ulzu5dHaUX8n12JIo2WRoJgHMivdxcrjz0en52MJjaFeb2xfNi_-AQu5TKw9J-P5l3UKuEYSoHmnvcSqcC4ERMlJGdBVWyNAU3jptzLQj1Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=tFsVVW5zP1D8-QdQkZqh2jr3YsYjOwgA9n0acVfpPfnxCGrahn6YzZEiSPEZUShhIGv5p0ri2tWaPUuYk7rseoZD7Kr03mG1po2yo7Iaqk8bnAp-mpB-p549yK5fj-h_4t570I7o7kVOEU0ozSe3ZDnMk80sNg1_H0RsM4Yuf18yRHv1WAqjdk6bxaW-a7xMjcmtJ_wsCsjBT7CiKocg-vs-712cUfbnl1gvqEQJBjP3x9kWBVhm3vPB1u3XhHEdAAgBlu93gTVAcPkrR28Ca7nnx-Un_7sPTztgXC1e-1RVgML2w9ItblNzAInavROXMXhhJ05e-DBLQLC8ls9Xtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=tFsVVW5zP1D8-QdQkZqh2jr3YsYjOwgA9n0acVfpPfnxCGrahn6YzZEiSPEZUShhIGv5p0ri2tWaPUuYk7rseoZD7Kr03mG1po2yo7Iaqk8bnAp-mpB-p549yK5fj-h_4t570I7o7kVOEU0ozSe3ZDnMk80sNg1_H0RsM4Yuf18yRHv1WAqjdk6bxaW-a7xMjcmtJ_wsCsjBT7CiKocg-vs-712cUfbnl1gvqEQJBjP3x9kWBVhm3vPB1u3XhHEdAAgBlu93gTVAcPkrR28Ca7nnx-Un_7sPTztgXC1e-1RVgML2w9ItblNzAInavROXMXhhJ05e-DBLQLC8ls9Xtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg559It_i2DVZT0p74WCxtKI6lRqSrIIpxeDEuuiBFUgPAr1L8Q__WPAK0748xY94Fa7F-6ulGZFLhzC09b1TeMM03b1cRBp8kBJfU_AHG1-7bUtb6CEEKOShnt91-IpCo8oC3MTPC1WScCGP4neFTtKFCWdRW_Xa7mFfLTj46vp0PltQvT_laPgZZNXfxM49J8JnaKsB-jz1ZUtXcK-hA5OJRkca4fOVh1RszXHxoP_L_cDqX30OijoevMARmGgyP7UbtFJMIwVr24tAfmhZmq9LLNJx5wjvqURqe73htQVV28w7WsXHwO4FB283oPNRkCiy0BYDWewi8n5TCWkMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=Zj6gf4Dmw-ZsWyxl6fqA6vJrW46O4ihc98yjtKHtfdkkdXckw1748uLoZzngBZKkuS-K9KhyrfFRbgm7Zm8CgbH-TIhojHMer-1qEzo1vuJdg6dOgIGCxxayRtECf0sIh1_pZ2D4qo3uyH17nNcwK3fnVfeWZwSx7i2EMw2GReYzI9reYZV9QBl8hi7i513Eb0lQelOpkCsEr9xMJanDhWk5K76yfRzNkDSA55SOrwD_BefNv8orY-TwARc6pD8pz9Snc6UpzX94CL8DAJkCqlZqzoPEtkZarbnNNQLFcQFg5pCwj-wJc4JmBExhFKtDL7nH4tjTe7x0XpUTwsSM3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=Zj6gf4Dmw-ZsWyxl6fqA6vJrW46O4ihc98yjtKHtfdkkdXckw1748uLoZzngBZKkuS-K9KhyrfFRbgm7Zm8CgbH-TIhojHMer-1qEzo1vuJdg6dOgIGCxxayRtECf0sIh1_pZ2D4qo3uyH17nNcwK3fnVfeWZwSx7i2EMw2GReYzI9reYZV9QBl8hi7i513Eb0lQelOpkCsEr9xMJanDhWk5K76yfRzNkDSA55SOrwD_BefNv8orY-TwARc6pD8pz9Snc6UpzX94CL8DAJkCqlZqzoPEtkZarbnNNQLFcQFg5pCwj-wJc4JmBExhFKtDL7nH4tjTe7x0XpUTwsSM3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWSDKV4txfDHbIwBVvQqsprqBrantMMe61TYJOr8hEl5SyHjyUwjJLv4AxNec_tErzKuH7OklKtW9PJvrm41efZnk43ktjAAJqVI6Kq4fO_3Uoaq7oXcqbc2kFXMbnl_M-ywQWxXW9z5n2dLfvl0aFkfvrgxBMxjrFWcgAxDTgSie6cCCpl0fF8iWHO5GS1YQ42l9HbbO0k2tzuxeH8TTCQErBoYsTNPSQk-5RTj8F4nMPAFmFBcZXUktvhoOODNrc0nulMFYdnq0xXJa-v-yzYhtzjeh2iFoyI-YD00GKCShJ1rCO80AgCYC4fHSvmMAN3CNApsSJHSFMe05j1sEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGLjcNfDD1ELRO0I4FmaZkRktuENLpQqV180B-thMUlA6XrDP7YDvZRgRXt02it0IU_zugtuBjUQmHAcxprpoZo_msKvARp6byBr9NyAWuEiKtpWGyBf4_Crls_sAP6KPjCf4elzmITyTexYNQ_sYYmTiXSbz1o4zY0CmGqaDYesinHf-GiuSXiHY4-s-c5UuZGmgGsllAQUL53ddxYelJCXZvZs31olxOsPNRX-7qi-0GtSxORX2MgDnVWThyYeqC5MVGzF6JS4aJVSwyMCIb_gsryaKbLLvSu5Hf-ptTfyy56IaUyPNobJxScozesz8jvr_NcHkq-aJo42QCqsCuEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGLjcNfDD1ELRO0I4FmaZkRktuENLpQqV180B-thMUlA6XrDP7YDvZRgRXt02it0IU_zugtuBjUQmHAcxprpoZo_msKvARp6byBr9NyAWuEiKtpWGyBf4_Crls_sAP6KPjCf4elzmITyTexYNQ_sYYmTiXSbz1o4zY0CmGqaDYesinHf-GiuSXiHY4-s-c5UuZGmgGsllAQUL53ddxYelJCXZvZs31olxOsPNRX-7qi-0GtSxORX2MgDnVWThyYeqC5MVGzF6JS4aJVSwyMCIb_gsryaKbLLvSu5Hf-ptTfyy56IaUyPNobJxScozesz8jvr_NcHkq-aJo42QCqsCuEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=eFwYT5sOFoAN-f5LQoGGQBwUJKuYlShqQa3BpKPUIwDy67WwfVL7guAOptUR3TwqoWj6xiOMALr6s2VeTfZEUBijT01uS7Wynz0AWHl7csgum1jr4COUwZJAARgwrGY6E_ETuoEMea_SGKV0qBoK00wulaWw3Yqj4ULlsjm9JhZU4pq0DxCyrYOYIs_60jz9ZatFdkzjjxUifeCmbOjLkFqpaanfxbhP-G6ZNki2pnB3L_3fpymseKPWqC4yJH515cZjlXcVnXBX03Q41N4ICg9I4mrK9gcXEizgZHPGu9xib-Xnni39FNL4FrzMfYYXD2KekdJGgEcZ-eS1pT_P3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=eFwYT5sOFoAN-f5LQoGGQBwUJKuYlShqQa3BpKPUIwDy67WwfVL7guAOptUR3TwqoWj6xiOMALr6s2VeTfZEUBijT01uS7Wynz0AWHl7csgum1jr4COUwZJAARgwrGY6E_ETuoEMea_SGKV0qBoK00wulaWw3Yqj4ULlsjm9JhZU4pq0DxCyrYOYIs_60jz9ZatFdkzjjxUifeCmbOjLkFqpaanfxbhP-G6ZNki2pnB3L_3fpymseKPWqC4yJH515cZjlXcVnXBX03Q41N4ICg9I4mrK9gcXEizgZHPGu9xib-Xnni39FNL4FrzMfYYXD2KekdJGgEcZ-eS1pT_P3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=vYegWPWD3oPAgSmvUw5Ez3PfzeTO2q7wsFKgFMv98tcMxrwrbuGH8NfcpssreiicHV92TeW0L5c3Ig_YSPwZe9Gnyp2pIyqzgyDqxA9x0WTJ6W-0wzNHqSzL9IZiE0qjdS-_SVGhpJf3WVwSxmifhO1R3vmbmCivs1Ptk-R9H9T3Kav_2wROlrk9rpavr-3GWCQmuPaV6OGWGaeccDKfAgh9xLUlN9Poj0e4wjMjnhfFrcuvZDasrzZ5rEoCZO6995mRx7NE8RmzFnYzyh8bndF8aQOIyUW5Cx-ABkHu5mvleRhx9oGYixgZoChUn7LNEg0mAJqWw_jmM_O5JYLX-TPYJww7ALhIElkb4Z5jGGLEuBhdMBihEePxB2Q1imx1bxVsyFFO7qEsHWlzBw3dtXdVeRLfH6wzGMprqTORSUtTdcL0RJnJgYlynOD8D_TCg_TG_VMOaHDPr54mrcMqKYlkG9A_oNfUflUMrTeY4cmSuSuu-IKFZe9GEXveBo4lZStMq2SdmuB0aGOGdCrFklziGCmT7ddAJNrh2gCEuTreuAfPgH-kl_S6tGWb9lKaG_mW3PQAXmIDKITILNI2vEH85WTLK7xGg3WwsJHOxOSgaat6bh35CMVrWxwSQxTZE0ViHyD7-0aP8af0AbBkRSerT_0JZ2OZswB14asygkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=vYegWPWD3oPAgSmvUw5Ez3PfzeTO2q7wsFKgFMv98tcMxrwrbuGH8NfcpssreiicHV92TeW0L5c3Ig_YSPwZe9Gnyp2pIyqzgyDqxA9x0WTJ6W-0wzNHqSzL9IZiE0qjdS-_SVGhpJf3WVwSxmifhO1R3vmbmCivs1Ptk-R9H9T3Kav_2wROlrk9rpavr-3GWCQmuPaV6OGWGaeccDKfAgh9xLUlN9Poj0e4wjMjnhfFrcuvZDasrzZ5rEoCZO6995mRx7NE8RmzFnYzyh8bndF8aQOIyUW5Cx-ABkHu5mvleRhx9oGYixgZoChUn7LNEg0mAJqWw_jmM_O5JYLX-TPYJww7ALhIElkb4Z5jGGLEuBhdMBihEePxB2Q1imx1bxVsyFFO7qEsHWlzBw3dtXdVeRLfH6wzGMprqTORSUtTdcL0RJnJgYlynOD8D_TCg_TG_VMOaHDPr54mrcMqKYlkG9A_oNfUflUMrTeY4cmSuSuu-IKFZe9GEXveBo4lZStMq2SdmuB0aGOGdCrFklziGCmT7ddAJNrh2gCEuTreuAfPgH-kl_S6tGWb9lKaG_mW3PQAXmIDKITILNI2vEH85WTLK7xGg3WwsJHOxOSgaat6bh35CMVrWxwSQxTZE0ViHyD7-0aP8af0AbBkRSerT_0JZ2OZswB14asygkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCs--Ao2ZW2OyWwY2zNsvJP4qHJT4pTWfehYNkxZbiDpqIt3i5KzThcls-_4hM1vCVdMeWR-I5faOa32Z-6-nVq0-h1zCfYtOPPH1-yYtsQi3SpKqT7K0TS_-Ylumcpx3qjZ6xUj-t8o31HnIjqpR-o7E1p-zYAeRNcboBR9aUt8hU35XZoBmo9ynmVKnKOCgkPFRQwBnRy4AW3jKzIWV8BckWHHXIL7_0JkvWbzIQMufVWhHZj4lHjbzVeZ_RjTFdQI69VM-kSF2Rk9LE1Ze8xCPpVrjJMWMenXTmHCMLnTtUx0FtUUH4JHAablSyBTmr8FzU8vmmdEmHsMmlBSlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTlI2SoKDh9hhdfirvD7GGDIKItAGZDKYWzIp-707tHxYKqcSEmfZxvorsoiymAWEyiyEM2ZpzLV-lhAnELrZjcohXFvBEtZ2pjPQSzSWIkOZN8Zwc8FImVvMEu4seXNaHoM_HtFzUqtAZqMoP-lkMk_cUD9-YrrzHhE5d4SEqGVK3oAdakXIS2GWA-HoA2ROcatIqeBV82J0zL01rPn51pqTzf65xWZ0TFiJQZzGIrs4FdpAVinQOoiGGZ650w0fR0YyhJkR7XjUZ4gCKMwMGDmXcVeX_q42s_iDXkyI3R-dIQM_sePGqRr8GLnpMTcyxrDMPIuGAEAuVBCOP2IjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTkLLAh7GdZEJRMaDr82BfrGr-9AqAMCPOeLZ-exSTug7aMqm7Z2-3bo2hUkKt8q3I1Xc1kxX_WH8Kx4eFOuKlovAk5TGW001nOrTiWOUrXNTcNnSjCIJhvusY-mAInIY331uDs38H7KIVgX8jEad87zfrnWdUFFZ-Zo9WuaLsEbvzE8CDwiDlwL3cUOsXfyTCwqqzssDRAZmZHIgNFg3ZccHUgW5JuE72tGidpFwuQqzSvPRMVUq7RmxD1zPdUy7Z8smHhv1MYUGM20UhvoYXKc3Je6KevgiVAhYy4x5b_D6XdGg676hVxxe1ugkSnEkLd_kTMB7JzZY0T9PjVtNg.jpg" alt="photo" loading="lazy"/></div>
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
