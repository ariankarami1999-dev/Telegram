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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 09:52:45</div>
<hr>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3MpCKVVrx1PntTNygC3Gt4JlZE2kIm26wZ6Z5dhDpwehE1TrdQZtUAIf2nKcq2cReCXqLz12_1fWi1kWZSfPkj4DF78i9WdKWSCmBIXZUoym7FJBKQLODNVt70vcubZA21NB_9EOhXBbZFCQI-mgV_wUnwM7oPTVj177HEZZieRA7cnC1lNgQhFSoj0yGS5-9eiC4hpeN8kz6fWtc8G6hi-9W9SrCpTMim0TBL24q3fon5F4YtVN9BXR8M2ltgZ0xRPOApd4T9zP8JO2I2ht_t2P9Uj9FF7gm1ErXGzJJQ1AKo2QYOIBxriA1TG5RS5WgurOX7iCE_xUFHCrROFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=EcnLGljOrgt6RTR-0SwNwYsuafcJj96IAL8y_EYFMxGMVByJt1PwVVUgROc_ZK0-dzi8VVmRT2SgLqKk1nJNoVc9SluGekMMDuHAx5sOWWMbmWZsEc3curm_yrCxBItJAIgD7NYyuSHstwAFezhr971mOPTdDCvXoIkBZssgUaXetmJ9_D_EmBN8mV9T3b93pQ5ZI6c2DeHquHReeX0swkGcC3JJaw9Xp02bwgGN_r5pVHP7H9qr_DeuXErutwV6xQxL8QXHFjZmaTlHjgSMRfWUYiXO1isp6pMDiIVBBJ_T_94U9GD-UkDlR61NwpYezJRnfmOCeU0XNjzUk7HzOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=EcnLGljOrgt6RTR-0SwNwYsuafcJj96IAL8y_EYFMxGMVByJt1PwVVUgROc_ZK0-dzi8VVmRT2SgLqKk1nJNoVc9SluGekMMDuHAx5sOWWMbmWZsEc3curm_yrCxBItJAIgD7NYyuSHstwAFezhr971mOPTdDCvXoIkBZssgUaXetmJ9_D_EmBN8mV9T3b93pQ5ZI6c2DeHquHReeX0swkGcC3JJaw9Xp02bwgGN_r5pVHP7H9qr_DeuXErutwV6xQxL8QXHFjZmaTlHjgSMRfWUYiXO1isp6pMDiIVBBJ_T_94U9GD-UkDlR61NwpYezJRnfmOCeU0XNjzUk7HzOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHNBOfObDhohgiOJ2eTtJrHwocUrIerEjuSUK8UoaoxldZT1ILI6I_-J1ec5dAm3iT04duOiDSQ-5jhTbub-inkfW8n7r56l1_IaBVr4NTqzgm2CbNrK4umla_Dg-KNWy31yoCw-jvpaYSIsioMGApnSz98ySp-Qtj97yW4VJGGkb6URkAEEadKw0cHdqbaB7PwI7b5PKx2OHfoPMWPBoGSHmEGqP_QkFJzD5P_AJdQRjuNqJP9IdE6L8NhlSDnFo4b2P1jzKdiZI9TZPa3qSgOO2mI4DrTjZIpjJn4izOAKHXQAS5oUPi1Oehd-mwIRnAI6CoAA26q-QmrN4wtVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOuMgUcNhEA2vQq2LfW_K5o9h8H3Nz3Liv7rmjnyDYkSSA6sN6qsT4bKhGyUKHyV5w0du8_I1_Qphs50pfSLDim7jnATibj3nSHD35aNnqZoWRohesqFlgGKwBCRkDXIXHJSa8CsmBwAIaCG2He1CiFhfOylU4IL4uJ4WkYSMET6pTX3F9sFMft50r80ADushpFG86zQs87fQMXFb_Xz21yjsvZusTrV23ZC4mTH6A_y3qGUEeSrXizc-85ErXHU5mRkwt470so76IOxg-bOLD_nwIIlMRo8G2wTcGDbQozsvRJgj6fwk6hD2fmxcFvi3HIdozi7fqyZlF2qo8q8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTQzLW12fcu_3tWKsVQa9HXzX4CchRGQgUhEbfiwPqosOD18R-ABbvvfcNGM6qdBnepHXhIOCA-cf2BoFQYckPz74Mf46InfqMX7rheGDqhJ-EI6LGpf-AfEkNhLWxiykNH98GdxdM5o1PygHzLNho2UjvgEt-Y9bqDpAcntAqws4-UdlxUSVmUhGbrTv4PjRdDH2sku22gNBAdWU6ljetXtXEa_kh0hPpCtBgIM8DofPpZlJi1nuzst-tFa1f8PuWGsEgb7VzNRJAC_4_Qyn1aPiPWdS3uh4jpkYMZxdpjNKBWUSc2pufo2qyvVdSQHCe5aZ6FEciqTBL-06Ep4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJk9GvyJW3OQ8I8WfukEvnqBEO6CcLIG4Mn17c7HD79QR50iLZhv7Lu8GHplNWSuHtnXskj93wexuVzIg4Oak8WSuGj8Vxg-DBrYdIMJD0in0VPGEpG1H1pZzHOaajtq8ZtAGMSY3CDirhDujALce6KEGJXeQ7u_2GX214n-Z6B8NhTjFxpcEM1ETlLHTPjzmos11pFWYAK0wDLTE7BJNtf1Vj4QQC1djg8XgYkdpYIAA7XoXyrUr2X9MmPNIcNVajs6YFwP453Cu1Svi54OdmpHhKof36v94YjotzLBoiuIsDEQivJMYbpEW0arxXDm4wX-YHQJ5pJtwF1OSxCcCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVUfbS1-hRgUAA1U09dOnUIDCUQ9rEbCDlM2Z-VbJBDgN5Ilzny4dMlB0fQRKinANxP5kCWSnd3ipts8RtDQoY3JBXXPHLFda-fXdaxysXFcHMQVYg2gWT2Dht6Q_G8nAWVxgnPEsees5ub_v2e1i5Impm2_9rNbapjeDQFyACWHSOMGe_DBNjfyQA_qGaFQUEdpjx18urRITLmng53Mku8WVYuBAGJRAXzTMZTAiHXcAzpV2UUJX8xSEqaOGmRsZho8gz6w6LOfH8VF2gmqwQR2EdZ92V5VgPbdYzZVo5SMUEvJjtS8tqhljfWecRAnVsT8Kfcc9HKln-Z29LKeFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqK9xctnlVvPpnVbj5vOwRXurYw4pbleRflAbvDL0BxJadcqcI8CjQOiN4aA83loOTbsHbjEOCCrqpcE8IzaeOiJNdp-ifhNF86kimZKW-g-kifKaCpWamM-LapfBPY1qPK30y1U4jDl-LFgy2i-QBdMB55_Aq65fEzmB439HtzQAyLk8E8Y2G-JPzSHbWE6qbKjXlOAsBSIAojmFZWxcYxZYiVL5TYakQndZRZsOj5frVjug31kGx4xGNP_SuMPBa2CUgjY-6_JsFuEDaEyJWa_C0M8ll_PN_AFGRubL6a7-UAtzCHg5tVSp1XBoJ4Q8ybeOHZ4IGvP9G-uDutXZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjNho7JFd3r8kzA4IJUMJ62KFadGMiVLl2N2RQUiz9KOFfjeRKuDuAbIeJHCbDH_yup50ptX6xPvu7G7Kkk4P6cOGvKPIzS3WmbsTGFztL1hKcubppU6D2_RYJSFV0p1ozFdQiLr-8mXXFWtQVMMEGRRDhZaUtwlcqyJ9oPOmhZnal1wW-ojPLSyKyR_YKX6ChiKhL3h-VJjK5CvPy5ZsbYQYaESavMrsFD0bSAbCcPKaWp20MAQ3vxOMJzf587721AYNkkRmi3gw5JoWuJG0mLDOqCDHAQJrwA6wFw_a73fHtZA7bbUdCRN879WiXgmbZAekipWktep3sb8m5aSRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMuVB-8aYZWdmmtfl53F9taUrzrq4PCcWd0lYeAmSOfXVcopGPSo4K2P2p4lYWgWF93k1DLnykC8-SCSGhXqshJRUr8QIx6qBCgESVWoY28VsXAcTiAO9o-jh4szirza1fTPH15WIthedVhONyamvySvMCLIndKMRqfi1f_Fg3Gqlm2mxlF_WwhlkQkCFFOEej1tDWJSQPs1VXNBMAyk1gk1FWJ9iEQ_n6I5FZWMjPgiw3dEIM5fxzROGslmjUApkUFwwhU3G6SfV6L4dzvaMAkfz2-M90aZnroJj1-6grArvuKp4RQJxnJwORxVIM4NCjrdTslklYOO4bc07cXKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwIQveqeG1Hc_7YajuUyMYssWCsnuqcVv5IkF8p39qrQXZrke3cOrWsnfjwcMMie6YGj_L4KxB6BeYKr6HACHokWst4fA8le7Z1CmVTa1Zi-volX84JIwga1rk9oo4QvsMCXAOdAyJJw_dsadGt81TqC3VE-iSnoV2QZVDiuY6QOh9BsIJcVZ7pKs82d_9zgqNFBxe2fUE0gXJdl0X6t5s3k1BaHrWgajfb9VlHHvuUuxa3DmCaiAYCedLGDIEjh4xsLCsgl8KRiQjljOUT8KBe5PFLvJsjC9bvjmrGxzMwySIwNOVbHNh6tqMPZOS6Z5wUh3UuOQjsVDIgki48IXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUuACE_m7HRfkd2wkTMTzI87qcaXAG4IjTZaJn_deM4ce_LV4ZCtQmEJecr7vX9p6FDNosamK1hz-ej8PnOg-a6Sdpw-7lZyg3HhpyEeWsHXcwPNSa2RG6Y5XS4aADta-hDNrZx92w1D6n3LlnsYuoIkaPhFUxsFDb5K4fU8qo1ewvkVQTO7rczx0SoJ3Brx401OSkXMw4RlmDLvBf8GUA_oBYtBJV2l2EXHhB6iaj0SxE7SCDH0I6X__UkFokYhT4G6jkksldoeMGLnmD4ivnerV6sE-znbMWfNTtk3axNMK9BxKlQo_XiFbk5GStGsW4EQCWVn984DevdEFj4Kdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3Nw58WW9slg4PvnFwGmwohH4NC08Anbpz3JaN7wO3jJnlVEwELJJLPtikxSoySEDyRylb6keD7jt_aXES3HuHajGScBuCdZxxT7aBnHnHf7nj0j6pvyProfumE6_hTmcLwHnJCpjHpx7hfgTfbNOUvaLTk9hJ7qUGw3KKHd29R5V0V21oiXe9lEnocwAffBLxJ1BqLOPJttpJw3i1HnrFbEMJMwkpL5aXT1SyYaDh2HeD3IRykuHjAAihDMzkqeRbYaNrTE8kb1fzxuGrOra2q25_zXgeSGj8XQWhoDezkjhdVzMZ_b7w9mdP0RQhOKYbBmtcMlBe6wtzNdYNIMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akRHSUA4OCqttk1S21HssOTxPCVKg95ABOTAe2jeYGknlHHiIDtf73xD3GXwv6NOh-VXg1xdTAwOTAsFCYCXp80XmsyA6r-yGLIOglvQ8RQ2ye5QRz08uaACO68qSeozavoNSbbNNjbd0R6A-63Fa0zaqN9QL4AyY3yQeD8d1wA5xa07Gxo5PDj5KQdqIAjcEPt13p0-Vx4igRuqsPtRcaz6IWdvphW30Op-LjCS_e8D1EToFLwv-iMt8uOYgMKXJdIP4jENyIhZLMKq31rEvc3sOT_W01Ae5xPL5TXrvjv6K5-Xd4_SDFaAdwIDkhtKNPr-UHmhr1OcZA_cBwFUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=B9qWyk-7aHqs-64v5kbbWrkloFeQT_nBlwSkkB93q_aMdoy9nvw--3u_23zJVWtFcrzGrFVhZws-RxPOacqMAYAtFOO5leeR3IHGt__9me0o85oxRbOn6JiE7NqEDJC0kQE-fwiBQmTrS8Z_nLE5oUdqEtFKKyC9OebH1AF_ABBQhjqTAfD70epgy3deemOXJDI-po2lxenyLIRWgHQqtt4wbBeYHQO6DZpyfIu9XxYK48NpxtU943khntLhc-FUQOw139qxMbxXxOhB1baG194ABv0l4NLE7MuslAhslc2I-yBLFUoY5I2n6CV3lysvTylqeQks4JsdlctoK7ArlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=B9qWyk-7aHqs-64v5kbbWrkloFeQT_nBlwSkkB93q_aMdoy9nvw--3u_23zJVWtFcrzGrFVhZws-RxPOacqMAYAtFOO5leeR3IHGt__9me0o85oxRbOn6JiE7NqEDJC0kQE-fwiBQmTrS8Z_nLE5oUdqEtFKKyC9OebH1AF_ABBQhjqTAfD70epgy3deemOXJDI-po2lxenyLIRWgHQqtt4wbBeYHQO6DZpyfIu9XxYK48NpxtU943khntLhc-FUQOw139qxMbxXxOhB1baG194ABv0l4NLE7MuslAhslc2I-yBLFUoY5I2n6CV3lysvTylqeQks4JsdlctoK7ArlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=ID18jueKUGk8L5WWdDMKSYEvNkDpjNW5B8_D-HPHWkq4h934fCCj46HOI-jN8bidHw3J_kiRx_qeSQtED3enhqyRLmshEeGmYzwlD7jJ1rwYvtaWpK1djnzIbhMkMB4OeMEWA3oOOsIwJgm5JL4zIv4oHFTS3L5xxfM0OX5pWP1Mb22YElaP-paKiIudP3gIfT-7wclaocF_g0Xf6v6NRre8Qlb48euQUWMSp1_MQyBZ9LL5NWL4uwExKH7l4auWs_sLWo0ZsoHrPJ4Jp1Mjk7t6BQHPmDrxCK3siyMxTCPcqxEJmYqueDiIznTXVvLcuNX_f_8r8whYEw2fMLGGXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=ID18jueKUGk8L5WWdDMKSYEvNkDpjNW5B8_D-HPHWkq4h934fCCj46HOI-jN8bidHw3J_kiRx_qeSQtED3enhqyRLmshEeGmYzwlD7jJ1rwYvtaWpK1djnzIbhMkMB4OeMEWA3oOOsIwJgm5JL4zIv4oHFTS3L5xxfM0OX5pWP1Mb22YElaP-paKiIudP3gIfT-7wclaocF_g0Xf6v6NRre8Qlb48euQUWMSp1_MQyBZ9LL5NWL4uwExKH7l4auWs_sLWo0ZsoHrPJ4Jp1Mjk7t6BQHPmDrxCK3siyMxTCPcqxEJmYqueDiIznTXVvLcuNX_f_8r8whYEw2fMLGGXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=p_3nFHcYswtk-DnvwaZAQtH_RwSJ3PYcqttazBTxYWN9OBxcP5WPnDvvpU4alFcv9CX9-qt_glknHLHU-FkIEIeZPuLdPJdvJwybXvodb_ztS2KnGJXsJp2-GbEJu2-q1H4CaHE9IcdFsT2GhXQHBUAQ8XfjuIztu3R6CWWmHyKQMRUetnkoW4khdO-ga9oapJ75O_8KhcPMW4DY5Pe8IyMhIsQUOanHpQpSBnuPzz-YJqC8DYqhkXybA9fXnMUq94wT2oZSFlTgz9TmKOgUgbhQCk5t8RiWkBxIvcBWn8gbhOntBBjQgdjweIQyG5s2lgQP_8tOrE3iQGy1sVW1-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=p_3nFHcYswtk-DnvwaZAQtH_RwSJ3PYcqttazBTxYWN9OBxcP5WPnDvvpU4alFcv9CX9-qt_glknHLHU-FkIEIeZPuLdPJdvJwybXvodb_ztS2KnGJXsJp2-GbEJu2-q1H4CaHE9IcdFsT2GhXQHBUAQ8XfjuIztu3R6CWWmHyKQMRUetnkoW4khdO-ga9oapJ75O_8KhcPMW4DY5Pe8IyMhIsQUOanHpQpSBnuPzz-YJqC8DYqhkXybA9fXnMUq94wT2oZSFlTgz9TmKOgUgbhQCk5t8RiWkBxIvcBWn8gbhOntBBjQgdjweIQyG5s2lgQP_8tOrE3iQGy1sVW1-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=UJig1IXt2kjHPJ3sPHOPDGu8wmR7h_qA5fuubYAQ0C4JiVj6gyYAuux7OSVduAMoOhJl4mt9Enpax-vcc4IDxPS_3_T1Vmi1AtL2qCj89v9I3vfh_E4kMGIvBoQ7YbXxswlcZxqS6PgC5AMP0SArdFeqNTmSYiYP8-G5dZd1RWzmdlKCXbCpiG3j6YdZ3d7xdr1GOqKu_P74yJYofNRtspraO9tk0gk_E-kToz66-bJwtafoJmx3rfi0shlBGQFiYsRVL4_y53q3pIaAtnFx7PH5tOnMAWjHOylX0ZU6lp_3AgdpcVt_ebVANxIjkGQyyMTckGaBhzQECGv1yDr8-gW9OPxa4KF-zhHWG1g10gIBlhqYcHmqXNZ_52lY-NOMbQJIlilpDKrm26QUVRkP8d9xqNfWm8AqADwOewkXGUs382KBEQJ4XTORuTuZQJVKH1pb_GSmMWfZK7HmRQ_3zmGQbGmu4n0nFOyvAHb9c6_COcDwKSD3xdMYeCNUzj8OrpsA_SwtPA3ocV7v5hQrH5qSG2yuSyqhHQ9-K5HKo5TGfnG09-FfD-EAI6AKZHxk_tCrmf6mewaS_PEGM_ygyMofNwl26WoUzzlVnHoDEpQORb6CeMpUD89q5M1IMLi9eJsfItS7LE6DWRjoSzmJyM0Src414nsP0oe4OeZ_Ccw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=UJig1IXt2kjHPJ3sPHOPDGu8wmR7h_qA5fuubYAQ0C4JiVj6gyYAuux7OSVduAMoOhJl4mt9Enpax-vcc4IDxPS_3_T1Vmi1AtL2qCj89v9I3vfh_E4kMGIvBoQ7YbXxswlcZxqS6PgC5AMP0SArdFeqNTmSYiYP8-G5dZd1RWzmdlKCXbCpiG3j6YdZ3d7xdr1GOqKu_P74yJYofNRtspraO9tk0gk_E-kToz66-bJwtafoJmx3rfi0shlBGQFiYsRVL4_y53q3pIaAtnFx7PH5tOnMAWjHOylX0ZU6lp_3AgdpcVt_ebVANxIjkGQyyMTckGaBhzQECGv1yDr8-gW9OPxa4KF-zhHWG1g10gIBlhqYcHmqXNZ_52lY-NOMbQJIlilpDKrm26QUVRkP8d9xqNfWm8AqADwOewkXGUs382KBEQJ4XTORuTuZQJVKH1pb_GSmMWfZK7HmRQ_3zmGQbGmu4n0nFOyvAHb9c6_COcDwKSD3xdMYeCNUzj8OrpsA_SwtPA3ocV7v5hQrH5qSG2yuSyqhHQ9-K5HKo5TGfnG09-FfD-EAI6AKZHxk_tCrmf6mewaS_PEGM_ygyMofNwl26WoUzzlVnHoDEpQORb6CeMpUD89q5M1IMLi9eJsfItS7LE6DWRjoSzmJyM0Src414nsP0oe4OeZ_Ccw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iA3wMDEd7E8vu8B9OBIvBOFA8tbFuL7dWvSZzA6ZzFJn8RNyZACahq1dwfZSWeTm0-kyz_kcs9xVJK0pYidECoCg6z72J-eUjXQAxDdbmpK00vUjxM2iSU49yTFqmcCQAYcmKOjMkhg4F6Nzvq2BasrosnHMtm_xxW2cDXsnsOiUejl-8HSFvuROiqNHaSFgWAceOY_oU-6DMxqHwUjRXYIUJEpFEKo4jpQe9DgwxpOGSm_7B1uVEaZCZ4e342mumfd4wluTi_pWL6mOal_JajRE-_iEmoBLdnAH-UW7lPCJppsxR7dCHWGbjjKColTqZnVIgs8gh5bZsgcBKOizPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8JmGGM__gAn45zdT8zh2bJ-PjOwuIvvD15CPE8idjCm6HgTFTIODEqrGt12aYMPbgSEypXSQP0RXoiSpah4pnPsl5LRsSN6JxsiYIsKuqLM6cDaTOGOT_0T_S3vWsTtuH2ctNdeGDIrOfH2ztpAJW59lcfjW8DJuzIhnIs3m48jf-BTQpf8ISMM0383yd8VWnBuulDrg7CduOT84wNzrtJUJ9Xim5B09hYksOOyvQu6FyEDVHS-T-g5MntzpjGhYokTt9qna-s18HhCL1_2JREfKVZxlwD5neOA7nFx_gGzYp0_mD9mLThEcPH-vcYNdKoKmNOuezQMJyC43s-jYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=DaUHiv_v-VbXJLx2lmyXIt3bCJR7Q99kVttbNalXeoEvg8eyj5uYysq5ux_SrfbfVABYhalJu5ArNP1-IIr6RdEu1RxlILUi9J9p72x5S3hnugw8xJeRahZe5Jm7H8RqzeW6AaiDRgvQjsS6eN8OFDV_O5ztGKl-KfVIlkw5j16P-NKXZdc8SofQQtZbnJ716XGaoJMGw8YlsZosErg5svfeQhsyKQKWrcacrIoTLKbKBpCoVzK04undpV2TBbIgGzQWrj93ffbkXnGa9v8pbEoZ95Bgoh9eo381Yx46yg-KP1in5cAdSxDEDEZFxNrMezF2PgP2MOMurDc2yVhhWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=DaUHiv_v-VbXJLx2lmyXIt3bCJR7Q99kVttbNalXeoEvg8eyj5uYysq5ux_SrfbfVABYhalJu5ArNP1-IIr6RdEu1RxlILUi9J9p72x5S3hnugw8xJeRahZe5Jm7H8RqzeW6AaiDRgvQjsS6eN8OFDV_O5ztGKl-KfVIlkw5j16P-NKXZdc8SofQQtZbnJ716XGaoJMGw8YlsZosErg5svfeQhsyKQKWrcacrIoTLKbKBpCoVzK04undpV2TBbIgGzQWrj93ffbkXnGa9v8pbEoZ95Bgoh9eo381Yx46yg-KP1in5cAdSxDEDEZFxNrMezF2PgP2MOMurDc2yVhhWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=onTAC_zSXRCXnR77L3wRSDOmwcfyOOuKLMXId5pYShV1RlAc749Umx6tVDG8tJGjTYDT67BibmpJ-inO6vb6rFXrxSKDxJDSKTdGIqEY2Xwr1bwn1SmQ_BThh0pqOsC6NtZdADRmVdWDKL0i1pbYgMzok3xNGXaSpFlleUziR8AUq_BaW4RRfN3zY7iUD1lt-agIGUIyOVkoMAJwi4fVSDbCCIk33WMa6e8ZlSyH0O1Vy2GsKcLEQ3b7EEsDEohvHhEuwWS3wpGtOej6uterpqnDHg2w6R9FQBRt5yNUhsqdzwwb9s6oR6n4S9SSc46Ua-ux6Roz3pqW5TqPxrR6y5YYeZi6kGY4EmwcoubbEsKW7lSMYAZVMro62urpfUiLzPDzwl16cgIL3M44D_dmOe9XVOurj7lVR0gCAPQLqoIKYG3fho_sYvCrnVrDy0iuhwKS3T--6RZtB9AMe2II4CyCqCsyfCCru7S_FxDMJQbx7EdeaTBJK8I9m8FMrx0qN5fUBw2STjIqumNJxR-wbrOx3DuP_Fp4E_qQymN64xEjY5rr8Cd-jshCZnpzaw97CnFkhNUSVBUt1fuIsW4Ho-9VLZikj379DQ2A12T7PYAQ-uFsITz7q1J-BfVIfXHlLYMqJXOBN1p_svclI9AAhyfksyMa_okVws-4akjy1z0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=onTAC_zSXRCXnR77L3wRSDOmwcfyOOuKLMXId5pYShV1RlAc749Umx6tVDG8tJGjTYDT67BibmpJ-inO6vb6rFXrxSKDxJDSKTdGIqEY2Xwr1bwn1SmQ_BThh0pqOsC6NtZdADRmVdWDKL0i1pbYgMzok3xNGXaSpFlleUziR8AUq_BaW4RRfN3zY7iUD1lt-agIGUIyOVkoMAJwi4fVSDbCCIk33WMa6e8ZlSyH0O1Vy2GsKcLEQ3b7EEsDEohvHhEuwWS3wpGtOej6uterpqnDHg2w6R9FQBRt5yNUhsqdzwwb9s6oR6n4S9SSc46Ua-ux6Roz3pqW5TqPxrR6y5YYeZi6kGY4EmwcoubbEsKW7lSMYAZVMro62urpfUiLzPDzwl16cgIL3M44D_dmOe9XVOurj7lVR0gCAPQLqoIKYG3fho_sYvCrnVrDy0iuhwKS3T--6RZtB9AMe2II4CyCqCsyfCCru7S_FxDMJQbx7EdeaTBJK8I9m8FMrx0qN5fUBw2STjIqumNJxR-wbrOx3DuP_Fp4E_qQymN64xEjY5rr8Cd-jshCZnpzaw97CnFkhNUSVBUt1fuIsW4Ho-9VLZikj379DQ2A12T7PYAQ-uFsITz7q1J-BfVIfXHlLYMqJXOBN1p_svclI9AAhyfksyMa_okVws-4akjy1z0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogTuKYodIAqXbx98q3W3bQ0rNXsKnlI9cJ-JPDlfyESShVwmPFBq0PrZA-tyEGoxuZ7VIz5Gwrh0Go7wE9Jaqdb1YoWsHmcrRsloEhCn1oqgOAH6z8x-fCGwXOfkkvHJvyS0vIR-0C067f1tKNXTIXagUmVAewyTPOzTptST0exXG3iy2gMl9lm6mOkkW-pXZO_OXUB-p4ztKt2Mm0gMq6AxEzKC9s46mryMBESKw4bDC1RRm6o-uUGMo2exPXFmZzqsksKSeFrcouoPjCE21VwHLf_wRu_C8KAw7_JF50F179JwTJ-_k8J1HijGtmz3mV3hRcyxOEDZmXs9AN1H4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=UfsYz6GlIXmqnvq6hEh0Da_fqm1r44vETdS_yJ3WmErupu9aZFQGjJhWZHpE1LKgk7DrNjCV-LJCcov4c7nM3A2ZlEj24ggjG8lLsoxkjZ6JGCsdthoLp_7PPCFqIAySHtdYQKHhu2M3fwHp-fg_sO3uX9MTBWrTyAiS8dJUeAw2WtnYSJTBIQ2-xvYDkvtVWoT_enXUa7Lz1h3Rb46oztHDIoW-ys_WbI_B51oPq4FZ3A1JkLBiRUn2DyjoHZ5aOLwJ2mvIISiWBroUSeECHady7OirAro0JJIhrbPQvXOFxy41WsuCuwL1PjlMsUyM6MiFMUg7ByM457xLqlM9TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=UfsYz6GlIXmqnvq6hEh0Da_fqm1r44vETdS_yJ3WmErupu9aZFQGjJhWZHpE1LKgk7DrNjCV-LJCcov4c7nM3A2ZlEj24ggjG8lLsoxkjZ6JGCsdthoLp_7PPCFqIAySHtdYQKHhu2M3fwHp-fg_sO3uX9MTBWrTyAiS8dJUeAw2WtnYSJTBIQ2-xvYDkvtVWoT_enXUa7Lz1h3Rb46oztHDIoW-ys_WbI_B51oPq4FZ3A1JkLBiRUn2DyjoHZ5aOLwJ2mvIISiWBroUSeECHady7OirAro0JJIhrbPQvXOFxy41WsuCuwL1PjlMsUyM6MiFMUg7ByM457xLqlM9TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=fm-i4U3xHlFva0xtSdVpOuo4I_raHdbdHTUBQ7Eledr6Re9MSmas4bmy0llLKMEj-pyAZkLa_VsDdH_j3ctd6VSu9z0GFqQ3JMTfBpIiCuBJQC5fM8sPvcWklcPVC_MrOhtL4Qis90-IghKb-bgduUV2JW_xY4e9UmsJw5HDkIB37y3xJ49b_NddMRtPKsLyDk-wR4RrKE2tr7FzPmE9c4G-VPM2Wt8azVkTzRKgvexF371UVjE6u3wZ186311oiAySH4iWMtT75cu8EvWpNQ9YHnf-tWhsdkRd3V6BiwUfkRMsD8NhiDjlHnWMUaZ5zfn-icPaSYZMS3326Smj8sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=fm-i4U3xHlFva0xtSdVpOuo4I_raHdbdHTUBQ7Eledr6Re9MSmas4bmy0llLKMEj-pyAZkLa_VsDdH_j3ctd6VSu9z0GFqQ3JMTfBpIiCuBJQC5fM8sPvcWklcPVC_MrOhtL4Qis90-IghKb-bgduUV2JW_xY4e9UmsJw5HDkIB37y3xJ49b_NddMRtPKsLyDk-wR4RrKE2tr7FzPmE9c4G-VPM2Wt8azVkTzRKgvexF371UVjE6u3wZ186311oiAySH4iWMtT75cu8EvWpNQ9YHnf-tWhsdkRd3V6BiwUfkRMsD8NhiDjlHnWMUaZ5zfn-icPaSYZMS3326Smj8sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUZ3XlsNIYaDyjjBQ_ph9eCf4xR1U7cOk88wcQvtOHZN74Pch34KuAGwWd8jW57YakxXhBvlRKc3EJSAA0v5Z5r1KgLb5J5uKr4df_sFM786nXH4S2V7qxWSY-taYU6o_MZ1wkBWn83qd8yTvZT3M6k8x71bamHoEhNbXWI80oNiu9xlDiAoLadHB-K8t2n5TzM85fHMlhYwlNI9v7f2pPdoP_E8QeJkh3sdqRkj2YwWR4XAIeyKavz_4hBIsp_Mc_OWKyw9o-ZtFBv6WCGI-sTkWvYs3vFTAMi-IFIjD43LtSxB19nqkj-YEfEvsIOj9zF17_H1VbFVB8bwrRKafg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=pal5lbsVFmdH6jUZ9MP7sSqAiLBY1VdQ0HrZ9DkrmHSCEVtsida_Kle6ee4Jtc_4Evty9qkN7w8sBmdaXudxH8Y8cVhm0U6nIL5z1K38otn5MRMXA51AD3s13F3YJD5tB4dH9Z9qpxImUdKJOWhQ87hYgIbJuxfDgCPhE-rz_0gB4RifuguS7rcdAEDgrdN4XkcRvwqgHjSFJDfiF729qMQog6-KkEZGjCpdiSeTZLFx6JLjtKml-5XU4wOi3CCkHazjsUjmYa86CAhtywAjLCK3H1WDqB4dngBR3GB1Vel7L-SbvkZF-d7zbXfZ0t1OTiVBDdTE3N8wqcVevRcvpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=pal5lbsVFmdH6jUZ9MP7sSqAiLBY1VdQ0HrZ9DkrmHSCEVtsida_Kle6ee4Jtc_4Evty9qkN7w8sBmdaXudxH8Y8cVhm0U6nIL5z1K38otn5MRMXA51AD3s13F3YJD5tB4dH9Z9qpxImUdKJOWhQ87hYgIbJuxfDgCPhE-rz_0gB4RifuguS7rcdAEDgrdN4XkcRvwqgHjSFJDfiF729qMQog6-KkEZGjCpdiSeTZLFx6JLjtKml-5XU4wOi3CCkHazjsUjmYa86CAhtywAjLCK3H1WDqB4dngBR3GB1Vel7L-SbvkZF-d7zbXfZ0t1OTiVBDdTE3N8wqcVevRcvpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=ocwZ5trhrc4xTP2GO_lnZepXwdlBejmFv-9zvGo0ZjWU0HIl9tgO2Atfrr_yLw9VeUjioYX_WlS2nTvovOvV1mbU-uMVDasO441wjTMrfI-VgFE2Aai4lIhxNZCu7CHF6PM_qXncmES1SA2w13DU_TuzkljFXJaOJsydqb11lpd8qD73A8QpWrUfiJENixRb86t0kV4KkpYSdd8rhm67Zwl6IxzQv8NjlieHWW1co_qlcZ_wgaRDmqrtVBvh2EG9N4TdHOJXIl0x-1I5CyJHRMCzA6QDd3L9Kg0l2nFdH0Ec7GDbm17b9AmOeSPosE1GK_J6ZhJoCH_0ZXqiGBBiKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=ocwZ5trhrc4xTP2GO_lnZepXwdlBejmFv-9zvGo0ZjWU0HIl9tgO2Atfrr_yLw9VeUjioYX_WlS2nTvovOvV1mbU-uMVDasO441wjTMrfI-VgFE2Aai4lIhxNZCu7CHF6PM_qXncmES1SA2w13DU_TuzkljFXJaOJsydqb11lpd8qD73A8QpWrUfiJENixRb86t0kV4KkpYSdd8rhm67Zwl6IxzQv8NjlieHWW1co_qlcZ_wgaRDmqrtVBvh2EG9N4TdHOJXIl0x-1I5CyJHRMCzA6QDd3L9Kg0l2nFdH0Ec7GDbm17b9AmOeSPosE1GK_J6ZhJoCH_0ZXqiGBBiKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=YNP6m8pK6WpXN0mrSkjwxG6S7-CV9bcfDsW7KD0d2uBFKY7LTJVEgAdM0B_ND36xrStpiIENfgY6kbQoTrQWWwVr21dmhIi9mwQMoHtjgiTadAsB2HzQw47di2UblTPlBoZtPS9QM5K9-WOUT5K4Tl80zjFvvFcB7Tt0Y5BOGOpsBpyAe_7jM3OZgYpLq45LsMyyY12yiUKl5SU0oi0YrgYatEWwWtCRrM9qxzOMD7bx5Ybr1t4dh_-41Jux1oUoMPDfm-SwLbUA53jiO7Mq3dTZTNOMD8yqwVuJ5tcRb3FFVGJSsGsU2y4X0fVicB4w7aaUEXa15ZChN694TyywnllWHtBSOVx2eTak3fYK4ZhMEMlfBPa_GIQM3Reax-PCHfOb_GsHyAH4R5xOEVNkQXA5zztthvGl0T7ivFaKTfE7dqzCa0NzorOMq5igS3-wuQYcixGPlYOSfYgb0nmmIFxYUt3DOK2AsTwvQ-A2b1kHAEb-e2sMfP4_J3IpV9HN2JUybHLp437kVefHFSYaliqrzLo778mzptqWpv6eR2HJwZu0GzQK6u0xfzayfOBLqSLIQ8-bS3uOQeEv2lG9iv5oDrsU_eab4OWHLUXxc4aqQEpBfqlxao_rf5dCPpCXu1KiyRlVFSbJ6tVrYRuxsWkS430zM4Cc7D5GoF_LW2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=YNP6m8pK6WpXN0mrSkjwxG6S7-CV9bcfDsW7KD0d2uBFKY7LTJVEgAdM0B_ND36xrStpiIENfgY6kbQoTrQWWwVr21dmhIi9mwQMoHtjgiTadAsB2HzQw47di2UblTPlBoZtPS9QM5K9-WOUT5K4Tl80zjFvvFcB7Tt0Y5BOGOpsBpyAe_7jM3OZgYpLq45LsMyyY12yiUKl5SU0oi0YrgYatEWwWtCRrM9qxzOMD7bx5Ybr1t4dh_-41Jux1oUoMPDfm-SwLbUA53jiO7Mq3dTZTNOMD8yqwVuJ5tcRb3FFVGJSsGsU2y4X0fVicB4w7aaUEXa15ZChN694TyywnllWHtBSOVx2eTak3fYK4ZhMEMlfBPa_GIQM3Reax-PCHfOb_GsHyAH4R5xOEVNkQXA5zztthvGl0T7ivFaKTfE7dqzCa0NzorOMq5igS3-wuQYcixGPlYOSfYgb0nmmIFxYUt3DOK2AsTwvQ-A2b1kHAEb-e2sMfP4_J3IpV9HN2JUybHLp437kVefHFSYaliqrzLo778mzptqWpv6eR2HJwZu0GzQK6u0xfzayfOBLqSLIQ8-bS3uOQeEv2lG9iv5oDrsU_eab4OWHLUXxc4aqQEpBfqlxao_rf5dCPpCXu1KiyRlVFSbJ6tVrYRuxsWkS430zM4Cc7D5GoF_LW2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=F9rLBVOFcVAO2UV_Jn4DMoLywQuIBeZCa7J31kNlY9p4qNapFbz0oqnpmVLU6U4s2y6kThhCYMQHg9YBbvRTdKxJe6RNYoG1cOp5ANFnxTaoOxEdslyju4aPkBCsnDlhms9z3ERUMb-WeJVPnxzMis_ly4T-EB7RUFHlihxs8kGKDG-Uf9L12etXZUFCQUpmdHJ6TJcuK_NuAskK8-tNKuiDhhX5pWHkne0pSDLtF_n8ZncbaY8GCXg7FpMiAwoTnFIuFan1-b-v95Drvz_TD0YKqTj9R81KhYSQdttvSWdhvZBRuDJYW7EFpssDxycXbVbkMNBCQNftDGoACsB1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=F9rLBVOFcVAO2UV_Jn4DMoLywQuIBeZCa7J31kNlY9p4qNapFbz0oqnpmVLU6U4s2y6kThhCYMQHg9YBbvRTdKxJe6RNYoG1cOp5ANFnxTaoOxEdslyju4aPkBCsnDlhms9z3ERUMb-WeJVPnxzMis_ly4T-EB7RUFHlihxs8kGKDG-Uf9L12etXZUFCQUpmdHJ6TJcuK_NuAskK8-tNKuiDhhX5pWHkne0pSDLtF_n8ZncbaY8GCXg7FpMiAwoTnFIuFan1-b-v95Drvz_TD0YKqTj9R81KhYSQdttvSWdhvZBRuDJYW7EFpssDxycXbVbkMNBCQNftDGoACsB1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciXCXqYu4XGLET6yaYE0g2TiS2URe3K-fK5j3H7utoOPlEmnTWY_ogpx83OBxr7ldmpcYCtvK4GMupQcsIXk-VcBBefP6KnQMHauNxStDJ2P5XbyUYiokVhijzC-6H5MdCxzuyWceQrOLFvAOCfoVYwDzzlCvT-2BNGv-H7ruL-cdOwmWk5yNOXoe57DwKHex0SkJ1CdAaOrxH9nQtDP-UaNy19gbUf2RURGjaUfpof67KVhkRtcpEhlOu4smqKUMua_wGhx8lMKhKvS3YPgFDVyPfSh36VfDp776LcXyOzfJR18Qa0CI4xpFs_z-_RmN9XsJnccKrKZ6bTnGifgFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=ImWXFSQg1QK-HtoxXwhigc3jIqETSWVgk3xVNUSIgq_GZG55CcU73lSXWoDNT5G2N0gyD27g5wanmL1INX8Z0kfFXu6Z7tlqZTNWeh0YElhNuut9Cffg8EdxRngKGHEJDhy2RLRvHCxTHqBZlkMVfLqg6XoZH8iZEGtgtbVjXufz2Q8h8yDvxZedV3SKtUsh1TXu2ch6FHgXUxrGsQoqLmD5aAI9-emAZXh2lVHMysZdd4_udx9DxuRlegi7XjIoUu4XQa4XpkdHIFPEm53wp2yFNsTAXEhiX6yBQIj6RQXDdIMO1TYmGtUtuZuypfDGaG4whcqr7wIMD0NqmYPtqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=ImWXFSQg1QK-HtoxXwhigc3jIqETSWVgk3xVNUSIgq_GZG55CcU73lSXWoDNT5G2N0gyD27g5wanmL1INX8Z0kfFXu6Z7tlqZTNWeh0YElhNuut9Cffg8EdxRngKGHEJDhy2RLRvHCxTHqBZlkMVfLqg6XoZH8iZEGtgtbVjXufz2Q8h8yDvxZedV3SKtUsh1TXu2ch6FHgXUxrGsQoqLmD5aAI9-emAZXh2lVHMysZdd4_udx9DxuRlegi7XjIoUu4XQa4XpkdHIFPEm53wp2yFNsTAXEhiX6yBQIj6RQXDdIMO1TYmGtUtuZuypfDGaG4whcqr7wIMD0NqmYPtqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=Saf_Zka6Il3v2JB0A2b9ZuY7ocsAPwcddvXpNMCESZQNRcLn5ZrHhLnAmtV8-iO1df54ZDhXCwfk8k1kYXBK3NwKQ2gKNPHKPEiiTVG3WBt5QpgA0MhvdLPQ_Ect-jzjqis0PZI0i42fuMujLXD8AIDhN8v-qY7ueDycUpIfnfZIdfaPgkrs2nEoyv1CD2EBCBnOwr6hNW8COwPRlXoZyuN7kf-rJgZTBC6TvRZSjzDRHumtrt5sl6mKG0jhxydpbZ74BfLno9p1-d68C6Up_Fsx-6CiVlmTjV8AFjVW2NOwMr-jD2tI3DonxHCVXCBuTghAFlwUqXRJV9qkctp5jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=Saf_Zka6Il3v2JB0A2b9ZuY7ocsAPwcddvXpNMCESZQNRcLn5ZrHhLnAmtV8-iO1df54ZDhXCwfk8k1kYXBK3NwKQ2gKNPHKPEiiTVG3WBt5QpgA0MhvdLPQ_Ect-jzjqis0PZI0i42fuMujLXD8AIDhN8v-qY7ueDycUpIfnfZIdfaPgkrs2nEoyv1CD2EBCBnOwr6hNW8COwPRlXoZyuN7kf-rJgZTBC6TvRZSjzDRHumtrt5sl6mKG0jhxydpbZ74BfLno9p1-d68C6Up_Fsx-6CiVlmTjV8AFjVW2NOwMr-jD2tI3DonxHCVXCBuTghAFlwUqXRJV9qkctp5jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=e-igNLWeBKVVZnKPwQUbeIO9oKm8boYB9iJT953juai4aOHZWzcD_S6ynS0QXrbQBTBgktdhgp5oufaLW1R7lagtPcUZRgt0Qqggg4oSBXEtNduQPyB_qnQe4kJ4tcsBC7Cj7ou_VzkaoY_nCaLcIhzJmMfZ5lEcbgaKUkWZ1oITNCiqo3va2i6WksPYTOdRtCjvHIrehaqYp4Yw9dIwZFrndo3JFwN-nyCck9fTdkazgs8mcqpqRwrMy6lLbTMroxyNaa_rPWGEh3atdRfia9drifnY_eWYyZbNJj84nZ18Eg6h3beooBkvJGtedtSOESV9pdgPRGebBu_zgV4zMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=e-igNLWeBKVVZnKPwQUbeIO9oKm8boYB9iJT953juai4aOHZWzcD_S6ynS0QXrbQBTBgktdhgp5oufaLW1R7lagtPcUZRgt0Qqggg4oSBXEtNduQPyB_qnQe4kJ4tcsBC7Cj7ou_VzkaoY_nCaLcIhzJmMfZ5lEcbgaKUkWZ1oITNCiqo3va2i6WksPYTOdRtCjvHIrehaqYp4Yw9dIwZFrndo3JFwN-nyCck9fTdkazgs8mcqpqRwrMy6lLbTMroxyNaa_rPWGEh3atdRfia9drifnY_eWYyZbNJj84nZ18Eg6h3beooBkvJGtedtSOESV9pdgPRGebBu_zgV4zMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVwLewnKwX2zzN6JB57PEGt2KYwObvkChSKwsX2LRieJoSEHK7FLl9mjMkWHrcXOddr1j1uUXvyUwAsGFSD3Tgf89KZZW3fXj00zOtLuuili1FgcCtOAJDsTyEHx11bZSvpwWoMqQHUkTKiDSzb9MnF2YFPv_Jp7ni5W7pwDrQoub4SakyoN3_9QWvQZsvBOCJ5rwZ7w4mQAnthCWGLI93IFQLSnu_QCOTzPoX2uuwDHZeXvyV2HF94dUZSfNmo21aCHUJdTqAojOBUdvZ7u5svAgcRCRu9a5GqfuIIHr9U0rkz8AMjt0UiVACVJrxVVui7c7TzzWDs910VAE39lDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=p0rZhisiIAjF5HB1WlKDguI1is-cp8-j6AOUEKJYw8FZyIR3REmIKpU6tWN5fZSxUgFm1_R10ot3fH0oK1lO-3jJL6rdWzeOxsNJzuLu1nxEdxSLoCpgrXCf1tB-kDu7tTNcnudxm1Ko4dTAahg-qedglv8Fnbi97WlhqqfU5jQizq6-6f2MGeoYAyALo6UMIbFaK_4zpzYk8CD6_xbEU755dsXFoTZzfu2JPZeWp4wYwirvZYni7ejQCsV59EH3p0UiHZ0XK0jWfVAJLFOkyakhE_cC1LyJo91wYNUDJj68cvml2NAEophl3VZPs29mQYNHJTF3f5709esdwAq_dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=p0rZhisiIAjF5HB1WlKDguI1is-cp8-j6AOUEKJYw8FZyIR3REmIKpU6tWN5fZSxUgFm1_R10ot3fH0oK1lO-3jJL6rdWzeOxsNJzuLu1nxEdxSLoCpgrXCf1tB-kDu7tTNcnudxm1Ko4dTAahg-qedglv8Fnbi97WlhqqfU5jQizq6-6f2MGeoYAyALo6UMIbFaK_4zpzYk8CD6_xbEU755dsXFoTZzfu2JPZeWp4wYwirvZYni7ejQCsV59EH3p0UiHZ0XK0jWfVAJLFOkyakhE_cC1LyJo91wYNUDJj68cvml2NAEophl3VZPs29mQYNHJTF3f5709esdwAq_dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=pXdjTrdOf7xY5opIGG21GnHWPhkVWDWpyMtkP16HT8f0exxCImcqH_BT3wmGNoVTFCAFJ-N7QarC3x4VavLRA-wrI0mj85KGvckkjqOk_2amvi9mOCuHMOHPymBhxzDma-WD9DH_9X1OIwoWwgfCxz9BPg8w3dS437Iihe7R0DbGpTFhoMWnjOpxhd8HHQOF8p55YwpbnhIvnO-MdDgwBwIjz4uSe0CAdc5lOT4lw5ywDEljnEvW0KGS-UgG4SHGvVbd6PARRRHgn162ODAY8hZ2oWRQfTCoVhPDWkSiCa-K4y4q_WNsK3TmDU4lV9y7aD7sx8SIYZT2B7Z05sBKrA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=pXdjTrdOf7xY5opIGG21GnHWPhkVWDWpyMtkP16HT8f0exxCImcqH_BT3wmGNoVTFCAFJ-N7QarC3x4VavLRA-wrI0mj85KGvckkjqOk_2amvi9mOCuHMOHPymBhxzDma-WD9DH_9X1OIwoWwgfCxz9BPg8w3dS437Iihe7R0DbGpTFhoMWnjOpxhd8HHQOF8p55YwpbnhIvnO-MdDgwBwIjz4uSe0CAdc5lOT4lw5ywDEljnEvW0KGS-UgG4SHGvVbd6PARRRHgn162ODAY8hZ2oWRQfTCoVhPDWkSiCa-K4y4q_WNsK3TmDU4lV9y7aD7sx8SIYZT2B7Z05sBKrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=QLaQGrgka4YMW315iUPflifDhabR357SoQubHODdT0n8ulXNrZH11lzm-RHRQMhdrw-0ZcjJWfXuv4iOYFRr8B7I6k-7zqP07Po_sHKz1v0WGK-IWOQWAKP5wo5m8HiCvOJpAPhLr5q6Y6ZGm_BJa17QBJD-6ot5INzASiVeo-BlQ-WE-NDpeMKUPHl2gfNCH0O6ga-3p3PAAbhIvlNi7N8MWmqnAeYkfvzUVQuiYHdFgcMo4tuJFxSHRASnFbg5feb-6LcBorl_NHfMFm9zYBgzlIxbxxb9aoXOcJ6_hlpUDgNDjywhqD4eqSao45UVvLLB0ZBw-ns-fQg9glS2dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=QLaQGrgka4YMW315iUPflifDhabR357SoQubHODdT0n8ulXNrZH11lzm-RHRQMhdrw-0ZcjJWfXuv4iOYFRr8B7I6k-7zqP07Po_sHKz1v0WGK-IWOQWAKP5wo5m8HiCvOJpAPhLr5q6Y6ZGm_BJa17QBJD-6ot5INzASiVeo-BlQ-WE-NDpeMKUPHl2gfNCH0O6ga-3p3PAAbhIvlNi7N8MWmqnAeYkfvzUVQuiYHdFgcMo4tuJFxSHRASnFbg5feb-6LcBorl_NHfMFm9zYBgzlIxbxxb9aoXOcJ6_hlpUDgNDjywhqD4eqSao45UVvLLB0ZBw-ns-fQg9glS2dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=nHwM3xqbm88bjLpTtIZ-izaqhJZNNThAeIqvrFaKttvUh9aL0cSRIPA8V_2yjEHbUM-cNCU2JngP93d2hy_wvEB9TjyDZfbgR7YJLZANutPYUFSrUNohvIthhd824bnJJop1GYLTQz6Lt-Fe5ooGne2Zl_RxU7RTDmt-pPFrRLKITCb6fEBU6cgQiu5pk5681XT_EFWIY99eHGSWD9jon_zi40L67YBW9zDsdHmM8N5Fn6FR7TsVeBRap_GF1P85jFdGuQiAl7ky7znzULLKaLJcMNczHqPiLy-NzUW08-G45iSjyL2hnUx7mZEhTwkkiPGgICEZkotZDVJwOW3tQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=nHwM3xqbm88bjLpTtIZ-izaqhJZNNThAeIqvrFaKttvUh9aL0cSRIPA8V_2yjEHbUM-cNCU2JngP93d2hy_wvEB9TjyDZfbgR7YJLZANutPYUFSrUNohvIthhd824bnJJop1GYLTQz6Lt-Fe5ooGne2Zl_RxU7RTDmt-pPFrRLKITCb6fEBU6cgQiu5pk5681XT_EFWIY99eHGSWD9jon_zi40L67YBW9zDsdHmM8N5Fn6FR7TsVeBRap_GF1P85jFdGuQiAl7ky7znzULLKaLJcMNczHqPiLy-NzUW08-G45iSjyL2hnUx7mZEhTwkkiPGgICEZkotZDVJwOW3tQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vl7fZz50o3VwdXXKEQpc8TFeckbFRSU2Jmgr_E5ONiCEu2NKmFFNQvuHQ6XJGtK7jGCLzW_XBZLtEJZP3FtUK0wndc7k_c6R2dCpaBddDRzIA2RqnRgcP8sblrcl0nErd5Xdt5hU0fsxE6QxuRPnygYirmuKwZi_qpOk-3PBU_dP15tx1WDso5S9QvN8q8z_S2lOzABR3CglJt44_sov2Z69ylTXqiMxO9gfDbL25bvOPKQugV3tneNq6XB11v_McJjSaXpPTyP4b0dNYsMNH52bu_laEqnzgp5XrZMHfvrdHJqk9Sqgd-qrUrle2-w6NYGR_ZEmO6IYtt3Tct4xSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfaZTO4ruIdvYJUBdIQhRJ0B9GCm-Da1S-eNILj34LhFBiy1cVOUWt5u-kYuuaehcwo4tvAgbgi2sbQUIr_EfCv-Pq7_vM4YH7ZKtKfl9YfukIFcwrTUYt8O3GcoCIKiQ4Aaimqaa25Lywyoi_4ySlqCN3lVQ71SmHExf9fb4ZHq7Rm1ZD-JV7eLP07o1tZGzx8g8ovQjxh1u1eM6a4zO7EWOpBoNOPPTBLIOZDL3uLi9c9qSkxkXLrA0OPjT1vFTHst2soc571O8ccheZ_OatYEdRHSeHG6aSWweG9vEG6nWWfwR2z77-K39z37w947ICDH0ayd2S1BGCc-IRFuww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyWCSk4VOpt4f1XEKNNSsDuFUVUUod1iwjtat2gywDfqH9aTZEW8bMQtk0Y8ZQLYbaFPhZn9FEvZZugivLwE6Yt_h07YJxmXNe68HikQgVmVP8Yaom81vcdcmef4eXE5HyKk_loX6EBfKqH2W47IN9P9w1Yr59sCq4Ff_P7lHGp3pF3mJc_A9DNHw8EzLwCOquxZCcpOEe4JenFimyJhdk5AKwgYhZxklOoykFDx7GdVDnA_a0vQKdhKGjfNBXlidjoCXkaqfsTquN_Sx2oNOqzIOxcuRNbCIZLEXGI6fQiLuohK2qq2O-1SOtvGHJMIOmPXKJIzfBqehNQ2---Skw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2o5dRCKevO1kCZgbvwOSkNu6tP8YjIAP4muBVeLyYDFRlZgzve558qCOrRuyTTTQKH6OKNT4eldyhI52W_ywhIlAZD_zd4-b60-4AyyvHjD0kn0WkJanRJsZ_ghJ_sGox3sKLWQ19spXgZKMDLqWoqIDJPXLDGu7ixmIeL4KTFD8WagNkkCrgzULYpBU435a70m2Vwn1iaZ2kNLvaugPj1ULdWZXaTgJpb1XhpD36jQu8mW4x3M2yitOLSYXncYjZy7dG0lMoEbTGJ9pVKSOr0gj2ItVA_bo4ghWQ9QqTY2KWfpX_KeFFM5iAqGNJoOmkMvEjRu_wJouPz3vIUIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMS_xYveYyAGQTNgqkn2jhvk-UlOMbzOX6Dhj71yyr9eCcYzN8ENMXzvlhODxNqxQ_brdX_FCSGIv8zDenc6AzmijTE-dzCAGIyERCsN9tdcwp_XPHry43ErEPScquK2cMZHltG01Sdv_ku4IPdZmm9Ao1giJzi0iSrSYtFZARjcRQallx16622d7maSWellI7YAyb1_jQ2p3bX9pKoRt4mtCzq22sqDMCgIasx0TecAYpr23giuJCJdK2XVxoZ8Xs8a728OokKYNsiawRdxjgXpFlUA4kEuFYl5k_r37fH0BBBIb7fk9feMk_SuJBnhUWva3O1_ycrPqyqAmr15jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=vTz3yT7f7vh446YKN4uIVSiBSF8pC-fnRE-e-NGhjvFyfzgkwK1xfpyZpH1KQNdznA-vB1VQqBhCHlCFmRHoVKHpiNWyjOmTau7PCao6Ycvw2yJ9GvcyFItU4qGnUfG67VRQEb7vkdTvjsLwxbY3gDK67JXqe8o_W8PpwEtcgG_VYiTfgNd-f72hH4eao-5Ukv9f2zOa_JFf-DzzEauJqaWWYc4s2043KbexuW_IujPwWSNhYMBBR5a3iAX_1mcqxGHF-PchJZ-vcArZorOgvQze4OTv1HUvBRyL_IaI9d8Hwm3_snLGJ379Jsi2YVs7H2NLDzMJm8wcPhAufn2sFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=vTz3yT7f7vh446YKN4uIVSiBSF8pC-fnRE-e-NGhjvFyfzgkwK1xfpyZpH1KQNdznA-vB1VQqBhCHlCFmRHoVKHpiNWyjOmTau7PCao6Ycvw2yJ9GvcyFItU4qGnUfG67VRQEb7vkdTvjsLwxbY3gDK67JXqe8o_W8PpwEtcgG_VYiTfgNd-f72hH4eao-5Ukv9f2zOa_JFf-DzzEauJqaWWYc4s2043KbexuW_IujPwWSNhYMBBR5a3iAX_1mcqxGHF-PchJZ-vcArZorOgvQze4OTv1HUvBRyL_IaI9d8Hwm3_snLGJ379Jsi2YVs7H2NLDzMJm8wcPhAufn2sFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1ybsnH7dq4iSqh7hdj1oGe7Gx7qDzjTL4-w4bi-O3r9j2aMtzfOI05yLNeQ1wtne5_dyuPCp72vEGfGTGoJt4R1PTXBTNk7ket_PaqDPXySool1uX_kPJ7Q-_mU3kIbBfYHfMpY3H9JoZ3Cobl2DzQm9Czovxw4LeWs-oW6OBatS58Ni_7CXzcf4MdSfr3Y9IGwPfFKzBUPdnSkwUntrA4LmJZkmcaYkHUliYDQaRl--eZJE7ITCZLiB2MWbERximbugdf0cASCeDykpJI45QKyB_JBN7PX52k5HyhwzBUno0ta7VBk1rAVJs0dkgAhrCnHAz7MWnkbP6q26B3F1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmtJieNeb8gTKg76FkLkjk_ssT1LCIFpihjApmdt_5fFssJHHhS5j35nLSslfLLtFpmYRH0v63ss3R5swpN-i0dre3gXHTzvYGh3afot328yZ1pPbHhazdxkQUozyqNWhVBR1a1l5j3LmgdBxipJKqx_GpRwWlWP4JpyqnEmOZ2FvYjEBQIbi1JTL0Yy89tRGpjAcR674MuLF8pGWhKjbtfadLMiZVrctTEQtxydTp56sQYeC-OJs325xCgSthzSfiTb2cmMgS4V2HItCf5aReJwGTNgu3NxG3pPmoBHrYFvs36prCdrCg2JRyyXck1S5U6AJfjwhTiSLQXoPI-taw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=YX-70LWv_Y5vlrlCsLXLuBUMnUZJORR96s9rWiWHUEBa1J6gKNaOsh6vWpL3QrtZcR41mfaTDU1yuoiHbrdiZGa71T2C5_iUoxgijBknVzZOIj1UoJZL3EIeJWwO-gz9qc5Pg0w8O2J0PGSzcJ-AhzYC2UFiqlsoakP4lbETATsUmDPV9FsEyiGHVKJOoX_QYTbfJ9cxxOqGNthZ8L1WVX6_mQQ5F4_DwXXQ_54CZ_s_tUTODMga1tD_CQXV-RyARvM5lLeL3R9uca_FDAoITmyFeb7SzuZz-2uBjJfX_mvBTivFy_h6cwW0cZV-1akHrpo52lS2Tb-lIAc0r9KAGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=YX-70LWv_Y5vlrlCsLXLuBUMnUZJORR96s9rWiWHUEBa1J6gKNaOsh6vWpL3QrtZcR41mfaTDU1yuoiHbrdiZGa71T2C5_iUoxgijBknVzZOIj1UoJZL3EIeJWwO-gz9qc5Pg0w8O2J0PGSzcJ-AhzYC2UFiqlsoakP4lbETATsUmDPV9FsEyiGHVKJOoX_QYTbfJ9cxxOqGNthZ8L1WVX6_mQQ5F4_DwXXQ_54CZ_s_tUTODMga1tD_CQXV-RyARvM5lLeL3R9uca_FDAoITmyFeb7SzuZz-2uBjJfX_mvBTivFy_h6cwW0cZV-1akHrpo52lS2Tb-lIAc0r9KAGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=LQ5qWUNlHJOZlGg6Bhrm1cooImC-xPwqczyRRzk6L5F5ojjo-tLPyGU8ybpPUJOoLGNovVqxaMkj7um3RyGpnsu3uoB40R-dR54gd7j4FqRf8ow7CPIallzYvZ47v0KwMB4-Qi3qazKkyoqF2KkQ8RE4FtcfWVwbfri-y7ZaqB6hRwuwXxh7og1lzZVpq9vvA2JK2LYBLTzd2b-U3hmGcZ0k1X1EOqwu4EqDvnt8pS0gGQ36CbZogfYRtstij8LcAMasTKPdiTpWzU-CK6sUiSNZj7rmw1vDDp7DhpG82OoyXQVuxNgBnkXYQxpoqSCYGYS_X8nTH1dMXiK9g6WP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=LQ5qWUNlHJOZlGg6Bhrm1cooImC-xPwqczyRRzk6L5F5ojjo-tLPyGU8ybpPUJOoLGNovVqxaMkj7um3RyGpnsu3uoB40R-dR54gd7j4FqRf8ow7CPIallzYvZ47v0KwMB4-Qi3qazKkyoqF2KkQ8RE4FtcfWVwbfri-y7ZaqB6hRwuwXxh7og1lzZVpq9vvA2JK2LYBLTzd2b-U3hmGcZ0k1X1EOqwu4EqDvnt8pS0gGQ36CbZogfYRtstij8LcAMasTKPdiTpWzU-CK6sUiSNZj7rmw1vDDp7DhpG82OoyXQVuxNgBnkXYQxpoqSCYGYS_X8nTH1dMXiK9g6WP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=VJRLaP65KLtiQZCmUIEsEpBklp9fHqTlZyPREBA7avgxYiLowLDohrTguIDp2WOWzT4HeKFEE5OF4r2oRz9uDempoaG5xm0L9-TPELe94o1WJS__637jZ-SHfqVZhiIA5HMMwFCiRL5ZS_g0oXssojI-KY-g3dS5OF_-OKhN973ygtvJaYURkJTNmxkvywjuUE8RO40lnfJd2celfGT6ML6NvhcR5oLf2cN1GKdIGilgFKZT_IJOafgdtpWXSzJEvSBJRMWwSMNkA57C_GQQsD3P9uysXcKJeeAzkByJOJciH9M84ZT0cqFwD63YAWsQw0JAnkb99zvJK_0aUcaiGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=VJRLaP65KLtiQZCmUIEsEpBklp9fHqTlZyPREBA7avgxYiLowLDohrTguIDp2WOWzT4HeKFEE5OF4r2oRz9uDempoaG5xm0L9-TPELe94o1WJS__637jZ-SHfqVZhiIA5HMMwFCiRL5ZS_g0oXssojI-KY-g3dS5OF_-OKhN973ygtvJaYURkJTNmxkvywjuUE8RO40lnfJd2celfGT6ML6NvhcR5oLf2cN1GKdIGilgFKZT_IJOafgdtpWXSzJEvSBJRMWwSMNkA57C_GQQsD3P9uysXcKJeeAzkByJOJciH9M84ZT0cqFwD63YAWsQw0JAnkb99zvJK_0aUcaiGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=OiyVu2iY8ifl0yhwCR7QKDBToPzqYc20foggE62O36DOJjPn0AnZaekeleUF0gPWW57_JXkDJ6sdA5q_e2v3aLAWU81Jh4ekN5b0jaNSOIm9EgDkuR-_-ukZv8aniTTkR6VzCveCj5hshPMXSIsAcG22_9gi265eZk9dpKMPXgK0FgnnmyYwewE4Q1fHt3dpyJPYrMyo_sRb3sINOFmkEqkFEuBy-TJacE1qmlnX_eSy3a4QfowEjQC0R5Gw630XF0sdADZHttS0aMrr2a15_s6lASBXLG8rcekPkCISDCv9CrYt2KyXDxlBrFoos4t2uGPCv1GDZm_jTGfpwHNDgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=OiyVu2iY8ifl0yhwCR7QKDBToPzqYc20foggE62O36DOJjPn0AnZaekeleUF0gPWW57_JXkDJ6sdA5q_e2v3aLAWU81Jh4ekN5b0jaNSOIm9EgDkuR-_-ukZv8aniTTkR6VzCveCj5hshPMXSIsAcG22_9gi265eZk9dpKMPXgK0FgnnmyYwewE4Q1fHt3dpyJPYrMyo_sRb3sINOFmkEqkFEuBy-TJacE1qmlnX_eSy3a4QfowEjQC0R5Gw630XF0sdADZHttS0aMrr2a15_s6lASBXLG8rcekPkCISDCv9CrYt2KyXDxlBrFoos4t2uGPCv1GDZm_jTGfpwHNDgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=QtkJgWkYcWAl4KAT-ICpdhAIRaFe8vmTB0JGSkHuXridRB-tsWKjsDYlxd_HZFPL8imw_bPCGL83fzjjMKISwV-UPhFIJdu_EImk6FZzOJgUL5nPoV_yD1rrlCBpU5h87ZKlRfBnxNNlTHNEIIKuWGY17m3MHGWiLg4zLbbm-y_Y3yaWkZFDDZ2HAswIgJvWUmYouqZOYQ7RqsLdLnhMKUaKL7gpSF_13Hbi3j8n-eKMB3ZGZBmtQVf9_if81S8l1Dxt_q5kgclzpTW_l3VoNUKBmZofQQG6Oob05-OLcK0SkKyPfhbYK68RYhSSV5OSSlwrINvW_oeXOyRQt4mCJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=QtkJgWkYcWAl4KAT-ICpdhAIRaFe8vmTB0JGSkHuXridRB-tsWKjsDYlxd_HZFPL8imw_bPCGL83fzjjMKISwV-UPhFIJdu_EImk6FZzOJgUL5nPoV_yD1rrlCBpU5h87ZKlRfBnxNNlTHNEIIKuWGY17m3MHGWiLg4zLbbm-y_Y3yaWkZFDDZ2HAswIgJvWUmYouqZOYQ7RqsLdLnhMKUaKL7gpSF_13Hbi3j8n-eKMB3ZGZBmtQVf9_if81S8l1Dxt_q5kgclzpTW_l3VoNUKBmZofQQG6Oob05-OLcK0SkKyPfhbYK68RYhSSV5OSSlwrINvW_oeXOyRQt4mCJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZQv-VbIk-DE1ApXO8hQcZTwFDh2cD6JsNEpP6SWFgmxMrbCvDD-aCclksZsHuEb4yfZkC03qKr9aspmILuCtbqhtlMZe0u5aExZQnJne2VfeDzy0USfZzr5zjHA08sOm_WY_ACX-W3E89tmO41RsS9sfTpowoisxC0p0iFKXtqPVoOex1pwX5ekvjryeNv3FvKtbaXq57Z4CuKIqb4otBBbnHF0Ywr1lRivEWGpdm_rva8kliVYFFH8z0MG7fmVI_7-A5PHY1M0ytbcaD-BgoPpDq3-ujELNEUuMBByDpPzEzNgY2nFKw0zNyrg-ervDNKUKzgOlUSxHGV0ilRKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBE40y5eVOydZyC6F2W6WMj8r05SmtRnlSSOMPHpJI6kYch8-BjvvmWp0q2DFWclj3c2fZjqdoDB70Z1jbPaT6HVf_aiy_0GBHShe7-up9W1CdNvB28gkfy57nxZeiHBZc1_3ekpRX4t5-RHLIXXyJLF5Er8_aCgQF6L0BIPTnWqikE090UOXerQIZ8DdZSbGlIvpK1Uq1Db8Y5gDB7kbyq5RWzkjPO8fGWH-5FFtQkXz8wsCTcEtu57vEfomM0ZJi4NJ97s_gNGud_zfMfHyh246MSA1LBCSxsBzZQClfEz8fGgbaJNNWXzH0cerNtiGfOPjhWNUFmk8iNkzZjL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z1-TfPm1S_DdlruxLmvLg9cArpKoWp-jAnBxDYoToJ_xbm4H0GCtXmZX2EzoQxyuE1-tmTCMyDAnatx_m9im31QHoh3Mm2YivGCDpT-t-annZdQqEmbRwB6mZZ4uga-b0etECW1Xw00g0tEkWDRzZ0f07yddx8ceWhW3wdQ1QeHJob1DuU4gHjC0K2koqD909ssZNFtrH6dnSV1uSq7ElASk4GzRu3ntcSfVPr9Ltr-4N_MAjpcJuECqTPCs3yFHcaqgJXpRiDU_7-Fczj9mL8h51SEhRPXHibpmG3aPPfYDnMG7V4_1CW8ds9lnyubms02c-FL264AbE1la9v-I6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=trGWiH8I4Sb1eUHrRh80b39372ZO3wsM3eHZOWHaTnW6sZIxFCfm7LgDOx5xa1S5ihfryL2oiRkoTMjog_yL9rQy3LQd3nm_LDqwcqX9JgVxgHfdu1rWVZcMgZ8eVLInk4XUEpzV5dM5E6u_auoxpnzbtCanvro41m2IkzxTH3XQZD10Pasy0zS6oaOwhIOxsYurazrgtf2mcABaSJzPt6Fnw8j5chwTbGuz4MfCWktJj9pkr1FpJTeEy3uEjyYc54bMRihZADcWmaBOTb3OlZlDRiLvRnroygFLkAgTVGMnOhzhn2yzBLRc6lfH7DJRxr8c1pNKEadeMadlrqda_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=trGWiH8I4Sb1eUHrRh80b39372ZO3wsM3eHZOWHaTnW6sZIxFCfm7LgDOx5xa1S5ihfryL2oiRkoTMjog_yL9rQy3LQd3nm_LDqwcqX9JgVxgHfdu1rWVZcMgZ8eVLInk4XUEpzV5dM5E6u_auoxpnzbtCanvro41m2IkzxTH3XQZD10Pasy0zS6oaOwhIOxsYurazrgtf2mcABaSJzPt6Fnw8j5chwTbGuz4MfCWktJj9pkr1FpJTeEy3uEjyYc54bMRihZADcWmaBOTb3OlZlDRiLvRnroygFLkAgTVGMnOhzhn2yzBLRc6lfH7DJRxr8c1pNKEadeMadlrqda_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHe01_mYVouNfAxsFnXhuPmVsECeEC9judTma5QEEgLcMAOePcRaQ1cKaiOdydJxuMRhKBZXFNKtXYBga1VuYUXYM1VhcDwcHkrgc9y6WiuHpvdSp2Pmbr8dy7rTlGtp3In_SKzK2FVLAkQWTeIw61TmdCFI0UT5_V4JV_G72nlN3l1VmoNOkTimFahB0M4AecxjKBbY3anGG3Ykyxpep2Yn9lCc2XHU5Ay6I67ADZFka3dV_ePakgWL-qcoEiWXDGWZm09jcsJNj7W3iJClfzxBqxvUz6Z_HMpCqnbLK1Um6k6amgy-P11iZppUcO6Gp9o0oB-MwAG4lZ5yOZ360w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=eVObOuRWGVCceeaGv3fBx_lhEc9oQZ6UFxWA1itpOKptZ9FyP6bsGt07JIvm8oCs3DbTZzga4_4yvtPV3-MfE7myr1Q72Jn9anJwhu4pFj19CgP_7kohdzVwunLdVLSt_EqQTlHkl9Eosyzn3SLRAsRaDpF9BNDndDcmuZVUi0kNqj2UZVXqRZ7QRTxGSiVq6cJGAstFlaVP_r87z9HZ6OVaIMJ-HEPxl6Sx9gguCqsJKv0k6cFYPHY5HSFEx6S4PIlNz6vQeKHoVbiCyzh4u-NwA9eP2UX-ler9Vk-DT2BM7Re8G-zGTghvuNZtynq9e6re49dPyJuVuH3XfS6cmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=eVObOuRWGVCceeaGv3fBx_lhEc9oQZ6UFxWA1itpOKptZ9FyP6bsGt07JIvm8oCs3DbTZzga4_4yvtPV3-MfE7myr1Q72Jn9anJwhu4pFj19CgP_7kohdzVwunLdVLSt_EqQTlHkl9Eosyzn3SLRAsRaDpF9BNDndDcmuZVUi0kNqj2UZVXqRZ7QRTxGSiVq6cJGAstFlaVP_r87z9HZ6OVaIMJ-HEPxl6Sx9gguCqsJKv0k6cFYPHY5HSFEx6S4PIlNz6vQeKHoVbiCyzh4u-NwA9eP2UX-ler9Vk-DT2BM7Re8G-zGTghvuNZtynq9e6re49dPyJuVuH3XfS6cmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=Z89e2In3GD999epbBczgS0CZTc81LsKFNS9PidSAye3K_9MG-GwW0HzWZRnYT2tYi3VZXjrOfJoVJ-Q8Oz7PiGtWYt60Ze8oM_CcXlQtfsU5a_4l4xkh2_64YRDzWo1qWoNuAFaDLWM1yKwLj0U75FkdoiPZHI_7G8nDFpUDddgcuJFFmx8lrQ6JQjr3R4Orx9IZ5oGKM_75eCdwoO2_RnHt3BC7g8p763MIZsVlR3S3mWxCGL1HO1J5LUgKWfz2cZAd1YB7Nn-Ec6JeuC6F8Z_FMz8QamXO_15KPVVHWJ-xyYeIBtRz2Pw9J_SjKtxiJUOOlltf7VfL1ohXsn93Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=Z89e2In3GD999epbBczgS0CZTc81LsKFNS9PidSAye3K_9MG-GwW0HzWZRnYT2tYi3VZXjrOfJoVJ-Q8Oz7PiGtWYt60Ze8oM_CcXlQtfsU5a_4l4xkh2_64YRDzWo1qWoNuAFaDLWM1yKwLj0U75FkdoiPZHI_7G8nDFpUDddgcuJFFmx8lrQ6JQjr3R4Orx9IZ5oGKM_75eCdwoO2_RnHt3BC7g8p763MIZsVlR3S3mWxCGL1HO1J5LUgKWfz2cZAd1YB7Nn-Ec6JeuC6F8Z_FMz8QamXO_15KPVVHWJ-xyYeIBtRz2Pw9J_SjKtxiJUOOlltf7VfL1ohXsn93Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=M8TpAITN5dJLFuOUyn3k9LHheo_Cq4aOmW9PDDEwrzl1BkdpWT7GnB4LVk3M_SoSfefyI2zwbCgoduWSho-5dKfjUdiMLiNp6G0ZrkVHZYXmJFn7DxCjui3zVABmYaqahDyZjfs8SqyEy5Uha0FR5swCAGCzs4kbtcifw4tg-0sFqB8KxnZIYa_55UI-_76Di88Mbmi7toCQM31kb4raBuFJAZdhGEtgdixojbCg6awBnZGfeTI64qx_GjoaIXYUmiHH12F5tgx5bamsapaT6feBxtoUFRsQdBDY7MtlsFczz9rHoKiNAhhoL-G44Q2pdJ9zIg1OQaUZy9yJ7tcqxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=M8TpAITN5dJLFuOUyn3k9LHheo_Cq4aOmW9PDDEwrzl1BkdpWT7GnB4LVk3M_SoSfefyI2zwbCgoduWSho-5dKfjUdiMLiNp6G0ZrkVHZYXmJFn7DxCjui3zVABmYaqahDyZjfs8SqyEy5Uha0FR5swCAGCzs4kbtcifw4tg-0sFqB8KxnZIYa_55UI-_76Di88Mbmi7toCQM31kb4raBuFJAZdhGEtgdixojbCg6awBnZGfeTI64qx_GjoaIXYUmiHH12F5tgx5bamsapaT6feBxtoUFRsQdBDY7MtlsFczz9rHoKiNAhhoL-G44Q2pdJ9zIg1OQaUZy9yJ7tcqxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=HoONLriqSBWAi9W6SLZoUVu_sBQz03SxUXpqDWQdpn2SNfv4iFAdB-w3o3YV8JZGNjkZM5kbvmZXCzrkj8MyaKIIC2ZiP5xeoCBMBY9kkFP5-7u8k6EeVcmNunhmURVXB4mZoF0yELPXEADOUVIfPgJpDseq3w8GRaFTtIpRqaSIgLc_y1WGCZ-9Z4aC0RTl9HTDLwb-zK1BNm613tsHvwO7xK38HQZHaAoYSWw-W5kKxN7Op3OdE2uMQVty3BZJTz0cBTAxxuQxXKMJmdxeT5hk7CkUAm8e4akB0B5zAl_piN1DlsgmiYpG--IBQyBEpxrCoDPIp0lH1BTM7aooLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=HoONLriqSBWAi9W6SLZoUVu_sBQz03SxUXpqDWQdpn2SNfv4iFAdB-w3o3YV8JZGNjkZM5kbvmZXCzrkj8MyaKIIC2ZiP5xeoCBMBY9kkFP5-7u8k6EeVcmNunhmURVXB4mZoF0yELPXEADOUVIfPgJpDseq3w8GRaFTtIpRqaSIgLc_y1WGCZ-9Z4aC0RTl9HTDLwb-zK1BNm613tsHvwO7xK38HQZHaAoYSWw-W5kKxN7Op3OdE2uMQVty3BZJTz0cBTAxxuQxXKMJmdxeT5hk7CkUAm8e4akB0B5zAl_piN1DlsgmiYpG--IBQyBEpxrCoDPIp0lH1BTM7aooLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=PD9LDvAnHvFIZrrqwScLHm77dqcHNQEyI4y7vsKW-NNy1778UGLlw7SiffME95vlQorrSM4n8nEODquR_QvMfP2S3WwF1ttOd3tJQGN63drCCyxM4uE4I14JtRvdUXRHpRxkC1P90Lan15kUupae7WnvT4uGa9NNzgIHq80A0fjHBvxjPoCBV3AnE3iPOJu5YvJJj-K6yc86YTaICAIJRRbspDmOJBAs3kQTkLFbueh9_M9Ln6jXPpRokbs2CKHIsNYtnVT1MA05oGNGMy-wGerROsrVJ5LfgAOVJKd9y-72hhQ8z22_8rRW73Nyw6ehyHIFnV8kAZNA3tKGJJzIVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=PD9LDvAnHvFIZrrqwScLHm77dqcHNQEyI4y7vsKW-NNy1778UGLlw7SiffME95vlQorrSM4n8nEODquR_QvMfP2S3WwF1ttOd3tJQGN63drCCyxM4uE4I14JtRvdUXRHpRxkC1P90Lan15kUupae7WnvT4uGa9NNzgIHq80A0fjHBvxjPoCBV3AnE3iPOJu5YvJJj-K6yc86YTaICAIJRRbspDmOJBAs3kQTkLFbueh9_M9Ln6jXPpRokbs2CKHIsNYtnVT1MA05oGNGMy-wGerROsrVJ5LfgAOVJKd9y-72hhQ8z22_8rRW73Nyw6ehyHIFnV8kAZNA3tKGJJzIVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkGjC0gJS9IX8jo0WhWWnSWZjtbidFXumsMvDuzLYf9NIDx526AGHmEFbSwI0qGh_p53DT2HV4nlYuTyzmTt75BHcnmcIF_UapEzNB9lUOmHeA5A7HFz_ZejlyDu8NC9sbrEV22JcICv2Ywth3Y3Vp1FSnYe0Nb5wKwLv25Wz_bM85DYmU4YIyUZPbMEASESoLLcLRdQfkwqebXFDoamDAWHYr-unxv8hQR-_gBNeIl3CuPdPZBXc_hBqPQilOmLncXtHUtsnSGY27v75NU3DixFPMaj-D7BCDlyY2EzkQIgQkE5DxwjRPoIKhGfIXCqI_G3D-qrgPmscK7SZcH8iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSYyh9Z6WTaxAedVsmzBOczwgSooFEw7U0Qhcr_fpS3U3ZT5ClMP2fEU0Ak0snah7sYPDYFfjFRLu_eEs-NUvQiUjj0Fpi5NxEMdesob-o6QOpBXs2A7I_up5y80EYUwtZnNx00AcyfylC8urDFgshhGbq1tk-5xzgwVyiCemf2qL7YQiqIaliPkWNHmH3rVX3cAubrCZcdTG8NkigWJLJDHbSA3b_2u9iUzKZcQJ3FEGI-buPyYanWMt1xgRSak2buRzhOQdeQeZK5FhJjv1K49tNJR6LLpz4Cw5EojP4h0LKMuYfSR6Jb0-90fXWjfMQ4m8nM4y2N0czrjrhFn0vBvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSYyh9Z6WTaxAedVsmzBOczwgSooFEw7U0Qhcr_fpS3U3ZT5ClMP2fEU0Ak0snah7sYPDYFfjFRLu_eEs-NUvQiUjj0Fpi5NxEMdesob-o6QOpBXs2A7I_up5y80EYUwtZnNx00AcyfylC8urDFgshhGbq1tk-5xzgwVyiCemf2qL7YQiqIaliPkWNHmH3rVX3cAubrCZcdTG8NkigWJLJDHbSA3b_2u9iUzKZcQJ3FEGI-buPyYanWMt1xgRSak2buRzhOQdeQeZK5FhJjv1K49tNJR6LLpz4Cw5EojP4h0LKMuYfSR6Jb0-90fXWjfMQ4m8nM4y2N0czrjrhFn0vBvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=VCHAK8m3bJccROeE8qpPD_26IO9d8Mw-pccXVAP2TQTZNlS8sgkJQEIMEpvuPQ3Xk3GOAwyryPdspQdNBqNhH6ON4gWWLLT1lu3GEOBHGyGMD1piBYbmLqMqWQ38JjV0cJR_5uGgnQ7J1EW9Jc37o5qH5ssrsZvAqG5K64iA-aN7C0sn39XZVVzAuy-SxwAUajbJUWcjizwPvjp2YyWM19kR7yVn1W5QyFtjMZ1a4Y46XxFvYwenCuEpnLEojemsTScLrG7BKSeXDGds2BGyR0TTVdCfD5dbXUG5IXlvsZUhuAIunr_a0mV4b17D1BBQwNiZN17oNKNdJ1zezlnK6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=VCHAK8m3bJccROeE8qpPD_26IO9d8Mw-pccXVAP2TQTZNlS8sgkJQEIMEpvuPQ3Xk3GOAwyryPdspQdNBqNhH6ON4gWWLLT1lu3GEOBHGyGMD1piBYbmLqMqWQ38JjV0cJR_5uGgnQ7J1EW9Jc37o5qH5ssrsZvAqG5K64iA-aN7C0sn39XZVVzAuy-SxwAUajbJUWcjizwPvjp2YyWM19kR7yVn1W5QyFtjMZ1a4Y46XxFvYwenCuEpnLEojemsTScLrG7BKSeXDGds2BGyR0TTVdCfD5dbXUG5IXlvsZUhuAIunr_a0mV4b17D1BBQwNiZN17oNKNdJ1zezlnK6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=UB46MaeJePhk04-qFncOdYMWLcyOHeLYcQGTk66suMf5GWU3xvrSbL7sk7fKMAVfM6tvFJchbpleX4q4Hg1qXUBjwQJL3aLUpfRqUB4BZz5AnA-D_P26OLaRzaqlH4h_G1hZT7cjTfwjiCQSUPzI6SzRwfO592i7dw85EpgJVKvVY2t3RljGx7xqkCMgz6xh_OtHy62NtTlDoSrSzJh6SyzqBFz9IiROZrizM4f_CTyAIWtPFi0ZrzEfdDW7iKuqyzKzGaUzioqWVaO4fcoK-PLzUG6--Lgd59rkZCv6GS0AtaDfmb-roNqdsOZLzKqxlu8anlhYz1G3FGEvRNvyDrTPwdm5sGr857jxLRXiJ6VVo0EKJW1BuBw2y67cehbOTH65ed69qfbVcUCzP0qQIHlk-8RhcKaOvt-bd5ZWj2N9AZ2vlXQKL20mTrB3LIOdAh6Jq12RuJ7JNljTY1jFACcapGAPXbOMH_oroCPowxz0b2gP0UgnRJOJtS96l1zwkWEibbSxEkFyChe6JhgSf_3y7i8aTPeQG0PjGsVik4U-xFDo2O2zz-hmm_dBMxqFgK-nUtuiGPkyu-WYVJAshUAn-BOR0RP3gnMtSxyN7r6dp5eOcZQ0urp9S4G1sB3nHpS9ghWjlkLoIdKw1I_tpZAq462JaFYNPdRYlYZTOg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=UB46MaeJePhk04-qFncOdYMWLcyOHeLYcQGTk66suMf5GWU3xvrSbL7sk7fKMAVfM6tvFJchbpleX4q4Hg1qXUBjwQJL3aLUpfRqUB4BZz5AnA-D_P26OLaRzaqlH4h_G1hZT7cjTfwjiCQSUPzI6SzRwfO592i7dw85EpgJVKvVY2t3RljGx7xqkCMgz6xh_OtHy62NtTlDoSrSzJh6SyzqBFz9IiROZrizM4f_CTyAIWtPFi0ZrzEfdDW7iKuqyzKzGaUzioqWVaO4fcoK-PLzUG6--Lgd59rkZCv6GS0AtaDfmb-roNqdsOZLzKqxlu8anlhYz1G3FGEvRNvyDrTPwdm5sGr857jxLRXiJ6VVo0EKJW1BuBw2y67cehbOTH65ed69qfbVcUCzP0qQIHlk-8RhcKaOvt-bd5ZWj2N9AZ2vlXQKL20mTrB3LIOdAh6Jq12RuJ7JNljTY1jFACcapGAPXbOMH_oroCPowxz0b2gP0UgnRJOJtS96l1zwkWEibbSxEkFyChe6JhgSf_3y7i8aTPeQG0PjGsVik4U-xFDo2O2zz-hmm_dBMxqFgK-nUtuiGPkyu-WYVJAshUAn-BOR0RP3gnMtSxyN7r6dp5eOcZQ0urp9S4G1sB3nHpS9ghWjlkLoIdKw1I_tpZAq462JaFYNPdRYlYZTOg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
