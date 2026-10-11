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
<img src="https://cdn4.telesco.pe/file/EY32lHtHo9evz-VhKCNVpx4of5a8pChU7-iYD-H43OtSTCzEgBA6rPByazFJWgIqaoL--UU7ShNFou437HzBIJlTMH1ys13-hm19zDjy8L4K3bGSSJaK_9Iqgl7UIvoO_t32qtvogRKsOBMkIuvu_0aLpgYcsI9CclQbBNvYRTwmHGhCqDONoBTiV6CPbRqD5y8FBan79NaTqjjpWkBSvWEysbSnunbTlTd5d9CjtoI6ut8eLaCk2WJtOQY5Rz8_rWK9pqwASa-mESFvh_oAtLKNZZYVopXh3QFR9POFuDVOpLfmK-PRM9BSKEYC85iJ6Y_wUipPRVbl3eK0bL-Prw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 21:42:35</div>
<hr>

<div class="tg-post" id="msg-73132">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=bryAnmdIHFW8ToqfKBPF4E19DKa27Y28at_c7m994YT4yudIW1Rm3EXuodKcfnhCTar0LbCTNKhVLrEozTT1Kk9rA6KxLwcM636dzScMDfjvtPxZ_vyUwHWZfeU2h0_BVjCye8j0k84MVoJ8lwNJC-r-W3ruFZRsQGLR4h0M1Md8tTvwY66wxuHZnVCxXb4yPo1fYdCmMI7Ppdfm_h7YhfIOGPc5X_tqIc6_e6r_DXPkfguMdsiQXuWgOotYInmD8TO2NogtNbJ6KO5Tddp5SyNybbEd13q-uXcRs3fG-thGniDKIS5JpGnDb_fBr2wttIW_Epo_5zhh-Iu0WLyDtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=bryAnmdIHFW8ToqfKBPF4E19DKa27Y28at_c7m994YT4yudIW1Rm3EXuodKcfnhCTar0LbCTNKhVLrEozTT1Kk9rA6KxLwcM636dzScMDfjvtPxZ_vyUwHWZfeU2h0_BVjCye8j0k84MVoJ8lwNJC-r-W3ruFZRsQGLR4h0M1Md8tTvwY66wxuHZnVCxXb4yPo1fYdCmMI7Ppdfm_h7YhfIOGPc5X_tqIc6_e6r_DXPkfguMdsiQXuWgOotYInmD8TO2NogtNbJ6KO5Tddp5SyNybbEd13q-uXcRs3fG-thGniDKIS5JpGnDb_fBr2wttIW_Epo_5zhh-Iu0WLyDtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه مدعی شد سومین نفتکش از دیروز تاکنون در جنوب تنگه هرمز با مین دریایی برخورد کرده و دچار انفجار و آتش‌سوزی شده است.
سپاه هشدار داد با کشتی‌هایی که سامانه‌های ناوبری و شناسایی خود را خاموش کنند، به‌شدت برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/news_hut/73132" target="_blank">📅 21:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73131">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=JTMYakcFcbVy4tCF-yWhDtch2DMt5LHJ4QYDdJZ1bOCc82qy1gL7SBmnYNSvm_LA9RGccmJn3lYbpI1GAQQXqochgOpHjCg_MaIPhTtUi07kceKVbImi8RAR2MLevo3HSp1VvqpwAoIzrfsQreygcOVzbgWaDAEA4Zc-rLnJOzBV8g3hieHZF8ZDC5Dt4dx7yzSsIrQS-yUU5EBXS9JJoxuF_li_mwC1JEVIG33ATU2poqSqV9hWF7X3c4ye48yJwV0aDLTetZN2ag4wKGlQfREOLV1gi4uSIMDfzxVGRTwZ7uDiW4qmgE-WYo03bCGuPVMA57VhQUZa0oZ5ghlbww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=JTMYakcFcbVy4tCF-yWhDtch2DMt5LHJ4QYDdJZ1bOCc82qy1gL7SBmnYNSvm_LA9RGccmJn3lYbpI1GAQQXqochgOpHjCg_MaIPhTtUi07kceKVbImi8RAR2MLevo3HSp1VvqpwAoIzrfsQreygcOVzbgWaDAEA4Zc-rLnJOzBV8g3hieHZF8ZDC5Dt4dx7yzSsIrQS-yUU5EBXS9JJoxuF_li_mwC1JEVIG33ATU2poqSqV9hWF7X3c4ye48yJwV0aDLTetZN2ag4wKGlQfREOLV1gi4uSIMDfzxVGRTwZ7uDiW4qmgE-WYo03bCGuPVMA57VhQUZa0oZ5ghlbww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم وایرال شده از جشنی که یه خونواده، برای اولین پریود دخترشون گرفتن:
@News_Hut</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/news_hut/73131" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73130">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=sQ0qIcA_JXq4gHOqOVKjTxRk1x5NTnbk5dtQX4Gx1hqyuzT1m36t_RO1XcTEf3in4XsmyD5qtkLu8QfkgYNZTwKuCwD905mGFLoDtY0Ey5TtB_AAh9wh4NRDJAyVtzNjPmrqJBOqNW7Vs8PB8BuUbVeiHUqvfmMKi-oIEtNwNtw7r55-G3zjEZ-wJC5FyusACrTzKQBa3NAjd5RQEL_nFPgXGI6NIEH0k7jIQ50IhPgMTqO7lpCh1WPipHktU2hMwpq5ka52tspYFe9oc4qIKuFCKm0Z3aSwGHmQnj95ReKtyF_JVy3HOhPhJNdv-3GoFbks5d6fQI_iEcR3uRxOBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=sQ0qIcA_JXq4gHOqOVKjTxRk1x5NTnbk5dtQX4Gx1hqyuzT1m36t_RO1XcTEf3in4XsmyD5qtkLu8QfkgYNZTwKuCwD905mGFLoDtY0Ey5TtB_AAh9wh4NRDJAyVtzNjPmrqJBOqNW7Vs8PB8BuUbVeiHUqvfmMKi-oIEtNwNtw7r55-G3zjEZ-wJC5FyusACrTzKQBa3NAjd5RQEL_nFPgXGI6NIEH0k7jIQ50IhPgMTqO7lpCh1WPipHktU2hMwpq5ka52tspYFe9oc4qIKuFCKm0Z3aSwGHmQnj95ReKtyF_JVy3HOhPhJNdv-3GoFbks5d6fQI_iEcR3uRxOBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سازمان انرژی اتمی: منافعمان را یا با دیپلماسی می‌گیریم یا با نبرد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/news_hut/73130" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73126">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=W-8GFaMV6gREUQs0D0BliJKyUW-31qf1EdfKTAQlZJ-VxQ5qH9ICNKf6m71qPK3S09Hi4Z1HNa3vIBmvRXgBjrvwgAzrpsW91Hqr_RsV5Cbrvp_F8bWysq2nkzQ1Fsqt_Q1ryiKXMlxR04_MlGIx2qMqN1S1cTcVN7j1xkXfHaioRrPz_Csjwo5-YclYISNprNXPVVb2b5pyNYXKXikHt2aQdLSeRDOzARO5sBNfTnNvQSeKBT1l525tPv4GLuXSiRYR1qbHqgDD5YOvbzenMFI8cFH1LymCtvPvqVCq7U8rgDZUHbPOc95_eADUwV6tR4oeVnzHVWbgwkv-RgfHfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=W-8GFaMV6gREUQs0D0BliJKyUW-31qf1EdfKTAQlZJ-VxQ5qH9ICNKf6m71qPK3S09Hi4Z1HNa3vIBmvRXgBjrvwgAzrpsW91Hqr_RsV5Cbrvp_F8bWysq2nkzQ1Fsqt_Q1ryiKXMlxR04_MlGIx2qMqN1S1cTcVN7j1xkXfHaioRrPz_Csjwo5-YclYISNprNXPVVb2b5pyNYXKXikHt2aQdLSeRDOzARO5sBNfTnNvQSeKBT1l525tPv4GLuXSiRYR1qbHqgDD5YOvbzenMFI8cFH1LymCtvPvqVCq7U8rgDZUHbPOc95_eADUwV6tR4oeVnzHVWbgwkv-RgfHfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی امروز گسترده‌ترین رزمایش نظامی خود از ۲۸ فوریه تاکنون را با مشارکت سپاه و نیروی هوایی ارتش برگزار کرد. تصاویر منتشرشده، پرتاب پهپادهای انتحاری شاهد-۱۳۶ و موشک‌های بالستیک و پرواز جنگنده‌ها بر فراز تهران و شهرهای دیگر را نشان می‌دهد؛ تحرکاتی که می‌تواند نشانه آمادگی ایران برای دور تازه‌ای از درگیری باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/news_hut/73126" target="_blank">📅 20:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73125">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">محسن رضایی:
«اگه جنگ دوباره شروع بشه، خیلی از کابل‌ها، دیتاسنترها، مراکز هوش مصنوعی و زیرساخت‌های دیگه تو منطقه نابود می‌شن.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/73125" target="_blank">📅 19:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73124">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW-gJb0leROaxJ2RoSOurEkRYKve5D8zbZx8ehY0ja-d8CsipprPimOdGT4pJd4FdeGaROkO69yefkgNjpsYTNmoXQ8tNaHUfpYGm529msgCHa0c_MUaITdmUrPuv47sEZAbKaiju-mFHAlK_6rrAb3GU_0gff-txEAUjZxWEG-fZiP7lLpJPnqLYbN6Un1LUTqtkwtzXAgkhyXbfe5yAOjVpYULuGLr7e-XxEHHkyxeVlWuukVFS32PaISUTdFyqoBHi9m8xFo-E15qh1dUyenWt1kCwgQqXyO2BL14YEbK-QSZhsa5fEYZaNEeVt8vKZAhbkcG9T5rkl9hiMLVug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
«ترامپ به قاچاق روی آورده و با استخدام تعدادی مجرم که در آب‌های ساحلی عمان فعالیت می‌کنن، این کار رو پیش می‌بره.
اون هر روز ادعا می‌کنه تنگه هرمز بازه؛ اما من در پاسخ می‌گم شما مشغول قاچاق هستید، در حالی که تنگه هرمز تحت کنترل ایرانه و ما مدیریت اون رو در دست داریم.
طی چند ماه گذشته، هر شب پنج شناور مورد استفاده قاچاقچی‌ها رو در تنگه هرمز هدف قرار داده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/73124" target="_blank">📅 18:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73123">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee20290170.mp4?token=N8u0KRbKofWGMYEYqDwLZYt0AmyvatkQFTjaRAaCK9dC8UA-92HGNY76WvqdOansZ_-lAkukwjVkJ3ikov1zMp-nhecMkucv1zzHCYRGbbyPULsVXi8ESVqOLpoz1IUk3QjQiz1v6MPc1tKJWYRFtrsSm7uZ4NaC5mE9bCGUFD6Qx8ngLrQqd8wyNWRrTAmCB9FEoCtgflExNs-DqAuUckqf-N-pco3n_6eDkZOrE36F9lD6Z7kpwqmEHz_zZEgZfF6P1PCeLqhIteLmlKWzTdw5kR8hYiNiwHG0wHmJyZ_RD8KYgrB71LnD8aVBksvd97XiuOWJyFfucc_y7WoRhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee20290170.mp4?token=N8u0KRbKofWGMYEYqDwLZYt0AmyvatkQFTjaRAaCK9dC8UA-92HGNY76WvqdOansZ_-lAkukwjVkJ3ikov1zMp-nhecMkucv1zzHCYRGbbyPULsVXi8ESVqOLpoz1IUk3QjQiz1v6MPc1tKJWYRFtrsSm7uZ4NaC5mE9bCGUFD6Qx8ngLrQqd8wyNWRrTAmCB9FEoCtgflExNs-DqAuUckqf-N-pco3n_6eDkZOrE36F9lD6Z7kpwqmEHz_zZEgZfF6P1PCeLqhIteLmlKWzTdw5kR8hYiNiwHG0wHmJyZ_RD8KYgrB71LnD8aVBksvd97XiuOWJyFfucc_y7WoRhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارشات رسانه‌های عربی حوثی ها مجددا به فرودگاه ریاض حمله کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/73123" target="_blank">📅 18:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73122">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">زلنسکی در گفت‌وگو با باراک راوید:
«اعلام آتش‌بس برای من هم خبر جدیدی بود. اما اگر روس‌ها با آتش‌بس در حوزه انرژی موافقت کنن، اوکراین هم موافقت خواهد کرد.
اگر رئیس‌جمهور ترامپ این توافق رو با پوتین مذاکره کرده، لطفاً به ما بگید آتش‌بس از چه زمانی شروع می‌شه. ما آماده‌ایم و این توافق رو می‌پذیریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/73122" target="_blank">📅 18:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73121">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTGXL2q9qwQk8BDeXEYd8MkuWOPGp4PRpGppS6FCnXP6RVJDBWgVMicqcwUQ-_kh8g66YIbIsSzh_TEFcD--0ciqRXQbif_U3VZoFL3J7PNzlOCK2FFUJD-wqdwVT4gIFVJFAdet9WdqfSVYbTDps4Lib_nYNs-hUDYvjRo-vfxwIcELKKAngSss0bifi_jdK2auR4IDkVAmCovKaltSphuToLLnGaq9FalAXYdK_0S5ti9-bjDscB0OicLtAclAkFBm0GRscuqJ5aUhxcI__hESpQIHS83C_XfLxs9CImKlPqD35jgCQyM_VWKHZ6gClwly67zqLkecPWK3trV0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ از آتش‌بس انرژی بین روسیه و اوکراین خبر داد
«از همین لحظه، آتش‌بس در حوزه انرژی در جنگ روسیه و اوکراین برقرار می‌شه.
هر دو طرف با این توافق موافقت کردن. این آتش‌بس رو نقض نکنید!
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/73121" target="_blank">📅 18:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73120">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/73120" target="_blank">📅 18:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73119">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz8-Fo5AB8jJbOZnMrxAOA8UxcofpxzwIkwTWFszJb05hwFNWf56iiQqFgNmSWjjM5U1wXdnAN2E7G1GpdvWXwQwgIzNYAoU3EE_Pgww7HLowwee90u9cRtw7gSg4fJQZhLjBpA_Lk7nRsFqKMbE2ojkAlc0H8Y68XM6l0XGCvARlUR6RdnaxnevqbBg8WulKxJVvtxZnlr9FILWYYAdej0ckzrnE8vs3V6QatAikuCe4_vuXomiPOZFKwnekfT-U6NVFhtFYCLsRmJ2JZpZbKuQ8cwCxyFHQD-Ebl0JYwGD6Nru7Pl_AeCY83ZOUtSXR_SiONFdNWKP0p0rTjZu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز منچستر سیتی
🆚
لیورپول
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
منچستر سیتی: ۵ برد و ۱۴ گل زده
لیورپول: ۴ برد، ۱ تساوی و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/73119" target="_blank">📅 18:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73118">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6d17c940.mp4?token=bFWnSVR5EbGbS2t6aKruAtr15dKGRVtBN_yePede-N4Dax73elX1nCa-hiV9RrXPjSQ3cXBIRQZMZcx3845cJ1JrPItPbURdzsD_1gB_MdEyse_ZseBh9QKjUKVj9c9nJpg9NdePOyHhV0NWWUiGlIaA9BxlSbgasfF7PKx0SPA1uQ1-tDhKaTGiCQ_etAhcBdR6T2dr0MQsg8X3Mpz8IA9KOqvtEhr5lKK1gRpZ350Sc1ELek-4teQVkRZZjh5i4Y3rbM06B9iMf1d_YTmuzMLFzHVguk81yEY7TSEmWdOIOVnAdcYPL-ruOlip4GW4wttNnQ72ziKA6DIX3ImJqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6d17c940.mp4?token=bFWnSVR5EbGbS2t6aKruAtr15dKGRVtBN_yePede-N4Dax73elX1nCa-hiV9RrXPjSQ3cXBIRQZMZcx3845cJ1JrPItPbURdzsD_1gB_MdEyse_ZseBh9QKjUKVj9c9nJpg9NdePOyHhV0NWWUiGlIaA9BxlSbgasfF7PKx0SPA1uQ1-tDhKaTGiCQ_etAhcBdR6T2dr0MQsg8X3Mpz8IA9KOqvtEhr5lKK1gRpZ350Sc1ELek-4teQVkRZZjh5i4Y3rbM06B9iMf1d_YTmuzMLFzHVguk81yEY7TSEmWdOIOVnAdcYPL-ruOlip4GW4wttNnQ72ziKA6DIX3ImJqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
«نمی‌دونم این ماجرا چطور تموم می‌شه؛ هیچ‌وقت نمی‌شه از قبل دونست پایانش چطوریه. دیوار برلین هم بالاخره یه روز، یهو فرو ریخت.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/73118" target="_blank">📅 17:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73117">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=nGXWvdaBHuMOp13va-2ti78aE-9q_DT_gvuIoLg0qEmUZIHosKYouQyjYp58vygqbnrNRze1k175a-af1TdbOPRNeqVvnjfjttfhO0SezERVDqzJCvWpKeq0DmmmqsDxIPalm6Bu8kWeQFrvZcPaHT9dwIxytBF6YXo8n8eyo3gOseIaQ3JR1h9zZsAb4Sr1L4UfXyKm2Jo6_6D_yMXn5AWqG9jEbOUsFgkmZ9_J6xeXmI1Ga-tqDnjFy_Vn8hzxaWHSyyI2CYtdInK5HBR14DsGeU5ozTrWWdgl9M9GKS8fVKlXqAqNh7tEjx88i0yjMNxgeSRRb_1qNUXgtdqe_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=nGXWvdaBHuMOp13va-2ti78aE-9q_DT_gvuIoLg0qEmUZIHosKYouQyjYp58vygqbnrNRze1k175a-af1TdbOPRNeqVvnjfjttfhO0SezERVDqzJCvWpKeq0DmmmqsDxIPalm6Bu8kWeQFrvZcPaHT9dwIxytBF6YXo8n8eyo3gOseIaQ3JR1h9zZsAb4Sr1L4UfXyKm2Jo6_6D_yMXn5AWqG9jEbOUsFgkmZ9_J6xeXmI1Ga-tqDnjFy_Vn8hzxaWHSyyI2CYtdInK5HBR14DsGeU5ozTrWWdgl9M9GKS8fVKlXqAqNh7tEjx88i0yjMNxgeSRRb_1qNUXgtdqe_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
«اگه این ایرانی‌ها کشورشون رو دوست دارن، خب تبریک می‌گم؛ می‌تونن همون‌جا بمونن!
این فشار مستقیماً به نخبگان و مقام‌های حکومتی ضربه می‌زنه؛ دیگه نمی‌تونن برن لندن و اقوامشون رو ببینن، تو پاریس به دیدن دوست‌دخترهاشون برن یا به پول‌هاشون در سوئیس دسترسی داشته باشن.
اونا از دنیا جدا شدن و ما به ادامه این فشارها ادامه می‌دیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/73117" target="_blank">📅 17:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73116">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=lr4jiKPRh0QITzI3PmvFfSOSytVGTxVNg7CV_uIus2RsUAS2AmLXaXoo8nCcitbqn64r46j2U7yODQxRmryQ9088JMTpM_kTJ1x3fwO7blPEBfucxjQSk47L9OMM85pRtxWQ1_wpy-bGYg9lmDTEjx-XLVpWr1zoYTLejVgcFpPESTgx_g4BtF1SaFCUkWRdVKxqbD9dgjVypyOszb7SYb7vkTAN4DgO9AomvMHz0pUAJ0u93YxvwyaOwxnFniauftnasm0EklT3y7jOoVJYK7NXoMmoWqymcdsEQuhBBRw6r6Y_DIK8fufOYNFB1fIK1u4JlxUO3SgHPCHJX1Z-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=lr4jiKPRh0QITzI3PmvFfSOSytVGTxVNg7CV_uIus2RsUAS2AmLXaXoo8nCcitbqn64r46j2U7yODQxRmryQ9088JMTpM_kTJ1x3fwO7blPEBfucxjQSk47L9OMM85pRtxWQ1_wpy-bGYg9lmDTEjx-XLVpWr1zoYTLejVgcFpPESTgx_g4BtF1SaFCUkWRdVKxqbD9dgjVypyOszb7SYb7vkTAN4DgO9AomvMHz0pUAJ0u93YxvwyaOwxnFniauftnasm0EklT3y7jOoVJYK7NXoMmoWqymcdsEQuhBBRw6r6Y_DIK8fufOYNFB1fIK1u4JlxUO3SgHPCHJX1Z-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«بزرگ‌ترین بازنده در این ماجرا، حکومت ایرانه.
اونا سعی کردن با بستن تنگه هرمز، مسیر عبور و مرور رو تحت فشار قرار بدن؛ اما این کارشون جواب نداد.
بعد تلاش کردن با بالا بردن قیمت گازوئیل، فشار ایجاد کنن؛ اما این یکی هم دیگه جواب نمی‌ده.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/73116" target="_blank">📅 17:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73115">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d595a9a29.mp4?token=aQg01greQGQCT1fwPi_hAfa2N2oHJkChBhiB4Ort_VBGwqvdnMy95-cyCC0F8El9UtnFaUs4X4vrcOxxv1zm7uQFY5LK-boInxyfyAuLi4ep8i4pFUdTrpbtK8qyXO65i9Pdwc6zgc8zZcocxZMxI0pCGFZRF7ZbdKJZc7FqYglxslY6DV43cxIhf6TRRlah_sCpGa28XHb1w-KJq-vR5_YlbnJ-3q6w7nmOm-IN3c-nWQlZfWtN4_K2P9NdNjFJ8ogsvBY-rIEJ2C2nIeRAuqw8nQXU2qVBFBg8i2NchnL6F5Lw5c6XQS7nAh3YE0Ix1ujW2qOiHotkIVkc3ZNKVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d595a9a29.mp4?token=aQg01greQGQCT1fwPi_hAfa2N2oHJkChBhiB4Ort_VBGwqvdnMy95-cyCC0F8El9UtnFaUs4X4vrcOxxv1zm7uQFY5LK-boInxyfyAuLi4ep8i4pFUdTrpbtK8qyXO65i9Pdwc6zgc8zZcocxZMxI0pCGFZRF7ZbdKJZc7FqYglxslY6DV43cxIhf6TRRlah_sCpGa28XHb1w-KJq-vR5_YlbnJ-3q6w7nmOm-IN3c-nWQlZfWtN4_K2P9NdNjFJ8ogsvBY-rIEJ2C2nIeRAuqw8nQXU2qVBFBg8i2NchnL6F5Lw5c6XQS7nAh3YE0Ix1ujW2qOiHotkIVkc3ZNKVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«کارگرها دیگه سر کار حاضر نمی‌شن.
ایران به بازار دلار دسترسی نداره، برای همین کاری که می‌کنه، چاپ کردن پول بیشتره.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/73115" target="_blank">📅 17:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73114">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbe1e496c.mp4?token=PYA_ais5gtNGDHBOW54RrF-9w_ysZ74HCzcsgsrC3xJncpjcijobB_2oWoxsy7c9Vk9ziwTy_7EzSfv_7cZi7tz1uUk8z7kQDmx-esos8kkPMHLSA_VFXr-dtUb9zE6r4T1cjSpNyQ81-vJU2BI0ev8xepkZilqM94shWZFEbeJdQUnD1fqeA2WzscO6htvypG6achiH8FzMePtMOzUAUroAexsw74IMQhrWRmV2Lld9uX7U6xBR2GV6zRswMPNcQQ7uss95lgKqRRDopgBu2lN89OS8xdOJQRMEUxZquz0mJVKBHUa6XnPC9Oya3fxPy33tP68aWx1UvwklHLCgvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbe1e496c.mp4?token=PYA_ais5gtNGDHBOW54RrF-9w_ysZ74HCzcsgsrC3xJncpjcijobB_2oWoxsy7c9Vk9ziwTy_7EzSfv_7cZi7tz1uUk8z7kQDmx-esos8kkPMHLSA_VFXr-dtUb9zE6r4T1cjSpNyQ81-vJU2BI0ev8xepkZilqM94shWZFEbeJdQUnD1fqeA2WzscO6htvypG6achiH8FzMePtMOzUAUroAexsw74IMQhrWRmV2Lld9uX7U6xBR2GV6zRswMPNcQQ7uss95lgKqRRDopgBu2lN89OS8xdOJQRMEUxZquz0mJVKBHUa6XnPC9Oya3fxPy33tP68aWx1UvwklHLCgvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«ایران دیگه هیچ محموله نفتی‌ای در مسیر انتقال نداره. جریان نقدی‌شون منفی شده و ما راهشون رو بستیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/73114" target="_blank">📅 17:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73113">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aafe668bc.mp4?token=LFsm0i1vddM2-YFv8Qxj1qW6Kxb0zZakpxgpeeBxpQdemqoSpSp0pQurqQHxh3fLvc2TlPk5GINPAlnuQFz_sbB2vqNcq-bNYLmcQf5q8vRuDnxL0Tl8iYYVlWsP5yTFAH8oJrcU_bVvcN__E-p3py3BUViuPX15Len8FFbc53sQAvoE3NRGEvMCkaXw964MeCaI5eyncWy4WIb7AcMJqqJR-W7boZVtQJcqcjCCIEWdM9q76pwkQ6Xt7nJRayOOwUVE4-ScD8bF3_F-mB2lxKmeWlw_Hjpon1rKqAPmlmaOcKNxi6Igk0chLAUSBJEMk90Nnf7mFIWsCoYX8f6xUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aafe668bc.mp4?token=LFsm0i1vddM2-YFv8Qxj1qW6Kxb0zZakpxgpeeBxpQdemqoSpSp0pQurqQHxh3fLvc2TlPk5GINPAlnuQFz_sbB2vqNcq-bNYLmcQf5q8vRuDnxL0Tl8iYYVlWsP5yTFAH8oJrcU_bVvcN__E-p3py3BUViuPX15Len8FFbc53sQAvoE3NRGEvMCkaXw964MeCaI5eyncWy4WIb7AcMJqqJR-W7boZVtQJcqcjCCIEWdM9q76pwkQ6Xt7nJRayOOwUVE4-ScD8bF3_F-mB2lxKmeWlw_Hjpon1rKqAPmlmaOcKNxi6Igk0chLAUSBJEMk90Nnf7mFIWsCoYX8f6xUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«همون‌طور که رئیس‌جمهور گفته، انتظار نداره درگیری نظامی تا قبل از انتخابات میان‌دوره‌ای اتفاق بیفته؛ دست‌کم نه تا بعد از اون.
نمی‌دونم معادل عبارت «تسلیم شدن و درخواست توقف» به فارسی چیه، اما ایرانی‌ها بالاخره به جایی می‌رسن که از آمریکا درخواست کنن دست از فشار برداره و تسلیم می‌شن.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/73113" target="_blank">📅 17:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73112">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=BtjzbG6vqbOgpoOj5xEeWXJLKqZOKsvm28uLHSvO0Pl_lK_KmXj5lKz3xTi1oGh8Rbl11NYpbV8KBrY8YKIYLKLZ_1aQJB0Xt2jYARTpF5wm_WgdfrbkhJZ5Vcp_6CLkEMci-VG5Ansl4xSkLCq6JvhM5yr1HfJfUXoASod_C8yPcKaVntkoNOwsDCjlRN3g00wtttPckosZOQQO0zDdJhodbaJWBCyvgxc8L7mPNXsaKnjtD3Sp-p6Hy_mq8nLeZ4xZGB1o4WJjTrl5LuiHAe4ArLsOMOjy0fRJ-TQX4xf_4CSd8UQPGDv7yJGT80YEV59ggzXMoVw6v3DY3zz51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=BtjzbG6vqbOgpoOj5xEeWXJLKqZOKsvm28uLHSvO0Pl_lK_KmXj5lKz3xTi1oGh8Rbl11NYpbV8KBrY8YKIYLKLZ_1aQJB0Xt2jYARTpF5wm_WgdfrbkhJZ5Vcp_6CLkEMci-VG5Ansl4xSkLCq6JvhM5yr1HfJfUXoASod_C8yPcKaVntkoNOwsDCjlRN3g00wtttPckosZOQQO0zDdJhodbaJWBCyvgxc8L7mPNXsaKnjtD3Sp-p6Hy_mq8nLeZ4xZGB1o4WJjTrl5LuiHAe4ArLsOMOjy0fRJ-TQX4xf_4CSd8UQPGDv7yJGT80YEV59ggzXMoVw6v3DY3zz51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی یک کشتی در مسیر جنوبی تنگهٔ هرمز بر اثر اصابت یک پرتابه:
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/73112" target="_blank">📅 16:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73111">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صدای دو انفجار از طرف تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/73111" target="_blank">📅 16:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73110">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=P4jTGY5SDRsiq4ZZ85OY-HDocgGnl2xn6IxcnBgQhLCTF4soLaZSlhtYFQRXGJw3hs5xf9MIzkMppFCmxnu0axaQIt3JJ4wPpcDKWseBamV8JqXw_VxSFWGaPYBNyRfWGdoXhRkefA_ELUK5fWDVAu7ZQXzvqIXjDW3EqiKOIN8S8IZFECCmT2zqMzEx5TzN9jzAQNJXK18CwRFeqt26r4JZWijTSu8_Ls8MeBJETGFQD-fS4xDETwYoTwWsC51Xcio-aJFKDJwCyw_06G7TEx6RstsAGiEDsSyyKpDv3oUXK2KZxqBMBsTB-UaaBAqZ6bkg4innyzvdVGR-ECxB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=P4jTGY5SDRsiq4ZZ85OY-HDocgGnl2xn6IxcnBgQhLCTF4soLaZSlhtYFQRXGJw3hs5xf9MIzkMppFCmxnu0axaQIt3JJ4wPpcDKWseBamV8JqXw_VxSFWGaPYBNyRfWGdoXhRkefA_ELUK5fWDVAu7ZQXzvqIXjDW3EqiKOIN8S8IZFECCmT2zqMzEx5TzN9jzAQNJXK18CwRFeqt26r4JZWijTSu8_Ls8MeBJETGFQD-fS4xDETwYoTwWsC51Xcio-aJFKDJwCyw_06G7TEx6RstsAGiEDsSyyKpDv3oUXK2KZxqBMBsTB-UaaBAqZ6bkg4innyzvdVGR-ECxB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس سازمان مدیریت بحران کشور: احتمالاً در ۴ ماه پایانی سال کسری انرژی خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/73110" target="_blank">📅 16:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73109">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=bEWblb9hdbsrJocGiSLkIDGUDf4Brps2c-_XDlqOKQ5SZHDGCUN2MMMgaPmrgoBX9sIKyBO_SJJYHPjXZlyh-YceT1O94i4bHht5zYVMDFkECNeVaK7MCkorsbB7ir9T5mOadrQmCihzlwDd8W8_Q5oPXZiA83_vs-5c3oUUu1Fx6sd-mOfZDWdaMVS3aVyIKwCZOawe9EJqNWqxPWdCQGO5T2YvzC6Y93WTHovThU5WWANh4WaOGzqFzV6BVikZgwGbaeg1IcrS6p2HkzxxZ7bPBuRZcwDlB_btVy1UIBToaiSMdjOY0RtOxeO2aa7wEYVxxCTgLExCGnLb8BH1ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=bEWblb9hdbsrJocGiSLkIDGUDf4Brps2c-_XDlqOKQ5SZHDGCUN2MMMgaPmrgoBX9sIKyBO_SJJYHPjXZlyh-YceT1O94i4bHht5zYVMDFkECNeVaK7MCkorsbB7ir9T5mOadrQmCihzlwDd8W8_Q5oPXZiA83_vs-5c3oUUu1Fx6sd-mOfZDWdaMVS3aVyIKwCZOawe9EJqNWqxPWdCQGO5T2YvzC6Y93WTHovThU5WWANh4WaOGzqFzV6BVikZgwGbaeg1IcrS6p2HkzxxZ7bPBuRZcwDlB_btVy1UIBToaiSMdjOY0RtOxeO2aa7wEYVxxCTgLExCGnLb8BH1ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا بچه مچه با خودتون نبرید طلافروشی، یا اگه میبرید با طناب ببندینش به خودتون که همچین منظره‌ای خلق نکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/73109" target="_blank">📅 15:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=NA37AlFpnwBgdY0fr-S8wq7-qOWDSqpx5QvAmLIqiXW3R33bCXPfb1QNcHN_kG05iNPlobCSI8Sm_1SOC97c2riiHj4wNW-X_NJfuNCey7d5rwKig94kzDaQyLxT9y0pIRIe-1lM6Q0u3fH0_IrRgyt4hFbeFgUirlCCiv5cGgzlnRGTc88-Hqa7jo0hWXqIEnYPUoXS1lP5jv90y_enfx1TBCWvjPHV_9OL5ybPHbntgAUS86p46YXXM3erVW5s3yDQgwUBGD-cwQ90aca4dmHURs7iaD_BIPcGFwjJbnMt0_hWZ5obe3HcO-24CqTouMmh81a01Ax-Bs_yWjjSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=NA37AlFpnwBgdY0fr-S8wq7-qOWDSqpx5QvAmLIqiXW3R33bCXPfb1QNcHN_kG05iNPlobCSI8Sm_1SOC97c2riiHj4wNW-X_NJfuNCey7d5rwKig94kzDaQyLxT9y0pIRIe-1lM6Q0u3fH0_IrRgyt4hFbeFgUirlCCiv5cGgzlnRGTc88-Hqa7jo0hWXqIEnYPUoXS1lP5jv90y_enfx1TBCWvjPHV_9OL5ybPHbntgAUS86p46YXXM3erVW5s3yDQgwUBGD-cwQ90aca4dmHURs7iaD_BIPcGFwjJbnMt0_hWZ5obe3HcO-24CqTouMmh81a01Ax-Bs_yWjjSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت گرگان بعد از سیلاب ساعاتی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/73106" target="_blank">📅 15:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=OV8j1LNObGj5Lv-XWra6oqSfhwiQzMW1XHf6S4a0axjzVK7Xkrrd3mOt0a2F6USLyafCqAGhuMZv0QNxOH-fRKK9C48pEomE2yVDORR6uO4kxoTmgNM33rLLul70Rks0SMoCo1lOXPbO-bJooCTvuShPd3U0INs7oMjQOljZmM5sze72fyxC0x0OOEqz5dmtbgaBya4wjmq9kgz9-E_HAypldoXFyT0tyaEy2Zcj6GKQRg5TaLm6I6TDP9lsyvmGKUxVgUWy-3ZN_r4WMjeVU30VIwjVhuZgIBBlCP5vW9F9bTfdAo5gwaKz-sdN-MpHc1n11SH4Vmdfu3wP7paSDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=OV8j1LNObGj5Lv-XWra6oqSfhwiQzMW1XHf6S4a0axjzVK7Xkrrd3mOt0a2F6USLyafCqAGhuMZv0QNxOH-fRKK9C48pEomE2yVDORR6uO4kxoTmgNM33rLLul70Rks0SMoCo1lOXPbO-bJooCTvuShPd3U0INs7oMjQOljZmM5sze72fyxC0x0OOEqz5dmtbgaBya4wjmq9kgz9-E_HAypldoXFyT0tyaEy2Zcj6GKQRg5TaLm6I6TDP9lsyvmGKUxVgUWy-3ZN_r4WMjeVU30VIwjVhuZgIBBlCP5vW9F9bTfdAo5gwaKz-sdN-MpHc1n11SH4Vmdfu3wP7paSDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف:
من به مسئولین گفتم، با برجامی که کونتون رو پاک میکنین، فردا باید دماغ‌تون پاک کنین!
ما کشورهای منطقه رو تهدید می‌بینیم، برای همین سفرای ما در منطقه جا بازرگان و دیپلمات، نماینده سپاه قدس هستن.
ما همه چیزو تهدید می بینیم، زن رو تهدید دیدیم، اینترنت رو تهدید دیدیم، کشورای منطقه رو تهدید دیدیم، ما حتی حجاب هم خاکریز می‌بینیم!
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73105" target="_blank">📅 14:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=bC2D_xWNqdViYPodxB9eeW5obGQhAmd4T95dRtOXW68gIiAYYrrO0ZMHLgN7RqMgxmwy5kHvZtIo_OfERWH66toELEsm_diisCj19Zy2KDZLvR_SovqUsDE-0SQ8xODhNmE3wBlE16jATED-zQeDUZ6iVB3GfEb7ehRNjMSQ2e4Nlh1E9O5vkljDvQhNfZYvAH5l8ScI80rq1wVJqHEy3ExOWif-_UeljbZ5y_cAwVdjwoY2OH_yzgUYiMgMzNA1Y-zqG3pTm7P5pN0KCg6BxRcToKylpbpJ0wEAQPL2lLZ2MKrhsn0ZWrjzZCrSjk4M20QTuGMPqa-8xnPr97ylqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=bC2D_xWNqdViYPodxB9eeW5obGQhAmd4T95dRtOXW68gIiAYYrrO0ZMHLgN7RqMgxmwy5kHvZtIo_OfERWH66toELEsm_diisCj19Zy2KDZLvR_SovqUsDE-0SQ8xODhNmE3wBlE16jATED-zQeDUZ6iVB3GfEb7ehRNjMSQ2e4Nlh1E9O5vkljDvQhNfZYvAH5l8ScI80rq1wVJqHEy3ExOWif-_UeljbZ5y_cAwVdjwoY2OH_yzgUYiMgMzNA1Y-zqG3pTm7P5pN0KCg6BxRcToKylpbpJ0wEAQPL2lLZ2MKrhsn0ZWrjzZCrSjk4M20QTuGMPqa-8xnPr97ylqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری منتشر شده است که لحظه حمله حوثی‌ها به فرودگاه بین‌المللی ملک خالد در ریاض را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/73104" target="_blank">📅 13:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZw75WAcmSClKeP4qE6atOx-p445hWeN8r4x5ElOvEWXprbpRUldKIufCObpJh-s1g8ie-F-htQ_sqybVnNm5S16InXjlzJwn0riv251zKmw6FiMjSS9SerMr4hDfBrL8DWhlROjp6_cOohDv7Nfz_JejPEgl2xkPUD24U3jbBEHznsSa-YEMBtveXUbsEjEfd-juQg3Hj4Ym4nsRoUC1wlxj8OfmyIFaJMhKd6ZPTCm5mpNfh2RsEmiHwmrF2Vui5QK4J2gRCVSLXECl3sOyJHQf9UlyHFG16Po7xVi6XqEHC4oqErVZhFNzSQtkjfBOgSnXTF4Pf0DjKuMpFMs1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی دختر، بر دختران سربلند و آزاده‌ی ایران‌زمین فرخنده باد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73103" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiEkVWCyoJosWNVR_Hc3kqACpKt4yRpxTZ4Q1k5qLD3qguTNP-ySPumIzvwJHVh-1rh-5pyDYVA74pmlJZoowzatVVOSrCNocc0gRvHXRk2za7Z5IXbs0pgeFA3LtT96kOJaKpZb4NJKQRegd77bJXxRWUdrgX_C-QzoNlEJD_A2Efjn33Vh_ZHrsMzr-04B_we7E3lp8Stm1drCHo4xG7JQ_9JJZjjIhV7ByKg4ywBIMDGqyIJLUGJbRcmHXMQ4OCx-lYxzGQclQkOK6JrY3Dcsf3qe9cZQUnVvgIBpkbAKpURuyKuSxEMBHACv5XqMDvz59kPxqXABCMuLlT5ayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست موشکی از جنوب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73102" target="_blank">📅 12:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=s2HJYle5Gj1rMuuckE4cCzf12Lz5vXhiTvYailyUMvKDaBLDFT-g0M43pEnlJ0QMgFDbiwx8MloMthyxJC6CF56SzTvU3VJ9e07QC4qRVJp62bQ5tDLzdVz2eSH0cVOE-NDIeknXaQ1cme4uURUoHXexIHALXcSGj1uMcMipy90-7jJGRUaZ429bCfAtu7ItpkT7nJM7_1xSJzjqO4L5EIWEMnMwXsMqhydpLPO2YSeMcSdc2GiNAoHw1h3jJ7H-aM2ZWqVinHvHrbwfRhE9OK0olU_1zha8K3a1EnQo7Sk9zraciPx-C53nzPby1EPPIwBv2YwRw_JaRmX4qT-4Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=s2HJYle5Gj1rMuuckE4cCzf12Lz5vXhiTvYailyUMvKDaBLDFT-g0M43pEnlJ0QMgFDbiwx8MloMthyxJC6CF56SzTvU3VJ9e07QC4qRVJp62bQ5tDLzdVz2eSH0cVOE-NDIeknXaQ1cme4uURUoHXexIHALXcSGj1uMcMipy90-7jJGRUaZ429bCfAtu7ItpkT7nJM7_1xSJzjqO4L5EIWEMnMwXsMqhydpLPO2YSeMcSdc2GiNAoHw1h3jJ7H-aM2ZWqVinHvHrbwfRhE9OK0olU_1zha8K3a1EnQo7Sk9zraciPx-C53nzPby1EPPIwBv2YwRw_JaRmX4qT-4Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: یک کشتی باری در دریای عمان هدف حمله آمریکا قرار گرفت
فرماندهی مرکزی آمریکا (سنتکام) اعلام کرد در ۱۰ اکتبر، یک کشتی باری با پرچم پاناما به نام Ocean Molica که پیش‌تر از یکی از بنادر ایران حرکت کرده بود، پس از بی‌توجهی به هشدارهای مکرر و تلاش برای عبور از محاصره دریایی، هدف مهمات دقیق یک جنگنده آمریکایی قرار گرفت.
به گفته سنتکام، این حمله پیشرانه کشتی را از کار انداخت و خدمه آسیبی ندیدند. همچنین، طی سه ماه اجرای محاصره دریایی، ۴ کشتی از کار انداخته و ۱۳۵ کشتی دیگر وادار به تغییر مسیر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73101" target="_blank">📅 12:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73099">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=Ycqf_8e-sDDsL9ZcS4FaCd-wpATp447wf9coVhIqBESgT8iwPCijo7au2RDs8wLrFZQRC5ooF0L-EwPnjARORmCR9xLuJO8DCS1h7G0EGjIrW6pB7iUzY4Y7q2D4i_J2BDTWxZbNEsXmlPPl1LV19JoI3aCeNrawsuCRttuMWEjlG4F7pX682nA5ZogzaPV3ZmA-IQFW4uaBsjzVZkc7rMM4qFp_9QjGNeWjfx5ehrKRdwplqWgvdtsjUkcluwB0ydzxkWTovrU5aOpUVPmNQgFc1vgnqsE9cIBTItp9M3iMLFO8HKDvIEMX0saOYnrzkuljnLyQyh-JgmlM8Uc77Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=Ycqf_8e-sDDsL9ZcS4FaCd-wpATp447wf9coVhIqBESgT8iwPCijo7au2RDs8wLrFZQRC5ooF0L-EwPnjARORmCR9xLuJO8DCS1h7G0EGjIrW6pB7iUzY4Y7q2D4i_J2BDTWxZbNEsXmlPPl1LV19JoI3aCeNrawsuCRttuMWEjlG4F7pX682nA5ZogzaPV3ZmA-IQFW4uaBsjzVZkc7rMM4qFp_9QjGNeWjfx5ehrKRdwplqWgvdtsjUkcluwB0ydzxkWTovrU5aOpUVPmNQgFc1vgnqsE9cIBTItp9M3iMLFO8HKDvIEMX0saOYnrzkuljnLyQyh-JgmlM8Uc77Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی رفتن ویدیوی رپ هوش‌مصنوعیِ بی‌بی رو نشون خودش دادن، اونم به شوخی میگه از کجا میدونید شاید واقعی باشه:)
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73099" target="_blank">📅 11:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73098">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مقام‌های سعودی اعلام کردند در حمله روز شنبه به فرودگاه ملک خالد ریاض، ۱۲ نفر کشته و ۳۰۹ نفر زخمی شدند.
ملیت کشته‌شدگان:
عربستان سعودی: ۴ نفر
بنگلادش: ۲ نفر
آمریکا: ۱ نفر
مصر: ۱ نفر
اردن: ۱ نفر
سوریه: ۱ نفر
فلسطین: ۱ نفر
سودان: ۱ نفر
برخی مجروحان در وضعیت وخیم قرار دارند و حمله خساراتی به تأسیسات فرودگاه وارد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73098" target="_blank">📅 11:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73097">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=bgSQXKir0xGI2uv6f8C5eD7vaSgl5EvlMls6jByzyuyV9S7noy1u2UnqMI9cHaVljRXvLbfjze9966bmHzAh8z25yjPS2rtaMyIHOUwA45Na4Lo1NgMZFZiqww7XRASNEw7pPX5AVt-S1zBev7MEcBQQmVL3l1jvrkn3fBvO9C4vWVLoKvS1uwmXdOEiRuQAY2lklQIzIgj3dEqxYtzLO7ZxLVJA0EVzx6LYfiDlRVjIBtxvc9YMN5oYFZx8v61B6yjUW-3iqxBYyTR3hN6VcJGRj0-_BX8db6FvFPaMlFB0OcYwY_LU8XygWI5Otv6P2-_IWbg8mkleFx5f-ouJdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=bgSQXKir0xGI2uv6f8C5eD7vaSgl5EvlMls6jByzyuyV9S7noy1u2UnqMI9cHaVljRXvLbfjze9966bmHzAh8z25yjPS2rtaMyIHOUwA45Na4Lo1NgMZFZiqww7XRASNEw7pPX5AVt-S1zBev7MEcBQQmVL3l1jvrkn3fBvO9C4vWVLoKvS1uwmXdOEiRuQAY2lklQIzIgj3dEqxYtzLO7ZxLVJA0EVzx6LYfiDlRVjIBtxvc9YMN5oYFZx8v61B6yjUW-3iqxBYyTR3hN6VcJGRj0-_BX8db6FvFPaMlFB0OcYwY_LU8XygWI5Otv6P2-_IWbg8mkleFx5f-ouJdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: نظرتون درباره حمله حوثی‌ها به فرودگاه ریاض چیه؟
ترامپ: «به نظرم اتفاق وحشتناکیه.»
خبرنگار: آیا آمریکا هم وارد ماجرا می‌شه؟
ترامپ: «خب، خودتون متوجه خواهید شد. اما به نظرم اتفاق وحشتناکیه.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73097" target="_blank">📅 10:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73096">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ درباره یمن:
«ما با حوثی‌ها در ارتباط هستیم و باید ببینیم چه اتفاقی می‌افته.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/73096" target="_blank">📅 10:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73095">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174ee9d3ac.mp4?token=qTwCgJdaLIq91MK_PVhj3bVSN9gOsFZYO5vbC_rmnlDGPeK6u5WKS_K0z9mIr6gbC1rSblz_0j2zNrFqaTnLHiO6YU8UETnwGiPi0EYKr0kNhIn6pR0aB_RQQCTrpD1Zf-MIgEvfV_fNuQvI6Sb65UfyLjGR9L8XC8vx0rYemvHBdL9-bAkYNr5q8PvrgDPjziNZ9UiDv9f9aMbXItKflgUBCy8FOIny_Lq_aBf5ec4kZgxeKSoGNacU8pnuz6cZcFAMTtW2OGhftEo0tgJZlTjfMr7wuQW98Bqbtnj9VIe94aMmXGNcFmUle6XU6IEdMXyELTWB3ozG6Snu7yuBwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174ee9d3ac.mp4?token=qTwCgJdaLIq91MK_PVhj3bVSN9gOsFZYO5vbC_rmnlDGPeK6u5WKS_K0z9mIr6gbC1rSblz_0j2zNrFqaTnLHiO6YU8UETnwGiPi0EYKr0kNhIn6pR0aB_RQQCTrpD1Zf-MIgEvfV_fNuQvI6Sb65UfyLjGR9L8XC8vx0rYemvHBdL9-bAkYNr5q8PvrgDPjziNZ9UiDv9f9aMbXItKflgUBCy8FOIny_Lq_aBf5ec4kZgxeKSoGNacU8pnuz6cZcFAMTtW2OGhftEo0tgJZlTjfMr7wuQW98Bqbtnj9VIe94aMmXGNcFmUle6XU6IEdMXyELTWB3ozG6Snu7yuBwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا سعودی‌ها بدون حضور نیروهای آمریکایی هم می‌تونن از خودشون دفاع کنن؟
ترامپ: «بله، توانایی دفاع از خودشون رو دارن. سعودی‌ها جنگجوهای خوبی هستن، اما به نظرم اون حمله اتفاق وحشتناکی بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/73095" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73094">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73094" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/73094" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73093">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElvFrXraSVC9BUdDias5ZQVsdAoipYsj3t06i0789cLBKB1fkj94SXnQLcp1HIDNyB35qgBAPKZJbKI4cxJXLMhKC_KrLd4uw2KvbvxwJXTk7e9XEecxBKI3B7lbeDIU7ZgpA4RS1Jki7wX58YDuB8TroacnkEOtBPU4vT93Ay_SDiilro-HAGP9D8PY6vPWwigcEKC7Xe29TI8AS8WCxtrtCpRHelDmxhQHM21UwF0h5H3soKcDTXY9plgNGzsIuiBDN8IlnhX1cAuAgRrcc02Xl7LC-MCwp9Hp49ufPjwuFeP0j-kJtivgqRaN4upT3mlMP788e2AjZtqpPa2A6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ناتینگهام‌فارست
🆚
کریستال‌پالاس
اورتون
🆚
هال
منچسترسیتی
🆚
لیورپول
اوساسونا
🆚
راسینگ سانتاندر
رم
🆚
کومو
مونزا
🆚
لاتزیو
میلان
🆚
ساسولو
فروزینونه
🆚
ناپولی
یوونتوس
🆚
کالیاری
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73093" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73092">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e6800693.mp4?token=I8iX10e8kzLatZxdsZayyAQZWcD37B4YiU9Y-jOQdC6W1eMECUY_Jsgj7b3NvMhGNYqWQ2kbUHF9gsQZIR6WtdOcqv-rSVOE7DhAE2YvKW_xuAGh97Wp-JSb4at--oSdCdRltPbiGA3o08O99ZO6C5qKwF8JcyV-i0aZk2JC6J0dUfWdflNr-xbrOsiGPzazN9sfFmS1vwc2y6UIkpWSzkGxmIVzvrXJ9osUj-OEY9FmvZrsdW1wPFqtYdmgkiJvp80PK2hgyAgPbh5qo3ezImBkAD5u4Beyq1Hs3rK8ItFhhp_m1pReOR55N6PI2F_M9sDLQrr_5vsYQACkRYM0vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e6800693.mp4?token=I8iX10e8kzLatZxdsZayyAQZWcD37B4YiU9Y-jOQdC6W1eMECUY_Jsgj7b3NvMhGNYqWQ2kbUHF9gsQZIR6WtdOcqv-rSVOE7DhAE2YvKW_xuAGh97Wp-JSb4at--oSdCdRltPbiGA3o08O99ZO6C5qKwF8JcyV-i0aZk2JC6J0dUfWdflNr-xbrOsiGPzazN9sfFmS1vwc2y6UIkpWSzkGxmIVzvrXJ9osUj-OEY9FmvZrsdW1wPFqtYdmgkiJvp80PK2hgyAgPbh5qo3ezImBkAD5u4Beyq1Hs3rK8ItFhhp_m1pReOR55N6PI2F_M9sDLQrr_5vsYQACkRYM0vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام جمعه تهران:
توقع مردم، تجدید نظر در دکترین هسته‌ای ایران است
از ان پی تی خارج شویم به غرب می‌گویم هسته‌ای ما به شما ربطی ندارد؛
غلط کردین؛ برید گم شید!
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73092" target="_blank">📅 10:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73091">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6a5528a8.mp4?token=QT7D2CrghyiOD-Yorbn6vNctAr425kMEyw6y8d2JOBWxoIaeJSPVm4Wa8jZtV27gJlGbPJ3lPKVNDdneywtSvN7wWYt1rwkfTJAzq_OYyAcwXFR-c2oIqALju1KMnsgT_lgCzrjRbxh7MKaJq8niXvjy1S-R7wFgg_tPcmxXD7Gehz5lhmha8jQctOoh6CDcCLDn8XPbXL0cV1REO_yyCM1dULedeSIZ4_CNa4wKPcRd7vGqNzx_Zqt0wr43KcVIS342wBmkKPqEK10L5QOX4B6bynMQoUqboq8sSF8TrY348QaF5lszg_SocfLepjhVZ4yU97AhDiDVoMMANZJ0baXgIcMJnfyEXq4H0IpCXbaE7rIgwqyfLpxAWs9bRm16MZxMyz2TNd6Mjy7n-0ziS_Wyr7Vb2DyiKhSKqGCkXjmi1hYn69Gp49iYTDdtOuL4Oa2nUrbmMLrB6pqS4XHp0PZH7qFRwUxEYo06LeDsb2QtM1JeYu-UqccQEbCgtzxLH7iMd4h3VDr6lOXGqr1MBUv90G6Z3s9DXp4e_lCnfOJa5jy60uL7avkdy49kXI83WJ6naL_PhNwBASUX42kveg6tQSw2w80s5IYiEL1m0x890dTo4oFNBZMabowd-Pyfx8p3H-HACHw8wPitIeeduMjDTh3-9nyVMRBrgplFwJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6a5528a8.mp4?token=QT7D2CrghyiOD-Yorbn6vNctAr425kMEyw6y8d2JOBWxoIaeJSPVm4Wa8jZtV27gJlGbPJ3lPKVNDdneywtSvN7wWYt1rwkfTJAzq_OYyAcwXFR-c2oIqALju1KMnsgT_lgCzrjRbxh7MKaJq8niXvjy1S-R7wFgg_tPcmxXD7Gehz5lhmha8jQctOoh6CDcCLDn8XPbXL0cV1REO_yyCM1dULedeSIZ4_CNa4wKPcRd7vGqNzx_Zqt0wr43KcVIS342wBmkKPqEK10L5QOX4B6bynMQoUqboq8sSF8TrY348QaF5lszg_SocfLepjhVZ4yU97AhDiDVoMMANZJ0baXgIcMJnfyEXq4H0IpCXbaE7rIgwqyfLpxAWs9bRm16MZxMyz2TNd6Mjy7n-0ziS_Wyr7Vb2DyiKhSKqGCkXjmi1hYn69Gp49iYTDdtOuL4Oa2nUrbmMLrB6pqS4XHp0PZH7qFRwUxEYo06LeDsb2QtM1JeYu-UqccQEbCgtzxLH7iMd4h3VDr6lOXGqr1MBUv90G6Z3s9DXp4e_lCnfOJa5jy60uL7avkdy49kXI83WJ6naL_PhNwBASUX42kveg6tQSw2w80s5IYiEL1m0x890dTo4oFNBZMabowd-Pyfx8p3H-HACHw8wPitIeeduMjDTh3-9nyVMRBrgplFwJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه بریتانیایی ITN حدود ۴ ساعت از تصاویر وقایع سال ۱۹۸۹ میدان تیان‌آن‌من را منتشر کرده است؛ تصاویری که پیش‌تر محرمانه نگه داشته شده بودند و توسط تیمی ضبط شدند که موفق شد این نوارها را مخفیانه از چین خارج کند.
این مجموعه که حدود ۳۵ سال در آرشیو نگهداری می‌شد، شامل یک ویدئوی تدوین‌شده‌ی ۲ ساعته از سرکوب‌ها و همچنین ۹۰ دقیقه تصاویر خام و مخفیانه‌ای است که در روزهای پس از آن واقعه ضبط شده‌اند؛
تصاویری که کامیون‌های نظامی در خیابان‌های پکن، جمعیت مردم و پیامدهای آن رویداد را به نمایش می‌گذارند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/73091" target="_blank">📅 09:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73090">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e31f09431.mp4?token=jgTnWal85urUbEP-gh_NLCDV9-x1KxnTnfeTeAUCS6r2SSzUqEZQ9_nhz886hCLzaKljSvBMCjiHUfoTC3dtbly_x-jOQZnWyre8mse0WHN7-UItLCeaM8UOElUqWKwACk_N48YeBovi-yIGeZdUPDqN5lFd-4E_5AiFwYYWwORxxnAelBocgXSV47EkL90MZCMLE9K2tIXXlNLTOhgmWMdQ5fC2v2fck8BTjoRfACOyFfAzqr1SAxPb5C6iVmZ1JkXOe2nb2vufRwV-_eUR5BNb8WcrZr6VceLawZPL-t1HA2Y3TZ85lIn0mv5k0NDCD8YGDAG73eKT_13j9lB8pYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e31f09431.mp4?token=jgTnWal85urUbEP-gh_NLCDV9-x1KxnTnfeTeAUCS6r2SSzUqEZQ9_nhz886hCLzaKljSvBMCjiHUfoTC3dtbly_x-jOQZnWyre8mse0WHN7-UItLCeaM8UOElUqWKwACk_N48YeBovi-yIGeZdUPDqN5lFd-4E_5AiFwYYWwORxxnAelBocgXSV47EkL90MZCMLE9K2tIXXlNLTOhgmWMdQ5fC2v2fck8BTjoRfACOyFfAzqr1SAxPb5C6iVmZ1JkXOe2nb2vufRwV-_eUR5BNb8WcrZr6VceLawZPL-t1HA2Y3TZ85lIn0mv5k0NDCD8YGDAG73eKT_13j9lB8pYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
فلسفه بازنشستگی در یک کشور اسلامی هیچ مفهومی ندارد و مسلمان واقعی باید تا آنجا که می‌تواند خدمت کند
حیف است که افراد ۸۰ و ۹۰ ساله را از خدمت کنار بگذاریم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73090" target="_blank">📅 09:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73089">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73089" target="_blank">📅 01:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73088">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73088" target="_blank">📅 01:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73087">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1848b3d2ec.mp4?token=cSaG1mt7D2LkJMECEGuVR8okIFE48UOgvmfP4vCDyq_1niU6r5eLCeWgDgp3DKa6HymZ4TZ7lFc9GtM8W6Li8Xkux_fpkkMH_OnyRnqlAjrlEq8xi77tsKO9EK4cn679NgzajXWXo-0AZnChUErV_ls1c0ww3zm4skL0xNNdHzUZ2m8N1DJ4ZUVY5EpxslUPC9s69lt3wpwrjYQxJXo2HZ2xyayR6cgXhNjqIImM2vEs77WPR0-ezw-q1-qzYrrdduVYMH1mJ3pMZY4d51f25xxFo6OnNqmRyeRTxJXWibTxmVuO4imp96MDHwggNXgxCss3jTuX9bWfvL9tKMyVwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1848b3d2ec.mp4?token=cSaG1mt7D2LkJMECEGuVR8okIFE48UOgvmfP4vCDyq_1niU6r5eLCeWgDgp3DKa6HymZ4TZ7lFc9GtM8W6Li8Xkux_fpkkMH_OnyRnqlAjrlEq8xi77tsKO9EK4cn679NgzajXWXo-0AZnChUErV_ls1c0ww3zm4skL0xNNdHzUZ2m8N1DJ4ZUVY5EpxslUPC9s69lt3wpwrjYQxJXo2HZ2xyayR6cgXhNjqIImM2vEs77WPR0-ezw-q1-qzYrrdduVYMH1mJ3pMZY4d51f25xxFo6OnNqmRyeRTxJXWibTxmVuO4imp96MDHwggNXgxCss3jTuX9bWfvL9tKMyVwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«ایران کشور بسیار شروریه؛ بزرگ‌ترین حامی تروریسم در جهانه.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/73087" target="_blank">📅 01:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73086">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a4893ab6.mp4?token=beJT60_w78FiByRl91YcuCxDEHg3cpPGqwVFLDhyQY9Y2I5tGBhYnsm0SWfej0Q29WnccCc_9FtFUScxIKFHuHg8XjQO3WGWa9Jp78sX7ThlLWZrxiCCyP_50zWen-Cv-rA57SLqK1myHxIkj4cnEbQuslK55OH6bbUM_GuGth71FHILtnOGvVfEE-BDUomK2uj1FRImJygsHKsQwENoh-ozqXLExY3W1wFq4IgSuPWOUY6BfsSFNEFGY-G8sxHvNB2CQj844hEnHNc_yYtAFJ2CERYtmLs19bDWAYM-hyVbdNJAIkhB4VfyyLUYuK9IZqKyqSOwdP_N-ZmUxhcJRoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a4893ab6.mp4?token=beJT60_w78FiByRl91YcuCxDEHg3cpPGqwVFLDhyQY9Y2I5tGBhYnsm0SWfej0Q29WnccCc_9FtFUScxIKFHuHg8XjQO3WGWa9Jp78sX7ThlLWZrxiCCyP_50zWen-Cv-rA57SLqK1myHxIkj4cnEbQuslK55OH6bbUM_GuGth71FHILtnOGvVfEE-BDUomK2uj1FRImJygsHKsQwENoh-ozqXLExY3W1wFq4IgSuPWOUY6BfsSFNEFGY-G8sxHvNB2CQj844hEnHNc_yYtAFJ2CERYtmLs19bDWAYM-hyVbdNJAIkhB4VfyyLUYuK9IZqKyqSOwdP_N-ZmUxhcJRoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«اون جوان‌هایی که در جنگ علیه ایران از دست دادیم، بیهوده جونشون رو از دست ندادن.
نمی‌شه اجازه داد یه آدم کاملاً دیوونه به سلاح هسته‌ای دست پیدا کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73086" target="_blank">📅 01:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73084">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=W4dujg4Gs9ixB4HoXTudrgUbr37nWAFkOL2nHWpR6XWxffmNdzJt6T8hdReIzMVIRKKNsCoYevIVC3XIaWP_wns0G4RcvfMEN6Ka1loHuzXDpkBuP9alGfGA1_tD_N0u0xNXXdKCJktE0jw2OSEShkOPNr0H_m-kUDAl1JxV_HCgBzItGOUH9xwa3Y8TMwsk5g4PdG06VIyN8_BCuKmXKBqWEAHRe4ZRRz4QBk5ZiLSxQSHUG6y7NnyDvnj7WhYQ56i8axd8p2D1xZMDkAFUKeDBGmrUCKgEfoW7B3gJ37VvjOyxVSbxRyy_F4zUigO6D4oMQIAPgyAJsZ1LIgb8NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=W4dujg4Gs9ixB4HoXTudrgUbr37nWAFkOL2nHWpR6XWxffmNdzJt6T8hdReIzMVIRKKNsCoYevIVC3XIaWP_wns0G4RcvfMEN6Ka1loHuzXDpkBuP9alGfGA1_tD_N0u0xNXXdKCJktE0jw2OSEShkOPNr0H_m-kUDAl1JxV_HCgBzItGOUH9xwa3Y8TMwsk5g4PdG06VIyN8_BCuKmXKBqWEAHRe4ZRRz4QBk5ZiLSxQSHUG6y7NnyDvnj7WhYQ56i8axd8p2D1xZMDkAFUKeDBGmrUCKgEfoW7B3gJ37VvjOyxVSbxRyy_F4zUigO6D4oMQIAPgyAJsZ1LIgb8NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی املاکی
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73084" target="_blank">📅 00:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73083">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b6424edb4.mp4?token=tjELenruT6T5qXInB_t_EpFK_91Ohv7Yoq-L7htrn8tfHSbDrYEZA4dVGlp2f6B5wanJwZAS-hPPpNynMdo_NuxBRp3qVP7sUcuiWRUBc9AFsEFbLHorENCLnIpTtAzS7JSG9r4PkhGibcRoEMOx4wWpVuJfu7nqKrFXLhyihTfabhcmb4LF7NRj97VY-QIpt6aYd6vJo1b8zQ5uMaZF2su9SIeOb14vB0S4R8b8dTi5H18hrDQewsrrcIAWKEbAAI045A1hp5_-4iaE73WKbW8zOaXx6PjJcfANKWlg5Lb9deyzl5n2nr4xyZJiphOtVlKMdpIYoOy4au8QwzpmmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b6424edb4.mp4?token=tjELenruT6T5qXInB_t_EpFK_91Ohv7Yoq-L7htrn8tfHSbDrYEZA4dVGlp2f6B5wanJwZAS-hPPpNynMdo_NuxBRp3qVP7sUcuiWRUBc9AFsEFbLHorENCLnIpTtAzS7JSG9r4PkhGibcRoEMOx4wWpVuJfu7nqKrFXLhyihTfabhcmb4LF7NRj97VY-QIpt6aYd6vJo1b8zQ5uMaZF2su9SIeOb14vB0S4R8b8dTi5H18hrDQewsrrcIAWKEbAAI045A1hp5_-4iaE73WKbW8zOaXx6PjJcfANKWlg5Lb9deyzl5n2nr4xyZJiphOtVlKMdpIYoOy4au8QwzpmmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی یکی از اعضا از گرگان:
بارندگی شدید امشب در گرگان باعث وقوع سیل و وارد شدن خسارت به اموال مردم شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73083" target="_blank">📅 00:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73082">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=TvwKgH5D9JEyjSm8JF99PG4s1B5GSeORZvtFVL64nAHXxwS7UNHjZ2Rmab9ik6TBO9qIr29hbZlLqAGE6KXUXt3eVChztXXcLqldDsOGgeO017ZUt5RcNEI8xaozGkDRr2Ydwy6OCwrB_IKCWHleiKPtigfNHGLbBAtKv6Ejgzmuw0h6Ay50ytcWmRfj0BwwnvPj4ahXDyB0Vvaf-lOzKDah_ubvR35N3gGeDNJdp6VtwxR46FQECMligxZvKwkpsAa5L3eZAVjchHxn6DiVMqKc2veQHsKMfuHlXWt-n_zUdYW5bgPQTlFf6wQ_9fg9VIcOxYzWC9iXsvv2OyV6Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=TvwKgH5D9JEyjSm8JF99PG4s1B5GSeORZvtFVL64nAHXxwS7UNHjZ2Rmab9ik6TBO9qIr29hbZlLqAGE6KXUXt3eVChztXXcLqldDsOGgeO017ZUt5RcNEI8xaozGkDRr2Ydwy6OCwrB_IKCWHleiKPtigfNHGLbBAtKv6Ejgzmuw0h6Ay50ytcWmRfj0BwwnvPj4ahXDyB0Vvaf-lOzKDah_ubvR35N3gGeDNJdp6VtwxR46FQECMligxZvKwkpsAa5L3eZAVjchHxn6DiVMqKc2veQHsKMfuHlXWt-n_zUdYW5bgPQTlFf6wQ_9fg9VIcOxYzWC9iXsvv2OyV6Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">املاکی درباره تنگه هرمز:
«داریم به این فکر می‌کنیم که اسم تنگه هرمز رو به تنگه ترامپ تغییر بدیم!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73082" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73081">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=Sahwy6NaSzDuNjXImiUfPLYXAO1jDEvlpH7PKuPqY-PETEz0-u1tErTg1XRkTsTN_GC1oiTASjmXRKVCqRomgCsDXtiLaWSOfPT0WJXK_NalXbAFKR_AULtZVmA7_T6gY_QQ6O_A_gKJQ3VVaxMcd8XV_AO1fcNZqF3X4mqf3BAi1h_E6hcKKfspqmc1Vg6n0dI43qRiIBa4emiQM4S_BCNtkX09xNR36S-_udhpkI49Jgh4PSj3OvbiTgCMb8uy1e6JjXaYi77yKSVHQaqVu3e5g98tOPTxL7vzltetrs6NsXMVd95ZQjJzv55AoJRF0KdvOzuuliDDfWy_1Ny1_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=Sahwy6NaSzDuNjXImiUfPLYXAO1jDEvlpH7PKuPqY-PETEz0-u1tErTg1XRkTsTN_GC1oiTASjmXRKVCqRomgCsDXtiLaWSOfPT0WJXK_NalXbAFKR_AULtZVmA7_T6gY_QQ6O_A_gKJQ3VVaxMcd8XV_AO1fcNZqF3X4mqf3BAi1h_E6hcKKfspqmc1Vg6n0dI43qRiIBa4emiQM4S_BCNtkX09xNR36S-_udhpkI49Jgh4PSj3OvbiTgCMb8uy1e6JjXaYi77yKSVHQaqVu3e5g98tOPTxL7vzltetrs6NsXMVd95ZQjJzv55AoJRF0KdvOzuuliDDfWy_1Ny1_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌تونیم خیلی سریع به این ماجرا پایان بدیم. ایرانی‌ها نمی‌دونن که من تا حالا چقدر باهاشون مدارا کردم و چقدر باهاشون راه اومدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73081" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73080">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_0Frv86MqgzMYc1q4MbDcIGjwLhUby0EIvD8JJ0bkHGTxtI34RxizfU6HiZAXwLBFIzC3K2XDUATDmAUTTXnYbAAKNJKX4TcYMuJEEEGdKGFbzaQn58mDE-C3K8wO5qZsIYcD0QvXhmohpYcXkqjagwcUBvP1UNKIfK_wNF5nTOnRnmfNbli1egfxX4VpkEQjHChSL7PXzsqFS0Y50ybFtLMpJle9xbK1e2gPLA5aGeBltKbV7wnszIb8Un0Ygru_WHJF1JiWTyVEpcoQR6IaTsLVYRq2H_1JLllhtBOnCyOTwFT0wU5jJtfYMDguBUl-IoKOSbBqsbFpFEDChL42tM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_0Frv86MqgzMYc1q4MbDcIGjwLhUby0EIvD8JJ0bkHGTxtI34RxizfU6HiZAXwLBFIzC3K2XDUATDmAUTTXnYbAAKNJKX4TcYMuJEEEGdKGFbzaQn58mDE-C3K8wO5qZsIYcD0QvXhmohpYcXkqjagwcUBvP1UNKIfK_wNF5nTOnRnmfNbli1egfxX4VpkEQjHChSL7PXzsqFS0Y50ybFtLMpJle9xbK1e2gPLA5aGeBltKbV7wnszIb8Un0Ygru_WHJF1JiWTyVEpcoQR6IaTsLVYRq2H_1JLllhtBOnCyOTwFT0wU5jJtfYMDguBUl-IoKOSbBqsbFpFEDChL42tM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ایرانی‌ها می‌گن: همه رو می‌کشیمممم! همه روووو!
همچنین می‌گن: الحمدلله! الحمدلله! الحمدلله!
منم بهشون می‌گم: بابا، شماها واقعاً دیوونه‌اید!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73080" target="_blank">📅 00:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73079">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=j3K3kkovoIA0IkPL3C08CFndQFb8rLS772vLbD4RgGlEk3FwwUfa8UqDSe1m1mMEZqqdP_2HPubFPrXeJq5wEynnjfL6uMOTIpXGlnxTLkKkyzBPxsoYwABgbKVY_Uq9mlOWy1RrRsCDepeKv80gMP0XP-OroFSP1vMHLhO_xTn2163buPqdB_gXodUk4tgPmQvE92cwaHn3gBJJM_nSvBl4Xn24R9vFKb7QL86Ls0S2Vnxt1ttLIO0VNafNC75p_aNoHTka0V9MHu6smzflJi5aImMgQPks51XIERjRIzRdU3hf5ykD5UScT4aoiGesu3IZqk9JfEVPVt4RA7UURg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=j3K3kkovoIA0IkPL3C08CFndQFb8rLS772vLbD4RgGlEk3FwwUfa8UqDSe1m1mMEZqqdP_2HPubFPrXeJq5wEynnjfL6uMOTIpXGlnxTLkKkyzBPxsoYwABgbKVY_Uq9mlOWy1RrRsCDepeKv80gMP0XP-OroFSP1vMHLhO_xTn2163buPqdB_gXodUk4tgPmQvE92cwaHn3gBJJM_nSvBl4Xn24R9vFKb7QL86Ls0S2Vnxt1ttLIO0VNafNC75p_aNoHTka0V9MHu6smzflJi5aImMgQPks51XIERjRIzRdU3hf5ykD5UScT4aoiGesu3IZqk9JfEVPVt4RA7UURg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور گلشیفته فراهانی در فیلم Matchbox: The Movie 2026 و صحنه لب گرفتن او با جان‌سینا!
+ نکته جالب اینکه همسر جان‌سینا هم ایرانیه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73079" target="_blank">📅 23:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=tzaIPSN2clzfm_iBDMZ-6RLiiouIJl2hhxoEQjBTFDqd7cJB7Ropt0OHgZLpzWYH-7GsAb7W94tMG7dO70S7GMHCBTkBXgFzZcTp7BE84RyUMXlNv7NXmKUQVxyx6Y3DlmVdGJmLZTZ3khpDOwxKhU-t5sZyaHQVicDBKY-lJc5awo4NYWBPUzHxGgHbjyzGRrhLa6jmUN0W9iT6aevsxzTQs-fJxsICN2aOm-7S0vpVoTTtb3aInOHvAK4kjfopHG6NnUoQ_mYdJugEzyv2R5cm_Zd2ei7s22LAzY7mWWVcdKbBIuia0VhSYYGPYna4YKBEtAQO34dRvs1eTVZ2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=tzaIPSN2clzfm_iBDMZ-6RLiiouIJl2hhxoEQjBTFDqd7cJB7Ropt0OHgZLpzWYH-7GsAb7W94tMG7dO70S7GMHCBTkBXgFzZcTp7BE84RyUMXlNv7NXmKUQVxyx6Y3DlmVdGJmLZTZ3khpDOwxKhU-t5sZyaHQVicDBKY-lJc5awo4NYWBPUzHxGgHbjyzGRrhLa6jmUN0W9iT6aevsxzTQs-fJxsICN2aOm-7S0vpVoTTtb3aInOHvAK4kjfopHG6NnUoQ_mYdJugEzyv2R5cm_Zd2ei7s22LAzY7mWWVcdKbBIuia0VhSYYGPYna4YKBEtAQO34dRvs1eTVZ2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پلنگ حکومتی :هر روز صبح و شب اینجام که بگم ما فقط جنگ میخوایم  و مذاکره نمی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73078" target="_blank">📅 23:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73074">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a72e1a5c.mp4?token=ZyLoRGrOwGS7jLmGG8YNqE4ZFlGALT5LwJTL-mqS_MTinf4wtRG3sET75Isf__NbsmEZKb25sx2Polnyu0HW4o8AZyqdErLzvVqKX4P2pHH1ju6M7BkQoogt4MVTLkLVrSv7Nj-YGMKFvnHHsLO3ubQp9c9C-Yw4QTeO0K_qdefVy0FsmY3P6ssKxHNyp5wgfShPZqtF3CFaU_cuYhSkzADuzcRv96CyvclMLFKRznhas8EoEncUy8I2dozjf3QXxXoFyX5yAYPI50rNYZWXXCRj7kkCQrjGpnVmVH_pigNsD3gI-DYf0gybJrpZ5H8KBShgB6sPWv_3GR4xuZZzVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a72e1a5c.mp4?token=ZyLoRGrOwGS7jLmGG8YNqE4ZFlGALT5LwJTL-mqS_MTinf4wtRG3sET75Isf__NbsmEZKb25sx2Polnyu0HW4o8AZyqdErLzvVqKX4P2pHH1ju6M7BkQoogt4MVTLkLVrSv7Nj-YGMKFvnHHsLO3ubQp9c9C-Yw4QTeO0K_qdefVy0FsmY3P6ssKxHNyp5wgfShPZqtF3CFaU_cuYhSkzADuzcRv96CyvclMLFKRznhas8EoEncUy8I2dozjf3QXxXoFyX5yAYPI50rNYZWXXCRj7kkCQrjGpnVmVH_pigNsD3gI-DYf0gybJrpZ5H8KBShgB6sPWv_3GR4xuZZzVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هوایی اسرائیل به ساختمانی چندطبقه در غزه
دقایقی پیش، جنگنده‌های اسرائیلی یک ساختمان چندطبقه در شهر غزه رو هدف قرار دادن. پیش از حمله، دستور تخلیه ساختمان صادر شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73074" target="_blank">📅 22:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73073">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6e7ebfe2.mp4?token=jmMQ36zhKwj36F4FQeN1TfxUO5k6uWCmeI3K9BK-T6gdegashTjU1Upt50BI0SA2V51dx_o0hXbjY3WZ5W9JeGnBHSdLcQbbYgW1pwK8HE9qcXndtasEqmpMrgNC8qzpugUBaEr4_v96JPIrJptX4VeN3QFcBDbt6eJPJs7ASr_ntJAVqy-UKcWEPzxxAYNyxfnV35FQk0cr1V5enyPuyQVgqIiHqa_mGtOoHvEMNMwp-0kr30ER6KCwFTPERdj2CYJbzeZ9H4itjUvQczx1PvEn7icOKg-5Z8tbzpDrqZIBya2p9qxjKKJKoGcy0ojy7K8VD0Z2QQvp0wFagSitSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6e7ebfe2.mp4?token=jmMQ36zhKwj36F4FQeN1TfxUO5k6uWCmeI3K9BK-T6gdegashTjU1Upt50BI0SA2V51dx_o0hXbjY3WZ5W9JeGnBHSdLcQbbYgW1pwK8HE9qcXndtasEqmpMrgNC8qzpugUBaEr4_v96JPIrJptX4VeN3QFcBDbt6eJPJs7ASr_ntJAVqy-UKcWEPzxxAYNyxfnV35FQk0cr1V5enyPuyQVgqIiHqa_mGtOoHvEMNMwp-0kr30ER6KCwFTPERdj2CYJbzeZ9H4itjUvQczx1PvEn7icOKg-5Z8tbzpDrqZIBya2p9qxjKKJKoGcy0ojy7K8VD0Z2QQvp0wFagSitSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی: پخش خطبه‌های نماز جمعه از اشتباهات من بود!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/73073" target="_blank">📅 22:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73072">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/be565181a8.mp4?token=Fko17zJRnVzef2UhigRQq_yoE8Gnb0yRZFNW6FM1j9BUL5hYheYPE-S1QlqOfxylxhYB61fPfj3Rh1Vjr90lUHXjI0FyZl5sy7iYoGmsDyPJLrws6NXr_21AezMD-SZ0tGgTVLZkkfIVdO-RE7kPAsCuGHJrPOlqvyseeoPNPyAi9_RlJmvNwdeol2WUx0MMAwS9HG-TL9unL4Hv3oHFKF5wmLRcyBF9L61G2uVMlcPx6tneVOw4FJ3NcLhcNxRDc6YPoX8uq6ohhaPZQX35TV0AOpnzMg86m4QKBtMHT_rX45d8wAegGe4sqh2x0ORW852kMm4YqFCH_M-ztYnN3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/be565181a8.mp4?token=Fko17zJRnVzef2UhigRQq_yoE8Gnb0yRZFNW6FM1j9BUL5hYheYPE-S1QlqOfxylxhYB61fPfj3Rh1Vjr90lUHXjI0FyZl5sy7iYoGmsDyPJLrws6NXr_21AezMD-SZ0tGgTVLZkkfIVdO-RE7kPAsCuGHJrPOlqvyseeoPNPyAi9_RlJmvNwdeol2WUx0MMAwS9HG-TL9unL4Hv3oHFKF5wmLRcyBF9L61G2uVMlcPx6tneVOw4FJ3NcLhcNxRDc6YPoX8uq6ohhaPZQX35TV0AOpnzMg86m4QKBtMHT_rX45d8wAegGe4sqh2x0ORW852kMm4YqFCH_M-ztYnN3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند وقت پیش مصاحبه یه دختر 25 ساله منتشر شد که ماشین 50-60 میلیاردی سوار بود!
بهش گفتن چطوری این ماشین رو خریدی؟ گفت تلاش و استمرار!
رفتن امارش رو درآوردن، دیدن باباش حسابرس شهرداری تهرانه و دختره آقازاده‌اس!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/73072" target="_blank">📅 21:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73071">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118178a3fa.mp4?token=Cd5Cwxtyj2h5Hlr4QgDU-XHARPB6fxf4hAsaudAi_HK3a6Q3jXJRkpDwZJj0ooYqllzee60L2Rt75z6-oh6MKZazAjulZdFlyC-1whiENmVqq59UTanu4tTO-pZ89f9jzew9JeHeV5MaK3lmmcJhKXbNBddvoWLg2Z5Sygd63zBV4bMzbCX-QrMSQkyYQzC80IOV_u36dNZQ8aUWCIGDkRaTmU8LnaCcNOPcF0ednPK2c3PNZbDjHXKTJStRKgcQJRgcK7S_zGn5maSCY-S2GsQ-dj2whgI7cs2oHcWCkjFPb2uuFnFN9lF8HiMBHEn-Ao8D4gq6YhaWdyEmubDonA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118178a3fa.mp4?token=Cd5Cwxtyj2h5Hlr4QgDU-XHARPB6fxf4hAsaudAi_HK3a6Q3jXJRkpDwZJj0ooYqllzee60L2Rt75z6-oh6MKZazAjulZdFlyC-1whiENmVqq59UTanu4tTO-pZ89f9jzew9JeHeV5MaK3lmmcJhKXbNBddvoWLg2Z5Sygd63zBV4bMzbCX-QrMSQkyYQzC80IOV_u36dNZQ8aUWCIGDkRaTmU8LnaCcNOPcF0ednPK2c3PNZbDjHXKTJStRKgcQJRgcK7S_zGn5maSCY-S2GsQ-dj2whgI7cs2oHcWCkjFPb2uuFnFN9lF8HiMBHEn-Ao8D4gq6YhaWdyEmubDonA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته توافق نفتی شما با پوتین نشونه ضعف شماست.   ترامپ: کی اینو گفته؟  خبرنگار: زلنسکی.  ترامپ: باشه!  @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73071" target="_blank">📅 21:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73070">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=gXMI5U737irCQesf1Dnl0wAMj3-c1B2_n2fU-O2i5Z-w2WmJE7ftpHZseW83Pes-Fq8WBlHVioMJ423qVKPMo6jUyAzNgR1iNt8pxWE1_zpGVHSB_HS5ko5exBuS9wlfAxWs8_XDzwtOHVdwv0X83kdeZFTgWADVvdjrKwhIEMhX7e7LK-Ez3gmix_lfARP_ksKwLhQjBPSpEGX5E9IfgWHblYiBGpmFaPDNWriXfJnPpzxnEEp6rlNK9Vp1655mDT-4Gb86VhUyY_SRBwVNuCwCdiZd6tsez-edXFYuSRcl3S6pT27M6Z3zxPykxRMsnG4usJxx5JMmRuQbwdVx3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=gXMI5U737irCQesf1Dnl0wAMj3-c1B2_n2fU-O2i5Z-w2WmJE7ftpHZseW83Pes-Fq8WBlHVioMJ423qVKPMo6jUyAzNgR1iNt8pxWE1_zpGVHSB_HS5ko5exBuS9wlfAxWs8_XDzwtOHVdwv0X83kdeZFTgWADVvdjrKwhIEMhX7e7LK-Ez3gmix_lfARP_ksKwLhQjBPSpEGX5E9IfgWHblYiBGpmFaPDNWriXfJnPpzxnEEp6rlNK9Vp1655mDT-4Gb86VhUyY_SRBwVNuCwCdiZd6tsez-edXFYuSRcl3S6pT27M6Z3zxPykxRMsnG4usJxx5JMmRuQbwdVx3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه تصاویری از آتش‌سوزی گسترده و نشت نفت از یک نفتکش منتشر کرده که به گفته این نیرو، بر اثر برخورد با مین دریایی در تنگه هرمز آسیب دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73070" target="_blank">📅 21:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73069">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=B6sQl8rTPM6DeDkTiaJ8dvXkIGN1n4fw01nB_pXJvsLPmI_5Td5KUxWIKBQ5gSNXpa-fNfLcaVF9dqdX9YP_WDj4J4XHK-KLkByXAXBmn848Mvqw9ztsPeC0zZQpCwm4i9Q43qe4jnEUU-T_OOW6ShypyaYthsXrfO_187KNe2Kb3MiwINffvMuneiKURqwyyeZOgqnnrjFiayiX9yHNU5m68rbwbyrWXQmxKvEdJXXDjJoJI0lZBJUjvmz_J9c28YxzROhXiKhEA9mVzU7Squcm5oaKAYdck5c7qNsA82lSqQmv1YZ9hcfro9NSWVkbNn5xa5f9XStfjTk-lV9BuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=B6sQl8rTPM6DeDkTiaJ8dvXkIGN1n4fw01nB_pXJvsLPmI_5Td5KUxWIKBQ5gSNXpa-fNfLcaVF9dqdX9YP_WDj4J4XHK-KLkByXAXBmn848Mvqw9ztsPeC0zZQpCwm4i9Q43qe4jnEUU-T_OOW6ShypyaYthsXrfO_187KNe2Kb3MiwINffvMuneiKURqwyyeZOgqnnrjFiayiX9yHNU5m68rbwbyrWXQmxKvEdJXXDjJoJI0lZBJUjvmz_J9c28YxzROhXiKhEA9mVzU7Squcm5oaKAYdck5c7qNsA82lSqQmv1YZ9hcfro9NSWVkbNn5xa5f9XStfjTk-lV9BuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفته بودید تا بعد از انتخابات میان‌دوره‌ای به ایران حمله نمی‌کنید. حمله اخیر در عربستان باعث شده نظرتون عوض بشه؟
ترامپ: «بررسیش می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73069" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73068">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=BA04TCU3FbXtdD9WIJO9Jqf2lQL8CFIS1rOVkevEtQ3kDtkb-6CLwJUVebQg0YEShFdjc-LgQx6rgcItDgDGL-N7bPZkEsWj36H1GuPwQAw05vmqFexVjnMlmv5rEwEOx3DosK9lLnO2pAvOkj_AfCOsq_HtW52cgW4GP1QzpavHtJsrzlvYM6x1QCaLNWq21oDSgwiubm3Qdf2hUAZ_YRdLfCukTgIusHWv8jmfrcXyUIZE0fwNVsGQqIvTuPIGEpefxw6duSe0d6IACWV6LWASUxMsFENh3lI3y0-_75bcxtXOxKHkaBvB_0w_8tL3a-iwhMljoHOhYMPF1dA6Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=BA04TCU3FbXtdD9WIJO9Jqf2lQL8CFIS1rOVkevEtQ3kDtkb-6CLwJUVebQg0YEShFdjc-LgQx6rgcItDgDGL-N7bPZkEsWj36H1GuPwQAw05vmqFexVjnMlmv5rEwEOx3DosK9lLnO2pAvOkj_AfCOsq_HtW52cgW4GP1QzpavHtJsrzlvYM6x1QCaLNWq21oDSgwiubm3Qdf2hUAZ_YRdLfCukTgIusHWv8jmfrcXyUIZE0fwNVsGQqIvTuPIGEpefxw6duSe0d6IACWV6LWASUxMsFENh3lI3y0-_75bcxtXOxKHkaBvB_0w_8tL3a-iwhMljoHOhYMPF1dA6Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در ویدیویی جدید که در تیک‌تاک منتشر کرده، در حال ورزش کردن در باشگاه دیده می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73068" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73067">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89266c981.mp4?token=LdWRkaCbvHHwFk9yI3QJhN1XPhvli_rmLuDG9GkJaFB_esAtyDVxEmrRqzcVvgxNuKQzdsE0uTvDk9pb92avy6Hwen4s3p5sKftUWadddY-fQ2mjmIwwBgvk3y4BiwHuv_pyWngiwsZi1cfldg1PNUUfo1qRnx0g3Z3F8nwXvwEGXNO35quYmMdjvJWr0tVaV5AJUdin5OazXkKFSOHGbubJWx1vQjf3i_rkcO3jHnaYRATrki2vPGCFf_Eg9LndXATw60mXFQobRjxUBnif2q27Dz_q7-MVfe93sQGn47Q7qaUVlqGstkx7ER8iMSdJskjtXa40kCuyw9HZV3Atuoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89266c981.mp4?token=LdWRkaCbvHHwFk9yI3QJhN1XPhvli_rmLuDG9GkJaFB_esAtyDVxEmrRqzcVvgxNuKQzdsE0uTvDk9pb92avy6Hwen4s3p5sKftUWadddY-fQ2mjmIwwBgvk3y4BiwHuv_pyWngiwsZi1cfldg1PNUUfo1qRnx0g3Z3F8nwXvwEGXNO35quYmMdjvJWr0tVaV5AJUdin5OazXkKFSOHGbubJWx1vQjf3i_rkcO3jHnaYRATrki2vPGCFf_Eg9LndXATw60mXFQobRjxUBnif2q27Dz_q7-MVfe93sQGn47Q7qaUVlqGstkx7ER8iMSdJskjtXa40kCuyw9HZV3Atuoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور: آمریکا را پایین کشیدن کاری ندارد.روسیه باید پالایشگاه‌های آمریکا را هدف بگیرد تا حملات اوکراین متوقف شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73067" target="_blank">📅 20:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73066">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTtnYbGDFgDwMBKyWcEOXrF74OEPBSPz8DXc40CPu4E7apqaGFA-Q3IFEihAyzJQM-FxJEIqSB8JdBOPzvO3WX8HdTCkrwpfDPTw4GCzEeMDDZCAPrT6G2wGKQkfb_4ClYPR_JJx38H5MepFKAD3orAiL8Z-2HTQyhtLgW5BdVZkWJTB1qie6ntMtb3GeSzgWj0Z5ZCXtqMfTHotTotZQF9fFspqwlFOdnFu_NPPYwHvBLaVbg6lAFimodKyy1V6rISRTg2iauPNqF6k4W9Yj-Gdz1mcHq07sOFxvlFxxS-sVYZkzbrfOJK2wAb9wTn8klvuy7jF6UBvuFR7IDDzsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین محموله گازوئیل روسیه به مقصد آمریکا حرکت کرد؛ قبل از اعلام توافق ترامپ!
اولین محموله گازوئیل روسیه که راهی آمریکاست، ۲۲ سپتامبر از بندر سن‌پترزبورگ حرکت کرده؛ یعنی دو هفته قبل از اینکه ترامپ توافق رو اعلام کنه.
این نفتکش یونانی با نام MINERVA ZEN حدود ۲۷۵ هزار بشکه گازوئیل حمل می‌کنه و پیش‌بینی می‌شه ۱۱ یا ۱۲ اکتبر به سواحل شرقی آمریکا برسه.
تحلیلگران می‌گن حجم این محموله‌ها در مقایسه با مصرف گازوئیل و سایر سوخت‌های تقطیری آمریکا، فقط برای چند روز کافیه. از طرفی، حملات اوکراین به پالایشگاه‌های روسیه هم باعث کاهش تولید گازوئیل این کشور شده.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73066" target="_blank">📅 19:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73065">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=eX3inGRnm--q3cwZC1vd96I5pKH410e-o8FMZuj3LDPyxrohdWFmJUdVpXqFaqvrGwCuyvf56fNuRMfFgicMxN_CNv60vsHirhRfQVWczf7roglhmrjxR-JPodEzLKVpJCy59PgesdyCrquSYYbJ7waImyouU7k2_lFdBZe7omwiCwqjro3Gp_t5GKOmfB5A5W98csIFUYdDM9lu3DMNsfrXpz1hSRLPOT0MAZipbAz30C2KO5WKz6kA-NQYpM2hUQOoJH2I5NbGQP1Xn8PKOC7_hBVI8v9aknAQmekU0uyuw-GINYMw0NrgaUzmeCLgjoUJbK_naU9XlbHqBzil0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=eX3inGRnm--q3cwZC1vd96I5pKH410e-o8FMZuj3LDPyxrohdWFmJUdVpXqFaqvrGwCuyvf56fNuRMfFgicMxN_CNv60vsHirhRfQVWczf7roglhmrjxR-JPodEzLKVpJCy59PgesdyCrquSYYbJ7waImyouU7k2_lFdBZe7omwiCwqjro3Gp_t5GKOmfB5A5W98csIFUYdDM9lu3DMNsfrXpz1hSRLPOT0MAZipbAz30C2KO5WKz6kA-NQYpM2hUQOoJH2I5NbGQP1Xn8PKOC7_hBVI8v9aknAQmekU0uyuw-GINYMw0NrgaUzmeCLgjoUJbK_naU9XlbHqBzil0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان اجرای ارکسترال «آرش» در سالن اسپیناس تهران، در شامگاه جمعه ۱۷ مهر، تماشاگران در واکنش به صحبت‌های اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، او را هو کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73065" target="_blank">📅 19:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73064">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">برآوردهای اولیه از تلفات حمله به فرودگاه ریاض:
بر اساس برآوردهای فعلی، در پی اصابت یک تا دو موشک بالستیک انصارالله به ترمینال ۳ فرودگاه بین‌المللی ملک خالد در ریاض:
مجروحان: حدود ۴۰ تا ۷۰ نفر
کشته‌شدگان: حدود ۳ تا ۵ نفر
این آمار در حد برآورد اولیه است و هنوز تأیید رسمی آن مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73064" target="_blank">📅 18:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73062">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=IGkXf65bbRz5RgGPYclsRhPDUXqvTWK4YR6NEUb8BZR26m1I7RVN78epy2sZSIIavD1RgnBisTHKVSKfIQDQN-Si7_TeDUZrMCdFeMlyMECsl21QFBejp_rokKe9xq0KinM8Z7ycRYx9PTt14xzrHR-eXkT3ayjG52vCgjQsSdlkFAzL_4NSsPaFUfUuiLTNwVaXwr5haTCmIJGiiKW6LyZ8moZ_rpALhILGg2DBVCLjRAYe8KTXZb1aDhoklbztaNOOaNDxr03TI_lvvQ7wndeOJFiV97qtdpmqNhSSaChj7BrtViSGYpukX1bcpfb3C4YweGtjLRK7yZLVRGBFRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=IGkXf65bbRz5RgGPYclsRhPDUXqvTWK4YR6NEUb8BZR26m1I7RVN78epy2sZSIIavD1RgnBisTHKVSKfIQDQN-Si7_TeDUZrMCdFeMlyMECsl21QFBejp_rokKe9xq0KinM8Z7ycRYx9PTt14xzrHR-eXkT3ayjG52vCgjQsSdlkFAzL_4NSsPaFUfUuiLTNwVaXwr5haTCmIJGiiKW6LyZ8moZ_rpALhILGg2DBVCLjRAYe8KTXZb1aDhoklbztaNOOaNDxr03TI_lvvQ7wndeOJFiV97qtdpmqNhSSaChj7BrtViSGYpukX1bcpfb3C4YweGtjLRK7yZLVRGBFRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از فرودگاه بین‌المللی ملک خالد در ریاض پس از حمله منتسب به حوثی‌ها (انصارالله)
در این تصاویر، آثار خون روی زمین دیده می‌شه و نیروهای امدادی گسترده‌ای در محل حضور دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73062" target="_blank">📅 18:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73061">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش‌ها از وقوع حادثه‌ای بزرگ در فرودگاه ریاض؛
گزارش‌ها حاکی از وقوع حادثه‌ای جدی در فرودگاه بین‌المللی ملک خالد در ریاضه. احتمال داده می‌شه یک موشک بالستیک حوثی‌ها (انصارالله) به این فرودگاه اصابت کرده باشه.
تعداد زیادی از نیروهای امدادی و اورژانسی به محل حادثه اعزام شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73061" target="_blank">📅 18:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73060">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">#فوری
؛ خبرگزاری فرانسه (AFP):
خبرگزاری فرانسه به نقل از سه شاهد عینی گزارش داده که در حال تخلیه افراد از فرودگاه بین‌المللی ملک خالد در ریاض، پایتخت عربستان سعودی، هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73060" target="_blank">📅 18:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73059">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=O6LF9Wcrlz3N9M9yAZNWIMA_yd1m1F1aptoNrcf5xJMmLy2kuGg-49dQecyo_VFdZh6Z5oEZbfCNLl_kxXO_jWcNkvn9_CHd60aNUIXllFr543GyjmVgLWgjqg7HNGS5Plx175dUY0FPZO2EHV-axOErf8zMVgUOvwz8e2o74u3tPAS6BwfhhP9IS3LA1DNsPLMwdQRYSq-TgLT4HodCrAGUbcNLoJruDO1ZGT29sY-1Fu8aLb-kL0O4pVmmsYuV-INOUACPDyss1qDJonBa_hLUzzcnTwF-z9WuLpAEDJcVI0BkpdFJuZF-i3rZpavSxhO2a8zOMpAJHuPjg_UMgSV-uvniMLSGmvGLKUq4Le5ExlFPzlxo8xdKVqO2aD6jYwyeMlqvFG9XroVoHg5ZnnUtv_5D83QsFSiYU4F6jUYHxUKeiCz1GTifl6WKXzT9gFAh0GOxG2KFOFU8ocXwgo2HHsbddtYI7wdWXGVAynEUbhdT-p-tF4cLxtM7ZiHirPeTLvRCOZH8Ciq23Ll6NyuAMPotMR2F6xC-Bqoib9qymDEun7Qf-2iBuqkAqEf1pKFscq8eib9D2HK-2C2E_rrkMvByaBjfuoH4osxDlEuDrvYp0HY93ntK6impRBG3Z1nJvW2PsYj13JQAwKgg-Wikk3Yb07WMR9OTErqSX1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=O6LF9Wcrlz3N9M9yAZNWIMA_yd1m1F1aptoNrcf5xJMmLy2kuGg-49dQecyo_VFdZh6Z5oEZbfCNLl_kxXO_jWcNkvn9_CHd60aNUIXllFr543GyjmVgLWgjqg7HNGS5Plx175dUY0FPZO2EHV-axOErf8zMVgUOvwz8e2o74u3tPAS6BwfhhP9IS3LA1DNsPLMwdQRYSq-TgLT4HodCrAGUbcNLoJruDO1ZGT29sY-1Fu8aLb-kL0O4pVmmsYuV-INOUACPDyss1qDJonBa_hLUzzcnTwF-z9WuLpAEDJcVI0BkpdFJuZF-i3rZpavSxhO2a8zOMpAJHuPjg_UMgSV-uvniMLSGmvGLKUq4Le5ExlFPzlxo8xdKVqO2aD6jYwyeMlqvFG9XroVoHg5ZnnUtv_5D83QsFSiYU4F6jUYHxUKeiCz1GTifl6WKXzT9gFAh0GOxG2KFOFU8ocXwgo2HHsbddtYI7wdWXGVAynEUbhdT-p-tF4cLxtM7ZiHirPeTLvRCOZH8Ciq23Ll6NyuAMPotMR2F6xC-Bqoib9qymDEun7Qf-2iBuqkAqEf1pKFscq8eib9D2HK-2C2E_rrkMvByaBjfuoH4osxDlEuDrvYp0HY93ntK6impRBG3Z1nJvW2PsYj13JQAwKgg-Wikk3Yb07WMR9OTErqSX1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملکه تایلند برای نخستین بار به تنهایی هدایت یک جنگنده گریپن سوئدی رو بر عهده گرفت و پس از فرود موفق، از پادشاه مدال دریافت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73059" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73058">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73058" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73057">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYKA_CSH66w0wIzFKl2g4Nphp2XhIyezX-bQ2SqwYGQtD1v_AOVTjehBGIEKk71icQn3EaK2ytC-6vW72GS5MMNXQ72mGrD9CwnypyVLJwhfjGpYC9dDBUN60W3cS9xII3KZrq4eZq2MV7FKjs5xXGpbLoYKtfW6b-F64x6AiTzkMhS8BGuzjsJKDLpeQrl9ufSAiJNzdiA9IDDaot-ddfSe8bMLZrVjvXlfMXDiWl9GrzhaFD6pBrVQU0cEqYUPTQPk56CZxCq_OFha4z5eICt_XWks9Ghx7icZXIk9X0AEu5g7frkRLLW-WWV983mkBAmHJ6aPqfvfOPevK-tdzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز ویارئال
🆚
رئال مادرید رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
ویارئال: ۲ برد، ۳ شکست و ۱۱ گل زده
رئال مادرید: ۳ برد، ۲ شکست و ۱۰ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73057" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73056">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52e5fb32c.mp4?token=UdxlbNo9b7nf3DCNVDLTy_VkVAK_q7Vz-OlXsaJVmtwnI5AHVHcdouUcTU712cE1fcprHsqFw5b5zYSQdahbTkplILA5zRmvKHMDF_X9ewJBBPjoFc570SM4XZSb-rO-3CsxBymyq-4mNqYgPMf8wHp9OQu2XfrnTsRZQT9QNVEtmtmMOSxU-Qt68wFT5iksbmrxjFpTS4uDO7nTQhKH4gdkeX0EtFrW6WM0MEXzjEOywkvRaleU81d_kN8DFSSrRUmm85oui9_tcJIOflpEkylcZcExtcL9iyaB9uHHsG9xSHLuxSJlESLwSBY5xIJMgmYYNG_tQEfaqijles82dnT4p9w72orZQtD9qq-egserYWmbjGiMdBV4Nq-DHY-MOMdrd1jHMX9GiepppbJ__h5LykTtxhsV980xk1PabkyydroiQup2o-BMai4Pu8XRB1AqrY8Omo-Vp9ecrgVFg8vZZYUFv8ym2lSbecgQNjdwo2yLX6HIWuD0Gv714MgRk-UAXvZM6hA4vTM1cRE3Huq3VNLQKja8jkp04rIyia-Z2J-589ybBlI4lGYWQcNhZ1DipOaUo7HjW5FoBWRoKfk2UrqrqxPp6cQz_iQxvHjpy4VJPFoHtINIzYd2f69Cms71XNZTP9eD8auJspahDbg-atk2r8mt2mjL_RTENMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52e5fb32c.mp4?token=UdxlbNo9b7nf3DCNVDLTy_VkVAK_q7Vz-OlXsaJVmtwnI5AHVHcdouUcTU712cE1fcprHsqFw5b5zYSQdahbTkplILA5zRmvKHMDF_X9ewJBBPjoFc570SM4XZSb-rO-3CsxBymyq-4mNqYgPMf8wHp9OQu2XfrnTsRZQT9QNVEtmtmMOSxU-Qt68wFT5iksbmrxjFpTS4uDO7nTQhKH4gdkeX0EtFrW6WM0MEXzjEOywkvRaleU81d_kN8DFSSrRUmm85oui9_tcJIOflpEkylcZcExtcL9iyaB9uHHsG9xSHLuxSJlESLwSBY5xIJMgmYYNG_tQEfaqijles82dnT4p9w72orZQtD9qq-egserYWmbjGiMdBV4Nq-DHY-MOMdrd1jHMX9GiepppbJ__h5LykTtxhsV980xk1PabkyydroiQup2o-BMai4Pu8XRB1AqrY8Omo-Vp9ecrgVFg8vZZYUFv8ym2lSbecgQNjdwo2yLX6HIWuD0Gv714MgRk-UAXvZM6hA4vTM1cRE3Huq3VNLQKja8jkp04rIyia-Z2J-589ybBlI4lGYWQcNhZ1DipOaUo7HjW5FoBWRoKfk2UrqrqxPp6cQz_iQxvHjpy4VJPFoHtINIzYd2f69Cms71XNZTP9eD8auJspahDbg-atk2r8mt2mjL_RTENMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دختر خانوم با این پسره تو رابطه اس و که علاوه بره پسره، سگ دوست پسرش هم عاشق دوست دختر پسره شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73056" target="_blank">📅 17:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73055">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502e54151d.mp4?token=sRCgi8-b_eXzBdgl19eF6ID90zHFfSt6PNKaWcjQ4HI2i646bvyTkjZMGohRKKTlGrsECeUf3kg5aF2Bc8PXVkCXe7cXQU3459DR45kqyNUhZmRwoFakP0MBM1heQEhq7U5OGAWOBrNPEaoEqLDtY6SSsa3uZd-k2bxbAGv2Rk22Gir1a7wOIbx186pHP0Oa_5LEaoGCevjlrDGGGSHj2jKAxu1pDO4M2vxQzRfPNIrU--bN1imm1NqniorSFUdz8K5sgKeDU_vkYJ3_jFKV-xuyhFsRIm50F9oVOJdNTEVv9NHhypS80f0ZRG2AH8ELzvkjEWOnHNzhqYCefIdKlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502e54151d.mp4?token=sRCgi8-b_eXzBdgl19eF6ID90zHFfSt6PNKaWcjQ4HI2i646bvyTkjZMGohRKKTlGrsECeUf3kg5aF2Bc8PXVkCXe7cXQU3459DR45kqyNUhZmRwoFakP0MBM1heQEhq7U5OGAWOBrNPEaoEqLDtY6SSsa3uZd-k2bxbAGv2Rk22Gir1a7wOIbx186pHP0Oa_5LEaoGCevjlrDGGGSHj2jKAxu1pDO4M2vxQzRfPNIrU--bN1imm1NqniorSFUdz8K5sgKeDU_vkYJ3_jFKV-xuyhFsRIm50F9oVOJdNTEVv9NHhypS80f0ZRG2AH8ELzvkjEWOnHNzhqYCefIdKlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از بمباران پادگان سپاه در خرم‌آباد، استان لرستان، در جریان جنگ ۴۰روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73055" target="_blank">📅 17:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73054">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3cACqMauRkKT5yG3WZGitXLyX5Ubxb4u4cX1VHVajQnIBvoMSL8fiqZT4Inq-f0iyCB9INV4q8Lmo4kgIpaFHqYeLB18gWYQbdknKhU94gRMdC3PTinjT-vjVWuKQG5N7UR4L7fuC_2AOc8b316orUr6djCEzxI8OrFJC3ZCm5155QEXRt4LioONo3645NHkuzWWc70BJ6gsz7Oimkqen2eAWBJR1ttaVaJlJ_Ov7kZj5hnlTPKznpsExzlvh1oUEW8QWN9evofDxWV8VJzWdEeHTvmDvKNf8a6yOBsyq9wMqU8ergTGcjGKyBxq9h8U7OHl41Uizg5090rY2fCuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
معاریو: آمریکا از اسرائیل خواسته به‌تنهایی به ایران حمله کنه!
طبق این گزارش، واشنگتن توی مذاکرات دو هفته اخیر از اسرائیل خواسته بود بدون مشارکت مستقیم آمریکا، حمله نظامی به ایران رو انجام بده.
هدف آمریکا این بوده که پیش از انتخابات میان‌دوره‌ای نوامبر، هزینه سیاسی حمله به ایران متوجه ترامپ نشه؛ درحالی‌که چنین حمله‌ای می‌تونست از نظر سیاسی به نفع نتانیاهو، پیش از انتخابات اسرائیل در ۲۷ اکتبر، تموم بشه.
ایال زامیر، رئیس ستاد ارتش اسرائیل، هشدار داده بود که ازسرگیری جنگ می‌تونه باعث تعویق انتخابات اسرائیل بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73054" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73053">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fca26fcca.mp4?token=Dyjeka39C3hVJBVED23agASL0RtqjAtozFZLvyw-oNCt_0x6TREls7ludQYJ7OZRcdyn-MNdJ7CDKwg2ZFAWWYBy_jCulMASYh2uysGFCaxuIASy5HRyjjHrGDQMOI9JkOi4SM5YPXy-5Jc1B5wQhgU1SZ3WttmpEwnMTxobwWJkRCNHm9-4me-5zoPhVt1E_iJrNoD6CUUyTk7YkgM8byPLXsobU0F0RsetsfU0fTEaAOJldy_eDgBWYbifc3wZrATyChjQuViRdGd9sj-peRFpzIAGCmVJ4OtRCLwp1fVAhsZur-vPhPpCi3qq0QLZgjHbOlbGcY-Ocj_UmE3SZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fca26fcca.mp4?token=Dyjeka39C3hVJBVED23agASL0RtqjAtozFZLvyw-oNCt_0x6TREls7ludQYJ7OZRcdyn-MNdJ7CDKwg2ZFAWWYBy_jCulMASYh2uysGFCaxuIASy5HRyjjHrGDQMOI9JkOi4SM5YPXy-5Jc1B5wQhgU1SZ3WttmpEwnMTxobwWJkRCNHm9-4me-5zoPhVt1E_iJrNoD6CUUyTk7YkgM8byPLXsobU0F0RsetsfU0fTEaAOJldy_eDgBWYbifc3wZrATyChjQuViRdGd9sj-peRFpzIAGCmVJ4OtRCLwp1fVAhsZur-vPhPpCi3qq0QLZgjHbOlbGcY-Ocj_UmE3SZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی ترسناک و باورنکردنی که امواج عظیم زیر رعد و برق یک کشتی باری غول‌پیکر را ناچیز نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/73053" target="_blank">📅 16:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73052">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8hIqes-cnegJnZfv9UZpcZzBEAxIe4d9shpE5r2zUMjQpwPU9ch7oq1ZI9H0iuMhMJyKAdW8ydW6c85UwyeCml6FY05JBqyTiSZKj-S4jKr_04Ao5uy3vMVOSuJwSVjPT-eWNWSqQObQQhJvX07sZNa5jVxAtHdzG_rIh5XLP-zkxRfggXehnx_x9C00SRbpp_XLrtteMf1f9oOmz1pTsJ6x9pP265pQthmb2yrFLD3OISvDVasJ5IaZFD2cVQwN7P00ukLXs6O_QHy-IsfRZvwNBJppqZzIH9fy9FWpZSNslyCy1aoxtTosJ9JaoFg-nGdxWDHr8mlnZBFejyztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:«من به ۸ جنگ پایان دادم و به پایان دادن یا حل‌وفصل ۲ جنگ دیگه هم نزدیکم.
همه گروگان‌های اسرائیلی، از جمله ۲۸ نفر آخر رو، چه زنده و چه کشته‌شده، برگردوندم.
صدها گروگان از کشورهای مختلف جهان رو آزاد کردم و به خونه‌هاشون برگردوندم.
در ونزوئلا در جنگ پیروز شدم و دیکتاتور خشنی رو که با بی‌رحمی اون کشور رو اداره می‌کرد، دستگیر کردم.
همچنین جلوی جمهوری اسلامی ایران، بزرگ‌ترین حامی دولتی تروریسم در جهان، رو گرفتم تا به سلاح هسته‌ای دست پیدا نکنه؛ و خیلی کارهای دیگه!
با وجود همه این کارها، نه من و نه ایالات متحده آمریکا جایزه صلح نوبل رو نگرفتیم. عجب!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73052" target="_blank">📅 15:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73051">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=rEssZa26zoDlLgleLYDQsCbymclrt_g5wsnHFSgiM9o-_lTU4rW3D8H0lvv2_M7nRlMqpc2jW0Fc1oTqAa89qmWtyLYNiLEHCx5c1xKjxrbrGWUZ4tqxPjcrwuh5gs_HLfhwo0ZGBArd89jLt1VfdjtVzsTuvg0C9dde0JncRjvXonB-EjP3Fro6QM-s-3MfnSxUiK9cy6gvHfv5V7jJ5VjRh70vpE5aeyALMkTtkVLEXNbUYkMs7ZTBjiZMMtPNn5BeeZqVJz68LcmH6EG8pf9xal02kmCiDCqLGI3lRakks0YThkBiuNpRy78fKNlNAlwUaEYp1axjSWWjemYAbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=rEssZa26zoDlLgleLYDQsCbymclrt_g5wsnHFSgiM9o-_lTU4rW3D8H0lvv2_M7nRlMqpc2jW0Fc1oTqAa89qmWtyLYNiLEHCx5c1xKjxrbrGWUZ4tqxPjcrwuh5gs_HLfhwo0ZGBArd89jLt1VfdjtVzsTuvg0C9dde0JncRjvXonB-EjP3Fro6QM-s-3MfnSxUiK9cy6gvHfv5V7jJ5VjRh70vpE5aeyALMkTtkVLEXNbUYkMs7ZTBjiZMMtPNn5BeeZqVJz68LcmH6EG8pf9xal02kmCiDCqLGI3lRakks0YThkBiuNpRy78fKNlNAlwUaEYp1axjSWWjemYAbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهرداری خرمشهر دیده یه سرسره تو پارک شکسته، با خودشون گفتن چکارکنیم چکارنکنیم؟؟
که این نیمه شاهکار رو پیاده کردن :
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73051" target="_blank">📅 15:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73050">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=Sf1dUXo9wUwE4UAkV__ftINboGc5hK_zajXQPlokT1Hh7uFy9uoT8ZoZCNQP7bEyNKcWlOlXBShyfAlLdGyKKLyqvFkwMjbEB-0OAMxrlxcYfnXJyzUw-4hMbm6ou6kv12OXg5l-XBVOLN_bZ9L4GYd5L6sg94NDkuxp7Ebk1Ahc4tzj9bnKXh8lcuXm8EeFuEYDyAw_Jmkaid6DfGHW6-6IMmTsJLAPSUYgGBTiAp4LlyVV3eKLCkcN8PoAZIwA6lD3gskh7AznTzZMF_aTrzun1TnIyjsBgr-dnGxRr4-A03ScgWSjpm-w4t1CW527UMEpXZMdXFpOTzzXk1JkFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=Sf1dUXo9wUwE4UAkV__ftINboGc5hK_zajXQPlokT1Hh7uFy9uoT8ZoZCNQP7bEyNKcWlOlXBShyfAlLdGyKKLyqvFkwMjbEB-0OAMxrlxcYfnXJyzUw-4hMbm6ou6kv12OXg5l-XBVOLN_bZ9L4GYd5L6sg94NDkuxp7Ebk1Ahc4tzj9bnKXh8lcuXm8EeFuEYDyAw_Jmkaid6DfGHW6-6IMmTsJLAPSUYgGBTiAp4LlyVV3eKLCkcN8PoAZIwA6lD3gskh7AznTzZMF_aTrzun1TnIyjsBgr-dnGxRr4-A03ScgWSjpm-w4t1CW527UMEpXZMdXFpOTzzXk1JkFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
نفت ایران مال مردم نیست و متعلق به خدا و پیامبره
مردم  حکومتو انتخاب میکنن فقط و اون حکومته که تصمیم میگیره چطوری نفت استفاده بشه
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73050" target="_blank">📅 15:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73049">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520264f117.mp4?token=kuJWRf9a4rDX0mpdiIIRplmJ4qhTFtflH2Y-VAw8VHCcufhRFegzzJP94xOnUBr6OA9tgpxNPSD8AIqpDV_GDQCRT4pVq3MqP_SojQS3i3KDQT_VNpHYsTwFlPYe1ABD6VywkMvJGzEKK1bZSqg105_6r0lZox7954Jl7-ikWBD1ICpU5HrJMBPYg2U01ssfEJNSY-z-XzUwdODM1D_i6ewZCPGOs44T1hQdJz8_Rjs8hXYxDXDQha1GHRkQg-A20afaGEyBW8EuQSi3xBRBfba2h_urlEIEIBdsOrlJf39IUzBDHqS_CNuj2gvUHBOB_D4L29UnJjIAzBYEz6wfRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520264f117.mp4?token=kuJWRf9a4rDX0mpdiIIRplmJ4qhTFtflH2Y-VAw8VHCcufhRFegzzJP94xOnUBr6OA9tgpxNPSD8AIqpDV_GDQCRT4pVq3MqP_SojQS3i3KDQT_VNpHYsTwFlPYe1ABD6VywkMvJGzEKK1bZSqg105_6r0lZox7954Jl7-ikWBD1ICpU5HrJMBPYg2U01ssfEJNSY-z-XzUwdODM1D_i6ewZCPGOs44T1hQdJz8_Rjs8hXYxDXDQha1GHRkQg-A20afaGEyBW8EuQSi3xBRBfba2h_urlEIEIBdsOrlJf39IUzBDHqS_CNuj2gvUHBOB_D4L29UnJjIAzBYEz6wfRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از اجرای امیرمحمد، نوجوون ارومیه‌ای داخل برنامه Kaos Show ترکیه:
+ این برنامه، عقب‌افتاده‌هایی که تو فضای مجازی معروف شدن رو دعوت میکنه تا مردم بهشون بخندن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73049" target="_blank">📅 14:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73048">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=Iswrm8S4zU69iQem6KJo1H25XRKNL_xYEVe1sgYF5gIk9bKqISWLRHbFBYFBOprYFpah0WAxB7sMgQtWHL76cTXAucdbngY0JPnVaC3HO74d6PCetKhxttq0MuKSjXRSm0ogEk-jDJVe73yM3xCecMvaTPX6av-JD6pkMUOWdHKQXfegzd83N2WN453jmLE582dRcgf98-VPYdwd959yYQTj36Qb811pq3FEVgNkUMefhaG-jM0IRN27NAmWz_TM1eiZS7c1FcD5kQUF2t0Zi82A3949pxLW5HMaWlHrhzuySLFsSv3MknqVQFdZP0ikkGEB-4yI8fKJl3aahjNDOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=Iswrm8S4zU69iQem6KJo1H25XRKNL_xYEVe1sgYF5gIk9bKqISWLRHbFBYFBOprYFpah0WAxB7sMgQtWHL76cTXAucdbngY0JPnVaC3HO74d6PCetKhxttq0MuKSjXRSm0ogEk-jDJVe73yM3xCecMvaTPX6av-JD6pkMUOWdHKQXfegzd83N2WN453jmLE582dRcgf98-VPYdwd959yYQTj36Qb811pq3FEVgNkUMefhaG-jM0IRN27NAmWz_TM1eiZS7c1FcD5kQUF2t0Zi82A3949pxLW5HMaWlHrhzuySLFsSv3MknqVQFdZP0ikkGEB-4yI8fKJl3aahjNDOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله، رهبر کتلت شده حزب‌الله لبنان، ۲۷ خرداد ۱۳۸۸:
امروز در ایران چیزی به اسم تمدن پارسی وجود ندارد.
آن‌چه در ایران وجود دارد، دین محمدِ عرب است.
موسس جمهوری اسلامی هم عرب بود و عرب‌زاده. امام خامنه‌ای هم عرب است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/73048" target="_blank">📅 13:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73046">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=tei4tU3T3yxQAA8bykgv8zAQ08Ld2bIvh22iXn2qjr3-EetzVoT3CmQdma3aFpWlj8lbMFDSWV1LtXBSD4v-75FflmF_7kNR57h9qWG6sAXE8R7lPZjLR2IQC_SZ39HGHoJUCD-96XLblvJEzqtXgWE5j45reA__4hpl6OVVDouhotUyNjGEAYLcSMS4QO2gfA-B7vu901SiL37hJzD3QOuknx7f1LSOeU0ibnI2ATXumZnOU0ZKSBrI9ytjciVm20axfg6DMfuqYygBDFEQyrF7B8W6MiB-oKAdEPj4GdE8lCLnaV06GctfLIa3TEc_E2EbR-hSGNSoPxJWqPvERQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=tei4tU3T3yxQAA8bykgv8zAQ08Ld2bIvh22iXn2qjr3-EetzVoT3CmQdma3aFpWlj8lbMFDSWV1LtXBSD4v-75FflmF_7kNR57h9qWG6sAXE8R7lPZjLR2IQC_SZ39HGHoJUCD-96XLblvJEzqtXgWE5j45reA__4hpl6OVVDouhotUyNjGEAYLcSMS4QO2gfA-B7vu901SiL37hJzD3QOuknx7f1LSOeU0ibnI2ATXumZnOU0ZKSBrI9ytjciVm20axfg6DMfuqYygBDFEQyrF7B8W6MiB-oKAdEPj4GdE8lCLnaV06GctfLIa3TEc_E2EbR-hSGNSoPxJWqPvERQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب صدای این انفجارها توی شرق تهران شنیده شد که گویا تست پدافند بوده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/73046" target="_blank">📅 12:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73043">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/351194ef56.mp4?token=WtpQLFBGZqIjuWEzXrZZvab1YfydvHGNE1jMeg27xkJtB0p-td4726coZxgF3PdoGBcs7pWCnV9Ylq2UfiFxARzfpRCuVD0OJjHYuXLrhQPBsO8GAuXZGHf3Hak2GSLaukJAmgzCyFcdm2Gw2nMIb9xQ84ahXPQQJ-szQONFUO2s4i5hdMvmV4G9QMrgTtC9UOp96b_5jMrX4o5vtMwOVBER2hg8sAyS1d3RQqcWqcH0s9GwS7bF7VgIWLaCKrX44petZGvsikD3-_T2dh3rxTqDY2xqHL1KFUU8WZUIp3U3UdLl6TTwfvNDKsnr3PDvUkHfAro3pSJ4Yp9rTO-Lvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/351194ef56.mp4?token=WtpQLFBGZqIjuWEzXrZZvab1YfydvHGNE1jMeg27xkJtB0p-td4726coZxgF3PdoGBcs7pWCnV9Ylq2UfiFxARzfpRCuVD0OJjHYuXLrhQPBsO8GAuXZGHf3Hak2GSLaukJAmgzCyFcdm2Gw2nMIb9xQ84ahXPQQJ-szQONFUO2s4i5hdMvmV4G9QMrgTtC9UOp96b_5jMrX4o5vtMwOVBER2hg8sAyS1d3RQqcWqcH0s9GwS7bF7VgIWLaCKrX44petZGvsikD3-_T2dh3rxTqDY2xqHL1KFUU8WZUIp3U3UdLl6TTwfvNDKsnr3PDvUkHfAro3pSJ4Yp9rTO-Lvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و هیچکس بعد از ۱۰ سال قهر و دعوا، دوباره باهم داداشی شدن و دیشب کنار هم روی استیج رفتن!
نکته جالب ماجرا این بود که سروش هیچکس فریاد «جاوید شاه» سر می‌داد و سالن رو به لرزه درآورده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73043" target="_blank">📅 12:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73042">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73042" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73041">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq7xTdtn3ER3txVAK92vsBcWKongGbjaiIoRzMYTs8SKctM40HNt28jIjbBTy-Zi_q6-9wfgo73fjrtOhFdoA-3pWlgi30v8A40uiQtTOMnTcCQthzR0q3jL56cNj0GbYJDzNchERGw6762XNAanYAFPfn80c08Qarr_fn9wQWlWW1pJ24jnP2gzJ6rTggzEp9aATpUTZWZAX76EsWDba_srIYsPAM3Gkt5A4rgKZTomiWFi5i5hEz2mOFnFr68YOm7U1mLP8EEvrQQ2YYJc2V3LT-tlMTnOVscq6S5TF9CqYqSt3oAH0Yk5VdaQqkUggzoFhCgkaZ7TpCvN8qbGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
لیدز
🆚
آرسنال
بورنموث
🆚
چلسی
تاتنهام
🆚
منچستر یونایتد
ختافه
🆚
بارسلونا
ویارئال
🆚
رئال مادرید
بایرن مونیخ
🆚
آگزبورگ
پارما
🆚
اینتر
فروزینونه
🆚
ناپولی
لومان
🆚
پاریسن‌ژرمن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73041" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73040">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=ni7-E9eEejvxGZpwzqZAnQm_Hm6WNaGQPq1FAC6-5LuuICaCXptePlT1wuG4tcIkdujMFFMisJBeLvu6SpF-d4kLh5xaUmHwtA5U1ciN5ga34lgT1Qvw_TsZmRBUAXXoWUnJfcWKo20-I63xAAdCBEAHEASyfanT6wJIyJV77eX9kifSKFsFrMOv1h_ycPze8RydomPU3XWC1s4FgA05G3obvW65u45d5i0L_kNYHjFwUgjpujsdDPqToPxxNw4yrfR7iKo3B9j4LIC7ISDXiZckDLqu7YCsQ9K99jZU5zaYUMQNJzSktBLB8pUDS7Z1HLtoU7L4N6jJyfYt45mNlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=ni7-E9eEejvxGZpwzqZAnQm_Hm6WNaGQPq1FAC6-5LuuICaCXptePlT1wuG4tcIkdujMFFMisJBeLvu6SpF-d4kLh5xaUmHwtA5U1ciN5ga34lgT1Qvw_TsZmRBUAXXoWUnJfcWKo20-I63xAAdCBEAHEASyfanT6wJIyJV77eX9kifSKFsFrMOv1h_ycPze8RydomPU3XWC1s4FgA05G3obvW65u45d5i0L_kNYHjFwUgjpujsdDPqToPxxNw4yrfR7iKo3B9j4LIC7ISDXiZckDLqu7YCsQ9K99jZU5zaYUMQNJzSktBLB8pUDS7Z1HLtoU7L4N6jJyfYt45mNlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
مرگ مردم در تصادفات رانندگی به علت رانندگی بد آن‌ها است و ارتباطی به کیفیت خودروهای داخلی ندارد.
واردات خودرو خارجی باعث می‌شود کشور پیشرفت نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73040" target="_blank">📅 11:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73039">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=MnfWLUvNZmoLtjEuGMAE1QndMLRIScRCx_eotP_M1hzWXPu8VCXv93yPD_SqwPw4VsMgzbscgiBVhQ-z2fZW_56TnewFvrjeg_e649830PJu3KX_l0G-aYliWWhy0c47YRVFWejoSKGqm_0KykKgLcvlVzRg99o9Bi8KOBfeTjmls6sbfgIWhF3zX3QeuFsgeO0KAMucpUL2DG427XySXBUAMvBNCWP9584z6qmyuvPtWA9KZXiBdfOkQCYeYnWnqDsBRjJd-ZTeLQMbLpY3M-PP3Qdu5SPMWf4lf17FGhyWaNKEFi19jkLBjvwogv2KdfjKDOaHyBXrYnGtf13O2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=MnfWLUvNZmoLtjEuGMAE1QndMLRIScRCx_eotP_M1hzWXPu8VCXv93yPD_SqwPw4VsMgzbscgiBVhQ-z2fZW_56TnewFvrjeg_e649830PJu3KX_l0G-aYliWWhy0c47YRVFWejoSKGqm_0KykKgLcvlVzRg99o9Bi8KOBfeTjmls6sbfgIWhF3zX3QeuFsgeO0KAMucpUL2DG427XySXBUAMvBNCWP9584z6qmyuvPtWA9KZXiBdfOkQCYeYnWnqDsBRjJd-ZTeLQMbLpY3M-PP3Qdu5SPMWf4lf17FGhyWaNKEFi19jkLBjvwogv2KdfjKDOaHyBXrYnGtf13O2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک تایسون، بوکسور افسانه‌ای:
«اگر رئیس‌جمهوری مثل دونالد ترامپ وجود نداشت، به‌هیچ‌وجه امکان نداشت امروز اینجا باشم. متشکرم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73039" target="_blank">📅 10:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73038">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d334669b16.mp4?token=FpFooKG7xo_ZF9DARZFqmBSZk45MpReAN2Gr1ReaETbwy0h-DmR1QKURs5DqS39d3Sj9uu3B7zCQX6DpGGTUP4OsJ9RsPPjywjT_AMZlqh3Ou1phC_1me024PyTRlmlpJgL9NhJocwfQxcnTSUHoG-2rPhGz6P1nuAQQU5Qe7k92ooR2oLJWopqxItM4qFcjzq7n9obMWzo_wnYpNuPw6QaNqjH4k-OoyJ-Ftz9kuFd3c7h_ZpI0aqq55FlGlqaSkrePJNmsqT4fkyE4qBmgawCQH7eYlIDG9ZLpr1Vq7a9iWXe-KQwQ80kcFjRB4yCjTBniW9Dz6qjfHD0x6ZlJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d334669b16.mp4?token=FpFooKG7xo_ZF9DARZFqmBSZk45MpReAN2Gr1ReaETbwy0h-DmR1QKURs5DqS39d3Sj9uu3B7zCQX6DpGGTUP4OsJ9RsPPjywjT_AMZlqh3Ou1phC_1me024PyTRlmlpJgL9NhJocwfQxcnTSUHoG-2rPhGz6P1nuAQQU5Qe7k92ooR2oLJWopqxItM4qFcjzq7n9obMWzo_wnYpNuPw6QaNqjH4k-OoyJ-Ftz9kuFd3c7h_ZpI0aqq55FlGlqaSkrePJNmsqT4fkyE4qBmgawCQH7eYlIDG9ZLpr1Vq7a9iWXe-KQwQ80kcFjRB4yCjTBniW9Dz6qjfHD0x6ZlJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ پرزیدنت ترامپ:
«ایران یا همه‌چیز رو به ما می‌ده، یا دیگه وجود نخواهد داشت. خودشون اینو می‌دونن.»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73038" target="_blank">📅 10:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73037">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">میرسلیم:
تیبا با خودروهای خارجی ظرفیت رقابت داره
واردات خودرو باید یک در هزار بشه هموناییم که وارد میشن برای این باشه که ببینیم چطوری ساخته شدن
مجری:
الان چرا کشورای حوزه خلیج فارس همه بنز و ماشینای خارجی سوار میشن ولی ما سمند و تیبا و دنا با این قیمتای بالا سوار بشیم...؟
میرسلیم:
میل و انتخاب خودتونه دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/73037" target="_blank">📅 10:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73036">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سپاه  تصاویری از حملات پهپادهای «شاهد» و موشک‌های کروز به شناورها در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/73036" target="_blank">📅 09:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73034">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ویدئو های وایرال شده از دعوای پشت پارک یه مدرسه دخترونه در تهرانپارس که دو تا اکیپ با دوس پسراشون رفتن داخل پارک بخاطر اینکه یکی از دخترا همزمان با 4 تا دوس پسرِ دوستاش داشته خیانت میکرده به رفیقاش و گرفتن چند نفری زدنش و دوستای دختره هم برای دفاع ازش اومدن!
نکته جالبم اینجاس که چرا دوس پسراشون ایستادن کنار نگاه میکننو نمیرن جلو جداشون کنن و گاهی تشویق هم میکنن که بیشتر بزن هم دیگه رو!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/73034" target="_blank">📅 09:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73033">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/73033" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73032">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G9VS4qgXggIDuAETOJfgbMYqEqKy69hlgvKtIjkiJ5jdslPKv06Cxw44GgQ4TOtksHmI1gGao0iqG5nGUBaZPSkNfttYC1Vk3Feyon0Ag84kjmxLOEifnWyY4cdpbOXBRxPdcNMY3fscEKCM_ZMwAQ0vNHsdSgkkxtf_6djt97nu1PTUpSZTRD9HRrk8Oy_K31lAik3dTvBc8ihfy-pI3T4WIO0yF0ofiiAYEbCf0EOscrns-3jYP-RD3RLkWkH3bRe6am8S7qC0MsGrQzpUkGAeinapS5eS6xL9l-z7CwkQ4vlEtwybVQV9CkqsCoxZOzdBLhbRDZZF2bt0GT4iUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/73032" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73031">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=sHELgvNOIhkKMY7muoWD5loV-Z7kYasxzh7PIHAzhGYIop6ymvKqkQpoPBDIbByjjQo0PNV8_0_5s_F3qjPnFbYDihPAP6ZgRdNMaK7eVL9xzLqc1aPIOsV7l-zx6JJ59tIF0b8CqM_UJV2NgdELdI7hQsPZDfok97yMqxjtnQpJ2RG5Lm8qOwxegIatGHaDOL2tOp68wcuHKgBOIKSAzbDUn36s-R6DPQgm802IfAfll3yjz3nA7D4FHlyUaNOyRtMJk-G5ghUP8-ayXVCi60Te8vNuyQ2sac486OjC_lL_qY_NYD7Hbwzm7QJYMpWdI6lWnzt5RkaUNnAiTKWyYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=sHELgvNOIhkKMY7muoWD5loV-Z7kYasxzh7PIHAzhGYIop6ymvKqkQpoPBDIbByjjQo0PNV8_0_5s_F3qjPnFbYDihPAP6ZgRdNMaK7eVL9xzLqc1aPIOsV7l-zx6JJ59tIF0b8CqM_UJV2NgdELdI7hQsPZDfok97yMqxjtnQpJ2RG5Lm8qOwxegIatGHaDOL2tOp68wcuHKgBOIKSAzbDUn36s-R6DPQgm802IfAfll3yjz3nA7D4FHlyUaNOyRtMJk-G5ghUP8-ayXVCi60Te8vNuyQ2sac486OjC_lL_qY_NYD7Hbwzm7QJYMpWdI6lWnzt5RkaUNnAiTKWyYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/73031" target="_blank">📅 01:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73030">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIvmv97H_hunZpLTOj4OFRy4gDntNAlYwV4c8K8xFajL9R1USt5GzVywvrIQUt10FiG8KOsZSownAcpNwHbwjc3OeNNEHoSZpBQ_AgRqYK-2Yon1n7bADXWo1ZBl6XIJqXIFhogx_EezI8eMoa_Er7JNWmJmKYwFto5dIKj5atzFJ1xMo2ZP5q7niMGByvfWnqO92QKqGGPZhXvTul74_sjXaCfGXyq7rCEkHaySJGEuVq4CepdCMzS-gpcuSoBhFoSiExaKJ3JFFq35l_vSWHSr0WoP5tSb-ibg_fWP9YdD8Lx2OO9nNdJlMJgmYlxEo2AtKB1RixGz33aowa4jGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار امنیتیِ وزارت امور خارجه آمریکا:
به شهروندان آمریکایی هشدار می‌دیم که فورا ایران رو ترک کنن و به هیچ عنوان به این کشور سفر نکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/73030" target="_blank">📅 01:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73029">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">از سیریک چندین پهباد/موشک به سمت شناورها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/73029" target="_blank">📅 01:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73028">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0925073180.mp4?token=gpfZTd17bs8plmWmej7QvB2aFcHU9RF8yGd0-EwN5YRiBqiRYIYe03fYa13bgMdzc1Nb6V2dz9lA8gO1vwnErX15BcevRd7uLNSfFvsCRDsw2D21VQKf7fWQzXp2Lh_DUQACe9oaccSsFOBqX2MK5IOC4Ao9fpe7D8MpfbjJPEOqsqmrP9hXKU5c48jYJ0eEnDqt6mRs8qMBzscVcOPg6NsyZH88fMJ56Fat5yEqaUEPvqg9PVwaePS7Cv5zHmD_yx87qVDaRZ9QCUvHy9R97S3aoh8o1S3ImfENrjWn2UauDofR5W3j0SJlVBlv8nfgRFZDlJ9xO0K2Aye8ty493A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0925073180.mp4?token=gpfZTd17bs8plmWmej7QvB2aFcHU9RF8yGd0-EwN5YRiBqiRYIYe03fYa13bgMdzc1Nb6V2dz9lA8gO1vwnErX15BcevRd7uLNSfFvsCRDsw2D21VQKf7fWQzXp2Lh_DUQACe9oaccSsFOBqX2MK5IOC4Ao9fpe7D8MpfbjJPEOqsqmrP9hXKU5c48jYJ0eEnDqt6mRs8qMBzscVcOPg6NsyZH88fMJ56Fat5yEqaUEPvqg9PVwaePS7Cv5zHmD_yx87qVDaRZ9QCUvHy9R97S3aoh8o1S3ImfENrjWn2UauDofR5W3j0SJlVBlv8nfgRFZDlJ9xO0K2Aye8ty493A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته توافق نفتی شما با پوتین نشونه ضعف شماست.
ترامپ: کی اینو گفته؟
خبرنگار: زلنسکی.
ترامپ: باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/73028" target="_blank">📅 00:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73027">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=ml5GB_sLmd_N-UOMrAP1AQ0bi6A-4MhSWsjOC-q316U54MPBKUsubreWYREIHM3huVtFXuYgzkpS63cQP1LMAtJKuuMdTq5HhdygbWWg-b99m93XayC3UesIb1Z6y_s6oPe6p0gJgDYz-Uvd3BAGktnyrVPBSEaSvTxAIeCiJDqXQHBmBJbV2hl_WFo3M-0mk73NesU1R5aiimLJxwIfNnO3l9h00HpO3Bqigb6XOYfVmAUdjqJPsOW3_X5_GlKjjpGQzmZE2URNyJb3xZfXjyhks-gAwbErBpmwMSrp6TW4PPhSztHSdIR1yjPG0fTkdyYaTcos5caryNUvgaPNiJ9iCk5ebrf3p5FYMz0U1m6QOu3CNRo_przX4-tvETsettV1awdMIBcU9R9BtN1i6kQ033owE22t0KRQJcFZ_6m40TG64WyLGKQBFYMYEze7USGqX5e282irZFjrk-9F_SpI0drQtCeciEIog02Mkl7lDik3BN7h_qdPvEP_QhVLbwq-4ScdQ2umB9rbm0ogwJmd_xTKpT3rWbAA1wSSfMCiyBAqOmc5WRv4_5_5bCsiV8jOOhKVcvf-P65morhC5_5VJWKWPHJ1xsEpTNABFxsQ-GoxUOCp-rBqcdFXGuECLxuFfHEz61gFKfPsSSvzeB34G9Ca1pc8XheZbTlFXxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=ml5GB_sLmd_N-UOMrAP1AQ0bi6A-4MhSWsjOC-q316U54MPBKUsubreWYREIHM3huVtFXuYgzkpS63cQP1LMAtJKuuMdTq5HhdygbWWg-b99m93XayC3UesIb1Z6y_s6oPe6p0gJgDYz-Uvd3BAGktnyrVPBSEaSvTxAIeCiJDqXQHBmBJbV2hl_WFo3M-0mk73NesU1R5aiimLJxwIfNnO3l9h00HpO3Bqigb6XOYfVmAUdjqJPsOW3_X5_GlKjjpGQzmZE2URNyJb3xZfXjyhks-gAwbErBpmwMSrp6TW4PPhSztHSdIR1yjPG0fTkdyYaTcos5caryNUvgaPNiJ9iCk5ebrf3p5FYMz0U1m6QOu3CNRo_przX4-tvETsettV1awdMIBcU9R9BtN1i6kQ033owE22t0KRQJcFZ_6m40TG64WyLGKQBFYMYEze7USGqX5e282irZFjrk-9F_SpI0drQtCeciEIog02Mkl7lDik3BN7h_qdPvEP_QhVLbwq-4ScdQ2umB9rbm0ogwJmd_xTKpT3rWbAA1wSSfMCiyBAqOmc5WRv4_5_5bCsiV8jOOhKVcvf-P65morhC5_5VJWKWPHJ1xsEpTNABFxsQ-GoxUOCp-rBqcdFXGuECLxuFfHEz61gFKfPsSSvzeB34G9Ca1pc8XheZbTlFXxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«توافق نفتی با روسیه خیلی مهمه؛ حجم عظیمی نفت وارد کشورمون می‌شه.
راستش رو بخواید، می‌خوام از رئیس‌جمهور پوتین تشکر کنم.
این نفت هم گازوئیله؛ همون چیزی که ما می‌خوایم. پس ازش تشکر می‌کنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/73027" target="_blank">📅 00:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73026">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=Vq8JfloKOnxnkx_MP9h3V63QjWOKQiheoYG851d_l7wcZutWatb5BGpLzQFba3BWz4ZYIR7wbXe2j28eGZa40sAU6jNh-CmE7tTwEqb6uuuqkRR-Z1ez2tii62XR56muyvdnCHq3TwubcUjO9Qn3m90X0Di4FwpqGRi_RNehi-lkTLdCNspa-13PEjBBJqJtIycUbV20bwSAJUDXdv-mWwEjApRljxS7x3VXVbWOUmEe5ttvT5ueO3UTGN7geaujqiPVIrYQe4ZhdIn0eMIsjawfPKRLh680i9BBSGZ-xlB_2BpGn7MbRU97C89L5ZJia8ZDFj4kRY13PnB1EULZ7LdTGudhQ9V8m-MG_A0UPt3oSvIyAWj3B6qCUh8XPbbTy2oMyYfEy1uj4OS9Tee8sUlaX-tIzi6mZPTZ6h88f0GkdaHY8Yh-d4bgmtOM8sBsRALo5DWGszSzn82rDuTCY9Du2g-igtGTB6TpGNnzK-fDvMtcYD9DMzBdL5t2XndSkb1mt0XIcDKvUsLQNHRPQ0UE98HYZhibteQ634MvNUfR_929Y1VpyDzde9OuAloVash_qZyjugtNHLvzCXs86daYYUsE7LHLWNfkFlatKRhw9SkRfXV3tbFufGCwewrLWxr7tVXAsIBc3dkzlNVGSj3m2ISvrx_YiiErAIUXeW8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=Vq8JfloKOnxnkx_MP9h3V63QjWOKQiheoYG851d_l7wcZutWatb5BGpLzQFba3BWz4ZYIR7wbXe2j28eGZa40sAU6jNh-CmE7tTwEqb6uuuqkRR-Z1ez2tii62XR56muyvdnCHq3TwubcUjO9Qn3m90X0Di4FwpqGRi_RNehi-lkTLdCNspa-13PEjBBJqJtIycUbV20bwSAJUDXdv-mWwEjApRljxS7x3VXVbWOUmEe5ttvT5ueO3UTGN7geaujqiPVIrYQe4ZhdIn0eMIsjawfPKRLh680i9BBSGZ-xlB_2BpGn7MbRU97C89L5ZJia8ZDFj4kRY13PnB1EULZ7LdTGudhQ9V8m-MG_A0UPt3oSvIyAWj3B6qCUh8XPbbTy2oMyYfEy1uj4OS9Tee8sUlaX-tIzi6mZPTZ6h88f0GkdaHY8Yh-d4bgmtOM8sBsRALo5DWGszSzn82rDuTCY9Du2g-igtGTB6TpGNnzK-fDvMtcYD9DMzBdL5t2XndSkb1mt0XIcDKvUsLQNHRPQ0UE98HYZhibteQ634MvNUfR_929Y1VpyDzde9OuAloVash_qZyjugtNHLvzCXs86daYYUsE7LHLWNfkFlatKRhw9SkRfXV3tbFufGCwewrLWxr7tVXAsIBc3dkzlNVGSj3m2ISvrx_YiiErAIUXeW8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در کنار مایک تایسون در کاخ سفید:
«امروز قرار نیست باهاش مبارزه کنم، اما مدت‌هاست که طرفدارشم. مدت‌هاست با هم دوستیم. هیچ‌کس مثل اون نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/73026" target="_blank">📅 00:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73025">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv09OXppd1WBO6Wk_IaAKbdCsuoGoR7nnmce_5XEZ4yPr5Ysjch8ENJ3cMLO9MaqW2NL7Tj1qQWlbjMbcSj9SicMXTMrjd2Kk0vW9ggfHmiH2zwHBixGRcugFEzV0g9gEHBO0MJ0wse88eojbM8F99GBA2hoxVUzafjkDXlcLJBs-vngROssZJzDiwKPHnU7HMsupFk_LJFQ406jx5WNYk7cFe4Shrbn9Tc-MCyAUHL9MRE6ckW27BWW8lhU0UN8WkAmyQSvpjb5w1m2FBc5pgXcg8tpI4ubc_AL199ae-uuB_BEut2REwIURHJ0ABJ1qodyZ1eJe4hPE22ZIZV_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛وزارت خزانه‌داری ایالات متحده انجام تراکنش‌های مربوط به فروش، تحویل، تخلیه و واردات سوخت دیزل با منشأ روسیه — از جمله واردات به ایالات متحده — را تا ۷ آوریل ۲۰۲۷ به‌طور موقت مجاز اعلام کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/73025" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73024">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6f11119a.mp4?token=MRWBKZGsjF8yVRPBxlUI6EgFfT7FgWhWKQ4HzqohdIpaPiELXe-CvNWAuOBmA7jIFu2VdT4HDzWISFjKHUSmaNeomtnXB8VGA721QUr3MfDsxoNDl3DkJs8zj5rDgkDUqhjORERC0PsYmvCb7pvdBSdb9nHDYsib5Qf9OSz9knJg8RZu0Hfneb-y2pg1Gj10IALGxAinZG62r0LvhANGJmIw9evfl0XqA_Oast7fW48vG9z6gBhF2gaVp_UjtcXLcOIgAX9-7NUJ7JwGW_hZ-oEDQnuqeFFQSzuyLosQxBIrEiI0jpJtqTtEYoBkhbKhUA_wTU5wXNi891DAd_mq-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6f11119a.mp4?token=MRWBKZGsjF8yVRPBxlUI6EgFfT7FgWhWKQ4HzqohdIpaPiELXe-CvNWAuOBmA7jIFu2VdT4HDzWISFjKHUSmaNeomtnXB8VGA721QUr3MfDsxoNDl3DkJs8zj5rDgkDUqhjORERC0PsYmvCb7pvdBSdb9nHDYsib5Qf9OSz9knJg8RZu0Hfneb-y2pg1Gj10IALGxAinZG62r0LvhANGJmIw9evfl0XqA_Oast7fW48vG9z6gBhF2gaVp_UjtcXLcOIgAX9-7NUJ7JwGW_hZ-oEDQnuqeFFQSzuyLosQxBIrEiI0jpJtqTtEYoBkhbKhUA_wTU5wXNi891DAd_mq-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سال ۱۹۵۴ بمب‌افکن B-57B Canberra نیروی هوایی آمریکا از آزمایش هسته‌ای Castle Bravo فیلم‌برداری کرد
این انفجار در آب‌سنگ مرجانی بیکینی در اقیانوس آرام با قدرت ۱۵ مگاتن انجام شد، حدود هزار برابر قوی‌تر از بمب اتمی هیروشیما.
قدرت انفجار موجب آلودگی رادیواکتیو گسترده در منطقه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/73024" target="_blank">📅 23:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73023">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpDI8UB4sntG0Q73IB4hSN6yxCmuwH2jn5ZGfQfXA_XMihajxXRw6StPigl2U4Ry8LmjIJZUbGqgLj4hQuqLZ25CL97M7SHXk3UP7S5r0SHJVh5_5ql9BQTtFBmmfsP5thf3AmTw8KyT5HOuO7jW6V__Bh20cz-SR70G8KMu2KZqvs3IRgsfQBrP13lkAan0DgIesI4Sr9YJ9EH_QjGEh4sl0Cc302BXnlyYaWmiQ-Fflyc_pFbUFBtBElJejpqPqScU_oL5_QUxKImtBkxR2XOwVAyd1gP9rsFq_V8pbeYDe4CWBGInk5DcKDnUn7JJspVpjtClQOl7w1vUVqCgOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
من به‌تازگی گفتگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، داشتم که طی آن توافق شد روسیه بلافاصله بیش از ۳۰۰ هزار تن سوخت دیزل برای بازار آمریکا و جهان تأمین کند؛ همچنین ۵۰۰ هزار تن دیگر در ماه نوامبر و یک میلیون تن بلافاصله پس از آن تحویل داده شود.
علاوه بر این، با توجه به وضعیت پالایشگاه‌های دیزل روسیه، این کشور در مدت‌زمانی کوتاه، ۳ میلیون تن دیگر سوخت دیزل تحویل خواهد داد. با در نظر گرفتن «کنترل کامل» ما بر تنگه هرمز و این خبر عالی درباره انرژی روسیه، قیمت دیزل برای آمریکایی‌ها و در واقع برای تمام جهان، با سرعتی بالا و به شکلی بی‌سابقه کاهش خواهد یافت!
کاهش قیمت‌ها برای آمریکایی‌ها، به‌ویژه کشاورزان، دامداران و رانندگان کامیونِ فوق‌العاده ما، بزرگ‌ترین اولویت من است. این خبری بسیار بزرگ و مهم است. همچنین باید دانست که ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/73023" target="_blank">📅 23:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73022">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=JB2OqAPGmgqjT05AoqbtD1u-lHdo2oARmb5jUNoPWkIgVsluL6glqRsayj2o6L8B1WNrpot7aYrkrDwlGV51EDweyI-XCvr-IQE-xyt5k2MwHR6B0mcMAyWjVEZtMGFbNfV6eyZDWw1I7ug0es2FmUN_TlxMrnAu_nEBhLJgvW6CUcmzrI8OdND-jpXhz29t8mxWHutMuG9-TaVB81Qb9OHsODhtk8S05tlKCWmh2wEZ6Nxve4CTHOzXiY93fNBq1qe4ok9BubqgBmvC4zLL5gDfvA491dVxjyqw7HjmiXvZI5-1WFYdq7dJHH_O1RypsvNAY-lou_3eEA4y5SiR7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=JB2OqAPGmgqjT05AoqbtD1u-lHdo2oARmb5jUNoPWkIgVsluL6glqRsayj2o6L8B1WNrpot7aYrkrDwlGV51EDweyI-XCvr-IQE-xyt5k2MwHR6B0mcMAyWjVEZtMGFbNfV6eyZDWw1I7ug0es2FmUN_TlxMrnAu_nEBhLJgvW6CUcmzrI8OdND-jpXhz29t8mxWHutMuG9-TaVB81Qb9OHsODhtk8S05tlKCWmh2wEZ6Nxve4CTHOzXiY93fNBq1qe4ok9BubqgBmvC4zLL5gDfvA491dVxjyqw7HjmiXvZI5-1WFYdq7dJHH_O1RypsvNAY-lou_3eEA4y5SiR7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن پلنگ ایرانی در جاده عسلویه:
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/73022" target="_blank">📅 22:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73021">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=U0BjsX9BJxrkXCMX-f2JHO23r6MhJR4hrN67e04kbqQ_rMZ3A-gzhQxFq1ajb5Y84N9kE0VfnFY_QDEwNIY7YzH5DNhnoHLrTIzx3DnkLMxXCx_lyybWmFJodL6AjDhnyQYC0eV3Hh0Sn_uS32IO8bU_JGvaqUvxGcguCgput2FzwcX93x5CcmLFTYm_d8CE58qb1s-jmx8qVUAY6kbK5eXjcTg0PZSHP-oxcxjDH_IKLx8ElpKkMLZeteCCmzHTAe8BTaIrkBKJ9ZLSgOonHQ5SYusrSC6Z3xyHDVJhQm0SCahgvRTj5ESBSENlO_tpwAyrVoSWEFWIIhA6f6ykgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=U0BjsX9BJxrkXCMX-f2JHO23r6MhJR4hrN67e04kbqQ_rMZ3A-gzhQxFq1ajb5Y84N9kE0VfnFY_QDEwNIY7YzH5DNhnoHLrTIzx3DnkLMxXCx_lyybWmFJodL6AjDhnyQYC0eV3Hh0Sn_uS32IO8bU_JGvaqUvxGcguCgput2FzwcX93x5CcmLFTYm_d8CE58qb1s-jmx8qVUAY6kbK5eXjcTg0PZSHP-oxcxjDH_IKLx8ElpKkMLZeteCCmzHTAe8BTaIrkBKJ9ZLSgOonHQ5SYusrSC6Z3xyHDVJhQm0SCahgvRTj5ESBSENlO_tpwAyrVoSWEFWIIhA6f6ykgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه حامی حمید رسایی، سران نظام رو تهدید کرده و این‌بار گفته‌ «کاری نکنید مهرآباد را برایتان ناامن کنیم»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/73021" target="_blank">📅 22:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73020">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=GkV8drXnAy1Q8q_ymU_zQJlWXQhB3g-nHST96XpbeXJmBvbmilbgLTL1C3ckRYveSKHObbGlmRjXbABdAluViZEQsYghqPcZJKif78wui1vA5tHHM7xHiQnlR6diVO17xkdluA4TcsGd1JlF-BkwoAcBzRijAhAkmNuduoZIT-iE30cmsKlgJSlTzHCUw8d0e05LfAQDrh_WJfo7GULZJutbm6eBjJTVaSKXuTrxL5gbPb5b0JVgYXGYrgR8D8eTc96VvxPfDG9oHFkUBBGQ9O95rGTZ_MPFCcL9adv81AvwctYYL3qxO6b0rP6Ds5Vb8-JRKWbamqB9xV6rdZ050A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=GkV8drXnAy1Q8q_ymU_zQJlWXQhB3g-nHST96XpbeXJmBvbmilbgLTL1C3ckRYveSKHObbGlmRjXbABdAluViZEQsYghqPcZJKif78wui1vA5tHHM7xHiQnlR6diVO17xkdluA4TcsGd1JlF-BkwoAcBzRijAhAkmNuduoZIT-iE30cmsKlgJSlTzHCUw8d0e05LfAQDrh_WJfo7GULZJutbm6eBjJTVaSKXuTrxL5gbPb5b0JVgYXGYrgR8D8eTc96VvxPfDG9oHFkUBBGQ9O95rGTZ_MPFCcL9adv81AvwctYYL3qxO6b0rP6Ds5Vb8-JRKWbamqB9xV6rdZ050A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناوگروه آماده آبی‌خاکی «مکین آیلند | Makin Island» نیروی دریایی آمریکا وارد پرل‌هاربر تو هاوایی شده؛
این ناوگروه بعد از یه توقف کوتاه تو هاوایی، مسیرش رو به سمت غرب ادامه میده و راهی خاورمیانه و منطقه تحت فرماندهی سنتکام میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/73020" target="_blank">📅 21:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73019">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فشار اقتصادی آمریکا علیه ایران؛ واشینگتن به‌دنبال قطع مسیرهای تجاری تهران؛
اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با شبکه نیوزمکس اعلام کرده که دولت ترامپ قصد دارد فشار اقتصادی بر ایران را به سطحی بی‌سابقه برساند. او از تشدید انزوای اقتصادی ایران و ادامه محاصره بنادر این کشور سخن گفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/73019" target="_blank">📅 21:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73018">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=JLD5BrHNPKxl5YnEPFS0wJapJK4XGLEcjW8zb5yo3wAATbP6FOWXZPMpCkRk6kbt1B9q_Z18-3xh3XjqzO1qWTGxQ_OwiL4KYXNd8RnNl92KCMHdpTS194QdnF6K4wFsMJWo9TkJokqOVlpuXue1ItvlG_kGbe_ijsyT0uUvnhUEtUgMBR50MzoHFErUHKYdMuy63jUhcXtEfJikKdce4qO8AZna9DwANzybpbd68QBfoZ_LI4OB4oIVZ6W1sVySdJkgGxwxYhbX3kbfY-JrB8ZKxyhiAqqP3duYzorr6O6-GUeV8gRfBUq4qZ08oFpbcN-XHN-T00d8cs7iVLL3-3fNv3WIDGlIRe8FAxd4mX3OYm5k5cDILyG1qQ1x1xD5e18m8AKB3eQNu07DvclhWPx7EdWGhAO1ZUP6WaCr4GuyezcFDizX8Ak8KmylfEx60k5gM7oWsSwRpLltLSU0GEBXZj-uxvqZidnlhvr_n0GwfZ6IucccITsptfYykYQGBk2C7VWWi4BFC31UN9EQlQo5maHg1p3qSmzR11pTXt209AL4mdm_jOE1X9cJmnmj93LDle3q1dQ8wvoAdk0YbF9tutSRjkuCP-74cbFJFBFfyZ4hXslKW-yDkbxbJr9pZL-jsRh7QDj0CAI58sYmUn6aRPhkCGJb2kUzmAO-IXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=JLD5BrHNPKxl5YnEPFS0wJapJK4XGLEcjW8zb5yo3wAATbP6FOWXZPMpCkRk6kbt1B9q_Z18-3xh3XjqzO1qWTGxQ_OwiL4KYXNd8RnNl92KCMHdpTS194QdnF6K4wFsMJWo9TkJokqOVlpuXue1ItvlG_kGbe_ijsyT0uUvnhUEtUgMBR50MzoHFErUHKYdMuy63jUhcXtEfJikKdce4qO8AZna9DwANzybpbd68QBfoZ_LI4OB4oIVZ6W1sVySdJkgGxwxYhbX3kbfY-JrB8ZKxyhiAqqP3duYzorr6O6-GUeV8gRfBUq4qZ08oFpbcN-XHN-T00d8cs7iVLL3-3fNv3WIDGlIRe8FAxd4mX3OYm5k5cDILyG1qQ1x1xD5e18m8AKB3eQNu07DvclhWPx7EdWGhAO1ZUP6WaCr4GuyezcFDizX8Ak8KmylfEx60k5gM7oWsSwRpLltLSU0GEBXZj-uxvqZidnlhvr_n0GwfZ6IucccITsptfYykYQGBk2C7VWWi4BFC31UN9EQlQo5maHg1p3qSmzR11pTXt209AL4mdm_jOE1X9cJmnmj93LDle3q1dQ8wvoAdk0YbF9tutSRjkuCP-74cbFJFBFfyZ4hXslKW-yDkbxbJr9pZL-jsRh7QDj0CAI58sYmUn6aRPhkCGJb2kUzmAO-IXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش چشمگیر پروازهای ترابری آمریکا در ارتباط با خاورمیانه
طی ۲۴ ساعت گذشته تا همین لحظات، تحرکات گسترده هواپیماهای ترابری آمریکا در ارتباط با خاورمیانه ادامه داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/73018" target="_blank">📅 20:26 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
