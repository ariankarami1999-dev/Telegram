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
<img src="https://cdn4.telesco.pe/file/toKjM-XBPhDFdEauepOrDFZtFiRmSSKY1Ia73S-DVUMkT8h6XVwtNbqIREdD9ppRQZ3SPvv30rj0u5TK7xx13gX5Ew3ksiYYYoxUIS8FiPZK56nOLcSzDIxBQq1eYmZYPpGk0PrERePBGh2US24sunf28O4B_QfVoNmDLgEOnjFm9WDCwl8YACgjInKkX3GIOJGBs6vdHzl8gTtgZCjKuS-Y0lKPOrqT2BbGvNbT_0IZbe8fzmOsoSw08enfUGpE6GdNhr6Ju1DJibp286LdYws3igD4LfQq8B1pdm0flYe4C4lkp20SsT3fdRlFZLKFvU7jjUBjCS7NbV1mG37SZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 528K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 01:08:35</div>
<hr>

<div class="tg-post" id="msg-26182">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSH-weX1okAfvwDYUnJNTsTGABon821ptqRPm2fD6fdx1cLLsi_dDZsBU35LV3d9vr3tZZQmtrDHQAgngq6_l4piJEaqxtDUH0p9LoyKZ-_GICuCrAK0nf3tnjQItwxf_rv0q72WD28i5E3bTunXA0IlCAE5Kpg_LCVRCZ5TqMk3uVpsVQ4rSdrXAsS7rkIVK8_kLJH4oHQdE_erxnmPx6uuG3SRvUfJBXkCuBd3JT0uylfRoXq9BNT_cyRVc29-CC0y_uWoa5FT7jdYrUV9eqdLfFeyF5cFMtTdsUtGpll8kN9BuCmhJP3WppZag-EEG5HvT3pKCQnoxbn6BR2-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/26182" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26181">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XihLpvqfgyx6ev2gL9MZQCDKvpxEI2J5u_8yfPZ4COYj5u6s8kKsK5grUnoN-jF4UeUimwKyPnLlgPoWlXGGFAku0w1ZpUamUVRN-DgE61pVOJ2TNeqmT_4_e0nanstsUVfuqpTqOB1-vZvdKJ7VmAuCA2o79Z_pcz66RcH5-j4WQdnBLCWOf8opYfeWVBGJixPVJF6qRiMdvMyxjs6o5jf014PU_KPesCgjvI2FjFTpiSrrjsv3gAsa4bCYtVrph6wCK4uEilJ8eaV-dg73GbiZeqB1vEs9pJHBtE5o-nscpL2qBX7hEno9Jx_SRNv9eVVQwoArcmKwUc7_UDNwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوه اوه اینو داشت یادم میرفتم بگم؛ با پایان جام جهانی 202؛ تنها دوتیم‌دراین تورنمنت شکست نخوردند. یکیش‌اسپانیا بود که قهرمان شد یکی هم تیم امیر قلعه‌نویی که از گروهش بالا نیومده. قراره صداوسیما مخاطباش رو با این افتخار باردار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/26181" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26180">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=PYcHv0ZA8kQkcd2lgO9ifQ0jTzdMoNutbkj6v21N_bj-b1zNrwZK0iMQ1aWfRtdChlPRCvP46Q1XfCmJYC4F0PsZOU-QoP6I16eaEIBbr33vJtwQoMpBZj1b1wnaBMIhpPCoocTLH7Mqxc1TZpH2E9yEa871khm1w1MISXQSEuatg_S8kln06jVR6EyfAo7Pff992j3kLrKH30RineuZ_7Mmhmren9fMdHlHif5c8DXbBQ5itfXtSHcBzevAQajsdQxEjR3v6qMyHlLG22cruJq5nnsO0Ag2NwL0gX1GqcLiNYiYG_ga3omHyzil7nvT3emO2hUGbYll6wm1sheHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=PYcHv0ZA8kQkcd2lgO9ifQ0jTzdMoNutbkj6v21N_bj-b1zNrwZK0iMQ1aWfRtdChlPRCvP46Q1XfCmJYC4F0PsZOU-QoP6I16eaEIBbr33vJtwQoMpBZj1b1wnaBMIhpPCoocTLH7Mqxc1TZpH2E9yEa871khm1w1MISXQSEuatg_S8kln06jVR6EyfAo7Pff992j3kLrKH30RineuZ_7Mmhmren9fMdHlHif5c8DXbBQ5itfXtSHcBzevAQajsdQxEjR3v6qMyHlLG22cruJq5nnsO0Ag2NwL0gX1GqcLiNYiYG_ga3omHyzil7nvT3emO2hUGbYll6wm1sheHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگام‌داره واقعی میشه که؛ رسانه‌های نزدیک به امیرقلعه‌نویی میگن سرمربی تیم ملی ایران میخواد بابت صحبت های شب گذشته از عادل شکایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/26180" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26179">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=mxFNvYPYn8YEVx7WgDZGHOWnOmvmEBMmrJ9I-ka_AluM8jrW0DIoPT56Qe28kkpfJ45OsGkJhd97D5TfDmFmp06o-F8JJYEOhv8tStMIWkQDrvMdc3SD1pn75UmEZ82z6KiRfL0hqcybKNcusFzUM5cNmvMEBW_AXFUlijOfhyTD19s5_dgFlDxHZK1ZpF6bYg9qaNmP2dXS-kuQNe2jWnR0oOErnSXSDSl7szqmby_mHUabcrj02MGWFiCbPqI6j4sqvAt2kgcwt_42DVr70if2f5Dpm9GyP0a04pSOJddCvWb1-J2VWg8XYRMANpt6VPWAiK81dUYJIPaHpx2sDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=mxFNvYPYn8YEVx7WgDZGHOWnOmvmEBMmrJ9I-ka_AluM8jrW0DIoPT56Qe28kkpfJ45OsGkJhd97D5TfDmFmp06o-F8JJYEOhv8tStMIWkQDrvMdc3SD1pn75UmEZ82z6KiRfL0hqcybKNcusFzUM5cNmvMEBW_AXFUlijOfhyTD19s5_dgFlDxHZK1ZpF6bYg9qaNmP2dXS-kuQNe2jWnR0oOErnSXSDSl7szqmby_mHUabcrj02MGWFiCbPqI6j4sqvAt2kgcwt_42DVr70if2f5Dpm9GyP0a04pSOJddCvWb1-J2VWg8XYRMANpt6VPWAiK81dUYJIPaHpx2sDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/26179" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26178">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc3fTur2v9XL1cNaHTZYx9NsMA0RzXlFYdJaP91RuAqL43Q2cMCfKmfMHSlvmcnUTZscTmYUXYdnIEGL7RoBfmhATT8roTmZm7vGirjatCD16hddRYBllaIpRz0pYMZMpMfSfuciTYx9Na66xOq9us84ncm7rEa6Us4tGJgMxzoz6ejgZrXicbz2GbwFaQs7uBUWKkJlCCAUORF3cRnCncujVpj7apdeCa_gXwrin7i4wYsmzKr-jEZkRaYo-e6JcW4ox1CeHkoiMivY724LVGyBRd0Vj2qY1zeNEBuEeW-DTBpYLYR3yHHoh2qrNQFH1AUrP8JNFPuA4SWK5zxyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/26178" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26177">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlrglLG8qoyOSLXvunmfm8KG2ADR3IJVfZMyLHA46Biw3xcXtqIekwTVuCiW5fEfeg05bWVLkhjRE8QLOtJgaBqOikZpp-eKyEPppjzAy91qUNGknjLiUpgdrL8R3EN0zBrNbHOvC2fqC9eNvG90tFMycZ-rYwSJXrs9kEFdgMM72wDpn0M8drq2g8ZZEEdGUeJlrU47dJwZ4iBGC0JWYeuIN0L0NkfGztW_x5r5CZ_HOD_AVUU6NU2wsknG7_gNwYQrQq5pabqK_l9AEbBwH_TKkLLuJZaOK7HrZPNlewdQtPssE2gHF_govjgV75W2qb0qBawNeliyIdVEbVpDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/26177" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26176">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nij57szZSS_wfrN3GmkLbdDEdcCxJNtBN3Qsa0Dis5mAufuaNk0btVC0zvc51JlW84r1XHvgg46iAJhsVVaao46jPXGWQf0RU81buuxbf7KYX4U2ULM29VbIPZoBNldBInBaq3VebPOalPqkihxI_G_pXNdd9IhHiaC-mAasIDrMdYpVoR2DIg9kijLdmavWLA_b595P6IROkLapmJ4C5OiNzBLOsimvSfNbpBQcsxSAE5JJK429rNFFnvkf01pAPPXBS2nfYG-EkuVcAd4EwRh9eJsHlGF6rBuhMGLOWfHkDMXGfzWJNUXUEZroN5bBVfJNXPhidxx5wO6tW_-2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ راجب دانیال ایری به اندازه کافی تموم اخبارش رو ازروزهای‌گذشته تاظهرهمین امروز به‌عنوان اولین رسانه پوشش دادیم؛ حتی خبرگزاری آنا خبراز متتفی‌‌شدن این انتقال داد اما گفتیم منتفی‌ نشده و باشگاه نساجی72ساعت وقت داه. حالا طبق اخباریکه گرفتیم فرداصبح…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/26176" target="_blank">📅 23:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26175">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1L9CQqfd4KKVxWto8gwiunoFcCfoVIHwwor-_7Iw_yQNN4ogCuRyUOTM3dgY6YdYW0BlJGT4cDXNAxNgPceCAjkZuxAaFbb8cyCD0gnWVvPeoVxYNC-jA0N67n9VA9HbaiKES2o6h0_yblnL5QglRNKld7YPSwaVfwP0o5kzl9G36ClslXvAFAq3j6Uo9f32RMBjQVPlrCO5sOnljG5eX2O2EO6iXVV0MCQqAb9NCYTBx4jlZyj9sgMLq5ja3eEqLQatw2HlcrVr7QUc6iAExP0nImGnNLQvFgpMDxG0o3PsGuvCxTpby6CGacVKih7j9Rruo-PN3xY-vktLaugpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه فجر سپاسی با مجتبی حسینی سرمربی سابق آلومینیوم مذاکرات مثبتی داشته و اگه اتفاق خاصی رخ ندهد بعنوان سرمربی جدید این تیم انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/26175" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26173">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=JfFO2IDj6yTXoTKrBDBfXeQxRDMaJfMCW76xdg3rgJj5WOrZ4wakLNFR2UDoxdOl8RwHb2IOutFabP-7fEBbMjzqwTR9m01h70V3ZVVuL5oOBwGql8wudohNiIDR1oUEDmTnZccj0tWbx50hNbg8o02T9Pi-u3mLgwut4GAiA7kKEsapEJbjH0tb118IRN_MmzIJYndCa6UXzfG2EJ_cu1_kg9bC03Q5DMfR8-QVKfLddC8fuPtSFII-2z03BTUK5G0cXZfA3r6mm29DE90mAvklmYV4gdzgBb0B1oW4iqX_VnnHLb3KXqPmlEYJ7bBRPMOFcJNdURHMgkRJWfdTew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=JfFO2IDj6yTXoTKrBDBfXeQxRDMaJfMCW76xdg3rgJj5WOrZ4wakLNFR2UDoxdOl8RwHb2IOutFabP-7fEBbMjzqwTR9m01h70V3ZVVuL5oOBwGql8wudohNiIDR1oUEDmTnZccj0tWbx50hNbg8o02T9Pi-u3mLgwut4GAiA7kKEsapEJbjH0tb118IRN_MmzIJYndCa6UXzfG2EJ_cu1_kg9bC03Q5DMfR8-QVKfLddC8fuPtSFII-2z03BTUK5G0cXZfA3r6mm29DE90mAvklmYV4gdzgBb0B1oW4iqX_VnnHLb3KXqPmlEYJ7bBRPMOFcJNdURHMgkRJWfdTew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
دیشب‌بعدبازی فینال؛
یه خلبان در حالی که کلی مسافر آرژانتینی داشته روآسمون گفته آرژانتین قهرمان شده درحالی که فینالو به اسپانیا باخته بودن و اینا از خدا بی خبر اینطوری خوشحالی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/26173" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26172">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=tklvLyvlJy2F7CjrnyscXI4XnugHIQCDastqQ-etBGBHswr2Phm4fndiycwBBj_1639MaVJq7cP3HzzUMXolIffi1e6RGZML5Zk0oNOWi2QnWCz7et5s9bCp3eUcCk-aNL5vVE3pFW6NJdBEpCe-IUHo_zqxMmpyvaix2UC__eVdloyg5kDaZKDOr_5DYdwSXAkU1lnPaloDvwqIkcYKOKDr0oINR5r8hMzCWOQ24r3OwB0NrugHgnBR6qsZrRJEQcFIHqKldNmT9V6IyfAczkjvC4PExuk4NuGOJiWLVwWKrSOurHepeL5ctm82QPNBrUrWN6VYyN5DgxDCpYnzWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=tklvLyvlJy2F7CjrnyscXI4XnugHIQCDastqQ-etBGBHswr2Phm4fndiycwBBj_1639MaVJq7cP3HzzUMXolIffi1e6RGZML5Zk0oNOWi2QnWCz7et5s9bCp3eUcCk-aNL5vVE3pFW6NJdBEpCe-IUHo_zqxMmpyvaix2UC__eVdloyg5kDaZKDOr_5DYdwSXAkU1lnPaloDvwqIkcYKOKDr0oINR5r8hMzCWOQ24r3OwB0NrugHgnBR6qsZrRJEQcFIHqKldNmT9V6IyfAczkjvC4PExuk4NuGOJiWLVwWKrSOurHepeL5ctm82QPNBrUrWN6VYyN5DgxDCpYnzWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیس‌فوق‌سنگین ابوطالب در برنامه ویژه امشب جام‌جهانی به‌قلعه‌نویی: ما تو غار کنار عادل هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/26172" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26171">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=bmws2XDO-X3KebalC0dE4CGaUTV4qXv7RANo3TK-mOV4GQgr7b-LR4HNqtzefVdKl6Xpmwf0C5kusUINAr2aX881oVd2sJzKJAxsnFi9ywLaA6uIE4c-pGjfNVEIcvEO1DiKDDspG1d4cqL7LmKPBMX0QuK3E0IEhgr3NsxBDPx6B_E0DNTYTmP5UUeg9F_G0CwQ9HXFwI7qZuCNsbdIJp-A2T4UpFEWn-TYDHHbIlb4zxXmj77V1FAkeMKnpjJgHwMoNoskelqWU-Rf5vu3brz-hc2vwmS0miVbO5mBIstr_1IlKW1QLIrnDQZei6Xh2is7GAxTq2CgE4PE7wC0fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=bmws2XDO-X3KebalC0dE4CGaUTV4qXv7RANo3TK-mOV4GQgr7b-LR4HNqtzefVdKl6Xpmwf0C5kusUINAr2aX881oVd2sJzKJAxsnFi9ywLaA6uIE4c-pGjfNVEIcvEO1DiKDDspG1d4cqL7LmKPBMX0QuK3E0IEhgr3NsxBDPx6B_E0DNTYTmP5UUeg9F_G0CwQ9HXFwI7qZuCNsbdIJp-A2T4UpFEWn-TYDHHbIlb4zxXmj77V1FAkeMKnpjJgHwMoNoskelqWU-Rf5vu3brz-hc2vwmS0miVbO5mBIstr_1IlKW1QLIrnDQZei6Xh2is7GAxTq2CgE4PE7wC0fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اینوقلعه‌نویی‌بشنوه‌دیگه فکر کنم شکایت کنه؛ تیکه فوق سنگین عادل فردوسی پور به قلعه نویی در بازی امشب: آرژانتین بارها تا آستانه حذف رفت. فاصله‌اش با حذف5سانت و 10سانت و 30 سانت بود اما خدا کمکش کرد و موند در این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/26171" target="_blank">📅 22:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26170">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=FDNdKfkdze7_1u7bWrG958_huSmR8S5whHuF7TreFK8ELyvX1SytRKesDGSg7fzSd97Fds1v6EKgZXi9jDRK0oVyOkxi7c0qmRdISndeNfYUzrAOm4eOcg3VJ0oGn8F_xrGlM6ZinfI487AmotjM7st5Eqe3EZCkymwBaxcx0u2ZuWpGRS7UlHUL3ilnv_1Lxd4KxCmZUECWuaKBqyVUvOGeNCmshmBTnXzfzFBNtszLYesMNIJnv80jRx4ekBFiQ727D0uH3xfXPGYWh9ncPNz26OcP3-NvH5NAqh8Io6AzOFjhszSum4YccbEzR0605fWSuoM2xz14ZSZnrb1YhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=FDNdKfkdze7_1u7bWrG958_huSmR8S5whHuF7TreFK8ELyvX1SytRKesDGSg7fzSd97Fds1v6EKgZXi9jDRK0oVyOkxi7c0qmRdISndeNfYUzrAOm4eOcg3VJ0oGn8F_xrGlM6ZinfI487AmotjM7st5Eqe3EZCkymwBaxcx0u2ZuWpGRS7UlHUL3ilnv_1Lxd4KxCmZUECWuaKBqyVUvOGeNCmshmBTnXzfzFBNtszLYesMNIJnv80jRx4ekBFiQ727D0uH3xfXPGYWh9ncPNz26OcP3-NvH5NAqh8Io6AzOFjhszSum4YccbEzR0605fWSuoM2xz14ZSZnrb1YhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه سنگین و کاملا مستقیم علیرضا نیکبخت واحدی به میثاقی درگفتگوامشب خود با ابوطالب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/26170" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26169">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT5wport7fUSbDG9z7r2y8C4IJ50wYHv9zgcFj4ty2cgHjpPIdzi0ggNtxW8IMFXEqGz8oZ83IdVAYLR439dV4-lVpDzqholPZN-wQV0svh3bNhOgI_kDuCyWrL20BW8IWQ1u27GbJa9ymW7us_X_R9vJ0F9nU11eMSdrPBGeXDfeliVpbnTbGaj6uni70SGc9OPdazAAhr2S7mDKk4Hz1E2wfFUaDIQUwlgeg4zoJhidqF2NNkS8-olefTpJizkk6x8KKQ-_WjI49SU555kPwGYguG74EPdBPK_Bf0QhkDGSgIRq2v1EWqy4_SqQXPMrbcbYtfGJ_aLfyrFpMETHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
20 ابزارهوش‌مصنوعی درسال 2026؛
بهترین ابزار های هوش مصنوعی در دسته های مختلف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/26169" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26168">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=WNYvxzFgTVEOA_VpMe8kX8k23vaixagMTafsAy8sGEE8_0Hzlrsdj_lGgL-pSYPmh7eK4wF5ewbaUwrJIhyWQPy1EDotjriEPuHH9hgmbikU2cwHY10qqDZax0rqv8t0kKxDTZ8Mdpm73hb-LrsAhHea6CFUE-McMLS_wpQFCJGAnHHE_4PyR6gum8d-NmwzezE0_BnHfYGHT4RwoWFH64oWFVCwTfOzAM0wpaxjOnKbFT1HEADVOXjnq_KPhkWaBKwpxPScqTQWq6bXAFHZLrmcKpMEb_mOgGdGcMP47FvY_SFOrlA9_SFwBi-tsCjS8yiUH5seDV629rP-nNPdI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=WNYvxzFgTVEOA_VpMe8kX8k23vaixagMTafsAy8sGEE8_0Hzlrsdj_lGgL-pSYPmh7eK4wF5ewbaUwrJIhyWQPy1EDotjriEPuHH9hgmbikU2cwHY10qqDZax0rqv8t0kKxDTZ8Mdpm73hb-LrsAhHea6CFUE-McMLS_wpQFCJGAnHHE_4PyR6gum8d-NmwzezE0_BnHfYGHT4RwoWFH64oWFVCwTfOzAM0wpaxjOnKbFT1HEADVOXjnq_KPhkWaBKwpxPScqTQWq6bXAFHZLrmcKpMEb_mOgGdGcMP47FvY_SFOrlA9_SFwBi-tsCjS8yiUH5seDV629rP-nNPdI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26168" target="_blank">📅 21:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26167">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4HeFeBtzhQBAWW2mfKv5TM3hhhN_keeUPeN-z_8DBci-6O8CuVBK6CZnEJ0WUt6QBatQFVUP2Lrby7QBAG7kgxXbNXU3WClEzpL1InDb_xvXTmHZ3hiFEGtU-V91w6VrerA_DbWnSK1s3nPsV_DZ8P3DoEHSBISw5-wvAwxPqhjIDke-NAN3pGYWa18syEPBAIUezn2FoSZMMbhm-z6rMscIxBwPq6l1iXpKAraaKk4vd_SyraJyx77aUNGTrvsaGmj1WqHUrroM1PA0abvrD1K7RGphdcUYlhYU3CC--6CY2z2F79bYMmqb_yG4GVtuaf7pOy1_l00WZt67Td2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26167" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26166">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTDEG-_-1ckq3-P6urZ2KnwbYNW6gN4isMWa_QGBM9-GXX8Cq5sf2VKkoe6rpJta-S7L7mGVqKJ90hjJOzSIXRkdr7pq5V6Y3DzyH5bVAFoAr8oyl-kbSdHwHiaHG44MU8Wwi21_Jbd26vQFjwh5KL1ZIMxcz6FRyjG6YQze0CdsouAr2N37wMLHlxqjcfUEwgR_q1bTJf86JbrTr6pjTAIMQcqYif5IxjKLLHeN21-4z1c1GYy_PIkhcnn5HA8bzpZrTwoUjhv-Ka0KQSccmswAJeq9JsEVsn7niLuHx51_QnvSoNB__aI1glgtXbq42OL9pS46ZZwvLKFcQHrN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ جدایی داکنز نازون مهاجم خارجی استقلال از جمع آبی‌ها قطعی شد. نازون به مدیریت آبی‌ها اعلام کرده دیگر به ایران باز نخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26166" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26165">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLBQwS9JAplo0wbukOKW0DqSG2TNrn9ijOkl5KoGNMwAbUOLNSI5Yh7tvjawUH-nHDW-UnbI_8D_82oUjydbVmSOGa0gOfkXdPwsFPaNbUo8rMI7nmjk9VgvIC2BMRKPIyLJZclO7ELbM5WGNQJFocZVq_HZlUaLvzM2pmC7dp1_TeUgtfpOanVvNieWuZkfyMRT-PNb3CjGikY6JaFrg24vgvZiiOgL9Bs3TpDoBGv9vSvzYKo1mEtwnUZCp9MAVNWr07-stf_X5sc5jxbh20qJr-cF2LT4cBaGGIikYXKSpQhXD-IW7p32jAy-UY_q_C2CuLeVvr_r8rMqqeG2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخبار دریافتی رسانه پرشیانا؛ حسین ابرقویی دیگر بازیکنی‌ست‌که به احتمال خیلی زیاد از جمع سرخپوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26165" target="_blank">📅 19:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26164">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebqqgFHZl14cDl_aQYn8j2DV3w9qpJP1Oh2r6maDOzMM6G__zwfFrkJR6fjVPOck3RKYRfsAtg-24kZ4Q6ye_ItpeNGSkocq53b2RDivaBdc1chYnpaFaEPGLMtMiaqemlzK4ANsywnENMSnemPO8-3eAIfkybUTOaA1-JM91qGVmChBva5B-LnvfHkV9UNgzSgLzRypEq6vx8j7HNgXqnQNsp7Rc2hyPrPUTxrqc1aYppPOQktiI8Aaq1-KzrnUCQDFakbKSo3hfvuNAGwCvp9AeZ7QEYmBUL5T-IuMEbCr5WloFs53ZIwo2CWegZdNPunxlS1z2ERzkXZiOwVtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیرعامل‌ تیم نساجی امروز صبح به مدیریت پرسپولیس اعلام کرده تا فردا فرصت دارند که 150 میلیاردتومان بابت رضایت نامه دانیال ایری پرداخت کنند تا بندفسخ‌او رو فعال کنند. در غیر این صورت اجازه جدایی به ایری رو نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26164" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26163">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424844d43d.mp4?token=vsUP54t3ThAhfgkFhIfyOKS67WZjKdY4dfNKWd6JVSCAo8RO_3rUd1yf503XgPdi2zKxWGRxydzJwckxFyHw6aXu_7Kh6fSza0dKCuyfNaBbuVa0TQwUbtuMh60-KW5kC5ISH_WDeK6v4CF-oWcvnfTc4EgX2iiuJn7xd4MIA815DdffE6mWK1PWiIcT9iz3p8_-QUu725621ekLYyVkBFTxBKGtD5FYIpsNADXKpNiRsqtHdazitzR2FKeRQ4xsDx2NcvDVW6XsCoUIDxbft1R7h-J83RXm2maGeZdnJDno-XuHxy5LFB7ohDyAaAzgdWDhFHDTZufJ5Nrh9_yLaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424844d43d.mp4?token=vsUP54t3ThAhfgkFhIfyOKS67WZjKdY4dfNKWd6JVSCAo8RO_3rUd1yf503XgPdi2zKxWGRxydzJwckxFyHw6aXu_7Kh6fSza0dKCuyfNaBbuVa0TQwUbtuMh60-KW5kC5ISH_WDeK6v4CF-oWcvnfTc4EgX2iiuJn7xd4MIA815DdffE6mWK1PWiIcT9iz3p8_-QUu725621ekLYyVkBFTxBKGtD5FYIpsNADXKpNiRsqtHdazitzR2FKeRQ4xsDx2NcvDVW6XsCoUIDxbft1R7h-J83RXm2maGeZdnJDno-XuHxy5LFB7ohDyAaAzgdWDhFHDTZufJ5Nrh9_yLaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خوان کاپدویا فولبک اسپانیا در تیم قهرمان ۲۰۱۰ توییت‌کرده‌که‌توفینال ۲۰۱۰ جلو هلند من یه سکه با خودم بردم گذاشتم یه جایی زیر چمنا برای خوش‌ شانسی و به کوکوریا هم‌گفتم‌همین کاروبکنه امسال.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26163" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26162">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM0MSqsHGFLHU3HWnJxrlC8LzXq22zgqVqZ_mNLGIWwSg3fYVo6gPC8fLyIIbc1qXzSsOinwPTMM8eYlWsuR46OL9cFyYXxLWzccUoP2rRm4XVKExUSahWNSY3NDq5SjnT-uG2PwoZ5QGKZK58ApH4oRRlEPTBzQ0vhj4xOq1UxneVaWcodZzdbOm4Pgh0L95DGyChGM8-dVoxtwtmkHNuqpbRLnKjamUIyW8DBQQfSnD45ui-7FDGq01_NJKTY-IDQYJvig5_JHLHoRnO5EsHLiShqZBnx22sKAq462woeysKArNAabl6Pbz-fQrreEfWo45d0TZ5ODhEKjBz62Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
معنای جامع و کامل کلمه آندرریتد؛ فابیان روییز ستاره‌پاریسن‌ژرمن50 بازی ملی داره و تا حالا شکست‌نخورده توبازیایی‌که‌برای اسپانیا انجام داده.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26162" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26161">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b11787b.mp4?token=azidKWydorsHFhKU-ahwZPmX8JVgF-APB173unGRUpnTJJ65fXxW8mvvi-9W2WQuGG2tsuH4x4HDb2HwachyM_Q0FRX8NvPUzVnBnln_ZdoDjB0SNtXfo5Wg-7jD4YF4lWfrm27nUoz3IM7DKtHU-M30NEaoPQvKY9FqCOSpuRdMo8y98HKnR03J4ppq1oB76K_nWxqSYhOZcNDyLZca8fE-KljasbzXB4CCwoWZ-ZbuQ9L3OFOpqsLo43nb0KSwHrp77MubMwEgxfFb80cCLC7znDLQVnWh8TgLJ2s0N1HcLtXsxEW_BHRXuR9yZQmAsjpCZ0L7dYdn0o2jyIaMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26161" target="_blank">📅 18:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26159">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=iGsSYYrUH_Vi32QE6b8ZzvfJaTkI1NCjdlSC9bP-WWM9yuWBmiMCC1RMX0DLOpNFCBGq2tGestYSZDdia1I0TtcOH14Na04MiFhHPZPCAsrznDFNiaVZHkLHdxftHXYE5qi8qSPJrE09AYkWMnKwnmOXznvuApDpHIf1ZvxEi58yn_IGjddadjaODLoB3-A9zMpwR3IvhINp6J1uAdiStRM5ILjV7Y3ckdvtXaeVDIHURHi_ZOU4QtIdxUBq5MUFFo-ntKHQ3e1fhzUsqi5qTEyx4l78btfyRiM5V76BRtgIUnn2EVTAt6yCRt9yRi5AwPi59uDu3PFT1dBed9ygtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی خفن سوسن پرور دربرنامه اخیر قیاسی؛
قیاسی از سوسن خانم پرور میپرسه که کدوم ورزش رو دوست داری؟ میگه ژیمناستیک قیاسی میگه خب چرا؟ سوسن میگه: چون میخوابی پاتو میدی بالا!!!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26159" target="_blank">📅 18:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26157">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=otSDe0w-AcpX9Ep5irZsqnRcoz8h7nafh8_70Kx2RUlM4ozKTamfLbhDAxvfm1UysXICk8s68fs6djxdimRR6IiP4mbqbhylt_COsrdtBWJHlGQoLbc46oL9mO-xYNYaoa5hiMdDlxzQaMD0gWSh5_X90uefdeBbbP-APNPxlinPRi3rmSgGZuzTWNBxd0IkqC5bcwH51L38lvxKWbKln6rvhbEBIn22gVyubWKJHtvC4WXq_12ZtEUVD8rxdmHcUOoR6epcpJOhqpLrqNGq48Xtq9U5zBV-S4eqcvVN4EMGlsKQ9QtgXtKr_IedOHr1hDLBjsnMsuksUDnesrOrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترهاوقتی‌امتحان 19.75 میگیرند
🆚
پسرایی که امتحان 0.75 میگیرند و درباره‌اش حرف میزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26157" target="_blank">📅 18:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26156">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmfRnNJlIPjIdV5eNBGgB-XzM9NnRfUQHKxDP1r2-jUszIumufn6tS7ADKEF5J-dfcPmQpWQrdpPemOMzw_mUs2Y--K2DhtHJ4meZKSDxCXN9FAHKdxgMXrLFwHVcXUC4FhBU2mtYlDQ0u1NcM2GjhohWzn2hdec-W4cLT2fT8K2zqBwrJUltkOuNnc1vqy-oLzDdL6PqeHXLgKLpkgDN_t-J7M75iVRZnDlaC0_xBNxD_Yjy3qsEHS56kpLGR9TrdbEIHMivsBehX3MuHMHstD42uQGZskjZ8UP74Pv3zLwmsnYcFjLFyyXgZoG0DTGb8CgiPrGxJBmKtUtEafSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26156" target="_blank">📅 18:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26155">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL42G3bSjK_fsHQspJafKyh5mHUb5ht0UJB0Fn7Ukwz6NIIAnFPFXcaFaMHsW59IQCGCPKNKhBJupticnakp9H8FZ0XcLKazL5xhXDEV4KtmV5oFeduwXP6upLYYKfVhUTdUh-gEPzG8wxZU2S0BVCFslkMJBtvYIb8AZoTi4yi8JSaq6DGKltXH1niv8gwW3J-QNiL8NvvPys_QRzq2ukEfx1fkmpxxTAZKiy2yhat99RDVdaCYDcK1iEwjcVgb2cICWv22O4nSjURyOvXYriYibxmOiU8NvqsTvEtnU43vMHIS7P5ew5DEyhEvILqcOwaDwN71guBzMviHgJEwhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پنج روز پیش پرشیانا
🔴
محمد عمری26ساله باحضور درساختمان باشگاه پرسپولیس قراردادش روبه‌مدت‌سه فصل تمدید کرد. حتی مدت‌دقیق‌قراردادش هم گفته بودیم. عمری آفر خوبی داشت ولی تارتار مخالفت کرد اینم موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26155" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26154">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b054f61942.mp4?token=TJNSZ-HJV__vYKDv9jUgD6Vld3VUC33oDD68OoWTeLTtYnq_zgcS2VGoOjiP9YmWO9i3v1mtAoEKVfIGGzo6VLsDLy-uBU7TUpQsmVej8_nGsAR39Op0sPlEB-N4Ia3Hv4GtwD3VnQtNKJdtZYw4toZ39-EFvI4togQ_oRahTK8ijX3V1EYJtnZhg6Q18jZN3AWc_GVmt-mI9uyBYb-IAUm71HYYUDDPBu2meelI8J6oEzpHAM95_kZWmDyDYp4xUFfzi_GVjMGhCCUhwRf6yrxQ_a3waoq1ehgyaUd9OoOKjqk96_9QqtN3Y_knR6j5auePW7hayyHvvTdkofR4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b054f61942.mp4?token=TJNSZ-HJV__vYKDv9jUgD6Vld3VUC33oDD68OoWTeLTtYnq_zgcS2VGoOjiP9YmWO9i3v1mtAoEKVfIGGzo6VLsDLy-uBU7TUpQsmVej8_nGsAR39Op0sPlEB-N4Ia3Hv4GtwD3VnQtNKJdtZYw4toZ39-EFvI4togQ_oRahTK8ijX3V1EYJtnZhg6Q18jZN3AWc_GVmt-mI9uyBYb-IAUm71HYYUDDPBu2meelI8J6oEzpHAM95_kZWmDyDYp4xUFfzi_GVjMGhCCUhwRf6yrxQ_a3waoq1ehgyaUd9OoOKjqk96_9QqtN3Y_knR6j5auePW7hayyHvvTdkofR4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قالبی بسیار زیباوسنگین از فوق ستاره هایی که باعث‌شدند ماهاعاشق‌فوتبال بشیم. چه زود گذشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26154" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26153">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZZUK0w2J_k3bNS9lNdec3c-24_lDRicj-zI-fTD-exN2KgS8HGhYcMqakxrJAjIN-yRkJpBOGOWkTGhkUPg2-OzMNL13gfk6uw2lNLyKhEiryIw_Z2g-BN9DUCHn42wUNxB3r6L0yroipQUYyduMdVIB8j5lMYIW8ty1-g6FjjoiS49gST4eFedJrLNSTsRQcCGIJEhUO9uNUkiizdMZ0jA3IWhhz_zw3KhU2TIjEHNDqCfFcnrfzRouby5iGwIrvegrVMA0WcPB1kCIg_Z8Y2h72rnNKzSgkM2hGpuI_gNsD7kxSx0XGfCYRgOIqrd3ko3FrJJtF4oFswO8pgjemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=ZZUK0w2J_k3bNS9lNdec3c-24_lDRicj-zI-fTD-exN2KgS8HGhYcMqakxrJAjIN-yRkJpBOGOWkTGhkUPg2-OzMNL13gfk6uw2lNLyKhEiryIw_Z2g-BN9DUCHn42wUNxB3r6L0yroipQUYyduMdVIB8j5lMYIW8ty1-g6FjjoiS49gST4eFedJrLNSTsRQcCGIJEhUO9uNUkiizdMZ0jA3IWhhz_zw3KhU2TIjEHNDqCfFcnrfzRouby5iGwIrvegrVMA0WcPB1kCIg_Z8Y2h72rnNKzSgkM2hGpuI_gNsD7kxSx0XGfCYRgOIqrd3ko3FrJJtF4oFswO8pgjemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نیکو ویلیامز ستاره‌تیم‌اسپانیابلافاصله بعد از اینکه مدل‌روگرفت به این‌شکل به مادرش تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26153" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26152">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh8D0RhyM7T1cVHNzHw0RKkbI6GnNhSA3_MbqQtpkeop2w02JrWoj8XBp5MA-oNLD7T93Mea3mroHvQlKNaU3AXpDceYIQodg7lPSZYynR-WTY3NrQN-zQKerBeKgEVAHI4azHqNINO4SnzWr7v0w3nLAuVX0NRrVXsj3wz_cecIhy8tAiKWdbpSSdLMs9-BpPd2dUgcUbsJ49TVZofkLd758JODhagAmzs9yssWcPTW4kNxPqrsb0SvIq753wjKEjJ_Pm18UbxX2a47rMi1p6ZNxAaWbcDOlUPsVETtNe4ctx9qKuCvfgCHGUNkz_HkqMk_fQjI_Ioh5ZrEY8btyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26152" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26151">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdoGvj5IrWT1KXq2ofkh5j5dpmLCVh49R5RvCosjLtqCN2dJfbeOWxksQOLHk5AqTvWEcIYPPVr6XP58b_li5SjcXnzK7zEueTrW7XvVEaf8BadVPBy3TUYBHNXeMCow433h7tY_n4in9JYCP_GywZPrXDQWJvCvhRh0vrgOryyKUCXY72PU7o-H___zRJd6A9o-jl9XOQiTsoC6tF9lPvKK04dbnKmDtTILcY7_AooPgRfS37Oxj8MsEi46tYDVPLSJUkA7N9i7fmPwCc02GWR_FItgPZFS6OoEVfghH0BY7s8tt6XOHVSNR36lghesGH815sHZj-pj_9pLoQM8Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین بازیکن 6 دوره اخیر جام جهانی؛ زیدان، فورلان، لئو مسی، لوکا مودریچ، لئو مسی و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26151" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26150">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glHYNpIqR3njFztDM8EDvBQIPTLfCag4EJDomIw8ecXz-AV88yGD4b74ywGLyyml0817KhjtkygV5x2erya1DAAgMxb7-Ln0rPst7mPctp3s4mi9--inbXJkkxrf89lNqAK6Owf-QVEQ-eSWFIi_AZgPVcwmGz_2NcEJ55cLpOQOGt-uC4JDYGgLYNAgNhB7TlzN_UxsSNmtemfwqJdS2I4Pu3lE5QzbHbosZDcXTzKpE5-_7yxuaa_qVRaapnzA3YoW8zkpvPMKXZPZyl8PML-KR91f9hHyhm6DMr8u2VYkUIGaSxV6RIu8qN728mk0aLoupMSNQB1Gkt9FRea0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26150" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26149">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=A9IR0zoICqYs4Z7s4CWywwWzk3sF0fqe9JBPGK2PMS-IGIBE--Lio3PSneI1bbSDo4OTlHmdNSJjMV_SLTLWxtcvwiipr4EdYhacoBgm5qwvhln9HWSJr9nhmeL9O3DG6FTgVd0YJFFNtPq9fpUzu4cH8EZHGUVz4tuhGTyZzhBdK2QSY1aXub3CnMi5J8CvmzSXQ8Schayd_FcSfX5bvDGoKDmY9Tdf1xmADGC2NdANiNZZex6isgg4NXf952oXvhg8wjr7CBYO6jH9bW9chAYddP7wlbexnhwr34G5Jp2AFK5b1QzQpu1LSyYEuFsCURHjdlo_hvxtMYSJodbtpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=A9IR0zoICqYs4Z7s4CWywwWzk3sF0fqe9JBPGK2PMS-IGIBE--Lio3PSneI1bbSDo4OTlHmdNSJjMV_SLTLWxtcvwiipr4EdYhacoBgm5qwvhln9HWSJr9nhmeL9O3DG6FTgVd0YJFFNtPq9fpUzu4cH8EZHGUVz4tuhGTyZzhBdK2QSY1aXub3CnMi5J8CvmzSXQ8Schayd_FcSfX5bvDGoKDmY9Tdf1xmADGC2NdANiNZZex6isgg4NXf952oXvhg8wjr7CBYO6jH9bW9chAYddP7wlbexnhwr34G5Jp2AFK5b1QzQpu1LSyYEuFsCURHjdlo_hvxtMYSJodbtpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26149" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26148">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqTemamjNtuDoUBDjNyEeJypuksXWx7qNS2GbCpUGawVQoBhXN8FCc9zPwF_aQJIqg-QEi0Db0b5sPYecdnVNCs8Ykl8demX-5jsOYoWN0tcVBdY9EBi1xUHmHBfv4Al6SMwCfKciVX7BK4r0bw93aXXOtd6Jmh58axa21hFKLwnKvlWC4Dca5YxGvFHfzDMjCpCRoT9K5MfGqIxyfy7WI-ILsXm-WpduvOdPDDeXtTbDn1Z23-5v97JTpABbgKgj_QgHY8Yq_90TyhtY4m78JVgo4SjDeXD1dN99GwggZqGzWzPsFMBDBqKanclK35IhWo6gpWIpymQJ6QO4HdwfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تو نوزادی مسی با اون همه افتخار نشست کونش رو شست. تو دوره نوجوونی‌هم‌یه‌کلی جام با بارسلونا برد. تو 16 سالگی‌قهرمان‌یورو شد. تو 19 سالگی جام جهانی رو برد. این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد. این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26148" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26147">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dykkBHNQ_r16kXuc7KtbPyJCMUfR08kz2kv28spPR9ye1ULerRhj4FUORVd1Ur5ypA0IUXv15ctGSK2CQP74XTq6cAbPfjrLPm7ItselFEKH9GQLKW2VETtZNpT1ppyd7prYbGwuYtMbDHjgUh5jy74sr-5SywvNheFo_hc2pffErqztfL4s4VMehy2MaiKLD7M9BUfr9HnyHIFP-htciTfQe8EqiVlfGQOfirkNukwC3PDMjpSdgsiOyTTHJ8lWgUwJt34-7tL6YIvBQZQq8QtS70Hk1da6QQwrYHFXaO62_KDsTdPj5f7taZJ2CEbQVQo1GWdeoutnZa-bfYEX5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26147" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26146">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTjGHNqhWOeeI3A6b6i6FHhDVUkdk4ijHhtqI_wQIJKhE4ZVlcQhkcd-yVuYHH_NNE8lzGhiK-yEKFBh9wDHXz8cVHC6w0ECMdt6d4kLvH_tWoq_6FyLJwnMemZoGxbu12pfVSSmjaU6UKab-gjy5xdbcKe_UdFFCma3r6Jln0eDsBOvR-26aSFLiVxpbuM2tuVYLaUVkG5QODkK-KWnwMrgAzTRv68QRRAetbvCvlm5cir98ImR2Famh12m-BzQv_yFan6AKtv2AH4w4GTP1DqHBlvY_9SjH737Ao2sJ36Cpkt8d2TqZhUDydcEcJQrpBBGpET3MnhUNhq5aoQcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26146" target="_blank">📅 16:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26144">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bb2R08Ru8z8zez54BKyAn3EpmONCGw2HzE66VkhSJ5hi2umn3b3Ig-fsztD5aC4nilYO5s__MiAdeNrMxiA7BGnkePVd8XtnEhS-qd5wn9Z-wU5ifxZkiqGlWCwjE_NBIvZNZVg_c-fdnuGd-cMsUYs3GyLM1ZKPLMT_4r4f_u3gjwSwR1x954oBjtoST_qjGZMD0YcfDt7i1TfCe2rKhZAV_sfDHvLwpB7Km0A1wcUQqDl6xRKeXnQWxcbn6O0aJraq7HGOOTDtKXojQ6A4n4iPHoRgU-5QnUEP2WDOfZVlBUJp7KtHw6dOvs8F0Fy1dKFqV4QdrYkigV-woFTS8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTj2dIaFGvHDVyfQo6AyeqT5EL3x7JryaoVHhpUdYfNmJJdw1esdfE35S4tuirIdRUtWBlBQJRBaijOZ9rFKS_RVv9-Exe1P3AmZAYuDYtVw9iK8rpNRZh_DlTjR6BcG8Lf7KQQvscK2AQFDTBDPBmtY8U2SA2TN9ojW18uTdj2pN_yyd7zcumOBP2wzcb8mbYXs9-mH9XvEyz7NcyeOZBHSYSKAPhaQ5zZUiQCQWWWed1X9SuHTgS_ekUPtNBXj_4a8KksBdXpiT7udP1bqri8NqYCQm2Tgc8VgifLLBhl-wB34Nl0XzGu2ojbl5P_9_5X7Oty24zks1W1dFXdYEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26144" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26143">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0uTaeHKH0BBcQno-o1TsyjAV3vGQSJIduWSk3G3nyC3ddPdYhT5WJiQ8XOEfOrnWsq7tHCt0DPxndY1SUYCSXeJ7te1k4YdM_IdYz9vkIqxNKft6dSsQ5WJlxRy4vkN4VPR71iePAy23GUtffNcui5uykWaa_BZfekCwt6Zn4i12OZ48M_Bmzmx4LSpRcKtLIlk2LG7elGIl7NLs1Y8RIBh2wnyjs3TsELZmMFuiI1NSoqUTAhjBUvMzeCv9ZL-8jA5oOu2VqrNKHPiZ3TzvUaA6E8a4p32_ye1TE-KkE-jMzKA9thm0sPAqAPzyyvXBqz9OuufYKlm4dLzxAjfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لئونور ملکه‌آینده‌اسپانیا: بی‌محلی به گاوی؟ من اصلا همچین ادمی رو تومراسم‌دیشب ندیدم. بچه‌ها فوق‌العاده‌بودند و یک‌شب‌استثتایی برای تموم مردم اسپانیا ساختند. نمیخوام راجب گذشته حرف بزنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26143" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26142">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDutMnTkhFW-Ir1aQPQBn9YX_dtLX_cNfVE-OvmCWhsogcfQakmuURxxzuwgsCIigX-MPSFHUVP6GHDto6Blk6CurAWiFhi4kXZoEO5w1xVDoQKUkJ5TIk2bIvT3cdG7Fv-YNtIzcZJDt3CJkrTFpIsQzs9lkfjunHWG8KjEHYg1zlFHraw5ikCwya3IS1bHlQqUyj-8E_Zmuy5ew8ARfXFMDQjTsmZ1lvYLjXJxCGraBkhXRCCwqlUEsn3TmOEfn-irH8Ks6EB27s1JYasd9VArdnV4-Mth_XoETAJqICr1ycAVhQc5H_8CGwhBfDZ7XJFOumjT50tUTHkhi6uNsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26142" target="_blank">📅 15:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26141">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbhiMU-70xX-xgtnVs3vdUJcVlcl4iMwIaPuzVhTKqTchd0jPytv5WTakCZD-iX7f2fzJMBkEwUjFxR4u0jnldpsuJAhlNu5XM3OVu4pLtFVwEAw8Pp0aaEeUYayz8yt4RzZjoyA84yfHEvHRZBcnFou4DF_q7eicKxe_vc4qFdekjHPdBZTwtNZEX8j9yaAU-g2TDtYBoy7NkhmlP_yIowvL26mBhZQ3v7gkSz_1iKYI8UU_VCizszsY7Mkwts7BXW_-z3iNr-X5DTUtFWlSHRlmJTgVRVn_YkqKmGrT2exGT80UwzmQoRSBKbuCsbMaN-SmOxwxDjHyEmc2vtccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26141" target="_blank">📅 15:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26140">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=sUFCyCISVgKAJHKquVooc0avp6xEZiecKJ67XTW_qQBt41xGsFZcKE-VVorzCCEamcXT7L3ZeTpG-wL_LzCiOJ1xm2Ge7zup6l_fMpfSac89NCPLxKoaRu3u1j4YC38BO2_q0rRTxyzQvh-5WGvgNw5WvHnmwZT-nPoCcq38De4LCpCHz_n4qww9n_J8WzbAnAaVM9aMhF8jfELW0PyDzkqa48N8P-KPdR-FjVkywOgiaPMM_0oIXfMxqBQPwyqGwfEzjvV2it2IQMnzadbdGUkDaw9-5wVoSgjP5ZlKR2SlfTKQlQx0hb3b4rfSjifsdz2xgd-bblGkfvtBx9pYyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=sUFCyCISVgKAJHKquVooc0avp6xEZiecKJ67XTW_qQBt41xGsFZcKE-VVorzCCEamcXT7L3ZeTpG-wL_LzCiOJ1xm2Ge7zup6l_fMpfSac89NCPLxKoaRu3u1j4YC38BO2_q0rRTxyzQvh-5WGvgNw5WvHnmwZT-nPoCcq38De4LCpCHz_n4qww9n_J8WzbAnAaVM9aMhF8jfELW0PyDzkqa48N8P-KPdR-FjVkywOgiaPMM_0oIXfMxqBQPwyqGwfEzjvV2it2IQMnzadbdGUkDaw9-5wVoSgjP5ZlKR2SlfTKQlQx0hb3b4rfSjifsdz2xgd-bblGkfvtBx9pYyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس فوق سنگین روزبه حصاری بازیگر مطرح سینما به علیرضا بیرانوند
: اینجا ایرانه چاله میدون نیست. با کشتی گرفتن با بزرگ‌تر از خودمون بزرگ نمیشیم با احترام کردن به بزرگ تر، بزرگ میشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26140" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26139">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl4FTGE450bRiH6kHSb1g3ospOcWLHiOFzqSRx8DEvNkj2h2pjtcwKJBMu5QzRwv7Hh8QYO4B__5vjkeFeypFJj6kClGmkKQ6VUNDNTIL-w_H0Evz5RBc93Wuvzmg1ObT7dm6BzAgpycyGbyrlBEycwGHX_wSb3M162yGWNrq3uOK-2zbe8lwICgsF81ymJzluUMd7kWw5LCiY943XrM0Jbam3wsAUx3W7fxa_VuLLyMSlvlB08Lku_WLNNowsjCdbPH3sSHkcNeuBICgYY1jQz7MJe3ZO5mjazBaWqSDQs-B8RfiNYIusz3T8apsZ76evUIRLMqvQRXUdXr8GnWPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26139" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCwkE9o1RKfS6CpYeomCc4Zv3iaYykDzBXzHWvuUCbb3zcdT64tt4t1gOFFMr8HgnV74OYtp3B99ggrpJuvod46aKZsVJEOfE51BZCZlga_H_EyFu_x0fD_4gYn0a65XA3CZre003IwayNHv_2DjPdkmNSmDphvvgpKlu2_UOY-TX1-pZLM-p2t5QGAIDTfqF9jmMAxO9S4BOLfNkhOWc4nfRhK_ZdcbVHipPWg_hGHdVYQQ9jvDClT5wTs4mhh5AEBHMEx5BhxROHy6Rfch0NE0CkhGOzB1GSxZFMnGPSdlRyWaXeRz37NSSI4kxq8pRy-rQLawQDl-sESCCLFR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG3Hz6lVmz6TSXHGwtbKRo0zFdAFRAd-iMwS_iSPAq0fhDv1IjRtJeTyYcIzKS00DRLEwyb_SkbD-YP2fGfuO4JAgg4ZoYPENVxOkXFo2973xKd3E9H5crWEeDnpxGjmst3AImimvCeL2A7NvcemdlL-RqjNGc6Yw2b3yrRcB4Jtw1ssQo7JZIAoi6okZytuqi7Nt8HGs_q77KI9RGFKgAUYWKntRrp4Gb4XPfBqeTVLCAmN_-AznabnwIG7IO_aFDwo7fxU-6ic3A4_AxioqAaI2FbDOnML1FSjKAM-1vTSL95Yqt4a5dftB3uSIG2ew3BB5w8HUCdVnWwpOgz9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26136">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه فینال جام جهانی 2026 شب گذشته عادل فردوسی پور؛ برنامه جذابی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26136" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26135">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEDBJ-oCU5sYNjUMVTnpujoBWo8p6uX_kAObK4wZK3XnMXFnO27FyJKtyrH5t6KG81Vwm6-tczWxDHZmpQUazo_XemFxODwvYCN5D-g9T0yq5AYo6aV-t3mOt5Fd4iDPeai6Ny6lxYONGtN8uD1sTgfmaJ8_Ad_-mM6pdF8qk8HJmMu-ofEonBiQ6UinP19GYOAF6qTG448mfWOMShBI7JdnPXDkULklp78C2LjxxjkWiOrFnUnHJRmJGy_rnhWkHBGKQesMWi5G9XjZUEd82Z0ZxopH9Ko_Oc99PJZl-2G2d8ffyBfL40hx9VCvrzHk9nZeKUSl3VJDYZUDp8aGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26135" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26134">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTcbQ4TUgguaqMMirVPLTOz2oa9NaDfjxzUEUdzOL_dvCpy7rWHtLWHNvmPpc6qalgNvIqOxbC3NSLPpYXRVcRQx7Bk643izIIqITUwg5GuZVgcVFWg0R_6PSbIklnvimCFS9CNAPw8LPNKYgxfnZLVPtRlBM4XTZ0bkEbt7M9_Q1x1dSBZR2eHyJOMaikx4qLlr4DL973b8YtkFf_1ZbUJVdXI-4YlW7vWkucSbV2-T7cOimzZy3kBASuHmfIQPPmr9tdKjCrY3gjOC_BaiIG84A_YQy3If4aNzUX0ea1EX9BA2dsxFdyYMXxAE65CERkMKixSaYnHlQPX7GdSlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26134" target="_blank">📅 13:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26132">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7NFXvRGolZ5GS19B9n3z8BL9ogLeJb_uxZaqw5b_mrdXTcuoqv80LKw0cLwKo5z4ND_Zhinc5Z6QkUrOKhXsbi2ZwEeqbGqa6Q15fTrkolTFC3EvKc4l6SiPWUYxGw-lFUuBw8zTny3DRR8Uo1gtOifNvMfddt7Q_2XzGhNbl-l6Wuh-hryhwJAA9mE66L_n4KEiYnR7sVmKxc9c1IG8_fMF2oSWCtFoccYDeKuhNDI3JWNBoYfgAHILWS2OJDGWwYK_sYFKIsOnFwlfQaNNQyQU944TsrX0Ro6BAS3pGNFztmIlxpSgUcXROH1ZM_n9qUPgyJ-aXV2xcydIFTbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26132" target="_blank">📅 12:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26131">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2TixUH4_rYXIeBjMVD8zJVc4kNxJvpY1wVTVwLNAPDQLZT_bEgd_DidmoatKJmJhHn5462kOh64kOiCB_Vol00-r7Wl9rTJDKvxCPaQAKPXWbhC9vCoUPhBcDzab43S9UT7la0qI5lNilwInRIwlwStJOju6xSEe-U8wiXPN0n71TQatFw6o1TBcaafnP994dmMtgwuzqPjF1u37pmX2doBq9n7XDFPiXCoQbZf1VNC5_YyYeKLHoRXEqhTOhXlPskkpOAnSIKMl6UAl5_Q4DeeIBCMxmkF7MdJSz8akXbbwmKyLvi8EyC1KPR0VUeO0zwbf8aoh9lZfw2zz38c6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26131" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-BR4sYRMhtvM5i2ncle5jLQJ2cdfp-XEnlK6thXwcLmwDHu1rxPIg0v2JKjbn15Y4ku4dclasmG2pVTz1IGgqqwGDH1uG6NbM0_ccPSvkR4RA_Jh07NGgfPgN5oMxSYhECJ6DiuAcrBppB1qxz3wRGoYf_Ysw5xN2olTPUwR3z7o8kNj-TCfC3ZG_myfeMBZO-p4wDTLVYe5vJYggzZc0fUk7bKweIPqqX2dOpZDkCvBFdq83_uqsWRCVTpHT0gzruR07Bei_0Pys6g0M4L4DpBCY3kMnP3KPSud2qjMxtVocgSuniInryNWGB8pQUcfwMVlqlzMpl6mvny25rEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLR1OtcjTSslbO6saso_jGleUf_KDlMQUCBUGrpkTOPp-fH_dlIOjJ6LZBe6ELFXxDOIODmUiwBUKDQRYY1zZj2qtZQMStzhqpMonFlM4IdUIoydNPWPIF2Pu0NmNuVHxT24_jf8kSpJIg4oVHNLZ2nNhBc2I9nnPJEWiusxo__JC2DRhmk1iyG4dtRTlLI-Vsvcs0EU0Kj4F68qfOcUkHlkxvD4NULvRSAO_W0-jzYpDWPkvXYt2yXyCqbm1lrd-COOVDe2z21trxqtvz9-07MBbBymb9v4fz0IYGkBfExxAkDEswzyPDNX6UVnQMqYb9ZLPrLMpBD2E6ubAjMgww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2hsEQopD1xHqFTtWobsLdXPun9bclHcwRIotK8lSr7b3AJm7NZMyqsLvJ_LQgO5xuFYgfhWB2zcS6ilfeDTyP6eiHjXQkgHvu6NEvduEdrT1Y-BNuBhndbSdFH9-B89TLeJKKhNRX1OFcXZFC1iqelVCdGEfXVzmsRYBbHDLr6l-yfVxjYkjxyFmEJoieoaH5qkGYA4hQ3jaHDJHTlN01Au_cdlrg_Djcy_8in3X9_xiWYEFVhhIAr7y0Dfv8pMCs6JUxcMIf6OyB50kYZN8yeFXXfEtlbPjjDV4vuYLyGrEZT8slAeL6eIxISkEYHaD0hfkvE3QdLWo_Ssbkdsv2bI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2hsEQopD1xHqFTtWobsLdXPun9bclHcwRIotK8lSr7b3AJm7NZMyqsLvJ_LQgO5xuFYgfhWB2zcS6ilfeDTyP6eiHjXQkgHvu6NEvduEdrT1Y-BNuBhndbSdFH9-B89TLeJKKhNRX1OFcXZFC1iqelVCdGEfXVzmsRYBbHDLr6l-yfVxjYkjxyFmEJoieoaH5qkGYA4hQ3jaHDJHTlN01Au_cdlrg_Djcy_8in3X9_xiWYEFVhhIAr7y0Dfv8pMCs6JUxcMIf6OyB50kYZN8yeFXXfEtlbPjjDV4vuYLyGrEZT8slAeL6eIxISkEYHaD0hfkvE3QdLWo_Ssbkdsv2bI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26127">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0OQ2h2OGdomc3QcbwlqUUFnnjyS8zNBy1t2PBmsU94WbhtwR7Uh4fDUWbJlTrckDyraP70LLdQH0qeWPYTB-xS5xABR06iQNqGp2C-OyUYFaarfgKhW7cZHKiXcIncHkArSLfnTT43lYUIjwXnbFLMdsNvmN3sZD0qFoDeeWKn6w1eFBc6hoqv9krhCMtZ84A085W45RwbWOztpgDAmfBZToSBFIV9WwfMekiSwYU-DloUuRWISqE5PWRIwLORSeInALP5cdQ53qM_VEtmnQei5DV_lmYH3MqyF_xYp9UfualRkyE2Tih3RWDchtCrBIK2QaY-sjSC2L5HxYiHNtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق اخبار دریافتی پرشیانا
؛ رضا شکاری وینگر فصل گذشته پرسپولیس دو پیشنهاد از لیگ ستارگان قطر و سوپرلیگ‌بلژیک‌دریافت کرده و به احتمال زیاد درصورت‌توافق‌راهی یکی از این دو لیگ خواهد شد.
‼️
پیش‌تر در روزهای‌اخیررسانه‌ها مدعی شده بودند که شکاری قصد داره به باشگاه استقلال بپیونده اما پیگیری‌ها نشان داد هیچ مذاکره‌ای انجام نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26127" target="_blank">📅 10:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26126">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=BatjpRam30fxFvn4gPZHa7HKFvljjVJsUcG4CiLswyUCYIbmJ0ie90sX-sgv6CA6Umi4i7WDvKPl9DoyYqCr3vjHAjye_Zrp2-EtiNIVdEOSG2yQBi_WheixAe98be4TLXhfylve3hamsnJVigzZQ7cDuvyBIsjPYJ0O0cooVPtS8e1AffkuPaXfzF253is4GYhAXB704G6RHCplvYLucPCnYLFAo4TbIAEnMHeku_2dDCRZ6W7zRnSV9C2m09Ivppyfzy5IwkFy9CpqgCap81xDImfVngml1KD2iQ1wVkSATGDSt1YAEgX0GzD2ZNjROzAQrsqcKIC2hbV53pWbPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=BatjpRam30fxFvn4gPZHa7HKFvljjVJsUcG4CiLswyUCYIbmJ0ie90sX-sgv6CA6Umi4i7WDvKPl9DoyYqCr3vjHAjye_Zrp2-EtiNIVdEOSG2yQBi_WheixAe98be4TLXhfylve3hamsnJVigzZQ7cDuvyBIsjPYJ0O0cooVPtS8e1AffkuPaXfzF253is4GYhAXB704G6RHCplvYLucPCnYLFAo4TbIAEnMHeku_2dDCRZ6W7zRnSV9C2m09Ivppyfzy5IwkFy9CpqgCap81xDImfVngml1KD2iQ1wVkSATGDSt1YAEgX0GzD2ZNjROzAQrsqcKIC2hbV53pWbPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩵
آپدیت جدید تلگرام دیشب اومد؛
چند تا قابلیت جدید بااستفاده‌از هوش‌مصنوعی اومده. چندتا عکس رو میتونید مثل اینستگرام پست کنید تو یک پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26126" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26125">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=kBhIXvj_p4cavwP7xWrL419565UtenZNR1j6XYc9OMdnioH-OUKYxy75NNQtQmkYj9xUrn44PChd3aSCdbHbI-aTH8jiIhxEJ-AweoFb21xW4agG7ANJjxJhTsiJ--lGkPARsf-NNO5eA1kh008wZUt8hqNOYdH4aRIsZArozRkx40anE9znkgqzPxuKhAA5DMXglRNQVT1G9JnX_3pxUV78tUNGNDWZiz5wqKJEEUFTRilE4RjiP9G6AVFb9ri34ydbrNcnZiZ0MTWnl1CHusHZX-HkY7PNZ_lU1WSxR1_VlL49M8kFgOijcKDxd2p0lYFjV4gZHAWRvScy8DdItg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=kBhIXvj_p4cavwP7xWrL419565UtenZNR1j6XYc9OMdnioH-OUKYxy75NNQtQmkYj9xUrn44PChd3aSCdbHbI-aTH8jiIhxEJ-AweoFb21xW4agG7ANJjxJhTsiJ--lGkPARsf-NNO5eA1kh008wZUt8hqNOYdH4aRIsZArozRkx40anE9znkgqzPxuKhAA5DMXglRNQVT1G9JnX_3pxUV78tUNGNDWZiz5wqKJEEUFTRilE4RjiP9G6AVFb9ri34ydbrNcnZiZ0MTWnl1CHusHZX-HkY7PNZ_lU1WSxR1_VlL49M8kFgOijcKDxd2p0lYFjV4gZHAWRvScy8DdItg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26125" target="_blank">📅 10:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26124">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=d0-ezHgGbVRe7FESMe1xz8qqqVU2Ja-sul-avHOKDWsljHBgwO036Dm4qH_gCrwVkVmZyfBO70AyLB8Q_-liy7DI3Dw8793x5YvPqn62F-HVZJ1mUibYWDScYkzZU3Fqvxuh4JyzxAoXx4UmrQTQkFAgUeDYc67HkJOwzJfjJw7FOqT5O5lv7CClwLNDvdpl7I0969d5fFpdqM7q_rldaJBNzDaQtVNpEFBuFT879_SVdDdaHd59yJU5VsuXEgow5Bgc5dmN8rEPukS31_8nbwEXNxHS5eGXhr5Nbal-NRDmrY3mQgLa_p6N9hV5pSQulhlLkeeMA2j_cLNTZiiZzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=d0-ezHgGbVRe7FESMe1xz8qqqVU2Ja-sul-avHOKDWsljHBgwO036Dm4qH_gCrwVkVmZyfBO70AyLB8Q_-liy7DI3Dw8793x5YvPqn62F-HVZJ1mUibYWDScYkzZU3Fqvxuh4JyzxAoXx4UmrQTQkFAgUeDYc67HkJOwzJfjJw7FOqT5O5lv7CClwLNDvdpl7I0969d5fFpdqM7q_rldaJBNzDaQtVNpEFBuFT879_SVdDdaHd59yJU5VsuXEgow5Bgc5dmN8rEPukS31_8nbwEXNxHS5eGXhr5Nbal-NRDmrY3mQgLa_p6N9hV5pSQulhlLkeeMA2j_cLNTZiiZzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ‌موقعی‌که‌کاپ‌رومیخواستن ببرن بالا ازپیش بازیکن‌هانمیرفت‌ بره‌ کنار؛ رئیسفیفا اینفانتینو دست ترامپ رو گرفت جدا شه از بازیکن‌ها، جدا نشد وایستاد تاکاپ ببرن بالا؛ فِش فِشه ها اتیش بازی بالای استادیوم چرا آبی بود. قرمزنبود! ازقبل بازی چرا آبی تدارک دیدن!؟ فکر میکردن تیم ملی آرژانتین میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26124" target="_blank">📅 10:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26122">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLGfUSpu4OutduI86EdqsLWXogv9k9oFB35zgqMxW7YSEJ0NNX16MBoNrkapMdzNJl_khXSIJWzebf-73fHkpJwexXXqnFipVvb5e4kxe1apTPB8hUTvdAGFZUcJ4gNwxJDXCMZjj1L1o1d76TZnqIxp_M2EH-I0PonyE_nj7_2xUhA9i8SlJNPUS3KgnFH4ta-JJKXJUYpZ33B6zYeZaad5K1CJfcEqjyKu2mHmxKRur_PQkrvkdpPA4RykGM8DU8gAbcEvO0-b0MmCfN-LH313UvHNe0zW1oqkAdAsqOnE43hyZfLVb6-YmreWRefVSWoB4YNjrpBO7FWr4xseGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IamqQY3_c4bmNl1Q3OANd496NoYMiTBin7PzCqkJGAy4UXpUs3TWv0KD_L8VR3gVcahB9zRrRUTRuBaXTUV7iopuOyySSm7D7KOt86ZG1ExPl-bYcFJ2TzUjhW47yvF0QwqlDrM5sKKf3Swcqxu_fU9gJ1dzU80rSnyxm_vSvkbl_xjLgBhs899vzzi2yQNTKZiq131-MBusxqneCbkTdnzPq57SMX3pNwXojRSNrWriWmaJHPwHiiDSu01hl_SrRiE__O8hEZzoDUTAhQsnd3NcHo85ITBRVDZoXk94w998p800Qfmpmke8_GSYx1vRVHlOS0H-lQGVatUd9pI7yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26122" target="_blank">📅 10:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26121">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=IQCBAFlbtPSaRvL2XIvtxnMBxvQ7hjC2ScPOTGj-DdxcbOeOiBSVVBGUSJG5ptfkTOlL7dFpQbLDTRdssLxEm_u1Fx5B_CBHubnpwKVrt1xN6IlqhhLdMHTGDn5Xtdqd6qFNdzozSdU1hdERJZFi58T6qtsXEqvIrt93EIZ8nGGhwyomYxsNZdnbAqnnfYSwvZ6YNhQjNXWfzo8Bprkyy9EKYolv4DDDTewu-NUWb70qV4P7qwMFOJJFw7g4FlF1MZlSEgQG-fhfzTcpwcJ_h-27ZUcz_UtVlBIojH790oA3De5MXPWhfwPVdrzXXRf_BekPKaY9udL1VunudEXuwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=IQCBAFlbtPSaRvL2XIvtxnMBxvQ7hjC2ScPOTGj-DdxcbOeOiBSVVBGUSJG5ptfkTOlL7dFpQbLDTRdssLxEm_u1Fx5B_CBHubnpwKVrt1xN6IlqhhLdMHTGDn5Xtdqd6qFNdzozSdU1hdERJZFi58T6qtsXEqvIrt93EIZ8nGGhwyomYxsNZdnbAqnnfYSwvZ6YNhQjNXWfzo8Bprkyy9EKYolv4DDDTewu-NUWb70qV4P7qwMFOJJFw7g4FlF1MZlSEgQG-fhfzTcpwcJ_h-27ZUcz_UtVlBIojH790oA3De5MXPWhfwPVdrzXXRf_BekPKaY9udL1VunudEXuwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حماسه‌جدید خیابانی دربرنامه زنده؛ خداحافظی اوس جواد با مسی و میراث مارادونا با شعر مدونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26121" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=IMwTJ5qGhTligDwo5UB8Ukh7uBdKVrrzgfN-eByl4yAvgid_dzWXS4UJnnksjFDVVMkifS-n0wPmjC_zK9mj42KiLOR1UN1tVq4z6szY-Ij0OBmKuILIXK9inp94LJNJ-BkNMTNutkp3s5c2Rt_mH4qwrxqEdNoZG3oEGKTHYPx0que5dkijSr8qJc_AS172X4Uwt16VmuotbLMj1MbhlaeNbTgnLirdTEj0EuVJVonloH4Nb0WOplbv8UNRx0NYZW4mRZ5_FveEwqr_jDqPpUw4szjLPaKlAREO-kNEBCS1E7NOqAz_tJP8F7OjfHmJQpbLN9MLVswNrPZbz3rYeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=IMwTJ5qGhTligDwo5UB8Ukh7uBdKVrrzgfN-eByl4yAvgid_dzWXS4UJnnksjFDVVMkifS-n0wPmjC_zK9mj42KiLOR1UN1tVq4z6szY-Ij0OBmKuILIXK9inp94LJNJ-BkNMTNutkp3s5c2Rt_mH4qwrxqEdNoZG3oEGKTHYPx0que5dkijSr8qJc_AS172X4Uwt16VmuotbLMj1MbhlaeNbTgnLirdTEj0EuVJVonloH4Nb0WOplbv8UNRx0NYZW4mRZ5_FveEwqr_jDqPpUw4szjLPaKlAREO-kNEBCS1E7NOqAz_tJP8F7OjfHmJQpbLN9MLVswNrPZbz3rYeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=eS74ephkPYt2RGGkEpmNQIdrKqoBJa-PyOUbXS_y_QfG4sLw1otSWrAXADv4lg75OBm6IoZC1Fj1GbRmSAQVZSRIl9hLfNVae5g6lg4dLPADBdIGkL712R8Qdtz0t5C7FxqTVaqFbLRvR1MrcrMU6zeCQ8bYikGvGEowjeby92DYp-jopg4UMWxJ-8qbXZAyDqnpZCO3HR3-cJIQ1f4JwQgxrOx464EsDbyA856ji6GCZedkmsyNl0QaLHaX8g7V-7rdjZ_H2OnBGyM9EpcrN_c_MuSYdEf2NUPwsD_7_G2rGb09c0dxnT-BN6Q3YMWEK9IL6gI5S-MAxzQ8-2Lc5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=eS74ephkPYt2RGGkEpmNQIdrKqoBJa-PyOUbXS_y_QfG4sLw1otSWrAXADv4lg75OBm6IoZC1Fj1GbRmSAQVZSRIl9hLfNVae5g6lg4dLPADBdIGkL712R8Qdtz0t5C7FxqTVaqFbLRvR1MrcrMU6zeCQ8bYikGvGEowjeby92DYp-jopg4UMWxJ-8qbXZAyDqnpZCO3HR3-cJIQ1f4JwQgxrOx464EsDbyA856ji6GCZedkmsyNl0QaLHaX8g7V-7rdjZ_H2OnBGyM9EpcrN_c_MuSYdEf2NUPwsD_7_G2rGb09c0dxnT-BN6Q3YMWEK9IL6gI5S-MAxzQ8-2Lc5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=ucXvyGpXQkxqruEuyDhVaEqK4nqiN02T3EJ43gj3p3eGERBgR-29zrin4qY_aw076dXl4uI6oDeNjm37qKFc9ZQceRtV49E8cv-fOvHIerwzIKpu6tGHE534ku2oPGuJo86niOHnuKQ3UwgyS1BVpJRn0IT0AOQanAX3kMWHnZI5K962hTl9QNblkyFH71HTMb-fwaSrbiKIcaxnoawM-G_eKB0-n8KMPQQIVGZXmM3ipR71lOFJOXfn_l-hpw4u4iXIapDyU8Ukh5Mb7tIOPmP2hANxFRyoYEiXDHMK6AWvfUH0K-Sj6jfcH9UPBA1CqEVelxPcqF87Y5pDCLzqqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=ucXvyGpXQkxqruEuyDhVaEqK4nqiN02T3EJ43gj3p3eGERBgR-29zrin4qY_aw076dXl4uI6oDeNjm37qKFc9ZQceRtV49E8cv-fOvHIerwzIKpu6tGHE534ku2oPGuJo86niOHnuKQ3UwgyS1BVpJRn0IT0AOQanAX3kMWHnZI5K962hTl9QNblkyFH71HTMb-fwaSrbiKIcaxnoawM-G_eKB0-n8KMPQQIVGZXmM3ipR71lOFJOXfn_l-hpw4u4iXIapDyU8Ukh5Mb7tIOPmP2hANxFRyoYEiXDHMK6AWvfUH0K-Sj6jfcH9UPBA1CqEVelxPcqF87Y5pDCLzqqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26117">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=VD19acPkYP0u1ZMmvMvY63tvZ2zLENMhe-kT4FPypZHLN4d3lNkbowVC1CVIzs25jomkZKRgyMTw58I5fdrv6-53dZAsxffTK-or6g1DR-QgNhlqKBEfni4AXWftjFE6nMJ6XlDmKkqJI7K-Yhuft3k3sABwwtaSGeQpXXDir_yxH0E3oaR4givt_2NFBXynYrgX8YEm1tunZLyPDZtkiC-3QH1PAbLPEXJK2jJJiVZNLG36V1z-RDD5gw18oPCSuYVBqTI_uzHHXtM_uL6qLsm6liwedA24UfMxA_FDhgB0wewM1u6zlD7AEt4gwCx6tN-e4MF48ncxwf4fzmemHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=VD19acPkYP0u1ZMmvMvY63tvZ2zLENMhe-kT4FPypZHLN4d3lNkbowVC1CVIzs25jomkZKRgyMTw58I5fdrv6-53dZAsxffTK-or6g1DR-QgNhlqKBEfni4AXWftjFE6nMJ6XlDmKkqJI7K-Yhuft3k3sABwwtaSGeQpXXDir_yxH0E3oaR4givt_2NFBXynYrgX8YEm1tunZLyPDZtkiC-3QH1PAbLPEXJK2jJJiVZNLG36V1z-RDD5gw18oPCSuYVBqTI_uzHHXtM_uL6qLsm6liwedA24UfMxA_FDhgB0wewM1u6zlD7AEt4gwCx6tN-e4MF48ncxwf4fzmemHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26117" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26116">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=ezJa9Y3dt5Se9VQtd52_UGTld5PwEZdO1MVW5VNfAkkQrQDHdaQwFJErMGJaSHjNmsRvLqO6Ulw2-gBpiqJdhRQz71V-qwvNAUQ6DxX5ccZL4t1CoFB8bfGNLWgHxokfTswpYfSfDRuKt6O7FjAUCT06Zzh5OxXyj-rfNSJl1qqfktU3lM5OFqOuacEAB0uROH9yP_DHDA_y4QQuOKeq2X3-akNafO5AFEQxnnO0oBvedFtYd80EwFyWzIJxC5eG7LOit6KBmOBNTXrKswlGkzdyTYQYLJfrMfahTRuODpWf56PoTRXk03w0rPBActn8p5_SRnZt1lMZ7mH99NinOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=ezJa9Y3dt5Se9VQtd52_UGTld5PwEZdO1MVW5VNfAkkQrQDHdaQwFJErMGJaSHjNmsRvLqO6Ulw2-gBpiqJdhRQz71V-qwvNAUQ6DxX5ccZL4t1CoFB8bfGNLWgHxokfTswpYfSfDRuKt6O7FjAUCT06Zzh5OxXyj-rfNSJl1qqfktU3lM5OFqOuacEAB0uROH9yP_DHDA_y4QQuOKeq2X3-akNafO5AFEQxnnO0oBvedFtYd80EwFyWzIJxC5eG7LOit6KBmOBNTXrKswlGkzdyTYQYLJfrMfahTRuODpWf56PoTRXk03w0rPBActn8p5_SRnZt1lMZ7mH99NinOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:
اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26116" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26114">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIAfIIhrXh7wS0ce_sVfHesTZUwNmx0uSBRezsdoPQAEk64OP3bOKtAk_X-30SXn7OLJgg8MzqtDWUih9EsyW0fOyqc_ywQZIMffVqapJbAbN-gacHSBv-JquvxsRK94jvRQkQ4bJ1XE4nN12faJl0QgedJAsscCr4QdEcTWeJ3zQU4O0vg685Kj2WoQ5SJPmRmHeoGXXLJTWpfzDbbyaR0_0NRASI2Z42xKQNx9ZN3SAyQ1LH13_xblTgERD7ohIdtmLJtMAbkSDZ8iZqg_ETJadlx6yK84TmZtyZuDKtDDIEQZ_4YLPUpVJDRA-1oXms8b0OmohEVymhaFrCJXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26114" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26113">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwJ-drFCZhJymeCGPDKn0tt-KClTmqP5PvNaBlKRgRBefCBX1sWGtaFvmxcPETmFKQBw5-sP-3VjatvN3MvzeSw-NQZwhAlvH8IbUNIiTf2o1U2fC_VOrXfo2V6fE2Qmel6RvTOqm7FytZmrRiZtR1fNTFGT2LXMyRn5J7B9sZtJx6fh5mKaxE7ijNxvaWGUf3r5JQ2txWpdVxmyjZT1hOu2SHlfpF_32DX4l_krDsym3wc49xxb3IB8itDWDymWBDqwf8l8qurA5i6ML94t7RbmCT_0BDpaDzfLXf7bP81YKAMMXdUwqih-4DXhelFSmt1GWuOFJ6SNi2cKWeBw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26113" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26112">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDul0uARsYckfxbfOj9-5Gh0ytKTq1qCNDvr1SZU5-SO0uZ486pVDTY-j9WIZvRcj0v0ugqszWnoesg8SYf5WIU9nBQZq4nQSDAfVWo6WknJUS4ZHl8eD1hGLBPhj7XHIsoLgv22hLmhZyqYAAZ7OcR04tBCTF01CIl8QYeIdknSmA0-WaPzCKs4XCpLrBn1Sj2_IBot-TYmnnVtWv52mAAcHSLMzc9uYpZnw7eEf2D9QDPU2-ZuJcOydHDDv8qXutbQMk9liKs9xASgSLcIemtJFNjSx4k2pYBOQUi6qKI_CKNDgb3SD3dS1j1BCPR2N4XtwLWKp1xsCgcMZAS8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26112" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26111">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Haps-sX6SFcWL0zX8Pf_EEMWHJmwNIsCwNfekV26aQKkqH6L_1OKx_4NLs5pGmEkdm6lk20Ux9F2cl1Jj8pUh-BNJRM5xazRqDEVvhGrBXAu5qFrpCK3tY3-phzAIhUPCbzlwvVzjwwzfiNoLD5dyaR4OnF07w99oRDpn4cScCTjjCn_mLO_9-oKYoYdch7II5njwwSCI7uLO02yWjdLNP9KcbD_4hadxxgGs1duDDeLc9xpV8XBvmdi5K1MWDwIZUF7PuZGlpnqOkj_QS_Nl-_mzDN1efSeNPsfgdEUHvuyAcfDNqslOqeWuNoPAzFFxA0zuotaN--HT26ISis2rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با عدم گلزنی لیونل مسی در فینال؛ کیلیان امباپه با 10 گل‌زده آقای گل‌ جام‌جهانی 2026 شد. همچنین امباپه با 22 گل‌زده‌لقب‌بهترین گلزن‌تاریخ رقابت های جام جهانی رو دوره بعدی مسابقات از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26111" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26110">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQqkN39nfuE4uMOfK02OmEmQcgDpaWpSfoebZ2wPhAr6StDm9kzDCFw6GJqk47pgF4qdN-ejI_CxKK4Mv2mHU3pKMtbfKVgFhhn2vrHykys8bwZpL0WzhiOwx-FBHOaaM7huzm_1RRrYtsHEqRHMvu34GWxrCMz0vyvBd3AApET0Kem2-K3kB5L-9IvfkE7Apcg27FKwIrFfhxWIPBkT9NAE2Sg34YFI0JZaijyOuXK7P3S7AKK_N597p2ygA8rCJEGEOfBCMOixnLiQBKjRedCwHvloXrSYyJpb9LypCtWfjq6N9ckqRZWvVeIkgI7cjrn9ZrkM7gSX1e6F5fylWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
پایان جام‌جهانی 2026 باقهرمانی اسپانیایی‌ها و گل نجات‌بخش فران تورس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26110" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26109">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPafFH3v9-cevQlm9qnZFf0jLADbuolTF10oX_w4hml-C3AKpfg9eEDfRzQ_-FxT5XMLPRQCxkxETNd_E03FOUuFmr-OMHPDDJuZLyn1xaFGOb13y6hvkqjR5dNH0UauZnb4vUzNBu-y5AgJ4nPYeOgCovtJL8FLL6e9bky0s1KsQ_G1wqaQU1iWORpksMMBG0QntaHKpAsJlT0kt5WE2Njn4ceFq4U21v40C3CDKF1YFFQ52fhgzwAX7IvnJxlCjUJTnwPZNcj-J4CSdLoh4qB6-bvmKN197iVHhrI8Rg8sr6SrTgPj34deTt0jOxATi96YD4NFgpwd7PU69dEyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرژانتین وقتی فینال رو به‌اسپانیایی‌ها باخت که دریک رپر کانادایی روبرد آرژانتین شرط بسته بود. او در این جام جهانی روی هم 10 میلیون دلار باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26109" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26108">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWKiKBQtdfLjpZpU_5XRGyDKAzIhXWV91IwCwkkbaUdz5QJF9a_CqQDCu-iZ2MrhNODOD4roTJWejDQJYCGVVOf4DjyWExczybMMBpNF9aMDOaFXO9cF7C4ZYauWom5LTJ-SR5vSKZSva74Wa9kOmmdb3pdEbZ5dvnuTHe2chAmJSbanxbAs2M6lCAH5FuvIh9k_X-3emTH3tPna6m1vzc_HHePAA2tbvX-NOvEcxpwppuPAh6bS-HqEoVAIKziCdsd528V2NzKjtVu4U5AMqdo478xp2V5kG7LmT8gMt-2xOQbPp8htJbJ6WuEFyjOA_PNBLsLeDt245zz9ecK3pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید بلینگهام هم اومد:) فینال هم یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26108" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1-5RLFcAXVxs4qJNNK74PBrH7MKtaXu3NO7AMjIuDhBElmp7E9VKlOkY07acBJaEhWg-qdOVuVYq7YJzXrvPC-o3WcUTZtHxHZYRnq9dlbEVAOaOI1qfH6zj6aaOwjEDUBNvK-55iiS2fe5wFC0LXfnL_gza-pq9HQkI7H4OcuQJ7oDir6RXgop0Q7NJUjvmaY-YN8EV4Fo74tmqwfMiclmJsIJ8cgvUoWbST0N6s2nOli3xjt0L1nsRd0YTxnsS2h9p3akanrSeWaVcY7kh7y9e_pUcnGvL5c2HZ7Jy75GD0wnN3a5VarSi2RmRf6NfaYnYoOUYxcEqYmCJprZ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMdfUhvt_KFU9eF1NxQ0PSdZlJ4BCWIVUzdoqU4Cut4K-xj6c1ss2VqhMuUoHFFsawE5NS-n9VPFqdBB5yr-E5drBF8JgeyWSBiN-hy-uVhYUUst5bSo95biW8Cct8wLoaecR06MFOxeN3k1wDgCRWuAVU_wZrUonTNlTHZLw7hGZoibWy7rPnku6EyG71Ulsg9Bj_6llNolF-_O1gVmIsIJTqdGMa0ooabwqOU0IG3s2k2C4QQF-61pLQGldvbswKj3kR48aYSYKiiFKCXADRxP4hSa_E_0WBQ81Gb2Up5pJeJxyW-qg3DrSl2NhiFk92c7Ddad1CY1iyGHEzBEpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26104">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMQz4e0nPCCZ1rpAwvotUc_UHVDVwaW1M3iI7X6uyMqMDfepNPUja7aOGY96Nc0sJqMv2JFv4zIvjd7n0djVUBzQ12VvAlaHsilmf4Cq3m7IBOPj3grKhSgKqn8GH63dKAcsEWH_GS82Sm_NYEq68_2r2dP9Jm5D3jjKWGA_JxZ5gWv0UHgdTYHlCBezi_EXfroVZcQFTWsifvrSKIMzH5memtGdjgitoQcZtHUukViG-AgHrx3Xlf8EAroZY8SrsTlk7heHQD1hjSorS5PvP1W_C36xuF8kmo8wwbmvta_snSaOTrVzYXVG85C5xIhcR9wOPr6YIxHBtHgmqsIZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بعداز 12 سیو بالاخره‌مارتینز تسلیم‌شد؛ گل اول اسپانیا به آرژانتین توسط فران تورس در دقیقه 108
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26104" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26103">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=pgJp4MdBwV_X-bPL48F3YYQnxDXkDjdS8Cxw7V6kUG5JSqutxZhl6RhWDUMcbPc9T7AwR8Qi-gikHRrlqjSM_C7ache7LdcKB6yhmjudmL3vT3LEMuzwVojnL8SyLVwV_M6ldW8TbwGdhcBsg8vBr3H6NrDgg2dCSl2GcXLpiCYy-gZvhc3xzG6K6H-8oGy3VNz3TCjVnUGq58eiGzBCLnPPd5F3-tJv0z5lJ87dTRMQCgvM1pI2Ad8X-n70nw2xw7-CRIBCMRBwbvJhD5MRVcyW0WIgy4viMVu2Y6OKbrTnUsH1gth70KUvIUwrcKfIVaCBiuoeFxu2nHWKDOFn0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=pgJp4MdBwV_X-bPL48F3YYQnxDXkDjdS8Cxw7V6kUG5JSqutxZhl6RhWDUMcbPc9T7AwR8Qi-gikHRrlqjSM_C7ache7LdcKB6yhmjudmL3vT3LEMuzwVojnL8SyLVwV_M6ldW8TbwGdhcBsg8vBr3H6NrDgg2dCSl2GcXLpiCYy-gZvhc3xzG6K6H-8oGy3VNz3TCjVnUGq58eiGzBCLnPPd5F3-tJv0z5lJ87dTRMQCgvM1pI2Ad8X-n70nw2xw7-CRIBCMRBwbvJhD5MRVcyW0WIgy4viMVu2Y6OKbrTnUsH1gth70KUvIUwrcKfIVaCBiuoeFxu2nHWKDOFn0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26103" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae_878DbKpwHMOjTuw8IOPliU010Q8WO0IvdT6F4JTszAFFgxgT3JvOcM9j1H3ZE6BgxLLNDQhwlOQ4GHofJ5lfxp8q91qhlqJ5_WHNYyOQnXFfZF3fOCz8DDLwVKUjQYurHXrL1HM7hiC8SaQbMfaaRtVumHgOiuiHONxMPTHP04yZLrEDGga31_Gl2u_BEbiSdEZ0BgDqzk2un8nIesG-VXT52OnWmmgH0jmKedU45WNkYdVs3xBHPjyR9bTrXDOckZGkK7priqetYnPXO0Q4gAhj7kvEAkjORYIhbcML-DxszLmRJ5l7k3IwYMJcTdbBtSwtuZbA1dSbQAbrtnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cnk9-mZ4T9aytrtOOQ6CYfMyrw2W44GLyzJ-D0GaC_9ZwpoTbGqjQzVbDLP3TWZNPxotIQXTSVa8UXus2qx2byx0yrxcTGc7KLGwTUbNO0VJ6kqlYY-gI5R9v2CFZ6P1-b6a9SHfqPQqwn-eZYSe6tWDqYOL5xQmv2UvIzDpVrgh8WJVUrEbxepKacMH1QFix-0nWH0SdyOmmWgiMs0-DpQTtedlF55C4hvcIVotMiafIw870PFESHSabx_Zab-JVv3O4W_-nEBbn0YVbccFcufefhZk02lQpEOjo0UADLME-1G7vXoYIeWwqfEldopNDTr731NYSwCrHqiTztTo-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2wY-A5RfqB-OJAyPPtfQYvT7nXnqCcw89FTcIUi2BF6SqtPBgu6iQRctpyA3lRlDaLCS-AhPJJI2fQZeMppoOSmqHmGy5-AsmBzulyTcUXudHh0cjm6G4uFiql8ZpOouUQ4cpiRt94MvadyEVRXifr44OGT99I2NIMMzkDZMa8eQXGoR7EFegGSKI5Bjqggu4lvYy9LRrSZSgFG3saUFgbzm7PZkIFGXy-D5dlYkmfNe69kix7PvX9J_9Nuhfpcluem9jof3UHh8gIK2G31sDGcc3s5Lah1wBXM6ZREqYxSogFsOqcvtUwo7BnKLdkpDMRhooSvXd2SsZ-qt50EMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YgttSAjFoUMDM5H-UHVcL5I-WLGceKGwgsO0q_8TWkbAo5A5jlAUQs-NRBg5Z0xtHlrzzYaFFnmhQvObbIOkW3Km40YdO0kdIwQ8_1oeOVijTBRn77vCpiA85BprpB5ikkYBCFD6Iv1itJRiFqLIsAXLy5o9aWQhsvP5cz6TUM8OUJ3FLNTuHmMxi7jgigTMDAoh4JDl1baivyFQWyZ7RaHHDXw0pZ6-oynqk9Mzldbp-NUUcbW3yEqDoB7HXnRXEfhTXxLmof4U5VAMWH6snJeZV0Pql4RTdgqFJj2whDbl5MAcnfhYSPPrZ4_f7rOolZh16IfMHN8Rm2DT8Hgemw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrxKca2N8f6phVMK8NI-gGPnnciSZ0GiE_7jg_26Kw-Pwc3LtiyQB338s4-IDIP6ZuHscPN4kgzZkNCLd5izaAsgGHqIGSHjTHNBfvd8v8by919xaoEXuINdVY7Zqzd6hLICWPXypFfyFB4Rnjd7zs616KiCThMPNIOSqBzg-kq3NEP7juS0WOjKcU7z9aSzs6A7ntYcXeiG8C7GtgeH_yyA6QHW2GeRHrdSIKoX0HHxsOSWSB185q_hlT20LR5xiu5KuJqLW5D3oOP50gHHIi_YfUuCg-5_bihAOyMl2T6Emrx3SVCcq3s1i68Dg7MbUj8SWIZqniLG4G9jCsA7qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26096">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=bAQNUQnjuLBVy6lV2aP0luPgvMNzJxE6QP-B42bnnAOf8o5eWHENFk4TCSLneADaxdC1CYQruha1QYvE5LypPXfyAWiHqLRyV5kqzv8efclYP6_j_48D4teaMkD2EKJqKcsig5yN326skkJRq0WFd0Y1TgNF0akuen-2ELtfZnEXDxVE9mv89sKMNkKFGvcg5KHa85h2IXybuwinr8-YQaDHIh9Q43t6nGUmP8NKQDp88sO0PkalWhHvaX3Kqdohc7cAd4luc8Qx5rJXPr2P8dhETOgOf4YEeHGSOUVaN0OphNaQWy9aXn-5rZOY09ZKwTVPEYbTkdR9x8ndbIhyrRLM-UnHh0S9-6Kvq86MBt-szZhVUfAKYZ6ARWhF42xJnSBRteDI91P0TPrUuqp9MaiMtntoGxfwH47tsqLMtRoLWXs5jpyQJSeb5ic1Jovvd-rE8Pg37itn3BePRdP-Ll2yp8z9PxzeHloVPK09x-6N4OX6Zl-HTlDzE8p1slJiB9SKxLspOAf0-5UHxcqqjd9E2CIWX15Bliw1CBhMjNOwllGBCmHGa4drf-yg_I4kD8hG1T0eWrHWQxxWHIK-icdeRhqaItPUfv6AHueoPici5lJWuQK11eEfGD-E2C7A7xIgI8C1dwk3zejHvZ99EgN-buDoBDA_yfm9-gDA8xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=bAQNUQnjuLBVy6lV2aP0luPgvMNzJxE6QP-B42bnnAOf8o5eWHENFk4TCSLneADaxdC1CYQruha1QYvE5LypPXfyAWiHqLRyV5kqzv8efclYP6_j_48D4teaMkD2EKJqKcsig5yN326skkJRq0WFd0Y1TgNF0akuen-2ELtfZnEXDxVE9mv89sKMNkKFGvcg5KHa85h2IXybuwinr8-YQaDHIh9Q43t6nGUmP8NKQDp88sO0PkalWhHvaX3Kqdohc7cAd4luc8Qx5rJXPr2P8dhETOgOf4YEeHGSOUVaN0OphNaQWy9aXn-5rZOY09ZKwTVPEYbTkdR9x8ndbIhyrRLM-UnHh0S9-6Kvq86MBt-szZhVUfAKYZ6ARWhF42xJnSBRteDI91P0TPrUuqp9MaiMtntoGxfwH47tsqLMtRoLWXs5jpyQJSeb5ic1Jovvd-rE8Pg37itn3BePRdP-Ll2yp8z9PxzeHloVPK09x-6N4OX6Zl-HTlDzE8p1slJiB9SKxLspOAf0-5UHxcqqjd9E2CIWX15Bliw1CBhMjNOwllGBCmHGa4drf-yg_I4kD8hG1T0eWrHWQxxWHIK-icdeRhqaItPUfv6AHueoPici5lJWuQK11eEfGD-E2C7A7xIgI8C1dwk3zejHvZ99EgN-buDoBDA_yfm9-gDA8xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26096" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26095">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=Tm5zy4c1E--80bB0ueVdVGBNdj7aQi8vNAzHTRxZLPqOt6m4rEoNuQPTF0BSPhoS-8LaYJgPbjcc2LyTpP5qgU6FYwgqdOquAxmNmMVIqfpLh0D3jOX9bAO3NNYkeUwavJV_lS6QErauSUtQMVqDctTXNrobycxNuTpUAFADrWZepLlAVyGbdT2gallgjhBmqeeS5esMtjQoLgr5miuqzfeRsjGtN0KKhim2D6HsdEJdSR3_8BQqRj7qq3FlLqE6wqGuFmVNwxxAvqf3KKfi4bHxS6fDK8hVAlJY6t4ynXFysrim2pC6B1vOxSsLnVV--xs43wUfV0IE_kJBV44kCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=Tm5zy4c1E--80bB0ueVdVGBNdj7aQi8vNAzHTRxZLPqOt6m4rEoNuQPTF0BSPhoS-8LaYJgPbjcc2LyTpP5qgU6FYwgqdOquAxmNmMVIqfpLh0D3jOX9bAO3NNYkeUwavJV_lS6QErauSUtQMVqDctTXNrobycxNuTpUAFADrWZepLlAVyGbdT2gallgjhBmqeeS5esMtjQoLgr5miuqzfeRsjGtN0KKhim2D6HsdEJdSR3_8BQqRj7qq3FlLqE6wqGuFmVNwxxAvqf3KKfi4bHxS6fDK8hVAlJY6t4ynXFysrim2pC6B1vOxSsLnVV--xs43wUfV0IE_kJBV44kCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اجرای شکیرا همین الان شروع شد؛ بزنید شبکه پرشیانا اسپورت نگاه کنید. ویدیو کامل مراسم براتون میزاریم که ببینید. نمیزاریم چیزی از دستتون بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26095" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26094">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhcWEhn0lGQ_A_K_VjMVKi1aCxsAovskbfCRli4bisXKmAAzECFoNRtMnFoZmQbKkNkrYnU13BO28f2lNh4qRwjkMnywpzNZ4wXuerEEfn_7RfesczDWkkzwISvnnKm59ga7ptLP0SNiwRpg2ycybJwF_AhYN70MKQB_MFeSqr5AfwvLUVmGD1rGns7cEauw71X8w_icmUcRFKg59zWvV6qPQhpr3B_4LB2jMoN_iveLaIol1VU4lYsfAJerPhKiMAPYIJQmWaJybSqUphoJJsnnTddcmMijVCxke34sTmj5f0ie6V43rEbIS9qdjEK6d9ri916yBSmjHtsk8190Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26094" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=XKvc1PymgED-hP1WmAa9kf1ojreyEElK45zBkD08kGS36yLe-lSPFDa0JEBY3GovgKSyme9_QAt9OQKnWrUFjkVn5hqsze7KOjQ44HJqMqrTPb0J8L0sDw7Z8VBPDPo-medR3fuLaesownqDNQIwcHkTdRrVlAUWXAKdIlqLc-4fRua1mH-OhQbUqDapaHNTKrrnADfpHCNITbuce24PFPxQuMi8WMDfE6BSpw-_KUEV72BqITRdOhwQaHTA5r_ECpQh-laJfh16x8ZLQnGTTYKGnj7EkCjQATOlrqRmXpXuL6Bax3t3c3cN-jqWmxAMtBqWhaSXolO2yDNM9qmLow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=XKvc1PymgED-hP1WmAa9kf1ojreyEElK45zBkD08kGS36yLe-lSPFDa0JEBY3GovgKSyme9_QAt9OQKnWrUFjkVn5hqsze7KOjQ44HJqMqrTPb0J8L0sDw7Z8VBPDPo-medR3fuLaesownqDNQIwcHkTdRrVlAUWXAKdIlqLc-4fRua1mH-OhQbUqDapaHNTKrrnADfpHCNITbuce24PFPxQuMi8WMDfE6BSpw-_KUEV72BqITRdOhwQaHTA5r_ECpQh-laJfh16x8ZLQnGTTYKGnj7EkCjQATOlrqRmXpXuL6Bax3t3c3cN-jqWmxAMtBqWhaSXolO2yDNM9qmLow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛
عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFBxtT3JF4oCICXauA5hgqt_gM1Spwpb7Vd5sW68J0D0t49PYIVKgnB-6YCdonbAjm-quGjMlDlDi5Wvp2IEfB_qrW5UXzPVdAEKozBcHec_baLLEnFqn5AuDm5R6A322vAkNwRPDr69sGDco6MPg2xZNbU6BJcviUdhneCl3Chs-cB1jcBNGNyd7UVngOFdOgskHYPRoa9YbcSH-E4qgIFUHpf0USiFTny5EFPd6ZNBzWxNY1azM3AekEuIwq9ahWhR_udgnUDeCRPzkej7bbxIeRmvV1jQzwGTEXCaUz3MLpmUjIsiYt_xNqJy6Ki-hIDjEUUPzTGZiOcKjWVySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0KB8XRKtxPnq2LGhKsrbW4_owYvqzqReSu-hhPUZ5_L2jgW-2k0uP68Y36UvkLq2jFcSgvZvi33odLQaqf84geSlPU94KxXd3qVAoMoSbuDZK77yGtTqSZcNKUsLBE2Q4GvNQ-PP3_iEk6uqJFY7JD-mWM57_5t8dQXeLjd86DUnUaG3RzR4BeYVkd8-YXiod0ZoYO0YmO-Z7-MlOKnzaKgBJI7AumzwwIilDy-xty5TaUi7m8jS5u2iUxJt4kK_F2MvHpVSJ81sFLyyoXup9d2geZ9r7occ9h6ZzfxCQ444UahowcdXoDfIgFpfQiQ5nYMDv9yoyR_qTVZom7ySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26089">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=keBpk7fZVo2P-tGpQKushUt_4CKlxf9jk__BfipGjmV2hIOTbaplYJNzHcDOjkz7PNlL0MmV_pftZHI_TzzvqyTwAqN8M-vN3dGPGgkJ1SOeO_ITleaj-6L2wpfnM7CqKQEcCZemU_nopkqZTSaUjX3EXQ6XvOe6NJPoHVg9eNf5_omI3FNIV6NALFJvvg6TIJA5l1W75JFHols3fc7jL7B8__xte560eqoOze-fXHJIMJSVFkY5wQ2zia2MCY56jq_a_KlQl2dIDf1njWiKiibUrSm6XEsOpl0P0nm3sk6uJBMQgk6swMxrkJ2ZYD-kSdb2r23V9s9gkNNSRgqS8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=keBpk7fZVo2P-tGpQKushUt_4CKlxf9jk__BfipGjmV2hIOTbaplYJNzHcDOjkz7PNlL0MmV_pftZHI_TzzvqyTwAqN8M-vN3dGPGgkJ1SOeO_ITleaj-6L2wpfnM7CqKQEcCZemU_nopkqZTSaUjX3EXQ6XvOe6NJPoHVg9eNf5_omI3FNIV6NALFJvvg6TIJA5l1W75JFHols3fc7jL7B8__xte560eqoOze-fXHJIMJSVFkY5wQ2zia2MCY56jq_a_KlQl2dIDf1njWiKiibUrSm6XEsOpl0P0nm3sk6uJBMQgk6swMxrkJ2ZYD-kSdb2r23V9s9gkNNSRgqS8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26089" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26088">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jixia7CLozlOG6R2I74jSuqtk-3cJ4fTr8Bu3GD3DqXBxB2-r_av2tM3A3A02pXVVk6lu8W3pwSyQqE19ommE67Rt2y9_s5pLXK3BDBOBJvlgddd8H3DOsUsp4I0ScNjRj1D9vuL6fae3lpoUAi9TBGiAl9DllLbfceErnS-46Wkh9xGTavDJ6BY9LZuyw4PkvRSYrjNRyo3a3GYuINbJ6HBvDFrrsIDesbmri_z26FnNbL5MCklFJXDwM_aQaFlE-r91G6nLK2X7l8ySd11xkIdDgE5GVhsyZDq-9SMY4sH7-DfMeTubxj_oRyfY2t92-zdpvH9YgtyE-R9zdQ4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26088" target="_blank">📅 22:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26086">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68101d4663.mp4?token=C-iZdfuU9kOwGSmSFUgPvBCWXC7wlX2Ky1HRT4zu79IIzpu6Yvh9R4DjjQcPWcFchxfAQEFCZVwSlyD5XNGjuf2jnhQJrWxkWs6udjTnLcjjMHWAi5stv-d_oI57kEnps1DBT44LZCT3TPjPyTsk6DUqTvj2C_vCMat74kq5y3QxSCI-7ej4cMHOrSrkHnNfoOBMOFAVt-kGwTEgevbRAoUAXEPLpIb-vgClp7uYmBqnvQpbbgYhrhQfvXpqaO-f-zuwJiCwUwvwR2VEGw5-VSYkAvGDUYVUtb-UbT98QrJX0HrknMP34F9-L8dmPN6lZEyrhlS0pfKYRsnWR-xUsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68101d4663.mp4?token=C-iZdfuU9kOwGSmSFUgPvBCWXC7wlX2Ky1HRT4zu79IIzpu6Yvh9R4DjjQcPWcFchxfAQEFCZVwSlyD5XNGjuf2jnhQJrWxkWs6udjTnLcjjMHWAi5stv-d_oI57kEnps1DBT44LZCT3TPjPyTsk6DUqTvj2C_vCMat74kq5y3QxSCI-7ej4cMHOrSrkHnNfoOBMOFAVt-kGwTEgevbRAoUAXEPLpIb-vgClp7uYmBqnvQpbbgYhrhQfvXpqaO-f-zuwJiCwUwvwR2VEGw5-VSYkAvGDUYVUtb-UbT98QrJX0HrknMP34F9-L8dmPN6lZEyrhlS0pfKYRsnWR-xUsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل‌فردوسی‌پور: سعی کردم تیم ملی رو خیلی منصفانه نقد کنم امااین‌حرف‌که هر کی نقد کنه وطن فروشه نمیره تو کتم هر کاری میخواین بکنید. وقتی اینترنت بین الملل نیست من چجوری میتونم برنامه بسازم. عادل از اوردن اسم قلعه نویی خوداری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26086" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26085">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df505731d.mp4?token=d54ar3nLd1mfjDW_iwvAhaZHuOm6KGUnaDoKANkN7LOkBW2W3eB2QmT7kDudJwS_8QsrNFoReObinlBdlxZINlAPceh028llxTJTyYiA3sm_bPOjg6WBDbxsuw9SzgzFJUNuYzkHQWrzltelJRvk3nU39BIsO-AT2MLomcISsXzh9vUGvN0sReP5JaJi0g6Z-QoVy9TmdsTNhD-uFDQeSNF8RQcOy98mIUXSJTsPhLF0S04KljtK6uh0SS4mWJMf5URg0g1P2Y5WqMinayfcb3I7XGrx1mqxyHfkJW8GUX0fiDsC3d45m75qIzXaSvarHS7VPYdyZq3QyVUgwhQL5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df505731d.mp4?token=d54ar3nLd1mfjDW_iwvAhaZHuOm6KGUnaDoKANkN7LOkBW2W3eB2QmT7kDudJwS_8QsrNFoReObinlBdlxZINlAPceh028llxTJTyYiA3sm_bPOjg6WBDbxsuw9SzgzFJUNuYzkHQWrzltelJRvk3nU39BIsO-AT2MLomcISsXzh9vUGvN0sReP5JaJi0g6Z-QoVy9TmdsTNhD-uFDQeSNF8RQcOy98mIUXSJTsPhLF0S04KljtK6uh0SS4mWJMf5URg0g1P2Y5WqMinayfcb3I7XGrx1mqxyHfkJW8GUX0fiDsC3d45m75qIzXaSvarHS7VPYdyZq3QyVUgwhQL5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی تو این دو ویدیو به بد ترین شکل ممکن‌جواب‌صحبت‌های‌قلعه‌نویی رو داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26085" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRs_o67Nt2Z9-ldPqFopDdRpRWL1S2_zgPaKdZBfUSiddW_qytBbGiXw1RfJKlNMD2c5fmvwvBbBdkuU3bGjSmNAk686Bl-HNJMnWunBH2TWJZVlOs-2uwrzk-4vENjy8qb8P1wCsCDTMarI-rIqkuH1R8MCvTFNGAyCAShOOdkgcWSqIB386SB4P4s-qSHwbsWrF7bADbbs0p3qAlRyI4rviHj8zf8-GC7P7PYK7QwOI3ybHOYXMsGzdU4NzKR3InHAUzIaPzlv1yJj_GeORE9n3XgfJJdRjJ5SViZX0fFUqA3JCeo5ISkGOEW2JOz7_LXDUPKJAUSbi2k5cQR6ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=fjlbYLYIBAHAg1pbAnkR-SywpT4lSUOHRSlN_EUgDShTS_IFElubeHu4ExIgflVi7wHhVceWSoXjcPPhh9jVGRLUgngF9ZPJZjxE7DboxQw2eBfbHf9uDkgk5CJJ5Dd13mTYZYf9sc4fLNXPdI4-nPGsmpM0FC16BQutDuW4rHiJ0qUYMkNBGat5PPUPxKJsIwyJK_N5eXCeD5Koi0csTFsdUb5HOXSRt3d1DRkPgHTljkcvfPOoJ0OyajngoPIQPSq8BT2XhD7qtRmvoYMmTOvA0IOLNVBUmBPadl0iQ4ebkPzb7OIcP5j4A5ZaKCF4rr15-qm0Kxx9O1Nlpw45Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=fjlbYLYIBAHAg1pbAnkR-SywpT4lSUOHRSlN_EUgDShTS_IFElubeHu4ExIgflVi7wHhVceWSoXjcPPhh9jVGRLUgngF9ZPJZjxE7DboxQw2eBfbHf9uDkgk5CJJ5Dd13mTYZYf9sc4fLNXPdI4-nPGsmpM0FC16BQutDuW4rHiJ0qUYMkNBGat5PPUPxKJsIwyJK_N5eXCeD5Koi0csTFsdUb5HOXSRt3d1DRkPgHTljkcvfPOoJ0OyajngoPIQPSq8BT2XhD7qtRmvoYMmTOvA0IOLNVBUmBPadl0iQ4ebkPzb7OIcP5j4A5ZaKCF4rr15-qm0Kxx9O1Nlpw45Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqBF8bYCzYOnkCo2saCYG7ka_5Pt05IiRaZ-KFdDeSIG-LiAbyq7KUtI4z4BCuCqedyGxBVVdj4LN6T67bmHBmU_m_AzyQYR-XdnTjTQhz-ZpVIMGxPSFCVAsr6IavAiYe29P3KfBBzSOrf8cL1oVK8P8NSOWdRFnBF2aoRTbznXDPg7IjE-ZayPcemwSpRq4cSBSQmg-R6j2nKClzuBJmDg7QJ0jWVyxqNhHUaEx83Bn5DotqIEStpTTuKOTP0Tn5fYgGAfRB6Ft8Q3omO9_B53lR42mVKRDNtUApXLExhfSddAcFWu8c8dqBOJMoLDvHecCBmVZY-PoDSVxSH2_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWIRvCsyBWEyBdV15tNB1_rKRRMwrxTK_B8TUNn_Ys20aA3hIR7VMHkfMKxX5DY7-17c6OGgvp9zozXXmRz759I-ddu9Z-AmfU2D7dFecC_sR7R8V9p2Kqe6SNWJvgS6WjMhfZKI_qjCTMXCjdtlzyLSbou8N2fef49dRioRP9IgzVUkyQcjjO57jiJAbjkoDoUMcBaioOtDAotdlXEoBoiga3RAFCZOXRwF0T2KKoPbKMWFUOV88vVLSfDCt5j3lKYuXvVdtQ0HqnEqW3s87GDQDULUyVHJIt-khqCnsMuVod8AD18j6lpGnQ8c142JT1PCYqlyKVmfsPFT-9kv6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPstIxhurwtfjpT7kZckqDxBBW_RyQDRXYa5CRZa8IxfTIZ_b757mlxVKWHpUQWvVj1Nnjx51G8Qney81fPohPe7wzeCEbxu6iN8NhAxyYO6XMqZ5valGx-uqfIps47QAj0ZQvdjmzWtzEZXTI450RUaE0ZrRGyh0pAHa0hVrYL_7-TEe7utPuCFdvgrQc77e4BJErHeCKLJDtxb1rbO3mCgM-D519VyPM0vjgLrzQmJJ1Rm7AOTvb0bv6uY5SmO12pdW9jsroJj7DkuTGm3uON81-Nmc2Mtx9L5hlxyHrZ72EApO-5m_r7nYo-s4_8Y8zIDqejkqeZMxaQPHvxQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oA5tFKb0KOJy8i5mthEoxIIVzpk0PTXSSAN2CDW9eR2zUuq5F5FWQHg0FN0mGjfcs0hshIIpCoTXH3X27u7-zZvk_O9Pp9J3xRVW8IduEWmqiDGyCObADNj1Dcl2qaMxSG4PJ5f145VrftBWSj0FRkCz6HeTbegLovneYOi1WI5wOVldCkrkhxlPlzyrGEv1q3fJ6ZnbgGRQLwhcOayLz2wTfwAETYNDMc3pVcfmfI9rJrtqY58wdkHVs0wxYCnqCnaXSd-z9BtJY00rnXf2-4bn1C59x1PFbcOFoEBU0s7qs-7d6MRSgM_HlqCDm8Qbnuzsp84nig9LWWWTjfJqCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-j6xpuBIXKxCggz-wdZk2Ec2hORcj58fi3CCccyb_tELk2YMRPcVsoVLKIbHq9kx4Rdkm-gOMrv3thTHzQmYKsthHOck78yHhD1ukH8DhdmbAUgWFdq__ipY-BexkzAUKUSFzQ8xJuVeLHgKljYa7anwkNWlJld86P7AjqjdEUjawDNqyxZiGdVxh3o-vOscYU5O4MlKhn8QvuvVn2E0QafmUulwJcHFUKhJWC6caVsfPCogpyuv2MJRdti5v53fHQj5TiDihkyArIQgfN2i_QcAoz2OiJR0W8UGItN-ETbw2omsc8-Q8d71VnkVxG6DY_-JDgU_gvxG2_uViFmrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26075">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9-aoveErruiSITPsZ3sgpjTJ7QZlSN4S6K2CyXOO7kVQYvF8__r_vxDakhp0uAywJig494BCZGBhRQe2P02V7iBAtAFJqJJ-7u_MoY0_xbs5Ak8h-iF4xOdIrac2NW2oh4speQA7j-sZOs1IJbO1clubVjxQRPby4VfQPaCkKkXmCX9_T8xxg2C1Z9GkxYG8LdCkKb71A_-J0ChAkXz4Rtu7YT1d9MLfGUWWUV7c1otDgOgQ7HIqLBuUvhpUN33sf_UziAqh6kkNkzUZ644uMVVrA4UvIlphDoszF7N0D3WXv4bkrWsxYIIVHCcF3uCZSEnz_X3wnp5Z8vSk6p1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26075" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26074">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB-RVMTkA_b7DKOYOurRPVSaoSV5nIBNT9IuzygShUp5ZLgzt8KF2qFXQfSII2ke-UR8fOhl_W6Xrpl55hAooGJyi7FQ4_NV-V_Dh78oeYfG0-mq9wVfup7oE04-vf-ouF5nPKusU-s1J8y9knNODHZvR4-Wc1hRoCnMNgK6kv28_nX1KZCKLjMhC-58oQt_dtIG9OSnPJj0XtSzU4fXe2InXjmCpd1ZxDBWuoYjuMESSGk-0DE8g0NA7IUZ08qNZH499871qL7PrT-E7CGa89qqvuyicDG4hgzjXWnrhZxnqivFwZFlh2lNpnN-ieksDz84c95ar3Xo4aXNOFXnjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
علی دایی بهترین میانگین گل ملی در مقایسه با کریس‌رونالدو و لیونل‌مسی دو اسطوره فوتبال دنیا؛ بعضی رکوردها شکسته میشوند، اما بعضی از نام‌ها برای همیشه در تاریخ بشر به نیکی می‌مانند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26074" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26072">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzoP2wfwkSsvAZMV8BWlTK3OxXstux17yhVMi5s6YTMhynePvb6wDhW-wt69pjlpZg9Btw6MTHu10sOFKQjAV8Ca5N3vNkDTCkCbugL8H7ONoFTYPOrQyO-fElKKmAO9r_igKGuRoUu0WRNDz270goiogAtGWxHm90xCSNIJXjbTf2Ou_s_2477oLGrVSLW_cmuX7zXapLBNMFWleO9Ipp1PG2wrRDEyuWsioSZInl6d1D7HuRikh-JKcs-QGch_jGjAl3i0uRvJSIAXquXK_Y5w94b4wJD3mgcmXWBvqZMR7aXkv9wkloLTjwK69ppdUPHxsQAKe2ZroZ23_qUthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:
عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26072" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26071">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyXwjQdDXmxBsxKTfTd7VTaok1MpYL31qRQwgClTWQt1o6q0f4JO9EQMDLw1Q0GK1aG9HxNYZno8gJjNpHFB-UyxuIqr0KpyYM15pkO9ZcVIkHa_D3PMOJub57RyPrNQVdth5wtHr0gBN6igRBpok_Zd6mnKjIBGVq_BryyIJOWy_9wEYSgJS_kEMvBpb_oZvjw_X1maYuqEeLY8PKFfj2JxNJ8DJ-fPHdmNiGHK3VMDKgseEYmXnwvfrBHgJjpAm-_P8mlVvnP6xXKG1kEMeqhbAz5HKOgg44fyQ1xY5KmRbcmupx63sqKT84xeG7Ai6qjPpGridiE3sMO94n0g8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26071" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26069">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=mqDphaegN1Q4OFcPUDS-u89wbdQjEKo2ed1gHurWmbY1RaO1FSJ1qYQkVHSAOigQ1_b1FWrgB4Tw89InsSL42OExSP2K1auLYVXi6N0vzP5ie5r1R7Lhio6cfqGRlEo2PfNm4RRxwnMTiO4dVX5fgvZzP3PAFiCjeSmL48Tgxe1RdrHA9oTHS9_1VOxICPO0KK0dC61L5WHVUn6ywyy0hUXHwZt54nEVF20zXqW8zb_fX1B_KXSbr7Qa8H3b1EWJpW6bvaMD4VeLpfWVAnVN_l7x6MAySmFiI8sFs96DIj3NfeLP3GdfyOU_R0PPHN03V-BQNS270NHtE_DexougmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=mqDphaegN1Q4OFcPUDS-u89wbdQjEKo2ed1gHurWmbY1RaO1FSJ1qYQkVHSAOigQ1_b1FWrgB4Tw89InsSL42OExSP2K1auLYVXi6N0vzP5ie5r1R7Lhio6cfqGRlEo2PfNm4RRxwnMTiO4dVX5fgvZzP3PAFiCjeSmL48Tgxe1RdrHA9oTHS9_1VOxICPO0KK0dC61L5WHVUn6ywyy0hUXHwZt54nEVF20zXqW8zb_fX1B_KXSbr7Qa8H3b1EWJpW6bvaMD4VeLpfWVAnVN_l7x6MAySmFiI8sFs96DIj3NfeLP3GdfyOU_R0PPHN03V-BQNS270NHtE_DexougmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26069" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26068">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti5Ys_npEPXFzqG_JB9ZnjE9q41rrQDa5fEvIHO8flHbZH6aU5bkqkARgYpNBYZ5KwOra3y1KH7HPEuQQvcHYJjM9hWnRSqa2j0Veb4q043pwu0x8h2PEQ86ylfYZoeyaltHyvt_QqyBFD-XTAc6gBRzoxsglXqv6C9aL8oZb-0jt0hSVsbG8YwHQCUt8zZuzfDECK7oZJE-FTHgNLO-XbEnwzW3D1g_nooWJEq0hwqGA7_oQ-nwN0wJnOkrxoACVL6xAGNe6NKkFuLeDUbNnsNq74J7SjDXVH_QvdZscZ9D5Wg81M-4CDpmMf6Vxim01-IzYJP2vRFDcxhH-6AUEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در دو جام جهانی گذشته؛ تیمی که در مرحله حذفی با نتیجه ۲ - ۱ انگلیسی‌ها رو شکست داده در نهایت درفینال‌باخته. این اتفاق برای کرواسی ۲۰۱۸ و فرانسه (۲۰۲۲) افتاد. در این جام جهانی، آرژانتین در نیمه‌نهایی انگلیس رو با نتیجه ۲-۱ شکست داد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26068" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
