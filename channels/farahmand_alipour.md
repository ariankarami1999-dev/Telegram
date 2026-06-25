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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 19:28:13</div>
<hr>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFdFiG6Fo_21l3eI0g9gf5NGpCehHQROmy9gqjvXJpYJeTEPafgkUx7nkUKtMtjFP9wIeLMyJeCLfsclv0NiA-jEOkHOW_CEpgQ6_y8DF6v8l3r6VeLmhIvk_r3NCqjmuu18gMJpj9xRmp9ZZQxCwzTEqVTK4KLA_Fl-R7i_MS7BeJ8rqZCPWxPGw5fQ-zqyKEpNrHL2d2MktcW40qhVBwp2CPrCbKJVab5MSSLSKFMpulUQDNlhAT33DH8tamqPJNB-5RSGquoUGFYyPHa8ivRjt4VqG19a2mNwpC9ZlUClHNenuM5RQAb1z5EazGe_BeH7Qtjgg7ZKZ9yRI8U_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6jRmf0ba--mShtp3pjmojRkhZCp-yUBEnp6GPKvFtb3MMpcG_cIQzwaod3z_JK_RX0WcI43aGl1PG8XmYwzcaGgQ7dZllPn7bL_tAMkqu-e8pnolZdB-Q-a6S4t4t_MRQdvzC9tEcOt7r153fqzATAH8LYRxtoTYUlgM0XHwMTIqMH_IdvxcS2oe0cyQ02n1aEQvjki0NWaxnrRN5V256yS5ch6xnrJnJo1ycvk2uS2MEvUjvXYooNISJULVTX_0ILL0iz-jyHamKmAPPmPccXw6i0CkTHoLu9aZhHWnUtG1tZkcqsayXmxDu17jTsRr3B5DD6yTk1vufypS2cbFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=FV5QME_MxtPvyGnvdYt6lEapBQUZq-XpE48FOaWhF5CPwJ18KBnoCoA08VDezzVUpcsIRT2spFlfBHzAHYsCq6jBYhE4-Cn_FCkreWenalal0dy_arzkVBbT8R6NSZDpf0dPmtiN0RPzUAwCiXwpufgkhgaItW21a-1R6TPVljX47IriqzOIi-cIyBt9fkuTn2g21C8CwMiQEYeGJBEGCmyCNiAROgKZmbmMeD-8qSB2l626lilRnm2a-sWD1XHhSj1agjxz2S2uBlI_6iuY8YMGIfRvXDVwA-AGZD7homXqlyuS6LRZ0Ha-brwJD9A4--yT5zyEj9QdzX2VlRFjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=FV5QME_MxtPvyGnvdYt6lEapBQUZq-XpE48FOaWhF5CPwJ18KBnoCoA08VDezzVUpcsIRT2spFlfBHzAHYsCq6jBYhE4-Cn_FCkreWenalal0dy_arzkVBbT8R6NSZDpf0dPmtiN0RPzUAwCiXwpufgkhgaItW21a-1R6TPVljX47IriqzOIi-cIyBt9fkuTn2g21C8CwMiQEYeGJBEGCmyCNiAROgKZmbmMeD-8qSB2l626lilRnm2a-sWD1XHhSj1agjxz2S2uBlI_6iuY8YMGIfRvXDVwA-AGZD7homXqlyuS6LRZ0Ha-brwJD9A4--yT5zyEj9QdzX2VlRFjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=pYjXjK5qPQuNnyviDJNPDuPH7_tvnHJfCnXr6i72Olh1h2ithz0rosXibIAwQX-JuUiKXj_YF8czaSXeRuH_baKte4RYxbdsgu6cbaL6Tg4Vef_dkPRYCV3fJqf2ASN7-lIgg7iJc1Z6-woBGStn2bXWIUkx67atfd8BNAhrWmggaDbs8XSYBF-CUQuGn116qu_MQhfcCuK3NFh0DO2saiWLvqD7-ugHLZ-_S-TASxXPmixhnOys0nVzJstdkFrUYIWhPoVWBkkZGkyaLBDzMe8VizwrhvSGwG1rRXCKHlj2QVZWVd4Qu_zuVybK4b7MhGhEEV8JTnJgKUpyztQFvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=pYjXjK5qPQuNnyviDJNPDuPH7_tvnHJfCnXr6i72Olh1h2ithz0rosXibIAwQX-JuUiKXj_YF8czaSXeRuH_baKte4RYxbdsgu6cbaL6Tg4Vef_dkPRYCV3fJqf2ASN7-lIgg7iJc1Z6-woBGStn2bXWIUkx67atfd8BNAhrWmggaDbs8XSYBF-CUQuGn116qu_MQhfcCuK3NFh0DO2saiWLvqD7-ugHLZ-_S-TASxXPmixhnOys0nVzJstdkFrUYIWhPoVWBkkZGkyaLBDzMe8VizwrhvSGwG1rRXCKHlj2QVZWVd4Qu_zuVybK4b7MhGhEEV8JTnJgKUpyztQFvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTwd1PZgtxyk9gR0BeLXT4HH9NJBSEv-GoWmPocklLko1kaf4l4DSkY9gdhkW4GEPAsm579GvpZ9_dMnFvPFrVpeK1iJRhpa8vifE17BpLQfhr00rnK0v9UOaUoQx0Zlns4m_NNYZexTlSsx5rUDY8aQqpxlf5sA4oFXATASdDNmK2Y98zhpHZzBw4lp5UK___g91VDmTjZrzpCws2F7aCKct5QozVKtpMYQioNYpZ6C-NTK39I3tKuP4DiY7UNvire5mXpaJMGhznMxllPphfuXZt9XMFn50O2x4KQy8iMYXDSodh7H1RsaW6fBRE8fReRavSpm6NEm0AAXNKTUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=olPsU5oKiPfkflT8zn4bT-tRG_Sb61iYOuRJroEos1ryeUOij57W1doUJQKoX0s6tx6H5Vf4zxfmwEAufGS0A-ib21ZMME29U3jqWo-iQNVaI3lxyJtv1F6v9uBIfw7_uWF-Ko3M_7mrfMgW5eQ_qYECHxQsGsDDRMV6v2dTO0SwGnUo2nfaI6LXkNcMac-JXoNkSnpdo5nrSlNNAOPZ0ISJI92f5f3aLX-WRp5VSZWpqqJH-ybloupAlmgxZQls-tvjh6lWMAnZixNow8eIl-p4XYxLi4TLgMJPxBMPf9KLA54Yg0LABqTcm10AuWR6eRoLoRPUvBSDEoQ8bBkbqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=olPsU5oKiPfkflT8zn4bT-tRG_Sb61iYOuRJroEos1ryeUOij57W1doUJQKoX0s6tx6H5Vf4zxfmwEAufGS0A-ib21ZMME29U3jqWo-iQNVaI3lxyJtv1F6v9uBIfw7_uWF-Ko3M_7mrfMgW5eQ_qYECHxQsGsDDRMV6v2dTO0SwGnUo2nfaI6LXkNcMac-JXoNkSnpdo5nrSlNNAOPZ0ISJI92f5f3aLX-WRp5VSZWpqqJH-ybloupAlmgxZQls-tvjh6lWMAnZixNow8eIl-p4XYxLi4TLgMJPxBMPf9KLA54Yg0LABqTcm10AuWR6eRoLoRPUvBSDEoQ8bBkbqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UXWRm7lYHpYCw1qyAzHoH9RpGZg0HjFgdm8Q1kds-ms3j-nRfwtgDZXcfonmTD7g6owXxChLzeQwDUA59NS_vE-mxipovnL2q6pNqPjqjkTiFX6GLK0-OczdSTp8YLYn1dtMC_ZKH8KbE6tzQUkPhKP_Vs_i5dipAu5elZkl7_tl3sI8ixpk4IUz_FiowCHCC5ynH1vflJ1HToS-R8bDSfMXuBY_TxmRERE00Lq-_NipJVwv_H720p27mV8vqC0v17o6dDEUxD5wTkxtWFF0Ccna0UgMsYBSwss8KjxzJwSqqEcm8mlPeGFzeuQjS2Mvo7nCXanZ6JwtBlJCPC7h0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UXWRm7lYHpYCw1qyAzHoH9RpGZg0HjFgdm8Q1kds-ms3j-nRfwtgDZXcfonmTD7g6owXxChLzeQwDUA59NS_vE-mxipovnL2q6pNqPjqjkTiFX6GLK0-OczdSTp8YLYn1dtMC_ZKH8KbE6tzQUkPhKP_Vs_i5dipAu5elZkl7_tl3sI8ixpk4IUz_FiowCHCC5ynH1vflJ1HToS-R8bDSfMXuBY_TxmRERE00Lq-_NipJVwv_H720p27mV8vqC0v17o6dDEUxD5wTkxtWFF0Ccna0UgMsYBSwss8KjxzJwSqqEcm8mlPeGFzeuQjS2Mvo7nCXanZ6JwtBlJCPC7h0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqT13RyNpxvUyZxQNFhVYfQBzIKdeLIX-Wx3tewxuP5oCuimFJi1Y5a4guXAEES5e8XGvOKKLIw6w2W8sxvWzUSm5sgZb3CV8xBuEDUFtVGBC3aJbm5RpA5rbTftS0PZVXW4nKbJ6L9AUlmHbvEORdos0O3eW-Nfzafm_GNZ9Zcda1j34Kw79jObwWkAc3s9iE-X3J8S8mAPJbf8eKKGzkPWaMau4hePQz85wBuhjEi5wb1F61e75ikqXinmHFmfe2Y2IR3XR3V5HrAwU2rrfCqvW12n_87wCDI-Jzb022Fh9lnpve7BsPj6WTy2uSRtmxHaYXGebIsa4ghxxdVVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXER_l-LBMLiXUNB33fB_pVLho1N5j5geqD5iwZNSCRZeRaXcPR7rODAX_LnE_Szi2zKRCO1dAeb4GSYNlF3ZuMKP9cIRsGMs8d2c5GDwFlyL0NqOO1s6CBbPzwRGKpBL8VALtX01MDiZ9uC0mw_7aNYkVfOFsbc5DANIYPbEomTjZs29DVOQXCRKvXTLxn5HkMMkcvfugzA4UzisZck7ljHcJr0AnO-3h8jTuHpVBd8qqP2r3UZYsqzqfsRbZqv82noRdl9bdBw-jZEky-ZpfyQuJew0FLLrHYpMZVyFdf9MAtj1nOVqLTSKvZXIDACEBt5TJcrjxRta6sgm1PiOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=bfHtfbFkcZhEeNXQDX90Dj1WTs_l5DBjrTFbANLd0RfNw2qT1pJv5s7qk5RR0Qb2o6ua5uoYZuzFBBBLeZhjcYBbuyufIweb4RrTSRRGa3CjATpEHUgCTpvjDtPwVd3ZQ3zRKwT9m9_h28_HnRKTRQWORjwqYEsigmACNsrNCxsbbUfntuhULMTTZhduatEyRr9z4PwkElWasbNuzTigIKVK1Q79cnvRSnak1kZ9UfFumGfsZecxcd2OvkBAqowAyh2jmmZKz-02Vtf0pxDu4mb0J7LV8cwEBgsMxTu_-98kPfUC8AOUDwzhhYC51Va9GN_IsEngqdVBRtVue35HIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=bfHtfbFkcZhEeNXQDX90Dj1WTs_l5DBjrTFbANLd0RfNw2qT1pJv5s7qk5RR0Qb2o6ua5uoYZuzFBBBLeZhjcYBbuyufIweb4RrTSRRGa3CjATpEHUgCTpvjDtPwVd3ZQ3zRKwT9m9_h28_HnRKTRQWORjwqYEsigmACNsrNCxsbbUfntuhULMTTZhduatEyRr9z4PwkElWasbNuzTigIKVK1Q79cnvRSnak1kZ9UfFumGfsZecxcd2OvkBAqowAyh2jmmZKz-02Vtf0pxDu4mb0J7LV8cwEBgsMxTu_-98kPfUC8AOUDwzhhYC51Va9GN_IsEngqdVBRtVue35HIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnmc5BM_BATfxTXVABN7ZsU4BordS4eNQI6aaqyKbrjAug-1oqbJULpCSOPfYakPPn9IZ-6ilxl52zQpXke46Ly4mAhmQbWX1Z-k8r-YjEO5u98NFLcVnFff2kRgvZENkQp3Q8xpJFa2dMWI7VyX4iTJmhsmHCkQtgKwFSju7nd03Nj2PIswXOa_UUSqM0_82PRRv3-ahh0OTttH1aNBrl1m6_5DFaf0dRXXf850tcCHdoK48olS356kVX0TxVUsYSMYuzq1PArgATXEtYix8B3gPpmYgj1l3V0vn4w_UGUYBUHR2PpUbchJc90kbBcLfX7eYs7kIprTfShUcLr9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgDyKCIFEawQuKRuajP-DVDVTd1Ga_rSK6An4FYmu5tAxlv8-AM182xBy-1fvpLGrFjCGZX39Vo7QkyKvO30VeKd_jP7vthJv0lRXdNVVhyOaLyaR-qf03n5OxQDg0BnkhMPG_ExvuGqBr0AqR6ZLJ7PPXXYhIqlOaEtqa76UTwGmDHsoLmqho03aA3OksSX7YPHfJjA-3dAGodheWP_4wVpmOeQjI-0lV_0vmjOgko0kjmOcv8PiY5mHQ8zjhvpp4Kf4HlIcj4xwp1SqVgbXdSPimGzuTwkRdj5N_5y4u_8pKUnW69mkSrDfgKmci98brOZDqJb9luH274MhlwRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htDw3ou5FArRSPw6m4dU1AGFinupywzaO06sl9nRYlG7uJhsQ7DaWyT40fmyEOsWnU2qelY1cOEeM7W2BdN7d5oL7Bb7gyjocUYoQcxku_mu4Qf_6hsBaVKZ92Kd2Mut5kFz_6FEy7301PQqQIjNqPg6y09l6Q7oUcyEHnudfrSFq50TMpZkeAHLCWqcmZmrrMDaXBFcLan-LWPiNgxg-Vm0bA88BcmoJtOy3cJb6QfaHoLhrRki6KJrg1KTAqF1wFdIiBJeqkiQ0vRJ2l_39_veMmComafVOwhnlupX3E6YVSuHm5PAajKZox4qbkcXg7egyUKo_gurhqxLOadTdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=NnjQoogkXZJNhkrukBsz_5sIXK3EtWFzAHBFnltV6X7N3sb9iR1HdqwXNCFdqq5_tenUtmB6bmE3gAGTJGYUv_zBfezLwrTd2FpJxOnwm_j5Kcj37mz-11XvvQdprUYp9y9FrphIjIVE4IzHVMM6-toveCCjVreCo5Vwt88ei2MScYFaZv3GmjgTE16GG9eX47p2fSWWjaB7GaGIR2eEVIjVy7ZP_29tI8AgAtjhAoO48jkcBZ6y9pmnOBnIZgP0ZC_2eActYdxV1tAWufky1espAS5qwwKRB9dyC3JWHFBbrPzDhTBbsl1as6Ci_OYUZT-axYByuOFo_nv0zDBc8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=NnjQoogkXZJNhkrukBsz_5sIXK3EtWFzAHBFnltV6X7N3sb9iR1HdqwXNCFdqq5_tenUtmB6bmE3gAGTJGYUv_zBfezLwrTd2FpJxOnwm_j5Kcj37mz-11XvvQdprUYp9y9FrphIjIVE4IzHVMM6-toveCCjVreCo5Vwt88ei2MScYFaZv3GmjgTE16GG9eX47p2fSWWjaB7GaGIR2eEVIjVy7ZP_29tI8AgAtjhAoO48jkcBZ6y9pmnOBnIZgP0ZC_2eActYdxV1tAWufky1espAS5qwwKRB9dyC3JWHFBbrPzDhTBbsl1as6Ci_OYUZT-axYByuOFo_nv0zDBc8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLbO7Q8rWyTv3l0zQFed79rWERiO2Rm29aL1jROszaOSgfxq30tUT4HI6W5q_f5kYNRqe66LSIAoa3zVk-TEip90I4gzzHpVZRLHT5Q0qLumtwvXcInpgd0Ren4YYNL7QPIjA0DbBJhKNFRKELeckiaFeLGqdjxk5n2zUxOFbqJ0UaSMErrYTGLp0vb1tNCLVlF-DjzGkUhR4_ii4IORDiZZDvxJDJEbNg2S0xpGOgn2xKIa4i3dmONsjt0s9B4NKRsmGE8nEHZY7Sv-mq728Zpve2jNPFh5b1jvXGogn3AhcTCRjlUR_WnEuOvXRxxKhclB3Lw9ppjNlbzGVxINpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxQVpCM8Wlmxs69R1o-uRoyDeP4Jz_Y9wjh7_Urh6DBuq-c0aAlt-tpftDhTReUpyB3c4zaeuzlzmOElUwlAunIBpv1gUrROPnrMtHeSBEy_c8-BGchVFnpZU7RLalF9UCUHv_l44Z1Tv5Lgfco2md4KR_K6s26vZ-swrk43XZkDF7nzq5BeJavHPVUWH2x5oWeiTIYQgEo6zr_gmR5dUG0M8Rx5TrH3ecClTN6kn065jBsIu453Dqf4ivgYGZ3dCa2BsQzDF-WshnK40yjz2QsGfBT9rGhjxcMQa5EKeQMOLwFPMVVXkuaFZD0uUhmX5D9CFYS_8d9dzsivk1cVAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAlY9XCWevI9Y_Z-_dRQVbANrZAnqJvgf9F81m28VOaIiOBY7GAXj74ByWpXMwOr00NpANN072XbnGM4yVjkPT11BZTGXOyOrgKmehBLyCfPpw-OEAv7NxqAmD-YcJaa0IEj2zs2OPQa5pgnvU7hVl4g9cHzFtbXJEDQQo_ZqeKoUja9OjfXbwhTuWwIharFzMKHCHR4FtWooaru_WPneMTqB7ltdSe97Lv6s_aiP-7vGNstrS5OO-X-Q2ZptvjFMpi4f-grBidLKjCjVFjdur50k4Z2BeGu3omUDg-H0EYa7uD0d4di0XxFJLpzXLkhkM1M49qELk2hWAq0M5qAlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=hl0AMkEjuPJ4Q21Sp4-xe6U9eSflyDMXqyPXlfD0aWl254lIwXWVJoF2ZCOTRxmGHxxG2qGy1RCe9BDj3f5b75_4uWCthckmzZrsUjy0un8men3E4ZnpDqm0M5Taxkyzdrd13bMIZE0C9r88ZmjCOR_Eh_zj6ywBiK6bW1t2XQ3bKrohSM5cuMmPVjZcUNAygK_UtUZfCDhdTibCEX6Stll0d0kEB_y-lzm3umT_GZ6EHgPPd0g0xqrdjHCxVyx97t8LQa2LQfvANGVlAImM3PG7xeXxj9DxMXYtnKm3pHCrEm54vDTxWnllkh9i2IZIOKuIo42jZvlGBT1ZbkkUUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=hl0AMkEjuPJ4Q21Sp4-xe6U9eSflyDMXqyPXlfD0aWl254lIwXWVJoF2ZCOTRxmGHxxG2qGy1RCe9BDj3f5b75_4uWCthckmzZrsUjy0un8men3E4ZnpDqm0M5Taxkyzdrd13bMIZE0C9r88ZmjCOR_Eh_zj6ywBiK6bW1t2XQ3bKrohSM5cuMmPVjZcUNAygK_UtUZfCDhdTibCEX6Stll0d0kEB_y-lzm3umT_GZ6EHgPPd0g0xqrdjHCxVyx97t8LQa2LQfvANGVlAImM3PG7xeXxj9DxMXYtnKm3pHCrEm54vDTxWnllkh9i2IZIOKuIo42jZvlGBT1ZbkkUUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=Fj33f3XM6rjjfV_cDOWqw3pqZsBMr3jZ1WMJZklf8nfsp3kWoB8KQJ7_urbCZT5BqR_znaUS0oyV9uZxzOxDuX6lJ3CKwAbwUdvw42hNdBWaQTl6ebRSZmMIvv5XU8vzS7sy89X0ZmGPetrPLVvtvDUItXhxNM_QCd8tkSSUwdsdH4frmvTSr5R2Q1qtqAO1sX02g9WO5VoKrLAwJr0OGs-t3ocajHiZfZnL_dZEzes8CQ6OrTU-GuidNxazmQqeddu4Dq3kOEvWO7BdxPQHAWHtSt1D5xSLNuETswRhW8psHfJWuAAcg6VUWJzkeBG6e_-ltM97lyTNOYzljmeDKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=Fj33f3XM6rjjfV_cDOWqw3pqZsBMr3jZ1WMJZklf8nfsp3kWoB8KQJ7_urbCZT5BqR_znaUS0oyV9uZxzOxDuX6lJ3CKwAbwUdvw42hNdBWaQTl6ebRSZmMIvv5XU8vzS7sy89X0ZmGPetrPLVvtvDUItXhxNM_QCd8tkSSUwdsdH4frmvTSr5R2Q1qtqAO1sX02g9WO5VoKrLAwJr0OGs-t3ocajHiZfZnL_dZEzes8CQ6OrTU-GuidNxazmQqeddu4Dq3kOEvWO7BdxPQHAWHtSt1D5xSLNuETswRhW8psHfJWuAAcg6VUWJzkeBG6e_-ltM97lyTNOYzljmeDKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=RamI22oVOZBGM9YhyDyJEHhDwQgdBPX2no9OuIDBZS0fJW1qB3TUcT8B4hJq-kJNmiMYaTcR8XzzxDMymd_7Vs8INtH62T1YRtQSYzsvqpaZjPJMDlMEB4SULKWP7_-fEsHegkuR_kn995-xlkGhBOfZo0gFj70LIWWLp9PUr6pE7xnLVfKyoG1oK7-1wifvQyeHFqnymSyqPHnSKGKoK_HsTW-Ks2OcnQmLfCuL8-ydOpO5j9BFA0q-YhaUO0l6yQRLAghoPlXHw9xzgku2Xvy6lknuanz2GiqEXiCQWASM6hwAsDHuSs26cosWY8fXg1pd85FrNv0-l_LvFtVxMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=RamI22oVOZBGM9YhyDyJEHhDwQgdBPX2no9OuIDBZS0fJW1qB3TUcT8B4hJq-kJNmiMYaTcR8XzzxDMymd_7Vs8INtH62T1YRtQSYzsvqpaZjPJMDlMEB4SULKWP7_-fEsHegkuR_kn995-xlkGhBOfZo0gFj70LIWWLp9PUr6pE7xnLVfKyoG1oK7-1wifvQyeHFqnymSyqPHnSKGKoK_HsTW-Ks2OcnQmLfCuL8-ydOpO5j9BFA0q-YhaUO0l6yQRLAghoPlXHw9xzgku2Xvy6lknuanz2GiqEXiCQWASM6hwAsDHuSs26cosWY8fXg1pd85FrNv0-l_LvFtVxMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byVR9BkNqHQSTkBchaMw3mnkFUEoqHn4WI7tXqB_AjY3t042JSPA2yR4OFL5IBphDcs6FAR0r7AbBBNvWN9eYiHclQqBAPlY7-dC3Yr6lDIYA8tpGdedGwlrEeOlpRruHGJxDD_dQm3JMMJ90tmbt_6q49GpmEyk9zft8mIQxb_NmLZa5iyzrpca2Kc-J3jRY53gfGSMCSynAnQiKkOvHMZHJ1_cJtL3IrGjyAnS5bfaw4S69e_IZdghRFYjFdtg61GaePRQZdloqbQ8A7xOkicJfRq0w7TLKcsvqrVNBIf-zvmazVLeVFElY44jh87gqU7_pZdOq3d4pnnIVe5n0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TA9do0KDf3DRNV0f9cRvPIdRGQdjEt59nLrI4pxSMq9W6uW3xo_AjRnXgxBcdV-JkfzfExtcnm9FgvyZqgd_EjtEVLSYpoVPZcGlVSJ1OidX_uELfG_tN34nNnmY2YA9fwq9oYm0WMbsdTFV26aKvJfTvF8P6c9GSpK4woqx6PkobdYgZGSMw98Xtznnrph3t2Y2lrXmCVSfYJnslA-FgKmkVg93Rtn_vbvfovQWFw0uAjPgTV_bCiJBCyP06LUV9wUe0P437fdKGvVLLdLSPEQPGghkV3KygbM630jG-wiIxYfc3EsmGhh2wwRcOANX-0LQF4s9uFbZl90fFSdKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snrEtyCOCR8SpvpCnBYQTkNEl81Bdu5rxxcu7XrpFKxty4qsafKBQ9GjBxUlda3TKMbqyUDU-ctRsNL01zLgt_D_quKi-D2h8CCNuqjBZHRml88W8GlV3KijZjXEiCQ10Nt9rXDIMFD48dYF442562Sm0kq7-ZiXjGEg3cHHAroiAMUomSp2HayGbp9JbG5f2eZc4CJJFaLH5kxm3MeLm95_gEag4sm6B4IHcPmNUKhR7XerW1zMvNotpANId9XvOTzQbwK_1kIpYC82avXYc2hMXOebDYYUdlfczjA1v7Dmxy1X79Kkq4Nmqufld_N0RE4IpY-CRkQACNnJpA58tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZizSm2GRSmiCNMBL0fnbEy-fLAWX4Lbxaa1V7YkEy7mAHxDfKj04qQuArWP5eyVsmktcDYQydpqbjDd_de36n-AHeH2uW0c_FS93pqTNw1fy2ethADVhzwWCQ-iEuqCU2w_0jT4LJ5RNvkm3DODi0zQpCfLEtVLGEiWZU-7Yah3bTR6I6lfvgHC5CvZIAgOU7u39uvTDrIdwfFV8fEZuz-o9mUGSSUTHxgnhthuYMcsDQTMOkq-bXyPCbAIyiXyssn0kyNh7ecul1ddsN7T4hAAAc5jMAQ3bQN2-_Svs-0-y2G_m8sedWKDh6Z8OxY03d2lOwxA4Bb6Gy8QJGXFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLsIdHKPrlUDeJ8v2kVegTUdAHE4FvgY9LWT_wwlsAI3FXFvEEk__CBX50Y_tVlWGmRzi2uWg_ibNKkBjF9e3zb9rfmVN-FynkUpvWiFPTf5s5ErlcoPCc2c2rWyg6gDf3Pbfg2glPa52MfP9EG6r1W2i7tzfA1Ner1WBGavertp3sRH85Y16-B7txnSRn1qh8eb8WXPa6Ipa4IFL0uqG8Qnl--zgFlUD0zsfMo5PRnt-boE5RFaupRYKL8IX5BwKuYxWY7J0SdGtDWOFAnR0NYXMXJja6vmXYcZEZYuiDfeJp8uC4KJZOD4sMAWPjVcHh7sw2IG_iYXbc2gowwgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8kok9nhe1ICssQO1zyUs9lxRbMPbJ_4sXIp4eOJhBRIMCJcXq9x-C8QVORkFR9b99dN5mh3Luyo9eH_mkBRrM-VbS-syaU_f8q6z-STzEOH90cw-dGv_2NhuvrTHDfPRr44GqGriXwpS2L_pT1ozZizv-H7P5PycWMMCtCr05x0hs6d7gGG97tr-uN05BG24m5BaQylpheohJCuAL1_VRn4XA0ll_sAfb66o2YHPz8RHJ-RgkGoFqNiHWCnZy0CsYzX7k1aGtB2Yg0xJFM55NNNPlDO_SvQLFSVecZmmjUXaGcQivTXMP74BgH4pJz8tLmzeq_uDFwVtO14cGLCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4L5AWZJPMcOzNeFNd377N51qv3dWxm13kP4ZibkCijHSd3LMTZxIoLc55bwHQc_ADA1Xq2iUg1TfeftM75Ggd0VjBF2WoTyLZIkIabhxL1w5KH2zJ01HLIpUoSfn34w7nFF_pYLSpAayy-xvLc3JMor7rXC3yMGFo3QZ26RpD3VIJ1Cp5jjTRx5lunhImHcCXnXYsQeNh8JqOyze5eEwa5TV4sULr1Nmv1mdFWbpdWgU2_GIXVc-0WjEEvWyiF5M6UiOCXyNv6as1YiYZ-u4Bde_EW3VziQlS-G-KstbemlCvRgZJIkaYGCcpxOddlEEJi5vRt3iparMgMd5yfqSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqd2OeZ18zJxKHEzwlepNRtk8uyLbHg8ZZVLE_uxukJ58fJj5arhjcqE0V5CsrePBZr8PoGDDAgdsBwyq5BtTK3r1JSQ3-UHfiuGXIVnLY7FEuG2dvWxckecICct1FNQXhYRdTU9-4R28CQ4TuTKmfAcjfjTrdccWS1v88BoglAba2eYxzl5yPpyjunKKB7-Hxca8wEC8K8LtXyHIMqxgNcZWKoDBE6HW7bU8JMk2J1-tV9FFQagy0c4Pa-XsTfmxiU58Eh9i4t-nN4fJERTuiyH38kpGqy9nzYSPJROmFkuJKiQzGSuv4oNRfJNeceXRoj2i3gE4K11621O4QlLsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPq1hpx_C_axkmWm8MpF9n1HkYkcz-2TQPaRHyT2Q-aGSCv4Ev1ebuKz9ErGo5mYNXZ6f_BClPmkyUYgGWgKtyCiE0ZvH4LfeQTiAiMKp3yw1y4064E2ooDSkExxkytJ0wGP3ZLNDyBbLxAZIpnaZawIXxWI9IZXqj7sLA6ymu9Z4CytHeBVuhXgYBBl-W2h3a8xfWKZbzLY9Z92uP9PvAtOsQ2BIort05F40NSQV19z8iuK13gXRNlgdQZn9MgYZ6BbYUxmu9lp1Wxl4UuKcXYN3VNRx3fu4Uub27PIdhLhOcwoyrjCi7VY4rYyXh8-BfWnjUdwZZZFDYK37bjSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3LErWH2FkgrA8pEBtN6pnxq4D4dBDCAO5cfYZiN_o568br_aKhIkgGfj0Sv4mQUg0NZJrHjgiV-n6iOVwAc1J0k5xPIEg1aDtsgt6hT0EG8Ptd_Vx8nwh9mRXg9ucadvkDOXSdmhdDAF9qu5PKjdwCrLhwMVRQ5k_BeSRqsevsNhDDcHDf5KSz_xP2u4ArRZZPtLthMdVbMuwJQtW0RDjLDGVD5CWFMC4CTFna0jdWhrn6xkK5qVRyfG_dQrDzSPumKjk57H0PcXgNzgcJeniWU2DaCQy58wu7eOzEu2Yl7fGOaAlq5SG9RFf0PwEz4gkhnZ7JRI8KePSEoTwzCKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtXILjH7c1CfjqNFVagJMBBaZN5LyO8-KYjKwscPJTsxkoq_u7rkgjCyJM-biNyPhcCO6x3eraupNmMXG5b5ay-A8Xfrzdz6Ycd7FaDYz3rCf74H4Wc3MjR7wH66381t7ElfEl_4ttcAdsxDGsp4H23O-G_IbpYJuEzRRzH3focmfv4nVkn_NjpUPF-0-FccqsLDz7OgY0-4F3lmbugRSiXQCI2CQkoqFB04JrepehT0HLnVwkBDxM2foDrj8N-e2MNbOCA1a7RNTD8QIzCakV8Emk3FZ0VceJI3wGZO-czmqd1WH81IyU5RZjhHpcjET-nSKBKOTu5klPQU-IqsuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obtc2LNhJfZAzu1PBHD4xCy2arlGPomfeLFtL8zQy92msgEm-DgSWR5s9c92QKFVmpSFxdGeqMCemeksKUtTEx-y9tlRVfFt9xJKfV8hT0lILVuevdF3sJR3tq0kIqOHezAwQbkVPJQvs_gM4HlvN2YHk_ajfWp4stNJsE9aclzYKQcxzW1zkpmONSphOzpbC-Szf4EfuXix3ZgzSTlvmFZoatSqL_kly45-OZaQ4EgAyUqO_G4TDuhoPbQbvzgwNIIauMi5IKc30YsZLXac0hxhKcLtxUnKRiYHZotZPCVWzvfHxu_45mfjqhTBBiqOty0g89GwDDEOrUGDu0gVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxDdCwIZ9K9YJdy_ecciFnOQLGkMexyq6wlJ-zndL0DoOJtiUUQDhPLFt7VJDHkzlGa3hamaqcU3nAc-xCAz-moSsmPRU2RyT0SABuSsKzg-NzR9_1FwX6EOhAMHYGM4np7j9myg8RlmjGm2A4CbOY9Y3L_4q7gS4YAfOcFQulU9txLpOsR6jRgVU3DDWMTQcx8yljiLc955MVYVoLxpaZlhmamTKEVrI8FCkfkZsyjhPlkQklKDQaKDkdcAYnlJAt-AmgcnxuehRK6Ti6xDzNFRcjm2T7nzT-GvUUX_OY-V9KF6pnlvgw9KMk7s401cQGJb2zA3LUWP6AFEUkU4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFtgnh-jzG0LoZwPOvsH5e1surc3Vm6XUIk0UneukkmUbdo7ahObmPl17hl1L-51lzbtUfBwBmF9Xf5JSxIZUmMP1IK0zsq5EgF1qvdfazXNikp7AgV2LLeGkoPY7QQ51hLygOn9qYY4CVqk95veAmASazkWahjjU8IbdNs6qlmUkGvyWEF2hB08b-Xo1Meja6eE1svNZq0Yaaxt9JcjPSWDTarf2lmYDZCFZi5RWgl-NZXi9SFaBuqdniwePuztLq93zcwQkaBUOIZ_VnIoe44y50xgR54AHYKJ6_PWImNIttY1AeGzVm2ikNyMxxy-ohwBPWBtpz0dpWi71CtimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2EZpA-zFFGbWEZnZZ6lfvWHFiSoBwJAYz8i8DP1Q0dbPTanEknzrEWlno09UwDJgJiRC6Koj7dhR3vYvRBLkQTctVRuFfWIRiqTIp9u-MhiBbR-uwXSFm_thQ1BgaBP-Np-8R6Gmiuhu_d0QdXe40Ddj3zI7Bhz16ZNGvSJCb_vCTL72tUFT2k5Oxe5zHH-g4ke1Fcj8LcIdaoCx3LGJi_ySCm_F8iBwMxoNWXL_kUfrQI2oPugdv-I8FBA-GaViEffA2i2JFzUmARpB_Iys9uTLPwavLBLwQGzYfD1uyOKVM8lmvB4526ssJ2Z5WYYCI4zOlz6zGNbY75kegCKCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=QGjLAUx5IBxsLWzSlsgRAgVyY2uwd5xmJhH0yvzrmuAoXLKrcEQoFGExIyRa0saB3za59-NhBWzMQZodf_QXREUmecya4G9sLaMdOknHnO-3xXY3tsj90YMDnXUP9jvzc0seaSEC9kBVTo77MC_EsAyyUijJ_-dgrfysr1cRXLB5sQkH3jzyU3agBTAy7qOKEdpNsayNVOx_aBEfVUb9k2Yewv_ANzAFg9DSquZqWzZs57A8OhIZMLJy-l5xHbyuYJBTal2inbxLf61mG5o5kEJHu4H_XwJ9r4Bk0rAJgEXZd4_cTFeK0S6t4UXmV3N7awcE0oHyYiUHXxo-vYcLTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=QGjLAUx5IBxsLWzSlsgRAgVyY2uwd5xmJhH0yvzrmuAoXLKrcEQoFGExIyRa0saB3za59-NhBWzMQZodf_QXREUmecya4G9sLaMdOknHnO-3xXY3tsj90YMDnXUP9jvzc0seaSEC9kBVTo77MC_EsAyyUijJ_-dgrfysr1cRXLB5sQkH3jzyU3agBTAy7qOKEdpNsayNVOx_aBEfVUb9k2Yewv_ANzAFg9DSquZqWzZs57A8OhIZMLJy-l5xHbyuYJBTal2inbxLf61mG5o5kEJHu4H_XwJ9r4Bk0rAJgEXZd4_cTFeK0S6t4UXmV3N7awcE0oHyYiUHXxo-vYcLTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcG-3qbU4XZVVjoIDfbgkgJUlyYI_55wYqO3g9qLFDgdYdjABmkVI651EXxcyDE8RJqJh2qzog8nQFlslu4T-vIqGPX7q2pCAIRxquvvYOVnUkp1YpH9CSt1KDegGhKnneLIyNAf8zbMJz794SsPvdLDNsMUZbPro9EJ0v_r2wAAhF0AevcAQ1o3nAjSQjBD5VhWR2o8zpfzcB95sYREv66cjNtARUnt4E9WCOoACziW_RljdI88_rquZPH4AslTwsgFRu9M5iGibQSj-5dTLVk34_VaptdEbr2NjUo1foRLcdPfByrjnCOnAwO7wejKvFEVhnb03U120tpMHaX2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=jb6sd8Mmsp6WMTXC1N6OUGje2vnhh5CO365516M0C0H-CpK_SUpJSBW1SIXdff4g3U0MPjoTQOLBdOAepCUrxRqDXqX31S2UcX7Cx7md-rAI07fy8kvS4cHW0dQOMqVU5gPiAMIkpRwEFA2g7QX1y6w5yBXQIvhjjmZ6TOMD4afZFRRy52uJVCEmawInM0A_mqA9Pc2eWqYtTvY-fUZorK_Y_XCI4XZPPOE6eZA1HudxhC6jq7tIQd2xjdRA0DoK5RgLo7hXowtiOaU3tV6FIcuhL_0lnDndzaMaHXFY75Hzyni6iKHsz_oV4NElHcyFcjBwmVE3RX4Jh_dDoI9A8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=jb6sd8Mmsp6WMTXC1N6OUGje2vnhh5CO365516M0C0H-CpK_SUpJSBW1SIXdff4g3U0MPjoTQOLBdOAepCUrxRqDXqX31S2UcX7Cx7md-rAI07fy8kvS4cHW0dQOMqVU5gPiAMIkpRwEFA2g7QX1y6w5yBXQIvhjjmZ6TOMD4afZFRRy52uJVCEmawInM0A_mqA9Pc2eWqYtTvY-fUZorK_Y_XCI4XZPPOE6eZA1HudxhC6jq7tIQd2xjdRA0DoK5RgLo7hXowtiOaU3tV6FIcuhL_0lnDndzaMaHXFY75Hzyni6iKHsz_oV4NElHcyFcjBwmVE3RX4Jh_dDoI9A8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=r2T2uzOwkppDFJFg4i1w7j0EEZXYi2wrkpnUa2GiKQ98wDi3IPTLxJNVPp7bJD29HC_OfPaJ6up-Wg1ZiCbo2Cuglgtvr9rctWwdY4SGsKFqM4tYeMkhNvhRW0VY47m5xoKEvB3Dz0_wEawTo3GzQSpzx-buxLe-ORS1gybdMiRGa3bfOuYqS66CJRE9ixC5R0DIinsSCKk4IiW8Nr-rkitF0EWqxJj6Qwi1GNTHAOCTZx9-xz-qFMe7i_LW58DWJlPnO56yQrznyBHB6zmt5gAzGszBxN7vFqXc5S2Wsa2sJ6445pP16K0OZ1cJpcYSoiFT7VB_9Ey8TD7hnAwqiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=r2T2uzOwkppDFJFg4i1w7j0EEZXYi2wrkpnUa2GiKQ98wDi3IPTLxJNVPp7bJD29HC_OfPaJ6up-Wg1ZiCbo2Cuglgtvr9rctWwdY4SGsKFqM4tYeMkhNvhRW0VY47m5xoKEvB3Dz0_wEawTo3GzQSpzx-buxLe-ORS1gybdMiRGa3bfOuYqS66CJRE9ixC5R0DIinsSCKk4IiW8Nr-rkitF0EWqxJj6Qwi1GNTHAOCTZx9-xz-qFMe7i_LW58DWJlPnO56yQrznyBHB6zmt5gAzGszBxN7vFqXc5S2Wsa2sJ6445pP16K0OZ1cJpcYSoiFT7VB_9Ey8TD7hnAwqiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWO22GM0TWS1i7e-ijDoeeLs40Yoq8FV4SfpFmRVgJRIHsppXKZqOzf0AXB4ksLTSYqC1WkycuRGpNrT5LjEGBOWI2u6PM1nSEUefwGWdmbWnhNVBXzpfYz9IQnCcHlhtYClLgb8XAGQh4gYgCshAeYPKuyO9AdIiIzMZOft-51t3lgIILyFuTlPvRLdk3QbFna0nD6RpbrzlLZnklGdorrVZqlhRG1k-6wP6Rxwf0XaDvKMU_5j0DNVvAb6V_DteKRBWtvR6rl-XsXPoF8V7XtmzmjoCNmh9HSew9Z6rG0LivQUWMUKYlNgGKwEHLKksLRc3uMFD4bEgaUZsIFfcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=NXn_y2mxKXTCfQhVxDNFS_3OG0bth3sv-J1u_auzQZnz1JNYB33v1QFBN-T_WWVxWJ2rQbb8uGXqOSJjBX_tKmGMuMps8F_3qa972AUrZQ4dLyVSLg8lgTfx9K-DGFFLtH6FT4CYoUGNTvGrzI3bLN1NDnPfNr0z2Q5GnmOLEcJfvwL-_ebrppgNizdXmSpOiduDW8E0cSe4hc7r0XKdfr4grnBZzwXZBxpKI9pgiwZj7s38kW3gbnY-Z6QOZshcw5mR9U9UrYKeN6j_EccNmDN9OMC2qoRfbdVfAmuFlJEnIwsALF6XKt2YgBZFfSvLgFeiKX5xfHazE_EvPfpdSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=NXn_y2mxKXTCfQhVxDNFS_3OG0bth3sv-J1u_auzQZnz1JNYB33v1QFBN-T_WWVxWJ2rQbb8uGXqOSJjBX_tKmGMuMps8F_3qa972AUrZQ4dLyVSLg8lgTfx9K-DGFFLtH6FT4CYoUGNTvGrzI3bLN1NDnPfNr0z2Q5GnmOLEcJfvwL-_ebrppgNizdXmSpOiduDW8E0cSe4hc7r0XKdfr4grnBZzwXZBxpKI9pgiwZj7s38kW3gbnY-Z6QOZshcw5mR9U9UrYKeN6j_EccNmDN9OMC2qoRfbdVfAmuFlJEnIwsALF6XKt2YgBZFfSvLgFeiKX5xfHazE_EvPfpdSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT5QGw8lk4bYFb2FDzKNXkjxp9JsT9-6SigZL5hfvQ4uRz2SmEk_uKXtVkoIG2AvtNN_FAJc_dC7Ab7fSxmusyGnAhdelrqsaudDJEfJ23xeMMf6pDZW3RckrA5g20PBMVBdaVvTNh872By9gd3aSnYVhuwV1TSLMFxu7cEGp8U-xM3kE_w84atsxTdvgHc5JHRDsy11E8Q5nxBSfeQRaN_BIODvV7TPZGE5IYH3ebJp4gIJ1Lj8ch4ZMCT9vsedvyeu8mTV_YjUodCd9v3BBeuQu0tIdRS72OQjTLT-TE0HdZpTMWtaWLTrBZkgCQ957Foc3O7mhdlkPixm7nJmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyBJE-5vQbvBor4Wb2rOQCXglUw9kGaBOfAEd2lCiZC_miD7qJKMQ7LvBtNKJVBx6Ev3mfymGcjB0bCkkyxz1g8FnVmv5pg0fJNB_2rprAE5byXkxKl4gDm6Ohr4jvQt_ZnsZW8LGy5id4cOhEtLmMH9q8WGsGC3TOhWWPrn-vxcXzD7o8yGR82BW-X_XHN5G8Jz1biOsdiJdpGvzSJh2FtiNEhMk9SyYK25seHwhSgy2z5JQLkc_dOetWXcwPUoFJOTp2mywp2mi9qmkB2GnWfWZ3NMjqGvP1H6ZDhPdsiLYow8BBPcbqNcBebAvORF95IoiPL82LPbeCfgx_fkEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFGCG99GLlSHu_Mz_GwWpfXZxBEI4NrhD4mYPIRMrxVaZQJv6W-41TNBKAkS0rHwm8U333MHLSyaohl7HJjiEWxKr5kGToMJ2Vh7vOWGMbJScXuz5E68ifrD6m16NYMBZewPONmxTLl1i_ydRAJbNNaVmMz6fD404YWUh1Jx-QcdNLtGjnFhI9tbQxtfEtL9Ha00x-AZQqASrJVCDERyAqNaCm_0cz_wag5DcW_wS3L8jEMB6WpO3bhW4IN2HmcoUZzyJAH8bWrAQyvCo2k-4mrXEzpiCN4SEHIo7Dw3a7vebw0nnk5Cx84NuMPYjLlTvFPreHHff-VI2a4VJLtWgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQa4pS-QN_pfsazzG5tEn7O7ci5CW3LEPNueud1_iit3UOnFCxOQ1WVD-SrInf2cIwQjOJSVxIskAsx5bTKKpioHJ0hVwxiNrggnX-Oej7fMzjwhWO3KoR4I6AuvIURbaqlrNuEk3zJSEj879bgpbWSrwVfCZ9Vx7GWz_e8Q-LyuXXS2LGpcB9aD6X6D-KoCpoMxLIFf_KueckU5r_0jBced4pXEyJoarfK1n4gkcgsVcWpqZKp_n4gYv0lXXJcyWSNnznsZ6a5s59CIYGcjyKnTQjGj0NjpuEJv8rgYxlhRjdkx4uyWNoN9a_k9j9E3C81YImDTbGpd2EIs24qLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=bEfKWRZigVgNhYiFGed6vHOlrBSBzYzzlkuPku0cUlUuo_XiDW-iAyyzvjARCEAIZs4CIULYeOCvMt6leiXGSFkm2UYbchksrBIuLktIu9g2427xMeGVBFjy1TE5bk7BJoTOHNZ499iN3pOrY9wfJPd0183NTj_HhCf43PiM2Aeykur7b-xDvr008FgzS6J2nwEPd4RMYoyYjASPr0c-4mRRdq1iJaiFj4VZzLJE5X4bktm45Wc2H-Hi4QAtNoTtMBu7hpEnKSH8c6YdsXh-XstNRKxqQ5PmZuIUGZm9dDwx4z7bGq4uO1_D0IKKkf8S3Drm0ENU_mnN77axOOPjPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=bEfKWRZigVgNhYiFGed6vHOlrBSBzYzzlkuPku0cUlUuo_XiDW-iAyyzvjARCEAIZs4CIULYeOCvMt6leiXGSFkm2UYbchksrBIuLktIu9g2427xMeGVBFjy1TE5bk7BJoTOHNZ499iN3pOrY9wfJPd0183NTj_HhCf43PiM2Aeykur7b-xDvr008FgzS6J2nwEPd4RMYoyYjASPr0c-4mRRdq1iJaiFj4VZzLJE5X4bktm45Wc2H-Hi4QAtNoTtMBu7hpEnKSH8c6YdsXh-XstNRKxqQ5PmZuIUGZm9dDwx4z7bGq4uO1_D0IKKkf8S3Drm0ENU_mnN77axOOPjPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=tFNmcVRdlZTKaj7ehnKT65T7bSZJacQdeJmBx1heQjI-eoCjsN47hgxxE8dwaf7WNGL21DZTk2KyPljJQ8cCn66g68iDT9_gWyzzG2HWUE2uVq4Z1LJuxqX8hlJ0SSOfITkRyhUoZ2sEJJsbVYAG-o9nYCt__tzahBTq84L9WTXOWJQy4VQYnLBoGcn2HXmZsZmFmZkm0QOvE3GbDWtVlLDztTOHyKwZ5E6IeDhgq6w1pZs1AJuJatwiep7HzckMYTJ015Oe-zQRpeOjuxm5aBEtE_1PR1Wycb0Y81XRh7hWENnEhYj7uzJT8bVtvfuLbIMNzWc770HBLxOVd-K_Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=tFNmcVRdlZTKaj7ehnKT65T7bSZJacQdeJmBx1heQjI-eoCjsN47hgxxE8dwaf7WNGL21DZTk2KyPljJQ8cCn66g68iDT9_gWyzzG2HWUE2uVq4Z1LJuxqX8hlJ0SSOfITkRyhUoZ2sEJJsbVYAG-o9nYCt__tzahBTq84L9WTXOWJQy4VQYnLBoGcn2HXmZsZmFmZkm0QOvE3GbDWtVlLDztTOHyKwZ5E6IeDhgq6w1pZs1AJuJatwiep7HzckMYTJ015Oe-zQRpeOjuxm5aBEtE_1PR1Wycb0Y81XRh7hWENnEhYj7uzJT8bVtvfuLbIMNzWc770HBLxOVd-K_Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=OH0X_f887l30krOdI3JcPAKBz3skYCfguosnPtfycyOmef5G_XeyLviCwJ0XA9LRqH7qoOCGflzimePLsyCxFIGU1JqotmFWmY6zL-NT577yHkDZm0-WVxzvLMww9qZFed7hZxqIJ9F8Hugho9AkplMDJmntidfIMz04J2qOJ9wLpanRJ8UNyZ31nucGhixY67P78SrP96IwWjPhDamFBWaRWwR4rM89pBTAXww41me3qLQbEuLFG5jktGJx1c02yRpWs3JKoaNiXpboGiy_jg98MvQP4V-yPiB5FUdQpkY2DzGB2LyTXI0rMM-78OWAHsZzXkv2KF0wTlENZL-cAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=OH0X_f887l30krOdI3JcPAKBz3skYCfguosnPtfycyOmef5G_XeyLviCwJ0XA9LRqH7qoOCGflzimePLsyCxFIGU1JqotmFWmY6zL-NT577yHkDZm0-WVxzvLMww9qZFed7hZxqIJ9F8Hugho9AkplMDJmntidfIMz04J2qOJ9wLpanRJ8UNyZ31nucGhixY67P78SrP96IwWjPhDamFBWaRWwR4rM89pBTAXww41me3qLQbEuLFG5jktGJx1c02yRpWs3JKoaNiXpboGiy_jg98MvQP4V-yPiB5FUdQpkY2DzGB2LyTXI0rMM-78OWAHsZzXkv2KF0wTlENZL-cAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=VOPm1LCHuH2E8M7Y0w_OXdsavibH_w4WqUgJBAco5y4fwd4dcVlxTD4SZq_fKo0BcYe6pPOhdYmDxqq3D1pwvu3iZBlmPFdUW7Teawr9BDP-1TiHv18mPPeEJl4pbCRKQtI9Kf5cZZ4Tax8oJi06Cnrr-uGNRbnusD1V4jhpEh4q2y5jd7dRLthLZAugE1H89JyYY2GW8TcheH6xnzA_BageZh30hmuHdvacIAORwZynRkY4vNmosHN-UM9rdE-OOro_sZEfJWJ2VyDNaZVhUSoh3dNuizbqlSx8GMFTtV3fF-ejH2DGgLMDx186EARPYBoHs5r_tu_YFCFtzM94ilo-Xo22DPgQj-gF81-AY43mxCkD9pG2xPrTTCO1lkO1Rydce6EVDmQc_fQPY7I_-AB9y7B93Ide1Nt9D9TomMpAwVbqLTJ_kqfDteP9vkx7MwAGM7gbp2PwV9jMQqiNAmO3H8HL2uN31W249blDl1Qjclqbapg8wNob2kxM6FHSihyuq7kWlLbqpsbEeXNZaiw34i9Y26HNXt-N9oh2xNu-YngY9va6AQz3t34FSjWMRGghiO3Y5ac3xsM81K1E8JBIVTDrQlhLGyslvSuL8xyms99eFBmDhHtoETx-tY4ucwSxe8bFaYENsaglT6uHenkRYkdIjRUXY6JALOSP8TE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=VOPm1LCHuH2E8M7Y0w_OXdsavibH_w4WqUgJBAco5y4fwd4dcVlxTD4SZq_fKo0BcYe6pPOhdYmDxqq3D1pwvu3iZBlmPFdUW7Teawr9BDP-1TiHv18mPPeEJl4pbCRKQtI9Kf5cZZ4Tax8oJi06Cnrr-uGNRbnusD1V4jhpEh4q2y5jd7dRLthLZAugE1H89JyYY2GW8TcheH6xnzA_BageZh30hmuHdvacIAORwZynRkY4vNmosHN-UM9rdE-OOro_sZEfJWJ2VyDNaZVhUSoh3dNuizbqlSx8GMFTtV3fF-ejH2DGgLMDx186EARPYBoHs5r_tu_YFCFtzM94ilo-Xo22DPgQj-gF81-AY43mxCkD9pG2xPrTTCO1lkO1Rydce6EVDmQc_fQPY7I_-AB9y7B93Ide1Nt9D9TomMpAwVbqLTJ_kqfDteP9vkx7MwAGM7gbp2PwV9jMQqiNAmO3H8HL2uN31W249blDl1Qjclqbapg8wNob2kxM6FHSihyuq7kWlLbqpsbEeXNZaiw34i9Y26HNXt-N9oh2xNu-YngY9va6AQz3t34FSjWMRGghiO3Y5ac3xsM81K1E8JBIVTDrQlhLGyslvSuL8xyms99eFBmDhHtoETx-tY4ucwSxe8bFaYENsaglT6uHenkRYkdIjRUXY6JALOSP8TE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=pe8_Rv49pIBu6QL-A9piLCVfInbcUEYhSWPExSVAJBv55G81eSvXvl2B5yfm3DNStqn_J-zY6ydwgt3wZyiqkKuD3JmGnf-Q_d54PI6TvAP13y3h-S4N6QKP-yBffbYWHoxOGUTv-NqbqxkI4_IxjdI1QO51w_oW5jMGZChaE-KKtNhMQ0JMF1yVWR1WpbBUUrhiLdiOPbS05nuARXbTsUuZFhmGS-vG8UW_uzNmiC4HZh-ZqqqDAfDAyK8xTUbcM1OhY9cVQWQvxkn5g3R3qDYkHZEGTy_TgobZIMs-_DNQ1LrveJz5u2Lu-RFjVmeh7wXyonC7VPJkrxuArob3lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=pe8_Rv49pIBu6QL-A9piLCVfInbcUEYhSWPExSVAJBv55G81eSvXvl2B5yfm3DNStqn_J-zY6ydwgt3wZyiqkKuD3JmGnf-Q_d54PI6TvAP13y3h-S4N6QKP-yBffbYWHoxOGUTv-NqbqxkI4_IxjdI1QO51w_oW5jMGZChaE-KKtNhMQ0JMF1yVWR1WpbBUUrhiLdiOPbS05nuARXbTsUuZFhmGS-vG8UW_uzNmiC4HZh-ZqqqDAfDAyK8xTUbcM1OhY9cVQWQvxkn5g3R3qDYkHZEGTy_TgobZIMs-_DNQ1LrveJz5u2Lu-RFjVmeh7wXyonC7VPJkrxuArob3lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=Deb25w-owrfPDtTFUmDfe5TZjA3s68PhXernFekVlg3QU3roXVAvJHJo4JuyNP4Cbx1VAbs9CeD_UgOICdmHxE5_WZK5bjg8Q-nz_yJwyZ5r-gTDi7q3jPiGbex4z9VaYQ43IPl1hUaqPgtWGM5cN9NPH5U51GiO9JFxUQmbZtfIQ5xQIexYzZeq6TTBw2xZNsOiKUMx9q2axanjJET3UpHxWkKoRcCqvY3mqstZpZmwh2bb0CutwYiPvBvcM6ahPWqKx1yP8_nzSVghU1YS2ncTp-3YKQlb19M-ixwtU2e5FhqvQHkOJjjmQo8Ess7-SdB6jo9vTb1hi8qnQDZI5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=Deb25w-owrfPDtTFUmDfe5TZjA3s68PhXernFekVlg3QU3roXVAvJHJo4JuyNP4Cbx1VAbs9CeD_UgOICdmHxE5_WZK5bjg8Q-nz_yJwyZ5r-gTDi7q3jPiGbex4z9VaYQ43IPl1hUaqPgtWGM5cN9NPH5U51GiO9JFxUQmbZtfIQ5xQIexYzZeq6TTBw2xZNsOiKUMx9q2axanjJET3UpHxWkKoRcCqvY3mqstZpZmwh2bb0CutwYiPvBvcM6ahPWqKx1yP8_nzSVghU1YS2ncTp-3YKQlb19M-ixwtU2e5FhqvQHkOJjjmQo8Ess7-SdB6jo9vTb1hi8qnQDZI5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKooOei2Xk_sI7SbNQyb87E1wr9LD71lsTx873iBOECcTfp3v3NOnqq8UPKe7HiZTmW6sdFQuqQpDtisqpm4DVFXtDV41iiHRwziSv0DXFakXugQsnejQSC3Pq6IwU7JM8yYlAgEgIg3Lb7gRJ9FLLbArwuNwxN3RrEB3fgbUmMtOpJMogSymRRsenxHZ8m0cNJdcQ4AS2nJ6ePe-SQMgdo5e5jiSyxUFly7-dhJ8y5lNUH57w8Fml-TiJHxJ6hzxYASC-i4hkGBytOfuTsAL0VDImbV6XLOEsHiR4ayA3C-le-fsb9PsfHQPl0O5kM3GjUo3ku2l7CUdV2jXVCkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=MAEp9qRYum8ENXdnX33du_RK97ZggzZQmEw5qbUn2ZgaDTYPNp0zfVrCpLU7Yv9AlF7ujBvsQ6sTzhDK7b46wk5SWj_CQW06tY6WukgKS5n0IZBZQk5QpB26uEA-cehUBeLF6WPdiiHT3USNhq1d9S2shHMcrwtTlLEpdF1vEx_wIJUcTRIFSIr1Sa9QYcG1JPckds5tZ61GpH6ZIK-Z4NqwHXlyQCSWb7B7-dB3RjBaO0U5UCQ9qjhrwWCRnsf594MtdrXmHUp790TVpQDoh0KxNia5dcE87_vhTvvg0GZB6gyCf8oLY_sXjLfPuB2aE2_DxZ6BVQnV-lPvvIMNIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=MAEp9qRYum8ENXdnX33du_RK97ZggzZQmEw5qbUn2ZgaDTYPNp0zfVrCpLU7Yv9AlF7ujBvsQ6sTzhDK7b46wk5SWj_CQW06tY6WukgKS5n0IZBZQk5QpB26uEA-cehUBeLF6WPdiiHT3USNhq1d9S2shHMcrwtTlLEpdF1vEx_wIJUcTRIFSIr1Sa9QYcG1JPckds5tZ61GpH6ZIK-Z4NqwHXlyQCSWb7B7-dB3RjBaO0U5UCQ9qjhrwWCRnsf594MtdrXmHUp790TVpQDoh0KxNia5dcE87_vhTvvg0GZB6gyCf8oLY_sXjLfPuB2aE2_DxZ6BVQnV-lPvvIMNIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9sHBVA3_iuV7Xp4aJCRcxEwuwG6ttDS-GECJxliYho5cD530RgMCszSGEunSVcaa74VHvop5lltS3ENhlseovB1Epb8qN3pAH8ItnfhhXHVqKYsMhBnumm3LYzfWxhB6sUvrTm310qEyukxoQH4kbyGxb7Mv5XtL50w17509xd30BV2cI9pbYDdfNxIe_rLrH_45K8JifGrauGfdpMh9ZBveUNF94e6EXPwDpkLAzVDkVM9UFE6uiGyBptHLCUy6lGB3sR9P4kRs-KM3K4gijvJoyUBVskAdudYSyfM9rz38doq-lzS6Od4X4BOsT7_CYJlngliL_UaEthJ0AN3bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGRn5zNAPsnqq8oeMkXanHL5fGmyEA_P3V_ZslT6L-FGsTjk2qNN7gvobmtTdWxw3QDUsP9wg4e_RXO4063DTT8xwx1Sm9P3muzXrUnnkpaT3H3c5h9seOp3WvCI3r1GK11jo3jlkrzqNPVYi6ShQdWrKK3beFsaHdINuoEjy9xgZ3wvgWBuNAY42zqdOxukezIR1FKz-7RjXuiaApp8M9cV1pVqqtaRjS9vzzZVUGlPbvXPiMyblN9sRuVCn8QAv1bEGMZNGtaYJLICiHb7Z4tuZ-uhgu4lRdg7OE_k8GZ56gO4ZEQl8Bi-WLx_mYVOzdpAGlPXH14_I0tWL6UElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=OdhOBPBN8Nw2Rfw8mbbVwBjt4DqiaOSGn3XoeF0ly9GUx1iPf4y1X40Nld6aPDJb6AAgHp9fCw9yG7pxXse9i0a3HtSJqQnrS1aw_3cZcOFsAk4E5uHdn4_QxS0jYE0MxkGq7IUqRaGpZ-JMYY-R4ICQ29qwC9kXWDBBUgYc3la0TLH_kIByFgdfkTyIXWmIPP6Dkv3ghGePaFOA5ax9qxVrfES557t5Anb8BuoQFIZ7Ma27348-8TxjcdC1h5EfY0vsLymFVJMDbPRWjMvFuwPJCyAdiJ_xXWsMSgVVB_9ajhiTt4ENv7hNoD2XmG0py3eVzI37PjEPX2urQs4CJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=OdhOBPBN8Nw2Rfw8mbbVwBjt4DqiaOSGn3XoeF0ly9GUx1iPf4y1X40Nld6aPDJb6AAgHp9fCw9yG7pxXse9i0a3HtSJqQnrS1aw_3cZcOFsAk4E5uHdn4_QxS0jYE0MxkGq7IUqRaGpZ-JMYY-R4ICQ29qwC9kXWDBBUgYc3la0TLH_kIByFgdfkTyIXWmIPP6Dkv3ghGePaFOA5ax9qxVrfES557t5Anb8BuoQFIZ7Ma27348-8TxjcdC1h5EfY0vsLymFVJMDbPRWjMvFuwPJCyAdiJ_xXWsMSgVVB_9ajhiTt4ENv7hNoD2XmG0py3eVzI37PjEPX2urQs4CJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=cO3utu03ZBtJQNKrocCE9VcOQmBmL41GZb7Ws-s-Pyu-nEeHiP1J7qm7HFRS0DU4znFKMhOGlelow7DBepGOkL7s-A78povBiqQeNDBnXVpG17eZ6eL4ZS7C-0wGL3z77gNBkbOjNc9L9qs7s-iYivygkf2pcyZuYQFa885BfF9EAcipxFsElUm2NTr9PpdebfiOFfcLZ0AViF6OXpiYHGPtor1WdzyhlXqHusN1vZG7YqlduvJfZqt-QAEYDBfLgttY6ocmJWRC5SG4x8tUAUVGjQXfplDSl7JQM8FjuOdmTuwSamicKMKBWntYPO58Pxd12mjY5KOC809qBMFXOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=cO3utu03ZBtJQNKrocCE9VcOQmBmL41GZb7Ws-s-Pyu-nEeHiP1J7qm7HFRS0DU4znFKMhOGlelow7DBepGOkL7s-A78povBiqQeNDBnXVpG17eZ6eL4ZS7C-0wGL3z77gNBkbOjNc9L9qs7s-iYivygkf2pcyZuYQFa885BfF9EAcipxFsElUm2NTr9PpdebfiOFfcLZ0AViF6OXpiYHGPtor1WdzyhlXqHusN1vZG7YqlduvJfZqt-QAEYDBfLgttY6ocmJWRC5SG4x8tUAUVGjQXfplDSl7JQM8FjuOdmTuwSamicKMKBWntYPO58Pxd12mjY5KOC809qBMFXOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=iHJaO4dBCjezH3xseKjtSes1awdLnUvriGOtrw7S7lnFwx3-iZ5uti0Dlml1it3fXXJ0oCJGkCvlxCM2NXh-XlGaNKle0qhQdjTyYHeQo3FxfkjebavmL5yYAkVtklB1wK96rne-G0KMpvd7YaENM_TvkQGcwrsHhBUl-gcV6ys7hOlw40-kHbNVdFGSdSHoPbmVR-2jUPL0zNiB0OEvHm30G1vmHACF5pt019GotDq9uV4WU8XaCYb2yC4RZ9j2dF4y0npNyfFlYUdFWSKorMq0vrgnf33QwLk3xmCJOja-L337fxO5uXzDg27q1VeJbO5JyNxDmq_qdKInQDDqog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=iHJaO4dBCjezH3xseKjtSes1awdLnUvriGOtrw7S7lnFwx3-iZ5uti0Dlml1it3fXXJ0oCJGkCvlxCM2NXh-XlGaNKle0qhQdjTyYHeQo3FxfkjebavmL5yYAkVtklB1wK96rne-G0KMpvd7YaENM_TvkQGcwrsHhBUl-gcV6ys7hOlw40-kHbNVdFGSdSHoPbmVR-2jUPL0zNiB0OEvHm30G1vmHACF5pt019GotDq9uV4WU8XaCYb2yC4RZ9j2dF4y0npNyfFlYUdFWSKorMq0vrgnf33QwLk3xmCJOja-L337fxO5uXzDg27q1VeJbO5JyNxDmq_qdKInQDDqog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5xFlwq4LxVX_yIXNE4W0efmvnadxRJ9oOzjjvgv8hlTbkxLhqZW6WxmsRBhPpDAXX8PGhENsqF3A01P_15fcKQuGo1Ky8nMCPVOObf_0aTOo6wF4Xh9LD2VYxhmniXJ1ZaYIVEtrYWLTAtMAnKLPYpcwqplw_zb6Pyt4z8n_THWKojFH4kiLDehWPMH4aIHa4npjMrlHD9r9WtcijPuyenMKBfX5VIZMvqkS2EszJ11Kmu32Fw578TXGltY0XUO6ZrZ6bAbcmXBA-JM81KXbyY4-uOEmDVex73U5UiLHZMfHYRsyYTGUpzFX8xM1KXbzG-XQnQinnhdWfaQGLDY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=rdz5T1Wr3dykHHz_kIhC7d6K_AEVovUlc8d9O0P-AH8MEGn7PNlHf7E9VZMXMPWg5O4ptW56NWsgoXB9bw-kArgwhm15bkFNF9bAC3h_iH0tY-1cKXhgO-WVwKoBXPnpYHFmWm4IkUMhpxUqZyBSqqZy0v5x2bG_mhh29rQqjdshVs9qKVWs9a01T5MIoXYvrNx1O9pS0Gi9kl4rHwCBpsS-3k9nny0H10uoPN07K8k-UzyTCzG2xQCHzdKowN8GQHfNGUy6YdWtJST6XMo6waejRyfEUDT3XV-_uc8_BB3KCs5lJacol6777tXpvaua04BrozIZsH5F68DL744Tyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=rdz5T1Wr3dykHHz_kIhC7d6K_AEVovUlc8d9O0P-AH8MEGn7PNlHf7E9VZMXMPWg5O4ptW56NWsgoXB9bw-kArgwhm15bkFNF9bAC3h_iH0tY-1cKXhgO-WVwKoBXPnpYHFmWm4IkUMhpxUqZyBSqqZy0v5x2bG_mhh29rQqjdshVs9qKVWs9a01T5MIoXYvrNx1O9pS0Gi9kl4rHwCBpsS-3k9nny0H10uoPN07K8k-UzyTCzG2xQCHzdKowN8GQHfNGUy6YdWtJST6XMo6waejRyfEUDT3XV-_uc8_BB3KCs5lJacol6777tXpvaua04BrozIZsH5F68DL744Tyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=qxZtzAq1XdR-MOIVTyolh4s9YERbCUu3A2tHJQ0M2meMkU9hkdzPqsZ17-1PU-UCovZTIzSbus7caVrm43NT03K379SVja6YbzBZy38d01z00gEzT5LTF_McZiKG9BNLoG5k0-oM3aqf73BN3gxpy4yCKhuzTNMgdq9LVLmzUWxqJ_t9j5IKZZbiXPbq-OQtv66l7dshsOVkeJw1SC_wkIKYhnH_VHlNrq8H15A3eMbT-VWdUB4-mhQFk7bAqWH0YWb9TVp1YVqljT8PWxAcVjmz6gzZkVeGlrWkr1f3wpzuApHQLbHrbcN3-dM2Km7m-kIWA2wm8Pk1v0Y9XXFx7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=qxZtzAq1XdR-MOIVTyolh4s9YERbCUu3A2tHJQ0M2meMkU9hkdzPqsZ17-1PU-UCovZTIzSbus7caVrm43NT03K379SVja6YbzBZy38d01z00gEzT5LTF_McZiKG9BNLoG5k0-oM3aqf73BN3gxpy4yCKhuzTNMgdq9LVLmzUWxqJ_t9j5IKZZbiXPbq-OQtv66l7dshsOVkeJw1SC_wkIKYhnH_VHlNrq8H15A3eMbT-VWdUB4-mhQFk7bAqWH0YWb9TVp1YVqljT8PWxAcVjmz6gzZkVeGlrWkr1f3wpzuApHQLbHrbcN3-dM2Km7m-kIWA2wm8Pk1v0Y9XXFx7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=O8pXx3O29nis9KTnHcAlTXBCE7QOhhBa9nAzMrL95dHxrD5Qgla9GRNoXMcKgfGECpezgKnHU5iwSmhzWM5sEadAoYpuJcmK4ik_UKvv9qiZCO4UVmBTINdVHcch8l5B87DqweNzKB8BNgydyPqm29xHgrHSFUJAroYZdBSOjIPEnpkB7tuMSdYhYMiXyh7wiKKxd0Q1QR6lW5IfeB5p5xKAP3Deev5Uutu3p0DM5hEsJy0X3uQiBOFdrw7C5NePQv_DlZkW2nbZyfkwZUzeV6E3n2K05vWZTcD2n_Nijy7vbDVKRTL0WsE_3IB1SdwEduu_3oViIQUYtvYmQU2kVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=O8pXx3O29nis9KTnHcAlTXBCE7QOhhBa9nAzMrL95dHxrD5Qgla9GRNoXMcKgfGECpezgKnHU5iwSmhzWM5sEadAoYpuJcmK4ik_UKvv9qiZCO4UVmBTINdVHcch8l5B87DqweNzKB8BNgydyPqm29xHgrHSFUJAroYZdBSOjIPEnpkB7tuMSdYhYMiXyh7wiKKxd0Q1QR6lW5IfeB5p5xKAP3Deev5Uutu3p0DM5hEsJy0X3uQiBOFdrw7C5NePQv_DlZkW2nbZyfkwZUzeV6E3n2K05vWZTcD2n_Nijy7vbDVKRTL0WsE_3IB1SdwEduu_3oViIQUYtvYmQU2kVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1FcHFsNJ1WgeJM0iyWGAWKrNiYbSBu6hfmcRAi72Jgj2oBvVukDWbbro8odj5pHgyltP-sfo3cqKK3JJY9c-0wOht9uVp8NaArhPC4yMd866S6n8H7hxyhK47I7Q4qgS0T8LhigxScHRLboPC-3IKPBV76fQZ3GqON0-1ErWjbpiTV2Fxrt2azIf9ospCWY6fG3WdYWD7RHy0brfwarRoGmjbnzsMd1DXDw9jfd5bz7_gtgbZulhDGX7ONjjys30bBykKnP2U1LoxNyxL_Eir3d8jMg8rM5skXDirUkYxOUgk3BXzaaP3B8nrlVyxBfTY2PF9CY91VSO61luXp8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=MDWGL-GmQrJZARkAx0hKQZ8BwIqJEUkiG2vDd-dkK9SqmNPXKEmTbPFG353DPOROahwZgAAyGdp2qqXDKkl6sWIMCJ1N1-IcKe3JiLe41if0YeSTCYza9ZKc9lmDiTp--Ggtx_TsGt2Bt68olX-CbyM6K0zexPGVWUW2-bT_SJQnDI6Q8_YWMVOO725Zpv78LStKrUBRLiHRvHGcbxRhH1vcHKdkGe6e2qCRQLkoT5ccEVr02YpGkX1dG8pS1ldvd45mk8_WCW8d7dEvaHHmxSzRvqr8Ne_6HtDFIz8l8r-HWE-ZgP0BR31wbW51WYiqHEq1FCmNOpb4RjQcdqgjiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=MDWGL-GmQrJZARkAx0hKQZ8BwIqJEUkiG2vDd-dkK9SqmNPXKEmTbPFG353DPOROahwZgAAyGdp2qqXDKkl6sWIMCJ1N1-IcKe3JiLe41if0YeSTCYza9ZKc9lmDiTp--Ggtx_TsGt2Bt68olX-CbyM6K0zexPGVWUW2-bT_SJQnDI6Q8_YWMVOO725Zpv78LStKrUBRLiHRvHGcbxRhH1vcHKdkGe6e2qCRQLkoT5ccEVr02YpGkX1dG8pS1ldvd45mk8_WCW8d7dEvaHHmxSzRvqr8Ne_6HtDFIz8l8r-HWE-ZgP0BR31wbW51WYiqHEq1FCmNOpb4RjQcdqgjiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lrg37eII5p-KJ2pdIOu3ILn1BlWelYXshYe-05qsbkB-HXrAMEZ64piZVG_tkNVpKyCXICRfeEfVYV3OfwmukSaTg7nR4LoMNTma7DcSlhZ9OzD83rAAYBPT4zTbYfCuq3w7N40PDxqoc2I6qXakTeJIHiIGMns45jluRIiZL8j7j6cYP1eKzAVGLdHjfnSdNm2zkx3BNPH8L3QkiIRVJycPZbjBpTSmjAcUPYZ68E0CoJz-CMzx780aAvcXKXtYNk1HBgDe9J25mgtugnjfP2oyuXGvdQB3ix_3tRtQOr3uLwjKjVkygEfz9V2w7nDzSbQuilOgc013HKyJB18aDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=gDygaiGVd_9DQK5nB2tCiuETMlcee4VOH2ew4rv0e0ywgb4bLYMkm4zJiR8AM05NwYfHOU0rd1xqwJSimN8yH7lfZ6e5psZpB60C6rPf-sMT3pCyfpa_7Q1NAuUI4ajAUmQTyPKJtvNKWboBCb4JP21e1C7vhEazjfOTUM5W980IidZRURAGRGKUnFbzvLOVo-v51-MrZInOdIOLHvY5EqhUA0G3HXJe6HLIx8L0wXEvbMw0fz4-5ynC5x7eu-2Vn2HHQKbDXM-VUKPvonPM13DVA0YPjTDD83WH9ZbLo2f9wkQiYhkSkzd8q4LO4GT2-MT_KIqdMJaqAGyVU3Py6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=gDygaiGVd_9DQK5nB2tCiuETMlcee4VOH2ew4rv0e0ywgb4bLYMkm4zJiR8AM05NwYfHOU0rd1xqwJSimN8yH7lfZ6e5psZpB60C6rPf-sMT3pCyfpa_7Q1NAuUI4ajAUmQTyPKJtvNKWboBCb4JP21e1C7vhEazjfOTUM5W980IidZRURAGRGKUnFbzvLOVo-v51-MrZInOdIOLHvY5EqhUA0G3HXJe6HLIx8L0wXEvbMw0fz4-5ynC5x7eu-2Vn2HHQKbDXM-VUKPvonPM13DVA0YPjTDD83WH9ZbLo2f9wkQiYhkSkzd8q4LO4GT2-MT_KIqdMJaqAGyVU3Py6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mytYEP_CEPACUnNdQH9K1-8Gl3VXIvwudFUHJgg5vzWrWb_gwgOX0uGXtRPbzz7uzIq8Fv3X0UyxECU0PcrOUHHQwQlS7760AahlMxdWgTzGgkHVL4vsKV-rXoAIU6_Ut0r21s-kWKQ9YfY1gG0CwwVYnV-xRulDRO_3KtcVXm_HsATGUG1urtl8c7JnUqoacgrG39NnJ8AMbQS8J_jtrfhX1faz6yiLY9zgdNB9wdiT5eyxmZ23d3_1_JMCjionuSsMxAvFo5PGfVfG54qbd-zFmS68J-0J1iT0uqd-wlm7QL9nwMos0JDYS_1bOmDA-9D8sydAbwiNfONImitqkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=Wi-X-ziC684fwK9l8ZlX3z6-0GV1JFAz3jiAAJCkJgokCPdwQd-9-CM4sWlLtotxUbmCWEf4YOiZ5dJ1LnizEkiRPszuCe752EYLXy7xzZ3dSw0a7sTNRgjcw5WJKVZ4kbf_B-bRTkPa5BNrJlgvq0doHEL2So8nXF-80VBwhyUb5iTv-VbYqchuyWdlZfwhon8T-WicAjdETcrwp_t_yU1icUhai2n7ilQb7eoKow7KZgb0kqoIovijAKWjpycD4OVELyVaG9bPv1leFPi8bBsucvjvdi0I0hMNKh3BDfqS1UzYaNCIHi8noBrNV0XGTXYsvdrBsesohRoUR0plKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=Wi-X-ziC684fwK9l8ZlX3z6-0GV1JFAz3jiAAJCkJgokCPdwQd-9-CM4sWlLtotxUbmCWEf4YOiZ5dJ1LnizEkiRPszuCe752EYLXy7xzZ3dSw0a7sTNRgjcw5WJKVZ4kbf_B-bRTkPa5BNrJlgvq0doHEL2So8nXF-80VBwhyUb5iTv-VbYqchuyWdlZfwhon8T-WicAjdETcrwp_t_yU1icUhai2n7ilQb7eoKow7KZgb0kqoIovijAKWjpycD4OVELyVaG9bPv1leFPi8bBsucvjvdi0I0hMNKh3BDfqS1UzYaNCIHi8noBrNV0XGTXYsvdrBsesohRoUR0plKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJ0RhVkisZYVrYDq95Etcd5O13ob8YmZOHdgSJj9eJitCnZRrwTXY_YX8Da3IO5NtZ-vHvGFM0zoCKY_yRgcV_7LMMsTVu4vLX6LVJqGCm4P-y3dZPCs4jbYgnnWuNpKZj8-pXiU-YS7ycyrG8xrE7ZwltB_rsUK3N--ktlKPClL13jrUfkJxiqEWuej9IdDoyEM4GE7_d9fO5yUPcl8zyOPKyU5_K5CpTZhRudr_67P8ZtolQBt8Uasx-fgaeTIEoyShbZHb8JW7UCnBHhg4C3gZhw3zBeniMBJf9p1GlEKfiVUwpqIE4WRLqfCSFrkwAN3_X60Vpu4ExUVSlJsBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFlDt0ouZLh-Zde2opzvbvWJlWF4ggaxSqtz6QEVrxsKu_wqqiUsaStFvdQ6MSxV9Cxd_CM7G29Ae9WP4sPGoh-HaPMh3zIsVKPFmcI8tNZ8_LcF0xLafJejiUvtjhV8APSX3HgsPiedekMI7lRw-QMzFAnzNOvmnCmycOhb5SJ1ly6RY_7FJvU2RCqB_aqKYUmgZkdnsWp8hibGMQuFptuRymZErK5nnrddXv4UccQgWdNAUmdm2Qrn2858L75SL27P1KFLG1fMg0gxEeSr_8DaB3QPCnDdl2r64Ax-4XQWpZ-J7tU0iGFzWYParvUU2miir_Mi9prLfexV6TOUQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=a9UV4ZDnannSIGmu0N4Xohy-aL5rOdI6Qe8ETb7CvdGMgzihg6o_nCOvd35t4Zvpww2yrGQkvo0WacdQ4IXznFX4D322R8J3Ztwbm3fkbFHISaY-4VzIgVip9y848kRphzeKyZr6s91u9SU8VpH1ElbGkDDU7cK_5iW3u7ubghBLmkGH4dDwHveKmQ2UwqHY5Hr1Cw3Te4sOIAw8fO7kNJCs2SysfvLyisAHirdvJtQQF5TNDmPeQPD0pughS46r3P0O8uAf6HHU8JP9E6KSqXcdKHivzj-9L0pdZxO6xYVaGG4l7bF58GjA2HsTB0Ok_4oU12MtS36I8WXdusaoHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=a9UV4ZDnannSIGmu0N4Xohy-aL5rOdI6Qe8ETb7CvdGMgzihg6o_nCOvd35t4Zvpww2yrGQkvo0WacdQ4IXznFX4D322R8J3Ztwbm3fkbFHISaY-4VzIgVip9y848kRphzeKyZr6s91u9SU8VpH1ElbGkDDU7cK_5iW3u7ubghBLmkGH4dDwHveKmQ2UwqHY5Hr1Cw3Te4sOIAw8fO7kNJCs2SysfvLyisAHirdvJtQQF5TNDmPeQPD0pughS46r3P0O8uAf6HHU8JP9E6KSqXcdKHivzj-9L0pdZxO6xYVaGG4l7bF58GjA2HsTB0Ok_4oU12MtS36I8WXdusaoHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIs4vqmQEqaCDD8RDTd0QGwJgblN0BiQJErJC6bifpNxZV3ndApSVSj8FIa3DT3SvvuENYDO-UNxLxkoqelbDNhZRLCE_LylyGb9ar-I1IvCVnieqnRoYhxomfY7IKHN6PxvZZyC_sr5E1iFjqNRp3wh2cu9Wqp8tfZJY1xhTFaRi0BE_QMHfz-t37vsAun_rSmL9fVTEPvZP3uPKsox7bf1k2ABUTTxANfyikveJljdEkxxWgjJCE5io5DDf4ZoCGgm8S7MWviBfvmC6gqiFgfA_GdOkj9ZzwlqOlCAV6Cjez58ZFq_Xzqp8cS-ju8M1a7xjYZ2PH6H7-tXDlIR9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQksiVq6gy82WtpRyH97yPfi1WzjoG65oSRzNLU4PATSrwmaAYYHsgStEWGqQMX8-4vCoNSQ7ngHsflOG7sCGz2N0z4z-fXTfrRWqu1RjCEl4iYRWWVHWVjLByk13uFTQd7JsLtN1ENWt4Wg7vY_mU9iZJcY3xJZ88sK5LuwXJghv9oVc4hUFMmNX84wPhMIJqzNE71ujPULEXSW1A-KsuPahmEeNXh7mlkaxX7rlCXdjayP0Xv7ZHDfHBF5TWTMT0ffuDu7SmlrYdE5aKUL83GQ04meF4_hrT0a0U9NW-xmGQzGQYeaQaGMqx-jNQGqeVpwhKXS7Pe7rGZrHjcAbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmlUhXjDRsC6-1b2NMcKPmcgTemE_IGXrTFAkS14E6KGRQ-8CyzUwIWG3ouwkyogICgM8AL8rH8lS14eBZ63uqmshyWZxr3QH2h1EiupvQq0otdTIwvDhgIUhGbuiJIDTOZlZNAjY6IDVk1ZYXm6HtF5SQ9DlGqmsQuzWoHk6R5oM8nlYtygIKZJapksFc06AL43c1l47t9ZzBIDrNm1Btm2Qjh6VaIjUKemzRghiWyioW748EeQs3Sz6jswVQgmdo0vLcmkuvPRISOTeWcyXBrMeshMCjB7mtbtdRtO6zw8ifnhWDfof8Qto2TP7DBgnTdahxsnboLANbVNA5-CQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Si3ryLcGLV3IMpP30zbbKfTfx23LRcja5BijyWNAq-bpEo4Y605pHdLOx6d8Zdyywogm4NrwAW5fS69Hk0XXEBi293o33FIucYLJcXaO6ChSsqO_SuWFUn2BbDGBMQKoj5AhYW02pb8qPLRlfiN_ebOqhdgnJq9alRiM8k3vY4BtvVL3QbqG1Zo6t1A9Hx3bczla2xnsOipU_Hu8pxnyPqxW0USsDIkwa-wa_9JtCL2VqGAt2bOKmOeZngHxqdoP_dtnfZM9QBbbkyjoWwFSzScyK24_9oV3OvHV4NLvqNRbAt5X2l7nKRiJcigCtXk9HVvTZ4fytL9D4v3FqftTVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLkQQOYz3KQqK-wuInEYc4xocTwdd_yISK_4x6a0WnzHJwgi1Ep4iPzSYVIFPmJG9ZLiF0priwbJ9dDXS4briFCc_pJBwhUyT1I6OLItu-eWPshkx17-ljCDFX1BmNnJYAw3L0c5sdUQTcEE7_QAZyJ4HhQSPEOPgRCUMqThDPHw6ImS9Wdj_fd2YtpDcVqr3jlTjTnA-T5reUtfZmvTTQ6g-wjg8Yp-xKCTcnUfIy-YZR9eX6P9Dl1FHSwhxqlNmhTCRWiRVEyuHWsyzB8PeZLwanHhzPBGe05uAnbapzoa4nNcMbWiiZ99nNb1JEZExDHxi7y11LCWWXxMIG7Hlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=RTcpNPHVbE-LAXczt6Y8DgtJgG3G9LwJ3011O_DkC1DhPA-coEdgvBGUjKzIvUTj2bE5-ZcAmxP9BJtKWLFUI3OKDMgdP3jGGgQTWliEot5Ig6nbJMyh85_xJ3M47mjJEkVuu119qrqFE-JVia7LIViHyjrRzPtOM43xkmv72V9HfyL79Hf_dmtkEP5furn11TqONqlY--WYQN-tJq20kVJuUOfktXD5FQ0wRsCLjeFtzMRhws-n_wo2untyz8TjUh8zTnb_Uoa6qkA1rw8rpTp76Z92oo3CgOibBdE47Dg5XUyMWJNqz4EIfx5NswRu9LsNsAjCiS4hvLhawKWYsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=RTcpNPHVbE-LAXczt6Y8DgtJgG3G9LwJ3011O_DkC1DhPA-coEdgvBGUjKzIvUTj2bE5-ZcAmxP9BJtKWLFUI3OKDMgdP3jGGgQTWliEot5Ig6nbJMyh85_xJ3M47mjJEkVuu119qrqFE-JVia7LIViHyjrRzPtOM43xkmv72V9HfyL79Hf_dmtkEP5furn11TqONqlY--WYQN-tJq20kVJuUOfktXD5FQ0wRsCLjeFtzMRhws-n_wo2untyz8TjUh8zTnb_Uoa6qkA1rw8rpTp76Z92oo3CgOibBdE47Dg5XUyMWJNqz4EIfx5NswRu9LsNsAjCiS4hvLhawKWYsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=p-zx_Yjcap13l8V_KqTRe8hudTuTP8NpFPlGWGq6R4KB08TIO7TB7-90gKuL1irXyyFDTp_qjA8nyXhr2suSPcZrL6YMukL9l64CevnjKB4QxGE3Vdmbv-2iVDP6e4BPJ9ii0JivG3yajBWMeIUVwc8iFdPIATRxHDchWQrESDS8dVX_cDKjI9yB359xirYQyEN9rlccXz9MwKe61ZQtN1DPmqgZf0OcC03P98NNZlVPEIs_3U6NgAD_Dwy4bCOCuyQ3BPP1cI5aws7Zkhld_HsWcb87DBHg0uYcNqSdtfAJhWMBOKnFO3xZoxelQ1ecXi-iN-eB-VLLT3bBOD5VvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=p-zx_Yjcap13l8V_KqTRe8hudTuTP8NpFPlGWGq6R4KB08TIO7TB7-90gKuL1irXyyFDTp_qjA8nyXhr2suSPcZrL6YMukL9l64CevnjKB4QxGE3Vdmbv-2iVDP6e4BPJ9ii0JivG3yajBWMeIUVwc8iFdPIATRxHDchWQrESDS8dVX_cDKjI9yB359xirYQyEN9rlccXz9MwKe61ZQtN1DPmqgZf0OcC03P98NNZlVPEIs_3U6NgAD_Dwy4bCOCuyQ3BPP1cI5aws7Zkhld_HsWcb87DBHg0uYcNqSdtfAJhWMBOKnFO3xZoxelQ1ecXi-iN-eB-VLLT3bBOD5VvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=mtAZJrwyCagRvH_1fUdP8Dsj8Nb4JbOV29jvTNz9Q9qGsNviqo30TrS_qG862eRmzzgok-1LOSSaaaINTh70FfFBkSDwQk8_Mu5Ko1gq9QEU4TTkGvT9ASgocv7XAm88NUlKodLCRQPhxYwjhp_hSafiu8I5oJPn1LCW0NZNxUpPRv5Jm3dEXHU5RpTV85jUoPXUx6MOwTlvrXAhgzmSXmxSol0FSh6YKkxcjctlTuiM5LaHfTFFJnD8GIU4xkTWkf3Ng12lfK_907eB-J04j2cT8CKy1zkc2dGRd9QvHd53DRKm_8F6a4dwctnvk3OmCZJ6SZ7paH0XCCLuzmFDIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=mtAZJrwyCagRvH_1fUdP8Dsj8Nb4JbOV29jvTNz9Q9qGsNviqo30TrS_qG862eRmzzgok-1LOSSaaaINTh70FfFBkSDwQk8_Mu5Ko1gq9QEU4TTkGvT9ASgocv7XAm88NUlKodLCRQPhxYwjhp_hSafiu8I5oJPn1LCW0NZNxUpPRv5Jm3dEXHU5RpTV85jUoPXUx6MOwTlvrXAhgzmSXmxSol0FSh6YKkxcjctlTuiM5LaHfTFFJnD8GIU4xkTWkf3Ng12lfK_907eB-J04j2cT8CKy1zkc2dGRd9QvHd53DRKm_8F6a4dwctnvk3OmCZJ6SZ7paH0XCCLuzmFDIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=mHXQEGc0bpqEzaO4StL6En25OXvXkkYNNQLJMkqXXlGp8SH6FjnL4ebjJy8XbvExttRQv-0npG63HQSWXGAm5jrYb5sy5GCANy0E9rzZ-SosXHrqkxToFZtGmq4oNsBbB18Wgz2uK1q-LYjMN1j73rh9qY8YsSpoMs9VQKqJKQIZ3SB9XRP_HaTDbncIJY_I7v_pyOcT8112e8EL3Z-cdb5nmQh-ite4tQ5rS29r6aCL41qkOUAotcgys5m0SnTVVMWZnZmfaWjKYhKxZy0goC_UgU00AIrN2XFmXZqhxvwYG7IRjzZhjl2c-fElzgMhhembMIsMciPsD7so1jNH-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=mHXQEGc0bpqEzaO4StL6En25OXvXkkYNNQLJMkqXXlGp8SH6FjnL4ebjJy8XbvExttRQv-0npG63HQSWXGAm5jrYb5sy5GCANy0E9rzZ-SosXHrqkxToFZtGmq4oNsBbB18Wgz2uK1q-LYjMN1j73rh9qY8YsSpoMs9VQKqJKQIZ3SB9XRP_HaTDbncIJY_I7v_pyOcT8112e8EL3Z-cdb5nmQh-ite4tQ5rS29r6aCL41qkOUAotcgys5m0SnTVVMWZnZmfaWjKYhKxZy0goC_UgU00AIrN2XFmXZqhxvwYG7IRjzZhjl2c-fElzgMhhembMIsMciPsD7so1jNH-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA5nLT-Xret2M2NJUbcoeaF5Hhhw5sJNfviQvd0A0zjv-NT4wnhzokumryyiv9mMv50QgqjG_an-bFWKLjTxUov_wfrKEJHe8DDKKgz93YaYS-FOXRF9oQOvp4kgDnqRBg7W2qR0L3sKJo-bmUVTAIAVq7v2LNRqUmSyh5n1G7cXEJKqBQBRZcFkKcNNXhwPGgoAVFCKUfByKV6r-isBazRpUJs-iSTNmXSIMLjn1rHyip8KcWfvych0oXMij8iBNkNp1BKX9ZAQkEmjC4PTtpgTBkbYVAfvsfb2rDtkQgU9YhsuV5SbYVHfAN88cLVsJYfHOzjFG1X29N3JW0EcfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6jPLTMdnrb9sv_W97dyGzSHeKCNkSkeXo6JuqVP7adcG9_dFnd0hOzL6WEnrahj06vg1nbtAdUbshhMR52-CghHMIJNQk5TiYd-jhrXeOICcYKsoTWmiReLhJMLjxosftNSv7i-SdTldqL4SPXwMJhGZ4KplbeqaqeFGet_hxKQWGhHNvPY6wLvom5m4zpHduM3Jflb74d5wvJM3Q3soPuA1AckZokGNGhnvfPshGwMi8ZSWIxcsAlVijUUsW3-DdfTw7YlAKkOgFUK5I8bmq-D_YUADLykO2s8hSgwhXIJN_lx3MVdGTmsoLw8lFL20OvR0HHiCENDgy1SRsWT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=XsMJnMPCfjqtCXe2cV5KnM7APVoMV1_-ODaV9EwjPXiC_5KsfBz97wLnJwuLgYXKwXibAkWt6JF7AFywVPXYipSMDDHWuahsdnRT0ebqVH7kFiuh71yYA5qKkGm-1iW7lcE3Ghr9iiH2I-c0POp_pRuf6mKniwCkvImVXWtCBqqPxlIHPdSL_xeV58jbuKuh7FFRvoWSFzVWqipg1WloJVh0UVVB_cQOLQpFMfxqQlscjgVA2vUJJggGN1VWf87xAWHwjg71dKhAi3M1rVaqsecjOU6lFodze-6dab-3a-UTCYwBLGdzi-1MnoH0Blq0DwSXXwmDLPhNoxXSDSqLmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=XsMJnMPCfjqtCXe2cV5KnM7APVoMV1_-ODaV9EwjPXiC_5KsfBz97wLnJwuLgYXKwXibAkWt6JF7AFywVPXYipSMDDHWuahsdnRT0ebqVH7kFiuh71yYA5qKkGm-1iW7lcE3Ghr9iiH2I-c0POp_pRuf6mKniwCkvImVXWtCBqqPxlIHPdSL_xeV58jbuKuh7FFRvoWSFzVWqipg1WloJVh0UVVB_cQOLQpFMfxqQlscjgVA2vUJJggGN1VWf87xAWHwjg71dKhAi3M1rVaqsecjOU6lFodze-6dab-3a-UTCYwBLGdzi-1MnoH0Blq0DwSXXwmDLPhNoxXSDSqLmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilvi6Qw0v1kL2lTO11xN2G3R7dHPyUDC8p0fgQ_el749gd35qfE5oYW-4hq5QWiXdPIBVvhkPBkIp6jAITrEv5_9356x8sWJdkfRmuK26xonhugo6W1_dL6_LAJjTMoVcj7nknRSI5OaYTsbNE6_BnHfIrGKIw7T27kiYtoAchQ-khAg9hGf9KZ7pfBm1Gh027eLLySyDRJ44LF-WbEFLl8jbJU-5kuh3AY48CFrHLNp_WHsBpcwLlHv7dpwbRomK-60G8uKFOL9O1it9w2KMK0nSwBOPK10qRozuKjC6-c_PaDX_19F_SxSTMcC_AgIOoS9XLODbw2QNy1wr6ropA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=eMBX8_e7N6zEifTVV5DG5nEodld1P9m7aC17KkiAJyNmyotmVc_xdqnCmqW-l-qp52GRg_-RpvlouPEMh8kQLYvEaeOxoJoVxpoW4fomWxrtB6d7kkysYQHeeLj2-fA7y4YHdbaAWZLDMLdjWwJnAxSQG8IX8QuTVn1QoEloxzfv9VzLNmezPT8LWWcRcjUXzLNOIC0iWb0EgS7gsJ8oCZTJBXlePKg4D6x4DkXJlTXfl_OvQLQGlhYkyylQNsPyLBrblyz28osCmCxU3O3SsuqmFqW_nyaquZDwTsUTXSC28CSk-8ofF2dm031vz8a7qmkDZaQ_b52BFYe8MzUOTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=eMBX8_e7N6zEifTVV5DG5nEodld1P9m7aC17KkiAJyNmyotmVc_xdqnCmqW-l-qp52GRg_-RpvlouPEMh8kQLYvEaeOxoJoVxpoW4fomWxrtB6d7kkysYQHeeLj2-fA7y4YHdbaAWZLDMLdjWwJnAxSQG8IX8QuTVn1QoEloxzfv9VzLNmezPT8LWWcRcjUXzLNOIC0iWb0EgS7gsJ8oCZTJBXlePKg4D6x4DkXJlTXfl_OvQLQGlhYkyylQNsPyLBrblyz28osCmCxU3O3SsuqmFqW_nyaquZDwTsUTXSC28CSk-8ofF2dm031vz8a7qmkDZaQ_b52BFYe8MzUOTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6cLOHpZ2E74qXG9gnveFJWdgrT8aq34on1E0wUC1540tKd89_FWvHqLCKszeWvKPxiuHz-N5EFY4tIkuissOaGe6C-b3TtPkMVXjcv4DSXqgqIvMpOyUOdPEtRCYhLcytB9d0t4KfKYOq-ro65lXHSRihtEWj7LLLuiEM0vqUTYFjp3FURN956_hDuyjrU5uPB0XF_QqzaEhBEZVV2Y9RLeK6jUzgtM-R-ec_4RN8lGeSwDJ-98k-gYpW0c01t6B2RmzGTL0mnVBtiKSLZm2V8rtofsp39CqBbCaN0wTPV3zEuNevUo9YxANVIizf2eO456-UjthJoGQLFydazg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk2oTl925hP88HjUNgc0uhBUW-VhXkz99R_4G-44C9vdz95A2Mx_OvRdQcPFhSQIRji6jnWENLnZOmhPgxjb_QiL8rgBDNuFI-Jp6MjTIF3ucrfM-f6q82E50aqgWEY5JVbvrXUL8h_RdRBBjpdcpIU5nbwzbRRDA57Xhx4bUwQrqzHWR_XPNX2r0x57GsWXp377PRmm-48HdQAJ-CfTpZxYET2085YdT3nScSzHV_RKXL8wFatybp7Bl85bwfEtxqsuvJeYN1RaJbBeckLgX-rQ8M9nIqfMV-VIFRXmFnK662vKUbeHw71MMYyMc8Tg3okiKrCCpwi5zrMKFwQ-ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
