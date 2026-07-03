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
<img src="https://cdn4.telesco.pe/file/JIQpRkqx9NoEyOi5Jl0u1L23smQd2f63yAJjQOI7E2VEAQlxNTBHbyTEAfO1_IqwReJGL1NMDUTkq1tMsllVgxZWCrXLglrNa-4cG9gN3A4H9OnlbGo1pIkcZTYbOMkELZmD_GUW0_yd6Tw2GpTfLJ18TvwOTo3H1J3ROlCEE7jY0CszWmQQHEHUTQcY3qDTNvJqgWPUpk6uqIY-0WtLSbYkpdMg3KQg6V9ACp3UWmS7Nt9RV7MNLHdqsdL1kdXnEeKlkIU2qOWA30MwM_fBlzokPHDaWpPz2inAolF060B_SqzudOn5XJRIxsEH8NNLBzBxmUiKzYtZvyqu_DdNUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 361K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 01:28:00</div>
<hr>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ3m8EBCRxGPCPS_OV_Li5DZ96jrXENx9fSZIb7v1VrAk0DOxzoywRJWlmdHJe-NQVIYxqckDEHiriO4ImB1OzsngDclGuFJFVJg8Fkb7Jy34QTWXQMEAL2pwxxM-GohBMs115tOv8DWc1pSKkQk7dBgpsX3coeLwnfTuFdLzLnWg-RMEAaUX4QRnKPcc9JpsR1IXJxyMxsBc73WoAghu0bFXqGug2hv8KJ3CPJh_t8bxgVAPiWoaSbctFrSIQiW8jkZoSvAAwPhm2nd_K_oKYoJiS-AovFnm_pebempJP1Dnu8F2JJad6keNzk0ohIwBYNTSaUaF0cxQFieI18CyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUV4QWK8-GdRfRu2dzDVKXBX-4CpINwBBjWrgKFtVRbPTNTTJcdGmnLSjEgHa7WZhPOablTiey36HQB6Ns8rE9SS0LJtRFLHHMDyiKHHj_mHQJ9kYTg7DRSOj8Wr7n20HakWe5j_5YWUXhZDGqkZkdlWFCa4vmUxizbQPni3umksLzeKNn1hMSUG1RQZcyO_GBK9raXELbA5G4GQg0xSNlF7n2JpPtnN-Uv3pg30tZ7FcM3YabPaM-U4saFjeg9v5FNRQg3cHk51BBgmQQNC-LrLgU6Jo2dWRNuuE_fx0FxcZVfDfWeO8VLVNmoIxif8TSZD6rFqApjzfeHYD7BQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Hgf9fxLNhq0gF66M1clv5oN4ygh3PnPUj6fIHVRxr99ZHsi-O9XUmz6bkArDGVBaq6OlwP7_Brfqxo0_lSdPfFuXrwr5pgyuNSsAlKGZBKUud2DY176sM9xsxDWbEscG6JdlUywSePsuQWcscYyWp2XSJPb8Uae6a6-oTtPoC9Nn_8-WQvp_YI15uoReywQX3kVgbUYf09imd_YTQ_ieT4rE_ij1eLku2MH6z5bZ2dv-aCBkQnDMFIGoP__JMIOQN2hBkuo4Jl9iSz7pUOAvxwhjSjgBMh1mFNea-tMmkGmvrGfff-uMwosV_NeF5F3fv7JBcpErn2lB7nUomyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7XbEm1EMMQ08_opBMmiIEI-u27AnO88GTp6F7VhN7XAWF2ttqPa41KYomLUWDQEAs4XkVGDWp3HXVMwCLyAREdTDpSGevGlTMn7UrQHGG8AXhWP3Zal0HI6GhQBxfMVxz1VdyE9KftYMRvxeWC0pK47F7O3-kvtexiLnhyz6HAdsq3BvoIuULNcqF4h5_0Lq43XTnCzWcdycIRtDUuEz7HUMjEib9DgP7GBupTI4vHXB86vuxs9zN-jmP_pn3osUxYnct482NimCyqVxhK4_ZhnieKTvk_sGNx3vAKqVePnaujzmBdWpmP6n4SwkkfOOdUleps2P2GR_WSOCtPdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24897">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/24897" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
با این سایت به راحتی میتونی کل ضرر های جام جهانی رو جبران کنی. بونوس هاش واقعا عالیه
👌🏼
✅
اپ اختصاصی با
دسترسی راحت</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/persiana_Soccer/24897" target="_blank">📅 01:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24896">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBzoouCLUWk_j2NCqni1KD0RxkVOLsjhVkxYd1pzvGOM0VHtW_m5sTAn7N8q_1OPrtTKw6XdKwh80kY2wBGL5pXubTOwtx_OZkGhEECLjVVskeATTQ7VL2Z6lEyXKYAkDxs25PQPXCXX6AWe4KQB8CH5t8NFu56V2ilte6CpLFZUK9Glwrv7deIAPq2FWISyHogr1mEKsnqE5olrl7MntxgM5ueNEWdQNwfAaFexvnA2vPwH7PoF47StFJIwwLR16LWIVvri5jVaftd_x2jMyRznzI0GpnPK7nJfEN2yE6-yrnvOyq5p3imgKw17iBiNMP3nATBH9LQ2KjBBmONFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توصیه میکنم بازی های جام جهانی رو فقط توی سایت بت اینجا پیشبینی کنید
🅰️
📌
اینقدرنتایج‌امسال‌عجیب و غیر قابل پیش بینی بوده که ما تصمیم گرفتیم به شما کمک کنیم:
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a12
@betinjabet</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/persiana_Soccer/24896" target="_blank">📅 01:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktggsuQgkEiBQ-rJE9fUv5Kw_ZjsmNeujV1cZrRGdIh9_fTDSiBLcfTHD6Z0_WSZJkTBTWK4qqVcDNY2S1Ffh658naHXz8qV5-Vxca2WKGRasrKHwDzbB3WEDPA_skub7kLuD-nPlonCflSSDONa9dOpvgG49jSp22ooDuShE_OQKQ8jWAW46Xp68qaEOqF82pRM5uCC30ApW77lJ5lMCXPWcNULFYMiQIPf2DtuES79eBjaGCQ4iOn2Kz9NSYizNgrYYoyNNg_2Szq1p_DvMCcIHh0eD32j3OSWpdHCC_bIdhVwhNIraU4kaHYEsgzIYFYnZGUn8FyrChSqietp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=plX_JuxoxyDaHSe0MijBF37xbQ9YJkCbcktYlSieBkruu4scHajgpdhrReuwxF31EV5UnG0GvpIY7wt71tOmOO9UnChSEMHl2vuqzlapRj4Cj2Kg9_bssQHydd3z_1gzAqc4omEhCMlwSrZNtEUs8iCeeKR_WPhlGPeko3eV7ZazxahN6USuqKg7x9hzRi3SNHXXUGpu2wjKAE_htdz-2LIImpYoB97WNVyAAcHLgmNpNvUJGCdjbwUcuQXvJ6BpDTnuNxxmnWMUdbXlYG0_BKG4PxDNEvtSs9JTdBEbjoKl5FkTgOPT646F0jV9fNjUutvJFUniJUcyRFgNd_QuTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=plX_JuxoxyDaHSe0MijBF37xbQ9YJkCbcktYlSieBkruu4scHajgpdhrReuwxF31EV5UnG0GvpIY7wt71tOmOO9UnChSEMHl2vuqzlapRj4Cj2Kg9_bssQHydd3z_1gzAqc4omEhCMlwSrZNtEUs8iCeeKR_WPhlGPeko3eV7ZazxahN6USuqKg7x9hzRi3SNHXXUGpu2wjKAE_htdz-2LIImpYoB97WNVyAAcHLgmNpNvUJGCdjbwUcuQXvJ6BpDTnuNxxmnWMUdbXlYG0_BKG4PxDNEvtSs9JTdBEbjoKl5FkTgOPT646F0jV9fNjUutvJFUniJUcyRFgNd_QuTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛
به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxQ3FrKx2JJJivBogD1S4G8W7qYv4CwuY6A2IOt4TcLoYJa_Ut5eBtEBO3RxAhcgwYe7N8sr2-nHpQuS-lp3vBXGE9WLxJFB21-I5-CLA339BQzScYNu6lT9oaoL1Ha5OYP_dh2VKVztN_QtAN4_Yd6n2YJM4wZMomtcZe9ExcrSR8KA_0_vz8PtyZ1A5BtoS0DmFi8_5noROfI2hqstwEg2RJf0aaK-LJ9VXyO_b8AzR5H0EIe6r9pmXfAxFP_PUqvhaZgp3x_UCtpKXvIc6G66W_cfSeMXNkZ4KC3vDPFeeMp5g4RVAoMGS8Ugmci2BIYZMnFhdLadT09_BPygxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIxl1cQP_yygWpZoM5XZ-z64Z2dqZKUWzCPD1MVQADkeezR4v_BuDOZ5BoyXy1YrRy4HqqXYqkCV3-MMgUGFspb1sxUabvHhiYfVTBTN58f78gnih406ipPQCCZpkI4wHirefmVqwnMMmGlP8jKa4zAWMMsGnvo_9r29G8rWQlhzWze4q5DCqJFzfkJfPRvBfXZXKLAOV6y5OF3MBj8tnQA2vjK4v4x48NPBiBmUcL-8GmLTN2wRQMp5pzF1fJp7vNbWELOKjFKsdYWHhWzgOj-1Gbocn2uretZVA-DlIhqHZE6ZGhUHMj309Gb-c2h-RagMqFj3cm-aV_8TifxqBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛
شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2OZkRggAtQIXwnH1WaGccO6_G3AElwlq0Jf2zBzaxP0mBm9Q3ruAB2zyoNceM5IHkX67xx0snb9iJFpMXDFKbb1VPxOEcQUo7LyDZQTphJOmr7-TQnO2TJ5Ifg1nOCMVZFVCWwMHsl2hm3x5e6qhp4ms6SMy7skZ3qCnLJIGS4vWGuAuTc1sy6tGk6HyQTAWYGUttY9lR7ZcqCnUq8DrWIYuutsbcirZsYdQRHBowcrrvCZfRA_LXLK7qmVo8O3qCDXTW3ChH_g_RDGbhPQWyK8aUtzxqBjqpGCGImaPUTyVi4wbSigasTwntXeL-L81LL3AjyjLPmVeJ2GAU2LeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGaaE2O5eSUqc61cgNXsuyARlieWXVdUPfvKDETzhgebqZQzj2baLQTYe8gy1vCxWvEic56t64t_jRajmUR6xRnDzRV7AS-Rr0ofIlqaq-S44jtQqRlPJ_csw67IEM6eRnUg6dOXaYVKJh4tM0g01HSThD-K7HL0FxXqmnDAvBfzuvP0BLY__kO4SnLbgX4HPU3u2x9LgHXQldGOPyngOZgsdrsdQg72EA3EpFhAxN_9drEjv6Ba5rogeYgUkuiXAwmfKUkJWLrIuynDQUh8llqmG0c-t_W6M1nsbElpgkB2IDH9Z98T2pnSrkrB0n4WI2-pOI78qmpziG_HDireZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsUElJ4kEmDTovOTQvhYxD41_rLQNv1wiGk_FKfWn59-urN8mi6mnHK7VnzkUHuu66hcbDvJMTpv13B-xOasbTzk19LrbQJ7KSGIIi7QnOxhqAhOL2EyiK0BIiCTj5jiqKQUPyUFdA69zdpwDEx9rNTUtCxs_EoIqarFlRFN0jweEmgSv9yflR8u4eW5DWmmdcIC1qU2BhfmPKoBjvIMBSU0VPlFMLojoWPhRqx14yFv4Azo7nJHxeneCY3cP4jIrAOWgEXwGEwT1mH4_nLgsAgu_J6cXtN45u5-rPXkrxxQerXBQUzOVKdBMeYcKKWXpmbFUeomPph18hJ9watvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO_8rJU3qwUeqycduwFJI1-4oF03sB1krJqGnDakoKHjIYf9OTNPAbaRbedzoo1YkUTls9Sy1SfWyqNhGXbAUEgkI3Mb_Cmblz73Nwnyd1CHgCB5l5Ov1kYI9boOOgA2BoXEs0fM6DdOWeOpc5twGJAfIrKdSgdlDY50Ey5MJkKHlSevXUvWRrmsP-wEdaaD0vQoY5ZyJdmY9_LYS5UWEMItH0y-VFmfj20CYfe2PaxwL8UDdfEzSqXGxOpRoeHFmEojU6dOAXDr99Ayby0Je80kxG3BBbsoeJ_hdaGATLQYqz5Gz_W_GwDNCnj2geWviE3A2D_lDhnOVpPaHyQ8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r48c7rKX2P0D9KML4NLF4PeBd8Ykvxqkompp17-A5s9kmR2N4NM36RXFpaziQI4VU8AdCDaoG9tZT5gptKbpfZ3gETet51Vl8oY2F-VAQr07RYNT-av97h7t88q-1Xop2vLEbpoBQSrJnAgXMtXqHdI2aYtPcneaxd0-8LQ7V75vSBkABVQW7je-A__e_0HWlzn4fDlrjRBAToJH3koUx2JIIrCwj9fWqT2mc0z3PniJAmyYRGhMazc0mO29sRg9HLMID8Mz_csAMRNRUCQPrue4tUthc9X6PdIwU5FpWQ9lrtObKNRPgB5-y4z67Nh8-VbtgrBd9908UZuvbzQ9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24886">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHTwD5F0k3TC5lLObNGIGmLs4oF2SHrbBzmRkywxIsuw6Wq1_rESuGoUn-G46LWs8W2j-qZ_cqZNZDKE-ICrbA1OpTPpkTZmUDljX_UVFuqM0ghn0hPtDXohKg1ToC7GpeFDf097gUE0DWYckSw2eWZZJBZQKeyfKrQDvddzq77SX91Czib747bOrt5femvg3aHux3Tr8UWrq3JyJxBAbmVJhpOzvrryKHX7Qk24Z7tYPC6a51Zd5zK8btHYcqc8PDQHSdveh56jXXBAvCA9wr5vn8CCK-wIv-vcJ7xoNGx-YypTgMNi6Vy2_c6cTxh2h8-2qzKAoTNGS7N9kHKhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه لازم نیست بین انتخاب‌های تصادفی یا تحلیل‌های زیاد سردرگم بشی…
🎖️
همه‌چیز برات به‌صورت پکیج‌های آماده با ریسک و سود متفاوت آماده شده.
🔝
فقط
پکیج مخصوص خودت
رو انتخاب کن و وارد همون بخش شو.
🏆
ویژه مسابقات جام جهانی فوتبال ۲۰۲۶ | ۱۲ تیر
⸻
🟢
CORE
📊
انتخاب‌های کم‌ریسک و مطمئن
🔗
ورود به پکیج:
https://betegram.com/share/betslip/ZKTRF62467
⸻
🟡
PRO
📊
پیش‌بینی‌های متعادل با سود بهتر
🔗
ورود به پکیج:
https://betegram.com/share/betslip/VGPXN72923
⸻
🔴
ELITE
📊
پیش‌بینی‌های ویژه با بیشترین پتانسیل سود
🔗
ورود به پکیج:
https://betegram.com/share/betslip/DACCB49184</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/24886" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_-D9cQgTTkYv3kUsbiyAag7xF5uxj1ph2pU9D5seGWTqYM-6uO9y_B8rWPXb9lIjFElQyQU_RahdEJ34RW18V1HkuB-ooKLaoL55NASpfFEnYdiZyp6VHIN_LCl6fkww2ILO66UwoAujrWwwzYcrlB-eBAdqSg41ovtmD-X2WdgRFjLvMK-_x16SQF0gik5PUAbgX5TeEqtG_q4KNd8oUI41TGJBsGV0xil7aTYuDb40r24c8-yGntYZ_DHORK77UD-eetdwjH_2WzviOOdpM5QuFU9B2mqmrzk9fnd_aIQ1Oz7u-p2c5KDjONSGhh9Zz2bhGuhNEbgHQoKkT-wsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBWr_Tiw8MWnk1ZRGpCYIimhAm472eTGswDYhBWyv35b4OWBXCklfaivUvp944RjGcTSPP91hqAH31N4c4G0Z4ytQN2tWeJdkRCiMR5GMTdkMwZ2ytJZMNO6UBJgOkJRsMknS2JFqRflKhYOoNhBaJzH1iQQFmiaM9Lk1E7HGNxoWr2ptd8HgqJof51_50QPpeMmrvZKnCI39Cq8qZG7oieGHtxeBi5edwGE4z0-8z5u4x1hkigZSlPAt7ifWbGt06ulycyAjUBXJ7F-w25w89-2xwrUGweQI2AnleXfEekc4mxsH6iY_wgM_Wkvuq1JB9Pwv42U2u25CkzLwditMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=rN7n9BFrkI5Mcp05D_AcN09g4up1DA2drSSbT6eueeK7Jpq_d1i5q9Ffqwjt5Q6abGNTZV7t043Q2Xvzms-RjxTMdyxYEC1P6wFipr_AxG5B1hGVDzMLqferNy9g7h1p--F20A0Vgwr6TYe0yd_BTiKadCDvxTAN9w74ED0qGZRx4o0vFcUNCwXtTR_CjeFyKB4WY8Nn6loFZcv4zsuiFQfxqMMNJI6YzDXDlhK9NmauMwkb8g9eN9Y7X8q4MIsLRUvrZF8ZXFUQCEc97deq8v_IMGwQE1ozd-FcVhZVZAp7jj8cJ6q5o1F9y_jhfHAu4fdZLTVhYaU8KqnD2s8PeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=rN7n9BFrkI5Mcp05D_AcN09g4up1DA2drSSbT6eueeK7Jpq_d1i5q9Ffqwjt5Q6abGNTZV7t043Q2Xvzms-RjxTMdyxYEC1P6wFipr_AxG5B1hGVDzMLqferNy9g7h1p--F20A0Vgwr6TYe0yd_BTiKadCDvxTAN9w74ED0qGZRx4o0vFcUNCwXtTR_CjeFyKB4WY8Nn6loFZcv4zsuiFQfxqMMNJI6YzDXDlhK9NmauMwkb8g9eN9Y7X8q4MIsLRUvrZF8ZXFUQCEc97deq8v_IMGwQE1ozd-FcVhZVZAp7jj8cJ6q5o1F9y_jhfHAu4fdZLTVhYaU8KqnD2s8PeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFO5eClSUwA3-Eyvjq4pK3-Jjlfrt_M6pHcuzVhBgHSPEESQI9f5FKRCafWZoHDXRuzD_RqbOlJIvLRWj8B5rT5BFB8q3k1YzKdOVTOeTuQfqQXbtM706x7Wa8lhRz9m2OvtkRFRKSH3JnZdo9vKjz5NVI6i9-pwuuhVHAn4XWefz5qHnWgcYMnjf1pZYTyrpT3YrIslzB4lh6a0F4Ok69LAe49q6VEUc2tOuRcRSSbOgOL38tTc44vlRKYYRv_NPjdJpptAoXWyZolLmvvad4KBS-MITBwdAEPLBkrMwoqion7PA3QlRS92oQ8ALi_5rzZaiyXaoOIPy_Qbq6eIYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfPi4YxYvfEC9SrGLjRyrx06jCWgJTHrjoxHerPd20QLMFdJvAkgpqMpH6WXOiJ0uyONMzQsiZBid60AwyEsFRF6KZ_58c1Ba5BGeO5HBuM7mLV5Ase_W7QgyI2mEmTmznLDlcrxXupba43aRGjglyoOckgQabMswOQJUboucg8xV_VGGBb3INcAyUWkSzEkQQDjDM81zQcIdOI4D_QpQCC-a9Xusk9xcX1JHj7nA8luR2wM5dBwEop-d2hFGVrsjM7FVbDZ2XtIEr1eRtm0klKt3k-T0Wb3Ch8G5EpZi0U4fnlHWBODGn-LVeDbD4_r7CYcL2TDuc-6I3JM8ZfbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW3DUoUvCITgEOfWTmZHsMUvGRgSvZlOOwgxI37Hk2PaiGPjRoXH97MPQXfFekyxjD7UO2q-hhewAxinYRAf_5XeHkHgoxhYmwPanaKP1dox_mCQ709zt_nDQaPPwKzhSBjPDihTiDfGidn6ucsAXuTukfDBSulf9-D2e01-S9tICd2542imY1Xp4U2HUwdK22d09dcenrjS1oBVCP-Ya3MfYsO0eVWvxPIgvHzZaEfghwUhnKLEZrBBuYTbscuZxSXB8qV1J_c1uRLGVXYaW5AJrnVkX32eUkobH5TOC2SGfggTgLekU52r7yJO14eELZK3hjwZVhuNVDlcwA8VoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=XSHz6FjxGocusP3JX1b222ajkWyFQxa_PTy7T-a95xFWK2JuuyHe6ynV1I6VW6mByu_EHdjYYFfJrjPdJ-Gz0SlIqb1UQe5JWmnkIKard4tuv4gde9e9oH_3N_4TOFe82kt4ceXZSsX6FLIp1JgqISzrs1X0SPpy2wk4z2_NlREjkrPSYYCtwKksnYGGv_Kr9XwQn0SQWNmkBpr-owTbjhKr1RZbrGa071TTZq0JuV7W04k20fAjNoRrNr6EPv1NetzKfXCErdzD27XjbwP4CfUTq5BfQuSs5hlX0IwGAm0I3n5k7nu-uAnyNU07F3dOI4euMirXl85jG7GVa1vF1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=XSHz6FjxGocusP3JX1b222ajkWyFQxa_PTy7T-a95xFWK2JuuyHe6ynV1I6VW6mByu_EHdjYYFfJrjPdJ-Gz0SlIqb1UQe5JWmnkIKard4tuv4gde9e9oH_3N_4TOFe82kt4ceXZSsX6FLIp1JgqISzrs1X0SPpy2wk4z2_NlREjkrPSYYCtwKksnYGGv_Kr9XwQn0SQWNmkBpr-owTbjhKr1RZbrGa071TTZq0JuV7W04k20fAjNoRrNr6EPv1NetzKfXCErdzD27XjbwP4CfUTq5BfQuSs5hlX0IwGAm0I3n5k7nu-uAnyNU07F3dOI4euMirXl85jG7GVa1vF1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB8Rb9Xp01oC1g3rswv_IwRZn2BfQe0HsT9xFkaw6OQ05jiFyY9hTy_1ZZSMi1nbaqC79SYvpyLDTQkUwFa-jMUBuiFb9z6nsUZefMj6dala7begcfad-tALL7E0W0xIruJTvI5S1pxaz6qrk0W3Qk_5un2pSHUzw-okxFdIhkkbcygQhFMFe_P7gd4KvsM2iTQWaXk2X2RI1TE_8vE14JSm-ZnpQEZFYLj-WrFLENP0nT9Z0Rpqj3bjNgT1J6tCTo4DgIdQ04pUy9K_gLf4R-KdcDz6jD8xXVmrmnBFoiVHOKP-EKBsJESSoXDsN6bxAiQFUNTQYDZAW5db6P8SwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=njyodFnmz-zbJjlnvkYRxdranaG7G-DTA0B3l0VAZ6RWn2YIMvKZAd_ZN_WMPPnFbh2ulaq9TIQeNbTi1VxGxJpKdksxHJodoXWSTYSfi0YX9biQb8u8pbcdJNzYdEpfjjTZRu6XLMy_NiHde344Uq_i3X0WoVrvVQjDhyoXvCF4Yx4nl_r-LAUBG0a2faVHCj0Jz1ndslShF1ac1AQl1y4MtLuxZTEzyN8eueJH315ftUDFf7zT8r9OxST_lLdkFo8kCdI8KEAcN_xzJmc5itTeh2lvS2nhbM-gFr2e5DXexZtce4DhlXlbaYhPNbmOwUrAB74Z89l_piuxwmYs4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=njyodFnmz-zbJjlnvkYRxdranaG7G-DTA0B3l0VAZ6RWn2YIMvKZAd_ZN_WMPPnFbh2ulaq9TIQeNbTi1VxGxJpKdksxHJodoXWSTYSfi0YX9biQb8u8pbcdJNzYdEpfjjTZRu6XLMy_NiHde344Uq_i3X0WoVrvVQjDhyoXvCF4Yx4nl_r-LAUBG0a2faVHCj0Jz1ndslShF1ac1AQl1y4MtLuxZTEzyN8eueJH315ftUDFf7zT8r9OxST_lLdkFo8kCdI8KEAcN_xzJmc5itTeh2lvS2nhbM-gFr2e5DXexZtce4DhlXlbaYhPNbmOwUrAB74Z89l_piuxwmYs4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmSw7j-QyIUzaIXkDKrrxXZQMizGyBz_EoXAFZCUXKo8XDyg_aswwlKgJiDbyfrLLAD6G_-banJ9a7riEeBgHwsNHQR5LksHujkjMwOxrQ2zy8NtcwgWshukHsN_tsi6Aofdtr9iVCDSQgZyS2kMdIenqZG96Y1lhPQLhCxizStNdNzUx9CZsAU44hRljjfXVY4Nn4us3orRdlkIWTgFkhgFRWEhlHJ9it-N5UBOHFAHljTIeFFkycPZtbUFtCYGIKdZZZpPTEPwHRo2p17vWAmkLKp_0k0Ju7-aNoJgknWp5W7YN525NpjKP0Zy4tY1sPOcRVd06xA1BDwGO9uWxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=ICKjRezksHfdRw0iI1U8ocrPlnWw6D9Rsii0KUAkiI2FEfv-CeOFXAX5PxIJOkI1lGw2kR7wGCEkQI3g2hIMVcvNN8rKmwiWQ1lfa8r9DAY989UFd-DAI8GrZ9BffT_F9Kiym7DGhZyvfzHVFZENX3n_wiRyFhavjbrgLVcX9gj2ahvu0eO07zgMRQl0vXwGLHheAtN55HZAqharSJ0BkntbRyR8lWfopCasXE9bMiRpEAin_Mx6Z_mJJcgShNxZsUf4X847l64_e9qr5yhk2y8oeJF1lF2Zh_SOBILJG8wf6Cu98NPHsFCUTUgRcItIJJ5cY9DRTOud18xatbNCQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=ICKjRezksHfdRw0iI1U8ocrPlnWw6D9Rsii0KUAkiI2FEfv-CeOFXAX5PxIJOkI1lGw2kR7wGCEkQI3g2hIMVcvNN8rKmwiWQ1lfa8r9DAY989UFd-DAI8GrZ9BffT_F9Kiym7DGhZyvfzHVFZENX3n_wiRyFhavjbrgLVcX9gj2ahvu0eO07zgMRQl0vXwGLHheAtN55HZAqharSJ0BkntbRyR8lWfopCasXE9bMiRpEAin_Mx6Z_mJJcgShNxZsUf4X847l64_e9qr5yhk2y8oeJF1lF2Zh_SOBILJG8wf6Cu98NPHsFCUTUgRcItIJJ5cY9DRTOud18xatbNCQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=EWRoVPcJf6sx1wpfACFXUx7Du2ek4Io3MbqAbISc05DiF5m0uae8Ap_59ZC-T-GoZWqQLOJBA6ZZzeygyvoJSv3qjcMWFE6gVR2fsEE8QeUXkJ5H8M9KO62RmK6-R7vYH--zSy2MdOcU5kAnvwyYzJIG8wPMF2ZWSZKM6c-cTJ3hDSmpQQUxZwZ0ZPN6wNoLIdd2ubnxdRUwa8ChbXXwXFIzmbsAhnKSPIBNKxemMXxQ1XeW8c8jr2ddifDhZNpM4U_pX4YBmORrqhKE_kR2ZElHY1WOVhy6AEtnnt1gEyRyKVpwTOvDcSgRdCbJIpqX88a8YqO7L1ky8SS6YxreWDbM7ZKY2gyMti410XKgvIccjhXo12oBxxIHZdEk-5MCCHmvvlt6T3sGFKIFklwXX0S03erjg-tCImFZME7vILBYH_3NYZ-OIdxyCxtElEOBuBiVYZ3MZrpuQ9Nqek8M2BAEtFhjHlx-j8Nl_UCj0SE5bQ_CCT7sgBIcLqaJhApbA0A3se8Q4WXCxjc-7eDHHbqL5cwlkKnmqWcim3X958RJ12nz3k7sTGiFmkf2TEJM1XVw_LpcKs2oI2UdXxnPz9CitO8ZMoNEYBTELZYLr6hUReaL8vT_d4DQ1koGzOfcbzghtq8ZAC2F2iHxJVOgRi19-BT2OfuKbuumRLDg2fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=EWRoVPcJf6sx1wpfACFXUx7Du2ek4Io3MbqAbISc05DiF5m0uae8Ap_59ZC-T-GoZWqQLOJBA6ZZzeygyvoJSv3qjcMWFE6gVR2fsEE8QeUXkJ5H8M9KO62RmK6-R7vYH--zSy2MdOcU5kAnvwyYzJIG8wPMF2ZWSZKM6c-cTJ3hDSmpQQUxZwZ0ZPN6wNoLIdd2ubnxdRUwa8ChbXXwXFIzmbsAhnKSPIBNKxemMXxQ1XeW8c8jr2ddifDhZNpM4U_pX4YBmORrqhKE_kR2ZElHY1WOVhy6AEtnnt1gEyRyKVpwTOvDcSgRdCbJIpqX88a8YqO7L1ky8SS6YxreWDbM7ZKY2gyMti410XKgvIccjhXo12oBxxIHZdEk-5MCCHmvvlt6T3sGFKIFklwXX0S03erjg-tCImFZME7vILBYH_3NYZ-OIdxyCxtElEOBuBiVYZ3MZrpuQ9Nqek8M2BAEtFhjHlx-j8Nl_UCj0SE5bQ_CCT7sgBIcLqaJhApbA0A3se8Q4WXCxjc-7eDHHbqL5cwlkKnmqWcim3X958RJ12nz3k7sTGiFmkf2TEJM1XVw_LpcKs2oI2UdXxnPz9CitO8ZMoNEYBTELZYLr6hUReaL8vT_d4DQ1koGzOfcbzghtq8ZAC2F2iHxJVOgRi19-BT2OfuKbuumRLDg2fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY-UroLZkx0KzP_JwOHpGHwLFNZkBQ_3uxkOsJxW83JfdVllHsH250KxJ0RK0YyRHJlNFzL04RnAA_t3AvoO4sCDPAKUZJobFJIdrUKJoON30XjywATzPEm6kYKe9gzJMaWGBEbGYUUiZ7kN7UwT8BBZO6jyffcMWmhxxyqXmjJJdLBBhHqh9i_So6VSKsP55lYvPE4UjjKkS-BeLc7trUvE_JhntGSE4tmDFvfC5uEzIv0rvitH-V13W8UXrFz7F9UqiiGOaM570eESVltpOotN5dqVb5oPwTmqBolOWaPDllzAde1a8XWHZOXioZ-k6IGKQ4GBZWGBSpkyGxgEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=gh9hdwss9RTKakFXFKtwSZv2Aew_iuO0qIoXojk9rMUCQH8ZMv5GwxRoxxfu-wkz2LvpQwOXG7WUemwVeB88SXnUEbNA1BqgLH3_7Qc-6VnxVYdpMsBweGyf4rg33FVgvpa4yJaHjRnWb7ozTawM7bfIgQpZFVKaDwmajgPhVVwJUIcwaENFwtsKSlCfQ1OTjh4ic1VhoPGLAUbyS-g-TviLWulXGB8QHaDVhQzZgzF6Orih5oPSDNbON56NgN-1oZqpwYJj0mQe7zV_MtGZHEc3-UAyhVzS3IC7J1rNpkjQxCTKnp0BgclMPlSMFLbEf-2SbY3DvCSBYP5F0drNBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=gh9hdwss9RTKakFXFKtwSZv2Aew_iuO0qIoXojk9rMUCQH8ZMv5GwxRoxxfu-wkz2LvpQwOXG7WUemwVeB88SXnUEbNA1BqgLH3_7Qc-6VnxVYdpMsBweGyf4rg33FVgvpa4yJaHjRnWb7ozTawM7bfIgQpZFVKaDwmajgPhVVwJUIcwaENFwtsKSlCfQ1OTjh4ic1VhoPGLAUbyS-g-TviLWulXGB8QHaDVhQzZgzF6Orih5oPSDNbON56NgN-1oZqpwYJj0mQe7zV_MtGZHEc3-UAyhVzS3IC7J1rNpkjQxCTKnp0BgclMPlSMFLbEf-2SbY3DvCSBYP5F0drNBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=OytFMgiMnjfHsr8cdy75rZ6poEAt1v3ka-BI6Q8G9WRjhhlsIOiFTk5QegOjRYPLHLn1QUfcY7KM3aDSbafV0JUfgOr5XLfbJGsY9Kg8kwGjLZaIQtO42wfr-YpiesaYtwkYxQygD2oy89-MQH2SxNy8R4FuDOm-yJGPdeLNBCzgiQwj-kCXkdqQG8tOWo0wgYtkHPrSyPRn-Ut4G-klaoSJJS64bha2phbk3-nTfckti-bLGaWj6i1t5AgDpUUgUDA5HOmtzHyIPJlBkvMbXvn-HQO6bVoWxU2ELKsqZUMhARrCavBe9QZpbJHQgTNBd4TECXENg_qk6XzqKRA9YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=OytFMgiMnjfHsr8cdy75rZ6poEAt1v3ka-BI6Q8G9WRjhhlsIOiFTk5QegOjRYPLHLn1QUfcY7KM3aDSbafV0JUfgOr5XLfbJGsY9Kg8kwGjLZaIQtO42wfr-YpiesaYtwkYxQygD2oy89-MQH2SxNy8R4FuDOm-yJGPdeLNBCzgiQwj-kCXkdqQG8tOWo0wgYtkHPrSyPRn-Ut4G-klaoSJJS64bha2phbk3-nTfckti-bLGaWj6i1t5AgDpUUgUDA5HOmtzHyIPJlBkvMbXvn-HQO6bVoWxU2ELKsqZUMhARrCavBe9QZpbJHQgTNBd4TECXENg_qk6XzqKRA9YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=q3ktt_NlaTFhEv6LfnRs5fDyJ24A0yUH3uqZ0lC7oSK1bR5rLPXWC84yRAbGfAiQvPYG0I891UWMCv5Eyb3YcwFwH1cDCLGlNeALZgMpwd1EvW_fm8AAPHIdMoZ_7KnYt4CsPzQSCaDX6Psnyjh6a68qpH3Tm6-r93DQztD3GLsimN26vhDDffjwfq4ZZaZzIw02vm95Y_Sjxh2TeOvl-x2RFN0ShmYjObnkLiaCYQ81G6DME6GYjVN4nHDcDwdFeOQ_zQnv2A5tup5IHFPzVmfaHOpCqXliyO85hjfPqd7aWAgnSPX_-f0QOVgZLjZIxEhJH0y57GunN8LZp544QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=q3ktt_NlaTFhEv6LfnRs5fDyJ24A0yUH3uqZ0lC7oSK1bR5rLPXWC84yRAbGfAiQvPYG0I891UWMCv5Eyb3YcwFwH1cDCLGlNeALZgMpwd1EvW_fm8AAPHIdMoZ_7KnYt4CsPzQSCaDX6Psnyjh6a68qpH3Tm6-r93DQztD3GLsimN26vhDDffjwfq4ZZaZzIw02vm95Y_Sjxh2TeOvl-x2RFN0ShmYjObnkLiaCYQ81G6DME6GYjVN4nHDcDwdFeOQ_zQnv2A5tup5IHFPzVmfaHOpCqXliyO85hjfPqd7aWAgnSPX_-f0QOVgZLjZIxEhJH0y57GunN8LZp544QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et5SPxGSstU9yMwrVUohOuD81Tge1cyhqLfD-JCNwI6tYnpmxFiZVluFmZlLnEQjv8tJX6YHfE1j130WMaqQ_GXyvoqr8ZM4DuKzJ6rKNBX67AuurZXPVEWm5c7_69krUYmsKxVefWk1HkRF_p2DUJ-xYQIrq1pR63R4_x4I5RCJCqwLrI0ifCvovyVEE6z3ZlEd_-9CJ89KConZV2E31vgErIFzeqG_r9Q4vYZrCFRQpMp_F65IC_S1hLtLPI3pNQ59JXHHzdwWGncnvo4QlLxSQOUeUb2b4_IwRw6Y1wASM_Ru5YVyzggyKZ3_FU-5wF6HUaf-mKnLtZ6FZ-wFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKaG3wp4jIHgoNe8Z0mBdwfhgK1PcMxDBadN4L6nVCJDIC7Cm1ScDRzKJGLOwcZvQbJz1-k3idjSO5PscoOSMRkuIMfTkE0zQdfwBD3-0XjdlLUMMkUsLiWa5VQEjtD8EWTUf8Ds2SQ81rT9ChyF__UsGokf_CXTsM3X8eFPYH4tvZnmgP_dNOdclsiRu4nPT6zbaMfCK9YmCST6YInd2Z8hrvvVlwfpjzvm7H6s_IsyhTkVx526RTNnKKb0Lo56ymMdL_y_n1bZeHZn82vJ-lU1v3iSn3zBUdQlQ5ri9t04xUuiBVxKf7okeOYA1MJZOaDeYeJ_89Cw7vf84zJWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raw_V3scxhgMPK32d3vGN8DsVKKfyzX5EA1fALNuAMj4i-AaJwXwHaYJz-idojoKf39tGkiRTznG_j9Sf6P8_XmzHP5Y0wxa0HaZ0qOQjEI2pXrY7gJ5YjTg3asqaKhg9Aujpac3iAYUOF8upa0ohqzEKxMPjS6AHQj6pm1Wf6LuMqwqrMlXsf4eBVrcxY7GON04DxE5f18JKKgit4l-QEjDhqXVjubUbTZhkQVR3-u7PVKyeMZumLBjM3ih7e_AHo8oQ10eC_1rVFl-6Yk3pt2bchQGIvepW8O2_RPP0-KsAN8vInLWlHl0Mf4_9QnoL7Qt-J3HwjbCspr5sXJAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHduZ07EsXMH3c_rzFibHXTYw585b3mgj8TUKEAYx1waD8gYr6Cyy8F6QeReSBLZprKcnl09Gx7T6pztj0m41K7FDFo-mYWZlJA6ECAFvc-6mdza9bW74eHxLSy4ch-jMLU05V1R2IIYqHs-sZzQCSINco6-YVD2PPpSUWTlacCdRVPf8xXCiKuCJQRYqtb5xMlqc3rp2U4KpNnbM-kSN2fLFW9ZxawYEEK14_Ki3AZl0IaJ3QCfoSwU_LasrPDW_d9niKPHb3DsUZXaYYACdsUnVBii4W03w8PQ1rdlNPBZ2AP7yXWqrE2Dr3MKM62o1c4tI5ieqVHzEJVM1x4_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhvUGUReSA2Icn4DCwdAKCHRn2JsEe5B6NVuoO8tlLwRP-unpp1MGDivSHFtjDz0W7-9UF-aE5g_gDx7987CPuGHhs2tjJiIYUCutuNmBtzhPw5DU7CxZNxj-2HvmQX3QbDugmrnR4EHjhh1Z3BwTloy8RsxL2L9lmAkDCTLLtio9nrh0E6Finj9tupOsies2uHOfGaWOzqUr2tCDOpi0HBj9y6B0Sy9LHxwLIGhzHDeOl7d0YTrFIwdUvenqyz8wdaZRc8jSb3AuEA87rZO2aNXzmxMvEEgiK1JhkA9sFKdz1L363kGUOoOQT4Mxcz6B_5JqtIflafgvbpNKPR7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzK9tjm8ijbpG3UGBlluBRWppm3mmrM9ij9b_VauIOhYD0gpNSoDbjB5ApRPQwEklaBPZGPj-HZ1fU0CFFNb7iQ9EYsL3V_Oh4sw-cTpZ6BL9-KTgJjrGHeSZQbavhzCP8nzZSW-i1MevaMuU_rLls-yr-2CAu6icIqyrlDu6C-CyZJg3ZAKmAAEJdpTlUgzpCAXqD_BW-MUDFGNlD7wMaojpEk3c4Q-z8KajAFYJn-ty7iwKYcB2OjMJHJKRaIZWfFr90JXooG4UlaceFXQxDX58G1bZ_v1CfQfG6G4No85VOc6VhFLR-HPtm_U16D6VlRFaQI-9LI8N6cOTBPz8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=vL_D0XeqzhxamSp4Ptk0dP-h0ihwgk3DTabnm3uJy6hCIE0uRf8TjdV4jcHQK5qGjcax4NwOxvIYHCiFpHpEw6ReummJd1_-Kcw6fYJlLyFjm7K1bim2L1FNeBsxXWp7Ys8TcTcI2Nb7DEL92OX58zLK1hYtrgz11hDOKyGSHjSsxhiOORvxHKxOJP8E3sc5pHkgXSlFnOYUXzgIZAKMnH_rWCE0Y0kcnDPanhi5XFo4zTgQeeyvGoyGmYBqG5YyRf_P2S81Sa04wIcJ4ULnfyBRXl0v1S2WH-wv5hCck1p17cYF7vnN_BskwC3lBuoAbqRhH9_njwwn7BIOJVc6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=vL_D0XeqzhxamSp4Ptk0dP-h0ihwgk3DTabnm3uJy6hCIE0uRf8TjdV4jcHQK5qGjcax4NwOxvIYHCiFpHpEw6ReummJd1_-Kcw6fYJlLyFjm7K1bim2L1FNeBsxXWp7Ys8TcTcI2Nb7DEL92OX58zLK1hYtrgz11hDOKyGSHjSsxhiOORvxHKxOJP8E3sc5pHkgXSlFnOYUXzgIZAKMnH_rWCE0Y0kcnDPanhi5XFo4zTgQeeyvGoyGmYBqG5YyRf_P2S81Sa04wIcJ4ULnfyBRXl0v1S2WH-wv5hCck1p17cYF7vnN_BskwC3lBuoAbqRhH9_njwwn7BIOJVc6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcevOrDPKtSbAQ7cHxSHRTzCm81mwmIHs7ZXl9f_GugWj619JQ0U429LbImiNh2DUklhUmTu-Y-WfXKKIRd1J_DiP0p3b-hScCzd2KWdB0aKkwXTQPMYCMvBoox2KSakr2Nu1CELlyC7ieLp03DBynNZj1WnaZetmQ2w1pRpd3bAdGTPsmQcX4TWWVHLrMV72hxYeq5M-DY2fx-Zw0HIsj__2MzFaDjOVP__kEQmK2PfFPyPTcpTg7u3NEbxcTZRV9CvB-uDbt8eeDnDIVT1OEN03n7hvItsY7Hiiig3bnmZnnw61i1yLNWWnw4NtH3LpwcA0iIbOxsKVVALA6mMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRSl7x7bo8zqZysfbyp0sHOYVG4O2JCxcopm4Y18JoTPhPyKFTR2AoCbfymcY__Fj8wSEC6u_w2XnWsrHGRX2cZ4Qhs3f8yt85WI1nl1d0Tkp3Sz8jRBjnyYVMKWHZSkIyhCtv3-CXXT3rXqVr3pt7alEKekl23Aen3PXnRUXFaMGgZujVTd5QALgBimfRnhlOSbSonqJ9sPpFgrHV8oha2aRRJ0Zy1y5EEIlFqCXSO2N2mCTeU6o5lUrLq-IhdMeoGyMQvthsIXAERvOSlGpcnzbIGs-p5I-DZmNYsWfFixchEtCBzD14ETipYRbBpp0fA65rCZnAXF89xpSoOLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-EmDcPCm8krPbH9f-nSX13fbeATy5w-yt-xnL-f0HkrsIamRlB4bBc8SzgbffaZyh_LPQ_Tn4l6V3cwHqxQvclbMj2DWcgtmWMG9-aYLSJhZQQ-_xItyIy8rm_H3t4_e5AeVjgkgpAelXLWh9UCHeMVR2LpKqw9OAgY1d53AArN3RRydHZtQIVNehCfru55zJKm3nOT9WyKFGvpFbfui0MaxRdtj9CdONMkfdlQf4270vc11JxHDoYtHc4tuBgPyVMe8ZLAH8oRpsEfnehiBzZFxz8GYLyj6pMmsTxyFZxyF1dTshKmSfYM9U8Cg4ivUjrgrEdiPgumVneG41muUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhqwdVP7f9epjtHbBWvFAFpB3aqept9TLqIwluw54_sohdRd2cxo-bqDJ6sUaI7kuvguC0Ol_OhUWdoXr7P8ZFBSLGZjCWeDZx4iJ5D_lzTlTX9zObBBSCe_PEd4V22KyV_IqbuEo4vX9jltFMymRzvlmxExGNnH0-sUShZxzMBspd3XkeOhTuMEHncFhWxOxoKb6IOC96podfB-K5w9BRrJC2iAzEPoOu8p_4__ji8LdcnBcx5U2Jp_uGItzP9pLCmV_aQsJWSBDSCfER9FA9fIN6kQWkVrRC-cagpj0BeAjj9CEDj9fd0lzhdCYXZQcfZ21j6hQnlw-mF0IWJW9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjhgvK8kvbb6JM22Y_Z_2vsexBlT29RCJndJ70dKo0i2qf-W2-dbgLMaMoyoifUk8VR-LVgLTH0UyKblvaI-XKG36gxQOnKR9R1VZi_zpoR2sgfmWmSWep547fv2lmW73M2DXCIoTNmUY6a-uDWa3N102AXMOyynAtXtsRIjoWd1ncpclzp2DFCTXQPfkRPhx8AMRT4JyxW8ZNpmYBFvi64vvt1YDEBhDZBfHonrWDjyQ5mp_tSe5cQhgkcI7Oclsk3YkMUOJB2SgB9LrkeC_0SFd3KVXXArYD1fJvg2Am2zjETIkoSHvXRA9hQIE3UgHjtOGW8fWJ1tCTh2TlS2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJ9vVu8EoXm-GXTXCptmzcGmHc9uCCkBIGqjAHiJ3sBHyvZyThnSjx8oKxnSV-hgGAH2WN0ksVW0PRTuSYgRcQQcTcT4WAmXAUYoD4WBRNIg2mVut9JCIwnc-c-Q8rphNXR-rQT-a02SUfHZS-ZMJYh5f9fKaCQSJ5H2Sa0S9c5G3JrzhmSNFgisKKfpBiXi27X_XbnXHKz3E-i8wxWYyrvJmQKK9kPsI2v9zyDEvslI1sci9GhGqiFi_11-2hLuU2Xitd8oEUc1s9rdhlPsol-pL5Ukx_YDKypaijG3mxwSUcvXPI47qPuVNL2sRXZaIvyfF-I8Hc6erxe_Jiu_3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=s_2tmMV4vwwVI_MSmpBAhCIoElQmxyDttXZhXyDaVw1kIkhtAUh4S_oaf1XiQCqYDbqANX-nixcheOxIi91DUcAJ5Dm6efnNqSbJzQS5NZhZ_Sqh8SK-ETpKSTiOUr9Vm4P4tOrednp_-8HHT4kk0OWiwhXW7XtbHT2h4Tz7XKlAPJGIjVbx4aSM2Qh18Rfgg8d_zz10cxcRAcQT2hfV1u9byYrbRUmsZSIlrwo3qud-Sh7a6tstOUQVrtdKrxlNqABqE3IvwylHcUHz3mlnCZyhpZzjcI2xmMAjXzV_BFi8rkYLTs321VcXxGSCrSDK9OyttTynSW_voPjVDNhZQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=s_2tmMV4vwwVI_MSmpBAhCIoElQmxyDttXZhXyDaVw1kIkhtAUh4S_oaf1XiQCqYDbqANX-nixcheOxIi91DUcAJ5Dm6efnNqSbJzQS5NZhZ_Sqh8SK-ETpKSTiOUr9Vm4P4tOrednp_-8HHT4kk0OWiwhXW7XtbHT2h4Tz7XKlAPJGIjVbx4aSM2Qh18Rfgg8d_zz10cxcRAcQT2hfV1u9byYrbRUmsZSIlrwo3qud-Sh7a6tstOUQVrtdKrxlNqABqE3IvwylHcUHz3mlnCZyhpZzjcI2xmMAjXzV_BFi8rkYLTs321VcXxGSCrSDK9OyttTynSW_voPjVDNhZQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=Xapxi2jt7sAliOLKXnl5ILozEfjM350vrgjAPtPoVdEi8EwN4dj4AjuPLVgQY788rw2169iQ7gZIEa-Z145narhdDmRI9ye_tsxaOnHKh2BQzpPChYQsQ1iv3x37g7RnSJQ2WPqVuZDN78F2-DBDDNyfPaUkors269wSElRAuwsGj8g-HULFPQcLSx8rPrOOfbHv5aZFs-sirc-hYWK3P8X9lqiI7TO26HhO5o_Wz-0FqX9Riwro9x76oFoR9BgVj8oAo6xwoiYXDI9GVl27ZS7WLF2G5uAtnitowcwQFmSp7kSCkTONH1lWn7mZ2lpqzj1_yH41kUQp6SORgeEWGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=Xapxi2jt7sAliOLKXnl5ILozEfjM350vrgjAPtPoVdEi8EwN4dj4AjuPLVgQY788rw2169iQ7gZIEa-Z145narhdDmRI9ye_tsxaOnHKh2BQzpPChYQsQ1iv3x37g7RnSJQ2WPqVuZDN78F2-DBDDNyfPaUkors269wSElRAuwsGj8g-HULFPQcLSx8rPrOOfbHv5aZFs-sirc-hYWK3P8X9lqiI7TO26HhO5o_Wz-0FqX9Riwro9x76oFoR9BgVj8oAo6xwoiYXDI9GVl27ZS7WLF2G5uAtnitowcwQFmSp7kSCkTONH1lWn7mZ2lpqzj1_yH41kUQp6SORgeEWGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24850">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B42rBsp0JGdN3eNIHIjf-4iCU0YjrLWXw8_Oh4zVW0U6mNxRU0uB2_ZjASmSA_gB9CPfaPJ15nMFe1Pqi6lG0robeF2cmCSMMYhcM2MIn0MuGNT6gY5oAMuTsxTlucBRJmcUuoh7oW4D6CcjCHd5X6caSRNk4skWGZVtlOfjKCRhfZqY41OEdSIKqESZvG8UAn8y4812_b17MlbuQSd_yLuHCd8Km2fJM7rDr6zL9Ql-ltk2MGEVBH16suyzn6U16bxaC-Obc_vTnBDb_R3lmy8XvkHnjfNGlDT0NmcXYrKudm2qFAYZojHEosXWDHaKa0ZGRTAk3uNJNc8am916NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🛍
ازاین‌لحظه‌به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r12
@betinjabet</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24850" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2ZaZdng9RmIdspCVJCk4pbwT_n9ppCw54Tse4KWzNThg1zcqHKZ2jj7SuCZpek7RMWGy5fuMxgs2wDcMaSTGeQ9RdZ-WKDiWV1QsCNSZUxUBaczUEcTmIAEB0np30Fkn-Ft4Kd616L9HCIStq7KoMv25WgosFBbmAaVR5hnolw-MeTy2SnMJAz7W1VFl1djLbSoo0HzlQ0Iyiu4TZjLUgEdBUvMDvoWsieK9o0TuAhVsukVNCrv_Fh6lGrzLcEaC9UsJrxdfazuNJUUcLO65BiDDtaTVkC4Jl5IN0j8RhaPfE7vPQi4F1X-u4FuuOrrMo86eRYA3nVV24LU4_WEeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTMdpmrWcarX-J6fbnfzJo7x0Hy7R2_UedNifoWoXvodDsIm6l3y2afKJYah_IaTcokT0RUKgl8p7xobZceRPKwlr9_3DxZ5xG79TDcPKwfKT-lZAhhdFCCvsk8nuMetfJlCH3YEwxLI8L5j7-S3-syFIyYJsK18R7QdXJtk-UjNyE4_FAdat-MF6JHwoJ8LEcsT_Dvut_uduhTgoRwSEubTVD1MZThtqi8xq7cT84ne2mnDNqS2MBtu0_ivGqXbeoeY8Dhetn3kDmIUxpWxbuRjSkgCBCkCOwYfoGWoX6_mYMLpvEh_bkgAFlZ3_Fqr1PrDnvgZrllEslQLgN7VVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUSdhh3JDaeDpY7rR33BKpl-TYwME5byAhgmVP4_6toUeZLf1rJ1furMrE9DApEcO2BLFgXc0d-wJRLtjSirTxme9Z2fktPg37-n45QC-Z-26XQIVa8Qgc--Bizx5HsKseLR09WMjs3UJJJivosRAK_GH1S8xytAD1Kau2AT_RSElBqdZxL73Pf2lcilZIO1tngl42rpMs00-zNCPzT8Nqbt1KI2sQEvf87COUUREh1zRXdh1MSqywhg9NUQdAFn0XbVyyY7DSprohwmhd-pqDV3RZrpgUgvXEIU7PWSuot62LXfbJKDEuRtuErAGTywnKDBBYXIx-EUw54uf9s6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZJH_DdQV4R3BEI8f_1c4yrnsa5qB31rX1HyE7fkniEJQ6fQKlrbE_TaFIREJ30Qz0r2Y7d5dWByGLkLqJQoylJ_FgBpRQSnmI6bEhGrVT1O7mgYHJ6dz8WwIYwDfjEpqkcIPdafPfAvgRdnEoLzpypdikcT-sL6vo-mtPOrYDJ48rJtJCtrr_LHPO2iivrlvARE23qmWF7Hi4JacLowz0mnDW9_Qp1d60vRaVD1v62rFJReWKhbNqAt9R8v9yEO2ERZ1Gnx18XxJNghro0MB_V5-bbMAun74lT2_W3wFpYg5VCO2WWQeRWALRkVhL2VVTBvOHB3ZLv-9KdOI4cu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrAkjQkc1xnMoRK-767r087oonlAHmBLSkN5vdbwByMspZ8OWXrbokIGWpk0OvkkNxBlxR0nVIoLhMRcjoSjxeqg9y07vOwbNE9EC1pxZ8Y1_92WjAy9pyhiAJhUxo9URbBdn__rXkmnIenZkgnC27_OdTeuD3QEEA3qJX8OYVxX2L5uaeM4YGEhx_QXC73yNkas4TWmTl7tCKM7aLdEDZyd6f4CvOxmoxU5oLR3dBIwGwigZi8e-ENqq7ACJBjECyHuUuf5PYEHI6q7ly7dBw_3BwMN3atLbZ06Xif7IJrD_Pl8BVLsVsTTRe-JsirrP9OPyZHSrJe61G3zElCQPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24844" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr7U3ar2gEYMgYUr2F_9mu8gby5XQlnE4KRXeS3XnOniyMt0_Hj-JIc649u7A8GgPtN_joEn1GkFkeo3EvdhD83iFSIRu3RKwajk7WI4TMNqeFfjNR8Mdm10M8K_WWbmFb4Hqdozhed1P_VA-ykY3h5SysRck9gl8Tzf0FouCImGlh7lxZUb7vOSr9HEJmP1AV_K05hxPjZMvuFio4p28eFSkUzOwgAPyTsogZQ2v76v-m7cRO_sedEwHaeLr5AuUfQphQjQjDgZzrsG_lyG2pE1RuNF4x9HuHSmfeM7S5_faskIS4x2SWSW85IRyRbWGK1oiJTdO6du_EzQUc4bCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ku2XTwix42_TjCTvUnI7Ju2G1ygIp4XpIxWkU5VpgJ1u--Lxggl8F_MJE68ucx3NRsNTni1vpiCtBqRbce7sf89-uc0ZnbWOkUhkjx9Gl0l7wqLOi1kP0r54lc7E4pL3dVg-RPfDVEDO8snlM1UlRoHF6nT_mU9xwjOUdoeqVtPrbtgryXO0hVDn_9AZoOGMpyqxgVlp3UPJ5D60jzRoXcUOXufY7oi6YMgyhtaX-JZXOdzO-ipSKBpn-OUFY5zGoUQivRapqsz7657valSi3Zt08HQbj7siSTBHq3WJHEcY8E3WxERc1FZ5rKM0s15TITRISr4l9Hpl2gg9jhXaWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtSxbUQ-meSF_bH3itxDgpvw_R-ToM2lS3cOOeUHQUalVKH2nM-zFGf2JC_jeBKgMo6l4fuh2hELjPwR6L2luSxdzQdyM8RZuL-Iet9yWtd3hEPpt9Qn38giyv84-IYv2t8jFBRal2QcE7keyRPLRlk43KLpjuRThiWfsRYdLCC3lx7CY4-dZGSsMAVligMLMN9ARCf-KWiHu3Kj2qQKcBpgTrsMhAY0dcewMQFqao1fBIQWlTXE0afUtnGFQW7S4X0AvsddDFRU10DbDPGyiUzxomdIbAOPkuVbG8ckJqGAnYdhcmXl1TkqKqhDaYTQhrPXO-NZthyL0V4utA33-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9aJOKxkyaAE3wfDu9a9BW2q0vbgyiPK28ztl5MbL8V6RPpiKkiIeC-NFJQhl7Ns1L88g4rHO7AJSeudsPL7_bN0-L0i4xRvgL_qqlPdKlcX_JIpspdMy7tqgDqSY3e94_ysUw189froB_maZ1g5udjhvja8p5wNFm6I1uTOK4mfmP7ZEZpqUZdZFyMDJEKu2_PmMDQgXrSnJU0EcJuDtp1aA35W5NRxoUYAlETa4yS0ljrVMJCbfG5zpxqQLUvSl5zkDXhwB1Nwh9XAJMHixihaKwPrgC99gKhbZMor62LqrRXY8UEAKCobDWVsoqUAWoH8A2dGs_tl6hDkT52SMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h98c0N1U-BPREkGUMSAvuqbwHKEJZhICJMkKEoAuWLMZqfP1k09ErIKx4m3IlXOJbf2PIrjTXt-9ApR6R8hMnkPxqZCCuzIy36T7rp8EnzcyNJHwRWFjRdnB2rfyMSdCgkJBpMJwjyZKWKS8ef4TJPvQUUlfEF7OW-ZZyYnnwQsgZ_v5JYRGZxoOy2EJPx4KWtIKTqc8SUH4VMvAbCV3fJJ69Fwgy-gXDEUl6iqy83_F2slG8OoI_40_cOz6qNTO61XLYLEWsdD2OOxHjTSgRtnpyiBPO0ElYcQGja8qK4MLmJIfXKQNKrnxGVtQx_PtvKiBiQaqvuodGKURT93ubQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام
‌
جهانی
؛شماتیک ترکیب دو تیم ملی پرتغال
🆚
کرواسی؛ ساعت 02:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTBNSlZix0JCtfQnWUyihfJ8d5ohXT_LGts8ByV6liAZkbNEycP_utMQovg3SE1Ffxa5JufLMLqyhJwcG-N9TgHsRlIUm00gbm5TEXxzEy9-r_e2xVIWCqV5vPhcKNp05d0r1wEzwjbG6krLAmmMxq3TBwnkiYd4bPexTsiP24NfnO11SNc94n6Mc4PTvsKyL7Fku_3wxVgrt1ZfVqFLfGW5G1sIvKOVkSHdIUDs7RHrdf6_UbjViMA5IvM4GwjZNu6xhAVqJeEMqKWVGGFzt12qOmQunDXsGS8U2L1o5cK2hkqMgYeYuJdlPU_8BYGhgBanIDzMyynLvuc6TD-85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTNKNyJ72nvMBh6G8lJeUSJGJc-8briM_qn_8GqhkaB9wqGp_YA1TjtBTzlowrB-8sZ31jqsuUayX_DJnlqhAoF9my2mzttmupwSlPHb2dQNVpt9-AhWf6KZd7DNLCTjwjPK0CT4oK2dIw1YpaLMrtGcbWIA6tXrMdE-j8NaNw4Wh-p2ushU4GXIvqMTvjoOzDV2cWFrParNzuB-z9qpfAFo8woIpSxMOBaU_uw2fGwoqyBSajiYnXXfaV4dlPZx8Gb34g6QDNDD8Bwa9rKkvMfjXDPPzMMb3bCE4qbR1mGxfk76IKGKX3hBySNha_5Li9EMHgfdGNHMO7J5X1PwKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد فوق‌العاده حساس و تماشایی یاران رونالدو
🆚
مودریچ در تورنتو
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijg8zwwrdJRTWUKVIBqQbdebw8UXEY3OsZ56eYKvvU8Z95iLF0peOB00MIf7rrvN6CVgQwuG1IfvA8sfO-6wp1p3rq35MMlb5NpqaUgEh3YYD1j6HrKA0xRpKx7XCGZedpEuaOkizHWcpV6f7rcvkxNrjUuqrJJoIFkDkbj2lAAD-630lyzFkTfWl2PAdL7ej2H1Qlb0rzSJHC1aKTmmchwUEzPz3WurpmKS466BvARLwZN19ge9RENfuAmxGwDAxU_uh-ewnX-v5wpuJBBbSLmG4Zjg1zq31sjmM4eG7CsSedUhCbeU0Dt13-BCfxSF1wTjYQEeTv11QVhiPC5FPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IcD9V6nMMthky_HFcnPlaqHx7EsS3mNLtNjKmRnlU39CFxZZ1_H6VhxNjWUB6fsLUep78YzPSVo8t-mbxiZiKrThs_zbePswaNB6nhzaddfNvIx9sXOKp4alaBSwsPcUmSD994HqpZpM0kj_cfvt96LaYz75QoeRlU5VVtJlfWiVCR5NfT3t5T5N-2T56U7vshEEpMwzGswHHzULBjYq9ziOFdAIvMFj7BE7twGUjJy9cuO2EaAbC3gReJaYEZsWFOZfqNwrUsaVNSud-GlCc0e8939rmYjoAEBFRY8OKBLbLsha2w2GKlZCB9-KiP9ZCrUm-qGYVplYyNIeZKa3rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IcD9V6nMMthky_HFcnPlaqHx7EsS3mNLtNjKmRnlU39CFxZZ1_H6VhxNjWUB6fsLUep78YzPSVo8t-mbxiZiKrThs_zbePswaNB6nhzaddfNvIx9sXOKp4alaBSwsPcUmSD994HqpZpM0kj_cfvt96LaYz75QoeRlU5VVtJlfWiVCR5NfT3t5T5N-2T56U7vshEEpMwzGswHHzULBjYq9ziOFdAIvMFj7BE7twGUjJy9cuO2EaAbC3gReJaYEZsWFOZfqNwrUsaVNSud-GlCc0e8939rmYjoAEBFRY8OKBLbLsha2w2GKlZCB9-KiP9ZCrUm-qGYVplYyNIeZKa3rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌باشگاه‌تراکتور؛خدادادعزیزی همچنان به فعالیت خود به‌عنوان مدیرتیم ادامه می‌دهد. عزیزی بعداز عدم‌آسیایی شدن پرسپولیس از حضور در این تیم خودداری کرد و قید توافق با سرخ ها رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIcuU1L4O5crRkuScAOFdtSuDSw1Ak2Fh4jv_CUXpF5OHpbSd01KHgiIt5Vv9QQA5PemmX-cXVW8z_eIsHQ9ad596apfsjZR3SYbZCvywdKGqnIWnuF2bsKkNxvf05bF24lc6ZKDE3yzKwWr4oYUnzKE2TLEp0-l8NRZgXoib7TAW4gePUU4RCBF_Cu4f4lJxru6Eo0nTTGpC10iAkmoqUPSbShPyV8-irpAq7KELGYzI3mJIR-oUame8Cjq6gRYUzczR7tlOspceMId-0KA60JgJz2SsCSyWtEHZjzuz8i7VXDYFHW9JFuMzaEBZhyI-xyWX_Sh1MO_tnfhSfR4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGICK7zHj2P7kIPWM9jQqQ10YSkzjNIfAC3ZhSr1kttg5Lp7zEjCcRvw4iEiDodq2DH9obBN-Eomits9zevguKrTnplB0_3KwKxylcJBfcHBgoPPEeQTl4ySXJPbiEq0EVJdkx_8Bz9uNwmkYo1MoySri7nqS306WhE7TbZzwpiCp9LiPvyH1ig_0aCwgt-It2ckOhXtlN1XKVA1-YtgXTAgR735Gd6_yBxFMMkG_nZE_u9pNFdbzs4xVOs1XDvG47BQ4uC9rUjTNanSAd8w3x-qjufydRigBuX3gxmId4XyxPc1zyCN7ktTmUvPnEQ9HnDc3k3yaSBSgPJGI5xNKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXnBcJGnelOGdz_nnVwMZqQfChHIv6bnDlQNQlKSFOvvLnm9OeBePQB4bf8RRcd8wgLRPBWq5c138qsAqdLPGu_H89G0jCITfV-svpHjT_xNwqvedkxiYW9DA1Ag-cvzWEUl172Y4ZC8SHGBqt3S747jMe_U75FAis8yZjtofLTD-aS-lMyJZTm4Cbc8E2U14NNkdea5aFGUGhZWK1r_I9TJZ5m0lR7JOEP8ZFdIf5ZDr6jZXiVTc5vDYLujzbJ5TmFxgEGq3VfnUxuh414VxzBs45VIBPYxfuc0c2x1ftkzvy588EbHXeavHWmgFQh2hf2xQHI6rmZItuvqkvL07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=Z1ldoiR5OgQtY4Hp_wBcn6q7QXCCpRwmeKV2aU5z4xlaGog8S61ukfOLKUN99IJDsntCQkkvtf5jg17Zw-eoKzZlf6S7rz_MZyB0rICUz0EqlWcezR-kBAVMdrTAPDruMhhCws4TmapIP372sq6MPjB_JZ5A-DGlSVX5AFv8DAIXzCQS_gZV-lLajQvyZUEkq4sfcsbWAxHNkYn3gr1TKo5VhF4Wyf0TWtEEXmOvdmO25r0XoOHotVpYmsfDfoC3TxKdpbcE2et6EpohLyrKjowyj0PW_ice8ymuVvnozyxky8kuIfa4IqoorOrEeQnR8kqpzedSxEtFEq0UxHDa6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=Z1ldoiR5OgQtY4Hp_wBcn6q7QXCCpRwmeKV2aU5z4xlaGog8S61ukfOLKUN99IJDsntCQkkvtf5jg17Zw-eoKzZlf6S7rz_MZyB0rICUz0EqlWcezR-kBAVMdrTAPDruMhhCws4TmapIP372sq6MPjB_JZ5A-DGlSVX5AFv8DAIXzCQS_gZV-lLajQvyZUEkq4sfcsbWAxHNkYn3gr1TKo5VhF4Wyf0TWtEEXmOvdmO25r0XoOHotVpYmsfDfoC3TxKdpbcE2et6EpohLyrKjowyj0PW_ice8ymuVvnozyxky8kuIfa4IqoorOrEeQnR8kqpzedSxEtFEq0UxHDa6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رونمایی‌از قانونی‌جدید درمستطیل سبز بنام "قانون شجاع" که توسط ابوطالب تصویب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdNEcI4-2a0FBG4ZiFtnWW7Nkt4bhNWNb5fBcL8csYQFBBiysZe3L86VcYAPopdxEbTIQpFD6185MW1MgoqCQAjgX2-R_BXFKowJCflwXIn3uvDSGaI9HHJMNSq8kG6KuuVtf2GQHftYWuatdkXFvcvsC8-W5KeJ8XCnHZLJVKMyeadE4VsHe4IZR_IJFElUxwmpre1YZ5YveD1p47u7SwJK4v7qiB7l_9eqYJrMOmFJgn404BDZAyOVLzXmN6bDbSMYBJJ8_PkWim4viHCgiR9kn-Hgl-rdhasIrCAqcqLpoIlKnAnx57yi4zlk7kju5OiEMtlEFGqCR_7s6dKIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=j7WpER2sDPr58Gh9B4YVNLCSQAy_bYiomDh1G23OEia72h9d_5VYAUP6nSY1vIZHCePJDztSPU-_FaVL9T9rM73oNX56p1LiSERZ0YEdmPvnipaPR0KFtBocdvAkzDdaFFuq9ZTcfba2BzbmqhkjZ0UfKo1314nDAY6KZysJjhSRGtIivkVjjv_LAMYXCd-VZQvtrBQUfAsnfJ6VaFOEaF66dfv15Pu5SXTTtLubCEadRavDlM7iOVoezCrN3TvVo-sAGpV1FwKfCqkWkzZuDmZo7UQ_VwLsd6FCRDZMR84FBd5xxvms7knhGJ1aD33hh11EP-hzxliJ6HxycJr3yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=j7WpER2sDPr58Gh9B4YVNLCSQAy_bYiomDh1G23OEia72h9d_5VYAUP6nSY1vIZHCePJDztSPU-_FaVL9T9rM73oNX56p1LiSERZ0YEdmPvnipaPR0KFtBocdvAkzDdaFFuq9ZTcfba2BzbmqhkjZ0UfKo1314nDAY6KZysJjhSRGtIivkVjjv_LAMYXCd-VZQvtrBQUfAsnfJ6VaFOEaF66dfv15Pu5SXTTtLubCEadRavDlM7iOVoezCrN3TvVo-sAGpV1FwKfCqkWkzZuDmZo7UQ_VwLsd6FCRDZMR84FBd5xxvms7knhGJ1aD33hh11EP-hzxliJ6HxycJr3yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره کریستیانو رونالدو در یورو 2016: از برد مقابل کرواسی خوشحالم، اما چون برادرم لوکا مودریچ گریه می‌کرد، نتوانستم جشن بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQgn6uuoWYdh5RBc1UBCT__RyC2TOumXo5jVY3UO7etlh1deDtHU_IyfJ3_hM9h7LQHKUfIdlLGQW59QCnPlrwJs-iPvl9vUyuPQZa3mviwsDZd1SRNY-m3MqN1zeGLYI7I_YSz46Cb4EqCA0adVLyk-yG0ugQ59jt1ONR_1Cww_1B-4juoJLacQkJMSbdpVeruaAcT0CgBEFfob-8Powrk-TgSmrf_0k6mDkRzQJ25d_d3D3-uxiuvNLvI6VbrMQNW9zkoSnzpJBc5h3o227JkwlmL-sC2X553Aaq6VA3JF3O2tkqW2kX0jj4OCc28KCJYAvfUZzaUPBA7VT3YLbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YC0ARqyvfJB4PMB2sL2Oqh2o4NZkzoi5NrNwCY3KZGZ-FZWH5_D6RCmKVXzLfN2D5k0vVVVHm1G3lOL6MM-6XiEEQh_iRM7bDrbvGfr-oxGZUjbEHjXBdHRmuF1eWI7pRMsrIlkW30EZK8mE64G5kIqlMfF7tCmrtPRlWn3df4m3ep5JwLmIyAYIYgOuL8RfsCNVDmufPi9xaipXuzcXQdHTC2ccfpHlP2haO5n3bkWgSthtEHsNLG7k_DyIOFb3A-01qimuQ3UswhZvaytsa4fMiJMnsJlB7n3uHOQCewBEvAo-3RsnttJheX7nq-26QeWu6cPlQsPrUOoXQGaxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8glo_Jlj5ehxXjsWXcIr_JzM0n5G8_MpWt-4xO7imSEfsEdGXYeP2WIJa7KY-VbdjOnlO37Uvaa3KF9krQYgukRtvEscIPeMKlqkhV-ZXKGvCNw6lxFbU_TKByvRFE-BD5_B6EiU8OzUIfi9EPU6LA1oKe9cEOzlPyFsMb8P3hR-I5Tu5xVxH785ItOCMepRPQDgn73hSoFdkwyKVWiiPYYYoGYkUipcZzER1AcJfBKhZiy8TEl4rR38ditL9x0OciCzUAt0U9ZVC5v1VGtB2c_5Ya5ZEG87zbnEkfKZ4omXJ7UPY3OFucaxf69C0hsfwo_yA42s7PBAt_0YJJ4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24821">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vmm1NZSc1wU-udqtAtPI8SLf7iPg9iQKoA-wx6B6HSQCcT1GNx7DQtNsK5-S00F6uEnE8QJ_u1ZLpUU2UCKCrD6nLm6Hvq7fc2VIbmGpV-PtOvtFuY1Itda0szcLwfwo-N5RYgmYG_F04tKsCtPEaQ3VNaG0-1psCEByOta9Mzd7fKqG_iSPkitN76S3GxUx4jgubFR-JJJ_dIKNWo96Uk4Ik3I3BIvZj1Spe35ccpZzj2ta4hclP__JOgCMx2BHDWhKp7FLwRwmRsetx0RS7CCaTKuvLOW8drS19UbeMzmyyKOUJgSpzPMxuSqvzdVz45qQPKew0GWOQqIi23PwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24821" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG6Yv0a-cMWU4rndYIhsdrukQPToCQKDD-W9aYqKmuTSg-fVZ46JRzuaiNxIr5KSeonzCfhkQRLG2B0yE3r6uyApg3KLZbR8mj28_K-cl732Hg0hxHZA_GJDPGj5-kmgEOkgx-UpKwUR--HYEb9Hu9sEBcC72bkK1Q6pH0Kod12w_APSw5iamkd1AFGT_itgbk4yRXwe5cHshgihfexKqOpg4EMunIh6UZVkzA7-2O4lkVejxeICM1AU9OYwbzBWq3ImR8HPOw2RW8Tq04sC3oySDTWG9GqY0beYA2JZ_bZTjbmTTDaGZNLm6dHYoDdRuRv2iTQ8RFB2zCho5HZOeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1xt3dFLpJdOY0hpi3hxlLukWKv64bcDmGDRKax_t_AKTRCscs5RgD3sqL55j3IQ88qQHLf3Ni6eN7CpFcvNxRjpkI8Ta65p6GZKGjHX_EgjI2Ted9EC-6tx2Vda3jXkCXZzXFcJe55QuXxsrYBnoso8i2vdiiCdZZfY1FlG7rK8PwrfdzUnarrXUONgKNRD06-7h3SLSo_UxdBEpsBlUVGuh3dAXSZxl9PPYomo7_Z64S7MMtLYhgiKQDnkoaMc7kHWUlkT-acD39nq6RW_yqHijQQ_5NczQOpr6_RjUcR5zTX7itc3bxWYC4VtYM0Z_zRtPivzA0h5bmbU7_Gy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-b0vUEFsvTjp-8iPoGG6rfqN4dQkQa1Gj-j4Q9Fza__LNXkqu5jJLD1B8ouywZL_VDjMVycD2v3LUlbVt3VUwHjnErFhh0RuraT7zKNFBJGLg84Yeat-wVoApERwRfjog3jakmb5a-VgYpB3WCXuX40s-FJWjBpzHR-jZG_5cito8NmDLV9YT54scoZ_HWE_mn9_rASlJXR9-y3VR3gfRBT6gFcH1Ll_b4tFZBW4ZqtGbIu-mI3gXbnMOVvXIUSt51lQErb3ff9HUDMKwHYlnArM4xbw2J6z9lhiM6gSi-8pTOzvADnwtQb0iw8nfcwZ-r0BUelmzuJVUc3Hjx4Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSLqJZfQw8_6dw4aw_f52OeNaNauMij_dpuYXI_Tyz_N5PmkdQ_FrU16pKDAEed0AKihyBfpIs7CevHUvcggGwhG-QwWtovrE9NXn4xapE7YUGaOQyFmJ2-7mfAtlug-6W8UCd0TFdty8fIFY4BL9JaBwvMeesKXkntdNLjKzCjf7aELDFmEYTCI-7KRpb8tqUQRT-nKe3Lhpruj_IYpWba1TTQkbzNF_fex7_R-5WJ77B5cq-UDzSFbfmMWy5eoUKWRD7k2ZB57ShsXxkzFnxGXNemFgvJoO2JnbiWBAJmrtK4JJ2on2Rl_CL-Wn70ZQSbuuRkZcwOEr76AvHr3iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLpZ7AhzTLYZ4tw9x_sZL9pzlTox9wdCecrxuQ9BTCH9q5w7fRS_2azdnIRZZ4n3FpG7wd9QQ2LsmS3bRzt2APGXRO_d0X3XPKXgo7UFn3X4xQhS70e44zFXQbvdz1yxnXGb9cLvsr0-JLvYdx6ziP3Z-c_IcQCvaiciMEsQN8khwAbaIh1SNZR0y8c9hRtdg0jsT4EehE6ogjELOdmq7MkfjuP_gkQCXO5pMC6jEKa7VyYGGXDLu2rO5S12L8fDHbFjKC_TV28oDs1mv1IsY1YzfKAcBsX8qfbcQ2WfgfbDP2pOj9ashOu2GBLlHrFwgtbjSByz4VIUtGcWO943VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVv0BC--Bu-aD8RqON7t1KMOpBOrbieRAYM37DltO93-5mcHDWYwQf9F6mjwX4Ul-7YabsWBNRBPWG4MocVfLwJL9c9WuMtfjbW5PdTkoaEQ54wXV3LWZlbtMTyVnz6PdGdyMbC5axzAXym_R4rRwrb0RO08KwQ1T6gJ5RDgRoncNghcGi-IUiMZd9ILG9LDL_OTYQQfpyIaNM415dAaWXjJikBGbXzL9CkoULqMye9Reb-DDmHerJx9yOtbJTa60bMx87tuPI5yNYL0OvovPC32igq0faSpFi_n2Ln0AyhKDv9ru33c_c_W8d7w7kwrwqjxA2iQUhrnUfYS1VLoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhOZwRgAD237k9JB5rB_0ESLFUCzI27U9RnQYBmATS2o-k_igX_4la61mAaoda7z84cg5jU7_JfGk9fqzhTxyChSu6gjHTQy9DskUR4TNlrBeq1wNO9LIyRAOqCAuO2-AVRsISalAfU1rfJXAxy7rwryJc9RWSNM2aczmAIR_hthta9MhqmKHF3Ik9_hizvuen2-XmmlsRKaAF97RUQpIX7D3ZoUKmJwmyrd4MflJYlqiTcmhbD1FOT8-tZ0yLV8_n7MV5GwD9z44-kTp1MtL7mORblapbjw-0bnjHRUc7EqY9vjaVqoQDfn1x3rId8gkWjQDEn4Wg9VN0Gu85fPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTemrAHHIKHE5EhIa_4eSPMwe_PubsbIR_Cy4RDVWcovjTiMv-8UdsMc_SEbiZZpqF_rjrbWDY8BPQOgidSaWUlnsgkUh81d24SVz0MkeoXDYDXwaS9vJGFHWzbvVFJISn3vzV9KutII0k9k5mhloUYP2VppDaJzyXMLXA96XHR-P6eih9sXQ_0iovjxkRND_po8-zuhhttN9dPau0wwxjSi4PW1q50OfGAcQfYH0TNWhVq6cd4c1KuJWcmxAZw--aZLsd25A8PtqLjlBrDotqn7CJwtnWBCmmI0ErbYQLH0aKbDeHkVknuLvKwTRVFL1lskC8LgPMPotNPtjTf94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW0uRRyDJpaBiaaUk-BhNeRLA6Y6Crtbmv-RGvbfck-S19HhiIIB--evoDNCItyXzx_BoNfLaPooc9k_xAj2BzJQlWkOAMFBRLqH3oVj5lpvXyUsftM7sCFo1rAK8ledQOcvz1Fer7-yLIY578sKsvE99N-2lgGY_4l2EZGFa3OOhwBhQOP-V-agov4HV4jeSwHpNZ0xKX_V3pvVICdnN0U9zq4aOTIwioYlrztfx3GsY-P2txr64S1iS9uhhEdvzZC1YaWwlPSdI0AkfE1HTfjkQWLmqRKtC4EOG0w7drr5NhCLauNzHY-bAGLZrc2lEwGkAGtBu1SBNuj9eKBN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9GpTKJa8_gwvSQU18IYI8OGRug6K75SUK3e8h2kAHMFaht7kKKk8pmSW9ZNUOHkXpygHlbzxM8GZbCyK3Ax9nk3zwLwK-iD9hvdhY6vBX8rIwHiOE3Zt7_h42tAYPrpGVznPYCPsyjDT135FW0kY7LsD6iEeRkOidhHIbAuWNqj4iLdpx-H243eC3665fO-U6p5qbPX4Q93kS3lTgk_AwfcQ2dyypg72-ZYwzU7GDNRCj_5VhpV5QUPtX-XbeZGuKn2rMpsjGN_DfgeTl89IYHYz8iu5b83556xMfnJlSBneEqg-4TRnV0dpLjRgWeht_Fbegf9knKRIc35Hy7Vog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrU1X2HahUZ-79qx_l3BUAvjNqqLZayOO4I7hDHNdERFGlEHDJV6vx79M3gIUWLdjoMlJP4-k0h8Q-gWq3vKKwVSnjmo0GDN2hCFutfexIvl1vu3PVxQ852T5jyj_Hwl2m3s2Ydti_liRUoAks9LzBHAt0wsR2TnX4O3XsngxCiT74J9FTVprLYOCIXzfFD2OhcsD1uaoSCFLWeeuAG-uohA0mJz8sH6Dk2PbFoYn1jRW1LBzbkaWsMnQDvvOj1nOA2sZ1e5Syx0fF6rP_r30RvH2sLBwQ7exKxGMB71LFWhdPNnTVUQU1bsAnMUaoFEaEcvmrDxdx6mezZLVoP97A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4RwzcJnU6gUX43cy-P1Mk5VZP-yThHWHnQMTyBimXnp_IA9dWaGDDcvkJtp_SYtgzxGTJujzwgj5YanyaiAsxP3Wb4cLssAmK-7l-hHTDLWxZrOG-oaSptDR6Nue5Br1gI_5NAVQnH2x_iw0Y5WbY3OUyX-lujFFZYqCPkjz2btBB5w5oplFfqtfGxRrgxGdYl3fmZkLqPK2kOYFV_egdxdT-GD5I1GPkBUjkBpfsIl88e1W1P2Lad1z_JAtTIWlMFwvwAU3twHWUPd54CMTGR0arROceC4YXTnbMXFpZF46W5rFPzgmjMCdf_xJlk-lIWcYP8cyakbmhPlimkegg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VcPkcZqs2TLaMWIxYCF17KBMEXnWHBU-eJ6zfX9mJtoh7K6UVGvOh8hHjauEcJ98Un_yS_zPqO13E-4TqgLYnhHPS4yE0QaZc0sxSzKxoo7yPrgc4k8XSLqpqufNqlg86PxrW5N3y-nhtxvRrxL6oASFfMsWhg420qpzA3FrJT4xF2V6CfqI651EPmpb30TB4RuhHktycFQWDt7oRoYtaqh1tcNTBlEJTrtxMn9BLjgW-cuHoDDDbdxXZZjNMzoWTnKe-dtlLhzMXvcKsI1sgPdKXjLNlSqEHPsm3m3VJ_-Q7atfnkE0bmJWV0W-v7qC2uLhnOI1Jg5hQAWoy3n8_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=G0rZBGmTq50cDXZKPseso0LtQOjMiXSKzNElp8-GlzIsE9VWL-8JaAzLsqTUVoBtp6sbyoLCQVrKDCH-nnGRd7ziuUmXRaKIjjFgfIe8fTCcnEd0JJordMdcYcw7s-uV1ohYJJi7Hhn2W4bSmKgWXrYXCq2stiV3tbZAx0izB5BPJRczy6aXwfSC46dqiBpufbEYiKjuSSBt4DI4RHjfyT41DpoMVrv_ScablQskESEys9kYWwVCGC8ixs6nksXdEPlUixqT6nmxQN41PO8YdhXzYJZuSM5rtDM7jASAECmQ9TZd_8qDnNm4L5ezsG_uXPSiacU-_cKGvziDtX0n0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=G0rZBGmTq50cDXZKPseso0LtQOjMiXSKzNElp8-GlzIsE9VWL-8JaAzLsqTUVoBtp6sbyoLCQVrKDCH-nnGRd7ziuUmXRaKIjjFgfIe8fTCcnEd0JJordMdcYcw7s-uV1ohYJJi7Hhn2W4bSmKgWXrYXCq2stiV3tbZAx0izB5BPJRczy6aXwfSC46dqiBpufbEYiKjuSSBt4DI4RHjfyT41DpoMVrv_ScablQskESEys9kYWwVCGC8ixs6nksXdEPlUixqT6nmxQN41PO8YdhXzYJZuSM5rtDM7jASAECmQ9TZd_8qDnNm4L5ezsG_uXPSiacU-_cKGvziDtX0n0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC0TbDd6mJ14e8F0X8hXAVndU9SY56eOXJeIXZCPDHAeXARaGOvv-r4xl2JAyMt9VIMxzGek6Y4hTeTTEjYaWnfELW1t2ufHXxjIkrVS1xR0wMKomh7fvyp3xuWVP-oBXC59R87QiIpEoyOfu7uwfXB2DXXBSKmvKQv0GGkzwWT6xjmGFqyYPBbQsRgN6f-S3cEk4kpQmAgC-ruXAAdXKodGSLQyRrjnztHyaqyZIWUk9vyByNc35nBeedjHbNZOE-jUsov4zd_WC_xc2w2WPADEJznUu-LL4p1EpXdilUxLbbagAcdArHoH93UnfgyNt4cgRvavDyQ3ugKlmtvs_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=mnyhhUNLghtCd7pWHOre3tBkZmuZ_mRT4MiJGqk0qQLEJrMcTL_UHvSGnO1V2pRSwo0_lUI9pyhLJsgfB3heAn_UMezRskJyLKBrvgqIwdBT9tExy7xmRdLHWg5sCGh-Ryjhpn8Ooies_gI0wqkuWhZCf9W_SdnRa_b4mEFHhpBluyI3EosIXqRJiZVDLBLo23mJx4PlYN9SIFdMrYN1CfKJh3_w-64Tk3gbUiXh29ryUFsnyGbDpVy5vJgTOnU7UAFyct9SX94fz9m-7oZDX2wK6DEEXtz1m--oolkwQHH23FhkUjJD4Yiij2txSVpBEO38XBPAR3aXd1RPfr6t_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=mnyhhUNLghtCd7pWHOre3tBkZmuZ_mRT4MiJGqk0qQLEJrMcTL_UHvSGnO1V2pRSwo0_lUI9pyhLJsgfB3heAn_UMezRskJyLKBrvgqIwdBT9tExy7xmRdLHWg5sCGh-Ryjhpn8Ooies_gI0wqkuWhZCf9W_SdnRa_b4mEFHhpBluyI3EosIXqRJiZVDLBLo23mJx4PlYN9SIFdMrYN1CfKJh3_w-64Tk3gbUiXh29ryUFsnyGbDpVy5vJgTOnU7UAFyct9SX94fz9m-7oZDX2wK6DEEXtz1m--oolkwQHH23FhkUjJD4Yiij2txSVpBEO38XBPAR3aXd1RPfr6t_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgfBSPpd0Z3iIbrRiSut_UuyUkLQn4Vjr0wPURAPoadRxpwoTLyn8BmpxiMdXETPDRsZnOHImIFDOp_VCSYS1O-vMT0CcqaTH3rmCvpoiEvUOBPePoOid3CNuErkFgurJQW0btmww2VJnt-Uv1KXKSc-4uoC8IVsmOJkmK_PutPt_tNH2Pk44kQTCRltYyN6CKAO7uYeE0zC7DZOm9nXyMRs9o1cgViPYqsUzT8PIfUY6EZUKD25BD0eiit955VTP-Y42QKYxZf5Lwt_n3tA_a0_xSWN-sUP2fX5Cc6EadUL9XSSNS_5tJMKxIlei1vbN5jg3GupHPF-z_lIka_Gtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=v39czf4-vYoCOL2SLhl6ICbBLvzbWo8vXVBs-2b0bY2D87J5epiZj09Woq3uamyL4TC8uVOUh3e1W1ZET3VJncVBOLiFzrt1LAJ_TR6f1vxZ27fYhBER2mjnmk7-iKAXTE-cYRQLRq-bMgZqYaiBqD8n-PhwyyNsvEdBDiSB810c4DJaO7zXtIklfwqSrtnvvBmeWXppiuDq4cKfP_bkGrliUJeWgTe3LOpmHrmWpzXGUAdoS-NMEDZ_n79yUgwMbfDtQBB4Zr-zdglIvgV1qSqdmqXa42qeUoxM2qiK0YOK2Uts5f9QQQyC98XX_qD8Xrjuy6ywpX3O3H6qw0nshA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=v39czf4-vYoCOL2SLhl6ICbBLvzbWo8vXVBs-2b0bY2D87J5epiZj09Woq3uamyL4TC8uVOUh3e1W1ZET3VJncVBOLiFzrt1LAJ_TR6f1vxZ27fYhBER2mjnmk7-iKAXTE-cYRQLRq-bMgZqYaiBqD8n-PhwyyNsvEdBDiSB810c4DJaO7zXtIklfwqSrtnvvBmeWXppiuDq4cKfP_bkGrliUJeWgTe3LOpmHrmWpzXGUAdoS-NMEDZ_n79yUgwMbfDtQBB4Zr-zdglIvgV1qSqdmqXa42qeUoxM2qiK0YOK2Uts5f9QQQyC98XX_qD8Xrjuy6ywpX3O3H6qw0nshA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آقای تونی‌کروس عزیز؛ مگه تو چند نفر بودی که بعداز رفتنت نه آلمان روز خوش دید نه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBpbRjWeT9ny9zz7CUYikhizV2TopUqYzp4Bq3pBcgsxGXrG4CD4vBIlvozUNxqUCRuIqLSD1jb3lBoQP6HbI2b8LrPiROaHrnBLjyJG1NzXjyo8HBWVeJLYMRzZ8gDvwqVJ7kPXVIQT7o19ZCnBZP9wy0h6yaefYnwe3ZbDtz_zYjOwPE98uUYKB7N7Gwj3W8tikVp7vUi9sTgRZ0b8vLR2ZA3MLyJ2J01zUNUZM9CKhYGJEOEjh7UniFZ8LJOb8UYctAAC3eh8GObWXP5HmSN3veWOl3TZyhShOhOTJnXHYlJ-ynzj-SlSKrjtBSlEYZQpducdN77C8H_L13IRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaut4VBDSCaIovt6Qxe6nUbrNpwnlYmdWEy66jwO5yNvKDRRmB6Wqx_wSycFb_Kwv4ymDLZkh06Gb0FdxUFn7xxjWKcgvT9349EVtg81ir0H0C3yBLtStLe5aqWy67k1YlUcV7Rsk1Zc9TZbrZi5Ybq5CchR9ng_kn4R5VcpRB2FMUiU6pEwn599nXVZkUHs9oH0nphv1zYjugxXhnhMsFXs6W-OJJyFQyXLATMR3ckQ7JLEZFXO9zem-e0Vj3AeOypeOt1RjV6GFTWyU4uo3L0BbPdOi1vbzQNPpYPsZ175EOAXjbQO0nsdRgn0PXpXgaST62S6vOgnAAlQl2yLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_Y6TBP5E_2Mxpmm9rdeHbYHsjVc78dTYxtjClNFuBs_ELHOuJvtssYIS8b1Q5zGMjRIp95dgY7UidfvVp2NYH8hBcCYtrOpgPZN-NGzjxEQiei4AH3G3ku8YViACI_B_7FLGb2Yz9ot_Ubq6EtYTlwzhmzpCPPjShwfU34h-LXj0AEOkzNWQUmW053V2JjCOKjI-H61GILJeduhy7a6KV1xbhzBDyl2QfzcXtD7ekU5D2JWhI_mzD8IovYb_LEHqC4tPFkdkxNwmzPinSMe_n5uRjiu88smjH_s6xSMGJip_wS7Nzq66CHYyftT5olqPYqGGgRd9VgC9PiqTTBwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=U2bMv35D6-hkpKXijLuutvukWvwLAagxWNxDjpGC-eiV7FZuYQWcWVxCVU8N0A3rWQc15M_SFyIrlKRV3M-IBgPLEkyO2H6nYhEuVVed7FNRn1ITujeP4ZhWk_T6xr35Fm4gElnRyYRqerdOF6PA1TfLOUOXMsSMRRLN1i-IZktXDnFWHae93suJHxpWKI1ESuHg_lQVDNr0CA-YRQhWkIrJ0QqUEEkPelhfxAd-6vpDqbWdayWyFUY4xpXreAYBcDoE4oh8x4bUxvwR2yytSBVFuQ1b_QiTzbqJ8n4_B3im77kQdlX_bDTAkM6UqvGT8QGQkaLMW_MTyda2H4_55Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=U2bMv35D6-hkpKXijLuutvukWvwLAagxWNxDjpGC-eiV7FZuYQWcWVxCVU8N0A3rWQc15M_SFyIrlKRV3M-IBgPLEkyO2H6nYhEuVVed7FNRn1ITujeP4ZhWk_T6xr35Fm4gElnRyYRqerdOF6PA1TfLOUOXMsSMRRLN1i-IZktXDnFWHae93suJHxpWKI1ESuHg_lQVDNr0CA-YRQhWkIrJ0QqUEEkPelhfxAd-6vpDqbWdayWyFUY4xpXreAYBcDoE4oh8x4bUxvwR2yytSBVFuQ1b_QiTzbqJ8n4_B3im77kQdlX_bDTAkM6UqvGT8QGQkaLMW_MTyda2H4_55Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yj3R4_iceDstqF4Ll48OKYEAXxRohC9r1CdeJnn5-HHe7ygDqjWhI1T0vQEIBexHfxKdsNCRc7eXqE30TukT2PBS6LAxZ2qaykHl7brXrUdFNcHFqlpj1obQP4gHTZVVp1MzdkOYyv_Us71R4oGgXzeMgOBgV1w70X-atUZI7HxKJUmniLO79XC8_nu8ZriTAM0dO3BcVgbhIrKofvdFC5msWzzne2insoFtlH7ZtTIVUbq4mcfItv4ECbamF9HU259rSYoQKfMYW_2t7E8PKeoOViEi7wdskyB0AvFFoOZciNiYqfHRQ1IGm2D0xQ5BZiyjUDFUh3s1vl83NwsZxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkOh_f0C7NIZqSbrZJ2eat2b0LipcLJr65c6832T-NA_42g1e-kHnH8Rk9XI_AiYkMsmFsDsbuDba-OsqbcWEzrYTkbN7a-gcDxDX1AY2xmixXDMZPWZXQY3HjYhRTihXkcZSE61-KyDp7pZQsMyaBjnnF1OLWJXlux3FY8uZfdux8AlZHy16TnF31x3FhN4IoXknjSVotoE6LhJiZ2KGwSqP6KZD8kcimqjhu2Dm3qaOXnPfAEze_bUHFvQ4CYtUT0RtDOh-Sob4hqktgD0Ifew9LKB_GYDtxVokIBWVPL1QupJ3tt9T4SU8Nq20p9UTNoHCFpcR5WN2kAXa2AbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVIbSyWxXqrnNPjkExVO3nJ79TzJXjTq0ZjLyx3Xk6GCzqVjFIs_MgYSYzsWccYTCjvyRNZudHMy62_gApz354n778Q6gm5-0ARGJ7SOE31RoJDpqkUm7cKwViqtCiE5AUVUGrQgHJG40V9dvidf_4iGrgeuJHWpbQ7p98vlpnNAbW6MiZgEXiIHbi7NW9IsceMKQmHb5-AchNnsLnzvVxUI8uBDQwwWBSpEBNlHG-9CN7c68ZQiRFBr074mvIWTzIVgsLW_3Op976AyAmlmIXZAR_0kU834vQE4dtVqaVQBlKO6L2Hx5DYEqIwfV7AIlmJ8uOud1c_EVc-PLBG8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtV0b_p81rtSGdahjHXrHkQlI-bGJM56NaiQGEFbhmj5mxSXpNV2gFotaFa_LKVohPmWyaPvDleJmI1GkzhAMc00d3IJqVv5F4qYXf11487YUDjumHzZwJyy9NtvgLc1zMMiy4aurQizJ5r-b-fMd7Gjk6_DcVNHy-gihkIBPXOMC7sAeCVvgxCy8D46pHtnDqpfnK2XW1p3R57SDrH4O0iJ_UqSKeHbHWcCPMbuHklci8QObNFJmYE-7i2O_1AUmGipuQzrM0N4LzF4wufjCkfAeOW3g_Qhr14I2ju8L7M1tL0elRtl8YVqdYU6PJAYXceuqgCO9jahxxAw-Kp4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daHzqoDD_MjHC1ebnjIDtcsfmj34BywFie8vKp02S8hiFt6n8_jtPM_9sb3SzH55IELs5wI0B20LScvxEUjyB6sPENptMx3334HAtbzA56ppGp3FxLIWtrtcrvhl0BoMpwVI0EQ9BQnyGi5v_vKoHTCQSSOOjO4_FQlTUSGOB79bn9kyYsyX18DiexkxhRXUCW_va__PkO4QSUh-MkGl8QRDJolCGQAVtWo2jG5AyIKo9Ok2jKAYS1r1A9tIBPZXMlXJeoE_SDyZQfFH5zAbJ864aYV_g8NJAMrwi1QbEIDn2S4DEGjCGGGXbS7gPsoPJrFgJyxXlvpgxFXA7QA5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUKptCWq4i1YH4lDibq_AoYBNz5zX6tgd6hKBrFfgWp4UIBipSywHbnMDrrX955Fm8F7fDiRUbgOUm1YvCT1E8BHWQMezIwe7KJG7HAYoJBLBsfOephuAeXIefBtF00rGpDjwmARC2aEZGYPbwHbrsWSqmppvjzmRPsbzy-shjAdanGLMZUwfs0daGdfg2FjdIcUZ4b-RjligJl1FahAsEKZlFNv86gUqdT6wHbS3L7K6yiRJ9Y2JQrSLUgSAHirs_3EeWsf1ylTwhs5r6uaLxTDjTTTD9oUQmcj1vWxt5o_nxu9zLUYT9fff2M80GER5chAxHUzY-93ZZbV-dOsEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLXPFqLHJKWYjrG-BI1gorGykpObmMtTvXR1NRthwYGuOHx1iIp_Kmh_6BUIyu9I4kONkSDrkIVr789KuU05dB98GnaDnQicXPU-FYJwYlCiCfD3HPoc035DlL4qvVq9be4fs9QSKcCsxqL56Xzr0Wm3HhC_JygAIgKkvmxHKb7_QBHzaQbmNVm3xgy4GbZB1-e6NssADlVS4uImieqYlGOBRXfd3AEzdPvbxNdVv4G_PEz86JuIz7Ml1byIBUXIbIpJimxtCGbeSXlQLurQs_jk-ZOhp8XVCazJC8DCkVkN0THp4ZgNoH2H7PEJG1P4j05gNlctUYKfmArVLIgW8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgQSjQjPuwkpZZeWEpK46IrC9qG3imWuXZ1G-6nXGSncS5wmHv0-DLaa6-8QaV6tvUcBgWOkIqOpGmbtfc1ITBPgo8_DxZCLY9UZw09MS-J_cAVfghFRThGgi8RJtOaGAjg8oF6rRuoIL50r415-UBPhmf0P4oPL07akv73V9iT84eP5KL47dHIdIaQx-CXCsNskaoEHxQi7nNF0wxM0ioVIEquZ25i6L8q39va9a83b3UIr4qfupvArBnkG0L4Hkhr8kCbSsXqfh740MQca7ccFOBJaTwfJoIH04DGlbbUuT1ygujILc0mkeMKCtkiwi3YH11Y8WZmIdRaV6aZRKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZt1lOO2lfAxlVcmvrgNkUwMRgTJuo51GJjcA8eHLfXBw_qkGFYt0Y6d0FbAbHy659dWVDoXbsIFB4dRGr94Z5OSFuKhAdEB3bHE521hp_pnmPyoDY_4GvXeP_6soUMw4c9NLM2GTPvgXcFyBHO3PyxeLH5Y2TaclQRpwbcSzeGqFc6fZ7icGyp43zeQa5IKFKsVQBdYoG-LJQ38IBJhs4vf4wB8FvwEt8DsPwETN0RDfpQhQdFe_x5c6toOqhh1bhJpDTqkGopRpVIsP5IngIUd3JewDcKwejA16siUAyi3AH7_pnPOKcLSRRTrJvHjdgz2CBpWUTFSUojDgUSUV45Pc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZt1lOO2lfAxlVcmvrgNkUwMRgTJuo51GJjcA8eHLfXBw_qkGFYt0Y6d0FbAbHy659dWVDoXbsIFB4dRGr94Z5OSFuKhAdEB3bHE521hp_pnmPyoDY_4GvXeP_6soUMw4c9NLM2GTPvgXcFyBHO3PyxeLH5Y2TaclQRpwbcSzeGqFc6fZ7icGyp43zeQa5IKFKsVQBdYoG-LJQ38IBJhs4vf4wB8FvwEt8DsPwETN0RDfpQhQdFe_x5c6toOqhh1bhJpDTqkGopRpVIsP5IngIUd3JewDcKwejA16siUAyi3AH7_pnPOKcLSRRTrJvHjdgz2CBpWUTFSUojDgUSUV45Pc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
