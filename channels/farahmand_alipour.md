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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 21:39:50</div>
<hr>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFdFiG6Fo_21l3eI0g9gf5NGpCehHQROmy9gqjvXJpYJeTEPafgkUx7nkUKtMtjFP9wIeLMyJeCLfsclv0NiA-jEOkHOW_CEpgQ6_y8DF6v8l3r6VeLmhIvk_r3NCqjmuu18gMJpj9xRmp9ZZQxCwzTEqVTK4KLA_Fl-R7i_MS7BeJ8rqZCPWxPGw5fQ-zqyKEpNrHL2d2MktcW40qhVBwp2CPrCbKJVab5MSSLSKFMpulUQDNlhAT33DH8tamqPJNB-5RSGquoUGFYyPHa8ivRjt4VqG19a2mNwpC9ZlUClHNenuM5RQAb1z5EazGe_BeH7Qtjgg7ZKZ9yRI8U_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6jRmf0ba--mShtp3pjmojRkhZCp-yUBEnp6GPKvFtb3MMpcG_cIQzwaod3z_JK_RX0WcI43aGl1PG8XmYwzcaGgQ7dZllPn7bL_tAMkqu-e8pnolZdB-Q-a6S4t4t_MRQdvzC9tEcOt7r153fqzATAH8LYRxtoTYUlgM0XHwMTIqMH_IdvxcS2oe0cyQ02n1aEQvjki0NWaxnrRN5V256yS5ch6xnrJnJo1ycvk2uS2MEvUjvXYooNISJULVTX_0ILL0iz-jyHamKmAPPmPccXw6i0CkTHoLu9aZhHWnUtG1tZkcqsayXmxDu17jTsRr3B5DD6yTk1vufypS2cbFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTwd1PZgtxyk9gR0BeLXT4HH9NJBSEv-GoWmPocklLko1kaf4l4DSkY9gdhkW4GEPAsm579GvpZ9_dMnFvPFrVpeK1iJRhpa8vifE17BpLQfhr00rnK0v9UOaUoQx0Zlns4m_NNYZexTlSsx5rUDY8aQqpxlf5sA4oFXATASdDNmK2Y98zhpHZzBw4lp5UK___g91VDmTjZrzpCws2F7aCKct5QozVKtpMYQioNYpZ6C-NTK39I3tKuP4DiY7UNvire5mXpaJMGhznMxllPphfuXZt9XMFn50O2x4KQy8iMYXDSodh7H1RsaW6fBRE8fReRavSpm6NEm0AAXNKTUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=OPq3cR3Qo6hhZnA544SqRW1zTB4Nc7i-pxNq6PjN4uhFo-_0wZTHtg-dfM7qan4ntEVLD1WuLx7zl4RzsQBcqfOHiF03_1QHFlLKvVzGwPIJVwi-p6qQ8NIutEXCXPBBndmLWEekyj8ld8uhibLR3TEV92LFVBtzuvjteIA4wDhXKduMmbu4RAkeDixWC4Dva9fREoYIASDk2qsAbgq2ENcoNCsfwTedn__GB8i-9KpYglj2M6TwHWX6IdeDs1plcYTF3Mdghowt-a_liRTVvPHYxlNV8nUTOXWf1Tk3cjlhqvaufI1ZzvR4HSrURn57Pm-0gBleuhi_atNz3OtzRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=OPq3cR3Qo6hhZnA544SqRW1zTB4Nc7i-pxNq6PjN4uhFo-_0wZTHtg-dfM7qan4ntEVLD1WuLx7zl4RzsQBcqfOHiF03_1QHFlLKvVzGwPIJVwi-p6qQ8NIutEXCXPBBndmLWEekyj8ld8uhibLR3TEV92LFVBtzuvjteIA4wDhXKduMmbu4RAkeDixWC4Dva9fREoYIASDk2qsAbgq2ENcoNCsfwTedn__GB8i-9KpYglj2M6TwHWX6IdeDs1plcYTF3Mdghowt-a_liRTVvPHYxlNV8nUTOXWf1Tk3cjlhqvaufI1ZzvR4HSrURn57Pm-0gBleuhi_atNz3OtzRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqT13RyNpxvUyZxQNFhVYfQBzIKdeLIX-Wx3tewxuP5oCuimFJi1Y5a4guXAEES5e8XGvOKKLIw6w2W8sxvWzUSm5sgZb3CV8xBuEDUFtVGBC3aJbm5RpA5rbTftS0PZVXW4nKbJ6L9AUlmHbvEORdos0O3eW-Nfzafm_GNZ9Zcda1j34Kw79jObwWkAc3s9iE-X3J8S8mAPJbf8eKKGzkPWaMau4hePQz85wBuhjEi5wb1F61e75ikqXinmHFmfe2Y2IR3XR3V5HrAwU2rrfCqvW12n_87wCDI-Jzb022Fh9lnpve7BsPj6WTy2uSRtmxHaYXGebIsa4ghxxdVVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXER_l-LBMLiXUNB33fB_pVLho1N5j5geqD5iwZNSCRZeRaXcPR7rODAX_LnE_Szi2zKRCO1dAeb4GSYNlF3ZuMKP9cIRsGMs8d2c5GDwFlyL0NqOO1s6CBbPzwRGKpBL8VALtX01MDiZ9uC0mw_7aNYkVfOFsbc5DANIYPbEomTjZs29DVOQXCRKvXTLxn5HkMMkcvfugzA4UzisZck7ljHcJr0AnO-3h8jTuHpVBd8qqP2r3UZYsqzqfsRbZqv82noRdl9bdBw-jZEky-ZpfyQuJew0FLLrHYpMZVyFdf9MAtj1nOVqLTSKvZXIDACEBt5TJcrjxRta6sgm1PiOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnmc5BM_BATfxTXVABN7ZsU4BordS4eNQI6aaqyKbrjAug-1oqbJULpCSOPfYakPPn9IZ-6ilxl52zQpXke46Ly4mAhmQbWX1Z-k8r-YjEO5u98NFLcVnFff2kRgvZENkQp3Q8xpJFa2dMWI7VyX4iTJmhsmHCkQtgKwFSju7nd03Nj2PIswXOa_UUSqM0_82PRRv3-ahh0OTttH1aNBrl1m6_5DFaf0dRXXf850tcCHdoK48olS356kVX0TxVUsYSMYuzq1PArgATXEtYix8B3gPpmYgj1l3V0vn4w_UGUYBUHR2PpUbchJc90kbBcLfX7eYs7kIprTfShUcLr9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgDyKCIFEawQuKRuajP-DVDVTd1Ga_rSK6An4FYmu5tAxlv8-AM182xBy-1fvpLGrFjCGZX39Vo7QkyKvO30VeKd_jP7vthJv0lRXdNVVhyOaLyaR-qf03n5OxQDg0BnkhMPG_ExvuGqBr0AqR6ZLJ7PPXXYhIqlOaEtqa76UTwGmDHsoLmqho03aA3OksSX7YPHfJjA-3dAGodheWP_4wVpmOeQjI-0lV_0vmjOgko0kjmOcv8PiY5mHQ8zjhvpp4Kf4HlIcj4xwp1SqVgbXdSPimGzuTwkRdj5N_5y4u_8pKUnW69mkSrDfgKmci98brOZDqJb9luH274MhlwRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wys691tZHc0ysggM0uvwTSlz18JVAsktOQ3N7PjpZyfX8FOxchu4V-CS3Zyigm1NyGaQ-pV08anyiyUm1ZSEFLPkIMYanh3iiTC5U-HIIVBRaXeKtdmd9G44d6wgAqtNlLm8PYI9Qj2otcbMco1PGCKijix8TCz6x67n0vjW8tWJaX_dCjBq8W5QpIo_MfQzOnfP_eS4XVkUQf8NTlaSpQDpVGnL70SYjIkuyljv1etK3242RmkNJC-M719Nt0YfusiQ4V2-3YHFMW5X4m_dFwUrBPrLQMzVYaQKkCm3coiJThAwapr_sTfvW8WQtHQsbBFe1YKH4dyScCPFqcf_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=nV2rp0IqGTOt8rNdg8Rfqci2f99H-lVgQn4qIzHBGsbsUeVX5Jqm1eS43uS8iF3-VO4P2Tsabctewtu8N4XZ2eBQ03H5p4J51nUCo9-mFaMMZsZDfLYOvu0f6mI_AjHpm4mP0M6jESEM0ZB4UPrq91tlveHa9694SQyXQHNJfVNfXVTq0xAmMBRw4E0HRxeh8V3A1bqnufXMbOoeqaBPJlXWDx3DwcxzJ5Ms_pZF8bGa2b-J36z229A1sHcyyoFXkpszutR9rvDejwU7WZ94sIEkY4frOMXe9kPCU-5Q1teF7Hj4R-9FRssFQ_t8aSTrEfuCtKvL4rK7l6iMGXxo3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=nV2rp0IqGTOt8rNdg8Rfqci2f99H-lVgQn4qIzHBGsbsUeVX5Jqm1eS43uS8iF3-VO4P2Tsabctewtu8N4XZ2eBQ03H5p4J51nUCo9-mFaMMZsZDfLYOvu0f6mI_AjHpm4mP0M6jESEM0ZB4UPrq91tlveHa9694SQyXQHNJfVNfXVTq0xAmMBRw4E0HRxeh8V3A1bqnufXMbOoeqaBPJlXWDx3DwcxzJ5Ms_pZF8bGa2b-J36z229A1sHcyyoFXkpszutR9rvDejwU7WZ94sIEkY4frOMXe9kPCU-5Q1teF7Hj4R-9FRssFQ_t8aSTrEfuCtKvL4rK7l6iMGXxo3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYW-0hppHgZkncQmaLoPbNFCA7nnq_412qqeiw46zQ7IkdCOCKXzNLIqZ_fXrOV2ZCHmPJqtawymJLfysv2Hv-IzwTDIVp4rkygf4Bm9hJ20k_hXzc61BNPZCSn4KbLuxNcpjbiMQRLfZO_3OxarmjhOUA7TV-VfPO1RyC9pAkpuBy4NJ4arlgM2enztYz6a2UHOAEZnuXvVrOso5EwBF8zZDRs-C6A1ZMPw2vwe1j69VzjVJWy8XF5sRoWvMQ6P-QxV8TOOAGh8szqftTVbkn3KYGmS9fXWW269Z4Jq0iEa44IDnS26GhoMtn2CTvpAW6gkaOZZ3Eb7CL0nndmPiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICZXFjdGIs8Knq64FY2jFvKeACDbKsj8oamY81nIyvvqfdM0-8MUQ0PYRop4ldBrg_Mq8jvnFmndiYZ9aRL3gRd5c8CpgG6DEo_o6H8eoZ28rCh79cRLhPsTmRnfC_Z3L6bLQMDmgBL87SwZJw-1SbD_XsYWjGDbFJM_MzeqJquVxDla5yNE0bUCbgBRq3ORgemYqw28ZClplO15-9g6i68WOonB6XS-1GGNS_10duopaIaVoEqQ7eu5ngZb8p1VvjDoaHJbL5T9Jt7Y8ymFcSfpBxYEGtPZ8OP_jlPD5VtHnlJGCiZOkWRT8ptX3KiDR9qGVO9a9q9ejBzjZ-gu4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJ3tSIfUXgpJAlhcezwE7hRNbiy_2vK8TbxJQSUXKtf6bT16fDLGZWL-8aHksUHGe930zO7sbKZQhA_wVzkF3jjKVp4MF-uaKOqn0-5PA_31rXO3AQphmF8yl3PdDaCIiCAXpBAPrIaPRys0l_hmRvDAST7kd5uFwDbd94GXTqrzPoMvImenoWP8iCKKSqdCvggtL_f7_-g5DoWTCyrRgSgBahXna6PxK8eVENMSC6JskjzEz1IRc8K1JULLBqzOpUtckzeQUGE-2CXCjEDCiToRnr0DN11rkhRdgBUJgz0DSwg67hqfT6L6esGD2dmqXDTK-5SsFhYGxMRRTQQCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=SjJnETw62cNz1rRgnjHcwrTQo7O9CGrOCFqmspjJ1p1SB1KsXeYCXIoS-ukx6Tv-8Impg0qg_8VNizR9y5yWoNIR74UkZpD6VDu_bFE_FanlMHHpzH4uCSh5nmG3ytlK4ebp3XB0yovRKY_I4q-yLqOINq27oGxYNqNBrqF9myPLiu-sLeaWRICrx526YviAf6sp3NCACc0j9lk6y3hbKzWx1r2HM-8u96yppUN0fsFx0-4HaY1ZYQubFsPzrWjnM4PDBVQ_UbfOnEWqPxx4iWgMOxiBXTpJaWNV3VnM0hh-Dre95NCslfHpkrNhaE6QZz_A5N5-yzfAm94VFxfP1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=SjJnETw62cNz1rRgnjHcwrTQo7O9CGrOCFqmspjJ1p1SB1KsXeYCXIoS-ukx6Tv-8Impg0qg_8VNizR9y5yWoNIR74UkZpD6VDu_bFE_FanlMHHpzH4uCSh5nmG3ytlK4ebp3XB0yovRKY_I4q-yLqOINq27oGxYNqNBrqF9myPLiu-sLeaWRICrx526YviAf6sp3NCACc0j9lk6y3hbKzWx1r2HM-8u96yppUN0fsFx0-4HaY1ZYQubFsPzrWjnM4PDBVQ_UbfOnEWqPxx4iWgMOxiBXTpJaWNV3VnM0hh-Dre95NCslfHpkrNhaE6QZz_A5N5-yzfAm94VFxfP1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=nfIIAg6jAH_LQbWIfus704kMB44uqf-VlcP1kt9KDfzW2_slEtBXqzaWx5nC2PFT_EokbDQ6UnVEHYXpKZm1joj6Nj5mkJIhzc5qPm1c8sGor4vU84BEUi-Rd1WpUEx3U2zVHEZs17lKL3xSDfrbOQIYlukAtR2rVvbr4hU4wcvhYzwuzFAzRoUAzfR9m93SdXD4kMJ48z8WuI71PufaP7G0h1eR52t8vcbX2vD2VI8_Fg18nl7IGWZJuoOwQTw4aP4geEi1BGfG5qSUZhYW5q1n1v-m-PjCcep7BnxXCUgEDN2mjCkOHmo5RNkhclmJdilqZ-Kpvoxot650XHr4Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=nfIIAg6jAH_LQbWIfus704kMB44uqf-VlcP1kt9KDfzW2_slEtBXqzaWx5nC2PFT_EokbDQ6UnVEHYXpKZm1joj6Nj5mkJIhzc5qPm1c8sGor4vU84BEUi-Rd1WpUEx3U2zVHEZs17lKL3xSDfrbOQIYlukAtR2rVvbr4hU4wcvhYzwuzFAzRoUAzfR9m93SdXD4kMJ48z8WuI71PufaP7G0h1eR52t8vcbX2vD2VI8_Fg18nl7IGWZJuoOwQTw4aP4geEi1BGfG5qSUZhYW5q1n1v-m-PjCcep7BnxXCUgEDN2mjCkOHmo5RNkhclmJdilqZ-Kpvoxot650XHr4Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=IIB-piixVm3eH9Qi1HRYvMXV1oo1eGiTxBQEuVwlkTacIhhvNSnbLzT0xFNI9A8pIYPOWiOhWjTCyCCVwKIJQ5hcSQx1mhVWObIddrmq9cBxjsgn9_e55qOhwzGO73HXBRvZJghSHvWELXKRIHf2d7nQYJJzMpPFnwWW0X5ZbTfnwA0UUfqU7N1ygKVSPfDYrN8ZVmc7o-SApL1Yqe4hkPLXDeFJcql7ixkhKf2t3aSNXAMoeT5UZRTwsBs2x-wNg9bkLALvu1PbmuH0_jeENQlpqAaVTnGmnHqLYWDRdm2YVi9PMW4A599VYTNl0oZ8NX0cpji9zV7xSXieykm_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=IIB-piixVm3eH9Qi1HRYvMXV1oo1eGiTxBQEuVwlkTacIhhvNSnbLzT0xFNI9A8pIYPOWiOhWjTCyCCVwKIJQ5hcSQx1mhVWObIddrmq9cBxjsgn9_e55qOhwzGO73HXBRvZJghSHvWELXKRIHf2d7nQYJJzMpPFnwWW0X5ZbTfnwA0UUfqU7N1ygKVSPfDYrN8ZVmc7o-SApL1Yqe4hkPLXDeFJcql7ixkhKf2t3aSNXAMoeT5UZRTwsBs2x-wNg9bkLALvu1PbmuH0_jeENQlpqAaVTnGmnHqLYWDRdm2YVi9PMW4A599VYTNl0oZ8NX0cpji9zV7xSXieykm_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xz50T3V6XhV3sEM4jmzVnYvK-Q4544eGfw1YHU-jfYWaNZb-2sMSMW5ImKze63-DRgOepiDbpKN2tZAQC4oovezar1ZFimjAmY7Bau8omiyEmtiUn715padCdBfutYcw9ginbt94jBApapSw8y1ZHPDYc399TnPcp4nH756DqIr8Fu2lU5__ZkgwCzBs27gJIhepzWStM_UpgxC2u4ba2ZYzwwDR2wJNbQgHePtfu38NDM7uoAJXiEjSLpzCKvHwDOcYrFdj66UmLEfPCrw6N0F8sItHGMPhhRB5j3z5cLatnWDvflmbECoiWe6ZFMOwu24-1kNRZyveW69vGiGkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsRMWJLGfyMw4HP8nV-ondEr1JqvB1-veGfDUbPKdByoBPEdOXjxhWDzLl5RTiAUC9miqDxpu0Dg7jdRBmLhC8tUA_rozuNIgxLPAiY8KbZYSlM-2-W1DHrHqt9ACO-ud5WUULmxlrCUfp54I15rU9KsFt4-zBYH9ZFhvg2_EcAxqqBxoURm4tB5rkcRqFZBE8qcawiO7RVTPVQpctpIMx9U3D8TvIfkaMuyM90FIhUzqb7hFH9HzVZpD1xiFQLEDrJz5Wr2MqBn9Gvvxk0WihYgOmUaTQ_TPNTT6qh0sazmQFBcmUe0etJB_ZZPugtamB4hHBkLoZ8RwT3XAZgkJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7S7aqzKxp_V5Jwr7JHH5X8myehlhzbRLi6gvKyO5BK3QaOoaoL7J4OVPkCuiysp1IVvSi8GxkNe0QF9QL4j5Oe-8fTeANQNFA58KL0_b-X1nEfLHbgTTaEBdxuztrE3ri-tnmdg5gZy_myK4ur88dmvP6A5hEG-2HsyBVFy6fxKPrx9lTM0jLwI55Q7aQ-D2zvjv1aRIZW_vsJ6nyua9Vzhd5at3QqmpozwqMQYGDGtbvvITDvOFytb9JePhR-qXadXcIiLTsnycA4H0RaAf-aC6FYSLnCutIojtKpL969RtG7MVRKnz8xVAlUgZlrYBGDpiLmTT-NbiMDxVTdX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M835PXeTYBuNr_fH41zh33VSasux3f34-EKywepIuRGAgt2G8LVyZ6V0IcqYIfL-DNGNPvGYNOuh2ULMOMMjtQEJkwjmxsY6M2LUJqKx1kETTVwcoIwQJwYH_8NIjQQmv7h--9TOYDmmAsp509a19LxTUj-9aklrjHGzh_jlk0BQGum5v2oG18aEJqCpgmVtm86X6VrHxns0SQh2UgtwF41Cos36pAQDmaiqOjnovUqu7nfBfiB4G4mFGmoB5ZwN_7Vw1nUnAVV0u6ruMxLEL-p51wexFqVapgRANLbsF12dXpIN27zJ8q-A4j1N3QSNbdk-icaGlYoGS189sSY_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LlCh2HBfkJDX76ZFIJTWCpgXdhME4b9N-xIyD2R0k-gTn7WgxBa_kyxJBt0SMIC70hUgcIvgwzffFV_NG1iXyJpPdKMO733Zhh-7WcXsoXWtwIDdlELUqiZJ-lz2jSWjtV5-rVHStye3kVbbmAWtNWvA1GnH0BKyNobpgKX0JwSR7TdKOj2B8vTKNNBTwI3FhOWR8rKcuDXQmqDXb1HDwh2YhyOfVlgGaGXaADrPrslAUSi1Hy-45FoTX29JxTtd0bCQBBZBVfD8_2PCSn2Yz_wqCb_kYSWAaErGXqeGux_wKBvIwOTY9jXH2UUfV5x3o4LDiSZhiq9Dx4s_eWdJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlyanfVPxTkDyJ6GVq-hUPpdaskEEn9nEPIKR0ftiR5gMPzmCmIAwEK0vbXUl0M0xgHSMdZnBXljMRp5339KWq7UAZbnpp_w0j0jlgQsamkK_3JBbiadd0o4ZDKlIkzPuwBUCO8UdL9RiPKP7rw-0VEiCi20My2kqcKuLLdwHr8SaARXcj4ohcrTngs3OVL7cNzN9nJBASBcX4o_bmes7tF-f6UV1j0ADrPoqB6fvTEjPko1H7fxZoWOR7E2Ov9sXi0oh6lnSCOPgD2r7JxayDAFMqL56WFkAlATGAgo1c-up0FhiK7Kfu0645p414hHOjWrXfLHQahF7tBSlO7uig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJRLCdS0gzpNsTboqvdRg1L2DI2JY-Fdpin-b4VHJMC9Rzo6-XUrY_a8iaBnvd4p3J2GUmEQGcGH5hLMkgBgjzg1Uri8pH3kAGcoEqumz_dFCZgo_TSvfJ165uw9cmd-s9rXVxUh9OtY6vZsyLHBUsqLrr1cLYQqXtzmaMlNFZn_R-_N4WDxn3f962zJx3J4XJP3SS4bQvZI6swleQ3oEcVwMjZ-B1DY65cSRPUIMoZK4odFUnih9ywEU4wMXnQPa3mnm9c5sDHsuYNz4TatkzxnTa9ng7MnzsfVWDOnpmbIc1ozyxlpDfQ1lcnF4sqrRw32ex5MC70hPF-jbu-EcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I48uFUH6mB3j93s7c_Yf_BuBotVUrxfogoqmi7HAzd_InxkHmILFPnv6HOp_vtWFchf0_7uA5-dEh2E_bkTrbF2FW-ruYWXiOcMBknXQhXaWJbw3S-Db0KT93FlTPZubcd5IwEUz-oiPMhl7aw18PSDymFUYp-SqLVOw7d3nYQdWMaCAMYZhMcy9owKzBDcnPb1cDDEzSQZoB9SHCdMUbendlg_ng1zTzO8EKz66RzIqUhWveJKzFbqgUxqH52tFeHzjnok71dkk5kq56E58Mqdp9SOUzpH-pRk8m-BFKjiXdWMgn9sVnvFVbrUKqD4ZNMZxC0eCTNLaqz-b8JLltw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0r-QVGy37Fgb7nc24bcQLi2Y3bdyeCNX4M61VWoCjkmn5evj4qGAu7nOKDNKxuIasj9NM104K0P-hqCFRIn5tnVVpHDvJBCaQjTSXm3DVnn-XuTCO4pjS-VxzwKq1OcqkOxzUBUWcJDNBoxWN3h_gytLHLUKb7KjWyXH9seG_YWffTaAZPQh6dWtVAxVvtdcakcQllS75NFusudvg2dVpANzF4bP9S-hJCoCjFGK9Ai7getIF_Z0Uq-P7Ul1dqP9GHccJYI-rYRAPW3rXgNGWofKrWbaxxfiOf7X3OT7SaI1I3Hos6izK9XqDAHV0NJYdyGdb8WvbKiSWm0HLhNRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWeKPo3E4TADMGlM--3PSRNyIHq96Boz5Kmlzf9huKbUOzDiVbwAcEFLJVox3LP11ifbNQXs25lMZi0-DcBVJVDdFKAZ9yCmryKFT0f1nDZwwyiPBqaq_a-S-WmVgfFTg9nJc79zavJmI_LDbrzwN6zeEyOytqZRjQeyqF1GKRqbLT22G8zLGXS1Y_ksiD3xG1vWW6c2nt9_2lOD5yZJmJyPdMc0VcybH1eX1UTk8k_lyDmnKwx2ZTiabpvANnmWCiRIJ6ZnhLBWFt7de9PolPbN_pmrWJzur1WAzFFi4WH8Ra1ih7DAEPOu-WWus2FDQTXnMS0DPMx8Mel1xhJmbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guW3ioc2SNjXpL2lYx2mxaxCiAWt4qjr1XpNRm9-cok8TmZlxwPsI0KAApdKvX50Y4s2ndOuEo8Gtx4Z2fg2r9TiO31x6DniaFAMgfvLDl4CPwdkdP5Kw90q1s6loDHbiVw1CHWDqAhrEuBZm-IzgeSOFCN4Wb5tX6AIt1Pdvqd9k4Qx1S_AbwDxb-086bUX_iWuqyM60mjwRYZtT3719kxnchEJs_cJp6hl4gUV0xe5AKKVuOTFlGtw4b1d313VZEBphp3F01NcHAAmIrEfgYTeKJhSH1wNXv61MZmcxiE26BlSct3qLZANniw3QSXyJqoR1hxxbG2jMlQUbHSdrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqcPJAxS7PDD5uyDN6FwekLVNXb08zWMWd9hOnWwdYUUy0Raj12I23uYmQ4rShzKTYhguRtbg3U9iH5XeQCV5l3t7ulFLyWJfL8SVbXCRJ99yu77136TnQQRDp22MyCBZ5eml8SK7FBViMNBZhHZWFDJ6OeyVekNQaHOtyz4Z3VvAZuf8FbphsNgVt2zDB3JnaKXCj_INQM4XZn-8agsIub4hMCkTRzfaYZIv7-H0jOPNRop5-Y54kur70uIifS8jT14wRg1WGVFIbO8aSk_yl8BMrlFYAmOA10x8IjiacyKnagQJWnIQWimfCJ59chTrfXDovBaou4-tGm6EPvHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVTZ6IBCsUwxBtkULUqmzS1hn074XJUmX1VQcLX0P6xR2Gan1MPjbHDj-w8JY0tv9q7zuv9O-KXz_HxXoqo8tb39zUI36329dDCnuDX9xAFHE6gB5-NqKz7iY3xN7wRlBfHQBiffFk7aq3RfMZ2CNrWwu_74ef-CbPrX9Q2u6LshiuukeWv0GVf6LQRB78eXph5XIBsac0RyTAgbzwLobVhkmFPW9SXJoQZ-JHPnipcgdCVL2ElI2rgeE9ftH57v0F9RJSdgWqJxjfUoqZYP-nHNwBrHwZAPr08pMk6lmkuNAIkUWMb3jKfCkiOKGaNYIBBUSRIYwkgS45C9tqeW6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyMI3KhYU7Bq7Mn7D6MIy8LuVrW6CUDSkUY921IpGzs1i5M1IbrhmR_JvOGI6oEwrdzfHoZTK5ol7ml1r5rwfEwxUeMFrAh4bAW8P9vST93i5kzdrcW9-kHcn2hRTI5UZOXkilyB6plgRbhHVvRR2KQq1loJ-u2ocXK36cDuxoYvwPR0p5GjK5sWDFqyB06x7UPvqQD3jvjBYwWr66a5TxpFN7jBeRyg99pm16P9wqYvybNfB7SC70YSlJf_SGtQ5S9VWQOVyzJ_FtqI7yqtuXAE1bvWS-AnfmlXiXOyzm2Ir-uxCdJkGLEDNQyIPZzwm7OpoCPX64TRQfOdeXhgXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfU7-ad1quMhexzcbHhGzIdaIjZv8htJOtb_EZWi462Odh3THsEhEotFw2VheNfbplR6PsjiQj4IyoxL2uu8Gqwkj0jOzdVfNVvz79PJa2wuFCyjT6g3y1hYJL2-UKrWyzaqWjMOp6HaUwotpcbtJhobA2X1k79r5HKi9MMRnD3-YtZASnqnVmCoT0u83bxDLpd_0bRbOHIGiFCd1-6eN_aVzWi1ZSR-RdW-YG5tb8CK7dc4UU6WDpne3o8wT7q97Kt5BQHKekVR4AxOVCb1Cqo23W4HPnniM1Rk7X3Z4aHWq8tTdDkJsEnFb4guLGj7n1vbOtKsWKyhwAO1uJNR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=FSluRxMFc9a4Dti2kHfe1gScS2OebDYZ2tukQwKfNCgVN7ndJj7caSKXatUBclWRCTSTpo0h5bodiT7VDQAcTsNel9WsEzrg1oOv_yJJqOCP-23baG_-qVzIbVhLaFGDoV3jyp3wGkq8TsWQhIEoh8YaQ17iCId6yvHvo7hlCPUK-nAdUB00XBjgpuZAMECuLuLrJElZ9n4KSFor1bUa7pDrIDdVDfRxeYC9flbubVP6ZeWx-GlQCqsjP-HddG2W522QrYVk7GYjkl4eCJxBnxuXTCKwDNiuMtnI7rbOX5D62qi7fpQwfAS0CyWtypBo5nGRIjT_6JiCOJTln7ccnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=FSluRxMFc9a4Dti2kHfe1gScS2OebDYZ2tukQwKfNCgVN7ndJj7caSKXatUBclWRCTSTpo0h5bodiT7VDQAcTsNel9WsEzrg1oOv_yJJqOCP-23baG_-qVzIbVhLaFGDoV3jyp3wGkq8TsWQhIEoh8YaQ17iCId6yvHvo7hlCPUK-nAdUB00XBjgpuZAMECuLuLrJElZ9n4KSFor1bUa7pDrIDdVDfRxeYC9flbubVP6ZeWx-GlQCqsjP-HddG2W522QrYVk7GYjkl4eCJxBnxuXTCKwDNiuMtnI7rbOX5D62qi7fpQwfAS0CyWtypBo5nGRIjT_6JiCOJTln7ccnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhPXx6w-ekmqJBgfawVbPklfOgAu4ylHVOLAnAbR93luz6c-a_zinawH8OOpLUtMp4W_iOJDGn1Y73WB8MfPbIHjtq1ch7_fD5aj3UtkAJEo_KgEgcifWj6XI0zC3eAk3TgPMD1OgDXNhlm-pak8df7olZLrxHKEgrjjr9yUR-0cGxeW4osFvbVK5RcaZaEI65484QNNBUGPjbIE2iVrBGllKFv94YYgTVhTlbVgZM3Z86wxaaRjuPpD_c0dPnKggHHylYjLxgrdoXy99PneT2R_SJVpmxcoCNlaHhx9akPvrL9j66te4Jh9DiXOJLhL_hI0YdT0k7-2b6EAYFdQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=jiSyeqXUUnMf6myUWLBryWv2ymvR7BKaYFfhPx6MOrlofrDduG0Yd210b0glH_967TmmiXqC8GPM68yZjQ_Lvv97GOgXwDpyXnpTgnlcXqQ85cKRPlv2Now6cwE8Pax9nC7JYHE0k-GLHpovD9_olqNpaI7R8Nm2GeFAaSCxTMgK8HVEQniFLtMmK6cat_0ckMwRAY97rPKecwIjprywQ-Hhd9iqKRSoIB3G8mn5ZQb6xH0LaEeFIPf62iEfNRwiSXum9vL8gAbGLTi0HbjOeETK8i2pgqwV-fD0TJPUpJs8hPMg51x2GfQUpcPxK4FBlPQGN0BvFno_Cop2M-crZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=jiSyeqXUUnMf6myUWLBryWv2ymvR7BKaYFfhPx6MOrlofrDduG0Yd210b0glH_967TmmiXqC8GPM68yZjQ_Lvv97GOgXwDpyXnpTgnlcXqQ85cKRPlv2Now6cwE8Pax9nC7JYHE0k-GLHpovD9_olqNpaI7R8Nm2GeFAaSCxTMgK8HVEQniFLtMmK6cat_0ckMwRAY97rPKecwIjprywQ-Hhd9iqKRSoIB3G8mn5ZQb6xH0LaEeFIPf62iEfNRwiSXum9vL8gAbGLTi0HbjOeETK8i2pgqwV-fD0TJPUpJs8hPMg51x2GfQUpcPxK4FBlPQGN0BvFno_Cop2M-crZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=U7BiqIYtDxzDwiR0IxKozZPg2O81LB0g0NVqNAVHeBopIpdVGO5qLvwSf5rYg19RxR4eo2_S7mq4PZWvKHqlr5wwA8DD5SADtykLl7txtGOn1RbjwF3AAYdNnMIlNj_-qa24noR1Av_I4CoW2ZkOKsKm7MMxmu8H7R1rkSW4Ebv4Xi7w-7QMnepAsf1nsDb75xSu0Dt_A1c-2ATXCHdB7CTH6xtYb6GVxTfyCoCqFQiBQCbPCOe5toxvKIjBJSM3Yko0MgQlzR-D9tK2Om-gGiIrxMdB2xm5ZSS1qMQrnXcWIa3fYu3stoV-eEhcb7AmkeWTfDd5xRNSMezYmXoXVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=U7BiqIYtDxzDwiR0IxKozZPg2O81LB0g0NVqNAVHeBopIpdVGO5qLvwSf5rYg19RxR4eo2_S7mq4PZWvKHqlr5wwA8DD5SADtykLl7txtGOn1RbjwF3AAYdNnMIlNj_-qa24noR1Av_I4CoW2ZkOKsKm7MMxmu8H7R1rkSW4Ebv4Xi7w-7QMnepAsf1nsDb75xSu0Dt_A1c-2ATXCHdB7CTH6xtYb6GVxTfyCoCqFQiBQCbPCOe5toxvKIjBJSM3Yko0MgQlzR-D9tK2Om-gGiIrxMdB2xm5ZSS1qMQrnXcWIa3fYu3stoV-eEhcb7AmkeWTfDd5xRNSMezYmXoXVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9Fgo-_wasQQ4gbpq-OzUizP2cCbqvpJY3MCLsjCsBWF2DcBxdwXvXUeHOEhkiPPUIiN6VXIdS3DFvlqWZGk11KQ4QvvQHAfF4HkDpOtywcbuAIc5kTWC1wF4-6K1_zjwFFvGY-i459YhC79MsK6SVlJH_4VrM5YajtpTFQHJPVtygySOPUUPW0lRY7BYVePb2dA8d9mvJD6syTJw-6Z5UzM2678nn1_Zfmr5Nhis9JtNgLxPRr8E-9tKEyzwAr9qHemD0uNxL08kwAyHB9Mx42LnVgD2SJeRKNrsaWr9t_GUDQ0MXt-DAmlTv3Q3-SQ27KZuDA4j1VTxAjYjOv7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=BAesmR2Fz_aHFCO0khA85MeCpx5StPxKSmSuJ_EapBmXTw3_XgLN9vLYzbOMu-Fz6Ci_gCm6QL9usc73qZJt0InTN40_si18cGOCdFOjiXehIrwOLA6QSZAghqRfLhCgWcnc2prJYPkgzv1VHIz7B2WrMNKprQzeb-9pmcoXv69TMnN9VjJQqCS9TeC1TKkVOFIB8riSV7XAU4S5u4nW1cCIOQP4e0VSEj4gi0lQo1subygEa74fOHuuN9HwNYeje6Fs7VfB4VSNtnIrZHP6vASGYZHnVUgMYWAv45w9FsPDP-UMttzPltsn6OzNZTo2pT18F3Yu9hs4m1BECz0IGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=BAesmR2Fz_aHFCO0khA85MeCpx5StPxKSmSuJ_EapBmXTw3_XgLN9vLYzbOMu-Fz6Ci_gCm6QL9usc73qZJt0InTN40_si18cGOCdFOjiXehIrwOLA6QSZAghqRfLhCgWcnc2prJYPkgzv1VHIz7B2WrMNKprQzeb-9pmcoXv69TMnN9VjJQqCS9TeC1TKkVOFIB8riSV7XAU4S5u4nW1cCIOQP4e0VSEj4gi0lQo1subygEa74fOHuuN9HwNYeje6Fs7VfB4VSNtnIrZHP6vASGYZHnVUgMYWAv45w9FsPDP-UMttzPltsn6OzNZTo2pT18F3Yu9hs4m1BECz0IGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dx8aJYfypIaE9XAXkVXwbwfnRcG4cbX4nEkPe00FLGcsAhLxLpKqAlIRiKHgU5w2Uo6K8Zrz3bfjzfItGaAVWhZ0_1Zvw6iN8CpJZasjfwlI1S3tcU5NH_PS1pm3Gc0Ml5I1sw_pUC1FtsLBwG01pKrcMc5DnY534lVMuTuD8cVYgWiKbJCSkivfKVLqru24Qs8SEP_cf1Z-RgkOcLUKNr9Omg2T0_TGCA1WVO9-me4Fdov_tPq6GNhrV-2AaCiOctQ5oX2DS1plHgvJnicplClmYt08iEsNtrsHVuTWo3DoNRJyg6k-9_keNi0cK36iOFCs9MslP0NGw6pDgFn1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5n3PMYSejc5en4UoAY9RKvhlJHri3RP2ETO8nI4edWmVfUtKkgBuRo2rT8Oob9F3YDL8FmqweR37fxXpS-MwKjTcWJAVvMkPliiYlES-mXkQ0T5DiIclTinJofqBH2m6eIgQCbCTtxfJHSLFrCMktwYBEIyWYjYZ1OOSrcX-V5qvCPmqEihZa1FMNzhSxHot7W1L5O6KrnThNCVzdHo-la6eMGP0bCsLJXGR9kV6IP_cx8NWKl1Miil6q765ydnriUPEwB6Dlqv5xsH68hhlHy4YvyOzr0YjQMVyvAKJHodgAkjMVzi_5J_9hpTkDULbNLvNpS91WNc8k_FyNyULQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfkSPsDexloJ6XtpHcgHboxK1tZVaihA8wJp9T6ksepcmrNexvRYMESmRSYohP5Q_fMFbUdpLkMqkIqmqulTrJ7qzL5CYMFWPud_fcvtBRKlj3U5Plcm4YBqOS03VW4dOouin0sBIKycWKZg5xE61JI9LOZKfKtdLh88HJu0j0_bmuyY512jqFeIw3v_M5bOYUUZvUUsUX9vvdXeVlIdcTax72QjtINnAJ1GsfrfaL8LYhKrWePp6Of736MDi1xWkGUUrYotU8enyQES7u5StCCsDAuTz9_dUzTiwFuL52i_UuSal-8QZgMG-ALFyFsXt_j--2SMjfsjT_Bss_ORWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKBiAcUsKnrJz-D7yaFXM_F0EHFSzODoL_8eBZX0acoujYe-_Ezs8SGa_N9haxtPFYo0XJ4cbUNm8s5FTeQvMxokpa78XWzFcHyfYcp8jnddWfAJ6_M1q8xwtEL9JXyvymoviq7M3oYIS8N9_LaXFICaT3FkR52o-tOv4H9UoPch3WH3oonekmRpbAJiN86iNjBxc_DBXtP2AeJdWOiLJbNM6UmKQMjCrH6UnQNIo5455E-aF3QuknxGT-f2E3RGvW6lnZ1NT3dFJZWuaYC_UD3jzAo14wiufdReR-5LvIVG8pPVjTIrfDivZ8pTGjn2A6EV0DqHBLRdpZsHVnAx_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=oWfZ9-oqExc9SVaFgQeQtBNbvPyDXIUwgEFI0EW5r8hqSxLLV84Zk2VG6pfS3ktadAaL9zaWedXS8g_6Ix4AgEqA6Nv--_uT0Z5iCQ27HvNXGmNfVbJ1N3MkBRCk1YFB2uK-qOCWgomwvaWL2S-JFLl1r8g69fcra0qo_4XCCzb-9LuyL5ON8q2B99Nkf7QMJV2DgOU_eVatPVbeNm0joF81WhsXfYkaJtyPW3ZOct6c9eFp30cqPd2YZz1nUQmPqBiFqgpm-Yn9__5WhiHd7FgNm1uWTuMrbPVaCzDP2V3h_MqQ2OpFB_i6PzuuJqrUoa7uFV9EWFJq8TX7r-Dzrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=oWfZ9-oqExc9SVaFgQeQtBNbvPyDXIUwgEFI0EW5r8hqSxLLV84Zk2VG6pfS3ktadAaL9zaWedXS8g_6Ix4AgEqA6Nv--_uT0Z5iCQ27HvNXGmNfVbJ1N3MkBRCk1YFB2uK-qOCWgomwvaWL2S-JFLl1r8g69fcra0qo_4XCCzb-9LuyL5ON8q2B99Nkf7QMJV2DgOU_eVatPVbeNm0joF81WhsXfYkaJtyPW3ZOct6c9eFp30cqPd2YZz1nUQmPqBiFqgpm-Yn9__5WhiHd7FgNm1uWTuMrbPVaCzDP2V3h_MqQ2OpFB_i6PzuuJqrUoa7uFV9EWFJq8TX7r-Dzrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=BPhtDArTD3jnBZqYA7-LSwxNLVzY7xCFRgN0B7TtaUvBMfAPaotHRhjWZor_Qqk1DzZ3kHrulIHyFiWtZh4CxDZzp7g0nux2spnwBc815OQRGRQLhMNDU1TC9ZpXBXSTnGlvNTtPhtD5PWIKLTIykdOgAjc6XZ3GY__q_fuFqBav_QXBvdx472WGo4rR0eTDWTirdT0UyRM_T1RGzm3_KPwBbf5xHoBUsQSR7SYyL4Ko4U7NDpMNTU6aHnmmwQxSPa7oAE4Of8zm8gAvDXL-IE9ACB3Xoxa1Ok4R0WtKX--lO8Zgbt8z_ehMhcvfVHc33dahFjjQZ6cN6Co2R92GhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=BPhtDArTD3jnBZqYA7-LSwxNLVzY7xCFRgN0B7TtaUvBMfAPaotHRhjWZor_Qqk1DzZ3kHrulIHyFiWtZh4CxDZzp7g0nux2spnwBc815OQRGRQLhMNDU1TC9ZpXBXSTnGlvNTtPhtD5PWIKLTIykdOgAjc6XZ3GY__q_fuFqBav_QXBvdx472WGo4rR0eTDWTirdT0UyRM_T1RGzm3_KPwBbf5xHoBUsQSR7SYyL4Ko4U7NDpMNTU6aHnmmwQxSPa7oAE4Of8zm8gAvDXL-IE9ACB3Xoxa1Ok4R0WtKX--lO8Zgbt8z_ehMhcvfVHc33dahFjjQZ6cN6Co2R92GhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=Rq7ck37-mCneUq40dzy1dD3GC4n--Moy71C6OVXUpnmwxWzUE9oYgtXU6U3C_Diq_vCTRnTX2ltZ6TTh-HWbi4OEC6kLecD6sPKN4utJs25mvkIPztHaS4aQWuiejOafVy0kDQSTXeS1jH-b5Twje8dytEkkDTmrNsijRfouC5_n7Jmsqjhc8rLSCA1O0SYitfdHI58dHoC6PP7flSp7cFGhnYLGeVC-0S6J96av-6_u6_Db5I5ljgOFsOo7oQR_w5g5awtbGlj6BTVv58zmCG3b1_xzkYg7g2tgA9pY6cfuIKnj50OcGDJnSXePpf48OjyFaD8HKcK1lcySsJdFDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=Rq7ck37-mCneUq40dzy1dD3GC4n--Moy71C6OVXUpnmwxWzUE9oYgtXU6U3C_Diq_vCTRnTX2ltZ6TTh-HWbi4OEC6kLecD6sPKN4utJs25mvkIPztHaS4aQWuiejOafVy0kDQSTXeS1jH-b5Twje8dytEkkDTmrNsijRfouC5_n7Jmsqjhc8rLSCA1O0SYitfdHI58dHoC6PP7flSp7cFGhnYLGeVC-0S6J96av-6_u6_Db5I5ljgOFsOo7oQR_w5g5awtbGlj6BTVv58zmCG3b1_xzkYg7g2tgA9pY6cfuIKnj50OcGDJnSXePpf48OjyFaD8HKcK1lcySsJdFDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=FzXIRTsTA1ZpGzknJgcUIHgwUqVmSJrPfbaWjaCQRb1KxGW7ZaU5liF4K5zd0n6KN0vI4HVEDIyX0HJ17rKhzBljJUeaq792gFhA972hxgcKSEbHFYhaIkPRLY4gSowZaerIBWXQq20EXofb9mfmo20x6iCfxwNqp-ysQgc9UE1P-J0GEUH66atsvzdc7xa40m0N-5d11ayHciBgLgPsJhFqI70YtJVz4sygjRpooiGbxu5f6YHdS2qWU56dqAEPSk_4INkpQYyeuLtACtU9oTd7p1kwOo9ogmxtxgDzAeuAdybKa_05edqE97MBjss41l0UNRjHZpeoEDbHy_FuFl3kTYjc1z5RNJ4A88cg0TDjPuLSKNeaJMsPlahI2wxXpyl8tTZX7jNt6oOFeF4nb8ZcYsD92mbY9Sy62xkUz15H7eTNtX-i5AiSPZQesqyTb72dPlhUwi2mzCpK-oeRUz9kdgxj9F-sAkMrUXfZVfPswyw2fPSor6zWol64jWbahZS-dKitcaDxJ6DSEWcSqfjH-mIoj9ZaSBuGoPZrEJm8KXrxAzWvWuKiGbSmyC7AeE-o3ZSERPRoPILu9pcKcu8mKvRLOIiYcPtCRnOtSJKLqAajzRxEcF2Zn3rPstutiUNq-FG4W4MQ-UAWSneMzs_GfBZtdtQ4Oma7vQUe3z4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=FzXIRTsTA1ZpGzknJgcUIHgwUqVmSJrPfbaWjaCQRb1KxGW7ZaU5liF4K5zd0n6KN0vI4HVEDIyX0HJ17rKhzBljJUeaq792gFhA972hxgcKSEbHFYhaIkPRLY4gSowZaerIBWXQq20EXofb9mfmo20x6iCfxwNqp-ysQgc9UE1P-J0GEUH66atsvzdc7xa40m0N-5d11ayHciBgLgPsJhFqI70YtJVz4sygjRpooiGbxu5f6YHdS2qWU56dqAEPSk_4INkpQYyeuLtACtU9oTd7p1kwOo9ogmxtxgDzAeuAdybKa_05edqE97MBjss41l0UNRjHZpeoEDbHy_FuFl3kTYjc1z5RNJ4A88cg0TDjPuLSKNeaJMsPlahI2wxXpyl8tTZX7jNt6oOFeF4nb8ZcYsD92mbY9Sy62xkUz15H7eTNtX-i5AiSPZQesqyTb72dPlhUwi2mzCpK-oeRUz9kdgxj9F-sAkMrUXfZVfPswyw2fPSor6zWol64jWbahZS-dKitcaDxJ6DSEWcSqfjH-mIoj9ZaSBuGoPZrEJm8KXrxAzWvWuKiGbSmyC7AeE-o3ZSERPRoPILu9pcKcu8mKvRLOIiYcPtCRnOtSJKLqAajzRxEcF2Zn3rPstutiUNq-FG4W4MQ-UAWSneMzs_GfBZtdtQ4Oma7vQUe3z4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=Te02vGyibdk-tPP8W7O7X-n_wyympYp1HMgxy2aj7Pr9eDNFXh1jv-t3fyLtLthHOtP6NuW8_Xvqcc1-Q8FljTsIOCPk3flQuGw0oMz2bT4TwyoyPoNJEG1dd6qjkR9rg2QiYKVHLJ6SdLtkg6RYhHijmOtJA-RIy_BFXTiWG2ApvsXDgk5-MYI1jvSlKy5cgKClEKnKcj76TCKl-h66lCfsNV-BiU7kgzT2FG_fllXwDXT2jCdFVN-NgzAgo1A5z96Oay6FTw3s6oZQRUuwQ6Ho5xn6xj-Ce0kiRUUVQGUhi_3bUpM0jDk_9IRB-zbtehFKWK0g58wqy-rF4tDCXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=Te02vGyibdk-tPP8W7O7X-n_wyympYp1HMgxy2aj7Pr9eDNFXh1jv-t3fyLtLthHOtP6NuW8_Xvqcc1-Q8FljTsIOCPk3flQuGw0oMz2bT4TwyoyPoNJEG1dd6qjkR9rg2QiYKVHLJ6SdLtkg6RYhHijmOtJA-RIy_BFXTiWG2ApvsXDgk5-MYI1jvSlKy5cgKClEKnKcj76TCKl-h66lCfsNV-BiU7kgzT2FG_fllXwDXT2jCdFVN-NgzAgo1A5z96Oay6FTw3s6oZQRUuwQ6Ho5xn6xj-Ce0kiRUUVQGUhi_3bUpM0jDk_9IRB-zbtehFKWK0g58wqy-rF4tDCXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=J0I5gZ8w-qNeYKH0HpdH-hfu-F12F-QRU7XkoZQrjuiDkpu-8EwGd9DlvVJOnmgTfCd-mAaB7rvWyss4hX7tFBKaqtTGRmN5eewjE2iX1TDefR6Otc0_wiTsqogjwqAFvLJKs1iZnzDNZ77LbXfxXMmoCYpjdQwRVWYCxNyw0crNwH4JoErdozLgnihQ7Q9Jhw2VKHTEuiI8RYD2p3a4VS-hZfSEEwAjMI8-D7Px7Cm60_yGxt6bpBz0RJOBZUY1-jF23gyPIsYQsAUtrGMh3Ncm2MXjcTbgdcLWZZDrmCL998iBaU4ptPWLNH3MV6ev6SyEXQjoyHpxJAVNwWSzHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=J0I5gZ8w-qNeYKH0HpdH-hfu-F12F-QRU7XkoZQrjuiDkpu-8EwGd9DlvVJOnmgTfCd-mAaB7rvWyss4hX7tFBKaqtTGRmN5eewjE2iX1TDefR6Otc0_wiTsqogjwqAFvLJKs1iZnzDNZ77LbXfxXMmoCYpjdQwRVWYCxNyw0crNwH4JoErdozLgnihQ7Q9Jhw2VKHTEuiI8RYD2p3a4VS-hZfSEEwAjMI8-D7Px7Cm60_yGxt6bpBz0RJOBZUY1-jF23gyPIsYQsAUtrGMh3Ncm2MXjcTbgdcLWZZDrmCL998iBaU4ptPWLNH3MV6ev6SyEXQjoyHpxJAVNwWSzHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptj5zpAY3w-sjjvVH3P4ag7VhFxxc-Qm67Xwn89sgepHyOHizfrScIWnd7n8z8g-Eji38viIlARorlZq0sEBKb0T_Q9GDmPOkjlxssuNFgR9xSiBswOZd6DVbAp178XNC4NGSCbpUmb2RRpYjtJEaSjqdkd5zE3f2u6-CJO4BMOArN3LQc2apGIjwCaQxuYBfo8a6jCRZJdGp72gRLNC-SLUAKPhkIQHOo6EmsaPiYDor0DZf4gJCU0WCM1LBJcblID9msTktbWeqnDYcKJiM1TkMARFkQmpKm93nEWRxN2nVGTOJk57x8_pg1XODI3wt7jQE0_JYlLl3kL9fN6KEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Ihd1eMYaW84a7lQlP6YSWzhivbCW0SzTdhqwYltXBu9SfeHhY4cq1dEtbXZ_9QTu0CUnzBUHRkc_QDRi6a4sXQYf9UjZ8l-ZjXPw540pYlgTQEtcB4UdotJ8PR3NMk3xwupp2yjlZ6xE4vFPu7fvMu-UBRh68efNtfqFnKcXLYHlhMaGtA37Kenhz8xojLwmzlMxe2bL2TtU6lHqm1vl-QTx6-7Fm5djvKiW2l_c1D-TV2OtpjOBa0UVTxQ-xHdkwW8YgzNAhVVAtbDd4t7w5CXRONcgqBWT4N6LaXhzPvW1xEVrPHc9RIEya9LBxt2MDcMPtYXn_NrSMLvDdvuOog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Ihd1eMYaW84a7lQlP6YSWzhivbCW0SzTdhqwYltXBu9SfeHhY4cq1dEtbXZ_9QTu0CUnzBUHRkc_QDRi6a4sXQYf9UjZ8l-ZjXPw540pYlgTQEtcB4UdotJ8PR3NMk3xwupp2yjlZ6xE4vFPu7fvMu-UBRh68efNtfqFnKcXLYHlhMaGtA37Kenhz8xojLwmzlMxe2bL2TtU6lHqm1vl-QTx6-7Fm5djvKiW2l_c1D-TV2OtpjOBa0UVTxQ-xHdkwW8YgzNAhVVAtbDd4t7w5CXRONcgqBWT4N6LaXhzPvW1xEVrPHc9RIEya9LBxt2MDcMPtYXn_NrSMLvDdvuOog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1vIDqg-kosD_1-a7MUjJsV7_MLAkEyNKwpSeZVtMP2qJo3kd4lD8_wUf98sxWIHXQDZBtHVCDqq1SraeUdZJCFoZQv6EYUAt5_g_2IeoGh1TfJn4JD4e9TGhXh9vQpD7oRkjCLmBft2h4vKlW9x_XipS6n7w-1MRew5-ANzji9HOk5qnjBhPsFWXrmvae7kyb5KRyw5-WovP4WJTvRuQY1yUG9huqU-0peSHNeZtmPUAImqyzr89J5ntbXfpgiO5XyD7axxJ83xjY_y8bEM-ih01aRDIFSPmYBtqeTV0qPZretfLGwZjmfz8KwHKpUQpb9LySTy8-O7sUMAsAKwHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iqq_hedecB0N8tRACCkQ1_gzcGO73MjZW010DrafbBtrFfEUcFFXSnn4XmxLGmzJkOeHfyway6-K4xOmrFsMqmH_7ajJ4Tw-owSkO9DVS973Okkcd265BmAbIup43ZiPhYcVZp-wAnuZ1TvrtRSLXnsCiKXBDtmsTdFkAbio3ghBbz71cZP492iiJ-oLgzYQczpZpDLgkLfUGlfOqkDrE2YR2Pcguo-c1-g0EPzuw09JxQJq-KO61UjhBRhQaDPdWcf-1n_MD9vo2JD800sfeuMWWFTTFxq6a_gwtA1cvnuzzzpiPoU8hkXA8vE8rF78k4PjYHseFjMSwNeYDfO9Tg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=qLtwMixfvCZMpQPVUVdowFllLg6PBbGdTTd3JMY3apZPlsO8ZVemNPBomLDcOTesDTtY9ySrnfJE7m8gBZXkP39kW1waGXnbpQvBxDvrKeYkM0DsyqVkzEBgG5MlByrc3pmRPfSPWvD0tP9HzwRYI_4bhU8g0s-xGuBNF0ZRnCIk-CyNoiYR78No6NPGC4hTbsLNltjWdh3NSlcJMXuWjQHmA8vCVatsMvRj1ezZ5MJi6W2W-esqExT8J0ZEv9GfBUo_an7jF3EnGGoCeynW2Cg9lqIS_hgCjkzvYoWSfyU7YtsDx4CAdIEtwLGza4azSoYzRADECkjUgwYTutDVbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=qLtwMixfvCZMpQPVUVdowFllLg6PBbGdTTd3JMY3apZPlsO8ZVemNPBomLDcOTesDTtY9ySrnfJE7m8gBZXkP39kW1waGXnbpQvBxDvrKeYkM0DsyqVkzEBgG5MlByrc3pmRPfSPWvD0tP9HzwRYI_4bhU8g0s-xGuBNF0ZRnCIk-CyNoiYR78No6NPGC4hTbsLNltjWdh3NSlcJMXuWjQHmA8vCVatsMvRj1ezZ5MJi6W2W-esqExT8J0ZEv9GfBUo_an7jF3EnGGoCeynW2Cg9lqIS_hgCjkzvYoWSfyU7YtsDx4CAdIEtwLGza4azSoYzRADECkjUgwYTutDVbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=TPQFSDDh6p1CUEUzz8AOOhk4DLNU5J0mGNZt4YRX3WvSeQLpOF8RgsSFhlFzb7xOhVOc9I7dcqUl1TktcYotU1By8JBEOgqK8uLdvg4Utn1LgtVYOA09l2mJd27zEjs_k4A3OQOZ1P7s8EEEAQP6U3Dj7To8beiHk2uum-fwQnM-v2TO8G3NjiTXMiJwuFU2PnkDqDhR-bynNmFoj3PIF10dSnh6K_SsevXVZV5jtm3hNHPNMjDj_AEAK56vN8KTOKzntOzPpwYVR3ZGQtOzD1oHLZylFpWuzbYnsNANGh6eE3ieJ6TqGLCYCwTjunhM46UWhovCB4SNSQe5DJ7pGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=TPQFSDDh6p1CUEUzz8AOOhk4DLNU5J0mGNZt4YRX3WvSeQLpOF8RgsSFhlFzb7xOhVOc9I7dcqUl1TktcYotU1By8JBEOgqK8uLdvg4Utn1LgtVYOA09l2mJd27zEjs_k4A3OQOZ1P7s8EEEAQP6U3Dj7To8beiHk2uum-fwQnM-v2TO8G3NjiTXMiJwuFU2PnkDqDhR-bynNmFoj3PIF10dSnh6K_SsevXVZV5jtm3hNHPNMjDj_AEAK56vN8KTOKzntOzPpwYVR3ZGQtOzD1oHLZylFpWuzbYnsNANGh6eE3ieJ6TqGLCYCwTjunhM46UWhovCB4SNSQe5DJ7pGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=Z_kainxN_mAkWj_QV213ms2d4ktOLEk5dzJz7S9MTNqc3VpMn6VFp5GNEvTxecnuVmyrcmKC_VjkqCzmOg4sstKJe_AmEg6j8XQyDsdNWmha2WY-NGLmuBXLg1he-oPg4pVZluQ7eI3Xrd3QwGcJFTQGCG8oc4Vvf0hRMaUVQEEaKSMRmA9bw088883_vz4CPiiHAmptAiR45VIYLt9LKQu4gzkVQHYeZsQJLDt9em7Mjx-Cnfbwnsm2CE8XfsIdoJuu-whqL2yzELdpzNcb3QwJZBKQe5qVr5iHqXOZmdC1KhxfuGHYctqJmhtSsKHNJSqsMjwt3J0gJvHPKz7Ikw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=Z_kainxN_mAkWj_QV213ms2d4ktOLEk5dzJz7S9MTNqc3VpMn6VFp5GNEvTxecnuVmyrcmKC_VjkqCzmOg4sstKJe_AmEg6j8XQyDsdNWmha2WY-NGLmuBXLg1he-oPg4pVZluQ7eI3Xrd3QwGcJFTQGCG8oc4Vvf0hRMaUVQEEaKSMRmA9bw088883_vz4CPiiHAmptAiR45VIYLt9LKQu4gzkVQHYeZsQJLDt9em7Mjx-Cnfbwnsm2CE8XfsIdoJuu-whqL2yzELdpzNcb3QwJZBKQe5qVr5iHqXOZmdC1KhxfuGHYctqJmhtSsKHNJSqsMjwt3J0gJvHPKz7Ikw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoKYZ_rqiZMaAFnVqbBP7uqtyLa8KUFfesYqVHQ9SvGw46lN6P8VgnqAwY6Y0bU_2ac20HWxCpEK7T0rPx2eTZsFWFnq7Q3qMEBRPJ8srbjGeh6x-UOYV-HJiHvi7GJRr4I35wDtlqvcoKihWTN2xyis_HOZZInyIWvRKyuwNKYlQbdBqTq6PrhuLMr6EBwNDkwGbkCaGr6dFhFQQQIcdW4L82Md8N3uJHoDoMeJq_MOaoAvFyxKiv1Kzh6SLp8qmemVMvsV_Cnfgk4PQ4BMRj7iFMoFJpf6_nCehS49PSPGUj1exnNdCxWkg0ouUy0LSeEjPDG0Pb_10_eHbHaShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=ekle2LD73BOzUXlobDVQMMa_sTbKMI5LwpHjrS1GXUzPumlW3-0wvqSTDXtzYQleghNL-7Vr1tCOp7Ax_AwbiSejFJT_FwykSYlMC-tQB5sidKQdQhWsKxlGXQZEKlZPfEQEl8svWdgZml0QAOT5rMDAqFaEK88CGtlN1rDpualb_rdrBnttO5qNPbVkp36wgXU6NV4sGH9x2gEQFhFMjhtIpUBiGH_rx-xHJKPe5JuY7Qgy8AP-fP3NFHLQKAoIu9YnCk2w5Wz_JDzmSzwDy3idQekdlO1vYnDF-s6XpDRatq6lUEneUrDk74jHVf-VO9AsoRjDScsANbB-bTMGNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=ekle2LD73BOzUXlobDVQMMa_sTbKMI5LwpHjrS1GXUzPumlW3-0wvqSTDXtzYQleghNL-7Vr1tCOp7Ax_AwbiSejFJT_FwykSYlMC-tQB5sidKQdQhWsKxlGXQZEKlZPfEQEl8svWdgZml0QAOT5rMDAqFaEK88CGtlN1rDpualb_rdrBnttO5qNPbVkp36wgXU6NV4sGH9x2gEQFhFMjhtIpUBiGH_rx-xHJKPe5JuY7Qgy8AP-fP3NFHLQKAoIu9YnCk2w5Wz_JDzmSzwDy3idQekdlO1vYnDF-s6XpDRatq6lUEneUrDk74jHVf-VO9AsoRjDScsANbB-bTMGNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=eBDHnlopZkhgPfmuOhs7pUGvQlT5HPRotFPni8SseRs_SRPWY-wVhaOMTPct48kFaR_nEt4oa4ca57cmJ0_a7oPSBAMGxswFbqYaRmTBFKGz0eA8D7qgPVCY9AEZB99sEzIV7S0u9sYrOmrG82ajLEosRpycFTugTTNtnGxYqirKrd9WO1oJ-DWbhIgtkn7H51Xj0kWJLCx8HMPNrn8278OKdXIhzfsB9QCJuu2uWLlcCwonTV6Sw7QBxgiI4mBsFHWIiic09hWVfB-8jLBgDHfl-T1suQIhG9MZmSkoS7xzBS7SYRu_7btTr-y60M6z3DWClBbyQ8dz6uSKVGlrvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=eBDHnlopZkhgPfmuOhs7pUGvQlT5HPRotFPni8SseRs_SRPWY-wVhaOMTPct48kFaR_nEt4oa4ca57cmJ0_a7oPSBAMGxswFbqYaRmTBFKGz0eA8D7qgPVCY9AEZB99sEzIV7S0u9sYrOmrG82ajLEosRpycFTugTTNtnGxYqirKrd9WO1oJ-DWbhIgtkn7H51Xj0kWJLCx8HMPNrn8278OKdXIhzfsB9QCJuu2uWLlcCwonTV6Sw7QBxgiI4mBsFHWIiic09hWVfB-8jLBgDHfl-T1suQIhG9MZmSkoS7xzBS7SYRu_7btTr-y60M6z3DWClBbyQ8dz6uSKVGlrvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=uQHj4VvqHuefLNJCnv0nwhjkP7EP3_cBnf9lE-hx4xTyCAlmTGGe06u_ZflehPByQ7ZmZohCGcVYR8-cBxPhwQyJgCCSFV96Y_R1ZhejfJZkmhmvMRziwGRAX0PRLS-XJ0ulMwahoZ9Fm5bKXevWTrIEuP3T1IwGSdkpNeQGjPjVcHSx4tb8pFw-Fmqj0RxogaoPFae_S7oxqRc93Nk4kFiUusta1vaNXv6DFyhVOidayS6txcBAvZGehFIqaZzZH_y9_n07IEiL6X2PZy4xanZ-vp5oyXOaqAs_h5QSzEbhufP8cFh0QRPBeJpt_-iE34l3Ad7ZMvvLJJAXGfBmOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=uQHj4VvqHuefLNJCnv0nwhjkP7EP3_cBnf9lE-hx4xTyCAlmTGGe06u_ZflehPByQ7ZmZohCGcVYR8-cBxPhwQyJgCCSFV96Y_R1ZhejfJZkmhmvMRziwGRAX0PRLS-XJ0ulMwahoZ9Fm5bKXevWTrIEuP3T1IwGSdkpNeQGjPjVcHSx4tb8pFw-Fmqj0RxogaoPFae_S7oxqRc93Nk4kFiUusta1vaNXv6DFyhVOidayS6txcBAvZGehFIqaZzZH_y9_n07IEiL6X2PZy4xanZ-vp5oyXOaqAs_h5QSzEbhufP8cFh0QRPBeJpt_-iE34l3Ad7ZMvvLJJAXGfBmOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXs1KzsUvjNOyBZ89wKHJkCUwcas_hsYeB2D8bJf_iAVaQFU0eIl1nVM6dxH9hwiAl5lz6SrlVdOxV_pjkSTSTJAcLWfcWAKIVjioElrrCuB345cs-CHoKSYgEpFOa6JcffUTFcxp1mx7gwU1MjWdmsmysxB-sd93CBFXhY1iOHOytAD_XNQltz2Le2x4IKOARkKxTShY83YKeUpWl84i0PIWROuAkmHuG2L-YisGOMkJ8pPMdeSeZ5b12-pTR5z8huzy4Ex_oRNgglSuDMXwwPrEyNBWNxsNm1z2zidGYvYgx4An4bHlInYfAGZIeE-RCuK07aNvsDJFb0MwDhQjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=abLVaJaqXpVmvr8VayqshQFIA8JWCCe57A6ADrbRsmcSZ2ucRy_PZyX3X3QWrQh__Y3s_aKGXSylfG1eKNtJ5C0hbgUN-iGT1iDU0EdGhKpE9RFW8ohZVF86LctlomWtopDobUOwQXkvK3wHwL_gaid81P5MAl7B_T-HFsX88_Mfq8RxLJPrAVT8HwKmcWLre9lSOXmk97gaCIFxSg_7XtPhDOe6T_ZqNJHABXKQuo-yjWi-Na5kW3YqnpkJn8VtLyAy8m0_IVVoA4vRRqySpCH2Yn3SkOsOCcEep0FiPgxkUSwexUU2DwNsOUYAU6vjNtq51_A88KYVAQTRccTRCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=abLVaJaqXpVmvr8VayqshQFIA8JWCCe57A6ADrbRsmcSZ2ucRy_PZyX3X3QWrQh__Y3s_aKGXSylfG1eKNtJ5C0hbgUN-iGT1iDU0EdGhKpE9RFW8ohZVF86LctlomWtopDobUOwQXkvK3wHwL_gaid81P5MAl7B_T-HFsX88_Mfq8RxLJPrAVT8HwKmcWLre9lSOXmk97gaCIFxSg_7XtPhDOe6T_ZqNJHABXKQuo-yjWi-Na5kW3YqnpkJn8VtLyAy8m0_IVVoA4vRRqySpCH2Yn3SkOsOCcEep0FiPgxkUSwexUU2DwNsOUYAU6vjNtq51_A88KYVAQTRccTRCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH-qBdRhsc-L7ljLe_40x19t3KfGhqnTUcZeA5yL4cVr1v8mruUuF4h0hwqNYedwO6dcdEdWzKKXly_26OpCIcufavfPe2YZNeSPUw1BzGy690GaYRr0TvihF_evFiq6OQCqOkGTiErFMcRfjipDDMu4hd97PTlEIKw5tOxeve_Oy7ANTcfNkddGSm1EgEi-BfVZZJQTKnTThFBygIC6bEmFeOSzTFX_0F0KnS1yzcrns5oKquOmk_vEwnyT_oDm2khp1WX2vRMgTeFZkSoGDCictCUSwfz_xLOexxYntErD7obG_Y2dld2qA_lEOqSxQpQnd9g1txMWuBrRoaTJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=eYLvxzn2pQRRRbu4qwnJHN6yNdjBazkibXKp6TSSLMmBEmDIZQh8DGPbXvT6sjuGw08lTyunwnaGTF3UB4WFZ_Yx7CGdQSPvYWzXHzIP9c9q-wTvSDgvgfBdJqDqOBye4LV3725naV953jr7Xn5ya9n9EhTwKtpp5NMGgjpUGI5o8O-1rNgCVv9JYtx_8oytJ1ex-rXvFoibquaNQcHldfgAGt8qvQqPWBRcHYENAVbi3LxjGaFgKn_QRWzvAApau3lKRgmV4wr0ud3Xm5P1_zeWiTqDytRtRF9bJutcQvzRIev9e_TXDxfzFnRjuILxwFER_xAb9M0Wv8lM-b7mEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=eYLvxzn2pQRRRbu4qwnJHN6yNdjBazkibXKp6TSSLMmBEmDIZQh8DGPbXvT6sjuGw08lTyunwnaGTF3UB4WFZ_Yx7CGdQSPvYWzXHzIP9c9q-wTvSDgvgfBdJqDqOBye4LV3725naV953jr7Xn5ya9n9EhTwKtpp5NMGgjpUGI5o8O-1rNgCVv9JYtx_8oytJ1ex-rXvFoibquaNQcHldfgAGt8qvQqPWBRcHYENAVbi3LxjGaFgKn_QRWzvAApau3lKRgmV4wr0ud3Xm5P1_zeWiTqDytRtRF9bJutcQvzRIev9e_TXDxfzFnRjuILxwFER_xAb9M0Wv8lM-b7mEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ip6Z7zlddhMknHIiQa05kVRJrhTzFZ1h72a5SwWUcAdPXb3B1TX6lLj5y-Lzm3Cal-GfB-O-7lKn63FJ7s1Dk5TSrbb-een9tuNhThxZoSzicwqFP9qiPfnfw1z7RdPIsXp2tcsik8UGQTkVty3944NKcXPn7PWFUtt2VT8vJF9SQdPT29n8RsXokLt77TV853QUTxaFgsOkhIB3VSjf1UO2ASEdK7wh05uVdz4ceNmUlJAcJ3imKN-SAmFC4wovpTVOwZ3E82RQMR0L1XWV5iWEZK198KB9KQWGmNABCms7qSIrW24tgCb2iLhsRUK6gMcFlIwntBUQNbz3XWu5zQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=LANIAi09rhO2vwrWOankKH_OL5OlWBGp5XbNXUplSonIXpOgaRQ8tjXnOes5yIZ5Y6iPOV8RihtR_E7nQw2u2iKrMACC8haIFzHeULB_e4F60i05t5xUw1W-WDyJsCVdIbj0rAn8LK0vsQFcbfO3R0_583qGdY0HIosGGBGrif1LmrjR7Dhnoni8df4WBOU2cDcuIrUMZOuHTSlQVe_zXFAKDZi5ruWi_eRJeUXvpBS32iod7IORUbIg3J92FhAeMMZFER51wFpVfi5OZjwYrBBQ-dcnsCYttQqB5cQsWwlmhcLC0JQveySAUTXqiMPZoXGIddyLZafMW4icxEsafg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=LANIAi09rhO2vwrWOankKH_OL5OlWBGp5XbNXUplSonIXpOgaRQ8tjXnOes5yIZ5Y6iPOV8RihtR_E7nQw2u2iKrMACC8haIFzHeULB_e4F60i05t5xUw1W-WDyJsCVdIbj0rAn8LK0vsQFcbfO3R0_583qGdY0HIosGGBGrif1LmrjR7Dhnoni8df4WBOU2cDcuIrUMZOuHTSlQVe_zXFAKDZi5ruWi_eRJeUXvpBS32iod7IORUbIg3J92FhAeMMZFER51wFpVfi5OZjwYrBBQ-dcnsCYttQqB5cQsWwlmhcLC0JQveySAUTXqiMPZoXGIddyLZafMW4icxEsafg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKNs0xNy1Nfhcc-ij_XhZsKHqXelZePa4EYkprxfILq1zMoySC31yJjlR1mRF7FpMc0HEhMa0vMG1UH9UfSmgDAu4clluPyc4p8CTWJLhv3S9-xOu3ZDOxEX7vk3OMTrT7LXjKevfHV4UTiImUjGQ6l26KyLTFp7fJgdBq6GOaUwCABNweatXIi6_zFnd75BRGewkasijhDPejFg27aL8Yh3BQVPwFxVKQvVq9X3Fyzwo2kaJkHNcgmm9OzawyOl9u3G4F8o3QpACCBHesYkgH1f9f8dR4DECyfyy0Ldu2hnc0ApAdIumRuOsAS43ACIHHkCF3lh9zGnkAFCH50rHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghmc3WO90pEAK_EjThH_AfJJG72kK4Lgiz53bN23Vi8qWZ6PgMvTGAYv5c3aK_pimm1ILljEDE-DDyWgHJ7NaSCDnCLX44EA_Olf3juxOrQO2Mfg8oKzZ7iwzv_8Ts_EvSwIhANLSG35bY5z4KBzsVX0_5BhtPDta9AbgaLlVgTNEwOVhByT-Ghtl_bM2jqq9Hs1C2TUYhggYtA5P57x-w46fhE9-Aix_Ng-1L2-g9blivx629IbW_zImih2UUBzs-v2YKCLUm4p2tPsXszD4WLYSIhDDsmqPqyKtxoxxISQIf5veV9noLVb9g-Guk4tq0dNrjF4Fim-41yLz_Qp2w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=BJRUnqGCEQxD_qtiGaqm67SitZBwOGYllZRWwafQ8XfJDRktUoTVM8-cy7MGxDUe3PchC2OKmcrCOyqDjdxbapgLiA46DQ5jqhGfcc0QlS2oklYc6IlJMExiwr-7EFlK8SjE2X-FY7rukr1bgA1PKqUxBp1I9NG6OXvZcOxQ6NGzBILAaJLjSTgSeIp05KnRYOK8iRIGIpMlcBRqluO3AWTQzuGxJSk0B_yufMP1d8mEK0IPB0mWYogMIw72WTajaQ_P3IdwFSB1VwSAlMIUzPo2pfoo6X5f4V4BCa2gzlHYrrn9toixgv51l7ppJFXTha4gyL7QzWoYKmo6K6UtFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=BJRUnqGCEQxD_qtiGaqm67SitZBwOGYllZRWwafQ8XfJDRktUoTVM8-cy7MGxDUe3PchC2OKmcrCOyqDjdxbapgLiA46DQ5jqhGfcc0QlS2oklYc6IlJMExiwr-7EFlK8SjE2X-FY7rukr1bgA1PKqUxBp1I9NG6OXvZcOxQ6NGzBILAaJLjSTgSeIp05KnRYOK8iRIGIpMlcBRqluO3AWTQzuGxJSk0B_yufMP1d8mEK0IPB0mWYogMIw72WTajaQ_P3IdwFSB1VwSAlMIUzPo2pfoo6X5f4V4BCa2gzlHYrrn9toixgv51l7ppJFXTha4gyL7QzWoYKmo6K6UtFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUQKHRZzU6hofXXuS8RIc5VolItNTSdFT_1q57zs0US4wH_Mw4mQz0cPhYbN_IU9VNKiSMAJ-LhI_ZgolL62Fj6RRn_NHeTIB-8QDsXwpFZvCOaw9ToXm4iG1NmRbZvY5zwvOzfOqkaGN6d-P8D_RTSwC_RDWah6lN225m7TOEAsSbGmYc9kSJEbSLcSkqvr43JWeFRgIU5wl8wtFXgLcprcxOss-6K_M3oaT7AyKTvmBJJzk7fBuPoR1B72CS5OYmSe6Qk0NMoLyOmsqkFAQCoRS7V-pu24DE-Y8WcTvPDQhcCZOoIaVfQVc__YY5CjvNS_S83uLfDYZ7ou0JYIVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na31ISnVdauZtqXt2D5a2d5iy_2AydWuIBjdL4nh3LGHn3unjoC0qHpeCaKfgTg1cayW7Fh05G8qxgSNfZLgZa-c7jRpibnt0RfEgCtf-TcFCKbG_YtvN6YkF3mn6MLQG35alSGKdfHJpDDFVTGAjCYFiPUrEfRejZii-oi_SFHxDiarB7ApC8aQGTPmtRXOCeQ55m3zSuUDTHG4E2bEJ9VuiIUcQW-jyVQ-0emEhrmQwStoJvGzCZoq-uUyWMf66LlQSMxOSX9GcosWprul_dKuOQFGczgAAU7SL2gYGvIB7qATtgW_qjV5wqc8s12Q91WZqWyZh4zJ9oWSkdSdiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzyJf7yosqMY8ieXN1JutVmc6NZ08HU7qpYSKw0e4Wp5YA8hkycrpE8uFxfL2fimJS9V7h6vVSuWrOs8tFOl_Bnev2zSrsPit5_rVQEpjxQg_HmI654PQ5yWICX9eBzaBMP4NXUGcWK3FCbu0lXjzHBfC3hvcRybp5zrKneZZgZvVbelmycLxLmLu9-TaQj-KSIorvaxAGwzJ-wILbdugZHQp3xlsCVXsRtZsUld2e3Uc9LQChT5Zydjjgj_GI_F0v2iSYipgPivq_JpKpGV3Xc8dY3OSHkUT1PCdJ5NKmftXYTEIlGwIG5oF25FZsOtfv7hLC_cVwZiLjkd2p7O0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h01j0m6BmthfUGBQL_uswYFUe9wueaTGnLl_NunPShAkL_UwZtjxt6HryP9jAvzxFIOS2N2BFrsSXV3U8WQrzHpMQY2QGt6G6nH8FX8nDynieEUJfv8o_k7XffaU9exfx746eF5i91KpGg-089FOwOFXo8eMTxkdO-Pp6Y_eWYWd6QMTjZeq0b1fWiaBxYkErHni-GzRUi2yXLI4_KqjtqMiMqAIV6rjd1LqE9IE1MQDjJwmikMUQhhIpQ4OE9JLQotKPG2clljrgKbA2JBqbCQkiKZ0eFA4Ho3SPupqnL-xN7KdpBufeblVYnyVQ8hzliaqmQ9brZ7m3g8OfLwnXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtnvdCc9dJfLCaWwhrtmeEwjLJwT5hMbB_M8u4IDcSyrvUz_xRy9pbEIdWxAMHMijkf6xKNubcGlFfG8vCSsqJlz7vvs-0ihrFQtMlZQVpllRSJpE75jss6kwZTpGQLEdX-5HotHoRu3j5TaIimwO-4PrFWupg6U1HkWjrQvE2pApiBR-5g8s6vulotJccV_xFQghepYTwSHI0VCIyWF9Sjct-ShO-f4huwZfFABigpulzzNaDX4XznFtP1D6SaLz95N0AQPsS-2jDTwXk3hlIR9m8oFMCaHOYGaV_zZTq8tfhpUl8qK8Avsq8kGQ25a_FP8mSf6_vJ_RV9rxsvuAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=Lz_4F5xVLqrgYJZnHrNilRawz2x-E4lMOKUhGdhvMbPPfIgS3bmOlGj67So9jqXUihQjAactg_X8G7PIylvRYHzBXtkSfnCuqApqkfbvS3rP3CkufYrmdJpoD-50S4ry02j6BDxx9JEFGktZ9I-cjzEphRFPs8nZnqkjSZnb6aAKC8h5XnqQrj7zE5KGy_OVX5yJCRfBxV6NypC_wsl__nULq0yKfaKoIchn_PnmZygbKfNHU23Wm1w2vOLY0w4JFS4ryWAS5kh36gCEI20sJQCz3rU5QOigBf-RInP385Se2N5czQF784rQHDmrph_OMIoqvjsw3AB8V7NQ1_ynGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=Lz_4F5xVLqrgYJZnHrNilRawz2x-E4lMOKUhGdhvMbPPfIgS3bmOlGj67So9jqXUihQjAactg_X8G7PIylvRYHzBXtkSfnCuqApqkfbvS3rP3CkufYrmdJpoD-50S4ry02j6BDxx9JEFGktZ9I-cjzEphRFPs8nZnqkjSZnb6aAKC8h5XnqQrj7zE5KGy_OVX5yJCRfBxV6NypC_wsl__nULq0yKfaKoIchn_PnmZygbKfNHU23Wm1w2vOLY0w4JFS4ryWAS5kh36gCEI20sJQCz3rU5QOigBf-RInP385Se2N5czQF784rQHDmrph_OMIoqvjsw3AB8V7NQ1_ynGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=ejauYeliPbtz5_It9x2ss-zrlqHmYvVzssaT6TB3DaIqqdKE7_0So_l_rMS09fmXloy1LB9FpGoGeP7YGFbq2W8YCVt-mzgZG38AuPXMRVy_0os4eXzOZQxYsDcB1IPn4PlZmOXdhR2IsbaVSTEC0sdAmsdG2Yi-Cmt4d80eSrReat_MNv_HTTf26WuaiIyVvqZvzrOGbZTt1hK7bStS_McQ23N9iZYLYJi9VNIZ9aMK5HuVc_l-zh-co17XTO8q44eIqgYo_sfGyoCbzdQyze3m0tI10S6LndMkrh71bH-3ItasCpHFNArB-194LaCdOjR-__na2X8cisTt_K_QfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=ejauYeliPbtz5_It9x2ss-zrlqHmYvVzssaT6TB3DaIqqdKE7_0So_l_rMS09fmXloy1LB9FpGoGeP7YGFbq2W8YCVt-mzgZG38AuPXMRVy_0os4eXzOZQxYsDcB1IPn4PlZmOXdhR2IsbaVSTEC0sdAmsdG2Yi-Cmt4d80eSrReat_MNv_HTTf26WuaiIyVvqZvzrOGbZTt1hK7bStS_McQ23N9iZYLYJi9VNIZ9aMK5HuVc_l-zh-co17XTO8q44eIqgYo_sfGyoCbzdQyze3m0tI10S6LndMkrh71bH-3ItasCpHFNArB-194LaCdOjR-__na2X8cisTt_K_QfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=i3Dl3Y-0V3ziO9jgV9yrzFk6Bc1sDXnPRgQEYosPeqWl7gcUmN6bLBQMTwZI-0WZ6PaqL6158DIpbbvZTRFllOzKPdQjnllKmM4D1N1rHIPEpQhLfyHLTiEY6ycFzL2244_QuEEbIEKupyAh1xALsLoexuwc2PkssPKGO6nz2LYeenHFaMsCmIYHgD87JRsF5zrM1mJnpa83Ha0pU3l_ZMNrer00QIG9G8XODN0QSHNrU5ruln_R4TB9FMAyT4BrHKh-OzuShr-xoykdWy1ElF7YtUXX7i-cGXMGrFWNJS5g4UBpBrOvTWEy0nlGViHljaPn3l-BEmVWX3lIlA6LWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=i3Dl3Y-0V3ziO9jgV9yrzFk6Bc1sDXnPRgQEYosPeqWl7gcUmN6bLBQMTwZI-0WZ6PaqL6158DIpbbvZTRFllOzKPdQjnllKmM4D1N1rHIPEpQhLfyHLTiEY6ycFzL2244_QuEEbIEKupyAh1xALsLoexuwc2PkssPKGO6nz2LYeenHFaMsCmIYHgD87JRsF5zrM1mJnpa83Ha0pU3l_ZMNrer00QIG9G8XODN0QSHNrU5ruln_R4TB9FMAyT4BrHKh-OzuShr-xoykdWy1ElF7YtUXX7i-cGXMGrFWNJS5g4UBpBrOvTWEy0nlGViHljaPn3l-BEmVWX3lIlA6LWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=aoihpfmNfGqCAMgGQoRoGghYhvW1nU__QGPjJc1VWNjKv7idRmmoCCNif8mPgXytEmL4A15vlvrBzX_j6z1-IvJ-rXF_vvynRLPVblt_gNWmGVcJnELHGBFY1GrMoUyLKbc4CE5Nazv8tOV4Nw2g2FV1Mo8Isb2QBExewIc3QGMCKtSPVDkfGbX7VBGpgDt6igwGHih6Kcv1j2rkFhg51cvs--mttE06rSxSQZuh2aZWLCNAi5ncT37llMCB7ie5zfkx-qO314EbWzzn74Sh05OlJtCOP-oMJlcccEjml_TMdDbXIiISKBKyH_Dx3eErghmJYRt-bIq1h6yizpF9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=aoihpfmNfGqCAMgGQoRoGghYhvW1nU__QGPjJc1VWNjKv7idRmmoCCNif8mPgXytEmL4A15vlvrBzX_j6z1-IvJ-rXF_vvynRLPVblt_gNWmGVcJnELHGBFY1GrMoUyLKbc4CE5Nazv8tOV4Nw2g2FV1Mo8Isb2QBExewIc3QGMCKtSPVDkfGbX7VBGpgDt6igwGHih6Kcv1j2rkFhg51cvs--mttE06rSxSQZuh2aZWLCNAi5ncT37llMCB7ie5zfkx-qO314EbWzzn74Sh05OlJtCOP-oMJlcccEjml_TMdDbXIiISKBKyH_Dx3eErghmJYRt-bIq1h6yizpF9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iySf3Ltlis8kIvC_AGUEwpPYJwCe1XokZEIJdl5E7ZRQq-3L8N18OjATKU4yXMlsXWfqu662xBgDmTABYnPUYgKdMreUhMQJ6Yir3mRSejcSfSBXFz9w5JfVn30YH5-XIrN2KB8WH0xAboJdDiwcCMQKV2H1rbzgKG4QA_Iz5mIOlfdz2AveVLkhvO4R3DhwSKvpbEVKUCCwPT003IyKAY1dgJOy1hI2-APd4hrdgeIe80AyKQumON0iUxsDEYLPSOqst4VHuKmTdtl0-RuHBpbGna0Fp-O4rJFOjpC4c52l4wkFZfQQuthMoKhRFvdUxnVknoHH3DkD_uNWlsfWfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Foj1WzYr_ROqI5R-WXxGqvxRSUDSA0tRLt-RfuG14HOwojjSfzgppE9mrTcw5WPitaAQBtmd_9AuepOkVkbXSTeRcnhCveolWTvp8mXYO1wB6EBGxM_LPjbRwl9Ri5JfGrhFQORHmFTCV1CAgbO-qNkqVXyqOgqaFyvmTzDxqT5R6SFL1snR_rXBjkSBsiE4-vHD-OWKrvsMFQ_1Axz7lgktkWm_7tqEbNiRSfIhTMzNa8754rkpwqi1J0abKMQYPSXAutZGUU8vwBVJGTdD9eUineuYj6k77NRyl22tA5SB0pN7QN2v61wcO6oR6bmHI3jYV_rQaYg78xp7q0Crfw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=kEm5IDyDUFtvEVqHrtdjkhNmgc8hV-cjLJa8qWc2uQc-pKq2Xn9-SkckDLfPhgaYGEM4Eel9CO1RzGpaUXpUADYuEvPtst9Fle8pM1c5gDTexaw7-CVXyjc7TzoBZYiH_yTGrN9MtuUpoMaj_88gimYJC_b604-xIhtghn6os7_F0FnDgpweknqzRUcR76KA4_Zwrzd1qEgReM1vvMXImg_E6Lwa5DRuQ_Boct5EQvDPZK5fH8HTFzraBrnEyEjzUlGvj70SAkyAOVtYXhfwcsTS5kvpig0MZBa7OHwcZ-X9bSZnSXnyal2qW2NE7XWmZL43aPUukQ81ftWDODs5Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=kEm5IDyDUFtvEVqHrtdjkhNmgc8hV-cjLJa8qWc2uQc-pKq2Xn9-SkckDLfPhgaYGEM4Eel9CO1RzGpaUXpUADYuEvPtst9Fle8pM1c5gDTexaw7-CVXyjc7TzoBZYiH_yTGrN9MtuUpoMaj_88gimYJC_b604-xIhtghn6os7_F0FnDgpweknqzRUcR76KA4_Zwrzd1qEgReM1vvMXImg_E6Lwa5DRuQ_Boct5EQvDPZK5fH8HTFzraBrnEyEjzUlGvj70SAkyAOVtYXhfwcsTS5kvpig0MZBa7OHwcZ-X9bSZnSXnyal2qW2NE7XWmZL43aPUukQ81ftWDODs5Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uga485dvVt_1TCQjxpuv2m1XRu5kveUotRMmBBBBuYZKHaASe31RaWmDOZc0t3cQZrjaGiWvba58EFO0PeRQFK6xBbgbArZqps8EW6VQE-GAOV0fyKaR4O8tlQGhdQOEXvk4AR8XnhHTED1RaSpNAaKSEfUl9Q04MDljmz5FE5tO9BQTa8AsFDczIGdwxCtyWJbVKIsWoi8QmJMlATuO4Qb89fL9tLuiN2pQOzRr1ENjnj3qaNkz0_mcJxHd03JS0efAcU06FuTtkh2GO8IZgyHkNSTE5uoc8364TPs8D_lAcf0DR5anPpG7-_58NVXtIAfy_3bBp2dAHc6V_s_czw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=HGIYfyDCOKm8VhKiB2X17QFU-9xkQyDJAzQkm9JnvNG0smlbePIxHlq4SfU7GS9EimXOEaE4GlK7mbmT6CYWqiiecQEdeIXJgY6HNULkifCXkr3ASwiTNtSLxxppOm8OHMZHb7WezOnwneKmNqP1LviJiWxaxrHOFOP2iel23FI6WTQLdDU8Of_2TM8Lae9AsE6ocJR08TdAI1UPSGBRS-KmhjoUtiHin8jwZ0O_Dk6c5IL5bwhBtJHKVz_A_aNKww8b-pRWOAI0stc2lJbDYcCoYSreY7K_ld8sLZJrLOqi5vipl6ZQ9wNU_ddIe_NfeoJYlDHZe1AbgWC3sYYLGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=HGIYfyDCOKm8VhKiB2X17QFU-9xkQyDJAzQkm9JnvNG0smlbePIxHlq4SfU7GS9EimXOEaE4GlK7mbmT6CYWqiiecQEdeIXJgY6HNULkifCXkr3ASwiTNtSLxxppOm8OHMZHb7WezOnwneKmNqP1LviJiWxaxrHOFOP2iel23FI6WTQLdDU8Of_2TM8Lae9AsE6ocJR08TdAI1UPSGBRS-KmhjoUtiHin8jwZ0O_Dk6c5IL5bwhBtJHKVz_A_aNKww8b-pRWOAI0stc2lJbDYcCoYSreY7K_ld8sLZJrLOqi5vipl6ZQ9wNU_ddIe_NfeoJYlDHZe1AbgWC3sYYLGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kxzs61k-IRiyrIXQ81qzvivM-sb3cydqM9ixN5ZzN6-pjVQhpEWAk4Bwk5DzCZU7GQBatJkmt-dE2TfQcec3YftoyLILvHcWT9KYiu_tuihVLWqpJO_6h1DO3zlT-LwnfUpXXIMF723Ri_OAKSfCbGbWC8lroIkVQ5M6qk9hudhuK5_usw2_2H_PEeR9oEPK_1CyJO7vHPXCH7zsOuWrtONstxotbyCbfbAbZ2yeHN3taXJ0YzmqUVIRBhpfbuknpG_ctnjuWs9CnITkS_-kxnAwRK-Mskrxqbhm0tUU6cFkS4GdE-TsvVPb3PoFTTety_Xid651PUAduQ5x2FIpKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xjn-HEZ06x9TitU2fj7_9lTyFg8QZaOCIfsFOhPGHf10xrACFB4gBsACQPncLpzjy0_vWpoY113py_ne-g_pzypO7J1fXvcvg-BwGrnKhIyNjwJqrg44IVA-EEYjTrsoALckb4dkv3ZzeM7Cjs1PNHZexpuvFpgvZcq6Fts5YFtSy2SxxPOzjWbJU_rSsiOA_-hPZexkpNW-pGCsu0fbYrzJ2zuyXtKfw1PyrDeyvOY9S4k7wIBxm3HetgxK1Q_pwYp97t3XhtelBkcb6XDM_FJaOSfrYLTkkfyP0DbYXAdDt_e_rLPXcjBVJOKoYJ3iCVoF-qvlgwCu4TRR5ZpooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
