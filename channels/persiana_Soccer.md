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
<img src="https://cdn4.telesco.pe/file/OZQE00_PfM34szbpFST-nn5Oy-xyWdh3B2bpb_YlQvdCxXe_j0Lc5p_xv77MRw9WMxtSSJNyBFYKGIQdY2l3BynHxE2CZ5tuSoc9hUFE_RqmxhUKrOeEYzJ-_9y9xFgv3WqwnKdzmeAU0sTl5--GSQvWC9VSGYrnEfeuLJ0hQyaK-G-akiUcsobqh32bKdOjFFpNNXlTE-Nkv17ek4kVU2uVHlWNDJY2GHbfbSG8gy5SPKU4qiDCeBgY_4CDSg-h6Hhit0aE92oB1mJMokA_-b3AfwbTngL_VArdjqrnkQ6bi6vBJ0FGYMKh7e5y7TqB1F9Q8DYhoq5qBbDbHUmBwA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 501K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 13:03:18</div>
<hr>

<div class="tg-post" id="msg-29937">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTSxklE7fdWCLAQhor72WUJbTXFpCerDZ9GpFKa5aaG3SX9_Sfo0tKIynn_hQep6b4FkStCD2L1oe-XjKJvDsNeKa4Tnp1og7XwDdJ_z4niJ9aMSajGJyMU-kHTuqeoM2IJgwiXryfGWm6gmSebp4azj4XD9Mm4HpJuMKK1D7XRFxfqS27enUiKelfAJP3UmHZlWUNh2DEi2YgxmEua6MvB3OkwsI_qHcDJCrF_jho5rTkyzIUb7ZB1G5x9BI9lY09kc8psEDMIrL08WhYT9X9zLVmqJZ3kGeDHDHnuNld_qRpFdq4lMchIUJ5o7wKRF9R8hdaQbABG0CIHnYhEvUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کمیته انضباطی سازمان لیگ خطاب به مدیران‌باشگاه‌پرسپولیس: قرارداد یاسر آسانی با باشگاه استقلال قانونی ثبت شده. شکایت خود را به دادگاه عالی ورزش ببرید و در آنجا پیگیری کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/persiana_Soccer/29937" target="_blank">📅 12:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29936">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0fc3a9a3a.mp4?token=s44SDMYD9kHx1qBGNXNpKNldB5sBmbyZVA4Mv0k2tLpI6xcPRCnp1nY78hoFU7_yxreiyt1tIPBgeyALGaaBt_l0AU0aZtx4_EkZY6wowBZIemhYwSuQzUyyj8mpsePvilJUMilWz3Fg4CnYL2S8C02k6mpIh22cW_O2GtXuiezkJfVAoKZ-BRZZXxpVeAn94e94UhxFmf9gYKATGQJ6-c8vCxRi0ivnQ-wi6HsqXGnjj-GEqLn4cDOdjnugNWuQ5ZqLQnDUFu9W0uYIWN6USELor8HcbsY0ZMtOncyxRKfIbEnxutTHjL2Tm_NEXxR0JVcBVKYCsLeIj62ftBOupoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0fc3a9a3a.mp4?token=s44SDMYD9kHx1qBGNXNpKNldB5sBmbyZVA4Mv0k2tLpI6xcPRCnp1nY78hoFU7_yxreiyt1tIPBgeyALGaaBt_l0AU0aZtx4_EkZY6wowBZIemhYwSuQzUyyj8mpsePvilJUMilWz3Fg4CnYL2S8C02k6mpIh22cW_O2GtXuiezkJfVAoKZ-BRZZXxpVeAn94e94UhxFmf9gYKATGQJ6-c8vCxRi0ivnQ-wi6HsqXGnjj-GEqLn4cDOdjnugNWuQ5ZqLQnDUFu9W0uYIWN6USELor8HcbsY0ZMtOncyxRKfIbEnxutTHjL2Tm_NEXxR0JVcBVKYCsLeIj62ftBOupoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
صحبت‌های دیوید بکهام مالک باشگاه اینتر میامی درباره لیونل مسی بعد از قهرمانی دیشب: ما هنوز باورمون نمیشه که لیونل مسی رو داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/29936" target="_blank">📅 12:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29935">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJ57LXQAeRCn02co1i4Udvp3hWStqvJUcxdovPiNaHJULsV8HQyrUrHY2GT-13A508UiwXvqImPf90IFZnmNoEg-DxfVJL_1y7UTEe43-HQCvTJgQC382lk5-vjMJO_cYYmmOlDWxdzO81NYeEDOWgFn22XQ0ZVp2Vum32_8DGjEgpBCo-CqQMTmcua2IRX3o4OwJ8hNxpECPtVH-0PPa9biw7i-ilxn3zcbvKbsSSB4jlUBwRTkEhmU9W3iDI7y_c-PvVxkz9JQWN8jK9-xdk1FG55wwwma5shwO_cV0tCZAgmarEj2gqqRO_TMxcneX_h_HE-hi8kfBMxQBbPJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روبن نوس ستاره‌تیم‌الهلال: کار زشته هواداران التعاون رو هرگزفراموش نمیکنم. اونا ادعای مسلمان بودن میکنند درحالیکه‌به‌کسی که دستش از این دنیا کوتاس رحم نکردند. توصیه‌ من به اونا اینه که دیگر نماز نخونند چون اصلا مورد قبول الله نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/29935" target="_blank">📅 12:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29934">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW8X4ZvK4zOpQSHq7zgYvdP8BQW4MGbE4JIV71ceWbF6OIj3rJ-Cm1pBQG4OyspKGlfS117e76RvP1bOzaBV2X7e0HLoQRzjX5XINCOl2xSkIuBfrveGeEuRYl4I9HrrXkHIMvOc4QhjGqaW5d_ClAJ7ntj6-mtZIG672sEsY72IIMO0btj0Xx-CkS3ELT3S7vQAP-kn2C4i3cObu-7LmjQWrt4DHvxcbBwgO6BGloUhpk0KjBomefjK7axK95h6yIgofD5xnTDKcLkWh08s4uzmzsNdpAJgwi7ia1Xi9dSo_FkjzTBDtKOHFv-YlzmFVkXCVBY73xtVNWz3BUXXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/29934" target="_blank">📅 11:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29933">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGJryP5bh4B5mQoIyGH_88O43jdRIWx44v9oGs1QNA3iG5ybiNP0yncyOaPGx1N4pWh2JuknJt3dWMTjZj7inJ9X1P40pUqJwIcjX5cvdzBhBx-GmkHTsrfC0jXZy9cNtmYqZuJaKDL6OOofk2kJ0WHNSKQ4lbDLDKSUP0dJ5UP9BvV3dFxYjmUlS35PpKCl9IsG_2cFALbcWbaW5GpJbAs8kmExl3Wb8cGP747s3Ky0oIbwIkRF4O-iQ3x4PKLQWglrgjmq2z4p7xn5ISBOxYcYPZXb8h4cHMpLe1PLQZijuvfGs2-RmDzxgHXZ1NgKGMjnlF5pYs34JVD6nTrWZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/29933" target="_blank">📅 11:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29932">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3-6R8QVEVQJUYj3buTDpzEhXGYigmbK88IU94poistC_jxP_ZHy870N5aSw3BP1a1wPSjo4B3VJMQz8KCiloxI7wChbDAgfR1uMYEP1IaaHjlKt6RNFRJOLJJIdi9n5SETS1b3ywIOGjEDymw6-d7gLMW9StATTfsQ6zhHhtY9hZQNi7w5qiaxF1--BR1Gf8dZcoRp0LcJcHiTiJ7rkI86vsP5tU0UKKxYx34OXZ-V5DTa_e_5trZsPcND2X679SdNQE7ZRjK1bLuHhPUaTgLIQxvRUHvSLrYDduURfUOoI3dHey5o2pI2cFwk619oDmzh1FGp0LhKPL9i7qX1CQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/29932" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29931">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8zlBlCEnSIxM54bSOsKj26W5HB6tHGKRN-cvonl_BAKzZEeUOYkdSbLPAxLGooNijOYhbbhTTgi6GHWhrrfLljTyWHdkXQwgGqyox-i4RBzqOIOn7xkQ-StdZx38pvhAzLi1k3hUelCOj6-gznqKAYDADVdG5zCROMWV8nu57qcS8518xj19BU7h7emYPq6xA9XZa2mU7C98lGJE6M-0JuL9i4IM0KfLkcpaeryHDek6ugZvxFwMApzuAc6Jx150ndTEvLWyYrGHXajj9h5X9YyIqC2KxTavpl74eLHwMxWmb5GZtnIwuOEB3w6DJFURb9iJow5ca9wov_EOc_gNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جی جی گابریل پدیده 15 ساله منچستریونایتد که در دو راهی رئال مادرید و بارسا قرار گرفته تموم بازیکنان تیم‌رئال‌مادرید رو در اینستاگرام فالو کرد تا نشان بدهد علاقمند به پیوستن به باشگاه‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/29931" target="_blank">📅 11:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29930">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRl42cct9TLCF0gcBUxH7H35M2y30QocMrHd5gbGNfiSbQjKLp1wwvkQq-lfQA3mfrcNHU0rXlVa1rAv6s7DIM_4SZL0Wtfha2Af4EoSiKnfIWWWY476XuaX0QlQmam38z9JnBt8eIC1EFhxa_wb5-1uKpc17CcgyQ4TDXBEdG_75sPNu3mJUlnzsnIWJ7JZK3nXR2A_5oW5U1YbReCKlWslrjG2JiVT7_ORWbzYjUPMAPeQeWLE14d6aP6nBdSNLmvb0znjxhDGFepQsjn96YSn6ymMxOPJWt2ytyvqfBQ4hsevjaE_4WfmuIlIcNHxw6JOUI9NU0ZW1okyZiF7Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌لئومسی دربازی‌بامدادامروز اینترمیامی روی پاس گل دیدنی لوئیز سوارز؛ این 929 امین گل کل‌دوران‌حرفه‌‌ای لیونل مسی در مستطیل سبز بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/29930" target="_blank">📅 10:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29929">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rClCoAifTJPR9Mf8H5jSpl-9MoC2ZKJKS6RPJlw-C9IoneXt0a-fjY7lOXdCxW7hqI5iEpf79ArJuv5uHhl_x762octIkSHLlcw8esjLq7AFlQYOoT8jbYQvQ0OKiV875KwVuHW5Ou06Hf3xJGI8IYdPBLSJBcjqspJkX2sYVvyyWlTFNZ61jfdYLkx4JbXzOpLIbMqr1aNImt3GoVJyUVgYjmeuz19ESoiUTSP7eJP1hoTqxdjZVwAL1p1qiXkGOhE1-EC7J9Qz26Uj6P5Gl-Wcwwn1oSSriqsRMnLG9ZfpLLBW1A0__2DJljkFW8Z8usjL833uLw4o2bukTBcGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیونل مسی بامداد امروز 49 امین جام خود در کل دوران حرفه‌ایش رو با اینترمیامی بدست آورد. لحظه بالا بردن کاپ قهرمانی توسط لئو مسی همراه با آمار کلی او در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/29929" target="_blank">📅 10:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29928">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92dd5a0020.mp4?token=NXY2Qtl41ROfrMSneaib1GlcUnwn1PTixmFWJjV6U_vtfiWLNWsxnaoclJV8ISz0v7ueEHwG7eTF4RHep22vskC20vVHNMn2qv5L-thNpN6aGB3R3AdC8mgbwwkt3IkiQrh49lryJGpXrxvlVi8i_Pw6j7m6JTAdf6ZNKLyfJGpNPlRB5hPrg6PV0l2mTdViwOL4YEmrDGwXjD8ONvag1AxH-4QT9O0ieaIB0bjkub7LKQgNvwfnhTArVo2s_f13Qr3jw0yJUS8Scc7BNHg3eh3K9Lp6wbviDHcbqqd6ChVkPo8kQBAkzaXLzlMoXYu57mb5FK1A7D3Py1b95irx-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92dd5a0020.mp4?token=NXY2Qtl41ROfrMSneaib1GlcUnwn1PTixmFWJjV6U_vtfiWLNWsxnaoclJV8ISz0v7ueEHwG7eTF4RHep22vskC20vVHNMn2qv5L-thNpN6aGB3R3AdC8mgbwwkt3IkiQrh49lryJGpXrxvlVi8i_Pw6j7m6JTAdf6ZNKLyfJGpNPlRB5hPrg6PV0l2mTdViwOL4YEmrDGwXjD8ONvag1AxH-4QT9O0ieaIB0bjkub7LKQgNvwfnhTArVo2s_f13Qr3jw0yJUS8Scc7BNHg3eh3K9Lp6wbviDHcbqqd6ChVkPo8kQBAkzaXLzlMoXYu57mb5FK1A7D3Py1b95irx-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇹🇷
کاشته‌دیدنی آردا گولر دربازی این هفته رئال مادرید و شباهت‌آن به‌سوپرگل‌اوزیل درفصل 2012
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/29928" target="_blank">📅 10:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29927">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5WUQHcR1LvyQA3JZq9AHGKzZ2AFkvu96LSgpD0WP_l-pG35GiUD8KDtG7Q2HY1-vVXWYW6x7KgBr4-ZtXiI8So_sZ_zhywOOlDbFex5LjBUQoGMh-_xvqGNRf-_sYS6ywgxvFVKM7SYYs3TPmZ7DsF-5cL5Hb8ERoWIOPsxkilL5Q1Rnb2RWu9VpXLit3O9U2aP5-fMoV2XRXlFxwwvV6lYa02qpIpNYiNwsoZocfGmXcs8a_Kx9madb2HfTVUWX-x-LZ7oBgA8brS9sn_LXn_Aa0-lAot7TJAw-na7M4E3DS0cfX1QkoGYNhywLto48ZuAvt8mrYcGL7EjdVsMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
❗️
❗️
💥
جذاب ترین و پر سود ترین بازی پین باهیس رو از دست ندید
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
👑
بیش از هزاران بازی محبوب اسلات
😯
متدهای پرداختی ریالی و دلاری اتوماتیک
👑
25% بانس جبران خسارت بازی‌های کازینو
🎮
ورود به دنیای کازینو با هدیه‌ای ویژه
🍭
انتخاب متفاوت و هیجان‌انگیز منتظرته
🎉
همین حالا امتحانش کن!
🎁
با پین باهیس شانس بردتان را چندین برابر کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/29927" target="_blank">📅 10:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29925">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1jhsfQuHUlYY49UM7n_dl2BgY3tnxltDIqMXsJumjwxlcXeMHvTvxfoWVvD9Fv2NT9FdtyY1NIEyUvjHwC27pLxFeVpyRRTGJFNb6VKHXxzFRyEwwMjBHh_TXoev24w_xcyvC8-IFQGIzkSfCY-jwX4dYwCNV0iZsvwN8V6wGU9g0DRof7TSXd_Q-4MpkAB5qji2Dfu8a-PVUoK7Pi44YiOC6zAgltTaSWUcOsvUjT9zp_ei9rwAK7Fg349_L-5MkZx0hZGbpLgRN0oKAHUi8jlO-X-v0luXlEinQKnNNSvN-w0AaD-6iNBYp_GaXmdmSyR_HH31sL0VpTODQSmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d0f762e7.mp4?token=pIjPCikpR3XH96b266_cpiYN2V_2sUiBceQ4rH_zBEOudPVJyV3ye8YDruo97oW6kyjJZ9MOu4feQF042TF4wAS0puAns6jQpoNeOjj0UFIOgRKcThwG2MBQMqJDImTYfmDEpMrmv5Bzm1oSbcOC1P8qLIORDOxXZM6mLioY5H-Vm8X_1K8ikGWpVobkcFkx597X090i-F-OfNyq6RQhTCaQWr0Wf1nSjcTyMqvSRVgcPPdkWTTGm6JgLFsqZDEoWOXh1qzMv1oQJ5XhmXZmwpN8NLBr04NKMMDf6de6th1m9x-o5aWlAtuE1HrZHjJdOvN0SQGfehuBlWR2amQ7ZlNyfV0VYLKvGc3m3_6X5vk45ezzWJii7hEK1MNUXi0ecHOpaca2gzh_8BBtSuWyrTCbmiajjI45fHN1CJRvnGidC9CHubcZruhuV1NyZ7sxdFh7uvCkXWNVznelfg4zh3aPiaIJ9Oe0mD_zTiJmytoxweMH6cEPM75PgSM4LmDULjPFcigYgOr1j2RA80u8vzNJJjRDmGu3AieLLq4DZ4jmot5hxsDtiJLnhNZXcAr6XED1Ir_VtKSs-1xDJ83lbvZ6L7EdsI1UJFi7rbeqrucFU8mQmKYhj2o-ZlbAIsBUbcK4tHnhselz-9DL0q54SxurlZfEy_hOzQXSGXZDI0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d0f762e7.mp4?token=pIjPCikpR3XH96b266_cpiYN2V_2sUiBceQ4rH_zBEOudPVJyV3ye8YDruo97oW6kyjJZ9MOu4feQF042TF4wAS0puAns6jQpoNeOjj0UFIOgRKcThwG2MBQMqJDImTYfmDEpMrmv5Bzm1oSbcOC1P8qLIORDOxXZM6mLioY5H-Vm8X_1K8ikGWpVobkcFkx597X090i-F-OfNyq6RQhTCaQWr0Wf1nSjcTyMqvSRVgcPPdkWTTGm6JgLFsqZDEoWOXh1qzMv1oQJ5XhmXZmwpN8NLBr04NKMMDf6de6th1m9x-o5aWlAtuE1HrZHjJdOvN0SQGfehuBlWR2amQ7ZlNyfV0VYLKvGc3m3_6X5vk45ezzWJii7hEK1MNUXi0ecHOpaca2gzh_8BBtSuWyrTCbmiajjI45fHN1CJRvnGidC9CHubcZruhuV1NyZ7sxdFh7uvCkXWNVznelfg4zh3aPiaIJ9Oe0mD_zTiJmytoxweMH6cEPM75PgSM4LmDULjPFcigYgOr1j2RA80u8vzNJJjRDmGu3AieLLq4DZ4jmot5hxsDtiJLnhNZXcAr6XED1Ir_VtKSs-1xDJ83lbvZ6L7EdsI1UJFi7rbeqrucFU8mQmKYhj2o-ZlbAIsBUbcK4tHnhselz-9DL0q54SxurlZfEy_hOzQXSGXZDI0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌لئومسی دربازی‌بامدادامروز اینترمیامی روی پاس گل دیدنی لوئیز سوارز؛ این 929 امین گل کل‌دوران‌حرفه‌‌ای لیونل مسی در مستطیل سبز بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/29925" target="_blank">📅 10:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29924">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePSVPTzEdSmB-Jc1_d8eRUHS08VEOsSN2gKxyhP_rdassnNVgb_tBqfM8PNOQWRwbk9IMg6JlQj5oaK8ynQTSlkdWm1SAut1JZxZpKGLFy8Y0bx5ghXFpEb1GGP5fh9NEywQQu7j3OMw2ETSu_h_ARVN2aJb7rgGHxVSmIhjWOcMgkr3Jx60BZQ2a-ytTHa-AT9wjyJPnplDTW0_vGBYeFMg31vZ3IAMciEX4a-Cqv-a93C773ccwZksSqNqz_RRbu4cQJxQlQJiKRTFbZSspXbMVNA9dETpQiiAhOMyLhyYVrdGUGDcnmAhOBfBXL9qJazCFsw2mvBvcEHyEmIgFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یک‌ایرانی‌مالک‌چلسی‌شد
؛ بااعلام‌باشگاه چلسی، شرکت‌های‌گروه سرمایه‌گذاری Clearlake Capital رسما 87درصدسهام چلسی‌راخریداری‌کردند و به‌این ترتیب بهداد اقبالی تاجر ایرانی مرد اول چلسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/29924" target="_blank">📅 09:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29922">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📊
یازده گلزن برتر تاریخ فوتبال؛ 21 گل تا رکورد تاریخی‌کریس‌رونالدو برای‌رسیدن‌به 1000 گل‌زده در کل دوران حرفه‌ایش؛ لیونل مسی هم این هفته 928 امین گل کل دوران حرفه‌ایش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/29922" target="_blank">📅 09:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29921">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
کریم آدیمی ستاره‌جوان بارسا دیروز سومین گل خود را برای آبی‌اناری‌ها به ثمر رساند او در این شش مسابقه‌برای بارسا 3 گل و یک‌پاس‌گل به ثبت رسانده حالا پارتنر آدیمی با یه کامنت به یان دیومانده خرید 140 میلیون یورویی رئال که این فصل اکثرا نیمکت نشین بوده تیکه‌انداخته.…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/29921" target="_blank">📅 09:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29920">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇪🇸
👤
در هفته‌ششم‌ لالیگا؛ بارسلوناِ فلیک با نتیجه درخشان و پرگل هفت بر دو راسینگ سانتاندر در هم کوبید؛ 6 مسابقه، 6 پیروزی، 34 گل زده، 7 گل زده؛ عملکرد استثنایی شاگردان فلیک در این فصل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29920" target="_blank">📅 01:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29918">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4OucnB1s5tYNz19miA2YEa8D_1s3eKyK0cj4n5qQOoyjpEkVzpdqPZ2IyXYv1_dwb-ylTlXsHyNtHNk3ecwHh9ANByd1E5EZWr_eUpp4RbCCu3OTdvcOpWEyUGM-WUmKEoYdCdd-0OVEI7h8MZRheroe92aKKv6i5ZIlvRtighmkVqGmOCf_nXgoM0Wk0cGzgPbOrd0WoNTuSH8Xh2RdfB4Fw11uAyYR1e_13x8lmnSY3Wi1-IaZDQQo2hzkSWFI_KDufLs1AURgC1TNNGpJGqhRAAzajEhdpZ8wxULNRoeSlTd_WmmOwO-Tx0QKYoA4Xha-QG7aeZQKZzzRpgWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌ امروز
؛ رویارویی صیادمنش و لخ‌پوزنان با کریستال پالاس در هفته اول لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29918" target="_blank">📅 01:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29917">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUO7GFfy85KiSmGFuIHH_GLqoy6WU_pQo6z3aX2DpjqMY4ZcGqY69Iwk3Dg3PUPniOnAPghKHQwCO3fqTP9gRMrbIQjQVfllHBV0spe3oF6v8tN4XXjNWia8fhvUOQme6BlOKjjYVqTEvP1EQXobB89dX-Xzi6PCDCpETahIxqpr8mDND3rw9Rl0I_CTgQFLYHDACBbNcqNKe_YsKBzlQG4xOC1b_ZNHllUtIRhfn6NfpNMjUb1hT0tl4LUZ1tctYLhfShixMCV0YHU8pAkboppAPdVHsIp1SZ51XgDSPShvygUo_YkAyoewVzFiKgSTMSGHB7b5MzDZfblyEy70kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازکامبک‌برایتون برابر یاران کریک تا برد هفت‌گله بارسایی‌ها و تثبیت صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/29917" target="_blank">📅 01:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29915">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ne4jxWtkBQKgtGN8Jt8ogRjyFvRjuRroO57LjuHFfDxkIBh74dax4OtpCYqRBhVgmfhJmT427nEuJalLeCcS0kES0zA5Bz15TaF9ZBdnCcbmRji9pfrZQ9WgURZQ0ybLarGBPr2PkECZ7C7DsxbxB8OhhZYfv7DvdIsrqIA8jVy5SB3m6IHYBlSlVYv2oE7RdA8guBTxX42TSfiTHg93EdUAOyKtaF_1Vqds2m9NHC85PZLSA7UjimWfpj39eqCZJs-DaOxJdahTNatsb9HqmuOSGDK2fo4trm1HxdXurSUYDOXYFfKV_K5cAxqqQ2HEWYlklbIVokO_U38oNdHKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edqbb0ODooBJkCZZnwRZ4mZfKufDrZdohHEuye0xxsVnlx1MqSi-k8aYFWQN5st37LoMw1gvtz9wCQoFWUtXCMwF4V8I8mMjHPTLZzmCQWs53vrnxwjJ85uGaefSGs8xj24CTysTz6mTSwSaG48vtTY9yYIHA3NRchcg_6f6PbuvqYXGj1zihcXYTwceJeNNKRqQWnA1ivz77m_SplQbfeStRjwyimdzJS3klZ-QWqf1NABtyPV2EQ2eURumUEaNGdiF85t7rG7suqUf0BN1ugJ8alK_RE3mS_rGfNadTC_EBkwCXzmy3t0YajNlRWnNODiO7rGt5GOl1mEnLuWZTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29915" target="_blank">📅 01:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29914">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELhHKFzxT4MC5W8ASgvIwddzQhIiVYCOjGRYijkBqa5MseymtPVotDKrDLKCH90fQrIZfJmjEBAEAkPLsDl8dSaVKyQqQYT5Ivyvu4mVUxHxuyAC1ml8IcV1B7uEAzeQUQyQDL-xSJqpqEjEh7nvhlkgOzJuOczPZfHK9VbIY-UnNphQMECPtxZnryhCqAjZGbqNx24cmrGuBcu4lUsUhWyLP4lyb0jBYSBnNPuYa7OKImjCxWiPZo3sliiHOq-lwNrf8jLCvZPTDV7Q4uyXuqC8eD-WhgxjdJbHmD91sWsQk0YmxDSsC4I3ryfPyyeAYXT04qeepkLgM6NOjkfmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
در هفته‌ششم‌ لالیگا؛ بارسلوناِ فلیک با نتیجه درخشان و پرگل هفت بر دو راسینگ سانتاندر در هم کوبید؛ 6 مسابقه، 6 پیروزی، 34 گل زده، 7 گل زده؛ عملکرد استثنایی شاگردان فلیک در این فصل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29914" target="_blank">📅 01:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29913">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv2e6-NWZ6ySH4ZD3hdCuIRPOwOsg2-xISeboE7G-8aakNMq3XQlezJBEvBc5Q2DAZ2DQFzJ_GNkMb24UQ7OqU7aMQq9ohDVwQc4rB2wbNNLsSt22-eFp73j0BgFuWoY5nTlXUYjUbTSUT-dSx7Z0W2HMHKpx2dtBSHKGn64lQKi7EMHP65Kpf1zm9mRysrGHoeh_uVYHwQxXJUDd6WwmZj946Ss-c-3mF6RzKyllJk1e8mtyDmSc1MK4ovBnLnpoqaAK1V2vmpdrYzRz_GWrXtw1AZmqzDptom0LzouDppphMHNOOFl67M9FiITUdw1m3GC3NnBw4sZE6lepoEtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
دبل تماشایی ژائو کانسلو در زدن سوپرگل در مسابقه امشب بارسلونا با راسینگ سانتاندر در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29913" target="_blank">📅 01:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29912">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLxQTddycIBl7lKbDdbXX-t5iqzXM_hJCW-ktELwxQBWLicLrO_hotLL95R-X01KeelXNIm5N1cAmoi2R0JpnvElVhxnYB640klio9nv7Eip2bkY70wKMbwATxBE_Z02GQPc5g82_0qyqEQvuKWuCvUgu04whnW7IntnwRVe-wyF98hQbRiYB0IUwWzBDMEG63d4dmjk6snbwwRoNPTkiidkRQkj19Dfda_XV3nfAC5XarHVw8r8-pXxiQeEsrFIU8bmODDkAd3VEY4-6v3ctljLjLzJFMaHWstxGBLVxu5MIDUChKMgN4XM4ePfwyNg1JQdnsZc-RpURp5moev8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
دبل تماشایی ژائو کانسلو در زدن سوپرگل در مسابقه امشب بارسلونا با راسینگ سانتاندر در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/29912" target="_blank">📅 01:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29909">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nye-_8VWXAOIYrIUyzI99FMtfEPhZYXBtKKJN4VNttoos14yv5xp-MP0qaYkicet5_n8uivMTCs66Bjef81VfKV4glCQshoXhkDW-UzSrwvBldyy7r8bfCXV72RLsFfuWDcqHUT1oaiK0U4piIjcvqDvxgneQK0PPnRjvH3Fb4x3JmkDm-Xxi3pNmtnXFS_Mf92JX6f4Rml-entdjH0Ldhu7yIfAPWk5qaMZO94PGbzuL7OnhmNk_W9wsG3RfacvvpueCs62h2jGnj4CvRwdElHbRkmkp1KZTCHNzK6e2ik-PomFGrbIjFxWg9-LHRUdO8-ynxWIuGCKn5-cO6Ix3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l2W4i-KgQofWSaFRsGaa3Gp9ixdpjDxgzz4ZkHtR-8-H-JG41XzY2G_X0CY14a7eQWKNYOljezmdYtrNrJcr8HxbxdJbw2Swd2pgP-Zl2Gw2n3hMgmeDd_lr5TXEX5F8kz1ZA3PgB9SUgpaEVEIElOobJmiYLYw--zsvdfp91ie4U2oDET5TjmBFsVTo6zBljESvd6ikXtnmTpQN0f3uApQ5e1qcwQDHdFMa36kmWd8zyl6NRB4QYiAnbBJ4KoGJqb3cMm3VqgKE_ev3mZynFevQsqfTDRcuWXLyBtqB6nZSQhgcGGY-qIWj5miKxDMss0J2KQcuSvvw9U_-Y01DAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دو دیدارمهم‌امشب؛
حذف عجیب و دور از انتظار شیاطین سرخ از جام اتحادیه با طعم کامبک خوردن و شکست میلانِ روبن اموریم‌مقابل‌بنفیکا درفصل‌جدید لیگ اروپا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29909" target="_blank">📅 00:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29908">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVkYo93re6bA_gXhmF8yK5pvmLH4NVYDL4vbeyZQOZMJ9zk_n7FeOVQPNuIvL_pOQdpWembxHLTV0SX7rypWgnpV3CG1ik-ZSQNbnaMl4SjtjHhM6SpEeOAQ4cAWY79NFrE4a4sYf20B2S4yV0xCwUD2db9VGjBRGxI2ipS6fh7PCN3btMf53dfnhmG0PcrcKPBj4aegiTnYsPtbuTI21JIh2GDy5ea4SLWxHKHsoIgoRsGcS2m1Qgx5QudoKaYEuiA7nwtdLqip6wGXfYQOe7wbcmdMJMpy7jd0iDHVRyn1lHOBS7oX7KkaM7sib23wK54fORFzdAKnSKpmF8nT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29908" target="_blank">📅 00:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29907">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9DWPuikI1E6KuVD3NbnbCY8r5LS8g421DXFJ9-NSVWdFjb4yJvy1yAT3MXfPjpnp95H1Z1jxKpTN7cZZGPsK16gTt3wRo7ViKdTqDk3b7tmY-cMB35MPSGf_I11rfRC6pOiXvYNpJE0wfD__DfqbDF7n0h2FiNnFr5eOyPh5lHDMNlimgYVEYuRRGxlH2pA5SqWYngwrWifLHXY0YcmemkprqUFfDrX5pRjTHWTpNI02SRCvURqALE6A10nkdN9d3wDScg-yzK15Fy-NDpAArEBR7VkbwYEGjNpeDp-2sdtSzn318W2hrWX_RFw0lYdNgmMAbp5FCPfz7IJb98BCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص مهدی‌طارمی و سردار آزمون چیزی که ازنزدیکان این دو شنیدیم درنیم‌فصل به لیگ‌برتر برنمیگردند اما این فصل‌قطعا آخرین فصل‌حضور این دو در لیگ امارات خواهند بود و درپنجره نقل و انتقالات تابستانی سال بعد به لیگ برتر خلیج فارس باز…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29907" target="_blank">📅 00:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29906">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgIlKg0lmBAX3q6m9CkxWTXf_DtJIct0lz2z_lBjEoTSwe2XgJq0sv_YY2nAtODiJRRzfduhoqNcbnvlxnCXANiyq6hsxMgfPJkYRVE2tmwmPq7Nxa8HV4HJNA0yXeQMAdX-Iow53aO2R0fi3sLag516bfBAh8gUt-yZ5kbxjuSBXK8zmYc4mrQr088VUaOELCFUskQ5UX45TU5YgEdDKuj_d6lVoof97GREhy5DxqvQoMbRIqkmdsThm0yjOyli8SDf-b36LkPHfk6RBVZQXegBlDU5C_YRyqeej0WeaCX0Gh-hMriLRLNIwo-MQFWhUjLfKlbQK9RVVjzhjApIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/29906" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29905">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b56fabc8.mp4?token=p4ue0PTU_baDy4LJ4W_wxujg7O2yYxRWxt5XZfSn1faoLw7cdmi3-fRmT9g7z1eAEaMgC20gYei0Xb6FXpXUrUZpUX2yJefiSsCsAsziwFwn5bI6JyGbqZSZT4oRF_8-1wj6bkYawCKy-lzhuCbs9TkBoxFC6zRcJNslHYgnLPO6Rr4acFMA19Id7JTShQC-dHDc3Z8XtVl0cUSVEpXs_b8zS9_dv2WT09nrTnVnzURbu3QQd7L3v_JG4yee87yuWnQ15K8Qo4f2sjAgnXaEx11bXXVvOgR0Ml2c8VNmdKrbpydmcm2tPdsQZwRVA3i8WRyhF7_wriTyGYwN-oEllA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b56fabc8.mp4?token=p4ue0PTU_baDy4LJ4W_wxujg7O2yYxRWxt5XZfSn1faoLw7cdmi3-fRmT9g7z1eAEaMgC20gYei0Xb6FXpXUrUZpUX2yJefiSsCsAsziwFwn5bI6JyGbqZSZT4oRF_8-1wj6bkYawCKy-lzhuCbs9TkBoxFC6zRcJNslHYgnLPO6Rr4acFMA19Id7JTShQC-dHDc3Z8XtVl0cUSVEpXs_b8zS9_dv2WT09nrTnVnzURbu3QQd7L3v_JG4yee87yuWnQ15K8Qo4f2sjAgnXaEx11bXXVvOgR0Ml2c8VNmdKrbpydmcm2tPdsQZwRVA3i8WRyhF7_wriTyGYwN-oEllA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
گل‌فوق‌العاده‌دیدنی ژائو کانسلو مدافع راست بارسلونا در بازی امشب آبی اناری ها برابر سانتاندر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/29905" target="_blank">📅 23:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29904">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7cbf3081.mp4?token=ePymEQK68QpEofVDBTzyBjXwCJw_tXk30qiPkK8IlrBniNpAyW-WBjxEXkzsEYrugy6KQrekon8F7Z5_JomoahdkH2HwVu-mXGLZqh3f5x5-YFzgY5e2hAYhz9LbUIBy7Xt9teIRC5OGz4TwSdJXakBpD0F9cjYZfV7gTfJ1_ToFSQdtCChUmcpOc-h3v7AK6Q_dtXm81SdWPviOhU9XGPhtI-7PdrPNfF4KSf5dntHlDbDoTgmyBQ_wPrC2djggJoKW0vilE1Ozch-q23gd3_KuKB_jKllGoHbSkCpxP01O8NgMMH7jvZjBLG04M2N_Qnzj7icFOrQHJpAVfUDLuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7cbf3081.mp4?token=ePymEQK68QpEofVDBTzyBjXwCJw_tXk30qiPkK8IlrBniNpAyW-WBjxEXkzsEYrugy6KQrekon8F7Z5_JomoahdkH2HwVu-mXGLZqh3f5x5-YFzgY5e2hAYhz9LbUIBy7Xt9teIRC5OGz4TwSdJXakBpD0F9cjYZfV7gTfJ1_ToFSQdtCChUmcpOc-h3v7AK6Q_dtXm81SdWPviOhU9XGPhtI-7PdrPNfF4KSf5dntHlDbDoTgmyBQ_wPrC2djggJoKW0vilE1Ozch-q23gd3_KuKB_jKllGoHbSkCpxP01O8NgMMH7jvZjBLG04M2N_Qnzj7icFOrQHJpAVfUDLuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته ششم لالیگا|شماتیک ترکیب تیم بارسلونا برای دیدار مقابل راسینگ سانتاندر؛ ساعت 23:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29904" target="_blank">📅 23:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29903">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyf1O2qFBzmHq_dpN24K8KqivfYy-m_taAmXceBl1wkTyTIz5VcSBrznkpal6pD9Rzy3Dz-ZisSBQzBBudybYRzW4twZ5GXQaqyWjD2S1ej6OwxhqGhPB8sBIUptjxLhhjVy4tKOxkqPH-A2LRrR6Ynmhb4sgFvr8ANbZQIxygPgxqe1zzUi-oF6ZT0V7Zqi3y1l4SpICJdGlpq7eAWKh6W_HP_luoWTrnIKUjd0jOdN0Qphigjwwkmr6RTkdQcksIWK6IzGaZvv8sbMT5qvRDNPcRZzgUYKyF9fhztB_ITjVQXMLoFUnvSeqTth4RwK9ayNK8HPKycpqKATBs5UOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29903" target="_blank">📅 23:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29902">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-ew5I2PUDaz2Q5OSwhVEt9b9MNNEbTvt-jjcrmPWVy9uwh3faZHLgsR7sWi8R6BK2XLxiSn9wvt_UDkYFl6a8oBpaQKcx0Xtt63T7xzLCkMqKSpUrFrGas_nKzynIacDI8pFDYOi1ShdtvHS1AkP7WP4r7J3CPWC4EyLfd0FI9yK7H1PzV5H_HDyQgzoK7KdegaSQiXdnCKiRtvUuGVHVCNyszbqPo0_m2lt3mbGyOvwT1mId2M67B9pVVUJK37H3qhIGkDtPV-3ekVJH2Nwt6TBUrnkWMCWxLGmvc66NVs6HXDJBPcEVBVd27BWtQv9CG04OTYZva2otDm3BNQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ مهدی زارع به دلیل مصدومیتی که امروز براش رخ داد2الی4هفته دور از میادین خواهد بود و دیدار با خیبر خرم آباد رو رسما از دست داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29902" target="_blank">📅 22:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29901">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG1HccKMDPiIoqaFF4X1dMusyT2R-zE59B6NHn7JxGKnEuPZYNQrkpytRN-Jc44fl2w08iZy8ahnLloHczIqSXHIdQiM4SvMw_rc-vRqSB47FozB1XCxSQJxafT99JQ4l1Mk_3-eipkyg6cyjL_Qx50vq37ovYRr7NZRgdkSinqG173pDr6UNKl7zCBKArJAIuY7IFRcZ16wRcJkMW34rhUs4nTzjUhk1sPgcJ4s5HogisBQfRMquLsgx885pqlZ4u50yv9J8vEPDsYat9_zFLUhrhe-L2Mv6MXnfLAro4X0WRQYWeyryT6mTgrdl3jwNm_28axk9pfy9CbjONj5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇫🇷
فلش‌بک‌بزنیم به UCL فصل 2017
؛ که تیم موناکو بادرخشش‌ودبل‌کیلیان‌امباپه 17 ساله بورسیا دورتموند روشکست داد. تک گل دورتموند هم عثمان دمبله ستاره18ساله و فرانسوی زنبورها بثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29901" target="_blank">📅 22:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29900">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzkkfGmG_oRI1PH97QiRFSc2K-MsTNmzQgfz5x7KDQVAFhCskDVJ69KvcsoLg3C2y2S0NER0JLUmtDnI4p-kNGMW4r3HqPKb-jgvd7J4EpauggJ2IYHVGDdAEsr_xzOWxiYCMFYFrTOk-8FXTPq3IJrZ2YVDjgY4bDwquXJ471GNBISi-LAgX2EGRtxNRYrXgvWz-FlLutiyDp0x40l1x5SQbeUlJPXn7infj7JWcAuoBmZcvWe1Wp5gyxKEntpWt6-8gpmwUblk_HuiUcjV1q1sgtx1ttk6NASoDT2jZNwvzkezOq-_-xR62eZpj9kreLgDFt1rXpoSO4c_5gQO8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش یان دیومانده خرید جدید رئال مادرید به شعار هواداران الچه که دیشب شعار سر میدادند که رئال کثیف ترین تیمه. اینم از حرکت دیومانده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29900" target="_blank">📅 22:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX4Z-5TuBvTvp0Ng9LdFtnZ6Gi-3kDhug_aeTV11BJM_nDvjnazFULm5LZfvnOxXwSnLJSuBOeImgoYgMJ4kAJ4sL7UZNhpHRMNNowXmz2TxXdVwJfiWEMQQG5qbIOynm74KyYy7UDQK0aPdANnkbZMQvhh2AHZtj7ZtaTOVOpM_nL3xxG1RPBocQ5Z0wk4hujSVtqxEKiExN7m_L6ZSyQtiIeiS0g6OFE3eujI9ISlWgdb4g4x-WY5yySN9PzAzJum7-tPltC5uCdCjetQ9CA-bHrVE0Ttc3eBmD64z96XyFuFityDch54dMjJM1eP-n0mzTrv2s5MRc4nS65velg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته ششم لالیگا
|شماتیک ترکیب تیم بارسلونا برای دیدار مقابل راسینگ سانتاندر؛ ساعت 23:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29899" target="_blank">📅 21:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvJI7VD6VHcIjAJp-h693styN4lvEaDwYNtSkFF8OheA4Lio8TG6wkvEY6ugIaRaUeL2Mn0Qn4SYOrdUD9PH6qsIDQaa95jKJbd-a4DYQlxX8WVw3AgpkyICBkpSBTrrcywRjVS-jWzM0sL2zgm0W5eoytuLcjz-43G3lYQEZ02pCUS-8bxnJnswiMdSkyFll87u-FuxU1kn2XXqWp5vjEaiWkSPoHfzGnsgakvaa2CfGIyhK-nXpwt-dApA1caUR24RbWWXspHrLyReOlVsj2dKl_bizs7BsiI4BvDX5KPCYnz9Mmin31nR3X1TbDGpHpUrF98jymykvZ7IqyZgVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29898" target="_blank">📅 21:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29897">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcsV9vPaVIUgQ7rQ2v9YNahWbNg-VwByWVmp39bHSoyd2-V59jzOHwLwriqcymbRpgOVFUk5XAtzm2Uh-XBCH5wEnM9F7-oVR5_Nbx6G52KNoIMZS7SEHxzO-YKjzxauxpJY564_eF-uz42xRikgVnoyOky6ZdZd6irHfkeUIl66xJVhhy0HfGXPuBeOqKx9R7GV2T-UcbzHLgFwNW6lIGrw_4hUbNt3qk1F1ivo-vF2HUFUoeIMP5VyYRR-bEezwWcd8px4FkQekA5nvX_V_TShijo0UIwcs70fHZthaZXMjE40kT_rtKdxKmkb78GyQuiA_MlY-Kp8YA97UlYj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ رونمایی باشگاه پرسپولیس از فرشته کریمی خرید جدید خود؛ کریمی از 18 سالگی تاکنون درتیم‌ملی فوتسال حضور داشت و بعد از خدافظی از این رشته به تیم بانوان فوتبال پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29897" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29895">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmoO8WaoJJTrb-lMvod_t6rErKjgWIYX1aBLvDIx1DxvxknnHvvdawNEag-XEGTU0M4kW0jkQ1yvsgOYHTQg6NkBpRRfhZuAt__sylK8yMz2ID5u846CZoaatfzYBMTH0AqVp4qQdo1LTl4iRbKcL8CplJH4NxsrMHXAW9PZ_OzdgujK7hWGProE7CNtedp1NrQsV_1H888Ph9c_UsWwygbblLLgs__Q1f1InhxViqEJVZvTyZEut7yPmEnE1zambLBP1e1RXAZ6tAWsxjSsgpAj2CvWv8UWWr57WCjHEPuJ1gNxghBc67vgKkpNRkXt8elqlkJmZwz6Rek1Loo3Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ یکی‌از مسئولان سازمان لیگ امروز صبح به‌مدیریت‌تراکتور اخطارداده درصورت استفاده ازعلیرضا بیرانوند در بازی با استقلال در هفته هشتم لیگ برتر که روز پنجشنبه 16 مهر ماه برگزار میشود بازی سه‌برصفر به سود آبی‌پوشان میشود. اتفاقی که سال قبل برای سینا خادمپور…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29895" target="_blank">📅 20:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29894">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nA2qVOnvnP-nKxgVlG160pifUFPm5uMX6tdjjGI7LIoET_tUdjeksLV2_hfu1rjC_W6hMHG6yT9RXdLoJuTtuQ9bYUXU4CmPcvcagbrT6qpu8gOBeYvS959HNt6UzC15l5MFJJ7gajUC0wqFe7vGYp1DhgEarP0lLimAsbYR7XyA-wPpZenJv0ELxvJjeKTsIzwa-S4gsW_a9jE2bRF1Dxec5wlWLjAO5dbzJROTdYI4y8UmBCnXjH7y7-RB5MpBbm6MHgbIVxP_3CS5ng9jU6PLxWiKJaAH2yb6YqrhfVUUhX4ldiezucc5VH-ciUQHZ1cRokpBAgmUPcGYD5Lhew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیسی‌هایی‌که درپایان‌فصل قراردادشون به‌پایان‌میرسه: پیام‌نیازمند، امیررضا رفیعی، حسین کنعانی،دنیل‌گرا، مارکوباکیچ،یاسین‌سلمانی، ارونوف، تیوی بیفوما، ایگور سرگیف، علی علیپور؛ در این بین گرا و باکیچ قطعی نیم‌فصل رفتنی‌اند. اورونوف هم احتمالا تموید میکنه.…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29894" target="_blank">📅 20:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29893">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HILbmyK5hihWRQPE_K6tTYs2GUgAQXwUq8wjLnKlb6bS5QjlxBy3QUwvJtKyFRKb5esCjPkbXs9GuUCB6dkBwBYCYaEfZVHLBtTrZ0U5C-GVoJWf5kpTqqxhR-tnPyaF2EmTeKRWarFCAgZCE91ecauEVeFkzN47FUYnJIZwAayG6vWM8vjG9pRwaQjui9Yz6Ez4ZbNOcGNj3OLHyJ-B6vqLZ07VUtkQAzs131wBnGZ4kkpyNa5pUSC2tA-AA8m2G9XIcF96my4Eagvd1RpBHq_xXXB4cq0smTzeYXa0qLEE1Cta73P-WEZ8TTLKfQoZ0d-JR0pzj2WH9UvsUx1Qyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
رئیس‌سابق‌اینترمیلان:
سال2012 خواستم به هرشکلی‌که‌شده لیونل‌مسی رو به این تیم بیارم. به او پیشنهادسالانه 500 میلیون یورو دادم و حتی معاون باشگاه رو هم به اسپانیافرستادم‌که او رو راضی کنه که از بارسا به اینتر بیاد اما لئو حتی نامه‌ای که من براش فرستاده بودم رو باز نکرد و آفر رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29893" target="_blank">📅 20:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paz2wId1lXrBecRDpItTt26HXoem70yN_0DXKEjjJBFfcPU5OEnxhjGD3ZVInfq8rMnr6w8l4a9ylvt5MuECItkXyiA7PP6H_kzwlSdQ0kfpQLDqw9FZO8bdS6YIHqqpDbIBiqS3OmsA09xlEwhlxwcGm_LVoXdCTxoL7OcfULTi_7lzN0QBnRC1u5XWd8TuUIdN7Iwk0TtEtVYKjxgKaCyiANXQOvJwLDUlwPVosps4Z--UTVzdAkpSo3tmlvixsi7VgC6GFWJUUJKzArsnt4jWraMgFJ93hOg_93etVqtu_9b1wAozqqMXJRq7taeXCAF7ctRYztKCf50CXz9m6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29892" target="_blank">📅 20:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29891">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRRr2Aci6lZ-mvbVfMkLcYjhZicvsG-xG1Rbo0IxS-CTMbwUGxJR3YrfXuMvHMsEON6lSZi0M8WEhWDUIwUjWkMT9DtTlbBm5CPX9mq7hUWKy1SnRzudD3foJN2khRDc-80yeDBqlyIyYhMVfd9yk0Y78c6BapN1noO_UlZa33LKcQfClzQkGhsjDxizRIXQJdKmdTlmltCJ0dpmtFTDxeZZhQXJtw_rxDE1OypmM0sClpyds3QIOs0HDS32XYflTlwfs-kbMf_Rr0xpfjNE2je3nZqf-aU04uhroieuH2H2JHCQ2xPl4I2QupUEDa93LBMo1A8DNudByYo1Qcazqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره سوئدی میلان: یه روزی معلم کلاس‌بهمون‌گفت سیگار 15 دقیقه از عمر آدم روکم میکنه منم بهش گفتم کلاس شما 45 دقیقه ازعمر آدم رو کم میکنه اون‌هم‌عصبی‌شد فورا من رو ازکلاس درس اخراج کرد و گفت تو هیچی نمیشی. داشتم میرفتم بیرون که‌بهش‌گفتم…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29891" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29890">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W58zsQq6ya1gMm-NeyNgPqY6iFZs4cpUufzWejXEm6CnwOTBaIBrE6LbiLiPpZkQao3tX77sdMRLad3EscTr06camy5oElYK69gJpF1cljSWIQKAvqjpRWS3JpV-Kk9jKpYcT2ULYwv68aeFQFc46v6yeDNv7lUNMdhRYbKLyCk0yxdDI6b9Q_tQMg4VQl8RiS_-RGxmPnq7c8gLGPF_-N7T3YnFiNrpd2X4TBHSztjETOvnAHOGYFVTWNQ6tmm-dOlRatnNN9MRTDnPNN-Jt7V8JMZ9dgqgVQ2sWeG7mJ5fSp-l18bxlawi424On4VduTCGT-TjrYPJQJ-KpcRgkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
یوونتوس در نقل‌ و انتقالات پیش فصل؛
سه‌مهاجم‌فصل‌گذشته خود را فروخت و سه مهاجم جدید گرفت. مهاجمان سابق‌یووه این فصل روی هم هفت‌گل‌زده‌اند درحالی مهاجمان جدید بیانکونری در این فصل هنوز موفق به گلزنی در سری‌آ نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29890" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29887">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1ChuR3yx_Y8oJtW86yYrviKsfjQyhvHTvQyHrTuaDmSsiyAs6AHBLoXeXJXmoIUjuLJaray7hNPFMWeBjwkX3w3HGfAANEoyJPSZI3vaxf16jM4RFLGPXFpGCp4dY9kcDIrISSAQrNDLNJda9nBekx_20uCUZIiNK0sZ8g041sBAEX_90vswTa5LtwRhWy49HkiI6Nlktn8vw48xAR5VYGAmBVdo8QBQ4ed_8u8A9zTBLxlUvUGlbaON8GKIV9HzvoZSCeMBMcmwciEUTfxCmqFiDpTjc6L784xCgqRwvg43mXQNDtCw3zRjIqwk3h3B1X00yLqCf0VNQBK2fqcJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
وزیر نیرو در72 ساعت اخیر دوبار با رسانه‌‌ها مصاحبه کرد و گفت دیگر به هیچ عنوان برق خونه‌ها اصلا قطع‌نمیشه. همین‌الان برق‌شمال‌تهران رفت تا دو ساعت دیگه! با خودتونم نمیدونید دقیقا چندچندین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29887" target="_blank">📅 19:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29886">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDti5yAQV-m6fhpR8LXcuf9GkwZ-GUXEbheiWqjH848L48nP1DAZGaU5KRjDlFi47cFgrgOPFo7b29pzL0fZ1tPLIl0W84XC9Q4EtTFGbK5ipDJ5dIIurnk8PQgfWo0piSNdpBJ9DZJIDmlbUUBAJ5Tnyfk3m1S34t45ef_CkB3r_n2XpEyZ3APNLUyuVJIFOLSWIzqG9KfQv6tmuv-BU0x0D9UbSVgWbY5VX5jkkYpx2cAemM46G-O6bhPRMyuB-YfdMUCtNKWYF2ekxrQVKoLBDJVQKODQ5HiBZbJYhy4GXi0nMjUrIy3GLWEmmGk7M-sjyFObLRePu-JLNNz_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29886" target="_blank">📅 18:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29885">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R52eR578eXpklm1FBIV1GRWuBM4aIO-6e0nfOOgLJY7Djt-lnr2aaMd3UOAjbSycLY4Cmx9ykppCNjhCJn_KPCtgnOzWropd2a3igS-h2s_I5ZFb3x-Z5owrydKOGbXe8om8svqCnBQA6QyT6ZzbEFOrW-wfyoD9WFFAKAbNqLw1Zk-zI56rk5hGkmY4eCG4JewKaIO2179qu8N6QXpQnUqgUHfoJOX1SHLXa-coksuOTdDILptnljc4ZQcDL6btUJFk7NvRKq1nF9O4pkWp5uqJWDwf_qw_vsJK98LKIRC8poIIMnaAkwjlUigI9RHu6Z7BQSL_Q6wOgAFJqmKo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس رونالدو: این زمستون رو نبین ما هم بهاری داشتیم. افسوس که نامه جوانی‌ام طی شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29885" target="_blank">📅 18:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29884">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1SZcH2z6WMjk9oPYn-QQ-H6VY6KAb8-t54_3lAbsbv6qIrW0scf4JKYmI-hSQEN__-nejYfkb6EfSQv3eWfK9QDbZ5fjbD3Tw1zBjnnaFtAWK6HRdf8pmHmE-0uVnXWZSCO5m1AkRc3X4CSFg9kH6kVPBS68haBB6JmNbQEGsy0TlCiKQrXzlRz9ux7DRhiUb0k3mfLlTnHfsEthevUQqs2n4ptKm5j_oOFBDB_ZHyfkhPc-qZUSlcdMU-pITpJk_kiM_gP90rKBiz3-BH5_EUGAxVrUhb_IHkyqFvv56nIcmiVEwSbpVEl06OKh5sPDkaaY64IpOM0L2M3CJJcvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور ازابتدای‌این‌فصل تا کنون 17 موقعیت‌گل‌صدرصدی رو در بازی‌های رئال مادرید از دست داده‌که باعث‌شاکی‌شدن هواداران رئال شده. پرز هفتگی داره 600 هزار دلار به وینی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29884" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29883">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6de055e3c.mp4?token=Fe7a-edlLs1Ua-w58ITKRUGhKuYNgChIaK1cFyD9kwRRlF2Fr_-4vQCN5kQ4oXq4D5XBQRCv_VzabJEQhOrMk2KhYo4gPpCCQVNHTBt1o5uDk8hyzoBzsJNePAdg7Qtj81t8vcjcIXu1AhS6352wDcdtDpfW6tOV3LqBgqwbsHUUzP3bYZsAzySOAcnMb93Cv69XtEgZzpld2y-rnVlB_cR3oZee0oalqjs76rYIyQuCluf2rMVjP8yveduwfxjaoJREV206eMJeApEtynljULj2s0meVlV98KEID-i72p9xC8kduFe8g-8qxn7ifiW5N5B7O5WULApapxeWQ0jEMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6de055e3c.mp4?token=Fe7a-edlLs1Ua-w58ITKRUGhKuYNgChIaK1cFyD9kwRRlF2Fr_-4vQCN5kQ4oXq4D5XBQRCv_VzabJEQhOrMk2KhYo4gPpCCQVNHTBt1o5uDk8hyzoBzsJNePAdg7Qtj81t8vcjcIXu1AhS6352wDcdtDpfW6tOV3LqBgqwbsHUUzP3bYZsAzySOAcnMb93Cv69XtEgZzpld2y-rnVlB_cR3oZee0oalqjs76rYIyQuCluf2rMVjP8yveduwfxjaoJREV206eMJeApEtynljULj2s0meVlV98KEID-i72p9xC8kduFe8g-8qxn7ifiW5N5B7O5WULApapxeWQ0jEMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق ستاره برزیلی بارسلونا از تو این هایلایت وینیسیوس‌برابرالچه‌حداقل یه هت‌تریک درمیاره. دیگه خیلی داره به "یه‌ورم‌طور" بازی میکنه. دیشب داشتن سه امتیاز بازی رو از دست میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29883" target="_blank">📅 18:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29882">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a7515755.mp4?token=C0F97XdMjzC4yVBmoXNelDh8AXgTv4F5iDPhomKrS-X-pX1Vx2sXauVFw8F7rrWMuY14NtKP81ahFNEgpacNk1ZUUAGZvTO7Ylj2GXmEwcZR_8pNqXGMWzCYItab9jurdbtAJvaJPgFlQAui_VIpTrfzOnwUypbYWPnh3RGCIQeRYygm1WOEN0J6F3LL9ClTMKQ1MMWldpWWCjulIkBDj6vwdav-PGhyH02AUzop_8fFb0aCobEUya3mA-C_Ysa39S_YTmAuqEfZ6Qp3kFIytvHAlkfT4JDYrzWfQ37gNiP9QmSiUyhainp14p-gUM1T76LANjnf_ZV72JmJXwhG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a7515755.mp4?token=C0F97XdMjzC4yVBmoXNelDh8AXgTv4F5iDPhomKrS-X-pX1Vx2sXauVFw8F7rrWMuY14NtKP81ahFNEgpacNk1ZUUAGZvTO7Ylj2GXmEwcZR_8pNqXGMWzCYItab9jurdbtAJvaJPgFlQAui_VIpTrfzOnwUypbYWPnh3RGCIQeRYygm1WOEN0J6F3LL9ClTMKQ1MMWldpWWCjulIkBDj6vwdav-PGhyH02AUzop_8fFb0aCobEUya3mA-C_Ysa39S_YTmAuqEfZ6Qp3kFIytvHAlkfT4JDYrzWfQ37gNiP9QmSiUyhainp14p-gUM1T76LANjnf_ZV72JmJXwhG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29882" target="_blank">📅 17:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29881">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14d489d5c.mp4?token=TYZ7Gxj1n2HHuoor5WI5S9LPnW31O6k6VkWVYse7SOuc4fwqUe-3VnJ2C_noax80yMpAxep0h7T-7-5IDSJho1MvwvGbVMDJHV8-jqvW2jfTgBodZqLCPt8Pmi5_arCoGXNY3XGQZZ0on6EDf9URS7pTwK6m2W7bTypCvDLh0wVRBxbIHy6rDjRSog8jx4VDt-aOxdGhNdTTh0FsrVo7wjH_zI22BH7o9z8j0gbZHmuoKNhYKM1SdestBxmC-XGhrJr_wrlwvAVmGbao_GTogBzpX-T360JjBCHw9vEvYdaikaNVkyiWLyKlrGiMvYo7ZqrZyExExG3uD7oO7zWIb3SQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14d489d5c.mp4?token=TYZ7Gxj1n2HHuoor5WI5S9LPnW31O6k6VkWVYse7SOuc4fwqUe-3VnJ2C_noax80yMpAxep0h7T-7-5IDSJho1MvwvGbVMDJHV8-jqvW2jfTgBodZqLCPt8Pmi5_arCoGXNY3XGQZZ0on6EDf9URS7pTwK6m2W7bTypCvDLh0wVRBxbIHy6rDjRSog8jx4VDt-aOxdGhNdTTh0FsrVo7wjH_zI22BH7o9z8j0gbZHmuoKNhYKM1SdestBxmC-XGhrJr_wrlwvAVmGbao_GTogBzpX-T360JjBCHw9vEvYdaikaNVkyiWLyKlrGiMvYo7ZqrZyExExG3uD7oO7zWIb3SQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت
؛ علیرضا بیرانوند، داوود نوشی صوفیانی و فرزین گروسیان سه دروازه‌بانی هستند که تا پایان هفته هفتم لیگ برتر موفق به ثبت پاس گل شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29881" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29879">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Utuex_a_ANeu6HGDsuJ7IfnyNHMCgCtyNWRNSmZkm5FdbQsScxww8kCUrVLglsUmCqGAKDxqO6gemXdm0ivj_Azq9JIzrUuwUggUeHEURh9WLNEenvkbLjzuokMbHixfb6Im9cotzOnMWDOYNIf-WdO-DO2QMZoryB5lEjppK_YTngyS0e-MADzoIvciMrIzyes5jG0p9BSzBGM1ukOnLaa_rkUvrYt47FAZVZXmua_bBCZE-ILfHSzaB3ktZ4wMDz4HglaU9NlQfw5C-46ymQl7Mv2R4wcJCJk5zhm8X_VpOCAYkwoK1vkmRS__fqFSK0p8wroiW2Yo2IOgFSSHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره سوئدی میلان:
یه روزی معلم کلاس‌بهمون‌گفت سیگار 15 دقیقه از عمر آدم روکم میکنه منم بهش گفتم کلاس شما 45 دقیقه ازعمر آدم رو کم میکنه اون‌هم‌عصبی‌شد فورا من رو ازکلاس درس اخراج کرد و گفت تو هیچی نمیشی. داشتم میرفتم بیرون که‌بهش‌گفتم روزی کاری میکنم هرجا رفتی با افتخار بگی زلاتان شاگرد من بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29879" target="_blank">📅 16:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29878">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltBCX1xXLJYktdvEGNgkp40J2FTulOnXHRVQ0D-wSzxXrcpdul8UbinTVXCV5B6pYDwIRscTCZPueQyI7ywBalWnyLVR1meRzkpy4rz6vN6yb7Tw9jvfoprWDcHF4RrfsJxrtzpLcYCXRnadUGiGBnptGEKcPKnKk4Q1skkBbEGd-ut0CEVmI4IOiTia1nICO0k0jdCNu8n8y103z-p05KlbSPMXzQfIa7HIpiYDUrGEOepI6eo3gKKSeAd5aYml6qtNCFZeMVQcNfa4pIl1oqhs8I-BmBONomOsYTI_JbLBrvLDXOs_6If7zHV5n1KJEe0QJlRI9nAo70C8gQTVhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌معاون‌سازمان‌نظام‌وظیفه؛ از بین قایدی، حسینی، قلی زاده و جهانبخش تنها کاپیتان تیم ملی علیرضت جهانبخش معافیت تحصیلی اش به پایان رسیده و باید تکلیف سربازی‌اش رو روشن کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29878" target="_blank">📅 16:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29877">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf87MZ2OL1TQR4cSkxAKjb0ymmoMDOMf_YHe-PyrSGhjSx-Lne-hF5CigwSchuzkAIYN_ZU_5oU1o6ShTRXn_y3V5TqrFXZuy8wFdMBTa4h51xTqxAQ0wYsJ6o6GbY1V1R9x3Hh0EP9BoY7-_FHEfJJ9cew03qu1EReF62vsOcsgVlpRwNp7TcEVay42-5XyJJpoJeXxJjYqMdGVnM4Vb_lsNCxTWjfkZm4UBNWSQiNuLsYodabtadNqcvil3_VCn_qammMC1gqerXyuNrWpbG6eKZjeFxqYC8JUKytFVrwvMypFO9TF-1YzjRvJTJIn8BlyozHUw_ysCslbACEHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ اگر یک ستاره هر فصل به مدت 19 سال متوالی 50 گل بثمر برساند درمجموع 950 گل خواهدداشت. ولی‌کریستیانو رونالدو: 979 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29877" target="_blank">📅 16:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29876">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owgrbg0cFAmSdBuYttNyhlKVVWd0I-u9dwLuNij0GsISiUmaH8jQOK6OlHMU7Rrb-t_nNPEmiPUYPxXwZn7OlnQZ10DRGgS0iEJa7Wy7JqLyiBzWsnpU2Bg8FVs09TNDw6YnAguN8VC81DuPK9FA-U-8d16aKclfpAp8ccMqFoKVC324j7qTsbKb65Dl3TZlB3yW8lFY73DReytlgxj4WBoR9rqtNjDssd27Vrv64YewomZ-f001lw3GCm9MVvYRwvI0fN91tmwCxE8m7dn4obJ5eKk0kEWy43xH7zpj2CVXxQ06ozm7sYfLVe6O4kTFLYFF0PCsSKsOerDGtLfydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لیونل مسی
🆚
کریس رونالدو با پیراهن دوتیم‌آرژانتین و پرتغال به مناسبت خدافطی فوق ستاره آرژانتینی تاریخ از دنیای مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29876" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29875">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-AIT1BPZ8T1b3OOQtfG8lOX0mVWw43sb7xoLjCwMMnXISR8lMpmCY-k9MuBRgvncfsy6CqEfwlFrsqoYEV6bnpfMjbildwRLLxE1NBLXNjbxgvmVnw9kNPw9aU1ccCS10QxYO0j6W3TyuPTCnl0-VT_GS7kcb9Ytdg7HJ4AEA2g4OwaKatOQ_1lj7bbVPmpLM2oQG080suFT9rdhQtAx3_yM_nRs-RRh6yQYnP3rqj5ub0W5T4gtbsU3GB44zxO9umxEbzPo0HxbMBRU6kHpNUulA6NOPq8KsgzdEaMwZOpyYftVI-0xbNIhu-sfJ0JXMgCCj2rUMSgGgaxagx8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
دیدار گرم امروز زین الدین زیدان و سرخیو راموس دو اسطوره تاریخی باشگاه رئال مادرید بعد از سال‌ها در حاشیه مسابقات جذاب فرمول یک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29875" target="_blank">📅 15:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29874">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO4jGbua6eV8GP7MxEGIEKIp8ZCmvJKyuwepzTX8R4BekZm-Xjk81bggqcGap2WIqqmSqIPaoJXYOtNqmk4cKczPsib6oJn9dZZ1R1DIs5bn75Q4Bc1h9IomPlXks47jIlkZ9o4C6qjv5zyf4nT2xmGvhbIHxHlEmfiofiQSOKFCyl4bvYoqhL4AaXqYvJKQQc0HhJlHtxsiSvneGlU1jxJWEa2VAbXKAUOcMAlyMhclv7ulKTmKHrrSmBGGDyDpwO7P9p5ZpRbqRKVvRbI8TFTha2NrU1A2Z1vErdOjZ6D0oWdrJtTLNfmyq90sGQPVqdsHOoIKCPBFKMgq7L1H4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فرعباسی گلر استقلال‌که دربازی با السد دچار مصدومیت شد اما به بازی ادامه داد حالا خبر رسیده به‌علت‌مصدومیت از ناحیه‌کشاله ران به مدت سه الی چهار هفته از میادین دوره و فیفادی رو از دست داد.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29874" target="_blank">📅 15:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHsgxYSBianWCEP_M-prFpkDetpBPvJUs2BBNDsDdEjkHSeHqAlzgoDJfhOfWWPRUsso0tI4IWZfGhdp8OGWIgfv6KyfLBumR3j6It_jbpHQiwECPsuMfDmlC8mRietZPSBrv6DnFgKwyH5Wzh6shaE-Cwxgegt5W-9HczGdiojVukv1ThccuJRZ1hVIHFJ07TaZpf8FsXxI-itBI8C-ihAnzShvTGXQTXKNLxMYPJc9-iPxXw51zIyUgv33GULHr6S9x0kmC2kCRdZPpXTZgQeCR8SxqSPfPZUV32GXA0soJDv0Q8hW1GxPPt__BX-ZDZcaT6-Jz43QJsq-cU0qMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29873" target="_blank">📅 15:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29872">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flRs-VKEfqmH40Nyhte9LZ7WrSMSeupT3HXS9I7q_1bdjF_pFGDDKDEYrNm-rR9T4pDxFoyOnIIYxnUsx30guDnvZxAru3CCkXpoUWcnEU9cWKkPonHWZqj-dGJgWUQ819fIHvLB5ojLyVqWHe-ye_WmDn6j6JziPBYyY-gtjLxGA-2gRejUcki3gKJSZEp5vX-oGrlEedqkvXMX8snaJRZInR9x-vEBafxGPy5TGLa0k3SBP81tzXJGiN13O8-dUSW78mpE_d9R-Ac3FQsCTHBejko2q08TeegBHPF7m5vln10jubijnoMy1Dq5mpCU88VphqXYDP57l-T8iqac7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته ششم لالیگا؛ شاگردان خوزه مورینیو دردیداری فوق‌العاده سخت و نفسگیر مقابل تیم قعر نشین الچه با نتیجه سه بر دو پیروز شد و سه امتیاز ارزشمند این دیدار خارج از خونه رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29872" target="_blank">📅 14:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29871">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jab1PILYaMgc2S8LFY1UvxFKhix7A_BwmmgjW3-3KlXrWKunY1Ye1tSKqcgAwKRTeftcK-qoJifyRaefqSXktDPZjF5iJKIgHnc9dcmmbeZLcTNoJ1nKdmm5Ai233bgyWAObTAjcpZmmO_5Y2bvmCJlFvghbr1IrXUGqsbtzXcSXxEUklP97xOzKAsfbk5aESbbQdCalfK4hwPwhe-0e37L8QeE3QxcBNf5whBK-JzB_CfbOdeTfH5ko-F_OHbmMn9e2uQPrQFigkLJxgwaTxcMjMX9ZMhRmOqiwxrPDH9xslZ01UvwrgPCjuD2GLrOu0XFQCBcwmC27cpjsx9BENA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فرعباسی گلر استقلال‌که دربازی با السد دچار مصدومیت شد اما به بازی ادامه داد حالا خبر رسیده به‌علت‌مصدومیت از ناحیه‌کشاله ران به مدت سه الی چهار هفته از میادین دوره و فیفادی رو از دست داد.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29871" target="_blank">📅 14:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29870">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق ستاره برزیلی بارسلونا از تو این هایلایت وینیسیوس‌برابرالچه‌حداقل یه هت‌تریک درمیاره. دیگه خیلی داره به "یه‌ورم‌طور" بازی میکنه. دیشب داشتن سه امتیاز بازی رو از دست میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29870" target="_blank">📅 13:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29869">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoXLaFD3jGyLd5m1D0WJe988ZQ3-XzpSzuGZfwJBh3rNbiOHY_rRaxycl-Q9gMjXOUR37HY0u2MOQcWhTUr6E7mScuIE1JG-nbF_s7K-kgD5jzcFhXe_wIumjYwV5SrbJxOM_2YSX_5eG-HfIEsByKLYw7SVP3VZSEzhTfOFFLzVNf_Poa6ZqaDWfEx1aBzAxg8yAeiNphksQh3xWwYUudB_fAxTir-y8UVsBs5ILGYIfYuWLQZo9ziUcIB5Gkc0rJk1FJUCZJcP2Czm9wNkw7PGH8JmgoVvY7mUi51p2F5JNgjtw3feafCIMzprrY1I104uJGuBRjahd5Ewcx_sIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
سهراب بختیاری زاده نام دو مربی جدید ایتالیایی و پرتغالی رو به مدیریت تیم استقلال داده تا با یکی از این دو گزینه برای دستیاری او در استقلال به توافق برسند. بختیاری زاده اصرار ویژه‌ای برای جذب دستیار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29869" target="_blank">📅 13:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29868">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpgvyLPZG3PX7Tn94U7zvrcayAA1tqXGpthGfixjdJGSKBOuksVugk758xpxphnfTDQ2AQmOJPuOonBgQHiaEvDBv5Mjq4wXzLMWsLA2mXUL26vDa67YNiMyvJJgcXwFmd1k0DgGAyc4Vuhy8BwPKGqO10VfeU-BtVa8YDvPBcnDXaJ7Ti5a_2_MiGL9UbtzMTUlRcZCku9Ak7CsGsBHENl7Z7vS-6dpXnQwtqP7KeF6fZKMFlx9Pn2OXbPR6rgpJAwcSiRvVkkBUc2KaeCegnJqZLdRnN8Sj5e6zN3mVPqhixqHy7hnV7D8j64GoYM0IZYSkT4Cttp8QOORn1zY-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکرد حبیب فرعباسی دروازه‌بان استقلال درفصل جدید در تمام مسابقات: 8 مسابقه، 7 کلین شیت، 19 سیو، میانگین نمره 7.9 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29868" target="_blank">📅 13:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29867">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX8mfiNUjrBY46_ln8ITK3l5y4CiR6V1vYsOhLFt8F8_BQIzzenIH5-8XHXQ8iPaDm3dtFKT5lclAwv7tbtvc3OIITLdv2ACMHQ8RWButLmAoWqhcWJE27-MTe2sAU_hCyRdUNY9Q6UhujHE2dWK0GKUqJeqW-WjbvciOGHYjXQTJRezCZ7iHoshh9JZSWkJezXIcHGEkkHGQpS3GjFZWx4cCxqJQ7_BXCVEwfkkxUgZ0lVQsvtpgvdAzEGG2m1pn14rmFTXShteBbnoGalZ6Z4F3-i53D-0TO5nOhKo7pE-Ft2Z4AkXui4C7cjTruPOEBYDu_wqeAGNbPuFXGrSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29867" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29866">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b508f4860.mp4?token=uj6w4Vowvj2lm1uN2hDvS2RPmMNnUyca3x8pwx9zkLL5koZpggXzGu9-dp6ZjZk9uBfaPzTxLYVEYdo_wVPH4d6W14KWeI6INJMUVDC4iRzwWKuR9ZF7ggI4m-3edff0rf4XNow7EzRQQbtw1tIIzLzVozwrAb132n-b6x26pSdW8Vk2TI1z9hk0-iVjTBfx6SCDap3TCFxtSb1iGZlFQDIr9xfTiN28PLiX4iIliKU3SqmrS5cx5ktUoqT7YLyhsG3tWZUjNQ14qDbcGESfI74avFr_YRpnb36zUjKQzXJVD7v7K0dc2UrRRYTex02mIVXIbt9OSkEmQX3dgpRYjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b508f4860.mp4?token=uj6w4Vowvj2lm1uN2hDvS2RPmMNnUyca3x8pwx9zkLL5koZpggXzGu9-dp6ZjZk9uBfaPzTxLYVEYdo_wVPH4d6W14KWeI6INJMUVDC4iRzwWKuR9ZF7ggI4m-3edff0rf4XNow7EzRQQbtw1tIIzLzVozwrAb132n-b6x26pSdW8Vk2TI1z9hk0-iVjTBfx6SCDap3TCFxtSb1iGZlFQDIr9xfTiN28PLiX4iIliKU3SqmrS5cx5ktUoqT7YLyhsG3tWZUjNQ14qDbcGESfI74avFr_YRpnb36zUjKQzXJVD7v7K0dc2UrRRYTex02mIVXIbt9OSkEmQX3dgpRYjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29866" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29863">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7cUl_-AgAT_pkFC31k4o38bzp8pLZk9qjt2Ak-3iRUFXRMqztNxzQ2W2pFj1j18TwHOy47zft0FrhI94mhzhKo1ShJ59L0_vgT-aSoPAkUImu35bpg8zNC8qCsPcKMsPY-R4oihq1-jmF9UvLaUllLZtS7MCt1Y1vo-eINgTi97wllSnJBI1q2wfnlpoXnUB-rbmStKyL_AS9NeRdopERe_1_i2_aS5NfTU4VWgXmKGcoK8alaBCiONnMpGWQBG_0Uzbxpk-VdzHdzgB502_H-juVSi5dmkibwIt5ib0PqwxjO5Kgtt7Uwltz-9L0CJRs3PEgE-jo72AQsJ8NEoaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تراکتوری‌هایی که در پایان فصل قرار دادشون به پایان میرسه:
علیرضا بیرانوند، شجاع خلیل زاده، محمد نادری، کریم آذر، دانیال اسماعیلی فر، صادق محرمی، مهدی شیری، اودیل خامربکوف، تیبور هالیلویچ، مهدی حسینی، مهدی ترابی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29863" target="_blank">📅 12:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29861">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSd9DjKCGPodxsgvgtt8O4-p6OYSZIGG85Cwey4b22LHaqeAjSZROg55KMG1L7XxTvu571WSteoKYG9HmTudFNeiI2lcWgHeQaAz6ZGNhi76GMto30XqqbX_ZpcDVd4SjZNlUox4UII3Ys7ta5E7aW0uPSuFQJceMRy2uUcXsBDkblZZxkP2_orKzrCaotI_UrnUEsvhC3rk-CYCcWb928hV1boAGO8qedV7iBcmI0_NmXQIkNeeq72AGGEM2Cs-HXEHNKvRTWzANXMcK3zwxYFWigw7rD3dOkZAv4l30jfUGfNmU93kmmj9OlvcYdRGZdMHyI7-vVhgf1KcgdDWKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپاهانی‌هایی‌که‌درپایان این‌فصل قرار دادشون به پایان‌میرسه:
محمدامین حزباوی، آرمین سهرابیان، هادی محمدی، احسان حاج صفی، ریکاردو آلوز، آرش رضاوند، سعید واسعی، مهدی لطفی، کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29861" target="_blank">📅 12:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29860">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCOWPf6MQpuuQBiCe-EALgpI5ucdHSNLxyZmU6trX2_sgj4KMlVJwZrAhynxh9GY5kvroYGKTTg1lfuMEsIm7FDzuqjz_yWGFmVAUK47VXvhDCYJt2SEMNVGE8Fsi8uDi6DOq_zPelzhNHwDrGUWJfRReufC9aZdeDKO9-1VQDauX1k7wJfJ9r-9N6uaUXfXVHezioHewxVFmynxO41rwePETv2X4yjrUfjOJai1cKR-EH148ijAOLFL9re3Qc_B5KZX63QXQ88CTtyRncJY6jthBnWGpgmT1tZGzDktXR4ioPp-1V-ridkXHKfFaOmnHdwJ9ZoWsXFOHHL2afzpFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه استقلال قصد داره در پنجره نقل و انتقالات نیم فصل قراردادی‌ جدید به‌مدت سه فصل دیگر با یاسر آسانی فوق ستاره آلبانیایی خود امضا کند. آسانی از طریق مدیربرنامه های خود موافقت خود را برای بستن قرارداد جدید با آبی پوشان…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29860" target="_blank">📅 12:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29858">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSrsN4m2Rx6w4G0oZjl_hYRadXYv1p6UrQS1RUiNIQ4ZV5ibE257mo4wqqPRCldbYax5lOuLzUSz0qgqGwCND-Bxb8-82fsBdwohKGKrvwxQYe1OpUihYnGsMMj3qdPEat_GOG3c5rCPmVNeAfL9IR1oyWghtcv_T799AShHatmEaCslhEPyclXCiXB1UjBuEMMkSZxfdCWY-gzKh-UASbe0o8X6p5UGmEzJCFA2fBra4rLKADoDdquhSyROetjHipYTMX7AvxpKy3JKWcmsFCYzK0wHorNKymy_9CvdWwonMeGN6E6SSTgPxWxpyQ9k67R13bBHtruEmL57wL6C_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیسی‌هایی‌که درپایان‌فصل قراردادشون به‌پایان‌میرسه:
پیام‌نیازمند، امیررضا رفیعی، حسین کنعانی،دنیل‌گرا، مارکوباکیچ،یاسین‌سلمانی، ارونوف، تیوی بیفوما، ایگور سرگیف، علی علیپور؛ در این بین گرا و باکیچ قطعی نیم‌فصل رفتنی‌اند. اورونوف هم احتمالا تموید میکنه. بقیه‌فعلاحرفی نزدن باهاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29858" target="_blank">📅 12:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29857">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/so1g413GKVLLXjuqnN0ZrynTide0v_mzkpaYkg9faEKta0vV10U6QkzwCa0oIoTlnbA9S73gcW9s6gLab51-oFkf93r-ZaPH1FGP-FdTptybuE1kNEZnt0AmnfuYQmyoLZTF3o_Djb7dP8DqdgD4ijaiKLKGp19RXautmmvdn2pfNcX6o7uNoSLwMdFmqxyz_h7-H3NV6hqCKcphamW3y_Omr-03_NZRzoKW8hP8EWZcde69_I-khGxkS-MXQHT_iC_GBne7yzLggkh5mJ4N1SC4yBtbAdAa-pKcJCkfwZCIFv7kM5Q1efYOs19YvLREDEF-jJ1r6vOFd_IajpiZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
فابیان روییز ستاره PSG
: اگه توپ طلا رو براساس‌تعدادجام‌درسال و بازی جوانمردانه میدهند خب‌قطعاهیشکی شایسته‌تر از من پیدا نمیشه. تموم جام‌های‌سال2026 روبردم. تو زمین‌هم‌همیشه سعی کردم آدم‌آرومی‌باشم و بابازیکنان‌حریف درگیر نشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29857" target="_blank">📅 11:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29856">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50dfd8488.mp4?token=CKHbUuTsRp2S0qw7gcOxuQCCg8lo3sBGwI1_XxIH2zJhCeMfX0ml8VgcjeOGkCLELRei3Qrs3hGqmfi1UyvTPDYHIVX4esLgbr-2-DGCfdbCdot6StZ1ZpxvbVFVEDewzmg_YnXPzFdWTbjnQxn8mNqVqFd-P_0v5vNFS2K3VttJ4Jv5bv5J3vD98GVjvqPXYGlLPY9d0UhArGozlySWlTqA3rwgRlBTzXfNyx5ZSkL6lWZ7E8WEP89eLhE2ufFBNwGrRAskp9VxwdnXKoLeoBRuUpF_XohBbMVtaGHeCp9og6LwRRc9PGzBV-33xeQf2JMGi6TmizBz3XiDZosi7FHd8nysmn4_arJF3kJG4942ODf0CzGC4eeuvIERHlJ2eqGofRN0JW0ZgasbZUxqla9dQ9P47HPuVcIcnUiush0OMR9fg7DEE6M7YXMGL9zdsSfznqmf5UnbJnQmcebdO5HOuaazLEwWdIMEN-3NlR1CPD9EXjz0vkUUuLXQusWphjzcRdKxT7YfRI4NjR-Eoc3IoGzIuLo7UfnkQdDPP1H0KzaXHtQZr4satA6ESeI-ATqSY-MslyMaP4ILHXanqwK4Ef_x6rfo73WsCQx2ODAHWkuWtXCD0uKQPxMIZGonXQg7GrUhsMQ59tvfAF4BiNgquWU32ZRE4f4_JUIUtKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50dfd8488.mp4?token=CKHbUuTsRp2S0qw7gcOxuQCCg8lo3sBGwI1_XxIH2zJhCeMfX0ml8VgcjeOGkCLELRei3Qrs3hGqmfi1UyvTPDYHIVX4esLgbr-2-DGCfdbCdot6StZ1ZpxvbVFVEDewzmg_YnXPzFdWTbjnQxn8mNqVqFd-P_0v5vNFS2K3VttJ4Jv5bv5J3vD98GVjvqPXYGlLPY9d0UhArGozlySWlTqA3rwgRlBTzXfNyx5ZSkL6lWZ7E8WEP89eLhE2ufFBNwGrRAskp9VxwdnXKoLeoBRuUpF_XohBbMVtaGHeCp9og6LwRRc9PGzBV-33xeQf2JMGi6TmizBz3XiDZosi7FHd8nysmn4_arJF3kJG4942ODf0CzGC4eeuvIERHlJ2eqGofRN0JW0ZgasbZUxqla9dQ9P47HPuVcIcnUiush0OMR9fg7DEE6M7YXMGL9zdsSfznqmf5UnbJnQmcebdO5HOuaazLEwWdIMEN-3NlR1CPD9EXjz0vkUUuLXQusWphjzcRdKxT7YfRI4NjR-Eoc3IoGzIuLo7UfnkQdDPP1H0KzaXHtQZr4satA6ESeI-ATqSY-MslyMaP4ILHXanqwK4Ef_x6rfo73WsCQx2ODAHWkuWtXCD0uKQPxMIZGonXQg7GrUhsMQ59tvfAF4BiNgquWU32ZRE4f4_JUIUtKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
⚫️
آنالیزدقیق‌بازی‌استقلالِ‌سهراب بختیاری زاده مقابل تیم السد قطر در هفته اول لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29856" target="_blank">📅 11:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29855">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3HLaXMP1xm__StUXUMAyBrSY-QwWCsp1GixbqAwhfs8HXFfa6-yclha_H8CmFyiGSVp9n8urbFXIXxKGbj3U2f4Kzh1Ji5xO6OTUi16LoDJzxe0XFUNccFeMzzVJAPK4R9KFxQZ1Hb1xFoPsqIxGKbcVklZbCZyGcETH4pPOJABRwjWIT6Ft3_JmB83di0QcUgFTWk_8tQ6BRKex26t_1_maouNt4JVOC036KLEiE_D8Z2YRmJwu9dObZeZhVGey8gEmPHMv_cDz6bYogoqojrAODnvbLm24ac8w6F0nGNuh5VG0nw411hjFq1kX7SPxE4BITEU9o7NeiBhb8Sczg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه اتلتیک: به احتمال زیاد جیجی گابریل ستاره 15 ساله منچستریونایتد طی روزهای آینده با عقدقراردادی10ساله به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29855" target="_blank">📅 11:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29854">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8386c27ee5.mp4?token=ELUAiX1nNyS3YD1LkDWjQ6DrJlw5HqJAcKSBE0Wm4oKOaUvYpmbZOzDK6YnsF35Xu2YraZG_NGiK-E5Sm_PtrUu5iUvuiuM4U7HiyaZOcoMRede0xtAvdyQ-3U2aJgQTqoMolR8Lf3q6CBrhOQsSqsBsghIq3mcqaAWd8c3yrTR7AuwijdhJkg15TMer_L5ghiOFp_QEDI_qgBxsUzTZv1iFem2XMH9fGEZxGo2OhcLCRD_AeUy9N7rN9OO2P0ZDq8cXClYmlWafSNkprhTpc17oWoF6q4GO0iMfwPBe2zq82OegOHG_c-dyDch_3y3RgPWhHr9AoQFlL10tu3fQU6YiL-qZtwz0TUMDaZnK0miT_6h4G_fDXb5SFIrgLh9O4mZ8uSuwre04vVL02dzDbKDRHoFfOZvp1OIuCPSrQZDt9oWGT7I_8J9SDvEGeR_oDGBC01kKFlbHXV8HPgGXjji0dxzPDFwwl9Gl8oJC_6rEs4dSNnTd2Gq0FEqnEeg1RQcGNm2JXD9epIsjD4iNhXfLMxGVR3y7RjQCnRlI8x7PyQLD9YB-SAaREmI1dm2_utVvZm2rezvMx-PXTbtjKRdqayFainfJVbTqVtbnDXHjf-iiQOlRb-hpPgLzhqvzIF6JgFHMS7cZBKDGOaO54GcQJrGt0eMJyCWMArebYQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8386c27ee5.mp4?token=ELUAiX1nNyS3YD1LkDWjQ6DrJlw5HqJAcKSBE0Wm4oKOaUvYpmbZOzDK6YnsF35Xu2YraZG_NGiK-E5Sm_PtrUu5iUvuiuM4U7HiyaZOcoMRede0xtAvdyQ-3U2aJgQTqoMolR8Lf3q6CBrhOQsSqsBsghIq3mcqaAWd8c3yrTR7AuwijdhJkg15TMer_L5ghiOFp_QEDI_qgBxsUzTZv1iFem2XMH9fGEZxGo2OhcLCRD_AeUy9N7rN9OO2P0ZDq8cXClYmlWafSNkprhTpc17oWoF6q4GO0iMfwPBe2zq82OegOHG_c-dyDch_3y3RgPWhHr9AoQFlL10tu3fQU6YiL-qZtwz0TUMDaZnK0miT_6h4G_fDXb5SFIrgLh9O4mZ8uSuwre04vVL02dzDbKDRHoFfOZvp1OIuCPSrQZDt9oWGT7I_8J9SDvEGeR_oDGBC01kKFlbHXV8HPgGXjji0dxzPDFwwl9Gl8oJC_6rEs4dSNnTd2Gq0FEqnEeg1RQcGNm2JXD9epIsjD4iNhXfLMxGVR3y7RjQCnRlI8x7PyQLD9YB-SAaREmI1dm2_utVvZm2rezvMx-PXTbtjKRdqayFainfJVbTqVtbnDXHjf-iiQOlRb-hpPgLzhqvzIF6JgFHMS7cZBKDGOaO54GcQJrGt0eMJyCWMArebYQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌دیدارجذاب امروز صبح دو تیم امید ایران و امید امارات در مسابقات آسیا که با برتری سه بر یک ملی پوشان ایرانی به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29854" target="_blank">📅 11:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/29853" target="_blank">📅 02:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=DAAweUA_-fN1kpg3i9F8Bc1yZLhLu9lvvxGrR1Lp6sVKMxEChzPaQYp8_7zvtFAtrzPXWOqoSYYPZThplrtusxACHUKcHwMoK3jkuXFwx6p5ZJ55VpK45tXYv0yzS9jqfjUY7c7B9nAsCzJjuG0U0CBnazQ0LOJfkjBhAqng0GLRbh5AnJvDcYNBiyrjeQDZu11hQ25MHnvUE_quBXRk8ISKaVjkn3Uy4Hm33VIXBFGFy3jMYLgX5GZurQ_juEjXnFcnNIZprYW0-4E6SiGILqa2VJ1fzEW0lQMOCcefkDfTf7ZjKMCkBBbGhJJeTclZ8UfR6rbfIOHQEGAUxa0e1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=DAAweUA_-fN1kpg3i9F8Bc1yZLhLu9lvvxGrR1Lp6sVKMxEChzPaQYp8_7zvtFAtrzPXWOqoSYYPZThplrtusxACHUKcHwMoK3jkuXFwx6p5ZJ55VpK45tXYv0yzS9jqfjUY7c7B9nAsCzJjuG0U0CBnazQ0LOJfkjBhAqng0GLRbh5AnJvDcYNBiyrjeQDZu11hQ25MHnvUE_quBXRk8ISKaVjkn3Uy4Hm33VIXBFGFy3jMYLgX5GZurQ_juEjXnFcnNIZprYW0-4E6SiGILqa2VJ1fzEW0lQMOCcefkDfTf7ZjKMCkBBbGhJJeTclZ8UfR6rbfIOHQEGAUxa0e1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک‌ شانزدهم جام اتحادیه انگلیس؛ صعود راحت و شیرین‌توپچی‌ها به دور بعدی و پیروزی ارزشمند لک لک‌ها مقابل شاگردان دی‌زربی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/29852" target="_blank">📅 01:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29850">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5HcijEP8VDf_JT7vfEzZ56exIAjuF0y4uNb6jt3aGKc3Y4m_yCR12eKXZ0B07eLSijOOD2MF3jnOXseBzTqfEeQtA7wZFiji9zgqYkjRlGK1x6Qzd7P70c8Fs-sl2FCNUWABfSGBvvP7Tq36xnjXb87ijR3eSa9r47MM4HT-lfqVIdov24ffnQXo0Jy7ld-UwteemWskH4g9iQsBkp3EdOjvowuMz9iuFIdl9yHSlUfmkMQ9YlWtNdsZ4M3e2CNznTbIcXkhWaTrEAVnQZlt7E0OcTjz_Z0P74oSvZpVzdzb-FN95pQwzEB11yKz8XCUVO4IBCtmisHNAjodnPCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ از دوئل یونایتدی‌ها با تیم آماده برایتون تا جدال بارساییا با تیم تازه وارد لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/29850" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep9YWPaw_aO43DmfgIYCGrG2BzfIs3PgVdcQG7UO_kjAX8J_U_zTrurarIplUBVokjfEZAAXE-F3hGX5Pa5pupjNevVuUkpAUCO-kc66EEfDZFeFihoMRCHLd-e3l__vzUCSr-NO6s9y1FTGnXHJVyioMqTogpeNyDxLg04DJmbhpTBGJ4GEjK_TK5avzzEgbWPDfFvplYh7X_5NBECYQtUnXzZe9T6VjUaGOb4z9YW2Fnt9N69xb1YrWVgJfeIc4HTFsbCqZ_37uET204Xgd1pckSwcHcqYHX0c0Htx6vNE864fYTPG7Mx9Lz6PTKikQ0LdS4HDyTp7Q2BIMJ3FqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
رستگاری‌رئالی‌هاباگل اسپی و پیروزی غیرمنتظره العین در جدال با یاران رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/29849" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29846">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNdevEYiPJYncvVmV0pQFb9iZ7J2FuCkkiDP0T7UO35wvHrv0dsCLTEDAJf9ArTUArCVJMuDkJO9E32dm_BfFeQ9ad-CptZYseQhHuiJXkByFPHGcOjkayixEUHliTyv8GJDZSvteH-wX6EIoepxUgQS3jUq_l8zg3qZBAaYRVOKriSEimWPsvmHQj7sUrXi2DvdHagmv-ho7yzubPT-uzzt3B_DFzo2X4HtOQ-cgQM33Buqh7H1CpjlKxjkW9qevByOkjFpV_dr0O9NTbAdxORb7gTKSLuvVE-euLbP4aFRGUPZckC4QOySDxbVchnNV5vGeGlSAYxul9hfIc51mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ مهدی تارتار سرمربی پرسپولیس امشب موافقت خود را باجذب بشار رسن هافبک عراقی 29 ساله پاختاکور ازبکستان به‌مدیرعامل‌سرخ‌ها اعلام‌کرده. بدین ترتیب پیمان حدادی بزودی مذاکرات رسمی خود را با ستاره سابق پرسپولیس برای بازگشت…</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/29846" target="_blank">📅 01:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29845">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPEHLKPFB69YJRrKCXAcnDwLHvFsaFY7nRB6-qD4IzSMDxzEWdkU75f0CYN1BxthTBuEsPtJ_0cWBgmAkQle1WsKP4Tx3quEhDkuQjBhK2NSYLTOQsnt3jLcUfpYYc_klkqEBXfBOR2qI_VnITZKxLGLLI3GBZi10jvWjNLjFlr-87L7yvOGdDnTxTvAhmMkk8CNw9Qv_PWPckDjLMwrlO_U53d7us82t-btvHWXWCVmg_vkEhk5yqX2EWT3IdAfJiO0mfw3703FEVY5lvbmFp0RSN-kq86dqGZUWNJgr0XiS-JmNTUDkbNgfC54kIPeGEHMwncEui2sIaIZ9mAoPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس تا اواسط هفته‌آینده پاسخ نهایی خود درخصوص جذب احتمالی بشار رسن هافبک‌ عراقی در نیم‌فصل خواهد داد. پاسخ تارتار مثبت باشد بشار رسن به پرسپولیس بازخواهدگشت و مارکوباکیچ و دنیل‌گرا جدامیشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/29845" target="_blank">📅 01:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29844">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMaPL39J4b3NbqBkQyckAPxzI8PqTk0N7Z3T9K0t9FvlJI966JANsvTdcvQZcnObyM9vRAGmT01szol4lyZ-tZPFxoQQVXxx7HCdl0o2GrBoixmmZ4SryTLqhkaWbWntHNg5OugO6byAVSW4O3l5iYyA0deYvWvA1wqkBitbi3twsDdtoEdMTzJ9BtBnWCLiDYLc0qsc44rhRTnG6JSE9s8fVknBHohCk3bbjEBmK8eIT6PAJ9-zTRi7bRtD9E9tFiU_9MCyqD3oCa466fq6l8Y4omD4DZ3h8XfJQC7RPbF_s2AGjmtW5VAOyVlU3c2vNbVhGrDL_4ohxdRnpGEK9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام در سایت میتونید مسابقه بازی رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/29844" target="_blank">📅 00:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29842">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVH20bDbkyC08CodpMZjiKvWV_mJMzKmBU-u8lUPBNuJP0DhXsFCc7D7i4GSt5iiyj6eUjEBRA7V4ASqOh2pEfpMhsQNJKxeeV94lmbljLYRzP7iarWA9MHINj9LoCSmLgCenpxxgcwaaUjxjlPTlkmH2YIMH0XXe0_eDoYvUGkhvjGso9jjIJTmZX_GTcQ0Xw4FK3ty6TJKEy3fe-MoAB9w5k17LCc9T5j5AJNWw11H1BwQl92KgcGiC500-JnVcpQTha-aSCPOYLScWGEu3Epi4wsoeoTm_Q_56iBDDU5FnicQj0nE7eXbt_hUv-qNyU-dQ-8CzibyMe8yaCIE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ 8 اگوست؛ تاریخی‌‌ که برای مسی افسانه‌‌ای‌ دردناک بود و حالاهم دردناک تر شد. هشت آگوست 2021 اون‌خداحافظی‌تلخ رو با بارسا داشت و 8 آگوست 2026 هم با پدرش خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/29842" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29840">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GN0FIoBk-fth1QuqtKpd0TAO5wvbmol5cZlLMxUNiOlXvVHcXAIdnAhMxE_GzgrKzbnIjfgetCde9HbMWMfDW1wFZvl_IXodzWyDCeRVxUBfH0soRKnlmpz1tuxZHq9CHD1prmAHuMHDQm4aR6HFpHQpsQ3532h62y-Sot5uZajjfpGlCyH-YZj_LDBxcDZT2yJdLcl-Ux87t-_u7p-uRB8Z--EzEgiR0wddD2a5LE3QlKWHAIJMBSfCTOOjAciXgRhMWHvl-PO_Sl3u-EmE56gLXlSCBpBmVuEPZ4-uNZs6ixj15KRyTXvfWK5dNBtwPALqWZse4Bcdsbd8sR1RxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbqjKbIoOHFVtPWE9Djq2peFBdVZy8TqDttRvxU3I1tPpt6_RsH94J_rtiRi6WFMJBEbGeynV4vuat3RUOX67NReBxKWebViphwXDlXIwl4fsaX8le52pf02fOzqq51mbvWZlEpMPCXAy_zGu9KQxDMk0XZJDVE-X2-WIFM3_TR95SZv-WqRatfnzUkRr0ToZESZpEjDnEpuhE8L3lnRVVHBVqmIT-9VZWo2qePXtj4MCDCHUh1TsGNU-4PPI84NDR53l9xmHoU5eM8mO3i5hn1aDEf6hNjVclXous9LOA0AXY30tBZKqIx4lPrWmd7vgBV5I5LtEF90q3U-EpT0CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌ شانزدهم جام اتحادیه انگلیس؛
صعود راحت و شیرین‌توپچی‌ها به دور بعدی و پیروزی ارزشمند لک لک‌ها مقابل شاگردان دی‌زربی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29840" target="_blank">📅 00:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29839">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URmBt3fYc1ZfDTkalTevb-h_lvkvQqiRgPv5P5DO9LoRypTs7ZmkoZzU7gH7nRVYoW4NDWwd87mfON26Au_XgiHM998VGaG6B3MJkODAwQH4YTV86B7WSCQB-BWhG4Vgt6WdE7qYfNuwHEjLltWP3lInaBXxKvViOWCv_WsuYLjPl4AC7Z7f2vJoLeELBucq-dvfQt3GjVYsiGjKEgPjF1Qy19fdVp-zotOoDxYFnkwl06dgcAKWOlDJ55LEpcTaJZce_RtD7cOCEEVN0xtAEHd9o9ZiNLU5ZPcH2v3vdNmbT0X7pPooyb9rhzpANWEVWvAc_8aWaSByN3ddIXKzuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ججی‌ گابریل پدیده 15ساله منچستریونایتد در دو راهی رئال‌ مادرید و بارسلونا قرار گرفته است. این ستاره انگلیسی درخواست‌ جدایی‌ از منچستر رو داده و به زودی راهی یکی از این دو تیم خواهد شد. گابریل 15 ساله در 26 مسابقه برای تیم زیر 18 ساله منچستریونایتد موفق…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29839" target="_blank">📅 00:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29838">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fde2425c.mp4?token=HcNkX0itIDlEY0C0XTsTIg-rsQRBp8rkk0ROx4XrEX_j5QFqbvlFHxyzM6Gz6DsKCmwCFhAfZ1S8b6ZP-8-bxxivfmL8o5YEGMPq_PRY35nEsrYPgqasb5os2tHJOceAdOX6vmcRuoKszd66QM0USONABIJ0fBuwnpQ9Ybt4_Bk4Ha-qtFDTw-2XCLwb2tTKX8YnnqQ3yt_WO3VLYwpvJ7LDoZTYzO-FbCcdOja9t-sI2mqBArYpoOhWtT7QQPQCO0WoSJt7qI5EsrKgqCACZ6oXaqU_-X1QkKO9ysBK2Lhmuo2Hkxpk61CJWZsujQuo_g9R-VYf43dAC7JEckop4Uh3FQirp7Vs6tfAZSja-eqcCqUA_nWk_aUJz6TfiSXH8Bju5tVNetm4b19lKfGx87eXco227PeEAESv9r-81SsC1NzM2tbpnJuUCWaLJ5nnzoCvC3umW9L9mUKfNvtDC2kLxRkp6jfw7Y32PcsfYIwVPmbH1fDKXvme-p7EPRfAe5sxmSvgBM4JgMmC_GMlui9oQmFFIGTen0Pr59AYSgMta75Rn4hU487IcEwQJH8F5LbNo28ouunatgmjsCGOZStgP786kdAd101Wxf-U5fHnNCTJz_XjEq-GivDIDU1A0IlCJZhGDD8ZdA5eWaIeVzXh0nXSmvs19WOb2gKs3HI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fde2425c.mp4?token=HcNkX0itIDlEY0C0XTsTIg-rsQRBp8rkk0ROx4XrEX_j5QFqbvlFHxyzM6Gz6DsKCmwCFhAfZ1S8b6ZP-8-bxxivfmL8o5YEGMPq_PRY35nEsrYPgqasb5os2tHJOceAdOX6vmcRuoKszd66QM0USONABIJ0fBuwnpQ9Ybt4_Bk4Ha-qtFDTw-2XCLwb2tTKX8YnnqQ3yt_WO3VLYwpvJ7LDoZTYzO-FbCcdOja9t-sI2mqBArYpoOhWtT7QQPQCO0WoSJt7qI5EsrKgqCACZ6oXaqU_-X1QkKO9ysBK2Lhmuo2Hkxpk61CJWZsujQuo_g9R-VYf43dAC7JEckop4Uh3FQirp7Vs6tfAZSja-eqcCqUA_nWk_aUJz6TfiSXH8Bju5tVNetm4b19lKfGx87eXco227PeEAESv9r-81SsC1NzM2tbpnJuUCWaLJ5nnzoCvC3umW9L9mUKfNvtDC2kLxRkp6jfw7Y32PcsfYIwVPmbH1fDKXvme-p7EPRfAe5sxmSvgBM4JgMmC_GMlui9oQmFFIGTen0Pr59AYSgMta75Rn4hU487IcEwQJH8F5LbNo28ouunatgmjsCGOZStgP786kdAd101Wxf-U5fHnNCTJz_XjEq-GivDIDU1A0IlCJZhGDD8ZdA5eWaIeVzXh0nXSmvs19WOb2gKs3HI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه‌برنامه‌اینترنتی شب گذشته لیگ نخبگان؛
محمود فکری کارشناس‌بازی بود. مجریان برنامه 500 بار "حاج محمود" او رو صدا زدند اونم کیف میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29838" target="_blank">📅 23:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29837">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHoTibethavyy-UkG6bmh2wGkTBexLEExUjZU9uD8ckw3co4_fK0s-UurLRsVFLKimQicBpmpIrlJqt5Sa6wYeVlC76RNFiS1nsYNGDn6f5AhXEJTGd1pAHUCpelPOtBSaJQ0ujWX12pCiJDkyGgeasMVQERwjvmicVsRbDE0Jk3xXLotbe3-w-hPKDPF1E3owm9h-aHNjcdZsedUpVqgfB40dOnu8cdpuUrZLlCePreXA-JNSSURzfO0QX58kDdyals1kHW10Pf38LWY0qb3WY18JW02peGbx85VjJOovb1Zca9gPk1NRKLMrXiX625wC8esKMgRQBgZBHGYZ1y6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رونالدو امشب‌توبازی با‌العین اعصاب نداشت، مدافع العین هم خودش رو چسپوند بهش اونم این حرکت رو روش پیاده کرد. 4 تا زدین ولکن دیگه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29837" target="_blank">📅 23:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29836">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d67274da.mp4?token=t5SZGcKauQHodPMU8LrjkNSI6r5Utvs1C2rQHYEsg5X8Epzz5Lyzh_i6ZU5wn9HnMz84yqTKL5o8lKAWxNz-NoMwnRXzX3VSEDikiyBDkTy4qdPytjhR-NUQyP_Z8OzS4j-uqUTjFAumi5xuQG-cfObIKVjzmD2sIEN3yI2V-obDd8PVqX6bhQSEdCiqhMQ3WF3T3AaaPnumU7TFDmMoVcL5psP2tCTUu4wcsrKyJYUJXOeIIahkrs38Oe41cCP_IdAh_8Biqnv6eAOuxFInMk1LGMhZi1MioQBw9VLGixc7jNl3giPIk85Dv0VsscVq1wiZhit1NUVXBBB_7ZWKFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d67274da.mp4?token=t5SZGcKauQHodPMU8LrjkNSI6r5Utvs1C2rQHYEsg5X8Epzz5Lyzh_i6ZU5wn9HnMz84yqTKL5o8lKAWxNz-NoMwnRXzX3VSEDikiyBDkTy4qdPytjhR-NUQyP_Z8OzS4j-uqUTjFAumi5xuQG-cfObIKVjzmD2sIEN3yI2V-obDd8PVqX6bhQSEdCiqhMQ3WF3T3AaaPnumU7TFDmMoVcL5psP2tCTUu4wcsrKyJYUJXOeIIahkrs38Oe41cCP_IdAh_8Biqnv6eAOuxFInMk1LGMhZi1MioQBw9VLGixc7jNl3giPIk85Dv0VsscVq1wiZhit1NUVXBBB_7ZWKFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام در سایت میتونید مسابقه بازی رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29836" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29835">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=iuD_ZGpID8L8RHnizQoCpwIno7v9YJ36F1HOcRFLsMJgORhQNhfADS6eGsrekL4wEsGKJqGBYv-yI91n8KWd_Zq4T63lxbAWWh30p3P1SoRrlQ7UfWDtEoIAZYLcScc-maM2abTgPCof5lwUdTqQBhpD7QTCfa94QDuEKDuPvIhddPo6_drlNRAgzkcpJr4TaX2e5_PedVqhdeJrDs0iz8NnAxuw1MNLqiYmklmhnT4Ef0-AYytGyVVRGgAcSE0OrRn2HN8JgYAegUZs_NGL5b9r2XjrwyKEfGlBl03XrvkXNWpD0B7eaYJcOZB5jEBaX1ZJTQ5QCbZQ5ZIKdd0tiTIQdr2c5Xy9jnoHCS8_yOGK1HlwD5CSBxoBgE_Wwnp0U1mi4gs6wSaZ3UzHwkk1PTrQaMWLGICiT2xLiqFHN3NonGp02eGUYYaN4lIFeNCPwIq_FhWXr_udvTvbXLC728yA2FdeajBNEGRiD7RihIa3xVuUBoMr3DXUKVDthtnsLy_ijT9rG2WpVYALrveGiKqL27WjcacqLVWxy63uzMs_eMWqNWCnqy8i7V6ZljEGVrvCT0UMDmcFBtENgtgQPSxo4Cc8QM1CNE9kk38WYzmKS6PyDYpT-dIC5Lh2UEkyhYHv04XAEI4SxZhzeTWyoWll3nSJPPqUb62dnr-yoEs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=iuD_ZGpID8L8RHnizQoCpwIno7v9YJ36F1HOcRFLsMJgORhQNhfADS6eGsrekL4wEsGKJqGBYv-yI91n8KWd_Zq4T63lxbAWWh30p3P1SoRrlQ7UfWDtEoIAZYLcScc-maM2abTgPCof5lwUdTqQBhpD7QTCfa94QDuEKDuPvIhddPo6_drlNRAgzkcpJr4TaX2e5_PedVqhdeJrDs0iz8NnAxuw1MNLqiYmklmhnT4Ef0-AYytGyVVRGgAcSE0OrRn2HN8JgYAegUZs_NGL5b9r2XjrwyKEfGlBl03XrvkXNWpD0B7eaYJcOZB5jEBaX1ZJTQ5QCbZQ5ZIKdd0tiTIQdr2c5Xy9jnoHCS8_yOGK1HlwD5CSBxoBgE_Wwnp0U1mi4gs6wSaZ3UzHwkk1PTrQaMWLGICiT2xLiqFHN3NonGp02eGUYYaN4lIFeNCPwIq_FhWXr_udvTvbXLC728yA2FdeajBNEGRiD7RihIa3xVuUBoMr3DXUKVDthtnsLy_ijT9rG2WpVYALrveGiKqL27WjcacqLVWxy63uzMs_eMWqNWCnqy8i7V6ZljEGVrvCT0UMDmcFBtENgtgQPSxo4Cc8QM1CNE9kk38WYzmKS6PyDYpT-dIC5Lh2UEkyhYHv04XAEI4SxZhzeTWyoWll3nSJPPqUb62dnr-yoEs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
توضیحات‌مهدی‌زارع ستاره‌جوان پرسپولیس درباره مصدومیت‌عجیبش؛ دیروز  پزشک پرسپولیس خبر داد پای مهدی زارع در تمرین ریکاوری امروز طی برخورد با یک جسم تیز پاره شد که بخیه زدیم. زارع امروز خودش در استروی نوشته پای چپش به شیار تخلیه آب گیر کرده و اصلا هم جدی نیست.…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/29835" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29834">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=sRn067E-Hqos9lyr41geemB2V-iJf2kyEIPojbc23MrqdcUWaoZQa4sQo94hyFFGy2Q_7H6vsR6v5ijVYiudIWXDRIHNizPIiAeFaZMVSw0rPjI7x75gODC7KCIHFoZdNycNZyzn9IEZ0YTawTxE8Hun_NvekzhsX7idVf6qlZimBxkGEUCjRCWPzOOlyK8o_5s6MoA2OACvBX_XcijWrO0mnkMjASfX3V2Ab8rfIBK5J0-5TBkgIy0GTDni31k4ynIe0TdnOcKhgN1UwQ1_xeGqFXjrwpRc8YH_sK0icpw0HHPCqs5YBLXGYinUxyQtgtjB-c6sbNIGHLrGs5wTdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=sRn067E-Hqos9lyr41geemB2V-iJf2kyEIPojbc23MrqdcUWaoZQa4sQo94hyFFGy2Q_7H6vsR6v5ijVYiudIWXDRIHNizPIiAeFaZMVSw0rPjI7x75gODC7KCIHFoZdNycNZyzn9IEZ0YTawTxE8Hun_NvekzhsX7idVf6qlZimBxkGEUCjRCWPzOOlyK8o_5s6MoA2OACvBX_XcijWrO0mnkMjASfX3V2Ab8rfIBK5J0-5TBkgIy0GTDni31k4ynIe0TdnOcKhgN1UwQ1_xeGqFXjrwpRc8YH_sK0icpw0HHPCqs5YBLXGYinUxyQtgtjB-c6sbNIGHLrGs5wTdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
یازده گلزن برتر تاریخ فوتبال؛ 21 گل تا رکورد تاریخی‌کریس‌رونالدو برای‌رسیدن‌به 1000 گل‌زده در کل دوران حرفه‌ایش؛ لیونل مسی هم این هفته 928 امین گل کل دوران حرفه‌ایش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29834" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29833">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=r7mQ8uGo17RdID_XJOLsq9mxMlJTh57-QQizx_Mt_aRgJTGhN-7Cvn4s6k5RDKhAsb6PEIrnc58I0HOnO6xoVfzFO4KzYNpWO_WdAO3zQoDAx89jIXymvdneP4Jempn0BghYgljnyOxnNGyXYVC4iWh-KqcDbXNZAg50RxUvqMkXoul5qgR8RNRFdUyAn2pPTllpumDyPi3qEhEHlN9nMQG_7v30c7fnn7Xigsemmz8XO2qpSJYTFmP3g42Li2Q5OSbhAUT_WV3MCDFb25SwgOoGd6fZo6S5f209auw3lB1JGVnRzIqhnERzb4tfVSAPAzd5CcRVyney3rJ5q9CtkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=r7mQ8uGo17RdID_XJOLsq9mxMlJTh57-QQizx_Mt_aRgJTGhN-7Cvn4s6k5RDKhAsb6PEIrnc58I0HOnO6xoVfzFO4KzYNpWO_WdAO3zQoDAx89jIXymvdneP4Jempn0BghYgljnyOxnNGyXYVC4iWh-KqcDbXNZAg50RxUvqMkXoul5qgR8RNRFdUyAn2pPTllpumDyPi3qEhEHlN9nMQG_7v30c7fnn7Xigsemmz8XO2qpSJYTFmP3g42Li2Q5OSbhAUT_WV3MCDFb25SwgOoGd6fZo6S5f209auw3lB1JGVnRzIqhnERzb4tfVSAPAzd5CcRVyney3rJ5q9CtkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
درهفته‌اول‌لیگ‌نخبگان‌آسیا؛ العینی‌ها بادرخشش خیره کننده برادران رحیمی توانستند با نتیجه پر گل چهار برصفر یاران کریس رونالدو رو شکست بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29833" target="_blank">📅 22:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29832">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avRCCtNA9J_mJ06SD-aOywcY-3Qf2hwUKFiho5MUKqAoEI-zVQ2iXYcoedGtfOfGb-9I9Nq_nfiMJ2qAU29SWPmW6MjRQo_-0YxFVLTZoBeNCjHBNu9aGmhuEQLkO2GjLd7MG7-W9IwminyYZaZijnBqyMj67EH62e7tdRXNJYAhjH0kFHO5iZv1joFvCWZ_MaIWx1a1R9AZZd2irXco4y_Usksx92NhJCEkz3GcefqcE-TMmDZRiFDnekc1erR_hTNlt-3xj4crZKeHrtjrG3x974zb_Hse4K8pZ33_18zA-UeaTA39O-lsK3VZGjhv3Eyw9vNcYsTErYQW_z9GKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29832" target="_blank">📅 22:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29831">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbIdmoIlW4A3XgLT_9dgZ10RqF1yvwfLW76qjweDUK6b34pXaZQ99mzJSgAVUetT_GayjKC1CpPz55xXesQk6lExyuXJI3LXNmt4kLthv6-FOMXP_JIPGf1gNHdSiqY0xSmIJ6ZYWpD81aB0reIKCIyDZ2gGRMgmUfg01Nki_jaXwZMgLgVKAAkMCaqishmO8_Z9zQtA6qqq4huV-zMu8NBZ05h7QQn81NtT2RVRCTIUJLG4Cke7A4e55RBQiSAzZyDL7iJtPN6dKnEDzmfCmyMw4DJGr17YN3AlUhxJMFid0DJkeapk2_8euYs3yoIDOFKKQa7PBUAoK3P8M-RkXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29831" target="_blank">📅 22:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29830">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVr60md23yXyut2dlQMMikfsgVhIFMRvdRXZrOHagGKB8pxKKEvSCdYmVQ1YkR1NoU_NLuYC-1X8uUL9kTzY7ZcjGKrd-ki1rXP5kBFLT1l1ps2QwwylJC7BGsbqfXNv5QIx24ZwasDrv_5yMxMqDtgDpPllhoDxlJTQtrf4SDrBWCRNL0Xql6Fxh8hC5dLpDQnk0wToh_-alEmtjo8HU0nyPhslLzc92euwZjDS6snR3da_Pd73PTVXvWB-c4LRpLbEadloiySVQ8y1PXnNLL04jA3IicGvFrCiHxZ45pW-a5vnRzATs_tEggvwBgwLXZ8h4Mwl51qFWivR2XcwZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛
شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام
در سایت میتونید مسابقه بازی
رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29830" target="_blank">📅 21:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29829">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJbw3CdV9koBOQrH4776H4iGsMRsU3r9iDBYa0f2lxOcXWAoIUfZx9Yz5v_qAPQOAHRKKwrFqjGjDPvpykxvIitIhB6Z2NikkpTwbfhUGtE7B6l-M6YNKLo2PIeBahgh4r5YXNkpJ_uiuaZLMq_O2PS1sS-cjsvIpT81W8y7mZPP3ETpU0Ac3HeDNK56tvYjQM7zgiZ3yR6MFKSgMQS2r3NA_0iUnvZ-n-jG2xtS3-B5N_3E_L-2S_AGw2_zNtdm24rY4qLLwj8vO2ub-nxKrnhSU1wdwp2RZABzVffknlh6pcJqIV6A1uX5p7jDLkFlZ0-IJO5ttxH1pBBM0ckrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇨🇴
#تقویم؛دقیقا 11 سال‌پیش درچنین روزی؛ خامس رودریگز فوق‌ستاره‌کلمبیا این گل فوق العاده تماشایی رو در جام جهانی 2014 به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29829" target="_blank">📅 21:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29828">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29828" target="_blank">📅 21:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29827">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=NNvaqXEytZoUu3Xn13ZYYK5jsekLF5QUzsEKoFjea5ypHOQ4MFr5x_zk2rAVGgAMc9bMS_fZ2rQZCBD7spvx9TwWPZFvlmM7dZScRd3YWnksumuWXZxVak0aEOaL9FsWA46ss3ebvWVd6bQdoVcVjVsoOfsL71P3bJbK2772nF1idPluzyR0RR19kBESDv8P8zW58C_hnhZHHLyaTTvxZYkidTJdkeIvt3sZDQxJQqEgzcHMvwJtQCRHPKpWPxBwBu5AsNB4UhlaPo1KbmAP2C_dXrIF3qP9oh6H8KtIWOefk1jfnCsMLO7dwkkYvN66xQAUu4owRuvhsqNINmG6HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=NNvaqXEytZoUu3Xn13ZYYK5jsekLF5QUzsEKoFjea5ypHOQ4MFr5x_zk2rAVGgAMc9bMS_fZ2rQZCBD7spvx9TwWPZFvlmM7dZScRd3YWnksumuWXZxVak0aEOaL9FsWA46ss3ebvWVd6bQdoVcVjVsoOfsL71P3bJbK2772nF1idPluzyR0RR19kBESDv8P8zW58C_hnhZHHLyaTTvxZYkidTJdkeIvt3sZDQxJQqEgzcHMvwJtQCRHPKpWPxBwBu5AsNB4UhlaPo1KbmAP2C_dXrIF3qP9oh6H8KtIWOefk1jfnCsMLO7dwkkYvN66xQAUu4owRuvhsqNINmG6HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای‌ایلان‌ماسک:
گوشی‌های هوشمند امروزی تا پنج الی شش سال دیگر کانل ناپدید میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29827" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29826">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NV9CTJBy06wC28P_4RS6zUe12mYiGnu8K69a0bw7C-HgvjQHy8KtC3aEkr5dPqrV6ZljbqCPZpkGlJyT9eXwxE4F6XqHzBncM81pg3pu0cVMeCc4Wa_UIaKohoyVcJ1wjCI4-GxGyTITlixYFlJvQT8qXvNPob4eU1nyQPBTzBu8LodJAN_51clKD6E5YupELWm_wLQztueQHUE9-ULpbC0BjYJ8jTQgEbzHIgT_EVePy1GHCcBnAvCyrDwXEcGVJAF0R05c-KFC2TISvEEvW0kWRbLTfFe4pEX80OO-NPvI35vReFlN9hyRGyojzcXqvsqWPiErzsy_oiO-b0dc3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29826" target="_blank">📅 20:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29825">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmRuGFuEpXdwq7r_3Po6z4-siGBJJpVrbe4Oo2U9Q-5UCsHrtKB07I2pxd4dK2nWvMaAo7uL0C86P07RhRT_3J07ALkCw6HG8VaX5i_h-lDC8iolMi9uFYReK0YeLXLgwrhmoI7osw5BvmkPUv53oLSJNzAuupZ8jF4AheP_pkyvaxeXsVocx-bHbGttKrrFoArOuvq5rtAg_HH25zNzbgJuMT_YVgHzI2Q_OE0y15GjHxAjHGbxyEoB01aPBR-MYKo0QETd5477Fiy4F3MVqqRn7lP5hG2ceONMmxvXtjhj1DZ9XpuRgWUnDf5xtbPT2ug3kf0gmIH4So2SCXRreg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇪🇸
رودری ستاره30ساله‌جدید بارسلونا:
رد کردن پیشنهادباشگاه‌رئال‌مادرید اصلا برام آسان نبود. بله‌ابتدا درآستانه‌پیوستن به رئال مادرید قرار داشتم اما بعدِصحبت‌هایی‌که با دکو و هانسی فلیک داشتم تصمیم گرفتم به پیشنهاد رئال مادرید پاسخ منفی بدهد و با باشگاه بارسلونا قرارداد امضا کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29825" target="_blank">📅 20:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29824">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de2283857.mp4?token=H0o0E4hjHpWC_BlRU_NNhO4heLVaue8mKHCCG2LOWDo3XbUHsigeiGsCKszuOdegCbF_dvQfMknue5sTZ6ZTZ0SuQMv-TEC6ev8VhI91pdX1UCxtoRqpVpxqHcQyOFIm577dCqrUxzKAvRLQif2FuismF5R0Os9bxxGWcukSrRlG_PJ26DgjxE6E1eZp40PYBLfQfAOGDtK06uA6eTi4FRHyyraBusmLS84qtK7ePDxm1luJM5bxBtfRUk_Lg3OgI9dO0xuJtN-LqW1mYYywfT01kOQBLIOwcYRU1tAv3MknpLWqDYu-HbSCeMCYDii_QbVe38TVwbS1DoqlahHR1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de2283857.mp4?token=H0o0E4hjHpWC_BlRU_NNhO4heLVaue8mKHCCG2LOWDo3XbUHsigeiGsCKszuOdegCbF_dvQfMknue5sTZ6ZTZ0SuQMv-TEC6ev8VhI91pdX1UCxtoRqpVpxqHcQyOFIm577dCqrUxzKAvRLQif2FuismF5R0Os9bxxGWcukSrRlG_PJ26DgjxE6E1eZp40PYBLfQfAOGDtK06uA6eTi4FRHyyraBusmLS84qtK7ePDxm1luJM5bxBtfRUk_Lg3OgI9dO0xuJtN-LqW1mYYywfT01kOQBLIOwcYRU1tAv3MknpLWqDYu-HbSCeMCYDii_QbVe38TVwbS1DoqlahHR1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایتی‌از عملکرد خیره کننده جیجی گابریل ستاره 15 ساله تیم منچستریونایتد در فصل گذشته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29824" target="_blank">📅 20:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29823">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUkLjtfFP43DN5AQxrSdnNvH4rw7A9pCIaS8AMj7jpDr5b9YP0AZfLKJi6yKZutKjPlopQUfN6v2KkA0qZKUZ99wC5CV6rl-aXN6y9laB2j7dBCWSeiZcZ-9o_a-3P1dtROTYsbT7N63JxPFkmvuoIsZKvpkG8h5qEB_sQUrE9hBb4QFGeXi23sObWANMI-G0P1Iq4FprgP95wNolOvTQlvOynHNA_PYZg6xyahRMBFvZDSRzTtsQ2GCg4m63DmWNYw9fJzuqPgMgh0OFuaHgZ30YqIVCKvggV-kx6tLfwzUF3QrGnIcWoK4wBsTcS5izfa4pGZZbhkcKT6IM31_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ججی‌ گابریل پدیده 15ساله منچستریونایتد در دو راهی رئال‌ مادرید و بارسلونا قرار گرفته است. این ستاره انگلیسی درخواست‌ جدایی‌ از منچستر رو داده و به زودی راهی یکی از این دو تیم خواهد شد. گابریل 15 ساله در 26 مسابقه برای تیم زیر 18 ساله منچستریونایتد موفق به ثبت 27 گل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29823" target="_blank">📅 19:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29822">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yr2BRetuVoXFqpjJYKuDedI7hYXGyE39g4IU1PFtBlbuCWETUgT9TgFjw0H4jJNj6uvK-tKjQeGiqnpmnzTwQCxFJaF1tJmXOqw2ZGSqdnzChQ_O8YFUVNgpQzkFQKIt_QLBPl4dvQeAX33Crz_UDh2OCjpSkMSTgp-a9RJmKq0ik9HFvRRNLBx7y1tKa0lpAa7aGgsT9QFZmhV6t1TMXMbHd5QVux2CI1_z06StfFFL4qE9jkRnXStd3UL8pdTQ_dDNb3k15w7WpOleT_9JyvjFlXRz6Fi_M9ZkNHi_kcubkXT0LjQQ8NJ2xAr2tQsKUy7DKn8NMb-U5ZcVQHcFpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29822" target="_blank">📅 19:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29821">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYjqm0VECCFv-wJfAQq61URf18fV1U86qMmF28Rb17H0nrQmGjgYRUho0C7-IaHcyjeMupMqapyWKOYcrSw_wCn_4tpBgiHahIbVX82yvgbn0wgWpjarYKAhAKqq8p-2hHihTnZ02_dI7fUSuM9x2jWU8oFSzIbyHDI1cULfEVjQBX8-Jbik_RLN1as0vkflbt56w5IJqS_GYprlaL5UPylwH167uz7QRxekXPDkGsmw302qEaUgRj3uypW9TldDOmI70nQ5OwBeQt3bO1rLMblOypZUHRWx3LuHuYm9oeGdNxMz9E7yhlnpcDv02Dbu9Pwytz_wEcQ38CtPktF6zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29821" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29820">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29820" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29819">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AooLVDxUqMD-XySOUW0l8PsOgAi6Gmqth6OgsfavpxOYLI28AvQylbwg42yUkYVArl8Rl_pOcR70FP0ujaBvjhovFbG5BH-4LXS7HPnwcT5WTy9JKxSK4Z4SjdpE1zembexPkuveHnsOPLVAs_nr9z21V_VNf2pNsF5CLqDJQFgqeQICJfR7KptYKI5Z6Bs7G4j6exVbBUuPtmL5sK1WF4BNTdgrWJSktHnZWDSdYFNtyntf8b4iksljkuipvDh6_3U5HoxVPLPmmlfWeAgiOZvbaZv0PVFQ80EizbsPXQK9hjBRRF1ONFiUvZHxuanFSDsjHx655ZrxI_4eKGkjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🏆
لالیگا اسپانیا
⚽️
رئال مادرید
🆚
الچه
⚽️
💥
باپین باهیس؛ برای تو، پیروزی یک سرنوشته
🌐
سایت پین باهیس بابیش از400اپشن برای پیش بینی
🛍
پیش بینی باضرایب بالا
💎
🤩
🤩
🤩
🤩
بونوس خوشامدگویی
💎
🤩
🤩
🤩
فریبت ارزی ودلاری
💎
🤩
🤩
🤩
کش بک روزانه
💎
🤩
🤩
🤩
فریبت درگاه های ریالی
🤖
دانلود اپلکیشن حرفه ای
💵
درپین باهیس دلار با آربیتاژ 30 هزارتومن بیشتر ازقیمت بازارمحاسبه میشود
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g24
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29819" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
