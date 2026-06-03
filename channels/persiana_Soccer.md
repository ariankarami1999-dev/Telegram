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
<img src="https://cdn4.telesco.pe/file/Ly8Q7R0nBATnUgJMD9geHOL1M9zUhe_qMeBnYkiaSsVII3qDMYOvYP_7oVSjW53PQBbSb04gwsuV9FMH1gqlfmGYnKEeW3RcKzcovLWZWgI-sGvMdC1VwSK51ZXzOtB7qMoLuI6JDXZZPqeiUm5HrvsQ_b2Ks2mBV1hqYgytzP0EnpaZnUY0eNGGtwgQhv5wtrc5OLQRxa7zgglBe-mPabT-SOtcUJdVphkSa9h_dO8Dv8RCdHWxu8p7Ik6MJtPobfq2YhbHWHU8-5paqDDwIN093Dt_JH7MqBwwystIYPUXZx6_8SYg6Uatvkl0AUuA6kkjhJe6wKss2QC8RvWlKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 176K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 00:03:17</div>
<hr>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ7BJJRDno7cmEIDGqfmkWozCkp1N9ytZ3Li5plcj0LMap4liG_cGwZqE-pITjsgmOjQhgxgxNmdaAp7fInvi7CfH9RwEg6B8Ig19RmvUixm0VAoiclUpj28t2V64dnfCg6MyGAZUZnPgH_V9cj5KvfgYKd_y7oTucNJ_WvSzFecD2qJW1do0-9OKVRWKV5BfNJNSjKFF-rk1r0l4tIjRduDaNqto7i2-Qn6rRMkg6evHYAEmtwsVYS0un82ysKCDiQG9Oy8pynnb8PlIymyAOAjkSeF4sT3x5q7NalYUzp4bCV9pmX04YXyMQyK9KeEcvPnH7QgBoLJVye_5blpRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فکت‌های جالب از جام جهانی 2026:
1️⃣
۲۲ قهرمان جام‌ دراین دوره حضور دارند. حضور ۴۴۹ تیم‌مختلف‌از ۷۱ کشور جهان. ۳۵۷ بازیکن حداقل در یک دوره از جام جهانی‌های گذشته بازی کرده‌اند.
2️⃣
۸۹۱ بازیکن برای اولین بار حضور در جام جهانی را تجربه می‌کنند.»جوان‌ترین‌بازیکن: خیلبرتو مورا از مکزیک با ۱۷سال و ۲۴۰ روز سن.»«مسن‌ترین بازیکن: کریگ گوردون از اسکاتلند با ۴۳ سال و ۱۶۲ روز سن.
3️⃣
کشورهای کیپ‌ورد، جمهوری دموکراتیک کنگو، ساحل‌عاج،کوراسائو،سنگال و اروگوئه هیچ بازیکنی ازلیگ داخلی‌شان دعوت نشده است.» «۷ بازیکن با سن ۴۰ سال یا بالاتر.» «۲۲ بازیکن زیر ۲۰ سال.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q81PgzSjaiKyvjgjQfNlE7qRV8lqLw1bSDSFfWCat9LaZyt52FoSvsDH9WhBlTJNJVq8jNraUR2EymgGA2HiW3bUePqpwjk8bcU28rEgjV1vKyMFsRSvZuCi_d-pu4Wk8V9kBgbveZNo4qIgz5IF_RthgGzTsD-wIfuUrta8itOQfqjT0NaYD3bCbclhwAXnLxSDr4QnpmksGSMEstkMNIHGe1mn8nr2hRNWwXMqDZTKurBiHZMKJ5QSnFEuLI-KuFP8tLRE7uSVv1hUOeHH4uq6TqZWGIA3_adZm2pvWMz28efbYThXUbhiTtHNl0z0TaBTuQfDx0ugCz6YJjs5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLUO4jvDdTBhO_7BLxEBr2p0iDkYF6w2ttLjkTsxfjSBYIJVvaL4EIyPPqyj8G4kQGGfmZt5Wk6pKmCxJ-_GD2ZCNga4HqqRdnl2m5vONI9Xyiwk7RA1rXJDeklLbb0lp7cCyQAz9I_GEcQmWXOb6HSJvEg9ErAkKlVML_aKIOGYZzTGkQeJ9Damr72Y_mpkgERsv_0v-oCwHmSsvUk_tlG1v1DTktQtdeDUuHFpj03ylqH7pWImG_ZbF16CE2yhwJOKD8rq3f3gnQJ-cUpNoj2IniQnSY0Hcf-fEiWUKwauViIWTb_K7roqebzUz5v15EgTto04N0nCM_1mnhxQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=kO_yjcmLWh_puC9SAAyrQIOcQljhvIcl2gqXEnciy_p9oVA8oF6Mqug7RHrrgC8SlqeuuUWprmPKs_lRA_eilcA277sQt8RbswEu7-rGOJbqhsjWVKOWNVJ1mWvvO8SNAxRpnaTwS8q7C49mN1FXl4Ma0uhY4aPv6zPKwlqhvWjkTtB5OTGjkAjgxUVkUE2KFhhcUYk_RKv7v4FtQT8WywEYIZtmjv22JNhb47IH1dDMVXITtiDBEshL7hgBT0JK2ltdDBi1M1-ccUPHFnxlJVVJFymtNK_ukMROcMVjrWubnZ657yCJYKtTDcgSA-TruHEv9RQxt4_qdTriQGrdvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=kO_yjcmLWh_puC9SAAyrQIOcQljhvIcl2gqXEnciy_p9oVA8oF6Mqug7RHrrgC8SlqeuuUWprmPKs_lRA_eilcA277sQt8RbswEu7-rGOJbqhsjWVKOWNVJ1mWvvO8SNAxRpnaTwS8q7C49mN1FXl4Ma0uhY4aPv6zPKwlqhvWjkTtB5OTGjkAjgxUVkUE2KFhhcUYk_RKv7v4FtQT8WywEYIZtmjv22JNhb47IH1dDMVXITtiDBEshL7hgBT0JK2ltdDBi1M1-ccUPHFnxlJVVJFymtNK_ukMROcMVjrWubnZ657yCJYKtTDcgSA-TruHEv9RQxt4_qdTriQGrdvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW3tjeiplsN4j1FksxijzPYXxobfE5q6wb-XZEMgwEyfgoUfgTm0NWxkuRlR0re0UmqzjxiBTwOLnEHAFBmP2DoBUFFyKnoG2c9EGO9e4PuvYanL1adW0p6JT72Zs850eCkqYWdxLq-o1ZZrdLK4V9n3ggm6goKQKQnGc6MrkZ1KEVGJ7RUMnAvBtgJ4AdVbTjiZSoQ1I8E8NpBoiFiBL9aPGadYrrZZxTdvsIgGzlrkc9wxyBUo69UdZQfH6HrgdlIVlbhIHl_cXkEE-eujRP2YQAejMZUdd7AXKxjho9d2zYL8bFvjoiw9_Kd3M53cZC4oQFqUp7Q9LcqwhwYdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIZVxJGfFRC0w1MkFRTk1FhEfgnz3XCh8pxdTCmVpmz22RU-3qy_x39oAzYEqOZrnx69hYatVpkSl6vnVlLHDoJtrip98rxP8o_mo9bXjVe5LdcLUd9gh7sboDjhEYkp2U-ykJ21Ybu2YS7bnlV8pExZIJ3RhmH5_q8ySLT6wZ7LQpGgH84xlDmevtrmJsX93FoOtFbKgl_nNsA49fZl_VXmrNxDFKuqjeX95-9hhRThf3VYC1vA3h9ddHeoqyEI26ecXiUswcS1nTPTUmah4L1ZJUd7xdw2uV4uY2wVzi7qpACSWqf5cdEyShS0rlZQMt2ZQMex3AsQQ6HR3P1d9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برسی دوپیشنهاد برناردو سیلوا ستاره پرتغالی:
🇪🇸
اتلتیکومادرید: تا سال 2029؛ سالانه 18M€
🇪🇸
بارسلونا: تا سال 2028؛ سالانه 8M€
‼️
ستاره تیم‌ملی پرتغال آفر بارسلونا رو قبول کرده و بزودی این انتقال به شکل رسمی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFQ3TBlbzXScu-I6486nR16JM8PQ8blOf0MBl4xFm9aKdQRFm5JRwoYNzV_6_G-_QLhj0MXbGhlFsgxuh19LV24bQx9ejdL6VupQLz5BLSdDI9td5W2wa0iNrfTnOVY671No8xP5pAWpIxmk4cBV1DUVRZ1v5lV0Vtqg5qxCkk3SFIytgLfcv_Uq6sTbHE9NjN0prlfGVPeXolFdvdKVNipZOTbdhi3AQkdGmvbLBzneEomLODnaXJB1vOr9EG_uYYo8PGxffKsmykprD5AB7D8PsAkT1-ai9SzPaGPiaoWbd17AoMDTsa7TLJcOun7Q4RXqzTLHJjMTLPzke7krnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfvq-_A_dnTrzSykHCosI3CkbYorWb5YVgep-dOZlzj4jZ-eWz3jtt5qhHqCU0iRpChqmmPX-iW9t2LycoU5G1JNP5ChCBze4RZw68htKoPoxCyGH2xptUhZR-3oXcY6jn8gq0FneMcHJCAbrEBrnI_LM0jXkZXzVa0WcgSJJSigrA1iZqOuqPIPQQzJxpYHfj2MKxbNSFtRIM0HqN45r5U9JnlXGa6qSgPFYwNfmjJz2yN5tFitsqTMjFwHL2oGPQJK9umTPaPMsZWFm5YKZN0BNgrHCNljycgKpsdYX2Rtacz7Dob_IAYg0hFySzZwD-PVoAHM6km4xKzhxOuVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjjVRMKdAYShHK7humCZ__PMVbXTY5wVexjq9Vu6k6nRIOqU96d7_lDazoy6kwh1A6kqkSmss5EsxS1YdTrLpaAUAjUMRBEpwdT0bqgVc0G71AFTnEp4DBND_OjyT0F2V2pBxkutU3FnYScLt6MHIfNbv8fsVyd2YZ2ykYCiaT4Rx85_ulnu7_bgrw9uBDRGCmWZPdTXBygJBHSAsMwLU_pEfOK3hvqhXhlfqbCwYwkB2ZJAXdLnWek7SbQMQYhlvSQb9v68qA_5Q5g6OG3X4heRf_Nbt2oZvGSMggb9d88Xay95SE3LEacUVv9pvM4AFDMQ31piFSwmT5UMz3FNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">توپ ترایوندا آدیداس یکی از پیشرفته‌ترین توپ‌های دنیاست که فیفا برای جام جهانی ۲۰۲۶ انتخاب کرده. این توپ میتواند در هر ثانیه ۵۰۰ بار سرعت، جهت و چرخش توپ رامحاسبه‌کند و داده‌های خود را با اتاق VAR به اشتراک بگذارد.آدیداس‌معتقداست این توپ می‌تواند بادقت میلی‌متری و زودتراز داوران آفساید را تشخیص دهد و به سیستم تشخیص آفساید نیمه خودکار کمک شایانی کند. این توپ بدون سنسور در فروشگاه آدیداس با قیمت ۱۵۰ دلار بفروش میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22724" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22723">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mgmi5LqyuAHQAfwkvy_go0hBZbn7dm070slh_hAumbVjnHq88kEJC0s6dhFx-noqB1zSHk7JEQ4zTe1tasjo_N6vVdwYjX02gtwesh0NH2pyd5My4Mie7ErJAGMUAeLmcjCwMcN9OlIK7m3lbNqx49HQEyAFKEisnjb09bLIWSB72X5z08pKH4wT_r7WJHGTkdtzSszN6xHAvbYZcwlv5PbQanaAXHKc_FSmfRzTzM5CKp178JE3UXsZvJn1HezXL0wpcuzTvHs15XScbpLrKFKkaQobyqo4L_XUaZs44yaTxJajdsUWmE8E11GvwNa-aVJX2GRkD5ZmTA9BLGk5Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/22723" target="_blank">📅 21:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHpLxbiXdFjiiZ8rGUB5xDAwtYn2DNy38ovyu21-X4M4vybIwFN3abbyTGxbb-XRGA7SEGZR42b-u0yAo0Ed1lXEelDhY36d7jPYJGE-Ioq2bYlfdZMM0UnwgzgQaMNgx5oOYjQHlbjyno-jxu6TMl_woHwA8re-wib4MuAjBiAROiYfGCsFcR3euec2UYWro-2mTR8iXyTUycIbxY_zL5eKe6dzonhR3_WRyZ8pTGBORYgHAN7ZDMJWSxORkUw8_K44yi0UPqVE2XM3_8uAzez2xQRVtKT9eOQ2x7imU3QpA2yDb3nNKjVjpdxoZg_1dviYsMWuO2pJIQ10XAaGzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sI7Wh3XjkaXKnuzKdjTLbc9i6gb0Q0Xn1IDXjrNClJZ1fAbFzxE38F2karDJgVVNXbD60rRz-dqw1d82BFP0tVe9NQTaTToHGKQFFj804596Jbly34nmREBMxnDVX3qF5yLlmP2hIddhZ1HV-2X1EsgA27DwTN7pjnyUy7Ci3OiO0vsR21gM4bea4hIUOsQAFQu18xZ91GTBgWfe3iYUQRnoIBeBtzwqbj78pImU5xcCIxgO8zM0Opy2oXiyncvdkMFsMgJ5jBd_or_SXaB8NuKjbRKWebcGItJNyyKKuoievx9giZXkA2BKFk0vaRBaKkUswhRpGEgshRc-f_fO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOhJX3ieTGcVeyxFs36GmkGdVj8ZzZ1A45x5dgAAFTw_D8w5kf1HmQ6RJBRcASp0OtVQke3emu5YeL7BIvJ9cgFmDWNPpSh8Wj0Ouve80aeJbhWP5AJIPcRe5zQKCqQuU25k0svfG0V-6aRsMlIBMm-A6xiRNyCZRH333Yt4AJeF2a05tpt9LjCu0bjvLKlceXlis_RnD46U45gI4n_WVes5OlLG0JDYstaAJZvD_IEF5mN2lJdvuFCXab4zwMBzT5dzWXr-T-3PrFybm8SkuujEu32J8sZhs1hlFhgk_NJvDeI_9ZDQCiL6ePdcfs5v7vtEkNSIzybEsO3NHYrN1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG49v2U1XMeV3EYKWWjZ5riE89pY9yrf9U5bBQgSDrDEU0544HA_Xmtyl--bU6noISFu-Knj2k0OU8SRbMxlMnjlVyaiJjYJdLWxI_uIo2zTawGChcdL-soKktEp8TjOqBwmqXM4CVFJoRWkfpecpclIMCbrBSlW17jrR_glKjQ1fTEJPClLcwT6jJMksDejp2WoKw0MSHW8NaZfmCW3Zak5krS8I1gJyikkHKz--xRgjeKO8oHzb5uPz8yH28JXkzsDgz2pWdI8Hndl1z04FPnCqzaruswjfsHjITj39uZvar3R9NJWDoIQk5ox5fgoHrueigyB8DD2K3M05dsHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im3dfVxAlrwLCZq9lgpOiocN-f5jB1AoRChOMfQe1xlbx1OrF4yhIX3OFfF0E58rYhCLgpUjXyWUIba8Qe6emX0ROG2Ja03Zs21JCAAqTIrSNvK_-2sI5Ccxng5m0mxYW6-hQsTu74ygcB_W-PS8SBldTSki7shoSwZJQ-Tgwr9N3lkcomRL6CKYjKIqhbEBDWOvxGbqJ_XrcuSUSRJxePfj61iBd64JClN8IEnzLHedQhrYvssng3MduGxkK5pmmQ-zihxlNq7orRTD8DrgVzaeAkaxjfL3OHyt3DemMfdy9ncSZJBX8pmXdfY8fgUhPSB_ogVRe-hjDQ6AzqmCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc2nSwGpn5UO3u5-nkMCkVfN9pud9wTsuCUxdXka3ni0zZ4cS2EM8L346DuyjWwtI1FxqeMuZVIfX1GoSEdor_NDkr5e7XNrc3dq-CV89tUiWbMsPkWgc-fFJMC1QTCpLqT8-e8diTnvwMpsb3MoO-e6nCmA3GlQSD9Q2cOQR2qXFHnsElqbIdLn3xw_Me6yGzy-yxStIGbKrJY5yXYvz42bHBlJQ_vtPqCvTG7vHx16InpA9vuRJ58omuegTm4hg0QP3E_YVgqLEXusHUDQlAFy5oOYssEg-G25r2cB3Ou7lfPfRY_np1qWxZ7KxY-U7aerTlJQANwpa7l4MpoGGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت عراق با انتشار این پوستر؛ خبر از عقد قرارداد دو ساله یحیی گلمحمدی با دهوک عراق طی ساعات آینده داد. هنوز قرارداد رسمی امضا نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/22717" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9TloGmb5wd2mWUP0EF5StZIwCeekigyeQi0n19xX0obvXkjSg_IBUr4-1mGM4T0roJ-0Jh5_0zbY0OBgsjos5_wR4QcVpMpbyrk4vjDos6OHLiXj-k7OALjAs1WPaXrKtnJmf8-5ECCWbi-j-r0HikHp62XF2p41C1_VHdqbwVXWCcxpYRvjYrsfcZ-yEh361_ODMSogfJr73DxHrKE_G4nWRB7a17iuUI4M5PyeQ-NMr27UykvebO534X26XErxMGzEc9xl_BtDGB9slr-LLBA3EYuMTzwVpAJniFJ2P79uo5SeMm6o17MgwolooqkTlsFsgXIwxy_bqj_52aiaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIM0x8uj7DvOws32dkrfwu0cp2apAvUU2wdrFZ_o26-5TkZPo87xTqZLDcIBbRQQyGiVKKt7AZkn-eGZfZlkk2AcJy4NcBKykLptU6PC1wEFQU9qU706YwZWJI4mXvF-KSpxmHSM-hDIwUoT_XnChkwTrFlrYwQVlr5sfy4CFjgWOxYRMaN-2vRezpK9jkz8k8jjCn3ou0vsaHSNfEOFdPz7E5bfo5BKAWtLMQyNOC_4aHNbQmKmmIdHvJpfkSvd_npdFbPGBSIA8e91QFi6HXfYE4BElxsUPHntFVumN2BZe-QBhZ_pHb2PyWDC2CF-n7PV45GNsF9jI6EDIWujNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇿
🇮🇷
ترکیب احتمالی تیم ملی ازبکستان و تیم جمهوری اسلامی برای رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22715" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=SzQvm_dw9Uc_m7N7WOTQ0XK5jHcsYaKfUZgHl9TUAkEWNZwmyIAcdCLz-tcgiccp97BWPWRGScTRdRVCA0CHlvNaPsYdoaYHHaxtrfxwl8hOBo2AvWlsbSYEU3gr5E6KDwz15Pik-sk_3bN4lvDi3Oex4oiokgjVRgK5WZne1Z8X6AsRFiT03Vx3twWJBlqvH3HjSehYJpSdU-eOspu-5HmFTNPnxC5lI80r3EVeXBZYGQdMCPJGy-yJotrxk7hjpaKsYcmrbjOunDOYwIpAl9_osRBhtayvvEPQtOZL8kUHCgOlsfeucKPZUOkm3HQUyUrVt5ECAOxnGlxBLd8bmzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=SzQvm_dw9Uc_m7N7WOTQ0XK5jHcsYaKfUZgHl9TUAkEWNZwmyIAcdCLz-tcgiccp97BWPWRGScTRdRVCA0CHlvNaPsYdoaYHHaxtrfxwl8hOBo2AvWlsbSYEU3gr5E6KDwz15Pik-sk_3bN4lvDi3Oex4oiokgjVRgK5WZne1Z8X6AsRFiT03Vx3twWJBlqvH3HjSehYJpSdU-eOspu-5HmFTNPnxC5lI80r3EVeXBZYGQdMCPJGy-yJotrxk7hjpaKsYcmrbjOunDOYwIpAl9_osRBhtayvvEPQtOZL8kUHCgOlsfeucKPZUOkm3HQUyUrVt5ECAOxnGlxBLd8bmzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازشوت‌های فوق تماشایی گرت بیل فوق ستاره سابق رئال مادرید در دوران حضور در تاتنهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22714" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdOQkj3_8dYYytVNrPT2XLDO9wUJ9m95KsXebo_6QyPvz4F62M0IQhensheo5_HDF8S9BXiaw4FWHvcwW2GnROIPmmGJyz9-w20gqf2ioB_r2WfrwwZ3t1adLNx0qmI9Np8RB_YAu4ufZUa_rDcNEXaLabAzPuvNE41v_8889x7l7htxz7LQ_aLtMZ8HR4xo0h5CsvQbk_ZNLKNkNMuJkJuHr-R0JE2AfXoRYR8ejv9YrdOVZeR40ocW7TaZuv0wo42ipK4iaACaRP69oTFJt43IiBN8Y4h9WwZ1n01x2CK4uard38nFJxoitKrfTzHr4ilaLub_FxzjuhKR3ZgKkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ یحیی گلمحمدی در روز های گذشته مذاکرات مثبتی رو با باشگاه عراقی خواهانش‌ داشته و حتی توافقات لازم بین طرفین انجام شده اما منتظره تا تکلیف نیمکت پرسپولیس برای فصل بعد رقابت ها رسما مشخص شودتا درصورتیکی بنا به‌هردلیلی‌اوسمار از…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22713" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3esVWe4rMY0431xtlIhY5qfau2LJWIRyRIfGxzOXTBtjC2zRZDvJcQVk4oedw3Pzc8AJy4FRyGGJeg9z0tb3mz9Yan1HVjb4Ezs0gtTBGit6AVQ-StdrI4ml_BtJUIOWOC3_R1pv5Nx5OXdZ-3KAU7LNwAgSt029DgvTrb6mCcjPSkLQLFBEH4bjxm1KlCc37pUJnunXOdP7Tdh9BZ3A0Ci0Mg6V68V3OVdwaOmIjK42qqaFMlyWTucWE8Jtcsav-v2yuB-QB9ycaPLCVayWJKZq8ffYv4sccZooHiZGMGDDrMjo3iY7TWjF2fIF810VUNEMPGlJxZB0kddSiUbvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22712" target="_blank">📅 16:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=uRFpe3p019uoZvG0dsdi2_WsYWL60oQXjLaRlVbOxHG6DBX714b0fnjRWQNopY3cpoWKSs3YECRcx38bMxTQ_h2eFz4qsAjxoeR43M-Alq28JtZY6LaEPora8b9pmQHplk8aAx0NPrh0frFxWa5wCPxaI3iHqWLBiC4WjdgTSYN2fulM5lUUJ-0jIOWksC5cAwALnpjQh1-b2CH9uS5o_dZEA0zcTxp9U0RGoNlYsFz4cn38Trg8-Lu_9yVEYHXQm-HP1b_-QPinbouZAakF_tFZIQUH4x465x428SdcAeovm6XoUBKXv6c03wgYcmqD5n0z3H8YJUbyukUQjfDMjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=uRFpe3p019uoZvG0dsdi2_WsYWL60oQXjLaRlVbOxHG6DBX714b0fnjRWQNopY3cpoWKSs3YECRcx38bMxTQ_h2eFz4qsAjxoeR43M-Alq28JtZY6LaEPora8b9pmQHplk8aAx0NPrh0frFxWa5wCPxaI3iHqWLBiC4WjdgTSYN2fulM5lUUJ-0jIOWksC5cAwALnpjQh1-b2CH9uS5o_dZEA0zcTxp9U0RGoNlYsFz4cn38Trg8-Lu_9yVEYHXQm-HP1b_-QPinbouZAakF_tFZIQUH4x465x428SdcAeovm6XoUBKXv6c03wgYcmqD5n0z3H8YJUbyukUQjfDMjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
توپ فوتبالی مجهز به هوش مصنوعی که به تشخیص آفساید کمک میکند در جام جهانی استفاده خواهد شد. توپ رسمی مسابقه می‌تواند داده‌ها را با سرعت 500 بار در ثانیه ثبت کند، به این معنا که هر ضربه به توپ تحت نظارت قرار دارد.⁩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22711" target="_blank">📅 16:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO9-4nf5icscnuPbA6HlhRQ4YDSPzG632jb9HuzUhFpXu9HIcRinVAlfChxg_6bnQz_Vr4gm3dfN9O5WWQ_eRbrqJBoOMUelc213oLxFPFT_uONyZPQeZcWG5WRNU-f7Yq_wghFLMVvq7U_ziGjXU5d2PvyLlbUUatuKX6Oa7kpLKtjwTll0OpK35KbF-fWVqTuDnUGU-vCjWH9NA-fxlNTD5gWFPrJAi5gpegPVvM5JYPSOFxu-Ci_FsfZaK0amvIhzAcQm2KePWbjvgy8B42hn3G6OEhXz6CO9AcS6p7plZXbVUOsJVKq8GFoqaVCXMW75n6hDia2TUj6ESdIBQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAt-u6Hkka5jF8sOWjKusL_kjLalC1FLzPPj6IsjkmDlK7ifp1Oq4ZRpVonERrMDU_ECMULI2NbJRgTZRliyP2zh2sYHDg0AqWAMhr1Tpdotq8QmxCtgDOuXaUiHxeImVh0w3MSaBaJA_xPeOK_ZgdcxzigiHPKYTxFVcXkSSweDipnXVyiMWwARPeJo3sHHWUQufmML6dj4ES0G2hg3xmCyw-S6H8Q8f0cP1hjI8PnRMGGOTVldg9p3ix4S7iEBqjnnLlCTwMj9Mxzinuyx0ARM-EzByNAaob0uyVhGwExGoZFWmVQXVaEpBOxJmAncJAkbzTdfEFJAFdTWZfwEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFhAH519N0BSyVrM4Qnh_3k47jYZPLRErdDk4PxOuelFSRk3OHzjSgTRBWKYt4OKAv1GzCnc_dpJcWZEy8RcbB40hiMUTb5GS6n4dtWHft4zBZ1zPPEJWe674dVyHcJLF8QXHyX8BQt1UPOaqTbXoEy1RsHYaKQ8vF3KIDeCTzpNRZzMD5X5XddA36ObiDkQhJvB3PyEoZEfBwEOaBAUfSppW-loRjhEgaIaPHPjaJ3hGqkZ2vy_rz7tP9dzXxzLg8-qQaHdnZewf6OeJMWoIidcZzKSeQDY6R-rUvb7nHJ1Oq1m5xXhRgXUMSAWlpsMdHWewL8jPchyHwY-t17x1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaX3xGWvN1toU4IA-hkxZsLeWPjjEpyubiA7Qn5VhjrTh-SDGxXpXKoeoegsDoJitp6M0IzL3BKTmRKnTXLSrwchah-E5cIT_MPkADNO3Fdzm86MhQ1sYz_NiiCXThNMyGWJp6EM5ptgpe_7-kjf1Uyn6BArRsVIRvCmv84akBwWQBew_q6QrKTQXLXbIxWjiKVJxK_3q1sjq1knlmyvydO7e47w3Olwlg-Gfzq6NSU6-Bth6sLcahquiFMV2aQPwRrFNMZTsN6z7sEMwcgofU-CiYokASRtIRQ7gBu3SWSsKZe3dmI5--U83PcHJRs5HWKH1DJeTKSBzx1SVMRSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
راسمون هویلند: امیدوارم‌که باشگاه ناپولی در پایان فصل بندخریدقطعی من رو فعال کنه چون حقیقتا دیگه‌علاقه‌ای‌به‌بازگشت به اولترافورد ندارم. برای من بهترین بازیکن تاریخ کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22707" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mjmf5bqPetibJIZbXBcZP9sOJE4P5BhuwVAPrmwXieDlMXLPc93ffpg2wbGWrb08myMyCrL7OqMda4fKdyBZnSNBg_QZXllMDTICUKas0YvGGtQwWDk_jcUVDTbG2H5HqGjEo4NXEtUHWHLDXiK-FMaF93Fwn7Ae9IC8Qewlh4_HCcqrlzKdDYTBx0k8D5p7bRunAHtTaUkF8Ks7axMYeg8tfeDexfUVrDu-4pqjLQ9bNXERjZEKhpLGyY9pv5ZWBDO6ky3UApraGLxOQXMpnTinBtwzmqHBGbvVtjrofTrrCW_oSxfdKGf84gLi3ysYN9PkNpr6pMSwg0lLOGZpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
#تکمیلی #فوری #اختصاصی_پرشیانا؛ یحیی گلمحمدی علاوه بر دوباشگاه‌عراقی؛ از باشگاه تراکتور تبریز آفر مالی بسیارسنگینی رو برای سه فصل حضور در تبریز دریافت‌کرده. مالک پرشورها قصد داره یحیی رو جانشین محمد ربیعی سرمربی فعلی این تیم کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22706" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=pRlvoR7j8GitUbow65vqop3rEGLTcd4Srx1OFXPcXiQGyIOzAKihUxQVRv7Yx2z4VrLceC-n7Ofc0tin-FhInPeNYXColEHwu9wfa4BpQRMtP2TKYbGFztGfGVnOqPREQKEL3W713K3gCJV5jvZXXBwN7aL_Jr_AuGT2X9qUG30kMSQq1OJg5UpsAeEJgWTVMPVNLZQnGhh5pXX1uO6bIlfzrPf_h3EnARl_WDFEzciFx4pcwI1RDt4mdXqqXJe1C6oqEjeuDGF7I6pho4W5Q6Vn7cM6ah9GNSirPIWV_K6k7C4bFAsq0edY1btWO9PAId_WRiNHcV2XDMgOr_aXmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=pRlvoR7j8GitUbow65vqop3rEGLTcd4Srx1OFXPcXiQGyIOzAKihUxQVRv7Yx2z4VrLceC-n7Ofc0tin-FhInPeNYXColEHwu9wfa4BpQRMtP2TKYbGFztGfGVnOqPREQKEL3W713K3gCJV5jvZXXBwN7aL_Jr_AuGT2X9qUG30kMSQq1OJg5UpsAeEJgWTVMPVNLZQnGhh5pXX1uO6bIlfzrPf_h3EnARl_WDFEzciFx4pcwI1RDt4mdXqqXJe1C6oqEjeuDGF7I6pho4W5Q6Vn7cM6ah9GNSirPIWV_K6k7C4bFAsq0edY1btWO9PAId_WRiNHcV2XDMgOr_aXmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تکل جسورانه تیاگو پسر بزرگ لیونل مسی؛ این چند ماه که اینترنت نبود احساس میکنم از همه چی عقب افتادیم تیاگو کی اینقدر بزرگ شد، آخرین باری که ازش ویدیو دیدمش دقیقا نصف الانش بود
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22705" target="_blank">📅 13:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXgTjAeTpQjyeWIi1HdnbInM46tXTebLiz1OdSB6x1wgYd6cItzD0-i0CzkF0bNwuj1MGO2TXl79v85vB2vc37d5DSDURi4V6smKFwgUhGTkbHsAAJwPOv6wrC_j50UN3xt0fY3A6i3GutzkiuhCB7776tYqBexWUR0OoZ5xLsNgqKUSI-qNvvQZqoZBtDf7uUpyiXidPsG3UT7UhgTAAN-dipY-3ms-qDN8OEa4A_SOf3OX39_4QDPqsJtK0QA1AuNIC-PDnHMLPB0Ou4qwaMoEsd2j1ZMjnjWwjuo8I15S4nPXYoNDpUzACbU8s--5gre0oD0qIeIedXJyVWxqVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|رسانه اسکای اسپورت: ژائو نوس، انزوفرناندز، یوشکو گواردیول، ابراهیم کوناته و باستونی‌فوق‌ستاره‌هایی هستندکه‌علاقمند به عقد قرارداد و پیوستن به باشگاه رئال‌ مادرید هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22704" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smGPLllCbEo2fZaol9h-Wd3ohTFH8XASKF1hfOXpCRBcsFCV9dAZStHY9dMbjYOVNlOlbQKo7k_HJboGBA-bCRy8OIiR6hRfK616FvhFg_dQhQt6zAyytcFMOuTwwoN9fi8ifU_sFslmF78F7aWoubd7FhfZ1mtPPSs2NW9pvQWewZynP3Gh2_F-ap9xJyvTT5xB1pHCYli51V-ZKrvW8M5ng672vg_8qLTHv-WgcuX0v7j_rxd9CgrVzRi-IKiNQ7Gf2DftwpHEycT7I6P0952MMlovsF5Y_uirda7l0V_cx834s07d-7DC0uyhUPW9v2kqoE1ufcS2TpHMvAjbdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌پرشیانا؛علی‌تاجرنیا رئیس هیات مدیره استقلال تماس های اولیه خود را با دراگان اسکوچیچ و نماینده رسمی او برای عقد قرار داد سه ساله با آبی پوشان پایتخت بعد از جام جهانی 2026 آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22703" target="_blank">📅 12:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8Eg-VnK6zXDOTRKaPv4By0BFApAs_5dLzn3rh68zGa8YrMFccpJ0ttIDWAl58jLNBK6li7YsCCN0_thpyG1-HqLAa_TBIzY40QbJkAZtXh7hoosoeskV6NnS1cI-YQYH9qEQF9QGlbeRygGnphJmw44c1Un4hI4Mg2y7QwIE2_v0H0bETLv0XxOdi3KZba0eL4w3C4OyVhyWgdNfUHpCGqohJ0prQokO5hec4kSke-lqVnshTDtxhB8bWMTswRoEAElD9k7Slu1jszfDzHDdi01Rbn-GeqkB3b9sfUBZHNiZm6mWdTuvrsJ1CEwNiHJpnJn0dnHRlnl68fuO7M2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری‌کین‌درباره‌تصاحب دوباره کفش‌طلا: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22702" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDIKvYVL8GwvHHh3-nSyFxv_4K8BljUEuPkzmS_cM8EVK-jKbSMWk4TBxYgzjRssDjMQXih6O-lsfrre1YaRDuwEpUAApliePPErNNiZ91AhTw6iQbdp_uMAlCL09IT2mD2u5UygFFI5B8LOs0YSurmSvUhMtv_XKzI0kYyAn541j1muFd_pRlVjRnIvlEz-5vPtisJmISpOIx1TocJnIt3KvJ-60_4K9dIoMlMWIF8Pky8ysA7lbL-QWAMi8iyT4M3Q3Sfl-MzFG1v4Mr7u5_Iop97NV7o3g1Shr4dJ7wo4U5iTGmkKJFte7AreNpyw73wsbDnIBfcG1LeIb1TxcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن
🔴
پرسپولیس با 6 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22701" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=cfGNi8eYBk-_0I3CixuwOOP13kZwOcfqT85g5w9JY2Mw4nZpO6ajyczRTvfD7kVIK9gvdzOIdAD5y8pJCU068eCYYdxLg-oSMHww5mBlRPqZjXOplUm7AYnlPh1IANCeybLXB51JwPd9ShfjMVHKzdC0i5w8HaA8K-YVJRLa6ZkBUXttswA_eUB2Sl8lHQfaHpb5hU29aPgPfDgMtQQCu3QTBC2-l0CtuLx_2mxdWFRjBXEz5SnxXN0SmAKBxOZKxoQki_SbcpaA-8m2CThTMUZMpUgTVjH0WAPhwRAGd8pqOKIayFec2iimmXCoDOUtTUPmzJtXeDR_GjNEuK7S-U0dtjYcIdMPW0r9vaUPeZhzx800jz0nfREGXgLbqJ3JvpsNhhJWLv9juv4cNxDrWQnH6nPs9ycG-aY-3XUPMxiwdsBC52lKApC4eOuW8_2fVd_LeZxWdZk76bz_TIrdZL7Y8CujroGw_UKY_pxjsGcwhiksFdtwnCMbtWGeSXKNGVUSNaKDOqFZ54k823NRx77MF5w6RwCBLxE50yCVFts6_4axEP8zcpp-858I469A98t6MqbfHGVh3BGyGSVVIY-WkcoJV3g6zktHVURdTsmZAn_5yNKidd7rieGcKxzlJ-wjJk8Fd5FRVAGEWqtCcqXIVtauPV2HYjtpEhcGIYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=cfGNi8eYBk-_0I3CixuwOOP13kZwOcfqT85g5w9JY2Mw4nZpO6ajyczRTvfD7kVIK9gvdzOIdAD5y8pJCU068eCYYdxLg-oSMHww5mBlRPqZjXOplUm7AYnlPh1IANCeybLXB51JwPd9ShfjMVHKzdC0i5w8HaA8K-YVJRLa6ZkBUXttswA_eUB2Sl8lHQfaHpb5hU29aPgPfDgMtQQCu3QTBC2-l0CtuLx_2mxdWFRjBXEz5SnxXN0SmAKBxOZKxoQki_SbcpaA-8m2CThTMUZMpUgTVjH0WAPhwRAGd8pqOKIayFec2iimmXCoDOUtTUPmzJtXeDR_GjNEuK7S-U0dtjYcIdMPW0r9vaUPeZhzx800jz0nfREGXgLbqJ3JvpsNhhJWLv9juv4cNxDrWQnH6nPs9ycG-aY-3XUPMxiwdsBC52lKApC4eOuW8_2fVd_LeZxWdZk76bz_TIrdZL7Y8CujroGw_UKY_pxjsGcwhiksFdtwnCMbtWGeSXKNGVUSNaKDOqFZ54k823NRx77MF5w6RwCBLxE50yCVFts6_4axEP8zcpp-858I469A98t6MqbfHGVh3BGyGSVVIY-WkcoJV3g6zktHVURdTsmZAn_5yNKidd7rieGcKxzlJ-wjJk8Fd5FRVAGEWqtCcqXIVtauPV2HYjtpEhcGIYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استفاده عجیب از گاز اشک‌آور توسط ماموران در بازی این هفته دو تیم بندرعامری و شهرآرکا البرز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22700" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22699">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22699" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd3pcRpv5H6Mfc55hF0PKYlvjqVnGTf93bQASDJ09km9hVhyFn2vjEtKZyZVCzbcrtustjIuSEIAYJJYaqCakcsGjdfyhH_jKD6ipD-H-iC0lT_A97NzX8D1BrUn0SsEpQrx6RBCyLwgv0uGGah0qxW8mgjVrvH8Hf-6ISMjpnPIWgL_kYPsqUGtRvAHuzcCPBWyogTlDIoAa0-ZEgj822ecclEmOElRuuYSc-ULT1u6IJ8EoY0fFVf0q-UtGuFlTAp97zJWxYTNvNOudy1xsonj4kGcWi-Q8LTYpp2oG2dsvoWolyS1CjqiKvTGT4oAA64e5I4BORGhYZWW58A9cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ دانیال ایری مدافع 22 ساله ملوان اصلی‌ترین گزینه اوسمار ویرا سرمربی پرسپولیس برای جانشینی مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان در تابستونه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22698" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خلاصه بازی سوئد VS انگلیس؛ بازی‌‌ای که زلاتان یه سوپر پوکر کرد و اون گل مشهورش هم پوشکاش برد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22697" target="_blank">📅 10:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6-_mjC_aP1qcHNGN1Q9n--DWU8NWP7GWBTuqtM7vghy7DG9eUd7gaZwdihnY9BIGWYlDYvfcfVkuPIrMrrSSvm1npLOH_SSftQQsuMFVTlWH1gwgxNOxub08F4pj-xNRcO9LDvtq5GjKWo7CgUf4PkSNwuW15VLwDT-khRWQopuIztqCRtEDZh3E2mTalYwy-IRrpVC-oOWgIS4h12sJ0zDBBbCY5qamAAwQ-Va4H80wP78dc7yc0MU-bBvt8jdnj6h0QQ1cNxDju-S5sdoxULDgZE7-htY0SlBxa4GSamTKfRMebZBm12Dl2SrG3ghw_Lo0-LyXc8Cu0yN0deBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسکالونی سرمربی آرژانتین:
مدعی اصلی جام؟ بنظرم تیم ملی اسپانیا قهرمان رقابت‌ها میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22696" target="_blank">📅 09:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViwDVVTofW-QyFaCQspQZe94UO8ZJhHbRINBLaFJxa-ppURfzzulmCi9QnyAT9G-20Y1Eo2eyTrCGrLlhL04qR6n4ogUxkrJip4KzQumUc0DSkzkhPoq_GWuPbF4aDUwi9E6SauL5Of-nqzjG9Us7u6F-d0nJ3xorfDF6h8DZDoOews08Mzjt2DKCvDxOhZqaysRcWr6B-Bk6c0_1844bwzTD9PHrB7Oky05tVvdu7r8zJC40mV_soPNvyLFgT2mIqz4sFk3Jr0qXG1HSZtv0hiAEm8PpZzjLQx573wQs1X_oempw0z-_F4EOSKRPbKD79FdtFhevdI4vq-hyoWgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUi9mXzx42-g2G3gpIO3eSlO6XmRjk13FOg6mAlRzKEP-FVq6GEEDSTrfktwCNnbEVcgPNe1lpTgR_Uxab1FQiWkIAi3gkEJ9s0M-pifDjWa-EY4ym3yOw2y4hptpGFDV7vky4s3Z8MFpNq7iLmC6_MSrhe-VAdnPn1CG2zj_15NsiNWiDuJfMWjneerSc7lyqZb-FWLA-rfdyCPFdMu12HFK0Ee2pS-gP52KllomDvq2QqP2pNT56gZUm31VgcfFciUve7y5gW1ZHreFlSNGie8Vz-N_iNRr9rX3Fw1qqUION98HBhssDUlQ5hoFo0vOmuJU0Ymay5iB-90NbSsTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدار های‌ امروز؛
از تقابل یاران نازون و کریس وود تاجدال دوستانه هلندی‌ها مقابل الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22693" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVPfuDroZ91pwmaVFRVCK0clACo932gQTe4HoC8sK-N2K960c86iuJ_Bzyw6uNmUa85q6eTe59L9gqP9FRASet8DyRKnva0N14duoiD8OO2ymSpmsWLnxEfFP6nuH9S_EIOo8IJoVCJKAAo_NA73m-eD21gmptRRJxs2TrTTYh7tgBxo_fZxIMBuSui8P_IQFwKp7y_qvp1K5Ri3H7M5cxguxHfGM5Db2NGgRgDV-y1AvTmsZZi-QLhEW3x7a874g-LUo2uDViMeGGypj3wgTzYQMwGiqSsU2Zrfx_vhoOGxffw56t9R7aVxOmIe9xTtsnDw0Tjex0AiD7uDB5PEGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست‌شاگردان کاناوارو برابر کانادا و برتری بلژیکی‌ها در جدال با کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22692" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6HEM-ixABX2xogG7uZC5VDgQXBpnSeHmgZ63N0DubowIqSfdebXYJa-VRSzMqpXG4BKWywVTkZBMQwREqywS7OPBFcZgVAEiDCUEh1cdIANPQZdS-_CG-kKDRAysJ-NAB-2KIe43oZW1e0k1LzzJEIHXetpLplei2gyidOd6zmmUEi-CJn0Lk2-itCCDD-vbjAxxg-q-r8R0QCHc9LzPmKvazU26cqJrNj8mTgREgztVA8XXIzMAXvTep_EyygXIT7PBqrJiPxpZVdOVlX9mgcmEfVX4bQPY7DEHlbH3RNDGLEjuzYsh3I888DL-Limoty-Uof6DUkaodYThAWzwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22691" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0TjJvuq7U9fUDOCYOO4TmZtbXQe8QOKFfJpTXClRYqDdWwX9xwKNwYeDlAu0sv-gSstHfffqFxMX6scKBqLGIB05TC13uQtu1pO5SlBoPm-OwT0RnK2QOFkZ85b51aMPum3aONH6wn86I2FvI95-FfaK-KnKMt0pYG9QCRXhKPZUb4xJ5Vk7caSU4UBALHyHUbzIADjeWbQivsT12prfOj8VNnzHvsykggopLftbKwrJf0V0uXGindtEtaBFnfVk6yg5cZjVs5ZoV9FSpUOgRZ1C4UOLbbXkBsoSJfNDNT4zo_cfiR8_VT-LkRdl0R627Nqn9sN6ERJCSv9ZDPGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22690" target="_blank">📅 00:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=XxHQBUw0D4R-S8mXdE8X64JS3TD4gv2l1stf-juVMl-ZhnTsc0nb8vWX-ObOwV6k6yQbzMGMJqxRhWue2kO6VH130WBSBJZQ1pgOfZoIVulKMC8Xlcl7ibZWjeHuZdp3_ifVwUiWdS8abStkBlMHT7z1SRZ7XafVzbOhBBSXCi6zCRJnagXFCQdkdaT34Bfr67O1nuC0kVnH_WC4LdbqA--gJGuUWysVAsrmSR9ShLyjKDjoVxx5Sg03ry9n6I6m0PbKB3SeHs27pX0hj_CluGjcyYdSsCJwh2GGs6QAzY-gbPs4F4XG7APjWj5-GOMq3pJKAROKGvjGoOeTAsbIDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=XxHQBUw0D4R-S8mXdE8X64JS3TD4gv2l1stf-juVMl-ZhnTsc0nb8vWX-ObOwV6k6yQbzMGMJqxRhWue2kO6VH130WBSBJZQ1pgOfZoIVulKMC8Xlcl7ibZWjeHuZdp3_ifVwUiWdS8abStkBlMHT7z1SRZ7XafVzbOhBBSXCi6zCRJnagXFCQdkdaT34Bfr67O1nuC0kVnH_WC4LdbqA--gJGuUWysVAsrmSR9ShLyjKDjoVxx5Sg03ry9n6I6m0PbKB3SeHs27pX0hj_CluGjcyYdSsCJwh2GGs6QAzY-gbPs4F4XG7APjWj5-GOMq3pJKAROKGvjGoOeTAsbIDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22689" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGvdVbWRSCoonzHPNd7fgUaV1_fZPzdO_Itd0FT5oWixrH0Z1abHIGwt6_DeIhtLwyMLci-Eiz0q9crn-2tUQlv2nE2LL2LFRBhv8C7WV1Kyzl_A6cLB3aVqie_ylmq2t6VdIMnAVXIaYeQ_ffRj8m8AkppW9WWXu-q7m0egBO5yuT2ZrMTmjc7TVTQ8LJKzYzqn1KNSlAMcfOp4XkGxe12sIw-Q_6DKUo7rRnjW3eFCoof_WyR9Mk1Qb6jhIlVwAn0tMZn_7zYFUiGe25BfmeZwacqaL1u5b6Pu6pByvQ5b2zYuyWJ6kXI_ffvsmxdBrlFk8X3prYu_RG1qTc1zKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رسانه‌های عربستانی:
باشگاه النصر بدرخواست کریس رونالدو پیشنهادی سالانه 85 میلیون یورو به برونو فرناندز کاپیتان منچستر یونایتد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22688" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uzwoy9dsZOVrCQtpb-zomaNoUBpYXuCjWgI6YiA_P7u2CaMSzmSv4OQD9jNTjtQZ-UEzDbaYxmP3ZXqNJo7rnwvi90M6PkOBtby0Zhq8p_sgzgAq2SOteeYtuGaXbd8xcWsePlebK365E4LJdf6KjctRgFfqLC7V5R-we5h2Oepo_ysrCtDBCzg9rV1WGTPiHSQslhokb3Ln2XN2YNivoVMHXyrGfSZW3u0YVY7PbdJ__ajvHsOBHoXkSDRcqxaQ1nmwBhqMG48EYAcamM6XfqhfXmBWa9Wgn0EhhpbsSYTl9ahht0e-fAjpsXsnYTinYRpB0DG-teVqe7AtfmVJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ملی‌بلژیک‌درفاصله 19 روز تابازی با شاگردان قلعه نویی، با نتیجه 2-0 کرواسی رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22687" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4e9pqHdzD9PFVsiAhYCg2xNNVVCP5slX8jxGAcbXS1p8xBo1skrved4u7FrZXPlUbjBM8Oj3GWcG7ApP8KU6WhTzrXrCfdVAauOwgWZxWMTG0aWA1-GEOpiYGsV4wSg4A9JbQ5xw12s8K_dl7rJBGTV1lkDVCMGbYfpPeepS_svaDqnGmA8ZnwVWMneBm2EgZlyOBORyXKNqw-uJIO7Sv-y3MUg8XvZVNjBCZvfrO6xqacSg4jOxDZ5X1KKb_VD3FyoXaTwFhSOvHlUt2tmahVDdty9l2_X5VYUQQZN_LXZrVG25-F60vaENuvX6F9LwNhT4DsL8USyIYvvn_GORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22686" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=AU83HqH6-DR9hwYeSBoe1Nykp7ARArKjQ9Dm6izV_ZHsPVwk123IVye6HCWJVzXTzgIcfhJV65rHyhZo-libTgmZxXvXp_1t9t-4AhAKHj3fIs1dg8Gh7kfOhGYF5Km6hvE9Gl96ufQXluKL2bMj0OO_8cyGHJn6f4TS0Ah92MQObA4p56_eL_RTpSmxXkEdTWv_uaCykJAiMfdQDiKXFVSyuldpkDVZIYngeGhdGvXe4iLEGVdk5Ts-dhgXbJ3CAjOhAXEal7MDAkfKbm9cg0w00410-28qnvf4Qz_cF40QPIxYM8RpHpVkQ7PSFk2nGl2d_lwWx90g5s29D3dTyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=AU83HqH6-DR9hwYeSBoe1Nykp7ARArKjQ9Dm6izV_ZHsPVwk123IVye6HCWJVzXTzgIcfhJV65rHyhZo-libTgmZxXvXp_1t9t-4AhAKHj3fIs1dg8Gh7kfOhGYF5Km6hvE9Gl96ufQXluKL2bMj0OO_8cyGHJn6f4TS0Ah92MQObA4p56_eL_RTpSmxXkEdTWv_uaCykJAiMfdQDiKXFVSyuldpkDVZIYngeGhdGvXe4iLEGVdk5Ts-dhgXbJ3CAjOhAXEal7MDAkfKbm9cg0w00410-28qnvf4Qz_cF40QPIxYM8RpHpVkQ7PSFk2nGl2d_lwWx90g5s29D3dTyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدل‌های ایرانی لئو مسی و رونالدو پیش‌از WC
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22684" target="_blank">📅 21:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1ngkzupTfnnJbWxqtYE31QOdjGuDgSbQ6GuJlfdNUFBTvkejpzYJ-n1SH-yc7L8tfIRLQGKbIuiv_LSZkAkKESiLf1-ivgHA4Ya8oiAHPX4U3apeVew_38U4S74BKAhqhd5iDY2w9C4kwJTC3GEXI9190JsBiv3JPhJet0xyGLqq8FSCNNxukxZ6LAnoG7N26qO3s2CN0R_778YXrV3wrHttZSOzcKprBMS1Coc1CunT3oEpJ-7irZNIgeewsDvipUQG4y4sIruizRhnNbORimtba3H2G__yu2POyHTA9B3GiYlVyMnMfxkvThWSAbg7i6Sr0vFWi4kp7Fl96B9mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=FYLj6lMx8sVxDA48Gcx5-4S7ZhlpiKOi_zAM73bqm0WzTm6Rqqrlw1VnurZALLZKZrLmz83eITHP1RIy8Fb2fyXUgKYHVJoh2NabAieMfSTuEFQbI7BYmu_Ult_p4_a96xdM4ijUo2i_7pPbO7ZHrc7OAXjG1qBaehIanhPWTAME4yH09ZGNalV92PSpyJ_G74yURojMT5HDA64mU1WQtyAxh3znpdzqIIn1_374G_Lwnv578hGBA-LF5boG-dR_hAYozToEnHHylEkMbcZaV0Eor6pkRKW8LxSa4ukddaIse_A_6ZjCjNTrY27M7rliOtj7d7WYZfo806b_lgh-Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=FYLj6lMx8sVxDA48Gcx5-4S7ZhlpiKOi_zAM73bqm0WzTm6Rqqrlw1VnurZALLZKZrLmz83eITHP1RIy8Fb2fyXUgKYHVJoh2NabAieMfSTuEFQbI7BYmu_Ult_p4_a96xdM4ijUo2i_7pPbO7ZHrc7OAXjG1qBaehIanhPWTAME4yH09ZGNalV92PSpyJ_G74yURojMT5HDA64mU1WQtyAxh3znpdzqIIn1_374G_Lwnv578hGBA-LF5boG-dR_hAYozToEnHHylEkMbcZaV0Eor6pkRKW8LxSa4ukddaIse_A_6ZjCjNTrY27M7rliOtj7d7WYZfo806b_lgh-Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی‌جنجالی درلیگ آزادگان؛ سلمان بحرانی پس از گلزنی مقابل تیم نود ارومیه، در شادی جنجالی و بچگونه گل خود حرکت گلر حریف را تقلید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22682" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA9Mi-PR0mkiP8lX1UH66FwxOzh5_wycWKOSl5udA6P7v-FQJjKhgtPFrTX3r9d47uPMuD3uGZJM1g8el4aaMDIrHkHFZY7LOAUltt_ro08wRCKL78QQjAR6LSfqVlGZINqAzMqtgxznZ2Tk3HGF5ZE34Fu32hMHWqrx8hfLEtf9l2gq3vZYyjesxPIx0-_PHMZ7ZA2-B7SNLGLv7pcbNmAEPnqdm9Fbe9ivElLLqlOvMR6ujh1gX0I5GnTY0Vggpe90K64TjlYW9hady92zm7HRs9MVZii7LBgIiXZtJvXFO0LR08E5p9-GRgHcpGljP-8ZkOx9CVzqvM1u6ouUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو 25 درصداز سهام باشگاه آلمریااسپانیا رو رسماخریداری‌کرد؛ 7 فوق ستاره‌ ای که سهام باشگاه‌های اروپایی رو خریده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22681" target="_blank">📅 19:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=OvDCgWWIXSPdycMbDoXQ3iQ7Fnwiv1tIaE45_YmpG9W2E1lJLFL1BZyMO9U1CvAFzsT1250JvpyQPCEvrbb903PVuq4BmTStn4lJPKXLIa0Ft_8wgarosa1FMHhFMxKV7Ju9ZB2_nDIBcQi8pntTAqFu9OKCCCMdnhbVaPsw8Mjd08QotrJdz0JtKbCWcDLwLcPV-nF87wBguII1iQoctyUB2jrHrYcgigEAlvRn-lG824yXOVVrfqz6JiErXxolwyKd5ZqxxJHTOYTaygmOnhZYNCd6tm1GR_--5nZW7PGDEPHI0Cv9yJ1MvfdSqghT_otPninVKFpCXILDawfbeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=OvDCgWWIXSPdycMbDoXQ3iQ7Fnwiv1tIaE45_YmpG9W2E1lJLFL1BZyMO9U1CvAFzsT1250JvpyQPCEvrbb903PVuq4BmTStn4lJPKXLIa0Ft_8wgarosa1FMHhFMxKV7Ju9ZB2_nDIBcQi8pntTAqFu9OKCCCMdnhbVaPsw8Mjd08QotrJdz0JtKbCWcDLwLcPV-nF87wBguII1iQoctyUB2jrHrYcgigEAlvRn-lG824yXOVVrfqz6JiErXxolwyKd5ZqxxJHTOYTaygmOnhZYNCd6tm1GR_--5nZW7PGDEPHI0Cv9yJ1MvfdSqghT_otPninVKFpCXILDawfbeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پست برای رفقایی که تمرین بدنسازی انجام میدهند. بهترین‌میان وعده‌های‌قبل و بعد تمرین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22680" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEtOQgcuXm9cqZrQ5tPMJ3Cbfd6lwkm_3uNx3HE6ZDT3uimLsX8kXQgYfUqgDBXwWeAtKrDyHaNnlxnCIrJcM15jstebZfw9iOtBz-RRWfGuggkggzUvWmzFU_ZJfXrzmliShGxg_CDwF2wU8K0Z6ASwwCI16U_sRK-BdEf8HqhfMqL3HQd7oRBghe7MJ_lmRZ3RY38MFV9_MtwnJG3veWTm6noOl_BNtmXdthXfgNDgLRrrp0995eHpAcDT9mnz7EBCcN5L_5g7uNyQh9m_uVwVkCH0_5OFrZBTLwJbscmr62nGzAX9UtYuxHVTD8AHYoQclGrek3MbU_N4p79KcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام‌رسانه‌های‌معتبر بجز رومانو میگن که بعد از ابراهیم‌کوناته؛ خریدبعدی کهکشانی‌ها برای پست دفاع دنزل دامفریس مدافع راست اینترمیلانه. ممکنه بزودی خود رومانو هم هیر وی گو کار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22679" target="_blank">📅 19:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kdof7Hw41i67QeG8P0vLp3fIVcOttuLSWayTJAXyWnAImsLGHqvJ_vTU_jNde66dzy2iTvvM2yp29sfDcOuJXJV9s8lzyIwjv7pl7co8PaRT4WBFx38uHUokpRSUy-tNu_5n5et2qGTLXLDCuPXuFmzjSd9xUzLPdQdyt06W-h0jbxbh_M4neM4RJKUJoKO3_eAgChpWwyD_FVIfvPAuQYidXV76uMSDSRZY4cT8jqVajbz-4dzOmoy_7QG1H6rTkIj2ImGPpj1QfEdJkzklnm0JHNgxXNvCmC2TbgTlFqpy7o9aUvbrXXnLQ5YFASp98Gnp7K1yzNL5WaYq3FDN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22678" target="_blank">📅 19:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGC0SpSFQVOtsTD3unkf9ieuI25truksV_kfr0UYSkKqn_tQT-dNMhDsWgCZBXqtnbNqUNBUvQCaRxlrgs7bEP8ULjq9sRYvifGTlEIH12QItILh_U8UGJo5FCgN_S-7t-NSIUhSiJeLqBisq3ziOACP6i7Juj6jgRor1pZzAX73ctcP3-cdGe90DqLdHel2uUr92bWjFKAsJ6NzZKR_0aGR6N3ijQ3u8sAoeosMmf1_CCg2vHo4YfgExQs5K2lNxrh_VJXvGoiRzHBbsKlQ-AjhfysLQI11zKJdfUTOSHuQj9YwJAsKYu5k6mH0kWw0AgUKuEZPMHE0rvTGkCEThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارفوق‌العاده ویکتور اوسیمن ستاره 26 ساله تیم‌ملی نیجریه که درتلاشه در ژانویه و یا تابستون سال بعد راهی تیم بارسا شه. امشب هم عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22677" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HV1oAD6geRPr-QdtaFPytgFOx1_QD4bMt5YNE311DTs9rN11vRbWVDxb9m-wHS83sBxoYaEsB5Q6aWHU6PTr0AgcJB-a-KJkY-gWXb_D8HymY3_KQV6a-b02IwVrpQTTwnVF1CRukcETI0IZtR1TSb3BZFQEXIO3wRwmKekX5cDq3NxOIn6NNq5o6RXr1z7wTqZZKgwR0tgFKhNBLl3I0F6kPFnFHrdRP9TPumZLzgFAkOxpNBVUa4B7NxohXq6h7XFwXAe7KinXVX_9mPiiUM-8VhnbJWur_EsOTMzVcHmFcqsSEjEf66Di2M8U6YIOdTrmLAYoJnhmUQYbpZJs8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام باشگاه فولادمبارکه سپاهان؛ انزو کریولی، مهاجم فرانسوی این تیم از باشگاه سپاهان جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22676" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=bwHw_TPcjkGjRkdNkI4yQHU8tqu1ysjNPF-cRMrJ47T-Ez-7IH_XbGqvmTfd9bQu-tWYQba2t3MS6qxdJ7vJ_xR5A0hjywBjDYb8UsaowijbW75ppXGCYgEFH34voGu3zju7a4obY717epipLLjG4x1hbWXjoQdeGjEPiYGDGvma4wUeIgkerISK8V-E5k7PDctFDIdEePky4Qr4cKFsyuUNITWijfplF3rXKx4RQyFDfQjnDNaY1wpcXhBU8UOxr2I4n5F0MuZjkAAe_dwqO4DVp62-OWFI3AxOaLWBJCp1lcJ0vDl_GiWAaiaxa1dcpobRGUNDr1OVGdZce0jgGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=bwHw_TPcjkGjRkdNkI4yQHU8tqu1ysjNPF-cRMrJ47T-Ez-7IH_XbGqvmTfd9bQu-tWYQba2t3MS6qxdJ7vJ_xR5A0hjywBjDYb8UsaowijbW75ppXGCYgEFH34voGu3zju7a4obY717epipLLjG4x1hbWXjoQdeGjEPiYGDGvma4wUeIgkerISK8V-E5k7PDctFDIdEePky4Qr4cKFsyuUNITWijfplF3rXKx4RQyFDfQjnDNaY1wpcXhBU8UOxr2I4n5F0MuZjkAAe_dwqO4DVp62-OWFI3AxOaLWBJCp1lcJ0vDl_GiWAaiaxa1dcpobRGUNDr1OVGdZce0jgGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی به ازای هر مهمون پنج میلیون دادی به تالار چشمت به‌پسرخاله‌ت میوفته که با لباس بارسا اومده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22675" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jib4kiqHS09T-LXOKQvLc7ElSFZYOoqT7QIoHn9KKoT_bDJPG_4qNYgJfavAzNk9Bx9NdzR4dnQvBuH-hqqLXIaxn9itQh-8li0v2NOSpBYz9R6USFdpBYWS9qQ6qlOGzUZi02Z9ki35nxVg0BzgKufisSjAlZDNtox11N5v9QH1ahifX7FODFfJ5JHI_dlhUJiMpXJSeTwlw2_ZSgfAOt-D_7aMtE7DlZFH6XmfAK0SFzgJTxghzkcCFT1VebjVbULixQSe3kDX327tzjCgl4jqvBEEhCPI_pNlLLnHGW1M7h-uBqPUGhbA2K33OXx-wrQp7am_PcCjGyfCDykJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیم‌جونگ‌اون رهبر کره‌شمالی تو یه‌حرکت کاملاً منطقی اعلام کرده طبق قانون جدید خودکشی کردن  ممنوعه و هر کس خوکشی کنه زنده بمونه خودمون اعدام میکنیم. هیییچ تعارفی هم با کسی نداریم:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22674" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktpWw-bpm8FLKYmk5xDFXK6qqfKLZVi4kiB6yFlusRljsln2oXNi4P_UlV37HgmRYGWeh72P9GlZ0r0-OjGSszYL-gsubFNxpyqyZcNUZuPy_svlwTLDjOHhEUiUMWjO21pYDnfAFEjeQbVJ7Ik1PHwOstQ-rSX7D1j7WaR2UUErkJ-lyOZaRoLqgJlvDlaSJBBs5cHp80gbBwfTp6qZh55ygPMAO2yEqd9jC3aI1HY_YdKtRDoR5XAzeF4BgiMVWrVM51IVcSeen-CVjzxbPpMgEHtjEtlonNd3Fns7iyJyCpHoBmHiaHhYM9zC3NaQwsvZVNU399LnwLosBUjaMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیست ارزش تیم‌های حاضر در جام جهانی؛ فرانسه با ارزش ترین و اردن کم ارزش‌ترین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22673" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5-bvv5qtkygjxPrLKOzhDjPG4CnOWNlnQnQ-SAu-mpUC7WWiRGlqkVvSdWYVAm9LakPMI4fMTAWbk5J66GivT4e9q0I6GIDqMrW7_w3PyqonEoswXy2NrR3V0Vx0GCRO-fCpzakYgWnaNmYHIqdQQkm64bKo8_E8wV9TjBQB0iApBB8AT8Hs5kAHqK6OP2pRtranBVIJ8vWQxsmZz-JzxBK7EarqDIcLqZQBrBNJ31ZoEl5Lni0KvqTGgCdh-lgVzXGLBFEzKmmv0BSaSOBy4dzOgiORzEO7GJdzdWCZGxjP24Nn8bAuB_0c9mMNWPHsk9WqHdA86GkoVswkNcJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت: بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22671" target="_blank">📅 17:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWBMZDDKlr4YrU4Nea-riXo-c4gRq3KAHBqkmVBkYZAQ7bT4FazUhRUni6Zx8mYZSvhfi8DCOLyBxzgfH2Wl1bL22bDT_NvTqU445iRSgQjWw0JKFB-23BQT7O8yMSvSONb1W1Wcy3iNNEkouzjKIsd6rvyM4UBPw8TljCdn0gw7aOiuHEdJxYHrBnoa1lmD7WXIrVwUfB1bDF6ULqPu76kA5JXO5tuagmY8dhYpKTXFGo1W64lGhFoeB4dlIflPSfXCZViErlOhqbTxqmUi4aPMxgIzLKenaWMl6XUx2dNNg-NQ-zMIcZ4IZPE6seeSlPP2M7FcTd8frCcZ1mQHhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ روزنامه آاس: ژوزه مورینیو سرمربی جدید رئال مادرید موافقت‌خود را با پیوستن ابراهیم کوناته به جمع کهکشانی ها اعلام کرده و به احتمال فراوان بزودی این انتقال بزرگ رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22670" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoT0caXWuq52pfdCEiTO65eH3ud8WqkAZbve-gDIn2jO8veoV8sUwd20MlAusGau3gJGX_N5xbb4yrX46Fb4lmbz2sH8vG0DJi_9fs6Q73GKbzJ6hU6k-5cLFGU13g4Wscdbv9McBLa6HTWtfrx_fjddIJ-RRuMqT4eYx8GZoEd-c8kg8voTGan1BszEpgjxG6IYwr2GhKsYfU27OlhsHwMCsIHlQ9PfaeBtKcySfHcdYYIg6DIa1xr6lXl_XZ2-LWOpjGYTubhs_USg-5dZSzDh-aDlGjSFIWmRP-KGRM1SX7sCqPSS03gO1XbqQeu2b5pGPcBWIb_af_zfXm0NCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلام و احوالپرسی‌رسمی بین‌بچه‌های کره شمالی وتیم ملی ژاپن، در مراسم پیش از شروع بازی مرحله یک هشتم نهایی جام جهانی زیر ۱۷ سال.
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22669" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVtfXxrqthnyviR-1e3gr6JfqHKWXbAXmZ_RuD0fnWFAOtk24YaYQGoA8XdP20T9ZJ1yWiocM9cuKwDDxjHKZ076wxk2ZUmZygl7hcQFyzfc4tTXnnjcR_nLJIdOG7S9ROl5Y4YaWOH7eMNVYDX93IOLJUsf3az2WZ-nGTLrj2nkCQLB3XAtuRp32vi42govaJXblo5qGRGws3b9uYzh94GMYPKoeGq85GrkRTR1AAJD5DshEdPRAUOyognP_iad0xrRaFLAxAAqwLJfZ4WG0Tlfrengf7ZI1lMkQILr-mUERdgIwUCiCDtwFS2A7sjMjw_n3K92AyGhHKFpuB5x3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22668" target="_blank">📅 16:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCT9ZsBHZI9JYXIxZhLJX6rb8brFDh6wbKVM00TKh6D5h82BVgkQvkdhwcl5Je7bZooO5zQvGAuIuKiLOkGk-JQBrn6hQPJoeHbeVMb6FZ1BmEWHTIUs34kyl_-cpH6OyS9Gb4gOlYCgIIJp61KpH-jOUVO0Pswz1U8iFHEYpkxZfsmpTgLws1DlFjljy3u2WIGe3R1LvQ8H9Lmlih8BiIHRPU88XNuhoWEFrKwW56rEkQUfhy0cgtO6slSnTSKLZX6ucWouIrWU5_FjNbChzYu16I3VX5o3rDp1pTha-3wAbWjxlEvpIAfCajnQRHlG362bjVU_opR9F8LjGUYG1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇲
دراقدامی‌عجیب؛ کادر فنی کامرون؛ وینسنت ابوباکار و آندره‌ اونانا دو بازیکن با تجربه کامرونی ها رو از لیست این تیم برای جام ملت‌های افریقا 2025 کنار گذاشت. ابوباکار و اونانا در این فصل در تیم‌های نفتچی و ترابزون اسپور عملکرد درخشانی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22667" target="_blank">📅 16:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyOALZNKz6SrJE4-wZgCzBki_T5o71EtjwJtGY68cHXdoyPBMzYKVvzC5xApDIPiVAXghNcAh2bXJnr9BEJDDbb007ehps9Gwbh2nybibErOTc6IS23U0fWcS_lAyBFxfKjdkzmuCF_aOA0KyEJFxRgIMcez0uzlRtQZ9uCjN_g7UGTl6sTbcZQTgihabEYIjtW_XgcZ-jq_l5V16m7XvZpewy1E3aFh9o3o3f2lwnVLof2SEYhW399Yh1Zv_WnvKlHrMT0NnT4dKK6T2lAIN4NoM3sgG5uO2gjqAWI7mroU0Fef_ISCbbgjqXqllSP68riq7wS9XaNTr2V5LLdUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22666" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTTG5j8_6Ygd-m_xcT2IUMhoVIhq0ZwJ58TBqCTc2H-SgXA2qDxhMPpBUmxPZ-kyir2StN3me1qWk0yE2CUVDFLFHjYwNvDe9scWXDJXSRh92aSRn1RJrnqkP758WyVR1z-yuHMIqZI1gPhyRyUUnhu6CHzbOk9RQEsAJ9KnChWCYZiLprBurB_T48iqlos9UV2mQOyJeW2SLbo_v4iyxMuS2MVlYrNCmaO4ppKRwoNIy6dCwjcsMEVsMvCS9G3avgOyH1A7aINmvsAou3cc4vKz1ctr1lSPMXdreZhOGRlLViVJz4r5VXaxEXEJ0AZleUr6Y2m0vrNqtLB9IDM7pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22665" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22664">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJEF4lWL5iEIAyNBnEpFgGQ44luRPFVN-eb9pWRyE9ene8N1GqUqnqqxJcfRDHWt0qbU7o5ofA6l0OyR9jlpy6RcSgP95R7PkC3cagxYoWZuRMffh37bbtChTFSsI9dIxJaas5_GSyhDJZSbRt96hRISOvAIuNGlXwgRaJv-AEVHpUDrqzgCK1DkzLY7xOHgm6igfl31VoMcx8jYkF-XDIP2_uyvGsL5OO7icLKnqlnz7WhUCqR_J7VDG-3dFTPPWg0Zl1FAEWo4EC1tAJ8AFeQyqSGQ1mdwps7bTB54fA0rq_s_lVKA_o03py6JSvIu4qbGFzHGmj6ygssljEEMIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22664" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Joiau-gWv1No3d5a5syNSjpUwIQ0SUegD3rKruI7pHXtYthRbRVi-h-UoAv0W91CgvG34wvdwLvzeyxhq-bhzhVAKGxtUfCDNJlSgxmv03dX1ihc0sfgpGVg_Oe9dHV8r7lW6dg0WkgBDsmzqV66VHEePU-EctrdKb0lobQiBzb8M91BRM1vLa0Jwl0uzJ5ZamS7jFgj8Lb9Bjbd0SENNevp88iB7O7jWNDyyxvfAMkaxfpW_i4jN67-yxMS6NfDzUBsZWAm_zdaZAEAw95tBSCmzNR5n3Y1tfJce1hxNGZSBZhSLTYq361lVVuH7pveYk0rcVQtJUizWPiVySWP8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22663" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOhVJaPQarht0aDnFC05gJBGREogGbiiCLQOTE_X5p_3mJ-gH7gAWU93T_WkM94pupmJGQWuGQDH6Gi9tGC0R9fmzuNKDsNrko3bPGVlR-PFomdO5G5vuMtT8B7VyB5SxXCJA5Z0F9l81kbeeE_FGZ3bRwgLBaF5uI0l-S7Ui9tvoxZ9h3Zl-HRFn3zCdjM5BOWR9KkPXWDmds56CMuK2KvDTzf6obE0xgZczvfdUXGVikCqywBx1jQEEw-jdr42c2RFjwUB9T3Mm9euVX5qQdPYhAl8U1UzKtKzoi17y0CINhKZIc65aVM8GtE6-DyZFYdUQY8MCA6SSzj518CUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا
#فوری
؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22662" target="_blank">📅 14:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mo9yOUROSVEt2Cm0OELzC6ZxLAruui2eDMZjbVcYcoPPmqVMqgbK3GzTUITjKvRLuEWyEBoeBNdrmTDWydCb-n1m3Ql7nyxDjycN0W5PG_9mLXPYsZGTjN7yK7jMmFdY6x9KCo6l4ThIxr4ly3r8WjczsSjLUjRyREX3YoUCX7gOx1qU3JlXAUg4f3uCvn4mNmB0WFn5HdRmdNDCIzwdjD9HQRjYcygnA7H1qkDLqUwwkFh_GoS_Pcc1iAYZ3V28Jbms4YRednR1jyw5pnGmtaWan-G_Vq-cF-QkwWhi95PpOljYEKZj3PjXywjeMV9IMEqRtAm5ARrXUy2RtMmfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22661" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=U-ZUdX9JZmYlAbBKXfZ2oNqxK9sIYJA5hcBq70c7M0XQOSg22l0BiqbyroUh1StD18GRF9quOyqtauPEjdrAkCRzTHkgrdG3qHIyYlV3Go5cderWg8h_BNcHHHxpprY-v-qt-cjOHMtm35-DZcZzMiLM1tui7VJLMO380SHGjTDAavPXZh4fj5e7AI8ws5wSAv1nSSztcIjlKmFUQiyBssrWuo33uoPiUchPH0LpABxBIsZLsb13tPPshcclqGtLqL0E8lKhCnSbhs_gr71GrF8OHD8xRXnx1JPzekz_BINQ_Ng6SLwp70LddXWmO2bPGTinJ115Nn5R4_u-sffYqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=U-ZUdX9JZmYlAbBKXfZ2oNqxK9sIYJA5hcBq70c7M0XQOSg22l0BiqbyroUh1StD18GRF9quOyqtauPEjdrAkCRzTHkgrdG3qHIyYlV3Go5cderWg8h_BNcHHHxpprY-v-qt-cjOHMtm35-DZcZzMiLM1tui7VJLMO380SHGjTDAavPXZh4fj5e7AI8ws5wSAv1nSSztcIjlKmFUQiyBssrWuo33uoPiUchPH0LpABxBIsZLsb13tPPshcclqGtLqL0E8lKhCnSbhs_gr71GrF8OHD8xRXnx1JPzekz_BINQ_Ng6SLwp70LddXWmO2bPGTinJ115Nn5R4_u-sffYqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های ایرائولا بعد از پیوستن به لیورپول:
خوشحالم‌که اینجاهستم. به هوادارانمان قول میدهم در فصل جدید یک لیورپول جدید و جنگنده خواهند دید و از دیدن بازی‌هایمان‌بی‌نهایت‌لذت خواهند برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22660" target="_blank">📅 13:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwgpzgQWdV9u633fPOdqQuVgYsS1WPKQs5B92ZqAYDyREH8v9cUCMYuEMG_BkLAoNw2WS66d-VarRUWuA00U4QKO_vabFczhjb_sJNEhdaVC-LlydcHk2R4fSjggAqZ_aqnoT5maGI3eYLBnaBZvFNVR6J1QimpFGwxWYGjVKtWct_CkoD0Puha5zuOxH46MPXJ_3gMkRclGtOljIv3XomqnD5F3LIWfMmHXmbPT1FaTy6dlqIzYGv_VpdfYbVfijjNzPEz86VXdPDLz8CDhrLFqr_-NGnNQjExF--utsn7aNpGR4Z3iMMeeHgt_OJc47Qe_WPqJwfbtMVq65txKGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا مدیرعامل استقلال: برای فصل بعد هم یاسر آسانی درجمع.ما باقی خواهد ماند هم مونیر الحدادی؛ یک وکیل خوب ایتالیایی استخدام کرده‌ایم و قول داده که پنجره باشگاه رو بزودی باز کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22659" target="_blank">📅 12:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Et90gzNkmZonNPTaipGc7MdGWRO2wrX2bUmLOfqFlJPJVMSxnG9p1JGtaEyvhFqkiYsj0vbsuFqp3x6KymfiyBigf9eOc0qTfbeA_ksobpHhWFKGmbntUhLo2OMvxsybVDlyP3GuKlUtqM_eRVHL689WLJKsjA4qa5eon-5vkoRTdcP2m6PthjvCkMjjPvG1FyuRb1Xmm2vdc_G_EnRrlZc2ztdmWa7mu_L8Ga4gsK8WnbLJ9VTN-sKceE74HbqEC0Ulu3mUglNNpa_Uj1RkFT5Rp8Vw20u2bVHRphISRra9NZ2kzL6FCZsfCa9QXsG9JC2V2gOWI4fGIbc28IuyrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22658" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=XzvKNEdGOjpbSUzyIVRObHDlw66oEmvPtZtWOkMeY3UoemPioVZ70A6b0gHuyqIkdBgbK_vvVnbT90Fy0lSeaYQrMknlmwoSM-paA88ptciE38qeafdldPNJb4WKhWthsO9OOHQ_X9SwUrhAmGexsOnCC2877svaVZG6Z4yuVtf7g90X_4BG7N1QcGoKLxSB6FoKAKu-QUMrrvRtyNHSM9XGZXwL6yHWHVvZPlB8h9ZEeIzi5WNO0YCmju6w31kfCOOXoLZwNawe2OAS2hd_eM9Ab09dY1Io_KLMX89BGfAPa45kzDwhkwSn1Bj6oOAAzqvcf-vFVFRJxuUnm22chXDfzorxF4oKvQi-56DzNYbM8si3Bj--L_G-NcTHzoH8NOzoXsnl_ft91T-e98bhn1sxwIzMW0egFmfto7qcnCwnJdzXYFi9jv-Q_u_RjhIQV-o-MrJOBxLbGguKywm-m52RIul-dLlm5_zoevuilSsplj0pXN29F26kcm2zx6sEDZzIWSUvZhLAWQ9x2CHQ0nigIUk4YKs07LPBa2HMwaJVkZ5d3FVUuU2FgZhV6pvCSd1E3YzizDHB-nC1TR6pXb7aJwW-8lOHb1V75mo27AvMqhYYHa4Qu09G8X_VekMBq37aVhpUY2UjKG0c9uLO4OuzheBkyOHdR9Yke5Fkd4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=XzvKNEdGOjpbSUzyIVRObHDlw66oEmvPtZtWOkMeY3UoemPioVZ70A6b0gHuyqIkdBgbK_vvVnbT90Fy0lSeaYQrMknlmwoSM-paA88ptciE38qeafdldPNJb4WKhWthsO9OOHQ_X9SwUrhAmGexsOnCC2877svaVZG6Z4yuVtf7g90X_4BG7N1QcGoKLxSB6FoKAKu-QUMrrvRtyNHSM9XGZXwL6yHWHVvZPlB8h9ZEeIzi5WNO0YCmju6w31kfCOOXoLZwNawe2OAS2hd_eM9Ab09dY1Io_KLMX89BGfAPa45kzDwhkwSn1Bj6oOAAzqvcf-vFVFRJxuUnm22chXDfzorxF4oKvQi-56DzNYbM8si3Bj--L_G-NcTHzoH8NOzoXsnl_ft91T-e98bhn1sxwIzMW0egFmfto7qcnCwnJdzXYFi9jv-Q_u_RjhIQV-o-MrJOBxLbGguKywm-m52RIul-dLlm5_zoevuilSsplj0pXN29F26kcm2zx6sEDZzIWSUvZhLAWQ9x2CHQ0nigIUk4YKs07LPBa2HMwaJVkZ5d3FVUuU2FgZhV6pvCSd1E3YzizDHB-nC1TR6pXb7aJwW-8lOHb1V75mo27AvMqhYYHa4Qu09G8X_VekMBq37aVhpUY2UjKG0c9uLO4OuzheBkyOHdR9Yke5Fkd4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام‌برندگان‌جایزه بهترین بازیکن فینال چمپیونز لیگ از2020مصدوم‌شدن؛ ویتینیا طلسمو میشکنه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22657" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlhX-MfZRyFaOyKrcP56Yi8t2MnXImJCzrUc7yS12LzKhLGImqc13M_rnOzJgBVmoOMjyGkV0Deb9eIV1wvcq2cHsNTr_qk8RYeoQBymS2Fc7Da1cinlkPnGq1KHBXjAfE0TPRXJC5HjX69nFW7d9wr-2MI5raSs4qNU_wOzXeNeFnuJq0tIm2lvGyURIGvPJUtfmTFqxvYnIooYe2goi4l5qg087Q6lg7ECiPbYqt6oAfsOp64vdKio7iCLEGKx1oPweW5Z6hub4QKqDEzTCjqwFhY8T8LtiFajZS3sspZtdjw-VSXuSgpjHMLxsRmMxuXZ81K1kpLtPB245yp-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22656" target="_blank">📅 11:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=q2uYLu2Eh7VdusM-N9eYBrhFYZlTTsOMkQireZbILSbQSuGj2VlJhvXLMk-tEooFwYC-YpnIwgZ-JETC1DfQGMebsDxDh--OE8njlnOs7hrz79fc27sPTSkK0AbGoX7xbeKQVlaEutzIrBLXnXSyxAa_Qef9vmDaTjE2A8OXmIL01zwKJAWw1RciyGfs-ilckmE0W0upHsbIjQPm-rUNdyBY8Bt6TjmwBwGh4FsuAdYuMTPkoKdS5zLmoUmMfzQULt2eRCIYTKKlUQ0DPilARZuSzvvjYk-7FrnX1vWNu9a8BH4Il5k9AadTim9C4tcaLK_bg31dsak4CUGYL2ygn3lEXgFotpTa0pBmPRAqdFqNTgzyw_lOidppSpItvxmlAlIB3t4wkKWPV5OswVNdTQ8-6WY4fw6TZZI4fUa7eunsL-oNGmZwlWeEHLuI65e5jrDOk9e84BLXRmTvpjwG4N1f02msH9tNk1eJJtkgDU34GeEKkiowOvST6Zt8lfS4qeQE003HNRRKXoLD4J-H61rqd1t4zF6g_8swWnIn8ScjMbn99c7eOQ00EmIZ7g4skvrTbo3mNdkYqC6XPSMEuoipI3Ky9VO0J1h-daIdMABHFGJTHbQ9EB-mPBatZahecu9WuJObu-rI-AQFeiVCAn_y1ZOZ2nIwFkda2d0aoFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=q2uYLu2Eh7VdusM-N9eYBrhFYZlTTsOMkQireZbILSbQSuGj2VlJhvXLMk-tEooFwYC-YpnIwgZ-JETC1DfQGMebsDxDh--OE8njlnOs7hrz79fc27sPTSkK0AbGoX7xbeKQVlaEutzIrBLXnXSyxAa_Qef9vmDaTjE2A8OXmIL01zwKJAWw1RciyGfs-ilckmE0W0upHsbIjQPm-rUNdyBY8Bt6TjmwBwGh4FsuAdYuMTPkoKdS5zLmoUmMfzQULt2eRCIYTKKlUQ0DPilARZuSzvvjYk-7FrnX1vWNu9a8BH4Il5k9AadTim9C4tcaLK_bg31dsak4CUGYL2ygn3lEXgFotpTa0pBmPRAqdFqNTgzyw_lOidppSpItvxmlAlIB3t4wkKWPV5OswVNdTQ8-6WY4fw6TZZI4fUa7eunsL-oNGmZwlWeEHLuI65e5jrDOk9e84BLXRmTvpjwG4N1f02msH9tNk1eJJtkgDU34GeEKkiowOvST6Zt8lfS4qeQE003HNRRKXoLD4J-H61rqd1t4zF6g_8swWnIn8ScjMbn99c7eOQ00EmIZ7g4skvrTbo3mNdkYqC6XPSMEuoipI3Ky9VO0J1h-daIdMABHFGJTHbQ9EB-mPBatZahecu9WuJObu-rI-AQFeiVCAn_y1ZOZ2nIwFkda2d0aoFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بزرگترین و خفن ترین کامبک در تاریخ فوتبال؛
بنظرتون عثمان امسال هم توپ‌طلا رو میگیره یا نه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22655" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=uLS0pct6dvbkSYOZaBmZpP_KXmqf_uhmaRcdCxALKC2ulaRxXqH0gr2GBSnbs13RALQwUpr9pRbkyOwRCqQmlZB7cqlfdPUw0vSIsfnMHYsb-8vb4_Eg6Rd9rnQl3JuiUTp1N1F8rQpcE1l9TvhKjYYhiT9-xat3NXRfdOlaA6EzpWbrrvKB6v0bc3O6iJhO7hxfNmEHtaz07nawekmJAAYNDiTrZitF7JCpUhrTVTPK6ifSZ1Uq6I5k8jirXM45PTQ4j_SoL09HbCeZoVp8tQNdIXaQOFq85rE9zYn2TvAZFZJqeFPAh9q9fpqrsMclHnYH4Qr7vIp9IowmF2oqDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=uLS0pct6dvbkSYOZaBmZpP_KXmqf_uhmaRcdCxALKC2ulaRxXqH0gr2GBSnbs13RALQwUpr9pRbkyOwRCqQmlZB7cqlfdPUw0vSIsfnMHYsb-8vb4_Eg6Rd9rnQl3JuiUTp1N1F8rQpcE1l9TvhKjYYhiT9-xat3NXRfdOlaA6EzpWbrrvKB6v0bc3O6iJhO7hxfNmEHtaz07nawekmJAAYNDiTrZitF7JCpUhrTVTPK6ifSZ1Uq6I5k8jirXM45PTQ4j_SoL09HbCeZoVp8tQNdIXaQOFq85rE9zYn2TvAZFZJqeFPAh9q9fpqrsMclHnYH4Qr7vIp9IowmF2oqDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22653" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjhSG6fD-yWBK8nwyHt2Nc8j6DtQ2FdN552BKuA4wEjpBdLrSz5XgLAWkg0Fk-qVRxDRCefNLXBpujwji3T_5ovDnO7tPBXV7K_9qSfMQkOka_LPau9zbTTDUrQZoUOq67UIqcgFugwQyI0zzueUSqR9mFWdgYgKaLep0NCxxDfEZkADJ8arEYF-pXIzkW9X5-FnQT9Q1LoqdQkH0BezlwRGbUq9Zp_kJmYYn-yG5UU0zJ5YKjM9hXT7d9UDfTqjacoEsOPc4NEsRIDq5HNgouI_KjJ_Hn_RMplQNuM-x53SQiyspZjjD_ZzD5NLIeV5wasbpl9HKw-SDnwL_az3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
آرتتا سرمربی‌آرسنال درفصل‌آینده پرمیرلیگ تنها سرمربی‌ای خواهدبودکه‌قهرمان این رقابت شده. همه سرمربیان موفق از لیگ برتر انگلیس رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22652" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPprB6rTGi8OdRNhq4wzyi23sSe2jIYG7aqTGP4CDD92ampwOCRcmpRlMZWpXyPiDNB0pJzFBPtSmJkJ3Hv0Jk0A6pxCQ_KhQbc1vZ-3GV-v3-gqlfBhckgJs2RVzYm3Mwu1C-RMzPc7cyLfFVMJyDuCtt61trNDWlEl0PxCx_2pT9m1Mo-0PsrDR-d6yzDi4t-eAhyPMiXI_O_HpGTnUNwK7J40kTktsw_OcXQ4m3qEmnbbEJ_BkxH2fOiGlvFvzW0RYXs8VGdAi2WKTGlvyECm2J5eckvT6z8kL7SYRP4SkeRHKQf7v6ow1SzUyf-j5yD2PetmzneYtMw0BGmeBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ویدیویی‌ازسوپرسیوهای‌داوید دخیا در مستطیل سبز در آستانه تولد ۳۵ سالگی این گلر اسپانیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22650" target="_blank">📅 10:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22649">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdHIkhJIEEMasx10OBoOrhTj5MFECdyC_KUPzWAwciIdjrkoRg4QKbzZADa19ODnlE2vBjJ9ZxHLPR9eNghSJ7kFKGdvcvMQVRFeci18vaMdWnQ6rbWf0D9E4AH2PXVUu928uRCKkQgwnAZSwo-HpLBlfP2ZdXmDY9744I4At6NnXGmrWJVN98vej4M2U8xWuQvOByrNB3Rg9RdkonGFcyuSFeZ-H3isPkKb2olP3Bw4_-I7TpEGqI2cv1vKXeEnbA9eRKqn-gfeMkjvMBT9Zw85kaBvFEHQLcGD3u4_l3-iKVzNwsT14k2vkh_r4_wP9_LPsL2MQ1jc5H9Trb8k1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادعای رسانه‌های آلمانی: هری کین یکی از سه گزینه‌اصلی‌ونهایی‌سران باشگاه بارسلونا برای جانشینی رابرت لواندوفسکی لهستانی در خط آتش آبی‌اناری‌ها برای فصل اینده رقابت‌هاست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22649" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22648">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-S0hQRcqY97uSonRi96aAmiizKZwTkJCDHp64sq5iN3SzVUzYo66LmSy9B7Ytsd8uxSq5DkfLG9hQbSumh9PD_3si0nOK-UislzNEaz0U4gqZ1EIOY7jugM2qb5kJMZf7ONMyUd1HZ3VcUtQn-MuXeTm3iU15crO_8RHivO3YeL2BLVwFDVqwwK4UUyuLT9sTIZ_Te2ITaqJN0-XoJMMJFFjC9o5f85kG028LGKIS1x40qIIHNdBSIDUPAR4UNOFBaqmsgHipmH0L30wVUVjTONBr9kOGZoMgV-aFHN8tkLeXlEhq2LjBfLB7owQwR5tOE3nZ5dBpHj1V8rh0JELYOpY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-S0hQRcqY97uSonRi96aAmiizKZwTkJCDHp64sq5iN3SzVUzYo66LmSy9B7Ytsd8uxSq5DkfLG9hQbSumh9PD_3si0nOK-UislzNEaz0U4gqZ1EIOY7jugM2qb5kJMZf7ONMyUd1HZ3VcUtQn-MuXeTm3iU15crO_8RHivO3YeL2BLVwFDVqwwK4UUyuLT9sTIZ_Te2ITaqJN0-XoJMMJFFjC9o5f85kG028LGKIS1x40qIIHNdBSIDUPAR4UNOFBaqmsgHipmH0L30wVUVjTONBr9kOGZoMgV-aFHN8tkLeXlEhq2LjBfLB7owQwR5tOE3nZ5dBpHj1V8rh0JELYOpY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22648" target="_blank">📅 10:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJFR5X3yhzYBUrQWYtBOue-dTGAv3oL8fnIRl2e8wfUHSz3QWJQ40e5gSFueJHW97Z1EikehrxGMFREWqlfQacnU4Svi1FRi2C_UeJzt5ktjPCeSbWb6pB5TQ99aK65o0CTh902-WgPrBWNmXsPPyAx8FUe73YIx5-0j6HhEaxJ0l2DIw8r6ALrV74f95oLelMn9BjYnmZnj9s3-N6o5Hvp53GA0r0Q_kZJmms5NxQlriFcPmKuO9CE530Crjsp785Ite40mEGD9UvkXwVdS018PePVReDd4ve2DZevkookxiLyBHmEXI4zq56oGAbAsnybpGFmNn7a-DV_7g8Llag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از پیرفلک تا شاه کرمی؛ اسامی لایسنس نشده‌ی بازیکنان تیم‌ملی ایران در آپدیت جام جهانی EAFC 26 با نام‌های جاویدهای کشور جایگزین شد. حرکت غیر قابل انتظاری که EA آن را انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22647" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMy-9F5vuukTMjpdnhlS9V_euMaLGo7xO7S4q7bq6_bFa-R4rP2x9Y6rBPZgPQ4QOHNBq6Z10LBPbX9wYt7Kgima_MmSnipW12ELgMwi8RiWHqa3v3c-cT6-Ucq8YUpTosJ8-gZQbyTu1e0AfPOK12MGJUZjrOFA0BrULAzEfPMRD2aB54m7OWUhIjzT-Z3KQi6FIFaXOWCA7LpBIHPQo0ieIOppYysG9pCxigA-25ZjKZftzByc9FZcw86yAsLuGyYRtyRAtEaMTiOTq-JgSR72j_BwB_49xqFtj2JbFql8TxBm8kM_qgIMknwtOlUIJsVw3ecrIK3F2X-n3kItnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ابراهیم کوناته مدافع تیم ملی فرانسه که‌هم اکنون بازیکن آزاد هست اولویتش پیوستن به باشگاه رئال‌مادریده و درصورتیکه آفری‌از سران این باشگاه دریافت کنه سریعا پاسخ مثبت خواهد داد.  کوناته از پاری‌سن ژرمن و الاتحاد عربستان افر مالی بسیار سنگینی رو دریافت…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22646" target="_blank">📅 03:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRltZif8Ii7TCXSZxgmnpjDdJOkrFEZZCVETsnVC2vEpxSNW39KT8JFwzMURhCuEFTHQ9oI2lrGz7XkdrsM5DBOSoyKTTBrVAFLcO0WMOvjY911geYLTaIdeduEdtMuCcwPFYPqlD2KNFqOtL5dnJP-ou4SscgGCxLKR47d6dzz0EalVXaGShIugUu-h58ACGJ7kkMLFQGsvPhtC47O9umRFEb3diuFfMn2zqxSJw2_mswtf73tppBI7KaobydCetqdxY7wll8_ZubhBRcFf0DpNWAhG1UITp4WJBuJeZZ6KEANsKLdz81Zlzglf2S3Hm2adM9j41fob3m-SWTwJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت:
بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22645" target="_blank">📅 03:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22643">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzllUDIDZWvibwBjlL9eBApXvkMZ7QvQGwR-UoaZG7rDkWxGlIqpb-d-GXMr3lggWTrlnj0v5C7RGuQFEdZS6aLvb8dAEadv5pron5WeqY8IHdnW1a1pyC2Pzg9AmwLAsukJLgqO6-2p2KkBiynPD4VsBrYlw8D8S8ND5blkXS59ro0fuSgLQjrH1GbI2QsDWfHVhgEkudwHYkTTD46evtORZxvMMPWWmWrUErqR0_64ynR3lRMsD5mmfCB0r9ndjcV1nhGKxD77JLzk3r_8DYmCJLFoUAwvmarymRJ8hKOR_YnWjURf9QGl25zRw_5YR4m1dMMCqAl0QSeo4V-UOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QMBjRJlJiXxSByK8h97K6mewBFJ8dDM9CgdmOq0_DHz0q-L5ME9wMIf5Ia-m1mJiQtG5SLX-SwCTDwpMk2I0obubvwwRuUXnhlhGs50E6uutBRiMdsjdK434qcwR6No3Emo68U1tVOx5M0BO3bIqeiTXzchSJCh2IvEmtf7QZPJx_aeinZmBUaRkzAQjOmxq0ZbmerP95AYMbhCK84bKVuYIslJxf52XQ2VF1aj0Q2GDuIjPZ9XxIyknvOspWWgdSjuOzNJsbeYPA_6QQoVxW7J-NS85gGq_ZkNZ4yIaRBuZ-iuXOWSe5Qwl8CwdJEu5dfswyaHHW4smhTJqRLNn6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
تاییدشد؛ مدیربرنامه‌های فابیو آبرئو ستاره آنگولایی‌تیم‌بیجینگ‌گوان: در ژانویه مذاکراتی با یک باشگاه ایرانی‌انجام‌دادیم‌اما بسته شدن پنجره نقل و انتقالاتی این باشگاه مانع انجام شدن این انتقال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22643" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22642">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=ITWV6VFYV11NOtaQn5TLmhuewfMuvt0kre9yL6vBxb_xNKKuFNChxC4hgEzSFs30wabbpkPsEO5ysQwlzQ_Yv-flhHopwW_yETnVZhaLNtwsjVwDREDgo8dThz_OIN7IZoQpyvb-hiDlGu6gYh2mkLZ-TCiLhnTDEwU6aB6eBYjCjAxJnk5iNwHC36IXJLNRflLjLxuprxwZ6T9gCIeSFt3UVSlkk9QgxN5jOv65g3DXC08biFnurIP31RRM_6cuj-rsLS5GQsccQPApbKfXWwX_cLCRvTuoZqt6XtTG5GCCWKyZP02flOhXN8obtll5k2obg2oPgTAKQF-OC_AmUQcEdnOq1Y70VNp4HxGg80stCzLFZ_c3DJt3gZ_2qSd0RgXNDIBPbHzV0Jlkc83DBbuoz9LIvlnrpBxqbVCsR3K6etEvnLvITfDZsWVwGpPbPCvTMq3HgTEQN7tg81EXFgo3wOdgYYG7RSFUaxb2d5jmb1Tz2uZhvBLDp7WHa7qeDsKiZWX6IAE7oCdXO91_mb0tNNEvqirjmm-28OwEUBYZti1nmr2WxhhLgP0szR3ndelgfQAxn7SZ4aoqMFhxXmCD6Fq_YzxGCx9CP34FxSAVOqcFNaM8mgIyi9GUmGvEWxeEwP6vBEURzzGLlGZ_CmX31JcyhBBrJfnf0411yeo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=ITWV6VFYV11NOtaQn5TLmhuewfMuvt0kre9yL6vBxb_xNKKuFNChxC4hgEzSFs30wabbpkPsEO5ysQwlzQ_Yv-flhHopwW_yETnVZhaLNtwsjVwDREDgo8dThz_OIN7IZoQpyvb-hiDlGu6gYh2mkLZ-TCiLhnTDEwU6aB6eBYjCjAxJnk5iNwHC36IXJLNRflLjLxuprxwZ6T9gCIeSFt3UVSlkk9QgxN5jOv65g3DXC08biFnurIP31RRM_6cuj-rsLS5GQsccQPApbKfXWwX_cLCRvTuoZqt6XtTG5GCCWKyZP02flOhXN8obtll5k2obg2oPgTAKQF-OC_AmUQcEdnOq1Y70VNp4HxGg80stCzLFZ_c3DJt3gZ_2qSd0RgXNDIBPbHzV0Jlkc83DBbuoz9LIvlnrpBxqbVCsR3K6etEvnLvITfDZsWVwGpPbPCvTMq3HgTEQN7tg81EXFgo3wOdgYYG7RSFUaxb2d5jmb1Tz2uZhvBLDp7WHa7qeDsKiZWX6IAE7oCdXO91_mb0tNNEvqirjmm-28OwEUBYZti1nmr2WxhhLgP0szR3ndelgfQAxn7SZ4aoqMFhxXmCD6Fq_YzxGCx9CP34FxSAVOqcFNaM8mgIyi9GUmGvEWxeEwP6vBEURzzGLlGZ_CmX31JcyhBBrJfnf0411yeo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری
؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22642" target="_blank">📅 01:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22641">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcKef2szCiZNt6RLGYhyTIHMrU8S7Y8ZBBXTKBB_8u0-NlMn5xtlIbzHzOdNXLt5mSj3Pv2CVCPgdnN_rTfhBl4PU-rE2pvL-XFvtghbk8rpkdQPk0gySrnpGYNpgXHWOpFdiortB_Bhma55kzyOEbX2bfPykN5z9_dWSVjcFWzO03mgMOtIR6Y2f3x3ongOZOI6ddBv658hfAngpDH0gt3YwdlQUGvHHxug61meGHDUsD9Df25bEc4KcJvNkdZ3ppa04qOr7K7rah_2Fbxl3WAtbBUKCLJpWAy_C47GLSh1aHFAzL5KZo__u_AfamZGVIDP2GUPeCmukURUyZoaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آخرین خبری که درباره وضعیت پنجره نقل‌وانتقالات تابستونی باشگاه استقلال گرفتیم وکیل ایتالیایی به باشگاه گفته کارهای اداری رضایت منتظر محمد انجام بشه پنجره قطعا باز خواهد شد. هر خبر درستی از هر باشگاهی بگیریم میزاریم براتون حتما.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22641" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22640">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df595076a3.mp4?token=MfNYRJVZMQrfOdIQMlJ0_DxyeFSu8namtFlY6Ed-bgJAH3rjxxwcjR1nDShoz6BsvW45gbyBuKbcqK9MKviikNXhEqXX653W3xuwITqWEdK3dVY3A1Gk24SnYRWdmIou_m7rL0XXSAmYShpNmTVDaAgMsKtdDnse_USUH1u-L4L6xzx17mcv2kuBLqg2CDigWDx-uwNtSTujfgYaNHYmTK0Rc1CfNswD4gJ2BhDqNDB4xWVi-36TYl14zmCiZiLEF_151AWE5kEnA-fsJgfWSK1LG-IQjNdHOSRQxnHHL8MWKQAxCabg4HCxu4lWlLJauOIyLiHeF-o2u8HB6ibI4Q4K2vF7Do6ZX894feHg2ZF-j8He8ZHOxzvX-GydML4dGeCAMvkE2jdpMN0PJDakpT4cp3142f3wALkzeeB-d5c5uoCWKhKfiB-AiEoLPbaCG8lXOzp7V0Z9S7ZG7hApzTwInFVuxcldglWEd4le3LromnEKGwTpfj9i1W1NNfbbvrIXfHTUmB-WPLOGsrVkApi8BGkMIccdZC29XqedrdtH-_VevH9Y5v3qlvGWkYjESSDXftBigQu1qj7tA81a4_xeqwrzlK_JSf9g1_4IbWynJDGr1TfktCwcQmMBu3r8TN0bIeabChe68JAi-6PeRMSZ_xOhZxxtnA-2IDd6PQE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df595076a3.mp4?token=MfNYRJVZMQrfOdIQMlJ0_DxyeFSu8namtFlY6Ed-bgJAH3rjxxwcjR1nDShoz6BsvW45gbyBuKbcqK9MKviikNXhEqXX653W3xuwITqWEdK3dVY3A1Gk24SnYRWdmIou_m7rL0XXSAmYShpNmTVDaAgMsKtdDnse_USUH1u-L4L6xzx17mcv2kuBLqg2CDigWDx-uwNtSTujfgYaNHYmTK0Rc1CfNswD4gJ2BhDqNDB4xWVi-36TYl14zmCiZiLEF_151AWE5kEnA-fsJgfWSK1LG-IQjNdHOSRQxnHHL8MWKQAxCabg4HCxu4lWlLJauOIyLiHeF-o2u8HB6ibI4Q4K2vF7Do6ZX894feHg2ZF-j8He8ZHOxzvX-GydML4dGeCAMvkE2jdpMN0PJDakpT4cp3142f3wALkzeeB-d5c5uoCWKhKfiB-AiEoLPbaCG8lXOzp7V0Z9S7ZG7hApzTwInFVuxcldglWEd4le3LromnEKGwTpfj9i1W1NNfbbvrIXfHTUmB-WPLOGsrVkApi8BGkMIccdZC29XqedrdtH-_VevH9Y5v3qlvGWkYjESSDXftBigQu1qj7tA81a4_xeqwrzlK_JSf9g1_4IbWynJDGr1TfktCwcQmMBu3r8TN0bIeabChe68JAi-6PeRMSZ_xOhZxxtnA-2IDd6PQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی درواز‌ه‌‌بان‌ ها حوصله‌شون سر میره؛
فقط ادرسون که‌گزارشگرم گفت بی‌دلیل نیست پپ کچله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22640" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNOsiUUB8FSmpcMerfz6zee8RElaqw53Oo4WUMUvzU1SUyfdNlbcbz7V13QOc5CQkB9s2j_yAfyuYI2PJa9BVbzuj38UAQR9iV2H_QUgbyvQMDMbXNPvXYdZxwqrpA5CyEBrpCJEhLPpbsRAFHch_moJQ9Ur3L_uodCx-Cmaod4GkDImqT4cgXXmtiYl3H1hgM238tAX0RQ8zousjnsop3xxVwlM45FmR7RM4kvgn0q7BX8W94MEPfKmsJ6MRhhipA1IO8LwsIte-LUT5QdebodPAZt13qmYJniBb6XIhmlooXO7joh8dJrhMEr8GCGMElyRj71q4Da0OrUCxKw5DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ مهم ترین دیدار های‌ امروز؛
نبرد دوستانه دوتیم کرواسی و بلژیک برای آمادگی در جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22637" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6QMcjDWBoVdbDjdH0WD89wVM-DpPf0lbCxO4FNihUCs92ROBZW__saHPbbz2JYB0vhBDWtHXMFvnJDpjhR5g4o9m3w9JNTN7pCb_FxStVIwFXwUFdLuyOcOxB71brPuSfkM-R3idpVb3hQzXRqc7DVbqQbq9AqR2XfGs-iSShZy9rmvLjP4BmHVNDyU5W0J-rcoA237QZIzvvrha8tDbT6_HZjXVDTHvQ3Zjq0h40LOhbFy_xo4ca_TEFRlMDrq3BqVma0g459-BKNvJHtUvGa8YxKViatuVd_CTj36qHUiecOFS6r8o0qUzh95-SGMQ--jYdi-CpBYrTdcBcufaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد پرگل و مهم سلسائو تا برتری وایکینگ‌ها در غیاب اودگارد و ارلینگ هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22636" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=BlYDpo_w43ROGcOQnWv1BBzi8aBXcmop_M1gNFtavv4gFv6Xco0OlQKuq5IDXm_R5FVR36HtYwOFkvcEkW96G59MOSSw_UxmSaHPBfrY5h2NWHjiHmSB9MQbFNwHNouq3ExEHjgVf2_6VUrjEgvH3eQcmnqP-_YaQxXjRHCvWbIe6Wh75LdByaG9TFVCcex4rVabF7uAqLC2zFTEcFsxFUNhzueW_NRcZQo_cGAVsEZfLEc8g9NFBg8nat4LTU8yz4PlZCZku71UwKBiNQfDWkDIKuGXxb07krGB9zTl_X5fq13T_RJ701aPpQr7OAkJ08vdnjqstA0WrF7NO8J20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=BlYDpo_w43ROGcOQnWv1BBzi8aBXcmop_M1gNFtavv4gFv6Xco0OlQKuq5IDXm_R5FVR36HtYwOFkvcEkW96G59MOSSw_UxmSaHPBfrY5h2NWHjiHmSB9MQbFNwHNouq3ExEHjgVf2_6VUrjEgvH3eQcmnqP-_YaQxXjRHCvWbIe6Wh75LdByaG9TFVCcex4rVabF7uAqLC2zFTEcFsxFUNhzueW_NRcZQo_cGAVsEZfLEc8g9NFBg8nat4LTU8yz4PlZCZku71UwKBiNQfDWkDIKuGXxb07krGB9zTl_X5fq13T_RJ701aPpQr7OAkJ08vdnjqstA0WrF7NO8J20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دربازی‌ایسلند و ژاپن قانون‌جدید ۱۰ ثانیه تعویض اجراشد و بازیکن‌ایسلندبیشتر از ده ثانیه صبر کرد تا از زمین بازی‌خارج‌شودوطبق قانون داور اجازه ورود بازیکن تعویضی رانداد. به این ترتیب ایسلند بیش از یک‌دقیقه تازمان وقفه بازی ده نفره بازی کرد و ژاپن درهمان زمان گل پیروزی را به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22635" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAABZed8Ujc_jhSNpw8UW9keyrXfnAut9_yejmXM6GcCUOmsFDjI5-Iyf-qpgdcMxX-7ZUOG41aKjeyCqCdvMQneReBhd8EmHEXeJuLZB_lc_GEhVI2y2q7vF465lfED2HmH9nz0KVr219hS7_qbUM2YsXLfBKQdFAgM6CZyZxfxAtq4nJFDlOaVdeT-hC8hd8gPKQP3ReOdE7xBTrmVfot3fLWqWk6n7lai4ajBFmvPTcvn_gDxzERmRHGDN8rRzfdF_GfMZQB6AWx0nVJXb2NEIAizZmNnqvAJP58K7G-12GhGii22ib-LoWiEXqLnY8ZdeIJy0uIaBdnT_5ZZ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22634" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1bXDt2QhLjNmTbxhp5UgwZ9zuoYxMHSlB-RhFttA3xKGBTXxvAWl14AlRfCEFnOi4hqdcDHGoBgLkOBvTLdqouA0kQCv-QN4hD-_W_2IG7mnKSpw04rSD-6mhnXD5c1SnoS9CSrem8ZMF00vWx33HpIPlnR7RUEmGqrnOWz4gSIM-hbpKHyx2i-SI4_Cmhw7ZIoIKlKEqCDLjkbjraiCjpetq5p9JnUyRZqN4YNEXUlujVvh7P8tO4EHy_q5ZKhNLLUMVjN9IV8rvMh7OQBMrMxaatk8SA4AMMOaZydEQII14zIVccx8p99Z4vUVUwps5sOpskPHUTQRj1l3GU_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=iIuU0jD_4VFhtp2XXat7hww6lc1qACRku0pG9jgRjQ7eEDobGQqZsCHJ1Py0XFq6E8DbOdSkq3meQioXnYnO3KHZeUo04x-K1IBwBqTxjSk8pUipFGt5RF8ZrnQqzhDntihdkgHeTOhqvHYfePkxuIavhct5f6caDDY4pJMEsirZrYGELXuPut-BoiJXQaUC-_XpYRAdQ6Qx4YyCk7oiPZpvNHG_mK_9z2uRgudFc46VaIztdyRoRqdQpY3LD8bGQ76shQ_elqeqi2qJrMxEMXhX0lQl26CfsJcyxbtTFKGBAik585NcWrXIET9jcTk7PKDstvByLndXGq2YTyNC4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=iIuU0jD_4VFhtp2XXat7hww6lc1qACRku0pG9jgRjQ7eEDobGQqZsCHJ1Py0XFq6E8DbOdSkq3meQioXnYnO3KHZeUo04x-K1IBwBqTxjSk8pUipFGt5RF8ZrnQqzhDntihdkgHeTOhqvHYfePkxuIavhct5f6caDDY4pJMEsirZrYGELXuPut-BoiJXQaUC-_XpYRAdQ6Qx4YyCk7oiPZpvNHG_mK_9z2uRgudFc46VaIztdyRoRqdQpY3LD8bGQ76shQ_elqeqi2qJrMxEMXhX0lQl26CfsJcyxbtTFKGBAik585NcWrXIET9jcTk7PKDstvByLndXGq2YTyNC4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول‌برام‌سوال شد که چرا بازیکنان پاریس همسر مکرون رو اینجوری نگاه میکنند، گفتم حتما خیلی خوشگله و رفتم گوگل عکسشو واستون بذارم که با این رو به رو شدم
🥸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22632" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZInDn5J5cHIV3CSWOoGtDvTw4A-ezWKCEmlQ9a_o5qF6ze-9TYJEzlK_e4Tl0_77G8VN-NwHTru8yoK2quUEs0JhlrKf_m3LZWnkJz6Rye2KQWPWWzWaFgyDKNCkYI5zxEdTMbbaWHSt8nRkBXPyVZOeJ1vh4nmd1Au4Gfv67qecFgn0xEb_rEXCHv0TcteCjAi0WkaMrBTeDG_rFNnkillt5KDp3hyktN4qjdPV4L7RzVONeQfSZjd9nLH-UB6J_gnNuGCLR74UL-lbe5x9y4i9oygA7togdAABNB7QK1ShCNUM-jci64YBsd3B6y1POVuMDdmrzzToGfFwTiBWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇦
#تکمیلی؛رسانه‌های‌عربستانی: باشگاه الاتحاد عربستان اگه بخواد سرجیو کونسیسائو رو اخراج کنه باید 25 میلیون یورو غرامت به او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22631" target="_blank">📅 22:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOwanN-qsXHhPfdMfm1zCaWZX-h-AZtPBdauivCcIgkWOxMA6n_pB-KXGV9FQCLz7ThZtwzWD06oyzkOEZSmqtiL_5XVsBaohvkbpAe0YHsDOtywdhNCi0ObLlBQvd6dkWVXbjjfKm9NjsdpO1TJchqYBgOtFOo9W2KmVSWDa3kAF-ZXFlXNyEoZfDxtBiU0LAmp7qY9FW6QZIrgbUbdebm0Lgqm6orgcU_IBBgum18E7tVQzcAYdGsHPcZTyGXo3bNFZP5zHhSJG84GzVQNO8SMiRwENCpGs870VhnPa4nxEP6x7BB4xaFk-KM_ytzblHY3G-9yGdmK24Guo4ipdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22630" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=D0Wpqdqn_LAtt08tpTT2wSWgxSe3sw2SsMXv7n2c4XaxuD3QYo64N5QhpTRDBpemaAv5g7EVhotzGJF26NtCv5CxphcOWybT9X1Iwtp8sAcCKdNYRU9kVt-l-6DgIrqUFrmsuIIHc0c8g0Wf9-zapx3kua418-ZIABUJtpnDlpLAN6LS5caz5aCsIKiAXJZ_jECOcpL1gJNOUDRfw99prRp6F2qIxj00WJM3Mz_Y0AXEQeWCTSKnnSFOtyz8HklZiXGZuCKfwfW0diuCISyJzL-JAGoE66W1tJcvFzvLYexwUV0Qha978JoeNsL8H7vY5Xt3bVOztj_E2kCmaOrApg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=D0Wpqdqn_LAtt08tpTT2wSWgxSe3sw2SsMXv7n2c4XaxuD3QYo64N5QhpTRDBpemaAv5g7EVhotzGJF26NtCv5CxphcOWybT9X1Iwtp8sAcCKdNYRU9kVt-l-6DgIrqUFrmsuIIHc0c8g0Wf9-zapx3kua418-ZIABUJtpnDlpLAN6LS5caz5aCsIKiAXJZ_jECOcpL1gJNOUDRfw99prRp6F2qIxj00WJM3Mz_Y0AXEQeWCTSKnnSFOtyz8HklZiXGZuCKfwfW0diuCISyJzL-JAGoE66W1tJcvFzvLYexwUV0Qha978JoeNsL8H7vY5Xt3bVOztj_E2kCmaOrApg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
پرس‌ سنگین برزیلِ کارلتو در بازی با پاناما؛ حتی وینی هم داره زیر نظر کارلتو وظیفه‌شو انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22629" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=b5G8EEUSHrFUUnOD-H7rfgItFJzDmKR3ZEextgH6oMvt5CPyBNt0OKj7bM2tEjJUaZFX-SBspyuUzDoAJ1zPR8IztN4cxhtnDnl9iDwG5SpjVMIByooJBNZDtoswLxxuNO8ll94CkVq_Rn5EoKprI68jGOHnaB7xYDGhjBn9Xskx8cXRNOJwKI9H7xYvY35cK7Ov39L9gSBhNtW4M-X44L9YR21huvLzcx3fPaiaqcAK-e0c5QFkfr8uBabZCk2vkORcWtINjMr5sJ0s2PuuMPR4Uw4pl3wylR-3v-ASXiZPoicks47zL7vFpYGa9pntiynlfo9R9tYIk_j8_lkG6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=b5G8EEUSHrFUUnOD-H7rfgItFJzDmKR3ZEextgH6oMvt5CPyBNt0OKj7bM2tEjJUaZFX-SBspyuUzDoAJ1zPR8IztN4cxhtnDnl9iDwG5SpjVMIByooJBNZDtoswLxxuNO8ll94CkVq_Rn5EoKprI68jGOHnaB7xYDGhjBn9Xskx8cXRNOJwKI9H7xYvY35cK7Ov39L9gSBhNtW4M-X44L9YR21huvLzcx3fPaiaqcAK-e0c5QFkfr8uBabZCk2vkORcWtINjMr5sJ0s2PuuMPR4Uw4pl3wylR-3v-ASXiZPoicks47zL7vFpYGa9pntiynlfo9R9tYIk_j8_lkG6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22628" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S-MPjXktsdOH7OdyXLcQnPK6_R7Q5wSe2Iw05DdixyKXo9c86J61-_rCjytMVcCH7EafbRODD_2x3N87keSWC-y6binqfcY1n3O7tnG1yeRbF4LnxbGGdZTM1VBOYaS6AltgoaV6q1vf7IarAFxHPtr0TQr3L2oPzBTCmiQf_Fx9jEq2lo9xoD7_Mi10zIHduy6N-Y9q4Ww2ndPaaUKQxldON80FjP3hlCEPq1wrlzA5UqBZ6bJ7PlEXwIsYObI6Fz6VEgAoTWe-h3JgqbKEYWT8SfbWYhY_bZGVwNJTOLVYgIuXOfWplVy-UmcKXUycWXV7dvZLhsWpKpHTPaR86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NN-nD2EdCFQTDjHsTqabKyq7tqzMcgCE6qaFZA5eAoyzrP7pNyjCgnM9i5Xr49kV4Keq1XsynmQNl7c4iZfe87oQc8Ex2ivX2iNrR6UE78Y9ZR2NfNiRAw6iiIbvCTmymLKx3UG5NmZoeyw9La6e94TilgDfw1qbsDjrTeBF2wFVvLUGK_aj6udgkvq7d8gVChUTv7GqrXaTeQrNOeZkO_VtQFaay5GgsBspAhTD4xSEEv26gQxPpw7Fuf2DQ0Tx5hD1L9pPu9GTnunuTK-rrzVM5IC-nchmK39b_SCFUfplYKHfsvQ8EfcNoQSc44wNhjuRL7SOi92LKDlx4ObYgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22625" target="_blank">📅 21:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=Wi0EWH-81E1PEm2OKTXMwz_XDlX-K6vX94VPY4ocwJ_PSPnubsvc6SElg-SFKWB1HV6HeLh51KToI-L6raS2Efjd0nXGZBK6vUkUozxOotW2N4-2rEVJiKutZua5MKbsT49xaoxdPqusYo5ztpPrWfS1owPlnGOcJxNeYUTGaD4x1jdHZOzf9Fqze5l7fuvA9JU5Ap7LDMfB5Wp1J8nUGv9nA0dEVdJ6ttMCxLkDJzIkZZNGjWEkj4v2fdouVky89szdEDWcLVrbNJZ0rPkqXtjf91Wtxv7vUg8_O27VPkp9PfrxQ4DqDjsX9trZnges-evog-4WlH1B8GH-HQuIlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=Wi0EWH-81E1PEm2OKTXMwz_XDlX-K6vX94VPY4ocwJ_PSPnubsvc6SElg-SFKWB1HV6HeLh51KToI-L6raS2Efjd0nXGZBK6vUkUozxOotW2N4-2rEVJiKutZua5MKbsT49xaoxdPqusYo5ztpPrWfS1owPlnGOcJxNeYUTGaD4x1jdHZOzf9Fqze5l7fuvA9JU5Ap7LDMfB5Wp1J8nUGv9nA0dEVdJ6ttMCxLkDJzIkZZNGjWEkj4v2fdouVky89szdEDWcLVrbNJZ0rPkqXtjf91Wtxv7vUg8_O27VPkp9PfrxQ4DqDjsX9trZnges-evog-4WlH1B8GH-HQuIlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر ایرانی سرمربی‌سابق سپاهان خواننده شد؛ همسر ایرانی خوزه مورایس که یه مدت با تیم بانوان سپاهان قرارداد بست با انتشار این ویدیو اعلام کرد بزودی اهنگ جدیدش منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22624" target="_blank">📅 21:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c62242613a.mp4?token=AXo2-oauFgQwNy8sGmvFfcN9eq9flPk-fSxcpJIaoXl7wUQLpl5qL8shIvOOedZfyovX7wJErVUAt0WIZMem6-A7IxI2l8CqWyOWbIbjLO59MeUU-jjQXNl2mSoN4WY35LF09DZx8Kqh_17OrHD-xt4HX3YOcC3kqpS7Hdvf2U_WOej9LWZvBBldzT4IA4_TUVn3NZpGDiQyBJYoXFvlPeAuhChQyse0LXKvNpOuvoXhKuhmaUZzpHnjzqdLGWYK-D-8k7IzNneR93lefK3vfM4k80RC4VvG4VCI5B0TZIxTgEVsFUE707Qrn2_RPDVm5fFqPgOuVXxuYq1teZbVTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c62242613a.mp4?token=AXo2-oauFgQwNy8sGmvFfcN9eq9flPk-fSxcpJIaoXl7wUQLpl5qL8shIvOOedZfyovX7wJErVUAt0WIZMem6-A7IxI2l8CqWyOWbIbjLO59MeUU-jjQXNl2mSoN4WY35LF09DZx8Kqh_17OrHD-xt4HX3YOcC3kqpS7Hdvf2U_WOej9LWZvBBldzT4IA4_TUVn3NZpGDiQyBJYoXFvlPeAuhChQyse0LXKvNpOuvoXhKuhmaUZzpHnjzqdLGWYK-D-8k7IzNneR93lefK3vfM4k80RC4VvG4VCI5B0TZIxTgEVsFUE707Qrn2_RPDVm5fFqPgOuVXxuYq1teZbVTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
بازم‌ این‌یارو با هوش مصنوعی‌ش اومد و اینبار فینال چمپیونزلیگ رو برای آرسنالیا اصلاح کرد. اونایی که روی قهرمانی آرسنالیا شرط سنگین بسته بودند دقیقا یه همچین حسی به این بازی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22623" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtX7EPy7M60XpjcIlbOHvTGmIH5vIdeugzbaCyllKgzKtT8XVzxKLjPj6w8yeYig4GTv-kMu1aj6nVF7xIdFK_xUkczMxcbdhMFhoIXbZLEHSfwlJudjlSo9y_yVtHTWYKCc2amdQkI9R2OSFWsxtaFinr-3PSTbXwrkUQEJiOmOqhs9QffPnQpTGBGRCYQUyNtFxblWJl-NKmK4VvhldwrA09g_1FGEwg36vWTgqK3sTcWxVM3w3rn_zQaZwvULj_D8D9K4UIKS7jNSyI0299B_Xk2jIcOCvB_4cAR1xT1_ohbPtk8RSULiwrK145arUVg9yeK9zbl3Jyvr8ZJTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22622" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
