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
<img src="https://cdn4.telesco.pe/file/vVIXrgJFeMi6eb0LnMzBxNjGM24XjofyA3_4f3C96VH4I2DpJxaRkAKNWVmt1GgcW5PHEJTtoX3YvSd6IGmwTc7XkDX19dFdc0J6zdnn4gu2Zx9COCeJfGQ_KoBV4dqv3qjZ0uxra3SzVdcQWK7_u-cBp8CNOzF89gf8ASXCtnE1Se9etS24G1Swa_VI7UdvwR383NiAT9rB_D1XHSwv_f8qHY6Ea-vyKR7SraXMY2kvdvQ0H7h06ZdTS7_iftVJWz3ix3gpcxtZLND6qnwR1Doom5dMQlMXukk7KmWEb7Cxe5kt7eWmt1DCQRoj3qcWBar6Ivi2kHQPbqUMXlrlnQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 18:34:28</div>
<hr>

<div class="tg-post" id="msg-463680">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c088ad7e9.mp4?token=I7EF_xawBGhWViAbJHkh6rMOPs55stYzGj0jZvkxsvkehSjVx1zjJlEpgSGjiPHhkoFETtuCRZUOig6SnaMRaJuQuO7CvTCnvbwbA-tf-wsCVly0F3I_vf9z-F__rN_JVhravewdheuV6nfXpXAnoERTEBfiEBIKsx98_p5-aM8AfkV7MEnBVa6jXueUDeblHGqirsmraivrJxXtVNH7jVM-I_BTaPdogD6kr5W9aZ0ZLXUltfUOXkNqnEehvuu5m1VEkHZL6r6fLODdp5Ar24ZSvaSrK7NRggrayz9uBM9gR8TvFkVC3ABAUbua4Vt37z-g3CSXnNo0hFBD4d639A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c088ad7e9.mp4?token=I7EF_xawBGhWViAbJHkh6rMOPs55stYzGj0jZvkxsvkehSjVx1zjJlEpgSGjiPHhkoFETtuCRZUOig6SnaMRaJuQuO7CvTCnvbwbA-tf-wsCVly0F3I_vf9z-F__rN_JVhravewdheuV6nfXpXAnoERTEBfiEBIKsx98_p5-aM8AfkV7MEnBVa6jXueUDeblHGqirsmraivrJxXtVNH7jVM-I_BTaPdogD6kr5W9aZ0ZLXUltfUOXkNqnEehvuu5m1VEkHZL6r6fLODdp5Ar24ZSvaSrK7NRggrayz9uBM9gR8TvFkVC3ABAUbua4Vt37z-g3CSXnNo0hFBD4d639A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: بزدل‌ها و خائن‌ها دوست دارند بگویند آمریکا با کمبود مهمات مواجه است، اما این‌طور نیست.  @Farsna</div>
<div class="tg-footer">👁️ 352 · <a href="https://t.me/farsna/463680" target="_blank">📅 18:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463679">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fecabc4311.mp4?token=aru-fzsW-UZABMoH0P8IFhPJeclA_PSj3VDrjkSmwfdso8cLewsCRgmWH1zTMPD_-_X78ZWADTjFnQFqz_KDmrv41k5liz-t7zD7JcWzJuPaSLtuQ0BmAEPjh06AFIlmK4CQwq6RwlQ3FMz7FLBQ8X8xcb2Ih3a67cFK9TGOhowIcsBdGS0YOmAKh96aspP2-3bAwyh5Ga8Nr-nMgXE0NWOntBcEe1PRPEvrT0gmlaX1nRGd24p9v6SW-pul54bFWQPy-IBb5SOAJqZARmPCd8vcEhfhLw9PrdrtbIMGi7CDs07Bec4WxEmgj_9rDYo6-w7tIEIvwyaPjtyWYt0vfqPzjYIImiLIlit-8nzVYEs1oaQG2PVU-2nRrZOQaJNDD2hcAwiXpf2-ysOuoAIiwdC4JLjWWW2u7kCrOUWeXMoT8m2-0GW2yEw8Ihl0VMO8rgVuKU5NTxvf4bM9ZDmjo8aPwGvzllX_vru7YuNReQxbJ45y51Fyhp4Ioynn2vQn3V6GZ7uxmkCNcO2lFq7UrvLyNLL3j58_eyP2GgcoGJHNuCkQjVD8OlhKpuh27Ue3TnZEHFoptrhjncZJ5HFz2mrLrd6MyB9J_6n3roJlfjJZMJRpLwmXXK1Mp2Xweb3ivJiz8Aiy1BUFIqAU3QgaDzIxIGkZ-23iNYMsQkF5a48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fecabc4311.mp4?token=aru-fzsW-UZABMoH0P8IFhPJeclA_PSj3VDrjkSmwfdso8cLewsCRgmWH1zTMPD_-_X78ZWADTjFnQFqz_KDmrv41k5liz-t7zD7JcWzJuPaSLtuQ0BmAEPjh06AFIlmK4CQwq6RwlQ3FMz7FLBQ8X8xcb2Ih3a67cFK9TGOhowIcsBdGS0YOmAKh96aspP2-3bAwyh5Ga8Nr-nMgXE0NWOntBcEe1PRPEvrT0gmlaX1nRGd24p9v6SW-pul54bFWQPy-IBb5SOAJqZARmPCd8vcEhfhLw9PrdrtbIMGi7CDs07Bec4WxEmgj_9rDYo6-w7tIEIvwyaPjtyWYt0vfqPzjYIImiLIlit-8nzVYEs1oaQG2PVU-2nRrZOQaJNDD2hcAwiXpf2-ysOuoAIiwdC4JLjWWW2u7kCrOUWeXMoT8m2-0GW2yEw8Ihl0VMO8rgVuKU5NTxvf4bM9ZDmjo8aPwGvzllX_vru7YuNReQxbJ45y51Fyhp4Ioynn2vQn3V6GZ7uxmkCNcO2lFq7UrvLyNLL3j58_eyP2GgcoGJHNuCkQjVD8OlhKpuh27Ue3TnZEHFoptrhjncZJ5HFz2mrLrd6MyB9J_6n3roJlfjJZMJRpLwmXXK1Mp2Xweb3ivJiz8Aiy1BUFIqAU3QgaDzIxIGkZ-23iNYMsQkF5a48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها موشکی ساختند که قادر بود اروپا را هدف قرار دهد و به آن بسیار افتخار می‌کردند؛ امیدوارم اروپایی‌ها این موضوع را درک کنند.
🔹
هدف ایران این بود که در پشت این سپر موشک‌های بالستیک متعارف، ساخت بمب هسته‌ای خود را تکمیل کند. @Farsna</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/farsna/463679" target="_blank">📅 18:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463678">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb9cc48d1.mp4?token=AmrTPedpzzZpljSd-RLD_1l8rcwspKVDiPhLolYljDQWwvNH2IUUVdUwNK_2NqXbAW1fcHasayK-IhbpbXM120GZmdWjdo3sArxRO--2s6Z9wMWg-1PVAr0DA2fs-rm0XEY2EXldXeT6aWAIoLKZbmO0F0qjstFlj8qAs3t1jj_a9XAOJ6e4RmRQB36DpVcrjpMWQC5GhmgTXVitSnWBVH1YT8cKK4dJwQLzuStUeSK0m_tXyobaZ4cfWUrmX2H_2hqhXpruNwLKPe3hJKM2pKEbkpOMOYDdBG4UYPMkqenSfWlTTo-CrayhhKQxDl-okwpiZMAm8fCag_YmlZsftw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb9cc48d1.mp4?token=AmrTPedpzzZpljSd-RLD_1l8rcwspKVDiPhLolYljDQWwvNH2IUUVdUwNK_2NqXbAW1fcHasayK-IhbpbXM120GZmdWjdo3sArxRO--2s6Z9wMWg-1PVAr0DA2fs-rm0XEY2EXldXeT6aWAIoLKZbmO0F0qjstFlj8qAs3t1jj_a9XAOJ6e4RmRQB36DpVcrjpMWQC5GhmgTXVitSnWBVH1YT8cKK4dJwQLzuStUeSK0m_tXyobaZ4cfWUrmX2H_2hqhXpruNwLKPe3hJKM2pKEbkpOMOYDdBG4UYPMkqenSfWlTTo-CrayhhKQxDl-okwpiZMAm8fCag_YmlZsftw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ایرانی‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصۀ سیاست، موضعی تزلزل‌ناپذیر داشته‌ام: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد. @Farsna</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farsna/463678" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463677">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ:  ایرانی‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصۀ سیاست، موضعی تزلزل‌ناپذیر داشته‌ام: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد.
@Farsna</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/463677" target="_blank">📅 18:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463676">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NniDftPetY89TlqN7nmGwiJfNcJNDKhJqDoFlKHEFReJ7NdqZfK9q9sNoNME6bX6WMeSRn_2eTvZOdQvtzo4OQvpMwTbODuoyN0o_XAvihSpAfIOslxjqTS6XYHuc_qpaMflpTN5F5Ws6L5MQjvQTXNLdfLnaCphlm5OUu2LpVOVqTTFQPjy5addxIscSUNVqwFfDnIp5EyZpgZEiDaR0_v1ubAvADd8ocd4bhUp2RyfTKmVwUi3kwxmv1LW_3Odpe1472vCXl68HcS5-edIOBcrJdBXWdLoAgc6zo-jXDqcUHxdSq_yPQJ-6qKgRN6tISxYaM87bEkBiCa1dJpI_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: معلمان شایستۀ آن هستند که در مجامع و زمان‌های مختلف مورد تکریم همگان باشند
🔹
ما همه وامدار معلّمان خود در هر مقطعی از دورة‌ تحصیلی هستیم. این قشر عزیز و محبوب که اغلب با خالص‌ترین عواطف شاگردان‌شان مواجه می‌شوند، شایسته آن هستند که در مجامع…</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farsna/463676" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463675">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رهبر انقلاب: در آستانه سال تحصیلی جدید یاد دانش‌آموزان شهیدمان را گرامی می‌داریم
🔹
اینک که دروازۀ سال تحصیلی تازه‌ای بر روی خیل عظیم دانش‌آموزان و دانشجویان گشوده می‌شود و راه‌نَوَردان علم و حکمت با امید به توفیق الهی دوره‌ای جدید از کسب دانش و معرفت و مهارت…</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/463675" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463674">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is33ZmhpuX8sQVAyeacWUYjMp_ad1L3kDiCTc9XIzHENUwGppQwSmMILOELyF-D08IyUGcEe3KssP4VwcsV2PHN4Jlc8lI5ZB13UZjgb3It0VYRgOdLhLnOL0Hr-OO3-B2Tj839YunwclSwouOK9stMcbr3TOMrQh7QIh2m7JyULzOi1Sk2Vjpo5hn-94pqs4ueLFae4UdODH_lkyeHRYb3kR2Fk1R9AVAWXKBlD9QlNgItf8DJj3fZjcMGjMUmegekcfw32QZnXUOlRrzghLUenodCcp2HWMX6y1Eyke-f7sdNFDIh9LE18NnaRdbcN-2Zc2aQUPkSUUexKNv_lHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: آغاز سال تحصیلی نویدبخش حرکت به‌سوی آینده‌ای شکوهمند است
🔹
طلیعۀ سال نو تحصیلی و بازگشایی خانه‌های علم و ادب در مدرسه و دانشگاه‌، نویدبخش نشاط، امید، و حرکت پرشتاب ملّت به‌سوی آینده‌ای روشن و شکوهمند می‌باشد.
🔹
آینده‌ای که تحقّق آن در دستان…</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/463674" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463673">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رهبر انقلاب خطاب به دانش‌آموزان و دانشجویان: مرزهای دانش را بشکنید و قلّه‌های پیشرفت را فتح کنید
🔹
مسئولیّت امروز دانش‌آموزان و دانشجویان، سعی در مجهّز شدن به علم و تقوا، امید و اخلاق، و دانایی و توانایی و زدودن پرده‌های جهل و تاریکی است تا آنگاه که با شکستن…</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/463673" target="_blank">📅 18:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463672">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsHVJQaGjZACPftDlGvCDxBUZtNcVwvy-srDnd2QJMzmWOfPDoct-6-OagLXK2w6WAFKc9rlA90Zm5Pi4RrNdJS8tlE-4ck4sxMp6kEqGnHZZs5q6zSZJX1FeNh5tL5YAlHca_BRXjgWN0hkORKkPTsoMPj6WeKG6uOIM3JEWo1tTohq0BjmWMHy8kCRGa-LhVLbA6zPXHQpJu-u5koY3MuD8O3m5zlt93wo1lus50k2ATbHEkBbdDm7U-UEbf62TdY4GR_OsvQuwX0bbLGDVohIFcyOgnsTsULnaeek930OHf0jI4tPQB4uEnzko_Fd7OWEQfD3EnUMmNLEVUnWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: قدرت برآمده از دانش همراه با تقوا؛ سپری در برابر توحش نظام سلطه است
🔹
اکنون در روزگاری که توحّش نظام سلطه خصوصاً دولت جنایتکار امریکا و نظام جعلی صهیونی بیداد می‌کند، قدرت برآمده از دانش همراه با تقوا و اخلاق، چونان سپری پولادین و شمشیری بُرّان…</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/463672" target="_blank">📅 18:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463671">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌ رهبر انقلاب: فتح قلّه‌های پیشرفت، مأموریت تاریخیِ دانش‌آموزان و دانشجویان است
🔹
مسئولیّت امروز دانش‌آموزان و دانشجویان، سعی در مجهّز شدن به علم و تقوا، امید و اخلاق، و دانایی و توانایی و زدودن پرده‌های جهل و تاریکی است تا آنگاه که با شکستن مرزهای دانش و…</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/farsna/463671" target="_blank">📅 18:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463670">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
تا ساعتی دیگر پیام رهبر معظم انقلاب به‌مناسبت بازگشایی مدارس و دانشگاه‌ها‌ منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/farsna/463670" target="_blank">📅 18:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463669">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVuLo5IKfl3-bBwHguIKJoWWbLhc9JvJmED1Zn2_wqGOydv9JaQj4LaJXPVCrETTVtafY8dKjLEM2l3Fcqv2oYoTR1EQozo-jxe1hACza8X4OFfID-I1IdyNREug_loqTo-3nWXtHC4tCFKZa3IGmx4oPr-P9zk49DMlYAu8qIUCJgSn-isQDQMF567VEwkhqNMjnqVOR-GYqo3eLSUhnZw8NHAFs5vv0xyY_oHuj-4E8cLIVCLx1rxpKlyu9wExNvA1qLpf5nqK-cAqlrv-bJ6xFRNI-zsTUQU_ZjzgzxF_8b2rhgJJ9ALSalBEzheDjvkY35uPQ7scOQY_SunZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها از سقوط جنگندۀ آمریکایی در آلمان
🔹
رسانه‌ها خبر می‌دهند که یک جنگندۀ اف-۱۶ آمریکا بعدازظهر امروز در پایگاه هوایی اسپنگدالم آمریکا در غرب آلمان سقوط کرده است.
🔹
شاهدان عینی می‌گویند که یک جت را در حال کاهش سریع ارتفاع دیده‌اند و سپس ستون بزرگی از دود سیاه در نزدیکی باند فرودگاه مشاهده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/463669" target="_blank">📅 17:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463668">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VckHnc6hfOPzCMwODLvkrbxlvIUB7-R1VVblDB9JcfiYVdOJyry7JogImUs8l-SOqI_eESBBazebwhqeLt4XNDsCHHCFghM6QZisy8FWo2qjr9pq4Ml3q_kxqWXumUfq2BfpVQ-SqUbAY2YQJL_MVRrLxgInfEEBPzQgjaK3gTvFZRCktSHmeM82fa7GNCF5JG_CLLrLVnwF_rPyRGfMxCxBCLsELpzC0oYBAxrrPoaDywRJy_bpVu5bJ4QBsYetQPUD2mSNRSH2Oz013JECWYVuSmR__uXBb-FIeWhK5JAWnHfFW8lorkzMhKQNNNMxanDUMevCBEeuKKNCSWmOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنزین خودروهای فرسوده با یک شرط قطع نمی‌شود
🔹
طبق اعلام مدیر نوسازی ناوگان حمل‌ونقل ایدرو، مالکان خودروها و موتورسیکلت‌های فرسوده که امکان نوسازی فوری ندارند، می‌توانند با ثبت‌نام در
سامانۀ نوسازی و اسقاط
، از تعلیق ۵ ساله محدودیت‌های قانون هوای پاک از جمله حذف سهمیه بنزین یارانه‌ای بهره‌مند شوند.
🔹
این امکان از امروز، سه‌شنبه ۳۱ شهریور، فراهم شده است.
🔹
پیش از این، جمعی از مالکان خودروهای فرسوده در پویشی در «
فارس من
» خواستار
تجدیدنظر در قطع سهمیه بنزین یارانه‌ای
شده بودند.
🔸
ثبت‌نام و استفاده از معافیت قانونی، راهکار فعلی برای حفظ سهمیه سوخت خودروهای فرسوده است.
@Farsnews_My
-
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/463668" target="_blank">📅 17:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463666">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvX4iG_SaICQvNighR928-Pptn3dR6RWYxTmFv73Bdy9vW3Gemib17McVEWCcFVnJAZYC-I_JJsnzMZ5_6hczJekOhVpv1-wMlcv3gXqXKUMYk7ncq94_Bx5CA1MwsvC33bHBolqcT9_C4n2DM5wfBENcD7uUHWDsddtAxywai15EJYbTxdM1-qG-IeIfVOiAHWPrYD29Sd96e7glQtWhGzOdayOzKDaamMZKye5Fu1HWvOBZYEo-aK8-4SsHaRPQ-hTp5B4ujl6vvXseDsdZF0637b4fyB4BwModD3I6efUCajKApGK99hUIIb4Hil8Ev2RjKKptsFDL4UysXbghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تا ساعتی دیگر پیام رهبر معظم انقلاب به‌مناسبت بازگشایی مدارس و دانشگاه‌ها‌ منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/463666" target="_blank">📅 17:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463665">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff2847b8e.mp4?token=PVq1CUKc0YGoMRD6MOhRu7o2Pf5RlNVqraOhJicJl8blRfP7PncWEDeJYYyygOHpXY9f00iFSp19uuzhXUq4XEYmdXQc4PTib2R5hxFJryHah1vLhndOVALRhGOkfK5kheClEwCv1jneuN7Qk3wTWLxyJkDgj96cB19TYEMdj-OBdjIOUEWd47MaRpKOkwHcYofW-wDrHOTzOIw4-42n3gj1d_SVcQSkwlDAclx447pXWjlv74onhOrqasHrFh24j5vrSVBcOmk6x4ezfzM1DsvMYrIlVSYq28CzCD9KzGkx2tppBojhPwB1D4D-idYHVcjXooj4t_TET6ilidKOTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff2847b8e.mp4?token=PVq1CUKc0YGoMRD6MOhRu7o2Pf5RlNVqraOhJicJl8blRfP7PncWEDeJYYyygOHpXY9f00iFSp19uuzhXUq4XEYmdXQc4PTib2R5hxFJryHah1vLhndOVALRhGOkfK5kheClEwCv1jneuN7Qk3wTWLxyJkDgj96cB19TYEMdj-OBdjIOUEWd47MaRpKOkwHcYofW-wDrHOTzOIw4-42n3gj1d_SVcQSkwlDAclx447pXWjlv74onhOrqasHrFh24j5vrSVBcOmk6x4ezfzM1DsvMYrIlVSYq28CzCD9KzGkx2tppBojhPwB1D4D-idYHVcjXooj4t_TET6ilidKOTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی با وزیر خارجهٔ ایتالیا دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/463665" target="_blank">📅 17:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463664">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_ceDN_tv11bLRY5Vsvc5O8PS59_MSGC1COqH_J0PsyX1hl_cS196Q5ztLUpfCAzWKuy28XnJ5ileJjhqHvGMCxbK8NhZ6ICxgsGoF_0Xgmrhi4hsHPTZNuKZ2uoS8dB--jwSuB-V9iu0DSTq31Pa0iW0kAyfQZMfHVLBDXsr9HX6pPapdetPo7NbbftE8SWsxQGmcbi6sOlzXYGDI8mGh72hkhoCihkv_XRU0dZFpAweOrImKDTiSUOK1GuusDzLdrAFjxSWEaYraQzFnTw_Xodq08JYmgK7Vbv6E5IxhdB9WSVyvLdNXnddrCVoR9eWuffzPFqc84dkZLG7DRBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعهٔ مذاکرات، نفت را پایین کشید
🔹
انتشار همزمان اخبار مثبت درباره مذاکرات ایران و آمریکا و احتمال بازگشایی تنگهٔ هرمز، بار دیگر بازار نفت را تحت تأثیر قرار داد و قیمت‌ها را کاهش داد.
🔹
در تازه‌ترین مورد، کیودو و رویترز به‌نقل از منابع ایرانی مدعی شدند تهران…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/463664" target="_blank">📅 17:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463663">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e713acdda.mp4?token=ZYzIDP6bijko3EMO4qiE0HRzazTHoxoBGwRfY6EmDNAr9QL_DjnquBRIbfYKpcwRFmO7ZJllddT6IDR4aSeY50IsMC9DSv4jV-kbi4zKL4o0hYC4LLAhkRLRWBhCYoxft52xD9whQXCqjgIowX2we2KlZ7XBrrWJaOrFtKO2WKymWP7opR5w4RUJ-5-Z3v_oLXotXWE41_83_SI55STTRq3u5-bzRMvkxuVBq5tuCJBriS4aOpRJFA_IC3sO1WoreLGWflYhjDJB6_t-jj1xCHd1kP1hJta5Gj524orxS5f6SRoAamUQTcQl86KYKyKWW2APeAhnQAQ4wSm1QkkwPxK22aox1XrY8EajaKm6GHHyQFAYFxymj9IQISxmBo1erlmXiPj7qKt3Eo-GSa3CmsWiSx-bWRhCQjACn4OkpiOoXVEpyRNSsv2CFJFBGkK2yr5cfXQ5CehlVB2AiEwmqO7MKmCM4e_mft0a9YsWQLZk7CAAi-6RGtS7N7C14TuCEHhOcHmyPEl2cTX1xWnPibjN4jJdjXA76ZG-aH2uuA0Tyls__mMbQMGaMOCdSQY2aHkiy7SQAdd42WxnuURzE4WmA_bamNgROlVwbah4sZBsNqpe_jq9IVznCH7jG9XygAFRd5uB4gnFpM7gQLmXVvniKeYsJWp6n23cwUrRQIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e713acdda.mp4?token=ZYzIDP6bijko3EMO4qiE0HRzazTHoxoBGwRfY6EmDNAr9QL_DjnquBRIbfYKpcwRFmO7ZJllddT6IDR4aSeY50IsMC9DSv4jV-kbi4zKL4o0hYC4LLAhkRLRWBhCYoxft52xD9whQXCqjgIowX2we2KlZ7XBrrWJaOrFtKO2WKymWP7opR5w4RUJ-5-Z3v_oLXotXWE41_83_SI55STTRq3u5-bzRMvkxuVBq5tuCJBriS4aOpRJFA_IC3sO1WoreLGWflYhjDJB6_t-jj1xCHd1kP1hJta5Gj524orxS5f6SRoAamUQTcQl86KYKyKWW2APeAhnQAQ4wSm1QkkwPxK22aox1XrY8EajaKm6GHHyQFAYFxymj9IQISxmBo1erlmXiPj7qKt3Eo-GSa3CmsWiSx-bWRhCQjACn4OkpiOoXVEpyRNSsv2CFJFBGkK2yr5cfXQ5CehlVB2AiEwmqO7MKmCM4e_mft0a9YsWQLZk7CAAi-6RGtS7N7C14TuCEHhOcHmyPEl2cTX1xWnPibjN4jJdjXA76ZG-aH2uuA0Tyls__mMbQMGaMOCdSQY2aHkiy7SQAdd42WxnuURzE4WmA_bamNgROlVwbah4sZBsNqpe_jq9IVznCH7jG9XygAFRd5uB4gnFpM7gQLmXVvniKeYsJWp6n23cwUrRQIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از تلفات سعودی در حملۀ نیروهای مسلح یمن به تجهیزات و ماشین‌آلات نظامی مزدوران در استان الجوف  @Farsna</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/463663" target="_blank">📅 16:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463662">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌ چراغ سبز سعودی‌ها به افزایش سهمیۀ حج ایران
🔹
معاون سازمان حج‌وزیارت: برای افزایش سهمیۀ حجاج ایرانی در سال ۱۴۰۶ با سعودی‌ها مذاکره کرده‌ایم که چراغ سبز نشان دادند.
🔸
ایران در حج گذشته سهمیه ۸۵ هزار نفری داشت، اما به‌دلیل جنگ رمضان و مشکلات انتقال ارز، حدود…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/463662" target="_blank">📅 16:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463661">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca659922b.mp4?token=MkKe1fBqa-zsD6ZaaTksC831BI5Tq5i_AsSPjc8WP3FIPrAoQGkGna4S5ILlMFx2BakzRaeLLNDvTLiLIYPcyDpO3aBlyz2l_Q2ReHABGAuSFvRKGrtnt_StxU7F0vp3sLeVo0j2m3TVU6_cAybexjQb-XGI4wnWWD7q1PpuPT0ufU6Qz09eQmObawvwugs27lh8O_bgyknp6DjGGKotlDjxWKIhajL7-lc_FVdCHVzxWEptjrVr60JiKKtgowFil4zP7xu7YBf1FRiSYaGvAGY6QieXcNC8B0sG3MtmzpiAEhOJ_jp70j0vDE7lz9VVV61rwhAl_IVxcuFeyG9Ljg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca659922b.mp4?token=MkKe1fBqa-zsD6ZaaTksC831BI5Tq5i_AsSPjc8WP3FIPrAoQGkGna4S5ILlMFx2BakzRaeLLNDvTLiLIYPcyDpO3aBlyz2l_Q2ReHABGAuSFvRKGrtnt_StxU7F0vp3sLeVo0j2m3TVU6_cAybexjQb-XGI4wnWWD7q1PpuPT0ufU6Qz09eQmObawvwugs27lh8O_bgyknp6DjGGKotlDjxWKIhajL7-lc_FVdCHVzxWEptjrVr60JiKKtgowFil4zP7xu7YBf1FRiSYaGvAGY6QieXcNC8B0sG3MtmzpiAEhOJ_jp70j0vDE7lz9VVV61rwhAl_IVxcuFeyG9Ljg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی در حاشیهٔ نشست مجمع عمومی سازمان ملل با وزیر خارجهٔ سوئیس دیدار کرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/463661" target="_blank">📅 16:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463660">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aee677ae2.mp4?token=DYY0KHSXdkuLFRbi_M8EZKHr8CZ7xMA_C7SEEM796Bgmzbq-nqoqVUrW618SeX7i_uvHfIWYGPp6fvLnAPEFi8gW9cA-wyWlNIorc6GJiGKGuZ6x62IvsC2lNZAaxK3buFS0V3HQ9Sr2LPqsZLDE-F4gO4LNP_bJpkBLMkLYc6hnJkSROXDYXJkosrl2bDoRnACif4-0KfjFXyeapQtA_gPTRidyS21NpGsmPQMWd4kpLJA94Px1ccUUQh8u_1Z48usY2Vi3FqvUQBhStYm7UsoZ-wlR2rG4midb4aXqhu4Dkh30cG0KivOYNBan_1Qjm3XFhDt_Cet1yzncwKcyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aee677ae2.mp4?token=DYY0KHSXdkuLFRbi_M8EZKHr8CZ7xMA_C7SEEM796Bgmzbq-nqoqVUrW618SeX7i_uvHfIWYGPp6fvLnAPEFi8gW9cA-wyWlNIorc6GJiGKGuZ6x62IvsC2lNZAaxK3buFS0V3HQ9Sr2LPqsZLDE-F4gO4LNP_bJpkBLMkLYc6hnJkSROXDYXJkosrl2bDoRnACif4-0KfjFXyeapQtA_gPTRidyS21NpGsmPQMWd4kpLJA94Px1ccUUQh8u_1Z48usY2Vi3FqvUQBhStYm7UsoZ-wlR2rG4midb4aXqhu4Dkh30cG0KivOYNBan_1Qjm3XFhDt_Cet1yzncwKcyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر بهداشت: کرونا نیاز به واکسن ندارد و شرایط تحت کنترل است
🔹
مردم توصیه‌های بهداشتی را رعایت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/463660" target="_blank">📅 16:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463653">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lfsfZLck0Rq0AoVdEQIbOkZXJGDfLNVj-y4Lsm9ry3BUfQRn_Ck5JhryXQieFabrcsTtq_PKP9pqoXpCpZFZNJHsyqUiQ8PKgXqro8DVNYzpLY1zqt2lNgFmSRj4lwMIRxXTHth7i3Que2MLhsdtBoqR2b7DWgvyUf0WhgF-3AENEtREPnrOpscIa3u4qr8JcKt-xpn8YkcJtGAH_6zaRDaHgmKIRo2Ax8uSWFQF2S8VuchQKy13pfJH3a6foECelxQkd4-kHXFgxx932iyX59EmSLl8U6n_JkpcC5KEj70wvWDZCqSM7LFT4on8Vh6IaDpMEstAwkEJIvUeetSPew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBTPSNA6EKGhZoI8zLboWZS9XPMUYLz2fGXMgbHc-t0mrcOgUAhy6So24iM9qGEpTeZLewf2NJ-arWkqvucGRDwk6rFG-BQtFAuLz7HD_b_UfB837wau8TVrSePXUBbOJGN0YiKErpFngYzBTQJa92b7zAS53JProPwHi_ThObimlX-_Xm56FaFYhU2_b81MfAULM-vwETIFCukYzekyWrIeeXRax0tcC24-5aGTCZiOC2ksXp9q1lsgb7x6yXgYZoA1uAvxYxVhDDXnslaLyzNiBODF5IvGaFgI8BYKxoj1wC904yuWuCf3b-ul7WhFu_tI1_LiL8EoFjvMuZdKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnfPHaXw-FAjsncz_1KaDdgRJO6dC0tS1erqGRlF5FxyXXpFYK2crzNXlkzqPA0Lqa0R9sd734Lao1hKnSdbG9CKyYFUxEaZ2VVGYuNEWiS1c_XT5AOsv2h8FKruJtz5-GEJ9HLPep7KO0Lagh4_PwpCzVCpzPzFhSMkkRXFh4FxJDpbufX_28_inGlwtdOxX3Jr2-d0HCTjn1f10RB0XdNqEDFvaKYErKadrBaUoYz9iWYpchHcAmXDv-LNGwlbbqdG0YaRCLjwz1FgXmummFAKFHOIvelh3rgug1jBRk7_V7DN5IjHSdpA7ffkfIaKKr4zu-PujBNDngTry7l33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOiRDHFD0ehvXxRQL18eunN4yw_9iKnoKsYxTny-4uOiInMKfZGFXUIiWNXPM9zflF58Gvq1hoyUcc-BTXldfxp_PlSSCwF3b4MzJu39OUowacHePfyeVd6vaZkArJh7xMTWCrm63RUK_BdXS1PvjDD15Pbnnlg6wUlElo4uqpBlse2_PidFBy0J3hFbxk_Fvey8FNnJA4vMOYLORuzs81RjGYSXphO-NlVWMQO2V5ISZcB6SpyFNdRcbNOaOTkX3vlkSwP8itS1t8_6-3N44DknCJZw_1UoVGnJWr7FYSTSm_s_URA2juvPIrLfYmIpHszmigM_bMmFNIuVIWh5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IVHoRRttVJ4s6uYWTcxD1HPagSZi0A_jvrNXwuNqEdFXCKFePE2H_pXr_nBwR6Y0ze5C_HwT6ibpqENzKxwU1dj6GA3x5fooq_pX3T8iGQzeCNM4VXszWyARdyisQHoWqxiCHMRmfGaAipQejJxUyAmupubFzEGbMdCgsFTySxnpOmo7SIMT8o_W-5mqd0b4JGpqN8LoDmg6vbLw-QQ-LLs3nBDZqlQpwZXPDxhP0_CaKinwOzrnDOKpNhDr567xdQLxDiEsHH1EiF-J0CvwmSqp907wp2v73V32-hgW-HQC9UIN-ZZ0xoDKdWK2_ApBnUOS7qd-bBrtjG6k_JvoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1JEgqGxmPpEioP1ZDPRU1CtXZ7lC74_nZyqtV4vGplj-N5sxkcT8frjB4y3S1UUx2ysI0ESKDURqM1uRuPP0cIXD3bstzEaLsIzw-dsonMZ7noiwZX7pJJaD8je2wnsRIo8dWZp5hAVCT_FDJ4jBCfgTYsrpdxy7reDQyJjvCWu12ie7j2l9pbqE1IaC3OciKH9Q5HexDin43DF9c0q4cOpeH7GG1NbwrJsjTImbULWtzqSq2Obdam7Ro2LVR-FWeEHpekSLOK5FP6TUvlJFIZebaIF753BBrPcrP2mwnnA288aUKD5ZelOE4Xl5kMxfkX5Y9af8XJBw12jtWwD_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARtlOlMaqwPSHTEC3vYwz8jXldd1-4IGK_rUzZz_1bMv4AwEHW8vFqBLTqeK1112aJbZ0fhQfGphnYqY6FFSCL4br5VEQDVXjE3LdnHphZ0vxfgw1P8xRDNTIke2p0DTmfml0P98WKSKKu9xfCG4ltEgB2nGwiJj3mWFcDXtTiKv09UyZWHydkoHDs6wIxR611il9zon_9LnbYoyHJuEqdFLc6Rs-giGxkKDXLtbcUhJfyRa1m0lcq8czIEGWbH_tcKLCyrxjBGPmrBkNp0NgUln0-Ma9FJdbdiHbU2VlJwi3NWzwZS1ydXVci3Yd3NG1EBkRCE29jSHTlvPuRk9hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از حضور رهبر شهید انقلاب در جبهۀ حق علیه باطل در دوران ۸ سال دفاع مقدس</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/463653" target="_blank">📅 16:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463652">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc565ba1d2.mp4?token=Ina6uGWP5_iSwsMtfn7GXqhJygiHE-20jz5hcRRacH6NuM8av7pCVx2kj51cruejEbtK07tFJ5TOTSkuGvxg3yA2YH8ZFCrBJvYe42cWzwJkaB5nmb0mCug-hOklwI3FFBoEyVjsEFWq799v7gCkZsjvEqqpYDg-xkanD8nbyHxb1phu3gCIxtH20_irQEGNeqrJnzeE8rwwwyLE1o2X1sO5Nlv9w6oID9dpjApTqIozaWGcZ28_1Tc2XzvWrhYcduNdqUgcXtDOp56QiPQCcUCae4k9wIPMnHc9gmfw7H6xx70wYOu8xQzsG-BRVWOUzST0T088tb8N6RQL_Pff9Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc565ba1d2.mp4?token=Ina6uGWP5_iSwsMtfn7GXqhJygiHE-20jz5hcRRacH6NuM8av7pCVx2kj51cruejEbtK07tFJ5TOTSkuGvxg3yA2YH8ZFCrBJvYe42cWzwJkaB5nmb0mCug-hOklwI3FFBoEyVjsEFWq799v7gCkZsjvEqqpYDg-xkanD8nbyHxb1phu3gCIxtH20_irQEGNeqrJnzeE8rwwwyLE1o2X1sO5Nlv9w6oID9dpjApTqIozaWGcZ28_1Tc2XzvWrhYcduNdqUgcXtDOp56QiPQCcUCae4k9wIPMnHc9gmfw7H6xx70wYOu8xQzsG-BRVWOUzST0T088tb8N6RQL_Pff9Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند دقیقه‌ با قهرمانان سرآشپز  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/463652" target="_blank">📅 16:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463651">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3d78d3aaa.mp4?token=J-CKByoKk_RXCmiz2BzfR3kUCU0B32M1WSp5REizHW0AJcZYsDK_LB8wpLt8NfU7PEMe1mg7KudDuFQPMi_rYz_VNg-ZokGmT3_GRv3xXmy0l9AB7yIV5gIFJYYBJN--aODiEuyx_LdiLKH9Qbrpz9jjJVTVGooQhXMnj24OqdoZM_NhHpLj4YAvnqOHQhXof5BoKqgj54cvOGMTfnSsjLISjhntOnDXI-k-pB3QnidfIlXJSJC2m8WXKxoBPB1sNdcXNNeErMDVD2V1FbCPxlAq-8xhIxHZ2ozkzni1d-Sk_TinWYhZET_T9tmSCrXB-w7EQhVhDWrPqdb0Ny5MMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3d78d3aaa.mp4?token=J-CKByoKk_RXCmiz2BzfR3kUCU0B32M1WSp5REizHW0AJcZYsDK_LB8wpLt8NfU7PEMe1mg7KudDuFQPMi_rYz_VNg-ZokGmT3_GRv3xXmy0l9AB7yIV5gIFJYYBJN--aODiEuyx_LdiLKH9Qbrpz9jjJVTVGooQhXMnj24OqdoZM_NhHpLj4YAvnqOHQhXof5BoKqgj54cvOGMTfnSsjLISjhntOnDXI-k-pB3QnidfIlXJSJC2m8WXKxoBPB1sNdcXNNeErMDVD2V1FbCPxlAq-8xhIxHZ2ozkzni1d-Sk_TinWYhZET_T9tmSCrXB-w7EQhVhDWrPqdb0Ny5MMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پزشکیان در سفر به نیویورک، در توقفی کوتاه با وزیر کشور الجزایر دیدار کرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/463651" target="_blank">📅 16:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463650">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYvgAPYfSjMEeZOcHt4Snx0Wn2cvmPlhSRchnNS5uGPoNheMFGFafh4xIUl_W5wDG_tJb9lQispOpjBgLO069hYvHoGU1hsOBM0Q8Djx2bfSANwPKwITWPQjhaM-G_Ns0xfLsRnDEz95h9BbUvI8PXQN5_prcd-NueJSSoRY9he1X5eZ-XpNLCrrGQhX9u-oxAbCgfVmHgBwZT3XhlGlQ2dYtBkMX2r9Sf4bYF8Y_i3MMEyzmuWsMOA3yUdDpNghNaZOLDEsTGvUmfu2iTrDTCacpmhU3LXoexivI2__uVHZCh-OuRfkKExGvCd-VqmpCy00Gr_XlQaJV6gWwRFV2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای تهران فعلا پایدار است؛ باران هفتۀ آینده می‌آید
🔹
هواشناسی استان تهران: گرمای هوایی که بر استان حاکم است تا پایان هفته باقی خواهد ماند؛ از هفتۀ آینده با ورود یک سامانۀ جوی شاهد بارش‌هایی خواهیم بود که باعث افت دما در سطح استان نیز می‌شود.
عکس: محمدعلی برنو
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/463650" target="_blank">📅 16:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463649">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b25661b35.mp4?token=HyH5LWjl7xIg2Nk1rOGmG6zHxQgTsS7MU5BIWzkFRfEPxy9GpiJY6-haHuw-UvEZ-NspNniM7zEZASiZPKaapXXvkVSUh5oiXoJElwFowtA4FvTO3oWu2_XfSPBkTJMYbkc4Vjqstx1GFEGQ1MpTJT038exU9bua1NBpzTivgyxr_B9-Hs8CPDZnAH845l1Bvzj0MsEOaCTCw5JpnKZs2M6pszGWQ2FNLxyPpxNWGNjFypjqsJ1QMYolbSHGLgTADEEjPHl-DSCFJuP63OpC61eFqhX9FkmnLlBkvo4CqyISjiPatE7TNMG7CoJsIP89pRSWNafQeloTpcwb7JtyN0_fIO_pruocouO2Q8sLSAd37fkEXM3hVXevddNOpniDtTiL9Ingp7oar8JpXV-AcgTvdsaqfkDWInCdYkcLp70wrDs5lIV5Y3m6kZY1sJK2pdHbVDdZsO46N_TqKqnozFcPPFAII__YJxUBnShSQuHNtGc1uPDNWDeTxRJS-CWJ1eDNu7_j8ulwcfQM6zOma25JrCrNM4SmXILQcgsjS-JBb9WcfGB5450OIaaZMt41TiIZ80kkukZkHxu3OyT2NqPDnXnIBll3Vdhm96Qeq2ZbOz1EBePV9lv5s4Du05WxbS0Al7qzCsaZbLlhWLh7T6dk65grsKC4kLOIROMjutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b25661b35.mp4?token=HyH5LWjl7xIg2Nk1rOGmG6zHxQgTsS7MU5BIWzkFRfEPxy9GpiJY6-haHuw-UvEZ-NspNniM7zEZASiZPKaapXXvkVSUh5oiXoJElwFowtA4FvTO3oWu2_XfSPBkTJMYbkc4Vjqstx1GFEGQ1MpTJT038exU9bua1NBpzTivgyxr_B9-Hs8CPDZnAH845l1Bvzj0MsEOaCTCw5JpnKZs2M6pszGWQ2FNLxyPpxNWGNjFypjqsJ1QMYolbSHGLgTADEEjPHl-DSCFJuP63OpC61eFqhX9FkmnLlBkvo4CqyISjiPatE7TNMG7CoJsIP89pRSWNafQeloTpcwb7JtyN0_fIO_pruocouO2Q8sLSAd37fkEXM3hVXevddNOpniDtTiL9Ingp7oar8JpXV-AcgTvdsaqfkDWInCdYkcLp70wrDs5lIV5Y3m6kZY1sJK2pdHbVDdZsO46N_TqKqnozFcPPFAII__YJxUBnShSQuHNtGc1uPDNWDeTxRJS-CWJ1eDNu7_j8ulwcfQM6zOma25JrCrNM4SmXILQcgsjS-JBb9WcfGB5450OIaaZMt41TiIZ80kkukZkHxu3OyT2NqPDnXnIBll3Vdhm96Qeq2ZbOz1EBePV9lv5s4Du05WxbS0Al7qzCsaZbLlhWLh7T6dk65grsKC4kLOIROMjutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰۰۰ بسته کیف و لوازم‌التحریر در چهارباغ البرز توزیع شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/463649" target="_blank">📅 16:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463648">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhKUYbJviSaFak2vEzYAF33QLEMA-gouZt28zwEy3pw4STCpu5uhaTz0gOD10bqV6Svvoh9XvQCb3MEHfvwGPv43sOUw8lXJY5oqTlJ33fqbtSg0VgnX_kzpqIOML4teeUhKFr0lcl8j06dIOirwQt2uKt6eIMvK_ns7jZm4Co4IAU30eV7v_sXqfRPPKi5Dp5jFQaD83rru2zoLyKgKOIoj8I2alTyKgiZlCtF0ymUTdt6M1WsQgiLfSnhGTKfvUDFjFxMkvEKujsuffwvroUEpSdFUU8FZafJ5wEcus09vhQZ913vg35B0AuR8HgB0Aq8Jkdcwit53hV6oJrHVAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعات کاری جدید فعالیت سامانهٔ چکاوک اعلام شد
🔹
بانک مرکزی: ساعت پایان واگذاری برای چک‌های عادی ۱۰:۳۰ و پایان تعیین وضعیت آن‌ها ۱۳:۳۰ است.
🔹
همچنین برای چک‌های رمزدار و تضمین‌شده، ساعت پایان واگذاری ۱۱:۳۰ و ساعت پایان تعیین وضعیت ۱۲:۳۰ در نظر گرفته شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/463648" target="_blank">📅 16:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463647">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دریای مازندران تعطیل شد
🔹
هواشناسی مازندران: فعالیت‌های دریایی در خزر به‌دلیل وزش بادهای شدید و افزایش ارتفاع امواج، برای امروز تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/463647" target="_blank">📅 16:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463646">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aecabb426.mp4?token=TSQS5eM7q13POttOkl8XP3JeYyrdHCRHJNk34AwYQOVynoqLmj8C8WfXVeDTcFTQM6DtMOwSN5jWPoVhXXCdnsVtYi6qWA0I3RQQkfz4P2n3ZcEjrWNAyC1TTM7rVj6WebZ4B1encn4sfIx4XYYWjYPhDJUKlumnEwflOshU3t-U8ywXHcjq_czkwudfvNGiWJilEKP2KRpFImfpHekxa8U7GLFsH0yvua4e2I3ueE9wcDnOnNq5vRFWiYQKHeq6d5P0kkdXtnnB7W5qLhyz9bHGA5pZ2L6K1G2TcrIp1HBrfU_EthcHuuuZvjr2HZ5De6tRr01wKDCbcqDjX88aJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aecabb426.mp4?token=TSQS5eM7q13POttOkl8XP3JeYyrdHCRHJNk34AwYQOVynoqLmj8C8WfXVeDTcFTQM6DtMOwSN5jWPoVhXXCdnsVtYi6qWA0I3RQQkfz4P2n3ZcEjrWNAyC1TTM7rVj6WebZ4B1encn4sfIx4XYYWjYPhDJUKlumnEwflOshU3t-U8ywXHcjq_czkwudfvNGiWJilEKP2KRpFImfpHekxa8U7GLFsH0yvua4e2I3ueE9wcDnOnNq5vRFWiYQKHeq6d5P0kkdXtnnB7W5qLhyz9bHGA5pZ2L6K1G2TcrIp1HBrfU_EthcHuuuZvjr2HZ5De6tRr01wKDCbcqDjX88aJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: در تریبون سازمان ملل مواضع بر حق ایران را بیان می‌کنیم
🔹
وزیر امور خارجه در بدو ورود به نیویورک در تشریح اهداف سفرش گفت: امسال پس از جنگی که صورت گرفت، طبیعی است که تریبون سازمان ملل، محلی خواهد بود برای اینکه مظلومیت مردم ایران، شهدای ایران، شهدای…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/463646" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463639">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFnfJt31MYwYlpZrimq_nKFDIx6Y_JK4Hsh0UaYZL3y0dTFeLfGVdx6XPkArj5-1dOt6B1J9yxDVCfaOuQQ-yPwf_3qryI7Khl6g4r6k2I3IqTCtqPzBRbG4TwW6RtEy8P_ZbTpsT5IHbMYRcIhRvq79JgoB8BsVni1hrslyz0SCA0GvTNHER9TOb3lpx-o3gczfC4vkv4QpE9aKxSs27hNllvscJoxdXg56dkTJ0rNK_WYmDT_2G9iTDONus1D-ViKtvCe4cQ2GEh8JkyUoDN8Ily4D5_Ov4OYaniwFNPK8cTpct7qvHyZsYYDdpuTrVglHha5N_KeSq8M1vGwSDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fp1K3WUOdyNDoSPXcQtv_UOZTjvQMbzT2SGc7t4Uhjwhaafkg4JBELNTQDM6xDRcbca3uugaWOQfZBIGDzJT7LRqBIYVOz3ey2YaS7jtxk0-pAZqPLG6O8KFfdqFhnG6GQXs2aItf4-51Ta06yDasPlPCPduMyhaPYZx67caP5Z5CK1yO3yOfENuf0SZJg0cHSstZii2GD3_SPCmFo4DJPG48m_RfHeJviDUDIZRorX5Qu7lvA5Z7OWWbefamgiPAMyBu5wvJoNtZxJKa2lZDEsHEw5tGv0H99dJj0JW2kGcUIOEhwL-pIc4RfV7SiHBDQuH-tjpsdO-I2U3oFyDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6PkO54Mc0OCYUiuEQneukO77QbOkd2o9BGWPeoh7eTy9-ypsCvTRLwhXKz8ncrLvq1Pk1UghBK93sQftKnak7dEIVrelvPrLBrmii43e5OEsAlpQeeYbQW579oC5Cv_z72qNnfyh9tl1H7chu61xCrTDWEeSZG3sgcR-lvs9EoeGdo7xrhDc5S1va-wzxQRvDxTecrHNWIntdfq693pQIV1uBt2m63koeiRZgxPC9WuO-lREsR7ZJNN2QV1SeasyDF9ntHIhKbl-YVtUGm1nlXmGGjbY9ux13fq7YGtGsCZVhQC-06v3yEXSaJ5K5Jfr83w3dOi-z3-ieauOG0rmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2CMUgGVEXjyOiyWLtkE7vWDiJUAq0Pm8WpciU6B55Cq-jJuJVRHlwDpim2498zhMUShUgsp584VCpI-Z35jbt5XpkgaJnQmm25V1Kc5l1Os8rsoyevIWH5FrOKqZmRkZgwkvH_c6tq18ZD4zx5oRGCEoHWoe0tXKYk7lW1OFu0Wb9jppYg3FuwoNLosdGssLVtW5YNMBIlndcLs4Sgwhvaehar_2mFF2pyO3nMrvfVmFezljm29ioMLv-_3O64mwSiqe7ZdEabYvAqRtf_cJgP8QzReef-UGzwT49Quz8UokSC8e9Gr7lgdshzlTVYPSdb9skbWhP8hvlIdCdj8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUToucCeQP8S1Nd7xxAtjFIo403GDFxoraf22sQz734OkmzJ-1qLTMnEXN8w5lHH4PlbuXexlFsDHRmJJTu9hKTYEOquYQUjDVgtYsiXZcdS6sttzenQ_A0Nt6bBztkAIJKkLKRDTHhkFdSg3wXbs20OYa-8QD7nBi1vLJ2RIOW-dRZ6QGTcNOAvURjuM7KCCVGwiYfoh-LbOC-zE943MeAulTGCjNgFRP44q2ozUCBe-Hdhb5DA8rG7nEQuq7sagR3C1lySpTVpfGIn_ozj1BgRvovbgYWHeE-OhnA-5zXzKoX_C09RXhTzzxi9iJvzgOUz7vUIexmrzTYo5wqpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BISlwwUnyhiWGVCYVtMZ1Ayf84nzBr2WcgtF7nILQY6HR_KXrk6MtY-FRQVVDore_eqLSPc_y4X0jXJHtaVFDrvwk8_m27LskKfrNCkd640S9vBmFgFFQ4M0BaArr9KpITdy1UIEkyzm2pKU7PK5MeRsv2fL7JInEiC2SzmY6j4YK6r_Kzro6haFCUrqiP2rQZgNNDq-bQNOO4_wdqRftJCrQWBRQAVaqnb5HinoJAgIPR4lw0xNp1xAK_G0bWPrRHgzhMFE7jvZXcyi7yf9vxtNvPfxO9EfJaSFEctu0Nm4Uy__rSwqiwNgaqYw5tv6tUkbgh5DSGmdYpvhpHwJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LDUcofUnj_etv6Hr6Rxw1un94mVGJqNSi2q5Zumr8gy0T0r_KzTEvgldEUR_IPVJ-cnTOxa0MDOE4SRwPoRW0oZYI2eHyBnfb2Y-JtkLuNhl81wDJW0Bp_mr1E9UN1hjxa3XxHlgyQ_GnwZZjsap3RX-OTb7506_qKYfPwb-jCzWhbJUUzxPJdEBSXXhrLCDHHEPO1H3XAKQt3bv6_zp6RPY37IMDmGAJJwtr8DV5UMedT7HgLauWczKo_qpqhhzkgeFTwpS7o4bDeZxG7PdeNYfIUPJ8mtYRXwbOBG83sf-vWZl8YBG2TZjfYx8lodFMgPw24m6ikTYb1Uc2B79ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور دسته‌های عزاداری در حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/463639" target="_blank">📅 15:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463638">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7ce7b7633.mp4?token=fGm98n_XxgucfVoRGiGUagR4cI00aRZIv3YG9snuYNsHE3hlADOEYYDZHXzJbT2yGGM67JDeN6KFbkTWo0jXT9dwyrpV1MsW6TZo_SAuCakJoZaP9FeyClFEpzOBwkoUFsiQATCfP-BSxMCvO-ZJN56mXUKmlNC-U8wOi37QZz3vvq9_08zzjieWsnPon6_nSwbukDtQZ-g2xeMPOgsCDLy5k84hJabpbJYmZfjYhtBBHssZE_vtBwot5zZPP__yb602LAems3v3TzzB-SrUXiSWW3aknoa445t4uGBQDdgxk7MQK0SZxFOzWr8wBONQI57n9IQDYHV8G9RjEQKbXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7ce7b7633.mp4?token=fGm98n_XxgucfVoRGiGUagR4cI00aRZIv3YG9snuYNsHE3hlADOEYYDZHXzJbT2yGGM67JDeN6KFbkTWo0jXT9dwyrpV1MsW6TZo_SAuCakJoZaP9FeyClFEpzOBwkoUFsiQATCfP-BSxMCvO-ZJN56mXUKmlNC-U8wOi37QZz3vvq9_08zzjieWsnPon6_nSwbukDtQZ-g2xeMPOgsCDLy5k84hJabpbJYmZfjYhtBBHssZE_vtBwot5zZPP__yb602LAems3v3TzzB-SrUXiSWW3aknoa445t4uGBQDdgxk7MQK0SZxFOzWr8wBONQI57n9IQDYHV8G9RjEQKbXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکایت ۳ رسانهٔ بزرگ آمریکا از دولت ترامپ برای بازگشت به کاخ‌سفید
🔹
شبکه‌های خبری سی‌ان‌ان، ام‌اس ناو و پولیتیکو برای بازپس‌گیری دسترسی خود به کاخ سفید از دولت ترامپ شکایت و اعلام کردند که «هدف از این اقدام، جلوگیری از دخالت دولت در تصمیم‌گیری درباره محتوای…</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/463638" target="_blank">📅 15:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463637">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6uM2d1IidGm7-JqnkrxqU5TA7tBy6hkIdAlNGrowEPHtceyxXRC_Qgk7WnEYrzVIBt6H0-fNcKU4cvkeGgswaSBIS0BXeV2R-aI_qZC9L7XR549NWg8Wk36vle0yZtIlRxA9JgO4BpCpqfEqKVvH5T-zkwiE53YqZmoCVwgBmGsSEf_wokylJG7iQ50bw4j0AtA38HfTNyInIZAsFsbvdx7pecnO_BJjuMxsFLRa_2FlF3H_9NoSOc_tzzEs2S3z2ELrvoh-7AxS3BmcUcmRju-v2hKoK_ahlW0N5fxWg0XMW3zoG1gX3vZZSF5qhcD-yQpLrjZX5N8tms9ALfsgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور پسر مهدی رحمتی در لیگ یک
🔹
سیدعلی رحمتی، فرزند مهدی رحمتی به تیم هوادار تهران پیوست.
@Sportfars</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/463637" target="_blank">📅 15:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463636">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104b583a2f.mp4?token=Z-kkpvXiL0tvWu2alH-pD0qo8Y48OIBZelXkw2NUqHB94vFQJW-sjbdaXASX0HSZXR642plCxPnXFbUfwSmIx0MM0aF1TMm9X5BTkGfjhgdgEu0FtoS_s1vUhqFjnrSfYhJB0r44HcxovpXFhY5QIPl-H5o_XxEepBoguL5Yr7p6XJUbIUnZ_BXeo_uz4lbG07ulRCWqZnUGAZNLHLSV5l37E3Em2NNHEaKMEfRbS8y_0zCwKtQQqfXlotnDahExVqbsyPasErvDIWg0xPdgz4DpBNIQPOTgkGsiNSKRXcY2IElZgKKxsBJlyfEkCxjLmFL0DUAFPg1wOoXXz-Sb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104b583a2f.mp4?token=Z-kkpvXiL0tvWu2alH-pD0qo8Y48OIBZelXkw2NUqHB94vFQJW-sjbdaXASX0HSZXR642plCxPnXFbUfwSmIx0MM0aF1TMm9X5BTkGfjhgdgEu0FtoS_s1vUhqFjnrSfYhJB0r44HcxovpXFhY5QIPl-H5o_XxEepBoguL5Yr7p6XJUbIUnZ_BXeo_uz4lbG07ulRCWqZnUGAZNLHLSV5l37E3Em2NNHEaKMEfRbS8y_0zCwKtQQqfXlotnDahExVqbsyPasErvDIWg0xPdgz4DpBNIQPOTgkGsiNSKRXcY2IElZgKKxsBJlyfEkCxjLmFL0DUAFPg1wOoXXz-Sb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هادی‌زاده، کارشناس مسائل بین‌الملل: ترامپ به‌دنبال ساخت تصویری ضعیف از ایران است؛ جهان می‌گوید ترامپ شکست خورده اما او می‌خواهد تصویری نشان دهد و بگوید که ایرانِ شکست‌خورده را پای میز مذاکره کشانده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/463636" target="_blank">📅 15:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463635">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb5f07b210.mp4?token=VCQaBwZnsP7Kx-zOaqA7_BKjOaGJmoK5nlv3iQFiOtKHqRq116cRw_2QFDc_KOOzA3tab0jxPZ5Inu_kogxPbet2Xy5tWclx-jPKKNkwyPGVHiUaYwo0Ae-E0Y0XEOSafojFaC25Jlt-3ytOIeu0ms4LMXe4VKOIit13n9RDlXN77bFF6HjbolfcgNPjV2Ylxi0N1YGB7Peeup69tQFNwDi2EezBrkduozl6-zol5UATS1nPW-JDdNxAXQ0KIw8GJtamn3dKKQChJp9NQAqJrhojEf1RDH7f88FaXlBNRSE-WxS4VAoxcB6kOIQT1WQ_fk6UXwKhmxjlUoOePGWnUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb5f07b210.mp4?token=VCQaBwZnsP7Kx-zOaqA7_BKjOaGJmoK5nlv3iQFiOtKHqRq116cRw_2QFDc_KOOzA3tab0jxPZ5Inu_kogxPbet2Xy5tWclx-jPKKNkwyPGVHiUaYwo0Ae-E0Y0XEOSafojFaC25Jlt-3ytOIeu0ms4LMXe4VKOIit13n9RDlXN77bFF6HjbolfcgNPjV2Ylxi0N1YGB7Peeup69tQFNwDi2EezBrkduozl6-zol5UATS1nPW-JDdNxAXQ0KIw8GJtamn3dKKQChJp9NQAqJrhojEf1RDH7f88FaXlBNRSE-WxS4VAoxcB6kOIQT1WQ_fk6UXwKhmxjlUoOePGWnUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: بیش‌از ۱۰۰۰ مدرسهٔ کپری و سنگی بالای ۱۰ دانش‌آموز در کشور جمع‌آوری شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/463635" target="_blank">📅 15:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463634">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWsW_SJfAG28YWQexcLyDlwtZdRLRhR3aI-ttC8t-B5DwCqRavEntcVoZ45CJ2aqyC9hwduIvTlaxbw8aRoCIxCj0pJ3_CrvZrllIXq4Zi4YqtK7kHkHkN2RuCBfaMam1qWWIwHshP9RqunaVfdlTALqRh1cJUiL0iSSELBzi_xPCMff1AG0H517xtUx860xYes4W2lv69WDfod2Bm-WGHZ70JA-XRoM3S6QGc_h7Ti0eTyCNrN4EO2N4f4kV97YhkBCzmYddcOB2FlvXEXskhIYx8AJvQTerVFhh-WtkV3VWXoKMRLiFLSIZG7DhcBrfdvAx0oK3rKTvkA0yc98lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس راهور: تردد خودروهای دارای پلاک مناطق آزاد کیش و قشم تا پایان آذر در سراسر کشور مجاز است
🔹
سردار تیمور حسینی: صاحبان خودروهای دارای پلاک سایر مناطق آزاد برای خروج از محدودهٔ مصوب باید با هماهنگی سازمان‌های مرتبط، مرخصی و پلاک گذر موقت دریافت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/463634" target="_blank">📅 15:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463633">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a49d3d78.mp4?token=rJ46mHgvmR8o0FBkVHTr9woNmtrQdMktUkaaxz6gtISScya3rIRpL7GYj5-GIP5ecXq-5RgiDmpQ5mcMjdOWKMxiQHcil9sHjRBgYMokayH-yFBLiP07lptH52H8Y0ZZyItP0iL8iMpDFSmTJm0XLOoraRnykpbrTFgbjLQUEwbS6jYFQEd3Rc24Mgl-yjHxdkntWtMGkg0D-m1Vr43LnOH3lyOY6_oCK8Det0NeqI7Zt2H1TDVdY6x2hHyYigvvah3xO1fhu__olOQ2j74lVGUs2ogBK4I4Hz_VMAVhtedvAY0IkF6fyTRitmHgeOY3YcXHQE5glu2yo2DLvLfDuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a49d3d78.mp4?token=rJ46mHgvmR8o0FBkVHTr9woNmtrQdMktUkaaxz6gtISScya3rIRpL7GYj5-GIP5ecXq-5RgiDmpQ5mcMjdOWKMxiQHcil9sHjRBgYMokayH-yFBLiP07lptH52H8Y0ZZyItP0iL8iMpDFSmTJm0XLOoraRnykpbrTFgbjLQUEwbS6jYFQEd3Rc24Mgl-yjHxdkntWtMGkg0D-m1Vr43LnOH3lyOY6_oCK8Det0NeqI7Zt2H1TDVdY6x2hHyYigvvah3xO1fhu__olOQ2j74lVGUs2ogBK4I4Hz_VMAVhtedvAY0IkF6fyTRitmHgeOY3YcXHQE5glu2yo2DLvLfDuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر کشور پاکستان در سفر به تهران با وزیر کشور دیدار کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/463633" target="_blank">📅 15:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463632">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMJDb_vn2n3t-oZGD_cAtA561XaGTzrGN58OOgKU5hqEWjD-Gmaw3t6sDscirloorSdZqtQccjlD3kLPXPMEAaBAwghA_PokbRAyCoEcwC7c4Pn0yq4W5ZkqUfl1b2VWIKz6f1izodFeZHLZXDdkpD3mNNFENjaCtE_1LwSYfwg4RUYBifGXuuV39Sgx3ot_A2gqnXJuTy0eJqmM7gfEFdhg1Xy_ikgW21F0CEWw5n5iS5NajaKUVXZ10hhR9bHlgg21ASxyModGJc24v0I4q9d09McnWaLzNK5RmTsEfPFbU4OVXKnLEQX-qp7o_HU0ODdZwdNd90_cNgM5fbPvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
انتظار رئیس‌جمهور از سفر به نیویورک
🔹
پزشکیان: امیدوارم مردم جهان از رفتارهای ظالمانه‌ای که در منطقه صورت می‌گیرد، آگاه شوند و مجمعی که با شعار «اعتماد» برگزار می‌شود، اعتماد را به جهان بازگرداند و برای پایان جنگ و خونریزی تلاش کند.
🔹
مظلومیت کودکان ما در…</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/463632" target="_blank">📅 15:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463631">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smAWikNq0GAwBShG8YnoyAAcWHCoNYswYSzwvsUme7SrIn-OYsh-myLbPpxGGjxQ0nJp6TLIx6EeHsHbSIJr4JP1y2NhjXe0xrbkdGjjqaDrm6GtQ4gT3LT49tgJYECd8Dgb1l1U1dXx4a9mKEN5bB_bgQ0gBVErOdriaNlFyR0iBXRRGufR3Dym-39lZXMCCNSeRZfwNYYO3Z1Tx6CyjfvtnlhBYm93V3zLL0bne9t5mGJEooJ85hUbl46nP4gqp0hPFzWkrPwOn1Y6TKl36LuOvnmtGWjlFCatoXEQV3H-aasWqrEMKncwtogimSbiGqyArGAkrNmxFsg3Zh7vnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تراستی‌ها چگونه کنترل و نظارت می‌شوند؟  @Farsna</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/463631" target="_blank">📅 15:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463630">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2476eebc.mp4?token=LXkoLGlkF7YZXOqQLRkVLXwyE4FvBwl9jIGsGntKvehRVFCGn7YaZXOrs_o6KCXIfCuR-qRyaJpnZXOtBqqA49lAQt424hFfkH9J8IuxQ-xY1wRGwBhFIHgCr_qMVqjlD_yi73w1atuzBoroinSX7DAe9ingWzp5WThtaQreyH5ku-_51MeOkrvLoL8yIKDSX-JeY1JrOhU2AX3-xg-pLJB8TvVd0Fk6D46lIxikgbq7Y_LB9gs8U200P6OglfErr1HieiO_X-vp0Lx3NUveNvW7buVpMWNUQA1u49kX-bSHR1frBQZF_9j4r5G6wx9be5AXz_qr0G8pS-9Cb9iVNi6TWrtMQuTIFt4I8fK73FEN_1-7YjkTF1RwKWfWAVx8APdFLSNjUQfIg1nmZi86tIkwIFCj5QxPoAEZvw9Ywgpts0bysUCZpENT-i-FUcs6qr5jKopLiwEbXKexj26OWzM6_rkCuhkZMM5YdaaX207r30hvU974c91dFyr8YIEZNQLlLQE2wIHti2a1AJEAv0k8XZJY7U4c-AMDDyzF_Cds68dYtwH0oV9KC5TLj-lLvV_2LJLi-wbAhgOnWHKZp-x9l_pyOPQl6oPuwbo8octYaLaDWznfOmfn_T0hWIefrsz13NvB-8e9k1k7Vf-DBCh9BnevjPrtLFbuOa-tyMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2476eebc.mp4?token=LXkoLGlkF7YZXOqQLRkVLXwyE4FvBwl9jIGsGntKvehRVFCGn7YaZXOrs_o6KCXIfCuR-qRyaJpnZXOtBqqA49lAQt424hFfkH9J8IuxQ-xY1wRGwBhFIHgCr_qMVqjlD_yi73w1atuzBoroinSX7DAe9ingWzp5WThtaQreyH5ku-_51MeOkrvLoL8yIKDSX-JeY1JrOhU2AX3-xg-pLJB8TvVd0Fk6D46lIxikgbq7Y_LB9gs8U200P6OglfErr1HieiO_X-vp0Lx3NUveNvW7buVpMWNUQA1u49kX-bSHR1frBQZF_9j4r5G6wx9be5AXz_qr0G8pS-9Cb9iVNi6TWrtMQuTIFt4I8fK73FEN_1-7YjkTF1RwKWfWAVx8APdFLSNjUQfIg1nmZi86tIkwIFCj5QxPoAEZvw9Ywgpts0bysUCZpENT-i-FUcs6qr5jKopLiwEbXKexj26OWzM6_rkCuhkZMM5YdaaX207r30hvU974c91dFyr8YIEZNQLlLQE2wIHti2a1AJEAv0k8XZJY7U4c-AMDDyzF_Cds68dYtwH0oV9KC5TLj-lLvV_2LJLi-wbAhgOnWHKZp-x9l_pyOPQl6oPuwbo8octYaLaDWznfOmfn_T0hWIefrsz13NvB-8e9k1k7Vf-DBCh9BnevjPrtLFbuOa-tyMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۵ شب از حماسهٔ تاریخی ملت ایران می‌گذرد
@Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/463630" target="_blank">📅 15:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463629">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bby_tajgw3ToeF252tqYnV7skcUC4itgLdRNe9xrQvqYzKOLaA6apYzIfXzhHoxa7pZXBw6kT8cB-kM3_nJbb3MAN5m8XY39j2S9q-omQllKAZVWP5NOm6u145f_zahO1l72YrVdijA8JU5jzdQbMxtPKUr71V8oBt3MA-pp6-24pcG7JNAOzr1wQEkwGEUg68zE855bExaKaYHHG8bofCYJbdWGgcxLzhN2sYlyVWyuaoHxNoUY8hXMTNU7rzitUH5CW9p0sJBpqQzXa_iM4Ej6Bd9Q6ld-yy-wiZzjkbj677b5ZS90GzcdR-AV6Kgx6IM8rRIbNR9vpTwwdEyFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: آیت‌الله‌ شبیری‌زنجانی عالمی محقق و ژرف‌نگر بود
🔹
پیام رهبر معظم انقلاب در پی ارتحال حضرت آیت‌الله‌العظمی شبیری‌زنجانی: این عالم بزرگوار همهٔ عمر شریف خود به‌جز چند سال اوّل طفولیّت را در مسیر تعلّم و تعلیم و تحقیق گذراندند و همواره از سوی هم‌ترازانِ…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/463629" target="_blank">📅 15:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463627">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4601dd6ca8.mp4?token=anWhOXxy5GpErwviwb1EUY1YSaSGjMQAlVzD6F5gctt-sKUG4FuLhtEeEBu5oeQdHizU64ls0jqE5eAoyuS9ULpbOKsZmm9PIzKvACJ65aqQAjuG1dw_yQ2HyyvQ52OxbjUrSvWpnQ3quVVZsBez8iCrrGGTTWnsl2CEfYFCcC4YQ4Lb2prQSSPQOXHTbARdUvKK26mnKJYXBGhT38PiOFLX3CnX82svNXttJOX-pdaxoHBe35c4P5nZlQ_ywNHLrjLccCaj57HPeh8tRTvb9-bTYLz65OY7Bcuxpq52NReFrwNJdJeDVwktuBcptPDzsTQWK9okpEZ217mnoanLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4601dd6ca8.mp4?token=anWhOXxy5GpErwviwb1EUY1YSaSGjMQAlVzD6F5gctt-sKUG4FuLhtEeEBu5oeQdHizU64ls0jqE5eAoyuS9ULpbOKsZmm9PIzKvACJ65aqQAjuG1dw_yQ2HyyvQ52OxbjUrSvWpnQ3quVVZsBez8iCrrGGTTWnsl2CEfYFCcC4YQ4Lb2prQSSPQOXHTbARdUvKK26mnKJYXBGhT38PiOFLX3CnX82svNXttJOX-pdaxoHBe35c4P5nZlQ_ywNHLrjLccCaj57HPeh8tRTvb9-bTYLz65OY7Bcuxpq52NReFrwNJdJeDVwktuBcptPDzsTQWK9okpEZ217mnoanLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶۸ دانش‌آموزی که جایشان در آغاز سال تحصیلی خالی است
@Farsna</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/463627" target="_blank">📅 15:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463626">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdsIuMnoP_hcNkX5d6j4yrJpH5KDa1UATFzIP4q-dSIq0YK9MkLFUEB-rT0yldg7kSoSHs52Bf8v1n6LJRlOfmHfify98KKu9b1Nimwu4CSpwmsetqaBcnA91jF6Z8LyIB7KjYs1oJ_-vYMq9flsbVO-G5fQ_28KNvRMfsyrCPLlpqBsvtSDJN8w0_c-LJa1mUqNqQvbzMIKgQw6TWitfNh5O842mCAlxhei3pjBLATpS7Ma35is32zvC02FU162AVALm1OnpWFH7YHz9rMxg0MxtiJR9IFPIgRnBQi0O0UWxmYfUxreihiSn9hrmnTaEQ91d6a2_5Mdjzi8jj4XfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترافیک سنگین در چالوس و هراز
🔹
سازمان حمل‌ونقل جاده‌ای: ترافیک وسایل نقلیه در محدوده پیچ‌های جاجرود در محور قدیم تهران - بومهن و حدفاصل پل فردیس تا پل کلاک در آزادراه قزوین - کرج - تهران سنگین است.
🔹
همچنین ترافیک وسایل نقلیه در محدوده رضی‌آباد در محور شهریار - تهران، محدوده قلعه‌نو در بزرگراه ورامین - تهران و محدوده شهرک صنعتی خاوران در بزرگراه پاکدشت - تهران سنگین است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/463626" target="_blank">📅 15:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463625">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4680134550.mp4?token=ZFzJxrLdG1Bqh4X2VhCc9lA_sZdSDKHDOmFpFMmdAsoDTqGce0nnxqcu0RXsHapxUYotHhYIKOrXiyj5x46KawXCGbEOaucW8hT1JKPp_zxiBS8mBT_oJ7sh9eJL9aPMePpv0i6stACKry2Uch4nYm0P1cFubEWO1iEq8-oXIFvZEANRhSpE4xn5bQjA219WAsZkx70bBmMFBMCCbvqZFviu3N8JN4cDEqF4G_w1wz4FJi9W2InW_1lJU2oxFN1k45VOUYlUudeoFK8g5JgP1GQjYZpWzLEQREPX5wik9gwO6IGbODE_0LTM6siFRQ-XGRw-Vd6QhtfQMGJqkY6I_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4680134550.mp4?token=ZFzJxrLdG1Bqh4X2VhCc9lA_sZdSDKHDOmFpFMmdAsoDTqGce0nnxqcu0RXsHapxUYotHhYIKOrXiyj5x46KawXCGbEOaucW8hT1JKPp_zxiBS8mBT_oJ7sh9eJL9aPMePpv0i6stACKry2Uch4nYm0P1cFubEWO1iEq8-oXIFvZEANRhSpE4xn5bQjA219WAsZkx70bBmMFBMCCbvqZFviu3N8JN4cDEqF4G_w1wz4FJi9W2InW_1lJU2oxFN1k45VOUYlUudeoFK8g5JgP1GQjYZpWzLEQREPX5wik9gwO6IGbODE_0LTM6siFRQ-XGRw-Vd6QhtfQMGJqkY6I_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سی‌ان‌ان: هرمز بحرانی بزرگ‌تر از کرونا است
@Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/463625" target="_blank">📅 15:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463624">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622fb68d3c.mp4?token=YPjR0eaglwwJcsZcPNdnoo_18o0nDVEQNikLZH67SgU8ZU478CfSVkoAXubzCyQUH8VPv5Zra1_VgudQNhkMym1E6ejvlMOEyoGHMvRLvXslX5IcjMLOHLom5CoU2wNuKWsswHjzRnwaOtPFhCYSsWdCCSYEMXot5segJsl9U_wvwoS9kiXxrEXW-QoP2baMuencjB1s7QY-AKanIww3f7c4ZTyxRiVqYP_HNvKWWB3Ugm4RjB3FtlCLxwQtRfy4cH39tDQjz7oigPugkYsENjYIels0WjhlsYLTWu3diLlUwVxfS-zHhHOEKpJS-ZDvPIhqRQgth4A1RizZjn1Fyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622fb68d3c.mp4?token=YPjR0eaglwwJcsZcPNdnoo_18o0nDVEQNikLZH67SgU8ZU478CfSVkoAXubzCyQUH8VPv5Zra1_VgudQNhkMym1E6ejvlMOEyoGHMvRLvXslX5IcjMLOHLom5CoU2wNuKWsswHjzRnwaOtPFhCYSsWdCCSYEMXot5segJsl9U_wvwoS9kiXxrEXW-QoP2baMuencjB1s7QY-AKanIww3f7c4ZTyxRiVqYP_HNvKWWB3Ugm4RjB3FtlCLxwQtRfy4cH39tDQjz7oigPugkYsENjYIels0WjhlsYLTWu3diLlUwVxfS-zHhHOEKpJS-ZDvPIhqRQgth4A1RizZjn1Fyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۸ محصول دانش‌بنیان برتر در نمایشگاه پارک فناوری پردیس رونمایی شدند
@Farsna</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/463624" target="_blank">📅 14:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463623">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">۳ فوتی در برخورد موتورسیکلت با قطار در نهاوند
🔹
اورژانس همدان: در حادثه برخورد قطار به یک موتورسیکلت در محدودۀ شهرستان فیروزان نهاوند یک مرد، یک دختربچه و یک پسربچه جان خود را از دست دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/463623" target="_blank">📅 14:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463622">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27d0edf56.mp4?token=VU8UFsfxXF67n0LA7zmw-UiwdZZsTswMMKSA4e_r1Jg1UAFxjdi45HBGV0IoSQaC5PKpK2pufT7SXeZ4FZBGueTd4P02ILYzLhEk1loUI0QPOhgOdeGGHpiL0wos3WnOSxK-SC9BOQKBv4WixDzCED7cyPVsY12Y0VKKAFxmFY85dovhnppUVAi5W_6rvdzkO95eB6ksIJor5t7pfhQQXCeFbeOD4PEVEsQTxsmFXB2MUxy59biSPN-lmuob55gpUy1KZ5avco2lqMod2F8UDXu87ylqmMa33v22f9D77G9YxD_O-pfImhccwJBiNpd3XVIskzK7HhoYpLiuTxj7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27d0edf56.mp4?token=VU8UFsfxXF67n0LA7zmw-UiwdZZsTswMMKSA4e_r1Jg1UAFxjdi45HBGV0IoSQaC5PKpK2pufT7SXeZ4FZBGueTd4P02ILYzLhEk1loUI0QPOhgOdeGGHpiL0wos3WnOSxK-SC9BOQKBv4WixDzCED7cyPVsY12Y0VKKAFxmFY85dovhnppUVAi5W_6rvdzkO95eB6ksIJor5t7pfhQQXCeFbeOD4PEVEsQTxsmFXB2MUxy59biSPN-lmuob55gpUy1KZ5avco2lqMod2F8UDXu87ylqmMa33v22f9D77G9YxD_O-pfImhccwJBiNpd3XVIskzK7HhoYpLiuTxj7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درد پا به دیسک کمر هم ربط دارد
🔹
توضیحات مهم جراح مغز و اعصاب، درباره ارتباط عصبی برخی بیماری‌ها با بخش‌های مختلف بدن
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/463622" target="_blank">📅 14:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463621">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCY_qKR4kRP1IT3AxVpMsr-abjsnWr5PGx5SAhZrtOrUIoX0qOno5g0mIU9HF8VFqXmSRW33Unfio06Y1ToC3qcL6Zlrp8D1BcCTYYnI4DAZPA_z2SafprF16oRP3_9Cm2ZXQbFyovc46AtO7sfJhirHCnW0pq3O5bOjy4I1ljqFXNIfeVwbaTISUM639ZfGJkRSTB4uTnI5Cv6XAtJZVg3nD1G9I4PX3Wluva7BcHEtSfSGlQC9tKEZIOyzVaHg4Ymp89GJSNlXNqtL3D4dBq-43q-9y_20x_8mPtmUmDH0u6_kLemm1iiG0-ZgxHaDtkem0-D9jZkvkrA_P9Hz2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل ارتش: شخصیت شهید نصیرزاده حاصل پیوند دانش، تجربه و میدان بود
🔹
امیر حاتمی در دیدار با خانواده سرلشکر شهید نصیرزاده: شهید نصیرزاده در مسئولیت‌های مختلف، از فرماندهی نیروی هوایی تا جانشینی ستاد کل و وزارت دفاع، با نگاه راهبردی و شناخت دقیق از تحولات منطقه و محیط پیرامونی کشور، در مسیر تقویت قدرت ملی و ارتقای بازدارندگی جمهوری اسلامی ایران گام برداشت.
🔹
آنچه شهید نصیرزاده را در کنار توانمندی‌های علمی و نظامی برجسته می‌کرد، شخصیت انسانی و اخلاقی ایشان بود؛ فرمانده‌ای شجاع، مؤمن، متواضع و متشرع که مسئولیت را برای خدمت فی سبیل الله می‌خواست.
@Farsna</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/463621" target="_blank">📅 14:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463620">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7H1qebvZcKo2xPfN5jNiSdFm2hnVyEXNE1RpFUi4qoNSO5jx7CfvyQ2-CVe30zJ_AcR35s_gU-TftaXdVLjRF04EH0IxIBiTpkLERdqRwGU2WVvdSYN_wTjJhhJhGG_NT0MVu4vFcQ7uRaf2IoRzSkrIWZFTSqD4vVoOOH33wJTvkIA9R0DFOlKkp90BpXS81vY7hvD22Lpez-I8TKCuY2WmX-mSgCnjPH8B41hH8T41zU2Ld-Q1HkKyx5CSOetVQwwtGj8ZNwE4s-yUw7qytwcjKKNSv9_LGD4MZvA97axjm3t5lWfG07TvESt290RuOFOr7GsA8w3Xmu8Mu6beA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در دیدار با وزیر کشور پاکستان: ایران و پاکستان از قدرت‌های منطقه هستند
🔹
امیدواریم با توسعۀ سرمایه‌گذاری‌های مشترک و تسهیل همکاری‌های اقتصادی، شاهد تعمیق هرچه بیشتر روابط ایران و پاکستان باشیم.
🔹
اقدامات و فشارهای آمریکا، زمینه‌ساز افزایش هم‌گرایی…</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/463620" target="_blank">📅 14:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463619">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wljn7f4wblRSDL9hx0juxQBAWu4_pEYGRikZqkp1bXh57ShSfvjCFsBfDSG6QiXccv6N3dEJcc9ardLTosHi3Pa5UucRAK7akzUZxE1fUzuPQpWJDfUeK-ht4N7jELKoDacRritoavNrpMxe-qySY58knxovoPwI34-s5OYCTZJLZ0_u1rr5V_kA_jX4R8IqOja4fIydqG7sAjmfwYMlC3EcgazdCNwhN5q9hKmvHONhQl4HT_SFDruhLefePuL4ENtZUA9HOl7anRS2fwCgkEEzDqd_uxnvuyExbGWpd_1o7Ye5bMBSPqRRSwhI27ChZBU-WQeXPiEqq4TYa21Vcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروازهای فرودگاه امام به ۱۹ کشور برقرار است
🔹
مدیرعامل فرودگاه امام خمینی(ره) تهران: طی ۲۹ روزِ شهریور امسال، در مجموع ۳۱۰۹ پرواز ورودی و خروجی در فرودگاه انجام و ۴۴۵ هزار و ۱۱۳ مسافر در مسیرهای بین‌المللی جابه‌جا شدند.
🔹
این پروازها به ۱۹ کشور شامل ترکیه، عراق، چین، گرجستان، ارمنستان، امارات، عمان، روسیه، افغانستان، پاکستان، آذربایجان، تاجیکستان، تایلند، ویتنام، ازبکستان، مالزی، تونس، قرقیزستان و ماکائو انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/463619" target="_blank">📅 14:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463618">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d0565582.mp4?token=JzRBuA2GKuH4gXjUltWHoZt-CVT4-Sm1BCqZGwuyD7t9vobIRmaqp9-ODkkKF7uLqYIlG9aGwkGPdudpdVNSCwHoQjGSozXJm-LZQKG26D4Ml8pfK-vWbYYGAZmUOarg3M7DN1KDgXqqJv_XQaqHHfjc1SzTEaWuOOCd99Xv3uUKhhxGHuBpB2P7A_08DFrwGSQzHPb29e2yQYRRB8CCkWiYAPwHx7J2D1r8GlLGioO8978FVyHJvcRncayuOCO-lDylQxZwufU6s80d-E4z4Hl7JMZvVHUR0S7PmDCmSp_e8jUlFu-LP_lwJC6xloZRKQCQ9TfkhtRgEGsDnT90TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d0565582.mp4?token=JzRBuA2GKuH4gXjUltWHoZt-CVT4-Sm1BCqZGwuyD7t9vobIRmaqp9-ODkkKF7uLqYIlG9aGwkGPdudpdVNSCwHoQjGSozXJm-LZQKG26D4Ml8pfK-vWbYYGAZmUOarg3M7DN1KDgXqqJv_XQaqHHfjc1SzTEaWuOOCd99Xv3uUKhhxGHuBpB2P7A_08DFrwGSQzHPb29e2yQYRRB8CCkWiYAPwHx7J2D1r8GlLGioO8978FVyHJvcRncayuOCO-lDylQxZwufU6s80d-E4z4Hl7JMZvVHUR0S7PmDCmSp_e8jUlFu-LP_lwJC6xloZRKQCQ9TfkhtRgEGsDnT90TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سازمانی که صداهای حق و ناحق زیادی را در این روز شنیده است
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/463618" target="_blank">📅 14:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463617">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d64b04866.mp4?token=KgQZyBl70ALpP6EXeJe9koVgRfK12rM-PatZeF8yfTT5TYDvDufTcHiTeJpDr5fZhH54dccAIB3R7g1yLTOdJf7Srm-J4RbjNPXSkyyMhgCe3ZIjYsOKhJH9BBcFnhRUBh6o_qQ2kLNZ6RDzva__qC2vhhKjRyOqIusc6wvlpg8HAQJQRGpbmqFYHCh2z-0ZHkxi0U1DbH0_96y9Kp42xwCH2EE9t8so3XSOfqsLVDk3TYfpui3z6cQ4usdxwSJbI9_cWcFhIGwxaRbaTx8xflnfYOz_7wn9hUhiZsNQBVnoeluMP2p5KOYArZkqqr1MvnBogf3VyDV7pl33sk03Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d64b04866.mp4?token=KgQZyBl70ALpP6EXeJe9koVgRfK12rM-PatZeF8yfTT5TYDvDufTcHiTeJpDr5fZhH54dccAIB3R7g1yLTOdJf7Srm-J4RbjNPXSkyyMhgCe3ZIjYsOKhJH9BBcFnhRUBh6o_qQ2kLNZ6RDzva__qC2vhhKjRyOqIusc6wvlpg8HAQJQRGpbmqFYHCh2z-0ZHkxi0U1DbH0_96y9Kp42xwCH2EE9t8so3XSOfqsLVDk3TYfpui3z6cQ4usdxwSJbI9_cWcFhIGwxaRbaTx8xflnfYOz_7wn9hUhiZsNQBVnoeluMP2p5KOYArZkqqr1MvnBogf3VyDV7pl33sk03Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: اگر آمریکا به کوه کلنگ یا هر مکانی حمله کند، مقابل آن می‌ایستیم
🔹
به سردمداران و هیئت حاکمه آمریکا توصیه می‌کنم مواردی را که قبلاً تجربه کرده و در آن تجربه شکست خورده‌اند، بار دیگر تکرار نکنند؛ چرا که آزموده را آزمودن خطاست.
🔹
ترامپ عادت دارد دائماً تهدید کند و فراموش می‌کند که پیش‌تر نیز تهدیداتی مطرح کرده، اما نتوانسته آن‌ها را عملیاتی کند و اکنون دوباره تهدیدات جدیدی را مطرح می‌کند.
🔹
اگر آمریکا بخواهد به هر نقطه از ایران نه فقط کوه کلنگ و نه فقط مکانی که مورد تهدید قرار داده، حمله کند، ما با آمادگی کامل در مقابل حمله آمریکا می‌ایستیم و تجاربی که آمریکا پیش‌تر از نوع مقابله ما کسب کرده و در واقع مانع رسیدن آمریکا به اهدافش شده، مجدداً برای آمریکا تکرار خواهد شد.
🔹
ما برای هر سناریوی دشمن آمادگی داریم و دشمن در هر عرصه‌ای که بخواهد وارد عمل شود، قطعاً پاسخ دندان‌شکنی به دشمن خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/463617" target="_blank">📅 14:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463616">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYwA2G6VFgUYGEMUC4XSq9ObRiJOMQoqvUIMxYSmH4cb1TY_-xwaGBtVuvplo81HYZ4RtjXRm88HjIQCrBc5UgTq34p8pWARbGQPvvDn2G9lvQaFUUxuxxNilccsk4af1wyzQ3HxcawbPDvf-ns0Wt9idnly2tWNVz3JPxeixdMItJ0pm1gU1bK4qQfp2OrjuFQ6RYp7iFhZG79VUCZFjcfEwJfI3_XxSt9Z-yC-yS8finUtx4USF8HYHchCHKilfAE73cG4BTIZpQ9HGdFiC0UjnpHiWc0RkBNLB0cH74s6-UkV52h7GDw3HQ8yI7E-qPuYUtP11uXMWTkOZPDzRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر ایزدی: توانایی هدف قرار دادن شناورهای عظیم دشمن را داریم
🔹
جانشین فرمانده کل سپاه: پیام ما به کشورهای منطقه این است که باید با یکدیگر امنیت منطقه را برقرار کنیم و آن‌ها مشاهده کردند که پایگاه‌های متعدد دشمن در ۱۲ کشور به نتیجه نرسید.
🔹
امروز رزمندگان اسلام در ایران از وضعیت و قابلیتی برخوردار هستند که می‌توانند با موشک‌های بالستیک، شناورهای عظیم دشمنان را هدف قرار دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/463616" target="_blank">📅 14:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463615">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">احتمال مجازی‌شدن مدارس در برخی مناطق جنوبی کشور
🔹
وزیر آموزش‌وپرورش: در کل کشور مدارس به‌صورت حضوری فعالیت می‌کنند؛ ممکن است در بعضی نقاط، به‌ویژه در حاشیهٔ خلیج فارس، مشکلاتی وجود داشته باشد که در این موارد استانداران تصمیم خواهند گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/463615" target="_blank">📅 13:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463614">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6agn9-B-IZPx3cV5n-J38w8v9NrYKEerhZST9Nbb5KDBkUiFe2lSCS0YoSfEiVAuRpSIrEtGAYN3Bn1kiVYD21Y4NVTbtNq2IAPU-YwjDfTcoex2EmrWz1QrVowe1eK-JbeXOvBlmhs0nlLoXZetLXMBAimg-E7rFjceFolNNUnX0sCLDzJ58kP4AAYMmBqMFks6D1Zs1fxEGoU9TKnCmfwVtXPOw9CfMjZImOT_HqXOdTJ2XO7iwJTEBD8ZEUt7H7dKfrJ6vl4vBq33Gxm9stjTs0t8D1kf_C6ByBp3mmJ2EKPJvNQUM8h2i2Bub3KBgc4PKvQ8OE9qKIDvxbaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان در پلی‌استیشن هم حریف ایران نشد
🔹
در رقابت‌های بازی‌های آسیایی ورزش‌های الکترونیک، ابوالفضل آقایی‌نسب از ایران در رشتۀ eFootball Mobile امجد عثمان از عربستان سعودی را ۳ بر صفر شکست داد.
🔹
حسن پاجانی هم در رشتۀ eFootball PC عبدالعزیز فلاح از عربستان را یک بر صفر برد.
🔹
بازیکنان ایران در بازی دوم مقابل کره‌جنوبی هم یک برد و یک تساوی به‌دست آوردند. در بازی سوم هم ۲ بار قطر را شکست دادند و به مرحلۀ حذفی رفتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/463614" target="_blank">📅 13:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463613">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-r-OsWwSDqryN_0cPik2jfLtYGR8v_lCW2_mnElcymLh_qSH_yU3aRy9nB6fRBSiFV9L5J0Ofyr8A50_mjEOBPyx4c6y-NnSLh1wyAmOZVjr2w6eMnmxMc47HHS2R8wn7vca5Y8UbfDRNJc_Y7FsXSClXqYfAfJPx9Pyno6jgwmTmHbMrtUzlEUk6-Ohm8v38KgYjW6Nwkduq7lZ5rXAt_wG9rCXyxx8LwvuwyfyO4jzcOHCYvFDrLOTWGbtS82gXfTJJm5cPN34kZ4d83qpdQixV8zSW95EMW6pCM2F5J19QB3gGMnMNFuhLOuPkwUY5uxV2TnnEsew9aiwMu3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون تیم رسانه‌ای عازم آمریکا می‌شود.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/463613" target="_blank">📅 12:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463612">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0TB_D0zoig6zkqYQEt9Ed0hb0A8tLLk_edyjUlIhIURl2a44j8X8Ig6YcR9QOk9i6REPF2CyN_XXXfvea8vi-irMSXWtdafrNWjbL7ckcu3DI7N0T_KNPf2otY6hSC5iCeIJK2Wx_Za9HPhLLEdzJdOEHSk88MpmNrXV31NYKXZdWYKWeA6FbvcYQpixn9PZFTHWogInFajkbsHgUYdPm_JG37KsWCwtCIg-orlbn3zilUNvER6YPVqia0NUx3aC29VaOez6x2BcYXKZnPlyDEBF2cjJPypzahR1gKeehflFJ8SC6QGh9I2Mqx0hpB0T0zSfBl-pUShEUC3HDDINA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس صد هزار واحد دیگر هم ریخت
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۱۳ هزار واحدی به ۷ میلیون و ۱۶۷ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/463612" target="_blank">📅 12:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463611">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قالیباف: با موشک‌هایمان بدون محدودیت، به هر هدفی که بخواهیم شلیک‌ می‌کنیم
🔹
امسال اولین سالی است که فرمانده‌مان کنارمان نیست؛ اگر درایت و آینده‌نگری آقای شهید نبود، شاید الان فرهنگ دفاع مقدس اینطور به کمک کشور نمی‌آمد.
🔹
در سال‌هایی دفاع مقدس حتی به ما سیم…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463611" target="_blank">📅 12:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463610">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0LqZCZZDOJiHieZ-CD68YPqd4EsWtkvq4NU9gErzL9WZZK-c1DCkgDnwbXPFdR8YXGwanw0ecIqOSco3D49PRhUHYX2il2VGdzLKcxupm9W9Jn_sX0kGtiaPt9BhXu0QD1uk9-6KUfwN2CyVPPRbhjgMs-XdyJQv5urBjFdTts5-1FpTRwQtyElbSxZIIbTr3FVQ2-YMVr3u6nkporMpJP_LTqxT3c9QCHIjLpVhgmF7Y3T_pDkwt0wm0Mric6A40wtuULk5aLYFW7Pes5EiID0ubXalpPAmKHoL3h5WW03P_Z3y0QXKMSOLs3qjxCk84zWf1Ha58Z6y1xvqYfLWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: با موشک‌هایمان بدون محدودیت، به هر هدفی که بخواهیم شلیک‌ می‌کنیم
🔹
امسال اولین سالی است که فرمانده‌مان کنارمان نیست؛ اگر درایت و آینده‌نگری آقای شهید نبود، شاید الان فرهنگ دفاع مقدس اینطور به کمک کشور نمی‌آمد.
🔹
در سال‌هایی دفاع مقدس حتی به ما سیم خاردار نمی‌فروختند، و آتش توپ‌خانه‌های ما تا ۱۴-۱۵ کیلومتر آن طرف تر نمی‌رفت. درحالی‌که گلوله‌های توپ هم جیره‌بندی بود، اما این فرهنگ باعث شد امروز به جایی برسیم که هر نقطه‌ای را بخواهیم با موشک‌هایمان بدون محدودیت، مورد هدف قرار دهیم.
🔹
امروز در این جنگ ترکیبی، اقتصادی، نظامی و دیپلماسی هرگز تسلیم نمی‌شویم و ‌کشور را تعطیل نمی‌کنیم و با قدرت پاسخ خواهیم داد. همانطور که تاکنون پاسخ دادیم و دشمن را در همۀ عرصه‌ها عاجز کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/463610" target="_blank">📅 12:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463609">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwqBMuBI35QEIoX4_IXRDVEzp_lq1QJTUTkBjwOscF2QD-MYHJ3MYPBHZKuwESVpwVAzL2XHW3v_-sP0YA6bfdx4md5WALIx_7VbNLCBqwWyQVBPpcSBR291bkyGCUV97WLtO6tOWt283nFF9vJMxMpsAzqjIYgu9lLxECCRan3Y4hTsEjZz72VC2CQ8tpdYTQNwqIeHC3AtuWrWy6cRljmz0lVXBY8-69dcBOSBI2o26Gy4DHHVbm9lFvWyAk62zb3DIS9LpSmsDTVudsnT9TRXIDL6KVnkULatnjM8olS0fA0G3_B0376PrQmzV-bcwWfLyyIUU4vBDvKNv3N6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اول تا هشتم مهر نمی‌توان از ۲۰ روز اختیاری ورود رایگان به طرح ترافیک استفاده کرد</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/463609" target="_blank">📅 12:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463608">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5gWUPN-eoA64mFn554W-2U0JBYL9YLkm2YgpZFDnctIKZBX56sDTRTOmWpFsERuWBTamPAvnKIkfmCD_hW3lI5SEd1I1PdMFrllvFtkSn3vxxd6E2PSjeJnmzTONLJckL6SWNqhrF_glEoXymxk85Y7XH1eUhKqIW0UuQQDR_dBkCenOrk9Gz7Avp21d0_LxJ8Or95rni8efLmoTeM5ZeBOrRaEV0JCHRN6eGdS3xBXy3GniNu7Q5hTi8TQTaikp_QMwOjadGYhOFpjUXgbiXifroJXX0b-sThraimv6xkfh5cLHZ64K52d-60cGM4JspYrRIqooiWrDEAj5EE1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۷ درصد مطالبات چای‌کاران پرداخت شد
🔹
رئیس سازمان چای کشور: ۳۰۰ میلیارد تومان دیگر از مطالبات چای‌کاران پرداخت شد؛ با این پرداخت، مجموع مطالبات پرداخت‌شده به ۳ هزار و ۲۸۲ میلیارد تومان رسیده که معادل ۸۷ درصد کل مطالبات چای‌کاران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/463608" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463607">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516e39796d.mp4?token=n8veajQta9Mm-FhOYRNI1WofGaFXhqX-wPAM9Xe5cUcHrw_P5mfJvD9p4A2E7oPgJaSlKbRnZpDQri0UR3AW9Qq6TGs0fcUoB-ZDWJ2xG5RF6Q--6NMCkVjZaz9IO4__6FDanRzxAcbgq4pI6KQUhzSHOUeWYhuXg6d0YD98uxf0TwQ_KiMR_mS2knqAUHV9ud7SdgwpIJp-LQeIaEBXilBM4CX3pQ_DlEzTLfKc1YGJ4oaPcC_8CHmKxi5JSm-kfM3gQr780VkBRCcNbZrpJx9RCHyBZaYhDgy5GDRF83ttD6xvD7YiOpHHYBe7JB1ubWHvd5818a1M-2KJ0WoPhbe4NoYLc-7c5gByQUxSx_FSvzlMb_uNw0-itO0PkcyIniecCoJ_S4h5FcJyEQ-5BafWNanZTzwwYsltLBPTJgqLVa8bHnWkTUpPWW1Uf72otB6JwdfkHzYC20vFJSaUih2Xa9ozObdhu3u4GwMJKKeVyReHuI4A4NY-l8IeEj85nFq5BnzAV-03n2Ax6vFKsErEGhZTeIuLrwQo4_6HLus8gvWhkInIrh_t0M3G5h-Hh-1sD0UllDpRLnZXtsz23NQjpbnpMWOJkjN4EpzW2xfdGx2lUwUGzgYs8TlAXQ30iUhLLrszQezMqBOccTIssLPlcq9I8wr9cr_c4wv-PII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516e39796d.mp4?token=n8veajQta9Mm-FhOYRNI1WofGaFXhqX-wPAM9Xe5cUcHrw_P5mfJvD9p4A2E7oPgJaSlKbRnZpDQri0UR3AW9Qq6TGs0fcUoB-ZDWJ2xG5RF6Q--6NMCkVjZaz9IO4__6FDanRzxAcbgq4pI6KQUhzSHOUeWYhuXg6d0YD98uxf0TwQ_KiMR_mS2knqAUHV9ud7SdgwpIJp-LQeIaEBXilBM4CX3pQ_DlEzTLfKc1YGJ4oaPcC_8CHmKxi5JSm-kfM3gQr780VkBRCcNbZrpJx9RCHyBZaYhDgy5GDRF83ttD6xvD7YiOpHHYBe7JB1ubWHvd5818a1M-2KJ0WoPhbe4NoYLc-7c5gByQUxSx_FSvzlMb_uNw0-itO0PkcyIniecCoJ_S4h5FcJyEQ-5BafWNanZTzwwYsltLBPTJgqLVa8bHnWkTUpPWW1Uf72otB6JwdfkHzYC20vFJSaUih2Xa9ozObdhu3u4GwMJKKeVyReHuI4A4NY-l8IeEj85nFq5BnzAV-03n2Ax6vFKsErEGhZTeIuLrwQo4_6HLus8gvWhkInIrh_t0M3G5h-Hh-1sD0UllDpRLnZXtsz23NQjpbnpMWOJkjN4EpzW2xfdGx2lUwUGzgYs8TlAXQ30iUhLLrszQezMqBOccTIssLPlcq9I8wr9cr_c4wv-PII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانش‌آموزان جانباز مینابی ترس و دلهرهٔ هنگام وقوع این جنایت آمریکایی را روایت می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/463607" target="_blank">📅 12:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463606">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ed9869ef.mp4?token=djC__axzCUWv3vHa0OmypLkWtffpfFSsXzhCgo5ZLKhYjW_m7MyBV_M55OQoTi-fkwjVbfRNG8o-Q4qsB_zOTMJYSFH-4YVzjIqq6-VOUf5CIHW9fxCx7KkDqqmujiDHvf2Q4B1ZddMAuoysqWbOu01iBjv8gQNIQDCjUGtIRHfR70PRYxn6fwi2E5frOX5KgLy4RR8vvWvX1cBEoIGF7dui9HfwM287Wbk8YxSCDsz7B4GsLomqBYeZbiWPR8-DB9LswWJ976urzDYTohMN5zITgIHMWVHN4sWrfA2MIT6OoolYurj4lfJUBL2QS-jd2jPeMLBgRuYYEwOYZPmKPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ed9869ef.mp4?token=djC__axzCUWv3vHa0OmypLkWtffpfFSsXzhCgo5ZLKhYjW_m7MyBV_M55OQoTi-fkwjVbfRNG8o-Q4qsB_zOTMJYSFH-4YVzjIqq6-VOUf5CIHW9fxCx7KkDqqmujiDHvf2Q4B1ZddMAuoysqWbOu01iBjv8gQNIQDCjUGtIRHfR70PRYxn6fwi2E5frOX5KgLy4RR8vvWvX1cBEoIGF7dui9HfwM287Wbk8YxSCDsz7B4GsLomqBYeZbiWPR8-DB9LswWJ976urzDYTohMN5zITgIHMWVHN4sWrfA2MIT6OoolYurj4lfJUBL2QS-jd2jPeMLBgRuYYEwOYZPmKPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: دادستانی سبزوار به پروندهٔ تخریب ساختمان تاریخی وارد شد و ماشین‌آلات تخریب را توقیف کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/463606" target="_blank">📅 12:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463605">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc61292397.mp4?token=m0AZ4SxLZ2lHn5LC5fd1ziO083dhJfZ4PPRsO_d1SaPSEm7QiSxs6dyuDB3LSWG2yM6KmmCXlV8zOJSTTGge4TCLf0N-CLlBqMEtD5GxTFo0iS1ifNH7ny_iMI5Qc5CDk3jwF91UzSHPHmlUmQeOyUgYS-2zlz71QFL3C0cFokF4xexT1XdnnXsBJycwY1dzQdtWP6_U08HqK140SX_MslB-pP7YjP-mBnVGxshIP7Uxr1FwTwOcrqGFFD2UTJCDP7Bw2U4OxvowWdnHjUa6w95U1WJVKJNsxXvQbAR6GiIocWyXCg_HxrjGSb3PbYpH3qlbrO4Rp83OLt0WXH7G-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc61292397.mp4?token=m0AZ4SxLZ2lHn5LC5fd1ziO083dhJfZ4PPRsO_d1SaPSEm7QiSxs6dyuDB3LSWG2yM6KmmCXlV8zOJSTTGge4TCLf0N-CLlBqMEtD5GxTFo0iS1ifNH7ny_iMI5Qc5CDk3jwF91UzSHPHmlUmQeOyUgYS-2zlz71QFL3C0cFokF4xexT1XdnnXsBJycwY1dzQdtWP6_U08HqK140SX_MslB-pP7YjP-mBnVGxshIP7Uxr1FwTwOcrqGFFD2UTJCDP7Bw2U4OxvowWdnHjUa6w95U1WJVKJNsxXvQbAR6GiIocWyXCg_HxrjGSb3PbYpH3qlbrO4Rp83OLt0WXH7G-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: دربارهٔ اختلالات نظام بانکی، سازمان بازرسی بررسی‌ها را انجام داده و بانک‌های ضعیف را شناسایی کرده
🔹
هشدارهای لازم به برخی بانک‌ها اعلام شده و برخی پرونده‌ها هم به بانک مرکزی اعلام شده تا به تخلفات رسیدگی کند. @Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/463605" target="_blank">📅 12:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463604">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ql_GrOcbaR-r0E0v7wPZ6dVDofxjr_SoQlXTdG_KhZ3rzUD76tqC9WVjEJ-JyYNUHSG4YBYlH98X5liVQCoTkSduUo_RYXND0SN0W_5UhxQc0UWdV3h3HeSwn13skNpUxnF0BguSpJSRF-YC7kxBAQorQJ2W6umJnDJMkujXYVXRVrB_h1RFYXZAm9D2ryc3Mrn6d_i2zGUFl3QhaNnRzWjbiEDro7fMUM3bIwtZhvg6uF9ZhygT4iyOeN2ce01i6O_IkNgQ4fXGGOvt06yw2QBzel1bkVJ_tYQa5EhfNJG__hZQpL06PrK404cb7jJu14a6PnSKoTTAbAMhMId-NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«پینوکیو» فرماندۀ جنگ اقتصادی علیه ایران
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا فرماندۀ جنگ اقتصادی علیه ایران است. او در هفته‌های اخیر عملیات روانی را کلید زده و گفته‌هایی نظیر «افزایش صف بنزین در ایران» «رسیدن دلار در ایران به ۳۰۰ هزار تومان» و «تمام شدن نفت…</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/463604" target="_blank">📅 12:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463603">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fc0c690aa.mp4?token=k_CBebfRIlIXE2X0SoRMQG30WbPbXRericMaa5Nl7yVcoaUwel7L_q7pyiCg_AtWzQjU5pNDg7Eqc_r6mBq96haDJHXXYiO6uPEW24zuimm9a3rG9ho_azvsJpY0Y84e4FY-o8uCkAQpU25SGoXHkHeIlGBGv2zfM0isvw-EZHOZ_CxTuhRIhsrXKvq-VZ-pHUDA3klyqRX89b0qfMLRvqzj69y-PPzUwvsq7XZLGKN6hsOVdI98Gf0IrSk3SAB4SLm6T_xgK6g6ET9t6DtMSVL5Mjy5ShlK5he6dbo5JGtAXnNODggfKO2UHHvWI23eiWik-QFqwKLAzMQ-wIkPCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fc0c690aa.mp4?token=k_CBebfRIlIXE2X0SoRMQG30WbPbXRericMaa5Nl7yVcoaUwel7L_q7pyiCg_AtWzQjU5pNDg7Eqc_r6mBq96haDJHXXYiO6uPEW24zuimm9a3rG9ho_azvsJpY0Y84e4FY-o8uCkAQpU25SGoXHkHeIlGBGv2zfM0isvw-EZHOZ_CxTuhRIhsrXKvq-VZ-pHUDA3klyqRX89b0qfMLRvqzj69y-PPzUwvsq7XZLGKN6hsOVdI98Gf0IrSk3SAB4SLm6T_xgK6g6ET9t6DtMSVL5Mjy5ShlK5he6dbo5JGtAXnNODggfKO2UHHvWI23eiWik-QFqwKLAzMQ-wIkPCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا | نعمتی اولین طلای ایران را شکار کرد  کاراته‌کای وزن منفی ۷۵ ایران با شکست حریف ترکمنستانی به مدال طلایی آسیا رسید. @Sportfars</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/463603" target="_blank">📅 12:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463602">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbgafQWxFSOy9r7iFf8pHW9YHnhp47dchiVK1xqyKJjNlujznOq2rM9NXhsRWCHeJVigxEWMtw0Bc1u6azIWwbA4FrPvud3CCRUUHc2aE8AxOK998bdaIb8ZDNmRJwlHBwob18jO4l9Kn7SfcdLFaxCT0QfrQQknkdUoicBEnC4bj9G6R_x1U753c-0exVyl1xgBlZtK_uuliNQcY0icD1N4bVxSKQLMyRQ3s3R9FrnHl5bsNFjM_1PhabSdjIGV36jRGkEH_xEKegQdlvNDmcV0W42fhnNc6I7q-MGALTOolHnVthF81VzR84FvqgrJ3LMXHvuVUIfClpUzf_5bCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان‌باختن ۳ نفر به‌دلیل گازگرفتگی در غار چرام
🔹
اورژانس کهگیلویه‌وبویراحمد: درپی مسمومیت گازی روز گذشته در غاری در ارتفاعات چرام، ۲ نفر مصدوم شده و ۳ نفر جان باختند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/463602" target="_blank">📅 11:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463601">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b9d2454d.mp4?token=dTmTS8OR82wu3-pTHAjg0IgUKSRJ0QdsdP7DDWZiZWUr07XlikW1TQOdnjyy3j77eitkLyJ4aKQ4sjhrYzW5H1YFfvBaur1Y97RSzeaAfx6cojNz7lto5HhwfbXakyR9jQ5IZmBsfZJEZIlgtSQa1cg728TV5mQZbiahkZTLNbGLcNSo8gDTimju8EQVCJ_picEBmJx105zD3bonSQiKDISMS-b27inx5c5o6w1Cx9hFkNaXFQ69IChvu_vidWoUoIG3B3eqAuVynPAz7xVqnK76fRZ4blpGimn0UtTRyqzRkPjJYzSlsi8cGahP3ijErF6N1kPxhGFgoyRyVieMvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b9d2454d.mp4?token=dTmTS8OR82wu3-pTHAjg0IgUKSRJ0QdsdP7DDWZiZWUr07XlikW1TQOdnjyy3j77eitkLyJ4aKQ4sjhrYzW5H1YFfvBaur1Y97RSzeaAfx6cojNz7lto5HhwfbXakyR9jQ5IZmBsfZJEZIlgtSQa1cg728TV5mQZbiahkZTLNbGLcNSo8gDTimju8EQVCJ_picEBmJx105zD3bonSQiKDISMS-b27inx5c5o6w1Cx9hFkNaXFQ69IChvu_vidWoUoIG3B3eqAuVynPAz7xVqnK76fRZ4blpGimn0UtTRyqzRkPjJYzSlsi8cGahP3ijErF6N1kPxhGFgoyRyVieMvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین نقرۀ ناگویای ایران سهم بانوان کاتارو شد
🔹
تیم کاتای بانوان ایران در فینال بازی‌های آسیایی ناگویا با نتیجه ۱-۶ مقابل ویتنام شکست خوردند و به مدال نقره بسنده کردند.  @Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/463601" target="_blank">📅 11:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463600">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e95560c5.mp4?token=MZCWe2UTo6E-zwCedmvrlWXrGPHyXoU8gpvVHK0TrcmQHiMjl5wwWSrSMkcsCiXYQbL-Utc5exoq68V0d-INd2WUoSWJLMIIx9urjojWXBxTVBhpklKdJaqSTuD1t7xmac9UTrQFaJDKG8qTUjomxgoB5lk0y50dd-Dx6ix7IF2EE7jxyHWDkg78gVxgVObrovLb4ErhqE4u8Miwd1RnZ8fyGzUzAabh44p_yS_PAPVSJPdo-G-6nDODlJwatLB5hCj-vOVqvazXkXhaTRJgWmJbzxo8OMAmX3BRTp92uVerzm0PZaEnHsuVVdCV04UG4_fW3udpmf96y0p3wIhAiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e95560c5.mp4?token=MZCWe2UTo6E-zwCedmvrlWXrGPHyXoU8gpvVHK0TrcmQHiMjl5wwWSrSMkcsCiXYQbL-Utc5exoq68V0d-INd2WUoSWJLMIIx9urjojWXBxTVBhpklKdJaqSTuD1t7xmac9UTrQFaJDKG8qTUjomxgoB5lk0y50dd-Dx6ix7IF2EE7jxyHWDkg78gVxgVObrovLb4ErhqE4u8Miwd1RnZ8fyGzUzAabh44p_yS_PAPVSJPdo-G-6nDODlJwatLB5hCj-vOVqvazXkXhaTRJgWmJbzxo8OMAmX3BRTp92uVerzm0PZaEnHsuVVdCV04UG4_fW3udpmf96y0p3wIhAiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: خروج آمریکا از شورای حقوق بشر، یک پردهٔ دیگر از چهرهٔ دروغین حقوق بشری آمریکا برداشت
🔹
خروج آمریکا از این شورا صرفاً یک نمایش سیاسی بوده و ما گریبان آن‌ها را برای پیگیری حقوقی خون شهدای میناب و امام شهیدمان رها نخواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/463600" target="_blank">📅 11:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463599">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d16be13b9.mp4?token=UjSQyIKkn_s6sgGktgXQHU6IWU3Mt4JMjtP_qSSA-4qDYT0NbdGiHWc2fAcV-nGfh1-Up67lIhosdgr-7eWGWChV-k1eyEViZUVwP9kgrdOcpvd37r6TU1xYRYLlTAgelFyQuZNmleesf857Ne2o0nUFESdEBTITN692zG0YgdmaWHYfcZ5nYDOR46kSrd9cRX0yBQaGO3NKyYxWbm5D8CgL5M9ClkCXl8zyWVoYQo8y1L_EiNxTQFNdO-2SqJAkLIUTPChY_qNOOaWj_3JqSgdo3Apb-TKT8XGR2XOsVNpEv2HVzCg4b30x5zpvS3uixTdz6O9YbaeJktvzwcktLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d16be13b9.mp4?token=UjSQyIKkn_s6sgGktgXQHU6IWU3Mt4JMjtP_qSSA-4qDYT0NbdGiHWc2fAcV-nGfh1-Up67lIhosdgr-7eWGWChV-k1eyEViZUVwP9kgrdOcpvd37r6TU1xYRYLlTAgelFyQuZNmleesf857Ne2o0nUFESdEBTITN692zG0YgdmaWHYfcZ5nYDOR46kSrd9cRX0yBQaGO3NKyYxWbm5D8CgL5M9ClkCXl8zyWVoYQo8y1L_EiNxTQFNdO-2SqJAkLIUTPChY_qNOOaWj_3JqSgdo3Apb-TKT8XGR2XOsVNpEv2HVzCg4b30x5zpvS3uixTdz6O9YbaeJktvzwcktLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: ۷ سرشبکهٔ قاچاق سوخت در هرمزگان طی یک عملیات ۲ ساله بازداشت شدند و حساب‌ها، اموال و املاک ۷۵۳ قاچاقچی توقیف شده است.  @Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/463599" target="_blank">📅 11:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463598">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06554c8831.mp4?token=EFJYxBz4Hx4SRQuvOQaxTOPOMRAVkeYuvE7E8ENAc99KqKyJUbVp-IQVdQav6spBoy7WyhW-2yp3Cy4rJ_V9cLhjPMcz1SrnyKMWjTIuh1gEFrI_YEUHkfwcykAuLznEOBsSjqhg2ODnUzdQeCpCIklQUBVouF-Q5xbf4dMA4tdzVaMwvDHNlBUCHOLc2KBpGs--45MrNFHS0h-NBu6d25oeHT6wCt2DfbqMO9Lo_nggU2OYovJrVGbmNr10sWpuxXmuTAHxAixvsP87SxzpkkFlWtUSLhY_A4MZvCZKiFas2VYtM-SGx21eyrju34q8ZJesRB-yPaxUrDp1rllTdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06554c8831.mp4?token=EFJYxBz4Hx4SRQuvOQaxTOPOMRAVkeYuvE7E8ENAc99KqKyJUbVp-IQVdQav6spBoy7WyhW-2yp3Cy4rJ_V9cLhjPMcz1SrnyKMWjTIuh1gEFrI_YEUHkfwcykAuLznEOBsSjqhg2ODnUzdQeCpCIklQUBVouF-Q5xbf4dMA4tdzVaMwvDHNlBUCHOLc2KBpGs--45MrNFHS0h-NBu6d25oeHT6wCt2DfbqMO9Lo_nggU2OYovJrVGbmNr10sWpuxXmuTAHxAixvsP87SxzpkkFlWtUSLhY_A4MZvCZKiFas2VYtM-SGx21eyrju34q8ZJesRB-yPaxUrDp1rllTdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه بقایای موشک آمریکاییِ اصابت‌کرده به مراسم عروسی در هرمزگان را به دوربین‌ها نشان داد  @Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/463598" target="_blank">📅 11:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463597">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad24702360.mp4?token=gaFXZuzRpbaojAFA0T-BDQp1L09ER5OchrPQXwVLKA9QO9X5c_mDhAvmDn8AgSAxcZevVLMk7FJhFc-WtQ-9OmgjuYdyV669aPhDgVKW3mjyoSnTwIAG5_U5eGVZQu-zNasKlQDtjcXKMWlTGtFwCLYhaXidbHMpG-R-CVFZhKweG1mX5Z5mVpyj4IQNAf6GhFeRE0f2LW214pTV6bomwi0z8Wxn4TwZR3PjGxcohnoUWGSTS9hPnPNWGfaxeSXIVJEqmZiusLf17xo-JuncWxhddA_X7RDHKWBAL6a5_9hvuhT5vGR175tiOyrzndqb0ZG5mQkxzhcwX8S8tIbmeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad24702360.mp4?token=gaFXZuzRpbaojAFA0T-BDQp1L09ER5OchrPQXwVLKA9QO9X5c_mDhAvmDn8AgSAxcZevVLMk7FJhFc-WtQ-9OmgjuYdyV669aPhDgVKW3mjyoSnTwIAG5_U5eGVZQu-zNasKlQDtjcXKMWlTGtFwCLYhaXidbHMpG-R-CVFZhKweG1mX5Z5mVpyj4IQNAf6GhFeRE0f2LW214pTV6bomwi0z8Wxn4TwZR3PjGxcohnoUWGSTS9hPnPNWGfaxeSXIVJEqmZiusLf17xo-JuncWxhddA_X7RDHKWBAL6a5_9hvuhT5vGR175tiOyrzndqb0ZG5mQkxzhcwX8S8tIbmeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای پیگیری قضایی حملات دشمن به مردم و زیرساخت‌های هرمزگان ۶۱ پرونده تشکیل شده  @Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/463597" target="_blank">📅 11:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463596">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a3b282b80.mp4?token=crUNr6mk37z_dxZUb4L1XIhpEnzCboTrb2IIsUFXqeDN6MeO8Fae_tlUb9c3kUocMFyANtKog_sNBsHy0z-c8LwuYMbAMbpgBCtw_D1hQgs4uQxcjqzYzvBnuvDINtUiML05iQhwjTLlWQGqZPglVl_SIE_Z3bR3APeoKI8oPeRVeVRCFDM2_vYdEe2WP6MoQ6p_OGdoizMknEyzSuUqRpMFcI0F5lWiWUNuOeLyZlCsdzIQdYOM3SFfyV0vFOyGifgrwq8QPjH1g0FJiZ3o1KqehQH7WZC2a3jQR5UbPX-q2lGjHo_3vxJjLtQjr2Zh9AYYjyEZYwwr3IrWziGn3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a3b282b80.mp4?token=crUNr6mk37z_dxZUb4L1XIhpEnzCboTrb2IIsUFXqeDN6MeO8Fae_tlUb9c3kUocMFyANtKog_sNBsHy0z-c8LwuYMbAMbpgBCtw_D1hQgs4uQxcjqzYzvBnuvDINtUiML05iQhwjTLlWQGqZPglVl_SIE_Z3bR3APeoKI8oPeRVeVRCFDM2_vYdEe2WP6MoQ6p_OGdoizMknEyzSuUqRpMFcI0F5lWiWUNuOeLyZlCsdzIQdYOM3SFfyV0vFOyGifgrwq8QPjH1g0FJiZ3o1KqehQH7WZC2a3jQR5UbPX-q2lGjHo_3vxJjLtQjr2Zh9AYYjyEZYwwr3IrWziGn3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: پرونده‌های حقوقی و کیفری جنایت حمله به مدرسهٔ میناب تشکیل شده
🔹
پیگیری‌های بیشتر قضایی برای این جنایت ادامه خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/463596" target="_blank">📅 11:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463595">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ae445547.mp4?token=js-0Un-MxhqSmJR770Hecfi6BEeOf4X5_EofuciP0mI7kh1FjCLHbTrdrCMk9E89muSlZth-c1dU8tvV5jSaysEa_qpC-2nGqDUg9i-VxYXVdaoZTjXb3-kbgn3keMjGFUbdD8arKsMYHni2_9ThQtIMISEvQ8otHIRdil70dZis9QSm-A-xLtmJ4YzLIpF3sPrHpOfGW4nYz4kEYmPR9VJvb3YRU3JbY_XTm8FAUZaZywZAwi_xg4Orjk_NHE64x1vR0FAn7qrFb__3k2qRTRUnVK1_76tEnXSYk6gTX_zYXopHUQw0I9iikEnXWpO9n8PmS8SUjlB5Ei0DsHynYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ae445547.mp4?token=js-0Un-MxhqSmJR770Hecfi6BEeOf4X5_EofuciP0mI7kh1FjCLHbTrdrCMk9E89muSlZth-c1dU8tvV5jSaysEa_qpC-2nGqDUg9i-VxYXVdaoZTjXb3-kbgn3keMjGFUbdD8arKsMYHni2_9ThQtIMISEvQ8otHIRdil70dZis9QSm-A-xLtmJ4YzLIpF3sPrHpOfGW4nYz4kEYmPR9VJvb3YRU3JbY_XTm8FAUZaZywZAwi_xg4Orjk_NHE64x1vR0FAn7qrFb__3k2qRTRUnVK1_76tEnXSYk6gTX_zYXopHUQw0I9iikEnXWpO9n8PmS8SUjlB5Ei0DsHynYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: بمباران مدرسهٔ میناب، بمباران بنیان‌های اخلاق و انسانیت در جامعه جهانی بود.  @Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/463595" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463594">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70d7c99d8.mp4?token=MkATZh5m6JWqGFxh-hvz8gv7KJZ3ZNxTO6P2KZTUCr7oDYhoBk9o4H5uZfTgzK7MFdM4xC9u0JszDvIsS29azrDh-pjysLnUm0nmQJC6IjRd8MN5sdZZeovIRrz4M1m5VmLH7iwud5ay0Ry2zOcS33D1isM7qK5Iph3mE4i1CPjVYNVzdrB00BfVrBxR4y8yWO-t8mCQYOx8zog9ysFv7jtFR6HcW_kBvErAVX7fvb7U0NeXIskpAP3f1bT0gjOWIt3fapcLNUw4kCKmuoz1IMN3ri_6Ndnk5QvhCT27t6IXK9AVQXwRcpZygnEPpnPaZvoilYTPFiX8lYA1-wY2Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70d7c99d8.mp4?token=MkATZh5m6JWqGFxh-hvz8gv7KJZ3ZNxTO6P2KZTUCr7oDYhoBk9o4H5uZfTgzK7MFdM4xC9u0JszDvIsS29azrDh-pjysLnUm0nmQJC6IjRd8MN5sdZZeovIRrz4M1m5VmLH7iwud5ay0Ry2zOcS33D1isM7qK5Iph3mE4i1CPjVYNVzdrB00BfVrBxR4y8yWO-t8mCQYOx8zog9ysFv7jtFR6HcW_kBvErAVX7fvb7U0NeXIskpAP3f1bT0gjOWIt3fapcLNUw4kCKmuoz1IMN3ri_6Ndnk5QvhCT27t6IXK9AVQXwRcpZygnEPpnPaZvoilYTPFiX8lYA1-wY2Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: با قدرت، مواضع ایران را در مجامع بین‌المللی مطرح خواهیم کرد
🔹
مواردی که در سازمان ملل مطرح خواهیم کرد، بیان مظلومیت ملت ایران، جنایت‌هایی که رخ داده و بی‌اعتمادی‌هایی است که ایجاد شده است.
🔹
ما چندین بار پای میز مذاکره رفتیم و توافق‌هایی را امضا…</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/463594" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463593">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10628ca9be.mp4?token=QslAzHdxK8VBnMRrL10D7U1XOl_YXgOvxepGXXyP_1AilX-4cKqgcD6-Uqw2eYbVlt8GKibbeiws1PBpruWdEptX-jUZpGGGxXyxtEm1IX2GpaWi5QI5o1b-JPd2wzSB05w5ckCqqs_VkYtgkbqD_rIbbVYRXRniqewChvdRhPAG5E0GQeMWw-NeeVDulQ2RktyX0WTkLgSAZ1GXbacEjKkJkUGUEaoje_HlAGXN6oYJLvLMnk6nvoevddD1TXnRtXqGlaal3nqzxA3C86U9955ShondkdsLq82q1CYslMJjzFKMAKnzvXnfDTBO51Mj97oGZEGZL1UyCWwoeKXpMI3If8gSJYtXWPbHrOjZYpdxOYmW36MNvh8sB0eN92nMjHM5XwyF59K5xSNgQs1M5mET6D5c3C29lyo05-_f_oWkGgGq-O3mXhztIvHV1Vnn5gDqzbMNSt7cJ8b2xd8-xJegAWm9uklxa6SZNNiR8JQZJGNgsvVmsysDJDU01EmALzUef9YhJp7pZL48PmIkyPR0d7z3l3kx51Q5HgvRPNPgycNdoqyVjZnKmlrwiokENYIAXMLFpZhs2MIjtct8uiAuEjC4CXlIuGKaGS0uSEOJvHZDwwAoQal5qJvAc3lOBT1R_I-BqKOW6r5SWjt5ybvjorivXm1nA8JQTaAScu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10628ca9be.mp4?token=QslAzHdxK8VBnMRrL10D7U1XOl_YXgOvxepGXXyP_1AilX-4cKqgcD6-Uqw2eYbVlt8GKibbeiws1PBpruWdEptX-jUZpGGGxXyxtEm1IX2GpaWi5QI5o1b-JPd2wzSB05w5ckCqqs_VkYtgkbqD_rIbbVYRXRniqewChvdRhPAG5E0GQeMWw-NeeVDulQ2RktyX0WTkLgSAZ1GXbacEjKkJkUGUEaoje_HlAGXN6oYJLvLMnk6nvoevddD1TXnRtXqGlaal3nqzxA3C86U9955ShondkdsLq82q1CYslMJjzFKMAKnzvXnfDTBO51Mj97oGZEGZL1UyCWwoeKXpMI3If8gSJYtXWPbHrOjZYpdxOYmW36MNvh8sB0eN92nMjHM5XwyF59K5xSNgQs1M5mET6D5c3C29lyo05-_f_oWkGgGq-O3mXhztIvHV1Vnn5gDqzbMNSt7cJ8b2xd8-xJegAWm9uklxa6SZNNiR8JQZJGNgsvVmsysDJDU01EmALzUef9YhJp7pZL48PmIkyPR0d7z3l3kx51Q5HgvRPNPgycNdoqyVjZnKmlrwiokENYIAXMLFpZhs2MIjtct8uiAuEjC4CXlIuGKaGS0uSEOJvHZDwwAoQal5qJvAc3lOBT1R_I-BqKOW6r5SWjt5ybvjorivXm1nA8JQTaAScu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسیابری هم نقره‌ای شد
🔹
علی‌اصغر آسیابری کاراته‌کای منفی ۸۴ کیلوی ایران بازی فینال را ۹ بر یک به حریف اردنی واگذار کرد و نایب‌قهرمان آسیا شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/463593" target="_blank">📅 11:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463592">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7435d7776a.mp4?token=vb-LTy6l4C5evM8ICvZfofOOYiZrp9AiJZG3tzAjaRDseY_XJP2AeOFV_BlWV7rbj4-NOQi9qOsXYXUhE0jprj15bi_M2pEH1ego_pxF9YPUFjdUsczl8-aNPrQuGEBh8qItlzTouQZKEsmHFb5N8SDjCDhfv251rkNZnYe-dYb-fnfXB5TuwGeclY6mHIFLl6r8dYw-sMP0vxdlMeBpqNlePRzhm-oR87dJGgQ6lI0BrhNzEVoxXuS2FMC7KgRTRRU2y7mheyoW2njJUplBnc31ru3fK2dvSazwyGD2Ppu0fnLb7PGHWl7Hb5egLqaFUl_0jWexKC8QYxKorTlnUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7435d7776a.mp4?token=vb-LTy6l4C5evM8ICvZfofOOYiZrp9AiJZG3tzAjaRDseY_XJP2AeOFV_BlWV7rbj4-NOQi9qOsXYXUhE0jprj15bi_M2pEH1ego_pxF9YPUFjdUsczl8-aNPrQuGEBh8qItlzTouQZKEsmHFb5N8SDjCDhfv251rkNZnYe-dYb-fnfXB5TuwGeclY6mHIFLl6r8dYw-sMP0vxdlMeBpqNlePRzhm-oR87dJGgQ6lI0BrhNzEVoxXuS2FMC7KgRTRRU2y7mheyoW2njJUplBnc31ru3fK2dvSazwyGD2Ppu0fnLb7PGHWl7Hb5egLqaFUl_0jWexKC8QYxKorTlnUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا | نعمتی اولین طلای ایران را شکار کرد  کاراته‌کای وزن منفی ۷۵ ایران با شکست حریف ترکمنستانی به مدال طلایی آسیا رسید. @Sportfars</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/463592" target="_blank">📅 11:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463591">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287d502760.mp4?token=oURtQj064kjws9igw7eCfJuadoIXVTW2RVeya8Q8cTJls4_FPkN_7-z-sD5RmMBFCP7F_FZPZggl7G83vjAOiEjBpd0ruBMYTskfKdPuhRh-Td5g6KFwQlK3EIHpurEw6jJWAGDxID4YG3hc39kshRz44xDPZ1gI52zKPzykZWZIRnYMoDQPSG40VfbUUPyArJz2gDOVt-ztrW64d5lihol05CclS2QJLqnKIniA_SG7d9gXOPoGZz-IVNzbd2DosyJJ1CCx3Y0yOri2PBMUXRsm6CcBCPU186-A-9qZYhvvU80Dn44GDyb0vjAZuY8c7YHra_CVLwc8rNQ7lGFygw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287d502760.mp4?token=oURtQj064kjws9igw7eCfJuadoIXVTW2RVeya8Q8cTJls4_FPkN_7-z-sD5RmMBFCP7F_FZPZggl7G83vjAOiEjBpd0ruBMYTskfKdPuhRh-Td5g6KFwQlK3EIHpurEw6jJWAGDxID4YG3hc39kshRz44xDPZ1gI52zKPzykZWZIRnYMoDQPSG40VfbUUPyArJz2gDOVt-ztrW64d5lihol05CclS2QJLqnKIniA_SG7d9gXOPoGZz-IVNzbd2DosyJJ1CCx3Y0yOri2PBMUXRsm6CcBCPU186-A-9qZYhvvU80Dn44GDyb0vjAZuY8c7YHra_CVLwc8rNQ7lGFygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه زنگ مقاومت را در مدرسهٔ شجرهٔ طیبهٔ میناب نواخت  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/463591" target="_blank">📅 11:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463590">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba51ceb74.mp4?token=DmydHQPoRgR3QSFXty3Vqs9xaK9_oXGFKG7km9hTX7ntUNk6rlev_SHRUdKAwc-AOSxp9cvrf6qoNZMhCnZxWX7ZiGiCXogZ53XGpiyD6xSsWW5yxrbhNAWJHwXHCE8FKYYZHIejIJDUs1SYc7DpEi0pD5k2u6PshZMfaIg19yvDCQQDMrVSrUnOcWL4ccDpxah2_UrGb8m70S2KIwJ5yctMlxWFmBEg0j9x1EUEIvySlWY3XzP7jnhUpTUdBRnStmSJKxs59K-0D2mzsTNnqg4mbTvyZwTnh6gh4TEUOLCfGP7LlVmyOl5gBBLIBSN0bqqOB-PPhdFZ8gKWbnMYsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba51ceb74.mp4?token=DmydHQPoRgR3QSFXty3Vqs9xaK9_oXGFKG7km9hTX7ntUNk6rlev_SHRUdKAwc-AOSxp9cvrf6qoNZMhCnZxWX7ZiGiCXogZ53XGpiyD6xSsWW5yxrbhNAWJHwXHCE8FKYYZHIejIJDUs1SYc7DpEi0pD5k2u6PshZMfaIg19yvDCQQDMrVSrUnOcWL4ccDpxah2_UrGb8m70S2KIwJ5yctMlxWFmBEg0j9x1EUEIvySlWY3XzP7jnhUpTUdBRnStmSJKxs59K-0D2mzsTNnqg4mbTvyZwTnh6gh4TEUOLCfGP7LlVmyOl5gBBLIBSN0bqqOB-PPhdFZ8gKWbnMYsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا | نعمتی اولین طلای ایران را شکار کرد
کاراته‌کای وزن منفی ۷۵ ایران با شکست حریف ترکمنستانی به مدال طلایی آسیا رسید.
@Sportfars</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/463590" target="_blank">📅 10:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463589">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575f3e76cf.mp4?token=YQdhTbK6M5Qd7GsFUE7C7nRQuGsd-LqtMPo2hODqeOONINyq4b6GB_Rc8pQKuYYi0z8IkHVgzDnl54IQ4AOM0JnTIwyedaC3vAO4QO7r0pWMEl39xjQMvApzsUIRvPXE9jZkJz8q4f5ELr6YJrJGAV4vDDXU8PVaeHezD1lF1y-KWDsTXaniDQIhrQw65I5r18CqvGeTWQNh3cjc0SLZKGgoyr4KCUUzoHjvgoI_9ynDDJh62gPpTmywNJPVEI4bbeZ3WNWn8JKZRhzEEzT6UbsYa2nESGGKoayH3kzsrnZrdXJ9GUZXIUC5VYpkP3MYUVvdiUOjho_v65hmhrgp1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575f3e76cf.mp4?token=YQdhTbK6M5Qd7GsFUE7C7nRQuGsd-LqtMPo2hODqeOONINyq4b6GB_Rc8pQKuYYi0z8IkHVgzDnl54IQ4AOM0JnTIwyedaC3vAO4QO7r0pWMEl39xjQMvApzsUIRvPXE9jZkJz8q4f5ELr6YJrJGAV4vDDXU8PVaeHezD1lF1y-KWDsTXaniDQIhrQw65I5r18CqvGeTWQNh3cjc0SLZKGgoyr4KCUUzoHjvgoI_9ynDDJh62gPpTmywNJPVEI4bbeZ3WNWn8JKZRhzEEzT6UbsYa2nESGGKoayH3kzsrnZrdXJ9GUZXIUC5VYpkP3MYUVvdiUOjho_v65hmhrgp1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین نقرۀ ناگویای ایران سهم بانوان کاتارو شد
🔹
تیم کاتای بانوان ایران در فینال بازی‌های آسیایی ناگویا با نتیجه ۱-۶ مقابل ویتنام شکست خوردند و به مدال نقره بسنده کردند.
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/463589" target="_blank">📅 10:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463588">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
عربستان از فعال‌شدن هشدار حملات هوایی در منطقهٔ نجران خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/463588" target="_blank">📅 10:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463587">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رهبر انقلاب: آیت‌الله‌ شبیری‌زنجانی عالمی محقق و ژرف‌نگر بود
🔹
پیام رهبر معظم انقلاب در پی ارتحال حضرت آیت‌الله‌العظمی شبیری‌زنجانی: این عالم بزرگوار همهٔ عمر شریف خود به‌جز چند سال اوّل طفولیّت را در مسیر تعلّم و تعلیم و تحقیق گذراندند و همواره از سوی هم‌ترازانِ…</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/463587" target="_blank">📅 10:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463586">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
عربستان از فعال‌شدن هشدار حملات هوایی در منطقهٔ نجران خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/463586" target="_blank">📅 10:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463585">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: هیئت کارشناسی به پروندهٔ مدرسه میناب ورود کرد
🔹
کاظمی: در آغاز سال تحصیلی به‌نیابت از مسئولان قوه‌قضائیه به هرمزگان آمده‌ایم تا یاد و خاطرهٔ دانش‌آموزان، معلمان و والدین شهید مدرسهٔ‌ میناب را گرامی نگه داریم.
🔹
شعبهٔ ۵۵ دادگاه حقوقی تهران…</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/463585" target="_blank">📅 10:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463584">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxl_AELFjwqQkQJQrWyKm-5eQ5Z-QGOQ_Tvu1-G-EJM9C3ztvGSo4hajBsknxlG-YDg5q6wn0Cs38j7THsXILwZXymRxCYSMKxzY8triLebmlJR8dNMYplKzl3ChVKHrlGf2acM2-7tvSA8znInA5nu3zycPlDTo_ea0MWi7mU-P5sj1lpZu2DPTtF0VtBCErGXO8hI7b3FNSSBhagTdRbDQZfKR9CRN5mGrZB8SrpNGXFwI0TJa3EYNSpbxeyoj71U080NFNFxtJT80Ub1WQCMBOPfuQB53D-R_oAN6FLFpEjLgPix-MNi-U4mBm84BVHW1hvVevfLsH-erHZey4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاییز معادلۀ بازار گوشت را تغییر می‌دهد
🔹
«۴ میلیون راس دام سبک فصل پاییز کشتار می‌شود» که عرضه را افزایش خواهد داد. رئیس شورای تامین دام امروز خبر داد.
🔹
این رقم ۱۶۰ هزار تن گوشت معادل مصرف سالانه ۲۷ میلیون نفر می‌شود.
🔹
به گفتۀ پوریان امسال ۱۳۰ هزار تن گوشت گاومیش هم در کشور تولید شده که مصرف ۲۵ میلیون نفر در سال می‌شود.
🔹
در یک‌سال گذشته قیمت گوشت تا ۲ میلیون تومان بالا آمد که تولیدکنندگان علت اصلی را کمبود و گرانی نهاده می‌گفتند که با فشار روی تولید و عرضه قیمت را افزایش می‌داد.
🔹
اکنون قیمت هر کیلو دام زنده گوسفندی به ۶۸۰ هزار تومان کاهش یافته که طبق عرف گوشت خالص باید ۲ برابر یعنی معادل ۱ میلیون و ۳۶۰ هزار تومان دست مردم برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/463584" target="_blank">📅 10:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463583">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPXvBVkjXbZU5vwl1LkklKuldbtXqoUN3hRWB1U95S3mV3L1gWPun4kb35kFZ8KQxU-ImTSAOtb2dXthtvv5i4xX1wdIt91-XuMMmRsPPDTvwWFbfi2x5rFBcV00ZvwyRXNtoV9-XGfYpOVCDjrFAWQUQNgW7JJXvenaAoUF7AEuRDWb3IM2M8YkrvtctiACmlJHYmfXow86h_fMzrFmGLRhPH0epgQxAYd-AtujJe74YwaN-Ty3UrGs7iPqGRQAMHWEZJmZ8NkoA2Hq8xgN1Li7hT7Cq8ncPWdWBmry9eqZz11jsg40x73WeD0c4x2XWdwYnsktBd9TYF-yQalGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نگاهی به زندگی پربار مرحوم آیت‌الله شبیری‌زنجانی  @Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/463583" target="_blank">📅 10:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463582">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سپاه استان هرمزگان: انهدام مهمات عمل‌نکردۀ تجاوز آمریکایی-صهیونی در شهرستان رودان امروز ساعت ۱۱ تا ۱۵ انجام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/463582" target="_blank">📅 09:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463581">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b516cd8c96.mp4?token=h-w_mqf_W40GwNQpH7QMr23DU31APDwnYQZ6RHAeIp8QvXCLDZmKK_hNOJEF0aGPgdjjv2QIv791iviUWRr_bAcNWnJDIvHJJOKyqh2-6H4runTTIAX4cMNkJoX8XcfFIAeGe5JGxEonnZEwV_UQV1QJVwzgyhPxD_3x0ie_cMEjqrrvgwv_2eVDwBCMg0tS_mj471QFN3zWyVmPqtnNPLOGYrP4Y_HdD0Rzuic-tBdCXWyqQgXPwbPaBqtAvH5JCkF68n4pcEc3fd2GJqIewUETj7DlDR679RJcsQKeWQ4aMMLUyEiO0SUPcf65kFL8V13t0o7MjG4gXP9ShP2h9paBiRXbJSGtHrWSFS9rLvwmNtjkCQEuSHxRPIgQqg9r45GLEX-O6wUaFB-4svuvLWMSwH29lXFGAyGgt62tx_geZw1yQBGXIv1K5wy4TX5L1lLTK2pRlNMSBQ9za8zegZZ20jM-D2n0JVuWeepAtYJggehrAVJjtiLB6QWFjpLcDrkRMve0rzRUrKkql7XCZpBdmFC2Thx4nyKHZeeLIA6Y8dXmuAfAlBaIuv0sxnK72Z0p26_m59nO4XLaBwbIVpskV3CRYw7zKlKpa77eoHfmxX1MhKqYYqQ0KsxxO5w_E5_SchSLEAE-h80AQGXC-6U_GnFmpapEX2KQ-nxSyAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b516cd8c96.mp4?token=h-w_mqf_W40GwNQpH7QMr23DU31APDwnYQZ6RHAeIp8QvXCLDZmKK_hNOJEF0aGPgdjjv2QIv791iviUWRr_bAcNWnJDIvHJJOKyqh2-6H4runTTIAX4cMNkJoX8XcfFIAeGe5JGxEonnZEwV_UQV1QJVwzgyhPxD_3x0ie_cMEjqrrvgwv_2eVDwBCMg0tS_mj471QFN3zWyVmPqtnNPLOGYrP4Y_HdD0Rzuic-tBdCXWyqQgXPwbPaBqtAvH5JCkF68n4pcEc3fd2GJqIewUETj7DlDR679RJcsQKeWQ4aMMLUyEiO0SUPcf65kFL8V13t0o7MjG4gXP9ShP2h9paBiRXbJSGtHrWSFS9rLvwmNtjkCQEuSHxRPIgQqg9r45GLEX-O6wUaFB-4svuvLWMSwH29lXFGAyGgt62tx_geZw1yQBGXIv1K5wy4TX5L1lLTK2pRlNMSBQ9za8zegZZ20jM-D2n0JVuWeepAtYJggehrAVJjtiLB6QWFjpLcDrkRMve0rzRUrKkql7XCZpBdmFC2Thx4nyKHZeeLIA6Y8dXmuAfAlBaIuv0sxnK72Z0p26_m59nO4XLaBwbIVpskV3CRYw7zKlKpa77eoHfmxX1MhKqYYqQ0KsxxO5w_E5_SchSLEAE-h80AQGXC-6U_GnFmpapEX2KQ-nxSyAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی مرگبار در دبیرستانی در ترکیه
🔹
یک فرد ناشناس امروز در مقابل یک دبیرستان در منطقه تورگوتلو از توابع استان مانیسا در ترکیه اقدام به تیراندازی کرد که در پی آن یک دانش‌آموز کشته و چند دانش‌آموز زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/463581" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463580">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akZ1806gwauW3WiiJ420cwZqk02hi10an0W328_hG5ERfVnKcq7RpAob5e5HqwLRwmYELbUo4Q5ZTtmBVPUrPdxOoYdCiQuFgsQH9hAoerhOrvqz4HKYgySq4ebjSBGAoX3le54WiXnTYLJf0M7zgGIiC37Gpk2pn1CZ_pj3YZW4nl3awzUybmJ_ALsnMWR4q5zRhSDGBsofZaD_3MwOFKlhmDrqUXDQi4l2MVlgisCvXv3TaDFlNVyP65PHiGU75qv8kYjae3Xcavytcrh53WJEs0xt7NdnQsQadcJq9AJiPt6C5cRzWqb3E4HCRJavjhwfIZJMbe13rBakB_OokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/463580" target="_blank">📅 09:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463579">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcwJBv93sXF6O8PWEVFf-TOibC1icKkGa0pnHE2ZbaE0OiuUi6BIo0oxF_0LkKwYWR1H6NcUOPvwwaFg21s0PCUQT8cB6OFfm53qWz9cKD6jhQ2ECneDMho1Tx8a6UWUJqCJTQXqTqsvrvWVDP3NMIfMYOMBAkCFZhr0GWrfuUE1qVosbzUXFQ8O5M8_sSWMZOpdiu0la6iIkpnOYqQeg9u-RrubR2U4LyQZHzL_--oSAEle72zQov7Zl5LsI42pASd9DGGtCuEvVXd5luP0pANV5ORgH-GazjlZ6u-GDB5oFTVLZTKLOcMZWzvPN7gLV5CPydLp17oUOjrmA1YW2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  هیئت نظارت مجمع تشخیص بخشی از مصوبۀ «مهریه» را مغایر سیاست‌های کلی دانست
🔹
اعضای هیئت عالی نظارت مجمع تشخیص مصلحت نظام، ماده ۱ و تبصره‌های ۳ ، ۴، ۵، ۶، ۷ و ۸ آن و نیز ماده ۶ را مغایر سیاست‌های کلی نظام قانونگذاری و سیاست‌های کلی خانواده دانستند. @Farsna…</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/463579" target="_blank">📅 09:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463577">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d094073aa5.mp4?token=rp7Kk-_u5haZagNjVn-7eHYzR3vPb-aHYGZACLU25aoSJt0ppk3EXhuA_nxQoOHGO9967y3p_CpgZda_R8W6etdg8EiDNK-csTHlp5GTx-VA5t5oWJK7En6ftQ7E08agqeFvsmXEt_jRv1g1pQYCGFY3oBVHHtp6jHhuvetRR1ZtDNkMaFcAoxJYHvjuy2SNfmBq2jozCtlArX9y66-FYw-Za3e0ks7kjHvQs8Ry2FVveu-QRVZMaD2JAVXRM7udjXCEGK4zKa-Hrpx4A9fG4y2ARqxBDARMbQaGDfAh5lnUxlTGOZW6c7DPSbFSMDsWhrjEPenVa1iahQ41wvgcszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d094073aa5.mp4?token=rp7Kk-_u5haZagNjVn-7eHYzR3vPb-aHYGZACLU25aoSJt0ppk3EXhuA_nxQoOHGO9967y3p_CpgZda_R8W6etdg8EiDNK-csTHlp5GTx-VA5t5oWJK7En6ftQ7E08agqeFvsmXEt_jRv1g1pQYCGFY3oBVHHtp6jHhuvetRR1ZtDNkMaFcAoxJYHvjuy2SNfmBq2jozCtlArX9y66-FYw-Za3e0ks7kjHvQs8Ry2FVveu-QRVZMaD2JAVXRM7udjXCEGK4zKa-Hrpx4A9fG4y2ARqxBDARMbQaGDfAh5lnUxlTGOZW6c7DPSbFSMDsWhrjEPenVa1iahQ41wvgcszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ جنگنده‌های سعودی به جنوب غربی یمن
🔹
شبکۀ المسیره گزارش داد که نیروی هوایی رژیم سعودی، حداقل ۳ مرتبه شهر «المخاء» را بمباران کرد که بر اثر آن ۱۴ غیرنظامی شامل زنان و کودکان، شهید و زخمی شدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/463577" target="_blank">📅 09:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463576">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">متهم یک پروندۀ کثیرالشاکی در شیراز دستگیر شد
🔹
دادستان استان فارس: پس از وصول شکایت‌های متعدد از سوی شهروندان علیه فردی که مدیریت یک فروشگاه لوازم خانگی را برعهده داشت، متهم اصلی پرونده بازداشت.
🔹
متهم با تبلیغ و عرضۀ لوازم خانگی و ارائۀ آن به‌صورت اقساطی، از خریداران به‌منظور تضمین پرداخت اقساط، مقادیری طلا امانت دریافت می‌کرد و متعهد بوده پس از پایان پرداخت اقساط، طلا‌های دریافتی را به صاحبان بازگرداند.
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/463576" target="_blank">📅 09:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463575">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44af34dc25.mp4?token=sspiUNJFzgzjTMwKGucvdwU9hajSJpi7nda7MO1VUgZzEtLttZdpP3FXjZrSSsHKgb1R4vlXlItmqec9dTGdPA_O-e4hOTNPLh3RgB04KAYUQTgwPVdhJdlT9hhf9nNNaa9sbXQWqZnx76BsaXnGzGwQxxohgGXXZJOLkNIcHkmq3CvVsVhXTjdub3JdAvCu1BxsJG2C72qJMroldUWMLCfeewcpi39hYsv4Cd87ZM6BvM11gbGgeZBwRsJMUcaB51YyXWnKud8J5gIS6pqFKReY4i8uiQyxpHM1qYMZweRIJkWEPwO5_YSsDKEx4mUj-2l56UV_YWeKL-P2DaJTcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44af34dc25.mp4?token=sspiUNJFzgzjTMwKGucvdwU9hajSJpi7nda7MO1VUgZzEtLttZdpP3FXjZrSSsHKgb1R4vlXlItmqec9dTGdPA_O-e4hOTNPLh3RgB04KAYUQTgwPVdhJdlT9hhf9nNNaa9sbXQWqZnx76BsaXnGzGwQxxohgGXXZJOLkNIcHkmq3CvVsVhXTjdub3JdAvCu1BxsJG2C72qJMroldUWMLCfeewcpi39hYsv4Cd87ZM6BvM11gbGgeZBwRsJMUcaB51YyXWnKud8J5gIS6pqFKReY4i8uiQyxpHM1qYMZweRIJkWEPwO5_YSsDKEx4mUj-2l56UV_YWeKL-P2DaJTcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرتضی نعمتی با یک ۳ امتیازی شیرین راهیِ نیمه‌نهایی کاراتۀ ناگویا شد
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/463575" target="_blank">📅 09:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463574">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8876d0d65.mp4?token=cTLt6aPXw8SxDfHRYFOU6xspWVuJlM_hHe55o39MOZ82CkuWVwJh0yXSxzoIhro2D6S2fZ3qlv6eQyJxez8ETc-dWvRPbENPWW-I0bvkUyvzrs0q9oJLWs-RJjTGAfk2UD9qpx9m8awUc73DdoDDobn3sGqlKW6qOpLMsywKY8bySfjBaQWVMICcJmF0AmRaQIR5W5wZUpRv74kZ5kC2tp_lyNhYlOnkj39E45er1TVfO66pNq72oepioZapwGrE2D8XbRZse_d7tp_O03QpexO2yIjU8Jg2-SxAqR98GmIiUz4IamczBlmIA3MItsg8rm1OyN_TV6Rlj-KI5dxhtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8876d0d65.mp4?token=cTLt6aPXw8SxDfHRYFOU6xspWVuJlM_hHe55o39MOZ82CkuWVwJh0yXSxzoIhro2D6S2fZ3qlv6eQyJxez8ETc-dWvRPbENPWW-I0bvkUyvzrs0q9oJLWs-RJjTGAfk2UD9qpx9m8awUc73DdoDDobn3sGqlKW6qOpLMsywKY8bySfjBaQWVMICcJmF0AmRaQIR5W5wZUpRv74kZ5kC2tp_lyNhYlOnkj39E45er1TVfO66pNq72oepioZapwGrE2D8XbRZse_d7tp_O03QpexO2yIjU8Jg2-SxAqR98GmIiUz4IamczBlmIA3MItsg8rm1OyN_TV6Rlj-KI5dxhtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سپاه: ناو هواپیمابر آمریکا را در فاصله ۵۰۰ کیلومتری هدف قرار دادیم
🔹
سردار محبی: ما امروز مصادیق قدرت را یکی پس از دیگری به نمایش می‌گذاریم. نمونه بارز آن، جلوگیری از عبور و مرور هرگونه شناور بدون هماهنگی و نیز ممانعت از ورود جنگ‌افزارهای دشمن است.…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463574" target="_blank">📅 08:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463573">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee78c3dc3f.mp4?token=nmnJb6OsJ-qbm6m6eEk07xuag088gJfSlsM0EkV5Lstvxn07rMZPxg98Hn0Ppn4t0KyJ8h-sbKjg_JUwSUp5Ukt6fZW_5WTEhcSUcYa8vVzXmLNou9ZGowtKhasJspsbbli-NdtJa0qKqKpTBDpV1Q2ehKxBk6xyEnujEtlZdF938E2pAITVAN-Vx-v4AifJ2YoRocvjRjPIM51fxmautuwR23eVdS7ALa3Jlk4dP6O7vOJ9dGj8rY0iZ8xqJsw4oNlVWAadrykdJXgMjZiFsCWnclrRBnoqklKBxXcAJ_qSFA-QaFK2-GoCBYsyD2E-jO88UQqT04CZUfp_6kV_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee78c3dc3f.mp4?token=nmnJb6OsJ-qbm6m6eEk07xuag088gJfSlsM0EkV5Lstvxn07rMZPxg98Hn0Ppn4t0KyJ8h-sbKjg_JUwSUp5Ukt6fZW_5WTEhcSUcYa8vVzXmLNou9ZGowtKhasJspsbbli-NdtJa0qKqKpTBDpV1Q2ehKxBk6xyEnujEtlZdF938E2pAITVAN-Vx-v4AifJ2YoRocvjRjPIM51fxmautuwR23eVdS7ALa3Jlk4dP6O7vOJ9dGj8rY0iZ8xqJsw4oNlVWAadrykdJXgMjZiFsCWnclrRBnoqklKBxXcAJ_qSFA-QaFK2-GoCBYsyD2E-jO88UQqT04CZUfp_6kV_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی پلیس برای نجات کودک به دل چاه می‌زند
🔹
این روایت یکی از ماموران پلیس است که ۴۰ دقیقه در چاه کنار دختربچه ماند تا نیروهای آتش‌نشانی کودک را بیرون کشیدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/463573" target="_blank">📅 08:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463572">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4a14d887.mp4?token=Ba1Pg6kDKn0WfehRxmg0omTsMRnRLrOcXSeZ9KMIH0Kj0_8ji9koIQZdoAXEtGNQv977pVHWr5A0mpr8H2MRoafbn0orWXpZcicFfKtyS_gRXbC818QU2H9Uz576RNnpmFkHqtNuB2iu9oF1xnAexyY47ryKnT-HzzkH-woVAdH0-Tj-c9wwDfEhV3GIBVnAmRmFJ5phwTyOOgGMg8IZZlE2gwTTGCOj8VwBqojvkV1NjajgJ7PgJJfi4N15NfQxC3dekjF1IsputIvpqQHZ-cvr9yKn1lkeZ4CuZZ5zKk_eR7ddURT_GiAHmqRn2D4gxuc6brEUu5uyh1aYaA7cK3fIQFbnWOwD1DrKPoENdjIccj6CN_HB86y-WqNupGFs6FbaEwwoTHTAoSCqTsR_B3v6aB4DMCdKdqKCyVFe7JmuO8rlk53FL9_RhifTF3K9FWF93Odic_Mh2SNrICwOH_qCEGO32zfBOQXxAxBbsxW2no7Pa_9CKmZz30zTAgqk4iSdAAI1rP4Ycmb2cpWPiu9b8dwXY3lXoeg22SroJPMbJU0Y0I4YT6wCCB7oeL9njPbNuOwZGMed0GUBWE7X9PtGg8Q1BwVew81U446q9PoP92trnO0VgY6DsE00K2uq4dI3Bdpn_VEO9GcFczwwMrOyBZJTmZJ9Ip9JQEJrt_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4a14d887.mp4?token=Ba1Pg6kDKn0WfehRxmg0omTsMRnRLrOcXSeZ9KMIH0Kj0_8ji9koIQZdoAXEtGNQv977pVHWr5A0mpr8H2MRoafbn0orWXpZcicFfKtyS_gRXbC818QU2H9Uz576RNnpmFkHqtNuB2iu9oF1xnAexyY47ryKnT-HzzkH-woVAdH0-Tj-c9wwDfEhV3GIBVnAmRmFJ5phwTyOOgGMg8IZZlE2gwTTGCOj8VwBqojvkV1NjajgJ7PgJJfi4N15NfQxC3dekjF1IsputIvpqQHZ-cvr9yKn1lkeZ4CuZZ5zKk_eR7ddURT_GiAHmqRn2D4gxuc6brEUu5uyh1aYaA7cK3fIQFbnWOwD1DrKPoENdjIccj6CN_HB86y-WqNupGFs6FbaEwwoTHTAoSCqTsR_B3v6aB4DMCdKdqKCyVFe7JmuO8rlk53FL9_RhifTF3K9FWF93Odic_Mh2SNrICwOH_qCEGO32zfBOQXxAxBbsxW2no7Pa_9CKmZz30zTAgqk4iSdAAI1rP4Ycmb2cpWPiu9b8dwXY3lXoeg22SroJPMbJU0Y0I4YT6wCCB7oeL9njPbNuOwZGMed0GUBWE7X9PtGg8Q1BwVew81U446q9PoP92trnO0VgY6DsE00K2uq4dI3Bdpn_VEO9GcFczwwMrOyBZJTmZJ9Ip9JQEJrt_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقدام اطلاعاتی سپاه ایلام علیه شبکه تروریست‌های مسلح
🔹
سازمان اطلاعات سپاه استان ایلام در اقدامات اخیر خود، با شناسایی و برخورد با عناصر مسلح مرتبط با اقدامات تروریستی، بخشی از فعالیت‌های این افراد را تحت رصد و پیگیری قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463572" target="_blank">📅 08:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463571">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28fd05db0.mp4?token=tf8pp-KwmouyWFLXXrRdvIasW2xXzuMmEgvo34uZnUzO_Qz53D5b1hEl7xI3QOkF2IvsP9K3U8vVzxm6VIZ8JIwwk7BCiH_rgJusXS_SwhkjqN9kV1eARvOhnz2WIA08qeIVZr6gqlcWIR0P5f5C6DeYV2yCrmtJwRjX4ZlV6CQPDiPCeKH1YWw413vr9w2CUuw7zOM8XHYBeb-MfF5ieh0mz96K450rywF5Rv56DApc5zVBY45rjFj2PAwJdBPRyZPOFifzX-aCoQW04UcDT10YdTiVF9r-fUzdjPR6Y7jGfHao21K04AmjJoB7BCutLsikmfAkO1ceDdCzDiBgvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28fd05db0.mp4?token=tf8pp-KwmouyWFLXXrRdvIasW2xXzuMmEgvo34uZnUzO_Qz53D5b1hEl7xI3QOkF2IvsP9K3U8vVzxm6VIZ8JIwwk7BCiH_rgJusXS_SwhkjqN9kV1eARvOhnz2WIA08qeIVZr6gqlcWIR0P5f5C6DeYV2yCrmtJwRjX4ZlV6CQPDiPCeKH1YWw413vr9w2CUuw7zOM8XHYBeb-MfF5ieh0mz96K450rywF5Rv56DApc5zVBY45rjFj2PAwJdBPRyZPOFifzX-aCoQW04UcDT10YdTiVF9r-fUzdjPR6Y7jGfHao21K04AmjJoB7BCutLsikmfAkO1ceDdCzDiBgvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشف ۶ تن انواع مواد مخدر در تهران
🔹
رئیس پلیس تهران: در ۶ ماه گذشته ۱۰۹ باند مواد مخدر انهدام و ۱۵۷ قاچاقچی عمده دستگیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463571" target="_blank">📅 08:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463570">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اموال متعلق به جمعی از عناصر ضدانقلاب توقیف شد
🔹
دادستان تهران: با شناسایی حساب‌های بانکی و خودرو‌های متعلق به ۳۹۴ تن از عوامل ضدانقلاب که در جنگ تحمیلی دوم و سوم و اغتشاشات سال گذشته با دشمن متخاصم همکاری کرده و در مقابل ملت ایران قرار گرفتند، بخشی از اموال عناصر معاند توقیف شد.
🔹
تعداد حساب‌هایی متعلق به این افراد ۲۱۹۱ فقره حساب بوده و همچنین تعداد خودرو‌های توقیف شده نیز ۳۷ دستگاه می‌باشد.
🔸
پیش از این با دستور دادستانی تهران ۱۴۳ مورد از اموال و املاک خائنان به وطن که اقدامات تبلیغی یا عملی علیه کشور و به نفع دولت‌های متخاصم داشته‌اند در تهران توقیف شده بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463570" target="_blank">📅 08:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463569">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34c18721c.mp4?token=b-OS4-cJmnoNZXaE15m18aaHSJS37avhifUrKWWhJ-RpBf2TUk-sdQh0QnBN_4LbS9kWMpgIHfcRBgmY8WLoUW8TvwhAqb7vMjyW8cGI81QmBhgv7qcdEURACZRg-Fzs_LWcNhw7zJhbtDkdH_zKAZ_6bw3URqoFkZ3kmlzhJ5Tq0-0iz-JJquB7L3GMOxygYqDtSbSOO2e1ubs5ncR_lLkjP-vg3LQnTJbDGMCvU-OYhDBc6Eb9N8ajN4o7AB5G6ePJ-gc-8Y-ZOTi_nhNjt3Rad6twvoj_Rauu1Q_2ynKAmz7h7U2Tmed4Nq3yWXwYzS_4M8vjOrwu0hSkMBEHDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34c18721c.mp4?token=b-OS4-cJmnoNZXaE15m18aaHSJS37avhifUrKWWhJ-RpBf2TUk-sdQh0QnBN_4LbS9kWMpgIHfcRBgmY8WLoUW8TvwhAqb7vMjyW8cGI81QmBhgv7qcdEURACZRg-Fzs_LWcNhw7zJhbtDkdH_zKAZ_6bw3URqoFkZ3kmlzhJ5Tq0-0iz-JJquB7L3GMOxygYqDtSbSOO2e1ubs5ncR_lLkjP-vg3LQnTJbDGMCvU-OYhDBc6Eb9N8ajN4o7AB5G6ePJ-gc-8Y-ZOTi_nhNjt3Rad6twvoj_Rauu1Q_2ynKAmz7h7U2Tmed4Nq3yWXwYzS_4M8vjOrwu0hSkMBEHDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور به نیویورک سفر کرد
🔹
پزشکیان صبح امروز برای حضور در هشتادویکمین مجمع عمومی سازمان ملل متحد، تهران را به مقصد نیویورک ترک کرد.
🔹
براساس برنامۀ اعلام‌شده، سفر پزشکیان به نیویورک تا شنبه ادامه خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463569" target="_blank">📅 08:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463568">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8da70a10b.mp4?token=EpuhccbyThjiwByupsjUXcZor4484kRWR3O6t_JOIEMv-edfqMzKwggxfsTMJeq6iWmV2qOt1w1s8HgLY9P2pVM1L5OBjre5lj9bhWEWuUZi8bBwtTbMry1PJJznFDZb9L4YfOybbluRLT02yvLjDCwtg4dAB_j9TW8pdJLaI_EjS3EvWeyC8UYew74ds8YbA5qfDde0dZ_BKVLGwvREfOX8jQNSEgvxPGdWeIcjTAyDnfBGwaWNeIMGhm0xf8-xZezR8pgZ3iltnva3hSjwXSwntWK4o5vGz69ZMZi8Xq5CR7Fv9NaVOeQM09ZjC7_Sf0Ds338OZZLGQo8nD3gT-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8da70a10b.mp4?token=EpuhccbyThjiwByupsjUXcZor4484kRWR3O6t_JOIEMv-edfqMzKwggxfsTMJeq6iWmV2qOt1w1s8HgLY9P2pVM1L5OBjre5lj9bhWEWuUZi8bBwtTbMry1PJJznFDZb9L4YfOybbluRLT02yvLjDCwtg4dAB_j9TW8pdJLaI_EjS3EvWeyC8UYew74ds8YbA5qfDde0dZ_BKVLGwvREfOX8jQNSEgvxPGdWeIcjTAyDnfBGwaWNeIMGhm0xf8-xZezR8pgZ3iltnva3hSjwXSwntWK4o5vGz69ZMZi8Xq5CR7Fv9NaVOeQM09ZjC7_Sf0Ds338OZZLGQo8nD3gT-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فست‌فود سرطان‌زاست؟
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/463568" target="_blank">📅 08:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463567">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzWnUZLBUCGSsSSNOal3gkYBBiVv_8F_TRfkkcDlAFsl2TxcbS3pW669KVyadbMwX0HpDrcak6iGean94SpXjl1I1o8XJpo-YGeAznrtcOWEnuSTCiAwVDtMB6PP66qTlfA4Q4cYlOZbtaVjpa-yvT_9k8eW40INhhuOVkvAYjg2nD73HP_SFrfdKm4Y-hTu_d-bTcOkcVtsxVnaeUTWmE2JXKj4OgaXF_vqCF-ZqpJlJ6RI2b7Qin6cyXkh2had9DvUnJgRuI7OIqProT56FFsq3G2Dq5AuP5dKFGCuLFLqPoKqz3UngLPxzi0fk53OhqjL8DeUPGLLp2vLX37sKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: در تریبون سازمان ملل مواضع بر حق ایران را بیان می‌کنیم
🔹
وزیر امور خارجه در بدو ورود به نیویورک در تشریح اهداف سفرش گفت: امسال پس از جنگی که صورت گرفت، طبیعی است که تریبون سازمان ملل، محلی خواهد بود برای اینکه مظلومیت مردم ایران، شهدای ایران، شهدای مدرسه میناب و در راس آنها قائد و رهبر شهیدمان بیان شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463567" target="_blank">📅 08:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463566">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ7hREskYS92n6hH3D3AOYR1arcRwhIaN-iK5-nlzU9Bs1KVXvCVypaeFimVShPU30jS8oZnwmKKGgeqYlhGXZAXxWNXYqSMRDh1aYV9OeUrBdU-RetqjRF5Lpoagl95xmJMUzNXOWDaVPt5kXOdulkRm3A9gl9sm1p8L-5KV-a8vqPj2XQzYrNnjV_0dtXY9fWfYWpHAha4epad1CnQ91lS7hlOm8pjfPNgMyLylfrmR4X__ZTtNFce7TA8VTsg1gA6dfR9RqQCdQ4YBtZLeMwp4v7fy_lLsNjJ1tm4K0UPCI5YHXDfZ5utJ39meyKrxIjeMrH4XtEWNoXdhwbAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور کیف دانش‌آموز شهید مدرسۀ میناب را به نیویورک ببرد
🔹
همزمان با سفر پزشکیان به نیویورک و اخبار منتشرشده دربارۀ این سفر، کارشناسان معتقدند ترامپ برای «فرار از باتلاق» و پایین آوردن قیمت نفت به‌دنبال دیدار با رئیس‌جمهور ایران است و پزشکیان باید در سازمان…</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/463566" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
