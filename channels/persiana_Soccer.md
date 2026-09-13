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
<img src="https://cdn4.telesco.pe/file/Wa72znTc0EAiX1Q8iXwNxy3w_zHlndu3ObAUQKA4MG-C1kxsL0LOidTFuojE5rkx4eoK5p-4radGtz0bUugbut2t5ZPdac8MCaaEXdcrcscvfq5g6x12FMhYrMwru0mYBSbTqCH0GRK773fCkTAlOCeeZr8eSkgYa7zPUD0JbN8fJu-PJSEemJW0YuI45VJhEI6g8774upu0m_4n_AjoMxwmF2MzDBbnATW-2h0bFMv8gljjuT_G4ndRzirxT23jrijHlsyGsxfhaBpoKRjzKyV5MYg0bHvt6yz3AECC994SLXAam39sHucohv69tNOHkzqSK0Wo5oL2u5ziTEMm7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 519K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 20:20:35</div>
<hr>

<div class="tg-post" id="msg-29689">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQjt6KEobYuw6lQQ17Y3eP9WIhcfXknBjQ-y5VxCJes5cvmv1Wz3CYKDRT_vEHPFLUKEmxArmUvQLbrbOu0tvu7WAv-lwllnBe8EPfziel9D4UmfvHNDb_zdF_YY-EHV8otnu7nEgK9W1l8YOcqc5m0FKMO0r1nZsAng5gbzunE1IGTEbcjC_jZcQFSH2iqClnoNJoVhEoZKaBH4JTYcYSYmiOgE4rqJRZGhGOyQPxjTHaCMx5fVfgTpvK13H1tZWAKyw4bajwMmfQWRdiM8DMdJEOp5nYCvl2cUy9hjVINdpdn63a1iOMxDomKm70_JH5y6TD8MQfjwkQO38WMNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
در هفته پنجم لالیگا؛ شاگردان فلیک در دیداری خارج از خانه به‌پیروزی‌مهم‌چهار بر دو مقابل لوانته رسید و باپنج‌پیروزی پیاپی در صدر جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/persiana_Soccer/29689" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29688">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB0sMx9Svj14pS459iZOLnTiKk2wbuQAzF0B1vLgVYQtRfdDs1nGLNzQl8rEygP_SnwVJK1mjDklKqtnvlVqcRAA8-Tgrzpi8zkza-dFsEfBHrFDrfmj1G1GReKWKhuNZdIb7qmzK27NmHaskkef64ZyTA-dNrYJFWexhTRWNtGbwYMmm9SyUJLe-pmN6pYmI_dzkroa0XPJdBqtbCa_2P9jOaqCnRF4J8fPqKwp6N8qsCe_STwTIBFz97V0RzQMULpO2hdAFyevUOOW79U4xsdQcPxaB5_AlvWIOpGptYmrwAEGg4K1WSfAnftgogsxZwzmBP6B2O1DzRVeTWD5Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب بارسلونا برای دیدار مقابل لوانته؛ ساعت 17:45 از شبکه پرشیانا.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/29688" target="_blank">📅 19:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29687">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wB2CZ72VmkV4o3KqI1KlNNPxlP4wbbHhwxRtiFhAa1ntbw9hfE-hwuUIZcQeKVChCEBrrMHmZIWV0RfaowrenHUR0ubUBE0D74YHs2NbeZCmx0APdbdVLFkiKaZdCRgx9NPjKi6hYjecyl1fRh0J7AJ9QsnhED5tRKkDFJHGA2l2tx2PNbmOOMMIEJOwFdhRdSPwLDhvA6AZFOugSn3nNcPV74TUnh9dvJ5yi9DdgQsP1wmQJCynA1yaBzSQrvgbm8UZ3cVW6FcrYoRC6QTHMO1UuXt8SlhE3JU7PFLONmi54OCGNcmNe1We_eMYU907iAOku4xksgE50MJPI288Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/29687" target="_blank">📅 19:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29686">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4a-hSRkT5236Cfk7MpvK38KESMfMHRn76DyIIVxWgSAltHwkM3JEPg4wZKdJC_6SIXkFF4JrZXZnnOAddWXhIaDS2BPZvu8oAghwdeqVG3nP2jHUIrguNqR9Ggl-umavrxBmve0XVGWeA4aqJMPEbi-PQFkYgCzDJ0iNQXN873eTVsNUGVG-93et1m3cnClKK90wPGlKZ8hJP4-yfsOfPSRx4aKHqh0Mi7dsEEsQM1e6wQqFD_ETBUVtBEHs-AlKSfIDtN43nI3MsYFCSbWSNZOU5x3NAPApDT8JHcWDJnKl1Q9OKjs9qL5kMdx9r4hadisA4DLtOmZbOsFmqrs8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رونمایی از کیت استقلال برای رقابت‌های آسیایی و دیدار فرداشب‌برابر السد در هفته اول لیگ نخبگان؛ این‌مسابقه راس ساعت 21:45 برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/29686" target="_blank">📅 19:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29685">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUSdllg7et3FOMNT1j3bEAjqKX3lsUptkGGoe8yrgQYtm2gt-i7RVsebRyHtAEvg_vgIHZqOuitklO4Jt_urXfA8lkMcYc2fWJAmK4AYuJpWjZH3UKGk6netmx7W6jza8LHzsmQVqav4sFt2ytXZKO2WQvFy_odSgAs0FOWZ8gpU3vV5JavSVm3y1PIzuZz7z-RlGqzZMjNNRYEIDq0GV9tB6iXrUklAD5pgECdsX-Rdax3IhD75NOWEkqc3EUsS__8zCiL2Kq9V9Z7iDiVOreBwAaUJY42d_sAu_esiqXrXYT_fu7kUsW850r_dj-1MvImI3d1Zc9SxFUoee4zKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/29685" target="_blank">📅 19:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29684">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2i89N1KaJzXE7SuR9WDd4_UG9QQGUeYfSWTeLUXiwXwI48vhU_XmCi30PMdhlkexlK6J5hzA7owTLz7wHhacF7I7vlNr0vvT9OKU84OdBpS_QeWz6T2kODlVitueT96LkDuWztQpqZe0qFjFR1Rpa9NsNGaVA8pXOBqMXHC1yNPsyO29bC_6_27eFIghxGgpk4AEhT86tmq86rw1_eqKhgMZBoAzjvYl-FN1nMLvuDXYCZxx1nmlfWVqGY0W9s_awPtFKJwyzDtqHwXNgzyQFBMzVejR3OVksGHFHi5my_ti6oS_7m3H6XzsOh6jdKp60pRUfftN0P51WBhlticvZks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2i89N1KaJzXE7SuR9WDd4_UG9QQGUeYfSWTeLUXiwXwI48vhU_XmCi30PMdhlkexlK6J5hzA7owTLz7wHhacF7I7vlNr0vvT9OKU84OdBpS_QeWz6T2kODlVitueT96LkDuWztQpqZe0qFjFR1Rpa9NsNGaVA8pXOBqMXHC1yNPsyO29bC_6_27eFIghxGgpk4AEhT86tmq86rw1_eqKhgMZBoAzjvYl-FN1nMLvuDXYCZxx1nmlfWVqGY0W9s_awPtFKJwyzDtqHwXNgzyQFBMzVejR3OVksGHFHi5my_ti6oS_7m3H6XzsOh6jdKp60pRUfftN0P51WBhlticvZks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو آنالیز دقیق عملکرد شاگردان سهراب بختیاری زاده دربازی هفته اخیر آبی‌ها مقابل پیکان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/29684" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29683">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=vBo-D4Xj0G9XSqVWo1Karh6U8B-IY_e9EZq_LRNsJ-oX9YB92lheS8WBSUST3CJpFMGjVL9Vhxjy0RyWLcTM_xFGpcx8xWrBfwfl3HlKtDDluEQRFiCnZzSXrSQ6LrCOjhyyDDFCM193zdwBVA2fqLoaJN1FxE_ymPlhmJIcq5Zp_8bKQ-lNLjT3DagueQuaunMXunMk7QR_h97GOOXLMNNuU-K6jy0Y5-ZsoIiBC68wiAeG5katpHvI59JxiKUiF7mGdPeSsoAzk9v02lQpQxSNiBdLI5HsLJ02_9XZrUQ5VXwkk4tCNbor-lsdK3hj06hT4MD3ilVpbGSWroX17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=vBo-D4Xj0G9XSqVWo1Karh6U8B-IY_e9EZq_LRNsJ-oX9YB92lheS8WBSUST3CJpFMGjVL9Vhxjy0RyWLcTM_xFGpcx8xWrBfwfl3HlKtDDluEQRFiCnZzSXrSQ6LrCOjhyyDDFCM193zdwBVA2fqLoaJN1FxE_ymPlhmJIcq5Zp_8bKQ-lNLjT3DagueQuaunMXunMk7QR_h97GOOXLMNNuU-K6jy0Y5-ZsoIiBC68wiAeG5katpHvI59JxiKUiF7mGdPeSsoAzk9v02lQpQxSNiBdLI5HsLJ02_9XZrUQ5VXwkk4tCNbor-lsdK3hj06hT4MD3ilVpbGSWroX17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته چهارم لیگ جزیزه؛ شماتیک ترکیب دو تیم منچستریونایتد
🆚
منچسترسیتی؛ 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/29683" target="_blank">📅 18:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29682">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtnfJlKORJslbYurrVMMT2sZsk0Wy8097D1C1X7lYtSmfvUzyJ-KY8Xth1SbgsxRyQfd1SqCgaQ7il-x5YlqOUrQdblZE1qxGgNkzwNCpJnOMrNNGEI7BUL1pJcXLAqE63xiTHmithknN4Ap1btxknDG2N8lgFPXm6oZLxx2CCxadcPoFtYX5qjnLjk3aLd64BG92YHQX7NcyEz8zjnQ_I0t5VCioTd0BD1Emg7fLhyTzthcxkjFiDAYnT9AIYOGSEKcBURE1f27KWH3kVKVix_cWs1ysEEHYhI6s9sCtWiW9bqGGdcyv8GldD7qb94yBLu5xl4Kth9c6lPttARuXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم
؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/29682" target="_blank">📅 18:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29680">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flAmA2d4bqVOABfKQFLYocyR2m27199gPE5Wx7RxC0AfrXiUfQKcpJTxpiNehvSnD8NM5g2j0O0A51fC8AgsPUugVJKLjt5_cpr4tiFyNVZk7dMaitv7HLuf5SrjIeENooM7chUCPQCm_kt645epWByIr9b6fSZCDLHZOCk1uKkAxdXI38el0nMhy2adkmXYB4LDcId5eoqMWdM3Q8HdShKlwekCbdPdoUO4n9kWR2k1ChE7YEBslDtk9-29Fwgski135f68HvXK_xfJ135qV0eHAYeS4UkLTTEx6y8StBjfKSDKr8sU2IBm25cu0ez-pTRkA_6HtqHtRJPHdD9-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frlAAcxteDmU96_DzqQCGFwvTRdi7aS3HJOrWjJOv9fQBHPuPR4B9EF4FMASfGw5XYDl8ykU6MWEnzjzJDjQPyB6oe6H3Zb3m1bo1TZT5r_gRjU8gu6X79eRTWMh85QEMaI6KYsia3IT2eBErHbjOHe6Bl6Zga5QXodaXl21jCZm_JZrKCNk6uzVjooqt5iPJfDs4YyhLa6PZfXpBQ-qpc9mOiXz8YCY0IYTBnL8lyPSGy9SIVH9_USGDLsNT8WgslfhH4pIBKnIol9WVTCkMpqKs8oWrVvD9RZFXkwNPSTG8WwTPjmlin5iL2AUMUPaJe35LYWnum47nRTWacWP9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
به بهانه بازی حساس امشب دربی شهر منچستر؛ نگاهی بیندازیم‌به‌افتخارات من یونایتد و من سیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/29680" target="_blank">📅 17:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29679">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE3eoS1_oql3rbYMWyqrqOoehfi23gxbEJgT-2-k6e3KM0XqJ0XQ8pTHUmJdSCczl3HO3r1kA867VWhb8Z1h-Xfikx1QmVk_L8agR7uelRdRL24UOeY1KBS8UXnvpt2s4pdox0LoE1_jOlMUMbQ6BDTrfoajBDNfmRu7qObo_OjOUZnynvxoM41oqNPtQWcLh7r3o7dWmRkHDtZ1nEW_dgPhSDe4NoJ-dkNfWZRgtsOC4tRQE-8JdmDkpAhc4J9OBB3flKZTvRcEkujWWgtAALZDjOqunDHxm2Bq4Aj_clt7jRSaooPS68WSPHd4eVKSeHPjEcYgn-Vg-9bTPbtrkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رادان: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/29679" target="_blank">📅 17:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29678">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=GQWV5zOr9ODkhh82F6H3OD_Ayowl_rQ1Svu6h6NIohspcfrXL15qfteyo51hg7zNoRcjhy0YyUYfmD8Ty25sjZUC1rtORbcta9du2bkJUFHzsRYm897sN_qqBuoppJKftZadprBvs_8Dsc3zw-x5LKGNQ4weqGP_FKGs7UPR_1jUL8JMi2uc6JRkTUtTW3BHHZV9QliJROo6zR26Y_miru4JpV5RxwhWyNcML_sA4wjUX28pcjqj6uTOUEz3SGMOLApKrHFFMnMXKDJjvGYKfxcme5qoSl5ULSTU1yjjWwA4fbh4r8fwPJ3XE_CA4QqvudPH9ikohmvpn3hhsKJQETzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=GQWV5zOr9ODkhh82F6H3OD_Ayowl_rQ1Svu6h6NIohspcfrXL15qfteyo51hg7zNoRcjhy0YyUYfmD8Ty25sjZUC1rtORbcta9du2bkJUFHzsRYm897sN_qqBuoppJKftZadprBvs_8Dsc3zw-x5LKGNQ4weqGP_FKGs7UPR_1jUL8JMi2uc6JRkTUtTW3BHHZV9QliJROo6zR26Y_miru4JpV5RxwhWyNcML_sA4wjUX28pcjqj6uTOUEz3SGMOLApKrHFFMnMXKDJjvGYKfxcme5qoSl5ULSTU1yjjWwA4fbh4r8fwPJ3XE_CA4QqvudPH9ikohmvpn3hhsKJQETzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رادان
: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/29678" target="_blank">📅 17:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29677">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=Zv4i1SKdjbaewOOqkelgkeyMyco1YouSuTcrkIdb6m6UvtGY3yat8lYb_9YIv1JVHHj-U1Ri1SG-j3z8I6qrLqnYipZYLGejOeA9NQavEiYlhQywvCVaZxKIgu5c31C5Bx-TgafIdZsvgqr2x6ctgph5yGn2mQHxRX9LKZLKvo_31u3ieDwp_JYP5Bcr0pkKFbX_atI_HH9ujMMcQM4cIX1B12CSUm6FeY0duJgnKO0br3RSx7z9X1sESHWz9iBjHnqPsrGWQF6KpswOHu3_oAqG08neCrNVyPFkF6CtfqxS6POGHreMeOfW9LKNpGjwgjGl0WZ1p2VTs8Eo3qko5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=Zv4i1SKdjbaewOOqkelgkeyMyco1YouSuTcrkIdb6m6UvtGY3yat8lYb_9YIv1JVHHj-U1Ri1SG-j3z8I6qrLqnYipZYLGejOeA9NQavEiYlhQywvCVaZxKIgu5c31C5Bx-TgafIdZsvgqr2x6ctgph5yGn2mQHxRX9LKZLKvo_31u3ieDwp_JYP5Bcr0pkKFbX_atI_HH9ujMMcQM4cIX1B12CSUm6FeY0duJgnKO0br3RSx7z9X1sESHWz9iBjHnqPsrGWQF6KpswOHu3_oAqG08neCrNVyPFkF6CtfqxS6POGHreMeOfW9LKNpGjwgjGl0WZ1p2VTs8Eo3qko5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/29677" target="_blank">📅 17:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29676">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6h9itWlcCeR9lIMxuwHVWqo51vbTKTbNevPAa-ws-qNKPBhXhBVTN_XRKs8FMlU5Getuj5pdMh4vGJKiVpemcW2BmMOueR-QJjTFNvrqx5wXzCXLaUSPw69CdURXGosm8_X3lplUltCRNQk8rqHqovLtRIQv-hyiLzM5gTuI1kLh0p8HWyxrhDN0376zxqc9XrJZHzmHF5m4WGn1CC7VHJLREpNZQ3m-mJaSeFQNwYw8kcs4IRZVqUzpNKjHPm1C98Tdj-SwNKs37b9i7Nrp7dqtc0x7PO9hgWCFZ_Xagtb4oR9tL0z3kp35C6wpcoG-FiYeON9sqYADQC5XEk3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/29676" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29675">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
برنده شدن جایزه 15 هزار دلاری یک مسابقه در امریکا توسط این دخترورزشگاه؛ یه مدت صداوسیما هم کپی همین برنامه ساخته بود که بازخورد نگرفت. هیجان مسابقه بالا بود حتما ببینید از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/29675" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29674">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhWn8FBMHtztjhnwoW5kSMOrs14i-OC_nh9ohRLWAwrtdAS7xkiSs6g20gRdsF0-TBthxCgh6Xqn4LfXY9pm3NUraoqVltXfTe1mfEj2YYrPFqMJrTmwy3ntUJrnAXQFdrs8GG-phCU7tRfWU9P9jlNu95-0tVAn9fqolwYerI8ZHZCVGnwP_--V6lPc0J8Re4X4M63dL4sUy0hKWELEw9lQaXuhHGeNRfEbsyv7a_9jffpGt89cqotsyVmJq2w_efVS5qfpvAoXO7gR2N3q0TPInvFfewjgQly_K9FThA-wpBdvJMwuA9oD-SomEprw4moYTmYjmfyLIItvkXJ5Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته چهارم سری آ ایتالیا
🇮🇹
ساسولو
🆚
یوونتوس
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/29674" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29673">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnIh-tPYn8zeGy1RXYUpwAwEBoQkVHLybsIH6pWWZ5VOZj9EsVlDuUn2_-KfzSVHN6AJ1XjsoVgFm2qfHbSjbm7O2ntAleng6EI6J6zeaSB13MD0R_WF4Zi04nkdGFm3MbK6mVN47Y6GrE3zE-vmw_MRxDKmol3VeGWD0JHlTu8-wgzqI_SAVWYb8fGtZRmKK1P42cxfbcgAYqlQ7QSBg3YCDsu1W9WnIwuZSaAw6kLG667iKrytVn7Bs-O9yM4zXkrXCAkMzk-qVhuO1vQAI2srDf3UVetPtNGhI6LG5qoV_DE9Ot_RVcYhOc47W0xfSFpeK67ZLQMhAr6qR8akYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب بارسلونا برای دیدار مقابل لوانته؛ ساعت 17:45 از شبکه پرشیانا.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/29673" target="_blank">📅 16:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29672">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0d75NvDJ3clA3UjlyA6gWkhLo1FOXMmPcurtSwtOTERFFXmWMocOsf_PsCXqrgdmZ_NjaFbAHli-d1hXOXOi5_9zbT_jjmGoCE5c6AY7RkMaNHQvug4GyqwZjNi9gWtkrIft3iXHDMKTkGspmfwrAnGKMbUrptftrwiYFHC_0xOYhF0oyclRrtcuv6l3k_dHeMUv8zz-egg6K551srZIEFKjyEJkZ17P6gkfJRltVV1H0CGL85Atxcp5sKG-ZWa95REWE6IFbKFws4tUncR7JR3VDhB_D5uI7JjeB1OANKZxy76pFSfppEcKVoKM_LJ-YdjSBlCCyg4O-dZ5b_MyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت بازی فردا استقلال مقابل السد؛ نگاهی به تقابل‌های آبی‌های پایتخت مقابل نمایندگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/29672" target="_blank">📅 16:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29671">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570942af95.mp4?token=MoYbjX8At1cX3BV45POOdZRvfb9gQv5dEDAiYI7l0BJbUdRPGNIFvkoy9Iend2p17DqAGLWtQB7SG2E3tC_QQwcPS55MmB21DEj2inIoO4jKvEEJHJ6RcX1rDih9MDOjVPpZ_uzGZBIAVE8qGvvES_KXQpYnochpkaM8Fzlk7IBOG6MUxCS-D0AL8-AtSiuB0qbVgF8x4hzZzvzIK-8bXQoqFlul3gSny-2BZRmLAbAqmAgOkgw3-KTdP3laH3Vpx2qEjP3ud5Hj9plFy7CEZeYMrL7TpLEPFWW8EX9JWzEcaXKn2spgKaP9azFLOEgaA7ApcmoRCPD6cEe3DgaJlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570942af95.mp4?token=MoYbjX8At1cX3BV45POOdZRvfb9gQv5dEDAiYI7l0BJbUdRPGNIFvkoy9Iend2p17DqAGLWtQB7SG2E3tC_QQwcPS55MmB21DEj2inIoO4jKvEEJHJ6RcX1rDih9MDOjVPpZ_uzGZBIAVE8qGvvES_KXQpYnochpkaM8Fzlk7IBOG6MUxCS-D0AL8-AtSiuB0qbVgF8x4hzZzvzIK-8bXQoqFlul3gSny-2BZRmLAbAqmAgOkgw3-KTdP3laH3Vpx2qEjP3ud5Hj9plFy7CEZeYMrL7TpLEPFWW8EX9JWzEcaXKn2spgKaP9azFLOEgaA7ApcmoRCPD6cEe3DgaJlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ گفته میشود قیمت پلی استیشن شش که درابتدای‌سال2027میلادی رونمایی خواهدشد یه چیزی بین 1400 الی 1600 هزار دلار خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/29671" target="_blank">📅 16:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29670">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rj5nrCvw74If24WdgY8P2FqiUH0nzTazRZZedD9R1zH72XP6VLIy7oONH9qwYWyh6rze4f58qpTpFnj1I0trEQP-f3821qN6mve4OmFc0bKh8a3QuCnNwDIbMy71Bbd38IcEkBZeeaNi9gxj28kmL1DlGCoo6CXcZDMoCsbQKKkjG3EA6FaYMEW9sKu72Des67Ha-0lvh2lzWieQ40hI-sWuWS4uhzuewnApsvrU_vbF-BvSoUj_wCXpK0vDXH-NwMFC2NMUaGJppxQygyPIRTZ5gvDtaS9pBhypJPuX6hGzIwSohoXGKFCuOKi4-Dfy1qL8BcfxWyVoEiu6_EC-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/29670" target="_blank">📅 15:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29669">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7GnrkmbTVmZyRyukfsC1NcO9OePbo9IhUXv8M2UsSFp5NRq46Cr917wLEXiLP9Z9hB7W82JZeBmpTILkcJLXFjcrwuPRUoAsBlnfN-WUZBARrsJno3DqWBftMFlpbVGbs-Ls5qj2F4SIqOoQAOu81hJEaHPNg7myqx8nXwMfBpg6Anb5GzESUQXi350mg5YRBKaxp3Qu6-RB2GHiVdw5lPFfAjKYAsVeo1uiSHVQ4X6GLdGRInS4YCZDc9XbYPaidbKqC2x5yrrEgCZPq_1SyaKEZrhZYzfSCk7eRO_d3ehQhopfB3f2huPu6wYq9rtZuQ4duF_AHdL6jIF72AhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های منچستر یونایتد
🆚
منچستر سیتی درلیگ‌جزیره؛ شیاطین سرخ با اختلاف برترند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/29669" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29668">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXKT2DUY36eebBDQMFrKSdDLtbRTsJJyD2VFeeG_r2ohy8M_A97J_bTfA-P66jdP1hDEoyOE3G6KNYKODd32egFOUKBrMTcTa2CUCdJmGy6NnsbmR0xng9P6lukxBnREOUo8lORqE_SOop8BSkjpOMmP934CsHb4AMQx5mJkTT6PnhwgxrLFrywhOA1mXKuPx_-HTkNhPg55yR1_XWcmiHcCVKj8LnY15X1QWXA2hi7iieCpaz_U7AJOUsT_G3aglVy2yvuxw-27UOxKEgkPacg2P4-lcQNyaw7zpkWJ9Maj076eIXFW5sX_jdfyNXQixT6ipBwuIkDwV9j8HmM-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمتراز یساعت‌تاشروع دیدار فوق‌العاده حساس دو تیم ملی والیبال ایران و ژاپن در فینال جام‌ ملت های آسیا 2027؛ نتایج تقابل‌های دو تیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/29668" target="_blank">📅 15:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29667">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=AqNP0U726F1c6tJ3juMH3yXCMYcvbzNTL0n4nOUYaNDIIi3rU2Eit-1fLxDPBgtYoMrErOLleazT2tU7w30ztzYYceWGfQVL9gLmVoKbQ0Q6OudPVGQuvIEHt26h-m5bbm9h_i89WQcvuzYv0alQ7YCUVuG7mdJ7rz7t0ZoOBFSFWgUoqlo9yt3y65agEiJ5l-D0H_LU3CPZ357doKNcZpeFTPLGRSv-dIIwyXnM7JQRijB7iKX2OLMtmkpjhdlzKPgl5mizjKipXahrJH7oXF-ZojOd9AWZvIpjKLPOiTwYndd8Qa999V8X7gunnPvMPWVk8ZiiWyAyEBIRNT_NiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=AqNP0U726F1c6tJ3juMH3yXCMYcvbzNTL0n4nOUYaNDIIi3rU2Eit-1fLxDPBgtYoMrErOLleazT2tU7w30ztzYYceWGfQVL9gLmVoKbQ0Q6OudPVGQuvIEHt26h-m5bbm9h_i89WQcvuzYv0alQ7YCUVuG7mdJ7rz7t0ZoOBFSFWgUoqlo9yt3y65agEiJ5l-D0H_LU3CPZ357doKNcZpeFTPLGRSv-dIIwyXnM7JQRijB7iKX2OLMtmkpjhdlzKPgl5mizjKipXahrJH7oXF-ZojOd9AWZvIpjKLPOiTwYndd8Qa999V8X7gunnPvMPWVk8ZiiWyAyEBIRNT_NiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز کامنت‌های‌پرشماری‌که زیر پیج السد درباره غیرقانونی‌بودن یاسر آسانی در ترکیب استقلال زدند این باشگاه کامنت‌های اکثر پست‌هاش رو بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/29667" target="_blank">📅 15:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29665">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=nBDwUtyy9EuNlegMqmLirK-J4GShBNnTN6LC9AFHjF3vyJNFAoEOTagHypWj1OXHCSQQUHfUf1dydKlBXjjY9v4t74NRQH2JfLuVxEi2WDpHJc2jqYnEuHjh0qbKnY-jJKP2EfSSx_GLJDoLEHdnkeRq6X6AKD14g68s4xENmmGXgKeOxNWgMGwSnsXtTNK0fpapWiDiUmWyd_bAwZsQhybA5I10hRcXALxrSr60iKdzngXLsHHCgFcMxvDS8MYwvHVyTFMH0_S0ORqBuMFBxZaDNrvAzx7DOjyTXoATalR5Z-0aBeWzWTdzNYWSuIS9REf7coUmeVlmyyJpMrxA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=nBDwUtyy9EuNlegMqmLirK-J4GShBNnTN6LC9AFHjF3vyJNFAoEOTagHypWj1OXHCSQQUHfUf1dydKlBXjjY9v4t74NRQH2JfLuVxEi2WDpHJc2jqYnEuHjh0qbKnY-jJKP2EfSSx_GLJDoLEHdnkeRq6X6AKD14g68s4xENmmGXgKeOxNWgMGwSnsXtTNK0fpapWiDiUmWyd_bAwZsQhybA5I10hRcXALxrSr60iKdzngXLsHHCgFcMxvDS8MYwvHVyTFMH0_S0ORqBuMFBxZaDNrvAzx7DOjyTXoATalR5Z-0aBeWzWTdzNYWSuIS9REf7coUmeVlmyyJpMrxA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو با این حرکت که میبینید داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/29665" target="_blank">📅 14:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29664">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mupLnvTcGPwuDir8228zC9bqfjEQ7HpBp6fDZjFMSRwJ7rU147H9ATvCv2vL1R-KY8zF8gZxEOWLnobaBeM0mixMbqXDwXT2G4k1XjejxpYN9U5DmixMmvkXKDGqe8cNQzfjrXpaQ5ECDgIsMFzpIbVsnV6AKSNM876K09QDd-wBjB_BRSwvrm4wMYkwP1-gSKaqb0-2wV5xji3-vaqwghb8bI3s222Ix1qrnmp5x-sFGwe5l3MGgA7RCjUz0YEz-fCNE6gVYrIDynGnO7NxgDnnLShFWgR3WvW_Ve56vy_p8r9Oc9krbi9i2njRPhmMmPyMma8AUrGdn8XhiENWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب گویا صداوسیما بهش برخورده که مسعود پزشکیان گفته بود تلویزیون دیگه ارزش نگاه کردن نداره و قراره‌که‌از فرداشب‌مجموعه جدید و جذاب امپراطور دریا هرشب‌ساعت 19:00 از شبکه تماشا پخش کنه. بعدش هم قراره جومونگ پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/29664" target="_blank">📅 14:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29663">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltXbbVS0Fp4Q8IEK0Tcubte5uoBdT-BodLu4Ov15dk5wem79YDhpzJUlaLc1psUHdx9Mf-68LDVAgyL7-KGxV3-QqTEIR-ulGt61n-mUMrn02FyZmgiS9fk2JLOeo6UM2ued4GdJoxk95ATrlzl_g1d7S5nIaf82_IR9jz0W-htWw_52lKW5ugCHLwmgYZe8F-vmJShf1uqIX0jOjPiImSSFWgB8BIUSUf7F1os0GVjI3vaIlh34ihH8xzqC4wuHSxcuRV4VzqyZm_VUURmSvd3Md3yMUrXUkFZc3eircfV5duwSl8zt_dFB4fQ4sPpvlkHwyx8f8hZ7bE9K2Xz2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برای خرید آیفون 18 پرومکس در هر کشور چند ساعت کار لازمه؟! خودتون لیست‌رو میتونید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/29663" target="_blank">📅 13:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29662">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm50EgbCqreBxax3o2HlHkVX3T99xrzZKWzeZ4cPVm64Z431lRArKfkGiiASjqOByY4H3ZoERi8RTXD9zfUuAs1anNKABxfqTVQsQKIg8SU6S7y_B1MulxJE3cYBn6Ci8GHqma3EF2fq0xApvI3sD3YFT8T3cfCrVak7F6CbVMX0aSa8GflFNUQssJaDLY2T114Tg-WUG7bkgH5S0sQZo8x7tudPwsYMGZblNc0iPA7laqpnTBRqWNEc5sivHgkHHf-tBjpR5c4z_8wlFrpl99vOyhsgHHjxqx_kR4JDUL9esLSKjxdvIGeacVKKb-ZKHL2flu0EHlRuOo-NsrlC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29662" target="_blank">📅 13:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29661">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TizcT9Yen1h6mdaOvErsq2vf91gA4MYVUpxcMXQklVX1bL6SrEm22khapTJ-dDtcJVHiWd_s0AAOFY4sVuKaGZscGHienieu4wPWN78le5hoQllzYnC832GWXhmoyXczZDdJNyRLBv1kYv3Gns_fMH0qhXWnaIwuXwnXk2VGQllnJBgPZtEQQ18gtnIY-u1J9GP-y2Vlc6L1a_0UKM0F3PIIX-lXQLhOGsUPCB98RJkGZXHw_s4KZHzLfxqX7-5wG5tx-IAX_i2nfJD1dgUwCX_o23BUAk714Q2OjlqMO2PeWpJZkGVvg81qbal2RC31droZKbQTiux-WyCzar_GkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخورد ناخواسته و عجبب و غریب علی حاجی‌ پور بایکی‌از تماشاگران ژاپنی حاضر در سالن در بازی امروز ایران با استرالیا که بعدش‌ فدراسیون والیبال بیانیه داد و از هوادار ژاپنی عذر خواهی کرد.
🇯🇵
ضمن اینکه تیم‌ملی‌والیبال ژاپن دقایقی قبل سه بر صفر کره‌جنوبی رو شکست…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29661" target="_blank">📅 13:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29660">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeWMmqHfHQcHiL2AJndUit_-kPF6bXFPStmoTw_CqG3imNgbtEaVAWduPR9Y07lvwf-jjVcLzrOW8Lpjq9O3ZcrTa4XR0BEImdWP8vU4ovdpJemzk_1VtGk7IgP2UuKTIS3UA_1kQssdO8I-Xgym4CosYiElJGSt2RezoFT_lH8GXn3ym9ipeh0_TWp5NZpPnctF2sJzEuesvy92T99QYi4p-P_55lRQcidJZtFqc-kggPWRnOi1vrJg6kGD5dhn96RP43IM1YDQ-u6VJmuCJ1mmn0CvBq3qBH1lERst2U6WIBJ8Ewu15J9flJRT4J_6WpXZUGD_yKshDLLN6CDJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29660" target="_blank">📅 13:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29659">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=NK_jffZK3JaTHBHQLQJePF-mOau9pePIxkLi0f5oVWNufQPpgEFO9YX1F-DAfPuWvjKGV4E0f_VnViUEorprHvfX0ilOL8PpWDouvJL051CLceG1daYI2S4BximN60Gb3PE3GjEk3gQ2ACZM_o9rhq4bvZGdYrm9qMGlK7Z-0i1VijLHkgLBm1D42Ov2v92zv2FMGluCpdtRgo5x54vKwSv4cZiZ6EKPbBWhkelZa9qibr7uSOgEx0kkMyOyZr6ZIlD1t-9if2GXbuIh9dmOv6Xe1MDho6z9X9rLBH2xX3lEAb0C_Xb8-SJa9ZSHAOl8n5hvEtC_xr5UhuoLT6wDBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=NK_jffZK3JaTHBHQLQJePF-mOau9pePIxkLi0f5oVWNufQPpgEFO9YX1F-DAfPuWvjKGV4E0f_VnViUEorprHvfX0ilOL8PpWDouvJL051CLceG1daYI2S4BximN60Gb3PE3GjEk3gQ2ACZM_o9rhq4bvZGdYrm9qMGlK7Z-0i1VijLHkgLBm1D42Ov2v92zv2FMGluCpdtRgo5x54vKwSv4cZiZ6EKPbBWhkelZa9qibr7uSOgEx0kkMyOyZr6ZIlD1t-9if2GXbuIh9dmOv6Xe1MDho6z9X9rLBH2xX3lEAb0C_Xb8-SJa9ZSHAOl8n5hvEtC_xr5UhuoLT6wDBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
هایلایتی‌از عملکرد درخشان عارف آقاسی مدافع 29 ساله استقلال در بازی هفته اخیر آبی‌ها با پیکان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/29659" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29658">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHLXi7UKAlQq955pLEKT1107jbIMSX2JCSGpQFU8PmIlHWL4KEM1e0Zgx8hTHssXjwK3VRaSEHcc5A3pxbLusyjNvxF91uoI8615efjaNbqiJpW7IqIsGrM1qluOne_lRNph0mgwhD2o8tUAbwnDKaY8cDnuAP1B5UUNy6E8KfYqlvT25ltzqA9X3snq7OXFU9TyMbAjja5t-tOHzGcAGjcfIloKjflnpGMAQ76Md6q29CTTFMaypZnAmeQBrvkxMQMPqlymA4fjj7aU91yYUsUT7zgV12PnFfcQ-HAkzCDSdyFg8lEOyFaLKVn5WvYhj5hdt-kzD2DwV-aGAA74tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/29658" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29657">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=rvIzBdqmnURk_WCodABMRIQcdZgFRb4belj7iui-IPw-B92J2zSQE9EDZaDscEiTtaJx98duj6um14RtSgQUQXqLFYqyUHqtEA-D1ncpx0j5chnhtQHTLOWyW13CrZEFs21aybTWqBYA49Ji1CEeQKZnh9efcnkXGvbq_-yNj3J0pnvGd3jVwNQBPBKiy7oHoWvQ59Ju5-Dvw14TPbYm5IabOUnuiF36LvFfaE2gS9_a-DOsDadmUIOgdP2N_VcV_DYqJyM_gxWlpz9Y5nS-reK22JdRCfRL8UvvUttqXw55POVE81D65Ny87CekcNXExllwQqN1jts9chIbL2sb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=rvIzBdqmnURk_WCodABMRIQcdZgFRb4belj7iui-IPw-B92J2zSQE9EDZaDscEiTtaJx98duj6um14RtSgQUQXqLFYqyUHqtEA-D1ncpx0j5chnhtQHTLOWyW13CrZEFs21aybTWqBYA49Ji1CEeQKZnh9efcnkXGvbq_-yNj3J0pnvGd3jVwNQBPBKiy7oHoWvQ59Ju5-Dvw14TPbYm5IabOUnuiF36LvFfaE2gS9_a-DOsDadmUIOgdP2N_VcV_DYqJyM_gxWlpz9Y5nS-reK22JdRCfRL8UvvUttqXw55POVE81D65Ny87CekcNXExllwQqN1jts9chIbL2sb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2018 در چنین روزی؛
ممفیس دپای ستاره هلندی لیون این سوپرگل تماشایی رو به PSG زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/29657" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29656">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAG8Kf6o5A5Wq1ewDjB6AaXdpnVfdSl-_pJdz8jOs99W8OS8ZVRbQiciaOncmHCo_LJo3r4IcWQ-cFf7w4EEI0T3YsNaWSL9_RAPWPA3cx_FTDo0EhHGysmIjf3-T4QzWiUSNNGfyAW6wHcnNYX57fKmdXQfDuZ7Z6WZtiLfcLUesMQrPovYKJ_olDB5i5fU9bD_hnpjkEkBc0ETeDf5K27nye59brFhB15DBaL5vS2_RCouFLSvLW81P-L47DMMq6KtJTs6t4qK0pvhUnOMM5mLsXCYv4sCTP0zshUd4-lzhz25sZ5GM8Q_4xsoIWdRlr3Kr4mdKeDCnIEUGgytKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
هفته چهارم لیگ انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر یونایتد
🆚
منچستر سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⏰
ساعت ۱۹:۰۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/29656" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29655">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw6dCRyN5VP8GgVzQaHO_0CRTbMeWTAqfnwHZy-uaqca35163K3YyvyhSrmZcqFlGfPjlPjiEiyI5XQ2zuSAvCR0izvnH2OtR-sAnJoHi94Qe1HyoF0vUdLpzptbGVMPIxq-jHDUGHO9_aDE5TeVtmVDBcDwylSQAC1JnsB7UJj0Qfei0D-wnOctQ4NYP2SOeiz43kCEv8-eLidv3o487HE7-Qb5--WdGPbjFV99qvXwYr6U2aBS5qgdgv-Jlq5wAIkYm5rPZ5rOrdx7W-Z6JJ2UOSugBUngmXzEr1H6dNRs3b-kjvL-m_BGhjAnmPs2kNR1xqJxrIPYlnJXBSR9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/29655" target="_blank">📅 12:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29654">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6HYrI1vxSeQkKwfkJaC2Pa3fJRgDT3CMyVUUtn82NgN-gqxlU5uw2tP-K0hBm706cnICX2zlNZK3YcAtpGf_vWQK-bgT2uSzevmg0zogLyftR-WkV8CNF4rjdJK1uB_gEzpRSLnmNW7ibc11POM3sroWBixnZg-9k_s6yWfVyxFJZdVjnP-uwQjHMr5osB7uE8EfbkESMikjggW5h0B-D9U9lTQ5rKAsODTh7i4Zm3pEB_lFmAecV-atj-lPeBfcHl-zRb94OLJ1AzgX8MvOJ0OYRxwRKjhdlxMbBrq3ZpU99LH0WUvl5HJepxV1lbW-ZfVs08nf1nh_M4Kfgl6mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/29654" target="_blank">📅 11:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29653">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFxDrCes9JP5OrK7P9ocBUNuuF_8sf9N0fHcbmo0KEXfcbAuDOG9iB9VLWOpDPpqiAL4W3VFZdmkL4AN_y1jD4sSMoI0hOW0kKsO6UiwX59FVyTY-CwGYAoWJNYiNCR5f63x0GXIPGYeWRHKv5jRpbhHpeVuBl2i-98Qlp5Kqbj7XRDUEq-qHPzNCr2GYjoSeDWbUOUNmb1-rRoNkakngSdWFejO8a24yNmVR4TV1XSyXnavZXWXu74BeVfrzWTPUSInyy_M42zLF1ZheGKCXXwVD1CRGEaLtiTkhtosPy_aNvgOvbCPk3gEhsPK0ZW055JrPQuhOvuTsfz-09a0zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
#تقویم
؛ 138 سال پیش همچین روزایی اولین فصل لیگ فوتبال انگلیسی شروع شد که به عنوان اولین لیگ فوتبال در جهان شناخته می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/29653" target="_blank">📅 11:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29652">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال در روزهای‌اخیرمذاکرات مثبتی و فشرده ای با مسعود محبی مدافع میانی22ساله خیبر خرم آباد انجام داده و قصد داره با او قراردادی بلند مدت امضا کنه و نیم فصل به جمع آبی پوشان پایتخت اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/29652" target="_blank">📅 10:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29651">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/29651" target="_blank">📅 10:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29650">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjPHgmB8mJmC4c6swpo8YZM0O0L0euMmYiSxekcgiDu160798EL4xgEDENOex_suv2bpgsD-QwhA8KnKGxU7_pUCwAZ8-jrNu-mexh5YpIaaOZjEZ8a7mrbG6xbbUuAAor9rkmbk-eIMM2hKG3VmpBpHGt13MH9YA6O7OuvzFgcqGIaolPzwQJIFBy7QLDoglJdSM9ADLY5DvhzdD8OYZw_jfmLSrE5bwXsBSKzmWAM4crpHoRyCh1NDRFbp7v8YhUIaqXvzsknL5ic7z6sQMj_cpuy4N_YNWDE3OmWfy3fb9UfCIVlG00CSKzpcelOuKVVg85pF93vFw6lfAtqSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌اسپورت:
یاسر زبیری مهاجم 21 ساله رن فرانسه‌ که‌این‌فصل‌قرضی سانتاندر بازی‌میکنه که در این 5 مسابقه پنج‌گل برای تیمش به ثمررسانده گفته رویایش پیوستن به بارسلونا درتابستان‌سال بعدست. بارسلونا از علاقه یاسرِ مراکشی به این تیم آگاه‌ست و به احتمال بسیار زیاد برای جذبش اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/29650" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29648">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
#تکمیلی؛ محمد قربانی، محمدجواد حسین نژاد و مهدی قایدی سه ستاره ملی پوش لژیونر هستن که در در حال حاضر در تیم هاشون شرایطی خوبی ندارند و باشگاه‌هاشون هم درنیم‌فصل علاقمند به فروش آن‌ها هستند. به احتمال زیاد هر سه به لیگ برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/29648" target="_blank">📅 10:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29647">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379e42f937.mp4?token=GptfafHSfCbwOQgMXvlj5zAI9ZrKJkYkL72rTa7wcpXQ0zkck3iPc4W1ZeOud70mJWET30CuwYrW9XUUk2fw91H1stOEdaFghm0_4SDgNnQjs1UOh7bJ8K77888dJ1TMO7OJ81HG4LG_xr97X14sLIo9VOmZCJGmgUfUXpiEyFcKJRlnfFAwKbuCSOLDoE9vO8SdulocHhS0IRHUv4azRQEyNCp0P6RyQ_Ru9LE4YoH7-W30UQXzqxlISw0YdeWACEeURepro6r4iiJ3tWSbeof21AZ28V4L-K76CIttfBAWluDuPKZkgSwKHjESYkp6MH-g8PhRb6yEhrWw9fPJnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379e42f937.mp4?token=GptfafHSfCbwOQgMXvlj5zAI9ZrKJkYkL72rTa7wcpXQ0zkck3iPc4W1ZeOud70mJWET30CuwYrW9XUUk2fw91H1stOEdaFghm0_4SDgNnQjs1UOh7bJ8K77888dJ1TMO7OJ81HG4LG_xr97X14sLIo9VOmZCJGmgUfUXpiEyFcKJRlnfFAwKbuCSOLDoE9vO8SdulocHhS0IRHUv4azRQEyNCp0P6RyQ_Ru9LE4YoH7-W30UQXzqxlISw0YdeWACEeURepro6r4iiJ3tWSbeof21AZ28V4L-K76CIttfBAWluDuPKZkgSwKHjESYkp6MH-g8PhRb6yEhrWw9fPJnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار آپدیت‌شده‌از عملکرد کریس رونالدو و لیونل مسی در کل دوران حرفه‌ایشون در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29647" target="_blank">📅 09:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29646">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=ZDPLvXRNa5XkUDlKntH2VD-gqwtcwURxxNo5yAE1Pqe-QTnhBq3YX-uS0aohhTPt2WfarVVIfo2bj-Xj6Rc9hs4rmSQtUQHzwojrYylXnwfW3Ts8b8Npzr_w9pv7Ozxgz1DZpXK8_yriGUeGSWhMoO5_CrPwFsyA2CVR6IAuLyayEAY4LPpQr0bLeVbc6NTt92YsAkWNEsSeE_opFVuelyHSYqFiNTFSsOR_wImxKbWtSaL0cgPgg44i1isKME124_4ImiHU59t1JzM0KUxiGB2mf3zQpLwwWsdVzKP_wrl2HfrPhxbFspBtrFpA3yqJA-o_hzeZ62u4Caah-LzfQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=ZDPLvXRNa5XkUDlKntH2VD-gqwtcwURxxNo5yAE1Pqe-QTnhBq3YX-uS0aohhTPt2WfarVVIfo2bj-Xj6Rc9hs4rmSQtUQHzwojrYylXnwfW3Ts8b8Npzr_w9pv7Ozxgz1DZpXK8_yriGUeGSWhMoO5_CrPwFsyA2CVR6IAuLyayEAY4LPpQr0bLeVbc6NTt92YsAkWNEsSeE_opFVuelyHSYqFiNTFSsOR_wImxKbWtSaL0cgPgg44i1isKME124_4ImiHU59t1JzM0KUxiGB2mf3zQpLwwWsdVzKP_wrl2HfrPhxbFspBtrFpA3yqJA-o_hzeZ62u4Caah-LzfQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29646" target="_blank">📅 09:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29645">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH2poW9tICCFx9CDNzKtk-xl3byj3kUrgJq_BFTIgkfRvWN1uTh57ViLKXiRHkFSrKw_hUhpW1qTWQWA49LlsfqA4troAWYgVIQ-fdadEfOr5dT5CPaJcH2Utz-oPlVmPYYgc2JY-0_PX3v3F_YyR_kg_1R9FInaWl_8Lq6wa7qRrDhIxjZ1u2dK2ZIaFH5j6CpR6AxMsSx1VA3bmZyqWBVc2cEQvE32GNIS6cPkMPDaeHfAlRfhwXkOKSD3O46LqsjHmlfZO1b_KbIaROEzUwJaxMpcaTsl-rPn6sj272ZSvvWiun3YXrL9FbB2BPwVmLDBpBJXkFLDsvfOq_T9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29645" target="_blank">📅 01:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29644">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔵
ستاره جدید الهلال افتضاح هفته‌قبل رو جبران کردند؛ الهلال امشب با درخشش ستاره‌های تازه وارد خود 6بر0 التعاون‌ رو شکست دادند. گابریل مارتینلی ستاره گرانقیمت و تازه‌واردآبی‌های ریاض دراین بازی موفق به کسب هتریک شد و واتکینز دیگر ستاره این تیم دو گل و یک پاس…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29644" target="_blank">📅 01:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29642">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWR1ezl5azbA0IUEepBQbb5pc3OnilQYM6c0RS03QaOg73RwPGSUt04PJ4Hd7Rl23qVHWK2CMPR8hnQkzXM55qR_3MJ5Gt2Ac1X4Gqc76_uPIGQ21KRQMPNqJq7I5lMZvrS3j3l--GhycU0jPliMiX_6l4P8c8wtgi-4tJdEzGl5iZdWeLonHdP-MhP4Ifi-XmLpcl7jmislE-LfcNOVHVIzhxweoeCBR81lbRU0MiS5mHmvNArkY-XfiXfeys60k4onq4LrUznWXq2BuSFkVM_BXcn9EdCkga9urAlq2EqGOmub9CFDOCHu1w1CCS-5sVW6CghTrmWMjxkv2oFDHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29642" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29641">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROyy_grIL_iwd-ylw80wB4_JG9pyqu911iALxzTC7a5OhXrQ_VXCOGUuiofN77zBnwIX0h22Iz5lI0IhmagbBDw5zKJWrNLWdY7dnPmKG-RNAPYr-Q7mdoSSEPJHkwMdbpslrMaHXloA64okVOSLjW_ZWzZUpm-9oz1BDpFvHbztj63zMNCvmLrM9-jBzzJIPf1hRUvdddoRztd-P-bvuTymTwFQkUmGmMxicJhCe5YU7Y5djBNMqj3EG-bNKYcX1XwKYKd_8lNAPeaYgMhrdNdXaM8uXviCxvVzbQOJkWSSnFCgHzsmMj0EBPEod74I-uBKvqZm8a2AqOIPXGhNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف همزمان لیورپول، چلسی و تاتنهام در لیگ‌جزیره تا برتری پرگل شاگردان خوزه مورینیو در شب درخشش کیلیان امباپه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29641" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29639">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXlqjYa-LDJTiXwM-hOnw7HAngOsbbRSR12skY4IPwxcPpEQsu9_oG2t5_5vC9Fh_KykI4RN8S8fYGS0173InHG_6lFTZAwPXHhEFDlGAhNjueOJe5pK-yMTQbPaF-cL7aZCrDRLJMnVG2osL-gPwcfs0dRpqC93ksZQEwLUhNfhtYZJcVVU7P4MtJqEI8BMHxjxBtySDTTOtNB85QGdp3JrADTP0v4z_IPmJAl2axxvKbJG5PrjAm5dpfiF6UEFM3lwUT2piPDRfCKaVaNPSXZAF4SyedQ7jsj2fZmjklvtjP0BpnJVsT6PX8M11WoOnyrvK2pP9MLmGTm0S5QmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
تصویری‌زیبامریم‌میرزاخانی‌ریاضی‌دان ایرانی و استاد دانشگاه‌استنفورد روی‌جلدکتاب ریاضی دانش آموزان ایتالیایی؛ روحش شاد و یادش گرامی.
🖤
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29639" target="_blank">📅 00:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29638">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=FVkF-LLLT76HVjDpXhqXHeSYWdtkJfpmGrZ0BhSkOrp22ko8foH_NLMRg1eGj0r4G1oeIkuaPQ3a4FE4qwUdffBgCzAnphOd6dS10xQRDzkt4iJA3LxSvSCspqndUZLoLtDs7nzSdxx4MXeqMa22Ct1wbxnD_Hd2z8WhLV3usZWDklY8EO6jkYeaUNXA4WeViDD9U8P5iP2WbtZJDhwv8miiqfdYP1QwuEUO601WQCdOnQcOXUJLgC3YczGypj0CZ8Ne_9b8eP8E_pGdHeGP6xNmPe2gSOZihKrjLqLU6HhLEEQnobWmXYe-U3z7jQ_OOA7xNiKEp7y-QOgWvSh35FkHecmJVEi4i18XHYcoTana78Waxey7ShEFM1ixpMbd_wxVj8jsDRmv2phuxkw94CJt57hweZqRbJjQv5wHqWq4TxQH7PjJpB7tik3etR-KHe1v898xMI_sByv8zUmKwrmA4GTZwlMcsNyCIXie5fNK-w6JiB2YgGlK_KOobLrtY2SIVNOrgoPFNLOZ4a1EZ8fXYERfzoBuIB_956NSCjPZOIs-dgyHU23vjJJ2UgbUA2r9pqKuw5pvDTW5OnyL1PmHRIrFy2UkcFcVFAy4DSBZD0HYV7aPq1M9BIBaBL1C3_apSkimAxTcwImN_ySOwa3v1bhFC2nKWV38481eq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=FVkF-LLLT76HVjDpXhqXHeSYWdtkJfpmGrZ0BhSkOrp22ko8foH_NLMRg1eGj0r4G1oeIkuaPQ3a4FE4qwUdffBgCzAnphOd6dS10xQRDzkt4iJA3LxSvSCspqndUZLoLtDs7nzSdxx4MXeqMa22Ct1wbxnD_Hd2z8WhLV3usZWDklY8EO6jkYeaUNXA4WeViDD9U8P5iP2WbtZJDhwv8miiqfdYP1QwuEUO601WQCdOnQcOXUJLgC3YczGypj0CZ8Ne_9b8eP8E_pGdHeGP6xNmPe2gSOZihKrjLqLU6HhLEEQnobWmXYe-U3z7jQ_OOA7xNiKEp7y-QOgWvSh35FkHecmJVEi4i18XHYcoTana78Waxey7ShEFM1ixpMbd_wxVj8jsDRmv2phuxkw94CJt57hweZqRbJjQv5wHqWq4TxQH7PjJpB7tik3etR-KHe1v898xMI_sByv8zUmKwrmA4GTZwlMcsNyCIXie5fNK-w6JiB2YgGlK_KOobLrtY2SIVNOrgoPFNLOZ4a1EZ8fXYERfzoBuIB_956NSCjPZOIs-dgyHU23vjJJ2UgbUA2r9pqKuw5pvDTW5OnyL1PmHRIrFy2UkcFcVFAy4DSBZD0HYV7aPq1M9BIBaBL1C3_apSkimAxTcwImN_ySOwa3v1bhFC2nKWV38481eq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29638" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29637">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCbC6zrPypdEKNX3C1-4GAAd74026KKn8LY90zy-djg7A8etyY8K0a5zBqwdNIZ6BqlCJcSpwT6n5X-1z4IizQp65q4ZX-VKMrrFnoTXbRR1-Id6_2c4D4lAqaMdPuqJAFohrI2a-aGf5n3pGGSqz7pmH1nDiwizYP3jOZ_KS28OfRVRTQyZ66Wh7lWGGcq1D_UDDdpi25-WvalBQdfO2jps0F3uxBEGfPMAQYIY3gYAcEb_ufE1hDe6UYnx-LHX7ssZT6XRw4T9eRbIfawpwO5gKw6Uobl266ltLXz2Qh_r-6Nahk-6Uk4xr3vs0UAYwlhdaJcmN4T1jblOi0liDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29637" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29636">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twsqnHv3SUH62JqMlRn26Nb16oG98Qe0XBPjtbYJydTS5IqdRtr2uILTbbogdMS64WhpQFVytx-SmeGO7i7IZ6RPWtI3nAIKHHrX0879WYhEUTys5tBg_uxnX6pT4v2M6tYACTgcCynplIgB4x58rStFysvrGrNbjmXFlrIOhlpknebYcHPa8IkFtmQwik6zZUY_WwjX92pxDlToc8NqLSkziojdAlXWzIU8J80Rzsgik1nRjJbgzRzoXzruMKGTNXLK2R_4jjJcdUSYTE5TxH_KSqOx7rCrwzw8nHR6E_To-0GTaqgcIXhAEogjBnPKtHK0hNVxmIgmL37xucUQkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
حضورپارتنر وینیسیوس‌جونیور در ورزشگاه سانتیاگو برنابئو در بازی امشب رئال مادرید مقابل رایووایکانو؛ نیمه اول رئال سه هیچ بازی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29636" target="_blank">📅 00:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29635">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYPMd90sjHEBXeUaZp3otaOL3R5W4-8bK-CTnhwXhhW1Esf1Xw8cS_JcRAYmkbVFNvjnteK0c0O_7puHyt42yVnYPXw6hwXg8cQgYa76VvPaGl4eNJvSGJJzEws3d7n4r1ogECd1aJGPNMDxmOrpymrHt_kL4TJyNGLJW08G6boXhBGYvVU0pmHx6mJFaGBYMO2DaarsMuXB-dFhU3SP_lHoX0YvBqF3rQdg9E8NPn4D4qNMAL0OhHNy73NW5U0Aiyeu-UcmPdirAbntVWXSylGVUMQT5BRLhSXu0K0mEbr8_7M0Z6TTxvoMWRmuvQW00pOUi_qbUw0OnjH8atpD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تایید شد؛ بااعلام‌رسمی باشگاه استقلال و با موافقت سهراب بختیتاری زاده صالح حردانی مدافع راست‌آبی‌ها به‌تمرینات‌ این‌تیم برگشت و در بازی روز دوشنبه با السد در لیست آبی‌‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29635" target="_blank">📅 00:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29633">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJlPOgBJWx87d_v9x0OoE2zeFPMBP5SRXRJ3qSWQe-jqkSEDqOmhtzK9TgKvHkqDgi5zcnLqFZtxXa6VBh9OHcfBSYm1YXO6AQsxyZCDTfl2porxFqOvK6mCLF4nDDwKGT105KVvRIDSPg0DfufbldRl-6kc9DdChHLRyD_JIWjJpdUuh_1OdjTaLtGtCrS7KcPs5iX-hXe91puicQIY-WubywLnKXeZ9F_ogzWo2aUrFl6rFLTP_V6UK-Bmy9Qj6cWpecDVcLbPnxCbG7ZHcMfuj87MUMxH965LxjTs-FYV-GMH9XC-IgAUuxsqiWcMWhUPCECju5DXO31rHFBDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛قیمت‌پلی‌استیشن 5 پرو دربازار به 310 میلیون تومان رسید. بهمن ماه 45 میلیون تومان بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29633" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29632">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8_gMG59utH6SrN5hS9ZGPSF9-182Zy96f3g5fOBOcV7w1yZ8b7Vy08H6Vjd_jrAg0KP2dTvW2STNPfl_85iR_dV_qqjakvYHgIN9tn0zzPv1oh5ecFJlpwXQmJzEDQAZ65sv3Il_NZ6X4cZWg5OM8_CRcFfeg_8_twfVDKhGppAUFNyFGTN8A76tV9hQ2Yp2XPTDNttK41w5DDKgtQ5U-Q_BVdoAyRmQZdGH3hPQ0HfktB5UGPW6YJrl3GfRLMtL_KYECMGopVnN4o1qAqQp4o1H-1SlmSTDQKHEM-_6Xz6qUPEDPbzYKkQHbE1-IbT6JFOeqR6o55cGlaTlNlQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بااعلام فابریزیو رومانو؛ مارسلو بروزویچ ستاره کروات سابق النصر با عقدقراردادی دو ساله به ارزش 12 میلیون‌یورو دستمزدخالص به السد قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29632" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29631">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5XY0kqkKbeLmEPoHBa4McxRiQRfa94c0HFLRPLDsyQRo7xEbGl2lHhq3lojQOxsoPlk5cTbOjmeKHn5TLikFSFG3FwIp_OMweD2oyonLrp6r7btoHGsBAlxlQMVxT4w46VLQGGLo_9-IROrlKvXjIqCypSXuJa_igti42Z8u-eahaZhqdgQEodYIg8OGeaeLeo5p1f6QyLClhRq-k4ZmdsgSYVV9-lVlWFVUrvhzZj0aSvSrDvirUrb4amGlpaOJ_UxtTTLAuP4vehp_xBWAmU0eoWFbL_f5lBt5npE0aNmBYCeNRR-7KKFEO881ex9J_1mQwS8XpdoVC_WOb-8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زگیل و تبخال تناسلی درمان شد
‼️
ویروس‌خطرناک‌‌که اگر درمان نشه تا آخر عمر داخل بدن ماندگاره و عوارضی مثل سرطان ایجاد میکنه این ویروس
❌
HPV یا زگیل نامیده شده.
⭕
درمان کامل زگیل و تبخال تناسلی :
1️⃣
زگیل تناسلی
2️⃣
تبخال تناسلی
☑️
زیر نظر سازمان غذا و دارو
☑️
بیش از صدها رضایت درمان و آزمایش منفی
⚕️ آیدی  :
🆔
@hpv_help7
⚕️ لینک کانال کلینیک
🩺
@hpv_hsv_clinic
📞
09212046421</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29631" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29630">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOe7GecJu46yKd0Uofh8kvtUuDRy7VerEZHYLdUq2yrbyYqbxJlqNnkcx2oRyn5aP_MFkk1OaGQ1095QXSnrEEDN2eDH8nbbd_HCjCQuT1CXoELyViPFx1eD1h8QsimZKnZ13zsiYkKXu_KOvF_-89P1y_4qkFEmLjMJHP3Ae-mtkH5T53MTbQXz3_iEPSY_km6WxUTXRziXvby3YEqXYYgT-feZD1ifl7UWAc9QcRdAJJi9uI5x6pQUfkKW9Js4giI_JyhKGff4xpxO7GqOu9KczmfqJ-z-ac4mzVlcdi8KQtBS4CSMYAeykFAG_ddtWfNEDBLYHkvFEiKqWgqsyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29630" target="_blank">📅 23:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29629">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC959Taa003IPFySKAz8BQRl0W3BZvvjrR_9R_-Oj0hBBtfTT9l8wp6MeyotBZBxcUzPCjUxM8B3OfMmP4Dz0IWnx_aVxQqYRtnU_F8gMqFCC0McW_e9qbSbV5QV2pGOg7s3fkVR1o7y4JDtMBwy-YweZ_Psoxv82T073sJW50ig7XhUy4q2h1tJWKRNX4kutgU9F9g3RanmUDB49ztSHcGVj3JlO5DvZs9CnKGDdvv_y6uNyWB102E8F7Xgvmu8oWCmGpGDGoD-XnLrALxArsgPnIGJcetEtLAO7u5XN8gSmj1KaVKyBvAVMALUJzU5N0CuFICALtHEVxc66nsv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌جدیدترین‌شنیده‌های پرشیانا؛ باشگاه‌پرسپولیس بامدیریت‌باشگاه فولاد برسر انتقال ابوالفضل‌رزاق‌پور به‌جمع شاگردان مهدی‌تارتار در نیم فصل به توافق رسیده‌اند و سرخ‌ها با پرداخت 150 میلیارد تومان رضایت نامه این بازیکن رو میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29629" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29628">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9rb78cFoVRW9hMQsaY-q_CkzYDUNW9bbEs56NEBpn0Ci-2xLAYLajsYY-94w_Un16Hngq8cSb-JxitHWfju_HOiV-1cT0i-5_ZtAW0dEcAPKXWyWsouVpVqkO8a576-pGrHQOOHOTHeZhOutPsw5BLQ1YpeC5wcnrvT6P29wlTeJP7vAXAhTQ31R8thAO2LlvyBYv9JWJPlFHoc9NRdXhwbHLPBR0TLxC23h7AFXNdFYin9oTmrPTetHLyUYFnqMV15eCKJgtzuScidKxWOGi2D5gNHG7lTZB0WPYqoda0pBWcfnSwqTgRjcHU6Kk9_TCTaI4Nbb0z2EYP2e2TNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌جدیدی‌ازبهترین‌برنامه‌های‌هوش مصنوعی برای تولیدمحتوای خفن در اینستاگرام؛ این پست رو یجایی ذخیره کنید به‌کارتون‌میاد و برای دوستانتون هم بفرستید که اونا هم ازش استفاده کنند. عالیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/29628" target="_blank">📅 22:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29627">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AP_TAMXgEpaWaSgX5_FJv8qoXoGvoYHsTRTCLkDwJyzLW_qK_HQ-mSLXiHbaA39eHlmz1e2pkIpAS0pipPXj_gLEwdvdacYxIt3ffUZtgN97KF0rMn-w3vlIkwIuO7B6jXOqnfIc6rr6TX8rLFN3tz3NQ2p6SJkBZCDRmig9zySwjb9XNimuTDrJOw0zYUysNi1DRoAZshHNl4hDtdwCG2kuprCwTHDd1FMgvZ5r88o2XLli8QCjIkIixTzSev3CTq1OcT19qiAn2gQ6MrSNFnajaoEVEx9u16c2UK7UABWakmvsph6DUmMLHr2_sut3R_9_mGVCZhInabgXR9UAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخبار دریافتی پرشیانا؛ باشگاه پرسپولیس بزودی با پرداخت 250 هزار دلار به دنیل گرا مدافع راست 33 ساله این تیم توافقی قراردادش رو فسخ خواهد کرد و گرا از جمع سرخپوشان جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/29627" target="_blank">📅 22:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29626">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZpOdX51eVwFa5pIyZEQ5zNPVqqONHPil7qcRzXL7bENx4r7YE4cXADlrOIPUjjy5HZrhaXbGix0iijkX89FgOZda8JJYy5Qw0w84PVz_Fy5kTGBTMPdrgcZ-Td1nhi1P_9rVqc5tusDMcQsM9Ozw1ZyKPvW4ZxKj9rU2bVV4kaWyLg_lIrQO8uKDlYc9ogp1GmoTjKiZlh8S5dbtsghL2oqGfYeIAKAZzMCU4sXGWHgr6Ygm9lEsw282Kv-antcVb3CXRfCtpkCLObUzmmooNXcCUt6PxQAOkI_SVByhSbrRgaJaOLhBvXaS6Fx2ErnUHvCWzmjuEnnpbzUApMUkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/29626" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29625">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=rHxw0s7Ygt1qOgQ3eop3h03C9iBELRxlnhP585VIP9DN4agOZdL2UqbqzJbGvIdjjkumERkTFjwJxu-MXv4z_KqBT4kQRkFRi5_ad6Ems_jk0CeGBNZGD1ZcOVo11ZyE6cELyshUVwmVfa7smVjWJ2qh4-TtuZ6jQ4QXaqqfjFsl4u4dIRdjkWGbhegedVlnavcW3IgkFf9AU9b0UPSJ6aj6DfwIYU3mG_66jEp9nSDe-i5VpEhQjf1-Kc_rUwJZ4nFYWXFFIHqPaOXP3SftoG_XM2Af85VCFnUx9DMH4JuUIq7Qb6veu9M106eXscO0bdjGI0BZDiE2ViDgI_wWvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=rHxw0s7Ygt1qOgQ3eop3h03C9iBELRxlnhP585VIP9DN4agOZdL2UqbqzJbGvIdjjkumERkTFjwJxu-MXv4z_KqBT4kQRkFRi5_ad6Ems_jk0CeGBNZGD1ZcOVo11ZyE6cELyshUVwmVfa7smVjWJ2qh4-TtuZ6jQ4QXaqqfjFsl4u4dIRdjkWGbhegedVlnavcW3IgkFf9AU9b0UPSJ6aj6DfwIYU3mG_66jEp9nSDe-i5VpEhQjf1-Kc_rUwJZ4nFYWXFFIHqPaOXP3SftoG_XM2Af85VCFnUx9DMH4JuUIq7Qb6veu9M106eXscO0bdjGI0BZDiE2ViDgI_wWvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار! شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/persiana_Soccer/29625" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29624">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKn08gmiGcQ6LEN1bIgIkBt60YVa4j-qEIUkceWJcgq6nN8r53RsYbT4Q34lrRQ3SfG1frV3RcRknZGCMEo_GlkVIh3snj671a_z2tvM5e0jdPGy_wnuJHeJKaW74oeB_mXnK1bUyTnRKibxnVnICAEjnFiRKVrrauIsF23oykWWtQTVHaExuYLXaIuGUn6SvzlB-R3hfY13SlidaoA9afl8cUkQciarZmsdVYc7tCl-FrfMSx3D0n1iEkMG68pvjA1BwosXknMIFbbMzoJsPyBlVkPXlDaEQH8cNidWUiTXwAfQAefHbTrxKS41BYvD--FFw8dwoGTtAyxIenFuyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛
بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد قرارداد با این ستاره 29 ساله تیم‌ملی‌عراقه و درصورت تاییدیه‌مهدی‌تارتار این هافبک تهاجمی خلاق به پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/persiana_Soccer/29624" target="_blank">📅 21:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29623">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRyOx2-SG3aCMBdt9mAr-9y0fud04g7cZgSJJgoU-NvjIdPESviSyXs47-WEhCaNau_dxnbhQnlTTKKQ-S9arEfNxsUDGHBGlOzrfPBwCu_iHIxqovBEMupSjDkCoS1KAas0eDX51FYx6uuNk-TgddnF-7rsWSP8wsT6B2t5gucxc-LfIXyTXCdejiLpEHUUHVcgYfl9QQK-muZC7s8XPKqaWVtntjsipMzMfGYOOXRwB3m62ZHklGpuznhkfXnhAK5cawH8JnarZLfHsc_3NqYIQk_3G3beEdEQ4OiSsCg-Jc_bEcZt4WCIXU6xRKuqb-XCbf7hAyDTSNsQHKEh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گواردیولاسرمربی‌سابق‌منچسترسیتی:
برای تموم تیم‌ ها در چمپیونزلیگ برنامه داشتم اما هرگز ندونستم چطور رئال رو مدیریت و کنترل کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/persiana_Soccer/29623" target="_blank">📅 21:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29621">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN6Q2Blf71GsmBppALg2AnLvSquoeMlPr1ms7maCIbRU6XaUqncw5CXUgXQxe4rm2onb92cZqASJDjcj8IJVsqrupR8XQLWSeSgV9JvyjEC787UUXtWkj-QVqLU4Ge3x0qjCHrWuY7-Vh0lwZOUHhzPkNouTi_RizcCOVN3MDxUQyXUQBPF_P1FfRJHjDlGcbdXMf9KWpL7ad6NG186Bb1fQGDmn7XOKJIc7da7Et5qXIX_z91zUw0G7Szm10j_qym-wOljvWlrOVegKXLy6Z5evJZTmN5MSJ2ZhmPmA6SNz5RJMHRmACUZUU9UkpJeab90j3AC40vKaLWCwXxcjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌امروز انواع پلی‌استیشن 5 با دلار امروز که حدود 223هزارتومان‌بود؛همین کنسول یه هفته پیش 190 200 میلیون تومان بود! قیمت‌ها عالیه واقعا:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/29621" target="_blank">📅 21:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29620">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVUhuLZkPnnsNhSSP2_DyqHn2s3lQ0DnjoII46c0IBTaMiEAcwHloYnKQYoymGkixXO8R-ijD5njW_58f44yC47Jo4o3WfCisWmOmexbQoiPaj_qLSjf4dj5XV_oUPwGTswr44aaA8ZyYOT1vg9PmuVYvAXvh_8fl1AnYWboj_gnFIUglR1xLTlHDe_juxLI7Goe_-29h3fRxPQ91p_HNE2_xpnvJpZ9B3A8Q6tXnJ63NdkjQiWQpMareCxjR9FSFPTgwVPEjBNREHB6IT6IGgOC018z8IpmsHpExFLt4lLw6pCCyJ0ceBsnkO0CCeF20zLL71wKMCn4O6iX5WzM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29620" target="_blank">📅 21:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29619">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_v4kJJWNkBlH16ZMGEfFpr6bCO1ko-nkpHFqIX5Er3cSLkKtoqzZv9LBwTGJSa-IvwdOo-tHLYf2hJwAF_GNVynG6qEpH_1b-NxKsSueSeUX2w6WkUWbJqHiWMwRhrH8f_BRelC2Uj81YiaeYiaOPaVhVPwSIAeEnaD5oyBeKsxwv6BxitImjN3r7Fz69-i9FvR-Rd1eMRlhk9Z67RHB4j5HIaejW8tIKeK00CA3JouXoTkPoViL3A7lerBUn__q21PTc30UxtggAWSBVOP3zv8MHJT-jUE_C-KeXQj72chWJF4ulq_QeNGrifVVwspvLmkajGEtSnJR-Hihqsw1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛ الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29619" target="_blank">📅 21:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29617">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSYRSTjVSoCSXJ_i23EDuwMPj_PDwpCYr6yr4JA7sWv-uQdRMM-OMDjwtv_iQQB1OgCw-xjzLhADgSB4s_v7rhS8MCfu7k5_YLfOH9VIZaEt3XLhiZsoHWRHbNLtbURiL4P4a8tqbcJvxQBv0FZpDCU72tLmiedhB3l7jBo_73hlpCJk1m9Vcwv1HRiPQYoLUdgyMBTIUBs776FHd4epkUCXXCkyad8jtD8YPiPSe4RQVWUfP3HFd1Z6FLKlwJ77zS2_u5FpyIPcyP7KLiyhp0gnog8KftvYnR7x7Dy1xOm7ORmOEdW9vFfYOXp9GBRazvwSMxandvBPV2Ud2kbGIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29617" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29616">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc4f99_wROiDird1Qcd_eyHuDnih-ldnUrVlAwfVIWVpi3yKcrkXFVPezXCVDm2loIsyVNuRi1wmj6K7mwHBuPqZFHQL2Es2C8zIG1BibkTC4252dyM0ZnhVJXxMnSKYxzYRyJHj2TiaA_30vZVUSR0BmBEKLZU-7m1FW-eJt0urnAjBSYCHS5ESDhici4uTWDppVKow0FNcNAyPLKtARza3MpkKYr4TrtypqcUzEnAcQQ_3hI5hveZNEEIPyqDXgpoNHiTTLNlIEX-rSrUKPnzBkc5sz7mnf6hOeRn16r2fMldAqEwnTKzT2srWm_9yUV61e6dfWiV5ovG9MGDA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29616" target="_blank">📅 20:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29615">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=la7E0TksVvsb068pPGbuFuOcZi4RU_tIKUpmU7ACSMKsxH33gMkCaoXItEAfvtze_agoNlSsQEJiQhUi9msxQPS4u18injwHKyjdBquKpySOHBmAhNdrQrfJAjOAr9kYPvi9Yb2Q9KbuQ-hvL0dofLTEchV_Eq2GdqngI4vd9e2QE20OR4vrUC2AsiN1qIHbEb38bXRKPZ0UEDOBnAH4OBkIZK4G0wMcCbEJV5TOfE2yLjVLSKWmksjsEAIyer6qhzMYLVFu6vGSlUppxDk3F5rLgx7xo9cINIj7KozN_1DOasbf6X8GF2C2wBZv3seh03kaxU9UEhNrWnHM7IvFKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=la7E0TksVvsb068pPGbuFuOcZi4RU_tIKUpmU7ACSMKsxH33gMkCaoXItEAfvtze_agoNlSsQEJiQhUi9msxQPS4u18injwHKyjdBquKpySOHBmAhNdrQrfJAjOAr9kYPvi9Yb2Q9KbuQ-hvL0dofLTEchV_Eq2GdqngI4vd9e2QE20OR4vrUC2AsiN1qIHbEb38bXRKPZ0UEDOBnAH4OBkIZK4G0wMcCbEJV5TOfE2yLjVLSKWmksjsEAIyer6qhzMYLVFu6vGSlUppxDk3F5rLgx7xo9cINIj7KozN_1DOasbf6X8GF2C2wBZv3seh03kaxU9UEhNrWnHM7IvFKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گردوخاک اللهیار دراروپا؛ گلزنی دوباره اللهیار صیادمنش ستاره 24 ساله لخ پوزنان در بازی امشب.  عملکرد فوق‌العاده صیادمنش در فصل جدید برای لخ پوزنان لهستان: 6 مسابقه، 5 گل زده، 2 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29615" target="_blank">📅 20:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29613">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OrQs7h7oh_4SEY86OkKTEC4nTuGgoLPxKLXNYNnhev0xQX7MnaJ11l2fqghXnEl01_xiy9a2y4S8IibFqnVsTJidDKQcYAJajP6cW26vzzl2v6NdpuWBf7j6gvvlusBkTHydwOu9nQPrKXKCxuJZVSzTGEyQheH5f58Pjwyrt3eCU8Zb1rDm_-toZeOmzR8-oWJSouX1834oulSiYJ5EdGGjPUBwZeaWFzLVXAW1n6XNgPFONF5whinLaL7vV2lW4MCnxFbo_9-61M1UWXBPgQrraxRt5oGbYl0mwLTQ4oPUm0cL6nD97n4P3CsclIbH7ANCy0uwZdWaALK6ra-vqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXez8c7JxDjRtgwbtt_qcYU9JRfX0kE8yjGak1gMuoUlhEmrup0GbOqedGwadHxjBAyimBxFaEfjl77alzfIXBEuVUsfsa1ZsQLMB2vLeBch5Js7yenOaVQjsFUfnxLed-475Fr4-K6vZGFo8Vll1Rn7fqkrHhe0bAagXnZZvBmCFMffbhzt2gsRiEu_13FJTBAeOvlw8V2rN8MviRELCVhhg1-InOc8fuDtxJ271chtZfF8vFc0F0iKUQ5w6GvJ1SZHMF9XMf219NNPoj-lL5wpmbgbutBK6TwHMZtBI9RwoWogFkr-sB-_4NCKEO45CJaHUj7G4cco2zqC2doTGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29613" target="_blank">📅 19:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29612">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
سرگئی‌جاکیروویچ بوسنیایی رویادتونه‌که 3 سال پیش دریکقدمی‌عقدقرارداد بااستقلال قرار گرفته بود این‌فصل سرمربی هال‌سیتی شد و این ماه نیز بعنوان بهترین سرمربی ماه لیگ برتر انگلیس انتخاب شد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد هال سیتی در فصل جدید: سه مسابقه، دو پیروزی، 1 مساوی،…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29612" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29611">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUUeqL7gmWXx8Sa2pHSw3kZA_XvLugsLBNNn8TCra7YEPEqmXeubl09AnnLrffmhw66kBxliTJgpQMTh2QdTuzJJOqU1gDKeCG29gCoSAG9Z81yZ5vAv_UkEflr_UpoF1EbeLmU4h2pz0bNv6AHmO9xXxJLLlpX79WwdPp5xOeqNuTx9_uhNIE-lNujx54C0Spy4nHmeL_l4FmkjGCUI5E2rhbltI24nE7vSSCMcgDL-UNd1hb-u-7veYkMLF6gTLM9rrtJYnrWCQ2fZVhzgKSpDycX77YRiXqxgvfd8Q3t3qfMbg4awGN-dsWCY4ntZxb94rdQu_Kogvb3LaHw86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرصت سوزی برگ ریزون لوئیس واسکز مهاجم بیرمنگام در بازی امروز این تیم در چمپیونشیب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29611" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29609">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbE94bVMQRCJynE1qt3xpr49YD1_2C_YshxmtPrsOjFJ2fI2Ow89gO5gFVPOube9nncMFBSH4F-EvDiu-dw1lXMlrqytI5Nmc7eOm4Tkgkh8vsg_nf8rXhkkqDdAN2gLuvaGh7ZuZmWe7E2s_oIm83J9T8pLJ26fvsoEKKWmsmF3MO01ZP0APCYwD6tq8lYqXOmvHwlYPUQCzLhxVvHRdRuVpLxaYuk2kk2-JDxloUycpmrsZ_h40Vv8bpN_TAKKRyvXBFuf0xMXDSmX_Cyw60JmN5YD206QRa6DiRv50iJMlHiQRvJUi0ZvEcg1fCP2Q-plUrqw9mdroLLSGyiXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نگاهی به آمار خیره کننده مهدی طارمی ستاره 34 ساله الوصل امارات در دوران حضور در پورتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29609" target="_blank">📅 18:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29608">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfeZBLHje1lAZUVebQEA2S0Ql5WlG1Uzd7O-HdzR6Tz35p_CT5t5lsGNBzz8TAUTwn6MERnZZ1iQ4dt5pNMLRUsfxFIWljkti-wNKMv2AyHrzw3yW1yNw5jtStmsHFx8hti5HnOw9sueTivjJwfId_yxpc1tShUadlCMJ65NbrklJ6XWMKZbi8cWmOMsqzISTkjhsphBUBo-FVQjOfrwfrsleLU15u427F4bR8s6lR4nXqv2ra5AwqamY0wRpNTQWyxloy_HJP-bnKsm2VkUBAWV44Fg_cylUyjH2EbShGbaibwH2TN4J22YpZnu68ioX_TSewNa0lHYjYIyAtl0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29608" target="_blank">📅 18:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29607">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇦🇷
ویدیویی‌فوق‌العاده‌ازکاشته‌های لیونل مسی فوق ستاره سابق بارسلونا و تیم آرزانتین درمستطیل سبز
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29607" target="_blank">📅 17:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29606">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCv2wMukeFPJ2ngdjKJAnh2Mol7NFPkrCTm_qInka9Ieec-j9ytBhLxrP1iW_H68MgbClTpb7T60hf1B9_dpjrKD0rRIn7sjOqmmQy1hXM53uLt70w4CB3zXECgH8c2CeMRWjr87KlUYFLB1H0SEBELd_2MZeV30OU0CpbHG6HP9IGQv84iHjlIr35GU4st-o02gHYJOG8108ci9rXWFngr4yU6Qt7w0i357bPyy1ACHOB7BO2cayLGgiYqDFThTTm9TcR9QzrEQIEBP0lT--leZgLuqxuS_Vk3qOtOR4d9LHbZaVsYrl-wf2qHwsVMotzp71IAWSJ8qz_OdFffXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29606" target="_blank">📅 17:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29605">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vp_1ynnVzc06Fokq7_nLADp0PBhm4qLOq4CnaisyJn4e688Sabs6sz8d781FJtjExv2X_fCowH89N7LaJUdMzk60BlkV9U9BIHRls5kD3LKGM3pI-ky6xKL82HId0B_5fXU9mAI3X4y3PwfLaQcWrj9ZXa12DzeNx4xDJOqtvI4aRcXxz68pDnK9pJBMu4KcN9a8zt-3Qfngut6XvAGKrctEhtzV-Mkqhwh3CA3IsIdGKAdcpn3OrUalV1HvEx1temvYhnlbdHqLwEMzBrMLzOf8eeJBto8JwJnSdlgBrHfyhJFFkyEH16yXaE5YzaHQoa5dPLDj8_LDWAWf3I2b0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
برگاتون بریزه؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مدیران باشگاه سپاهان امروز صبح به‌مدیریت تراکتور گفته برای صادرکردن رضایت نامه آرش رضاوند علاوه‌بر تومیسلاو اشترکالی 50 میلیارد تومان هم بایدپرداخت‌کنند تا رضاوند تراکتوری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29605" target="_blank">📅 17:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29604">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H70Krob8UiH34NdpWVDwq7g3YlUWvak72tjLT1L1dge98l8XNIf4qJ364WnmTJo-gzE4TCpoU59qwMNh44DYUY6NspuLfeU6yDlSxqDd5Wrg4ANpgnBaX5OyDyUfVpwjug1_w0zVAuFbsOMEafOANz8vko6Rsr6MiZSxyeWwF_ny1OMQOJsK-d-oFtZexsrSudgBAYKyOVMPPLEnzmx-Z3vZ893tl4VS5AXM-9wxSVMzXL2Km953Gig7o5pY3_tw1Cgd445Bqt6_d-o03nrCzShN_lGRWjteQ82vueYOZesWYe43apWHVaQ-Uzh6jonNuPrUd8u6fWGOMUQWjcVsQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
با برطرف شدن موانع موجود، کاروان تیم فوتبال استقلال تاساعاتی‌دیگربرای دیدار فوق العاده حساس مقابل السد در لیگ نخبگان آسیا، به طور مستقیم از فرودگاه مهرآباد تهران عازم بصره خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29604" target="_blank">📅 16:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29603">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8tUrhPWxp7QMVkWo-1rOnPHZhg9j9OD1DhwgyMvwB9QhVmlrDFzloTIAsXM5B0Hf0x_VXRbuCm7TgJjvozJ1efT0RRq6anAkBooWO1ctB0ZhyWCnM1QG4LQM-ysCJIX2PqEoAH4pHWx2wpHcQ3zbceABe9aMWFFuqsMbRIQYc_0qIVl_H4qcy8YP7eSbA-mR8ci6iBFyfmGmsT0GBe441Ty6ybpdMlWC_Ql-H_dwSN7MU_Vm3CfzpVE-Esecu2EOITYbUYw6gXjbjDazVkq5zLuyWq_AhKAUbdyzpLxzBiKfD5ByZb9TOHqT7IzL6Ag3IcDPR8VAi1EcMAFijQfWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه‌کامل‌ودقیق دو سری آیفون 17 پرومکس با آیفون 18 پرومکس که دیشب ازش رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29603" target="_blank">📅 16:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29602">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=sLG35WJz5oGi9z6HSs21SAgVpw-IC-5RsIpfngsplGK32MX3nG_hgkK3bvA8vIjkmfyBVpVkaJQ2yA5JBBd7qFoyO_lyeJLx6a-17zL7q3EPypjY9SU0DNwu7e5Gko3EDsp5vAtCji5mjjg8i4Q-PPbSm8qMAURh5DT0fCyabm_McsbQ6RHXGANqpg4buitbLbxjRaw4lEP_TlHsNRIprIl91mHQHd45zT-xTLqpvKE-aGBHQ9RGPNutJRQNgGWkPxbcz-XvDCWC2knQnu0W7AJe7ccJZ1OjUDT6rNcTdqOQzyvLM454qXw7XLMXH7YL5XwQXsBu0Q38PsN5mWtKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=sLG35WJz5oGi9z6HSs21SAgVpw-IC-5RsIpfngsplGK32MX3nG_hgkK3bvA8vIjkmfyBVpVkaJQ2yA5JBBd7qFoyO_lyeJLx6a-17zL7q3EPypjY9SU0DNwu7e5Gko3EDsp5vAtCji5mjjg8i4Q-PPbSm8qMAURh5DT0fCyabm_McsbQ6RHXGANqpg4buitbLbxjRaw4lEP_TlHsNRIprIl91mHQHd45zT-xTLqpvKE-aGBHQ9RGPNutJRQNgGWkPxbcz-XvDCWC2knQnu0W7AJe7ccJZ1OjUDT6rNcTdqOQzyvLM454qXw7XLMXH7YL5XwQXsBu0Q38PsN5mWtKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیویی‌از اولین‌پنالتی تاریخ فوتبال که کلا 0.2 ثانیه توپ تو دروازه‌بود. دربازی این هفته لیگ MLS به این شکل که مشاهده میکنید بدون اینکه توپ به تور، تیرک یا دروازه‌بان برخوردی کنه گل میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29602" target="_blank">📅 16:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29601">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_k8c2tSGIwy3mD0GKPPALJ6s8LHb80k-jswfmxEe8BeGiyXYaGmg2Lj8XiKgjKZxrhMeA6ngrT_aQKoBJjkI9pYkapzm_uTw0a0x0weMxiLD2XrpmlAnqgznkUqdYFV-Hw6pIKyr9VJx_1FuVsJ32X7DfSfbwmrtGAo9662kOr2jgPtCAQfF-g9Et48TIacZeoMyzhR6Huo4Ps8XRgchPxuFYYlzDyFI1i2BBmQX-1cGNEw42ddAGHoED9AUXefIHQZx40Mah32iSVh54H88TLPh41_AQV9zfzDeRshzYQbWOKSZll_MLkOVKyCZivZ_m_5r3-AT2DW1Yu-LXVbCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29601" target="_blank">📅 15:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29600">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OES4iccGYVKoQDTGNz8NlX6gA1MXQ1irlG4T82se9-tCoosTmrAa1lWbApBZlIbNLiuNAW_oqUyKuxmZu0cpjitPPPsk-o7JgYjggiHYoJkn4i9S5g5Oe1T0OLejP1OA5gnS2__ply-9J_Rg5UxjTik-hOWTovG6lJ1pJ116soAUYX0ye8mYlmq8YGVdTvqP65wLbL-EfN6wpIlL4ZT_lkJ0KJQ9kgN0r2JcY7wZ5_PZ5UI1Kjr1SK-AP1oZ_9122gWFhU8WxuCEjYT63olNnGRy2mRINEY9xKkcnATdtb3tvV9V1oqQXchgbgbZNrptGcaUALDmec0ZQ3g80a0_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29600" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29599">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP-E37d9eCfdta2Tacx_ISyPkEBK_z92nejo9PW9QqpZ78ZZL4JFfpkUrHoX2unjKSEpDmN6CDL-HPoiAD-yWjX5u7YVG6WIl1ocJ_4_0Y-NaLSKDTnu5OqppYhGYn3_aST6JZgrnyClwVyFJMjndIeifv6I0kvcPwedgnaA1_5hmT7V-JrF0R81w-9MT2TVLYBSBdDV7PfE86ijPkhIisZlububmnvYwE4sSC_ZzboBCBHBwDCuYlOretEFhQhNKnWOAGHRVqIq6RjRF1Hb_5nGgu64Vybq7wDeMF8Gj5F4w95Qwdx9UD43B3jvW4XlxqZ3iW6pC2u2l5AIhwEypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29599" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29597">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=YvNyrXcpuoGaE2jEiwIVufsU-iaItk-hAy3lwErrg7E1AC0_t-xAHNSYBcYmkdJwscK-VeuqB7dFlV8zee8I-zx_LIklOJDRLHmyrUQwMMi5nSuX9FYAg87idR9D7N6mIYBK5VuvI6X7Y3f7gXnnQpo7FD9lfOLnwjldyOKHIGS0yQyHjy0fXAStjjOUC5jrXh9Ek_Q_iJnsMLfKApU42Ag1nI1Q5Gy_FYe-EDmJUOnfstEUfBmARKVaI81cDI8EWJfTR2qNCq1mGb5eXIPBlrsg48E3cBCyZEaZHjMe2Iyxi75KT9jJ7FEzpxQ2olohLEQc59LCj2YqkzYUiAdmyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=YvNyrXcpuoGaE2jEiwIVufsU-iaItk-hAy3lwErrg7E1AC0_t-xAHNSYBcYmkdJwscK-VeuqB7dFlV8zee8I-zx_LIklOJDRLHmyrUQwMMi5nSuX9FYAg87idR9D7N6mIYBK5VuvI6X7Y3f7gXnnQpo7FD9lfOLnwjldyOKHIGS0yQyHjy0fXAStjjOUC5jrXh9Ek_Q_iJnsMLfKApU42Ag1nI1Q5Gy_FYe-EDmJUOnfstEUfBmARKVaI81cDI8EWJfTR2qNCq1mGb5eXIPBlrsg48E3cBCyZEaZHjMe2Iyxi75KT9jJ7FEzpxQ2olohLEQc59LCj2YqkzYUiAdmyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان پیاتزا بابرتری قاطع 3 بر 1 برابر استرالیا درنیمه‌نهایی جام ملت‌های آسیا به فینال این رقابت‌ها راه پیدا کرد و در فینال برای قهرمانی آسیا به مصاف برنده دیدار امروز ژاپن و کره جنوبی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29597" target="_blank">📅 15:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29596">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKOpeHJpXYuONzmzfJQG_Ov7f4ysd_m5-_GTk2Fvbs5FK2TolHufWQ19Bn8ZDiQeyiTOYpAXP4yIxaQXBz5JksCAqkPPwdk9nQpBbbVh-COe5SIFPR22VgCAEwukWlnL-wKRo2y1AimedN_8wtXFTtCQVeB_JGTdE7xu3-AcRWGJeWVIp4oJ8Aj070ivpeDSHHa05s1s5uhBXri9hY98lt_EZZTzF_fNwHGOUZuUACJ4npnVyhBYYJ6CWpQaunoWiGoyis1zqrJ_l5akTCuMRBNGNOXaGXGSjpBESqG9KNcAkySSs9xMb2tnE4qMqZUIU988spBQ6O4JqXeV6NYl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاریوس دروازه‌بان سابق باشگاه لیورپول در کنار همسرش دیلتا لئوتا گزارشگر شبکه ایتالیایی DAZN
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29596" target="_blank">📅 14:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29595">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOaUGvdwDuOtEYDj26DbMq5-RQhERqZzgJ4_GvCry0NfpB3-l0CXA1Ntv2x5OxqQCcaHUU3AtaUGeMsrB8wjpdvxTwgXm79_ihn5yJx18zWnY4qpVMMQm_dV5f4V70nFQV0LlZYKpV5uQhukV3MKbSfFK3RLeQARaZaX0id1bq3C_lBPjGFKVezZIQGtklvBylmmxISAdLmO6iOL29IJvT277gnUEo10a4ui4zTH6fBTzNiDvO--rKoQRSd6syQ39GvFKnTo--qn4OwDAwb10rHl6psNkv7P2OfFPHgY6DieoISfFlNqZw9kmmdLixeM82AvygaDCT7uWPz16kA4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌ویدیواز اول تاآخرش‌سم بود از دست ندید؛  مهدی توتونچی تو برنامه‌شبکه‌ورزش نادر محمدی رو اورده بود رو آنتن زنده بهش میگه شنیدم میکل آرتتا دنبالته که تو روبرای آرسنال بگیره نادر هم کلا ویدیو کال رو قطع میکنه. بعد توتونچی میگه آخیش! پست ریپلای شده رو هم…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29595" target="_blank">📅 14:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29594">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ji4o0vxHqfgr2k1_x84-fuliVBlp-wQWn-GF3eLVDmEZzsgQgojNicVnrV33u1UcugYONm633mH7uR-Mu1rfDNjXhTqXDpYU2OeVHIe_PJzz7p8OrB3sIgcbB8BgtbKXMuGAHgym6h05tbGInxSFPrdlfkdSLNPRbfGdVt_ro4FKAUJ_9Ws4qeVfesAUw34gd2kp8KGPWvSUnYNJObUrmuQB-lDCfdReWkaLO2mjLksdifTyHwojJF6LHD8bYfpJZkVb5l5obdn-7lqfkzIXZT3DLRdoFFTbKwG7i97FJbaQDxj9-_YvqhaV-KDB-KdEBwjnU3NYRcatHuLW775HUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛ ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29594" target="_blank">📅 13:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29593">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3vLVzLkoEwByHzQrCKyCt-YfbhyYHzczjSDtTs4P4NSQOaRi3xbCb5Hbtc0Bq-fIRWPpuWc1Ty4RG4wZ3-wg5ZR5O6kx3X2riZ05-8QNUmDO7vcgEKmjZideHE4Unq93vSB6gQRW33mLBJrBF_0JR9BFXRCE2eIQUDxTN9ZDq8LVp1jQ9d-6ndB_cWRQtP2ef-QzTerLRQpSatcHyTLUlGInUiyrTtsK8138vEtUMm98GiTvuJDTP4BlZfsE0Z1WWDIiIE1HjAid6A7_ILDuG2yqnlThs_TyZXHkNRQew5XZc89oL8LP3HRJXF7AP3TC_ibqXbalrsyXATG5q8Kqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بااعلام‌پزشکان باشگاه تراکتور؛ پارگی رباط صلیبی مهدی ترابی تایید شد و این بازیکن 32 ساله رقابت‌های این فصل لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29593" target="_blank">📅 13:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29591">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29591" target="_blank">📅 13:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29590">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPxm3H-cDaebb0YQ9nqf-TNVnwQ6vq82HOXO5QbT_LqNXEpA49WF2H4hShlP9mZ6N00IzP2ZvXECBx9OPzADh4q2lid8TKOtvoWE0IdG9N4rozrRwdyWe3-wqGcZWDkPSpFtWGRrKI-L_pehFg_dfexaJZ7v1xUX61CnaCWgeT-p03J7kNALQhhcS6s7KHv3rdfXwZ_oS3PsgKno9aFUL6gAwFZWwGj87TNF11r9spwk8wshababM8bP0wBm9sNJ7HVZm8VtiFnELsezGSvrx16A2xoq33_zZrGU5TpeFwn6awxZrfGiXrb-hR-89aMvCv4RmtUQpufO-4p89J1wRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان،…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29590" target="_blank">📅 13:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29588">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaUB8z3qmsYrhuhew91ryPykqa1Y1z4YYP_uv7-QwsxodwHDRDK3I6DHOTO91SKKo0u0rKiz3jol3t3gnO5c9oN5rB0zytvhywss8Tv8tTcxZx-Gc6GvttqdKzHoNEzNmqn7oOtxpFsfN0v3YTPFT_98P2-2Xz5rfFNUWNrRqgT39gnP4EbwRyU_2HMy4ouSFF-qgyom_93FX4qk8vcCjRLjDPMpu3ce7w8R3cr8Ky-9R0eW-voAbUfDwXgAmvWDeO-8OENI1EuEEkNheX2WYq39zi940s8XlBXH7eYNOrSbkAIrf5E6GcufkTetrx8USQuzLIiu8d7QDFqsjAS7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
معیارهای رای‌دهی به توپ طلا؛ عملکرد فردی؛ نمایش بازیکن در طول فصل و لحظات مهم و تاثیر گذار؛ موفقیت‌های تیمی؛ جام‌هایی که تیم به دست آورده و میزان تاثیرگذاری بازیکن درکسب آنها؛ بازی جوانمردانه؛ رفتار،احترام‌وشخصیت‌بازیکن درزمین‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29588" target="_blank">📅 12:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29587">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-6CE1SGqvowasP56O_cD5Her6s7m3brWNnws1ScijZaUv6ovhxrDscWz50fRg60o_IquqGkckrkUyXn00F93KVbmD3kETvD6hJtWdJbpi6-GTVMypngTZrdaHnVTqus4Y5_TgcBT1td7MWoY7VeOLYOopk9eTBTN3AAJeWBXLll4aLsfqmDfO-yYAbRs-MFwcbsqzdzZysnKr3jyOR_IQcgjf7fidKiqN8KK5s36FQhRYJhYVuYga5IUrjByOnxGCoemLIYy-AZ9Hju58KvPzNovZ5lSn2hjbYoV2Nu5EVJORG81La4lJ_XrHMZq84Bgebng5wB-SZhxNpZQfAXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
برگاتون بریزه؛ امیر قلعه نویی سرمربی تیم ملی که تاپایان جام‌ملت‌های‌آسیا در تیم ملی موندنی شد درخواست دستمزد ماهیانه 15 میلیارد تومان از فدراسیون‌فوتبال داشته و شرطش برای موندن روی نیمکت تیم ملی در جام ملت‌های آسیا این بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29587" target="_blank">📅 12:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29586">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=e_XGxIKa2OVgt3EjHAMUQSqcBlVKl8sD2pKUclBS9F6PD3AXSUeEqjOibss_KF6eI9oPgXKzahCpdGMdg49jyGKKRxHCjxPZCDQABkV4accMo7GXRFuquqlfI9YVqVPDR3g3_EWAz5kUtxSJNuWbZTPPbxQwD6x0jwXo_eLMOa1luxhVbwQZTSq8SHNzQTim-ZBOajpo_v-LF9Ane4D1ucaS4Mq7T3os2eqB9ub6znKzdotLXylewIUc3ECWlCP_LyEUCMRrzCDUCsaLkBdnqarpIb_hdZEalWdfntK9SOTSRZkQSqrQJjG0ubwcvRBOUrNnzYf-nGMrqzeE7puanA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=e_XGxIKa2OVgt3EjHAMUQSqcBlVKl8sD2pKUclBS9F6PD3AXSUeEqjOibss_KF6eI9oPgXKzahCpdGMdg49jyGKKRxHCjxPZCDQABkV4accMo7GXRFuquqlfI9YVqVPDR3g3_EWAz5kUtxSJNuWbZTPPbxQwD6x0jwXo_eLMOa1luxhVbwQZTSq8SHNzQTim-ZBOajpo_v-LF9Ane4D1ucaS4Mq7T3os2eqB9ub6znKzdotLXylewIUc3ECWlCP_LyEUCMRrzCDUCsaLkBdnqarpIb_hdZEalWdfntK9SOTSRZkQSqrQJjG0ubwcvRBOUrNnzYf-nGMrqzeE7puanA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تقویم
؛26سال از این‌خوشحالی عجیب و غریب محسن رسولی ستاره 19 ساله سایپا گذشت که با یک حرکتش روی آنتن زنده شبکه سه فوتبالش نابود. بعد چقدر بازیش خوب بود این پسر. یه لحظه نتونست خودش رو کنترل کنه شورت ورزشی رو آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29586" target="_blank">📅 12:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29585">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JN1cEAv1lGp_gsLYLgBX702AWq4Hv9daKmZI6nfNlUSyLO0h7x8Wg-do9xMonlDjLfV19yklP3Px7maFMJo6_3SGbr1t0V4rAqfmwHYJAFKbH0KqcSWlnruPxMgF_9L-NkHqF9Gtkb4U2dCsP80OLq4mpASgGtxZk3Iy7Rh1epC-RUB3o5oiVkkA2dat8lD5QtGgvnnwMtlXT7ze6fod16ynH5a5_Hsg2kA2jNtHC_TAfDrSVxg00_d2g9UtA16u-qQ1GTvraRyw03HPXDn2lgOgCPXACWtvaVTRjj73SftYSD_qAVs6XvbAKvSnr3MAjcrDM1Fcam2jYONifp1kAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛ فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29585" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29584">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd_X9W1RjXxUlgCjvD9Mv4ajgFbFGyhaYG-dTS9irbkzAl-riM-AaWzYjMjX8ujIwz7CFL6NazN_T9H9eq-KXBODoPfoEgeduwX1cIAEpdRkzWFbOkas58j6aUTXcN100Ir_6VkS_wm_wepKrDYxYvB370IGqs2QmzniGzVuY63d6AtfGc-0fhSJCrsRfzdJysfq4tXLkCQYS5kBW8k7yfX27FOFc2WHMjbkAEm8cFHgI6jCJQZjWz041TPl1hmIl_MtUF8NB82rh7-M0qhj-rgtm_4nhIwdvQboUDh3KZYFdGW-kwLL892cIdkXOErkrNPzDHw8-yLofQ1a_D8G4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
باشگاه السد قطر حریف‌هفته‌اول استقلال اعلام کرد برای تمرکز رو لیگ ستارگان قطر و لیگ نخبگان آسیا از رقابت‌های جام حذفی قطر انصراف داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29584" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29582">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
فرانکو ماستانتونو ستاره آرژانتینی رئال مادرید که مورینیو به پرز گفته بود اعتقادی به سبک بازیش نداره و قرضی اون رو به‌فیورنتینا دادند امشب برای تیمش درسری‌آ هتریک کرده و نمره خارق العاده 9.8 از سایت فوتموب دریافت کرده است. ماستانتونو در پایان فصل به جمع کهکشانی‌ها…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29582" target="_blank">📅 11:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29581">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SilWToPeOVBJ_aXkxidSkw8KycqPqPi1yjasTtorjLLmdWh9IqLOyBw9OAdTazmIeIYKJscnhU67rczJmpuA1RbQplAw17Yl34l2R4YsPRcAwUFJTPFyBUkzMV7VFew03O6-wMXFRRdppSNANDUn3uQzZIcasO_b43Zq_G0HxCz5k7EamQ7mUt4rpBvPB0vcoiSXp1YrmdsLcTmi6mnuw58MJOx13yZHP9UfN0yhqmuXeEPSoQxYcejPjETmZhnoVAj9hGtMVY-6Y3QydqHb2506kRGg6nIg7ln7ObOechUNcdyf4GZpZBDjMxo9YH0b0T__w9aTBMkRrPj0T3apBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
47 سال‌پیش درچنین روزی؛
اریک آبیدال ستاره سابق بارسلونا به دنیااومد و با این تیم به دو قهرمانی ارزشمندچمپیونزلیگ رسید. آبیدال سال 2011 هم به بیماری صعب العلاج خود غلبه کرد و بزرگان بارسا در شب قهرمانی این‌تیم در UCL بازوبند رو به‌بازوی این بازیکن بستن و آبیدال جام قهرمانی رو بالای سر برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29581" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29579">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af01699be1.mp4?token=ek1sYjQKA7dFZYbV80y7BsrhGnEtE75klv-Fi-nTh_zsTqL1EdQEr0SW8Pr4aspeB7IWZr7vvGHAr46k8krsTLM0ViHG11aswP9t8srCrfCZXcVOy-5L9tz1tEd9BADSHUJeKMJuqeO-zqOi_K0-sc0C0yPK1xrc2mwbR64CubO4KuuZQQzjdR7gvZSLUsSe8nwu8w7IrTSFrRIFySZgKQv2M5THfKhdekZMmAuUmyF9s2rwPr7rPp3kFnPoSIxY-OmAi5AuunYcO-zS71iPxFAMXpEFQD3IjKpSYe7Sky0aDSoTlq6RVj9VrxoJeN2k-du-Lh8-KOZ5cjXZVwGxzT8d9oFP9OvsPgp8jHsuIatorZyO8x6ypO09begvsBxI_7mfc9wH4IX4MMt048zAIze-3PaHuBqxvCdU7SVFWVcMjP-DfspKdwU57LG6Z-x5Z8h2F-mKksFutkKB4HS0mt_U-C928q71owIOWqxAJcWO09v5DBYuia3fSB-VTWfG1aJTZWKyA_HhepGncbubPCs9XIos3pobIVJFxwSb0Y_VoiN7shi3OnEXnJF9V981L_g3HpMqQekjW1Dj9ZQwwt7SF4sPQibopmXh1K0pBBQNjgGGIrZaAHO5BEbIPwrnUumhQNltFHauPRoczMlCNl6qgOpBTqyauxQIZRYItH0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af01699be1.mp4?token=ek1sYjQKA7dFZYbV80y7BsrhGnEtE75klv-Fi-nTh_zsTqL1EdQEr0SW8Pr4aspeB7IWZr7vvGHAr46k8krsTLM0ViHG11aswP9t8srCrfCZXcVOy-5L9tz1tEd9BADSHUJeKMJuqeO-zqOi_K0-sc0C0yPK1xrc2mwbR64CubO4KuuZQQzjdR7gvZSLUsSe8nwu8w7IrTSFrRIFySZgKQv2M5THfKhdekZMmAuUmyF9s2rwPr7rPp3kFnPoSIxY-OmAi5AuunYcO-zS71iPxFAMXpEFQD3IjKpSYe7Sky0aDSoTlq6RVj9VrxoJeN2k-du-Lh8-KOZ5cjXZVwGxzT8d9oFP9OvsPgp8jHsuIatorZyO8x6ypO09begvsBxI_7mfc9wH4IX4MMt048zAIze-3PaHuBqxvCdU7SVFWVcMjP-DfspKdwU57LG6Z-x5Z8h2F-mKksFutkKB4HS0mt_U-C928q71owIOWqxAJcWO09v5DBYuia3fSB-VTWfG1aJTZWKyA_HhepGncbubPCs9XIos3pobIVJFxwSb0Y_VoiN7shi3OnEXnJF9V981L_g3HpMqQekjW1Dj9ZQwwt7SF4sPQibopmXh1K0pBBQNjgGGIrZaAHO5BEbIPwrnUumhQNltFHauPRoczMlCNl6qgOpBTqyauxQIZRYItH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما روز به روز داره خفن تر میشه! شبکه دو یه کارشناس اورده داره از خاطره قدیم میگه میگه کارتون میذاشتن زیر کونشون فیلم رو میدیدن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29579" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29578">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTEj6BUimS-TZBHH__ep5EVu8oNroylQx0JqIGm9sK_V1isBCiefXNIgYVXRyNBmUC36Dby0dtLp_pZ8MYUh5LEVm7Rk_UbGKYmnYT7X3JNQYobsVB9YxGbUWnKUq9DAzZSXBASCi6VMUFVhzEOh3E4NFpDDMJBy9G7xNsm6WCxkzirxDQP7RiOKRWYOBY1_IAnTZ-O0C68G2PEqqGj70Hy-Min4bI5YExgXtw_vBrV5zqsu_CjYE9NFnfQPrF8H1pJs49SLTOfUmb85sJbVSKufDm6z2Olap4MyDjOIEF4vlJZsIRTVeF5oFf28NxOAcr-umfwQOOnM16FPHdY18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29578" target="_blank">📅 10:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29577">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS19-GX2PUY3tnhwkDKtzdrTbveWY9PITE_-oQUscsUY8RTxcyIyzurtHLqtMllS27a-8a3k82-_znFh8faIMf0O3PdyI4xIfZFLRpW7aH8cYDZba_WTxoRntPGImICEx4rOks0-YMoXcCD0XGegCiXLpknEx3t-__huH3XgLPhKUj-VQyZiANVDk4Llhstcu87cPR5U37R0pRYVB0Od7QT2pNJLxikaj_cEDiCK-0zIdgTBD6ju3HOwGMfVt7k_rvtQCX5VrnvddkGdJbObFCmNFeURyuZGWpojXHFAkNXb_ykyEs6RJ-nHroKa7N4KQdJ2T3p15s7lzYvyq5Kdyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان، حضور مجدد این بازیکن در لیست بازی با این تیم غیر قانونی بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29577" target="_blank">📅 10:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29576">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=iZnjQrW7OwHfiHrKFQ2EpwNeiUYZ1wegxucYkeswTMQouxfrvYy9fAdbENXVCbsQ0qKxiOcXWabxFWLsAtBLqu0jePmsyiaI5tdD7c-Dx9mVyWj-p3opp51fpeA3milaUVVyKdOtoWnM21WOAU9UlZnZ9_9b6HOa1SdhJCE25q-wQOmVbnzo5rLxJEtCedjsIBuNTYtJniDOwBrHDtOCNcHncwC3hiDWlCWACnwVucsTfOabpmSJQsP-XqLRodpmGnIEU0-vp9OhtmEKJuuHQpuxbOhb6yBSKtwwvQPUGkYKh6JCJ7dSfBV00mu-lUIjhtZ3crAR-rc19BcFC-ArKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=iZnjQrW7OwHfiHrKFQ2EpwNeiUYZ1wegxucYkeswTMQouxfrvYy9fAdbENXVCbsQ0qKxiOcXWabxFWLsAtBLqu0jePmsyiaI5tdD7c-Dx9mVyWj-p3opp51fpeA3milaUVVyKdOtoWnM21WOAU9UlZnZ9_9b6HOa1SdhJCE25q-wQOmVbnzo5rLxJEtCedjsIBuNTYtJniDOwBrHDtOCNcHncwC3hiDWlCWACnwVucsTfOabpmSJQsP-XqLRodpmGnIEU0-vp9OhtmEKJuuHQpuxbOhb6yBSKtwwvQPUGkYKh6JCJ7dSfBV00mu-lUIjhtZ3crAR-rc19BcFC-ArKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/29576" target="_blank">📅 09:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29575">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=Nf6THyKwZVLizQVzjdHPpgJ51j-6xUJE3XObJHMfg1IFxms2CrqlOX87YkbYrJtG2ik5wDMAerfq6lRKAoKu5Im9GXQfVbe66iBVQRLCirNt7s6upupJfL6e3RH3x90h3TdaUG43dUK6pIzRtqOQ_ifR4isdISl1EQiInpnja0wkVDmfOyqZwaoAOo3i9p289-xA26p6piWjDDFvpLEFIRtNzNiTmSQ7oaYHpSGjGi82QPqYG2sIdsShW_6R9rLUt7amIdxFzYz1Z0OsKF4Rn4UC2hQcp26gwtOlf3M9RrtsY2QqN3_1IwxmvMyVUKHFnbzNG5iZEipEJ2jWXRSyqz2xcE-M5PackT-U-VlsXdhjCRy-Gf1BaeG_70V1inXt4Sngaxg4_UDUJmMeeBt8l17FL9I4T_GtZVYls0BP_7s8L9YYD92QlAXzLzDYvwMv76u88dmjzzoffN3ZTAdmHi7AyURK4ixSf-r8jmB6KJaU-XhcTu1ptm_aOFCzOdShkfZxOi9_7DyBYgKM2lfBxYorOnSWVuS6KZTrNDHp_rqz5Ra5YPE9OFR3EOfe5f_uKe5wwLQNDNWBOJxJQ2eCdLTNR77aUz_9FE4p5x2PfDgMguzYIPJmMoUegOHG-zRMgN7Mw8sTBwh3D6-jdFtEj4pqW-rs7qVogqekf0uSgMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=Nf6THyKwZVLizQVzjdHPpgJ51j-6xUJE3XObJHMfg1IFxms2CrqlOX87YkbYrJtG2ik5wDMAerfq6lRKAoKu5Im9GXQfVbe66iBVQRLCirNt7s6upupJfL6e3RH3x90h3TdaUG43dUK6pIzRtqOQ_ifR4isdISl1EQiInpnja0wkVDmfOyqZwaoAOo3i9p289-xA26p6piWjDDFvpLEFIRtNzNiTmSQ7oaYHpSGjGi82QPqYG2sIdsShW_6R9rLUt7amIdxFzYz1Z0OsKF4Rn4UC2hQcp26gwtOlf3M9RrtsY2QqN3_1IwxmvMyVUKHFnbzNG5iZEipEJ2jWXRSyqz2xcE-M5PackT-U-VlsXdhjCRy-Gf1BaeG_70V1inXt4Sngaxg4_UDUJmMeeBt8l17FL9I4T_GtZVYls0BP_7s8L9YYD92QlAXzLzDYvwMv76u88dmjzzoffN3ZTAdmHi7AyURK4ixSf-r8jmB6KJaU-XhcTu1ptm_aOFCzOdShkfZxOi9_7DyBYgKM2lfBxYorOnSWVuS6KZTrNDHp_rqz5Ra5YPE9OFR3EOfe5f_uKe5wwLQNDNWBOJxJQ2eCdLTNR77aUz_9FE4p5x2PfDgMguzYIPJmMoUegOHG-zRMgN7Mw8sTBwh3D6-jdFtEj4pqW-rs7qVogqekf0uSgMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌خاطره‌انگیز و دیدنی از عملکرد گرت بیل در تقابل با بارسا در فینال کوپا دل‌ری فصل 2014
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/29575" target="_blank">📅 09:34 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
