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
<img src="https://cdn4.telesco.pe/file/RL43ruEtqcGwsh9m3dN0nKxVwM1sKBucpSi8Q22f3XoVqENTABM93ujHpiFWU3Y6vr62Z81K1W7xbp4HFFsvbdtucW85XOSjCcKx4B6ujTd8EVszlg0Oub2ZuUVyUbnR-csxKH6izTDLeSkNLbUUca1YQo9kkwcJ-vfz2qqrQsNIgUybYkfxDiZ8ZPCp5kohv-C2Bs_QTFsst3LjjJRYKWy70GCjwaugATcb60toIV8SPHacc8K-9LoeTDWJ7P7xQT1XLPeRZ5_xHCKa3zwNpTGPdAa_yMxNGlIjxXKEQGTWXB3wm-TPhny6RFixkc6TpA22x9hFzIfo7UrfECH-pw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 212K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 18:07:48</div>
<hr>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=RvoatEUvhF4BFYQZXcGD6nOP9cgo9fglvwrQEN9bMzwSqyMlL-w26HiL_z5XSd1T2fDKxKbgnDD6j6vArRk_eYNMqKs2zaXY07PsjOlpls4-In4q8HPT0cQ8WGB1jTpXTLoG0jFbBp6ZveQl-WSUItnqT5_eGM4SIrN7CdvIF8Nq9x9YS2pA1o9NHwntJHbNoaxQ6H4BHb-JV2LAfSrO-ChDZIpTSKTCCJnsWc6EpzDEsD6DrBPH0OUfNOOSQ4QaSngLtkiIt5teNtVqCk3hFMHTmYFpTaEgkreEIrbUMgA-xaZTmC0hysjJ4ZIwwU380eSER4RfMbsTGVhL0N5Czg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=RvoatEUvhF4BFYQZXcGD6nOP9cgo9fglvwrQEN9bMzwSqyMlL-w26HiL_z5XSd1T2fDKxKbgnDD6j6vArRk_eYNMqKs2zaXY07PsjOlpls4-In4q8HPT0cQ8WGB1jTpXTLoG0jFbBp6ZveQl-WSUItnqT5_eGM4SIrN7CdvIF8Nq9x9YS2pA1o9NHwntJHbNoaxQ6H4BHb-JV2LAfSrO-ChDZIpTSKTCCJnsWc6EpzDEsD6DrBPH0OUfNOOSQ4QaSngLtkiIt5teNtVqCk3hFMHTmYFpTaEgkreEIrbUMgA-xaZTmC0hysjJ4ZIwwU380eSER4RfMbsTGVhL0N5Czg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx2eRCTIr9uMunLHKizc6XYcVAMMOGe1GHYmgIRaVMmLZg7KPfikcW81nxcTGRtsABOiJ5-h8Bip0BsS693PQvaK1_B1pduEjPu-7MDh3P_1qomfkfkYL8_bzvxOysZqiaffSkoOst5x-zi0LtojWVchjIPLDn3j1iRqocMu9GDjo68JA5nbXN4L89oik1DE07iOI0gYq40W35yWTNazsDX8sdjS6H8r391cVCLSeGsn-DcB_vqbNqKBzjFlBPS8BrgO4UH84T_DYOztpfFTHu2TPp0dC0HjWFd3YCcYs7wmTdYiSuNmgwmBkXlDLpzd4qsDUprvy79LV4IFA4Wqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=mbRhuqC8pwKhdRr-p5VchtPf7ev1RYCfFx0U5O9z8R5bmk3sG4NvdwWdFxorHBWpqoQlfMku-iofdnhzWyc8nUHTHAGnPOER91rkE1BpntFMYLARGQYiRgtZnNAaTD9QvwzkzXEIQQd73kzrR9SQJn3YPE8D-gPeqvye9QCTAF6acpuiNvK2_sPmbIQnzW7hHosZsb38lI33AQWbDtXZCNeKUbLXu4G4uyda_8nU0Q1FNA4IxjxgDYouWHEEd777MH22ld41MGi3TV0h3Su0MdNn8v2AGDK7-uQyu7MyP3yDFW2-BsYx_C3Tmv8bvmgNIWGoIslQR3MAcEN_8FTpdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=mbRhuqC8pwKhdRr-p5VchtPf7ev1RYCfFx0U5O9z8R5bmk3sG4NvdwWdFxorHBWpqoQlfMku-iofdnhzWyc8nUHTHAGnPOER91rkE1BpntFMYLARGQYiRgtZnNAaTD9QvwzkzXEIQQd73kzrR9SQJn3YPE8D-gPeqvye9QCTAF6acpuiNvK2_sPmbIQnzW7hHosZsb38lI33AQWbDtXZCNeKUbLXu4G4uyda_8nU0Q1FNA4IxjxgDYouWHEEd777MH22ld41MGi3TV0h3Su0MdNn8v2AGDK7-uQyu7MyP3yDFW2-BsYx_C3Tmv8bvmgNIWGoIslQR3MAcEN_8FTpdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=NK8MRJbk_AFJJIgDsawp0C6uAfs9Fr4hlagK6bYTNMGeE_kpbK9q1lxeeC1k7Qvji5gZ4jDWSamSmzmZOFCG43hgkkLy739wgFxOqY1dUe4raR1s8cFXQXt-VEQW7k9O4_zUPg-mQpIGI9OQAo1bEKQCI1x10TY9aTrxrWTOAj46OBp5rozCUPrs63SptDF9otnz5Yg0K_EeBCXpTEVzV4Se6fuqDlPJeasm8UtNciYhRRBmpbdliZTJtEkcMl31fqUrsvO4xxg8v9PQ7F9vydaRsuYFW_8djtA4s6Fe1oK5pv1h5OQpZ3wJqkBnwp0YGgMC1UU9BC81AmYiVtuwpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=NK8MRJbk_AFJJIgDsawp0C6uAfs9Fr4hlagK6bYTNMGeE_kpbK9q1lxeeC1k7Qvji5gZ4jDWSamSmzmZOFCG43hgkkLy739wgFxOqY1dUe4raR1s8cFXQXt-VEQW7k9O4_zUPg-mQpIGI9OQAo1bEKQCI1x10TY9aTrxrWTOAj46OBp5rozCUPrs63SptDF9otnz5Yg0K_EeBCXpTEVzV4Se6fuqDlPJeasm8UtNciYhRRBmpbdliZTJtEkcMl31fqUrsvO4xxg8v9PQ7F9vydaRsuYFW_8djtA4s6Fe1oK5pv1h5OQpZ3wJqkBnwp0YGgMC1UU9BC81AmYiVtuwpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=v9GTWsBpyIsFNCMeSuJvDA1cAF-uwnq1UM9VWM5VCsEL24LlZSXjyjZmn55XI9Ms_7-D4ZlPHnGtmHR_L5hZnArGDmcvLuVr__vP8ZJRCO8Nu-LSUYyHI95Ybnv0JWuRW5s28uaWY_uG94fem-pTBZl7U2RXoMQ-KaOp874NYH6BDpHoZHuy1uOu3F3_sy_0mVqVbyPGpfLTY4aEZO6_FnOczirQvAUeuOuBnI1XK5UqEOGEiwes5XQhx8ufUtLNG9HHb7zCyBDdhJ6v8tOcbeIhzFR27LOOLDWRZxfqpKR0UHL8KjAdi6-kMfJBhzP7EH83iW5q6sk8q9-PlB1rpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=v9GTWsBpyIsFNCMeSuJvDA1cAF-uwnq1UM9VWM5VCsEL24LlZSXjyjZmn55XI9Ms_7-D4ZlPHnGtmHR_L5hZnArGDmcvLuVr__vP8ZJRCO8Nu-LSUYyHI95Ybnv0JWuRW5s28uaWY_uG94fem-pTBZl7U2RXoMQ-KaOp874NYH6BDpHoZHuy1uOu3F3_sy_0mVqVbyPGpfLTY4aEZO6_FnOczirQvAUeuOuBnI1XK5UqEOGEiwes5XQhx8ufUtLNG9HHb7zCyBDdhJ6v8tOcbeIhzFR27LOOLDWRZxfqpKR0UHL8KjAdi6-kMfJBhzP7EH83iW5q6sk8q9-PlB1rpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:‏در واکنش به آسیب واردشده به نیروهای ارتش اسرائیل و در پی نقض توافق آتش بس: حدود ۱۰ زیرساخت سازمان تروریستی حزب‌الله در جنوب لبنان هدف حمله قرار گرفت
🔴
در حمله‌ای دیگر برای رفع تهدید: نیروهای لشکر ۹۱ یک کامیون مورد استفاده حزب‌الله برای انتقال تسلیحات را هدف قرار دادند
🔴
در حملات دقیق نیروی هوایی با هدایت لشکر ۹۱، روز گذشته (پنج‌شنبه) حدود ۱۰ زیرساخت متعلق به سازمان تروریستی حزب‌الله در مناطق بنت جبیل، بیت یاحون، کونین و براشیت در جنوب لبنان هدف حمله قرار گرفت. زیرساخت‌های هدف قرارگرفته توسط این سازمان برای پیشبرد طرح‌های تروریستی علیه نیروهای ارتش اسرائیل که در منطقه امنیتی فعالیت می‌کنند، مورد استفاده قرار می‌گرفتند.
🔴
این حملات در واکنش به آسیب واردشده به نیروهای ما در منطقه امنیتی توسط سازمان تروریستی حزب‌الله و در پی نقض مجدد توافق آتش بس انجام شد.
🔴
همچنین بامداد امروز (جمعه)، نیروهای لشکر ۹۱ یک گروه از تروریست‌های وابسته به سازمان تروریستی حزب‌الله را که در نزدیکی منطقه امنیتی در جنوب لبنان، در حال انتقال تسلیحات با استفاده از یک کامیون بودند، شناسایی کردند. بلافاصله پس از شناسایی، نیروی هوایی برای رفع تهدید علیه نیروهای ما، این کامیون را هدف حمله قرار داد.
🔴
در پی این حمله، انفجارهای ثانویه شناسایی شد که نشان‌دهنده وجود تسلیحات در داخل کامیون بود.
🔴
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود و شهروندان اسرائیل ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOffS2N7OHGboVmRoeG6o1qoasmi3LzMueLjNYQ3suTViAC_Nk33fyx5hG60ZlwoErKhiEueQLj3YQUEi-faUkM7KZ3baGxeXxFQ5gDqdyxzVurU0mkIabhqCwIuOfjGw-UYbCxgSwsQs7MPI3-YSvaIYwpUVzl8sxONEf3vYIuaKBDeoeCCmpbc48xa1PPvo0OUXN8EmX8KuBr_26dkZlAHJ7yO36QwUWB7vuD4rHLObmcdDlgqynL_RvzQ25qdl2-3oWXaK9SpksxHP6Y-GWjsLm2EbE48nbzdkLJXsijR82jn-TP49MhCdzztfgRfsybLexZUxSqmiLya-1f0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxDX9_bQ0Mrq1PcEnVb1gfqFuMM0pk8xRQZ_m8iqEkox0Kfd6W2GFbXSYYw77Zv15kEp3mH0LfNzdiSZzl-aGteYKpSB_YKcJLAu_S9EsZt4RARnlqNAT_VRevAbTqQ8liZuMG1QM69sfh9pYucmK9w9XYxazJZY-GnIhJKnJzGfQsLLvxDa8TormROnyAdc3-XtECLWDXVBc-kySY0yS8gmlVZfqB6_3N3X7zXZBHOi00TzgzL9ldhe2V55f3aexO5zMXPxJ6rqoC3r3ZirDUG7ePAw7jcPPKWmDF_syuDwdR1VUzH73cSb1L2nlb62uKGyD1smeKtLsECwOM3yFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=pv2LIAB3DBGOrYN27pnTjXp5USeXCeEmzjYSy4_XPD-CdYcm4hGybNv_3iHnuBllV2IBVLzTgu08VbffL3WgQslcy1CZU-PxdK6HNvF2wKUCZmDfri6iLQBXXjtqNajjgaI3BcVgnQmh9mPH8MzhzOKX08p3kvuClphQxeEeRoP468O6YYlmuRM0xiNlag90EjPZNAlefH80VcJ8hqsf5WxFdYmmeVUTH5zaT7O6nLaeCJ75m3m4-5rXjUWKIehiNMldwdvnZziK8gVtdd2ysfIj17gOPF3aDLCe9NIum_gszUBbIMB8JNQIeMz3-Cfv5SJD35Njt48uYIkrDbD1VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=pv2LIAB3DBGOrYN27pnTjXp5USeXCeEmzjYSy4_XPD-CdYcm4hGybNv_3iHnuBllV2IBVLzTgu08VbffL3WgQslcy1CZU-PxdK6HNvF2wKUCZmDfri6iLQBXXjtqNajjgaI3BcVgnQmh9mPH8MzhzOKX08p3kvuClphQxeEeRoP468O6YYlmuRM0xiNlag90EjPZNAlefH80VcJ8hqsf5WxFdYmmeVUTH5zaT7O6nLaeCJ75m3m4-5rXjUWKIehiNMldwdvnZziK8gVtdd2ysfIj17gOPF3aDLCe9NIum_gszUBbIMB8JNQIeMz3-Cfv5SJD35Njt48uYIkrDbD1VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GBpInqS1q9i8uc086QuO00AWM5JZZeQoSnPe963lM0DhGUsR8ANd1rsNDE_1CSCqEzKrDhDBcBD82sdhsNN8bwNKte9f7ZdPxKJ1Iv9Sirq7zYNuDjwrJObo7Q8MzuGNyHIufkl3vhQ_QDDoyPsoz5yCeo_KbstF2ERSi4bXJnL_VzcLQ2caYh4Wzo9kTAG1RnxB_YOv6c1Dza4NEuYBlJTxQ4-Qy7_QfoMmdmKCiKkD7fP5vp41X4_5N9Ev07JA933WoyVE5dbkeih0Hc0oMyS3CN8KiLkIpWFT7qrJ9aB4E2Srsvj7YGFfogs5WSA14EKI-af1n_8_yC7sXwF6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=CngbaPnhkYunY8Im3WvkTfY5gNbEKrOBDp6ZSgJC11cQZT6YsKTIZ7oFopU0PCkq6bdYy69fDHi1EuzVGWyIYVRIzO6ssDww31_YTWxMwadyM63IhbO96t3rNiT62V4YzOxvL0dE7xmpeSG3dhHTEzanug2r_Co0T5m5MYNGdk86H0U9wnIw_VemFeFtJUpw01onEvNQFRj6ZjCVDAIE3zEtT_Reih8S1sIwuJ44LdX7vAxv8vC2D4u-r17m4GSlDCW9UcDRbKG3TRBzn5oTh7Jk-5F7Q1VIn1b9s05o8qA3vnZ1I7DCVGefySf8RnK7zOcggmdqTNMLgOutU_7JPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=CngbaPnhkYunY8Im3WvkTfY5gNbEKrOBDp6ZSgJC11cQZT6YsKTIZ7oFopU0PCkq6bdYy69fDHi1EuzVGWyIYVRIzO6ssDww31_YTWxMwadyM63IhbO96t3rNiT62V4YzOxvL0dE7xmpeSG3dhHTEzanug2r_Co0T5m5MYNGdk86H0U9wnIw_VemFeFtJUpw01onEvNQFRj6ZjCVDAIE3zEtT_Reih8S1sIwuJ44LdX7vAxv8vC2D4u-r17m4GSlDCW9UcDRbKG3TRBzn5oTh7Jk-5F7Q1VIn1b9s05o8qA3vnZ1I7DCVGefySf8RnK7zOcggmdqTNMLgOutU_7JPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHCBypWj8V1smiqBxI6jysT2rPmZi0ZHfsqPyz6OLnyYWwj6Tl5MLZJNm-uHHTbUX8IwjxVS2_9e7vvw8BXO3s5tGrtjsJKzMAO9yVSsslDKJ0ysKf2THTUV7ak-Gmriq6SayV0wrnLyb0-4fbGZDqXss9P32XUa1kiuccuHi1zu-AhOKLtyI1UWX4mUuWgo-rqheI1h3zc-_I8Z3XlBPvLpxUPepN6cDsrWKqpy7G21MTEgMq-QQs_bav1HDKKBT5v5jv26tGiWu3vj3FM_SQE3qgPhoW_ZGyBMuaSmzdwXCBwAFyqOh8rsXSmu-xWBBUSNBrj7Dgk2FKEWFu-Lag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=XDp3Ij1NbT7gMnodj40QomRka-6UzYZegjAGspitJ-iN9Pb9F_adEKnf1H3jrguNkOB8_TGCDEJiQHy1kgHAK17cqU3rL2jVxyZHL2ckt54QbBs3vjrUjxlqM1tSOf1gJ-YhoaWECZhELUJrOaSs8PpxKu2KUO-gco6NYWIMmAxKp3UeOf_rtXPpqwXCTl9FHYxY_JnUI4kDO_fpaTyqn5wNwyhbWLw06AR-K80fOgg-8EzVGUZGOzq_VJXS4G-H2qBwQttHcNgKykUqnV3E2hLv56h0eiG9H2vRxQXZcFvjItGAawYExUnIrQj9gKASjfZEbgrPwAQ5eKTVzHhi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=XDp3Ij1NbT7gMnodj40QomRka-6UzYZegjAGspitJ-iN9Pb9F_adEKnf1H3jrguNkOB8_TGCDEJiQHy1kgHAK17cqU3rL2jVxyZHL2ckt54QbBs3vjrUjxlqM1tSOf1gJ-YhoaWECZhELUJrOaSs8PpxKu2KUO-gco6NYWIMmAxKp3UeOf_rtXPpqwXCTl9FHYxY_JnUI4kDO_fpaTyqn5wNwyhbWLw06AR-K80fOgg-8EzVGUZGOzq_VJXS4G-H2qBwQttHcNgKykUqnV3E2hLv56h0eiG9H2vRxQXZcFvjItGAawYExUnIrQj9gKASjfZEbgrPwAQ5eKTVzHhi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=PabOKdS_FRrbrp5iOEPr13riN0LqpdrwmtC87WTog1hMDZrDtWNC2Uc1nfZjYZ21jnFc0dw-glZV5xilE7PoqKeFmef_PuEAIEe8MfgnR0BJtKLhrbOzM-EdHqiXKKQjPvEAj-zmNiFpZ_HD1PFCooCd9yTK6Gj7Pr6nxzkRdbVzaWEJHBZ_ku7XMsP_2bl2LaLTRrhpe8qAlYwo_1SsYeSVoDeecMYaf5rURsetRp5xdONKEnjzcYxDSe4wwjFKFDYZH9sfhrKP2_WYp1XqJib03kXxx0gquExEhwPnrMth-ayMFutM-uZ6H6b0rziNMtx0FL4yNdfj8DUXJPAV-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=PabOKdS_FRrbrp5iOEPr13riN0LqpdrwmtC87WTog1hMDZrDtWNC2Uc1nfZjYZ21jnFc0dw-glZV5xilE7PoqKeFmef_PuEAIEe8MfgnR0BJtKLhrbOzM-EdHqiXKKQjPvEAj-zmNiFpZ_HD1PFCooCd9yTK6Gj7Pr6nxzkRdbVzaWEJHBZ_ku7XMsP_2bl2LaLTRrhpe8qAlYwo_1SsYeSVoDeecMYaf5rURsetRp5xdONKEnjzcYxDSe4wwjFKFDYZH9sfhrKP2_WYp1XqJib03kXxx0gquExEhwPnrMth-ayMFutM-uZ6H6b0rziNMtx0FL4yNdfj8DUXJPAV-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vngU-gluAq2W7NrN-XrlXjiU-py6pVm8p2c3OM87UcorsBppSzzd2Bjh4IuEINnOxslNxipm7Hz7Toj-ubB7FodO2iQqg__75eoQxnKI4C8o9PALuY6wByL6jEqJT31n9MkvHUkkpODg7YUif645cp1zfT6XdodH5i_N1DVMbXA6lXbjgCo9-FoNQ3wHK5zSpO_1L0BlH9Qlu5dzdm0UibkxvIoQw8n5RKKvadCFywvT-ayW-9LUccOiJ13ZhSUPB3dkVZavJDp1u8GZ4OVN3Nq-zVnkW_WQ2-9GHiW1Sk7vIyM4d8q-UHOJZbq6NezfcxVFDRqzP5Niqnm_ARJ5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkW608S4bQ927Sx8P9ZG-VBQ8gLIRWq6mtJiF-qgIp36m6z5abIC-0V5XQBqZeJh2H_BKyBEGMP8-VnuaYWBPGa92faMHtJ2X4UcHv9VC0GeYymbHwoA-GHza2_MahDGSDtmaClsuZqsxb0KIvm8ZQD4Gv4m8PewKRILh1iex5qjYvOvhn9keVzK9Tv5EBj0LHn1lGPLQJtVnoBwdYspEkpiBEnJABPbZ9bN0LtNrsJnyC-xsSRWqhnMOFrgOPywKY4GEJaMdQIn8PjXYkv4i0PmBEZ5XAMzELA4J-7XkcAYAkb6bSvr5eJn8_MVC9xWt7ZWZLe-uYPbnkg6m33_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE9hlzuE6wHxUBLtmlUUvV6NbH-y91Gh4DyiKbA-bCYPyhaIWid_xqSYSIAPHFq0AkAxSZrfrmybelu_zSl0BHGW19P_QIardt4J6kCmOCtaB4GJ3Pxrv8Z3Al73QvpJ2VSZfAtweHZeKtR7tgagRyPZaRS8lZFBARsWedxEyGBPFgtCol7mbV_rx9zq1g2E-mhAoZRqhY6I21lAGl96Nxy-U66ySmFgbWJJtBiMcEgs7xE1FwoCGg4yeClFX8qjGezGXDcCer5C_00s1XIcYa3hE36DYsXftMn0Gw0i2_6-vVnQ7VQ2Ezvomc0eW8jZQNan6tZ4ib0Kx2uui65c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=Y-w0-qMmE4R-bjE1WiZl6sQBBIJsxCU8SXx2hSpAoqCn4UWMlbtFeh6FqHlmFxKNPzEtAXC9QJq4fvfW51CMAo7B4KL-ElFTBAkKCPte49vMOapz_estr5akJVmi_tHFpghSXyZuYsD-ZsNKryU0-1S2TpIGBLxf02CyKlJfTGk-cmraq-YB3tFFFN3l-GQgKZyYQnGp8qhMnd9wAXEeRiI0772nOLsAnkOtQvgu13JWFa-wQYiTQrKAhri98angrgg65Pe4dcdAvkX_pllQiS9UgwLGe0dR23KY5zWJwItvjs4n8D0m-Mqi6boMTG-UQWplwfI-Rw0_tKhuWHqGAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=Y-w0-qMmE4R-bjE1WiZl6sQBBIJsxCU8SXx2hSpAoqCn4UWMlbtFeh6FqHlmFxKNPzEtAXC9QJq4fvfW51CMAo7B4KL-ElFTBAkKCPte49vMOapz_estr5akJVmi_tHFpghSXyZuYsD-ZsNKryU0-1S2TpIGBLxf02CyKlJfTGk-cmraq-YB3tFFFN3l-GQgKZyYQnGp8qhMnd9wAXEeRiI0772nOLsAnkOtQvgu13JWFa-wQYiTQrKAhri98angrgg65Pe4dcdAvkX_pllQiS9UgwLGe0dR23KY5zWJwItvjs4n8D0m-Mqi6boMTG-UQWplwfI-Rw0_tKhuWHqGAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=pE7s3MJ0sUX-44GGMl94wR6Qos_YZCD46XSW-hvASm2w9SoWO8sQfeqQpLLbwUyjAVifUc0mQ6x-JLScxRHbD98Rh-AhU7h4UhlPj6URmbkKVhBMNLciOgnFfHYsrfqd8qZy4IEtFgK3GqUnnMBuwEWeZm_3wvv5shKqGDgkgKEvyuL6oK0veJCcvrfD96bz0odXgYR_Bhr8BDGBDhSoD3C-2DnW5EDU499PXKRHw3BkrwyX1UVan0INOsYX_WoDjg5HiVcRI8VPoQfvNu5ovnHZ2Qv4fizIWtL21H-JLDysn2TwW3XssDx-hg7F8j8VHrdxd4KMpXxdz9V-9lr15g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=pE7s3MJ0sUX-44GGMl94wR6Qos_YZCD46XSW-hvASm2w9SoWO8sQfeqQpLLbwUyjAVifUc0mQ6x-JLScxRHbD98Rh-AhU7h4UhlPj6URmbkKVhBMNLciOgnFfHYsrfqd8qZy4IEtFgK3GqUnnMBuwEWeZm_3wvv5shKqGDgkgKEvyuL6oK0veJCcvrfD96bz0odXgYR_Bhr8BDGBDhSoD3C-2DnW5EDU499PXKRHw3BkrwyX1UVan0INOsYX_WoDjg5HiVcRI8VPoQfvNu5ovnHZ2Qv4fizIWtL21H-JLDysn2TwW3XssDx-hg7F8j8VHrdxd4KMpXxdz9V-9lr15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYIhj6ck1AJSyZn_Ato6ALO1k8t4lzJfkYbl2qH5Wz7Nu27HmE300pd8NbV43QkZjaOzRbNyYNUp78TkTLfY7Lk6D7jHu89qJ307rkZ1u7XcEqHU5s5y2HZIfKtfr3_TeAhw8lju6Wuwov7a17TP8ftz4p_Xz9y1au7VRXz_ArdEsXds7IVp9Wvg7t8R-LoUAoD6J422DNXo545MoRog9o0Al5DXlHnyZakFByP65LhbedtCT2TGh-XwygGTWotgCJxukNprFhNNG-oTV-O0cBDScJNKJPzJNtxkuI1l9NU7J5OyKhmIOngW33Y5s3TGTHlOxtcReHI71k1CM2RNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=j8kU6u2_IAbZRw5MIHapAjBWnh-7BArJH0x1BtiY_9tMZn21s0aCQZ3eBBtGNaQO6WeYC9hE1hVhRGKGcosCte5AzymlvTsaNyoCB3bUl8W-6lJw1Dq5s44IitZeBbg9XDiZlZum5B9ayG315EmOVzsQ5DoM4GoKebK6J_dKFFFWGdajU7gZ6-6HGh2QCqafu9ePSRk2NGajvxKaI3Slbr8gVE_Xoi5Dn5FHIdyDVhoQSuOWPZUYbcmxCfnrLGN3Yqmwzh6SHlOxoVbcg5LxgBsxgLB72ylZvrhPYqbpNl-SBgNAZZ2cjQYNyzahQYnpXcTNtA0SUXdJhnCmLO1c9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=j8kU6u2_IAbZRw5MIHapAjBWnh-7BArJH0x1BtiY_9tMZn21s0aCQZ3eBBtGNaQO6WeYC9hE1hVhRGKGcosCte5AzymlvTsaNyoCB3bUl8W-6lJw1Dq5s44IitZeBbg9XDiZlZum5B9ayG315EmOVzsQ5DoM4GoKebK6J_dKFFFWGdajU7gZ6-6HGh2QCqafu9ePSRk2NGajvxKaI3Slbr8gVE_Xoi5Dn5FHIdyDVhoQSuOWPZUYbcmxCfnrLGN3Yqmwzh6SHlOxoVbcg5LxgBsxgLB72ylZvrhPYqbpNl-SBgNAZZ2cjQYNyzahQYnpXcTNtA0SUXdJhnCmLO1c9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3MpCKVVrx1PntTNygC3Gt4JlZE2kIm26wZ6Z5dhDpwehE1TrdQZtUAIf2nKcq2cReCXqLz12_1fWi1kWZSfPkj4DF78i9WdKWSCmBIXZUoym7FJBKQLODNVt70vcubZA21NB_9EOhXBbZFCQI-mgV_wUnwM7oPTVj177HEZZieRA7cnC1lNgQhFSoj0yGS5-9eiC4hpeN8kz6fWtc8G6hi-9W9SrCpTMim0TBL24q3fon5F4YtVN9BXR8M2ltgZ0xRPOApd4T9zP8JO2I2ht_t2P9Uj9FF7gm1ErXGzJJQ1AKo2QYOIBxriA1TG5RS5WgurOX7iCE_xUFHCrROFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHNBOfObDhohgiOJ2eTtJrHwocUrIerEjuSUK8UoaoxldZT1ILI6I_-J1ec5dAm3iT04duOiDSQ-5jhTbub-inkfW8n7r56l1_IaBVr4NTqzgm2CbNrK4umla_Dg-KNWy31yoCw-jvpaYSIsioMGApnSz98ySp-Qtj97yW4VJGGkb6URkAEEadKw0cHdqbaB7PwI7b5PKx2OHfoPMWPBoGSHmEGqP_QkFJzD5P_AJdQRjuNqJP9IdE6L8NhlSDnFo4b2P1jzKdiZI9TZPa3qSgOO2mI4DrTjZIpjJn4izOAKHXQAS5oUPi1Oehd-mwIRnAI6CoAA26q-QmrN4wtVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOuMgUcNhEA2vQq2LfW_K5o9h8H3Nz3Liv7rmjnyDYkSSA6sN6qsT4bKhGyUKHyV5w0du8_I1_Qphs50pfSLDim7jnATibj3nSHD35aNnqZoWRohesqFlgGKwBCRkDXIXHJSa8CsmBwAIaCG2He1CiFhfOylU4IL4uJ4WkYSMET6pTX3F9sFMft50r80ADushpFG86zQs87fQMXFb_Xz21yjsvZusTrV23ZC4mTH6A_y3qGUEeSrXizc-85ErXHU5mRkwt470so76IOxg-bOLD_nwIIlMRo8G2wTcGDbQozsvRJgj6fwk6hD2fmxcFvi3HIdozi7fqyZlF2qo8q8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTQzLW12fcu_3tWKsVQa9HXzX4CchRGQgUhEbfiwPqosOD18R-ABbvvfcNGM6qdBnepHXhIOCA-cf2BoFQYckPz74Mf46InfqMX7rheGDqhJ-EI6LGpf-AfEkNhLWxiykNH98GdxdM5o1PygHzLNho2UjvgEt-Y9bqDpAcntAqws4-UdlxUSVmUhGbrTv4PjRdDH2sku22gNBAdWU6ljetXtXEa_kh0hPpCtBgIM8DofPpZlJi1nuzst-tFa1f8PuWGsEgb7VzNRJAC_4_Qyn1aPiPWdS3uh4jpkYMZxdpjNKBWUSc2pufo2qyvVdSQHCe5aZ6FEciqTBL-06Ep4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJk9GvyJW3OQ8I8WfukEvnqBEO6CcLIG4Mn17c7HD79QR50iLZhv7Lu8GHplNWSuHtnXskj93wexuVzIg4Oak8WSuGj8Vxg-DBrYdIMJD0in0VPGEpG1H1pZzHOaajtq8ZtAGMSY3CDirhDujALce6KEGJXeQ7u_2GX214n-Z6B8NhTjFxpcEM1ETlLHTPjzmos11pFWYAK0wDLTE7BJNtf1Vj4QQC1djg8XgYkdpYIAA7XoXyrUr2X9MmPNIcNVajs6YFwP453Cu1Svi54OdmpHhKof36v94YjotzLBoiuIsDEQivJMYbpEW0arxXDm4wX-YHQJ5pJtwF1OSxCcCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDSaI0hksBIEj3BxMW2xqHeIFfxG0Ey75XbiaGyWasBhcPdOcrSIYlLbGQc3Oq3Q9vak5XXAJrRJ5Z-6-XxZPQ5p5wz-x8N3InAXq4jIhIWOwc_TM2QKX1IeQeWK-QMRadwad-GlilSYEK_-Ay8G-YcbrJbJK83-DTtZ7fhcIcrcIYXj9mzg5UrsAYehYnBCJbwFD6RNAMHQ4fD5vyCP9nXOkvhQMKgr4V4Nt5C7rlc3BxxBd5JK_6aaNBOViEejskyRYpfPHkqU2Lqzhe4P_a2KnUf-rHoq3d5YdOE2DVgZYMCHluDb3F9z-zNzAopcF2tS9GzjiNuv0_m6SnAP8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIMDjFAkbnSqgNKc4hMlkn2Vv9ODgjeQDRgWt_WwZ9XO-Em7uMsE8CcCo-79bRVIgQaaL9REDf1-jhHheG5aiP_qkZxGrwmiqMWgYwhiyHkBnT7_FnXOdgNNuHzbRWoUO9c3VS_1YdoTRU8tQkVWQSWqlG8mhg1qIFHURxZ--ao5OmB4K24MBMCS_A42e-nDfzPrUxW0COTbOm99CE8pczo8pkbEowD2U7sE6roaWdZ95e8k47vNmc9S27QS2I1KWGq_BV3MTBbzonGBJyhl3SfNCsK-B7wU6vV6gmifLDoIzqM7kXr-CMHLWJBmGcraWZYQsa47gTIW01NgqA7img.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZlUCuV8Br1MVBvjZtYPf2PYxbqfzC0FjRZsbTzgoUZQNIQQUREjNQAdWboF1Yp0fJfVC6ysTGNq9NVwlGYKVWqZuofb5lXJ7dtuNDypnvPloOxAzsZ91GfCdqmveJaH8_lSeRViCN-O3N_rdUAqfCU1o8VyjYnaYFGuSe8lwmhQ893P3g5f5eXlYqRQ2-Om7u8znHk8oXQfDlnLovFV1hGofIt95y93ftnpXtiaQxz4XwTuxSqrjKDPl9doAHCWUjjD6CFigHy67a7rM9pXkVrgyr4OSq9V1dVTd3CJ_6GL53L0byW_6-lZ4n-RUBsjAVqCyqufu3zNUDpBgj82vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU2Cguk9eer6Qmt3nyw4KTOC1UiVWabBYUoa_xeTIA-ONq1RNMSXELp98XzRwDvUfrZMfk-eisDnYgt6KgmSCV54fYzg3kOirN8P82DqIKcDayp-f_PWRBNlgBEGD92i-SW5H5_S12btL-sJty89Hvf8gqLjxWocl2KNX1YbyPBHH2NF5STu744DPZWJDXWOL0PeXmntjh6kKOdfzn22f0IhqBieWdWG7DXYKwEBpkWxw5qkPV7cs12xyDEGAjj3Otrg-92ZUSYu5tB5mAezT_OQFceAEOFhvB7an4qZlbINtWAvymweKy-OQvYOhfg4egxTboTDnldMG__7i9pn4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk3LlkR7gOI7qJBFSjM6oW3hXXAbs_wc_0k7lIBHtQTmRMK9lgjMnR-FthAHCiBpBiX_UB_Hdbl5rpt-2Vd3GsBswoFq9-bod6rsGggTq9c5P6LIT92bAkhPSayGkoZgPCRJzAO-XxOfEqLYtEq2fyMk_lmBDTcXClNEcynogp6CS20tQwsJavwCXo6iMtePaMkV2kJashE_XaezrCQ-H9qNxzynmNrGmlg7DHkDGVDIDVwPJipwkl5i4TLi5jd1lozPD3zXOAphzCABJWWNqOK6XAr3lm7Be6xUOm5pURaBtbqJw9QfjdDEGk7uMYrI0HXNClF1IETYWue8yMZFiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=Ii32Hpip5Q5JyxJ1v-JgxIZw206_WL9RomuSl2SWggpszvdnQqvo5nsHbtzkFK_zTAdmdwxVKTWRNwiFzRd3CTprd40G36YYKGv1XikkX9vCsEU8KmcHF1lIMsAILzIDtLbTgS2z7xLjX-TZYOFJ-NXNwtABxW-dZt1K1QqLk9NdZbQjq1u_JW3tAlEmbTyd_EojMVh4jAltgIFo4mSFO9qAUz2xJ6N1yE7i0jKZJKLWFYMOxEKsJ_jbCmA6KZZWUXYWVGUmVX81plWQfIBXReAj8uMHGFTK9tZSECU59RuT-xMhMnerbdK4_qw1UFXASOx4_YvYrdbqB15HhOa3qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=Ii32Hpip5Q5JyxJ1v-JgxIZw206_WL9RomuSl2SWggpszvdnQqvo5nsHbtzkFK_zTAdmdwxVKTWRNwiFzRd3CTprd40G36YYKGv1XikkX9vCsEU8KmcHF1lIMsAILzIDtLbTgS2z7xLjX-TZYOFJ-NXNwtABxW-dZt1K1QqLk9NdZbQjq1u_JW3tAlEmbTyd_EojMVh4jAltgIFo4mSFO9qAUz2xJ6N1yE7i0jKZJKLWFYMOxEKsJ_jbCmA6KZZWUXYWVGUmVX81plWQfIBXReAj8uMHGFTK9tZSECU59RuT-xMhMnerbdK4_qw1UFXASOx4_YvYrdbqB15HhOa3qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=LnVg7bLta_335CUWUo-_pF8Z1piSWc9SbVmNw7URUcRgVXPNSoVdcg9DlGbob83CzMXxlISgDQKJdbyCtiXWqpggt5zZGwHobnfio74ypBkVUGV9vfpBUztlI4TnEq6toehGp-zr2o505I-AlVSl2UK4V0AO_LU6qAeMcb6B2PdTJpWaxXnxcEGnjrr9lWRYFAFKbkhGdCao0UZDKdR_SYFsn11s5aeUn7hzNzpzvZx2iYK03fCZJi_Z7JwfUsyYuGSIHeUFK28lo2DsihKbIdjWFVkOD4VSyl02qr5ewKKSARX-AxwjVirYm4TBM-qZu24-5-sJ4Z7IUUmLBpAg2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=LnVg7bLta_335CUWUo-_pF8Z1piSWc9SbVmNw7URUcRgVXPNSoVdcg9DlGbob83CzMXxlISgDQKJdbyCtiXWqpggt5zZGwHobnfio74ypBkVUGV9vfpBUztlI4TnEq6toehGp-zr2o505I-AlVSl2UK4V0AO_LU6qAeMcb6B2PdTJpWaxXnxcEGnjrr9lWRYFAFKbkhGdCao0UZDKdR_SYFsn11s5aeUn7hzNzpzvZx2iYK03fCZJi_Z7JwfUsyYuGSIHeUFK28lo2DsihKbIdjWFVkOD4VSyl02qr5ewKKSARX-AxwjVirYm4TBM-qZu24-5-sJ4Z7IUUmLBpAg2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=WZYbZGWtkDvBo-OsmObmzxshWg53x9Mk4vXekF_QaXKm6Xj81bVzLQgD366VusrJ3QEPvqjXf3XQ8Uo4OVyHPzGNxug-XlyugY3zGdSLCmpKnJEa3hLbg6aLdP_2ntt05y6-axKxb3ddNzQH-2-bs2JaBbCupKcUJWZtY-i_Gflp7_zQ0x38lVF5qVV3gmDqjH0rA-FJ930zX9JlnalDxjWwq5vqNxex1zreZbRTokQRGkkZPvlYBe30t9Lb6p7805IkE869EmS8hwPNEn4dbpT9bj5lbrbPeqFNAeri077d7YvcJWNyfgT70Ofd50tQQVgrYxqwXms8kTu9fCrlmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=WZYbZGWtkDvBo-OsmObmzxshWg53x9Mk4vXekF_QaXKm6Xj81bVzLQgD366VusrJ3QEPvqjXf3XQ8Uo4OVyHPzGNxug-XlyugY3zGdSLCmpKnJEa3hLbg6aLdP_2ntt05y6-axKxb3ddNzQH-2-bs2JaBbCupKcUJWZtY-i_Gflp7_zQ0x38lVF5qVV3gmDqjH0rA-FJ930zX9JlnalDxjWwq5vqNxex1zreZbRTokQRGkkZPvlYBe30t9Lb6p7805IkE869EmS8hwPNEn4dbpT9bj5lbrbPeqFNAeri077d7YvcJWNyfgT70Ofd50tQQVgrYxqwXms8kTu9fCrlmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WIfP2kE2uuMbssvD3Xgg8mIl3IalxIePDKNJr-WGQo5PFeaLXIeeIkQbfr_TUz5sHFkD4MfhnYPpaQCMwVNLSJCUnFZA17i2nMn02OvL1Le-g1Wx9i1m-Jo8QyNZpTG_0fv3JYxh3euvJ0TemVvQpp6czT9Slb582UMNxgB_ztTJyh6LbIqX06RgMEKY_negFa0eP6Ce2F0wxMV-lba0Q30e4kmW2VW3x650linvzQM5Nxz5i9z7QNhTArnzRjJE_EhGeuvFAFgSnQxkMNiBBjhBqclWy7U9ap4j9pf2MOct3e6MRnPigf2oYgKS3q31plZuqI7lERMWfpPgoBUIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAT-o2Al0dIEDAHSwvvpoJ82vcyQ399syMJAnQUGi7Y1Gr0FOriV-PHv667e3O3mAATC1jTbe86SsoroBwNwFHKPTiszSox9z4A4avbUjifOCTIImfYUFT4HrN89kRi5rJuaZYqCpJ9vrmUK-uNiJ_GQuaXzgxtI2G9uxy8-QovNZRc6Q6T1VRPwTuhrxaQ6AkqXh6hc5X4ES8uJseegrFakJSZ1Wxnj7zVyLRNeT4Qb6GknaTAUFISwdpAqRwbjpDPLikrOlP8-9hGL9FB9IRB6-kLfTw-5qwNvJ5wpCyqyxZH4BpkCY3uSPjvaV73g-QoFlVczwzhhJYyS78O7lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAi_kQ_LvZj8GXONK7a460ZlPiSAKlX3wXpzIcibNnkEtduH_wAKsIu5t0h_Um8Sd5_mdzQoOytlDuNWVuEoFc7wJPJz42XciJmR5Ve1obT-N3Z3P7Tw9JCxGjvKvPgrByPFV5ePi5xQOqTLwdFwhWYKvGLr8-ZrkItPS0SKmNnUmN2hfnkFX4FxmXXGdN4AupEV5RPrI_Wm1TMuF8Hy2tUXhtylqr0psDWtgkTJfgmYNUFMTLLqlcU5-P_ZbXdVtvb6zM02R1pHrNoLNscpNc7_Y84B-oEGerKE12bw0gR_qSAlz0c36-KQT5hMpwy0s3SM0VZr8Ouaqjsg4B6q4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=du4RGOYlhHpNzexleoJVPRlW-5MwrSBJQyng4Q39znqYZwYfOtYrov4_By_pu-E8rk-lstMgW20kqkqeshEByCdWYo1mThhwN0NGGKFG5nD8E9Sk7G5FlrbLWhvXm73drN9FRacqFDOuvSjATbYrOrbJUjwFdeEu2dmM5codVEh9LM9gD3waZ1L70cHoJZGAtVHIkMqGor6vI1bGvPK5weSYxB4PHR3IdPpef_n9c9C-Y3yJl17W4Rngpau60vIvsVOCoKQ5iT1fLgjo3LZ1HU8Cl7pActo0nYtEERiLO7nbL-pYEmGURcIm86026JVvjPkzdndUIGK-ajaWi_yyfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=du4RGOYlhHpNzexleoJVPRlW-5MwrSBJQyng4Q39znqYZwYfOtYrov4_By_pu-E8rk-lstMgW20kqkqeshEByCdWYo1mThhwN0NGGKFG5nD8E9Sk7G5FlrbLWhvXm73drN9FRacqFDOuvSjATbYrOrbJUjwFdeEu2dmM5codVEh9LM9gD3waZ1L70cHoJZGAtVHIkMqGor6vI1bGvPK5weSYxB4PHR3IdPpef_n9c9C-Y3yJl17W4Rngpau60vIvsVOCoKQ5iT1fLgjo3LZ1HU8Cl7pActo0nYtEERiLO7nbL-pYEmGURcIm86026JVvjPkzdndUIGK-ajaWi_yyfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=J1om58VDwYIxEuziQn0oxJlGkzUoNXT4TX5ErOXCQtzvvKDewxlJROFK-mUeQMYTV07nIHGq5Bf7OAZSiXYra1yCoP3VHdG8UApdIYQF63tRS2k8ezyPtKTxGpFboVObPrwtgdqnNAHx6MV1UXRcKRb4H8OT5AoU9hTN3fTF0R-rUNDNolP3qBxiX6zCCVBJYXLDlqO2OaTB1Jf4jP_v5xHpfrpm88C6yVB8qZ_Lbc1GPzPXWUoyvQHLQWVMzIswQ1jo6YPxkDVL4dmDszcy0cvPYTNHWTudGupaaY9qooJVINF9nRRqWEsnF4bjeeyZkSMZGBjU7OdGNr_3CgKvOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=J1om58VDwYIxEuziQn0oxJlGkzUoNXT4TX5ErOXCQtzvvKDewxlJROFK-mUeQMYTV07nIHGq5Bf7OAZSiXYra1yCoP3VHdG8UApdIYQF63tRS2k8ezyPtKTxGpFboVObPrwtgdqnNAHx6MV1UXRcKRb4H8OT5AoU9hTN3fTF0R-rUNDNolP3qBxiX6zCCVBJYXLDlqO2OaTB1Jf4jP_v5xHpfrpm88C6yVB8qZ_Lbc1GPzPXWUoyvQHLQWVMzIswQ1jo6YPxkDVL4dmDszcy0cvPYTNHWTudGupaaY9qooJVINF9nRRqWEsnF4bjeeyZkSMZGBjU7OdGNr_3CgKvOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=lyUhC3xAiKbzqFpRotjktKU2L7UdDqIoUk2qbg6iYZ3Ux65t_gTDQfPycNVrokFGtyHz6Ku59FRTLG0n9kbSRxwCpo6CmjJGl3tCUUZjjB294n-E2LVdUDYFhdF295Zm4w8VlJIoIkPhc1raNAuj3D1ay9UMrYNoBKMrOIdQiJbK-q1TUXa2TCfOoNjhYrEh60LYobVlz98kbyWWMnsCYdTJRVj2jzWyQbqw-dFev0I8A_DqKC2R5nFv2YoCicx6w3X9FgC3YjyzbaTPHoJ2w0qQk6PD8GsftkS0kgNrHCzL9GskUy52nljevxK8BFSfnZCzZKV0hOTRkdrg-s5Xjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=lyUhC3xAiKbzqFpRotjktKU2L7UdDqIoUk2qbg6iYZ3Ux65t_gTDQfPycNVrokFGtyHz6Ku59FRTLG0n9kbSRxwCpo6CmjJGl3tCUUZjjB294n-E2LVdUDYFhdF295Zm4w8VlJIoIkPhc1raNAuj3D1ay9UMrYNoBKMrOIdQiJbK-q1TUXa2TCfOoNjhYrEh60LYobVlz98kbyWWMnsCYdTJRVj2jzWyQbqw-dFev0I8A_DqKC2R5nFv2YoCicx6w3X9FgC3YjyzbaTPHoJ2w0qQk6PD8GsftkS0kgNrHCzL9GskUy52nljevxK8BFSfnZCzZKV0hOTRkdrg-s5Xjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=WLB7YzVH1u30Rpz1FjCv-ErrFESJMYkZxGivu1ggudXgxILNXoUtdsVoA4Ah8Cv4yNjKnWhiieUjpHPHb-04DwfdxfCHElkMNOM752u-YdIKlaAaEBim41VwKOX7sxGGGBn7Ri64Z-ql3tvbyvck79Rz2Ggp2vInQgaq0jlK9Ur2HbWWANFWGsYIbIQUohwPxEo-nLgjBrk3Y84x-jfC1ubAqXbLKJ7_t71M7FQkguOtHpS0r-sdEimU39jH3BhS1yRsDXyQo08g7LWjtDSmyUc4lSi8W07KdZ5PI803nEBFoUxMQdiLk67TI-9743XuHCN1Pq953KyBw9DPoB0aNoaB5p4eI0C5ZmzPRqnY9HSqIISPPG-lXnJQYbfEhuX66FQJx27hcqOJqnvYqMdouczlbIp8JxDTZ5Hh5kzFEVUdWnfnYeIib9jNKE69IW9OGsYRXgjOgsr6lrX_-idlyofMEEEKEowsNzZyD2ODnUgE9plT_sEPOTnSmEHiXlaELR5O6RX0QearElExao-nOOQiYsiXKbiw7wKApZBv1_M76Dhtt0DDNb58zrQ1_-G-e5yYDF36Y8glPStMtLP6ddrAsOMtMxVMqFewv-ERuUPiFeBHg_hi1ZIxvhzTqZ0IfMUmpW45HoN56huYVSGsiL0u0Rj7u2VJr4x4af39uAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=WLB7YzVH1u30Rpz1FjCv-ErrFESJMYkZxGivu1ggudXgxILNXoUtdsVoA4Ah8Cv4yNjKnWhiieUjpHPHb-04DwfdxfCHElkMNOM752u-YdIKlaAaEBim41VwKOX7sxGGGBn7Ri64Z-ql3tvbyvck79Rz2Ggp2vInQgaq0jlK9Ur2HbWWANFWGsYIbIQUohwPxEo-nLgjBrk3Y84x-jfC1ubAqXbLKJ7_t71M7FQkguOtHpS0r-sdEimU39jH3BhS1yRsDXyQo08g7LWjtDSmyUc4lSi8W07KdZ5PI803nEBFoUxMQdiLk67TI-9743XuHCN1Pq953KyBw9DPoB0aNoaB5p4eI0C5ZmzPRqnY9HSqIISPPG-lXnJQYbfEhuX66FQJx27hcqOJqnvYqMdouczlbIp8JxDTZ5Hh5kzFEVUdWnfnYeIib9jNKE69IW9OGsYRXgjOgsr6lrX_-idlyofMEEEKEowsNzZyD2ODnUgE9plT_sEPOTnSmEHiXlaELR5O6RX0QearElExao-nOOQiYsiXKbiw7wKApZBv1_M76Dhtt0DDNb58zrQ1_-G-e5yYDF36Y8glPStMtLP6ddrAsOMtMxVMqFewv-ERuUPiFeBHg_hi1ZIxvhzTqZ0IfMUmpW45HoN56huYVSGsiL0u0Rj7u2VJr4x4af39uAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=pP-y7QntAWYgIYI000i1fIk6QaFmsX-5_sOdESOsuOrksbcuQQ3i9qE-6PFfpepQvNr2PrJnnpO2zNLyFC1XPfZgXyFkoMpcDwc8qPKRMZQHrlPJ5g1Oo2Z6yG2CeTTljQ_L-k4ubbLEmoxXD5m2lJLsPGypM0p88haWhyPq8mURVvdG3J8gB3NBcQnbUyQiN8UU9lNK5iLq60eCSZtzSdxx9R-os0gV9EeHnU-iIdpDuzChOhuw52HiJgr5YZad56J1depdRBXi0vM-NAU25rVjv4x_gU-DTDmYUGxIkNG9Q0MCXq7Po_4iEq5SFG6FYt8LBDycv_hTy99J1-9YNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=pP-y7QntAWYgIYI000i1fIk6QaFmsX-5_sOdESOsuOrksbcuQQ3i9qE-6PFfpepQvNr2PrJnnpO2zNLyFC1XPfZgXyFkoMpcDwc8qPKRMZQHrlPJ5g1Oo2Z6yG2CeTTljQ_L-k4ubbLEmoxXD5m2lJLsPGypM0p88haWhyPq8mURVvdG3J8gB3NBcQnbUyQiN8UU9lNK5iLq60eCSZtzSdxx9R-os0gV9EeHnU-iIdpDuzChOhuw52HiJgr5YZad56J1depdRBXi0vM-NAU25rVjv4x_gU-DTDmYUGxIkNG9Q0MCXq7Po_4iEq5SFG6FYt8LBDycv_hTy99J1-9YNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=syye4QAvwMIbsMaTPn8pnaXDqIce9058g8OWP3xEXH3mbfKq8daLIk1Va78qN4D1V-HURfD7PsTbWOiByNGfmV9zSfW57mDgj1ys-pg0jpkPNH5Jr4AytyOJCH8bekm0gvqo_eC069fHBFWEbAODx-EhVRLdo7zy9bsrwPOtiMgyndtttC11qbJo1UbOMjLp_X70vS-8kAWINe4tenZiFyGc3d7mz39x-KzmdhzHmMUILPXzDJaB9dS8I_xeyQw9nhErYiERk4s5VUync56UC_JJhcbylQ8INlQci8NlLsEsmH8pW2_hBij_4JzDacVnButyhPhCNvAbNTo-1mVMmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=syye4QAvwMIbsMaTPn8pnaXDqIce9058g8OWP3xEXH3mbfKq8daLIk1Va78qN4D1V-HURfD7PsTbWOiByNGfmV9zSfW57mDgj1ys-pg0jpkPNH5Jr4AytyOJCH8bekm0gvqo_eC069fHBFWEbAODx-EhVRLdo7zy9bsrwPOtiMgyndtttC11qbJo1UbOMjLp_X70vS-8kAWINe4tenZiFyGc3d7mz39x-KzmdhzHmMUILPXzDJaB9dS8I_xeyQw9nhErYiERk4s5VUync56UC_JJhcbylQ8INlQci8NlLsEsmH8pW2_hBij_4JzDacVnButyhPhCNvAbNTo-1mVMmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktZLKClo5pESdmLdVehAoz2-OoJalPs7KJX6yVt3o02ZT2ddmGSuc9D7tD47Nd5soSPMap1YAVoczdbC6Nh0EGVUzw5baqDo3Fdx2-lloIrBjF97RRljOzWOS7KM_IrrETzae9UyK8paek27uaUVt-dwfHzkdEeSjzC3M4ObpFTLNszat_kDQ1oJ6U9a_ANtlUjgyISq-1-snSeqFzQ_2Q_lPh6fLB8JYobqjiMN8En8VBY5nlABZS6_8QvrYuHaXCEFUTKseT8DyDk2oKjkhxRyAeBf0AxpXjcaPYclkFwSXQ_u1xMKqtcA0qZFtHt_p9DzQQjMIALjuhBzcldGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRw17oF6lKM6IJha4vmHnoAeXnP8gY_Jic8KS7JTDUEmgv9kW9ugVZfS4RWt0OPQ0q5Y7eIgJ_bZktUuoyJ2j_4zd_1PS83QshYrrVIf43KX2mrPOlkjue1WKzTpiafbIjjlCf1qWgwjN3X2EgwTwOobjJskLPobyl_nPiyHU-um-KH1mbQhjDtOEl-dhvQ0-gr2voSKbJhRB46uMuyJiGGHJjebxhawhLG4Fj7_5-MOUrQaR2JA3GQ5IcKTEBmqWTNe9xIoRfEeTWepyncduRQLDU6V0WdpMlqhLL4pDKH1TjDMJEM2XzGc2fMJKVZ9coxzW9znbeP73YY5r3-ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=Sa5C2iWQsB6MEZrSQ9cflSoXjkx-k6DDvJXR0Ofod81zpwM1Q9_AhrtHpvSL3_RwasAqbFDMkwvHSGY0SxdSHPZuF4SIWDlx3Zdf9_4LyRnERoVHbu5-JpjXJTju-v3xP3Xsgrgd8vsYtusk3-x2AF2ldoBg_P2mr2GAoiGMye2q_XQwIjGkewZZhjgFamSoAmqLU8My7CbarDd5B5pvZcC6NzF-Nkn9hpQ8_5WzgegQtt5qPWr10C-OhypiYAyp_2v0dEM5IsAycV_v6tpv7yPM4U1YV7BTrIr8YPYxekOJPQSaF8WFGke1uZJu2qZx6OeJNovd6JYH7K__u-FBDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=Sa5C2iWQsB6MEZrSQ9cflSoXjkx-k6DDvJXR0Ofod81zpwM1Q9_AhrtHpvSL3_RwasAqbFDMkwvHSGY0SxdSHPZuF4SIWDlx3Zdf9_4LyRnERoVHbu5-JpjXJTju-v3xP3Xsgrgd8vsYtusk3-x2AF2ldoBg_P2mr2GAoiGMye2q_XQwIjGkewZZhjgFamSoAmqLU8My7CbarDd5B5pvZcC6NzF-Nkn9hpQ8_5WzgegQtt5qPWr10C-OhypiYAyp_2v0dEM5IsAycV_v6tpv7yPM4U1YV7BTrIr8YPYxekOJPQSaF8WFGke1uZJu2qZx6OeJNovd6JYH7K__u-FBDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=uBjV8A7KXV_TYvDNvHNTS9WlX8zr4gDC_wAu-pFPP2NukqIxicafto26Wy0SzZdQ60ttbuv5LPjAl3PVxlb3xlpcXTAyZr1DXeHTSLTryKZKj03r-km7PS_WcYKiGWh7kFdBFPYlS0yql_yuJJs2jt3BiZDSdHFn2MICHfssa26I-FA34CFez1j24_RMzsEhvU_Y1Go_IrJ6thgQW9F-4HdBf2y1ifVmX-PKm5G5jWHesqfmGeJXl2ADzW-rUHZcykw82yj-IdweYWB2qOWckROU05ZZA2BpQQg1t5lDXgI7HJwyNGpKtSWx12CBvKGYgfNBE9OARe9F46lu-nxMhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=uBjV8A7KXV_TYvDNvHNTS9WlX8zr4gDC_wAu-pFPP2NukqIxicafto26Wy0SzZdQ60ttbuv5LPjAl3PVxlb3xlpcXTAyZr1DXeHTSLTryKZKj03r-km7PS_WcYKiGWh7kFdBFPYlS0yql_yuJJs2jt3BiZDSdHFn2MICHfssa26I-FA34CFez1j24_RMzsEhvU_Y1Go_IrJ6thgQW9F-4HdBf2y1ifVmX-PKm5G5jWHesqfmGeJXl2ADzW-rUHZcykw82yj-IdweYWB2qOWckROU05ZZA2BpQQg1t5lDXgI7HJwyNGpKtSWx12CBvKGYgfNBE9OARe9F46lu-nxMhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=lfa2lEOMLqY7_5v744D5n6J69SN1uAaBV99cmo55WDTPiVrkrvS-ABADwHAy8JtFXGrgUCAZazrvWBn3Y60vejro0MYO6WIFLkEVzkCaXPuz3Jcz1qm_1o9aBraevvzg-QxoGugsx1zKXOLuZzMWV0BQ9AhT5_iHME3a2Roe9HnnWeJhGlm7dsO_EUr45sjtOT9dwRJcgDOmxhuehMnsjx0R7fsv0qlexYc9Yu8a5gbvCnYoi9LsRFE8qPS-t3eKIZRo3Jn9K50OYL7Dqi1hnrFGQchfAU6VUM58IkYIvFRRMNx1GqLecSACZWHX9udmenvcfWj_A2HEiaC-rx4knA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=lfa2lEOMLqY7_5v744D5n6J69SN1uAaBV99cmo55WDTPiVrkrvS-ABADwHAy8JtFXGrgUCAZazrvWBn3Y60vejro0MYO6WIFLkEVzkCaXPuz3Jcz1qm_1o9aBraevvzg-QxoGugsx1zKXOLuZzMWV0BQ9AhT5_iHME3a2Roe9HnnWeJhGlm7dsO_EUr45sjtOT9dwRJcgDOmxhuehMnsjx0R7fsv0qlexYc9Yu8a5gbvCnYoi9LsRFE8qPS-t3eKIZRo3Jn9K50OYL7Dqi1hnrFGQchfAU6VUM58IkYIvFRRMNx1GqLecSACZWHX9udmenvcfWj_A2HEiaC-rx4knA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1tNv29LHFn42Fu7amSyFfkN-d3fV0wUY6T9VZUFMEXVoTxqCmj3T1iGrDhggr9hTotL4s9a3C45r6JWf_TgJuN-pvjNKiVPlHf9WZFanD1r6YiQf-vp_38tcHmRg8SxqkjSSZ5dNWX8qwUgJDT_9PUkSRUVOVFPNDQXjSAHo5dqPrkzmUshc4iXILzpDUAmkKmUwjNjdm8nXcW9FibMPjKtjESqIEjiafgOjE76-U3mUixsiG8uUPfERfWyXbRR0JEEn7HqpZ8vooG30EJsToEqIG6KtjOrIKdTHEAfap2bGrA3efxcluvLSBWWMm0MhXVM12XMk6TJPVb3icYiPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=uk78fhV_s2699ZOeoSeIUa-mCoRJMM-qx5_vkj1zy7e8v05ISd-VEaZESrMyGO0kEmSedXGpXJW_I4Nmta2G9kTmxsr7xHYWVjNNX4xnD9RQtPOvx9okmu0j-70VWkCTRjq1VzGXR0AN-1y5jPIC-NnMUR7Y2o51HgDji-zmpd5adRI2dCS10RE9giaFnEY1x-uliHDr1_kjRpnRo9C9g7B2glgVpBy4bCY7YSc0CPLNQD9Dns6TBx08Lq5bwcf8Z_QRqvSnynt5ljIIo_iHrmrkBoZ_qYHEj7PdAWfEEndE1_FyaXy0oYQI8PXMiYVDZQAsgu-CHId2Iv8JqNTITQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=uk78fhV_s2699ZOeoSeIUa-mCoRJMM-qx5_vkj1zy7e8v05ISd-VEaZESrMyGO0kEmSedXGpXJW_I4Nmta2G9kTmxsr7xHYWVjNNX4xnD9RQtPOvx9okmu0j-70VWkCTRjq1VzGXR0AN-1y5jPIC-NnMUR7Y2o51HgDji-zmpd5adRI2dCS10RE9giaFnEY1x-uliHDr1_kjRpnRo9C9g7B2glgVpBy4bCY7YSc0CPLNQD9Dns6TBx08Lq5bwcf8Z_QRqvSnynt5ljIIo_iHrmrkBoZ_qYHEj7PdAWfEEndE1_FyaXy0oYQI8PXMiYVDZQAsgu-CHId2Iv8JqNTITQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=mggPXlW4bG35dIi3mNSp8KBKXBfIV7AdPoeTvjvTSZnv2MZ_y7MnrFJaL6qK4NzYTIrzHr85ClA4JL97zYO9u5w8lfdzqvI2Jx7DS9KeYEix7XMMpem7uXOXV36nEHQ2wXi7utGmL7bMIrhdRUMgtVDrsRGUhO6l6ztfn3ZDLeQ7PApn2ql8mA1dutEl8Vo0E2RDbPgHCOWcKnqYwe99fwBAVOwh3TYS3zy5n_RblBzs1rKcHoZtMXaqlrY8HMMR7U2U1XXQGswQwds8buci9KQL_WH2bIc5--PEQsXLS4v4gOBlO4cMs6fxl7Pi9ilUvZbbhG4RUh5zjrc_wU_vSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=mggPXlW4bG35dIi3mNSp8KBKXBfIV7AdPoeTvjvTSZnv2MZ_y7MnrFJaL6qK4NzYTIrzHr85ClA4JL97zYO9u5w8lfdzqvI2Jx7DS9KeYEix7XMMpem7uXOXV36nEHQ2wXi7utGmL7bMIrhdRUMgtVDrsRGUhO6l6ztfn3ZDLeQ7PApn2ql8mA1dutEl8Vo0E2RDbPgHCOWcKnqYwe99fwBAVOwh3TYS3zy5n_RblBzs1rKcHoZtMXaqlrY8HMMR7U2U1XXQGswQwds8buci9KQL_WH2bIc5--PEQsXLS4v4gOBlO4cMs6fxl7Pi9ilUvZbbhG4RUh5zjrc_wU_vSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=cF1WMYspqlXaSTszn0LGBqLjIjJT7uOTNDukfxglxMX9yLwKKkJqccfr36hYSx52-jYps-q5ELJc9DrF4OPVph1Bj1XloMoKLfJM_Z7uqAgc6XWtvuUG33SvFCf7_FWoz8z-JBK3w6LKrMhG6l8Nz8GM6DQ6husfsZfeok1Ho2rm7ydzmPDECrOU1Mdl5QJ4Q9jWlCcsTEYsx0w7gjo6O9wPbWzK2y5SSOnjp5-R0S5kdsMh8FGFas3RkoODdaibNILBvTyscGBmwSiXLI58OLPQV_GmW215eEVdgPVhhXnQ5-hc-MMGJAGCzzsu96704APnvBE1ONqV3riiNV_C_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=cF1WMYspqlXaSTszn0LGBqLjIjJT7uOTNDukfxglxMX9yLwKKkJqccfr36hYSx52-jYps-q5ELJc9DrF4OPVph1Bj1XloMoKLfJM_Z7uqAgc6XWtvuUG33SvFCf7_FWoz8z-JBK3w6LKrMhG6l8Nz8GM6DQ6husfsZfeok1Ho2rm7ydzmPDECrOU1Mdl5QJ4Q9jWlCcsTEYsx0w7gjo6O9wPbWzK2y5SSOnjp5-R0S5kdsMh8FGFas3RkoODdaibNILBvTyscGBmwSiXLI58OLPQV_GmW215eEVdgPVhhXnQ5-hc-MMGJAGCzzsu96704APnvBE1ONqV3riiNV_C_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=DeW-S4mWwtMxcWzkEt0gLNNuZZgea1ReXaLqNwM3Dq17Y3nv7B0hcpk0O5xTybMlS1iahb_Uyw2ehRCyKAL-_GA0aYZZ7euzrH6PWcQ_wok7dNibaswJo6mHvVVztc4WzMTUTyG579EHj7P7s4tblWnuekqgPCb0If2fiv6jj0iWvLoRVgDY-YLBFL08HqL3Sb6si-HdbexdDfekWymkDV5O8Av8bbe-jX6PFOp38O9Xc1YQ7HQZj91BU6AYGsle9fuFq2FsUI0KItdzrg2XVFnrzE_ku7-eLmnNuggKokqlNT8Joauaq-R1GJIl2g1R8EV1lo5-IGizNEbXWmKxSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=DeW-S4mWwtMxcWzkEt0gLNNuZZgea1ReXaLqNwM3Dq17Y3nv7B0hcpk0O5xTybMlS1iahb_Uyw2ehRCyKAL-_GA0aYZZ7euzrH6PWcQ_wok7dNibaswJo6mHvVVztc4WzMTUTyG579EHj7P7s4tblWnuekqgPCb0If2fiv6jj0iWvLoRVgDY-YLBFL08HqL3Sb6si-HdbexdDfekWymkDV5O8Av8bbe-jX6PFOp38O9Xc1YQ7HQZj91BU6AYGsle9fuFq2FsUI0KItdzrg2XVFnrzE_ku7-eLmnNuggKokqlNT8Joauaq-R1GJIl2g1R8EV1lo5-IGizNEbXWmKxSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=I39i6v3Pt9DABI8GZuJ5fUaspNhm2SxUVG5cVkfpl-9qFHaMPRnK6yXh0adRl0mBfdOm3mrmThJ8J6q05jCKZ2kjMdq5xT2ESa-sF3NX0lti1pUKXJh6Nh4CqHoHSXR89QV-r5QWos-_x22SnhxE5eoJO3dcN6-67cF27xBXnLs93LqHuXmL-FCoVBC4KRyHgkAY94ME1HVXYsOyY7PwE0xL9rGVCS_M3PqzNhUapyCkCkGPpWKIDqradhoVRo0UO_pjJ5A08j8J4o80LtM0IiJl-rceYCusMZ5JgEsZ8LrWk8qrv7nYHk6B0pKbMb-py7Ycvy0Sz22Lnw4jjF2jXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=I39i6v3Pt9DABI8GZuJ5fUaspNhm2SxUVG5cVkfpl-9qFHaMPRnK6yXh0adRl0mBfdOm3mrmThJ8J6q05jCKZ2kjMdq5xT2ESa-sF3NX0lti1pUKXJh6Nh4CqHoHSXR89QV-r5QWos-_x22SnhxE5eoJO3dcN6-67cF27xBXnLs93LqHuXmL-FCoVBC4KRyHgkAY94ME1HVXYsOyY7PwE0xL9rGVCS_M3PqzNhUapyCkCkGPpWKIDqradhoVRo0UO_pjJ5A08j8J4o80LtM0IiJl-rceYCusMZ5JgEsZ8LrWk8qrv7nYHk6B0pKbMb-py7Ycvy0Sz22Lnw4jjF2jXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=LwwccGz_Xo1ewcB8VX0X95Umb6ELX9i3OHEhA03qnPRrWhGthgdesuuY0ZRCZLV0ourIcheihz7bbcSz7az_NPfnz5JRxqo4VB3rbtPuprYRcNc9ozRFm_uFvG88dKu37xLaGAisWrJgm_PKWIBXYureIz1iTlzgp5bAh22F6rokytHMxJ8lFnhpFK0dw383uE3y6omjHAT_BNntA5nNJNmOTvsz6Dei0ofiheJhDlGGvYnOvkc_ftgrqhLLzDCNDOEeYpnUt1jDvh4IVi99GSDVGTcb9kpjIg70EG_ccpLwRmDxaQfSX6SUS7PFeDwZGZFD4ZQKwV8CXbQTXC5rF4R_6xfSXEjNiRpQp9jqbMLg-Mdlk4Oa5ALohcZeSngxGr-OKWLhI4aCxjjuwkoYKl1G1lgST1WA13dl2zDcBTO5hzm5f6YQdFxWZbiCj-xcc082gnU03acb21K3DaQdAQgHEt5fDOpPrMZFVw9AEcNTH9jr6wkDZ_SIOLensyeeXoF94yOhx0I1NDPChX1uDGGqF08idbYat2759IwCJZdugFF4bHVnixE4UT8-6ZneZD6fIdS4zsgxL2eA8tb10Vlxq4xF9LvMXcxCIw8wpc92gMhlQ4RgaXH3SrB7SCb5jEjS-s29ueIZvUvvnSUvk21rPq2adRjcC8JhsKCfXD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=LwwccGz_Xo1ewcB8VX0X95Umb6ELX9i3OHEhA03qnPRrWhGthgdesuuY0ZRCZLV0ourIcheihz7bbcSz7az_NPfnz5JRxqo4VB3rbtPuprYRcNc9ozRFm_uFvG88dKu37xLaGAisWrJgm_PKWIBXYureIz1iTlzgp5bAh22F6rokytHMxJ8lFnhpFK0dw383uE3y6omjHAT_BNntA5nNJNmOTvsz6Dei0ofiheJhDlGGvYnOvkc_ftgrqhLLzDCNDOEeYpnUt1jDvh4IVi99GSDVGTcb9kpjIg70EG_ccpLwRmDxaQfSX6SUS7PFeDwZGZFD4ZQKwV8CXbQTXC5rF4R_6xfSXEjNiRpQp9jqbMLg-Mdlk4Oa5ALohcZeSngxGr-OKWLhI4aCxjjuwkoYKl1G1lgST1WA13dl2zDcBTO5hzm5f6YQdFxWZbiCj-xcc082gnU03acb21K3DaQdAQgHEt5fDOpPrMZFVw9AEcNTH9jr6wkDZ_SIOLensyeeXoF94yOhx0I1NDPChX1uDGGqF08idbYat2759IwCJZdugFF4bHVnixE4UT8-6ZneZD6fIdS4zsgxL2eA8tb10Vlxq4xF9LvMXcxCIw8wpc92gMhlQ4RgaXH3SrB7SCb5jEjS-s29ueIZvUvvnSUvk21rPq2adRjcC8JhsKCfXD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXZkTXgW-SQmy5QohfoNYLn9DJQMuCEo_4MJ_h1OLzG_1Hmi9nfR7WIlTEqhiKMtyatwAQtOkjjS2FnwQiNIzV8HsWVJUvMTXcpnleKb522ClUVybaBM8YJVvgsHLeuvfANzWNKfhgBqYPYz2T_hdZzVqm07Ky-ZLDLn_RoWpOu-wVYsScRsoSkwjsAHHwrcg41tSp_g7lkVkqMBar2eDzdshVwJ4r96PR7K94EFQ-a1hi59nXht96SCVIXcetC1sskUuQoO_q49Di3QUJ-wauuVAYCViuoyACFT2hS8nBbCNgw7oGU2FtdedeiFd-7gC6OArMEhA_wANsULvOP1Ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cZJc8jksN90iVLJC2PYAwME5DUeoh8nZiz-j5zXCruc1pKSPf7An9oDPLuPo6G1egI9Vs05FX6NGCMudVwz0LbPdEhf7MTsQ0i6-rRkJGyQ5fOl-Yv93QPd-oAVs5HOp80IWeMFKlndWoeMpJXs9VuHfVDFRLh7IPuS-W02l-IuXZLUf2Z_we6psRWGHOAwdy9MQh5ZrCSh3tjDiy3h4LUrRV9aCyO6_Y_TpP1K7kbTaAS10OGnBN-kpVhciRhYNO_uHQQF1hsOtScAoxmMNXPX6HnJFykoizXBTxq2USxWzfHcEoWWLgjUgGmNq-c5wLjip6ipGujN17HrRWDu28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbhTbrSKjJsywSfrDnNqi9lJDVW_Wl7saUOmwK5veaTl0SFIBDxoAISIggDxa8uP4DUe28PS9eju5dVQwZIHpGOohQED4K2nN9qrden5kLg13mVYrMT0Z5WL1sM-sDLXA43_EB0Vd7nzlMiQrYrU_my3iDNIxqoSaBKU5DGg62svVhIgIz8cLiOYRxsI20D5854zCDq8NYhcxUCl1MXv3GRQ4h8Xh3EtSsJKatQkb4f2775yfhCg99e_0JnWXhyar5K6obffZNEhNoEAbV7bcSgeyoLMxQnq-oJVTc8ABls2NOuHpW3yEtirqW_j4kkhJNxi8GcQIpPfcc2HXQ1eaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=ZmJX9HQcezHHmNieSUJZ_jMwvA5DAKHI-yDqmnfUWnz21JD80ky82-0a-c9Xvaw_IIHLxGgCx5KOq3MapoxqzTCVJiYGQHa-3stLstSGOPi4ARad71SNUkgsERR2603cUHiJHd1iizVqd1t72U_tyrMtVgOLVDPa324ohI47vCAdBy-vzp0ckrMhYsXOrZd1hPmClF8gJDciFFOTDoK22qixDLiF4VI8eIN2_ichhHWHygZiCz8BlCYMgcSgDl-XqqVz20waQgcNynnGom4SLj_rfSoFjlkZy6DBb93bl4lLA_C_lBmc4of5lms8qUbuwBRvYG_ty424qQuYshuirQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=ZmJX9HQcezHHmNieSUJZ_jMwvA5DAKHI-yDqmnfUWnz21JD80ky82-0a-c9Xvaw_IIHLxGgCx5KOq3MapoxqzTCVJiYGQHa-3stLstSGOPi4ARad71SNUkgsERR2603cUHiJHd1iizVqd1t72U_tyrMtVgOLVDPa324ohI47vCAdBy-vzp0ckrMhYsXOrZd1hPmClF8gJDciFFOTDoK22qixDLiF4VI8eIN2_ichhHWHygZiCz8BlCYMgcSgDl-XqqVz20waQgcNynnGom4SLj_rfSoFjlkZy6DBb93bl4lLA_C_lBmc4of5lms8qUbuwBRvYG_ty424qQuYshuirQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=FWLjhrcFNDD8pT6vuoWxygh-LwCxqd1AjhQuHEtKpq8FCUg0lWMI5abtc8ov-GHWqp24tKUQnWPmvEU0teRPv1NsyD5r7ucz8l0MGtw1uEH11n2JuoALz2SLb54k-JlkDhgigFER_c4zZPgsQDN6P9ggGz4e4fYcruDi37nPLZL8-KAqB1NeWr1-eh6ba88iyuLczv00HWwsm-yQYrIIOA8NIwJF_1BNwJ20JT29JjVcuxWax1Xl7HHjL88E6xCveVjKGGcCmLAevmowaTp8_FP1EGWC1RuFDQlx0fj8eX7Ze_SG65w9nkT-38ehhykxLZ1ABICZAz9latzF2Kcbtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=FWLjhrcFNDD8pT6vuoWxygh-LwCxqd1AjhQuHEtKpq8FCUg0lWMI5abtc8ov-GHWqp24tKUQnWPmvEU0teRPv1NsyD5r7ucz8l0MGtw1uEH11n2JuoALz2SLb54k-JlkDhgigFER_c4zZPgsQDN6P9ggGz4e4fYcruDi37nPLZL8-KAqB1NeWr1-eh6ba88iyuLczv00HWwsm-yQYrIIOA8NIwJF_1BNwJ20JT29JjVcuxWax1Xl7HHjL88E6xCveVjKGGcCmLAevmowaTp8_FP1EGWC1RuFDQlx0fj8eX7Ze_SG65w9nkT-38ehhykxLZ1ABICZAz9latzF2Kcbtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=Y38HGTnMBXEjQ4_ydJ4FTB9Pgk-yJMxL4sL4Q6tqpu81z2ZVEcHwfljGdjKoAuvbvs71wLAXpUijTfWCG6AavHh0imyh-y7_OQ78GA2JeErxI5PanvYy_dceAKveIRdG8XLfNb06zG284STomqtLIqW3AvCc16eAUnvmx5UHk9Q9FQ6UumJdQ367aUg9jWOy8Y-UxiF7Ri7dqjMxj5X6fkPaPw8zyzK99lt6EB-RZYxAr80lsO_kWqtgb4jTQSRhi8gT_BQYG3PY11uv7r_K2_CzWZ4WMzA2SGt59-Te27nICkTzAvx39cO1WxVCS9H2Zg6LoGHqaxXAaSeFYQQ4vlgtAy0qQm1_2BpQpjtI6N7EB7IUC97xvO60vA3ZvzfJOJ84j6qJUd9yPlkvSZ24XprDZWeWrz_b5HuMjsFeRCFO9cBFL1tWnM8Sfq6aD8MgPgeXQYJZaPEh5Hh50OMT7onn8unFaZ5sTeXRS451KXP7Qwi7pqKOkBwl9b0wsRd4_cd29zAq2MR-x0HQ08UIV7erC_vqkXBz5HIU17sh8T2evGxDvmHmUEoU_FOBp0yS8lufZMwZvrBVLjAvpMTkHIs4y8XOX2jFkbU9J66gT1WqueH3drjpCZwPcT6PMLqPd_kYJm-PulOOpjhvV_PxOISm684EBMfWydBrFhcagao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=Y38HGTnMBXEjQ4_ydJ4FTB9Pgk-yJMxL4sL4Q6tqpu81z2ZVEcHwfljGdjKoAuvbvs71wLAXpUijTfWCG6AavHh0imyh-y7_OQ78GA2JeErxI5PanvYy_dceAKveIRdG8XLfNb06zG284STomqtLIqW3AvCc16eAUnvmx5UHk9Q9FQ6UumJdQ367aUg9jWOy8Y-UxiF7Ri7dqjMxj5X6fkPaPw8zyzK99lt6EB-RZYxAr80lsO_kWqtgb4jTQSRhi8gT_BQYG3PY11uv7r_K2_CzWZ4WMzA2SGt59-Te27nICkTzAvx39cO1WxVCS9H2Zg6LoGHqaxXAaSeFYQQ4vlgtAy0qQm1_2BpQpjtI6N7EB7IUC97xvO60vA3ZvzfJOJ84j6qJUd9yPlkvSZ24XprDZWeWrz_b5HuMjsFeRCFO9cBFL1tWnM8Sfq6aD8MgPgeXQYJZaPEh5Hh50OMT7onn8unFaZ5sTeXRS451KXP7Qwi7pqKOkBwl9b0wsRd4_cd29zAq2MR-x0HQ08UIV7erC_vqkXBz5HIU17sh8T2evGxDvmHmUEoU_FOBp0yS8lufZMwZvrBVLjAvpMTkHIs4y8XOX2jFkbU9J66gT1WqueH3drjpCZwPcT6PMLqPd_kYJm-PulOOpjhvV_PxOISm684EBMfWydBrFhcagao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrEnnt2F1wC4cietwaxRBquI21HGjy42v5ED1EIfzPxxPRotitlDitIGbAuDV1q2r4wG9hwvU409gEtGhZHYcvWna0Ww9SRUpasP49zhwn4IdqD_h_dwW0mlP1doJfGDr2mXBttcbgmO8MvlNMekG5hYZu59C2XJrJFLUx_OVh3Ei3AzMQjFGNFgo3w8-NxC2nNvHKQ4qO_Vb7gTuntjzT6XR7UI7Pq_xqgxBvl8Z_qQzjvNLWQ9yFYzfNvwWZh85Dt98pUxo78oa81sD3oOuqrCvKbv8UGVNmSrgKw17bKlXzMTGSTu9cNGi_LhoWBz1Z-U7Ws7rAll22bKY_GCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=qLuA91DApcBbhIRMG_Ik65AK3MZvL8tplMOYWWsmftbvQ5H_AiznKcuLTDz8vBcthV6gliwwV9FxgdQicVfzkf0IlajA8bCG9uEv64_N0fnix09Te8I2i65H9tlNqVaWhHXyHpFerVgVVlGBxrz4vq-RyHh4cgQ5W3U6aanA1rIRNVj9bwDbI6LzFRj3HQTLI3-Cc4myWx-6afYIaWWGrYAr5bGx--kJRQ9InOy_LSbrjf3RJhk04i5PGibxR4FK4JHXOSDdN_yftWT_UKGG1C7YhOYdGXWQhzLMu5E4z-hvXUOFpQSbXYuZIoLYH5RsevUOb7wVjE_MIqz7U8Sr1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=qLuA91DApcBbhIRMG_Ik65AK3MZvL8tplMOYWWsmftbvQ5H_AiznKcuLTDz8vBcthV6gliwwV9FxgdQicVfzkf0IlajA8bCG9uEv64_N0fnix09Te8I2i65H9tlNqVaWhHXyHpFerVgVVlGBxrz4vq-RyHh4cgQ5W3U6aanA1rIRNVj9bwDbI6LzFRj3HQTLI3-Cc4myWx-6afYIaWWGrYAr5bGx--kJRQ9InOy_LSbrjf3RJhk04i5PGibxR4FK4JHXOSDdN_yftWT_UKGG1C7YhOYdGXWQhzLMu5E4z-hvXUOFpQSbXYuZIoLYH5RsevUOb7wVjE_MIqz7U8Sr1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=omI2fb5erSWEOCy5ezQkZibcp2rCXo5IRvR2d7rBKLUQzhXENllw7xlbztWgm-qe9YaGaH6U2NXXQamIb1d5UQLJVj3QLksMV_ciG_MoVDdQ10InCrJBZW-ZVnrOnHynUH5bt4Z5U6EEGvQ5Kr1keBc7da29HdeH0d0h3ahe8LTU_uDHSB2WPU5xZf761OppYsfJI2eKAka7PeJbl3Sa7p-aw-sZxH2XNPii3RXOEg0H-3w-pK3ukU8pBw_zrF-q_YSpBkIaGVZgl83gAd3pZ-VA9w94rz1XrazihcUeA0kOPnE4Bp0kuS8KskI9Wu7MruhpiP0emagtc4Q2xUkGwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=omI2fb5erSWEOCy5ezQkZibcp2rCXo5IRvR2d7rBKLUQzhXENllw7xlbztWgm-qe9YaGaH6U2NXXQamIb1d5UQLJVj3QLksMV_ciG_MoVDdQ10InCrJBZW-ZVnrOnHynUH5bt4Z5U6EEGvQ5Kr1keBc7da29HdeH0d0h3ahe8LTU_uDHSB2WPU5xZf761OppYsfJI2eKAka7PeJbl3Sa7p-aw-sZxH2XNPii3RXOEg0H-3w-pK3ukU8pBw_zrF-q_YSpBkIaGVZgl83gAd3pZ-VA9w94rz1XrazihcUeA0kOPnE4Bp0kuS8KskI9Wu7MruhpiP0emagtc4Q2xUkGwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=Y2lgHL8Il7792UYWAO691LnRJ7XfvnG3R3b91nmlg5t8ocG-sptC1o9EntXtDVz22yDfIDfcFKObCDrj_nHZJP9EKBNyHSxHCAUhrG3F6M-asgArgxon-4HJcldRDX9fQ8ipLMFcBYApTOL6aLI8umsQdsXYLEsZlRU3G3pRP_M8EO4oIPlCe9PXFm-u9m3NhXYGw7m9F6UFPwvIrzcM_i6PW7st7Zr_AG8nx9GQ0-tm-Q5j2WDMAXvZdxD7FC_mF5x6cYrbFdJvbncPe3o4Wro3sHlN1dGlKxJffAGB1tA7KuTVM00xaeIWKd3Vzl0QCvHeRhQi9yQ8iRZXmReWXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=Y2lgHL8Il7792UYWAO691LnRJ7XfvnG3R3b91nmlg5t8ocG-sptC1o9EntXtDVz22yDfIDfcFKObCDrj_nHZJP9EKBNyHSxHCAUhrG3F6M-asgArgxon-4HJcldRDX9fQ8ipLMFcBYApTOL6aLI8umsQdsXYLEsZlRU3G3pRP_M8EO4oIPlCe9PXFm-u9m3NhXYGw7m9F6UFPwvIrzcM_i6PW7st7Zr_AG8nx9GQ0-tm-Q5j2WDMAXvZdxD7FC_mF5x6cYrbFdJvbncPe3o4Wro3sHlN1dGlKxJffAGB1tA7KuTVM00xaeIWKd3Vzl0QCvHeRhQi9yQ8iRZXmReWXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5oPX8qRW52vxIo8WokgoEir_RHPfRnt7tIhnGVfa2J4d1gUpe4fy5833-f9_soQjrnkNED8OdWdBE5OgM3LcIEZPPhU_jji4bYfAVLtlChIlKT8DICnKzwzBbYKmt9qDbAyBby4-spoKSWZKcKxWbkQ_4HPocAcajIHg8v0-YW4SRt7zIclNpAgEnC9EXmIRL4GYsM4x5hBTF0_HZMRR-x4Oozm5yKdj6O47fMyLC5Ucqai0I_uzJZacF2SQHa33IxGFGICrI6gLMPW0MGJy1e3v6RtQGBR7OgGIdr-kQJCzsrKEGQ41Wk_kudx28ojmVWDNd9iIxIsexT7qEz3bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=Okc-XfO_hXHV-wPn79w1Q8z-gLmny2yKjU1uA8Cdh3ox73w0fpOGMvMQ1n0JDYu2Phwhic9a36Zl-nhypWzhkMfvytTqT4hnDyafIGSLIPJ0DngLy7a7ROxKXOWYWj4AbAHtZ2vppifkOpadVKKSpPf_EqaVhBmxhfK7VR8w63mYEW9LC7vJqcX9QTfWCDMI1mot7JCLp4qtao1WMeclR2R4IYbQ4vr8N2pJGZryIQR4nOXOOINz8AcEVqlfa5hYoDnICPgojmK0SsOowvHppTweKm9t3KdN9sFllhHmzIRHX6WimtXW_wLjfwo6LbV8yFQDWQZQKaSUOjLPglCLdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=Okc-XfO_hXHV-wPn79w1Q8z-gLmny2yKjU1uA8Cdh3ox73w0fpOGMvMQ1n0JDYu2Phwhic9a36Zl-nhypWzhkMfvytTqT4hnDyafIGSLIPJ0DngLy7a7ROxKXOWYWj4AbAHtZ2vppifkOpadVKKSpPf_EqaVhBmxhfK7VR8w63mYEW9LC7vJqcX9QTfWCDMI1mot7JCLp4qtao1WMeclR2R4IYbQ4vr8N2pJGZryIQR4nOXOOINz8AcEVqlfa5hYoDnICPgojmK0SsOowvHppTweKm9t3KdN9sFllhHmzIRHX6WimtXW_wLjfwo6LbV8yFQDWQZQKaSUOjLPglCLdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=v93FeOvMXmj9mccu9JhwqOH3uUqjL-RTyOXN49m8sK6yLNP-uwTZad1-LBQnFq5hhGDXZP0iecfaN04yIhTelziItonumoHwYF94k3CE5p6TS_3a8wLhzTNKSp8KDG98rOY9gG1oyMWy57ueCBNxgceqpEefym8e9v2fbc0MD3EhpZ3LPz8YzBTtQofbZXfu835xmnTp73vAjxomjGQjkzar4m6uhGDdxFPb85GnPRnJzGV2KlEuenY_YiANNNhdqdi4_gZ9A8Wr-7EKZ2uRiKyKJr4o4HkUGFxG-0gQN18Wz2G8j4saxNTsle_yMkX45gW_eenHNASnt_WueqH7sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=v93FeOvMXmj9mccu9JhwqOH3uUqjL-RTyOXN49m8sK6yLNP-uwTZad1-LBQnFq5hhGDXZP0iecfaN04yIhTelziItonumoHwYF94k3CE5p6TS_3a8wLhzTNKSp8KDG98rOY9gG1oyMWy57ueCBNxgceqpEefym8e9v2fbc0MD3EhpZ3LPz8YzBTtQofbZXfu835xmnTp73vAjxomjGQjkzar4m6uhGDdxFPb85GnPRnJzGV2KlEuenY_YiANNNhdqdi4_gZ9A8Wr-7EKZ2uRiKyKJr4o4HkUGFxG-0gQN18Wz2G8j4saxNTsle_yMkX45gW_eenHNASnt_WueqH7sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=dzYqnqWLquYwfjx3O5pj_C2j32F6AtFTVMT8zYw-FrgDPACo6AMOTCjSiTk3fga_PhslMbdF2esAsywxBFCv_5trxY-PowTB_Xspi6XDLARXSVV37y4hHEW9Irmk6cRx8vUUZvPxrn6H9ntlnVnH_2IAQN2UgXygpQNPQxYB7dL7cpS0VnSRZRf9klQIJdwMiu_UOZ4wariSxvqM7wIfPMNKRp_bwDNX0KFF--UBIO3pD4gcRjwFyzknym7xuHskNLLRIxxHL8LwPqv-orBl5_kieWQG_TMrAF4DxwjLurGfuJ8pSK5YKK8f0LpOy3ebNlUQ1QTNt1bSfEAocsVUxThMtXDkbsNf2obvmqpU3T3ZQ0sjdd8ZzN718b-XWRaitAbk-GUMYx1q1zOz6CVS6m3liwjnJdPB_zcDGHcILTltsTdpUkgNtgOmrQgoS1bG4SBZqhcI7LENcsvGanH1FaYUJ9sBirNNU52rc5xUmf0tW8bx6lS3SgUVKNIMyuL67B00UovyzC0iYMv8aB8S89K5UZJahDQeWWyUtBC_aO65jclaHSh7OXtJH09ssLANo_gqCUwh_ZvKKpWnrkuS3uucRPaEGxbUFROA--T-k3kV_gOPwyt5et5VoG-VOpNjsRng-4khdZngs1Kre6DHldmcv5mUyK56nQUHqo1DIZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=dzYqnqWLquYwfjx3O5pj_C2j32F6AtFTVMT8zYw-FrgDPACo6AMOTCjSiTk3fga_PhslMbdF2esAsywxBFCv_5trxY-PowTB_Xspi6XDLARXSVV37y4hHEW9Irmk6cRx8vUUZvPxrn6H9ntlnVnH_2IAQN2UgXygpQNPQxYB7dL7cpS0VnSRZRf9klQIJdwMiu_UOZ4wariSxvqM7wIfPMNKRp_bwDNX0KFF--UBIO3pD4gcRjwFyzknym7xuHskNLLRIxxHL8LwPqv-orBl5_kieWQG_TMrAF4DxwjLurGfuJ8pSK5YKK8f0LpOy3ebNlUQ1QTNt1bSfEAocsVUxThMtXDkbsNf2obvmqpU3T3ZQ0sjdd8ZzN718b-XWRaitAbk-GUMYx1q1zOz6CVS6m3liwjnJdPB_zcDGHcILTltsTdpUkgNtgOmrQgoS1bG4SBZqhcI7LENcsvGanH1FaYUJ9sBirNNU52rc5xUmf0tW8bx6lS3SgUVKNIMyuL67B00UovyzC0iYMv8aB8S89K5UZJahDQeWWyUtBC_aO65jclaHSh7OXtJH09ssLANo_gqCUwh_ZvKKpWnrkuS3uucRPaEGxbUFROA--T-k3kV_gOPwyt5et5VoG-VOpNjsRng-4khdZngs1Kre6DHldmcv5mUyK56nQUHqo1DIZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=enjVW8E906SCyNT3lMpNsaTrIDGZHKsIoNAXb-xmY8l_NrL29g_Ss2NYBHrPumRoP90zupxgnuPb4xOHTbPrC9QVUlstx2wwvbh6oTrVKlzYiNy9AEvQnnmKV76Undk7mWionnBdMCB0RFNeU_gxbmHiCYGd2IEkxukO-Bg3LpXNR67l-N5dHR6XHrtL4GzARxqeAOKKr6x3dryN_YhuzZEu1BMiLo8492V1ckRX6KeBGqxFVTJTbhK8HNBQt04qyfx6VIqbiZukRyF8pYRukpd6uleZxLBn6t8TtO2fuyB_CdDvZUerLgU68UytjyvmBklrzgOw62ICWwpz5d3IgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=enjVW8E906SCyNT3lMpNsaTrIDGZHKsIoNAXb-xmY8l_NrL29g_Ss2NYBHrPumRoP90zupxgnuPb4xOHTbPrC9QVUlstx2wwvbh6oTrVKlzYiNy9AEvQnnmKV76Undk7mWionnBdMCB0RFNeU_gxbmHiCYGd2IEkxukO-Bg3LpXNR67l-N5dHR6XHrtL4GzARxqeAOKKr6x3dryN_YhuzZEu1BMiLo8492V1ckRX6KeBGqxFVTJTbhK8HNBQt04qyfx6VIqbiZukRyF8pYRukpd6uleZxLBn6t8TtO2fuyB_CdDvZUerLgU68UytjyvmBklrzgOw62ICWwpz5d3IgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUo8Ig4yNgAuRvI0d60j7cdhgYtKBG6LRwVF68jBWqI8-d5ImpdtxIA0Qd9GtHiN2UkGfJQORjHkVv0GdiXFaiVzaAWAJq96G6XP7tNMT0mMmDehEcEamyrq3LhqKKuKct8c9VT-f5iSG1J-SBjkpfU9rqoZEIyINxomPvx1DSrF96XkVCmqzIAFef8wwBp3VZlfNXUw2C0qY3kr1XH3NWKs2_-o2t2hQGkbeS88w9W-VSYYDMSRzO27uKvTWJplGaKCPyiljDCld7BNj1vyGtUIhUUIXfJ7enA94x225x6HixzBZWQlF9Nf-4KAyiOcZQ6QL8gED-ToRjoKE7OC6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=D8gjaDrPG1VZgzouz9mn_iXKQZ6fyHyBX-_p6ODoF9osg7KBk5P6INP4OhI7NWT4gTYq4qj7MYXgLhg4SSHeeiKOavLYEjrFfPDxbB7FEE60jJCit_r-oDjQuh-odeGu1F1m2uN688p-e0igNIrZp_Nr9TmBoSXovdAf8MRntauMN_r16V0mxGnCHKCG4Zzg6O6G5sLtGQ9_TJYArfmToG02T0yAPypygA5btjXG-nDJcTE4dfA2PhUoUvudDVEDF-ct3LogVR_-OnVG3nmWqNXkuHii2TLOPS-J58zH9jqy0W2hHqnGh5IlCz3dH643Zp-uPKb5nKOZv603bWqglg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=D8gjaDrPG1VZgzouz9mn_iXKQZ6fyHyBX-_p6ODoF9osg7KBk5P6INP4OhI7NWT4gTYq4qj7MYXgLhg4SSHeeiKOavLYEjrFfPDxbB7FEE60jJCit_r-oDjQuh-odeGu1F1m2uN688p-e0igNIrZp_Nr9TmBoSXovdAf8MRntauMN_r16V0mxGnCHKCG4Zzg6O6G5sLtGQ9_TJYArfmToG02T0yAPypygA5btjXG-nDJcTE4dfA2PhUoUvudDVEDF-ct3LogVR_-OnVG3nmWqNXkuHii2TLOPS-J58zH9jqy0W2hHqnGh5IlCz3dH643Zp-uPKb5nKOZv603bWqglg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=JaN7GIW7qx-IGhS3e-9xuceNr_KnVE3l1QqVqgogBZUGovZiFZka5xDzoqAcnPDmB5z1Pnh4Y1ui9Z3TY7wtLQmp9t6yyBZ2_qml8NZXKj6dyw2aoPkP8jdEW_g64J1VGsgMrTC8zbfG-NdUwkWp2UdchGjqz0Y7rT_B1VfBJgW3ChX-lSszlMbPlbwoKDMEukOpNeNgRAS-tt9yc5rvd6ROCnV4Altz_heEDNiMt5HElfjIyFSQ0MYeFF1LfgS4rKGTbcjZzCSpKzEgwIjyhFlwto6BrqmWjuO1vAhUT47MOZ68AyZ-c82Fd6n5gcuo9q4dbx-Ny2ncatOE33bpag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=JaN7GIW7qx-IGhS3e-9xuceNr_KnVE3l1QqVqgogBZUGovZiFZka5xDzoqAcnPDmB5z1Pnh4Y1ui9Z3TY7wtLQmp9t6yyBZ2_qml8NZXKj6dyw2aoPkP8jdEW_g64J1VGsgMrTC8zbfG-NdUwkWp2UdchGjqz0Y7rT_B1VfBJgW3ChX-lSszlMbPlbwoKDMEukOpNeNgRAS-tt9yc5rvd6ROCnV4Altz_heEDNiMt5HElfjIyFSQ0MYeFF1LfgS4rKGTbcjZzCSpKzEgwIjyhFlwto6BrqmWjuO1vAhUT47MOZ68AyZ-c82Fd6n5gcuo9q4dbx-Ny2ncatOE33bpag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=jRY2VcycFClERIop9DvHWLedfUZ9feuGdQ6BQaI-KnGhPs2IiLxnd7BL4BI4hlAwHOO8osiSA1xWuO8JZvHh9-32tokMoKbbQJtriim2d-UF52CjyVYBShr8MeMoeBoiZecSwonTYXEcdNa6ozLb7f9MZ6aTUmE4ERkEO0KwjH-75gBmSncOYQVTGTTTPIdmBR3bsPj3e-HqrzNqmRxyfZYmhwTASAd2OpwLHMq_JdCLXk7g5buJwQ6qzSL77ZAtAzCWIsvpPVyQWnKu4sOULciuk03z1ARrfWSRP_RvOVqgkus4DLCcdLFT4tPik2PmPmcN3a1_jYso0vUZs1Wb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=jRY2VcycFClERIop9DvHWLedfUZ9feuGdQ6BQaI-KnGhPs2IiLxnd7BL4BI4hlAwHOO8osiSA1xWuO8JZvHh9-32tokMoKbbQJtriim2d-UF52CjyVYBShr8MeMoeBoiZecSwonTYXEcdNa6ozLb7f9MZ6aTUmE4ERkEO0KwjH-75gBmSncOYQVTGTTTPIdmBR3bsPj3e-HqrzNqmRxyfZYmhwTASAd2OpwLHMq_JdCLXk7g5buJwQ6qzSL77ZAtAzCWIsvpPVyQWnKu4sOULciuk03z1ARrfWSRP_RvOVqgkus4DLCcdLFT4tPik2PmPmcN3a1_jYso0vUZs1Wb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBdJB1zc0uKqZh6xRHiKRZrh--Mu3I-wOZmp6YRYfvZwE816AQLmiw_r491nvCHE1Lfk_eZc5o_Q5bJHPWbQNU18nSa3tajCPpomtnCxYkElxS2jDwsPmWKr6JHc7TtMc8urdG3Iur8mqnngo8vNbf8GMxzlHzC3miYzR6nF-DBaSeaBfWHuJXrmZ0aG8_aFbWArTS5lPsfXzfidAP9_RDpXWQEXEQU2CCYujJ8PDktV7lcj0ZCMZ3ytVUZ92twcndLDP8L5DEwWXEu0sLkAqm4ej1_wj4n8or_7Iuzx1_FYVoly_MXq36hnHPYS9DtCOyidajxHZ7lSvHrCY_0xoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=b7PDg0q3jMhvwxaIKdXgmrwPcHKe3ZsYIES8yZWNEr9Zi5DmWtZNMDCsybchSsoZW487d_ap-6idkRjLgCI9tnkSsOe2juDReo1KVgXGEHXISbrLvbVeXLRMLVavwU_AKlclpsJx8VLwaOfqECWyrhRJCXHLC3R2od-VrTPqrEyWoST75jld_1rHhRiaonYJdVTpMvGqVkLCwCfHyn8dCHbSD1QdiYuxJcZsjO4_iYHC2Gkn1nJfJvz_Ft02F0VRcnhmB4c3VhWjhv7zED7gVtjRPpd8WqL1hi3J_MY8jsMNDMZy1CTR1vbBsiboJIJFBRgdo8MIvGgfxPmzn6XLbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=b7PDg0q3jMhvwxaIKdXgmrwPcHKe3ZsYIES8yZWNEr9Zi5DmWtZNMDCsybchSsoZW487d_ap-6idkRjLgCI9tnkSsOe2juDReo1KVgXGEHXISbrLvbVeXLRMLVavwU_AKlclpsJx8VLwaOfqECWyrhRJCXHLC3R2od-VrTPqrEyWoST75jld_1rHhRiaonYJdVTpMvGqVkLCwCfHyn8dCHbSD1QdiYuxJcZsjO4_iYHC2Gkn1nJfJvz_Ft02F0VRcnhmB4c3VhWjhv7zED7gVtjRPpd8WqL1hi3J_MY8jsMNDMZy1CTR1vbBsiboJIJFBRgdo8MIvGgfxPmzn6XLbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=nEtmyQNarKIJID-dtz3zFZ7Ji4QtHHkmXggtK8LmO3jBMfQQfqO7PS-XxrNhDCm97klJpcSInaB7rVwV_L-Ez2tonRT-LwoHzo_tD0m6wElWwoi0oOuI5jpLSXwyNImOlHD4qHy6UAbUDN6H4jicQ5cAm4jk0ESJWtx6oh1sNIBrIJx7BLqrH5fe70PgUzyE-tdYniIizEMwglFQ2qXaqnG3odENB5xbTHdfuWdZQfbPLyECRyqACrPJUPTHiALgERj39Pj6zY0D58SOQGwnp6qIUG4OrilrBerXHxivZSlCzf4BvO9c5_yf3AsykAM1BGbI6C7Zf42ylBTJZPPscA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=nEtmyQNarKIJID-dtz3zFZ7Ji4QtHHkmXggtK8LmO3jBMfQQfqO7PS-XxrNhDCm97klJpcSInaB7rVwV_L-Ez2tonRT-LwoHzo_tD0m6wElWwoi0oOuI5jpLSXwyNImOlHD4qHy6UAbUDN6H4jicQ5cAm4jk0ESJWtx6oh1sNIBrIJx7BLqrH5fe70PgUzyE-tdYniIizEMwglFQ2qXaqnG3odENB5xbTHdfuWdZQfbPLyECRyqACrPJUPTHiALgERj39Pj6zY0D58SOQGwnp6qIUG4OrilrBerXHxivZSlCzf4BvO9c5_yf3AsykAM1BGbI6C7Zf42ylBTJZPPscA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=EzBgg1-cyGLoKEM0eGaTgH66P0eboAzBgjlVioQ-cmiA-Q9EyAgTfuhyWyOk4iEaorqEhXiara5wS0yGKZzFQ60CV9w4NZFkSE3eY9d7_9SDrWMFu3j3GK51iidlwH-CaUdomnsGReCmPQ_-6Tnhgl5U6ojQhjyGqjQiizpMf4dgHGw7u4olNiJX2mxPwp6gEvrpW1EvJ9BtvPrqkRkk2wlMXsJU15y1838AZ7KLdS7ZZJCwUXqfuV8iJHporgEezvtuXqHVcm29Vc8vg0G1_BT1dWn0FeToTgxkoGV5zsQNW9UuLkFErzgfn-GoSFL0Fxp2kKffNsut-0kcnXLNxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=EzBgg1-cyGLoKEM0eGaTgH66P0eboAzBgjlVioQ-cmiA-Q9EyAgTfuhyWyOk4iEaorqEhXiara5wS0yGKZzFQ60CV9w4NZFkSE3eY9d7_9SDrWMFu3j3GK51iidlwH-CaUdomnsGReCmPQ_-6Tnhgl5U6ojQhjyGqjQiizpMf4dgHGw7u4olNiJX2mxPwp6gEvrpW1EvJ9BtvPrqkRkk2wlMXsJU15y1838AZ7KLdS7ZZJCwUXqfuV8iJHporgEezvtuXqHVcm29Vc8vg0G1_BT1dWn0FeToTgxkoGV5zsQNW9UuLkFErzgfn-GoSFL0Fxp2kKffNsut-0kcnXLNxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=Ki6LnLzVnl0JiwdlbWX3e_UwcjAN72gOHmFiFH-gJ8P2Tl3mgKFdzdt4IRqiJcfoz3wtTFMQG_8PBdaw39422kUs4x7CEObcxtg7C8svLT8cdt50MAO1JHWjiU9ADnWfyniMdZyHd0WG7UGPSLHDKXxqNEWPdS-sMr38762WaZ9XFvd215Q90sAhoj9y2pH_UsIUdJP5hyQpAAsY3gfNZFlnNiEMp37Yd6hOkhMEaoXfcyUboq4puLaaKZVlkMwAIoKJtqBrMAi-PEcuPkKSs-PTMHYqu1dZjKl-SrddpnhvTnlS6TlwjahRSUMNB1tIOLpmkFCLwd0Cp-K0liYnLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=Ki6LnLzVnl0JiwdlbWX3e_UwcjAN72gOHmFiFH-gJ8P2Tl3mgKFdzdt4IRqiJcfoz3wtTFMQG_8PBdaw39422kUs4x7CEObcxtg7C8svLT8cdt50MAO1JHWjiU9ADnWfyniMdZyHd0WG7UGPSLHDKXxqNEWPdS-sMr38762WaZ9XFvd215Q90sAhoj9y2pH_UsIUdJP5hyQpAAsY3gfNZFlnNiEMp37Yd6hOkhMEaoXfcyUboq4puLaaKZVlkMwAIoKJtqBrMAi-PEcuPkKSs-PTMHYqu1dZjKl-SrddpnhvTnlS6TlwjahRSUMNB1tIOLpmkFCLwd0Cp-K0liYnLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjNnufs3Mtn4xoJzI2hSr5FZfgPcxPmUj4CwrWZgn1b66pV_v3bOnSS7UxvnUml6Fy0_vO-2py8Yg-M7kgz1G9E05vxV5sYe8YU1taaYq5cmu0hINFpnEeqvAVfg7aPXfK-DAt5A_84SvphBw5WIGgFYoycHEB1y63sFJv-zB-tPYs0799pe5qDy5xTlo3tkf1A1i7RhZAJ5yr_ZQtzFRBDG7Rp0KJVkTQ5C9DD3reB1Rg3sz8V_qhFUWPhBIpJOuCaSiyxGa8rgcGaM1GDxmqsUio8-JfN5Jkl5vsLvWZibaeJTcBjTZoBZjLXr0SmPR9__5l920z2RRNBeBJkXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVQ4etcE6tc3i_Gx5hPTWEgvN76Tg_NO5_370xSahStDo7xRB7pFHywX4jgVJZQXMTFgEsOQcJAhYSNGyCoSiKALVhiZmzkoil4e36pb6ovQj3IT5PjAxszH7AlHHVrSvUWKGeE15wWqF_v8LIku0a41CFvyVWQ9FXysc82ufCuavBB63rzhqoPq0NN0xRyyMTHLaq2cXOEKTzlTOHpveOc_hF9MKa4UGp0I6QkDwWE_606lj0M3p933mM65RDa1I0VTqQ5_sg-IgGqLS8i0bQcQyAEDpCUkYE7hNd4gnEeQ1-qEDFXMHX1TjviS8Fmaon2mJfLc2iesI4CpHmeZEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCD5x7JifwCwaK8OSYVkFzVG4H946lHYStoY6fY57PQYRab0f-h-_8Vd3MazmnCmK5SjMRPBYwfDLjejdBKguhtUNkMcLYPSuSnsiGSBYX5kSEmSpoQVk4urM2B8CMFROgJdUKg6RgMeFZLYKcX9dISauit0PeVcILUN3EkpwX5Rnm3m_EBYL_IS_tYNPw7Mueh-apHzJIZwSX3hoEiudV_c33LTjha54VpSAYmkxcDdAbx5r3YGH3XNNmI5-1A9nKxHhxMYGQka6iu_WQJ4hXVJoF_gQ7G6HlNS1eQycaa9qlx2fSnrhmUaBlSO0p1esjUB2RjHacFuisOaqZj6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpFJTizUEXflcO7xz5_WYW1z6HMu3X_wIHWjiAwqryYy7JFkPIx2kV4ro2J78Cffu7G9XIERXN5uJp5Yd38-MMr7r6Ro20CL5tX7U_RyueB6AsGF7p4eERav6Dju2HjXSDl2nCibsm1XLz0tbciOyhoTb9SX7vfkFp71EKxLL3QuGxksKAkgMbslYt5PI91vMqKylGoiGqwFUfhZLHXc7_364nVZoOlEY7rHZEETXQ6lDygHb_giI_oySe7jEc-rh-fHlf-apXPqxgUAN4WMWOsLWeDZqlY1uXCNa1W9fCBUCODg9MqxSVOTLh9oTdle_awtXY32-TxUoqAHweGbcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBIbyBsSmP_M618XS2_kyQVEscWqCfpnkg3f7Fbjs6cEYbnA0xezAuvtf52WqxBIZaKv6g3NLVH8V3K2UzE6CSmi9phanItzfdhAT820-ywpp98d0KhCFdp_IWryeV0tNHyrTf_yw9Ch8uB1YVN7FvaIIx_ASBbUDD0c37uBztEidFvJl-bUCprFzltLy7GydAJeuqd6l1jOcuCgEW-mKK0VSnstlW4AjRxaKm7Nyy8qTFfr-lOGqpTMtiTGc-BtI5Flw_W1ScyPDwuwaJS7HDWCEXhi5vcVtwKeFYyWFZyExmp4GdagjJst9xqLThY7VIocdSREKen8wqWExJVhag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=BQ_EU053MRHjLInNauyH43HCKBBlK3Uw2QSX4yO8QA6_uMfKtb7OX4f4QbNH4Mgi0jtjq_q7KGxxvome99IPKAFyabCwHDafidyZZrtVkDOYPNtttrCvxVWuYNyfu3SYeuELNWH1I-MZFmPs7bbY69QBEYOQ8hw3GJOMQrNmbUKqui6oQoLA-k5gbdi7_sgyk9cFaVpTbBCl1Nybu9OVUBCA9o-Z5h9aMoylQchxHsKH4rtu_WwkrwKWeoKHPwm_3Jyy48BGHvdiHoElIQK1Cm3PPKfiVsYO_ll1q45vD55lTPMH7nSSnjjwixylA0HPKOZjciSfjpX6-Tf43xqJCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=BQ_EU053MRHjLInNauyH43HCKBBlK3Uw2QSX4yO8QA6_uMfKtb7OX4f4QbNH4Mgi0jtjq_q7KGxxvome99IPKAFyabCwHDafidyZZrtVkDOYPNtttrCvxVWuYNyfu3SYeuELNWH1I-MZFmPs7bbY69QBEYOQ8hw3GJOMQrNmbUKqui6oQoLA-k5gbdi7_sgyk9cFaVpTbBCl1Nybu9OVUBCA9o-Z5h9aMoylQchxHsKH4rtu_WwkrwKWeoKHPwm_3Jyy48BGHvdiHoElIQK1Cm3PPKfiVsYO_ll1q45vD55lTPMH7nSSnjjwixylA0HPKOZjciSfjpX6-Tf43xqJCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6xvNBkPzja2JWU0ebw47R2PSX9R-VO2-POCQByWnmYS73nRWlSr2YcRRM5JKhBWajIDpI50IHNM3pEWiMdJMu0_fNDRvrm8-n9T4R87QEuNupdWAlPeWeXeyMZmA2c7GqxUTUlingBNUQUgu8hHAICS1aZBLV74irK4-cDjdH2FQcKvQUOEE0in3vUosJlXinPni0X5XDZyMfYVetc9MTEhU9igQzUu4EmPGXWOfdflFXe8UQFvTYaa3lc_nst5BunXuuG3SUBfqC8yn15q7eq0Y2tng7AWk35sTtZ4Es8zY5e_J8bDsOgtKsGFWfmSCKITLgWbXDT7cieIBf4jyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTtwnrEzss3cb8H2GKDaTRyhYMLJTv-efsPk6WqP0lzwcqZTZ27UJlV1CvGqk91Dp5ylSfs0JHn1ERnpiHkhIILDW2IzM86eVHOnenKl4jZtBGhokmxlBqzu4oT-G5Q_Ud7HbA1yY2K0lu4-FcELeXbD0PkfUDMMZdo09b49UsR4p54FtYYAAWwyQPcKB1NEO8-sVEoxsPqcSi6li7zDo1q3SosvEAJpkVs46EuV2FyR00u3u6YDIDauuDMYaKoZuWuJYKSonIq1CZgGHUbzK29Zaag9_FbWLiJkEUhXlbA6Q8erxOwuMrRwGvAN7-JrOhwaRz5ESY1ry8Zj6TOu_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=mHpK5_366nrIf8O2lJfjsLsbPAVIPSjQULReUEXR8wN15nio7aFTFhBKJEbBd-bviEmO7sVd3c9WBUnzT_YluGItt4NCDjW6rRQ2oo98rfuB6sxSzmjRYXfB-Kve9T7r96T44ATEnjAgmeRx9MZj1ahRnugVrZRpraSCfYxjHZwquVHCBdnRSsH3_kxsrk1bi80p-D0yABCAyHocCdaQ89PC37kDPo3-FM_AKQe1N3_Ytone8puT6Bbw-PZXhfoMt3mdtgo00cEcHhtQoxDoZRtuRSzbYjS0QUXpzEfMYPLyWQurIdbsimz-mvvjl2h454zLluBnsYOnTbqSucOr2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=mHpK5_366nrIf8O2lJfjsLsbPAVIPSjQULReUEXR8wN15nio7aFTFhBKJEbBd-bviEmO7sVd3c9WBUnzT_YluGItt4NCDjW6rRQ2oo98rfuB6sxSzmjRYXfB-Kve9T7r96T44ATEnjAgmeRx9MZj1ahRnugVrZRpraSCfYxjHZwquVHCBdnRSsH3_kxsrk1bi80p-D0yABCAyHocCdaQ89PC37kDPo3-FM_AKQe1N3_Ytone8puT6Bbw-PZXhfoMt3mdtgo00cEcHhtQoxDoZRtuRSzbYjS0QUXpzEfMYPLyWQurIdbsimz-mvvjl2h454zLluBnsYOnTbqSucOr2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=TG5x4ubM2TBjEy63aYyzO2_G2fcF_hT0jXv0tx0HC3w-1GMDKs6IAgGlywdsNknhhh6L645of0M0RXdTR6QFK95iGDxPJ4u2nQmbxBPoMsi_vPp2boCk_O3LGhi8tGncIX9Sj9-GUwKFMFzAjixuKGHIA-0Bbyq2vyCvy-g7G_08jEFQ45cIfS4aKRI25pFYKhUqHjaxLVSTJvP49Y1TwK4-MgNgajg8eQlbJku4Qa-FyJxQc_Js0jkAsiaX1pDbHPIRilMmgTZunJ-fRYKQ07EhjQi3RoXGCgQubtEBibENObxsQDRnPjgWgVFSsZ57hClz4mrOei5e4cY5Ahk45A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=TG5x4ubM2TBjEy63aYyzO2_G2fcF_hT0jXv0tx0HC3w-1GMDKs6IAgGlywdsNknhhh6L645of0M0RXdTR6QFK95iGDxPJ4u2nQmbxBPoMsi_vPp2boCk_O3LGhi8tGncIX9Sj9-GUwKFMFzAjixuKGHIA-0Bbyq2vyCvy-g7G_08jEFQ45cIfS4aKRI25pFYKhUqHjaxLVSTJvP49Y1TwK4-MgNgajg8eQlbJku4Qa-FyJxQc_Js0jkAsiaX1pDbHPIRilMmgTZunJ-fRYKQ07EhjQi3RoXGCgQubtEBibENObxsQDRnPjgWgVFSsZ57hClz4mrOei5e4cY5Ahk45A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
