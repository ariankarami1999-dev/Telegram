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
<img src="https://cdn4.telesco.pe/file/YkssjLsohcaiuxRnMx7DgNxDXE3FwmI9iaKr7ynqethkbPbFLRsocxJBbtBx0uldu_HPbCyiMZP45Id3C725ZHkvBSqHAi83yAxSzrirZfMI_gRJ8KVbyfUp25kp9ueTWKm13AxtQ6Yr8xVdKo-cymz_VF-lkn6wUnP9v9gfQTrCeR15CVhGiDF65LNvIlDI4IanPwEZfTF6lL1jZvF7EStjKzPuQU5nbExG6hxsj49mXNxuzGZjRDcTKexN5kpEo8J5oUv74a9uFpRRkW5h8iU6nOxnizOOLHL0lSj7G-X24j1YMhWRd-IA8YxuGKquURJ9SwVU7Jh2Wgy7hzQhbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 14:15:05</div>
<hr>

<div class="tg-post" id="msg-456199">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX9iyaju-uyLwVmeJ2d1TB0mN9xnW2IAO_QilwUNOt-ddKCWzf7oxmUbkFqXD5RW-a12bjxW2zVic07KiaBoh1B0rkcm9V7rpdbl7pjBBrCaQ2r71eNBOd8uYFc6McCE4FOW3Cj0aVW-d4wieeu7fMGlCUlbtZTGBwXCxcsXlG104qBHwZWiOB5O0BthveJ25tN_33uZADMleG4fVEV3WgL-2VWVpzXa_m8zKjpl0_VqkUivczkI6JyMyLNJUOusMQF59fk6ybygFf67ihXmuJJ8mygiZsfdSiL6HWoLo_spVlkhglyQvzf4RpnHo09Gpb-xdDsHr71WK10ij-b6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران و تاجیکستان پای قرارداد نفتی بلندمدت
🔹
ایران و تاجیکستان در تازه‌ترین دور مذاکرات نفتی، بر سر یک همکاری بلندمدت در حوزهٔ انرژی به توافق رسیدند؛ توافقی که ۲ محور اصلی صادرات فرآورده‌های نفتی ایران به تاجیکستان و تأمین نفت خام مورد نیاز پالایشگاه‌های این کشور را شامل می‌شود.
🔹
براساس توافق انجام‌شده، ایران قرار است در قالب یک قرارداد بلندمدت بخشی‌از نیاز تاجیکستان به فرآورده‌های نفتی را تأمین کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/farsna/456199" target="_blank">📅 14:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456198">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تأیید حکم اخراج لیدر ناآرامی‌های دانشگاه شریف توسط شورای انضباطی
🔹
شورای انضباطی تجدیدنظر دانشگاه صنعتی شریف حکم اخراج رضا دالمن را تأیید کرد. وی در جریان ناآرامی‌های دی‌ماه به نقش‌آفرینی در تجمعات غیرقانونی و ایجاد التهاب در فضای دانشگاه متهم شده است.
🔹
براساس…</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/farsna/456198" target="_blank">📅 14:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456197">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d648076.mp4?token=sU6IssAd_s28g7EvUTuiGAgzq-ZnBZNER-Ufmb5aZRk9KIXMBXbH5vYv_f6tF5VMC_0xyUriP7NsXLhiCCHxbk50dBrslHtI9LMtihECH9pXOMO2iHUGz52uZv3B2xe9q6LU5RJrw_ZHRq_1-F435wv9702nrCuodBbUPM6S_jOzGm11PgFFTh6C-hZH9NORDP9ESJ3B8RVyLW4htkfnY7iWFj1E9Ys0RiSIo8sWXDSphcYZqOn52fmuFB7LZn5ETo4BMUUpIroGTsHJRIyt69TL5m-AI_iIlCvMPgBEOKYHgGDGc-vRSHVZf1yOrIbF4srRgQKovcRL7K5oufap6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d648076.mp4?token=sU6IssAd_s28g7EvUTuiGAgzq-ZnBZNER-Ufmb5aZRk9KIXMBXbH5vYv_f6tF5VMC_0xyUriP7NsXLhiCCHxbk50dBrslHtI9LMtihECH9pXOMO2iHUGz52uZv3B2xe9q6LU5RJrw_ZHRq_1-F435wv9702nrCuodBbUPM6S_jOzGm11PgFFTh6C-hZH9NORDP9ESJ3B8RVyLW4htkfnY7iWFj1E9Ys0RiSIo8sWXDSphcYZqOn52fmuFB7LZn5ETo4BMUUpIroGTsHJRIyt69TL5m-AI_iIlCvMPgBEOKYHgGDGc-vRSHVZf1yOrIbF4srRgQKovcRL7K5oufap6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاوت تحقیق کل قرآن با صدای شاکرنژاد رونمایی شد
🔹
حامد شاکرنژاد قاری بین‌المللی قرآن از اتمام ضبط تلاوت یک دوره کل قرآن کریم به روش تحقیق خبر داد.
🔹
این اثر طی دو سال استودیویی ضبط شده و به گفتۀ شاکرنژاد برای اولین‌بار در جهان اسلام کل قرآن به روش تحقیق و به‌صورت تصویری ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/456197" target="_blank">📅 13:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456196">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVhj3LJwC59GbPQ-OaB1QhAtZp2njEEZQZBZk0LwI_Cx9SCjf62zHtqqhNao1SG1yE50chNrY9l-pK-oInlZuXuOwlEB8_kZqtLlcBv7UyEP-nc2mfqk7QYQAtVciafKCoHMErmhEJm7g-kHfUULL_0b_ZjeiB2fek4oRU-sdbGgrdcbLyEa98bI2fhCuDwssdMXEpvNGgCE686rDy8DlNgsYQIZtUoUNbrb66QBS-1nYAGofM8EUkIJ3jJb820XsFwqAIWfK5vBC8kJeNY_8P5FJkSlFSLCu6fNyNuwSSJUHz7trswqRGgn2xszHrM6nhTTMgk54-XwWmwrIigGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: ۱.۶ میلیارد دلار توسط برخی تراستی‌ها مورد سوءاستفاده قرار گرفته
🔹
۵۹  پرونده برای متخلفان تشکیل شده که تعدادی بازداشت هستند و تعدادی هم خارج از کشور هستند.
🔹
بعضی از این متخلفان در کشورهای دیگر کارهایی می‌کنند تا از آن کشور ممنوع‌الخروج…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/456196" target="_blank">📅 13:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456195">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFVQzFUm3_FRQyqPc5nQMb42lHYAhXZoV4i_9uynudhIlpXtitzczXZGpOp9AwVpHX9O-VLVf67tOyxOuS0TvmERynC_pR8cu-H15vVB_qg1YCrISNGdkbLvGOXNV-txe-qN3CPb9auOcH9Cu9ST4bJn-IxY4tbBr1dnJfGB_qS7-pnVCqlZj7ucwGPjO_RpLOQengMxvqqeeaJco_vLhzIwXOWV1Hk0CQMQd846cud56NQmI4fJ1cmyqmPL2ibx-076bWxepugpUwoaJ14VveFFIdMOprok3-D5Cp46IXILatFK5Zs-EanFAzxJjUmcZg31wpJbSTRvL0a8YlZf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
در حملهٔ بامداد امروز رژیم صهیونیستی به شهرک «انصار» در جنوب لبنان یک مادر و تمام فرزندانش به شهادت رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/456195" target="_blank">📅 13:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456193">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a34895eb.mp4?token=s-avHggZgCu34Dk_2GjyB6uM-JpdreSe9FYXJQDQhABRgSziWMmvJIucAYV02cZqbi3NWJyv8I2CQ8tlP8FarEVdK8xOgSGNiCcCGom_RORkAhle4tSnGQWad5h1lrxE3_c6DtGGyHy6O0m_b76FR7cz6u6mAa3SG11hDdo4KKn27SDQjOmECzfLKRZthB2rthzDCb_If_RqrUc4mOy13t-tJDO50P-J5ccDwYasNVt91oOG7VVPgJVba-GuNgSh1Q6nNO6xevUhhyLRJAo2DilIc4rRbKXivO3mWnA8sRen6u2W3V--cVrTV_porzNBVsUT2ac64fy_B_J5HQ8LGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a34895eb.mp4?token=s-avHggZgCu34Dk_2GjyB6uM-JpdreSe9FYXJQDQhABRgSziWMmvJIucAYV02cZqbi3NWJyv8I2CQ8tlP8FarEVdK8xOgSGNiCcCGom_RORkAhle4tSnGQWad5h1lrxE3_c6DtGGyHy6O0m_b76FR7cz6u6mAa3SG11hDdo4KKn27SDQjOmECzfLKRZthB2rthzDCb_If_RqrUc4mOy13t-tJDO50P-J5ccDwYasNVt91oOG7VVPgJVba-GuNgSh1Q6nNO6xevUhhyLRJAo2DilIc4rRbKXivO3mWnA8sRen6u2W3V--cVrTV_porzNBVsUT2ac64fy_B_J5HQ8LGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
۲ حملهٔ هوایی شدید رژیم صهیونیستی به شهرک دیرالزهرانی در جنوب لبنان
🔹
رسانه‌های لبنانی از هدف‌قرارگرفتن یک خانهٔ مسکونی در محلهٔ «الراس» در شهرک دیرالزهرانی هوایی خبر دادند. این منابع گزارش کردند که همزمان یک موتورسیکلت هم هدف شلیک یک پهپاد قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/456193" target="_blank">📅 13:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456186">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1-B9EOY37S0WhPLv4PU_BZpSrPzxhl35MPy_ynSXUuvBufvWurLW7PG_MrrxUCEkz9eEX5Na8Ktchyfb4_F8OO4VYM8zNYSdTEmOjNeVtgdj026rgwODs8eu5TZt45jZjxLiw7KOQBMDD5tGI49Sja-C5Xl9YmaQwhmtdZyr6etNEk5Wpr48AAmVNuvkbeyKvPgxDly2YtEAsOrY0-ivVocyrt9SeynIj0l6ns8gHgm7jV7NlmV-nTsB3fg88hlhAyhkT5lZ1tYKVUeKAu2GJbbiLO3Hhwk-5su50TIWchRxcCbrsB5saMW8ps3CGrlc6UkR5ZaqpOVxE6ONzCcUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4pnbHoYnaBMq7P8lAGhTybIgvxQ4G5Q6rx8qM4p9kZvjPIhEFBDK_myaPLDNVg99X60O1Nf6z0wq1v36SqJ6piyYOowix5cewcc4Fo07lyZ1_1gXYD1_y4fopZFZA2eNJ_K9T1a1Thu3RghsTHaXLVNTG2v9msXNxS_tLp2YsnnW83zUh6kKBDcWZZXuyBIJcXdPzqHsVzPv8z0-B02GcOAjwFo6iOocxupZMqnvFx3QDr7EUbxqezRr6sFwM8HtwcP3fyVoc-3wr7lsEOJqXZqeYQ960_OPqxw2a-fbWjaVh73__BNaqDVg2cp9Y1k1aWEe2I676huaDBFDXvY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z62gVptTTS4oiOyRgU3RxKUD0dKMn8pywK8l1rUOUxM__68nR6QuN1-b4WAXOAv98ddjmowCkc2TuZ0zxNzFyAPtATh-xPRJxYXbArWGv-fMSt8L3E_XZcsAWv2cr4bAq4iJaYdU0ZgaS4tJp-ZmoDn5kJyUWaOT9I8Srgita6uZQR4osIcQWeyfQhqlfTjvU4KGM53AOwWdqjequ7BrO07OfJM6NhdQ8rlqEbGjlYMHElw6q7IJa-TwSanPs_l7rqxAKv6KnjXGTSdrN5wV1Irpo5gUoG6B1Dm1hFVz-GtKiWODIJoU17qpE7spc5buyjODHK7js8U45Irv_SCCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_Rockk4y4yp2RNPq8MRE6TN9QylclnkduzRmEWWE_1mO3uaWSAaZqiBkpOAqGSQ31coCU6rE3KJXpnCgALW8mny42eq-ZqPIib5EZqOgzsgf3UnBZT41AGg2lgvVwhVadCAf5uN8dqifg6u4L7YzYzcnb7UnGoIcr_FFAEM1iokC2oRw84AiokLRv3bTtXFO0VBN1_SJTXzCr1-M3Scbyl8ojZI2AO-We68vjp5P1N7LC45Ib2ahs_Ogojod7jCqSiYtfXkn-5hOsFrr1D1jr0mcbdiNzcJCwKTjpeqkMoQHMHw8lngYNlALBw05FoG_PLlRVrRKmxxiT0NFxQDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqNMdKESFN5eXNgx-PfYtXr_L6_8HGP_Cqz_IizMKzWFpaRcPpRediRVrHgNnoQJyDlPKl1yCr_pgbydcUrruwpjfPHpQB4U6oJ4KeoDbsTOFVbw42h7SeHFudMw1R9MLZChw6fVF3yI_8pFVeXAN6KNGzrkAdqiTDxUzooQ3272Vi-O9Vad0lbLL2fzHu3ZyjNBQxcQasoWKabl5ydm3y6zQMkLZPSs_an8Vnkr3hEAk09pZfmTu9UgMXW6RfzGJHgy5I6LbQEOFYiNnfB9Wf3zOpeigZic1gGJsxb6ISstFd-9iKPVgR1L2z_51vSHtEt4GUD-OknOR2t3KD0mhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1h4LPtp7eRHguz60lC8lKJrJcjbmjHAfah86ToRrkwvHaWEVC-wZsvC9WA44Ic0bZLUDNKubVpatQrzem9BE8JfQGr3NYT30M26P4q2AXa20qQ3j-TgQMpmnU2yc4uAUJfaQfNLSyItlJlCa-F416WYQLAJyB_dD1yzSYKClOv_AoL3o-LCjPdnZS0jd49gw4H3-Cl4enya2U9RYg1fObh_TmQ-m474zXZomTx8Zq4Op4H3Qv-lv9FUs7bwAGgDsItj8XwVs1TPae-8UZjJpzfY6bLjdk0HM3qVFfgbzpAJaeMB01UyS3j3hEHMLzV6MeOWVDQAI_MI0FIwHw1_Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWnEAP-rVTfPmWcrPzeKs1hNYf2V2YLLxGmGeGdy6sfYxJTAQml9UC79tJUbf2nlTV6oBow2Y0gY7nXdlKzFBwz_zk0nZM8bvjWVo5IxsOtW0r1qWS1nAqLbyZScHqRARn51emRQHNPp2DTuVrAPKg-QyMtfgfMkKI32vfKWiDOZ1E3vNCw6rGVvPrGZHDMpA6jrsHMBJSAzcH_utQu5vKaPrKiB8vWOcFviWVnlGWsT3oVJNBTkmey9TFEDodJNXBDZ-68J004ob_uVOf9FX_dgDrXm88WZDEAgecq1pKr208X872cxEARQwTr64hLcLOeM170cSnlkYC4sVPGNCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات واترپلو زیر ۱۴ سال کشور
عکس:
عرفان تقی‌بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/456186" target="_blank">📅 12:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456185">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpRUCLvaGxO9ZIdA1OMHv4Q9hMWS073tfgk1LQMA5Rpyb3aZodB9VOBIrwC7Akmi6M2lJ3bTjUFdjvXeXp5zLIu6rLKxjnBNbeXFY-2K1mlMbfnhNGJ0tNXyBti8Jg0WYbqTKtJiFD9S0ycH8QAQ6VliIWF8j47-eep7OlCQ_P8Tascy0jEaP8qgYbDExn3317sOgmddcpz8L7h8rYoNXcwW73iKI_XHOMjepnn5_kCPuUGxZAeYE0Z7EmPFA8Xm_zuhmGMrvsbI3_J3a4BgzvIlJMrIyRFqUy5UGffRRrn2CbWMWKOz9CTIwLwHWQXEXbAwjanDIqwD9YJe0LeO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ دانشجوی دانشگاه تهران به علت آتش‌زدن پرچم ایران اخراج شدند
🔹
شورای انضباطی بدوی دانشگاه تهران، ۲ دانشجوی متخلف را به دلیل تخلفات انضباطی از جمله ایجاد آشوب و اخلال در روند آموزشی در اسفندماه ۱۴۰۴، به اخراج محکوم کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/456185" target="_blank">📅 12:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456184">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS8auPNwTrk5LIIT0WmylnrGebjfEx1bpzFuB-bU-Z9pxTzNihzn-WbIPx15VqUyX03OyCWZOO_itSyP4BpWDs4FnDoTHDeJM_mODtbiRbsMASamGo5fhx9n7dXPFtBxgSWSly_1DIPL2TPrHQNifpT4wuZBuqEVV9TdIeQpiAvCMSdqEaiy89fgCVqGvZVj4sz-EzHVsLUf-nGI8LOErKObclLgc__-YxIcMaQ3Dd4oGNWJJnjwUOMyaSX5lPkd7PSzNkRxaEEQdJGJF6C_kjKzdhggB7I1JNNeAEPg2NNTah8EaLRsC-HYHaj8XxV0HGvOv6pjACGInWlKTyvYUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضایی‌کوچی: کنوانسیون خزر دشمنان را به سواحل ایران نزدیک‌تر می‌کند
🔹
رئیس کمیسیون عمران مجلس:  در شرایط فعلی نباید دست به اقدامی عجولانه زد و به‌صورت شتاب‌زده یا حتی محرمانه، توافقی را به امضا رساند. برخی از این اقدامات شتاب‌زده نشان از ابهامات جدی در این…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/456184" target="_blank">📅 12:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456183">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab15b5cb9.mp4?token=lDdjUjDtQrQzoIY1M2lZnMZpKTU2DZKp8JgBn0Zg-zoFGsJPw2ic-5jwbW_PC89RouLmoIIFnGnoCwi_OaxWYXqEehHVrQfQR9CWSvAgY_hm-35ly-f_VR5W-ITtyXP2PCLJDnLhCH2fckSobUuTc1ftyxJ1JLqoS_SAjfVpmvygz0SwcJpMu4aGP-Jp08vaA4JmiemC_Ht23hoM_Kz9btLWL_Fmn2PMA8C29papre3xVkXCvkY5_YcL2POD6bW4iZ4fTcquNtXcNtwqAeFqKow31g-JWTRJfYitDpneOTCHeTR8K47-6UKZJH5Sc7YdZ5tpi4OiEy0xZxBbCYn8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab15b5cb9.mp4?token=lDdjUjDtQrQzoIY1M2lZnMZpKTU2DZKp8JgBn0Zg-zoFGsJPw2ic-5jwbW_PC89RouLmoIIFnGnoCwi_OaxWYXqEehHVrQfQR9CWSvAgY_hm-35ly-f_VR5W-ITtyXP2PCLJDnLhCH2fckSobUuTc1ftyxJ1JLqoS_SAjfVpmvygz0SwcJpMu4aGP-Jp08vaA4JmiemC_Ht23hoM_Kz9btLWL_Fmn2PMA8C29papre3xVkXCvkY5_YcL2POD6bW4iZ4fTcquNtXcNtwqAeFqKow31g-JWTRJfYitDpneOTCHeTR8K47-6UKZJH5Sc7YdZ5tpi4OiEy0xZxBbCYn8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور وزیر علوم در خبرگزاری فارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/456183" target="_blank">📅 12:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456182">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT3v16xv5JlBUpVYtdu6jFA7cpdDzTjFUNER6H_EQLZekUTl2uR3NIsXK4s_HZrYBia1Ku8tzfABeTUrFGoj6PJfuukE79VC-_Vo3vaTYGZ2ebua9rpgZQRRIMk7mZdthWjqYS20xsZ32ctCZJzRLQ5Si5bn6ugUbnB0AEBNMxYnWDCqi6AsdqFajsrwq3bjv3m0svJr1Vta2cFJCzNrHVMqg9Yc-iCDp4a0F_dnzsz6QybKjklnefokLeAzxsKog_2uq0g0--A0DsPoE8gKOeUzE4Gyl9IVeLn7wD-vdeP1G6gthEUzum74JCU7HHOxi0lwn6D3w5Fd_SvCZhFyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنبهٔ ثابت بورس
🔹
شاخص کل بورس که در آغاز معاملات امروز رکورد تاریخی جدید ۵ میلیون و ۷۷۲ هزار واحد را ثبت کرده بود، در پایان معاملات به ۵ میلیون و ۷۳۷ هزار واحد برگشت.
@Farsna</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/456182" target="_blank">📅 12:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456181">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شهردار منطقهٔ ۲۰ تهران: ایستگاه مترو میدان حرم حضرت عبدالعظیم حسنی(ع) به‌زودی آمادهٔ بهره‌برداری می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/456181" target="_blank">📅 12:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456180">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0pCTNp2XL1LGAdsqbeRxGAgunMcVD2Gg8MzOFaSrSkyVy9Sz1yueG9sAeYnYOX_6UA82_amQyh8UGrU7UDOASf8kHDBThAAwjZ1gJcYVLxwi6048HmAhYJSXGwMztShiQ6eKEK31pW4BOTvwMoNYJFNte-Ln8EkhRZHp5UnEmPJRX2rem_VmBHx3McdiA7MfY-9B1TeRV5j0h77ijGaZX5dfcoWZkehz6pxGOvh4RMfBWzs9MojeX6RA-79QR2S1Z6sXqwvf4GN_LgyGwTNx05rYsNVXTlzh5CBnk07qPLyWRpPgBRDx5lBijdCA4_UKqKAUjPAAkE6ZCZbybYMyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر انرژی آمریکا باز هم فاز کنترل بر تنگۀ هرمز برداشت
🔹
در حالی که روزنامۀ وال‌استریت‌ژورنال با ارائه آمارهای جدید ادعاهای دولت دونالد ترامپ در خصوص کنترل این کشور بر تنگۀ هرمز را به چالش کشید وزیر انرژی او بار دیگر ادعاها در این راستا را تکرار کرد.
🔹
او…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/456180" target="_blank">📅 12:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456179">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a913722b13.mp4?token=o7c7RC4DCe_9TLZmaNhv7QWW4BDF_zK0e4FzLvjdVKbKtEvD33tVfiLc3IB-P4SFEG1K4NDV2UMqi3VJcNS_bW4BqN_qFgunBlqhYjroQEF3jXx-QHm_i6Tq1ycbKezAPnk8NSl6yRe8_8piUMrU6-1Ea2k1qHVr1cUNSFa3iS8rQDrU12jYfqslmtaxDPWoQmzMl4v4BKa1oUyuXZnqFkt-hnF7ltRl-Fj0G-DZsmwL3WAMloM0WbTUBgGOmCKUPrm1_9Tp8HRqvdsKCqWl1Chmskgo18vt-dshMmfCb7xDlxQq8CCKzX60btiWUUgDRUB1vntrJX539V442Lu-Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a913722b13.mp4?token=o7c7RC4DCe_9TLZmaNhv7QWW4BDF_zK0e4FzLvjdVKbKtEvD33tVfiLc3IB-P4SFEG1K4NDV2UMqi3VJcNS_bW4BqN_qFgunBlqhYjroQEF3jXx-QHm_i6Tq1ycbKezAPnk8NSl6yRe8_8piUMrU6-1Ea2k1qHVr1cUNSFa3iS8rQDrU12jYfqslmtaxDPWoQmzMl4v4BKa1oUyuXZnqFkt-hnF7ltRl-Fj0G-DZsmwL3WAMloM0WbTUBgGOmCKUPrm1_9Tp8HRqvdsKCqWl1Chmskgo18vt-dshMmfCb7xDlxQq8CCKzX60btiWUUgDRUB1vntrJX539V442Lu-Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقیف خودروی متخلف پس‌از انجام حرکات خطرآفرین در اهواز
🔹
دادستان مرکز خوزستان: یک دستگاه خودروی پژو پارس به‌دلیل انجام حرکات نمایشی و خطرآفرین در کیانپارس اهواز توقیف و پروندهٔ قضایی برای راننده و سایر افراد متخلف تشکیل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/456179" target="_blank">📅 12:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456177">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca49c36c6c.mp4?token=XNmprV_sID3k80b4hIPPJn5FcNpQXl2AozgLLDhgRMP0he4QKxPgEeD4CC4YNq-VvmkmttlFOG_sxrzyH2OlnRZiWX_ehUVpo0wq-2BVL7eFYX3h8YfijPDiC6Mud85Kyfl95JOODiVGBjYFpGeB519XNJCTMkafFTcXntDrPK5QlFEDgkpFm30_iGK3g6DSBbDTdK9wpoDNgijJWqZVq6bue5-ml-9CiVx83SkjElgLJTj8eR9iILcwMMpomBhhhDE0Ya9SMHYHjdgG63SEi41IZiDT4NjX_qyoz9eTSn9AoAWhmqQiYByzdR_V-lE_VBgFd3DxZP7juqIHzqWwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca49c36c6c.mp4?token=XNmprV_sID3k80b4hIPPJn5FcNpQXl2AozgLLDhgRMP0he4QKxPgEeD4CC4YNq-VvmkmttlFOG_sxrzyH2OlnRZiWX_ehUVpo0wq-2BVL7eFYX3h8YfijPDiC6Mud85Kyfl95JOODiVGBjYFpGeB519XNJCTMkafFTcXntDrPK5QlFEDgkpFm30_iGK3g6DSBbDTdK9wpoDNgijJWqZVq6bue5-ml-9CiVx83SkjElgLJTj8eR9iILcwMMpomBhhhDE0Ya9SMHYHjdgG63SEi41IZiDT4NjX_qyoz9eTSn9AoAWhmqQiYByzdR_V-lE_VBgFd3DxZP7juqIHzqWwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاتک سنگین حزب‌الله در علی الطاهر؛ ده‌ها اسرائیلی زخمی شدند
🔹
رزمندگان حزب‌الله لبنان با تلاش نظامیان صهیونیست برای پیشروی در ارتفاعات استراتژیک علی الطاهر مقابله و ده‌ها اسرائیلی را زخمی کردند.
🔹
ارتش رژیم صهیونیستی در پی ناکامی‌های خود بمب‌هایی را بر روی منطقه علی الطاهر انداخت.
🔹
گزارش‌هایی از درگیری با سلاح‌های سنگین مخابره شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/456177" target="_blank">📅 12:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456176">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBDrRAykowbLg8IJgDT0uNxr-sCRnPMcKEu0HZfXQFD0kKUG0nYYV4NUThwywZcFmSVaEuWf6wqlrhQdTJamOOe45n5L14ziqzezOwd87EQliictH6P8v9pZVrZwaO8NCp0Zw6lsMgflmskM5sSKULlKuG-K8e1GEZF96Poy_t8G6gOiOWzSRpwFdcJzpAQDh6efDs18i9IP683Ey3-xWNAah1naXobVaMeQR-_qUXeM3hU8ZK1X0JYRdxGc5CMFPagarc8EuGPNMI2nilnDGR4iI1M98DBifmdUWls6L9R2oPvvjeZF6DkMC9QmnfU81EGVjQVdYVm4qW7cr9p5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تابستان هم حریف قیمت تخم‌مرغ نشد
🔹
گزارش‌های میدانی نشان می‌دهد با وجود فصل گرما و کاهش تقاضا برای تخم‌مرغ، هر شانه تخم‌مرغ در مغازه‌های سطح شهر ۵۹۰ هزار تومان و در وانتی‌های کنار خیابان ۵۰۰ هزار تومان فروخته ‌می‌شود.
🔸
این درحالی‌ست که قیمت تخم‌مرغ ۲ هفتهٔ پیش تا ۴۵۰ هزار تومان در هر شانه پایین آمده بود.
🔹
رئیس هیئت‌مدیرهٔ اتحادیهٔ مرغداران میهن می‌گوید هزینهٔ تولید تخم‌مرغ بالاست و مرغدار ۴۰ هزار تومان کمتر از نرخ تمام‌شده می‌فروشد.
🔹
به‌گفتهٔ او نرخ واقعی تخم‌مرغ برای مصرف‌کننده ۵۸۰ هزار تومان در هر شانه است!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/456176" target="_blank">📅 12:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456175">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509c9e1c5f.mp4?token=udDaB-_I9o0cAGkxBf7LQVap5VfsF-1EH-diUlN0k70ben198UXVQe5F1uasEpdUfoJnZVkiog1xVq703mWRZQ-wWpD1utcbeeAo9D4vTQ9bLyIC3zfajnvMIJ1l5eJ-odyAIYwy3bLJCs6RFqnSfI-NusJlyYavVk_YYpeU0bQ4lZFGqZaN4wHvv96n-Gwe2-zi6td0DeJwvC-LRyFGKELTeSUCFde7DnXp9T3-wbNe1aIVsCaOoV7C8Kv3WC1NDp_gprDsAIrR3tmahs7aXn7OL5sOK0D3kJME6Kqk8c6U4xVQbDYQW3gaz2OIq4N_nu_l_6gdu5gRb56aU9ztpgLJZ4VxMlCIjIpue_RiL4sfaq-gn5b_SVjE5Rw2x4FG9DsQv79Z-Ei27K_RDDUuYGYM6kV-sxyKq6ZqZzEPks4PHRkqBQbAPvlDArcPrn90zL-h3tZ45-RWxpAPo-Zvc5u_U0pUeQL6prmRHOSGc_WJ3EAOVj-yrTL16yJ3gD0VAoIARiCl3-MUyLE0Br697fl-3AN7dlfFMIiuJx7L1uJSqyBA9pQbt96FvxLBu0uSc69Sn51W7WFppVnPxAw66Odeu6pRK4UhjFNKe7Ls3UdLZYOnmhF4GWAhlPEww8r13RoJxWECuBZ56Q4GwVrA7dYVXlarI5jnwaK7ggBUFNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509c9e1c5f.mp4?token=udDaB-_I9o0cAGkxBf7LQVap5VfsF-1EH-diUlN0k70ben198UXVQe5F1uasEpdUfoJnZVkiog1xVq703mWRZQ-wWpD1utcbeeAo9D4vTQ9bLyIC3zfajnvMIJ1l5eJ-odyAIYwy3bLJCs6RFqnSfI-NusJlyYavVk_YYpeU0bQ4lZFGqZaN4wHvv96n-Gwe2-zi6td0DeJwvC-LRyFGKELTeSUCFde7DnXp9T3-wbNe1aIVsCaOoV7C8Kv3WC1NDp_gprDsAIrR3tmahs7aXn7OL5sOK0D3kJME6Kqk8c6U4xVQbDYQW3gaz2OIq4N_nu_l_6gdu5gRb56aU9ztpgLJZ4VxMlCIjIpue_RiL4sfaq-gn5b_SVjE5Rw2x4FG9DsQv79Z-Ei27K_RDDUuYGYM6kV-sxyKq6ZqZzEPks4PHRkqBQbAPvlDArcPrn90zL-h3tZ45-RWxpAPo-Zvc5u_U0pUeQL6prmRHOSGc_WJ3EAOVj-yrTL16yJ3gD0VAoIARiCl3-MUyLE0Br697fl-3AN7dlfFMIiuJx7L1uJSqyBA9pQbt96FvxLBu0uSc69Sn51W7WFppVnPxAw66Odeu6pRK4UhjFNKe7Ls3UdLZYOnmhF4GWAhlPEww8r13RoJxWECuBZ56Q4GwVrA7dYVXlarI5jnwaK7ggBUFNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماعات شبانه تا چه زمانی ادامه‌ خواهد داشت؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/456175" target="_blank">📅 12:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456174">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزارت اطلاعات: دولت فرانسه باید پاسخ‌گوی مداخلات دیپلمات‌هایش باشد
🔹
وزارت اطلاعات در بیانیه‌ای به دولت فرانسه هشدار داد: سربازان گمنام امام زمان در فرآیند رسیدگی به یکی از پرونده‌های مهم نفوذ و مداخله خارجی و در حین اجرای دستور قضایی بازداشت دو تن از متهمین پرونده، از حضور غیرقانونی دو دیپلمات فرانسوی در محل قرار مخفی مطلع شدند.
🔹
از آن‌جا که دیپلمات‌های مذکور دارای سوابق گسترده تخلفات و رفتارهای مغایر قوانین داخلی کشور و تعهدات دیپلماتیک بودند، پس از احراز هویت آنان، مراتب به وزارت امور خارجه ایران اعلام گردید و سپس دیپلمات‌های متخلف با حضور پلیس دیپلماتیک، به سفیر ایران در فرانسه تحویل داده شدند.
🔹
درحالی که وزارت اطلاعات بدون علنی کردن موضوع تخلف، مشغول تحقیق از متهمین و بررسی مدارک و اسناد مکشوفه از محل قرار عناصر بیگانه با متهمین بود، فرانسوی‌ها به هیاهوی رسانه‌ای با هدف فرار به‌ جلو و پوشاندن تخلفات محرز صورت گرفته پرداختند.
🔹
تحقیقات اولیه از برنامه‌ریزی و طراحی پروژه‌ای گسترده با اهدافی همچون نفوذ، مداخله خارجی و بسترسازی برای اقدام فرانسه علیه استقلال کشور، از طریق شناسایی، برقراری ارتباط پنهان در داخل و خارج از کشور و شبکه‌سازی همراه با اصول پنهان‌کاری با برخی عناصر مورد نظر بیگانه حکایت دارد.
🔹
از آن‌جا که در قراردادهای مکشوفه از این پروژه شوم، امضای سفیر سابق فرانسه در ایران مشاهده می‌شود، دولت فرانسه باید نسبت به اقدامات غیرقانونی و مداخله گرایانه خویش پاسخگو باشد و درباره این طراحی خام اندیشانه توضیح دهد.
🔹
وزارت اطلاعات هشدار می‌دهد که اجازه رفتارهای غیرقانونی مداخله‌آمیز را به میهمانان دیپلماتیک خود نداده و در صورت تکرار، برخورد درخور متجاوزین را با مسببین صورت خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/456174" target="_blank">📅 11:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456173">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2RGxP3o2yx7-9eInlZE7AcFykA_KyMlsbi6Os29P8j3RrVwKto8h_6C2nG1laK9x69mzrZ0KhVhEX9SiEyH9i0XVWxtDCIBUIS_ZXUWKT_xrkRKHrhv0pI5oYq3PgtFcY8_W5M5wElAzk7d0v58sOMAWlkv_mopLK53O8TYxsjfWRURiZME0nDtzX2CGTDdIHyJRzko3RjBqC7K2pinQcjzePS3SrQRH9NTvmbRKmGIcwc4_qstylS_NYRlfBVceazK587rMNvrkOErLL-WGFa034rauZuonftvtIeseWHy8HTvWFscWVUVGLeEwc0ksPlQ3wMKzxeCDPv8_6bwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید: ترامپ دربارۀ «آمریکایی کردن» تنگۀ هرمز شوخی کرد!
🔹
وال‌استریت ژورنال به نقل از یک مقام ارشد کاخ سفید گزارش داد ترامپ تاکنون با مشاوران خود دربارۀ اعلام تنگۀ هرمز به‌عنوان «قلمرو آمریکا» گفت‌وگویی نداشته و اظهارات او در این‌باره بیشتر جنبۀ شوخی داشته…</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/456173" target="_blank">📅 11:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456172">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حملهٔ توپخانه‌ای و راکتی ارتش سعودی به شمال یمن
🔹
منابع یمنی از حملات توپخانه‌ای ارتش سعودی به شهرستان «الظاهر» در استان صعده خبر دادند.
🔹
همزمان حملات راکتی از خاک عربستان به‌سمت منطقهٔ «بنی صیاح» در شهرستان مرزی «زارح» گزارش شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/456172" target="_blank">📅 11:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456171">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdvK0k_BZ2B59NbHDPLaM0h1-vCD77Pz8dOfGVR3HESlQeHfQR1H4_DKtPGYfq9jncFPbbBeH5kguN8jbbGdLDKyoEDEK3p4w1BFye68DDb_82OIZeWwmzh69tyzh10qIqCcFN3dJPw2zj6YseSHd-4VDN1Zrd9TSap-znl9l1uc7psQrTMU-mKKVRP2vWWh2ECzorRs3mwpRP9kEvB4t2pE6H1C8_MEqdpbLP9txD3_sXe8umiNVHZucWG9CO018B321gDznVNlGZAOe50l_FnErhINWn2U5s--vzwr7B2JW1JDX6P5kyxZjFeA1fTNVioFzx4Fxn01YWMUv6Jr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار منطقهٔ ۲۰ تهران: ایستگاه مترو میدان حرم حضرت عبدالعظیم حسنی(ع) به‌زودی آمادهٔ بهره‌برداری می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/456171" target="_blank">📅 11:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456164">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGy8BgEqT-cIwksF97A-Ys9lpvIou7j471QhvMHWWI6tCUdPlZdYvKrzI5FpAIcmQdcyfncYJZj39HLyyeIo17DZrHcXAMjgU4Jw_DW1yZQACt2dNWiTP1Xa9EMQqSlzYC1PykChXZQlYUsPF7zDiqAVWl1SvFOejFFoI2mxx7osjB88jKbpRHDFsb8FZxtXBNyyZl8yZY4axC0rv_UwkxVYTHtqSBNsFw0JqvVtybkb_01P8TR0RQJylDNG0SV2mP_z5pKvLBC1KUsgQEbfoY5ZTricdZC8LCcwmrb7GrQqYUKJWpq0jPZ27WAUXJfEQYt_RuHu1a_uhozbNH9bzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WE5faVvxPQGq8O13SciE1jFUf8crl7BsP_bhpWXw5yqt09C6OGDXBdWOcXyyLRozSX9VtQqDmdX-VQp2bYpK7v7nVPIGYfRmSX_-62HsljVNiTZ7qyu-of8wpKl1kbNGJxmsQmIzWnBWqy1Y5Lbrs-bORP9Xw-2XndHb0LqTm18dcYEWPNEyH4TFYzmu-IDsROqu4WZ1iK5N-1ofG2rutzNEgk0iQ60jHM8BM4EXS1zrOkpEin2IX7_SbfuIDu3IZdnfAKeS5jC9UE1DS14VlQnlLnlFn222q6m0kPqYBolK5Dx9jNYZPi6XySp7su0BDMd5AM-Abs4r8K5SC9RxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQoG5H8JACZsxmBkILCbs4J3ZCwiJ0oaK8H9nvWeeY0BzsYDGV6lIt5WCET0aixlfthaaG2LccV7oQ7xcwj3VQiZKswH6FzcjRaj44Hkh5RgVJpXH_xMMPJr67YiQJ6XVkeU2Tyd8W9cTVzY1QrQHOdPF8Qo7O0AMFU9_xh_mAIrT74y9fR75_sv4WeAEc3F-svtQzwsXPD2q_Gs5SbunMuhs4Cuv_M-uNSHJ5SzN6XnNlG_diQ3dFXFdYRpZWupOyJiX_UNhhSHatTB-yN4iZXPSGRzlKouKJgMJH3nqDIt9MnImEDD3EzJQZD6a0Agi63-nmZ8TnXQ4g_nT2bSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ol8SZO8RaN8wlSdiYnPbMAzTkfhfqWnMNBnbF_rt6cVABKG0pmCWuagnbVH0S1aZZj143YqU6QOZ9utvj4zdvdQYPl6E4pqOFvNABgfqmxtvtPyDXd2XA9rU7100e6Tv0OQVKwM5czYAeinlTvfUtlJJbIigwNe5D4R-CyyCDrZJXb8etgL6WKLEqChgXwP6xGZ7e7PA1cIVtA3wRyCAMm4kzm8l4vKX5zs3Ta7iSEmXxPqUfBN43CjwAVU6G3jjYvkbohdVany_4qe27vcVychJYEmD1rCpgQa2ukaTnZYDCEqxgoVrghuvnMrjGgbTM13CU6QCVj2-sS7azH0kEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UgMeaxk39uAhai7Rxw6Ht8vKRhdRkYDdIK6v3Vn8QB-HF1Kbi9rcCNNNDDl5_VU0ksA0CgIgGrR1XvZqJTDTd-mArgdv_n42cX9K4828-3xXUP52QKigiym2X9P0eKnwWE7Wb_QFPAYOgHYQDM9gp7J3mFnKU9t7w59935yW5D3UAtZVfJTrWgZj7fsaau2dvyGaXl0OARIRq6wVVzAHgBoOwqHhUiMS3BKt7UqghhZUHOgwhNWPSEmLBl8Mn0IWMIP85fHKT7h0z2kzN5l64JbDvBw_GdIXoGeOj2DM3W07LIJ9jp4CcbQhYYErGUIQAucejYZY-1JLi9apxInaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlGlGW7rOqmgx79-3eMgCWiEYNIEXljBxwBFvnXXHF88XCezPO4QmixhflqiKii_GRotp-I0dW8SdIt8QsA20FvyUeLO1SI-YNDT0tLLWnz81xvtU3wRNApDU0bL1L8eZ1mrOC5XpFaxbQlv2nLQVRJU59crFyx-ROho8EMD5AIF9RpwUL1durrKad-jsYA7ZR1DlVPe0Y552_dTdLae7WMgcG8QrVEGfH8kZGuBSZr3lfSdfqajnW4DrtZkRFZG-knf30epdBJdQCC5-t_p0qrz_44kHWT6rmppdp4FkJqvR2Ejzh82X0qfeLktK2HZiKi7r33w4dMsn_1HqE2ZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUcLEllWIla1uJWbf894HtcUX-Et06PBDlIZB_FC8Pc10FiuGawQFXteITgAD4dqFLu_GLSVT664VcCEGJ5syY08jaSLU60z04N_p035GcSTiSykvhP7aHdn5gB0SccPhvimvYybdOLT1KR1v73zeEk2CoaVPwiGmE-B-bnExk2xdI903p--ljHn8IJoWMtw9k2-JzU1210xHU2mt1RPxrDCuMtyCxu3MLEBu9OQqlj9UttwkYENnhtMlO0A5mi2DooFu528kEFaLItrHXj1quS5LHEiBcIGKm6koFZgE4gtwgD-ejbiWk80pr33kNRJUHWQUN21syvI2Jin0B1djg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرچم‌ ایران در دست هواداران تراکتور روی سکوهای ورزشگاه یادگار امام  @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/456164" target="_blank">📅 10:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456163">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/necYsKpJ09UISmbrLnfGqsbyFy06JoLn5FVHMV8VNV3VwaIdiMX5wfcfz9n8CQiu3tdfqO_6PJY7g3G887OBRXoypCNeVH-M7M_H4wSARB62q6lMktYw0e2gypM3luGfeB0kNJpIJK-eAWyII64IVFyk2ostHvYKYpGv4jb4xFYHtba3Hm9r-RQ1BXYJwHSAoiRjs3G7nkrb2qZfCS4YL_PYHCPlTqpbjJ2jAXsNnxphHYU7eak_25uVXKuLFm-WvU7jSsSTnjtCSeMvTHV87YfOFfq2Dr_d6cZARFDGdXjLEVl0OwHumc1r3eL0BrETD0rlJIYqOSFuHf-8wzD2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ثبت‌نام دوره تخصصی «هوش مصنوعی در روابط عمومی و رسانه» آغاز شد.
🔹
این دوره یک برنامه آموزشی جامع، کاربردی و پروژه‌محور است که به شما می‌آموزد چگونه هوش مصنوعی را وارد فرآیندهای واقعی روابط عمومی، رسانه و ارتباطات سازمانی کنید.
🔹
در این دوره ۲۴ ساعته، از تولید محتوای حرفه‌ای و مهندسی پرامپت تا تحلیل افکار عمومی، رصد رسانه‌ها و مدیریت هوشمند بحران را به‌صورت گام‌به‌گام فرا می‌گیرید.
🎉
ویژه مدیران و کارشناسان روابط عمومی، رسانه و ارتباطات
⚠️
مهلت ثبت‌نام: تا ۲۷ مردادماه
📝
ثبت‌نام دوره حضوری
📝
ثبت‌نام دوره آنلاین
مرکز آموزش‌های آزاد خبرگزاری فارس</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/456163" target="_blank">📅 10:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456162">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-text">💙
هر پیراهن، فقط یک پیراهن نیست؛
روایتِ یک سرزمین است، یادِ یک نسل و افتخارِ یک ملت.
⚽️
کیت جدید استقلال خوزستان با الهام از
خلیج همیشه فارس
و ادای احترام به
شهدای میناب
طراحی و رونمایی شد؛
تا نام و یاد کسانی که برای این خاک ایستادند، در میدان هم زنده بماند.
برای پیراهنی که فقط رنگ آبی ندارد، رنگِ ایران دارد.
🇮🇷
⭐️
بانک ملی ایران، هوادار استقلال خوزستان
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/456162" target="_blank">📅 10:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456161">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/456161" target="_blank">📅 10:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456160">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsljmVXlyq9VsuBYSqw7VZoDKZUYRQ04dWmshmlU9t7mRckPkzz5o1cfgEtey6TMtWRNnvLaz6RFnSTSRM7yM9cgfiF1lE9YhmnAzr2l4yqcDajepjTJrxS96YyTON02Yc9tF9qTjR_ON3BKRGMnS8ECaGq7k8vhpG88V3IFpWdt9E85A8OGqnK_3WXtqYGI6najbhoteewmMLn56Ci8iOKvD20h0yG6pxwfQjQNAzt0iNZteExmOUqrUsiGwOyl-YbjrODMjJX5f2a1qEfp5aBzZUNjUzEauDSQzTSjSIDYtr6PYZNA7Ks0e_XqtjlopemFr4pQ5WNNrw3oaDoO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترقی: کنوانسیون خزر ایران را از مسیرهای اصلی ترانزیت انرژی و کالا کنار می‌گذارد
🔹
عضو شورای مرکزی حزب موتلفه اسلامی: موضوعی که مستقیماً با منافع ملی، تمامیت ارضی و امنیت ایران ارتباط دارد، نباید بدون رفع ابهامات و بررسی دقیق در دستور کار مجلس قرار گیرد.
🔹
پذیرش…</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/456160" target="_blank">📅 10:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456159">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2f723b6e.mp4?token=BUdiilLxgS8tgH0Hv0Y3RZ86X-RdYQ__PUdihkOEA1YXBCE4Hat5XooB1CU9MoDo41F97ABwZQBElMsh15kLtSHl-20RvUqoDBDJd-8bgq6FkGvO2xvs-gVp0Syvs01WWKC6lDHVz6icBkjs5kGTfugiuCJvroZBbWL5di4IRgA2j_Z4aU5MpZ-eQqWfoYotB8PVQjafy2cjaO24YqK-dtdbvy40du0Ew4JaO1yvPpVhDdMdPqvxrLI54LUefDFpHvoMjK3o5zbJQcY10vCdNkwoUExS_cJv1m8oOua-UivsDG0y69ViyayNW870A6QH8I7QDgRoX5O6dZaPMDZGxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2f723b6e.mp4?token=BUdiilLxgS8tgH0Hv0Y3RZ86X-RdYQ__PUdihkOEA1YXBCE4Hat5XooB1CU9MoDo41F97ABwZQBElMsh15kLtSHl-20RvUqoDBDJd-8bgq6FkGvO2xvs-gVp0Syvs01WWKC6lDHVz6icBkjs5kGTfugiuCJvroZBbWL5di4IRgA2j_Z4aU5MpZ-eQqWfoYotB8PVQjafy2cjaO24YqK-dtdbvy40du0Ew4JaO1yvPpVhDdMdPqvxrLI54LUefDFpHvoMjK3o5zbJQcY10vCdNkwoUExS_cJv1m8oOua-UivsDG0y69ViyayNW870A6QH8I7QDgRoX5O6dZaPMDZGxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرگزاری فرانسه: تعداد کشته‌های زلزلهٔ ۷.۷ ریشتری اندونزی به ۲۰ نفر افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/456159" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456158">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/456158" target="_blank">📅 10:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456157">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7870aa7ef.mp4?token=HqMAAYJI48--vDuFuEQqHaSgAfr6bi-_VpPaJ5vHQCVCu28Y48bqYqfMSN9l89pYUdfJO0UrLpVHFg1UiLBsbtNHOzETnQGEVHATj03GuBrdq1LubSXQfGvxKjk0tUIcgkV6KkpqbXN1KQJ14hC5vZOoUhs40EFilxVm27QoIkk81dBSI3TbsQIAqjP902e3m8hjq6brWXZEZvUceHXpug9i6wJYh6XNoke_t9IB9gv6YcCDxmlvq3-qkFCrRQuQnd6Ps6kqfIvc4wZuW7NriyY9XC8F0xVDcgTMoHBdRmhkJbZwF7VJl38U1gZHviB3dpla6ZOFTVz0ip4eYRXVBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7870aa7ef.mp4?token=HqMAAYJI48--vDuFuEQqHaSgAfr6bi-_VpPaJ5vHQCVCu28Y48bqYqfMSN9l89pYUdfJO0UrLpVHFg1UiLBsbtNHOzETnQGEVHATj03GuBrdq1LubSXQfGvxKjk0tUIcgkV6KkpqbXN1KQJ14hC5vZOoUhs40EFilxVm27QoIkk81dBSI3TbsQIAqjP902e3m8hjq6brWXZEZvUceHXpug9i6wJYh6XNoke_t9IB9gv6YcCDxmlvq3-qkFCrRQuQnd6Ps6kqfIvc4wZuW7NriyY9XC8F0xVDcgTMoHBdRmhkJbZwF7VJl38U1gZHviB3dpla6ZOFTVz0ip4eYRXVBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای اصلاح پست ترامپ در توییتر از زبان قالیباف
🔹
در آخرین حمله‌ای که به ضاحیه شد، مذاکرات را متوقف کردم و اعلام کردم امشب رژیم را خواهیم زد و اگر رژیم پاسخ دهد، کل منطقه را می‌زنیم
🔹
نتیجه این شد که همان شب محاصره را برداشتند؛ در حالی که قرار بود طبق تفاهم، ۳۰ روزه باز شود.
🔹
وقتی ترامپ توییت زد که امشب محاصره و تنگۀ هرمز با هم باز می‌شود، اعلام کردم اگر ادعای غلط دربارۀ تنگه هرمز اصلاح نشود، حمله را انجام خواهیم داد و ترامپ مجبور شد پست خود را اصلاح کند. این نوع مذاکره یعنی مبارزه.
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/456157" target="_blank">📅 09:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456156">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHKBg9o-R1jnbGDx-Mx__wiLVc-4pPWrD9PUKFmEMZGS7VM7ELd3oWCXhChVHbf_pszRm08wwOrem5XF7zkLg9yxnCxVbx7LtRwcjMmkyU1VDnV00x3WiSye7wgSn1owozOiGPwfsDlCtfwbKWqorLLvF1of0SmfjuGaATppeGKPAYonaIfGRIjyNACPrsIBzMZSRbTxs6NyFcEIGKlt7QoiqEHxATBagBJvQX4jKajRPxL33SVqLhQOvR4Gcbh4W8G8gLLuy66seSLivdgX_PmmukXQUYoz68dPfawfbE2AdHRn7ulfpYs4YkfIPjXSueHm_5481nn7oJvMRQ0N-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ‌ جدید حوالهٔ ارز در مرکز مبادلهٔ ایران اعلام شد
🔹
دلار: ۱‍‍‍‍‍‍۵۵٬۱۶۳ تومان
🔹
یورو: ۱۷۹٬۶۸۹ تومان
🔹
درهم: ۴۲٬۲۵۰
🔹
یوآن: ۲۳٬۰۱۵
🔹
روبل: ۱٬۸۳۵
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/456156" target="_blank">📅 09:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456155">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhBsRrlM1Qf1MTSfWrfbMTusKqJMivGO1eaJPsHgbkO_Rq86qeZbuHBX2hdP2H_bVYFizqMkaul3c7FY9kgeuafAHsLigDVIFp8oBwdr3UXvQjIrLxp_DxgmkAyEyWMZRRttDThXV-5ecOt-BBZCxQKijNL-Z1fAQgxbaPUFEFk_Pls88th4np04oNas4_NizlfGPYL_RyzExfmz2qWf5Ayw00uHYyiKmtNymPnw81cN_zEFHIyZxDPH7K2AawH3Ckg9paF4nwF2nXsuM13nVxrHRlAPWHxtBzxeto1AnL3KqqR44u_3kDnD6VJwXc2dVp7CjZHVAHh-U8mZUSAnTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مقابله با فشار خون
این‌کارها را انجام دهید
🔹
سزاوار، متخصص قلب و عروق: بخش عمدهٔ کنترل فشار خون به سبک زندگی بیمار وابسته است و با رعایت چند اصل ساده می‌توان این بیماری را تا حد زیادی مدیریت کرد.
موثرترین کارهای برای کنترل فشار خون:
🔹
انجام روزی ۳۰ تا ۴۵ دقیقه و هفته‌ای حداقل ۴ روز ورزش منظم
🔹
کاهش وزن
🔹
مصرف کمتر نمک
🔹
ترک سیگار
🔹
پرهیز از مشروبات الکلی
🔹
استفاده از غذاهای کم‌چرب و سبزیجات
🔹
بیماران هرگز دارو را خودسرانه قطع نکنند؛ زیرا فشار ۱۸۰ نیازمند مراجعه به پزشک و تنظیم درمان است و قطع دارو می‌تواند فشار خون را به سطوح بسیار خطرناک مانند ۲۲۰ برساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/456155" target="_blank">📅 09:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456154">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrkLsYk7JcPxO51nIUpMxrB4-iWDhZ54MQ5i3pLZdu6nphoVb_CcB6V0Ag8DYsQv2cBVN5caPV_kQ5sx7Ol8aSfgCSHFo9JvYXBHCkD73KjyCoRdBbnR6S7qpG2ADPjflCzLhZiL0Sif4myNniPZoduZoUwjwKC4cdVDIie4VW1Zb3ykAgR7GXUSJwbyJt9BfqUcfKBWHkbxLerJ9Lgji7fCLefsKVud7W_bXZNVdxshDRJo2fglrZGVcT8eBYyct-PIVrjjabyaXmi0OS05RiOMGByZIT6Z0zh22F1uyUrwykgUXT7c4d0N-RCJiKMkZIlTmCicqKcvq_-8iq0ymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی انگلیس: دیشب یک کشتی فله‌بر در تنگهٔ هرمز و نزدیکی سواحل عمان هدف حمله‌ای ناشناخته قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/456154" target="_blank">📅 09:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456153">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c890dc0fd6.mp4?token=VMj-Ml4ZagDunpMYink2TOoXP0YVr1yJXgHIpR0VIexNXE9w9fe2nbF4QI4sLFbsARbP8YO4e79pv1mI2m3Ee06UOZ5E77SFPms5N40wmcBVp2iiayCNXOlNHftOUpA_VrbRKSKPZO6KiXNDZ2N8aY6CD2BmubKgeIi0NPV7z76m77urCKmbdcuJUZjL4jC25DTTBeg4ZOa_KCpxbnV42rXPCpbY8AiwIqCL-H0x3jAV174H__JWWY58TIF2lCKcSK6B6DHWIw6N-QzUUClwRr7m84osYrG5zTlta-K27GeAz8_563QrhXNeAhBGC_dWQg95cDGhF0baT0ys8rKRCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c890dc0fd6.mp4?token=VMj-Ml4ZagDunpMYink2TOoXP0YVr1yJXgHIpR0VIexNXE9w9fe2nbF4QI4sLFbsARbP8YO4e79pv1mI2m3Ee06UOZ5E77SFPms5N40wmcBVp2iiayCNXOlNHftOUpA_VrbRKSKPZO6KiXNDZ2N8aY6CD2BmubKgeIi0NPV7z76m77urCKmbdcuJUZjL4jC25DTTBeg4ZOa_KCpxbnV42rXPCpbY8AiwIqCL-H0x3jAV174H__JWWY58TIF2lCKcSK6B6DHWIw6N-QzUUClwRr7m84osYrG5zTlta-K27GeAz8_563QrhXNeAhBGC_dWQg95cDGhF0baT0ys8rKRCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزایر دریاچهٔ ارومیه میزبان پرندگان شدند  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/456153" target="_blank">📅 09:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456152">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5oWoTWMLluIFoDanRc-OzFDUaCgrAU9gVYLDvGCVy3bWL6Tp8zr8Rr8TseffHLaJxIsbcB7TXnEmSRItMQy9pvYu8aSNYfFN_NcidWJSGZZSOiOgnDDHt94nKgYGxxkUBCz73uiXvk3pfJpwtzqKeCCigoxUblD6Ei6emeUIISizLA4Wt_0BZsLVIyBl8diU2jdr_eNfbTMtEanqxnFuSj8gHK_K0saQoodZ3lQ7dgavuLTZf_jxD3hNXk_k6ppWIMWkhRtb7rLnYB_B5L02C44k9Lmd5UEV-c4z6a7sWXFGo2zmiGxrxsna9tlTi9fxQSkwg64icWql3ns82XjwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر وحیدی: رزمندگان اسلام مسلح‌ترین ارتش تاریخ جهان را به زانو در آوردند
🔹
فرمانده‌کل سپاه به‌مناسبت فرارسیدن ماه ربیع‌الاول در دلنوشته‌ای خطاب به رزمندگان اسلام نوشت: شما با توکل به خدای متعال و رزم پیروزمندانه در شرایط بسیار سخت گرمای سوزان و شرجی سنگین جزایر و سواحل جنوب و سرمای ارتفاعات مرزی سربه‌فلک‌کشیدهٔ شمال و عملیات موفق آفندی و پدافندی زیر آتش سنگین، مسلح‌ترین ارتش تاریخ جهان را به زانو در آوردید.
🔹
در این پیام آمده: رزمندگان شجاع و عزتمند ایران اسلامی! پاسداران غیور، ارتشیان دلیر، انتظامیان سخت‌کوش وبسیجیان و عشایر دریادل و سربازان گمنام امام زمان!
🔹
قلم و زبان از بیان منزلت و تقدیر مجاهدت‌های درخشان شما عاجز است که خدا خود رزمندگان اسلام را بر دیگران فضیلت بخشیده و اینگونه محبتش را در قرآن آشکار ساخته می‌فرماید: «ان الله یحب الذین یقاتلون فی سبیله صفا کأنهم بنیان مرصوص»
🔹
شکوه و عظمتی که با ۶ ماه جهاد بی‌نظیر خود در مقابل خون‌خوارترین دشمنان بشریت به‌نمایش گذاشتید چشم جهانیان را خیره و امید به غلبهٔ نهایی بر سلطه‌گران را در دل‌های مستضعان زنده کرده است. شما با توکل به خدای متعال و رزم پیروزمندانه در شرایط بسیار سخت گرمای سوزان و شرجی سنگین جزایر و سواحل جنوب و سرمای ارتفاعات مرزی سربه‌فلک‌کشیدهٔ شمال و عملیات موفق آفندی و پدافندی زیر آتش سنگین، مسلح‌ترین ارتش تاریخ جهان را به زانو در آوردید.
🔹
شما با توسل به اهل‌بیت (علیهم السلام) و آفرینش زیباترین جلوه‌های ایثار حماسه‌های درخشان ۸ سال دفاع مقدس را در صورت‌هایی نو، تکرار و خاطرهٔ نبردهای تاریخی بدر و خیبر در رکاب پیامبر اعظم را زنده کردید.
🔹
شما که با مدیریت مبتکرانهٔ صحنهٔ نبرد تحت‌فرماندهی حکیمانهٔ حضرت آیت‌الله سیدمجتبی خامنه‌ای (دام ظله) با عنایت پروردگار دروازه‌های قیام را بر روی مستضعفان جهان گشودید و با تحمیل ارادهٔ خود بر دشمن ثابت کردید که می‌توان اسلام را بر جهان حاکم کرد.
🔹
به‌یُمن تفضلات خداوند به ملت به‌پاخاسته که حتی یک روز صحنه را خالی نکردند و با دعای خیر حضرت ولی‌عصر (علیه السلام) ان‌شاءالله به‌زودی با پایان‌دادن به دردها و رنج‌های مردم مظلوم و مقاوم منطقه به‌ویژه فلسطین و لبنان عزیز، جهان برای طلوع خورشید عظمای ولایت از همیشه آماده تر خواهد شد.
🔹
فرصت را غنیمت شمرده، حلول ماه مبارک ربیع‌المولود را به شما و خانواده‌های فداکاری که چنین شیرمردانی را در دامان خود پروریده و به میدان فرستاده‌اند تبریک عرض می‌کنم و بالاترین پاداش الهی را برای شما طلب می‌کنم و از همهٔ شما که مقربان درگاه الهی و محبوب حضرت حق هستید التماس دعا دارم.
فرمانده کل سپاه پاسداران انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/456152" target="_blank">📅 09:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456151">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌ زمان شارژ اعتبار کالابرگ تغییر کرد
🔹
معاون رفاه وزارت کار: از این پس اعتبار کالابرگ در روزهای ۱۵، ۲۵ و پنجم ماه بعد به حساب سرپرستان خانوار واریز می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/456151" target="_blank">📅 09:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456150">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ورود ۴میلیون زائر به مشهدالرضا
🔹
معاون وزیر کشور: تاکنون بیش از ۴ میلیون نفر از زائران داخلی و سایر کشورها وارد مشهد شده‌اند و تمامی امکانات و نیازهای لازم برای خدمت رسانی به آنان فراهم است.
🔹
بیش از ۷۰۰ هزار نفر به‌ویژه از استانهای خراسان‌رضوی، جنوبی و شمالی…</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/456150" target="_blank">📅 08:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456149">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD3RBYPzp6fpONvJkhQlmfFyGx6PoEbDGlMZCUWQkSpIV-Ch8XXeyk25VrVpeetRuzKo5Gd6-XHVfTzJH9W8KQsrViOecpQrqcH_m8ZEoX8Qc5Px83Slr42e4xPW5UYhz-4Ri2hr0wSaS9sX_wJ5zcTdoihW77m6JxDBfjPTo0wd94MHDrm9XU0LBLeQ0_E7OqkAg6KQ-3_4KNaGS0K9LZA4Ugc2tMP1eajIcAfQae6FT_k_r2XaYdBgWFJm7fQ4SgsFVo2LRpH4MEvHZmdGAItiP7zuypVxmxt6z76UkZ0FE6v4FExJrjsEKcHEHmGbEPdZ-qe-FremrwvDjIimew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ بحران در ناو لینلکن را حاشا کرد!
🔹
خبرنگار: اعضای خانواده‌های نیروهای نظامی نگران شرایط موجود در ناو آبراهام لینکلن هستند.
🔸
ترامپ: خیر؛ این‌طور نیست. این ناو به‌زودی با یک ناو مشابه جایگزین خواهد شد.
🔹
خبرنگار: آیا این مأموریت بیش از حد طولانی نشده؟…</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/456149" target="_blank">📅 08:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456148">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnXLqOXm8D56TqQm9IN2o40OytxXCy3aY2kgzV83FfXs5riLl1LsAr4saPF_6jWUO3zPLQ-_2pqZ4F0sR2KAzy2tDBO8nDKPAnBvM5FqOYon9C67tvN9NLEGCPHIL9qXr42GdZBjNkWVuDIOv0SzpvxiwPf5e9bvMpCLuVMlmRmWUGSIWUbnXDiXFpkB1Ohw00X6XVgVIX9mGr0holB7r5MRawsK3mBr00Y3J4NdpZ-cWtGx2tNnghV9BdwX7eJzarK3yuJwB5_dOPJM0i2QfQ-In-g9LGPVq2GlFHw-w6VQEwLRoUPL8r-EcmNeKyT9U647qIEkAAAQXrXTAmeJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای تهران در مرز آلودگی
🔹
شاخص امروز کیفیت هوای پایتخت با رسیدن به عدد ۱۰۰ همچنان در محدودۀ «قابل‌قبول»، اما در مرز وضعیت آلودگی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/456148" target="_blank">📅 07:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456147">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دریای مازندران تا دوشنبه تعطیل شد
🔹
هواشناسی استان مازندران با پیش‌بینی وزش‌باد و مواج شدن دریا، شنا و تمامی فعالیت‌های تفریحی، صیادی و قایقرانی را از اواخر وقت امروز تا ظهر دوشنبه ۲۶ مرداد ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456147" target="_blank">📅 07:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456146">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAD--X3v2Ff5qV1VhEDhBS9SH9yhXXaNQEJBS9Qf9iinoV5Ovr5DisfK3YjE8MoKC18BC55SSuqWbpAAN2IsdIm-HnKChgQ1KrplfpmhsC5Bb_Ti1HrxU50QCfqZOEBH_khntrnb_LgMCnEVPau6Jt3Jrfx4fGAlGYLJ_GAJeez4KjOVWuci3YaWKwev8fpAi5tOxwRdwdyTw0p8t7RkvErZ5bYA3BZgCwgy8rJtN_CbGt7tcKmEhKnJNzVSTFzycu80qkQaErJH4xomUP7obvFKeLLuMEluu4AQkDd9-KvOrqzD6hysaEzBz28yUmLkEJMbvf86UvpnSsWQPPbigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: آتش‌بسی وجود ندارد که بخواهیم آن را تمدید کنیم
🔹
آنچه در پایان جنگ و در یادداشت تفاهم اسلام‌آباد اعلام شد «پایان جنگ» بود. آمریکا تفاهم را نقض کرد و درگیری‌ها مجدداً آغاز شده.
🔹
ما چیزی به‌عنوان آتش‌بس نداشتیم که حالا بخواهد تمدید شود؛ ما «پایان جنگ» را داشتیم که حالا وضعیت جدیدی پیدا کرده است.
🔹
مهلت ۶۰ روزه در واقع ۶۰ روز فرصت برای مذاکره به‌منظور دستیابی به توافق نهایی بود و اساساً چیزی به‌نام «تمدید آتش‌بس» وجود ندارد.
🔹
قطر و پاکستان به‌عنوان واسطه پیام‌هایی را ردوبدل می‌کنند و با ما در تماس هستند، ولی این به‌معنای مذاکره نیست و تصمیمی برای شروع مجدد مذاکرات با آمریکا نگرفته‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456146" target="_blank">📅 07:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456145">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/394c607be7.mp4?token=WEatZyFRRya7TRNdrIVOtpg7qUf9CzmxS0AWx-lXlM5FqVbgwrXSWBPDOc0QRxprvrIQlGDV0mxc24ovg-XR0Zhhsqw6-ChrsAZI2dh4WVf6LMLeCwapKBDPiNsKOdUhPpIVZc9nhE9i2P82cbMq03Zt_MGkdSQJTwJ_grNLasW_-8IB0vDB-mPp-jp5Bf6xTTv7A7XT46sXEO-8cbZcWy-f6OFyaPUNyfz_EM7f6xRFgxnc2dY9u7DHweD7qx2LynkVC33DYlu1uTLbqtYUv6npo47DaK1pseQMnU9qRyZQeYBqTzLYvluBTj0nNbOXl9FUw-mr32rpvrT5litBCYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/394c607be7.mp4?token=WEatZyFRRya7TRNdrIVOtpg7qUf9CzmxS0AWx-lXlM5FqVbgwrXSWBPDOc0QRxprvrIQlGDV0mxc24ovg-XR0Zhhsqw6-ChrsAZI2dh4WVf6LMLeCwapKBDPiNsKOdUhPpIVZc9nhE9i2P82cbMq03Zt_MGkdSQJTwJ_grNLasW_-8IB0vDB-mPp-jp5Bf6xTTv7A7XT46sXEO-8cbZcWy-f6OFyaPUNyfz_EM7f6xRFgxnc2dY9u7DHweD7qx2LynkVC33DYlu1uTLbqtYUv6npo47DaK1pseQMnU9qRyZQeYBqTzLYvluBTj0nNbOXl9FUw-mr32rpvrT5litBCYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌دره‌سی کلیبر؛ روایت سبز جنگل‌های ارسباران
🔹
قلعه‌دره‌سی کلیبر، یکی از جلوه‌های تماشایی طبیعت ارسباران، با چشم‌اندازهای سرسبز و جنگل‌های انبوه، تصویری دیدنی از طبیعت آذربایجان شرقی را پیش‌روی گردشگران قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456145" target="_blank">📅 05:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456144">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcDYIjSKWjVlC__Z2oafsv8ij8n9_FU6X0by7_Dlq9RhzsbgMJvy-M1s5GPZhsX7QFTuoiyatOZV7815Es0jXxj-Z1pBDd5yg15xrjU6XvgrksvH7NO2zapau3EMjgUlt1fxzmX9lAcRnVYDkgD5WWD7o3GZFncWOB9o_50rQmKnKE40Zvsy0LfIgtkd51wSRV5FKA5B5lQv1EdbmsmDiKSeAYtZdow-ePay-bfcH34fPp5YAuDuxUUGqUBiwAhZ-j0yNCT9LV76ynnsJ_KCctUOlvjFAF84aqAGYLrKNcSwv6MoGBOpTqPo_ehGqLzvjGhCiaI0ck6EWaEOUjJlaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: به‌زودی و پس‌از پایان جنگ، تنگۀ هرمز را «قلمرو آمریکا» اعلام خواهم کرد!
🔸
ترامپ چند ماه پیش هم گفته بود که نام این آبراه «تنگۀ ترامپ» است.  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/456144" target="_blank">📅 04:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456143">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حج‌وزیارت: متقاضیان حج ۱۴۰۶ معاینات استطاعت جسمی را به تأخیر نیندازند
🔹
فرآیند معاینات پزشکی متقاضیان حج تمتع ۱۴۰۶ آغاز شده و تأیید استطاعت جسمی از مراحل ضروری ادامۀ فرآیند حج است؛ متقاضیان برای ثبت‌نام در کاروان‌ها و انجام مراحل بعدی، ابتدا باید هرچه سریع‌تر به پزشکان تعیین‌شده مراجعه و تأییدیه استطاعت جسمی را دریافت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456143" target="_blank">📅 04:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456142">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2934db48f8.mp4?token=PcdVhskccvcDXPyRoac0ki2Na-y3fnKMgxrGJRKdW9uAAc1w-0Rw0-nN9WE1k_gipXrp8sUduRO_4VyMTXzCx6CviFvxCTmYPFp7TPOGqqbGoqrX9rP0COzq805m86WVPte69nACAMcZCoW6AhiiXa2ZkbJvZGaIWJMU88OstZjwopDIVbtmHrNeinqQUf2FQV0hWIluMR4X5a1IQMdYplVj0gmy5GjbvpS3Nq9wdsQE4oDUCUm5BR-2_lpSk48PZ9zKS2xLM2cnwyINPtX6J8B6x357tt15tX01W-DgLPsgPc-VvISQr8gtjWrpY_ZzOSRrCAKfhHwDBreCd87Auw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2934db48f8.mp4?token=PcdVhskccvcDXPyRoac0ki2Na-y3fnKMgxrGJRKdW9uAAc1w-0Rw0-nN9WE1k_gipXrp8sUduRO_4VyMTXzCx6CviFvxCTmYPFp7TPOGqqbGoqrX9rP0COzq805m86WVPte69nACAMcZCoW6AhiiXa2ZkbJvZGaIWJMU88OstZjwopDIVbtmHrNeinqQUf2FQV0hWIluMR4X5a1IQMdYplVj0gmy5GjbvpS3Nq9wdsQE4oDUCUm5BR-2_lpSk48PZ9zKS2xLM2cnwyINPtX6J8B6x357tt15tX01W-DgLPsgPc-VvISQr8gtjWrpY_ZzOSRrCAKfhHwDBreCd87Auw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از خسارات زلزلۀ ۷.۷ ریشتری در اندونزی  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/456142" target="_blank">📅 03:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456141">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1e0003c6.mp4?token=NvGZ_paPF-AS6elMCU-0P8_zUpWKseZDDmlYjS2CMgka4H6eR1N_SqSMUVcWkeugsm4bphvcIwiK9C6Inu9oQaRTJWoK9UPbmo1XerQFsABuJ_Zupd9pBp-faG6nT4X2LUcQ-CpuuP5DJQMpEp33Q_lXWQcJIbCzajrPFKupzsZ9UPG7ekqqHGIWW3EMPDYo_MRxwWjLjgecQxPfexmFxGUAVcs-91hLChDvKR97n3zpHdmLwDroZj2pCu0CG4KTVYcvEk-u_p3PsHwKD6XfTYABfqm-JqY_ICtElXs1pX8_V_f7oc55NvzrMSuzCtmQapTzGb966dV4mhXW64SHHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1e0003c6.mp4?token=NvGZ_paPF-AS6elMCU-0P8_zUpWKseZDDmlYjS2CMgka4H6eR1N_SqSMUVcWkeugsm4bphvcIwiK9C6Inu9oQaRTJWoK9UPbmo1XerQFsABuJ_Zupd9pBp-faG6nT4X2LUcQ-CpuuP5DJQMpEp33Q_lXWQcJIbCzajrPFKupzsZ9UPG7ekqqHGIWW3EMPDYo_MRxwWjLjgecQxPfexmFxGUAVcs-91hLChDvKR97n3zpHdmLwDroZj2pCu0CG4KTVYcvEk-u_p3PsHwKD6XfTYABfqm-JqY_ICtElXs1pX8_V_f7oc55NvzrMSuzCtmQapTzGb966dV4mhXW64SHHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بالاترین ذکر از نگاه آیت‌الله بهجت
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456141" target="_blank">📅 03:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456139">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53c76d02b.mp4?token=MGLUThPrEzzQFd-6vFI5FP_TJfWXzK8XPaEqIAgbt-Aq_jkcK463T0-6UsWTxH4BeBdKueuN_jOrldTTmD5dFVcMva6dCpewNVRV-PZKZCs6HQk2hHjiMIXOqB0Zetome-DCUBNlLO0yS9Pu8_lprq3suMWIjQsi11Y_L9Ccu5wYCi8qwtelH213l8YTbmrwoRSvkiiEVIqfpUL2elVxhzh8Se7PrFO0Hiv20WJo21R-j8hJKIaCDEw6249De4Aom_DG8X1XusXvALLjEuiP1PbmWfImUBN7-Z0_GEEfhz9At4j3RkwthjA-WEJnK4U5AiPZZkmU0PuygSgE90nDTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53c76d02b.mp4?token=MGLUThPrEzzQFd-6vFI5FP_TJfWXzK8XPaEqIAgbt-Aq_jkcK463T0-6UsWTxH4BeBdKueuN_jOrldTTmD5dFVcMva6dCpewNVRV-PZKZCs6HQk2hHjiMIXOqB0Zetome-DCUBNlLO0yS9Pu8_lprq3suMWIjQsi11Y_L9Ccu5wYCi8qwtelH213l8YTbmrwoRSvkiiEVIqfpUL2elVxhzh8Se7PrFO0Hiv20WJo21R-j8hJKIaCDEw6249De4Aom_DG8X1XusXvALLjEuiP1PbmWfImUBN7-Z0_GEEfhz9At4j3RkwthjA-WEJnK4U5AiPZZkmU0PuygSgE90nDTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلزلۀ ۷.۷ ریشتری در اندونزی
🔹
مرکز لرزه‌نگاری اروپا-مدیترانه از زمین‌لرزه‌ای به بزرگی ۷.۷ ریشتر در اندونزی خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/456139" target="_blank">📅 02:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456138">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">امارات: یک کشتی ما هنگام عبور از تنگۀ هرمز هدف قرار گرفت
🔹
منابع خبری اماراتی به نقل از شرکت ادنوک این کشور، از هدف قرار گرفتن یک کشتی در تنگۀ هرمز خبر دادند.
🔸
سازمان عملیات دریایی انگلیس روز جمعه از دریافت گزارش‌هایی دربارۀ حادثۀ امنیتی برای یک نفتکش در نزدیکی سواحل عمان خبر داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/456138" target="_blank">📅 02:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456137">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">زلزلۀ ۷.۷ ریشتری در اندونزی
🔹
مرکز لرزه‌نگاری اروپا-مدیترانه از زمین‌لرزه‌ای به بزرگی ۷.۷ ریشتر در اندونزی خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/456137" target="_blank">📅 02:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456136">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f0b14a1d.mp4?token=R2TyyJ3I8GOrDoW_CLMfBu3LId9mptS_5mfKkMHGNHgyd-njOD9AD_MHVulmlfOVe5PpIQ8hPlTSDWx5GPJBdCMmmCPXESQsXRtUVl-rXe6o9o54F8ecvy0bomURk7A3ZxWnG2iH7XX8hihA9CeZCj2z0mJwOMuW2O6PTl6xhKsViimWiFXFDmpjrfaXsns3XWBtiXYLesau5p8ta_5Dc3Zz1ydff8r6BcLLQYYZPj7z6MmlFbaFC36GUsXayhVb6YZ5eoK-O5yR4mhrHrZKKraJRLueDSpqMb4RmVmpzESyiGZOR6xtMPHwlaY5Tva58wDtqPlTTFxRqwQmzQnVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f0b14a1d.mp4?token=R2TyyJ3I8GOrDoW_CLMfBu3LId9mptS_5mfKkMHGNHgyd-njOD9AD_MHVulmlfOVe5PpIQ8hPlTSDWx5GPJBdCMmmCPXESQsXRtUVl-rXe6o9o54F8ecvy0bomURk7A3ZxWnG2iH7XX8hihA9CeZCj2z0mJwOMuW2O6PTl6xhKsViimWiFXFDmpjrfaXsns3XWBtiXYLesau5p8ta_5Dc3Zz1ydff8r6BcLLQYYZPj7z6MmlFbaFC36GUsXayhVb6YZ5eoK-O5yR4mhrHrZKKraJRLueDSpqMb4RmVmpzESyiGZOR6xtMPHwlaY5Tva58wDtqPlTTFxRqwQmzQnVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا دریای خزر برای ایران مهم است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/456136" target="_blank">📅 01:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456135">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOIXt_Mx4YRiYOmxejMX5kRUWCSvyl8Rq9G5cvZgiFRbrfAUbnouMVqpSg_aCueR8zWQrQI5u1q6CaufjwczJK2CBIBh7WBSDSZopT-bKJK43jugT6ZMX2LMBanipzMm-qdVyRPwx5SAbPw2-QUkC7ymqfxgpdkPDa0AnxNcM3rUcTkBgvufIT1krw_edhHNyxAv9cC-e5ZPWV3oR2VyLivU674ZEImKZQnpXdIXhrf3q7ipMoZO9HraMkRmsb0FLeYgxH1UGJi1z9HAwWPrPqE3BZ5c4ptDzc3aTe1Or79A4INqrfU-LxcIgd_Uj_PL6JDlhdmlXe2sNj6Wodt6FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو خسته و بحران‌زدۀ آمریکا به خانه بازمی‌گردد
🔹
پس از ماه‌ها بحران در ناو هواپیمابر آبراهام لینلکن، وزارت نیروی دریایی آمریکا اعلام کرد این ناو ماموریتش به اتمام رسیده و به‌زودی به خانه بازمی‌گردد.
🔸
اعلام پایان ماموریت آبراهام لینکلن درحالیست که همین چند ساعت پیش ترامپ گفته بود، ماموریت این ناو طولانی نشده و بحران در آن را رد کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/456135" target="_blank">📅 01:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456134">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">منابع خبری از بمباران شهر رفح در جنوب، و حمله به یک اردوگاه آوارگان در مرکز نوار غزه توسط ارتش رژیم صهیونیستی گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/456134" target="_blank">📅 01:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456133">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eb9745744.mp4?token=gaclicWAfeptSMLTt12K6zC29icSf_Go_ALadH4mMXxk2A2p4JDx-Kmwtd53SUfCWqrqgEq_IUltWfzs90If8921eGBy8lB9a6Mc7rrOBJ5_RvJQ2rrPDTGNgCbUHs9Mp50bFfgzTEGIim5LKP7wLjCagLdUdaW6N7JoBT3L71SP9VCVSWR2Et4DKsWoO9wOUyf-m2mFcO0IeeoRmECIKRk6gvDLSYYssrxBENjQe4hfLjMHcE1szNgKoBCO9oJWFf50evJGVUyjshy08dFyim1hv0GT5P6gPeLBb5kKmxiJVw5aBVqHRdcTWqFT-6PiVRjRbm1zfjqG_4L82rk7BWQdtblZNx-wELyXt56Y14E1BpdLQZWbBmXUVMwyhq-fw5GRWEKtu8v8jdqiKlt7R2MLyWnXdtaPfGggMA4c-iXYpUdJy564POs0AwjCuC_Q7OIDTAqXB7K_KZgH4197F4zWl1npeiEfZwsoCVJ-DXT4W2Bd5nMB--9WOpcJvHZKNYfE_NXfwjE0Xe3PqqRRIlxxyymBqtDWWm2n7xfnUIueq4CT34YUbEIC8VAZCoOZuUp-b_OFdwZ21MsvRa8i2fOBRdckiQg6vzg_1G9_QyCAD04WG9_E9ReCrBW96KWFf6YljxeF90YnKEN1MXzJYi6UDk7tPleXMPq8By9dGF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eb9745744.mp4?token=gaclicWAfeptSMLTt12K6zC29icSf_Go_ALadH4mMXxk2A2p4JDx-Kmwtd53SUfCWqrqgEq_IUltWfzs90If8921eGBy8lB9a6Mc7rrOBJ5_RvJQ2rrPDTGNgCbUHs9Mp50bFfgzTEGIim5LKP7wLjCagLdUdaW6N7JoBT3L71SP9VCVSWR2Et4DKsWoO9wOUyf-m2mFcO0IeeoRmECIKRk6gvDLSYYssrxBENjQe4hfLjMHcE1szNgKoBCO9oJWFf50evJGVUyjshy08dFyim1hv0GT5P6gPeLBb5kKmxiJVw5aBVqHRdcTWqFT-6PiVRjRbm1zfjqG_4L82rk7BWQdtblZNx-wELyXt56Y14E1BpdLQZWbBmXUVMwyhq-fw5GRWEKtu8v8jdqiKlt7R2MLyWnXdtaPfGggMA4c-iXYpUdJy564POs0AwjCuC_Q7OIDTAqXB7K_KZgH4197F4zWl1npeiEfZwsoCVJ-DXT4W2Bd5nMB--9WOpcJvHZKNYfE_NXfwjE0Xe3PqqRRIlxxyymBqtDWWm2n7xfnUIueq4CT34YUbEIC8VAZCoOZuUp-b_OFdwZ21MsvRa8i2fOBRdckiQg6vzg_1G9_QyCAD04WG9_E9ReCrBW96KWFf6YljxeF90YnKEN1MXzJYi6UDk7tPleXMPq8By9dGF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور اهوازی‌ها در شب ۱۶۷ حضور در میدانِ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/456133" target="_blank">📅 00:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456132">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترافیک فوق‌سنگین در خروجی‌های مشهد
🔹
رئیس پلیس‌راه خراسان رضوی: با آغاز موج بازگشت زائران، شاهد افزایش قابل‌توجه تردد در محورهای خروجی مشهد از جمله محور مشهد-نیشابور-سبزوار هستیم.
🔹
از رانندگان درخواست می‌شود با توجه به حجم بالای تردد، با سرعت مطمئنه حرکت کرده، فاصله طولی را رعایت و از سبقت‌های غیرضروری خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/456132" target="_blank">📅 00:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456131">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎥
ترامپ: به‌زودی و پس‌از پایان جنگ، تنگۀ هرمز را «قلمرو آمریکا» اعلام خواهم کرد!
🔸
ترامپ چند ماه پیش هم گفته بود که نام این آبراه «تنگۀ ترامپ» است.  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/456131" target="_blank">📅 00:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456126">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sm_wdPkrouOmMn30PtH2ErgLpICsPuU-seZUr-wJti4W4qEmOeSvb31N-bLl6aKsWcfcQzfpBL_0tbTRwnsu4vvNORp16XuaehZat2OaaU2gVRhJ8kdhQZhBCw3jC4_VdsyPxmjXsJUkpPmFzAuMDYiuCeEpcb4TZu4qrE7s2qsROS_vsjZY7Jc05NH8R8GJQOkSMnShY7GiSTuWV_H0KVCc7PIw4VWDCDcG_CskZfhl5Kro637r_lQg3L1KKQ1bjz4Z6Z4ygKZC6xWW8sHIQ7_0agAyJtOh8_TTMZaDuzuJAawb9ot5qNm8HipKHR9rKgELQoRNuWjzYkTdbJb0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCcK2shyCqyvecygIaU5i_rXTZocfvNtPgRZeYLmMISOcGXIYnPn2dKCUmr1hqyib8rKoW19OChKHxIvQt9QIc9O7RYOEO28y5SeWwcru45D-Gv80ghmCmfzzaRWRxGHgqzRagpT7mnQDPlDD7VrqDb8I7BWnx3rkhtWYUudxSeIhzS8yXrX1S0wjkFxXA_wrFCYr6mWN8d0rW1AFd7PhIzrqT57bCcywoK6eLq6Ki_Vj2luhf9a8nrshnBr3Zvje1xWVYyrUJN0U2KcvDuM7K-m9KnZ2--P8vaaqxXht0dGV705t7zzYLYvHs-rG3nXQ87ke4yZLPQHT-VoKJqYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQrBAHs3_ENeNRa9tH7icgP7TwoaV48r2Y5Kbk6reKZR9irVxt7CXtaqgLJ8G-NQxDq5BMos3qdBTLv6Mwyf9hDjF0XDkrLEFIlIReczqGoBYkSY7Pur4Dsumngy3I_n3_f7QgUOq9-XL5nbZZptBsqh9JgKY0dMrD1sCd--i-Zu7K42eTCZV8yTGK4uY5H9vzVM6LT4Bz8BYWR8jUnNtp1gijquxJqIX5QR3T-BE5hLsPBrZmL8_TKG9Wr_HNn3d_2brwRPEIgAWUmFvFGWu_3Aid6GJdT633-i68Mc1yGkS0aZr3M_MGfZ1N8Yd2W8u6G5_8DAfh149zrd2aSx5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmMHeUoKkFPQ1DnaSI6-5e1XA7eAcbJeQzQj67FF2JzbVZyEVkW8XZU3M5RXndEIA6Bpz8cSBXJId9LDv9iDC8cEItPG3pMm2bMXggWG0EDP9XzzOz2p4wcEFRNI7J7-XcDw54MoWZjIJYcbg6Zvx-DQvCTbgGs_4vp4fWNWKFq2jL8tLZWAh8qyj-P1DIclEi3u9M8590QapQFGPasUc0RWtXXWK-am1C4VUjDVSYwoJ24_WzPDYSuee2-d6FNCNZVgP1Z7_GLlXMUeuKMlTzn2bnlHRRs2tm3maM3PfIq194CbK2DGx-pnU_wEgi4dcG9GqLur5qmZ2sU8_aNtew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmwjsL27Aq23GNHz79Ik1XKbG2kGyEYf-G5jnSpNoJvum_kumk79C8Q00bTsp-y40jmKdYlYFzJP-DAdJ083_ZWF3dc8KCUAbaXmd-1KlgNBmurpmkHEGItovjy8kKGbbl-8pNUABOEuEyGOSXc6baO5DGd_Mb-Q55X-wwFrTgaR6Jbjz68GBe500f4M0100_hGXXbMqu278eQYdpDjiW6iIk0jpygkoAyIX0jvCTT7FvFT7Y5WjVaipGRC8pyhsYuOhwrLcS_GlQI-LUPCkr3mI1WDZjy1lZhOrH865W5aRYveVCSev32li-uvZ80X7UidS6ArbGSKB8unWsqb-bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات پرش با اسب در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/456126" target="_blank">📅 00:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456121">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4LsRbkMhDlw42WNHkHf8ufZyBQiseRMlXjf01RINFpKIfO9BdKjCOnBoXavXrlmnmpiIDc0apVwDhKBO65Uxx4V74hXT60tbdiXDQtK16qtH8j2FvNFvt-7Tnrdgrk6kwRYz_4GeKHAs44GvWbrIX-u4K7OllSi36B88WOOJZ0q-hUIlxHm7wxV2CUKrEGMt-m6wZiNF6MGx-pu__Kr0tIYH3TIRVCezK_g2-i-7by71haq7_2myp3RdxAc4wCFo67_WUJ08XJRK3HPYQc-i4ZOK_JI4mOZDpQQ9BhCad9G30uXXcvkUg1AI2WH2IX6zmMyWyPMw4im5AeUCH95hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Avwq9CuKQ7_zq942YNDVZQspUNQTsbl6bRvDc2pFn10LDu9kpnxS-Mf656DQIgEVxqvsnPXSYqq6SFIx2MJM2zarKnWhedIJTMGlS_CPdca1zE62nmTZy7neJj8wrpwMj3_HFV-XGPJD-EwMgxCpua_ADDlrcFxwoMRq86ZemqaSLUpYp4ACS_8q0hVLiQup5nK834rcDKpfkAZWUBhBpp1CVY-bftlbIKRkkvkq8AfLbpdj-3gO1phRQ_zEQN4EwPSFgrW69uWbbiB8wFYx95T6coUuGUNEh39NJc0TyaRSB7IXk4sUiF_NHMx3yNoz1eE4w4oyeqXwNM65Xcg6gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzm1TSRgxkTj1BMtLYeNxdzq3_sMRvOwot9KF0cVnY5TWPmLoig-P1zpwo2c1YvvCFwSz1xf2JTlKt6C_P_Qy_nWOVW6fA88T3qljRy6BNDXhkB3yzPNSmihftbTN0RgAgorgCIE6I9IllVIDRWu7Y0t9lHnzz4tQ3AKb6JGWl9Pdk92FBILIn8u_M-kJ-ebu-R4xRd6KaIdYAhOdYtjbV75YuPUxcGD5_Y2uEKeoH6o_4BLkfZRVua0mmV5PicHRl5aOXwfCgXddbHObF60QdvmpLlQZKBf6p_qnSSY-CtLh2vaqCZocI9-Jc1GIui21hoiI7xmYAXmm_QZ3dV0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrAPyvNzJtn_LKg5hRIab1JvoFYswBQ38sUTtgIhecVJDFWn7a-kZkmUgoCjHHe0M5gWbofrCNLjVLOErPzO9niXlU9vDfhNTNQwj4PSiYHxt2WeIKfyhkRxdlpfrbOXoYGAqmHEyvSdM4kqGitDsyGz4L_wfyGvC8y3HaVx7i96OD7JYP9acMGIOrM_Fd9kTzR5Sa5KN18BLLIHEvES6108T_dorQPzeJqLSMO-4XsHcQ4v4OS2HO01iAOYakiTEdIR60D-eADnE54nci8cpPAtFoe3xR8HBhLMHPMIP-xqAiywJs5WAFUXc_6hSVCX7p0J7mY7qdKZjwpRqlhZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqWJV0rUTFxzSD3JwMhCGr4-MOLRGqOs0Me8jcGTBRJojyeaQNht4xmEvsL4sb_F2bF3xPhnaL5RKVCSaW8Gj2mLKY0IDfA8oXIr2owA-j5l_WmjR8lpArtIScwyqkf6M9gS2wahfNqW0IbJqkcL8EfnhY7mj6MWS61zie0BsYIIFLJcQydX08GC-BlDoyNvUOrkxfT6XEKg0v_4sg3gnkLLA1sqRXIIFWZUcpo8HEcYjvViaMha_Xb5QLQmSVk8JqXvDxSAZFwSty6gHwTQ0DRawhcqAKttYMf3oYQxG1at_IO9MfNPHQpgunC8ehk_x-cK4aYQ58q69MkvjFR3hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲۴ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456121" target="_blank">📅 00:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456111">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oA1N7Y2nuxvUfQThIJ40ff2VQdKxfxG6VOwTUUe87xsmlTZSfx2z1YFl3JD2TMfAkIQ_AgUHrOsQo6hMvX8UqwUxLAnXVP4kRAyArZy4jPmR8e_s5QFI5MKM0SDWHugRJBd_Vxs-gSOgmxrZozM9EO5SYirLxrbFG5o-epA0oJKQPzxPvmGE0MH0HJILAHpvOEk4KtJv-TtWNPmiteRYzNCylDR6WWo27Lwj7oeZF_zteeYl39vw6nWfQ9vW2cxtxVWxlfBpA4NCFtDaxywyk0SbMTeecQeulKQ2osA_ZIkR0Aia53aCsIH5I_VsEfozEZB-FORquUn6V3_5P4cbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ByWwTtp9h5kzzNffhZUvJ_u1KGnUKbGL8bbJIHCw2ZT_omh6KakXXfuTq9oXfCYObNq_JDD518eF_3aQHzBUtLl1leQP4CoL7tbSGNHJmqdz_k8uOBBXgDk7UV_lEukxZ0fzlASCr0mWaZv9MpDFfnzQWZlZUoc5aTlTXsCOp5nnBaNBosvN4S5TfVb4zli1Zyy0c2yxulBdxxLxYZTe3vw15nXEiUW1aUcxCqbU5yBklkmiOyTuADvBz1my4D25vlKuzMoX7UU7uNUqerRVgl58CsH0alXCjQAaoYvNgaw6pEG3oujKiYPq6hROTOg8eqTYZheTcfonm9BBwDuwYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9LyyzC-58EnifiSFGJZ4OIkgtHNsvxMj9miu-fE952cicLcb_WqEmcWmL5eRBWfwUzKavJFZJ8B2motx9ngt2Cft7RbbUuRFzQ_YG4wSnp1knRqHFfhgwqmzrEQryUmP5EXBjtspgDkEJWjp07dFIYLKloG1QhUIhtxgNKXSCiDhYRpqVHyod6dCgM3SrqNhfPepwXEzz2B9VC1zVXPBizqhTP5LrkXRdhlpCE2gXHsgP2BZJ2QsGvxao245NpL9coK_pqEuM5nSHyWvdVWyaMHAcMBHzHip94Y-Z5rlt98QWgbp48g7NMl1CcUzag7h_GtuhwpZJ6CXkeDHJbzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9QHmlfO-vzyNExYvc61MBretoO-ZsXljI03GF-jz5Ka_laBhTEirrVAm3trCP99IDJkdVHVhgjZK2MjYiblAN8uqZ5wYF3Xjbcb4oePu0vhdnD_4c2KHTLDwKBqhgqtHE9Qpx6K7TiVyD8QU9-M26mEbhbbZjFdsQkKt6D4jbMJ1HUuxHu70D8SZj-AYjEIIttubFaQn9khCWo-7LxStzO5rnp9kecP-0RhS4P_qWHx2-PrbaOiKtW_GfcU9R11eguLpcvYjfsA2ViqPbIZf2K2AkB7JmPvk3Kindbm5eVvpBq0kSL9w3w0SVZnv8MDSMQNdnyE6d9_mVg4jObPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqjrO6TnNRQHqr6Wr7FnXvBl6r-2NYAzWWC3U6FIhKRHeTgdsrZXQVkfWlaEZWRuFnjsIRsZgMdtK-2t_H98mYZT5MMacq9SQUeOw_gk7LBGLUr8AvTDMzW_K4Ti4tAfDSKx1UjWJalwIV-pC3tf8EFADbnZX1V0m9SF-rRsjdXSle0kbRzwOERb77mJHbUfK2a1CsNkYyrBDYVCnCbedtD8zwqgmO5Dc3cpOHnzgmpuOFPoP5Tc0Z_AoA-zqV9JCyloaroqPBNC-ny3lKCgJRBuv8uWu0Z4ff0eEuot4slfH9jQmrD9QaejZ9-v6vJNlGh6f9i8uZObwfbAFu851g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fLiUrB8DhFmTLAHfp8hmOV3XdDzPPSa8JyGtSzYOTLR6EBQEu5Ok1u6pvgO82hh3HmaYyxuYl4EqihaZjgioD3gULloRgOU1mByxJHa5VDW_ceJVXMj-kpL8VnYn71ijfuXQeJxSyB6u6bW2WbWYT83UQSi5A9vQCuM9kG3ayLcDFs84bTekDRND-Uy0GqLHsBUvHZk-9byl89AS-ox8VMWOibtaWxf_ArwCKr58Hyt1XeRxDpeSYGyW1d4uOsUmIW8cDR-l-gECDbMMWFYvoNc7sEKJV0lcdSeDnVhzRN1Iza8hoqvy_KhtXEBt5hBFqmdKtXooY5KNp7NYkB6cvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9kOaByssZ-mScBYLN_eaYX9H1Xoz0XS8N0oBjNJ89ZEIDJF5tBsgysxH6b28aHTMClTC8342MpJ1v0sd3m3gOHP-yPcP7HQBvheOlVr2XIz_1EUhc11ugZtMoRCfn5K2-oM4AxH1l85t962phN4wOdHvJm9Wx9yg48MZ1DD7Abpi9gBKQU80rYOV4G2WmiipmOqJtp8ipsqWcKqGZG5fLkXfTh8jPkieJSQkzBi5tSc8EcAReIwtWpnY5W3OCR5cqimnAIk0CjRxceasZGhoqrU6wrl-prY51BRY3nfPrAjOmxPGn4vCzKfStIeJEnTooUfTnf6cHVYb504q1hr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVYNLq1LD6TTyYNKsJAgeq4wAyfTic9kFu0nDN3DliU4b2KcHKKDLBIyOaWATIqXDs624Ore2XhwIasnCJg4daGu5DPxZkGh7oCj3OiiW1iL_pgVRmijKeYziAtJmrTa0_IBn6DEUW5lF5LKJGMJ3KgU8lTWCTN7cEiV3YY5KAHV8k-PR5R41vR71BcnoTBcwzzNTJncPXEQqHQJRR7qDxD4MPu-5i050nc5WxFdA6L_bkv9u46ixZGFqSC36qEVVfELXrx-KRH78yIcqe5hdkd8GzcMEwxTpNkVo_mw3_8CZEO49PzeERoBxmoczCJZrQzpU_mpcJM7oFpxmcsyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwafjbRC8P1kNVLMLXQH1v0u3PuJ8yNQQZFrf8KSZ7ndMwPigkij9OxJFiF8vjNxYO-ak1Pnj1ZyAMFvVf3Kn8Ba2QF-FxRdOVHHeFV8kMMiboqEVB1S_unwt_16hc0isC3ed1A8dymIw0sSf1vj337tvRABIeATJ7YTrNeL2bQ1mdAjoIVHgsDS2igM0nGUYH8f6NwssSYO4ZJ9gG9NScUUu9N4xd3qkcdBBo1W5kuCk9HqwkDBc6_emWsPuNZBPNbQMnyYkrM_9xDfrCEV0nPUwtg0Lq3-OZVipcIZdVL_LBK-7lVE4fYUp4rFGDd0ruZJHQmI27YUW0fQBrU92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXwGgN6QigIfqCNotezqqklm5pBrkjreGR-3gkyx7gdyQOFQKii4lamH29r__LMozrWo7a7euDOhQqSH3JCJp2zvN-DdAwLIIDnKHDnAZy8_eQC_SNGRJXt1NRLyr3Qiton53WN5_3vdgyFZz6_38EHoLHvdR6aOVux_4BWsdDRlQlWbXQ_Pc2TN429BapoCqu_FezKhnGO_kjrADvBS2HSI0wyjgIaQsLpxoxJ9cnxOszgkqaFatfuhxboq-4P92AN8re2_a1Kg1C4AD-UJmNDpBm4x4oz7azbY-_lLdP_2vnxjRBHoDgPoK1mQIlaK6TuVJsJjyxErC7DUiFmf3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456111" target="_blank">📅 00:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8x2DZNj_Cx5wa4f5yEuVq-PBgEckH-2bbWqU2lUixm_V9oIqQeEbHaIPRnlppLLbGHoHrZeis1RxSVh4qMiZVer7-5I-bG1GXkPuEvtNqrxanyd3UUhwaAbHxwatu2A0bET9NeJxdvI2Ki3OmbJq7yKxQFvJfEJRzi0J1MLus9C--bhVPFxbFzGFcCP5UOQFSGd5OeyLmZRON7OSrif4PRi8GsKH4MIHVhT-jxtrT92dHBqH2Z66Y_C1tIGwDZz-LeDl79tybppnDFEvxq5phtbsmCJKpuAoj3O0f1ElnlkNIbiTDSPwxpq4bqIVJ5zxXc30mkK4HLjuFcyMZJdRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lD2f5zAiKtaRNvXs9P1iVM0AtRDySvgovlaXX6F2ES7uN-shPp8N5Sus72LzvhoKFtYpQ7cC5AHdemPFOVYVQRN7MqrtgzdWEJVflXs5iPftSYWmMRcbAEdNA9EPrldu_iGgZknewdnbVT-ecqbScBDr-MwVW8b6wIJ3hwBpzeEptrqin8yxgVB782PiSr6uJ19yUzMs1X4zAui1kKahahimRahkk2FzwuBPUpj4AOB_LkLkiR2cPybcVvEAXCgpE_aWHI5B_pdnEM8WGQqG6r6kI1rTqNiWU3x20Gr8VOgbWUQtlHif593XHeey18MBL2qVx2UCqb--IfLlcFv3pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرچم سرخ انتقام دوباره بر گنبد حرم امام حسین(ع) برافراشته شد
🔹
پس از جمع‌آوری سیاهی‌های محرم و صفر، پرچم سرخ انتقام «یا حسین» دوباره بر فراز گنبد حرم امام حسین(ع) به اهتزار درآمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/456109" target="_blank">📅 00:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c9df1e95c.mp4?token=f7DLgUTMZacfFhiAbhXJagbJ_sm6SmfLefNHxlzgPn1EtR6g6cbPBqtH7YYm0C8uK_MeAZ8EwVk1n5g1cEARn21QER03i70Sgk6dJHb6g8lSmk2oZSKqPiyeIFqQulHVseNovBRwpNEd-0bqo2-ypIHZ0l_qe4KCboFoobCHeJ0piZICIzIMnkD_uFRpvR1Ci19WlGACtG1OTXOg5WgcouU6yXyOqmnGSzUXc60JeIDdnTcSxLBv7WPpaAgm6IXlRRlSvwFmTMNNIYWkxD2sUrToFpZObqtnT1UL9N5itRIlklwGCQuzO9SxwTFoBSsVQNRDpV5q5awUAHAMcNyptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c9df1e95c.mp4?token=f7DLgUTMZacfFhiAbhXJagbJ_sm6SmfLefNHxlzgPn1EtR6g6cbPBqtH7YYm0C8uK_MeAZ8EwVk1n5g1cEARn21QER03i70Sgk6dJHb6g8lSmk2oZSKqPiyeIFqQulHVseNovBRwpNEd-0bqo2-ypIHZ0l_qe4KCboFoobCHeJ0piZICIzIMnkD_uFRpvR1Ci19WlGACtG1OTXOg5WgcouU6yXyOqmnGSzUXc60JeIDdnTcSxLBv7WPpaAgm6IXlRRlSvwFmTMNNIYWkxD2sUrToFpZObqtnT1UL9N5itRIlklwGCQuzO9SxwTFoBSsVQNRDpV5q5awUAHAMcNyptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: تنگهٔ هرمز یک ماشین پول‌سازی بزرگ است
🔹
ما امتیازاتی گرفته‌ایم. اکنون ایرانی‌ها باید به این امتیازات پایبند بمانند، اما سلاح هسته‌ای در کار نخواهد بود. ما قرار است مواد غنی‌شده را تحویل بگیریم. من به آن غبار هسته‌ای می‌گویم. من دنبال تغییر رژیم نیستم.…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/456108" target="_blank">📅 23:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHbcwoI9VDoONuIsK5wYy07sjiocSDczIlX-1y74J1WqVKlKkRT5MInI145Jg9YkzNZs6QL_nYu2hhmSfzdRAwYPJP_Hvxw3gPuusyPb3idS6ID5qMuveLAt-Yhjyds18UkyVdadzYPdTIW80WxEOsTZhbbboP6_oPKgoD8yKA9jwc02qnLBVHSlFO4lBsjWlnpjZKVUtA3OAXzGXHFXB4PyOiUFTI-y5XwRv0pjh5nJoWAIcdeLg1JuAwwdVOav4ETA3OAgdzqfmCW1MYjicyv3Sc9wjlNOmi9znsnLNMWTJLbCQsy3j3l4DoEx_R3Qhyt5e0xcRogwFXhu93L3Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدرنشینی استقلال
🔹
جدول لیگ برتر ایران پس از پایان روز اول از هفته اول
📊
نتایج:
گل‌گهر ۱ - ۰ نساجی
سپاهان ۲ - ۰ چادرملو
استقلال خوزستان ۰ - ۲ آلومینیوم
خیبر ۱ - ۱ فجر
استقلال ۴ - ۰ مس شهربابک
تراکتور ۲ - ۰ پیکان
@Sportfars</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/456107" target="_blank">📅 23:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456106">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f438219c.mp4?token=g4mwCHT6yCVNz2ljPpoNfWldd6BF_Zs6XXCCRVhiRqs_6TqyMDfSdYwg1EvgrYj7dlifjat-LxgLu1ylriDjfNFKfWFDBp8Vb6cCBTpM9ynKLrryUmzep-QVXDKhqp0uXMUrjq2ep2aMeddPTQKrW3yBm9QMk56H-KDSgHk8bB4g4h9B-0ReesAQbor88BRvmqRhGOE-FzMIYLQECH0iyC0cRA2JBx3voEdvwLkrtBLGLSPCBbgUQFiDGPyxIbiV0H-cpgifkJziQV76-USfmif9hPou0DgvLDiGj4glAJrPVKTrmhgyHGxGkkBydFBN_EwxTkMXyLRUeGoL4OJU_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f438219c.mp4?token=g4mwCHT6yCVNz2ljPpoNfWldd6BF_Zs6XXCCRVhiRqs_6TqyMDfSdYwg1EvgrYj7dlifjat-LxgLu1ylriDjfNFKfWFDBp8Vb6cCBTpM9ynKLrryUmzep-QVXDKhqp0uXMUrjq2ep2aMeddPTQKrW3yBm9QMk56H-KDSgHk8bB4g4h9B-0ReesAQbor88BRvmqRhGOE-FzMIYLQECH0iyC0cRA2JBx3voEdvwLkrtBLGLSPCBbgUQFiDGPyxIbiV0H-cpgifkJziQV76-USfmif9hPou0DgvLDiGj4glAJrPVKTrmhgyHGxGkkBydFBN_EwxTkMXyLRUeGoL4OJU_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دغدغۀ من معیشت مردم است و نمی‌توانم نسبت به آن بی‌تفاوت باشم.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/456106" target="_blank">📅 22:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456105">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c8bc4c94.mp4?token=lY2w4pnnWGOln2fR0eV0Ee8pFUKp6e5nrHTmT-20L9HJGNouOXlkGpwWhmaNvVsIvYUQnT7aB1rZ1fwjRpVB0KVY2H5PpARxglirUjFjE3LQn1MQv4a1BJCHVUOEJaA3acNY5_BqtegDksrLUilytrGKmMRn3Oaa2Lt1vOvosqkgX68azhgi6JgBcdCXEnjXCVcDcGznFsiEXS3RlQigCfWG5SZoKsBOH9wy9kUVz4Q0P9eFZY8X_X-jDdfeRg_SjDoCrRbsY6va9pXd9HGfXvkCjZsEWt1Klkypc-aKsLD7lFPB4mlzkRp4wTDUI09sOxyOWvr-S-2V0KAyxUkLsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c8bc4c94.mp4?token=lY2w4pnnWGOln2fR0eV0Ee8pFUKp6e5nrHTmT-20L9HJGNouOXlkGpwWhmaNvVsIvYUQnT7aB1rZ1fwjRpVB0KVY2H5PpARxglirUjFjE3LQn1MQv4a1BJCHVUOEJaA3acNY5_BqtegDksrLUilytrGKmMRn3Oaa2Lt1vOvosqkgX68azhgi6JgBcdCXEnjXCVcDcGznFsiEXS3RlQigCfWG5SZoKsBOH9wy9kUVz4Q0P9eFZY8X_X-jDdfeRg_SjDoCrRbsY6va9pXd9HGfXvkCjZsEWt1Klkypc-aKsLD7lFPB4mlzkRp4wTDUI09sOxyOWvr-S-2V0KAyxUkLsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: شکافی بین دولت و نیروهای مسلح نیست
🔹
دفاع جانانه نیروهای مسلح با پشتیبانی مردم و هماهنگی همه بخش‌ها، محاسبات دشمن را برهم زد. @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/456105" target="_blank">📅 22:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456104">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVPHj1bPDoFxEd2XXWZoT7Gsg6_UiT3p1D7MTqqrqiUPzYKXCOEGrCAdXm6gbWicEmnY3Fh64Xuva3dCuuhv2VzHF53hEccDsv_VQz0zCn3Bvg8K1-_SeV-zZM-y_oIzvBo8ZhkhWCOKUK4s0guQA5ChwXpfBs9ka8TYaZ2MCH-UapAQfGlNCFpERgyc54j9b-RTBYz52Xll46cFQlcTqxNcaMQxB9QfaFtLBeyZ6BVNiXMbf8lcGYm_8UFq7CAo0yYDml0ivgR4qghu6VvskI3wTtY7FXatGs38X7C2h9u2wwLSzChxLWZ41n_DNzl_6ZEfhfI8dR9o_CMFuuWxmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نیروهای مسلح یمن: تأسیسات آرامکو در نجران را هدف قرار دادیم
🔹
یک منبع نظامی یمنی از حملۀ پهپادی نیروهای مسلح این کشور به تأسیسات شرکت نفتی آرامکو در نجران عربستان سعودی خبر داد.
🔹
این منبع نظامی به خبرگزاری سبأ گفت: «نیروهای مسلح یمن، آرامکو در نجران را…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/456104" target="_blank">📅 22:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456103">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca76598f8.mp4?token=tlpyMdUcD8cfzzg2KzG25uUoRaeuUSNxj-INsm4bHziXAqzXPiioepo3IEZxkERe7jZp0EaNYCUzEV_1Cb1lemgMB5uy-XNX5OMXWVHRtCwxBwQAicI4_YeY9FfwVZSLN07hhwH2TsFDT1CviTsd_mfPYodjmOTJvH9SKC7PltHOG1XK0lNhdisP67LNMSPxzuEdL82pVmG1MdASz8u6SrZqup7VKT77c7Oiu2dSBC9K6nZC3s86KmFl9331rXllNhYlzV4_DGcgf8MfOSwpxsMXqrv_sNtkb-9i28GlvTQhPqN9BS2x4sJmODz85VHfr154jzbH-TN9vO-ty3R2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca76598f8.mp4?token=tlpyMdUcD8cfzzg2KzG25uUoRaeuUSNxj-INsm4bHziXAqzXPiioepo3IEZxkERe7jZp0EaNYCUzEV_1Cb1lemgMB5uy-XNX5OMXWVHRtCwxBwQAicI4_YeY9FfwVZSLN07hhwH2TsFDT1CviTsd_mfPYodjmOTJvH9SKC7PltHOG1XK0lNhdisP67LNMSPxzuEdL82pVmG1MdASz8u6SrZqup7VKT77c7Oiu2dSBC9K6nZC3s86KmFl9331rXllNhYlzV4_DGcgf8MfOSwpxsMXqrv_sNtkb-9i28GlvTQhPqN9BS2x4sJmODz85VHfr154jzbH-TN9vO-ty3R2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاش پنتاگون برای پنهان کردن اقدام به خودکشی یک ملوان در ناو لینلکن
🔹
همسر یکی از نظامیان مستقر در ناو هواپیمابر «یواس‌اس آبراهام لینکلن» که هفته گذشته اقدام به خودکشی کرده و خود را به دریا انداخته بود در گفتگویی اختصاصی با رسانه «ام‌اس ناو» به افشاگری درباره…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/456103" target="_blank">📅 22:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456102">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a620415e38.mp4?token=VQ9TLfXqxpptcXdbnaT6Ok1wyZOmgVhnXyrLK96nhlSjtGIB5I7H0V-PbhJWgWMugDN7Vzj4-QKVT6Z0HqelcuIAWumHXi4tQZJFk3Rn3KaTcGX1LgWuhm63R0jIVUqII_viU8NjBURgxzgRDdHHtI_RPvWM6FE1cMhbhaLJlcDpv-MZbQcrTCt_-b9rrRlxuhHkFN_j_8a4YZP4gtPG9uplVnPVxhIolIw4zREI7oL9S8DPSPYsSZ22jJvLpvA5Pe1HFyC8CtOOqMIVLoJgY_Hk8XWhpVa9r2z8wqSF5Ue2Ppq5zqxF3M11ZBxPEWLF82s1n4vUqgPv5y890-ynDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a620415e38.mp4?token=VQ9TLfXqxpptcXdbnaT6Ok1wyZOmgVhnXyrLK96nhlSjtGIB5I7H0V-PbhJWgWMugDN7Vzj4-QKVT6Z0HqelcuIAWumHXi4tQZJFk3Rn3KaTcGX1LgWuhm63R0jIVUqII_viU8NjBURgxzgRDdHHtI_RPvWM6FE1cMhbhaLJlcDpv-MZbQcrTCt_-b9rrRlxuhHkFN_j_8a4YZP4gtPG9uplVnPVxhIolIw4zREI7oL9S8DPSPYsSZ22jJvLpvA5Pe1HFyC8CtOOqMIVLoJgY_Hk8XWhpVa9r2z8wqSF5Ue2Ppq5zqxF3M11ZBxPEWLF82s1n4vUqgPv5y890-ynDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین گل‌به‌خودی فصل را علیرضا آرتا وارد دروازۀ چادرملو کرد
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/456102" target="_blank">📅 22:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456098">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDyTVe7g62v2qBQY58itp9DXqTNwd17OjwkQ5EkmDBjI5pr_dN2j3LeTPr4eBmwz25wt5wD6y9lj0GLpxXKJMQo2hCsyRCzsjnvspKcofby9qph324ZqaIKTjUbU3KyoxExmoWClnEyidZ5qZgPmjm1F2093E29ygn0JcDLQuyT-NiMauZn1CLMwYU_2HkX-VaiYhp3GdmOyC5RuUvoN3CNfR9XNYaOaocyd6TopgA1wTKqA37hcpI69bunBUjQOQFAt2WLBqF6qrehZWBLrlA-drNn6yMk14xcUyGWl5S-bRBdymSs3bh2PHXVCraKqCqZOouH3lOruVz5hfkcVTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fsc1peZ_5VxnMtkyBFLAcol8XlHRL09wyuOguxfilRwEGCoowGcYeihTmSl6-HcD99DFzcK7Sl3bpjptD19tK_ZObY6DT0xu-ZEGwNKEGrs0Jb5N2pQogKaNWe5tjkR45vPAkJ-iu0bJwuoXQU1el7M_f4zZJxCsU2r2exAYWP7PFkkhrIwQkEUklucWdKrOmeKwr49GUIc9JfFqeQ7gvFUWOzjFT4jGjoFUS6LIV38Cm2s7sbxWML_5rqSKEeAzSOuBWXOCGiVrwOXZAdLMS9n1azXNWENANb5vGfWfYRxQqIFgbLbYZ4J0ggMHsmgyRBuXSlfH0GlqfMs2giDK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mg-U9_OsDVToRowXw88iXisN1jo6Ogsbd1i2rUpDhq9IK3lZiaveTqK-fybxhDQU365IhBQzP9lKj4-j1axX7WuExRRFJWOu_ACcmXYbr2XVn1R7cpqKiaLBo2pO7sxntdz21XLIzJaAi_iT2wY_KXDx7ly_bvDqGVcf_xHg7yzPezJLjFVrINpE9-Uii35PdQmIY6pp_SjjKukoLMRphpZo5yA1mm__Qig_GVGzKRmUstYSa5SwH6SA4qFKX0Xx9E1eEpO-Ubr4LnnalSSZMSxuD6HT_GlIm7feHKBxB_z5-PHrhz67ScZXu77SkkZa7A-wPpv0Ba0CkA7iflhdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4imfBvKOuvox411t7br_TL52SCqwV7-c15G1dFyrmFzLNLjeekTooRumoz1-kTZLdObcw7tVjEdeBFAX01xrcrV4wPPnx7wvJo79eMWr_aJe5A9wobUueNwZKhH-juh-9vNGIMWXHXz2YF98oFyNHjS8ila_X3h418ALlZ3JX-gJPKxlvSPUQ2RMl50pkTtKPeKyImh_sAUlHt9jitk_kArozqmyfYfAM215rd6PoOdhD9a8MP0QiWDrqTUn7cCVH0mwadJTQy-Y6mRmYKQsR_vBZwTW8oreRwBMEWgrzqEt0MbbW-HEUrp-L2bmmv-UTSl0GXcSpkTIkSnBV3V4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
گل چهارم استقلال توسط قلی‌زاده دقیقه ۹۲
⚽️
استقلال ۴ - ۰ مس شهربابک @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/456098" target="_blank">📅 21:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456097">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dbef8bbd3.mp4?token=mr0amcthnBb9yy3eab1qY92Rq1RNHgS6L_1f3eDKmZfHzjUZPZZ90mrD-GSSJttlb3TAgp99wIGs4xBM23cK2Qh1du4Di_ljNZk9wCsnmVCID0BJpjZbkZthVGBbwx7Ag5WuKSL0eosaeGR780ESC8iZhrAYDzAJOjO5XvaZvsvvpyI3Qh-pDoLIAlPnqFErVPezhjgCAXvVvmXnjJEHkWXGSP_DPY68DgL8MSXhkEtZ_qQy2hsHQoG6TRRibTIfWd_bOvK6ZpJ-tbeiEB3gH1kmlAX2ztKtvRU_OwBGgcKgJ7FR4h48hAGvr_J36TOPfN2b2I0qkz-SzLk8vk-UGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dbef8bbd3.mp4?token=mr0amcthnBb9yy3eab1qY92Rq1RNHgS6L_1f3eDKmZfHzjUZPZZ90mrD-GSSJttlb3TAgp99wIGs4xBM23cK2Qh1du4Di_ljNZk9wCsnmVCID0BJpjZbkZthVGBbwx7Ag5WuKSL0eosaeGR780ESC8iZhrAYDzAJOjO5XvaZvsvvpyI3Qh-pDoLIAlPnqFErVPezhjgCAXvVvmXnjJEHkWXGSP_DPY68DgL8MSXhkEtZ_qQy2hsHQoG6TRRibTIfWd_bOvK6ZpJ-tbeiEB3gH1kmlAX2ztKtvRU_OwBGgcKgJ7FR4h48hAGvr_J36TOPfN2b2I0qkz-SzLk8vk-UGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم استقلال توسط اسلامی در دقیقۀ ۸۸
⚽️
استقلال ۳ - ۰ مس شهر بابک @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/456097" target="_blank">📅 21:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456096">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6b1ea3c2.mp4?token=h2aUAicJzkN1xf9qNcjRMy-XAJ93iFb5BMVckQhjmlQoeQQvvZAYdhql_rYxCrBpUhYDk9Dpovz6qHwfXlA7gZ9XXC7voeB0y1fkT43i7zTgSaV_rxUuoiXL-pUJLKvRUr-CQ_syifiJshIfCUpfFgagtN-gqFilcxx2T8LneOKG_FPTys7pBLOdWRiAv5xzb5IFHpMcqyZE4_loLOz9uQ7SMeF46II1P-EsoQ3MyiUlXD07g37CI5dOa0wDJ_nlWmB6FBglwP4QBgBNXL9ptu7XxFSgn-Cr_hAt011epKBCtxwCuAjpWKFOR-ubWzCn5yqXvxrQZgcnqOEBAsQA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6b1ea3c2.mp4?token=h2aUAicJzkN1xf9qNcjRMy-XAJ93iFb5BMVckQhjmlQoeQQvvZAYdhql_rYxCrBpUhYDk9Dpovz6qHwfXlA7gZ9XXC7voeB0y1fkT43i7zTgSaV_rxUuoiXL-pUJLKvRUr-CQ_syifiJshIfCUpfFgagtN-gqFilcxx2T8LneOKG_FPTys7pBLOdWRiAv5xzb5IFHpMcqyZE4_loLOz9uQ7SMeF46II1P-EsoQ3MyiUlXD07g37CI5dOa0wDJ_nlWmB6FBglwP4QBgBNXL9ptu7XxFSgn-Cr_hAt011epKBCtxwCuAjpWKFOR-ubWzCn5yqXvxrQZgcnqOEBAsQA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سحرخیزان در دقیقۀ ۵۵ دبل کرد
⚽️
استقلال ۲ - ۰ مس شهربابک @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/456096" target="_blank">📅 21:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456090">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CHNyBYelj0cL_MDIe-DXgZXiE-14H5rVDg1Le-13gYuw6iyjxfW8oqVo4etj9VdKg1cCZ6KqmQb-_u1b4WOkrYDR_EQhy8N5ZTlaZesfJmd4qM2ZmB3WhcgTc6pEAN58hcXmm5wIMc-e6d9JBUqnCVzKkKfm0nKRme5EZI_lbS8lFid3AGnkFOLOIpXHkN-l9sRkz1JtIH8lHmlzEY5LNYfc5OtNP_1K1ldJ19EH1Hfzasn3zMU4kZYBU-wGfF1OtJTgbS5RQhWmrsZI_jhERVtdXfbMcC0XQ43v9gC4pjBO_KHojWTvrjz8P0qCSk9VnFzP2C_N9VauHESXv5OANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vu6jKLDsHs0o-HRHjvO0Kitn8t1WMYsRFCtUIpv9M-Rk18mhrQAoykV2mpQmplyjqtmf7A_T2Unb7a-1lH7KTV8IJ_NtPoKlHpWNYVBF3fO8gDJ-445UgZFWDGB8d07khZtmlfdFkcNC0Lj0ek7JFt_MHW2dPQ8lGnvt6oQ7V1hN4iu7h1bddmYN6pdtZxWa1cWUS5rGPtjofmaLaB8XY0CmLQuUWbJUxnT6PLC4G1awe9JWyDJ9v59hxq5_Vgtd78mhGX0OHpusjFfO4-nK6bMC8-v9SEltPKx2T10Qo1G0HgjWzkehOVGe-lLAhZuELumWwmfinWV6Ena0I4cJMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brCOf3LAuet8fxZHaPBWP3wkntsPXd_Hd2wlupcy6hsoIqOAzMgEnKZV0wGw-PmHoYKkNeR-C20h0XxzZGGQDO1DOhml7Srucj9WNj43jPWZwOyXUAXVQyH2LOTzWLtzYuYOEyDmYikgQM7-EfrrYpa5rGlA4UopU5Cbz1K4WMLVTH7kdFVrUJzgVcYPXZMpImcSaoUD6WWn40Wpi3Y1wQZKmsF1atSikREBwhr4TtpPY84HOnJe3RebYV1BaaHl3k2KftgS0nZ1UwVhXSZA0mv56zO8NzygJk-lP8_kpumiZS9f5mNIf7topQoiNf_prnZA1gwU9Fu3AlHgqST1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_UmH4V_FFan7YB6nDkqq-jIHaLn7MMRQLdsp6T2EPgg95LqHsQzGsXUAtnp3EO6RbPa0GIP4b-jJeMYf-bbesg4RNjdinPowM7G8BGm-qlCvL6fuJDJ7RCgSkExeDR6IYxIyUBqibm4KMPUlvSTP9mvs3LE2aBU4FAtCp4AvcRj248CZwEzNHu0ERLJ5iSED3BUstge9OP3c0a9f63uMi0SkUfULSgqqlnc8j99bJMKZW5RBEg90eudSbGQyYxILfiAiKZy55gaLi9q5l3v35-h_puZP4gkKUHLhQriI8U8Z4p5ym4PlyKmdDfkTkS2SniFNvY9ul2iGa2HDv1x-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JaHMZrMyG39T7dAkjBiIN0PCMXqg6NZj7jovS62_8rpgi_GzwXZSYefLgBIXn2L1tydwmpRCBlDH7jKql7ufEfJOb3_yxb_9LznyOocOp0m95sNCNy6vMrUakh0_-fyfvgdN5EgPqyVsiUDxC65vscFmG9WchtpoYK0pQdDzuvkGdkdEKgz_ytBEYZfOvAXOt585xR0gdOYQu2fn17WjdNyquMMQA16WzzMlTv0QK9Awsivi13Z2UNpYDWAmCWHp5HEvZpegQUU4yl4QrASuopG3Ybuj2HAc3WrFtZ-XF5lmz0ZUqlKohku9tV7YpqoPI-NqagHdWYWkUTyNvoZsSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxoQMh00fk3lC1GIJcckt2VQqnnOr4j3m8Pqm3FYKFYqf6xK9NCLJMvIc02CrhYyFu73X7r5i_Lz7is9-77OJquls45E-kOCBLLXnaslIgbvWiys4HUniA-Bqa4dMU9bPE_77RlG1mudyxNCFq9B9JPx9ZwxNou_WVNLHChqaj5PTAETugct_xNpzfAPksblYwpCqtzSpvDYsugHrfvYHHNCsjxCmZPDN8DzJHSsEWcgWO5wctACMCMQVSytv20YA9CqEZETLQwqtF0lNAULC432_5vSIIhGZxyci_C1NyIzlP1xriYm4hya2KR6Fro1pDkquHE93x3HdnULM8R5iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غروب خلیج فارس در ساحل بوشهر
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/456090" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456089">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎥
حملۀ موشکی ارتش یمن به مواضع مزدوران ریاض
🔹
منابع یمنی از حملۀ موشکی ارتش و انصارالله یمن به بندر المخا در استان تعز(جنوب‌غرب یمن) خبر دادند.
🔹
العربیه هم از آتش‌سوزی گسترده و واردشدن خسارات و تلفات جانی در پی این حمله خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/456089" target="_blank">📅 21:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456088">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4424895b69.mp4?token=FH2M9bdt-Nmiv5JJAmgFTGbYhFuu-BRW153O24PukeJnFDl-Djxv39XVBvWpKH1XdplgRrdBZlVbId6xQEz7zBWxYSw6tBv4Es23NRutcW0MwC94f7GkhH2mgQd4XLJUyVf5zj9AWJyDcaFK9cDoCOHibhTyEcUv9VLlJy5F6ozB461cIZu4VPnQ_oRX342oGy4AWyRZ69mj7pgcjKvuWVOxexUd3BXZr8Fzx4xuexP3cM64i9mdYzNCWP_PjpFTDVRdVtNX8lWuWUM8pzySNCak6v5pGvEmmE9k-P4zRY6t1dgjnQSn4QfDDrmkctQwtsuTTALNRssyvPKxoBzBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4424895b69.mp4?token=FH2M9bdt-Nmiv5JJAmgFTGbYhFuu-BRW153O24PukeJnFDl-Djxv39XVBvWpKH1XdplgRrdBZlVbId6xQEz7zBWxYSw6tBv4Es23NRutcW0MwC94f7GkhH2mgQd4XLJUyVf5zj9AWJyDcaFK9cDoCOHibhTyEcUv9VLlJy5F6ozB461cIZu4VPnQ_oRX342oGy4AWyRZ69mj7pgcjKvuWVOxexUd3BXZr8Fzx4xuexP3cM64i9mdYzNCWP_PjpFTDVRdVtNX8lWuWUM8pzySNCak6v5pGvEmmE9k-P4zRY6t1dgjnQSn4QfDDrmkctQwtsuTTALNRssyvPKxoBzBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال توسط سحرخیزان در دقیقۀ ۴۵
⚽️
استقلال ۱ - ۰ مس شهربابک @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/456088" target="_blank">📅 20:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456087">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458d36980c.mp4?token=LqfiQ5jEVXIh6tQXqlmfM0_1tpa66prDe7XIRpIP9gGlZ51MJi5kQ25BoJ6FNy3efFq06zTGWdpD9SLMZ7sBiXC0T7WU465faaTSWNxD5D74E5CzAsstMzV63DLBxOjZEG04poeGwRxQOSEIbCOB4nbDrelKQH2cC4_vr1tV_91X_fuZP-K5ela7Xb9cr5PdJnyeKubZSXgpSSmIambjJ-dbFzdV5Z4vK20xjS3GRe4CtMURBKVb7Dd3xr8ucdXPtYSCBGEwHZlUipR2CfHRFR00-ZRXNkzJpWAw9Vj8d_YTeJHNXAsRqSUyD0jWPFmGcvVfssi1GmApNszlxzvR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458d36980c.mp4?token=LqfiQ5jEVXIh6tQXqlmfM0_1tpa66prDe7XIRpIP9gGlZ51MJi5kQ25BoJ6FNy3efFq06zTGWdpD9SLMZ7sBiXC0T7WU465faaTSWNxD5D74E5CzAsstMzV63DLBxOjZEG04poeGwRxQOSEIbCOB4nbDrelKQH2cC4_vr1tV_91X_fuZP-K5ela7Xb9cr5PdJnyeKubZSXgpSSmIambjJ-dbFzdV5Z4vK20xjS3GRe4CtMURBKVb7Dd3xr8ucdXPtYSCBGEwHZlUipR2CfHRFR00-ZRXNkzJpWAw9Vj8d_YTeJHNXAsRqSUyD0jWPFmGcvVfssi1GmApNszlxzvR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجرای قانون جدید فیفا در لیگ ایران
🔹
به‌دلیل تعلل دروازه‌بان فجر در بازی با خیبر، ضربۀ دروازه تبدیل به کرنر شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/456087" target="_blank">📅 20:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456086">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb2f4e282.mp4?token=rDJiMwKcJOVmBIcn1awOm3opaobPTuhIHLDXwDMMeW1TL3gFulwNZz14Q_Cxyf5VVCTL1CqNVD3u0r9yz-Kp_gH4Z61yAuj75tFDJuOoSC9VvbXODUtwdJrWy9bz4zedz1AsLfj_x0aL22rxJPOUmZHWjLTBp-s1dpUxIE1iO2LyDxZMiMZ6LPaT2Iv-QYoUn5HgKmQqv_F5dqfDeSDdLnUw0Kl5k5VQfODmBH7_q6TW8Tm2W-zthExC4ZE2d3FvejJr3tpwKkiMwXII1mS6JnlFmh2BfkicYCfu2Mbyhh5TJbWL4OLVLdfZK5rjSmT2x15wK-lOkKipdzp4o0NOYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb2f4e282.mp4?token=rDJiMwKcJOVmBIcn1awOm3opaobPTuhIHLDXwDMMeW1TL3gFulwNZz14Q_Cxyf5VVCTL1CqNVD3u0r9yz-Kp_gH4Z61yAuj75tFDJuOoSC9VvbXODUtwdJrWy9bz4zedz1AsLfj_x0aL22rxJPOUmZHWjLTBp-s1dpUxIE1iO2LyDxZMiMZ6LPaT2Iv-QYoUn5HgKmQqv_F5dqfDeSDdLnUw0Kl5k5VQfODmBH7_q6TW8Tm2W-zthExC4ZE2d3FvejJr3tpwKkiMwXII1mS6JnlFmh2BfkicYCfu2Mbyhh5TJbWL4OLVLdfZK5rjSmT2x15wK-lOkKipdzp4o0NOYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال توسط سحرخیزان در دقیقۀ ۴۵
⚽️
استقلال ۱ - ۰ مس شهربابک
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/456086" target="_blank">📅 20:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456085">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74556fa3e.mp4?token=CidcV7JoLTnxPEy94zlyN3QTSkG2PQclTDXKSeysv1GDrC72Mi3gZRmdcIR5soD_g0B4h4lYc7YwW6kA8u6l_oxUMZ7aAJR1f-uL7zjjb6z4YOWXfPTKhzCAgDL_F5b3Buv0Ld4_bjAh9FcIQVUgaZu2J5gnjMdhsH20SAG4KRbvhpA3O2WagVpTIaHkYKlkhtyPVlOQLFO0gaFDY5c171Ux2W-7NuZTfB6fGNkN3Y8TBGoBjDWhtzKol5_jyR6vKbVyWObdG6uMunS-p7Hiyg-D3IFtub7uCxoDSb5-EjuoX6awHXSW8OqHmzCJCjLQoFiB6yE8abNrCffH4j1M9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74556fa3e.mp4?token=CidcV7JoLTnxPEy94zlyN3QTSkG2PQclTDXKSeysv1GDrC72Mi3gZRmdcIR5soD_g0B4h4lYc7YwW6kA8u6l_oxUMZ7aAJR1f-uL7zjjb6z4YOWXfPTKhzCAgDL_F5b3Buv0Ld4_bjAh9FcIQVUgaZu2J5gnjMdhsH20SAG4KRbvhpA3O2WagVpTIaHkYKlkhtyPVlOQLFO0gaFDY5c171Ux2W-7NuZTfB6fGNkN3Y8TBGoBjDWhtzKol5_jyR6vKbVyWObdG6uMunS-p7Hiyg-D3IFtub7uCxoDSb5-EjuoX6awHXSW8OqHmzCJCjLQoFiB6yE8abNrCffH4j1M9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ موشکی ارتش یمن به مواضع مزدوران ریاض
🔹
منابع یمنی از حملۀ موشکی ارتش و انصارالله یمن به بندر المخا در استان تعز(جنوب‌غرب یمن) خبر دادند.
🔹
العربیه هم از آتش‌سوزی گسترده و واردشدن خسارات و تلفات جانی در پی این حمله خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/456085" target="_blank">📅 20:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456084">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حادثه در کارخانۀ سیمان در تبریز جان ۲ کارگر را گرفت
🔹
استانداری آذربایجان‌شرقی: بر اثر نشت و ریزش مواد اولیۀ سیمان در کارخانۀ سیمان صوفیان ۲ کارگر حدود ۴۰ و ۲۳ ساله زیر مواد گرفتار شدند و جان خود را از دست دادند.
🔹
بررسی‌های اولیه نشان می‌دهد بازشدن اشتباه دریچۀ مواد اولیه موجب ریزش مواد داغ و وقوع این حادثه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/456084" target="_blank">📅 19:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456083">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شیخ نعیم قاسم: پروژۀ «خاورمیانۀ جدید» در جنگ ۳۳ روزه شکست خورد
🔹
دبیرکل حزب‌الله در سخنرانی سالگرد جنگ ۳۳ روزه گفت: تسلیم مقاومت صرفا یک توهم است. مقاومت همچنان به مسیر خود ادامه می‌دهد و اجازه نخواهد داد اهداف رژیم صهیونیستی محقق شود.
🔹
یکی از نتایج جنگ ۳۳…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/456083" target="_blank">📅 19:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456082">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnpCkgnpEkjZiZ31-m6qZn7Gb95be4lpjYJ-lkMIjLryKJG-Yr9FHDZskBfXGav2RLcM8FeycGwBfeFiCBEQLX9lz5UTdlaoMDzgIRmwKYyt9vJYSWzPli9U4kY8zuQlYRRd4lQ0wbph4Eg4vLFnTayrK4FVc3XW2RLPDY3B77qSWzSI6I2s4UrpzcAXs8OQd_agxig6OJ-eFS14zLIDYoQl_VCc-WP8EN-YGeAro1eBTxCSokCLoZSE6U2P0G-zAaVwWM9GkxaedDz2xdYStv20Gq5kW9L8N1xvmu8VINrFdaD3nBytBhnQ8LnvzPl-NqmlkMu1-HfsCcFlv3HeIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیخ نعیم قاسم: پروژۀ «خاورمیانۀ جدید» در جنگ ۳۳ روزه شکست خورد
🔹
دبیرکل حزب‌الله در سخنرانی سالگرد جنگ ۳۳ روزه گفت: تسلیم مقاومت صرفا یک توهم است. مقاومت همچنان به مسیر خود ادامه می‌دهد و اجازه نخواهد داد اهداف رژیم صهیونیستی محقق شود.
🔹
یکی از نتایج جنگ ۳۳ روزه این بود که بازدارندگی در برابر دشمن از سال ۲۰۰۶ تا ۲۰۲۳ حفظ شد. دشمن در برابر این مقاومت، این ملت و لبنان مقاوم تسلیم شد.
🔹
آنچه در پیروزی سال ۲۰۰۶ رخ داد، نشان داد که مقاومت می‌تواند معادلات را تغییر دهد و به تسلیم واداشتن مقاومت سرابی بیش نیست.
🔹
حاکمیت لبنان با مقاومت همکاری نکرد. متأسفانه مسئولان محاسبات دیگری داشتند و تعهدات دیگری بر عهده گرفته بودند و تحت قیمومیتی قرار داشتند که نتایج آن بعدها آشکار شد.
🔹
شیخ نعیم قاسم همچنین خطاب به دولت لبنان گفت: چگونه می‌پذیرید که به ارتش اهانت شود درحالی‌که باید از آن حمایت و حفاظت کنید؟!
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/456082" target="_blank">📅 19:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456081">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehwWrv5mBA-Eyo8o_4j0pePirc6JKiQusQgngTFJcuOUQPm1OznwBZd9H6TdoXv949o2lUx1ZDMqwKecHlL-ziFDEOHjLCDSNvs6WJMa_KZPzkgd7QaZOegMlY3W8no_0uTy_gaziejKhaIy3jTkC8rUAJ6q3X32NS62oNQA1m5RygJXJdyfxH4VdATntKuMiVa4K0dCU0tiYBXQlcvTdUwSodC4B9JdX48Agrq2dd9jXMMxXOcXE7CXr_h14zapPiwTE22KLUf_JXGE_WVjjGcGKf2fc09C5EC5OsEoev4o5Ty7GvJxPbJ-R23kQL5XNzkMgXR5wEXDAnZik4yBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفای مشاور امنیتی ارشد ترامپ در میانه بن‌بست در جنگ با ایران
🔹
همزمان با بن‌بست در تلاش‌های دونالد ترامپ برای بازگشایی تنگه هرمز یکی از مشاوران ارشد امنیتی او از سمتش کناره‌گیری کرده است.
🔹
پایگاه آکسیوس گزارش داده اندی بیکر که از مشاوران قدیمی جی دی ونس، معاون رئس‌جمهور آمریکا است طی هفته‌های آینده از دولت جدا خواهد شد.
🔹
بیکر در ۱۸ ماه گذشته نقش مهمی در شکل‌دهی و اجرای سیاست خارجی آمریکا به عهده داشته و یکی از اعضای تیم مذاکره‌کننده آمریکا در گفت‌وگوهای غیرمستقیم با ایران بوده است.
🔹
خروج او از دولت در شرایطی اعلام می‌شود که کارولین لویت، سخنگوی کاخ سفید نیز از سمتش استعفا کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/456081" target="_blank">📅 19:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456080">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4744c05f93.mp4?token=qUEMkLV0-qwfNkkloBsjg4RHLaMAWQEJh48EmVY5YU_q6gcTmuTXXb_-qbfy9i-yHF2Ny7slZ98fboPJ-xIsZQ2VZqNIX1pRbStbU6ZTgvV8kJRv0EaQTCJzZfSvqeRwJGgkPOPRcHT7PalfWwrUeBaNIE0NfIkn1WNF0Ld8wSq7m8sIFayUJ2ao6qNHR03dP4RJviHQ1gyKBoabBobAn4-OuwwgUF-JL--3x9Yh_GuZ3rEVM0UjCJ46G1fBWNIGfznnYQE9XxD355tWyb5d_NYV5Cut9Vk0le91oRXeCAZ_lACEWiuQA4x-nptWV_FYRx3fPnwo-VC5OjjXjgkLRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4744c05f93.mp4?token=qUEMkLV0-qwfNkkloBsjg4RHLaMAWQEJh48EmVY5YU_q6gcTmuTXXb_-qbfy9i-yHF2Ny7slZ98fboPJ-xIsZQ2VZqNIX1pRbStbU6ZTgvV8kJRv0EaQTCJzZfSvqeRwJGgkPOPRcHT7PalfWwrUeBaNIE0NfIkn1WNF0Ld8wSq7m8sIFayUJ2ao6qNHR03dP4RJviHQ1gyKBoabBobAn4-OuwwgUF-JL--3x9Yh_GuZ3rEVM0UjCJ46G1fBWNIGfznnYQE9XxD355tWyb5d_NYV5Cut9Vk0le91oRXeCAZ_lACEWiuQA4x-nptWV_FYRx3fPnwo-VC5OjjXjgkLRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مغانلو اولین گل‌زن فصل جدید لیگ برتر شد
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/456080" target="_blank">📅 18:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456078">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0vFyZ4Fi5joh1wVENc6iazt7tN0vFkUrQz4hJqjPFp9t1pQrh3fVCLikzkbbbBLHSMrogNN2GwaHUU9v-Kror5oPYwzyumcolg2ndiNgAhKe6S7r9Alfq_oj1rGHEvt5sDcb0n0Msjm1Q3krvwcy0Kkj_E5FcwjdpMf516mpe3poAHzSZ58Km7kbvyQAjaQ2kc8kPAuMWeg73VUvXDOQNtOGZ8TJeSqpciVCSMOD-fT5oEZBQL3mLW4dP4EVALtK3gyPzIxeXjwU5OFnEnQ4ykW0dM12TAXfiwlwXnS7CknXP4CiWEP5nzkfmVy1WhUVDpBZ8IpzfUZ_ZhnqznWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-rRvhyVnkFybehH73LqJZkeeHtlT_hb8EzkfMMMjXpYzkA4hmIUcYd6DufMxZHAVEkbmocmn9JzghXT8_qVg0ZATDVNEycPKkvuAGzJxu0ZOBDFqgQzS091NsEmo3ZdWsZDUwE1xRAUK3OFDsjdljV0jqzrOTWeNYFaOFUsP6sX2NxsQVKUuG7E6Ht0V4Dkx76-1OHlDVeFk1CqJpeo2DSeNgOqnNvfCYf4FevD-HvAr82QZM8xEXxBQ0gNGn7zNGjswLI1L-55cL8gWBUQ47u7CPMe8nmi5rPMW5egoeNAi1_pmT4gybmxSgOkRg27GDr2FRzzUigj2i4ucPJ3kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جدیدترین تصاویر بارگیری نفت در خارگ
🔹
شرکت رهیابی محموله‌های نفتی «تنکرتِرکِرز» گزارش کرد: داده‌های ماهواره‌ای نشان می‌دهد یک نفتکش غول‌پیکر «شرکت ملی نفتکش ایران» امروز در حال بارگیری ۲ میلیون بشکه نفت در اسکلۀ آذرپاد جزیرۀ خارک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/456078" target="_blank">📅 18:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456074">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqE6ZncD7rOZp9h4pXah-5KHtMgPWRs33Hid_TnImbRsJ7z7fxEiodEe3EY0Tsc9xAc2SQ_kylqUIeOpWMx8_fY2oO7-195Qekw7UlogvnU9nJ8UTH9iFsE8NsmjWgNA89NQKFpD0xhLw8ZABULQCJNOKOXowIwiKVWUL_Mp6BHth4erotXvKyehRukuJQrrcf0Rxl225DKzyLBmeXAPuzP0lRlMBJggsyCj8DRnavoIoHzqwJEGOwdMJWC2OsXDye1imuPfqf1AZkoi5znsz6p73cI8Cu6PBcxadV5SCC9nH7EwAKulJgUm2wEN1zggnl-qQiKbvurynHW5f247bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AO04gDgNYN53lvmpj8QslGHGrcUjWeWQ4D-Z7vZOznwX1_KEgi80GYYuwng4OmWy2K1jMTavkNa9kWwDokbNrpJrdUEbD8awnnCMBXsmm9MNo8a1UTSf9Z4Li4Dnc_vlArSKZvGlE2gEwACBY67MhSF8AFNkySXq025VrTeNtIYi4SeWk_upCKv453AIHsKGwTtFA_2bQFsgCAb3j5nklof4uJEvI2w4E3sExODaBIruuoH5PR1VR7ziCgjsiizuVxwOM-2Oz8g8lCVWQzeu82bUsYlscFTZ-EipMr8OKe05sbacn2Ffa_nMSsozSA5cyxESo-bMBI0rm4re4gGn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmCWt3uMCrIR19F6eAALce22IDnqgpiJDjIACR4H1bGXfB6ACBfkfuT0TBF5TyRwTKgZAIfh9srd9Io5ZVgqqaDL_cAtmp1P6xC_K0Et5dxzV9z7AXeyWs2ebbaelMHfVGssWwOTW2EHeetSwkpCu3Kw3OLwm1CNx_y__InFzrQRr9vHCqDaEqhKpNOvRrOEbPhTuPXKP7pJhKsYalBUNWI2WRHYYDQ_WR5Y4dGR0N6bG36JfetVM6b176yUptaLLIrl1Lr7xTl1Dwqp7wG7VqHCbQeFlH9Q9_H2elNjR37CGOrRiFmxzSU3W1TBN2fXozuY9N0COUYaVrO-LbIqPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdu39GsTS12lQiFf03M3W-lrSy1G8ZLr2UEGHV7G9tf41BqcetIxjBhvVCaGV4rVaO44AGI5mHMNB9a0RK-GhmMNpllS_tITjSgOItIRWXhWyvGJwjSAJ28OyxGBJTw0xqx-c9wi2F6pIqHjwiRPpKk_CkonQ18hCNnxevZ-aJlhjtDoBrcYoVQJPcjU0RlJkQyfCQuy-Fjx-AuuujiXgChuPCxmckHg1iSL-I4poE8KK3L8-ohte5s3gxSxADbTv-yO5plcC6o2lCcr8ygOotdi_qKbKeks59wnRhqJFE-GckegUu_w8mYk9OSze1G1G9bIDePHbjbckKOsk-0LiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزرعۀ گل آفتابگردان خراسان‌شمالی
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/456074" target="_blank">📅 17:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456071">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrFG_WgkHh8FnpjzuNFxantsfIHKoRTVpjSNkJO8ZROBeBFnalddzxQFX1BLu7lcLdtPGhHAYFJ7NF3ylTt4PYFzk_cU05xUv7WpUN8qaXL0nPa7Kk-CZ9AJGLU_Ci9ETtWnwgGtIgL-ZhL-TtsD_174uPkqN1QEAirONBA37gITCQYdm9ZfC0r_b6MepYiROFCgCm8OFhMUhGxWl7YQUTJYWVjJjVfyo8JZiT76ItaYTLxBUvSPXfhj_tqN84FWeW4Hv31ggwOAhaG8omXpoKEBLWkQt93YxuunbthLYDq277VE3C4k_V1WzLUWo1_7E4tj2eIm_zqBTqhqrOzMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez1PLyLT_K4UbQogJu9kaJbKTXUNMKPbo41rEnfPRIpHZQD9uAlj5uxhIE_d67JvtdplUPIJdHW3KiictnKbqBPa8BsHZrNimp9WRQlhAxQXsgOQR8l53oqYUke57eKdaslw_3cFpuGHLJzkorgA0qqsWgAfSdgoAxIDejHQ9X4oQCtdzLxeIxWUv7ODzS86FXkSG-UwJ7yr6xo1WePxw--_yh3B9dn2a0SsVH-ya92N3gtKGxELwSHFdG873LJ5WctUCCOiBZefb4djsDTl3nPAIipvHAxBhNdO-EwwFfKcZsEtz6rkcR_5tDatu9fOV-eRojRUHi8egBOTiOqcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7HU1fGmEUV2pRsN76s7RdA0gy0FRYm7TuyaA4A1iz7vYbuHtBHqP_CQlWs2RJTkUdFRPDdiw_zwcmI_KLIFf3BdmVG-XAc0D7VinDOgfi_17MOUku8q0AagPkKgd-V5RB0X7RXB6-beukC1kil2T0oZJq-u_Mq9XZvah0S8VTt0px0vQCiKUbuBOmfX97zD5JsYC17-_xa_vfi0jELISSqCChM58OseEYD4-if2zR01iVEC3jVzYeVmoAkIIEfbOgDXApFX_btYqMmXYW3hZG0VIHd_vb7N0s66wgjqetDnbHGFQQ1zQnXFSoWQ4rrUtLpp2nE1TDzL9n4PaAlkZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرچم‌ ایران در دست هواداران تراکتور روی سکوهای ورزشگاه یادگار امام
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/456071" target="_blank">📅 17:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456070">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f724812d24.mp4?token=YWYEzeCgBOsQeUPM6JMia2fvUl-xRxb8e895yv3a-QSwW-cLInyo8sNkrCNbqzBuB59eHyqATmT9GYP48HGYJGn3jtfnKmQL_YUuVgmeuYWIfgFMCglXKAmzfuRH08NzVCqFYGQxQIEE-XqeqpVIAd3QIQH9k6svJx70G72ELr4Dps7cirwImh0cdpUHCIhITi1comzMk1B3dNFupvrKDu4aKMwZ8ns_Hql3LgirY5CAsCGX5Y71EuXSVc7g6vGtCPj18-E1NT_ZFvl7lAARxgTBF9XIB-F7BCTwDdpA_ihzzMgjqfd40dWBOEtxFCiJyhyDvGQ9hDSE1yz_vfYOdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f724812d24.mp4?token=YWYEzeCgBOsQeUPM6JMia2fvUl-xRxb8e895yv3a-QSwW-cLInyo8sNkrCNbqzBuB59eHyqATmT9GYP48HGYJGn3jtfnKmQL_YUuVgmeuYWIfgFMCglXKAmzfuRH08NzVCqFYGQxQIEE-XqeqpVIAd3QIQH9k6svJx70G72ELr4Dps7cirwImh0cdpUHCIhITi1comzMk1B3dNFupvrKDu4aKMwZ8ns_Hql3LgirY5CAsCGX5Y71EuXSVc7g6vGtCPj18-E1NT_ZFvl7lAARxgTBF9XIB-F7BCTwDdpA_ihzzMgjqfd40dWBOEtxFCiJyhyDvGQ9hDSE1yz_vfYOdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️
🎥
تحقیر تاریخی آمریکا به‌روایت نظامی آمریکایی
🔹
ریتر، افسر و بازرس سابق تسلیحات سازمان ملل: یکی از دلایلی که ایران ما را جدی نمی‌گیرد این است که ما هیچ‌چیز جدی‌ای برای ارائه در میز مذاکره نداریم.
🔹
از نظر نظامی، ما شکست خورده‌ایم. ما توان ادامه‌دادن این درگیری را نداریم.
🔹
از نظر اقتصادی، تهدیدهای ما دربارهٔ اعمال تحریم به سوژهٔ خندهٔ جهان تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/456070" target="_blank">📅 17:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456069">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZS_-Z9asVwQHsEq3nchtta3mOo5djUfitUPBn4DpC7mU3kUHAVQUwlyLUMv8dqzm_kAED7piVsomRlJn-BbSLRmxaKYK_Z-xwyfI_JJIlKbbgC6ncd6RJ7Q6hjssrYuC_X66CeYbECHZCloazeoKZkAj7HHr7syaxGO_f3rtZi-pLPxf1QDKnhrfP5B3wQeWWMxnwM-a5ThEiHCLju1LnAM-VWcoGltd0TaDCDRHiUOU4Gb2jNA73SOrPlLRHbWe_TXLuQTEX5-TaK8v3qDnYhS9TaZWqtBX7Movn_PcImQrxEkLQLW6vneHKekANZBnbh1Kh48KQhyg5sDFPHAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باد شدید و گردوخاک در راه ۲۳ استان
🔹
هواشناسی: از امروز تا دوشنبه، وزش باد شدید، خیزش گردوخاک، کاهش دید افقی و افت کیفیت هوا در ۲۳ استان پیش‌بینی شده و احتمال خسارت به سازه‌های موقت، شکستن شاخهٔ درختان و اختلال در ترددهای جاده‌ای وجود دارد.
🔗
اسامی این استان‌ها را در
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/456069" target="_blank">📅 16:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456068">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2V-Q5apXwaT_R29dAr76S2nXPw3ARkzKetjqdkw_3WOvlZcdHB-1YkARyttnY9UwPEZ1J_tUm1MusMpq3F15HO4Tc8I2OBLq489a43B3GJQ_qNJC-NJfihBfXNowNZAhCsMhJYVHkcPbZsYjCAswbxvlA3k_UcTqQkprh34a-qjqCs9lQghGuG0MznpSbp9Mat0B3W1x6xM9dCYbN-ZzUcCprT8gREfJDmnsLAlyxtppPDRqDXkjGlgBU2RFdf4gC-9N6h-QH3NZDOaBhAsRMHlpzc8FuPH4SYlgwuE3NoHYYC3azSeujfi9CaH2R-ceYpsN4oWMW-env7igtP5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناظمی اردکانی: بررسی لایحهٔ خزر به بعد از جنگ موکول شود
🔹
دبیرکل جبههٔ مردمی ایران قوی: اکنون زمان مناسبی برای بررسی لایحهٔ نیست و تصمیم‌گیری دربارهٔ آن باید به بعد از جنگ موکول شود.
🔹
سهم ایران در تقسیم‌بندی مطرح‌شده حدود ۱۳ درصد است، درحالی‌که پیش‌از این…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/456068" target="_blank">📅 16:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456067">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ebef483f5.mp4?token=e0BjJu2zhRPhVLFLwOAn9FO6P5On589ruOTe4JfQM_c39deljuADAgbI-KrPqnYwiMVO2hdQpANlDukdB6XtUeHvUmSfvyR2kp9xuE-NzMvJgL6TpsHxX9ohq2JdUjRSCULNKeoT3gC_a0uNzscAKFlDD7gEum_C1wyZi7iLR7S8zrXjHGcULBUJ1yph1GNAWHiNk13HnRtbfYM_IuOHuWEmskBOQKkXkGcHI6wD8uHIXgZ9YALELQtfomZw5LNqq97UN94O4Q4dKyhifsx_7zi6paqdkLffVlN6xGlzCQt383kk8lqh8IPTjKS2fz-uEy_nroQG5OOreJhIH5xkaE9C_ZgqUuWAbR5fqYBOXNuylJb3PX6iHLXEv1oEiqu7ZgY0SplGQM2iH8Tw0FK1KuYeI5StrepwV9B4yFpWLPOY99_iVra129OcGlDnGy6Y1r1n0NULroVuEpb2ps7ytKBZv_LzXXQvV19iAJnQkE8VEtIo6Q0y94JubctGOC-OyliGlHPVJRGXS2Hz0OEDzybhESZ8jBTY15jHX3LseuBHDaxjax3-Yp2c4BpDA6nRsU4T1j8D6rYPodyO-tw9Ng2Yg79IA7M-0fy3C5A8vi3m-R9CG7U0ASbPEAdwW_-b5Hf8Z1hbA2iCJFHKOKPMLc_vZ_j3d2osNVjZ-tVciCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ebef483f5.mp4?token=e0BjJu2zhRPhVLFLwOAn9FO6P5On589ruOTe4JfQM_c39deljuADAgbI-KrPqnYwiMVO2hdQpANlDukdB6XtUeHvUmSfvyR2kp9xuE-NzMvJgL6TpsHxX9ohq2JdUjRSCULNKeoT3gC_a0uNzscAKFlDD7gEum_C1wyZi7iLR7S8zrXjHGcULBUJ1yph1GNAWHiNk13HnRtbfYM_IuOHuWEmskBOQKkXkGcHI6wD8uHIXgZ9YALELQtfomZw5LNqq97UN94O4Q4dKyhifsx_7zi6paqdkLffVlN6xGlzCQt383kk8lqh8IPTjKS2fz-uEy_nroQG5OOreJhIH5xkaE9C_ZgqUuWAbR5fqYBOXNuylJb3PX6iHLXEv1oEiqu7ZgY0SplGQM2iH8Tw0FK1KuYeI5StrepwV9B4yFpWLPOY99_iVra129OcGlDnGy6Y1r1n0NULroVuEpb2ps7ytKBZv_LzXXQvV19iAJnQkE8VEtIo6Q0y94JubctGOC-OyliGlHPVJRGXS2Hz0OEDzybhESZ8jBTY15jHX3LseuBHDaxjax3-Yp2c4BpDA6nRsU4T1j8D6rYPodyO-tw9Ng2Yg79IA7M-0fy3C5A8vi3m-R9CG7U0ASbPEAdwW_-b5Hf8Z1hbA2iCJFHKOKPMLc_vZ_j3d2osNVjZ-tVciCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
سفر رئیس سازمان بسیج مستضعفان به قم  عکس: حسین شاه‌بداغی @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456067" target="_blank">📅 16:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456066">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ii4lQA7e423T-MQBc-U1l6C87S7E0enJ7KI_ul2jsy5M7zpsLG1YT1vvdgOVifJWMMkcaJosFWi4uSrdrElFFD806Prhk8HMbn8FlqcoO2VakVEZqkpmDcbx5-B7R_6zyKoPjMICJfRWFfuxJF7L5q_fSHKVKc50EkCK6qsEc6fYhxucuiZ5IK38hZLYGYxKDL-E9DunfLtmz8tO57uLHukZZKZV9_cBCWl3NLeBdDLV2_f7NhK5YTYkolVdrrgqk-Cr9ipwyah6mPUW8Uh-JK_DMsrhsfyf_ImDSNhSbVxMANX-CsbO87DLSxCffEW5Bl1Jt4Ok04NNI1UKmWiu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف محمولهٔ ۳۰۰ کیلویی تریاک در اصفهان
🔹
فرمانده انتظامی اصفهان: در یک عملیات ۳۰۰ کیلوگرم تریاک در جادهٔ ورودی اردستان کشف شد؛ یک متهم در این رابطه دستگیر و خودروی حامل مواد مخدر توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/456066" target="_blank">📅 16:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456065">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2N93xDo8j-b3yOHJV1WgSrh0Ic19MTNWLgki-2ADyw475smNx8KrQn8qRDYug4fHwPD2ftWxO5CUaXszz56ytxMrTbp-hIGhc6sH8kPhtu5yJzSUZUckhsGtnCj2PQr6peC-GH91n7IiZ-dbxvgDHaeIr8YQ5SO7Gd-EZdIqbtWW2jD2VOdQ4S_EZgGwjDJabqGhLUZ5eielDiOYrYk27QRINCj-9uTVloDp0FQV4-OM2XltZOpLC5SuAzt1Qyg9t45z1uIy09mA4bY1a7Ja6rqfXhn2dUcccmmqfXe8q4ajJ5D0-LnIZiReNJIuIT0XGA4hzCmTzgdHPKWRQgYSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پکن: رزمایش تایوان صحنه‌سازی برای جنگ است
🔹
وزارت دفاع چین: رزمایش «هان کوانگ» تایوان نمایشی پرهزینه و بیهوده است که هراس جنگی ایجاد می‌کند.
🔹
مقامات حزب پیشروی دموکراتیک نیز بی‌محابا به هراس جنگی دامن زده‌اند و تلاش برای تبدیل شهرها به میدان نبرد و کشاندن مردم عادی به خط مقدم را شتاب بخشیده‌اند.
🔹
ارتش چین در حالت آماده‌باش کامل به سر می‌برد و به‌طور مستمر توانمندی‌های رزم واقعی خود را برای مقابله با تجزیه‌طلبی و مداخلهٔ خارجی تقویت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456065" target="_blank">📅 16:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456063">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4JHNKj-stdxexbqFh32FyUxgBCPGGmu2yju0nNSXzk4zMHRyHh6a0u1eZTa3DMh30TujR8J9rClDum3Q82hsIXkiZeBUzZGI_5oGWLHQnzY3a03a_qhpS_jiT2HQ986S2B2ynW7wyv2kZYx5dJBIpPvIYp1KNDRYX20C1WAkHciESGx14JR0bsPaAgJo-eVIYJKaXf04Hb1w43n1Q1BU_w5mwCg6XJzZycntWRurUBYr6IIuY7N5WYh9KLCpqrObvyvU9fWXfMIJk4W59KoB7QD5TTB2efoL_8wiWlL4KPmAJIzlqzSdpVn5rd3rD5Xa8iH7hAhketiL65is15DSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حملات هوایی اسرائیل به جنوب لبنان
🔹
شبکهٔ المنار گزارش داد که جنگنده‌های رژیم صهیونیستی از بامداد امروز تا به الان چندین‌بار شهرک المنصوری در جنوب لبنان را بمباران کرده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456063" target="_blank">📅 15:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456062">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFOddxujZ5jtAqYGaGnIHPj_NOkaZsCmq2H1LZ8KEW85IQDCFNQJXvUK3JilrTqtoYXE2aJUprZ4VHNuwirxfukuOMKFpuThrqEr3UmGqe9nIs9BZ44I5HKOZxgfYlY162sQLk0g_mi8vmdyUR0vCYHebVNknZq52Lx2SHr4x9mjb8i-dS_DKJABVD6ZQqlQFm9VE9_LfrwM3IaWi-RWw1W0W98wWUkb7_3dYPxmO_NgrI6j9NFEK6JojduNmhrLG69nOr6KioRfecJ5-N9ejdepkgy2cdjIBw464RcVC2hhF2DtI5q5GVhqRzMALdDtU6c2Jg-1YP5EXZiRmBTreA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصر، ترکیه و عربستان در رستوران تحولات منطقه را بررسی کردند
!
🔹
وزرای خارجهٔ مصر، ترکیه و عربستان سعودی در شهر ساحلی العلمین مصر دیدار و دربارهٔ آخرین تحولات منطقه از جمله تنش بین ایران-آمریکا، راه‌های کاهش تنش‌ها و تقویت همکاری‌های امنیتی و سیاسی گفت‌وگو کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456062" target="_blank">📅 15:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456061">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5-Q5NjjiLREGSatihJvbpJbqspI09RHVmjNIhOSq2LjuovWj_2OzTpV6ZMf6ryJvTMnzP6M-GRqOmAsTqnxzn7lmibW6hhJ1Fx3sELBVOI14NNBt1hsydDRoB1wcCS9Wagt88RRto_I-5PxyZoLn_wJmc61eAOcAcBji3iPmN0Z91FfMMGwsFU085_hz7WgIQizwdY_gk_P_Fv3BVgH0pxEHDNRrb_wmgJXXo1suicHvMKiWEnU8bvpslwAnHLwDhlINj_7DsgsefmlSWZoyf57yKhqIllJY4E_TWdTQtJuOYDeNOfrFjVdW0363TwIQFXbgXfN1jCMgTuCQHZEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج تازهٔ جهش هزینهٔ مسکن در آمریکا با بسته‌ماندن تنگهٔ هرمز
🔹
فایننشال تایمز امروز گزارش داد، تنش‌های نظامی و دیپلماتیک میان آمریکا و ایران در هفته‌های اخیر، موج جدیدی از افزایش هزینه‌های استقراض را در بازار مسکن آمریکا و چندین اقتصاد بزرگ اروپایی به‌همراه داشته است.
🔹
این افزایش ناشی از واکنش بانک‌های تجاری به افزایش هزینه‌های استقراض دولتی و تشدید نگرانی‌ها نسبت به بازگشت فشارهای تورمی است که ریشه در تنش‌های ژئوپلیتیکی، به‌ویژه تقابل نظامی و سیاسی میان واشنگتن و تهران دارد.
🔹
همچنین نرخ بهرهٔ وام‌های مسکن در آمریکا به‌عنوان بزرگترین اقتصاد جهان، بار دیگر به سطح ۶.۳۶ درصد برای وام‌های ۳۰ ساله با نرخ ثابت صعود کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456061" target="_blank">📅 15:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456051">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/roArX45KqZf9vFBYEaWHDRJQWXwZIl6CgeSVQHtA5ysIv7ierQq0RftinHxVnPHG1z6nMPjW9bVOZHIk2q0daUOmseYq91eYM2zhS8kxrrMMwVQEkVDajJBHa21LHBOUdEeiZKekA2WD1AbiDgpFVsGXhpeDhhuXUCTOkoL4vXINFfmPsY4RQdRiZW9k5pjO6bWDvgDWkl3RxNq-Zi9BHWu6bI15PNUe414PPkh5NQ596zJ_-rLmhJDt2WyYXdjFXCI9WmcAvQQWeXE6xyOOKqkd87Goh8Z2-QKEaw4yPD07mp_hF_vQw9A3k3uyLlGjWVZHzvdQUDYA2EpHGf3amw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqf9CcaOWc59-x_qLAxCueOo0ecw2cnOOm2NE4qRAbmL76Q4_SpxpuJrDgXBVT8dsguDpsWHwB_g_mIGtdfWPg-bk4d1Pbg7h7jfMkbP-2vqRjhT6-8eG6RkNRqBtqc2pWz19Tyc88kMV1SeGBiUTE_-0TkCg76F4T8niJS14tRyThASkYl3POOuHqFcWbUvn5TlNP43Wd1xljvBc5bg_Yj3NduXmlUBJ4eZn62-mbWdBKXiYCfdFZlQKGe4vfdfWtTLiF5tmAVYLtNpCE1_otv3fxylffRToX4D1sMT1ccj16-JkJc_zMJwaarSyO6I4Q_2Vh1X9cAPDDta3yuViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBvPJWiqhVSTeu6TR2x5gIqN-mdcSyIggd66HsNJj4E9y_7NVuaWsrDT7Gcm3AqB6j1CCjSEAyw21OTygpTi9LeG4ACy2dlg5l6scImz4CrAByd80DPvKtTiagFKYHnb8Mj4lrba2Xh1UDcEGUS1FVZno78YA2AZmwMZnRVLwoFYuoaa_cC8qKA_ZCzTExCwF-qT6kZdWKed1fpDtiCTMr2Zet1muqUW3ETg7n-EDxEtaassvnnM7cOZSzD54Bh9D_J2_91c5djkY5TbIQzmJlAsOAjpB-0vGLY5dJ9ieAW6bB5e4-1NyiAqWCF0O8_XF_ujregr76I_yk9zyF7yQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9IY4qygm4CvrCCOSTx-yErTf6_Y45paiCOL20S6cPiJp7U0h2KaS-_cDOrSvvoeLlYCGN0twxv5l552BH2O9mfMelg8Jjb7iHfyjW_3TX23wfdZ167f42WIr3PyClgpifzxvtTofldizT6ie3ybxeO1G0aBxzeA8LWYvWbSceyE6CuaoD1k_rMTvaLNN06XMb0XMbzWEF9G-Tl_taGOldeafw2kcNFxJ785ofHBt0VDveZmI8qfE-IYISmkT6KCAkj0yMNQ19m_OF0tp6QCUdBVIBisdIOzPv62R5niilI6RWNFelaT_TDlDoGP4pNmAiO9QsIDUuzfXtLYb0ur2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpOPCdPxDblSjFdzyNreImIyd12g2iW7BBIZPB3-nur8qm7vHpl5aD2hHYI9l_P0bjX_POytO7Im2YB99h-m6-Xc1l3QtzlNmEb_Sp856tUtMcSMYc3eOxv80aucNU1wLzul7Qy6ccm8bfpmU-zqvJpZn7rYuNPRxGvCaP40vIYfR3QYXg_0kCtO4OJYLxgzP5BBXthVkxkY9O61HdLNLvHayfoNNhH6Qj5AtgpA3JlZ-tEvqSJAPYWjHRdFnCAcipjlufv8ot0xpafL2guUPZf8O3bDI0rzFFJISe4pVBVP2x6iDsLOXuHuUOq603nh-w3sOR-HojMKz4_F3IJaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovAnmqJiINsGQhKDRR35ajWIPeBzmf3Mj2jWSTcjJjYK1gpCRXBlIMdGJvp2ZiA7KUXHNEyXlZdoaeKw2D-rCRNNux43-A_xivUVwQk2Rk9fzNsSy5ucr9QxHGRySqk4DV0plm5VQdyGYRKPIkHieyky6wODDWLJW9-q_hqn1FAyt6m2m29B9wLpl5CO5f-SReIaGkv2Em69bm8x_DCGLAj-Jz_znJ-NOBPhX7Fj7p6iAUrRDoSHS3_Yax6bngjIq2snZeFIlSCBCdtJY-RZ6HNb2couD1Ffa8mMXaUWeGCcUpTT40J95_dL-raN79rlkdpPkKjWxb8M5rAedyXJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KoSHOp1t6oP01aSsUt9NA_MKH-XRgKz0SUJjJhoK_aDRsao04Ji1azuR49MXkDY3A_rF3nRUO-dow3u1tHinJL5TlTPkDoJqbi_RUydUGbfsIAGB936NzkS9RFcjieKvch8ts4AT6zyjMQgWhmVUvLes1ixU_IXRYbuUx4bRX8bcnukV95FXio223hpAkUqn8W1OpouuCgPoMTKm_IDOXItSnrXHhRx99XdTu9av3T0O3Juni4MBcoggMloO-LuKbma6Aw6fIrB-JWcUVHM9HntTmky3RLdZkAclXHy92P8TmW5oxpdQUJu--MKAG9w2DGXyNpz3RoacGboDzs9Xgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pImYVWa3rTjslvG9yUwlFJzUvqcRgKRAHm26B6FCBPu33ce7mg4HPxF5u_T91V297xWftvhfRjlxfsj1BV8TKmaBc_1C8wlw9znrgyaNZj9GE6qTik0EL9whsh2jmQwLXhi7KW_JnSqXWLC6-CgN1CBWxBbo3e_BnHA9zcXf6YmWLJf6HSBHj3HzyakdhoaC19mTtRykGUhVPb33NZJpqE8zzu7EGQg1qCXE9zkVY-VluEEu4biRTbjqlk3d1nXYgNmu4zsIzMRvczlNQUcXoyRHdRciFqiNwUy0eIK9SUFKzUp1D2P6VkK9xOZJTzbyL_eNPKPZQwA8tT2HN3w3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBAMvb0jxeaD3IKs-HpbGyA1Xkt-vatM64RMRd-ylVGHVwTnO-f9hlQOrDN3o132HU7uTwk1v8Zji-S4tXd9lHxVHIcWbufjGYehNwcdDHj6oJL01571clvU8ttgJvF8oyMpkqQfcLIIMVSy58-3G9W0sqjgWg3RNwiPnS7TkGR4aieDMYElxUyqvI_EJzrYXJ0MGRWHgffndKYe5ovDGBG3QZLReDAyQdqi9mTgw2Y3wKz-Oje7wct_E1YhsWdnOK8z3NnOeaPo772t3o8CqM5lPWCkmYW-JBfrPphP6yYKMx8Crp87r4mQu4QAb6AmiduXT0LyrpA6TLIH7ilQVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JK6kvRiJB2CDHRkJGHtWvOcjKkWed_06k_fkRkz-mTUKIXOU-mpH-QL0M7ZIehYOpqby8EPirDwdlRoBG8OS_7aIMmslkX4g7D32yJQS_7hxLdgG0eRHUSnGUX6kSu24vR_99lt157BrHd9ufigvHOa5AQaPel9ix8D9Ir3iu8seC8y0urDkblTzEPljsHxvuHjk_T996qTE8lxMYd-YCMmA6aQGyA1Gx4STu6HSojCyHBiFKJBB17M05WzoDnn8_S6QOssNfH-LUskIOZcPERUBjK30_OaeA0dCFZkmQ8yx4_gYZ6hC6Nn39Hta_LTTzrh3y1NeTPrYM0jMFIc8qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
زنگ اول لیگ برتر فوتبال به یاد «ماکان» و شهدای میناب
🔹
بیست‌وششمین دوره لیگ برتر فوتبال ایران عصر امروز با برگزاری ۶ دیدار و پس از ۱۳ دوره، با حضور ۱۸ تیم آغاز می‌شود.
🔹
بر همین اساس، برخی باشگاه‌های لیگ برتر در آغاز فصل جدید تصمیم گرفته‌اند با طراحی پوستر و انتشار ویدئوهایی، یاد و خاطره شهدای گرانقدر میناب را گرامی بدارند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456051" target="_blank">📅 15:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456050">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohcMlk0XXSIarfiTPdEf5jFB-SwitzwaMBvhV3NyDf9waT-iNgJI8x2FiUavlyHuawYpkoA2V3neZZcNi68vhpa0TX2ZjttH9t_HUp5qgJqBvVoshQxWM4FUL_pfyxgKk7iLI-GivcEdBhyVzGI4PxmO8QBdWuIHoBrjTBev_VK537wsTOpsAOG8du6K6IjOPpYM341Cycrnx8FnPcXjnydKojl66jCGs3W-4pgbhaQ7oelQnZEp7ANEcnyxKsL-pVHzzmCCvRv8EG4EwzN5fIk8I5ftsliKJrb8AtiUP_a_Tgyfz0qXdmr2CqXhvDIj20rwH1FX88gYSWrrcH_CWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت‌سازی رسانه‌های ضدانقلاب از اتفاق حاشیه‌ای مشهد
🔹
روز گذشته ویدیوهایی از برخورد تعدادی از عزاداران در مشهد مقدس منتشر شد که در آن چوب‌هایی به سمت هم پرتاب می‌شد.
🔹
این فیلم‌ها بلافاصله با آب و تاب فراوان در رسانه‌های ضد انقلاب دست به دست شد و به نادرست القا کردند که این درگیری در صحن حرم مطهر امام رضا(ع) رخ داده است.
🔹
بررسی میدانی نشان می‌دهد که این ویدیوها مربوط به فضای بیرون از حرم مطهر است. در داخل حرم رضوی، اساساً اجازه حمل هرگونه چوب داده نمی‌شود و محیط با بازرسی دقیق کنترل می‌شود؛ بنابراین، نسبت‌دادن این اتفاق به درون حرم، تحریف آشکار واقعیت است.
🔹
هرچند اینگونه تنش‌ها میان هیئات مذهبی رفتاری پسندیده نیست و انتظار می‌رود عزاداران با رعایت بیشتر اخلاق از هرگونه تنش پرهیز کنند، اما در هیئات و دسته‌های بزرگ بروز اختلافات سلیقه‌ای در نحوه ورود و خروج یا خستگی ناشی از گرما، امری طبیعی و قابل مدیریت است و نباید به دعوا ختم شود.
🔹
عزاداران و دست‌اندرکاران هیئات باید بیشتر مراقب باشند تا این حواشی، اصل عزاداری را تحت‌الشعاع قرار ندهد.
🔹
با این حال نکته مهم‌تر که باید مورد توجه همه مردم قرار گیرد، دلبستگی شدید رسانه‌های ضدانقلاب به بزرگ‌نمایی همین اتفاقات ساده است.
🔹
دشمن به‌دنبال بهانه‌ای می‌گردد تا اختلافات را نه فقط میان عزاداران، بلکه میان همه اقشار مردم دامن بزند؛ هر جا که وحدت و همدلی باشد، سعی در تضعیف آن دارد و هر جا نقطه‌ای هرچند کوچک از اختلاف ببیند، با تمام توان آن را به رخ می‌کشد.
🔹
این رویکرد دشمن نشان می‌دهد که درد اصلی او وحدت ملی و آرامش در جامعه است؛ وظیفه ماست که با هوشیاری، این بزرگ‌نمایی‌ها را بی‌اثر کنیم و با پرهیز از دامن‌زدن به حواشی، اجازه ندهیم تصویر زیبای وحت و همدلی زیر سوال برود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/456050" target="_blank">📅 15:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456049">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
انهدام پهپاد MQ9 در آسمان هرمزگان
🔹
یک پهپاد MQ9 توسط سامانه نوین پدافند پیشرفته سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان هرمزگان منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/456049" target="_blank">📅 14:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456048">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58068ad65.mp4?token=uGb4PjLz49C0pES-ZPZygkVXk3GR34dWauJQfAMhAmo93CFeEl7_IbtcRnkMwMbSTwNZvu4B9Kzn3rybvEmH80ejms8pnzC-aKvPPHdh0RIcgySEFGv2ly_ly7gY1Bm5CDVLoOhOJaiHX8j-VZYp2yfBzDiWEbCT2svKj1f5VCwA_T8BZI221k6R3bGSGk0CVFmkMHWo9o82TA0bQJsLfQAMVhLFOZAIRsn7LHZ3KF4jAqwdz0tG0U0R04s1hYLNGC1hw0d7KvFyegr1s0wJrSlEy_40B1lwW1aeaLA8qYnWJF11ob-Aj41ScZZLZC69fUu_m3ELnAesNAFaIT0uig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58068ad65.mp4?token=uGb4PjLz49C0pES-ZPZygkVXk3GR34dWauJQfAMhAmo93CFeEl7_IbtcRnkMwMbSTwNZvu4B9Kzn3rybvEmH80ejms8pnzC-aKvPPHdh0RIcgySEFGv2ly_ly7gY1Bm5CDVLoOhOJaiHX8j-VZYp2yfBzDiWEbCT2svKj1f5VCwA_T8BZI221k6R3bGSGk0CVFmkMHWo9o82TA0bQJsLfQAMVhLFOZAIRsn7LHZ3KF4jAqwdz0tG0U0R04s1hYLNGC1hw0d7KvFyegr1s0wJrSlEy_40B1lwW1aeaLA8qYnWJF11ob-Aj41ScZZLZC69fUu_m3ELnAesNAFaIT0uig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از بقایای جنگنده اف۱۵ منهدم‌شدهٔ آمریکا
🔹
افسر ارشد پدافند هوایی سپاه: این جنگنده با سامانه و موشک پدافند هوایی نوین شکار شد. @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/456048" target="_blank">📅 14:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456047">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NARuTTFG23iRsucc8HuKqbRaERrn1GsIan1E5sSzMJ--ayRw91UVv-XKoFumIqmEino9hahwcmshgPRQdHCUO5fBK-EPLgs3hY7kxve1kYMExL_5-tYkbuZgRjAdhHH4JkPNmh17h_62RBjS2P_H0Iab4IXOrQilp06q6Pe9IKGBJMbr-nrN1s0Xi_L5zYOgRwAK82fqc8q1tRh29WyGAMWkYKnk5APeLRvh5-4kiUjj-2f2OBMmwHLUhu_0_Z63SK6svYLlu4lpR5DR4QgWJ4kxtjf6Y6dupSC-TvW3Bv709-LQZrfOqBA0HMvzUnqa0N7qhNgTmNVBga37VGj3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه طرح توقف حملات در دریای سیاه را رد کرد
🔹
روسیه پیشنهاد توقف حملات به کشتی‌های تجاری در دریای سیاه را که از سوی اوکراین و با میانجی‌گری یک کشور ثالث مطرح شده، رد کرد و گفت مسکو حاضر نیست به توافق‌هایی بازگردد که به باور کرملین صرفاً به کی‌یف فرصت تجدید قوا می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456047" target="_blank">📅 14:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456046">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2252485e79.mp4?token=OSFZwUxa6wv9kMrQx7v1iLgXdj92y-KYFgwYHvlxL96X1J-NBHv4-X4LP_iJurE7ePTqn3QnvthV9dtC-_bDQ1hkv_jVmSZqL2c-LUD5xjZdDHEpXzjkqGx4UHAVBuYyoieIAv2LXaEY_UoZUOniM17m6az9SEtcA_Nck8rikyAH48Im1GBkmNCTsg2OBbip-T39Q18t5HdI7Nf3cYiu_Kl6uXwKGiVo8Xnyo-OK1wIg_1KcdirqYA2t4tfw8KUEBEbVg6dZ5FpUKXTJNl9kgWopKPfYInWhuJj8-QvibY2gNXLeuDDSThWc-7SaR6AIq3Vr0fCRSiZ9jDrQ0vl1Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2252485e79.mp4?token=OSFZwUxa6wv9kMrQx7v1iLgXdj92y-KYFgwYHvlxL96X1J-NBHv4-X4LP_iJurE7ePTqn3QnvthV9dtC-_bDQ1hkv_jVmSZqL2c-LUD5xjZdDHEpXzjkqGx4UHAVBuYyoieIAv2LXaEY_UoZUOniM17m6az9SEtcA_Nck8rikyAH48Im1GBkmNCTsg2OBbip-T39Q18t5HdI7Nf3cYiu_Kl6uXwKGiVo8Xnyo-OK1wIg_1KcdirqYA2t4tfw8KUEBEbVg6dZ5FpUKXTJNl9kgWopKPfYInWhuJj8-QvibY2gNXLeuDDSThWc-7SaR6AIq3Vr0fCRSiZ9jDrQ0vl1Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از بقایای جنگنده اف۱۵ منهدم‌شدهٔ آمریکا
🔹
افسر ارشد پدافند هوایی سپاه: این جنگنده با سامانه و موشک پدافند هوایی نوین شکار شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456046" target="_blank">📅 14:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456045">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c86100247.mp4?token=l5MSYrx37OBmB2h-TNUbRhzfIKsVAqz3kVy3oEw3EhBi91XknGCDlDbBRxs_CL9pr_DPxpDvAxdBJv9JFmar9hSh8HLeday6ZZCVNeL2p6lhDuEgPw-5D9nAQT7tigIdMMDmcsdazYocFO4j16H-fGCKehck4Fnv1qCJGJkPnVtXgtGljGKD7gjY50knpRaPeHkztoYG4eeaQ8ulhRh86ZggK0KgudKTSRzQdQgCw0ACO6OJqUrctQvWT4xo14QtIVUl9XiTMRlnx-HAo8uCY6RDrfJmRb1hGQZcbtKq9BaxdlmW7BN7md-qEotCvVRftaz2UtmMNPWOkFZA2_EPDBlMgZunOVeiOti-VLT1rT28fP-0sWxkDF8AYyOp42GXaKTaA4kry88M-WlVPgweXRkKC6SnIC54GBeIWmBi4BrOKJUOkvOqIudo9Kna4tVpXX28ZLu5lncwJEU-UQcq0Dub_Mld7o83jweba7luIB9vreW-YdfaDS-84beg0l81OD62xS5huqlgk5hnUgjQ2oOj62Dzd3DQEwud_IwiOQBRqM-RdiatGP_rJzgdxDhtMQ3f5CAQyxrkVRT5ie7Bdc2TZe2BoFoObnyE-cP1rjYc6LhrPZmXjfJJupx3-6EfvnfrhZ-OAdL0PRLPdudV5uU5yymg_skGmNaKV09qo9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c86100247.mp4?token=l5MSYrx37OBmB2h-TNUbRhzfIKsVAqz3kVy3oEw3EhBi91XknGCDlDbBRxs_CL9pr_DPxpDvAxdBJv9JFmar9hSh8HLeday6ZZCVNeL2p6lhDuEgPw-5D9nAQT7tigIdMMDmcsdazYocFO4j16H-fGCKehck4Fnv1qCJGJkPnVtXgtGljGKD7gjY50knpRaPeHkztoYG4eeaQ8ulhRh86ZggK0KgudKTSRzQdQgCw0ACO6OJqUrctQvWT4xo14QtIVUl9XiTMRlnx-HAo8uCY6RDrfJmRb1hGQZcbtKq9BaxdlmW7BN7md-qEotCvVRftaz2UtmMNPWOkFZA2_EPDBlMgZunOVeiOti-VLT1rT28fP-0sWxkDF8AYyOp42GXaKTaA4kry88M-WlVPgweXRkKC6SnIC54GBeIWmBi4BrOKJUOkvOqIudo9Kna4tVpXX28ZLu5lncwJEU-UQcq0Dub_Mld7o83jweba7luIB9vreW-YdfaDS-84beg0l81OD62xS5huqlgk5hnUgjQ2oOj62Dzd3DQEwud_IwiOQBRqM-RdiatGP_rJzgdxDhtMQ3f5CAQyxrkVRT5ie7Bdc2TZe2BoFoObnyE-cP1rjYc6LhrPZmXjfJJupx3-6EfvnfrhZ-OAdL0PRLPdudV5uU5yymg_skGmNaKV09qo9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیاتی از پهپادها و جنگنده‌های شکارشدهٔ آمریکا توسط سامانهٔ نوین پدافند نیروی هوافضای سپاه
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456045" target="_blank">📅 14:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456042">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146f452f88.mp4?token=j9cstrITZd4GKYnq-fjEPWzR2tcOyximIuKorLD-LLgR8IJtXQsryQBZhtBQZ41I8eGQljHNWFmGuI1ZitfSRzjiMbQ1LTyYfxZFYT0urB64JjyP3EAjSYJ-jlSvlz3IECHDfxnqy81JW9s34_Cj5BvQvCotM6eQSZxNaLd2MdKcMD-mY0E9EQOoWC9hhYIlCqV_oOzhxCz_msX9_kNW0PxrMakac6EVmqyflW8-z6JOE-DThaKD5rEs8IvLwafRLa8ZICgF4M2iJlFwTv3in3ln7UHHWmQ993Llzyd4YP0YO2HtK-y8gtYki9S_98VY8x2b1fUUydBnwHLpno-OdjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146f452f88.mp4?token=j9cstrITZd4GKYnq-fjEPWzR2tcOyximIuKorLD-LLgR8IJtXQsryQBZhtBQZ41I8eGQljHNWFmGuI1ZitfSRzjiMbQ1LTyYfxZFYT0urB64JjyP3EAjSYJ-jlSvlz3IECHDfxnqy81JW9s34_Cj5BvQvCotM6eQSZxNaLd2MdKcMD-mY0E9EQOoWC9hhYIlCqV_oOzhxCz_msX9_kNW0PxrMakac6EVmqyflW8-z6JOE-DThaKD5rEs8IvLwafRLa8ZICgF4M2iJlFwTv3in3ln7UHHWmQ993Llzyd4YP0YO2HtK-y8gtYki9S_98VY8x2b1fUUydBnwHLpno-OdjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ریزش تونل در هند ۷ کشته برجا گذاشت
🔹
دست کم هفت کارگر بر اثر ریزش تونل در ایالت اوتاراکند در شمال هند جان باختند و سه نفر دیگر همچنان در تونل گرفتار هستند و خبری از سرنوشت آنها نیست.
🔹
به گفته مقامات، در زمان وقوع فاجعه ۲۲ کارگر در داخل تونل بودند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456042" target="_blank">📅 14:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456041">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7618ebcf0.mp4?token=ZnFYgMgNyjzkpS_cWms-jYFF04Yo-KssV7nQqiv5oXxAoXhbsv6JnLIrERFIsYfzDjivzHuSGuXFRMvufcC_u4dUm8B-aHGc4kCypd186ZEUEC63k2xsp-gWWp0wDSbcmCLPO4_T1vgv41_4vgu6orcf5q5jRhtjPtzlWFR9SqoIzJ4P5LTKu74zGd9PWFPShAzGltJlSV-fVqMGo2rZDNa01pbLOYqf8T122S3RGiQIAJwnB5nRvVQ8pQvDtpN2cMgBVPwdJHvqnFSskuhhOYMOyLWFv-fzzxrLN0UU39uPBvk5sQFkm7S_K9Xy2BKdXy7Rkzn0I2F8Xri_c2C_ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7618ebcf0.mp4?token=ZnFYgMgNyjzkpS_cWms-jYFF04Yo-KssV7nQqiv5oXxAoXhbsv6JnLIrERFIsYfzDjivzHuSGuXFRMvufcC_u4dUm8B-aHGc4kCypd186ZEUEC63k2xsp-gWWp0wDSbcmCLPO4_T1vgv41_4vgu6orcf5q5jRhtjPtzlWFR9SqoIzJ4P5LTKu74zGd9PWFPShAzGltJlSV-fVqMGo2rZDNa01pbLOYqf8T122S3RGiQIAJwnB5nRvVQ8pQvDtpN2cMgBVPwdJHvqnFSskuhhOYMOyLWFv-fzzxrLN0UU39uPBvk5sQFkm7S_K9Xy2BKdXy7Rkzn0I2F8Xri_c2C_ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور دستهٔ آهو از مسیر پیاده‌روی مردم شاهرود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/456041" target="_blank">📅 14:10 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
