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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 16:41:52</div>
<hr>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6jRmf0ba--mShtp3pjmojRkhZCp-yUBEnp6GPKvFtb3MMpcG_cIQzwaod3z_JK_RX0WcI43aGl1PG8XmYwzcaGgQ7dZllPn7bL_tAMkqu-e8pnolZdB-Q-a6S4t4t_MRQdvzC9tEcOt7r153fqzATAH8LYRxtoTYUlgM0XHwMTIqMH_IdvxcS2oe0cyQ02n1aEQvjki0NWaxnrRN5V256yS5ch6xnrJnJo1ycvk2uS2MEvUjvXYooNISJULVTX_0ILL0iz-jyHamKmAPPmPccXw6i0CkTHoLu9aZhHWnUtG1tZkcqsayXmxDu17jTsRr3B5DD6yTk1vufypS2cbFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=FV5QME_MxtPvyGnvdYt6lEapBQUZq-XpE48FOaWhF5CPwJ18KBnoCoA08VDezzVUpcsIRT2spFlfBHzAHYsCq6jBYhE4-Cn_FCkreWenalal0dy_arzkVBbT8R6NSZDpf0dPmtiN0RPzUAwCiXwpufgkhgaItW21a-1R6TPVljX47IriqzOIi-cIyBt9fkuTn2g21C8CwMiQEYeGJBEGCmyCNiAROgKZmbmMeD-8qSB2l626lilRnm2a-sWD1XHhSj1agjxz2S2uBlI_6iuY8YMGIfRvXDVwA-AGZD7homXqlyuS6LRZ0Ha-brwJD9A4--yT5zyEj9QdzX2VlRFjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=FV5QME_MxtPvyGnvdYt6lEapBQUZq-XpE48FOaWhF5CPwJ18KBnoCoA08VDezzVUpcsIRT2spFlfBHzAHYsCq6jBYhE4-Cn_FCkreWenalal0dy_arzkVBbT8R6NSZDpf0dPmtiN0RPzUAwCiXwpufgkhgaItW21a-1R6TPVljX47IriqzOIi-cIyBt9fkuTn2g21C8CwMiQEYeGJBEGCmyCNiAROgKZmbmMeD-8qSB2l626lilRnm2a-sWD1XHhSj1agjxz2S2uBlI_6iuY8YMGIfRvXDVwA-AGZD7homXqlyuS6LRZ0Ha-brwJD9A4--yT5zyEj9QdzX2VlRFjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=pYjXjK5qPQuNnyviDJNPDuPH7_tvnHJfCnXr6i72Olh1h2ithz0rosXibIAwQX-JuUiKXj_YF8czaSXeRuH_baKte4RYxbdsgu6cbaL6Tg4Vef_dkPRYCV3fJqf2ASN7-lIgg7iJc1Z6-woBGStn2bXWIUkx67atfd8BNAhrWmggaDbs8XSYBF-CUQuGn116qu_MQhfcCuK3NFh0DO2saiWLvqD7-ugHLZ-_S-TASxXPmixhnOys0nVzJstdkFrUYIWhPoVWBkkZGkyaLBDzMe8VizwrhvSGwG1rRXCKHlj2QVZWVd4Qu_zuVybK4b7MhGhEEV8JTnJgKUpyztQFvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=pYjXjK5qPQuNnyviDJNPDuPH7_tvnHJfCnXr6i72Olh1h2ithz0rosXibIAwQX-JuUiKXj_YF8czaSXeRuH_baKte4RYxbdsgu6cbaL6Tg4Vef_dkPRYCV3fJqf2ASN7-lIgg7iJc1Z6-woBGStn2bXWIUkx67atfd8BNAhrWmggaDbs8XSYBF-CUQuGn116qu_MQhfcCuK3NFh0DO2saiWLvqD7-ugHLZ-_S-TASxXPmixhnOys0nVzJstdkFrUYIWhPoVWBkkZGkyaLBDzMe8VizwrhvSGwG1rRXCKHlj2QVZWVd4Qu_zuVybK4b7MhGhEEV8JTnJgKUpyztQFvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTwd1PZgtxyk9gR0BeLXT4HH9NJBSEv-GoWmPocklLko1kaf4l4DSkY9gdhkW4GEPAsm579GvpZ9_dMnFvPFrVpeK1iJRhpa8vifE17BpLQfhr00rnK0v9UOaUoQx0Zlns4m_NNYZexTlSsx5rUDY8aQqpxlf5sA4oFXATASdDNmK2Y98zhpHZzBw4lp5UK___g91VDmTjZrzpCws2F7aCKct5QozVKtpMYQioNYpZ6C-NTK39I3tKuP4DiY7UNvire5mXpaJMGhznMxllPphfuXZt9XMFn50O2x4KQy8iMYXDSodh7H1RsaW6fBRE8fReRavSpm6NEm0AAXNKTUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UXWRm7lYHpYCw1qyAzHoH9RpGZg0HjFgdm8Q1kds-ms3j-nRfwtgDZXcfonmTD7g6owXxChLzeQwDUA59NS_vE-mxipovnL2q6pNqPjqjkTiFX6GLK0-OczdSTp8YLYn1dtMC_ZKH8KbE6tzQUkPhKP_Vs_i5dipAu5elZkl7_tl3sI8ixpk4IUz_FiowCHCC5ynH1vflJ1HToS-R8bDSfMXuBY_TxmRERE00Lq-_NipJVwv_H720p27mV8vqC0v17o6dDEUxD5wTkxtWFF0Ccna0UgMsYBSwss8KjxzJwSqqEcm8mlPeGFzeuQjS2Mvo7nCXanZ6JwtBlJCPC7h0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UXWRm7lYHpYCw1qyAzHoH9RpGZg0HjFgdm8Q1kds-ms3j-nRfwtgDZXcfonmTD7g6owXxChLzeQwDUA59NS_vE-mxipovnL2q6pNqPjqjkTiFX6GLK0-OczdSTp8YLYn1dtMC_ZKH8KbE6tzQUkPhKP_Vs_i5dipAu5elZkl7_tl3sI8ixpk4IUz_FiowCHCC5ynH1vflJ1HToS-R8bDSfMXuBY_TxmRERE00Lq-_NipJVwv_H720p27mV8vqC0v17o6dDEUxD5wTkxtWFF0Ccna0UgMsYBSwss8KjxzJwSqqEcm8mlPeGFzeuQjS2Mvo7nCXanZ6JwtBlJCPC7h0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqT13RyNpxvUyZxQNFhVYfQBzIKdeLIX-Wx3tewxuP5oCuimFJi1Y5a4guXAEES5e8XGvOKKLIw6w2W8sxvWzUSm5sgZb3CV8xBuEDUFtVGBC3aJbm5RpA5rbTftS0PZVXW4nKbJ6L9AUlmHbvEORdos0O3eW-Nfzafm_GNZ9Zcda1j34Kw79jObwWkAc3s9iE-X3J8S8mAPJbf8eKKGzkPWaMau4hePQz85wBuhjEi5wb1F61e75ikqXinmHFmfe2Y2IR3XR3V5HrAwU2rrfCqvW12n_87wCDI-Jzb022Fh9lnpve7BsPj6WTy2uSRtmxHaYXGebIsa4ghxxdVVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXER_l-LBMLiXUNB33fB_pVLho1N5j5geqD5iwZNSCRZeRaXcPR7rODAX_LnE_Szi2zKRCO1dAeb4GSYNlF3ZuMKP9cIRsGMs8d2c5GDwFlyL0NqOO1s6CBbPzwRGKpBL8VALtX01MDiZ9uC0mw_7aNYkVfOFsbc5DANIYPbEomTjZs29DVOQXCRKvXTLxn5HkMMkcvfugzA4UzisZck7ljHcJr0AnO-3h8jTuHpVBd8qqP2r3UZYsqzqfsRbZqv82noRdl9bdBw-jZEky-ZpfyQuJew0FLLrHYpMZVyFdf9MAtj1nOVqLTSKvZXIDACEBt5TJcrjxRta6sgm1PiOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=bfHtfbFkcZhEeNXQDX90Dj1WTs_l5DBjrTFbANLd0RfNw2qT1pJv5s7qk5RR0Qb2o6ua5uoYZuzFBBBLeZhjcYBbuyufIweb4RrTSRRGa3CjATpEHUgCTpvjDtPwVd3ZQ3zRKwT9m9_h28_HnRKTRQWORjwqYEsigmACNsrNCxsbbUfntuhULMTTZhduatEyRr9z4PwkElWasbNuzTigIKVK1Q79cnvRSnak1kZ9UfFumGfsZecxcd2OvkBAqowAyh2jmmZKz-02Vtf0pxDu4mb0J7LV8cwEBgsMxTu_-98kPfUC8AOUDwzhhYC51Va9GN_IsEngqdVBRtVue35HIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=bfHtfbFkcZhEeNXQDX90Dj1WTs_l5DBjrTFbANLd0RfNw2qT1pJv5s7qk5RR0Qb2o6ua5uoYZuzFBBBLeZhjcYBbuyufIweb4RrTSRRGa3CjATpEHUgCTpvjDtPwVd3ZQ3zRKwT9m9_h28_HnRKTRQWORjwqYEsigmACNsrNCxsbbUfntuhULMTTZhduatEyRr9z4PwkElWasbNuzTigIKVK1Q79cnvRSnak1kZ9UfFumGfsZecxcd2OvkBAqowAyh2jmmZKz-02Vtf0pxDu4mb0J7LV8cwEBgsMxTu_-98kPfUC8AOUDwzhhYC51Va9GN_IsEngqdVBRtVue35HIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs2PsAHxgsIzSuTUkxuvBA3rNX2fpAQhlOfIKqHxbNkSEHa-KTOHl3CAMNwEdwhU0e65CnJVeGpLCAaC2bL9u7wrFS5jjAWdc2UK1BvQ1SeQg_CqR54w6LCFCHvVhkre1okm3JV-7ld_Y3uIgsRmYhE650_eUuwS9uy0ypAavWPPQ9B2uDwVaHvneBezH-N3E9LothbhpAdNetPharzqmgQ9mXuZTM2ydOSi6ZkcTZ0pEYZSd_8ssCboVWp_3d39v4iFRwcvSVMJj7DRPrsDHWQUhAiY2FqGz4lAEo_c66Gabo04dy_aVVt0t9D_EfhGqGpSlX64Enjb299tJNcFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgDyKCIFEawQuKRuajP-DVDVTd1Ga_rSK6An4FYmu5tAxlv8-AM182xBy-1fvpLGrFjCGZX39Vo7QkyKvO30VeKd_jP7vthJv0lRXdNVVhyOaLyaR-qf03n5OxQDg0BnkhMPG_ExvuGqBr0AqR6ZLJ7PPXXYhIqlOaEtqa76UTwGmDHsoLmqho03aA3OksSX7YPHfJjA-3dAGodheWP_4wVpmOeQjI-0lV_0vmjOgko0kjmOcv8PiY5mHQ8zjhvpp4Kf4HlIcj4xwp1SqVgbXdSPimGzuTwkRdj5N_5y4u_8pKUnW69mkSrDfgKmci98brOZDqJb9luH274MhlwRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fp5cXG1EJqBDsqu0gKsZdvUad59FzSjG4MeAoCcJ7ujnhWNd6s4YoJOTyTlpRZi2yOjIC-R8p_wptkIOY4VY7KiBFjrH7r01yK-ybYUwHB5-vArQbpLvEDSky2oA_zKM0-K_YtUhoWojToPx9U_MhHJwHh0L7tWU7HW6cuBX0mjLJrQApm4eneBo65TdTNdVU1N4QvoqwDOkBzbQEsEaXB2qAnOAzmYDRvd7rwJlGloZ1_nUru8xeV5z9bLhhVa4_LOVOfgjJJQ0NvtwDhbp6B-jp0WuXBSiGge4coHVkEF4iHh6areDJcTnWDou57aI-CCy-Efbx0029gfKMvL4QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=VjXJk4uaU5PZiYyb-2hX6E14DmQcAsOS5yJREG9d1l7pGF6K3v9IR5b8yuwfC0dwZp9m5WZEsuKyjLikQqjUtd89x-_2vxT9SYJXIRXr897hZEWzzMUpBN1VPq1ehBCgupKti2efT7YsZWEBndZ41KI-6xIgnqtQW4oNTfZ0igk0cavnlQ8jvhjx5owCJRZOt6nwVxjJVLzXguCnlAVIM3bTaw_IO67OPf7pyKc69sAPcUjnaeZJ_qwiz2QVjWWCcdPxE4PSXG8a4wU9_oh4zXPx_zWjIXSuV3D54n6eynhlurRfl-5rqjgFPXz89CIwN9wIRWugucsfBkXMyB3xzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=VjXJk4uaU5PZiYyb-2hX6E14DmQcAsOS5yJREG9d1l7pGF6K3v9IR5b8yuwfC0dwZp9m5WZEsuKyjLikQqjUtd89x-_2vxT9SYJXIRXr897hZEWzzMUpBN1VPq1ehBCgupKti2efT7YsZWEBndZ41KI-6xIgnqtQW4oNTfZ0igk0cavnlQ8jvhjx5owCJRZOt6nwVxjJVLzXguCnlAVIM3bTaw_IO67OPf7pyKc69sAPcUjnaeZJ_qwiz2QVjWWCcdPxE4PSXG8a4wU9_oh4zXPx_zWjIXSuV3D54n6eynhlurRfl-5rqjgFPXz89CIwN9wIRWugucsfBkXMyB3xzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blMMPxqV-r5weHQDioPJrOlz5vD-htZWk2ijJAlcImRH0v5fKHd5gikClugnEfE2XNQmj9wkb_5yKl9QDzetncTwCT_DoiR6Z9FL_ndABjHMi4dwoDvgGm2KYURZRi39xssKVKfZjtcTfDCz4NEqAWH64goubWbEc2gKFZRLfQ4QK0wz-2Tp-6BWuBbYUJ-WSWDeLLIyHNoeHp43Wlv61kOdWGvT7ZZdbO_S9VqwMS020SoVUvhxblIW6GkMD_eei4sVMKotr-0tnN6XiMeO1U3kAMbl6cLXNlLIRodi-UQoB81bmcbDqtKOFuaF4J9ca08u1i_5MiZSsVzNau_glw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fn9yejszKvHZx7undqgslW7LpeXO0TIcD5w6OkNTmxRfmXu7hxSNZ1XRIfQ6Xh6A5uz2WhSwzMKNVlLaMPOD6xd0B3WxGN9-1P2j_7IzXmXqWVgl3fMEgd-FR8gTw-4yHN5JLWyPN2hBtVNtSpGyto9nSaN_iYZZIPT1UBDPxjKAO9_2L-cvEce_uOt2zrVExoQghmCXyX1cFcdwvEzUoLptbf4QxXtkwMUhSSAm3Itvz1kXhqDvZp6OugjZ5pRtFjtjMU1EETleT2oj-JPocn4yVUKYQKMJT5CnKvlA7R8XBJUlvy1Th91QjRhCfkcI94mrM7isiGeMM_csjoGreA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAA0DAkqU45tlDY0coK-JeafG_jnzSOB0AuwATRoIOqfhDUT81j_9ioaVqt-GKQotBl8Vxlh1HfT5gB-ve47DaQAhMgT2D4Nt6EJXcaaXB-3YumEHuLBp4ZMK-WMKB-iW3Xeknq2bAkZkw2rqpZuAekZ3T4u3UeZQXUd1ee49am0NK39AgVfZzuhpuZpG8rjYoHAEkvXs_862ogJDLwHLgqaOEveTmge64EotAHq3ZKyu6thhXmX0_eo_8QOnLcjJYHRz_9nCWsuhmXS7kWCvYO4XJXcU4DN11A1T-3E810vP9dsY6qafYVpa87YEnImoXSNpSQ-5T5IOH8zqF8YWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=CasPKcCVD7mvuwRWwjBYXkQ_-UIX7cd5zEhLP965ASB0qmejKH5kF6PQO5rPU3gcQiQNIM5Q8i0Q6skFPJWgYXD_eyhhdn3zJ-QKIIxqGZmu3kq4gIlylt1CUfjm3dcEhseoHMTfpfmx-MmUC78F0KIuhIlkkjNRzwOtsnq-zbI0IgjG__aM5loSUSmzMsRwRPcYtgVRf2e5aS7x7_ANTAoePzv_LwfoH8jNUWIEhUE3hoL60KsoP8I2z7qjmqzyzLoAmpDYzTAK2FlhLgYiG8lrAfeaGoSBvC7HWoXSQrxHO1FzcZOKlc48SzEnGNmg8ddD1r7fBZtOmNAOuRxXqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=CasPKcCVD7mvuwRWwjBYXkQ_-UIX7cd5zEhLP965ASB0qmejKH5kF6PQO5rPU3gcQiQNIM5Q8i0Q6skFPJWgYXD_eyhhdn3zJ-QKIIxqGZmu3kq4gIlylt1CUfjm3dcEhseoHMTfpfmx-MmUC78F0KIuhIlkkjNRzwOtsnq-zbI0IgjG__aM5loSUSmzMsRwRPcYtgVRf2e5aS7x7_ANTAoePzv_LwfoH8jNUWIEhUE3hoL60KsoP8I2z7qjmqzyzLoAmpDYzTAK2FlhLgYiG8lrAfeaGoSBvC7HWoXSQrxHO1FzcZOKlc48SzEnGNmg8ddD1r7fBZtOmNAOuRxXqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=W1NGA1urZ4pZ1JsQvBPeAkVbR_Kgev495nVDls-ms8TQufx0t1JMrryXs2wz-iNcKbHKXdOIOkTLFsgZuRspY3z56u35NFllrmV6av8_L7xjtTFk5M52JqoTgyv4Sd9xRpnvQO6eoZr8FF9noYzI0K943e9G_65y29MR85MbwpbntJGOXbalYLa_1V3AJOCaRjoUF5wwqoiwgoSF0gvOYpGk0NuD6rMdAmsW-utHPNFiT0z_gxdWh8Kt7l4uXNtEz7h7ADaZ_53CkyJ9L3d6rqif_M5sD2T_NbjK1F4olxes-5O-uvYEJtP5gL9u_7gv-Olb6mebwmlYZCbCSzM3NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=W1NGA1urZ4pZ1JsQvBPeAkVbR_Kgev495nVDls-ms8TQufx0t1JMrryXs2wz-iNcKbHKXdOIOkTLFsgZuRspY3z56u35NFllrmV6av8_L7xjtTFk5M52JqoTgyv4Sd9xRpnvQO6eoZr8FF9noYzI0K943e9G_65y29MR85MbwpbntJGOXbalYLa_1V3AJOCaRjoUF5wwqoiwgoSF0gvOYpGk0NuD6rMdAmsW-utHPNFiT0z_gxdWh8Kt7l4uXNtEz7h7ADaZ_53CkyJ9L3d6rqif_M5sD2T_NbjK1F4olxes-5O-uvYEJtP5gL9u_7gv-Olb6mebwmlYZCbCSzM3NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=Lrp6PYsemitJrPfe50Yepc1w8zTmdzTUKmuNbrViEfeAEVe93ytkwpWAVEiCBUj8HoypE4RGP49cFb11CCB3icaxu6C7JFFlPcjrLOvThGkvWkGozXZtt4xWQY8qaXPNY4C4e64u9btm6M1am5ywJ114z4yc3UPK3EK1Ync_eogMAfyA8Nymw9KFmqJ5YONVYyvdV4Momi8o9tDaeRSDGT40JU1vWKhKuc2F7Jfx-VI7LNVcDhpFsJEVqyJsh5vg8sr3MNk4sJGuDW1kdFZ400bORLtsANN8p_x5ak1OENfrPQv7OXkwAxukqfPkDxZFU1ArLvy08zzZa02VqoW6Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=Lrp6PYsemitJrPfe50Yepc1w8zTmdzTUKmuNbrViEfeAEVe93ytkwpWAVEiCBUj8HoypE4RGP49cFb11CCB3icaxu6C7JFFlPcjrLOvThGkvWkGozXZtt4xWQY8qaXPNY4C4e64u9btm6M1am5ywJ114z4yc3UPK3EK1Ync_eogMAfyA8Nymw9KFmqJ5YONVYyvdV4Momi8o9tDaeRSDGT40JU1vWKhKuc2F7Jfx-VI7LNVcDhpFsJEVqyJsh5vg8sr3MNk4sJGuDW1kdFZ400bORLtsANN8p_x5ak1OENfrPQv7OXkwAxukqfPkDxZFU1ArLvy08zzZa02VqoW6Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu8H6kYCX0hI2HKnuUHeiIw3JaVOGB6p7rx2gEP2eRBAzSX05iH2DtbzbLmYXP3046Rv1oi4eWOIR4v5j8aVAqapSUVmnSf0ZQC0kkWBZnj1kl8gd1RpaQkP56Fs9XzXVlmzhYRWofV8VosTVnzFAydmMEcjxuJcnzNinmBv4Jv-HoZbAzjvFzG1jYK88sgmbIfRKcl4JtrlnmpH3PrHoxNpJIBcDXS-Me7qQxlOo3jYjgCT3Q0l0bIMZQX5Kknr571qQjO8WIysonqx9fzqPlbPNQH9z2hKBYQJgQS-NdxU13P2En1A1HMiFsDTvB58mFTC9c4kL2hGZWblS7Vb-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9-x8jtCqmAIISjPFserkmGLzdtQQKzCMM-0yXO1q3Wj6T5xfZxLwPwRhPZ8DhvKn5U9sSFkKnh_nPpfF8gQvA5JwUxVdC8bzl3fbsf1zm6mAYmw7iB-UvnUihfcvQ1efqMZWJICm3kgs80AGP_jPSzEA7UlR309rmBZSwRnZYLZr4m77_Tt7Rh-m2htTnSh0g0HRKTT5ZblDCWoJGzjStSf_bjGCOWlP_G6C2Z-PTgiv2ixT8HqVh2vNrBvSe46Owea2P7L3qzZ6wkSePxy0JQ5OSt5gEwaP7wd6c9juWcfsClnPwMwAA2kTJ3aPGmPFWsAVXKNF-M4naaLGgodhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMecg3Sfvk0j8q1saMJ3wlI0CftEpYt16LDBAW4xigKVMBsjU8BEi1Rh5Pq9X5NgVE7li2TGz0udcaIp6RLwoOFyOPI9gPAPVashx8ydudJYwYAIjb3w2FTf8VVFnnyPLBiOXljbGHpflkZbf4wtIRF4dq-hj_vtufL7YWVVzZGMCYR_d6NOcsP_PLGYno2bGajXG2_qEmDRHNGJ8aQDAvMAJR_cbTTZboJG-sUJ9Wb-m6y9jkbauXPTxAMW05jfX5FivUCNMx2C6fbFVb5whuQ9XrVXBy6VvtM3GO9vKhO2dQ91-FMP-KYBdqbNYHcwhhyM-9xb8R4f3OqXnAjpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIiH_LJkWGD5Nk1wIrIuS4Ua55qwDKj5TQPEeczDgBNSEVw8ilVhso6mFMl5Zlm_XNUoDI3yXpXCbHUJ4pc3aQNxKnjItNzVmWF9EEkuMq6x53ZKUTjQgEyJCuA-JMn4U1-33mf1BsIuPBALrj8Q4gEl293tZB-lOSYHvksFpa0kJdVZx6ycOSj7VZ3aRc9uPBjOUWQX1UtEJrWP4k-smQh4y7hU6aGjPfqhnSTKfLSgiEfpACK8ua7nrq4DIacI5h_u3kReo1PjZ5KI6HdK9hzJpBAE8wUEX1ziUmw2v6SUWYRTKifGI7b3NIEKcTeVindDXLNJkxpYpKYRpi7-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_ZNl7ZG_pN7LsDRAkxFYA58z8JVw7DY8SDqw8a0bvwRrCd78L-Z0dFg9YSalxJ_X-karVoja81nwkiXElpf-b15zzBaga18Pbe9mKF37Pej_C3KLG_0YGrj7kpraB8TXsqeRN6CsJ_ijoiZfUc_K3pwVmGWw2BU5EYCRcVKJQKukwBsZjFeVz0d-seaBid-4A1Vhhn36HdZhbOGdnHCs77Ndsz-eko7Zelc2wXSO0a6IUmXdeNpXwaegU5thhgiGPiNLkJqRI30oxs9N8s-F_PF_RMNO_NHpnDQMFIltb6D683Zph6k5JGhyhlv0MfCHNEA1vvkJdB7ijtr9mD9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ej628mOnJZ2M9pemxqQ3PbSxwdVunYfemABs8VeMYWBTQvpkI0dDB5mL1qV5G9kkCkL-1D0FwQ8-wsHhq8uSMa2tLJofyXy9Pzlh3pnJMCpoelg9ojGpYu2O09GRa94tBbskhZfgfv8Zo1BDVrqBlevURCCtevVdlI0EMBF5XfzVEDDmqHf6oZrMls_S0fo9MKwWxd9uNtZSIzxfYzwgwx59Mp2uqvvrOEIADcdQ43ZLQxFqW0BbabOPIV_wxpjtEAkUAUtqpw3YEh111mhqU78VBewvZcd5xyqOzwXMLVBswrda6cA1_dA68ajDKkhAGePDtctULVTUzLeCi5iSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqMVd9XqlOV1ClBHhUimBqpQRyEjr8Omy6XKmZPkyePjcgbWSLnE7WzV4NWl_CQH1ag83jeKqpokwe9DICoAgRWGLFnh0mOjzUT0hfps4wlPAgLEVtW25wLVXgk3SYme9u6uW0m5_57w0ZoZPtgCbsiaVd-jTvDUSWodi3pcLasuXCSqyuId1F5O_BYGxO8V3uUFtzHlprJNTpWxUhPyV3pyYdoFHNgKQ14HK3AJsg2drLpRpC-IVlbTAfgWomSEX7YQSNeXyQgxzD4dcxtyY_KBciWjjrc9t94fwL-l8MDXhRTAjG_7YVtCUkoMvwfMVlcTEeqt_2PeIsPPtV9zkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2vJZnyumUhWWbA7QqcUHcfLuCfo-9O9zMlt45yorIUXvGWhh7S4B2b1VKTM5_V5XCj5XbmehObTMApxXeLBcE21vybjSgQzbG4Uopbpjd4a7QgdjVMy42zA1EDDW6UsZAzTZ3vfcywklfpIWnT9dybpzmE-24r8PbPjaB7keAVNiMXncEgvG3_c95U5bvAoR4ARLWA09Zc_ZCJs7YPipPfEZKV53JRb-n_wWoHoR1vlGFgWZ4RhSIxJny0zmRsG7bjA302p8TJJDxQ-8leMjOL8XeV2fH6_2LiInelNvVDO4f912KHQfJZmkmI5iW12r3HZgMqDSIeEf-2DCR1hHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeRLhJtjwDn-ghaauPl5V9cmf2BhkM59_lAeXNc-h8Wb7Uzb2LCgKREqlbBY2_w2upoHSznju8f27sd-QlVJ_3UozzZcwsHcUBCTPbFYVAQmWbf1m4UU75m_xn4h9k2ZSlHv3jJgG_QJHcxdA_N_Goqx2lFErJ8csi15VN08AmyVF51uNaLVPTs18Oqit9k61PhmJ4Yx5xU_KXlpaIgfHyiASLTntK9g5ydk0x2s3L6AkobQ2FuMgMRdeHPQq4ftnCjIEhDrDHHkglGAySuXICy5kYOik529_VqdBzA_Whh2LKwY4Ko_zcg5TSRTmx8rIVOA-X_K10Vr8rbwO8znug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sim8YVK2Z6aOKAE4zgku5mH0xcyjw45PW85QVjKEvQz95yNvIfm4I7LInfjYq_FQhYMALh62h4EeSrh5kjOEkSat2B9xwo675hJSn9t3TnvmTJGXTpMBxzP-n-nc5joueD58WhpK6QGtW2rDwSGpGN7-oAnItmfFeNmhu3G7lZPC8jfzPd6DTq8IubauvwgDSWKqaCfhxkcvivI-5HtXhMeRJkuHyqhBWVxuIwaT2smJ60eYg8c6UOK-lCqKHMxFgSsRCQOOZ_ITb4Tj742UFrmYVljM3a3D-0lWmJCvWjZ7Q13P798bHSoE8tM4vwhdJ9fIkWO_dg0JLZs6iAdIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un7I4o9jZvlY0atLSShNZCDdfcE9Bv3jTlvfBBAPmorGBTZR2jtLfOtvNGrvjJiuPQIvh1UZIk0vRJpj2jlx1RsiqkKsuJcRckkDyzM6dN9vQQV9qe-20iJLiOFj9fCTlqytxM9MRk8kHpuPu1aMAywgsEa0nWwgH3a1c-ngxacPwP92nql36ah43p6UM4BIv5htFqnjJCii8sL5BnRaZ13Jbu959XY3g6-CZSBqxB0nf5aIgwWBrqH4N_B02hZU8gSD5r2FlyhiqB-vqdls1Eb-9neF1NcpKBDhenPeXQTvoz3-OhlifZa685yoKIr4VfPi6JfwbzfDCu7c84YlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCETmNFx0IvB45ambmUAPBRLnq0JwJCJsyv0eHtGdXEV80EJ1eku2R1AITM_utaRuWer0e8FKLVBv18FTVHpMHraLZPmjsCqMUbw8d9vZSlYS2Bl1Yv6ezHWyvhFo9R0G6ljv1lYzMfyZFfKn9jwntflHshABZF4T6IhkxbX6f6citx1pLxWZZaKo3s8U2UxKt3RO2D7Fc_rwvBXkgrVCbC-G2tCoQe5WPWNvyBQluQSXg2V8YbH11LDG0bASIJvXLZMIuq6gNNn-UFzyhSw1hh2XW23ZET7F6E1wVGsSRiZU9KJegrS_CNBMA3gcRHsODkZNvJyixsmm2d7CTy76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDUgNkfEputkoIZ2AQBTghJ8NOBu5J8-QoZ5I7EWW4mu1VhLx5qmbRk1Wx6sgMWLMkT19rEW_q_W1GaKTL5kf9VfrE1QclPsCsIA1ltlPuTy3pBORpJfiXo7QvFndEdB-DaekLcn6S54zRZl1574j7QegqCEAGUkPxaXhOZmuWSY_VjUtcGRZEpmqRD3a41Vlwmw729Mdt3MRimNHLZth41wWaF5tv-yujgPl4ikPDaWnlw41eIiWdNkxGu1gsjR4wQWGq4qtnJUiQZCQO6t0ww73BBHWsVycWvaChxUARbrWCvp3HC6OKiHfyGq1hKJlkTB_HJ5DSZSSjhVipJgFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcSfNkSvZvZX8HtWa71zMAdP0jpQH-xwWuDsWxaCPWVYY9Mj3lv3-bZshikYCeL5bzYSUuSSMs531tHMhCZQx56dhSL1f4jYalqxPkfPMgZHts8gquivW4VMTG_00JzU84oNPCIeMZuXrbdU-Etko4qgUsS2HmcBr2wsT4aYTAWiarL6STkQqEpVOa1OUCYXChSG669jOJCp6ia2e8Xj6Rwv8PTeaPjHen_iNI0_ICc_MngQrN0wf_qv4ofLqilRRGK03vNp6VGddti3PoUHpvoB4DMKRZl0h_CqPGiqTt9vsEsMxCVkfml4TSn9tM_Ov5aWHfkrld9WgdHs2lyxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhRuyucO2Y8NTS0lllYdc1MPWuC4WlQrgbJ2nwTatkga_Gltq2zh5EVA0Xe0OT4P-8I-YSpImg-XLVcEDHJLrkZ837sBzHEV-uAjjrxeWMk9QgpUpXSTt03ynG_32Zv6pQW8OPOErf_TSb5hDCSB6TGN1eSdSExV3XDD4dYg42vPLqyxx9tPSrIz-NIhHOf2GYXkR_PJTOzoOX_O1qaPM8gLyFd2_mg8QKjZM3rt8CyUzj1skb1r8wpIEukvT20BeLfM53ho73SmHDjCPpbaFUwXD3yOt5UD2rllgtvxRsVJ2gNf2F3LfjWhBOKwkyKLKYT-3y0sn3jfn3bxAED87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=fqDsRjC-uE0OkEHKylj-Qxp4cJB8ItMzEKKioGFnP-z6d4Mp6QZMN--NXCvTbbo21NSFkkqzUEUK1q-5X3sohbPnC4d5w_Uh4Eqj4ctD2c_jvLA_fqljDFAC_aIGxQRs3mDFNMJX9M7gBYWUdzTWvu4FP0RjtYfyjxk4vcfhJTxLGI8QxWnHxM7CjupcGrtAAA4JNcXhckRIY0hFVB4e0Mz32clwDAow5cHE62xzk1GeQFSaROJmRjUqcXz0wLQZ7yrJDdTS2bp3w_Ymf1C2M8SAdhTOg6O4Z9F3p1wS9EtFrnEsNlxz1b1WtWBl9vkijdTx1ZuSQHsXy_yQlkXVhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=fqDsRjC-uE0OkEHKylj-Qxp4cJB8ItMzEKKioGFnP-z6d4Mp6QZMN--NXCvTbbo21NSFkkqzUEUK1q-5X3sohbPnC4d5w_Uh4Eqj4ctD2c_jvLA_fqljDFAC_aIGxQRs3mDFNMJX9M7gBYWUdzTWvu4FP0RjtYfyjxk4vcfhJTxLGI8QxWnHxM7CjupcGrtAAA4JNcXhckRIY0hFVB4e0Mz32clwDAow5cHE62xzk1GeQFSaROJmRjUqcXz0wLQZ7yrJDdTS2bp3w_Ymf1C2M8SAdhTOg6O4Z9F3p1wS9EtFrnEsNlxz1b1WtWBl9vkijdTx1ZuSQHsXy_yQlkXVhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-Qsfk0x21sD_1sN9x0qYKmJUrjt8Zq_CRyjI3wjPzYWwNMdgwFyuCwjIO0iriyc8QFY0VWaAHozsxbwNLwU5AQEop50zZUlxb7q4tcQ_TyfbBXqfisqhQ5gjgtrgzS_xvcfTaVO4KDgHcOcmHPZ2WwPYAq2TyTwLTNcb1XZSJ3I-uktKTcyAU0vRmYjrraUt9ZZ-FxqwhfpFiWpilFRy3Yaw-pcD8bcYR4dk0nYxxg_q8TUrSwIyz737IxRL36z2WE1FB07jdP65aIFJOCCzfE-ngPvaqC3a2-m4jeikx8cV4iLNgbGhAEdTBuDI55HHiNlf5tPnAtaQBfKFval0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=MiTM-KRnWU-LdtwVM2EeRkTX6EUFpfG_oE4IXPbUUb1DqVo9AG6M1MxFZu68j41c5Q4504UEbPlwV8AggovIkN97xDEC7Zsn5aamWPBWtkGDCudTQrVLE52VoyKqpnoDXazYqykmvzy8BOU1kpoSgoQjbQWhja9bnTNSqib6caZzCx8yDgDZylniLP2idTdl9fPm8q03V-XaYsyxnvQdSAJNQUOBaZAe5zhYX7RTN1I1JAWfr-EyN-A63UCUZUw3LUtPBklpnM4wgjhWASBk9xdauBGDAsInjFdTe2E1pq09Yqhz7ygZ-t7CuNtvNX4ackuBzUGf90ddhZP0T78gzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=MiTM-KRnWU-LdtwVM2EeRkTX6EUFpfG_oE4IXPbUUb1DqVo9AG6M1MxFZu68j41c5Q4504UEbPlwV8AggovIkN97xDEC7Zsn5aamWPBWtkGDCudTQrVLE52VoyKqpnoDXazYqykmvzy8BOU1kpoSgoQjbQWhja9bnTNSqib6caZzCx8yDgDZylniLP2idTdl9fPm8q03V-XaYsyxnvQdSAJNQUOBaZAe5zhYX7RTN1I1JAWfr-EyN-A63UCUZUw3LUtPBklpnM4wgjhWASBk9xdauBGDAsInjFdTe2E1pq09Yqhz7ygZ-t7CuNtvNX4ackuBzUGf90ddhZP0T78gzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=t7wRmPQHqNQvNqVPtzQAyaZFiHH5DBlnqWg19BlxRTHrj9lgfwoWOpGs8EuyaC3OHwniZQ2Mz_rG9NeVEUbEYaWbvj9r1XCB2mCp_hqdPZEm6hphmlRxlk7KRh99BV5-ArQFqArLd-FW8SQehPVR8nqgIPh_p0fdKGiSaJfsWCJP8uw1yfDvk3-QNdLHA5N_97AUf60CaFSGIW9lY9vrH2di3n1D7Do1ghr7Pf8f-4_afnk_yLcvyQxTezcvKQoCOZvVOlGONPpHVG9oJOnactfNcJkjZMKFG_6CZNUlIZUkQpXQfDhC6dEYByOwolfNn2AQnJz1LQFSuCN8Pdd39w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=t7wRmPQHqNQvNqVPtzQAyaZFiHH5DBlnqWg19BlxRTHrj9lgfwoWOpGs8EuyaC3OHwniZQ2Mz_rG9NeVEUbEYaWbvj9r1XCB2mCp_hqdPZEm6hphmlRxlk7KRh99BV5-ArQFqArLd-FW8SQehPVR8nqgIPh_p0fdKGiSaJfsWCJP8uw1yfDvk3-QNdLHA5N_97AUf60CaFSGIW9lY9vrH2di3n1D7Do1ghr7Pf8f-4_afnk_yLcvyQxTezcvKQoCOZvVOlGONPpHVG9oJOnactfNcJkjZMKFG_6CZNUlIZUkQpXQfDhC6dEYByOwolfNn2AQnJz1LQFSuCN8Pdd39w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLvcb3Y_8U35aRROjTJRcP0CA4XAU8gQm9uUotIVDQccAcq2il4C3DcYHmZqbl6lwFC08BqZsSf2xHyUICgBVwJ6ZIfhtc5u2IkeulIc41YnONE1oRzTZjjXhH9PVp3C2FgFRRajseS3-qj63LlC_iPyOvJRtHR_smaZBdHTbGD5sK93JUDjKIaaR4O_MV8sJWYZZyhkxEBL2qR2c5D2Rcebp6IICYasJBx7VK7mRbv6SswTQ8YOC2SBVIZQM9QVRsikz6i76C9OAXYiL0u3SdCIXPH0Jktdtwc2gDYnS-YPyPID4TOEYny9WbB-Oom3G22FGcCcVHcx2IsDzakoTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=VTW-DiH5HyT8E2g5QGCFooH_echCbZfa581XHxQ0U6MM38hQjsTWyydaD0DQpFnb0Ix3NnrCjiRkZ1Zvbl6-r9EOs48b3S_Fshpg8okLlD9wwQzGSuf7EXTLbfwmtESc1mtGF2v5LDC06XxX7NtIByNEJZeaYpnzvw0u4Jq-pyipD8MCQ6cYKCLz1d0xRKgrMHo6bFRoS9rWWcrJWlHkZfxAoilApOvaEW-8y9iSsbWJFBeXOxKxI3gM6liXrxcIbQ8qQR-UPIcufRx_eG2Z0c8eTMkR5uuBcgTOXWdd4BqzzuYUC0dN9U8zWlpy-Tn1-raBRU281EFvTPwZlv8Qkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=VTW-DiH5HyT8E2g5QGCFooH_echCbZfa581XHxQ0U6MM38hQjsTWyydaD0DQpFnb0Ix3NnrCjiRkZ1Zvbl6-r9EOs48b3S_Fshpg8okLlD9wwQzGSuf7EXTLbfwmtESc1mtGF2v5LDC06XxX7NtIByNEJZeaYpnzvw0u4Jq-pyipD8MCQ6cYKCLz1d0xRKgrMHo6bFRoS9rWWcrJWlHkZfxAoilApOvaEW-8y9iSsbWJFBeXOxKxI3gM6liXrxcIbQ8qQR-UPIcufRx_eG2Z0c8eTMkR5uuBcgTOXWdd4BqzzuYUC0dN9U8zWlpy-Tn1-raBRU281EFvTPwZlv8Qkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOANFQGilx54Yh9RZLzvmY_zDJQ_VUT_BTBtZUkiE_5NgfVaBLGIpaUCKciBA_zpG1Haw5pCqUlfyCrlzijFwUAP_66w4-RmRCPVrSHvTXscNmaMLePyUWPcZjEgwxhFD0NBR_-Qzz2rlPw1Wleo0PszLyFzHqKioGatYI3tk5Ohj_jXoCrAn-CqpxCcMnUSKEzkp1AmFgpmwHSlszBu9oIZoGulrMHZKntTtGJTtHHVk2MK5usVFMDzMGAWY9iG7NGg39pr_tnaHmqcKyPaZ6XqA5mj9W4giCymhK7VJKx68do_B2CpkYrwYhZCrUhDRr7CNryICKh5hvWaa7e_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu_K8b-A5kJcWSkhBlM2ty5DlhrTFvfY8be1zkEpRT-21Z7wytjqK4KamQJ66sDVF9kGwkVITAn3V-hvawkbh7y0Cp2L6P1lnirU2KZS2TbXa0BFP_878V3WTGCv8qRzpINfweK0iTIknIireNsBOeaRw0aWhkykY8OEj6syWVIeapNOnOabNEj3vPyX0C3VI7ZDjZsSlJ7FieziaCERo_m3mMPIpGrboAasUNo0VoLp6fbKeJZrrMosJe0tOJOP3I8umL5gsHMpyj_0rG2hdLg8ORt-ZF9ALuIrWbA7J1JjwsMzU9eI-p36TN_wiKWVyIrowDcRZ0wYXsgEl_k4NA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPZMt9Oe-6adoGTjxrr4uuwFX9pP7LMWkI9_vhqXHFZoX31ykI_6Haghp9Gkz1RTNVnK184tUV5gnODzZRvDtnVKrorRZRu8VD4PDPDDG1qooI4uIo9ssQI5zS-HijBVSrH5N1cWKniDhG75e44m_nBKhUBrNNu2fTIujya1vCTO0TWSa-A991mLOWarmOiHpHsi13B45KKwTav-1Cs8WAL1OklxGv-sq2SdUJ60_-oRgoQR5P-mW3Sl8gfaB3eJRQTnHEThZnxH5uM4czEjLhpsWYBSKhRfXIo8bIZCAOVVJKKO0Vv8oUhrjQqj-KKesALhWtfs6R9Q8nFlfL1jNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Za9Yce37beup5WkRTB0Z2-VU-yIDOvlzE1Z1svlH1C6Y96y5Ywm0MRxNiV1x5uTpE3cr4sWPH_3D3uwHjNjQtfnS6n2NZk65pbYu79IMTr5ue8eHLecZYGUeRpmdR-waElGrGllNLRkxTB7OlwKRa4KmmPM6cxV5FKV0Hz8HJHraPaLBnTI7ldeoiVbBq26qkUgpQd3Sm_c-Q0mKU8NYyatDYCvQNF1RfdLg6UImAw8A0gQioGVrjnFKUqaX9AyjX7KXopgrBE9eWFeA6Vua2jbgLnoko9O_dRIK6JxWgnkW6Rb4BdYcwEJXwvgyWTMi05cHOHsSuPwjg63upz2hcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=WUS9_hhX4EopVOzSw_5SqwaSQY0lBy7LNsRPWB8E0yzTFiYKmHOZxKSotd1gCKXoIJFJXhbZY5fUp8SQm_xmi5z5SXmHJhbHQCNnbDGnU1VgDyN9AlAsB-5v_JgmOTLpv6KhYGAxO-yBqYZvv5U1458VHsrSeMVuZ7nFDHl88cBe7eFubsls20E3-mKkiEiSiEeLU48pd1puPwfqhTb2HeXCulcs-7GBJzpKKneovMIc8aKR_dzzF_g18B1vkI-VNTORH1YYMA_oopASbj-QNXBx3-9Jnu6KGxkrIwyAyR27x-sE9PiYE39YFpvDnBHCv7xVBiZ0M4pwaTbWL56X0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=WUS9_hhX4EopVOzSw_5SqwaSQY0lBy7LNsRPWB8E0yzTFiYKmHOZxKSotd1gCKXoIJFJXhbZY5fUp8SQm_xmi5z5SXmHJhbHQCNnbDGnU1VgDyN9AlAsB-5v_JgmOTLpv6KhYGAxO-yBqYZvv5U1458VHsrSeMVuZ7nFDHl88cBe7eFubsls20E3-mKkiEiSiEeLU48pd1puPwfqhTb2HeXCulcs-7GBJzpKKneovMIc8aKR_dzzF_g18B1vkI-VNTORH1YYMA_oopASbj-QNXBx3-9Jnu6KGxkrIwyAyR27x-sE9PiYE39YFpvDnBHCv7xVBiZ0M4pwaTbWL56X0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=PqPB1N3cmdLeBa5ct_DmZ_uQH-WCJ0UtTTb0ZCMUIBJO_Htukoo0fevyF_IVK48bu9jljr3Bj2z6H4b7EmPPiwPB9vcjHBBVE9dd_ch_C6yFowQLm2mUBL3FSzoSVFTQwy6UFrH7UteArcGPqVf02BgYE4__GiZRwmHNUKlbQUZ6Eto5kPS4HCtsOE419YG-KJCo3o9DhXMQjEECFPB_G8j4yBxTmqqnYyU1sWTCVMLHXWANsUFjNKmyxAuTtMbp0VrOs0gvG47Qv2VjkdR_0zQQk6ZtwjFpthGAOhfWf5qPTZ3a3L0Bij3THRxHCyNZffrnlN2TiY-QcBLC7PoTow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=PqPB1N3cmdLeBa5ct_DmZ_uQH-WCJ0UtTTb0ZCMUIBJO_Htukoo0fevyF_IVK48bu9jljr3Bj2z6H4b7EmPPiwPB9vcjHBBVE9dd_ch_C6yFowQLm2mUBL3FSzoSVFTQwy6UFrH7UteArcGPqVf02BgYE4__GiZRwmHNUKlbQUZ6Eto5kPS4HCtsOE419YG-KJCo3o9DhXMQjEECFPB_G8j4yBxTmqqnYyU1sWTCVMLHXWANsUFjNKmyxAuTtMbp0VrOs0gvG47Qv2VjkdR_0zQQk6ZtwjFpthGAOhfWf5qPTZ3a3L0Bij3THRxHCyNZffrnlN2TiY-QcBLC7PoTow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=MWCJNO-8wYRqVNMKsNNFOzneGb2Rl0PcwK0HJ2UFlssyah_Hv77lo1Z_FLk51EU-YHV_blDfTX4fGFalt13rXeQTF99spDZ2UikEbjH90pn4U2-EpSCyFaQoOeREhOI2hVBQTT_PxbYJAOpHZXnWaf9yTBjZcYnMebOtZkyYMUZmJNLWiOsUU4OZRRByDiJdud4EgPBSsXJQ8lM18yJcyJVwCDzSoMqTdsWGKbcoMXz-DOB-gDx1MSn0an7dPLELpfaS_phyGWcR9RrxZTWtNpe5XO5xXJV85HMW4GwjUpwy-zTsGIjp-GH51I9I6_ClCgRoeiJevDeFtWbf7JyUng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=MWCJNO-8wYRqVNMKsNNFOzneGb2Rl0PcwK0HJ2UFlssyah_Hv77lo1Z_FLk51EU-YHV_blDfTX4fGFalt13rXeQTF99spDZ2UikEbjH90pn4U2-EpSCyFaQoOeREhOI2hVBQTT_PxbYJAOpHZXnWaf9yTBjZcYnMebOtZkyYMUZmJNLWiOsUU4OZRRByDiJdud4EgPBSsXJQ8lM18yJcyJVwCDzSoMqTdsWGKbcoMXz-DOB-gDx1MSn0an7dPLELpfaS_phyGWcR9RrxZTWtNpe5XO5xXJV85HMW4GwjUpwy-zTsGIjp-GH51I9I6_ClCgRoeiJevDeFtWbf7JyUng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=M4OFo6Qhe-St6DKx-KwY6jV9Hcnp2jnvC2Tj6wIMQtIxKmWqduKRR6tO-3wjxNc3lC38mjD_CoMQm7uoeNenWzfz6DKHhXDdySigsutc3TT9jQPa-LyqYei8Qki8zi804c7UNnuRpv8RURBbyWKgWkDlglc_FQ7zwQkYQw_Ut1IxZS7WZTSkGVWLe0Qkg0qBLne0DAniNb4FWzQq9xxJ2EajWzC9HDTx3OMG5UW0txfACeq5mBgNrg5D72ytZkh0nrh2Aa0kU0tKcbBop_XXczWPa4iIzgQgZI6A6uIIaUrziURwxP0izIOL5l_B8T83RaTJD-Qth2FbKiHp_R_iugCTw4kxRLWAQ1MybBsVnZ7O54cmkDqonS5Q4AyfDH3S_WMFTc8mG_qdKAnLrIKdaPMQnzHhMTXMA_eyIB1ng1lr2TDMMUOBUHjDEZayiKfRxmJ3iX5XDyXA5RARgiG8BHzmAOgOPJbF66KmgYFj-4nqBMV7yrC1xukjxkfrAnEXzlm4G6Hs5BqDVJfd-Kmq4q5LIFyic8ov-7_wWXNbClhUBPXyuGCCgbhVTlox35F9lupKuiUHza0FfOC8EUOBtDf7IeOAiC24LydIo1nPAIRxiYOdhGMhzgSDFby3p3sng5__zFFkx6f3Qbsg4J589MrhYRN3DiT2uPotxT3kEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=M4OFo6Qhe-St6DKx-KwY6jV9Hcnp2jnvC2Tj6wIMQtIxKmWqduKRR6tO-3wjxNc3lC38mjD_CoMQm7uoeNenWzfz6DKHhXDdySigsutc3TT9jQPa-LyqYei8Qki8zi804c7UNnuRpv8RURBbyWKgWkDlglc_FQ7zwQkYQw_Ut1IxZS7WZTSkGVWLe0Qkg0qBLne0DAniNb4FWzQq9xxJ2EajWzC9HDTx3OMG5UW0txfACeq5mBgNrg5D72ytZkh0nrh2Aa0kU0tKcbBop_XXczWPa4iIzgQgZI6A6uIIaUrziURwxP0izIOL5l_B8T83RaTJD-Qth2FbKiHp_R_iugCTw4kxRLWAQ1MybBsVnZ7O54cmkDqonS5Q4AyfDH3S_WMFTc8mG_qdKAnLrIKdaPMQnzHhMTXMA_eyIB1ng1lr2TDMMUOBUHjDEZayiKfRxmJ3iX5XDyXA5RARgiG8BHzmAOgOPJbF66KmgYFj-4nqBMV7yrC1xukjxkfrAnEXzlm4G6Hs5BqDVJfd-Kmq4q5LIFyic8ov-7_wWXNbClhUBPXyuGCCgbhVTlox35F9lupKuiUHza0FfOC8EUOBtDf7IeOAiC24LydIo1nPAIRxiYOdhGMhzgSDFby3p3sng5__zFFkx6f3Qbsg4J589MrhYRN3DiT2uPotxT3kEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=uC69gcNy2WIpIOxKJ-EYi64VMln4_05sKalVf95EDa25nq2pthB7g_pQsF__XYdOlN1Xk22K_-cpo56SV_QbZpATThn6gqZj3hZrBLzxNYNqAr3kf9zapcy6thPepoiRACwWrasyeLontcWBQ5mkzL9szWjQr4FyoRvffDkuXZBKFPZNJGANWOAgscki1ZLnmPxa-fRxDAGHqs1cmjmOxxBxzNZXbDFbQWQGe8cZdOxRFHpJw8fTF2iQPv4XcrsyKLdaBg-1W0g0qsi6qnCQiiYhcBb7H2SFYCnSVeBuqbeT4GtADPGaRiULegzUIao6YsfKzlPZ8pYiy0-T3n48MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=uC69gcNy2WIpIOxKJ-EYi64VMln4_05sKalVf95EDa25nq2pthB7g_pQsF__XYdOlN1Xk22K_-cpo56SV_QbZpATThn6gqZj3hZrBLzxNYNqAr3kf9zapcy6thPepoiRACwWrasyeLontcWBQ5mkzL9szWjQr4FyoRvffDkuXZBKFPZNJGANWOAgscki1ZLnmPxa-fRxDAGHqs1cmjmOxxBxzNZXbDFbQWQGe8cZdOxRFHpJw8fTF2iQPv4XcrsyKLdaBg-1W0g0qsi6qnCQiiYhcBb7H2SFYCnSVeBuqbeT4GtADPGaRiULegzUIao6YsfKzlPZ8pYiy0-T3n48MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=thScbPKHkHYuJwD0t222H6oa3b-F3A09cEr2K8r1uVsE41BLOYQlF7xlhduQxh7JuctD_7a5cutmIbcKydlGWrRif8Dwig5LDMUUBVqXoEkcQetnmXPfqsA9T_gzbrGgX_OIMfr9eNXXsRPwoFJkwLdUU9SVlmcHMYKG57lFWi5WEJnQGuyw2AkL6ygO281qsvDhbgD4ef4Wt15QeI2JX26yGwZFDdr3xosYFejwUJ-yN6fwHhY-Rcoak0Q3AJ4rAEC-At6zOhpRjkRXN6bnkqmATLSC-hmUcieLjDrm4JXNmewnXFbGd_Nbv3AnA6swIs5I8aVYwQ1bkXqVkMZuTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=thScbPKHkHYuJwD0t222H6oa3b-F3A09cEr2K8r1uVsE41BLOYQlF7xlhduQxh7JuctD_7a5cutmIbcKydlGWrRif8Dwig5LDMUUBVqXoEkcQetnmXPfqsA9T_gzbrGgX_OIMfr9eNXXsRPwoFJkwLdUU9SVlmcHMYKG57lFWi5WEJnQGuyw2AkL6ygO281qsvDhbgD4ef4Wt15QeI2JX26yGwZFDdr3xosYFejwUJ-yN6fwHhY-Rcoak0Q3AJ4rAEC-At6zOhpRjkRXN6bnkqmATLSC-hmUcieLjDrm4JXNmewnXFbGd_Nbv3AnA6swIs5I8aVYwQ1bkXqVkMZuTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLuAzD720VxURGlY3VFzpEM6pxJZeElLcaRfkDUXBuoHnD7fT7pG6isqTibMs_5JfOCOBbtzKv-j04vfkpc2Z3C7YAsqG09wLMrJtb44c4f0b6U9ZTu3xd6MGzHtPeJ75tu-7ElfOKpbYwTkGv9XrkdnTs_-fNSK3SyRwDzw-8v7u2yhzKdvXrkPWQMSNmmIxLw-aj9LAHQi5WQxpuiQIwtMEdPeXksm4yhum6hzS332cx7PQb5snLGLYzhb24uqN8nfHZRXQe-YwCLB-AWOHzSdUaoaXTiCuLbY4zmub6aV93vSY49uQ-jsedYGGnwASRGK6wCFN4CQUaEda36scQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=NP91m-G4PHeMGOcr9XeRrovOyBveYrpvxxTTEHESrJXA_cTkTiPVNjDZ-yg6R2tTap2I-8PMHmp_n9g2aDZHRfp-XtdFCT_25K1qtYF8c3lRS9HU7yASGiYC-N-6sIS2KPoazhw6sJPBbZzLkKGsSEV0KoimFzF0ED-O0Xj7zGjizoC7xXnOo_i1c4mtjDrJ9rJ1WmbI2zUwwpRkKYEXhWFYIKtB1-DYy79x47Oas3VJ43f5V7uwuywlSDV4sHGXZON5u3p8ayGB9mwVWsUGBl860bl0pDaHTAysKBD96us2dJ2GTaEDIGeJjCXDaKiwYQ1jZ8zfD_jEEfPSuwGjvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=NP91m-G4PHeMGOcr9XeRrovOyBveYrpvxxTTEHESrJXA_cTkTiPVNjDZ-yg6R2tTap2I-8PMHmp_n9g2aDZHRfp-XtdFCT_25K1qtYF8c3lRS9HU7yASGiYC-N-6sIS2KPoazhw6sJPBbZzLkKGsSEV0KoimFzF0ED-O0Xj7zGjizoC7xXnOo_i1c4mtjDrJ9rJ1WmbI2zUwwpRkKYEXhWFYIKtB1-DYy79x47Oas3VJ43f5V7uwuywlSDV4sHGXZON5u3p8ayGB9mwVWsUGBl860bl0pDaHTAysKBD96us2dJ2GTaEDIGeJjCXDaKiwYQ1jZ8zfD_jEEfPSuwGjvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_LxmY5LiviApriZ_nLHXBSoxBEbFEHsD80AhSDLdVHuWk8-G0p_IBq7hA1O6SeKxswbmGLvXMCXrgO2MiU5_jJQTrd9blGI-7JLMgI6zczQEGSGFrn-3vRhwKUxxOI_1Sr7GGJt7QU8C4IaOC9aJr7nmV5q8EToTV-sn1CJxlOsjCnZ80cS0fiEptYklx3N0VYnFfEM8j2GPsgY9ZU_lydUAXbVsDiUUYiZU2CJq22Y8mFBJ7TtNpyTBnFGGBy9OAUP9Y4xrJqUgMXSc-6YRieN5-EBcGiZ1E7q-B1SHlkzkccxIzTC6AYTirFFMhbKjf_Nj40db6mZOv1vEOzb3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4UhUokxMd2aaQfNUeji97leW3tGEVzcRNDLwgAfNG52c3LnLbAw0bIXxLPKmqopQvIMF4VX9TSP_Xdp_w19NTB5op5g5z3wHACThntKBZ1kYBji1vX_tGlrt02bS3FJXM01VYSbPVWLuufEjf_YAd3w5cjfqRJaAjjUoYGrznxmfUE-2x9m3hW0dP7xFCrz6tzalMCTL8Zhe3_L3N-P74EDvdwUiT9kH4xQz6gWzNhznu31GLD2bNHyuyrQyST477o-qv2i-R41jXJMzedfC-EQeH0p5lbgZM9MFNGOvCe5rEf7SZ3atKvhXuL1q_jz7rQLf0bVRTAGYi9se7IreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=V0IF2yQxB4j53ubyJ743SSxYjNXt-45GFqmTpdQGykEpB5bq_54D8FKMQ0jagWzGKqHBEJKmQulLaMTkRIJpb0RuNQb_wA7wvNHRzBoF8UmicGQeUL02Z2z5C4tT5bQLPtOIfdf5fdgy2BsE4s658nmGVQdmLWyl2v5QA7n7LniHyBSCjV-Y08FSZQvPJ6YXXaNPibNTEtULeOgb67Z7dtB9nQ70tz74KIdUOcFWhq-RcAB-iaHjbLd8wBbHuFh1RXIWwzav9nRu1fjbwiG_AHA4cNto5ImvbwsRT8YV04f62jv4VaHbs3VydnMXpq_jMVIdJkOxkOiaZqOpZYS4tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=V0IF2yQxB4j53ubyJ743SSxYjNXt-45GFqmTpdQGykEpB5bq_54D8FKMQ0jagWzGKqHBEJKmQulLaMTkRIJpb0RuNQb_wA7wvNHRzBoF8UmicGQeUL02Z2z5C4tT5bQLPtOIfdf5fdgy2BsE4s658nmGVQdmLWyl2v5QA7n7LniHyBSCjV-Y08FSZQvPJ6YXXaNPibNTEtULeOgb67Z7dtB9nQ70tz74KIdUOcFWhq-RcAB-iaHjbLd8wBbHuFh1RXIWwzav9nRu1fjbwiG_AHA4cNto5ImvbwsRT8YV04f62jv4VaHbs3VydnMXpq_jMVIdJkOxkOiaZqOpZYS4tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=dLZOL_o7zI9jlCqVcmyoW-c83x0ID3hwbyhaerAhqL9lUrymaj0QNT74wGT0VYDRhbyYirkvGSiz-yn5qgtMsPQRJjhxO0LH8UCophuoDhlnlJRiFMhLUAmUakwVao7AqghIZnPIQSi6xjbp-kWfr5tV651anSejFsGEBk9-_LYhp0JovkqFQtq1EBnJ1dWRxVSDnFnYpqPKwcLoluVoCS3w6-mCOr2nf8rvRMkml55crJBswUP1061PMGTKVt-wpJ27rDMQ84Bxz75nnVA5yMnoguPGJUnBuxMmhOPEpBw70gP-xubJ2GgDmaegsfuIje_YCwhe85Mo1-Vd8RDffQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=dLZOL_o7zI9jlCqVcmyoW-c83x0ID3hwbyhaerAhqL9lUrymaj0QNT74wGT0VYDRhbyYirkvGSiz-yn5qgtMsPQRJjhxO0LH8UCophuoDhlnlJRiFMhLUAmUakwVao7AqghIZnPIQSi6xjbp-kWfr5tV651anSejFsGEBk9-_LYhp0JovkqFQtq1EBnJ1dWRxVSDnFnYpqPKwcLoluVoCS3w6-mCOr2nf8rvRMkml55crJBswUP1061PMGTKVt-wpJ27rDMQ84Bxz75nnVA5yMnoguPGJUnBuxMmhOPEpBw70gP-xubJ2GgDmaegsfuIje_YCwhe85Mo1-Vd8RDffQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=AT_HyopMqx8VFG8S5UTZZ9m_0G_4sOB4HHZZHSm24PW-V-mQYL0hUUgUUaC7UcMRj5QWpdQs2d-ImCRxA6O-mNwuU1xTCloDeXSLHCIoFgUmhDjaPPweNBeq7-c20rwvJe3fxekXoYJNJYKLmOvCZKMOlc739YUJuqCliIGIQ9-_Yk-196Zmm5EFVnaEbx69yRs1G2GogxGX1usAYReqde5cYgECsddbhuo63G3C8ts-319ncZl23kLFgTmWQWea8Ope1WewDW8JC-HetgJAVGkmszNxOsQu1Xc3b1gCfRQozDHLiuq8kxorUpnFXouTSYjpm_GSgnU-vPqT0dziLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=AT_HyopMqx8VFG8S5UTZZ9m_0G_4sOB4HHZZHSm24PW-V-mQYL0hUUgUUaC7UcMRj5QWpdQs2d-ImCRxA6O-mNwuU1xTCloDeXSLHCIoFgUmhDjaPPweNBeq7-c20rwvJe3fxekXoYJNJYKLmOvCZKMOlc739YUJuqCliIGIQ9-_Yk-196Zmm5EFVnaEbx69yRs1G2GogxGX1usAYReqde5cYgECsddbhuo63G3C8ts-319ncZl23kLFgTmWQWea8Ope1WewDW8JC-HetgJAVGkmszNxOsQu1Xc3b1gCfRQozDHLiuq8kxorUpnFXouTSYjpm_GSgnU-vPqT0dziLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3S3mCnAtHnweNeZhJqeS45IQ7m1ufM13dKp9kyC2hzlMrHtPYAgt8dKKyg2ymT9_xrlQtjKbKonQ91vD1CG2RixV_fcCuvOBO5Xrb5-8K5Zas9LxIn_hiQf8JVviwCwv3QjBS7DxypuyeIS-BfvKAZ1H0AlnFaWHA3RBQj4EHxCksAUhXP9NYGH0EaV4mnjSbfKUL31zwJWIrfyEHFJgK2CTX1PQmUMcRrsHhCdz_bMPRDSV1_h3SmVj0VR_0xFH3skQcsAbywitYynOLpiMh1gSAGi2Yh2CKHKhwCdiBpAZnVfirhsEJOQdQHtb91g6b7eSl-zAlf015BYASVN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=KMOZIH3Je0syJ1dZyOvtznJqbjh-TvGpa78aZcg8bTncGSGyUke7-6nWyc9xGkEDjz5gwqjPP7eyLOokN2NDuP9lWUfeU9gdnZanpof5IejJDf6tiPTkOFCHiaZE8aYr9Ok8JtRwC9qwzFEypj2qbvA41bwjV_69_ygp1yeIWk2gWjSHqhd7xJf1Y1X1SIrAYcgnsDB_y8v0EMKNJfoix9LuRiYOkeMD6yWG6azmgdsRda5DaMMWJ8YCORUrqSh73v3pp2gSPf9Phm4a2pUT8arJyfKE0uR22uWNbkLD5p-uFF-HxYjLi8vqSdmPT4tj_x6AQsfRUOnc8RKBgJFqrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=KMOZIH3Je0syJ1dZyOvtznJqbjh-TvGpa78aZcg8bTncGSGyUke7-6nWyc9xGkEDjz5gwqjPP7eyLOokN2NDuP9lWUfeU9gdnZanpof5IejJDf6tiPTkOFCHiaZE8aYr9Ok8JtRwC9qwzFEypj2qbvA41bwjV_69_ygp1yeIWk2gWjSHqhd7xJf1Y1X1SIrAYcgnsDB_y8v0EMKNJfoix9LuRiYOkeMD6yWG6azmgdsRda5DaMMWJ8YCORUrqSh73v3pp2gSPf9Phm4a2pUT8arJyfKE0uR22uWNbkLD5p-uFF-HxYjLi8vqSdmPT4tj_x6AQsfRUOnc8RKBgJFqrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=km1iV0S_XnfBC0fHt2Pst6xek4gGrt3OtuUImtegEwRuWu5dPUrTlFy0Ac9G9DjnrIywuZTmT5QUIiz9pQyhH0rCgVjN6Xzfew8qd_A_X5P0qTCxLGCpf4428sc3SXS2z8_ieDk_9Y703uPg1jmQIwfrIQ1ITadn1nYwZbw383d0RugdvcF3PGfUWP4-jDmaQa2W0K-Nr01uSbG2QrZ2Vs3eCYsXxE0ezvaTOxpPUzwbRF4Fk0n24Ueg0xxz_XkoJOwSYY1--yOJtEzGKzrUpCAH2Mp6Qx4z2bBnceWtKMYM7fKqAE1PubuZRs9uPtjEt5i4Vi5XtRND0sPPyD0DFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=km1iV0S_XnfBC0fHt2Pst6xek4gGrt3OtuUImtegEwRuWu5dPUrTlFy0Ac9G9DjnrIywuZTmT5QUIiz9pQyhH0rCgVjN6Xzfew8qd_A_X5P0qTCxLGCpf4428sc3SXS2z8_ieDk_9Y703uPg1jmQIwfrIQ1ITadn1nYwZbw383d0RugdvcF3PGfUWP4-jDmaQa2W0K-Nr01uSbG2QrZ2Vs3eCYsXxE0ezvaTOxpPUzwbRF4Fk0n24Ueg0xxz_XkoJOwSYY1--yOJtEzGKzrUpCAH2Mp6Qx4z2bBnceWtKMYM7fKqAE1PubuZRs9uPtjEt5i4Vi5XtRND0sPPyD0DFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=hOT3CeZZCZbGktm4uJLSxO8gTy0dlWssJi_XFbm9yYdhPOjnjFb0ZTBylNkLP9OAUIruEsKFs8PwkVcDVxeO01yN38zcR7ZAe2wI7eWUPAclh3NQUAn3VElWBAznycgkcuyyK8ypNUI0u3PH6k9CoorKHuFuo9oz5W7i4VMhc-O9zEbnIgDlB2dY-B30ym0DsFJ8IKV45E8a9n2IsGIBLUMLSIwTZJKVccsjI5b2kErNCTwcY6T1m6nsAE0hVqve6QWH9adSsazdcVo9gFvEViTicMgk-Qmng93zQ-1SD99slRipn7I7Yqj0YnsK2-dL30NDy383ZLFsYL9ehgBALQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=hOT3CeZZCZbGktm4uJLSxO8gTy0dlWssJi_XFbm9yYdhPOjnjFb0ZTBylNkLP9OAUIruEsKFs8PwkVcDVxeO01yN38zcR7ZAe2wI7eWUPAclh3NQUAn3VElWBAznycgkcuyyK8ypNUI0u3PH6k9CoorKHuFuo9oz5W7i4VMhc-O9zEbnIgDlB2dY-B30ym0DsFJ8IKV45E8a9n2IsGIBLUMLSIwTZJKVccsjI5b2kErNCTwcY6T1m6nsAE0hVqve6QWH9adSsazdcVo9gFvEViTicMgk-Qmng93zQ-1SD99slRipn7I7Yqj0YnsK2-dL30NDy383ZLFsYL9ehgBALQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkBpAMhS6mEUW485QXZZXnB0Q4K4ceqWMB74VoibuZJ4jq9Vl22QE3wT-hIhG0WjREyuFnnSkoXa_TnhYbBFE6agH-WURuEX8UYJFsveAiimM0YVZw4p3xeM1VZ88FLQenT6twI4zTdwH2a3syZD-Rh7m8mal7yUPtzLdZJJ7WRCtkab7McJ53TGA02Zz9R4SFPLT7GXNzCYvxJWGbcJaw82O3D5Ydzs7r6sWsOkaK_QH8E2s13JBDPbwjr96WxoZ5MN8jI0lWvuMcWWbB-_fmBj2I3uunJtnDNZT2lXCd9jjwaCBLycsyj9FJRZwP3X8Ml0jjONco_4grTqqRwZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=Fcja-YZecuJ2Sv6VMveho_d7qA1rxn0RvpfdwLIyhfvyuPVsKus320YTUd_JvAhSUr4O_vpWJyx0DmsUGK5vcbix1jR5pnZQ9Qot9yOg7uRoJy5OyldtDuN-8k6tfIsOUcauv1c7IrG8yweQr9f7reHZIh0EwRFwpPkUg7liAz8XoMeDDhZEEW7mWYpJeOZN40DRB2lvM6BpQ9zyh7cYU1iIvG2VIW1S7Tau7-j95gcXOy6X3ZaCVKH4x91HpWWk0NKkylHXdxUEkW06OcGQDYKq7Na72wSXyac9nm5769ypM3xRiYC2oX2HDT9TfWtyoiXAbgf_yuO0I-66-C7KqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=Fcja-YZecuJ2Sv6VMveho_d7qA1rxn0RvpfdwLIyhfvyuPVsKus320YTUd_JvAhSUr4O_vpWJyx0DmsUGK5vcbix1jR5pnZQ9Qot9yOg7uRoJy5OyldtDuN-8k6tfIsOUcauv1c7IrG8yweQr9f7reHZIh0EwRFwpPkUg7liAz8XoMeDDhZEEW7mWYpJeOZN40DRB2lvM6BpQ9zyh7cYU1iIvG2VIW1S7Tau7-j95gcXOy6X3ZaCVKH4x91HpWWk0NKkylHXdxUEkW06OcGQDYKq7Na72wSXyac9nm5769ypM3xRiYC2oX2HDT9TfWtyoiXAbgf_yuO0I-66-C7KqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un-7oZFLIMUuTiV5ew6mgko8A35p0JAe0H4boJbJ2aV8t8OBPwbwLuGfLFmFDg25FhAq8p0YH1PwIk37IicoTjVUiwQpxuc5WBJGIDdwchNaYwqYz1I9z3iZ-hYsmsaK1J9D3U3OMbvKy7G1taefXsGsqfg84qwoZJMBBJbT8Bi88L4Rk_vxzFokQbhHSIskMYo_Og4WwPqqLuP7CNaluRlmlKxyBVn5UFN8g8HVbtKk2x3a0I4uKrU7XzsSXXZRvvei_ciX6EnUHpqyTL203XrVIy3t08VaTSGlvCKGFD8ObAxxi_K9N9gzLAMMqyF2fRNs9ZzxwUjaUG5FM69mmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=rRkuK2E34JjWVdZ8L0FrEfiLhVrOBQYI_s8YW_XNf6hUKAYvc1g5yFr7k9VUqP12JrEfrIe5BfuLhkZEih4n_J-hjNAzrE3o3-sTpGLQuEZRJaRWKh5X55-rpCYB9T32-ataw-JoUncTyq0rgOIY-F_wNkPLwTPV_Byau-XZvhUiKAw6PRVJMo8bo1gc3GUEBrfrfoGD5DP18MxB91BsVDode8-G9oW5oM8W5Zs2bHyqICTZWGFcmIzff1zNIbi5DeAlqsWWSoziDVS3vmZJ3w0Q6VEFVVfvjbX5KXAQfDu6GJk7eaQgQxhek8zD3ndylGAH4O0_djiT_1qhxxPW4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=rRkuK2E34JjWVdZ8L0FrEfiLhVrOBQYI_s8YW_XNf6hUKAYvc1g5yFr7k9VUqP12JrEfrIe5BfuLhkZEih4n_J-hjNAzrE3o3-sTpGLQuEZRJaRWKh5X55-rpCYB9T32-ataw-JoUncTyq0rgOIY-F_wNkPLwTPV_Byau-XZvhUiKAw6PRVJMo8bo1gc3GUEBrfrfoGD5DP18MxB91BsVDode8-G9oW5oM8W5Zs2bHyqICTZWGFcmIzff1zNIbi5DeAlqsWWSoziDVS3vmZJ3w0Q6VEFVVfvjbX5KXAQfDu6GJk7eaQgQxhek8zD3ndylGAH4O0_djiT_1qhxxPW4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKI-aaT5xUJWQXXKvDd5sO7kx2ph_B0uQp2n8gG7vmOg5-UztIxX19nkz1U9mIixBjpSqkqCYtY2zEOJkZ552rI_9qVxWe4naHhv99j9STZnzRnDVlTOpe2X7PWi-QLqXbcVHzzsa7dhSZFhvKN7l9yr_MHE-6gg9gPtZ6aI2n3UBLT-4esyd_GZFvzs35QCSChPqVrYMM1Wbk2QFA_q29ghBTzoiB4xlGGhgYYWv4OLjs6LsGF-ywvs-KbT3BHi_AAP87shSW_oORFTeGMs9T4VmeFo2VQ7lM6ps8-0gSokhn2ckgz_imf8x8n7LhXgQd0b0xXe8cAMtAk_iC2Cgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=d2ShS9buZoGSdPZR2U7EHvOHwsi2Cwjj9mjsuTgkyWot2Ang1KfQ7auYsRsoX2byeUW2Xnx4cerwzVn77GNTFsUgZGxAKP4nEID7S68TD7-gxV1guRrtoBIla4P9ylkFWH5kfHNlFBr36rVAcacPCM7yrea5JpQDqREdH11L1HjAn6SEKrqNVuQb26Mqxyh9IeIbmdEweNuoToFBPZHKuXViPcrKW2ZJ92PTodAOg4B1lMOslM0djZ2-h88u5lM8_wtd-hXry2G1z7TaW2c_RNhHROVqDBwG07siwVG__rmJnQYhpY46im7YuxxGZv8SZ9mtgN4oN6ATfr6sBjlYNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=d2ShS9buZoGSdPZR2U7EHvOHwsi2Cwjj9mjsuTgkyWot2Ang1KfQ7auYsRsoX2byeUW2Xnx4cerwzVn77GNTFsUgZGxAKP4nEID7S68TD7-gxV1guRrtoBIla4P9ylkFWH5kfHNlFBr36rVAcacPCM7yrea5JpQDqREdH11L1HjAn6SEKrqNVuQb26Mqxyh9IeIbmdEweNuoToFBPZHKuXViPcrKW2ZJ92PTodAOg4B1lMOslM0djZ2-h88u5lM8_wtd-hXry2G1z7TaW2c_RNhHROVqDBwG07siwVG__rmJnQYhpY46im7YuxxGZv8SZ9mtgN4oN6ATfr6sBjlYNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q-_lURu-SdQJZRLCUzg5OV2g3f57pXCzvmT33mpx9fSTdpu5ZvYGkTrSvcVSusv_ddttdRnVh5xPXF_JVHCFbUeJ3D8ILJVkWwCa0rd-97QsCpXNGOWBCeTT49scyFxOV9GEHd8xn1dYN1kZhQ7mDzkFDYnWpW2tAWyz9GnGnh1aWN4pPjQCk1m8tltEBNxyQ_3aVnz4XoBtjaSBoeM65lsQKV2GztErWLXR15mVLlFeyW4_acLcFZf4qrVnKpjAWNZoIghHu2z0yUUTnz2UcC3JvdfWeJtWM_AVJX8yYtJIl7JndlZbw4Rl64TWo9gi4zY0h5dxHziCIKQSNO-ekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pByiBElPJ5NDOrxK81v0vyQ0ETTgsvAgQm9fpX0UX7lTO2nbA069aRmp1yZgYsNhK2dJyA9npgmOIqH2WCscnmXTJyicBNGA266ZALF9551nqcxydBFJ8rL8lbB5W75x1lXbkINDFkWwtAnhKEXFKO6InOW3Rx7AUbPyK2-_LDtAnikDmRuv4CD2Dngtf1fH-c68c-eIIRqR-fFwWBndOoBhdSgw1bJU12BjQGLwI94sNsqxNyftJbpLZdAoZRE-vT9eZKXLGihxS31ZrqHhTYOUMgEQJ-8gM5UFeCfhNKTjgEx3nlsTTDZyvcx2eLrOgxFUYFIfPqhPu6JqGNLk-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=httY3HLe2R0DXRsydFFuAthl_GQ6fqmbX-4SA6o0fHbWGBGWZ_SuLYf4K0hVA8AK8PzMDLophWwEauDtQ6Mu1sCRL_GG6QLBuFUY3nEpZCVYIR6IirDonG2tIymZdSfS1xCzFCzi9lIxoNojkyuV85ICDSSaIV5MSS3rQGAEh1yGSmF6UIyxEml3Y6u_6f-kbcfnULHyVHs_wP_RCICqGSo5xxkCOpvU6enB6H3F__bya1L_uKyqSec0ZMw6XoByZOCsRq2-iL5qDEGdjR2G72aw7f2TBVoLdAreviMwEoKATY8WHZG-Ryplq43r_stBMLS-eKZlw5-iZpVwZ8oNxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=httY3HLe2R0DXRsydFFuAthl_GQ6fqmbX-4SA6o0fHbWGBGWZ_SuLYf4K0hVA8AK8PzMDLophWwEauDtQ6Mu1sCRL_GG6QLBuFUY3nEpZCVYIR6IirDonG2tIymZdSfS1xCzFCzi9lIxoNojkyuV85ICDSSaIV5MSS3rQGAEh1yGSmF6UIyxEml3Y6u_6f-kbcfnULHyVHs_wP_RCICqGSo5xxkCOpvU6enB6H3F__bya1L_uKyqSec0ZMw6XoByZOCsRq2-iL5qDEGdjR2G72aw7f2TBVoLdAreviMwEoKATY8WHZG-Ryplq43r_stBMLS-eKZlw5-iZpVwZ8oNxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-9HqM-0gJyRDbbMcllu3OqXpqRAC-2IgEj5O0Mt_JI7LpN-lFBhd2R0jgYbyihVx7dp67xbbHsi9ytVHQtUV90X1-RxCB1LC8Z8NciuJK_DA9jNV6JnzNO3TboVdzeCFxgKRoKGNuC-PetKraU0Foij_t7c3Fh0MGI3upeo3dJO5aMTICOfGgU4nLr7VRIHXHBvBnfwsjPtXZd7e_20GISfMqDmVcWcYa9wUM6A1KqO1sujd0AxEv9OcmOhZDGeLNQ2ir-1gj7vhIzzJux6J7_46Z-KEc_i2xPqFSLiAqqTTyZUxM2R4rAbo-h9VYmIJrEMqqgCz4BELpDwtf93Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGNpDQm_SLduHZqNWsQmPcyjWDu5mVGOmiF24JY_XOxuSXGyLiss0JqOTG6jlooqpac7Ma8sgpJZsf4rUO2cm7aaBmQsTX9TZtjEk3iu8O0ri6bdolgTUIdgwP1pi0Z4aTKIJO-BTwX5SqwRXOkA4WBW5XhTwh8dzAUfSpFIG7HR3odRF9gJDptpIvYRtI3tJv4lV0wvx2kugj3cuk5rp2DpJ3mExv-pXrwzoO2dBM-cCpl8R9suQ-5j7SfnOtyBOgFTx4Q66p_7p9vomfQTazdtNYPNMCTqhpNadKZhi309IwsVrqJ9Vg7q6c56tnBEr1dzExhVc4COe-icy_EhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnVpiGzM21C5VfmtDx9j9nACfr3AOU39wJmBGOL_OCjIrP-wbAMyNHEYNZkvFStHbilwphOcCahippveSyuUqatbUhMrqX0zGCrYMjWHwd-hsxBDxk9zsUfEG7qKXwpjplqLF8-wkX5cbK7Lx8-oJLLaSzavaJPFIJWRPxCG1JE1Q8MomdzcDPsYcLUFM7orNz7IoLRpOkpgPWS4YlX3V0DkJ-xx8H3qYyQKL5Ju6ed1fPLtYRnFD6VAkx1D_kXoi4Pbg0NPbGefo_k2i2Z-NhmxmQNyG7ATw69SbX89SO8SoRSMK1kKXGM3HUcWs8IXfDNDQa_6FTIUVculELOzEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekZlF_YynrIaSUw3ZT0SXmotCxL0qNGTC8Y0aeyn7olPG71ciK-C2fdox0D2CB6GeRMQp_4Ce222pI-HsYGB4K9e5g5fcCRmzJVfmrZQBukiZflRA_NZSseEMU2xFiQxYR-gl1JkECqNLj9y8lrlcXGfuh2AfXr81UHfQzPJYnHY50WNX72-lzyhA5CzxvGmUFftNTpdRyvlJd3kaXVDVwHcAm8AQb06WH7LGElevw7DFebXFlw-f12BZgjMJ_k7IY8U-XT70bt8pRXmy7O_Mh0F5mHNy4TFeiGaS3Y1VBIIdBXdSkNdX-TtBG0lN_CJjCqBTlG0GlCEEZ8dzz1nMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZM-R4g1pMkYsY3iDMfOfYzmU1eQLxTySp3CexY3-lXknYksPOmxrD9Ahp0DLCTA_e9BWFmRWAjJxomZzRodMsJozmIlnCx4mwqg2UcrjZnQ8t1lQF-MjEzHJr8AUSyLBYwz8MKU-eJGfglzPeRM-vjLPUaxWoaxJunR7sPgQS_B8DG8Qv_z45WB_QsTN7fBnQVptWqt02W8nbnvpnnbgCFTQ9Z6gM50OSqQnBaJpb22jusv2eyCHu4h4IZPfPryFrOBjHQkdUsEfvVrqKYMC8jCdZYbevK4V5Bl8__oF-rhOXnimXGulL3sheGoN9OivMd1PYsuU4eFC5Vuf6RAQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=BVSTW0pN9ViN3O0PDn8adbs0h4FkFfB1oIew4fCqwOrT4T9SQ8tVlDW9gNuInC9Sd8wCtCDT0BfP_GKNhhIdAO2vjCHYbLwWQB0kEyflUOs1cuNbCbGz0SPKG7AExbCgnknJTw3vYMI7VwRj0Ce5dup5YN5s711qJP5cfUAh3Rj8Ew_0uhDi09069DXXBTMdEWxaQN0_OAY08JDjz04pVO4X4G-jr85w55Y3oqjNVYzC2AokactkOCY1_mtImk00O_SqArFQB3xmR1ckyuAzu45bxVSOdlYuGfXRa7iVNBixVTs67IFIdPRsrkeCHQxffbAC991jdF6FIpUuX1ENuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=BVSTW0pN9ViN3O0PDn8adbs0h4FkFfB1oIew4fCqwOrT4T9SQ8tVlDW9gNuInC9Sd8wCtCDT0BfP_GKNhhIdAO2vjCHYbLwWQB0kEyflUOs1cuNbCbGz0SPKG7AExbCgnknJTw3vYMI7VwRj0Ce5dup5YN5s711qJP5cfUAh3Rj8Ew_0uhDi09069DXXBTMdEWxaQN0_OAY08JDjz04pVO4X4G-jr85w55Y3oqjNVYzC2AokactkOCY1_mtImk00O_SqArFQB3xmR1ckyuAzu45bxVSOdlYuGfXRa7iVNBixVTs67IFIdPRsrkeCHQxffbAC991jdF6FIpUuX1ENuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=J73Xcsq6MPbmBemAoStYQVrboHnAdhDTr-84Ghw3Nzke18H_ysitie4zG24D41PYvx_TpNifXsK25-4d5DvkQrEDK_WUNFFWoprlc50H51APK-VZ1SNAVxdUrpJD40b-tg9L9z5Ba_BDUAhsC5kXjdw_Wu-JZxhLb-2-fchuzu5Aiz1c0SgGuCswOPkguByCKO8EKir8SDp-wDrDcDA93eW3WVgPxvS-N-JEO9GB9r10BQ5m5-SyNLzIad5y4LAQ7_8nQbUfFMRMV_edZ-dNF3lXd4cjY2u1LGCEwyNqmuan9lW1vFat9djSt8Vea_-4HjMr07ZJGHooMmNYaFkX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=J73Xcsq6MPbmBemAoStYQVrboHnAdhDTr-84Ghw3Nzke18H_ysitie4zG24D41PYvx_TpNifXsK25-4d5DvkQrEDK_WUNFFWoprlc50H51APK-VZ1SNAVxdUrpJD40b-tg9L9z5Ba_BDUAhsC5kXjdw_Wu-JZxhLb-2-fchuzu5Aiz1c0SgGuCswOPkguByCKO8EKir8SDp-wDrDcDA93eW3WVgPxvS-N-JEO9GB9r10BQ5m5-SyNLzIad5y4LAQ7_8nQbUfFMRMV_edZ-dNF3lXd4cjY2u1LGCEwyNqmuan9lW1vFat9djSt8Vea_-4HjMr07ZJGHooMmNYaFkX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=Ny7bxuw1PO3sgb1UmHO0YvnjDJTFufeN956B7UkxKp_xc93AZtecKobcOb1EP47qUgVdBaggudKy_PsO0gvquOgfLF6FQ-ad3o6k0-ADI-YFIin2HiWkpOTCKGuJdK1BCcd0qFTQ4MjGw54kTGfyuhnIRSY6Ih68eHXbgEp0xhxgnJIK0FlY4cn4HjCSc0UlKK93ErvixBXFgKNkQkha950CKnZ53T8WepONuRv6c9gagCU3dw33dRvumGcdzqphj5-2MbkVegn0m3dU-kNIPc-V3zDk_l0SedIMhtcBHDybuzQDaN79_g1Rfi5Zy5pS79JYHN6H4bl2k3zGFy7q9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=Ny7bxuw1PO3sgb1UmHO0YvnjDJTFufeN956B7UkxKp_xc93AZtecKobcOb1EP47qUgVdBaggudKy_PsO0gvquOgfLF6FQ-ad3o6k0-ADI-YFIin2HiWkpOTCKGuJdK1BCcd0qFTQ4MjGw54kTGfyuhnIRSY6Ih68eHXbgEp0xhxgnJIK0FlY4cn4HjCSc0UlKK93ErvixBXFgKNkQkha950CKnZ53T8WepONuRv6c9gagCU3dw33dRvumGcdzqphj5-2MbkVegn0m3dU-kNIPc-V3zDk_l0SedIMhtcBHDybuzQDaN79_g1Rfi5Zy5pS79JYHN6H4bl2k3zGFy7q9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=q-BQXhGmcf-2q-58NrGtca3mb-MFMkAec73NhyyXlNnWGipoR-hXY2kNTIjb4wugYgNO47i7mXxGRERXr5e8srFEg06xj21scmdvPHpfKdFIlQWDM6QbLk1_4gDAXJ6nWVsNGTyAJBn3EyP0xvusFpbOjSTGgf8tkSXjlhqJx8QDbNZJxQ3r8mcsnVYrmiT3xcdDKmbFTTUaSDfB56dYm2d6obIBhNjkaG5ynxVK7qLB-BedpMtrqZzsjeq1V6OSCXjn4tJhnw-Tf96qBmFBiH9GXZRXARcESxC9Rlw-5D5xpI6547rDlne3yArtz25yRz6jNgTSDaKuOsIzQT_mhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=q-BQXhGmcf-2q-58NrGtca3mb-MFMkAec73NhyyXlNnWGipoR-hXY2kNTIjb4wugYgNO47i7mXxGRERXr5e8srFEg06xj21scmdvPHpfKdFIlQWDM6QbLk1_4gDAXJ6nWVsNGTyAJBn3EyP0xvusFpbOjSTGgf8tkSXjlhqJx8QDbNZJxQ3r8mcsnVYrmiT3xcdDKmbFTTUaSDfB56dYm2d6obIBhNjkaG5ynxVK7qLB-BedpMtrqZzsjeq1V6OSCXjn4tJhnw-Tf96qBmFBiH9GXZRXARcESxC9Rlw-5D5xpI6547rDlne3yArtz25yRz6jNgTSDaKuOsIzQT_mhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYk4g-2sH2VQSMGIn_wR2IiNSQqajsOQHA5n8wXWuNlrOpgcgyyTU7eD8Ltbwmo6jyi0VhwwvmrQToOybUTu6kjpE9JK3BfTLcVW7yAsNFE4r3mAEaHaAI6cbXJKgz_nKa3GPpd41YJHu8SPS6Vdk25cJLHTOaMJOqT2RKtHy-83vfRRTzpyReiXHx4N330-IBKQNZUUjZaMgVHhMH25t4sAEEaoVzRSKtUozj1APEYG6sKVryxSkt9NyfQyYX5x6k_CNGvKBL-e2LSfmPkBup_BiZOpsm1RJTmY_ZzdKsTiwBwznVmEtwyUestsv2HBtMJRdMDsD21SdVEBRRLU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFF4Q_uaC9KGyKgYeR0lhl0vF9HZdlHBg9JJnuaHpGOZc2ZHU2mZGXPlbnk7au2_WaRDxWsIrIb9w7h7HrlU76sZvN-NVDC4u-cWxhfl0sZpEbVqWZnLtFSnmQkWkce1p8egXK67auT6w9UvF-l0c8OPom-XVNYlYvXjt8B5piyB45bM5AKZZCBM55dGiBL4kRm-p_fkPoSmhbL6GGnJUwuSwCfxwTKzr174lYDF_0F4eaTi51ZJNMRZIJoZCOvU8OLnwoy9ajBYajpfuKL8H3ZGTJCVvqe_up_EINCBMEEdw-LKGa_W9oBuaaeio9h7bQoy1PVKywucJFyVMLbv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=BqlA14WD_P8YTTySU496yKTPJMbvMFMXJVGodApn266hbRdwnsQJC8O3qc4e_UzACUwQ9vU7oVkrH5JN8gzpuE2hCSj3LCD9456-b1SdrMPdeibsSURPyxaZINms3QbzOPEfoYYP-XBhaT1o40kIbCThMvP5JB6SF9DMHDOxv1LuPndjX4zirc1iZomYTz-j-dyl4GbMYhCLHUalVyRsfT5BTVcZuQQKCDroEFwuDvsmyx0YBRfJZ-LMUIdLzFiV2kf3vo6SgEpXthltXcBCxqp3oZiqQuwoKlTuKJOM4CmlSoZnEtP9A0MRNhCqTCpkW0as_iJ4yJBSHobvAa9osg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=BqlA14WD_P8YTTySU496yKTPJMbvMFMXJVGodApn266hbRdwnsQJC8O3qc4e_UzACUwQ9vU7oVkrH5JN8gzpuE2hCSj3LCD9456-b1SdrMPdeibsSURPyxaZINms3QbzOPEfoYYP-XBhaT1o40kIbCThMvP5JB6SF9DMHDOxv1LuPndjX4zirc1iZomYTz-j-dyl4GbMYhCLHUalVyRsfT5BTVcZuQQKCDroEFwuDvsmyx0YBRfJZ-LMUIdLzFiV2kf3vo6SgEpXthltXcBCxqp3oZiqQuwoKlTuKJOM4CmlSoZnEtP9A0MRNhCqTCpkW0as_iJ4yJBSHobvAa9osg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giY0M2Pv9edGz7Zpu-Cxee7n9WYkPDqJwNLFPcUmMVY7gcfWiiMJGygshlfgNYA8FkDzti5MeR3VU797KvQV7tEFFyu3ALLAwF5wJoAs8Gv9pgRyRLQ73G20Nty3SpXYEatp-VczvsOdfcXfhwaH9PL4sNxvf8ABSJQXB6ShDz_2tl6fzXXhlZgOPhw3EdHILUEUlnrFg0VcK6LU2yopufv95iE7-Dj5cETFkKWblgmZWNDE8E1anexh4G6tC5aAhjHRUrTPH6NeXdeNTraSGjk_MJiOByJbRcgH91vz-4lz_yITifD9MNIVarQVitXfyDlFGIx8e7e6ayXGC4Bimw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=GAEhP4QbzbDKl_XO02gxYXfJarecGUTnjf_VT_nWXzi0B8Tf5thNJujH3v3ycKXBRy48MILXyOacyJw8_Ox6h-r7Dxd_eitk_lhurGXvLh-QAOQS1V6dZn3Zki4Cu8bmW1Teu-SLB9QvZr2oBspRG1Pzyj9sz3G4KgtzMgXV0T6l8FsmK0ExJIQDx86WB5ShuGmQQrgWVvF1XlaoHp53bH6J9hJvPGJUu3onCgHjKyZiT-o0FH7YahFAzo2i37MtmIWZLNL20A9AEZ5q3oAzGRJj5m6PDQZZKer4ULQ2fCjDSW8JajP88RESbMKvCwmGiS6V3a6n-3tlL5SJ4VlGCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=GAEhP4QbzbDKl_XO02gxYXfJarecGUTnjf_VT_nWXzi0B8Tf5thNJujH3v3ycKXBRy48MILXyOacyJw8_Ox6h-r7Dxd_eitk_lhurGXvLh-QAOQS1V6dZn3Zki4Cu8bmW1Teu-SLB9QvZr2oBspRG1Pzyj9sz3G4KgtzMgXV0T6l8FsmK0ExJIQDx86WB5ShuGmQQrgWVvF1XlaoHp53bH6J9hJvPGJUu3onCgHjKyZiT-o0FH7YahFAzo2i37MtmIWZLNL20A9AEZ5q3oAzGRJj5m6PDQZZKer4ULQ2fCjDSW8JajP88RESbMKvCwmGiS6V3a6n-3tlL5SJ4VlGCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuTcLH2B1k_cORD6HpHLjJ_AELcG_LoLmPCd8elSJ6hyO0OAzYdC5bPQfgQTi7mdFRXK802ZlSU_xSpSClfP5M9sw6FLl9JJGmtjgHOYXR7IIlnfvtw7tPtBKqiAy_bz4Go4Vg7nGukbgw6Aysx_q6zNunZMOls71ONPOXNIBcn0vrBEnjcE6THGUB24zw88g5Fv1wxm4tO6PPbYGZlow0zugOngmpoUVO27uMUjprX5MsXgLug1FqV_5gId0gUK62eSGhz6YXvxAsrKhnVaoxGAzUAkdgWhfXh4CRJA6R5kJ6Q5hKfi0E4jxrsBL_ZwWa7Eb959X0c0-TJkPZr5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gphYOdyqnG3cNdtvQjBNY7mZs1pmfY50oA57XDEv2Iow2UrkSktfqqbTB52UFwunCQi-LN0ZYXwxqpmoPCiI6gtCIlZGqYs5d4rytpae4BXlZAyXA3b0iMJt7I7egY2Sw9WpR7K_6CMkQvXoyQwFtv5RBWHeKwapBU0MqhPiKJxDZEnwSGA9krtMYL4qRO3dQLboajIGkwdtPUJ9dYwdxteYZbW3pzutSUHw9XtVuVHtgCTPO8n_7p2dVwSEmUuX1fzU4fExVvy8JAR2ZsLiPrwb49VdRiFYsVpHStRDkAtohwHXrQRHGGp5tE-N-j4CZOXrsTYB0rc2OkNcqBHQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
