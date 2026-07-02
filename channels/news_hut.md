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
<img src="https://cdn4.telesco.pe/file/Z29MtDzD8kuVCuJ3wbN2RoolRIKGskGCZj8Ozjv9soqkW7eQTKkPEtj3G4r5i_rhUMHNL0Quz-gB5vRP2CG3eHoLIaLgFeLAMOisJzoucDBA2Y_KQKr9vaKKYF4IrXWN9HIEn3EVBhhbKh9QJ5DzhG2fr40VNv3ghKi020_B_2Ysl0SX11ngWVn0_j8dEejfC9u5PeHj_Q2GPXx36J3nY8W5An0KLRUtuTgdtPBh4Z1i4Rs76B0uI0JpSfbKpdgQ-jB2HfX7c4iQruq03uMe3fujVmsBb8R6BOoDZnB-BY7iMyNfPXp_gEPOw58hsB-MyQKCBpRAHqTzmOBqpBQR_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 212K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 03:26:36</div>
<hr>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHNBOfObDhohgiOJ2eTtJrHwocUrIerEjuSUK8UoaoxldZT1ILI6I_-J1ec5dAm3iT04duOiDSQ-5jhTbub-inkfW8n7r56l1_IaBVr4NTqzgm2CbNrK4umla_Dg-KNWy31yoCw-jvpaYSIsioMGApnSz98ySp-Qtj97yW4VJGGkb6URkAEEadKw0cHdqbaB7PwI7b5PKx2OHfoPMWPBoGSHmEGqP_QkFJzD5P_AJdQRjuNqJP9IdE6L8NhlSDnFo4b2P1jzKdiZI9TZPa3qSgOO2mI4DrTjZIpjJn4izOAKHXQAS5oUPi1Oehd-mwIRnAI6CoAA26q-QmrN4wtVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=WnMkFW8uuNJdoL9KyJ4ULuTB1w2a8gfXlq395jR-TcM5S3UeG9RYpaVI2PvXembJIm4eSadMHqEU9q9dEetSbL87YoljBnF37zDNMxSabv1NHkbKN0oeM8BvN5M0ORJGgNPbt2Emf4EykeZnZzFvsh7ySTkohRkhQstx7a0Oe9J_8EZDPhWtMYDrvnNxjxQF3vVf6vthPEy68FKjK2kRkkZvzNcYgO0z-rniSvkrVlx-ImglECT1Jk7BShtIvRs-ibciLXOFDwQmoyO1L-vgntnBTMNgO5I_4Jqf5bnO4HlWgqD9aYd7AV6lRZJotThEg-jOJPDmKsjd5vfC-s3g2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=WnMkFW8uuNJdoL9KyJ4ULuTB1w2a8gfXlq395jR-TcM5S3UeG9RYpaVI2PvXembJIm4eSadMHqEU9q9dEetSbL87YoljBnF37zDNMxSabv1NHkbKN0oeM8BvN5M0ORJGgNPbt2Emf4EykeZnZzFvsh7ySTkohRkhQstx7a0Oe9J_8EZDPhWtMYDrvnNxjxQF3vVf6vthPEy68FKjK2kRkkZvzNcYgO0z-rniSvkrVlx-ImglECT1Jk7BShtIvRs-ibciLXOFDwQmoyO1L-vgntnBTMNgO5I_4Jqf5bnO4HlWgqD9aYd7AV6lRZJotThEg-jOJPDmKsjd5vfC-s3g2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=Aq-ZC0wq2-h4KQBeFB6anT5PWywcVADVm9T-i51K8Q5cJ59sI50w0YVXh3r60XO4uos7BegUhype4r1RUJAJhGBJoSjBkRZ9r9Yf6JyXQE6CJyzUxJ7_cb_GWXMQkooH8LL56YbVDU6VTT3FS8MgWir43rzNO4XAUKvoYiqZ11EbAv3ci9veuBqJr1PZNS8Q4vtzsBQuYB1RJ0mTBbF0mE00WQxZGyFwKyPZw8r428RNQZQ8LkwquiTpDrV8VDUnm-1IDOLcUy6rfjQZTfHU4EbJ9exNuGEqga8Ck9ndaPk64LCbB6RZ2-fmGajm7OIZ-Ch-wRTcHqmhOdcJcsk5SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=Aq-ZC0wq2-h4KQBeFB6anT5PWywcVADVm9T-i51K8Q5cJ59sI50w0YVXh3r60XO4uos7BegUhype4r1RUJAJhGBJoSjBkRZ9r9Yf6JyXQE6CJyzUxJ7_cb_GWXMQkooH8LL56YbVDU6VTT3FS8MgWir43rzNO4XAUKvoYiqZ11EbAv3ci9veuBqJr1PZNS8Q4vtzsBQuYB1RJ0mTBbF0mE00WQxZGyFwKyPZw8r428RNQZQ8LkwquiTpDrV8VDUnm-1IDOLcUy6rfjQZTfHU4EbJ9exNuGEqga8Ck9ndaPk64LCbB6RZ2-fmGajm7OIZ-Ch-wRTcHqmhOdcJcsk5SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=Z7CQ3heON4lsdB-xac2276fQc8-_NkhZGllNrFJBlpAum4JB_Yge1SSTDJlI68s6pnDuv5rvRZcGxvPjYZC6Y-Sh4lAXry335Q6Txo5CtJ-mTNW89k4wJxLlhksrLwIat5jBmhL6vMd9U_Eh2Pq3RPmCDF8lKX0lby_SrxVH3237xBH1nUHNZnOz7_G6kck-LfyxWL6gu_gyVUuvOXpC4AIqEwzoyfbckYQtcvi8GQ28i8i9v6Q8PZdS-dTo-HgOmSWRNlA8hPg3IiXXwANEnTAmkhuxqVeKrpbfgE9GtZ__e5L2zqX3-2wp1ytqpiz_6dvI5Dd3PBQKniTuUWVoGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=Z7CQ3heON4lsdB-xac2276fQc8-_NkhZGllNrFJBlpAum4JB_Yge1SSTDJlI68s6pnDuv5rvRZcGxvPjYZC6Y-Sh4lAXry335Q6Txo5CtJ-mTNW89k4wJxLlhksrLwIat5jBmhL6vMd9U_Eh2Pq3RPmCDF8lKX0lby_SrxVH3237xBH1nUHNZnOz7_G6kck-LfyxWL6gu_gyVUuvOXpC4AIqEwzoyfbckYQtcvi8GQ28i8i9v6Q8PZdS-dTo-HgOmSWRNlA8hPg3IiXXwANEnTAmkhuxqVeKrpbfgE9GtZ__e5L2zqX3-2wp1ytqpiz_6dvI5Dd3PBQKniTuUWVoGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOuMgUcNhEA2vQq2LfW_K5o9h8H3Nz3Liv7rmjnyDYkSSA6sN6qsT4bKhGyUKHyV5w0du8_I1_Qphs50pfSLDim7jnATibj3nSHD35aNnqZoWRohesqFlgGKwBCRkDXIXHJSa8CsmBwAIaCG2He1CiFhfOylU4IL4uJ4WkYSMET6pTX3F9sFMft50r80ADushpFG86zQs87fQMXFb_Xz21yjsvZusTrV23ZC4mTH6A_y3qGUEeSrXizc-85ErXHU5mRkwt470so76IOxg-bOLD_nwIIlMRo8G2wTcGDbQozsvRJgj6fwk6hD2fmxcFvi3HIdozi7fqyZlF2qo8q8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vuz0732779nWRs8b2cUuUDWdgS68-oCsUm06cdpwdqBuH2J-k9_sQ248bptz3ss0XZ3qS8ubrSUIU5xQlCV08czd1XAV22JhOH-svqCjDXZ5yEa6PwMj9GPifGIPgCnMy-lPN7ctKHHhirdZ87iaCEl5XnaXvcF6WICObR3uqp_6oBTGzUoVEU8-N66KQ6gjLMyWVneznkxfriPOHHcPvTjPlGNy1klCuA2TdyawvqLjAnXOU_qO4Cgw1XoaHuatHYNpa1b0wwzjPzWBfrslzsqaNYcIleeQD-jSm2XMAI-dBNQmdiMttIkWR3KoZyGXxFxM5XF63yUrZyRGTjXIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTQzLW12fcu_3tWKsVQa9HXzX4CchRGQgUhEbfiwPqosOD18R-ABbvvfcNGM6qdBnepHXhIOCA-cf2BoFQYckPz74Mf46InfqMX7rheGDqhJ-EI6LGpf-AfEkNhLWxiykNH98GdxdM5o1PygHzLNho2UjvgEt-Y9bqDpAcntAqws4-UdlxUSVmUhGbrTv4PjRdDH2sku22gNBAdWU6ljetXtXEa_kh0hPpCtBgIM8DofPpZlJi1nuzst-tFa1f8PuWGsEgb7VzNRJAC_4_Qyn1aPiPWdS3uh4jpkYMZxdpjNKBWUSc2pufo2qyvVdSQHCe5aZ6FEciqTBL-06Ep4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=Vx7Ox0ATL_ohIBFGL0C7tds3AFQdRLA76HuLybJgEmBDtLwY5u3CrFZNkwTQGUa58Kqv6l5Z9v7OyrG4I1harluDaPXSoEXY5Bdan_zL5Rc5ehUcI_Hr9r2APGHi20Bq-a7U2VCXZU0a25MrA0lcHDU8qlzkXwEjUj8lxTxex1x6WzhQRSQDrpIB1I31C2ufJbmI3ZkJqiL2NrQ2al3_Z-OLC2PGPmyNNrt2xIWqB8qycfRGiYodotQY-O_UtE_FfEUIPF_Mucf2lICGdjZEFjBsVwj1slOqaAo-rib3ckyoV28xvzW5R8lh43hRHepSquUMvjnn6EUryGbKb9dFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=Vx7Ox0ATL_ohIBFGL0C7tds3AFQdRLA76HuLybJgEmBDtLwY5u3CrFZNkwTQGUa58Kqv6l5Z9v7OyrG4I1harluDaPXSoEXY5Bdan_zL5Rc5ehUcI_Hr9r2APGHi20Bq-a7U2VCXZU0a25MrA0lcHDU8qlzkXwEjUj8lxTxex1x6WzhQRSQDrpIB1I31C2ufJbmI3ZkJqiL2NrQ2al3_Z-OLC2PGPmyNNrt2xIWqB8qycfRGiYodotQY-O_UtE_FfEUIPF_Mucf2lICGdjZEFjBsVwj1slOqaAo-rib3ckyoV28xvzW5R8lh43hRHepSquUMvjnn6EUryGbKb9dFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IMd6PvIQtfL95x9JoCWpAxXEkyBUaPtU1jPdhIMcGj3ZEwSTS7MwwsgYR5slKPC8GImtfwSXedf5Pu9SwP4lSXw_AI-V82fpV5zrSywt9D6V4gTblnqgIyn45ldxQWBk93VMFR9yl1itvIqKL059EHXRnhPvJGi3umD89wYe2oXe5C6TEvEq0x4ajj8deUVB5TEOoL5RQXLSz88g_XSJJXZaT-EdeGJe3jOk7qHcwB4MkPlVnBwsoJNKrvu_cwJpIyfK4udfmRjCTELoAXoiETPGOHR9s7GB9dhQ8s3CNQox7Gkt5SksilDg93B6v93Z8oPyqj94r042MbNKKoH_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=mmxpEd8sqrpOwFLalpUic4M86VXUFzUYxuFzxVgS2cToRDkczRAmpRxOVv-HiIP3cpdgEns8b89FH8zwDur3tR8GVDRQn-IAv8K6JhTgkeS_-ZdUfBCU8XFZRuBkjAN8g_cN-zTBXfiQ-qX86FVlzLPqJJwokjYaJmTGC0uXbD9Fua9M7OoxovJQ5c2Bilo200RNELiRqzaamt-sGV7F2Nr7Bb5mvoX-DyyCXF55YATWpg41W_KvRSHB46W0PP7GbWhXqZPJuvN4ocRHk6CFM28TbQLvzMxh3rXKbeS9DyCJ2LcWS8vc7VEEuO6sjC3WRLKGpULV3rKROYQHwItGVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=mmxpEd8sqrpOwFLalpUic4M86VXUFzUYxuFzxVgS2cToRDkczRAmpRxOVv-HiIP3cpdgEns8b89FH8zwDur3tR8GVDRQn-IAv8K6JhTgkeS_-ZdUfBCU8XFZRuBkjAN8g_cN-zTBXfiQ-qX86FVlzLPqJJwokjYaJmTGC0uXbD9Fua9M7OoxovJQ5c2Bilo200RNELiRqzaamt-sGV7F2Nr7Bb5mvoX-DyyCXF55YATWpg41W_KvRSHB46W0PP7GbWhXqZPJuvN4ocRHk6CFM28TbQLvzMxh3rXKbeS9DyCJ2LcWS8vc7VEEuO6sjC3WRLKGpULV3rKROYQHwItGVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJk9GvyJW3OQ8I8WfukEvnqBEO6CcLIG4Mn17c7HD79QR50iLZhv7Lu8GHplNWSuHtnXskj93wexuVzIg4Oak8WSuGj8Vxg-DBrYdIMJD0in0VPGEpG1H1pZzHOaajtq8ZtAGMSY3CDirhDujALce6KEGJXeQ7u_2GX214n-Z6B8NhTjFxpcEM1ETlLHTPjzmos11pFWYAK0wDLTE7BJNtf1Vj4QQC1djg8XgYkdpYIAA7XoXyrUr2X9MmPNIcNVajs6YFwP453Cu1Svi54OdmpHhKof36v94YjotzLBoiuIsDEQivJMYbpEW0arxXDm4wX-YHQJ5pJtwF1OSxCcCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=BLnDLM7iYokZ0G-vbEnQJvCIFyFwThRghtwx_ifl8pcCKdhpOS8x5yIMQQtC4taBtwrplzLq40LVOcqlax6w3yPFt2bMDnrc7BDA8OfXJe6osD-pNzxx2kLr6duNvcbEfizctxrr7wUJ3EatcZpd937BIuB2Ns93ZEp6vkFLRb1sZmr6-zZa7r8NThG0mBavGIg9WJqBcLGLbtzzBVvXKjwWLmfeVAciJzUPs2uvSa7Zg-wvHJyjUGNQJ4ug5H0mI4SZ3n89czpbScKTNEbD2ukK6Bvh0Zwro0hRvzGrzEfifFAI-tI9aGBVtZHdEHDJ7cGyHldmh_iNikE2L5b-_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=BLnDLM7iYokZ0G-vbEnQJvCIFyFwThRghtwx_ifl8pcCKdhpOS8x5yIMQQtC4taBtwrplzLq40LVOcqlax6w3yPFt2bMDnrc7BDA8OfXJe6osD-pNzxx2kLr6duNvcbEfizctxrr7wUJ3EatcZpd937BIuB2Ns93ZEp6vkFLRb1sZmr6-zZa7r8NThG0mBavGIg9WJqBcLGLbtzzBVvXKjwWLmfeVAciJzUPs2uvSa7Zg-wvHJyjUGNQJ4ug5H0mI4SZ3n89czpbScKTNEbD2ukK6Bvh0Zwro0hRvzGrzEfifFAI-tI9aGBVtZHdEHDJ7cGyHldmh_iNikE2L5b-_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVUfbS1-hRgUAA1U09dOnUIDCUQ9rEbCDlM2Z-VbJBDgN5Ilzny4dMlB0fQRKinANxP5kCWSnd3ipts8RtDQoY3JBXXPHLFda-fXdaxysXFcHMQVYg2gWT2Dht6Q_G8nAWVxgnPEsees5ub_v2e1i5Impm2_9rNbapjeDQFyACWHSOMGe_DBNjfyQA_qGaFQUEdpjx18urRITLmng53Mku8WVYuBAGJRAXzTMZTAiHXcAzpV2UUJX8xSEqaOGmRsZho8gz6w6LOfH8VF2gmqwQR2EdZ92V5VgPbdYzZVo5SMUEvJjtS8tqhljfWecRAnVsT8Kfcc9HKln-Z29LKeFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqK9xctnlVvPpnVbj5vOwRXurYw4pbleRflAbvDL0BxJadcqcI8CjQOiN4aA83loOTbsHbjEOCCrqpcE8IzaeOiJNdp-ifhNF86kimZKW-g-kifKaCpWamM-LapfBPY1qPK30y1U4jDl-LFgy2i-QBdMB55_Aq65fEzmB439HtzQAyLk8E8Y2G-JPzSHbWE6qbKjXlOAsBSIAojmFZWxcYxZYiVL5TYakQndZRZsOj5frVjug31kGx4xGNP_SuMPBa2CUgjY-6_JsFuEDaEyJWa_C0M8ll_PN_AFGRubL6a7-UAtzCHg5tVSp1XBoJ4Q8ybeOHZ4IGvP9G-uDutXZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjNho7JFd3r8kzA4IJUMJ62KFadGMiVLl2N2RQUiz9KOFfjeRKuDuAbIeJHCbDH_yup50ptX6xPvu7G7Kkk4P6cOGvKPIzS3WmbsTGFztL1hKcubppU6D2_RYJSFV0p1ozFdQiLr-8mXXFWtQVMMEGRRDhZaUtwlcqyJ9oPOmhZnal1wW-ojPLSyKyR_YKX6ChiKhL3h-VJjK5CvPy5ZsbYQYaESavMrsFD0bSAbCcPKaWp20MAQ3vxOMJzf587721AYNkkRmi3gw5JoWuJG0mLDOqCDHAQJrwA6wFw_a73fHtZA7bbUdCRN879WiXgmbZAekipWktep3sb8m5aSRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMuVB-8aYZWdmmtfl53F9taUrzrq4PCcWd0lYeAmSOfXVcopGPSo4K2P2p4lYWgWF93k1DLnykC8-SCSGhXqshJRUr8QIx6qBCgESVWoY28VsXAcTiAO9o-jh4szirza1fTPH15WIthedVhONyamvySvMCLIndKMRqfi1f_Fg3Gqlm2mxlF_WwhlkQkCFFOEej1tDWJSQPs1VXNBMAyk1gk1FWJ9iEQ_n6I5FZWMjPgiw3dEIM5fxzROGslmjUApkUFwwhU3G6SfV6L4dzvaMAkfz2-M90aZnroJj1-6grArvuKp4RQJxnJwORxVIM4NCjrdTslklYOO4bc07cXKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwIQveqeG1Hc_7YajuUyMYssWCsnuqcVv5IkF8p39qrQXZrke3cOrWsnfjwcMMie6YGj_L4KxB6BeYKr6HACHokWst4fA8le7Z1CmVTa1Zi-volX84JIwga1rk9oo4QvsMCXAOdAyJJw_dsadGt81TqC3VE-iSnoV2QZVDiuY6QOh9BsIJcVZ7pKs82d_9zgqNFBxe2fUE0gXJdl0X6t5s3k1BaHrWgajfb9VlHHvuUuxa3DmCaiAYCedLGDIEjh4xsLCsgl8KRiQjljOUT8KBe5PFLvJsjC9bvjmrGxzMwySIwNOVbHNh6tqMPZOS6Z5wUh3UuOQjsVDIgki48IXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=nKHqSo7U5wdMvElN0G4O45aPWh93xvoe7zo3HEZzJfrvAJo__opdPXeafZASIrMt_0WgLgGwqWJuFdEc_q-k1hixkbUt-ZDlTrmvf1cKQ_SafV4UKE2tbl3J-_JfyFmhnK7nuiYqqVfDRPhbWvEKZ0Kn1hC3Id2_ynD-F8Cyu1CgWzey5gftAoQUJr9Tx0WN-oPmbAwJW42OspWuDeQwq5d4lxTBjVAS7_5uWwbSchj4DAJTdRkdUzUEztfxuPx_jlWMZ-QmW91UBNxhV8uoMylGKQN0F9uM8VerPqCyo1rLbBthPaoBQKoMOGu4GaILdPJncsmV3ZIwCNWeEbjEpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=nKHqSo7U5wdMvElN0G4O45aPWh93xvoe7zo3HEZzJfrvAJo__opdPXeafZASIrMt_0WgLgGwqWJuFdEc_q-k1hixkbUt-ZDlTrmvf1cKQ_SafV4UKE2tbl3J-_JfyFmhnK7nuiYqqVfDRPhbWvEKZ0Kn1hC3Id2_ynD-F8Cyu1CgWzey5gftAoQUJr9Tx0WN-oPmbAwJW42OspWuDeQwq5d4lxTBjVAS7_5uWwbSchj4DAJTdRkdUzUEztfxuPx_jlWMZ-QmW91UBNxhV8uoMylGKQN0F9uM8VerPqCyo1rLbBthPaoBQKoMOGu4GaILdPJncsmV3ZIwCNWeEbjEpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=rt0NUHGLv8I0re6r7OQMmfw9lTLl7_mkr1JOC7T-vrzuOSpVvHGvh2GOMny0LauQdbaT-IhfSLCHPi5viBgR7defWenSc9du9lm4TWVmqrA76j6sWMLkdpLACs97JBUqQB0S7bxue-JfbG2RWdKAIAhzDw_BHvJJ3DzVmPfXL9fd_F2_Twp0iv4TKvOsUO2t2bJlFr1WCVBdq7vlMzUw7jEsBLPp1PJ6s0mfwS8hDC_uJC3FrMr3H5YBFpAa3R4iFQPbn1IinAKpsnZjyOJ2KFnGcf6PWKsBZDEOdinsG_c0Zn7RtCmQEs49CFAKQegTN80xG-16jdLuAooRBWlOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=rt0NUHGLv8I0re6r7OQMmfw9lTLl7_mkr1JOC7T-vrzuOSpVvHGvh2GOMny0LauQdbaT-IhfSLCHPi5viBgR7defWenSc9du9lm4TWVmqrA76j6sWMLkdpLACs97JBUqQB0S7bxue-JfbG2RWdKAIAhzDw_BHvJJ3DzVmPfXL9fd_F2_Twp0iv4TKvOsUO2t2bJlFr1WCVBdq7vlMzUw7jEsBLPp1PJ6s0mfwS8hDC_uJC3FrMr3H5YBFpAa3R4iFQPbn1IinAKpsnZjyOJ2KFnGcf6PWKsBZDEOdinsG_c0Zn7RtCmQEs49CFAKQegTN80xG-16jdLuAooRBWlOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=Gzmt4xOIlxonsa4r9jH5c5bhbN5EqPpnD1_q-kbGT7wFk4wVIUu94LUpjSPJ_jKZ11mpEOcjAcRZYp5SL-znPT1ceE625rkSksYGhl3tBXF9626VJpxyGK6VKIllUhQfqF4fuQXIia58bOWtLsngDQY_qufnue7MAJGVBbl82-nVlBsuqLZBGiZ3k61cqX6asZYHDHeAF-fCWGxH8DoVWD2zEEFCDl3c2AuGi9pv5AafpodvIecztbsF0ycqlyzl8xRwDr571Z-lr6WFTXBflpp-x_niXiI-6hSrod8lrrzGq11LTJnfUt4Vcf7QudSgyfIQNrTlr_TW0uvXHKw11A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=Gzmt4xOIlxonsa4r9jH5c5bhbN5EqPpnD1_q-kbGT7wFk4wVIUu94LUpjSPJ_jKZ11mpEOcjAcRZYp5SL-znPT1ceE625rkSksYGhl3tBXF9626VJpxyGK6VKIllUhQfqF4fuQXIia58bOWtLsngDQY_qufnue7MAJGVBbl82-nVlBsuqLZBGiZ3k61cqX6asZYHDHeAF-fCWGxH8DoVWD2zEEFCDl3c2AuGi9pv5AafpodvIecztbsF0ycqlyzl8xRwDr571Z-lr6WFTXBflpp-x_niXiI-6hSrod8lrrzGq11LTJnfUt4Vcf7QudSgyfIQNrTlr_TW0uvXHKw11A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnhCD1ih_b0XXLpvBDIAZnB4fDiC5H8SeARPt5sTfjdSnyjh7c8SvaS22amE14lYKRALdiB1LUyndlGc7EIoSdodyk-Ix0JYYpNSTu2ESI-dyxzrG0qyzYLicA-oCr0CC2xCJ_4kEMn-oZIlH_rHa6SziBupIydZLbCPDGrTxq9e0npmBMyC-7bwNsDitoSKjVyF4qh3rNn4wd5sck8u5MRal18jsX20GRJij1ZXaYSXY4d2R4wqI2Qws0-PoAm6gdomI-mkgiGmVz2gCk-hCZaUiWFNBB9d4JBTsrXSTAVvsugLS0NYl_CdD4VS8tQuUzsNkAIL5fsjpqvLJVSu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqTkhnTZ41JnmVdIDMm5Y45F1mYe3vtoy7AaKuh7n_JVqeJ7iEUHMEvfLeD__GXNy7ulBHagzDoRqtRbWH_z2cN6XYbGJF-h0Eib26G4Z4lVYKYvMHOb4rdT6weZwNiN82AjruA_anoP9PTaKJAOmBQ5OAAop6liPSFC_hmKca35FpH7fq-m4STugYe7dMhxsOheTV4_tQaXnxiUJmsj9kcQHkVVnq8_o_iwrFXiVf_lbBxwY-6d1ILamDKKChAIBpfMkP6WN--Zeofe6qDsqWVnBaeUnlB1teM_2JP2xevHBpRe-LDIT1QGv_H7Sif_eYUNPMn-Ig_8ZQ8Ot6XNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUSPj4vuyhkxsW-C7YOxTIkqqMTxNracE_iHXbUY6kd0bM1Ml0qVRD8ekCVyROl6OsrG45gJFCwbRUTGXMUClNgTs2ILMYPjqP4g-Y70JOiZ8sDOJPfGoeUCP76Xa46oFxdEfEyq3rdWWMPX9wA4NgTlYvDMwJtTQh2snM9mwmiB6_TJWX6vf9pjqNIQZzV3CVdL7xarFz4BmX-0huY0lEH7RAHoiK6u3uu8yPkEzitgBUjeeOc7sbwARb60WcV-oYSwHCkKAHzh86SI7cCWmRdKakXOuKGsEmLEasapscfBmUvgnhE_hG19aZ9Fav0VpRKYtFN_F6Y--3aNb7rp8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=Pt9pv8uvn9x4qAHmPdMCt0p5x_h-mVk_zwSNyT16xjXRkCewNzEdJ6D9Ny6IZjczopqmqtFonUiI_KFwqe7IFynHRXBuAAf4D1bd9f-AXji_FuuTF5CX3kRq1q-Z9Dv8LO436JkZ54m-jqA9vOrIb8WBeaBCOWzj00OPlxLEGw0NWk9bw6LcKEpbMeBJAo0Lxzs0CcssO5so-flZ5zLahLHWraqr_0TOdNvQ9fvrA0jBz5A4GWG9UCR9HhVyCVxiTA_FQKJD4Md_yFgjdO-IH5i2dVJYlh8vw_iK5GQ2g86nAIx0x1Zb_weaRCVSMVOQ_SPoKqZziBmUcnNJ0k0SNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=Pt9pv8uvn9x4qAHmPdMCt0p5x_h-mVk_zwSNyT16xjXRkCewNzEdJ6D9Ny6IZjczopqmqtFonUiI_KFwqe7IFynHRXBuAAf4D1bd9f-AXji_FuuTF5CX3kRq1q-Z9Dv8LO436JkZ54m-jqA9vOrIb8WBeaBCOWzj00OPlxLEGw0NWk9bw6LcKEpbMeBJAo0Lxzs0CcssO5so-flZ5zLahLHWraqr_0TOdNvQ9fvrA0jBz5A4GWG9UCR9HhVyCVxiTA_FQKJD4Md_yFgjdO-IH5i2dVJYlh8vw_iK5GQ2g86nAIx0x1Zb_weaRCVSMVOQ_SPoKqZziBmUcnNJ0k0SNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=oAFdhcQR-W6EoxvYh6HHto7yMn6iaO35qobyu_qUA7onTOvslggprGLIXFdzrUhdZj_irVHIH7irFB3hRLYmV2MIWv5B3nI9S2RTg4Z5asEAX2gXuYw71nw6dxykIX7o9fhYsw-Crt3XbEqtv6mAfSWS0XKfhQT6mKXzQawpt3kuJPdwomIJfXL8dOwAuFUCQDSzvNPoYHfGzKq8lovY69fVXQGCPUpO-0CIEJF2KJp_UIYHDo39H5C02aG8MvDkQ49r916BfFXJ0lMBIPt7leCblmhvPm84IGCAxhAdOTIVe1pT6_kRHh6db9zNlZ201LWystgfVMitglii2PEtIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=oAFdhcQR-W6EoxvYh6HHto7yMn6iaO35qobyu_qUA7onTOvslggprGLIXFdzrUhdZj_irVHIH7irFB3hRLYmV2MIWv5B3nI9S2RTg4Z5asEAX2gXuYw71nw6dxykIX7o9fhYsw-Crt3XbEqtv6mAfSWS0XKfhQT6mKXzQawpt3kuJPdwomIJfXL8dOwAuFUCQDSzvNPoYHfGzKq8lovY69fVXQGCPUpO-0CIEJF2KJp_UIYHDo39H5C02aG8MvDkQ49r916BfFXJ0lMBIPt7leCblmhvPm84IGCAxhAdOTIVe1pT6_kRHh6db9zNlZ201LWystgfVMitglii2PEtIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Kl9HAPEDGqhINFhq4GTfEtJo7k21SaGHgFWQ6k93-HPNrKpWp_vG4tRaIsrHsAOpRBxN3jzbAei2q9y2C29L-dmb8skIVgQWjP5TnkR8Vi-xznKbem1o5b-7nWRqi5nZ8A5SSxkdB27HfM3gYptLGUTpY8e2M-TBjmb8HqftJmJNy3xC8WC8v47qTX7kM4j7aTyjFtcmRYDC5OCtJj0kBwI-x_MBXRaxhTCP8EDeaAdN2-Aa7xwezvXEOgWoA_yQGyRCeJVvgLbovsXtKTsn28iddpCE-FMurtxm4kRc6Y2lqEmKwzzxe5HT_ZWJ9Vzxld_lJjqrTcbtd_jOsAi6tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Kl9HAPEDGqhINFhq4GTfEtJo7k21SaGHgFWQ6k93-HPNrKpWp_vG4tRaIsrHsAOpRBxN3jzbAei2q9y2C29L-dmb8skIVgQWjP5TnkR8Vi-xznKbem1o5b-7nWRqi5nZ8A5SSxkdB27HfM3gYptLGUTpY8e2M-TBjmb8HqftJmJNy3xC8WC8v47qTX7kM4j7aTyjFtcmRYDC5OCtJj0kBwI-x_MBXRaxhTCP8EDeaAdN2-Aa7xwezvXEOgWoA_yQGyRCeJVvgLbovsXtKTsn28iddpCE-FMurtxm4kRc6Y2lqEmKwzzxe5HT_ZWJ9Vzxld_lJjqrTcbtd_jOsAi6tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=KOZgcHOpQp1janCRVFmE5Nxl52E9aE9hSnWuuHt5hqcD446tgsf-Pp8UoSXUFDbNfAB1CgZsy24-l4cn4FxfQxXfUon7mgUzoKLS3-fYi_YKyjh9P8Ln07KoxlyaVxvPSONZlVpcpGSD2loZqrCD-vAN-uuFvmU475Wrlx6YAjJiiiQxfMPWxhB7yyX3cIsyCbHyoY1yUCW2OnRtJyf_ykmNoMLl9LbMe3VxERkC9RXCc4-VM94_lkTuAtkSsx7XhvFkvJ9Ilh4EO9XEIOTTipbnnp3NiGNUEr9aJVRvLAadHKXApyekVMp14NCuGUEV3B9itd9agWP9QKuTvInZaq5WM9_2CrsB1LBuQaaG7rqm3MiyMUqpNCD0KLrRwUqnPN1R0D8rUYJrvDjl_aZAkQmSQ2qtC81xP3Riu2gkdZB6dOEXtr7cxYaqqdWAFl2_GIjYRvLqLlpQFKlcBLZn8dJvZ0dA69v1_G55GbWHotisUbDFHtFanEkM67JBFflC6rpxUqWoDDa1rKf2UdSQUinUCdGgAbi-O1kB7nALUH5ksC8Gtq-9x_rZVP0iyUpddBuf3RC72MZybbyZYDEjSNZ-kloGflJpEiWsIHHiijqfDOWBQwjlnoDwmqxwp7dEIeuLPLpV4-x6hshS4Oz9bJ4rqbWlHdPMN5wtd6s0eFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=KOZgcHOpQp1janCRVFmE5Nxl52E9aE9hSnWuuHt5hqcD446tgsf-Pp8UoSXUFDbNfAB1CgZsy24-l4cn4FxfQxXfUon7mgUzoKLS3-fYi_YKyjh9P8Ln07KoxlyaVxvPSONZlVpcpGSD2loZqrCD-vAN-uuFvmU475Wrlx6YAjJiiiQxfMPWxhB7yyX3cIsyCbHyoY1yUCW2OnRtJyf_ykmNoMLl9LbMe3VxERkC9RXCc4-VM94_lkTuAtkSsx7XhvFkvJ9Ilh4EO9XEIOTTipbnnp3NiGNUEr9aJVRvLAadHKXApyekVMp14NCuGUEV3B9itd9agWP9QKuTvInZaq5WM9_2CrsB1LBuQaaG7rqm3MiyMUqpNCD0KLrRwUqnPN1R0D8rUYJrvDjl_aZAkQmSQ2qtC81xP3Riu2gkdZB6dOEXtr7cxYaqqdWAFl2_GIjYRvLqLlpQFKlcBLZn8dJvZ0dA69v1_G55GbWHotisUbDFHtFanEkM67JBFflC6rpxUqWoDDa1rKf2UdSQUinUCdGgAbi-O1kB7nALUH5ksC8Gtq-9x_rZVP0iyUpddBuf3RC72MZybbyZYDEjSNZ-kloGflJpEiWsIHHiijqfDOWBQwjlnoDwmqxwp7dEIeuLPLpV4-x6hshS4Oz9bJ4rqbWlHdPMN5wtd6s0eFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=qmFo3scwc71wqM2txzBLrcRbJlApWbStz4dNsk4Sac_xaWim3A45Z-XDUpKwBqnDGDup3BQFnpLVuw8VPRPc5rUh2WAQPcRTlDp1ntpjwE90bUyzvB3rSKYqKOoejZmhmN0PHVCKs32ZmMlf-ZuJVwxuvE32_-6CRygHRIgGmbl-gx0tKzOMhMzMi7-wCgoS9XQkxfX97SwOgxl6JRAAfVO1z7oA3NvWDzcejfj3z8psvEbu9_XC5JWkTeMeZXrxMYQEcURJbt_bukRITM5855WnBbm7x9cqAyse2f3_ocW_snQYtcwFCPZzAuqFJyNUHUJNgHJfc7NlIn_23NyelQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=qmFo3scwc71wqM2txzBLrcRbJlApWbStz4dNsk4Sac_xaWim3A45Z-XDUpKwBqnDGDup3BQFnpLVuw8VPRPc5rUh2WAQPcRTlDp1ntpjwE90bUyzvB3rSKYqKOoejZmhmN0PHVCKs32ZmMlf-ZuJVwxuvE32_-6CRygHRIgGmbl-gx0tKzOMhMzMi7-wCgoS9XQkxfX97SwOgxl6JRAAfVO1z7oA3NvWDzcejfj3z8psvEbu9_XC5JWkTeMeZXrxMYQEcURJbt_bukRITM5855WnBbm7x9cqAyse2f3_ocW_snQYtcwFCPZzAuqFJyNUHUJNgHJfc7NlIn_23NyelQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XWi2iawMMrGQer4FcTB3QCtVPgyavb_MKVio1UF3eH0t1GZT_E6HZeZfSXx0iVzqsp7D-sR3m99aMaEXCIJ88xJ4vNpSXptk9EiKf6pGjm0N3fUGh6p7zvNokdzmzkq5Zx7KEvwuCDp1JJ6o5FXifJLVmS6X3jL_hrZunYSGUJ6J5k78kg8ZtfdzHdHpPLcBUk7u2HD7mtwECTedxrd8vqKdhT_3eDXhqCprj3qmVmBlDuQqI7BR60T0d0XVl1J8n2eYx7Scq8BjPwqnlTjAGm_D5D-VDiEJHvHARjEjPntwjTjfq7tY1PffTNtDi7wTlIboRF9wlu3gcUFBYcFGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XWi2iawMMrGQer4FcTB3QCtVPgyavb_MKVio1UF3eH0t1GZT_E6HZeZfSXx0iVzqsp7D-sR3m99aMaEXCIJ88xJ4vNpSXptk9EiKf6pGjm0N3fUGh6p7zvNokdzmzkq5Zx7KEvwuCDp1JJ6o5FXifJLVmS6X3jL_hrZunYSGUJ6J5k78kg8ZtfdzHdHpPLcBUk7u2HD7mtwECTedxrd8vqKdhT_3eDXhqCprj3qmVmBlDuQqI7BR60T0d0XVl1J8n2eYx7Scq8BjPwqnlTjAGm_D5D-VDiEJHvHARjEjPntwjTjfq7tY1PffTNtDi7wTlIboRF9wlu3gcUFBYcFGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po0Cdn4oHdFbbP27NRffqE-_WdKXTSxW6U-kssF4D0O1cpaVpwSLzCv6k5bdQn4Tthfv6s0dVdTXwF-ndw7bb-bu5XIpR6ghFfyQrpUtdhDUWo-8ppU5GDg_GhEFDbR_j-grjMR7-ujFkQySWBpacy3g9L19AIveVXxv8DZBVNCnq22QO2YFh454Vnzw7Jm2ngC-WXZQobMZhoChW2C-TePmRoPmpT-YU2YSzwZRTyKk2smLbR15Y4VQ5Te3WjlsYQZ9B2uJuR_pHQkgkQKVn1dDl5c1Pk877aP2Y4ut5Gd2kv3lGMWtxLDVG3jx1L8Z2e7OPcXdlSPc1EXspfMuqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3Nw58WW9slg4PvnFwGmwohH4NC08Anbpz3JaN7wO3jJnlVEwELJJLPtikxSoySEDyRylb6keD7jt_aXES3HuHajGScBuCdZxxT7aBnHnHf7nj0j6pvyProfumE6_hTmcLwHnJCpjHpx7hfgTfbNOUvaLTk9hJ7qUGw3KKHd29R5V0V21oiXe9lEnocwAffBLxJ1BqLOPJttpJw3i1HnrFbEMJMwkpL5aXT1SyYaDh2HeD3IRykuHjAAihDMzkqeRbYaNrTE8kb1fzxuGrOra2q25_zXgeSGj8XQWhoDezkjhdVzMZ_b7w9mdP0RQhOKYbBmtcMlBe6wtzNdYNIMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=KKfe7eVcgOla_x6iMCOAV0ujHj9VCa0SELGh6X0YflXIU3YKv4MtK_7PFuLUDitdTTA_kTu3doiXNOWfqGU_ZR1kW5xNV53_u8juvr4bfacUs5P6xIxJo72HIR6XQqPFIe6R_F5LtWPK0bLPv2WsB_uu_79x_u5SQxYxlmG1iSU6APOvI2hLTON74m0CJQyFJVI6whC9SirlKew3ZfUJTPzHK1QilLfbkqQuB-u-9HmvfYrvnOyNdkryaGNq8WNaTm3AmnlG5vbChdjcaOXzxpPjQEVrXuaz19f3PF_41-352eB1W8BSg5DHcgtWtwUGWIVe6WHO9zONrjysFf1k2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=KKfe7eVcgOla_x6iMCOAV0ujHj9VCa0SELGh6X0YflXIU3YKv4MtK_7PFuLUDitdTTA_kTu3doiXNOWfqGU_ZR1kW5xNV53_u8juvr4bfacUs5P6xIxJo72HIR6XQqPFIe6R_F5LtWPK0bLPv2WsB_uu_79x_u5SQxYxlmG1iSU6APOvI2hLTON74m0CJQyFJVI6whC9SirlKew3ZfUJTPzHK1QilLfbkqQuB-u-9HmvfYrvnOyNdkryaGNq8WNaTm3AmnlG5vbChdjcaOXzxpPjQEVrXuaz19f3PF_41-352eB1W8BSg5DHcgtWtwUGWIVe6WHO9zONrjysFf1k2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=FBba-p1Iy8UbZzOx0-jL50vBatmkc5pkQQYxpncurVimG6zI_Vepbra0kCEi0drDsEXC4AWVZNo_E05bkJvVQhqjgWoT-GAWkPNV-pPWs7V2PI3qW4xa0yeopODFddWvNsipdmuFhpVGrWuVludjDrtDpYys9qWNuxV4ag6dbaU2sTTRPJpGOLo3iFgYsmJZwbHBWpYKN5Cjec9-o0CpU0-L9DExhKD5QdGL2gaTGbUvUd3CV2WZaqtznTNfpbQPdCln_EgL1c1zPyN8-aMtn_t_cdXJV66aH0WCvH-CMGRp_GR4G3wBfLzwUFgI1R6Tdce3LNjSQNQogAQ2TIXkhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=FBba-p1Iy8UbZzOx0-jL50vBatmkc5pkQQYxpncurVimG6zI_Vepbra0kCEi0drDsEXC4AWVZNo_E05bkJvVQhqjgWoT-GAWkPNV-pPWs7V2PI3qW4xa0yeopODFddWvNsipdmuFhpVGrWuVludjDrtDpYys9qWNuxV4ag6dbaU2sTTRPJpGOLo3iFgYsmJZwbHBWpYKN5Cjec9-o0CpU0-L9DExhKD5QdGL2gaTGbUvUd3CV2WZaqtznTNfpbQPdCln_EgL1c1zPyN8-aMtn_t_cdXJV66aH0WCvH-CMGRp_GR4G3wBfLzwUFgI1R6Tdce3LNjSQNQogAQ2TIXkhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=F6MJMNDu-aOdXrFnseqlYIShJm8wglwDEEtJe9zdciZyQJiB_go7d6Svr-N_urxzu8Xue41GSU3tKFhoU7-sQWqEdTQDjDzq8qOkCg2KPNByqNzXAi1LjVijX1xYzxmqHFX7w8Efy2whX_nJGAT_8TxLkyPR3CfDZe5XwKiB5JDJvcdqhjGcImotmxZcOVT0kediKqFulrXhlOOsitvX4GKG9fgwYnG0k7AmjK3v1BgI4eWqkbt0w_kVerIedU9UFO85VsXlMSDFD2n4u9q52OXj9PvdCSCiudDqidL_1GnisHm6PGOTPgWbM7t6n1dk_A6my_wGd5JJDr_9kWGEow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=F6MJMNDu-aOdXrFnseqlYIShJm8wglwDEEtJe9zdciZyQJiB_go7d6Svr-N_urxzu8Xue41GSU3tKFhoU7-sQWqEdTQDjDzq8qOkCg2KPNByqNzXAi1LjVijX1xYzxmqHFX7w8Efy2whX_nJGAT_8TxLkyPR3CfDZe5XwKiB5JDJvcdqhjGcImotmxZcOVT0kediKqFulrXhlOOsitvX4GKG9fgwYnG0k7AmjK3v1BgI4eWqkbt0w_kVerIedU9UFO85VsXlMSDFD2n4u9q52OXj9PvdCSCiudDqidL_1GnisHm6PGOTPgWbM7t6n1dk_A6my_wGd5JJDr_9kWGEow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCncYqLTWeThVTrId4nLQOnDUgpVGkssJXClX625OzL_Zf5LEs39v1rvt8XUAFgqyrKe5kWQCOkgj9L1693XDrKJc9U6BA1UUIYAPCFlExndRpSgu-CP-_kVWFB37-qpWVZmME_X8ngwZSPsfsINu9PHpTeFkIlRxdW7zgIqCauSwi9gzrq3FOz3IYXXDgXGDHEIrcn7BgTPurtVcxyR2noUUIpLJdGx_UTgHqGkO1LV9iFmuSaCs7T5vlTKLrZ-PaD0daecLkkoLB-DClf6nQThcKStN5l_sn6ecHqaFmFrO4sFn1kodQE1ucWVj756TURTIbO7ieyu1bZNNrKrVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=nGSkGBGkcIi2EoscDpTAuCnGMlrBu6tNIVgNwPYuq-uZBcXwCL7066-nPuOzPV8BVj97_5OqOhKvYIa5bawhOfvZeVQX_65rqqB2aGK0ByDWt9O1VRdiHDXPJA5v7umpQY7h1mhB-lle_rt0ja76vywjmC4zOFdxi7PkALOMRcW163TS6v4M7MeqftuH0s9tPiP6C1Yreepm9Y0Cwzm8Fouyy9CMmEN566lsrLZ2DnBagjEDKjywgsBat7euRFZaQXdF3FlkATt3uuxcqkZUJhSqSIxEjhxcQb8uF1GogoOenLpXoAhaX_txBFUGK0dbd0-bwj0vbTTw584A542iFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=nGSkGBGkcIi2EoscDpTAuCnGMlrBu6tNIVgNwPYuq-uZBcXwCL7066-nPuOzPV8BVj97_5OqOhKvYIa5bawhOfvZeVQX_65rqqB2aGK0ByDWt9O1VRdiHDXPJA5v7umpQY7h1mhB-lle_rt0ja76vywjmC4zOFdxi7PkALOMRcW163TS6v4M7MeqftuH0s9tPiP6C1Yreepm9Y0Cwzm8Fouyy9CMmEN566lsrLZ2DnBagjEDKjywgsBat7euRFZaQXdF3FlkATt3uuxcqkZUJhSqSIxEjhxcQb8uF1GogoOenLpXoAhaX_txBFUGK0dbd0-bwj0vbTTw584A542iFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=k3HwIrf5RfQn0bN06M8CzKSFE9LFCUSSF5JTCpaBiUcnUwmHxD-rwENjg1SQtTeqCtOym-6o7SiwfZyuJatZf9Em1eGt_hoKtiKmTCYEONzz7Da8Q9DAwh3V9UsvlwX6zKGqUcsg1dITSg7jbwbVdQLJntEfuyETPOoD-HyUcAuo6mxTBW-emisWSE1831tephjSJ4jFGSZzefNiZdtsByyk76ySESaFRL23v3fETaPT7bsG7rWzX6Xy35gLwStw9ZDvKvKEVokM_r8NCKxsR1D54vK_GYopKWuyvqP3zOwZfXOM6FtU_T9-ae4z9dSmZK59pHWkr7tFKjzioX1rSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=k3HwIrf5RfQn0bN06M8CzKSFE9LFCUSSF5JTCpaBiUcnUwmHxD-rwENjg1SQtTeqCtOym-6o7SiwfZyuJatZf9Em1eGt_hoKtiKmTCYEONzz7Da8Q9DAwh3V9UsvlwX6zKGqUcsg1dITSg7jbwbVdQLJntEfuyETPOoD-HyUcAuo6mxTBW-emisWSE1831tephjSJ4jFGSZzefNiZdtsByyk76ySESaFRL23v3fETaPT7bsG7rWzX6Xy35gLwStw9ZDvKvKEVokM_r8NCKxsR1D54vK_GYopKWuyvqP3zOwZfXOM6FtU_T9-ae4z9dSmZK59pHWkr7tFKjzioX1rSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=obymCKkzyK5xnQEqed4Vu0dM8LB4EUZp-pQiJI2JCb2Fzx6dy0bL3iYKwXTgwPTwgpNZTMF0EGLPibLcQmaSzQpnRNPFUHaZHGmaxsaFRZa92ut9r_rBK4pv2gW3Hrf96mcA7Fhqdh7iM12t3Y9Yqc4NFikwvo3drFS1Zzp5WRjzdzirF0etCL3ZDm29pCtsDdJ_bClNWHlrMQ204R5QKaNtCBA2OsPRe2RExDGDHRIUivfKkRO1H5yYuWPJLz-eHoTArNs0ok_HEhpj80q9ot6C2tVL-FA462qtDAU16fS07eKK8vvXjAl2Li4y9LgSJmEnX54-V3xtoMOC6f3A6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=obymCKkzyK5xnQEqed4Vu0dM8LB4EUZp-pQiJI2JCb2Fzx6dy0bL3iYKwXTgwPTwgpNZTMF0EGLPibLcQmaSzQpnRNPFUHaZHGmaxsaFRZa92ut9r_rBK4pv2gW3Hrf96mcA7Fhqdh7iM12t3Y9Yqc4NFikwvo3drFS1Zzp5WRjzdzirF0etCL3ZDm29pCtsDdJ_bClNWHlrMQ204R5QKaNtCBA2OsPRe2RExDGDHRIUivfKkRO1H5yYuWPJLz-eHoTArNs0ok_HEhpj80q9ot6C2tVL-FA462qtDAU16fS07eKK8vvXjAl2Li4y9LgSJmEnX54-V3xtoMOC6f3A6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=hZ4s6jk9nHq_wkvXYyHRrxIPflOPLhn505ZDHjtEtgfYnvsQNGEbX9Eeg4OoNWr2bmeZlloOpwfuzGjrB1btkcip3zt5tUo8L4U0ryzgjW8ot2SDYgGJdRsaLmalEjJkLnQxXSuiGbo02EXhBe0jj4yKndvvkN5EkjfIET5DHvFLowY4_9xEOaaojXaVsz_rTh-5we3aB9mlVlrwlnWujuu8iHsq6qC9LDP2t8ePcYcuSRQ4sUkZy0CfV63-YgoLMSLjVeUWtNZWmNahC-lonpPQWCaS4D2YZ85gJp3-qOYJAu7faByRcD2oCGp_lwXsmr5oaHH6Q9YTg0Nm0DLO5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=hZ4s6jk9nHq_wkvXYyHRrxIPflOPLhn505ZDHjtEtgfYnvsQNGEbX9Eeg4OoNWr2bmeZlloOpwfuzGjrB1btkcip3zt5tUo8L4U0ryzgjW8ot2SDYgGJdRsaLmalEjJkLnQxXSuiGbo02EXhBe0jj4yKndvvkN5EkjfIET5DHvFLowY4_9xEOaaojXaVsz_rTh-5we3aB9mlVlrwlnWujuu8iHsq6qC9LDP2t8ePcYcuSRQ4sUkZy0CfV63-YgoLMSLjVeUWtNZWmNahC-lonpPQWCaS4D2YZ85gJp3-qOYJAu7faByRcD2oCGp_lwXsmr5oaHH6Q9YTg0Nm0DLO5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=R_xh2_yHm47Jlw1y71YYssHubNIY9--8Pymyy0fa76mdhkqb5aWz_pM3Z_AWVe6FhMEPtsgvDJnoZf9sgvq5gToUNcWjo9dDOuVumPK7NUfjlBUa3c0ZMJtNuqEpv4bTP7tSNO-A8_C1QLcrkQW1k4C1GhIX_767zV8Nuizc1v67hm3nNuHDo6o6fTzeapQwKhw3y1_o26obhQoabjwFJ746BW3BV5MeDWTuCmI1MPRHH638rL2beWm1dto84wJwH2mKENAM8qjsXnuEEZXaUOBl_ToFav3PhVCQ93LcrZ55VQJ3eCGaoZ0Zd5eH_n3bW55rauzTguhVScQI-KyI3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=R_xh2_yHm47Jlw1y71YYssHubNIY9--8Pymyy0fa76mdhkqb5aWz_pM3Z_AWVe6FhMEPtsgvDJnoZf9sgvq5gToUNcWjo9dDOuVumPK7NUfjlBUa3c0ZMJtNuqEpv4bTP7tSNO-A8_C1QLcrkQW1k4C1GhIX_767zV8Nuizc1v67hm3nNuHDo6o6fTzeapQwKhw3y1_o26obhQoabjwFJ746BW3BV5MeDWTuCmI1MPRHH638rL2beWm1dto84wJwH2mKENAM8qjsXnuEEZXaUOBl_ToFav3PhVCQ93LcrZ55VQJ3eCGaoZ0Zd5eH_n3bW55rauzTguhVScQI-KyI3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=fR36E-XT2uEbwjs4JuolGzysHeqeuNfqL87WTqVWF7OUG4yra6qyoZTo18HZ68kHuNMW70dcLehVMqjhCvU4r8uc_3k7_OCq_YEdWY8IWgx7JVAloRqrN66B4-DQMbkPkoUFeYXyzD5_snQnCIWDVUh6avr-pVPrcr0qsrPx9oHxstSH3iBS4cTrl_-VHOORqWpQFAb5XhM7JcPIuP22DemxnmHt5aj_NwAxltzrhYe2y7M3u6KBYLJNhTIWe4L4QmvX3KRdRCzK4z6YnuCSO-bgjArLZ8-AXm93U-pC1RCOC5Mg3s1uLSus7ctifmmkjCIaz_JCoE0nW_KI9HSAPa90r_iDIQsnYPQ4Vf65ZvOUeuHKXX9CyYFl6M7JsTma0SXtc_7ietKe9-eksHJQajYpuk3HLKqsjM6V6urc7N9Bt-ItOJkFpDexHiwT2S1UdAf_VpkkfusNtZcwTpOHimSnwarWxu4M7ZU1enh0o3bzwE1t27zON7cPJDCW0cyEPtfdg9pV04br3Gd5uELbl3w8n2hMoPjIozcYPkR4QupCe_TFQQIAB4a8dpYOg_6UrBL_zq0l0HH3sinURJlqIF4xrUW6Yxd9u_a2R1wGRgxhlHvJV8NqGMdW7OorTAw_BxJEboP6d3LDpwEYh-eeMd4lKSra5vlUgj2UkT99J0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=fR36E-XT2uEbwjs4JuolGzysHeqeuNfqL87WTqVWF7OUG4yra6qyoZTo18HZ68kHuNMW70dcLehVMqjhCvU4r8uc_3k7_OCq_YEdWY8IWgx7JVAloRqrN66B4-DQMbkPkoUFeYXyzD5_snQnCIWDVUh6avr-pVPrcr0qsrPx9oHxstSH3iBS4cTrl_-VHOORqWpQFAb5XhM7JcPIuP22DemxnmHt5aj_NwAxltzrhYe2y7M3u6KBYLJNhTIWe4L4QmvX3KRdRCzK4z6YnuCSO-bgjArLZ8-AXm93U-pC1RCOC5Mg3s1uLSus7ctifmmkjCIaz_JCoE0nW_KI9HSAPa90r_iDIQsnYPQ4Vf65ZvOUeuHKXX9CyYFl6M7JsTma0SXtc_7ietKe9-eksHJQajYpuk3HLKqsjM6V6urc7N9Bt-ItOJkFpDexHiwT2S1UdAf_VpkkfusNtZcwTpOHimSnwarWxu4M7ZU1enh0o3bzwE1t27zON7cPJDCW0cyEPtfdg9pV04br3Gd5uELbl3w8n2hMoPjIozcYPkR4QupCe_TFQQIAB4a8dpYOg_6UrBL_zq0l0HH3sinURJlqIF4xrUW6Yxd9u_a2R1wGRgxhlHvJV8NqGMdW7OorTAw_BxJEboP6d3LDpwEYh-eeMd4lKSra5vlUgj2UkT99J0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD0HmCuDTXNyYEGP-rNFhym4DEMNw0nx9FAb0d-yjJjd1L5YCqjluSahKVWgzI2lk9I8JMO0Ay3hraK4u29ZyhRxp76DPNT7oPN1wipXXPmyl4q_dsiXI-CLzZetP2T-Udl-Pmi4C-1u1dkahO8M_19XNrTUawRrlpIKut1hSulX86LIOk3-OFtYxrQaKgqLEeHhb_FGiqSMRIyv1M_JFVkmmISIeFZPqyWJBCouArBwk-aGYEddfJo3yrB9yxhriSHuj4WzetUwa_HZkC4AhnSi1onqzT58s1AWz07aCnOkFP_IyaRzJfQ2E_QY0Oe0IdSPAkqAWvCADGDNoyhikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BQFA-O8ublnAtbw6hgu0e8Zqaw6EGwJOxAf_M_6PGJq7eDi1l13CsPsajWaRU70C4aTQ456tPuR1PDW-szlE_Sn8Ym5rmhBvWwTOrt6Y3dvRzv1p3IgzdQ0tvxXIzhV6voSeVE_zslFz7hLAxy4d0bzqcIpaABqS6GtCFJ0Z5WVaL2thUbhSLpnzCQpJYzZYEkFOB8wtRHOJEAbpyAaBcHedbUxFmP7In8MPk4fTYOJQofySRn6nHDxRKoqK1e8F5iiG_kLS8BBAbLlpkFGh8Z_OspkDDxQnsPj2Ja1pO1toqicv8uCpyPfE8t6lOJ9qvrvuRBs_0Y5NPsCstL1ZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfs0usi5WgXo3EpY3PWTsPczzJtqF0YIVVxd0D2iOsTNgjOGcjdcpK5TqyYEYdmtZgrwa4tOgn4RNb8JValAufe8iNCW--UnBitFsRrye5X9YuJHmxufMQzm_Vx6kyo_h9fadRvXdHSZLMJ-ofjy0D0EOQEeGnEmNQvPnZtYfLa5WZ5PiTG1LhIQVr4842LrXqQjrK1wAx1GgD0-J55w_1-ig4EYo5SGE6OwnKE1nJAC_Q-OeTRcq7kc-8jjxJ8-udDepMYyFXOF8TKkhsvwzoxRuviBQOyKZAmZK1fleeDsxAZeLjw_1AFh4n6fn70UaVP9KsYRNBytKSlbKg_cIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=tbXNbnoUw_Y1AoqJ2myRAQG8GfTCYb5DEe0SrTJoZerNx0neEDF_vN3dCitnJG7U6NdC-LwWo4U-wu3PSinCo1scxfGQCwmlo9UaFxlh3HBbgvfKxhc1L5MVKrtacpsfJfTNYEwmMijiJmYv0EOpReRODYbKmaIx309xXtY9Ab3JxRfEcNJeMwo3o9cyt2vj7-hT-CEArkog8eufRsRqk__W__n9C5RRh1kG2bNzypO1fm69JwzpDDazL-favB-K7SqpHsQ4yJN_GICPVVIKvRb2BvBRQ41J4UQNnO5ml6f_Yn0cemjuvpJi5yMKvWN0PrfyFwAmx1Gx1zE9I71BfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=tbXNbnoUw_Y1AoqJ2myRAQG8GfTCYb5DEe0SrTJoZerNx0neEDF_vN3dCitnJG7U6NdC-LwWo4U-wu3PSinCo1scxfGQCwmlo9UaFxlh3HBbgvfKxhc1L5MVKrtacpsfJfTNYEwmMijiJmYv0EOpReRODYbKmaIx309xXtY9Ab3JxRfEcNJeMwo3o9cyt2vj7-hT-CEArkog8eufRsRqk__W__n9C5RRh1kG2bNzypO1fm69JwzpDDazL-favB-K7SqpHsQ4yJN_GICPVVIKvRb2BvBRQ41J4UQNnO5ml6f_Yn0cemjuvpJi5yMKvWN0PrfyFwAmx1Gx1zE9I71BfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=afji9x3hNaaU8_ToLplsfaLQupeDOaygeEbHPUSdOrZX7KbhnqG96NUUcsNrf6SLvTYNU5scahTsXMPE_bwyNU1PU1PfNYwvCeOJ2hs4IZyolfWGxiwgLv4iM7HyQo_bZpMK3LnmUqtPgjFfNCdGbIdz0n9RAg9-00c4Ehrvc2b4M2phJZ0QMK08-AvEXjPxN9qk0Q1gb7pNq2kjr73JqeJhRnWdHHMY5zJwdgb-qMTUZiw5WkdOqgQ37wIQcuKjw4eMCuuCHpr4_rHqV2eRhWspuVfvFLtGMEAqnTQREHPyr3b4gwqHCZulzHlxYe5jMtiXO5G7Dd6o3h8zm46Z2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=afji9x3hNaaU8_ToLplsfaLQupeDOaygeEbHPUSdOrZX7KbhnqG96NUUcsNrf6SLvTYNU5scahTsXMPE_bwyNU1PU1PfNYwvCeOJ2hs4IZyolfWGxiwgLv4iM7HyQo_bZpMK3LnmUqtPgjFfNCdGbIdz0n9RAg9-00c4Ehrvc2b4M2phJZ0QMK08-AvEXjPxN9qk0Q1gb7pNq2kjr73JqeJhRnWdHHMY5zJwdgb-qMTUZiw5WkdOqgQ37wIQcuKjw4eMCuuCHpr4_rHqV2eRhWspuVfvFLtGMEAqnTQREHPyr3b4gwqHCZulzHlxYe5jMtiXO5G7Dd6o3h8zm46Z2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=cfEAHGtDc43UrZbFD73DRL0MFLmVms1jD3k5JGPUJSN_PFT6W1KDFazob9TKr3L9PW8XnxGYZOLoM1qNw5Io3tzp147uqP5XLSWE4cr_JCALHEJqcPM-qSqDEwG_banEwI9oceQKBgBGa5eURrDmRPD_3yeSpwaSP1JiMvafc_SGrKab4aSv8rF8RiWKVHj23Vpj11ICB7COLIdzA4JAC349-1DAFcCCWWdqdq2p8qotW9L2BoNw1RE15ixXUeuU6nRHCM-OwSIYlVBuqz49hz-Z4YU8jg3pIBjGgYPlB-AFs1PSYOBdluRzvSrxElVwg3AbatTJGjQg45hfP6dd9jiOxDQuZQVxLnkkLIboSvfEfH5d66s62v9ZtVb9SNZ39DJQDXXEIHzREJQ1M0vzCJnkNK0pbv1WbzHS3nZGHTDsEjA4omPltWfWuMK4Pefgt6tZ13dIGp5PhGEJkVrjAmmR6HZeOHsC6gQ__UrR7NFrMtKEQJXfnHPt0iOeLF7eecqRefroaM18Xd9Afujn6Kxfr2vdp57VkfOKnqAYXpj_oPM9YOki0w5AFFLw_G8RARWe2PwBYblNMtUbgisAlwF5Lo2Z-QLAMnU-r_W1ru8AZLZPC66ZLqcdoZcsfOTR6F2SUuHILQjYZmUslDqu1QEm5uLn2UImnWt9mCeTwC8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=cfEAHGtDc43UrZbFD73DRL0MFLmVms1jD3k5JGPUJSN_PFT6W1KDFazob9TKr3L9PW8XnxGYZOLoM1qNw5Io3tzp147uqP5XLSWE4cr_JCALHEJqcPM-qSqDEwG_banEwI9oceQKBgBGa5eURrDmRPD_3yeSpwaSP1JiMvafc_SGrKab4aSv8rF8RiWKVHj23Vpj11ICB7COLIdzA4JAC349-1DAFcCCWWdqdq2p8qotW9L2BoNw1RE15ixXUeuU6nRHCM-OwSIYlVBuqz49hz-Z4YU8jg3pIBjGgYPlB-AFs1PSYOBdluRzvSrxElVwg3AbatTJGjQg45hfP6dd9jiOxDQuZQVxLnkkLIboSvfEfH5d66s62v9ZtVb9SNZ39DJQDXXEIHzREJQ1M0vzCJnkNK0pbv1WbzHS3nZGHTDsEjA4omPltWfWuMK4Pefgt6tZ13dIGp5PhGEJkVrjAmmR6HZeOHsC6gQ__UrR7NFrMtKEQJXfnHPt0iOeLF7eecqRefroaM18Xd9Afujn6Kxfr2vdp57VkfOKnqAYXpj_oPM9YOki0w5AFFLw_G8RARWe2PwBYblNMtUbgisAlwF5Lo2Z-QLAMnU-r_W1ru8AZLZPC66ZLqcdoZcsfOTR6F2SUuHILQjYZmUslDqu1QEm5uLn2UImnWt9mCeTwC8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDfQxs7fXRac9D-hr5Zpa2B6TR0TdioWAeF2cpmswo7b6rgwgWQ9wcrR5UA4y_6Wh7PxMIab8LLFVUWehbUNOsxvQVrpjqFSeRnf4kHn23i-6BrzG3S17IZYlcIvLncRKarMUhqJigL8nEz9JDn2l7lSk27o1VYupbbtjiXeWSRJAfy1FZcmPHFG-0ICtp2Y2KOEMcA-PFTQ5taXvMV5271fm9XVDBcbVUnneyZGwC0thaFh986x0g9RB9q8OVNzMLUyQyAk1wrLHmgynqOSyPwMocKc5mWwOrevr_61L9rvc5akRIvHLgNUTFY_jOlAaIYVgAF_P3tb-NbJTEGVVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=riLE-hMq8rYV4Rs2pAF96YE7E0U5_HQp028fdxoLuAjyXRHLvYVdTX9HyPmR76iH5Ds4zAs4rdP3BSucT0abLCqPFOuwMnU9GzJkrvYp78-r0CAw5Vm0HT0pWs5AugHxXtPQL8GsZIJ-ahq42AD3j0ovk0rRvj_Ay2c8-Zy69aHMfLXeRTzPHSgtpkMNa_NkrerjJ8ooWvw0aAOaLHwS0H5jz2wMFPCWIE-eXlh-KLUJtEjmGPCwMQWMBloAoLO1g-ZUx_nHwkH-LdTqSBmM9jYQU7gC1EtB6JYRDd4gUj-Ms7vuY3-2aiRwFuu-Vb18bSHkWW69rzHqCP1WJGcp_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=riLE-hMq8rYV4Rs2pAF96YE7E0U5_HQp028fdxoLuAjyXRHLvYVdTX9HyPmR76iH5Ds4zAs4rdP3BSucT0abLCqPFOuwMnU9GzJkrvYp78-r0CAw5Vm0HT0pWs5AugHxXtPQL8GsZIJ-ahq42AD3j0ovk0rRvj_Ay2c8-Zy69aHMfLXeRTzPHSgtpkMNa_NkrerjJ8ooWvw0aAOaLHwS0H5jz2wMFPCWIE-eXlh-KLUJtEjmGPCwMQWMBloAoLO1g-ZUx_nHwkH-LdTqSBmM9jYQU7gC1EtB6JYRDd4gUj-Ms7vuY3-2aiRwFuu-Vb18bSHkWW69rzHqCP1WJGcp_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=FU-gBYryrSkeuTWVqmqw7cSicBz0F3BC9wkkYGakamWVSDGVowXx22xFi7Fsep19_SzE3L7PKCuYMZInq-1sX1_3GKYeYaoQLHjZxsokvBbz6u9KaeQ2ZoucNVv5AzP4tOwvvWCQBlFnNbi5wmUFh5ww5cBwTt4Nm59P_zTckgtK8ht9ndFoSdj114S74jr6dr9iooiONhNwdl3R68LfUwgrasUFv9bEpw0b1TfmQhsgfWYvvs6CtaTi5jP0r99tZcedptqDy9yXN6r2Zg6QaAGhY0vPh6S6bO_j0ACpPs_6Z10UzOrJASx59Sa4G2t7J8-D0C8fEvgIMOllD4K1YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=FU-gBYryrSkeuTWVqmqw7cSicBz0F3BC9wkkYGakamWVSDGVowXx22xFi7Fsep19_SzE3L7PKCuYMZInq-1sX1_3GKYeYaoQLHjZxsokvBbz6u9KaeQ2ZoucNVv5AzP4tOwvvWCQBlFnNbi5wmUFh5ww5cBwTt4Nm59P_zTckgtK8ht9ndFoSdj114S74jr6dr9iooiONhNwdl3R68LfUwgrasUFv9bEpw0b1TfmQhsgfWYvvs6CtaTi5jP0r99tZcedptqDy9yXN6r2Zg6QaAGhY0vPh6S6bO_j0ACpPs_6Z10UzOrJASx59Sa4G2t7J8-D0C8fEvgIMOllD4K1YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=g8KcVDmkxlcAMbcukRxG8AmWbNDb9CCs11oj7fOGu9mtxhVexPbzjnNtFLPL_3RW9UdU4I_eriW-PeHSoDicXC5U_LvYe8qZ2PUNHEw1PIxMaZ9m5alS1IEj9NZgP8pZ2Ozu-_juB5-cZUWOUjolJ3FlIRkxEgAUeZHaAkBhH4JILqLctjgWcZSww-txDQ5tmQMB-qgmthYgD6M97X65gjI87AYOWUu5q4a60928hboAa9PmYk1Yf1kJqAJpPHyYpdOfCd3ns-uf_sKM4hYljhIf0G7vpu7nignWxjWAx0htIEwdmwZwJQek1AISz5DPn8rvODHYa6rEsIbtaZudDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=g8KcVDmkxlcAMbcukRxG8AmWbNDb9CCs11oj7fOGu9mtxhVexPbzjnNtFLPL_3RW9UdU4I_eriW-PeHSoDicXC5U_LvYe8qZ2PUNHEw1PIxMaZ9m5alS1IEj9NZgP8pZ2Ozu-_juB5-cZUWOUjolJ3FlIRkxEgAUeZHaAkBhH4JILqLctjgWcZSww-txDQ5tmQMB-qgmthYgD6M97X65gjI87AYOWUu5q4a60928hboAa9PmYk1Yf1kJqAJpPHyYpdOfCd3ns-uf_sKM4hYljhIf0G7vpu7nignWxjWAx0htIEwdmwZwJQek1AISz5DPn8rvODHYa6rEsIbtaZudDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g15Zr3Ml0pNlTMRqXmoe_t2fhWeuzQz1pF29AAfxzvEn62M942dJyJ61EjCbWFBkLanqrWSi2G5-AAtxo9Y-Z-HStq0_nVRe2qIMs0eWB6G3XboN0pWADVZUyqMK5v6AgCYYhnMljMHBuEi9u7CMNsUcAh9negGL8PhlEU7O30jtDAkqwNBOXv70iU8WvvO2ZG7N9XFTu8EmjTvZIplFso7XjK9Ux92xPuKVUPji1RlwaOlTGrWJAT7XhUl5xdIcXqca7X64j-xmVO8PH7KRvXKMYHZtE0IUXQ1aq3wXC8w4QRBp7zbslNOpVDxH_qELeT5DwiElYQGROvI4FVezUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=jBdlbXHNvouuXmZfdqz-R1L4LVnyONnoP-mxd5ud0sj_zPlTrKPF8sfrDYOuc_PC5fFE3OjxO7EMYRxErOzsssYuVYDVcwOANWeUzvX-K42t94PYh-vUur9_AAsd5jdUDPxxbHppB7YEdIYF2CLHPEaLKnMLue-EDc9StqnWtbl4on4r0jNWsyCspNyRbV-oUhEWyelIzLHsrqomGVOUq0iKAGqkRWg6yUfLFC6RUg_Z77sWjUqkTxmuRZWQbHgOWIhZ6d_dLz054pRYQF5GoQo-BGqk3pFTmG8dDZLLYuiQomPc0dsgLQAilYmftD_G7ns8req33a95N2TIIUj0TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=jBdlbXHNvouuXmZfdqz-R1L4LVnyONnoP-mxd5ud0sj_zPlTrKPF8sfrDYOuc_PC5fFE3OjxO7EMYRxErOzsssYuVYDVcwOANWeUzvX-K42t94PYh-vUur9_AAsd5jdUDPxxbHppB7YEdIYF2CLHPEaLKnMLue-EDc9StqnWtbl4on4r0jNWsyCspNyRbV-oUhEWyelIzLHsrqomGVOUq0iKAGqkRWg6yUfLFC6RUg_Z77sWjUqkTxmuRZWQbHgOWIhZ6d_dLz054pRYQF5GoQo-BGqk3pFTmG8dDZLLYuiQomPc0dsgLQAilYmftD_G7ns8req33a95N2TIIUj0TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=Htk6uXz9B_g1sZ67j7bm0v7UMQx08zOWs9y53mwUif9yHM2SlSsNVrECLT15HKAcLmW73ZmxVT682p_A8L8ZBZSKNxyF_78LuCjqbL8254T1JFe_i9BQdkqbIdspqk11jC1nL90nedhbLJGkIQ59vmHAjxOsql7rUS77IExfwtMrTj8WryjzvAlCoZxH7eLtD_Zs8J1fdEw3KC3g6Bag4ZEdNd8XSO8FcSGQF1o2o8ActjNtNbfJrM77b02ah65ZaViImPupmK7xq5hSJEpUgymd9pBlghb62wL1daL4OWo8QJfEwSEhmLtNN7Aft-gGU2IpdLl6t2iMoOH_oc-eVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=Htk6uXz9B_g1sZ67j7bm0v7UMQx08zOWs9y53mwUif9yHM2SlSsNVrECLT15HKAcLmW73ZmxVT682p_A8L8ZBZSKNxyF_78LuCjqbL8254T1JFe_i9BQdkqbIdspqk11jC1nL90nedhbLJGkIQ59vmHAjxOsql7rUS77IExfwtMrTj8WryjzvAlCoZxH7eLtD_Zs8J1fdEw3KC3g6Bag4ZEdNd8XSO8FcSGQF1o2o8ActjNtNbfJrM77b02ah65ZaViImPupmK7xq5hSJEpUgymd9pBlghb62wL1daL4OWo8QJfEwSEhmLtNN7Aft-gGU2IpdLl6t2iMoOH_oc-eVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=LEzdaz5fD8Lv4IPKrNoUx-ECtz3i3FjM3S9Rl9GkJICefc-THrxXq_4x6pAKDnubt-SXnB0m6JaztlZYn0QXzRZyimj24qJGCpmA0EdPb4udFCioDDAdO7HeqhAFmTYFR5Lu9ma4CcbbsaqNgIl_PS7H6UMHiOIcEODxn92YkqGZTCEh1WuANZQ-LybT52SmLqKeg4DWOvByVo_pRXwCuboFNag9C4XTgAJ0FLSv21E2fMplkHtNqAqzD2iLgye5dHwoP9-gVA2O1Cn60d4mJZC4yyNZkHy1LKSGQlcvalnSFhmZFGAhNZk4eq4iwDUsVYTVfYKLcDvx5FkfuZrJWLws8-BH6EufxR53sDlDZgg4Z2etNRhwBVRPhvJIB8InxZJ6cE2UeuZ_rLzIyAzM3IAEhZCg-jwjn6AkjACgsCymRfhfLk1Rdr9HPQlQ8lSTn8pt7P7eC4lPBPnnDg_9V3voe-Nnaw_Eg-pCEFoHVV2YInfJLt1vo3X2lo7ma6spEGfUwCicCl93fKvVfJjl3SyO11hkjQIZfJMcJmfKIQPruGNRvMQViAT5GPhTqb7GcwrmJg3x3u10TyF-AlM26Ld05lnHu-_EFfCd_dQbmEZfBQhIZ694Kd417jTGQXIbe3b32Ckd-ZvYxlDkMngTpS-F_vMSow4rjJW9E9mXEh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=LEzdaz5fD8Lv4IPKrNoUx-ECtz3i3FjM3S9Rl9GkJICefc-THrxXq_4x6pAKDnubt-SXnB0m6JaztlZYn0QXzRZyimj24qJGCpmA0EdPb4udFCioDDAdO7HeqhAFmTYFR5Lu9ma4CcbbsaqNgIl_PS7H6UMHiOIcEODxn92YkqGZTCEh1WuANZQ-LybT52SmLqKeg4DWOvByVo_pRXwCuboFNag9C4XTgAJ0FLSv21E2fMplkHtNqAqzD2iLgye5dHwoP9-gVA2O1Cn60d4mJZC4yyNZkHy1LKSGQlcvalnSFhmZFGAhNZk4eq4iwDUsVYTVfYKLcDvx5FkfuZrJWLws8-BH6EufxR53sDlDZgg4Z2etNRhwBVRPhvJIB8InxZJ6cE2UeuZ_rLzIyAzM3IAEhZCg-jwjn6AkjACgsCymRfhfLk1Rdr9HPQlQ8lSTn8pt7P7eC4lPBPnnDg_9V3voe-Nnaw_Eg-pCEFoHVV2YInfJLt1vo3X2lo7ma6spEGfUwCicCl93fKvVfJjl3SyO11hkjQIZfJMcJmfKIQPruGNRvMQViAT5GPhTqb7GcwrmJg3x3u10TyF-AlM26Ld05lnHu-_EFfCd_dQbmEZfBQhIZ694Kd417jTGQXIbe3b32Ckd-ZvYxlDkMngTpS-F_vMSow4rjJW9E9mXEh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=hJii4VRA-RJ0i6Yl4NbG62oi6fO0yFEt8Jd3Y1jvbjiIxiTITrjs3avyT-CmBA2l9KEVth5HRumkACm6cl1MuZQlusvong4siQbb8WUUDE8VyQV5TfXiCEJyJZNbYPBlgjM8p-H6Q-eoAUO0hBST8RgCH_EtAsM9npyge30qtNdhGVDs2kBrFJBJV-e9l-7Z_O_d-OONu3vds2dfjBT6i18NNk18XKbytcqKFjTpxcHk6DWtzeJKFaHbO7oLKFWicARvJq0aqiUDG-gElKh8OHMTaxfEkS7vBBeLPcqpH7uxCFJ46qks8PA3YSQUyB7MWwFFRBGHDZGa1iv1-UXu-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=hJii4VRA-RJ0i6Yl4NbG62oi6fO0yFEt8Jd3Y1jvbjiIxiTITrjs3avyT-CmBA2l9KEVth5HRumkACm6cl1MuZQlusvong4siQbb8WUUDE8VyQV5TfXiCEJyJZNbYPBlgjM8p-H6Q-eoAUO0hBST8RgCH_EtAsM9npyge30qtNdhGVDs2kBrFJBJV-e9l-7Z_O_d-OONu3vds2dfjBT6i18NNk18XKbytcqKFjTpxcHk6DWtzeJKFaHbO7oLKFWicARvJq0aqiUDG-gElKh8OHMTaxfEkS7vBBeLPcqpH7uxCFJ46qks8PA3YSQUyB7MWwFFRBGHDZGa1iv1-UXu-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzZX6YHsTtkSEJ4S-O09yLfLmTNtY1Mnkl4OcsF56kdOB0JCkfllGo0kcSAbTn76EHcx-iz5Uk7Qhx-UbmADJGV0f_F0d6vpxcnCX3sUA7c4AJmizMY_yXxu9djMI0K-EoE5_Slmk0uKok-sq3TlZKQ_ONI9L6stu9DpQi-W8MRbWdU28w8aXFqd3KN-xglR_9pEiVLgvWmpkTfPAPo67hplDHoG4dNBD5RcN_0qOBfzXSSnRM5NqFRjzQSYpSxNT5rEnqh5xM5aeoaEwxNvoT3JbjxSiEgi-wHroSfwFKW4k_04DXne-OBaR1ljUhI53PsiAygPIK7LiZW2_gxEuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=lZHnA_3IhPsQBqrjs6o2Z37HfPh7TT_xmVp682jPSi-Io5pUd9X-maIEgIeXVi-AvAvJ2iSxfLyg06QdFqMn8N4IlMlWivpoC9m-dwYPuoVJ7S9kfQDDKzFWDUUs0nk0lWOmVEgK2bOdT-MnFmA_15sUSlOE0ZxZ14EHl2EtoDFVrs03LHt7Umh5ukg8agUz8pexfB4Ibi_BkAYmxwqFb8bef45DkX-gUTWajioMqW1JUdgZlyf8Q7po_n97ihNfJWYE-8SllMpjG-dPfUUQKQaXU_OZnzH4r4Yb9tSxM72ml6JbXCU_1ipSria418PQUe9g-5cpQ4V2G5QX7TGLtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=lZHnA_3IhPsQBqrjs6o2Z37HfPh7TT_xmVp682jPSi-Io5pUd9X-maIEgIeXVi-AvAvJ2iSxfLyg06QdFqMn8N4IlMlWivpoC9m-dwYPuoVJ7S9kfQDDKzFWDUUs0nk0lWOmVEgK2bOdT-MnFmA_15sUSlOE0ZxZ14EHl2EtoDFVrs03LHt7Umh5ukg8agUz8pexfB4Ibi_BkAYmxwqFb8bef45DkX-gUTWajioMqW1JUdgZlyf8Q7po_n97ihNfJWYE-8SllMpjG-dPfUUQKQaXU_OZnzH4r4Yb9tSxM72ml6JbXCU_1ipSria418PQUe9g-5cpQ4V2G5QX7TGLtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=Mx_cZx8dcLKxjws5RcFqbopi_2-5mjlGmNE-u2QRErCv2vnfNwKl60D5z4BMKQwluVnQBw7kozCPSm0rNlFMswKeK6nLgpgXTtpFNRGYtpifLj_xbUV8w4Euhy_lIn5pVld8qLpjdyNgaQBq0iIRJrlsVOHfYLN5R_t0OEAr1YQOeSAYuiFmmGl5TaExzk64gYRaBrnbXS_mXiQwTdxth1uFP0ND8AuDwZxlnse_4oUk4E7bsl3af_ePlBGqjA_nds24i-tY7TsYtej3wp2icjku22k2wcFFgkZnuox9GUlQXGG3BUJxCj8jU9ZI38b4jQhNn1zk11F3OokilcTsPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=Mx_cZx8dcLKxjws5RcFqbopi_2-5mjlGmNE-u2QRErCv2vnfNwKl60D5z4BMKQwluVnQBw7kozCPSm0rNlFMswKeK6nLgpgXTtpFNRGYtpifLj_xbUV8w4Euhy_lIn5pVld8qLpjdyNgaQBq0iIRJrlsVOHfYLN5R_t0OEAr1YQOeSAYuiFmmGl5TaExzk64gYRaBrnbXS_mXiQwTdxth1uFP0ND8AuDwZxlnse_4oUk4E7bsl3af_ePlBGqjA_nds24i-tY7TsYtej3wp2icjku22k2wcFFgkZnuox9GUlQXGG3BUJxCj8jU9ZI38b4jQhNn1zk11F3OokilcTsPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=o7TaZAUilZU-4pHajeJ1qkq56BAECghNaToIj4YsEJ4oBe10d7thubukN1YRwBTwG5Sxs4XslL0BG6F7uIM6uKNtJo0_5zl_lc6mK8dLRYz7M9pfaTB_aTdD1GM_84JWQPkgZxKZ3mj4Ls2HG7sXwVQEG-rpk5AW98pGVD8BrYoQZdXkE1ea8YLOdk-twtwAvNnCTd9WZdSeDe4mZnm21OAEt6QxCJQ7ohlMnEH-1kmaKGtsnMX5Jhkvki5-P5mxSV5Tk2XrF_S0XqWUm1wdY8i4n5ziCxTkE3AmUxUkVuceG5cCZGNNZaucSpHIqniZb6WF3E7VWVrZ9fuDW9B-7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=o7TaZAUilZU-4pHajeJ1qkq56BAECghNaToIj4YsEJ4oBe10d7thubukN1YRwBTwG5Sxs4XslL0BG6F7uIM6uKNtJo0_5zl_lc6mK8dLRYz7M9pfaTB_aTdD1GM_84JWQPkgZxKZ3mj4Ls2HG7sXwVQEG-rpk5AW98pGVD8BrYoQZdXkE1ea8YLOdk-twtwAvNnCTd9WZdSeDe4mZnm21OAEt6QxCJQ7ohlMnEH-1kmaKGtsnMX5Jhkvki5-P5mxSV5Tk2XrF_S0XqWUm1wdY8i4n5ziCxTkE3AmUxUkVuceG5cCZGNNZaucSpHIqniZb6WF3E7VWVrZ9fuDW9B-7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkooCwmSaKoNPhDpWx9qlVgKJhAu8E9eeTvSktlLf_l_mNt2cD70z0nrqF1H02u6vmZ8kvU9xjhDG3QicYWnpuPSqQ87so2FbX9G3FE_m47eyyP4QXuiFAwt_9r209dQRxYJ84PIshCbKTBKiiGp0kQZ94qDAlPj0TyZpGxP6Q6x0XzFrYR1RnL6UrG_7e3AeYhJg3oqsXeKaEZyHr586SUdMqao6lQQnAMeQ8sCU5SNe3Ythtcfhr4OIQfxEwQY96ILB1dPvhp57nWjNV3TuvqK1QrkGwekSayJJhuMns2f8Yx0W4aFS-Z7EtV5TvoKmBuBMHV11jZJoc2tZQ57eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=KCUP1ETDIi61mGKQhygt6UYFzvl4WJDXwWmu4dcgTGpxUZypbK3z64oWsLJDiy4njJsR1mzgX14kBJFv68SCpjmqYqKXYkf8HzMpDkPMwgqtybQxRNcAuVYurHScAZtNVsn023DolRu4UfLUzNGyO26saD-uJh4zoe244PCrtjmmcqA3W9bUOnUpu75yMaYNYkGPornC0phnWqso37MXMiJ-g9y3ctbmsWrJFPMlF8tjygi5U8eMNeVxRqdqKDapgzFDBk67Qm_CmghIGcd9qxVcSz1MDNo_wsu_VtLeOo1AhezmjHCRUINX1S7etjAAqSUFG53ORRxSQ8bvTWnNAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=KCUP1ETDIi61mGKQhygt6UYFzvl4WJDXwWmu4dcgTGpxUZypbK3z64oWsLJDiy4njJsR1mzgX14kBJFv68SCpjmqYqKXYkf8HzMpDkPMwgqtybQxRNcAuVYurHScAZtNVsn023DolRu4UfLUzNGyO26saD-uJh4zoe244PCrtjmmcqA3W9bUOnUpu75yMaYNYkGPornC0phnWqso37MXMiJ-g9y3ctbmsWrJFPMlF8tjygi5U8eMNeVxRqdqKDapgzFDBk67Qm_CmghIGcd9qxVcSz1MDNo_wsu_VtLeOo1AhezmjHCRUINX1S7etjAAqSUFG53ORRxSQ8bvTWnNAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=t_JyKa7LfGErkni5vA2LzGV8mx6apI_k2-JbvCqXX2hS31WetTYi-ctI3R5m2Ss3HlMdQs_RDylOeOM2jZh-HF3XJGwDh5gw0WV3zkjrk6ZuFaNaGv8Qws51MsQ1SaFprUzhEE0q4oY_8GTn16YoF0bgMuti4gPYydih8i4tPqgCSRMy0nW7LDzl4LOk9wnbXnUDFYVE8YEAD3acIFbTPU4_xGau0oAYhd390peMPbUdOSKZXDzmF643W2vudwjJw0OG_X5h-ocNKkiv39AdkyyHTfDoJPaV440B2orxZ_PduwdD5nwBtMFfNZU2AEL3-h2MKhzT-tgCF1kTQ7sd5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=t_JyKa7LfGErkni5vA2LzGV8mx6apI_k2-JbvCqXX2hS31WetTYi-ctI3R5m2Ss3HlMdQs_RDylOeOM2jZh-HF3XJGwDh5gw0WV3zkjrk6ZuFaNaGv8Qws51MsQ1SaFprUzhEE0q4oY_8GTn16YoF0bgMuti4gPYydih8i4tPqgCSRMy0nW7LDzl4LOk9wnbXnUDFYVE8YEAD3acIFbTPU4_xGau0oAYhd390peMPbUdOSKZXDzmF643W2vudwjJw0OG_X5h-ocNKkiv39AdkyyHTfDoJPaV440B2orxZ_PduwdD5nwBtMFfNZU2AEL3-h2MKhzT-tgCF1kTQ7sd5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=EBwnBPNS4fgvQd8_g_lmZXKxRZlGKzqSt5vemXOxnUtDMoFeu5cY-ANtahLmUqATU-g1X_pabTjOyJRZcECHm7tzUMVSBUB8Q-4p-uQcW9tfUvMBrJEr436EqHWsWTnwC8vNnV5Wcqe9NIKq27O0BZf-R2WaPA1Ijcs33WizWIxQ8kTLY9GRXQ1xotXaY4hKJQ-oNJ6TLbTGUTOTlEGJ6Lor8JPIl0y0CvP0IUXOrd_h6DS6a4e9h9wXWQBYygJMiyrHmG0pFgH3sSasKNT8-8iwkuQJJ0wl0VyCqjOZ80QYdwXDa063HxXL4Tfzq3hBCw8ymMwVmjUSyk3OraKoNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=EBwnBPNS4fgvQd8_g_lmZXKxRZlGKzqSt5vemXOxnUtDMoFeu5cY-ANtahLmUqATU-g1X_pabTjOyJRZcECHm7tzUMVSBUB8Q-4p-uQcW9tfUvMBrJEr436EqHWsWTnwC8vNnV5Wcqe9NIKq27O0BZf-R2WaPA1Ijcs33WizWIxQ8kTLY9GRXQ1xotXaY4hKJQ-oNJ6TLbTGUTOTlEGJ6Lor8JPIl0y0CvP0IUXOrd_h6DS6a4e9h9wXWQBYygJMiyrHmG0pFgH3sSasKNT8-8iwkuQJJ0wl0VyCqjOZ80QYdwXDa063HxXL4Tfzq3hBCw8ymMwVmjUSyk3OraKoNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=ULab4-7Xc-lK64FqvLmEqv7AW7tBkW3NsPLTor0pV9SFT0jyJEw6db8aPAXiA8_rPzcE7eIwb8EomPDBwaATpWmzuUEJRERCmkVlrI7MibQZOF5bIuEydAx9uviA0RpdLtcml_RT6rBzoSd-cuZf6xvhzrKmxF-yw8576vjxAYdLzg8rVrb6CDdV9V9VIiJ50s35dRL7uEQ6u8ofdv2uSZL6cfA5ZrF08csRmJfASjWkHegwaIzBjA0R18zDv5rrmpl-S5dSC6U_pOnpSGC1yDGBQoQpcYZ9olanTPlsunTZDwKw1wP7ey4h1xtlxIer8XyhJX5T5I-EFazSj-XQtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=ULab4-7Xc-lK64FqvLmEqv7AW7tBkW3NsPLTor0pV9SFT0jyJEw6db8aPAXiA8_rPzcE7eIwb8EomPDBwaATpWmzuUEJRERCmkVlrI7MibQZOF5bIuEydAx9uviA0RpdLtcml_RT6rBzoSd-cuZf6xvhzrKmxF-yw8576vjxAYdLzg8rVrb6CDdV9V9VIiJ50s35dRL7uEQ6u8ofdv2uSZL6cfA5ZrF08csRmJfASjWkHegwaIzBjA0R18zDv5rrmpl-S5dSC6U_pOnpSGC1yDGBQoQpcYZ9olanTPlsunTZDwKw1wP7ey4h1xtlxIer8XyhJX5T5I-EFazSj-XQtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjwHsLQ7oIl7h8dSSacCzWQ9CRIdL2HL8olR5E7fKFHN-yLNLTgIrJPn7Wyw6XofKL8rPrXeedX_fJsuV6EPeowzM-B9-a1WgHzX7xz8_97eEws_y7NexAaNA7BxIujQmlSyfE-yNDVHinU8nthiulvLgYTBEuOlxFmZ3LrvQQG1mzTm8AzyDbJviGG3OHPkISKHtKXtMVuOQKYsuQJ3krnRvGUJV14jIom2Y9E_4sbAm8wW8ZUmqQkSM1-Y6wjy-xTXo9fHKqnIQ_9NKVrsWYRp0dwFwXyEj0fLhuzigB3r3aJLnmKPBhr_QVbm4Di6ImxGFOUSEgX4d0pm_QOACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ij-Uw3oJh7ITursUofnZSDSXM8JmZkaDngLePWpCLiO3pUTAwX6fWGED3Vx9QksCUQIu_CW4gCubfsspr9vgGWNDHswvTICxCJ6_RZLYCkWuyqKoUMDfmoQO-hHNIDH0wo8mWftuVHijqgLZ-o58FAyi9VZYzTI-h6xTtopFJHd-F7tCc-cGHO6RdPs41aDE8-jnhZzLo3kARKvlbEr0h-Nh-MlRdGHgL6QJ1POmU60zB5pchzqqRxV1g-gVKDeNOS0__KtzZ2mRUupKNIc5nck7rPgI0Gn6MMa_zg3fF81v952FKAh9nJXzHywfRGp21Z_EF8qQVN9GRK7ytbU0Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5lqF8lmaPa0jAE2-zgbafFHZtijn8HlSC8XOfZUA6-TFZhy0kkMvQd0EgI5LfKzhYL7FXuCe1y1-zWrwQWvYtEneXrsgK919EM8FKBKi-6PxtB7FPck_JfzFX_KHwPqRlage-X3tns-wuDNPDRHmSNU6zndfg_TKYDMgJN1F72cIqvMWT7XOQBGKyv4d8mOj0g5UxgCN3OE9pauHYMIdweVJstHCC6NiQT0JkBAALpW7zlH4IAKARvSCWUsDGZnsGOTlwWcEatl15eP388BUSBKelccNkfcaouJayPjL2zgc8zRi8CJknorpkcDXeeACfBzZey4wtk-4z6JNggswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bp8G9OBFsPo1AxVhVLWISjdAhfvWtXwPyPlPosMwzG0sOZpXSmTWuhKvleSnV5K_ZZOnAB0rqTqfb9lX_nPwCu4eqcVy2LtLfh0m7sSrVWIhxYqennnRIj_g3iFnoizkeR960oIJOeJyrEjUtzwxG0Z2ZeUzqVI5E0HII8HWeM5tZQ74mpGMzKtrliv_RYRsZ9Ks8rMpRof-Nuet6196H9e0hk8RwN4QGeVyhchHs_JQrRDbgy0nHPCjQowEKdybUbX6IoPLIFTD59L5u_LYwsC-om2IAOnho6R38VO0XbvfnFlSzo8_YrLLo47Yyq0Qa8kJfb_wc0jaWBZila3boQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMTTtEYP5jD7bmjmW6RbpgpRnqfdzKVxzYeePupafVwSn144_JSy7wDMhxWcoTZn-A1H4HjGUiWToz8IYAhC8jCexaACClsSoy99FRlv1q9QaN-5qDaApDAf8fL9pQI6DyEc60lRM7Jy5dsnfxv25PhM3Rap-4JSc9d-A3jJ5H9D1iRLp3e_RngN0G30zgJgyBXPnhujhlQEHY5KEVyL6dJ7YgOJ6gYFDxCy7M1idygh8K7e-LO8cQXxjRD0MZP0xmHDfhdFqLegOH7OTUW_2Jz_hc5sGglpFjOW5K5TdiP8Y0bYVgDqH6H_YFUYCZHgOLHZ70X5naDZm6Qr6jMh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=cITNCjYJvqyq1E3-RQCRw_CEy7Op_ckvLiwoQst2eAeSELVplIaAWyma7eQFwx7oiTeHrNthT4s27S5cC4Vam_i2EbMMwT_JcJMwZHVsjGHUV_44SGOstJnJ3NYEm_164Do0znAJPe3tGp8gDrMtLev20kcrBvaNEvQU5yCOwFoG4vtcXWkViG2V4YyFFpkYkuHZiqC-mzuo0xoGvOqDNwgwSVRUcEur2l-yoj-ME0PMqZ6FNWicKwBv948tpq6vz0ssiP4zukWytgisNM07xXse8zZjTSDVYecoi1zwsYeNav5bH3eK0HyvUlOY_qYrxkUgdTXW7PIhl03kSeS0vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=cITNCjYJvqyq1E3-RQCRw_CEy7Op_ckvLiwoQst2eAeSELVplIaAWyma7eQFwx7oiTeHrNthT4s27S5cC4Vam_i2EbMMwT_JcJMwZHVsjGHUV_44SGOstJnJ3NYEm_164Do0znAJPe3tGp8gDrMtLev20kcrBvaNEvQU5yCOwFoG4vtcXWkViG2V4YyFFpkYkuHZiqC-mzuo0xoGvOqDNwgwSVRUcEur2l-yoj-ME0PMqZ6FNWicKwBv948tpq6vz0ssiP4zukWytgisNM07xXse8zZjTSDVYecoi1zwsYeNav5bH3eK0HyvUlOY_qYrxkUgdTXW7PIhl03kSeS0vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/InHRRKtfe7N0F8AHblLVFakAXbYnZxoGztVHbce8Xfdrk7VPC5c46QF5s1G_R6AjnjdAvl-8pdwt-SIFWgdPmTKSDR-npwBgMM9Kyai-phlSfp-Jz3bWaMzPfoftE3Ln0M4XpuL7pZICnNrXum9hotIeRb62i5V0F6fYKS0ExWZ8vRGEElSqBmdCkOMRl_aWAz4gnbhsm-56oDNLTYUWrWgrj1pyAiuqA3IZqTKNLKNRpMIN1To_GjHheJT32C4228XbYBbkDhW8IVer_67DGs4nlz9r1cCeM_rRXKHOnTKGn7fnXOe1c9zbs_Ei3hvKGirxTFEkOBQr1F25nFVW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Am8HAjFsvPSOH0rZYjfPKQoQs3BXw4i0fe8A6B2uYtUqaGKyiqp41gWmsDNNa15IfSBPTkVjCvl26PqRgKmkaaACTy1FuTTbopwTEwFpR5D5BwqM3seSAzL2c7ragJcpcdQJo1G4CYSLmiLp5QBQ6UeknG7Z0wVdjZkD69IuG3CyAasGysk7NmJR6b8PpDrV-O_7AP9wyXHJqIteE-UbzsChGsJwo1qDJfxso_QV1SveV9zKUvIi1KR3EXMp-3eIUEpgrFKbWJuFNU54DMv_t7EB7vNZOxC5c9drLBJu2uZa4be9_TLQJhRYDNOv78p7dBc5L4qgBqCpiSapxL0VhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=qaA1jao41UqpxjR_CRc4CpbGp5uYh0U91VDgm1NhchvfRP9PgmEktgSOFKdOWa3i6RQpkIC8dGqoNWUHPW2oYi1qIZrBOdsM0xr4l2ni6B84AIEO0IocSRY3fdUO7kxzUALSmEh61yO1HS2qdhZNJjxAhYeJwKUOGnPY6eqSMdmfApDL8EgJ99EKfrgiLupTbaGfmtgAdskmwH6tWGwvd7313_W-wJCREwnBGCvjoFctmOWAquv2759wTuYZdZU9nGcse0ZX2RxwWT4MOMCWvqZudN5jBzrH9f1gg1mB0yIR4kX6ktIZGR3KQ2SYk46PR4uxkKzzYas1kQJvLuqfCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=qaA1jao41UqpxjR_CRc4CpbGp5uYh0U91VDgm1NhchvfRP9PgmEktgSOFKdOWa3i6RQpkIC8dGqoNWUHPW2oYi1qIZrBOdsM0xr4l2ni6B84AIEO0IocSRY3fdUO7kxzUALSmEh61yO1HS2qdhZNJjxAhYeJwKUOGnPY6eqSMdmfApDL8EgJ99EKfrgiLupTbaGfmtgAdskmwH6tWGwvd7313_W-wJCREwnBGCvjoFctmOWAquv2759wTuYZdZU9nGcse0ZX2RxwWT4MOMCWvqZudN5jBzrH9f1gg1mB0yIR4kX6ktIZGR3KQ2SYk46PR4uxkKzzYas1kQJvLuqfCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=WY8HBjouMqeJXPqbg0JtbHhrVXnWFU1GPPZ-BUYS8qSTxhquCom4-Zb07k14L9oqa6YIrhM8XuRYXQVpDAWojZ8BP20n7uMQfW8N7SYJRz6ggi59D40kac3yw1H-Jeo3NR4Hzci_lpfL5rMLDhQlHFwJhLos6_Kvg2pM7Td3M4K2ohU5SlwS9xcN1TyeJ45T0ATqn6eYXnvY82ZUpiUGUYJfRWKpDVJtyu1pWlBPdr5D0aUfQnb0o-TM4qABjwLIfOdi40vJXOv2FDLgxi9W83sHT_migu4FDmQjMAUmYhEZdfV51YXjLVJY3UxlsP7Lem0GE495iCrI4v2uoj88OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=WY8HBjouMqeJXPqbg0JtbHhrVXnWFU1GPPZ-BUYS8qSTxhquCom4-Zb07k14L9oqa6YIrhM8XuRYXQVpDAWojZ8BP20n7uMQfW8N7SYJRz6ggi59D40kac3yw1H-Jeo3NR4Hzci_lpfL5rMLDhQlHFwJhLos6_Kvg2pM7Td3M4K2ohU5SlwS9xcN1TyeJ45T0ATqn6eYXnvY82ZUpiUGUYJfRWKpDVJtyu1pWlBPdr5D0aUfQnb0o-TM4qABjwLIfOdi40vJXOv2FDLgxi9W83sHT_migu4FDmQjMAUmYhEZdfV51YXjLVJY3UxlsP7Lem0GE495iCrI4v2uoj88OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=siwfwOXqvz9_f-sDUKuyQz9LqZVyurHQ5lvGoz9_ChmEigi_XIOpv_g5nPw-z430mMgkYR2KH363b9Heb920XEYUdYQI8MMJ7DxA0wyc1mYMqA67x14ryllFr3SPl2FISi9NL43ORazlyDLEg7ry0FoTrrrGqV6tMsb8919oXAkCt0A9Bf8CvunhIfKqm8a8cunc0YOq1yp2KxYw8CsTHBpGRLMXF1d75mb8u2wgYm61WdzkP35AymkdJVyPiMOb_i7goI-MGeNGmi38_GSwjidFL_gKoPGmuXbnzAjRgPnkOSt1pd0vWNJhF8w6Ti4UTNoy2K6-cAX93WKz-KLAnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=siwfwOXqvz9_f-sDUKuyQz9LqZVyurHQ5lvGoz9_ChmEigi_XIOpv_g5nPw-z430mMgkYR2KH363b9Heb920XEYUdYQI8MMJ7DxA0wyc1mYMqA67x14ryllFr3SPl2FISi9NL43ORazlyDLEg7ry0FoTrrrGqV6tMsb8919oXAkCt0A9Bf8CvunhIfKqm8a8cunc0YOq1yp2KxYw8CsTHBpGRLMXF1d75mb8u2wgYm61WdzkP35AymkdJVyPiMOb_i7goI-MGeNGmi38_GSwjidFL_gKoPGmuXbnzAjRgPnkOSt1pd0vWNJhF8w6Ti4UTNoy2K6-cAX93WKz-KLAnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=TNvlJYkIHdwxfzpcZ9YxZrjAscIJc6pUzBJ4qfi2PqFi8fkkxcSQoPbIAapi7EFoPUrcIETxHLangYmqFUXrwq_YhKdSi-aoELXbQvl1BXduMBtyb5LI2hfUtOnugr137OXLx4b0OjKo9Sisu7iD5AZRCgDOxv-3BRLxl_EQYZqGmiZHMl5dDOX7ZBqs8LcrG06ktzPUFS_ZwmhjmEJzWkRJmSvXWkJjY_owJW71M8t2cQH78n8p7EIKBfSemLWhSoIuMjl59bWF50S55HTckIB6zyzKw1A3lUoZJ-IwEr7m7RKJlKskbScR7cNxMxik7EyMWxnOGifdOgbEH-erUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=TNvlJYkIHdwxfzpcZ9YxZrjAscIJc6pUzBJ4qfi2PqFi8fkkxcSQoPbIAapi7EFoPUrcIETxHLangYmqFUXrwq_YhKdSi-aoELXbQvl1BXduMBtyb5LI2hfUtOnugr137OXLx4b0OjKo9Sisu7iD5AZRCgDOxv-3BRLxl_EQYZqGmiZHMl5dDOX7ZBqs8LcrG06ktzPUFS_ZwmhjmEJzWkRJmSvXWkJjY_owJW71M8t2cQH78n8p7EIKBfSemLWhSoIuMjl59bWF50S55HTckIB6zyzKw1A3lUoZJ-IwEr7m7RKJlKskbScR7cNxMxik7EyMWxnOGifdOgbEH-erUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=A238R6qtiUE-4a3EY1RtuNj6zgPd9AYHDWLNzAoGuij_-u70vC77WhdeZakXeXNbSFqC0AbCdV1nc_GTYBSFEll2MoUgKYrs_V2Ei3QfviE2Bdd8NsgRfL0dDFJnYcvWjQv3leuZOtArH12ld7VfxDYP4jsOUnzbd5r2HxakNLibUyEEQ2KXGIDNReJMM8VRLHKNIE2iPA50c1m72QTMuh9PohiAOSCJcr9xXzpX4S0NDrKBq9aRuTujwBXJv0SWcC_tTDkR29ul-D4_QV2geBLGCfb4mUXeRxEzKRALsnxZREcvVZfHlXIWZok3ywroQaMOX8EDZM2e1PZypo8ycw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=A238R6qtiUE-4a3EY1RtuNj6zgPd9AYHDWLNzAoGuij_-u70vC77WhdeZakXeXNbSFqC0AbCdV1nc_GTYBSFEll2MoUgKYrs_V2Ei3QfviE2Bdd8NsgRfL0dDFJnYcvWjQv3leuZOtArH12ld7VfxDYP4jsOUnzbd5r2HxakNLibUyEEQ2KXGIDNReJMM8VRLHKNIE2iPA50c1m72QTMuh9PohiAOSCJcr9xXzpX4S0NDrKBq9aRuTujwBXJv0SWcC_tTDkR29ul-D4_QV2geBLGCfb4mUXeRxEzKRALsnxZREcvVZfHlXIWZok3ywroQaMOX8EDZM2e1PZypo8ycw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6Pwpn0cjiA4YBmKldjk3_IYM5Mw2Re4HAPtQbLP32c-OcwImknYGPh3n0-yF9IY2r_Xf67zdBEZfz6Q-YyPNY9IceCpxPjEHwHXGGGPzOznSerXQ6UU1Ucs-q8FS5PNsRAwrEBLKL5XiD35XAnfda_KxVPASXfWPOWWFkxIn1KB0dgUIzWSMt6xiMC1NU3L3OFpshHkBvR0_69rrEFsZaJul-V849qgCTUFLnLgRkdQ_FjfWj7KoIRmrkWMtQSWNp4rGZQoHB-i-C7sxEchRPo9HIidKhRKh-bISnZ94RZdiGy2tOqtlt866w-3kolDN8mHjTMJDsfcZbGCmRSNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jH8unE5uO9jfAYwSJfmW5zCeTs-6Qlj0nyUbd7IEwa1iEqk0p7lxKIOPridR64_m7wRYEcgB0rD86UcJCR3RDIdzF9-G84oNFVtn5YgtHTAEOziVFiGxvrUT9ob0DkuF-2WR6V9tqVXd6gaTivgOHnVlukizV9aMOoBYzcxahOHje-Gm6_uZ4qUZ6w1z-L40e1gpi3URGF1eFqxfHwEqGI8UMDA4Uav2aIeC5pI8zI_k3_VfDhXVN2FYxp8mmJjk4T21VvbPCgwo9b39mzAWi78fIPwd8fsljlY9jhYajE7l8wPBRL-GGYRHGoR93yIhOx-0sbBSIJDLAcoUg0p2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VFQD0bBPrUrDdY5LVNVHVglT-BvifS6nmIc-k0zkOn0ncNsyS2xY4zkXsySL8DufbwDdvwMmmP6qV0y8a84j8ueYWfVbq7OV2eI6SqtK8TNORxtUXRjQ_O_P3HB7cfq2VK6-ccnMmzntjlz4sQtiKZkbkJZ7ZLniBtzIrnTcAXLRYhcdoojGAUcoyjAjSHdGI4M74rb4FT2dpoxIGdSzBSp2frPpE-NMUR8cqrRsUXxiMtx-PRXqycmLBDXWnH0tNn8cCzU5Bnb83ObeOt-1xsw_lBZmKKR26LV7ZKTjESLi1vIrtWaOibDg8qQfDRx0L_n-xfRGL8E2hxd8-ff6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=bRuHX7kwh-HolMIWQRVb53B2D8nVydpgRE3gRr9AJJ75DRCNjn1pLP4L2U2mByXnOkmYVOBRmKNw33JknrkUvTgJXXA0iLi7zQjxpEE_F2YS4pYkxenjA9FY5atHouH7r8W6uw51QfAWDuZmimk-m1QxgbcaPdb9NgPdx70RWRektgocLlhHZrs_q5a1yFjeZHskOeYr51J_1R9zc2qnPIyicpTTeP2F6bADY-h4Ac8_X-v6Unaqs-N-awnfsNwWgOS-EQj3WPMP4QhF6LaYiKDHyjM2QmNik0vmjUYUtweLNlk78sfCNXRkWh7lzO9uYxsqgwUenB3LRtAA4mI5Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=bRuHX7kwh-HolMIWQRVb53B2D8nVydpgRE3gRr9AJJ75DRCNjn1pLP4L2U2mByXnOkmYVOBRmKNw33JknrkUvTgJXXA0iLi7zQjxpEE_F2YS4pYkxenjA9FY5atHouH7r8W6uw51QfAWDuZmimk-m1QxgbcaPdb9NgPdx70RWRektgocLlhHZrs_q5a1yFjeZHskOeYr51J_1R9zc2qnPIyicpTTeP2F6bADY-h4Ac8_X-v6Unaqs-N-awnfsNwWgOS-EQj3WPMP4QhF6LaYiKDHyjM2QmNik0vmjUYUtweLNlk78sfCNXRkWh7lzO9uYxsqgwUenB3LRtAA4mI5Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQrGE3wSSj3-9rpbGYePGEk7Z8rpzVagL03n6dm_uOPAXep-aisZ6_UkRsq8NrgeOd30Qxr3z-VDc8hH_fnUlwZT7bfkVDH9-Fuch59b5zsrhadgoUcpVEYlYhZS65cU271YNCB9Xm05p9nwTKioKuiXzc_WsNq4Nb4AyRXU20SJ-hqIahOY-_kQlxdQYvsphwNTTi7b6Zb-Tk3pQNdM0cNuuSUGJyyGZpzyvwFs70fsAOwzHZrRT9qQi9Ejsyghv8K8ZZBhf4Sb1Np0VdzsuHNxdxhXSOh_9I4JAJDqR38wCcoemsIhrYzTNXaFlj1EPF3KFHxT6sUeh-wIBFsjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=M3AQ2-2ZXoMrFdPXno4BKzOWl4AJBl2qRN-zz7EVDjry9SszGv3pf-jsURrC5BeXVJFktOit6TuFAQscqh3pFSo5ozfZhhFIZS6Qy-nfLhW5Ad5ChAdurXrPYuUjf48pv6mtKrkiAolltpRTInK5QbvMU7JM6DEnnf44MXnho-JWWtvRo3eCCqph8fF-M-iDgG5vjCQqkrgT5q6xwkZckVZHVxhJzDlLwt5PxdO7ZLe_s1l8EN2saDSCVNcrncmMevuc0FH9uCCCJOD6cYEMDSa5Dh0YTldB_gHNlhWV3Nrv7sUIUXJDgypja-mJCn6zI7vS_JmoGaRjkCLdgBQCBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=M3AQ2-2ZXoMrFdPXno4BKzOWl4AJBl2qRN-zz7EVDjry9SszGv3pf-jsURrC5BeXVJFktOit6TuFAQscqh3pFSo5ozfZhhFIZS6Qy-nfLhW5Ad5ChAdurXrPYuUjf48pv6mtKrkiAolltpRTInK5QbvMU7JM6DEnnf44MXnho-JWWtvRo3eCCqph8fF-M-iDgG5vjCQqkrgT5q6xwkZckVZHVxhJzDlLwt5PxdO7ZLe_s1l8EN2saDSCVNcrncmMevuc0FH9uCCCJOD6cYEMDSa5Dh0YTldB_gHNlhWV3Nrv7sUIUXJDgypja-mJCn6zI7vS_JmoGaRjkCLdgBQCBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=Fy98lbavZGUjXCHjByUScH5o5-vgq6bzADTusN5b7Yh5UDmLVX34byR9almaVSkGiaEwLjT36T5rr2FsRl6Y9fmAzYz-7ZFCr929fZhjEkM6syBGDUsov_cjo8DGReDUVuKw1qfzR5RDZXZ2betPC1Bie-ndCVG3gHn9c0R0xgC8OBUn2QM7NDINcSr1DMxjPbnI4cYl7E1n-dpQAOBLQMokZyJvrfXlsOAHs5_sNVPoQOTbos__w9DlBYjvefdR5NDAoPNqaYhspsZCBCSpjU3UER2I6C_4DXG5vKrA7vcDR4L7P3VUztGpGzG7SJsxNJ49mblkIQkRdwSWn-TJ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=Fy98lbavZGUjXCHjByUScH5o5-vgq6bzADTusN5b7Yh5UDmLVX34byR9almaVSkGiaEwLjT36T5rr2FsRl6Y9fmAzYz-7ZFCr929fZhjEkM6syBGDUsov_cjo8DGReDUVuKw1qfzR5RDZXZ2betPC1Bie-ndCVG3gHn9c0R0xgC8OBUn2QM7NDINcSr1DMxjPbnI4cYl7E1n-dpQAOBLQMokZyJvrfXlsOAHs5_sNVPoQOTbos__w9DlBYjvefdR5NDAoPNqaYhspsZCBCSpjU3UER2I6C_4DXG5vKrA7vcDR4L7P3VUztGpGzG7SJsxNJ49mblkIQkRdwSWn-TJ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=cmjRzEdcZ0fQdu578wLUPH6pJOV7sVaYAKrqqWhaGRdpTiSh4Y0NBS5cPgAJ3T6-HQZjEXMN3BXPnpZKfv-TNnkXaXPEUyorJ3fxhhSGfv12JcqOSXmiu84DFfWFe7Q4isu0LjLrkHOVvMajbnKMB30HZMy_8gqOlhpObACbqUXde2IdSqofHXvmiLTZoEjTA1Byrt4t5U_0WsF7E4GK5becL7fWg5tCJMucgKy29mjNJ3Ez-F8mmnOCmRwFzwntPGuKH4wsmhpFvX_8f0DzGzShzOJZh63v2kBY8gJPKch9Ws8J0YKJR_nWTmkN_0FLKEcYwTs_Fke8agWqJBaVzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=cmjRzEdcZ0fQdu578wLUPH6pJOV7sVaYAKrqqWhaGRdpTiSh4Y0NBS5cPgAJ3T6-HQZjEXMN3BXPnpZKfv-TNnkXaXPEUyorJ3fxhhSGfv12JcqOSXmiu84DFfWFe7Q4isu0LjLrkHOVvMajbnKMB30HZMy_8gqOlhpObACbqUXde2IdSqofHXvmiLTZoEjTA1Byrt4t5U_0WsF7E4GK5becL7fWg5tCJMucgKy29mjNJ3Ez-F8mmnOCmRwFzwntPGuKH4wsmhpFvX_8f0DzGzShzOJZh63v2kBY8gJPKch9Ws8J0YKJR_nWTmkN_0FLKEcYwTs_Fke8agWqJBaVzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=NxoiPx3DHiZh6IIaC-HV3XTG_uZzV4mXkxJfOfbwv5pblpfc0z2gfyM3Q7N6J3CtzGh2flBL6c_8yIoT0OyKixUgIAGkd7Pq6rcR6XNCZu8v4ewpZv0CSF1uByN4u_DO9LrbkJpJwcJXY1PTsMOEaC6vSxYmKKFiMFXz7J9bcQJVSQ_R_wXE5_eevd96ooQQDICEHpieQxTXCa5nzqtYt8SPHtbZw1NQI4F_OzRpvoBTdLGe_5n-GL9xB53N6AdYY5er2W1XgXzScQYFUCJW7aYEEdb8wt1npmYcQu0Bl6yh1g4wIesoJvqX5xF5y_DIgdy5QyPvnqC690S_nKzNsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=NxoiPx3DHiZh6IIaC-HV3XTG_uZzV4mXkxJfOfbwv5pblpfc0z2gfyM3Q7N6J3CtzGh2flBL6c_8yIoT0OyKixUgIAGkd7Pq6rcR6XNCZu8v4ewpZv0CSF1uByN4u_DO9LrbkJpJwcJXY1PTsMOEaC6vSxYmKKFiMFXz7J9bcQJVSQ_R_wXE5_eevd96ooQQDICEHpieQxTXCa5nzqtYt8SPHtbZw1NQI4F_OzRpvoBTdLGe_5n-GL9xB53N6AdYY5er2W1XgXzScQYFUCJW7aYEEdb8wt1npmYcQu0Bl6yh1g4wIesoJvqX5xF5y_DIgdy5QyPvnqC690S_nKzNsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=e6kPqpRId03sEMuTywGZDVc-KAcKk1HV46Sw4nzJ8Cbza518xqMguY1F9WCvFIN2XZSdAjmQEkNccGvfc-iRFRCtBBUZEPzVe07XSopLZeEyjg3CfW1CZtYog9hj23_d8AW_3j0dVh5Q_usJK9lhZf7QO24LQvNeaS6HsqXLFvyey0SnmD4xMBb0Sc9lxVkcMaNoh2-4AqhpPDYwlPsK0h56jlisbRfStR-QkXyH-_7EJs1yhpVrR6FolHGqB2tx8geH_25YfsEHh8XzKOlV74JaUSqI4ipjCgbCgnGsxpL3u-msr7F7UerR8ZLr1aoR7-jtxMDvEvSRskKtR11d7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=e6kPqpRId03sEMuTywGZDVc-KAcKk1HV46Sw4nzJ8Cbza518xqMguY1F9WCvFIN2XZSdAjmQEkNccGvfc-iRFRCtBBUZEPzVe07XSopLZeEyjg3CfW1CZtYog9hj23_d8AW_3j0dVh5Q_usJK9lhZf7QO24LQvNeaS6HsqXLFvyey0SnmD4xMBb0Sc9lxVkcMaNoh2-4AqhpPDYwlPsK0h56jlisbRfStR-QkXyH-_7EJs1yhpVrR6FolHGqB2tx8geH_25YfsEHh8XzKOlV74JaUSqI4ipjCgbCgnGsxpL3u-msr7F7UerR8ZLr1aoR7-jtxMDvEvSRskKtR11d7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHSic-zLk45ilfjM9dGqJk-e_rNL8imi5hqP-fV-t64aBDKe0eRO1Zkm4kMG9kUKCOioEeJaULt8rehRqIr__PwDI29-n6cHh-YKg8870HtD28CEhGERvdccdDzz-IEj1K9cPXd4OUhzus_Es5lIYO3M0QeLIRHFnVtbCiIZdnn_jGm4VV8RcQuNrLqqz3EWCQEhNjgIubIart4zKHH1g4sWt3gTFM34zqDXt2LGA3XmP1fqO8RsXLfii8z7d5wjoRXZHY5C_zgZqUKmLgP7ZCqLRcPuK5BWay7eCWPp1jAVM8kPmZ2d6qYi1rXgTwS41kgjH-oEU5TlVw_aR5tVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=eXlIkK9OCQ6W7-a8A5fOv_Zk56E5PMHCbv9Py8x7RKv0iGGtqI0bLGUxwzHFSOb1084QxAJNvRjnnbovvqeN76horpp11kbApsaR4htqXzPSFnCsWc3h9qISC0Ay31A7C1A8WjFJz8sfI7cs-ZHRIoR1k8RV0chETfBOyGaobvjfkKbxohwr_PpRmAVXf-GFs39KMdJ0g8zl9cpJnnyCPetAWIwmJElSp3N7iX8wLkAz2byUYmtnuvk70fEKnYXp-8Hc7Ppl5qAuEeswLate2SPGSyvZsGVkKL54v7qUy7OE28wK6_4LkG2KhmdFafiRv2rDxmstOSh8gqhA6RsdJa0uko8ZlVskKybcaiG0t3fBtJ-jFTMfgamFTJT86Jak5vNBZb6t-0yM4D9SDJU4Oc43NwsYldHwoVE2pdzJXfuGUQpOmm300ghteNWhUe-kCIec2EJNY6TyJub5plw7y0nELFxoAXcACNN1kw_RkTY-Hld40SrWJBrdWF-oX0pxQg4OeS7kzHOk00i_8xJ6ruSkEzwVLM1XM82okp698tm0441dTD5ZckT8UHoPPgq8vpQkRiL5rX2X9k6xSZUR7sj1MLrLNvJP9mDLtKa8pq8P9lBJukQJ7DQkFSJudfeSrjAwch3zpT2zRTRaXYb-OL8_mQBNYf79623zEM0KrN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=eXlIkK9OCQ6W7-a8A5fOv_Zk56E5PMHCbv9Py8x7RKv0iGGtqI0bLGUxwzHFSOb1084QxAJNvRjnnbovvqeN76horpp11kbApsaR4htqXzPSFnCsWc3h9qISC0Ay31A7C1A8WjFJz8sfI7cs-ZHRIoR1k8RV0chETfBOyGaobvjfkKbxohwr_PpRmAVXf-GFs39KMdJ0g8zl9cpJnnyCPetAWIwmJElSp3N7iX8wLkAz2byUYmtnuvk70fEKnYXp-8Hc7Ppl5qAuEeswLate2SPGSyvZsGVkKL54v7qUy7OE28wK6_4LkG2KhmdFafiRv2rDxmstOSh8gqhA6RsdJa0uko8ZlVskKybcaiG0t3fBtJ-jFTMfgamFTJT86Jak5vNBZb6t-0yM4D9SDJU4Oc43NwsYldHwoVE2pdzJXfuGUQpOmm300ghteNWhUe-kCIec2EJNY6TyJub5plw7y0nELFxoAXcACNN1kw_RkTY-Hld40SrWJBrdWF-oX0pxQg4OeS7kzHOk00i_8xJ6ruSkEzwVLM1XM82okp698tm0441dTD5ZckT8UHoPPgq8vpQkRiL5rX2X9k6xSZUR7sj1MLrLNvJP9mDLtKa8pq8P9lBJukQJ7DQkFSJudfeSrjAwch3zpT2zRTRaXYb-OL8_mQBNYf79623zEM0KrN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=MVsIo-l3oM4sLunnfNi5zZXWk8iozTRunKyZYw2e8tRorv6r2lEaYXw3biFZ2CcA7kKPS5IecBGmcsj60zF_8qbIhlfP8kGtseufBHkjAJU0DshASPLfm_XFwpMj0C--emSkElralEP5OnJyuwRsjBZyYUBdaevN12BjFBEebbQSNuhgZDqm6wkyC4o9grjVUa5mf5J2E7wjybmEQzDPLRKtLg1bixyEphtMPkmirMqv9LFM1nNz_Sd7HqHycRTwjPzVkci3aeGGKeZemAXrUdZYRNCl8NFuU6i9IKt_R7SqtAJKU6hiYGNuVM1Y-aTTHnTDX-SAOxWytAMzto39tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=MVsIo-l3oM4sLunnfNi5zZXWk8iozTRunKyZYw2e8tRorv6r2lEaYXw3biFZ2CcA7kKPS5IecBGmcsj60zF_8qbIhlfP8kGtseufBHkjAJU0DshASPLfm_XFwpMj0C--emSkElralEP5OnJyuwRsjBZyYUBdaevN12BjFBEebbQSNuhgZDqm6wkyC4o9grjVUa5mf5J2E7wjybmEQzDPLRKtLg1bixyEphtMPkmirMqv9LFM1nNz_Sd7HqHycRTwjPzVkci3aeGGKeZemAXrUdZYRNCl8NFuU6i9IKt_R7SqtAJKU6hiYGNuVM1Y-aTTHnTDX-SAOxWytAMzto39tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=WewFuBcx3EQ3lPgM8UovvOt3-4rm-uAhg1b3VpNJYlxyLulG35o1ToZVHEjEJ8D0DlNfe4dnbIhCXs-nqHJsWgJoZgL53wDXONjO4Bk-5pSNN_S_xRXIS5ZJDmqeYRt2HUq0zBEzKSiH-_pVBZXMCSm1w_GKOJLZ8LH1lqiHmqNwUeoKeWBdebgfXPTR6qvwPcpYAFU6oWoE8gHmNu1XdsFf2jwjl9sbBFn9gSUHe-IKgYcpGTJoIwOTV5dnwQ299IK53Ho6fFS8ofUMIPshlebnyByUi9ztzLvGBbEscIYIJR431KAbRDZEg49Ofd-CjYu7oxd7H8Mx7yfrGglYuEvD4VF0_RL5Zzl44sRvD87sw5kstoIEvCESQOgq59W2FaSB0VX2M53CnJk5Mg7TV2GO3R14JU6f-7iPPcmjWSjWaEtA_Q7zMOadvRGdmMrzD8EvnWBT_LPzfbM3g7w260xI1jh7fErRXbczM-B6FHsZWs7Eai-pGBlosE5eK0svNXxGVw9GFrObsIwOBk8oF4gZcZYeUqEMUwuuhFN38EPPKNJsnpWXzspE2pJBqItJzTLdRBbNb7nHKkwsPF1rMxwamptRmhp7xFKDkxpmO9heBPT1x7R4vSb2gOugUquL1aMBgDdcBNEaJUJZ3d6xBoTOAcYcuOV8rr6gQFBYMBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=WewFuBcx3EQ3lPgM8UovvOt3-4rm-uAhg1b3VpNJYlxyLulG35o1ToZVHEjEJ8D0DlNfe4dnbIhCXs-nqHJsWgJoZgL53wDXONjO4Bk-5pSNN_S_xRXIS5ZJDmqeYRt2HUq0zBEzKSiH-_pVBZXMCSm1w_GKOJLZ8LH1lqiHmqNwUeoKeWBdebgfXPTR6qvwPcpYAFU6oWoE8gHmNu1XdsFf2jwjl9sbBFn9gSUHe-IKgYcpGTJoIwOTV5dnwQ299IK53Ho6fFS8ofUMIPshlebnyByUi9ztzLvGBbEscIYIJR431KAbRDZEg49Ofd-CjYu7oxd7H8Mx7yfrGglYuEvD4VF0_RL5Zzl44sRvD87sw5kstoIEvCESQOgq59W2FaSB0VX2M53CnJk5Mg7TV2GO3R14JU6f-7iPPcmjWSjWaEtA_Q7zMOadvRGdmMrzD8EvnWBT_LPzfbM3g7w260xI1jh7fErRXbczM-B6FHsZWs7Eai-pGBlosE5eK0svNXxGVw9GFrObsIwOBk8oF4gZcZYeUqEMUwuuhFN38EPPKNJsnpWXzspE2pJBqItJzTLdRBbNb7nHKkwsPF1rMxwamptRmhp7xFKDkxpmO9heBPT1x7R4vSb2gOugUquL1aMBgDdcBNEaJUJZ3d6xBoTOAcYcuOV8rr6gQFBYMBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=Gt0Rs7hJuGzEb1UNAdfzQWwG4opNeqj9Gj5vA93I2YnJvROUiS5S0ROc8ev5v_Qi7OPRd6vEKHUfzGPyGA3buB3ezLO4R_-8j3M84pybP-2tyf9fgOAPlJZz8TDDzqY2ogVW76DLCVVDqZqxtcqcCq2xtoHraKXPw8FEUrKxf_Wo6vKnjAMqXKZjX6xccGuMh-iU6Uz0tTpUwPql7dqG8q_3aRaIg0u-dYuv83msbgzP_pchyZmWeQqlhtjs1GpXhYOJs7i-u3jImPH1xuCKYeLZHThSr_8cpHn2k6FpZMVNZ0ghkdxMs_jM0RupMo2YGd6GjoRkyrQfbHcYgQRhpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=Gt0Rs7hJuGzEb1UNAdfzQWwG4opNeqj9Gj5vA93I2YnJvROUiS5S0ROc8ev5v_Qi7OPRd6vEKHUfzGPyGA3buB3ezLO4R_-8j3M84pybP-2tyf9fgOAPlJZz8TDDzqY2ogVW76DLCVVDqZqxtcqcCq2xtoHraKXPw8FEUrKxf_Wo6vKnjAMqXKZjX6xccGuMh-iU6Uz0tTpUwPql7dqG8q_3aRaIg0u-dYuv83msbgzP_pchyZmWeQqlhtjs1GpXhYOJs7i-u3jImPH1xuCKYeLZHThSr_8cpHn2k6FpZMVNZ0ghkdxMs_jM0RupMo2YGd6GjoRkyrQfbHcYgQRhpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
