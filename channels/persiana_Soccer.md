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
<img src="https://cdn4.telesco.pe/file/Yu8IiDtjtDBz6CJlqh-OZ8aUXrfjmQRoYRmSET3mXIxa2rCI167tw8Ef6aQF4UmU1-Bousy9mx0ZU1-PrzuNJAkTzUq-A9CajtVP_Mq-QOonHJ01_YfljT34rOWNUZ_KyNx3kUnx4jM6l3RpOcN48FkdxArvsoK-ipeebp6-Y5UI5DG4AFLVXX5d3f3yuRJSHQcedTjRGhOJa9VzW7NpFIt-ojkG2SKbcfNqfGfvGZcXcfuCysB-vEOdO-xe63Lr5-OBv_bSMfJW6ezwmxsB9c8om4gHeOqGMyfJOljS72rjNtlnN72TaCOKN9rlViywMmaaRIF0SNSV_OTREiDXTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 605K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 01:04:36</div>
<hr>

<div class="tg-post" id="msg-26913">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucd-goZn5RzXxjI0NNznZHLTTcwaHqaAkNmnlVmVLASUZ5ODX1TVB9w8HITFOgpzPnm90Sob96fnC2U1hTu413-rm8kPwuuPn4ZORMjPr6_P8Pmo2uMJGiJpyrY5kJhLgBHma-zllwgyJU0CbGEpnn-ouqQXx1fEH8rsxAJQk4XTNZT9fxX1YVflm3ykKd9tvNhlQ0CEUVcT5soxxofE-Dq2sR7JHvR0FF1jWcuAu3jr4GlDi5PjWBay8etjOskIzLWvwKMLaE8Cd-1FOeBHI7K0X4_KZh96LZHibSUDK4N3haM68GueZgORGOarx27Iwe6s_jP-Q_LmvlLngx3CLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه آمریکا و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین حملات هوایی تاکنون علیه زیر ساخت‌ های بخش انرژی ایران هستند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/26913" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26912">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NouTR0r7ByTgxyBm-WcwnOhMC0YCwXAfSLYYckEGuJohr9W4pGdOPnM9xL3VIvbw3q6gGrozAt3c_0JlOnpDmA_4FxQsyAcaZw7wRjmzQ7zAcoqB6DVn0TmoWowANmFyIE-D97RqsADK_HiKEZz139Wsx5A6mJc5ydSrK9GQ4eBa2LO5wmh_TRvGXzOmPh33dQKi_5stvnnvj_BjBicOrXomY2hItjmMtzD5c6Cn1FiS8tL9jnyR3gQ0cpaeiSbDbko7Z0mLTRI9KOFc8EiqyVZycFuKIRosdTKCXxxOkX-Yg7vdsXB3HOeeI4NaEqA6jR4xfF-abR7CMRggJPPLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
رسانه‌های مراکشی: منیر الحدادی ستاره سابق بارسلونا پیشنهاد باشگاه الاتحاد طنجه مراکش رو به دلیل پایین‌ بودن رقم‌‌قرارداد رد کرد. باشگاه استقلال به‌منیر گفته‌برگرد سالی 1.5 میلیون دلار بهت میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/26912" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26911">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flZP_YVipT_xRU8jU1DZ2ZItE2Y-46SGmrGlPEKXkp1pnTa9CHPxOH5HJtnS9TOFBAeyYMFJwOa7qg3ODv7R4UYkXPcwnMfGALsIVwh_QtGe5ldXx7ipGdmKI0tJkdCIxP7Q0U_1oXA4VxskGIMOm2qzcMNUP_Fp22lwymHVhsIb_a4rU1v6ccmbpqadeM2XqJub7QbcRg4_IxGCd2sF4S0EmHPUGAhYlE6Nv6FeRHJ_bZbH-Ol3bWXQ5EL6FpVmgsNt-UPFZk3PpyqqQJPCKNJMiBY4W2KWYUvnxtiMIo55aP5w9ViNjlcPU6NgPbNJM3mhlEXKc72Xl75hdAlPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛رئال‌مادرید بابت‌فروش‌بازیکنان آکادمیش درشش‌فصل‌اخیر 440 میلیون‌یورو درآمد داشته. تو همین پنجره هم 196 میلیون یورو درآمد داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/26911" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26910">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDx_Zpevxb_8Bv0V4ASR_ZzADf-5v7GdRZ_2QBvjecruRdkjsJ2onDDxyIleT5IdYGwnZVaJVed6OuBcIRJavyqXY8OhI3T3ceJbHStY7klYU4MflKRzBLSzpJiOhyxXFOGtb28Wl7zVuepbbb6YBR47k1j4m-E4Y3XGmwfoOZ0BuNd0Yi-pSJqTQ1iQgph4VT2EX4LtEmljaQuSOX8KBGDSCNg6GYktmVLrZuTigVQDCgthW6QdlWbjjQEPVf-9K027_mkZqluTu_l0nyeGT6lvNjkFQII-MoDB5pQSFgnvmahJIKyzHqyaSkGTFTAhooPeHr26GXYGRWvvssbDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/26910" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26909">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAKBkyGMQhZqFVkWvR824LmE53JHl1BRWnUj-D8UYt0nt4ysScykwIJCKViKUvmNxT3GCeF1LvfSGJtw1ucmdWLRYYStmeu_wYFAduHLHhTEYW2NSEOb8s9P9Z8MqujlXerrLbuFk_f1WkLABYlOgeAsidj8qpOAkwZp2GAK5CXpG90r6UsDPSkvvIcqLMPphBpCWw5p3ncWoS4dabPfbTg2ekUlXve6qFIM54m4VAhoFEQIrOkrm0Q6RYBIeqcslbE8aMiJs_kHr67xPHLdrhLxgwqEibrdLHS4VBat3v84aXoJtQVUOQoRXh42dRZvbpwN9ubZHR7HKnmBHrAJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/26909" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26908">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1MOJrhXMW88Orxw5asXvDN_CzQOx7L4qWFwR3jziJf6w8DyA4XEKt03JDhmDzADghPnUhpMdInKaKzgLN6PViVlV6N8o-kQ8P38_Kyrh-oMwJXPgpyyzkXBbumhcqCqe4shcRWNqY5IxOHHmxPEj132HCDDNTmLse6d4ZJiGpN611EhwAjKpxJCzrluepf0ZkIZ033E6rwABoIFDV-V3ALIxSE7okBINbL220VerGTCBuWfxPpC_Ze8KZ7U0HxFeOI7NfR-BliVRpX6HyTAqbgP1fb61K0-72M7TDrODAor60Y2mcKMYD3khKR-f4_5E5UI9V5CbryDcuFGxUjbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/26908" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26907">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEwL5_OZhQQbpGr4gsiCVIHgUtuJSbG-AFljFlerMuWfN3JbSb5rIeFNQHDpOZfPVQzdydI1AxthCLW1qeBjxx-2GbbZ61yM6yjTLyXNgw9gMOXb8lDGaZaBJiUVY9hz_8fAOgQ6bw73IJSnQY-Q6QgqurBUm2SiKFQL0D_giPyalEFoPk98OEmmUQxkn9t7uBYYXFOez9lOpBl4XVIVsDpPc4ZOv7xT8Ro4RHVgchkrjSWAyw_alECLXr0IIale7l3UVTpr4K6NSJgWGlM81x-90c_6uBkUA-ypGyHUwQo9vVxF77wRU6e8NUkkXbTe80fSA4NVjlA9S-uFRzGkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/26907" target="_blank">📅 23:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26906">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇪🇸
خب گویا سرخیو راموس اسطوره رئال مادرید هم‌تحت‌تاثیراستوری‌های‌رامین‌رضاییان قرار گرفته و دویدن تو خیابان‌های شهر مادرید رو شروع کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/26906" target="_blank">📅 22:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26904">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBzZH443Fh5-dmQfHD2wn_u24skfpgIxuLYE10oHQtYT_OP-lEost3YOiYUWUK25RfeHNC1FcJMf5F7er40UP-lKcJz9GZYCwM7GmnErAHxp109i8Yf9wAQRvkUszAouMIhbpbXcVGEhL3BHihuhx6iJuMm21dqarYFdWcotOUKdWmfesNutFE7or_nk-ZXBV_YmR3FFk1TZWOtJpCXboYqx73wruHtmkonNEGH8tgY1p8j-iS76EpsWcknaZD1f1cLCYzSx4tIdj0b8j0OIB4uF-wUXy8-OfK6LrP_Yeha7-q4czZ4EQhhV-CVMlgPMECjdvmVaWaA25f6Gk6fF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/26904" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26903">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeGOQ_LVlCT-tmReaDAfXPAwJTkey-3XxTc1esIs7kMVvRY_f5047n1SVttLjSV72SIGu8yIQIEPZLZJt1dOkHT4-rcaCEXEzsojT5j5uBd-szCGlveWomlBckz3ni7lJhKLaRTIzeJ1lGnRC1hZpQIwFZ_olJyN-fHVuwpRS8gvYw9KgXx7uwKVhH7OkouquC2YBC9i6W451GLJCAh-vqRYpMxIJFxXPjE27wxmHv9s5gENzc-FqAieKych6gPWjSgNzkClX2SI3QoZcIWe7yo4jDlx7sjcbo8dez6rMjK76kxauJSRE86ryRsqRWwOABffAmqNW9ah4kncN0KpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شش‌خرید قطعی تیم رئال مادرید در نقل و اتتقالات تابستونی؛ به این لیست رودری و الساندرو باستونی هم اضافه کنید که در نهایی شدن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/26903" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26902">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIWYFehRZE-E0F_uqiSc6Kik_9gjcKpHIFiRkTIqeBEcvB155j-NsqahyASf1wqNVepQeZdBexEdzD23pg6QSMJiFHxyfMLTnPze1v86CqxSgOe-xa5Fdrx-XM_MP6GxV4B7t8iFoi3j50iHxaPtFby_1R52gPY_HKGy4C_PUOKeX7AWG-oeaHvXbcE1bV2VH_CEUeSusyb8FZqexNb37p2fSqGv3gL3EkCdi4ywn1xNEUqT9CZ5zsAE61OrXgQvC6uHJdyj0WYBVUNURwFZOJDpDWsJJCN5tM9OGIOG81GVUexudeGHpd4zF3ZAlp__UYLR_AlfEi-K-8i4lJ4Izg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سلام رفیق، اگه eFootball بازی می‌کنی این پیام مخصوص خودته!
🏆
برگزاری بهترین کاپ‌ها با ورودی کاملاً رایگان
🎁
جوایز ویژه برای قهرمان
ها
🤝
مسابقات فرند و کواپ
💎
خرید و فروش مطمئن اکانت eFootball
👥
محیطی فعال با بازیکن‌های حرفه‌ای
اگه دنبال رقابت، جایزه یا خرید و فروش اکانت هستی، همین الان به جمعمون اضافه شو
👇
🔗
https://t.me/+2oFLOa12FAs4YTJk
🔗
https://t.me/+2oFLOa12FAs4YTJk</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/26902" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26901">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfAAYoSdIp3tME2ggTDuDhBd_Zj7UZuCiBuXaATYXYZaVC3MjDAQyuqvnlcVbH-A7Z2HiLOwcYKH9XiVyv7iN7zWSJcuzpDZaBhoZMLk-ptbY3medJ1ZrducDhFVOs7HOtmlL0xMaxD0NVs-SJp_eY8gcXcqYIxYFoYnxG8u83kpN4aZl7RTnb-V32HdQgHhWlfA3F2-ZXMbkmxCj6OOKlVckp2YzrQNiMdDp8h9UzhR5C4OB0JLeEhFpC5-lZPviI8duBE6o7sfRKkztbetq1sBNf_iuapzbRkOzGimRpIJOzL2KXzshwO5D7YPUbYPkQ12tyl-iEnfrzirqxDLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/26901" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26900">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDHPhcQueMPYBEc2I3MO5_j5ukORb837hEYI81CQoIcmVt0HZ74JE5FivLOLp9K8urFTcWc4E496wfUo0QUd1KeykkjD7h59Qhn1wdJpZLBcQe6biXefmbNfZ-McDarNdBk1djsE-AXDJdIA-TcMK1ppZlOH4OC7rfZKaeiVlrjbrOroOz6Txs6lqOBAHQ0IcP0KL5NDLZ185fUIIfWJZEL75edPoipChM86v6zNCQX9RO1JRxhXOQ9DSMZbE0gbs1aUT7lgouJCUeURYrvv9Dn_uyRFA6ABcoH6OhJ16HsOHm9ljC3ZcnRiOkTucx-OSGMpTBRAbumdDK7Smt8FbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفامیشود با بازیکنی که 6 ماه از قراردادش‌باقی‌مانده‌مذاکره‌کرد و حتی قرار داد بست مثل‌ همون‌‌قضیه یاسر آسانی با این تفاوت که در حال‌ حاضر پنجره استقلال‌ بسته و مدیریت آبی‌ها میتونه الان‌ باهاش‌ قرارداد ببنده و تا نیم‌فصل در همون تیم فعلیش بمونه و زمستون به عنوان بازیکن آزاد جذب بشه و نیازی هم به پرداخت رضایت نامه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/26900" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26899">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzm5m7dK8V6tganEY3x-l1AfAqIizPLtFZ1986aGdqixA1UR0Zhp0ZfpcoCPuQj7rv4iCo0HiYFI2tqY43h8hkDYVbf8G7IiMVYW5gMMkY5xs6U3aeshWjxqHKsHrYwXDns3VSTid1TqYAVmFfTfuShMSccCoasHcP5iKa6vICbci4n-JLpc1z2H4gpwl8OYH0F9wQ_nDDue_oGGgJKEELqGPAhRqM7GiiZZ01s4YoFT6_lUDnOkc7UM3Hskv0NhZa5ty3cDemrGuhtf8Vp5PD8JGg94voynRwWZF4xq-9vnvSQYaV9ZKx9hMyyhNc1dFAFgxhOLzJ0XTdT7Qbszkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
براساس‌اطلاعات‌ترانسفرمارکت؛ تنها 6 ماه از قرار داد فابیو آبرئو مهاجم‌ آنگولایی بیجینگ گوان چین باقی‌مانده و طبق قانون فیفا میتوان با این بازیکن مذاکره و قرارداد بست. در فصلی که گذشت بااختلاف‌آقای‌گل سوپرلیگ چین شد هر باشگاهی بتونه بگیرتش ضرر نکرده است.…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/26899" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26898">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfUBmioy9-K-Xi-ZqisNuFJg6c4BFfvzyn64lW6an0cHWgb0N7eLNmnvc0dXlb0OzLxqjcu1nHXGhqbm0SURT2Cvar7py0wtHxjepwVIdoxk4vgwMCykroBFJ_1ueAgXrnqSSPblqSJK4IE-P3zXUvQZEYmaZC9E3mMr2CyBiL8UbXhvmF7YYF8EqROnL1zyZn0SagN51b5DrfPEuY9to_P6egmQSwgphFpeKJAgduU1FXBTd7msNYuqD7LVB_v2Ht8j8-C5ku8QXrRp7g3tgMcNvX121T2HUBvAvBitbCnpZT_IKy_bfJ-JounnC6_D5Me4JcWECQZocZEJwQb82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26898" target="_blank">📅 20:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXRK09w_PkQlexQ71qs0ketq8WpEH-3ozHeP-Dg1zDDQbvoIUc-OjIGv8nvz6N2SoeIzRkER8IZ3wtxf7gKg_x9M1DVFdy9CPRmYrj2jrYsy_ijIeyKgqIAvMy6MLwgwvzt5nuHQSd_HJeWbHDvii6RWMs9dDJWyeNdRiZi7mSQA2zxEzhbVmSqssMGY0iH4E1zlqgkPQ-VsSqfjK0_h1HrzARFVP4T7MeVWJG2DD97ghx7eQkiZRa6MOphhc5Wpt9o7jBBONldKfHUwL93EU_VVKiHl4-pxS0VLS1fkiAiIYlPbO6UbHV7gp-cGg5qP6ntOxFPoBkL4TqWKS7QtHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92aea27557.mp4?token=GR0uohhauef2twzQMD4bsMiyneKa_W8xZrgyb3JQP7HjCHe4yQJHmXLkYhfN0OaqKLp-Kn9vDI95kbfpyLz7_wQj-1cwJXyglcIjaYUE61psfIfiAhzvDMgnh4vmuEh4NLbXQH7c2a9LtOteVWOFwm1Asqn84WC999I22t8Kco6t6j8HQY2TeLVD3kqjiXGVYYy5s6FO8V8FaHUWEtEAYMfAxCMPVwrZK3r5VuToTT3tcYTUOBetm_aJU_VfyG3sK0lZ_MozcGWT_MvGXqPcuCxcZxC6hjm02wC8tQcSW8YqtAOqwi6sbV8jczaFLppWerAlcDhU73PRvtAtq54HqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92aea27557.mp4?token=GR0uohhauef2twzQMD4bsMiyneKa_W8xZrgyb3JQP7HjCHe4yQJHmXLkYhfN0OaqKLp-Kn9vDI95kbfpyLz7_wQj-1cwJXyglcIjaYUE61psfIfiAhzvDMgnh4vmuEh4NLbXQH7c2a9LtOteVWOFwm1Asqn84WC999I22t8Kco6t6j8HQY2TeLVD3kqjiXGVYYy5s6FO8V8FaHUWEtEAYMfAxCMPVwrZK3r5VuToTT3tcYTUOBetm_aJU_VfyG3sK0lZ_MozcGWT_MvGXqPcuCxcZxC6hjm02wC8tQcSW8YqtAOqwi6sbV8jczaFLppWerAlcDhU73PRvtAtq54HqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از عروسی نادیا خمز دختر خانم پاکو خمز سرمربی اسپانیایی سابق تراکتور به پارتنرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26895">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfLMr3CqfhseGB_zFmjbV2LuQX7z5aMVNn8orJdB1YuzcMFN2D91hNswVDGeaELq99ErmJLX_Cs33YoWT6UfOspyZsJR0xf6BM1wer-xEtr0QfMw5xS5KdG-6gmjCA2rE_6I9mmoIuvry60WPml3lvNhzKSwj8wd6k94mPRGZtAG2vzBZGCZ39hhlk9VIy_dAkq0Yc4bAEpBjhfYTnrH1qua8lLwgeKcCMUAnyMcLManfyufNX5U-1Fvmp_63WMxnby2B6UvHRv1FUcV3LLZScXnMNL-hH0iFUe6kyCBwz_J55d9mFO2Tvi6PeTAHG3_UPH9u7GCWikfn2G4UqZLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/26895" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26894">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE5YjafaXq90Y9zhDdQCo3slCnI8IFB0zrgnydVCqII9oYueFpLGIgGRluuMgcyKWZMgKzpqmjZgoYn1jNGKF7TrE9nzALsVpPKVKl5RAD_RAVFufEMlQEAm8cTle_vQeJTcJpEhpMCNn7zpvBuolHWb8zBV3XEXOb9UjFTQkwRIFgITFFP23Lwjb_4Em7_FiZpZs-8b5DG-nGU-MFihQy7I5P5XcaXccgEvEwgU9UDO6wgBTSQtKocgUZyf7wmmNm89LxTl08yrDFe3LkkYcDqu4_XkUsrVLD59QsnkWjMsbvV4eANwK1FI1kNuijBU7RFh5pK2xhE7OVS9c5Dzkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شمارش‌معکوس‌تاآغاز5+1لیگ‌های‌معتر اروپایی درفصل جدید؛ تنها چهارده روز تا پریمیرلیگ ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26894" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26893">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArvQwunyWzB-O-IoM9HHA8J25aHLfzKo6JRlZvCHIhyc5AEiJAMGZCv1TXzH4pmJO4GJtdh9lBDk2sRREyqI0HeYbFw0hVkZKbpGbgbUqfS5frdMiCmv_EbDHhlWvghbX1UEJIeBzVDk-ijIUusmZY63vuCSRvmFkzabduWRAM8px5yJKzRgEyIp63ZFwRfuwQwtPHL66SfEP3fO_BqHWT8Y7VhEDi_t7Q4L_EM9XmAEUEeJXHDhDjljMzw19YEVGn6lfjwenJmr40HofE7lTZjaW-ufKUm4bH2f38ZZU0_03P3KyS-zJoVCcYPrCpmKvcwcYZd4qSUAOiLNSnWx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکرد اشرف‌حکیمی،ژائو کانسلو، ریس جیمز و آرنولد 4 مدافع‌راست‌برتر حال حاضر فوتبال جهان؛ رئال مادرید حکیمی رو مفت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26893" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPJU7NZX1brCgg8d6_-PZRmoaVNZgrZd4M_VW0V_VMyzPQLBwkaSKKBG_H2cgZoCoE8YuFjuRslrnBTKBWVHIz4W4Mi9xhWGe1wI-ZKJ_EXJh4SLQBfoNSxJxDEehzWJzDQuvVeVnSshzS3fh3f-2rEnaz5QsrNH5b9hIdjE5JcbKzQ21GDSk2x80W_hplV223AoYSLtoZXp641_YqZjZmYvAf9_ERbgytPFwfwBZT57S9PWOEKK77d_1b0g9-8g8IyIe-cZutKVyMAz1-oV1TPr85A0-GBxW3gkHBns9pB2ASPkD-QrPTMrjX3HDvHB1JFJr_mU85X9sheV4viFFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیربرنامه آنتونیو آدان؛ این دروازه بان اسپانیایی از تیم استقلال جدا شد و درصورت بسته بودن پنجره نیز قرار نیست قراردادش تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26892" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26891">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv50TcRvy1Ccr016CSCW9LuwwVhCyzhR23zDXTeOvUb03v0OGnpAVrNnBU4zWiGeq9ZJF7sNlwGbvzN_LyXrpY_SnfxgRzBKqfXlt5QJrljR42QbVqjD_SudEuxCJdovShFqKumzTSgFF3JID_n0x-5hhTplhn945N7UE2LkwHh2EaM6IkLIwEXV4dpa3HoXZVl4yuTQkCzzIyQ74CbYPBLIEWmoQ-twgqK-SkdMJ5HkRcF4uHghl8IamKFvkV64QYqgY8A0unILdnww7p9QtYOM1btlEbeNKpZyQPU1YTNJbc-oKvwd_HMdQZQvRg9MNjxoJ-bRmegH08kG6TdkqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/26891" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26890">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⚡
گل اول استقلال به   🄼 TAJ NEWZ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/26890" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVb-8UNxqbvo0PkplW37BTpM1rSeMgLTLTCvZ_N5qprNiiyBWMD9qZpRz7BVxEysuXtjhSFqxjvjDM4OIm_PPkgCPpD97x11_vUhEbUIj0wXZ6vc_9WOctsUdqazCSxFqbpVyrrFT8taWHCZdhQU3TJ6vLTTt2Yjk7oI3_kk5wlbH2JKkdR_aOOtewGJeX7ZcxQ9idsjZg9aK1R5GXRaTT0S_24pbBjXFrC4OGi2EYVQgSmJabKo1xCJ1wy4eiJjkijeu9vEKofsqih9A7z3TLSBewjHDY6X2-r7LO8VePwwfKyhxMtB8VRitWKEJPDf7bW2HDmGXuyHv1zhF2QrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26888">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2LjaSX4TZx_Mz0tv2dvoiOebtwREv2LxcNJjwfaF4QDkmH5mRchaUNklN44Tu6-PkIKyqLGHm67LrUEywZCtDkGST_KbJT03Wa-ed8moAsmilPe1b870Fi9wKvHuBS320TUdbFg8OL1o9JFE1yF6qUTwvjMcYUyqcF9Kd0P1V6yskSyf6oNLRYTGLCHd6Zlx_mgHmuaHEkycSnxdJg02bPA2tfLw7AatE58vtNHBegtv4VfEU1f2T-GjCUoAMMKiV_1I7z-bbnlngVMfcnHU0Elqhw3xIqyEv_roNRU3F2cDnBDI3eIiWOmbBr92y3AV7d4E1GEj7hgxEuswzAJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇺🇦
مارکا: میخائیلو مودریک‌ ستاره‌ محروم‌ چلسی تصمیم گرفته که در رشته دو میدانی فعالیت کنه و هدف او نمایندگی اوکراین در بازی‌های‌ المپیک ۲۰۲۸ لس‌آنجلس است. او تصمیم‌ گرفته‌ که کفش‌ های فوتبال خود را با کفش‌های دو و میدانی عوض کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26888" target="_blank">📅 18:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26887">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی از مراسم عروسی کریس رونالدو و جورجینا  که‌توسط AI ساخته شده؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26887" target="_blank">📅 18:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26886">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCXmbs7eKPLSvWQgk1raIgsTqQ3CQNAkl84XBdVz-kNZd_VZXmQa68bbk4e7psW7uDT-JV2n6_aGoC19Y_UHCUwBfS-wV-YXR-K3A58A5Zl0AXQgDx37tXXIJFbKUfxOtBTit53KTQqP16taKtrHK1Y99b0MpPT-0vNiRYGyuxRAb03sJevpQ8pR4dbO6jBzQp44EODZKjP6AQHUugbnW8ZXoBbTZsz6GBKL6xC9HM6m8XAmfy5_pFQCnE1G8eRLY1zMFJD5yZLo2_YC-oNAYop-s-oyxdTBCu-irrwjaYk_1uap4XPUzqoaptdE9OG1KCP2wtF8HHN3NZYdGBNBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26886" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26885">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omwCO2yrt3i8U0EkzNl8wORqFSISTaQy5Zpu06Trh_g9Z8f2WZAjKupHBxrwAK8bvc9w1_AB2AuDXzrMAoSzGnT7KOVuXR9BimihRUvh9EKwRKYVofedbejZnzH7Zu09SqZTunSeAqJw4aTc9tXakMC01-sDD47CxmMvr8orbYnAudZzxa5rqzEg9bN_iohSBOrfDRYiJXb8gKAwdkjjzxTPk-8U1roymi7UEcZE3MJQY7HCig_Wqunp71yGiZIwf-L0B67-ktr25KPgzJmW-mNZNk82IbDXV17pJe2Z8xA_8tt9ZIpvq1TW7qst1C_Ru4TJNJBhL82i78JNFCHrUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارمعکوس تاشروع‌رقابت‌های داغ فوتبال اروپا؛ تنها 27 روز تاشروع‌جذاب‌ترین‌لیگ‌دنیا "لیگ‌جزیره"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26885" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26884">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtsIW5NpsgfkL5JGESlOU_A6GmUJY0VEvknv6uzpK01YziHtmXEhyC8jMJF_UArq1C0YY91q8-OjvRE4Lcv3VSyM6M5ZMEO1sxifOsbfd7tpakyVdZm8QU2ycWKWunrdwEdZKmxp4K2fVqB6rcsuSKTpQvRKVkbx1vkE7r3zyOmzBsOXQRvLxHtqWhcDzvhDXlJr_hfSIRY_nauzgISJAJ-EEsjLITXt54F87-7jVXCP6eoW2eM7rknAiBir5WA47OrfOuhssVbjdTdesxaTUsuvxlNQY8ZRy5l7aux_SQQTPaybyMH1Im7Nr5lLcSXui6cKTLAB7B1YtGZm_ZFIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26884" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26883">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLomxXubrDMS_9pBnIKHILoys0wtjNj2sZWFbcPkOsI4E5u16qfGEQrCUJUzvS_xWdg8nsuEwZLUSnCrf5G-bN6YkGITzpmzhsSCTegx8pJDUgW71yOp1scdtaYIErmpIKD3FwZuBMzf8jJh_qItEh61bXtDd_g5bUbo1ZgZAmQ1rtdlZfrQbIM_l-eHf8BQYOr_GiABE541a1smJUqGxu-06WvVLbUiB8eO9DCx5yBHy9gO8qlUL8QztTvecXLmSKRiTai6lTo26flNyif5rnw7S8V_kZzFs255DUDvwk7ec_Dp-0DJ0yJZXvFwVZN3Ve5o7AKKzleJMf-k8Lpafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/26883" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26882">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqBhWOM6Ntaxc-V06H4P89ulWy47vGgrhHLo9AkuFKifuRuc9VvnrGYlD7_HKfLKpdOELcRxNRVthBoH_upW7t0h0P8bswBJw3YUN1rDSXqYnAuNj0HlLDuGUU7sGp9S0j0oAsEdOZjpY7LvxaL3j1r5TE-dOWLCp8VWr-K6X_QMNB7q0hUntwFW1bbtI0F4GxFUHAM2qJJ031Av0kO7kOMYOVnruU0SnRY7bgOB-WJ55kfAnUKm1XjHq8dLIxCcRuc4y3n5CAp1iJL5gjkZgpfYyipJ7jhhBjQ7IEMM2_P3jkK023PnsucitevYzeBExJAg4wk-wN2_jEPqXjbMbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
وحید امیری کاپیتان سابق پرسپولیس برای عقدقرارداد یک ساله با فولاد خوزستان به ارزش 25 میلیارد تومان بامدیریت این باشگاه به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26882" target="_blank">📅 17:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26881">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGJP5KF326jXiIQsSwmQVFTwJVf22MhRRTaiH8WTVSzMe6va0v3tY1jquJSfxQXxwR-B9cXB6pt6OkKxKJwJ0DaJhQb4YKF_r6q6g3pwzo6vUKxPNOMXKSZv5vjT3pyB8CyqGmvRRgj8aam9oIr16oZ6hmXqzlbURd0Ubvc3mU3uhETmdQERbFUewAlQKaq5ZKKhjzNcuhee4Z1ob2NEn4G_iwHyxKVrhvEmdR1k6Qx5H1OgzlJndkzqNpFEBo4m4WLxR4N3xCrS3BGDp6hebQ9mUBjKaOrEvyhaUaWFqBRh3UuYJAsMYZC-S4j_LYFbqH5VqeDwecImOfwvdyj-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوتامندی‌ مدافع‌آرژانتین:
دخترای‌خوشگلِ زیادی بودن که عاشقِ دیبالابودن‌ میدونستم‌ که اونا از دیبالا خوششون میاد، گاهی دخترها میان دایرکتم میپرسن "دیبالا پیشته؟ رفیقِ نزدیکته؟" سرِکارشون میزاشتم و میگفتم:«آره بابا اتفاقا الان خونم مهمونمه! میگفتن میشه ببینیمش؟ توروخدا، میگفتم آره آدرس میدادم و تا میومدن خونم میگفتن:"کو دیبالا؟" میگفتم رفته بیرون مغازه خریدکنه الان میاد، بعد از یک ساعت باز میگفتن پس کو دیبالا؟ چرا نمیاد؟ میگفتم کار براش پیش‌اومده‌رفت‌متاسفانه دیگه خودم مخشونو میزدم و باهاشون دوست میشدم. دیبالا واقعا رفیق خوبیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26881" target="_blank">📅 17:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26880">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fak4yjDGPfHb-GVm5gb2574uOvRnpNmHAprl1ksP7xyFFMT0YQTOgGkXP5dtny1JhMfZwwdc9ajcidvA_V51Jj_CzULeUYo-rFF_899zUUKoIgq8g8lWrnezfoHtlWz5-jFfEgM1VKoJD8Vzs4PjXJml_hkPGjiOuQ6HpclHh5DlTRaWEtPMhkQeCosnbgQFDivuZUmMMfnqL2ge7OK2JJ0bPPxKTwYGpmJ80IRW1TpbhtbskGA-zub2s5wH046450EmdDJ66L1sVMx2wxKZZkec2j0GzLczTZlBkmKxM9n2cKLO4MhjEUBIohPldkt6SFAzGirw48qz3n3KOOvBBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
#اختصاصی_پرشیانا #فوری؛ امیر رضا رفیعی دروازه‌بان جوان پرسپولیس که در آستانه عقد قرار داد با تیم‌ گل‌گهر قرار داشت با باشگاه شمس آذر قزوین واردمذاکره‌شد و به توافقاتی نیز رسیده که به احتمال فراوان بزودی پوسترش منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26880" target="_blank">📅 16:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=g8qV-Hez9h6eiDuF-r-BeiersuZ1ifFEP0I79qEVc4442abrmzxmyRvDnM77I1yzM7LR8bqlWiVd_YcoHSkoN89aypbvmMSmFtLgaCiPIjM4wAZHb-X8s_yOk1aDswpOtf_Q0ad5UlnxuI-jhxG6XId5rTxq57U-XaMK9Ah_rVtFuP5gjH2NYzovy484gdqCPPNN7Cg2MEeVWxpiAooL_Zf42jWk07CtY3QVv4D3llsxZwiIXYWgZ_uYLwG3uoXKsZsid5cJDCPxD-Xx0mi914fM1AKTQswoVW-tSzJJlQLl7ffr7AqMb9ouH1p1jufJP_atrud_dlwKH3XP-sMmGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=g8qV-Hez9h6eiDuF-r-BeiersuZ1ifFEP0I79qEVc4442abrmzxmyRvDnM77I1yzM7LR8bqlWiVd_YcoHSkoN89aypbvmMSmFtLgaCiPIjM4wAZHb-X8s_yOk1aDswpOtf_Q0ad5UlnxuI-jhxG6XId5rTxq57U-XaMK9Ah_rVtFuP5gjH2NYzovy484gdqCPPNN7Cg2MEeVWxpiAooL_Zf42jWk07CtY3QVv4D3llsxZwiIXYWgZ_uYLwG3uoXKsZsid5cJDCPxD-Xx0mi914fM1AKTQswoVW-tSzJJlQLl7ffr7AqMb9ouH1p1jufJP_atrud_dlwKH3XP-sMmGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛ فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=QWtXW4ckxMS_Z8LxcjzR6tOjnMTj3QAptbwYDD5_DcmqiyLcgtXEQ6sEPu0yqUFD2YilgV6E7Mrz-j62ubBbyF7PSEl-wAMC_l2_yn6jv1FJiGfKpL2T0PaA_uO2GBUTZwix4Uu3GdzM5zj3PcJX1v39b0ai4datnyHGvvm5OnsnoDX2gdJvzeEwbwQftggPiVrqp374inqbzVKpA1YFlhNphcD_KFfePWb5WPcOUMkHOLZW5MlgFfLF2x59uTo3ap-sx2TagrdBTgm9T21X36s1_WXAHx38MPXHpoA-36cC9kWqsbBA8HdoF-F_4zgj6oTSMLcfHeDqM_dxBIlbgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=QWtXW4ckxMS_Z8LxcjzR6tOjnMTj3QAptbwYDD5_DcmqiyLcgtXEQ6sEPu0yqUFD2YilgV6E7Mrz-j62ubBbyF7PSEl-wAMC_l2_yn6jv1FJiGfKpL2T0PaA_uO2GBUTZwix4Uu3GdzM5zj3PcJX1v39b0ai4datnyHGvvm5OnsnoDX2gdJvzeEwbwQftggPiVrqp374inqbzVKpA1YFlhNphcD_KFfePWb5WPcOUMkHOLZW5MlgFfLF2x59uTo3ap-sx2TagrdBTgm9T21X36s1_WXAHx38MPXHpoA-36cC9kWqsbBA8HdoF-F_4zgj6oTSMLcfHeDqM_dxBIlbgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی کوتاه از یه مسابقه والیبال محله ای در زمین‌های خاکی؛ جدا از بازی‌خوبشون و اون دریافت خیره‌کننده‌بازیکنه به‌وضعیت داورای بازی نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw7-C2LWmzb2GqLIB1cN6WbUiR0spK5mrQ9M3maR_EzoQmWayWA7YES0pM_HWcNu2cM5l-uRc0D3anVrjthhWYmZWGogpRk8ZHPzs4xD1RNrMu2oLXbB8ApiDPXsTEIF4QFZS3tFHhPaZkOK8uliKkPFOcd-2RzuwLrKnSQmEfPT_YTc27rYSxLISoFKlmmt0grYYpXZ4jfATq50ML9yEZShx06e2e6JFmq49PwIWQ4YnHXghzWunDWeL7DK-jCKJLq6GsvpntaQVjOxzkpf514KJLDjpDdmQovZuBE2SNfglMudLc-SeJHuWNuyhHDJUWIJfx_nSff7TtQ8roOCDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFWmg2djPR2ViC4IDwPPCgW02HStxiJORfry7chqhX0r7Bk7Dfxk2IQmQ6H972lypYp7e1Jnbj4_F7TYL4JNxrJ2nhrfqQaZpgAz31z7miFZ4FW4V8MfLzK6zFsKbNoMxUPaOankOnDiYYSmdSharfpQV22OjqLdKLN4v6UvWeCtYnQ_acRWIhZREtOiA--gVHnPlJ6Ula1k5m-uHSQi5jIhWoGaAhwUr2XW_sESwdzc4T5bq-5BvnsGFVVeAK3zxE_1K6ZwP0aQGhHnN2nuC_lBbKS23mreKL0HU168phd60U4hW9MbXUlfcalLX0NXRicNaHQENQD_IbTjT3sDMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=B0s6q-FP6GJ0Qv5X-Fm0IcofPpz6YVRRR8rZ14v39CPY3bZCK26RKh4B9H7u9YP7Na_PspJK4TbbwojHSi6chnXXmnj8k4VfeytUBotKDqdqsnAsTsO1cxydA1m7ACMQBdGRRXygCsmT_jzdqk94_6dBli7C14QVKteqm72PRYSiQLBiD_k4s1vWBpgq7TbyKuwk_dvmZ37oMviMqJdWd0hQolrzIFeKzidMDfzfsL4vBwuCx4I_ZRbaw3mkeqYfrPz1QiRzhNItWNxbrJOe2OdUAaYf0zKxXZT2lR0cNikWihi5SteM7ZPH3NmYcnUfeTpr0j26EMb3C7X57-VGxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=B0s6q-FP6GJ0Qv5X-Fm0IcofPpz6YVRRR8rZ14v39CPY3bZCK26RKh4B9H7u9YP7Na_PspJK4TbbwojHSi6chnXXmnj8k4VfeytUBotKDqdqsnAsTsO1cxydA1m7ACMQBdGRRXygCsmT_jzdqk94_6dBli7C14QVKteqm72PRYSiQLBiD_k4s1vWBpgq7TbyKuwk_dvmZ37oMviMqJdWd0hQolrzIFeKzidMDfzfsL4vBwuCx4I_ZRbaw3mkeqYfrPz1QiRzhNItWNxbrJOe2OdUAaYf0zKxXZT2lR0cNikWihi5SteM7ZPH3NmYcnUfeTpr0j26EMb3C7X57-VGxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇧🇷
پوستررونمایی‌رسمی‌باشگاه اینترمیامی برای کاسمیرو خرید جدید خود؛ قرارداد یک ساله همراه با تمدید خودکار به مدت دو فصل امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABPn78h-4HqIb-yAvu7at90dzuTCX5Ap_SfLuAbKXn19HYXmEp8xZGg1y0V1lv__ohJiFCoHvYbsRQr9Hv2Ju6Ym3Rd-R9j2rbAtijWAPZ8s6tRaYjcXpB-SeJ6QneRMo_I6-mRC5ZKPq6s-XWGwwP8j-EynrDSUcM3PdDr5H4ZlFJQlhlcOVnJYqZ0KVCskn9rjkT3vRHIEOQUnRm2Lha58BoiInR3OK_lewWz_3hwSe3e7cTySMJ42q_t6oNAWrWwmn02bs6rELXjLHqY8DFVxCVpeuYSrYazvtF2xYw4wVcKv95uiYt40hXlt8VdZtlAvSzyG7xX1wsmI8dqmjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkL6WP15tOFf_sbn6toZo2K8GrIMJD3UFqblyfkcY35WfFfwvcepq-gnoX8WS69y8QBMkS-Kux9oZ5ujkQ9Z-_XEP1tmh5woHDo0z-Ttw92Y7j1YHmI4j8r891MFBW4DSXImyJGxSz3iJBV7tvDsPn2J5LCRNWz-qaMF3Nd397SCXd-3cUn4movWCbSOcyzoTX6qtb_0K_rSCyAv5f35VdvHVpgqtyOV9UOd96cQOGw7fTAdBnD4pf_MVSgs1jvfqeo-6D8HrF0Xa70kbrFIR0UMt88jFtPIfcxXJZOxeWAFNY4cV8Dg6LZtmPFIXNKBtAPP56xXJZkmcxt65ZtVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=BXt_zSolzFVXllyPGpDToWv_NFvfAIyi5fzStiIn32gAjaK0aU-i5n1b0MmxuTViFpurjNHj468Vc4UqkCLv8kVT97CB8UEeTnW5wzI3HCEYSZR1hs2NUYOFf0ZUvhfTrnTmP4TLgSUIsgXK9Js_v3mNgwDV_kbMar6yaHbI5UlS8O65S36_fs-o87CBxBlRlofXMLnmNFvfMjU2_lQhDGHbfut7lVscblXHEGKsQZyumcoJAiP1QCwrDRDjD6iLWI3StFdK1shnywySHg-Og-2M7bYaOG9mwUuASlW2uJgEBM7XhkchXRytfTlybNXGtTUKYn0KTx0NMxwWMcJu5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=BXt_zSolzFVXllyPGpDToWv_NFvfAIyi5fzStiIn32gAjaK0aU-i5n1b0MmxuTViFpurjNHj468Vc4UqkCLv8kVT97CB8UEeTnW5wzI3HCEYSZR1hs2NUYOFf0ZUvhfTrnTmP4TLgSUIsgXK9Js_v3mNgwDV_kbMar6yaHbI5UlS8O65S36_fs-o87CBxBlRlofXMLnmNFvfMjU2_lQhDGHbfut7lVscblXHEGKsQZyumcoJAiP1QCwrDRDjD6iLWI3StFdK1shnywySHg-Og-2M7bYaOG9mwUuASlW2uJgEBM7XhkchXRytfTlybNXGtTUKYn0KTx0NMxwWMcJu5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJcHHEk1j9kEYJcpPyEnnlJuI0fjuRmgDM2JVyT2IeJMamm3yRIeK_GH91rAq2AxmWX5Id_UhP50bhdafuGGwfny8DuDiW5RmVXGlRPFO0GS1yUkfcl3zCE3fBrigDB3iybW4M2HKdjgnCpeSjPT52Cs7rwLjXvDLPTDO6lPpmutDbykGfD127DLZdXi5fsVpvlsJAXx2_jEnTqAyz4b2cJuP1N12oYjJk5zBTvrrQKigS2wl9a3mvI-TuQp36jxVEqriPMjY9fNZT1ZW0LJuotwdNaOM1L75IIQGCJZsn5DCtCWrL8LaNT8MZ4Io4OA55IhAqzT7r33pLSde-E0AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=SeYXDyXXqxQrKIymCYAurqF33rJAr_Kq0NWVYWzIEPVcXSR8nzNDz2Rbwow_VlgDl8cFNEQxjN1y1owBgR9EOF0myGo_EeYr4GCOWe3ZtGOpVZs6WH6R5BdZ1d4Emz3YV1GY9elEJ-e6ArbAY3Epnlo92MGHZcVWZ_vC-9H0PHcrqMQsJ7nL8lu8P0UWON56RjYrTnVqyp-wYrr4mjF0fhKiQb5z1Pq17rbGruAOothpNWLH8nmnSYlcKh0TwlpuRo30AZPC8mUOv2dak7chpU8l-Baj3jFDaR8upD30NBPmrpG9hFIAyUz6V_6zYS_mXkv2XypHOISUfAGLpYIE7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=SeYXDyXXqxQrKIymCYAurqF33rJAr_Kq0NWVYWzIEPVcXSR8nzNDz2Rbwow_VlgDl8cFNEQxjN1y1owBgR9EOF0myGo_EeYr4GCOWe3ZtGOpVZs6WH6R5BdZ1d4Emz3YV1GY9elEJ-e6ArbAY3Epnlo92MGHZcVWZ_vC-9H0PHcrqMQsJ7nL8lu8P0UWON56RjYrTnVqyp-wYrr4mjF0fhKiQb5z1Pq17rbGruAOothpNWLH8nmnSYlcKh0TwlpuRo30AZPC8mUOv2dak7chpU8l-Baj3jFDaR8upD30NBPmrpG9hFIAyUz6V_6zYS_mXkv2XypHOISUfAGLpYIE7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npPOpclj0UHvuhgR-0nl5tl9lxomNvxAG3K_0HswZvP7LN5iHRUXBE6x4QJpq7PhDvFbAsZv7rxjBYjoPgy-6wn7ameT7M3Ejh2k269ygzornu_lwefRW991fr_y6v4-TetJHE4ZIqIjhWppbRhfNWRae7Auy9RKa_-zxSrcZ6Q_O8IXye5mkRZNrx8FAmHMHd7oIgvyNBgZA9PNzDiNR-uohfTlsKp3vbO-FBCtJkZC7kBlIaeLPwC7Am54nw1k-FcmxuImnO5otdLmUItVNzt3GR_r7TecMpIQBfQ75WcYesGSIpLN-ds2m1Ce3lPOfVxtCuhiPWapHNKKonuZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnZpIavNMIxNJ7KsvqIdKXQ2tSRR9doF36XSZxQo0o-_l3CQvvd7xBpXadwTdRxXggh1LKMVHojvXLOD-poCThQ9wVNmGsfNWYAUjgvlNJdKoKTuuvoysXc7SdSLULB925e8SYdvUCmIXZyf7qQY6Oe8gNZ50h46035G2O0ejxwCkc6bTcdbq5TH7CQqWN94YpsXNhthzvOzL6VnANpCpz-QZWlg7nP9X7eEdHjvI92nDJFJklaa0H80US43qNB0s--YpXjz4Oiv4R3WQcmIHmMstjQhgpCLJZNNSOf9Ni-kyA6IxrrsTxEiVDehaYuNR6pHcxMb_zx1kw_k0-oSLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QipNHZ3RFcGwgJ-wl96E4ml-dPeiw07T2TmMVz1mcVMZ5qICa58SC1sNs96-oGULfe8J6bDnhc9fljT30sy3UtamhuGX5fc1MxDf0k0RrMCQrVE61vEBz0iktYrf8Ntew1vZK2X8aYm1HomQ68AHrS83D5Z4cHdF0R1k96qxaQZ_jFksZ5eYOtaEc5yxSHy3tu6S32Np_hQCylZi743jXOBky5lSxlNp6RYIuGdaZoLxo3GjGnz_iua3FyYM8-L4zqlyK0zqjkY0Cu1tXlFzRwLwJi8Lth56Nt_t5HvX_kjG-75clcoz0yOnkj7T2RJAC0AggKzmJusFo0ttpyJLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26866">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN40l_oHHz5XtzYNv14gwdF-IKBLUNkRF3NmUmpqH2MwkLjwDq7kVmHjIb9-MgxZV64eP4lPxKALxwp4Vq4jWSdmd3uEMG33rDLufXEMf_Oz3xCfQAjG73SHCeKGhslSn_ds_Q5wi_PMy_wkYy6bHfoUQm_17oTYdJgh5G3sNUbooZng_QEeTKiNes80HVek28WIshPT5WIEn5zb9styFixzAGYfp1Akdo5Gc5170njQYKLay9ORU6mOGwVsXRrxIRflIQSGYXc5czv7W-9FjTXTI_D7DfsDJMNVSBzf4peK0mOcT8BInYkUNHjlx_cd-IToWn0YVmwQG88p44NMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
💵
اینجامیتونی‌روزانه درامد داشته‌باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26866" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RsR6sNfM-CMXzyqjX-38JfupdH7-pTYtYeTt4oOiNsbrdjBbgnGKTRdOtN4VwPxJ2_WJ9B0uQM_Qf7xD-ZhtXuUBMQApSUTjCcFE-XmmqsP8koHkJpLjIuZjGsv4FuE_SmKOlppHeA6T-ivgIFGcWyVAtzRdauw1ucIiWYgjdN2Ip4jkcD2dDuGbW0i00fnMx-0xjXnFheVCHndaeyVdQZkfQdBupQ4M4i1O0pcKYykk-LhLGYlV8GU6iSinESgI3IPvy8rqibI8YPtiZSZKF4yeXSf1Wf0nz87nkfs6T7OxRhDxVW6rEFGNz8NHA5jK9r_4tIzJlh75kvuWd4LHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tz5KL2748dtHlTRoJFv_Ln3yFm8lPu_7DpXJ00JqK9yhbT8tnvjxQ1mxIJql_wz2FcjOklSy8P3QWmlF-VHqXb92L6w8q7m3l7h5YaOA6MgGru_uLN-r8B-fbuuXeAH3TkMFX252MplUVXVUEfTg6AVE65OjFbu_oTCNTZUR1gSGrRkLret32cKbNuHmtto5z4D4458P2pOqV-GEAKWXsbmyqM8aC1yyzDjTTrCQ7ONNcFIFM4VVHqzYheupmLUUhayQi_IDFtyqAoACYBlELP3LdqNtv81taNqngTBOQianKoGGGXLN-8Z_Ry41YhOD3KwbuqBf2EVoeQjIykeIog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxZP9wV0tMzXY5qfUVr5bcKDHTOPkIg6wSgNG-FHh_SnFjhFIXURi2_IHQRVeCKN1RJBejQBOslZwDvrmpu7dG4eOuB728uZCdkFjBAb9RAeE-KPENEXaQ93NWGyEZORXoc_YKxHvRw1t18kSwkqMvi4njfTD9jfC0f-4gY4lDoxrGCtvdUWhvO93NmZ6P6whiPL_S-0rjtUawW-kID0H2tyW7FDB98M2zOvmvn5N9coJuRaK6ngmLobIz7f5DzzOXvxsxrOqRMTFUM_0gkbxxsHycvvqRov8nlfrUECXpi7GlyWCbbBuDHT3hG96x8AW251ExWXXs8V2vesrAeU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmEGfPb2AK9KKOnqUXuU7wECrk3MK8IHFr8HRYCUs8qSpKyNqDmYLUwb9LzdKuxbkZGFcVMl5j6Q5CNTeHIu3rg07iupYHMeEsUgFUmO6WhFxPy_SBDeyC7SDOQ39oZ-AJCP2mLygsH88yNVc7cdE9wH1YSjySTIeGChCTH_kLvxfMopWjAv0l97701PDEV2dcOwK0kFH4jcfNLOkcDa2Uufm4OjO02NE3YhRxY3OMAMTE877mqf2NVbcUorNCkLpEIptLsS_I0w01Sa8s3j7WAa69um_K5ZuqRaA7zIpd_Wk8qpjppesdnB0GBon2po6pCjR07qtQCkHlIL8HohWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=jbj0ikAyGuZen75EXX8gWF4MHp9mMhVLcTlLWSmz3iG_T2yfHMKCsIhavfVDstxKcx8-VgOC6TztOn9pSIKoEbUH9Lk_0mpqSsgcsQaq3DgS2z1CVSZPBGD06UcH4siXwt0Z-IGjlVCS5253xJxTenBJwpVON0lhAp0PeaocBd89wH3tvdrd8uMmktzQzLHDsHNlYMlDYmvXoXgyWmlCUcmq16l0gTuLKv6JJn1OLw4d9HmH5jJpH-OnEeod7E2DpDgA0AKcYdtroVhs4eAxxx4G8G_CWg-ZnWLCNki2tyLKs9bGDULCoovzDxdhNK1DKOE3pfdc-ZwPncFniXA9hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=jbj0ikAyGuZen75EXX8gWF4MHp9mMhVLcTlLWSmz3iG_T2yfHMKCsIhavfVDstxKcx8-VgOC6TztOn9pSIKoEbUH9Lk_0mpqSsgcsQaq3DgS2z1CVSZPBGD06UcH4siXwt0Z-IGjlVCS5253xJxTenBJwpVON0lhAp0PeaocBd89wH3tvdrd8uMmktzQzLHDsHNlYMlDYmvXoXgyWmlCUcmq16l0gTuLKv6JJn1OLw4d9HmH5jJpH-OnEeod7E2DpDgA0AKcYdtroVhs4eAxxx4G8G_CWg-ZnWLCNki2tyLKs9bGDULCoovzDxdhNK1DKOE3pfdc-ZwPncFniXA9hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohvSrrKoFxCQHgJzA6xJlTjEyXwz8Dwqv1We53e8rFTIeaU3tauQKJTWUKARxT1GEEFjzI0OSzecXN6eSWChljyVPdfwPKOk8TKWqo2ODry1spS0RpeDF2EyWrapmBimRPnPf7SFL_1IW9vpKBwUxA5U2s_WnU5AsJHOEo6q3EPxQ0Tr7pPoSbjvyUA8pVxuy26F8dMqDKRXenHjH6HR0AMJFvlHadM5DDuvH8TTFxRL1IqcGeZhzRnXGoZID8NwRgiypc-5L3xlYAfpnda-gA5b2h50EdLvIgDq6nWKR7Jrjfm7nDd0nDz-5We8JnK0GUf-LQxAWCNMmC3_7ecFfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEypNiirkPyN-VWaWpY35mkIDvkZU7NzMe87mjvO7w1Tr65XgbXGW40A1qW8uvJ0zUBJkinhrn831yM8DKuCd5DnjRY7MSJvz-x5GFwbcwA7PJMJ7aJN2wDdcTPkjw-BZhwEImUPahdCXQlE585ScRmpiO322kiPQRRvJlIh_wJscUcM2IVUWp1nwVN1I8sgPwI5c64cWdSo6gIYbsr5Dq-FtJTic7JcW1v6t0-MUSFnaHl-_cG43LyVihokZj38nURHvO_qV94dwLPXNrbCCpNa8AIY2B9vckj7ar6Nhww77mL9gIf1a02-0YACG1h0DKfLW1RhfnmklKV1ME4sKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPIYjHtJVZo19XN6utyw2Yl-U-Jkt87d_5ntgtGzeENLjtajKODNnWP4uRn1R8eL4JsEL-hAq0VJi1vA8y1epELWJyP-Mg9gwJyHtEOXqE1V29LwuZRcHlIgDZcPjo5qEqlkGFI0ECY-vYtxqOb5aq3EU6XXi91cQdlZu5r8e6fwoMDvg1hL53MB3ETp7uK4gCAwGdPfwMvO_S01h7d23RnZL87-su9QtdKw78HhbOYIL88z2oCWJPnt7zIWiD-0kRV0F9rIaz6YZZVioXpBxBpWnG_hRa8pIdB5ZwY8lodmAZvS8Dibjh-J4heLLUTDEWgJ6vzfbuso8aB-jEJt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7Z_4EoomM5a-z7lsfoX1fGNqhj_fHAbFmr2igEOIdXl0Rz0OaOid89bCTNPrcUL2xp56nHNaPejeADWviQvRYgf6h8DaA_h8HtnavHIcblpYjkgfSOX-UtdSu_WWaTe7oeHfAWcYTYsifwSRyVdksrnD_dwcnaol_2J8fuIXOTT0K4CT8cJrxHSsf_AKAguEaatfxPjnGtHoDQM7foq5ftKr_J3P0rkiJK-9F56b1Gf0JPqvUksKBnuGRIAtFVoQ-hz3c8h_zZoBfr6n_-CEHZrUXRTNWdwFc5C7YemHrIESUsPpJMT0bXlBlsPIr2H95Qa0YDDtbHR9zUH3KX6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzDOfMbrcQ3ZWwbA-wu33HVipKlmOTvDNRzZ-oyDQt41lWNq327xfaqFGfl4jmApXOR1Hfx1hy7A3-pqimKlp0vk5eghgYfzTIlbPI-0z4RpN9gEJnsZpUE-dDSi0NTJI9tFAgqo0sMj0eOKETYG1OdjzD40E3Z35WX1F8GizfernUriB66S4w08pY4-nFCESn9juBF7I-WcYdYTjZ0XHCDgiwGU4SAMu0-6wGxM4vcQNlbNW9rFzGwOSqnXQXBq2NSyBG1F5ahUijuZiwB5bhyImBskg1c5SXtsDk0GK0L-lCySc0R6Azj0FYJYny9cCL4T6AzoXPO1w97URQcMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqeLldmgAztTa4oFcf4WStJJ2amn4hX7RfQbDOas3D-EW6tXOdkF3Ww5-vk4n6YMEIlZDnk7bBb-tU7_FthAMutcmUXU0gM_wkUSl1K7eGPq5d5GI7q4rCUXfd30-tLI6KzV9eF8uiX2p9ySnZk3aeEKUEB1_Qn1a6S5BU3Z1Z0wnvbFlg6-TNIy6GMC-PrhyjAmBIfws3YsKnSRTGJ4C5FZ7syXh9-IBmn_QRoDpbGtCgXHtQgBJWTM6eMbsgRvR0dmmeQiFi46UM68Z8Z9_MPOXU19PswHfvTTMCWuPQLy4haiu3ZErsyOd8LwoAExFWg2cVjjlNTOZnY7pwFHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAJQzuIfEKAn_AivhjkbwEnlNzAhQt13fbr7gu7i4pTqIPE3sFQ2I19Z1FpN5trgJ4I8wVDgg3FHnCNIwlkcIQMffxZ-kogqixOaTqGKwhzqlHOrwZKUnRzPQ518YdlasRVl9vmyIZvl6uFCB0sVquf-eSkkp3Tvkai8r-S6M9FkMDF0H-9S2KvuGI6ceHhSsbtb1D-Yi0FuJmB2_uhCungzbbCsZTw2Mfzj-tnHpC18uGqZXngVtwNU7qet0mJ6qFJb6ryKta4EeLruEfZzzxBCdLTfTbPxhf7BQPDURUxL14bp2kuNo51GXtKr3nsdma-KEdSwm836XNlC0cSIhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVHuHX5nXyaCXvIH3LLNeW1ZUbnVMx2Kr71oETKDb2lxhplFKw32lMiHldZknbHAZYejIEHOUwzGKU99nicsevqS2vHguA_EopT268oHw9t0q1b3zPlyUylBglcS7I3kAMW03BS5NsYDhxpmoqUX-OuwdB3iSIOHw4fhZAU0j6Y4-yc0Nwc6mCoBoO0-oSVu3cRob96hTfJf-bnFjdGA7Fedbu5e2vfQkpITHa_AkYZZdwYPI_Blat0boUj6bqCA4WQUaGNckv3BEsWggNg3_uR1-bAfwNv0BouYBvrxAMdg6Z99WGU9NU5qhjmw1LORsZosaICmGhSlxuIrk6b2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTyEJwSyFKLkqG6Gc_AQER4X2ZTPQD3TwsJUpfvofVlBH9jCbf-g36eRskKvzzhR3HYCUL3uRiC5lptlI3b_Uxj7b4j3_hiVpK_4yEudSmpTfSgH3wL7C5ph6YzBHW7HGWmly1rOMU69So2lNok3guhNZFmCN8Xlj3DPkPh_sRcNeKHh-OoTKGjjDdc1VScSdDoYYa0Xcb4YAuGbTAI86uhFTSSX1NRG7T6jKkDr27UDEPKEJZqDTxG1xl9DMyAp7TofUhO57LQsnJSLN3x9LXDEyyVo9tbrh9cJ7rJCpmEwnxn_JCCMlAoPI8dzFomCbFy5hNCXHux79noYtYQz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ij29Uky3FUYLjRq7kN3cFjAUUI_uTMwSvb8VekDHoxbGDJw_Yu_PkeLk5jtDnj_Uy2-oxbB7m_q8_qWt7DPnOKCiLmZJ8IuLVzQsAYnlZPigfCmIGDMaVQFusDJwsAGtJtSzrC1ccDcervy96iN-lNgkbPDHY528ips3QLDHcPYNl4yoWDXDqwRt7ebOgAYYQg_JxgJc6L2HxSzI1LVjPL0potHiK6y8nONPfxZeyCJRj355hV6y03Z0qWYWvnj8XnDKW3NBDfqWBmYQyu9vTrCRUb2KGBkFTLcYZAr8mZ7ub30jvvUAYwv6ajg6SCrE_jr7CBM3LIWIcJTsMSi6Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t8z-oypc2RfKlr3Njex-f2CAkHliU538F8OvkoDKihkF1cGyiZ8r7OFtq-GgFJcc-HPteol8EqNEe3gcM6C0Zkpz_p8y3cqd2A9h2-x-2PJsGF8yePZMVt8FLYkGb_BanPRfOr8yaKY7PVCtlZxNzy3BwW3XkcOGPimvgWjnfsDcvhB18NYqJ-7UyGtJ0pZSRTllpRfk6Oqaw4jQJ2__vfRaTO5upqb9JDpoeKvkdOkZtWmT3XXh1nj7tLSCQ3TMOykVWJuqNA2M_B1CoFGuy6oVbu891qnOVyQ8ArNR-qju6Pr02BuH-PTtrgDoHo1k2Td4X9vHIotoR4Vs-tK-t7o4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t8z-oypc2RfKlr3Njex-f2CAkHliU538F8OvkoDKihkF1cGyiZ8r7OFtq-GgFJcc-HPteol8EqNEe3gcM6C0Zkpz_p8y3cqd2A9h2-x-2PJsGF8yePZMVt8FLYkGb_BanPRfOr8yaKY7PVCtlZxNzy3BwW3XkcOGPimvgWjnfsDcvhB18NYqJ-7UyGtJ0pZSRTllpRfk6Oqaw4jQJ2__vfRaTO5upqb9JDpoeKvkdOkZtWmT3XXh1nj7tLSCQ3TMOykVWJuqNA2M_B1CoFGuy6oVbu891qnOVyQ8ArNR-qju6Pr02BuH-PTtrgDoHo1k2Td4X9vHIotoR4Vs-tK-t7o4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBbk5PHY_g77zs-L9G_GEb5oJmLvY_0WKoqjRHo7lrvV4rG4iygWpodkq_aXfQegIAls_ROR48hTRPXQZQx-tfPyGW18cBZcSesZ_tAzQP4dFstX-_ty1uPGYEI7NC2fdlbJ_IET-S7T6MsldEkbjmJd24x2glZoJrKurYR0o6q_cEBI52aezL-gm8lnE9BuYsSJU6PPyVvMOmi4MoYR5lvyt8GBfHqMsiw2R24wu8i7yq581jhyquOm9i5XV8Z7rbcTlE0paGlNzGUOEzqKKvdSsXgMMXAZxSxmX8CLJmL_m7U_s7QZ9M_z7tPhPD00A9oIeUxnRDqV644OY7rbOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh3RIm2PIowOr4lVzl7ShDB-6m3KUu09mUy8nhEQdxztY5W_VXRKGxg-KvM-hokRv-Lykt25iMGiwxOYCpFRtdIsmt7Yz-98En1w59ANT5u1MwBxg0tihayi-rs4IobHu1SAOc9ems7N7-pY-M6NLH_f6gK3mqbeD0fU4F-oARRDqYxUpkg4yOvKPNOgW8igcoJMmSXdevrPursyHKQNzRTjS1uKVpflcOEs8U76YtDwMbbAQEtYlkLN_J6W-qZaEw73Oz44vhf1UKTCScGcuGdjPWiQBkWCc8jOUASFzUEkcdoopFd-sYmK_TUrE1DDR3_a7P00daoVToCTlB_fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9kBXGw9w13MQVnB6FtgK9A0JHG2tnoY0_sPtieLgKueRK3tKEKtjkZpq3_PUILR02CZQi4_ydE0FGEIaZDtat6kl1UjI9dhlBoWPqe0fBtL29GuUPP36_d1vh5aqU9i_Wz_EF8SeDa0VbEKbt3cYikvadAxnzcXLaFcwMSMhMKCaUH3NxLKvGd89j5FXQ6dnxVP2h6WNi5aW5gMK0JhFeDwGvQ4T-_0VMwRFG9L63bxAUBs5134_JE80Xi8MLSV_yukxop-DWS2CYyH9QK7uwbn3QaP1oZnX_sjllal7FGcBBG5qisDwVmP6doSrCYdG7UsCgnnBYG1tVXXMcTHRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANaytWPrwGXylvuej5kNwXKY_X4n7QqRoaWp-sc8bp_-Flhy-_S-sx3uJfE5twg8Yv3xh6KHPqhpYQYUqNcaZfnqoPGf2N4BwZ1Ajzv_39Qwy0TgHyluPKoL01aIxpb7nvuLwZ_6bhfD-T1ztxx5VVj_w6FJMTE1omw-M5X3KkKUM2HM1f3lakfQuFL6O025OrIBk3Rv-7ZmDVVxGMiIYHuVUYNxFpj6MTgz9ZwDbTx1Ul9_6kAQ9hmjnspoZV8qLc_tj7qTc0w7lTICb3R6GjGiEGTlId_ToAzjCDL-z0zvBiOZ4jgesU7y8uP1HZkHdjko3TJbR8MBp_nZl8fL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vh3-y6W9h189I5z7Cq5lUmudhxskU6GyF2alCF_fPztF9fmHkn-2QPNOhxGait_SEqMSHuruBKueApIPhGO71b-UrrSKdHn2OEff_xPq5lsnfKOimxeMTbClvQMDTrThh_k2UcKFkGViKaV_MrmJC4D_hpMjcA4DUzL8PoY1rldei4L6N8K0aVcgAZ8XQd1g_QsaEe1ZiSLqmNtZQkgwCdSNFjcOV80eTar2pA7Mup8gtaPakL9e62AWf7bAd4-ps0YoXwqWDORCW-MZut-RRRDBgtRlIIBRdUZTVruLiTET_VkRWV-zdKUTbLrLExrxkmMNGcrSR4YZnQ6-wt7gFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2THUKKl4G06PNroS4WEi9wnHXIjFZW_3Hlj28Obj-Z_37OU4hoziZUzXJ2azePib_jXQfQaaJS90ZrCoTypTeVNrv5Yf7ykhzEFQPRpBnK97qhQ2mDFR3zS97umEbFV_Alepi8dVwUzaIp6A0ql4gceMFkJskV3BEwrSYAmLq1vlJ2MVKJmzu48s4agQcO_yJ-k5cvX0ljM5ZpvmvNdJIp1i6t1kitxGXHUBzq71z1azVaPg9qKHOb-SxcnXU9k-V2C3d-AXDVxyNmp6fMAa5Q5affuuQP2sBzJEA1SH88D4zrVMjPtBmHZLWevxPPOCqpoXNWowT32iEOp15omTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqB5-_vpYjk9uNXAoa4FdlnQbWZNTqt3nLsj43-e0FqNS5OGuchhCWnkY02kwP2xnp8MOQzz1nTB3zQR5M-K5xyvUjEtNhYv33XhofyOZNLm_hGaUaJdGEQf9GBcBi2U4SPxQln5QaG2P4lAZq6rnMv32kY6V_Q4H-1lxUXdr12DQFpWTP84aZZnNw7cuWJhTQDtCAy_CgT3UbT-WGLkN-ff2DHTd6zyvfad6Hh97XYT-CAvcvphIWCCY2NQVN7IT0aF6bBKZhIE1d7QsaS7E9HsdRbTgtUPVyEj4G_t9EMIe9_z15tr533puHz1Z7vKNAQ0xQlaKM7UXTvgpX2maQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2mjbVL2SwKJiErHboEPtr8jwQatPBaH51GOS30qaae9Ru4EzmV_72YMGmowLF3F18oGzdAGJp26nYxlsH5Y2sGyaJlbaum99RALaJUvYglXahgCtK8Gej0cVJQYRBt_q74D-37I3ocyTtX6Tu29wP5zroTCVrMD8n2IpbrlN-0Q92cGLf4GOlnncpsub89JQQZyQWBvuMViv4zwpqI6exn8L3X5WpYEYzGsGhBuOOA-SZ6wZlwiB2Og6WgTKLjygCq0If9Tf79gWmzXJS8myuqOLDh2uS5eXD8DEZKKBAKtQ4BCJNMwyJtkTnpByZ9z_96En7_6OEp5gH0W6RNnKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap1JqT2eYa6J7zhWR4U7EW4bnLu6wfse0oagGkW7zj6kHAw0WA1XFEjxb5daEuchWF8G9WeMI2K6oYs7Oa4tr9HcJX4kZWi1G8wsGxolaDZdo4_g0YbXBhGeO8XXkFlfFDUz0FSFsJU4dpW3y7zxRw6jOI6b9SdqYPg2D1xdDycbvOd5ZS3vYl3yva09x9lJCxIy8jDIlQovh4PWVd_CM23WQGVpmVnlBU1oEays3PKsAu518UDeTUqJiWfweBDC11GnK045r_0qadOYA9Spz8bc9QRkl0XBRv8ecfeFQhW2FBYHVDVGJGROT0jad-ljA7PdfOT3p8bqfWL5daw0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY0t6qqAQB3yGKeUGvbhsrXWdIjG0P9I95VOdOibkCc8lnLhTQ3AmmqZqgzfJ9UL9VICAttxl8F55egtwYx1yhUgQVBs-kFBmQoaBQAhd4UJRRmGRg8H6UXq3M2L6FfEvZTspUqzGjc-V2zm8sF81yueJHCs11bRNcFvSBBsYPbRYE8uPo4MAnVkZmPoY73EfIf46uSqybun2hVyV8HYdr-mwvrPO99HOKUIC7a-UYmgE1ntSrus-EZ4qY5DquMJcmHkVcgiEEC6eQC3AJh1GSWbUOJdyMyrPUdxR3EQU6-Vby9r5E7So6SFnyQusAHh4-Oal-GRqmHMrUdFx28_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEs1dYwsiokfq_SRUFWQq14UKiLVz_xw-FOUEu7Tw8Nt0TfHWkD5hE2BduFRcexhrsiAEJcO-toK5mrGChWEMAsiTcrjY-ta0iSF1qd67BnGkdVhmS4vBVZQ8Q_j2TqqbzeJ7UlOVpjIheNAua5F1m30flYLvATEUlJnpVhziTgbLeu2PX-xg3AfolDBxCarxnIFthSdJHfJonieEIy7IhEgC3vD-SOJQwC6RRmKQ4Utaqx5tLRuTioFGxrwDqHDxenNrMud9RCBr_k0KdCGmQAbthaDYobv1VZUDuwEEmIwerEbEv7FaToXGRGk4S8ugjSa1ivVSeY-NFkBcyE2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=b-eF1C9vTEiVy_LZ5kRicYbGZpm7zWqe7NCRJ2wsGRl0Tk9kFutLeUpgzEB0sNhwUH-8KoEkltU67yl1Ak38uwVPCvM-z47ZcJl74ze3Iy5-4LXvBzVRJhD0HRznTg27_7NaxusXE_rb_zqKOuTB2SQYxTMQsck_TCd2gmEjWO5Sh5nXh0Pe5KTKPFQT9q8Rn-dmh4GLIckaSWH2gl-qivQe5ysf0KWQ8EIDzMaF7Ob31K79OwneQXv8rjfs5ud4ZANvHQK3_WZJkMSnZccWQ5T5KYuNN9MOepnkVXnujBbGFhsNlaCN68kdbt_erbO4p3nJ8BpcHVbCnA4TLT0mqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=b-eF1C9vTEiVy_LZ5kRicYbGZpm7zWqe7NCRJ2wsGRl0Tk9kFutLeUpgzEB0sNhwUH-8KoEkltU67yl1Ak38uwVPCvM-z47ZcJl74ze3Iy5-4LXvBzVRJhD0HRznTg27_7NaxusXE_rb_zqKOuTB2SQYxTMQsck_TCd2gmEjWO5Sh5nXh0Pe5KTKPFQT9q8Rn-dmh4GLIckaSWH2gl-qivQe5ysf0KWQ8EIDzMaF7Ob31K79OwneQXv8rjfs5ud4ZANvHQK3_WZJkMSnZccWQ5T5KYuNN9MOepnkVXnujBbGFhsNlaCN68kdbt_erbO4p3nJ8BpcHVbCnA4TLT0mqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuwBWLgLE3YTIdAs0HEvjQAREj4xp9kiGIIw89KluOpqSRBdzvuZLoi_AQHxC008EmvwAweFRzMLYoFzZOuwTy-1oQ9wCAsLLbmIbyaimVCwwsZ-EL1fbToi6l_QXHyyQMvf2yQJar4iU_KQA3Abrh37a4qFWVuYzyl1PaZzhZogIwEmrrwqxox02K3CCc6phAD5AwFRRZxx8huXoWaWX5vcc8w1sq8MzZ5WUNesTwsczcOfi_DsDyWaz5zgDs6GHvyOj_tMjkfNJZtXjlrnuDy8LTslKzRTNWfcNCCjp-H33ijB4i4K-5D1EsR5dPQGXxszUzu2W9rgwjDPgdKBXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnJkfv7w8wyqNEC0H66sx5Q8FLUvK0mgm4T88ZRm6EWFwj07wEZ76Mbtnsyv4XBnj7tXvVWpsjaG_qFf_OlANPRRdUr0i6waA3oPWVSBtCHvGggYMUMgCb3jXKXK5OjL56pFRarscU-4UuJtR5ouUXn3Jd_E7133N9jABDkfh_f0QqrlM7HVOOZW06Dxw2YtRCBsE5IaJg-gphEpW_KYsMMx-ElRaYs_A0-bamMfb25azC8-dNWu6z-kZKKQXPHxDDoa7uha9fJo3gmZuKHF6Y2TiM_LFmlgIjtzPgFMSAjBnpVsHZx8HTC4dKPZPI2Ky9pX08KeExpVPDWExogUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSG_afZ_Ibi0Ec-QYicYefq4CU40iXIp0nYnXwcpzEyfSyK7KPB8acFKnEF-runY2vyuzUfG08Sda19LFL0EqjyFsTH0Grp7OAr4kL1WTQYRI_6Dfbj10QlQXZrL9QmfsOuFB7FLLffhGbQlWhPvUeOWVekb34p05Z7w2zEdilG5G9HCOHl8_lL5LmcbUb1XEeHK_TqqxFIhnPIhxsQWYgfRO7EcDGqb_LbCUzoPd70LhmI6gt7RAlvwFgB61bgvne5fs5h0_YYhELdplE5tJbY6aQKmY0L2WemgTfcBBfFQipGu-RmNjWS7MOee4dPBA0o_Urg9TBc13Jv2azy_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=KevAbAZ5GMEJTt-66N2zYpi39p4txQggV9oghwdrhhddYShoehEE69SifG85Nw46Nn9NiLgArCB7r03PhVZ5PDyHKvS6dmSA9P2HW0zpr0yKjsXzLOlxSPb6i2zhw2-cyZwVhUgafRosfspL3UzSouNf9RQWpzestmI8Ye3zx48VIDZ6fmI7CJVtmvoxxyP-Do899UUdQ9CtjimuX4xgha51N9uJsxJaZo5S9uLen0n_qwnGsg8-YLvGfQ47F1QW5Am1xsbj8zgi5QsIZ7Mr_7xFXFflkJ4OT3P6UkD61Zpih-zi26RQ3JTYlajwFtmGPUIT6DRSJga2bY791qzhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=KevAbAZ5GMEJTt-66N2zYpi39p4txQggV9oghwdrhhddYShoehEE69SifG85Nw46Nn9NiLgArCB7r03PhVZ5PDyHKvS6dmSA9P2HW0zpr0yKjsXzLOlxSPb6i2zhw2-cyZwVhUgafRosfspL3UzSouNf9RQWpzestmI8Ye3zx48VIDZ6fmI7CJVtmvoxxyP-Do899UUdQ9CtjimuX4xgha51N9uJsxJaZo5S9uLen0n_qwnGsg8-YLvGfQ47F1QW5Am1xsbj8zgi5QsIZ7Mr_7xFXFflkJ4OT3P6UkD61Zpih-zi26RQ3JTYlajwFtmGPUIT6DRSJga2bY791qzhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQFi0tbLndcW4xK4gxksjHFm5vkwNw6Oaf_fnLPCjrVq0xKQ3OInjyxq8zkVvWH2PytpV5ZRz-a9UX71uYbuaACN6Yyc9aynja5VZWV_JvF2LfqsaRjqQfg6sr6FmU3aXuzDBmc1ebIr-FqPOAgjT5uGRn3N0A6HKWqrTEsYn4Xw7ZmG_wdc8MMBQitGEnDFO88dsYnhZz3FZkH_0D72Zcj5KXVXiCSuBhFi_3sWcp83hAM8t5frvF_WiG2xeepHz6vOMaJ4jA67pL4DhEsVMIkhwO04HA88DLmH2lU_urkuU3CvawE_rP3FkYZlB--PEz2TTYnVKo2HRH1RAqYVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdzBwwqW9jmE_F-0oBSPHM44crhPa5P9kCtsMxUaiXyK_Xi3KG8XV26vVYPGZ0F2V13toNdOGTgUK7dEm9QXi4VcB5_aPgSFhZqbzW7Dcul9Iupm2ewxbQ-Pz41KFeVS39zBtpFXtg0IdLYBQQfaKZdc_w6-qd7JNd58S6leK9eFe2Uu5lbTNFcns2557K3IjAFIovYBncb9Jo41nWNMFv2g64lBKRBw6iocS25XPytgMqREOi3Ju0CR12F1I4ZApehOyRyumJIotJpi0mPZg675BT3XeaESavIAI8Kxi6-iGChhVSK4V9COOUn3Bkri9069-ilOdwdjKUFOBxU9UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxesNUepQ8-q4kYqevpb-D035uNL_xDomPBQokzH4rADdcTbohNO3WTDufF13A4Ce1_x53-n0TRnHgURqvk8hSdckgCbZJ3X6tZfciJIQmLuXL3PWTPGJSjXDhcSrFuPeN8FnSAS8MjHUy6EDkBDffC62VaDm0MeYdZ7izwMM1nRpFJHsg-_SYVqvmJ5ZW-VdIW3yyn2UUykvv7cnehvwXE3Iv0UJ0OvTI2YubQydd5jj0XJ4Ot78nufa1Pp52zJVadRt7rcmgqsmGsgR-1GFGBF9Z1iAig8Py-ObVc1xU8I6uhQSVJB1Sp0UU4daKv0KkrQLInrHnoKY158St6w9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=qsR1M87DOT1_1o0gbl5WSI_h51pUHkmTgYAIOo-sn_MDHAJYYuk866_gEf9EHXO4NQ4hyo5dCUsKWlEpCzqOBkSCwr6WjUv_N5V7ulpBH1-hnt3elSkX9h5S_4P25iOgzrxJjkFMZW5a-tSEZyjEEMxzjmZHXK8_-8FZVyyxfGjf8a2MsNTcHQsw16VJQtnOeaVyN12PEzBtPw9sWXSG0r9CXgwc3hSpkwzCKzQ528VMKczgtNYFHZPlPpP8NYsC-veTbDzPdmgq4xyXEUTLTAIr1IbJBg64WH-uGXAIZjI65gDRr8bOVuN12J1i8ycYlAMTN6mTe_spBgQ6ZlVTmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=qsR1M87DOT1_1o0gbl5WSI_h51pUHkmTgYAIOo-sn_MDHAJYYuk866_gEf9EHXO4NQ4hyo5dCUsKWlEpCzqOBkSCwr6WjUv_N5V7ulpBH1-hnt3elSkX9h5S_4P25iOgzrxJjkFMZW5a-tSEZyjEEMxzjmZHXK8_-8FZVyyxfGjf8a2MsNTcHQsw16VJQtnOeaVyN12PEzBtPw9sWXSG0r9CXgwc3hSpkwzCKzQ528VMKczgtNYFHZPlPpP8NYsC-veTbDzPdmgq4xyXEUTLTAIr1IbJBg64WH-uGXAIZjI65gDRr8bOVuN12J1i8ycYlAMTN6mTe_spBgQ6ZlVTmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhl2WkIafjPvcKSlxZr_xE9PAx0zpmN2aE_6AIzoUmmAdInKeVzHL7Mbw4kRiM969z3qjsRCzqeuanVoeS--5x-rXAM0yt4_eercVz1UqqlwIWOn7SuHcN7a0itgJaHYNkmeIBN-zcDM3RIujaGYKgbLGdms4Hv-7691w7Y69DOU3LPCKcoHH8wsdv0R55VRX5YC87-HhWl6aoeb7w21ad4ZNoX9c8oxgAEkdOPK_u01mSDO1eLH4nNQMHaanfk5tL3MfWnFaGwTOk6lhU1EP7zs1H-9rIMYqdlwJ03303rQhtpSu4zcOwjPpJ7DnNl0hw0rJ-886xCd2srpXvEhuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=Njty3bT8wl8-mNzqLwp403djPt83EioOGAcofpwu5CUskFTWFZcbOY-iMEumi_mtfanX_2qWTQG0Z7vy_LWQDsTuytUV3f3sTuavs5pjb7bQhDew8z82Xjr5xUL_ELZhlNm6Iso3z8W3XPDZzEdKLeZVdX_7ALF5ThWE6FNWJuud9J6STq7nheMho9tcRfdBgUDzZVFMNgFQP8mPwRsAAEoXx1Cc9vGkQL3mX3h0KUieWSUDCyrHxqKBxrBI5kj-8v6X_ybxCqfNThmdJTfAzFMS9xnuxXDUoLVIMlK_aXu8CsC3qHng_d6g0jW0ck1z87yiCUR5eo30h9Tt_WGp_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=Njty3bT8wl8-mNzqLwp403djPt83EioOGAcofpwu5CUskFTWFZcbOY-iMEumi_mtfanX_2qWTQG0Z7vy_LWQDsTuytUV3f3sTuavs5pjb7bQhDew8z82Xjr5xUL_ELZhlNm6Iso3z8W3XPDZzEdKLeZVdX_7ALF5ThWE6FNWJuud9J6STq7nheMho9tcRfdBgUDzZVFMNgFQP8mPwRsAAEoXx1Cc9vGkQL3mX3h0KUieWSUDCyrHxqKBxrBI5kj-8v6X_ybxCqfNThmdJTfAzFMS9xnuxXDUoLVIMlK_aXu8CsC3qHng_d6g0jW0ck1z87yiCUR5eo30h9Tt_WGp_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bo65DV48Qv42xYxU-S3P3FP3n8weAP4pQbHS0FXX90LGusOFFIEjxyKN4CUtcHW9nnPQffOAXndmG37I4GkrbDcANqDApjDz1ausB9enlQ_itNsSRwXEFcT8BhM2xHn1qrsR6pJeEp6c5Izi4yCdMC48qx_ldlD0dGbRhO8PifhEhZik8Yo2WEG83ALqIcibxRzukf3LEtkBSN61oaT4Uq--_3AejcbI48qVNiPhcy1aLsRNBb5E3Egia1PKpIPWQG6nIH457oYTqsh2F-k8R9BWM5FYguc7NNcYxBfHfHvOoX0QsbZswCJn4NYGjTdrAj-Bc1X7kXmWXrNuqMIRUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-LqqJiwtMajX1uxnegF1O9BQ0V9kt0EaA98xYKz7fLd8aZq67RosYQakjOJPDY262cmt0WNcfuE2_f8V_uY6loF8jIwOTgmx2FJkFHfXFkfueRIGu9OWmwhczqi3C7Pzi4uzk0JS6HP38WMUpjI3HIanM35cpHrLYyYDQQ6iNGwEtXBDQqTpyaSB-LUN1dbVaJx3-eZlb7aB3ErYl9Sj3ZhC2LGtjGZc2mfdDAJdJqKK2PKBONoyrFEhu4M8_yXUsMbhir6EOaxZDvemUa0wNWyXbS4aesM6xpShsvxSU-vzzkUpayXOwZ_JAFaDMZvB6TjsfbPpsoG2w8A_Csnyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=oatGd9oreeai1lvVu8iX1NSZI7gcX_5BpZq7xu7osA2tVFOq5hIDQUJO5xPYm4xU1dZxFORs2yW7CBTH5jZTYq8SaCM2SRYCqd2928xbjsFEfIJudUUw-ari-QYXLGdar_A-Z8RxY0WT7zdcb4RJ3ZDxcEuhJqLaIkolpUjniDsDsHxto1gDi8F40WI6AcegoA2GyLr11I3ZmMi3K8riMpMocaZo8_vs6-UpbXSicj4WLsuzP4p6r_U8TSPQwA9cEasg8HRrL40WsG8pfc_bULcDNyDZXy-MrdYIfqGB2eDLNywuv9m7Bi7sjiFtMmcGcoVCYzP5nsNfT2RWAEEuKxjSspC7W2I3-29JJ9ucMoq65gDA9qTLJetYCgPNEkkdc3f72JUOXr4fbZ0x3sfZb5jEeo0mTAe2ac830Ceq4YUkw41KED5TQU_IykTknojQCXUA2uh_aq-YHR-yQegvrK08VTwFvt7BgxRYB_GnErOBzmjj7aNkHxn6apprQ1_Q-Ui63If2IH0gWcOIM5_Oi5UB9dLsy6e3-51Rv6elJj_47lqYZIAvjyVhBUDVzNZBHHB2Td7H3F_FnI4cvgrUCPiRioCo9a__-t2FoLlO3gXDAMaPmweqc0gPQHVyrw6xrTO7ifbemAJKkbO1O5GiXnbjG08OQXGNB89fOwQLS5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=oatGd9oreeai1lvVu8iX1NSZI7gcX_5BpZq7xu7osA2tVFOq5hIDQUJO5xPYm4xU1dZxFORs2yW7CBTH5jZTYq8SaCM2SRYCqd2928xbjsFEfIJudUUw-ari-QYXLGdar_A-Z8RxY0WT7zdcb4RJ3ZDxcEuhJqLaIkolpUjniDsDsHxto1gDi8F40WI6AcegoA2GyLr11I3ZmMi3K8riMpMocaZo8_vs6-UpbXSicj4WLsuzP4p6r_U8TSPQwA9cEasg8HRrL40WsG8pfc_bULcDNyDZXy-MrdYIfqGB2eDLNywuv9m7Bi7sjiFtMmcGcoVCYzP5nsNfT2RWAEEuKxjSspC7W2I3-29JJ9ucMoq65gDA9qTLJetYCgPNEkkdc3f72JUOXr4fbZ0x3sfZb5jEeo0mTAe2ac830Ceq4YUkw41KED5TQU_IykTknojQCXUA2uh_aq-YHR-yQegvrK08VTwFvt7BgxRYB_GnErOBzmjj7aNkHxn6apprQ1_Q-Ui63If2IH0gWcOIM5_Oi5UB9dLsy6e3-51Rv6elJj_47lqYZIAvjyVhBUDVzNZBHHB2Td7H3F_FnI4cvgrUCPiRioCo9a__-t2FoLlO3gXDAMaPmweqc0gPQHVyrw6xrTO7ifbemAJKkbO1O5GiXnbjG08OQXGNB89fOwQLS5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=JY-OdgpNJPDVb24pBSwmq5pMhM2SQ7rAy0pxl8_G4unOeoez6IpNU4Jdu_hnJefqSYqHopgug8_NCHbeMHZ1rJKbmeG7k3LV0-f3XuNzTW3cj2Te6NIrVYyL-bYnqvY9YkTaK2_kv2F16heWC2qknb5r-b1wkpVf6Yt9m0uKMp__UKi_Oxo0t8Fd-3Bu6y-tupnQ8zkiq5GjZtBisWa-jMERs9Ng0Keear-aUC08LwFvy-JfYGxD_vrKpHOHjCux1qhP5lfJRFamU740WrdgEYrAU3wJZih1hvXwlzASkU8ZapoX0pAwBFPacYeg7oVlEFfDrSB9XvXBeqBLac46yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=JY-OdgpNJPDVb24pBSwmq5pMhM2SQ7rAy0pxl8_G4unOeoez6IpNU4Jdu_hnJefqSYqHopgug8_NCHbeMHZ1rJKbmeG7k3LV0-f3XuNzTW3cj2Te6NIrVYyL-bYnqvY9YkTaK2_kv2F16heWC2qknb5r-b1wkpVf6Yt9m0uKMp__UKi_Oxo0t8Fd-3Bu6y-tupnQ8zkiq5GjZtBisWa-jMERs9Ng0Keear-aUC08LwFvy-JfYGxD_vrKpHOHjCux1qhP5lfJRFamU740WrdgEYrAU3wJZih1hvXwlzASkU8ZapoX0pAwBFPacYeg7oVlEFfDrSB9XvXBeqBLac46yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlRNJKyS1ZpLYMPYxKX2s1wbUeThmSsqmkGB2cwqvWd4s5LQkTIKTmUaGf23QtCDqD5niNaIPwEdhwVyjND_cgmmbG6780G0l02kfxFQa0mlEZYGbtfmKq_UCNv8pJTSImIYT1IkvbLdaoLi1PhCn7nQ1Bt5FaV63Voz4nrhilI968hRheAag363gEl345D-MF3SJ_ZU4GPydA-u_8kcR4NWOQnCZGRcFUOp3saR_X4D1OHcXzxsjOR8TvGbaYqw0B0pPZX6qPhJW4k6QNr1HBI5o2sX8I4dPlX3cQxLNYuEobhM5Es7qjgE-y02bYiy9HWR2Lmiv1pYfRs_tblzkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IltkvfhqJazMz7WUlvOUmtidIfIKkKf8Te-sDHuyuLlD7PU-IfW_e8uxRxGVe7Zhrnh7dyCo34aqRo8bsaMCAZDUeNQb8Wv3RyKIDCtXcd2k_-bUKkBN0dHObNFcPObTLoNqHP_gyseBQaXAJI68XDZ_DmkT8hqoP-cBQizPEdssuzELNjdSM0_3kFrhqAo28lnYemOc1VE7_UDWV9791h_3eMTeWe0tbgTUwZUYLEptcogcs_ft_6The_nrgAonTQSfjtFajV_3OyyszDRBd78Jpul-c9mcRXkUA5TEAXG1PUJQvou2p5uV55Ac67B6KT7ZULrbHskgdYE5NOzzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8wjtmaxYT6JzBJue3PMGisgrKjXAGRlgw-ChE0lrMWSWr-cE-zMCns-BHagHeFJNaGcfYH1hbLmYrY63fiSTtMUDnkwYmYWAvT1JuEy8F-oXzOdzElpDnxVBjiMt5G_WRPA2ddEBkKf_sB4Azm9XRMzUUooGG90gDQ-OXOfuJVzPsmW0AMEhvHRgAfQNWRT1voiZCCcwMZ85qhEFam4F4hxAkaLzRt98-mTicc6Vr8iXxYXTL2mnq9ENQLYGFMd4h-YihsCNqwu0_BD4n579mKBEfMbZ2hlkHLDQE8kLA_syhWqVLRZxJ7kpbh09Y9eT-FuWXLX8ei6R73BfXjqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0Ir4_FE7ZcuK-WOJkWF-3emULV2OQ4veTm8NALEz07byAphw0vF5C6vuxf5xogHFnKk1BH92DYvjp3bUK-DMnNQeYOmlxUktwJygyfZkYFe4HtndneIOBF8FvlIJrjfF2WwQunZ_SP5QiBAytWUmYURmecrPDOLwCbCu-V6NzjfjiE9px1FpiAES9V5cjmT5ZamktVeIG_Fw69nnKQSEnZW8XQDyaZeTbu9V9S68pYlFtbk6d4cY_c2bh7GztL7Wqo_UXLjLUFXYvTYztzKaQZeA4rRiHe1IGU4MsCaIowhooxgqaPQNTPqq_GgnHecNkYwWv7OLI6ET0x-WknAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWLGzuTQsI4w7WkC7LkJCvwFL1xSJWOIGYMQjzBGU-A0NF2QlSvwiU8lnF4uJ3M1oWPe1J8I5ghgW9XzHYMuA3fYlee72Iz8YHcUz75goEla9TOwmWuDBop5u2MG-KucRPJ_Mv43xsBg_gXBJ78vjCK_jN3CQw8yzIagYWTVzNIG2TZyAGcL8u6hWKJQIuQo8615jBPzGJBWcE_P_8e2l7ZUIZ95cuBkDuKMnxkrp7ZZbUihrWNManf6KajB2gAk-tvSXSq76T8ewngnUqiTVl1rPz6_ypoG-jw2B0gr3iwU9swE55LV8K5I88f2M3ushw6I6TgkSsZjSwpCQKzJGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrU-qUb86lLBuHBwIqerUjB9daIuaTgkbzRo1JIwDM7FpYea-ZQ8XcnGns7-PS9L--CmvYy3yYdWU6sDezbUq-2_b2aCTyGS_N65hdMXmN63LgcH_Gs_PsfdSDK2KBdPRCJnoJ24YSya8IyZT4Ko468QIE0Xfw-KjRSzRHATZYY1ALsRbB5d5Nh4BbloLzgZX6-8g4QxG6z0qij5now3TANh3mnqzJ0LPMP9xWXk3_lLA4Z2mI4zGQIyUVHHwx7SdOLYTQp7vfAWHN51xHc-V9zUVY_8BVIhNpQjciMHXCriFfYeakbFP1I9gDKPVjfcKUJt-TV142B_ooCDwstizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLADCl3IkA7YLvpe5hagl-ZcXCp-B3Hvjny0ElpUgPbUuum-D2OlZSLr6RnP1-OV2F4MKNKKG4rcx40ldS8QyRNgfjUaDXbSXft_lf4u3fbx9y0uJZxvJ2mgV2KEG_Soekj-eA_VN06NuIklFXw1ENWADTIagKur6rlqrSGyUIirMHD-beQTB-S8bThg1WjQN_5E2JSUMUA-RsTVccz6wkiTFJTyyXZq9SKLUoc6NjDbf053FumR_ZnzzlVmIzV562c7yKu79Jv7TNDYx1Vld2DZBI0zCZ8hn5By9PNRyDf7s_CX4ZDVOfTp7mGaHMqNW_OiNeawHFxvzAXS3QGjrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdIwLlUa77-muKlU8wbmjKjwI6tA4KrszRTEtRe-3wwTkXcxymsSdB_hiXJhVDuT_KslNGmXvga8nxWgbdn7bp0O98YywoDfZQ2ldoWiNbj86th-oBdqw_4bmghnC28ix1r7XoC_VFmpTBCjWZtxqLchf3o2S1l8O29igFbEKnDjrQqYhY-MUpYIVGtzoSr1GCfAyDp1pUzpUKEpXW-GdSobcM4cA1X4OBSPhqdPN6_FeZv9MCRAUAo5BGT64z-T7Ry6EOCW1FADma7dr5m1a4KhKTBJvVWRUrJTsT4uD9TEOUYDm6BKes_mAIPtMO8p6pwsExiwWRtzmpRN5nwJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LynZ9TvGj2Kmax1IizVRH_axwArdHoL089HkqhZrecw5B0XBRO5b6ME8S8uCsJapSc7Kjac7UhZIUln0w6canUPIubnrULJaZKIAckgZyoSL1OI24O6jjpClBTf34Z5_z3_-n71JOWacs6iHXvDViY2uGBkzcSBUCNxYGf2og4FcXqBvJKJb3_K01g6HWC4iX0g4OYn9k9Vy-y1RYGkJCJPR4olpcrx9tcHZKbZiFVIDKNhTXWCv1WxIcvq0LuV0NbodNxokNk-ynLQOJ60c1lV7kRM6YlzPDSh7SxAtBCjPqMXlhi5Xwlow4DD4SUHNj26VNX32-W5aZg8k046OEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X17Hho6mP_fuPb9UufASVCaqa9tk4bpsykKF0psYIzKePPHgB-mcnpr10s4Ad8cHGHw5ZGm1iPbA0QhreEx4WwN_JWwVx1XLtkfg1uDWA-llg_LWudsBYXfeUW8waiDypPohjlHfkPWIdBXNDvHL5i4hx3i0Wrrim7yWedJSXNdJsyd1TzXjgB4oLgCWrQM8B4Rij-bxDTZK1h7e5LOWF0F0hzbRtlGL0HxOKUm3aksfQNlTVTgfmpJgFi6-xH9wEM-bymAbMV6NW-2go9g7TaHxdIwailHFh6uJxXpz6eH6B016e8uSgUg7o9wIbSZkYqYU-JjdnCtnhcLkVSh3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGTusRwz8aKAhdCE9roDEhDUjqFJ5OOD4-OX_QMHW5E5MI9uuoHej057r-t01axAs4hVOOZ6tDpWuJed1633Sy3tQkS1iiU1fq5WEZJdR19TgltVe8zHMSnLUyLgCs9Um_M1rApfBvORZ8vaRtx7z9mmDC4KXtoBtF-mqOx3l7SONlIiJ8GbmAism_xfOwh1WTgahorWKjnyqJsCilhLcXIFDdnk1QmC77Jgct7Q9f_YsESqBQbM4PWh024K8NEqhoS4Nv4-hg1oMflUsHiyYkRWNf2ocD5337bXq0qUa0b3z7OwLjXwMffeSc6vu_j25AX7kiiYVy8AUNtW16rLyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XPgRwZvOi13YoI-Pa93zmFcjoC7hqzDc71_mTPSa3xzjt6p2e3EOKGn8SPQUoM73IQoS6fUQF3hDFwuYetoH2e5BFL93bqCuJGtj-JomGHrnXn7_66ordAuETkGi1arYDeos0_aUn-9C7VRBqkmeRRiU8vw_yYi6HLM3JVdQTAU_ndat01iMXkZkkjTQcT8UyJ5n8F_crXO6-SvimcNEShQ1dCClTfjH2am82d_ENMV4TfukrEE-WRrufHfP8DoFOcsNes-nh8KwFjpPlmXYpdHr7-vSCTvud-cdkMs_KUSmz0I1jDzNRGHKHF7CKTHaFHVMiN1SIbo_bU3qIpWJXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XPgRwZvOi13YoI-Pa93zmFcjoC7hqzDc71_mTPSa3xzjt6p2e3EOKGn8SPQUoM73IQoS6fUQF3hDFwuYetoH2e5BFL93bqCuJGtj-JomGHrnXn7_66ordAuETkGi1arYDeos0_aUn-9C7VRBqkmeRRiU8vw_yYi6HLM3JVdQTAU_ndat01iMXkZkkjTQcT8UyJ5n8F_crXO6-SvimcNEShQ1dCClTfjH2am82d_ENMV4TfukrEE-WRrufHfP8DoFOcsNes-nh8KwFjpPlmXYpdHr7-vSCTvud-cdkMs_KUSmz0I1jDzNRGHKHF7CKTHaFHVMiN1SIbo_bU3qIpWJXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rv2pdKxEami8bb9cXn7jNF7dlM0Sdx3LcuWQnilz00iknDBspGW_v3HFIBkeb0YEpoY6II6l3T_3OKFfgmTrFBguMlhyEF4Hnu3A1CG7Mhwuig65cLRUa-nObSKJr8UGGaTMZQP9oDCUcqcSqEiocL4CD6JX0c-FOimSN_3BbGYia1g9ghY8B5qVNZyNqtikbxo0GzZrkw7wLQx-I3CQo2j-OiPw4-c54Gh1f5P4BOFrx8I9M7mHGF_gr3gHYsWthoQ4rbgoFFUHiJ4pSR8y72SpW-HsJPL1eLX3hDEMC84iDImpivzu048ig6dtNQHjJFrVaIy0Q54CcykjIz9Q_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
