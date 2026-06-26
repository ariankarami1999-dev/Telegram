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
<img src="https://cdn4.telesco.pe/file/YcbzCLjWb48mP49v6iPvrwlclOE2xD8E8ECso0GdyrUWi-LEyEEhWpCZDwv6MKegyILTXmgQSZj2M1frEefpZxbYgMt4TuX3FduvIhCAdK_oDgSeiNJEOp8-ESCv6NsJL5gSVE5k2-WpED4ldYmJKQW5HYe3SDZjiAaQtFsHsceENqNFsTLB9ykTkCskix6xFk09zO8ENW2aEDtdXlMCEviXgIr8ulkyu5onlxgCghcirqvQi874WZvQtMR0xElD4-zjjrSsRpcSe5ZJ3iRmN8A4KcnlU4bCxR3WsfGufRsrxM2wusMLf2TleVBc_pyWZIhpbXGsC9PEV6vKSLTiuA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 10:14:50</div>
<hr>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9J2WgJ5JE4bNwwdz7q3V2IrUVuUtOyCbKQMhCWopxKc1s6gix1hOSQOB24hmiOoqWoB5x08HGAydJYskEYx9uJ9fB7VnZeWF5pJJpDrJVOMnu_47qlJsqCRfP-HOpzs2qb0DYgznXUdQcIv9l1fZfBnSuOa2GGqlnj7f10NIymfektHzHhIgN_j39xmwWiE4ZQufHxDVJBCArVKFr2knX3wNxadbTNZDzc9agKT5UKobteysFOWA7d5CnI2vyGz9gYz5v9JuSejqwGuFbqIzFAPUn6061WK260Wq5q8Ifk9YPDRe2giW4GzW9wG7cma7pXSGwOOuYbHyQbhN_p5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFdFiG6Fo_21l3eI0g9gf5NGpCehHQROmy9gqjvXJpYJeTEPafgkUx7nkUKtMtjFP9wIeLMyJeCLfsclv0NiA-jEOkHOW_CEpgQ6_y8DF6v8l3r6VeLmhIvk_r3NCqjmuu18gMJpj9xRmp9ZZQxCwzTEqVTK4KLA_Fl-R7i_MS7BeJ8rqZCPWxPGw5fQ-zqyKEpNrHL2d2MktcW40qhVBwp2CPrCbKJVab5MSSLSKFMpulUQDNlhAT33DH8tamqPJNB-5RSGquoUGFYyPHa8ivRjt4VqG19a2mNwpC9ZlUClHNenuM5RQAb1z5EazGe_BeH7Qtjgg7ZKZ9yRI8U_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6jRmf0ba--mShtp3pjmojRkhZCp-yUBEnp6GPKvFtb3MMpcG_cIQzwaod3z_JK_RX0WcI43aGl1PG8XmYwzcaGgQ7dZllPn7bL_tAMkqu-e8pnolZdB-Q-a6S4t4t_MRQdvzC9tEcOt7r153fqzATAH8LYRxtoTYUlgM0XHwMTIqMH_IdvxcS2oe0cyQ02n1aEQvjki0NWaxnrRN5V256yS5ch6xnrJnJo1ycvk2uS2MEvUjvXYooNISJULVTX_0ILL0iz-jyHamKmAPPmPccXw6i0CkTHoLu9aZhHWnUtG1tZkcqsayXmxDu17jTsRr3B5DD6yTk1vufypS2cbFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=FV5QME_MxtPvyGnvdYt6lEapBQUZq-XpE48FOaWhF5CPwJ18KBnoCoA08VDezzVUpcsIRT2spFlfBHzAHYsCq6jBYhE4-Cn_FCkreWenalal0dy_arzkVBbT8R6NSZDpf0dPmtiN0RPzUAwCiXwpufgkhgaItW21a-1R6TPVljX47IriqzOIi-cIyBt9fkuTn2g21C8CwMiQEYeGJBEGCmyCNiAROgKZmbmMeD-8qSB2l626lilRnm2a-sWD1XHhSj1agjxz2S2uBlI_6iuY8YMGIfRvXDVwA-AGZD7homXqlyuS6LRZ0Ha-brwJD9A4--yT5zyEj9QdzX2VlRFjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=FV5QME_MxtPvyGnvdYt6lEapBQUZq-XpE48FOaWhF5CPwJ18KBnoCoA08VDezzVUpcsIRT2spFlfBHzAHYsCq6jBYhE4-Cn_FCkreWenalal0dy_arzkVBbT8R6NSZDpf0dPmtiN0RPzUAwCiXwpufgkhgaItW21a-1R6TPVljX47IriqzOIi-cIyBt9fkuTn2g21C8CwMiQEYeGJBEGCmyCNiAROgKZmbmMeD-8qSB2l626lilRnm2a-sWD1XHhSj1agjxz2S2uBlI_6iuY8YMGIfRvXDVwA-AGZD7homXqlyuS6LRZ0Ha-brwJD9A4--yT5zyEj9QdzX2VlRFjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=pYjXjK5qPQuNnyviDJNPDuPH7_tvnHJfCnXr6i72Olh1h2ithz0rosXibIAwQX-JuUiKXj_YF8czaSXeRuH_baKte4RYxbdsgu6cbaL6Tg4Vef_dkPRYCV3fJqf2ASN7-lIgg7iJc1Z6-woBGStn2bXWIUkx67atfd8BNAhrWmggaDbs8XSYBF-CUQuGn116qu_MQhfcCuK3NFh0DO2saiWLvqD7-ugHLZ-_S-TASxXPmixhnOys0nVzJstdkFrUYIWhPoVWBkkZGkyaLBDzMe8VizwrhvSGwG1rRXCKHlj2QVZWVd4Qu_zuVybK4b7MhGhEEV8JTnJgKUpyztQFvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=pYjXjK5qPQuNnyviDJNPDuPH7_tvnHJfCnXr6i72Olh1h2ithz0rosXibIAwQX-JuUiKXj_YF8czaSXeRuH_baKte4RYxbdsgu6cbaL6Tg4Vef_dkPRYCV3fJqf2ASN7-lIgg7iJc1Z6-woBGStn2bXWIUkx67atfd8BNAhrWmggaDbs8XSYBF-CUQuGn116qu_MQhfcCuK3NFh0DO2saiWLvqD7-ugHLZ-_S-TASxXPmixhnOys0nVzJstdkFrUYIWhPoVWBkkZGkyaLBDzMe8VizwrhvSGwG1rRXCKHlj2QVZWVd4Qu_zuVybK4b7MhGhEEV8JTnJgKUpyztQFvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s34mOHMeuVC0jOaF1fvtKQlp5pi8_4eKzJ6oJ-mk45-IH2MD7WaXoZlGEGH1ya4XJGTgmas3M4Ehjbe9bhLP05REIeD3tGl2SLqkwJ2KT9i0nDMeXPfpGCPsJtI4MGiSDF4aEvElxraVw48ufVI6XmFxCy3ITsYQWqrv_IcxyKy2wle8oGQ1Mp8JGrsGcXmt_KrH5ZYXYtlZSC7eWqNxvstn8U-v1H14OcS2XhwEVQqS8loELsDqvK8MqMEwWCcxz4bPU6xYYZ7T7g7K5o1YCiUln1tkVOVc_yw6p31ev35JCp8ganzf3LSCjjoylkK2t_yqOpEdWJtNkw5XjMOSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/budDXemWSIQ7SkoDFzao16aXe1hInTtqIATa672agPsa9WF8EDsKLaGZV3l2WyzcdOnzy7lD-3AEzDARLU5DylmTGzy0xod2cYQUoVyaiEDygWz-aP4E3vtWkqMWNxQJMjnLh4M8a8tQhjNAa4Bv1ahYqY2UsYIJXOyQRJwyJ-kc9iYNaeAxPHkEf-9b9jhSA_aFjFd_9BNpDx0NOyB7h1peFf_j3XVoUfJM6YCCcfUQgKQ6TLuUAshceY4M24WeK_XLFURecglGtzjYh-FhsWLTeO-BGHNOc3_FHV_ke3Aq8JfdVy4vhfqBQWEuwqtDN5V_HvOy3tYY31T2d7gnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=c0tT7NJILZpPvsY9Qa_MG0_zT8zZvgFkUhOG4DHutGP_Fx04jwA1XvhCAzzfrXbA1WPCkVG-bhBDhplXaxoVWsHR3amGwXtlul4FVaWKh0xwTKj8dfhZJqajiwl0Bv8zFpSg9npH8C-BQBY8RWdCG0aMiwK1jTVLlc2TtxxqDRGk3PANTHcaVL0X3OpmDAy2TFUnuhH9FJRDGM0yL1xEYouTP0KKWAQIrrOcLtcKeLpbbIoT_4S8W1mrjP9HRfkaPv27oBCckaXIBFkGVemRBXiYK40lvgrPltQ0WZ1ncfr9OfeFEx3x8iCR_skQNb1dKmNfbNA_54gZ_VTFYSJixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=c0tT7NJILZpPvsY9Qa_MG0_zT8zZvgFkUhOG4DHutGP_Fx04jwA1XvhCAzzfrXbA1WPCkVG-bhBDhplXaxoVWsHR3amGwXtlul4FVaWKh0xwTKj8dfhZJqajiwl0Bv8zFpSg9npH8C-BQBY8RWdCG0aMiwK1jTVLlc2TtxxqDRGk3PANTHcaVL0X3OpmDAy2TFUnuhH9FJRDGM0yL1xEYouTP0KKWAQIrrOcLtcKeLpbbIoT_4S8W1mrjP9HRfkaPv27oBCckaXIBFkGVemRBXiYK40lvgrPltQ0WZ1ncfr9OfeFEx3x8iCR_skQNb1dKmNfbNA_54gZ_VTFYSJixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=OPq3cR3Qo6hhZnA544SqRW1zTB4Nc7i-pxNq6PjN4uhFo-_0wZTHtg-dfM7qan4ntEVLD1WuLx7zl4RzsQBcqfOHiF03_1QHFlLKvVzGwPIJVwi-p6qQ8NIutEXCXPBBndmLWEekyj8ld8uhibLR3TEV92LFVBtzuvjteIA4wDhXKduMmbu4RAkeDixWC4Dva9fREoYIASDk2qsAbgq2ENcoNCsfwTedn__GB8i-9KpYglj2M6TwHWX6IdeDs1plcYTF3Mdghowt-a_liRTVvPHYxlNV8nUTOXWf1Tk3cjlhqvaufI1ZzvR4HSrURn57Pm-0gBleuhi_atNz3OtzRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=OPq3cR3Qo6hhZnA544SqRW1zTB4Nc7i-pxNq6PjN4uhFo-_0wZTHtg-dfM7qan4ntEVLD1WuLx7zl4RzsQBcqfOHiF03_1QHFlLKvVzGwPIJVwi-p6qQ8NIutEXCXPBBndmLWEekyj8ld8uhibLR3TEV92LFVBtzuvjteIA4wDhXKduMmbu4RAkeDixWC4Dva9fREoYIASDk2qsAbgq2ENcoNCsfwTedn__GB8i-9KpYglj2M6TwHWX6IdeDs1plcYTF3Mdghowt-a_liRTVvPHYxlNV8nUTOXWf1Tk3cjlhqvaufI1ZzvR4HSrURn57Pm-0gBleuhi_atNz3OtzRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqBOGD9bIpG6m3swORo2sMF5Lx6KDH8xfA999sxYGEII6v-fjjGKp--GL_f4qAcVszv8ApCF4F65IUGpdHCal-e5FxCSWsPl3GOC3VHDkSex63rM90reMlygfG_emTF1jAJBuN2Y-rPR5a03_BnHxk8ezYC0FlaknBm_ZOYQEB2cdSwZoFickXaRob3dQH1rSgkSL4ZNdFj_-33NqgKD_RAbgiR69012XHoQiLRLhKDuWbipGMKUzZchd4KaXTOQMqA_Mu2bPiTshkujmg-tC4fSAwT4LKKSMYODPSqV-d1c1rZvv6D6a9lURLWwVoyCPP4k6Nu39-OPJdS1aAwD-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqT13RyNpxvUyZxQNFhVYfQBzIKdeLIX-Wx3tewxuP5oCuimFJi1Y5a4guXAEES5e8XGvOKKLIw6w2W8sxvWzUSm5sgZb3CV8xBuEDUFtVGBC3aJbm5RpA5rbTftS0PZVXW4nKbJ6L9AUlmHbvEORdos0O3eW-Nfzafm_GNZ9Zcda1j34Kw79jObwWkAc3s9iE-X3J8S8mAPJbf8eKKGzkPWaMau4hePQz85wBuhjEi5wb1F61e75ikqXinmHFmfe2Y2IR3XR3V5HrAwU2rrfCqvW12n_87wCDI-Jzb022Fh9lnpve7BsPj6WTy2uSRtmxHaYXGebIsa4ghxxdVVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXER_l-LBMLiXUNB33fB_pVLho1N5j5geqD5iwZNSCRZeRaXcPR7rODAX_LnE_Szi2zKRCO1dAeb4GSYNlF3ZuMKP9cIRsGMs8d2c5GDwFlyL0NqOO1s6CBbPzwRGKpBL8VALtX01MDiZ9uC0mw_7aNYkVfOFsbc5DANIYPbEomTjZs29DVOQXCRKvXTLxn5HkMMkcvfugzA4UzisZck7ljHcJr0AnO-3h8jTuHpVBd8qqP2r3UZYsqzqfsRbZqv82noRdl9bdBw-jZEky-ZpfyQuJew0FLLrHYpMZVyFdf9MAtj1nOVqLTSKvZXIDACEBt5TJcrjxRta6sgm1PiOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=s2OqxLCUisCRNVZmsyQ_bjVdbS2gYV765ecd-Eh3w-Eq4C0rBwDbtBKNXlcEHaXcXmGj1bd2fRMhOTEyQRRw5moOQIcR21dfPJD_JZoRmOcDJPI0Fc0JNjyhvXBjX46zmoaibH6RZPqAklEUcdi606TVoT5Rr2mVIncp-4NC0Iuw78llpIeLRrHlOUKi12W2i-FkCPrlJVwAznvv6fHDR7NUT_cp_9_JVWJ4zurDvVtVQ8Rep6s7QmwVd2s0Sl8H2JQyQ1enqDZlz0Z2crxcFZvGr-GfeeTicXaWq0F8sfm5N6QKvHMG7Wxy-nQWFASSxT-7G1QrgRVNQFev7nRV6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=s2OqxLCUisCRNVZmsyQ_bjVdbS2gYV765ecd-Eh3w-Eq4C0rBwDbtBKNXlcEHaXcXmGj1bd2fRMhOTEyQRRw5moOQIcR21dfPJD_JZoRmOcDJPI0Fc0JNjyhvXBjX46zmoaibH6RZPqAklEUcdi606TVoT5Rr2mVIncp-4NC0Iuw78llpIeLRrHlOUKi12W2i-FkCPrlJVwAznvv6fHDR7NUT_cp_9_JVWJ4zurDvVtVQ8Rep6s7QmwVd2s0Sl8H2JQyQ1enqDZlz0Z2crxcFZvGr-GfeeTicXaWq0F8sfm5N6QKvHMG7Wxy-nQWFASSxT-7G1QrgRVNQFev7nRV6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnmc5BM_BATfxTXVABN7ZsU4BordS4eNQI6aaqyKbrjAug-1oqbJULpCSOPfYakPPn9IZ-6ilxl52zQpXke46Ly4mAhmQbWX1Z-k8r-YjEO5u98NFLcVnFff2kRgvZENkQp3Q8xpJFa2dMWI7VyX4iTJmhsmHCkQtgKwFSju7nd03Nj2PIswXOa_UUSqM0_82PRRv3-ahh0OTttH1aNBrl1m6_5DFaf0dRXXf850tcCHdoK48olS356kVX0TxVUsYSMYuzq1PArgATXEtYix8B3gPpmYgj1l3V0vn4w_UGUYBUHR2PpUbchJc90kbBcLfX7eYs7kIprTfShUcLr9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgDyKCIFEawQuKRuajP-DVDVTd1Ga_rSK6An4FYmu5tAxlv8-AM182xBy-1fvpLGrFjCGZX39Vo7QkyKvO30VeKd_jP7vthJv0lRXdNVVhyOaLyaR-qf03n5OxQDg0BnkhMPG_ExvuGqBr0AqR6ZLJ7PPXXYhIqlOaEtqa76UTwGmDHsoLmqho03aA3OksSX7YPHfJjA-3dAGodheWP_4wVpmOeQjI-0lV_0vmjOgko0kjmOcv8PiY5mHQ8zjhvpp4Kf4HlIcj4xwp1SqVgbXdSPimGzuTwkRdj5N_5y4u_8pKUnW69mkSrDfgKmci98brOZDqJb9luH274MhlwRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPPms7ip4Vd21rgDXb36agjZ-_vn8w4iXb3pQhKDAZUvy5O109PYakM_a_j3TXxBLQZfUC0CYnxGynCgMar7PsB1Kl7Ftw-MClNsevzxUO0DNbbhzKq6UXqly0jsSXj4iFTt7m-jdLCwvcEPNlkxzQkTGxglFO_J7dCMfMAdl7zQrUTGVpf04HhuohVfuX0YfUEGnuEkjAbuKHoSenYN1DAMM73OSVZFQnKOTyuf_WwsPWJRRQPE9mJ9k-vW-bLdfXEk8YW5Ns6MSDZwmx_q7u7yR4Gn-Bhun8GEP4fu8BgGqGPWzh5xb60cuvYxmPgsdI12uG6W7wgS10jepMXNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtlnVwf7T60B8fcMhAxJtSFOf3NU_d_ek4ZOA7GUXa_nm6HbrxUTtg3bHzs8442cdN6Nmy4aEBsqtuP7358b0ARijpxGLAeD_2UXDtbiAnvpnoBhuGTnD_vcCXMcLa9k6edU9cxFoQQ90DDlLwww5IHlpUgqc_XB-IAT_9TKcsDV3u_GK8rNi947s9Q5_6J4BL0ta492IR5Jq5yqKGSJye206mCG-5TiWump72EqQfZnpVqDEjaBxNAi3YWioKbo_Jv9965fZb9n1hASe5PcOjGm2OdND2hBFzM0yjtt8687nwtY351c37U2c8cDEE3p25U1Uojc9EqHMRadyVBDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=ij3Uj8-dHo2SNnqPoWNvHjKiA0-7DkBToQPA09S_A2Q4rG8hZ-9EnglXXXUvCiQdslzwxAcHzOUo81vsTVSMR3ALjhxCn5L_xCtGUShkythN-pXe3spSZonWkSaupMiuLEaPNphXZSbVpRv82lCngWnkHvSxmmMHeLO05N7HFxyUB7Gj7BZdl-oili-eu2HLviS4sjjGZb6ie8LCCDYfT8zWpikolNYLGKaKhXni_K6_qlgPkyn3cAdvmH42ihxf_vNCd_5loDD0sUtM66Y9QE-IU1oVUriPboCy2WSiDvXW3qq7YZlhDl8MUkxl6ftrRuxym-m_OCLfkPz2VfEztg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=ij3Uj8-dHo2SNnqPoWNvHjKiA0-7DkBToQPA09S_A2Q4rG8hZ-9EnglXXXUvCiQdslzwxAcHzOUo81vsTVSMR3ALjhxCn5L_xCtGUShkythN-pXe3spSZonWkSaupMiuLEaPNphXZSbVpRv82lCngWnkHvSxmmMHeLO05N7HFxyUB7Gj7BZdl-oili-eu2HLviS4sjjGZb6ie8LCCDYfT8zWpikolNYLGKaKhXni_K6_qlgPkyn3cAdvmH42ihxf_vNCd_5loDD0sUtM66Y9QE-IU1oVUriPboCy2WSiDvXW3qq7YZlhDl8MUkxl6ftrRuxym-m_OCLfkPz2VfEztg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbTjDID7yjjxh4L6IbeNmbhvnRhwHWf_YMBsFp13n2xE7G_DlfPkh3VxrSujDi6dcupjasYLN9adTnoSMbD1saUTMybrKOGs8uZzplF46OxkewZl5ZM9tN1qO_Q7dT_s4OrX7zZfmZtC8xiZ_u2IVw7oxQD5KpzGCkVh25G3pzy_hFYo3W6QAdlX3kfnIe-VWofTvBSh-JnxiTI9b73dTm64HdXUPcHleL6go6Jih7_sSHJRjIVikgBdj80_xRb_nGXOAMN5i8HBJ-C7V78l6eLi-38YU2Qt73aIgvNTHx4VDbl1RjBgQWxn_jWEYq-Crzcj5-kno8dP_A4xCKybUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMW81R_72v72wTrB0VZM6T4DLI4ZPw9dTXDFcflJIv4ioRSwd2fKhGJm2cO45xc3tSXlGxTDoFDBBZLx5aRlNM2F8IUauuVtBDBUhB2k3YnKaj5wdArC-vvjfRaITTOTJDraC5e6rhpFltjYJ7FctDDoQqDMpj7yCy8yI1QbQeuCk_HR5WUHUzEBMZTyRJOdLCeHvKMHaLGXTh7zDPclKbnzbnAQY8Y7I4uwLGtmlmVCKW8pJ4BuCrNlMUF8znQoP-ogSEr_WojjpACnjXtD0iPD7_E8Yl-gpjc6xb_Ipf6RVHsrK0gqLf10bWtBrAoigtmrjIyuFU8GyUGmtbSs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udCQa5-Q8DR0-ETTKM2kNhAsW-QTYbJjeOaiopyypxDDlw8SeRDoEExP177nTrR3Z_4uQk3-M4JmtmUi2hPvQbN4401qSqAf1ISX2MtgRHcqUApzk5OUeAfWunbCUK4SChyyrFX98eGgIJokuAmZukkrHYq8GC-QrMrchT7OOTDNrPr2M2v2U3n4wZcphJ6fKsbMY2hGPOD5ynU-834QMKx0Reb02X7WxOyGp7vKzeyGiVmlwd_4vwlO_8wbszr3lqu1YlCTzkxt22tgEJm0v5Tnqv1gU1SOEqPuSzEbckziZps3be3z4OmV8V16UR41reg5ATP-TBYB550dEVaKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=GlzhJRyQq-ZXf9AvQYuQruxdPaZLyq01RhC4Bmi-bh56VlbuGVSkPUNxA_EJFBE-Nh6Oru6ajxpyw3p9Kb1awGpUaTKT9kf8rDmRHn3z8GOLq-uikzFfg5jvbfv-BbdfFhO-n0QFPnQ14zlKeJMF6CgN_hB37z64l6EqsTmEO_Qg2oV2JZv__DHWPWCe3rzs_bpanCMgcV0Bln7nAj1YeA61m07wywso68pxcX0zSEGAftmCsa1HTcLkmgz-Ic1pmwGjQn2taRHhmL-Rjjs681SUpagPVzahnmhBAPan7U2roqAhhMSR8-8LacwSMd5YAaN2gjEKk1wzp5tu3KYasQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=GlzhJRyQq-ZXf9AvQYuQruxdPaZLyq01RhC4Bmi-bh56VlbuGVSkPUNxA_EJFBE-Nh6Oru6ajxpyw3p9Kb1awGpUaTKT9kf8rDmRHn3z8GOLq-uikzFfg5jvbfv-BbdfFhO-n0QFPnQ14zlKeJMF6CgN_hB37z64l6EqsTmEO_Qg2oV2JZv__DHWPWCe3rzs_bpanCMgcV0Bln7nAj1YeA61m07wywso68pxcX0zSEGAftmCsa1HTcLkmgz-Ic1pmwGjQn2taRHhmL-Rjjs681SUpagPVzahnmhBAPan7U2roqAhhMSR8-8LacwSMd5YAaN2gjEKk1wzp5tu3KYasQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=TxjwV8Dfhu6BiXgfu5mbIKH3TJGZttpga9ewfUSNo6PXuZjOlXyLCD3UfFbp5g2W80Q0CqGiGpK8tupfDXR3SAUzZQI6C9SzF8jyf6mgzH1QXSpT4HqZtEmVm6gnIfbQc65Dd-yRHLFSYi9ZgvySrpaGSj-ZEbl1GqwzUScAuWsTggH9MCA7FPRgft-YQu2WlInvyCopYuMsVeN_QKYGWP_8RtBTi2KBPDhjYTDyDd6Bdv6WdsEdXvW7nLj7gTB49fuy-7wGDNuYN4RgFpZIoKRBwhjBgwjvwq5hpZ5TaBs8Vr7q8J_gz2_GSkQZh11-qwAQ0inB4u8f125HeI_e0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=TxjwV8Dfhu6BiXgfu5mbIKH3TJGZttpga9ewfUSNo6PXuZjOlXyLCD3UfFbp5g2W80Q0CqGiGpK8tupfDXR3SAUzZQI6C9SzF8jyf6mgzH1QXSpT4HqZtEmVm6gnIfbQc65Dd-yRHLFSYi9ZgvySrpaGSj-ZEbl1GqwzUScAuWsTggH9MCA7FPRgft-YQu2WlInvyCopYuMsVeN_QKYGWP_8RtBTi2KBPDhjYTDyDd6Bdv6WdsEdXvW7nLj7gTB49fuy-7wGDNuYN4RgFpZIoKRBwhjBgwjvwq5hpZ5TaBs8Vr7q8J_gz2_GSkQZh11-qwAQ0inB4u8f125HeI_e0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=AkD-qC_nU6cbpIgxvGluUyWVTHkiWAt_u9qwU1Gg4r_g71RZJha6kX-5_3zo93ZoR-lem3xY_YfKSgJjJQ4b4GIYwUHKBJaduhf67Gul5WiQubeidBOoIu1rR2Pg0z9KRtZk-pFunivZBdsJng0nKn_7g-c8OQ5wC52n1KwoMDod8dwPcoZ1gM2VPkCFLP6G5_0qydEoeeKi90KdkJhhDfLDSnrpN3tT-o3-WD2NnPpd-BkPFKbryEt2rnu2Ibr5Mz4MaEemvUgtrBJN9E_Bpq6bcTltVyL7r-m-7Tw8Ea__wvl5fpV_Q1aOgfWvb5jF_vfg-ijSpdgyaNP2X_btSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=AkD-qC_nU6cbpIgxvGluUyWVTHkiWAt_u9qwU1Gg4r_g71RZJha6kX-5_3zo93ZoR-lem3xY_YfKSgJjJQ4b4GIYwUHKBJaduhf67Gul5WiQubeidBOoIu1rR2Pg0z9KRtZk-pFunivZBdsJng0nKn_7g-c8OQ5wC52n1KwoMDod8dwPcoZ1gM2VPkCFLP6G5_0qydEoeeKi90KdkJhhDfLDSnrpN3tT-o3-WD2NnPpd-BkPFKbryEt2rnu2Ibr5Mz4MaEemvUgtrBJN9E_Bpq6bcTltVyL7r-m-7Tw8Ea__wvl5fpV_Q1aOgfWvb5jF_vfg-ijSpdgyaNP2X_btSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AU_2NZ7wcEBNHNyBLWKXN9Hq5eGpX9qr99pNMqeY5c9mNIF0c8Y4iNXRAEVlWV4iivCWiJCNSTgFy6CmmWWve0B3R430EhaEHfYFJbao8nJmCJLPAviyOJ5hXMvVprBJRtAsFT9y3eeWe4Jn5K9RJZiOZJC1vHzC9EuAnHbICDl1DXuKn0JDcyZfX5pom_W_hlO4yqCQQfm5ZrTShMddsxZvIrzEzFnTl1Oko-6yu6bULrC8BTGgOA69awP9mr3PkZX3fhJgnFVjq2nc-vz_C9R7pcx5cVF-ew_-1m_OG8_zquoMoTVcViUUL-b-IcvDQHJc6Z3k--d1Pad6i0Tr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr1PBlA-uWQil68LA5L2eh2NPG0iNtYzloEo_7kXfCBtolgrzWJI1lT9S1RBb8S4-uYNfCqRpfA0vTVZ1fQrS7kH5YpXGldRdG-EtQhimrMYdDQty7QecWiMH4jfPJv31PlIa5R3pxyOgzeNiGui5YRHKcs6g127V1VOTLhilkR1kjJaO97la6Fzb6ZxLXw-uT0x8C0ojzDuzWuvfDv1HZb7ZVcwxgekSySNTP0H_fiJsX6WjPXV4_PaNeLKZGBEo1gwytDUp5CKtn-qlhAMMAFVK0CAAHgfiV-ZqP_-Bi68Et95a1T7R0-TLqEpi3CeaxedfJG2iF65mv7CVdgNLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIvuG3GaxtKyZvzjfN649L9_MZBcO9U7WGKmxqZfatkkJMJ-D1e-h2j9pGNU_fArJmJod_J-inpOD3NRAp8TxbA-cTg56xJwrr0b_y3ytYszCl3adAaatm577vtgPzgJEN2nD2WdWALrLL_sQQ1kWRcItpVOFW1IL9fKySDGo7Q5_JILNH4KwQFrzNTOg9VB1B2EY0EJJtyEEk6rU2i4SncCjsgXealysLomkaI1dDVxxbdWIznvbchzfs7bkuQnAB6gPFOGxAmQq-eHVAM9V76SQ_9mcf1ktWAc1aQq6EsVdvrh3IC5KzhuOf8slvH5wEo0PuEMxpP4IvE-BNAzWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sBT3N9H8m25s1nsXrlirdGadD8dI3S7tOyIIOFfAn74u6cr_1oiJyDpaVCmCrhY9LEe_c7ljR9bqir_8ikCZpE6yrIuqofUL-QBDp8wzYmOZ8ahMIvTeKTH7USXBDnGNkkmQi_gGRQk1nLbts2iuAlqhZF1pNkCGNC9W9LWdpBGpI1v1T9Q1vhAErqpjamaPbOzvE_VFCm-kBfS5MWo49i_6SUjeYSq4YDN2i7f7vHFv67-P0TTvXsT9LGlAFZrZorAzkvWXMgp6mRgKfNxYQamRikrftAvX02DwnEDBooW3lgfhfd2mMRm7zxKgaSalv-hxG4ABuY2Tkwg_VACKEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SO-3hRB4RZMEm_0LahsD-6aAbE1Rv8EH01Tlv_w6KqkOFggXs7LgB94STfK-0kCehvQ26Tm6lj8PdtwEPBlZmkhNExlOR6vP7q5G8WaBcsDyrCxMptngZ_wjZF3xAb_zZck-wwo4fFCTJ-7ej8NzpdXQ1IrBb9fz50orOIKhZ0VgKYmZtlPX9f_uRMRNcgTHmoc8OWbRGdMP-JlMXmWfGMHhBWLfnVH9PejbBXlrvWRup4o2YkBTFKyMODIWDDwQbIuC_-ro0qYa0SotBRD1heKu8N6EMSLRDSg1Trd3MGhH8Jy6wYuAQ8BfM9-GiMGpd-ythoeh0tzt9t6LOh5vXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJCffOt0Wy4dVOcttMEAcwuKPImCDPnhOOUpapJv4SzordTlcN7_Y12EcOB7yqHFdS9uubpV-nNS4fs_VomA1-RisU76E6k5LvT06WkkvEbwfHxEhsvyJ6jxX_TPsC_iRZF_VIlk-yPijEIC4MoW97hJPYYOWBW7-9yshOWO4OG_53tJh54MKityZ06gc3RjTAfhl5rDGxDDvmmCUTR5yeRuXTBHH2TifiWdpVSYXOFhF3jd9wdZDGxZWbQ8CafaLhobIwy8ZeCLodaZ9c0VF85mSBRM2Pjj63vJV7ZZQknSewmt764yHs4DdeoeI-55SDGTq8d9laBBlm8o2PSeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lO5iDGKZNiTHyAdCcxojjhxXi1WTAqG8j9bHRZhpNRcYLH8GbKiSx1Xsvf5FbGI8decK4jsK0kXoB-im_NnOCP5PgkU_Apz73_rJqqEnYY5nZ1WfB-pRcpfwOBehlF5dlCDekJ9SAJXANnKq7Hqu2_6SpszLVr0pwh5V31BgfVevMZJXi0gxF-EzI9tYK-I7T-8nCd9hMtf24ObnKwR71pjtjkQY_uqxoe2BxEvn5rVsecNJwckMD4f0cS6IULVm5HEx3q-o9eCfoIblevaPMDvdAxmyDUqQvotBRq0DgSA-_Hua0DXXMbVr_TV5UAZR_mLcW3F_WLf0j47PJD8nVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNn7gPYQ5qwQAgl_FcfBu_pR5uzQIVnqoaLYmFnIstCgM9Ep3YMxr7NxFpfGsVRSKBXUEQEIoVwK5aOl4PMaQiWhwfdaYcsAklGk6qCkVzDx6k2bOL4hFTbB1hfNo6W2n79wPVCGhM9plpGbwcRu5KAbyYdovhOCPcGpXgk8H4_Il2Ut8e1rac4wtqD1uf59Txy14r5CO5LEGBmAVmWxk1K6HCOETh0v7Cmt3NJZuYLCZ62LxYwPm9OGbA36zKJdK3j3Ow3jydeiqmFjc6rFy7Wq6a0lb27f4w_mHh0ni8bYkjoTWZK4Zbp_YlILYaIPfD5QRj9yvjcvFhLo_KBKtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzy3siwR_4lSNyZdRUSMREB9VpxBMUeHKrNkl8NgP5LnmZfxYGIwt_LqqxTVfvg-dz67Xd1TMBBwdAwQCsrC1WmAs-FJXtaQ9z9YS7AvL0niC08cLB9R-UZ5Ym7k7faKPjgd8bi0Kyj32fH1pdZONxNNxdS64NwrBIF3AKJ4hGvmhS5Jsbcvc06izxcGj76gDZF_Na2OyTb2VBp7R473sMSHeapcAPbs1n-AyO_qqb7kS_WfXJKZt9iYbVuax9zNaOcHkhLVGwJfxG6oZ-c1DvcHks-97V9CjEesPu_qYdPnGEbMOUKPUIR8Ug6016SK8yAJGWeCCC-Yz_-jh_UE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNvrffiPdEjeAVWNMQ_f8TexB_ArV3Jh4LeY7FClRanEOI16kZI7BOGPjq3rW1OI-7kQVWVb0s-rwxjnAdKBPqVFf6K_uahuHod0sHScw4a98T7y_ChaKEMaFCW-LB0HXWHxBRRpXIa5229RZ6DH3kaZJ1weh9GUtM5-7uX5AUbQWXVzLPIF0PcGGIcakXOAy6i2y_IgupSpSvIoY9LqD_sy2WlU1QoyKR5BeH6_XGRmxBlgbGJJ1DOk3Ch2vEXR1-Jz65fvdmdBSaUlztbH3I1RS1EzaToXEbQYkcI-K4VUeJ0whM_K-UOLkDik-HITFpCs2fk16YUlUKCdbDh0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzTsAYo03Ncw15cL8tfToM7UtGLHj941Qlrvz5xXvckcg3IV82X2fhpvQ3AmsYIIxTa1EehFOwaeQ54h1SUnmYOI-6aP11CTYg3p6tOTGkEoCvi3rqhiVv6_aHG2mmXkVt1V8aNoo-UWDwKaGs_YPxaxe9a6PkXBQXPo2A_g8EnLqCiDsdhdy9svEJLzIXYt-9rh0o-Qh3vff7Cike7IXk4HOJ6U2V9_NFl1mbe4VAjG34EIgkwV15U2UlhrexNS8Ac4T_JDrFgnhhShrQGUuRhRiuldPYVucPWGAn2pmKR_LnhzDKJh9bkLxAHpyKGjNOFCWkbdzzTznlGZoOjeRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ibgjr-dcJXqXFHNidVZDTM8PAllQt22PRX3Bw9SAsFRXUR3am4frWVE2jkc7QVgW1GkRmCptb8otAaFiDirEXy1Npaj5vwXTLwJNSyQj3sd_GOFwHOPCTup4Y0mR_TzwOukIORJylmEubTfBiF6PZV4lgWJ3DHoMvSMDgFuPkqWUh0q1FWINnkZuUwx3n8udqSSKBGwgOy5IGwQiiLVYrJCCpQpAvpaJ3fnyF-42AR8FJ60RGEz-SwyvkusX5B37uCy6VSI8KRPta3XU6paX8oK0faNGoyCX39TngWDj_n3gEo6eEgOu7EX82vEEBuZ7K6EmHxJCEF6AHlrcTK-fnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRUmhlZvTjKUqYkal_iYHcH5ewJfIwiorRzyO3P6G1SQCDUNDpQHT92Ntn1DME12lUwksgsPvuB6pQCfAv09qbt1zcf3QKb7NdGdH_bDVTN16wcDyUs3jGK-f0V30i4p7CqecrP0ilveOpCcQhsw3tWLE8oEyISoedLC4TUxTtuluXJegY9LYBiwPFCquX9nbxd8yr3193oFimMkxMq28oLFheB5GJ_Maty_5b-frFjAC_17mlU5SykjrJ5Gl5a7Vk6l2dVM2-0A9_Smj5Woqy2e58Mg4ZXUL5IUOzlFEqFKAgDaRX_Z3YC_haDNk1sfPzmJm9kV3YW2lIGGMx8OxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVVsj1y-Ew3aolIbkOcgwR2En7UrCiVMgaL0pUJ6kjZlcohRc3L5aFS63yp2n-JYQyVJ_anu64vZ7R1Ckq-YxBLwggIvAj5fAarVdFc9GRP7-zLxuiMVpLHUWG2RHwIMf1YLwKWMoyQEbjNgYDwefO3wJR1X2JT0npvC-_B_xci2TOkaNtJyQ8NsSd09KAjn0EsXrRI85YAV36scY0DNYgwcv-SOSeJIh7PH8AIoUi7QSoGgagfppieqzJD3RfXYKk5YNrUKXqX0xZnYKNpTJXCpo9IeWEDdLkb6z7rWQBQAldegdUCP-kELhLrWV-cJ3M5dS13XUEECIOko9cvsAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaE5_surgXiamJd9w9FZd_pZoygUTkAcYPJbcGydYVO7d8fOyG3X_uIPEQsGBUYaJIx7AZWfKoIul5i2t9Cah_mjOyyKjZm4Tqj7hPo6vyESr-DGee7jgaBJruSaW9CMMMKaaJ5njFZth_YVMptE5x-kuigEXB7flQvRjMt4GqTN9MEHgRPEuPnRL_KM6_DbVNQ8642pJAHD9PK-VMgTwqEMctxxueq-FqyBzVxrnbwd7QccslmcF4lkguRPFOCB7_rw5zdbRYbLFeHsY2DLTZdWFQX8F2W7sGWcOQAxaD6YU1NS-CoUyBfYKkw7-Am9yEkElXzEH4gV-UeePM0ubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=h5srxtA3iRKSuauC_rk4s1x_nZXE1k2_e50Tyt2TA1NZB3Ll58oHK2570BE-FQy8Dx1KqA1gP3TbyavOYcB2GwROcfr8ru0XCYKXITrXSsoGYx0EHWSOueD-ZyNKN9BqpMzrDkkc7kb6onA6XJCu3z8OYW4-x6ZATgy_Es6m6UrFDzccCpCR3iI-fKAqMLdEYBMRvyGm_f7Cpd1uRdkFcunQTWAqnCRGJLZfTQMzeycoYe8cRH2IcY2Ev-pRmoa0OYnRvPNGrnyGlNll2kQAaQ--b7i528kMnpE1ktt_qt5XegGLFHQS_RnZfHWxfmyw1_4DquOeIaulVCX05KcuUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=h5srxtA3iRKSuauC_rk4s1x_nZXE1k2_e50Tyt2TA1NZB3Ll58oHK2570BE-FQy8Dx1KqA1gP3TbyavOYcB2GwROcfr8ru0XCYKXITrXSsoGYx0EHWSOueD-ZyNKN9BqpMzrDkkc7kb6onA6XJCu3z8OYW4-x6ZATgy_Es6m6UrFDzccCpCR3iI-fKAqMLdEYBMRvyGm_f7Cpd1uRdkFcunQTWAqnCRGJLZfTQMzeycoYe8cRH2IcY2Ev-pRmoa0OYnRvPNGrnyGlNll2kQAaQ--b7i528kMnpE1ktt_qt5XegGLFHQS_RnZfHWxfmyw1_4DquOeIaulVCX05KcuUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaw0dVa-Dy3ZyPhjtdaaVdUspB8ByuPut1HFgYEIHYTg9soSgi61GvIjx1S6p9ziQULn-vg7V4_syb-vYiqFeR7B_wzRJ5LX2KBIlJ5gb--qLWHhnKzRlBYjaP40yZZfGo05KbVKqfDl846kL7XWGE-i38596Rpjus-llMHgROX93bEJ_2283PFxd58en5_Hg885RK9XdmJJhicAopDUvLWdkQdCy0fIYDgbxw-zOzMXf_Z9VqtjHf9FxWHgHZcus_cXu9BDeIyaqHouYqCx2rzfsdGJV-7RyhTZyxlnhxy0ArY4LQawRNY-UsytAXlkMXQGrk18C6EUecsCfCKqng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=ADvCQMyz2Of4kQUbDFZGYUPdGcwqxoc_WndGBYFXxYGolQDiJcnm21kIq6MYonkv4DhBdwJMw0N0eROucZSbQhPnIoDi6BNpwo0nNiQIS50YeUBNW1vFmWBf-peD6jEtLebNMmpqr723yt3a7IPQnTOrx_OEUbe5-QKQ_fm3VSlgVc3gSebFlxFoT8in-AFMlqF08Gu4AYG8sEJFF5Yykra97wSvt4NX1UvyjiOFgcNv3-J9gySxzSHYGrdtqFZzD2yB0dupF8MesOztcWPkNUaTxTpiQ01FgWDYt1KRdGz8oY9LIs9QUnVY-2_XN82QdASKYwEPzb2pCfYXblumgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=ADvCQMyz2Of4kQUbDFZGYUPdGcwqxoc_WndGBYFXxYGolQDiJcnm21kIq6MYonkv4DhBdwJMw0N0eROucZSbQhPnIoDi6BNpwo0nNiQIS50YeUBNW1vFmWBf-peD6jEtLebNMmpqr723yt3a7IPQnTOrx_OEUbe5-QKQ_fm3VSlgVc3gSebFlxFoT8in-AFMlqF08Gu4AYG8sEJFF5Yykra97wSvt4NX1UvyjiOFgcNv3-J9gySxzSHYGrdtqFZzD2yB0dupF8MesOztcWPkNUaTxTpiQ01FgWDYt1KRdGz8oY9LIs9QUnVY-2_XN82QdASKYwEPzb2pCfYXblumgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=LRvgxced7xRmiQgygP7ht_A4WceHygLacr829cWXmGWGaJ8CJRugasOYw2elbcsJxGZ5xQZ-A841METiHbcIOvWt4vSX3xRulkXxlTetrg97t8ELFZbQPk84kNcXQDU65Y1fFADMG1cap8CjrLuqq0FVTZSQH8JLkTYHy1hLqGHzOdxm-3IgPthWSWLyKTxmrUv7M58qC7UrkztXJQgVR_ShWGqxbvpWktQ8A8ne4YOTymMLZSd6njtElLIGDs0evas1zOn4gHG_pVlryD7eGhC9X7hPZG00uS_UILXBYtR1qSSA4KH8eCHGqElJSoSbWN6rjILgK7jgOkEEqOCAnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=LRvgxced7xRmiQgygP7ht_A4WceHygLacr829cWXmGWGaJ8CJRugasOYw2elbcsJxGZ5xQZ-A841METiHbcIOvWt4vSX3xRulkXxlTetrg97t8ELFZbQPk84kNcXQDU65Y1fFADMG1cap8CjrLuqq0FVTZSQH8JLkTYHy1hLqGHzOdxm-3IgPthWSWLyKTxmrUv7M58qC7UrkztXJQgVR_ShWGqxbvpWktQ8A8ne4YOTymMLZSd6njtElLIGDs0evas1zOn4gHG_pVlryD7eGhC9X7hPZG00uS_UILXBYtR1qSSA4KH8eCHGqElJSoSbWN6rjILgK7jgOkEEqOCAnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5fgx-8N4NhNWZPSQff5BwIoF2eyphPBa40PPCjIlmaBhapaOhOW8l7FhYYPvgDKOzwRBiBnDpJ6K-Sxaay-I-t5RUDPcHXY2oXCn_NKZMiIOQ89r2mvqnMdIh0fswV46tgldzKJVjFJZrukDkIvyDTlMPhBKycQ2HfiotmaOva11zLXj6L_jDu2XevJnXp3ihxklOyrULs8QuwuZGBKGfFVEeHDs-N_ECWQ3EuQU-hkuIh-04sRClS4N1O5XWbLd6lA9KpyMkp5y-O9p-abUAVYBGSxuyxTM8k_wKV9jWuyiWE8O6fzqjk9AAByjQJ01D1ReKBlCue1VvpnzxJUOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=EWnT4rPY--mbG3PjeT_45V3vSDpumfzTbr97ezEK3wzgbNi8ZMNNrpOzoOkFYedJdhAq8hjAm2if9wJGoHURIrqC_3eUvvTmoilLQfRMNXkiG0jEHfA1U4o8Xd_b2QfYwjiiV2S28YXa679rmB4TyCVIdq9usHyWgeXqpmi9Ap8oVzKJEMVzsO9C4mI1OmHvkB8N5dmoitizQvvqvuvvzK-jRZVsZuzhJsiZnUUh4rpg6rIdYCkKiGDfShCPnb1BBlU9y5c5wsEnaoWYedTYxzphkrIcbrmyL84haEAfY2roXz-IWXRyct1sWzMagKltd4Bc0Q966U5Kfc9b_tKgnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=EWnT4rPY--mbG3PjeT_45V3vSDpumfzTbr97ezEK3wzgbNi8ZMNNrpOzoOkFYedJdhAq8hjAm2if9wJGoHURIrqC_3eUvvTmoilLQfRMNXkiG0jEHfA1U4o8Xd_b2QfYwjiiV2S28YXa679rmB4TyCVIdq9usHyWgeXqpmi9Ap8oVzKJEMVzsO9C4mI1OmHvkB8N5dmoitizQvvqvuvvzK-jRZVsZuzhJsiZnUUh4rpg6rIdYCkKiGDfShCPnb1BBlU9y5c5wsEnaoWYedTYxzphkrIcbrmyL84haEAfY2roXz-IWXRyct1sWzMagKltd4Bc0Q966U5Kfc9b_tKgnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp6aZOlw0JWq2Wk84Nk_5NW1bxtwjQDizamRXYuZVvD07mMMlECBI9qkhdzkFlXXm13KTHq6dreemcHPYALjbryNCP6Geton6veKeJQHnhTd1lwRTcvwZSdYUZxt32CoZWCewDSorZJiHSOgLNN4A2NagEVr34zCSODAU6dJHngpXqf5GJG3fCrYc6HjTQYns_A9QPxEM9cKgW-gpZeohTaqUekPRZOXAADPxO3hgGR2PEUARrksL9EibJ6YeilM3gM1NN888-aFEQ-SLmEybwanX57xmK34k3e1POm5REPZTvKEEDt_oFLhHZts1JlR8JO1L6U20D1H1RgcJn5d0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNW17Q1b01wASONodvZ3Eut3yx_B7KynOCecJ8cAJCB3Nunk8eC3PG0N2aLqX0V1FGC-Ky22IE7oXYA8MowtALw3i59yLsy0sooTixryFJsIXBGjxz42kwYIXRkI9X9o2TtauLIHgap0rWrH-DNRic3Z2BayO7t29S295u_72ftx_XSYz2wXbjsY-xvG8LF3HS-xLCWqSHE5aqX3aiEB4TESAJ6CQ06abiDsred_sey7YsA4jjFwCdcBuyukMN7WubxPc46SUAH8j5pzdvsSjGnXCeNYQDE_QWEljk9vsOh2m4VdM3f8hcU6CUGX3eC96mmkh4KTKtHjrsab0A21zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTZ5zK3hkPnj_vi8FHa9Hst-cYXKj4QA03xa6BMEMIS5Ui3eSw2tl4vF0f8lmTxG_CzmEZX6oWky9pVFYzlffUFgBMT9NaEx20yehw-GspTAv7_Y6gq92pJlSgmibD2DalA-rd-pBCgbEGr-mEevgbrfrvkml9_g20U8n_mzaZoh9Iz6UnUXp75wPfFS3yOeGVYeiwBqYMJE9Ynr29bcrnRviMiuqQQ3FyUVpEWBqwtCHhwkYLNanoemOR6KN_s2GEGeH6FPQ8k_gM4TI7C_4AB2NmAp5sdvVBLS2diclHxaThYTB0AyPRcdtsnAyXO9HeiCLU9HZcN67q0wD_v_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAoLuJXY0sNQ2f6vQ9hcAL964a_ojLSGmxqQAHfc4NGMnsp2JdapgFI54fJnhamjA__uJu3ZdYCD5M_5nDveHOuYy2Ok-4QPZ8ErK9X6E3k3KbxdyhiS0NkjXar1M5b4A5iOtHBqPd4xX9t4jveJGzxHF15QAbPz4d-E6ytLHNJA5rotmIsQxv2COn-dHlv2hWXr0ZJ2wxzdOJCMcPfAX9SIQBM7OwkDKgDUF12gcqh9oBsCzdj5lZX0N51_obH3gifcnFf-ko_Xz0AzBl4EvIxPCc61LFbxMTVfP49GaZ6W330RD5RoNtGniHm94Ej_Vr7yxDyUlf96lk2budiJWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=DFKYdVd11mItWrtZ1nbWh4dsPwVVLStAewKRrGnglG_4ru_CIk6RFTo5FpwPD2RCTPFO8KynHMGpLxoodyYDUH7cR5SYtynBTPL629ynIdVhs9CKOUPPNiH0QeodPLrim6nLHhCQZCmFS3D9zCqH5BsoSytXDY_xSOX6_foJzRb2pJ-1fOghL-76ZNobh4LRUo7dmgRi20eoAdoyrBlTVlHoKiQwWHsKjmoNmPVQeHg-IrLPeZYd-1D2JErEsV7GBB8qUGtFewOccIHjhQupfJrzNNebK8TrEDBjxI2YJwihDhE0odgQbf6kn3a02xnYDPovPmBVn_VUKcXHUnFQzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=DFKYdVd11mItWrtZ1nbWh4dsPwVVLStAewKRrGnglG_4ru_CIk6RFTo5FpwPD2RCTPFO8KynHMGpLxoodyYDUH7cR5SYtynBTPL629ynIdVhs9CKOUPPNiH0QeodPLrim6nLHhCQZCmFS3D9zCqH5BsoSytXDY_xSOX6_foJzRb2pJ-1fOghL-76ZNobh4LRUo7dmgRi20eoAdoyrBlTVlHoKiQwWHsKjmoNmPVQeHg-IrLPeZYd-1D2JErEsV7GBB8qUGtFewOccIHjhQupfJrzNNebK8TrEDBjxI2YJwihDhE0odgQbf6kn3a02xnYDPovPmBVn_VUKcXHUnFQzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=XrxcKyKEFbcWaDEo8Dx0C4FqrWFzQYIo8XAtL8zDhS7ofcFWN7Fxsv7RbYmNkekOZ_22vW1lTVLeuiKAHdoswB0gbYCbkIOJhxLwhxAzJQ7wQhwMmf2bURo4-sgr10VuPBxZM6zsKNgSB4y79swXdKk5SlgABruGb0ZL1PzvW3dyUxJ5uy6x2nWHrJj39ftt2eqWkA_ZNC8PWk5ASnEu2FJkYnYJI6pGevlssgj2z0sN5LcI-OwqVDJAy9u7o4FoOAiRA4ePoGkPrpL0GEp8UbPip5VDNSXmRfbDjpeOA-zsQ8DiROzOAUcLkU9oaI9YiMoQI_o2R4DTyZrciKMIzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=XrxcKyKEFbcWaDEo8Dx0C4FqrWFzQYIo8XAtL8zDhS7ofcFWN7Fxsv7RbYmNkekOZ_22vW1lTVLeuiKAHdoswB0gbYCbkIOJhxLwhxAzJQ7wQhwMmf2bURo4-sgr10VuPBxZM6zsKNgSB4y79swXdKk5SlgABruGb0ZL1PzvW3dyUxJ5uy6x2nWHrJj39ftt2eqWkA_ZNC8PWk5ASnEu2FJkYnYJI6pGevlssgj2z0sN5LcI-OwqVDJAy9u7o4FoOAiRA4ePoGkPrpL0GEp8UbPip5VDNSXmRfbDjpeOA-zsQ8DiROzOAUcLkU9oaI9YiMoQI_o2R4DTyZrciKMIzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=GIeyuCQuNlRWcx111yIz_MB9XQkCYayZEetYPOItKx2nq9xllWnKRQKYgQUUcfYw4RQ1PFCoQZyAjgx4ueK2R9Aoiey3DuQPR54YpXs-xPPbVClYDe3RhNplkA-XU1qmg1axD15B7s6k0-SIp7s6BwqF-BVrudnsZihiBBeFppnqpQMJczfSG1tcJtIyxPFRMWvR8sRAUda-KLkgu6zUKM3sYFCgjC5O2HMSk0Ruz2MZt2SXeCJNqFGeYD0Fhi3WmJH1fANxqw3baxZw5zP7KZ8ZJjSHhTHsiwZmTxACxqxXFwDqbFQ34fB9xaGLNOBx5Bf4g0SJifhnAiZwCZCo7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=GIeyuCQuNlRWcx111yIz_MB9XQkCYayZEetYPOItKx2nq9xllWnKRQKYgQUUcfYw4RQ1PFCoQZyAjgx4ueK2R9Aoiey3DuQPR54YpXs-xPPbVClYDe3RhNplkA-XU1qmg1axD15B7s6k0-SIp7s6BwqF-BVrudnsZihiBBeFppnqpQMJczfSG1tcJtIyxPFRMWvR8sRAUda-KLkgu6zUKM3sYFCgjC5O2HMSk0Ruz2MZt2SXeCJNqFGeYD0Fhi3WmJH1fANxqw3baxZw5zP7KZ8ZJjSHhTHsiwZmTxACxqxXFwDqbFQ34fB9xaGLNOBx5Bf4g0SJifhnAiZwCZCo7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=S183dvA_zexB3vM3A4-7FtVHUiTWAPptYwfjFzyrqa0B4mmoWhMo5a2dGW3sZ5gSilKevpcHLTJ6IM1xCpGzzuQYXuxA4ljAMgUEMPQuWSJIyr_Nv4lVAOFnSLG8F2A4YpVK4NbJRn7ruB6sqoW-8iEsMOZ1X2xvDaqUFaOirOrJt3ad_JPeOwoTdn_EARK-ahdlt6Om6KPhXnSpEj47Vg5jCIYp4Wv4jmRD_IIAjcIXsa6I-xhzD0ZYnwCJrTywQOarFE011ztFBWKdg7aGKUaqjX8bxfbzmfkts7_EQJvRlHeJPxsIOKrnhCm9nNcp1Tr6VIfsb7hWFAR1Q3_KlWttCWWRPFZfSteuNF2Y7FCx5r3LdINT8T0s5Sw57et_LVRN1lRf57-DUFeg-odmu8uXMzDsjrUVeCTx32EVGavMO0fbAyxF_yIgKp-1hN4W7DfMB6MTxkM-RsviLTeohwkH35IXH1kC2HLSgTxQh2SrrcKWiJsIsPzKNcEj4m6TZDAHXCYNgaaQQDZ7iLwNBxXfKr6XrHS7sayG972eJ8zSoViZvL8iOyHr7VMXmy89qpTDbWcjdgeUhgs-_8QwrZVNNxqYGsDS2s9ONNOmjDnkdJjJtYuzZQo9AYSVGUFgHjtJvx0eKpVQcJfeRWMeNMKdQbaXOeuCZm_CNfoZapI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=S183dvA_zexB3vM3A4-7FtVHUiTWAPptYwfjFzyrqa0B4mmoWhMo5a2dGW3sZ5gSilKevpcHLTJ6IM1xCpGzzuQYXuxA4ljAMgUEMPQuWSJIyr_Nv4lVAOFnSLG8F2A4YpVK4NbJRn7ruB6sqoW-8iEsMOZ1X2xvDaqUFaOirOrJt3ad_JPeOwoTdn_EARK-ahdlt6Om6KPhXnSpEj47Vg5jCIYp4Wv4jmRD_IIAjcIXsa6I-xhzD0ZYnwCJrTywQOarFE011ztFBWKdg7aGKUaqjX8bxfbzmfkts7_EQJvRlHeJPxsIOKrnhCm9nNcp1Tr6VIfsb7hWFAR1Q3_KlWttCWWRPFZfSteuNF2Y7FCx5r3LdINT8T0s5Sw57et_LVRN1lRf57-DUFeg-odmu8uXMzDsjrUVeCTx32EVGavMO0fbAyxF_yIgKp-1hN4W7DfMB6MTxkM-RsviLTeohwkH35IXH1kC2HLSgTxQh2SrrcKWiJsIsPzKNcEj4m6TZDAHXCYNgaaQQDZ7iLwNBxXfKr6XrHS7sayG972eJ8zSoViZvL8iOyHr7VMXmy89qpTDbWcjdgeUhgs-_8QwrZVNNxqYGsDS2s9ONNOmjDnkdJjJtYuzZQo9AYSVGUFgHjtJvx0eKpVQcJfeRWMeNMKdQbaXOeuCZm_CNfoZapI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=S8XSAFVdFKs4CNu3VHQpEjEBGQdCwjv0uYKN_BjO77mUxJ8HEwj8OTkKPOWUlA0cBDfQlj-GInYw5kO25MsTNc8Ukg2yuqjunoUCb-mge_mAkSubikIrZZZJ-__qGKcoQiAwfgExWFlalZJgIqN585JH84dil2ZLcxXPklQbpEbTBzktRL5w0JUWpdl8mdZ26hRtUcz4WJ4L_bximfnWtEHVogo-x4DfT3y0xtbaRXTLY5K9kZWb4SdrV2n0U3wffH4XMmFyOb4xddxu52-4-k4sWC2tRg2ySuUeJb66nHDYO3a5um5s7N7yt1DgDOp3QM81gg8knslyBil9krCeRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=S8XSAFVdFKs4CNu3VHQpEjEBGQdCwjv0uYKN_BjO77mUxJ8HEwj8OTkKPOWUlA0cBDfQlj-GInYw5kO25MsTNc8Ukg2yuqjunoUCb-mge_mAkSubikIrZZZJ-__qGKcoQiAwfgExWFlalZJgIqN585JH84dil2ZLcxXPklQbpEbTBzktRL5w0JUWpdl8mdZ26hRtUcz4WJ4L_bximfnWtEHVogo-x4DfT3y0xtbaRXTLY5K9kZWb4SdrV2n0U3wffH4XMmFyOb4xddxu52-4-k4sWC2tRg2ySuUeJb66nHDYO3a5um5s7N7yt1DgDOp3QM81gg8knslyBil9krCeRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=umw9yRPirpgz6-GIHZMMOIFAAKvrfw4pAqwPPNwkLxZmb6TJxsUTtTCSYsuZJpA9ZB_gvyaSInaqhri5R7YyFczTYi_alPmm5FMgBJQszAPgrI-TGdjBDRwk4NFWbusj9eZYMGNbpzCnEyP1cbp2eUF8OC8vA3f4J7gDL0lyPAHPFQBZcpwRGXen6ui9sBSZZvm0nrV0NRrxnEqlaHs9FIWncpzpTcigbRfa9DcpDH1svvgCbRftlI3pBTJc25mKpRJC65VWNoTlo8tANHAButrUZ69fw7I9JVSX5NGjM7GEOT54U_Nb2cW2QsZwI-jTu4mNZxI6pIkEqkHBr39m-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=umw9yRPirpgz6-GIHZMMOIFAAKvrfw4pAqwPPNwkLxZmb6TJxsUTtTCSYsuZJpA9ZB_gvyaSInaqhri5R7YyFczTYi_alPmm5FMgBJQszAPgrI-TGdjBDRwk4NFWbusj9eZYMGNbpzCnEyP1cbp2eUF8OC8vA3f4J7gDL0lyPAHPFQBZcpwRGXen6ui9sBSZZvm0nrV0NRrxnEqlaHs9FIWncpzpTcigbRfa9DcpDH1svvgCbRftlI3pBTJc25mKpRJC65VWNoTlo8tANHAButrUZ69fw7I9JVSX5NGjM7GEOT54U_Nb2cW2QsZwI-jTu4mNZxI6pIkEqkHBr39m-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMPVyzEe4lsVbNIAKjyulsQPYCUg0NxVCqrjtgJXpDUv6resZeqs2eFEdDoqcbFMyfkQ6ISGz203lFPLRFtHyCrPc0L64tZgulqMAfaBlrSI0QzoLNqJ8fG1ahmfrasV5c01WkThkvDfkBCqsQHbWhGNkKaMwPVwh63S2pzXgSGp3mgwizgqFWck_HxXMST5IBuZ6pB5pSHPQa02hSNmzuYVMog3zqDGnhRhyDSAk9CKXx-tL4Pg5Txeriz8NvQ1nCULgF1tEPMrFpMcIQaMfAKnrtjts_P5lIuX7pEh5U1UOI683YP3Eh3JbDdpekX0_6o4o6CbPdN-sWxJvoTLSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=oIRkYAwmHoDjcgj4-D51qedShk7cG7dpMVM1VdQvDy4VxOrKl2OIPgq5mVt1CEN7AXyXWPEdFTt1iiU2iaf0w7EThJS21qqe3qtkYE3C1CaXoZOTS7Pr76i27_u7bVFixMsF-PGcfRVaxX5laT5Imps7LKLFYue_2PDS3xp59IAImYxqkOk9UefxGG2CT2GOKKUMP1K5zFk0Wlc6WwemxM8AHjvcY1TrghcOKUGyx16sqs-wGwZyq4dGFvyvSFHfchRZ7iKXvgQs5tp4PkuwfEgrH8kA5gLNJjlFhykOB_4-tsfS_NJyeylVtc6nwhl8Hv_dzDrXsz-VJB5OZ0KWIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=oIRkYAwmHoDjcgj4-D51qedShk7cG7dpMVM1VdQvDy4VxOrKl2OIPgq5mVt1CEN7AXyXWPEdFTt1iiU2iaf0w7EThJS21qqe3qtkYE3C1CaXoZOTS7Pr76i27_u7bVFixMsF-PGcfRVaxX5laT5Imps7LKLFYue_2PDS3xp59IAImYxqkOk9UefxGG2CT2GOKKUMP1K5zFk0Wlc6WwemxM8AHjvcY1TrghcOKUGyx16sqs-wGwZyq4dGFvyvSFHfchRZ7iKXvgQs5tp4PkuwfEgrH8kA5gLNJjlFhykOB_4-tsfS_NJyeylVtc6nwhl8Hv_dzDrXsz-VJB5OZ0KWIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmkmAXFv-ENTA832i0FelbJAuxZM866OCTr73leoys9GpT4crfOlTLrsX9p5t1H7aYkMjmF3e_mu2CpGEBh7JQev1Djwwaake0vOpksaUIJA8NiqOZhXSirgp7V3gJM5VjZ99x3oyUbCGnZJjWqf5o9CtpT27enO57mfA_eG-rjSudl6bcZm4rexwTLR0XRLsgv6YGOHnF02CWXNrVoEo1IxAnWavYkpv3WPtsHRR7h5tA9tbUUbvLVmEURt1wWcDNH1M6s1ubakYk9Qt3LX7j_WD5chNQxqUhi-TgO2ELf1QypTiAinF6DkQyrXsrhOHvCj0m1H_wRnW_oOruJHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkNCFo-uMWUTptDf8-KwIZ5YDUD0sLwAN-MWOPo9DOcRuyyZFRRbABkKEODI6VM-skWjczGtVn_adMntnfPGokwKLuQ00MEFI8RzlJ7jd6qLamtf8E6poWvWyNs4e5ovysdgBJLbT6yP_coiH9JBeZKQoktLM25aQVUDCYK97FkZJ2vFxvd8hCUWQ0Gl2YCSWyCzoGhuG5UwNM8dDPy-It59VIy9e53QQNeKHjEC4HfzD390-ftkmzo76u0W-QLpJKXHtD1wumDHzkLboFEejmclV7xtnVpzT4anHrC_okQ054i3F7D1BvWmFnk3dkiLG68jyOLipJs_qdp9-zaxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=bSKFP4ikcn21EcGPs1Ask7nDAJA4beKACGFq40_0-5EXKW16LzaxUgZMNJHBg-1_q3B_oMAAVckuzHhCavJ6aSEA6muMQvareWS64z3I6w0cbrJWyCFXEHF20FuOFRp1VbBwTHTAmOMhWl_EsFOsCgdOoCHHylLwnZzw_D2IxFasvr4-09e3OVxl5Q9I3MYvLA1gwXkUbdBM5gAo0tVpimYjK9OqkLUnf3wLoDln3S5iEdE3eaDvUT1wQ-jPZObha0fNHG2MtZ0KTGBbTrJkXfhDPJ5AGHsrfAClic24TLJ9RWywZeGVYdj33GZgHYvNXto_gHI0Q9WwUXnM_AVvag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=bSKFP4ikcn21EcGPs1Ask7nDAJA4beKACGFq40_0-5EXKW16LzaxUgZMNJHBg-1_q3B_oMAAVckuzHhCavJ6aSEA6muMQvareWS64z3I6w0cbrJWyCFXEHF20FuOFRp1VbBwTHTAmOMhWl_EsFOsCgdOoCHHylLwnZzw_D2IxFasvr4-09e3OVxl5Q9I3MYvLA1gwXkUbdBM5gAo0tVpimYjK9OqkLUnf3wLoDln3S5iEdE3eaDvUT1wQ-jPZObha0fNHG2MtZ0KTGBbTrJkXfhDPJ5AGHsrfAClic24TLJ9RWywZeGVYdj33GZgHYvNXto_gHI0Q9WwUXnM_AVvag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=ZWJ8BrBDVLiFkEXaUGi6jRYXwntAAxo2pJGCioWENr8IxW_Mop2BZrm6dw-SgZmN2Y6_4Wlgow_KcBc8d2FTqXiFD435Sh0JYoKSoWNoSfDaMIltnpSIDR7CDH5TQ6TNgeNSvAgoZOiJRlWnKnfjLfZVtCyVPHSnndMaHVtKbIe8qaSWeqvBTj7kMtWACUCtU985wgN13XWsgjLtOyY3E4CC_DNDWXID-2lDMka2zB9YuZwrjCtXWdJiU-H1lpTELv8bv9IEHHjAojWsBUXlcPe7GGeMEigvfEuzrcvSsPk8UUjDTAvFoolovjiVbNa24ErqS3Klcmh4Ia9s7su_Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=ZWJ8BrBDVLiFkEXaUGi6jRYXwntAAxo2pJGCioWENr8IxW_Mop2BZrm6dw-SgZmN2Y6_4Wlgow_KcBc8d2FTqXiFD435Sh0JYoKSoWNoSfDaMIltnpSIDR7CDH5TQ6TNgeNSvAgoZOiJRlWnKnfjLfZVtCyVPHSnndMaHVtKbIe8qaSWeqvBTj7kMtWACUCtU985wgN13XWsgjLtOyY3E4CC_DNDWXID-2lDMka2zB9YuZwrjCtXWdJiU-H1lpTELv8bv9IEHHjAojWsBUXlcPe7GGeMEigvfEuzrcvSsPk8UUjDTAvFoolovjiVbNa24ErqS3Klcmh4Ia9s7su_Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=KWLEJMii18U0rGEouqWPq2Whw1yfskgv01_aXGAVpKtJ0FsBxAisHYPbSq9kx57_32QXlZNJ0ZNc9pYKx2EbPd6Cy51kpFaMwazxzTIH5t5KQAJRVW6kCQIfslsK8C5xQsnFJE8KWteWjMmmCIm1FWMKQ-_BQGXSgRy55HtG3Q-AKm44oGLIkoI6GSZ-xC8x1kZIGwYyLnm3vSAoukDG5oEkQ_W88XMDIXdrH2h6-fFlNJI1-Y_DNbp4O1hxqIGQQ0IHKRtYAoAufsrNZXTBW43UPT6-mfkGd7bvybhqeUEH5IMuSRlHi9p4vti1nhJEwHJH_3248YnVQZ0ma1GJug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=KWLEJMii18U0rGEouqWPq2Whw1yfskgv01_aXGAVpKtJ0FsBxAisHYPbSq9kx57_32QXlZNJ0ZNc9pYKx2EbPd6Cy51kpFaMwazxzTIH5t5KQAJRVW6kCQIfslsK8C5xQsnFJE8KWteWjMmmCIm1FWMKQ-_BQGXSgRy55HtG3Q-AKm44oGLIkoI6GSZ-xC8x1kZIGwYyLnm3vSAoukDG5oEkQ_W88XMDIXdrH2h6-fFlNJI1-Y_DNbp4O1hxqIGQQ0IHKRtYAoAufsrNZXTBW43UPT6-mfkGd7bvybhqeUEH5IMuSRlHi9p4vti1nhJEwHJH_3248YnVQZ0ma1GJug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaV6d85fYvaG27tMCdzQpahpUav_Gkn0iU1jMMVT1XhlD6FC-Qlasvtp183dI4DfgRTq-8gtLnvKS07oD43C1h2eFvqVBpeKjI__7H316261iszKjGcSZVEId4nZfKAcLTMQylNg9URacBFRCXUTRnZxQFe3Afu0khDZV3HMeXRJJAO2ZqykLTlTQQpB1_b0NAM0OUYFYLxaUp2HyLkkTBaJ8klTwCaTRPyAIi6LH2YGTgcGCpwJOn9dq63NeQVSpKXC1oPPh6pugUlXrcJvEizLTNrxN6_D9KNVUyewzbz_rmENjCQYECKagwDjon1jmaS8WYLYNmEftg5VVpdX3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=EEAXqdoTi7MDdK2WfjDhGXo7i611Dn_y-g-pA7unQ3bXVEvHSaC_8ijnmQxgJC2EyalPtergyi0_vtWcvnG-AOVcw8NAUnd0Px8au8kjG5aBWyxM5xF8H4eg7MEtG2-UZGyFmMs-CS9SMWdxNxnVLA5qqGgz-qZwmGX6gojCiVxiDwadtC0nftlBtKijuZ8UQK7io_Hh9Ympi4b4Lvep6NvgwkfOTN1iR7DDsQs8DQHrhtgHw2fsLuIvYMZCX-IM6UJLfCN88huE1iTE4mLVyKcr4KvuI-Z_0IiAg-VwHTztdXEMe06to3xKXDiU6xjnRryIoluPWKVdehBdipLpcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=EEAXqdoTi7MDdK2WfjDhGXo7i611Dn_y-g-pA7unQ3bXVEvHSaC_8ijnmQxgJC2EyalPtergyi0_vtWcvnG-AOVcw8NAUnd0Px8au8kjG5aBWyxM5xF8H4eg7MEtG2-UZGyFmMs-CS9SMWdxNxnVLA5qqGgz-qZwmGX6gojCiVxiDwadtC0nftlBtKijuZ8UQK7io_Hh9Ympi4b4Lvep6NvgwkfOTN1iR7DDsQs8DQHrhtgHw2fsLuIvYMZCX-IM6UJLfCN88huE1iTE4mLVyKcr4KvuI-Z_0IiAg-VwHTztdXEMe06to3xKXDiU6xjnRryIoluPWKVdehBdipLpcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=OIpZtkhJ0dAGvQnUwV2vmyCPQQK1fl7KsvQ4Pajk6ZVLxnWqHoptWgvxMfjm4fhKdWKHUXP6p01lSP8uiVO31QlxPMe3Jyst0rKtawqZldSD-PXhmNVRkwb6QEzKhvgrHP0-kxTi4U2gxR466XO9vEPY8t3ML0x9ocKmLK_5qzulXKF6wb7EXCO_N5gZmUmPikD2tedvzX5sFBKxCXfzLXOswOitr5cJBHRSRSKPUklu3KXvFzsdh99GujUVdKOWg-j6h4gt8eBzbf4W0416DhckyDHO-HpF6aX6T2FRhFUZMp4RnYAoKDi_3lepAtKMRVSVaokQTT365UVa4AECFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=OIpZtkhJ0dAGvQnUwV2vmyCPQQK1fl7KsvQ4Pajk6ZVLxnWqHoptWgvxMfjm4fhKdWKHUXP6p01lSP8uiVO31QlxPMe3Jyst0rKtawqZldSD-PXhmNVRkwb6QEzKhvgrHP0-kxTi4U2gxR466XO9vEPY8t3ML0x9ocKmLK_5qzulXKF6wb7EXCO_N5gZmUmPikD2tedvzX5sFBKxCXfzLXOswOitr5cJBHRSRSKPUklu3KXvFzsdh99GujUVdKOWg-j6h4gt8eBzbf4W0416DhckyDHO-HpF6aX6T2FRhFUZMp4RnYAoKDi_3lepAtKMRVSVaokQTT365UVa4AECFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=g2e3pV_97MnnokL4ShY9qdAPqHLKB5qeVW5A1j-PYIjc1stEAHi4hMqGtabig1zbgqJFvurc_m4-Hy6WgYm9JhIu_FcBmSmSSC-tmNMzI-BvbZAGxmBvxfVySWWMIJooKpRM0w-vagtluvMjwG2KCC6o2yk5RapUHrg5cnwdl0iVQ06JuvMj7mIPLhRj7RpNtHKOyAaKYGi1zoR5AkSdR-yYIvhUJjxtjAwaWaUeyHAPlfhpUFrE6AY7r6-x5f6xgCYzqGIU9LhCier3BVQ8KGpH7VNpI7km7guLky__hCFA4EkdpjA-YCFihboI4ZSxfYQA_Sclz38dE92TzpqIjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=g2e3pV_97MnnokL4ShY9qdAPqHLKB5qeVW5A1j-PYIjc1stEAHi4hMqGtabig1zbgqJFvurc_m4-Hy6WgYm9JhIu_FcBmSmSSC-tmNMzI-BvbZAGxmBvxfVySWWMIJooKpRM0w-vagtluvMjwG2KCC6o2yk5RapUHrg5cnwdl0iVQ06JuvMj7mIPLhRj7RpNtHKOyAaKYGi1zoR5AkSdR-yYIvhUJjxtjAwaWaUeyHAPlfhpUFrE6AY7r6-x5f6xgCYzqGIU9LhCier3BVQ8KGpH7VNpI7km7guLky__hCFA4EkdpjA-YCFihboI4ZSxfYQA_Sclz38dE92TzpqIjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB4PmulUqoq6OJDn9Ymm2XoNMfwY7eZvTbjwS5relDx0u12q3NNxY_0XXz3IQdGmRGqWS-4s9VDXb8aZ-Uz--1qoEOgIszPo-d53uN3rtoeaafdF1CbaY7Vq9AVO7U0luLL1Az0jDgAmkPtvLUmTL7Sl96zAbTQyvbzRyATDt_DWgvZkUYTwYLy5kWPSpET-p_ky3sZlWAzV-3wJJm3b1Sba-bhN6Afq3LECJusPhlkAs0xve-vXshzovQmhS70dCt8L_WRZebAp7oLIimNUvf7Q5l6B1rgAHwnOzOw18J8U7kjs4opSPtCmnFGcHVzERsV7clSmlkxRQbjaHNGB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=nTCN4YRDeoTvi9JnRlzp7ZOI99h8Ka677ad8ChoFYpPTP7Pv0U2OZvSUik0o6AjKD9fE4MnIeDa3wO9DkkQ9DToLjXD2NI68GUDo64pSUFNhJzvSCZsrbYl6ekSoFbhuwPPFY5qTMODuo-BUiDepNFEqBQmCehGvUsczaDoIPLJ3oGL7OIcxTGd1kZt8zkRtozWU1oD_7hggyJQbNG7bPiE9t16RoxjbO9OqmSXaOHwPRxq-ntdBYP0wjnsyuqs2Lt8ji2sOyFutKhEX8hw-CJJneWvfaAqeXyBqj8HYG8qhw2aLshsfz5RwTdTR8ylHKJaJaqm7pKmOMskARvYTow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=nTCN4YRDeoTvi9JnRlzp7ZOI99h8Ka677ad8ChoFYpPTP7Pv0U2OZvSUik0o6AjKD9fE4MnIeDa3wO9DkkQ9DToLjXD2NI68GUDo64pSUFNhJzvSCZsrbYl6ekSoFbhuwPPFY5qTMODuo-BUiDepNFEqBQmCehGvUsczaDoIPLJ3oGL7OIcxTGd1kZt8zkRtozWU1oD_7hggyJQbNG7bPiE9t16RoxjbO9OqmSXaOHwPRxq-ntdBYP0wjnsyuqs2Lt8ji2sOyFutKhEX8hw-CJJneWvfaAqeXyBqj8HYG8qhw2aLshsfz5RwTdTR8ylHKJaJaqm7pKmOMskARvYTow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0RNjHi99inRIkdnFKsvISUoMd6EgleAQMdfX6CXA0ZMxUghiIy9XKxe9Ql-UbX2yd2WLMBOlpYNCH49u7_nZUYLT1VVDuM3m6djgwrE3g4hhExehEvujJmi8qEbpLaxzjZ0QdAi4EDjsgoUpU9tE-VaRi7T5PnR8NImNuZVx-fc4RIR__tATUuvp5fHiRq6wS6uCI3kJbbxSTCNePctaoat10XnpyIRPSDOJHoCOnpz-z48WJf11I3Zjht9Caium1WWJPp2XvM0jAuhEOPvTqdpOyMdWODhwTLag5hh1T9AXMZvfSG-364vwCh3RVOVEjoA2YajTcwSlo_NX597RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=ot4IbOSOB4s8q_9FZNGE4v7Zle6CkMdN__JOQ_ODLLoOhyxfgNTkT0RHQju8Xkdc15Wn-1Pjnvfh_DL9Zyk_E12OCQAUvLiyQI1QtFzRpZpXYV7KriS1LD2-S3ZUvSIPS7ueQHTHUfTFmGpDn3_6AQtswadHh4J4jv1cK33faCYvsIIDtK7b-Wr400ouX57y0NtFDGuvl8Vaq8LJnNIxZUYLSciPcejVFelsX8tTLhuOk7xjBzZB9DpLNij8fvFiLi1fi_65FFrD8b5V5TuRYPNAtYqD7YWnflRXLzrdrl8LdV2xg_IZ0pfFNXXnqYw-wuBMSTRS2SWQVic_XYq0IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=ot4IbOSOB4s8q_9FZNGE4v7Zle6CkMdN__JOQ_ODLLoOhyxfgNTkT0RHQju8Xkdc15Wn-1Pjnvfh_DL9Zyk_E12OCQAUvLiyQI1QtFzRpZpXYV7KriS1LD2-S3ZUvSIPS7ueQHTHUfTFmGpDn3_6AQtswadHh4J4jv1cK33faCYvsIIDtK7b-Wr400ouX57y0NtFDGuvl8Vaq8LJnNIxZUYLSciPcejVFelsX8tTLhuOk7xjBzZB9DpLNij8fvFiLi1fi_65FFrD8b5V5TuRYPNAtYqD7YWnflRXLzrdrl8LdV2xg_IZ0pfFNXXnqYw-wuBMSTRS2SWQVic_XYq0IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRKzFq8dqvrINilyc5P_aHZlJ2mILmPzpvtMaOJv1TMOgy5X2VDr99y_m0O3-kHqW0uku4qj3jJj4_-vdyp9X4oHMalSmW1gJxd4DWSXb1RnHKVTTijvLbZd-2REJHgZP7zolz3-e-kRQzEnHQW2bGLPPz0LSCiNDCo3FAiXs2pUDcB4UjaNFMwB3xavhVJh1h8QS7Ja46-NOGaFT5I8aQDL3LhmtBDg_YVB_K9DNNLAy3EAraHyxOneU46O6c_-19dIfsXpyuhUvzQRbn0BgeCoulX_SUNGFnlqx1bM856xkX64AtWJ2A9FBUR4LcBki8oNdSNAZMhyi_VX-zl2QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=eycwL0lG-ljOmZ18DEFGNDoOUI_b0VHu7dpwPWiTAx4o3d2a8jB034jHOjRZYPx_Qwnvwdq2aXVea11ZcHpZibMJqi4gcb835tpZPQvbQ_rzTrTjJ9E6IJgdZ0_3ex9HrEw-V2pPj4gePcXQa06haVklBm2VH0j8GDpl_gDGYK0etOufkxiJoWE05Vm3ZwLmkQ3OEU_qNL27crvS2jO5--j3cVbcz7oqWwa2qUFfWur1PWwlyiBs9OnwtBjujX1a8l4o0rCh4tbhms4H2myRd2IqGn-7OCJg4tuzg57gN229rEpSlru5pbGt2NVBcyksuB-P3TBqV7GhTn68l0hOEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=eycwL0lG-ljOmZ18DEFGNDoOUI_b0VHu7dpwPWiTAx4o3d2a8jB034jHOjRZYPx_Qwnvwdq2aXVea11ZcHpZibMJqi4gcb835tpZPQvbQ_rzTrTjJ9E6IJgdZ0_3ex9HrEw-V2pPj4gePcXQa06haVklBm2VH0j8GDpl_gDGYK0etOufkxiJoWE05Vm3ZwLmkQ3OEU_qNL27crvS2jO5--j3cVbcz7oqWwa2qUFfWur1PWwlyiBs9OnwtBjujX1a8l4o0rCh4tbhms4H2myRd2IqGn-7OCJg4tuzg57gN229rEpSlru5pbGt2NVBcyksuB-P3TBqV7GhTn68l0hOEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nG7wVMgSrSN3rNHSX5Wi9YJCmptSVmq2aj9XFx9yqXaCwnyzZrn02DuET4pNZai_BSdXDFrKnrJVpfRb96cybquzp8hpRum_bxuc_i1CR7OffMTUrQk1InV0MaBsUE1LDxatWldC56XyG_ZaauObx0iNpah914h6wtY9SyKWZIkT9oSmNeZtx6EHj_ihKiO3tM8P8Ya7nrTGJ9nk-s4PTJrXKM97ascbBSAwb-VUXXXAtTomzOIDRp78xMPVJG2T29pVmO9HzXUzMos_E93YV_40MyO8ngVMyv5GGYlOPKIH2lrqJvx8hSRWAooZXuXXYd3L-6KlyjDEeKQfkdWJ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MhIgEM9H2wNaajgrnutPMaiHNyRyEYpov67lhs6gP33kqBxRrJrFThYszJeqG1y5XW5JXy9fpWQIdrKTrsu1HD7Ke2tlFOEgzoeSj2hIxmIfKcsaMS8q5xMNrmvm-sFY5aoYEkIWAmkIBDFRk9m79xeB9WsUkunA8PKCT6cks_urAD96qKpUtB6NMcyeE28zK5apBPitDiz1YRQRXvyf5jajnlgb64HF4t3ymLtU2pM1WsWVp1N2IIqlPm-AkI6KQTSYSrIp0D-xEIHiLtuVSFVoEILPL31-BPx6L61GAW5n1Onwi_0ZC_WzoZosLQoQd04fDr4FtGE2KgYJrlq9ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=rxiOQppPxRFD-QPkGGhluiM8UGttNj4483W9jSgfnbPEGYjlO0gl4sUf9mgUgtFGyBGPStEHnn4wISlyG-5d-KV-a-PvhURe8n-O-sr2mz6SrE63l5kg2nhbYaiqt1QfLMYWLB4eK30hBxaHptT0hHLqi6C2DmSIoyo_ZmCiAh59UfzZnGBloRyPYPRGl6dfw7SVSe_RLkAvzNFQEyXyxWfav0P597OldfvV_uk4AeQhdgdvdEilnH4RSplV9Dojx36s-5edS3GT05fNKjaNhE0aLhEtb05DKkmlvnBF41alUK0r4o3mNMaOb_mQlY1AyhKO7Q0o16hqK-GZ54yMTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=rxiOQppPxRFD-QPkGGhluiM8UGttNj4483W9jSgfnbPEGYjlO0gl4sUf9mgUgtFGyBGPStEHnn4wISlyG-5d-KV-a-PvhURe8n-O-sr2mz6SrE63l5kg2nhbYaiqt1QfLMYWLB4eK30hBxaHptT0hHLqi6C2DmSIoyo_ZmCiAh59UfzZnGBloRyPYPRGl6dfw7SVSe_RLkAvzNFQEyXyxWfav0P597OldfvV_uk4AeQhdgdvdEilnH4RSplV9Dojx36s-5edS3GT05fNKjaNhE0aLhEtb05DKkmlvnBF41alUK0r4o3mNMaOb_mQlY1AyhKO7Q0o16hqK-GZ54yMTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFk3ou9SONjxydg-KjygcZ-OPiidohdlsjCOLu_NPxkpN2--Jb4eh38ZxNXLuTgoTAJwFqaiUjoRFE-eFXJLmBXNCkmQaptNbjRy4DlA9IN67YzFjVcMvV9pU6aEjUD7S4DCUNWa2Rjr3Q0Bl--HUAVIsI58GrFImwOSD_m22ynKwxAINp6opQZiRZM-PxQpP0M-w4jXjZl4fxi54v2czxTYNZ-sJ9f0RgNciAcBgJKUkRWMsTwuMyOnBvWhbzUJPui1V10IbIQP1RzIK81lQC0f1Ib6gbyEYo4wPhEN2VnkjTlmSH1qDBsJpJcKyQdJuWdUQIy0hwGEWyzB1ahUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZuu2k7VDby5Fgm1p8TwllaroR42iTkIc9Bmw9ne7EP_tuqZIWst0YkqbkX3WwfecGonqpPQo1QLKY6N5jJ6aiL_fwgiLYA0HJSDdTE79PjpIRn_v95hgdOfpf0fNsbXZs4ONVkbuW-NxQI7-PgMGCWee3smviDA9ZHM6xwUIrDTBAdNP8_34F4nYQVouhMHPDUmJzzh-YnZPbRlvIngf9miVkUb6TZD8smtcrvCiQ_igQr9gRkW3A4QJb39jwOypWd-7gizHAjrbgwgGSeO4RBVIP89vpYCSG24DX_5g4QXegwq_PCi5-Qt6ciTTwhIgDNkx0ICHKIrK5KTosDIsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRqbsydzB0apwxCAp0T_caKbH91iGuWkZukZlJ2O1dbK02QtswVdbqpexOGQV-wDZEm_No6DX0xhWlrvXCHT9ZX1jEvPlZG4HwtRqwmLp4ZtOBnFsrsWWjUhYaCvQiMykR2n03zE48lRaYIqlvgJ4mNKQ4KdoRKEHUOGpwwn9S8bLFF2x9calVn9r9o6nW_fHE63Zb9-Y32NtDClWZE2N6lJBj14CTL9wFhpXBPPL0A3pzEiHVwuIyg0NHwB-NoL1vNIyjxpTAGZS3RVwKjjhr_5uivoAvIlLcmA2S_BN4zwQ50JyxdH34zstHwBWGP5au0uXvuolyB9_tyR8TqUbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTqWGlkMUdDlSMF2G7pL-ecRHb0ESXHXAOxKh4-APg-Ni90rZ40Zo4yfJRvDVyzELaCJKcA2Cs82UIbD42HzhlAIDebRW1FeGF6d2sz4Yxyn-TCWeJxjpndn04zrl5rT3rkNPAjmDkpN3LHaTRDuqxGZD_a_uZAFLa-gc4aUW9BTfcuQ_vyVdH9xsZBBbf1K0zmM5_YXiLXUZXorPI4ncpDiw8ewnU9fkQ6i-phO2ITmiRpmJ7RWwK2zxeb6FcswhuY4Ly72sd8ChRNrxXA4AloKqZKjOfaxVOgmXaya4soZgZoPK44aWoVFcqkr7AXbzXYtso6gMRb3XARr8EPnfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCaXDMJXNBW8NKgvtb0-Coq5Dt74NfF4QbtB1n5c6PyPsdwsdY5GEdwU9DvF-X-1znpU60A8Olb_tBhjC5RyWgcekHqVBcLShHiFC7Y9WtJfeUhFeBIql1LolGLuRpoVwQ_NFaRkjLhi12fBeMXIwxab5SCcoB0daLY92rFfDaleV3dDKu-WSprzj0LsuPhUvIRCsmWIJio1wgSsNW55tZgV-3uBpjLvqbhr_j_yhsXs_IEIWi56L0Fi_z3gjR8mPnYeF-dgc6LUeQVWzbZneOt_ujKoQyAawm6F0fWP9PTWaLy33w5z2e5jP3DSmcoNAPaOqpNA9pHy0JFQ8vLRiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=mNjRwcKZ0qQ5LYch-PnkwtSbCUGIjKIBfp5WSHNhFQZJ4HmCQel714g3J-7uW3pTYPcZBWOZxViWAp7_FxUG0bgOktNwHGZe22qHY9NqfnXPPtre6TkQ46m9zVHlp8NK0guhXdC77C4ziq342A7ll5PBs46tSX72irvLC_W4hypD8f01O6BWw4PxngoD6TVwbqa_eZ9ySP5_-sG3SSP9nrvucHcbsFKHRHNC2mWWz1UJv4qGwSPaCOlvSWtQt0ASNrG9785srFYuHJWzWFmO94JUd1rFCs2jbsw-cP__Q_TU8LFn0zDrzdnlt3MTZvGVO_AePfwxVyFcjgY3CbGvuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=mNjRwcKZ0qQ5LYch-PnkwtSbCUGIjKIBfp5WSHNhFQZJ4HmCQel714g3J-7uW3pTYPcZBWOZxViWAp7_FxUG0bgOktNwHGZe22qHY9NqfnXPPtre6TkQ46m9zVHlp8NK0guhXdC77C4ziq342A7ll5PBs46tSX72irvLC_W4hypD8f01O6BWw4PxngoD6TVwbqa_eZ9ySP5_-sG3SSP9nrvucHcbsFKHRHNC2mWWz1UJv4qGwSPaCOlvSWtQt0ASNrG9785srFYuHJWzWFmO94JUd1rFCs2jbsw-cP__Q_TU8LFn0zDrzdnlt3MTZvGVO_AePfwxVyFcjgY3CbGvuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=Gj1eMcmuIlBf2JsktGLhpSFMM7MqWo4i2k5ABYUxXUbqvv0l049H_gr0EontbY21fWBJnJj7BCPoJJzgWb8LW9nsf9gMH6xNOPYfFQxouJWK7ASm3J0AkWfgFenVxAzjOVxeknLYaazgtLtHJCutbH3_ReQDORNosxmsA27zG1sSZRo4Y9geH-i6pc126C7eCk1XInwdgR2F9hVn_4FKH9rpKP10SPP9hGAHLswUT7DlbHFRpuDoExOTBXcArEYgtcjpyslgY5I6S1po7ENNh7Ih6ZfxXq8QHyJCLhJMqBav3MhVZO1TfuTEZ5EwphDaWJJ9A9-ovPd-9uusxAZsWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=Gj1eMcmuIlBf2JsktGLhpSFMM7MqWo4i2k5ABYUxXUbqvv0l049H_gr0EontbY21fWBJnJj7BCPoJJzgWb8LW9nsf9gMH6xNOPYfFQxouJWK7ASm3J0AkWfgFenVxAzjOVxeknLYaazgtLtHJCutbH3_ReQDORNosxmsA27zG1sSZRo4Y9geH-i6pc126C7eCk1XInwdgR2F9hVn_4FKH9rpKP10SPP9hGAHLswUT7DlbHFRpuDoExOTBXcArEYgtcjpyslgY5I6S1po7ENNh7Ih6ZfxXq8QHyJCLhJMqBav3MhVZO1TfuTEZ5EwphDaWJJ9A9-ovPd-9uusxAZsWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=fBSnEZiHafN8x17x3P-IdEtJcOmDxraEhwF12hoP8ucXZGS35UAchLsa7lwd068dlkv5cMM6Ydi42QFLeXATBwEC-SDZQEW-uSJBW4ekm0cGocO2eWwajfHk7DCuBbwhd9x0WO0GBMymNZ-qojxqwZ2YBPAdCv5ldRJLvh51IY87DVPvibApNzbbC-aeetesld4L8ZxMzuisD5yLY04UB7FDkLjSrClbB0m0NzsRsHG30D2616qtsPy-gH19FniUJ14a008VCUmpmHcbO0OgZjtI_oV_0Z04q3wLdiUuYpe0USkfixl6H8EM_dffpbuBIxbFseeBnLXWpX-sLfiwYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=fBSnEZiHafN8x17x3P-IdEtJcOmDxraEhwF12hoP8ucXZGS35UAchLsa7lwd068dlkv5cMM6Ydi42QFLeXATBwEC-SDZQEW-uSJBW4ekm0cGocO2eWwajfHk7DCuBbwhd9x0WO0GBMymNZ-qojxqwZ2YBPAdCv5ldRJLvh51IY87DVPvibApNzbbC-aeetesld4L8ZxMzuisD5yLY04UB7FDkLjSrClbB0m0NzsRsHG30D2616qtsPy-gH19FniUJ14a008VCUmpmHcbO0OgZjtI_oV_0Z04q3wLdiUuYpe0USkfixl6H8EM_dffpbuBIxbFseeBnLXWpX-sLfiwYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=qbV8TsnXPjVXLMmOBeJNIpDp1f9CctTyvCslpMTB_zClnsIqSQZtgzezuOw5MPjfdsz_vo2F_iT1OM1p1dAMDPrn5xW9iq3Kry04fdSQhxpt8YKY68ck3sbVmQI9MxW_GY_RiWHEmKsLorK6YeqTtd_15AZ-WJBW1F894Hn1Tw9W6ubOlnYlI72x3VkN_C4M24s6cRM63WPGXdw-BhXv792V54QYhMvAC-I8NnGvZRMHwybDxsnllsqmT8qwfVvvYD5nRzNtdR7zszea6IKkrpYpxvaliOHfnS1jSVfSLkkZ7IYtIJCX_Zez5ijgDEo1_YbnP_baAMKxXUvJiV8f6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=qbV8TsnXPjVXLMmOBeJNIpDp1f9CctTyvCslpMTB_zClnsIqSQZtgzezuOw5MPjfdsz_vo2F_iT1OM1p1dAMDPrn5xW9iq3Kry04fdSQhxpt8YKY68ck3sbVmQI9MxW_GY_RiWHEmKsLorK6YeqTtd_15AZ-WJBW1F894Hn1Tw9W6ubOlnYlI72x3VkN_C4M24s6cRM63WPGXdw-BhXv792V54QYhMvAC-I8NnGvZRMHwybDxsnllsqmT8qwfVvvYD5nRzNtdR7zszea6IKkrpYpxvaliOHfnS1jSVfSLkkZ7IYtIJCX_Zez5ijgDEo1_YbnP_baAMKxXUvJiV8f6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8Qsq7QxYkNKsLuX3QLfJlpTSXDRisrOEPstwdYcpZv7fUCoEkZz8CUhEcqv72qfSJQuV-T1n2P71L6BALPB9A74ENCMSmx8NDMX1bQGrx9JQSLsodkEu_ox8APkainM5GrSTBsEFjLtmskF0aw_EUkm_z0LbFM4D2LoCvxyLM68-hsHLPNEv8HcUYS1S_P4do5EhPuk4awvRe2-0zNvh7kZ6fCoSIu2YmJV3gmAjJWinZSKrj6nvH5_JHnbrOUqQUXIBsb2KCJzQl489ebSutG9fN6nPJh4VLAxi0_4eTmSibekEGzB-8fG5EmU1t57-Ze8rOljNtcKm4Bs_2wulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXW5Am_H7lTJ-cL2IWGOWDCknLX_HnQmeQtOkLP7GPgUg32rDY1T25ohbzqDz_KnG6MyCiLQmY6VhR5U7QgPSrC7s8YDSqkmxMU5iN3j85fDg9YEhy_I62jlQFJHMmGOWZTEvrzHojtPn9cH4cyCFUj1GHD-M3KJH9Y2QaZz3Rdy0I4QkfTf_CJd20Z7Ex6gHVeV0gup7jllNDBsDpAfQ_mTb5ZFcSDS9RIgq0DRA5Sv-TAEndGgl1t0S73Su4AFPwG1wfZYb2qxpJCk2bU7LX3zZlJ_YsHyPjmjrhPqm_KpYqlRSDGgTiiyT_PnUMtagJrmzG3Xw1T6vO9oGjARfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=CYBgWeYqf_HJ4ll5KF8Lc5wqZhlkogv4c057gzj_emww27BrP_wqaPTC2apluRlb21WmM3vcXK1H7F0unS-op68gmu_P7yF7OsuFhO_rTtf70cIchUD0FhoRXzZHK6CwQoQ9nuoAYL0I6pasSpBvV33LD59sMbZ786VXlSs9iq4IjOwFTjJuXhUB0pFtqOjRwQSlWhJYDH26mkMhFtqTpVzmjrQO8l4Kz7wLuAuoQcSFSJCUinmXb4PqKpET-cNY82MZU_yyh4MQ3gF4c-8n8WvB0oG-7hdwz--zB0sauDE0hvOjdnJjUckVZ50XNd3U3g0If6UvIsTEJO0LRQjEyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=CYBgWeYqf_HJ4ll5KF8Lc5wqZhlkogv4c057gzj_emww27BrP_wqaPTC2apluRlb21WmM3vcXK1H7F0unS-op68gmu_P7yF7OsuFhO_rTtf70cIchUD0FhoRXzZHK6CwQoQ9nuoAYL0I6pasSpBvV33LD59sMbZ786VXlSs9iq4IjOwFTjJuXhUB0pFtqOjRwQSlWhJYDH26mkMhFtqTpVzmjrQO8l4Kz7wLuAuoQcSFSJCUinmXb4PqKpET-cNY82MZU_yyh4MQ3gF4c-8n8WvB0oG-7hdwz--zB0sauDE0hvOjdnJjUckVZ50XNd3U3g0If6UvIsTEJO0LRQjEyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZDy1UEoea743rk3cGL4ZuQx2Sa7SBgwyfw5Feyef4p4aizrUPhUiJBcJD0BWAYEBo5uCKYwS3z9CTWTCVJ2tA15384D2Lnr10DEQTuCDGo-wzOxScMDII7uRtIBhomtRESxN7ZCbWmlSLBhDFynkZ5a83FKFLAwGoq7Yob1JFNhBMqkJy_nNmr63CJjaBM5eKu9ThTGbeHjTkIQHFiHEJRE27rliwpRVymQ1sgHM9k0TqEg5eSD5u9WuyUkGY1MWdOc8YQCURG7oyyGn4wK3XFA8tuxtVCs7Ben9HyFkrhTAgndcCnvbiXCF-ZrUAzvB6y7uBVxCSkNVnm8mftQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=cn7x4McBhYgA50lv7C2ObKDE3s9P93CNvGVcPnGGzlnKurvlD574hrV6XzNIALAZOCkVMP2spjvZ0SFDPyZS6z9H58-kKU4g-Ul4TnoC733MVX77TzeCdYgoHuAs9Jx2kVc3tGX_dPvrq-0aE48l_DsmTGlUEdb4Nw7afuGrkGnS1NBU2Uj5MobkpPWwKUh382qRvvnc2prJtiw-30t6-cy1aychGqvp-jLoqO8IV0mFFNKRHeVmoWWA9ia_kgRAgKi4hyzFqX-gUa3rlRYZQYRVxrDyKK8B0Ic-PDarr3QhoNev40HWhjM9ew1IDmedQ2wXJl4gq3bib4E3Wj1bdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=cn7x4McBhYgA50lv7C2ObKDE3s9P93CNvGVcPnGGzlnKurvlD574hrV6XzNIALAZOCkVMP2spjvZ0SFDPyZS6z9H58-kKU4g-Ul4TnoC733MVX77TzeCdYgoHuAs9Jx2kVc3tGX_dPvrq-0aE48l_DsmTGlUEdb4Nw7afuGrkGnS1NBU2Uj5MobkpPWwKUh382qRvvnc2prJtiw-30t6-cy1aychGqvp-jLoqO8IV0mFFNKRHeVmoWWA9ia_kgRAgKi4hyzFqX-gUa3rlRYZQYRVxrDyKK8B0Ic-PDarr3QhoNev40HWhjM9ew1IDmedQ2wXJl4gq3bib4E3Wj1bdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecldsiTlx1cr9-H64msstt84RK4EXhZqLHSbGhbIrZqBITgrytdQYD8W8a4orBbgs5slBv3Ms_rxyEs__G5d0j-VI4KtADAw8yw4JODevvr_w3PP4QgFlF_evWwZJ219B37oxRVmKEdh-1WMqTdR_3B-ChzncgQVEG9XgmIzWCvotiscJBy4YIM8CItc4zKJ1exDgicoXuoHr1FvTw1iqD2h9A5XoVtCd36uOzFTUxQ7Yc8XoR23mhJyDbAxrOTwKbWe15ZC9HsVR2Dhu4lZPANMhTVuCq0jjT024QxJ-gNONZ4RDrx5Z_o6KTNZFvJixjg6zvQ9sFHbsSyRlncX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
