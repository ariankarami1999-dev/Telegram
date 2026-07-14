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
<img src="https://cdn4.telesco.pe/file/RGcu3xmIcfBQPfslLY6VZyssRALkeDEjz3-XfK_3Newv4EzX2eMXZ36aTBQpCrzPGMidn6AzyxyQjuu-MPlPish4jsl4manRXxMD6Wn5g68VH0fxDNeU6Jq_bwnGYGyHvGilN60Na4oFdQ11LfcLR3lhCNVcnkT5llqvW3y188HrKfxTfrsQGElzQ8BAEyDZMJCVGfgr6nKQTiWWV_OHtvF0sqUDlNTDXvNaOsPMFT7HvfEsUUasTQatDETSVBMYCgmrrO1lCUKHWix7yuq5vdir-D_sejNDoL0AJiiQyxPl8PQMFbNM1q8JkzShlMkdEQhfJEBXY9x9WViKMRchRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 460K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 21:07:56</div>
<hr>

<div class="tg-post" id="msg-25697">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obzQKmNs1eJ4LbI0Q4o0S3ybfDKY79dzELtiXC3nQw-km5B3AO_3Ov57iV-VS3mEIwpH_4GDXYGpzpNCI4jd-kd4Vg7h5jH6dALlaIaU-lvD_VcUye4XVSRcZx2F76hL3zxw0q8Bp5ivz0fztf1J2PTFIOV7JQAQNsc2r8a2BwRVOjodT9NMeRuYhMOdp9gY-UAHyYANc7csJMk-absBkRuJ7bpHcvC1quo-IHou8jZwr1t_KnZFT0q-QzJZ6eguiPLX6VuEnptaY8NNKZb11D0Jgr2xLK3bC8ykObpsvsTbMuU9Tm2VSsp4hw17wz-_3633WJvu9A_hsoF0wOryxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛پوریا لطیفی‌فر ستاره‌جوان گل گهر امروز از سیدمهدی‌رحمتی‌بابت موافقتش باجدایی از این‌تیم‌ و پیوستن به پرسپولیس تشکر کرده‌. همانطور که‌درروزهای اخیر نیزخبردادیم تمام توافقات بین سه طرف انجام شده و به احتمال زیاد این انتقال بزودی انجام خواهد شد و لطیفی‌فر…</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/persiana_Soccer/25697" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25695">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH48wKDkQvtoQ6g5k3YM5XGypYCiPRfk2UuX8lVDMvIskCFY8_L-sgu9JflJkQMd6H2C6lOLSftFgr4O2iLzRcNFW0Q0b9NA4wqZI5aA8x6oeOaQb4sIzCqA57aiVqmIsEioexDUGJ57DIxuQFJvI7-zw7zNUZYCAK_TChPuoUX8OmJbJuL1gVlz75bxFnGhwIy_KtapkWdR0JDqMPN3kd4gJ6N9HqMxS0eeep1o1HpV1SZq1PlwOc7BOgO1wSIdnYVJ2g7-E4ILoEDFkbdwdzdTjo51EodqQcaapxZRn9uaZvrg7VBnEwBEovXpf55ZWfUpREg9D8OosCHXrcyfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oh951LdfyGgH_bVXE2_IT8jfRngrt9IxEQE_ml5z7TWXf7Fo19NWUJ19e9LzbgmKiY6erJxmkip5ctU3892Ms6D74Lqr8ekUfoGb3Z-ba8TNAnBytBHjoNsUCBxwvTWprZfcfz2gubVvLYO8aoncfpDkcnvxJSjn2aWXrKvNAiCcRBRb-mH89X1UF1vc96OOo-vYkXOIxsOpZ9edTU5ElcuuvjdvRvYB-wTsuVaRCv9LCHyU6k4tmVOsYmleEPgbVhdNfi5bcfsPhejOVkK_0UBvevuQTp9pzLqahNw76RYgGI-MmWjgHbPhJDSQ8zVxDZfH0UjJezGkeR9WpuNaRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛
شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/25695" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25694">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ4VuuJX86IZnwDx_gNlrVNs8XwWlCiDQbnydpKTYslzDNBv34gFa5_s7LilvIvrIPYzJIXgDdzDms4oVO0yb8eeb_sa-ed57pxgNwt44vz44y613YnBrnGfHSHNzMk8l0VsHHRoRxJt9068PgwQlG6yZDM4Ef4wRyx7iOsIxQrwu2HxZI3gIzZ3XNo-iMfl_TeFdbRfaFWcmZvTnSmHp4MeY4YhePHl4zWY68yOMMuli4lR-TpnyV7-LjfON6y3-_CHB6Vsv90UDkddo2TCcvYXMheclzstW34uq3KKrHqiDwy7h5qioZYtN2m2sK6_2fWTXtcIzT5ByCPQDzlK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
کمیته‌داوران‌فیفا پس فردا عملکرد نامزدهای قضاوت فینال‌جام‌جهانی رو برسی میکنه و به گزینه نهایی دست‌پیدامیکنند. علی آقای فغانی در این جام جهانی سه‌بازی‌قضاوت کرد که به بهترین شکل ممکن هرسه بازی رو در آورد. یه کوچولو شانس باهاش یار باشه قطعا فینالم بهش میرسه.…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/25694" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25693">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eimQIYOmGkepOjYDH3rSdreqrhsnP52Ag3Eue66moK8nbioYst21x4daNXJ1pawMFpP2TBKrpGTsKrdqiljmrC-yJszobOlPrmH06r38whEUT6X9bB0uHVJoqeLd1F2g70LjiXnnb4rzWVr3bUi8EwVvlXM1Fw81MCMCQpQxWIBp-x7GZsFiWmaSjT8WPb9W1uo4lUBjVGAiSPQ3P5FAzUbf-FZ6u9VYGgum6oyXrymGrY0jI9IUw5P7mFPDN6WVe_5J9BkB7_QjBayGoYA2j7KdCdhPmLb9Y1Kj9nV3scsg8AY-uDSjwjl6DCkw9jk9Wu34EUv6m3gGheQmSlmLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/25693" target="_blank">📅 20:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25692">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-sfXlVuZQoodC7-z6i8qlQtP9DC-eu1k_VUW1R7wCEFtlvd-vFuyDJfUnRminFJq9osPTBGFUPiw8lJLqzC5pKBAZJrzgk3g6pgn_gdobCzTNPaaJA_JlalrDYe0cnvbh9yJICiMuW0Kh6q4sjldEKJXijE6W0nIDEcclNp5beDou3R_VDrV-93t3jlq16-rdGGSOoPfnJXwb5kDck2PzUcejiIt9T9QQuZ8Dr9eV0yWzwmnqnmbLFX-UyKx62gUBx-Lp9Fwpc8rDD16qbBsy0i5yqfIw9-1nuUIUJGKqpCiGpTmdMMD51YvhJTRKdx5HRH-PrZFuuc4UDro_mPQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
یاسر آسانی ستاره استقلال ساعتی قبل با ارسال نامه ای به مدیریت آبی‌ها خبر از فسخ قرار دادش با این‌تیم بدلیل عدم پرداخت مطالباتش داد.
❌
مدیربرنامه‌آسانی: باشگاه هیچ‌علاقه‌ای به ادامه همکاری دو طرفه نداشت و از قصد مطالبات آسانی رو پرداخت نکرده تا او قراردادس…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/25692" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25691">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAqpsYOtATHNO_827NeugGBupsR5O4CTmrQgo1G-hyCUyKj0gJPZW8Au0xytNEodIsYplY2UxzWnLfeH1Ro5ulKi9aELG037kEhOIMocWi6vVGyzr6EYZD0qs8bWE2Lz2bvMCC_so3t3rZ0-2oRJju_a1rtZwROvzGOE6Em7g5opGE6efinfbX15VEZ2piDS_F4AUQV-WLfdJLbESqHEdBz9vbNmQExQ87m_MgTfqyT-7LvtJEhox7mZVUHCRKDnlc_10lSl2hIg9SV_I5d6f8vJgyYanIgRyURokr_n7Wc7d44tehg_gJF1buDZB07yBDjNKN5SWkj1WKYcTcIT5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌هیات‌مدیره‌باشگاه استقلال: یاسر آسانی و منیر الحدادی با باشگاه استقلال قرارداد دارند و به ما قول دادند هفته اینده به ایران برگردند. امیدواریم به قراردادشون پایبند باشند و آن‌ها رو داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/25691" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25690">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/25690" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25689">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZe-7RHbIs1eioaF4FceFIfTZNpZgLEljG483O--oTJuZPnZ4MfoCbyHXX8ThLeqWPjnj75UryIxDndoHrwmcpdvlTxWGgxwO2DS8IpLawkKRD7-Vdlm0FFu9oXaUST3fMFVlyS05iNl2-joTyYP97Wl_T1bTV_tAsuUFaT4cs47otPCYtUKbAU1ESjR8zQlF5U2cJVU600V11GMuOzfCT_M1eJouUBDUIZI80YZYS3kVURH6XiD9NhW1WfxoVPa-oM91wVHh4sxEHyzvYF38u10h8FvRIgisxGKXncwPEfRrietTK9SGmIjLzHu2u8mI3k3PvRh7hAD30tiBBnRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/25689" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25687">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONoG5C_v9zg2V6A41jbnPzvTUmuLxa2nesE18NR6T_JP7ESiJCuxDby477nqta7ZcM-wXKC1YbQnwxdafVusxZC4yhC3dblrfDYjHwy5as4OiKJljOZeyI55I4uTTa0-QrI8nnJletAXqnaroF7AhFyu6R9WpraNiqgZ4ShMdTSs7e9WH3386H2PzUJ_cVwJQpsYdwVpPX1ip9jfopRfimi_2EgM4wrYBs5e8oqhJGVdgk_w00LUKaecXK48vUGLaErBpEWPIbNcv1RXiUaSdJ1LauQyW028-CtXgJijauSA8QeTQSGXpZHuFurzTgmuIK8dfMsJW0GY_vvb4M1dGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8vbCiihuY_cUM4ffYa0bPQEaB8x7j8hg0xusaf9h7FeSXbjPfdYU1MqgVmQy2huE4-F31JVII6fvS9ShwRPC7r9K45foeQ62wCv38pPer-pNpRgIPcb28jQlVVYdEXpUIYaru29veIZooXpgSLUJtGbuTfqK0CrArLNCnDFKgbQ15TWRZRC3Q6Z72cWpA8PcHtRgL5rZA0cJ_0CF2sAAqc2mGfs70tOibd9UOr218LpnFvkI4XpQpsYtpgOn1afp0phC71vBRvWnsliZbSKCYdVD_W-cZmlNuZ7VYGRAT5VOx_etyIq77jAtGoEV8yb4f9fp6oCH6l7w2dmAnf6qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/25687" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25686">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGCpvVZok_FztYJ43Tq_JVa8-oTNCPtKH2BxtMIRQ3dyfBYJR5etSONYEniT-ztYIwcNbY3CsqnzYtBfa2030LmmGrdZVF4CsGI5liDnloZwaHbaGg-toaOf0k7TovjUozhdcpMc3OjuxuaGLYCijLCfZe8FzotLIh9zEib0QgUFLm-nw-8Y3JUJ-bz7IhAu7naff1R8MxP_GD2LTuXxFZTZLua6LerM6f8590KZgU2-QC6pMVytVTs_UOnjvt2guw-Ab82Sv80GB9B5ZzG945g1Exjx5yTAopOYS0eTgc8shFpV9hGmmGSXobnQ2o-3Fziebso2kCPRUZvl7mEBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/25686" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25685">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYzCm-Gff4UbFbKd_EXn7Sz_bhrswI2UX5jbUiEK-f_rdFX9xQ_TIqGegNHKEeGaZcQ_y6OA0-ID4SZDA_J-e29OUeGO3rMwJdL4M-SAAGZASiQLvWiFGG0Rg2mQKm0vFlSlQycMdXptahATgzTd7hPIMtrN5bD9FFq3sKLmwFMyTXC_LNmJQ-RmnDE1RNPwOtA0mc48irpWg56a4GDj9FMmZwrYS3erm8xBLx2eczuthFDIxUS5YYKjocd5VR4SJoepQ-P3gkq3fvDfoD35e_ss39paZBHuIMIuTzrusRbMTpXyPepNkF7tINB93UMEbIWhWs6045WR-LwPtziKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا؛باشگاه‌استقلال علاوه‌ بر پین؛ با یک‌مربی اسپانیایی که بالاترین مدرک مربیگری اروپا رو داره در حال انجام مذاکرات نهایی است و به احتمال بسیار زیاد با او قرارداد امضا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/25685" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25683">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6cxROF32YOiorVKKno5WmRT_T8XeLdVe2vMF__Ra21PIVHT9VgYNfGBfRyQ1tmoyqOKl7Fu_mSlKAQyebmzlpisiDKgfLUW-JIQ2HFAICZBsPiLZ1ee2uUtcC1qmUXM276PHfsbe72IBElUQXDYPzjggaLoIfyZsFTIHMuMnVb1u6Lsx-bp-55p0XSul1q-eeG-GcA1hbHOqFcYcukvtoJoutfF1qev2A3uDRGfuf5AS9Td4-FCalikRsORqYaT38TA89guJ8zNfGjfxcUjmXCQl_ttGYG_k4zXhYKpAmtVQ6SjLI4jy5SDKjZLuR5o0JaaLOJV5HHsyzj2ItsTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eo2ENMGups1Z7nf2h822ojfdArOAI3ISQYOYvk1Pf_x10AqU2blIwL_Ui5Kt7g0sm5SjyOi0S93uM2lgDQo_XlCLKDf1uv7eawX3GqtZYy4Pr4bV1tCeVaeDVp2SEVPdzuBYi2s0QfzHfMxU9yb9DElchnDCNXiRRfMSDgpV46HCICgA41oVPtphzoaCfHqdD3hmraH_oOHjJN0Jr7vTwjvsAWPt4tf_H-4TPcAxUQYBkwWyXF9k-soAFCBTkXwMTwWk2uT0YGFi0S7C9qEyTbi8hOWQ4Orz6ozWDmdkrPoDMuCr_k7TZDnfX-Z1B6BNGdbXvyUdnvckdCrW765Ngg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25683" target="_blank">📅 18:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25682">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏆
40 سال پیش، بازی انگلیس و آرژانتین یک چهارم نهایی جام جهانی 1986 گل دست خدا و گل قرن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/25682" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25681">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq-Bo1CfK-9Vw7NWEinnvnnrvR7-2M39V4BoCHyZLKj_PG8WljmUIT_xbZ6lILGuUF99csQTHSAUOQPH4a2Ib53dmKD1LBlHAOkl3Z_887MCE7KP8NTpgvNT4F8UMW5p591kb9CH_9EdcwB9dfuRDtl9hjMKlNgyFt_Fh8_PK9V2s973-7bABhdLYplHIUGMwX7WkQWUXHB5A6zvbl7kFCRMdbsZOCQhtSpimK-l9L_kukd9bgMuSWrdov-vchbwWBBVyQG9hD-XnHuP8iIG-qooLJhF1wASFwR-eiixnqi9sN7TTPgnR8qH8V1n96odn9uPZkpXUA1VjYqWOUhlaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در انتظار دو دیدار در نیمه نهایی جام جهانی
🕐
فرانسه
🆚
اسپانیا؛سه‌شنبه 23 تیرماه؛ 22:30
🕐
انگلیس
🆚
آرژانتین؛ چهارشنبه 24 تیر؛ 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25681" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25680">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCvi9xg4xeLltkf9YePO9Ec-s877JD2-pOrJkVTS9BJjToK754_IPpCLbyS_SBsLjyrqlZQyWfMr-wncx1jivK3ESKq62yNUS_Cx4Oumy62SveK1bvBqUl2f8PsxbqUdjvI2miE3kZne1wUzfXH87Hzk5Et92x9E0Ur1uyk5oQ3fdPoVILqfaU62P-gCs1_KvfIl47DHpdX8CSYPHG8yJWLohLGsdtPir6L_WsuDviWnMj0wW2vrYCXMUZISchqGrmie6gtDV3Vx63Y5lEsa8onXA0aiuLok7mfjQIa53FqaGmAWt825diKTS474-G15g6CB4_BFioSe7AoaQ3Z-gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مسعود محبی مدافع جوان این تیم رو 350 هزار دلار اعلام کرده است. یه چیزی حدود 65 میلیارد تومان. دو باشگاه استقلال و پرسپولیس به دنبال جذب این بازیکن جوان هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25680" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25679">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtZKSmmBAb36WnoEdObz4jy4ah7AHR7wt5fVBzqVuysVrN170WxLiZBnu4uEHunjhMlOu8i8p-88CImQvRraDIxlvKdoYwsZHdkwRD4EdB5vDC_cpEEl4eM2DHKkOPeqkIpYzqe-DOOwzWdFCISxBJN0MoS5c_GHeiG3ddB7pknDy-OHAy-eVPrSoXFyaYwTQ78NmgNB3rzqEVo1RHG5Ak2QL7xms-ck9ZAJVdE9B5pH0w7OIjLAb9ntZKc6wMry_xcjqTAI64f0VL79XGfNrlKTTtBYeFjEOX8xGPqV3cS47ezXx5vBOZkev2gMyCznpxzhB8PvmPv5StYg_imaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری #تکمیلی؛ آغاز مذاکرات سرخپوشان با ستاره سابق برایتون!
🔴
بعداز صحبت‌های شب‌گذشته علیرضا جهانبخش در فوتبال برتر؛ صبح امروز پیمان حدادی مدیرعامل باشگاه پرسپولیس با کاپیتان 33 ساله تیم ملی ایران و مدیربرنامه‌هاش تماس‌گرفته و پیشنهاد مالی…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25679" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25678">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0mGgrbY3t1DIJ-MdKR6mVYN7as0LeejIsYmWmd4UCzrGdR3O8uc5LUQvx2xG9Eu-PutnBSYnUofhs1RnDHQVSvQioa7OIDc68aMtc6WKCoDcjIei0wKe23DPz6xOT_P9gj54R4m8u7v2ak4_cGf4icHbS5jBBJpsdCy9-vpnEuBE8MJTVSgXgtWMxTBijSxlHziC7gVj3nNHzICP973GPRCrPweF2txfZY8Ai6qo_4Dp9xoA-NOfYNC3r3NdBuWwhnTx76KXA7An7p2teLxppma7IJjuet8HQuvLxdZCChOTPlimJATdWYr-nDyEoBukHXRgmcrd25zQifoAQblCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی: تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25678" target="_blank">📅 17:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25677">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-1rMzDsH669EIrd2mk7P1mwpKBnBPsGh6FWaSWU94nzNKPNFLpx7CchC9dLV3zIiMVGBlfi6rboXraBTKSzC_RrnObDf__j0lzyfUVJo8aG_kGB_04S7B0HeQFmQ4GSHNsnLYVgP2Nyh3jSZC9GUwM551wGVAwawU8_mjOonFlsbuxUALqTrNhTBqpC6JAGBJcDR9IILF7YOLK2H0a-7GjAHt2n0AUpA_R-px7OCFQpAPRE9whSuxOFAZW22DwIGYm_E8rJr48qzUEUdpZpY7solG4_5AtuODnuM-Tv3MUFmVsUONwyYTRs1YIl_gh4-I65cQxz38b94GawnBtjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسی، نیمار، رونالدو و هالند اگه دختر بودن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25677" target="_blank">📅 17:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25676">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTV4dROefUiO0u7oOWWL1KF7P76ByP9LgMzg6iEA1hYZ6Lbx_Qe2offr5JjaxTZ0O8AWru7Uw3b0be3eNahf_XC_2Wzyn8JHbWpJlSUaABV2h3nmCOMPdO2gQA6ylS58DnXH4rLC8qhDaIi3YMGZLiEmZDXz7dgKh7h8asOv2cf7Od29pXVGIAspqChOd7j0OI8VrGJqTkyu6uo5LDOgEFwDBcbynIVX51U0naPDahfNHjGgWHv0oNuv_FChusz1tN3S1jWD1t4JDjCpS4KYsu-EyMGj3-Zp4_RLu38fiRWBMIupauCd-mXXCMid45VBwkd6v2v34mDqZ50VpvnVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... علی کریمی هافبک سابق استقلال با عقد قراردادی 1.5+1 ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25676" target="_blank">📅 17:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25675">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBJWSR-yAJCxhKtEb-PCKYCu126syHB7B1LBa0EVomKAotZ3WNli4SjKtqfkC5vijqMinGmwGlhyM8CC-aINO-uSGz99Y5129ryf-AO4W5cq9jufIG47ueJX99y03KSbD4Re7i38iVoP2TBPpov-gkGhBvm2eUfBmdaR721NJpI-wBf77RYcwsEEihcJ58-MXvW09Mjc5ryQ34cJ6kbj85wTBrwWN-DT5laYtNUiJsrUo2V6Owz_ux15791VSxLHrGQduaEkm5ipPCnODYMzSVdeGw_bqSo6ZDLYzQo9T9Wnl6SUyYJooRN4OsasuuPRhTuZbjjEWeN7S367dIrT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25675" target="_blank">📅 17:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25674">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0znaSXysMmU5hTNAomq9Y_W8Ao7jNN7xoTMmm3GC-Mu1it2l-rxkiHCS4us75IOGv5nlA5GEkTYFXhSu-9hQfOv2tKrta5zmZs5ArJQ-Pi14s8my1vJ-OPQysUeZTI_F0mMB5zzh5hbpHocSG3TqdgImHCRP5MFeeHhfdNBHj5k9LYVpBjyiq_YQvQwJ9Vyb2W_glffYLzxG6sycy_SEFgQD4OeVz9v8gb3aZsKOL-omcIjpk4AUWd5kuoYR5VoO7vLLxrueXn6D_exbMqBGvqWDv2y3lZn1p9HbkoSO1kT8FUjMEnh22rnV9TTQOPR9lxnc0zpRzbUh9Wdw1t6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آندرس اینیستا اسطوره فوتبال اسپانیا و باشگاه بارسلونا مهمان امشب برنامه عادل فردوسی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25674" target="_blank">📅 17:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25673">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=Zuc-4Apwc8w9gVyfbpIH5UQYL9R9tknWth5Pcu0YF47moFKsE9dD8YDUWe1PrYLIum0uweKWfTrgHZhcTMrXp0bB52gNFT2z5znzOSF4o1kT992RISTBEKGOUjGLRMkrCSIjtqqpZgipg0YZTKliT9xee3AjO3Ti0f1TeWUpLX5uCO5h8ZSM6C8pTF5o5aawCeZL8Pmbc4FUV4sh2tM4jC7fEjhE62rhDQEuEAbUDK5W1Gtvucwe3MWyFQDo4_Ot5-Qm0OxDwnUCbDmcAf4f47KAnCoC7twUA2-M58DcZ6thutW3Lm8ye8wdea1K3g266DBZpsp_--gUFm-Cq_hymw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=Zuc-4Apwc8w9gVyfbpIH5UQYL9R9tknWth5Pcu0YF47moFKsE9dD8YDUWe1PrYLIum0uweKWfTrgHZhcTMrXp0bB52gNFT2z5znzOSF4o1kT992RISTBEKGOUjGLRMkrCSIjtqqpZgipg0YZTKliT9xee3AjO3Ti0f1TeWUpLX5uCO5h8ZSM6C8pTF5o5aawCeZL8Pmbc4FUV4sh2tM4jC7fEjhE62rhDQEuEAbUDK5W1Gtvucwe3MWyFQDo4_Ot5-Qm0OxDwnUCbDmcAf4f47KAnCoC7twUA2-M58DcZ6thutW3Lm8ye8wdea1K3g266DBZpsp_--gUFm-Cq_hymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25673" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25672">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeCY7yzELLfWhYa1L8cBls2uT7yWFCTOHTzTgqYoflT18dSdLMbE0BSe6NDvnkhvqvGBcDAwKJR--EXQiMVAKqW6Clc2Su-0Eh3CzRmyHSbHcWqjZBzI2oKwTj7PWBb6-9amSDdOp0apf0p-4NlWAv2KprnOqzfdJ2tyr6cSU-Hm2r6Ck_sI8iV9vCIIp9_6c6GGfFD-5z_zGbJOpxAzbObZ0oauFCkHWW-QeUO0QjXrd0wBw0ysdwHt7tbpmyRjftJZAFeMGSesBAMv5zC9qXitrGYYO3PRE6RnmvwI-iN-MTWq3CbY1urCTzTD3tphy8wiHnyyURgU4j4ZABNbuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛فرناندو پولو خبرنگارمعتبر اسپانیایی: بارسایی‌ها یه‌فرصت 72ساعته به اتلتیکو برای خرید خولیان آلوارز به ارزش 100 میلیون یورو داده است و سران اتلتیکو رو تحت فشار قرارداده تا زودتر این انتقال انجام شود. آلوارز به اتلتیکو اعلام کرده تحت هیچ شرایطی فصل آینده…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25672" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25671">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=uesQdjV1W0msJ5AMVwf0I5R5G_AadY_aA5qA2rMAI8UJYnHWJDUJIu8qRBegiJDOWUE97QNC9oaSVPRCZELEmmQ76ol1BNAVPm9ArvlxqM2-8L6WIiHMFqFiwDIDUVKUONBaNlreEmNPp_Lhjs3FxYZbMRWyWAl8ezTUuC6dgc5pRR-CkzgrwwhCN82fgsB-i7d4F9ftVgf_M_j4EyNuAYtmfWo-sk4Qz-VkFdYT3yHdF037uHFTwgXW3RkXLTFGwRSB_cxhLcl7oXGIeNH4mgyr3Zgoal7V5ph1nKkQ439kwFiMQDaHAgofbuFjLsdHx8pDBjN_gV_Gb9Y5d9MxEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=uesQdjV1W0msJ5AMVwf0I5R5G_AadY_aA5qA2rMAI8UJYnHWJDUJIu8qRBegiJDOWUE97QNC9oaSVPRCZELEmmQ76ol1BNAVPm9ArvlxqM2-8L6WIiHMFqFiwDIDUVKUONBaNlreEmNPp_Lhjs3FxYZbMRWyWAl8ezTUuC6dgc5pRR-CkzgrwwhCN82fgsB-i7d4F9ftVgf_M_j4EyNuAYtmfWo-sk4Qz-VkFdYT3yHdF037uHFTwgXW3RkXLTFGwRSB_cxhLcl7oXGIeNH4mgyr3Zgoal7V5ph1nKkQ439kwFiMQDaHAgofbuFjLsdHx8pDBjN_gV_Gb9Y5d9MxEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کریم باقری اسطوره‌باشگاه پرسپولیس:
تو عیدها و مناسبت‌ها هرکسی بهم پیام بده جوابش رو میدم. اصلا برام‌فرقی نمیکنه طرف روبشناسم یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25671" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25670">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=P9ijkgYwO2VT0eKcAl1Qm6CuM--sUuYQjI-NMLxrPQlIs8GvQgSR_9jhBHikI_gav_cdBjGVP6iNydX6gjhqfORP4HbTZZTqh-N-KR-2qT1b2yzz8AQ0NIfAujNfAmvU9ld5k3qw34sD-w_eslAqs9DzpiX8n707pJmvMBSnVM4jyTEA8vOkHuw2LcHguEPBA0jcKphQnzHE3vcm-JqE-NY3729789pUZSi37nUBn-IX1V6VWr95HpKv1G9H1IKEczxComMNPJjAEVtatpr61G5Pvpx89tlE2l_yEzLx4xlmkcp079vlH5HDe24kKVwxPUAvuD8SoN0P-KStN2YRu25EiJ6-GkPNsTLDFvXCBlA_a71pXS8V_Osz0RvhziO-a1b0kxFcYkTo7OvSb2hKMqSrXRQ7km6sEg4AbD7rMHnhvh9GMQHR-sDvkg38Y3io648eXSpxOXvYeyPBX9_S3fkfSZ8b2xCp894cyhV5ZY6bFzhFv3q8C3SnXYbb1WghIsm_vyphPlBJ5Ky0GQkywDedgpUt1k0dfzcSNhC7BIvoxCG-cHRwlAjEuOlAHFkgi1cmnUNV0N8uZNMRFrbHLN0vHdNRQovs9klpG3JxfajUKFD_3VauGOcHL5ptnUv39wdQc8kcLb9th4eitI-Wy5AjwlaXUJGPYrpSRxqGz5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=P9ijkgYwO2VT0eKcAl1Qm6CuM--sUuYQjI-NMLxrPQlIs8GvQgSR_9jhBHikI_gav_cdBjGVP6iNydX6gjhqfORP4HbTZZTqh-N-KR-2qT1b2yzz8AQ0NIfAujNfAmvU9ld5k3qw34sD-w_eslAqs9DzpiX8n707pJmvMBSnVM4jyTEA8vOkHuw2LcHguEPBA0jcKphQnzHE3vcm-JqE-NY3729789pUZSi37nUBn-IX1V6VWr95HpKv1G9H1IKEczxComMNPJjAEVtatpr61G5Pvpx89tlE2l_yEzLx4xlmkcp079vlH5HDe24kKVwxPUAvuD8SoN0P-KStN2YRu25EiJ6-GkPNsTLDFvXCBlA_a71pXS8V_Osz0RvhziO-a1b0kxFcYkTo7OvSb2hKMqSrXRQ7km6sEg4AbD7rMHnhvh9GMQHR-sDvkg38Y3io648eXSpxOXvYeyPBX9_S3fkfSZ8b2xCp894cyhV5ZY6bFzhFv3q8C3SnXYbb1WghIsm_vyphPlBJ5Ky0GQkywDedgpUt1k0dfzcSNhC7BIvoxCG-cHRwlAjEuOlAHFkgi1cmnUNV0N8uZNMRFrbHLN0vHdNRQovs9klpG3JxfajUKFD_3VauGOcHL5ptnUv39wdQc8kcLb9th4eitI-Wy5AjwlaXUJGPYrpSRxqGz5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
رونمایی‌جالب‌از شباهت مربیگری پپ گواردیولا و فیروزخان‌کریمی دربرنامه‌جام‌جهانی شبکه جم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25670" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25669">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-g_760eFBS4glTmHdN1V6JBV9b-vUt36D9sW4kOuml-lrcuBw_jT91NFZy3D3z4vXW_eO_AjsbAMHAlqV_as639xtlRABgACnIu5T0AFugtKmis9wsPTF8NDqr4oT7PYl98E3xB7GBnARnK2_8J_glULzrQxjqGVt_5HiPPTcjVrvcfHUZ_67liX5Gv3r4l8qste4dYYLkweeoMHqFh1avdO68xjqP6HSlfNgZHoeo5BuuA3pmAMecR0rRd8FnElc8XhBKmONKrcL4QXHBKrsa48qKOSzALzyxL06Dx_Z8RvZQvci2ftlDRx_3Hqwt0_TUBgAGo1wUXPFrRWSC3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
کرک و پرتون بریزه
؛ رئیس فدراسیون فوتبال سنگال گفته که: من‌اعتراف‌میکنم که بعد از حدود 10 سال متوجه‌شدیم‌پزشکی‌که همراه تیم ملی بود، اصلاً پزشک‌ورزشی نبود؛ بلکه متخصص زنان و زایمان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25669" target="_blank">📅 13:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25668">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd10299011.mp4?token=QQBRza5k5GcuT6dfFI5QJUfx9DErIt-mmetRX5B4pNwqoczEPSNU5QcpcUxGFKejZlc4wXhIZWa1AphsAujMB1T2CW04aI_NfMTrVEJuU45pfu7mvlpISGxxhYZZwJjtgxzo01yOWNYvMZVrUhJ71B-IUa-tVrsliW2shTFaS_MJfArc3u0kKYgVgjqby2HV-IgJtqHSol__nUM_VDx82K3Dcq14X33e78OgR07PYfldOIg18Cgx0_5C_cibE1zqO6rWpCrtVMgIXy03Smf6f-5tP_EwBS4fdKdJNIF1H0XnuzuPlDcK8ssPXAUw35-5wmw-edVKH7E5C60G9U6UdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd10299011.mp4?token=QQBRza5k5GcuT6dfFI5QJUfx9DErIt-mmetRX5B4pNwqoczEPSNU5QcpcUxGFKejZlc4wXhIZWa1AphsAujMB1T2CW04aI_NfMTrVEJuU45pfu7mvlpISGxxhYZZwJjtgxzo01yOWNYvMZVrUhJ71B-IUa-tVrsliW2shTFaS_MJfArc3u0kKYgVgjqby2HV-IgJtqHSol__nUM_VDx82K3Dcq14X33e78OgR07PYfldOIg18Cgx0_5C_cibE1zqO6rWpCrtVMgIXy03Smf6f-5tP_EwBS4fdKdJNIF1H0XnuzuPlDcK8ssPXAUw35-5wmw-edVKH7E5C60G9U6UdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25668" target="_blank">📅 13:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25667">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=h9zustLE1RR_wJ8EsOHKwf0Eq2dH8OsWnkaRa0MiPQ3n2ow0F1EReCkEb4_uS2itELxj1boHTzjejF-nTZNvwYTXV_plGVf9Wgb_-UM18lE2SwCw22017WnN5hwLKTYHB64QSyA77YpN6gWfsTJxad5Fqeu6Pe9uw1JmECOgZkx_donnzVD7usBpphPAABi1ovLX1d3YqWi7E3pn2LYD2KmDxO9ChaU4pLeplsuKiocHxqVDfGg9QrtCaVuZ86vU_hYT8FgwgyfvsBIoW4FiZ-x7GpSvFVv9-xa_C3uWKxR7VqMHGdP9LW--HbvaawwXwRWHT9V8gEPkfQK8zl7LAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=h9zustLE1RR_wJ8EsOHKwf0Eq2dH8OsWnkaRa0MiPQ3n2ow0F1EReCkEb4_uS2itELxj1boHTzjejF-nTZNvwYTXV_plGVf9Wgb_-UM18lE2SwCw22017WnN5hwLKTYHB64QSyA77YpN6gWfsTJxad5Fqeu6Pe9uw1JmECOgZkx_donnzVD7usBpphPAABi1ovLX1d3YqWi7E3pn2LYD2KmDxO9ChaU4pLeplsuKiocHxqVDfGg9QrtCaVuZ86vU_hYT8FgwgyfvsBIoW4FiZ-x7GpSvFVv9-xa_C3uWKxR7VqMHGdP9LW--HbvaawwXwRWHT9V8gEPkfQK8zl7LAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔹
فدراسیون فوتبال و سازمان لیگ بزودی خبر به تعویق افتادن لیگ برتر تا اوایل مهر ماه رو منتشر خواهند کرد؛ با این‌ شرایط موندن بازیکنان و مربیان خارجی در ایران سخت و سخت تر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25667" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25665">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfugoIbsbMo4pq081ZSxLCYSQsf12SZQiervVSMMTXXxqptruOFz9IJ-5frUMTib2cD1vnY5IUN9WwJls5bJCuYobkvJEdA6zekRndAaiW8g1uagjo9-BtrzA9dSPdKahx9ibgOcPsJryaak49yipz1nL8BTY8yW5NdbyT-JJ5pTLskp4dez3xd1JHwJkwrX7L5QlGVTIl2KnXTJEZFY2PuVRtZ9Vg1mtRale_Sla180yqdTb2pPaSp2e6sJYXPKnzW8_6KsvTWlKgg-r5HRqmYcLEX4SIwY37zC5R0BbdtDtJqAV8PsSrHWLM-H5vYmg8-vLfaTGNxm2nxP9iQR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=drmlS5H_oE6ov8QN4CxouvVS6FhE2EdEnp0CYj8MSNlJqMNEte299hpMblrJbednRrIFjp0E397GfdboZMsGTAK26LSN_-OkhRgaFl_QbkxYEzNzRj1B2kK9ufgCsuuG6IkfeDlqO8TpGz1XxEfxB9rXA1rm-PvFmzhStT41sQFlkj0qE4pVoy34reCmt7v7vnFxhP4qmHFuOckXtZYh4qLTBIWtKgQbU4TR6Doo5csZw75Qcu4G_5OkyZFUFpQwwFXg80vshiTVCThEhCczy06cSvS0PYE-JlkDFGVzMFlhEZw6CC9_M2qVHVLhUVeOevM4sTal-qx9fgIAMXTzrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=drmlS5H_oE6ov8QN4CxouvVS6FhE2EdEnp0CYj8MSNlJqMNEte299hpMblrJbednRrIFjp0E397GfdboZMsGTAK26LSN_-OkhRgaFl_QbkxYEzNzRj1B2kK9ufgCsuuG6IkfeDlqO8TpGz1XxEfxB9rXA1rm-PvFmzhStT41sQFlkj0qE4pVoy34reCmt7v7vnFxhP4qmHFuOckXtZYh4qLTBIWtKgQbU4TR6Doo5csZw75Qcu4G_5OkyZFUFpQwwFXg80vshiTVCThEhCczy06cSvS0PYE-JlkDFGVzMFlhEZw6CC9_M2qVHVLhUVeOevM4sTal-qx9fgIAMXTzrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25665" target="_blank">📅 12:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25664">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URFy2dV9_j9mGqY5ibJ3XdEsjKET4QYN8_S1-x2Hr2utCNW5_9J4NDvjOkh5IHsw_MaNuB-qoEmzZVg6hGZEenaX6OcIUigQtIhgFkCytL-j0XZ5sIPhkn20hQ9aoIGIfPuR-Pj0e-QhK31r7zvgqHRTD0bMeC6z5mE4sJer4RGO6b-V9ELMBfX1BMobJJv1wfaMgl1hJP2jvwBDJYiINSUdPyCRZ-eKpZja6Ntk6OjDV34nljJGDzXO0TOj1o29HMG9SRBMwfwBIWjhvRIB0z7Bojh3hnLr2wzY7MChMYzO-uCbxBy2CL9TGnX-ZIFzAeielVxZofaZJcC0mxTSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25664" target="_blank">📅 12:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25663">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=HzSQ8szYbF4l6hN9lLUCAWdFv826Fctegxs2RdYa1ug0qDIDfB1Qu3Qupsge9VyE7m1SfW7KIaBvpDOLkn16z2VoT2QPqRpdtt7YwxSVGCMnu47NYdq_hSuUvcNz1Toy3C169CLg6fruQot6vMsNq0F-zw8Ln34siPUY2E1V5WAEQY0Z7i7lPOxAE0aoC75VdXCg8hFmsj0t0w5pecr1_7db9hN1zHkOlJ8l3jO0GOyWGHv14nJ7SAVXmtnQkFFYS20zF2svui0j4WBhIGMyIiRTt7wWcpc_dd08wuoSf86ZelJcWkprwsI9ctJJkHOGYBue0VOkZSn1sDY-cmVBQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=HzSQ8szYbF4l6hN9lLUCAWdFv826Fctegxs2RdYa1ug0qDIDfB1Qu3Qupsge9VyE7m1SfW7KIaBvpDOLkn16z2VoT2QPqRpdtt7YwxSVGCMnu47NYdq_hSuUvcNz1Toy3C169CLg6fruQot6vMsNq0F-zw8Ln34siPUY2E1V5WAEQY0Z7i7lPOxAE0aoC75VdXCg8hFmsj0t0w5pecr1_7db9hN1zHkOlJ8l3jO0GOyWGHv14nJ7SAVXmtnQkFFYS20zF2svui0j4WBhIGMyIiRTt7wWcpc_dd08wuoSf86ZelJcWkprwsI9ctJJkHOGYBue0VOkZSn1sDY-cmVBQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25663" target="_blank">📅 12:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25662">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjqczQ2hFjEwU5rLhHLeod6FfwNprPgAUu5TNpMlUXzVIyBdndff2ot7tzD41lt39MDjJj5-F_rvhaaJCiUwgAnkb6Mn7S9acozqR6ZwvfEDXu7CRZJhk1XFuplFBN8m8TPG4ZhiEHXM2YpIFa_UvqhaxG9E6hdf3kTJ08P0a8qw5Wem_V44V_SgQsmzqP3l9YiPKKYvwfl7m0W0Sil817JBd2V93FadZEr51nMjv5wR7LSy6C1d99drDB-tvpily2Eyp936ZPk3Jy9pBW4nabAHvM6yo4sVWZ0jpNnWLDcP89miJVSeRNJnlrUM0YIUzmgKSqHrx3XiCifq4wNfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25662" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25661">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thff6Fel2Bxpk8tIkoFktChDg3wjNunqBgKR367EZ7vtDFPmfvgfaqYY5RDjLToLfNE879mEFZGVz_i8Pj0AYZZF6KjpSnc-5NDGbNgdPPCY4L2sZ80SXx6Kw1EM1LvRhmxZNqVzaQFMU9MNjM7RhqydjaZEkvbPMpoBj8n07qdo4S2kbK_nfPBHEBlTYAoJFhG4yHtwr97_eH7kZkZlpmxoypurQNgQmGLA4UYdTro9WmLD5zQKCr_AtSXTTUO7W-0HakcpLjFYqHyrnk7Q35-7UsnZymbAx8P4sp3Gtx6aiW0wHVz4HWhvxqFfHjbj1eWNJ02CL8h1L5Y7fr2m3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین تصویر از حضور یاغی جدید فوتبال ایران درتیم‌جدید؛ سیدابوالفضل جلالی بعد از پنج فصل با لباس آبی امروز با لباس قرمز پرسپولیس دیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25661" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25659">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcwOCiV0Iay2BsuD-MEtFD2R1nXrsxriAPrpxvVTSKxQbgdKj8-3BMs0SLNZjJzGeS22FbnfQU-ljWVtBs0pTVo-FEERq03druKbj1aZCsXDza5Hz5Y564R-HPdD6GmH4qebjGeUE63quA2vG9UGFbcLmmHfYPB2ULb-ov6yY7pBHOtWOuCJoCAKphmt9h5Zd_lDR9Z9R3s7sORUMsOpHTVeZeokXkGY9uUwVqHCBPNJNoflaaX6afFMO0y9mC47EQ09jKW2iJXSI0lT3CsGAtzSBtYEKC2vUZab4uLx4bm1cPDs-SV-PabizoYR7s9K4fG3beyHMBVNR7D86N8ekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی:
ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف میدم و روی نیمکت تیم ملی دربازی هفته اول جام جهانی مقابل نیوزیلند نمشینم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25659" target="_blank">📅 11:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25658">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKY87OkvvJkWdtJFwZ-a_QhEOAFWuxBrVb5in188nSLqa5hNnnmsCAoOQm3SSLLY4zABcM3D2n5BrN--RgeRSvzDW70vHwipS-ZJrZ5DJA2arP4bsS0xgK7-baGte8Ie1DlBUYRmI4zoi9oz5ltIPTeZPL_U9zXgcwADYy7FKS6-RC3CaMyVtjO850BuniDBJSvDy1-rMJKdXH9jolw8umJDqSVP9AwgRfk9SQAKNZ4V0b8-caNRoOLYF-gOyRubBGqnwjqZKSpZ5CsKSBucdDNag2hYJAC5rID-BhhLHblxIwXil90qXbNrmBY_etRZfZYx_BJBpVOevHU4fatsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
5 داور نامزد اصلی قضاوت مسابقه فینال رقابت های جام جهانی؛ علیرضا فغانی در رتبه سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25658" target="_blank">📅 11:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25657">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=LLd5JCTkEuEwK_2X0q2ohFrYaxOc57cnNijq1-KCY5qM455Lz1121QKLfPjxfYWhTzLxd7t9HSmte4UIvScazpa301kiw0t81oqhWj64dYXhM2EORwUDIeb7MjLucn_iqcSVEOFp-9xY9ePETlsuERz0zVHyekLJNWhF_gsA5svjB3X9VtVTsBoIcOkfEEu7d-2FdcpbRqVlVVu3Y0IzUMx-XVKOP_WitjApeTc0tpw1-z78sMvHDIPQqQVOmcP7l8IcyZ2fRQksV6iGynRsnJ5LayzrD2Qu-Dx6e8lzMJOer8lyMhKz4jiDSw38inPeer4eB6nrdvxaGWMdFD6moQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=LLd5JCTkEuEwK_2X0q2ohFrYaxOc57cnNijq1-KCY5qM455Lz1121QKLfPjxfYWhTzLxd7t9HSmte4UIvScazpa301kiw0t81oqhWj64dYXhM2EORwUDIeb7MjLucn_iqcSVEOFp-9xY9ePETlsuERz0zVHyekLJNWhF_gsA5svjB3X9VtVTsBoIcOkfEEu7d-2FdcpbRqVlVVu3Y0IzUMx-XVKOP_WitjApeTc0tpw1-z78sMvHDIPQqQVOmcP7l8IcyZ2fRQksV6iGynRsnJ5LayzrD2Qu-Dx6e8lzMJOer8lyMhKz4jiDSw38inPeer4eB6nrdvxaGWMdFD6moQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25657" target="_blank">📅 11:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25656">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=TkH12maaxsESPIB4J2zGr3rgYDpYwvnbbtATCdUDd4FItdgL8s7GJ7Tifs_ICZbgoiWaB-N0o9PGE8teR4gjx5kKOfUKXQpSbTarVyhAhNlnfjWnT3-nN0QDAVm4B-vKQGReL1e3nPZ2ecrderuD7GSLkRUHZqlH2oag6keTaFSXbKgn-KlqaZ8AB3xUUOfvZLSdKQJzTNnly-utYfmL_vo6Mi2BjkYY8QR7_Eavo860Zk_s7piOtlQ2Ax9pGv1fzM86P-IdMb05lfBWyonTawYuu-IhDb9SLQMb3x1iiub7spZUFKM1xQxS8E-Bgn0TKe8b4f9e2OCEMN-MrWfTCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=TkH12maaxsESPIB4J2zGr3rgYDpYwvnbbtATCdUDd4FItdgL8s7GJ7Tifs_ICZbgoiWaB-N0o9PGE8teR4gjx5kKOfUKXQpSbTarVyhAhNlnfjWnT3-nN0QDAVm4B-vKQGReL1e3nPZ2ecrderuD7GSLkRUHZqlH2oag6keTaFSXbKgn-KlqaZ8AB3xUUOfvZLSdKQJzTNnly-utYfmL_vo6Mi2BjkYY8QR7_Eavo860Zk_s7piOtlQ2Ax9pGv1fzM86P-IdMb05lfBWyonTawYuu-IhDb9SLQMb3x1iiub7spZUFKM1xQxS8E-Bgn0TKe8b4f9e2OCEMN-MrWfTCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسری طاهری مهاجم جدید نساجی:
من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25656" target="_blank">📅 10:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25655">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OylnSll1Zio04qumMO2xUQ3qnnmS0VFX1a78kKGXtAsBxSmqGEbAnzU7qj3oT-UxM0gYuyoNDqult2idAYKr4tqM51AhuBjffj_zkesGjsBe_SN_svDGIDZU4DQ5Nwekuz0moAbaBIMzYjTrHqfWTl0vICJZu2dCnWiatRpI3xMOv_-DyLET7Aup2DX7V90WfiTH994XU63IR_zzwQYgD3qIIdcc3eaFo71_iJGysBqVbC_SWbnh8Wl0_yRuBsiDaaegqZEHvF_QdQkaXoTmxTwBUW0c90P_hIhBTe3Cdxm5JSczdtWOVHVDz2gzKLLw3UkvZOAbxSZK0_jCFHFwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25655" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25654">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=CmxMzGg8Z9n7MeRJ_zkMB4Pf5kfsI0ttrwCDCAu4ZYm3nqUpjDCFfQ6TW5CVFUDbl7Elnr9S30w111zH7Ac0ZVzGkFV8hke0h_OzK9bgiLB-WLXON88nfCD7tgnGHwOsr9JZU88DnRZjtY6vNXmP2ASRoGTyr5ieQCZ-0_FCnvIm9OLjtCS40f_dyf_h9tmFyaxyGN_OuS7r6rrG_Vu5OltF2bJB2rLKMK01kkqjLRALc9_qoEMToYdYSIZIiJgEdrkP5lzqMXjGMw62XuvMkzYitKUdSxVj_7P8JV5tFvvrz32gTUdyQZNWZ5kBkS-xgi7m1IJJS1pXmOLwlrpOqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=CmxMzGg8Z9n7MeRJ_zkMB4Pf5kfsI0ttrwCDCAu4ZYm3nqUpjDCFfQ6TW5CVFUDbl7Elnr9S30w111zH7Ac0ZVzGkFV8hke0h_OzK9bgiLB-WLXON88nfCD7tgnGHwOsr9JZU88DnRZjtY6vNXmP2ASRoGTyr5ieQCZ-0_FCnvIm9OLjtCS40f_dyf_h9tmFyaxyGN_OuS7r6rrG_Vu5OltF2bJB2rLKMK01kkqjLRALc9_qoEMToYdYSIZIiJgEdrkP5lzqMXjGMw62XuvMkzYitKUdSxVj_7P8JV5tFvvrz32gTUdyQZNWZ5kBkS-xgi7m1IJJS1pXmOLwlrpOqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ایسان اسلامی درخصوص درگیری شدید دوشب‌پیش جوادخیابانی
🆚
خداداد عزیزی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25654" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25653">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=TS-bGC3qsO0zTeRGfUZmm_3Kqwz0Hl0QZdHyZjDibeWYUVi2Fd56atIOjZP06MJ01IGmXkrCptPWfBl5szsO8_fhtea9WzxLz8uw-akcKQDRO1ZDu_SzbZRLkHbn6CR8EGDokig5ZbT7_qnpqZlikRD2-aNUOb_vFx53cOunCvRrK0BPTLfUWa52BiLX11UYGs_MjlxqIs-OT16VAuRo9zaB82RCMi4a4A_dyDhd8y0lR2KhNDLYpf3EkF1rg8pysrOIfb-EPCSKcehNmPXuoKbO7_OcO0355Tn73Ms7t6BJ8AVjknwJ97X-K0o-c-iM4TvZjZYHNF74rfGRSb-dGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=TS-bGC3qsO0zTeRGfUZmm_3Kqwz0Hl0QZdHyZjDibeWYUVi2Fd56atIOjZP06MJ01IGmXkrCptPWfBl5szsO8_fhtea9WzxLz8uw-akcKQDRO1ZDu_SzbZRLkHbn6CR8EGDokig5ZbT7_qnpqZlikRD2-aNUOb_vFx53cOunCvRrK0BPTLfUWa52BiLX11UYGs_MjlxqIs-OT16VAuRo9zaB82RCMi4a4A_dyDhd8y0lR2KhNDLYpf3EkF1rg8pysrOIfb-EPCSKcehNmPXuoKbO7_OcO0355Tn73Ms7t6BJ8AVjknwJ97X-K0o-c-iM4TvZjZYHNF74rfGRSb-dGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند: توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25653" target="_blank">📅 09:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25652">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=LMmLVHYwTjFfCRVSx0BGe82946OvTa3sOiG7vjvDoh3E1ZGVTe_3EzWBxR54AKOH-XAb7Ms6iGZ8Jd0k5DCTsIqDSlCE68A8_5SbtR1aIxEXYvBVfjMoFrZ5evjvuDrlhBJevqfh-8QFfRgwnnXdiGesjUgJ1I2rXxfBRmjNAan8v5mJQ4V4v_O-u0dOS3YsIpZmQVik-AsuFWCL4b-C-aYoFH2n_I0htSQDsHm3NEXkjgcQReoq7U3yEz9MRpYadCy2uX4gSWmAwfsitLcSoYndz-V0eFkuqRMOtdCGnjuys_dmNOPukJegybag0uQYzQ93q65mVrHj1x2W3rpcNDti0c1X-m4S-PvUuwqqj3xa_4wqao-LeBJgBjQbZZqIvjpDn8QSUNhksDie0269enwB3xTVAcQ-pL4Ge3htPgnUlr9E-hx07-APCwUUJ38YDYrEkocmMGq93KMFsDWHWRcf7OEU1b4_eMyf3SSHS0SZBlA9AhR7dffzcWckpnHYyp9PB-FvcbBY4z9QROBCfJNM7UOw6Ma-0lbLQw4FHLAc9ZitXlT8PUArRI-AXya3rFlK9dZWOEZeo8QnttLw5bgtqFVQa30JtHNoQ1Np5Dog25PYtKYqC5vqDeAdy1dVzzzejB6oH66ic9rEFSJ5yzjNXmUZAb9LDu7h4a3IJ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=LMmLVHYwTjFfCRVSx0BGe82946OvTa3sOiG7vjvDoh3E1ZGVTe_3EzWBxR54AKOH-XAb7Ms6iGZ8Jd0k5DCTsIqDSlCE68A8_5SbtR1aIxEXYvBVfjMoFrZ5evjvuDrlhBJevqfh-8QFfRgwnnXdiGesjUgJ1I2rXxfBRmjNAan8v5mJQ4V4v_O-u0dOS3YsIpZmQVik-AsuFWCL4b-C-aYoFH2n_I0htSQDsHm3NEXkjgcQReoq7U3yEz9MRpYadCy2uX4gSWmAwfsitLcSoYndz-V0eFkuqRMOtdCGnjuys_dmNOPukJegybag0uQYzQ93q65mVrHj1x2W3rpcNDti0c1X-m4S-PvUuwqqj3xa_4wqao-LeBJgBjQbZZqIvjpDn8QSUNhksDie0269enwB3xTVAcQ-pL4Ge3htPgnUlr9E-hx07-APCwUUJ38YDYrEkocmMGq93KMFsDWHWRcf7OEU1b4_eMyf3SSHS0SZBlA9AhR7dffzcWckpnHYyp9PB-FvcbBY4z9QROBCfJNM7UOw6Ma-0lbLQw4FHLAc9ZitXlT8PUArRI-AXya3rFlK9dZWOEZeo8QnttLw5bgtqFVQa30JtHNoQ1Np5Dog25PYtKYqC5vqDeAdy1dVzzzejB6oH66ic9rEFSJ5yzjNXmUZAb9LDu7h4a3IJ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌ بهانه بازی امشب فرانسه
🆚
اسپانیا در نیمه نهایی یادی‌کنیم‌از بازی دوتیم درجام جهانی 2006؛ فرانسه‌ای که به زحمت از گروهش بالا اومده بود به اسپانیای آماده خورد که هرسه بازی‌گروهی رو برده بود و اغلب فکر میکردن فرانسه رو هم میبره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25652" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25651">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9cNZh8-Ho7SR6tmYJZWCCQ5PREJUG2TRc531obHfByhHMatBzKu5FukuA4ji6GLTHnBJbmYnIS9NUSRHATfj6vJGEqNCIKfMlHqlKE7OGrWfEIRSrN9aXF1LeYikIpnXPHrIRbU3DHlARJSXyjR1uVyWg4FL0_k6OU0hbSr92NatBAbLUM2RE77jqm6Zub8JF-zxeYQVvRqroEjWYHHzS920CgRZQvbxFtcPmrxy5SG3KMznwEavRki1jjUPM-eTWXtzizq9aTfS9nCqHmQ5mGGQc9RRMAzUZS9kFPnnnTH8muw1fxDIKYV7ORzWfq9n5a0Hvqh-TVJp_HPUGjSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25651" target="_blank">📅 09:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25648">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=ULxb71JDSZb1AEbQadLJMLYHCR2RHFqKMwFt-TpdsjGqftOIqYnrhQQX4qvPgGkV6SRRS4Wk7PBrm2dA8HqGKfbBswRZ0cTf9k2Qa372hmtapO-_gwqsusNuaQVo0kPUR3GPVxxyf-VrxWEdIlMJ5QlVbyzEtfU6zSvgGLm-3Yxw83SRDI1C4OKlqiN2BOWIVsHXKrAhYfeANhoqnohMXRyVZGWsSYRBQP245HgQ664Q4ajGzheC3xZWlvuLGfWf4gOmxny6d9l1GbQncoCoZE6UDgn9_73aQG3Ypb1fLSLi4-jWkVvWPySSwPfRsFSI0s89njm3DwCV6B4UBOiXgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=ULxb71JDSZb1AEbQadLJMLYHCR2RHFqKMwFt-TpdsjGqftOIqYnrhQQX4qvPgGkV6SRRS4Wk7PBrm2dA8HqGKfbBswRZ0cTf9k2Qa372hmtapO-_gwqsusNuaQVo0kPUR3GPVxxyf-VrxWEdIlMJ5QlVbyzEtfU6zSvgGLm-3Yxw83SRDI1C4OKlqiN2BOWIVsHXKrAhYfeANhoqnohMXRyVZGWsSYRBQP245HgQ664Q4ajGzheC3xZWlvuLGfWf4gOmxny6d9l1GbQncoCoZE6UDgn9_73aQG3Ypb1fLSLi4-jWkVvWPySSwPfRsFSI0s89njm3DwCV6B4UBOiXgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
افتادن شال یکی از مهمون‌های امشب ویژه برنامه عادل فردوسی پور؛
تعجب عادل عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25648" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25647">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlyp7QnlZ-DM6220aLNe3r2M49NyU_QifVckbIgBDR6cFdExiqAo6gqS7QJvt1HYxSakQ1SX6igojlyl-heg5oSnizLC8omXbxzr58CJjx1gRLXMICIFuyDQ-xqd5WxDEKcX-Exx4yqxqve6hPLxnK4_yxNl9KvEDrYY6tt7AVK0sMGMAHebRsRwcrMrZSHSrIUZTQuaPbwpwh7WIgRQMVL8q8m-vXt_nyVJy-no8GheOLL-Is2CSpFnCYHPlEkMLoY39ooR-CDtfubU-CrjdE8Mc8PEBi5ge5nzzA3EBs8CKYSq2SBA-Z1M_5u0KXGm4B8-5XhQyW6SI0jMFVTOeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی:
تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25647" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25646">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U98Ut2NyL3zWMm6CwRhKecP_XPbYAagN1B-wOUcZfcmCykXZG8vjP5khGSS8tf_RV7lBNai0tuqVlSIW57ao8bbl-U6zBOwsG_rkFnSXbudbAgcwLUQg_VtXIoUrl7ieKo2NnpWbuT-MWYWhojcsz8k1V5PvZWOMmw4vllyDauPGpe6Ky8M85lY30CuGovb3bMlqul1wTWDfU9sijHvaLM-UsC_aNy5Y9C0Zjz0pziDKShF70rFemQjZvXp1G5VJmDFJLQJ3QAJ4Teao4d0R4SqGJqn_OLRgtHSZc-OkeXeQ6eCot8moKaxJpG0QjyHnbq8TORKJ-TjqM0eGdwBlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
نبرد فوق‌العاده حساس دو تیم فرانسه و اسپانیا در نیمه‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25646" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25645">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=pAOuclXc7VqvjvzDptGyDa81Ceu5UvgRFHkhRigUZ8uEviIqlTV9a5RVfQDq5IhQOX_UQlvpf77cQp7fVyWBPRqVK3L18RPLc6j8NzGd0sgPGr4ncjYljkYZTgQgbwpPke0Uf_d1uGmVJYR2TnTsI9B0b6EyyT3NN4cqNeDS-c3GAVhNsK3l5LGypLPf8Ei-3gXBDFuVk8BhLJ5A3orAu8j4xJlrbiyubgzqemh0rd_V-NpEUtWaVl4uSP3YysJWy6EOfVn6dHJCV9yZ1zGR96g9hfKtV2QuNl2K1_4TXJ5rw0R8qFXKRJwzYkJvZeZIknFp-VPBspPXgfRvxHjdfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=pAOuclXc7VqvjvzDptGyDa81Ceu5UvgRFHkhRigUZ8uEviIqlTV9a5RVfQDq5IhQOX_UQlvpf77cQp7fVyWBPRqVK3L18RPLc6j8NzGd0sgPGr4ncjYljkYZTgQgbwpPke0Uf_d1uGmVJYR2TnTsI9B0b6EyyT3NN4cqNeDS-c3GAVhNsK3l5LGypLPf8Ei-3gXBDFuVk8BhLJ5A3orAu8j4xJlrbiyubgzqemh0rd_V-NpEUtWaVl4uSP3YysJWy6EOfVn6dHJCV9yZ1zGR96g9hfKtV2QuNl2K1_4TXJ5rw0R8qFXKRJwzYkJvZeZIknFp-VPBspPXgfRvxHjdfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25645" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25643">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZUb9zJGgXOLUJriy4iUeTkgXJ4QfxxtfD7NGpMMqLWNDzBx2QosNRO_p03cpLyblD59Ukyw-RBn6EAdMzy890KJFhhxGBJJrRgbqYs6zbpBDLHXfkuh4J02g4Jawso0c5w1fV-2vMO9omMQW3nCTQh_1IMZbL080SkaS1gmx43aLGZaii5nyjPxkrQBg2uKVB-iroBaNPzsF-CMjlHazdedrWmIh6HjD5W-w96f1TyQOalka3RaGDjcxRutXWdswFpFIwxD9oMvYKB4Q5vUeH4QKm12Bcx-aQ2om-qFa1bI3xM1abYrZlMZMh266BJny3RlIiUDG6OxmLlCqYjOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
با اعلام باشگاه فنرباغچه؛ اسماعیل کارتال با عقد قرار دادی دو ساله رسما سرمربی این باشگاه شد. ارزش قرار داد دوساله کارتال پنج میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25643" target="_blank">📅 00:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25642">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=TdAwcMwyyWaYKc4I7b6r_xZomaqiBBNxi_4HLY27jNsoGU0zDpILuCKAV7_SsmSi35uQDY5remP4X2-Ssqvc9UK4ngSmkG0Aqy-cpevs3Zyo6pIdfTa16rOf-Ly-bD5KqYvDj6SHXRV3GlY0sv49_s_4N9p2VinNRbac1choWHcUR-CB6kdNzUs4UmTNRqtIhb_E11dvUOcX38AnogE6kuQ6nHPAesQYPbbmusAhMk-puHqQctAzDSjfFo_CFJy9zfXLUu-dbLLqId1LfCMr51G3kEa4XZbU7bcFdZKJFR8RzK_Y1DgxRwmpUZmzRdyolEsR90gN5CAYDka72Nj_MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=TdAwcMwyyWaYKc4I7b6r_xZomaqiBBNxi_4HLY27jNsoGU0zDpILuCKAV7_SsmSi35uQDY5remP4X2-Ssqvc9UK4ngSmkG0Aqy-cpevs3Zyo6pIdfTa16rOf-Ly-bD5KqYvDj6SHXRV3GlY0sv49_s_4N9p2VinNRbac1choWHcUR-CB6kdNzUs4UmTNRqtIhb_E11dvUOcX38AnogE6kuQ6nHPAesQYPbbmusAhMk-puHqQctAzDSjfFo_CFJy9zfXLUu-dbLLqId1LfCMr51G3kEa4XZbU7bcFdZKJFR8RzK_Y1DgxRwmpUZmzRdyolEsR90gN5CAYDka72Nj_MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25642" target="_blank">📅 00:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25641">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=F7WMF42KCbpAxeiAC4PWSvM0BdFPrsH6VPNOMWQX08mEPNfPgw_4tyS4s22G4Gu1NOc5G83KXo-fANpMZ5X4Pp_9q95XWzmMttR_6jyEwVviOjZZWNYPeN2Z3C5iO38qx7FHmHJec09zB7xRjtMBoOqgLCdqeMd86ofH_Mq2Thcvfll8RtFeTFDezhhbKIFQCIcnQf9wkwlzB0yuZF4ARNUf6O2YX1Qic3WlqMGlHtDzcu5_FD-NGzsok8VcqSMWin4g61DfgpATDlFEq0d-foXDfsb0V2kg3_SCB7Bkp_s4LMv4WxXFHzo5AGI0SwNqPpeTp_nuhGNPdG8xl9qEpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=F7WMF42KCbpAxeiAC4PWSvM0BdFPrsH6VPNOMWQX08mEPNfPgw_4tyS4s22G4Gu1NOc5G83KXo-fANpMZ5X4Pp_9q95XWzmMttR_6jyEwVviOjZZWNYPeN2Z3C5iO38qx7FHmHJec09zB7xRjtMBoOqgLCdqeMd86ofH_Mq2Thcvfll8RtFeTFDezhhbKIFQCIcnQf9wkwlzB0yuZF4ARNUf6O2YX1Qic3WlqMGlHtDzcu5_FD-NGzsok8VcqSMWin4g61DfgpATDlFEq0d-foXDfsb0V2kg3_SCB7Bkp_s4LMv4WxXFHzo5AGI0SwNqPpeTp_nuhGNPdG8xl9qEpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
فیروز کریمی درباره‌انتخاب دومادش بعنوان سرمربی تیم پرسپولیس: انتخاب خیلی خوبی بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25641" target="_blank">📅 00:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25640">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-g1P5_rbGE-IignzlkknBCbvY2B9BA68Rn9eShAE9cTHZ2Y1GHPStqRSxIz0u4-3WAC1WG3yIVWO9MPDkqYcg9Ze8woNfjYtJOyU5CYzDVTN6HrEUYEMXpjKZhmb1fuEO53JJ4EmpJYUI33DTOmEKUZn-pZ9PzvxAkDZRQbHunLIZ2m4ViN_CjTJYX20uNmtbuO8YYzCrX8YoqOzxtr_2Z72hH8NwUo99IVMt2BdkZu5R_JXbqn7l_Cwu29h4jmVHmdeMFywpOXJjO0ccXkU24RNdRMRBb4hX9CW6mEuPQMr74L9DX_F0a_rtEoa9Q3NdiqXqBErBZhnljERur4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
رامین‌رضاییان ستاره‌استقلال درسفر خود به فرانسه‌کیفی‌از برندمشهورHermes به همراه داشت که مدل‌آن Birkin 40 است و قیمتی حدود 21000 دلار دارد؛ معادل 3 میلیارد و 800 میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25640" target="_blank">📅 00:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25639">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnU6Rv4oM2vLuFkQvzuZBdFZrDpQVQ2CXuAKXunWe4REqmSxXKR5KItmBO3flvjB_qa-ASihGK7-wR6gigP4ut4b8mRKF877rDaN4Zy8H9uZu-kX40ZcGYmCYiU8B7KLkIdN3HOhUy4ycJe4yodHyQI74F6Zt5-4sNSRnKLY_xX2-K-DDc3V-ovqZQGLVLroo7YxMzQzUuC_Vjrmn0G7rXxZDAc-yLril-30eYSJhYPTQytYeu0PxC0R_CezGvgYRmfIGMh_6xksN7BsBoWgdK5LDLIDrwEH37sSRyIQrI9ZbvnNsAC65yeRKrXbY6YAuHs_oqw0ixJIgtGuxOrBfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس باارسال ایمیلی به‌باشگاه‌‌الاهلی‌خواستارجذب رضا غندی پور مهاجم 20 ساله این تیم شد. اماراتی‌ها پیش‌تر مبلغ رضایت نامه غندی پور رو 2 میلیون دلار اعلام کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25639" target="_blank">📅 00:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25638">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwaYKvm5ETecedpAls7JctjksrxgsahYjcc9b1Kmmb4CZjclXIgiKudRld1xtWNrvs_Nhl4IYi8AeiVhAOsEnPqIygzjT5DX74h0be8xfpq6TSeowpUMutduCbGXTG-qdnMO79gTWnrQkmv3avkgGPZCd8TddsZ3ZBemHNdJQo_sBGvgjbEuJDKcqBKKuL9Bm0zGmZ5CpJdESBSwsT65OgtphYEjaRFOG5p8VYzAwFCfkAAtKCaFdkIyvwGAPTNKx5fOyQiU4qt1fNwBBd2u6js_UikEnkThNI8Pb03pwhZeTJrNrjRpG6u-EPKbRxaKOEXbc1DEwfeRlD9CqUKBhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
این صحبت‌های مدیرعامل تیم نساجی نشان میدهد درصورتی که باشگاه استقلال در جذب جواد حسین نژاد عزمش روجذب‌کنه با مبلغ زیر 3 میلیون دلارم میشه این بازیکن رو خرید. فقط مذاکرات باید حرفه‌‌ای‌باشه و بی‌تعلل مثل آقای زندی‌. گفتنی است باشگاه استقلال برای جذب حسین…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25638" target="_blank">📅 23:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25637">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=Ei4qEH_XFgwIn4EFzpAq3Nbmmw19ixWaP2DLcEFsYPa8Q_cE1QAxID-nZr7T_mPA3QXSY_TsD4au9wDDAKTbBFBWPt8_tVbkRMoKdBEYkJ4CR_CUUVlZXhkMvR1eZQ2Kv2wNr2ZWR-rnHTK7xXCA530k8FDLS3slXpgSdlqpQVvllHG-vFOY9JHRV4597DIqSwsMJwBFL3mXtmGeP7Z4QDD-UhdEQ_cVsJTEw61d-qAax8K_7dOYHwLNvNhUC3kJeIpR5apBuMV8cl8uWTZU17qRs3jWo0UPXK_mXtVRwsMaOpkiqLRf9pbrtBNh3YjrvuWGGHhsEq7qoj6U4DHkkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=Ei4qEH_XFgwIn4EFzpAq3Nbmmw19ixWaP2DLcEFsYPa8Q_cE1QAxID-nZr7T_mPA3QXSY_TsD4au9wDDAKTbBFBWPt8_tVbkRMoKdBEYkJ4CR_CUUVlZXhkMvR1eZQ2Kv2wNr2ZWR-rnHTK7xXCA530k8FDLS3slXpgSdlqpQVvllHG-vFOY9JHRV4597DIqSwsMJwBFL3mXtmGeP7Z4QDD-UhdEQ_cVsJTEw61d-qAax8K_7dOYHwLNvNhUC3kJeIpR5apBuMV8cl8uWTZU17qRs3jWo0UPXK_mXtVRwsMaOpkiqLRf9pbrtBNh3YjrvuWGGHhsEq7qoj6U4DHkkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند:
توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25637" target="_blank">📅 23:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25636">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=PO06sAmaxJ6ti9pWQuJG1BfzZ6p3NZj5fCJyxoA1i9wdinUqcdCUSJQ1bRAcUJBhropUTaINVkxh6-EeV-erRH0tgEyTaEOCRZzTmk8cYqg9GlL_Lia4OgZL2q3FMaHG-clj-xfqoEW4Y-CI00bKwkWYKDtS_7F49RfhsfVbM0Yahr07ryJYuE-wsEQGeP9PeqIhV91zZd2jgjiggiQc_5Ui5pX9xl5NhtlWOJqrYkqGkDo_OwYxEf8hB9Jz719EI1P6OM8ZTq2VTO6A3ZwotGKcdxBw9dLdHOOTDnVa7fnE-01Wh8GNJl3Hc2XVuC2tYF2eAWCpWq9XK4cl5VWnow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=PO06sAmaxJ6ti9pWQuJG1BfzZ6p3NZj5fCJyxoA1i9wdinUqcdCUSJQ1bRAcUJBhropUTaINVkxh6-EeV-erRH0tgEyTaEOCRZzTmk8cYqg9GlL_Lia4OgZL2q3FMaHG-clj-xfqoEW4Y-CI00bKwkWYKDtS_7F49RfhsfVbM0Yahr07ryJYuE-wsEQGeP9PeqIhV91zZd2jgjiggiQc_5Ui5pX9xl5NhtlWOJqrYkqGkDo_OwYxEf8hB9Jz719EI1P6OM8ZTq2VTO6A3ZwotGKcdxBw9dLdHOOTDnVa7fnE-01Wh8GNJl3Hc2XVuC2tYF2eAWCpWq9XK4cl5VWnow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وسط برنامه زنده شبکه ورزش برق رفت!
رسول مجیدی مجری‌برنامه: بازماانتقادکردیم نذاشتن ای‌بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25636" target="_blank">📅 23:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25635">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBptpEfh46Ic6ZncMBpys2af5e-io0lofpgMqCyICJu6NpJa3xD5kPAXVOlRwz_r8ChcAX7Ca5v82mAG8gsFGtSqHmygaXXy9JDGAuJJQg42pTYlDcYccOrrcEciprnu0sUh7yA9EW9TTofEouySkWCqoxW8897v0g-RQH60gl68wsLOptFUn61yReiJNgbi1vTPMz75AzttRfqqeVz50m_NiaF-RfaLJA3q776gTJd1YEMqaRGJ7jxKJ5TfNZEuOJhNUbU3_mCom-0N9MIt11tqv-L-0fweFh9KDjBskwc_3cWvz5d7AOSRcpJfyscsiUHGD8-w0FUNneo1Te08zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
خوزه فلیکس دیاز: مایکل اولیسه به سران بایرن مونیخ اعلام کرده میخواد بعد از جام جهانی بلافاصله جلسه فوری باهاشون برگزار کنه تا تکلیف نهایی‌اش‌مشخص‌بشه. اولیسه میخواد که در همین تابستون از بایرن جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25635" target="_blank">📅 23:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25634">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaDyQfOB81QB-i3zcje95CaNask3ZBXXsa7TcpG8oY5pxAtR6-crpFXPpj_7h8CLbnDO5pNqqjk-QPqNnCRlxL2Blb3T0myeRpDorIOTxlM1jpxBJcC4b31DuZ3L6otvvvOJHLtqwNfue-DJqM3CJ_hg7tQaIg6Pjc-ht157j-VR-uU3qOFamUl5c0S5W2J240Ws8FnAHmkgODDATSuT_cTB1uL0R1jxboMlEz7Hz2CHOW3lMqHcA5fxaS7gxy8sywTYZIMQzt75m4BwA5q-Wetb_ycNO9uM-UBUOlGrXNL_LasVgpPGXprMpbf8kQlbapC-u6JIp_7WZwxyIGaS9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25634" target="_blank">📅 23:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25633">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJNLgeQ73BV3zmW1inAJ_pzGDkqH58fCu7vSK7DkcTF010ziG5sJpqaA6R_DghIcbcWZzoVgAlxTKgGrr2uoW5oPSt1lQpVIuM_iKhSgQ2Lo9Ps2WFfE_jk61MNxJG4KI5cPjAQMz2EcapdhaV51RDpI7QqU3tc4yMVnDncmKQZNanhATSH7zxoOmZzYeBspdsxvgqPw9nshAiHR1032QsV4z9pFcBM7LKV_EFgep72Oj3lbTFGgevgSPx8zAEa2EweA2padJnvZV4wQhtnkOoJqZUo2B4LBdGZLd1CFuEw5CQ0vPhJdh4qWYCF6bMWRNj4ko87rc7EigE_SFUN4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال ساعتی قبل بازمصاحبه‌کرد و گفت کار انتقال محمد خلیفه و بهرام گودرزی نهایی شده و باشگاه بزودی پوستر رونمایی از این دو بازیکن رو منتشر میکنه‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25633" target="_blank">📅 22:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25632">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2kTBOzwF1D5YYWNldfJ6goJo6KIhzvQY1uqmNmOK1ujrMQ7Zgoyj49Gxr1xyyqTYuFsMlCTj2QfxXolpp3wzCT5lWmfITiUYcL56KRC6v9AEEmj9rxHQXEihuf9Hyp35eYjbxrBGdOSyRWqxVjtDc03JKqMqzoiLvnsvhNkPPx5eu-cc7v-fOrCXITRHZVbLFbj7EJ1zR7jsAnm99yFKse_ixysZfgZ8FUvuuUbC1wzhDTm7uEd71FRxSjU3hW7u07OQnKekiZbre_Jcm4EV21mfZsNBnJ4b2wcIGLJUmQBV87ZkfNdt5yPnqfT616Y5JlwGZzaXNCiJnwJeNxSDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25632" target="_blank">📅 22:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25631">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=d1cmxMlvvYKaafBvZLX04kzfcpQ47zbZ2XtigXbU6aCXGgADeF3L8lWDmRAopuLCQaly_A0WCyjJzB4CF9WX_C48xJrrN2KzPp829ldFdNJvNK3lwId82Ejx5N4hgduZXTU8OQMiRyiwQwplfuzqmWlip7fPliBNUM3pv1anmPJBZxWicjgJxPkLPyU3yfVNa9rt9_bfY0E0GadIwiNJ2N13-yheXNEyJObdl8HTjb-fb9dI_NwPJgrpggpXy8Vfv0uS4RwEUSCQfgywsBS3QMdZaLdOopRHZ07LF6oigBOXipVGT4xwRE9SQzy96M7cwgdMH6Mo_rVeKan8EvpfVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=d1cmxMlvvYKaafBvZLX04kzfcpQ47zbZ2XtigXbU6aCXGgADeF3L8lWDmRAopuLCQaly_A0WCyjJzB4CF9WX_C48xJrrN2KzPp829ldFdNJvNK3lwId82Ejx5N4hgduZXTU8OQMiRyiwQwplfuzqmWlip7fPliBNUM3pv1anmPJBZxWicjgJxPkLPyU3yfVNa9rt9_bfY0E0GadIwiNJ2N13-yheXNEyJObdl8HTjb-fb9dI_NwPJgrpggpXy8Vfv0uS4RwEUSCQfgywsBS3QMdZaLdOopRHZ07LF6oigBOXipVGT4xwRE9SQzy96M7cwgdMH6Mo_rVeKan8EvpfVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم استون ویلا یوهان مانزامبی پدیده ۲۰ ساله سوییس در جام جهانی رو از نیوکاسل هایجک کرد با پرداخت ۷۰ میلیون یورو. اینجا هم مارتینز ازش میپرسه میای ویلا که میگه آره آره بزودی میام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25631" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25630">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGPGXBMtukjQhfyvGAnLdwA08X5BGtHLqkO5ZAkgnysSE5RhRaahV5BIldv2Z3aswW92ZgvSOT1yg7ceSOJ8nlqbu44Qn9bCSGf21aLLlIkzHkiYXPFXrQhKc23UiYyWAaP9ur13r6-S8YVO6fcDjXEKF1arXRuWiqwzsk0La5HG1X6ehCA-khIxrPnHbWe1DpfKRPh9rO67mXyhkeTqKEs0qMAP1bKV2KxEPwjsVBZrkE0bB2sRrsNz1Jb2ku0yZW9dSagoGKY54EYy9QPx2Se-91eEpjTow3Q4b0o1DASX6mS6LtxUc0SQ_BLBSvmXc6fQvGRxD2qONsOx44Ls7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25630" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25628">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjH_QcxmRkidq_kOCvYkC9a8HuBJRP08WSXP9DY-dSyHfxEOSNFeTP3SMy9HxmlWz4of5LQ1eVJwci_vyHWE_WRpMm5jmcb2JVRDMrhZvtxT2x_k9I3kZ0O-fVYQrEouSStTzdC5JoI0RZ1iiR1Bv2yWmHrvI5NEIrtoFoMe-AEg_lUCGKaOHYCJrK07KRYY7DOpEQIgl3Y54avJDP4rGwsHjDaGMsorErCuhOUhmCbI9lTYI7TFUfTz27LoIXVUG1k6VG2HirN6IFWmF9_oemprl1cBTZrpNBLwbhxkiI5K1v7KRYGVYHspEYZpvsULcpuEOUhrW63WuJ1qYfFOlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#نقل‌‌انتقالات
؛
کرارنماری‌وینگرسرعتی 19 ساله آکادمی فولاد با عقد قرار دادی به تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25628" target="_blank">📅 22:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25627">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYqx-SGQEOz8yrW8CyU2PmC0KzUQ4_CS4qBOy9Iiq4m4aSplx75ej5QEqhUAUmNwNTykDZGeA9oIsXQvXw6dUjQ-5mvHTxcKm3CPNZ4ACBqsPTYGypfIhx7-g0rup_gv21-3IbII-MqhAYm0gR4FSIN6y-JaZ0ou9uSAffL8fyhscVZFG_WTqjtOZ_gW3nrlGFHM-QhX14VZnTaInLHwqK5qrHM-DnGHyq-V9IY_TIigFfcX1QeK2z-WZ_iDHesR_gBnaVcu4c767ddYRx9ANIGt2PY6R4ragQDzFp7wzelTWxK_mz9bi-YLwqabEojkS_QZZAxQinUeiLYMVQGZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌فوری‌نیویورک‌تایمز: ترامپ رسماً به کنگره اطلاع داد که جنگ با ایران از سر گرفته خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25627" target="_blank">📅 21:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25626">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGDjo0gVePIIayG8PrB1roHV4CwNQ_R9SkUrvh_of7-jp2KvYnGIJZi-Ln6-iyR-adbc5RebO2Pr02pUdb3wGQ1ZtC3mPrpE3ztCfjIMa2tM7gASbD-07q0VhxHl8wj8yOTFQyClAxJii9U48-LFpoDTrpop-gtp1WYKOvnc7xrQB5uMMY32G2NZyV9aSXbuEtH8FblbuUh1RFbCgXQnmhLoj9PGkkl0q_ifkCrBvBgtUjCzBbEHaW_GHf4zekFdkArPAWPvzQBTJOb-YcPOOvSmY3h2P4Yibd8Y0NCG-6jUaK0rPiw-FatKI87DgU8QpkWjs_8BSUS2b1dz434mkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25626" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25624">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_XTjQnBtwYTP15z8O71NwvC_19wB0YRe8Ql-lxukF9wIIApMAUqjPM9aadkA6x-ozhXXmfzjClG2H4KVEe0SrTcag3qMxso_REmJin5MHSfGZzzqVxa42-KU6de6xLUX1oJXb4xy2EwY_-UJJmZ_MoOXs5-InPgW12VngJrJu6UHQgR6AkHD1D-a537L0A9gGeuf71kP-r4INurkcJpwcFNJnW6TWd_-nFDT_hCz6O7aPHC0g_diLMa6tVDmpEDE7rRycXQTjU1TItlRTjXDXqmwU1z7FTynlTGE_0lu5OPqHBc4pZ-2DtoaPn8glm-9RKYjn5WIIlIUbBQSTptOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yw8rAf6SikvEDVehnnK7gG_JBQY_hpUg0390nP_r6XoX-048DjM51hMDfDzcWH6WzfpPnr9APm6OVq2bHAKX3BLSK8Taz34XlF2-SZC-LexRUM5PirFQqLaZvwb2ms6LXEWgT1DWTAb5pMG7OCoHlQVT5Z-yEhsQR3d2J3ZGPogGNMHsMBZKwJQvN434nS-fG6ikDL82AeAN4GGeJG6qfi2nUqNBYr9CrD44_Lgmmn0RhtH3G1tO3r0wbnJMmpVo714YKmDSvh4btGo0C-bFJPaNdRyqW3a60_oaaraGdngJACXOULknS_lmYA8Bq6hLYbopNdeoX3Jc0h9CYyWaKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25624" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25623">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MurXmgrdmwSqUaJnka6X2krnYPDAEwqalvn6yd2p3M2VgsgtQpIxXA-83KhLbwaJO-xiRjocU1UEK4BnkZvjgT3gvlc_yweK6YVkbdBdc3N-vjk2GB2WB1qAJkJjA4mXurIDSxfPKbvJu8Z8Ey_N8-4bbKFoltQgveYSnl9To-N5HrjNJL6iCdXcMZ68Qnb-HpXblLZdFdfQCbXZSKWSSDubDLRB1xMLyYqr0_e_o43MpdQnzZz13OZjnWb-qH4zURXi4J2WIoLaPNiIgkVnInWK-Cr6j_mD3dShjhxED-aCqum4Bw2dnUacA5lqAXoyN3hw2IlDSaFlTHOSwEJK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/25623" target="_blank">📅 21:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25622">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA6UHghbR9lMfuXJQYhtLU2ixsYaay5tQl2zjgWzWxz9GreEl2mfOF4d9Br42Msqttk7EZNYybwuzyIybVEfiOURVbXAt2hHm9-FVz6sieiseBHVuwJKDhVyqtVNbYp01OL1WUCILVh3f00msJKcHV0cJF9EK-0yvzC8qalvDhyE5SmCMM2qcm4CeXaAl7Dm_LyuWVckIJFw6eizKyno9VH8A5Q9cS9-mcka6sOwTfdli-CVC08NBQ4VqEqJzoBsX4ZQ-XWIKJNvIVu2oSjSXfTjeOhS_1yvja45Th7kqxVKZlumkrqjlu_2il9T9aTMR7PGKQWuDl30JVoJw0oNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/25622" target="_blank">📅 20:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25621">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_KALLW4n51Z-ccibFpW_j-P52fZ-KzuVeX2td0z6nI-V9rwhnf1DxUvOU3BcxL391xbk_xBPuzfWPPXHQkyhx7Gaf3wNDEOdZe6FsK2n_TxbQJuaG8XoSJ95WntWvR8qeAyPb7X0hzOCcX18gvSF7CDwP74OCEi9wIPdaF_xOFyPBpewTlARD5oN3RrA7Vj725wwr2Wcpz56jBlBzhVcv9e2JY5vDh85hS3qsrZ686O7n64jfeVYAjbFFdEo8WtD0K-31c9vKsBbvONY6BQm9F-YdO4whPDBsDKcbmYCCIy_z-tNV3fNvRs4iqGt6FVG-bYguwWM3gfMrD5zfJxZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25621" target="_blank">📅 20:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25620">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlphhFlKQ6ByFprrygXfoJPUQIThhp7WXOsF8Eik3DeLEheANmWfykXXv61iRhGK2pJWKTD_Ek33K2JVRr_mmO2n1b6DgEp_7A4n8Q1NrlwnNBaeMsJV7RYfMp7Thw33CLznucd9Dng2AnRnY8To9vJ7e02zjc5TiiTOck5BxdcHQpBQ61DnHpPb_OY8twe-yEeV8RrfLuzXWlaL8xV2vSHvuKgR4UmT9bK2T46ILhLQ6xl_mJ9IkrjzpmB0sgAzjZBO2AP9G2_6AXQOM34A96cbh1s-5DEw55x1FSxhd3iXc2FLO6-e5FGGgiFbbXYbvHVgodfy6XSH4_RNEG5ifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
خبرگزاری CBS: علیرضا فغانی داور ایرانی الاصل قضاوت‌فینال‌جام‌جهانی2026 برعهده خواهد داشت. فیفادی بزودی این خبر رو اعلام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/25620" target="_blank">📅 20:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25619">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NL1baVp7QX323PASwncFtPNEylofomLk1sWyKcwmBfbNsr6_lLA-lmuxPy-40yhO_zkudVbXTOejtoTECgMOww30Dki60Zx-ILzdxe1PNEwuj5DyCnBJsB2fvb1HrTamQRdhpLYCrE7svGc9tJd0_krEdJLyRyA7YniZtwQnGiGaoIAmJVuS02Oe3PRHxYdSPzpMpJFHRlpX76g3LnSfWoQ4OKaFx_F_TVHeezGTtFJT5-_7hEngYEfmkPuiwaacKCmtyKkgGjf3Is0TrHlr7FnXfudZaDRrRZPi8guL7wpquQSLZUTevJDXjMk_BBoP1AKns71Rpq-ZDg-diikV2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال: باآسانی برای‌تمدید قرار داد او به مدت سه فصل دیگر مذاکرات مثبتی داشتیم و توافقات خوبی بین طرفین شکل گرفت. امروز آسانی برای دیدار با خانواده اش به ترکیه رفت و به محض بازگشت به ایران قرار دادش تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/25619" target="_blank">📅 20:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25617">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYMf16PUEYty4XHJ-HZjxOqjYnFKyRJ0WkLCUQaA4a8DdXEZsDzs8rB22iUobHRkArzpOlvlPbuMCMsilhWSFxz2vN9sLoVsCv2uhw-eYv7yeAyY-9GivKywKg5OsPFRF8VWiG2vCQe3lItOX8CoSxXJyW98m2jPHMfvEs6K2Yten1acStKXLHcWHEAfj-WZzhmq_gNPgXttFHL3UIuuJt60VfWchOneNPsoWdLpAqnnGUVbS-HUQ6PvNoimf26gc-t3gjBXpoQfDRb14jLK2jr5xpIjrkXrDw_b6Yeifsodqm-Lb-n7klWMKziGt6HfAmlSCT7RatH7H5mRULraUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/25617" target="_blank">📅 19:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25616">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-4HosryBQrPho-almjOgHMWKIJsCpI07_BelTUUnAMupsia9ifzvHfIkInV18dksui98npJ5S9dSURoj6oPM297uxyw_hEDBJ5sApWTUyaUGjR1dMn3WBHbzkwMQy8iZ1loDDKChNipJVOmtzxnCBnN49GWW_reAE-AjV1nCyGMTXxgskKSEJ0gL4EFZGRyUcxOC6bgXvj1j1P32SzwQfh6i2iGZJz3jDT_Ftos-XuAKtzwgfEyCzwGp5wSTG2_nYgG7hqyEZ1KGh4vhr8f-08n--rS_iV7b1GB9s3JJtxJXV3czgQ48tnjOOdA3gmnfO5PfK-f2YZ04PuXH2hZuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/persiana_Soccer/25616" target="_blank">📅 19:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25615">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEcqR2O5E4G9hKMT1s9zM0iiH1cNiLxKVtiNQTeohlVfsh4tSTxc6HTI6f06CpVjK9843ksh5qrB0-5uGoJtAMZEla5J_AYhS9cQSgsQyU8l2NVeA4Wtg2hiDj9K4g_-ZxdiIOID3-ctMw9p7xAfSGsiUirYCUDfCoAsGHtQWU9avSejp1NI4J_oMjvhRGL7NtUbS92LO1jGefEC5BrmJETVwuh1Uok_KDwAhly1dbdSkGHB_59C1kS628Yr3cg7PmJ2OIkHNz0VApSoogGQBYXPx1Ycgp_DUhjuu5VEeu4xwaPurvYg7mepu4NtFPsQSuqdpTv2VcrA_uUOqE3X6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/persiana_Soccer/25615" target="_blank">📅 19:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25614">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=DIXi_SN5sT0P4376oTFwcK74u5iCFnaz9iE6UOm54qL1lK_aOjMePfTtWbkDahPFmgdpZIxAhIJHoB01MgGLB_uY1GKJpGvoLK4wBtoaHudEMSADMi35Uxd5MK4_qzjBjKmrlLzk4kowluJIz9ebxnUNmYdpNy5smCY3FV-42kBaK2VbqX7HQ4vrwg3r1mQVmdru0BjqOBj7HZ6pTd9jnUukLUw_pnXHbS_nbzdbVbkMrs0HyHrBtLP9aOct2EztB_27iMlx5gxxEgQ5IkGVaUkxrEY_pKYWnwZG0w1qnBFnqPfLiYQuNVpT6bUQ0YQduV3Nxo6dNy-GE29H8sp21g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=DIXi_SN5sT0P4376oTFwcK74u5iCFnaz9iE6UOm54qL1lK_aOjMePfTtWbkDahPFmgdpZIxAhIJHoB01MgGLB_uY1GKJpGvoLK4wBtoaHudEMSADMi35Uxd5MK4_qzjBjKmrlLzk4kowluJIz9ebxnUNmYdpNy5smCY3FV-42kBaK2VbqX7HQ4vrwg3r1mQVmdru0BjqOBj7HZ6pTd9jnUukLUw_pnXHbS_nbzdbVbkMrs0HyHrBtLP9aOct2EztB_27iMlx5gxxEgQ5IkGVaUkxrEY_pKYWnwZG0w1qnBFnqPfLiYQuNVpT6bUQ0YQduV3Nxo6dNy-GE29H8sp21g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ یک سال پیش در چنین روزی؛
تیم چلسی با‌آتش‌‌بازی‌ مقابل‌ شاگردان لوئیز انریکه در تیم پاریسن‌ژرمن قهرمان جام باشگاه‌های جهان شد. دوره بعدی این رقابت‌ها احتمالا در قطر برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/persiana_Soccer/25614" target="_blank">📅 18:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25613">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=O1QUeLkHY9t6v8vQ_QO5RnpBAhc-3xhrqNb0QbbmjnRSj3fpvBLXtr7_OrhL2hRNnj-4Yx4H2OMFw2gtPEFiPm3GLyDbVqYHV-8EYI3ItUSJzI-f_CkxmmDd8lacy0JoTx6zNMB3tMbLQDbCid_qcYJ-JMGOxznF5pGq4FoAXYBA5-0CGmFpHFIdEeCGuVFbGNmRgmGMqBqPL4V3-nkQg3WhY2BfaotxGzzu_F-_UnRSvSGbeZT9zgMldXqZ0o2SNpLDUskM8Oi3LCcp6zk2Gn5ISlTxFt5GeHoR_-LBXq_0aHQTB7cmkOChZWuVJijjGSlCMrLBcmXzDjtkhT7lgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=O1QUeLkHY9t6v8vQ_QO5RnpBAhc-3xhrqNb0QbbmjnRSj3fpvBLXtr7_OrhL2hRNnj-4Yx4H2OMFw2gtPEFiPm3GLyDbVqYHV-8EYI3ItUSJzI-f_CkxmmDd8lacy0JoTx6zNMB3tMbLQDbCid_qcYJ-JMGOxznF5pGq4FoAXYBA5-0CGmFpHFIdEeCGuVFbGNmRgmGMqBqPL4V3-nkQg3WhY2BfaotxGzzu_F-_UnRSvSGbeZT9zgMldXqZ0o2SNpLDUskM8Oi3LCcp6zk2Gn5ISlTxFt5GeHoR_-LBXq_0aHQTB7cmkOChZWuVJijjGSlCMrLBcmXzDjtkhT7lgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/25613" target="_blank">📅 18:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25612">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8oOuSR89BB6vAgmidXSo3i7x4yK-aP0OqajHrC_OytpIprNvva5rFfrGGqGsskVlchWL2CmfECin6-63ShesE_Pjbd1Hx2VoCCPQmcNyzzP0x9DBXR53l65XYgbqVlK5132F8RlZSl0lzSPwXrhQyDvHSZHCcGcs6JGleNT6_K9ecdVD8YX_vVf7cKQz-35dscQf_INflkb6GAqI8Y_7jkQWORNQbRL9rNn7MYWiGANBTpQTR3ChsfEkQQRdnnTum9taLNTHTKZI4Qq8DDF8zO52Iw5kFXaWARXESKNYTI799KyHXv_HtrgoKVRNz_W8ZRtBmBg646xhM2fI_zmCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25612" target="_blank">📅 18:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25611">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSGXzIf6nVfTsgY5iA_9jNtrHc-Ao3z3pogFpkTc_RO-X-Gjby4W6ubBK2fS-kDGtJYZTPJr0pniItXJ-dRyUTs5TH2eMsrNT4nexdWGxuHjS7h26_kQsVwzXbepV7ulIvBwYVumD7ZTiGs3DvXLgTB01El_fJt3-A6avIm7okMoEx4fAL9TBHnYqRWG_WC1SqIcUKEGl4XoMuKgsAEYZD262j-XVNHc4-89JgXWEgR2y3euCAK0vO5B8HxDMI6LUqi0asK8jU9XgwyxN-bM0h_qnlZLIuP8eDDCqYOMmloxYc7SZG8icDMeInu7vwUz7Lf8NSmZ72jU3HDCqDqlXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
مهرداد محمدی وینگر سابق استقلال و تراکتور؛ باعقدقراردادی دوساله رسما به تیم فولاد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25611" target="_blank">📅 18:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25610">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ogk2ieJJkzoM2D3WcFOi7v5dX9LWSdnjuEJk7T3kPpFsiTQn9uOW71666rZR9xIHK-M4SJUvra8s8M8hRv6J2xucK77HQeJdsarBKKIxNKEZlveU_su67srNWSvSRyw9OQ4Ocu9vOrpNXPCFM-q1lNEhQ_m6hrlpSugRA7588CD_D9b0VMzptmItmKShy00GMTr-DBdUedxbj4ThWTEACp5b1HWQG8dNoxw1LTNiTUqwVBJcYpmyrSPMbmo04zPus7-jy3qAg2oLnVUSmHej1i8qe1I37EDDCJb6uVKqJc75BGePgYkWu0SM8R0IYfGUKP0S7R-J3TIf3BjDm6ME6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محمد کریمی هافبک طراح سپاهان قرارداد خود را به مدت‌یک‌فصل به ارزش 65 میلیارد تومان باطلایی‌پوشان تمدیدکرد و در این تیم موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25610" target="_blank">📅 17:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25609">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDtRBib0fM1z9wa-icJ2tf7I5Rr3hobG3LKWZsP5upBQyN-QzqkNiKQe2CzvXBqXOGtB98O8eI8ESt5JhiflQipO18qJbOh4rnLbalKnO1fwat1VnAC08JmKbjuuPgGe_mRXKoQvSXq2ULIzjNTUmLSDI7VJwGtHYzoHbGlG8fLoihHb8JjXtO-cF5Kk5UoII-8QjF7WvrZ0xL5sIcDW6IaVVPZNRlzIuZ9gh6NCbmWvn6AUBcRno_qUxgsYzYYiuFmcXYgkq0A4miV6TyAi3ktmT_Ue9pz7ihNaP-Oli8u1O1Fma_sU9mYuUC1u6a1XEs7u7_MLYdnWf7GbviLetg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25609" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25608">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHhkEW3xUScT0o2EovBcENPIzsTN1MtSvI8TldKtlMa8Mdqsz27Nqe49GODSg1scYRqoXOMnbrAKoxDV_mTgnsWcXfualafiL4JoBNXUsguY7bsiSanShx1R3ha3dw9OkEgkfA4n7XkheoNTT2xqMFNJlZuVk9iZfzaR8LzXjNUddhuuuUoO7UJq7sK0scZI5QuGNPKOyrpvCLO1bUGeHkUvuEkEhV7HNQoGMeyEKpYH0AXm5uT5dwuAJTBBVDm68YwHR8NNlfNHT5PPDsH0dlluSG-BrECmsdNk8uqXAtysC7_KByAFxx_eRb_2VsDuKDdQfmejCqIXPi_6L6iTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
خریدخوب انریکه‌برای PSG
؛ لوکاس دینیه مدافع‌ چپ آستون‌ویلا با عقد قراردادی رسما به تیم پاری سن ژرمن پیوست. آستون ویلا 10M€ گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25608" target="_blank">📅 17:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25607">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEcYUBKhzp6XZE6qk2cGKlSDIu4tPbaTloEHU7kFALtVupkP2A33ytfkr5kl5gKRBGuRf5d2UVnNpm3sro2_dZuAH1puzCks2YV7Qvo6Zae-Di0u_37xftDKM1hTR3wRHVEwMSccC-iFskxshcNStbywogejC-zhv9ScCjEXJy7WgWCaW_pQPNLJDJHrE06KehVRoEaMVEGoCvJmItJs7sGKFLFCjtHY4lnCXgpM7c7amlVmouFJYZzb5T4sEjMOQk_ZGeyp4igu9AscTDLYQ_lcvkoz_ekBtdEciypBceIZnSK4kkoy6jr5hsCAzQC9h1gFZDAxSEo2kiKvJmfLGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ 5 سال پیش در‌چنین‌روزی؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/25607" target="_blank">📅 17:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25606">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_AXQCkpbVpqKjkD8KJPhTnnTPmmi3PNJGTmR5JkpWlJWR7y9FR9l_iP2_VUvj1RQ25TXZ3idnJl0oaasSwo6vtQglBP45zju0yYGuonQJraXjEmtYgjQCxIE9MPO4dJ6fa943tLswOqEOefWRuTKfockcsgip1nZ1d7-P50yeLScLBW4yjIewF-iYj3C_mC90EHZyCnrkBpeB5p8M-Nwegnf5I6SDUoLUG5clYVHVBUrf9SKJEo-koSNGx7msPvUhhrhB3Oqcfu78KwK07jE4wWuWu5hBYHQlJl2UI6m5drBG28y40lf3UFbC3KDwmaxTbuParouQQaDo4AOc0EXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25606" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25605">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWx05e3QRTzc3MIPHEFaMDdjqZLSKcxZ1jg04hWJ__qtjpFnyubFcp3LdEyqODc0zxfolIHH1z5IOmphKm9aaGyZxQK_dfx3_l7mauIq2HhAiCHkySu__c18o3nLQQMgZ0549ku5RHid3HLnSVwFh0ivmAeAsVpd7fvTwF_2me-gp-am-WpI7Lm5yGxIqNY7Pm5rGn07wGoDQqw9PsLYX4IkTafMPlHvQgPYzXSdoR9j0i-c5XVfj29G4Wvhh2FmONEDsWN1s6PZYTdrNtXX0sr7jo1TMrgcFQzinY7XVGPO9nJqTcnbeIMOZVTWNWB9W0Gh-h7wmSZhrw0hZoFB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاقه‌ویکتوریا همسر دیویدبکام به فوتبال کاملا درتصویرمشخصه‌چقدر زیاده:)از سِر الکس فرگوسن پرسیده‌بودن‌اگه یه اسحله بادوتا تیر داشته باشی به کی شلیک میکنی؟ گفته بود آرسن ونگر و ویکتوریا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25605" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25604">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8WpLqOPjL8KWsJSYZysnC_CDyukHTcyQvu2FMfbJR9N16I_qZ57VQHEUpAF_EcfslUSyt2f0V8rS5IsuF6F4KCjJPsc7F6wi0wCvKNyX83pSAAhOe0CDuvjV98NVUBBjz4DD1caPNhefFlcJqAuOn-2uL7rbfQXqYUEUslBPdIS8ekdz2zXf5oVA80EMSZg4YvqCQe6XKuVbkYm7AcAt2uEtQ-tWtHZGpzbGO21lSbo-x5Cm6N2XuT_TUWN2XGOqMjyLhOhlYLn9lLCYADAwKcaxQZxwyWCEJ7NCv__WiFM1JWZomfx-3zMcKKaihs3CP_w11_MEMkfUxGNgWFLmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25604" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25603">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogmOVf1VDVOCvAV8BBQn3H0n87IOA6zi-ugP_Rcx8CmeGCLKSGAe4PqzBlsDD9YTfPM7BtNwnYHjZL7-z1piHhUvBqHhY6AZls5h-zMguNfPwUsR6dE5Br8ikAGr82zuN229XdZHqwCJKoSyrQ7rUFWghyaTSXHzykkUgPMC2nIi1Gb9hqhhb3me2tbsjQyle35NRhszDwOvM71p0358Va-AZz-vk1Deo2db7hXSfSpHI3pl9O4KEM3xr8zgm0h2KDxekZBWicj0NjltJqaVarRB9Cv7CgOo6mh-ExUOH3UAjrXIP0YfD-pePPO--EoSC71yiAEB-TedCG3lozqiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25603" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25602">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnceNhjwlh0mGmh1cM0qrZRYkNpfRzEZzBJR1v2OicQllMu3Osx3PkUCu4bAR_4K1UEL6aVQypk5lUmI3mcIM-gH5SBwNSUt6PpB-pZ5JliUwGM4z5ibDyg5-GZKSE88plv2Vh_9IJ7PWa1p-J7RQ0EVwsYKZ_hdT1g6bZ7GIJOvMU_55CzBH18RHQdhfbnTat8-tOKc8pPJH08eHydwNi2Yi2Fmmwg_VGEs8lQG2wvbAM3uUZzePt6PdmchfMsEab0SgdrQwrPQn62OseeSP68mRi7SqWzcj68-w_mQlRprNOnFGMYzGnzEWxz6SIIXxhEtQ-gCL4Eofzk0ybJdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچنین مهرداد محمدی جدا شد.</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25602" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25601">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📱
دیگه وقتشه دانلود از اینستاگرام و یوتیوب رو بسپری به یه ربات خفن!
🤖
👑
هرچی بخوای فقط با ارسال لینک برات آماده‌ست
😎
👇
📥
دانلود پست، ریلز، استوری و ویدیوهای اینستاگرام
🎥
دانلود ویدیوهای یوتیوب با سریع‌ترین حالت ممکن
🚀
بدون دردسر، بدون سایت اضافی، بدون اتلاف وقت
✅
فقط لینک رو بفرست
✅
فایل رو تحویل بگیر
✅
به همین راحتی!
اگه دنبال یه ربات کاربردی و تمیز برای دانلود از اینستا و یوتیوبی، اینو از دست نده
👀
🔥
🤖
لینک ربات:
@instafilerrr_bot
📱</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25601" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25600">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_gfhoEuPBNrCTOENVWW-472bm0OOYoEB42WV7S-GQQe6kZTZHRGLr7tki7l8x9qdsNLYF3JCmW0enbK6IgVJmswMB5pYsqAZ94UGYN5UobI-CydEzY_Lid8cIt6SdjCzXh6IzikEwEKRzORe7JpC38RZWv1nF74N1swDtTETlrka5jSFd0t_Yrt6aJISCuX26qDiFrKik9Bx9JkHuba-musCteWtqyHSwSDZWpns1terUz7EUpobiR8H4vbDiOLmPYJqR85h0JxvJnpanSVdOMNtLVXRH95hayuGTGvOS2joABX4g7L5LXzDLnKHNw7c69nE5hrjSTJCWSPB0fRzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق اخرین اخبار دریافتی رسانه پرشیانا؛ امیر هوشنگ‌سعادتی‌ایجنت پارسا جعفری دروازه‌بان‌ سابق ذوب‌آهن او روبه‌باشگاه تراکتور پیشنهاد داده و عصر امروز جلسه‌ای بین طرفیت برگزار خواهد شد که به احتمال زیاد به عقد قرارداد منجر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25600" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25599">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=CpcIB2kCoTPmJvSJj50rDQP64detr1hFX6YNBh9i-3UQpl0tdtP_JhMGxRWRDCLSNlF2SDLK-0pqjU0k3c2CuHjrP7IM-E9GDPclCrDzr9XjrAiqv2SA7aV3QeFqymYoKd0_8MzYUFFy-7L-Yzo6MCuNsdbFFXc8i-yAwS76prXv7tHTIMSXyNA6i-qhn-bxDT17k3GPprqGOvA7G3cDbLFQngpeRPxpDFP32CrW-hW0xCNViFpEeXJxlX62VXZdCq0TZm1YaThEYn8cWu8xJURzu7HIe8fpxtfVbvDBhuMTnF9EPQOwP8wfEMr1R5d7SKZolOyASDmokeYWu2E3lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=CpcIB2kCoTPmJvSJj50rDQP64detr1hFX6YNBh9i-3UQpl0tdtP_JhMGxRWRDCLSNlF2SDLK-0pqjU0k3c2CuHjrP7IM-E9GDPclCrDzr9XjrAiqv2SA7aV3QeFqymYoKd0_8MzYUFFy-7L-Yzo6MCuNsdbFFXc8i-yAwS76prXv7tHTIMSXyNA6i-qhn-bxDT17k3GPprqGOvA7G3cDbLFQngpeRPxpDFP32CrW-hW0xCNViFpEeXJxlX62VXZdCq0TZm1YaThEYn8cWu8xJURzu7HIe8fpxtfVbvDBhuMTnF9EPQOwP8wfEMr1R5d7SKZolOyASDmokeYWu2E3lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
علی رضا بیرانوند: یه‌ روز طاها پسرم گفت بابا دوتا اکرم تو رو دیوانه‌کردند. یکی اکرم عفیف که همیشه بهت‌گل‌میزنه یکیم اکرم خانومت. منم گفتم اکرم خونه خیلی خطرناک تر از کرم قطری هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25599" target="_blank">📅 15:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25598">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YufAfD8F9RbsXULZULStOnhbNr0GeBElBudWnEuF-hw_ZkVyQ1_g6E-FpVjSnL6mJgfDpQA_qrgml3SBOqqs60fHvYo4Jm_iiZBdpPuGWtgAPl4qXhIxsHUPYN8CtIowF7cPEQ_aDo1WwjMmvYB46VpxynMMmCR97-MpJUaAJIyhbzLK_RZVIpqYGvEqL-Ti8xv4zettHy2xQWkf1IoGHC18UoaY2CfRZO9l8Am1X5KuudUdfQtlhRQQfKIMPmBf6XQ_3wrNhtte3q9TllFg6IYOt6SFnBLpvLsSGRRk1OgrHV01a5IxyK94DdxgXzj7hZ5yzPE4WoTV2VtyJl8xow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25598" target="_blank">📅 15:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25597">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC55cSN2_bMlXRfQ_CbDU6ridyxPKC4cPYd_NrF_5DZpifpPhrp6Dr3JJBXovdIA4CdGB9kuj79WfNAy3-Ah78K4k2Dvo0SliDcv5dCERac6Rpgi37CCC8xBjh8gPn4RiBwdqVq-SOxv27y-mKvcE-wC1UyO8LRS0EXpbMgTPf_XjSj8w48IYZlBP0tX9ZP2HkYNcCfkTBYUkU7E_VNxhJiQyduEnsF19ADzNh59LeTY9imMdxt68O1SptRVUo6xeiIc_zQtT3vsUj6vqbGuymoTOPU-R7XHe1Vb5TA3nOorcjF4Y7V68G-7dI886Nh1iBlibhmIbN8lGrqqktsXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
👤
محمد جواد آقایی پور 26 ساله که دو فصل پیش سپاهان برای جذبش 100 میلیارد تومان هزینه کرد باعقدقراردادی به نساجی پیوست. آقایی پور در استقلال خوزستان فوق العاده بود اما بعد از پوستن به‌سپاهان با اون رقم فوق العاده سنگین افت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25597" target="_blank">📅 15:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25596">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORAHJM4nNyLegM70iR09oJ2ygFULiyj1XkmV7y55_YVpMCFy02NCFE9XL_QhJsilxDrp4N7WmIqxjnYUicdTn2l6TlUM5twR-KuNM3QRMeQeQsTRYmuWF00f2JhGuvcHvKhFqhz6dl306vTmBDSHORMEyfe1ypwArGtaTZ0olpfEjT_VE2hkvRYR0jCwlqkIyeXV9h4GHeVwwbXFzO9wxLg842CD1CDHjtaXhi0Uh0XgocYPtwFv04Ru7H8geEBm6kHhUFihH-rqDqzkirHz4kKTEQombpORlczIMGKw1cZF4xQZ88uBKEZ24_LANroP1AmbW7e0eLkIGeIO0w8W9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
فرانسیسکو ترینکائو مهاجم26 ساله سابق بارسا باعقدقراردادی سه ساله رسما الاهلی پیوست. ارزش این قرارداد سه ساله 45 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25596" target="_blank">📅 15:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25595">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzbqnMZTIbW_CMJLXs3iXYTYl3zEHEP8ctGrOxIg5ENykjumKrs1dSPSij220BKd2_R4uStxkQzrO5YXhUpf_mkJu78B9T6-FxiwwdHYUVvjgXxgXqzsIDYD8Xv3o_VgI2zCjRSNq_ZN7ZW2K9aAHjagaELn4gOwBqmPRFBu2VX19HDKlzFmZsKa7RSZlo8BiwaYMwwnQyJpjeQ32EqtQYKGQfBvqLfCzOXPvNOUT1soq9WaGf59_gPFFrIsk43iluN6btSBwBs2P13Pddn3c_2UCbf0wl0prtP70tev3IsqeH_6LdUh5Ik3FI3fsHTQhSRjFx4Snfld7h21QMSoAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇮🇷
بااعلام باشگاه سپاهان؛ سید حسین حسینی دروازه‌بان 33 ساله این تیم قراردادش رو به مدت دو فصل دیگر با طلایی پوشان زاینده رود تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25595" target="_blank">📅 15:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25594">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgoX8Q7Y-PPfzEMokRSMlxm590oAB7s7oGNzGnxLH02ihHOmYzCC8FtMoE-ffCQFOQhea09QXp2PgpI3bekuRPtrn57cYwdVr8-bMk9spHhHpJITqAN3hjnz1PddiAn55wIkJW6aMSpLpV2Mq058fVYNkcE_Dq-VRYUJhx9TZyc5mNQwARFJoVBX8hxJgFbYTZakbxWCXbFiazmjzL7_IQ-a2gEq14X8vVwZ-CmXnwklixBmfd_WfLACXGUo5hZUZ4A4QH_1G1cNGSIcIDed_ugP9U_BfWB1mcVzv-TY0H6K0b4T5CzpGnNlIsH-_IwcB2FLO9QJ7RubkZEZ3m7sYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25594" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25593">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4JWudC93chGIUAhcLdk4WAE0mvAxOvlCzvTFigtbYi_518xNXOfAyrYSO5oE2qWYCjuF4JcKIyEke5173MqIPOwG3sLwYjPZ8e4EqWreoVmZkN_pOGqHKnFmydvn9yyGKqtwC8l7Gjdxt2wU--j97tP1vOKRYgR5FtQu0AgTeipAEDtjytHTx8jo96D2MNN-aNxtkzpYRQBj0vojc95w3cZ1NMybjgS0xn-rVSymo0RX1sri5An6HWzc2OeR7VBIEIyQ3O425BJKJpzyrM2tv5L7-UkKvBnxB3c7wyDGRZqvIcctk1dL8jVOqSjRHlQfDgOLgJX7f7IzQQuycGagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حسین حسینی با تخفیف 10 میلیاردی که‌به‌مدیریت سپاهانی‌ها داد در این تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25593" target="_blank">📅 14:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25592">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLvmscDvJ0DNSlhrvbGvZGNUJ7rBaTLNuwRyO9I8xHbpoFo8GNzd_5PiUaiJY-zUE4Az3JVfk5foQDhFhZ8Yy7D1aBJ2nGyUVfjfTvReCz03a6FVCiwMDhy-P7-Sz3luVGKycSSFqjdzrcovL3kDdantoqfoQrpSNvftn0FAc5Y4aIG8FenxNNuS7tq8xrDACFhgBlplcRkfn2WJb8576l-M7lYegFDj_gwWP0Y28N05_BYptCa3Bc4XswRlRFf907A2tHdTt2bzzvLL7HawGOgpAxUFCXw-y9tCQ4fv33t_5JlisDolGIw8fsqXWl7YngZNCXs94CN7J2sz9GlVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25592" target="_blank">📅 14:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25591">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO-P3VxH_Nky6qZ-luxcLOzRan0t7YMx8hXdbziJEecwPNLFQlkZp_288ylkB08UmYiARMf5-Y1H6U90njEsfOZujYnGwpfMzDi_AXfFnSiFLcTmYWuxa7VWiNKVZsqFuvJp2xP6ikVv-Ul6SmOkqyHqQhVKZUv902pBNRx_A7rLnVfh9N3SPSSts5dUNQZjeNTQoY7qqwEAOesaG_QaIYaOFoAJpOxAboZ4hZlu0KOMgXjUkGM2JJmNiZxETZ-aJcI7VS3vohhths-ZjrFVXPtDVhi6vc10IWOSJfRXQmVYXZl4ch_kC8KwE-id6rUm9YOTdlRADCQ-jasgfffw6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی سابق دوتیم النصر و الهلال با عقد قراردادی تا پایان جام جهانی 2030 بعنوان سرمربی جدید تیم ملی پرتغال انتخاب شد. دستمزد سالانه او 1.8 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25591" target="_blank">📅 14:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25590">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcHEar9RJtuAaX92WVZ-rNjf4Vh4Qbb79gK5bJXaOY9niRb3dkLnSjvzcI6zf5VOrLo1bxVSdR7Pag2zFxLOisWIs4It8wHeodAe2HXAt0rlMX28vqxs98hgpIDsje54a4B76zLij183QU4xHbPNCyUbwojon39v7PpDc8dH-lXh0NmXpD89v2AgGu4yMR3k2wmzD7QjFpMD3VWgR-q9UJ52tlPYufzW4Av9U6FShLfjkNJtVFeDMacS5FRFmASx4R3F3PLtYKAILlu3NqRUR9YD4YeNo1NSL5kA_-uf7oQGWwHALgxfVxsI5-0FbVLsMJwKl-H71BaDVdQHNOV6dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا #فوری؛ یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25590" target="_blank">📅 13:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25589">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U60ueuxhSHBkl91u4zF5RY_ejCScCHgLnEHpzVKzM_xumE_RQpYmyuYK-PWZAKSD26OIlTFF95UMQaeeN-bmdf0PmQUHvUoWYVJ06W1Y2NL8OfVWjgthxziLLjdHwWpJaX3OKSPbY1HR_wLcgvdhsW2WMe0DqqCwclx-WCFeydWzOEmLmpfw3xfjVQy-fc8YX5nGzpegMnJy4IuFVacD3hfLBNSJxDPbjwQ1Y6OKjf9ZYxwUkWoehhdMQzJ9hDpbApKaolEhJSJegIq8jYjaCSfSjgMQ1CFpIMCziO1mVnLnvKf5NaVcJu9tf7GxPSCMEsE2wgoclCXSeJ2Ue2WsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛
یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25589" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25587">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brbVKP8pCFQEyAkEHfEbaQlEjmYCSHIMl3e4Rhruc1sV46Cb6HbMVPE2dIH7SFqdZbe4oemmgHCfFvDjWY7DH6rsCINWyaHlVNNmhaVPnltg1UsTzs4Mqf2fYmsq9iwzyFvRscFYD9xswUVanwjjq28asmcAhblVfgYyjGPeqSwjhICoFLR0NUuoRQW5H-TDG7iRfaBiwaL9B3ftPBmcCt290cKzOz8PydblsrvFAspKhdgdpblZKka8gR-43PGuSsuG_ywOLGLFFcjVpDKBjGxxdMxPJYpmC8VhC_96Oz-8Cg3sLzleMNxY-r0zEcjtsHnHNjunCR89iGxu-5xGoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXlGKExfCOIcaaijQerq7OExeNxugrzjbxd2TofACMJOyA85OiXEOycclkBQz6VE988v5WMa34vKNvRJNtTJ7X9mJUK1uQdebS-mAgxOcvHLZ94rywg1lUZRopebQrDUwYBjpvjePVAVXRFWfM_ceBh1YMSz_8FNDNFMEtEe0UEfyhdlFm3DgwUZgMf6JMJ0GJJKvcNT9-wx8CJYirZ3JQufs6z0Kbik1LLbJnd8YFtqA6GgGVoThTD_uebMF9jckY5D0nIMEkr9HAcGrg1POGhy9q8rP5A2zDeyOXkvQcdP73cVqzeEHYW8VYv4k3bbt3GAJEMasIZzfEx4h9_jXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امیر سام دلیری مدافع میانی 23 ساله نساجی روز گذشته ازدواج کرد. جالبه‌بدونید که همسر ایشون مدافع میانی تیم بانوان پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25587" target="_blank">📅 13:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25586">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etKkU_Djfbw1Ij-lrZeWqlXqcA9sIEYLAvLPH_TxKe0qQqGiAClxtSvG22qNXR_F-ia6ahFZo4l-2b_mEaKdgK6oRDjdAcOmhPSfnkhxReSDi4W51hGyHaua61GRWI8ZZp3PQSEir0fiEzRxA_1azxXCNRpnOig9hRICu5zu7kNpzt06NPjglcEGeItAxv3mmbvzosSsZwIPg2ni1LLL-OSJ9UU9v7cLU1Vmpsnm3ErX4G3eFun5zfVoKpNnXYhKHgWmnPNG2iIW35AanSfAjh0k6EJkADWfgNMeotUJrrD7pujn2l6joBOgLeBjMhe9VWNp3DjGojbA2kcSpITwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25586" target="_blank">📅 13:22 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
