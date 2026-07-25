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
<img src="https://cdn4.telesco.pe/file/cMcLCylQfKn3wVhgZKWTT3O_6Y5dbccK-QbJcHGKrx8XzDJlotY_IPzgvuyHLKG-ibIqktn7BtkLStd9ycuYfJX5J4SSoWfTh-oGL9eZUkeEwznD3YFu5lQ_u8Bl8jLa3Lt7zOsnv86xJa_LuR83k2G1gkWOaGZRTY6X_EqR8pafM9ogkTlqnq56m-HQUXdVkvS674kptBsOp4sfJnG294_EOZS6KDaYmp47ycXTC5C5JnLmcyqwtGRYuEOESXkIlCOmh0ii7chepaToYevTFK4XBUymk3NmiggLLBF_g5WSvPuTC_vNnEnbezaAxHeyEBHaSiJQNpK3CDtrZjvqcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 23:36:33</div>
<hr>

<div class="tg-post" id="msg-85584">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
المتحدث باسم الحرس الثوري الإيراني:
أي دولة، سواء كانت إنجلترا أو دول الخليج أو غيرها، إذا دعمت أمريكا في الحرب، ستكون هدفنا المشروع.
استخدمت طائرات B1 الأمريكية مؤخراً مطارات بريطانية. إذا حذت حذوها، فستكون هدفنا النهائي والمشروع.
لدينا سيناريو خاص بنا لكل مشكلة.</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/naya_foriraq/85584" target="_blank">📅 23:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85583">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
مجلس الوزراء العراقي يقرر تعطيل الدوام الرسمي يومي الاثنين والثلاثاء الموافقين 3-4 آب 2026 بمناسبة إحياء أربعينية الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/naya_foriraq/85583" target="_blank">📅 23:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85582">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/094db86814.mp4?token=m8rqw_iPRufgRqtWfceWdlSXLW8S-iF1lb9ZSlmX5HqStlePRRhJwSJucJo88dhWl69L-bayOgQSfgSeITmLZM1eABf4kKm5twiRAsTCaVzSaapD_umX9c04wWbs3j1WJkX0UdgR0FQtIGsl5b-Nd6OTI2pGEseXS_d-KFVcg0j8gPT5SiL5LUMyJYV6Rk-TS_fJLJZror_xhXbh_woGXl5wktTjNkS4b-oSls11V0ti8GcA1utjPgA9LwDfhbxpMAZPykVpNVRxJcRqXlaiZQ4hgNcCkiyYyaySEBdREOWI_gdZiOYjbO4KklksB6KNWg2eoV4SgzxElqJWBhnqQSANuh0HLVoTMaAP97ppZwCOMJZy29Oks9x1a0KuGv9IMaN84I_4ap0k1T9SJIMQnMcQtRG5MxZoeOdP7P6q5oYUNVjv1Fs5EyZpPLyhGCOBQxzvJL9oUR-_udIrVvgW9EpAypzISWMkeJ_fYC76FqS4UtWGl6uJ_nlbCoG-oiUrZLpz0rnQJLXURYFHV31MF29WhiciQTfZkKC7jMCr1dcSHbKQBL02vmZjIDx5Ro9qEYlHihVYfYfqmOAV12M_Y2uOemvaRg6bxBOXGXySZjbYIapy4FPbm1Bu-uwY-XgN_rNocHLzzZihVgMYZx_AjYvXrkDSZ_ZIab4glhXqvNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/094db86814.mp4?token=m8rqw_iPRufgRqtWfceWdlSXLW8S-iF1lb9ZSlmX5HqStlePRRhJwSJucJo88dhWl69L-bayOgQSfgSeITmLZM1eABf4kKm5twiRAsTCaVzSaapD_umX9c04wWbs3j1WJkX0UdgR0FQtIGsl5b-Nd6OTI2pGEseXS_d-KFVcg0j8gPT5SiL5LUMyJYV6Rk-TS_fJLJZror_xhXbh_woGXl5wktTjNkS4b-oSls11V0ti8GcA1utjPgA9LwDfhbxpMAZPykVpNVRxJcRqXlaiZQ4hgNcCkiyYyaySEBdREOWI_gdZiOYjbO4KklksB6KNWg2eoV4SgzxElqJWBhnqQSANuh0HLVoTMaAP97ppZwCOMJZy29Oks9x1a0KuGv9IMaN84I_4ap0k1T9SJIMQnMcQtRG5MxZoeOdP7P6q5oYUNVjv1Fs5EyZpPLyhGCOBQxzvJL9oUR-_udIrVvgW9EpAypzISWMkeJ_fYC76FqS4UtWGl6uJ_nlbCoG-oiUrZLpz0rnQJLXURYFHV31MF29WhiciQTfZkKC7jMCr1dcSHbKQBL02vmZjIDx5Ro9qEYlHihVYfYfqmOAV12M_Y2uOemvaRg6bxBOXGXySZjbYIapy4FPbm1Bu-uwY-XgN_rNocHLzzZihVgMYZx_AjYvXrkDSZ_ZIab4glhXqvNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
طائرة “
شاهد
” المسيّرة إلى جانب صاروخ “
ذو الفقار
” في ساحة آزادي بطهران.</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/85582" target="_blank">📅 23:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85581">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFt89NFi6CcSYI-bsawqXXf9ecZbz9ktsf950efFD9s_5qfAriE7RPETS4cJ0d_TPxi2DKVACSNMqfq91KT6tueVE5-dYEd3X2fn8gxKH1h-qvAtrXUFii41cJxMEOSCiVbbJ4RjRi2ykkQOmO8jz2XUOhmB1B403Kmfbn_Ll6N0B0vgh4GjnfLBWbQYMuvCQGybtKD8Fvqoj6ZMHUmJVm0HfeDtKsHYRNTSYblVCzq2YDdcHIlB8_8m85s-77ga_JQBfnU8vgBFHQOGUfzdo4BOoeeEN9rdmrS_zhJCXdBXnwZfLJfm9eZoUSac9QoOuxc9_ys5LGWSKn8DyjMl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🔻
🇨🇳
توقف الشحن البحري بين الصين والسعودية نتيجة ضربات أنصار الله في اليمن على باب المندب</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/85581" target="_blank">📅 23:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85580">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-text">🔥
آق مجید نقطه زن
یه موشک اوکراین بزن
بزن که خوب می‌زنی
🚀</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/naya_foriraq/85580" target="_blank">📅 22:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85578">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690a9e602a.mp4?token=eKqyV8oFWw6mNRX283abTM8gGLDIZ96WRV18jddnJXo2wxHGD02WF2l9573IF4UBnCXj505ar1jc-FugshpX-SPrzF3lSeLTbfq9r7LhVwD6YwHAJIdqwZXavJH9kVtakFjIGDsB8NkJ-s8WZpRlwszE3bD4tW1-sn8ad0rNydshmXxUzhksTCfTAvVRp-63t-tqdfDPQEyCCbVKjQo-zaUykgSLc7u2RBhYwzLVyMkienP6o_cUS2vyam9eFo2yzRslMEbPsLqT-ZIkJt7dwhDvts76s-hsbRXmr0nFcJHmENRQeFdCWXEMxO2jlIxmpdp04vgFnsgQwp6G-aOZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690a9e602a.mp4?token=eKqyV8oFWw6mNRX283abTM8gGLDIZ96WRV18jddnJXo2wxHGD02WF2l9573IF4UBnCXj505ar1jc-FugshpX-SPrzF3lSeLTbfq9r7LhVwD6YwHAJIdqwZXavJH9kVtakFjIGDsB8NkJ-s8WZpRlwszE3bD4tW1-sn8ad0rNydshmXxUzhksTCfTAvVRp-63t-tqdfDPQEyCCbVKjQo-zaUykgSLc7u2RBhYwzLVyMkienP6o_cUS2vyam9eFo2yzRslMEbPsLqT-ZIkJt7dwhDvts76s-hsbRXmr0nFcJHmENRQeFdCWXEMxO2jlIxmpdp04vgFnsgQwp6G-aOZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوف يتم تعليق صور الشهداء بأمر من العتبات المقدسة .. في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/85578" target="_blank">📅 22:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85577">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJe6bDdUuaIwDu1igvJz7fIOtjLS95XktZ2a5YX9C-W-QRhiEOwf5KGDb3NvHvml3g8RJRmOKSh-e5J2LIFZUg6xgkex5FvrfWxvPltl9QvpYopcJpF996eSmY4JO8awHgI8XYUPm-UlWtjXBzTcGCFy5o7LrPx4moLjK_fDPwPyULIeaNFJqLnGE9ylHmECV9AgfPc3ZcAs5rIPrK1swiJ9Twu3_3jNuNQrp9gZnceF4JjCl0yAhSJN8zCRnFrTHFd3jfg6L6Vhd9Y4wZeQf0FCmYSCRo4AHx2rorTM7rE893UVKD8Hos6KUGBzIOEcRZx8qbxHuWT5D5PAtUOCiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زيلينسكي المهرج يزعم: استهدفنا سفنا في بحر قزوين تنقل شحنات عسكرية لها صلة بإيران.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/85577" target="_blank">📅 22:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85576">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOdBoCGLJYxL1UFUQxHA4BO0TDXZMth__51YMPoovazHoLlnOHVhpVg5UQZ5QCzW7X1qnGLGn5n5JyMjya-WHW4skzTjH_fdr0RGyh02LqQfLSFtfhddQmwP-Qg85_Wy5tRGlxgGIFc9KO2Yivn0lyRoULmCx8GEIe3u4R-ZJ9sxXlZbkrBRB_d-ptRonpVwxe3D4CYvpVPpqH4siIENOwMsXPbNCFuBeP-aLN5ibveDUMQWxnBW6EYLQ22FZy_k2Mkt23hr-l_fHt4a-yUKFNtys2Nz0jJUAPb4_RcmLsCtdCBS2Z5LzsW8sy9iXukGdjB7RuvdL5eG69eWPj4tsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
🇱🇧
🇸🇾
🇾🇪
🔻
نحن أمة الإمام الحسين
من ملت امام حسينم</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/85576" target="_blank">📅 22:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85575">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4Ggg17taxM5iLYB9y6ZqEXcSD2dKqVvZEjrYiazUysmL7WGLs8Mb6ToB5FPNZ1KbmoRn95GPapMV5GRuuys-bUs81zMirWbgvyXdBMM1fUqxEG5ebCwwfXXBzE2-u7RM0EbVqPgZkCoiBkrL4GMEDQ0m2i3XY8CBsvSJq9xX55Rv5cFiZZNyC-UwJypLXi8sjF2U2SHqRkZeX82ekQMv4T3LDkYz4X-OkFBl7BKQK3-1FuU60JYcWQooE_cpeHQ0iibx_TbW4ERDa6CeHUsq3EG5x1LJTbuXHPKJ-FZYo3Wq9-RNlImKtt60ByV0JJw7VPBImyPDipzqcIiWkERtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوف يتم تعليق صور الشهداء بأمر من العتبات المقدسة .. في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/85575" target="_blank">📅 22:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85574">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85574" target="_blank">📅 22:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85573">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cc3dbd29.mp4?token=lhDWCtgISJU8mF7U-PAGXhS14-MqKUxVAf80iN6g7REJbRW7LmAjXawzb_P_6A4num_rZAyimMnHXNCJ_l5S8iqZ_bme8VLk8_n-Tud-TcIioiGCinzS7ViHKPsjAyoA3iNqPdF37SrzyMhhxnpSe39kEi4l1nHURSOvnxfsK4xdxVLAg3qqpZREd-yWauu4KAOzqVjKcNj6s_47CYGAIQULkoviKgcX0ylI_fNQ_FObukiHlLEVo1Z1L_s8obMDFffrf1o3cE0avVcdteUxWNYVPPhld9E6oRFtzI0jQ9GftIWfJx14kY6ct54w6Gm_Yz73eMOtSN0Be37SA8nvaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cc3dbd29.mp4?token=lhDWCtgISJU8mF7U-PAGXhS14-MqKUxVAf80iN6g7REJbRW7LmAjXawzb_P_6A4num_rZAyimMnHXNCJ_l5S8iqZ_bme8VLk8_n-Tud-TcIioiGCinzS7ViHKPsjAyoA3iNqPdF37SrzyMhhxnpSe39kEi4l1nHURSOvnxfsK4xdxVLAg3qqpZREd-yWauu4KAOzqVjKcNj6s_47CYGAIQULkoviKgcX0ylI_fNQ_FObukiHlLEVo1Z1L_s8obMDFffrf1o3cE0avVcdteUxWNYVPPhld9E6oRFtzI0jQ9GftIWfJx14kY6ct54w6Gm_Yz73eMOtSN0Be37SA8nvaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد خاصة لنايا توثق لحظة اطلاق الكويت رشقة صاروخية نحو اراضي الايرانية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/85573" target="_blank">📅 21:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85572">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
‏
سفيرة الكويت في واشنطن
: ادعاءات WSJ بشأن مشاركة الكويت في العمليات ضد إيران باطلة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85572" target="_blank">📅 21:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85571">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012b1c9a7c.mp4?token=K4tCuIOICdwG7ohC7XqOo_PiAVFSmFtIT4qImeT4mSf-6xrbNkZhkCK0kqZfFdgb7ntLyViAIzpHsnFraNudEJQLc-b7xjgmzokYzZteCkowUwRhOPT2O-y9LkyLHbaqlAQTnp3IoGw2JE-XX7eBUBMzG7qzdI-hMbpV7P1bBGLxT1p0SB5DwHxx1gfVtcPwLwQFbNqYXr31E-Bj-eLO0SrS1nXsH_kw5r4qyOOtD5JQ08PxOG9gMR3QpCVzMAz-eAqXIHbukCiPjMjwrtf06PltUljXwD1jn55UTrK57_uDg56D3Yq_c2uv8lIzRVvhERoXQEu97cNkHpks8wsTYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012b1c9a7c.mp4?token=K4tCuIOICdwG7ohC7XqOo_PiAVFSmFtIT4qImeT4mSf-6xrbNkZhkCK0kqZfFdgb7ntLyViAIzpHsnFraNudEJQLc-b7xjgmzokYzZteCkowUwRhOPT2O-y9LkyLHbaqlAQTnp3IoGw2JE-XX7eBUBMzG7qzdI-hMbpV7P1bBGLxT1p0SB5DwHxx1gfVtcPwLwQFbNqYXr31E-Bj-eLO0SrS1nXsH_kw5r4qyOOtD5JQ08PxOG9gMR3QpCVzMAz-eAqXIHbukCiPjMjwrtf06PltUljXwD1jn55UTrK57_uDg56D3Yq_c2uv8lIzRVvhERoXQEu97cNkHpks8wsTYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
رتل عسكري كبير يجوب شوارع العاصمة العراقية بغداد.تحديدا مدينة الصدر مناطق جميلة الطالبية المدينة تتحول لثكنة عسكرية</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85571" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85570">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d9b8fa0a.mp4?token=eKRgEgFvRL-8qS1J1PVUu21xoCH-VFGR7tv1P-HDeD3VOTp8Joegdf8eC4QqVJ4V783FitKn-zkjkIVMdSscqAFvA-sYLcM4WWNRK9k9bzFj4GTZTPwvalqeV__Euz6aZjFiCukV4UQZzzT82Eby3mJBqrzqIPEkjmL4chE7uZ3tZzta8haP10fLx7g4F0cb-O1R7tW1cpr4mssib1Gi2xVpOlRA7YDWd0rQ8n5u2XO-mcxxFiZJA-hB8hNzJP_4yFcr6yQqmicaVGWgmtWAX40WtydFN49lRlog8ZdYkFoLV16TO5EPk-8r2YH4-xOH2YmMQ2oMoJaSe4-ZRdI7VSNapJkWGSpELMHUs9vh3-gnshZK5By9NDSEXLBQbV9QaXx93LEXnPKCQ9qsKYzMLUykLpsRmP_oZE-qiCAlVq2vrGkgcxhgFxgzVbZzKZMi1bWSB3fWHW_2xclBLShHdK5eGhEF9z7yi6WYWK1pWGKIZP1w_9YTDRToFgr8pHLLQhgeaI_ksSDLGe1llfMwtE85tOcfbBiH0foAcRzGxaLTg6RSsjzDWv9hJw29L-_9lWlFut9eqjDhVAibkDk0W6KEp3m0ya9u85htW0jkNqOEDbzAYB9YlQCSFmqGF_MymoEzNeB_trE-FzyVp9Xh9_dnDTCfeyWZfbIYj4oGacY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d9b8fa0a.mp4?token=eKRgEgFvRL-8qS1J1PVUu21xoCH-VFGR7tv1P-HDeD3VOTp8Joegdf8eC4QqVJ4V783FitKn-zkjkIVMdSscqAFvA-sYLcM4WWNRK9k9bzFj4GTZTPwvalqeV__Euz6aZjFiCukV4UQZzzT82Eby3mJBqrzqIPEkjmL4chE7uZ3tZzta8haP10fLx7g4F0cb-O1R7tW1cpr4mssib1Gi2xVpOlRA7YDWd0rQ8n5u2XO-mcxxFiZJA-hB8hNzJP_4yFcr6yQqmicaVGWgmtWAX40WtydFN49lRlog8ZdYkFoLV16TO5EPk-8r2YH4-xOH2YmMQ2oMoJaSe4-ZRdI7VSNapJkWGSpELMHUs9vh3-gnshZK5By9NDSEXLBQbV9QaXx93LEXnPKCQ9qsKYzMLUykLpsRmP_oZE-qiCAlVq2vrGkgcxhgFxgzVbZzKZMi1bWSB3fWHW_2xclBLShHdK5eGhEF9z7yi6WYWK1pWGKIZP1w_9YTDRToFgr8pHLLQhgeaI_ksSDLGe1llfMwtE85tOcfbBiH0foAcRzGxaLTg6RSsjzDWv9hJw29L-_9lWlFut9eqjDhVAibkDk0W6KEp3m0ya9u85htW0jkNqOEDbzAYB9YlQCSFmqGF_MymoEzNeB_trE-FzyVp9Xh9_dnDTCfeyWZfbIYj4oGacY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🔻
بعد فشل منظومة الباترويت اليونانية بحماية شركة أرامكو في جيزان السعودية
السعودية تخترع سلاح هام و نوعي جدا يدعى صابون نيكوت ؛ مراقبون اكدوا لنايا بعد هذا الاختراع سوف تتعاقد كل من روسيا والصين وباقي الدول العظمى مع هذا الاختراع السعودي لحماية منشأتها ؛ شركة لوك مارتن هود الأمريكية قالت ان هذه الصابونة يعمل ضمن المزلق او اشبه بالفازلين ..</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85570" target="_blank">📅 20:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85569">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي‏: من المحتمل أن تتوصل مسقط وطهران لاتفاق إما الليلة أو غدا حول هرمز.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85569" target="_blank">📅 20:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85568">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي‏: من المحتمل أن تتوصل مسقط وطهران لاتفاق إما الليلة أو غدا حول هرمز.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85568" target="_blank">📅 20:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85567">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: إحراز تقدم في المحادثات ويمكن التوصل لاتفاق بين إيران وسلطنة عمان خلال عطلة نهاية الأسبوع.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85567" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85566">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ترامب يوجه بعدم مهاجمة ايران يوم الجمعة، القرار يمنح الدبلوماسية مساحة، مع بقاء خطط العودة للعمليات العسكرية جاهزة إذا صدرت أوامر جديدة.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85566" target="_blank">📅 20:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85565">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
🇺🇸
لاول مرة منذ 13 ليلة   لم تهاجم قيادة العمليات الأمريكية الوسطى ايران ولم تنشر اي بيان !</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85565" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85564">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇱🇧
🇮🇱
اعلام العدو يتحدث عن اطلاق صاروخ من جنوب لبنان نحو مناطق التوغل</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85564" target="_blank">📅 20:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85563">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881aa0985d.mp4?token=Za76hng3Z8PJ5wuuw_mw680vEHrz17DTngwyqdWkFCfZOJvAEcG3Qc2Gq1D7VQru7Bywy9PzA6yJ-1ZR8onOTW8tiSAI2ClsRfst_fQRxRsQ8_GGk6HISxZRTzWwiZ_ni5vyuUe42Gbn9lYtZrWU4DEKvSf5pMr4iNhPWo2SAgg3g_HqPdhuPfwywfep9bs7RUt8iJaiKeOPILvFcDJI8BNmklZmbV_oDizwqUTQevxsRO4Vuq3_mWWH5UR_zBmCgm9qixQHJnnS0WF1UWOwJTJmoziN31horoxswD66wqezpj2PC4D6xczlyTh31kXgZo5KR_UsPLg1ORJ8-VNTRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881aa0985d.mp4?token=Za76hng3Z8PJ5wuuw_mw680vEHrz17DTngwyqdWkFCfZOJvAEcG3Qc2Gq1D7VQru7Bywy9PzA6yJ-1ZR8onOTW8tiSAI2ClsRfst_fQRxRsQ8_GGk6HISxZRTzWwiZ_ni5vyuUe42Gbn9lYtZrWU4DEKvSf5pMr4iNhPWo2SAgg3g_HqPdhuPfwywfep9bs7RUt8iJaiKeOPILvFcDJI8BNmklZmbV_oDizwqUTQevxsRO4Vuq3_mWWH5UR_zBmCgm9qixQHJnnS0WF1UWOwJTJmoziN31horoxswD66wqezpj2PC4D6xczlyTh31kXgZo5KR_UsPLg1ORJ8-VNTRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
من مطار العقبة في الاردن حيث تتوالى طائرات النقل العسكري الاميركي بالهبوط.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/85563" target="_blank">📅 20:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85562">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇱🇧
🇮🇱
اعلام العدو يتحدث عن اطلاق صاروخ من جنوب لبنان نحو مناطق التوغل</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85562" target="_blank">📅 20:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85561">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00bbbd525.mp4?token=T5DZc-Hod6ZRPbykXvVAkQaKHndQUNq3BLov_RS2ZKlAqZbOYdyIMrfeyU3QHKOsJOBBKNNTMQv53dd3vpAR2rWsJr7U3eOSFr8TzBPyqdxXLmlAiE0yAp3nPau-EosaM8BLU8qEJ0nrcOov4yhm4N1fcs6GeuBj7yZGfMWfqfOQIu9de4A7niDdw8hEhuTmlTrL92J69IkR5j_zLr7INpL7H_GMu8pJh4g_3jIbW_9SXZxLwENBWZjIN72g37pz8F6WfOPbk38kYdgm42O7-YSWHVnuP6hZH1vyxFFpLNdfUu5GSGDq7QrWQt-A1zRo3z12LIJMFx6QcxBRJzEMGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00bbbd525.mp4?token=T5DZc-Hod6ZRPbykXvVAkQaKHndQUNq3BLov_RS2ZKlAqZbOYdyIMrfeyU3QHKOsJOBBKNNTMQv53dd3vpAR2rWsJr7U3eOSFr8TzBPyqdxXLmlAiE0yAp3nPau-EosaM8BLU8qEJ0nrcOov4yhm4N1fcs6GeuBj7yZGfMWfqfOQIu9de4A7niDdw8hEhuTmlTrL92J69IkR5j_zLr7INpL7H_GMu8pJh4g_3jIbW_9SXZxLwENBWZjIN72g37pz8F6WfOPbk38kYdgm42O7-YSWHVnuP6hZH1vyxFFpLNdfUu5GSGDq7QrWQt-A1zRo3z12LIJMFx6QcxBRJzEMGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اعلام العدو يتحدث عن حدث امني جنوب ضفة الغربية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/85561" target="_blank">📅 19:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85560">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇱
اعلام العدو يتحدث عن حدث امني جنوب ضفة الغربية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85560" target="_blank">📅 19:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85559">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">غضب واسع يجتاح الشارع العراقي إثر قيام مديرية حماية الحرمين بأمر من اللواء المدعو أنور النصراوي بإزالة صور القادة الشهداء ومنع رفعها في مدينة كربلاء المقدسة بدعوى أنها تعد من المظاهر ذات الطابع السياسي كما تم اعتقال عدد من الشباب ومنع إقامة أحد المواكب الحسينية…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/85559" target="_blank">📅 19:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85558">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COx8e5w8paMWAqYkG_vf7J6kmI-zjid8csCHcYwNxiWtY_EAu28ZQj717TwyEk1H6HdoeYxdQPuQT2F2t6ZzatU-BrOhlrHeZiqOwojMsBP46edOf-6ISXVic2tgTFl9DG_q-HYcESMSMwHxkUd4RlqsvsiE8mIUocsXgLZejMgV0v1bKDmo2tMyawVcSXhsGtdW67aBR7Ea90eebKMMdKB7pO8MRopqfHSANimYusSjkLd3-RhLd-mJFYuf7FnBbZqYctT1vJgqfGcbyPuSURH9-NB_aca03RVTbuLFrMgZU4bsQfFRs7H4pZixDfBqpC_4eKCzrm61-DFubqjPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
ارتفاع اعمدة الدخان وسط محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/85558" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85556">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EOfCQJe8LuFzl8OG555Qa6iR32k00iZYTVHkRD1D3ejGqZi_DdafBZAjJxo8OnB91EJBhIqEzPk5zNt8t7jH_pBu9L6JLlNZQKcUPsS3cXySL-Pz84EB73MsL5h88MpfCQnCIOKpq6FJWI3oOtmeHu-JnGqtUa6jFEC4lkcLQ5gPnBbFeAc8oghZAaCeesbEa5YRxcSRQV6H_UN3RHXaINbQB36a9ql6sB6Duupy9X1QfAg4ThB3MEfJ4ZsBvcuCAkn37Z83ZNLU_DcM0zI3v7fsngDLlGarraxGQdqrA_P35PKkwIx7Tp_HOLjuDWC4dXcNYUKu60c_mDwcI8PDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfBEdIWCT58c1vK0OPLFQtI0jPWYF8sBQAD0-m1I7jS-CEtvmy1LuhV6Ok7oILSKr0sIMa2F-1175T0aerRXbRY4wD5bF2S9bX8iitE9lpMZzflolBahwbH_evllD5JOJjiomkbnpJ-AmqjI0LuFbfVMcbebWiR0z81AbyG8-u8viiA5JV495YvYThuwGnh84desUkkn5u5e7A8I5zt4ga9V81eX8GK0f1yhxMaIXhHiY9nqqoxP-wFRGwnmap_Iv4tPWSkGBTS9H7ck_cfjqY1-noj_5JHsKGWIE4zN67vwd0_LhbTFMvqf7TbGguA8WXvvCMT6xVoS3zeqeBUmGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
مشاهد من مطار أربيل الدولي شمالي العراق، حيث تواصل عشرات طائرات النقل العسكري الأمريكية عمليات الهبوط والإقلاع في ظل أسباب لا تزال مجهولة.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/85556" target="_blank">📅 18:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85555">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇱
اعلام العدو:
الهجوم الذي كان مخططًا له أمس تم تأجيله إلى موعد غير محدد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/85555" target="_blank">📅 18:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85551">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9dJnUgq25JU_8qcpr223mVqRonQ2LhalAiire0OzDPRjj9lqxK5KyPr_TSI7rI4Mr-FIebTan4JjWEQ-iM0y2-7LL_D-jtQ1PkuOVsDZSpf0nQQugZ7naRJxtoTrfN73SuC1-WFV4sByiC-yGbBbdH7r47TrgYOeZu3P3KQ1OY_FuExJmY_qmnOduWqUCGQf2bQS02xT-3f8kgImxuPYselzVdh-72MuNDGe4GOJ6qOesx4Kz9QeT4ailWZGOKs1ExL50Mk7nB7jNVgowxdaMbbVAyhayo0vdiz4CULhqIrrjw7xsFkfD1e9AQSZwswjL-VWONVhSsQymbVxE-LYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lx29okoRZRVbtDWoLQdW2sDoB2-A0R3vOtmT-x0Rt3Qno6c_4DLZZQo6F9iEe4sVJ2Y9FlrlrxCDa2Kylb-VKtnqaNoS8HsjJENq0RnC-gFRbW4MiKZF4nFCzCGaPcSy3-8QN86Q0Wu-X9J5LZu8B7REDJx8d_f57l4g_FpOZzlWRTOFJ7Mxfq0X74gHHJARM0UDutH1mXv1NeOr6XUQUhd2LHbyX69qw7t9b1aQ6rM0Ul0TGjA6czsidqkhxfLwl3rTFes10WX83Wp8TfryqcJeQINYTcnQHMiskzvVSeIK89O5kOWxuqXx0asm8qeeb3pFT2SwYdi0yzNSwfAfIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_JQ1guYhkc1yMnxh-haEhpjJJCXk5ZrGWwQBquGg0CUpKL_k2i5jvH1N8_HfEbYL2cn-o7Wl2cyiqq_d8eRXtuxUDQlPDf8Fx3dyqPIT5TnP8s37A1ff4Yi1ih48ZUTgIO7JCjUNWP40amD1b_fdT_nUZ4dVkzCmoGiHuM4od8DpPOVJuMoYO_GXn61Mj1XeNdtcFrnDppSsw7BlDhjAX9kjZF7wUaVzxWmZLgEiJuAsfb59fj-qrJc32LJJ8QmwtnF4NvAsW5Foa8jMBRVEofWKEiu4Xpq9J40BnVF_D9aKPygRK6tC8lnlqyF6AA6QMpLx4e8GZ4bYa9K1E9KhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5a389e95.mp4?token=csqb8fa4jjZWanUFj3KZFBuHLl8qPUrzuI3KlwWmen-mAM7PwZyZYjklvkE7ft7bxLZdDvfY3a1yYothvx0YXNV5ao72sa-ChOSaQbZbrbiKScDqpq-M8HIOBMFAGap4YYYRNkBgeay1-h4CVYkKlR003ld8V-o58MRyv9YbyUtp8bBuLvKVSJavbjQhly1IB6KjJtZPibKG_6ocrL-sD_HuI3ZIysBnAiQU1nM-7lm8F7_ZZAmMynfXkTvlA1f6lN4idXNDDzmHS9wSikLgTD992U_BOCIyn_QFwRZNVxHbqz1gqPls8dPVzMnv3y4_NPKsUi56c8zM9H7EwlbD9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5a389e95.mp4?token=csqb8fa4jjZWanUFj3KZFBuHLl8qPUrzuI3KlwWmen-mAM7PwZyZYjklvkE7ft7bxLZdDvfY3a1yYothvx0YXNV5ao72sa-ChOSaQbZbrbiKScDqpq-M8HIOBMFAGap4YYYRNkBgeay1-h4CVYkKlR003ld8V-o58MRyv9YbyUtp8bBuLvKVSJavbjQhly1IB6KjJtZPibKG_6ocrL-sD_HuI3ZIysBnAiQU1nM-7lm8F7_ZZAmMynfXkTvlA1f6lN4idXNDDzmHS9wSikLgTD992U_BOCIyn_QFwRZNVxHbqz1gqPls8dPVzMnv3y4_NPKsUi56c8zM9H7EwlbD9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غضب واسع يجتاح الشارع العراقي إثر قيام مديرية حماية الحرمين بأمر من اللواء المدعو أنور النصراوي بإزالة صور القادة الشهداء ومنع رفعها في مدينة كربلاء المقدسة بدعوى أنها تعد من المظاهر ذات الطابع السياسي كما تم اعتقال عدد من الشباب ومنع إقامة أحد المواكب الحسينية الأمر الذي أثار موجة من الاستياء وسط مطالبات بمحاسبته واتخاذ الإجراءات القانونية بحقه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/85551" target="_blank">📅 17:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85550">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
انطلاق مؤتمر نداء الأقصى 2026 في مدينة كربلاء المقدسة ؛ بمشاركة وفود من 60 دولة، تحت عنوان: "الثورة الحسينية والسردية الفلسطينية</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/85550" target="_blank">📅 17:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85549">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇾🇪
رئيس المجلس السياسي الأعلى اليمني مهدي المَشّاط:
للعدو السعودي نقول لن ينفعكم من يُمنيكم الأماني الكاذبة. ما دون إنهاء العدوان ورفع الحصار الوهم والسراب.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/85549" target="_blank">📅 17:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85548">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇷🇺
روسيا تمدد حظر تصدير البنزين حتى نهاية العام.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/85548" target="_blank">📅 17:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85547">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2a3994f0.mp4?token=tmzua2Fbjbay40pD1ImZN5E3LxWnbu1A7Qw-W9kS42o9z0qVloH2_SZzq3EEukuLiweBEdG7dvWINkVR-DUqZj2Kz0nnfiookRXZwYjDXgZLtAGU2dmHXFSUJipcENUo5nhrXRRgClC4nxtVijP_RDHl0jBgdgkF4jfNEvUw36bwlUcO__HovyxKOsYwO5EsrMRp2JqQ5iM1g9k-3RA1aobQPzLzw69315vxWN2nqCWsVzffS_X8L1vMevPyco5IiBX-6G6vSY1flpSmHWcsVKeyTN1I69MVGSWR8wgymI1jyMyd6KpwbENQq8xBXsO2yxgnHUjfx-ebvCjrz13Grg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2a3994f0.mp4?token=tmzua2Fbjbay40pD1ImZN5E3LxWnbu1A7Qw-W9kS42o9z0qVloH2_SZzq3EEukuLiweBEdG7dvWINkVR-DUqZj2Kz0nnfiookRXZwYjDXgZLtAGU2dmHXFSUJipcENUo5nhrXRRgClC4nxtVijP_RDHl0jBgdgkF4jfNEvUw36bwlUcO__HovyxKOsYwO5EsrMRp2JqQ5iM1g9k-3RA1aobQPzLzw69315vxWN2nqCWsVzffS_X8L1vMevPyco5IiBX-6G6vSY1flpSmHWcsVKeyTN1I69MVGSWR8wgymI1jyMyd6KpwbENQq8xBXsO2yxgnHUjfx-ebvCjrz13Grg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موكب شهيد الجمعة يرسم لوحة بشرية على شكل سيف شيعي</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/85547" target="_blank">📅 16:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85541">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLqgiSXGeMFdfE4qVH21Lpj8zn02AfVM4AW2gBQVuq_2lkeZjVqhNtQ6tFJqFql1gSwWRy73l2ChsLIaJIsI3DMNKxtNyVNu5G9x46KfAoLCmS0PFa0YXsno37DGZbY7Qbf9sjdBrTGcvvc5RUtC8nhxz0DE6Jl1uwCKB5wUJ3U_pN_cCb3CbIKftj69BPPwohj8UVMxGMslKT9fPOFYesNn5A4IEOVGbdZ_O173SwLX1AKbufdJ9edGE_1jmytffJL7ihEYyj_wNa7qMGXGMIg6f-CVAnHpeJ4ihI1WtUquIVHbA2KIL5PqbzonUYmL4i-_h6jpESvrXOamNAPcKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-zfj6GYKgQncM6nXvZUaYrF_Cd_PSHR05p_dAhKM986jkWInhCHhjUgjxJjKP-Et5T_l4wWXYGUgPDCdt7b33jnlouVaSwfCRLBsonJVybNqmorlHp0I1bmirIAtwKucu1NbPvE9JOIIbPVAdR7DVVbzZZ0bBKWCPRRXsLqHjoUGgpWNO7VwNFYPzA4besA7byd8ayM_Js0ETCLQ4EORQgVMbcBGNG1kUoG9iURpzA5Jg0JYZOt3HVXAWdyA6RQY010e4r9n6Cf59GtLPggAhE0DMV-dkqLzLvLuVhYUi5j3y8WBXW8oZ7_S-iR_yX5_Few4rBsakGHnArxmlFA2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0gjgsiYHP7TzRnu0SoOTEVf83EIfy8i7UeTghhy4mGOqlnHB_cwHUc_0N-f7WbV6-XYQYW0BqHTFo0WUiDxHyCHK2L-ovDZFim8nEv5bQDWqvImqCeP6OKj4LMg5wr3cAHdNCe4FWeItpSlSF2Nm5xZOPGgJ7CUCK0vuV1enXvFYrZX-ckbOljIstZ400MgCh0FrPV142phVeSR8M_J7uH4YUvQc1qHpnaI9PB05HM6_GpXRlX2hlN45gatUKATh5mBrX39j9wrbO7iD910WdC7qM0uEh9oasbh5miNYqwcXDR6yjLZKAoEFVGOhhYzRo2hPeHYuTcwwd0YZ6nMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icg81f6inW7V_YCTRLuBYWxliq-7aV3NSL_zrYCqAyrHIqg8BvnyfAfycxIjMa8XK3XfVlCae4LylSDVdPQwz8aXPcNkoT1yUnAQuaGBnpLfUYtAg_l2mQUjkNUHEYC-J8Pc5j84uXChv_EWhw3Rf-4MgE5yUnehjuVM5UWRvYfv2BhGzIqe_SS1xcfAfBnhAbYN2fygp69vzwDGlU-lDojPei_xTzAqJpOuSJlkiPCAVo2b7yMibGMrEJkxHd_l7AJ82Baia95o3fZkcTM_Cy5LWq7JJ1QUi3bBa2PK33KoIU8JZs23SzvyQsj6iewigiH0DC18E-SjJu5TglTFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nV-0y0xza2JWD4RS08ixXvt9hK3Eb2L7UlI6CbAfpwezqTAd45tAMx6ENdieEHslbsHJXgYDknuATndvkKV-mkpSqQJ4btaU2sMfLYgqi1a2lboYjJcNjNBxnhrUIcAdjoWmjaGaWEX7vAwBaRqeG9X7pOh1kTnQc1RxrG9tDhFY9P90duEwSBIEqLn5w9-QbCB5-d0InEpDL3qH60Wif3K481_9mwU1xAU0aGEPRgor5Rqj_apkT25EFpln9qu6pX5XWJ6yQRFzawN812LfXZKb5sJ9ZHaBuVzip-XpEn17cl3GDP1gTttNGYy-fGcrOtF2ivybj0WI-Rht3dLX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdtPIEtloC5BmlFs-ze0-vU2t1xFPLbhGRpkAFb6qHmHpkE59BEQM9zU4DYHy1pj4C1BYLuy-LC--j-HXFAwM6XdLh4KF8XC0Vvfnon7t8J0SqsppSiXUwNbJULI0Fu_CrtaYViDhz_HGZT4L_mGYYmFBefEt74fbhRIoKAeqbnI60oObgn5PoEn_birtuJUIbLYkSUyQjGTdJTBmhfA-hofQsbhVKhERVcGC0kAxuDa1jvYeVCRGRmjvGA0vWBY2WPfmjDlLqbP4FBBUbo593IGhwidY-pVXTiY7y8Dr_uh2NTfPEEP_Dg0wXMfDe0OlSoieOIapLJN8x9Etedfxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عرض لوحات في طهران شكرًا للحضور المليوني للشعب العراقي في تشييع إمام الثورة الإسلامية الشهيد، تحت عنوان: «لن ننسى وفاء شعب العراق»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/85541" target="_blank">📅 16:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85540">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏التلفزيون السوري: مقتل 19 شخصا في تصادم حافلتين على طريق تدمر دير الزور</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/85540" target="_blank">📅 16:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هجوم يستهدف القاعدة الامريكية في اربيل</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/85539" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/85538" target="_blank">📅 16:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/85537" target="_blank">📅 16:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/878fcc76b7.mp4?token=ULPSEEBttFDMai5TQM5gi-X42El6pKB00P6p-kaz9tyMWHyxyp8D57fQmBFUobEHOawvjF2XKc1V59yZgGW0T0hrNVP30QaDVxh29SJkVUw1gBPKEK34ybcAOGqkTrKMYITGqVnkyIDns07c7C-zqYa6dn6CV3gXvzBnV_mWyCaztFUv524g5jS2TVb7WtE6zhb1F-FUbAxKTfdshjiZQ3S3ZhROc99PK_7k0INVmZmxjLyV-rjYz1VuLCPRMd3EcsqM_q-LMXTZx2u4czITPB64IpoadTb4kIbnN621veUGwEIptyvq-AIzHZaC8yTaRRyqDkkRddyjguszSiKY6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/878fcc76b7.mp4?token=ULPSEEBttFDMai5TQM5gi-X42El6pKB00P6p-kaz9tyMWHyxyp8D57fQmBFUobEHOawvjF2XKc1V59yZgGW0T0hrNVP30QaDVxh29SJkVUw1gBPKEK34ybcAOGqkTrKMYITGqVnkyIDns07c7C-zqYa6dn6CV3gXvzBnV_mWyCaztFUv524g5jS2TVb7WtE6zhb1F-FUbAxKTfdshjiZQ3S3ZhROc99PK_7k0INVmZmxjLyV-rjYz1VuLCPRMd3EcsqM_q-LMXTZx2u4czITPB64IpoadTb4kIbnN621veUGwEIptyvq-AIzHZaC8yTaRRyqDkkRddyjguszSiKY6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعية التي التقطت مؤخراً اليوم تظهر نقطة اصطدام مباشرة، يُرجح أنها ناجمة عن ضربات صاروخية باليستية إيرانية حديثة، أصابت ما يبدو أنه خزانات وقود في قاعدة موفق السلطي الجوية في الأردن.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/85536" target="_blank">📅 15:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85535">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇶
الغاء رحلات شركتي A Jet والملكية الاردنية من مطار اربيل الدولي شمالي العراق.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/85535" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85534">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مهاجمة مقرات امنية تابعة لنظام خليفة في البحرين    الشباب الثوري البحريني يدك تجمعات امنية لنظام ال خليفة ؛ اشتباكات بمسافة صفر .</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/85534" target="_blank">📅 15:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مهاجمة مقرات امنية تابعة لنظام خليفة في البحرين
الشباب الثوري البحريني يدك تجمعات امنية لنظام ال خليفة ؛ اشتباكات بمسافة صفر .</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/85533" target="_blank">📅 15:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85532">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇾🇪
بيان صادر عن القوات المسلحة اليمنية:
بسمِ اللهِ الرحمنِ الرحيم
قال تعالى: { ذَ ٰ⁠لِكَۖ وَمَنۡ عَاقَبَ بِمِثۡلِ مَا عُوقِبَ بِهِۦ ثُمَّ بُغِیَ عَلَیۡهِ لَیَنصُرَنَّهُ ٱللَّهُۚ إِنَّ ٱللَّهَ لَعَفُوٌّ غَفُورࣱ } صدق اللهُ العظيم
إمعانًا من نظامِ العدوِّ السعوديِّ في حصارِ الشعبِ اليمنيِّ، وانتهاكًا جديدًا لسيادةِ الجمهوريةِ اليمنيةِ، أقدمَ العدوُّ السعوديُّ بالعدوانِ الإجراميِّ الظالمِ بعددٍ من الغاراتِ الجويةِ ليلةَ أمسِ على مدينةِ وميناءِ الحديدةِ وجزيرةِ كمرانَ، وأدَّتْ تلك الغاراتُ إلى أضرارٍ ماديةٍ ومعنويةٍ، وقد اشتبكتِ الدفاعاتُ الجويةُ مع تشكيلٍ من طائراتِ العدوِّ بعد اختراقِ الأجواءِ، ومنعتْها من ارتكابِ مزيدٍ من الجرائمِ بحقِّ هذا الشعبِ العظيمِ.
​وردًّا على هذا العُدوانِ الإجراميِّ السافرِ،
نفذتِ القواتُ المسلحةُ اليمنيةُ عمليتينِ عسكريتينِ نوعيتينِ؛ استهدفتِ الأولى أهدافًا حساسةً لمنشآتٍ تتبعُ شركةَ أرامكو في جيزانَ، وذلك بعشراتِ الصواريخِ الباليستيةِ والطائراتِ المسيرةِ، فيما استهدفتِ العمليةُ الثانيةُ أهدافًا حساسةً تتبعُ شركةَ أرامكو في ينبعَ، وذلك بعددٍ من الصواريخِ الباليستيةِ والمجنحةِ والطائراتِ المسيرةِ.
​وحققتِ العمليتانِ أهدافَهما بنجاحٍ بفضلِ اللهِ تعالى، وكانتِ الإصاباتُ دقيقةً ومباشرةً.
​إنَّ هذاَ التصعيدَ في العدوانِ ليؤكدُ مدى إصرارِ العدوِّ السعوديِّ على مواصلةِ حصارهِ لشعبِنا وانتهاكِ سيادةِ بلدِنا، وهوَ ما لا يمكنُ القبولُ بهِ، وسيتصدَى لهُ شعبُنا الحرُّ المؤمنُ المجاهدُ بكلِّ حزمٍ وبكلِّ قوةٍ.
​إننا في القواتِ المسلحةِ اليمنيةِ وبعدَ التوكلِ على اللهِ ملتزمونَ بأداءِ واجبِنا في الدفاعِ المشرّفِ والمسؤولِ عنْ بلدِنا العزيزِ وعنْ شعبِنا الأصيلِ شعبِ الإيمانِ والحكمةِ شعبِ الإسلامِ والعروبةِ، ولنْ يجدَ منا هذا العدوُّ المجرمُ إلاَّ التصديَ والمواجهةَ منْ موقعِ الحقِّ، وهوَ في موقعِ الباطلِ، إنَّ الباطلَ كانَ زهوقاً.
​ونؤكدُ أنَّ فرضَ الحصارِ البحريِّ على العدوِّ السعوديِّ لا يزالُ مستمراً، رداً على عدوانه المقابلِ وحصارهِ الظالمِ المستمرِّ منذُ اثني عشرَ عاماً، ولنْ نترددَ في توسيعِ تحركاتِنا وتصعيدِ خطواتنا استناداً إلى تطوراتِ الموقفِ خلالَ الساعاتِ والأيامِ المقبلةِ، وذلكَ ضمنَ معادلةِ الحصارِ بالحصارِ والتصعيدِ بالتصعيدِ...
​
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 11 صفر 1448هـ
الموافقُ 25 يوليو 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/85532" target="_blank">📅 15:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85531">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله اكبر
ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/85531" target="_blank">📅 15:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85530">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfeedb6f3.mp4?token=FN42NcpYgzDWlk-qNKmbSRGKYVDwNIBCYicUlLEUsx7ygyj9rhlGU2owp2y05d1it2ZOWQwnIMvC5l7c4BlHIYPv3IWTFHIoliFG15bAiY3neU-juCQDsH9E53NB5Y6Q73vO_NWxp523wAwFX9CFhS9v0Ij6eOWTLNlNAJxRClaS1nPXt3f_Jd--Ru-ztRrFAiF7EYOtZ6dOu9g2vJLnQQfiegHg_8dY_19vOlEvLaszL8S18TQh-rtVgv-NjZxMJ_appoNiE1nPs6kWIRmX1jpCXrzFVRU1MawL9TQt-8n-1EHi4KwGobuL7i94OzbOK-bVdztnlHAMsrBrS-EtfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfeedb6f3.mp4?token=FN42NcpYgzDWlk-qNKmbSRGKYVDwNIBCYicUlLEUsx7ygyj9rhlGU2owp2y05d1it2ZOWQwnIMvC5l7c4BlHIYPv3IWTFHIoliFG15bAiY3neU-juCQDsH9E53NB5Y6Q73vO_NWxp523wAwFX9CFhS9v0Ij6eOWTLNlNAJxRClaS1nPXt3f_Jd--Ru-ztRrFAiF7EYOtZ6dOu9g2vJLnQQfiegHg_8dY_19vOlEvLaszL8S18TQh-rtVgv-NjZxMJ_appoNiE1nPs6kWIRmX1jpCXrzFVRU1MawL9TQt-8n-1EHi4KwGobuL7i94OzbOK-bVdztnlHAMsrBrS-EtfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏التلفزيون السوري: مقتل 19 شخصا في تصادم حافلتين على طريق تدمر دير الزور</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/85530" target="_blank">📅 14:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85529">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ufl8zd4wf0JMN7zIpbWjQEUIzLrJ9nAXihv5zXahGD9Jc-Baxovu8cVDgbB2SbiDzDQGUr6CYbN1CkyUBWb-KbKW-VeNFb12XTO6GGIS0Jm2MLIJy4pBE-erYJ8bXV6kxq21QJyZDsMvcbIookVzVRMPzEYw6QY4HOiPQUgkNXWZ1MjQ4yKZ4fwgj-Cu6ZLFSFWEYLGi7XvKJIt6PSjMAheVmwp8UxuO8ksbl--9OzO-fG5DgYvYQinG9PiOzC9iNtVQqqCiMYAQyXXxhFx8wSvcGv3NyY-tAUrUnnXgeZbvHgOnmq0HtJmm0qQN-4GAwe_7vGt05XSB9CkIFALTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
أمين المجلس الأعلى للأمن القومي:
ستستمر النيران المتواصلة التي يطلقها مقاتلونا حتى الاستسلام الكامل للعدو، وحتى الثأر لدماء الأطفال الأبرياء في ميناب ولامرد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/85529" target="_blank">📅 14:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85528">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">#ترفيهي
🇰🇼
وزير الداخلية الكويتي:
العلاقة مع العراق مبنية على الاخوة ولا نسمح بالتفرقة والفتن</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/85528" target="_blank">📅 14:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85527">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33e9c1866.mp4?token=RG-pzakPd2RsOIX9I1l69AiDwiIzwl3AAvewAI6N13RqAhqCMJ8w-x-MUZW6JZciD2_MYuJm4OEG-l_2n9srqppfgxv4p5wDmTRakd8y6rKGLlfYukxFEZW2sIpZpEOqrpVfWTgl5tbAcqlLXGt6iKy-AfMAYgyzjKPDXMLYj18ByyPD4qIRAnsb2SE9bURkwgOV1DvO-EPO3KvMU9RhdFH_mXOs7kThJL9Ej3RbxI0XRb460Rl6v8YkQBZ8fVGU57bRkx4ho0fLFqLfJrHnQBQGuCogrS2HJrQJv57qPiBR2_d2Cj_KEohrHDk6ixEbmejO92etdCj9ShjMN5G9ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33e9c1866.mp4?token=RG-pzakPd2RsOIX9I1l69AiDwiIzwl3AAvewAI6N13RqAhqCMJ8w-x-MUZW6JZciD2_MYuJm4OEG-l_2n9srqppfgxv4p5wDmTRakd8y6rKGLlfYukxFEZW2sIpZpEOqrpVfWTgl5tbAcqlLXGt6iKy-AfMAYgyzjKPDXMLYj18ByyPD4qIRAnsb2SE9bURkwgOV1DvO-EPO3KvMU9RhdFH_mXOs7kThJL9Ej3RbxI0XRb460Rl6v8YkQBZ8fVGU57bRkx4ho0fLFqLfJrHnQBQGuCogrS2HJrQJv57qPiBR2_d2Cj_KEohrHDk6ixEbmejO92etdCj9ShjMN5G9ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان سعودي على مأرب والجوف في اليمن</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/85527" target="_blank">📅 14:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85526">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇸🇦
🇮🇶
هل ستحاسب هيئة الإعلام والاتصالات العربية السعودية ؟!    تحاول دولة السعودية عبر إعلامها قناة العربية تخريب العلاقات بين الكويت والعراق علما ان ولا جهة حتى اللحظة تبنت الهجوم والعراقيون يمتلكون من الشجاعة والإقدام ان يعلنون ما يقومون به بلا خوف ولا تردد…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/85526" target="_blank">📅 13:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85525">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بعد قليل ... بيان هام للمتحدث العسكري للمقاومة الاسلامية سرايا اولياء الدم  ابو مهدي الجعفري .</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/85525" target="_blank">📅 13:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85524">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">زيلينسكي المهرج يزعم:
استهدفنا سفنا في بحر قزوين تنقل شحنات عسكرية لها صلة بإيران.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/85524" target="_blank">📅 13:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرايا اولياء الدم</strong></div>
<div class="tg-text">بعد قليل ...
بيان هام للمتحدث العسكري للمقاومة الاسلامية سرايا اولياء الدم
ابو مهدي الجعفري
.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/85523" target="_blank">📅 13:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات في مأرب</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/85522" target="_blank">📅 13:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجارات في مأرب</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/85521" target="_blank">📅 13:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85520">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
لوحة نصر 2
تعرض هذه اللوحة يوميًا هجمات حرس الثورة الإسلامية والجيش الإيراني ضمن عملية نصر 2 على الخريطة.
https://nasrdashboard.com
يمكنكم الاطلاع على تفاصيل الهجمات ونتائجها بحسب التاريخ والموقع الجغرافي.
مصدر المعلومات هو الموقعان الرسميان للعلاقات العامة لحرس الثورة الإسلامية وجيش الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/85520" target="_blank">📅 12:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85519">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFrqpV7qYYuXqcdPjwNtbSdWLkwK4NnEGPd-6iy63CS7XmsvJZB6BxkeXoao-DoSF03JDoG8g0Rr3OTJLuqHVPioouuGqv5iJ848ywkLaRB07-iRyINi8UQUjPyAzNaCl3RQ6GgydzQPh8MivgDDh0KP6cwOVggnxc5T0nFnuFECO034GGiG1NlzlwGS7c6OlbkeDxah77v6XkenaIgbZjnbnxEPXy8htI9Lf7lCLmHr6OJToG5zL0kRU4mMAQj3V69706_ZBydUwqnflyXkkHpsjJmZttiXJfE0dofLjcl_ikPQTM1cNLTPkHnicLUZGy8khbciGIBx_UxyuDX5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
وزير الداخلية الكويتي من محافظة البصرة:
خلال 48 ساعة سيتم إعادة فتح منفذ العبدلي.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/85519" target="_blank">📅 12:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85518">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هذا هو اطول وقف نار منذ ١٣ يوم   امريكا وايران تتوقف بتبادل الضربات منذ حوالي ٣٠ ساعة ..  الهدوء الذي يسبق العاصفة ؟!  ام ان هناك مفاوضات غير معلنة ؟!  كٌلفت دخول أنصار الله للحرب في باب المندب رفعت حجم التكلفة على امريكا ؟!  هل ستعترف امريكا بان مضيق هرمز…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/85518" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85517">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هذا هو اطول وقف نار منذ ١٣ يوم
امريكا وايران تتوقف بتبادل الضربات منذ حوالي ٣٠ ساعة ..
الهدوء الذي يسبق العاصفة ؟!
ام ان هناك مفاوضات غير معلنة ؟!
كٌلفت دخول أنصار الله للحرب في باب المندب رفعت حجم التكلفة على امريكا ؟!
هل ستعترف امريكا بان مضيق هرمز والخليج فارسي تحت سيطرة ايران ؟</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/85517" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85516">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
واشنطن كانت تسعى إلى دفع الأمور نحو التصعيد وهي التي انتهكت الاتفاق وأوصلت الأمور إلى الوضع الراهن.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/85516" target="_blank">📅 12:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85515">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzXro-mBiI6WNg9dCjLgvz_LoejOhuoC9FKJH9QL1ZkaUV9b85wF2NDsXxvXaVn6V4OqG5Gx8V5LyLb-3dGlXfU_2UwKNCyzpTUMNe09elKM6_AGFPFyp3BZS556R6ia9qMK2m7-Tm_bsA8nxcd8CzZvjKLsFCGcvSJ-tYq3gJauFeTjlhp2r6OTXjynUA2SFCz9Ajo-oS0M7SuFE--Zi3BoJUKgHVJzlFutvD1ulXYwkI36JbCzOAvBxBcEieRf55aSCpZBPEaH4bbpQjZ9CvCCo_daIl5u7Az5muW5yNFn0iHf51OdZMBkXp8SKswWIOoMMiOy5pZYkemvCuoy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري في الفجيرة</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/85515" target="_blank">📅 12:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85514">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حدث بحري في الفجيرة</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/85514" target="_blank">📅 12:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85512">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇾🇪
الدفاعات الجوية اليمنية تجبر الطيران الحربي السعودي على التراجع ومنعه من الدخول إلى الأجواء اليمنية في هذه الأثناء.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/85512" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85511">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
هزة أرضية تضرب قضاء كلارا بمحافظة السليمانية شمال العراق</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/85511" target="_blank">📅 11:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85510">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
🇺🇸
لاول مرة منذ 13 ليلة   لم تهاجم قيادة العمليات الأمريكية الوسطى ايران ولم تنشر اي بيان !</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/85510" target="_blank">📅 10:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85509">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📰
بلومبرج: السعودية تحاول ايجاد حل بديل إذا اغلق أنصار الله باب المندب
سيكون تصميم طريق بديل جديد يتجنب مضيق باب المندب في الطرف الجنوبي من البحر الأحمر مهمة شاقة. سيتطلب ذلك استخدام خط أنابيب إضافي واحد، وربما اثنين، وعدد كبير من ناقلات النفط، وجرعة جيدة من دبلوماسية الشرق الأوسط السرية للحفاظ على سير كل شيء على الرغم من تهديد الصواريخ والطائرات بدون طيار. لن يكون الأمر سهلاً - أو رخيصًا</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/85509" target="_blank">📅 10:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85508">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇬🇷
القوات المسلحة اليونانية تدعي: بطارية دفاع جوي يونانية من طراز "باتريوت" تم نشرها في المملكة العربية السعودية اعترضت ودمرت صاروخين باليستيين أُطلقا من اليمن واستهدفا مصفاة نفطية رئيسية في منطقة ينبع</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/85508" target="_blank">📅 10:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85507">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇾🇪
بيان مهم للقوات المسلحة اليمنية في تمام الساعة الثالثة عصراً، للإعلان عن عمليات عسكرية نوعية وواسعة.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/85507" target="_blank">📅 10:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85505">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PipGTHeJWNjQfNM0mkhGif0Rz1zhTmP6NmZ7EsDSS372zYDA6IfK2MwYjmGa_lXSVzQdg7XtFvMrhzdrKdPtpMVXbuZQabUMpKxH-5ECS9Tc5T0frOyuSUjzPcKWexKhTz_tICDz5JR02SOX9HUjiWqcPM7fSuMHl3rkw91J7wBlUlqRHFTOb-77IEE49tklWw2sE3LrWiO5Cd9tHDH0Wsb6-KodL6fRHdHNfcIT3LdysZLsQGMtFFBTuAxyLBAc6kUYt0EhWZFI_gF_3Mb6afG1iKNOzjQcc9VVpKb7M-wFBRmmEEYuI9ebjtUE7KbltUltHnwAjdUO-mi8WdOR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBNrvUipUKHjrdsc6mJs8KlwCRmA0lT9MbykDdmaxjG7D8Lyyi8wepHwcz1h1AdtZE9u0q2rQsLBWcv_ouZIy8i3q7P9Cuk9252BqxxFQgAGqcZBKQIc0GAgRsSbtMBYJnlixSmoWQcA_bIYCf4EBEspUdRu9fMDlzUXhhSfYrzWncnghnLUduCVICURvjaH139OXn823bJzdMoQ7mqReoxhIqjLxhNZ1u0ciUmNG2ucwZIf-XgmmT63kZmNeBRnpCvkh5PXfBGjJ_KjsrELVLVM4JUNiHHKOF0161LRjjanNla1ZHzNAn-eGYZ6FhQhLXOZyfvRpJDJHsvjnAzLvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صور الأقمار الصناعية من ناسا تؤكد اندلاع حريق في مصافي مدينة جيزان السعودية نتيجة هجمات أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/85505" target="_blank">📅 10:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85504">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFVQtQHSafITCjpaz4QVwoqNWWzLAarbDkEOcXIf609i_1xu98sh0HthwYgl1mIHDDogod3OKxzZsYJWG_4fV6jtULt4RTjYsZTuyGGnzu1sAdEKgTCBp_vORNoD4261XBNpjlXF0UwypK21KYE4DRo6n8JZZjTU44EmJ6oAJdgztcXoCuhBS6jNi2msvckAxaJluq6gj-vPbI0vHNlRcaL7T8JkOflXIkBMUBaJTSaAwIVVCUB5O2xR1KdH9qmSV6hTo5TjG-k08mnIazxxQ6J8OyJkmYvEJCvsJTjtPjrH2nZGCmh_buaBTjzbPwOigWL2roFSRTnIQr6VLA4b0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأقمار الصناعية توضح اشتعال النيران في خليج فارس وعلى مايبدو استهداف سفينة مخالفة من قبل الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/85504" target="_blank">📅 08:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85503">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86224dabce.mp4?token=JM91oOZ1c2_ygHOZLvt5_oNk-EcvPC2kexLvbX_KoSEwA2Gz42bVLnEfftJ18upSRMV5aKRSKymL966q8VwMcUuPGDIOLKKLGp57c3v13QVLWDyEexf3byBg-8nE54jrLxy6j1QiNeeAiaBZeDlygEyO0LdsbNvsQ2nWTUVGrPD5rBwh1hKWbd5k51C2kkCKoXGZslZHwCKag76fXbEZIAps6dF-k2eBuoSXZhSZinF2vNvz8PIfTtx8mfoga7uDOfqRzFTfhNKFdQInnd9r6Pgud8xb3nnA6bcAu4u7xv-IsQ1o-O2QwkHxpyR0wevCTk0tK5GRO0neO-waQY1BZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86224dabce.mp4?token=JM91oOZ1c2_ygHOZLvt5_oNk-EcvPC2kexLvbX_KoSEwA2Gz42bVLnEfftJ18upSRMV5aKRSKymL966q8VwMcUuPGDIOLKKLGp57c3v13QVLWDyEexf3byBg-8nE54jrLxy6j1QiNeeAiaBZeDlygEyO0LdsbNvsQ2nWTUVGrPD5rBwh1hKWbd5k51C2kkCKoXGZslZHwCKag76fXbEZIAps6dF-k2eBuoSXZhSZinF2vNvz8PIfTtx8mfoga7uDOfqRzFTfhNKFdQInnd9r6Pgud8xb3nnA6bcAu4u7xv-IsQ1o-O2QwkHxpyR0wevCTk0tK5GRO0neO-waQY1BZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏لا تزال أعمدة النيران تتصاعد بكثافة من المواقع المستهدفة في جازان السعودية</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/85503" target="_blank">📅 08:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85502">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoyksrCzUPGZLnENRIah3wdQUgBwqrj1Ik2oiOLAUS31AylUXK4LsRubS7vsGg6j6QG8pOE1hjn5XhQYM6rZXPP0gFI8DM6Opi3oBROjP7fto5LIgbrF6QmHFmFRC7DrXw7Zb2D7xa73jtK9fuaZNlFITSeqmnpOl_b-RAW5XzOYu9ZnjDtsiouBkuWlLLUSaU_jOoyEW9PcHZ-VFqSGUJpPSRMLVskrzL2TAbnygyA1Ufx2VZiSvnFB7e-rdfKb3wQ_HtVk2fo7jvk0lDPUAyCFrDTno3rVTxJMSbS7l4fOGg7bg8X2yS26MTsM_4x96smR3xlTNSgL_8_3ZsIxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السعوديون يتسببون بازدحام خانق يشل الحركة على محطات الوقود بعد القصف اليمني الأخير على السعودية خشيةً من تفاقم الأوضاع واستمرار القصف.
عبي عبي يا طويل العمر
😂</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/85502" target="_blank">📅 08:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85501">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e9e30099f.mp4?token=uhsy1ys-UM0KwO5vqellOFgUUlZhyhNtSxl_jjn9p6VjiMGLX3JtT4kBo-v7JflYpvZuszFmk1UWZ2USApXX2jEy59iE_DRNkHVUs4jVdwMJTEUZxaOmDG-0mvSPxGwlITad1XLRF-1zaKVhkMRxGCgMvlGqgoFeTfTSBfX-XXgYaHiPDzUhIMSbawvriG_VUW0i021BDccg6zCFOm2IL6sp4eLpFhsPHr2CQeramMceFsWH2-ql8VAEKtpE10WkaBtC0BTuBSuuFyt6C4ZsgwdOCYp3EXvZhEYGuIPZyyfzysJp0I-zFzENk35-YAfTK0762gaiOhI_YORAHeVFlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e9e30099f.mp4?token=uhsy1ys-UM0KwO5vqellOFgUUlZhyhNtSxl_jjn9p6VjiMGLX3JtT4kBo-v7JflYpvZuszFmk1UWZ2USApXX2jEy59iE_DRNkHVUs4jVdwMJTEUZxaOmDG-0mvSPxGwlITad1XLRF-1zaKVhkMRxGCgMvlGqgoFeTfTSBfX-XXgYaHiPDzUhIMSbawvriG_VUW0i021BDccg6zCFOm2IL6sp4eLpFhsPHr2CQeramMceFsWH2-ql8VAEKtpE10WkaBtC0BTuBSuuFyt6C4ZsgwdOCYp3EXvZhEYGuIPZyyfzysJp0I-zFzENk35-YAfTK0762gaiOhI_YORAHeVFlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من انطلاق الصواريخ اليمنية باتجاه السعودية</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/85501" target="_blank">📅 08:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85500">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مطاري الأمير عبد المحسن عبد العزيز  و مطار عبد الله بن عبد العزيز في جازان وينبع يتوقف عن العمل موقتا نتيجة الهجمات اليمنية</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/85500" target="_blank">📅 07:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85499">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">Guys in CENTCOM  Where is U.S. Concludes 14th Night of Strikes on Iranian , it’s to late ,
😆
don’t forget to write we destroyed the Iranian navy that we  already destroyed them 2 months ago</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/85499" target="_blank">📅 07:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85498">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghn7Wpm3WL3KCbr17TLKEnloZSd4Izf1tHD-KRHo78neA9fKWDh-dS9erd5je6K35kYC2GLXS8PinYwAZAA_DfmcBxLx9Bq03dT9zPEUypckobcB-hOQLAohgkjZo3nCiGKllL8_iu1aBgtwNuCTrGNxbL3Gcb--V7prcA_kaImxBQlc0_HCadin6XiKD28NwAqfAQZhDdlw0qS1tTF4f8e2hfPMPTXD0eOb2YvJi-GaqDIGgEV3zqN8EhfAIlJKgetfuSrvcYK0X-Keq40TDa3KFgJSK097ePXonhu9PFL6CbrjdTuwZC0xK9JQ7_YKZr5B2kwEkGIUO2IVf4J6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من مدينة جيزان السعودية</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/85498" target="_blank">📅 07:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85497">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هجوم على ينبع بالسعودية</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/85497" target="_blank">📅 07:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85496">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/85496" target="_blank">📅 07:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85495">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e105faa0e.mp4?token=N0L-YfhgoXmeZfQrWEiqUTysR6XSoJwhadsHBfxw0twXo6_WLY_KRIXqdPSysHS-IZDlr85T9jtOmrZSo3IEq3N1tqCioAoRJlKToI0g257qOQkFLqHqNmbdSz907CqFwejZ6SfY1ewUGED97JZSDON3IBu7m25VaBp6lvPINggNZIeTN-LdkbsDHNvaEDmrqk9UhHBDMSgK7GTvDqWV6yO6vYFIiWrH0cfNFJIRbhL8SYTQf3Q4UDQ4H3YHtoWmOm3hBgDA5KquhKeVSr3cIpqCwiQdGQsKvH9DUjjgxzrH6E1y0oKuK7oNG6Gjfi8kRfgrOWcKpgpISI6A0HNXDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e105faa0e.mp4?token=N0L-YfhgoXmeZfQrWEiqUTysR6XSoJwhadsHBfxw0twXo6_WLY_KRIXqdPSysHS-IZDlr85T9jtOmrZSo3IEq3N1tqCioAoRJlKToI0g257qOQkFLqHqNmbdSz907CqFwejZ6SfY1ewUGED97JZSDON3IBu7m25VaBp6lvPINggNZIeTN-LdkbsDHNvaEDmrqk9UhHBDMSgK7GTvDqWV6yO6vYFIiWrH0cfNFJIRbhL8SYTQf3Q4UDQ4H3YHtoWmOm3hBgDA5KquhKeVSr3cIpqCwiQdGQsKvH9DUjjgxzrH6E1y0oKuK7oNG6Gjfi8kRfgrOWcKpgpISI6A0HNXDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جازان السعودية تحترق نتيجة هجمات أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/85495" target="_blank">📅 07:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85493">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b3d6745d.mp4?token=TYJX_Zj1vOW1iRoMTZrX1B210co-9XUQmvfJ39VEvYFOWaOk0lVe_MiupctMnRj7EOeLoT0QRxodekl3MbAf941iIXEueQhALATMG71fBt0j47k19uAuHO6pm2Ou7gnnAZeN70V0-6OumzujcMpIwKQXuclvNG9rT6vHIu575aHQ2zGq1_buejkKfi7DeryqwPkC-xKEdlWwALUPob6eQzQTBgXVKueNQ-6tvFLNZ5dVMOYX5gOUyxGNYE07ea9IX16z0aLsoVdtAK3CF_qjwlIcEPhg82NZX9zy7DB39QybVtmqhTWGYRoltNnMeN0nvy07j_5awFulofr-8VBNGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b3d6745d.mp4?token=TYJX_Zj1vOW1iRoMTZrX1B210co-9XUQmvfJ39VEvYFOWaOk0lVe_MiupctMnRj7EOeLoT0QRxodekl3MbAf941iIXEueQhALATMG71fBt0j47k19uAuHO6pm2Ou7gnnAZeN70V0-6OumzujcMpIwKQXuclvNG9rT6vHIu575aHQ2zGq1_buejkKfi7DeryqwPkC-xKEdlWwALUPob6eQzQTBgXVKueNQ-6tvFLNZ5dVMOYX5gOUyxGNYE07ea9IX16z0aLsoVdtAK3CF_qjwlIcEPhg82NZX9zy7DB39QybVtmqhTWGYRoltNnMeN0nvy07j_5awFulofr-8VBNGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جازان السعودية تحترق نتيجة هجمات أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/85493" target="_blank">📅 07:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85490">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lu1_OSVWRy6e53KDlPWYbaV_GeCHKf_B886GCG2jhTWjZOovNmlLUEkiI5rAroQU9vc9fc9lFH2v6R21JLwikdKD6g16eRVE4SXFyilcMHXOYC5yeqPwBAMdMEuOJ3SlzzDVvVutr7hKeyrMsNmACCBKRhRGhr4Hsdap5Y82xJyWc1uApTShwB0-nt0vIpU1QtbrbPy2GcM1x8bE6jbltMayV9EJNDGotOAQw7QBgkkPrDIkUUV-VqBktAkDZP1STm5voe0vcO0sfOdSNAYyZAoxxjHve6Ha5vXb7uKdvcKcPOVy1eXnh9-VGbdxvWFenM_6axUu1sKvpsJ48AkFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من مدينة جيزان السعودية</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/85490" target="_blank">📅 07:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85489">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq3obwWYv3JXW9RKuLErwM0yShDBWRQpl1UCe6kGNCaPcbOOXZ8QGn4tCYoxAT-zzyPOh6ElrPR_R0Hr4gZxZMhJKF9m6MBaxNQ4UtIapLiC_mNfStqkb5tChF4zGtPyMZu4zqHi4hy8MNKWqRDqlel43jTIqVw9nkWKEgNGADC0u2j1UTBOxug5dzIeQ7_GuIfiRE5XMesM5E74oShcg5-DjAf8CeZIlxQVuBq1aBuGmn3YwMzK9wq-m1NRDzBta36Yby5bV-eia4pfSPV5GLXY4YY6WzLfQF58cohJTh9cZS5C7UCk-eaLMtckGzlL10U-6UKea2pXKzJ1xnT6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد فشل المنظومات الدفاعية في السعودية تركي ال الشيخ يلتجئ إلى الدعاء.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/85489" target="_blank">📅 07:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85488">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etp-B7Ox-YahCaPViXnU2LgXpepb-sd4XUf9kGifZILbNT_6A3JzF41QwCvSqCrPxmBUDRbWHLGcqOYsgUSDanWtzLKEFrK0kTiH7pPBEsFW0VpAAuEoP67CFuCtaNDkAFyrNeRqSK22lEfxfl_ka5Ot6BcAwc8m3UppLbUsKhyF2dSnT23rHHSCoFz8rdbLLu8sr1lfQjQOW1NGiUjEG5A50i64AHpBCzSDL-KZLINmpEviibVX-2J9beQJpVNrU_81LLLer-_BvKaB3ALIqbZysPTzdceYvbsQ10ffHmoKUc2oUzkbwXK9UfytDhQVKdlPMy6WrGLY68TrD9SwBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الموجة الصاروخية الأخيرة التي استهدفت محافظة ينبع السعودية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/85488" target="_blank">📅 07:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85487">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktlrhgi0v4k_ocsb0YSFGiLj5XKSAm2jW_GWQhCl0eiKNAN1CZ1R3X4MeZwH14zv6PBjHKYugOz6ng2r5T5mVvdrdc5gyPqAPXJpck-mPbsFJStmRNH1GSjAIj1qdqVyThf3u_-IoIiprKEagx_g5LGsjPfDKWpbcxBJDB2wIaluh5_xoSqv9WImzwu29vVWwbpdaoU569QiBl071LkjVT7U-tOTfJDGsfiN3UmzeDlUJRDb6b4HcIt_qTUeNXqTUQCTYo3niAFShX_4z-zU_D6IYFSbiUPh9IcyUA83OcEhdt75m88GzzKdItIz2dapSwfL2TVykZe_fBoyykZp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ اليمنية تصل إلى ينبع</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/85487" target="_blank">📅 06:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85486">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWPlk4QD64N9S7OKy30qM-9L5BIq3_4Cmd_yIfKp3ZihRTsZ5Cn5sUb9foT1j-IBGIOoETFqhNMCUtnSHIQ_P7TkqdYP5CQZ12YgOzjiTO6iyxkSZ1R_46SWQLorHcFlfbwbzUE-fJkh5geGZMwgYpBjst_SsSeQR0qmbFWZ5r6cx-eUQjX-6eAcdmJ2KGgQMqIo20XkydwKZah3m96smhdENRZZTdUtsLoV9p0iH8Kq9Y8pI8e1Gv840mDmQ4qMDBB1rPBIBi8CERINSRmfYPk5hfY1e5RwiM2dPgh1nrzA4nEbq1Sy2S5TLDJJCLz9pFodlNEBacMXHs_5D4SjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطاري جدة والرياض يعلقان رحلاتهم الجوية بعد الهجوم اليمني على السعودية</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/85486" target="_blank">📅 06:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85485">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات تهز خميس مشيط بالسعودية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/85485" target="_blank">📅 06:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85484">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجارات تهز جازان السعودية</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/85484" target="_blank">📅 06:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85483">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b79c69b57.mp4?token=lHzd_UX45TSwdCom94FkDae5SwQUnT6yV0sTcyzSty_ZvKoC2w3D1SKRYR4iQE9R7hbZM00Oq_6ZTnIsxPhUAY7Qtl-KTRpE8K2tWhh95uEmO8ooJ3BoE2vbvmYp71hDUJldtzyd2CjgqptJCkIhOaOIB-qUdZS6kbvygiVnjg8dDcE6PKPE0CJByfd4xCRiFwAnF4FZtA2JLIESZfDR-Bvhd8pZJsltg8zyBmQVM1yKQL1qKvVj1l6qctzNIyfGlXR_tcNQdS_HALsTRiOE2Ycrt3TCe72Q7hQLSf009PiqVW2M0lFG90E1lTHLOlVei7NI-YUb9whz3IstpAQ5eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b79c69b57.mp4?token=lHzd_UX45TSwdCom94FkDae5SwQUnT6yV0sTcyzSty_ZvKoC2w3D1SKRYR4iQE9R7hbZM00Oq_6ZTnIsxPhUAY7Qtl-KTRpE8K2tWhh95uEmO8ooJ3BoE2vbvmYp71hDUJldtzyd2CjgqptJCkIhOaOIB-qUdZS6kbvygiVnjg8dDcE6PKPE0CJByfd4xCRiFwAnF4FZtA2JLIESZfDR-Bvhd8pZJsltg8zyBmQVM1yKQL1qKvVj1l6qctzNIyfGlXR_tcNQdS_HALsTRiOE2Ycrt3TCe72Q7hQLSf009PiqVW2M0lFG90E1lTHLOlVei7NI-YUb9whz3IstpAQ5eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من مدينة جيزان السعودية</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/85483" target="_blank">📅 06:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85482">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انفجارات عنيفة تهز السعودية مجددا</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/85482" target="_blank">📅 06:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85481">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجارات عنيفة تهز السعودية مجددا</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/85481" target="_blank">📅 06:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85480">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/593dc6491b.mp4?token=W4o5RiOe1Z87VuFPAvPSK8diYhRvMY8IJhDIbRzt-G25V6iNnfKqn15_0SSTbB0tZzcQJCepmu92SBEk23VdlpfmraSvHdpwJNYsIt_2gPuCBiqXe5a7ZOlFIjit9Qu6j9LKnhAWvcpfM_yx-kbUIgDvUwr-LnCEV9ZgZoZFZwtIiEgTxYgq9HH85OQpTuMToK7zisZ9sJvCm-xcpTAYs0LopEFlC-FqSpLaRrkH7pnDHeApIgX84S_umS5tuysU7EZifeKQO90NG9b4aPVAQbts7SJYaUzY5frNxgIMF7WEttqstrOX17JcvE4x3_UJ5N_jH4P8vwg0jCYhD1v9KgDq17V31hQQMWAqdzEzhKUBddIDeVqLwwVApGiStOXr84oLyCF-Ir6BwMXLseYWTc8wUZ9o298CF3WD2vaLm5KORs3lc_JU0XM_VEvdk8CnDvS8Iz2qpB5qERzrw7Ezn9xyVQ7cF8dkGPFcidZ7NL8XURTiiEl_QbLqdco_2hjZRBKmJAQV2Fi2T8bRGjKNPh63l256yl8digYD8t9wceqHuPijlZxwlcC_Fi1ihCOl42rQ1_Bh12JNT6NSBXahk1zlC1Vk_bTCYBtgjaUOyfgpONf4DjSQ4IKjUoAsTWUV5N-Ig2cMLcECWky9cRihlx7Lido8Jhj97Smg5BD6lmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/593dc6491b.mp4?token=W4o5RiOe1Z87VuFPAvPSK8diYhRvMY8IJhDIbRzt-G25V6iNnfKqn15_0SSTbB0tZzcQJCepmu92SBEk23VdlpfmraSvHdpwJNYsIt_2gPuCBiqXe5a7ZOlFIjit9Qu6j9LKnhAWvcpfM_yx-kbUIgDvUwr-LnCEV9ZgZoZFZwtIiEgTxYgq9HH85OQpTuMToK7zisZ9sJvCm-xcpTAYs0LopEFlC-FqSpLaRrkH7pnDHeApIgX84S_umS5tuysU7EZifeKQO90NG9b4aPVAQbts7SJYaUzY5frNxgIMF7WEttqstrOX17JcvE4x3_UJ5N_jH4P8vwg0jCYhD1v9KgDq17V31hQQMWAqdzEzhKUBddIDeVqLwwVApGiStOXr84oLyCF-Ir6BwMXLseYWTc8wUZ9o298CF3WD2vaLm5KORs3lc_JU0XM_VEvdk8CnDvS8Iz2qpB5qERzrw7Ezn9xyVQ7cF8dkGPFcidZ7NL8XURTiiEl_QbLqdco_2hjZRBKmJAQV2Fi2T8bRGjKNPh63l256yl8digYD8t9wceqHuPijlZxwlcC_Fi1ihCOl42rQ1_Bh12JNT6NSBXahk1zlC1Vk_bTCYBtgjaUOyfgpONf4DjSQ4IKjUoAsTWUV5N-Ig2cMLcECWky9cRihlx7Lido8Jhj97Smg5BD6lmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب للصحفيين: عندما أرحل، ستصبحون جميعًا مفلسين.نموذج عملكم سينتهي.لن يكون هناك أحد لتغطية الأخبار.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/85480" target="_blank">📅 06:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85479">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامب: الأمور تسير على نحو ممتاز في إيران.لا تصدقوا الأخبار الكاذبة.  إيران تتحدث إلينا ويريدون اتفاقا ولكن لا أعتقد انهم مستعدون الآن.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/85479" target="_blank">📅 06:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85478">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇸🇦
🇾🇪
متداول.. انفجارات ونيران واسعة في مدينة جيزان السعودية جراء القصف الصاروخي اليمني.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/85478" target="_blank">📅 06:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85477">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9fd9e3a4.mp4?token=V_B6TGwGoLOR_6OnbFB6iC5tGQYcL2vjm2ao1oyzWAIsZG7X9lAGNapW2FcpXEYHT5mW_r-UjiVj5PSYaJL10aj57JqEPb7ffMTbHwKqmxColSU-goSVIxbKSssR4P3CM78ZN6Dv1TUneSI7Ohy7AUBSNlfBixxlO20zoxyE7mnFNwVnhdSj7mQPuqdOIsNj7C6YJZ26A9Ea5E3cnSivLqNWTSZOZ_anp9iOvqS5Ah7FYTiUNBziIrm1XWK7vUvfEL8Pz3_duZaxsrfBhD4Iju5q7aY3aCSN5oQr_5LRMfBOHoarapyl3JbnWOGVvECABuXrugDH6CH2FXlJ0KV3ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9fd9e3a4.mp4?token=V_B6TGwGoLOR_6OnbFB6iC5tGQYcL2vjm2ao1oyzWAIsZG7X9lAGNapW2FcpXEYHT5mW_r-UjiVj5PSYaJL10aj57JqEPb7ffMTbHwKqmxColSU-goSVIxbKSssR4P3CM78ZN6Dv1TUneSI7Ohy7AUBSNlfBixxlO20zoxyE7mnFNwVnhdSj7mQPuqdOIsNj7C6YJZ26A9Ea5E3cnSivLqNWTSZOZ_anp9iOvqS5Ah7FYTiUNBziIrm1XWK7vUvfEL8Pz3_duZaxsrfBhD4Iju5q7aY3aCSN5oQr_5LRMfBOHoarapyl3JbnWOGVvECABuXrugDH6CH2FXlJ0KV3ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من النيران المشتعلة في جيزان عقب الهجوم الصاروخي اليمني</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/85477" target="_blank">📅 05:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85476">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b34ad181aa.mp4?token=DLuD51Anivzi6mqwCnjOS5bB_ZkH-lu8XAxTKTCMVYtbxhDYeEvyYl-gO55MGeqYre8XIoo13Dl_I2sAK9D7cVBv-NDAe7aKe0lDUWbw8hJMjeolrF9ofBaY1O-c6qLCAKCo7ndrgXGwGWmjh8jJD6KXt5TQgxBRWWo6tHuUle5NErmlYTdSduZ9O3nZPTC0Uz1w2W9SQNKcZMIw927ehwE_9X8NLh9DdGKDkisvvvafECcDnezHw6vni5VO3lltKu6n55hN9llNWd76lF6IPrPXsfJL43xuSufNbjpHR3f5H0TTnjES7zWUcCh-sa72hJUwnHy7i0PLAQS3DB7DAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b34ad181aa.mp4?token=DLuD51Anivzi6mqwCnjOS5bB_ZkH-lu8XAxTKTCMVYtbxhDYeEvyYl-gO55MGeqYre8XIoo13Dl_I2sAK9D7cVBv-NDAe7aKe0lDUWbw8hJMjeolrF9ofBaY1O-c6qLCAKCo7ndrgXGwGWmjh8jJD6KXt5TQgxBRWWo6tHuUle5NErmlYTdSduZ9O3nZPTC0Uz1w2W9SQNKcZMIw927ehwE_9X8NLh9DdGKDkisvvvafECcDnezHw6vni5VO3lltKu6n55hN9llNWd76lF6IPrPXsfJL43xuSufNbjpHR3f5H0TTnjES7zWUcCh-sa72hJUwnHy7i0PLAQS3DB7DAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
مشاهد متداولة لم يتسنى التأكد منها لإنفجارات عنيفة في مدينة ضمد السعودية.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/85476" target="_blank">📅 05:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85475">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامب: الأمور تسير على نحو ممتاز في إيران.لا تصدقوا الأخبار الكاذبة.  إيران تتحدث إلينا ويريدون اتفاقا ولكن لا أعتقد انهم مستعدون الآن.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85475" target="_blank">📅 05:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85474">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ae533044.mp4?token=FW6f5Z-R4S9gwKflu3QIDq-HUF7zynCLjXWaKLDwQZMIzQ4hx35MV77xKWesLLoOrlSJKF07mpTERX8eeqx-RAMzIsFLg4NMzkn8GELm5goAlEYFD0g0CYJSGrVOVKZEcso9Z400uhLPFkV5fhFIP5VntJP98st2qneuNJSrM1p2lxjzQYcFRnVQZ4RQIwkDYDQIgGRrhXzMlHGd5sElIdp2fPEBJKwf11UP-goqDG36UE935aGltJ3LEChmV325LfM-LW4okCDynIfNBnkHztL9cbknaRfF_zoRh9VGcf5tjucIoKnIbMFZMTbXv8dU0oykuVJqW9A4nb33-4ryRQEKmPM-kdhfbxjgWmixLmNUkGmBhjsRiXvoDZNnFVIqLHREPw7OHW1m7Az50i87R19_Dvp7i_4M90AzkBkblMaykrafC4jzkYeTlo_tGEGhnEJglzUJxtVFdgtAsUvgxBAN6SJhsOR1SD4EKzkLtsAQJ0hoVUCIZ-NBgqw4FA8p-MGJnZSwKi_3vh5FHlbbW5b0dyqI-61euJOPhEGfhu8AlzLRkHOKa0z3s8O0GmBA9vrDUEa_KGfZAidNQJ16hJgRum6E-v9baqdi5qhpH7JF2YdTxRQrynyIqjfWpbr2YHdDvyM9PgMctV5i8HdvleFp8tqyztrRegxNELSD7ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ae533044.mp4?token=FW6f5Z-R4S9gwKflu3QIDq-HUF7zynCLjXWaKLDwQZMIzQ4hx35MV77xKWesLLoOrlSJKF07mpTERX8eeqx-RAMzIsFLg4NMzkn8GELm5goAlEYFD0g0CYJSGrVOVKZEcso9Z400uhLPFkV5fhFIP5VntJP98st2qneuNJSrM1p2lxjzQYcFRnVQZ4RQIwkDYDQIgGRrhXzMlHGd5sElIdp2fPEBJKwf11UP-goqDG36UE935aGltJ3LEChmV325LfM-LW4okCDynIfNBnkHztL9cbknaRfF_zoRh9VGcf5tjucIoKnIbMFZMTbXv8dU0oykuVJqW9A4nb33-4ryRQEKmPM-kdhfbxjgWmixLmNUkGmBhjsRiXvoDZNnFVIqLHREPw7OHW1m7Az50i87R19_Dvp7i_4M90AzkBkblMaykrafC4jzkYeTlo_tGEGhnEJglzUJxtVFdgtAsUvgxBAN6SJhsOR1SD4EKzkLtsAQJ0hoVUCIZ-NBgqw4FA8p-MGJnZSwKi_3vh5FHlbbW5b0dyqI-61euJOPhEGfhu8AlzLRkHOKa0z3s8O0GmBA9vrDUEa_KGfZAidNQJ16hJgRum6E-v9baqdi5qhpH7JF2YdTxRQrynyIqjfWpbr2YHdDvyM9PgMctV5i8HdvleFp8tqyztrRegxNELSD7ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الأمور تسير على نحو ممتاز في إيران.لا تصدقوا الأخبار الكاذبة.
إيران تتحدث إلينا ويريدون اتفاقا ولكن لا أعتقد انهم مستعدون الآن.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/85474" target="_blank">📅 05:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85473">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4bb7ba831.mp4?token=oXPpqEBq2mlwepfkT38b5lO3z8UPYus0nb65MJCLpEtTvNeeSj__X_zD6q3NE0SZcwgUGgZsQhK-vZo6DdT1SY69zA6kfY6PDvbMbjfmd9xRUxDwFxBf7YpjmqiaDLrNQMDA70leQQlo8f0qplcoid5NT_iU-P4dQu5vipUQhE-7Hqy_ao4EClpb4UhOpkCi2JEg1bwalcT59sryAdIENRLNBMjvp_ED66eQmcfNkDcRlB7bywc0t6Fbcb6ZhhDRn8BO2CexMYeqPxnm8LMXG_zrTbPLHw3RJQJ8b25czj07tLJjPwK69uAW4rtJbOleP4hRWnMjRmsTXAuurW_pkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4bb7ba831.mp4?token=oXPpqEBq2mlwepfkT38b5lO3z8UPYus0nb65MJCLpEtTvNeeSj__X_zD6q3NE0SZcwgUGgZsQhK-vZo6DdT1SY69zA6kfY6PDvbMbjfmd9xRUxDwFxBf7YpjmqiaDLrNQMDA70leQQlo8f0qplcoid5NT_iU-P4dQu5vipUQhE-7Hqy_ao4EClpb4UhOpkCi2JEg1bwalcT59sryAdIENRLNBMjvp_ED66eQmcfNkDcRlB7bywc0t6Fbcb6ZhhDRn8BO2CexMYeqPxnm8LMXG_zrTbPLHw3RJQJ8b25czj07tLJjPwK69uAW4rtJbOleP4hRWnMjRmsTXAuurW_pkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عملية تأديب آل سعود مستمرة</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/85473" target="_blank">📅 05:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85472">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQzhIp-kkwhpnUmGRlIsKxxbLnjfA8kypq6BbxHkmCRU35Jju6-6AlOlNEMuwxGWCO-LkvcMajGyxPCrZHKhmU4NzSTmcqlXXBMyNDavmE_oxno808SIyoDd89rlqaRDu9QkX5fu8bJFcr8ZrS06H6G0exCvHfdxgCiVwtZZjbslGHYtF1TwC6oiPERiFGVz4aWPMPOSwifmQB3Yv8JpUnaDVFJ3GbP8RKkjqPfHsklpwTEuzHSicKw1NPzI0AXK8E5IyR4qHCLoiFODejqRgjil1_fa9P0aaowNsRoT-_gpvVJNa5p1B8NTUeYKm4CNn11GtusXDJ_JWcZ5-rRSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏تحلق عدة رحلات جوية قبل الوصول إلى مدينة أبها الواقعة جنوب غرب السعودية، حيث تتعرض المنطقة لهجوم صاروخي يمني.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/85472" target="_blank">📅 05:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85471">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">موجة صاروخية جديدة تنطلق نحو السعودية</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/85471" target="_blank">📅 05:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85470">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/85470" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/85470" target="_blank">📅 05:33 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
