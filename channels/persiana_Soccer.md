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
<img src="https://cdn4.telesco.pe/file/UVE4kDOR6uh7OvvoDUfGIXEaULS_ae5vGc8mSAzYrelbWk1gt4_Lc4dK_Rr_yDCzocEo25LoQyOLjVAyU1R35VACJl6sb49IaOqOPRmvPtjufM001mHfI4nK3wWTiflKjiaoGUNTZ-sVu5ACHdu2zJGmuB0w6Du8iZLx7Pr79RTH5lxF9y6BMNvDQIio6Fok9ztIyK4CygvczkAORQVu7jQ-vToGBQcbPCuJdLrFFkeXGu98o74J3R-RNXoTaAuEulT9JcrkIomqPTiVADI7p5KjSJstfgF9lzQNvi4Ain8vB2HrVO7Yd-hS5UOXTyr8aqVynL-fiCHC5jrWiE0Zsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 435K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 17:32:06</div>
<hr>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C52JfnNMJoiqDi9hYNlFTyc-NvyWDmhKN7zusjb6FHnV2LhhfKbQ_lVGpJ48jzKn80VT2DI6PqXNogOeit81kck60UgoRYkxK2QJT4wYCYhExQUK56c3Q99htaSmzfqMijbPfZZXHybo5HVRF1PIIlW7luRll412J0rwHSwXomf5sKFbE-bSzhQxpMKlDyoehb2osfMnRh93-EUZNVjxta3N33v7ufVhAxiru15IxNK_lIAsaGuSM6AeE7Qc5ND2R1DxBfOW70ygSiN2YLpS5Ylg1ms5Ohj5017U2untuC8BuWzhsVhX1OzuE0Y0-6c2P7a5GZjiyyA9nl6nswMDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhaR5RRxBQakZE8NvFYjHMFZN4RrVkySacKs4JVcPc3iWgJVyG7kD9ACSKvi5kfNpUUTuztbCh3VadptPIVQ1_LqmSoWvV3MvjdTj5iHBKIWzrzesxEFRtxn9ZfOxlxrYEu2ISNz8XOndhgZLDfJ3DGjb582wC4jyBSC2k0l3uZ3QXgNfeuGEDwGzpRMd_mvyKB89Al1N3l52-Xmbc5PoKc5DfZMisLsYz6vlC_a_20_yayxaMkg5WXzTzbYO5Du-qJQDXesPmCKHdUAuWyL1neXj4o-D3N3yVMhu0vekMJNASW8h6bgFwZrx1d1tzG4wZpi9hCgohBJbWXcWdpwlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=dDP6Cj7FuGB04YixsAahLKYKoJs3OfSlCpOGHfdr9QX-LJlUEG4gGV6neDOryB5Acb47aZLO9FLHG0hRfOCi4MoyqMPLC5LeiUniY5i6kFD50x1KryVCguZEvaLAzhKLi6wk8gWHlhctXLI_w4JW0mhwiYDbnDD_kLjrSYU0U2BNW1mlX9tAEvFaLGDRYEKPJBAv9W7nI6r1XZeshtFP24pG72kf-2XYOVxwDAOW1ULhtEIhKXAI9An5PluacdQFiD6vSfwfDBGMLOKk3m9lr15NavnjT5BTfvUg9tipx3R_4ewJwHFjFfn9Nw9n9xp4wQajFbMfrceFftZXlT79oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=dDP6Cj7FuGB04YixsAahLKYKoJs3OfSlCpOGHfdr9QX-LJlUEG4gGV6neDOryB5Acb47aZLO9FLHG0hRfOCi4MoyqMPLC5LeiUniY5i6kFD50x1KryVCguZEvaLAzhKLi6wk8gWHlhctXLI_w4JW0mhwiYDbnDD_kLjrSYU0U2BNW1mlX9tAEvFaLGDRYEKPJBAv9W7nI6r1XZeshtFP24pG72kf-2XYOVxwDAOW1ULhtEIhKXAI9An5PluacdQFiD6vSfwfDBGMLOKk3m9lr15NavnjT5BTfvUg9tipx3R_4ewJwHFjFfn9Nw9n9xp4wQajFbMfrceFftZXlT79oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هومن‌افاضلی‌از کادرفنی تیم قلعه‌نویی:
شجاع پاهاش پرانتز برعکسه اگه پرانتزی بود پاهاش اون گل‌هم افساید نمیشد ما میرفتیم مرحله بعد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=ZjagCP72b48UANjEJB9xTHjlhjUnqNGN7lnlq0UWLc1I3ZOn_cAm4bcYEdA7hbM7GuYOwo30UU0KYVPeHxFLI2elv_mDgKDWFj8xoOI7Xk7zjTZjdLHJIpOXkCBokKUvfITMqW28CAxqoGlx3hzHHKm_Npr6lmLixJavaC3hrSxG2xMAkECsTuoCEQq9gOc1YhF-oQamWwql5WTnN9g-Vm4T7-dL8VtdvgKx6WQtaH0hB82NBllzQmsGFH-D8xmZySl5cq-FqNF4TjULCewJF5jnTfHNu6E5GZSpPZnwmyPVjLji_NPeIziu3sI-h2uqjJ42Gt09wznZywI-SDfMdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=ZjagCP72b48UANjEJB9xTHjlhjUnqNGN7lnlq0UWLc1I3ZOn_cAm4bcYEdA7hbM7GuYOwo30UU0KYVPeHxFLI2elv_mDgKDWFj8xoOI7Xk7zjTZjdLHJIpOXkCBokKUvfITMqW28CAxqoGlx3hzHHKm_Npr6lmLixJavaC3hrSxG2xMAkECsTuoCEQq9gOc1YhF-oQamWwql5WTnN9g-Vm4T7-dL8VtdvgKx6WQtaH0hB82NBllzQmsGFH-D8xmZySl5cq-FqNF4TjULCewJF5jnTfHNu6E5GZSpPZnwmyPVjLji_NPeIziu3sI-h2uqjJ42Gt09wznZywI-SDfMdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل فردوسی پور
: آقای اژدهایی، خبرنگار صداوسیما وقتی‌صدتا موشک‌خوردیم و صدنفر آدم کشته شده ‌میاد میگه که همه چیز عادی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25521">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4009214e91.mp4?token=JJ68B73lD_DPtnowezEOUCtn9ne9gUioj_Z4_8KkaBj7z3XMb02us45e6WC2Mp7cCSkcrFECs9nMsb_REkZWCOb59oiXFhBB5U60pp0pwAblxOYjF15v0bTIPce2YRqHLLwq03dZ9KPQ3xtBD2VObFwns2biblw3ovXySNEYPag87DZ-K-FMuzsCm7JIUvtgAkjC3p-Z9xCVYBXDOyzEsoG7M6vrC2FXsK7emuxI8ywtODE-ncXJwJnXlp2XaGNY2541YP2ZLMSIkx8dJ2jMcMA_6fbvi5GuYHiHOvekb78rI3dFbRUoeLTd-8lQGZrqO4FmmKaOUFYy2rb5NxrSvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4009214e91.mp4?token=JJ68B73lD_DPtnowezEOUCtn9ne9gUioj_Z4_8KkaBj7z3XMb02us45e6WC2Mp7cCSkcrFECs9nMsb_REkZWCOb59oiXFhBB5U60pp0pwAblxOYjF15v0bTIPce2YRqHLLwq03dZ9KPQ3xtBD2VObFwns2biblw3ovXySNEYPag87DZ-K-FMuzsCm7JIUvtgAkjC3p-Z9xCVYBXDOyzEsoG7M6vrC2FXsK7emuxI8ywtODE-ncXJwJnXlp2XaGNY2541YP2ZLMSIkx8dJ2jMcMA_6fbvi5GuYHiHOvekb78rI3dFbRUoeLTd-8lQGZrqO4FmmKaOUFYy2rb5NxrSvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازی های جذاااب
جام جهانی فوتبال
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای‌مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای‌ورود بسایت‌فیلترشکن خود را خاموش کنید!
▶️
‌
Link
🔜
MelBet1.net
▶️
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/25521" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=m1diO67G7QJS1-405qVO0s7_ddwXFiH7vJyIVFzqc1FQNZNX405kFouKOv1NoQOoQ239tduKM0tE2WutXfLUiaUn9NE5Lhxb4LZWuLAHo8WRq4lLIGccVLB58Ati81Fi4mfOpb0LgJJ-dDIIP8-_mussXdTkTqj0NbTZhHcgiK982235UglmchNcPsVPmwTMl3Q2pQGEIHLge3u5UX5gAL0F-QAX9QADR753yNByjvFnlDpE5P5qH09UnSoehzYxthn9mcB-EcGM4Hy-R6XCNV7ZpKPK3herB64PeDDDFb9UbDYYHRH2lzK8l1-sFyBIjTrybpE9C7ZKcNHycQAz3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=m1diO67G7QJS1-405qVO0s7_ddwXFiH7vJyIVFzqc1FQNZNX405kFouKOv1NoQOoQ239tduKM0tE2WutXfLUiaUn9NE5Lhxb4LZWuLAHo8WRq4lLIGccVLB58Ati81Fi4mfOpb0LgJJ-dDIIP8-_mussXdTkTqj0NbTZhHcgiK982235UglmchNcPsVPmwTMl3Q2pQGEIHLge3u5UX5gAL0F-QAX9QADR753yNByjvFnlDpE5P5qH09UnSoehzYxthn9mcB-EcGM4Hy-R6XCNV7ZpKPK3herB64PeDDDFb9UbDYYHRH2lzK8l1-sFyBIjTrybpE9C7ZKcNHycQAz3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzYC-aGbpyXz-AoD-FMJnJujjYO6Ij4hSQxSpPXdtIl1NWN1PdRtOCu7weHrpmG3ADJyBYWxZAUpFw182_LLl30MQS_-H6v6P-JHCAQZ4wpphxNdAKfB51uwdz1JnAQdDIy-ZahZ8eAzrxtlBSAnFDFFYsYZr1N2SvYK3eKN9olVthy0fbnIHvLxQJNJd8OdEAHu52S59SMtQDaV_IXe3UdDp5g_Dagiixs-uGNfNx3IbgyRK1xOcq231PSg3wMGkecUEpGpu5tDX2B1rcBxb7XoBHd2JUGFHAY43MlBQ_u44JFu_qJ5C_veKcMHFXjF3-EEdPTV70BJoVYZs7MEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VME9K4RT3iCl34PnHAZeUb9EC6RW8t8pL26tIzU6vC2jLQDO3FfBGlJQMp7GA2LX8fzSMTRmEm6UI0jHqJTsi_HloYJ66eVf-BKSNUJLhAH9OELULDrvp1pGPzPLDt10ZdhbvAYDXnJYMR-BOY0fnHfwUF4--av9y6Ygi9VH0Bk2FxOKy2GVkDdd14-C-_bgJRfigmeggljNSJnnpyr6_Yg2VQJ-5cDYThF66j5KWwxkWH1fKlNMu5VcVD6ZC-nf7LBULqOXjx7ZpSDvRzBJ3D_cAueHLsSeMfvZFLVw9j_mS1zxS5qjwDxWslQLHmi-Yv8AlkXgbzcNPf-F4cBP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR-Ya7jPtEVUDY_6o7KAptaCbjNhVifM2rkX__-HBGjI_sk2sAzjZxBapvG9_lKJdQYfaSaThkEh1_5RXInbifakPw10nx-yYCSCuEcBnQIX4phN5a61f-Yq2pCjQbJN6KsKGaoY8gvUW7k7aWteJkNhcgOr-LcpYRu8q8AecHr0ePN7w5Deu0W0lp8xNh0SBm3pzgCBnKDlx46E5DMhplmOnYuxaNWbwTZQ6VPyXPY8HFVHMDG2FmdSS_Z-zjSe58KYUuhx5cLdHDH39PauFpUZbDOH3dOPfanJOvEcTnkQ4SDSWBot8XDVwj9vhc-iayeD5HlwOJ1HrJgHFOXnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIyfhm4-xXY6hvSXYdouxvh0AaY3xNrF6NIKkYjfCuzh1FCDDqW7pOFgjMNdl6gGVskEldp8z4rIIzJ2D5tx0xNtMd_A1-wB-4GYC8qOgo-wWcZgL9Ana6Z-7meWmW0Obb4eY8yN2VjGxVLIVrbTKCipv3Ra1JTj-SJP9xcw5XZaYR-ZllCvsv33NtB8ceO4Je92YEHCA0jTJAxv_r3FfedmjSuwX1xuC7D0dXnqS54NVOzz1XnBEShTY9N-bOeUhcDb44Qbzy-f6tXRTS8qcIiXpRdzJu5U_6660J6EHiWFJF2enXhAqBT-q6ALPrxUEpDR2dwtSAGmXHVXb-lo9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reO2uPjupq_eo93p1GYsEVDFlQFxvS9JD6Cxh8Nnxc7-4XHa0NN1IAoT2ZLXXSPQ1cRyzFuoQ14DIJt5jpuVey9in0v0vEcKvzTNEt_bupskG3jp9aoe7cwJ8Fq9vw9yQao_wwpvCDWjU8C-37tgyyi3VbHj76HUk7GH-AeRB8m6WbZ4QiKzMYY9WhPqDmpdS6KAOd1LJww-50HnMboCVCFEX8jAcF91Ak331d0m5yzFqDHzziExauNUvyKi9rCPzsHJNa7Eb6gyoLZjPCBavWjqq3OtUFq65VTM2fHCn4CCpyWi8EfI1VzkRFVnI-I2SULs1JgOIIpo-ZT2BQX_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=LZiq8C26xUqwWxclyEhVH04X-F22nB6ruYfYsVcuPlR-qL_KvyNknJeljeJeLL0bKGva1LT98IeSblxViIhkzqFT88Ucsg8_pyuiVU2tqqpiZzHJvXVG9QMjakJdo59DgJB8K7r47cKii6V-zfvOiNwBa9x9T_-_j1GhJ3vHxfb4aeEO9Yda0baYHD1cgh93F-G6XPiJ6mi4HGW034x8eL7HEHy7jePehmUqmRNtjojJAZS_U4OrdSOub-RjPM8uPDJgwrfgdpXShSIVX1CUZIfTqfVB_AAtUTO2rmu9z-0zOzHN7BWjlW2ud9rUG6k6d3zGHVC8FHqtPr8DTphgbVKXO8RG2cN3r-v2VBPo3FTiiQpmQkflqZ-0UjqVDCT_Fyw8Xbyyy_t357qAcB0T0WZerMEGAhPdJiGOYoQgUX0VI4_q8S4alLHXFMyLFtmoUPd-vHAkUn4AcqmQpfjxxEeoTRaq-scowcWiV5dhd5pIIf3vGMZtEWFcPspl2TWqMBqCwQc5KrHh4QZU5oPPit2BG2pQVERPj5TcJeMs3q6GVCgS1wKf-gwnE9gUtHzaGJ56QrrLELiDCinbX4EqV9957cuII7s2Q9hEI1qdJ8ppExin_xVWLCfQ7iSw1NBRyjwb8im9FjJXO5LF3YGkulfBgP7ARlzV7m6ufzvU2Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=LZiq8C26xUqwWxclyEhVH04X-F22nB6ruYfYsVcuPlR-qL_KvyNknJeljeJeLL0bKGva1LT98IeSblxViIhkzqFT88Ucsg8_pyuiVU2tqqpiZzHJvXVG9QMjakJdo59DgJB8K7r47cKii6V-zfvOiNwBa9x9T_-_j1GhJ3vHxfb4aeEO9Yda0baYHD1cgh93F-G6XPiJ6mi4HGW034x8eL7HEHy7jePehmUqmRNtjojJAZS_U4OrdSOub-RjPM8uPDJgwrfgdpXShSIVX1CUZIfTqfVB_AAtUTO2rmu9z-0zOzHN7BWjlW2ud9rUG6k6d3zGHVC8FHqtPr8DTphgbVKXO8RG2cN3r-v2VBPo3FTiiQpmQkflqZ-0UjqVDCT_Fyw8Xbyyy_t357qAcB0T0WZerMEGAhPdJiGOYoQgUX0VI4_q8S4alLHXFMyLFtmoUPd-vHAkUn4AcqmQpfjxxEeoTRaq-scowcWiV5dhd5pIIf3vGMZtEWFcPspl2TWqMBqCwQc5KrHh4QZU5oPPit2BG2pQVERPj5TcJeMs3q6GVCgS1wKf-gwnE9gUtHzaGJ56QrrLELiDCinbX4EqV9957cuII7s2Q9hEI1qdJ8ppExin_xVWLCfQ7iSw1NBRyjwb8im9FjJXO5LF3YGkulfBgP7ARlzV7m6ufzvU2Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDObvdSp8zY6p6LC7ow0x1a_0bV83UC1Elnx088WXaLd_u0qWQGVKzGw4t-2b9GoY7ATLMyBJcRQpEIKhhsIcBWKPPDWnDvSSzoJyIyHCAHpNxyiFf3WlQpRYQb271smZPPo0AC6XG6hGvRI8uo6Dyl7lWGaxqNY3yvKWSehWbPdTNSc5kp38tZPoCasaFr_JYSa8NCZc4SlL7RZ8knsSE6rFybCschcULan_o3rIxaTOyJYxYzkdPlefgGU-hwcbznt3Trt6s4risoUIvWrMps2yj_MwHy3SWHupWUE1KMywMbAsUq8E06QecMR42A1E8uiVHNfS7Nw_NS-ddlzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6wXzthsNyrA1uOoPxZ3XrZ6XWhtRvU7g2sVuHWzXk0z7m0JWg5hdMZKJrku1jm1kYHFYvSZdCwgljV_0AzsbNXrdth4LqwYFlAHf46Heepfrq5My1SIRceH541IHbvAKKfPvrwb02D3kiRDR3jv-tkmz5zxX4mbRS1Z2hoejZGdEuBcJPkTbw8gKN_joFoQe_4L7r_k7TJodee8Rr5t3P8XLcBZhnqCUcbqR9kx4SYhfTWuksJeuP72y_lUzmgzy-B7VoZea5yeiCclqIPL6Qa6AB2zqPOFnw-KmkAYbA0WNJnnw7YSOrzY4-E6MAEmuBZc-YkJ012q2_4JqFHhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkZ1Ldb1GlfROK8STbZawO7U2kpYNA8Hr-weRwtjf3ib5dT3JpTvtrRWk4LwsOg3aqCgGyfgErdgrJC-iw9ghIlVHvNqRNTsKpiUHxPUNKDRtAQZH2Nae0GMO_aFSHBgPGDPLjTNvWudSCtnZ8cNT0j-WRq3OH370synbj5T1Y7a7NFTlIAUfTGA8OfKdmDwxv2PzC4LOhX6MRJBJa9jbzixBIWfzqhzPMbIJgELmsI35fPEWCtnVg_aN-4XRzbO9HTCJOt-Ao-HWfeUt0cX4bvZCWOgQar-DAmTcQ3e6_6edpSYVMFblxFKfoz0sP18eXOW0wzD2J4nIR1xL33S9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErXHRkzj1mAxWJQ_ujYPoMLm0TdgFWQ_W3ek6GjauM5JCEJWNz1_HcsKEX2oH4tREVkskr3RmORCtyIq3xpIn2SjsAevKvq-Bk1LGP8HLHPWBgFZbtXViLqN6cwYtpagNQ4XUOiQpBjn14Hs6CsvzPLuzo0_MxOJr1Gn2xIqYiL0G5_sUKJbdwzrfJTnAxrxi45EfMkLtv2WODo82cbPyt_gUoGs9X3Kl9TyXDMRsqMHchFZTK7DxZYOhnlNlg4vvmoRXqLPnPwyu_LTbVRrkzxpnMUj4FeiVgVqLGZmsc2CV5D-ftHXbhD95YngJp0NQmJD8acDms1ddjLfFRLEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3yn-09Esruwb5e6Gqybdc_8FsQJRfidqMVtdIGxHeD-wqTdqAKXl2GUzUlXGfDdmWwDs39dNFiHFzbz_UYb8ysFXo20zhs2IgW5D-XZLFM-K_THQ71dSGUWOT-vCnqRJlj7HobrHeQtQp5jyyCk7CFRFSw92ZMMjL3BvJIJYERDv1TbJgMlRHEtnoTDv81smrHziog2JfY8-5oxGV2ohoRE9RqEl95OBZKQxgjlFHDPNRBVvdHgXwJ6KmQKRimVFJlf2fPyjGVvsAAkXRTPFRU7cw4m5-HTP4fzNly3lGFZ0EGsQ896PJ1t1A52UzSYQsv80JSg5vtKyCYpVHzYbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6pirnEhanEAfdU1fFgMrlDSrHTWqVc9_8CX53tnuyVivvqxBNwVT59aRqjAxaQ3z1nNDHZv_q6gqS4DHE4E925jLKZv2EPdYWXGjaXa9z16Ekk2bviYc67MKKkEMaWlzEyCqPqR7yGjShx_Ca-t1Aeudy5vkljMhhjnGsAA2hw-6c9yExYQIIa91AJT9AJHwyvklPzk1N6K-0c6UmIGICYbC1QXlooidCx8602rrpoO7LAl5xwUzdZ82EHmh16xv-Dd2mHY3Ga778z-k7BacvvDz3ACqSdyFVFiuEkAdRxjPdfaz4JDU0Qbwe7tIdZQux4cqg7svitn8QYZ8vWS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا
#فوری
؛
سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=I80nTItZNdTCKkfuSLXF8wcSU3FnQl5Feis8oFZZVxoKFCjgDmxdAtmJN-QB7Dg1ZV-3QsTRbX7KHLrFpn_7vGtN3Me2zCgmupIUrFRqJ1KBH4WdCjp7M6DV3cQZkZ44LWT2cznpUfnZaO1p3flpz0DvcAH7Zn9P_A2SU_OhFdgpjZ7c1zYIPGILWATPIJCK2hexTXt-zhvojkPq9DdFAEfh29sMCcpGlT9HSZCt89DolNZ-oWsXKjrBUk2Ay5d1yrKqQEt0_MXsXIRXy8csBWrr0llyz3UiX8v0aVAglAKth_CrcmnLL4SC8dvdQbFVqGlw0R1I8Crkv6vImf-B_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=I80nTItZNdTCKkfuSLXF8wcSU3FnQl5Feis8oFZZVxoKFCjgDmxdAtmJN-QB7Dg1ZV-3QsTRbX7KHLrFpn_7vGtN3Me2zCgmupIUrFRqJ1KBH4WdCjp7M6DV3cQZkZ44LWT2cznpUfnZaO1p3flpz0DvcAH7Zn9P_A2SU_OhFdgpjZ7c1zYIPGILWATPIJCK2hexTXt-zhvojkPq9DdFAEfh29sMCcpGlT9HSZCt89DolNZ-oWsXKjrBUk2Ay5d1yrKqQEt0_MXsXIRXy8csBWrr0llyz3UiX8v0aVAglAKth_CrcmnLL4SC8dvdQbFVqGlw0R1I8Crkv6vImf-B_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIN5sYFGN7LxeDxtyjk4r0VxcfOGKcmWH9o7brbG2Obdw_ZzFq20G3yDVsM5evEuKz5xVXFZjnfVGeaYauFkXf4iiH9pkrRFf9HyVK7T9Zhf6ssCjsxaFe1FmWJoryD_xYjJHIeGfWUkGLgr4fiWjJeDiNvnzH5cuTvwW8KM8JP2DWugOrSj1PeAh_rXvTywr4vr05f6xksVR1-3is8i6GQIXlWc8dbiErfB0hm3t_sxedKo_DYGDMsl0mQ_zlhmRuUd9tJlAFh2fbwlI_f4KVSU8hS6_gCNKAWHgojqO6knzefD4UUnBLCIxs_hadnX0CpkPXG7N-51daOQ0m0dpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjs5bxTjsfcFshbPqq9BCg5u6eOW6GOx-hsPflui3N39Zlh9UbNwsktDzrbecJmsJ9OBIT_ROIhdjkz7DDOSDu4jxaA2U8XiQVUNXBqU07bASFXexGfeOVvywAn2ArCEqd18YDN30IwQ2TIxQ1aw3Fr2JxQiuml0_IJetemYwBWnU6psXQLBpOssK_IxE79Nz1pPu4aWmwnC2q9__geMP1JmfXCvGmHQUfGbCnCRG8rG8VH1wW-F80j-EhkXG70nifxoN4edUFdpcteEz6WoW-esrc90iN68vlAJM9Q_Vh90hl5tH7Vc4HWw5ltb3_c_luSiVVzoCG4Bh7XZ_7WHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=JK3WHqBfwYN4gj_TR7N7vm2a_Kw9qpeWi62HkJlilACXSsn5p78PAB8RYrjlDsFZcNrnL2fsmHOsFe98sOBygHSylDU-moR7X38ZsBkqH283aXbGGmVinMAf0mB1qZEgf51Hyp1brcEh72MIqQJB04mZh_y4XwJ72I6sTS4u7BeX6YUqDaq7nXnrw91AhpMNARA2F4WOdQG5dkHZxPFGwH_w2sI8XjtEwixucCn4FQV7i-HWAzsDp_fuyfOCShKRKXpNBCrsngGSYcuDaOh-1QN-JppYEI29lSgZg2Te8ZrKldacnMhc0uhaqLYmSq36G8c3fi5sd22J-1bF7z-0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=JK3WHqBfwYN4gj_TR7N7vm2a_Kw9qpeWi62HkJlilACXSsn5p78PAB8RYrjlDsFZcNrnL2fsmHOsFe98sOBygHSylDU-moR7X38ZsBkqH283aXbGGmVinMAf0mB1qZEgf51Hyp1brcEh72MIqQJB04mZh_y4XwJ72I6sTS4u7BeX6YUqDaq7nXnrw91AhpMNARA2F4WOdQG5dkHZxPFGwH_w2sI8XjtEwixucCn4FQV7i-HWAzsDp_fuyfOCShKRKXpNBCrsngGSYcuDaOh-1QN-JppYEI29lSgZg2Te8ZrKldacnMhc0uhaqLYmSq36G8c3fi5sd22J-1bF7z-0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsc7_WqgsnCTNwdAUYGxmBWY55pE1AomIYjgbVSmBqOrhDNC8uk5h46_QChUy4PrYuyqt2kH3JwWXS2TVV47Qe3wDAGEB3m3Cg3m2Eo_4qxKQln6yzIFmh2wlaVQ2xkPvfDw9NfUtbbGiuLL5yCzkHmOni0AGEC34lmqhSLf2aqymrHOtpehmjIuH_eEQt57q9Q105p2CzoYJYo4wSdJvjZX6Qg8Q-SjJ28_4u6P_hGjAXJ9PddkFHTxXXMzIQ2E_SZMgrCGJqBUQWQiHDklkCn8haW_35EOzSksdTf0BSPwmDlW8fUWBOgEc98rTRjXnafxG2FcF6yzGdISelWPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=Giiw11oOwBugb-O7_1HAixbwjxkxMRpLIcNhwlBYN6bgqIyt9hy30gJ3n46aGMQUtmE7Tumz4vxYqIFFRw-Eea_E72NHRZiv-vP3ZAqaoYC_nnu8c25ahhpekVbhD-g83Km-NMcZrMa6nUEfQuv0s170KRX_MUberzWXErFU5j9zYWp_bbyq_s5_aqzOUlIr0D2FkbYAG6O47kKzxWmzPelzumoq14gsYLpK3kEy4b4tROKRBoO5FvVHHxtZ1ccY34nbrSWivgcnK8IKuHJp-u6sVfO2ijFS0roYCy3BmLIBRTLBi6agBsQIIGfhtcddcFT9ZBaoRGszSf6oC9nrcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=Giiw11oOwBugb-O7_1HAixbwjxkxMRpLIcNhwlBYN6bgqIyt9hy30gJ3n46aGMQUtmE7Tumz4vxYqIFFRw-Eea_E72NHRZiv-vP3ZAqaoYC_nnu8c25ahhpekVbhD-g83Km-NMcZrMa6nUEfQuv0s170KRX_MUberzWXErFU5j9zYWp_bbyq_s5_aqzOUlIr0D2FkbYAG6O47kKzxWmzPelzumoq14gsYLpK3kEy4b4tROKRBoO5FvVHHxtZ1ccY34nbrSWivgcnK8IKuHJp-u6sVfO2ijFS0roYCy3BmLIBRTLBi6agBsQIIGfhtcddcFT9ZBaoRGszSf6oC9nrcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op8PhbyXCxzA2NRx2tJ8DPbwaQ2TX7J_-Buw51d38D2vmsTH3gmMfZQcf_Ua58-gOc0vhrAijeK2JnX33pUg4Ev2OPLdNb_s99Drx_O5OkJ3pGBQsKew5gFIwFJbx50cD50Y-X8y22W9nPb8RahAnPMMjD4GQorweBLzukinh3npWz0vBdFN6ShHLDUbvnr_zBR7cg_qlqQ6kvEMSbCvlr6mn0TaAxm-kJl-pC3m4W_gRqJ5EcqlAw7X8ted1CXRzLribHjIJlDCIiI1Ykfwrx2d5f7ozZWXOATZ0UJgfu20e0jE3JpyuCLzrkmdHOoLaSe-bCGMBpVFIjY5H9QUsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5cz05sCyvQQDN33i_l7jOCcsq0AXHa0Xetpg8iY5xVWymUEsfTN3PVYJk8ZGHEgLSgw-2AaP9r83apWQlcUdbb-9qDHa2eQbpW2QUcwh54g7FQS5sua-EArfZ-hw7z3g6Jv6PMpGZNyiktWNSZR9uFuTHxmqvlEjATTQBbn6FhSsEOSO_7xpH1LfsrG75A-w44yp6tvFha1VF7pNbbWldnjYwugVuds0jNdP5CQ2-2pzeBZsnoctt_EKWxk0ZvxD2f-yD6_fk4Z5LRcnU09LR8yiXPmy1QFlcITtJWQwqYSTSpXVuzgUeRXihTSKvmFyPQzAlk7frDxswBgjZd4Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=ZAPMsglfKLf0TGNVW23NEsUd_3ARFmOe_MqVKE0FJiyVknqgbK0bL-LFO-xpQalNoRy2YGRXmgmuS1cM0Ab_hcA2yvo4XlxyqcMuI-33Qng09EZL5qphnX0IYvpe7cllUZnTyo9fN0gGJRmTzT4e63D5MIB98COy8w4GXR-K7KTgEGVneU4qPX-C8zj4gZlFBkUoFZY3fHQv94_hCEil6EgeZO48XX03WFQxS468BRQzIHcufcf3IPn2VHyEWr4S3CnJ-CuleD299iPpekaVkr1XA5oxi9eCPdzQkr2MPp-NdPq_6zI0z83nO2Owhl5jkKxmMcvR_RQaczPMyJzR8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=ZAPMsglfKLf0TGNVW23NEsUd_3ARFmOe_MqVKE0FJiyVknqgbK0bL-LFO-xpQalNoRy2YGRXmgmuS1cM0Ab_hcA2yvo4XlxyqcMuI-33Qng09EZL5qphnX0IYvpe7cllUZnTyo9fN0gGJRmTzT4e63D5MIB98COy8w4GXR-K7KTgEGVneU4qPX-C8zj4gZlFBkUoFZY3fHQv94_hCEil6EgeZO48XX03WFQxS468BRQzIHcufcf3IPn2VHyEWr4S3CnJ-CuleD299iPpekaVkr1XA5oxi9eCPdzQkr2MPp-NdPq_6zI0z83nO2Owhl5jkKxmMcvR_RQaczPMyJzR8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qi5rcjBx9GKaTsgPb0Lnfhrf1fPSELRhBGObPb59Ys8CnrbExPaMKN-9mMdKPWD-YEGgT5AZj7wpsCjgKGIpmbCnkC2XCW51-w5ja06e4gHveWzBCP_KGllLi0NrgM4Lxae1R6_0jmqNO__ScEKFYcx_PJXrYsniFSgyMsk-lzKr8fxI2cuVe9kPg6kbq2ydaeY2Y4IsScOwP52TF6Xwzuh3Hsgu2FayXigKcoD0S_d2Mr6-etEulpusfV4iXGbMSdOS3Y2q8JM6kNYIf1GagnltgQxcxn5fFZDzTnh4nf9NycRQN40FQXIjxplor1kKTZrtq1PgckB2SDZGSqx-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری بت ویژه ی فینال ویمبلدون
🎲
بدون ریسک در وینرو پیشبینی کنید و از تماشای تنیس لذت ببرید
🎁
🎾
فینال تنیس ویمبلدون
🎾
🎾
زوروف
🇩🇪
✖️
🇮🇹
سینر
⏰
امروز ساعت 18:40
🚨
ورزشگاه سنتر کورت
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
بابیش‌از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr21
📩
@winro_io</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25496" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=Ojbey0Z7oYrmF44Rnfd5dQN0UXmXbTAdTDbXoiYSSruLC9UCC7LvbEku-smAc00OFimLkhaU1FbvlSPh9o4unwbjKAHvXyH6r23ugyZ2GKioreN1CVq0NOxnLJpySWg1Ds_PYdUg_1lnd-4kUF5DCYBPIaic5gaFI-0SOTMjfRFkGwFvjn1t6KM0YxGvWAFF8bv968PADzJ7Sm7ceKZTd7KGtW9BoX-CF9k_s9veCVPzrCwiEFxjk0HLgFr6Vq99XtGk4wRieUGVUcxhONK7djQVFjZMcHh9t8hG0d5SzWsLACOg22P-uvvz1082boWqBz-gOGvw1Gvgrm33HEjZ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=Ojbey0Z7oYrmF44Rnfd5dQN0UXmXbTAdTDbXoiYSSruLC9UCC7LvbEku-smAc00OFimLkhaU1FbvlSPh9o4unwbjKAHvXyH6r23ugyZ2GKioreN1CVq0NOxnLJpySWg1Ds_PYdUg_1lnd-4kUF5DCYBPIaic5gaFI-0SOTMjfRFkGwFvjn1t6KM0YxGvWAFF8bv968PADzJ7Sm7ceKZTd7KGtW9BoX-CF9k_s9veCVPzrCwiEFxjk0HLgFr6Vq99XtGk4wRieUGVUcxhONK7djQVFjZMcHh9t8hG0d5SzWsLACOg22P-uvvz1082boWqBz-gOGvw1Gvgrm33HEjZ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCam8NhIE61shhlp7IKrnt5ycOtv9UHDFMBRDReXAt9z96E7Cb7xqOOohCOSarHNMLeL1YeGOOvwowl5FN8Hsj-Z0iPA-7RWpRpiVy7dOsII2ZP2uTUlu7z37TKMeQUqyzSjtvqIQnl9xlkRReOl6rjaj-eJTgSnxMTiH0heV8gjAKmbE25AWKJ_p_I2mAt1EnObiJ9IUsTEW3kP7dH7YDXwH0ZVKQrdNGuwsIQGLvUYUzKumz_m5q-qz4a-wFkddnjhZND2i0qphtzF2kiAKJIXV-x7HwKmf04FWXBMtMOZy34n8OAEJBFKUtuLqWC0b_PFwbj-2coRXWxhduJh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XC0RR3O-WsF244sfCDcXk-iYpQWz1ij67YCG4nQIE2LjSNIMc-E8uLZ7xVTqJe-FgaBsYFsU9CAXkB69ZsCVhAwUEfdLrpIUpHSlbmjAluCtes4EsKnpuyqqSy2UQBt1wReqApia_iQqugUdXQLdJlGYyhx5NYg2wBrV8SqMmGx1-z-sIf9yz5WhSZuA3Moos26kHf0EZmq7V88CadV0xn07msQxVB5mc4-eULqjuVEBS_A3K8Zpx97ozQrNtzvpwVRO9zo0HFqTFXR8pPDHgfCjs0u9n-9f-1eDSM0xnTZs9uOCwU0JmA1g2Mib2f8GrwYGQlXBnEt2Tjbi_A8U-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=OxS5pln_9WuVipuUEKlr8uI_lJaRgPz45eQkwylKSYvXRzvaOIzbhhYWQfXzAJCteq5T3k0mMuD0raItEi5AdBMB_fgoYy1RxCF4ftSTF7leK319AYh7na4r5CpIuJ1ThN_AOc0bpuoSHMpbRcuGSRG0ppgECP4nB0CUQJmRC_v9AWLG2jW0rqy-hkBxWMocjbxuDAbry_Wgqm_VayiRSLNeKIuMNxuOcg8MAxDUXDw6WJI-X1mGkFYdTgwUFxhVGTb9iHACdQtRk_htzK7tRTLVDxH-dUPOoxbpQgnoWsGc6mqQQxYaps3zZTB-uZMwVlaoVYfFghIWihk7g2FWaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=OxS5pln_9WuVipuUEKlr8uI_lJaRgPz45eQkwylKSYvXRzvaOIzbhhYWQfXzAJCteq5T3k0mMuD0raItEi5AdBMB_fgoYy1RxCF4ftSTF7leK319AYh7na4r5CpIuJ1ThN_AOc0bpuoSHMpbRcuGSRG0ppgECP4nB0CUQJmRC_v9AWLG2jW0rqy-hkBxWMocjbxuDAbry_Wgqm_VayiRSLNeKIuMNxuOcg8MAxDUXDw6WJI-X1mGkFYdTgwUFxhVGTb9iHACdQtRk_htzK7tRTLVDxH-dUPOoxbpQgnoWsGc6mqQQxYaps3zZTB-uZMwVlaoVYfFghIWihk7g2FWaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBpBjrR7VLTjRd6LntQtvTmXrLjJDBexlXt3XSVEQxNqCtU2WQby2_yRQ00CA9H4nI5pvX9_ESJqtLWUKMDT58ickBMx1MKZ41G32r3JgT2YJEVZVWjujOXWVd8gNfFKxtZPpOkAa91L1_FRzNTphUSD-YbnP7ie0ot9ZDfY1ttG1KJPJHDKqVtR8CHo15SkV-UNKRkKrj4g1V4nHPukETkc5jbAxo_WpO44TDabmDoZ9iqFv_2saqr2eBFi2W-YeYLE46E5AE8jCyiig3KURIkmYa5uHrrHW3SjDit9xWmdQrTzQWK3EBgkA27AS9Eff32Lfp-uVUuArtC4utxSmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_qG7F7x1bBRo6PyjSM1Di8x5c7auLAwBK2d7RmqZmhXq9WWwdIGjPhgq4KLk-iGG0KRRjyLEcxFEvXS7ZGTlDBxrIa3Dy0TrO3wXsqBlBrkHTX1Nu8dr77Cy3sti3s5VvAxOxa5MnqyTJtdMntbOwMip3-MhtQaQFhuvmJ9UeRKXNGFigTWFjo_Oms91KC9jqCFUiMy1KhuX0PZQLywBCa8mMbX3qBuBs0cWc9dTFUzzrs8YUXa6Pfp_ykaNKNzp-DOfHn4BvNDD8SE_JQTF_CU156fj8u5kBH4C-bjFibOyn6CxBv-8T8eKBo3XVFG5WjO8_TD9PbtQ4-nAHnbBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8bsEM7UP8ZuN8kaNgUYQN7pIlj2cyflHMissfuP8C18fEdOvRKragqA0qc4OMY5_R60jtRu9O5OHUaurvkZ9KZvocZ-_wMgCIvnRA_QwBFjncanfZkCJCr2AIekzOnkFXIb0ml92g2bG0wZ6j9N5gbD9zhlWxPKxIQh0RgQ_-Bt1X7hcXVVGRGEb9jYTs4xixKeX6XgEAamJlUN6aYE-DrcPeIuB51WWMZiKPIJnbX3632mFhT4EJg_hQPkERBWKW5Qx6wbMehaHCVJf7-gIb4SnKQkSCkItcUXXvZzCaFPLkh3GKIyfSmOw8yGUpFGzAJG_3jds2YyKySfVYyjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_BXA6loqpM_txWtA9Bbs0TBltACf0FJG7hnxcdM5Rvn_xVnq7LkWbICeRNx1K-HmYivX83c9stLEJxSPLn1QEwA-vS38jDUHx7BdnlfHu9_sUsVB732WhAZR3q600mxnwXOINcVxyuvBpiZDEgUHLv7yQzlirCY5rnK-hbYzGU9GSFVE4a0I6YAhowUXcAlDk7BJbNRvqEyJqMImeHLmyFsOjih9nuKO3_VnBJU87y5kgsWjewSHN12keJZMmk5RxDuJTTJxQM8VM45gUu8QbPPowCL-2Z2F-x4Utp6-kEJ0gEl1fA8olGVGPiSiOTiHpZ3Yw1RP3F--gXOv72Y3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_RikaDIb7ZZF4kYBygEtIa4Y98QcXDZQSEwWStfEiROSjCxPYrUN3liTmwRXtj3BNXHvOAkiR86CSrOE2TgIfYalRyOC_sALl2RUA34c9pygSjiSfhSWdYN1Hi69oHF_dOK8m7vtSs1h8_dyc6v0795KrBg4nRFyAj2ZQZqL3LXewbFpPrR20xo3rCxJxLLPe4PTzJFFWeY8vFGRJRFUDJ-7wOVdDfXyQUK5g6lTxTSdupHUWlKFFgbA4HsrvKhA261mxpK41fP5jqpJzgNg_4bD7KxDFeU__2ZfvapoZ6YADrL3pGrHiC9y4_Y7z4ZOKK1t-Bq5-htVdNMfDsAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcR6_mOgBqhmIbQicjw1J6gb8yD6_gpOstgH-R4PTvYY094kvb2PiMrh3Qi1zbLUxFF_E-Fssrk8PBC7fxZ3FkLy77teYRYIW8LIM_q60vhVTy49_2k29bnuwdd8ni7frxYV-iRCNrpPjT-nX9wu3192X21NnoNZdnvCcj6ikypz49azy7tTr-q7amkCDdnMrGgHL7O7k-nyz4aaLnlbq2tkmAQ-Hmjh5HJjBg0DMGckJEOu8i8BYCHFUAYso0zmt_pLmClII-bTOVePh19316-rzJciX35d8v4eyKAR_IG_mvfBgPBHUqejUqpsTLM_stajbh3VXbCxaXRa1HicCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=FSVV2hHG2c6gAleC7oh_8JMM4aQ0O4ADXT6krm7WSTmDbFF97Ae8a-txLMxtuf3EvZ03AZWFZ_kpwqdI-Y_KFIvlBlfmAgELar5nGcBNpRDx2D77hlOb1v1kNvS_K37CZxWF2DAgq5blFXcd0lhIeSBcN0DqJFCD7Pss83jea-xFLgon5vyPnSOufA-XyPS96Iea41Rv5XPnlMBpAA_3_fE598p78yRg5Bt_grP5JTqiYA1stp3imb7M51RM8wrF3k518LqL9dx_pK8PrNJQHRTnUpo8duOyp-eW6WLwS59nzC6i_lTUHKdCAZQUgmKzOD1M9tCDurU1yzAT31EbKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=FSVV2hHG2c6gAleC7oh_8JMM4aQ0O4ADXT6krm7WSTmDbFF97Ae8a-txLMxtuf3EvZ03AZWFZ_kpwqdI-Y_KFIvlBlfmAgELar5nGcBNpRDx2D77hlOb1v1kNvS_K37CZxWF2DAgq5blFXcd0lhIeSBcN0DqJFCD7Pss83jea-xFLgon5vyPnSOufA-XyPS96Iea41Rv5XPnlMBpAA_3_fE598p78yRg5Bt_grP5JTqiYA1stp3imb7M51RM8wrF3k518LqL9dx_pK8PrNJQHRTnUpo8duOyp-eW6WLwS59nzC6i_lTUHKdCAZQUgmKzOD1M9tCDurU1yzAT31EbKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtCR08oEMIJS6616fgMCBQm_h7uAMrnZ5DPk7IV52vikt8Z_9Vv66N3FZ9KmN0WjJHrABfZ2LW7CE-tFtdV29mtD98E0U97tnYrryVOYJc0lgOeic8Ri2iAnFihRH6DEkkBelTjG5H9DdCQNF35m2YqMLF0K5FB4O0KG7DawsUZHOkl1SUKjrm8vUeF8ooYT87j6sXSrRO7n1cTR3c6iLH3fgfzo8QAGQCmzehgkKl_EDZeyk_Sqkw9dVEqFlHv5TeE5IEiuOtGWZzbne6TzEY5Qbwlbn_1UxLzbnxyahC5aGJrtl1c3N-4JrPgY4WKvb-klVg0cOuMGNBUGV-o6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfqFP1D7wxCsmL92ONlaPIY_d0nyJ_b9bnJanFV1-RhR5CYX264hHB7-ZfhXcwblvjeL03IfF0IyQ-TxOWMbX7VJSYr7j-CYf20k6NgjXFrPAGGObK3YywXTo7QxtBTe2Ag1HqNm2yjMRVlE52JeVAgY_RoUh2BW_3HN2QnhvtvfegBQTQmqKbsnZ-_8DZwnQ4alJRK_I0B0iuCpjHjyoS6Med25xu8D4_aZHL16J03JYIv04c_VT3iKcDSOFNwnXIJaXtryX7yLwnyHN31sql3uS-6MswnJz784LaBOcoxWYyqEkfKwt95PT3cTeHZq1eCW90Ihb8LOBSa2FwY96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwfau7koQdUK99nZHl4ArmDKeSdrAg3zW3fDYOSAU3UtxUjajhfRAqSFDPUXVjQywNq9OyUX7-o3ZsTWG4VAtHzonpPzYkkvuhu31wbGJR3Oj24SN8nW4Q34krdFskeV9nV1xBay63LCfLDFBqSGlY6qezp9PGc1GEwAsVWT1xiQWtDJbMPL4I_CUrRKCEtHjs8sFFZr_5rOvMQ581J03AxKRStZgRxf5Xh3a_lVOXONBb1mkp4YylPgtZQQvHqImsRb0Zgli1_Ba9rWAugBocDENic_bumJMYCX0MKPIeiCVhrs_VZs6-ELpCDlIX1MfF3Fn2IvFXXjl4bCzzEifQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1FDKYgF0RtMCcqAFlPp3Ut_4bPyYpY3TKfgFg4cF5sE5nKP1cdvGrKWoUVSVHpLtWjJDoJhEFSlGlFJEHhF_07k91CwSk6eaR_3dwUuGtYUJv6XgV7DXRUdoqi2w7HlImBqkIJNfyvPWDmxaQtbLOaVMpYNg9598WaCMoMkQBpLph_OZUhIjxp9wD9Cs1OuUvaWBchsRpL_8BZS81IBAHmL3cqNcXN3iUc2GNILv4KrWaDMxeHI4myMpcXDzQWhj2-A3DOuOIgmgvt6QDvBtMo6fQt-vZRJtJwguVj3opiEDTXjQ3zdSLilLjw52IxZ9mL6lqwvtm-dfk_xjD-S1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nh2CM8dRyOC30nG00SJxnW74VzU_CauxaEixG676LtDnWvalbBvEfbVSA3iunetr8rn8e1320TfWWzh6Zq9Qd4L6ZXhRny4m4EeI-zW7lz4PNjvGVtdYFEIcBsH9gtM2wgNT1QTcm7EkbilNtaRl1Fed3eI3bUUWMnLN6eUsRbOIW-kdtUY3tCOA2CPuDxwS6Tp0Acomvmp0XrQjSPQz_tNpJ-Wv5LqkjZgsNDRZjEOSIl2q74p78wriNtg6WxwLKqRGGpfH25_BmXPM-8o7tvayzYHKcQOuTJC8G9moSdOJIAmq07yM4ruC8sRMzP7P1iwlq796YkKi2ABer32tQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1shiUAvTCIyu-j0qMumWH5VQdApWm8HsPdTUHsVvL04GKzoiKdRK0LQC-BA-fLCglmPKqCG1V9rmjo2nvfep9PwgfzR4LPWyFVqAGSK3yi10vGPKik_PsnrLAmsghtPYZ7BaNpgzNt7vtWW8vmjtWdHtva49zI-oGstsYDByJY4OPyFpp3SLRsYOzgm8FdKvIMXx28253r6qgcla4iDwNWYnvjAsXGiq_tRpuONrO5DbFWCqYAX-XnZmWOdGxqkF7RWoBEFax1gtmE5RHsqQcyUNK13eSw4GSae1CK_1_6BiKJziurm_NBdSEcRlwkTczEj7JYu0QOnlpKbkOJFaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1iYhfWvbG0_PxP71mQE9nZ1ftPjJxsIo5oGCjbmmsXi20UErrKALDI9S_fQtXyZwu6y3kTRR3HMr69iWOcOMUEcusrONIO5ERhjcoXNvuar8FcZVlgc6CQKogeneFzlHG1T2kGtmxsyCgtd5-DupfX7UeAIXh_IyLZDflAlnKHo7m_PS8sy5FLjgXqzjXEMXAmiatQp5Lzsd45AZFYx8kqBRLjzowZrnLgUx5UP4zALlyrKVAPtE2vUVtksjtnlbfGmCNpwOHz58qp0sLFkBAEBuEAxrOEg2fBfElzXs2ID-LWXuCEGIhpe6_4IJTGZP6Pn7ooecrqNNtaCOx1_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMKSpcxw4u_cP4CtxdnTCB6e9VGfe1ONMBKtzxZ8eFCRlU-l24HTSGsbhQ-wluQAFtbGqmWqwK79C9CFh7raU_j4s1xxNWgYLDDgvH9dEfLaL0keLVa5XSZVgVtzh4XnkojoS-e7-lgp1cqXUUE_8ZJpXlt_5h_l5IFsj6IFFC7WgKpBs3wt-68p5mhyJkTAlkpkymCNN233So121X8wkgchgJ0XnF7PnWDpwVzJWhpJz087w4BWCC2rpxNLpoOdp3f9j8bdzpqyn_eDyhNOU04XCwtPhwJ7YxcZO_wOS5O69xFEk1FQLplutI16qdcuhGbL3DEYe030jFRrUHjpHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NB3qKwe89i9A7rNENTGPfnkKSWVVUgJ11Wol_MRzuabvKvfywkbtLrFlLuNNQByOaZIPrsh5L1tomcNbrT06K_BcYSwpdA1jFdXKvcyqRD8DCDe-w3qUenBbvxxTmEWIklkmf3D6bvXOUV3LQVf-D2TdLjfOljDsTJjkDDyyfKiPFS4TY6gZugMIZqN5lb7UgBN14L3NpefFBT0WVXNRLw-3P9Nf9wWdaTebQmPp1meg_YsQAtVSZ15-L-rsbJTf-6lBBimUu1skIZBA5hNR95EqMzkWQweFzd10P_JbyAS2-h-leUpM0MfyC0Zq6y9gDT9uNMsK5LPqA5kmocDyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=vjfGr-KqHnMe_ETFQCVmiZe90SgwUHGpjZGbQhWinFn4vpRvak49WZb6OA7C-6Obijay2ujnw_Wt5Q5Xf2JKxEKgV3plNkZURyFzOEA4xsZuHDRqwDs1VXZHj064uoLDa0veczfuY8SKMF2mZ0HnvaGTPo5_6x-D8MNxpfFVcWhQ3ETZC-MyNfKKybPxCqT5ZgIMEGF1Ia1M2IY1VMKu04VB7u1zRXZA2ofTTV5bjjQWyI11W2isEwpcxODInmxTYdKVFtYXdhWOYeY80nnUgWmGAvF71hPLjk984dp_lZwNCWQUNX7ETBAUxpWiMwYDfJ5kiUtUOhbwq53ddXr2hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=vjfGr-KqHnMe_ETFQCVmiZe90SgwUHGpjZGbQhWinFn4vpRvak49WZb6OA7C-6Obijay2ujnw_Wt5Q5Xf2JKxEKgV3plNkZURyFzOEA4xsZuHDRqwDs1VXZHj064uoLDa0veczfuY8SKMF2mZ0HnvaGTPo5_6x-D8MNxpfFVcWhQ3ETZC-MyNfKKybPxCqT5ZgIMEGF1Ia1M2IY1VMKu04VB7u1zRXZA2ofTTV5bjjQWyI11W2isEwpcxODInmxTYdKVFtYXdhWOYeY80nnUgWmGAvF71hPLjk984dp_lZwNCWQUNX7ETBAUxpWiMwYDfJ5kiUtUOhbwq53ddXr2hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0ENxmSUplKLkKwGdeOf_fi_cVmH-k0HWINbNPFHAy69xLpc264aCJw5wSt7lzj97z-UE4axairGFMFZWoeH94bO1EVEl6TP__FNPoFxvFV9b4JuMmaswt19jdaEmYGuvHrppX2nShfrIUgiTT1LIvKgeh00YFw6sUR9FurpwVxqqbnTu5XIVY40pdmYihv4eT2KOhQdzOo5z2UDsv8wBdpqMjp9QMiZImyxKb415Qd46X8-cIRP4OFpPWSOCAzTuOZrTa-xGzDc3it9ZcSwENtlC07Qux0NxaF8PMw3CTzQaHRT90aEjvHhthkoFwhVylBYD4n-EB5oFEgwQLbNXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=XPwIHLhebW9lK_GrgwC3AoVj9NUfUpZl9UXcOT1nhSWjyqpTn5JtRzVVsVR7XaM629ey05Mr1naG0D98xtDzCa729TJ_FA-66k3QHPZtGvXBJyOHOPj7vr2hLM2XdrXughhFlSy1kdBZfcEBEKZfYeZv1KaaQ5vhxxJh9lAsmBP-U-igd1gFHg5pyOoqnjAqLtLyjoLrv2TWdn5VGYMvXqNwzuLXmnOESd_sCBuGgcoMb-nnk8k_6TjlzHcmVK6vsbeJlktAuW1KwdJ0wugksjepd_qSawkdTLZbH4FvSHwz9CAZtemIkvm1xL32vWZmBH-dxI0iL5d-DVIpV2fZcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=XPwIHLhebW9lK_GrgwC3AoVj9NUfUpZl9UXcOT1nhSWjyqpTn5JtRzVVsVR7XaM629ey05Mr1naG0D98xtDzCa729TJ_FA-66k3QHPZtGvXBJyOHOPj7vr2hLM2XdrXughhFlSy1kdBZfcEBEKZfYeZv1KaaQ5vhxxJh9lAsmBP-U-igd1gFHg5pyOoqnjAqLtLyjoLrv2TWdn5VGYMvXqNwzuLXmnOESd_sCBuGgcoMb-nnk8k_6TjlzHcmVK6vsbeJlktAuW1KwdJ0wugksjepd_qSawkdTLZbH4FvSHwz9CAZtemIkvm1xL32vWZmBH-dxI0iL5d-DVIpV2fZcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4EaciFv2Rws-Yd7X0bGpf6G9bvVp4Dra9dAyq9EPJtGagIWfAQl7ovRbVFHEGl5TpBpy2PCB86-82UofMqxXjHYaopP8Sa2G5fzQslOh8MqSu3ovcY_VVm12RGaW9cKqUHKEU8pU2jRnyLAaK9yeoUsPyWhwZYC9b3Gv_h_ADmbEWYJC9VIl6E-VAe-nOuXcsRXFvgbwrIP6LsJKCHzmaP2FEB8S0WQhJ-Giuaa3aWpHyyPHcvmMF11la5HbtJwemsvgfVwX_MlfDkvyzxf7jMrHqe3UyMupT7tlRK6X5KFN-tpBTmq47lEndmccg3w0ZKgCMB9yvwQaeh0QcRQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قدرت پیش‌بینی‌ات رو ثابت کن!
⚽
🔥
دو مسابقه جذاب:
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🇳🇴
نروژ
🆚
انگلستان
🏴
🎁
500 دلار فری‌بت
بین تمام کاربرانی که نتایج را به‌درستی پیش‌بینی کنند،
مطابق قوانین سایت
تقسیم می‌شود.
🤖
پیش‌بینی خودت رو از طریق ربات تلگرام ثبت کن:
👉
https://t.me/betegram_bot?start=p6_r4EF37DCE
⏳
فقط تا قبل از شروع مسابقات فرصت داری!
موفق باشی!
🍀
⚽</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEfiUbYL5ukEtAtulk4hECveLgwm3k-NlfE0DLwz4Gi-mTphuwgsIOl_KEVDAevXeJcIXn8nQ6lzQoFKjNCuZuBBDMpPOqsAE2CsTqGqe8WBQRbNuXXtySohBOnER30HiZnT25ydFpdiOwFvYbkinDmdrsmBdpAnNIo_lF19l1IsjotjowyQ79yr7lIPol_5lLdpvFBm0rxQcNYro6t8Y0A21eUOFXUYYhXhJpxNVS5yaDGCn9VFRo8H_K-rLxD5gL5NAUVUOOOWFVm9IsvJ6fVn55cy2nWPE3YP4Zrjt-fFVRlkY_WF2I_ByVl9iS370pW3SSKb3fhFhCQX1joPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kV0d3St_WlWnytdCHSuOiTB78HPVbrH5mpgJfKzJ2wlqTx19LOyxsjL66-fGsfOybxamDNYtiJuPqmQFT-J5OBooWKY5Ib37XgLjqPynmKzSHJV89OJKMZdHChFW16xnMyCscPiHQZFvb0Dj91d6nTmupoM_GUgo43WnHmtSSAe-HUzjhYII9_sXWdomTfKEm7CZzno79SEBp2B2UGKMJGqAegpL4PUw642Uz-0vgKeqHBRmIa4XbfwuscobhZ1QhIdCRuIEV8TkX56Slsd-qfivaFQXRAjQK4gUjoOpQQN67IZhB-owZy7zPaTktV6lE9YEahPsfNpLXFsI2bTgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=k_w-rVK7bY43avlxGeRKmcqt8ednge3OniGdy79lriLtywCgMq0y98U2wRNML3DZwqxA7oVNvmiuP7ECTjAzmE2tvHr1PUIRXgBrecN7f7zANtI7148QmXujYFe5yizJwEbCNO78efNVJWGA6l2tXKwcckdfZ9Sh-eigjzCHeeZPwNSdzunBlmYZihzYONexYlyVbODGvJKPiuPrCUuadLgNOQlShnQ-0JeCkxf7eNZ6qYAD_X9aWdJMkKoGoV6siu_6mInvqCc_yCDsTSoF_an86Czr2nKmz0hYIB-bCod5SYjdNkujiKjkIQjd9aImcaMWyhcquJZHS5lbVuZQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=k_w-rVK7bY43avlxGeRKmcqt8ednge3OniGdy79lriLtywCgMq0y98U2wRNML3DZwqxA7oVNvmiuP7ECTjAzmE2tvHr1PUIRXgBrecN7f7zANtI7148QmXujYFe5yizJwEbCNO78efNVJWGA6l2tXKwcckdfZ9Sh-eigjzCHeeZPwNSdzunBlmYZihzYONexYlyVbODGvJKPiuPrCUuadLgNOQlShnQ-0JeCkxf7eNZ6qYAD_X9aWdJMkKoGoV6siu_6mInvqCc_yCDsTSoF_an86Czr2nKmz0hYIB-bCod5SYjdNkujiKjkIQjd9aImcaMWyhcquJZHS5lbVuZQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNmomfT6y8IjDXWT7z1YGmdcvk1xiLgne0-e0Ml-e9Jz9qDcAD8C5EDAq3XQW3bUZGczaFe3dTJm99ruKg0U39xzE2G3e4a8O0HYQtnjHZuY6R1zB8iQHTOTuoztGaf78VsetNnOS1p4gzjTRf5-xHwEfk0BVVcKoMb_5QTHn7hS4tsAg1pL0GIFuhI8tjbNTMHhHHQaedN5fwLbRal0Ol-ebQKVe35sW-0T4g-J6P--yIMVSyNYXiiIHp4T0V8YvtUlBABn683B08y4-JJZYBEKCn_YeGtt8yreI85tdmm6Boigvnuvd8Z5f0SHwQYRscvLQUPwq6ntFDqDDDBnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYoN_eZTQXD9MILeuiN7QV0qhAUXPv2wB_kOH97mcQW2kRDYCvUg2teRYI9ye3w90UU8l53ZRpfVHWHpZhSL5w3ZCIIZdmmDDSHvLIZpyXvNbvpWhPseIKOZYTayHe4sZEvssVcie1F9hYgR_AQHwBNVpvdsvYXwlM2t_sU_79m19Hi-cOtkxw2WJY7-0X75aeCgkCwrobbCxdPGlCfnLJANMdRVeU8lpjXRqdwYdvhLrcLvu0f_MkvhuFodQqFWqUJK_po2UTm7BNiBMixWbICGc8ZrbUDLf339RigQzOA8zz3HuCN3Orm7C1Nn-qzKA1svzyU_Lc0J0ytP6hXNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ_09SI6lQr5YTFzBaDr1h3LUydWdqWIQEeD9F13G2bt6ePUAOD0dYRTlLk0ZVB-A3qhplWIAjGYr3C8C_dZPh9dTX7B22hodDKJHbRDrOZezkIh9dGWxg9_Xv0tsJj4pLGm5_XkDbmcAWmZ0OPKJAo1PTykEGSJEAmlHkz5UtYadrvxHaIVkvJXeWxKbhbkuWr4Pq8zlNMrSJYx387uq_yg2h92Z_S0-GozGbxs2NUWkOgUAm9F6JctvG0lGN7zX0-PApyiIhlr3wgXC-HEO3UWuOga85XAn-2nHiL3sD2XiOIsFXgtrMzd-30mylbnv0MsPb5AtCqBoAg2D1ydhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RohqUfHLCjg_IEIddJzgita2GKpew1Kn6m1TePLKr7Hj3uDiH1ox90PkEq8nsQgZPja9Wp4Tb7xyQP1n3cFMv_3kcLIUuanCMCw7NEPg7EMEfmOFDsgYSIA-FS3_WHRLkC4w01bHfOZUgjhjfiHyFDJwIQdKBMeABJtsoMF3HLpGwmyHLP4_S5p8sDaCQXT7qlmGXwBVnJvtSphtndU5lVpCY5m6pb3Gn6JCJoyROapuy1PnxgLU0XenQcQWUazlV14Z17XYvZ_aqm_iPdvHFKLxr5k8G8OdM4NtozoZDottr2wH9KxcBf6Ego9J_GMAzBs0La4s-F4jcBY6CKTgkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm-6175SE3FbG7yuwpUbhgZW-XIc9pAenQ5HH2n3awT6TaUaK0U74kcgvnHLwkqiVNauVUbY8ggxt5O891VPIs1rc25kDFVlWaKlAz5SWA3MiAQnCRxP1oa5Et27xxYqZLqxY2gHdtoL3Py1lAd7_CcX4315Q6ahm7ucS9ABRsQbpmJGO_8D54-80qTsVSR5qPTsDYzL-Hw56HisOipqN7X2tFK3dhB9BrIaqBD96fVIohOD-6efmwg8w2SMP3CACq7os4uxlnhsO7ZeZBH6nqdHZhvKP3s4DUwBUMscuywh3e7EiZ_pe8DXpFbXekcpuLYFtydwvCkwNg6xcJPfSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bq3iSB1Lzy3uxnBku23MgytAaMTJCDFhikmLRhQ2UCFV36-Y5FgP78nUv6LioViA0xnRzNxulP4Ugx33TUmUTxaRvFiJpl0axUd10l7UR9rtcV5vBwUgHSBKMymdAoDdF_aRFDnbEdHEO8niie4AnaSZpqwyuIMS1x8p2VuHty35SG-VX5xg7na_34Z2tS5g0Yqqyx7B12K-1X0ySu3zgFcwLULjHNWYlwTVn2a7_ytaIEdYZInpaieus0bwuQgiw3fYJyI3m1P2gd9636Xl-g6YJ1HalYIRNPuq6-tvILdq3rURpz_wCgQNk5sOuV35Z7LqDK1kcAZZRM6ycLapWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObIfN00zVQ5gDIWvZXC2JZSoU4tLSBnJg22cqkfZT3bcJh8zZqjpVwtkp7aq2Qbe2XQCfgq4hRp86jgAbNVycKp--GB2ceqJmYX-yobbcYE9ecDqJz9vUQ2YqboyzCHtdUU3fJxtv0WgpDWMGJkZFiaLJPqniDNtStXwTUwpq02IVWLbnqJWOirUElgEqBLaseZNMIvhJna68yhqb3AazwonfO9mvH5M9qrAJzDsvRVwer3WEE_ykwaGCnqxgOn-rDKUVqGpDNGI4H0m_F6zXC8Kn7TG2MPO_y2zSmemAu6BIHrZuq43GReAqbAi3yLv4Ng-EytIblN5uoOAx66n5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxSQhjuVgJEI6hPD88xVs84raVPUzxc-tD8xmpfSIDYqynW6ANQVIrb4uGWllP-f_5gX2t2oKO9jYbBiM5RE78YhIAc-xsryZ--2plT4FTk82BqYyUJxIHEhLYG1d_X5IkEsKSpcgqiVNBMg5QcqfbwXie6ZU69SyHJE7ZBErkM3-9WR2y56Bhd9ajt4Ilhf0XfjfLaZ1oMLF1U-GXK4gyMwJqwGgnt6M4WWKdmU_7IorBS-u7vEwkd6McLTO79jjNbMkZvgRbo73IUofqFuRuTzcSVgorGCTg_RelK8YetxpikK4lJ21vcP9jdWuXXLc3zxt9p-bkJYFXq15tFdMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=h7-oN-_HjCe1ha6feJgDU4GqzqqOWtgLu6KS34iqsM3z-D4wgF3_qWJyBqtHATxh6P7Ysze5WO_JL7L0eoqkXIfTQ3sk-af5-oNvjI3xyiGMOyQFLKapN7G9I9h3burbi671dVYjr5t-dUVMmNwOWINoFbXN3kawefJE6gknDkqwPxcsC6D4lYRFjHqgNVkWBiH9c5rw5U_F-HJ7k9B8hSaypDj0wWlRlNjBhMuKQBp942i79tmDZWB35UGl8Fe5ZzNFKCIE4t7SUQAtEjB0EzP4HxQ0Xq9K0K1iV3kjGLakJw-bUaSJYVhXD6uy-yN1RX1EkS94-xHAfhnHK264qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=h7-oN-_HjCe1ha6feJgDU4GqzqqOWtgLu6KS34iqsM3z-D4wgF3_qWJyBqtHATxh6P7Ysze5WO_JL7L0eoqkXIfTQ3sk-af5-oNvjI3xyiGMOyQFLKapN7G9I9h3burbi671dVYjr5t-dUVMmNwOWINoFbXN3kawefJE6gknDkqwPxcsC6D4lYRFjHqgNVkWBiH9c5rw5U_F-HJ7k9B8hSaypDj0wWlRlNjBhMuKQBp942i79tmDZWB35UGl8Fe5ZzNFKCIE4t7SUQAtEjB0EzP4HxQ0Xq9K0K1iV3kjGLakJw-bUaSJYVhXD6uy-yN1RX1EkS94-xHAfhnHK264qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBhwi26scCi6HiRns-71vnqtkQCLarAxeobC8c_i-X_w2w_ft8aoS19IuHdA593NiJBmQ1v7gEYItJBFbr75jsCz5kTr1069PBkTuQ5KWNUs7clx1gP9RT9G_xA3EMz97HY8aEQuMbeK2J-foH7j05AwaH5cKSIWdmz5PPUGkW1cjk5JHOccwJLQKg2N7jG-GUO1ia1NtKNmzQBhpT6I4qLdcz_KReo3tVDbpfa02nUh80BveSjQ8EN6LF9nzS-ZA37WpAokhyNHPNC0DfEkeGE5vFzCId4QAn9AnGr01wPBAfk6tSiY3AlZzFpFpka55oNwoKb3PzWf7AvdDwyoYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKkZtilrlw0IV8vscplWROgMgWSPklvKdskgJZxufaA_-xhrWSCaqr-MCZdMq2GbrtGufOx28z1dhYxxnk6738cYfq0DK4afMLzC6btSQ4ubRBobwOiTVt3VWD3q4W5zCoeHkxKV9yS0ni1Dg-CWNyZw76-o_KnP6AMrmQ-DOTJ885HBktjlqAx829BYerpBy3fi6o_90LeqoB9S5Nsu86b1mFixdItWD0Ibu3J8b0h4LMdd9zRcxS3GZmzz32f0wawD29zNIIAOgloGWLN4yescKlQSHJXBr6J6GTJAJSPFSnK6MLjz9q2iAvm9oV4s8-MCf1hi8IeUgEEYKe33fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCnVJ1zDYAS8hXzQPC3xREjbBaqEcN7AeirZ4JNFzOqQjltqeG_U_YB0tttqsIuTeKx3Z8a3RNbdrpeED4stuWazy5LMmuAUZaWxAZLQv8bst1MYO83JeIYzO3e4VPokvCbqkdVQBjM3daF0NlmGJlF1CjK6JctwHFrsgEhOFrAgl5VU0QsB_f_TB2l-_wWIiTuzGv8D2NhGhJW3a8pvgZbCT2sapcXnZuY6zb9pH04qoYhwwG_LjUWJX6S_4bN0aMjzewLxPlBS57-3TQr6SwjaTeF0n2Mswcf-cj5QpyU4uPPklaP1HpbB2FY_8X2wsipr_fHvURsk7ed0Nxxw0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYRSlEU1-IUlBx_sbwwdT8h2z8_sl9CMCMVghPX3_sWtS6RQP2Z1JRuEA186XLqIZpczjU107Shqs5MMrvikvZNdzl-N___8KiVBopOEM3TNCBJIRBOV0Wz95F02ApNOOkMZvWvgy1xo5Htdys8kvGdsVpeymlUqf41o_GYR8apINZZZPjThKxc9xJP92496WzH1lSH3JbNoPsdD_UkL0y0_IoP7MkHzXN0HHQmkff70IvIkRr7h-6qmIktLs3oryL_qYsKaOCVyCB_kNitVZIP1BywyKbfTEU-1yfSWHT8ETQ2UMBK2zpGKUTcatjvzZTEpew7so6Zxp4FKDuAZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEBk6cgowjLFO1m2OZbEpwgJKFDoz22TTJG67R9RqJbSi2viMc4wiauzH0M7SixUTqyFENUtJRNN_3Q24yLr8PHIrCHtecK6I6jacWtaHhYyj2dZVgznfnqzuxYLqUD6bWgzqEjc4OmZmORGyMz8tTFBf7eux8MmHSk3hTgimVJ7dLTvv1QiriuBcjDGRYaW6OCbosrGL8S_9aYbWaLNort_JZxUtlPHTy_nLgdMu9XqF773puu5YvmzlJ3xQQfE0u36Enuyas_91816MdPztpjWDWxxTan4FFfCpNdqBzGfRnrWBeaZp8n4SBaSD47NLfqnJX1WwVu6yfORrXQz6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miOcyvL9znPNP-OewoHtCi-Z8SLbOMwCjLFxHbZ4_CRxQRCIYjSRDsBz83Vmyru6a0fSN79x6nf_b_-xQfBGOXH20ksXkquiGh4JrNGO3dD9pjBOTt16mE5CTYLZFB8YKeDFl9FObytJfgGP5FnOSx_lyAuczjYwHypZl5j0SogyZvVapvSzB7VuxoyNpfM4mWXoYu0-ud8zwc8Vs8XCR1KfeMqGjZTIZ5mSn0l4k2cI0HcRnFvDe3oBp3j7lv342ys0LXrfaBNCS2BFI0occewM0cXM6_nRnIuw1-Bbyxt7Nsmpq3U3IAVPznPiJI9O0qev2hUd-kNELdvpBnIZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcKAgYtm7btnJn75LiDRVy-9drANuzYf4jYWTb7-pJfFE94J1UrC-mFA2R4S3BI0dKSAUWFYz7ZlCmrpn-lxHqSmYRjFZTJYzIwm_5SGTc52jAHVU1DdOvCgHc29XDb63ErFbjcuT_xqFznlQtox-bEmdR74iuEpHOWIB3LXcVOZyziyxOi5UGFL-yoVv0Sfu-rVss1rUWNk5sLUCy97Mj31J1SQVJksMgfdEaLDweHLgY9KCX5GuQzfojm1hGhkYmO5GVfbyAefMLT5rocjizORxJM-kKozPT2iHn2qR-HYkXkALmbnM4NJ_BTySsBpZxS9dkfmaMdkSLGg70rCkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmNy9M4hq9KEUt65Uo3lRpze00bueWYExNKmzMY-tcLElsFK3O5RkV05wpPiARVa-zqU0yz5qgYuv_UD16C4FjGQSkgo-iEhbfdSe0VWKxraexa89yehZmxqcHRtgsx_5udCZDA2NxFfm6CF36ZyPaBwFcb94Osq88xmD2PKyFGGGLS0CwpwLeABvIEsmnqGcAURlYXXaYpx_WhzqKalRB_5EzGvE2oCtEgaNfdj4NvSdXTSZFOgVtZikWVu2qUJT3Gtf8ERwhRo5cJsJ865SNVuuSAqS9XxbKNnFghJ8SSCgR32aZlwaAqNZr62e0KAARKNEF1JxCvN9V6wUsufHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6GodASgSMiVBiHpVZPuvY-dm6-L12ki6aiZtPvZlgJOrw2QeBPT78GXiGhrt77Byd1uMzahN1Jy6uLzJvdgJnv5CE8zG_LEAjOmSHKqlD80S9sVJFIzoRaVTMAM6v-CRrIiy-FM8hvlSZR3BV4D3-WZs7ZoZ2C13wql0UaxtaPi5tXggW1wXrj2DdxvW5UKeWYRCEBgi1cvl57iCYeIinizbgRuED7aEIQ3XXYVJd1gjliUvsRwTzDEN-zrHIGn0LYmevZhcgCw7N0ilEej1DMi0Dv5EfEyOCG16lhPKknMGM1NCaLsGMSH_MuT3VZUgMutr79dKFzfcb-ra_a2Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGF-lyDhsnPB3lQ-_s8h_8461tDxwL-Z0RaH7diQsx_hiz2WxnqtP43xZzisdXghPa79JdsE7-yTDqjRDprwkdyVlVYmAdHK8QVtNG4PFw5ksxQjNATzB5pcKYFdvIaDFbucGmPGHgeogMmlUp1Zfv-axuxbucGlFVEBYoZkYBzj8nto73tcQScqryPZub226DQkjIoMgAq2SFg7NQ5fTQ5JGG7m0ddXP4O_7y4lm2n9mMOsxNB_K2Djz2pyX7sc2bHUGCtNdY_xCFVd9YfmhhElFGTMqm25GscInp-Z7LFDHBf2gibTEYL8sBzVQ1Mp-uGGn_a4IgBZ8L316Zin5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKHGYbfZofr2xYnFeocvftu1u1Miema_dqgWv0T5suzGMbzmIK7W7Ws4l96MWP_DGXB0LgOO2P4eZcJsVTVbb4C4cjLYSdwpiIy-vlT12APv4BB9VAJy_BdXkBLucTMYE7MUetwLpmTyypeSBbp_R4AinKbdJzi7lwQi2Ck1azwyjzuaDzEgKUTiWb5jm0ddqikhlbPvxOkqwfPip4ZuMkAjDF4yWYR-sImSRtL7YdZzmMdNbeBTqo5Um4T4iVNy_tV21lQuFbJj6PIn-3Y-SkF9LK2Fq9YY248_GnMs4IduGvzUKe3K0s4ny5bNwzzgTozXz2deEcRHvID7EKPZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihGPNAsoaUSyRgjwfqRot-n-yXUAon0tATtAv1CwVZe19vegOKdPy0yLub18z5u2cKj82YYh2EDhmxFhyYXQ1KCeq911kM-fN4Z9fvQsCWkgkZmGO6TEcS_oLyuNxltw8YqZKurUV-qEwuuaE6A6GhGo89ear88ocDyupbBnhR3syGQ5QkuehEw9aJAlo7IBGR24y06UGDh8Zi_xxvE2s7scugbgYVC0H2iW9bsKmLHf9E1fTAeHtc4aZCa17YRsex5mIdr9pkduOOyLiWmmSlccYP9bV0_hWdsI7MeJOiBOz-Wcjr_jvvcNvol-geTe47RXyY_bdZRH0xczD391wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuJwqpqvOwDly8Uatg3hj7Vg6t-y4_iNifvKOyOTqSl7wOmKOtgkYY8qrqK5h_laOa8CDyr0A-LrFQa0jcc9QxnVGiowRGrhibnAQE6meoZRsiDZgTzToOEypcS72Br5ofrHZ8cMetORj4KSAVMNus-H8UydE3OQMAk368Q4RCDZHuO_PklIsR9wnZNRVu1-mcomkBVhsosXL2OIHEdp4zohaDOfZN2QBgg17r1BeY6olW6W5xr-oBgijyDJ2rxuktaBv0HqA7rcClQYkHJBuoQ8rn-HlcLQmZQd0FpjEDtmL5h1k4SgKxvK7r9uhqKvSMGW-QcaBo7b2uTO9vRM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8czHvcDGqfJBPPiMsmfkpvW_LlVHRmpsIsTb_Mij2jRyix9oN5gpa06Nqgv0lyh51BUK4ScbbL3jPhpKAYzUv3cu5sEJscHcd75XpSxVfmYc9T82eJuCN6jfXwujKZ_0q6YE5MLi1dJEOQS5R3InuEn-qDdpmz092kW9OWmT4MV-Fro82-A0N5EOJNBhvV9d4inFUKkDJJek37LH_EpiPAtFk-60a_ZN7knIBdsthTM06ZDNxthfcWNklqEDh7ofVw6SkqRHTNmihHAS3Dv6q4XClCo_l-OOVC9y5W1QD-lTPa21jx4tw6DDv-zYvE5Oebe9CWzlGsIFCGSXYMRsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=OgRTOj_ErWVomvU_a2MRPRWM5zWOi-fsLTiHLvYHyjOiO73JP0oE31gQsSmu39rCr6Iu_hcbtoXT6IsM-qt-g-3RrcABwk5syue0o5_owperTSheCYCmlDNLu3FQ0XjpkRCGbo6YcchHKVSd4OIPdvwfrMmxquLpjd3Qp9NqhSgzLusKBruMAtp1ngOmCpmsXLB9206GfEkyW-SXzhS6AkVqbfh_JgpIY0USnndjB7uRjH-mWPilvdS2cJhwyN6grnn4vpNtrNJ-kq6n15MDvmIYolofqcKqB4jAUWsQyO6laQJfyAjl3G0O-hfp1bspmj3gH9udkOF3FF6RrTSrwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=OgRTOj_ErWVomvU_a2MRPRWM5zWOi-fsLTiHLvYHyjOiO73JP0oE31gQsSmu39rCr6Iu_hcbtoXT6IsM-qt-g-3RrcABwk5syue0o5_owperTSheCYCmlDNLu3FQ0XjpkRCGbo6YcchHKVSd4OIPdvwfrMmxquLpjd3Qp9NqhSgzLusKBruMAtp1ngOmCpmsXLB9206GfEkyW-SXzhS6AkVqbfh_JgpIY0USnndjB7uRjH-mWPilvdS2cJhwyN6grnn4vpNtrNJ-kq6n15MDvmIYolofqcKqB4jAUWsQyO6laQJfyAjl3G0O-hfp1bspmj3gH9udkOF3FF6RrTSrwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
خواسته‌تموم‌پسرای‌فوتبالی؛ روزی‌بخوان ازدواج کنند و بچه‌داربشن، بچشون‌حتماباید اینجوری باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITaZMEVI6gjGyzK1xOYUELAOKrqR6DPtKZtr0dBBmwcGULIHMNJjYwWGHAIkb3m-eoUHkfVRokxOmtYXBCWUbyWaj-5YHO2ARIvT5H4M8kEcWJRu83pZY4RUO5FozOjk6YW_tVR89v4JmhVTIftHBwOuGpyanzz4YS5F7GV79XUASJ9QMjdVvutC5yEe_IBoS4UZ6h5LD046CeEkfGgpd0ydGjsxCkHAqSMoReITPayukHzshEYk31ggUQhMwdfjdYmlf-GdzRZJD2QJk2NnikUeyN21BlIDdu89SPYldSPnjCYlYOujZXQ9Z8Tjq9cbVgTzmOHhwPt9uB8A_Xfyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOiExtvb_L0edQVS9Lvej9W92cSmDJ2hw6AdNKviRmPwixZlvIk-3qrYU8V7MQfg5MnEHIA__6cAdIlIhpKEQPCLCxteaT9OeDprTrzyPhG1J6mdiTCN-wKuyb8rU68BrlMxLL3yna8rV_LvGOFbpQ3IkkD1xMA7L3gKto_qxUnzK6xGgHvVWAvRhRmn6w11UvP34doddmXG5AYz9f9-HqBY1Psd0qGrVCTHM-BnqQu7GHF_-QVmeziw203oMmCgPBKT4-kk17jXOrszmAoCGm6SrLz0shhXS_ZhPKI19w2Fu9ClbTQAUId_IXj4_bppa1aQ__P6y5IcZm_sDDgwrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtAUa7SuNH-nR2dkQoR6TnGV0TbxB9kh_7otz1NyAhfgSAaGjJXxvKWkoO1I2-gIoAzkNaHogwrBlb4Pj_prYzSdqKultrTmCbOY8znYgI54woLIt_V10JrJGdXIk3ZOQ1BbbedW4o_4LevW6Pa2o556E50LxS_Llk3fm1jIEfwOIlUhZ9BOm-tt-hhDt7Ly9Y3h-leBUUL-jdLzaLCrMptGoJqpj-ddLxEaDpAfoiHjmWAwSRIz-KcaE4TH7eBwrylu4QRC0KICODJnHA9jMDEwQKXYFkftBP7J0zEP7ZXUTyW6N6vA4VR3-E5hpZHDi7wsS-18mHxXJUtAVD_hIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eF-fsWB-t96BHxlfv4U08OzDCM1WVw1FhV60NHRgXIofDXiyv-cTpTCAIelq8ihrkRPxmj829IRqPullXtLRtee_kABDfCL4UITojo3wsFFYXNxX5VOVhtDsag6Hkplo7I6IO0vvP4V3SfJfWedRJY8ue_1Zix2WRbXPMW0-37pbk4-aZxQ8zbUFwr5cuFA4GsFKxnAKaglQ6nHjOtKm3O-8aTqaF4NcHFm9I9xT2hxJCG1FVbp7sNnJXUzYxb1GRTDk2Ft1-MhTORCP6d7J8kw5ouGc4PicD-3-YHbvw7yRjH0lWjgW-5uaRpY9HXpy8F-YOeOqD3KesnqxhOd5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwndKgrQH52FIPogGzUazpFnaBSAOLf2UHhHxLM19pKziFBtnXrcVRk86QKGPOiHX_lENXEpAbxfiFPUYxgM7-I16AgrLMU6TeW3euulbFjnyIc8H2NpXzBUCfam0TN_FjDTOqPNiXs2b5Z29t5y0es0Wk1P8P6Kb-nVgF8qsrjSoJ-8p0gOs_S7WazjzbanWObuyP4vUgc4POWAz3_mKZavlGS9UeCc8q7P-YL1zCnB7WukI_5pyJ7XidcypvJx32y8boL_-A4F-Q9lDobZP3PRsdJxQkLFn6I0003THNvlI0nebOhqfOv_cN-3fo8Ivc5Fg0uc_tZd-mb91_W5GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUc8EmeLk0eLcDTuRw2d2MN8PUl_QFYzHCIYGiHVeH_Q3ztpUZw7BdqouDkdN0tb_mdld-C7-7bF2cBo7Xtmwdbm5gZorY-rZIBCOyp9I48QVqYNuejAfLigZGVOlsCYssKGaXyi-IBluSnKnap3fE1T4G0xXTrP7qrxoeWlPMT_COitjK5HnycO5rPo-WtcrUGLDUWBl5ZlYMO9kC524PQg35qdueTdjMzAcrjIdOhvwTaTGOnrTKKsOEfYyB76X9bgil6x2zWH3zfNYBdiAQtRRjSVeS-udmP6SALwUBtkcJJXiR1ZS4r22EDN_PJQQKDlBLC5Et3p2euxTBSGzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=OZoApwyPUlZZ-GoQR5KC8C9RCgmBX1xlFQaGaD9Jrga-SnaR4LtElTmE5kb3bC8twX0iRcbj_o8VO533MzMz77HsGmRkox5KFLmydnkKGb4ZxOZOFJ9lwZJ8AKbAO8s9-ZBP0bvSv2gAxvg-PMlmB5Z7emgDfwLAqUf1fIe2Zk1y1k7Zg9KhvY0pfGQwTd53btIxEWzFcnwKmDP6LxR9lwamVWRcErEUS7DSLtTInUghvU6AuSc2evCU7hsOZjENUab-osLnqe8-dgKrIOW677AFFgANPrWg58NewsFGVCesrjlzdxni1pb_cyTn9PR9-XoQ9omN175hQwSZVoHFVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=OZoApwyPUlZZ-GoQR5KC8C9RCgmBX1xlFQaGaD9Jrga-SnaR4LtElTmE5kb3bC8twX0iRcbj_o8VO533MzMz77HsGmRkox5KFLmydnkKGb4ZxOZOFJ9lwZJ8AKbAO8s9-ZBP0bvSv2gAxvg-PMlmB5Z7emgDfwLAqUf1fIe2Zk1y1k7Zg9KhvY0pfGQwTd53btIxEWzFcnwKmDP6LxR9lwamVWRcErEUS7DSLtTInUghvU6AuSc2evCU7hsOZjENUab-osLnqe8-dgKrIOW677AFFgANPrWg58NewsFGVCesrjlzdxni1pb_cyTn9PR9-XoQ9omN175hQwSZVoHFVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmeFnb_B3HqDa7AwUFozhQPlFJ-Wfg0o0FBStlqDVLTXlIV9K4rwFclPRDBxO2irB30hMym_RtWMynRDNtciYEPnvaFZqnaii9FpTprqypYPZuSbf-lyL81X0LJfnaE3JSZn1Bwhi6vmzsMZEsoYfy3VmWCxByih80ptPKFFEi3c9_TCWFEEQdCAQXvpoCs7v-_OllogyapKynVLGG5CqXSs5p5goW9hvHqshwUb90iJAumqY-oxo024_YYWxHOxG7aqRgz1esd6E22iy05c1_nSphlvDqdCH3wIqbnHk6zEAEF1xi1nO7gq49V5hey-mVchTexJxSLIID28o57yog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrwjHdzkCo8ZVAEobXDhy5Q5sMe2sQpnbWUSp5wAVym_YU83dlYkaXS8cgW2ne0zEovCqbCpDQ1fY_FOlqahQZqPVF_SSvl2BLyqG3T81dEreLArp-2qpkDMw4_zgd8PZoA-T0eWnt0AVi4JXdJU8Zn4WUhzHSVqpdKnXQksoLvwTQAE6Rr8RZLaM8tNkZvREOTGCWZd4T6Kuk_m34Rt3Y52FC8c9i0drfPyp3WibAnS_iMXKFTd1BnuL21OnA_FJod346y_1o5K-aJC8VjuAplxj76JRa7IjgXOXc2v3nMbHQS2IXHwGCLg95Dii1EH-cZV_DMqOGUpJZeNHdsrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDho4TMPzwcsFelwzySqp-i1ko7RFsmrsYfhiHwI6RYBUliKwPP752qn1mwyoeQ_HqDzr-8fszasegRNs7ZYr_yqVzo5xsoLjYgnem70HoK0vh1xxfA-qji4ppcoFwREPIoiznMl5G2uq0BoBYp_Ds67rN_0axr67xaATdqobt2vLxYxDMXTlCvAIqXlN8b88XRa73F2PD6Hr8x97eNdoG8tvYE0WjecUsNRHQrrZ5kXtVzRIERP0Bo1fTK89u626k8-Ukiqsrv8AdzyNzqHLfWV2Ks26AavNDnCN42AS5_pgFmSu4537UYKN7aMEesW-UfOCxlfPl_RVcXT6vmC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4rlq2eyC0_YsqHPpdXYGSA_RSkkGIJU04cixtm1GvKFnTA0UUyH757V6eK0B2b_YT8n1BG43GaVKBw5duJ8L3uhNJiTdlQo9nSlh3ftU8ORM7dLIZ8c6jHNYycJNbLNRPltBAek5uR4an6vUMSxgzk_Dicf9SURiIdUbSy4cGOtNXIXRLu4B8jNxayvxtfjSQ2IBBFZTAV8QYqEa9arZRaj9zwevHS4GMiEjB8LX8W3cIGGlBhPqILXd0bKLNB0TwHieP6VR_ITL_SIbMCao0zZBF_-k6zqe-QNTxCbFRPn1GJrJNbGVOCs-P17tkDSN2TEjXNfzTKO-8TMAmYWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItGSiBNQleYoCuTrvFT7UA7S6oIJd8e5yjwV2SdR2r8QX7si_EpzVrwwtxEB2UMQudVakSXOVxTO2kWGnJSWK7fqDrP5KuoMraFAOX4rHQw-UTvvzLFkf5xHj4GPW3Fza5Db5je2sjePN12af6-ygyVZ7oO_NJuOT0T5vuuHxIjncIVqN-OYO74BucfysdQNmM3gwKdlah2j0bpNwb0NozasV12-1Rf8Z10wK4jeCV-pGXzVePbQNakDV4gMX1RItNRkyZnzSZVuzm8EJ-DgqL7lzjfCtAX2rXvDuFb7Hj_b2DVWoP2PyZ3jNWPuAFfpmUjaZdNjI0PS84EWh9ZTcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv7BLGN2LB_UQa6XGZ-szP3d8M1Jd-ThMs-Sio4T0ClFgJlmjxgOpmFBwwtAQnCuQ0k_IFo3bYtkKd3ESfdh41mRttdldhBLgioEp5nJxWF8l4bp7xEZHcNtXC0ZEXBhl5Iwwshdc0e5O61VwvXDOEHOGhgDChRF9Bmj40cNJn_pc0_i9AJraoagmMTXuQ6ABKANjeh1bodyrE9rWxLMU-iXymkff5WOSEAuRyycvtMQq_J8R6p2zILB1iPvZW5Hm03Eyv-vf8cVCRrnf4GgDknobOkqzCC6HO5_pI_pY0DrV1lQ8i3hQIPc4ejV6J4A_bqgg8u7sntWzvOiIZGdGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3oZvwxP_g03jAjZ8raAgtE0udYR1681guZFiIGR2qJvkh2BIkUYIAKJAx5gLZ0w5fZ7W-zhLEICiIYe_Lo_iZlUSHsIGtXe0mLBbvITPPdBQX_uesA_tJ15ehcNtyWJZcf8Txw6a7uP_26bnhew8hM4BqzE9rT7hbTK92eQPakaOw6GPdHcCpgQaXPL_CJqEP30qW-eSmr6ylkYNFah4p1RolAjWNjSHGlROZu1sd81DqXrtGF4Ns75HIBF9YPMf9EQy1n3tC3K4aKjeWULg8wRetcXVq-SRdqxbjIQAJVsgwkVxoaPxMjAYWfkcqhKNTDlKX_fTl3ysdP6Ig6_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=I4C4Samh6V5YKwuL37_g5Zor-daXjDI4jUGWxm0hTYEyQy50DTFQ-0BzbUBydPb6hfLmss-Iat1vvLs__aEykJAvghYFtNRFjV70_KZ-tYNamo-TnY4R8GN0fEv1EaUe_ZqBC1jW5s5QBf-HAhjwfww5ew-ZTIj5MYQ4FZHG8G5NyfLXvmpDu1_c4biNXOocYG2W172IbTFFXdOkvsmnsKSlvIOmZgIghh7fKnI30_vNhVTKcxKBvl1zyJZmIXnTSYEkTNToJQjDHMsiyRnw0lm6Kv-MxuRJhgrOcILdz0hRZrSrWr2qFxpyxB5RhpilK_ewpBEMTmWjBs8v8QjwsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=I4C4Samh6V5YKwuL37_g5Zor-daXjDI4jUGWxm0hTYEyQy50DTFQ-0BzbUBydPb6hfLmss-Iat1vvLs__aEykJAvghYFtNRFjV70_KZ-tYNamo-TnY4R8GN0fEv1EaUe_ZqBC1jW5s5QBf-HAhjwfww5ew-ZTIj5MYQ4FZHG8G5NyfLXvmpDu1_c4biNXOocYG2W172IbTFFXdOkvsmnsKSlvIOmZgIghh7fKnI30_vNhVTKcxKBvl1zyJZmIXnTSYEkTNToJQjDHMsiyRnw0lm6Kv-MxuRJhgrOcILdz0hRZrSrWr2qFxpyxB5RhpilK_ewpBEMTmWjBs8v8QjwsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌باشگاه‌رئال‌مادرید به این شکل از کیت اول این تیم در فصل جدید رقابت‌ها رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6kvnoSDxQxfpY5OY9zQesTnalsuJp-Wmc4gucsniY5XK-P8TXhKPCOX39Xu9n9mnwVQ_KOHxv33G-VHof8O9M-9KuOygleLfgMvsghOTfqa191X1oHj4UKYBgdedinRfoe8AIE73113k_DAOT78RA_0dFZBeFgCXZI5nBGo29yjuz9WU96U4Dq8Q_Noiv9LWq5zV2SVc3DWbI0igEftd63Z5GwOPt8SEOTtTa-Jobt-w-Wu9jaqHXUIJIgPYj2RCIKh7cm3pMAKqQNAyeV0ZFMo9hD1HYmw1ZPAMGC6Onk-Z5Kys2Mwz1dHgThcZrq90xeK0qrmtV-qL3xhWa-lpqK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6kvnoSDxQxfpY5OY9zQesTnalsuJp-Wmc4gucsniY5XK-P8TXhKPCOX39Xu9n9mnwVQ_KOHxv33G-VHof8O9M-9KuOygleLfgMvsghOTfqa191X1oHj4UKYBgdedinRfoe8AIE73113k_DAOT78RA_0dFZBeFgCXZI5nBGo29yjuz9WU96U4Dq8Q_Noiv9LWq5zV2SVc3DWbI0igEftd63Z5GwOPt8SEOTtTa-Jobt-w-Wu9jaqHXUIJIgPYj2RCIKh7cm3pMAKqQNAyeV0ZFMo9hD1HYmw1ZPAMGC6Onk-Z5Kys2Mwz1dHgThcZrq90xeK0qrmtV-qL3xhWa-lpqK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XysnaryduAcCgSCTGxesdPlGzRl4C0s3V3EJhhNdYpvn0mGF7oXn2Qf01brxvQPL1nA5NXJPL3yQwjqRInXw2hpWmVNFHkHYGb6sX4CHYeVi12ZV3f6o_EEJiTB9TjfwHmWC3nl75TPM7CScmhsM58PO9FScJJ4tCUL58WmU1O8rTHWLYDKkOnkXrwGMFYp5QOs7HVezLpx82aVlLwm22-huxyytH6x6fhByH0wVO5gU-1rlRAVgnz5QYtiTbGiaZpcVa0QIHRwonb4B_1GbHK8ucAEPrsWJQeY7Ksi_vDXxv0sB2uC7iSTsmce0bUxLizfdSXYZv3u56GAEdh7WkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9sy95xX5otW4-hBaRcSMJY8pmk_Umwe9wNizDKgSaJQkHteWaC-IByqpLTrI15FnduSdamQADz17uXUYqECJ86sAj7sECC34rYtrRuUFs4-s63NQnqg-j_KduN_uVCNp41SAmvwrjVPH0NXucmC-NDyWkc2vkUF5D9NH-o3R2wO5O0WTKCH5zudmePo7dIiNH7UwQ0ooV09UF5BSaJZ0yYPMPbatqwfw0omJt6kf68EeXMBgn5C4dH_ZMdYOgiewAXrCt5IhrGoxPW_gI_yULtifdMiQxK__pKXsR3XhdQybpg-BTVAI3vfDKj-CAZfe_0Bzr9x3Nbsx4gTYv6Kmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=CMTkfSLTlIACcmA9Folx446ouLlK13zHMFFgJBPZn-tN1QrrLvtYhp_WsZCDAiSJXeghWvY4ueDm-TF_UK8APG9yzHsWzfvVj7vrR__AHZU9A6nLuhy1MXmeea50Gj9Qb9Yy0jm9ERKfgl89vBOew-cvjf7bT3kuoACu49NCDFtOMblJ4sE_Ex50At9y1rnqms25QC0sVsc9rxDL25BuGUxXK5K4eW5Rhz3jEqg6_oWlUpQLQmu7Ca2gOMxqsSyCpK7NHxpVwvkIsvXPDZtFtwbdsiTWjCtY_Usz_HrXdL_yC6VPCMGWs2Dyo0z4zM9E8V_yBU0c6E73ttWvYAuFpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=CMTkfSLTlIACcmA9Folx446ouLlK13zHMFFgJBPZn-tN1QrrLvtYhp_WsZCDAiSJXeghWvY4ueDm-TF_UK8APG9yzHsWzfvVj7vrR__AHZU9A6nLuhy1MXmeea50Gj9Qb9Yy0jm9ERKfgl89vBOew-cvjf7bT3kuoACu49NCDFtOMblJ4sE_Ex50At9y1rnqms25QC0sVsc9rxDL25BuGUxXK5K4eW5Rhz3jEqg6_oWlUpQLQmu7Ca2gOMxqsSyCpK7NHxpVwvkIsvXPDZtFtwbdsiTWjCtY_Usz_HrXdL_yC6VPCMGWs2Dyo0z4zM9E8V_yBU0c6E73ttWvYAuFpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBo0vOAqFLSi5YqD2JY46vz6iK1ORx3zIyyGAHxAgjIhlDtjg-BK0I24GShqf8cH1tjFJwzFwfrA62j3xWbuAg6nAF54Gx5NmavX30f_rF3pDAJvLbDDGuT5J3Aj_O_-JEOSbu0Li8Kf9fSnk56BkAWcgLYH9XYHumNGGI76qTHSoWRVJl4xPyoK9mFX3ZAhSruIwCEzd0xd6jhu3RCWIksDSqZ0o57HnP6fdnQCgCUsicNkJFAB48BN3J4bQhshWeWbPyEBGS1rzx474CtYuDVlldUMkrI1aXEvbaXpssoiRoMySjD3lzgG8JWw_sN8auRAHxa4suPkop7RkGbaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr9eIXweOpNv5TfEeIHQQE5jKR4dvH_h4WCqiQEYDXwOtopoBByHoI_3MZaeMEHSqKB4_o1OospXvRFfT41ffoqcqskiZghMSpf5r4DvTHpNs1yoBK8ei3ABh72nf2D0n_zsxRAeczguy2g40y0y1RcrCycLrGo3YfkIJXamvlOsTil4ZWdglvS8JXrgY5-FP7NgQ6niYH_1u7NT9vd_ZXu0nVESQwZTOsQ-6J7LZhoptskx0gn8E57LTI9Qma-AznEyoTHgzmsmMAlTAK5nPbPEcB_bfkfB4zvaNDclCGrHHQvc9va_BTDjeBqSfZpVNf2XBvcTTmHxPcBSo41xIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf4x41AD3d0v3mBp5i_IalJjDhZhwT2djnntdRC37TSmEMKgmjYXNgYL-pgRWALscBWBFygSBb6VDL-UdRVjVhenwKYTWnVog5gk8mAsJJpUZ_R1eMXrWK7xz89wgZnvTgNIlXF9C8AlgjWOpOo1PzPY3NekXHGN-r6cZzXEFhfu831LQEDL6_iH7Qn5cyFMIw-3w7YO4xBroi66o85dRFNdiRaIj2tWevM6DL4xbEVR5546iCI_L1JmlBEy7xz6apYVXK4mchDGHY-j6xqiQGVMRiOa3Dh1W6xNMbq_P6SEXasybYFY99DSJEx9Mjb9IAWOEESA8wmWWWnsDw-6bQZyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf4x41AD3d0v3mBp5i_IalJjDhZhwT2djnntdRC37TSmEMKgmjYXNgYL-pgRWALscBWBFygSBb6VDL-UdRVjVhenwKYTWnVog5gk8mAsJJpUZ_R1eMXrWK7xz89wgZnvTgNIlXF9C8AlgjWOpOo1PzPY3NekXHGN-r6cZzXEFhfu831LQEDL6_iH7Qn5cyFMIw-3w7YO4xBroi66o85dRFNdiRaIj2tWevM6DL4xbEVR5546iCI_L1JmlBEy7xz6apYVXK4mchDGHY-j6xqiQGVMRiOa3Dh1W6xNMbq_P6SEXasybYFY99DSJEx9Mjb9IAWOEESA8wmWWWnsDw-6bQZyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های‌تامل‌برانگیز این داداشمون راجب حذف تیم‌ملی‌پرتغال از جام جهانی؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wud-085YaZgWr8Ju0Sg3-KcSLHvHS85ZdTdOLOCTlm4uxkk6jCT7ljmXzFlgPtKg3kMXJwQTe50FzbS-HMZjY9izy_YcRyrIPeTmEZ5pCpjm_E-Lw48tR54vFOVYZi8GAU2tOkrxRIMT5eMI-MZOwFXXQDdHmoHwuk-tTj7HKyz57GXYKXhQlGL8O2h2Yf8PuQewL0YkNMe46ZbZoNPKwYVT4tqBJsw7PXx2z0WpEkg5EmXd9CFwkyjVb0o1-I8AJBCBhMW7dw2jzHM6w1dS-idg__XCqlw-RHBsfCQZVNQHIa_PrbC6UyjSxWkJEWK8sm2X-unRzCK2l-7KO7BTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
