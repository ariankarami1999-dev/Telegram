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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 01:45:57</div>
<hr>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9J2WgJ5JE4bNwwdz7q3V2IrUVuUtOyCbKQMhCWopxKc1s6gix1hOSQOB24hmiOoqWoB5x08HGAydJYskEYx9uJ9fB7VnZeWF5pJJpDrJVOMnu_47qlJsqCRfP-HOpzs2qb0DYgznXUdQcIv9l1fZfBnSuOa2GGqlnj7f10NIymfektHzHhIgN_j39xmwWiE4ZQufHxDVJBCArVKFr2knX3wNxadbTNZDzc9agKT5UKobteysFOWA7d5CnI2vyGz9gYz5v9JuSejqwGuFbqIzFAPUn6061WK260Wq5q8Ifk9YPDRe2giW4GzW9wG7cma7pXSGwOOuYbHyQbhN_p5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFdFiG6Fo_21l3eI0g9gf5NGpCehHQROmy9gqjvXJpYJeTEPafgkUx7nkUKtMtjFP9wIeLMyJeCLfsclv0NiA-jEOkHOW_CEpgQ6_y8DF6v8l3r6VeLmhIvk_r3NCqjmuu18gMJpj9xRmp9ZZQxCwzTEqVTK4KLA_Fl-R7i_MS7BeJ8rqZCPWxPGw5fQ-zqyKEpNrHL2d2MktcW40qhVBwp2CPrCbKJVab5MSSLSKFMpulUQDNlhAT33DH8tamqPJNB-5RSGquoUGFYyPHa8ivRjt4VqG19a2mNwpC9ZlUClHNenuM5RQAb1z5EazGe_BeH7Qtjgg7ZKZ9yRI8U_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6jRmf0ba--mShtp3pjmojRkhZCp-yUBEnp6GPKvFtb3MMpcG_cIQzwaod3z_JK_RX0WcI43aGl1PG8XmYwzcaGgQ7dZllPn7bL_tAMkqu-e8pnolZdB-Q-a6S4t4t_MRQdvzC9tEcOt7r153fqzATAH8LYRxtoTYUlgM0XHwMTIqMH_IdvxcS2oe0cyQ02n1aEQvjki0NWaxnrRN5V256yS5ch6xnrJnJo1ycvk2uS2MEvUjvXYooNISJULVTX_0ILL0iz-jyHamKmAPPmPccXw6i0CkTHoLu9aZhHWnUtG1tZkcqsayXmxDu17jTsRr3B5DD6yTk1vufypS2cbFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTwd1PZgtxyk9gR0BeLXT4HH9NJBSEv-GoWmPocklLko1kaf4l4DSkY9gdhkW4GEPAsm579GvpZ9_dMnFvPFrVpeK1iJRhpa8vifE17BpLQfhr00rnK0v9UOaUoQx0Zlns4m_NNYZexTlSsx5rUDY8aQqpxlf5sA4oFXATASdDNmK2Y98zhpHZzBw4lp5UK___g91VDmTjZrzpCws2F7aCKct5QozVKtpMYQioNYpZ6C-NTK39I3tKuP4DiY7UNvire5mXpaJMGhznMxllPphfuXZt9XMFn50O2x4KQy8iMYXDSodh7H1RsaW6fBRE8fReRavSpm6NEm0AAXNKTUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqT13RyNpxvUyZxQNFhVYfQBzIKdeLIX-Wx3tewxuP5oCuimFJi1Y5a4guXAEES5e8XGvOKKLIw6w2W8sxvWzUSm5sgZb3CV8xBuEDUFtVGBC3aJbm5RpA5rbTftS0PZVXW4nKbJ6L9AUlmHbvEORdos0O3eW-Nfzafm_GNZ9Zcda1j34Kw79jObwWkAc3s9iE-X3J8S8mAPJbf8eKKGzkPWaMau4hePQz85wBuhjEi5wb1F61e75ikqXinmHFmfe2Y2IR3XR3V5HrAwU2rrfCqvW12n_87wCDI-Jzb022Fh9lnpve7BsPj6WTy2uSRtmxHaYXGebIsa4ghxxdVVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXER_l-LBMLiXUNB33fB_pVLho1N5j5geqD5iwZNSCRZeRaXcPR7rODAX_LnE_Szi2zKRCO1dAeb4GSYNlF3ZuMKP9cIRsGMs8d2c5GDwFlyL0NqOO1s6CBbPzwRGKpBL8VALtX01MDiZ9uC0mw_7aNYkVfOFsbc5DANIYPbEomTjZs29DVOQXCRKvXTLxn5HkMMkcvfugzA4UzisZck7ljHcJr0AnO-3h8jTuHpVBd8qqP2r3UZYsqzqfsRbZqv82noRdl9bdBw-jZEky-ZpfyQuJew0FLLrHYpMZVyFdf9MAtj1nOVqLTSKvZXIDACEBt5TJcrjxRta6sgm1PiOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtlnVwf7T60B8fcMhAxJtSFOf3NU_d_ek4ZOA7GUXa_nm6HbrxUTtg3bHzs8442cdN6Nmy4aEBsqtuP7358b0ARijpxGLAeD_2UXDtbiAnvpnoBhuGTnD_vcCXMcLa9k6edU9cxFoQQ90DDlLwww5IHlpUgqc_XB-IAT_9TKcsDV3u_GK8rNi947s9Q5_6J4BL0ta492IR5Jq5yqKGSJye206mCG-5TiWump72EqQfZnpVqDEjaBxNAi3YWioKbo_Jv9965fZb9n1hASe5PcOjGm2OdND2hBFzM0yjtt8687nwtY351c37U2c8cDEE3p25U1Uojc9EqHMRadyVBDAw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Vm3fTQ95-x4pO9ySuRlx6eU77LrGgpNufAdqJKTB3Kx_G4uYafZ_lML2Vf1PVnxuA32n98zXCCxqjb5w7TTddo6nmhqoF0WNcw29JWz1SsjrmUnFenvfVwEMHuD-Z6n1ndsyqghkbM4egT00BZ7Ox-MODRYJG8rtKkavNgfeqV9eY8IGQRbAPdTYz_PejGbHwquFl9zUsthfBrVzPhSeSgzhrgCXfOo_z8HDibOSf8AIksDqrAPhW4MkvPpKSb0s997GjdCnjpdpJDnsxIHleZwhBnqqH3EkaA4vcfXTl67WpO9E_rOd9sel8OiJG5EnlufGfyxZa-o_maJs8RrWmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Vm3fTQ95-x4pO9ySuRlx6eU77LrGgpNufAdqJKTB3Kx_G4uYafZ_lML2Vf1PVnxuA32n98zXCCxqjb5w7TTddo6nmhqoF0WNcw29JWz1SsjrmUnFenvfVwEMHuD-Z6n1ndsyqghkbM4egT00BZ7Ox-MODRYJG8rtKkavNgfeqV9eY8IGQRbAPdTYz_PejGbHwquFl9zUsthfBrVzPhSeSgzhrgCXfOo_z8HDibOSf8AIksDqrAPhW4MkvPpKSb0s997GjdCnjpdpJDnsxIHleZwhBnqqH3EkaA4vcfXTl67WpO9E_rOd9sel8OiJG5EnlufGfyxZa-o_maJs8RrWmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCVV3OPFnYNxFoyIEgz_rcv3upW0JiNqHJWTqx8z-y0wwywhUz-je5BGH6f3UlZ3tjY4mLzReVRt3iK3F5Clbx3QrGNVn74oub0l_YgmwAt-p2kZrALhaAAI-ywh53v1i5sdopfG6NbMz0mDKk9tCU1DsDAUMWmdLErrf8zTbz-bjKbL8yCmPTVWb30QvXlOP63ytGAh8eF6VdEe6ol0GXt5MaIt5w3SjCYyvA_mWEAEAWPua8PDOXxEwNf-2Xgw_edVxEOx8VqnUkCjMoobghkpzaR8dVtdKbK6_euvgj1dE7DEVh5bVizrzZzuJOArgKWSCCcG6DRKHsmpl_ZNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMW81R_72v72wTrB0VZM6T4DLI4ZPw9dTXDFcflJIv4ioRSwd2fKhGJm2cO45xc3tSXlGxTDoFDBBZLx5aRlNM2F8IUauuVtBDBUhB2k3YnKaj5wdArC-vvjfRaITTOTJDraC5e6rhpFltjYJ7FctDDoQqDMpj7yCy8yI1QbQeuCk_HR5WUHUzEBMZTyRJOdLCeHvKMHaLGXTh7zDPclKbnzbnAQY8Y7I4uwLGtmlmVCKW8pJ4BuCrNlMUF8znQoP-ogSEr_WojjpACnjXtD0iPD7_E8Yl-gpjc6xb_Ipf6RVHsrK0gqLf10bWtBrAoigtmrjIyuFU8GyUGmtbSs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZY0t6RpoADeCWWORFigs7NRddULOpA-ve2oW1SiQe5UYx8LlQ5t7hUyq4pX8-ymagtjxDhRR_Aq4aFIOjLUwij0DFv5otQsNrdrbV_fBp2wZ0M7J4RKV0eMk-L_EVmS7Ae5s7HTAyhUeO-gatbOeGgg6ODFcn9LMnSHdwaPaZ9jNdIJuU7rpNGFtcukqUIru9wHVGy1GtkkwRe0wwmRZQ5KWRkTiibq8JjtDLdqyPY62IiM24Mcw5Bvmy5xrxYcB62bFC7PhKbv5jyw0qf3DZ7ulSwFxSqHd4jFOSJ7QsDn6prP9nNHjmQ3F3k_wE-TwUsLcTmGV4ma4_Ff6Oh2og.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=GlzhJRyQq-ZXf9AvQYuQruxdPaZLyq01RhC4Bmi-bh56VlbuGVSkPUNxA_EJFBE-Nh6Oru6ajxpyw3p9Kb1awGpUaTKT9kf8rDmRHn3z8GOLq-uikzFfg5jvbfv-BbdfFhO-n0QFPnQ14zlKeJMF6CgN_hB37z64l6EqsTmEO_Qg2oV2JZv__DHWPWCe3rzs_bpanCMgcV0Bln7nAj1YeA61m07wywso68pxcX0zSEGAftmCsa1HTcLkmgz-Ic1pmwGjQn2taRHhmL-Rjjs681SUpagPVzahnmhBAPan7U2roqAhhMSR8-8LacwSMd5YAaN2gjEKk1wzp5tu3KYasQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=GlzhJRyQq-ZXf9AvQYuQruxdPaZLyq01RhC4Bmi-bh56VlbuGVSkPUNxA_EJFBE-Nh6Oru6ajxpyw3p9Kb1awGpUaTKT9kf8rDmRHn3z8GOLq-uikzFfg5jvbfv-BbdfFhO-n0QFPnQ14zlKeJMF6CgN_hB37z64l6EqsTmEO_Qg2oV2JZv__DHWPWCe3rzs_bpanCMgcV0Bln7nAj1YeA61m07wywso68pxcX0zSEGAftmCsa1HTcLkmgz-Ic1pmwGjQn2taRHhmL-Rjjs681SUpagPVzahnmhBAPan7U2roqAhhMSR8-8LacwSMd5YAaN2gjEKk1wzp5tu3KYasQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyzW9exC0sqvM0fOAgFPKH9D1PFHU4bux_TLxk2RGXTUi5MjZUJ_VD6TfLoQe-877v3YsyD02HQBKdNiW54SVP3p9u8010p-CXpRLggyei8fBvhPG1zmTjl7mOzx_okL2aEKzSZDNSg3PoQ-V00O5DzYVCpdwZJzVrJakNxawQp4cjPYdU5EnBgsfvMkJHSQH7HmRaSexXAr5ie3IzI5quOmpqDEvJqwZYmXfQiZLbccnYE2t0RGK1kYCKDu3XYM9f3zlqKq0B3GIfptzUbORCaiIPgQuhEgZpOyo5BzEhctyXZhvYnY3EfQJJjxkcDljk4Vl7pYcz_i0QqYrzP4Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp6Z5svGKvHJhOLlhDCdgaECCLFGWEF-XCUCA1SiWmXrIBwLTKCUTQV61ONLW7_RZQD_Fl-_psqF7kuTRv7a2J6HOTnmDCVc4s-mvFtEUOu00jx42QdSwz4zcLpONaAkvWV9L_Bp16YTqkOOtGRQpyDLuyLg0kcRj3hHwyCX_EmkJcqXN_OAICJIl96ZeHzHzWRrRaRvsn2Cg1aQgL2bEI4UG2plGmvvkvguHd2FefMm6sahcHCO9DUUQ23zFtSu-JRJF-OGweeeFMPA5VrRk-Iwmfh_28M69VQxIY3loH9_tLg7A292gpKIMXWiTkBkKa2wm903ANtztEoywAMiHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LB-Yxn2q-oCMRcNgf3hd1o1eXIhGCwKVKKjQLRcj9e_mUxc11P4pXob-SpTDvGXxpZ6MzuBfIo-cyF3GED5CAf4HxbAMSEUB3RbSPtE5oRnCDPMegfQzn50JK7eAShqrVXWPG6ucLPVyAl1C6O_zpM7_QB6cViOqYntYsRV8u4F0X9qEjvPWqTzShx9lqHRWyOvYRs1saE4UflwNbe5gU1GOIH4fcthRTTFQiyv6Cc69iNbQ-vDymZQnZ3BctL_JnQUXhdN-lyYTI_JfWnZ2s2w0fOxoHDbal2X0YDf-V7Av1fKebx4Xa67Jq3eNmT3yIcOxCuA6MYF7x6SkFNIEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipgXfmAqnq1eZsvtVEHTDk4nQOMjozNQbC5ZuvWQUBXwCyAetKsqF3ab_foPJWqid4UTiJKKID_0MOn_37AWPKSu1NKirkpFtOL2d83RYpPFj9N7pyIQZSpreBOjRzM3B2_RhTWQ-C_XaZK3tWRm5Vz02TYXoawbUzfrPoIIQ6gGCSPe5u7wyLXcQ1GjS-XZMH95fsKizhAV7gWTSu1M0JJPMqgrWgHJGbwQnBZvynZbMJzUmp2pmihfgmsnsm5-JZlJFQjuqU-vk3mIx0mK-PfLgFFgPPZ1e5x5VV9BLn-QcSKtDcbSkreAirvBY7M4CPe6onkgANDfC2klOVGEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SO-3hRB4RZMEm_0LahsD-6aAbE1Rv8EH01Tlv_w6KqkOFggXs7LgB94STfK-0kCehvQ26Tm6lj8PdtwEPBlZmkhNExlOR6vP7q5G8WaBcsDyrCxMptngZ_wjZF3xAb_zZck-wwo4fFCTJ-7ej8NzpdXQ1IrBb9fz50orOIKhZ0VgKYmZtlPX9f_uRMRNcgTHmoc8OWbRGdMP-JlMXmWfGMHhBWLfnVH9PejbBXlrvWRup4o2YkBTFKyMODIWDDwQbIuC_-ro0qYa0SotBRD1heKu8N6EMSLRDSg1Trd3MGhH8Jy6wYuAQ8BfM9-GiMGpd-ythoeh0tzt9t6LOh5vXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJCffOt0Wy4dVOcttMEAcwuKPImCDPnhOOUpapJv4SzordTlcN7_Y12EcOB7yqHFdS9uubpV-nNS4fs_VomA1-RisU76E6k5LvT06WkkvEbwfHxEhsvyJ6jxX_TPsC_iRZF_VIlk-yPijEIC4MoW97hJPYYOWBW7-9yshOWO4OG_53tJh54MKityZ06gc3RjTAfhl5rDGxDDvmmCUTR5yeRuXTBHH2TifiWdpVSYXOFhF3jd9wdZDGxZWbQ8CafaLhobIwy8ZeCLodaZ9c0VF85mSBRM2Pjj63vJV7ZZQknSewmt764yHs4DdeoeI-55SDGTq8d9laBBlm8o2PSeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VOAvLEqPe3Z8Z5zMItYqs_ClSZf6Ti49TwB3F_Hz9_puJKhrhJqMgSnukMcqht-DuecO08tSjW9_uiU59RxneXp428b9RX80T0V8ZB66OX-C1ROWZOE81ubcBwT2gdeLosFfj50ikVWY17GsP-aWjeTqKCPX_c2hjI4IYIJL8ql7kvR6veupjKdN8TeMiC2l_nMUhCWmVmHC1EKX3OCBin7UrLYSuUmxpMVBswI5tb1ATl8IgizSVWf5mXeUYzmjpwhjf_3-VoY8gGvbcES0038oGeng3FFchQZRe2_g8ivll-iWvsS1B6Apr-qYZxdXLAkedw2NvmoOeUtw1Xj3HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfjB9Sj6u8QKUOq0xM5B85QG3JlbZiNYnblE-LRnjxcsa9EDm4-SJhZBMqpjiLNl_CYwT6ysbydv1Tu5zcd4LakZL280PlYDxX7mPwu9gddh44EDt8O6bRjkt-OBk8h9xWLtxB2twXJ828clFQTcSXRpkOSiloedzaAFdHBbPxOTzku82plGaR7amtdkEa-P2K0Wirq_zvVK8Drw3aJqUHW94diIQdMZh_FaAXa9vMU9MtqNkqcM9kRjaBJ_EnCyfgyeYInP7Gsj3ihcaN5-YNfyieKs8rRBGRhkVfM5VriZVEv5TnN6qulrEY8toouaerbcxbWsCe376wLOWJmdaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKQocd8yitWG2hCu5w1RMA2WpjlWMgfbQlqqtvqFo1ii5hCeGQI2ibWlrYLaZZowfxqoY2vFnWK1tI8vc5cJjAz75Ld8AYPPdt-O-nY41BWlB8yUIqcALjRwS0k68WxZRKBRKzpLcfflt4CYG697sarBzDNfSQ21hM08XusfkKuRwfBoNUCfJCI5tNbkYHeg4FULTkfkmuPchwlysDF3_G2_Hxi4-gNAISTHICpJZg7fMYqtvSAJ0R-LNpV7dPpzl30AUCq2XD8L_V7_kjS5fCV0yMVvEaPJ2X_i4rRSPAgKUypWmdHjApSY6d4erubl9CzrGy_QW4_yfXn_9Y0J_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqoLXWpOxzHT_8tPGAKrzVZ68O-vzG1fDNOaEFib8KHsJ1s6bszoR5HDQpJqOg3FhjtJqhmkXMWyClDLeNeanziAeyowgTLfgR9ar82tJOeWnDswTuJL8BV8A65YNUiPtcbt3qkouOOn3ZY1KYPJJa9TDO_tvOphFDl-GPDrtDAavGBmlFcFW4zzbvWF5iRA_CWbfhPVniYs4sUOH-jEZP363jKhA53f4go4WwKaFqSpE1bqx1stkDaUUhO03tNNZyuBf-0coJvX6MUoOEFgKQ7EqA4no3lKUSAawXCJAI8KUUCRtCPIBYVERXEbFh3nTCfk9n9EqQ1xW3JawUZ5-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXwa6pnZyIUdLpuqhqc5SqGRF4yPDwMPno5wmmjYvoAp_zZ3L8tpix3F8PDzilDQgZ7AwP-W3lF9Sjz7DHW39oSVwXXhSMjJNDLJN_d-a27GFL4SYDYoKWtRMdSn948Oi5JDnJpW0jsknlXMXnjX5TEvf7QFgYBGk_7qMxylx1dwMgJksuXcRUBVcbAx5KXvXjroNV6sr6R91M0G5qLUv9KENhFL18ah7t_88vhPT5bMiiQV1X0J15I-lUjCn0JrtIgUQXX8GJqaH-OENHaNljUuLPf05XCH1fwFpNo9LXdW0HY_PEouRqcEAhgAP0l_HJtyRD5_xUIEE9da33Lvzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DD7iacrgvAY_GqZZnV2fQ3i75BWs5IJcbWHkL25uQk5K3aELr6fe2PgQd-rTSprGBXR8jz7N9GN7jW98SgxzlEtRmX-8uFzNSzdEKZAfDugbPT3IMLifE8d6p14c3l557v50ab8PAIPolUsAfwQc3SIAPQZv22xoYGHmlkxzuyBPaagLn6KFu8Q_tyRUodT6tb2AMB9ToL3o_lS-2j0jBFNewiA2OM29xUe-4wgzlZ4TcYpnHKpTr9zUzAOuSCD1DQzBIZj1x6dSITK1LoD9G6SrwMisno-GJkCPujRIO0fiy8ERPT4YWdMA2BZJffNgzdEGItvLNjU0zHVLkA2Vyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE_PW3qf3r3EdRe_8y79y9l7kuop-3AWfR082yGzb8_ATHneROQr9078Dw5MwZLXOUdznvFvVTmFpQihCKsxcp7TGCfDEeU405WDHlLOEJR9iu78FnCP42g6oEeaApFShXCMNCY6cI1XN1hIz3Mc4ndbQEUzVMLgwLOS6si6n0P0UAUDtk1cmDQrs63ToN7INowaK4nl0MyHXmZEkTO-Hx2S09ZqEfjCdc1jlqsKFCMyVS5Y9bDR0dOxTtMYmxVxreM1jM2vmYCT44fkfLnhGB97UoPYxIxV3J4HFRU08fLKX6HyySmrpON81mYcQfkDABPal0gCU0IXzBv0Gkk8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXCtWuBRyIiu0jwK1K6qP8ictP5pXGK8WdutR_l-izAOSccdNd_wXNubc8L73g-KOUCjsITveLNtqW8XkoP_NoGKbNxu4cpqZ5xg1L2-CDxX6GKlRGblhhcjhxU7G3uxyQJOt8tdb0J6A7aAdsEQJQtKQhMhl3TIgBaA_sMBJXqFNA2SW4IxCtN0SFLO-YE3NNq7T2Y7t0o_KhHGn0Kqira_dLTuDiuHcmB6zAQ9J7UHqeKyE88z5EfjL7EhjXmloEwDSAaBPkRO0hSQa3M1NWY5vsysbXMfP2qkvflz7KT_CFqZQNSyaE3xb5ABc-qogAPxXb8zmO8F5exOv01bxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQcEyWLnqy2QjUc6bMwnbL7SY6D1WqKqwLa14xE81tYSCjO6oN7KMCMWDjohX3A6t9S21gpyc6T3gIe2ngFtB6b_HAvmv1WsOMG0Xg2i1jRiPzGKfwKjyYsF0SKt-IkYvD7Ncx5niqnqJX5in67TTQVG3F8m3sdLjIl_AMxN80fpbrW3dUsMfZS5whbe_fPgeDkT3Ye-Pf7gpCdo7u6Hom_1JLlt0HDSblLfo2i9MpkLy1Or3TDQB_T-4js8qa12ge-LxferQKHry-FlnbRX5Zic54LzPjnk2snHD-dseNF45gjctHqRRZTwVRAdwfI892DKNshkXy0AH7h_pl9eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=bs1JgYXFZ-BsYBP7SzCX7jjiOFfKrAIK5RX6bc7LC1KT-mWDTpmPpzi_C3ZOmBaLRd3Yg4_BmHAvZqXZFcCTlg9aufu957cxOvgTbZ2sQ0B9Enjr2zWjapBdPmUIW-WiDauIyLj0XCSrx6uDPfDxQ9IaPBWeqV-50hnel43-RsAwWRgl-m55_XPJUxi502ywoZOAXs50RSKqdtiy06ARp_zqzqy9yR93BXntLY29rHj3w238r-kIl5hLvQ-UD0A5pivrl_A7rG7MmZiBvbiOSGr3QsKoaH592a6AyZajRqM0YkBZup0wHEPIEM26sw0ZWBUtobuxfeCPcK8NH_1GKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=bs1JgYXFZ-BsYBP7SzCX7jjiOFfKrAIK5RX6bc7LC1KT-mWDTpmPpzi_C3ZOmBaLRd3Yg4_BmHAvZqXZFcCTlg9aufu957cxOvgTbZ2sQ0B9Enjr2zWjapBdPmUIW-WiDauIyLj0XCSrx6uDPfDxQ9IaPBWeqV-50hnel43-RsAwWRgl-m55_XPJUxi502ywoZOAXs50RSKqdtiy06ARp_zqzqy9yR93BXntLY29rHj3w238r-kIl5hLvQ-UD0A5pivrl_A7rG7MmZiBvbiOSGr3QsKoaH592a6AyZajRqM0YkBZup0wHEPIEM26sw0ZWBUtobuxfeCPcK8NH_1GKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c29ythJeiqiAiFRHF8P-D_cn1VKjpj8xs69lrF6LwHcArVpg-_v7GclSlQdjvA1ysnbO3QAaQW2U6JTMwAVFT00_shaV7UGWqIbMJ_tzOilIbKugQFwYFNcM_aQX9ogXabEc5zCQM1BjWZ_HATGFQeX7Cke9ia0PrrcVEZJZH1GV1gGoGzYJ28EnqjnGvWJMjJiGMfa-7tSQU3kDBXjh509JcjYtX09PCHsFkKc9g9aKRbUU_wd9AjX29ihj39nLnAmrCFYzjxL-EG4vwK1cd8QsDKbEs1xdAvQb2pcDnyYmKU60JiHx5XsdRFeMBNVc2l7A78JGicICKGLDZINliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=Fp86MG5jt1AQST1aQ_LtX61fGDW8S-fX3uc0FxHf3laWPK2JnFf0ue8JthRZHW05GB6JvFC3U_hy0fggdHdlgzHZ0F3aa3qQZR1WLSF138uh-hU36V-XDmGslY4i4Sn7gNKtzuQuJtNsG_pqZWabxUXb5NbQTBPPSEqwqknYP8Nv3KSfA2mbORKCVObLwOaCFPF6FYRgo915HreK6f4swCtIiW7RdMQY4tT7nnYoiAKhGVmnusHI6sGe9aP77wGyt5jR_H1TvOAInMFbO-O1JAciI5-b8vSolqrcQkr7rhmDKTITbOac65CQIJjdOaf0xjuMq9MjwLBofXPSEukH9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=Fp86MG5jt1AQST1aQ_LtX61fGDW8S-fX3uc0FxHf3laWPK2JnFf0ue8JthRZHW05GB6JvFC3U_hy0fggdHdlgzHZ0F3aa3qQZR1WLSF138uh-hU36V-XDmGslY4i4Sn7gNKtzuQuJtNsG_pqZWabxUXb5NbQTBPPSEqwqknYP8Nv3KSfA2mbORKCVObLwOaCFPF6FYRgo915HreK6f4swCtIiW7RdMQY4tT7nnYoiAKhGVmnusHI6sGe9aP77wGyt5jR_H1TvOAInMFbO-O1JAciI5-b8vSolqrcQkr7rhmDKTITbOac65CQIJjdOaf0xjuMq9MjwLBofXPSEukH9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=Sd39dhcJJFjYRF2iehg-SordshgEe5I86-dP_GB3GyNQSHEqB_KtnLChNP6LHrjYqaPngIH3IWZWTgAcRXKLEz7d-LORajhTLgCnsQ7TKVrzCmd2G4eesaxINwr4K7sZolIla2nqFl88oZtnKrGQI6FK0qvO5H0BmDaa1fIHJ375myMKTOpx-PD83oBI1mpwFie4xUOp1l_tKwb4NQBoYwWOaEcRKk9w1Z3_lwnQm4uMKwRJb5Nu9Js-diByKYzRWBLFVkzaBH7RmT7RQupXTIvXTHVtG6sco2W0NCAObfMVi0sVykYuXNTx1wOqD3uRosOa7m_4FqrxZOoQT7gGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=Sd39dhcJJFjYRF2iehg-SordshgEe5I86-dP_GB3GyNQSHEqB_KtnLChNP6LHrjYqaPngIH3IWZWTgAcRXKLEz7d-LORajhTLgCnsQ7TKVrzCmd2G4eesaxINwr4K7sZolIla2nqFl88oZtnKrGQI6FK0qvO5H0BmDaa1fIHJ375myMKTOpx-PD83oBI1mpwFie4xUOp1l_tKwb4NQBoYwWOaEcRKk9w1Z3_lwnQm4uMKwRJb5Nu9Js-diByKYzRWBLFVkzaBH7RmT7RQupXTIvXTHVtG6sco2W0NCAObfMVi0sVykYuXNTx1wOqD3uRosOa7m_4FqrxZOoQT7gGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5Z8FjIwWtXN55Pd-vod3ktxxEdH8AvKSnOORqbmxHeThr23OqHoBR7qKSD9GqzPllG-QcPWUA7cGnWb6ByBMxQXNNwIfdeGNaHz_0ZjmlEUQWv0p01U3gr9e0-jbuB2VctBza5AMcVsM9GSLOYIf_HsUFwagYDHlw9qV4GSkr30SXlrdsiWgxA-PU-WxcYGvD6GsQtBPhNgUi6Chhdnzl5JGr31mrEZMkdcYmWgyqmpCpW6vBEFyDhQrJIyLYUiffg-_At5zIMg-tJLUkYgrVOrXVZzbW1HKf5KdgyMU4GRWfbjaritZytkXNd7S1fK7QxnpK5WU9Q_0p7StJ_ivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=gXfcRAP6FoRGpX9850ls6RJ4qMQiTylhCXuxHOCy86AK4xR45QmS0F3-t7cPomESj4bgw4yxzzDtM9fQBwYon-BcrPGpVkAC4gchZnCtbeGnfg-ctL5S6wxf4Tn8BWVVsrXRnW3L-GhI6eiMZS4IwBkLmIYjJmRuwN0cEvSwTw5MQnKQTok9qN5_cR24Osk-6K-GT8T0nIACwNUOkKc_pCS3AfZEvl1QLAQhGPxJ_VODsAF0efVkKTQRZVFdSbUPdlaoqxWM5LV6OM8hhHLw-yv15hhlGZF3-o_T_Fk1-fE0BLRapk99ZDkjPJAaEcTSFvp2RRj9qQOcDEaj7ajPfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=gXfcRAP6FoRGpX9850ls6RJ4qMQiTylhCXuxHOCy86AK4xR45QmS0F3-t7cPomESj4bgw4yxzzDtM9fQBwYon-BcrPGpVkAC4gchZnCtbeGnfg-ctL5S6wxf4Tn8BWVVsrXRnW3L-GhI6eiMZS4IwBkLmIYjJmRuwN0cEvSwTw5MQnKQTok9qN5_cR24Osk-6K-GT8T0nIACwNUOkKc_pCS3AfZEvl1QLAQhGPxJ_VODsAF0efVkKTQRZVFdSbUPdlaoqxWM5LV6OM8hhHLw-yv15hhlGZF3-o_T_Fk1-fE0BLRapk99ZDkjPJAaEcTSFvp2RRj9qQOcDEaj7ajPfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnW2tjbV3Mk9bt-7nmuOQkgwrkd2wtsEvrQzJFHl64_V7E4AFr_eJQAXCIHr9_P29omu_YpdShGNu5xrqP8VGQ2dcj5lat3N3qKpNB9Tp0bzALHEO-p2j8XihrjdFqHhfu17oAagq2NFOH6qTaHL3j-hcnh5zTNZzsq8ZlPkc949_dTajGj5Vbg6cIEOmEipkhK1nlA9PJSYKM2vlPwGaziSbPRDp6B30ckoGN0bPIlPxOi3HJedbVgcHoy4MdfxX_rnLB2W8KZk-x6xcrgv7Kw8FOXvyT2iIeW58H932ANin4TQfUHNMIkioPRQPldewcKlXjLvbt0BqrhYBWHv9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BshCX0QUdTS6w9QHkyO0xfD1QWMtmAKaNJT1i8H9MjRkpB3f04abRp3dkbNU1DSGrn2UsMi2-sMoCqKD3Z8AuJru32S_RQ-J_zRQxM1hdzZtpqQVgV0WlnCSWlDbPFUrpzQ5HtbeKBskuItMbJpZ1zl7FaNf9Z-WdRAww815uzoEVr2B0rwqsTEy3w1DmNV2kndNQTARD-hI3Gt7LHQIMIRRCggGhrFfBJ0AUCL1PVORn8LIZYzXL2za___WhS6J-4Zn0MGBxt-gh3bjjhiPDAA0TNDKxQ9iBy9KGCDTQjGdaO4Z8JYvjclGuzCfbL0f3vngt2P-tx-YnU8ODEEoUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDfYWgw4C96eYMCJ6FKwZ8JtIDTIUo7bqFNPwIfX3VGaG80VykD_qWG_lx3J4vhcKWG4vdlbsrH9T68iG6aRVzAQH1sFRYJb0Bc7zCgU9_XWePTGfFgymqCUc2eao4rPJjwoYmxeOukLDjgDrsZhnvMXkhfToPYYYZfpJ0ZKhiy-hc_LTfyYHtnMUtl68S6BQq5sPqr0ZrQzi4CjyPXa1ogGmiocE4CcJnKa-hQrfNJhSby05hA6rZX0k7e9PLOPIugc1tMlGn4nG5qHgkZpMiaW9mmDdW6HOvUzpBgRldgRqwYzhcfY3jqnZJjT1Iw1vCBrVJy61JIrnUyEUmz81A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwZ106BUtfuTfso3On5MHTks7x5usX2wQSbUFrTzsxKscJ6w9-orC4gcDQUCPMgVXLqBpn3n56AHwVONAePJRuLjjTOSCk51WpkKtWkV5SyQcB0L64LIrHkyUpV1FeYwyh4URfDugPyoEbZ8tRLpqMAfvZ8Aln20TtZF8OaWrYMF1Q-Tc7oXiDI8LFaR26-sgL5O0VYk-0aQ-AmzG6pG1AWlO6BKK8lKRnULHlHvAJtY61XAL9XiSzz0u4W6CvOdV93QeAsaWdcAdxJWmnueslJPLqxx_zO5EBojEZMUfBvFzMgGcSb2IyLag8k_zcUmxzwZemVPmfpd7aN1Yah3Rw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=bF6Jmznl8ZesEZZirBvsI_RnQncz598oCnTjav7Lr9k1naGSPxRNnEDGxoeolgGUB25g5To079UKKY8MOG62gePTO5ahj_CCMZc3wCYLglqB9xwD4PVbQC17n-Out3BpcPbPKlPz-dg93PharlrQvGwxeB7fs7JezwsCDKWs9l3xJ5ZeNK_U3xIQ1MXHr26uuMW0i7oNUNQVKru6_JB2ZAPpDRgUcHOF4iuNTiGyuuPyZ-A6RalW8gbvGAOEFbkofyfYdxU2ufwEqf9n_irE-8YQMO_trdqm5Dz3Eu2JhAhDuti2DA_lj_z206mxFTXRgnnKoOVOuhRdHfxWNx4Gww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=bF6Jmznl8ZesEZZirBvsI_RnQncz598oCnTjav7Lr9k1naGSPxRNnEDGxoeolgGUB25g5To079UKKY8MOG62gePTO5ahj_CCMZc3wCYLglqB9xwD4PVbQC17n-Out3BpcPbPKlPz-dg93PharlrQvGwxeB7fs7JezwsCDKWs9l3xJ5ZeNK_U3xIQ1MXHr26uuMW0i7oNUNQVKru6_JB2ZAPpDRgUcHOF4iuNTiGyuuPyZ-A6RalW8gbvGAOEFbkofyfYdxU2ufwEqf9n_irE-8YQMO_trdqm5Dz3Eu2JhAhDuti2DA_lj_z206mxFTXRgnnKoOVOuhRdHfxWNx4Gww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=JrVFYejg9XmKGCnuxomOk6JAxtr0xuUnsjyttrqYY8fFnjz0NhaxRNqWZuwrCXbdZSUA2IrNxdEvX68FYfFmRUZEp0tUEH-oy8IELV0v6Sdw4R1KzxLG36vOiI5hy9FdSEH4XWtf4XU6G0ah74F1ZnNEVjQ1Xr9JT83tA59jm8kIc5dCUrIqtOk_xujwthtbZfC2EsXtsy4m1YNf3xQiWgSYionTnD_1vExjKp9CsAkdT50pH60_dD5pi9nk82SRRIjVSyU89A7Us1mQbh_oLP_vRx9upS_T3VbLiiozjtGzG-wS_xzOw2YUJH4GSGmmogKkJdmII2xVGiq0ers7qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=JrVFYejg9XmKGCnuxomOk6JAxtr0xuUnsjyttrqYY8fFnjz0NhaxRNqWZuwrCXbdZSUA2IrNxdEvX68FYfFmRUZEp0tUEH-oy8IELV0v6Sdw4R1KzxLG36vOiI5hy9FdSEH4XWtf4XU6G0ah74F1ZnNEVjQ1Xr9JT83tA59jm8kIc5dCUrIqtOk_xujwthtbZfC2EsXtsy4m1YNf3xQiWgSYionTnD_1vExjKp9CsAkdT50pH60_dD5pi9nk82SRRIjVSyU89A7Us1mQbh_oLP_vRx9upS_T3VbLiiozjtGzG-wS_xzOw2YUJH4GSGmmogKkJdmII2xVGiq0ers7qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=E2UuHFkmbjX5OMfkuI5t0b2MIq520XCHovNH5BCrGaCVbhFPU7vcQEjEVklDMqbaB8vyKoC9_GHcfsssGE_7RT7-4BShvt_yMipyeaIlCAfvyS3RnQeaOg8oP0GQNo5-yclzT7yJS4t3uTu9bX8519FWSHjRY_fB4mIph3wAUDkAfVVqSKLgushshOKaMZCz2mOmyUt2uCibbhDG-BWaMwOZag_6BqjV0ZqlmqaTt4vnv_UwKIs6E93EAyJaIIJ0VM3WFKa-NdLTDnFOBlqxj9JLDgSz8mzo4iUHzLWPW_ZkxqBRxnOMZ-1jdK_z6CaEEAY5VWnEZvJt8z6-lzk7fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=E2UuHFkmbjX5OMfkuI5t0b2MIq520XCHovNH5BCrGaCVbhFPU7vcQEjEVklDMqbaB8vyKoC9_GHcfsssGE_7RT7-4BShvt_yMipyeaIlCAfvyS3RnQeaOg8oP0GQNo5-yclzT7yJS4t3uTu9bX8519FWSHjRY_fB4mIph3wAUDkAfVVqSKLgushshOKaMZCz2mOmyUt2uCibbhDG-BWaMwOZag_6BqjV0ZqlmqaTt4vnv_UwKIs6E93EAyJaIIJ0VM3WFKa-NdLTDnFOBlqxj9JLDgSz8mzo4iUHzLWPW_ZkxqBRxnOMZ-1jdK_z6CaEEAY5VWnEZvJt8z6-lzk7fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=a7qgja0zN1R5vJ3v0fLLkBCYworW6Kf_pgW3t8loA78mSqtaVLZJMQ5gRbPPzu-FIEOs_7dlg17AmRsyI-tXwwvMUcDN7kLoBK4h0f9qCYexYNGuacbbqRu9jxcTiJr-6RFdSD7qdrG8HPVUDKfsMC43zy2SNLdEO09-N3-F2R12Zcm19oAXfOnBgInHQjdiNfFjcQb7s8ni0RKfWdPtCXBhc_2tjSPFt31Qq6Iv8WwG6LZqYndbjRyv_fKwOmZsXGEh9eLep48vC-dB7OkLQ229qijw4TGprchKzVr_qEYpvz2cu91rPK5Nor58E29FO6lesnNBBxzJT2UnRYtEWanVj7_RsHih2zEiNqTUNqGUZff298mOtMe49o5aV4EZLe5RzLJX5vryw2wHeHt_HiawrSxkG2MC7XHCdlrTcZ1sZaTRQsCVWHWSqueWurod1Z28aQWnty8f2xsEYWpemZEzMHTeCnfUmTHrW1_JPg_9-MclVsKEqHYVqlvtUALGLC4FnIGLq92HO5mm4LQC4ACu-6fOtXZMH9XSR4ekNTjyyBinnPJ_bqnhLaQYtLn3R5UHgXnvFMa7fyMkeU7soscfH_GKKhMu5w6_Gv70U8d_ln7kWbOYAldLxIpWEuU2ggB-5Ljd1Yo7rBFhZXsm_zHrBz_JUDmaONILGsNCRj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=a7qgja0zN1R5vJ3v0fLLkBCYworW6Kf_pgW3t8loA78mSqtaVLZJMQ5gRbPPzu-FIEOs_7dlg17AmRsyI-tXwwvMUcDN7kLoBK4h0f9qCYexYNGuacbbqRu9jxcTiJr-6RFdSD7qdrG8HPVUDKfsMC43zy2SNLdEO09-N3-F2R12Zcm19oAXfOnBgInHQjdiNfFjcQb7s8ni0RKfWdPtCXBhc_2tjSPFt31Qq6Iv8WwG6LZqYndbjRyv_fKwOmZsXGEh9eLep48vC-dB7OkLQ229qijw4TGprchKzVr_qEYpvz2cu91rPK5Nor58E29FO6lesnNBBxzJT2UnRYtEWanVj7_RsHih2zEiNqTUNqGUZff298mOtMe49o5aV4EZLe5RzLJX5vryw2wHeHt_HiawrSxkG2MC7XHCdlrTcZ1sZaTRQsCVWHWSqueWurod1Z28aQWnty8f2xsEYWpemZEzMHTeCnfUmTHrW1_JPg_9-MclVsKEqHYVqlvtUALGLC4FnIGLq92HO5mm4LQC4ACu-6fOtXZMH9XSR4ekNTjyyBinnPJ_bqnhLaQYtLn3R5UHgXnvFMa7fyMkeU7soscfH_GKKhMu5w6_Gv70U8d_ln7kWbOYAldLxIpWEuU2ggB-5Ljd1Yo7rBFhZXsm_zHrBz_JUDmaONILGsNCRj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=VLUzEniKeRbEqyMllu9I_SoOjlJIVRL3FSeMkOyUI7K2cCaLWokPpkkxtrEDHezYYiE9vlm_zMaOXlJ0XjBhU7n6eHePCJUi0ToUn5FbkoscNDjtDNkr8eKt-etAMjoDvAlfFMYR8eXDQam4HqPJ0IRB5J65YUJQfL8ZZOHVAZdtZ89ZgfRCr8TETVXIr6sKdyqWVfg2UyZsljlNHQTLVvQ_2Ichp7yS11jEIDZFaN5U1EuXrHCQRGXQ8tq6xG54Zap4pB9QJ5PVmqEo8ZrFweaRLT5AEGbi4h0zOQqsoIoQz6qYHhT_J7vTrwGh__JwpOsN7VWAfnCl4te3Krd4Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=VLUzEniKeRbEqyMllu9I_SoOjlJIVRL3FSeMkOyUI7K2cCaLWokPpkkxtrEDHezYYiE9vlm_zMaOXlJ0XjBhU7n6eHePCJUi0ToUn5FbkoscNDjtDNkr8eKt-etAMjoDvAlfFMYR8eXDQam4HqPJ0IRB5J65YUJQfL8ZZOHVAZdtZ89ZgfRCr8TETVXIr6sKdyqWVfg2UyZsljlNHQTLVvQ_2Ichp7yS11jEIDZFaN5U1EuXrHCQRGXQ8tq6xG54Zap4pB9QJ5PVmqEo8ZrFweaRLT5AEGbi4h0zOQqsoIoQz6qYHhT_J7vTrwGh__JwpOsN7VWAfnCl4te3Krd4Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=FX8Lf-cagO_PNzRLTOMzWciSH00gW1uGBZPth9nGvbUaZMMwR_MDM-FXriBTZskHRiy5QVL0TkpWPvCSyCUTEC5x96DnRY1DUzXd-r7wfrnUnbOb4FCK9nJd2xyfCLZHOw5B87TQsJc_qsZsKgZAuurHmBBz4qlZixmARdpJRdV9VkvqsFn1RlXhQ3VxHP1A-UwME5PSdxMEbarC1xP_BiWMcYAfT-g2Oj4HBXDG6i5Caep7bZZbJCc1mYgKsUdOsruNqUP0gGSYUQTuW2BbiTrYavOH5lJwsBdwzAWzwzKWWMvPS_Jh5Gtoq-WMZXfM5WN0TGWcwJuhHl3w90kNdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=FX8Lf-cagO_PNzRLTOMzWciSH00gW1uGBZPth9nGvbUaZMMwR_MDM-FXriBTZskHRiy5QVL0TkpWPvCSyCUTEC5x96DnRY1DUzXd-r7wfrnUnbOb4FCK9nJd2xyfCLZHOw5B87TQsJc_qsZsKgZAuurHmBBz4qlZixmARdpJRdV9VkvqsFn1RlXhQ3VxHP1A-UwME5PSdxMEbarC1xP_BiWMcYAfT-g2Oj4HBXDG6i5Caep7bZZbJCc1mYgKsUdOsruNqUP0gGSYUQTuW2BbiTrYavOH5lJwsBdwzAWzwzKWWMvPS_Jh5Gtoq-WMZXfM5WN0TGWcwJuhHl3w90kNdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgKLLh9dWXe5HsJhGbfvoHjxerIlkR_iVuI6CoZjNwoNDjCl76B-WLyFXXim2qSUyTm2ncADRoMGkw0rjOEpPTDU9CZH_tTMUwCqpEDZR6vdMHt5785ICVNqxWh76LOGxvyxjYTTnyusE_tj3XlaiyurMk06EvYxaFCy4XMuD3mjH4bostrYpXe7gA-KJnZua5Dy25wMWtVdYR1m9ZqKWEtNzI0UXSNpdgwbvxXL8LBFfFPFU4P6flIOyIt7IihaycO4HSxL1p-vRwSgDcub4I99rU_-eoe-cw9MxpNk8JfGXEBpqqKLXsXC4oBUtqbTGUj4nq827vA0IUJtfwwYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=AB1afMjVqthBNEeuSr_LoyBJ0BvrrK2DrB5IOkbErVPOXRdC3BCgl-krYa4CXWBVbU93om_LXhyhy3bYZRPJeBPGwsPEanVF4j4Uapj6mLKpxNP6nfFYMHeLevYlNIzuoGtHMzEI4CFw10NlECu1CChlt2cSawp5xPkP3mKvR9y-P5OsDoS-x4HgrKCWtGkFhtsRvQWyPti80EZqxsmTg2zQ3Y-zBB_otbOj-Pqv11gQovQN72Eakhd_hC1fCtlEFuh8ukp3XfL9Boq9m9QLZbIuj8XtHrW3xwTu2kNq7BPM6WRuLlWzGn0wj7BYt6f1Iu1ljf7d3d9UZ-oDZxOh_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=AB1afMjVqthBNEeuSr_LoyBJ0BvrrK2DrB5IOkbErVPOXRdC3BCgl-krYa4CXWBVbU93om_LXhyhy3bYZRPJeBPGwsPEanVF4j4Uapj6mLKpxNP6nfFYMHeLevYlNIzuoGtHMzEI4CFw10NlECu1CChlt2cSawp5xPkP3mKvR9y-P5OsDoS-x4HgrKCWtGkFhtsRvQWyPti80EZqxsmTg2zQ3Y-zBB_otbOj-Pqv11gQovQN72Eakhd_hC1fCtlEFuh8ukp3XfL9Boq9m9QLZbIuj8XtHrW3xwTu2kNq7BPM6WRuLlWzGn0wj7BYt6f1Iu1ljf7d3d9UZ-oDZxOh_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI9seTgAw1TZOLTG3hj-VbZXLndji-LjWU_9sjnXukxuL39Z_l1PZoTb0-Ti2EZ6PIu5tYXNDVMupwTWytsupgDhJHT13viTsC3ibor4h8K-HK6kfZzx1eSqYNEpTG0kxA67H2Z_ArZf-1Rd2K_p4aiuNmVOYyRL25XMenyKnq-4KyHGBAiWk9Zn9vOlvBycDW8GwaXM5YNFy4y2riCQ2Y8Vp62_Sk65-1alwqofYRyyslEvcfePvTovFlgNmJO4QKu9dMTXavRhjYdii-EREVYXDvMw34joKOri1xpVorrsOObqwXBp-XKO3LNzYx5OHcSxZX6gosBTrvh9xKG0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WumS2PcnRbnazDX0mArps7XvdfyZZQr1Z8sWZuv6blyR118jKuBnp62ZKSQh8psZDEd2Be-0m6V28-CitJBpvb4q-Jh15srKy1lePepvjkpKjLayfoHhPJ-5jKNWE_-eLdX_uzu6rO_KAcq_hVjXhHpiKNihIX8yJnW-NlVIBg0l3qLYXGpd7yo3pILirzoZJ5zdW8vKCMQWyU5DUeWgvCZF3LfMywWG4kcp5ayqStZWjmHFlWlZDmrYxwgJFoljtMYO20FRPNLd7OrHTvoZOBcL7rPF_wqLTn9Ddui-iJKvCoYFKooM01YNJSvC3zDLgEnTJhOlS1h-vZmmVnqpJg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=CKjwfDvacc5XDjpag0KGnJCEvwEOBJcSFPSRPMIUkGwvoquYRGrk_c72JSCpIKE83PMaM7zR6wZZ3kEQ2g0kZW9VCHKPCvvjpjQBoShq0iGe3ENjurc3uC1XRXltbJummFFrRHpPm00UoW63K4hYYvenshFh2T9X_zWyNS-NiFtLJFQI-zjWUXT86b4pfKy748lQCWiDgX__ESS503rAdSYSfQ65cIiNJ5trcQgLH9PeT175LfspO1y9XDJu53ZWAZyv_pUEBDHUH_jFlyhAaEZ6GS4T4-MXDlR6v0p4TuUCPDNaOYcs9ua-41vWxXvLI1zUMlKGMPfqP5ZEqtN76g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=CKjwfDvacc5XDjpag0KGnJCEvwEOBJcSFPSRPMIUkGwvoquYRGrk_c72JSCpIKE83PMaM7zR6wZZ3kEQ2g0kZW9VCHKPCvvjpjQBoShq0iGe3ENjurc3uC1XRXltbJummFFrRHpPm00UoW63K4hYYvenshFh2T9X_zWyNS-NiFtLJFQI-zjWUXT86b4pfKy748lQCWiDgX__ESS503rAdSYSfQ65cIiNJ5trcQgLH9PeT175LfspO1y9XDJu53ZWAZyv_pUEBDHUH_jFlyhAaEZ6GS4T4-MXDlR6v0p4TuUCPDNaOYcs9ua-41vWxXvLI1zUMlKGMPfqP5ZEqtN76g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=PtfTpIQMJnyGA4NrJKMDwh3X_veklHO2tdB_Bq208TRWMQMuQGzOIqBGIZC5kWSDML8yVoQ5eBpmv4dwK7pSlmpVizfEuDmyg5HqUeHFyYTRC5_mt6epuKUW9fzgnOXRdEWKcbrsHysHdVGE1n47QfvkFtPqa594IDNcOoZHPiOFUR_k6BHWhmkeKqLx_fzkA7Fi7mQOm33qnHJ8ZaASCSv770sd67lExVWXd9-MEhJFzLmuICBwxVlSg65eiZ7h2ykX7ulGSo9PzOKTtKBb5OcZnABw12eH86jxAYFesLzSUxQSeSX9ECLBZAvSSJGYnNjY18sMAnAtGj1w8YKzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=PtfTpIQMJnyGA4NrJKMDwh3X_veklHO2tdB_Bq208TRWMQMuQGzOIqBGIZC5kWSDML8yVoQ5eBpmv4dwK7pSlmpVizfEuDmyg5HqUeHFyYTRC5_mt6epuKUW9fzgnOXRdEWKcbrsHysHdVGE1n47QfvkFtPqa594IDNcOoZHPiOFUR_k6BHWhmkeKqLx_fzkA7Fi7mQOm33qnHJ8ZaASCSv770sd67lExVWXd9-MEhJFzLmuICBwxVlSg65eiZ7h2ykX7ulGSo9PzOKTtKBb5OcZnABw12eH86jxAYFesLzSUxQSeSX9ECLBZAvSSJGYnNjY18sMAnAtGj1w8YKzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=KterlYrTr0g5WAdFpQvuMHU-ugHkp1EegMQit605WW8I9v89mTVBjjiXJBiRWOUA1jeaZBFiU49mqQPm1WE-iszc82rWSrfR6WiC4GdXxdY5rAAFE_7vuD1mDcxvnsgKnZ6fePbf9_HjCKl-ntK8nuaV2u_We8zSeRio9-oDy1lhFvE35PHqFih2KKDiyCxaCjvbYlwjevZrVj1VK9x0HhxZOpKZnr_9R-jGOt9yxiD6e6IImmZcvFg3nqIN99g-FuRGS9Av5Vxi3nryF4MIEOMiRUv7gpaVx3ov-FasOzUceGUawe2HdoVrs6k7-4NWzxLBVSGtK_OlfpIb-4aZlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=KterlYrTr0g5WAdFpQvuMHU-ugHkp1EegMQit605WW8I9v89mTVBjjiXJBiRWOUA1jeaZBFiU49mqQPm1WE-iszc82rWSrfR6WiC4GdXxdY5rAAFE_7vuD1mDcxvnsgKnZ6fePbf9_HjCKl-ntK8nuaV2u_We8zSeRio9-oDy1lhFvE35PHqFih2KKDiyCxaCjvbYlwjevZrVj1VK9x0HhxZOpKZnr_9R-jGOt9yxiD6e6IImmZcvFg3nqIN99g-FuRGS9Av5Vxi3nryF4MIEOMiRUv7gpaVx3ov-FasOzUceGUawe2HdoVrs6k7-4NWzxLBVSGtK_OlfpIb-4aZlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOx0e9LGOU0ziZxT9Mebo_N7SiF6prn4Ye4J5bnB6nDd_GIDwYZt5aa300cFaGhT6LnVRPxqQh8B566ka_y5HbKB_Aj0ry1SBl91giuO79DZK9_0iJz62_cwRN5TGMe56KD1KPsVEMQB21o49W93bDtIXL5xhonWK7dlEYyNg87QXLBRisqZUIxkDIdEx_ycBUW67LjCCzirwiIVZMtbfDyw5E1nk41FRXTmxh6WtCb9dFLFIEvkDshZIBxY5c0yMeVrYwilGqJOZAYIu_VcnoE4w-xNU1siHZTLIJRIxr4_7S-FR_NM9U8OXiBrTN0XAc9AVtxO5PR346JrOmBtDw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=a_yeDdYMCmV2PnXjtrojP1K6HKdrbx7Y445OZadIOtWxIt_3mp3LH6fS4jExIyvrn8Nc9h0TlaBJii_q3Zju4-ZZ7Whz82yeNIRLdFnJLrQ7xaUrE6yydTNoah8SbTSapHWEFdx-3n4SrdvTf29pf0g1dc_0V86sTW5ZoK3mEOhsw56ut9xfVgA5HSAHDQJn_FVCxIS5C2MerF__3k3OtqSyI3-MM7Iv5zRw1-gDWGMs3yGI73JfcFWsvMRQgYAj725Wg49BHuaDeEpyzpl-kEywcVVhdzwoRpU5RToYTz7y31S4yDp1Ob7Ro3ysv0PayvUnZjjjCdNxoNyecvW5kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=a_yeDdYMCmV2PnXjtrojP1K6HKdrbx7Y445OZadIOtWxIt_3mp3LH6fS4jExIyvrn8Nc9h0TlaBJii_q3Zju4-ZZ7Whz82yeNIRLdFnJLrQ7xaUrE6yydTNoah8SbTSapHWEFdx-3n4SrdvTf29pf0g1dc_0V86sTW5ZoK3mEOhsw56ut9xfVgA5HSAHDQJn_FVCxIS5C2MerF__3k3OtqSyI3-MM7Iv5zRw1-gDWGMs3yGI73JfcFWsvMRQgYAj725Wg49BHuaDeEpyzpl-kEywcVVhdzwoRpU5RToYTz7y31S4yDp1Ob7Ro3ysv0PayvUnZjjjCdNxoNyecvW5kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=gxvIpf6UWRZ8TKR15t_yxnvuC3vJKSqck3gbudzDUIdCt6_YyhIS89nW01LYy8SVgPM_M0W7s7fP42-jkSv7IyjO09yukPYFvKAsSGT1jJOLxGSwFCLr1pGL3wFwUoxbRfIvflm6Z_LDRMoCGXTnwURFgu_IprXEyQngGP7LaG2p0WCREqyYxUgxyQ0ds-ifIeca1Hk9urnhq8kCKh737b9ao0ZpkSHoFNIEVLpUX9C4q_qwNqxYg_xakW0bi--GTS5SneRqUqxBFROMe0zFhshgDrpQq8lLiz_f3u6y6d2buh8IuK9NH2H_5Hpas-bz0iE270oP027MG0pto2qbVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=gxvIpf6UWRZ8TKR15t_yxnvuC3vJKSqck3gbudzDUIdCt6_YyhIS89nW01LYy8SVgPM_M0W7s7fP42-jkSv7IyjO09yukPYFvKAsSGT1jJOLxGSwFCLr1pGL3wFwUoxbRfIvflm6Z_LDRMoCGXTnwURFgu_IprXEyQngGP7LaG2p0WCREqyYxUgxyQ0ds-ifIeca1Hk9urnhq8kCKh737b9ao0ZpkSHoFNIEVLpUX9C4q_qwNqxYg_xakW0bi--GTS5SneRqUqxBFROMe0zFhshgDrpQq8lLiz_f3u6y6d2buh8IuK9NH2H_5Hpas-bz0iE270oP027MG0pto2qbVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=QOd6WbB-nMxzbexRhHcLR_n3qu_Nl_y0XkyRmov5zjx72etc-XN8VveDk-yxwj8Wzab8LckBwNA8Jnc1UaYC1NW8eeSUaVchDRaCeknyBFibzv_r8u30zlq3PgHucktReiIr6TR1xDJI-8x--jckrgJlohuoBelEwDLJa6YXkwjFIa_1G2_eYeS0QZqem1dFwGJ4rPplWUm-Xjb-olQFUnme9XJ2C6Y1CMYwYWLe10_Q__xgtIdtVJrEQnjr0ogckoIGpjm6NV7PEQBqofJy2uN-lppdb7ExO03VVvHI6YJ5WJjcKMmk2OjcPrXo1_1yV1eoUaj7psV275JaHujm6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=QOd6WbB-nMxzbexRhHcLR_n3qu_Nl_y0XkyRmov5zjx72etc-XN8VveDk-yxwj8Wzab8LckBwNA8Jnc1UaYC1NW8eeSUaVchDRaCeknyBFibzv_r8u30zlq3PgHucktReiIr6TR1xDJI-8x--jckrgJlohuoBelEwDLJa6YXkwjFIa_1G2_eYeS0QZqem1dFwGJ4rPplWUm-Xjb-olQFUnme9XJ2C6Y1CMYwYWLe10_Q__xgtIdtVJrEQnjr0ogckoIGpjm6NV7PEQBqofJy2uN-lppdb7ExO03VVvHI6YJ5WJjcKMmk2OjcPrXo1_1yV1eoUaj7psV275JaHujm6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6d1LMSEoC2jMXuiMrf9qMhKT6T-PVnmN6ZbxGlFVGHm94JGA8ucA-NqS7fLaVwu5sw4JNfMPO0VwMJGg1SDrioscNIrY6txHbTReRYUz3GoxltrOH6GCEH1yNdULY_V_tr3zWrj-m2YJ2FMiDjq7PobklkzKG6umrFrZOgGqSgo9OEiljUfkqKzMNHr_5FQoF4qfXeS0z_Qy-Gkz9KtDsFVe2SE0U9x3Kl7tPIJjyMo6QM7R7XiV56hR0Vtldlwfm-YlOjouoHJt_9IHaw3BawWadue2EL6YReNa3W59WgJ6nSp-0xpcLoMQpvJhNE5n6XdXl4cidtK_bhX4aNnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=HTV-0qBc8yJ4Ka0IxspVtwa_JE_RV5264Gyo_uwp--VMo8YJt1b0CsaQ7lqT0BL7i-0KfHJqpZJeu-KHkRjbjiQMW101dVjpC_ztef-Fazo37UUXkI_3Mlpp472_Htaf4lIWLmMCbJlgiDXe0hZreKcobzUmLGAGg_uAUsdWXkpjTSvtN4E0er5wN2XGQ4MBoAJ7RTHTXBfPgxAqCnwdN_7SCYRBni6o3d25B-iRyPknkoVKHLE-C8VU1vIPcjZlv1nSgjIoa2lv3G9o12DqwpEXeHBr-9r2rwDj2zsCIkcLOlyFfL-T_WVVQ0mUNCvrPwPIKf66cqKOLSJUV_TiMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=HTV-0qBc8yJ4Ka0IxspVtwa_JE_RV5264Gyo_uwp--VMo8YJt1b0CsaQ7lqT0BL7i-0KfHJqpZJeu-KHkRjbjiQMW101dVjpC_ztef-Fazo37UUXkI_3Mlpp472_Htaf4lIWLmMCbJlgiDXe0hZreKcobzUmLGAGg_uAUsdWXkpjTSvtN4E0er5wN2XGQ4MBoAJ7RTHTXBfPgxAqCnwdN_7SCYRBni6o3d25B-iRyPknkoVKHLE-C8VU1vIPcjZlv1nSgjIoa2lv3G9o12DqwpEXeHBr-9r2rwDj2zsCIkcLOlyFfL-T_WVVQ0mUNCvrPwPIKf66cqKOLSJUV_TiMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFT59XrSr_0tUZaJJrTwPRnh5WIOs-newfXvsqp0gRNOxo7lI3lLe225kdiObmg4I9BbMGF18N7pLiH5G2CSpdoPgijOHMwwMVUoIDDIj7aiQD6KuaFCWZREQumZvn4B5xSTUTBw1qpzfBRR88D5Srr4uvdsp7mWu0IqxGRt7YSnKbLQgMvR9CQk7aEn5Lo78MKhkFdrK0ohWRbkYGg4MfKtlyPx1ZVb_HElYJeWgoplP9M6vC-okmatl9qG9ejAP3ERVzF49j1o54foLBUvxqHRkxnrD7bwNpoQcmOn5y0SoAdb4Az7D9RnC74CrEftyT_CgUxTvVWtzLtLbWNs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=MYxSsWDr3oAQH5iuphl6kDPNYipmHdLb7621KHl77Ttb5sLdarnPYc0nvM8hLhH-uaqFtUpUxXHS-XhToeD40c_kEpWaJE9zBflWj0_m5h8IFjZ0ZoDi4LmTsgcYXBd_4d3z9kMnMybnT0vxNj-15In2-zFiXqIElQBlv5GbgYeERCDyfaz0Bl1RZDBBpykYnyk5fyA3Ic0BqxCj769yC7IYuw1KagNU1a2OJQ-8daX0656X52MbfQkjh1z-GhDr4SSkIeN1YAR5jducysZf7bSMbTRJtN3Dswn9zA1YDiNn17Xk9KeitQhpxYvs_9_r0Zfz2REMm2vHFrvMaQPdcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=MYxSsWDr3oAQH5iuphl6kDPNYipmHdLb7621KHl77Ttb5sLdarnPYc0nvM8hLhH-uaqFtUpUxXHS-XhToeD40c_kEpWaJE9zBflWj0_m5h8IFjZ0ZoDi4LmTsgcYXBd_4d3z9kMnMybnT0vxNj-15In2-zFiXqIElQBlv5GbgYeERCDyfaz0Bl1RZDBBpykYnyk5fyA3Ic0BqxCj769yC7IYuw1KagNU1a2OJQ-8daX0656X52MbfQkjh1z-GhDr4SSkIeN1YAR5jducysZf7bSMbTRJtN3Dswn9zA1YDiNn17Xk9KeitQhpxYvs_9_r0Zfz2REMm2vHFrvMaQPdcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU5FWU_h8SB0MbLFt07vwjAyN22u139dYiVcQ_fDmhoBkQ0dHh9XDVrBKDofRoYK1OPdjzYwJpD3b1dlc-TXJWCzvkamaxKiz224DrFS1J7-6UknZGzkHYItwL3166Ry852giX-uwjMlu1OaL6n4U-MgPbqyN6MMD8H45LTrKmsSTY55BaFBxaDnTct6OJPFiWBYCUIO2Qb5DTJkcENwlDOYQP1HLdJv0Bd-E0nzVAjRkE3UdTwaE8nA-gdYxFH3Cufjk7BkcFITMASi7APuW1GgsttQMhAQDcFAxzwDlTGH2utafDw85gHktNIxVAyCouvndRRaUR6_9_9XJZQuTw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=GcbovtX9470ko6VUpW1muxhYTs4SoHJEL4QsTdLxQWzKo6V4rJc8_9Z8VogoiDVULdvjYttrRYgBR7iqBMBd_1y1NlGVTOucjFo8wN86Gy48Itsti4oNGFXKPYanpSF1pQnHTnQN6V30i2naBFSWoX0RnLhMNdbWT8NRvrbf-Trz0L8ATfzE1H4Bhf6ai0VRvxTTrZfsscsPvtjz2N9lx-VZHYlHqAYrMSyJauMNXakB012fwUNoRM4t1SnQcqQFO258dl1ZIeTktr6Ib77vKYrZA1pOSywjXWVe3NJdD8Ha_Ugkssdq4VFW4gdqIWlhP9cBd528g1duAjSTqyYZyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=GcbovtX9470ko6VUpW1muxhYTs4SoHJEL4QsTdLxQWzKo6V4rJc8_9Z8VogoiDVULdvjYttrRYgBR7iqBMBd_1y1NlGVTOucjFo8wN86Gy48Itsti4oNGFXKPYanpSF1pQnHTnQN6V30i2naBFSWoX0RnLhMNdbWT8NRvrbf-Trz0L8ATfzE1H4Bhf6ai0VRvxTTrZfsscsPvtjz2N9lx-VZHYlHqAYrMSyJauMNXakB012fwUNoRM4t1SnQcqQFO258dl1ZIeTktr6Ib77vKYrZA1pOSywjXWVe3NJdD8Ha_Ugkssdq4VFW4gdqIWlhP9cBd528g1duAjSTqyYZyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_d58kXbXP6POjchNUdTyUIK8mnzegTbIEYY5f1fwtMCXS-PYtKY09Tp4bleExWs_HAQSvALUsBKVBp3sWo2JuMDAT93JzD1urZZb-NZML_I3seVC89ltQLInDLMTPgApSErAtP-1CZuozEESs1OcpkNJvAi00DpbIZA6Amf2_mR_3kRd_7Ko-DJGoVfzzi4dqAsESgMoIWdJ6wrV8uF8zroRCEoPK4jJuIKY8unf5NDQRphjQKm9uEg1mnS1-dopYhLliPSSA3PudA3m9rB1Wa8eA9gUz7DXJGGPuKGJLxosIwJOeRzNZeGWj2JFghj_fu2e9uFoyPCrfIbKwjb_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEy886YykXL0ZcOVLa85RmrGdq13ut5yLtPKUJYh5xT8mdQvYnypKTQ4ZUqxbJXIYN8T7G_NLI6NScK98d350t2_XN7WpNlujuVLsj76Axe9SUeAyUTMlX2gAoE_PiSY9mw-kN3W9_e7sEDah73h_FgwKP5Nqr-91ooBE_zzvYdexbtlyfQf5xA28tyzAFPC-lZMH6UsL1mj76i0B75CMt30eSIfP9M3quJ2fjtFJ8OVAgRA6d9xh0I6652HxzTglJ2jC5j5q4rKuXYrsZbufiEeAVnUa8PgwLeW95zLRxKrn3LHMSCyF8a--NS7hGpdux1v-xyUIG3vdOi5plRHpA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=YB7KCVXxnoRLcrwXUAdNxwwLegk9bQTt5DqVE7HPO9ZY4SGDoFyNRHClq02Uzz-wFT213LobC8ww3nnEcxeoU5yInnlo_iVNGRCiHz05qfKigeGmSguBo5wvm66lPj3WkynLwupi1C14zkB2NS9yYSXOlaaNEU1qQfMMg5uqgdIzjjSY0EWbarcUxA1mfQCJs7oHSK1U3h5gV7mNw6iaP-lLpYBV2GcBHy8N4rRieJie8GQ91jPRTsEINOhcCpR7sC7aQ_oVDMCj-fDeoVWBECOryawhTPLvYNwfuJFeZAVo-L5dG38yq1F6MtQT2aRdu0hYP8eK8uKsgauAZEwLHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=YB7KCVXxnoRLcrwXUAdNxwwLegk9bQTt5DqVE7HPO9ZY4SGDoFyNRHClq02Uzz-wFT213LobC8ww3nnEcxeoU5yInnlo_iVNGRCiHz05qfKigeGmSguBo5wvm66lPj3WkynLwupi1C14zkB2NS9yYSXOlaaNEU1qQfMMg5uqgdIzjjSY0EWbarcUxA1mfQCJs7oHSK1U3h5gV7mNw6iaP-lLpYBV2GcBHy8N4rRieJie8GQ91jPRTsEINOhcCpR7sC7aQ_oVDMCj-fDeoVWBECOryawhTPLvYNwfuJFeZAVo-L5dG38yq1F6MtQT2aRdu0hYP8eK8uKsgauAZEwLHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLdnppf_rFnZcNSIyOSFG9wVrvZR7cZAEp0pdj0Bb2xEysaCJtR5kupiaAw_t4fa8-AtRVPkoYt1QxWENKkJtEghlMzIEqs83yNFnlGXWZtrNHn9L-edzFG4fs_3NSc0uq8h6wXaZL3XbAQgYz6Bcz-fPFibCmOfjxhtgI7DLajPUEMqEmPyogzoF0bHw5ZxoQ39vHeVg3Isyyu2nIcsQvvcflAKFWZbMZozpITJ5rNbjmKeKQ-gveJ5Ez0hZeDH5J7q03uWSmr2SKzJurH9hteL4uWTFK9761zYX_XIOu_9RBglY6IR3kxp5MpRnuqE0v0F70v5aWm4miUzZkbDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2JpJS9NzuNLi8ivEeOvNaeYnp4P0fAqMG_TP2c_oTRpUUsuZ2esiMchWYLMJ_FCckOaYfBWRSQdOpIUN7Ydgw5lqy_ZLFDXTTo-dso8zV9j8KGJit1FysHKgszLJEOJX-eiR_mPaokaqVEgEBtLkX5l7ySpk33umJMp9-vZjD5E_15uVJIrD7VSkqnAbzp1HQMasA9Mr37ZZRrRXZ7nT5Od5WN1gEy4owLmQ58Z497KkEFL9FPH4ZYOsEWs_kzKXYCGK39n2my1JMSONEwYqRDrgz6T3v7YJuBYctxxEyg_wHP7O4CxLNAOSRmbKVVkHg-As_MAZbm0B4TXCiELfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqplMRrg5sDL29Oe5frH3Yo9J1PrCdDPXSXi4amJ_DOs7dEa6RsxSUMW1RbGXB1E6OpfVJ-F8Nfoy9v5rGo2t7aWatk4EODP-MuAtXwj27QqNmxOblToyQiERjjt68C6OiEjj1HCV7le_7F0Z6vogROJo4mFvDJDqZ54SfcjC8QMkIAI4Jk4RrxN5VSaaDjMRaDexl8McKGLOtc4c5p7SX3gRx6PjsivXjzHHKmXg5Qmq8NU_hEBKaY4N604XPnCr1rxCu0sBQRLFdBvC61_hltdnofmZ9rv0rtuYnp3zv2fxBSXNXvhfN1aPKQlQtFK1z0cBJktIR6auuztunTriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXlro874gijX1R6oWb4_bL8X0p_lSR_Ec5Uc9K4xcj-9j6TppbjTfjqhiHRGmoUzEDbCFlHj2tXGpnihH62NM5rqSNmXc5XAmbdi4s94Xb0ESzfGI3rkcCrIlLWC6f1h7ctn9Rae2YzPJKWOW6YhLB2a_tCjDT7ISrSkWvYl05kpv_jZJyfcgjm8sTlP0lTmsSJjZrr_yQJpkjbvcnVIBiy9tClX8x8VCF51ugSfmKYxCaT4JZjzmmdj2LNUVtF8fDVZLJLVhGbsIvsFw3qqfLg-CaW4n9G4d_b660UJT4YsIZ83VbAfRrYNNSv6V99w4RuqLyP4k5jZ5-9m_rgnDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAdKW-H0ihU3U-ST0rqNUHkMw_AGg74D9BJbBIvqnvJGAhcnmhSX0eqoNc0QqAaz7F5x6jCT4u9tbZ1L_bAXXooTmDq3c3F9NqFiDx9YEwIB6K6IgOUMXVMLEVN0yHRGZ-AlTJWe6aDwQ2-YuEkBmS18sd-n3nG_n-J3hobum-Eap7qRtU5FcP2AUThPM0ZokB-dElLF7Jm32C7k0VJhZeahPiT4DpBMdK134YHqmqkp5Gh-pDWr-iNiPS3skgjF7tTAY02sFIJNwAKct23gVgQeyXKupQsA_FpF1-vhfrB-XQuk31st5UEertP0QRtlUu0gnu_0xfOg8bVJ0YRpzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=I39qadfwLe98TzP9XAd5kj1m2945LI7OAXTjn7QzhwjMZHYWQFf4sxisXRj6YkzQCIy24pqgXYgNOmVXZsQof9D_BHKIajKKU_V2Zol6-jZRk3AsmhdbTqUESG5IGik_NLBKR1cDeMWMTMMGyvnxMZVlDZbs2paqzxnOATshpN8G3vPyjbDuSN0Wm4okZYDSPtmsMMJGitMgQxOgKq_s17bVBTFXSf5SLjnm2SR2aAKDciu-wnT5a3wgljjQRsAmEhp3U5R1PVS89NZHHl5xKNxrDmKbGtCksfc61u0xcrqVKpl3IjKSGY7AzJBcDJp5DHwkWLvSDJOhB9OTxEHbSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=I39qadfwLe98TzP9XAd5kj1m2945LI7OAXTjn7QzhwjMZHYWQFf4sxisXRj6YkzQCIy24pqgXYgNOmVXZsQof9D_BHKIajKKU_V2Zol6-jZRk3AsmhdbTqUESG5IGik_NLBKR1cDeMWMTMMGyvnxMZVlDZbs2paqzxnOATshpN8G3vPyjbDuSN0Wm4okZYDSPtmsMMJGitMgQxOgKq_s17bVBTFXSf5SLjnm2SR2aAKDciu-wnT5a3wgljjQRsAmEhp3U5R1PVS89NZHHl5xKNxrDmKbGtCksfc61u0xcrqVKpl3IjKSGY7AzJBcDJp5DHwkWLvSDJOhB9OTxEHbSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=Da_wtxMRXOcn2WDphgl7EEE-Zcs8xUonL4CtKO58_7mFFh8aFJO_31kr1cVHHfUqKdtme4bV6YHzxY-lWKeJdGDttTxig-JFtLq5m3K1Qbdi-ubyVh54aQBhSuddADPvsLUONbGu5SVs8TZ_UkvH9Ol6BnaeDZ_wd7qNy5gPwrw7NNXh6KZXsl74VcKukgGf1eV62BRX8fG_ekjG33gW56HmZKsLOyA5qX90FIki_PUtPcRuca4TC4TTzG7XcBFLDs2_ycbObmttuzEzJ8J7R-ubS8AVLNtiggRVpws3rGQmv39K5pFB0ZrbFnfGn7ke7sq7R90Mho3HdzX0CrVWEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=Da_wtxMRXOcn2WDphgl7EEE-Zcs8xUonL4CtKO58_7mFFh8aFJO_31kr1cVHHfUqKdtme4bV6YHzxY-lWKeJdGDttTxig-JFtLq5m3K1Qbdi-ubyVh54aQBhSuddADPvsLUONbGu5SVs8TZ_UkvH9Ol6BnaeDZ_wd7qNy5gPwrw7NNXh6KZXsl74VcKukgGf1eV62BRX8fG_ekjG33gW56HmZKsLOyA5qX90FIki_PUtPcRuca4TC4TTzG7XcBFLDs2_ycbObmttuzEzJ8J7R-ubS8AVLNtiggRVpws3rGQmv39K5pFB0ZrbFnfGn7ke7sq7R90Mho3HdzX0CrVWEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=Pr-AdOUdgfQCSh9Sp-W_AJbSxV0HQ3-4Juw-xvq9ncy9agx4ev8vghCmhk35l7XBd2E14xaNZvsGPQsUU78FmgEMIlPyEifcQ24W99dgweBfLBR0_xbcHTpN-_ljf_vOLDumDRwvUIlkof8nKXl9_rDBwZ5Hc1Bv1gltuiCyeRZa5RCHo4JbKVACxCi2-zXKtPX1rCWU-y02Xsf3vx5cqa38gxXDedexS8LdJAJQTL7IXOHndAHVbKpfTk8Boyllg85nIz8QUsosDWxYSc2t6ghM4EW5TbCTcAVYBgS9LH4WJOPL6MZx-v3BF04wMJ6m9tn7flkLKgpk3afKb3mWrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=Pr-AdOUdgfQCSh9Sp-W_AJbSxV0HQ3-4Juw-xvq9ncy9agx4ev8vghCmhk35l7XBd2E14xaNZvsGPQsUU78FmgEMIlPyEifcQ24W99dgweBfLBR0_xbcHTpN-_ljf_vOLDumDRwvUIlkof8nKXl9_rDBwZ5Hc1Bv1gltuiCyeRZa5RCHo4JbKVACxCi2-zXKtPX1rCWU-y02Xsf3vx5cqa38gxXDedexS8LdJAJQTL7IXOHndAHVbKpfTk8Boyllg85nIz8QUsosDWxYSc2t6ghM4EW5TbCTcAVYBgS9LH4WJOPL6MZx-v3BF04wMJ6m9tn7flkLKgpk3afKb3mWrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=dRB7A0LEOmiHc7FT-F9fsQmR6BSjFbS60YEJK2yeens9kylb6R-hgU_PoRriUbjRcrrrteXToQ5nXxKwpIG3svggIoxEgKpLbYPrUUatLkXOHNl5gFvQMWOgqCzR67PluFkV1tNtD6OdixqaMqsQr-dOIpH5Jmbc5ytf-h9MKkksYvMaDKu8EnVhKqTfsfSr5Xb9cG8eX24fZWqdicSfRSFNjEFTlK1hpVQsVyqMp--gNtsO3Hs9P_fXmcvh3A40LQTVkK_MlvuBjylMJqKzOh5GZUISiqk9xQI2FPpFZa8p3WmHvbrGyEnk6yjC65vO_OTETCLFOVTSwXIUi3Tfpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=dRB7A0LEOmiHc7FT-F9fsQmR6BSjFbS60YEJK2yeens9kylb6R-hgU_PoRriUbjRcrrrteXToQ5nXxKwpIG3svggIoxEgKpLbYPrUUatLkXOHNl5gFvQMWOgqCzR67PluFkV1tNtD6OdixqaMqsQr-dOIpH5Jmbc5ytf-h9MKkksYvMaDKu8EnVhKqTfsfSr5Xb9cG8eX24fZWqdicSfRSFNjEFTlK1hpVQsVyqMp--gNtsO3Hs9P_fXmcvh3A40LQTVkK_MlvuBjylMJqKzOh5GZUISiqk9xQI2FPpFZa8p3WmHvbrGyEnk6yjC65vO_OTETCLFOVTSwXIUi3Tfpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2jSowPaxDrAyHC5jKZywGdORMDITdB5zL1Epp8U88T8qCQPuZ9NAuE7OCE8FdbvgbbtqvuwDlclkQj_rRHKFldeYrYNk7_c8UwtdD3kO7chgIFiPMsOJdY_n1KcDpmmppEl--ydj_S857sBaLOUvqtIIgqaD8nvNoKbe64swJFzkQAa3r4hCPJiLbzA8EhJCEbTfIVFibJdYmAPTJeVgJJ_A70gVKhb1awCd5JO88K_9bN8AA55qOStd17vHIWDzSNGtjznFrVrRTrFggg31320KixceWbYvKZ_7ACR9ZvmIyqG4tauYRAAmtZVyBqTZsv2GQomHqbnEAqntUKxAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH1QD-B2B0Js8M-H-UFs_8X5pXT2BHjWHXg_aIpRs0dLaU4OV_ct8QAKk5LSJ1G2UZsk-Em5RAR-p88CUfz2lKeY0K8q-WaApo_royjb1X-tKBDlEOTV-CcQfrjGJreREzDpLIks9qlUbdyi-ozbdnuuR3QcqQVLEXEONXTsOhfF_AYvn5W0GxI8RCzHeEGH3AnuiamIN4ABk-pz4gOzIOTTk9-TEJruema_LDEQWupr6_bFodfJNup0DTepWtn5tVIwR0O4blfd___tXcZEnGMXa0_TceEWKFdi8QfvwhggidKWyOMwp7hOnbe8lsnDL0LQEWn3_YMBy-uWlc5ngw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=chSxFpyPN2LKssz9Ovb_gPR6rMYNh843Eje15fo52In94Xw9Y7qqi2cQh5Ry-Bc7rEyzhBOnPLiD3MbcQdAiJg8FjzSArxgYCler5ingSGT5m-OxMPTSuLrp-YY9vHPPcydghKi3fZYgFE9bu2RbSKB3xOmX21qQVY44z95a3abUtDarI1B01IelMIzu8FVIQAkKq83DuGoM2aJ7CEm4eac537qhlZoPTClP_u-P9m6ig4TJ_wXfZiQ26owZW-u-5dvUY2c1zEyFVl9K-n06C50otqQGLQ9xJOsIDLd2jVo4dNHDH4sDMPN5gJ_9afKoVGxsW6lJM0Vf6b0KuJeKmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=chSxFpyPN2LKssz9Ovb_gPR6rMYNh843Eje15fo52In94Xw9Y7qqi2cQh5Ry-Bc7rEyzhBOnPLiD3MbcQdAiJg8FjzSArxgYCler5ingSGT5m-OxMPTSuLrp-YY9vHPPcydghKi3fZYgFE9bu2RbSKB3xOmX21qQVY44z95a3abUtDarI1B01IelMIzu8FVIQAkKq83DuGoM2aJ7CEm4eac537qhlZoPTClP_u-P9m6ig4TJ_wXfZiQ26owZW-u-5dvUY2c1zEyFVl9K-n06C50otqQGLQ9xJOsIDLd2jVo4dNHDH4sDMPN5gJ_9afKoVGxsW6lJM0Vf6b0KuJeKmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-Jf-MslSwrCXyfOTtavOmN7L2t-JKQ5MCOReYB4GZRGaqeX6q08WYnYM7N6h70Oz5P-joaF6v6Td9rGxbGmRnZRKD3Uor3nS9m-4EOerog-CfppAJXG1gJrnK0Y3XFlvARW26dPE-gu2gy9VM8vAfkOA9KiYBK_0YA_eK0-LFPCEVMu8MVqwlXiP0MyCNFBBA4UHHc7esjlkVgUmxrlV1OrFxqEVNWV0xP3_5CMo4VCZm_3usByFukOhrqUnj9e8IzIk6kELFRdFbUDghqKukBQWhVb-QT4VEM5N8hW5N3KUCY2WFPh3N5n2cREJncAPshjJvQD2C40bJEvLvGLGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=BbZY5Rj3ZPF2rG-e8h8iQxgESGLTujKuyWen-kNHQXQtSiwPytHMJYRDNpkN3Yp7xUnn1Oi6IHECjCl95M26lUfKzjMZqC5-1Hm5VmXt5zfo_a6lKxw-Au8vCXQmzXNQ_BJAaz9uGP5xtECnhr94ROM2wTMEpR-t7WTYZfBvzgQiEU_IzS8TIE-woMZfEV1W-tk0ANe13shqbH04fZHQrJ5QOUy-0XURiTtH7SDPqUISnSC5-mRDLZgY1adXhG7sAYNOrpcCQW4jOYnp9XacS_fTEO0VNbQ4Hf7l-mayzsiUyRgzbL_uKBzobqMLrSJsc6Wxly306JPAS1OljXcMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=BbZY5Rj3ZPF2rG-e8h8iQxgESGLTujKuyWen-kNHQXQtSiwPytHMJYRDNpkN3Yp7xUnn1Oi6IHECjCl95M26lUfKzjMZqC5-1Hm5VmXt5zfo_a6lKxw-Au8vCXQmzXNQ_BJAaz9uGP5xtECnhr94ROM2wTMEpR-t7WTYZfBvzgQiEU_IzS8TIE-woMZfEV1W-tk0ANe13shqbH04fZHQrJ5QOUy-0XURiTtH7SDPqUISnSC5-mRDLZgY1adXhG7sAYNOrpcCQW4jOYnp9XacS_fTEO0VNbQ4Hf7l-mayzsiUyRgzbL_uKBzobqMLrSJsc6Wxly306JPAS1OljXcMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otYrihgMMsdbWcxmWWS1CUG3gWaIz5zDnJn3v6TyAsVhBK_G-UNFFoPUsFJ-7kzERZrjVKrOMAIT0tj9bf3Dyq9BdCDItnOBYFRj69TzDgEEWSeVKN2d8-N1bj6MQxp7lK7jpfz38Aip-ALgX4mOoecw2KyCMVwmpPNRum1vUDGM-js4_zrhOy_gJmyBc7COm8hxHR3T397ZguQR_6swm-OsakZ954jUapwY3CCdqrcx_db9bWIDnHsbakSFEgH4BbP8x7H38OIPZHC0THRzlJD90ujZ5t0Ugbg0Ysx4D07reQdwOiI5VZLI1Tet_lrp8BmOPhSInp6ybDImh1lCUA.jpg" alt="photo" loading="lazy"/></div>
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
