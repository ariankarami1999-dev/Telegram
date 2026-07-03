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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 06:02:13</div>
<hr>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOuMgUcNhEA2vQq2LfW_K5o9h8H3Nz3Liv7rmjnyDYkSSA6sN6qsT4bKhGyUKHyV5w0du8_I1_Qphs50pfSLDim7jnATibj3nSHD35aNnqZoWRohesqFlgGKwBCRkDXIXHJSa8CsmBwAIaCG2He1CiFhfOylU4IL4uJ4WkYSMET6pTX3F9sFMft50r80ADushpFG86zQs87fQMXFb_Xz21yjsvZusTrV23ZC4mTH6A_y3qGUEeSrXizc-85ErXHU5mRkwt470so76IOxg-bOLD_nwIIlMRo8G2wTcGDbQozsvRJgj6fwk6hD2fmxcFvi3HIdozi7fqyZlF2qo8q8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTQzLW12fcu_3tWKsVQa9HXzX4CchRGQgUhEbfiwPqosOD18R-ABbvvfcNGM6qdBnepHXhIOCA-cf2BoFQYckPz74Mf46InfqMX7rheGDqhJ-EI6LGpf-AfEkNhLWxiykNH98GdxdM5o1PygHzLNho2UjvgEt-Y9bqDpAcntAqws4-UdlxUSVmUhGbrTv4PjRdDH2sku22gNBAdWU6ljetXtXEa_kh0hPpCtBgIM8DofPpZlJi1nuzst-tFa1f8PuWGsEgb7VzNRJAC_4_Qyn1aPiPWdS3uh4jpkYMZxdpjNKBWUSc2pufo2qyvVdSQHCe5aZ6FEciqTBL-06Ep4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJk9GvyJW3OQ8I8WfukEvnqBEO6CcLIG4Mn17c7HD79QR50iLZhv7Lu8GHplNWSuHtnXskj93wexuVzIg4Oak8WSuGj8Vxg-DBrYdIMJD0in0VPGEpG1H1pZzHOaajtq8ZtAGMSY3CDirhDujALce6KEGJXeQ7u_2GX214n-Z6B8NhTjFxpcEM1ETlLHTPjzmos11pFWYAK0wDLTE7BJNtf1Vj4QQC1djg8XgYkdpYIAA7XoXyrUr2X9MmPNIcNVajs6YFwP453Cu1Svi54OdmpHhKof36v94YjotzLBoiuIsDEQivJMYbpEW0arxXDm4wX-YHQJ5pJtwF1OSxCcCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVUfbS1-hRgUAA1U09dOnUIDCUQ9rEbCDlM2Z-VbJBDgN5Ilzny4dMlB0fQRKinANxP5kCWSnd3ipts8RtDQoY3JBXXPHLFda-fXdaxysXFcHMQVYg2gWT2Dht6Q_G8nAWVxgnPEsees5ub_v2e1i5Impm2_9rNbapjeDQFyACWHSOMGe_DBNjfyQA_qGaFQUEdpjx18urRITLmng53Mku8WVYuBAGJRAXzTMZTAiHXcAzpV2UUJX8xSEqaOGmRsZho8gz6w6LOfH8VF2gmqwQR2EdZ92V5VgPbdYzZVo5SMUEvJjtS8tqhljfWecRAnVsT8Kfcc9HKln-Z29LKeFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqK9xctnlVvPpnVbj5vOwRXurYw4pbleRflAbvDL0BxJadcqcI8CjQOiN4aA83loOTbsHbjEOCCrqpcE8IzaeOiJNdp-ifhNF86kimZKW-g-kifKaCpWamM-LapfBPY1qPK30y1U4jDl-LFgy2i-QBdMB55_Aq65fEzmB439HtzQAyLk8E8Y2G-JPzSHbWE6qbKjXlOAsBSIAojmFZWxcYxZYiVL5TYakQndZRZsOj5frVjug31kGx4xGNP_SuMPBa2CUgjY-6_JsFuEDaEyJWa_C0M8ll_PN_AFGRubL6a7-UAtzCHg5tVSp1XBoJ4Q8ybeOHZ4IGvP9G-uDutXZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMuVB-8aYZWdmmtfl53F9taUrzrq4PCcWd0lYeAmSOfXVcopGPSo4K2P2p4lYWgWF93k1DLnykC8-SCSGhXqshJRUr8QIx6qBCgESVWoY28VsXAcTiAO9o-jh4szirza1fTPH15WIthedVhONyamvySvMCLIndKMRqfi1f_Fg3Gqlm2mxlF_WwhlkQkCFFOEej1tDWJSQPs1VXNBMAyk1gk1FWJ9iEQ_n6I5FZWMjPgiw3dEIM5fxzROGslmjUApkUFwwhU3G6SfV6L4dzvaMAkfz2-M90aZnroJj1-6grArvuKp4RQJxnJwORxVIM4NCjrdTslklYOO4bc07cXKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwIQveqeG1Hc_7YajuUyMYssWCsnuqcVv5IkF8p39qrQXZrke3cOrWsnfjwcMMie6YGj_L4KxB6BeYKr6HACHokWst4fA8le7Z1CmVTa1Zi-volX84JIwga1rk9oo4QvsMCXAOdAyJJw_dsadGt81TqC3VE-iSnoV2QZVDiuY6QOh9BsIJcVZ7pKs82d_9zgqNFBxe2fUE0gXJdl0X6t5s3k1BaHrWgajfb9VlHHvuUuxa3DmCaiAYCedLGDIEjh4xsLCsgl8KRiQjljOUT8KBe5PFLvJsjC9bvjmrGxzMwySIwNOVbHNh6tqMPZOS6Z5wUh3UuOQjsVDIgki48IXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=dmqKke3hirnUUXqkPEiZ1ItSNZLa0M4wLEllvhrlLPUudo35Or-8FCv5ia4eo4irm-tHVslpzHLI8bj0z3fklF0rr5lDgfQZ-D_Ge6K4x01BFgCvUte13A6apjKgnTcj6kb2hqFHI811FPhFBUUidqPxhTaPhVYZXe4MwSInuZVyIC2lHKHXCZEU1AYtv6907quH2zbMq6dMtpvNGcT0dvk2AWczOAGTVwbfkWHdXX7tyvGw3m_QZFulfu5nZTFOIow0YH9ug4--pEib2CmM_VEPMBaWSvZjxNrx0hXxVI0rtQNfznE2oJnyKkSLkDh_xbQWs85YAmEyZ07c-R_j-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=dmqKke3hirnUUXqkPEiZ1ItSNZLa0M4wLEllvhrlLPUudo35Or-8FCv5ia4eo4irm-tHVslpzHLI8bj0z3fklF0rr5lDgfQZ-D_Ge6K4x01BFgCvUte13A6apjKgnTcj6kb2hqFHI811FPhFBUUidqPxhTaPhVYZXe4MwSInuZVyIC2lHKHXCZEU1AYtv6907quH2zbMq6dMtpvNGcT0dvk2AWczOAGTVwbfkWHdXX7tyvGw3m_QZFulfu5nZTFOIow0YH9ug4--pEib2CmM_VEPMBaWSvZjxNrx0hXxVI0rtQNfznE2oJnyKkSLkDh_xbQWs85YAmEyZ07c-R_j-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnhCD1ih_b0XXLpvBDIAZnB4fDiC5H8SeARPt5sTfjdSnyjh7c8SvaS22amE14lYKRALdiB1LUyndlGc7EIoSdodyk-Ix0JYYpNSTu2ESI-dyxzrG0qyzYLicA-oCr0CC2xCJ_4kEMn-oZIlH_rHa6SziBupIydZLbCPDGrTxq9e0npmBMyC-7bwNsDitoSKjVyF4qh3rNn4wd5sck8u5MRal18jsX20GRJij1ZXaYSXY4d2R4wqI2Qws0-PoAm6gdomI-mkgiGmVz2gCk-hCZaUiWFNBB9d4JBTsrXSTAVvsugLS0NYl_CdD4VS8tQuUzsNkAIL5fsjpqvLJVSu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQFMHGh9f2XcRjZTZM0201GS9VNjDc6wlTwIcWNQtdHmkfVwpqU18EFbM2YxVQWtxod_gdLtwlv4MwkiholOuUsouaLV-NBKBm26notP2TzRZs7TdwRayhpJhokIWrS5kEFOZJU7iwSNQyzCpU7kvRtVgU6IB80t15brX9WA-fmocCNZWKmxkVJGuM1-upKkbWK0_kN4HGGEM4TyZbaIF8kJOPbhK5P45CXATDBEg-sgIwk-3our1J5K7PvnnTnIBvEIMk-RB1M_yCHaGZhaVzQ_B8YRB46csDwq4E8LI5NMnnm4RprGL2gmChpSm-9yo0Z84SzgYv5W8nz6UZv8rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUuACE_m7HRfkd2wkTMTzI87qcaXAG4IjTZaJn_deM4ce_LV4ZCtQmEJecr7vX9p6FDNosamK1hz-ej8PnOg-a6Sdpw-7lZyg3HhpyEeWsHXcwPNSa2RG6Y5XS4aADta-hDNrZx92w1D6n3LlnsYuoIkaPhFUxsFDb5K4fU8qo1ewvkVQTO7rczx0SoJ3Brx401OSkXMw4RlmDLvBf8GUA_oBYtBJV2l2EXHhB6iaj0SxE7SCDH0I6X__UkFokYhT4G6jkksldoeMGLnmD4ivnerV6sE-znbMWfNTtk3axNMK9BxKlQo_XiFbk5GStGsW4EQCWVn984DevdEFj4Kdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3Nw58WW9slg4PvnFwGmwohH4NC08Anbpz3JaN7wO3jJnlVEwELJJLPtikxSoySEDyRylb6keD7jt_aXES3HuHajGScBuCdZxxT7aBnHnHf7nj0j6pvyProfumE6_hTmcLwHnJCpjHpx7hfgTfbNOUvaLTk9hJ7qUGw3KKHd29R5V0V21oiXe9lEnocwAffBLxJ1BqLOPJttpJw3i1HnrFbEMJMwkpL5aXT1SyYaDh2HeD3IRykuHjAAihDMzkqeRbYaNrTE8kb1fzxuGrOra2q25_zXgeSGj8XQWhoDezkjhdVzMZ_b7w9mdP0RQhOKYbBmtcMlBe6wtzNdYNIMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cscO5czswYo2ALIueLov6GqZW6Ey1aSRN5ueXKol8acFU2Th1TTU_JkINaiI6ZRtlqi461c_iW30bSWhA3Z5uZpTgNxoFFrYk3RX8t2vA73DPohQVXGk4VKRV-r70h3clQvsp2_qVb9x8vW68Azu_Z9tRvb6cSxIrbPLf22wT57Zv0wDitgXj6fM4y5F86PvyOmkpJNCaDhRMcryP5Q2Oka9uC6MEkklwchnJijODjKeVxpdPoBF27A4ClkShbEQCG5VQjKk962hubebiHrS-0bz02cb2hOBH9dhnUMEaSq9_NVeDj8ClZEk8Zg90iJQccpJ03Y3KSXO7BzHbboVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=IdIzENpyMXnRI5UxsFYyCxHDzznJWAGZLmNOk47jUD3FvgAJixfHccBBKPTZrfoJlHveC5ZH0vHQr4OvMlO6V41hPj8NupqM5v-IAFk7rmaVdwa3LEfky3FabF9VbwHrR7W_rEawjkNQYUO-s4yzBBao_wHitfony0CT2B5aHP2S2yj_YoeLwgYcbVS3_mnhNPVaGoboEMCf1Eugp1WOjhLuBP4RKNKG3hsxrzbwguWWBnFKRZDWpUELbOjJYClHvxKinG2y_aqynC5xRxhonkdm3_6gQ1cZSnh2pWVHwE2DgXIi1KOHhAJKhS5EGxr7fO9BsCFFpl56r14bDY0umg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=IdIzENpyMXnRI5UxsFYyCxHDzznJWAGZLmNOk47jUD3FvgAJixfHccBBKPTZrfoJlHveC5ZH0vHQr4OvMlO6V41hPj8NupqM5v-IAFk7rmaVdwa3LEfky3FabF9VbwHrR7W_rEawjkNQYUO-s4yzBBao_wHitfony0CT2B5aHP2S2yj_YoeLwgYcbVS3_mnhNPVaGoboEMCf1Eugp1WOjhLuBP4RKNKG3hsxrzbwguWWBnFKRZDWpUELbOjJYClHvxKinG2y_aqynC5xRxhonkdm3_6gQ1cZSnh2pWVHwE2DgXIi1KOHhAJKhS5EGxr7fO9BsCFFpl56r14bDY0umg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=W_Uad-sKSpUoNF4PtMqLIiloFgXNdWVPGtByJ8TNvykHR7OP_MeNPnPiGuvwV4eU-8cUBsvt5qLPk7u1EAJqglKK-hY1Oxd0I7kluaY-Wm8FNCaWkRsdSMesCegvT2vDdUQrfBLrjBBpMcOE4tBcIRQ__rEy_KcnU_Favg92gkMYGNzU6PUNZBz2a8puZAzDKLZIGAKKtK54LZO7qZn5iGhaNEwW9r2o1Eb2okwiOy_eUznvWDkkBIU93-K0KqFh8Hw9FVCm_P5Oj5KtxteZqXkVbo-rva0drKkr22bCojp8B0A25jIXQfrSDj9s_3LUoYU5zofAzaXiHK3dDj6TLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=W_Uad-sKSpUoNF4PtMqLIiloFgXNdWVPGtByJ8TNvykHR7OP_MeNPnPiGuvwV4eU-8cUBsvt5qLPk7u1EAJqglKK-hY1Oxd0I7kluaY-Wm8FNCaWkRsdSMesCegvT2vDdUQrfBLrjBBpMcOE4tBcIRQ__rEy_KcnU_Favg92gkMYGNzU6PUNZBz2a8puZAzDKLZIGAKKtK54LZO7qZn5iGhaNEwW9r2o1Eb2okwiOy_eUznvWDkkBIU93-K0KqFh8Hw9FVCm_P5Oj5KtxteZqXkVbo-rva0drKkr22bCojp8B0A25jIXQfrSDj9s_3LUoYU5zofAzaXiHK3dDj6TLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=O8zbpiJgvpHm42iRLNhcZyCyAKdaSL9uKtfLWz7wqyDOUrfKhgsjwudEwpeunaad4NXhWzIh_5WEFY5G7Ij1gr2Gb2OiG7_b_l5pov54oqYoDxlgZIY6zPSRrLpyBp2cr_VfaHRPiSSRDYda1p_iBNq2bKChRC8hWsyW3SkHhbFFzaa3tK0m7O_EHztaY1FuByVnjKpa32onjKOdJicGTB9siJs8XEuFgnERGnwmyEL1hgcQQkem7gegCtGM-M3uGDoPZtzjYieyG3Qi29QGJ077rLbPC5EHVflWX4Ri9ZXLkJ2Q-SkRn3EuW2l10SoSRUs6bObFKs_wFTkmOvzMmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=O8zbpiJgvpHm42iRLNhcZyCyAKdaSL9uKtfLWz7wqyDOUrfKhgsjwudEwpeunaad4NXhWzIh_5WEFY5G7Ij1gr2Gb2OiG7_b_l5pov54oqYoDxlgZIY6zPSRrLpyBp2cr_VfaHRPiSSRDYda1p_iBNq2bKChRC8hWsyW3SkHhbFFzaa3tK0m7O_EHztaY1FuByVnjKpa32onjKOdJicGTB9siJs8XEuFgnERGnwmyEL1hgcQQkem7gegCtGM-M3uGDoPZtzjYieyG3Qi29QGJ077rLbPC5EHVflWX4Ri9ZXLkJ2Q-SkRn3EuW2l10SoSRUs6bObFKs_wFTkmOvzMmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=T2dCrJijnyTbWLtgE0KQpgjsbpcVGxIiEwiFYX814-z74FTBS1bsE84RzIIH91-SEDxEyiIuyBnUwfOKUCjNE2xtgYqP04oLq2IZ9J01QBkH2ySmIMArA5ytmfLQIzeXWarKSIiPjqIXgLZ4eIhnowipxZOP0EY87ia65k7G2kVDB05D-fqJDvzsSY1cTXxo0hZp6jdrM6aRbytiMq-K5wAzjaiyMgJrCfIlzxWKVfqfFmBOuOAOsSPjp5zRlImXSNX3Sw5kcuuHqDlWz9wH800v1ikBEdQOm0vNeOG0kuIoCZj3s0J69mfX5wkYPse27812twXGuTKDDMnZYelBWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=T2dCrJijnyTbWLtgE0KQpgjsbpcVGxIiEwiFYX814-z74FTBS1bsE84RzIIH91-SEDxEyiIuyBnUwfOKUCjNE2xtgYqP04oLq2IZ9J01QBkH2ySmIMArA5ytmfLQIzeXWarKSIiPjqIXgLZ4eIhnowipxZOP0EY87ia65k7G2kVDB05D-fqJDvzsSY1cTXxo0hZp6jdrM6aRbytiMq-K5wAzjaiyMgJrCfIlzxWKVfqfFmBOuOAOsSPjp5zRlImXSNX3Sw5kcuuHqDlWz9wH800v1ikBEdQOm0vNeOG0kuIoCZj3s0J69mfX5wkYPse27812twXGuTKDDMnZYelBWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=LXHmN54dZLPhHJA7iT0cBqjmYn5xpKRAiUnF6D_H2SkRNVdqA3BQkbBLfLTqYBV84cjKXDnDN6oCF3dyzY8iCo0x6ne9bp6pTU2mc3Gn4RxO9kN65xzM2e5myGSlTM971Ug394aO7clL3qrICpL4XCEV9-ANmhW0IgfKdUO3jJD80EHbpVvLliKV4opQjsxvDmcQb79yXUoJUQPvDzcpygCtM6eAU_ZUvbhsuUY0CVnkfkhgCKcELpu2uVPqbFmj7A_sdPwpEGVRL7mkbLr5czeD3qLwWgAjBc-1A8YbaAbbKn-Qk6BRoqC7G1zKc6ZQDHEzf7OPHYu3Iysd7bOmqaiUjsg6HoRD-LzoK-tpVXHGZgVmheHwShusNITbGprzPCOIozhVF9Fb6gF9cIu07X-Q3ta5lruCaFrYhgbzPW7pOYNKCbckEwhANrO4dhMeb3QIdbV06VjPVL-EvBgsUIpYTxgH-G0zVMFIHaE0YjKm3fu_xi3yz54yhZOiM0FldAFIVPPChFZUF9_8RA-ze2388O0ZE6w8X_tFISOtw_BhWMaudzhpxWiXjVuaYhtqLAALRkoax08lL65uAp1pXQs9yyi23bhySOg_H9D5u1fFb8Hb4SsQO_eVM3l_AG4FnMHFdom68Oue3Ta8tTkE5nd9O6TZxZGZ5Y8_7vOgyJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=LXHmN54dZLPhHJA7iT0cBqjmYn5xpKRAiUnF6D_H2SkRNVdqA3BQkbBLfLTqYBV84cjKXDnDN6oCF3dyzY8iCo0x6ne9bp6pTU2mc3Gn4RxO9kN65xzM2e5myGSlTM971Ug394aO7clL3qrICpL4XCEV9-ANmhW0IgfKdUO3jJD80EHbpVvLliKV4opQjsxvDmcQb79yXUoJUQPvDzcpygCtM6eAU_ZUvbhsuUY0CVnkfkhgCKcELpu2uVPqbFmj7A_sdPwpEGVRL7mkbLr5czeD3qLwWgAjBc-1A8YbaAbbKn-Qk6BRoqC7G1zKc6ZQDHEzf7OPHYu3Iysd7bOmqaiUjsg6HoRD-LzoK-tpVXHGZgVmheHwShusNITbGprzPCOIozhVF9Fb6gF9cIu07X-Q3ta5lruCaFrYhgbzPW7pOYNKCbckEwhANrO4dhMeb3QIdbV06VjPVL-EvBgsUIpYTxgH-G0zVMFIHaE0YjKm3fu_xi3yz54yhZOiM0FldAFIVPPChFZUF9_8RA-ze2388O0ZE6w8X_tFISOtw_BhWMaudzhpxWiXjVuaYhtqLAALRkoax08lL65uAp1pXQs9yyi23bhySOg_H9D5u1fFb8Hb4SsQO_eVM3l_AG4FnMHFdom68Oue3Ta8tTkE5nd9O6TZxZGZ5Y8_7vOgyJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WJq73dD2azBnzsMI4gV91E1lZocOGdrQjNPgESVRmBXtIuFgIQlSeDiavXzXaPF1KDWTmAcsWqG3n6drj6ZdqvXQUJh_vgn08nrQucmQQqZJtK9ZKtmYisYbjVykIeDmKP2PtfuwZM-SAh1QnJXWESV1xUmG23uIuhvMvSfaR7cS4sdg3Aur4qp6PUlJHwOVBRbVtv-Jcn3WO-_Ecaa_RjXXO6ogiJi5SVYFA020RK4-7t2CZCdzfCmx37iHG4dhZYzKfSjgg1CaImcpFfBkgjRZa_uF-zpfLc8jvecWsmKYl20_H_piL_0MEsW1Kq62X4IYlz_iFGQHMw9x9Z6AWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhF5KiKMCnwRyNt3iKCDu8IggDnKbHdUVCHCwejNhY2aiw1Dy4XW4Jomkx_6pjSeupGLXi4Z5vL1AqlQS4OXdi3cmh7Zs9X3oSf60gpSbh7tn9gJA9Y7ROOcfrD30xnQWqlreUkIs35bdZ-2D3y6L4r1weNz1PEU0YFWh-RDUd4RJSokxhRnVetqaAmNZkBoP-vJh7thGCMJlBlIFxQQJzVyaiX-v0SioRgVEGC_iaCHCD6VpbxHDeinUXdoMfAUVRhsy4xWyS3xbOFfYPG0UReoy9q1-lm_JxKsfw2cZPXwkcCOcqdOuLf_oYYtEJnc2gAI_CidToqqxhnQ__1yMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=cjclegOYe-2kqnQGflPJoKm5FEDF_mAP-OiYefTnv_KuFJbmtSHlU9rwVFZVjY6JOD_gTb9RK3ctXi-tdmrBwTZccfcRDs6pvl36ey-W7elfHsyRqOebhUL3ScS2FU0VEj7XbtxsC_USbTDtF7JsPrHlSaG00KuBGbF4byJYxVKj9TGtAjW4e-qsdIzxQ-1RS11Y8jrppDMT162neD79BCByhVPCELxds1TLejRAp0qVCiOPdLq7LYKvUVWIt5_hgbu93sJUPNZvF63SSsqpCknR_G_OWyErTrTtsAvh-E3T4dRdY5z9dZMNDHeu5voQGio7u-oXXS3TqT9yziZngw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=cjclegOYe-2kqnQGflPJoKm5FEDF_mAP-OiYefTnv_KuFJbmtSHlU9rwVFZVjY6JOD_gTb9RK3ctXi-tdmrBwTZccfcRDs6pvl36ey-W7elfHsyRqOebhUL3ScS2FU0VEj7XbtxsC_USbTDtF7JsPrHlSaG00KuBGbF4byJYxVKj9TGtAjW4e-qsdIzxQ-1RS11Y8jrppDMT162neD79BCByhVPCELxds1TLejRAp0qVCiOPdLq7LYKvUVWIt5_hgbu93sJUPNZvF63SSsqpCknR_G_OWyErTrTtsAvh-E3T4dRdY5z9dZMNDHeu5voQGio7u-oXXS3TqT9yziZngw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=LmiSoItzbx56KQPl1lpjgzUodUIVpVUP11pYKTtULeAH5Bi1fzrq71ogOqOEKwsdg5FvPqhB2G_6zUX0mBTdF8HBvJPpjMUMa2Lr-VOPCdBj6RxL4k2-js2keJ1ifSCyEtGseQcbmIMtb6Z_wqrw8herKum75Ld4_RkQQnlcDHapt6bMubRI4eUhzFZR1GPpW7HYGVugHE0mbjjxI62bJ7xL3-59JL9mOeSX445TXOm55QmQVQX6nTnkTByLuD0KBeqvllS6fcFU04LwZwSLhKHDqiRnHXlkUxs-189tAtKWSJ2N8S-dWwng91wNp3euMmBwC2VmR9cREHc3MNpUfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=LmiSoItzbx56KQPl1lpjgzUodUIVpVUP11pYKTtULeAH5Bi1fzrq71ogOqOEKwsdg5FvPqhB2G_6zUX0mBTdF8HBvJPpjMUMa2Lr-VOPCdBj6RxL4k2-js2keJ1ifSCyEtGseQcbmIMtb6Z_wqrw8herKum75Ld4_RkQQnlcDHapt6bMubRI4eUhzFZR1GPpW7HYGVugHE0mbjjxI62bJ7xL3-59JL9mOeSX445TXOm55QmQVQX6nTnkTByLuD0KBeqvllS6fcFU04LwZwSLhKHDqiRnHXlkUxs-189tAtKWSJ2N8S-dWwng91wNp3euMmBwC2VmR9cREHc3MNpUfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=l10BcJsdEuFoTXa8QLGQzcbYWcMBzEhKkFDNdOV3JgrYv1mKA82onstBqSU5Mhwu0U4NaDszlLU6dcFVXoWoN317m732V3-T3DBjcEKr2pt7wUppSAJzVkpfZWOsFiWBOpD7rlz3Jh3TbhyJw_Jno1omCY_hkDkWPYGnKphhG2tsg-_iWpY0-_LkOzp1PkizWXyTwSdH6sEAogLoYnKIW_UtdnRxuraIybpnqA6T0PPJb3TTcp5fL4WAC0DsC5TBDDW2AI8FFS6v5f1081k9rMWheFmgZVJ3iOiHX5biP54hOD5AbiFDYiIDq97z7cPHfOxJlzF0LTs0f2KvrJa707IfJVRFJEvCrSDNlULgBPZmtnmlVxk7JHS4sBzIsMFa9n-_vSVhAyx69ZMcYzwLjx_zvSrzascc5vqMQPpzTI3XtBMnm_xCL-1pSfrfJ4pLzkSK50KjmkunlMJb7EcJebvCuRsh38oUGDBoi53sDB3MbWCAMUs6xTTQ-T0p06Whp4AshfGcW706kZLDWjLDfpXBs41B_kt-ihFo1PkJmT4i_Tsvh09PXtyw4TcsDaKwWmW_gz71UIPOxeEROVy3WXTGE3xFmnjU11AHcilg-wHMdKST5R7PdAGGXBa10LEa1OHlAqUYs6BTKFKeb0A_bFyTe77R2P3Bs2ipVM2aQ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=l10BcJsdEuFoTXa8QLGQzcbYWcMBzEhKkFDNdOV3JgrYv1mKA82onstBqSU5Mhwu0U4NaDszlLU6dcFVXoWoN317m732V3-T3DBjcEKr2pt7wUppSAJzVkpfZWOsFiWBOpD7rlz3Jh3TbhyJw_Jno1omCY_hkDkWPYGnKphhG2tsg-_iWpY0-_LkOzp1PkizWXyTwSdH6sEAogLoYnKIW_UtdnRxuraIybpnqA6T0PPJb3TTcp5fL4WAC0DsC5TBDDW2AI8FFS6v5f1081k9rMWheFmgZVJ3iOiHX5biP54hOD5AbiFDYiIDq97z7cPHfOxJlzF0LTs0f2KvrJa707IfJVRFJEvCrSDNlULgBPZmtnmlVxk7JHS4sBzIsMFa9n-_vSVhAyx69ZMcYzwLjx_zvSrzascc5vqMQPpzTI3XtBMnm_xCL-1pSfrfJ4pLzkSK50KjmkunlMJb7EcJebvCuRsh38oUGDBoi53sDB3MbWCAMUs6xTTQ-T0p06Whp4AshfGcW706kZLDWjLDfpXBs41B_kt-ihFo1PkJmT4i_Tsvh09PXtyw4TcsDaKwWmW_gz71UIPOxeEROVy3WXTGE3xFmnjU11AHcilg-wHMdKST5R7PdAGGXBa10LEa1OHlAqUYs6BTKFKeb0A_bFyTe77R2P3Bs2ipVM2aQ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRNOtkz0OSzgm-xKUPeKkqlFhH9M381sXFqwD7qMQ1D3vugnfVnVVw08gXX_3kcG1zm-Nng3pyhHai1_VKa9fMnkK4EMTQLm6t-L3zltAm0zvYiZuqrDgVF2joZdbY0uUz8fGeK-2llCKYboKOdqTJGHY3AP7izwC7b6b9X3d86iat_H4PWI82_cfo6LcoyiC9l14EZwHhXPatFwdeOMIkYuntRuEBGvdnWYESrviUxHtWXZAytf4IRcYTCYL_FfoOhAU7Zaeff2vXBd5kNnIdLv8I4NKOO1zDKK8tzvSsNdYTX_yjsgMQC6JxC1vRa1SidHMUuFW7PGzEvHG-54ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=BJC2yKnsId8pyLycvQN52BJ_5VBKQad7qUonhE79Pl-NZOi6bU40ahbYcJvfkf0kL4xxN3GzYkgjJ6Eq4eINgZqswzGTd5nmTXbZk7ATKTPXyGfQv4NRPHUj-QEWe5ICprcLjofJoucIwJGrrQxmzyRSSzkgVCJkH44UPlHmyGLGG1DKDdva3IJ6P5qqpDmZfGbm71H2bMUVZjfFFzdBobWs8xm-b8I6DlYofiVfT5yWWdaFcI23xxKlkE2A2QiNL7mdBisUgbVkp2e4z57m2nQQZmeUDmvMcLGYj9_c870P_sKiJSXy4MkIUyT7Z2wgSELqjwuXrzOKDuAdlBDvEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=BJC2yKnsId8pyLycvQN52BJ_5VBKQad7qUonhE79Pl-NZOi6bU40ahbYcJvfkf0kL4xxN3GzYkgjJ6Eq4eINgZqswzGTd5nmTXbZk7ATKTPXyGfQv4NRPHUj-QEWe5ICprcLjofJoucIwJGrrQxmzyRSSzkgVCJkH44UPlHmyGLGG1DKDdva3IJ6P5qqpDmZfGbm71H2bMUVZjfFFzdBobWs8xm-b8I6DlYofiVfT5yWWdaFcI23xxKlkE2A2QiNL7mdBisUgbVkp2e4z57m2nQQZmeUDmvMcLGYj9_c870P_sKiJSXy4MkIUyT7Z2wgSELqjwuXrzOKDuAdlBDvEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=EdGZqVU7-P4f4eETa26HJBTa0ovKDLlxzDpn4nuAeemDwiauP44mfdhM8UmFWjkhkkQCl4MR2BHBxldKuktQ5zDLwuhDt97nY5dHhGAiF4Lzi80u6rf5iT9Sn9kGdh0VMExfzqJNHQG2uDQsBnpHo67CgJPuwHkefGSxkQueBSyKQQ9es9Uy-FoLntqlyNhyP3nL-jkAj2nBEZClaxp4ubkqZjfmYoLWltw5VfNRiP7tvbVuEOKRZsset-D4YHciVqOFMhFANF_nsMtbkR7aSHhvVouWZj44sknctpkv9ksANFX-1k5LFxOf1kOnXB-sKWg0z_a-Ip20R19z55z_-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=EdGZqVU7-P4f4eETa26HJBTa0ovKDLlxzDpn4nuAeemDwiauP44mfdhM8UmFWjkhkkQCl4MR2BHBxldKuktQ5zDLwuhDt97nY5dHhGAiF4Lzi80u6rf5iT9Sn9kGdh0VMExfzqJNHQG2uDQsBnpHo67CgJPuwHkefGSxkQueBSyKQQ9es9Uy-FoLntqlyNhyP3nL-jkAj2nBEZClaxp4ubkqZjfmYoLWltw5VfNRiP7tvbVuEOKRZsset-D4YHciVqOFMhFANF_nsMtbkR7aSHhvVouWZj44sknctpkv9ksANFX-1k5LFxOf1kOnXB-sKWg0z_a-Ip20R19z55z_-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-139spRYyV5qYWkDJswNJ11jNEkh6UydXja77RcfiRoBvRsz6FbHJdRntTUlgFPBeJm9FpjSRR7CyRojoQ4OfAPOMhyRs947EC7HdZ_S3ouebAawMXO6fDo_tSsiEPaTYSp9ePBTmp4TWZi5QMxvpY4CzTuQpKtN1XfHjB13UnKQX2wdgoTCIfaPZQMxRiYwHEWkK6uzRfR1N_ybqT6vwLzjEDwfyVAzmDWyjdgJrMKOCs6m5gsgezxfBFw83JmHxVvybASpGCOeuhDOaCb7iHyi3PpFFZ_uwPbhKDEUCfBaWKGZlFMDnvmcgSXlPGcT3I0Dvu67U1Bx3aihIGQ8g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=uTwdXCXeJMR7cxj30fXPVyxA6fgCejdC224ayCzWyMLIK1MlEmO11unSxVmj_OQLNyUSaGnYtqTxcq32O9VMzzEoTc1QmOlb2EkzDhR0ehkE3k--Al_zPytwuXLtwEEGtEZ7A3sqrO81PRFJhcHG-6ZrOwtLidFlCXe_zhSNMyfAjIcBnFliGj41YlTIgR9_Dso0GFaLLpfTMoEdFMspc_B8RPVvkZ7sbqv33knNEJPejfO8o4wKbXY_wsFutXW-1eJ7GoXwD5-610rpx2HhiyOHKmmurDHcFBpFmVmWj7C4jPfIY1Dk2Nd3TnMR926msyANrdJO4KF-Vuy6eUpuzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=uTwdXCXeJMR7cxj30fXPVyxA6fgCejdC224ayCzWyMLIK1MlEmO11unSxVmj_OQLNyUSaGnYtqTxcq32O9VMzzEoTc1QmOlb2EkzDhR0ehkE3k--Al_zPytwuXLtwEEGtEZ7A3sqrO81PRFJhcHG-6ZrOwtLidFlCXe_zhSNMyfAjIcBnFliGj41YlTIgR9_Dso0GFaLLpfTMoEdFMspc_B8RPVvkZ7sbqv33knNEJPejfO8o4wKbXY_wsFutXW-1eJ7GoXwD5-610rpx2HhiyOHKmmurDHcFBpFmVmWj7C4jPfIY1Dk2Nd3TnMR926msyANrdJO4KF-Vuy6eUpuzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=a1524Ni1oX3-15v5iUcpIDuLItZY_XzBeH7PuoTqRXtasXMhTj63txz52HVujUqUYpmsyW2RulHci312DcT-cBjTkBB5Cw7KQUXhMK388xNkg-RR42I08z4XrDVC9yfmXiwYkqRNCPKZOK8kzeA7M7kzOLH63JKOXRdUyuYqlbcyZXDTIZOGTC8HddptZkG0aveJAvNY0fD2U5kwtQ2H8ApZIECYYmbL3cqKNxJRDubc7ZRIkqi4yKnp0WfsHWEGnaamvVx45G9a2qWWHRBu9q-irKta_FqrUk9mAeDv5MSXOWg4TSP23q4vJlN2zM4Tjbd6r4iCvEUAKuVqHu1sTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=a1524Ni1oX3-15v5iUcpIDuLItZY_XzBeH7PuoTqRXtasXMhTj63txz52HVujUqUYpmsyW2RulHci312DcT-cBjTkBB5Cw7KQUXhMK388xNkg-RR42I08z4XrDVC9yfmXiwYkqRNCPKZOK8kzeA7M7kzOLH63JKOXRdUyuYqlbcyZXDTIZOGTC8HddptZkG0aveJAvNY0fD2U5kwtQ2H8ApZIECYYmbL3cqKNxJRDubc7ZRIkqi4yKnp0WfsHWEGnaamvVx45G9a2qWWHRBu9q-irKta_FqrUk9mAeDv5MSXOWg4TSP23q4vJlN2zM4Tjbd6r4iCvEUAKuVqHu1sTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=GunQlUbw2tcl-6-G6iOpQWhkDngE-EDVG7UCu4PuBTuGNpDvLIgyg5M9rw613cZDmvulHKksZDisuIPcJWtpOPqtbHDDPbxkZCqbqQBI-M1J4vP3K-xLJFKbvtjxl54T4Wtdj9eIK_ydUQYkT9tp121AVNeab7E6Vyz8Y9YO7p-d4jz5EEl-Xcud-XL41AX84B0P2n1OEdjYPfxNg0thIvEzJlmNDMZRhze6PSRgbZglNk47SXIbF1Xg4x6Pps2rFNWriewUO085Fk65_TkkjA1Q2hG-pNaFDi7pCAug18TxqyDA96LVvAU2bUDDY4qiQgLmE0K37tsLTDI8EVthQVGjUYwGIacXP3KyxDYFPxqIoU6M3MKnkJlcttjFXN62nSGu8lWFjSAnFZ5aMkR2kQdh693JDbYE5ae7WFFItv5E26caL3DoT4dLq6FkK7U-ZGB0HUNAt7XHIapmqe_JuNpZApqW7xbs7vE231TmqQ4O5KRKpq6wcoa98o8JA_MRWWYYN_pkAAn18uxf0GRLFR_H_FrjGklcfKEWInqk9xT3Ll61n_mx8pH1cltxeP0UJUHRonBRdjEsRA-6AAPR2uPysF1rCeQFoTiYr6x2T8QZFqqf68-kAG00VT8Z5A7ylne8DOVzVjFPVfNCrwu65JNtSs7F1KZCa35UpLdEEc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=GunQlUbw2tcl-6-G6iOpQWhkDngE-EDVG7UCu4PuBTuGNpDvLIgyg5M9rw613cZDmvulHKksZDisuIPcJWtpOPqtbHDDPbxkZCqbqQBI-M1J4vP3K-xLJFKbvtjxl54T4Wtdj9eIK_ydUQYkT9tp121AVNeab7E6Vyz8Y9YO7p-d4jz5EEl-Xcud-XL41AX84B0P2n1OEdjYPfxNg0thIvEzJlmNDMZRhze6PSRgbZglNk47SXIbF1Xg4x6Pps2rFNWriewUO085Fk65_TkkjA1Q2hG-pNaFDi7pCAug18TxqyDA96LVvAU2bUDDY4qiQgLmE0K37tsLTDI8EVthQVGjUYwGIacXP3KyxDYFPxqIoU6M3MKnkJlcttjFXN62nSGu8lWFjSAnFZ5aMkR2kQdh693JDbYE5ae7WFFItv5E26caL3DoT4dLq6FkK7U-ZGB0HUNAt7XHIapmqe_JuNpZApqW7xbs7vE231TmqQ4O5KRKpq6wcoa98o8JA_MRWWYYN_pkAAn18uxf0GRLFR_H_FrjGklcfKEWInqk9xT3Ll61n_mx8pH1cltxeP0UJUHRonBRdjEsRA-6AAPR2uPysF1rCeQFoTiYr6x2T8QZFqqf68-kAG00VT8Z5A7ylne8DOVzVjFPVfNCrwu65JNtSs7F1KZCa35UpLdEEc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=gGF-JyhhUbZNs_-3XN5BfrewSB8_O_abUjmhXnHqYQDbxrVi5mAPJ-_KD0oGjeaMD1wjsNatc_6UnUQlwKTD1pGMVqA6K8wLVUywA6fQifutkkpXdSVDBHn08Gh3YG4tjRDfQvlXcdqHbU2qWS8kmM_voPxnq67uMQE104Ylo4C76jjI_ZYH5zx4b7plItEm1lBgetxJUKTfcohFwcgJa3pdRisN9p1ymIWJNb4Pulmhb9elX3o39RV3QTAStgkW7Ve-l2mn0Pp4b99QSGRtC-HG7pccW03-xjtC8k3ZkrCA6LFKIgrOAy3cRDbnznrsqzsJw61Rx9OFl9znJVSyIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=gGF-JyhhUbZNs_-3XN5BfrewSB8_O_abUjmhXnHqYQDbxrVi5mAPJ-_KD0oGjeaMD1wjsNatc_6UnUQlwKTD1pGMVqA6K8wLVUywA6fQifutkkpXdSVDBHn08Gh3YG4tjRDfQvlXcdqHbU2qWS8kmM_voPxnq67uMQE104Ylo4C76jjI_ZYH5zx4b7plItEm1lBgetxJUKTfcohFwcgJa3pdRisN9p1ymIWJNb4Pulmhb9elX3o39RV3QTAStgkW7Ve-l2mn0Pp4b99QSGRtC-HG7pccW03-xjtC8k3ZkrCA6LFKIgrOAy3cRDbnznrsqzsJw61Rx9OFl9znJVSyIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=Nic6l6m61O1O6gXdZDxHXFOWa9CLzVsmoqLvYPRH_Mbuv126hQwZ-BTrdUsafGA7fmbe2R38A1Wfm087snqFG_fIOaLENO4_eWKQNr2zRjyZNtY1ATOL6iIOVynPvu-0GOq26PoU8AnRmF6hF_j9p9Fet_YYxlLBs5k8D3fYNtwR-a1Kt3E3uTIVtLkNxFQ2j3-6qfNv8IeovmpSmA25Z7xldkL13aqtTxuJx7gKsxjvT36qhdwBg_UfDPR6Oy3XQnd5pisb3Z3XL5QuIMBFf6GN_97Ou7ouB14j3onurkD4JUP96QijgOzOuXv1K5COUShU0ibf9isKZWVOSZLCew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=Nic6l6m61O1O6gXdZDxHXFOWa9CLzVsmoqLvYPRH_Mbuv126hQwZ-BTrdUsafGA7fmbe2R38A1Wfm087snqFG_fIOaLENO4_eWKQNr2zRjyZNtY1ATOL6iIOVynPvu-0GOq26PoU8AnRmF6hF_j9p9Fet_YYxlLBs5k8D3fYNtwR-a1Kt3E3uTIVtLkNxFQ2j3-6qfNv8IeovmpSmA25Z7xldkL13aqtTxuJx7gKsxjvT36qhdwBg_UfDPR6Oy3XQnd5pisb3Z3XL5QuIMBFf6GN_97Ou7ouB14j3onurkD4JUP96QijgOzOuXv1K5COUShU0ibf9isKZWVOSZLCew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=j_defD_0NSXjUbSvs4ahplU9jU9OIUelXxQxDPWuzf-MYvA-6Q0dqxg01NHP7XkHyl2Lux2FksDpdK05iBuPTsMX_sNCMiWgan5OC9iV097ov0jJYzGmbEX-o6KYMaX1Y07VI_aNlhgu384Rum3cm5F3If8NB5agW_QdJ1FTs2b64kQxsojYe_kmcHCDFz8iDUaZLEUQudKs7bFsMaRb6z4RkFw3vdafMAYH6m-CVusuuRjkdzvVfCtDuozKUq9uNxib6xuu8Q7ow0OtGxhkM8r17J5kd4oxdV13NU-sDl14AC_B8Q4mZAbPheKRbky-OMszMkoA5EApOEHbHCW46w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=j_defD_0NSXjUbSvs4ahplU9jU9OIUelXxQxDPWuzf-MYvA-6Q0dqxg01NHP7XkHyl2Lux2FksDpdK05iBuPTsMX_sNCMiWgan5OC9iV097ov0jJYzGmbEX-o6KYMaX1Y07VI_aNlhgu384Rum3cm5F3If8NB5agW_QdJ1FTs2b64kQxsojYe_kmcHCDFz8iDUaZLEUQudKs7bFsMaRb6z4RkFw3vdafMAYH6m-CVusuuRjkdzvVfCtDuozKUq9uNxib6xuu8Q7ow0OtGxhkM8r17J5kd4oxdV13NU-sDl14AC_B8Q4mZAbPheKRbky-OMszMkoA5EApOEHbHCW46w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M20twwXUxXmD7PCOHVbGNFUeksXL45zYNFHjs8jiLI2O9ZkrqqWbBJ2X1ppTCtoHYy0rXrjRgQeM1YfgE_dTiYxNZTnfR1WJ64nJ4Ezk54wx6pKp1c6QyoG96TgoFyv5Pp20UChpQJWOyoDUZ5Fq-_D7wXi2NQloAtbKXP0W72BDrQsAFrk8iBinMMqPywyIIgAMLkV2x5ND9pemK4BbQntV7n2va8sRCNvhc5w3b0W4RZwtoCSkqsUNP67QLvK4TzJeKSooumwm43WavBQt8xYNIVQELRpcAX1Eq0dDuACME1EC-7psllL9ZbFWRdJBwncmZvY7ZEYJluQNCuSoiQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=kxa1ucS2UePBjaXvfL4HXnf8-_vJFsVfnldFDi5Y34HGBMUrFwhMYvNzblA3X8V2IYlyDdgLgzkrgiRYr5AADrVm_T4IaXrYWytywvAkUfVkdBFtk_1fVIoiARWf4WdqpOXWaDcCFE5hDub6f55-dCqcN0azF5kVjwf-PyRqfI15fRak6pOKshXhk0xN8NTyAFeBDPHJgMheKfo4zKSQELlk80lh77QFo5DmDU5fNmfuWddxbOeUzuz-FESRSBBVDmzZt-IHwdNwRSaV2oBuftb8yFMlBhKnuna5Wqi9m3D3vvZT042YQo6yVejFHuT5r4N8FLxXR-7zVxgi8BKQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=kxa1ucS2UePBjaXvfL4HXnf8-_vJFsVfnldFDi5Y34HGBMUrFwhMYvNzblA3X8V2IYlyDdgLgzkrgiRYr5AADrVm_T4IaXrYWytywvAkUfVkdBFtk_1fVIoiARWf4WdqpOXWaDcCFE5hDub6f55-dCqcN0azF5kVjwf-PyRqfI15fRak6pOKshXhk0xN8NTyAFeBDPHJgMheKfo4zKSQELlk80lh77QFo5DmDU5fNmfuWddxbOeUzuz-FESRSBBVDmzZt-IHwdNwRSaV2oBuftb8yFMlBhKnuna5Wqi9m3D3vvZT042YQo6yVejFHuT5r4N8FLxXR-7zVxgi8BKQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=OOhP2xv2xPtY7MYtXq0danKhVpFdxF-GuELkXG3YNRwzlhsJ2fQb1Uwa6hA1TsCYmcnvdnOR3t_pgT3OaG7J_c1zLJgDpsEhhPH8UKbTchrc0IEb85sBDXQybNzUDnO0d748w9DI2ulySckYI74_pWzBeW1uYRQtxJen1EQeDoi2LROmzAUZ4dndj3lNpDEJg7cYUps26L88VC39ZG5-WmFspI0-kqGf7--ZXt4gZ_Vq3WlOibV1mcqrHFt6XUNEhMCctq8X9zSdscYfJcU2hDSJ75ukE_AzlDgBOyaf3gnBzM9G5Wo-oXyNMpmdaTQ-diZpZPdcS6KfWdFHRpEeqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=OOhP2xv2xPtY7MYtXq0danKhVpFdxF-GuELkXG3YNRwzlhsJ2fQb1Uwa6hA1TsCYmcnvdnOR3t_pgT3OaG7J_c1zLJgDpsEhhPH8UKbTchrc0IEb85sBDXQybNzUDnO0d748w9DI2ulySckYI74_pWzBeW1uYRQtxJen1EQeDoi2LROmzAUZ4dndj3lNpDEJg7cYUps26L88VC39ZG5-WmFspI0-kqGf7--ZXt4gZ_Vq3WlOibV1mcqrHFt6XUNEhMCctq8X9zSdscYfJcU2hDSJ75ukE_AzlDgBOyaf3gnBzM9G5Wo-oXyNMpmdaTQ-diZpZPdcS6KfWdFHRpEeqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=fLKkAZeaR4tAf1OvVCtzQSkivOjUGY551wVMRYknyDp749h53N0qfzqB3spCzQY1IeW2KRLNYmZX3z7ZtcxL8JYb-h7zFCwGjzRiPG8SkREVEttJzfSh81UO1VAtXSqIlrtZXtOaPyg7WVQNMVzSBynxL9LChJZu2K6-IAUZ3hQGdo_j9MXI-lb7YZzadEH_oRNeTQXBW69uB-ZgzfZLPuvzU7G9r3L0bLll7rLEUW9-L6bnDW_Bs5P5z_QbsnWTW3e_UYd6dN3cwFW96XPTnvWUyiLGvCOL1Fk4ErcEeIHFHpKfpDh8Oq_YT2NA6MijD3MYj3H612cZqd474gkxXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=fLKkAZeaR4tAf1OvVCtzQSkivOjUGY551wVMRYknyDp749h53N0qfzqB3spCzQY1IeW2KRLNYmZX3z7ZtcxL8JYb-h7zFCwGjzRiPG8SkREVEttJzfSh81UO1VAtXSqIlrtZXtOaPyg7WVQNMVzSBynxL9LChJZu2K6-IAUZ3hQGdo_j9MXI-lb7YZzadEH_oRNeTQXBW69uB-ZgzfZLPuvzU7G9r3L0bLll7rLEUW9-L6bnDW_Bs5P5z_QbsnWTW3e_UYd6dN3cwFW96XPTnvWUyiLGvCOL1Fk4ErcEeIHFHpKfpDh8Oq_YT2NA6MijD3MYj3H612cZqd474gkxXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=VXtqIDSWmcq-eTJCeqYgxkPZTvv0Uy14CTZcz3NQPR9A6AMwLjCWcEbjRe6Tbm7lfP02eh6_mEnPZER1rUzMoyCSASy3Xvs_FY5JnzlAvS8JIIg_JAU93DNkbbSj2MmP9jE8hHKVs79j04FzdnfAlIbvoFo46Yoj5l13m4Jss9A31e0JHP8AMyF0P1HsEgCxbt4jFPU0eaW2uVtKIjBkSxdqhurhpWY-03vt3iTRviO_3p6T7jx-X5kwyYMPiBRledtUdGNF-Y5874tEK8u80y3rPv9S14GvCf722rCLgJ-9YxoabfsOE9ZmNBQIJKlz9Yu5SmkGphaU07ReDAALIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=VXtqIDSWmcq-eTJCeqYgxkPZTvv0Uy14CTZcz3NQPR9A6AMwLjCWcEbjRe6Tbm7lfP02eh6_mEnPZER1rUzMoyCSASy3Xvs_FY5JnzlAvS8JIIg_JAU93DNkbbSj2MmP9jE8hHKVs79j04FzdnfAlIbvoFo46Yoj5l13m4Jss9A31e0JHP8AMyF0P1HsEgCxbt4jFPU0eaW2uVtKIjBkSxdqhurhpWY-03vt3iTRviO_3p6T7jx-X5kwyYMPiBRledtUdGNF-Y5874tEK8u80y3rPv9S14GvCf722rCLgJ-9YxoabfsOE9ZmNBQIJKlz9Yu5SmkGphaU07ReDAALIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDItKKhQaYUMWRzRyusbm93f_ZOPe_TBPAi_o1UnCCqTVC1X1oBUs1S7O7eyd6MylZNTHLUAjz1wlmLbWNMK8fELaIYy0JT3iPFEMPuV4XGA48int25C_TKyVvPKvid2kxB-zgYQS2JZmhMJ6M3HJOwoWmCii2WEiEcWsO8VDRpJ_cmYiyxtT-8u_zYYHYIrREvCEaXfNj9D71r3ozIGvmn1UTOpO7dBlFnsCNb39SB8Mi5w_gmjJCcwirxtTLOwRStkg-dRNXC3W-M93pZpfjuXtpcwWHdTpWZJ462bENFoPHiz0Bp_nyMqhdYCU2vPW-QcsoMYV-BNGstpPWF6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxvfRPw5YHerGtd03NXIRmYmoss2Lf4XJ48uBY5IpwAFNF1qh8xTx5p3NK_yNvN9pF-y8SvUhUQ3DYsH6UXbbTNqzGWtHdrwiF3NL3Zz7CZEw3n2b0UhDv3jxInP0CqOySWrwGkn-NIvegbiwu35tC3k0JApTXx90O_MgMa_2ZUAaJEkXNC6q3nltEiUs4Wso5G_aqxM6-IGg1_xnJpzBfOYPE5xSqz9a0eDs0P783hbB_eEDvIk4uYpqqdyqAJjhpEO7oGQW1Pp7zmvgaf3qyX0Qpzjt0W0i58F4K9duH-5Cj8ArWz7PE2ybcasOf0imCq37CApc2bHccpHgNqtNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwfDnY5MP9XRlgSRGqdL2azv3aBYBP3IZxTg9cQgYaNUUmJSvXYloJG4qIQjhhJGKmA5V5-CmY4YcX6S18Pa3st1sZ65yNT1ysOCaOqe17RIVUV58zbYSFZV3U1_TMAEUm0z4CTqonx8aWg4yjlpakBbORdXLsfBAqp35IpEdyn9zu2subBeczYMH6xcRevPLgjFnQwDnO8RnJ6QQMrFYMq6i66WZR4Zl9weOC7c2dYQrasVdkzlQA03lzKD1UrZoSnYRCcfrq5E75V36RO93MhDcdhJHlWcx-hCr9CypKmgIcgOqbQVZjEQX-IZi1pmbbFYcDPohGTfZx3GgWkN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDi6NErVRTcRHv4JpZmvy5LQ-_dQOYa63I-X9SXFy6LBKUTRGuAaF3wAmjdnekl0cbJHZtBd8JMcSLt119YLJ8Ht75qAVgjIBniWA30aCNs6DwSNCFhnaIuqT6yMRmFi-dEWtiYYc94ajqJ-5QJHhrwYf-SYRdmjJHQxdwvXIlaO83wrmeNm84KUZUKxZd-CWeehrNmlixuQNChL1OWMecXsC9cMTa6dWSLm4q0ykcUCrKs7wrLyOA0MU-KJDAAGKoChEh0tSZadTRnDcgxwOZPfzxsxuzZmQm1bOJKnfrQMxSHzvSpgEsFvIh0V6tepfIHbOxdK6WPEcIwWTO7img.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Plvi99-78dTpHCo3sZBUIRPWbpb7wJsrzXigHnp0KU93nhPP4h8c1fXmD7dxT1swGFeywDCfhI9TGeMVtmYSG3z05EuykTqD3gZ1lpCvzSBSzlhBLNWVJWTEXqJ5vc0Ml88pf1h4bJVvj2AO867Y7RAVYWsnte-jD-Ri5ilSJVFROBglsXxWUgxni6ywz8tQV3u_xjLulZnbD6a8v9eI_hOrlRdxRnxg2_-AF9ovh2fHMw4MrnYmSQLmaGcp1KaVDVYGDuttUsUvaNECF9WIep2IMGnozPLno4Hzl59TJsSclGDiIw5-ejXYoI20j3rRP4xQTE9tyXRxBaHkbfZv6w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=dDpOH8bqNcqy0UPUKCXP7gcH06BdhMfFwyKGPbtn5Ss2e2RdGHx-3hWEIRnGcWH-rdqAIfhtFrM2qBsd1dDx-i7z3QwxV6FtPmKIydUeCZTevxnA-YBkYNzV2ntMpMikqrYAhgxNrkt281ktM6LZBSma1z2yslKY8CE6OCiA207rr3zSPBXTywNrfhmBm3T1ghAojNxXfvrqATZXaNxecE_0ZEnZHOj-OILzPXQwVSZl_9LtTWkBz1wOKdKOoXjZRDyIR_IEiYkzrWVRXV_ALiVntWq55HS3_6usH736WuXErGHpnXZWEg6ELEB73NN4bau3a7bgn8c42rQpL4enKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=dDpOH8bqNcqy0UPUKCXP7gcH06BdhMfFwyKGPbtn5Ss2e2RdGHx-3hWEIRnGcWH-rdqAIfhtFrM2qBsd1dDx-i7z3QwxV6FtPmKIydUeCZTevxnA-YBkYNzV2ntMpMikqrYAhgxNrkt281ktM6LZBSma1z2yslKY8CE6OCiA207rr3zSPBXTywNrfhmBm3T1ghAojNxXfvrqATZXaNxecE_0ZEnZHOj-OILzPXQwVSZl_9LtTWkBz1wOKdKOoXjZRDyIR_IEiYkzrWVRXV_ALiVntWq55HS3_6usH736WuXErGHpnXZWEg6ELEB73NN4bau3a7bgn8c42rQpL4enKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWsMOrIIZeN-XktsSaf4PLY-_C3Hfg7kJ0asP9fCEKM8GDZuc3HW6JSWRh18TbxhwUvWmC2GZR5NwZWOachByg4AMT42hJn_xGl2HPu-KDIv62p9W2nzEZ4Yf30-8U8OMdc26In6be_DdWKQ_o1J7XGzr1Hu4PIGGb3ZoZrvR3rLEY3FPm7z48BNpdmDpDSRm2qRvde6qcWo554cXcMTB5fm2njHofXuEh91-562bmJLMRwq04ZvaXtKcJNzPZMK9LDL2VRpNyErkL7OMQDdwTE0SMErQ0-olWDIVNNYq3Gjv8KUXPCUSluEQv__VTpxuOjR_TIUvnnOsu5TDD10Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Am8HAjFsvPSOH0rZYjfPKQoQs3BXw4i0fe8A6B2uYtUqaGKyiqp41gWmsDNNa15IfSBPTkVjCvl26PqRgKmkaaACTy1FuTTbopwTEwFpR5D5BwqM3seSAzL2c7ragJcpcdQJo1G4CYSLmiLp5QBQ6UeknG7Z0wVdjZkD69IuG3CyAasGysk7NmJR6b8PpDrV-O_7AP9wyXHJqIteE-UbzsChGsJwo1qDJfxso_QV1SveV9zKUvIi1KR3EXMp-3eIUEpgrFKbWJuFNU54DMv_t7EB7vNZOxC5c9drLBJu2uZa4be9_TLQJhRYDNOv78p7dBc5L4qgBqCpiSapxL0VhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=JI2iEEELbOFJBn1u_nn0_Xusx9Xf9KLlExMrto-bOVGRwD9M4v-d5TDmOw9wuvZzlmu50SEkz0L67G3s-V1GuG4B_9IGqWZ6wO8peDUMHaNgaO6sATZ9K-mPAX2t1_fZlSesBsXbjBRraPhJvHRuNS1DWloflwOsNfaFznJJ_xp4VjC41PI-wUa52ntGyCs83F1B2VtUTU4euD1r7iTGD51dl3bR5YWsF5_2TzGDvJCiZmdn9fZVUROldDslMZ7z0v9Y5XpsFqSOtKm1H5fWe7B6sa86KYacgxOyC32xW_d7V3a9WWt61SDMR_HCaICGjzwDEeBpGgmAknTVnfM4dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=JI2iEEELbOFJBn1u_nn0_Xusx9Xf9KLlExMrto-bOVGRwD9M4v-d5TDmOw9wuvZzlmu50SEkz0L67G3s-V1GuG4B_9IGqWZ6wO8peDUMHaNgaO6sATZ9K-mPAX2t1_fZlSesBsXbjBRraPhJvHRuNS1DWloflwOsNfaFznJJ_xp4VjC41PI-wUa52ntGyCs83F1B2VtUTU4euD1r7iTGD51dl3bR5YWsF5_2TzGDvJCiZmdn9fZVUROldDslMZ7z0v9Y5XpsFqSOtKm1H5fWe7B6sa86KYacgxOyC32xW_d7V3a9WWt61SDMR_HCaICGjzwDEeBpGgmAknTVnfM4dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=V0mBIe2MJmeslnxcZ2Qx83mESXHBK6GYE1oLxdzddUhhPRgqAgu_bJLtWeNvPupfn9HyEyC8I1YVTHSLmMLxnz8j395JIktFWykTHXV3r1-e9HQ4lTcr2Xn2nOEAiaYs64Xr53DYIZP8toWXdAP7C_Ow8Ix4vgntXr1uxqiXF1t84kgbKKCl60jd883XCi8I2b_XQ6kmtYQGmO2z2JksLGAwdylDLRxPfR1rc5G1N9XhNcl8O55BGp5wKu8gPJlfE_eGzFi1sFlVHYqbngLSWiSVuDITW9Vgj7GzZy9ehtdy8DzKKwdSpysZ8vl0V2gg9JVbUwFYtg8vznqRjvYQBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=V0mBIe2MJmeslnxcZ2Qx83mESXHBK6GYE1oLxdzddUhhPRgqAgu_bJLtWeNvPupfn9HyEyC8I1YVTHSLmMLxnz8j395JIktFWykTHXV3r1-e9HQ4lTcr2Xn2nOEAiaYs64Xr53DYIZP8toWXdAP7C_Ow8Ix4vgntXr1uxqiXF1t84kgbKKCl60jd883XCi8I2b_XQ6kmtYQGmO2z2JksLGAwdylDLRxPfR1rc5G1N9XhNcl8O55BGp5wKu8gPJlfE_eGzFi1sFlVHYqbngLSWiSVuDITW9Vgj7GzZy9ehtdy8DzKKwdSpysZ8vl0V2gg9JVbUwFYtg8vznqRjvYQBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=jy6FiiD8QGg3GVTNlzbrZVRZncEI_i6okqUmK0SgicthwpSgRcKb8XFdiR-3HNijARmzZc2tQPFiHDZ_3W6tTQiIgyJwopvL60Oxlv1mayvci_wcatu3hdBlnmN0JfF8hIr4vnZWUlPs2tk-_dZr_vEgzF0PyXNAvmk1hAfZvmjph4gLG4u8HagvHECWXGTTow5E9BPvVfOEEBi5Yyav9bilCZqAdMoRFK0oFS_ABuKfVs3m5_7Kvo-1funfxcmdAoBxU95jIMoNfCoiy8JtokrW7Mf7RUuDzFtcanUQ4F5LWQEpAHtK7KYz30rpMxt1hyhFRzxRv9oRcsmlVvN1zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=jy6FiiD8QGg3GVTNlzbrZVRZncEI_i6okqUmK0SgicthwpSgRcKb8XFdiR-3HNijARmzZc2tQPFiHDZ_3W6tTQiIgyJwopvL60Oxlv1mayvci_wcatu3hdBlnmN0JfF8hIr4vnZWUlPs2tk-_dZr_vEgzF0PyXNAvmk1hAfZvmjph4gLG4u8HagvHECWXGTTow5E9BPvVfOEEBi5Yyav9bilCZqAdMoRFK0oFS_ABuKfVs3m5_7Kvo-1funfxcmdAoBxU95jIMoNfCoiy8JtokrW7Mf7RUuDzFtcanUQ4F5LWQEpAHtK7KYz30rpMxt1hyhFRzxRv9oRcsmlVvN1zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=bDXsNjcUFtozFYW0u-kWtAkhL0k7pZoRc5s3EVjXo922sHQIJxHb89NPHWyZ5Az-SedLVSkj-_EmCdcEQOwWI8aChn18Q3jX6HDGwapnoa6YoC7UhTIJVN2TscBA-HaawexaayEHpLiHH-NJ5BfSVPEJI0UNRlZ8iFNF4oPq0zpnqdvU00c-tJZ8nwBy6Jh-y1Y_Bgv83y8rltDRIYoMkL_7W7wT4j8NV77J3vAQyPnPnUwf0AonejM5Po9ZUGO5Ir65ghOzvdgAZAbjJcBm06QNHpTMs3AnN0IQ66rOMww1FBDWZwovY7X1agHeacmT7-1WOgYUc7_khJNNDg3DDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=bDXsNjcUFtozFYW0u-kWtAkhL0k7pZoRc5s3EVjXo922sHQIJxHb89NPHWyZ5Az-SedLVSkj-_EmCdcEQOwWI8aChn18Q3jX6HDGwapnoa6YoC7UhTIJVN2TscBA-HaawexaayEHpLiHH-NJ5BfSVPEJI0UNRlZ8iFNF4oPq0zpnqdvU00c-tJZ8nwBy6Jh-y1Y_Bgv83y8rltDRIYoMkL_7W7wT4j8NV77J3vAQyPnPnUwf0AonejM5Po9ZUGO5Ir65ghOzvdgAZAbjJcBm06QNHpTMs3AnN0IQ66rOMww1FBDWZwovY7X1agHeacmT7-1WOgYUc7_khJNNDg3DDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=mayhBq45DByrDWTmb9KFuqQ8d_gEsTapxxHbjy9VQAjC0iFd3qVEFyabcTae5n_cxViOi-dWkc8CJUmduSqVfpap5APBZX0vpqzWmXvaSPVbmBKyUwElwdGNLkjF7y9OKoWTMfYe7VNzO1LBdvmUxC8WXgmI6mAW_qdOKHvme0zdfNFiI7OwQXMeduQ7su15jeNmVgpk7NzcFaB2mux6ZiKr2xLLjuGgHU1nXf0U4ZG-cFxXmb3OPH0YgYD3v_3ED618ovyEwaXIg-OQIxpDQqqmK7Ry8-rlJvixlcnZxUrWRWXRbN8Pav1s7JRZAGPQEOwFOuNaQw70rsVRa_vLYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=mayhBq45DByrDWTmb9KFuqQ8d_gEsTapxxHbjy9VQAjC0iFd3qVEFyabcTae5n_cxViOi-dWkc8CJUmduSqVfpap5APBZX0vpqzWmXvaSPVbmBKyUwElwdGNLkjF7y9OKoWTMfYe7VNzO1LBdvmUxC8WXgmI6mAW_qdOKHvme0zdfNFiI7OwQXMeduQ7su15jeNmVgpk7NzcFaB2mux6ZiKr2xLLjuGgHU1nXf0U4ZG-cFxXmb3OPH0YgYD3v_3ED618ovyEwaXIg-OQIxpDQqqmK7Ry8-rlJvixlcnZxUrWRWXRbN8Pav1s7JRZAGPQEOwFOuNaQw70rsVRa_vLYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eq4T6dcsciBh2Ab6PtKj5xWLak6pcfSFQQBjRqRi1vBqGDVZIy4cP9tUsC2ndBIPXWNytyCPpL7DgUdwt1WNaYm7IiN2gF_t9Jj_YwUNscjR9lFZKAfetSRxlcQoHz_l0nyue_rFPiLVHUta_uQ_KGR2BGYA-NFu3zSZ5ililOFS7Kt7yVIaIVJ8nHLKBU3ygCXzHVoBoSCzBq3CjWIADnAiygbrmbWhm_JwfrTGDskkgaRcI5y1hgBkJ62W_0Rvq9jYQ8YDPSaqMJBI9nnfJi2TTDXXumoLRvymDEfVwCVSxk5ioIVNbU1Od8Tx27co3Ld9mDHAn3saGNcygSlHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGMpH9H-WhlTrBHC0LysB_IjUwa2V4i83yPnnrEz_n-ovLIZ5bTIJb0ur3xrx3tdQavAr4htTW9Bpn0zvh83qppyrQ4ilvWjfkOZZK_56zK5vOJzk7hvh4IYjlmmKntT0wwQJNNjnSae_KCKBZu1iw63PsTY8_gNvzbj2o62_ybosx1-FA8PjpyadXMVSs4OPmJV0TAo3MOw0yi5z60TfH39GH5USo74wMoThpG64FfNirXyA-gs92PsDMoNtwmb2QJlmhUlToNDW1M8INvscJVudBvkDosfegralYFoCaojw-mV4npi-IYnDl7Cb6dyUIOMcvl1mljpabSnjIJm-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NmhxWWj8qi49Plh70v3No-qL28CeOoHIrqIq28pnG4y7gJ8xaCRy63zgoAZpFxUyZYGNtvlvFHX43-Nz7_rv7Ojdkwr8jdWLZyFHgFAYAIWBvEeWcq_Y48RIy-NkYjLEBONVPpY95Ygvmuvf7zE5org_fj0HuDuLFOzr3oU1ppx9g-Yy6eLPbYlGckHtLmzaZH25eZo1P6Udg9gcVtlL4R7hfUl10fkhJAu25COQR-idS8FhnRBVM1nJ7LKidC8jpBqCWDlw91SrOpwlnD2Xe8orpCNfg5qbkItGzqsWoUq2HQPkUsXIRi5gx7Y4szaGJCeu5iyXu4xhMYkIj1ut5Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=cM6sQUOIneEKVLlqBy_dWSEA70zuYba4UMHfODoFIo7tcHFbRJwvr5fO0UhCpCS4kGU04hly0nxpEXkJIZe9rTqPC0WHUUsvwIQy7gB8_ajf7TWmCfSk-spW5sdAzMdqm3CLpklfp2xghyXab8crD9VuHuqUPoqQPUDEKZixeyC9g9irpm5lrKARz1PnEuECS-N-GE3IDQ7QcwYEGffWgeE2G4ot_420dvcovDIZ63zQZGJEo6OcIbdIwotSWIhwY4OeorbaPbBndFyo1ZoQn05Ow152tmXh-7p77cGsgAgajHYawcVgyL2D3n5Rln4DS2DEnf55hzFtyMA4LKOE_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=cM6sQUOIneEKVLlqBy_dWSEA70zuYba4UMHfODoFIo7tcHFbRJwvr5fO0UhCpCS4kGU04hly0nxpEXkJIZe9rTqPC0WHUUsvwIQy7gB8_ajf7TWmCfSk-spW5sdAzMdqm3CLpklfp2xghyXab8crD9VuHuqUPoqQPUDEKZixeyC9g9irpm5lrKARz1PnEuECS-N-GE3IDQ7QcwYEGffWgeE2G4ot_420dvcovDIZ63zQZGJEo6OcIbdIwotSWIhwY4OeorbaPbBndFyo1ZoQn05Ow152tmXh-7p77cGsgAgajHYawcVgyL2D3n5Rln4DS2DEnf55hzFtyMA4LKOE_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkwC-1VCNp2kYrfp76oqBrz0goYPuzVFe-KAITNCaJjS6rJW1XeRZPhcZsFahYzG5uc9oOZoClIDoYVEt8jyFduOBJnk4rCT16MNwPSOqawJgFzeTYBTMJp1UchPYLVLBGdrL03MgcXrMPja4fjS1VHDeS5QcXHAyaO9VGZK2IeU3XlSzMf8g6kMhd74g7xoJiJSjs65FqwRnmBTsfg6CoawNuDcArIwrD_BJvjATgUbKEPc4QPWLMdwm10bOK5p6l_8pTbkhPN4SCjdJcmss2Xghdr2SVULwHCcbLa9Z_63W1jQTCyRx7wX9wMx7q82d22UkQ5jR1qBQMukaZEFBA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=TwmZuEatNQSyMnC3-y24uwF4EemBWoMuht4_B-Ct6zhyb0mqqZSH3eMuMmjB5WeZxtpZz-_Q-9mN7YfIQ29N4HGleEVuAPo1OAZ0Gjkm6sCHg55AEAtF_Be0WKS78WdJgm3kxBSwOCHFOdsTtwQUnn8sMWCKTFYgHKgxWmRV4i3LjvkPQ3a0Sb5w_fnVYxZizAR1lQFJGUbZ7hQhmJPayiaHXazP7Cea0wpsd5uKIj4VDn4oRI-RiqrQlXwBfh2Xtq9XfLABltq_BaUozEZHXT6jnfYr7ntaAUv9byakjaHNwYcfyKckys4fpdJt77PplY5y6acZBU13C1jN1876hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=TwmZuEatNQSyMnC3-y24uwF4EemBWoMuht4_B-Ct6zhyb0mqqZSH3eMuMmjB5WeZxtpZz-_Q-9mN7YfIQ29N4HGleEVuAPo1OAZ0Gjkm6sCHg55AEAtF_Be0WKS78WdJgm3kxBSwOCHFOdsTtwQUnn8sMWCKTFYgHKgxWmRV4i3LjvkPQ3a0Sb5w_fnVYxZizAR1lQFJGUbZ7hQhmJPayiaHXazP7Cea0wpsd5uKIj4VDn4oRI-RiqrQlXwBfh2Xtq9XfLABltq_BaUozEZHXT6jnfYr7ntaAUv9byakjaHNwYcfyKckys4fpdJt77PplY5y6acZBU13C1jN1876hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=R2_bDsC_E3NJ8D9CdjSXtu1mF2gtErfiE4TchPmOAZZN-eEbiOSL-Dj27M1Bcn7wn6-9aUTRO3Xlyjz8DEdLEk6tQZ21afSw5V75k_5wRpwJP8Bcl1mekWsu5k0rl5EBaurTsk_XSHfvREkHCEvPjRGnFwZ57eKL08rg8fJY7aFZtN6YNmUJrdUy2ufIyyu5ARJd69NyqELSNrtsqG0zKtFAx0Gow6Llz1M3KONBnQUG9MPlVoREYV99Wcnmaaj9yZaXdckw7qq1UhxeBlXeLp0OyIC3czoyNZERigyWjSxvDMwv6UZmoUYGX4u-64jtb4amzC0lmJrOOSq0z2duTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=R2_bDsC_E3NJ8D9CdjSXtu1mF2gtErfiE4TchPmOAZZN-eEbiOSL-Dj27M1Bcn7wn6-9aUTRO3Xlyjz8DEdLEk6tQZ21afSw5V75k_5wRpwJP8Bcl1mekWsu5k0rl5EBaurTsk_XSHfvREkHCEvPjRGnFwZ57eKL08rg8fJY7aFZtN6YNmUJrdUy2ufIyyu5ARJd69NyqELSNrtsqG0zKtFAx0Gow6Llz1M3KONBnQUG9MPlVoREYV99Wcnmaaj9yZaXdckw7qq1UhxeBlXeLp0OyIC3czoyNZERigyWjSxvDMwv6UZmoUYGX4u-64jtb4amzC0lmJrOOSq0z2duTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=I8VJRgDxjku7e1UfrpwDk8HFtDYGysoFjyiaVAOse4DHIxOCr2FGkWT_Q1E3UCQXllgBOGZUwarq-8WoGFHR6CXMeaGquaLkPys4Tjv444zeR8WS8LFuRalFFia-c27ZiXMrOOmoNOZIq5hqFgV0TOGwIo7t4ArjS9-ogOL-nJwstYQnEcTpy9-CcZfVlu14gr1eP4qNjJFMAZ9ikjler1LSvnUz4DJPL2mjTstwdEtymMmEQhCcJM7huLTJis1stf3D69egficr1GjENrmcTqUtI7Sg-hrO6y9KtNR2qA2JWUH8Y6Shl8pVhpEdjt3OTNC6tbHzGndh0AaWZ1pxAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=I8VJRgDxjku7e1UfrpwDk8HFtDYGysoFjyiaVAOse4DHIxOCr2FGkWT_Q1E3UCQXllgBOGZUwarq-8WoGFHR6CXMeaGquaLkPys4Tjv444zeR8WS8LFuRalFFia-c27ZiXMrOOmoNOZIq5hqFgV0TOGwIo7t4ArjS9-ogOL-nJwstYQnEcTpy9-CcZfVlu14gr1eP4qNjJFMAZ9ikjler1LSvnUz4DJPL2mjTstwdEtymMmEQhCcJM7huLTJis1stf3D69egficr1GjENrmcTqUtI7Sg-hrO6y9KtNR2qA2JWUH8Y6Shl8pVhpEdjt3OTNC6tbHzGndh0AaWZ1pxAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=Z-1scS5bZaoEVsL-aipJ-2HMitjkVKej4S19WEssHkcucK32nazBpefydPuQPam_SW6zRunNUHNpC58IsMEYyHPD5djmrpnKbfQTtS7NMS1NppuR_m8L99gyrQW-ZudDRb9C-o1pEzimdYg50JuqxCDIsSSA0ObdASLkzmvggKYF9mP2Od1p0My2RUIEOQecrh6oDQtiQH86u9xo98Xynyw8M74gdwCeEnVftT9h7vaWYJ-PGrPgS9d395LN9e62ldpsD_qPhTDu0b8n-1M8CQNNM4_5oVLapmrpNmP9II_qw5j-pM8L7Wn4Dg8Tv_TNuh8pXq0FR7objV6St5AZZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=Z-1scS5bZaoEVsL-aipJ-2HMitjkVKej4S19WEssHkcucK32nazBpefydPuQPam_SW6zRunNUHNpC58IsMEYyHPD5djmrpnKbfQTtS7NMS1NppuR_m8L99gyrQW-ZudDRb9C-o1pEzimdYg50JuqxCDIsSSA0ObdASLkzmvggKYF9mP2Od1p0My2RUIEOQecrh6oDQtiQH86u9xo98Xynyw8M74gdwCeEnVftT9h7vaWYJ-PGrPgS9d395LN9e62ldpsD_qPhTDu0b8n-1M8CQNNM4_5oVLapmrpNmP9II_qw5j-pM8L7Wn4Dg8Tv_TNuh8pXq0FR7objV6St5AZZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW8kFmxX3y-3lx4ocZKlL5HEFJnDo2CrWFLUaBEVWVkCPrM_lUdpQgypgo7ouXf03XuY1ZxT_59RPtcnqmuSdTCyJmj-HC3HWq_jgmwOxvaKPKMgx3YVc1vMFElube1s26cyjRVqIZn2AFxz8VY7cBDQr5UHIcfSJQda5nz6vs-7t2OUFXfu9fOefAiMEF0qcOSpu6nr6ZZJJepHgoiL3OYMbTpT8wgsLWPHwqUQXUtBvtHYmKLN2a5Vnj76Pud0t5eyCAvluullzErZmGJ_FMFN9-Bt9RUGvxQwR-wEb8Itoa_zqCZeI85RAusZ-4KA8Uj314C8sktcgSl16OSEsw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY1IEgLWpUr-Iegd1-pUvJ83VNjN57e5VbKQtek6kmLaOM3AlJ2sofnCUijGmrxxqszWh4sHWtlwBZjde-e0HbLbGhMVPThBdd-HE-W2-cwIuIej-fzkeYfEVqcSKRxqI1QnuVFzB3Z3FbOxbSCmtGCInH8YFFP6UDgBDEpzcrmFMM5wexXLTDmQidQYj_bC7m-ChLbWF1blb_V_wo3_adTLt6eaMkD8mN8iCkg7xEvtEKLbjxo0AdjnWpj7EexltaIVpd101IgNE9mXB2LdiGWSVcTqd4eVjlQmALGRmgLl7PrlhqR5do5NVpQhXxz1E-mGmBY_TJs-LfAeXLZh8XrU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY1IEgLWpUr-Iegd1-pUvJ83VNjN57e5VbKQtek6kmLaOM3AlJ2sofnCUijGmrxxqszWh4sHWtlwBZjde-e0HbLbGhMVPThBdd-HE-W2-cwIuIej-fzkeYfEVqcSKRxqI1QnuVFzB3Z3FbOxbSCmtGCInH8YFFP6UDgBDEpzcrmFMM5wexXLTDmQidQYj_bC7m-ChLbWF1blb_V_wo3_adTLt6eaMkD8mN8iCkg7xEvtEKLbjxo0AdjnWpj7EexltaIVpd101IgNE9mXB2LdiGWSVcTqd4eVjlQmALGRmgLl7PrlhqR5do5NVpQhXxz1E-mGmBY_TJs-LfAeXLZh8XrU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=JjkoceA-4rDmWrFqUJo-BsNrEgoGwVtuvyxDynC47VoFwGL6JEOevA8rlaK72xAtXtIArTMtxVfavLjzl3Oi-mbwWcpbpOoVm9Pc0fMb79yclCNZE0H8pHov90yqwiV5ZEXdBTBezKRbDf36jd4lmA4w0a2ld1Qno5J7q9KwSgjqD0Thvb_OAQ28JQddpCUmm8OVl9GB0P85ldp4aAGYlT2GWtLJOfQnGsCk2hz4PWiYHQhBaSl3aoqekFdPfYiuQAtYGi_KtUApEEe37cWyJyOSO5aSAavI9Nhxwcqjt723O2-RUrPmFg6zpAfsTFqW7h4MtMxpldXzzrBB8h8H0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=JjkoceA-4rDmWrFqUJo-BsNrEgoGwVtuvyxDynC47VoFwGL6JEOevA8rlaK72xAtXtIArTMtxVfavLjzl3Oi-mbwWcpbpOoVm9Pc0fMb79yclCNZE0H8pHov90yqwiV5ZEXdBTBezKRbDf36jd4lmA4w0a2ld1Qno5J7q9KwSgjqD0Thvb_OAQ28JQddpCUmm8OVl9GB0P85ldp4aAGYlT2GWtLJOfQnGsCk2hz4PWiYHQhBaSl3aoqekFdPfYiuQAtYGi_KtUApEEe37cWyJyOSO5aSAavI9Nhxwcqjt723O2-RUrPmFg6zpAfsTFqW7h4MtMxpldXzzrBB8h8H0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=Q-fO9Btebow7seBzlykGydtii2JoVYrDhSquvxPclenjlsN5S2SFJlm9CPKzWhqm5bQFFiwE7vaeetfez3s68KEjP8LS_E22lgiqEuBvz2tmAWzQZ8V35rjbcaRgmkQixJtesnf4OM5HIV8kFeONoMzU4OlUAz0bOVAno_vWLPDxXA1Q41n3BLqmczLc-s3V-zCCHWVtUI4aXVgbgmrwGhjyLmhhpQKoKQ9aXMsmcv0pezS0n9XLKqF234uIcY6id0dFeboMgwwF9TlxO41azy9PKV3PmmAIE0Joq5CiSVNBfWxUGTtO6O0eKiFautXaznofHYCCOiIXGOR4TTNcfnmMkjvWssoAME8mzD-oZVA0ICNxceRwiM5o3Fx5jEW10OZqlGhfx30cYN6RXWelPFa7KxxCje3VC0EQ_ayM1zs5VA4wDBTCREqqGiHQym6p12C1_530-eYu1rq5LvHsPmH1ymPB_86wmC_g5ZCzL04s7FXMT-YzdGOurvAi0_O9vZ7OtdZv91L90aghLTs2Sk2FOXOXlac6K-rmKwlLCGCuMywzVG-Yb_gR5qZXO4LkI4PwSctT--JjIi0g1ZZLWJoaNSWeSsJldhcm0UodxScr-OoYSxuRAttQtwFFYR1IzonELsgQqgZ-6GmovNB2w9XAE7AwkulThy3K333FsM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=Q-fO9Btebow7seBzlykGydtii2JoVYrDhSquvxPclenjlsN5S2SFJlm9CPKzWhqm5bQFFiwE7vaeetfez3s68KEjP8LS_E22lgiqEuBvz2tmAWzQZ8V35rjbcaRgmkQixJtesnf4OM5HIV8kFeONoMzU4OlUAz0bOVAno_vWLPDxXA1Q41n3BLqmczLc-s3V-zCCHWVtUI4aXVgbgmrwGhjyLmhhpQKoKQ9aXMsmcv0pezS0n9XLKqF234uIcY6id0dFeboMgwwF9TlxO41azy9PKV3PmmAIE0Joq5CiSVNBfWxUGTtO6O0eKiFautXaznofHYCCOiIXGOR4TTNcfnmMkjvWssoAME8mzD-oZVA0ICNxceRwiM5o3Fx5jEW10OZqlGhfx30cYN6RXWelPFa7KxxCje3VC0EQ_ayM1zs5VA4wDBTCREqqGiHQym6p12C1_530-eYu1rq5LvHsPmH1ymPB_86wmC_g5ZCzL04s7FXMT-YzdGOurvAi0_O9vZ7OtdZv91L90aghLTs2Sk2FOXOXlac6K-rmKwlLCGCuMywzVG-Yb_gR5qZXO4LkI4PwSctT--JjIi0g1ZZLWJoaNSWeSsJldhcm0UodxScr-OoYSxuRAttQtwFFYR1IzonELsgQqgZ-6GmovNB2w9XAE7AwkulThy3K333FsM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=OV0TDvCcpMD6wmS62iyIoS8NDsmKCfnkPMJksIh-zrLQ0Mo3ZPyxJDMf81uqxJA2tvG5FEkrrLHiSHz5taSWSBwfIxz2B_gRGxE16iEzwoA9U7ANFyCCfL6pz49F_nSJRKRqs64vB26nvI6ACv-ai5qRyet7a77hyCQUja-H51yqdbxxMzA6C31zYB5NqYYgJq-lP7UuXnc-HjfHx-3DRELksPZT9PZSO8XxhCHt_cSNmRIlnmhQWJUjcPM7I9WKmo9c3OLLxNoNWSlYOShGM_onuJXbAhjQRRwNMo_ZvknTUdIHhZ20QdkhdzXeEOhgeT1DPV0vvcGQH2CD_4ZXng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=OV0TDvCcpMD6wmS62iyIoS8NDsmKCfnkPMJksIh-zrLQ0Mo3ZPyxJDMf81uqxJA2tvG5FEkrrLHiSHz5taSWSBwfIxz2B_gRGxE16iEzwoA9U7ANFyCCfL6pz49F_nSJRKRqs64vB26nvI6ACv-ai5qRyet7a77hyCQUja-H51yqdbxxMzA6C31zYB5NqYYgJq-lP7UuXnc-HjfHx-3DRELksPZT9PZSO8XxhCHt_cSNmRIlnmhQWJUjcPM7I9WKmo9c3OLLxNoNWSlYOShGM_onuJXbAhjQRRwNMo_ZvknTUdIHhZ20QdkhdzXeEOhgeT1DPV0vvcGQH2CD_4ZXng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
