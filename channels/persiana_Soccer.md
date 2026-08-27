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
<img src="https://cdn4.telesco.pe/file/WSHzpSj7pqB5SVSmmF2bVr5-z6Mgrhu9PaCa4KS19uyC4FSUxEAg1LOzsCYx5wDBlIar74yQf70IPVqHA9LfwRKLCchaN3ta6Z3aNoWWMyi3o7csRKRi5t1qiuzuBJmjxKu7O1rP10MPCkVcuVn2T4bpbQQpV3HvhDbMWQN_Wj6Bl6ysnTLCWEcZUIOMmHZGdqpg7uyHiRp7TPvE4S_-2w6gtrQeLCH9RILi3IPuVy1MmSgHVMahskdzgNvWBzlirhd1D5nZJL7j5kY3E48KeG_CCDmI07k0cT7wgdJePZUz_Ej4R6pa09F09F3mxBAT-iQcIQKnO3lqAhg0Zy__OA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 641K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 20:40:41</div>
<hr>

<div class="tg-post" id="msg-28589">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016588e26c.mp4?token=RUv4a3aCf2LBS-AR0hM4hu32S9W9A25fSd5KLxki2iDInAfkNdyb7c0-kGH8ClBlTUOBKqZfLARvlm8g8LRsxOVBoE12WS1-ky5KmjsM9wQOG547JeMo3AW7TzGmzEDSvoXmvhylYI2lcH0Xyg_k4_bVfS2QpYZn37-E1kOoSOiOaNFEzpcxBSmqpGYFtsQJT8Wi47qwvulUIehIvn79EfXfRIjmgzsAZxWJ26iwWhful1vO6-SIS27FkdIhlnro6dBu24SshXrBDTQQn2JSQ3zLwfEBEDIBeLLOC7lH2eKaC8Yoy8Q92jnnrlLmMYxGr9omiZoWkf0h0HLTtayUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016588e26c.mp4?token=RUv4a3aCf2LBS-AR0hM4hu32S9W9A25fSd5KLxki2iDInAfkNdyb7c0-kGH8ClBlTUOBKqZfLARvlm8g8LRsxOVBoE12WS1-ky5KmjsM9wQOG547JeMo3AW7TzGmzEDSvoXmvhylYI2lcH0Xyg_k4_bVfS2QpYZn37-E1kOoSOiOaNFEzpcxBSmqpGYFtsQJT8Wi47qwvulUIehIvn79EfXfRIjmgzsAZxWJ26iwWhful1vO6-SIS27FkdIhlnro6dBu24SshXrBDTQQn2JSQ3zLwfEBEDIBeLLOC7lH2eKaC8Yoy8Q92jnnrlLmMYxGr9omiZoWkf0h0HLTtayUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های علیرضا منصوریان سرمربی الطلبه عراق باخبرنگان‌عراقی بعداز دیدار این هفته این تیم در لیگ‌ برتر عراق که با پیروزی تیمش همراه شد: 8 ماهه که هیچ دستمزدی از الطلبه دریافت نکرده‌ام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/28589" target="_blank">📅 20:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAYUhZQmm4qQ_Q8iGN9CD0nQpSSHxJDdpxXh9JTm2IzcSSKPHkseP51Yk_mKFzpmVEA8Zv1SqEWOitbux6h1zzay0Tsk20MCUYeFMipVl_Jf8-WF2lf44hc1tgBDKzG_pe3knneoK8xvzAx7Dhav-idbuo72WHpv6wDZNcvb6sbMPMXcrZqRMLlm_7ZP8kUye8vwPGQtqGXi7ciSRo0J4E9MgFaKxeIWlXCkCzxNVv06lD0NELS8k3HCiXErYKlyJawoea6O_ib1os3qwtUhEOTMvBhzbmRekCcdzvfH1B6k-Slz9Lgbfdk61_pPYAf9ah5BTPUCgV6xwTb4Ltgemg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
آرسنال و رئال مادرید درمرحله گروهی لیگ قهرمانان اروپا بهم‌خوردند؛ آرسنال‌تنها تیمیه که رئال مادرید درتاریخUCLاون رو نبرده است. برنامه کامل بازی هارو در پایان مراسم قرعه کشی میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/28588" target="_blank">📅 20:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28587">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoHnguWcfNw8d1dEAaRPHncb_N73ZT_YmNyTP8IWdMyauDKjZ-yJ-Fy4cl7-FlLInx01mAhzl7uQ5BtThJu9BthiUqnGUPl1B1VCqxKtQpye8iqcyy1otEFFUf0_T1GnlpkyMOoU_8COp5er_Sg2wzBCmizVIc_7KELOoMqOx9yHJkxFCyMLT8xUi1maOyDl0kbUQQFHqXNFqVN2-57qPsvfphYjitoYvQLq416EigZxx-r8CGi40_tLyj06rCAGaZXwVGgpEg0NqOK57s_kmSSZBHRupm3bECp5dWMtPF0In9CQeJTHWdkiARi_orQPx6QFFUOPtIHyMHs3sp4VFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سید بندی فصل جدید UCL مشخص شد؛ قرعه کشی مرحله‌گروهی‌هم امشب ساعت 20:30 برگزار میشه و مسابقات از اواخر هفته آینده شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/28587" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28586">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQWiFtZcueHreMpzc1Ip5BYrPs7gGoRjivRc3hXgskudZgpaoxoY8JWspMooEaHQKOkQ--7b6zIIQP9bf4kwDrLLntUBMMdFA4ZBpCp2Fjf4wjBrRbXc9DoYecnGq2VgABkioixXcRbJGKqa4ymbwTZKsbuHiItofnoEjtivMontataOW_9el5LViy7svISjZEJSdZtuVdTiTyWKgvpA1i7EY1QzJ9S0z-YI9PXC5-sOU2rlM-8ay-6yt3BWIHljhmKgi_um2swVYAU5NTHx_GuE82jKFZBnCc4pYHxM9g5Ab-3IazNdGfpg6H3uzuuHgkT9Iob59Z8A_4BR2yUbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پیمان‌حدادی‌مدیرعامل پرسپولیس؛ پرونده نقل و انتقالات سرخپوشان در این پنجره بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/28586" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28585">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry5jK_sFiv3ycjltH9v7ufowszfe8P_k3kxEBBYP5OgXVfwzyM5uZGueJ0LEZFUAQpYv29GcvP2cEl-AFAI1JntXYYaWigI6TL4LZZda9E8Q2YMvGYcWD9xBhVGmpG4fAb-NGBgY3MAZb7YySA_3c2Iy00MwMus2To-maOkgQGwtq9WD7Npgi5f6_q1Qtlqc5d2VGfUGURo1Gkv1i6YeroUVBn54qwhzDqQidEiCnbM8BUmvTlnM_CtZ4EYrGpU6Z2Nz1j38vIRoVohkjI6i_IZzNE_zw8BTN28VuC7XlnwLyBJa2aLYCsCczRZwIF23l5sx2_oqdSce50ApOpln2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانقیمت ترین بازیکنان آزاد ایرانی در ترانسفر مارکت که تا به این لحظه به تیمی قرارداد نبسته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/28585" target="_blank">📅 19:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28584">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nST7ms-ITcXgO0wnL7exLWG7S6hjOH0yViuVIyPoPpULAumwSyVTLhPKM3-5fDSckLhWyQvETQOqm9qaFlEHpGCqnmEY5FFJXBWDerREGIocoHxKwTGFRa7Hd2GaIp4puhZrqP9xWqR9362FtUcEFtc80IIbWobxJE6d7wI6_UKe38qLb4ogK5K4US6CYjq-jR_XbmOGhg_Q-4NnzmvQr4pfCtXEkbUrylWgismgo-DN6jSjCcLuiAhp0l2DqU7EicAxlu2Ist2L16NOBeGNRnyrejBdwiCkTsP8uYs9DZrO4gwmI9TvvWFtTj-LRAUfNEsVvmK64pzSae2tlr4vMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ علیرضا بیرانوند دروازه‌بان‌تراکتور رایزنی‌های‌خود را با نهادهای ذیربط برای تمدید معافیت‌تحصیلی او به مدت دو سال دیگر آغاز کرده و پالس مثبت هم نشون دادند و به احتمال زیاد بیرانوند شهریوربه‌سربازی‌نخواهدرفت. سهرابیان نیز به همین…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/28584" target="_blank">📅 18:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28583">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTC8_E7oR-UdF4Epie-KGWDolv1U8jkiXXHB3TKILdk414CuOeCOiNufgRgH337-XLWjb5hZ71D5AS2SNPFpW3txFmJxyLldhtfr9_cu0T8OJL3yP3wkRs3Q6S-36OGNUaB9GhgWrCiSN43JlysHwN11FzZF5yJFR41VpO_Pc76yvwlrKe_EXgnS2rTNwpHis-4zZBek70j6M8DibOyQQ4pwlcN8-9D3E7gjuJjP61o82qu5Ssgyw5ukYVaqFAzy9kQZFKTpLD-pFHBKm_eLrH_Zws7MkAuo0QjupQlUZAQ97i9yOSyOx2u5xZt7TZB7MO4SvuWxqBJQtgwQHAho2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇬
با اعلام رومانو؛ عمر مرموش ستاره مصری 27 ساله منچستر سیتی با عقد قرار دادی چهار ساله به‌تیم‌تاتنهام پیوست‌. این یازدهمین ستاره من سیتی بود که بعد از جدایی پپ از سیتی جدا شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/28583" target="_blank">📅 17:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28582">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dsu-qjBud8-sOYP2UyijEe9jK8E-PFXb6_0MXrAtvk8rCU5kefLaKqr8Z6ErFR7BKAQ58XothK0b0FPi0-PAaLILHqGovPZmue0-ijH8260HkcFSk9QJpVnP2uW1lz4IZtdZtrTalwJ5LHZ4F5e8m0bZ1pJbbQJGFwmG5H7Ty8Ar6vLmPDTDa2-LptksDEPChtvia9-vDH69h51brGuMBFieA-4Pfqk_CzC5-HV_zUX6X9m2mIwLVHPMLqIfQGZwzZcyD4qnTArmMoh2cFaZwCN1GcWp8-h_P1JsWvzBEuJyEg14sfHLoTNVeD20ll14iH7YtwKOzK1QT5hy7IFp9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
#اختصاصی_پرشیانا #فوری؛ باشگاه آلومینیوم اراک رقم‌رضایت‌نامه مهدی‌مهدوی مدافع‌راست جوان خود را 300 هزار دلار اعلام کرد. باشگاه پرسپولیس طی روز های گذشته با ارسال نامه ای به این مدیران باشگاه خواستار جذب این مدافع راست شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/28582" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28581">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c66lvqwC8cak9LIPf7c79oxS8xoznuFPTACSmmGdEDh4YMr3Ea2AYIdXPAotRucwW9C9UciqW5U4J2zimXAfNP0orUBPlFjDkEAPMi0KAQ29xV7JHYqcZ_uw_Mso7FPLZYPOGraigKeCuQOtJ_2eR41CM06jqKK60rHQywbQyu1ExnBdQZk7-aPLGQu6P6Te2WjodzgUYlWCSX4yYjuKxPT5nAYYCY947FxGtk0UmsxCAuA6AGbK626aWKmgJ4BXOydJuwSTOc3rmc5g30YmKD8yIvb-x7Cu_VyFTOESTvREBBCopIAx85d1M9AZQNWc-WL5LnQuHG3gI1e7FxFlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
⚽️
🤩
#تکمیلی؛ همچون روز گذشته؛ خولیان آلوارز در تمرین امروز اتلتیکو مادرید شرکت نخواهد کرد. آلوارز میخواد سران اتلتیکو رو تحت فشار قرار بده تا با پیوستن او به بارسلونا موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/28581" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28580">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAOILHjCn8LkXoouW_0_c_L6owpB5OCcNDxc_wzloHgqUMim7sRRlGupo4T6uclGoOpJz-opeySAiLPLLQEemlKQMznarszTpmhA2ME2-Y3ZW6uTtR-RtSopFrkhSgWSHiVcXDvSVGHmVBBmi22x9v3_OZUjVd-OJ2paf5eIl8rx9DX2KvVdYMrqqxf8IwPDrN3kPARGNdYG8gZw-wdPYjILRu-5W_AYho-bFvmZ9pS8JUHYrQR0atkBHIk5_haML_Y3zyVcFATUFeRLU2S19xv7DMmagTEzGqaObimoLxK74SvanMpYtJRCjr0Va1GA0MYcQqqw1xS5jqv3FlPgMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
جام اتحادیه انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی
🆚
لوتون تاون
🏴
⏰
ساعت ۲۲:۰۰
🔴
بیش از ۲۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ شرط رایگان بر روی اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7=</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/28580" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28579">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odMgJCnKR_mdJjorNla1mlAOfMb77W0x6ibP532vI9KMpuuzMeEHSoG9VIMLR-7EmJeHzDCMcvupcCK2DyCthfB81qGMmct7JJabqHkUF8lw5c4gimYgCobgTVH_yLIB_3k6j8V3AJl74_LbonjT7yiADwTrrjIvy09d3jUaZWJ3UJWrk5zDRgYyc1Iv7HhdAxwNePzXqtC5gec_2dlF16sDpQQvb40Hl7nSecgMWQsizLyOW_k9ORIMeJ2BMUQoAtHC-BIapRYYAqYf5NWA7G9dJArZLvQciB0H354zJvefiEOef9p8rj5cEC0pVOfJhiKmM-Pc-8PY5mMJ27lTTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تاییدشد؛ بااعلام باشگاه نساجی؛ کوروش اژدهاکش وینگر18ساله تیم پرسپولیس با قراردادی قرضی به این تیم پیوست. همچنین یعقوب براجعه مدافع راست جوان سرخ‌ ها نیز با قراردادی قرضی به‌همراه بند خرید قطعی به نساجی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/28579" target="_blank">📅 16:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28578">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MENZoSyVQgiTmJE8yP8nNBpwLPdviQtppa8ltLasfIcAu70dft92_UVJeR5hQmO9XiHllXerAkYS6WgQm0CohIPEROcjoMAJKr-1QnI17GgCwq2zHWXm4LFa8vqDJtdnf-3OP7ZwLmym74rWIVl_As223GBXzftRTlTQTCJ_TfdoAcGKIxLbucT9_1X7XGEXskr2WEpDtmCm8cYqG8eXUSBIovCxQdwTnypAU5HOarMVoRHBvJaLxDPYXZC8RqnpUNfVHfP6LqCxN2qopFAb5V-Vt8P2T8iHy-aYWx7NoYUa9dF0dq5W_9SIhNkOfktTnwqNJLnmd-8fEypssAVkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات:
پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/28578" target="_blank">📅 15:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28576">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oufxqEOv6f9pjGeKtdxhUpACgzRUtjGDl32yA07BUWL9EUFdMPnexPXb2w7euG0K375fqmXMTOGv0kfPJmFjs3vXBiQuQgvNZ9aUlqmQ1Jov9VWl0odkfWwz5JJ9NAnjrNmppW8LTqAzZuLmmhSicReTRb3A58B-eP6lMnOd0UswR1n3ajKfnV3-Gt1ToBIRFx1qo920KAhaSg-csTu64rkrMVJufU41FiP9feD30DAALBDRvXS73fziz_3XEzqbINKQZl8tv3lhwZzQq9U0FF0Qh_Qf3AWxBXTHy-je6_B6YxozButwfR9ylbeh6mmn6hT_75qm2YB1y872_Q2T3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اوستون اورونوف که گفته مصدومیت جدی نیست و مشکلی برای همراهی سرخ‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/28576" target="_blank">📅 15:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28575">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVp4Ih-_sA4NIWF5GjEzXQvXtdRecjIammqc0Jjs7WrhhaKqlxKF0LJaPJsDxZQpJq8cQw6ztXZJXAryHK5Cdu5X_aGuAEB7FSuJk70SYIqVlatEHIn_BV2viPHLBGgvLHKhCXfalZOX5rybT09RhbquPL6Ylv0j1xmz6eWcCZ9Ty9v_exjhuWCcTSmpke_fDtaHP3heAS7XLF1tjarM3U83zyfq5hvgUevZ6Y-AR9PAKdEoNn4HOFNP4ibcHKaSsJYpxOWXnG1T4kDWamJcTMt1x8gSCaMBsYM06pBxfj3XF6kqF2FENCBfhAtAGXiUpaFRRrW2OMNCNWHguhWhEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/28575" target="_blank">📅 15:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28574">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22cb4cd7d4.mp4?token=sg48RpIqPpdy2dL7Mj0qXN0uwzFVlAF8bNTF30dlPEDQ-1VREmB2chZxPVL3pNLRuAPGyg96U29mNOwv16jbRtRXlKVDSjxvq4D4LDt1q3Mc3fbI4yqx6yUBRuYzec9JxL4J8NqCelh7yFtejkRY0A5PO7ZtlWuMO10HKhGw_f7vny4qCMJr5v2kymAUX_RMRkgTZwruif3Gaxj5kxl4unugkB250hmRB54gIoMgM_OKA9fVE7lu9lwTDaNJ5mfmJ6Em8R-XjvcXLb-LrJqMtOsNnREqRiq8Zk2Y4tOHd3kg0CLyItH-nncEPbIqIPOXji00Y9ceYTS0v1v5X8RQtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22cb4cd7d4.mp4?token=sg48RpIqPpdy2dL7Mj0qXN0uwzFVlAF8bNTF30dlPEDQ-1VREmB2chZxPVL3pNLRuAPGyg96U29mNOwv16jbRtRXlKVDSjxvq4D4LDt1q3Mc3fbI4yqx6yUBRuYzec9JxL4J8NqCelh7yFtejkRY0A5PO7ZtlWuMO10HKhGw_f7vny4qCMJr5v2kymAUX_RMRkgTZwruif3Gaxj5kxl4unugkB250hmRB54gIoMgM_OKA9fVE7lu9lwTDaNJ5mfmJ6Em8R-XjvcXLb-LrJqMtOsNnREqRiq8Zk2Y4tOHd3kg0CLyItH-nncEPbIqIPOXji00Y9ceYTS0v1v5X8RQtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
خبرنگار در پایان دیدار با سوسیداد:
امباپه میتونه به رکورد ۶۰ گل رونالدو در رئال مادرید تحت هدایت تو برسه؟⁣ ژوزه مورینیو: من چهل گل با جام قهرمانی رو به ۶۰ تا گل بدون جام ترجیح میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/28574" target="_blank">📅 14:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28573">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XchnbTvXTYoB0kCW5nyoMAqF0GN21ESWX59A4FEOLwAWf6-yPEQRqO3gTpNNL-FzWJNY-cMnH2QSz0ip6tHLtmY56VhPWyaoIBVhAanqfJwCbQH9PGnp7uu9lw7jtrbm-I3HIuFaJjMga6mwQejBw5h6Kh8NsyMI0mWxqM73R6XCtHMBQ7LzGqwz8-T0JqNO-uMxcHcC4xilzAP6-JUneexnuwL0z3hg-2LhI2NQ8FhZWFdK-Md0JgBB6N1rLgGPgHWhulB4X2ddW3yWIf8SAvF6BCpfoWRqwOLSu9Iolv4ITUEU0CbCjK-U2uhO2iWupApq5f6H5GazLOp0B826gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زنی باطرح‌شکایتی مدعی‌شد که توسط سرایدار منچستریونایتد در دهه ۸۰ میلادی مورد تجاوز قرار گرفته. این سرایدار در سال ۲۰۰۹ فوت شده و شاکی به تازگی شکایت خود را ارائه کرده. باشگاه منچستر با اعلام اینکه این موضوع ارتباطی به باشگاه ندارد و طی این ۴۰ سال اطلاعی از آن نداشته، بمنظور عدم مزاحمت این زن برای خانواده متوفی مبلغی را جهت جلب رضایت وی پرداخت کرد و پرونده بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/28573" target="_blank">📅 14:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28572">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVZXBHjN-GhGJk-QxdZvEFXg8dRv9kvfdAh-jgcEmt9vwVk7Omz1oK5aqtMWHI8SSV2B2K4D0d8OtWOmsSo42qRkARjlgF3hTAePvkK-9LODkufAUew4l_HjJcsQVYgN4kMgvIlNkPIz8LUfZRZPS6VPS7gq50abq2nza7DzEJpr3t8q1dJnyeRWuURvaxRslF31k8fDdXTGlS0LlhYA6Q0_kQq5F_G9dYHuJrMvMVtceaJgZcrau7FwHmFUvSrHMjzLpsmnGMoG-UUzPY0tBsy6NKZ2yaUSODZF2pyt90e00Wq26bps5Lg7RN0HO77Xicg4yrSdK3bR8EZ6-A4zeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
از سری اتفاقاتی که فقط واسه تیمای ایرانی رخ میده: استقلال قراره تو هفته اول لیگ نخبگان تو ورزشگاه السد میزبان خود باشگاه السد باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28572" target="_blank">📅 13:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28570">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIRMan7XSTT59p1ZdS7aNxe9dXN30qqWqJRwcnf9VqbJRy_G35PE7LdJ-4Fn9wRWwH_Ajeu-i_98MalouTij01i1mJEyZT6YwQnqgPc5KStA8c4_Qh-fGrhlx6n4STepjJVbYiXZ9NL7nw2IJmiXe32so88Q40bgxhJKJgENl-Ax5BmzLtjp23RqjtL9VVpb8RbBLdCoJ_W1hF5n7kgBgZJdoTruB8NEjto2jZ8cCTQZDMYejPn0KB7jmGWteQa9nB9nQ5V4CSv2incv7lf8ORIG42iLQnJPS-wrtJeSZUsjZggQ-AndWNMG3NrfN6sjLrRBFnj-R7ZX-vfKd8mXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/geRkUXAOvhgyFsPgFprG2DnSHVyN68gAW78bMTRA4Xs96Vicr5NR0Un1OJaJrPvubFNW9y3Rz_jDRaHTh7L1Wcz8q4obT8ATzuwRfUb21NROII49d04F1UEYk9O7XTDnW4aTtVsaqwvLnDLVcQGs8bjZexKxt9O_dNuSL31-0489LVN1NDAMBEjkMabM-7cbB0hrByfFrY_FwW68uh3aEvYTu30h888CxUVexHr1DeWnxQipnM7hM0WOEjgE63LBZNjEhgm-pztlDlkRp8fJK8GlStSJwHZQ1r-2bVO-tzY_36mfXMuZB3Nq9bHGoGhvZsDeioInODGTqOU4YwvReA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
باشگاه میلان بعد انکونکو؛
ساموئل ریچی ستاره جوان خود را با قراردادی قرضی تا پایان فصل به کومو داد. ایجنت ریچی پارتنرشه که خبرنگار شبکه ایتالیایی DAZN نیز هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28570" target="_blank">📅 12:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28569">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMBLXVl-r7QZVPNpjoMgMVr8JauDM7Hh4rhwf6rnCLlH_z5_MSBMQCCzSmma_uen-IXdJ0Y1Uo6hjNJemzGNdPka5V7NsQTZBBUFwqBCMFNnIA6gcwRrayv6mVPuuubcIm4x-BTt2wCM3GJ1NQ95U_-pIoQ0YulGbkGb6NvCMaRRHDZiD2623PQyqKoDM2sYORGVbCs2B3_hqv-4kt96X2yiAHKkIPeJ5LHdHs6OXvXIGXUsi4WvDcRVNxYr7nZ6aAhNiAySG4StOIn0edKgi9AEhJseHU6yQcMdNuz7n1dw_NsNuc10ze93Az6f0s_1xR_dJmzMKJ6bs6oPw9aAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتلاش‌پزشکان‌باشگاه‌ استقلال؛ روزبه چشمی و جلال الدین ماشاریپوف درلیست بازیکنان استقلال برای دیدار فردا مقابل مس شهر بابک قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28569" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28568">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b570a2c1a4.mp4?token=bhvgevVE9RbCebdCL0eQ9ESGMDBfcVJbem91O55WS4MdVQVkZKfrD_ryg_21GIaR680pVVjUlSykGdp8Cmh5NVUoKQ6CqOtDJnXLQ3D0TZZehoLwPxg-yQQMuL5iMuaaTHVgvgJ_-wbQNsIQcyU9Aqe4PWr1PE1LnGDZ-Ykg2j9EvRSQMA-OiB13xZMh707NRdp537OgIagqfmwUZKAKIjWtG8zECYHIPwEudEUl_s9GoyB5M70wH6UeBLxmZ-WqVXG31NIOGD5ygKpDZK6_qHyl_ccP1OLJAXqjYVtfgWPbXFwKQm56-XQJuung_VKdCfJBQaKqGsjGja_us9VLk0GgKYQLgbviZm4mkvsxi8qTpgKNVX33HD2YEnGod4hPvdDaZg-w1ZFXeM5HBKiytqsDE-_-_goVEcRfyVUJVjt5TF_x9yAsd5YsrMrLnt6t0CPv9ZhUkUioT8Bly2zKdMMrT8Zc5QDPNc7M0EoM9JZpwyyy5DHlBHW9KGhOc9MrmRmAsRvmpk5C2t2vl6VLH1n8e059aUVTsUlMqSzFqjfaN5suhzpxIBy9Tj5iywtQy0HRavJrYdTEH0sdW3HoSj69ofMx6TQ5zWPZEFyM9xYR5HVHNV9UplaNXvGBxTlZVQRE84I5nAtPvf0LFt427EoSXoc4CJ0V9zzjVRm5WuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b570a2c1a4.mp4?token=bhvgevVE9RbCebdCL0eQ9ESGMDBfcVJbem91O55WS4MdVQVkZKfrD_ryg_21GIaR680pVVjUlSykGdp8Cmh5NVUoKQ6CqOtDJnXLQ3D0TZZehoLwPxg-yQQMuL5iMuaaTHVgvgJ_-wbQNsIQcyU9Aqe4PWr1PE1LnGDZ-Ykg2j9EvRSQMA-OiB13xZMh707NRdp537OgIagqfmwUZKAKIjWtG8zECYHIPwEudEUl_s9GoyB5M70wH6UeBLxmZ-WqVXG31NIOGD5ygKpDZK6_qHyl_ccP1OLJAXqjYVtfgWPbXFwKQm56-XQJuung_VKdCfJBQaKqGsjGja_us9VLk0GgKYQLgbviZm4mkvsxi8qTpgKNVX33HD2YEnGod4hPvdDaZg-w1ZFXeM5HBKiytqsDE-_-_goVEcRfyVUJVjt5TF_x9yAsd5YsrMrLnt6t0CPv9ZhUkUioT8Bly2zKdMMrT8Zc5QDPNc7M0EoM9JZpwyyy5DHlBHW9KGhOc9MrmRmAsRvmpk5C2t2vl6VLH1n8e059aUVTsUlMqSzFqjfaN5suhzpxIBy9Tj5iywtQy0HRavJrYdTEH0sdW3HoSj69ofMx6TQ5zWPZEFyM9xYR5HVHNV9UplaNXvGBxTlZVQRE84I5nAtPvf0LFt427EoSXoc4CJ0V9zzjVRm5WuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب گندوزی بازیکنی که قبلا مارسی بود در جریان بازی‌فنرباغچه و لیون‌حسابی رومخ هوادارای لیون رفت از زمان گرم کردن که فاک نشون میداد تا بعدازسوت‌پایان که اونجوری خوشحالی کرد و دیگه کار به دو سه پارت دعوای سفت و سخت رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28568" target="_blank">📅 11:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28567">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u53EVKJo-lyT4TltcXHLFU0XNm7VE05rPV20QX4-X0rKO_Xt1yEP8roJIvN1mM2ZVuoFrNTUCX0JuAzI3bLxb0S8AKj-iKrgOv9XJjPWmYXuDEp8Un4HqCPLEYl2Y_aOERoDYxdYHZQtKVZ0C2uRPSxEEytBNgUJv_1vpUPXkIshoEOCPETfEvECNTidkseXXaX_v4MMCptzdOtura8PpAn9ZwgrJRFL8zs7TMT_pi8NDoLiZAOY1KnA871fdqEdGdQdCb2-_ae5fOBUjIWZHbk4xBwtSJzq-OSMKQp48RAzUF40llkisb4bizFLRBAcVsei7EJ0UWqU807kbDLeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/28567" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28566">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJnSVoSXAE7V46EpnD6NQsgJQOSozbCLL5ttv6Kyf8DhPnKFxtDzX-bKQ-F2frVF_2b_ZY-rxVE5zLCeKew50HZgbrsc91ivg3MtD5jeKDmqSeNRhvHGfD-snT79QgfAX29Hv0G_NvGZo08qpQUu1LB1az28c2Gacyntqni3Mv6yvNq_YxoJ4KJzmZNavSGF3riZgWumuZ2vjXISIfeHGHrr9zYTyMsScBNT5qYY50wGCdSz8ljXLJry7pEHcN2-s9OJ_t0rvcku5rXVdEnNDmzD0RCLiuRnEdt0p3D6o_cBqmK5KIOAo6k3ZXuZYEpy3jvrG_DIANc8Xf6NwUdHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛بردلی‌بارکولاستاره‌فرانسوی PSG در آستانه پیوستن به لیورپول قرار گرفته. توافقات شخصی بین او و باشگاه لیورپول انجام شده است. بارکولا گفته‌که‌نمیخوام PSG بمونم سران پاری‌سن ژرمن هم گفتن لیورپول 140 میلیون یورو بده بند فسخ قراردادت رو فعال میکنه. لیورپول…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/28566" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28565">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDg_cuwJHC2gzElGh1ja6ZMgPg9j2XUnyfJTOxDP5FJi4e58FmlnFOB3rMRczQP_goINe8y800o3OXAEWKF2NWc0YtIg7mT2jxSmMF_j5CH9HFmQdpAi5WDE4d6DVBMRP8ocfRw8eKEzv8sXg6vd9zX6FzAKsMiW6W12y0nDIIE9RJ5QAFPCLOxfS2RAmF6xc1-B234JCXYrid8sFIUZDHb2eG8oIed5Swhdjyrq3O5zPnrGoZw-h8Dm-VAJm_wP5gsQf0GJwgDWQyF9Ae7JCDxzdn0ayDJCWj_G_2JtQbVFQOgC6FoJcStgjOs81MIEWjbmx0q4sLkhITRFIJ4zwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28565" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28564">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇪🇸
🤩
با اعلام رومانو؛ هکتور فورت ستاره جوان بارسا به دلیل زندگی در اسپانیا آفر دورتموند رو رد کرد و با عقد قراردادی به رئال سوسیداد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/28564" target="_blank">📅 10:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28563">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed9d6f5b21.mp4?token=ikUr6_x0pFPzyFlXm19h3264F1Ake3LsZzJMtlJMGIniN69EtYREAgVY5bbc4IYkZqjWgrX6SgqKPvVB9ypRfED0dH4A7CKaFEYsaVPtMTYakzC1qMTkQ93VOaYiT_XDxWmmQsaeNKdFzHHNGquWKmkkmmsTJzrwMqlKSN54kTFg6-f6uUrUOItZmIOpQY6o0YErZHP6c1PcwhbPOtxncPMzeVRuc_KhcEO6fxhrHhiqjuR5Yw3Y-JkbuMMyUCfVGnmq8RnmvxV2-mNCHieoB0gR35YPcA8jLpI3ZtVpTpQ9pPuamUC87LL0TGtEVdf-PGgIQgE0mTf2wMDqv0QwlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed9d6f5b21.mp4?token=ikUr6_x0pFPzyFlXm19h3264F1Ake3LsZzJMtlJMGIniN69EtYREAgVY5bbc4IYkZqjWgrX6SgqKPvVB9ypRfED0dH4A7CKaFEYsaVPtMTYakzC1qMTkQ93VOaYiT_XDxWmmQsaeNKdFzHHNGquWKmkkmmsTJzrwMqlKSN54kTFg6-f6uUrUOItZmIOpQY6o0YErZHP6c1PcwhbPOtxncPMzeVRuc_KhcEO6fxhrHhiqjuR5Yw3Y-JkbuMMyUCfVGnmq8RnmvxV2-mNCHieoB0gR35YPcA8jLpI3ZtVpTpQ9pPuamUC87LL0TGtEVdf-PGgIQgE0mTf2wMDqv0QwlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند حرکت فوق العاده خفن و البته ساده حین ورزش کردن برای درآوردن سیکس پک‌های شکمتون درکناریک‌رژیم درست به قطع کردن قند مصنوعی و مصرف کم روغن در برنامه غذاییتون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28563" target="_blank">📅 10:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28562">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
این تیکه‌های فان داداشمون به امیر قلعه نویی و مهدی طارمی مهاجم تیم ملی عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28562" target="_blank">📅 10:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28561">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQCYzt9Ehq8so-VudfZyUBoweWPxlOBPo3nJRw3kBRVjiqz0hCDAIE1UVs1R6yPOmSBUPiayJMMWRgHZ81Fx8YtsZuMQ7fzsvR7aoCiVnyKHyHYZhn4G043SHHzkSnzgiODrg1yHcsFA4jWn6JwkO70QnC956v4w0P2ZOfR4fBKJ_mlncsuoJvqk1AB7orFY0AOFDcbkDLkH0Cwps-U8b8hUcuCwAfCOBMy_XU5Q3FRt8Q7LsVxhptnbd-BJl5x94fvM8G4hfXk2reOi55VndCXsGkdyPwqTf4XOpA_Jr7ynkXghLBu6_7XKzCJc3e6dzuIqx0k1jbHJTpV2gWvNhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شاگردان مورینیو در هفته دوم لالیگا با درخشش وهتریک امباپه چهار بر یک از سد سوسیداد گذشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/28561" target="_blank">📅 09:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28560">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn_ouAP5_lfoBCi_H3HHqJNt42TPg2w9rMpsLyzG4Or5D9ytntoR1AD8Ade_cxBEhvYSU0tMyhW_87jBY6L4DEXNaH63k1q759JVAxL2RkOAqmEnHGlkRFI3neis_XXSvdAZIojaIhavLqKe7lU7l0VnBWVOOnQwz7dC_ZLL1v2UsJYz-hNcoRmEf0dURaY_YTwh9LaALHtBcGo8NSrCjeuPnhDVWwqVfIqs0Ua8eFHe5GnDcDCF_wBVQ6qjpEY7l1JeYH50s94CoJ8iULDiPLUj28bEOI3CswtehHmEWGReQXHG5ZwLZOO0JmCk4JFAQ7PpnyHw3myumzProBNJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تاتنهام‌امروز100 میلیون یورو به باشگاه‌منچسترسیتی‌پرداخت‌کرد و از ساوینیو ستاره 26 ساله برزیلی جدید خود رونمایی کرد؛ سیتیزن ها دراین پنجره 12 بازیکن خود رو فروختند که بیش از 400 میلیون‌یورو سودخالص کردند. الان هم میخواد حدود 140 میلیون به…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/28560" target="_blank">📅 09:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28559">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM5MBST3iUJNz9Z6YNlSgdknpaxEL_iurgrQsHujR4Sl2exWKFbWvSNHbd4NYYoFvyrSiMJU9GbAHjKxKPczthG4_l-auV02mR_Arazk0Vq16lxw0iBCxWc1Zxk6PT7G0zWI6fy2GO--IRpwmdUJNf6AD4Z_JZOEZKle0EmZGXHcH2Skulw_KlS-l7bigKiHp6uvKuKqybNyiN4qOLPNXmYcLhVyhtTMW7d-zhKQGQzPONTQGVMCFejocPTUGhtGv_zGy2SWz1yfqbT3HtmzVTjAWB8l-dQ9Ygq01qe67i5C0tDD9ScRMAU9xQbtXn-aek_l6_fmIGAguxyWGHR_iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛سال2021درچنین‌روزی؛
کریس رونالدو فوق ستاره پرتغالی سابق رئال مادرید و یوونتوس با عقد قراردادی دو ساله به منچستریونایتد بازگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28559" target="_blank">📅 09:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28557">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxGm45GIUZTR_m2vJba4-oJdk-pKmPKIrEeYjTfHVrLaYcEw2ao5oSmft5s1BhgQ-iRJQSNBTeTM-rxpT6Qd85Zx-OUr_8HCdzHwoHNs8QDkQ_5UgYMtfrh6J6e4QP62ChzG6J5u3xSsggfTMSBI77q8BKR2sptylT-VFg8R-yFrZmM97g6AuqoyA1VSr3LMNbklQRbSuUQ9sqggi0IZQCHZChl1_Mi4628SMFFcBzgFn7JJu6aM5WCblp6_bFuB4UQjSS-6uSOAZaBRgg3fk-T1bK-U-5KeW4pZiin5LtfU_AWyHC5Y8iXqrwSE5u5MszGqf--Y9FRmTSQn9fAwiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌‌امروز؛
دوئل‌جذاب‌تیم‌های هانسی فلیک و ادین‌ترزیچ این‌بار درلالیگاواستادیوم نیوکمپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28557" target="_blank">📅 01:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28556">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8xHG5_0n4gfgfMDFD6qw-8WVbisqoPxKvXkkpweYz17f1d2AyoPKiybLJfHCaWGOL0KTRAEIJqFGnT65Bqw0ogZ1x19t5FvFVIWnFqwabFU7We0fCZiQl1qBwsRujvI7_rtjrGPsQF2ESNvRjCbnr7tYBb_UkgGY0dBUbGjLr3YZjg292xsKf1xStiZXWfjXSm57T9IAjbmwpSxr4Zhza2N2OsFLKaeA8YnEAeJJasnT7BYZqwnWImOr6Gn3sNKcWvobny7inLsqBpulOT4ObpHRP-63eMmXpPG_N5dXbyUt69JMro6l02JdNjWRLEdQJep13u-PO4Py0BPHFmonQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
از برد رئالی‌ها با هتریک امباپه تا صعود یاران کارتال به دور گروهی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28556" target="_blank">📅 01:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28555">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b5eee892.mp4?token=PmhWYhgquqIrp8tANnHWF27qhT0j5iAHFjJAvUKNBAmP2kWmZt77JesCpMkFSf28YtjSVuqPJcAKC9m6AtA_uq7XKrRJhrUsiW2zSB3rD8Ax3PrCEenDo7bqflAx-oTXaM35AUr9snmtZsV5-C_AWTxbHXgXJqIYqngzLB3dmG3t2e32icHzhZJD_WtJaukUkwV-6KLYHH0vhGIBqjEqTR5EsF8FwJZTL6zUN3Ee-Blg8ScD1dIBTDQztQBtVpPhsyoHESwGBwQTRzh0duRuf14iXRICOfwLhJfUVOUQXlM0e4NqD6Bxy0RbLaY7T8MgriL19IvTurqulTT1F7padA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b5eee892.mp4?token=PmhWYhgquqIrp8tANnHWF27qhT0j5iAHFjJAvUKNBAmP2kWmZt77JesCpMkFSf28YtjSVuqPJcAKC9m6AtA_uq7XKrRJhrUsiW2zSB3rD8Ax3PrCEenDo7bqflAx-oTXaM35AUr9snmtZsV5-C_AWTxbHXgXJqIYqngzLB3dmG3t2e32icHzhZJD_WtJaukUkwV-6KLYHH0vhGIBqjEqTR5EsF8FwJZTL6zUN3Ee-Blg8ScD1dIBTDQztQBtVpPhsyoHESwGBwQTRzh0duRuf14iXRICOfwLhJfUVOUQXlM0e4NqD6Bxy0RbLaY7T8MgriL19IvTurqulTT1F7padA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#هشدار
؛این‌ویدیوکوتاه‌از صحبت‌های مهم دکتر علی کرمی مدیرآزمایشگاه‌کنترل کیفیت مواد غذایی ببینید درباره مصرف آب معدنی برگاتون میریزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28555" target="_blank">📅 01:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28554">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-U-Yt6kjYIa4y7KdpkTAlfV9zlPznzSO59Xo4n3R635xr2wvUqywj-dcsfmTUrS_uuxTINAxh0hgpJopHeoD73eBtToZNeMd91pDEBg0jP1MeyR0o07PxIawMj3i0TKQgfzhxbZnG3P3p7Mc0KLpAOwP18JTSFh3xIM5T0g871tBrpRJmCXIhOxe_KiFqQ8e3lo0DhQZY7dBAWnFLTg36Belnv4f6VaxVsDhx4HuNuCwgPZxveOgGFk4x1jgdvmtbxpC95f6CX6wYQMW8SfQjJxpfkURBg_jNRvUzae3kBxXujrrHRMRGpu0j996J1lEnhADsFZZeAKHmKclHg6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
فنرباغچه‌امشب تو بازی‌برگشت‌پلی‌آف‌نهایی لیگ‌ قهرمانان اروپا در خارج از خانه لیون رو ۲-۱ شکست داد و با اسماعیل کارتال به چمپیونزلیگ صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28554" target="_blank">📅 01:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28553">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRbytw2Olw_BNqneKOubPqLA-7WWHhg2H_sTkHX5TN66hlZIACiqlerA9irDRCoitiu4KQ4dOHGOlHnW_bMnEvYPxWSe8oBw6umyiJ5NuIJpHE-DBledKFuMAYsvwltwBJ1e-VGGt7cLDIXty1DI6BCIl52JPeI42oXDb39Y9-9nydGuf3bIj_KWJsOil5RC309LsSz0zpYQUC48Clo8Bc_qZRJ1U6EGgA7ifz9fC_1HL9FNHmlfRow4Oo1Tn8sH9Tk8WagGCUVleHeCwld_a9QtBBgYi0P2uAeSy6JqsQQbGyoxXEytVPWfWr9pTpTDMCEjyxph1uD0ISPYrR84wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت دوباشگاه‌پرسپولیس و نساجی مازندران امروز بر سر پیوستن قرضی کوروش اژدها کش به جمع شاگردان مجتبی‌حسینی به توافق‌نهایی رسیدند و اژدهاکش با عقدقرار دادی یک‌ساله به نساجی  مازندران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28553" target="_blank">📅 01:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28551">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV8RiPszEr3egG0PLerxJA4xNwlGZjcAMcXisPQSRTFAKe0HTy4WXsQ6ZVj0LF7W072Hy81NOKsLa7VkvqNyr6IGk4P4MkwZlF-ic8P57oiiVqzdvj0EADhOb_f0CWPS0raGrrsYQBo-axWY3eT0fzW8Iy5IzLvCXCTCDOLD9AXAYVniRp1JWHauB5ejCXBH4t7E6wN1hNi-H5-MnctRrPl6oDW-tCGD4NfRpktr7GMl9u3vVIFuVifS24-zyUEnr7S1QFMGzbzIdP4WT8LAeh4VAxGe0NG-8Et8PKwygWHJ8Zc9pMpIuzAXbJJw31lGroyJ2l2YKag03SMQ7Weeyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
فنرباغچه‌امشب تو بازی‌برگشت‌پلی‌آف‌نهایی لیگ‌ قهرمانان اروپا در خارج از خانه لیون رو ۲-۱ شکست داد و با اسماعیل کارتال به چمپیونزلیگ صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28551" target="_blank">📅 01:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28550">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnYzWgb6l1NRgayCqeJGvshUbF8B2jF5jrNHHFgkSMU1hPKW0yD8VWUr2udMKcpCiVXqRQtzD93x0Jb4_ae-t7yGvEOSEONtyl1gyxITahYnHi1okJgQnQakMD4IDd8A3Iq8lNnACqoysQtHOKWW0AkyX7lquI1DR9JgFgg1GCsoaxtzuVQ-NiZQBtcpanzu4dDgJDN7f5i_NK_5Iaz0skY_XNkfi-l7yo-oXb3FRP5JdloHyZVuOlvu8eNG0VGnAMfsbExyR20C7K-6ZS6WtAHaiHaKY7IwlUHzJ9h8r4ahK1P2UKtPw0mjpTJI3YckoQ0Q8CmwL0-ynbKv68S9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شاگردان مورینیو در هفته دوم لالیگا با درخشش وهتریک امباپه چهار بر یک از سد سوسیداد گذشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28550" target="_blank">📅 00:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28549">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrvg8L-FW5vMMTkaCGGiullXU4TnyUMIdU6V4_2Cef_mgUkiMQ1mVxnx1muh-gxmj0dvX7rvSdxplB8jdLDEvvrBAqxpnIxR4PiuRF4g7kgTOFgtozqNJoaWw-4hsGrd8d5jKg2yY6aAo_f6GXL4s_s6g8--n1BtdYE_OkEln72K1N-n7cBCjDr2cMvkUY1Kb9YE4SdvHw-quk6YJKxqxEvzwqa0tfielkkBZ6OBkD3bLY58JdgkLoxxqU8yizqKRig9-5Yd73GNTY7cKpM9cpymDRe0HvXVT7g7z9B1T7wdpXcbLdSCTOhd3XVtsEKurW-XTIpTni5BFnEiGQMC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا|شماتیک ترکیب رئال مادرید برای دیدار امشب مقابل رئال سوسیداد؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28549" target="_blank">📅 00:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28548">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5bCA4nYjza_caPMVHVylEF_wPejJQOsFJ0yqC5KD8oR_weaoqdBttQJIhxBtfzNmM0OlzoZVgkH3TH8PvzTvaDmvmNMuPWJYQiF8PhmcqajZ6LqbIMjTfzYzAL-cnDAmn96E9K5nO3tSd-jOQwd5xSBrB-SeCkBoCMm02X_WipCOYJz41hvXzQDiiT1vmfBKmIL9k7qEZ3QUKpwXTM4n4d7UsqJ4s8hPCbFAeqQ9a7wv-UpOJw0CvLfXg2hNEbcQTAq5XNvkJY96yJk9WKQNLcMwNA0Hx8excura_e2mtH5e5SSrwTEGcRpXDPzqSPsXyQfaEpbbai6zBFZB3Vr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28548" target="_blank">📅 00:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28547">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
ویدیویی‌دیگرازجشن‌فارغ‌التحصیلی دانجشویان رشته علوم ورزشی این بار دانشگاه آزاد تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28547" target="_blank">📅 00:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28546">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9LxRFTr4m4r7rUKMbhBKuWYbWtNVQxFo8EUNJ2YYBAnYvDaJE9MTD5TKFEj9DPvSpqzcvgyWn0LeBgEip1oZHxuPMNJ3Xkb4xSf5_LbTk7PNm4xWmqoK3QpVkkjkFV3WRz2hfysYtPoty1YXg6LMdwzBqnvC6jymMEpotBk572Idx_WrdiF7NrviGkpjpzyRy_4TBjpSyC-7a2k0VfCrHhrVVZuP3Eo4-pTfglnVpIQ5g8-CetvsJ5VkBsm9OukTtbslEL4cQ0RmdxmUiS6CcwPG-TRPMmAEf4oTDXMadUTIHiuird6E4-aNW-NCpT0Rl8XveSHpVOYreEEMBS6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌هفته‌چهارم رقابت های لیگ برتر؛ شش دیدار روز جمعه برگزار میشه، سه دیدار شنبه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28546" target="_blank">📅 23:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28545">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP-mJs06mM00Die-srGcuRdMSil056W9BSW1X8n4XJP5tkSLBbiAxvvcnkioXvzgUsYOPTE04WROMHZDD5h37CgVIHxEA8i0fCuFGzm2XWGlmkL0atne7qeeaNlmqMv7ZmNvX5Ob8uGMhVAwH8smQLHuL_bl6mAjLLXuaqcf_YnO-7AGNV5LxY-XrDrBIjwasZxx1E8xgAXK292PIPaXMofJCwbDLv5BdgotcydY3BbX6F9x-7Fs9gl_7v_rCHzxRtwSIOwYRYh1yyquZ52jMgjhiJsGxhI8UrBVOB9m0Tt0M7KVhgdfcr9awlziB27f0Jzc7EZJFbdVs5iKybd27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌پیگیری‌های‌پرشیانا؛‌پاسخ‌فیفا به درخواست باشگاه استقلال برای‌جذب 3 بازیکن آزاد بعد از بسته شدن پنجره نقل و انتقالات تابستانی لیگ برتر منفی بوده و پنجره ابی‌ها درنیم‌فصل رسما بازخواهدشد و این باشگاه مجوز جذب بازیکنان مدنظرش رو داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28545" target="_blank">📅 23:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28544">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🗓
#تقویم
؛ 3 سال پیش درچنین‌روزی؛ لیونل مسی تو اولین بازیش درلیگ MLS این گلو به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28544" target="_blank">📅 22:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28543">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Myg-FReLAecaJmrpUn8EkyzppJxul4exOAS7QCZhmLP0qPWPj6BA9MfClfAN77gtqu-jVgSb2WASH-V6IxbXtpJ1VM5AdHmJQbab2JX5IKx_6YeLCx5So6VoQ3eo6NUHMOIc8qRpVmcIkVK7_Kv7p-o3VlxdwCS4ld63oEmHnWwoYY9mQmUVUlEDOIDTTt1H53sgmV1sytLyEgfNIkNlyfogbonpzPpLLS8AyQDMfS7aFt4U1F3U31t4dEvN_ZUgMRugGXHRauPVukxs6Kn37bQCpwcCSI6UulfeVcRRy0QVF1PDW9UtSp3W4q-flcrHBuQalNb55et-kEch6OyPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ اولی واتکینز ستاره آستون ویلا با عقد قراردادی سه ساله به الهلال پیوست. عربستانی ها برای این انتقال 60 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28543" target="_blank">📅 22:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28542">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad00b2ad3.mp4?token=gJCxRs739SZlH7xtOyjH-fhVBAlGHF4_TFTjLYQUz0hINCrKYCzFkDSHAnvsiQntEB5M1eDhx4icNzBTp1QVvYX25vECzjYy4g3Q4fjSWi0Xqlc--LVcA-zq_lNVDTKRgpk4f1jfevpTxd6cNXXfxQLVvbXNNTejIGGRHl8n4MkEv7WS30DkPAH4x4FvirZVpCcylgcDfix7aFjyfu9WXJoj_cgI4ev3QkyL4uQBtrKBuASI5htwaDZGwGB-L3xNlM7SGIXkgwrUaTg2hc7-lnxXb_pS117UXUQJsMcTILL0ByW40mPH5yNJMCkOhNtBJFH5g6Z-fNO_2ja3r-9ttQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad00b2ad3.mp4?token=gJCxRs739SZlH7xtOyjH-fhVBAlGHF4_TFTjLYQUz0hINCrKYCzFkDSHAnvsiQntEB5M1eDhx4icNzBTp1QVvYX25vECzjYy4g3Q4fjSWi0Xqlc--LVcA-zq_lNVDTKRgpk4f1jfevpTxd6cNXXfxQLVvbXNNTejIGGRHl8n4MkEv7WS30DkPAH4x4FvirZVpCcylgcDfix7aFjyfu9WXJoj_cgI4ev3QkyL4uQBtrKBuASI5htwaDZGwGB-L3xNlM7SGIXkgwrUaTg2hc7-lnxXb_pS117UXUQJsMcTILL0ByW40mPH5yNJMCkOhNtBJFH5g6Z-fNO_2ja3r-9ttQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانهTRTاسپورت: بعد از جذب لوکاکو، باشگاه فنرباغچه‌بدرخواست اسماعیل کارتال سرمربی ترکیه ای خود خواستارجذب رافائل لیائو شده و قصد داره با آفر سنگین او رو از منچستریونایتد هایجک کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28542" target="_blank">📅 22:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28541">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmRYA1eH35MvMx3mh-8NwOQGkuWmJXNEV8cZjyf2St4Y5KBPf3xNE20GN5tIUqqcV3mPldJ-ZltZvzGBegHgHrIehywDAZKhMdp3Oz9Vss51d3X8ZELjsN3UwXr1YGdYbBOBHI71_sm1khfOqmqWAAgU8k5liLGf75QqMzltTLoCEjwHstcIWD5Yip954mKt3sJFsVhL_p1qj1oSEkUVyjFxj0Gr8cTfDT7CWmZovGIqvOoUyvYcPqthQrZIPm56U5vDv_VR7XSVV0961AoMbsJpv_a-WR1wmgoN9kZTvMcQOOIvwanCybzF7mOT4Pvbu2RAv8i-9tRutWEi9z0UNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
آستون‌ویلا با پرداخت 65 میلیون یورو به چلسی نیکولاس جکسون ستاره‌سنگالی این‌تیم رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28541" target="_blank">📅 21:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28540">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUV4cRuZb0yKpjHXQFYkfLTnKtqkgUspZPGUasg2TSPlhZfml-gPE4WYCW45Z2Bcqu4rRxIbAzHClqYhs49EfcdTyXMLDhbNB_y26mS4q_3LBCNxGzxZmgJpxn06ZYORhVJdbXV_41kHQqf3GEYkTAJHGGTobK7HOx05kpblgY8HBps4KVxczKRGiEu8wOj7RHZ5ZLlt15iM66_Ij3XMgVeCsDXkp7H5OWE5m0d86gr3Z22lEBwkpkcu6TjxTB5DkAIhFavMFYqDZtLlrXRFYyq4AC5w5pQWnZoVbqseqwZqU2tsACkZJx1e0L8K1vt34s5xVIq8e2kFIm7dL7fHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا
|شماتیک ترکیب رئال مادرید برای دیدار امشب مقابل رئال سوسیداد؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28540" target="_blank">📅 21:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28539">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIT6SqWLICNwMlCVuuoybLtYxL0pushYIWz706cPNgFoyTTuiUNVYCD6cal4V7ihuMA83T6XdEu6LldxT0qY-rE_vfy_ZeDxDYPtTdwe28OCJDJMTy73nOgEB5rIf_ZEgSc9Vmn80qcSMUiahHjyd2TchZqRpOT9XvxWaRVJcZuoD95rLbw8LrdJyM3Pz0oyuz5Udr1lDq-7bA9JscOQZpLqLWPlfgjg1pMqTL3rJDA-6i9dBsJZS40E4OUNM42DfaLn9AXeB9MHOL_xljwSuEmQKkCJ9tPrch-GQy7jN9HVTQdTddL7Ekt7pSHqtUpCCHQn9FhmBZe-GOxGyD-hgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مقایسه‌قیمت‌دیروز و امروز پلی‌استشن 5، آیفون 17 پرومکس و سامسونگ S26 اولترا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28539" target="_blank">📅 20:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28538">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKI8LqwgiV32gM_NhIaFHWwhN_M2DReg9b-0zOmiWtH9c2ofsvd-G5GjiiuoVDrQJq8wzWxvpFvRsicf4ceWq9XQpveuckluOLsuSRFa-jk7n13pBvFb5FFJ2LICa6QaPrUTyxsz6u6atdkI02yWKoK7kCDK7c5dtj3xPxlCOXSXhWgig7exRM6_Y9xhMWGyYipXOroYjgSP3xjCe_ReG5cFI4vnPhMkb3RIR6bSU11EWv74d2J4SgMRvaAtNe1L6CWruS781Xg0RqdGpxGZfKS0EKC6VGMwumA7wdK5TCyZKTsk9oEyXR80FmA4rgasFdDCXKGuZGyafQvmpQVt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28538" target="_blank">📅 20:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28537">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03aba91807.mp4?token=PVc57LGNEbIetu-5Ujk3zEX6hEhchbDE72uRzzaIVaK25zwLn96qG13Zv1yl-SCmpMr5nI9UnR-simcGdSt10x-XuxYexepVVtOUJn3n6Mzakw86VKIjOZ71B4vXS2ujmDoKR7K1ly5feHxKYqYI6KJfi7CQHSoTAK_83oRI3sRixligluY0FOfh0G9GkO1hI2qsz8XCr4IonahxSg6dWsMShVsld64mbrerRiLOXyFxuzMra-lEnD1DUEHR5AUzG0a_63RDbctVI0yZ_0TK-jspviea0h3Ap7A0GPVg1lfWu8KvN5TefOnKcK19jLRPaW3DVXp6z0hf8POx6TMr9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03aba91807.mp4?token=PVc57LGNEbIetu-5Ujk3zEX6hEhchbDE72uRzzaIVaK25zwLn96qG13Zv1yl-SCmpMr5nI9UnR-simcGdSt10x-XuxYexepVVtOUJn3n6Mzakw86VKIjOZ71B4vXS2ujmDoKR7K1ly5feHxKYqYI6KJfi7CQHSoTAK_83oRI3sRixligluY0FOfh0G9GkO1hI2qsz8XCr4IonahxSg6dWsMShVsld64mbrerRiLOXyFxuzMra-lEnD1DUEHR5AUzG0a_63RDbctVI0yZ_0TK-jspviea0h3Ap7A0GPVg1lfWu8KvN5TefOnKcK19jLRPaW3DVXp6z0hf8POx6TMr9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی از سیوهای حبیب فرعباسی دروازه‌بان بی ادعای استقلال در سه هفته ابتدایی لیگ برتر که سه کلین شیت برای آبی‌ها به ارمغان آورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28537" target="_blank">📅 20:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28536">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aeff973be.mp4?token=jiemaehV2ZKzJLfhOFXhCPCOU8hHEyx7whcrNBkco64vyPRkLZKrol-ND-y4ZDlKORkqmQ1aFGw4H3vUkbTeI7keg1p4B3Zj6RS6tmrIT6jKpfwdXJvCRCzz2zqPDY3_5IvZripedRTt-3IuWEsz6yvctqEdMmgwKgE0V16cOXhJqQATsYtQHpo0aDYZb34EiiNOGWA_04f2ETfS-kZnK_Su-hT1M_yVhnMVNd-JkEEljvzYhXtfLG-GBessWSXDdedpX3lCnKJDTQ0v163LBIBT6Umpnl5VxKGKhTJ4R231IYX6eXVT8pl5Eu9hi2GJLscb6hglx38ca703iezUkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aeff973be.mp4?token=jiemaehV2ZKzJLfhOFXhCPCOU8hHEyx7whcrNBkco64vyPRkLZKrol-ND-y4ZDlKORkqmQ1aFGw4H3vUkbTeI7keg1p4B3Zj6RS6tmrIT6jKpfwdXJvCRCzz2zqPDY3_5IvZripedRTt-3IuWEsz6yvctqEdMmgwKgE0V16cOXhJqQATsYtQHpo0aDYZb34EiiNOGWA_04f2ETfS-kZnK_Su-hT1M_yVhnMVNd-JkEEljvzYhXtfLG-GBessWSXDdedpX3lCnKJDTQ0v163LBIBT6Umpnl5VxKGKhTJ4R231IYX6eXVT8pl5Eu9hi2GJLscb6hglx38ca703iezUkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آیفون ۱۸ پرو رسماً ۱۸ شهریور معرفی میشود
‼️
اپل با انتشار دعوت‌نامه‌ای رسماً اعلام کرد که در تاریخ ۱۸ شهریور ساعت ۲۰:۳۰ شب به وقت ایران رویدادی برای معرفی محصولات جدید خود برگزار می‌کند. انتظار می‌رود در این رویداد علاوه‌بر آیفون ۱۸ پرو و ۱۸ پرو مکس، شاهد رونمایی از اولین آیفون تاشو با نام اولترا باشیم. اما احتمالاً خبری از مدل استاندارد آیفون ۱۸ تا بهار ۲۰۲۷ نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28536" target="_blank">📅 20:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28535">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_Jf4ukGWsQP9HL7ppaLwG3BvPCXL5lG1cqRUKK2wvP2BVZFruG0Y_8bgeE-VvdvTLwgAD0HFmSv7z3IHMiMHMSYSiTEEWBtDBGoIwg39sblq--j-GUD9JDtyO7c2-eW8FiVPGEbu1inlMkGJxsv5RC_G5mH57HVq8KE-2mWIi3_1lui9qorYCIGESgElmtI145j1lUaEUAwFp3_-JfcmpbyeCFGbdQiwRdKJiFfE2HQCcimpx4RbWBXapKR-vUi1jqxJA4KBvhrMOllbHK8XXudbJuX0iWLJzQSP_ixlmjTZ3ax2OQujXyQMYr_XTfQlgEKBUBFbOKOVrCWEIguxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ هکتور فورت ستاره جوان بارسلونا در آستانه عقد قراردادی چهار با دورتموند قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28535" target="_blank">📅 19:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28534">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28b7c5b23d.mp4?token=Ixb2ayOwkSsJnP8-mqLfTOgzWyWAcdXx2r6sKKU643_x-hiYz-xz418TZSWcLgXPfH9m4_CZjlfe5Qpq4txoCabOtIW0fmLFIDJRR00M7H3-nvfFj6TQ2EFvockOJW34sSI7s_ARhd-y5UudEvJWqwrKgIcwOSRbBgEAnV30z7Fl-ntNj3Snn7EemJXmSTopNKQEysEyZxuZ_DYe0FCMr_3e_wgIPNe0shXilrvtDkWp2dMKPwjX9cUxbnNrXfobl3jJRbAZgFDbKhOpjvn1RMPolLEoIOR07DYncMHac8xwAlB4DWYCuk0_q1Cs2vuLxWhem1yKW267maNmzjjKdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28b7c5b23d.mp4?token=Ixb2ayOwkSsJnP8-mqLfTOgzWyWAcdXx2r6sKKU643_x-hiYz-xz418TZSWcLgXPfH9m4_CZjlfe5Qpq4txoCabOtIW0fmLFIDJRR00M7H3-nvfFj6TQ2EFvockOJW34sSI7s_ARhd-y5UudEvJWqwrKgIcwOSRbBgEAnV30z7Fl-ntNj3Snn7EemJXmSTopNKQEysEyZxuZ_DYe0FCMr_3e_wgIPNe0shXilrvtDkWp2dMKPwjX9cUxbnNrXfobl3jJRbAZgFDbKhOpjvn1RMPolLEoIOR07DYncMHac8xwAlB4DWYCuk0_q1Cs2vuLxWhem1yKW267maNmzjjKdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
صحبت‌های جالب عادل درخصوص یکی‌از پیمان کارهای ایرانی استادیوم 105 هزار نفری نیوکمپ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28534" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28533">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov80UsXWi7oayEKTKWEnv5Lv23J2URnHAYKPrgJLynTx7hS1IkVe9r307qr6jkExCMW8ZGBt_OiBSPaN_jPxjIrQUecXdfqK2SP3_g3VcRJYAHvZqwAmL6Pln32O9egJwesOc47qkFXd251DuLo7_NTAULSXEZ-RBnJUzCxPxl5VOt2bZYofffebO4K8cKrd1WHa71b8Sap-LUsUXVGcMik0qYaJk_QZTfIOcBvRY2JibrHnzUdYcKMVdaRBLB9xga-UxAMRVPogOPY3KTsJ0ePoyRqg8ThCow-vs2EtD-c6CxQntI37n_f6uNcT4ANZHowVH-y-NDD9ubpnDvC-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
عمق اسکواد بایرن‌مونیخ در‌فصل‌جدید رقابت‌ها؛ این فصل آخرین فصل حضور نویر خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28533" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28531">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0285e0b6a0.mp4?token=Tbuvpn5cK09C9yL9tLoEKtQYIN-8NdtdTxSeJ0tnfVJFE5PX6lWPOMaxLX8MuHxPCJMSc6-e63qC3KUsio0tSvipFG6ttp84BqEBZUT7eP4S_crCG9kLDheCACnrlLDXeCQO43A9KEn6dgQXzmiR-Rk-Pc6xrD2FDCj7I0bxfXhTBIxyyWvXowneGAqDWXR8kowiOGg1f9a0Gvk5CPn0UnFbi8JZzMzVSSUqhK3H5GHDdd3378WJKIwIHakUH6j5gOGQEjr_etCHhCpmjM9WQ1w-DO9xFLUb-uWwzQzuECQI6oCoEMOd2CP57Pq9UGCT6RYf6w1hT1bAeLH1KLkSk2LjhzBACo7b21erYRffowk3p9eNUDxfrj5KKBYsS8gkx3uLmjvXdB4c5AaUlmdI2iTjDLmwfNaXfJCrGDG-AGTC-Yq5um8LNKGj5oaJYWzLxWzIA4BlI1b-34fAwAtFJc6WE2GqiVF_CMlLEh-AaXQHpR0MdoXsjaC4d98gpU2NVbDWTUj34HysOxDYPdB8m72RY33cq6A8dJ5Ic5pK55e1ijeng7uK3R7Ba9zQcN4wofCtXy_TPlrffnYxXqG4gdB3EP90wEwKIsgn3_vHwFSD64PR2fxsiTMaA8cT5ojuxSdPLl4_W-yCPLGpg3_w17MmixSmMDTM6hDOpkYK8eU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0285e0b6a0.mp4?token=Tbuvpn5cK09C9yL9tLoEKtQYIN-8NdtdTxSeJ0tnfVJFE5PX6lWPOMaxLX8MuHxPCJMSc6-e63qC3KUsio0tSvipFG6ttp84BqEBZUT7eP4S_crCG9kLDheCACnrlLDXeCQO43A9KEn6dgQXzmiR-Rk-Pc6xrD2FDCj7I0bxfXhTBIxyyWvXowneGAqDWXR8kowiOGg1f9a0Gvk5CPn0UnFbi8JZzMzVSSUqhK3H5GHDdd3378WJKIwIHakUH6j5gOGQEjr_etCHhCpmjM9WQ1w-DO9xFLUb-uWwzQzuECQI6oCoEMOd2CP57Pq9UGCT6RYf6w1hT1bAeLH1KLkSk2LjhzBACo7b21erYRffowk3p9eNUDxfrj5KKBYsS8gkx3uLmjvXdB4c5AaUlmdI2iTjDLmwfNaXfJCrGDG-AGTC-Yq5um8LNKGj5oaJYWzLxWzIA4BlI1b-34fAwAtFJc6WE2GqiVF_CMlLEh-AaXQHpR0MdoXsjaC4d98gpU2NVbDWTUj34HysOxDYPdB8m72RY33cq6A8dJ5Ic5pK55e1ijeng7uK3R7Ba9zQcN4wofCtXy_TPlrffnYxXqG4gdB3EP90wEwKIsgn3_vHwFSD64PR2fxsiTMaA8cT5ojuxSdPLl4_W-yCPLGpg3_w17MmixSmMDTM6hDOpkYK8eU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28531" target="_blank">📅 17:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28530">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYcCf_E1-MaELn0xzFmVxtgPTfn8PNNzb64UWiLGCZym464qaqbJA126capHoRm-4VQQyjxP1TCbFKMpsSFPOYAZTH4r3E5A1n0Y4MF2Wh1hueTsR7LeZGSclzB0KhHAg_nylBK3-85EZHUQ0esIdwahOBJIixzxdOcLEPUejYe6g5l6Mbza9PRPjlvPPTEkVz4J-OJ1zBH_mqirpbQpIk8A2YcUzzp0_tiW_B16otXJUX5UfxViTKYEf3qUoaSRy7UhbLXY20PFpRXExOqe1nvUHtlAlneNOTxa_GT73zU09DRxzl2GdeAKvKaRs9DmFVXZTSBYXcGK4crEv69F1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28530" target="_blank">📅 17:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28529">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89d94e3b8.mp4?token=elGOd5yxK7ZBxwHRDz4-CW9llHGyVLV_fSO8WJwP8iHgEq61CULHb7EcCCOzfmncju2q3T1D5r0mkjo08mOOeB0Y-ZYXt_jssKytdkknIIad_SMZ4p3-_y9VF5OBWKISXU6mRuB9-mo6y6AFhGBNvvJCgAWjErwn5tUar-4_-dd_T7X6aHo7MEQT4VadXXM8At9mrmOw8gi1AsikDte_wgzmP9fUnByGaWy_S07_WbCZnW36LnU16RCdvWmJ6lKWUdVxL-jFNFx-XkKWJXO7sL6VGhVAksNfusHqJA4_welfpox6YarBVSUGtb4V_P1jtNBKKuuGf9XCTawoAPTagQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89d94e3b8.mp4?token=elGOd5yxK7ZBxwHRDz4-CW9llHGyVLV_fSO8WJwP8iHgEq61CULHb7EcCCOzfmncju2q3T1D5r0mkjo08mOOeB0Y-ZYXt_jssKytdkknIIad_SMZ4p3-_y9VF5OBWKISXU6mRuB9-mo6y6AFhGBNvvJCgAWjErwn5tUar-4_-dd_T7X6aHo7MEQT4VadXXM8At9mrmOw8gi1AsikDte_wgzmP9fUnByGaWy_S07_WbCZnW36LnU16RCdvWmJ6lKWUdVxL-jFNFx-XkKWJXO7sL6VGhVAksNfusHqJA4_welfpox6YarBVSUGtb4V_P1jtNBKKuuGf9XCTawoAPTagQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28529" target="_blank">📅 16:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28528">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GODRVvzqMQLBJflK61-bXjYu_G01nUpyTAuXtugi8_q5IjQO6GLwIJK4xo3vStdfQj6aGasFeinOlk8DFv3tvscnsNYFlGLwGZM9_a5Ptn-ZFZiqAx0HeVL_zAqrFnnjsph-NwUSlTe7h2sZPr0BRwZdaOwKInyg-lJFlfvrcloYC7IR5HUvPmo5sjrYYo57HgIgYXs0ZmHoDTxT1IBojI7GDoGfRhSj5H6OKP13R-fvYrDWBErLYaZJLq0-fybypLaI1-iPegc9d_qMLKqki8vNJCtyrOVBno6zOvHJHGfkF_N_fmE0zouccxPMQlTop6pkJLdpwbbS-yF6HTZuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌روزپیش‌گفتیم‌باشگاه‌خیبر قصد داره که ابوذر صفر زاده مدافع‌چپ‌جدید این‌تیم‌رو به شکل معاوضه با حسین ابرقویی‌به‌پرسپولیس بده که همون رسانه‌ای که خیلی‌ادعاش‌میشه که از همه چی باشگاه خبر داره تکذیب کرد و گفت اصلامدنظر مهدی تارتار نیست الان زده تارتار گفته…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28528" target="_blank">📅 16:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28527">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8veVYPmXmu8px85STVXTuR2cfWmakkOLMJM3l3bwro2yqAIsO3bHYYMn5yRN0cCj0L0-MjYtDmTDFKYCpC11pYMh7uI8wCZ3eTsjFxOe0v-QZxv49IenVas-w1onWBomz4qgcTvj3G5It8BhfvYdCoyfz0yMW-Rey83KjV5lLrk_zHqZKNu2svfxtG3oqauHqEZrFEiJ1OhkHVlesvZTng8ROTs99XhwhFqLgYY66YbyHqV8YKF-lpLarseoGGlR_BFvPZ9MRLzsijjmlbdXNm2bEVKp1y57_hDq-khoFOC_aDFpjUl9jUxoteePEPuQL6P2PGqmN_x02J2Sk391w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28527" target="_blank">📅 16:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28526">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVpQl-CEDXzJzhAR0-v4emEOe3wNQaWclPX4hJITLQbHZxkHw7NpY8kCfvz6zP7XfMFDFk8iFbcUrHzsE2RmzupHVirf6e1b7BrMkuNOPp007jQymlf7_pNYY1nxNSI3XLrDpVaAYOURdR1iGnbKgrBznjG0NODzdg7zfWpgc9C6t7B0UrhwM0VMPGKZLNSLOdgfMGx5TiJH9my2QRuybftSEWyiWlpxSuAHrLUb-mVkGx2CnVJwk7n5lxxQbQeKMOUPuuQApfIDLxpsN1cCs7z_UEgpy9sLxxWnBKXg3ydv35uE1pjgky-GHgL9d9Qe_GRLgRBKENmED01PaiXoWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل شده. زنده باد مادرید!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28526" target="_blank">📅 16:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28525">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRu401IyMzgRIlFK4FjMor5GWzN23yXbdk2xXJOuor6zOY5sRQ4XQeKNRPR0bzGFd6pK0iKqByp20cuTpSMiP8vhdql7EYls6W9K7gDBSrug-bGuvzRNILgbyAtfb5SfM8zy74b1Vjv6ql3RikaAHF_EqwZyjfXqxf7tLjaSfLjLi2xR9XHcQpmK9hmnwD_bqsiqeyrnRpRNy6zaZE66pHhpwBenNckIaGgp329nu2gNmp8EvpUc3H6hiVXDnj_YLvPRNB2C48U9pUXbi0ALw3dgeW6yXGPNglmvGgybXelobAqW-qAaKyYT-TheaAkus8wlICBbuIhWNfMDmxE5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛نیمار اندرز مدافع‌راست‌سابق لگانس که اخیرا با قراردادی 5 ساله‌به‌استقلال پیوست بعد از توافق بین دو تیم باقراردادی قرضی شس ماه به اس. خوزستان پیوست و نیم‌فصل به‌جمع‌آبی‌ها برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28525" target="_blank">📅 15:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28524">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe78b2623e.mp4?token=DIBUrHq2R4xrUrPPYVctt7zkykz-AuFvB1lmxCbjivqhx8SGdU7trMqNTryjkxkRHZY7_qBheM0AqY2rIB9fmYi5y8bBGVYK0Jkm-Mg8oiSSx0-Wzsv0GMhTvohCddqbil-rii9lEIrqSKb4m1Q7IW7836GTQiJ3SrXR0p8Q3VshqxDCaKIYDi-kJYOBAEgc5uC1BqmyLxboLifKhEYcLi3rMI6hQmTXyoemoyLaAhGSsUgiUJE7vnxARRR4m8SJp1Uc1AnXqVWTuoJ__jIPjHBchbGYWVgYVWwp1hLxuUlftbiuJ4KWOr1ifYZ9jvM9xzhUmNcwqPOmtiX1FOWIVEC0NnIh5SHrRjgXdix0VuyyUwYCUtrAoXKuhHK8TEr4Qv8azrSDOiU-SiZfJHbWxAzsAujOoEo_pHx-dFA0GFPbBBuH_iiYzpmRplcNAz00JzHawpFbnhtklVbw1ttM6CVdcypIBGRPsmLqzFuImoufJf6Qj4c722HKI85Jsi4h-WvQqBHRKU0N9N55lOraqKGMKk2sVhGIvuTQNFM_f88ggil6lbvQa2jI4BayFrpFL4BxdJV_5zgwroQRl-KJTcVqZXtJGkkxGPxUf4ueFVFuYbe9T5GpTiiOTXJocOxOcBU9PTVU9XsLU_Csse9Biem6oA7iu8u061bF9S2d9Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe78b2623e.mp4?token=DIBUrHq2R4xrUrPPYVctt7zkykz-AuFvB1lmxCbjivqhx8SGdU7trMqNTryjkxkRHZY7_qBheM0AqY2rIB9fmYi5y8bBGVYK0Jkm-Mg8oiSSx0-Wzsv0GMhTvohCddqbil-rii9lEIrqSKb4m1Q7IW7836GTQiJ3SrXR0p8Q3VshqxDCaKIYDi-kJYOBAEgc5uC1BqmyLxboLifKhEYcLi3rMI6hQmTXyoemoyLaAhGSsUgiUJE7vnxARRR4m8SJp1Uc1AnXqVWTuoJ__jIPjHBchbGYWVgYVWwp1hLxuUlftbiuJ4KWOr1ifYZ9jvM9xzhUmNcwqPOmtiX1FOWIVEC0NnIh5SHrRjgXdix0VuyyUwYCUtrAoXKuhHK8TEr4Qv8azrSDOiU-SiZfJHbWxAzsAujOoEo_pHx-dFA0GFPbBBuH_iiYzpmRplcNAz00JzHawpFbnhtklVbw1ttM6CVdcypIBGRPsmLqzFuImoufJf6Qj4c722HKI85Jsi4h-WvQqBHRKU0N9N55lOraqKGMKk2sVhGIvuTQNFM_f88ggil6lbvQa2jI4BayFrpFL4BxdJV_5zgwroQRl-KJTcVqZXtJGkkxGPxUf4ueFVFuYbe9T5GpTiiOTXJocOxOcBU9PTVU9XsLU_Csse9Biem6oA7iu8u061bF9S2d9Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
صحبت‌های محمدنوری سرمربی صنعت نفت خطاب به بازیکنان در رختکن به سبک نقی معمولی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28524" target="_blank">📅 15:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28522">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNzfSrF-VotbJ8IaG3x1tOgV0fLAMUCPezV0M7_wWUZGkCqfWt2s4XqPZx5Vfan7KYdzAKq4gzL76FASCQCdDvL_65JLUMBzWEjQ6mWcIAQjex8QN8jxGqOSCmOaUyGsPbQC5meUCsA9P6jOKWkGaEKten1kxt32RFXtIdPsrc42_63hCgPHjiytBjzfh1ss3Ut7-yyAN_wwBi2lZFCRqXsv_00sa55X6q7RTWX_34WMCfIYsoHaM49iUQaC9GB2xAaFve7bkd4JbrQWYFC0WjSMuIfYJy8IAJBj55VULWfntY2VkEOGufiV9a0JiRsS2DV8eyh-OlM04J5pwj60mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyXSzNCiFZ01sCIXNs5zQ3pUlUHkB73YduPXr9xz6fnnL1cMqt99igh3yZv6lSyxlovyz6Wb3-RlTdUXSKHApBtnlAI5DDBJBAXEt9ksPMUsOPDOHzs-X5sLb51UCJrdLbnvm5zqh_9Jsq8jpONjhWuU1MJS82iB0dEVgfF4t-X2JKwCk_lrR2QrF89E2uUSE0OInYXweg3KsNUeBXFfhTdBB-RUJhdPqTYJGVfNdrw-t_nADatfZfQvOw25mdgdnA8CgEfr-aLU1jmx7bFeeHzPnOWn6QEvCOdxYBOAx_TTcwhPQsGSo6xLp_beatgrL5dXyBO3EcY1Oh6hkDIBYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28522" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28521">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOI6hVJMvZohztVZAnc01pnlOMRTcIb94MlckFUk6E7Wbdlncq3-XLu3iY3kY4GKvYUvZkDbMIF9Oye2rA9h4A0cWx5JDuotXkXdszrX6CWU2jR0cz9rXldvNJrDCDFuhFwsruxH4x4jgGvhUDIXclqOa1f90DIhd0bzK4qNeMroWeoUTOw2xDbEMFA_wUxnvkZgrVCMEfFRWcx1lee5eCdJoZx5TpO8UDAzAveG13mtsBr4bIRrBFJJfo7k4LVmWt2BDJOYDxNpaUo2R8HcZlcUGsYsq7UFHOxpUcvHTZ3te85kWKDP_vNUNF1QqNIf1X0ZmQcGNSF8HAqmSB1vCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحاشیه‌دیدارهای‌این‌هفته لیگ‌عراق؛
یه بازیکن عراقی بعدگلزنی‌واسه‌تیمش لباسشو در آورد و دویید سمت جایگاه تماشاگرا تاباهاشون خوشحالی کنه ولی هیچ تماشاگری تو جایگاه نبود، بعدشم که برگشت به زمین‌گلش ردشد و بخاطر درآوردن لباسش کارت زرد دوم هم گرفت و از زمین مسابقه هم اخراج شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28521" target="_blank">📅 14:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28520">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0asBxfBRtRtUIdSeHuBysEGPfTO5sJ8j6pyQrPSXhVcE298e70qi6qzDycw7J6npXh2ZGG-6mD3ZWtgWQmMcoV335kGz-Omfjb6aUBc2mv3pxg5YWdTynFaP-PeW_q6hZ8kBJRnI1cjET7dz3iGorpC_h_VetLiV8wPhqc617CucDRuTD9i4zltHNHdtCvpPrD6J4qr2roi1RpojCM1KAhBZZ-Yx5LP8NyXWV2549pEhYojtoKdjwMO7AlJ3zIY9oolNruDuLr8nZJZZQHgx1PMTIw5XRgwnBPrQ6Q7i8YcL2Nijm0q0XrEQ-bQEyTNTV1EoIgCKmsGxrtBVPFAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان ستاره 36 ساله‌فولاد از هواداران این تیم خواست که دربازی روز جمعه مقابل استقلال کل ورزشگاه فولادآرنا روپر کنند و از مدیریت باشگاه فولاد نیز خواست که بلیط فروشی رو رایگان کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28520" target="_blank">📅 14:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28519">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ6TvQoMEYKNQUT47W6_xB0nBvG_iqC2RlUV03Of9o44B57IQpA0xyU6zN2Sui3jJtVM60w5EFzreW0ydPFv4dQT5Ho6BM3aro4z9YY82FVixXUt_GX4HCb36oVKOg5oTQ80Fu5QeQ5Gnbi5Au6SpeYhDrNIlWpmpIHSx1DUSyHpa2q0jVCeN3NHSiy_xTm6rQ-uU16bF8yfLYWPs69ORETRR9MzOLyBxEJtKvBwpA9vlEWym4J8fDmJN0zSEdeYBnbN9K2lT26RyPi8S9PJ1h2a6ebIrCHLtJOkOvToE3hxVKkur-Mghh4njgNZ2ilxWH0Jze-wGb9-IZLBEU7QRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دولت دو کشور آمریکا و امارات براش ویزا صادر نکردند و مسابقات‌جهانی‌مستر المپیا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28519" target="_blank">📅 14:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28518">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcRV1H6c3t0DwSgyB3YyVQL1I40PETm_e47-X91NnPNTBUmthadi_wxFpDRKfQYX3X0Bv3Q9aim40WvE20klOjYNlNNpQUIHDgYAxQmtbGl4jiRyUbkAWjMdvg76PBVQWnUTxZtwqc4lkyIl2EAFoy3YFT_jbZ7s-G6Q4sbRpfEJH3wNNV3A_gLeFkyccHXEjQ2Z-VaFrbssx5mQWYQ0nW6LL4DrbokMYuhz-6vuGFwuke7zzgYjyWkXRrSMbRVR0eY2M7L9sZ6fM0Erg5DK147W5omksvV2pp_ILUbfpOAb-Ubidtv_eQIsErwrT1A69zrlxySUghIDp6yxZRTUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا: ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28518" target="_blank">📅 14:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=jukhTxL2j5yd9nGGMdEIaehpWx6lilkSgwLuFhY1ahWzoEget1uk6Ivc_zKHtZnFiz3N6hN2l0zLUpsDGVHj79siE0VKvYk-AS8DTwCIub-sSsTG6h2QzB1wijhioShAmD3t5ZqfiXuJoK61k1vnVAmVSRXVFZyx9QA4cddhjut3XWjvJsvetu1wADo50GPJybhQETbNZc8vmAEUq5rywXFvFmTdJ5lI84eGqu1TQrQozYGBO2NXqXvOvHPTaWATi9E7vi0lQA_zbT_JRYxblzDnR5-XiTYs0dVOx_VdmvFngnaLl8d_OguOL_CpPXR3PZk7b2yO0ckRTrH5Cijyy3me4-a9KRqgef6_SIsa4rkZPADYYPqCL1_zWpJPyHgkUNYA9GGDse3xWRqqAZC0j4GK0XVPWERpSLYOYwnHweNtsoCZI6_VQc1yauD3IsO1TzMj8smyUl231oITUw0nO3AlvFQf-rUmQIvXFGb9ZHw3WxWeGsUMSzk0SLyvJ5whvP3kpzP5y4sMS86ze5Me9Bqg-QpE7JWWfpRRSQK6gchDjHcyjANTPVh-WsRiecW3eUHDR1l3Sr6TRvTDkU5ORKVGDFuUT5YUrxEGktuYcE56L_MbBTm-SAn5EACj0JgKGfYgZLgeKcjXn9LxvIFlJY-TAbRyWArVB2lrQ6S5WFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=jukhTxL2j5yd9nGGMdEIaehpWx6lilkSgwLuFhY1ahWzoEget1uk6Ivc_zKHtZnFiz3N6hN2l0zLUpsDGVHj79siE0VKvYk-AS8DTwCIub-sSsTG6h2QzB1wijhioShAmD3t5ZqfiXuJoK61k1vnVAmVSRXVFZyx9QA4cddhjut3XWjvJsvetu1wADo50GPJybhQETbNZc8vmAEUq5rywXFvFmTdJ5lI84eGqu1TQrQozYGBO2NXqXvOvHPTaWATi9E7vi0lQA_zbT_JRYxblzDnR5-XiTYs0dVOx_VdmvFngnaLl8d_OguOL_CpPXR3PZk7b2yO0ckRTrH5Cijyy3me4-a9KRqgef6_SIsa4rkZPADYYPqCL1_zWpJPyHgkUNYA9GGDse3xWRqqAZC0j4GK0XVPWERpSLYOYwnHweNtsoCZI6_VQc1yauD3IsO1TzMj8smyUl231oITUw0nO3AlvFQf-rUmQIvXFGb9ZHw3WxWeGsUMSzk0SLyvJ5whvP3kpzP5y4sMS86ze5Me9Bqg-QpE7JWWfpRRSQK6gchDjHcyjANTPVh-WsRiecW3eUHDR1l3Sr6TRvTDkU5ORKVGDFuUT5YUrxEGktuYcE56L_MbBTm-SAn5EACj0JgKGfYgZLgeKcjXn9LxvIFlJY-TAbRyWArVB2lrQ6S5WFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تقلید فوق العاده صدای گزارشگرهای فوتبال ایران همراه با نظر خود گزارشگرها درباره تقلید صداشون. جفت ویدیوها عالین حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28516" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUeTzh3SreAyjdRkBpHnLrNGoJxZYb7An5sytpqMD3jtzuEqGHbnjFbD_D7iFaxyDJ9L_dCA3byQxLe_CtL-tZbWQtgNZIRScRhZ0R-msdI73KH2y7YFsx2_GVbsBJwSvjd9bfnKWAPQ4263r8KvcKW81hfWQ-ZOvgiRoXAZoZGMPoO8iDFfYkHo9FzOUrzETqx__HAmy4-wnkhD7xGY77o_QD25mR9yxvFI6AEljnTry4G0wAnq-ofQHnaqvYfCvzxQN-FiXilbc1znCFBDwmBoieVQ-yhGkjk-mNYznsiSFoMkbMI8idgvcXi5RTHVqypeV6fdIoM16QeRG-vINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
النصر دیروز درهفته‌سوم لیگ عربستان درحالی تونست سه امتیاز شییرین این دیدار رو بگیره که از دقیقه 12 بازی10 نفره‌شد و دو هیچ‌از حریف عقب بود اما در نهایت با درخشش مانع سه بر دو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28515" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28511">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8JxLeWGEIx6JNKTmRJwVU4meGkgFLqapY6fD4W7kIGNPKb2l6Vf2Y_PeglAKm9hIcwbu035zrzkurEFFtB2-1uPSM9gZYK_FrlGovmm6HrlVAU5tTNY9Lsz1-9uQCa0czD0CPK_8K0kdzNO8xebrngzZCAhnNAmQ2EzhJzhCpPu_0TrvGrgTrBmN95FswFMhPmRGgwSfRhiArGWfwT9czR7A3CD7tlv8HxAXaOc0pOm3dDvsHOqrzzuIe_J5nQOupZ-yNqbcSnyW33_GAuUBkBkj65K-q7c7UInjGNVftF1BizAtXNdxXcr71WItHv2s5MQ0-HeRwn4k_8OYKMOMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28511" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28510">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1kh5if5PyqmiQx8lJyWS6EsCRUFJsrtnJUN6T327TT0I6MuepRAeoJmSFXpCC8HuT-tAf3FMUZA9RZ0cgj6yXzUqQPSGzahz_v5LzLeSZ6Xq82ugt90pYw54gap6tCrkMX8_-lUiEmAc0s2l9D50awB4auLmgH4EbmkwhtJIviME9sX8s05uzji_lhqmWp48Cyxt7Y5KoHlJ-2GKZ--HJHkx8mAunf-XzhJCoC4eQIUDgzexNqM_l-8tP4N3jdghwG7suNyn2xapSZgHCpbAL3cAaB7MH9NkYgeBLOwY-J7dDzEA8pKCtL-6lBaZbc0KNFVpsMK_sbzDI6hSrxWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشریه اسپورت: باشگاه اتلتیکو مادرید آمادست که خولیان آلوارز رو با دریافت 150 میلیون یورو به تیم‌آرسنال‌بده و توپچی‌هاهم برای پرداخت این رقم اعلام آمادگی کرده‌اند و حالافقط‌رضایت الوارز باقی مونده. سران اتلتیکومادرید به آلوارز گفته اند تو رو به هر تیمی که…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28510" target="_blank">📅 12:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28509">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9K6a8GDvzpH3C6bbexViNXI-XzvFwmmCEkIfSCInxy6mYsjbz-oQ8SEZXEJVcOB22L5T4EK1BnW5NY6phZLjDsocoalMmqLwB3_bJF7s_jOCpNpYmDq9Wc4khJS8PSe0I8gjLvflA4i6z4GN1HQdGTG3KGZBUImN1X6RirnuNaPVm0vZdfPd-k7QnY94fgUhF2nQKMZqdJbC78iA_jSvtRIhMFzlX4q5mAhusH03rnQ-M1Bm3wJ2EVg7ikbEasRjYrw75tA7LPQq8je5aH8Lk0C2B5afy84C4KftM9Xk-Dl1s3uaRvSljGiczuF6bW4dw7BUnNQY8rT5yDUQ8dIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28509" target="_blank">📅 12:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28508">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9PrEAdTr6e1Xz7OH6k8sHhgHfo6HoXG5IHsXhmDpwSv427MRJVV4OzooccNDRW8LSIMnIPeWaMI3_b1bBbedtfw6mD3LFvg4goNKcYca9y4VwhNk7oCLh94J9fIOdrOYjL6z0aV3N57tihYjqH9r-FgRUeDPQgshaMQym2vT2ldFLcayWl2kD3_L0Q0IYowHKji2RQ2UJtw8qaOzZ0FTzusjv6huBWtrdPMSSKw9uyR7lm2puDr6gDKFmAlQHgosbnAiOl5HEZASupQhonQOTEhfX72CaRr1Dl1wVAeqhoDn_AdVKXmk1iF1oqUYx_TJ8STr3kqzdE3WrN7vu6STQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار کوپه:
آدمای داخل باشگاه میگن که تو خیلی ریلکس و آروم هستی. مورینیو: عه؟ پس تو یه منبع داخل باشگاه داری. خوب شد که بهم گفتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28508" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28507">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099bc5af8b.mp4?token=tCuZJqw2S6pzNToMg54MU1z1Pt278TGAS2zISDyyx91XkJnyww97n0shSxom1tnJvywEOy9NDm6KLSVPwqjoKgme5QgeJAyXlwiV3cjlqR5DSpJD9taWgHA13v-C5rDksgRSH6AjiQ-4cBvnc0raIgv4fL4qM1gPx3tqwxwQY4dqrh29cQw6Xqp7ttazJLTmV63ziV2Y_FsO5BDDs55L1Vd10ATo0-7zuyneVlTOoAwYuuZfYWZkbYRSt1eohBjBTYgFMt8VTZQqKEu4amYK8AQeXEmvk5tnIbrFkW7Bou8_HTw5tXUkP8SH6wm2Tjj-0uxxyEwkr3hfx1PyIcFzBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099bc5af8b.mp4?token=tCuZJqw2S6pzNToMg54MU1z1Pt278TGAS2zISDyyx91XkJnyww97n0shSxom1tnJvywEOy9NDm6KLSVPwqjoKgme5QgeJAyXlwiV3cjlqR5DSpJD9taWgHA13v-C5rDksgRSH6AjiQ-4cBvnc0raIgv4fL4qM1gPx3tqwxwQY4dqrh29cQw6Xqp7ttazJLTmV63ziV2Y_FsO5BDDs55L1Vd10ATo0-7zuyneVlTOoAwYuuZfYWZkbYRSt1eohBjBTYgFMt8VTZQqKEu4amYK8AQeXEmvk5tnIbrFkW7Bou8_HTw5tXUkP8SH6wm2Tjj-0uxxyEwkr3hfx1PyIcFzBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
گل‌های دیدار فوق‌العاده تماشایی و مهیج امشب دو‌تیم چلسی
🆚
فولام درهفته‌اول لیگ برتر انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28507" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28506">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOUBXxYpxunzbEzI-IoixbfW6NAi76ra0dUgQ1rMNnuY5eQXNE71TRDxLGzIOBpQ3uzXcEP0XvJejjrYuQwyFLfYaUbjPOBXF4ie8T3dGaOpCevGagIOsii1lipyn2OPQ2dZwq6fLV4swDGKKPDZzhBcm86Kjg7woInX0JbSNZl7GN6sxANHwGnIkEHhrm69abZfHHcDD3c0TXHwUVGHjxYwMlGmSvbuyRiN5zZ_rQ93swKDkaytcEgxWN98FUTfE81R7J11nfDLMdNhCOQpHrVaAcCYDXsMBtkveQ_XGu501CttuMW8aDBcisMy1HUtkwf0OyJqyFTjkBRhuvr-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28506" target="_blank">📅 10:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28505">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwxWB_qMQk4x5DZT04TIE6IU5hEKQi2dKtBMFYQ6nC9xXSywysItzPG1hSiKThnHfMcgqLQzICLDMJpe6MI4tC9KW32bEwoqJu4nlfYRjI-nNDlJdo-bNyM_TTwquo3zs9wLa96IMlrDXtVsmUkJyZwGnSyDmgusbzIKlaeTPW-kl5u-5Ecb2iqSHszgksByjd4lFOyY8zOAdeKuynIHiKayJzQk3AAPJ_o4NO44_gpY8x7qQ4vD7H1H6_BXeJ0mWE3eXky7IQZaAYs-rpyfS1Eh0Y2-jha-73sssC9ymAH82-Pw-Ii-V3pI1OTtIiIjzCIY1Vih29Gtl9I--g7ZFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فکت؛درصورت‌پیروزی‌استقلال دربازی روز جمعه مقابل فولاد در اهواز؛ سهراب بختیاری زاده به تنهاسرمربی‌تاریخ‌استقلال تبدیل خواهد شد که فصل جدید لیگ برتر رو با چهار پیروزی پیاپی آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28505" target="_blank">📅 10:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28504">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S416ntd2mDERqLSXwkuoFRUhtpmxU5_bdq249Qq-2mo5yxdKPcHboNrk4R_z8UBOEAvE-Ny7A6j8ofBGS7qw0khk4uI0LFf_TW8qcLOWN6nx4ZPjIQeF7kcPh3CkFg0lg9ojl9rz0-dDVXxauRjB6U7LdfEfZQmG0nlvkWQmF8IrmanRQFwfjiQTVDlz1MEkFn6_W_DezqhrT0BY-zPv7AObQrV8wh-Ff9Bbbl5asJ8w8z5tdIcebQBUsSxQC8UG-O_BOjmHkaVzyv_zhAllVkN-Sll2wc24kMmi6y43G-roxxHXGV3Pb0OiK1eMb1Xl5jVUGl1jEvQzDUvaO5wi3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته‌چهارم رقابت‌های لیگ برتر که روزهای جمعه و شنبه پیش برگزار میشوند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28504" target="_blank">📅 09:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28503">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLv96oiqThdIf-JH1e0bflYvysuLHripO3EN5LHn80xdpa8NvZ6I3c4dmKSYxhkb5zlrMPANDbCczzrFpk8jIjsZTw2J7audHtr6YWsI4PrtIwapWnvfmnVWVK7vfAIhQ1-ncPpuYDPGRYrnewbhbN5AZwE5oIfHWCr7F1FFFmwBv8YFeo5gvyRDiDYgHwDsFvEPSMegx6hi-5xUR62JH1-BXdpG-e3DndOaLHzllQs0vdizlOkA7WLz8gerY3_f9v1zX49j2-U77Y05k5DIoEP5q7cibz5ezGVyiwb6fr1jJJHFghKoljOsgRwT3PZ1V-u_4wICBMP5AcXPGlrLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوانگی‌مطلق‌درسوپرلیگ‌بلژیک؛
رویال آنتورپ با نتیجه ۴-۱ مقابل خنک شکست خورده بود و تنها ۱۰ دقیقه تا پایان بازی باقی مانده بود، اما در اتفاقی باورنکردنی‌توانست‌بازی را برگرداند و به تساوی ۴-۴ برسد. سه گل در تنها هشت دقیقه برای‌رقم‌زدن یکی از باورنکردنی‌ترین بازگشت‌های‌فوتبال درفصل جدید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28503" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28502">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quRYs2rKFgKTMCLCfWPI49ACbGn3WA9X9PnbF5vUmqdplW0TGsqmWcW789Oxrp7g7WkAnDUgD1tFIRxngZXNCU68so7lOtuDlvHpGAoLXhsnQsGuUZue5KWYxr8P0yrTsRDzaaIYHLgmLc_jtts43_vtTrd1BrYSRghZPX4j8nyWA63tuypLpfSoWYdQSYV3dW5bSk7EtUkmNCz0YjyBRoNyF6xdJHOM-QIrYd0JDApV94EqVOjCPpqQSjVrhmECcBu2Jo6lcqJ2GjfxvAXIRxnYjiDEfLufBX1FD24QJURiRUJHYdQ4YVhET68PJWKDeAXpwcjJsR_yu0e4pv61lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت‌تیم‌های‌حاضر درلیگ‌برتر فصل 1405/06
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28502" target="_blank">📅 09:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28501">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXqSRjR3A_i4x4aNMtijmO5SoWRJn9HDjr4uvnMfaD57TfER_VgIFat2tESXSJviqxjSWhC3DnyLGfmm89j8ckXMSgQfNFHuRUGJbpAw0ywUnSugpXZqIMrvlOeiG4p4vL3-zvoGuHafBjmrw1H99fYAUF72tEECPRmaSIuZDhR63tDZPbR8EGmJ1KP2P3j28tpHFycw9cpbowV353IBg50vY7gP6KnIwpqIF-7F99sovJzT3Hd6oWGT-ILAx-WKh1oOVLghkHMFi-0Mxs42juD2IGvgejHDLLsaexs4M9PjUZR6s7xA5JkQV5E7kwXc4-if7WlCTeZHjbtlPVO6Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
مارکو رویس در گفتگو با رسانه‌های آمریکایی اعلام کرده به احتمال زیاد در پایان قراردادش "خرداد ماه" از باشگاه لس‌آنجلس‌گلگسی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28501" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28500">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MputYrQ4ZdMzxt6KTYn01Q0ClGpnlynZlrmzT-eGYHqOSrY7CJOwFxtvK5YqovZHyJD7WbQBn6KOSnDezV1JxF8KJhhoDIXrRwDNBBxlCSWI4KVOUsb4HvRjEIXG56wVeGb79aaF_gOtlwHMjCyBGapbFaMkpHbIeOfqeRihaPJ5SxY7TOdLjH83QpDEMdnMjBoXAFkc2f8gcy2AQxNKK5ipUIzViO5WliDwy9da2q_yKriUnwXzdPm-aG5adXbZKfKP-MaNxCKMBF6X0lgdZCvObc1Sc9ou0eu6EnRupMrEYJB414AfmD3yVVUYTosvdwHw3Tz4fWPxMTGFBt-PgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
دومین آزمون مورینیو با نبرد کهکشانی‌ها برابر سوسیداد در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28500" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28499">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi3eB5pOSNwABmVpSxYwERISah0vqa-bSZbLw22m4vdx7za7wIBhJjOzrco5SeNB9BDTDvP8b_MSWnJj8uo2tVhTD1X3B3uVzC0Xmx8lufPHnnXcIfWjdXweDiaw5xVowFBVENh1ZPHblSSzdZlRWrvua-vQgHoCzzrMKzQSB9uz8VbVLIQLAth6qMQ_AQqqvpDOmCdZ9MY-SLOtcpCzAqhYorom-EY8hDSuK4vv1D15RI7lW8ec1TqmPaIBMv4xUk6x3nSWkrSHoTFy4ratrBLKX0GV1yl5StTFbjsMxWPdrS9ujXLHa9wKUUzMslhmbhVJeuu1fAAgoLZh6ggWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
بازگشت‌دراماتیک شاگردان پوستکوگلو با درخشش ژائو فلیکس و سادیو مانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28499" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28497">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Es_KEtDzCphcP821YH8mvT8-d81XX--uiuZLUzdWdBfsCfTXo-GSkCkg6XCZNhlwLe-qwF8xpW3O1QN8g8GWCwUHQ3tYlwpeQmGzBsRGjVf8j60Co1xuODAe9ybuS0P-wzJNP8jdGBZ_XmgZ5v8luQ0IKcJHNXxHZn9nqaIwYCM_vEghIq6fO-c-0oAWfno_N9S-PCJUjplGbNeNX5tRXRm9HLB7ePrYmq2RBI051x0vGHeR1Dy5rpCse2Y88_9p4mi5d2m6orv9KhI15wsoDAEZp2xUcDNAwDVWyGiGVPhxnvy6eMXReXrcYsDidqq-trg2E3egAz5pdqFl59eypA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛ باشگاه آستون ویلان پیشنهاد 45 میلیون یورویی الهلال برای‌جذب اولی واتکینز ستاره خط حمله این تیم روکرده و قصد داره با 70 میلیون یورو این بازیکن رو به عربستانی‌ها بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28497" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28496">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=O-ho3LqwpyGS-ISIOaDe2NvJlyJUvh4zP4kcKpxAFjxs033sVY1ZYh30LamIcJjyc9HUN993V39d7EMI6oky7aU7Ar-CMn0Vh-Z-2eukdlIhBkmadvZl8GNk-9DVXyIzOLtcStLRp6fZqx5rStC2A2Sa45VKk_ke27pFj4_sI2j-ediKkPDtYy1YeELImVwZlFi84cgKd1HNG5aqqKtxJXg-0k0MhGEWFHVuh8X_Udincns4M6oGN5lz0gIQ0N7Qh4H4G_3cA_rPMKEqjmNjZXtrk3GPbuHiHk3TNjhoEjrFzfi6fJOPQDTcR-ok-AXFAY8H6waiijMirm1q8sQvnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=O-ho3LqwpyGS-ISIOaDe2NvJlyJUvh4zP4kcKpxAFjxs033sVY1ZYh30LamIcJjyc9HUN993V39d7EMI6oky7aU7Ar-CMn0Vh-Z-2eukdlIhBkmadvZl8GNk-9DVXyIzOLtcStLRp6fZqx5rStC2A2Sa45VKk_ke27pFj4_sI2j-ediKkPDtYy1YeELImVwZlFi84cgKd1HNG5aqqKtxJXg-0k0MhGEWFHVuh8X_Udincns4M6oGN5lz0gIQ0N7Qh4H4G_3cA_rPMKEqjmNjZXtrk3GPbuHiHk3TNjhoEjrFzfi6fJOPQDTcR-ok-AXFAY8H6waiijMirm1q8sQvnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28496" target="_blank">📅 00:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28495">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=aJEsMvUDOVI0WXm__ME5h5gXjnV2FNKp88gL98IqSKCqdewFgHO-isffopNG0kVKt6Z9FOkdvOai1vDlVioQTRuyAvYjGBKbPHHCpXntpF83FmJCTGQU2s_AUcG88idf-e8nolntEM7yAX-A-ej9luVZfKdHF-F5vuyjzjEHmRvFZ_azSHU_oif3Q53Aj6hlBNa4gvMKse1ujijbCnwhUKQQD2GGiD_Lr9gdPXkhiJqRdLk2VNDfXGQwht-zAhK0OIU4ALgPQyMszQ0abT_om1ylN-7PZ_WvPnUlIYwJplLxGaw8arMqH-3ixxMDt9zFBZIXNhZVKsmmae7rCmsnxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=aJEsMvUDOVI0WXm__ME5h5gXjnV2FNKp88gL98IqSKCqdewFgHO-isffopNG0kVKt6Z9FOkdvOai1vDlVioQTRuyAvYjGBKbPHHCpXntpF83FmJCTGQU2s_AUcG88idf-e8nolntEM7yAX-A-ej9luVZfKdHF-F5vuyjzjEHmRvFZ_azSHU_oif3Q53Aj6hlBNa4gvMKse1ujijbCnwhUKQQD2GGiD_Lr9gdPXkhiJqRdLk2VNDfXGQwht-zAhK0OIU4ALgPQyMszQ0abT_om1ylN-7PZ_WvPnUlIYwJplLxGaw8arMqH-3ixxMDt9zFBZIXNhZVKsmmae7rCmsnxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز اولین‌تیزر سریال «مرد سه‌هزار چهره» به کارگردانی و بازی مهران مدیری منتشر شد؛ مجموعه‌ ای که ادامه‌ماجراهای «مسعودشصت‌چی» را روایت می‌کند و قرار است از اوایل شهریور ۱۴۰۵، به‌صورت هفتگی از شبکه سه سیما روی آنتن برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28495" target="_blank">📅 00:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28494">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLVnzomNObCg8Qranp9HxCfZmFT1IowvFTq_M7S352HOSEP4va9ZF5GiluuJGGL8XcdfQ7JoWHHSJihGaOwWqlDRybyvrgCzF3RWdgijajwf1bg9t3VyhAL4gcDkuyX6s8WXcRnvdM3qY6hfQk5Jjo39JabNsklr2bqaVJunYJXw7s3wShU2S8UPNOyi2txtV40_BnTOrVTvfTgErljkqm3WcrEYpRBiRyv7WBh02gKdJ0iItRelu1HSRY5nCQugEUrlSdWDogB3S7ZhDZSByxfSWQvFNzGk0f085eUHLarCfdiElYqQ5L43kDizHUwDtueV0yoIRrEwKGw9EyWZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اوستون اورونوف که گفته مصدومیت جدی نیست و مشکلی برای همراهی سرخ‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28494" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28492">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKJUJq8ABTE9vt_0sHAXrcY9dWLy3iXZhx-xWCpTuAb9DzFODWiIPVycQs7ubU12Od8yE4IwTZpFKNi2dgPYXe_VcCKNpBwsBAVcpFsXi287vJxVn7ljfouu5BF-8BaxFO-xKrslCRQHp-w3aEEUqND1IBNGXZvNh0SmTm-wdrbmU4mNO8EbnPG6mXE_lcXVUThJvhM3IMr9XrKO0mXpKugz3lm352NhzZMI1rxgPx1qw5SeRcytUTy6-hqXvdIM0wWjPgdhL-IuXXkZWPezbXSL-mz1fkNIm0HGmurP6eH666d3crGOmaaj2SaftiueilHWPJiI3XIifSXVRDo1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C188Dvg4ChU_oLfb7OIPvpz-FUtEo7TB8G7eu2lB6gpuyFCzMfZSZ46kJFZaVNjOgW1vmB39D9jYjuOzXCkl9ZsnnWQX0KMWsQQtBXgd78ZQmUp7z01EsTNTJS_f22tx1b4lmVDQjpUJRa2f_WdbqGzcQcHi7yC-erzbi6bdL6OxMsZEyEqHBc4STSZbLB6DbRWnJqY6ktCnoQ_laKL1lbkAZ2AIlvUb4XTctygsAUlCxCoV60MnqiklCzxn3t_GOoaURcK2Fo27WHODgtfaXcJbFrJ1sDTopBq39m-NpHFFXRp8pYxQ-qx6_7prlX-iwNV43FCJ6rhoKqJ3BVdYzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28492" target="_blank">📅 23:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28491">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rerdnnOmrxQUM_neHfXZR_HHxhefjGum_k4q3ojo5evT9NQe-xMyncwd9h31hfzLnB2LjkDVTR04VlVh6l_Y-APGqspoNuEKAZxrAEuLKw0n8KLajMNTgHERCOUnqPDlOaiOjn1xzFEblxuvvi5tubhytLqVq51_oqmmpV1RVje1V02d1TvsFc38Fsm6yLFf0MMpkMGORq47Ogn1HNjIfLlJ6kL61JM4cgp-E9ZkW9_XAXARVnnolWj2Rl_kGQQ5aX8-YielrGG247wsMxY4Dugi0DinLVlYxpRffk-4YbRDG5rJ0I-UZWUPBuBuUYWhRtq4TVkMIS3IrrY0NzXBEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مصدومیت اوستون اورونوف از ناحیه‌قدیمی همسترینگ بوده که بارها در این ناحیه مصدوم شده. فردا از او MRI گرفته خواهد شد و میزان دوری از او از میادین مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28491" target="_blank">📅 23:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28490">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d926debd47.mp4?token=D19yK0CpTMK2vtFEQtA3el4OXOlYjLmdZ5u5gjPmUOUf8aXV4fXV8PEiNWqp5-k7L9DEQFqfNUCNk0N-cfsnJICnnLD5t9ADlFDQGtZ21U8mz_wMItyxT00RCrz3F7ieIZeaD5l_RUS9hn_vPshcfD48b_ZH-k22gSwp6ibS5JLW6j6rcktQO-zYHAaj4V1EZPZfbyrcNM0-F4FC1yxgceqbNizd7cp5HlKdv4m8BnAg3giUo25UMwO4gkXC5-lFKRsGMjWnrLcQrqS4KLL52kzYRM9UKFTtgETJsZulmINYNwiOJoHpI88Zj8vomjAQl2cFpZx990kVVcv8s9oXWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d926debd47.mp4?token=D19yK0CpTMK2vtFEQtA3el4OXOlYjLmdZ5u5gjPmUOUf8aXV4fXV8PEiNWqp5-k7L9DEQFqfNUCNk0N-cfsnJICnnLD5t9ADlFDQGtZ21U8mz_wMItyxT00RCrz3F7ieIZeaD5l_RUS9hn_vPshcfD48b_ZH-k22gSwp6ibS5JLW6j6rcktQO-zYHAaj4V1EZPZfbyrcNM0-F4FC1yxgceqbNizd7cp5HlKdv4m8BnAg3giUo25UMwO4gkXC5-lFKRsGMjWnrLcQrqS4KLL52kzYRM9UKFTtgETJsZulmINYNwiOJoHpI88Zj8vomjAQl2cFpZx990kVVcv8s9oXWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ژاوی هرناندز سرمربی‌سابق بارسلونا با عقد قرار دادی تا پایان جام جهانی 2030 سرمربی هلند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28490" target="_blank">📅 23:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28489">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28489" target="_blank">📅 23:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28488">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6PmWvATIjR0AjbmAlkHSnAQsjQNcpmS0BHnd6RuqddZ_4PdlganzJXmOfhI9TAF10H1PRX6yTAKUOq-i5aBZAPU6AiCehauONrOGzB93pZvDdpvXgwFi-3gIDcVba8-nVRDMxVSkhuVVXezF3p1yhd46bMjDK5SQFrq2KTbRCOyxqZ5YzMQ0f4r7y1jaDpqBQmzE2fefD1LrmffDk2xlU6nVE6spriEca0a-8uFgecCIzsdlWBaxkQNKjPlE2bJGPS2epruTIlRRGCwPgF41lI-GUOfPK_P61p45psMCkvmgQ2_cv9hJ8cZTvBiDzeuFWGkobg4hEgUn8uTFfxorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇵🇹
برونو فرناندز ستاره پرتغالی منچستریونایتد بعنوان‌بهترین‌بازیکن‌فصل گذشته لیگ جزیره انتخاب شد و جایزه ارزشمند خود را نیز دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28488" target="_blank">📅 23:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28487">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcqaoQdejRcr9UFi5jcl9JoD1KatCt6znj1GpIX4vrRj5FmqhoXB6GlR5OPMU8-nD-dxs2YIijNIkBpQxlKraXk4AxFIm8SukbXtGRCE8jrMriwHjCnJEpKu9cPYYE6_1yvqRg_JiPOLrvHW8rqtWDNU8PgBCJ4Yd9a_FB1eP-pmC0T_68hodAVYacdVMhZsZWP5TivoVEGsMYbdmS8ZkW-XJjFrCEdbQ6E-9NcazkmoApHsamwMnWXtMvC3deIBErz-x5gdLHGX3wj5SLnla6RJh9FD8AiKn3df8lfS-3hqn_8EoZZt6KqIUG3R5D4FrbZLdWhdS2hgjaYutnAc1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ترکیب‌تیم‌منتخب فوق‌ستاره‌هایی که فوتبالشون رو ازباشگاه‌پرتغالی‌اسپورتینگ لیسبون آغاز کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28487" target="_blank">📅 22:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28486">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f05b52e15.mp4?token=R1q5-_Qq6raq3KDFFwqE4dhMTUAiLADQVSdzMGdKa14coOQoiE7z5Wux88qoiH8jtqP68laylfu9KDCR5dHCoF-YSXQkczTyU90iJtYZWfHKoWfve1RFEAli_cXJ1aqhKoSU2Put1gEzx1fWRTRFIT5Fj93HiQNVQGnpM-2uHrhZ6t8XfQREvXVsmINLEtVfOxp1EliyJbT5LkNDNQmO3EscOBvFSqxP-mOHmP7TyWPpUkf9tKFPkNzfOREuRlSGTcG2Aew6OKTtwaPzLLuh-hUgZMhIiy6RSc0-dxWX-oupd7MXKNaz0dQTC9suF-LTdPHWaDOpMqX60OJ0674oBhRgLv17-oKtuEUG1rH2sPzfl6q0qXdqrR7jtT5Y8mNzh7CFtxql8JDUUaMFKTQmgy1DGHkyUOiiYon-5cQCIomT0_I8eQK13RoTMFG_o9Cf7Ouhf0cbYdWOZZaZTnaBH8LcTSONvwwPE_KoEwMhtakxXtsWLXL8nRRiLAysgGmeSaD4oAVJqsEvvahb8zdxYJFg0rQkY25VthncDeEsbdkv0vi6GrD6bESJkQs-MHhuoDYEtWpcauUqVPInmaixW2XRKBUPPP6nu69hz36ctZqCQY_WAi1wsJGofpDOet5kTufPuqykjea5i7n1cunsvBjJZ_fDNTjGPd5T6qxRhVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f05b52e15.mp4?token=R1q5-_Qq6raq3KDFFwqE4dhMTUAiLADQVSdzMGdKa14coOQoiE7z5Wux88qoiH8jtqP68laylfu9KDCR5dHCoF-YSXQkczTyU90iJtYZWfHKoWfve1RFEAli_cXJ1aqhKoSU2Put1gEzx1fWRTRFIT5Fj93HiQNVQGnpM-2uHrhZ6t8XfQREvXVsmINLEtVfOxp1EliyJbT5LkNDNQmO3EscOBvFSqxP-mOHmP7TyWPpUkf9tKFPkNzfOREuRlSGTcG2Aew6OKTtwaPzLLuh-hUgZMhIiy6RSc0-dxWX-oupd7MXKNaz0dQTC9suF-LTdPHWaDOpMqX60OJ0674oBhRgLv17-oKtuEUG1rH2sPzfl6q0qXdqrR7jtT5Y8mNzh7CFtxql8JDUUaMFKTQmgy1DGHkyUOiiYon-5cQCIomT0_I8eQK13RoTMFG_o9Cf7Ouhf0cbYdWOZZaZTnaBH8LcTSONvwwPE_KoEwMhtakxXtsWLXL8nRRiLAysgGmeSaD4oAVJqsEvvahb8zdxYJFg0rQkY25VthncDeEsbdkv0vi6GrD6bESJkQs-MHhuoDYEtWpcauUqVPInmaixW2XRKBUPPP6nu69hz36ctZqCQY_WAi1wsJGofpDOet5kTufPuqykjea5i7n1cunsvBjJZ_fDNTjGPd5T6qxRhVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تومیسلاواشترکالی
؛مردبازی‌های‌بزرگ؛ اشترکالی مهاجم 30 ساله‌تراکتور که شب گذشته در دقیقه 80 بعنوان‌یارتعویضی‌به‌زمین بازی اومده و در دقیقه 90 گل‌برتری‌تراکتور روبه‌پرسپولیس زد. سال گذشته نیز دردقایق پایانی‌بازی‌برای‌تراکتور به میدان اومد و در دقیقه 90 گل‌پیروزی‌بخش‌پرشورها رو بثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28486" target="_blank">📅 22:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28485">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWWUeq7uPodACStUDDum0GDAQVYndEAAS5SE6ykykQ7UNe-yxPAV1ZiAOQkSBKRQjiswN3w2rfAK28xfAN5JB1-1jX_IwBngk_NVKDItHRPH5L9HbJQ8duq0f5tqb_cX6acv8pTvs81ZWqtR9rtB_fAYfwTRkJlxCQ7kj6_es-Gh4RQ9JMIZoMIb-2eOmGL7QhSxNMdygDfh3nUXzxVMS67re6RLfLm3Uwkd3KuI-j_QtfJ7sAwvEojH5Rr4BsNvxMp4x1VuiVoh5dVt_6Unpgyh4TmnbB7PDxi3KizQCO4K1wJm_opUm5gYhcPDgToIYX9dLhlUIYKIePCHo-51oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ انزو فرناندز ستاره25ساله باشگاه چلسی در یکقدمی پیوستن به منچسترسیتی فاصله داره. آلونسو گفته دل انزو باموندن درچلسی نیست پس بفروشید و 140 میلیون‌یورو درآمدزایی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28485" target="_blank">📅 21:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28484">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgHrf4E8cCEbX_5dqOplo4Sn-U0G9iehbbxDnUVit1MTltRaudVzqVF33jevUaJZ-ULHgK7OzGf6hYaS39g-vsO_3437UbNSuQrX319VZbFGJlPMObJTAvVbyjOgl83bXdn4TIk-9UefnMVaaDWlA0ZaENrYDA9IpYMV3heB9GH2husbbgXl-r5TSSOgIxTMVm9Y-Dbna1PF0t371Us6eNla96R1ykVgh46uk0qxq8nkpR6phafuBRJ1i-03B9lLYQx7AuHNfhlS7Fc_ZiS5h7AD50NOOPL_cWL15FmzQMHu_OnFRtR05w600uTgYlzfI-zkBNfzKFmfBWz3Dc3yUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌میلان باموافقت‌روبن‌آموریم؛
کریستوفر انکونکو ستاره‌فرانسوی‌خود رو با قراردادی قرضی تا پایان‌فصل به لایپزیگ‌آلمان داد. انکونکو از ستاره‌های فصل‌گذشته روسونری بود که روبن‌آموریم نخواست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28484" target="_blank">📅 21:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28483">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3NRCLmRH0y0ser1j4lTS_i7ZvyGVEndgKt8nnCEJnGRoWlfQDabPhRZii8A1OojLXzcZfqFsp9pGgZcZqvW8oSySjpl9xlMHxGpl9cLs_efgGKRID09pQdOnXB6m3xTFkhqo1RUohaDuaHv0njf_1Dt7T4lbyMlQBeJixJ_EhZOdFbxo3yzBA4O053NMtcoqlzyD6XTtk0Vky5wCDIitWkxE7Mpr2YJVpi-Vaz1FRWmVPx_nBDQch1IA5bFmVntXx6VdT9r9YiqoOUd_5h9sUeQRHL1VZF71P_pcjPvebNF9S-77jH9UDYck7V8awsDlAlEbuYuHGZoa0dhd0UaIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/28483" target="_blank">📅 21:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28482">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po3hd-mzzdJ6BIpsPcaB3_qy0-wgkU5IqksSRBZg-vgZvwgdrHLRbbwa7Z5IuGEcyGTJVxKntHbCbx2GXnpjWOUb_oMLHIm5Ke6Z7WB61DjGG3QPqGFzR9JmlRFXzeYJ2w6kIYLauz3-edNjogKzft2CNM_vEqUAnPekEGUbN1_tnrrisdyNPoS5G1mmb1pqNv7FISxhhaL8Yd0dpTb2zlgvbKVejd2B3w4WVfddIwYk8A2APSNTsBQAnL9oCasyyCCOuLrpcbgrm8Yd1GnisjpZZx4GGTMsuH6AeadzqpdL3vq6d1drlADZJxKqYgp0f5jQNYLUCEfoKtoamI0v-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛
با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/28482" target="_blank">📅 20:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28481">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_mbbsyiynOJeNbJZzjKKBvD6Ky3K_NH_dggw2FBM5pnbgnXD8swcgaQwSD-AmGDW-23jSsPbuVUpkwXmkgRWBidyMP92tFiJRBMb_v_rIUn7SQK461hgPgUj4WtOoilKmEcOcTUSojzxkFXv8OzHBxsfjhsy4O9LaY10qX8uNncdaBcmz7LLUcq0UZZM_rr3CBfJ5eE4KntWcHO4h3ufFYG3jQUCTMiykh5yP8WeTWWJRVSSOFnWA1RCADOsk5nn3cYKN--omZRGdLwbxrBpK_Zh5G0ewx4HDDP3eEM8AAsvNteq6JgnMq9Vo7gjpAqCOfiBPCOfd4DG7aOUTvGBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28481" target="_blank">📅 20:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28479">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ec1806x35nl_MQqy1HKCAw5EqRkzSGrZzsNN141DV3IgL_JcjOiVtHFJrwjy7KagFOrGeHYkpoB-ghWzwixXbh7WGnyry-2MU3XxUVvMw5QXVVRxc31wouYnCj1s9Sheh2B_yvH432vVsELgYA8MmhriIWb8wg7-2T7ICIZ136CLPTDJDsVeYB95K-7VgeaGOGCIA10W-HzSRynbt9mmw950y2H_MAcpmyGEAE7H0YRkap9MnQl21t3e81nTur_EtuOwvBvqPBGkZkR1Toh7hlx6VxBXNVR_1JN7slwdbpdxbAzWexYGP7tWOoquHs-ArrEFpcAP09pYo_aKfvvsGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOjWWTnCKuwEYbqV92ZcLmIK74_Sm-pRLmcuSKSHGjoHZWjciwdAFhOjuBjDi9WLnIGZYNrcP4StU2bA7qbE0L8hZ8gOD-UuMnQR6DPEXPHTQTS2Rb0WFKZgqK-1_d2dapgIh1CKchd4qTiILXjqShsczUw1lSLBb4JR3_BpdQ4LxN95Igcbg5ltHcM51OitmAhuqs6rj_l189vyCzN5Ce1V94vzl9ZUeunJ-OpCC9UarVElkuTIT6LpOGHpSiLfq-3p81tPSM9xlo9exo5rT6ZzW_dqEyczVta20llLpfDZaJLJJd_FXveIzoLXdBoEoHdby54UUmxfJojlQso5vA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
خبرنگار معروف و محبوب شاختار دونتسک در کنار خانواده اش؛ جالبه شوهرش بازیکن تیم شاختاره اما اندازه خانومش محبوب نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28479" target="_blank">📅 19:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28478">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1_bvvmxDeJ1kbaOJEHQ7EX2m1LA-CAVEIdNqZu_0aO-a_ivZ--zLyCiBM5x7lLQ3GQP1hM_TNkMKvXncstRc-FNfDt9xg4Y3immjjFtBQUR3j8QNyDZUYO-oxm2tV9p-5ymtvqx8uKARcMs10Tz1gOHATK9trjeNrEHu6mBSxS2h8oGCPKnV5g6YAEndM8NHrzYvgYRpNOXdJUvXODwk0Q_bvFPFg3-yzNP3PT7IEJZLTuEqstP2nX4nrhDkb3NGw3QfRR584EEw9HacFmS8zpuzeZRvX2n_mNH69vRNtZ87MAF2ZxECGdlk8QRYJWernqZpWr4ZE5uShs2q4QzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ هفت روز تا پایان نقل و انتقالات باقی مانده و هنوزسرنوشت بازیکنانی مثل بارکولا، آلوارز، انزو، مینته، امبایه، گاکپو و پست مهاجم نوک برای بارسلونا و وینگر برای لیورپول مشخص نشده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28478" target="_blank">📅 19:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28477">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7rBi91eX_V_F6X9RB8DgLKyGMHaCQg8p9smsQ-puLa1V5GGJcid1GdVfL8RrWrwTFdyL7qCFg-DEmqhFD5EePLAyNjjSRHhiIlmeIAJypR8TD6oCHaKZOztD-g50rPYsT0dMgiuhJeeNwJThN6hbSbivUA04c_ceYSQ6yboA94iRPVSQC6AlM4QlI0l32503Vfevh-stPWM_OTrogwclQAHSXasXsvPR-du4lB8fCusVgE-bNeCCN9EYMoKXF-mAUREk6dqZn-8OpvIucOlEBryIzqG5CDA783wEDJEh4eBU0rstLWyhXvAOxCt_YbDXNI_F3vHj8Xa3L5QQ4H10Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28477" target="_blank">📅 19:13 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
