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
<img src="https://cdn4.telesco.pe/file/r-qED9ip7t5T4c2EZgXJNTemCeDcAdpL0hGyDhPNMyfWnI1W7r97Kavmpsp_MZvkGhTp30Bgn9-VTa1FqJd9tHCT4909gjxXvoGbPyqRZ0bzAHNhuLoe39YUXUv1T3r225eDorbY2Q3sYEECZy-rlK36q_zXC3Idxm56xhA5QswCxSVcv0c8DBD89qwz8kHyew4BfMZaExzDydPJzae6x8GXlfAhEYrbuil6BSuXu2EXAv_M9KPMhPWr5dGiyhU0GjgXzuaUTGtMSMBj3qFlu-L8DkE5jAiDz7vzYfAYI9Q6E1RvZy9ZumeePktdmcM5Pgt1Y1WOzILG1INATMnxZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 15:01:28</div>
<hr>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=DNmSOXTG3y-XgDwrmJ2arRPU_PyIi8BdcunbeBDjA-QXd_fQTWOveH7KbnhvS29NoIw87HNsn6CRa0dwdl-J8vqnpq9snwZgyVQ0ZOZK3K196WsIkyKkTYaLKhOwgpLQ2vPyNPXq7KDt6d-RUgwIDKA4qZfwTdZGnoYO7kEus5U1kxHw7Lfs8jmaq1U7uJqeOI3vB-y3g9iiO8EHT_p2zWpjEo1FSv58d9DH2rz5QkYzD1mpQh8c1t2jaOcpxi0QkoqrVrqOkZ_t9JcPS4UcmDiirw4WaPcdrmfWVQOU8EXo1M4REMEWTPdzAOLhu_unOQ3tm66V_w1sYaFSuC8Z2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=DNmSOXTG3y-XgDwrmJ2arRPU_PyIi8BdcunbeBDjA-QXd_fQTWOveH7KbnhvS29NoIw87HNsn6CRa0dwdl-J8vqnpq9snwZgyVQ0ZOZK3K196WsIkyKkTYaLKhOwgpLQ2vPyNPXq7KDt6d-RUgwIDKA4qZfwTdZGnoYO7kEus5U1kxHw7Lfs8jmaq1U7uJqeOI3vB-y3g9iiO8EHT_p2zWpjEo1FSv58d9DH2rz5QkYzD1mpQh8c1t2jaOcpxi0QkoqrVrqOkZ_t9JcPS4UcmDiirw4WaPcdrmfWVQOU8EXo1M4REMEWTPdzAOLhu_unOQ3tm66V_w1sYaFSuC8Z2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=jFvMtwsXd5Y9ACL3AIreIPdQV0p__WzXjOrXJ_-3-SYIEjpo-8Yg64Q3ykMFjsGkxVyt58uarJdrwF8r6Sh_IKevYtATM_dSXbcO3aRTnZopqMdm6LqwpC_8ffOpg45zzZqfd9w_QHb32jvxFmL6oKaoor82HyznYJK8MDDa9MM40jNztl2Q1B2nuHwwvRuyysdU1YQoyjr8YPqq4-EzQMT2BjeO4IINaLjOH7zNCGWA01WFh1ba5DDazqahSJIrQRoNnRpXP9WQU2upN6m2S57jrNqQ03Z9CKExeBFazrDqS2wF4Ujt3-7cfmn-Dckdja92yyb-N5Nm2R-l_9w1oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=jFvMtwsXd5Y9ACL3AIreIPdQV0p__WzXjOrXJ_-3-SYIEjpo-8Yg64Q3ykMFjsGkxVyt58uarJdrwF8r6Sh_IKevYtATM_dSXbcO3aRTnZopqMdm6LqwpC_8ffOpg45zzZqfd9w_QHb32jvxFmL6oKaoor82HyznYJK8MDDa9MM40jNztl2Q1B2nuHwwvRuyysdU1YQoyjr8YPqq4-EzQMT2BjeO4IINaLjOH7zNCGWA01WFh1ba5DDazqahSJIrQRoNnRpXP9WQU2upN6m2S57jrNqQ03Z9CKExeBFazrDqS2wF4Ujt3-7cfmn-Dckdja92yyb-N5Nm2R-l_9w1oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZEQJuVbcnqNZZHO7UjFbF5c5Wp-hZh70i1mON0nwPJXiyT9kPyasiGoUW0T9g6LNIIN6IHGZfBK19KjIs9n-UBY9DyHOfS7SahknXoobdxk9rAgcUea0wnNeB_--HjjeqccWRSaiKopHyS19n3_qXwB6Kf2CFiqqXo77mT9Fzeh_NUY3p-SFM-2bPYbnSZAERGxRt9l2cu2KPHotFhcEQlnjRwB_SmQGrDMLs4k2IhBJVIIxHbHhEy8dywxrSY9cN8bRk7qIOYN8GwyfWa-HAItdZNbRxnfVacjPfv5K1SK6kgh-GqspnwCMbtCo38bFPtZZCBgwmF2Sy4MsqnXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8HSUacRiksZ0-hN9dc0zJ_vnM1H2m-vnF_vIEtKrHuAHNHQHItXauMZMnCYGr70NCPZu01di4ds6cXcuf6359WcBiX4io2AjME8FoWlZcknLDYC96oI7bjv3BJcIB8lHEx8bHGScn4M8NaXbUXxagd_F1oIlyotdD5eHXVN2fNgJT3WhIU-PCyAiJ1MYPRNR_AYlV8nv175EhtneMTZOjxTXKxQGXvRwf6K3OUIUTyxl7jbR0NcclAsp6_cqVdZmLzY1f6Fu_jSsCawQEe7KMTDAGf27C0b0r34zFjdHajGIF53GhabsLlYYiYi5M9dWKNPkyGTMy--1PVV6tqEu0qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8HSUacRiksZ0-hN9dc0zJ_vnM1H2m-vnF_vIEtKrHuAHNHQHItXauMZMnCYGr70NCPZu01di4ds6cXcuf6359WcBiX4io2AjME8FoWlZcknLDYC96oI7bjv3BJcIB8lHEx8bHGScn4M8NaXbUXxagd_F1oIlyotdD5eHXVN2fNgJT3WhIU-PCyAiJ1MYPRNR_AYlV8nv175EhtneMTZOjxTXKxQGXvRwf6K3OUIUTyxl7jbR0NcclAsp6_cqVdZmLzY1f6Fu_jSsCawQEe7KMTDAGf27C0b0r34zFjdHajGIF53GhabsLlYYiYi5M9dWKNPkyGTMy--1PVV6tqEu0qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ARPRWX9Wj0TsmDf1-MN8c_EKsxPJAdqoMIEav8ezaij96uEpcGpwdnuWoLiyXqThQ1uHF4PAHlLujhTP4q6S7LJTAveG5rV49tJMpblJfrgOPsT2Us6rDMGBMB646sGSlWqQ3t0HAi-IneXWiLmArDpuWAdhmsPDKMErooFUvdby2ylVMWTdkMX9MourW_Izbr9HpuzKRkFc5-I0e_6sl1a9LgosBtCBQdmvupzg0dNwgZCwHt3dkDMdW-xr7R0bxN4kZM9fDx3w-eVEfUjwRtgBgRs9GWbHis8thHngGFIToViMdEldezxuds-3WQmRZeaug4g6-4PBBz3-rikbAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ARPRWX9Wj0TsmDf1-MN8c_EKsxPJAdqoMIEav8ezaij96uEpcGpwdnuWoLiyXqThQ1uHF4PAHlLujhTP4q6S7LJTAveG5rV49tJMpblJfrgOPsT2Us6rDMGBMB646sGSlWqQ3t0HAi-IneXWiLmArDpuWAdhmsPDKMErooFUvdby2ylVMWTdkMX9MourW_Izbr9HpuzKRkFc5-I0e_6sl1a9LgosBtCBQdmvupzg0dNwgZCwHt3dkDMdW-xr7R0bxN4kZM9fDx3w-eVEfUjwRtgBgRs9GWbHis8thHngGFIToViMdEldezxuds-3WQmRZeaug4g6-4PBBz3-rikbAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFGxaknU9gwmCHvWMuzyhciGwoBq3Wvjsi3vsfKtm2K1CmZB17mq1Oj1d8hkI4A-SXDdha--naq-8ctjhw05SJrokXf-QrRUo1-SGSg-oNlcOjLaizuMW_ukRYCU0icWyphiJ8uBmiz4OCkeCp3NI-igJlasLW1Rq8cjbqPSDyev85dYTagLTKZnty8j3U2XHpG-LVLyy_mEdTm94V6RmJpF_0B6iFbqw9i3fkthQ2Ntim_Kbm-_ZFp-rdbqiOp06xSBNNeDqb6JqPloEj4v0852Qxf17plAEj6GOf1U3H6mXfwYcObJrJF-QKuj66SXxyZoSAHItyMnkNRq-OGxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=U3iXfC8eEG7HZEskCI4LuRbexgqp_BYOBYEX6Rpt6CfIqV6QGrTTu6DC7etc84zPnUnL0jxdb2_3BFX66pXW16NqiUfkLAKqbtWnFHm-ixpYdT1HfdViZg4oQiQtlTvP5sQL_-Xq-lpBRSgxJAw7mR1BP-I3qt_UPAL8H_YAXAaZNOCkDEfQQpKAAl9tWsBrlIHzyWQaNRgEULhjZatv_DYSNvh6QjgfWRSvLM3bvX1-pkEwbciY8f38E6B8i9fBy92Ef9jf5AvIAPT5QbCYCTk62dn52ghbbbbPi4GEGmNSu9i_FhtF_hSrFQ-_dv4bUorPefvE7s_IeW_QOqPtNx6yTcGEAo7Xh5otA83jjQQLbXK8FkRvEhc8LmnrgL3WjfZfCX6wpr51v2qxSXoBAL5pNIbUTya0tjUnmp8sAsLyMPC3Ly_oBH_Wj1N9IX9y9aotORB5uLaZHhu1K2SlieXdQ2o694EEE8OGMLewwPExkui77EseTiuF8CeKBNkEQXPz7zUcTIG02rKxl2c458blRi8LekoS6TLwuJf1GWNuvc12f5ZQ4oZW4g1ZvAJrmE36DT2TmbPaGEq5SEMVgCghMOgevUgEYPfHB1L-006hkjEFgBuZbRx-eMXVY9x0N6XgTGYGC-i2jhhYj7QKU4NCGythEc_7JNs44likxFY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=U3iXfC8eEG7HZEskCI4LuRbexgqp_BYOBYEX6Rpt6CfIqV6QGrTTu6DC7etc84zPnUnL0jxdb2_3BFX66pXW16NqiUfkLAKqbtWnFHm-ixpYdT1HfdViZg4oQiQtlTvP5sQL_-Xq-lpBRSgxJAw7mR1BP-I3qt_UPAL8H_YAXAaZNOCkDEfQQpKAAl9tWsBrlIHzyWQaNRgEULhjZatv_DYSNvh6QjgfWRSvLM3bvX1-pkEwbciY8f38E6B8i9fBy92Ef9jf5AvIAPT5QbCYCTk62dn52ghbbbbPi4GEGmNSu9i_FhtF_hSrFQ-_dv4bUorPefvE7s_IeW_QOqPtNx6yTcGEAo7Xh5otA83jjQQLbXK8FkRvEhc8LmnrgL3WjfZfCX6wpr51v2qxSXoBAL5pNIbUTya0tjUnmp8sAsLyMPC3Ly_oBH_Wj1N9IX9y9aotORB5uLaZHhu1K2SlieXdQ2o694EEE8OGMLewwPExkui77EseTiuF8CeKBNkEQXPz7zUcTIG02rKxl2c458blRi8LekoS6TLwuJf1GWNuvc12f5ZQ4oZW4g1ZvAJrmE36DT2TmbPaGEq5SEMVgCghMOgevUgEYPfHB1L-006hkjEFgBuZbRx-eMXVY9x0N6XgTGYGC-i2jhhYj7QKU4NCGythEc_7JNs44likxFY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGQ25xHYuGqxx5XG-OhN7BWblOYCwamlc9pCe5zbXF5-DmjHupko9kROhz-E_2qOyQ7jbQ6do8Y5vRjz-zMJxIVBC0LRjdBY6DjpH-5eDaGdqHTKjakJw04J_78DS2f_u8S_ykevdWG02mJdpOT5VuJf_17J8ElimJFWv4eL0_Y3xR6u_rJNgzJ6lKRJIrS_khHzFhczEH-2i-xtNDKQjHNU1Gmcka4VFvlFxPBhe-vFeovHFO2QE_Kn6koQM8qtMJXwTb_zTdocIxq-wX9RWg8kLZ9pQA_xZhB9qCuB1w7m5LRmhIIxt8wTzFuadr8f2_qtdn07zjTRRUWpEYvbUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=LlLQV72wfcJr59HYExyj__Fn5OM8Yh4HsMBtLKlYUY1ZZNwWwTp1tEAgewTtFmyNGW3BrdOJuGYLx2bbJVUl1loYwTZlGPr7PyCEX88iuU9z6ix6bNi7sj-YLhHzS1zSpxx8IcKTiwmhOhilEyk3kQaWQAl-f91qxMQJzD9aPw0RmTuYEDO0snzh4VSOrr3PL3mQdN-zz4t8_9oqIMq-cUKxluIp5qcYVx1_DvOoD6okEj9zqDdVxOo6RnumOVfHSasQw9QyILp3faz9pjJuJgGuCcdv8rtVp54124C0sNzRjnrT9xAyp-0tz5eum5iZorDreF1DziDuLfW6o61bTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=LlLQV72wfcJr59HYExyj__Fn5OM8Yh4HsMBtLKlYUY1ZZNwWwTp1tEAgewTtFmyNGW3BrdOJuGYLx2bbJVUl1loYwTZlGPr7PyCEX88iuU9z6ix6bNi7sj-YLhHzS1zSpxx8IcKTiwmhOhilEyk3kQaWQAl-f91qxMQJzD9aPw0RmTuYEDO0snzh4VSOrr3PL3mQdN-zz4t8_9oqIMq-cUKxluIp5qcYVx1_DvOoD6okEj9zqDdVxOo6RnumOVfHSasQw9QyILp3faz9pjJuJgGuCcdv8rtVp54124C0sNzRjnrT9xAyp-0tz5eum5iZorDreF1DziDuLfW6o61bTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0aywzT_-GzwuS-25mi_0go9TbrYsABFIDLG5_fKZJKw3ldMd2vtzyuR6a1cYEs4HyFKCmu5xkgmWHGm-hBJDPvRVBrri5iB5aO9t4LE5QxgtoP-3ykIltfWQGeDiazeZovAYir7RXhaSogRkAqtMnSBFS-e8paGxP-d2lN-lV-yQrhxXacNBelER5tGXdSIkLdUZKq_Sp_pSQYBzQHcHnto6y8s-ITaXKwQjO2AKvE3cGLYwtx96h-7z4piCDYzOQZ2qQlDuT4N4byUDUvZQTVXLgUGPu2tYKthtaZU8gaXoCbF6Eg4l5GArzaG-2nFYMC_CGRIEvAS7H1Y9RiqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdS1pykzShzR8CEFx8oTl2v9K90uDjr79lde4OI135cV2n5XqcXgZzfrTxGNQmLKEr4H7iCydu317EoA9gt6pnQuZvbBjpFLkAZLA_DxWz_NJU96N-YNJmf5eSvAyW41kkG6QvQw0qr_cD8oQoIfbHtISGQVioqtXXGTeVmhi8UtFrqRqdlH4y2ttyHiuppjv2Q4puTedYS-CEn-YM_dNy6jaaqzceJJp756khn9xy0aAbNyC0SbKdY0dyRj883jjGuOvcRykzxSBVfQQ0K9tmmMCNwNCyD2ckPRdLJuO9kWQYvEUBxDgGUktti75SCfPs33KYJD7LIHakqo_ozJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wda1RPKY6KjADHUeSAR7DU26uW17uhcJiQTEoCUY_o-hJt-vZwuLLGBDVVnlB6wbNom6KrdSPiOUiQ7SxKBcXXsjqxj6JMQOBGFKvuwMtZ5lhf-qRN4_ZQbyXvaOf3MM30d31d5vSNHsSDYgJy16HsdOtbj5W0onrotCdfIu5VqEUxYmndUd58PwVGxFk3cgHRw2yKhfGDX017U_K8aug6cA_pMZSaNzCzdnfMDAQ0UoTYq7dLZV7TeGrpWhsb3uS8pQAw53FrHnWe2-bFuCql5mt268wfQpiBknZniwaj8WYvo35vaCoYPO0raAh2bMSojQcTV0y5bJ6XjWC0ixVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=fV04MyGAGxiUHSTZQ6LaV55MrwUubk7HF6MkluqTJ1qDe9QtFdFS3-WrL8xqfc_1FaJOgR6ImYoBL6LEFH4aGKGR0ZHM372TepTQpaAectQBUw86F4hbsjs-Nv-pghR7K1L5RE40LsTc3k1YUUqHixrRZIFVIwpQfTy1q-IBc8VmniD9xcmygieQSm-9fSELLQw2YxD-g8VolmER13dLRj1peiBmgP8jElOSDi7H14PAYbQCnqowzg-Jhz4q6NRBV-vwJ1xQfiSPOftK-7ZpTPNkGl_EHA4H0j_NNNAjGcgoNrJAArjAXXmCSLbkzseLbEkRsxCtpXkHvALcOdpeqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=fV04MyGAGxiUHSTZQ6LaV55MrwUubk7HF6MkluqTJ1qDe9QtFdFS3-WrL8xqfc_1FaJOgR6ImYoBL6LEFH4aGKGR0ZHM372TepTQpaAectQBUw86F4hbsjs-Nv-pghR7K1L5RE40LsTc3k1YUUqHixrRZIFVIwpQfTy1q-IBc8VmniD9xcmygieQSm-9fSELLQw2YxD-g8VolmER13dLRj1peiBmgP8jElOSDi7H14PAYbQCnqowzg-Jhz4q6NRBV-vwJ1xQfiSPOftK-7ZpTPNkGl_EHA4H0j_NNNAjGcgoNrJAArjAXXmCSLbkzseLbEkRsxCtpXkHvALcOdpeqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8Vow2FjnUqk1KK7Y09RtNGlHvYhkTHKyIsujeGN8pngecR9nRSBLHakrkJjmP_tUWYFplSicxf71LMnHfXYJMoE-FLPiG9m31JlDX7pepgQ-g0_HvqQ_-T4tM0nWqkRPEbHuRx_mhz68wJy27YQmKA7CEmoBqT3K_Kfr1N-eyftNClWCwcna7QpXnomeV23eh_73JQA7wiErOJlz4wM8gxXmC-0FfaH5vjST99QzRuejsrs4sTEIRRMsv9srRLcUd2-3f8UJH3d14LSYVF1dP6Rg6VevBxLJlk7z5GeoWvae7n1kjAS88AJQ__m3YSz2YmRWVuJ7q6zLWn7mtbAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFFG7AdiGPZXgrzlLpRVukn-QUnD0LWieZl9MW6-dqac5FvCa-6Zba4BDgwxUDFLmAEytszV4krn2pIktKsJcTW_uY1d8JfLcNczUiREtb0Ggjr0iAk5-MmYo2pNWwGTK8_yj8VJxW47E1PBaSs7UCqvsXlZVPtkaGCCo4L4Jez5H6w1lr9iQYD860in7n3emhWw0WZGaLokTQgrqwXynO17ltQcaQpcJ-BkTesI--WArABBqxKhp_OMyaeFq9Dyw-7oqofKq3iStNoSNTf514lnglGJrAfYe_MHI3DNL6EkPElbVueXFEVuLMM-sMQMTgBRqToHrAkMwIZNBV2yBc8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFFG7AdiGPZXgrzlLpRVukn-QUnD0LWieZl9MW6-dqac5FvCa-6Zba4BDgwxUDFLmAEytszV4krn2pIktKsJcTW_uY1d8JfLcNczUiREtb0Ggjr0iAk5-MmYo2pNWwGTK8_yj8VJxW47E1PBaSs7UCqvsXlZVPtkaGCCo4L4Jez5H6w1lr9iQYD860in7n3emhWw0WZGaLokTQgrqwXynO17ltQcaQpcJ-BkTesI--WArABBqxKhp_OMyaeFq9Dyw-7oqofKq3iStNoSNTf514lnglGJrAfYe_MHI3DNL6EkPElbVueXFEVuLMM-sMQMTgBRqToHrAkMwIZNBV2yBc8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=V_WqmxdkQ--PCo9QTnlPP3vEfz5zaJWr0Ffu4EgzJSVd8GM1QGLfz4L7PAIXn1N1KZsrQbT4vkFHTKOIhRWpceiPuvq9MvehPozAjByDp_27A3vv6rFx44kjT7-9eszl6DQ53ezeUnnEc1tuize4X8NmTChyg1sh0STCeQr_K_4-_m8mLEc0pn1VUnjv5d0zXHzWoziSeNTReDjjTXKmWqU1aWaUwW7SFjX7mou0odpczs_G5PbYQyKYb5JYxb8KvEUzP1bfo50lOVf8hZcc-hmV929Mw_Bmp9BTmu5SMhAD-zdcz9M_HLBFxFT8cA0weqL1TwViXfyBKCHWQn3xpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=V_WqmxdkQ--PCo9QTnlPP3vEfz5zaJWr0Ffu4EgzJSVd8GM1QGLfz4L7PAIXn1N1KZsrQbT4vkFHTKOIhRWpceiPuvq9MvehPozAjByDp_27A3vv6rFx44kjT7-9eszl6DQ53ezeUnnEc1tuize4X8NmTChyg1sh0STCeQr_K_4-_m8mLEc0pn1VUnjv5d0zXHzWoziSeNTReDjjTXKmWqU1aWaUwW7SFjX7mou0odpczs_G5PbYQyKYb5JYxb8KvEUzP1bfo50lOVf8hZcc-hmV929Mw_Bmp9BTmu5SMhAD-zdcz9M_HLBFxFT8cA0weqL1TwViXfyBKCHWQn3xpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=MDOB3e7RKhWFAylfXllPtcaAi-67PuPmMxglMtpjurct2BJByPrUAD5pCZt7vdQ5qai4y3GF2mVod_YnaITQIklPAO6U_0lB7BqJK5IADYuvql3_Sey0jJPpjObzLz2pBLobtpwysZlh-hcHfuvVsIHuOCwYgxIV818pJj8dYOd-M4ssGmErcf_7A37P4LhNd9xy1f70WsCeJVSrFQinSdRhpR7oJ3eUqO5RIhYozmDDvjFDhsmQoJarfewpw1xeRxXMMwGY6z8wSwa5mz18SsQlDXuC3iZYhu57pV-njxvr1pwd8cb-A-v0Vg6Vz8AYfhT6hDqZwoVqaVGDIH7Os6GEX0aeKo6I548Y-8mXxa32LBzoem3T3VXbv2HCgk1UN00LCY2bjvCCcsqJY7nioJObRoFJJpJqf_LjIUUoUt4TgeB0MrLsqMPdjM270vOjH-5tXgBhPQDw4BfwGb3QV5rVdXkDWuRWb6TKzdwkoUvsraht40bMBPdXTGcb9hm24yXzSPKPMpxnYYOEDKqL_2GUjFPHgbvdH11KDWheUAF0QiuJs_1FYNOo9bjHCbZvwfM0dv653JWvcDOJJPZ_LIAZ5iMoCI6SkP9gqSiTrZIVvCk-7UhLZmFjz61PNNv2ar735e3xqo_G54zCd_wEpndtuVy18ogI8DtkTlnPc4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=MDOB3e7RKhWFAylfXllPtcaAi-67PuPmMxglMtpjurct2BJByPrUAD5pCZt7vdQ5qai4y3GF2mVod_YnaITQIklPAO6U_0lB7BqJK5IADYuvql3_Sey0jJPpjObzLz2pBLobtpwysZlh-hcHfuvVsIHuOCwYgxIV818pJj8dYOd-M4ssGmErcf_7A37P4LhNd9xy1f70WsCeJVSrFQinSdRhpR7oJ3eUqO5RIhYozmDDvjFDhsmQoJarfewpw1xeRxXMMwGY6z8wSwa5mz18SsQlDXuC3iZYhu57pV-njxvr1pwd8cb-A-v0Vg6Vz8AYfhT6hDqZwoVqaVGDIH7Os6GEX0aeKo6I548Y-8mXxa32LBzoem3T3VXbv2HCgk1UN00LCY2bjvCCcsqJY7nioJObRoFJJpJqf_LjIUUoUt4TgeB0MrLsqMPdjM270vOjH-5tXgBhPQDw4BfwGb3QV5rVdXkDWuRWb6TKzdwkoUvsraht40bMBPdXTGcb9hm24yXzSPKPMpxnYYOEDKqL_2GUjFPHgbvdH11KDWheUAF0QiuJs_1FYNOo9bjHCbZvwfM0dv653JWvcDOJJPZ_LIAZ5iMoCI6SkP9gqSiTrZIVvCk-7UhLZmFjz61PNNv2ar735e3xqo_G54zCd_wEpndtuVy18ogI8DtkTlnPc4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=jYP-yCOOKsTlptQnvw73_1UC4G33fjQVcu9K5QRlvs3r4f03YiK-7V8Rzu18Hk454Tkgeqkl_EtMrxiu-cZXjbUzm_wbW4j5pV3MhSoZICEvpCrrTOLToaBwyNIlNJPSpsYKWGtzAb9N4RgpfGFRUBOzTy2t2HLc4M_oyX9P9RxyKOXlkfK_OIx4YbnSOwIoiZLjYoQrNuqI767ZfQ29wmqMH3W9tAo0o3Kl9yXF0Lvo0zZlWVaaZFC8lLqBGZf3MxL7JE_9XEtLdnitR9x-wuGq9qkRRZE43uml0lYIvddTDZ1Vt_WBbiONPPPEkmYX5kgDHnSqhiUckIzcFoTObg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=jYP-yCOOKsTlptQnvw73_1UC4G33fjQVcu9K5QRlvs3r4f03YiK-7V8Rzu18Hk454Tkgeqkl_EtMrxiu-cZXjbUzm_wbW4j5pV3MhSoZICEvpCrrTOLToaBwyNIlNJPSpsYKWGtzAb9N4RgpfGFRUBOzTy2t2HLc4M_oyX9P9RxyKOXlkfK_OIx4YbnSOwIoiZLjYoQrNuqI767ZfQ29wmqMH3W9tAo0o3Kl9yXF0Lvo0zZlWVaaZFC8lLqBGZf3MxL7JE_9XEtLdnitR9x-wuGq9qkRRZE43uml0lYIvddTDZ1Vt_WBbiONPPPEkmYX5kgDHnSqhiUckIzcFoTObg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5GeYnN5czxPp-Ctts68tl6unqIclhPI0y0cTOvn7GQ3X8yd5PsjnxojohoK4-PYXvCTwLdHiYwPpFC30Ms5qJzXkvnw0OcbQsyHTpiDOeX6E7j4mEnIUAHNs7vNlwqMZaSELE50-d5FUbpOfMV9VB__uOYYRtElHkunF0VO4w0-i1XtHjF5vWNq5TSJuMRQoFQ1i_mR-cO7C-p32wXkrUlnXSs4VuUj0vEk9Pun-hOadfWbdf6Uhi8Wf86xOACb1YGq6wbMQDFm1XueS25yCh-VKq1jQEHuhWTpOi7MNL19oyHDEi-ZWJbUVzCfFc78n6qe5ehVAsP4pmMkPwxMRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=pZBdenjiZPW101MOC4DXyTa6YIrrGR4AuZS5aOvN5QBf9-CVWP_B80Ipuz8s1jh79gFwVzSjjlvQ45i9XLIZoQlHx2pyUYQJVGUkY-wxKFrsVOOZSwbU69BSeKk79yD5IOlgrkmOVx4fsVjVbct_q5WBhP1Dn1YYzqv-ygzmCr8f55FWt--0eW5_UDhl6wk_-L14IpEfH4sUT9Mihlv6JtZ8UK4lRKZeuWnuw7ogJlUcYlfpwk54I_biGERHNxts3c0UsNGo0COTQYSJy-8FNnyYA3bXcaGsU3eZ7wQJRXbP1nJMrbyhOjy-LB6jMUK4sXvWhnQ8YxixSx5ridTVOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=pZBdenjiZPW101MOC4DXyTa6YIrrGR4AuZS5aOvN5QBf9-CVWP_B80Ipuz8s1jh79gFwVzSjjlvQ45i9XLIZoQlHx2pyUYQJVGUkY-wxKFrsVOOZSwbU69BSeKk79yD5IOlgrkmOVx4fsVjVbct_q5WBhP1Dn1YYzqv-ygzmCr8f55FWt--0eW5_UDhl6wk_-L14IpEfH4sUT9Mihlv6JtZ8UK4lRKZeuWnuw7ogJlUcYlfpwk54I_biGERHNxts3c0UsNGo0COTQYSJy-8FNnyYA3bXcaGsU3eZ7wQJRXbP1nJMrbyhOjy-LB6jMUK4sXvWhnQ8YxixSx5ridTVOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=n_1xhKVCDvsA92nv9vtJ8lojLnyRNZ4CeuWcKVXRWuEi9kKXLX1kJp3PpG5XZ47TFzr0Yar6AptQifIZCUlMJ0LVGi_0rU1qYtQupCAVerqjfoslJd6zsyAFZ_b78f-jf4qZS_RStnClRPjcS2pz5Y5r7MGete2Tb_-Y4Jy3ZYo9YlstD4m929vCtB8iyNZRZ8B_IiyPqQ6UtxzLBuJR91KCsYahVkbV_h5Xsq_V8JENbI-oLs0Vql34gRDjAJl6NaKA_KxAaGCKT5hCel-Zqd8ru3sa0Iz_ctoyCNVIYjmWCC7SoRLI1K1LWFibgxd2oe-pkepdIUyOu2R6SwYaG6vw62E7K3omxaOS65ND1POULvJiUopEbGsoRZbf1mnmzkcogI38bzYBNnpgkwDQecHgURMPqetY0LuNu_qvKPcMfOFquh1xqoBBBmgu74-JlIGiiMvbpECQG_L5Ch0I7comOiHAfudOXMVUgrf55Xwdw08DeBASoUZhp9oa8Fw76tReJQiD6lfH-fbEP1LyJPG1snLfzd_qhL95MLaRKjTAKBqrDUnv2spOUJ33IRDWuzbHZiZ3fHersL5LqVy3OPG7Pl9LT8dpSy8i_twTKTA-PuxMd7esTkw9DoCKZbltozGVu-sOsqlHWxJmwMpyMYfsVLyEXPVCA_GffZb6xIo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=n_1xhKVCDvsA92nv9vtJ8lojLnyRNZ4CeuWcKVXRWuEi9kKXLX1kJp3PpG5XZ47TFzr0Yar6AptQifIZCUlMJ0LVGi_0rU1qYtQupCAVerqjfoslJd6zsyAFZ_b78f-jf4qZS_RStnClRPjcS2pz5Y5r7MGete2Tb_-Y4Jy3ZYo9YlstD4m929vCtB8iyNZRZ8B_IiyPqQ6UtxzLBuJR91KCsYahVkbV_h5Xsq_V8JENbI-oLs0Vql34gRDjAJl6NaKA_KxAaGCKT5hCel-Zqd8ru3sa0Iz_ctoyCNVIYjmWCC7SoRLI1K1LWFibgxd2oe-pkepdIUyOu2R6SwYaG6vw62E7K3omxaOS65ND1POULvJiUopEbGsoRZbf1mnmzkcogI38bzYBNnpgkwDQecHgURMPqetY0LuNu_qvKPcMfOFquh1xqoBBBmgu74-JlIGiiMvbpECQG_L5Ch0I7comOiHAfudOXMVUgrf55Xwdw08DeBASoUZhp9oa8Fw76tReJQiD6lfH-fbEP1LyJPG1snLfzd_qhL95MLaRKjTAKBqrDUnv2spOUJ33IRDWuzbHZiZ3fHersL5LqVy3OPG7Pl9LT8dpSy8i_twTKTA-PuxMd7esTkw9DoCKZbltozGVu-sOsqlHWxJmwMpyMYfsVLyEXPVCA_GffZb6xIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZPRKHtY1v8_efXlmQrcKvW5xRnXf6etgLyHWJBEJLgDIO8ZWis4Nprr4Gmu7cSTwRSKLkr-Uw5WORvVVoaInzNP1TpLswBkgVGYIXVsSgfo_7zfFpUQGofCHKSpjKetyyb63R4ddCiX8QeAsm4WsmTmTXu3abupeytXxHqwfwAKTF-OtH8gLq_oyRuR7EaIgJw8tlifojfe2wWT6AxYOkJ3-agoHk27hIFT5A6s2lrKOT7MnxZMT-E_PvlGh5SNetNJDJjO8TfvxP1-5Q8KYGQw9fsQ43QICpQMcR5pnpUak-jzRAXh7pYtSUmA0v2JakpEtn7en1RTZbOOqVYBhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Q6nQS24sm1vRxKyxGJ5t2zwfnfl5HHe4OyCQrh6L8IkNPaofAzRiEIWcTLmm64R3cuWPM7MAFBrXQRTu00YpACvxjOkhe_BZR6DgiNnoCcMBWGj7XoWJNjPmjOAcN_7LyeF3uqZGYQ2NlIhZXspDkqvGNHHpuhuUyOQzBg4Nyz5q0A9qLzgFty8KTQHRsAtcCJVnwiQvl9RFUImGl5xW8bi9luH9R9UUsauHIzzShebSMjb9sicvg2xK9y-fbGtqI8bUUihWUGBrqzBmcts8t75vcwwO7LfRYpmzDu1SnXMnql05J-3bwBb0tScuNH9ToO5HM2xdHynAonunx59wiHc4xEhr79_MgJ1piwNGV-SyR7CzXrfsy5eM3jcNTTCBucGjeqIJ7b-kEdi5yM3MbW6I0TgbcSP1Td5C8bJsQlEh_zmM49TRxKq0TS5XLsZlGifh9chZoru_Qg1XTYTVJ9pInwlMctOOQQdzT0Q2pufgFGvROXqbKRQbFB6tto7eOgrvIO80JdcSoxt9wbPgIHym2Mk0sfR-PInNINVEHNHUzasYUNwcmRlJJ81cneTE0GCLkNZNuySgMZ7-YqXudnC7cfmyW_rDJej09KBs-C73PEBfc1dLy6V9swtuqasRX80taKBi9unX_QeFHRYlvf6dIa9HsubQ1Us8l5RQNLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Q6nQS24sm1vRxKyxGJ5t2zwfnfl5HHe4OyCQrh6L8IkNPaofAzRiEIWcTLmm64R3cuWPM7MAFBrXQRTu00YpACvxjOkhe_BZR6DgiNnoCcMBWGj7XoWJNjPmjOAcN_7LyeF3uqZGYQ2NlIhZXspDkqvGNHHpuhuUyOQzBg4Nyz5q0A9qLzgFty8KTQHRsAtcCJVnwiQvl9RFUImGl5xW8bi9luH9R9UUsauHIzzShebSMjb9sicvg2xK9y-fbGtqI8bUUihWUGBrqzBmcts8t75vcwwO7LfRYpmzDu1SnXMnql05J-3bwBb0tScuNH9ToO5HM2xdHynAonunx59wiHc4xEhr79_MgJ1piwNGV-SyR7CzXrfsy5eM3jcNTTCBucGjeqIJ7b-kEdi5yM3MbW6I0TgbcSP1Td5C8bJsQlEh_zmM49TRxKq0TS5XLsZlGifh9chZoru_Qg1XTYTVJ9pInwlMctOOQQdzT0Q2pufgFGvROXqbKRQbFB6tto7eOgrvIO80JdcSoxt9wbPgIHym2Mk0sfR-PInNINVEHNHUzasYUNwcmRlJJ81cneTE0GCLkNZNuySgMZ7-YqXudnC7cfmyW_rDJej09KBs-C73PEBfc1dLy6V9swtuqasRX80taKBi9unX_QeFHRYlvf6dIa9HsubQ1Us8l5RQNLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=evnGrYLYvPapGF6ZIz1al_jFo5qpYbV5VOg1CsahqnoAnhmff-lZvRP2qhijKPPMQ2vEfeOc_lLrjEENbA5XQG106_7DVJQfn6DFJbW_e7ixy3zzp9p3bgXzhnxmpybni2Rb01b_sm3LJiwjDRUIBTt3brOtS8sFU-9h9ywW19BzUzpeFEvSDlJ4mUnlKWxfHAzTgwaGUgVnO38nBYBEmPQMpMJiZTsHQBfXH_sjPlY5ink7uwrsQ3lYyxLJohqI1cfIP9WJak3PgZY5agBl03PlZNUuewQoHgMKUqq85_ILKvvbSiDQmOcYjOPde_laAHI70agGWs6RIEEMPhxKBbpczMsTWJ97EzbKX5QL_2o0S9owA6P8WoM9vgSSrJRyq3YO99Qy_BOPnMG37BXFnd5gx3tiF2r6Yvbtd3uNo79aX0vEDL0gJ1UweLtyrZsbfchXojTc163ruSuIan4pOsB8xYOZHGFt_hSf-tKqEo8etWDUT7aFGYUUcbQxOppP48KONswE3uH5OQVe2fkjVz0OCIFeVgF-ILlcm3GNsbcmiZihicMsEoqTQ5B8cqPxG2ebaQIk6PRPl37nZOcEj8-VgJftiQP5ZujxRPKkS58DYE4SA1u60dR0CUGcq_oHbmlEiOXyD7v6oY2oQsTmYFjLgmVPWA1veHJM1UxEH40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=evnGrYLYvPapGF6ZIz1al_jFo5qpYbV5VOg1CsahqnoAnhmff-lZvRP2qhijKPPMQ2vEfeOc_lLrjEENbA5XQG106_7DVJQfn6DFJbW_e7ixy3zzp9p3bgXzhnxmpybni2Rb01b_sm3LJiwjDRUIBTt3brOtS8sFU-9h9ywW19BzUzpeFEvSDlJ4mUnlKWxfHAzTgwaGUgVnO38nBYBEmPQMpMJiZTsHQBfXH_sjPlY5ink7uwrsQ3lYyxLJohqI1cfIP9WJak3PgZY5agBl03PlZNUuewQoHgMKUqq85_ILKvvbSiDQmOcYjOPde_laAHI70agGWs6RIEEMPhxKBbpczMsTWJ97EzbKX5QL_2o0S9owA6P8WoM9vgSSrJRyq3YO99Qy_BOPnMG37BXFnd5gx3tiF2r6Yvbtd3uNo79aX0vEDL0gJ1UweLtyrZsbfchXojTc163ruSuIan4pOsB8xYOZHGFt_hSf-tKqEo8etWDUT7aFGYUUcbQxOppP48KONswE3uH5OQVe2fkjVz0OCIFeVgF-ILlcm3GNsbcmiZihicMsEoqTQ5B8cqPxG2ebaQIk6PRPl37nZOcEj8-VgJftiQP5ZujxRPKkS58DYE4SA1u60dR0CUGcq_oHbmlEiOXyD7v6oY2oQsTmYFjLgmVPWA1veHJM1UxEH40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=MXjlxC13-IMelgX58Jvhr0Ghqvp6hYxepcrGoXfX10rqmIqPe3hSDJKzFCAqZ5NN4I2DgBsyRuPtNG69poIB9vmyZlWfWF71LBcRHftVAALxBbPdx6_rK-_AWr3FrFwEw2QqW--EJoPQaIeulWPYShUXmERGtk2FpDvXeIuxA4j--VINxRFtQU1ybbiRr7ihCeVFQPYpJoQpAP5TNGJO1FvDVoseCye5Bwyhtg_cIUIaUM1tiMlNczbjbCqYU_uv05tnMyNrDwaf8_m7Ay15b_J5KupcYT0XBDwwV2bsM8whWUZqcdiOoTkzi41tVTVo2yPYuF2BvROR5bWqEGcM0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=MXjlxC13-IMelgX58Jvhr0Ghqvp6hYxepcrGoXfX10rqmIqPe3hSDJKzFCAqZ5NN4I2DgBsyRuPtNG69poIB9vmyZlWfWF71LBcRHftVAALxBbPdx6_rK-_AWr3FrFwEw2QqW--EJoPQaIeulWPYShUXmERGtk2FpDvXeIuxA4j--VINxRFtQU1ybbiRr7ihCeVFQPYpJoQpAP5TNGJO1FvDVoseCye5Bwyhtg_cIUIaUM1tiMlNczbjbCqYU_uv05tnMyNrDwaf8_m7Ay15b_J5KupcYT0XBDwwV2bsM8whWUZqcdiOoTkzi41tVTVo2yPYuF2BvROR5bWqEGcM0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=hf9ijN-DEjWHlqdF6bamHBNWWn5c9vBgMH33MfbDbvsW1RK5sQipK_6WZs5QGyrM91OofJ16LSA5CPjpuoCSVPW9TfAMwNcZu4W0G3Na7YcahpU_VlA5INMVm1Zi1pp66VcqdP-YGR-LaoIGZbzWgxIrrsK9RHCToxcrZX06cCuGnWiQMYxa2Wo0loUWWfpqGADvZktYNvjTL3vCaIlj-WRfk1oO9SPNz9O63CsArGO7o93jSmbb_b4YJqRuZuXEm8P5bpZTqj12E0Vi61RJqtoMZDAqs0YNNo4aan2cfvBL4imSWiVZHHa-IF_24wz930QR3OQcxnOkMzHTeRTSvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=hf9ijN-DEjWHlqdF6bamHBNWWn5c9vBgMH33MfbDbvsW1RK5sQipK_6WZs5QGyrM91OofJ16LSA5CPjpuoCSVPW9TfAMwNcZu4W0G3Na7YcahpU_VlA5INMVm1Zi1pp66VcqdP-YGR-LaoIGZbzWgxIrrsK9RHCToxcrZX06cCuGnWiQMYxa2Wo0loUWWfpqGADvZktYNvjTL3vCaIlj-WRfk1oO9SPNz9O63CsArGO7o93jSmbb_b4YJqRuZuXEm8P5bpZTqj12E0Vi61RJqtoMZDAqs0YNNo4aan2cfvBL4imSWiVZHHa-IF_24wz930QR3OQcxnOkMzHTeRTSvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=bTxiqZHPJVoIaEssbocwRKEqcWKKsX7brHl0coxVIOq2UBYax9pzSqWwCuzzwT-XgAeUzSvhcL1pB0q7IeD3I0691EcmuyDLmN20_YbQ9FXK7MFNrvX-OuueyT89Knc0fIbQ8Tw3K79wfPxryMQIvHKKm47_wvbPGDe7hHEVibuDsECLrDjsuVWP-6Cg2t4yTCD_e2Tgod28DRNbFY2afpHeclR2wUtkjLTiIhuyJ6TfeF6lDASIoYipHG9o9as4t6jcYG6c2rb0PFNaYtz5-DQKiZ4fxnZHl6krACPry2h4e8-cLcj7uFyo6ojS_sKFZ70L-MaSQ7eQfnYst5vf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=bTxiqZHPJVoIaEssbocwRKEqcWKKsX7brHl0coxVIOq2UBYax9pzSqWwCuzzwT-XgAeUzSvhcL1pB0q7IeD3I0691EcmuyDLmN20_YbQ9FXK7MFNrvX-OuueyT89Knc0fIbQ8Tw3K79wfPxryMQIvHKKm47_wvbPGDe7hHEVibuDsECLrDjsuVWP-6Cg2t4yTCD_e2Tgod28DRNbFY2afpHeclR2wUtkjLTiIhuyJ6TfeF6lDASIoYipHG9o9as4t6jcYG6c2rb0PFNaYtz5-DQKiZ4fxnZHl6krACPry2h4e8-cLcj7uFyo6ojS_sKFZ70L-MaSQ7eQfnYst5vf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=lltshX09G7rnYe_-uGViPhOg2apV51quVy2iRE1dcd7vpFxYpJ9McDaXoKjkht4A97Ns4_vqyHXP3VZC8ydlpXI8xJ7HpD8pmWvjEgsInO6Npm4cU645pvhkwzxBNFR4xsr-6CYOjGYBuF86EonhHkmTTdEDri6mYgxHoOXAO7dDYUTOU8DIeLC07oDyhOGQaBAHa053eUXbe6BcAhKKHlp4PQJ-bfaJ0vsSSMHyDdRG1w981kgU-BsyYJzQz-zBg6YVJOB3_oU1s0oKW0tUAcQlKsHqWx_vmEg8zwgkoxuwTpSwY3qDxkQrKUAaI1pZ_uHhhsoTDtZOEyRXlJHmBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=lltshX09G7rnYe_-uGViPhOg2apV51quVy2iRE1dcd7vpFxYpJ9McDaXoKjkht4A97Ns4_vqyHXP3VZC8ydlpXI8xJ7HpD8pmWvjEgsInO6Npm4cU645pvhkwzxBNFR4xsr-6CYOjGYBuF86EonhHkmTTdEDri6mYgxHoOXAO7dDYUTOU8DIeLC07oDyhOGQaBAHa053eUXbe6BcAhKKHlp4PQJ-bfaJ0vsSSMHyDdRG1w981kgU-BsyYJzQz-zBg6YVJOB3_oU1s0oKW0tUAcQlKsHqWx_vmEg8zwgkoxuwTpSwY3qDxkQrKUAaI1pZ_uHhhsoTDtZOEyRXlJHmBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=dW-LyNScj-wuu_zCjSKjEUW_V86e1Kpr_UZElCNvpPe_Q7qEzysyw0drHTHjlsLMCKPKYJiEP_WZl1iF-nhE2m3T5c3vom2SxTscDJgEx1fqAiRsohWNsSZg39tI0TRl-sMn3pbPx_c_P6volxHwtaAxHvi9uPoZ4f_TwpGK1JiQQvqY80wEJQNTdMdlJ2MEws-6X04smv-CFlQL9YlQuQkGGSKJYtWiPGWVrxq8P7BVsBXNFbZdg9HGbBp7-PR_5GTirGtNmFQ0AFEw6eN419aQ5jj1vkzX34AwpHyi8CGzUOwP5eQ_4LVMLgyNTNmYcb0SOys6sRDEsH1ljHjAaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=dW-LyNScj-wuu_zCjSKjEUW_V86e1Kpr_UZElCNvpPe_Q7qEzysyw0drHTHjlsLMCKPKYJiEP_WZl1iF-nhE2m3T5c3vom2SxTscDJgEx1fqAiRsohWNsSZg39tI0TRl-sMn3pbPx_c_P6volxHwtaAxHvi9uPoZ4f_TwpGK1JiQQvqY80wEJQNTdMdlJ2MEws-6X04smv-CFlQL9YlQuQkGGSKJYtWiPGWVrxq8P7BVsBXNFbZdg9HGbBp7-PR_5GTirGtNmFQ0AFEw6eN419aQ5jj1vkzX34AwpHyi8CGzUOwP5eQ_4LVMLgyNTNmYcb0SOys6sRDEsH1ljHjAaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=jZGtabkkNbBWxLb00nIoWk2xtr0I73QzTVifp_zbNnCfpx6FGqOyMiE96jMbbZD0epreCA6uUBsFbeRg0qjrCKAcEtFqOceydn7HpurxsMIsZTr2uX4MH_YJhlHSl7hHkiWJNYYSa3_i58U4YKkeps4l4FHorgBxGu714CZ-mIZyL10IRxFFNRxk9lBmCL43mADGQqVZ9cmIxmH8ygY9pd6GWgUNCzOKn8iTzOekqa2MnBkt8VAN6l7HLTu_AqNKHSdIitvAOQy0lGzPsXfFFJYw43XqN4TpFVWrk87j55UE1q51zRUW7fDZ1C4AMCUd-42iHolMQW9dVmY2LSq37w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=jZGtabkkNbBWxLb00nIoWk2xtr0I73QzTVifp_zbNnCfpx6FGqOyMiE96jMbbZD0epreCA6uUBsFbeRg0qjrCKAcEtFqOceydn7HpurxsMIsZTr2uX4MH_YJhlHSl7hHkiWJNYYSa3_i58U4YKkeps4l4FHorgBxGu714CZ-mIZyL10IRxFFNRxk9lBmCL43mADGQqVZ9cmIxmH8ygY9pd6GWgUNCzOKn8iTzOekqa2MnBkt8VAN6l7HLTu_AqNKHSdIitvAOQy0lGzPsXfFFJYw43XqN4TpFVWrk87j55UE1q51zRUW7fDZ1C4AMCUd-42iHolMQW9dVmY2LSq37w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=QAS0N2rBOKVh8pD7Shcz-dNr1m68I4LEJFFoFvbOJwV5LXMlA_1nCWdQZSPYiuHLb1csi-sthqKSiucVXa0pj1inqAOZ2VzTMLmyaQum1FtPG35azanWr1E6bAbEYlloHEXBlA3PEJkLynQypsGNTGM1flUmCEH9Zlskn-ZLzOvw16ansnjQxz7A6ZPq45ay_S7gWjB0GOx1QsxTVSo3GK1ix4kTqNK4r1MqtKDC0fzUocUsWEZ-8Jp__BxvLhQrZRzumOIMZI0M14leK16bq6iFjuUmqlr5RJ3biGNG0eDqsqssPugSzqABsr_AtGzMBqSTTwbDoIj4izzZcb0HSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=QAS0N2rBOKVh8pD7Shcz-dNr1m68I4LEJFFoFvbOJwV5LXMlA_1nCWdQZSPYiuHLb1csi-sthqKSiucVXa0pj1inqAOZ2VzTMLmyaQum1FtPG35azanWr1E6bAbEYlloHEXBlA3PEJkLynQypsGNTGM1flUmCEH9Zlskn-ZLzOvw16ansnjQxz7A6ZPq45ay_S7gWjB0GOx1QsxTVSo3GK1ix4kTqNK4r1MqtKDC0fzUocUsWEZ-8Jp__BxvLhQrZRzumOIMZI0M14leK16bq6iFjuUmqlr5RJ3biGNG0eDqsqssPugSzqABsr_AtGzMBqSTTwbDoIj4izzZcb0HSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENoa25QAClgMz_q9VyCVR88Soi-U8YmBQCKd2V1EXG2Popcx61HxWniUs-SbZiedRHd8h9e8LR9QfuPzZKwr-f096G04Ozkdc4oi7kqxpGASBoIhXMTxif0iLJuzFNmseAzwqy6rv-RRAFKjKMCO8tJGE6Ah7O9qnZ2THOoJj3EADciDyRS3hUQLer8D0wNFUPR3mclkLsyYMDNC-i2VRCy_L5TKDSrOCJ7zgAr9mvkv0yTJ5CZnTpu8oERj6e4J1HFKnqaKHUQi-h9a3d7GL9HSFUDwyeSLpwnVeLTdgCF2jdKeHDxNoWsuoHL1PIPpR7AqZoc4IzC-4ILduBIhQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=iuRQaWm8mHV3j-mSg2hiHQPIdn2CgxssUjEajO9U_StFNBlkbq05P_moLk_jMudbhn60Mxg4RqLepKfHYSFU7r4hBbxARsZOZXnZe-r6lNwbJ1ugWRMFQa9llljAXGyzVFGGT2niGwMszR_FqDKGc3D1AVQfbxFLz0bpFKdTFq2a37eKEDUAdwpIFrSZOFyJ64eo71lR_AAPEdFb-cnib6uDDlSGprvDAakqefIeBR7rIstj4fNm2QLd_Kt4HzX6XmYUFm5_jW8tB_9xuFw4jxrzZBnZtpmj7zqdiaalMFPVY_VdxndQ4_R-7275MP3UM2boWvu_5DE3iubt0TaJYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=iuRQaWm8mHV3j-mSg2hiHQPIdn2CgxssUjEajO9U_StFNBlkbq05P_moLk_jMudbhn60Mxg4RqLepKfHYSFU7r4hBbxARsZOZXnZe-r6lNwbJ1ugWRMFQa9llljAXGyzVFGGT2niGwMszR_FqDKGc3D1AVQfbxFLz0bpFKdTFq2a37eKEDUAdwpIFrSZOFyJ64eo71lR_AAPEdFb-cnib6uDDlSGprvDAakqefIeBR7rIstj4fNm2QLd_Kt4HzX6XmYUFm5_jW8tB_9xuFw4jxrzZBnZtpmj7zqdiaalMFPVY_VdxndQ4_R-7275MP3UM2boWvu_5DE3iubt0TaJYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=k9sG2WSUYXHqOeSj6yKqIYDADvpxJhc-Zs4taS2A3-xKTQ5Mw4osI5opwkxfBxpcblFRJr9GFwJtmJaEVbMqdRtUW65Iz1v75adcclxG4E2MSQfwPhT3QUGct5x5CMz6-KxyPlpkuISMdPDhbsr8IrxsHDNDXtZwrfJS9OvAlfjl_gwGOmuozn9iIlcSdy6fekM7jZ-xs6Fj-9QZK9Ud16DIEdvvBIBajAZ4fHdhSSCfqKOePe2vNlgNdoGJZ44Ap8JqAcDTTur4Ci_bZZ9Kfa65k0ABiDjlmSqheg3NFdGZe8BPojNnv2DWZzHzcoHAH_iOr3gAMoX1IgJ9Tdwsog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=k9sG2WSUYXHqOeSj6yKqIYDADvpxJhc-Zs4taS2A3-xKTQ5Mw4osI5opwkxfBxpcblFRJr9GFwJtmJaEVbMqdRtUW65Iz1v75adcclxG4E2MSQfwPhT3QUGct5x5CMz6-KxyPlpkuISMdPDhbsr8IrxsHDNDXtZwrfJS9OvAlfjl_gwGOmuozn9iIlcSdy6fekM7jZ-xs6Fj-9QZK9Ud16DIEdvvBIBajAZ4fHdhSSCfqKOePe2vNlgNdoGJZ44Ap8JqAcDTTur4Ci_bZZ9Kfa65k0ABiDjlmSqheg3NFdGZe8BPojNnv2DWZzHzcoHAH_iOr3gAMoX1IgJ9Tdwsog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=oA35LdkBp2WB8mz4nfIubTwNh9QWCdYZUE0Um83QbZjxPkjjmCQWSbJPqtjCyA-zBNvtbk5RcxDovV7SknIqMakQt65NkoyoUF7sfpevw8dFPFn6C_55VffFsnSj6o_6XU80fRvOeil3FA3FfLuMqTJo9F-W043wu_QOl4uEeqpMIYocGwb3T0IIhPzCvJvwd5TdlhQx_m0X_7xvtUUyLT3pv6cGq_mgkCS7LZxaV9OG6DlyDapXdrP1uiuRGFQuNSX7pjMFVKZrDulFZSpRluok-b0RvGIhdW9eLZ94JooUxEmSoWVPhCLwjAIFTPnXkIeoUx8qUMwZaGw_IDq_cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=oA35LdkBp2WB8mz4nfIubTwNh9QWCdYZUE0Um83QbZjxPkjjmCQWSbJPqtjCyA-zBNvtbk5RcxDovV7SknIqMakQt65NkoyoUF7sfpevw8dFPFn6C_55VffFsnSj6o_6XU80fRvOeil3FA3FfLuMqTJo9F-W043wu_QOl4uEeqpMIYocGwb3T0IIhPzCvJvwd5TdlhQx_m0X_7xvtUUyLT3pv6cGq_mgkCS7LZxaV9OG6DlyDapXdrP1uiuRGFQuNSX7pjMFVKZrDulFZSpRluok-b0RvGIhdW9eLZ94JooUxEmSoWVPhCLwjAIFTPnXkIeoUx8qUMwZaGw_IDq_cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=SQ5nFg4Wx7UBxFpXOMbij4PkzORJReDg59ZTXIweFf8mLpvdj0BUCss-gdd8r97orlk_97ob52LcfR3rnzsTkcIrSllkOUSTWGDTRtCmU5a-C9gxfig8hOq2HFQtnnE8DOG5cGLwM6P8o5qOWAwLxBZvGZjcEbbbc-31tVbxUCkCU-Nu6lIKZVkzKscTqLaLim6EDO_7GDV5WmHljOhR8U_QgNclZR9mMpk9NyVY_mIy-qAr4AhvlTDDRf-fBuUAP9BH5UkTiIYMh27zufglJyavQLhZZEkz6rEndKbWk6FXYhD7r3qneMW_3dAkVNVgcVB9ebaqTQQwx59tti_V7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=SQ5nFg4Wx7UBxFpXOMbij4PkzORJReDg59ZTXIweFf8mLpvdj0BUCss-gdd8r97orlk_97ob52LcfR3rnzsTkcIrSllkOUSTWGDTRtCmU5a-C9gxfig8hOq2HFQtnnE8DOG5cGLwM6P8o5qOWAwLxBZvGZjcEbbbc-31tVbxUCkCU-Nu6lIKZVkzKscTqLaLim6EDO_7GDV5WmHljOhR8U_QgNclZR9mMpk9NyVY_mIy-qAr4AhvlTDDRf-fBuUAP9BH5UkTiIYMh27zufglJyavQLhZZEkz6rEndKbWk6FXYhD7r3qneMW_3dAkVNVgcVB9ebaqTQQwx59tti_V7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwDDwJ2fb-vjn7sEd1xjuoY-fGsatxr6YZyxf60xzlVMHd7BFML6g1bC2-wT9t6e9_HQYkv2NyWAF_4BiG1LDif4ZGenYncg4GtoCfYsprkSTY0-YQ-Ttlrl4cZA9zA5wIXbH3iibetgvTYvK-kvG9v8m6HWqaduLpOhVLV4xT3iQmCfSwp3eWi28bTIvJEmG4wl-r59K-nnrQrjWhnQ46cjdMh_9JIeb17PGRdX0WmLfQxRjwE-MPbVw6Xvf8gh5WGBzLwmJQX2RcxHHp0VzuRx68toRlzzyVz66ozuUlvYYvUCXc6Bj72vhH58FBHDcwJnG1bgQepB887fVgiPMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=COKoeWmiMEq6wlylXYbnUrnpnx1AW8v4l_bJfQUtfjfVKh7-yfPDel9VrX45NaEm_67W9TWkePnkKDNKiZMsje3M91tzv2EpfEOiokY5_j3-nNUWBVbfLAHuOXPVr-PeCBEo3YDc5JxizWHk7stSATFoe6LR7bnA3PkIzfTtgMW8qozgVcvZfeiZjJF1b2PPbF8FUa73JYjOMDPUS0L4pHL8VhTe7pmDGEl5ouQ7ek9NWN9I7zMwVgu3gA14QZMHm2vm8TCDL7IBMa7KH6dKPtAnu4BWxvvbqOtOjT61GRyNun7dWMTNTevUKpE9rXds-evtOpJ3ua0VcqPFvhbP7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=COKoeWmiMEq6wlylXYbnUrnpnx1AW8v4l_bJfQUtfjfVKh7-yfPDel9VrX45NaEm_67W9TWkePnkKDNKiZMsje3M91tzv2EpfEOiokY5_j3-nNUWBVbfLAHuOXPVr-PeCBEo3YDc5JxizWHk7stSATFoe6LR7bnA3PkIzfTtgMW8qozgVcvZfeiZjJF1b2PPbF8FUa73JYjOMDPUS0L4pHL8VhTe7pmDGEl5ouQ7ek9NWN9I7zMwVgu3gA14QZMHm2vm8TCDL7IBMa7KH6dKPtAnu4BWxvvbqOtOjT61GRyNun7dWMTNTevUKpE9rXds-evtOpJ3ua0VcqPFvhbP7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=J9B-LjKU2q0HGBoiLgjP2Vr035hg5sAuviX1kA_OjoozF6WEFyI90wQKOClpOXRxfWd751Y0s25p9jzycbvawTUbENiwtVrr1NeNJb2y9MFkzMxvWRf_jk32XLR7pPxbDJ6L4mySADdcP8V71niiSUDPCUZjeyergMAYVTvSCyQ2vQ-vxniBfKENcnoIcI0FCkHJmWXfGswR41D9So4Edt0XrmTHkC5B6JgdH13CoT0_iKvDEoVEyAbKWB8gbvM11BiJBZ4bfS-q1cAmtD6LC0XVQgpf7wgliTnj3KxhA3cAqtpzobL4iieKiaJYYsNkXakSA1FBnAxzFkhkmBb6JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=J9B-LjKU2q0HGBoiLgjP2Vr035hg5sAuviX1kA_OjoozF6WEFyI90wQKOClpOXRxfWd751Y0s25p9jzycbvawTUbENiwtVrr1NeNJb2y9MFkzMxvWRf_jk32XLR7pPxbDJ6L4mySADdcP8V71niiSUDPCUZjeyergMAYVTvSCyQ2vQ-vxniBfKENcnoIcI0FCkHJmWXfGswR41D9So4Edt0XrmTHkC5B6JgdH13CoT0_iKvDEoVEyAbKWB8gbvM11BiJBZ4bfS-q1cAmtD6LC0XVQgpf7wgliTnj3KxhA3cAqtpzobL4iieKiaJYYsNkXakSA1FBnAxzFkhkmBb6JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vc-A1N3W95Ejyfwc559LzZWgRUPRXiiDkbAtr4i0E8AtihEUv-vv060T3RaSLPGyGnmpSKEMw_q-rcMBrdmGDx3uLpHEj_K13R6KzzeRC9RiErKcflkLKLO-NlYVrrZgkiB507oNyz53rWIJ53klc6QSk_w9-dhBKx5jW8V9PGGLSiC46f8cc-H-mbR7Ev7HtgVIdadq_n6y1YfvYlS5OgRSVIFilGpubmgLd9Wiv7P0egoIogRSRJjc0z3vxHSK46sAW4-srs2liiKt01mczPotTjY-uUJgh5MMMsGdqAELNv5WZMXWbhUj6JjkWMg8YGiI_jlnHeYVfMPhAEj22w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFAneTc15tb58ORmDY5CU7aZjIIoRh8MS5vfelW1Q1VnBVMkba9QGp5vDOsdcIzr_7PK_BuJ6D5W2AOOHSMguAcRYyk5cokZk5YIS2XiGgJ8p0uzkYY1OZZ9aIoNmeF4d_AmZtY9yaE641tLx6TxWp3tpg6akk-vuCRBTG5QyqqBZwVu4ECLM__WY0qeOIY_0EssHz7Fls_SetINGUXGX7uTAh51K9ftFc-FfZwEli52O12bhX7ucNSDLHClDSBXQkKC4TpciXwL9BiKrx8GBURAQWH6WRPQaABKD8Q760sEAOasmxEKlYPwiI_hq13rA-0ACdF6SzQAz8TjtO1WBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=n06GYSh8Eon5U1o64RZ4z-G0_k8Wxi2au5VOau0ubD_jlsp3tXkzQEekikRmo9whcf6pB1pKHmMgvJ6POVuGLx8OCwmC0naTTMJZ6mo5QhMJDYeP7-WY1URYtQUrW50IUGgTgt93y3rCoY_OfAnu5BocAl2dWDl7O6q1EVPwMapv64ECQxauN-5Wix9iaq4wm8d5h3g4jvtE5leK251mFL16F6Uig_Td37HJXM0_ObzW5nEE-SjulhM2LYWZaHrWIePJsSsBlPvSwjPCfqv0p_89HGA5dTlGP4RksWy38tKGnfofygEtSYb6NaTnmiOt-bj5rHQBjeFjviPyy9b5yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=n06GYSh8Eon5U1o64RZ4z-G0_k8Wxi2au5VOau0ubD_jlsp3tXkzQEekikRmo9whcf6pB1pKHmMgvJ6POVuGLx8OCwmC0naTTMJZ6mo5QhMJDYeP7-WY1URYtQUrW50IUGgTgt93y3rCoY_OfAnu5BocAl2dWDl7O6q1EVPwMapv64ECQxauN-5Wix9iaq4wm8d5h3g4jvtE5leK251mFL16F6Uig_Td37HJXM0_ObzW5nEE-SjulhM2LYWZaHrWIePJsSsBlPvSwjPCfqv0p_89HGA5dTlGP4RksWy38tKGnfofygEtSYb6NaTnmiOt-bj5rHQBjeFjviPyy9b5yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwPUJAjfhFP8-gi35cH62P2TqHqDSp0zQBupEdoKQkfczuA0dnBaoF5NSyaaOtrUAXxzbazgL6Z417dxGVE2t3lxkpNuOkh3XFDDPxkqVAl6XwdWQik3zFL3_E7iR6yEKZAYMVrgdXZoa0w2nfz7f11Dys1d0UhFMkL8aoTCU2GtTZ74Kb0aj59lYTiLBUnU_hzNwkgw8JGcSF5kGoUvZY98JbN4kImNc9k7gr9PDsLsXN6sZZspHVP2Dhe5Fdm2JfSy-tGbCXQA7n6bsjDvcYjgtiapCEBGlpvPrRDnTxjKcU6x2CBcPbjSxYvKJgGCuFKRCKfcbyy6pHtU_FGDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5cMcESResEvtI9cMS5xHCPZdUUrTvc3ItMAMmjpUV3OEn3GALb6cHDlL8u1fdVl2qzowWI_34KurRUvUgMo-KlEyFo_-7yo8A87Dl6HeiarxFi9eYpif687VoSv7JNoDLRVcMox0yzDsPY_bWecVWo9XSiiigdgakFcAc4ACyvDDrQOeRuGzGHpM4SEWcfkx_KT86MqOkRoBVjYRs0NHBLkn_cTQDD8m0v9XMohCcqzCciDVNb1qS6USJpVhgCnNfWEEnZFj-J4rFCXT1QuBHdBz792hOAm3C71FlxvluONBIjsN2QlOtS8QGeRvf0CDkWtjVMeLT9oB_xvTg1Whg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwQ8YRQGVFM18xXYFveukbBZVJrk2sIbQq2_7vr_W2J8N1tx4xayFx6nkKDtDQ37jkKnGxxZlRDNeqnTuzFyk9vjczI6fg5u5nlhbjRGtSLdi0UdSAKmo5vYAbKQLbZj1vdOtN_fOAGeViKGQrt-OB8BYdFoVAxydv__nK3c_4c6TqG1ETSXwip6hbU_pbxODyyzZ2d2EUZ4e-C4Llk_TP3LXoHaZgLMxlgbUjMDg7juvGaOEviEu1nY1dWGHVoVjyRepXuneG1xN4atmhc0f-Cm1rV_sLPH6HloSIJHdXauhS137bT-5brifQ12Ta1_lD9NEzf8SaCYHXVz3UOnoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=USeVFTgGgo8K-O8qb4kf9eFvhLbqDkosxVS4Z6WY9QgEt2CfaHNfosgRUKkFS3qBiZf_io3D3ppTKBMYArk04tBcs_vcfueoIE5AocxsoxF214vJo2y_cD3xSqyC56UJz76c8j8YAhjdtVptdlAHu7oVRGb9nkBfYK9mi63T2DZuCbIRRF4Urjm8vaIiwAV5xGpz2DpuswxDDM9W6QYgt4nyKj2_mysdig37RZuHpv0hua5WJ5n-W3Zrrog1mdpIWRQznwb4mX9Cz0WkluHzgtisIBs0ymsS05q80uLyArZW2yjN4DlO4x16GX_QH0VhpwvvD9l2Rep3jvEUn8PGmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=USeVFTgGgo8K-O8qb4kf9eFvhLbqDkosxVS4Z6WY9QgEt2CfaHNfosgRUKkFS3qBiZf_io3D3ppTKBMYArk04tBcs_vcfueoIE5AocxsoxF214vJo2y_cD3xSqyC56UJz76c8j8YAhjdtVptdlAHu7oVRGb9nkBfYK9mi63T2DZuCbIRRF4Urjm8vaIiwAV5xGpz2DpuswxDDM9W6QYgt4nyKj2_mysdig37RZuHpv0hua5WJ5n-W3Zrrog1mdpIWRQznwb4mX9Cz0WkluHzgtisIBs0ymsS05q80uLyArZW2yjN4DlO4x16GX_QH0VhpwvvD9l2Rep3jvEUn8PGmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=bkJfalu1z64VRmWGUOGKLRYfKx2XnD2oOFl10cV5_LANIeQU7e5fyHeNQV14HTly-pCHcWoJYVchru1y5LYTqlS-s6ToOs_9xY-wHa5pZUaGVli9MqZxFHX_5qAIcJPtky9vMUoOWcOfK_dQQA9-bQWNUxeJVedkQYjS9GaoPuWQXdGS3PgDj8CUAtmriSUpwqbMfjUlUJutU4df4N25XazYJnfu-85q2rp3KG4MPMka2D5Mm4hAubISD89lf4-XP1NrqP0rcpEltHiSw31dAgMXtSY586zNPtsZ-4lmXJGDCeS-QfdWitnqyxWxNdX6mmoG50ZWLF0Xj5B-ErGgQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=bkJfalu1z64VRmWGUOGKLRYfKx2XnD2oOFl10cV5_LANIeQU7e5fyHeNQV14HTly-pCHcWoJYVchru1y5LYTqlS-s6ToOs_9xY-wHa5pZUaGVli9MqZxFHX_5qAIcJPtky9vMUoOWcOfK_dQQA9-bQWNUxeJVedkQYjS9GaoPuWQXdGS3PgDj8CUAtmriSUpwqbMfjUlUJutU4df4N25XazYJnfu-85q2rp3KG4MPMka2D5Mm4hAubISD89lf4-XP1NrqP0rcpEltHiSw31dAgMXtSY586zNPtsZ-4lmXJGDCeS-QfdWitnqyxWxNdX6mmoG50ZWLF0Xj5B-ErGgQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Bq19pjjeoiZtt8-0TaQ21vN9ONm2Q7K9E5TzoOyIT6AiDUkeH_w25OhXWCqrbraVmYOKF5ZaL14KTdQaqn0x1_P5UtNM4Vnh5p_olOx0thezy-cVOd9eGJfWsXsOgHLBzIN1dFmRgHeU3AZW1Xwu4GmvbOTU-ydaPuzizOLu-GS6LLyMmIXNiXUK3ezbK5fXiuC8V6tbevd2wGzsSGJgCrKfAulvvnfpK8Ge0yq8jWZzvCOldCIg1Xh2SnbmHXSHF212Onda5LwUpvJlYnLaWewxomoav8pPFnI53kdTHLwF5_FeG5nT9grXCqhvt7K9ajDyBntHDFZvait8nNe_KBUs6gur8fTIIDTllftq9CaHWk-2A9-BOWrQQhB_W2EmDNfKnrWyDy2k03Z9UcBMJ6gIw-o5Ek_DS1rQQ1syErjR6prk-wlDJf8pY4iFDimRuGc_K_1_bzxc1lKQ0Nv1E0-4a_-bXBp0edDz8uYjvAR8S0GL_0pg6jm99N1yWH9YIZvWkdQrXgfOE0AHSIF8XtF7As25BjmiMqMSMNnl_1JCiul4nz2666DFWHFe25Wd_BOCM6aG9v_jxmuOKpLyiMlziFAf-3Zp0Cah65ltRVMCNsgnINGvFd7ocStsRzZApP3_vkOx6HE67KVNzc_QjoX7zVoKm61IIvXmX9CqeA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Bq19pjjeoiZtt8-0TaQ21vN9ONm2Q7K9E5TzoOyIT6AiDUkeH_w25OhXWCqrbraVmYOKF5ZaL14KTdQaqn0x1_P5UtNM4Vnh5p_olOx0thezy-cVOd9eGJfWsXsOgHLBzIN1dFmRgHeU3AZW1Xwu4GmvbOTU-ydaPuzizOLu-GS6LLyMmIXNiXUK3ezbK5fXiuC8V6tbevd2wGzsSGJgCrKfAulvvnfpK8Ge0yq8jWZzvCOldCIg1Xh2SnbmHXSHF212Onda5LwUpvJlYnLaWewxomoav8pPFnI53kdTHLwF5_FeG5nT9grXCqhvt7K9ajDyBntHDFZvait8nNe_KBUs6gur8fTIIDTllftq9CaHWk-2A9-BOWrQQhB_W2EmDNfKnrWyDy2k03Z9UcBMJ6gIw-o5Ek_DS1rQQ1syErjR6prk-wlDJf8pY4iFDimRuGc_K_1_bzxc1lKQ0Nv1E0-4a_-bXBp0edDz8uYjvAR8S0GL_0pg6jm99N1yWH9YIZvWkdQrXgfOE0AHSIF8XtF7As25BjmiMqMSMNnl_1JCiul4nz2666DFWHFe25Wd_BOCM6aG9v_jxmuOKpLyiMlziFAf-3Zp0Cah65ltRVMCNsgnINGvFd7ocStsRzZApP3_vkOx6HE67KVNzc_QjoX7zVoKm61IIvXmX9CqeA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=QqKGEHahCzQugqYPbpAd3vksasXY2DrO1iP-MZKctTP9WxUVa0uJNILOKb3PTqOmj6uZ5O4TxEWpjA6qcIYoWFKa6pk1dLD9TQSSNs7qwZUbhH9j8OczLHqJkxMcHSP0pqb1nSSNgFTD-eiPb_qwMvCbuYd16Z0zBXo_RthVp-fz17psr7hMrA4h7QcLyBtDbj1rCteNGRO3MuOPC7KbWCpTyJlJe9sEUIuxEniaVHX1UGipQA9KSpIZr8vs8J6iW-rFUK3o8z4Y7pVh9yq9Mpmvgv_z4Av9NF7cXMS5JVzviL_MRT87XkllrKiz_wQ2zeh75N7lz7kQ8_8Q3dkVgSZZdITrEJW22YgcR97Caa16GWKkL6BOAC9ZxAAAJTGxC_QKT681MbFId9VDeexHxqQ7N3ZOs8xpO-yPIN84iuXEjZTarBkuP7CZALrdW6-4DaJJU3bI4iGE8Rnlg8H0PlAoYynF4dA3gD51Wh8TDJEfycPl-gQ6yKr05iyMPji8DNbEa1mB_lQAeCjTrYiYf8GeTsuo5m9yQLC3_a2UqYv8HTIwh4ltvLuRMp_jxryh25uVWwRoWC4uERuKYjl_QT6Zqsf0sHRPaZRFsXekQI-2SGF4pHk_VoL42VHW3ODj3miuHvg3tqefXAhSsU513u4cqKiMyJYAvGsjS9LxOoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=QqKGEHahCzQugqYPbpAd3vksasXY2DrO1iP-MZKctTP9WxUVa0uJNILOKb3PTqOmj6uZ5O4TxEWpjA6qcIYoWFKa6pk1dLD9TQSSNs7qwZUbhH9j8OczLHqJkxMcHSP0pqb1nSSNgFTD-eiPb_qwMvCbuYd16Z0zBXo_RthVp-fz17psr7hMrA4h7QcLyBtDbj1rCteNGRO3MuOPC7KbWCpTyJlJe9sEUIuxEniaVHX1UGipQA9KSpIZr8vs8J6iW-rFUK3o8z4Y7pVh9yq9Mpmvgv_z4Av9NF7cXMS5JVzviL_MRT87XkllrKiz_wQ2zeh75N7lz7kQ8_8Q3dkVgSZZdITrEJW22YgcR97Caa16GWKkL6BOAC9ZxAAAJTGxC_QKT681MbFId9VDeexHxqQ7N3ZOs8xpO-yPIN84iuXEjZTarBkuP7CZALrdW6-4DaJJU3bI4iGE8Rnlg8H0PlAoYynF4dA3gD51Wh8TDJEfycPl-gQ6yKr05iyMPji8DNbEa1mB_lQAeCjTrYiYf8GeTsuo5m9yQLC3_a2UqYv8HTIwh4ltvLuRMp_jxryh25uVWwRoWC4uERuKYjl_QT6Zqsf0sHRPaZRFsXekQI-2SGF4pHk_VoL42VHW3ODj3miuHvg3tqefXAhSsU513u4cqKiMyJYAvGsjS9LxOoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=XDgU96BJe5ewgvJXrb_a9pVBJK8JMGrBDcqjEN_NJCci-MDG15FAHzrPYZ4twg9ALiSc-T5qXfCFMz4_Hv9osWIQ1mGGH9-eG2MBzSC1RD4NT93_8Qx0uXAfhPVYLphGsg2a5ANMD1rrNrXBj2WTCaVVfWoy8sapD_FuJ7znAE8HsZjvJ_LGtjqA_fWsuhSCwzpmAFe7huNcYPh_cncR0e0QbE9Rh40TFXrdSjX6NwOMYCrrGiPbBYvl5tMXQfxdUTQln0uGvlwacrl6aKMuUO-v-_4OFNGIe7KhnKwHHfrd6wX5qKDS64xC6dp8bEGsnyUymxZjZ-MA9vBl3v00hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=XDgU96BJe5ewgvJXrb_a9pVBJK8JMGrBDcqjEN_NJCci-MDG15FAHzrPYZ4twg9ALiSc-T5qXfCFMz4_Hv9osWIQ1mGGH9-eG2MBzSC1RD4NT93_8Qx0uXAfhPVYLphGsg2a5ANMD1rrNrXBj2WTCaVVfWoy8sapD_FuJ7znAE8HsZjvJ_LGtjqA_fWsuhSCwzpmAFe7huNcYPh_cncR0e0QbE9Rh40TFXrdSjX6NwOMYCrrGiPbBYvl5tMXQfxdUTQln0uGvlwacrl6aKMuUO-v-_4OFNGIe7KhnKwHHfrd6wX5qKDS64xC6dp8bEGsnyUymxZjZ-MA9vBl3v00hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/md9b5zfcI_ESAnN9cSF041OocvAH-OYIgeaptAC0IJYxh27rUYzhmmcqOu-JPFcXMps4Qo21Uzoa0uaAUsqJ2uCF1MU-sk9bYVWcvQ-u1BWLZ_hFNCn5xJmP7ouYxL12R4m_Z80R8M3_3m6arLW9RreLTvoavn9KqhYrBj78m2f8Y0dGHAlZyLLmdU-6kapOqrQiPrFdQojfCawhgC2YW-n_26bK9a07Di4j1M7ksdMtLCW5sB66NHPpk3Ev_trW0jowR6BOd9bEYpiN503SeL735V5kq9qxgO-Di5N4hYSNnoEZXhZfIOWYoW0BmyT5vMUBXBiPct_w-75YYHOqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=vUxIglKlSlK5pD5ecmaQKokPubzDDMZxx16LKVwx__GItycG4AHUljg4M6hKLvsvBXwaGkKTbWDFcSK_szlTlnwSXlo9sPmiKc6p40E8mRn-T_hptaE5ustOdx0eG48jKWCGxmiHQPG2Najk5USOZTA4OkcGx2h6pzwBCYUs-kAob0S1DWmHUjJ2rdwphvtRgZ3cdAT3EYC0nQ6wOHGDkUvguwkfWLAbIj-c8n1q4yEoHyzhF33EQjhULn2qOdjdRyO9T2YfUw5XAILreWamDN9QRZ8FoyweL1c6ZvR1I3Q8_0YJs07TMBtWca4xWor1bLuPdRY7LMJJ1uN4YFI5Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=vUxIglKlSlK5pD5ecmaQKokPubzDDMZxx16LKVwx__GItycG4AHUljg4M6hKLvsvBXwaGkKTbWDFcSK_szlTlnwSXlo9sPmiKc6p40E8mRn-T_hptaE5ustOdx0eG48jKWCGxmiHQPG2Najk5USOZTA4OkcGx2h6pzwBCYUs-kAob0S1DWmHUjJ2rdwphvtRgZ3cdAT3EYC0nQ6wOHGDkUvguwkfWLAbIj-c8n1q4yEoHyzhF33EQjhULn2qOdjdRyO9T2YfUw5XAILreWamDN9QRZ8FoyweL1c6ZvR1I3Q8_0YJs07TMBtWca4xWor1bLuPdRY7LMJJ1uN4YFI5Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=LOuM9eTFGdfNdXpxhmF1COGDbjrimfK7VVNKv65ycdg9QctoDbzXW-UwDQKbs0lXeJ_eWGGcuT7COZv2SMFBX4NTRv41sY9ek9YHjPJhVZDt-lTDWLGMiDg3XMk6Q6xpD1mD-12_-bA0R24ymXPVOHop9IXi9VIqvFf3IxZAIl_udyDTwiAgASP-imHTSZWpWdCtVGh-oOJvarY3Y2oQ-u1RO--rX_ZLooLhj-Tn7S5V-QpVwNEX9_sxoDDjD-TuW9vWIrjjxeozdfNg70UosF8SaP9LL_cMIzUgDUPjPm1ZTubeO859uciIMhJfir8Rb4yndqyRGXUryKCxj7xRZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=LOuM9eTFGdfNdXpxhmF1COGDbjrimfK7VVNKv65ycdg9QctoDbzXW-UwDQKbs0lXeJ_eWGGcuT7COZv2SMFBX4NTRv41sY9ek9YHjPJhVZDt-lTDWLGMiDg3XMk6Q6xpD1mD-12_-bA0R24ymXPVOHop9IXi9VIqvFf3IxZAIl_udyDTwiAgASP-imHTSZWpWdCtVGh-oOJvarY3Y2oQ-u1RO--rX_ZLooLhj-Tn7S5V-QpVwNEX9_sxoDDjD-TuW9vWIrjjxeozdfNg70UosF8SaP9LL_cMIzUgDUPjPm1ZTubeO859uciIMhJfir8Rb4yndqyRGXUryKCxj7xRZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjtyUuufGn18nay_VKa5Hc8-eV-rhEcLhPbz-CF-4HBK-oey2tPBGhVMSpyTBY0Bpe5N0Sdyb7ebKOz251_Emk5bz71Kh7L7VM16FUmfL1TqP8OfPSICwLxTEMMj8Qq576k712WjJppy4unH5WYvo3m2UZFMHWuUcvtfvArNLS6Ri6k8-Ny7vrrX7WyJ3zdA6z8rNbiuTkVkaRrNhBVNBg25O3rCdPI-ZiYnPFKzcBQvywG8fqh-BeY696zID7sLUhggkIrdncd0EKq_scPQtQCgQoggQ3SB0qelO_Vmz3K22lgpU0rYSAelfHwOrgV6WryHLvcF2adgE5HzNOhlwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYkTLSci_ymwJGGRUQ-2HGQWeWkFk7XvG0eAsOg-eE5awVL1lj7k27frBcThrazQ6Ybmb10CIj2hLYXYgviIrWg0D9agAskiETx4szkYDYDwZm54HqXCBBdmehopYf1PissgC4j0W0YYE5ny6mGTfTkwnetZPiMOqYBK50VyUEyffIRSU2FQTB-yxRLutKx3AqlBfoqxyhRNwbihFalQJwk5obBYX_cmXyX1uIvJtSD8pFuTOYd57qGQ3KkiIBIW698k2VlFM9aQk8J1o_PHwPlQds-0zSjvlF7yXXORStpAuczUB7ZjjTbsB5uDZ_qizHBsPwvxBOtdvyduJ8H5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8lAXBlO-bLX3sAuAopL4OSdu2Ra_hxLu0PYwcssWsRHg765eGXlgcAk2-EM_qBUB2IY9wUbPnAoDhaoUTmo6AEPa671nt6PVwxKv6Fa13F25bAbOWRLuX593KHsRa-SQBJgLJLBSs8P4AlYIEc9awswjuGyPJ0rFhFLMEMj-x4-QmiNT3DzZuZyOrMeJcaE4DKxskjzY_myZrWLDIBSke74aibtIW3V4BRLNJrYSPxsabKOSTlI5bwz62aX68x4MggkB9CzIY46AQN-LPCmS77PULSuY9UHt8fdU9RuhFfIBwuRZ35u4chOijg718EnqgNAmy_oQooMghcoF_FAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXkn2ByNwM292ixsfG6_ofjT6YJrrNO4bMjDM7e9b5FjDwEeQBRkTjVW8samEI4vp1D7GD1wy9gOkdXIWER1GOb0BvIt9TXsVMiaYq87PiECeoGaFcZH_0MbeWOR9xS9B2o6KXgmwXvIKw1dmS2xTvzBEY3tzw9GFY-yBlMCTPNDYCgygFgvOogV3GEpCxtgzxf6adjOxdp0blT8ywrk3Jq44SjtCoYALFkyzAfHejL4GVToHnyg4A7_vtvF4stQEqbP3ujEBKZZfPIz_bQziyQu5t7YxHwfMoNnWkvaIf6Oyj5KihnEr1hcIVjg7lbbysP6SUx_jiqzamPdZSqfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TV9QL_YWZjSXFGWVMznzBhAoHTbi7cXlKZT9ztmEidNmrruqnUeraNZ1S03lfL3lmsw_pvI0PVqnqbEa_4W2TYfDlP54Hw64RZ9UwQCg5QzUsaD6efXmd0h7PgwsW99AnFRTDYVsHeNgBiwNEZdKcyn4JCNIBfzUWC39E3KA0Dl82egm5ece5ivgyABKW3XE9cWdUctRGOVzNVtnx8tFPGq3hNWkoLTz_LhAkB7_7SK9KTICEBHIH0M__3npUL9Dx5KHlUronWO3t5Cly9AgHHhVrY1u4kQVaVmxbCLbGAQNTNvdaFRFePVuv6JRExa5JUfs1sJevdRa3UjRvcQrPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6LneeQllujEOz9ZRKIkdeMz7T0nkklsxBUDyFuX9Z7n1lTlHutyL6GUt0_gLBcNwf7djn6ePCz4WkapeIYPo9h_j4xcdWwdUlAKRjsFqSkt538tWvSxqiX0fkPHUfcc75fjt3fCGi0R0Tcl1OagZq0QbYpmmklPwouPqQDziW8NYC7i-PPG_0saK5ciU2GwlvXEwxbn5vluQEd0GDffRR0ROmeBabaOisXd4MFjY-6L4xO5ueBITEVNqVqiIaF7ft4RORyV2dC3OHa4lQgUxK2YCZS-omhfHlTS-yD1J6D7tvQ_SCsGfYTCnWfGupP2t33c8-cuaIa242eIkbzyOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btLo2if_ylfQMF1Q9RENOzscOnEsPtwsl5R56P3iCW2OQ7LGuAqxMXgyoE8qxB1IukCkS9TgVi3Hd7AIBXfs6XUeqm52uA_iVYhzwQS2NL4A_9d3nvnLhJqjnfRtWGPoXvsFgUymRzz1o3mIEmYtwCwtBBiUP8RO_cZCHLpuPZE6s4ZRBAeJoxATzrDrScGczZZOfBuvu8e2aYrYYeUwPQ3H3Nqws-ib0dQJ2joXJvocQfxIZBO827zL1HJJiwSMBVHK7EkTHhXSiTN0W6P70lrlJ7hyr2atyxfNHcFz2vPvBkhS5eZgh1dgRQOS98eIjFGzz-tFqGf0uxOU88CjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jEq71AdMvWU6SCfMNFh7i5vQ_A1Hw5lx258RrYHAqS8newhQKwNlT8BW_GCI_-9qWy8oA5Gqfdiwn28CA25wha7TG0Vuz-EQk6KXgCCkkbCoZzwnzwpcJFU9wQ4hU1AbRPNq4g665kTyxitKYNt1OX8ZwkKSMz-J-rf5vBzHPdhRjiu7-bCxK46QU_F9ZtyfInBgJ6MS_zR4sb6ieXfcsgAGWt-ECm7JFCgLOijTBmOnFNpOcxRivcMbWrDbfkgxDZFnJHBkpyJ5KbwRsZ9W88QwDW2puiDEgKngjjB24baKPG7a4XfNc6cBRhhUuGiihf7PEEDorVJVMwZRv0DjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQhY3yTdofJepFsOquHTaRAAZmtPM747I_s-2kP4zPK8qe7t5_sHPMEP8KQQD9iNOkElfOCcKsFVkxCgalGI0fDZULQhk3tghL78YeZKC5rcSI63mi1cmyBJzWOiwhHJIg_RZrAiv3IbjZEj_79m5liqVjtFyl2YHIYMKL9x1voizmnB-zx7o7nfFcmDNl6K8M4E3IHvpXiUv96_WR_wZWE-Pyf0kh2VChn4XqhSira_KQ1jzM-fFNrBh7-QgC8kla53PPl7yMJdaNhfsnk01PiW89g0gHtAuakGdTRQyNNzqQX9yThSlQrxCkRpq9G9s0jriOzQVk02V_xuAN55-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t3LtlrEF6JYyU9bkrMbPKaar99iLqQOwO_78FW0_bBBoGWzsZz92I7XOLmnBTnQ5TEPM9z-8_njDJTZevumTURPpTuLCdx-UUum4xma0HGKMkN97C0DrYoTJXGoAt1KAmTo6dhGnUea3Nc-MuQTb_FED_QZufk99f1sskapli4g79MGJZBiWsZqQXvc7_vTtF_UVzI3ZA-zX6VeoxW0RoL1Q6pnomC18FHkHwACZl_GEZPoyaiaro8wJ_zjFVS9foJDMxTWLQIbkUMBxmDeXL96FqVc3NbI-koueqgYoNBuu1qMZdVZny_II_sdVA7W1etNMM1ibp7srfKdRqk1S3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=vjNbEdduTAKO7-0zTnmz3GgncfnXj8eA86RIoA5atntlQZFBXi1_1mZFLbblRlsnKszFUH2k4TNE7r00RhT0Ynh3Ai6fVGnljTcIuPQ3GV5LaMNt2BV-w34Bf5xdsIeJBMz6rE3EHBJNQ9L59U8P5lD7mL9czdiTcDqoILzhu2RGYqbHemPlmFYyxiihsrLphrww4vt_XUTB6Tk6Cgp1aM6oP7IdKTijKZjrmwA33C824QG0vujk_a-DE-080uyBNuo6I4SHib_MQ2BBf0nE5kPZlJqtQQJ7dObxrPT7oZGPfqM9-8m6gqpcyYI_pu2M_OtIqfzYHMBzjxXbLJbsEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=vjNbEdduTAKO7-0zTnmz3GgncfnXj8eA86RIoA5atntlQZFBXi1_1mZFLbblRlsnKszFUH2k4TNE7r00RhT0Ynh3Ai6fVGnljTcIuPQ3GV5LaMNt2BV-w34Bf5xdsIeJBMz6rE3EHBJNQ9L59U8P5lD7mL9czdiTcDqoILzhu2RGYqbHemPlmFYyxiihsrLphrww4vt_XUTB6Tk6Cgp1aM6oP7IdKTijKZjrmwA33C824QG0vujk_a-DE-080uyBNuo6I4SHib_MQ2BBf0nE5kPZlJqtQQJ7dObxrPT7oZGPfqM9-8m6gqpcyYI_pu2M_OtIqfzYHMBzjxXbLJbsEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTuNspmnT-NmtDt6qHRa63ADiN3tUgQjGh102flmQeseIHwatEp3Vem5QgndegdeV2ObPqRCpQKSTej-UsfS-pic9fnfYy0CBlB7-hmD4wEqsCG6PSFOj2utznxtPG4ifMiCUF54m1_CDyZkBt-fnSNB3ABLf0U2IoGL0wN56PGs4_fx273DuW_acnHpuSThwIUMFrQUUTD1omNBkxXlP7uiP47XbHLZaPtDPmNHJUzNhQr-sy_EZqYMldYzM9uIatc0eU5SzXRXM1ivSY2oKFGBfEzp17hWFSgGsEG0dDe9qkNwZrWeqeMzFoVB7TjSlPkrDTV_kb3sask_C11ntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiO7hPVUc3PruotkvZMzXzULnoAp9_C5UJBjWg1t1nXRBEjS-dHMRblv59Aw4ckdUkOvwLZ_lSWiKbj0z7QM6LA2sNkmC6yXkA1N1-GgmKGMQlzGF5hqXp5UWN-OY1pFD3n2lgi4mF-2wWJ_8c1JllAjAxDDJe9s_gITTzL93UHNt9pQMCwlijGJq4HC0AwmZvmUTBywRuo3dknurT_kapORVt1I2Ynog6YGklSJJvc8X3Z7PH7oNI6ZV61yWs-OdR8Xx_j6dcNbgWv6bKwU-ytd6ReXjsZUyTwR-N5ox2_9GF_Lr2AbwTfYnJOr5hOOrbUz2S6Nlybfv3k4FF1d5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=YeiS0Uxso4MMnWCfSY9BPmSuLDUukVAXT1l4OjVDG9lP_79PnvOzijXIdRshRyqR5sA8CSP0kDGj4nwlXB77LS1KFRENPaJJxBD-BuTqVmybwRnMX88bfF7FNAnKxbCYpyBJv94u9si2KRhjUaNtGB0UqO1L45nfClQFIMOrK12yTt1Bz7CAiRfLtOnYLqnYo6DfjKKij96WcvGmzx_9Vvxajxx2XeUhPoADZPu7CAAQy4VOPzbzB4KBlmpvcYmOFlQDtJxUxfQE5GAh1YsQTGQTYlzrhyIqwovTMS3E9gd-xVyRYYXfip6sS1eByXyvn8RHWKWAfM6NJpTiBam4dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=YeiS0Uxso4MMnWCfSY9BPmSuLDUukVAXT1l4OjVDG9lP_79PnvOzijXIdRshRyqR5sA8CSP0kDGj4nwlXB77LS1KFRENPaJJxBD-BuTqVmybwRnMX88bfF7FNAnKxbCYpyBJv94u9si2KRhjUaNtGB0UqO1L45nfClQFIMOrK12yTt1Bz7CAiRfLtOnYLqnYo6DfjKKij96WcvGmzx_9Vvxajxx2XeUhPoADZPu7CAAQy4VOPzbzB4KBlmpvcYmOFlQDtJxUxfQE5GAh1YsQTGQTYlzrhyIqwovTMS3E9gd-xVyRYYXfip6sS1eByXyvn8RHWKWAfM6NJpTiBam4dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=pvkdLShItghRbm9IzLefmOoVE__CwWUz1FKx8sjHsln6l16Fl6-_NzUqTVa4nonhUy-TPBf_jp7-hDLifcOYwjICWl3CMpJVObeN8NnTvKzDoYoZKcRnY5wfnvDU0Un6hUp3WhPSDdd5fjatqw04E79nKhNyeTv1H5KuHT6a92cwoQQbja1W1spcV6Eo9vEr270noCO3KmCefjJrJiK8YqdKIttSuRTq1blBh2uySvnu4oFQ_OCRZrziYDJtZCmg5bg1fURejJ189kPuX_QnG2i1m2xdLgcaSEI6OpysRfC56pavp394qGQsT0zUPdmq7jdS1CTm4pkbrbMNSI1GZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=pvkdLShItghRbm9IzLefmOoVE__CwWUz1FKx8sjHsln6l16Fl6-_NzUqTVa4nonhUy-TPBf_jp7-hDLifcOYwjICWl3CMpJVObeN8NnTvKzDoYoZKcRnY5wfnvDU0Un6hUp3WhPSDdd5fjatqw04E79nKhNyeTv1H5KuHT6a92cwoQQbja1W1spcV6Eo9vEr270noCO3KmCefjJrJiK8YqdKIttSuRTq1blBh2uySvnu4oFQ_OCRZrziYDJtZCmg5bg1fURejJ189kPuX_QnG2i1m2xdLgcaSEI6OpysRfC56pavp394qGQsT0zUPdmq7jdS1CTm4pkbrbMNSI1GZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQtZ9WnXT_DvYToTOezeHT98G6fiNUT7Gj-uAFIZUeP65NNaH119HdxhsOZhm1krDtWT9YfstfT7COmNDQxEZE6VMcral5skN-L6Df3gPYBBTD5koqTU5E77bhN7mZM8kyD_m8Tg_1uUf1vHgItfR8-MREnpm2hxya6-E2TgTemdT6beWklVHLh1Vd7i6OoV-jYoYOjv3hUm_j3ewtcDmGXv-MHcrdxzQYU-AIGpkqQAnxC2MPLGCdKSdRdzxKmDxU05tSv1qryZPzCY_85PuzD0HZht7ZDSh4kxWFdmYh0p2UMMBSq62ZDx1926HZG4Frdp93fvqEWTEk58vTZWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De5Ljs8WSGTPCe7PdQz_DzNDh8uBNPLVFHIXM8EXfUUX3xcwPYcMzhwt0EcVmlc5MqqEk3nT8UAOhgLwg6X_ZuqhnbgiQy4QlgB4ozlFV-c3NQd3F9XngxBHmcYvdsva8OCNW4gbdpiiPcx7GyiCXHQk8TthEefGBnrsrWPiB2Qci4y2b1ycfMPx0JpwuYYrQnzuvorQJP7EH3FwiKEGChQtGU0hHgW7zL9isQZnj7ZKPh1THn_THf1KVyrvmrY2-VPhfz0N8-7GuwM32fkwnbFWqhU22oaJaCwC8vqvv-G9fvYBVJ97RwdFOtSHRnu9AYotGbUA1hXc9EyKFHyiMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1OaC8bkBWUAm-isepnT2cTPnFBfPikWh_3aSMJoS2VrnObpAO7h5VTr2wV0tujqb9lo0K8p9UfMKEtANhqd1UusUF35QAsRCXyPSfJ_uI9ryRD-DRBYEFX8tKMWUdiIk5vynlrIiW7686kr6f-myUqwC-l4p_qjXUAoDXbqJbf8VsGcWjsnVAEwMcg4pPaHDm0c_Feol8meSS9fm366lPajICGwIKeiaHLnOjGeDT3FNbY11zE4nHOzYzThDAzJQSqxvX7LIpFEh76u0kKJVzD6wvc6p3xrr9Jv_G95cAgAXJbW4_dkqJZnYlqIzJ-YD1dwCyzynH-qWj2ftqyq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEmWEB-mPux4oqlfc0WyslwIYqlb7GwVbVqSfzuw_lUTproMXtCHwOS7kwr2cpRrMvR4QOjmOX63MAdF_RPKrWU4bIxvidIgSvDCtIPhYG1xs0RIpPzuvqxBIxVI813Orw2R4sIXROZ6kbSRREfVtf3AiRDdtcXMn75hlI6v60wpGdU2O16jnCSXKb95amDZsCHUce71i-h5IZiSxzAzjduZBo17jSrXcAYQlRWpf9QXCjPfeqBusDKcTRSqDFjM1gf_U33qTAHwhx8zodx-UFZcu66yWJIzVhuquWRfsivNRjUaPY9_vvzwe0Y6oFceTl2we1tXPvkX1TqrOdatRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZvrswF4LyY1HjqP030HESGyyJWiqtmOryyZEUzZx76G3O-Bnhs-U9c9U8A9NrMKPQuEn_2AqNZOwagdhyvW-RNN3LE8foKCARQY5ZQOstn6olRVQjB9bxCrn2xTC64vWC31bMIITvRAwRIZNCnNguqDlTK7R4NYHl2oorownTRMJEh5XkXYkxxvds1OUW648QIWocF2a2SWxvN9MUUavWu6xsa1LW6yvMJBtmhHJQQN5HDtCeNpzAlf0J_DfzNUPNxpwFemG8KlD5TcKxDurRNfdTTcuXlLnnNsg6V5rRfyXxirs4yrTswrFYfmabPHEBWoQ5ruWVdHtGbmsXmyJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
