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
<p>@farahmand_alipour • 👥 62.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 00:02:19</div>
<hr>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9J2WgJ5JE4bNwwdz7q3V2IrUVuUtOyCbKQMhCWopxKc1s6gix1hOSQOB24hmiOoqWoB5x08HGAydJYskEYx9uJ9fB7VnZeWF5pJJpDrJVOMnu_47qlJsqCRfP-HOpzs2qb0DYgznXUdQcIv9l1fZfBnSuOa2GGqlnj7f10NIymfektHzHhIgN_j39xmwWiE4ZQufHxDVJBCArVKFr2knX3wNxadbTNZDzc9agKT5UKobteysFOWA7d5CnI2vyGz9gYz5v9JuSejqwGuFbqIzFAPUn6061WK260Wq5q8Ifk9YPDRe2giW4GzW9wG7cma7pXSGwOOuYbHyQbhN_p5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFdFiG6Fo_21l3eI0g9gf5NGpCehHQROmy9gqjvXJpYJeTEPafgkUx7nkUKtMtjFP9wIeLMyJeCLfsclv0NiA-jEOkHOW_CEpgQ6_y8DF6v8l3r6VeLmhIvk_r3NCqjmuu18gMJpj9xRmp9ZZQxCwzTEqVTK4KLA_Fl-R7i_MS7BeJ8rqZCPWxPGw5fQ-zqyKEpNrHL2d2MktcW40qhVBwp2CPrCbKJVab5MSSLSKFMpulUQDNlhAT33DH8tamqPJNB-5RSGquoUGFYyPHa8ivRjt4VqG19a2mNwpC9ZlUClHNenuM5RQAb1z5EazGe_BeH7Qtjgg7ZKZ9yRI8U_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6jRmf0ba--mShtp3pjmojRkhZCp-yUBEnp6GPKvFtb3MMpcG_cIQzwaod3z_JK_RX0WcI43aGl1PG8XmYwzcaGgQ7dZllPn7bL_tAMkqu-e8pnolZdB-Q-a6S4t4t_MRQdvzC9tEcOt7r153fqzATAH8LYRxtoTYUlgM0XHwMTIqMH_IdvxcS2oe0cyQ02n1aEQvjki0NWaxnrRN5V256yS5ch6xnrJnJo1ycvk2uS2MEvUjvXYooNISJULVTX_0ILL0iz-jyHamKmAPPmPccXw6i0CkTHoLu9aZhHWnUtG1tZkcqsayXmxDu17jTsRr3B5DD6yTk1vufypS2cbFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTwd1PZgtxyk9gR0BeLXT4HH9NJBSEv-GoWmPocklLko1kaf4l4DSkY9gdhkW4GEPAsm579GvpZ9_dMnFvPFrVpeK1iJRhpa8vifE17BpLQfhr00rnK0v9UOaUoQx0Zlns4m_NNYZexTlSsx5rUDY8aQqpxlf5sA4oFXATASdDNmK2Y98zhpHZzBw4lp5UK___g91VDmTjZrzpCws2F7aCKct5QozVKtpMYQioNYpZ6C-NTK39I3tKuP4DiY7UNvire5mXpaJMGhznMxllPphfuXZt9XMFn50O2x4KQy8iMYXDSodh7H1RsaW6fBRE8fReRavSpm6NEm0AAXNKTUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqT13RyNpxvUyZxQNFhVYfQBzIKdeLIX-Wx3tewxuP5oCuimFJi1Y5a4guXAEES5e8XGvOKKLIw6w2W8sxvWzUSm5sgZb3CV8xBuEDUFtVGBC3aJbm5RpA5rbTftS0PZVXW4nKbJ6L9AUlmHbvEORdos0O3eW-Nfzafm_GNZ9Zcda1j34Kw79jObwWkAc3s9iE-X3J8S8mAPJbf8eKKGzkPWaMau4hePQz85wBuhjEi5wb1F61e75ikqXinmHFmfe2Y2IR3XR3V5HrAwU2rrfCqvW12n_87wCDI-Jzb022Fh9lnpve7BsPj6WTy2uSRtmxHaYXGebIsa4ghxxdVVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXER_l-LBMLiXUNB33fB_pVLho1N5j5geqD5iwZNSCRZeRaXcPR7rODAX_LnE_Szi2zKRCO1dAeb4GSYNlF3ZuMKP9cIRsGMs8d2c5GDwFlyL0NqOO1s6CBbPzwRGKpBL8VALtX01MDiZ9uC0mw_7aNYkVfOFsbc5DANIYPbEomTjZs29DVOQXCRKvXTLxn5HkMMkcvfugzA4UzisZck7ljHcJr0AnO-3h8jTuHpVBd8qqP2r3UZYsqzqfsRbZqv82noRdl9bdBw-jZEky-ZpfyQuJew0FLLrHYpMZVyFdf9MAtj1nOVqLTSKvZXIDACEBt5TJcrjxRta6sgm1PiOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnmc5BM_BATfxTXVABN7ZsU4BordS4eNQI6aaqyKbrjAug-1oqbJULpCSOPfYakPPn9IZ-6ilxl52zQpXke46Ly4mAhmQbWX1Z-k8r-YjEO5u98NFLcVnFff2kRgvZENkQp3Q8xpJFa2dMWI7VyX4iTJmhsmHCkQtgKwFSju7nd03Nj2PIswXOa_UUSqM0_82PRRv3-ahh0OTttH1aNBrl1m6_5DFaf0dRXXf850tcCHdoK48olS356kVX0TxVUsYSMYuzq1PArgATXEtYix8B3gPpmYgj1l3V0vn4w_UGUYBUHR2PpUbchJc90kbBcLfX7eYs7kIprTfShUcLr9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgDyKCIFEawQuKRuajP-DVDVTd1Ga_rSK6An4FYmu5tAxlv8-AM182xBy-1fvpLGrFjCGZX39Vo7QkyKvO30VeKd_jP7vthJv0lRXdNVVhyOaLyaR-qf03n5OxQDg0BnkhMPG_ExvuGqBr0AqR6ZLJ7PPXXYhIqlOaEtqa76UTwGmDHsoLmqho03aA3OksSX7YPHfJjA-3dAGodheWP_4wVpmOeQjI-0lV_0vmjOgko0kjmOcv8PiY5mHQ8zjhvpp4Kf4HlIcj4xwp1SqVgbXdSPimGzuTwkRdj5N_5y4u_8pKUnW69mkSrDfgKmci98brOZDqJb9luH274MhlwRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOMUQDKuMen9GWRTpmK3a6RYOJkYtNcKsjmccPDPNXCJnN49sdui-UWrzOd3uNCv6eiFYUr1h6BGpgroq3pSpDohjnJl8KWV2aP_e2w2SordnC68cPdxgHcLeRqajlAyI65uijCkdGEXDWrfM9lxmiTeVd9xTJb4_2mqL6aqljhKOxKWWiuSSWoBgL-bmXOyDcwhMYTRNSgKDIcPEJ9tbv1sMd0jURFPsJfcCPAJsUwgQRo3uEg0fXI44vmtlClUGgctlXM1DOlG1KeWNm-i97X9Zt-GjwI-E-QnTsZ8Q8mlW0aFlap5JpjhajkYoKazah-jkBULl56GCAhiAP6Okw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7nNptiXBd2O_1RNqQ6ql2ZhCBfQcG52_swC6IotXv2zDpNC4c5fWCtGbtpwMldlTETkjyW9Ux-uG8jd7VtE_APCNvGnIxoetnRVykwK_WJeZKCCt0ti1CD2nixO5QClFmHVRhWtZ85vL8h8JnLOu-uFpkV5PFMnbiUF3i23tg93ow2G5etbPE8vbfz_1OD076tmo5PZEXr-4kZKYMt2ZImMalE_0OJaCVl9qD_9KJDmFIbXrsV5QLOQexjusupfFyCfzzguvJEFxVJoQg5ryclMLIQZw2lEycnOMKyGN8BEhk5ByyTF8pmai-g5Pd03ySw-CLKExUktypqKB63hJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=ASDihvnVvO8E1DE4pcCpL_NTBNETqGPWbmLHlh0kCBmwqEn61cHZ0QlKk-Pa970iU-vw0KF0VlxS0NzqzRQ1zGRkhvnJtHMCnYwdHDhGEBM0OLev6PGdnCyMVq5KjC-6kVP0Fn6uz7-iQSuhU0gMTliGOz7lpJ9dDLmpzaFipTDWdo3F4IL7SWhd11lIBH1QCDjgLgDKhCg28tkjN0YzOr1Ya2Pb_SGe19MWqxSrvfYDDy3SrP4l7HVFc4fLRBfeQLPNEgg1FNWS5idbt7o8i6aSqetReLung6HBT7gdnZVOgJ7TWEIrBTg3ZZ-6M7Vp6GwzGVgm2O-tfMyywnN7mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=ASDihvnVvO8E1DE4pcCpL_NTBNETqGPWbmLHlh0kCBmwqEn61cHZ0QlKk-Pa970iU-vw0KF0VlxS0NzqzRQ1zGRkhvnJtHMCnYwdHDhGEBM0OLev6PGdnCyMVq5KjC-6kVP0Fn6uz7-iQSuhU0gMTliGOz7lpJ9dDLmpzaFipTDWdo3F4IL7SWhd11lIBH1QCDjgLgDKhCg28tkjN0YzOr1Ya2Pb_SGe19MWqxSrvfYDDy3SrP4l7HVFc4fLRBfeQLPNEgg1FNWS5idbt7o8i6aSqetReLung6HBT7gdnZVOgJ7TWEIrBTg3ZZ-6M7Vp6GwzGVgm2O-tfMyywnN7mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AojurpRtjGZ_sWj8jSrn6MauUtMCqZvbLGPliO8Pzy3_GjUXY4zMd9fOaZUWkaC_hUeEZSAhl81sh54ovXcQSXrQKp-nM57JBBQMuknVfXknB4bt7wtSzHyHIlCCLnPpPHUeWjbEwCe2wMXDnZTd9Pv015hmBSMCHUvnNeS3ooh8kHPA8Y2FChTXzdND3lpgX2rvwcriyZMuc-F5shCi3KUMHToUZB_QNvCgY_ijyLkRbl73dWRR4zbJQtXBE_x36Kqre6ZAukkfC-VdRbXuHaAPlZT2g6YZoBTpGoduwMdIPecKE3PP5U6FVscJsRJLAwqDaxWdD3TvjIBGcP2iWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kpdi0pfnqtjomeoYgd4JwLBFAF9it25_-C6ioXSiUOGzoGHqs7-ktaE2GMSJJyLrAG-Lt2tlyEkqHkDp24tNm7pwGxDXkA7xfj64Ex_JMmxJIR1YFQr5n89AgmK6TsCZ3Ox2HSKVIjGTtM5u02fgA0Jf8QFfOzdJSm9Xcv7jHLO9nlT8VT7nLABCFpsdoRBEL1nqBwH7MIW-ZyNTLHJ2oa3aV9l8h_VCYRWE6lkGMkKww4bfgjDM9A_H_Phl-nA4yN8bI7hDUDtsUXwsI9nSL_u4hsejdsmI2VTzeCb5EwdtrpwBWnUr9eKil0fyDyHzAIZCWmDP8xKPwzg5AqwbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcBI5FTWB7Gtqyr5R9CkomDv4-7uHC6wVupF69wX-qgAshGunDz84C1x47vLrjyeEwmu_Z3JN6V38NG6US0CGt99GXH0OQHCBU56Lt4IDxpX82n72kMyXe4T3YlftkTDq9Z9PpsOAvtfH_wU5FmAfzRO1SwbdE01hNdYq1oKkfZJ7Hlgl_qmqhrtKnkP2WycTVCgSQbDxx95pL3sP7ISP-1j3T--8gF8D_1wZKXIeKQpqsXkLTXooaxBI0pHFsRwj2wqVZJgUIG1WrzGDNdah2tKr9NV3pme-zUDavq9BynVry_fGx_TxOWQmP_cy_8_8VrpT0cKAIfVyguAY_Cl4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=h3g8fM9FfhvVfJabLXzd6RsDM2PpCjJjGepUHjUavbC2tC1BiPnJyauQYwSQKEpJas9-z6qvhUG_yiBWQU2zRX6soniQiIYSp5jwC7524I4MWvpNt36dq6tNvEiz9qbBhgQsdGb4VcnQVbZODXy23qWhmf_CpxG7jCmY6xFh7KDz_wk_rcJfLpyyoR1pL-0OqJC_iDdXBJAfo4VnuODLQMvT7TgNTjUuZA0hOf-xeCsSOz8DI2bsxff8ywVY5LQu-iXgvBOWimitqeFS1bKQgoO7LKS4OwnOR6cVc66dFuKnvjwwTefljxxLgb2K_9aH-A9lJ2NzNIQuDu8APbct1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=h3g8fM9FfhvVfJabLXzd6RsDM2PpCjJjGepUHjUavbC2tC1BiPnJyauQYwSQKEpJas9-z6qvhUG_yiBWQU2zRX6soniQiIYSp5jwC7524I4MWvpNt36dq6tNvEiz9qbBhgQsdGb4VcnQVbZODXy23qWhmf_CpxG7jCmY6xFh7KDz_wk_rcJfLpyyoR1pL-0OqJC_iDdXBJAfo4VnuODLQMvT7TgNTjUuZA0hOf-xeCsSOz8DI2bsxff8ywVY5LQu-iXgvBOWimitqeFS1bKQgoO7LKS4OwnOR6cVc66dFuKnvjwwTefljxxLgb2K_9aH-A9lJ2NzNIQuDu8APbct1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=tA4wPRfVUIZMce_GMZhPlvosOXLYAYUk8WWzbpsuhHLBoOm7tbeSWLwx2p-3e2lhCv4br5Aqx2575FRZVA0QbntPEPgwikmv41HABotK0yXTVrMe3fiQMLUH8LArXd8svFzLTV7ARwukIPUIDzBgPcEwZm-X2IbI6hiUWSI_YNxJO_Y2qZgVcSOka5WEItbjcNI17MjqtJxKAnzDCb7PsBfYkndpSALSCrDJNJtoZ4ei6sNAueaURG-aLlXgATfUtyB5juVigwTuckhuKRGXckv0ib2hFpE-Cc-Zgq2TwCZ94CT9CU_KrPiUGsj9WJXJf75hY-LXssqVTzhSRumf3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=tA4wPRfVUIZMce_GMZhPlvosOXLYAYUk8WWzbpsuhHLBoOm7tbeSWLwx2p-3e2lhCv4br5Aqx2575FRZVA0QbntPEPgwikmv41HABotK0yXTVrMe3fiQMLUH8LArXd8svFzLTV7ARwukIPUIDzBgPcEwZm-X2IbI6hiUWSI_YNxJO_Y2qZgVcSOka5WEItbjcNI17MjqtJxKAnzDCb7PsBfYkndpSALSCrDJNJtoZ4ei6sNAueaURG-aLlXgATfUtyB5juVigwTuckhuKRGXckv0ib2hFpE-Cc-Zgq2TwCZ94CT9CU_KrPiUGsj9WJXJf75hY-LXssqVTzhSRumf3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=pskBX4FSKVZ9eYQUMDxvZN4JFQZZzN6n8OhzQ_u2qsnLKnsnZkXHsN4bsHi2fK8jNKZjDHEyEi0vew1FjN_qfeNNamv3i4I4wFqOGlne1ILPVaGj3NQqPaak5Ouh-brZ2x_uHkHZgUSoivEj_JTPsNBP74vQfATRlxujP5qmu6epcTRZQV4uKUfTcUNgxOYMOuNQNq2Xarq1PmUzDHa2a0tulw9DPrly4r0T7iXsKqGYB7fySh6141bJu_KVCAc-Q-PwVHNYMfijIBbORpaSx3INncDpLRmdhRaiOlpySx5npxwNYSQ_aimDUm2wL-y7cbqtFMqR0Iiir1ao8N9B9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=pskBX4FSKVZ9eYQUMDxvZN4JFQZZzN6n8OhzQ_u2qsnLKnsnZkXHsN4bsHi2fK8jNKZjDHEyEi0vew1FjN_qfeNNamv3i4I4wFqOGlne1ILPVaGj3NQqPaak5Ouh-brZ2x_uHkHZgUSoivEj_JTPsNBP74vQfATRlxujP5qmu6epcTRZQV4uKUfTcUNgxOYMOuNQNq2Xarq1PmUzDHa2a0tulw9DPrly4r0T7iXsKqGYB7fySh6141bJu_KVCAc-Q-PwVHNYMfijIBbORpaSx3INncDpLRmdhRaiOlpySx5npxwNYSQ_aimDUm2wL-y7cbqtFMqR0Iiir1ao8N9B9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frrnmoCa-A6T8ZB_Fu76YoE3y1En2Bto5qJFLRvzT-8_D5PXS7PeSQ7KaSR8iOwHTWutfRUFUmZa9K8LeVME0KekX8o3yLYRmp3yE6WrlWlwU8Q1SVZ4SazojHinsjM3dxouxvD8nH53hzri4HEJavhny_2GyMFmBOUaNArfSsEFndIkyqpO73nO653sscfpqmxUNqPKSPs2xleXgqQ8np2myRgxBQpMqqVkqigdz1gBbi86pGAbQDIiQxWPvLtS6sqddhodjpXMExNqjjHK0jN-FumOi30QrMY46fs2j9jRqg8-tR32of5DfUnNY66sTp8-lZL_GMb3j8S-cGkRIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxkXyqJp7toaB__nONDUNhmdABoITRn0e_bau5PuNGmLjaq8tGAVB74nNy0Fv10NGYVngq7aQdGhXcb7NXKHZxoHa0TB66bmexdu50yLZMDIhndDUPZzcDEKSqxgZYUHIqPeVVvyd1TSUBULyO813o3WZmZViZfdaOYssvA0ouxiQvdfmPqwOnauRIspWeouuotZ1nzlq8YMpO6o7Zsx2WbY1NFTQ17F5AXu3JCqmsT9fBruRNUlnR8PQFQrtdYLfQaFNpvEGRJIzDvPX3SzrgqnbaCA8wQ_GMHu2sLN3pnuGuFdvCqaARCGtsCruDdEhgOqhmK-UbSqqlEiNlFSgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnAhs5ySgaQcAVZ6Ksv1lH9gN0umNwPIVtJi7PP4ZL5ccRLAerOLpqqf6WOQE4Q1xZFvDgw4jmSShLV82XtiQIUlSt4u5p1Gxq8JvBENHkn9F-e3abKsmM-tNjbjk8MSNtJNV-EL0RJb1zUKD7u_k4deIxvqhbGEy5nS4HCsEKgdUTUOaYQ9mRCDLOP9MTdBeUeoc2X07l7GcTj2zWdaLHLq2XB8CZGMBwpJyd6Hrxe0PUOFxxCki0182Kp0mwApVT3IPKdSREdS7jkowI6EfPlpcWNqvV_OMaxpRDPtTW5YbvZSk968FIZ1cYRRL5PQgG-ULm9NKP5_SI11Mq38xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOlVWaSk_-IqtI0wZc13lNY2kE53sCysdVutJ3FfHmuKQvoPWz9kpn0GT5da-w9PPijbmYczNnLVITSJYI3uUF-UXUsSg53SjSbCFS5iThBMwRBIgbd5sUmJ43XPRsNY6dZfvdbgM3L367trb-Ly_ye6tZ7n8alkBW3kwpWEf15KX7iGHJCEGaPI77RLhdZgXy7vZphQdpEfD5H_ZF0-T70p4y1yMVro5AJBHFHLz8nGiZ66buhVU5fso4IenHdQHjpK-27Lt6DuHsOrg-w5ZL9F8ttkzbqUtkBB7qMtvM2V2Kk3O5hnNaX2jII_v89rKSnMztnEj788ReMmjSHadA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYB4E65V3ora5Z5hQ2qxHaDk849j3ujLN9jkUPEJm_GEcth4S_WDdbJXDnHSfb_A_vusqykbnVS-ODtHFojkQCjKa6EJBagbwiIWo-ocymIAX5EEjQBzJNcUKvyI80zauTIrpha1QOG-1PGtDj-8HR5kKXwl-jkwBzdoEjYKq0butrR-PkwSFHLuRGfSV0lBLa8RMVxVUgl0gYPiDV1P-xIZosZ6wVRsF5oY3SUv5Z2WA5A7_2t5RLst1yPo7MAY-kMNB9RQ0sJbGeppS4sjsdKZWjUwhuOo_QrCdIclWhwFm2PruN4h6HhB0RumNIXT4aD2zxpEvHzW-eaRBzMBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAy4J8P9yPwik4h4NO7MXCOPfDms5kUrxdYaZ9Zjwm8Chijd0EdIUtbQ4muhp39wyCpvsZbUzJVSFegp5qjI-EslavJVjadbAjuO9mY6VAADsZrWzcPrvxQKnKwV-Rz1hQdtPOFnk--L0tyROYxYJJEdLlWLcQ-jxRf47-WRrzVXQFCuEe3NJqRWvuUhcMtNjMXU-W6-4ZY3-2OKdCCN-UVuAQqAZAvN-Lyp38NyUgZhWsLGulmD8Tb82Yb1nVoTOoL9bA8CnhgsJCirrlM3jlYnfS1TSXmputPK0s357gZ6USGcIb2K3r5DoAR5Zd_PavkznZHw5wzY7BMxsKAYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2kY3ZoKUzwmq8Xa00ea7N25sixGCXbcxpTJQAQwtY0_5Lib9sUg-6931CK539ChSm1g1XisaRQXdqKVp3AWymMfmFe0AFgc6hy1xAPYICWAQb8shacwW4c8yfAte2Lbvur_vwyw5kOdUONozQ8ueRl5j5Rq3TAYSTSsAFUyfMNdInzfGhSccJhNZv2iYdwyZBGu22LbmgXZ-aLjGxriFwrQkaEGTX0khQEmZM_3O-jcwwCZRa6KAQ6TvWBWo9QOgY9YV5rO_ct_vF7iyARJuByo_egPUYElQhL3a872OzX9p4H9vUpUd89V5aEDrUKg156bBVlCXaZMYevf-dSVnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLrwWurOP0NU5TYFyYW5MsXQUoQe2hi9zaDeCXsE5RyPSqwWFTP1_84SCqS7KNVMbA-DuYfRYBweZlrtXogzLFcs2T2UE3qpfXJt0cxvF4HC9uHnIdhJN5VUWZu8YyvEUByplHqbLJcwcWtth0cKqBn2yAMdEsmlecpM8LNzNpUJh76NiOtCT7g3WFgZiFkB4gN00SYVW3fhj-l40piwNcgPNsmCpHIJ4c88Pydfb4KFT8-_kL_Vd1XZuqyE_oIqHdN-kvWq8YazwXzaDV4I_L1dAvA3Wc40cn4uDDRxUm4dhQdeSMdR5bvj8pwugfgPUWhry9vul7XtAdh2s5752Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BidJarEfe2Xui5UxLI4rGfIWoPWbvgX6yWkiOQhxkCO64xYpOuid8wc4m8kNs0rclyXkm2utZZ-EF6AqNyNFsEIGjmOHIRtUQRfIGidGkA0NYL5qNaLSHC2b03x0YjV93zFyiqya9a8i2Pnfd81v7rhquV9tZ883G4b-CopoEQbswEoHOFji3oA4ILUpqL48yBEwqTLtk_JHTuJyYHncozgtmodltas5W72PQvL4hj9CASKTFQKSbHbcqmpBD5pCbDXmx035E8WI8Og9A-2vREXvvzS8OE5wd9XAVdO-5Y0HKTR0ibsWTvwAChNkFedr5_gWrPA-sbZM1kN1GwIyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YenEyc5VHiwbC5UCC3gB39Rjxgbp3VpeIoE9eKrTtFGrW0hMPV6yQV1jeL8Ef8AwFYrTDY_C7aut69DxTmw0HNXvceuVK5vfzKwyXisC8LjiQttmSjgtqMUCY5y8Vi4MvSwfAtv62KAOrytTZ9dokkGMxZBWANnwXCRQT1wf2aiw168Q_3t3m6QzYYICE6eQfA9NT3_IS7aHXjGul-lQPDjVvYk949NAkfEEHSfSuJ_Nq6Y5BN0suJwofvkGxBQLBj-ATDNZZWdO62VHP0_GIbyT_1DEYZXTEIZZ_zUz51zM4scOO3FUYgBhATeAyOBvLLIb3MMBZFDUmsi9WpnaEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUMTopZ_hR7vb6aBLNtDPXUnJINFYAU5KmKqIiIV2FM3jU3rgEX4EuQzTvwB6qo7LH6OfsZhRGS6__HH5X58fDgi1Y4hT1WR-lKI1CSxjCBtho79ppDosLVjIh7OZLLG9d0RDn9yeE5BRSBAJSG6ylbryAFC-g-054VAfRkFRibtkNLDqlZB_CG_Hk25ERDWn2WIX4WQAXV4hLn11TJ9UrbbLnFwP05c2RDJKWBfrHQPLV7duWhIrmQPTx07dbKH_ZTuLZg46VLPkWNNfcvPvw0UBF5Hg4aul6FXi8hjx7qRHa125X4evGkk6BaT8ys_RW0A87aplOlfQzKF1tLg7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vfznvy3KvkKpjXgVcKZHJMg3hw9I8n6f_1AAy5LfwFEkQ1IrCsKwipK85Wjfbnr5L_UerNybvr9qFn7oatLQjimDTot-YjFgKKvIuSmlVob7PxlwxAHrDZOaNX-W40eyIdnBwlXfrcgNa0C9cgjiyaCua0eqg1S3oy9OClwZOWA4XCX26myEFtrtPhmS45dp_z0mtSnJNnvqFd0GTU4mwd7GNSVCbzNWMoXRMvhWLtEbqcAhkbknrO_fcw9_NCjMRInTfZSM8fVb75CK76cPeh6dONPt_Ywqz5oBIx_1rJTTH3g1OpUh88QD0zTwpixf9uZnDAI0of6rS2eV1PYSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYs2Lk2fzYmi8HgFif7dJAWVtl6ygb6W6bVu3H5B-3E-vim2HGZDwxBVTZnSQYoT3dH6Vi5b4VRNgrYc_ZYblQm89shH9GzmXu2Jk1V6MnW399aA5ZK3Lk9O2l0sMMlY-HZTWeIvDvDzpdKDnHG_3FSn3wiH6Vllvryw3dxzP2N80AKAD8VnuGxPqVwNWqOdydz_wdWoDK3sigek52dxb45ZO5rawcdqWZxfObnD4hS6UAuarB6XJNMu1i6E6iDjPyrRQ8XrR7TsXRu2ZEMbotfWHuM4MmGQEdqb0Mkj74_pz1ugZAOykKktpLoJVfkWc34WY6DBmh8pAW2NZM3VcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG7kFeDsDJr1bR583_aQned2bkhNk05Lc2waP-jLPDlk8FqrEELnM_ujTWSjEtn77YNs4S_UbXB6cObxl933Hs1HitqGPe8gx1vqmdFfljGIlXvuLWBz1U9tVo02CPdhIzZVLZLiQpStwaPoV3bOmeZ5rkdvrVS7G23DsvuYiOwSJi0AoBC43Tuqd6QKhyd2RqHQer_NOg9daEXkI7zCktvOHDSLc0qD4WiUB1hjsf9Ot46ayuCD874k045OKCoai20zg1kx9Hf4CL39rPMtcFgbz43tDBQ0Ril4ywLnWqELBg0VUcnscfVcvRc7_LZhntRqv7C5OL_4SRsvVc4QEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgaGjcJqwTKOFwPeU3voWknN1ES6YX6HyIJgOeOJFz79_V8q6rQk20QeS8S59uI4rcCvHgtw0Fn3VaVhASwv7ZcVD7A45UOXy14goK2nxJxBxgeOoeL9e6yPXt0EpZFRlzXCkLuAG9Ij0m0iLB0MLlBXaWuO8VIsOgaZPijaIbjH5L33g368n0EaBrC_k3zaUIpadDKdOZVpuq2ERqg1SQZUs7VqpwRAxWXlRfE6lCEL-H_0Xy5kED2pxScmJgZFrTo5aktuqrrhkTQMIWigbjRBnJQpoJ0Jle2ROL1D8dcwpAOD6siy8cW-ApycbqmJZAOgE0AvMEVXDo3ANuKBUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=giSOtM5e3xsg6yQXASDZKAw6t40VrAelgS4HBj0P0W5eORZKvCq4ucp3N1qY5EY8fQw2KZVebfqOJqskJVXuwBotYxhcvL50llSGOALB3IgJ3Kq1cw_cfl_P_4Vl2egW6p6gKbseJmpWQMd4tu9A44-DJ4Hm968IRfFpOksHN6onHL8sSTjq-21yklM4mqg9ZNohvpnf96YQZQ_BJmNBPNLVMEdDrEhbY1qLIw3aE5neg1K_TYZHXNZISbZhH6e0ny3RZsom6mccXFFB_7Lp3cB0nJ9K17dOFB03WFmvp87IorAbQsZuSf4rL50SyVDLbUx7WgAkPdIjdhjFua_gEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=giSOtM5e3xsg6yQXASDZKAw6t40VrAelgS4HBj0P0W5eORZKvCq4ucp3N1qY5EY8fQw2KZVebfqOJqskJVXuwBotYxhcvL50llSGOALB3IgJ3Kq1cw_cfl_P_4Vl2egW6p6gKbseJmpWQMd4tu9A44-DJ4Hm968IRfFpOksHN6onHL8sSTjq-21yklM4mqg9ZNohvpnf96YQZQ_BJmNBPNLVMEdDrEhbY1qLIw3aE5neg1K_TYZHXNZISbZhH6e0ny3RZsom6mccXFFB_7Lp3cB0nJ9K17dOFB03WFmvp87IorAbQsZuSf4rL50SyVDLbUx7WgAkPdIjdhjFua_gEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djTotyqMxEk5PbZuzZ3u-VfjiTQDCS5RoCxmFG_fQer2lj8HLgpuBQJmPH93bkdNwzEXYtwRxYvh1WGwm6ZoI_78mFgmpIeFoSXHjzoBuIx5cTpQtcxVb2VBSzqSm7SOn7GzrQZL5EWutlZIUEIfNP90BnLY37xL4K99wf4s7e4PBJwF05aPQ1-YJlcAEbQS_Vb7E_MCsDLJRLhJO0kJYhQ5THE4zXYHbySPlAQ6exq95OzJEGSWxDVvLWjzr3avQlZ3lG0XpmuB8Mgi6gAQZfuhRRRO-rdYbGSXfsUGUf0nLq9oQ9GcNxm9IdKaiRHgAVUcNz8wJmYLRZrgjRzFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=PYOzX4pFdY3_NIvdKZVNjJBbF5LRHuK9r_pXpl9iocdWwmY-jtDwG1nrXSk_6Z2JPzqX6sveM5ox4Le_s0lLi24Sre0LwMfr8pZt2ENmJTI8cBAyLO45CBguq6gJmBcqCkXSQTE8w4uAVS5olmokzTpzLzQj9PJl3XiXQk-a3Kqd2HfxF1wTL0T2Bw68kDAlVEbFpxngTUiM8nohXeR4bExKx7S88YGJrYEu-Yb75aWQF7I4VkqEZixoXHWG5n8-_Jbh0j76VHSMAG0cdj7zLEXiPAmOWGDy47JXTyg3L4h3TOYU0PLpkBT5SUb_LnbKid5Qx3VrM7Q96ErSXUu1aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=PYOzX4pFdY3_NIvdKZVNjJBbF5LRHuK9r_pXpl9iocdWwmY-jtDwG1nrXSk_6Z2JPzqX6sveM5ox4Le_s0lLi24Sre0LwMfr8pZt2ENmJTI8cBAyLO45CBguq6gJmBcqCkXSQTE8w4uAVS5olmokzTpzLzQj9PJl3XiXQk-a3Kqd2HfxF1wTL0T2Bw68kDAlVEbFpxngTUiM8nohXeR4bExKx7S88YGJrYEu-Yb75aWQF7I4VkqEZixoXHWG5n8-_Jbh0j76VHSMAG0cdj7zLEXiPAmOWGDy47JXTyg3L4h3TOYU0PLpkBT5SUb_LnbKid5Qx3VrM7Q96ErSXUu1aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=azWeYqMmxKfRYUN4f_2Y-n9h9vADtimBSoBMwAZzGI1tnQMnkkrh-WBiu_hrKQQBjUiHKiyVrJMJbVItgsmIk0qIHcGKrcK3YIwsmGG1XB1DwsVttZfv5AMVbX7WEATRZrlq79Y3jUH-G6XKU42IdbW_Evq3lipDFzVtdcUr2MlXiFpnjtzuDsLBLM9rH5CxYDXDPP540-RCniHOy2CFvwwFJgjG2RB-15VMxXSstR_tm9XXSOssHxakNyTFUG55Cg2TbbQNbfk22psGolYeKmWe6DEJYYUuIlI71P9uHnHncd3mZixPI-06rLK6PuoE25VA0BervCRuPsfKzdjJIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=azWeYqMmxKfRYUN4f_2Y-n9h9vADtimBSoBMwAZzGI1tnQMnkkrh-WBiu_hrKQQBjUiHKiyVrJMJbVItgsmIk0qIHcGKrcK3YIwsmGG1XB1DwsVttZfv5AMVbX7WEATRZrlq79Y3jUH-G6XKU42IdbW_Evq3lipDFzVtdcUr2MlXiFpnjtzuDsLBLM9rH5CxYDXDPP540-RCniHOy2CFvwwFJgjG2RB-15VMxXSstR_tm9XXSOssHxakNyTFUG55Cg2TbbQNbfk22psGolYeKmWe6DEJYYUuIlI71P9uHnHncd3mZixPI-06rLK6PuoE25VA0BervCRuPsfKzdjJIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t42MV1OoatPMTWtVzVt2bGdWMSE-4DmatWlK6pG9RMxaOFtzvukRnhoIoS90EoBmLExUjnyX-5R1jEdGZtY_r6nGaebH0j7NpdjrcM2JFpIiFtDK7RzMERz7CdsiZa7-OUpQ2D09ISqKerd6LGiGpINyP0LvAtTRsfkVWEmJKjOcy6wR_4kHdDf6Dr7ZTefjqaGz8LuANgMhrzAavkCvMszBhTwFrTD33TzHLPQJdOC353QzuqgMisvc4de9gN9rg6HcS2f3ddAqWhN71bU8cCj1i3KJxVe0YFGBNYUjKULvKFz-39Gbx0zcwNfxyW0ODL3odHOaT5n0Aq1oGAggSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=N53Yf1eWTMT6_gd9W5YB0kR-ufz7YVCwovOgg_prbM8n60eaJcWTT75ndpwkB8kbHzbPZfoKqe-AhtBgrb58Nn5iRvn-LMEhMQHa0syW17mSsgmIPC1Hydohd5WKk27Q2Xaz_R_-ot-VwwbNXo-lZl6CxDUn2z7lH_DQIe8K-4xS9cbUD0ggk9kDuI8FC0b6ohF0xISmM7wLYH-oBTKlnswPomh7WrGHpwth98Ly_aJTLrh1hQ7aHPS5tmtEB8Wf1H5tJ_osd3XLHLULG9t0sAp-Xz6hNPZRtYTV2ORpdSshXBWvpRRJVoQlQXsiDES14Rfik5LmD-w2umoEJl_LsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=N53Yf1eWTMT6_gd9W5YB0kR-ufz7YVCwovOgg_prbM8n60eaJcWTT75ndpwkB8kbHzbPZfoKqe-AhtBgrb58Nn5iRvn-LMEhMQHa0syW17mSsgmIPC1Hydohd5WKk27Q2Xaz_R_-ot-VwwbNXo-lZl6CxDUn2z7lH_DQIe8K-4xS9cbUD0ggk9kDuI8FC0b6ohF0xISmM7wLYH-oBTKlnswPomh7WrGHpwth98Ly_aJTLrh1hQ7aHPS5tmtEB8Wf1H5tJ_osd3XLHLULG9t0sAp-Xz6hNPZRtYTV2ORpdSshXBWvpRRJVoQlQXsiDES14Rfik5LmD-w2umoEJl_LsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az4k8MAmWaAzlJ2A6LQ7nxR2KF0lR-06FYYjU5AMOAIJmRS97UgScnmuXLbls_DB43LYpaHWQIoOl4QALK4Dynw5vBd-otqYDERzg0BuIh8GzRvgHB4WHzX7gopOti5U5aDbsYuT2l3dbYDAJMHvlklzk-wkjJYLkvD1yNKd1GzsnRTtjMZ5aNVENim751lKOc75Xe3uxaHjoU4SaA0hy3IKazgFSbYOUBtFhR44Nb0aZrLGyiyG22lWXPH9o2pMKYysz20HY_Kd_dImSARHQAqPKjKl-tlO7KGMdvWspI__LLS0x-1m_NZ46yzt6CtLfnLir49lhFhwbRxpWTungg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVNj1wbOrkf6pFFOuNSBCLcqkC5-HhYKj5bIwCALurU7ZVnOJAh0fXH3Ml0MO6kb_IF019vT55woxB67A91hU-L7obHgBMaOb-NTIm_WabYouprKLQgUyUkUjALyMuGNwt7mKHCQiRCom6SAAS6ywvoOHTfVJjW0ugkp-Nq1wWtSPRw47PTQyZjgEIXGjS_AQ11osQePYrKiWUcba_DCN4p7T-i-r8TZoJHIBPwvh0UOAocy7yr6oEDQ0TN4CfRY0-tad8ZelBW11hbO5bbewee4Wnjklvn-C7FQi-OagZZ70KRFau_xRYPL9LJnF1cPX9JPjokQXgxXgyhnMpOYYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poF7rmDX7eZYkj9SWFEo0mh7kZrB0-qhNj4aS-VlmRA8-Z4q2r5Eer2oZDCZU_weoETGLBqk2sK2ksjxz8C1CTJVexucVKqJ7Isf83xm_6vp9qjFVWuqLetVj_HVAtOHdfHlWTiuo3_hL1d8aORKHhnwysUCIrsuGX2PLWdldy0eG6ayoDJngODoYEsPfPgpiQB__do0JzrK8ivhqhC4HJSPCO-c-W3-Q6P6yKw4l84oIb7CRbR1gEUcg3WqHJKOssFXrQJh96nnz8BmP0FvNCPyhkASjPVC_xkvqOo184tF1ZvTbDYjjv0X2GiH7oiBvuKKTogUiXajKgJgEoKorg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9tM-o6ZZ5fdlzhgLKCyn569T1TqWagwyoUNDKtG4jTeWyz1lT4LmIvVRWiYtkbX_4L8WTYigwtEqIFsLfcLROupd-jnDxlmISsmF4Q9xN03J1D5nB_VBif6JcakdSZBs9iXMvz-7kJTJho-EsLOdsdNfurfoIEz6cF2p2hxzNFG6woIuNfemyX-X1_J2HXTqyu7t46iy6_BaXRfcT50cPSJ87dxU8iIO_TFkjQE4EyQ3wOBTW4z1ZbhoAH28PENHDEWnOg9VldsHAsUFKfGbRFad4YbEDWBsX3fYJaCWL0DXLXdjdGUIJGRqMD-FWmcWn3_dJfA_ex80MBRHfQ3yQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=KnDhJbtxF27WxH3fOv_pO3mS3aIMhxxMZfrzaZox5qccbE43RTBV8nSWNPpXVVZfAd-2cH4RcDWGQx3wPqsfXMdjgElnUxSeMZnLlKktNChhWze8onHBLTjsqndiZWXpsbU3uyuUqf9yyTWZn1PCI7tr5hyRV_IiQTjCM025wyNUJ9txgBVak_wiQ5ylEdpDBS6LUrB9AmoA1EJu9uEnv_xMcKVaWbR5DdszV0RZc86Lw1mBuqtB2K3vZAX3Fpz5RIJPBuQzKJgsiJYuoPeUpG6CqJMtUF7IithScBl-tQNoo-dGMC-AYKHsD22-WDISRSq-mxTeo1Hd_2cPjERXPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=KnDhJbtxF27WxH3fOv_pO3mS3aIMhxxMZfrzaZox5qccbE43RTBV8nSWNPpXVVZfAd-2cH4RcDWGQx3wPqsfXMdjgElnUxSeMZnLlKktNChhWze8onHBLTjsqndiZWXpsbU3uyuUqf9yyTWZn1PCI7tr5hyRV_IiQTjCM025wyNUJ9txgBVak_wiQ5ylEdpDBS6LUrB9AmoA1EJu9uEnv_xMcKVaWbR5DdszV0RZc86Lw1mBuqtB2K3vZAX3Fpz5RIJPBuQzKJgsiJYuoPeUpG6CqJMtUF7IithScBl-tQNoo-dGMC-AYKHsD22-WDISRSq-mxTeo1Hd_2cPjERXPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=VUieeW6zI3n97u9q4GlGBSmBT248HYcmlVtWgaoePtsreOrRtzgD4JUGeHZDEuyC5Z5-BEjnnuOFGoXrHs1dIi4lO4VY2wv0fdq42pGd30r7xJ3hoJWUOknMRLQiBwItaoo-QhnNb1sEcqrl7kIwAH6VrAmaVbk96zMjE5DM1XGjEbgAhlNjMYWPsBeiDLKjobfIDb4P4_jhtNhdw3uTO370GEiC070bKORYsB0xEjB8V10KK1SGYCfrUM5HK_ShD8ByLDMTAX89DuOm2Eibnncu0B9Jru5op5yeQKfh2xkxNohTni2CqgifBhZR12yZvku1FIzTxMedGKSJlhMPTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=VUieeW6zI3n97u9q4GlGBSmBT248HYcmlVtWgaoePtsreOrRtzgD4JUGeHZDEuyC5Z5-BEjnnuOFGoXrHs1dIi4lO4VY2wv0fdq42pGd30r7xJ3hoJWUOknMRLQiBwItaoo-QhnNb1sEcqrl7kIwAH6VrAmaVbk96zMjE5DM1XGjEbgAhlNjMYWPsBeiDLKjobfIDb4P4_jhtNhdw3uTO370GEiC070bKORYsB0xEjB8V10KK1SGYCfrUM5HK_ShD8ByLDMTAX89DuOm2Eibnncu0B9Jru5op5yeQKfh2xkxNohTni2CqgifBhZR12yZvku1FIzTxMedGKSJlhMPTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=FaUVugqz0qvq73brODtHF_aHzwBUCn_xk15UzLbY2fWkIHfvsD1SI0nlGsVUSN1G6IhZEQfX-9K6mju3nwc-XPdhPTpHaJhiUBYRX_bWyFMivG4UHHkSwEo6_rgpJRvrRsrDNxRUZOAvfDgl-y-C_b-M-_0c9gJArKV2FnT-lB1T9TawLZHBjXeXfh1XBI5PvyO8zwM3vrVmEkheEjLFBvk_cfBdIKU1hr1QiYPWshFHf3RB6KpsWQnq_nfflqfHTaeY4tmjS6uk5p3OS3E3rTLEilF-PlVvNocHZZvOOCZUOlxf22FHf_583FYvafl06Pi97kB5-x785C0eI2XCeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=FaUVugqz0qvq73brODtHF_aHzwBUCn_xk15UzLbY2fWkIHfvsD1SI0nlGsVUSN1G6IhZEQfX-9K6mju3nwc-XPdhPTpHaJhiUBYRX_bWyFMivG4UHHkSwEo6_rgpJRvrRsrDNxRUZOAvfDgl-y-C_b-M-_0c9gJArKV2FnT-lB1T9TawLZHBjXeXfh1XBI5PvyO8zwM3vrVmEkheEjLFBvk_cfBdIKU1hr1QiYPWshFHf3RB6KpsWQnq_nfflqfHTaeY4tmjS6uk5p3OS3E3rTLEilF-PlVvNocHZZvOOCZUOlxf22FHf_583FYvafl06Pi97kB5-x785C0eI2XCeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=XAp10IsIcx9R2CO0FbS5QveFuAsMIgwptIY0fBzVkkMj-hcuOB2cRxLSyLgCZtSf4EhEfxbleEO6S_HJy3vdAC2s_YSGCoBk1FKSCDXsUdZPOlDBqXKE7xih_6V4ty0oWZn-rE1TTRpMi6zH-l1PGx_gecyizURuWpxSkYsOXEDnt7vi7wf4vNSgfmSGCajYxZ3qNro32p2VIYDFLyEcn_dlPCilMJKTvUFvsBKQUrxqs_h0X91XuSLJKHbNx5S1PX2Q82Mfc2w4ol4O7ESLj2IhMTmFXomz7RevaYP6Djeqd8pRgg265QnR3yi_lkO_Ocs5Kd3xDBVHF_JjEvTRLQpt7aKV2zBW-uYU064XjNHpBo810fKgFV5IRhJWuJ1E2VX38KTlGFwdRaFPbBPy3RP5WqRC48pS7IqI01jkBM0JHEH6eTF5DQEznEjStLsrCH0az9FHLRHoCt9CfRgvm_OPGWL54vBzgOYvjzYFCRsQmhgoPB1urI7ER-x4UOcSVa6ZU5CACcOpRkFuxO47SbM2imTfMnw3v5e5PXIEvFxKI0Two9mDXU8mPghcLNXbOQfPPG13PlfpqvNyrQmQzXQdzaacG8NWTuQQx8CREuXlcQxIUF0ZQ7CfS-T7PzkDMhQ4pa6W68c-EwyyrdAYikTTE0QtOJNKx4pvkPf9Hkc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=XAp10IsIcx9R2CO0FbS5QveFuAsMIgwptIY0fBzVkkMj-hcuOB2cRxLSyLgCZtSf4EhEfxbleEO6S_HJy3vdAC2s_YSGCoBk1FKSCDXsUdZPOlDBqXKE7xih_6V4ty0oWZn-rE1TTRpMi6zH-l1PGx_gecyizURuWpxSkYsOXEDnt7vi7wf4vNSgfmSGCajYxZ3qNro32p2VIYDFLyEcn_dlPCilMJKTvUFvsBKQUrxqs_h0X91XuSLJKHbNx5S1PX2Q82Mfc2w4ol4O7ESLj2IhMTmFXomz7RevaYP6Djeqd8pRgg265QnR3yi_lkO_Ocs5Kd3xDBVHF_JjEvTRLQpt7aKV2zBW-uYU064XjNHpBo810fKgFV5IRhJWuJ1E2VX38KTlGFwdRaFPbBPy3RP5WqRC48pS7IqI01jkBM0JHEH6eTF5DQEznEjStLsrCH0az9FHLRHoCt9CfRgvm_OPGWL54vBzgOYvjzYFCRsQmhgoPB1urI7ER-x4UOcSVa6ZU5CACcOpRkFuxO47SbM2imTfMnw3v5e5PXIEvFxKI0Two9mDXU8mPghcLNXbOQfPPG13PlfpqvNyrQmQzXQdzaacG8NWTuQQx8CREuXlcQxIUF0ZQ7CfS-T7PzkDMhQ4pa6W68c-EwyyrdAYikTTE0QtOJNKx4pvkPf9Hkc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=WENcGb-aA6_4_OQleX6BbRwUTtpkG-ArCsMGfZ4N74uiAZT887nNFSCgO4CvtXv8PRc1YtWKZjPLmBgk_-N6qDzQOB9RMc8A-RUMZLWlVPBz7MKLbc807whTKo00woG2XSf3qDhNJm7Qt4Tk47-e-GPEW-ntlVD_xeMMp0H9_-y1rB4JeBpty110aODJGoJKN2xMVTdmFxOqcLFEJ1ds8vApuSMHgH-vQmfVK3ptOoz3buE94XtCE_aOKsSTLIujwPmt2c-sFbcpuagsWtwrX5GkiXIdqwlBaAOH3V3UOMGEwCWs72P6y9VUfC3tlG9j0_7U5giSOmaZX5-tYu9w4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=WENcGb-aA6_4_OQleX6BbRwUTtpkG-ArCsMGfZ4N74uiAZT887nNFSCgO4CvtXv8PRc1YtWKZjPLmBgk_-N6qDzQOB9RMc8A-RUMZLWlVPBz7MKLbc807whTKo00woG2XSf3qDhNJm7Qt4Tk47-e-GPEW-ntlVD_xeMMp0H9_-y1rB4JeBpty110aODJGoJKN2xMVTdmFxOqcLFEJ1ds8vApuSMHgH-vQmfVK3ptOoz3buE94XtCE_aOKsSTLIujwPmt2c-sFbcpuagsWtwrX5GkiXIdqwlBaAOH3V3UOMGEwCWs72P6y9VUfC3tlG9j0_7U5giSOmaZX5-tYu9w4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=M6Pp-D4WV-53hhB-tSDJc9L-CauWrxxSRA5e_PJRJwRdkevdqvlXjUgKhGp6zfm7a4gmkQT_DYsYi7wlRlU_m3qyvqNGEG64YlbI-t3ZqICz06o77yEETlXlWfhA8YataWAemfb7CEhECR-UZmtriO27G6UhGUnRfzUaMHOrmjRRq2zmZRVRHL9X3LsRKPRyxZjhhYdnYKMzVvwV5MzkL_syFUTQehp8HhoEdkxuL3MBuCjMlpuqY_V-09eFstSSuteocmFpR0V1diObKJMJSG2lo5U7MlmRJEEZFXbx1UxCCBvo6UGh_fFe4DJmdKSTQD5NOMcHS303e69AcLxGxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=M6Pp-D4WV-53hhB-tSDJc9L-CauWrxxSRA5e_PJRJwRdkevdqvlXjUgKhGp6zfm7a4gmkQT_DYsYi7wlRlU_m3qyvqNGEG64YlbI-t3ZqICz06o77yEETlXlWfhA8YataWAemfb7CEhECR-UZmtriO27G6UhGUnRfzUaMHOrmjRRq2zmZRVRHL9X3LsRKPRyxZjhhYdnYKMzVvwV5MzkL_syFUTQehp8HhoEdkxuL3MBuCjMlpuqY_V-09eFstSSuteocmFpR0V1diObKJMJSG2lo5U7MlmRJEEZFXbx1UxCCBvo6UGh_fFe4DJmdKSTQD5NOMcHS303e69AcLxGxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7e2k496D-_yMTy3u32IyNCwofPIcA05IQaxmd3QJg75qKybSisOk6KRyMHBG7CDL7zPuzlfP2vBCLFSsR1A9ygN3Ib69p10LSm1VzvpBh-05DTkqfq7hU5R7dFbcShwnWI64RKpXK6XYs7FRu5aCzQJVeg9uX6JmXAZ_f6tgqnOthjab3OdySZwjiL98mgdqz2T5YIMlLmUkLf6R89mNjo0BTxleFJ6EqWfrGa7TOcwnXOuAnPtQ8zjYaKRnyoNK2Y8IhVAOmJ9m9ETYR-3_x6ztrlTi7uVK68xFb3ZgzTbmEkLT6kY9N2x3yzOdlMF2Juw3-cj4wnYuZljZFbLfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=RxRZ6akR9xam1XfAZjunvYYDnX-RInIKyuar96xp_YBjgv9UCSKjiSUGPnrF3LZ1vUiGCytiDVAAmEfqh6qSA82w4YRa--HNcxbkFsEWeGouClnNNWHhjwvcgaNmOJlAYRAwRWsj5vOvQSQ2BQvaIYEC4c-HmvUI47sNrCCyt1duWJWzt-nas6Z0Z1ytqbjcfsmXOX3LwY32dZn_T0vCZ4OcQLtryFCS-rNHP-70Lwq3Odv1eMc8gm_0OZEZ8NAVtPOePVr_9HKPJchtIQmABOZQJP0aCxdZ9zHFAuqwt0hy5llNa-5AsDxY7ieZJFs0cZ7nby7SpMVtv2uGuVGkzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=RxRZ6akR9xam1XfAZjunvYYDnX-RInIKyuar96xp_YBjgv9UCSKjiSUGPnrF3LZ1vUiGCytiDVAAmEfqh6qSA82w4YRa--HNcxbkFsEWeGouClnNNWHhjwvcgaNmOJlAYRAwRWsj5vOvQSQ2BQvaIYEC4c-HmvUI47sNrCCyt1duWJWzt-nas6Z0Z1ytqbjcfsmXOX3LwY32dZn_T0vCZ4OcQLtryFCS-rNHP-70Lwq3Odv1eMc8gm_0OZEZ8NAVtPOePVr_9HKPJchtIQmABOZQJP0aCxdZ9zHFAuqwt0hy5llNa-5AsDxY7ieZJFs0cZ7nby7SpMVtv2uGuVGkzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3BekqlX38wO7O7EiiSaIBO0l43YsBmWRkYASysWuOWgkll2p4Kxzczp9VoOHRzPtil10YrHILoJnAbEFRwLRxdhdXhoZ8LIQyJZgVBhbTBpyJkHp1W-VVuwYTFgx6YP7KbAr-5c7T2T4VrD3q38rBKPfKQjjrHrerr7mGMD4E5AZFT8jDVwD9ehR6BWvRpdhpQ9sBYvjFh0tQg-N7Y2NaJhQfmYv-zaRdih35OoItHGQFP3j7-CuIhn9fRWWMYdaATQNgIunOuN9vLlMEqt4cpA9i1bUBbqc5WVEeChfGBg_gX5gv-Aus2TcU6oNzqkKT2gpz57UM_B-XYRRD2IEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZ0GCLowC3ZsDTVGovFRHhYe3hnKAquo_Ido62msDcWKH3jyzgz8uovHy4q_u8iXRTUCrPBFeO6b75PczAtTHrU7e8qzp3KI3uPM0NxF0C7Wcu-ek4e-sDSlLOx1oJD5nyX5xmt4ivWsBiwThgiiqqrq1wA3mJRtC_16AS_6My1YCRWWzktR5K6hDHb11hIniExD5K4SafusGAH9x-9baHgbIHs4DF7Gt4Yf5L7NJIaacgOsMoegbKu5nOygfBQCt3ewnuFLDzN-iJKqd18PnVJ7B6TvPCGHacnBlxJFJ5ftE8qmuEy3oRHMdfZw6NVq5ewbgLsu6IFJ-28nPt9vzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=GhottVBi_3nZdBA_vZx21rG6YaJifay4crjqg5TdaeqvNinu1JpXOb411XiiDPgMvGOyBYFbxOGLx7q2k32MfIQ3upj08cmSwxsVVvZemTTc3ATitWagSQGjpyLBs2r2qYHR4wrBf8SYa5bLbMoikynvqnXaqrSiJLqdGwVw2Msm-PgoPzd9OQFVVxQGksUd-Jstc9yw-6sW_ZVFhivKcB1w3fbNa35UsejYnu6ZRUeg4papnaEq63ZfsoImjRMEr3zHDt64BCyyvNgbHrnH2wUZ81f-oeoh1AO_16QVNRDO-pIKqjwCMMqrvC62csjQF7Jo_qoR25CUaVF1ryktqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=GhottVBi_3nZdBA_vZx21rG6YaJifay4crjqg5TdaeqvNinu1JpXOb411XiiDPgMvGOyBYFbxOGLx7q2k32MfIQ3upj08cmSwxsVVvZemTTc3ATitWagSQGjpyLBs2r2qYHR4wrBf8SYa5bLbMoikynvqnXaqrSiJLqdGwVw2Msm-PgoPzd9OQFVVxQGksUd-Jstc9yw-6sW_ZVFhivKcB1w3fbNa35UsejYnu6ZRUeg4papnaEq63ZfsoImjRMEr3zHDt64BCyyvNgbHrnH2wUZ81f-oeoh1AO_16QVNRDO-pIKqjwCMMqrvC62csjQF7Jo_qoR25CUaVF1ryktqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=jeHi29TrLi6KzAJQK7Xi4HRlxIbHadYvPd2x3UOx57dnEpfOUvpEjYOQj-ZY56WnAoDJQxtHL0CtdpmojWs26f1wa3HEcQ0fP4IlUev3yQOuGjQJknwYIbb1jpcMv3vyuc5pyScbOzIoaWiGDFWEyvE0CCbeOpqFI5oKRLztNHQN_Dku1QAd3kZGD4-wTDjQFhM_8cgHUTjYLOEYB0TTGmBKUtmLV4WYx9vHWKljPA9xL89H8WNZOCwqbAEV245Sdv8hHva7cxXwNuHMHjuHgbneyRXS3W6kK6x8U88v4jobTCe0mnwt5XqopMGbNM_837vN4OEoEkdhZj2apWzILg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=jeHi29TrLi6KzAJQK7Xi4HRlxIbHadYvPd2x3UOx57dnEpfOUvpEjYOQj-ZY56WnAoDJQxtHL0CtdpmojWs26f1wa3HEcQ0fP4IlUev3yQOuGjQJknwYIbb1jpcMv3vyuc5pyScbOzIoaWiGDFWEyvE0CCbeOpqFI5oKRLztNHQN_Dku1QAd3kZGD4-wTDjQFhM_8cgHUTjYLOEYB0TTGmBKUtmLV4WYx9vHWKljPA9xL89H8WNZOCwqbAEV245Sdv8hHva7cxXwNuHMHjuHgbneyRXS3W6kK6x8U88v4jobTCe0mnwt5XqopMGbNM_837vN4OEoEkdhZj2apWzILg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=IRxFZf15hQzJ5_eGPjy1TGQNz233_yoTZx1M9b-A831eWBxPP78H3eGc5tXxc9yM8pvUuxWYIKwBrvdHvbtzARj1MgYm2LwQEQbqyD0Rk9A6hZJIWRVv3erfu4NF7Qokoz14YRTGEo-FYcVhGWIK5c59_cfRvCakD4TmWDm-AtHKuVDGobJzFIRXGQwjjS8u_BEqc__MeMTHqot0N11tueXjZ5QoHzYQ55X9skkz8jHrDxHnFYuQEsOUudUIOB3wx87Ad98ILeDwKZ8FL2K2hRBH3ak4c5CaKwq25A9pqk_Q1WUMsHNPF-YKQX1NdEWGW-8HvpzDeTXPO84PulCudg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=IRxFZf15hQzJ5_eGPjy1TGQNz233_yoTZx1M9b-A831eWBxPP78H3eGc5tXxc9yM8pvUuxWYIKwBrvdHvbtzARj1MgYm2LwQEQbqyD0Rk9A6hZJIWRVv3erfu4NF7Qokoz14YRTGEo-FYcVhGWIK5c59_cfRvCakD4TmWDm-AtHKuVDGobJzFIRXGQwjjS8u_BEqc__MeMTHqot0N11tueXjZ5QoHzYQ55X9skkz8jHrDxHnFYuQEsOUudUIOB3wx87Ad98ILeDwKZ8FL2K2hRBH3ak4c5CaKwq25A9pqk_Q1WUMsHNPF-YKQX1NdEWGW-8HvpzDeTXPO84PulCudg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFMrOTsGSk2b9nNvVo34wb13MeBhpjLcCSodzK9h50nmwnyTw7ASZtAyo-XZBFaKXaeoePTFf9ZWCJBNzjx-1Vo9079pqHP7vh9L8noHMtZjDEyb3fCW34tSfwoaWGgCBmldjSByl6PTKg8bLxgaxErr7_aOeF_QAFuuyAxxQRCf7Uu8TO6XuHMEvO5JxzwN9Cm0KT1Hk5LZ5RH18YW113CoGc0CtU16Uj_VYUcwjRo0zBTp7yJ29Zd3rPCc6-Yje83d1uffER91qNwgLoGNWk2ZpYhB19PQWDgh8M5sMrho3PbziYv41QZpHm1cZsJvkclOsEYqZsFp_rJeC9PBIA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=VUArBYNoWuaMzIgDkT_99nnhN780viMNxUW7o8MpwYFBKowGqrU8r6Fv3_NyUvlOQeXvdfKj3P3npSthzkKiMq0zL9xWlrgyrFE55pmVDP4T3DYXIPxxPV4vBvnszDDp6q2Z7GWas-hXLZthjNDe_hfsQlkyyamvkjK83ZMkPYXMEQ3yvzYgi-UOurUHPyGO1LOV-K9IrqFt_gK_6UKMcGSJrYPv_U_7D8RWMXjTKMmomDg5JF_Lkqxq0ludAV8NT9pi7oIT3b56mEa4bJ3H7CH5gRZ0UTQLVcjAcAYcXJttnkjuhqzSOety42UNaSaJ4tuhf56Jt64kgLRrxUbP_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=VUArBYNoWuaMzIgDkT_99nnhN780viMNxUW7o8MpwYFBKowGqrU8r6Fv3_NyUvlOQeXvdfKj3P3npSthzkKiMq0zL9xWlrgyrFE55pmVDP4T3DYXIPxxPV4vBvnszDDp6q2Z7GWas-hXLZthjNDe_hfsQlkyyamvkjK83ZMkPYXMEQ3yvzYgi-UOurUHPyGO1LOV-K9IrqFt_gK_6UKMcGSJrYPv_U_7D8RWMXjTKMmomDg5JF_Lkqxq0ludAV8NT9pi7oIT3b56mEa4bJ3H7CH5gRZ0UTQLVcjAcAYcXJttnkjuhqzSOety42UNaSaJ4tuhf56Jt64kgLRrxUbP_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ethV2vxMCsYFauB52sAwHfm4Ji3G8fjGnswltoAZa7BdTIV82HogPTP4luhq4yPfSEo986fM5oMkaMs5w-JbadtT52HbjdbvdqU0NuIIQ2pklhtPnrxm4k4Y4CLUocxZ_YuHBoqBmK2lbgCK0xvur6mteqbRl0n-GCvWz9L2MKjz5zTnRfNKcv_VHnh_3jSgc2hFZNVNWbHxXHSWUPCP3zLunCz1CrGjpsh_Kz2xAdy5usnYmD9iL78ERQ-0EPnFGMPcmbJg8eRFpSiJrnqVPocxxzIvQzRgTPZ6_1O2FxKbgheEG-4YtSAzN705Z0XznmsB_U7VDelwgLWjJ0x5tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ethV2vxMCsYFauB52sAwHfm4Ji3G8fjGnswltoAZa7BdTIV82HogPTP4luhq4yPfSEo986fM5oMkaMs5w-JbadtT52HbjdbvdqU0NuIIQ2pklhtPnrxm4k4Y4CLUocxZ_YuHBoqBmK2lbgCK0xvur6mteqbRl0n-GCvWz9L2MKjz5zTnRfNKcv_VHnh_3jSgc2hFZNVNWbHxXHSWUPCP3zLunCz1CrGjpsh_Kz2xAdy5usnYmD9iL78ERQ-0EPnFGMPcmbJg8eRFpSiJrnqVPocxxzIvQzRgTPZ6_1O2FxKbgheEG-4YtSAzN705Z0XznmsB_U7VDelwgLWjJ0x5tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=NGObELNHreS6X9WLPnjm6tokeNobXVQkAWoyc0f0-HW9lUMGyfa1zwDNvSZobQUZCEY7q2VZobjwbGKuntJulDnyx1p1JW9k3ufXfODOl6crNMIvKsG4bfSL8qyDLbr1rBObRPfWkrC8Y1u502wwIKPQMGHAjQyfIZKj3pgeOpF96M56cF46s-uOvEUgpmC31q5eAlH5DH5c-PVYZw33ZChByRg975FSgR94elOhAiZ48Ld01-F16Kgzpei1vXEUEKKrWbpInN7ymvvyG1mTCjRRTU_wfJABKlxs1ygJ-NCxV_rx5TDEShiOt_mwVkqMwMH_dinW87F30-OqwDZc7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=NGObELNHreS6X9WLPnjm6tokeNobXVQkAWoyc0f0-HW9lUMGyfa1zwDNvSZobQUZCEY7q2VZobjwbGKuntJulDnyx1p1JW9k3ufXfODOl6crNMIvKsG4bfSL8qyDLbr1rBObRPfWkrC8Y1u502wwIKPQMGHAjQyfIZKj3pgeOpF96M56cF46s-uOvEUgpmC31q5eAlH5DH5c-PVYZw33ZChByRg975FSgR94elOhAiZ48Ld01-F16Kgzpei1vXEUEKKrWbpInN7ymvvyG1mTCjRRTU_wfJABKlxs1ygJ-NCxV_rx5TDEShiOt_mwVkqMwMH_dinW87F30-OqwDZc7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqIHsubgaeYB6TE77J1O1ZXastkvEPSG0U_8MXiHqI8uShqtRFkESqsEaRLYXQRWVUvCUlYlqAQWU65H4vnV6Ar2wlb92yInD8VDzrNxRBotCwxZDST7kL_ysNokwRDanuTtM39JMrJ-7Di8Au9PszL6ldjJev-JldaXwvOghj7pss0po2mHI01mJyobFU-YU_F5qQLKQaJScD1dKQ4nFygTpqqjPqW69UncaeUdSZAfBhP7nm2T5rmwijWEwQQm5dltlE17OhQQ3_Cjp4PgnfrU4YKTYwPFa51o9nN7M6tNJqnWnZXi02jBvjpVnc8zQibVSYfAjnkYMv8XsCuX5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=FRELccIm7EfClOn5UFeeAcsvO9-Pd3Zza1iqg3ErTg7Vptkp3BOe_vRxV5MeanVT2dB3J-8Bz3NYFboeqxbs-R_9iZhRyqTR_zirJG3lDKL7sNTfVWL1_y7bBzsinF3QiVL2Dj5yho3Q04a42PgPmBrNmx2z0ERZY7MLAw3DmJB-88sitPzul4ZEt-jb-ZQqQ0sNa9FmAVXNBdm9-4gDJ0zaULrlksy7XnKLj7RGrWb1n0Vjw_sfQELkHOrc_Z-GZCAosDtj_hmFFbzKZ_9Knayrj3M-nsNS68CNYk7Z_1YPvgw8FAMzYI8o7Fyiu538oUFeh9x-iXRUZfNUm1ghiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=FRELccIm7EfClOn5UFeeAcsvO9-Pd3Zza1iqg3ErTg7Vptkp3BOe_vRxV5MeanVT2dB3J-8Bz3NYFboeqxbs-R_9iZhRyqTR_zirJG3lDKL7sNTfVWL1_y7bBzsinF3QiVL2Dj5yho3Q04a42PgPmBrNmx2z0ERZY7MLAw3DmJB-88sitPzul4ZEt-jb-ZQqQ0sNa9FmAVXNBdm9-4gDJ0zaULrlksy7XnKLj7RGrWb1n0Vjw_sfQELkHOrc_Z-GZCAosDtj_hmFFbzKZ_9Knayrj3M-nsNS68CNYk7Z_1YPvgw8FAMzYI8o7Fyiu538oUFeh9x-iXRUZfNUm1ghiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGPCcU4F_-mafYpdE1F6-Fzl6Z5Ib00tFOfLBllQQCWRXS_sGSIjB9w4IQNWhjcHiQ6EDZ1uyQUtG83ipR4kBEVR6tLXOcLRlx0j_Om-SI_uXokJdaeHh8vRhEuasmQL0-xeLaAuS2ilTH9tDvSV8n4NDigERZI2ETL_WmHQ6l4-sh40-WBGHlCUKGlJe9yBKKE9h6FEoGhyRs_r_IeVbXpkUh0CTjGemVI91-qfDT_k0VPefxfM2udogrgbGKLlKtBwiMMo4mBIJlGCGCoJy71OLLQ0TBH42DGdgnGzp20JXhiviV3bz__-cHI-adTgJuuRxq-fK5xLUBfnav77kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=Vk-yEZI4JqywO7gT4nw62Vqx-i9rWJSpZ15fmHjz-UhofnNhenbi2mc0v0d_ImxYSXZTD8izTqFgaC9jsELqzcYuPXSIaAHEpyuSEkxdf2GP-F1DXKaYz1kLehQvRd_byoYkboVS7RKQx0crd5ABXato1OU-Zs4LpHJ0wxaxjCpMuOHyMJgL9p7ci1XWMx4ow5TA_9QbxghaKqMUQjzXzfJnSTyUpKdX9Pt4y2tx3sbMITB8f7WXzBXxCSVfnipUy8sh-pkMqNinzWjsPxi-kQRozD9rxYO2Sa5IRh2MrTNT2CChjCKPCApYxb_s67i4_P2u81EHDdpCnJ-emi6rSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=Vk-yEZI4JqywO7gT4nw62Vqx-i9rWJSpZ15fmHjz-UhofnNhenbi2mc0v0d_ImxYSXZTD8izTqFgaC9jsELqzcYuPXSIaAHEpyuSEkxdf2GP-F1DXKaYz1kLehQvRd_byoYkboVS7RKQx0crd5ABXato1OU-Zs4LpHJ0wxaxjCpMuOHyMJgL9p7ci1XWMx4ow5TA_9QbxghaKqMUQjzXzfJnSTyUpKdX9Pt4y2tx3sbMITB8f7WXzBXxCSVfnipUy8sh-pkMqNinzWjsPxi-kQRozD9rxYO2Sa5IRh2MrTNT2CChjCKPCApYxb_s67i4_P2u81EHDdpCnJ-emi6rSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iE7hIJpORWKyP1pqDywXZoozPILPQ0LirHDgtoI04XGMMSQJicEWxTyCV_lswcXbgkjPeVvFYrfpLsGo6TBrgVWsFXHuldKfPQk4ZnDSkuIUPueH3f2mXKLd9-MZHrC_lXfIWrN5F8KNacUfr6GeX9xE4lnPwrtu0cXCL3fI-aFxpfYSNNFr1xQQIkA6oCAMoAgptanBZA8SVE2psdrI8De4ZpVniv_YexDAUkkb4HMBpFHJuesomKWiLpqjogdtOgeE9X0rYszBdYXFAEXb2PKB_S1yDUS-nQU_wlqrKr87iX0gigRwViO7dHQNCqjLPB8kdC4I2sMkb3wzqhMXMw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=ha-bZ_VmKPlUUPmrRmU-DOMeuaNTaD1wPNs7D90RtRgRBTsv5whHipCRuAQNqeq44qDrdddMPKlJQ8lIBWRpTExUPqtbB5ogj1IIsMVsNSKgtQeKaMvKjij5g3ikMhO0en9YO7WthcwJck1F553rWw0wOGgvtCu-TawXcmRbCXYVmPW1lDlIHRHR4s-hCJAIzGtV8QPiNqOdjP7k29hm9rG3HOl-QT7tQIL_vhtI3ox6J3pd-Dg2kyDnavA8SIqmMfiAe4skEyF-ZKmjlfosYDaODD1-IvridrPpsJVMe_v8TN3Q78cXxmsJSepoVUV7e76tKkH3R80d1lGdOa9EuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=ha-bZ_VmKPlUUPmrRmU-DOMeuaNTaD1wPNs7D90RtRgRBTsv5whHipCRuAQNqeq44qDrdddMPKlJQ8lIBWRpTExUPqtbB5ogj1IIsMVsNSKgtQeKaMvKjij5g3ikMhO0en9YO7WthcwJck1F553rWw0wOGgvtCu-TawXcmRbCXYVmPW1lDlIHRHR4s-hCJAIzGtV8QPiNqOdjP7k29hm9rG3HOl-QT7tQIL_vhtI3ox6J3pd-Dg2kyDnavA8SIqmMfiAe4skEyF-ZKmjlfosYDaODD1-IvridrPpsJVMe_v8TN3Q78cXxmsJSepoVUV7e76tKkH3R80d1lGdOa9EuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUWHPQCH18-0oQKVONbpKXEYyrNOIqpsJj88LHyourFKsuLxNgyADHXkqZp2NugX-CpGR7cEqKLDocHC5oxKSA_STNbCaJ8dbJ9u9afjkb09Pu1UE20gNm_ZMc62c7WpocixXfh1Yh3gXSyEzbpBCo35cC1EOe7bOkSbS4vIgjksIDh7v6Ecm5X9g_v701M5MGkJJWfWqhn1UVFMxDZLhkATY5CMHIoBsuVsfndsYHS1UWVj-DQNM1QvuTfLSD35JFAilz29PIfLt5VI93Z54HdO9yrKv_hhjLe6FDKb5p5Qg-ybxATN2G8PmfU2jC8cUzhuQSlRo8Khc1HkjQR0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJxmH4Jjzw0Nj1H72RHLKl1LtMwOk1MdzwxtV3yBp8SflhVatbAodmH_iG59O5mkzvfOhy4JJy8xhDkD5DzIuL-Ju18gHxPKUVNrUnRzs7kdR34i7wMCWhxVxFuF2orboNW4x4pc4m3itRD3m7n80TBuxRDnyse9bJrZ2Gwmzre0K-c_x599J26Ddv8a4A9JujrFF0pjmJUFYb2LvkdwJZS_39xwjS0NE8DPFel-qR_BlCamNGvvh6mY2OlLcD4VqXCfdSNGtub7sRwJewJ8w0dQILw8pJVOQU2e4ecNZzL7WxqkSkk8Quld9CrCEIDB9fxWNcSiPrDgnIysyeT0mA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=d6W0q47q4JUkYqHOXIYrvPfIjaR-_dVinYGm5eY9rHybSp745XhAozs6Rq43YuIpGq73hJfA3-Slbt9m8Ym_Yqr0BsOfREiWQ6I8bj4EDwg15FSqy9M9GFahYgS0EcU93egqQkT18Lp1AXcZBbMSc-pO2YNI18aeASrZDYxQ5SUmBDd4KsPlB3FTiCzfwlfORrUpOYjyG0CwSI4BKL-MSW3-wXHpWIUO8x2LjyOQWH3DyrF7niI6g9A_fwm-uXZoojzZk3NUdh_yiBfvBA-vIRFJVOjFAZGzvBjIjKwQjBIlUYVxT93YvUFXjuWI5DikdkDdEtYQPmsFlQxkOZUlIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=d6W0q47q4JUkYqHOXIYrvPfIjaR-_dVinYGm5eY9rHybSp745XhAozs6Rq43YuIpGq73hJfA3-Slbt9m8Ym_Yqr0BsOfREiWQ6I8bj4EDwg15FSqy9M9GFahYgS0EcU93egqQkT18Lp1AXcZBbMSc-pO2YNI18aeASrZDYxQ5SUmBDd4KsPlB3FTiCzfwlfORrUpOYjyG0CwSI4BKL-MSW3-wXHpWIUO8x2LjyOQWH3DyrF7niI6g9A_fwm-uXZoojzZk3NUdh_yiBfvBA-vIRFJVOjFAZGzvBjIjKwQjBIlUYVxT93YvUFXjuWI5DikdkDdEtYQPmsFlQxkOZUlIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1Jzoa-8abAAt4pN75rT6lQ5QZury3tHgpsQcaGUlc1ENEfvL5g8Jxj1zUvTf4BquUcshKbtceB4l-TmmrGGj9-rlseB1ACLt48kV6SPtavVgTJs3QHnqvEQ3VlPmBEWuZQSbnitILuT8M2zEq-30L5GAXRb41AvPcAS3TV1J-7lYJUDL36jgkBP4LJF4kBSOLh1Uw4vV_HzymdZkZOQn0pCpIsw6CtHgHaswQ3QV43hZDpJmJtI1V8xOQ0018SIYhe7xp2lof1zEBtaZDkON25m2jrgBnK5yLx9zmPMTIuOv5jlOQCeVq5l0d9603UBePTmDC5MqnzwK80ERhC4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdjpT1VE03wgkM4Edq8iW_mR7OrLE9-TFJ2O4AF6UrFpnPZrXku1o7AkfIB8ZkTdcf2qY69pNq_cX0nmQ1g5arV4Y-n2IwyCR1pinqNeT-NRM5fqe96-GnDtEXt6Xgx9tE_JBBqb8_iskLUkWdme24QB1gCZUmWLFbGyxCb4mCvNp4p60TUWEjPgiVd3nXnBLweDUeN9VjYtfDw5T0EeG1oNF9ys0C8t8f_S3zH5tx1Pzr47_zRvDs4FpO5mppE7PYB_528mmyZu_WEK_FPP2C1ZRlvNw_vZhL33YWO8Hhj1h6Keke4XARTczuhkLIBDNQkphG5ZhhmPDb73T_xDBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLxeQuS1xqXA1K9rBW0FALO03WV0w1AjZMdl79hdlloVKEBhgqeEaoPBYE5EANXZ-HH5UeCYlbrPM2I-nMERQ7EycKQERQp43EXTA7H0gs-Yvzr8Eh4gVunijH7Y2gcmbLwlnoI7iwKKSLee1HQbg52vchsjbgU5if8o0JJ1zxppeLFYyvA6kIvdlkzRDTWBFkrgVj0TwJ8saD2uFEQjO8UaMZZdAvXBR7lxCg9DPv8WkOQwCDGspZCN_JHutxH70IHP1yr8VR415tpDSIWmq2zyvtQMCUttorM-ZuMqrM9Ku7KpatiLUQ4k6iAxjFa_6F956pP1IYJBZ6CKlXQyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_hoNWdsku06UBhBfAM_CyUMVsA22YrwN_qLtNiaXMwVYA3KOJDQoM6zsujb5K70sggKx_VEwysJpYo4H5v1ZH9p1xGn1gBrwSfw7SGMnT5G0QzrkLOvqmDGwkpkbzAuq96EKtu1vcx-DuuWRZzp9KkwXP3shO5_2pp_W9Cn8Demouxb7LD_W1rL-XvRLKZC_sd0qfvTyPB7VVf2DUW0jmEXMsJBTByxEsfxFAcAHq2NwcuLBtnuUr2ZZ8aa7qZfNXsHmGngFRIjAprgXOMQPIm0Y0qnBLsTsY7gbO2DFtad89JDK7x9kr9LVWXMw3pZf3saPcsygagj29_sKXijbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miKrVStn9mtIMAfN02EDR10MtYbdHCPZ5iH5NvmckuZcGz3nITW9frIgMYxdkC3o3Rn9xYiR-TH80Xm7njhC0F66JTVL-Z0x9K4wxdKWXg9GSUE0n7jJwUyqLKLN36p8uarfnjjF_xnzRrrCfAKveoHWZDAZT6n7X0aXxO6rCF1KdOH3av7VeLn7hdqPz73XA2pvEJi0RmZaStU7BJdEzBXOsUON6TTXp3oecu8YcU4Q5ybiMs0nStbODZv3kzfTxi80GgUSZRacLHrJI5oR3zO4DT_T1fPsl2QJgfBb5pvpnmiYx-zv1WblMMWHMESHvZxLJyiPaYt5oRHJjvzCfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=eZPsz4YQ9cSWR8fEQ7B5LFLnr3it0PHfv8uB6iW8VWournkNrOYjudSWqf-kmIBLpqOW_qpYIpI1vk1Nsz9Z1DMQv6V48dgFya126bySbE0Gfv4noyFZ28rc4x2fNfN8168LZXkKMWurUoC_xZI500Ya2M4lXLY246EteXF5FAeW9u94ChQLWhXBBWH5W5vJKlj3vX9cuw0byUbTRqhvjeTc0UajOgmPv43iOkcUFfjualz0WEGs8D--27UgmA6sjR-QUCd7VYMoORubNOKXYDCYwgfB_Z8-czqqcEhRjmIm58d7ZzBNmUBvBV1On4MtyVQCjRrkfic-lnX8NNxasw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=eZPsz4YQ9cSWR8fEQ7B5LFLnr3it0PHfv8uB6iW8VWournkNrOYjudSWqf-kmIBLpqOW_qpYIpI1vk1Nsz9Z1DMQv6V48dgFya126bySbE0Gfv4noyFZ28rc4x2fNfN8168LZXkKMWurUoC_xZI500Ya2M4lXLY246EteXF5FAeW9u94ChQLWhXBBWH5W5vJKlj3vX9cuw0byUbTRqhvjeTc0UajOgmPv43iOkcUFfjualz0WEGs8D--27UgmA6sjR-QUCd7VYMoORubNOKXYDCYwgfB_Z8-czqqcEhRjmIm58d7ZzBNmUBvBV1On4MtyVQCjRrkfic-lnX8NNxasw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=eLeC3RCDi2IAYebc97iVsy3eGjimYRyq1E0-MTjxEAQSR7VsP9AAZESXftYWB5Kcxt-ftUcEr-RxAIkP4XKOJtLPX3gul3R-7AsQzMeQjAiyWzZWHOWfgFlTyJjrAEivC-u_moiy7yz0GT2NbGJEeHYgncRZcXKP6_GgXnOIwehlGkGaPhz8DbXE8MbuwgukF2mhwzdGnCWiaNzEKzqMXBBaLSGZzIndvktvmWSmWnI_A0vBDqOY-9dzf7B-9sb_r6QR-jiA988v4GD3wwKm7v6EH3HotaRbx31C_bhRZmZCikyxE6LyT_vkMnUA7JgT_Leb5ZQ6E8JiT3jW9QWXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=eLeC3RCDi2IAYebc97iVsy3eGjimYRyq1E0-MTjxEAQSR7VsP9AAZESXftYWB5Kcxt-ftUcEr-RxAIkP4XKOJtLPX3gul3R-7AsQzMeQjAiyWzZWHOWfgFlTyJjrAEivC-u_moiy7yz0GT2NbGJEeHYgncRZcXKP6_GgXnOIwehlGkGaPhz8DbXE8MbuwgukF2mhwzdGnCWiaNzEKzqMXBBaLSGZzIndvktvmWSmWnI_A0vBDqOY-9dzf7B-9sb_r6QR-jiA988v4GD3wwKm7v6EH3HotaRbx31C_bhRZmZCikyxE6LyT_vkMnUA7JgT_Leb5ZQ6E8JiT3jW9QWXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=KYa382Uy5IlyjMSTStetWSymc9YVI81qwKHQOvtqNNb6JRwCPxXMxWJLKWNMCBzG3cj-GDury5EORrgS_yINNCG3v6-PKvNPQr42x1-vxNy6QX-86-fLwlmZM3goqrTe4f2GKojsNbFKPqBxenaFqGojh_Ua7a9G6DNyVhgxhqy7UYJw4AjOnB9jkkhuog-a49aNXmcnNNteMqgy4DLYxo37jGKivA3HOQa0VWmHKG5NgY9UL7gXG3JxjfBqddNFEaJoVz4aoMCQFMSUb1dFjPTCcf5YFhiOvEnbJhU9X-Ve0iNUm53F13W9hrm3xpq2vGh3z7r4E_XE98gHaNmGMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=KYa382Uy5IlyjMSTStetWSymc9YVI81qwKHQOvtqNNb6JRwCPxXMxWJLKWNMCBzG3cj-GDury5EORrgS_yINNCG3v6-PKvNPQr42x1-vxNy6QX-86-fLwlmZM3goqrTe4f2GKojsNbFKPqBxenaFqGojh_Ua7a9G6DNyVhgxhqy7UYJw4AjOnB9jkkhuog-a49aNXmcnNNteMqgy4DLYxo37jGKivA3HOQa0VWmHKG5NgY9UL7gXG3JxjfBqddNFEaJoVz4aoMCQFMSUb1dFjPTCcf5YFhiOvEnbJhU9X-Ve0iNUm53F13W9hrm3xpq2vGh3z7r4E_XE98gHaNmGMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=Vqd-WLlZ85GWR9NszeouNJ_ZLec5Ue0bQXxLKrRFR8-Nbzz1s8TYsfK_ddUChMX59OEc812PalApVvsrnoUhKxhs2V1gANfkQo9bVRoSLMStGThCkHpbh5MWoXaB1OVb7y5p0HmFjRUmxJA_2NAhmLGNOJC0gZz8JrWtSh_5Su4pzqy2Nef88QVjwbNiMs66Cfbv7Wl63URJQX-jdvG1elk3iw2vnyzhVW7eGMuf4NTkR_5y0UnUNj_kplG5Dnxp0s6kJV2AxMHAG9lQVfDCLsjGu-ABlFYc4_v4bVNDmGidDY3wvFtt3ygCxXJQnYxyMceCVvcsGfr3TQ-qhXby9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=Vqd-WLlZ85GWR9NszeouNJ_ZLec5Ue0bQXxLKrRFR8-Nbzz1s8TYsfK_ddUChMX59OEc812PalApVvsrnoUhKxhs2V1gANfkQo9bVRoSLMStGThCkHpbh5MWoXaB1OVb7y5p0HmFjRUmxJA_2NAhmLGNOJC0gZz8JrWtSh_5Su4pzqy2Nef88QVjwbNiMs66Cfbv7Wl63URJQX-jdvG1elk3iw2vnyzhVW7eGMuf4NTkR_5y0UnUNj_kplG5Dnxp0s6kJV2AxMHAG9lQVfDCLsjGu-ABlFYc4_v4bVNDmGidDY3wvFtt3ygCxXJQnYxyMceCVvcsGfr3TQ-qhXby9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtQEOEi7jBg5JJ1B0uE_8bFxSQOO07EJmg_cjCSfe9pDVRiHMaa6DRgyDG83_UrSAQlJF5H072AAED41s-6ofbNRZoQq62g6drRTJxbvXTaZP_mJNZGM6KYTU2c-taUw-0li8wNfYc8txCQvPCupr9Jr3MbnzneYF9WUCug8oxUBfsun9MYP3gnVsHn0zWvX4xHYdq9BwfogavJ6-QlGT4u3iqzO2hsbvnctH-gOylOkKhk33w_TjMbjmzFS0SFCkK7yPbl55f9ZklA31cwS_1Tg86JkKlHLXvHEqPeqHXC90E2mgOabUfCiYanlFtbczrCFX9upQYBrmMpsuH_EVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBIYrBC9l2rTq8JICsO8GauMpH0Y1dGl-F8boQVht7CGmTRJBoKpPlHU0I2AG5ckWGyKjxLn8HDAlCsK2CO3uUmudZWLxSoOFJDHAKdraYi-2vW-mt6ADta2zaBFqLls3KZslAisWKAr_aSt3iuUNXtW1Nk9twNcGzpYjUa4rhVMX82n-cD3C-bITAQXCj6gWgVsjyCrMb2EhEReUB65W8A_zuPpqwwHWhzQRb6bbWdzIFR8vq32WYn8GBRQORnvZoeSWUXoVhvcxb6Gd_5xNMf2QbpE8T98CzfhkEKWPVZ0dh1oINuKdmiZcFKRHHuuz3AwFKRaCjXi5toXxYytBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=DZ5xGyQNiposa6z-c4TJvPQnab0pxNtBTxg2LQ2vWwAxfyw1c6dEKycHV6MVqUwKu8k1A8eNdQfT3sFcK804eqIBo8NgEzxBm0b6ATEtkfgERI2sUDqPNDJiH1-4yI2dG7yBdun-0JDIYlbRidaXTZyNUhAWLE8ypyYUlUjvKMeWSPaGXXO_yku_4wjywparxbERGZBos_0cOTQCv0e7OB__bdkh73DhHuIq2SE0uAfYvnQ22OzEc5kA9A8s3nIBrBsaCpgBxPPXG8aaDfR8jZAE6cOvWeTTmzQCRF518d4gLemet9DWe2tKZOWVPoP40QyEfJfZaBdTW5HkYIL0aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=DZ5xGyQNiposa6z-c4TJvPQnab0pxNtBTxg2LQ2vWwAxfyw1c6dEKycHV6MVqUwKu8k1A8eNdQfT3sFcK804eqIBo8NgEzxBm0b6ATEtkfgERI2sUDqPNDJiH1-4yI2dG7yBdun-0JDIYlbRidaXTZyNUhAWLE8ypyYUlUjvKMeWSPaGXXO_yku_4wjywparxbERGZBos_0cOTQCv0e7OB__bdkh73DhHuIq2SE0uAfYvnQ22OzEc5kA9A8s3nIBrBsaCpgBxPPXG8aaDfR8jZAE6cOvWeTTmzQCRF518d4gLemet9DWe2tKZOWVPoP40QyEfJfZaBdTW5HkYIL0aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfHlxzlmB-UvcTZOFh0QHW0CNsXX5xT8kRQlS6ovUauJfu1_VFHEpBK2IqFuYFPq9LopV91fXeVW0Aeb9KEzjcqMV0ig--wCDP-zex1_1QAPUQ_wdTYs8I_tDGQg0Vg_IiIxFkEdC9f36MC3X0dnPHe8LfHaNd72nUZQcQ1r1GP4W02qQ3hEvsWhyeuSj3g9ZzQiMw_bVa-EgBYE4nlvmIl7RwGWooSe9ciEWgqbrehBYFedbuQaBrcz8AWjNRMJDIrD2EUFkeu-7F-GwB49V_BIytMpazU_1yxRWJ14gTXfmFe1pkl2VmDcO1PDTOmdjdkTt7ttBZAE801EhDEtXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=vF37dA-A5y_YaEHk-VVGCI1k8FOC4fGEIiloerQ1qKdCWQPOeOv5oWyGMWcku25vLxeAbPsk8vHWfqHykQx68NQjhJaVdYg5GEstvQXVSyIq0Mu-kvkCJYL7f5a39T6rLNiuCuXAtMYYM8b4PqVmHim6UvIeZ3tTQgqHUNebTKIuZq_PF4dhVAc6C3WvTxEFcZl2_9pakDlGDBrWAZ0aaBcUvPlQUvo_f-__Jna3ShjEEcx8sjh32AtzR73M8ccYccO_xa-T9-7HWaOv1E9F5D5103VHacBxezICJ3GchUMBwwWHPlMsVeqAbxkigmKYsH8fILV-RMbuQX8I3jdMAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=vF37dA-A5y_YaEHk-VVGCI1k8FOC4fGEIiloerQ1qKdCWQPOeOv5oWyGMWcku25vLxeAbPsk8vHWfqHykQx68NQjhJaVdYg5GEstvQXVSyIq0Mu-kvkCJYL7f5a39T6rLNiuCuXAtMYYM8b4PqVmHim6UvIeZ3tTQgqHUNebTKIuZq_PF4dhVAc6C3WvTxEFcZl2_9pakDlGDBrWAZ0aaBcUvPlQUvo_f-__Jna3ShjEEcx8sjh32AtzR73M8ccYccO_xa-T9-7HWaOv1E9F5D5103VHacBxezICJ3GchUMBwwWHPlMsVeqAbxkigmKYsH8fILV-RMbuQX8I3jdMAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKlQ9lg2CCXcZBGIUimhCxnSyMyvNoUVkwyMUfsJ9EXGBiTsr6Sa29SMxXh9lrzmaNYr43fqQG6mZs_pUwL_koMf-H4-zzNE1lqAnzvV4fTk8yJKbwfaAsH6htUT1pi8Bmj7t2pukpBwvmFj1S9bOMzdY54s9iivydd0iBVW889gPA_YTQkbgFu56QH-ib2SqgMXx3214QhIZzcMx_qv3M6h3F8nWc3UbtgNaar8ddHvhOsYUvvxSV0Cw5ZQ_Ycu1XPrUipe4o9Vzxs3U-HHU53UpRYpEgNNXttdiluwbGVYlipCNMfEz3b443Ud9Jj10TaJ4gbwLAQeDHyrSd_8BQ.jpg" alt="photo" loading="lazy"/></div>
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
