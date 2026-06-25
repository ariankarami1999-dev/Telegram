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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 14:05:40</div>
<hr>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=pYjXjK5qPQuNnyviDJNPDuPH7_tvnHJfCnXr6i72Olh1h2ithz0rosXibIAwQX-JuUiKXj_YF8czaSXeRuH_baKte4RYxbdsgu6cbaL6Tg4Vef_dkPRYCV3fJqf2ASN7-lIgg7iJc1Z6-woBGStn2bXWIUkx67atfd8BNAhrWmggaDbs8XSYBF-CUQuGn116qu_MQhfcCuK3NFh0DO2saiWLvqD7-ugHLZ-_S-TASxXPmixhnOys0nVzJstdkFrUYIWhPoVWBkkZGkyaLBDzMe8VizwrhvSGwG1rRXCKHlj2QVZWVd4Qu_zuVybK4b7MhGhEEV8JTnJgKUpyztQFvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=pYjXjK5qPQuNnyviDJNPDuPH7_tvnHJfCnXr6i72Olh1h2ithz0rosXibIAwQX-JuUiKXj_YF8czaSXeRuH_baKte4RYxbdsgu6cbaL6Tg4Vef_dkPRYCV3fJqf2ASN7-lIgg7iJc1Z6-woBGStn2bXWIUkx67atfd8BNAhrWmggaDbs8XSYBF-CUQuGn116qu_MQhfcCuK3NFh0DO2saiWLvqD7-ugHLZ-_S-TASxXPmixhnOys0nVzJstdkFrUYIWhPoVWBkkZGkyaLBDzMe8VizwrhvSGwG1rRXCKHlj2QVZWVd4Qu_zuVybK4b7MhGhEEV8JTnJgKUpyztQFvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTwd1PZgtxyk9gR0BeLXT4HH9NJBSEv-GoWmPocklLko1kaf4l4DSkY9gdhkW4GEPAsm579GvpZ9_dMnFvPFrVpeK1iJRhpa8vifE17BpLQfhr00rnK0v9UOaUoQx0Zlns4m_NNYZexTlSsx5rUDY8aQqpxlf5sA4oFXATASdDNmK2Y98zhpHZzBw4lp5UK___g91VDmTjZrzpCws2F7aCKct5QozVKtpMYQioNYpZ6C-NTK39I3tKuP4DiY7UNvire5mXpaJMGhznMxllPphfuXZt9XMFn50O2x4KQy8iMYXDSodh7H1RsaW6fBRE8fReRavSpm6NEm0AAXNKTUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UXWRm7lYHpYCw1qyAzHoH9RpGZg0HjFgdm8Q1kds-ms3j-nRfwtgDZXcfonmTD7g6owXxChLzeQwDUA59NS_vE-mxipovnL2q6pNqPjqjkTiFX6GLK0-OczdSTp8YLYn1dtMC_ZKH8KbE6tzQUkPhKP_Vs_i5dipAu5elZkl7_tl3sI8ixpk4IUz_FiowCHCC5ynH1vflJ1HToS-R8bDSfMXuBY_TxmRERE00Lq-_NipJVwv_H720p27mV8vqC0v17o6dDEUxD5wTkxtWFF0Ccna0UgMsYBSwss8KjxzJwSqqEcm8mlPeGFzeuQjS2Mvo7nCXanZ6JwtBlJCPC7h0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UXWRm7lYHpYCw1qyAzHoH9RpGZg0HjFgdm8Q1kds-ms3j-nRfwtgDZXcfonmTD7g6owXxChLzeQwDUA59NS_vE-mxipovnL2q6pNqPjqjkTiFX6GLK0-OczdSTp8YLYn1dtMC_ZKH8KbE6tzQUkPhKP_Vs_i5dipAu5elZkl7_tl3sI8ixpk4IUz_FiowCHCC5ynH1vflJ1HToS-R8bDSfMXuBY_TxmRERE00Lq-_NipJVwv_H720p27mV8vqC0v17o6dDEUxD5wTkxtWFF0Ccna0UgMsYBSwss8KjxzJwSqqEcm8mlPeGFzeuQjS2Mvo7nCXanZ6JwtBlJCPC7h0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-CMETcUc6r3II7t4-ot8tUzi7rgzXrmB5n_IBtuOJi7h_gmadMcLHlPTxgBgb825hnhkGL1gqKBJdSY8m9MSR3bZwNQPbYUXSra5B17mlc3A2DO5_WxmQO6lukzYfK4yxIICB4GIZO3sikuyD1vIuO93_5Ik-kHl3pkOD14jqNyvjEMJIQdH0pw_FEdu7bmOuF5kYoSPaN2iFUp8OvFdaP86bEXN7Xj2gQQppxAhRTxtXJNahBHbQ8Rp0ozC3ClRbLhmNe8eNEKM4kZFjOWBZNPjSVUq1deOGeyWXq4v1t64Ft2ofTCh6ANPNZxTKEbcaIkzEDpbRFbnaw4-e2ktQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfXv39ugSjEHvm5gEjzri-MRjsw55eFIY6fHEtU1o1sHSBmz0vrukcl8UyGAiY2rX-m1DJH9kBHqtDCmMflMXK5kdE5-HigEG6F_SY4RxOrJDpo6bZ45q2VhftAkY-PwTaO6Vp2h0LIVkUULM6Fb4y2nCJ4Rrp1Z0gXw4Jj6EELuIPCD-Tko0jpH_AmYheawOxt6g9O2WV5lMOw2hmDdiwWmLmNyI37SH3llvQkNDiIe4JijY8eBsJdefSgoxzXtTmrHL_nj_joClfuyDQJIPbGfZ6IaTAV7WDcQd5H2FlWSg7Q8C6ObD6hywuFXzpPTH7OeCekzdH-Cx58ectm2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbyTtCMPT-IgwUAZUZLTSBccqB8S8jZ5C3Bzwei1BUAsr6XToSaptBGg98dz-VlL3VaWnTj5c9PFVjRexJW6mX6r5vtxmAkiPS9H0r9F8kdVkK5gLfG0OR2m3xYPz5CXRvJ4EyjTfMApF_ogmSV1XTYYZu5vzAbx3Jy6urzbS2fqy2m3_q5kyHqNmBuTxWeRqk8LXIUgrlfV5aPk-3BPrKMb3KpnMBbYq-fDmO-pekDH1kp2DeDbjK2pUaqzIRl5FJgy9wcEbYMvcn2hJOWI8-hx5DhWUeyPs3KPkXCHCRce_ugtH6rMvH-GNwlSGVdWyar5WBJmnlj9YbsvYA3isw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=bfHtfbFkcZhEeNXQDX90Dj1WTs_l5DBjrTFbANLd0RfNw2qT1pJv5s7qk5RR0Qb2o6ua5uoYZuzFBBBLeZhjcYBbuyufIweb4RrTSRRGa3CjATpEHUgCTpvjDtPwVd3ZQ3zRKwT9m9_h28_HnRKTRQWORjwqYEsigmACNsrNCxsbbUfntuhULMTTZhduatEyRr9z4PwkElWasbNuzTigIKVK1Q79cnvRSnak1kZ9UfFumGfsZecxcd2OvkBAqowAyh2jmmZKz-02Vtf0pxDu4mb0J7LV8cwEBgsMxTu_-98kPfUC8AOUDwzhhYC51Va9GN_IsEngqdVBRtVue35HIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=bfHtfbFkcZhEeNXQDX90Dj1WTs_l5DBjrTFbANLd0RfNw2qT1pJv5s7qk5RR0Qb2o6ua5uoYZuzFBBBLeZhjcYBbuyufIweb4RrTSRRGa3CjATpEHUgCTpvjDtPwVd3ZQ3zRKwT9m9_h28_HnRKTRQWORjwqYEsigmACNsrNCxsbbUfntuhULMTTZhduatEyRr9z4PwkElWasbNuzTigIKVK1Q79cnvRSnak1kZ9UfFumGfsZecxcd2OvkBAqowAyh2jmmZKz-02Vtf0pxDu4mb0J7LV8cwEBgsMxTu_-98kPfUC8AOUDwzhhYC51Va9GN_IsEngqdVBRtVue35HIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs2PsAHxgsIzSuTUkxuvBA3rNX2fpAQhlOfIKqHxbNkSEHa-KTOHl3CAMNwEdwhU0e65CnJVeGpLCAaC2bL9u7wrFS5jjAWdc2UK1BvQ1SeQg_CqR54w6LCFCHvVhkre1okm3JV-7ld_Y3uIgsRmYhE650_eUuwS9uy0ypAavWPPQ9B2uDwVaHvneBezH-N3E9LothbhpAdNetPharzqmgQ9mXuZTM2ydOSi6ZkcTZ0pEYZSd_8ssCboVWp_3d39v4iFRwcvSVMJj7DRPrsDHWQUhAiY2FqGz4lAEo_c66Gabo04dy_aVVt0t9D_EfhGqGpSlX64Enjb299tJNcFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR-cqyRh_cCZkHhGS97QlBz2tGbpbRBqyJ8glo0FWImVX8Q4F91UZL5prrRymYW4VvzT6Kly_dDPfvg3ilax0KEo6xsPly5LNkIULqpLddIyZmFcSGP-lhx0wqjzkoyz81aeCYdjoXF7h7ZFJZ7eWZhRDqN7--QRWx08FuuGQj6QDHPXXziFcsFm2XQ9h3rwLc0dVnAHVjrzJdBHaH6TKtXyf5_f5B6JPw3HQcEy3UzdVgF46q3iN7UrCgkFgsP3uAOPrsB2QQcFITU8j_INMUBtLPMOYFwBa-D3N9NtJIBgjVWragIDIxzKLi_SGp8OAnf__ZD90DO1Da1ZPmq3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r65_cUMVECRh1d_kX9m8b7VQ0FZmDfcKjK5LsxSJDbvxHVp5xnYLKbeowLxfnN1TP8Im_mqoLpJkqLYkiQVBqM3GLdgd4iJJ-NJDgn0ZsSdo2fsakhBlvVnfI862S-zi1kWLoGe-xCe0YhQLYdCoes_jWGYN8dvH3lV3PhVnD2d3-vmdFEVO1Qjg8eGhBmeew8YDn2JCZ2m88iTbZLu2zI87dlLKDFjSdfoB-B00V3poqMiinoXrZ9ej_lJaaMkHyCNpihs3nT_PfmFbiyHpxISRFAdpcxHFXmAdXp0ULkmpgwd_kG1eNBm2gu3ADaJW0KDnI9h3O4PyiZLz8k4Ymg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCENO7HAwxe5xWLgQqaGtApjF5C5lSXuTD6BcEOBtv0jNtqL3ZFZD6gTn2NtmIlIeGqR2Tjycio2kLkyS7CnZtVu7sVt13hoMPRntN5l64tUiKCw9LtowPte8fEjjD6sin6S5nGgUYufdBb2bbXR2O-iFfO-1qBZ5v22Nc2AAhDFLjrY8-tOOPPbGKE0Ma3YVmOsvk9_K3UjsNOU14Q5AFPIkr6g0Xz1JU4iKHtU5W_Y4qCA1RUn6LONpIrY-wNOozCupy0cB0iV0bFjKaSX1T_OxvxSeWxjoSM4L8yTHfdFT1KlMkZinE6kOwbVjKJKoBc51OSxgcH5pLoaosCcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=VjXJk4uaU5PZiYyb-2hX6E14DmQcAsOS5yJREG9d1l7pGF6K3v9IR5b8yuwfC0dwZp9m5WZEsuKyjLikQqjUtd89x-_2vxT9SYJXIRXr897hZEWzzMUpBN1VPq1ehBCgupKti2efT7YsZWEBndZ41KI-6xIgnqtQW4oNTfZ0igk0cavnlQ8jvhjx5owCJRZOt6nwVxjJVLzXguCnlAVIM3bTaw_IO67OPf7pyKc69sAPcUjnaeZJ_qwiz2QVjWWCcdPxE4PSXG8a4wU9_oh4zXPx_zWjIXSuV3D54n6eynhlurRfl-5rqjgFPXz89CIwN9wIRWugucsfBkXMyB3xzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=VjXJk4uaU5PZiYyb-2hX6E14DmQcAsOS5yJREG9d1l7pGF6K3v9IR5b8yuwfC0dwZp9m5WZEsuKyjLikQqjUtd89x-_2vxT9SYJXIRXr897hZEWzzMUpBN1VPq1ehBCgupKti2efT7YsZWEBndZ41KI-6xIgnqtQW4oNTfZ0igk0cavnlQ8jvhjx5owCJRZOt6nwVxjJVLzXguCnlAVIM3bTaw_IO67OPf7pyKc69sAPcUjnaeZJ_qwiz2QVjWWCcdPxE4PSXG8a4wU9_oh4zXPx_zWjIXSuV3D54n6eynhlurRfl-5rqjgFPXz89CIwN9wIRWugucsfBkXMyB3xzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhuH9jy1GAG5gCRGrkEnv3OEubwZtG36MQjdzt7iY-WIhKC5J33pnK6I0zDrlj_rsO-01QqWsY0-rYxSXZDqHCcor2GJoxrAlS65-P9wVQYWYORiSxbbEgYZNzSqzB_Z5-gf9iqz6D9bOtMB2cv9oIAUw2zCl9yzzdghq5NnR2nmRMcOsVnNWXiswul0om64s6t0qb4RQ1rqHQWoP-MDQXNln7TyK4YVcBJD2JQv0LwCN5yvXZOBbJVgIEvZso_-8MmttBrS8cCtwJsBdCM40Xftu7t5Sw_SninOFR7ENxlyGWS_Lw_nkeC8LZoFFkmwxECm7mbunxUWn7dMCwrqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwGnzBgXiH9O_5BWO8qk-lac7aaI69XcEWMPogniiKGZYeQsKRSpMkeT_PxAkfSpwP2OH7PdLGlRy3WfdGXmakFDBOojoNqpah0xH0CNWKZ82kLvqE5CWjHS4K-SFXhCbRX1taREnGLUEpcEJ_0CQYAU8bdTxKobxr3aVynlk3yIJI_eN5Uv1yLQwshNfZCol2QfFrqjDz_F5ppGJP2Ea3mjA-TfoUwGUKPv7PP9f5_tlXYbfjdVuM4nwXhMwFpaPuIY_-BL1xkiAQvpcTr0Bd6QTI0TAlfW5xB7L6ljs98yHoHbYKdgPerMAAtU3kqvRJX8QLIx5xaNfLPpp6-7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pg1Yfv3LxUZngYV93RAyETgKEa8otmxcVFqdSl1BURUwFplNXNoN-AFM0o6xEXk2jczLZgITPgugOnig-D8r0LhI6YUMkk4GProQCoccWn11DbX517UyeZY1xlTMMLQ4eL0plQJ53x6mQJ_agxK_Fbrwvt5b0Kb61EI1Tc8v9RZ7sHM6Zd8gaFxBvc_oHH1OlK9LWgm7jO9TnHvHTguMNTZ6a7yFXUu83JrC3-TLfXXhRBICy5ajDhthwh_lcKwIAgSSRbuUN7sIkAfd3aLwtZMf9Eb4Ui8YadnTZfDqDFH4j0b52-b9xoc3SJnWbj7xBucUtoayGuJ0q6MHoXyeng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=W7NW1yLPINlOHP-zwDageibHivGYBED3IMpWypcXw9-EPoo-hoxFDCldbIBRI4lQc635MwRCmhCJ4SnbSjI6mY5eCXaKTPNCmDgtlSG1oIMzB82b_h7Mp9KHfUEK6vbBeOh1QJbhMLyX2OE9B0_FqXsWEe7EEbhcAytJZOjOUSoao-Rbi80fP3WIiSPQ6muEEGuphOegii2gSsbq2vKuNRhNKzGDYJnGaivl-P4SIAZ7_dr41zwH6sDaGQh90PZyUGV7tf1rBbWs5CcROZ-yMI1a8tsXYh87ECS9t0M6DSRtJRjYq1MpCYyjMF7tKPicZSKG6FX7hTJ8kRMwdqHUUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=W7NW1yLPINlOHP-zwDageibHivGYBED3IMpWypcXw9-EPoo-hoxFDCldbIBRI4lQc635MwRCmhCJ4SnbSjI6mY5eCXaKTPNCmDgtlSG1oIMzB82b_h7Mp9KHfUEK6vbBeOh1QJbhMLyX2OE9B0_FqXsWEe7EEbhcAytJZOjOUSoao-Rbi80fP3WIiSPQ6muEEGuphOegii2gSsbq2vKuNRhNKzGDYJnGaivl-P4SIAZ7_dr41zwH6sDaGQh90PZyUGV7tf1rBbWs5CcROZ-yMI1a8tsXYh87ECS9t0M6DSRtJRjYq1MpCYyjMF7tKPicZSKG6FX7hTJ8kRMwdqHUUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=UwqRRyJC6FZkqup-dvfZyEHt9ujYCZ4l2qt63CYYo3640-ZfALLcfLgyMDgiYo-m1yEyY2qqDsPyNnHRQc2p-eQ6v6qpIMPJOrso2rStmWXfR_-tLqVcsUdUHyl-mjhZANKTnlmxcmz2tjbZOuS9u-2Xe0R_MK3M7g40OKtzpuo0kCIAiV-0IE8v7NXFEbHapajXd20SDlo9Y1NtJ-OlAjTMLNwVroAPF6z4di_OnwmtezHktytOV_MeJUqJM7Tr7e53JmevyNS_h6nS2O-MX3gA8O1_oH-S0IQvNAGE1-T2n2-7YYrty0XLEZpVtODGxj72ialsMcwDa_aDr2RhDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=UwqRRyJC6FZkqup-dvfZyEHt9ujYCZ4l2qt63CYYo3640-ZfALLcfLgyMDgiYo-m1yEyY2qqDsPyNnHRQc2p-eQ6v6qpIMPJOrso2rStmWXfR_-tLqVcsUdUHyl-mjhZANKTnlmxcmz2tjbZOuS9u-2Xe0R_MK3M7g40OKtzpuo0kCIAiV-0IE8v7NXFEbHapajXd20SDlo9Y1NtJ-OlAjTMLNwVroAPF6z4di_OnwmtezHktytOV_MeJUqJM7Tr7e53JmevyNS_h6nS2O-MX3gA8O1_oH-S0IQvNAGE1-T2n2-7YYrty0XLEZpVtODGxj72ialsMcwDa_aDr2RhDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=EIDUG9LQ4wSJlBY8gwmwAu4gY3-H-MR9iAu7mh3c0epjT7rhZ1qWf4dAtqw59yZYCdKE43_WJEiQX2FEeHUc2oaiVuc3uppceq7ZHqR2QsBq4yOptIAHkf_GJcNI-ntqMxF2yl5xfiYsie18KtaOJD582iYX7FdLr1uwdoOikXwxGlUNr2eLTa0ioldr-xdFCB2UrQgl7DoX_5Ds3zi2hDyFhhYXjoe9HxnFLEi9PmBHDyUFILAkD7-TCsdleTFY3zHvV6HFP2p749kfEflFStMX3MeAKKTmeKNjXXXhb3_hklanylQzfTefaEqgYLb6NNT2a9K4D5BkbbgFekRscg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=EIDUG9LQ4wSJlBY8gwmwAu4gY3-H-MR9iAu7mh3c0epjT7rhZ1qWf4dAtqw59yZYCdKE43_WJEiQX2FEeHUc2oaiVuc3uppceq7ZHqR2QsBq4yOptIAHkf_GJcNI-ntqMxF2yl5xfiYsie18KtaOJD582iYX7FdLr1uwdoOikXwxGlUNr2eLTa0ioldr-xdFCB2UrQgl7DoX_5Ds3zi2hDyFhhYXjoe9HxnFLEi9PmBHDyUFILAkD7-TCsdleTFY3zHvV6HFP2p749kfEflFStMX3MeAKKTmeKNjXXXhb3_hklanylQzfTefaEqgYLb6NNT2a9K4D5BkbbgFekRscg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIc8ikelVw8guxVQ2WN44QQIurSpBgTjrfOjkVHZbforj3J18kx8ZYTk0ar2adBJu5nsR88aYphXxnzhYHXio4JC4lA90wPUl3wrHzrW9sUXvIoj5BdHgCxlLft6s0j-qFrhBPppKNdN7IkhdJTXndflvDjfaLCnuCKZZjueeZcpyNuGIEvIuXK8qK-EIlB207eordtV6rtg2fkZb4cJ3eYB-2Lc2Hc9WG0N85zanF_CEIMdWEzyiqx7jxuAg4AVSF9iRs0DA9QV1ZHcjoHF2YiNuTiQDAEHkdS2Q4eZCEvxF08tfMB8VCnP0aTJC6U_mq3gPXal58A4hSj4P7DPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiGTGvXu_kvLXy_FYu20TDf4qL-p-ioLGq36DNRh7ypQ2JQX_y3tutUHmk3jzUS4f4pC-D2fGOf5YWcVDM1_G1c92OLlwZFvQesGtLBlEvvrG5ed2ct7vOYt68zPBPeRA2BB2rMPupFOD3yGhG8iSkY-q9p_fmKfsereztCxYegtwNJP2jGVhJxDpGR3n12Nj7SLlLNR4MbY-CvY_dp3QrO00rZsNajlXpzVB_uItqzG1Da_pVPGlalZ_lmFv1ZvZIqaO0SlXNW67lA1rHW-gZVjFp1QsoZN5uS5mO5945q2wLgHT_yi9M9jXih16x8f3Kd3OkTbqp1dqWZvA8M83A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3dh290f1Q6_ir3iiGtVRmzOrRJehpQjLWHp_SrkJjyCoLosdIuoFv13gM521W_rI5zd79JZOGucxGfUU0C0Z7SwU3L7eDlQ4h4Yyt2HA_-3ERel7ZhrZJuIAgK1Uf2ooqHs_EGtTvVO5Agwc5839Rh5z2avek1l5z_LgmT-a0zY2MitAYgjvIMWXVZ1r6APL__hYTnI2EvdcJ5Ln62JXD2JiBQrh7XCal1naGeDEImd6CJXkTf9nToe0qps7BvsypBEnbENbBJj2Lrb5jcUlgMVwHFIKeFwuQZ3owqA7T8pvoLEAwwAILD4zYXfHyKJgHBEXZf9-qCWMU5lLpuEeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uh_DbaJBbR4p7fZNCgjji1HrsTCMw9HPfgFHLOAthjsUzVXSLnDbVZkujVPbGQcZn9-1imuMZDwN_GFHUlrtQlrb5_O5LjyKhhpp1O1fteovzoXhATzJ-ucG82aNEohjQ4v5Qob3ZlY34EGeNt-dgELjMTWkM0fnVzwprNFTNwunqJTcd1DP0pMA_UDLYBuO00twiC3ikJKKP8KiFS2G8w8uQYznZfFTNQid_qXs34o3MX71AYLzOhBlhZF2GoysHbylKEuxLc1DDfApFk41EItRBMxXrPixApbGwT2Q5YQfyCVdFVD1U3IxIEG_9mtTCET-pjM0fCMbQksGV5F3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f1FcdvyI4N9LG8G6W79__58ppRyrBZGcDugHWFWzagnNXumNmilHHJypPiFv9nyWjQIubh_EgRg-eccB3-6oWlPXz1M9ukkQYxntx1eLfnbeOuYcMVVs47iMlq4Az8MXltr4jwqaCVPKTSCPQVdN8i0S4NNN5qcWnAniizpGMm5bXeYafgwRvdxkT_ZfSZT7LLr82M4zBVrz89QmFXEnIqY_hMkeNz70P2GQF7JQ089wEgU60aJI5cXniITrgQAh3qrgwOQIOBVJHbfk6G8ws2Ym7APfhtukVV8WeHBmnCRhHA-6JoSayzlsjm5mqTyohJQPbogapWGX3FIzDdtsIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHBCvpthlBJoBwvNxsN9gnfdSnF6l1V9v3KlLZcvJpWajH2zMy0DkDfQCglm1WhhLDxHrpaj6f4miln44MC1u92e6Q6jtALg2ah3fR2GcQq3KYvP6QiwGYYhFqXZjpmQUWvptqSa6GmSddVDAfwhJgZhHuc3FspBrS2awCWUFyVsdC7ubqfDfvulJ9FgSUq2AqaMqNxa55D5L2yBdhf4hg6qd6aJo5SRVkf91iIsOI7bxbpF-3_wHg-_O7xYSt74t2FeUAiMx_7nXEOtkIf4lkJqfB2e4kRSfsqA9zNJenIm30dsVlHJP7gMuLEbjccOx2_nc9ZzvaXguMcWo7cv2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6RheUueH3rP43lnGMQLU2F6sTEj26n9qFlGlObqrrP9mQ_uvaTbO34KNC1uMnK4NrKnYkhuYxdU9hmdVKpouBddIIan_DbwhsMM4o4bOWmPzPvaWCNsp22VcM2Kp-n25NV02YTgzkw22SFlDztWMaiawONhHEB5m7KOQAVFNIS-MJ_icf-jArs7chKiPPTNh0w3Q5nSHC0Lj7nbaQzAVaDW9OYNVMagbTxAfkGGVcat4OOBzUDirsMs7Wsi20i_cMQHefjG8T2JCZsaC7kzsHZKzt5iyO65gO53s9KejOoIsqDjv7_D9LM1_zGsy4EUxL-laY_bKH06S62Si7-lXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9wyK5fZYXYKrAC9XJA9Iv4wMHIqQ9PGeFLUi7Eo6L08_4HSC_sywP1wlJNVipOL4soaXhTl6eZbGfQnpNu6JYay59CUmfJu4bp74PmWT7S8ielEolydyLA-N9rgz_x_uFBEFzlBTvZrVhVg7eCeeS-rYhONu69IvBoza9VAmPZ6_SST7KNs5p_RT0r6Z0Iyf_q6mDy9YbwJj1j481ko4KoWCdJeHp0rezI_ZBqd87_04FuFGs7aIIDBqjYV7w0HOMbE_9yE6_-jUd0OpCBikG3Iwcm5NpnnSH-OPjyFW196QJQiVJd5EEmr79BdkP9Aosr9dp8kt3bWr7dSXdueyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3mIBEad2dDd45_LRiQCOCcOo3o7TrK_7B3nMjanCEkwLPLhWigZmpp62jFg5ZPhTL75BcZTO-K6ZStHNoX_4DZ951K7129Tx6_wOXYdbIZ7f27xQVjz8wfmqeHpy493lB-A4EwQ58kLlco2reVngsjBAmyZv49gejSqUM1lFG4hNMn9zL3VG8ZPDTzCoq-M-GUWTXTDGYDGTMIKNgSiGgcmrZui6v3Gq40OdCYtLSyYnp2txgTPM4yeI1khJHnYwSci3Aj3r2fgYY-ZOK1PtzoVsDAfqcZnG8CeyL_JX2zWmUwMcyugnBqGvPXjeFBB8WgZK2_JjoLGTYv1F7oP1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/se5Jw76KBzHqCBkG4lRDyMOAiENNVhEnA_IjINeMrpDTmfdIRZ5851ciFquHGIfGNfqI6SqXqXbHwZ8mpswzBi6a87wQwtF42-rfhswh2EZy6lOSa2hxH-swIJgDczjSANTGIM85exTLRwcktLFBewvVNA4LGDyt9u2RiBcAJKmXIPS1rdTiMpXVKVOFxqIOdQi6WzUIgJhffvvp-M2xHIEiAIASVxZVWoLXPvKRUPAW7LhVfuUy8V5Rm-w0ew887iQ_7L9l1mLzOcWIj7HUC-SBhSxd7rNFcf9y3YmPjn6BL9SS3b3mEsMtKaru4J7PRNhGsS-32FPpJr7JTmZy1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCnhSNX_E1rr8_vndMv87HwV3mgGtGRpsPhZ2NnoB_fxWoNo9pQBwqVZi-QD1nlkgI5kbCTaklJ9IhYyvPaihpRwQ1WGADNX0Vb9OK9gviZd3HSMfZ1-XPmivU1ZLmbzCRubj4XhMs-w6DoaBXoNAwOcM_96O4UCHrqWpbwHJNHOwYAAggCLqgvbzcjXASKm3ir9rd3N7mnuyWQwk3e0Wei6yIG8rP5MhViREWvmKQfxmp9XK7fWXRL8Uo2Tdhjj9zooKKNmJ7L-ir3zDN0wXUIXfzSHb2uLn8URHOQMZYny3mmJi31o1x-LyVqZtPWV-t7fwNFSrW8dnFTkBEnfyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sha0UXjzhp1xAEModzHXwEChbLomiBAAHDPn4g2-qPB2ZN7RGyPvkkfz3J0lUpM8TydzJ3WrrLg57sReFsPSicobJPWN8gYeqTap81IlgaYuFx_-Mk4mrfUVhp5AeruJWxmhXKQjtTGaoMTj1DAW8UBFx2n6tlc6LSHFs6pZrNGDfO3M2AZQKZgU_fUbbE6LiTxPIrGpwEvHRMqoc1fKfK25CJIggTWAQ96ZdSnL-NnJCflWUqHadaEZORnSwJXyVsoT263-WUOt92punPM8PvXJkvO1BONhU7jqxNVShFi3zRqsuFliQBf_CLhjcX6B-5K9y3V_igaFiILm_fqpjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilMR4d8mhTMwdQ_nfatlqVpWhd8KblVi0PqL1CDm8o2SXA7R16bpKolku3XLhqn8Y1zwKNrB9PycmlzO52WfbhYGPNHdeeEXiEZxXXOSZkyJJtL_cYPY_XDkRNqcOKa2lKrKMDDP10t2W0xN8AEODrf20Y8IKdQffdXOJX8A2U6FGlVeezqm_yEgyRa-cbSAB-op0rZjgbLDOK9hiUjL_0j3vZ_sArmittCEvXqQZTB_RPJT_rgKFxRjavXzJ85J8Z4c5czBvWpLsyRbMIrR4UieFj6fiS3BQnZPBBFxDLWsoHc0-iF2eJ6spmxzIfp5OAYk0U3D01xvc8M1SC9jyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfxVdo12X_pRk_0VLnnDnA0nFDsMIhlKurPYDddbU14cpSKWsotJndRX09g7IHiufTfl1me4Ouv_ddXNy9dc4Q2FHex8AQRbee5qm6Y2bUl3vVyGUzdwonb4Ib79wqLboEEIlvtpnHi5R20d7F0hSv7Ao56C-6YSTsOzNMPM1rradcsXTpn3uodnc8Le_-eJKv-p4VaBDv6fAq80s-fhxeuD6yQJLx65mePf6tM7cKEz7win3u5tgHh5emJCfD7mh6S1gxVkNe98Wmn1uqka7D8GQABIsA8l5WaoWbGa0b-hRFczui5AL3KpaKxIfnkpVghbUfTn-SpVjNxJvMj4mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZPr0WmFvFABfPHc0ayaMmAlxVQUMrbnEwQg6hZTbGDnTgfioJ2BK_m8PXnncwt7wR3qWJK7HHPga0hrt-M_2O7v9Ifz24CcA1_P5A0o73aHh7_G50vcspuD2i7D7tSivBIBOz9-6Z8S07zqFMvGg7kAR_OWMKm0dZtePxW8LSAzOREYJisAL-swjAtxGWcWNf92AWKtd7eMFWprHa5UE3n2Ii8675Pf-uG1RSjFvY0SO6Mzg_CMRONI_5SMCDOHNMXkVFvZG6aBWx-uuMAR57P23xuV7skQYurD-EwEN-EGxuWjSC1uAAYoxL3rWyxfcyOBsaEANtLjmswNy2Vc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=ZL6eYWgJbQg3Wsc0BKbc-cZ1CPaUdJzGgAMT9wYC2DEBsC0heHZxd9U0JqTP8dDoxBIGasQaXH6ekcnRCyX5d65v6LTUNH9mO1NJVuSBayUlVGHYf3L5Pb9CHTuRAhTYAT-VCROXmn14c5wgi826izpNe1ry6_2sQXryBkT8diP6HYT5eHZ39Nbwx1uA-g0ebJvWnv82DrOb6-2jeZipkLc_P9-UVU8Z2I0G0-2XLRa0PiogoKttdv6lGhu20A7PYe4SmjGjEjH-FoylHpkBHAJZFS_yiQlOhkml70XKS7u8rId2zxWrxrGYUpmlVZUDOt2h3Q46c7sGGPNj0fA4CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=ZL6eYWgJbQg3Wsc0BKbc-cZ1CPaUdJzGgAMT9wYC2DEBsC0heHZxd9U0JqTP8dDoxBIGasQaXH6ekcnRCyX5d65v6LTUNH9mO1NJVuSBayUlVGHYf3L5Pb9CHTuRAhTYAT-VCROXmn14c5wgi826izpNe1ry6_2sQXryBkT8diP6HYT5eHZ39Nbwx1uA-g0ebJvWnv82DrOb6-2jeZipkLc_P9-UVU8Z2I0G0-2XLRa0PiogoKttdv6lGhu20A7PYe4SmjGjEjH-FoylHpkBHAJZFS_yiQlOhkml70XKS7u8rId2zxWrxrGYUpmlVZUDOt2h3Q46c7sGGPNj0fA4CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq0HtgauliF_zsIPpbSZSNUqQal3C6rv_zLDzcvGljxsK5xqd9FBmXhWbBp-GBeL1_qML8CM4foCWLAMziiGDuDIdo1xkiPr64mAQi9bKJmHQ9lmWsIDEKN_SZxcfRkOaitta3iaiz26dYHvEmmG9tmdEj7d107NC_w1IrfIVzl2rg-OV2q1s-Fb8k5qNJcjsYndf_OLR0KsIdjBJ-8-ygmHjco1viHKSyYc7VoXeV9oOAobnKXqVzjnOB7mvIMpRHIP5GOn920OetOCmy2CAyp9lW1wDizOvdwSvS_1LhPb4EAJ7ZhzbDwHtB6weZzWdREahll4i5oK3icBbr6AZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=OdUh89IF3vGWvAO8HvzRXcErZPF7q-NdU0ZsQXeLwjsvSOqbcom2H2qAcDNsgg6DeMeX6zHvsx9aPLgP_E4tJOvC8VotTcJssuJRec-atcSzzkFEQhS_3PXIU7zDELChmQJuf2NUJ6N4EDnY8UXaaC_VtXAJKict6mKdQl-yH2Zretc583sTfzFgtrFcwGK6f317let1nufp_JUDy_DlvyeYXYna9iwCuGkc3OhU57v63-Wy2GDZUALU6TXbdYlpqGWt51vcL40zScZV0ZEiRXF2B-0su50tLNR2nfVlx4gK8EvO2qvAj9MoatGyb78OP0OKvo_18SchouSPeyPsAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=OdUh89IF3vGWvAO8HvzRXcErZPF7q-NdU0ZsQXeLwjsvSOqbcom2H2qAcDNsgg6DeMeX6zHvsx9aPLgP_E4tJOvC8VotTcJssuJRec-atcSzzkFEQhS_3PXIU7zDELChmQJuf2NUJ6N4EDnY8UXaaC_VtXAJKict6mKdQl-yH2Zretc583sTfzFgtrFcwGK6f317let1nufp_JUDy_DlvyeYXYna9iwCuGkc3OhU57v63-Wy2GDZUALU6TXbdYlpqGWt51vcL40zScZV0ZEiRXF2B-0su50tLNR2nfVlx4gK8EvO2qvAj9MoatGyb78OP0OKvo_18SchouSPeyPsAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=eU318m0ANUt4KsM9flUV_Gdw_cyb8HhWiuW72j4M_gLkeRMirCEdOMgitShAcQu5YGn21amwGI-n3KxGuZhX4U3h_tLhA8sDvT_NT0G5H0ZXG6Tcl2svYhIMDlwUKErovKJyLBO5JwYKxWRXsL3BEvum7OL5g6jE5z1DKX4bvcnM4-NVgCnSYoyPUKE5J5jvdju3We2hgS7Zo9_G3IozVqJNuexjlGGFiMnF_tr7435iZDKxaYOVO9Ry051uAdXKVtWH924YaNLT4ATt0-HCV_XjdLK7H1V3EmGPI60G_YG8GI1bIgK6uOcFjk8R08rjQ5oAKmQKiSWeDWIOuut9ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=eU318m0ANUt4KsM9flUV_Gdw_cyb8HhWiuW72j4M_gLkeRMirCEdOMgitShAcQu5YGn21amwGI-n3KxGuZhX4U3h_tLhA8sDvT_NT0G5H0ZXG6Tcl2svYhIMDlwUKErovKJyLBO5JwYKxWRXsL3BEvum7OL5g6jE5z1DKX4bvcnM4-NVgCnSYoyPUKE5J5jvdju3We2hgS7Zo9_G3IozVqJNuexjlGGFiMnF_tr7435iZDKxaYOVO9Ry051uAdXKVtWH924YaNLT4ATt0-HCV_XjdLK7H1V3EmGPI60G_YG8GI1bIgK6uOcFjk8R08rjQ5oAKmQKiSWeDWIOuut9ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH5zMytD5fxC8E35MjxlhdCxOMf0i8ErecqULDBbP6fwgCDaEgQI1_JzHetpuPcw-PIFHZNBfo3VD9M0TVCkI7CVr5VO5UG4L-s3no8lZytVbIF4J63i71JbbRhX9hchZ6M0uPeeXBHZgAP9JDNEc4WaxhQT6u4zu6A93Vt0aIFULY7nN0QT0yaG5zcrhVM1UKLkEmu-O1wklyIitYdrg24pGzPUmIJZp42L_TTF52e86E1Mg34EXFyCpbIzS_wVewh1Np71mw-wZfdkDRizVa5I_xEIXQ9mbJuDyqucKFDsRbQBkfu8TNGaVmuz25bPYAtwH1oUzzE401xtImVf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=q3cxjpnjt3-pYDvfhjBlPbQai7_br1cJYrM9r0-vSKsBm_dX5VhoNnRwJnG7mEPBSM2trCSYzRrR4UEGoSadGeJZd_bRYH7reHB-Es3iHYPWL5ltOqHkIOVDvvAFx1FmdO1RKCjruFH5TES7Wp8z-bMhSKabsN0Ko8ClDzeriggzD383uJiTyeDGOshr7eYmMtv0UjieN3PuH1Bs6rjJAP93ZXBouiAKK_aRDZkcWkvrhj2qfzmaK7E1F3qS6xVlvnaxtedD98tcN68cqbEXr1hEnOq-H-7IHwRxsg98y0kC20u4oSiw4DXHp7gvGCHB5dlM3Nv62YwA8TK5SuTB8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=q3cxjpnjt3-pYDvfhjBlPbQai7_br1cJYrM9r0-vSKsBm_dX5VhoNnRwJnG7mEPBSM2trCSYzRrR4UEGoSadGeJZd_bRYH7reHB-Es3iHYPWL5ltOqHkIOVDvvAFx1FmdO1RKCjruFH5TES7Wp8z-bMhSKabsN0Ko8ClDzeriggzD383uJiTyeDGOshr7eYmMtv0UjieN3PuH1Bs6rjJAP93ZXBouiAKK_aRDZkcWkvrhj2qfzmaK7E1F3qS6xVlvnaxtedD98tcN68cqbEXr1hEnOq-H-7IHwRxsg98y0kC20u4oSiw4DXHp7gvGCHB5dlM3Nv62YwA8TK5SuTB8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOjCMq9X0r5zM7Oo_0G79riqxOKy4Swzzmq7XZC1_jTqMd8Y3FwQbSdHS7fNiCZLGWdgdyGzkVyGsiS4ErbaAyspEVPtGegpENK3wz1CJ2F5OqFr634ye9OX2KQgvzgt--hoLE9cQE2Xet4ZvVlEHni1E6Xzw2pmFazUW1DCnMAPvcS2qYyHXPniUNX_8UaXyaRE-xUhKMoqBJR8mPEAypLSLibSW0dMPd1TdU4H2AfFl_Lq9dkEO1rV691611ReodAXWBYWKw_gB9h0VaUV3BTYevrot1bgEqppr4qmqVVxkyOQcbNyp6Nf_YHbl3uqzTKGC0ZNcTXsRuts85x5Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDuuIfH2aJncH9VhoaDk8M1Dfr4dQqpDopsdQDaQulnL2ty2_7_u4FgxuReUqNMEV06zFiHWUt2k_fWN0KplYQvpexyHo6TNO-VvhM4sztxEygOdxVWqgNmEd7p6xDsEuMElXJwsamtpQhtPpw1JRjSCzVDJDfvVtgt1ZuSFq2-5p6tRgPVubW4uTRMygK0dz0kjYT2Qyaw4NoJcC4OzCcrSDnwQNq2P3eDEzXbTHyRniN6sP4XRiIp26GMht9PL_rP8gHU1gnDfZRjHmB57kmOGx3lGCnu1KP7r_MDYEzziE1Ze6rqrEN0g5Zw82RYcQxx1K1LO18Kaw6UOmz5Oqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlE99gVTHfg3U-46o5p3ITOjrmf8buKyvlP57CNhwFv4dW62LvANIIAiBzKQaIUoAD-J1JuhiaVvG6-pUPBTnKeWDTOGI9xuHK003bFZu-AZSVXXSkXMItvcNDapUShx8z6CI6cOk693iScm0yVbtUjHHoxC5sHDO8JJ4PitA2bPBtwx-uhHeqLt7pXeW2T8yP7s8oCQfMBNLrp1vgxsjnOA0cgL7-eNizgbsbOkf3gMewNy_WMSWgzJrmFl4POUsLUOYkVpSDy9UVI4D2Gk8b3IwmRtSW9xWDQhcQC1xxPn4Id46HuEHBrlp0eIWJPy7kSeq01MjzhVspuFE-QGBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGj7U9GvBr_NTDD4IHlE0a9hbRtrPMcYrmF_ESprezeH2OMzj-U5tUOfbJxnm3SKAPt26PSW5T9qP19H4RoupdkTaPcQnPQ2pMq4dwl1hQJCZ_1_wUiIvvXCv8vK6qbQuouQK1wDtKIJwv-gfA8mT-267cIIaT50vopxUkaa3VVFuB8TwKKUCzr8bk7cHFgQ2j6ntHp7oskOHuPEhhCvozel4MIWE70j0pyqVCQaEwIhnBNFgg9I_Yyvd0SJBww635Q1nGv6CPswc2mo83maYtLxatoTmRfXxt2NoGLiMzpA-wvrZcb_iaMK4lP4BM-NQvEuKx8cougsmz220-aYoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=g4HOP051isQTrqSnmuV0fpA4q9fUTPDGSUorKIsyslcuYXA55V12ASOLiW1UuSS2u7kWewc9QGso4glnjdKwgvSdDitKRIju4wiQ3qc4spbGDeM1eTvavYuVXHB-Fz-3gH3dbILOuBRUsC2tzvenZYUaYOsf5lXiTUUssZYU9lRqs35vS1Wwpm8UhR63dSb3h9I-JJ4k_OZxhNG7yzfbMf-DMjaZSlXycv2I-NLQYr1Ff-gBZ3BwnG1_MR-xVy792MnFC1zjBorD_8BZgQPRC9Wae4qCASGpYytP9WvPTUIei7oHfzaWMFM-erCra-_dpFZO7MrqUuYIEh_BQEHpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=g4HOP051isQTrqSnmuV0fpA4q9fUTPDGSUorKIsyslcuYXA55V12ASOLiW1UuSS2u7kWewc9QGso4glnjdKwgvSdDitKRIju4wiQ3qc4spbGDeM1eTvavYuVXHB-Fz-3gH3dbILOuBRUsC2tzvenZYUaYOsf5lXiTUUssZYU9lRqs35vS1Wwpm8UhR63dSb3h9I-JJ4k_OZxhNG7yzfbMf-DMjaZSlXycv2I-NLQYr1Ff-gBZ3BwnG1_MR-xVy792MnFC1zjBorD_8BZgQPRC9Wae4qCASGpYytP9WvPTUIei7oHfzaWMFM-erCra-_dpFZO7MrqUuYIEh_BQEHpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=RGoaRqw-_aZudJzrFRW0n5_SF5szCO5tOETXESyOt62wScc4GAsDdo6eKfzQ_87EITKX6FES8RXLOWuvuaw2OOccWXb0dCo1qfvcn1TsoO14NRuqxuPWX2y-S79EE9Cs0QsQj9jtKYkHwL7y_5E0HAJdfacc1PtoEE39S2i0s9XjSc-O5dzGB6FDMAFZmLQsRORm1IwrN5K4Am1Fzvu0Y9wyKlIiZNjvZyrN1gt18W2uMe8mmTj0-Q-vEogkfc_Zu_SRVwS0mxybblGFSNHnSXLuVUVDgCZWWIbBw810pQOZMjwhIqEB8Re-Yr5qfLUnLora0J8-sibQxfYcGARU_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=RGoaRqw-_aZudJzrFRW0n5_SF5szCO5tOETXESyOt62wScc4GAsDdo6eKfzQ_87EITKX6FES8RXLOWuvuaw2OOccWXb0dCo1qfvcn1TsoO14NRuqxuPWX2y-S79EE9Cs0QsQj9jtKYkHwL7y_5E0HAJdfacc1PtoEE39S2i0s9XjSc-O5dzGB6FDMAFZmLQsRORm1IwrN5K4Am1Fzvu0Y9wyKlIiZNjvZyrN1gt18W2uMe8mmTj0-Q-vEogkfc_Zu_SRVwS0mxybblGFSNHnSXLuVUVDgCZWWIbBw810pQOZMjwhIqEB8Re-Yr5qfLUnLora0J8-sibQxfYcGARU_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=TXUO6xkJ4sfA2KNJOJ4XtZgLivApPpSTzmdpjoMFisAK2S8yrQLiDKcOQIRcdl3fiYS41AYyYxQqOWSQi-GlnbfUuwBsCjXkezNIbTp3S92aiToC8-qBKSrH9_tpu9y8ndTXTcBc36-pgvEvApY_vfo0yIiijWcSTumTEmUiXJhEvvKvdVn3bmXgrDYA51WT0GAlbdgYsvPr-yrIKWvn6iqwgC-RvQb5UKs7wArztWq5RmM5xh-ogEvVnc5jhrWRbXsrYoTIJfFnO_iU8cTSC7DnK6GQOAkpjA07eO3OdPXjry-xz_Tkmg9KwPu3XNDW8-vbPwf-Pxse9Q0xkua9Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=TXUO6xkJ4sfA2KNJOJ4XtZgLivApPpSTzmdpjoMFisAK2S8yrQLiDKcOQIRcdl3fiYS41AYyYxQqOWSQi-GlnbfUuwBsCjXkezNIbTp3S92aiToC8-qBKSrH9_tpu9y8ndTXTcBc36-pgvEvApY_vfo0yIiijWcSTumTEmUiXJhEvvKvdVn3bmXgrDYA51WT0GAlbdgYsvPr-yrIKWvn6iqwgC-RvQb5UKs7wArztWq5RmM5xh-ogEvVnc5jhrWRbXsrYoTIJfFnO_iU8cTSC7DnK6GQOAkpjA07eO3OdPXjry-xz_Tkmg9KwPu3XNDW8-vbPwf-Pxse9Q0xkua9Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=mjMW-nGPRtMXCX_KUKxpx1jznU_TI0TW1JycQ0ebVJwWoMgF1r1MWFUpuXu3GVHI8hoBkgFPcjRWpKKH_Gg05VgWhI7L9byvadRGq1t55e_R8BrUwG0QNDBWaifEQFY6yH5nuXEd7Zz1fzOxeYhBKCiQ9Ex4nSmKRIqAd9IEJvQ5LAjdppCoNELJofKEBflCgGFaUyt672HVqWkyWGFB5qrMsMh3DjW3SoQtrbF9KV5hGBX1yQK1QsGE9BLjaNHWymF5dfh59O6KAwuPsw6pDUvOexXRT5h_t8PCwBQVSSqd9nE8FJdfRmitGAL7107kpr2U8wPoovmy1kQB-MNho0adzQXqC-qomDA1fwX_Ns0CFkZjtcHcY1IvIhj4AhfQs-Cnamf5D5Cwvnqui1ZRqKQy-VOHY5CzVOrH65VNgS14hv0PGqexVP_tgZ4jlhNbTjTDhwCNR4C9e_l482z0xzkH6B-FLKNl4yw-w-JCDEs2P-CYEeh-laatcjT6dcv2SK2eY73b9saEiRQ5h2xDUBCngXGynfNOILdPe5IIwVEdHjerhaz16khj1TfHUgbh4nOhOP8qHLjhK-jw5_Mawmz3ykB3ZAMiEpvTqiAcnwmlSojjDW2Si7CF3koEj4sNbfcHR0GTui8toTlgQ-JQ2tgrU5SlOkukQN6bQHshxjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=mjMW-nGPRtMXCX_KUKxpx1jznU_TI0TW1JycQ0ebVJwWoMgF1r1MWFUpuXu3GVHI8hoBkgFPcjRWpKKH_Gg05VgWhI7L9byvadRGq1t55e_R8BrUwG0QNDBWaifEQFY6yH5nuXEd7Zz1fzOxeYhBKCiQ9Ex4nSmKRIqAd9IEJvQ5LAjdppCoNELJofKEBflCgGFaUyt672HVqWkyWGFB5qrMsMh3DjW3SoQtrbF9KV5hGBX1yQK1QsGE9BLjaNHWymF5dfh59O6KAwuPsw6pDUvOexXRT5h_t8PCwBQVSSqd9nE8FJdfRmitGAL7107kpr2U8wPoovmy1kQB-MNho0adzQXqC-qomDA1fwX_Ns0CFkZjtcHcY1IvIhj4AhfQs-Cnamf5D5Cwvnqui1ZRqKQy-VOHY5CzVOrH65VNgS14hv0PGqexVP_tgZ4jlhNbTjTDhwCNR4C9e_l482z0xzkH6B-FLKNl4yw-w-JCDEs2P-CYEeh-laatcjT6dcv2SK2eY73b9saEiRQ5h2xDUBCngXGynfNOILdPe5IIwVEdHjerhaz16khj1TfHUgbh4nOhOP8qHLjhK-jw5_Mawmz3ykB3ZAMiEpvTqiAcnwmlSojjDW2Si7CF3koEj4sNbfcHR0GTui8toTlgQ-JQ2tgrU5SlOkukQN6bQHshxjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=dfI_6pjc7mYQyLJ2kV-St2d37CkoOuZHPZMNLq2aqygESUgcN7a2g9BKPDNW5Z5ssBpRisVB0FkfOZiFQrRQ_nzXg_ivgPHBdX8SHUmClOCMsI0oG2a84I_87LVoZrVtvh9H_M9tZcbsRd9D6sPTD4HAjMIYKJyQaP9b_G8cjJ4Paq3ENcgyeKkIN-AiuMup0fvpY3L3DCmN01-j-7iQGeTxzUBJE--DLiiOK0sXB25k7GSfZVGXDkBK4d4w2UXI8d3JSkPJKPEQi1mcfkBuRYHk7q3EI6sTZ0pD_ZQbCFccF8JIOjx5zW-h_yVsOUfmLzaKxFrKm2KZU1dzxoCObQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=dfI_6pjc7mYQyLJ2kV-St2d37CkoOuZHPZMNLq2aqygESUgcN7a2g9BKPDNW5Z5ssBpRisVB0FkfOZiFQrRQ_nzXg_ivgPHBdX8SHUmClOCMsI0oG2a84I_87LVoZrVtvh9H_M9tZcbsRd9D6sPTD4HAjMIYKJyQaP9b_G8cjJ4Paq3ENcgyeKkIN-AiuMup0fvpY3L3DCmN01-j-7iQGeTxzUBJE--DLiiOK0sXB25k7GSfZVGXDkBK4d4w2UXI8d3JSkPJKPEQi1mcfkBuRYHk7q3EI6sTZ0pD_ZQbCFccF8JIOjx5zW-h_yVsOUfmLzaKxFrKm2KZU1dzxoCObQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=pFCkbujVbZzxyELL8lvmJpW2Go-SdC8MPZOM5BAlWBTkXXhhic5SMlqS8JtyUwglGwT267Rz5vzXB0jYtQNMX5F93ej2E_xrlb_nA_diOFGp_8q7jjrdLTCAsXesr2B26o3gIMpHKHJFVkwFQREN9RWahHv2G4yOcFfROPA6kEvHZY5AnnK6ApeddpEdducOCDXgCRDnuO_pfoQYlPvovZgNOloo0jbco-L4L7V4vWVBqZ45p6I3wdKFR8ETPo5KB71u-zPDO6Zph2YW62b2R-5awo6h3FM7Dh32ApABdX1EeFffbGQH2AvecKRhGmDLxvdvTxVFUOaI2doDDgKYSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=pFCkbujVbZzxyELL8lvmJpW2Go-SdC8MPZOM5BAlWBTkXXhhic5SMlqS8JtyUwglGwT267Rz5vzXB0jYtQNMX5F93ej2E_xrlb_nA_diOFGp_8q7jjrdLTCAsXesr2B26o3gIMpHKHJFVkwFQREN9RWahHv2G4yOcFfROPA6kEvHZY5AnnK6ApeddpEdducOCDXgCRDnuO_pfoQYlPvovZgNOloo0jbco-L4L7V4vWVBqZ45p6I3wdKFR8ETPo5KB71u-zPDO6Zph2YW62b2R-5awo6h3FM7Dh32ApABdX1EeFffbGQH2AvecKRhGmDLxvdvTxVFUOaI2doDDgKYSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXnJfp-FVYwouzYwzq2VgXTPAvgpcT7eW0daxcsSSo7zIOMD6cceeXHYIzYOXR6zrqrzlRIQKjdL7HNhXl82ybxu_Kh6Nlkg3i9jR0jiitReyqSoOh-ZSzjC2tm1zlMpcmTPdkeI6_1i2cnxq25cn9aaGlTF5wJHF8UEJytSaYHF3-LUeTISLqfDhBgblCbATS_SlG-FnC0DV1sbQ83nD0J-YNYDAC50b6m8inN-w8UDuY71NVQEAs12CIzUKX1Hg9YO5E-0bMCjufzDqeR0ScRM0bkZRNUka6a7fGhrkUJp9zzuGIYjABLiiAX8lGtZexO4HcpOZ-IBTxk1ZzLk6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=cgA-s9Byo9Sz00XCIxDKTQNoUICboikQNrO2MIa6y5AcOlT-sHUryJUCBql5j2F7jH1YGCTb_z-v-7OhReOOQ5CZRwBIcYREc8gJz96qL_H5n2RjfwDjdqo3SzOSPaiFnEKF_yIXl0_ttj_TDEazjxhmSzauShgTu2wzW_PJmiwlCNCQ-VNvS87mYzKBWHaPo7ECzVu-6dcnQbAWNEcIaTjx5ghXeYoDI7v033Gm-gz2wDTLn0VI7Kc67QNb-J_L0Lg9OingL-ifcqAeRClPFY1ZoVGLvXhLo2Ne7hVcmPkHQhLp5GRDvkZXrropwJ0g5mYFOg2ZkEpekYAi2ElgtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=cgA-s9Byo9Sz00XCIxDKTQNoUICboikQNrO2MIa6y5AcOlT-sHUryJUCBql5j2F7jH1YGCTb_z-v-7OhReOOQ5CZRwBIcYREc8gJz96qL_H5n2RjfwDjdqo3SzOSPaiFnEKF_yIXl0_ttj_TDEazjxhmSzauShgTu2wzW_PJmiwlCNCQ-VNvS87mYzKBWHaPo7ECzVu-6dcnQbAWNEcIaTjx5ghXeYoDI7v033Gm-gz2wDTLn0VI7Kc67QNb-J_L0Lg9OingL-ifcqAeRClPFY1ZoVGLvXhLo2Ne7hVcmPkHQhLp5GRDvkZXrropwJ0g5mYFOg2ZkEpekYAi2ElgtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhveu7X0toYlATamyHlSVf-V31vt0uE9F4KEDFxsnbfheWHeO8sPrfEm8wO4xfMa8ZJM46hw-CRTKdu-fifeoHvPSfqUSsBFpiOLecSbGUTka8xrBNbhET5AL9E_rPK7PygcGcKnCOwBYbv7Mt9U_rIcGgZGhJwXCiIOULiu-TGarfqVObn8slUv6Wge5CkII46cv514T6vx3lQcICaJI7JWmedmd4RpNY05joZmmBZbwvU4uB-YUbmCCtTYHS3aumJMPMGf62_lkxiIAIQh5EXPUXjS1HX5iUAuJcRAKbhtrWrrHGgrhYlu_lmY0USOqzWYNxdHaZgar11k-3fNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6en4vtNWmVb9IMy6SediqabUKXVuKjxL9jmJz-m_zD3wDM29uPZPYLiYA7BDwUSY7hyINGSzbWH-Niua8hw3DA-eTdwEhQ_1J2vV1S-_LD48ycTWbU_9F2z-F_JBfrylk5i391jLufbWABL7j0vG73RxtgOMl2l4VrupNUNMT5bcrrNKs6Y6M7A86_a9spLcW6wA0urfn2FAPjZy7fq7WGbHNi8zxk_cVhWBek13XyQ2REprFB0XibCtpLqDJ668lpChGpjrMZKGQ5muQYIt1ZshlzUf2fHO8Em5-ENOOFVcscAJIUyQ8hIV1BV3T8GyVPSg7suKOD8TQAg5A98TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=d2JwNoiS4poKAf1jwZ1uO-78aV7JBsT52BGhR2cA-EaznTQnQG0P0_OL8a6RGwk3j_PGkgJZSwWqYmpyMhurB2j0pNR6p7T2bvW_m0uWuQdkzaJEN2o1u6BUOcGVs4JwgL-N36j_ZSMWeJNmGVUws7o85hHa8Lys9AGQG8AEyfR5I2IaDUzyZ4ML-IBNxgffzl4ZDuazUlz4pBsxIdRn1pUcdHGikAF7Rr4Hy62Y188IPpeynNkqPmkzC8b1XfvvOf-G4T-iPIRnYKYAvhiweTRDYm9sTYMTmSeP5Gig148Bued-WUASmrBIPRAtCcgfYVTws2t3yvsBt3mCbPtc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=d2JwNoiS4poKAf1jwZ1uO-78aV7JBsT52BGhR2cA-EaznTQnQG0P0_OL8a6RGwk3j_PGkgJZSwWqYmpyMhurB2j0pNR6p7T2bvW_m0uWuQdkzaJEN2o1u6BUOcGVs4JwgL-N36j_ZSMWeJNmGVUws7o85hHa8Lys9AGQG8AEyfR5I2IaDUzyZ4ML-IBNxgffzl4ZDuazUlz4pBsxIdRn1pUcdHGikAF7Rr4Hy62Y188IPpeynNkqPmkzC8b1XfvvOf-G4T-iPIRnYKYAvhiweTRDYm9sTYMTmSeP5Gig148Bued-WUASmrBIPRAtCcgfYVTws2t3yvsBt3mCbPtc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=hGBxS78YMd_MT8gz6_1WZItitkhcBcshvPtrWdVCnpOQHPAXGbS0RItiWvhWYK0W-nmn3pSokqQNbdpnwLIPqhJiqMh2Vbtvu0VkWo-7TlWEsjaRCcoHHUvtcpBNJCndrf8cdujsu5wN44K1LS62121ZcIC5h54EzHQLEUOqkLSkStrC-FBMuysRjO6Ml19svTHcPfechpQrbk6EDqj1Bw4d93bwY7z9rcQpSFTrXfPpF6PjoFg-Dx1FHDUAzMXUjbDxEJ4swei__f-PiQwIY46nDXrkzoel7i8d0nHESL2UkWOfmxkdZw9m6ZoTRyQ7Mnd8ZI7OCKzkRD4rfOrxuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=hGBxS78YMd_MT8gz6_1WZItitkhcBcshvPtrWdVCnpOQHPAXGbS0RItiWvhWYK0W-nmn3pSokqQNbdpnwLIPqhJiqMh2Vbtvu0VkWo-7TlWEsjaRCcoHHUvtcpBNJCndrf8cdujsu5wN44K1LS62121ZcIC5h54EzHQLEUOqkLSkStrC-FBMuysRjO6Ml19svTHcPfechpQrbk6EDqj1Bw4d93bwY7z9rcQpSFTrXfPpF6PjoFg-Dx1FHDUAzMXUjbDxEJ4swei__f-PiQwIY46nDXrkzoel7i8d0nHESL2UkWOfmxkdZw9m6ZoTRyQ7Mnd8ZI7OCKzkRD4rfOrxuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=SjkzYty4rQpZwjIIp4vXCifw2XvLs6__81fjmI7rRowdWZkAgYvNCz8cFSBhEX3rkBXkHSyaPyhrz7CWvW0NDXdzTrmu5TeoAJBPk1g9DL2Nsoj-uYDePasQyBxpGXf3UXzDSN9Tc2xDBUQNPh0xuHNrtOgO_xeyQaNZI3uHQC4geHwHgzlcgb0jkQzwFOQwR96wfn4_VH9Q7RrH8hVFPIPLAiXqwgzrr9JYISUi64fBsRVDMXByLJg1C5Gihbq-57GRz7ybUlGl-Y6PM2kpcvtwAu-q8C0_64h8GCozPVNy5sduxaGnJL-XAXElPxC9PwGpTqHUvHAbMjk9pindbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=SjkzYty4rQpZwjIIp4vXCifw2XvLs6__81fjmI7rRowdWZkAgYvNCz8cFSBhEX3rkBXkHSyaPyhrz7CWvW0NDXdzTrmu5TeoAJBPk1g9DL2Nsoj-uYDePasQyBxpGXf3UXzDSN9Tc2xDBUQNPh0xuHNrtOgO_xeyQaNZI3uHQC4geHwHgzlcgb0jkQzwFOQwR96wfn4_VH9Q7RrH8hVFPIPLAiXqwgzrr9JYISUi64fBsRVDMXByLJg1C5Gihbq-57GRz7ybUlGl-Y6PM2kpcvtwAu-q8C0_64h8GCozPVNy5sduxaGnJL-XAXElPxC9PwGpTqHUvHAbMjk9pindbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyHJxbFpI3TeECh8064OTgxPm4JrHOetJndyVG6tVF9rbgHVj5waPOVNXC4RvwUgs8170P89UgAOC77hfC9UuIA_y4vvcyaMi4q5EF5Awc2aSpjOqOqQydMqzHNmcTostCmJBKuHLhS3P8pfY6KyzIjPPGtIKcTwx4x29UlYpn2QX53VBmYvTS0peA_DOvK75KnbsEHThnndUA8DTzQYtYC2mlO7FDTsl_m6YFKcK5_K9qVR6Gi0fq9BsvJG2sdA8XhbK1j5tgtAhXqO1IMpGXCiM_uVHhTR6tTEs_HtSvxD162vh1CrtCYia7ppc66G2idsL5rPjXsgkRqLKRHN4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=Q-hXo42yOixWIP4GutG_eDADIuNkXELzvvaAit5M665mxw1MbzzkLHdh2DB5cOdysabzJSU0tkaE3i_Py9qvmMQ2pWFWEqGKyG7ovPtt6yjCvFh1K6c2EMrJt9XMiL8tM5i9HU8lQX4s4Pxi5Rcu4b1sqrr23nLuf4lSZ5GHMt1YTFaooTWf3amJHQ68cZGPxdImdVKZbKsac6UfBBdp3TmjO8tJ_hU1Q-jY5ZHPiHDQG0ks57ky2Y_D61KtrDx6tXf-nhWr7Y3_vZr_QJQUbaYYl7GHwD6DP5Ga08BPmXjpvnWHmH59MM4lnaWLAVLU4IeR-J1fz75XIqb7CRC55A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=Q-hXo42yOixWIP4GutG_eDADIuNkXELzvvaAit5M665mxw1MbzzkLHdh2DB5cOdysabzJSU0tkaE3i_Py9qvmMQ2pWFWEqGKyG7ovPtt6yjCvFh1K6c2EMrJt9XMiL8tM5i9HU8lQX4s4Pxi5Rcu4b1sqrr23nLuf4lSZ5GHMt1YTFaooTWf3amJHQ68cZGPxdImdVKZbKsac6UfBBdp3TmjO8tJ_hU1Q-jY5ZHPiHDQG0ks57ky2Y_D61KtrDx6tXf-nhWr7Y3_vZr_QJQUbaYYl7GHwD6DP5Ga08BPmXjpvnWHmH59MM4lnaWLAVLU4IeR-J1fz75XIqb7CRC55A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=eyTWK3c0Y1HRnZKHhOFuYuoBGhaqLSLkxj3rLqtfaBpOdR3sA52phSUKTwOTbBVpz3nnUPY4d0m6MQFLFGTm7KbHwzQCO0ieLXuUz-3RV9o-dIWk-jzVGQU_8mOWr1Ixkn891hVlkIEI90j_wtpl6DH2fY5BSI88pgIIqt9D_deuUWzu0FlrhqwEBl_Rnh_ETGyQBZBBfmvKRXD4hCi7goFvEP-jye2T3VIEj0copsImxOgiwg812RogKvImDXHvR5dJcznShkx4MxYwDYkFv9sFsTCy9KtoqrxzHMgtukFxawuHDMTtuelK3ZLNxQcordX4e-AUI_I1qEZJ2-mDww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=eyTWK3c0Y1HRnZKHhOFuYuoBGhaqLSLkxj3rLqtfaBpOdR3sA52phSUKTwOTbBVpz3nnUPY4d0m6MQFLFGTm7KbHwzQCO0ieLXuUz-3RV9o-dIWk-jzVGQU_8mOWr1Ixkn891hVlkIEI90j_wtpl6DH2fY5BSI88pgIIqt9D_deuUWzu0FlrhqwEBl_Rnh_ETGyQBZBBfmvKRXD4hCi7goFvEP-jye2T3VIEj0copsImxOgiwg812RogKvImDXHvR5dJcznShkx4MxYwDYkFv9sFsTCy9KtoqrxzHMgtukFxawuHDMTtuelK3ZLNxQcordX4e-AUI_I1qEZJ2-mDww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=mzTiUw4hD-0N700PkH7z9nQZN-V3SRbWftsEyr9leJmmFGXVhkfT8t1m2-lRJkI5atTaihDmbMVzAIQRmi7stEqoNZwKPX-6mVCppztwGtCCvMZfMwOJhcN5qE86z9-0BYzQpGDZ-4IBqLGOxBAB6loPaej4NQo03fylI5dpEKq9zaIPCLDGPCAMP-TaqCUEV-YRznZFAZPUXTGbDQ2jeV4xUqOX-WuYz-hetheWynP0RPGI2F5j35Y9M49RGwMcqnUo_GcLNBN6unLo76CFRJZoCyqU6F2LlyLDOhqifIImFO6AlBVmzJwAZDg7_rAEh1Ur_UqIWZ4eZEIwUJNfmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=mzTiUw4hD-0N700PkH7z9nQZN-V3SRbWftsEyr9leJmmFGXVhkfT8t1m2-lRJkI5atTaihDmbMVzAIQRmi7stEqoNZwKPX-6mVCppztwGtCCvMZfMwOJhcN5qE86z9-0BYzQpGDZ-4IBqLGOxBAB6loPaej4NQo03fylI5dpEKq9zaIPCLDGPCAMP-TaqCUEV-YRznZFAZPUXTGbDQ2jeV4xUqOX-WuYz-hetheWynP0RPGI2F5j35Y9M49RGwMcqnUo_GcLNBN6unLo76CFRJZoCyqU6F2LlyLDOhqifIImFO6AlBVmzJwAZDg7_rAEh1Ur_UqIWZ4eZEIwUJNfmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQELXHQjJ5wfQwU-mUP-fYBXXeWjX6zNd5MpgdZNm9uUojaGCI-22SZvy_ugW7zNAlxa-Jz-fI1KlxCOaKfZl4yOlAURSe4rS5BQ_b_nZ9B7AX03gVeYoZs4RZqW20ldQU_I4yI8gMXgY3d2sVXgbh8lp8e4_tu0WI9C9oWZu1qCbx_0V7XjKgyhMJmnGcjB2kD4HAnfEzw6NqYsqYElmFLC8V8ac-2y-7LgxAp0o2nKd1llFJcHh1vyegb9GUw13GgspgY3Dghd5-vvElqO5vc4mMWjjnBCc0jrUeHQpoHVflIFkMVX-fX27sqo0K-lymCSJ9-Xr9TOKw8spEm7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=UCHMd4wcJ4dFUIgodGw1siyGaW8kl1adXXbXiiPJrr55VMdfiSfvM13jDLcPglzROYbNx2jkRZxr2b7PUgwLhKbeyYJSAGygZie3a6QN7YQqJeowpvHVsY6foh7VACP7FdIDhCvrKtIL-Bxcrwb-ZeptD9GzoSFEc-Ql1HuTeFIcQ-W1OZUWoYx5kuOWs-glUfcBC04yds-y-ZB48hNQc3YBBRxF7MrWiDVl0wJ8OE_oP143bqB0GNebJWivkyhAMPdkh-mrxgosFeQncZWrquVmeDqJtygVS-83GQ_PE3WyOvgxPG7yTZrnWDzPJhIsHXrx3-MMu7fB21xOXn_D-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=UCHMd4wcJ4dFUIgodGw1siyGaW8kl1adXXbXiiPJrr55VMdfiSfvM13jDLcPglzROYbNx2jkRZxr2b7PUgwLhKbeyYJSAGygZie3a6QN7YQqJeowpvHVsY6foh7VACP7FdIDhCvrKtIL-Bxcrwb-ZeptD9GzoSFEc-Ql1HuTeFIcQ-W1OZUWoYx5kuOWs-glUfcBC04yds-y-ZB48hNQc3YBBRxF7MrWiDVl0wJ8OE_oP143bqB0GNebJWivkyhAMPdkh-mrxgosFeQncZWrquVmeDqJtygVS-83GQ_PE3WyOvgxPG7yTZrnWDzPJhIsHXrx3-MMu7fB21xOXn_D-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMYcIwURZq7e9_f2l63R6ZR3KM3jV_9vMNH22AYsyNREf3hAa40C_iD_f4o0Z2VkaFCZ4_72UVswInecj35bPS3M7YWMM1Tbwnpd18rBMkuypmhEWWR10Bw3S_7GXVdwAcnUASMb0P14eEJ7CTywVvAT-MFzOsoNfgpNOw94uKpnL5DBVk3Vop2MkKtzNkgPPk_Aar7wFqI1geKnUev3byFWjKwbW_cuVyItj3VGyhiNdIfLILRLQM5x9tdoBzJvjOOc81O2uyReowB_1YPPNJqC0cqmD3LO-YwW6Nt4DkYUYiYwzN0FPl5_LeZSeqn0qQTez8FtzByWTAKf4YrBVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=hl1ShLLswa3oYcAW09UP0qNustWnHZ5bBH2-z_6pI7SMf8SUC4MbiMgJZ_AY3ux1yVCZd7DdgfqMmc7j1dPhqRGKat-8oSTWR0v8mLrBR4lMDUDwJ-L8HiXdsYMQRWwSJrrn46Pue4nE3aEXBt5fU1bxmyumtPdeF-0HlFbWgqzm7v_1Dzs4P_q1fZVZ4io6V6JTOLI3j9ihI2OgmmABPUPKfHf5BV1xckTYV8bVOVIPJkyEdrh2uX5HsQDnh7JxUv1UPJbHBCMW0ZhLMbfWQo0-MBeEoU4FvRKj1IBJY6Kijo79RhwmB7UwnlEGYcyt_Emrxl4mE8f76wZp4l9xHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=hl1ShLLswa3oYcAW09UP0qNustWnHZ5bBH2-z_6pI7SMf8SUC4MbiMgJZ_AY3ux1yVCZd7DdgfqMmc7j1dPhqRGKat-8oSTWR0v8mLrBR4lMDUDwJ-L8HiXdsYMQRWwSJrrn46Pue4nE3aEXBt5fU1bxmyumtPdeF-0HlFbWgqzm7v_1Dzs4P_q1fZVZ4io6V6JTOLI3j9ihI2OgmmABPUPKfHf5BV1xckTYV8bVOVIPJkyEdrh2uX5HsQDnh7JxUv1UPJbHBCMW0ZhLMbfWQo0-MBeEoU4FvRKj1IBJY6Kijo79RhwmB7UwnlEGYcyt_Emrxl4mE8f76wZp4l9xHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cy62DuahacdLWFUgAvvhT5n0C3sX7rn1wqNOYCAuRuimVZgNisvaLDIj2X6JdwNqAEuoOaFK0MjPpUmeBxzEo5sLAFmW_rPPFMSRD-FZbOg7qviA_tv9Bp_jXQss5XRRQYTwieNr5esgbw3uinkzx-keOwnEizGgD_nRh6Ssv0puM4pOYt-lytnbH8f2mCZ_kZrK1cDBzllfbMD6G4T2kZom8ISZ87_bqhFaCpxKWkp6UKicazkbreefp6vG77MfjMwHTTSETVlXDLx34e6gJrZuHfOQM-yEAEESCkFtq-CuycDkW96Yv94Tvn9OFTtPPlbEHDiGEPqYEsGy4bYeWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=mrfMGqwf7ivzhiGudQeGzssWyL5XU8aMddGeufwDgL7fphcZWxZ6LvHDiCYSsi8ItJH09r2_IhWrj3o8K-wchaLdTWZgo93QwYNa5Hnwsnhj4H2NZ3qWkJ43IlnOczf7_ujOo4gIopUf6_fS_jIf4-B6yIVHVcPjbggpgfVSFXvN_g_mWJzewar2vM6pK5rywvBn7VlfxMuRPzPMw-s_ZAvM3KQ1EZ3dzlsP2Em7exvDIS4BxQBNB-8Bd8E7x-zOD2pCnt9O3NUCmbTjMrXI8f_s8xjcXbS4fJr6OszTnpS3GJdKZhGVyEXdPTNS-hdMeKni3Y5Ag5bX_IAr1r86yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=mrfMGqwf7ivzhiGudQeGzssWyL5XU8aMddGeufwDgL7fphcZWxZ6LvHDiCYSsi8ItJH09r2_IhWrj3o8K-wchaLdTWZgo93QwYNa5Hnwsnhj4H2NZ3qWkJ43IlnOczf7_ujOo4gIopUf6_fS_jIf4-B6yIVHVcPjbggpgfVSFXvN_g_mWJzewar2vM6pK5rywvBn7VlfxMuRPzPMw-s_ZAvM3KQ1EZ3dzlsP2Em7exvDIS4BxQBNB-8Bd8E7x-zOD2pCnt9O3NUCmbTjMrXI8f_s8xjcXbS4fJr6OszTnpS3GJdKZhGVyEXdPTNS-hdMeKni3Y5Ag5bX_IAr1r86yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gcBTbu5tQ_LYsW1ncqcVAe2SQUcB5Zvnd8rLbf9VhWGVHM5mmo-lepfffVbtMfgQ7lv3eGQudJxsLJkbDSZojJFSWlmX5s6ki2oXjgKlGRFGjj0jpa1lXdXuxKLAFLgrVrVSHK-9S7felX1z4w9PLdN0C9r57wOJbnFwu59Cs45hFiOMckLz8k8EJT1QIiC5rsGkYlDx6D8JWWeJlDlgBskTAXUivU5cvEg4gmYcVNKS1Oj71iclQATGmn0LLinUx36owhPljf6-j_tzvyBWEe5nvAty9_wS596vXBJLaCqOfyU8jsr7EdOyXNcBdKJAyfeHcBX8BJ3lD2qg-VBRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tWsSr3LAERA2545liHteDss9X6Fh4HtXQngBJLtFvuBmlCo6MPdATWT7U5vW15nqhDQ_vLhTXBmmDCg8OvRuX8ai_pmrKyKXJfPP1knUQiO7vuGt_zIhSwazcRfFVM88KySqt9-Qn8FlBl7FhRD5YFiPnjsSj4PTpx652F6nrfx6uW2P0fk0kq7eWGqLznsZKpSofUxAqL_bjzdFiqBwY8UqQ4MOwyDg-_R6GHCAqtFK3BdGUgvCBV0gh0Dtzv7UJwGoavGrwtxAXDK3hfddiQGeCjYpJo1EPLW_3HkRu1jzhxUbXtulPssDyQVzIDwk3q45AidU7LsUgnZVr396ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=icyKiq2m2QfLN2BJnTjedfPNrcnUHp2CpRWBohNKm-ut_6M6gf_13ez3DB9nxfMYs4m5eTG4p-kab3qmh85-JH4BWNrvUXnbPmNL1db-4zQIAjMnmQX0A_ofXZNWq5oZCTMwWsw7W6DjBGw2yd6w6MMiJRORFTXd5QMinl0ql6q1bnmbzuJyMWSkvC6QK2U3Tk5HJ0JKL9pgs0nmb-f4pmsHmbqPYPQo-pwnmqZZ7O0TF7KluFM8dCsfDPUyWLjypGwsX9D9n3x6qGQj0Lgfc2bP87BzU9QwzZrxUWRhH-1Xd2M5ERg3fQyzFVBGQV5_uWDXN_4EtLpsag-Iu21lZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=icyKiq2m2QfLN2BJnTjedfPNrcnUHp2CpRWBohNKm-ut_6M6gf_13ez3DB9nxfMYs4m5eTG4p-kab3qmh85-JH4BWNrvUXnbPmNL1db-4zQIAjMnmQX0A_ofXZNWq5oZCTMwWsw7W6DjBGw2yd6w6MMiJRORFTXd5QMinl0ql6q1bnmbzuJyMWSkvC6QK2U3Tk5HJ0JKL9pgs0nmb-f4pmsHmbqPYPQo-pwnmqZZ7O0TF7KluFM8dCsfDPUyWLjypGwsX9D9n3x6qGQj0Lgfc2bP87BzU9QwzZrxUWRhH-1Xd2M5ERg3fQyzFVBGQV5_uWDXN_4EtLpsag-Iu21lZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2Si91x1HJZRjryoK1MiyhfaeZ5aT9GjcMinl2mrN8DE6J3o_nOBxvSaSwg5hQ-VHjrz139cWXiziqXPGGBsWFvH959Md-UtqEVmkk6wTNgCu670sU9_-LgQ3bZXux9UlPvFzly2DsWpgXYJhxHbP-UuF6ZwgF4E5HbYwia09iS_aB_UNur5bsrv_-fPz3olkWUP95dSu4gGGu43xppW6QHHWZMbqIYAbXxXDc1vx3EyB3siNGSO7jCBT8W2HcLL-muwncwNOWdPpOioMp6ou3Mwa0Q36tGyl1wtmOIAj1gXMoGwXoPELTpdw3-rxVnYWJfA_lWQvQDKPva18mcayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPX5YjpKuWbKjT5-gcI-GnObFlpwMe59fDEY_eJnLx5mboEjWVm9N3DUw-IrPf4Q2zRE2Qk6bIUGtAgxk89ITEfuooMdOllx6iC8Golu16zeEHB_oiXwriesjrItq9bNpq3tUHbezbI6qesPrZBJboQX7NueFI8Vs5g9Q3AMN0sM3gjiA2RmWyO2zVGTZQcmL35lBGyHWsPHzTWgRZH6rK20doVv9rGMBNOkn8ubvjl40JNQdRXkHFCmtom7yiVixBHU2Kek7zCkRK3DcP-DxrmK0hsAf4NIHTUEaF6va1W4eYdJKGsA2uDRB_IZzL6vp7v2ltGIJoaiWu6YlERxJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTjhwrmmp92AAh49fKbEC1PprzDjINCXqJKmbyfVZQPEeHJnccuXS7AlbifgK99f1RN9Wjczi8Idmi-PLLB34sdMQEceNg1pP7asaIGEBTsardFr5J8MFrc1aYxTTpK4azD6iHTPidKPXfMcjkcqFJkg43tlDpOG8FnG3zWC24dGMUc14n-qbF5VCFTGdK3tp94x7dpO_6MxK6jx4smJkNK-0fJChplKKpDT_8swY8ABxhl-Baqs3mnwotOf5zi0VMqxULIZiq7_QZX5CidolEI10N7AhIMyiODmf2J0Ga-jmATJ1nGQe68JBfNOgxtsFT6LFfklxRmxQYf9HKcmiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNeIfhks5l10vF0O2glm3y8ZMGxwNudgHMRmZXCaafZ8hJ0usBrnzBdmwv23Wj3oxGHw2qexlPRbsb98z1Nst2YebvOM9qIZDdJTfXJQeH0j5V9bxY62iC00HbPTSDzsdFZC4gP4T3E_DAGlFlo3xfvbq9ntx91GyReAYPtQjlxJQugllq0TRwNjMrGp-F3721dJx-M2S387l-Je0t8dH6PIaXYSppT_h6u2lhE57JfGEYmStK42jv7JURbAnxKtd6FZC96zSQpqWeZB5WiwQSvvRHscBLRq_r2D2f34stoviW4BQtu0vnwR40Y8jUBRNR-4WZ0IFRcjcA43n4vwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vj9vXAkfF7LAugTyN7MbLg4zVLTDjGUERCtnWkWAPB6MBVY0Voy_yj7PPT9r8UjkbQ9X0bRZfTNA-052vax5QwcoFDb3GZ29CiiGTpVIyFjZZRh1-2ohe0yTxURWkcYkEXo2b0_XrwXS7OPnO9wS78zGCPv1_3pzrm68eWe2fePVnga6UN8EMu6ug44b_Em-0usJKltC5wjVxardziq0NLexQ-xTZuoHZe8xNF-Q3rQrgTwMc9W9_ubDXO67XI0B4h0E6kTMxayVoPmccdTzHrOiiqE7Tmre1_FMdchuBc1ezhEFDkCoc1imPFWkp2mwcleQ1wp08ls234ZkcM7teA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=Wl4m5FgxaEHSYjEO8qcxUWfnAqIJZDMmqQTVIAvSDNy_Desw7o1NgslzBH_1mMsBmWFFoKCAmYByZe7OkMb24DgNia9onJmVTTOZjHx2pFHdrHIm4A7DbrxuB8UMg-Q-QJPgP1SeE8PC-iTpqIqV1BbJEgiPiKsdn0O2lGysvJSYgfKOoB-snprYiHSYAZSpxd-0KyBYXlImN_q1wcZrvEiCNtbPbgjMLLjhRLtiXeP_UR1-QhvKvy0sDu9mqxEff0j46R0b3NbLSSSH04elYrQwhI4FxuhBSMCYG9teMd_RPrUlh9-xLxLP1hT7zRYZ96l1OCwiW472BaHe9TG7SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=Wl4m5FgxaEHSYjEO8qcxUWfnAqIJZDMmqQTVIAvSDNy_Desw7o1NgslzBH_1mMsBmWFFoKCAmYByZe7OkMb24DgNia9onJmVTTOZjHx2pFHdrHIm4A7DbrxuB8UMg-Q-QJPgP1SeE8PC-iTpqIqV1BbJEgiPiKsdn0O2lGysvJSYgfKOoB-snprYiHSYAZSpxd-0KyBYXlImN_q1wcZrvEiCNtbPbgjMLLjhRLtiXeP_UR1-QhvKvy0sDu9mqxEff0j46R0b3NbLSSSH04elYrQwhI4FxuhBSMCYG9teMd_RPrUlh9-xLxLP1hT7zRYZ96l1OCwiW472BaHe9TG7SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=qHVNFzWpMHUr38eh3ZPYpnPy_q_Iouk5NrM5_Cxu0u0FYM5_DYpsngUv8V1jMVud5eCCbrptr4AoSN3xlducuaho8vmV8OZtei4N7qlG_wQWtHEU8h03sqTzjIBe-P-HXMdR1Uh6Aj6MH7r--9YH_00gYQTVLvJiMJzgFJg6GwNzX02D4o5NJ4s14V-uSLdLcM2qtmVmyue7dj-nlC6r7842qPr_-YZmGbSAAqnNtyWUxzsGt7fcgayA5JQ66nT-iTWuX1SjfT5Ujr8yg8i6FKRLCkvv3A3hqfruIFfaCimVrzRaRZ7jDe7OYDV84Unvt_iQ4koPG4j1EVgo--_wPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=qHVNFzWpMHUr38eh3ZPYpnPy_q_Iouk5NrM5_Cxu0u0FYM5_DYpsngUv8V1jMVud5eCCbrptr4AoSN3xlducuaho8vmV8OZtei4N7qlG_wQWtHEU8h03sqTzjIBe-P-HXMdR1Uh6Aj6MH7r--9YH_00gYQTVLvJiMJzgFJg6GwNzX02D4o5NJ4s14V-uSLdLcM2qtmVmyue7dj-nlC6r7842qPr_-YZmGbSAAqnNtyWUxzsGt7fcgayA5JQ66nT-iTWuX1SjfT5Ujr8yg8i6FKRLCkvv3A3hqfruIFfaCimVrzRaRZ7jDe7OYDV84Unvt_iQ4koPG4j1EVgo--_wPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=GxrN_Cq6o_Floa7CBiKMo3kKf9R8UiLr5Qq-Y54tqclBnZVM3SuzwlTyocv2TCDQerHz1FObz6TMf1zscdwhRu37Z4v83v-Vzk4dxqxilcgJ3UkgfCeTsqKr0-HEF3ijBZ6YzELVwwNOT_k_YCFmoSYC8Ja-ExLicXT_xPXfj6bTG2riUGOyEXyRtnnG2DrE1EwpGWAR_SkcqzwY1XSIU9eTC8Air-xhlcgVZ2GPtKmYAwBKfxBMhujpitUJd6Qwp5LyER-0pTrouWO7XNzPf-bI8nfark5RSsKIb3TkyFMRbQLoCCdAFcD3PE9twarfGI-kxKWysgz2yIwOEPDDwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=GxrN_Cq6o_Floa7CBiKMo3kKf9R8UiLr5Qq-Y54tqclBnZVM3SuzwlTyocv2TCDQerHz1FObz6TMf1zscdwhRu37Z4v83v-Vzk4dxqxilcgJ3UkgfCeTsqKr0-HEF3ijBZ6YzELVwwNOT_k_YCFmoSYC8Ja-ExLicXT_xPXfj6bTG2riUGOyEXyRtnnG2DrE1EwpGWAR_SkcqzwY1XSIU9eTC8Air-xhlcgVZ2GPtKmYAwBKfxBMhujpitUJd6Qwp5LyER-0pTrouWO7XNzPf-bI8nfark5RSsKIb3TkyFMRbQLoCCdAFcD3PE9twarfGI-kxKWysgz2yIwOEPDDwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=XkEsUsucTf095fTApSVZTwJZzK6MyOvYPcIdSFlpCJlI5HQGOJm67xhtxu048MD0H8UqUaJwL5V3LvHOSRO33nTSyPbJ0SBK0ZKpm8P1Js2KK7GgkQI7ZljeAFNq4bJLypsJjm5YDsMuwykS-MfsQ31N-CcqKTHWIMXFzC8KCY2FdCO0mAgsKv-nOo-2tWSeQyBsI4zHxmiqPAEluKFMqL0bVTxTLB1e0uJaln24lyxrmZIleV7zUJdEWj9p9lrrLHyCSGlsz3a_twmvbkw1sUuCu5Dt0ftbbYRhy0dYNUASjHfa_DF2YvpAM6TeePpBSVYKJVDCt80t8PGn724d2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=XkEsUsucTf095fTApSVZTwJZzK6MyOvYPcIdSFlpCJlI5HQGOJm67xhtxu048MD0H8UqUaJwL5V3LvHOSRO33nTSyPbJ0SBK0ZKpm8P1Js2KK7GgkQI7ZljeAFNq4bJLypsJjm5YDsMuwykS-MfsQ31N-CcqKTHWIMXFzC8KCY2FdCO0mAgsKv-nOo-2tWSeQyBsI4zHxmiqPAEluKFMqL0bVTxTLB1e0uJaln24lyxrmZIleV7zUJdEWj9p9lrrLHyCSGlsz3a_twmvbkw1sUuCu5Dt0ftbbYRhy0dYNUASjHfa_DF2YvpAM6TeePpBSVYKJVDCt80t8PGn724d2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buwndjQNcM4zg6NFrl_BLUFmILXFwCp6wj18WsjMJ0epB1lk4s9Yrtq3TDbQBemyOiCPZPxxeaf_SK1r6miBMSJ_UmoLEwbOu8fXns0LMY14ar_y6b7kdpNgdWoZH2aDYiRarir54FUpzb9XO6u926j_GnV43TtXRMAHOTWdW7zVwlNtl_B-9uHeemQ47gzIY2STunSDYlo1gUYFSneHdmSe6iXJBObm0cd2NZT2k4c1q2H_XAbss89NANL28KM-vtT0cO8659GPOHDf-OFB_SrxII9rLjUyiXvTYeEgU9gxhe7vv4tp3xyHTBnrosS94PpDjuTmsYRyWLseQT-f0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGNAKvu6zn_KA_PAw0s8xcXanoYNVijys6nLLe1EZbhJc2TFYx8RXXAtfmeJx02RFsiC7DMAHRwj68xpPT7gMvrVvH6jimkJw6-hsswgmQs0whlL9u-p7sxZBl7n7-hkKoEzaVXrhBJJOrwOGhNigte_06eekZuSda2G1tH_o_Uh6HBZnlSeA0PmN7618ZCvfUMO4pfQRooo88LOERq8qx0HrGBee4SE0iYTssacB95Pxdwm1HJX4YImLCg0VDC-l1_1LGGqC-zd5iWSzIcb8kYgmU7rcuKZtKpZCKOLtedvxDKLQzp4m4LFLxwm-SrVQCgrMHpreIQSTG20l-oJWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=t1JauctB8sLvFHF_F2rtyuwZjGnua96oQwUTqxgS50s7v4zM-O46M9nS0T5g72CTLC_N9xmczS-ZyuncpuJ1G1PhxhUavMekLA7DWtfAl9iDSenY5LWOQlaj_uXBJme9SEkBkm3QGjaIdVUV0Uky-itqEr3s-gjfP36j_PzLjhgN5cHEWjepmBwEr4mNoP8ovNQGugzFVm2XQb5L6-CxDyf5HlCTRHb_Em-NDegM-3ASreONL-hgYS5cxviI4lY7oc9PB-TUZxePgaGjvNqFuSdRI1ZFh7nvUwVcpTgAEfX-EwcrPofeC_juBEh3RsGh-hZM6JW5IFJ3lJSdpHK3nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=t1JauctB8sLvFHF_F2rtyuwZjGnua96oQwUTqxgS50s7v4zM-O46M9nS0T5g72CTLC_N9xmczS-ZyuncpuJ1G1PhxhUavMekLA7DWtfAl9iDSenY5LWOQlaj_uXBJme9SEkBkm3QGjaIdVUV0Uky-itqEr3s-gjfP36j_PzLjhgN5cHEWjepmBwEr4mNoP8ovNQGugzFVm2XQb5L6-CxDyf5HlCTRHb_Em-NDegM-3ASreONL-hgYS5cxviI4lY7oc9PB-TUZxePgaGjvNqFuSdRI1ZFh7nvUwVcpTgAEfX-EwcrPofeC_juBEh3RsGh-hZM6JW5IFJ3lJSdpHK3nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti59tljuyKSOoilp_BG1ms98SMqkZEn0RZAZVbf7KHsPmFdT0dxTeg5rxhrzEgfu1IeaaKS2OPPXbBVzql-a0ult9grvkbp75BwhyUJAGJeEop3fNTQ-CcfABYGgyBeDP5roo_2iqv5Cxiz9UMdEJDbhY0dKvZzTjH8XybxfvYMSuRPz-DiWMAokLA8qPb9GE6oMCe-AwriszuX2200lgZE8JJ_kwM9Zjw0Hncyi_Nci8iQTtj5XmZcUjJEfmguH4LWF4r8WUap4YFdTsPTvpFd7OTS9gFL4UQ3u2AW2wAhmZnEt5vOYJvAv2r0EdOgVP8zwb_HoaZXcPoYii2vEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=eSilpRjSKCOpoMQo0RvvsNT3jfZgPoegXv1mxqo2-auduZKLDi3QUUzNLi1zSSar4z0qANTD234gk9wMO4ccwNNF0S7odzt2lWUT79QBL6OWmERj4OWL4PXUZccKdS2dqbYDcJ3TwjPOj7PCQjD5wHPr5DWj7cSab3ZJnm-qJ17Zx9AjkbDDsQGHSfSf9BboE-jiGJObv5vfyQ2bUq_z_ysifcqfFJsaefwfUDbSbk8PROo35SK8iUzSxuOvPxiu1ols_7tPfoQVopDlkUPo2Co0mxL_iGj67zXTmPuVh1OGxsIEVoYQ3kUKsS1woIWjk_QD7Hgq_0shE2_qOZYyTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=eSilpRjSKCOpoMQo0RvvsNT3jfZgPoegXv1mxqo2-auduZKLDi3QUUzNLi1zSSar4z0qANTD234gk9wMO4ccwNNF0S7odzt2lWUT79QBL6OWmERj4OWL4PXUZccKdS2dqbYDcJ3TwjPOj7PCQjD5wHPr5DWj7cSab3ZJnm-qJ17Zx9AjkbDDsQGHSfSf9BboE-jiGJObv5vfyQ2bUq_z_ysifcqfFJsaefwfUDbSbk8PROo35SK8iUzSxuOvPxiu1ols_7tPfoQVopDlkUPo2Co0mxL_iGj67zXTmPuVh1OGxsIEVoYQ3kUKsS1woIWjk_QD7Hgq_0shE2_qOZYyTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkPVRG56YWYzV8ek6TEvaglgFtSKnTZFYa0sufmxA73Dd0tyXHEji12bR5ucQIUiBaUVUqXPSwUD33I1xkZuSvhPRP8z25lqaorYUAFy5wCc83AUMteuS3gpyIf6ccMSgVI2K5bGq7VkXGwDuvSTD2q82RsngkRNk5GIf7ZaK1xGDL_rs18G56pk1BeCEIyCDY2vdRza9COg2qveOqM4uFKSKCnaGHCvhVZKY7wslrKtd8hdDOg6lqgs34hMSsjeWNPb8NCUO_sXrd87zkQFzWh5aBU5hgyQssqaqdGXb0mbsruAr9NyRWweS-l0RHik1wz-MjYeXMxFmlPM7NCdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSETRf5bwefgEFlhogs62RyHvxtaZc1bO4PEOncU1lUPl69lkVoW30bKLcGOCutrpyAE-WZzVJiWEDKmRnNDMz6mAA396vNwUXRxk90zebrViRcaHMOrfhwcmu6E6TtePROTxh6Wjc1-bxwKs8biX6ZKnkNBD-oRx_oHrJh6KPQ1P7rHac_3aQrLPFVuq5zM3FOb0b4fPRWEQD2w5iVI3ZKqFpnGEzC3RDR6Wk8RaE1Sz31a2dngdQK3MI8QcY3n8M-GQSyr-NoZnbBEjm1irtbMTctzvV3_M0IYVGSMP2V3bPfl9yrfl5_aYAveirkOa5hDuaKL8ZzBMsFCvcIV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=HeadefA5pl6A_w7JR7-sA7Bp29VShxyBo2wXrM3J-mGxd2NOQ_UfnzrLwJ7bPnlx9PPJI29ClKFEcuUAgK9zMOn0fx_wOdf40yDc5c5g8NFK7A4xmoK8vTT6sfmMwaYr5S-8bF5TZqbWlBg5JNMf8TnyEINTvmTOXqbeE94Uic8n02Ruum3TGBwBWJ2nxYCr3PaeBjmnLetVWxJJuxtRzvrjaZaZSLI8iDhU-EKZc5pVHFaQ0a-W6ADJUuenC7a-1s1K5tCJ8bdNz8DHccAJgFDFZ2N62z0bNUMSmnwmUH_FYrkuD_D3QCy6ZNrIupcVw2AMLgA4GtikHpjdeCj0VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=HeadefA5pl6A_w7JR7-sA7Bp29VShxyBo2wXrM3J-mGxd2NOQ_UfnzrLwJ7bPnlx9PPJI29ClKFEcuUAgK9zMOn0fx_wOdf40yDc5c5g8NFK7A4xmoK8vTT6sfmMwaYr5S-8bF5TZqbWlBg5JNMf8TnyEINTvmTOXqbeE94Uic8n02Ruum3TGBwBWJ2nxYCr3PaeBjmnLetVWxJJuxtRzvrjaZaZSLI8iDhU-EKZc5pVHFaQ0a-W6ADJUuenC7a-1s1K5tCJ8bdNz8DHccAJgFDFZ2N62z0bNUMSmnwmUH_FYrkuD_D3QCy6ZNrIupcVw2AMLgA4GtikHpjdeCj0VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=DP0ACZj_QnKtTtFc2UjU6qasc2Q84zYyhIMe7XDPF94tNRhdBR6LJoSPN2ojIf5lgG20EldLmbp1OBdQSojcReczAY2QBG4Yq5K9Qk1crcIJ8SQgVMHVdZGJasOX2GDjpmNnN387W8U-phiTYTNXylxo9yOsnoUwTJN3RYtrutnXiKfKV6nBLdebet-C9O0gFHYR9HSF8J0m5SZe7W7sfY4MBAjopudPPgBkes56LwRHZupcViiO4qgnnhksuqiur7_SHO9dOHfYugJLPZyvjdyzCnr7yI9SOUobMj4slrilEXIcJbgEel2HdtocYhnoyn6i2hX7D_Yj1CzEQZhW-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=DP0ACZj_QnKtTtFc2UjU6qasc2Q84zYyhIMe7XDPF94tNRhdBR6LJoSPN2ojIf5lgG20EldLmbp1OBdQSojcReczAY2QBG4Yq5K9Qk1crcIJ8SQgVMHVdZGJasOX2GDjpmNnN387W8U-phiTYTNXylxo9yOsnoUwTJN3RYtrutnXiKfKV6nBLdebet-C9O0gFHYR9HSF8J0m5SZe7W7sfY4MBAjopudPPgBkes56LwRHZupcViiO4qgnnhksuqiur7_SHO9dOHfYugJLPZyvjdyzCnr7yI9SOUobMj4slrilEXIcJbgEel2HdtocYhnoyn6i2hX7D_Yj1CzEQZhW-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
