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
<img src="https://cdn4.telesco.pe/file/Qeii4NzLuQgA_6lBU6I2ZtyLJ2l7QmCL4u86M7YoAzZmMw1veTiWwZ-YJKVcn4ji18kfdCALWBJpat8UZudBHejaNXtfcxcBHvIfPvYMeziRMd0sDEsV324rh7dA0UZHd1xzxfC-1wOvvHipJ_t0GawT46IwhbB4r_8j5DR4mwGbx-saIYaHWWxL_IeaNKd-qjGr4ea0HsJ-roIKKbg3btKQVoNfhbueDMV8__cUtfPZ_c5BJMmL5WngYUwVBvhVyk-gaoHa6fWpStJspbQEukYXS2SIHWZv1NG4exLWnRwbt3dlRhM9Rp3h84oaM8fKOvZk36mVwCmBF9dpyBvmEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 616K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 06:01:38</div>
<hr>

<div class="tg-post" id="msg-28776">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=c6g1EeNRIes_emmEd2QqQ522xNN5Le9SYygtP5eeU6J181OFi-60w-dac2fdKln47XVw-nROzhxL9ey2RwSaA5ZV__aMIPzOnPWLFC03ROsquXHmph9S-SPBwjYKX7p5a0an0fUeBFMPwPOnUtnjhyeWyKum1NWM8GKtaZQWsWDYXCKC3SjGBnnJ0v76R20Hb5If_Ri1xVWiHXiumA1lHggEFg7mzocTdXnltRz1e6cQnCFvZtiD2CJhQItoXJBUT5wlTS7HjCU90IuutMwyns8-y3x2yVE6mnHmW25MYCisDmlFFb1rIQNuKMeARZN0q8GzpZmZpJaqOf5tw-N0RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=c6g1EeNRIes_emmEd2QqQ522xNN5Le9SYygtP5eeU6J181OFi-60w-dac2fdKln47XVw-nROzhxL9ey2RwSaA5ZV__aMIPzOnPWLFC03ROsquXHmph9S-SPBwjYKX7p5a0an0fUeBFMPwPOnUtnjhyeWyKum1NWM8GKtaZQWsWDYXCKC3SjGBnnJ0v76R20Hb5If_Ri1xVWiHXiumA1lHggEFg7mzocTdXnltRz1e6cQnCFvZtiD2CJhQItoXJBUT5wlTS7HjCU90IuutMwyns8-y3x2yVE6mnHmW25MYCisDmlFFb1rIQNuKMeARZN0q8GzpZmZpJaqOf5tw-N0RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌بسیارزیباوارزشمند ازهیجان و استرس مادر برای پسرش حین کشتی گرفتن او در جشنواره کشتی امید سازان المپیک 2032. عالی بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/persiana_Soccer/28776" target="_blank">📅 01:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28774">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc559k8gMYUsRPVJg1hh2Hlsz0uylS6WSg3XhgKQlrg_lMVouGvkrSqjDky_UOoComtVbrnYu6r2R_1oYl8zXM27Y7LyOd4J6bXOnHOjNVBorzxdM4GcGSagG4U1KmKf7OmcfO3BaaF0EmDf4zTLYF_fFb5Mpsr8Kc9W8gR7T6rPAaHuFMKf2DhyiFax7f-LLsDGsdGo_LovVtJ1EpZQOQnTNsV5q-L43f31PUiPBneahoybJ6FZ7Zzq46molPqsYZ59ENBhqcTgAvaZmghNFVNzCeECLPhoar8KovUU8HVU7h38DwjaIb_yGtJs1gyK4U1xgLX-3Ry1sZ6KhVnu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/28774" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28773">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA-r0dwY1xv4THZRrgzVzmtWHfPpJSXTSjlH5v2wrgLRi_jip4HsDFu1-rSUOW5e0TweBv8UITXsVI0IloA7Dv1Kz1MkGj0WZUwRywAg6uvLsTHtVPhFgu6iTE_GOxERILZEqOem3YgeD1TBc3jyvyKbPCMfanIsdDnHzUvmn0xWyP9gYUEzxzjatsh2IgBSNFPrkTHYq1da3DUdUtA2vNcS7_Hy6ABvIPi5XcNkimy8l_uRl1K_zGFfgjyYGNzlqRGmg4AkMAG3Q3c9wZGRP9KscrtpEKkIO_lybLUFZOW4IlRPgcnsno1StyXgP3wKYXJihcBiBpYhzWwCkbAvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛دوئل‌شاگردان آرتتا و امری در ویلاپارک و جدال کاتالان‌ها مقابل رایو وایکانو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/28773" target="_blank">📅 00:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28772">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNgMu_rvyCwf-6sbUxtEJh--h6OSToF2tb5DHAsuKG-jBRYl4U9ve6S3_65_rXjWBCIGNaw--cv_H4eowA2xgkFfVAOcXdVXTaRRh1K6PrC1vTv8CM8lVPDeH7zp4Cn8-yD0uYSI9XAQRs1TMyXXCRiowa2_pvIvMLEPWcPQjCqZ0bw4bXzHb1BAuB7tjtVkBhJJE8OoxGHxCJWzs1EbhcQO7GxZftmZ6uSZAldoCi6CiVq--JHlVjhQmaMTbtZwN0IhbuNaOKTDP1zEqVH-LZ3FfCPMhYv_ZT8kpafHfmyru238iYWU1nBPHZG9yiPSxlOE_B0fxe2BxO67PE_sNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
از آتش‌بازی لئو مسی در MLS تا برد دلچسب یونایتدی‌ها مقابل ایپسویچ با هتریک برونو و ورژن آماده کهکشانی‌ها با ژوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/28772" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28771">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3fcjE_WCco4htmU1BJCrTUhCpxJxbBiAJTC5bx4Qehbmo-IzxGdP_70vEZFWWsnd7IvMrRG4O32BdIPst9vLgyDSzOZXB-iNCpPxObGSCPdjJJDiW53XmyDKnkgHSVPH2tnAtI4XKZcM_DaihDvisuD6g1DqowGrShNaJsE9bN9CTL_XP3l6nSrPkgMpJkbafTDD4a1UfG1qrnsUIBSkcQctadzafXrtzbh6-t-lVUmJGQsYLIPcRM1YGqOFFobw_4QW11n3Pq3cizAc9xjitwlfoxgEx78a5J_vn0aQxTZzka8RlISQN_gPrTHGtTDyLkEf3d_3e_xd3xPVk9lIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/28771" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28770">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
نتانیاهو: من جمهوری اسلامی رو شکست میدم.   من روی این هدف متمرکزم و این امر ممکنه. اونا خیلی ضعیف شدن. الان روی زمین لغزنده‌ان.
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/28770" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28769">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT8BzmYXX1Zw_D-1OI8iqGtpULm9CQJrny4YiPwqCV_FcplqGucp94ogIM3T_pp7VZNPy5wJP0XIPxys9CQBP2oMLSB2M6RW0OHEpEnKBUwqzTo7w-p1p5p6OefpqjzwbhNC1LYxFQkc5-0miNsk9frs00HWmbgeWgUal9oK7h93h00e1vVcgRFMWOb28fj-jef_4im0Vuq9b0EHCfBY8INV9IwhiZIlUHmwgqHTAIuDOf-6ZlZvbCkgsrXpCUekeMZMvgJU3Mw60qvqym6ewcrC2o3kZ8MYP-yqsiD9tcp4PQ5uxc9dJcc1NXse7dMcIouKxV1nYiNa9cuXDUqfUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔵
سوپرگل‌استثنایی و برگ‌ریزون هاکان چالهان اوغلو در بازی امشب اینترمیلان در هفته اول سری‌‌آ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/28769" target="_blank">📅 00:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28768">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0iCcYbX2C9Y5W11vrVIrFjKGDAG9fGgph4N3SYl5JqxhB_HxVB3QbzBaqo8U6NcICTWtCo-poznLDdhdMIMWjii8y0-SHud6Mveyt3pNmmCBjR5Ts33mp_FKXAwKHe5QoE7dJCHmzVWF7cRzoNj1_TArlqJIZlfLASjcQXs7WXieHqOTF-BSfy1RCgje17wy2Mbp-M7biGh27UDGsukh1M_0arNiukPMvB_nWoxP65FuC04IJycqLEZK9oG0_hPYqgLkwXXR8yOe8_oqQpAEKSASyh-82zfnSTj8I17c2aboa-1zjSWAlwXZbWH1x_XHIPu_lgDw-ce_u6IAR6VoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/28768" target="_blank">📅 00:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28767">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcO3EWTVkuDe8nn4Vc3dBudm1cIqQXRubH45fJ2Fp1qwqCnRiZEGGsMx17KkIJt39o49LHYZn5X5_WnIDX0nexRSiGNMmEobkN_ZkDIiDcqP_eXsSvAZKe6e5wDybvuHBStPvpJrl-Cqsa1BCqtAX1iOiM1qLGj9fIeHCij41zL39p-OVRN3HFqu49KxGi1oENeLG3TPzxt1ekOaTyQo3UYC3C7d9T02Aj628RyeffVohw_69cJDh7cEVXnBO47vPSHJ_zP1ucaA6Bmi46CrBQbRU_o2ZTmuPurrhsjUGoZJmBq5iwSTnM-E7gqNhJnM6zR4QRolkjSmqA8RujWX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هلدینگ‌خلیج‌فارس و بانک شهر پاداش ویژه و میلیارد برای بازیکنان دو تیم درصورت پیروزی در شهراورد حساس و حیاتی پیش‌رو تعیین کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/28767" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28766">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8zmQ-gxwyqdOrjAqlY6ybZJUmNyL59ZDhoZVT_hNHbdf9ihZEUmJTg8R7LLArOu_UH4V0ypE1dPdcvz_MbZViiRJihVeB3Ok2sMoD0VGpKU2W5l1oBegqJqomgut2oHMNyjvHvdaDzLqNiEO-mCgHzBsj6igqu0I22sACl0KhW4rdl1ucVCj6pGysojqwbanS-PpCJclaGWoaIu4Nwcq6l-PM6iWVoMBYKhETx4qaI68PuUdeRpEPMvP3Yc7m0-LP1SKRDkyI4LOxeoRyzz36dbTblnBUziU44DHhqCJg-uO01UCH6kpuJW8dZwkwaks02_b3vSrH1Zs2jsHekSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
گل‌ های دیدار دیدنی و فوق العاده امشب دو تیم منچستریونایتد
🆚
ایپسویچ درهفته دوم لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/28766" target="_blank">📅 23:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28765">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuwsZj6QaKrAcnxsKS9IwBl7rpaY57PHvZr5luuNG4WsNt3tJQZis5hH4wMs9goCzGNqsfs1j9BRD--Bjbyqo4GUped0EgTnh5Y5MWpLUxvM8Ex8r6WMq4vYrv76nQpEa3lz5xLMB3o_Sqm9T2cuQc8sHSOdcbUB6wOYthsBAffGC8GcUaRokbf7w5g1Enoo-A5agm66zdsbBqtkT69aHzxbSmLWFfZhg7eeIXTfBWeJ65NQ1WYKIOQXjKSVe-blNGcSbl8wLbX0_1fq8LPXEMazI7JDpHd0EoHDJnwTizUvXPbT2BuNf4eStAEfQ_BchHoXNuxpj5tUBdNsenr_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ امیر عابدزاده دروازه‌بان33ساله سابق تیم‌ملی به نزدیکان‌ خود در تراکتور گفته درصورتیکه جواد نکونام سرمربی پرشورها از او بخواهد حاضره درصورت‌جدایی‌علیرضا بیرانوند راهی تراکتور شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/28765" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28764">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wt3M73TCZRK4j2XTG7Jv-lU5Gy3r68YPPaXOTy98q0mZd6cxI8lWVjQrptW65G6lWJwTfKwORSbdnjmyhzSR01iWCvZIvqLHrtBC7nbiO0fYg-mEcjaIg11KRW0gKnF4WWakNXYdS7Jv2tVSbkiMao2NTnht85F99ZmpyB2DW6e76nhKONb5_J9D3toq4Pntk__kQ592j5Q_52CeQH17DvX1AHq6Jq7gUZlhd6AUl0TLD9pB7IGBYwNdpcc_EM1RbRYTgBTnvNOwanNTeDNbFhF_u2_YPZv70EtfX7Cdm7UMAzWXGDj3Ig1_u1fAorONEolGj6bhBN74ZxF6kWotsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/28764" target="_blank">📅 23:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28763">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c007350.mp4?token=ZfMt_1TBDyWecigY2621JeLU6G-5AJVdMTFdwmtIOC8Z1P03ipLU9-bwgprgCHkQgMZMHX1eZ53Uo6A7m0KhvGq1ddXSCcLaAmK3DnCxHsndJ8M-FRvDptVLSoZ8eMNislwJYOcL8uUG53WQ6-7eJj8umNft6emdNR_-xJrqvYdfX7PWIlzDPV5pSXPcZ-OUGHw8oX4Hr-iQm6Knk90jYYCXywYO7GMTEVIxIEOwNhnBlitvO0doyKEyNno2LdcPU-TyuZiXCJiS-uWNqRMQO5UXyhv5lpzvwdgheL4oXpJ4pilqhlgwrYGGo91rIAMgmUSDBXpkUmkH7LY0HRBLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c007350.mp4?token=ZfMt_1TBDyWecigY2621JeLU6G-5AJVdMTFdwmtIOC8Z1P03ipLU9-bwgprgCHkQgMZMHX1eZ53Uo6A7m0KhvGq1ddXSCcLaAmK3DnCxHsndJ8M-FRvDptVLSoZ8eMNislwJYOcL8uUG53WQ6-7eJj8umNft6emdNR_-xJrqvYdfX7PWIlzDPV5pSXPcZ-OUGHw8oX4Hr-iQm6Knk90jYYCXywYO7GMTEVIxIEOwNhnBlitvO0doyKEyNno2LdcPU-TyuZiXCJiS-uWNqRMQO5UXyhv5lpzvwdgheL4oXpJ4pilqhlgwrYGGo91rIAMgmUSDBXpkUmkH7LY0HRBLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گلزنی‌دوباره اللهیار صیادمنش برای لخ پوزنان این بار در بازی امشب این تیم مقابل تیم کلاکسویک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/28763" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28762">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKEFc-cRQ3wXklcI-LVMVwB2wk5ujgLyMjJpIgOf5V2wXwlH-NXHHxLnxcCfYDysbeHqlpYxLuLgHdCyl1dDoaILj4I5CdSncDWvrhDg6om9mBGQ4b3E9Cg8P_q5JWAxBke2BUuVtEZ8o3e4uEflLnK0z2ZFBEJMOY5rvCn6YDBWRLNar893pnWXcmNwk4hfUj2B87FB4UTBiD_MlKLWcjiSoC6a8twxajNpAl2JYWHvbU5jguRmZRIkiOf0O8J7R4rde0V4CYjsCqjnUSel47v-Ns_H2sTbPcIbdEW14PYEBhLIsn9IvOoa6WofsrTF9gBNgOR6_dIebxIRmo7jdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
درفاصله سه روز تا شهرآورد؛ کوپال ناظمی اصلی‌ ترین‌ گزینه قضاوت تقابل حساس و مهم یازده شهریور ماه استقلال
🆚
پرسپولیس است و اگراتفاق خاصی‌رخ‌ندهد ناظمی این دیدار روسوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/28762" target="_blank">📅 22:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28761">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN1dN2uEwkVuDveWnhoOz8yX_W1rgTaxSaKKc2vJv1YpyPMtzg6PESkdxxXJKfw8XRvylDeKgRwiGRV8hkkehS67ZgGV2Gtyn_8VArWL0x9v4SzOI0qN2f9mYX-72SLOOeq9N1rvqOo4vXQqII_D0uHxeNSOEOfqQ2mcfM5JGYkpRjLCjrhjgF_AsZcbbPaUaP52eAxB0XXsXzN9GXc5yJMIWZFYv8sP3e9xI-I0jJNua17fSEo8CqVuTiy5ohCdjy87xSGlMK87rb8p0zwfzZPHSu_zyr8askL8b9zfplAsJu2uW03rWiM7cLXUW3vWMkHNN11AgOGsC15wC4R63w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/28761" target="_blank">📅 22:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28760">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=hk4dgdvhTHRvVgYMmgzxoYngsDQhB-KHq32rpDuCSugPcptDesUrArVsqDtzZ5pkbn8aSfQkFf7hAesU7kQ9hwLpYrH3ybU3ChcywIZIPhJkaxYO6KAPdJTySPM7Z68ya9lHBP5cKZagifrGPSTSKZrF5AqjeqfuY1Gj-3637FdtlW6ZWeoJCJDz7_L618PVAmj4TUrQ5fSEAuSFj0besu50IR8jW-maZSVu2cKA6tkTtvmbeQ2bbWsn8HIZxq1OJqu9qvPY5eYD0f9VWvxYu5TVvaMAFtbNDyHxPWrEGvyz3debaaqCvj7lGm0FH2PIcuWXV734C7pJv3iW7A-Gfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=hk4dgdvhTHRvVgYMmgzxoYngsDQhB-KHq32rpDuCSugPcptDesUrArVsqDtzZ5pkbn8aSfQkFf7hAesU7kQ9hwLpYrH3ybU3ChcywIZIPhJkaxYO6KAPdJTySPM7Z68ya9lHBP5cKZagifrGPSTSKZrF5AqjeqfuY1Gj-3637FdtlW6ZWeoJCJDz7_L618PVAmj4TUrQ5fSEAuSFj0besu50IR8jW-maZSVu2cKA6tkTtvmbeQ2bbWsn8HIZxq1OJqu9qvPY5eYD0f9VWvxYu5TVvaMAFtbNDyHxPWrEGvyz3debaaqCvj7lGm0FH2PIcuWXV734C7pJv3iW7A-Gfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
هواداران چلسی یه ویدیو دو دیقه از عملکرد سانچز در فصل اخیر لیگ‌جزیره ساختن فقط آهنگش رو از ثانیه ۳۰ به بعد گوش بدیم. این چه سمی بود:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/28760" target="_blank">📅 22:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28759">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZJbRrvzuUlXsETghSdfw3pFgA-pwVXS6FPPltsx6QOmRAuH07D0SwltD-wMhMoLoVNc0HNbQMqXTXrjjndvPiU-yzke4hpFtn9KKk8lWwlGkGJR3lksD6cjJXjYsWVKMsIoG7QIG0oVJGlaPzr5XZRngMeSvUqNO-sgT8ANwUrVh0IUoNwrmOUTLOb-z7TUXd4beqtFD2a12AFm6uXuLbQ34yT05jHbcwVozxDwz9ufMxum11AHfz6uJM6IPykhHmn22sVrMhpEMqs6_fBn7fOxBgSHmAwgCYG_hPjo-Kv438-LJQwxPuaiW92-HlmWSuD_M2SJUgeOpPHk0BRsAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های دیدار امشب دو تیم رئال مادرید - مالاگا درهفته‌سوم‌لالیگا؛درخشش فوق العاده جود بلینگهام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/28759" target="_blank">📅 21:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28758">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8ljpQmG0PmcjJg1EWUUFdTEyhBsz-tJ7Irwy1veeNWcwyOgQb_wgqc3pNRmhgYwH6uyLHnu8kGU7pFvjN9X-oMhWHgTJtkt0MPyjUgT1FaP4_4Z_JEqEc-VQS0JQ0r4nr0znnRG4uAiLhfjcPB7aI6wKbSAzRDXnubOZGCzugydzHZeCViVJgYFvK1iQ9bpjc6SPRkHya2kS0QCvsj5nxcQYoFs-Bnaa2CL_rEuxLWe4B3wxMAhNbNOh1ZI6MnGPO-a6ZnRp3xIN4QSGHBH4hqFcmJaREwQVM-hTWXB5ASDn0GjIAKAPeikyAIulOyB97DyibaSJCKbXB9IMnY_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28758" target="_blank">📅 21:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=edVgMp_8Yc4niLfSasGHl9utvgs7fu-kOnSWwq5nVOgzwZNAbH03Ok7WR6XgGJy-8Modt2ksaqCFm_lFZID1nQ-VUqVhUKr3kHzE9m_BD6FQHFqSM5igHIdOigQw6minKBzVIKazeoK6dpsWW0RvzxQNL7x4I8S_dp4tN7uR-7kt4PrHgXsdvISsP2bLbjLulCBRCmYdhMX3DJ2iJlneN_M49CE5hUNiVJBC6xFHmoH7dmr2u2XnyVO9hf9uO3QE6PsXiKcNEOZiHQxysi-PnHYfI4Fc5eG6AwTHJVBzYvyQ6OV8JZzo6tbVvfkF1dL8LYHfzKKaKk9qGZh9SXj1nYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=edVgMp_8Yc4niLfSasGHl9utvgs7fu-kOnSWwq5nVOgzwZNAbH03Ok7WR6XgGJy-8Modt2ksaqCFm_lFZID1nQ-VUqVhUKr3kHzE9m_BD6FQHFqSM5igHIdOigQw6minKBzVIKazeoK6dpsWW0RvzxQNL7x4I8S_dp4tN7uR-7kt4PrHgXsdvISsP2bLbjLulCBRCmYdhMX3DJ2iJlneN_M49CE5hUNiVJBC6xFHmoH7dmr2u2XnyVO9hf9uO3QE6PsXiKcNEOZiHQxysi-PnHYfI4Fc5eG6AwTHJVBzYvyQ6OV8JZzo6tbVvfkF1dL8LYHfzKKaKk9qGZh9SXj1nYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛ من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28757" target="_blank">📅 21:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKHipfXmbp8sZ-1dtpZUnYYFuH9oX8gpoX2R3DSyQH8ao0Gknkidi4PsOVoqdPr-Zho0EUoI4y8JyZA6_WK19pH5AniolvnMg2mpb_Bkn2uM2Nj5858nvRdSMt3gf5YKF25bQey_x6PWE8Vu6uiKzNxDmdEAIXq7Eu2mzA0ffX7sHz9rTroDHgRWoCnoEzjZnvaKhRpWpZToYfaT003Y-uoNcSVL_cRtEiMHYxMGYZx8pUtGW-zPyMo8mq39kLbr_QCI6EXjUZwAA_T_RzUHbDirf8BLmw8Gac-BEpS0cWAKcv9XK3WNbkFJ7ovML0AvMQ1igMfDedffMFAvjWcTIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛
من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28756" target="_blank">📅 20:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28755">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=XUzLDy4fQje7XrwN7jCbnBnLq2WoihiIM-GA_9Vn4-MdZDZyLkdxYPB259D30KrdSxSp-Zrb2pVWNh51b4li5UKj0PiZz_CVxjF_WtpDV4HU3GaVJTvzDuWYm0Vv_LodVFSMXVDwO1W4LU9_rwmkvUICIh_6h6pAXXn-srxkEQHscMejCAqZ4razByce_D7AZ8fvpYJ0HhpV7O-LKhw4ln-S1H30ypikvd8WLO3shcB7iPoHgEPXXBQ6Jxbx_10XdaBzDEbY4vYpXsHsVaysk6zbmEke2SJLygepPWKq2n-4fgqyLX1c5VoVO9oHo8vlk4HvWYnCuzo9cyKCWQygOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=XUzLDy4fQje7XrwN7jCbnBnLq2WoihiIM-GA_9Vn4-MdZDZyLkdxYPB259D30KrdSxSp-Zrb2pVWNh51b4li5UKj0PiZz_CVxjF_WtpDV4HU3GaVJTvzDuWYm0Vv_LodVFSMXVDwO1W4LU9_rwmkvUICIh_6h6pAXXn-srxkEQHscMejCAqZ4razByce_D7AZ8fvpYJ0HhpV7O-LKhw4ln-S1H30ypikvd8WLO3shcB7iPoHgEPXXBQ6Jxbx_10XdaBzDEbY4vYpXsHsVaysk6zbmEke2SJLygepPWKq2n-4fgqyLX1c5VoVO9oHo8vlk4HvWYnCuzo9cyKCWQygOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته سوم لالیگا؛ سومین پیروزی ارزشمند و پر گل شاگردان مورینیو درفصل‌جدید با درخشش جود بلینگهام و امباپه.
🇪🇸
رئال مادرید
4️⃣
-
0️⃣
مالاگا
🇪🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/28755" target="_blank">📅 20:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28754">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bm1b06vymIBDN_uPzNEu_z1AAzJqzS2ifRfu8XCzi1RfAQNQWLB_qpjiMIMeeCpXZIaO86Igne5UjGM8zmY8rwl6sht0PTLABJam2KGCMaNFDaxa9qgUOCzAAE05GRE2UgFeSy5RMsQqdr3sGRGLtEgBBrujxsn857U0lGB1kIs9oDZk09yycmVIGqT1mh-9etXzj8YO-dOwmYCudopLKOx24N3U5Ykeu7hjaEDf0HIC2m0DqRlpS5BIki-jPstgqbSc6Wl9rquisy01jMMtso4MzZm5AeeIbHlIWFVOgCBh1vbZywpWfNFFXeSzHdNzefbN_JWb1xFBEKmhI4Evpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ دوست دختر جود بلینگهام ستاره رئالی‌ها تو ورزشگاه برنابئوعه و قراره بعد بازی دست جود روبگیره اون روآماده مسابقه بعدی کنه. جالبه از وقتی بلینگهام باایشون وارد رابطه شده جود عملکرد درخشانی درجام‌جهانی و باشگاه رئال مادرید داشته. امشب هم مقابل…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28754" target="_blank">📅 20:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28753">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1KW66FJC7GvgJKA9id_dmfAlMsefdiV3_aR18sFeNAqwpYit1wuY0AdzrJNJZE5CsEROqjog_HUlR15u-wBhbmvwc1oVudHCm-Z7Bw0hfMG9smVv3BYAR7b5dKwEFxvi0KnGXv8_m8x0Yrtu6-bIp31O_MwbfVjB_nex-RFi6Vz4aVhtxs1aBxAcwBClt7shRaTaW2uxwguAKA2rRFF3uTNQmrTqGzlNyHwY1Ke0KGwhMjq1QYCrNBiEtmbcy6DFTTC3XCmnxsbtstq4ZWvhvinl83OoRZnvB5Ca8gO3R8F9JF7kREKJoNOGluluSORWTYAm0E4Ubg3IMLFmQDGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوست دختر بلینگهام ستاره انگلیسی رئال مادرید و یکی از دلایل اوج گرفتن این ستاره در بازی‌های اخیر در مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/28753" target="_blank">📅 20:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28752">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6tlxeHm4tn_xbButMZAEb-LPQbqYL1jfCQKuAxUq8T5RZh2rZxvEf_9vm1kNAaHNkQ-7hDZYbYTTA6kfCLNGwrFaLCFpKlyWPMVHq2u9DKWU8eStg9C9WL6L5sAoFVO_YdswFQsW0oViG92evCqgEZVKCuS_D4CIk8BJcCEDXleyuOShYRp52LgLIklmFgzxQ-5uEzSlUKhzZ1wAwGzuYscimSrLGIlBemElVka9iFVIlCELpe0GsAlcN7NU6_9M10DBcvZBOfkgK0FMVtKVS1Y2PYaMCCVf4_yalLWI6ZkluHYp9V6AffDf1rTMnfwogmZvECbEEstpqawrWkcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ اولی واتکینز ستاره آستون ویلا با عقد قراردادی سه ساله به الهلال پیوست. عربستانی ها برای این انتقال 60 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/28752" target="_blank">📅 20:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28751">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8u1pLifQBI64VYVNeRm4pqVvsybv5XxFJEwErghky8va60oHwcryHkUqluBQK7TL0JOdIpclNReyxyDeZVPYmD1Gb1qHxdnWxEk4HKED8aQpJG33_Bw9DEDd8esl3ChZy915IHTSyFZbkYQq9vEdlaVOcoq-0dRVhrKLbIWEJQ_S0UA9Gl4LlFOaa9C4x5KYbqdIRzHkYAWN2Vya3elYndpKlTcGRpzF1IYlhD-e035TX598r9mOvAZ1-RAiMhgr0ohzz2FAemCe-hqmJn-1Kso90jNPzIdR_OdBYOBNwoyY9ah5O70zKcBHLhuQcnuQpPFnM9yC95BuqpoOzaT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28751" target="_blank">📅 19:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28750">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=vJFe824170nJmZHHN7VSq7m7dRggJTV6MdhL72F_2l8wlxpWgBedpItOR6k1jF76NMwh4VZMwYiNtLIxPBv8p1m2Oh0TJ_nvdDAbZuhsLYZCW1PFrqZhZbTMhCoQJb9YaXBRwozO9zIXp61WvGmTJROEKRRvN7mmnYG1rYosD3ql-XUj6x1E4JCsXxS1XEbb8G23fTwo3bEUJl3whncDqscl9TYQoiBmNY-gMeNP1QF2lV3ZWk1x9FaOCO5tktB7yHYEvQ8gmEMjhl2h_jM0_IpC0tjhjSQdqh672OEWOvqFQQQgqORZ8uKye5WqpX8qTnapk6hD_3MvLC-mcC4eVTqKTGEHUeNDnQyxoc3CFWaHzcjPypiRFYMSzPECJlyXTYlHCT3npLOU31nE8dLNeGxTIlc_kPPhmNCJX4S7JKgGRK-f57ffz7o_t8kAK4cUf43ZOgVhwPovKZw-lwXp-pdToE32UPzVYYAQNJ01-ePzZ0ruLwNlbFEFnQe_vDhmhZN_2vHlVakwZbgEhNQUuOjy3TKa3zDHyK0-FwLyxEDWs4Qyg59yoP5DWxPAT0G94QnWqksMcJrKGEZtSsGp0vfseasUOLzHYgQdrdx2MZmEBGAMj7UF4mC4KcsPVsKa7MOSs6bDUPN94SgQUy9iyiyA-0t6BH5I5ew0I2XZWFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=vJFe824170nJmZHHN7VSq7m7dRggJTV6MdhL72F_2l8wlxpWgBedpItOR6k1jF76NMwh4VZMwYiNtLIxPBv8p1m2Oh0TJ_nvdDAbZuhsLYZCW1PFrqZhZbTMhCoQJb9YaXBRwozO9zIXp61WvGmTJROEKRRvN7mmnYG1rYosD3ql-XUj6x1E4JCsXxS1XEbb8G23fTwo3bEUJl3whncDqscl9TYQoiBmNY-gMeNP1QF2lV3ZWk1x9FaOCO5tktB7yHYEvQ8gmEMjhl2h_jM0_IpC0tjhjSQdqh672OEWOvqFQQQgqORZ8uKye5WqpX8qTnapk6hD_3MvLC-mcC4eVTqKTGEHUeNDnQyxoc3CFWaHzcjPypiRFYMSzPECJlyXTYlHCT3npLOU31nE8dLNeGxTIlc_kPPhmNCJX4S7JKgGRK-f57ffz7o_t8kAK4cUf43ZOgVhwPovKZw-lwXp-pdToE32UPzVYYAQNJ01-ePzZ0ruLwNlbFEFnQe_vDhmhZN_2vHlVakwZbgEhNQUuOjy3TKa3zDHyK0-FwLyxEDWs4Qyg59yoP5DWxPAT0G94QnWqksMcJrKGEZtSsGp0vfseasUOLzHYgQdrdx2MZmEBGAMj7UF4mC4KcsPVsKa7MOSs6bDUPN94SgQUy9iyiyA-0t6BH5I5ew0I2XZWFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم لیگ‌جزیره؛ برد ارزشمند شاگردان ژابی آلونسو در استمفوردبریچ در دیداری پرگل و تماشایی مقابل برایتون؛ چلسی بامالکیت‌توپ 25 درصدی این مسابقه خانگی رو از برایتون برد و رفت‌صدر جدول.
🔵
چلسی
4️⃣
-
3️⃣
برایتون
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28750" target="_blank">📅 19:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28749">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXtrz9r2AGmQU_oic1FMlaLY-2wnKL9KyqJ9m-9jnrjx_XZdkZomarm7gW12WNGcaJyFAJyPi21sZXBlejNeMvBkmqjgzUCpFeKCLkU2ucPfkIG_sERgDmGFVUOxMMQcb87h3dePYcjv7kSIhIiGr97C33JDVC2MswwAKa6cInUVXDbwtmqkEUcm17wI-s-r_q7cJyN-42YwEbWiAfWiQ6jf_FGWG6aEIIwJxHZkCDutL9ohDRh5YsI9beRCm_-Vs2vbxXpX0_MtjvWpU0SP7QlweIyqqWt_sld8wwgq6Mbx3n-TpShYRyFmhr3Hzo6N4ijWlnLlHi9kLekHQf4GXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب هفته سوم رقابت‌ های لیگ برتر بر اساس نمرات گرفته شده بازیکنان از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/28749" target="_blank">📅 19:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28748">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFnt9OPRF1Cec18Nr-Ewq3CbemLOZqelsblybvh1x56hkl4b0CrKVgXIjc24OT4rHbHYWdvsyUMh8O9fLH7ZUr9Iv6ffXac_-cfVrDBC5ZJGg4p3U3_SfyONyazIc210qNcs_pXm0nmxmHq0FpeEEBFfJZ2aybzzxuITqf1k49JV5Izl84DH436E2oFtrwsZtXg1k__GGTFDYstULvoN9xh4LvB_XwQ9i9NqoCpyoljkflLKVeilXrHLa7kRVM-EfKi5B3506XO8Skk1ogdEKkC4nIrPvMxEliS_yNZsTTWN9v1n8_NAZcdhsHeUnqdkwu-pvlSJZWUTnrKDJedkMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28748" target="_blank">📅 18:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28747">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeAYs4uY8JGobQVcMEGcFdUE4FKmD2fnXJdReN-USDp246QIHGJP239IYHQegVh_NevvKR4YHBUp7KUaLWxvJrBhwdycjqBnXhfLkt-j0mIklOb2w3trQ3hPZ971XI0L6bdHV1V6rNK8k_w9hyngq6b4dPW8anGV938c2doEySSyGGyrqqLcej7usafv1Z7AT_9JsKgvdFr6RFJksNkdbhEac8A9Mi4aKvxt2wC57zzLNFZaUDC-jQVDgcqS4M6tAghmGMPYzi-HF85QI_47aJcmvk-ykASd_TycA4IS9fbb_UQp84CQKLuGCzqKlmXNg_r14lq4P34Q5tPSrK-nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌جزیره؛
برد ارزشمند شاگردان ژابی آلونسو در استمفوردبریچ در دیداری پرگل و تماشایی مقابل برایتون؛ چلسی بامالکیت‌توپ 25 درصدی این مسابقه خانگی رو از برایتون برد و رفت‌صدر جدول.
🔵
چلسی
4️⃣
-
3️⃣
برایتون
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28747" target="_blank">📅 18:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28746">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad7e62a7d.mp4?token=EKaes7_lg3zhCdLevNN67dKGkG91OIwzDJ-foLfmEjdBjOXouskk09OEA299wLoSmGvNFG-hfuOBcia1tmQuiEDb7nigIVA0FXXgFBR-dBsyGLP21L2S9k7jSS5-VLgIzOsLyZ_oEyEDavz-fpTVYtgilCH-4itj8xrl90dW4rUqgsPGOLOleqw_tRyz8RjZEqH4HfqbcagdYG13HODxJZeukBqeYBSAGrTMbMGPFMMeP_NrhB6t2f3avbQKItFsAfiGctPjopZpnOJD9f-Ji5ciHsbpYcyv26SlpEU_zRoZOcj2QDm-_90LOJA6_sQ2NoP_M4J-d_RSMEfhz6uEAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad7e62a7d.mp4?token=EKaes7_lg3zhCdLevNN67dKGkG91OIwzDJ-foLfmEjdBjOXouskk09OEA299wLoSmGvNFG-hfuOBcia1tmQuiEDb7nigIVA0FXXgFBR-dBsyGLP21L2S9k7jSS5-VLgIzOsLyZ_oEyEDavz-fpTVYtgilCH-4itj8xrl90dW4rUqgsPGOLOleqw_tRyz8RjZEqH4HfqbcagdYG13HODxJZeukBqeYBSAGrTMbMGPFMMeP_NrhB6t2f3avbQKItFsAfiGctPjopZpnOJD9f-Ji5ciHsbpYcyv26SlpEU_zRoZOcj2QDm-_90LOJA6_sQ2NoP_M4J-d_RSMEfhz6uEAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28746" target="_blank">📅 18:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28745">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4JMvh6EQKfwQmKuv0i0EZqbx7VuQiM2EeuS8xalbWjTPBbTYh8gVRVBdbFel27jxwMJUPSoMKG6CbJz7x3YBmqdX6Y5RsB_ClI3wCbizxRjJmTmguYf0uXwTTOHa0z8HUGAbtEmn3vboejW9PU96c351xGRb4pYGrCoeIyZaef3Xw6_C9Lj9XVxpF8zzYvDmLBWzKwh5wQG2bqaKsFa5EjrR0U7bIhinzvcNfmIskratXphUu379ftgg1pzNPWX1iYnhORzmYyA3K9gEDRZdDKmRfPthAj2P0Ps3xwQ3Z3NSJELaAYjUfHReseRkMp-waT3BXEmut16eJTZRr8uQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/28745" target="_blank">📅 18:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28744">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKUjyAQGtlgj2aS5fuqwDSvq2VbF_PSprt0x4MTVcRsSzDsdqMkpl15Tk9UA0AyFXWuU4-xOY148CSEfqmosmV3d5Pf3KrVXmTi-kGRcaxhea_yUB8NDNPNcKRlq53TVIMqKM_EE1hvA2yaheoI9xlCWQZz4OrT77rOJ-QDNX_jrqSggTtO1ihQEhoIsjwbyMIwhsDhoQd-8N-4ft7RfHK9y55XQZh-RRKd6A2hvL7jZOs_V-ptIq1sKfxfEbfxT4bnus6WeU9U_6ZmaVycrMYleJj6cDcbMvyCGGMTOTQPlDsRZ6jQzaaFaWPp37EP_v8UNTTmNgOFsBuFuOnRO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه‌تراکتوربدرخواست نکونام با عزیز گانیف هافبک دفاعی ملی پوش سابق البطائح امارات وارد مذاکره شده تا درصورت توافق نهایی با او قرار داد امضا کرد‌. گانیف در حال حاضر بازیکن آزاد بشمار می‌اید و مشکلی برای پیوستن به تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/28744" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28743">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s91bSX1tFbzamGh5sxnCb4-jriA3W3DS55WMOJw2TZiqcssEQDHYo-kGmzA53YoGLs4Uuo-mdwE9DXHR_m-3v3JvRyz3cR5qoxfSocz1A47b_RwvZRdKPCpLuchRc9P769DpblrUZJ2Qyr2LSYeWrrYkqWTF6pY1B68R6aZ58XES_uZXSWbULkE6nh66wB-7Vs3F7ZiL-Kqy42TKQtj-1YzuUeFROhnfoS12VCtHN3z8FQXDShLWbIgCFJ4zo5q0DaP-u-f-7uMPxExlPASqxSHBfQ8Vp2Fr5soqmTKwhMhyneSIGtDwfwdISDoVID_0BN63R99IHhgUpOv_XN9HOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
مریم یکتایی دروازه‌بان‌شماره‌یک‌تیم‌ملی بانوان و گلر سابق باشگاه بشیکتاش با عقد قراردادی به مدت سه‌فصل رسما به تیم بانوان استقلال تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28743" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28742">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwPOdPYMNw0pFMbMMNbbHjzO2n5tahKM_2ycteGvZ3dsSfVDvhtP5oeRBxVD3eMWwznbrovGO6JqPJl9boe9S6_X6xgVsa2youiVbZD_aImCVooaUzmCZgAV0zmmQJ9P2eCa7BFKfXVTSj499n5ayGSPSQgswLX1_DwKEjxZV9Hiy2MJNXk81rCm4qen0yakZ2EHzyilsFecJ59GIwfMftsBC9tu3pWE39u1u9kZyKFonbs2AKKMfA8SGhKj8zpG_28VRLQWz-HivvCFXIQ50-Hwtol-jHAM1rBJvt4A-h2k1NhA9iTMmF1Pa_ByLg6_o0tR5So0cGKZ4X2P9QVMww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/28742" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob4kxLlWUjOKqYVcWvr9b90CPla6Ohdp__wPiclAVZDckxYKxSkP_NqLy0xqOh8Wf2TH9Qpf8Eqm4hm2vPC9SlNrgwFZSFut1I4DmnyxSE-7GJ7e00YMU1hZDSZbtoyYUuzHLEDDOshgVX5iRuG-U0rxxfrnoPwzUEicfewvgQkGpRH1XGmd1T5AgEtagy6gKMOYMrRCKJ1PdQ1cVZf2D2jbqxefvpTownqQfBDnFcQ1LrvJIwLFon1TJnZ1vRicrk-PlkExWBY7y5hM1Kq0LtfFloMgBMIqM-U7yCRKr6xc8id9lUtU0r6F7MtAoN8YWiLj7N6BIa7Bl33dcuwzmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
؛شماتیک‌ترکیب رئال مادرید برای دیدار حساس‌مقابل مالاگا؛ ساعت 18:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/28741" target="_blank">📅 17:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9Hswb_cs0CVj2XJq-v_Qjif5FI25kNKj5PnSqhwFCd2Tco2h_FFdJOk-ABW3DWX8eLwTUYgtic7aNEWUROU9uxoI4FzOpKyzffatrWiNGA3qqamYIRqcSZxz5hYNUgzGhtUIPsVSFfGrHp1kSmlBpjCzOwFWs5xPL1Ns5xX4ygbYPA22mPuqmqNJWu3HEv1lqRhdVuxTjvYAObNbdAtnn6KJpRKmp3SaJ1DkFtmc4Nxs6sMqAvyiyNL7beIfQWtAO64DGt7zlGfYc4oBSgAe6a-CQqVHK84ylGX_qEBxU0tXljsBt0hAKi7_HOKnYpLwhmOOSRWOIcCBuIzuO_DNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه حبیب‌فرعباسی درمسابقه این هفته مقابل پرسپولیس موفق به‌ثبت‌کلین‌شیت شود رکورد وحید طالبلو رو خواهد شکوند و به اولین دروازه بان تاریخ باشگاه استقلال تبدیل میشه که در پنج بازی ابتدایی فصل موفق به ثبت کلین شیت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28740" target="_blank">📅 17:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGkPBIcmRpQmQ2S8VlJs7UumaMA8m5mmz_MI0YDZl1DICSTRGwBb6RemJcnwReeGbiCQS82Sq-e0hq-nZHCbA__U6w1MOBKOoq8mMbL9euW17WH_L7ISbR4X1z0tjjp4P2kV0PR0uX2tNjDGIB42p0z62aWO5j_-WXN90Em4ghMM1lGnXCutYBrCXwBMELbhKjqBDHnwtB1xLyWIEFEoKE0g9PsxLcr0bpPbWI5TRixglAQ-V83g7Vgp_b5pMhnU-aYAdqQyc9X-5CUBD738Ws24TfIdegePFQbx9cYWYrP1xTf3mcq0VXNjtBqUY07Y6-yTYCM8jdZqdriavZxcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردحبیب‌فرعباسی‌دروازه 28 ساله استقلال دراین فصل: 4 مسابقه، 4 کلین شیت، 0 گل خورده، 14 سیو در 4 مسابقه، نمره 7.7 از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28739" target="_blank">📅 17:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTi0AxeliMdmRBQyZwCsuLEhYiHCTjxQ4RXGBVF98Iic_1nKkYUCchPxG05Tax2uk_a8bWx3qOUSFLMOSzSPLexCMFXOU-6qhV5T4yEPfsUQe99Wm2MbbiccCtA__qbM6Sl2rEMXRIUFBKGCMp8Omr3hBs3JlDaiTaFm72XQ4pft2mWXEeqeb_zaW8qxF8OYppwM-A-atT7CMuToOSP3C_xhAK8bpXhL8eOaN5e5iCwEU986YB4pktgB8G0GpNomfKu4ingHTuj2JP624p8k8JFq8L-qmWyFSrgxLftsgbXfbQYemZyHo1zXkxRq6JXGcZBhfAp8Vp5icyRjL8RWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/28738" target="_blank">📅 16:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FduZJIrKNGm7YO_w_RFXDWE4Pf8mpsaiQUCoSKQlNmQ5a3XskAIl_OWCIG9xWab7KzrieLcVtsvKl6fbUPxJokhQf8rSrbCTZr03yAs0NTh7vGoVD3C5fhC-0fozjVrLpw3qQo45F3nQGs9t6twFiuH57vGn3nVYbiRlqCjGfNZ-P_mgPTy2Oyr6iy1YAs8qsj5MJUU2qLPnlYRgXSBRlsZyBgZfpdhWO-jwMkS1W2yoM5dTP4uvIG0CGn5oBnGLBVluiIdyVWyh3CHo0exGMXw7aTk9QNUE9ik362wq8doI7vN0_8-5EAGJ4TpJN8LYY0D8Xi6Bsh7T6aejRZ-jYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#فوری؛ با اعلام فابریزیو رومانو؛ گابریل ژسوس مهاجم 29 ساله آرسنال با عقد قراردادی به بارسا پیوست. آرسنال موافقت خود را اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/28737" target="_blank">📅 16:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG7QOVvVFjpf5SecQsDXPuO78rYPAsg9r_cBz38UlDzGQscs5-lowAHgV3oH3VFm2LWupKv0duL212Vd6kg0F5y5zEypYk9UYGE04M1jUWiCBSSSLmMZvVuGS1gMiuiskE7frNgRf1k5J1zSdB9waAtIgKDbIE60VKJFPMSoBxo_fnpjm_adTxQNt6Un6EiZzKRDuf_86SsCODsTJ7XwqpjT7y5Ac02YyQYHnYnsGLLc4UUURrjhYTs8ANcPasG5NzJuDMfn3z36i0PsIxev8aHAaq5IQ6DiOph7Zlec_or-gfUsSvldtQ1RhqxHvbheN7aglYl5U9IqxJr8LMeM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی: بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28736" target="_blank">📅 16:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28735">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMlEWNOa_oLXKceQEb4LF00qHjF3_Aq3LX2qnZJiP_zY_S6eJM1M1yZ2xiicJgxNDGs-_qmWsiMRIbtvyVr_eW-iIWxUC3fCD9m4BTxHFhA6gLw8_j_PrVWkYDLY679EHVmYgbB6RHX9sJaz1cFEtOY-LQAeJUworLDqo1ul84fQI3E_3Ka8J5ixTy5g2QczSaUKKDu5LQU4QGHiewajWIyV5KC8nTie4Wuzf5HYbUDyqqAOuFpblQ8CCpa1Tki6P_b7q9jZncxsLfRTRZGsbyIa9eBRt2sHQ66dprHqAsJzxr7alo_EQZGH-q-oQCfykeZ1sm_sDjjfp8WlaWoW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی:
بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28735" target="_blank">📅 15:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28734">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6lJgw8hdSFYszg_Lp2iJG2twJV6ugXrtrYqvXvPA_OTDssk7ijH2uB1gQkb3i75atdR20diDpfhZGjyVCaN24G9f9AjAE7FLLyV5QtYuearo8qBvqEcGnfFYzbur4WLWgEbmTqtBmO-w4gTmrpFgTHkpdftEwFu5UWv6oI7UNG6v36gxGD7BKhO0qZ4gB9stF5mZ6y0vy4eMYWG4sdD_U4DD0QpPZpYu802I_x_VR4mUec-wDr066VZkH29lx66cjl3RgNUkNt801_ABdg1nzO1UyIQQVl-cyWEEuJl4f4b4TrQkfYrp_VvIm_hPjkbCU_ABDhDpCqLLyWlYfxP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی پرسپولیس در استانه دیدار با تراکتور: به جز تایم فیفادی به هیییچ عنوان بازیکنی به تیم ملی بزرگسالان و تیم امید نمیدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28734" target="_blank">📅 15:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFXiB_JfoSIZ1VhdHpx6m8ccPBZTft0Tq2jh_pZELOfeLXAFT5k567KPktvsean9EMZixxpE3HGw1cJjVLRRj9QdDxPRo2estOCXg2xTtMoNooDMuzdt3-F3wzvPyAKecgPlBcsEVrmfeq7d3XJPypr6mAL1BoyYtYyl3RLl9Lo5dNEGbM232ZpVMjpTnP6Tddl7CPxCr4rfBSF9nLyFkBVJfAe_z2H7x0tK0VNkJNqwIT7V5h2FZSOCKzkzbOQ5kR131EX9a-k-qfIOR1fHIfBsZQbzaiMOnSJLr0UvO3CpWzDCMTJ-_uuzx_xTLLYEmj2OO-chlh5KK2_DdNzidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdoBImd-nq9M1WNMgG0Tdy0m9fM5CIfC-Fp2hDfGcTgC9XPychqLQEflIaB9t2Eemurbd56kRSoH0BmdCjuL9-gzUSoGUsg0eTvloHiz2t_ibb0Hmo95kcMSE2Bd5Rz2QvI52VJr7wggWpQpxK5jVk_XQ5DiWU-iugLL_kukaASovUjjoiGf7mHJOMqU8P0yb-0GUkHLmVPuP3PStSOX-_mV8gHrvy0iTYHHfcDLUc9h2LqR4OlboZZxfEBGf196nGfBmJZR1wEdy9n5bLgnjyCkgYvd4b9TPtJcquU3YNMd0-KecvMgWJJyzk--ndRbhnvKuvfbKlsqItmTDUDzKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
بانوان هوادار حامی باشگاه ملوان انزلی که در تمام بازی ها برای حمایت به استادیوم میان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28732" target="_blank">📅 14:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgACXTdURjUHk_NFoXk2QJ6E0Wmfj5A4rmpYFofZkpr4PYG4bSf10FLC7QSUUk6O9Gv_a3u4NSDZyRHxwdzRFqbduSgPhIgTWb5TJimlcMZotLvJ_rTLlCWSXojWMTX3De3C6kLJv9VXuskud9xanTCc333CcMJl1rHxWJKCkSs_f1vWlW2Xh6Peb_BOxxIrrLBe-uzcDLh7FNwN5stwe0KiC40b8N1YX8xOMHa3pHyEV2aCLx3b_1vsA-__kRXTfcugaCUVDPbpc87x-FIqHp8ry09TtabPY93t1iXH-QBRK6Xhbk3DIGAhf-23pimEJmqU80ZA2lwSsPShX3CNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌انواع‌کنسول PS5 درایران؛
PS5 PRO که بهمن ماه 40 میلیون بود شده 251 میلیون تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28731" target="_blank">📅 14:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28730">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWo9ZVzSoSTxmv84y87O6aCVpflz0E3VhmQcNoi8tj3pHLy5XnOXiP_I65NyMu5yzgjXUJJRZZOEGegJNeJAA88vLpk05dJmrdtv9CPp3lIqONJNIqgnSTbqPdHsmNGqj_A_27kLjIO6NYw4bAA8lHz4ssLLQwsUOKAnTbsR-_YzQlq1OEmKIX3kxMexZnBvg1fedMaVTRct1uU6OPMK7qQEUdDlPtYovkJFfU-6iBUot9l2TmZeRrU_b0TmNRomn-pjeR4ey5i61hIUeevaI1IUNRcc35nDxtkWMffeIVv4zMbMQEzNmex5BrpSVfUrFg6YEH0IwJkCG2GiCJeQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
مریم یکتایی دروازه‌بان‌شماره‌یک‌تیم‌ملی بانوان و گلر سابق باشگاه بشیکتاش با عقد قراردادی به مدت سه‌فصل رسما به تیم بانوان استقلال تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28730" target="_blank">📅 14:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgbbL7Ky8eNSn9WqZ9m-zTeSuSLMlEpbWcV_lps2tqSTVopKCuDkYBbMdNqTGNOMh-zMmt7dJyVVCpQMWWJtKp11Nr1rg5zLDeGTppnIvpebl0bXJQKD70wpdrMpDgj4_vYw3e1etIByDKo9PaEid_QXmQq_0VgiSTIoFvldeJeoYz4-BQij8cw5dfBE5PyhcIiBPcMSsmmgnXq-p0q8AZdaQx00RvV_r1YZlb7kNROyM8srJE3UA6t1RFDmlSHT4zS1OyWwg8kGlpQCT-fKLdq7cwPyBN57N3uu9CtLAjsmFJTiw76Uq4XLMyyECx38DXgSjwdGpils8SL9sjlbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از همسر عثمان‌دمبله درخصوص پوشش که هرجا میره ماسک میزنه‌پرسیدن برگشته گفته این یه عقیده مذهبیه و دوست‌‌ندارم‌‌چهره زیبایم رو جز عثمان کس دیگه‌ای ببینه. حتی کنار فامیلامون هم ماسک میزنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28729" target="_blank">📅 13:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520eadae82.mp4?token=RTYkvIXflAU0ejpJWuiVgKqa0if7HUjr4sZEOYIYvLZ_3V-gmYJ-qCF4Ag0iAsiJLxJ_ei-kBK6dL88VmCVyqSyCexd5lsvZhm8_ZOX3IaXLmgDcwclv1z6wV63TLEoUOzSWfGvAkp6LO7TWmExq-nf7EdS8a-vmvWZjHnxjVmVyaDX2xUBonDBTnABgJBzUvv1GTxN8toJXm-xK9CgPgEzqhgGD1-C55GKEotMpLcNdzgzLltFJIRWtGViKHbqzPGDD_IbEfh9gcy9dfkEmRXbtG3O1x_SE8WrqMndXScm2Uto0bT2aJthrXvohG0fJhGlqn5lCVBKI6UrqpolNXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520eadae82.mp4?token=RTYkvIXflAU0ejpJWuiVgKqa0if7HUjr4sZEOYIYvLZ_3V-gmYJ-qCF4Ag0iAsiJLxJ_ei-kBK6dL88VmCVyqSyCexd5lsvZhm8_ZOX3IaXLmgDcwclv1z6wV63TLEoUOzSWfGvAkp6LO7TWmExq-nf7EdS8a-vmvWZjHnxjVmVyaDX2xUBonDBTnABgJBzUvv1GTxN8toJXm-xK9CgPgEzqhgGD1-C55GKEotMpLcNdzgzLltFJIRWtGViKHbqzPGDD_IbEfh9gcy9dfkEmRXbtG3O1x_SE8WrqMndXScm2Uto0bT2aJthrXvohG0fJhGlqn5lCVBKI6UrqpolNXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعودپزشکیان‌درحضورجبلی‌رئیس صداوسیما:
دیگر تلویزیون نگاه نمیکنم وقتی من این نگاه را پیدا می‌کنم. ببین مردم چه نگاهی پیدا می‌کنند. هروقت تلویزیون رو میبینم اعصابم خورد می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28728" target="_blank">📅 13:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCeuw6WNCvS6xfOVjAvy6rGNgAgcoOmLsZsF9nAfm-xhqSGu6gNM6D567nGBOiqvhDTo8G1HfDHAOKj7RfsLWcNWyh3qxWsM1LDhe744Sa8EgwjEQrhsAM_yeud_iINV-qHxzpdZ27TLgcD48o5j0XNVuxNEi60fYYkgxnjVWWm0tDFjgadTF2yUmNASjABxbXv0HDR4RP5wqcvrcbjnsy0Bk75brihFut1rtlI9GIYmiV1FPl-oiSRk9npOJ7PgpAdZEnYLOl96WpbffLLunj67Qfum9F-7vIf_IflI1gRxzuWN9kMqwc4lrfaNCbBrN8a1XC7Jv6YKKdNSkENPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
جوسکوهای ورزشگاه فولاد آرنا دربخش بانوان؛ هواداران بانوی فولاد بعد از سال‌ها بالاخره از فصل گذشته مجوز حضور در استادیوم‌ها رو گرفتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28726" target="_blank">📅 13:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28725">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">📊
تمام گل‌های هفته چهارم رقابت‌های لیگ برتر جام خلیج فارس؛ سیزده‌گل‌زده در 9 مسابقه هفته چهارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28725" target="_blank">📅 12:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28724">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yco4Bbe56wlgqUVMXcJJNimddwFUTjCTNTFKsg8j-GeZZctE7vTrnu-aFdXMTSb3N9sgDg9MoY9oy-jgM3YtXqrT3qgCM2xTxsqzaQ6ymc1DS48GG3QagQfp_0AixA4SufcsWGRENp7sU3yBu36MO6xZ-218uZWYqpXATtzkZ4DSfijwkYeiPo4Yaf0l18RCFio6NbJuV57P23xHEYMSZOJ1bU4FhVrFndRNdsI9YVLgn2hgUFf-y3I6sifz0ZS-iJGlRYRucXddRkFpVP_TdJe4e5CfVDVDbpxYIcjk8ynkVyXaeQ-FAv8XHsrhXVRIVCEXKkl-xZRpwpMdB6uB7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
درفاصله سه روز تا شهرآورد؛
کوپال ناظمی اصلی‌ ترین‌ گزینه قضاوت تقابل حساس و مهم یازده شهریور ماه استقلال
🆚
پرسپولیس است و اگراتفاق خاصی‌رخ‌ندهد ناظمی این دیدار روسوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28724" target="_blank">📅 12:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28723">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc627927f.mp4?token=DxmJELycmJNKR10km1q3P_2jREz6wiQSA25JQgMGcvhjtzRRx3fGVSyH2_rHvKFcb-otArigSz590r3X3AXt4MQoeljmCgbOQyzs7aUCr31kut7B_mNMIMW1VmTzBDH6Qtz4LL64MMMpnNCjPW9zSUWh1HRRrYM8FEB8mQCl7tLK8T-kXE4xUN0Eq09G5K9JDN9rv0XVgqko8-vXc_GPadp985wySGtCkyiShEANCTUmg-4IW6iOvr3F_Sc-UaM-kTSRCoABMJX3i2cqcHRe0BZJWBkXy23eWl0aKGIZlZL46Ai0pUFmdu6dE8hQoxBnsBGmbFvAZGba5rRnzlS_FYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc627927f.mp4?token=DxmJELycmJNKR10km1q3P_2jREz6wiQSA25JQgMGcvhjtzRRx3fGVSyH2_rHvKFcb-otArigSz590r3X3AXt4MQoeljmCgbOQyzs7aUCr31kut7B_mNMIMW1VmTzBDH6Qtz4LL64MMMpnNCjPW9zSUWh1HRRrYM8FEB8mQCl7tLK8T-kXE4xUN0Eq09G5K9JDN9rv0XVgqko8-vXc_GPadp985wySGtCkyiShEANCTUmg-4IW6iOvr3F_Sc-UaM-kTSRCoABMJX3i2cqcHRe0BZJWBkXy23eWl0aKGIZlZL46Ai0pUFmdu6dE8hQoxBnsBGmbFvAZGba5rRnzlS_FYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس‌جالب‌ازسریال قدیمی فصل دوم ساختن ایران و رفاقت باحال امین حیایی و محسن کیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28723" target="_blank">📅 12:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28722">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8B4CXHrPzybenEoZGaleDYy5fPDKS7h7olhlaBJcrlTBcef0lGEmfB4BFY7DIrU4tT_ploLPa9Wmo16qIjFcnH21r3PSkMwojnM-lryQVtCRMCKHxKgha8gY_NCpIp_k55hNUgOSOWwPsEyQFb8n4OWkD3lGGwpO5wevXDs3ADa2zv24XC-5FbddmszcjkU-c84_Ahw4BD1pcwiZybFcfZg0KapK6_vzvsh0Rk7TO9fSRP141aPiWUQRynnwrR-3yU11XTyntbm2z7RtSgzVK9Jh5thV6LmG5CZpI2v2iRJJQrI9Y2s5mgau8N3YGj_Ow75WtlgPkdJqF-xz_dc7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
ویدیویی زیبا از پوکر تماشایی لیونل مسی فوق ستاره آرژانتینی اینترمیامی در سن 39 سالگی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28722" target="_blank">📅 11:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFDUezmpVWoihhV5OiO4MDvKnS72PyqepGFE9Qlylgz4i9amw5DhwNNLQOFeE50CRXZDtn3h2z_85xBjmgAbI3gvP3yUwDAsUE1AceJf9fRnlTBuKbM4KDJmLT0_kbWC89N0FK2LzX-IeI40d38MKfd8rwKlhC_SsZBZhQBkgc9Tjnu8aPBIOnnbPHgnNCP-1iS2kKWepNFhdN0U9MpYR4wD-eH4QUWnJ6oUYFsyWEX7Ss1Amel4ORKfteTqDdJxvr3Qv-vPA0wNx8nq1ir8QLYQtNFByVvNZfurWjoG4ytv5078sHyUZx_gmWIFNM_uIY6gXGKfXB8hky6UkVkzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعداز جذب دنی ولبک و جردن هندرسون؛ چلسی به درخواست ژابی آلونسو امیلیانو مارتینز دروازه بان 33 ساله آرژانتینی تیم آستون ویلا رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28721" target="_blank">📅 11:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_oHrD1f4juHs5UV_98uc7BJg4OY1LM7tLGSPw5b8p3mS9qE08xBk-p_gcyPJTK5DstBIzJY6ZPAAQD-sJ7LiERQg2qByu8t1RpNHl31nzX2M9fEdwykcLPEfsiwXplYebT6WhUrb_nnp-ruT0QtM5K1OCFi8ctRnMMEVzMZV5dO_-N70UWCdEm5TKy12_vJTuQ8x4ZjtXIoyBD3eTkQ3Ov2XJn4GyiH2iKkaRZtdDKa1BtfrKIDT0H1LBQgkdFocEW-APDq_z-Z0D6KlS1DemgmNH8ud8wBtHQIimOo_A2VBpwxArqSmQTz5SpaRR0iRgJkAOiFfijXtDrH1ww5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
منیر الحدادی ستاره سابق استقلال: هیچوقت دوست نداشتم از تیم استقلال جدا بشم اما شرایط طوریکه مامیخواستیم پیش نرفت.‌ از تمام مدیریت باشگاه و هواداران که این مدت به من و خانواده ام لطف داشتن تشکرم میکنم. امیدوارم در اینده نزدیک باردیگر به جمع شما برگردم. تا…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28720" target="_blank">📅 11:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28719">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM38x1-Cn4iFuaF6KhVJJvNLMRhI3nzNJbcjFEjlWTbVSnQR1MpA5mrvt8gS-_mXEHXMWda9Oop74nHD94SwzwTSplDL4C1CVm1sCTs-w7aeJLUEKg2pu5iYIM6yO9iytenZ5GrmZV0ZrbQMQUroQYWkNheB66_grW9mPPaDzn8nJ4W6cj4dvU33bJ9KHEFEs1LZmK8ocU-NJJ7KnT7gnTEJJ8aYnW8KTFRHZ6MD3DDnezEE3XWXmF_lZL5JKhu6Yq_wiLwO_ksms8p1luwRuK5ihClcLc4Z7v8MuB5EyyPGQZfaVrZhwTnHARUEx19XgLkASV7ZaSAUbx1oFyvqGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28719" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28718">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4635dd1d8.mp4?token=rs4cxEoH8W3l7p75BgtQZ9IAs645Bt4agIHeDFTIBnDcKKzuNQB_12LvfnSU7NnrfKOu92wNjqvjkA3ccjJ0DISp-EffpJhsHJXP0ad6CA1yQV3mhkoW2_4c5FhooLiK2MlrS8A5q-LPxCiEvoQ6rVqWG96FzE_2MoEPgVthb79OzC90SNOdUv3IPDgcRIuYePMvmEXeCh-jht1zC8nti0oiCkdO3XwHZ2jkiD60kckxvisMOV4BpuDPQfs9wJZz9qA1VWth3JMvctxQ2QmPhxWNPtTgXJZTj35WEFZuNldqy8wlLpUalg45kcsKh2aXYvd119oYrOLvTmycdcTUOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4635dd1d8.mp4?token=rs4cxEoH8W3l7p75BgtQZ9IAs645Bt4agIHeDFTIBnDcKKzuNQB_12LvfnSU7NnrfKOu92wNjqvjkA3ccjJ0DISp-EffpJhsHJXP0ad6CA1yQV3mhkoW2_4c5FhooLiK2MlrS8A5q-LPxCiEvoQ6rVqWG96FzE_2MoEPgVthb79OzC90SNOdUv3IPDgcRIuYePMvmEXeCh-jht1zC8nti0oiCkdO3XwHZ2jkiD60kckxvisMOV4BpuDPQfs9wJZz9qA1VWth3JMvctxQ2QmPhxWNPtTgXJZTj35WEFZuNldqy8wlLpUalg45kcsKh2aXYvd119oYrOLvTmycdcTUOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
جوسکوهای ورزشگاه فولاد آرنا دربخش بانوان؛ هواداران بانوی فولاد بعد از سال‌ها بالاخره از فصل گذشته مجوز حضور در استادیوم‌ها رو گرفتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28718" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28717">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHQEvBBtsL3U_ZDJ2YUlzsx459RwxfrV6Nno_iqNZ6d6NYJ2n72TsvFDZmp2DbZ61kMoNIvu-4cf3n8aWJ87yFSfXS5IGc61L5zf6bIui7dOahhVGIYWhVAet7HlRbrmoPJlLAoQKWdn_kZ9c-4yCwxlv1v6GL5uLXc93Ss56AWSJH-20wV5UsEujiGm0k_U3b6crEaRX_HRDyXVgSOsUM2OkbHU43q-yowXPwHhQ9lRGTkiOJVJ2zmP6RZRI_bpCknXDLIX3Hs4ANlHXHj-g9XMGfa6Fx-7X88ATD-HA-QOpX7qjFAida_-AKE5H-6WeXU6qaKWsx6a-cG3On90Ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28717" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28716">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alur9_zxePdlVigvg28sPz4Y8uGHtyCIOR69TzQfV9ctMEBGnfxv0bixXyDKNl1gpYps0FedSlPVpxnt3TudAD-IHA9YDdQtIH9twh_7TOd7ZI1T-E-iRqqk40H5D4shSpJXq_1uO0mBaIFr4Cq_T1VymDg3rdj4_-JymmAagLWPSdz0AnIwn4QingwsKQnkmtolYN7fUwF7k8KGbZgeqKg_tb6suN3qZ7r1i-BXTKCyE-l9-CYyhfJBaQeOJIA3E-d5a-j-2klCrDHcpH5eAn0s0kLIDam_neGoyIsa4auP48QAF9atxHKtkXeF96BLmzQT7J75gt2urkvyqJffzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شایدبعضیا یادشون‌نیاد ولی کریستال پالاس یه بازیکن داشت به نام کریستین بنتکه تو اولین بازیش مقابل لیورپول دو گل زد . بعد دوباره در جام حذفی مقابلشون بازی کرد و دوگل بهشون زد، دوماه بعد تو لیگ مقابل‌لیورپول بازی‌کرد و بازم دوگل زد‌. لیورپول ازش خوششون اومد و خریدنش یک فصل بازی کرد عملکرد خوبی نداشت فروختنش به پالاس به محض اینکه برابر لیورپول بازی‌کردمجدد دو گل بهشون زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28716" target="_blank">📅 10:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d907216599.mp4?token=MuI_ATAx0__Ttl1lOQBuz8ktKnUV5mrftor2MAdsxBb5eu-R_CysOEaa4KHFK5yKR7FdRcyX7ZGHMK4IZZ_f5h97AKEVjXsibEPRonoMnR4TI4Q4-KEF-zWkKoskChgz-wLLqicqMZYM2vNt_70xnYF1fpEQ9XdFJ7hyp_PfhtkBtAc_2kLgZfwylE0klTAC7lNgYmSK8bHopnzPsVHKszWZXR0fQLjBVvDmeyyp6Cdqhy2_F3HeFam6XsHf2GAlOp1eFnFF7q1BO64E81hOP-MDFTtyQeo8Yu2VDqJy0EznRkYiKMdy-x1A9-6aD4aNBUoRBD595OQoGkW_3s_stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d907216599.mp4?token=MuI_ATAx0__Ttl1lOQBuz8ktKnUV5mrftor2MAdsxBb5eu-R_CysOEaa4KHFK5yKR7FdRcyX7ZGHMK4IZZ_f5h97AKEVjXsibEPRonoMnR4TI4Q4-KEF-zWkKoskChgz-wLLqicqMZYM2vNt_70xnYF1fpEQ9XdFJ7hyp_PfhtkBtAc_2kLgZfwylE0klTAC7lNgYmSK8bHopnzPsVHKszWZXR0fQLjBVvDmeyyp6Cdqhy2_F3HeFam6XsHf2GAlOp1eFnFF7q1BO64E81hOP-MDFTtyQeo8Yu2VDqJy0EznRkYiKMdy-x1A9-6aD4aNBUoRBD595OQoGkW_3s_stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
عملکرد گلزنی لیونل مسی، رابرت لواندوفسکی و کریستیانو رونالدو در پنج لیگ معتبر اروپایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28715" target="_blank">📅 10:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28714">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbpRh5I5iLPmAQ8ZMJAwlJqIzwlogDaWt7717z6Z-OhLOHg8uUwZZb02QF-Ybv-VaWL-TTP1q89rCkgZ7Q422kFz_1iojv3rhKgv0ySMuaJKIRRO1ZkXwJDO3tDXy-HfPtPsYMID40evft7E71MMEKDExlvbNhcXtBfcnXQJcCHkxzTZ_kQZQQV8A2EfSVJ1Cm4pkbS7bkU0iFVmV7Y5elAj5m7my8qjD8zLKcQeodW89pAxFR1Ulf0oGFJhLHELvikaO3qBixOfl7_htJhEGNvqN8tgZ1AeVVA-KoAT-8mRh-Eewsbrz_eUw4e-tgXbrkKa-7bhXARpVjm3lOEhxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28714" target="_blank">📅 08:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28713">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28713" target="_blank">📅 08:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28712">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M04mZbExQxuQbSfF3fv25iCw_Px_OUpfwdlfTjIp7TEaWkZ94JC1OTo8MJjatuzH9UPw4jlO06Vb2u_jLHYSB251h1fkIYiP4fHCTRckZN_vaHPz49NokLEGgEv7k6sDGBI27jLhTGbV8JvjRXve0EvP1c7ugkcA2lwCqV1s8d9GzLyVqozCTlPrbcwX7JA5W1-YaF5oadEp574wbfo2MZx4JyYa4XXjq3PGYhcynwma1QqRaNs-MM_7VmI1XGTitjvqHBcr0WeOG5WKkuNbrVesBNQ1vS2PN5crcXsUxs_P2xdWW7kr-YygiN8qTXsPKNnx8rqKZK3PGoBxPmad5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛اسپورت: دو تیم اینترمیلان و بارسا در حال مذاکره هستند تا برسر معاوضه فدریکو دیمارکو و الخاندرو بالده در روزهای پایانی نقل و انتقالات به توافق نهایی برسند و این جابجایی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/28712" target="_blank">📅 01:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28710">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrBjQIytxlJKcjCDRavjWw8lAFVocIHIBXKPzzvtdoaCLL_sPpfR22Ltvb73Yp2qjhbLOej_rLkEROEy5OdCrT-cVs3vEOMVtF54KsVaBupqKSU6fi_e9_b_NicNg6UvDvbkxh41sRabI5DYOFdz-AipdrnxL4uGOA1tXZYpRLiqCpsiYlB2rSNE0BLAUu28Xbr2ueWTUA4fbx9i4NDCMhirWpRKyGf1h_BI_-8wXZMYZ4ptdt2lYkMaHtVCc6-X2FJtLyF26ORZfuxsl6GQL7e3vHsjKoo5h24hU5VIOK2__ChXxq_82f2jI9bz-4VwP4p12uQVTg5A14E36vUwnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ نبرد رئالی ها با تیم سابق ایسکو و مصاف شاگردان کریک برابر ایپسویچ‌تاون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/28710" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRHlpOYzknjQaRvt_AdHsMvGIMmUhp0rOYll3KKccWq1Thups0_N9ifM4S6zi_p-4Kfn9QSZ5-IvOdJKmZ_0_I6Du6CSg1D6WMn3KmAlfYdYeWaY6AmquSOL1o_spvgzu-HoW1fcaWD6a40sNTXxT8m7Bp9BqD_qnBciQnif18cC_Ny20U3A--dE-tSSmFN-rtE0CPxrtGqMBvdI7H_C60y14rdwKs7L5BBaZalD1Z2-OOto2M0Rgr5MVfL7CnWsOYJ3RITvRPCXyKNklV7So3Z7r29VxABzorpgMiJDN592E_NyxxRdB8a6rYolPjLnGsHoMGYF1r9xa25Gp6ZObg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
برتری قاطع پرسپولیس و استارت فاجعه‌بار شاگردان دی‌زربی در پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/28709" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28707">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUcvW--BOfFhhFQS2FZ6pxC7OCJFgzHwmd7B9ufKIvLklf4JZ4WqXkliUDwqH4wlTF-44kmiRff_-uBCPr5J_qq-V2u6cJmZc1bOhvWJqWFUhy1XGRfTiCTT8gUE6dp1MzfhZa90osrZEZ3JW3U1va3WHp_9zcWvYvxEIk0QxUw-dVmT8SEzbmSnrjI28dP1vkNwxQrL5jx0oDsAS7ZmVjPMZ0CIiggNWTpmK9J2g3j69r_MhHO1HVyfSbhDFCtRNUtdC4wlWpL6WJpZAn5_QsCJ3Xz8-WWs2yj21WSg3W7ZMBBlDBbOZHR7PETQ1J4ASoRTOaXzMQiEsL1sLO3IuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍁
پاییزِ زیبا، پاییز خوش آب و هوا، پاییزِ دلپذیر و جذاب‌از رگ‌گردن‌به‌شما نزدیک تره. این گرمای لعنتی بره که برنگرده. با قطعی برق دهنمون سرویس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/28707" target="_blank">📅 00:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28705">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB69jYRoXJvOVCcPCMpePwgSUtINgB-vckX665rmdMIf1JrJjREnsNQDL6Mw0KZvRLE-Wmfj_GjM3X0JnfU85GBJbOVXr2G6iHk-CNw5c5BsqcZpTgMhEoOq9iFGjEsIxWN709RVCEO7adYHAXUncj0mD5wQ241HMXIOkeoFnEagxYb4Cf9mneayqTdhWyJrbUASimAa_ncG1YwmUMnVeKCbh0p1lGwxPg2zLvuFaBZMlCmNjcva4nJLJzI5RZCymD4wxP7G3fjrs0FRhpEsVD4SC6XAZNoixdFC2TCwlQWEsu6ZS7wDILS_2EvGnvUO-IKeVVi7dJ0kE6byat_SEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنهایی‌دیداردوتیم‌پرسپولیس
🆚
ملوان از نگاه متریکا؛ ثبت‌امیدگل خارق العاه 4.02 و انتخاب علی علیپور بعنوان بهترین بازیکن این مسابقه یک طرفه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/28705" target="_blank">📅 00:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28704">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmsO2VgP-o8Xn0BjxHJxI9-36AwEu089Ee8igWqeWc3vmMPADqCtjzPHor7xsgjTGEC5bBEamij2A2F_xs1rs9dzXLjeCf-wt7PsGETD4zXJ1Zs8lnnVLb5EW22DjwrlGAhXN0Hp58wP4JvkuhZQpm77yZT_Dw8a--PKPW6Sp9iGd9zniWCOU-XcvoFFZqdqqkhb7JzaisSZIXnKotaho_8qSqQEEKRkr3XU_lId1SmbXyVvuAQccK-SDlpngZx3BqE38q4v5b0wDG-7kdRS3Syhpdo58txFiHCrlDYH70kPN-abkMqdVhoQxLzcYAIeWYch2f9ZLRqdf-noQAIxbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزنامه«Novi list»کرواسی‌گزارش‌داد که محمد محبی برای‌انجام‌کارهای‌نهایی‌لازم در راستای پیوستن به‌تیم فوتبال رییکا وارد شهر رییکای کرواسی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/28704" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28703">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XclU7PZH4oG92RWiqKDnArKeQ3IXcAvUq-dejl6cfCD572O5rWHH0I7WcvKcQgMYZSu4WOhQv63UKQaNW9Gy95KHRADQPyFmTzFPnj2SDqECDf6unflfIB__calWP4Nvp-fj_3GOIPk57wU1rGfmpawECS-pXyE4uMdswNdvZgwlOTgclcjD9rD3CC_7uVrgL7ahnD3va6PPVjK2xf8rJ9vhYssybXTMC4Bohm9aFRW0KG_k0koGTrxJkrSylXZIgt6D5iW5kX7rKBDe44t4FyHg3165Ed3yqkgs3ST_H3ZMCKGVJ2EA_dlVJxDUrgIyBy3uxYNJv_2zj8xWv_R8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/persiana_Soccer/28703" target="_blank">📅 00:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28702">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/an_GIjHlcR6DO4uudSOwyFSYqB5NzpKcxwyacNA0c6xtLYF_00C0oCUE_MaNc6-YcPx-JlQg65xuudNWV5B6ZLIl8UCVPNlh4t4Ap77akt3BCJIkOYEUpZPkq-v-h3Uq2UIO8tM80tmZa6h1kXzQwB9uruyyy5wTxclPFtC1_nXV_BDGOHU5ftKndgCTYyZR9dmogUG5P5v5LLofGnDfX5CXYtzL9IM6wDBkkf740drpAL7aKdeRoGV5WXD5T5t-dZB3TIBBTpjQkSqXOP6AGNO5CDXCP825h6F9SIRwKB8XsPOqPzcPbFLtmlITv69jDApl7FoNCoOpqCdzW3yD3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/persiana_Soccer/28702" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28701">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9R6THR696tA68cVkjH45nEL3ZTxxO74hiHSulGfcpt58BmfHCUphfKuGP1yMQHrQPzlUWMdczhcgSjTGhov6lCbFrYMcUcUah9QLPdXoLuJENobqVRdVXeBm8WyEv9x60ezucaBRK-24v9t3L3bKNRIhN2vatraLd8NDL6TC3Ntm3ZSNnbr4sQaSwOxsR0VLDmxhv2WvFWLDxrrJqYzrj1EELHDZMLxixtBDDY8I85WQhe5m9QbmNjJOpV6iKhrragUA-xali0oZjW-Y5IXvHsOUFpTpALKMxl8jio0HEr1c2cJKtUkFYpBqb-ILWeSuR8J7Og6WXMT0mfdJKJf6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام جرارد رومرو؛ الخاندرو بالده مدافع چپ اسپانیایی بارسلونا تصمیم نهایی خود را برای جدایی از بارسا گرفته و بزودی از این تیم جدا میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/persiana_Soccer/28701" target="_blank">📅 23:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28700">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/letKCtEFgcI5Sj6B_3EKaC3EP9sLmGQL8wVSu7ExG6U0vrrPjiZOLm1_OyAk6b-1QUjrZf1JFAwCQT64DzYhBJhvnYN3WNS78sp2UUDquLEhkQvcNM51rGd_zdGhxfbrB3y5YIW3zJq71mPiSvvMYejCqNHdQRQwPaE4IBLEc0IEY4_5tilWZiZYIl_ABJWmGdEv6xHLl6dtySDi66gmGdKJCFfIJtXfjV3ODlnYTxrGPDtwbXmVw5QQHGUObrfixTnF9Ka-SQlE_JT5e5cPqknwcdxwu9YUvPwrKODlmgZtRXLZlxJeMbf88_-oarBOsmE2n1eSpIZUk_KzI1OM4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/28700" target="_blank">📅 23:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28698">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAFfRXTxRNGEfRd6H8gfEAL_-q7XX2ly2rqa9I5B4XF_gyVd0gA_jT_OhaShCwlHGsOHbZ9ea9y0J4vmrPZGT6UGWsBRfKC5O70PHLU7Gg3RxhjphlRNg8E9AieFIS4YKFL0UOyogJY3TOYK06vcDHa5MIcJp85lqNgGy82u9gyLtqQRqLXFlQHJEPWM8tdzS9XFqe5rERfrPD60Swtc-791mbQZQPZ07g2fM2pGmopqbwhPsEcxTP7dR404nr7sgvgqcKGoO1eVtWAAWbQ7IEDc1zDCq3tuQfX9pgYWrRV31p4yZHDnbFhcPDda7RSzaUhRsqaFhoLyTzzG7hzbvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/28698" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28697">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f3cfd1b0.mp4?token=ZxrLUXl15qn4bAjUmGSlNZuRy7F7h13XUELJmTRPkVth5hAzPWFuCXc12GZyJ5f-Hru8n9FGXGLaVTn5_AO13JDxgQn-O8x6kG-I17ze_N_N6qBQMapIe2UEJ3VqBiCYgT1H-6SDAEMVKZWb9neDqT05PFyBP6k52yutYe1ueArvZaUOeuII3vTfjoF9QrpHiQLxc9HyGh6nNTAWkPZapXB2pkLHAQ5NycLAd-0-v_bMkmMkWWpWTsMeSNfeITskXa4FWITmlj7fXnP6dex0IRtGsGViP8p-B74g3rLfe4qwV5pqzEW_6ejh9VxkGll_JP_obJ4KC6QvUAnVmpl4Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f3cfd1b0.mp4?token=ZxrLUXl15qn4bAjUmGSlNZuRy7F7h13XUELJmTRPkVth5hAzPWFuCXc12GZyJ5f-Hru8n9FGXGLaVTn5_AO13JDxgQn-O8x6kG-I17ze_N_N6qBQMapIe2UEJ3VqBiCYgT1H-6SDAEMVKZWb9neDqT05PFyBP6k52yutYe1ueArvZaUOeuII3vTfjoF9QrpHiQLxc9HyGh6nNTAWkPZapXB2pkLHAQ5NycLAd-0-v_bMkmMkWWpWTsMeSNfeITskXa4FWITmlj7fXnP6dex0IRtGsGViP8p-B74g3rLfe4qwV5pqzEW_6ejh9VxkGll_JP_obJ4KC6QvUAnVmpl4Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
فرصت‌سوزی‌عجیب‌وغریب و دور از انتظار طارمی 34 ساله در اولین بازی خود برای الوصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28697" target="_blank">📅 23:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28696">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSLXm9g5U5lF3dSy5xxiwa6nr1Hg6RjDp1yT6y1PSfYyLkRET_lUHZsw28n5PChmNLvfd8WXa6sdLscUAKUUi4k02BDceLooHi6RW4VcpWv0eDNbRhIUJc-qHvOi6_s-Mta1Db6ZbhdVUDWxSSm9ABt6bv-j7mymDQYONPUFa9B1m6qwD58FO_HQZmEmZHdCbBQ5pSCBnCm0KbCRJk1YilP9xbeSflnFLfuqN6-a3_ZqgLfLI--hV1gIbL2kNMoQz8_bbX2BeAfGsUkI_7O7PxYYlgwXko024RZndbqPEqtTQ6qUn_Gixb-ZXqi3dRNVzx4PQTK06NuKt14ki8G4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری
؛دیویداورنشتاین:
کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28696" target="_blank">📅 22:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28695">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0klxy5FgoqlknZPQGF7nTsoDEl5aTVPWQzzBUTVgiN__KpzzDVXSabrjafDcljZD0LGnNb2B1VahyxV-7yKblLjT27B3g6s2A3O71JQhodXvHhl4EiNdwn6zyDLX3ex7C6w3KkiW4hmK_o_pwqh5b1-UNmoR55gygFG4F1CZPH0N2pnHFQftl7Rvp9yxn_2Cbvq0k2ShE_U7yhhBEVjVNgZXMzFuq6gZCE8X1NSQFTIwTc4I5ocYEOvizOFwm2hL2kYxL9tF1J_7YM9yVwufmzKsgX9PF5bfC4bc-vTTfOkVLoAvUYrar722Dwqa6cNbGOjy9axWVlF7mELvVUWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های محبی قصدداره بعد از بردن حسین‌نژاد به‌پرتغال، محمدمحبی هم به پرتغال ببره و نیم فصل با رقم سنگینی به ایران برگردونه. فعلاسر انتقال حسین نژاد به ریو آوه 250 هزار دلار به‌جیب زده قطعا سر انتقال‌محبی‌هم 300 به جیب میزنه بعد نیم فصل‌ 1…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28695" target="_blank">📅 22:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28694">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=mLgv7ci3pAjnvYlB-nHVhkWWnI8eRV8SCKDGJPg-drbIkyuz8LTEPpSaT2JIi6HqQP076mZSvGu9yNLHBvV-hWeaxrkbIazdshlU3UjE_glamiXI0gs5u__Sv-V0-k1tB-0I2hsIfG-tugtzzqcJ-jXPvgde7YubhmyTBfplGjY163UiK7q0f5cKTv1vey7heykW4IcU9zxhadYWizLBCP-hhd_wuOcNqV-J2fDMZ_qK1QdKdNH_cjNE0GrniHf-zYtbJpaIeCC3JLbg__im669p78ZRtg_m-TH31bErIRTu6x6LM3h8w3ebYM1XBKRlhAGgDhONVSr9Amf5aWj62A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=mLgv7ci3pAjnvYlB-nHVhkWWnI8eRV8SCKDGJPg-drbIkyuz8LTEPpSaT2JIi6HqQP076mZSvGu9yNLHBvV-hWeaxrkbIazdshlU3UjE_glamiXI0gs5u__Sv-V0-k1tB-0I2hsIfG-tugtzzqcJ-jXPvgde7YubhmyTBfplGjY163UiK7q0f5cKTv1vey7heykW4IcU9zxhadYWizLBCP-hhd_wuOcNqV-J2fDMZ_qK1QdKdNH_cjNE0GrniHf-zYtbJpaIeCC3JLbg__im669p78ZRtg_m-TH31bErIRTu6x6LM3h8w3ebYM1XBKRlhAGgDhONVSr9Amf5aWj62A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس‌جالب‌ازسریال قدیمی فصل دوم ساختن ایران و رفاقت باحال امین حیایی و محسن کیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28694" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28693">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e895367e.mp4?token=F14lgvJDWiTGGcpLWwqw9BzFMHaN7Y4i5JGgLbZ42GOWhKs73UIjHkCeaFKWSRCGsv9j3fLz4BKmfY7tU4TjaxFtcHAn1b9zFOfD1D1SYJr3k4z3lpG3RDLO58pwPCNexFfNIOtmBQa-sY_aT9EISZ-KeC_pqC4oCisy_NxznipdGHdJtR4LKzPJ7PZH59BWjJDx-NXtXlaU_Xefx-74sAfy_vW_3tFfQ-e0QZGdu0xbv-q_oqVZlVL3ZVqH3npEZJqtsbKjZml79pYegMks19qatOqQlOFFv1zi8nvav0WlAFtfJd83Ztu23eck5wzeJwxRE1bG585ucRRTNV8KDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e895367e.mp4?token=F14lgvJDWiTGGcpLWwqw9BzFMHaN7Y4i5JGgLbZ42GOWhKs73UIjHkCeaFKWSRCGsv9j3fLz4BKmfY7tU4TjaxFtcHAn1b9zFOfD1D1SYJr3k4z3lpG3RDLO58pwPCNexFfNIOtmBQa-sY_aT9EISZ-KeC_pqC4oCisy_NxznipdGHdJtR4LKzPJ7PZH59BWjJDx-NXtXlaU_Xefx-74sAfy_vW_3tFfQ-e0QZGdu0xbv-q_oqVZlVL3ZVqH3npEZJqtsbKjZml79pYegMks19qatOqQlOFFv1zi8nvav0WlAFtfJd83Ztu23eck5wzeJwxRE1bG585ucRRTNV8KDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تاریخ سازی دختران ایران برای اولین با قرار گرفتن در بین چهار تیم برتر آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/28693" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28691">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=RLkPd8Y3JyiqAjV31o_Dy3Rn9b-V3nmbRDO_BafNddmkCu2_rKaWAVZYlREu3Pcbi_U8ri-8iEclZtk2kw_1Y6WMdvAU_FUOH8UoS1UA7KXYdL1bYzPJ8uY49QJYsQU8oCg9gjA63YsWiJBaHC8r4ZfPMcbnJsDDenUdbQwPLFWCc80pDPOq-dlYMlxmovkJymF9XNMytsrz8fycbc9LBPpAR4C82ZP_ad_8crT7Qom7hv6K2GwGZyDvc2W3VcHgpwGaGDuIiP9fwLu9wJdxptPDNc-iyWlz4fShxNLdlqxWRnjVK5b5pAHY46TsvHDbCogdd4fCqw6rd3luWsCFwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=RLkPd8Y3JyiqAjV31o_Dy3Rn9b-V3nmbRDO_BafNddmkCu2_rKaWAVZYlREu3Pcbi_U8ri-8iEclZtk2kw_1Y6WMdvAU_FUOH8UoS1UA7KXYdL1bYzPJ8uY49QJYsQU8oCg9gjA63YsWiJBaHC8r4ZfPMcbnJsDDenUdbQwPLFWCc80pDPOq-dlYMlxmovkJymF9XNMytsrz8fycbc9LBPpAR4C82ZP_ad_8crT7Qom7hv6K2GwGZyDvc2W3VcHgpwGaGDuIiP9fwLu9wJdxptPDNc-iyWlz4fShxNLdlqxWRnjVK5b5pAHY46TsvHDbCogdd4fCqw6rd3luWsCFwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
👤
مازیار زارع سرمربی‌جوان‌تیم‌ملوان با تریلی از روی برنامه فوتبال برتر ممد میثاقی رد شد و گفت تا دوربین خودتون رو از سالن بیرون نبرید، مصاحبه نمی‌کنم. دوست ندارم تصویر من رو پخش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28691" target="_blank">📅 22:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28690">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBTN84fPD7sYGZISZeUp4xyjXugc13gvKD5OT8fvy4V4NdWymf2wFeZdzDertV4mALbznvYyIldO-jrJ-aZvQpjG_e_ePuGf0bM5Ml3HV1fSi26v5Is5N7cbkIGBo-QLzG81a45_QXGAMuPMIdD9-eE6zjq-gahuBYknigO_RN5r5nCuyKrBl-DI3jzQwuJ5koG73Q36J-FRi9Aj-3jD_89pWt5JgJkQK-6n0N9LjARzOkLs1Rzv4qYkForkLNEW3ODqBsb4f7WHk6R0WvzLVzYbpM8hey_K7QY0KBOA7Kp_KAGjEk7FG2BWzj4vwVt-trH7wQ1MujWhZj3yK3lBdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28690" target="_blank">📅 21:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28689">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1n8Q7PBgyZLoRAdyEIB_QtS0qv71Twu18Ij7WlhcJ9HhoIzsiiAejw96nziYBfsOXVi5rsEx7JHOUeahWlSqoCHbGDA-TxpTasenWwr_bMzHUH07pXcuX8HS9Kjbs6NqrOF2i41cK2I41Xhe09vcgB7iVI_D0zCJtlunYdsg-si5dSMxkkyopCwBu0NZiNyB04-14eJxGBx2HA_f62KYlEkvsF-WHsMEJfV7JmARrJNWv6cms6lqE3qCVY6gULOcIcXwK0t6AtAxDlJ34412DeUNrwJmne24Bla4lpDaeyaSZJzIZg7jZQpzZ21vwmniH6HASnfQDd2DRQ29dwqdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌ونتایج‌کامل‌‌بازی‌های هفته چهارم لیگ برتر؛ تراکتور با جواد نکونام همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28689" target="_blank">📅 21:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wbyh7FchLOrjLQbLylprV0Zdvq43yWbdayYDAKNzNUqfc-OhIiyIlAXTwCQCgksiPWBYCtQ997s51SH8Xi2mP0xayxotKlr87Wx6gWQNGmCEf9GdWSukwFgq-a0nFYbHgjJm0KH9NwKsbdljZHgoVsrVxOsEpWM4foCtoXSR50Q5JDXNDr_86fs71hVb1CP5p6rfzdD6-gWUCcG4eHCNEhXMFqlyQq5pPgDCCvuqU_SKDCxk4getf0EDxXjfndmkQGLFdd7Enge6wnpstUSaB6j4Uc87qn4atVDAjJDtZKajfn0rv8oXhmt1p2qsRatdNd8cl077-Z-jZwIFWzZXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZczBTE7RpwnEsWAgDG856I_5t6wpfObJ9Dp1GdK3y2JMW_ZSINvxPa9-no1LkUGf4AWcF4T7C9cw4sRWIpnYsiqOaoUk2uocShN_bSH_J9ujvruwzuxnSV7mFZFEvdw9DUzeYx9OhaD8EKShz6aSbXHlBIqZMCayI282pke3TM4MoZ4hO11wgN6lZPsXs8vuyZHJFa0_Jb4ytQltnpAguke0JRXeHfWhDXO52tch4GmcSZaTF7ruxZXrxVl5NQtPLBlNgM4g7DQ9PdtOYlbnyHvy2KgKwouBgTNW3-DDtvGr9sVcHJGybkdvHhbLVHoEv3DL2FwkNZ8qPLVS_Y9pyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/28687" target="_blank">📅 21:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28686">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7Z6TiGSpIEDrYecc0yyT6SCpG07YZFIGG3a6oOvf2uyK0aScEI8WqLB8xO7mVLUYetp_sI-IFdBAQE66BiNV5BJKGqnqW3oZzLd5TMuwlRRggqc01hx-6LcMi6eB6Y2mlyrNPBC-bciPNyMxBW7h6eLtqCtf1jNOH__wHKzA5e7snsvqzteMCAgyuCbQe0Qt1N1qAlW-kZ1nyU8M7pBLPGt7rntqldxF3qrXxFKo2We6BU3h5E9KeBFCa0um7J1YcjTLSgFm6wEdpt1CRpoNWcVsf-n48axBTS7NcEGK1n3sSAS47puohcOC8rn4wsTq-ovWIIoZ99kbmpBFrmkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28686" target="_blank">📅 21:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28685">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUMAkoIxU_10S77zYIMh-yT83s3M2cOSk4JA23poETL7t0jfcXdw9M27enFFsM50JtLM23Dq0xBn29AikOTnxglT9aPS-nQD4_FbQ8n7DAQ-RXJWsffIUpss89xyTCQUQotFmxzTEdzBluoalushcfueh1LCqBjS3732SnADhxxaAdKq4WatvR6U-j_0ej5m0PdX2EwQdNXOHWXA0s-n4W8-Kih1P35sHOYEMjfXE7ZqRVREpKEH9SPuY4nR_GdJc_CsLhplXmVyvbfSJW6lGy0gJsA_oE0vGo44ipX71XHNqCgiDHuMXR67o-_4Bt8rScRxGkkHBg3LokfWAQ6_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آتش‌بازی‌سرخ‌ها روسوتی‌های عجیب انزالی‌چی‌ها؛ گل سوم پرسپولیس به ملوان توسط علی علیپور '56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28685" target="_blank">📅 21:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28684">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=h_9sFb4xZZIl4NbaTiQjruNdn-Q8h4n9Z4DGnLf3YjcDKNIVde4YK1L5RmX0kEDn6Ads8VzeCWAB1hK312fpQLfrDfwMGg67o19wG_iYgAOeR5i3o-4c_nCPsG29s-IWtXNx1OlK5C7XJp3tuYRiNxneun1ijMFrqNmL51jJWR0ePFHYYulTNr0gSu2-71XwcKkpzAy3hUwpyKswgKCsNneMGGnmF9QpDefzXJl7qQpasJG-98tUFfGFI0fH3Iweim_qejNdphOXX1PYhpePMyadebcmHdDTrU2T1NSmJPzSRNyFFc-7lNBqYwTIG6bJGJS8gHMrBOSifUI9hhx8nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=h_9sFb4xZZIl4NbaTiQjruNdn-Q8h4n9Z4DGnLf3YjcDKNIVde4YK1L5RmX0kEDn6Ads8VzeCWAB1hK312fpQLfrDfwMGg67o19wG_iYgAOeR5i3o-4c_nCPsG29s-IWtXNx1OlK5C7XJp3tuYRiNxneun1ijMFrqNmL51jJWR0ePFHYYulTNr0gSu2-71XwcKkpzAy3hUwpyKswgKCsNneMGGnmF9QpDefzXJl7qQpasJG-98tUFfGFI0fH3Iweim_qejNdphOXX1PYhpePMyadebcmHdDTrU2T1NSmJPzSRNyFFc-7lNBqYwTIG6bJGJS8gHMrBOSifUI9hhx8nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های علیرضا منصوریان سرمربی الطلبه عراق باخبرنگان‌عراقی بعداز دیدار این هفته این تیم در لیگ‌ برتر عراق که با پیروزی تیمش همراه شد: 8 ماهه که هیچ دستمزدی از الطلبه دریافت نکرده‌ام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28684" target="_blank">📅 21:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28683">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=k_e0d6h2XzifPD1ocLDzJ1zDZ2W3TgSxXqnfpqOGDtmEezDMA7mCIA0xiLyt-bxsj7wcq5ZY_lzTLD_yDDmhCXEeeFiFPguV50ZB1LrvL7CYOjeF196dM0XG2XmXmMwcZdPDHZ-bKms1znKoGp3BM9MQlV3pO0lhvdjHsx-BkyimHy2AQ47HYSm4RmDPs7IfW_hZIatzr5j7BID7Ib_0XR2gziJkxmvRHebH7D7GhyGHiF6ZnCaRCZEaUGPcvyhqZnUf98mujIOsBq2AXFLx-UO5ILnTmVtQlgPQBRt_8fgvnc28e064dIDObK3zesaDvy_gFF3BwR0DV9SwPK2jww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=k_e0d6h2XzifPD1ocLDzJ1zDZ2W3TgSxXqnfpqOGDtmEezDMA7mCIA0xiLyt-bxsj7wcq5ZY_lzTLD_yDDmhCXEeeFiFPguV50ZB1LrvL7CYOjeF196dM0XG2XmXmMwcZdPDHZ-bKms1znKoGp3BM9MQlV3pO0lhvdjHsx-BkyimHy2AQ47HYSm4RmDPs7IfW_hZIatzr5j7BID7Ib_0XR2gziJkxmvRHebH7D7GhyGHiF6ZnCaRCZEaUGPcvyhqZnUf98mujIOsBq2AXFLx-UO5ILnTmVtQlgPQBRt_8fgvnc28e064dIDObK3zesaDvy_gFF3BwR0DV9SwPK2jww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28683" target="_blank">📅 20:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28682">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=UJOU4aEAKpWYA0dXJRbXei0Ywq7cYbce-vfgLxo7dgZm0nBJRe0ggUKrq8Vj9r97pnVH4CYMbaHwjV_agARNbiQ55o6GQuwGQ1oyl6GGnHHvd-kmr4PgagwUSKlkbjEnv2E9d_QM-gi9OKteOs8M1J3HKYY69416MXfyySRiWaM10rxIQZO4xd52yYTc16cEtxABzeAA4rl9-XKggmaFaJBF4HyaAOylF63KwTuAATBWN3BNXXbr2uFcsYVunJ3AqaRB5Z-bX72Idc62AcY-9RLVkwSPNrvPOwPJ2KfFNhbCpDPr9SWd4nTFA5ZnJU8gnc_t0gqOpQEWrxjqj_gH6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=UJOU4aEAKpWYA0dXJRbXei0Ywq7cYbce-vfgLxo7dgZm0nBJRe0ggUKrq8Vj9r97pnVH4CYMbaHwjV_agARNbiQ55o6GQuwGQ1oyl6GGnHHvd-kmr4PgagwUSKlkbjEnv2E9d_QM-gi9OKteOs8M1J3HKYY69416MXfyySRiWaM10rxIQZO4xd52yYTc16cEtxABzeAA4rl9-XKggmaFaJBF4HyaAOylF63KwTuAATBWN3BNXXbr2uFcsYVunJ3AqaRB5Z-bX72Idc62AcY-9RLVkwSPNrvPOwPJ2KfFNhbCpDPr9SWd4nTFA5ZnJU8gnc_t0gqOpQEWrxjqj_gH6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریس رونالدو کاپیتان النصر پس از برد دیشب النصر، پسر سامو کاستا را هم در شادی اش شریک کرد؛ قاب زیبایی که حسابی‌مورد توجه‌قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28682" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28681">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nox_kcSx2dpnXSlsdGT_7nMnlGtfwpnNV9A1kyjYKpbHusaHY97Vs6JCk7cRko7lqhh1CjJzHXQz0LoHE5dTyZBqD3ZqHC5_Y2VO9Oe38aIcU4LOiStthE6SZ5kerz6TVhuPg1iObFUH6tnLBGMoGOq6VLInSpmdiOfzdgi_RdvbakkZOxa2Bq1FFjKldUp87SRmiZGFk008vAG6yTeWu2aMMQF1ber1trPDlfdwagLV5Diz0C35z9900X8CaHDovCK3A1mDPx5E-x94gTjOmAQJguQa5oJDieRddSiy7BPzmed2X6ixpXNJyAfIgCstDhmY7V34wu6y538sAdYejQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28681" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28679">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ntpk2GhdCfobLdkZEUbw0VmLrrPzR1MvhFNXmYiD_SC-xkUQUSxDdXXVBGW5hmX8ld-ELxh-mFRBLFPFQElG73TgmhmerG6SH8vO3Glr-_sbmVIpvscVRTphcy5QWQ5IIwoAkJ8jQSGbyWVivdbFjU1RzwCYi4Rhe11kBL5fuyK_zE1cPQ89rfIg-2PKgQvqbCl5tcMb-omJlrRncScVStPHweCFLpxs3eU8_X_Qrum8cNwczMtmscheBk3CFl70P8oOioCOmLqB6TlcB1_Pap32zvdlnTswnlVbHBVVWpgk1bwch_ioPTJhDNiWM50ID6ZL9b9_LzCfNF-YYHzyaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28679" target="_blank">📅 20:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28678">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28678" target="_blank">📅 20:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28677">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn1UAKiUBrq_JkHMODVdxVte-8Ihuf16cDbQ95tVeHkjYNbgwqqjkRAzWpwYG2Cj9A0yQoa4FFlkTLHRgFI2-K9RHXtcYxD4juoNMD4sln2H_uwasP_ucs_4jDakpuhyAmk6jWwlNL01TfsO1bTLe1MFsmM4yDg9Kjpm-zv__AJlEr_2FI7-8LFHBW6ZjZlODDEGu8YOFRDKw0mi0_fRwNSvSW3yM7vmaPIzARpOEspb5C_DlLaq22ZqbFUTUzVKOWQsxwf7qw9KpOEZjpFX60XX_ZtqEEZgn88kR6NWZQtcpAlpNL4kaHEkyMJonL-YtxjUlaJT5SKRWjfeqmPRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر
؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28677" target="_blank">📅 18:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28676">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=HWfZu5yqSDsKpJRNDf9JreZAi2PPPGJDrZ2akA3pOW_NR1yuy1PUN4iIGSMWkEQdgYNAbpEUkjf6AEDzDFHEO3sPEkzB_EVNMu1MvI1AL3XHirJz3oGNKUgQHSr34Xafzh0JlW0zJLsNh2FszEn-bqeGtzGPdVqzNKCVbYCw2Bfinsl_L3qABHfGdESD1--VhPZ9n2H1JZYZGrCxqZaI51gvGop2MkCndcr_AvIxaTu8yu5PzgVEmCv7VYzgVTqxR78tHxdIx_BRVO8ir87h1PebSK1atVHsqipBJLtUwUYL5q6TvetBfzV0SThl-r43rNTQqFF61HvOPHxtyNa7vjB7wi43hvbxLb6ijvfsXess8gjUlLVl9YPCnx10yXVQmndhkpnZtPJJBSnNIdwWPT4FYGI0lB7EbU9M2I1jmTPixJYLUur7MjzUWjISLj3V1R41858Ut5KP0ggEamBZn5o4WGIv-ls7gEjcIoc7RYpT3glDlr3QQU6LeNRv7MVQBp_b_Om1uPdGZffhJU9WLdDYsNGaStNp9X_-GTVP8fLnfUvsIqLMYBGWBbXb7BHs8UTFt7DZrwJizOzQIX87Gklf9PKboMj87mcfFWp_0uMtF3T98D03mRjODd0-3aCb0n7DIWnT5QoUzfE0nPnIDZ1fKvJr0Aug6GQObn8iKa4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=HWfZu5yqSDsKpJRNDf9JreZAi2PPPGJDrZ2akA3pOW_NR1yuy1PUN4iIGSMWkEQdgYNAbpEUkjf6AEDzDFHEO3sPEkzB_EVNMu1MvI1AL3XHirJz3oGNKUgQHSr34Xafzh0JlW0zJLsNh2FszEn-bqeGtzGPdVqzNKCVbYCw2Bfinsl_L3qABHfGdESD1--VhPZ9n2H1JZYZGrCxqZaI51gvGop2MkCndcr_AvIxaTu8yu5PzgVEmCv7VYzgVTqxR78tHxdIx_BRVO8ir87h1PebSK1atVHsqipBJLtUwUYL5q6TvetBfzV0SThl-r43rNTQqFF61HvOPHxtyNa7vjB7wi43hvbxLb6ijvfsXess8gjUlLVl9YPCnx10yXVQmndhkpnZtPJJBSnNIdwWPT4FYGI0lB7EbU9M2I1jmTPixJYLUur7MjzUWjISLj3V1R41858Ut5KP0ggEamBZn5o4WGIv-ls7gEjcIoc7RYpT3glDlr3QQU6LeNRv7MVQBp_b_Om1uPdGZffhJU9WLdDYsNGaStNp9X_-GTVP8fLnfUvsIqLMYBGWBbXb7BHs8UTFt7DZrwJizOzQIX87Gklf9PKboMj87mcfFWp_0uMtF3T98D03mRjODd0-3aCb0n7DIWnT5QoUzfE0nPnIDZ1fKvJr0Aug6GQObn8iKa4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجای‌مانده‌از دیدار روز گذشته فولاد و استقلال؛ دوئل علیرضاکوشکی و رامین رضاییان درکنار زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28676" target="_blank">📅 18:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28675">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0LYxoNWW-UBLuRhw9OhOeMODn0P5d65kWASMzxDEmz04ckTeajldpO6WWyYwDr8wlmA1w1lcBiV0iN51JQGq8JxK5u1UACbIYPBqj7kPWyC2My-HcNWXS6fq1jIxaF3P8RaPn--phJUZO_H77vVgCa12KeNPn-VKd8mR7oqccPJJ3kdTLIYFybckQgMPZcLbS_YzmZWdiv5txHmmeVGjE4BhBHJN4vP6REkniexWJ1NcBEQnPq82Pka3MzkPRouXQqLDH0XrGLa7ftJslDskmRxwhcQYnkIAiMKl1v5s5ByHdQYRMqlEp3_l4JDGHk58kUqBmT69LmGguyqZ2UyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28675" target="_blank">📅 17:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28674">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=KVY2BU_c-4OTqARD9uE4T4RZPkoiIfERMj0STnypkv_VstoPkHOe19oGFBf-OPo7msJW0juh712GtbyBvuQxADisA5RY2-_Gq699VzHL8o1aHF4QX18JsatTYns1kNYUxOaqBTNlmMgBl2ta1AWm3usI5TsceS2rcXMTQjesBJ71PoCtVfT8xxRtJ2b79Xfxn4f5QLglJuqzRR1QX8j_lIHraURsAy1qcA2Bfy-kpU9OrYTCw_2WIGbd11yon3YvEYGD_G0g1ZhGIeyGUUB0gv8Y6LaSRWZzkcZ59_MiOZc05Iz9ZLWPTY9m_6HA4gdwlpRpyA3C0Pdlyo-rlGmNiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=KVY2BU_c-4OTqARD9uE4T4RZPkoiIfERMj0STnypkv_VstoPkHOe19oGFBf-OPo7msJW0juh712GtbyBvuQxADisA5RY2-_Gq699VzHL8o1aHF4QX18JsatTYns1kNYUxOaqBTNlmMgBl2ta1AWm3usI5TsceS2rcXMTQjesBJ71PoCtVfT8xxRtJ2b79Xfxn4f5QLglJuqzRR1QX8j_lIHraURsAy1qcA2Bfy-kpU9OrYTCw_2WIGbd11yon3YvEYGD_G0g1ZhGIeyGUUB0gv8Y6LaSRWZzkcZ59_MiOZc05Iz9ZLWPTY9m_6HA4gdwlpRpyA3C0Pdlyo-rlGmNiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
صحبت‌‌های‌خوزه‌مورینیو سرمربی جدید تیم رئال مادرید درخصوص جایزه ارزشمند توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28674" target="_blank">📅 17:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28673">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxbFlRzm_NTl6pzAHU2k9LRTiK5AB-cCQ7NvCzPZBvCYL5FHEGStZG1YB4Mz6Djd7hrKkRLSoRqGm9aK2HF5t_h3Fs2v9AxwWeq-shGOnyYsCAoWeKKYJzv6JBYPEyTaxN53fJljpqcsdb0vr6pEE1_w-iO9_HjvYkfLqnorfC-Inm8MYZ9cMgTzOqVhFC-sl4-A8Lbw2uilbnWHDWJnK1JZ7yYKrHGzsn25wI6cBBUddcjGymcvooatJBqOltw8xarNmIVCInRMAlQY8Dbn_y5z-q4lbhovrs5v7ku3MrOg8dwH7_e_5Mx3VpuahSlqjZ7pQkm-z5WDQolu92r4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به احتمال فراوان تیم پرسپولیس در بازی مهم امشب مقابل  ملوان با این ترکیب به میدان خواهد رفت،ستاره ازبک دور از ترکیب فیکس سرخ ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28673" target="_blank">📅 16:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28672">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=M1Pb093J4y0SxD-QRiRQ-qshdA6wVMiYiBnwXHmIYaPhn-B4EELg8L4Y-_FSWJLMGYtevQL_R3YfyxftkfKUTb9N471vGmhHuKDJHe8N-jFTjypgA1tt8GCJaXKx1sEGFuaBFjSsyy6qLSoLcp-WjEWscK2R-2_8TE0CflGk2aKypT5DFI4Uz89UqGWXmQQToyWpTcDUEB7gcyw4sb72SZ165V_gmvKzFka1YeRp4p1zhd6YKYBnrsEKPwby6dcQLhj7hJtxpZuzeRQgQ2JyGIwQDhkQ9e4tW8YeWV0xULEEAYJEqyqv6PfBDEw163jXTKprfsTDtSZQWopO-65zZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=M1Pb093J4y0SxD-QRiRQ-qshdA6wVMiYiBnwXHmIYaPhn-B4EELg8L4Y-_FSWJLMGYtevQL_R3YfyxftkfKUTb9N471vGmhHuKDJHe8N-jFTjypgA1tt8GCJaXKx1sEGFuaBFjSsyy6qLSoLcp-WjEWscK2R-2_8TE0CflGk2aKypT5DFI4Uz89UqGWXmQQToyWpTcDUEB7gcyw4sb72SZ165V_gmvKzFka1YeRp4p1zhd6YKYBnrsEKPwby6dcQLhj7hJtxpZuzeRQgQ2JyGIwQDhkQ9e4tW8YeWV0xULEEAYJEqyqv6PfBDEw163jXTKprfsTDtSZQWopO-65zZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇵🇹
باشگاه گالاتاسرای با پیشنهادی 50 میلیون یورویی درآستانه به‌خدمت‌گرفتن رافائل لیائو ستاره پرتغالی‌آث‌میلانه. لیائو ازمنچستریونایتد و الهلال نیز آفر مالی بالایی دریافت کرده بود اما به طرز عجیبی تصمیم گرفت راهی سوپرلیگ ترکیه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28672" target="_blank">📅 16:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28671">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt2z3laKdnn4j4R15Ht7uf9JHh6WTU0jIKwyfjFSABtVuhzOJ5tmuCkVfyF8GVAifUFSRkv6rp79XeVtiL8MdOp-Ai1eyjKoQ4MVwvS8nC6V5t2b2Iw0_PmV0nfLEd-tfs8YbcgLpAxs_MwguPwkNdWTWHBekCCEFrZH-ANk_VA3XqrZHzPfon73ut8KV6fRNZTY0J1jjNrZlaUPt3FWeTioRqa74riO3tVkls6KgHpgPKzB7Ay9YcmZQ2Ur1kBhfndTDQJG1JYcV7PSdfTKviVQIvabQKX1ziQqvUfNP1HvNlJTqsf8itxJGprPZDWCI1jUc0_wbvJtSFqgT2Y2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28671" target="_blank">📅 15:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28670">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e418389c.mp4?token=iC5ccFpFlir18YPy5lncp0HZd2NzCK09umuMr3WKWReOTm37k6V4nRrhmz5hIxsejTPrla5eB8dhk7HFDNJvFNayfUYVtdgLu1jexOTufxeT9d0qm2ghY-yjQlhawVHRmwovYllZBtfbQzdnIyOU6j0P2WSFEqXxXO-TGk6Hvl8z5nBjJIXet3PgfEAGJNd8xgy9iJjfWAcy25_raKjGcCFWdxU2y3HuGXlr9rNWB8p3vH8RHX1SbztnyG6ONzqePqqZ6nIXSR9xi-76avNYsRklV2dWwRxwYgVaEu6MaK_rJa-l_CQ4wkhbLkAcvfDQdz6vPtUy5yFJok96V2aFNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e418389c.mp4?token=iC5ccFpFlir18YPy5lncp0HZd2NzCK09umuMr3WKWReOTm37k6V4nRrhmz5hIxsejTPrla5eB8dhk7HFDNJvFNayfUYVtdgLu1jexOTufxeT9d0qm2ghY-yjQlhawVHRmwovYllZBtfbQzdnIyOU6j0P2WSFEqXxXO-TGk6Hvl8z5nBjJIXet3PgfEAGJNd8xgy9iJjfWAcy25_raKjGcCFWdxU2y3HuGXlr9rNWB8p3vH8RHX1SbztnyG6ONzqePqqZ6nIXSR9xi-76avNYsRklV2dWwRxwYgVaEu6MaK_rJa-l_CQ4wkhbLkAcvfDQdz6vPtUy5yFJok96V2aFNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالدو بعداینکه‌دیشب‌گل978دوران حرفه ایش رو زد یادش رفت خوشحالی گل معروفش رو انجام بده که مانه میاد یادش میندازه اونم انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28670" target="_blank">📅 14:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28668">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0MGlp27dBbcPmVftGFDKBXtbIW0FydIyRw00l_LMi-CMv0qHvvB57jlJ5SzgYMLhhj39BhMg_LS4SQjocXjafsuNGgWEJluNvBs-8EiFJ_DoD95-MEJvEmp054jcBAkqYGoIJas8QnfSGJEXVrQHST-GkeVowa-D4eimlbhvNo62GM4g4escdfuNXwLqhVX6-t_T2vJGsUCpVaDWXkBkFlwcaQGNOGmnS4MuI0eZe_wu7bC4OapOpBNxYebfwZWD-OhqCW7Io22RfY1Vm1rJP8POAYwD_-QA3dK14OM5hCdqFcHChtAoke1GlTWzLHW-e3AsouujJtjXhjYuG_jQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gGXEPLcW2Q347CXJY1yGXopOzt258lse9f6V0sj7kJ6yuG9CYpE-wcQ8Sp5QwWyBzTzEfTO836xsy3tJTLlL4A5wqwfT7xOB4AaOqUiWte-Clu3e8JVUNpirVppEaw7ngcNOhcZb8ZkJ0IY_vycL9teZBy1NVWsLCbqbQevF2hojBuuapAfkNsL6FgyWJXahq5ndhScUil2bAoipf0Ub67Hhcu7lWO7kAIzVWoYU6yN1Mys5Uq-8wxiBEEEul2LXRXpzE8zSwyZvv1yi_9CxsnxnQXv0lLppEXvaYCh5ASryLfBEH4t_D2xUZiZuQ15raqSU9gBLKNnUEMEQdjEDIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب دو تیم فولاد و استقلال درهفته چهارم لیگ برتر؛ بازی در حالی بدون گل به پایان رسید که آبی ها امید گل 1.4 ثبت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28668" target="_blank">📅 14:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28667">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js66JS6qQwIoftyzIrFRBKbRaGP4oBBLJX3teMFf8C3vqGzYpCbZsTWw7QKy7rNKJS4WH0G9CtyZQU9yfz0KQLy_bs5p4bSuo6mj21SPfEz6UxRHXCcU1NG0Lq9_A4n1R6zK0eBShgdOYF3kDRntCv9Ve1WcY4E-allHaa9XP3hdKcAchtxyDosPqiHiubD0J0atq_jefHDF5PO7QxG5fnBpjiB34fssevmBlauvyf16XoqR-VwbrOe_mNcEtfsAhrdeeIZfUQ2YDHM3KAGW_J1KQI3NkLpwa4deyGMOLiiSZk63et0ODnYcuI3ARnVJTs-4Zvd3ukUi62Sbmuzw_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28667" target="_blank">📅 13:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28666">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=D_rGSu69QUheQrD-8RkluwzDhMZJEeziN8CHQ8ovnYpm-IOMtjiW3SnZuzOR9GEh83-t9bLVflr8zfl7dpssCxsW5394Z-zjMpTthEfKNbA847jhpuDMtz9VEIvxu2m1AzH7Acm6D4TECI280-BdLuLORQbR2fuQ0saC8_fHcSNmWujj6KhmE1nIpt4nf7_5OSuUHbw7VRW8HMCK_Xe6T9aVq9LzQldZv--4MgBFIhbPRAt_fv4xDDTSRvz04pG-5orVDTa0l0Fvsb-ghzlsU81cdpMWK0dCWrHVu98_mcsp94vltn_J9aMTNF9WowrZ8znOkYZJ0HL3MIcOs5RiQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=D_rGSu69QUheQrD-8RkluwzDhMZJEeziN8CHQ8ovnYpm-IOMtjiW3SnZuzOR9GEh83-t9bLVflr8zfl7dpssCxsW5394Z-zjMpTthEfKNbA847jhpuDMtz9VEIvxu2m1AzH7Acm6D4TECI280-BdLuLORQbR2fuQ0saC8_fHcSNmWujj6KhmE1nIpt4nf7_5OSuUHbw7VRW8HMCK_Xe6T9aVq9LzQldZv--4MgBFIhbPRAt_fv4xDDTSRvz04pG-5orVDTa0l0Fvsb-ghzlsU81cdpMWK0dCWrHVu98_mcsp94vltn_J9aMTNF9WowrZ8znOkYZJ0HL3MIcOs5RiQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوسترباشگاه‌لیگ‌دویی لگانس‌اسپانیا برای آلوارو مورتا مهاجم جدید این‌باشگاه؛ مورتا سابق درخشانی در تیم های رئال مادرید و یوونتوس در کارنامه داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28666" target="_blank">📅 13:41 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
