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
<img src="https://cdn4.telesco.pe/file/ngeaSjEY-Bk6lkVQrM2DNVsS2TFr68xIjm-N_h19ntFQSn_JI8um0gSyj-Jqk81FnpG0uZ5EPEkuX63CpgE5nVjVWUBUMHLvDCNFhzmWtzX8RVVMCAUaEV4hJkbR0PODEu9axZ-Cu4XFiF2UQFVIvnsFkoOkduRpame_MM4yJZ_CuWWAMkMNsz09MhavSOab4434WFPtUzSvJ5OxleDfR55qJa8ril9AlIoblo1sGywD1hkxPH1ZifQP53m5aFmPnmhJJuBxl9bzvugJj00Lo6EKjFF3yD5CuETAqBkdNlwZDxKW_f57ZiniybA29AnTGpVFYh7ovIR3fbpkhPERFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 21:25:13</div>
<hr>

<div class="tg-post" id="msg-452759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np_yh6oM6oGLxALhdktBLbFZX3PVXy_3iMnp9KAMXskMsZjtpFcBy_7KPlw8MZkc1N3IOSARVXumtrgQip2oUZkk-8Z6OWbaaAgDOWYey5jtGMU_uvFapuHmMXtEDYXDBZjnT6VhY6A76e3ggY9Sx7fY12ETF4sWKm8JsywofyuK97Rp7ESmUggaCLkh0NaULbkcHuX99HVRerubOzX7B0ZQmZBdWRjC2I4ojLoo14wzn8DvIoYaQbW_y5pSz8-zvCs2Lz78wi2hK7kTympjgZYgeMWCc1k19AEjzsQRmDpQjxWpxSjJIcqLAtq0uteGxg8Df-OZdKScfNECXdY_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وکیل پژمان جمشیدی: موکلم از اتهام تجاوز تبرئه شد
🔹
وکیل جمشیدی در گفت‌وگو با فارس: رای نهایی در پروندۀ پژمان جمشیدی اعلام شده و او از اتهام تجاوز به عنف و اتهام زنا تبرئه شده است.
🔹
جمشیدی تنها در خصوص اتهام رابطه نامشروع (رابطه غیرزنا) به تحمل ۹۹ ضربه شلاق محکوم شده است.
🔹
به این حکم هم اعتراض خواهیم کرد زیرا معتقدیم در صورت احراز چنین اتهامی، مطابق قانون باید درباره هر ۲ طرف رابطه حکم صادر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/452759" target="_blank">📅 21:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452758">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6ce6e816.mp4?token=g9T4LWELTSN0T27bcDDPKD7mxWxbtfDqyHFXbjGp0iQTDAlrwEcz_Lc8cwGYt5RGQn4YOGGEESht1y949P2AK7Z_l8i-ZQA7r2TKEAuSE0jZzYo6XjUKabgAFVlTOwl28Gycnc3xmlkyajpucSFVFg7B3AdKW9llWKPL70mit5DuOdeaCKBFuWbkt9WuIzMH3NAAaQsUukZMiaokLvqUuYVcI87BmOlt6Q6-EapAR32TggL5myEMreh-WdFIAyUHBltNi6TOvU80BUPrnBSXPSlIszwcxM9ACuHznCkU9qydhmXrsVfJjiZ4FibCy4tJTYDYXeFVK39Qk63zgc1wLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6ce6e816.mp4?token=g9T4LWELTSN0T27bcDDPKD7mxWxbtfDqyHFXbjGp0iQTDAlrwEcz_Lc8cwGYt5RGQn4YOGGEESht1y949P2AK7Z_l8i-ZQA7r2TKEAuSE0jZzYo6XjUKabgAFVlTOwl28Gycnc3xmlkyajpucSFVFg7B3AdKW9llWKPL70mit5DuOdeaCKBFuWbkt9WuIzMH3NAAaQsUukZMiaokLvqUuYVcI87BmOlt6Q6-EapAR32TggL5myEMreh-WdFIAyUHBltNi6TOvU80BUPrnBSXPSlIszwcxM9ACuHznCkU9qydhmXrsVfJjiZ4FibCy4tJTYDYXeFVK39Qk63zgc1wLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
رواق دارالذکر به‌روی زائران آغوش گشود
@Farsna</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/452758" target="_blank">📅 21:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452757">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB1qZMW8kSi1Pjvbau6URFHGodFEwLPHtl9slNgjpHLKQZTLSf7-brZnGZwHR_khhw3fzpfrbLqbKqfLVa-FcsYUiXLSWPV7fckwt3JeLL0lPi4zUJYfuA8KjeYD7UqGlepW863qEhXUTzp2z2S-AHIGI6I79LY7vjSNJWIv7t2WCQBram54ob5SDDkf6H-c9IAooUGNuJB5vGWyBDaFigjeVc5dWzpbVEC1eF1Oj0Lwx4K6l8SqDRThYZf5UJJrSvaX5S82yCVd3k1cRHRQEE9j5J7LI3LrjKF6d1bhBhz_actb2siDQ7xizBKZ4Hly-uel1TqCtcvtG8I-pG3LLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
لطفا عدم واریز وجه کالابرگ برای کسبه را پیگیری کنید. خیلی از فروشگاه‌ها کالابرگ را غیرفعال کردند، ما هم به زور ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/452757" target="_blank">📅 21:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452755">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سپاه: عملیات مرصاد درس بزرگی به خائنین داد که هوس هرگونه تجاوز را از سر بیرون کنند
🔹
سپاه پاسداران در بیانیه‌ای به مناسبت سالروز عملیات مرصاد: در پنجم مرداد سال ۱۳۶۷، ملت ایران با تارومار کردن منافقین فریب‌خورده، درس بزرگی به خائنین به ملت و میهن اسلامی داد که تا همیشه هوس هرگونه تجاوز را از سر بیرون کنند.
🔹
منافقین همواره به‌عنوان پیاده نظام و ستون پنجم دشمنان ایران و ایرانی عمل کرده و از هیچ خیانتی فروگزار نکرده و در فتنه‌های کور سال‌های اخیر از جمله کودتای نافرجام ۱۸ و ۱۹ دی ماه ۱۴۰۴ نقش موثر و پر رنگی داشته است.
🔹
در  شرایط کنونی دشمنان انقلاب تمامی ظرفیت‌های خود را برای تسلیم ملت ایران ازجمله این گروهک جنایت پیشه را به میدان آورده است.
🔹
بی تردید هوشیاری، هوشمندی و بصیرت مردم مبعوث شده در حفظ وحدت و یکپارچگی ملی، اقتدار و صلابت کشور را حفظ و پروژه خدعه و نیرنگ جبهه نفاق و معاند را ابتر خواهد گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/452755" target="_blank">📅 20:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452754">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRvecIXOYPtGKjBWRcI6dax-NyKHPEPomM4Tt6QKNTYAsQ8DT9RKOCX8ot7agaestIVC_g_4lcoIA7lXwU8GVGS9x98yGtnNSKzQJJjMWL3vmzq4Jxo8ui0uJHc4qOj2HNyBbPI_lJFjLyE8UzEwx3Q5CY7ng0jSu27_iUAApUWpFD-2YLDyN0MRnwUBk-40DvDN1Zw7tyuU1TRNETRTGMZsVB6GCO4bOqxu09EJioQO34FxTEjXF7r2BbSiOryMJCAJfc50g6i9bi4J-dSyC-vsPbi_ojqLIE_P_7fB-q0KRN8oIb4VlpnjkTMVYKaeXfmN4w6ovW-NnlRjlSeiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدا بر روح ملکوتی سیّدالشّهدای حزب‌الله سیّدحسن نصرالله و همه‌ی فرماندهان سَلَف مقاومت و یاران شهیدش</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/452754" target="_blank">📅 20:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452753">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a982009c3.mp4?token=CjIJVqVnYLpRSSneyUZ9iYv7pTRFsBLWtZNyXpUVNR73qiKCOPkiHzYL0hdCvcjVl-OHjOI8VvyVGUj3X1uh9KcZ_MjfYVamjeUg0XwI1N0V5IqCAYhsTWUznOHMfumJrwXcRrQuuH-uPC83cBkInhB5mi8AS4xJKeocmQMUahkW56QNeJh1DwT4VXaeRrHf23hZ8U-CSoM7X6p4jLNzdRDTzGkcJJUKJ4j-fkyI_GEFGXjQN__8tbE8aracjiiA4Ya7Mf3QcIZB5KaY8qdKzpQTzYjXrXshtGxgEujMgK6n2ms7oHoVi8imkxKoFEQdHiRJhtYUmmRAiw-1n6oLMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a982009c3.mp4?token=CjIJVqVnYLpRSSneyUZ9iYv7pTRFsBLWtZNyXpUVNR73qiKCOPkiHzYL0hdCvcjVl-OHjOI8VvyVGUj3X1uh9KcZ_MjfYVamjeUg0XwI1N0V5IqCAYhsTWUznOHMfumJrwXcRrQuuH-uPC83cBkInhB5mi8AS4xJKeocmQMUahkW56QNeJh1DwT4VXaeRrHf23hZ8U-CSoM7X6p4jLNzdRDTzGkcJJUKJ4j-fkyI_GEFGXjQN__8tbE8aracjiiA4Ya7Mf3QcIZB5KaY8qdKzpQTzYjXrXshtGxgEujMgK6n2ms7oHoVi8imkxKoFEQdHiRJhtYUmmRAiw-1n6oLMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تمامی کنار گذر پل‌های حملهٔ آمریکا به هرمزگان آسفالت شد
🔹
مدیرکل راهداری هرمزگان: همۀ ۹ پلی که در حملۀ آمریکا به هرمزگان موردحمله قرار گرفتند از ساعات اول از طریق کنارگذرها فعال شدند که اکنون این کنارگذرها آسفالت شده است.
🔹
کار بازسازی پل‌ها نیز در تمامی نقاط آغاز شده و در کم‌ترین زمان ممکن انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/452753" target="_blank">📅 20:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452752">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رهبر انقلاب: جهاد شهدا، مقاومت اسلامی را به درختی تنومند تبدیل کرده و عزت لبنان را رقم زده‌ است
🔹
صلوات و رحمت خدای متعال بر شهدا و مجروحین و خانواده‌های صبور آنان، مهاجران فی‌سبیل‌الله که تحمّل مصائب را بر خود هموار کردند. سلام خدا بر روح ملکوتی سیّدالشّهدای…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/452752" target="_blank">📅 20:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452749">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IeV4auuCACVDFGSDoU4xPUZbl9VG4EIAHmzgQ8esdN1US46rAWrnANDhVyJbY27Q7p8DM3qaUJ9rn2wZo2VYzCTcZk5Qcx_a_Tp7MKo9XpPAHtqIHKc6zWdE4HDMg1T_owg6q6K1wYOVE10pIeYglh7rTxLsvHAF7RhWHkxFvRkVGJhFG0hqmA-leOOMJCrmsNSFIyJPumQOLVpUz47-Ufg8_j3016kbKlw6aQbBMr_XNxNARCC520YeJk1OQGgov3gdQgCLFn_pZpRoltcJ7GNnMocdTyqF7PEr2LT6wXqPSn52mTi-DkvMHT5scq1ADMfet3eYmqKsDs0dIfyHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5d6_ycwSfqZ3n2_UMBj2wA7X9sy1IXEgMCsjQ_JNWWTa4FQqz7Z-TTuvTsC7bvE5dwN-0USeaHSZierwxwwspX-hzi002APaQB1SRp5ZCVONZZrgEhWaiEVhEme-1M-jz1GpD90kS0YQxsLGNn7sggJBdFDdigieuoMWKvtlFcr-gfdIbUMRJXJsaBHKndLrA_RbFuchp7_fw-3FS1wx4D39Ftn-q7KCCnbMWc8mRzwqYK3OpaW_cMklq41s6_-SwW5EbdfgKU6dqto-lyIIb0z0ISMCaQB4JJHe6dm8j3P3kaND2U2kvnOUACSWeWqJsMXYHNctuvtfuQ9N5tvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-L0FfwHBqe9KwEzTf_wLBxx-no9fBAq6qoDoNT4vtye4_ozXGO3IOzGQ5UWdHlFgz4PYH1Aa6w6e5EvjSzJG-Zbrn6XzpKEo4TBd7JOOpUcjDwdGSeE1IpokzHqBh49AVIZhORb-vzvIifboL1sRtWX6RUpEyjD0E0yUCSLViPgRFzWuZ6m3I0TpaVtWhx6M8fRBGpoPcbrOq0mpwKSWNvi2NHpbdyQw8qUgq1RQuW1CFNbHk75tvQg9XnUVx5PtFdp9VeCDHLioN9zTFGuEs86Tv8slA5lTea8LrnI6yT5Xn1hdVsTKsDpGhWWQDAS-nbEMcseO4sdrokgGCxGLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
۸۳ درصد جوانان آمریکایی خواهان اتمام فوری جنگ با ایران
🔹
سی‌بی‌اس‌نیوز در یک نظرسنجی نظرات عموم مردم آمریکا دربارۀ جنگ با ایران را بررسی کرده است.
طبق آمار منتشرشده از این نظرسنجی:
🔹
۸۳ درصد جوانان ۱۸ تا ۲۹ سالۀ آمریکایی خواهان پایان فوری جنگ با ایران هستند.
🔹
۷۶ درصد مردم آمریکا فکر می‌کنند جنگ با ایران سخت‌تر چیزی بوده که دولت ترامپ قبل از جنگ پیش‌بینی کرده است.
🔹
۶۰ درصد مردم آمریکا معتقدند ترامپ مسائل مربوط به جنگ با ایران را بهتر از چیزی که واقعیت دارد نشان می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/452749" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452748">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFVSOreiiI35ber_Xzj45I4Ua9rI7RTU1BsoG7xZl9DxQG7VN4hksp-OUBipg7JNU0szWXRF_HczdfrupfEzozyUHgJoYkbYt_hXw9PmUAcUwg4VJt4us0Edv7n0INU3GOpXLFUF3IHNIeZCQYyk14ElSKQAcy3US4bAfTIsD_Cz-dkSGSb9rX4quFwrjvi-iJx40soPv8fHyamr_4_yqDyVYKt6yu2tjaDDVfpnoNQ2Enu_fhNRwkS0XBTHP5cMJOkj2srmRGRblzrwaq7_06N5-HnR1NEzqb0N7jzR33WMJsJSvwnxL_Lgm7ewwVZzMFZO3W3NhUCq9DZyUQfGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  رهبر انقلاب: جمهوری اسلامی دفاع از مجاهدان لبنان را به عنوان سیاست راهبردی خود تعیین کرده است
🔹
اکنون که حزب‌الله لبنان به‌عنوان پیش‌گام گروه‌های جهادی در برابر هجوم سَبُعانۀ رژیم صهیونیستی و حامیانش، چون صخره‌ای ستبر ایستاده است، این پایداری پیامی الهام‌بخش…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/452748" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452747">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌ پاسخ رهبر معظم انقلاب به نامه دبیرکل و رزمندگان حزب‌الله: پایداری در راه مقاومت، نصرت الهی را در پی دارد
🔹
نامه‌ی شما برادران و فرزندانم، رزمندگان مؤمن و شجاع حزب‌الله سرافراز که حامل پیام پایداری و استقامت برای اعتلای کلمة‌‌الله و باورمندی به وعده‌های…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/452747" target="_blank">📅 20:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452746">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📝
تا دقایقی دیگر؛ پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/452746" target="_blank">📅 20:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452745">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e2d2a86a3.mp4?token=AcGj2iKieq5mHqodC4-YWplvbvmGNPQQO7PWbjyzSFBRs98LELIWEQ8LT57ikL5nXDop4c8uA8vk4qFdK6zI6b7NtKpCJFAlW-Djo3lCHgr5Tm_QQOUPPkEqWIeJSOBl7gmgWR0gQUpQSQ3GwG2gHKoEuWMhinmmczROLwEevXtDy1K7F8LbZxRCdLMafJ79y02qpQpLKeqKG7YmAVkyXdQ_oA458Kg1N46mI1LReAr875BBglbg_s5ea51uUKeXX8m0-XW46TxdRZaHJZRvZN9MSSrR185UwtBVpIovgTQOk_ANxN7N36dxRPx8cXuNTGak7QkTsr6RqHLSAjoZPiO0I5J8cWNkCPaXwhz4LtByLUO2AbOtcZ_l1BDbkkNYBhn35xYTvojpo2uXUX8I-rhM3wS1SA0lf7Cj7nGQqm_n_biu6ZaS_eqjoK0Lzh74OqXQlXIDtj1LLG10JnIUK3VJTyUhM6R6VgplkOhF_cXIq1Vuq919BuP_MtYd6uOtm67PBja3ywpY5wlbWobkDC3bUpcLiUcPPWds0nIL8yxcLiIukhycmno7ceaUSnN1vi-6ILrTghcdxr3RAwcEmytoC0eJuYbhut2r9HooBN5qYmU1GNtSUFIsQ0qw7Pf0BnM--afz54PuopTNdCqruYnNBn5XKFMF_62m8ltz9JU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e2d2a86a3.mp4?token=AcGj2iKieq5mHqodC4-YWplvbvmGNPQQO7PWbjyzSFBRs98LELIWEQ8LT57ikL5nXDop4c8uA8vk4qFdK6zI6b7NtKpCJFAlW-Djo3lCHgr5Tm_QQOUPPkEqWIeJSOBl7gmgWR0gQUpQSQ3GwG2gHKoEuWMhinmmczROLwEevXtDy1K7F8LbZxRCdLMafJ79y02qpQpLKeqKG7YmAVkyXdQ_oA458Kg1N46mI1LReAr875BBglbg_s5ea51uUKeXX8m0-XW46TxdRZaHJZRvZN9MSSrR185UwtBVpIovgTQOk_ANxN7N36dxRPx8cXuNTGak7QkTsr6RqHLSAjoZPiO0I5J8cWNkCPaXwhz4LtByLUO2AbOtcZ_l1BDbkkNYBhn35xYTvojpo2uXUX8I-rhM3wS1SA0lf7Cj7nGQqm_n_biu6ZaS_eqjoK0Lzh74OqXQlXIDtj1LLG10JnIUK3VJTyUhM6R6VgplkOhF_cXIq1Vuq919BuP_MtYd6uOtm67PBja3ywpY5wlbWobkDC3bUpcLiUcPPWds0nIL8yxcLiIukhycmno7ceaUSnN1vi-6ILrTghcdxr3RAwcEmytoC0eJuYbhut2r9HooBN5qYmU1GNtSUFIsQ0qw7Pf0BnM--afz54PuopTNdCqruYnNBn5XKFMF_62m8ltz9JU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله جوادی آملی: به جایی رسیده‌ایم که ۲ ابرقدرت به ما حمله کرده‌اند و مانده‌اند! این معجزه نیست؟ معجزه حتماً این است که یک سنگ حرف بزند؟
🔸
هیچ فکر می‌کردیم که ما دو ابرقدرت را چُماله کنیم؟ (درهم بکوبیم؟)
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/452745" target="_blank">📅 20:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452744">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jogcMKtqdC2CwwQdiY87fOv7cOHRO56csDZam4xxBczkTwtzfW7xXHJhYougdTAVF5H4wIWCMJ1H1wh3cwsrsmS0uw5wQySePTZeSuxTn-JMMj6GGIa1P01o-g81va5o3YSCYyH52iCRxDguW1EoRt3L2Uiz9qr0K7gXb7q-Yl6Mx3d3EXcU6qx9Km6lx5F4380tAqL3EukuNnIXnX84u9Iq5dEDO8cWq9r1blIjfyPN_0Cq7wcslD_J_CRArg1IWnVYDrEvon2zWIMbig0RaQt1l9Fl7wvcnloeOM-_Td1AgFEN8eSkIq7nLsUzVHZzDTwmLymiD85HBXHuROlY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فتاح: آمریکا نتوانست حس شکست را به مردم ایران تحمیل کند
🔹
رئیس ستاد اجرایی فرمان امام: امروز قدرتمندترین ابرقدرت تاریخ با پیشرفته‌ترین تجهیزات نظامی و تسلیحاتی در برابر جمهوری اسلامی قرار گرفته اما نتوانسته به اهداف خود دست یابد. همین مسئله موجب شکسته‌شدن هیمنۀ آمریکا شده است.
🔹
امروز مردم با وجود مشاهده خرابی‌ها و آسیب‌ها، احساس شکست ندارند و این سرمایه مهمی است که باید حفظ شود.
🔹
هنر جمهوری اسلامی این است که با تکیه بر نیروی انسانی مؤمن و متحد، در برابر قدرت‌های بزرگ ایستادگی کرده است.
🔹
در منطق قرآن نیز پیروزی صرفاً به تجهیزات و امکانات وابسته نیست، بلکه ایمان، صبر و استقامت مؤمنان عامل اصلی نصرت الهی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/452744" target="_blank">📅 20:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452743">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c11c9aaf.mp4?token=pOqc6T_BRZJeRnXtS33O7Z7bvFFzswdGKBg8maCYcZmn-ruDKeShEKSn-sReKiQSuJgp9GOD7z0Blo_E3MJdFsqnsmWMz82TvVikmV2gkgVCQDYz3IuNoMb53dCtNNQgyGqqf9sfyG8HdEbgtR_tqT24Jac6xy9MEiriRe3XKVx8JZ9XKdQr-OXdfD9N-xx2g7GVuWtPtU_EHfW2sOK4KiFrJtn62-p4ZXqbz7vvg2Y4nqokgExz60KpOTV-1OV9ZGI3Wa7DjiDKt69aTprkedphVk72ask7IaA1cvk7OALu37ZQTPN3Tz3HDOFV-tCDCaTnjMssaf21SJVESmQ8Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c11c9aaf.mp4?token=pOqc6T_BRZJeRnXtS33O7Z7bvFFzswdGKBg8maCYcZmn-ruDKeShEKSn-sReKiQSuJgp9GOD7z0Blo_E3MJdFsqnsmWMz82TvVikmV2gkgVCQDYz3IuNoMb53dCtNNQgyGqqf9sfyG8HdEbgtR_tqT24Jac6xy9MEiriRe3XKVx8JZ9XKdQr-OXdfD9N-xx2g7GVuWtPtU_EHfW2sOK4KiFrJtn62-p4ZXqbz7vvg2Y4nqokgExz60KpOTV-1OV9ZGI3Wa7DjiDKt69aTprkedphVk72ask7IaA1cvk7OALu37ZQTPN3Tz3HDOFV-tCDCaTnjMssaf21SJVESmQ8Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیۀ تحلیلگر لبنانی به فعال سعودی: ایران را به‌دور از کینه‌توزی و تعصب تحلیل کنید، دشمن اصلی خود را بشناسید و پایگاه‌های آمریکایی را از سرزمین‌های خود برچینید
@Farsna</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/452743" target="_blank">📅 20:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452742">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa4898b44.mp4?token=TpLFPjTS_T-32UCQU_SNdj73tpddKUFsyuj6SYtWcnurkDLxUuNXYoHbkF1H_eJr2FtUDFutcrojoyaetX7nhisj-7N8gRAzdzXHKXdt0AYQ0lRPao-h8QlKwFD2L-IvxYnuDvQucXlWe78Vc7UzedKhPLaViyNdvDUmE7Z9Wkhf6ZzUf0pOE-ZFvGmvRYiPU_d3yIufGzLQQFmP7DzyN0AKLb_eU3HuIpd3ELIQYvk0pQ7f5KXEvW1gVOoU7Pcqywx3ZvoPRgdSSfzNgF93Vs88RnBJHVV2C3rYFF-s2vr3asf3xNav312Wz0oOctaBdnxjie6brrYnzQwgBYD0mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa4898b44.mp4?token=TpLFPjTS_T-32UCQU_SNdj73tpddKUFsyuj6SYtWcnurkDLxUuNXYoHbkF1H_eJr2FtUDFutcrojoyaetX7nhisj-7N8gRAzdzXHKXdt0AYQ0lRPao-h8QlKwFD2L-IvxYnuDvQucXlWe78Vc7UzedKhPLaViyNdvDUmE7Z9Wkhf6ZzUf0pOE-ZFvGmvRYiPU_d3yIufGzLQQFmP7DzyN0AKLb_eU3HuIpd3ELIQYvk0pQ7f5KXEvW1gVOoU7Pcqywx3ZvoPRgdSSfzNgF93Vs88RnBJHVV2C3rYFF-s2vr3asf3xNav312Wz0oOctaBdnxjie6brrYnzQwgBYD0mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: حرف آخر حرف رهبر انقلاب است
🔹
سران قوا با جدیت به‌دنبال اجرای منویات رهبر انقلاب هستند و وظایف خود را تحت امر ولایت فقیه انجام می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/452742" target="_blank">📅 20:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452741">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">📝
تا دقایقی دیگر؛ پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/452741" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452740">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gifcw4Ctuyxa2PKN81Afs6bPXrgEQDmQxzFWOQGBwutYZWwOjd46eOFWD8YPqa-sb0SWkzh8YM4gJr6DXnoSfLiQPO2iyDLEeCVrlXU8vTVDWkEYSSEBH7oOvIQSVhnKygWWmvVTKSktWj9BPFCHMtqRXPcAHcpRu8QQCElV6Xa_o55eRY-WYkebu0C0LkxwhbfcKoi03ulgmH4mJpODaIdTrFMEUrEqhBBBnnjwmRtLU1-xWknvcBtz6JbajMLHfosHICtBFd8AwFEhWsDM6XkUlRWhs-waQSjoVZWWjiNRzU0t6OAFKuaBqvPIgr11nHS7XTkMPTBirEcqmg0GaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: جنگ با ایران، تک‌حزبی‌ترین جنگ تاریخ آمریکا است
🔹
خبرگزاری سی‌ان‌ان در گزارشی نوشته:  درحالی که ترامپ ده‌ها میلیارد دلار بودجۀ دیگر برای تأمین هزینه‌های جنگ با ایران درخواست کرده، دموکرات‌ها در کنگره صریحا با این موضوع مخالفت کرده‌اند.
🔹
جنگ علیه ایران اکنون به جناحی‌ترین جنگ در تاریخ آمریکا تبدیل شده و این اولین‌بار است که یک حزب همۀ درخواست‌های بودجۀ جنگی ازسوی فرمانده کل قوا را رد می‌کند.
🔸
حتی در زمان جنگ آمریکا علیه عراق که توسط بوش به‌عنوان یک رئیس‌جمهور جمهوری‌خواه فرماندهی می‌شد بیش از ۵۰ درصد دموکرات‌های سنا از جنگ پشتیبانی می‌کردند اما الان اصلا اینگونه نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/452740" target="_blank">📅 20:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452732">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QW9hKNLr9y45deE9zCiNpbM-Xoi4hvcul9mZsMgBeEqM9FFbOnzb7QqMDE7lVHCxg0XzuawrFoioV5Z1lEW2T9yh0kUGNnxhQPJ6yWPMWR_HhvKtLhJER5-lPHk0JJvaitwonwSOMvA_uIIVth9j57MdMbTxTFHdYtw6oYJM3IAcpHLoAOPR8S5Nu30SoDrO0lqMukV-qFYABUdcY62umtRQk9DTpWcdNX7gs8pBj8oP1xb0zTh03AKBNF6ySP21Erduox6xuAm18ydrU-OJTKxg7v4Ys2iA8WkU_3IBYxv0KGtfQHIwavhzuApvTbxrKduAIZb5hLcTkadRmTb5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلالِ تاجرنیا شفاف نیست
🔹
در حالی که مدیریت استقلال در ماه‌های اخیر بارها بر شفافیت و صداقت با هواداران تاکید کرده‌، قرار گرفتن وضعیت نماد این باشگاه در تابلوی نارنجی بازار پایه فرابورس و روند افشای اطلاعات این باشگاه، پرسش‌هایی جدی را درباره میزان پایبندی علی تاجرنیا به این شعارها ایجاد کرده است.
⏺
باشگاه استقلال به عنوان یک شرکت بورسی، مطابق مقررات بازار سرمایه موظف است اطلاعات مالی و رویدادهای بااهمیت خود را در سامانه کدال منتشر کند تا سهامداران و هواداران بتوانند از وضعیت واقعی باشگاه مطلع شوند. با این حال عملکرد این باشگاه در حوزه افشای اطلاعات طی ماه‌های گذشته با انتقادهای فراوانی روبه‌رو بوده است.
⏺
باشگاه استقلال در دوره مدیریت تاجرنیا، بعد از اعلام تغییر در ترکیب اعضای هیئت مدیره به تاریخ اول مهر ۱۴۰۴، به مدت ۸ ماه از ارائه اطلاعات مالی خودداری کرد تا اینکه صورت‌های سال مالی منتهی به تیر ۱۴۰۴ به عجیب‌ترین حالت ممکن و در دقیقه ۹۰ مهلت معین بارگذاری شد. اسنادی که ابهامات فراوانی پیرامون تایید و بررسی یک روزه آن توسط حسابرس وجود دارد و مشخص نیست آیا اگر  پای مجوز حرفه‌ای و الزام آن در میان نبود، مدیریت استقلال باز هم صورت‌های مالی سالیانه می‌کرد یا خیر.
🖥
گزارش کامل را
در فارس بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/452732" target="_blank">📅 19:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452731">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eaae38011.mp4?token=iXWTQAKuA05Qim1mSo9l_8qF5SrUXM9JqOT5IuVcXCWh2VgLDmQWZtxa_HcikLyiI0RAwLszzPXdpXJLLGEsf-maQMHzxqTxu2IeK1JkRsPyfVW0QDFXqvKQZ1SVXBS8cp9zr20ZFp0Ug0-B8UeP95DjIi5HTnqon_xhXo8PYQLRV60tJEiec2VUWwMe4-z-tmrGyCrzjiavI1ADgO6RZWnilZVJd7tjgTTIzXNJ9OeE36PD0It1FZW-bDFOYoMiJK5omlSVbyCiy7s4XTrsbBSELG4fkfc67IwRcgNI79Bg2PMGSvgDPr_-CCLAi5aY6WfEdSmzI-AZQqcWTKNS7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eaae38011.mp4?token=iXWTQAKuA05Qim1mSo9l_8qF5SrUXM9JqOT5IuVcXCWh2VgLDmQWZtxa_HcikLyiI0RAwLszzPXdpXJLLGEsf-maQMHzxqTxu2IeK1JkRsPyfVW0QDFXqvKQZ1SVXBS8cp9zr20ZFp0Ug0-B8UeP95DjIi5HTnqon_xhXo8PYQLRV60tJEiec2VUWwMe4-z-tmrGyCrzjiavI1ADgO6RZWnilZVJd7tjgTTIzXNJ9OeE36PD0It1FZW-bDFOYoMiJK5omlSVbyCiy7s4XTrsbBSELG4fkfc67IwRcgNI79Bg2PMGSvgDPr_-CCLAi5aY6WfEdSmzI-AZQqcWTKNS7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چذابه؛ گذرگاه عاشقان کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/452731" target="_blank">📅 19:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452730">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GezOtJfE8sj-LYSvc_ia89KU-JvBf-0x2vq3c19Fced8jotm-nzRbdUf8gOkHKFbX9XTt7xJKWqvXf3yNJNvkQMDZ5wZmteDExQwbKPdM7_3KhNflOhR1BMqeUn8-2MCcdxK0HOFfWgOymal5FGuQILxQv3CxT_l3Di9roF_sAmgLiTjfVxmr6qFEMNDTPrVsnn3nnV2TyGK2vp4Enff_y34PSmEqtTpBDALFES6AwiuNRx1TEWnZAlMR0evilIU4-oa3ATtqr5vKAzDnWmORXpFfAuLmbSWxNVFp4LY8XoYJDqJsN7gTrlR_zpqqR6kU1J5nbUv7msMllT5HM6g0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ عراقچی خطاب به مسئول سیاست خارجی اتحادیهٔ اروپا: شورای امنیت و اتحادیهٔ اروپا باید رژیم اوکراین را بابت حملهٔ جنایتکارانه به کشتی تجاری ایرانی پاسخگو کنند. @Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/452730" target="_blank">📅 19:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452729">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTQ4LvB_55KCRu57iAuxIG8nbXDocOXCmAxnc5LKiOH0n0F_Pvg-m0Rzftpwm8H8j2sqsgAa_JrfATynR5W_fr5N2dQd6hix5MVykonYCxIyYv0rMiji_r3bAA7UoqFY7fn86ywKbSuskqwiCmcHcpoQPtqphXYKiXVf1DXqW-aEoSArQxJtvc8TptBBAu6wKZzPuispfwcabkibxBFY_5YHGtB3sM1AQGvLh3IXcyop1_D-zll8zbFtl999_unCu1u3PkGb2e5VyF17V0sW8dSyabRWMXVL-EwRo6JOncP8CNLxIw0OXXkS2RmAMKmgtJ76BzZjNN2q0uni4UjiyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات تخریب صهیونیست‌ها در جنوب لبنان
🔹
رسانه‌های لبنانی از عملیات تخریب بزرگ ارتش اشغالگر در شهر بنت‌جبیل خبر دادند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/452729" target="_blank">📅 19:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452728">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaCpWGEGkc9VwaBevDeYxdiLzPCjEXwRT2xKain0Zzaewqj_djrzysPyu6xc9MNNk65ALC8Erl3nZ6rfny-2r3jkFM5t_FHNicjmL5ICPfyMcOu6DTJdjarKyBgPT_uxoffqvta927eW_lNJW7NDitZpVrTIaS0DB5HmW2nSbrAhxq010PtAAmGLPiMfE-PjoIItWQjVzsfyiSnRjol5T_QkuXbLVZxH77e6nIGm2yG9XV5_M6w7fjfReADtydnQbCoYBR3QD71nxfnolr7DfFIHEwJSkJk2OkyYUaqE8TRP1ajEW1stqFOxkic7Ql8A4eqGWy0NwiTInkwxpiojww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الاسلام قمی: دنیا باید بداند از خون رهبر شهید نخواهیم گذشت
🔹
رئیس سازمان تبلیغات: نباید اجازه داد دشمن با سرگرم کردن افکار عمومی به حاشیه‌ها، صدای حق را خاموش کند و دنیا باید بداند که ما از خون این ابرمرد نخواهیم گذشت.
🔹
وحدت حقیقی حول محور ولی خدا و خواسته ولی خدا شکل می‌گیرد و امروز حرف دل‌های مردم خواهان خون‌خواهی است.
@Farsna
-
link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/452728" target="_blank">📅 19:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452721">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MfkcISVhgwCUQ634mn3_DSozF8c34tIRYqAMlWoO1ySL28hnIQWSvIbF4Xq1yKZe3sKuNMSLoq-emzkuwuKXmnvTO7tRtTWL8P8WWL1asUnMGibIUpVgkFvzfJPP9pimqgIwe98BZ6-JKzGomGoRbM8EHvDOrI1ia7bqnwQltCTwyH5CzfDp8Sl0ky2SKQVtt8RdLHxqNeEhGIqeqWRu4PvDjY6J6wkot1FbOp2fpkGR3q8LUo4EZodUgN3odSGoJb-r2NZ3jcs29NhbnXus8YeJQJHtQzdxoLRu3tokV4OB85jP5Y7P9Yr6mak6phbRqcLALUBT1YF1fTgyfp00GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r87lpq8q0YXSfbwAd5xx-J5vkOytOyLLJ1vFenbhI6N0g553bRftatgcSfgjkg4Gw1FOkr6sUzfXBl0qERcAPMx1x6a0DN-qmbuQ4NNgMRs3S_Q8KNBkRQQef1SjlUrPDxkg7sZ2Swv5LjTa726DbjTw9oJ0UOz0ta-4oN4JY5rbSty6Wz2xrxM31tzjwkdVaf45PjzoMMHR1G8wV75TmguWaElFUj2ZMpwTYYhrFq8MLPfKMWpHnDxi_W9PVsw_CFwHMQGTUFGJwmsgTJdnwnfZmt1TJ3EhspqUFe8IO1liTGi7veADdWyNS9Pbku9i6qNakuNu3lVIDaFN2bj43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pNJLEdXBuuzOdwJzgOnHakcNVkrqMK1GMIQ1ovISxax5SuJxCXLTeV_QmL_r1JTub5rYP4fSJ5gn9AyV16IFGhiFnqjNr7sS7tiDr2CHIO3umYso4Dy_pxee1D6vkkHiO9gyqgKYgOamYJURMQMGiBQrqO8NZdEPDQBgyGoPBPRlla0BkK-V4RH3K2MzUrqZEWHxBJNYsxnTDteCTGVRmQSYpSNtjIn17WxQlO1YrwwqwQQR1rou_SpE7JZoQXeXofUsnLS8Y2YtfBNz0BUpk3hGZHo53RY7p2vTw7jNuCegPFhj1RvZIhIWEr6qrlNx1P-BuTh85pmt55rNtZzP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8oNhwTUlUi9f3wVdnD_o_XVI-Jo5AQpWHvR7fEzvpygWV9IHqUkx_-5PJH2ewadJFIMuYvGouUdBfoOI2YysoklZb2VvjcQ8RO1RB9PgG1tiGvQxJ031j1QUcbtAn7MkjsK28KmlY20iuLfA2zYHStH8DT00t-r8JobNKe377DOpno4kJqcfacoUs6kF3gPbiq1OIpZxOBuldtSJ8m3yY641qkYehkR2Q25WvHitekjzdaw4r32MRJhS5BrQa034f_Wkzcwb-Y_R3pmh-Ax3H8iPr6yRQebv6jMC7GsfKf4WKIgnj3RM9F9UU0MXZleoaSJcgwxEMtflmTNUxlV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DaIxmQzVagOEybJ4wgcDSQFRR5x0O8ldVOUzOYPfon5pHCWcqCIUAHxp9WWCasTGGACiJyx6f6cjDxIriKBqX3g4xWPC1ECJd50zifUUKquWOGwPr2uVEjlY4s_SRHO4Umm8XxEzVIh6UDuTZmNI_fduGovQYxoUuy8WBVZ-KkrgiVz5mR_Q5V52gyaVwTndgMmiUUgKGC7Q2uMiqfyF4wQkTZGezuHCS2Q6YKH07xMPuGYESfs4rDb-oARR91j8WvddXnSIgzncFvsZHCQg1BYxdOg0XCeP_FlMssIKFZ1IEOsWIWSrW-QSjgSB9iJhjrrh8QfDt0n8nNkY9qvLMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AM4t0BUjrlSSNK09Y4eTV362CHtzN-raZvMNL6krvZlgB0UiKU9W1LkxrLZ-y06FF3beysiiXaahF8emx6EwPOWF8kfmX5e_9Y1JOfWAgG5zsG241q-ycjFKH4FD4K0YamaG8YPDcMHKVjX7PZ9NlDpEhQIxOuN3kIJ1xp8Y19MZDYaQnPOpIk5boGUP-33x0Tsjsk3ZnAzshQK8goTFA7Ws0w3ejR3C-jMAA8pWspLeEjBbSeYLU0UPk-s3JAF5cV6HCI6u1tSMe3WclUNhZRAEURkvSUyS-90ZjzSb1efGxUHrK9Ru6I2SSJUUPo0EfAuZqzm6u6zInSac2USpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWh2xcqzojNgktIg7RiaIEbXCoWaHZJ0D0ycnphrqZpHp-mYUBKmlYJQvJCxq_PgjFKPf38T7RuO8DXkQ7IEqkDSPmHQOx8mAkKJcD13geUJIB66BZN1LFS89teGgSzdZpgQRHZBvtEx1WyUP2zG4YWx63ZJ_9ZT83y-XHQjlMyFKP5y-dd2do27RpQkDlN8HEFddYBdbvPaWeUjBkO54StxnOuRoPngYy-ldf_YXfIi5lfJ4jsmkpTrhSnTBEtevKXQaSmBWW5eeJ1eaOIdnLgpthB8q7dUBLFKKqhWPhV-EoYEaasyQ4mUiZvVxYXC5fy7dbmz_rc4R--sZQj-kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زائران اربعین، استوار در مسیر
🔹
باوجود افزایش دمای هوا در مرز شلمچه، موج حضور زائران اربعین همچنان ادامه دارد.
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/452721" target="_blank">📅 19:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452720">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fe9fd6ed.mp4?token=MVcPfmM4e4GF94QpE_NGk21ez_8elY5gSukrJBmRORsLvpJ0dBj-FPUUN7CRs2oyO9Ccx6ih_3ebjuzCwFyHfWuWQPZt5_KxhEIGjZbEZGj8Onqeb0dnmhscJ2yjjwP7jVcIDSaBsZ_7EVv6pRX-9TuqdDaZp3FPLGhgiRtcHAGAT1WDzr_UwyBwVS2UOKQ_r-hLgmNf_Lki-ouBxbYQM8CKle04DMs_jPdXQOkQZPh-Cfre6hAp7PaIrb-sHGQ59gX0af0oo05tD-L7TclM828iQi1307K9i_K9SMapSoSPGNKikvNH4VrGYFx-Yor68CimcGqqDIh85Tg-VVbSyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fe9fd6ed.mp4?token=MVcPfmM4e4GF94QpE_NGk21ez_8elY5gSukrJBmRORsLvpJ0dBj-FPUUN7CRs2oyO9Ccx6ih_3ebjuzCwFyHfWuWQPZt5_KxhEIGjZbEZGj8Onqeb0dnmhscJ2yjjwP7jVcIDSaBsZ_7EVv6pRX-9TuqdDaZp3FPLGhgiRtcHAGAT1WDzr_UwyBwVS2UOKQ_r-hLgmNf_Lki-ouBxbYQM8CKle04DMs_jPdXQOkQZPh-Cfre6hAp7PaIrb-sHGQ59gX0af0oo05tD-L7TclM828iQi1307K9i_K9SMapSoSPGNKikvNH4VrGYFx-Yor68CimcGqqDIh85Tg-VVbSyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زنی که بازیچهٔ بلاگر قولنج‌گیر شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/452720" target="_blank">📅 18:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452719">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در بندرعباس
🔹
سپاه هرمزگان: فردا از ساعت ۸ تا ۱۲ صبح احتمال شنیده‌شدن صدای انفجار کنترل‌شده در محدودۀ شرق بندرعباس وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/452719" target="_blank">📅 18:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452718">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41feae11a.mp4?token=OMeseNmRkEAFvVp162idHs1QP8IJPF1M6m9gSl0ebp61CVWhyecQhPFJM_hnXKGQmCrbBBzHOH_EFW9c0HGF0p0wfjPgOVkYLLw99B1_HRRzG-IN71soUfvf_m7Y_rzMBPydJiy_FaIW_ql5ctXkTi6sjWJdRqZMB37-f34Lz0u2DA89sg8BP6c_cMmivRB_LsOuctkrt7c2lXNcNVXxRK5pHiemo4oCHhHxNgdvtL_dGLanF7vGsYJoAzt5EORsnxtLSsQ6Sb_1Wm4_ajK3I2YvVpyxXdfeVc2FEZwZA3wftWHNiD2El9tSLWDwB19_SpK9tEy6EJVQHd2KKMO9hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41feae11a.mp4?token=OMeseNmRkEAFvVp162idHs1QP8IJPF1M6m9gSl0ebp61CVWhyecQhPFJM_hnXKGQmCrbBBzHOH_EFW9c0HGF0p0wfjPgOVkYLLw99B1_HRRzG-IN71soUfvf_m7Y_rzMBPydJiy_FaIW_ql5ctXkTi6sjWJdRqZMB37-f34Lz0u2DA89sg8BP6c_cMmivRB_LsOuctkrt7c2lXNcNVXxRK5pHiemo4oCHhHxNgdvtL_dGLanF7vGsYJoAzt5EORsnxtLSsQ6Sb_1Wm4_ajK3I2YvVpyxXdfeVc2FEZwZA3wftWHNiD2El9tSLWDwB19_SpK9tEy6EJVQHd2KKMO9hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنکور زیر بمباران اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/452718" target="_blank">📅 18:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452717">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آلما: ایران و حزب‌الله آب و برق اسرائیل را یک‌شبه می‌گیرند
🔹
مرکز تحقیقاتی آلما: وابستگی شدید رژیم صهیونیستی به تعداد محدودی از سکوهای دریایی، تأسیسات آب‌شیرین‌کن و بنادر، این رژیم را در برابر یک حملهٔ هماهنگ و چندبُعدی از سوی ایران و حزب‌الله به شدت آسیب‌پذیر ساخته است.
🔹
بیش از ۷۰ درصد از برق رژیم صهیونیستی از گاز طبیعی استخراج‌شده از سکوهای دریایی تأمین می‌شود و بیش از نیمی از آب آشامیدنی این رژیم نیز از طریق تأسیسات نمک‌زدایی که آب دریا را تصفیه می‌کنند، به دست می‌آید.
🔹
این وابستگی شدید به زیرساخت‌های ساحلی و فراساحلی، نقطه‌ضعفی کلیدی محسوب می‌شود که یک حمله موفق می‌تواند تأثیراتی فاجعه‌بار بر زندگی روزمره و اقتصاد این رژیم داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/452717" target="_blank">📅 18:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452716">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146807f99e.mp4?token=jK8f63UDNmGb5aCjRUBdrzL4cPBrbc6QxTQPkZjYLovDhBM7PiX-CEPxhjR57p858PNW4bjy2ZBQjonOGOBVC1lbEhJaJO4CAHet9s4xGeCuQUlcqkSzx27hBM1483NPpGqC2g9Fg8BLuAxBXax6HyI-MnSq_60Jl8ino0JSx9fXU6RIBadO2TbZ8KMS42VJoMlmx8NZ6u7f6bJKaRREzrzdgXhvWEzwPXRIEXhMgwCBeZs8xqfid73i2MBM9acuf1eES4rt4D_YJPiNc7fF9JTBVIA9cjFm37q9wn-SbiJSBJr9tpoGvpxJcTtUMxf5n9VpkOsulheYZLRhEVaKuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146807f99e.mp4?token=jK8f63UDNmGb5aCjRUBdrzL4cPBrbc6QxTQPkZjYLovDhBM7PiX-CEPxhjR57p858PNW4bjy2ZBQjonOGOBVC1lbEhJaJO4CAHet9s4xGeCuQUlcqkSzx27hBM1483NPpGqC2g9Fg8BLuAxBXax6HyI-MnSq_60Jl8ino0JSx9fXU6RIBadO2TbZ8KMS42VJoMlmx8NZ6u7f6bJKaRREzrzdgXhvWEzwPXRIEXhMgwCBeZs8xqfid73i2MBM9acuf1eES4rt4D_YJPiNc7fF9JTBVIA9cjFm37q9wn-SbiJSBJr9tpoGvpxJcTtUMxf5n9VpkOsulheYZLRhEVaKuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ممدانی: نتانیاهو اگر به نیویورک بیاید بازداشت می‌شود
🔹
شهردار منتخب نیویورک، دوباره تأکید کرده اگر نتانیاهو سال آینده برای نشست مجمع عمومی سازمان ملل به نیویورک سفر کند، براساس حکم دیوان کیفری بین‌المللی بازداشت خواهد شد.
🔸
این وعده بیشتر نمادین تلقی می‌شود؛…</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/452716" target="_blank">📅 18:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452715">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8626a4195e.mp4?token=bBDS26bL56idjaw8VP2bPu0Z5unhOyWCa23h82aFvNn0d2Ybha-xtISq1wrdk6B59SpRa70Yv1ZuUCuYcELEdsUsTdM9OTEF26OR-t2FnbKagafOCPO_rAjIVKP-Z5a4hmijHBWlhSvD9euK1inhgpZouZ3SjlhLfQHNkg-Y792rr7SYfJzlSEcDHzpojCyc76-mITepXI-QiEDhxYO6zzLYvUL4VZ9L0k-ROb80GsuDyJjhQ-zh0eOMt0ysmpXAMvr-tFdz8wlqFPYy5wMWFiQCHYdFrI6Sa7vva4A9oULAdlejF3TdP0m8dJWvbpKvGm5RTwIe95uVD6K5nvvG2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8626a4195e.mp4?token=bBDS26bL56idjaw8VP2bPu0Z5unhOyWCa23h82aFvNn0d2Ybha-xtISq1wrdk6B59SpRa70Yv1ZuUCuYcELEdsUsTdM9OTEF26OR-t2FnbKagafOCPO_rAjIVKP-Z5a4hmijHBWlhSvD9euK1inhgpZouZ3SjlhLfQHNkg-Y792rr7SYfJzlSEcDHzpojCyc76-mITepXI-QiEDhxYO6zzLYvUL4VZ9L0k-ROb80GsuDyJjhQ-zh0eOMt0ysmpXAMvr-tFdz8wlqFPYy5wMWFiQCHYdFrI6Sa7vva4A9oULAdlejF3TdP0m8dJWvbpKvGm5RTwIe95uVD6K5nvvG2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نتانیاهو: خانوادۀ شهردار نیویورک سالگرد ۷ اکتبر را جشن گرفتند
🔹
ممدانی به‌طور اساسی از حماس حمایت می‌کند اما در تلاش است بگوید این‌گونه نیست.
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/452715" target="_blank">📅 18:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452714">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqLK_fsmFhgvk4sDD9Diw6PR7RBqYgOTNgjN-UdGjFbO62RRHMHihihsq7nZj6HNSBrabr8nYV6d0kER_QLTiyoQTadsSCUAXEa2eFaT3aDymdmsn_OyoI3dfakSoq3YejkaHLSiZWRYFzPVPGtywfLuaYp_TmJF4CyrCyuZLPyTu2HgtI9kGkTMR_1ujO9EMHr_E_SG0zZbQsvC4XQNuhFHeOU8yH4CiZTZOR-BKmswK9jPR3JKzqLzQfFnPH9v4onzlyTC0oVvdwI4uxQ0q81gZ7OHF7_aSo3s7N_ktsfkpWDpibMLVgYHGI-8B8hDGP1Wj1yfD8waPBrNbbn-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس از وقوع یک حادثهٔ دریایی در جنوب دریای سرخ خبر می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/452714" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452713">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjgHCj62qCluhE0Fh1hMvzUaBubVRUTZkfedjHzrWLD6Dk2Dn8BhUvNR7ec6NG4zx1_qUajAnCW9711TSQ9CJGp_jjl_yPTzCwOey9IU5vjw_CqSD-5yr8NRNVW6qe3PkBqN8lfUtcCKYNIVeqX4AR18nh0Kf6X9J-JFwi3IVxjNB-vEe-A0PjwZW3m0soT9fxRZhinEbqnD8wN7g7BzYr-QfqQjD-5D4WZuUZEIi1EzU77m2pHEQHTFNhMpnswEe0-CEi2hNoyqcPQz5SayTaoDNLiw3KLnG6iCz_0feoUgUvq2aF5MBsDX9ydfwgaMIDZfM6tfBSSEXo5O8FoU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام یمنی: عربستان از شکست آمریکا در یمن درس بگیرد
🔹
معاون وزیر خارجۀ یمن: حتی آمریکا با همه قدرتش از به زانو درآوردن ملت یمن ناتوان ماند و خوار و شکست‌خورده عقب نشست؛ با این حال، رژیم سعودی عبرت نگرفته است.
🔹
اصرار رژیم سعودی بر ادامه محاصره یمن پیامدهای وخیمی برای اقتصاد عربستان خواهد داشت.
🔹
«محاصره در برابر محاصره» یک معادله برقرار است و کارآمدی خود را ثابت کرده و «تشدید تنش در برابر تشدید تنش» به‌ مثابه تیر خلاص بر اقتصاد عربستان خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/452713" target="_blank">📅 18:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452712">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۰۵.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/452712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۰۴.pdf</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/452712" target="_blank">📅 18:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452711">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e93b70354.mp4?token=EhbbPOZQaiZAHkwtKM32_xvxpAGlL-lcerDAP7vLlwNjzrU1gvNU6e0XA9c1Ds1K-616VDu3K1uzHZpO4SQ-aURlXCzbiaWkmLprRSJ4JDzacEekmjqX0_Q6YCtXFuApU0PRxddKg1wzsEKakYFs9zUA-ky5W3Er5_xxDX4swF0dpkj8VN44GMnzbo5zt0njPgaEQHAbFEtaod7AJ2xZwzJ59tgiBUo6TTJehcX5qZB1ruEgj7GVkCpfMCUCj6NOP_beOoKQ_XOLiMaLUTVkjP4Urye31HobOEDohRHoVlmR1t7ZsojZd4DrM7zlklFvZX82Y2PfPxVpQIMUe82QRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e93b70354.mp4?token=EhbbPOZQaiZAHkwtKM32_xvxpAGlL-lcerDAP7vLlwNjzrU1gvNU6e0XA9c1Ds1K-616VDu3K1uzHZpO4SQ-aURlXCzbiaWkmLprRSJ4JDzacEekmjqX0_Q6YCtXFuApU0PRxddKg1wzsEKakYFs9zUA-ky5W3Er5_xxDX4swF0dpkj8VN44GMnzbo5zt0njPgaEQHAbFEtaod7AJ2xZwzJ59tgiBUo6TTJehcX5qZB1ruEgj7GVkCpfMCUCj6NOP_beOoKQ_XOLiMaLUTVkjP4Urye31HobOEDohRHoVlmR1t7ZsojZd4DrM7zlklFvZX82Y2PfPxVpQIMUe82QRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لگوها علیه قاتلین جزیرۀ اپستین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/452711" target="_blank">📅 18:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452704">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNZ8OQUGN4G7Yg93qHlUOWPZ2A99b1xfegeErmq529WIZK-HYS7GhHmxZhjUFc-6uKnZquY9pKo4si7K17rotNjx1dOIZlBrfGY-xfKP09BLu9yM-gIqtfPNmkXKg0mEuiA7JDFTO4Fh1tQJlKlTkn55Juevt8RJkuAHJpdVJa1bRm7J1sEH9XeXxYYKJcASpQFrushrfknv43QhBK2jnNSJzhXqDIbrx2f0EHptZKgJy0xztWR-erm2HGD304d3OQ-QNiQRdgVStCvQeu1gWnxT0Jly2qNlIjat_-Vsi1rQSGY0yQddWCAm2Mi376yl75mjuFGcbzVy1oPA0R9hNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0WBXtdDhGxR-HktJVSuKbDyBhAwnTUZsGJVnEdF9Qg5gXab3rPYpbzFudzxFnIbXrp829xUItCvVPcHqBdHqJj9jI8LaXzkLrcg3XvdnsMnJE1fi8uRyTG1_pQpxD9DKM9_YzJoFxYDWP0Tn-QN5RxNrxQV1Pyoz30Yzi_NbrvkWRTZYAsjpVgtlvD5aBmey-MxiRVqpIaXG_bV5m7rzLrI1opqNZ0NPZimznW1a55cPLqRiS9Cg3bR3c7y6bYoJsXIrloI6cWwycbXHLWHZqM-V4J0-02zq9uvj-nfsKbluBlOWPnS5rdCjhsgnbbkm4rPWz3qZig2RFdiI7MTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kDZxtnEVCSIqO4CP1g8QvdEXjpLzmLaKN0hHN1LKJUMdK7PuWy2KjGJIjK4XgL4MqtmE88JPmaHDEw7-SU4X_pMWdcbp-XVOECvuRppxT6u2MdMl8oQg7dV2EzIqLhUydpXwgIdV1UnYSAy2pgcMiNDwVYjh4nwZ5Z4YWUv15ia7VrxQPFy2H93hZVwU0NZwTiFbnV1Qw6kX92XnABySNwdZd5zU0LP_fXJ7I7cj2_uCaLxNOG5yy561Fkpq_nkP5eoWn20ucovxsIAfF8AUeXkBiaHIkqsh2115HAkViEC74a9uxzBw8JpUZ2HNUmjII4DX8KnePB1J4XupjukhQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTU9chV8HXV_uoZrr7JjLIXrpO6xI5mhsTS22EWE4V3eU3W09xBiy6OkPBIdgxN5Fy2bpTKoZz4TzEzY8MP2iwgrNUACXcQyeePWBVnN-INMsWq1uU6x_M6AyDT7B67RGXjo5YIUHGg_8jT4Zn7qSJN9W15Ks6MaTqqhdB9bEMvqo6dd77I6rBzEGZ4K44jEJK8hHCVqiGjktewUIgOo4RCcTt1iWSPMkvCy__AIm__i6Xq41XQM8AtGwrT2mUO0-0_FnslQhrfI4u8TzpMRpwmbLyg5tMIWWFwqAO20V0tgEUrlpMN7gR7rkNkfd7jKHLCgkcz_3DtOQjJoEvnVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XS55Nz1_Q658JJww7kRWQ9ZU_hqxGr2_-GpPMLl5fHc5Gl2ZnwaTJQnwAXZgpDt3bUcTVP2rWOD3xYY2xXh-Fq-OzWMcf5Mlq5DuAh6t1D34C23eXvbgR5vGEQ2IekpC82vcYUrFp1vPCoyhKhVC8v5SARZxQSfCSFOUdXWGC6HfFYRkV1TF8iueLgse-ji7NCqWrpSfN8KZSkQfpKNJ8yYUsBATDM-lNDYkPepQH_7uHzsYhPEqBSA5oqK5Y6p48ggANVo29iPeC8Dqb1C3NDgz3tZJ2MvKF5ELLQi_bjZuQqb8Ln91CtCS4RdLNmlSFi43ww8UYDaszur7Wo3O0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVIEzET7aUHonhe2EoIbZiYRvk1Bw9uyv5Mk7jBlIhBafSk11SNpTF3AThaT0ICebzOMWPTsRMqAgUhSfIRL5berq6vplfufHqXD6NUAjVnYr8MjHeezVCMdviITruejl3tzNTAISnA5bI8xX_wuUvEPywV_xLo0TUakctBDRB33poS44cXxNUpo_K8q_q2d1kJD0g-0il5wEdYYMN9chmAOxXW1nTDiu_x5K9P3iPw4i3oL-JR1JO4F4aaQQm7T4iX3Fg44c6Nsi813lNOYoLSYpClwvJmqRzmZFX01fphlwS4dmRKqQw3vEmmP45NDPAd3qW1Jx2_e01HcDOXraw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxIbQ0K_M3-3zRDk8XBh7QbAlDUXXrqQt16F31FG4wsLjViviKRpJ1_HOBATM01ZG61M3lViOffX4-_csriZ0XoEXP1FdlB832PqZR3LySsgCVp2Nh7kuNPwTrcaBCRoHTl39JeGFR9dbr09vb-ZMYSdxDlvlJr-3I_YNOZ2kqN2rMAN_IDkBgW1mIansdXnsTv5PSyCZo3aa7JSAmjN5hw8tshVwnN0ubrtqpjX3tGWQAP2JwKKsQI7avn0Am1l5DeSo1mmh7e55mB6GekmKYFZpza20lgEmeql2Q17O8dpa_cWhy7xtfRtU54WEiavqUEhu_dwWfVvC4C_V8SBsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع پیکر زنده‌یاد اکبر عبدی  عکس: محمدحسن اصلانی @Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/452704" target="_blank">📅 18:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452703">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/580959d445.mp4?token=anWwuLSH2gLCSSgo_l9-Ow4I7_MWH1dhCBtsKgSrxRaOFlXP58CK6puMcQ5Vm_HuA_WLSv_jDKbblTqESuFDbeyWftXqdewAUvEYBmDJKhiaiyr07JryaSBaTcqOKOiYjqrpQITHJkA53-SaDyC9sIU8vGwpN3-fJxzK5-Aa4nYV26yzRlPyMhwE69cf_Rfsnqz9XPxd3TFhOKIWjS5OkplLDjSXpzJMAD7DtwCsHlD_zefk8daBfqjv4g_s4kEmKn7bQVs3kkD1atQV7y1ytAP8B3TdccY0myDW58Nj4rx24sRhZSO_a-rKII5JDzoYnA8SQOdRVObSVhn697Qidw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/580959d445.mp4?token=anWwuLSH2gLCSSgo_l9-Ow4I7_MWH1dhCBtsKgSrxRaOFlXP58CK6puMcQ5Vm_HuA_WLSv_jDKbblTqESuFDbeyWftXqdewAUvEYBmDJKhiaiyr07JryaSBaTcqOKOiYjqrpQITHJkA53-SaDyC9sIU8vGwpN3-fJxzK5-Aa4nYV26yzRlPyMhwE69cf_Rfsnqz9XPxd3TFhOKIWjS5OkplLDjSXpzJMAD7DtwCsHlD_zefk8daBfqjv4g_s4kEmKn7bQVs3kkD1atQV7y1ytAP8B3TdccY0myDW58Nj4rx24sRhZSO_a-rKII5JDzoYnA8SQOdRVObSVhn697Qidw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هرمزی‌ها خطاب به آمریکا: گیر اکری توو تَنگَه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/452703" target="_blank">📅 17:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452702">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ddbf4167.mp4?token=VcB-95Wn2st5RJLzTqZyVft4KorCexpXulMsjdHYUTskHBcI97akmcEDMZI7g8qUuhqP9oR4IE4bjefxNXOqhD5Rk-2dq_j1QIzVv3ZU-Ejd7Apwfy_Lo4nLRlZ7d7STaBObeIcETcoI2h8PS-NU8iQNgO5VFfwkR2aiWFi8xWCNur_7s5sBEBH4UuWCZ2sZYKPWArfWVDRjP2j92lJ1lzf9OKSgS2jKIq37GuF8yIxjlFlJVuR71Ukx08zWb7tsZ-VgkHdg1yw-aNSLOe6SvC7Mud5wev7_AKRfCYQjvFkbOQpzqYvZLUAGJiaYi-dgunSRjuReQAVn8jLfPxUoeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ddbf4167.mp4?token=VcB-95Wn2st5RJLzTqZyVft4KorCexpXulMsjdHYUTskHBcI97akmcEDMZI7g8qUuhqP9oR4IE4bjefxNXOqhD5Rk-2dq_j1QIzVv3ZU-Ejd7Apwfy_Lo4nLRlZ7d7STaBObeIcETcoI2h8PS-NU8iQNgO5VFfwkR2aiWFi8xWCNur_7s5sBEBH4UuWCZ2sZYKPWArfWVDRjP2j92lJ1lzf9OKSgS2jKIq37GuF8yIxjlFlJVuR71Ukx08zWb7tsZ-VgkHdg1yw-aNSLOe6SvC7Mud5wev7_AKRfCYQjvFkbOQpzqYvZLUAGJiaYi-dgunSRjuReQAVn8jLfPxUoeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ‌‌های اینترنشنال به دروغ‌های خودش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/452702" target="_blank">📅 17:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452695">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFM9hIEP5MzpaEWilA8RQ42SFqlK49CPT_wXQjCwl4vSsxTqfO9S1bg8IATa_xnkXvFFoFtrkdbqWiE8hvE2zAYTNy3Hw6hyDd--EisqAnLYg25KRjqDbl9pqjJploJDj1LHrdnPFxrcQ7AYFpBDD5Ij42uTNRpGziAIK7J45yStPrF9BWCnf5F6iG_5uJyVLZQq9w43SftAf9ut6sWKGooRyIRhkVJ7MZG-fyGvDmfGJm2Tb7OU-xQYtsNif-BH6sFIIYRwV87UWv1u2WmHszdRwGmjX24MyyiR6EPPU6P8rYRyZ1t4dX2o59DQx4uD3HHtpW0dZ3n-6BOGrmCtCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuAjm0IblinwRaz6WmPLDFXEQADi6nicw45_wk0c5k2jJmhxFF2-gJrfsdl7mh08TFRH8X4pCCpiki3MJepthpjK8ca-oLd2amESB09WC79nCN3hk2W0i2ZUTJSSwxZkFIBlJKCWBnA8zNZT-OwrT__rTw9eW60EDqGKQw9Ndxvguzymnu9EwC3v39hsvsuuAMJVjoDtUSSNRS969-BnaQRgomtYo-ALAkwHkzlLkQ-LxGTOSsJnRoYpBsa5hAM1htll650t0fKX9BmVOUNdiXLylqEVB5tvJSz09Ju-FbulzNRMMZKrix8qiwdzmXdmlAZqvoa4JHdd-SJ_hmOYNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxiRxmPCH9cZvzaumQi8uSoPMJVxDdecch9l3mkfPFO05RBH2RGeLqf2euZNkFw0DeOpnYClwg6LTYoxaSyecpPzHfpYbnsk2bGhmGWwVNqyeX8GyOhBJbFcfilDnxyFuKNUwuAE_XUFgPEFsxd1H0EHFWcGAglQZO8t8V-V4ctNGXJxnF4ECEz6Dk8StRE3OIObFFakBJuTzQ7Cxa3M_oJKUfOQOTyPEJoO-HyB1axG0bquMDTBM9yPOCylWBVxG9F1oddPUNlflKYWZHJ-jtaBU_fun6vFUXYLsnWbtBc0NBKmSbj1jCEws3lNDGorrDPyVlDH6DXZSDvO4TBz9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVUO5GqF69bV9XMxeFoqNR2Sw-wMkE-8h0zkL6EPtSFxnmBXcBp_xLWCxHh1NSdePEJUpOe8935EBKnAXzHen9LDKzJxfpkvDOT4GVfXfQpveFgVQY_fb5aU9vb5WcJVLWBHQHJc2oxlH__FBHKkCsgvDkEbTSuD_FWu1YkYZzG5uxgQ1dCh1HKw3ZZzTrZqpKzrcvy1_CFVjCE0u_J5-qMf4XzSgFM4Qvnf-oXX0V6mlWygWjRSmBhOEgBliioETGKqZeh0IuQNjiWoc8SBpbQq6le7lQ9f7FLYsIoMfdK9C90_cc8Uc7Rd5f2-A2QYbBQcrsuTaW-4GirZH09swQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_GaIb8mVmHJwzp1KvWtGBjy76q-EkNuUCgiVYknTLGYSiaTiDMETCvPUaSYT1Zm2YypexKq9eSC6O5E5V2UqBxsfY4lXEw_CHNj63F9_gRAh9N76AUhdtYLBDwd2w94hPLRX3Ky9Tp2yIN4uW5yeKCiM3eP6G4Kvf-qVFMQZuzV3mqZq7EWzberOPAf5s7tHg7KudhG7m_yzRbq44QOVEA3R4-m6q5tawlpXNrWp3v5P6T06rHYaZCG8rC2hqNl4RqhjJrQh2aEaX9deCvoTPcT95fjWYPqAsVBX77HjP0pBNqTB0o1V-Rg2PHpIaT3BryfSPSXXym8f_eUV8QdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgaBat__aWkDBEOkYt-0tyAtSCd_U7AfE1XgM6Ng-1pJ42vYSEuolt3wojzsmoZ79EJCSE3rteHxYaYyCcZzF_cybbCyBMJ2BIqOuIFm4RnvyJRLTx3UUm3Gbz9l3DY9i6TaKOER8LGZ330NOmhne6Zn0YmU0TLWTBknLZDb4wRrPYdvQKmhmo1A0-yrvFhrJIV3e06jI9osqD3NDyoUwpnZ049Ep1rS8a2ZJ5uhX4MAzBSBplPil-rU1BQTYydYhShtAohVDHBOuFvdyL6aQsmIV1LjrovSsaNt2UbByFX6QR5FHKT6CTyGEmQ5Ge9JfAxEyXsY254MvGiIj-divg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bxm-iig-NPdpXzWwjleca2cJPiKYe05Ewo3MC3A673YeFkN828U5pYjjHfRBZfd-snTK4VHUiQevzk-UdkmhUgNPZbDymFKFDWnucuRAaTx34u4DXppXjYDgwQUqHgygnnFhWA1ezzMWRP4t2IQ4V1Mx1VMaUsuOTVcKkWyGWsmBtSRfguZ4iDWX6PoWSKPggd-RRiN6kKSolA_E-b93YiJlUkl7r4MKwd7HDwDLK8_Xib10hygSDscAHY8I6qcVNcr5i4PvXEBRwuyed3EAmPRKiTCFhj5vd63I1CyFBTLpMBg2Cft-6uaA8RE_04e5bHBQ2KmteoKoT296hpCioA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور سردار رادان در مرز خسروی
عکاس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/452695" target="_blank">📅 17:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452693">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180f2b60aa.mp4?token=NIGUVtuYbOZz3x7aQhKUb2J51UQCvuVaDgSN99eJXwHquy12VGFpFJk2ftQC97sMR-0sj3uQitdn97h4TzkTS5eCskq1mHjJA-IjpA6NlxdJgfbELzg11TDCq9GMffRNNk8NNwIlkIK7pYkuN02KFpdNQeyNh1kPyuTjgI88EnQ1D5pDj5pnqC4tG4V_NEobzlXqORA4sf0G7kVZhvT4NGv-1i5nDJ5CE2IqY-qk_hnrZ5iyj7vts8Ou1Tp13hXXqKm3J4b_qonQ6s-ReIbVtqut7zAVRXZwa9e5hi0UVugu3a0N0ARoIcaVHNd6KZYHjXOKp-Ezzj3AjxBWPKn5Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180f2b60aa.mp4?token=NIGUVtuYbOZz3x7aQhKUb2J51UQCvuVaDgSN99eJXwHquy12VGFpFJk2ftQC97sMR-0sj3uQitdn97h4TzkTS5eCskq1mHjJA-IjpA6NlxdJgfbELzg11TDCq9GMffRNNk8NNwIlkIK7pYkuN02KFpdNQeyNh1kPyuTjgI88EnQ1D5pDj5pnqC4tG4V_NEobzlXqORA4sf0G7kVZhvT4NGv-1i5nDJ5CE2IqY-qk_hnrZ5iyj7vts8Ou1Tp13hXXqKm3J4b_qonQ6s-ReIbVtqut7zAVRXZwa9e5hi0UVugu3a0N0ARoIcaVHNd6KZYHjXOKp-Ezzj3AjxBWPKn5Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انقلاب برقی‌سازی خطوط ریلی در هند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/452693" target="_blank">📅 16:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452692">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThiL1_6OaHzhVxSh3Ua7eF6YHLVaubR4l319IQ800EZTfQm1oxEgESmE2V7GJJO8SHfFJjjZZcqC4wl1aUsosSMZNdRNAr95jSF1rmIUIBFtsnbRL-SHRx_RLx113ye5KHOGmDFONMH9x2OUoCiOipqdNrwvj_PUrNBR03JNgUeBwqGw7wfhG3J5iAfmMpbU8QgBrJccYsusy1ZXlZfe1W2ViIY0VqBDh0avlf69c-QbXBy8FCs1khB5GC5Fcy6tc498bD5UuJCbP_Z5LPPrgqCu_CzuRi6_VVFhiRAtvyaZOSyMTeI78L8DMIuY0S0Dw_BD4P2wwGIWWLaaK4zJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنادر کویت و عربستان خالی شدند
🔹
پایش‌های ماهواره‌ای از کاهش سرعت بارگیری محموله‌ها در بنادر کویت و عربستان در ۶ ساعت گذشته حکایت دارد.
🔹
تصاویر جدید نیز نشان می‌دهد اسکله‌های نفتی الاحمدی در کویت و جبیل در عربستان تقریباً خالی شده‌اند.
🔹
به‌گفتهٔ یک تحلیل‌گر…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452692" target="_blank">📅 16:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452691">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">از میدان آزادی تا کربلا با پرچم «یالثارات الحسین» به نیابت رهبر شهید ایران
🔹
مصطفی زیبایی نژاد مدیر کل فرهنگی شهرداری تهران: امسال با پرچم‌های «یا لثارات الحسین» میادین شهر تهران و به نیابت و خونخواهی رهبر شهید ایران در اربعین و آیین جاماندگان شرکت خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/452691" target="_blank">📅 16:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452682">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwhP9PK_8AtifsJpSPPbTermaHJp0skTFCuWxMeIAPRUYq_xp9MRYyL_iuAwzmbPlqVMA4807kQ-eVrYr7qNjxX7xSY76KXBtVGTQUjm9_YI4-ofLmi2gjU57Odv4bGANoeA9Zfxa8_U0M-w6geNbi4gXo9V48_WL3S40AVp9VwVHEHxD1yh1Tgg-_2DyHdKzDZXHtvJQTtVzz0nxfyFn4bSGDHTJ-rIQKTA5xn2xYCuOYkHgT_d2zoBmN1SlYLeIdhwfx_YGK-lAlyJjhwnCQWhCIqrsbJieT_yacd6NYaZcfLTofzNo2PdRHAdJnoa_jxfWVbfhL9N9LhN_dJTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/av_VfpEpG1sD_1AYzwtq9u9ARcialJvaE8rK7XVk3cQMpjgVaZrwG5RW6l0pmTZu8EZVFmnoYdJL-v8pHsU_90wPxlfRtAnM8r_kvfsLrjvJQYXbMQNwn01gnaW7faEKvPTgl-Hfx0BtCA_7n12gxZnEavo6IAijpmRSy0cQb5fhFT6MKX4j_OZmwKyFppMtnqxcgfmJZOe-qfdLje839iSSNPBVN-_AB1TqQ7mcsTEEHAJFJ6PZROD3Eljgzxn_a0SPqecEEIgb7FdSjio9lAuG1V7N5jPC_UHNJQ38qZ0Hq0TVVZ60FODkLyRx-V-YSRBhBE9ziRkJXc7rr78k8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/is17PTe9KvRkxyrBQWmfkLz33-PnCK5K43vFziOu7s9Tsp4AVpvlmumkQ556mrUSHD2dBZdIRGlyxsCQWA406Vetvy2LHhFEiBcTjRPtb45nP7guDy-UJGxokYFPiRjJ_glAf0X2I7g9bHGT7AHwG0X4GU34QoJdWUbaaIYf1nKkVBMxaogz-LJfSvrwSLM4lwKhlEincM5QV152_w_1WcL1b7BxTqPFam_vkv0bM-VEVgB63LCAPGi5sVCgjXE-7XyJL4CSWZjEvrX8JlUGA-pR_p6YQZd7fPJgaWl07Kj3wom0isJrookayhzHxOnS3eA6CCvzRkytojUz6hxdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1IaWuA9KIfvplK5H4Hqs0zifx2pAFuDz0OtOys68QB5CE4AgUZs4sXuutIh9F806opjPd2y16mTHIksrtBL-PjsrrAASS1hUsIl8hWYvjsL4rUw_XLEAzfClRFWunpPl-uh5Gh-hXzRlvStO_8wz9_9vsVlhU4bgl9CamPiRB7RdB_mwQkd-c5-B8LtSJ_rduYV3eOynmg7fvIWObbvsQPTRp-kYPAuWMjb7SpCK9ZeGrZcGmP-foKTSVawoz-ygxDVnOIo7F0rdlriSd9mdb_Nrnhy8YZZqdQo5YXeYaAPZQTNAUxPC9lxSiRCUhp061gyfYOGeVAPidBeJCEiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKIgItpGQ3UziCW2lC1m-krix9zY-iu41JYENSwq3TbBqqRiAxA5WsRVi05YLHZmU9w_FgOW7V57pJxnJvjz1F5uJw17YVPSt4IRjO6J-OMR_aidnLlDEoBt300gYDnQF-H2H-y3zhl9oXbuiKYDdDrD2nn28IJr13aP0X0pyXKoNHqStmNvesmPw6KjstQ7O3Sm7gEEe9drXX2pcZLJt2VoIfbtEdq1HVz7t7KJo8HxBdFjJVnEwoLdN5wYZnoPDHq_GnE-Fq3L9deZOCfF4cpbW588fmxnpkRzFNJnJQFK0O3pV9ou0UQhIU63TYXlgON37KE_B9Tb2LloMu41FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WwxK090SLWq12Bp2RxQbWYSf0oldOI_dxVsCkHXLHvAHpB5EEwXkq8r-U_DrAQdPytbkI1DF8_Q6WfzMFLoSjQAHrdBT1zC5_O8amW53bU1zv_JJNBzIR7Fs9kY2N4ryLhkNfhrQg8r809w7atNS5vPd5cok1gUg8prhCLdoF4GE9br_98Tcr7b59agV6P_fj52WPGAMA8YiIw32T7AaUw17hSt2edYHGErr3c0x2pVg2I6R10YvH-v7BlQeGcRyOsyxhu20MfoTTX8rLaLF9qcZP51EEC8CwVaILi0aPoWNcBEKnPF2wnwDLVP31iwgD3XK1D4rhxEa0u-tLDv6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MkWTqb_gTH7RDvvNtkGb7ZKAzTRVVHn8IoUV8dOqzRneJsPbFmjxxWokrhTXQkvafeCBDDgjSR6_FSlnB4L19rxSAuUBzYXWhhjWUmcuKeYKQZR4N5rsfVtW4YM-2y3-t2b2j2l00fvdHFYUqP__WRlrOoD5u2dQma-uTkOrU6Rlof-YdnxvqNmNC6PLrV3bm5N2_OOJCOnYiQG_KW4RMBb6Z3YYj-yOndxbZBu3R4PlXP6r94mWn04WMxc_XfdxAfhCG83emKaBmuQfBf1jDUEmBE0SBnLeA8abvCRFIw3n--tYYlu_1Y7OxlSVD-7SeRLU-to8DcWZFA-PIGwaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sU8p0RpuaqL--UD9ToJw0_BgkKIzUpaDBSOZAeSZXNDHTG3-HV-5HfLX3gZFU1ZtJF2V3_e32gvyhDOUGyEmMKlFuXyB4sKw3WN_cLsR56m5DmDlpMrUFIYp20Txy5cu6B_QFsJrwP4pnvZ95Y3ymqZGUYydwwNtYvUdedrJJbJFLEpEeaaVIVT1ZP1Ux9fHXt6s9Evs3gow9aWkbTWg9DAeJNFL-W480WZnLf4TMZHI1DGAjOlq41qnsGcaxyDiz8BSsD4gAKoymkRJz43ywT1zVg4c-5g6fHvzXY_h649tSgjKtLDCCZOv4ZUblY0w-zCFYGKR-5EPLRtsPzM40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNb5u9_V6ZyyjNgyxkHbFKo_OVJqLhdzzBwXxBxiG7NCNH2iXtqTJaXIkxtCX12Qnbsb4uNc_20QVErObiIiO7iUHDCuCxFkIhzbrJA-BuT9ziKR7r_V26KaOWO2k4ZeCgLqJyqbmBwyA4pmB4RkklzPjNVtvW_EZ1f6JkSNbBV4YAdp8TuqS1MRb_nyVmKDcJHyv4MV6R95qQbSTmLJ0tiAcmPmbbypFc45AYs2sUTbZ5OjTuOs-FfFpBUeO4DgoKEBm7lmOEGUhusiUVGyfR5oeLvLJqpgthoANLgyZSqEWyYm8MhpcyNPCds8RxSTUOoj-azdUmShN7lCL4A8SA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش تصویری محفل شعر شاعران و نویسندگان ایرانی در اربعین به نیابت از رهبر شهید انقلاب</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/452682" target="_blank">📅 16:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452681">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک توسعه صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJsmAjGRY4hzLVAQreMbqBNF1GrDEpx4Atch93od5nOf82PLy4TFb3Q9oaeA4DvDMm7ARxx_wWm4xnKcuAkIKzbS2i9wJFZUzniyJNcxOWwQPJiKardHFP-IVFeIgrmeTKbGsabuDTpykGu7TuxllQ4etyHxdNBSMy83y9AlyWDxpA52TvELrrzV1LfUyDJAOqxyAddxgkOXEdC3wvN24TrNSZOBg-0QXgBda4mKuQ0LiExTm6CG2NwAsaOnXJTZ5-DSKpow3YHRJGsqHcbAAm-JUdEfsAk5glpvdw9UxYcy6MLrSxyBgH1nfdhor9d_hxfnRaHNMj4SCw4klvY1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">↗️
افزایش
حمایت از تولید در بانک توسعه صادرات ایران
🟢
بانک توسعه صادرات ایران در راستای افزایش حمایت از تولید و تقویت بنگاه‌های اقتصادی، عملکرد موفقی را در سه ماه نخست سال ۱۴۰۵ به ثبت رساند
🔹
گشایش اعتبارات اسنادی داخلی این بانک در سه ماهه نخست امسال نسبت به مدت مشابه سال قبل ۲۰ درصد رشد کرد.
🔹
این بانک در سه ماه اول امسال موفق به گشایش اعتبار اسنادی داخلی به مبلغ ۵۶ هزار و ۶۲۷ میلیارد ریال شد.
🔹
این رقم در مدت مشابه سال ۱۴۰۴ معادل ۴۷ هزار و ۱۰۰ میلیارد ریال بوده است.
✅
این رشد نشان‌دهنده عزم جدی بانک توسعه صادرات ایران برای گسترش خدمت‌رسانی به تجار، بازرگانان و فعالان حوزه تولید است.
🔗
مشروح خبر
🟢
سایت
|
تلگرام
|
بله
|
روبیکا
|
اینستاگرام
|
آپارات</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/452681" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452680">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/452680" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452679">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDzIvWZIfZKl8ahqwqlxrdzVYYNPm6F3SsI_wSWMp69A1CIKQgohfPqhOxFd47BW-LIpIu8bhb9masiNFO1Eh_lsMoCvc5RzVMHzQlpMevAPAzb-9fDYFf_XrMtGhFrB5dMCYk9jEdXGaV4DPT4-QM1MApXu1WPUwOzgMhEDXXIoAg3Hxaj_iMu_XBXAIpgLT8SkwgRPvbO2Bgn7fQAhqdxFjqOYFB_FQ3CkHHT7ZqiYJ4hwMatUFs6IYsWp_X6tjISUhqmVYdDThr5z6i_x6kpv9qS1FG2Tq5nVBm2iRFAop6dyr6i_e2AKDs0lBypO2woV77HY9z8rVOcNfeXvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حج و زیارت: تا غروب دیروز، یک میلیون و ۷۰۰ هزار نفر برای حضور در مراسم اربعین در سامانۀ سماح ثبت‌نام کرده‌اند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/452679" target="_blank">📅 16:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452678">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b4cd8f6ff.mp4?token=jCGaGtlJDGdjkroiGiNU7Y-o0HAITZAg5KGuIKL5leFAm-8MQ7Y4RDwdjvZvgIVToJcjNL7xhVJ4cGCVEYBrEBS99roBL779PjO-YRtMBDIyTgz_lazP3bWvk1Z0CJ_HYWTqQVB1LjY-13I-1gc5uetOoTypmx1TWNdCVIh91tk8_A0Wb46QFcpLcnLCa-XaUiqEMs_BCgk87km79WmuFvb4q1CIviASI6YaQ3V8tERRpYWvOdeSgShIxzDXezh_eAlOLjmlgUCdssBT7_4dNMPTaWRkNlcHkb21kMbG9lqltzUD7cAp0BHFLgop3_XxgrpT3ZxBMuJDWpAnG72Xbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b4cd8f6ff.mp4?token=jCGaGtlJDGdjkroiGiNU7Y-o0HAITZAg5KGuIKL5leFAm-8MQ7Y4RDwdjvZvgIVToJcjNL7xhVJ4cGCVEYBrEBS99roBL779PjO-YRtMBDIyTgz_lazP3bWvk1Z0CJ_HYWTqQVB1LjY-13I-1gc5uetOoTypmx1TWNdCVIh91tk8_A0Wb46QFcpLcnLCa-XaUiqEMs_BCgk87km79WmuFvb4q1CIviASI6YaQ3V8tERRpYWvOdeSgShIxzDXezh_eAlOLjmlgUCdssBT7_4dNMPTaWRkNlcHkb21kMbG9lqltzUD7cAp0BHFLgop3_XxgrpT3ZxBMuJDWpAnG72Xbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی: دود غلیظی مناطق وسیعی در اطراف پالایشگاه نفت جازان عربستان را فرا گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/452678" target="_blank">📅 16:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452677">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">۳ محصول جدید لبنی یارانه‌دار شد
🔹
کارگروه امنیت غذایی ۳ محصول جدید شامل شیر بطری یک‌لیتری ۲.۵ درصد چربی، شیر نایلونی ۹۰۰ گرمی ۲.۵ درصد چربی و ماست دبه‌ای ۲ کیلوگرمی ۲.۵ درصد چربی را به فهرست کالاهای یارانۀ لبنیات اضافه کرد.
🔹
با این تصمیم، تعداد اقلام لبنی یارانه‌ای از ۴ به ۷ قلم افزایش یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452677" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452676">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
سپاه: دو نفتکش متخلف با قصد عبور از مسیر ناایمن جنوب تنگۀ هرمز، بر اثر انفجار دچار حریق گسترده شده و متوقف شدند
🔹
ساعتی پیش دو نفتکش متخلف که با فریب ارتش کودک‌کش آمریکا قصد عبور از مسیر خطرناک جنوب تنگۀ هرمز را داشتند، بر اثر انفجار دچار حریق گسترده شده…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/452676" target="_blank">📅 15:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452675">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYQnNXpUiZEPI5fHUKMk-9AUdqH0LdsDjehBOPrk5PGkBXhkXnfPn3odwyOPiw8LoxKJQXMIItf3vJxFPpA3BzsVmV9Mqt2e2TRnGY-0O7njqH7CqnzGwQKbHuvY8zKnKJuIe4kDvqKd59U4SQQmIS76WHOM-PIiCpIrj8lUvv_AyvvV6D1QxTSI2nwIyIqiZ0z0-lEanu6s8v3OADQiUch2Qi3PWJEpYCbAwxk_m1vTM78qJDsU4oQRr7pmNJws0dSLOAhqEyGgJruuOJNlooraMTkGOS354hBkGOfRYKr3h-nEOvPJRTdAFfoLUzDiai3YwVGSkFG8KASg1NzWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد سنگین در جاده‌های مرزی تا ۴۸ ساعت آینده
🔹
راهور فراجا: تردد زائران در مسیرهای منتهی به مرزهای اربعینی به اوج رسیده و این حجم تا ۴۸ ساعت آینده ادامه دارد؛ بیش‌از ۶۰ درصد زائران، مرز مهران را برای خروج از کشور انتخاب کرده‌اند.
🔹
تاکنون تنها ۲۰ نفر از زائران در جاده‌های کشور مصدوم شده‌اند و خوشبختانه هیچ مورد فوتی ناشی از تصادفات در سفرهای اربعین گزارش نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/452675" target="_blank">📅 15:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452668">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPPyWK-p8pAvsroTiqvvrOvHK0qN4pWp7aBJAjSZs5Okd1x8UoVR_vDpHcpg81aHni3izcDBD5zU9qUmGn4GJWMjLIP0JFFDqack8hqMa--KZESWT4nUvQ9RVJbapXGMXCd49SV9D8GPtxGO2hFnfstir-WqGe62zHFTt9cqttvlw-2dGlgzDetLaSHdldVXunTE3qt6A45DvMBv0McJAQk973clr3klQ-2wg6ACnG9VVUVoidF12wycVpfhLaQorJyeC4_A33KEM4ko9QfXGwNX06XpaFTNWG1c8GT574zmTdOEy6-DE8qio_d2ym23Ad8dwwOsWDjFm9kruig33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nraOxyXEE0BDUZAJjwkPzyqAJx6xaM5BbByq2yFW2-MtaitRBHgOJ_2hPQhCD6PaoUTZrOE9K9-zxbsqJpqbhpHm5FqwrrvPG7xoi2yFiX3Vyrkj9hnJx6ALHjK6PpROPY6VQ6raU0-9u7B-tVPCfGBpjRtj7HOffdZW4c4YXulEbplFELch09nTJmCrDcLij-YjNXrtUNo57MH40cdjuNRzwN7eZfar4Tb7ce3Kbzj3Hw-ZRQbRPiVK8uKaVENccfQoLu_OtXsisRqivtUyXFSD0Y2esuL-lyEEojdhW87MBtS3PWR_m7iZkpqV3qTGs_q3YFvZQAFkLBWhgWYVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTG7d30sJGcA4hOp0MA0p_zypW1MSTGtuNv56ia8lUKegsLhcD2qzTEDOClKkzuq6I3m7RpnkmkGEiX5WATOiLAxaCDT4sxrWJfBl-_rotkEY6F5t19StopsS4CcFbGFBRLUNU-VvDZERMnEKX6pUzUdW8qUHHLjZHKvCsYs2kek4A0iKK6solYXxDskxM5g5znaFkwnudUDOeMIBCA8hici7cA7t2IKbq1k1Se3unAPpMfL6P9Du7jkesAcrfSKjldyJmaJYc8poltiNVWA3-RST0EyPzRZwqdpGWeSceomdM6wIcUtRJL5pu7esjQEQoyk2XxuS-BWS04cE20hqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpZ9ErKld7NOezrNcYPnTCSQCwpd8-iqlZLAa4EME7GxC64HXrhT85NJFk9KbbBGByeA3Em7wZz8-0MAE4oRTowvuC72KWXxW4-GwyXqnwTrCkH8MFa2OsLbe5ygtSw_8jqXXT4VP-6T5pHDKkmA6HFBXnq1yXqSw3MQuhYiVyAUx4sUejOcBa0EydGg3x36mXB7zEbbs9Sx4E8SA0shAvlnjiaE5rgfXPcgAHtBc80p-TNbzm6bLKWeTwI5Rtb9Jdc6UG396mZWUV_ax7z2Hdv4A-H36LBcOaC1eAqYCk7rmI0M1VMEEjq3IQ-Cp4DjXxUL1DOo9ru7bQ4N09CddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1agOuVVzmOPrqpGVbFNg5ybLQhRvg9wN6IvypXM3sdnJ3gFNQh5qUoTd7seobn1fjcxKkMDlgy_1lfs3OwnBENfgXRRa8rqoNH3bqltMIJQPxOG9fL-1N8wuN7hlwG8t8YXuZ6ICiqeoP9BTV-siIqUAqpO0jaMkmxm7uKY24F80qbI6ZherWkczNqBYwn2fQHIRAHIGNdWfPNi5GCTSNmRlTm-LzpR0epY1UrWkZXWd4VB-ehoO2hlsYVEU-fuZyJUEtZZUxx3-Frg_mJqapy-wZq0fGwHiXJtxMv0dcY937jAX_GhQkLFIjA2n-s45o5TkSBgYrWkFgPWDxtL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8J9bJNF8-N1iSnUWtugpbBDjwSndXJjtgDfH03WpV7U9kPDopaH1RqHlKazqHpVoud9IAtby2KpkkiT3y4fSNde7ZV27CLlm4NXDWE0RP4rEi_5K8Su-wvBjBym7WDDxGXfc2TbIl1KyPKRyskcmaUj4HNuxJlh4uwXsXXp6-mt6_o1QW8qW0gP2WcC8LFw_RI6ZhlFTh261YLwh3xtBqmX28XVWMtL7oBCkizBSRjv50Y4brbYe4lsYBeDDK6X8-BKLunQBNqQolge7Zr_SCIRc7V3kkpn3V-t6Xpu0X6BMYOLapyrlmuHBmJBw7b-VznKTuo9R-HpazdYfJFeTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFFkSi4jsmwpd0F3ceSb_rnmRWTm3uVZG-ml_-yBGhuJyo-nZ8yMKiPdWDSALr3V7deSofKQ5971dVBjD11zeXc_m9QEgXmWfvM4fR96Yacxjmvyos6q7V9KHwWFMMANcaajsXWTGQewxGzPxeuckmsQH6TUqsHwPIJkDjDQiK8M3XumGLgSSmTSsq6_lTUQJ-mrbNZE_XmyYM2XYBtnFLn8RFkzvJpfv_JLWodzi5eeTkjxBuD4A8cDgPOaCIpBMhpEJ260Nw0wvvQ5K8-Wk5e-LI-htZPLZCbzrXXmRypAzVeLuoXjV185GuSjUtd2Umt29YfDBmcgeoFhLQ4YpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
میزبانی گرم عراقی‌ها از زائران ایرانی در منذریه
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/452668" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452667">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY0zL2r-0wPeFN874mpx-e_D7KHXp1Tf3MnCQA5nIgNIGNk2A0B9tpJbZF33pc3CN5AjPjBVwjCXsTIOaP1vBhyegdj0M1UWh6b1Kg9tVoHqgJmY1mL7-ksntGJq-cjYpLQaogZ7O1OgXvrGM_sklgAYv9mpXy2o7R3UsagPhx96YYzVxh6mAVlTzzhbgPsPi49tgKjcadVstJTP2GB_FU1d_a9we3BS3WyLc9DLgCybKLG-p69A3UeB1H8d4rEBwiiMu6_P3VWF1Gn2EFdT0E56wpNXpFbSaPvggAqAZ-5zsp0VlnfKYlrOzKkBvC3M4Tx01b2ysIgPrj12MgWybQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداری خوزستان: ظرفیت پارکینگ‌های مرز چذابه به ۱۰۰ هکتار افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452667" target="_blank">📅 15:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452666">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896bc839db.mp4?token=Gvzm9klzkSDFDkgYfAH-Pc_pFl9-B1LaKXiuWBwc5-xZpNQFL465Q9kJpHAOvNLYYW48YEa1mMTiIJ6GWjQTCqjttfBw_6yEkqFlrfdta1_f7vHxqsIgMpgAVmHw6OUSKDKgS6gvPwmdjyet3HjCA9Dsxn1NTMEBdYbwWJzxVpw34lEWP0kFkDQoP3xYGpgqRuLoDhDO559YHJ-qv_SBmt-IqSxY3LZC6xqq55A57MopdRuxUhRoHywuh810OmrZYK9UKsQGpFKDS0jy7SK6m0bw-pqcFKaQZPnLzwKrdEDt3xusPXog8hcXMs3fftXV1S3psz3kn0jDfFmwz81zDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896bc839db.mp4?token=Gvzm9klzkSDFDkgYfAH-Pc_pFl9-B1LaKXiuWBwc5-xZpNQFL465Q9kJpHAOvNLYYW48YEa1mMTiIJ6GWjQTCqjttfBw_6yEkqFlrfdta1_f7vHxqsIgMpgAVmHw6OUSKDKgS6gvPwmdjyet3HjCA9Dsxn1NTMEBdYbwWJzxVpw34lEWP0kFkDQoP3xYGpgqRuLoDhDO559YHJ-qv_SBmt-IqSxY3LZC6xqq55A57MopdRuxUhRoHywuh810OmrZYK9UKsQGpFKDS0jy7SK6m0bw-pqcFKaQZPnLzwKrdEDt3xusPXog8hcXMs3fftXV1S3psz3kn0jDfFmwz81zDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تشییع پیکر زنده‌یاد اکبر عبدی  عکس: محمدحسن اصلانی @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452666" target="_blank">📅 15:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452665">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exIoewVM3rP-RLrnAKfBcWQafM31bWfMxg3Vr5Z9TbM5NlIyQJeHcm6UW5hoZzTQimgopNbT3dx9GrWqc0kyJo16CMXZLriU4fCDNFX5Ku6A1kMCqOnS07miPJj7S0NqDrKU7-4XpnkfWv7cMaYiZMcmkPxThMeFnf4Z0G7aEQBVI9BGupEPYwMA_pGmtaUOXWj8VzFd-R66Q3QMa1dgA6lNnc-BBmax4fZBe_isMm5pVGM5evhBqQosTuvr8iAJG1g4RKtU8Vd95W6MzalU23fEy68TN75cQN403K7IJ4xyy9nol-veiOzku3HV_ei-IHtsRQp-sdgH7V5399qomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس از وقوع یک حادثهٔ دریایی در جنوب دریای سرخ خبر می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/452665" target="_blank">📅 14:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452664">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c97f68de8.mp4?token=XaKzszxjLh7T0C_humIv2qQIc1MQA1b4nDJoe-p6kTaUBufGGIWmzHVh42hjZA_yl9-1CZlue3Bf5M6MevHPp0s7dVhd6Ev8p0ex9nnaqwrZ1w_s_5IvXcyEPiOYDWmEuK16djgEKx2yDPs6ACb9iaPXRnFhoYj3E-jP3Kju2qEE33FHureA0xyOLxyTChCOQ7GFdimFPqcX99LU8IaAvKhDKrycpg2gMgjADtpZZNXkcaHk2Y7BJgwMt2KXDp3LpLbzSuo9oMkKwissly2oAWABufQQvhWniW-lBr8jDxzZIowX9wCCpQRBjX8l-tQgX1BSJobXitntgWCxLoJzNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c97f68de8.mp4?token=XaKzszxjLh7T0C_humIv2qQIc1MQA1b4nDJoe-p6kTaUBufGGIWmzHVh42hjZA_yl9-1CZlue3Bf5M6MevHPp0s7dVhd6Ev8p0ex9nnaqwrZ1w_s_5IvXcyEPiOYDWmEuK16djgEKx2yDPs6ACb9iaPXRnFhoYj3E-jP3Kju2qEE33FHureA0xyOLxyTChCOQ7GFdimFPqcX99LU8IaAvKhDKrycpg2gMgjADtpZZNXkcaHk2Y7BJgwMt2KXDp3LpLbzSuo9oMkKwissly2oAWABufQQvhWniW-lBr8jDxzZIowX9wCCpQRBjX8l-tQgX1BSJobXitntgWCxLoJzNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف‌قراردادن کشتی ترکیه‌ای توسط روسیه
🔹
یک کشتی باری تحت مدیریت یک شرکت ترکیه‌ای در نزدیکی منطقهٔ اودسا در سواحل دریای سیاه اوکراین هدف حملهٔ یک پهپاد روسی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/452664" target="_blank">📅 14:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452663">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzAT0bFWWD4KixtC2gzT_v0sQCJzhm_2buSNQXCm8d3WThD63CwdhU0Bikyh9JyyUlFVfFJtjJq_cbXxTWtF1QDlpP44xsHQBgOPnmzYrL84xu12mPyGI58HBPACOWASsxEPQH0G6ID7S3D6c774uuCOdZwky9QNdi0wHQ0n2DI1YA1Wfa6MsEuQM8-yzcIssPdIvIAWd89MvuqkFpz_rPayreTkGtaRhLYe1-mJmZsjV8KZIrPM578syIxlnNUrQH_BvURzMCxNtiZyzCJl0PNry2U0CNV2c4jP6svkOZbydKFJvnhKlR36Vtgtc6a13v9AZ3C0J87ceFuENCFApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنادر کویت و عربستان خالی شدند
🔹
پایش‌های ماهواره‌ای از کاهش سرعت بارگیری محموله‌ها در بنادر کویت و عربستان در ۶ ساعت گذشته حکایت دارد.
🔹
تصاویر جدید نیز نشان می‌دهد اسکله‌های نفتی الاحمدی در کویت و جبیل در عربستان تقریباً خالی شده‌اند.
🔹
به‌گفتهٔ یک تحلیل‌گر تصاویر ماهواره‌ای، اسکله‌ها به‌تدریج خلوت‌تر شده‌اند و تعداد کشتی‌های بارگیری‌شده‌ای هم روزبه‌روز کمتر می‌شود.
🔸
این وضعیت پس از حملات یمن به تأسیسات نفتی آرامکو و بندر ینبع و همچنین حملات ایران به مراکز پشتیبانی آمریکا در کویت مشاهده شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/452663" target="_blank">📅 14:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452662">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1b66c659.mp4?token=dQ6tQHKm7Nc8SVXAYA26NO_LZF8d8czpoBFrrmnYW1sFtTDKFnRT2dHiWxjav8ORnuWlZy-aOTiPkcE-Ny4ZdLCbWqMcX0wPZdjuvS935Ub6l9CufcEWRP106ZECPwXeDWYJOewigE0DSdqP7fZVTlAmfqoyBRe6O5KRd9owJSCpw2oAwOywkbyjcEfpkhu2Yng3LnEA0iFJhYatLculXwuiRklnAYv6QSn1P_KRTTNXeUnjD0kapWedUgaU5jrbiPLDx32FjENrHKEa6KB5vZMxyzyRAbpeS6OyA9B1yUswhqFtAcR9q-q_5P-aqjpR1SlNhcOLrRGiwj7tIbqj2CBaTPvkLLxA9gqB9kOVCB4Globhl4Al6oMT082KWGtfWKPjKkR-SNlf29wkJ7iDN6v3tRDlEe7P4iuZlBPgD-vE_h_nTArwPIstXA499rYFI02cZEh9AoxjzaGfGRPYv_3q4DQSaX1kW3Sw3naiMciwBZVxrG5xhZlIMRroF_JAfnzk_Ml_NICneiyNO2CpM-LHn9Jaqjr6BLtr3SiqXgLcIAhtLqgzwDYbNbyIRiXT6IShG8SZYPRPwwBuauSoikCZ_TQUwL8lvCXZFWZ1mirtn2mS9Lgt7lGdEvwqjEuW2M-MkY8Pkl_dvrewzC6b-biF6pkUL5wzR5aIrSqIQGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1b66c659.mp4?token=dQ6tQHKm7Nc8SVXAYA26NO_LZF8d8czpoBFrrmnYW1sFtTDKFnRT2dHiWxjav8ORnuWlZy-aOTiPkcE-Ny4ZdLCbWqMcX0wPZdjuvS935Ub6l9CufcEWRP106ZECPwXeDWYJOewigE0DSdqP7fZVTlAmfqoyBRe6O5KRd9owJSCpw2oAwOywkbyjcEfpkhu2Yng3LnEA0iFJhYatLculXwuiRklnAYv6QSn1P_KRTTNXeUnjD0kapWedUgaU5jrbiPLDx32FjENrHKEa6KB5vZMxyzyRAbpeS6OyA9B1yUswhqFtAcR9q-q_5P-aqjpR1SlNhcOLrRGiwj7tIbqj2CBaTPvkLLxA9gqB9kOVCB4Globhl4Al6oMT082KWGtfWKPjKkR-SNlf29wkJ7iDN6v3tRDlEe7P4iuZlBPgD-vE_h_nTArwPIstXA499rYFI02cZEh9AoxjzaGfGRPYv_3q4DQSaX1kW3Sw3naiMciwBZVxrG5xhZlIMRroF_JAfnzk_Ml_NICneiyNO2CpM-LHn9Jaqjr6BLtr3SiqXgLcIAhtLqgzwDYbNbyIRiXT6IShG8SZYPRPwwBuauSoikCZ_TQUwL8lvCXZFWZ1mirtn2mS9Lgt7lGdEvwqjEuW2M-MkY8Pkl_dvrewzC6b-biF6pkUL5wzR5aIrSqIQGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان کشتی‌های متوقف‌شده در تنگهٔ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/452662" target="_blank">📅 14:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452661">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7f0c9700.mp4?token=tyLFXzDvhpOWSGzqKkyGgYI0nd9nxdEwDBu2uzHk1TmECMSziWRYoIcDpDLjCJPXFfoVcFHoz2586P68Gj3jUa_w0TJem2neKTunkyq00HoxZYBKCZ0bUGuH-95DPWMHbFt5Zq-FId04fSz_OgYC5NbzO70QOIWskge02yKMwred_BQ2XQ4-oZFRHoRV1tg4FH7IjomMXBpSevSbw7O0sRfoLE4RNme5h6AZSJgic6Qc4H60HPXlVuD2I62lvVhFuEOsFucv2MKNzvYN6YWVmMhjUScbe9I0m4xyMeGajF5tLd0vcoGbW4MstBrepT00hBTyM5z_iSCd2_4sDkw4Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7f0c9700.mp4?token=tyLFXzDvhpOWSGzqKkyGgYI0nd9nxdEwDBu2uzHk1TmECMSziWRYoIcDpDLjCJPXFfoVcFHoz2586P68Gj3jUa_w0TJem2neKTunkyq00HoxZYBKCZ0bUGuH-95DPWMHbFt5Zq-FId04fSz_OgYC5NbzO70QOIWskge02yKMwred_BQ2XQ4-oZFRHoRV1tg4FH7IjomMXBpSevSbw7O0sRfoLE4RNme5h6AZSJgic6Qc4H60HPXlVuD2I62lvVhFuEOsFucv2MKNzvYN6YWVmMhjUScbe9I0m4xyMeGajF5tLd0vcoGbW4MstBrepT00hBTyM5z_iSCd2_4sDkw4Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برق صرفه‌جویی‌شده راهی جنوب می‌شود
🔹
در پی ثبت پویش حذف خاموشی برق در
هرمزگان، خوزستان، بوشهر و سیستان‌ و بلوچستان
، مطالبه‌ای عمومی مطرح شده است که با توجه به گرمای شدید این مناطق، حتی در صورت افزایش چنددقیقه‌ای خاموشی در سایر استان‌ها، برق این چهار استان قطع نشود؛ مطالبه‌ای که
وزیر نیرو
نیز در واکنش به آن اعلام کرده برق صرفه‌جویی‌شده در دیگر نقاط کشور به مناطق جنوبی اختصاص می‌یابد.
@Farsnews_My
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/452661" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452660">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bfba51605.mp4?token=qMtry7gfnniVnEilkmAjKepCuUVKyDRruGxHpn-f-B7AvQIHOToXbAwQA_pzayTf_4ggKTGgHlSTRf-Uy6vBJP0fXOCDHh3EggXoeU2VVTudVIPePq8pZf_rcl58eljguylA1hi2gMbGFSPrDrfR7MbPAv7drdujcgVe20BppXq8ZpK1gDx7YuWHo3JBWTJHHpRntLnJ_3fCmVakMGSnPStwZLR1EwuPp5xNUSe9jqv8X5_RGd7rwfj-MpcB7zQ-ra4jM2JxkEeqJ7c6EDl3SpAU4IRUbkYUUrZ_ERTHCiwR_ihcEc15TH4SznjcU0u5jGReEoDWFBW6MIOq1oNMjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bfba51605.mp4?token=qMtry7gfnniVnEilkmAjKepCuUVKyDRruGxHpn-f-B7AvQIHOToXbAwQA_pzayTf_4ggKTGgHlSTRf-Uy6vBJP0fXOCDHh3EggXoeU2VVTudVIPePq8pZf_rcl58eljguylA1hi2gMbGFSPrDrfR7MbPAv7drdujcgVe20BppXq8ZpK1gDx7YuWHo3JBWTJHHpRntLnJ_3fCmVakMGSnPStwZLR1EwuPp5xNUSe9jqv8X5_RGd7rwfj-MpcB7zQ-ra4jM2JxkEeqJ7c6EDl3SpAU4IRUbkYUUrZ_ERTHCiwR_ihcEc15TH4SznjcU0u5jGReEoDWFBW6MIOq1oNMjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در جلسۀ علنی وبیناری امروز مجلس، کلیات لایحۀ مقابله با جنایت بین‌المللی با ۱۷۰ رای موافق تصویب شد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/452660" target="_blank">📅 14:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452659">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/johQJLECn_hjRcgXwZFaC4g7f6rU9xMUd1BExVyyF524ovElwCRqQGvMDk6gbKgGX_HjgbOlkEW-ZShiCK-RKoTmexJrXLhlvSTbOWwlgaxr2T6w06328ebfym7WAXGAuqlEdF0IrwhAVEpsSOqbpGDtQotXgQt6Gss7HnR5PCrol2q_Tapy7BrmPD7IFjRXrxf78UUiiJtOxSIqq0uXN4w2FErFRyL9M8IpwvT_piGYNfMz8i-KC8Hn94TB9PkyTuyKu25B23Qlrc9IbfVW4dubwD4jfDdWqOGgHRrVG50vg_p4IvZZlYC9cQYvFOaN0PfJ2nz_BqGbZkHR_7P_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: مجازی‌شدن مدارس از مهر شایعه است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452659" target="_blank">📅 14:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452658">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXCNmkTJ3QyaKHXnYwqRuUDi601yUHG8YGB4NHR1dui8z873XpRx5gi3tRUybAhaEQRdcK_WeAvoOLmOE32ozWPcFVGGgfOyWPzDu12HB-vmJnuVsXK6C0pXciiiCNVvZ-e6tMh8hmpXeZ7XzOI1sDjmvnB_4m7fSaoQ-1JSic_Q1gy0UIbn3jwDGzM-X5EsKq-ZttfACUimod60v_TPYHuSlkg3R5I8bXfzXXRBhLnU-WaL8qQ_kqD545UYmU7BzwTsWbBwo4k-Jhe1CvyKtl19CYgLjVaUA7AJqOGTeSLHtiEpuw-OsIx0q1SJ7qNZi5Uf1DQvXsfmzaSceRCY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باند فروش دینار جعلی متلاشی شد
🔹
پلیس آگاهی تهران از دستگیری اعضای یک باند چهار نفره خبر داد که با فروش دینار جعلی از زائران اربعین کلاهبرداری می‌کردند.
🔹
در بازرسی از مخفیگاه متهمان، ۵ هزار و ۳۵۰ قطعه دینار جعلی کشف شد.
🔹
پلیس از زائران خواست ارز مورد نیاز خود را فقط از بانک‌ها و صرافی‌های مجاز تهیه کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/452658" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452657">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3d6a73b6f.mp4?token=RHavkvbtEhzmdiNeCxal_BBkVSm3asAj51jvpRz_-taXsuVjp83jPWL4qwrALzY5wfguJq9s1oNsj0W8ApwnX1ppP3gjDq4Ag5OwOjL5Yy71esEN61BPmXPa0EdXrR0TB3JnTeE2EBRHVnJDSw9S7UtDSefKdpM2ivnoB4DPhXn6kLFD4ebYsBPAqJd-TlEJuOmu_053KIBBKxJrcPFziqqHtZOvDcJJH47kgyrRF3fS70liKBQ6b3ytvI1ZhW-JYf5XEjLwoZdw4z8mLiPxi0FkdBF4r0_-9Mj7-ajl-SZJnw8eMt8l15LUttb59ruMiDTonkCGWaKIqKHV1s82IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3d6a73b6f.mp4?token=RHavkvbtEhzmdiNeCxal_BBkVSm3asAj51jvpRz_-taXsuVjp83jPWL4qwrALzY5wfguJq9s1oNsj0W8ApwnX1ppP3gjDq4Ag5OwOjL5Yy71esEN61BPmXPa0EdXrR0TB3JnTeE2EBRHVnJDSw9S7UtDSefKdpM2ivnoB4DPhXn6kLFD4ebYsBPAqJd-TlEJuOmu_053KIBBKxJrcPFziqqHtZOvDcJJH47kgyrRF3fS70liKBQ6b3ytvI1ZhW-JYf5XEjLwoZdw4z8mLiPxi0FkdBF4r0_-9Mj7-ajl-SZJnw8eMt8l15LUttb59ruMiDTonkCGWaKIqKHV1s82IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیکزاد: نظامات حاکم بر تنگۀ هرمز به شرایط قبل از جنگ بازنخواهد گشت
🔹
نایب‌رئیس مجلس: هر نقطه‌ای که مبداء تجاوز به کشور و خاک ما باشد، قطعاً هدف مشروع نیروهای مسلح ما خواهد بود و اقدام نابخردانه دولت اوکراین بی‌جواب نخواهد ماند.
🔹
به رئیس‌جمهور متوهم آمریکا هم توصیه می‌کنیم این پنبه را از گوش خود بیرون کند و تا قبل از اینکه شکستی سنگین‌تر از شکست قبلی را تجربه کند، منطقه‌ای که هزاران سال است محل زندگی ما و نیاکان ما بوده را ترک کند.
🔹
مردم آمریکا پیش از آنکه سربازان آمریکایی با تابوت به کشورشان بازگردند، رئیس‌جمهور سفاک خود را کنترل کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/452657" target="_blank">📅 14:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452656">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXHW0dN3gKLgqmolphpkoI-HF7aDp2RsZjVHx2pk7qpy-QvUEuaa3krSI_Cje-wbW6rZLqMo5vFxt5iDiBGJslBil2AiXWDZ5F5M-x_Y-u8PFNanmLZwEqvio6kCsq4SbkTQZdsgvq5tD2HdovwurHJaBb2yFxICBjzpKowkdTmFKc98Fd-bCAsrYbRiK2STNi8tnqpnkG_73Mw5dLntG7NucUw_R3x84ctzaoKnbfoDpcBks56pp7FKWo8OTd9HRzuOeubLQ-1tJhtBLX54L7_80bGmUCF7GLUyPR6yRPSNB3SeLMsmAPcoN4F9aZp1aIj1Yc4jYWXDvOQiA4rmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت دست پیمانکار را از حقوق کارمندان شرکتی کوتاه کرد
🔹
رئیس سازمان اداری و استخدامی: دولت شیوۀ پرداخت حقوق کارکنان شرکتی را تغییر می‌دهد و از این پس حقوق، حق بیمه و مالیات این کارکنان به‌صورت مستقیم از سوی دستگاه‌های اجرایی پرداخت خواهد شد.
🔹
با اجرای این طرح، سود شرکت‌های پیمانکاری از حدود ۱۰ درصد به حداکثر ۳ درصد کاهش می‌یابد و نقش آن‌ها صرفاً به تأمین نیرو و مدیریت قرارداد محدود خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/452656" target="_blank">📅 13:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452655">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6768242559.mp4?token=meyBhbb9WnY4ec8bj_x1yCLIICCx05Oz809OZ5tWXv1bF23Trkfyr-YR-R1Lx7jgjJd8yeIWmDfzPSzjIYr66C-woMrl9uDO3AWetsRRYpoEu3IFAkY6reRsXFD7B0cUiO0-Vtcs1wdrSfiGEsTQ0MdrSAMIrX_PbcAxQf-hww_THgw_8uUnTLJLvFndDweOTEJ7d7RLTuDrT-uwF-9vayah2-X3bQ2pCthSbW_H36OTXe8WspGk1RIitGpl8hwjIRKKG8aJXcCkoULoCvh_LFSGldPU0752zL44WwOkGGEtRHGVRodVtitFj7b4HifELsW92XozZSej1GD1lrrLH3ZZXJR0kkFalS6-kv_q5btnZBh6KLt-ftWDG3Y3Aj4yQqsA51bLzjyPJBXuUo75NjQJsVe9ZvE2OxMM4HPlflOEibgtm8BpXUQbp22MfgBzstcXV7W-DcH58ltJUyE6WgFEm7qpiISFwYRBNZdz7aMZacfzXPzQRHuxEiXhX0XbekpQuGWiHbyFOBQMmv2JxFsPlZyztzk1z_WfzkAccnhPPpjpjyJynJak8Tgc4ky7hUzYSjX7XHct15a6oL6eF5lnzuJVRH31Va4RmIGMbL2n0LQLaFt0cdjei6dgwLl4d2Bp5giOwX4Lt21HT_KEiXNQrak75pha0QpgO9FnZnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6768242559.mp4?token=meyBhbb9WnY4ec8bj_x1yCLIICCx05Oz809OZ5tWXv1bF23Trkfyr-YR-R1Lx7jgjJd8yeIWmDfzPSzjIYr66C-woMrl9uDO3AWetsRRYpoEu3IFAkY6reRsXFD7B0cUiO0-Vtcs1wdrSfiGEsTQ0MdrSAMIrX_PbcAxQf-hww_THgw_8uUnTLJLvFndDweOTEJ7d7RLTuDrT-uwF-9vayah2-X3bQ2pCthSbW_H36OTXe8WspGk1RIitGpl8hwjIRKKG8aJXcCkoULoCvh_LFSGldPU0752zL44WwOkGGEtRHGVRodVtitFj7b4HifELsW92XozZSej1GD1lrrLH3ZZXJR0kkFalS6-kv_q5btnZBh6KLt-ftWDG3Y3Aj4yQqsA51bLzjyPJBXuUo75NjQJsVe9ZvE2OxMM4HPlflOEibgtm8BpXUQbp22MfgBzstcXV7W-DcH58ltJUyE6WgFEm7qpiISFwYRBNZdz7aMZacfzXPzQRHuxEiXhX0XbekpQuGWiHbyFOBQMmv2JxFsPlZyztzk1z_WfzkAccnhPPpjpjyJynJak8Tgc4ky7hUzYSjX7XHct15a6oL6eF5lnzuJVRH31Va4RmIGMbL2n0LQLaFt0cdjei6dgwLl4d2Bp5giOwX4Lt21HT_KEiXNQrak75pha0QpgO9FnZnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دست‌نوشتۀ ۴۰ سال پیش رهبر شهید
انقلاب
🔹
پس از گذشت قریب به ۴ دهه، دست‌نوشته‌ای از حضرت آیت‌الله شهید خامنه‌ای که در جریان بازدید تاریخی از بیمارستان صحرایی حضرت علی‌بن‌ابیطالب(ع) به یادگار نگاشته شده بود، برای نخستین‌بار منتشر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/452655" target="_blank">📅 13:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452648">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aA_TKECl6ErXAsCEHGWbD5hZM1ZCQytnoLsdbiYu5wp2ZRkX4fSVJTSbMhIkY5xD48sxlOtC8Er6VQlNOyinH038lWPC1kcg7i6V56OhLSKRKECLsyTUZNXhh0SlkEZ3o9Qr11ZrfnJFtoMBmFIsbkrxaOKKYZ-v8BfK9L7gA4DbNqiZi4ut_3Mf3hMaYBl9ci83gC9Ef2dTloaOnSmKxvd5r3jwDASW0FTgMkCs55QkBGKHDvg8u9xlrWXgX0hvzfWXxYEfEitVe6r9_vKSBj6lNr-L6aNJe--5ueFpJpxCRhJZNJnBj-aJb3mgNxXMFXqzFaYx4vxUsKS63uS15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLNd2geuJ5AAihI26dRyOxWmxCLGgJTziV9hKrPlaMT9kEQdahsNoosSEnI-Xr9knA8jzD-_IhiguYa5LY0O7Eni5ED9tWXTR7ck64XNiTPnPwIjEEEdZXY5bHdDo_tivHkZhndlSSXCIXIEk_wmfyBqyOyCIo0jGEiRbmOPXK3v5m3MfMcLsZOl623NzNbYEnyAL7l1Vzoj0W_fjQ2SRUwow8PMjW6WYG93L5ktbwxG62C7N3RmwAFIB-Bpx-jpSpHRsyso4pc-pHGvM9lRY3wuQSL8o2fQrcskUNZdmBGi8gscoPaWMlcQeYdY5htmXJZsK5obs0x-dd59LNF5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uM-O5x4KqQajnaIqcYHHESOfzsPrp9oIL6aRxEIV0j-XwMlJ9Azk6K3Zd7fzvNH2DY6ivOawQ6QnbQK-e-jeOK79DwOQ1L44Io6CZ33p4GBspsVQdVRllQAbpv-534b3jaHjeDOUXqO4HcK4C4mJzpaT0PHUAWTpdsUHNY6jG8mHN2WEgdMPiMzZLHqQ4ooNk9Ml1tIe-6MLNu9fvIYqgkNHkNBQ8KtzZ_qtNbs4OUzjF_goZxtUeY9Q7_l00Q4SVzTXwpE9U4NTZq35cyz64rP2rcTR7J2JfZ4WZEjKYFR3AVQI5MNqGAyxkcQcYj7Mg_exqOZUt3ihiHW0ryXZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nhjcj5HGrGvValF8kzq200Af4Au_wmbe3JhlekWSnZXU-NFcmXtbDjm_GB-uJz_Qd5uIu5XEqjBYeC-1TRORjMfmqWmrKkLxGV_p_kjIIs17FRR7jMChmKhY5KjUbXkOnUpEmWP3c3k1TQGVtDu3ta8k0SS9XT5WgoFvVbihCdKi7rfQsq4TiJ8z4uMGBW5C_de21CRkZxdsYIuJ6ywJ8d9f6vKESnpOKgOdPFr0LzBjH1KL8Dgl0IZL4bEJ67NiOdu4Vy4oyl3tmFtC0_0TXpImM7ctiz6i3nliznDDt-ULMTAO8MzMmJX4EKM5z7X3wjDf29zFPTQXLhUmBoO7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovZSYBAq7SDBqBwcFHxBjBePJrgXmHC_8QdR7LpoyiTZP_gCkUtWkPXAJRdcJx_jz4fRN-7G7gsw_0c-P1Xp7nRO0s4IT2EvaS_WSdJkkUKvYwzSLkGnHGzMXDF5mr8Oi18ImQCaPUdC29jcVjOyiIutuGkAKyRhsn2Gso-6pLo50YMi1QEI_oq3JuhEx8urpw0eM0HnylE7-edd14VsAt1klrj3RtnKNfYFtmEwqva_4xKDqsn0SCoHXG1A2Ar3h-81JTqAQplsm5tldQPBzjYCVOCbRe5PI2LSO-aeYiMHy41GytH6_lmdKxHSYpcu76v9BPdEtB0WyYDquCGeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sveer2u4gtGaTuxLtzZ1lN_Sv0hQ5lVi1rN-x2PeTUlNuDoHx528mp7tfOshiWYiwDpL7KUZvg9TZco929Ms5mQ5Nz5JdzoVJWDLmH9VVahXnLKWlYpKgd6enj-idWcSZ9B1QApaZydlSwQZ8us78Al4HtW1ULlPGhrB6ez4C0nSkE3WOvV3wuvBanYyfcT8dx8kBlS5xcduuVcwuacmsamSZNqDjFVjztl9JVJW1NjhaZ1B1mnCObuxSlNyJxjQ9Bahtpq6H6vCCH-l1J8OGzDrVIVtbTTVbSu20qiUgGrqYZ5AIt9W8_p6PBhIr1UnUydBLQfktQyfl8_lmQhCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lotxqaCEhDuWi7IT5zr845eM9qJUHtLXywWUopiSsQTtzqKctoQWB4uh_S77SAVZlxvkklsILX76QzkpDjEJpuy2ArvbbwTF5SBjw0_7zQkqUuL-MzsTpKIyK38YPtO5yBEOlF-essfCSt8SfcePIPdAyUo1fOxEYXmMofTuM6r29ZR9_wY7rMFF7Q_EBKdrWiJeDynMlAYw30BAf1mNhj7ak5JwcpGeJvgU9kAHvVBs4CTzcz8XBhOLKhcigexfwK93ExlrdKvF2Wptl7bXNHGqsSrwjSUlsjO3mnT47CIt_uWuZYd4FrcxNBgFQ68mHZYUBS9zCunc1jrSYUB6Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
تشییع پیکر عمواکبر سینمای ایران از مقابل تالار وحدت به‌سمت خانهٔ ابدی  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/452648" target="_blank">📅 13:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452647">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMoMs6lVNgiaC7hFU8NDIXkxl7bGJeQkqasV_3YfUxt1uGQndotGkd1dtIyzOHImeRBkBoXmGC1tLk8oYKaB-9dET6ig8JmnnKYfOrT461ezhFnmBSKjhb8jIjA290CjHdBd3xJrW-Epmo3c3s_LX7HNHbPOOWKyVqrAEJ6_GX7F1kmGE2dDHH3mvQUI4P3WVlwbFdJzGoG7AkvOLqgvUx-BjdSo8OK9spi1rCHTdpopKK_YI2DY8_egeQcZCagk_MMKcIK-sRWVESmlMH3bpzicfW63PxFbKnK03asK5Al27HI6MGrydz7rWTkuG8_e8TzLRaczMLFqaownYBnpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
خضریان، عضو کمیسیون امنیت ملی مجلس در مناطق مرزی جنوب کشور: جولانی بداند اگر بخواهد وارد درگیری با حزب‌الله لبنان شود، مسیر آزادسازی سوریه برای نیروهای مقاومت تسریع خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452647" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452646">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vd2k-xhgxm5pRF0x_i8brdmyDHFwsUBIKo82vXQJM5XARCC8sUVRxeR0pQEDmy5Gle39mWHmhFoQYlITLtWYo_9rOyLSm5DMEDmXQAITI4uJ251SYm0CEiZqx4NhL-QRRrZQBu48yLmQ2tRDD_h_Soz_MENvwT_WCCRCJr9GMxt0sbLpqwF7HpQ-PaiPY3iWTVEcmtHhWfdqQ94Q570KwenZhRDdCwYlobbjjJIbGOEmUC9062intsw3ATTg1ZSt5bIpRxVhT0XqEc1OD9R39tNLTkgr_osVdafLzt_yhcTqO3k_5UTYx3s1i5qd_l57bEl1fIIZRdViwA0au1ZJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروهای مسلح یمن: یک پهپاد ترکیه‌ای را سرنگون کردیم
🔹
سخنگوی نیروهای مسلح یمن: موفق به سرنگون‌کردن یک پهپاد شناسایی مسلح ساخت ترکیه به‌نام «بیرقدار آکینجی» متعلق به دشمن سعودی شدیم.
🔹
این هواپیما در حال انجام عملیات خصمانه در آسمان استان الجوف بود. این هواپیما با سلاح مناسب و با توفیق الهی سرنگون شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/452646" target="_blank">📅 13:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452645">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg7mFfIwCNyR3JZ2ZjqjMmDm9tH6ftR44XRSXssfz2hk7uRMzPPjB0epx1IaTusyVUpE6NoC7O4OgUPeQ1lsDgkMqFvv31YwGqEZo5PdZqElTuQqhMogcWtPYGC8vJfU6-lfQCwhhX-d7YIw4EqLG-FnLWPoVdlpblZPSuzROrBCr67i1N_CA5dTJxNZGeOvN3aKbBf2Y3fBkDijJj4UCAAuCPmVeFk3Lj3o9kIWQtSr9Jyg811j0WpLAzEENL-fOFEvewAreeQfN_P2nZhpHsBPkU1DjbDwkh4k6LkFoW1bNDgWQ8wjOqP1p3kvOE7o35RKDuZLuEBfvvkHbMrxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جنوب ایران چشم‌انتظار همدلی جامعه سلامت»
🥼
🩺
از کلیه کارکنان و فعالان حوزه سلامت دعوت می شود تا در پویش سراسری اعزام داوطلبانه جامعه سلامت به مناطق جنگ‌زده جنوب کشور همراه ما باشند.
ثبت نام از طریق لینک زیر
👇
🌐
https://survey.porsline.ir/s/VoIeBbe8
🏥
حضور شما می‌تواند مرهمی بر درد هم‌وطنانی باشد که در این روزهای سخت، چشم‌انتظار خدمت صادقانه فرزندان جامعه سلامت هستند.
📍
شما هم به این پویش ملی بپیوندید
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/452645" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452644">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxAv2S5i6sufsSB7s-qRNDkSJBOsBoXlmJZy5xZ1S8v7NA5KyKfkt7B_rguGO8Lu0UsCEDeHmyWzn9QgtUxwul7fxdt1vAfdHc51aTT3rRwlr4uJWM410hCbmNJS9wuvgeOdMlhO6_PWtNupm_GoNIE4DRiV-AwtPHOJQvKolVHvDuk_-oSnmadp5M16Kz4w-UFjRxZCrgFPvGQQ-4-n7BNNYCQMIRcWu_IZp4seBd2bDU1mjKKSqdEqsSDuBuCE5WA46ozdOn031wr15fnXjL-TCgoAou0EJ652e_lTK4KakcrOck0gzp3cTIf9tgoM2hN-eFAag_p_BI6jwQ8KGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود شورای رقابت به قراردادهای مبهم خودروسازان
🔹
شورای رقابت خودروسازان را ملزم کرد در قراردادها و فراخوان‌های ثبت‌نام، تفاوت «پیش‌فروش» و «مشارکت در تولید» را شفاف اعلام کنند.
🔹
براساس بخشنامهٔ جدید، شرکت‌ها باید صراحتا بنویسند قراردادهای مشارکت در تولید مشمول مصوبۀ ۴۷۳ شورای رقابت نیستند.
مصوبه ۴۷۳ چیست؟
🔸
طبق این مصوبه اگر بخشی از قیمت خودرو هنگام ثبت‌نام پرداخت شده باشد، افزایش قیمت ناشی از تورم نباید به آن بخشِ پرداخت‌شده تعلق بگیرد و افزایش قیمت فقط برای مبلغ باقی‌مانده محاسبه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/452644" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452643">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba5bda3f7.mp4?token=S2A3sf6RjcnScNQRbejdNNsaGQ1wa8plr94kNq-se7loxC9Sxz_th3CXi3_2QiZQ4trywS93suyjRfMQje0ZXBf5skd6X58TNHnx7gdeJ8T4N8frxD0MIdZ2iXmPe0ypltrGuri6QWIC8Ufr9a3V35q7vbU5sMZFvQ5TRBZrOt8CZT3KmYFjVeNF2zE6L_gI7_o9IfloQmCWTwT3lwgZBJLToUozF5dOzE0IilMtpUCavv_Zkkt1xgk38CBTvkIAQdV0NmlWEsW_3c2wj6ctxwxL5HNwR4qHIHSyV4X2i32FCy9raoahVm_kT1AQI68xwwqO8YAax_KgyAcxoXA2KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba5bda3f7.mp4?token=S2A3sf6RjcnScNQRbejdNNsaGQ1wa8plr94kNq-se7loxC9Sxz_th3CXi3_2QiZQ4trywS93suyjRfMQje0ZXBf5skd6X58TNHnx7gdeJ8T4N8frxD0MIdZ2iXmPe0ypltrGuri6QWIC8Ufr9a3V35q7vbU5sMZFvQ5TRBZrOt8CZT3KmYFjVeNF2zE6L_gI7_o9IfloQmCWTwT3lwgZBJLToUozF5dOzE0IilMtpUCavv_Zkkt1xgk38CBTvkIAQdV0NmlWEsW_3c2wj6ctxwxL5HNwR4qHIHSyV4X2i32FCy9raoahVm_kT1AQI68xwwqO8YAax_KgyAcxoXA2KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای در قم با آیت‌الله سبحانی دیدار و گفت‌وگو کرد
🔹
رئیس قوه‌قضائیه در این دیدار دربارهٔ مسائل منجر به انباشت پرونده‌های قضایی گفت: نیازمند کمک‌ها و ابتکارات حقوقی و فقهی حوزه‌علمیه در موضوع تأخیر تأدیه‌ها و خسارت‌های ناشی از دیرکرد انجام تعهدات هستیم…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/452643" target="_blank">📅 13:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452642">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfOphL-YQDR03yQzUgNbzel--u__AMhwy-bIlyGS_ImB3hfGWlhwYwToNoXfv3G3b9uatWc6CMnv00euhBqVEuISQqhYmYh8t5va27qaq58CUz4BjtNMceALLattUrofP0Vp4GL-l39xJvdv0DO0TyJKuEuJP79DkidsXSPUN_44TtDLJRktN-LfNyd3ZtjgP53JxJydEKtzW2gEaRjeTE_-rZPl5xc3D9lH5ysljtTey87GUcjie0eNcgRZlQP1KjYR82V75_lhl8RusQ5OKlJkuhmvJKe-RafsEcrwwcVmKHnNYu-GtGV0MdB9ectAYqj0OWGzVRYIi5kAbBoG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراه من، همراه زائران اربعین با مجموعه‌ای از خدمات دیجیتال
🔹
همراه اول همزمان با ارائه بسته‌های ویژه رومینگ اربعین، مجموعه‌ای از خدمات دیجیتال موردنیاز زائران را نیز در اپلیکیشن «همراه من» ارائه کرد.
🔹
ارائه خدماتی همچون خرید ارز ویژه اربعین، استعلام وضعیت گذرنامه، استعلام و پرداخت خلافی خودرو، استعلام وضعیت گواهینامه، پرداخت عوارض آزادراهی، خرید انواع بیمه، خرید بلیت هواپیما و رزرو اقامتگاه بخشی از مجموعه سرویس‌های دیجیتال در نظر گرفته شده برای متقاضیان است.
🔹
متقاضیان سفر اربعین می‌توانند از امروز و همزمان با شروع سفرها، با مراجعه به اپلیکیشن «
همراه من
» و ورود به بخش خدمات اربعین، از خدمات دیجیتال ویژه طراحی شده توسط همراه اول بهره‌مند شوند.
http://mci.ir/-S36MND
@mcinews</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/452642" target="_blank">📅 13:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452641">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e834c6b9.mp4?token=Dzn7R0hc1Et_ejcSUmkJdgBu1_gdFv2EehIclIXlkk7tsptz1ougZGQHlEBAJcrhExo3f-vDA-VvY-CYbpWabpEB_l4zTomGn-TH41-H1y4AkFQEbaN5EQ0TnU8kTpcx2eR6WjOGzOEOzbd80DKzW58JjqR5w93Ognd3b5_7j_T_XHMytTARnv4FBNr7QBtdGjsdSXD9sBrQNt4qA6VxhEr-50fiPlpSLEo51ym_BICueEZyysowpDAXqRbejHh2qdHUXajeTqjbAL3DwVcsdHxJ55mzzZb0kwkPWL41DCI9FoO_9XwBE00Icb5Fn6PFCqZByomo0h9RF8uMyt563Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e834c6b9.mp4?token=Dzn7R0hc1Et_ejcSUmkJdgBu1_gdFv2EehIclIXlkk7tsptz1ougZGQHlEBAJcrhExo3f-vDA-VvY-CYbpWabpEB_l4zTomGn-TH41-H1y4AkFQEbaN5EQ0TnU8kTpcx2eR6WjOGzOEOzbd80DKzW58JjqR5w93Ognd3b5_7j_T_XHMytTARnv4FBNr7QBtdGjsdSXD9sBrQNt4qA6VxhEr-50fiPlpSLEo51ym_BICueEZyysowpDAXqRbejHh2qdHUXajeTqjbAL3DwVcsdHxJ55mzzZb0kwkPWL41DCI9FoO_9XwBE00Icb5Fn6PFCqZByomo0h9RF8uMyt563Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
#تماشا_کنید
💎
تسهیلات
طرح کارنو بانک تجارت
ابزاری ویژه برای حمایت از کارکنان شرکت‌ها
🎯
سبدی از خدمات متنوع اعتباری برای نیازهای گوناگون
🔗
تا سقف ۲ میلیارد و ۴۵۰ میلیون تومان تأمین مالی
📌
📞
برای اطلاعات بیشتر به شعب بانک تجارت مراجعه کرده و یا با مرکز ارتباط مشتریان این بانک به شماره ۱۵۵۴ تماس بگیرید.
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/452641" target="_blank">📅 13:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452640">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/452640" target="_blank">📅 13:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452639">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQuRQ47MTq0pgoFr141AFDy5D4fSw8eEFfBLexkZP-PBIPG1ixWqyn7FzyQgDyXtJN8JU0jY0le9nyFNI9iolbaFku0zjZo9uN4a13VK0qojqsCQ4BBoh97bpPVGy25mmQvplt4-GR3uz3FPrnbi1P4W6J3PH06djSPHeSBDuWeAQgmxM95JKS_QwJCR-3eWiv-NUSyBUF3QlaUk4AcEQq2n2BbWQbAX5dgHUz5ZofH2WXIWdg8v9RFUeZ2Q4rbvhWLWQRKFoVw0Nl6xBd4Cs4lUV-XIvz0ScXiAlV0Lsn52zvG_HYKWJ-4OZfoGc9AYwmmDQq9aHA4CbNyVdc6Jdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به ۵ میلیون برگشت
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۰۸ هزار واحدی به ۵ میلیون و ۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/452639" target="_blank">📅 12:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452638">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b23046f2.mp4?token=R3PomfF2hlgFyaOIZT7GnWvmKLM9PvtbKA-2msUqqkegMV82lNh3u-UIA7bwjXmT2ZbMh8F_73957y_Py5-K3ii_RvWIn9J5PV-dkw8IgmwPmEUr3-AXEIBAt4hfCpKTu6VIIYCRL3-sqFv-uaHe548dhgCFHiX1ohcXszGXn01HysFtgyWU0uHjgyLwAGKDlFl9DZaK2r36waq3EdwIjj1AviMlIRUVIN07LUu3ccqdJU3K0VQnHYCTTbFrfXXTlNlwyuBkTcrkkX00gCtP9BZXKHB_5fFgXjTsoYm3OWdjjz-DNBr88m_Kjr4BhrzBO7DZWf5gMbsWuhEFgFB2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b23046f2.mp4?token=R3PomfF2hlgFyaOIZT7GnWvmKLM9PvtbKA-2msUqqkegMV82lNh3u-UIA7bwjXmT2ZbMh8F_73957y_Py5-K3ii_RvWIn9J5PV-dkw8IgmwPmEUr3-AXEIBAt4hfCpKTu6VIIYCRL3-sqFv-uaHe548dhgCFHiX1ohcXszGXn01HysFtgyWU0uHjgyLwAGKDlFl9DZaK2r36waq3EdwIjj1AviMlIRUVIN07LUu3ccqdJU3K0VQnHYCTTbFrfXXTlNlwyuBkTcrkkX00gCtP9BZXKHB_5fFgXjTsoYm3OWdjjz-DNBr88m_Kjr4BhrzBO7DZWf5gMbsWuhEFgFB2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعهٔ الموت جهانی شد
🔹
مدیرکل ثبت آثار طبیعی وزارت میراث‌فرهنگی: استحکامات نظامی ۷ قلعهٔ الموت در قزوین که بیش‌از ۱۱۰۰ سال قدمت دارد، امروز با رأی مثبت داوران یونسکو ثبت جهانی شد.  این پرونده شامل مکان‌های زیر بود:
🔹
قلعهٔ الموت، مرکز فرمانروایی نزاریان
🔹
لمسر،…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/452638" target="_blank">📅 12:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452637">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf00e58bb.mp4?token=AzRnv7WT7JFDmWfrs5LDCey6iMgtZLQxNZmC4lALnoLbYptV3yiuPxOqe1dKzQUPyrFUR-gXN9hT68SDcp5ikaqxKuR7vocIeFGEN0_ZnWZmwdo1S6QQUx3pnB1s0YdCdQM939PcAEcVe_A4liy3JYjkQrXI8GEBX-rJ4fR8jhohWrAnjrm4fEIoj0fAhIOi0RnlGqpU0tnRu7gE7MB6_U63jcHT-Gqqqi1AagBeq0A9R4B-gMwgmTEMxRCaq6FBtlXQjA6D9iGvDa_rCF_Q0kzT2LZwrgBXnTOv7cplcmdaTsjy0bet18XyjOH8MPWpXvF2k8HbPSmT0j6w40f0LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf00e58bb.mp4?token=AzRnv7WT7JFDmWfrs5LDCey6iMgtZLQxNZmC4lALnoLbYptV3yiuPxOqe1dKzQUPyrFUR-gXN9hT68SDcp5ikaqxKuR7vocIeFGEN0_ZnWZmwdo1S6QQUx3pnB1s0YdCdQM939PcAEcVe_A4liy3JYjkQrXI8GEBX-rJ4fR8jhohWrAnjrm4fEIoj0fAhIOi0RnlGqpU0tnRu7gE7MB6_U63jcHT-Gqqqi1AagBeq0A9R4B-gMwgmTEMxRCaq6FBtlXQjA6D9iGvDa_rCF_Q0kzT2LZwrgBXnTOv7cplcmdaTsjy0bet18XyjOH8MPWpXvF2k8HbPSmT0j6w40f0LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تراکم بالای خودروها در پارکینگ مرز شلمچه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452637" target="_blank">📅 12:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452636">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ماجرای نامهٔ شبانهٔ وزیر کار دربارهٔ تأمین اجتماعی چه بود؟
🔹
انتشار نامه‌ای از وزیر کار به وزارت اقتصاد از لایحهٔ «ایجاد نظام جدید تأمین اجتماعی» پرده برداشت که ابعاد آن، نگرانی‌های عمیقی را در جامعهٔ کارگری و بازنشستگان ایجاد کرده؛ به‌ویژه آنکه این لایحه…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/452636" target="_blank">📅 11:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452635">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcg-3zpEYCFDwDBao8UHi3dHQYunw_lQWtX7xABwNI8uJVBhkZa1vjgx0LO12_BvoK5TXBVan1hmBPYqzyKJQk7B3LPQEITHkhenzSAyWJXhHxGK_5gUhXuOGebKIVKBKganGv5tzE4lQ-F2ArkEhxM172kfg3xwxXtpc2rOya4nL9BWVucDGiMInJgaLEPFvnKcPU9G0MUlh0GGq4y2gG2bf0sf0q_KyUhkM694UL0bih_vpcY1dGChiZzjNcihXZf6vEs16l-I1j3VB0a1JEQuoW-3QVUZwBfMybL2PuIv5w7SxRQl82uaOTjVsF_mk7Da8fOIxLld7u-TbQBGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاکی ایران بعد از ۵۰ سال مدال گرفت
🔹
تیم ملی هاکی ۵ نفرۀ پسران زیر ۱۸ سال، در  رده‌بندی قهرمانی آسیا با شکست بنگلادش موفق شد نخستین مدال برنز تاریخ ایران در تاریخ ۵۴ سالۀ فدراسیون را به ارمغان آورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452635" target="_blank">📅 11:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452634">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plAoq7eXIDboCZ67CQSQ7DPDrHFDJaK0e3ZCX_yrcXPtaKMUnnQKqi2aXQDhOMtL6eGMk_iHng7521AXw9hr9tur-I5_pW6Se0WuiTtZRlTMqGCG5_lAjQVgA93UZJ-dWyAFQ7qc22UCflBgPzN-DyDouLmiXIBh1b3Tm6ikRW1UiGGmG3Qe5-zCS-_kUl0-7itY-MeEEM58grYKif4JDyQS-bQjB3A0-fdPynh4N1DPCGH7c7u5MPC0VFXgKsOgkcZsJSU1yHF8jAtTce9fiNFew45VTRq9p6t6OJbEZVjN9F13OWuoLEHs2XGMVMLPqvfm4dqmKnMtAbHz712SNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهداری کرمانشاه: از ابتدای محرم تاکنون ۱۷۴ هزار زائر از مرز خسروی تردد داشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/452634" target="_blank">📅 11:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452633">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTy9pWzz_aZ2mOrTsHMA0QfKwVAC7jExBFe_LkAiqvGRo5sfDh5L9sTzcRE_HGMPmlfDXvbe3ZttmaX8JIGBIQxoCLv8wi7a_ZUKGV_BNTz2FipTDsfsbOLNczd3jmfcftQoQ5JYHzddS_r5aioM0gSIp6cSYmfEKscGMGpF1HfZFy24XUR7poRhi6nnvhl2i51HDTecbS-rwu2xNRbAdMsd3xV6lz4bm2PgbTkLb1-JHmbv1VMH85hcjwQwRPUXkL3CP6FXUd8_d9aKa6Wexp6hFdMWtFu6zq87vvYhG-oUN9-Vp_Avww_xFcYCj2TmxR8FAAu-scUYAgH1iCK2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعهٔ الموت جهانی شد
🔹
مدیرکل ثبت آثار طبیعی وزارت میراث‌فرهنگی: استحکامات نظامی ۷ قلعهٔ الموت در قزوین که بیش‌از ۱۱۰۰ سال قدمت دارد، امروز با رأی مثبت داوران یونسکو ثبت جهانی شد.
این پرونده شامل مکان‌های زیر بود:
🔹
قلعهٔ الموت، مرکز فرمانروایی نزاریان
🔹
لمسر، بزرگ‌ترین قلعهٔ و اقامتگاه زمستانی نایب‌الحکومه
🔹
نویذرشاه، آخرین سنگر مقاومت در برابر مغولان
🔹
قلعه‌های شمس‌کلایه، شیرکوه، ایلان و قسطین‌ لار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452633" target="_blank">📅 11:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452632">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارهای کنترل‌شده در بندرعباس و قشم
🔹
استانداری هرمزگان: درپی خنثی‌سازی مهمات عمل‌نکردهٔ حملات اخیر، احتمال شنیدن صدای انفجار در بندرعباس و قشم وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/452632" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452631">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7gNc8CypRIh3tVf_YRCiILoAhlEwJSULbVtjpYduM_3MJcZ8YuvLaYaRU3W8Lcv02wIxKfM3LH9EEBjCfnHxtuRv32-E158bD-aALzz7_1inKJjK9H2kKzD1EcB4lsBfoELjmcq3SimcL4aZoLwmqCeIF3rC8HjbOq-7QJmn5yFz60RH3Ci2wb6cvQK62T3_e4sESDZuIUtBOHP4rUby9uNQt9u7pU_vmWZDRFqBeHzfIKfuslzl5CAaefJN4k-l4t-UgsxbavMPdedGTnHn7qOINCvWQkVDu0IVEvx7ofTibkEtYk49Qz4EICHE4f4WRMQQ8Am5jo8DBLpeSkUew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬅️
درکنار ۱۱۰ شعبه‌ منتخب در سراسر کشور
⭐️
بانک شهر ارز اربعین زائران را در مرزهای مهران، شلمچه و ترمینال سلام فرودگاه امام‌خمینی(ره) تأمین می‌کند
🔻
همزمان با آغاز سفرهای اربعین حسینی، بانک شهر با استقرار گیشه‌های خدمات بانکی در مرزهای مهران، شلمچه و ترمینال سلام فرودگاه بین‌المللی امام خمینی (ره)، ارائه خدمات ارزی و بانکی به زائران را آغاز کرده است.
🔺
به گزارش روابط عمومی بانک شهر، بانک شهر در راستای تسهیل فرآیند دریافت ارز اربعین و ارائه خدمات مورد نیاز زائران، گیشه‌های ویژه خود را در مرزهای مهران و شلمچه و همچنین ترمینال سلام فرودگاه بین‌المللی امام خمینی (ره) راه‌اندازی کرده است.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/452631" target="_blank">📅 11:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452630">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21a433f13e.mp4?token=LVC0NJUki8lTdsRmGKMLRtJAAcnveJY3mfHDB_UDlrpmJz8WnTUgChe8z59goFKLbN9ofauSEX3PMaA2wRbtL_Bw40UmvA4ckNo2-M58NWZ-z1ofG71ThxwNUP48TuvoLGcogpf7TtIFeY4lGQGPu_6qQaTFn-RCEnfi45OUhIa6kQZ2CZDqWbxfxoYb6nHC6NWJvB1b_vrgq8jYnDKJlp6dZ2h-Ex4ObwtJtuI1XhbC1rE_Ai1CUiVKYeuGBhwr7nf-Ln-Fd2sc5J6128P378vyOihjsQsfjL3LlKhsDAFMd29Nihc8Ekkk0o8mRsb7XcJd4QReIgct7TPQVF0tuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21a433f13e.mp4?token=LVC0NJUki8lTdsRmGKMLRtJAAcnveJY3mfHDB_UDlrpmJz8WnTUgChe8z59goFKLbN9ofauSEX3PMaA2wRbtL_Bw40UmvA4ckNo2-M58NWZ-z1ofG71ThxwNUP48TuvoLGcogpf7TtIFeY4lGQGPu_6qQaTFn-RCEnfi45OUhIa6kQZ2CZDqWbxfxoYb6nHC6NWJvB1b_vrgq8jYnDKJlp6dZ2h-Ex4ObwtJtuI1XhbC1rE_Ai1CUiVKYeuGBhwr7nf-Ln-Fd2sc5J6128P378vyOihjsQsfjL3LlKhsDAFMd29Nihc8Ekkk0o8mRsb7XcJd4QReIgct7TPQVF0tuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
خرید اقساطی کالا و خدمات، حالا ساده‌تر و سریع‌تر از همیشه!
💳
با کارت رفاهی متصل به اوراق گام بانک رفاه، اگر واجد شرایط باشید می‌توانید تا ۵۰۰ میلیون تومان اعتبار خرید دریافت کنید و به‌صورت اقساطی، کالا و خدمات موردنیازتان را تهیه کنید.
📱
فقط کافی است نئوبانک فرا رفاه را نصب کنید و درخواست کارت رفاهی خود را به‌صورت آنلاین ثبت کنید.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/452630" target="_blank">📅 11:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452629">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/452629" target="_blank">📅 11:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452628">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mb5HwjpcFipgpRvAID5KQn-KWjoOLL7eRN0hTuilAdvlxEjNJ-KS2G-JMWNsR5qFRvhOovrdw6f242DcBVItjkAiXhXtFgeRcFw8kGBCFt4vnWcWaQy440sPj1OcUXAhXFcCY-ZEgGD0UGRuAxxYlPbImlT7c5m_B8MLHS8yLZERMUPybuDsmwHciiZJQKsp1LKnh5WUWUboWAZCCqFBcaWTzFN3-RS18dfJMHHnq1DRC7_T8_8jvTbcFIIJl25untyrBk7V7GOEpV0EnjsKer6HKFEjkrgBZ9MOaRTICs1VsAglfhjhet_csBZPzyrlLCBLYozwJDwR-ajd_9QrlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زائران اربعین گردوغبار را این‌طور از بدن خارج کنند
🔹
اعتمادی، کارشناس هلال‌احمر: زائران با حل‌کردن یک قاشق مرباخوری نمک در یک لیتر آب، یک محلول آب‌نمک رقیق تهیه کنند و با آن غرغره کنند یا از راه سوراخ‌های بینی وارد کرده و از دهان خارج کنند تا میزان زیادی از گرد و غبار و آلاینده‌ها شسته شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/452628" target="_blank">📅 11:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452627">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/452627" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452626">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a30fb503.mp4?token=vFUzlFT9po4aPY5M6-XRTl9CDst1Ez_q3shodGBqd5jo3bJv_woBhD7pd4Lfpw7YTSeodSgVE-jQ8L0grnONnbKVsfTbx8d4zyqQLIqmfq2PldMWKl2lbZF5utJbR3EZxfyTytiSa9K1Raq6lW_uyB5rn5qShZ2m2Iy4p8R3A3McQSyfu-BC6tQkvflh1exxMqz78azk9F_Wwh6ZxLDGHM_mGL8DTdng7fQRo8qsfmTghMzEg_3rVA7bLJfhlmYrXjkuD-Zu4gcuFpkIs4TzyxXTcBzKd9OOVfOBgg4TofDnBj2PPn8tPMCBqgfs92s9DDfWvjHkqNNl9X-Phb8e6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a30fb503.mp4?token=vFUzlFT9po4aPY5M6-XRTl9CDst1Ez_q3shodGBqd5jo3bJv_woBhD7pd4Lfpw7YTSeodSgVE-jQ8L0grnONnbKVsfTbx8d4zyqQLIqmfq2PldMWKl2lbZF5utJbR3EZxfyTytiSa9K1Raq6lW_uyB5rn5qShZ2m2Iy4p8R3A3McQSyfu-BC6tQkvflh1exxMqz78azk9F_Wwh6ZxLDGHM_mGL8DTdng7fQRo8qsfmTghMzEg_3rVA7bLJfhlmYrXjkuD-Zu4gcuFpkIs4TzyxXTcBzKd9OOVfOBgg4TofDnBj2PPn8tPMCBqgfs92s9DDfWvjHkqNNl9X-Phb8e6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت کودکان لامردی از بمب‌ بارانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/452626" target="_blank">📅 10:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452625">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خنثی‌سازی مهمات عمل‌‌نکرده در پاکدشت
🔹
فرماندار پاکدشت: درپی خنثی‌سازی مهمات عمل‌نکرده تا ساعت ۱۲ امروز، احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/452625" target="_blank">📅 10:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452623">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osEm8G7TFkwFdpBs_yBM9ZSds4qp4xrQYSRPTYLQbDjaw4pTTPcua4sm8Ml8WN9NAZyuM4doMf6ITEF7bo4VXs6iBO52OIeKlKGeicKTBVJjs6t3rVK74It3a4JzFvC7t4ps3F71UlpV4Ye_Wol6Crjdul4SL8U9cByr1cfxgGaEyoXZZhkZF2wNuBP_Qc-Yy2Escff4itFEFdqZL_xqyP1xbRabDHdLOX6Irk7XkJrXWyYWeW8p62XECQ9a57cc_J1_OmwBLJ8e9GVpAq7zwivwur4zfDF7sPO_IFHlV4d0_cXYXpxae8PiejzdXCL6mwkRB06JI4zczj9MO97HrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسهٔ کابینهٔ نتانیاهو به زیرزمین منتقل شد
🔹
رسانه‌های صهیونیستی گزارش کردند نشست کابینهٔ این رژیم که قرار است امروز برگزار شود، به دستور مقام‌های امنیتی به «یک محل امن زیرزمینی» منتقل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452623" target="_blank">📅 10:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452622">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_G0dnyBsrhiiXZKajXH510_gOKG5eTwXWXBMhuWkYt2nWlUvqJaFrNMqWXnk-H9rXmgcgIJhznZCcCjrdGY1D9LCsOfFHE7qCdUa0m1-x6sNu4ppNC1crhsHQvFpym-UX2lIJWtoNfEEXXMnRJlagD1E8CnCRTnECr5d2cht15iacKt0RX9OUeE9n6389m7cSN-Xiefmzz82IvlpEWRvP-ljTcNMgNtv1P-lmrbYf8kaTwpZGoTLXeIHN7oG9qEtPHps8EjtvdKDq09Lvg9fObleuYhFFT9-Mb-N-gxqb2cWHcZkJVmbpH5VTNfVEek1KX1NWhzEMF_ArP0gr7fug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست پُر ایران برای گرفتن سهم محیط‌زیست از تنگهٔ هرمز
🔹
سازمان حفاظت محیط‌زیست اعلام کرد با توجه به عبور سالانه بیش‌از ۵۰ هزار کشتی و نفتکش از تنگهٔ هرمز و نقش آن‌ها در آلودگی خلیج فارس، نظام‌نامه‌ای برای اخذ هزینهٔ خدمات و خسارات محیط‌زیستی تدوین و برای تصویب به دولت ارسال شده است.
🔹
براساس این طرح و با استناد به کنوانسیون حقوق دریاها، در صورت نقض اصل «عبور بی‌ضرر» و ایجاد تهدید برای محیط‌زیست، ایران می‌تواند متناسب با نوع کشتی، میزان بار، سوابق دریانوردی و سابقهٔ آلودگی زیست‌محیطی از شناورهای عبوری عوارض دریافت کند.
🔹
به‌گفتهٔ مسئولان، خلیج فارس به‌دلیل نیمه‌بسته‌بودن، توان خودپالایی پایینی دارد و تعویض کامل آب آن ۳ تا ۵ سال زمان می‌برد؛ ازاین‌رو آلودگی ناشی از تردد گستردهٔ شناورها، فعالیت‌های نفتی و حوادث دریایی، تهدیدی جدی برای این اکوسیستم به‌شمار می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/452622" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452621">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اداره‌های مازندران فردا هم تعطیل شد
🔹
استانداری مازندران: تمامی اداره‌ای دولتی، نهادهای عمومی غیردولتی و مراکز آموزشی به‌استثنای مراکز امدادی و دستگاه‌های خدمات‌رسان، فردا به‌دلیل تداوم موج گرما و ضرورت مدیریت مصرف انرژی تعطیل است.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452621" target="_blank">📅 10:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452620">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c464d4aa.mp4?token=uSEC2wxaPHKzOLab-MQgt_TD3CGqZZu0NQWCQrMgvoaIqXgauuhl3iKVujbsGAGHgXAyLPwVF4Q1G8NfcSU8Z4Co9JuSF5WyiyszgvULr1LsZT2RyKnwAuyRjSLvK-pNy8FVdU-hYkhyOS6zcGm8QlbMAiB--HKVQjy2OZM3mWCONzDCbNu4nt4-Mgk2jggrILa8_yunKBJHevkNdmcRjDwAy-5LLL3e3aaCOzwAJASk6kwjMl-RuCd7xkypHxctme2wjM7nqSdvXXqJgGDHG1njU353HxtHShXnVbLeWBYRaJ6S-8aACGfNlj6Wz3-Du0GxmIpWRf1omIuuVdG9qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c464d4aa.mp4?token=uSEC2wxaPHKzOLab-MQgt_TD3CGqZZu0NQWCQrMgvoaIqXgauuhl3iKVujbsGAGHgXAyLPwVF4Q1G8NfcSU8Z4Co9JuSF5WyiyszgvULr1LsZT2RyKnwAuyRjSLvK-pNy8FVdU-hYkhyOS6zcGm8QlbMAiB--HKVQjy2OZM3mWCONzDCbNu4nt4-Mgk2jggrILa8_yunKBJHevkNdmcRjDwAy-5LLL3e3aaCOzwAJASk6kwjMl-RuCd7xkypHxctme2wjM7nqSdvXXqJgGDHG1njU353HxtHShXnVbLeWBYRaJ6S-8aACGfNlj6Wz3-Du0GxmIpWRf1omIuuVdG9qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامهٔ نماز میت بر پیکر اکبر عبدی  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/452620" target="_blank">📅 10:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452619">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25eda9b8f.mp4?token=ZMSOIjdog7qE-tht_A8bzqO0KBjjxGIpNKFrsvZqbX3RT4B8KmxZFD7EZEFMcWC4YPwK6bWqIQjyeyESIh0i6NSLYQTm3ZpqkjRe405RaCn_sPhEF21WWYq1zZSJzXKIK_OoTisPczLUs1BRbaccRDHLDVZ-X7J4zUbHx8u6UwjNWaYCnALSqds7zcbXYPurxE4TH_xeyBOj4mo6_SY1kn6cVtgkNt6MjdcV2sWizBs0C0d1x-8OqYdVhyp3ERDZHdducIlgdne61NmvNFcdmD3BH_9cB1g4xSkYvgY5oIbdx38j1XXIM8aYqfMFpQXv4O9DWbAtWN_XIuiR0lxeNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25eda9b8f.mp4?token=ZMSOIjdog7qE-tht_A8bzqO0KBjjxGIpNKFrsvZqbX3RT4B8KmxZFD7EZEFMcWC4YPwK6bWqIQjyeyESIh0i6NSLYQTm3ZpqkjRe405RaCn_sPhEF21WWYq1zZSJzXKIK_OoTisPczLUs1BRbaccRDHLDVZ-X7J4zUbHx8u6UwjNWaYCnALSqds7zcbXYPurxE4TH_xeyBOj4mo6_SY1kn6cVtgkNt6MjdcV2sWizBs0C0d1x-8OqYdVhyp3ERDZHdducIlgdne61NmvNFcdmD3BH_9cB1g4xSkYvgY5oIbdx38j1XXIM8aYqfMFpQXv4O9DWbAtWN_XIuiR0lxeNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ده‌نمکی: اکبر عبدی حتی در بیمارستان هم پیگیر اخراجی‌های ۴ بود؛ اما نشد و داغش را به‌دل ما گذاشت
🔹
عمواکبر بدون دوربین برای زندانی‌ها برنامه اجرا می‌کرد و پای درددل آن‌ها می‌نشست؛ او حتی اعدامی‌ها را به خنده وا می‌داشت. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/452619" target="_blank">📅 10:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452618">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7084eee8df.mp4?token=Q2wCq7jovbux-mTT10XDinG7uPJI3nFJ_js5QmyUpPp47vnD5mwOSK22o6dhwwLMV9OswApCaLmSGeXLYsn-D5SdjYsazyFa37AnWtkBE1Yv0bTwtpxCp1sTX8X3X9KUdaeY3JLQh4NiKIoAabDoONmMnexKwBczheLj3_3VX4rIaIs-pE3gjmWLQo8ESFTg8u3dXr-cD4b6iJK3lrr2axwi8a8koHJtTGbWQsQIbOAi5nhrapZGMXCs0zQrEy-nXkj_IDMT9FsT_ieFvBFcss4KF762HIyVQWVcKD4RlR0K36rR5zoKUBzxrIPP2OmispO-rSU0wRdCG28XYcalOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7084eee8df.mp4?token=Q2wCq7jovbux-mTT10XDinG7uPJI3nFJ_js5QmyUpPp47vnD5mwOSK22o6dhwwLMV9OswApCaLmSGeXLYsn-D5SdjYsazyFa37AnWtkBE1Yv0bTwtpxCp1sTX8X3X9KUdaeY3JLQh4NiKIoAabDoONmMnexKwBczheLj3_3VX4rIaIs-pE3gjmWLQo8ESFTg8u3dXr-cD4b6iJK3lrr2axwi8a8koHJtTGbWQsQIbOAi5nhrapZGMXCs0zQrEy-nXkj_IDMT9FsT_ieFvBFcss4KF762HIyVQWVcKD4RlR0K36rR5zoKUBzxrIPP2OmispO-rSU0wRdCG28XYcalOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جعفری‌جوزانی: وجود اکبر عبدی عبوس‌ترین انسان‌ها را به خنده وا می‌داشت.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/452618" target="_blank">📅 10:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452617">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13abc8fc1e.mp4?token=So1mWNKg776Smg2CSvV5CuK3bvPxcJGxBRl8dD-BciK7O8F_so7CTmKdyvC6n4yAm_Q-PJjFhBrngKVP_VZreDyLAsBH33hgwedgsW-eH3y0BaHmmKCw-9wa0rqrTQLm62ottDLuEKd3xzgkkt7SIbTEAG36rQhnhU8KCgifUJP60HUIwZJO5XWdvUBouo8gddPFf3bosVUhm4jWVLopqb8Qv1yc7bV3rXkZ0RW4ode5HaGTKRO9fJewgOygyw5SEg_tIfTEysfMmcwhjFLlDEZ1F2g11XAw3Q3I512vF3JhMJEx8eQaeae8hPl-Gn8cvls0d9uvz1ZjMFH0tPicIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13abc8fc1e.mp4?token=So1mWNKg776Smg2CSvV5CuK3bvPxcJGxBRl8dD-BciK7O8F_so7CTmKdyvC6n4yAm_Q-PJjFhBrngKVP_VZreDyLAsBH33hgwedgsW-eH3y0BaHmmKCw-9wa0rqrTQLm62ottDLuEKd3xzgkkt7SIbTEAG36rQhnhU8KCgifUJP60HUIwZJO5XWdvUBouo8gddPFf3bosVUhm4jWVLopqb8Qv1yc7bV3rXkZ0RW4ode5HaGTKRO9fJewgOygyw5SEg_tIfTEysfMmcwhjFLlDEZ1F2g11XAw3Q3I512vF3JhMJEx8eQaeae8hPl-Gn8cvls0d9uvz1ZjMFH0tPicIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیرضا خمسه: اکبر عبدی یک جواهر خلاق، بی‌نظیر و تکرارنشدنی بود؛ اما کسی نمی‌داند که پشت این چهرهٔ خلاق، چه انسان بزرگی بود.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/452617" target="_blank">📅 10:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452616">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b1745dde.mp4?token=rwcTFi9A7pyVzbgGrRsh6dMIDCHVm3YzhxzZNPut2zQcXYhfxjRPRheVyq-0iMImuRqXcGrKVsaB6mP811QX49u0-RcZ671JTLMW8aQqGgvtRBziRUYG9tC87SyRLvCmqP5ZzN1U7tFpWqEYqCXRotQn1LmB9-Z8yc_o-3qn8GLXIeQ3xHbdUna2KFqjqGPeQUQQ7ZT9SSURDmtfN9Xkrvx3zvxvuUZx0K-u-pWHMjF8rulEhxbbPdzBgyo7R6bz7OcJlqNxRc1Yq5yFMR5ixOCFUm2t7pGZnnFtg10wltoTTZbAwNpUzkNrFtXcBFoylZFfFXCx9VoAkFncxnsRMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b1745dde.mp4?token=rwcTFi9A7pyVzbgGrRsh6dMIDCHVm3YzhxzZNPut2zQcXYhfxjRPRheVyq-0iMImuRqXcGrKVsaB6mP811QX49u0-RcZ671JTLMW8aQqGgvtRBziRUYG9tC87SyRLvCmqP5ZzN1U7tFpWqEYqCXRotQn1LmB9-Z8yc_o-3qn8GLXIeQ3xHbdUna2KFqjqGPeQUQQ7ZT9SSURDmtfN9Xkrvx3zvxvuUZx0K-u-pWHMjF8rulEhxbbPdzBgyo7R6bz7OcJlqNxRc1Yq5yFMR5ixOCFUm2t7pGZnnFtg10wltoTTZbAwNpUzkNrFtXcBFoylZFfFXCx9VoAkFncxnsRMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر مرحوم اکبر عبدی در تالار وحدت  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/452616" target="_blank">📅 10:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452615">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_1G2yfJjuN8dIM6umuznGvRtjSgC0N9IlxEwY2TurMVOspE2ORlEcE34QG2wUZVHGmaiE43pejdG5Fop9BnqHzSP9W1o15uR_1LgidHzOYNJNmNzy7Cy7dyZhexgba1StBCQ14tG--oNaeojcvdK5Tc76I1HdNmDGYxZIr8c44__mWdvPd_gZRlnQpdYCV--7JvSw7Ciz6JdSLS5di0KO0sBlzgox78cFC23sdByDV-jRQcW7IB7Nq1UyzWMJSD0sQmtzP-lCCEdaFD-yXWIpwLWXxm6JIE_quzpS79LI6hvlWy09w261BvzJ0GlSSSU3z4nUk2NurEoY-DLG0aKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ تقویم فرمول یک را به هم ریخت
🔹
مالزی قرار است در ماه اکتبر به تقویم فرمول یک بازگردد و میزبان مسابقه‌ای باشد که جایگزین گرندپری بحرین شده است. پیست سپانگ در نزدیکی کوالالامپور که آخرین بار در سال ۲۰۱۷ میزبان فرمول یک بود، احتمالا روزهای ۲ تا ۴ اکتبر پذیرای این رقابت خواهد بود.
🔹
مسابقات بحرین و عربستان سعودی که قرار بود در ماه آوریل برگزار شوند، در پیحملات رژیم صهیونیستی و آمریکا به ایران و جنگ رمضان به تعویق افتادند.
🔹
در صورت نهایی شدن این تصمیم، مسابقات فرمول یک در سه هفته متوالی در آذربایجان، مالزی و سنگاپور برگزار خواهد شد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/452615" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452614">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUOPFkhRCzhUZmtJhjdh0aGPQ247ac2aWL1q7tsrqOa-XZ5rcaBr2s0hnd26FJnz-dPBVbXKp7WKfjiIwpiCwMFLYuLqv4uTLvHAo1soVVbYjJwP0-RBtlKmmHqURrLpP72cB-LQ_NFtvq6mbO9RxiRY_IOt5dWzJzpOXH1A1fInjk-wetV35-ON7D7s8lQxoPwu3BRa7IfyuAh949aTOMn5W5g_dLZIqSb21I9VmPKBBCEgbaIoegsm9ioUxx5sQdsVMevMHHNVphF9tEATwc_rXvgJfW9CjL1qPPXtTpaRtQwQ-uW3R30UICMMqeA-TWvwpwXZ-309TAfRybuMFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین قاب از فراز، یوزپلنگ نر توران
🔹
تصویر تازه‌ای از «فراز»، یوزپلنگ نر پارک ملی توران، منتشر شد؛ زیستگاهی که مهم‌ترین پناهگاه یوز آسیایی در جهان به شمار می‌رود.
🔹
براساس آخرین پایش‌ها، جمعیت یوزهای ایرانی به ۲۷ قلاده رسیده، اما کارشناسان هشدار می‌دهند این گونه همچنان در معرض خطر انقراض قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452614" target="_blank">📅 10:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452613">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d8eab30d.mp4?token=T13Ph2kIM5KssE_I3CO33acaNMcLe9If518HrC4nnQJslsILxzoGDKviRK1vCOWGeMTZZ0OOzP3pz1tA0RCmfQE_PYk3ebU2OFsJk7U1fV9fa5KgQOKyDcT0bmmLBcWFv76Qdq47gydWAwnkRN0yTVZ93ZIN3CN3WfEKh9KJnpAkay-tjIXILGZ6bViJsMS1xFqe0MHdqEqjKUfHHK_Sdpk8X__EXi55VeG28kEumBi6Ekdt17BtXUex5CDJKX6fm846Hxp-immEGISPOxKYdhspYlclf8A3h3MAp-Y8WuXsRKnLhyxJ6_nSzR3Adg-zsuDdMzoZWCm1QNFnunI6sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d8eab30d.mp4?token=T13Ph2kIM5KssE_I3CO33acaNMcLe9If518HrC4nnQJslsILxzoGDKviRK1vCOWGeMTZZ0OOzP3pz1tA0RCmfQE_PYk3ebU2OFsJk7U1fV9fa5KgQOKyDcT0bmmLBcWFv76Qdq47gydWAwnkRN0yTVZ93ZIN3CN3WfEKh9KJnpAkay-tjIXILGZ6bViJsMS1xFqe0MHdqEqjKUfHHK_Sdpk8X__EXi55VeG28kEumBi6Ekdt17BtXUex5CDJKX6fm846Hxp-immEGISPOxKYdhspYlclf8A3h3MAp-Y8WuXsRKnLhyxJ6_nSzR3Adg-zsuDdMzoZWCm1QNFnunI6sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: هوا از ۲ روز دیگر خنک می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452613" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452612">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf07b1f98.mp4?token=J4udMK3Bt9hf4zLsTVbcPwrqFgR-PnBeGi9vOgFe2W36griUgas3IXlLv9nFcC-74u0X0z9yPJlvni_q3DiJDkkkEMl0omAf-MMfMP8ixMB2RSINovONCDL0bce4eJQqkO1PHeL6Cln_etyyDqcEcH31ggzv494xS1211RONJDrHKRaUwDLwnlqNYgeq4EMySkiSk_1IwPMOU88Ya9ocm1Rw9WB3U-M4wdL52IR5HsAvz9Ozf7Da-0sMy7WWL80bnvMcnfw2ijPqtgbm5YYAKBlvdd4Sa8RBdq8hck7-8Gut2KJfrRVA8dtf972G7WgnLz5-8lQ_xRJOQcSDPWxHow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf07b1f98.mp4?token=J4udMK3Bt9hf4zLsTVbcPwrqFgR-PnBeGi9vOgFe2W36griUgas3IXlLv9nFcC-74u0X0z9yPJlvni_q3DiJDkkkEMl0omAf-MMfMP8ixMB2RSINovONCDL0bce4eJQqkO1PHeL6Cln_etyyDqcEcH31ggzv494xS1211RONJDrHKRaUwDLwnlqNYgeq4EMySkiSk_1IwPMOU88Ya9ocm1Rw9WB3U-M4wdL52IR5HsAvz9Ozf7Da-0sMy7WWL80bnvMcnfw2ijPqtgbm5YYAKBlvdd4Sa8RBdq8hck7-8Gut2KJfrRVA8dtf972G7WgnLz5-8lQ_xRJOQcSDPWxHow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حضور اژه‌ای در حرم حضرت معصومه و مزار شهیدان لاریجانی، موسوی و علمای مرحوم  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/452612" target="_blank">📅 09:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452611">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2418a35124.mp4?token=hYZMGNgASoaTxzykutc7umSYS_fr487mp5_antwM19jdHAEWjIs8m-wAXKSNucBy9W3omU6SiT60f6YGlt6ol3-2HftEWsxjRRX6_baJgPoJwcM2JJV7WMer416rXsBMSRCbnQP3eaIOw-6D_CZnIEPsVg0S4qL8d_mHwsKfzFrqqbVUNprTxQBFYcRnRLy5cM9xds1WkBhwYTdEgi8TJL8iUGtCUJeu0WpayWe32gJA3zfE4GTS6JNTf_JvnhEysfO753ggCVhkdt_RFVCTK0d_ZaJPFAbdh2AQoWlxESZwTu_Y-jlFP7OPCjLBr_yLxu4xX-OsaMKqCFmxgtxQWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2418a35124.mp4?token=hYZMGNgASoaTxzykutc7umSYS_fr487mp5_antwM19jdHAEWjIs8m-wAXKSNucBy9W3omU6SiT60f6YGlt6ol3-2HftEWsxjRRX6_baJgPoJwcM2JJV7WMer416rXsBMSRCbnQP3eaIOw-6D_CZnIEPsVg0S4qL8d_mHwsKfzFrqqbVUNprTxQBFYcRnRLy5cM9xds1WkBhwYTdEgi8TJL8iUGtCUJeu0WpayWe32gJA3zfE4GTS6JNTf_JvnhEysfO753ggCVhkdt_RFVCTK0d_ZaJPFAbdh2AQoWlxESZwTu_Y-jlFP7OPCjLBr_yLxu4xX-OsaMKqCFmxgtxQWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس قوه‌قضائیه به قم سفر کرد
🔹
اژه‌ای صبح امروز در سفر به قم، حرم حضرت معصومه(س) را زیارت کرد. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/452611" target="_blank">📅 09:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452610">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6dd27524.mp4?token=vBDZPN5y-jAD8nKE5NVUEm-bHcVFI0whqkTC9s8hX4hUxpQZOEZDSaGWpxQajqaH09KgDLMVr2FGXHFEPMsHcaiXFZ_M5NAnGzL-k_JLSkiWbiG3pWr7lX6M4gEvfNhc_8L-r47-W7l9N6WuTOmlcoiN3gI-ng-YHZ9ZwNK5t1E9qwZn6CgUYg4YhpsAJ_BVU3nxoouciyZqOG5Y7mhFGi7qmvgxvpJPiPq-4kwT454G0f4Rp6sqvWMtT47-wGh4-6nE9dhtVjZdwzZFx6s6ETRn4PTEotgAWBgnVxXCMTApzzQcczlW6XYZObWaBE1QZ6nCUiXBAbemoXBVC4mXyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6dd27524.mp4?token=vBDZPN5y-jAD8nKE5NVUEm-bHcVFI0whqkTC9s8hX4hUxpQZOEZDSaGWpxQajqaH09KgDLMVr2FGXHFEPMsHcaiXFZ_M5NAnGzL-k_JLSkiWbiG3pWr7lX6M4gEvfNhc_8L-r47-W7l9N6WuTOmlcoiN3gI-ng-YHZ9ZwNK5t1E9qwZn6CgUYg4YhpsAJ_BVU3nxoouciyZqOG5Y7mhFGi7qmvgxvpJPiPq-4kwT454G0f4Rp6sqvWMtT47-wGh4-6nE9dhtVjZdwzZFx6s6ETRn4PTEotgAWBgnVxXCMTApzzQcczlW6XYZObWaBE1QZ6nCUiXBAbemoXBVC4mXyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسعود ده‌نمکی: پیکر اکبر عبدی روز یکشنبه از مقابل تالار وحدت تشییع می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/452610" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
