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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 20:59:37</div>
<hr>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOPBe-WsSyKP9b8iFJXu_j5PR_0lIEe2k50pJqHmxjEnlwZ0j94YJGCBG2XZ_m1-E5lIzS-uCEoSAwIqZByjdAtrURxa4361C-j0MHwVOYXc5RHqG5rGl7Nqk58cUP7HiiAmnhLXXhu7jS1wv0McnVMu37vavKH4-rLNI7Y8D81vO04kCcgI_JAejI2Mi2CdGfcTRRRsID6hnDCdvP19ub6N56KEtCwDrDAoeceEfqjYB_EF3YKLkB-FZW5OlDzcmSRzlOveJDK5k_fi52cSTkfDG5YrnnSg0LgXDVg9XtIxKe6YOuSHD_9JrBKpkIrDglDkCtl6QczjuIODYlnyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=LDIYgDe9SuUlCqlp4ieWPN_CY3E4lTBLfeZFXxLyvHD1Xq_8XjL6StcVXkeVZK_TiSjck6Pj1RXUW9exYO4s28dQt9yO9O8dCVDCbH6OUPA8sHNK2lmQ800ir9ddmurt3NpaEGAgcZGxLB0DqpiRBolhVBC9ankB5LNWhLBuvTjejP90rURznJOE6aIstUf9KDGaXHg6pQiR1ZmEWfuwLova3puwOLe38ozr6HuGPCRTdAWvZ4LTB-xSEqM08_64yCA2GrIBM_UKaXjZ8k2ZoVC0HtoePXGmYpP_DJ3Kz5VaACC-FaibA8TsBVYG3YvGUIA6tpvn97jUYo9WZL3I9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=LDIYgDe9SuUlCqlp4ieWPN_CY3E4lTBLfeZFXxLyvHD1Xq_8XjL6StcVXkeVZK_TiSjck6Pj1RXUW9exYO4s28dQt9yO9O8dCVDCbH6OUPA8sHNK2lmQ800ir9ddmurt3NpaEGAgcZGxLB0DqpiRBolhVBC9ankB5LNWhLBuvTjejP90rURznJOE6aIstUf9KDGaXHg6pQiR1ZmEWfuwLova3puwOLe38ozr6HuGPCRTdAWvZ4LTB-xSEqM08_64yCA2GrIBM_UKaXjZ8k2ZoVC0HtoePXGmYpP_DJ3Kz5VaACC-FaibA8TsBVYG3YvGUIA6tpvn97jUYo9WZL3I9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZEQJuVbcnqNZZHO7UjFbF5c5Wp-hZh70i1mON0nwPJXiyT9kPyasiGoUW0T9g6LNIIN6IHGZfBK19KjIs9n-UBY9DyHOfS7SahknXoobdxk9rAgcUea0wnNeB_--HjjeqccWRSaiKopHyS19n3_qXwB6Kf2CFiqqXo77mT9Fzeh_NUY3p-SFM-2bPYbnSZAERGxRt9l2cu2KPHotFhcEQlnjRwB_SmQGrDMLs4k2IhBJVIIxHbHhEy8dywxrSY9cN8bRk7qIOYN8GwyfWa-HAItdZNbRxnfVacjPfv5K1SK6kgh-GqspnwCMbtCo38bFPtZZCBgwmF2Sy4MsqnXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ARPRWX9Wj0TsmDf1-MN8c_EKsxPJAdqoMIEav8ezaij96uEpcGpwdnuWoLiyXqThQ1uHF4PAHlLujhTP4q6S7LJTAveG5rV49tJMpblJfrgOPsT2Us6rDMGBMB646sGSlWqQ3t0HAi-IneXWiLmArDpuWAdhmsPDKMErooFUvdby2ylVMWTdkMX9MourW_Izbr9HpuzKRkFc5-I0e_6sl1a9LgosBtCBQdmvupzg0dNwgZCwHt3dkDMdW-xr7R0bxN4kZM9fDx3w-eVEfUjwRtgBgRs9GWbHis8thHngGFIToViMdEldezxuds-3WQmRZeaug4g6-4PBBz3-rikbAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ARPRWX9Wj0TsmDf1-MN8c_EKsxPJAdqoMIEav8ezaij96uEpcGpwdnuWoLiyXqThQ1uHF4PAHlLujhTP4q6S7LJTAveG5rV49tJMpblJfrgOPsT2Us6rDMGBMB646sGSlWqQ3t0HAi-IneXWiLmArDpuWAdhmsPDKMErooFUvdby2ylVMWTdkMX9MourW_Izbr9HpuzKRkFc5-I0e_6sl1a9LgosBtCBQdmvupzg0dNwgZCwHt3dkDMdW-xr7R0bxN4kZM9fDx3w-eVEfUjwRtgBgRs9GWbHis8thHngGFIToViMdEldezxuds-3WQmRZeaug4g6-4PBBz3-rikbAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFGxaknU9gwmCHvWMuzyhciGwoBq3Wvjsi3vsfKtm2K1CmZB17mq1Oj1d8hkI4A-SXDdha--naq-8ctjhw05SJrokXf-QrRUo1-SGSg-oNlcOjLaizuMW_ukRYCU0icWyphiJ8uBmiz4OCkeCp3NI-igJlasLW1Rq8cjbqPSDyev85dYTagLTKZnty8j3U2XHpG-LVLyy_mEdTm94V6RmJpF_0B6iFbqw9i3fkthQ2Ntim_Kbm-_ZFp-rdbqiOp06xSBNNeDqb6JqPloEj4v0852Qxf17plAEj6GOf1U3H6mXfwYcObJrJF-QKuj66SXxyZoSAHItyMnkNRq-OGxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=U3iXfC8eEG7HZEskCI4LuRbexgqp_BYOBYEX6Rpt6CfIqV6QGrTTu6DC7etc84zPnUnL0jxdb2_3BFX66pXW16NqiUfkLAKqbtWnFHm-ixpYdT1HfdViZg4oQiQtlTvP5sQL_-Xq-lpBRSgxJAw7mR1BP-I3qt_UPAL8H_YAXAaZNOCkDEfQQpKAAl9tWsBrlIHzyWQaNRgEULhjZatv_DYSNvh6QjgfWRSvLM3bvX1-pkEwbciY8f38E6B8i9fBy92Ef9jf5AvIAPT5QbCYCTk62dn52ghbbbbPi4GEGmNSu9i_FhtF_hSrFQ-_dv4bUorPefvE7s_IeW_QOqPtNx6yTcGEAo7Xh5otA83jjQQLbXK8FkRvEhc8LmnrgL3WjfZfCX6wpr51v2qxSXoBAL5pNIbUTya0tjUnmp8sAsLyMPC3Ly_oBH_Wj1N9IX9y9aotORB5uLaZHhu1K2SlieXdQ2o694EEE8OGMLewwPExkui77EseTiuF8CeKBNkEQXPz7zUcTIG02rKxl2c458blRi8LekoS6TLwuJf1GWNuvc12f5ZQ4oZW4g1ZvAJrmE36DT2TmbPaGEq5SEMVgCghMOgevUgEYPfHB1L-006hkjEFgBuZbRx-eMXVY9x0N6XgTGYGC-i2jhhYj7QKU4NCGythEc_7JNs44likxFY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=U3iXfC8eEG7HZEskCI4LuRbexgqp_BYOBYEX6Rpt6CfIqV6QGrTTu6DC7etc84zPnUnL0jxdb2_3BFX66pXW16NqiUfkLAKqbtWnFHm-ixpYdT1HfdViZg4oQiQtlTvP5sQL_-Xq-lpBRSgxJAw7mR1BP-I3qt_UPAL8H_YAXAaZNOCkDEfQQpKAAl9tWsBrlIHzyWQaNRgEULhjZatv_DYSNvh6QjgfWRSvLM3bvX1-pkEwbciY8f38E6B8i9fBy92Ef9jf5AvIAPT5QbCYCTk62dn52ghbbbbPi4GEGmNSu9i_FhtF_hSrFQ-_dv4bUorPefvE7s_IeW_QOqPtNx6yTcGEAo7Xh5otA83jjQQLbXK8FkRvEhc8LmnrgL3WjfZfCX6wpr51v2qxSXoBAL5pNIbUTya0tjUnmp8sAsLyMPC3Ly_oBH_Wj1N9IX9y9aotORB5uLaZHhu1K2SlieXdQ2o694EEE8OGMLewwPExkui77EseTiuF8CeKBNkEQXPz7zUcTIG02rKxl2c458blRi8LekoS6TLwuJf1GWNuvc12f5ZQ4oZW4g1ZvAJrmE36DT2TmbPaGEq5SEMVgCghMOgevUgEYPfHB1L-006hkjEFgBuZbRx-eMXVY9x0N6XgTGYGC-i2jhhYj7QKU4NCGythEc_7JNs44likxFY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=LlLQV72wfcJr59HYExyj__Fn5OM8Yh4HsMBtLKlYUY1ZZNwWwTp1tEAgewTtFmyNGW3BrdOJuGYLx2bbJVUl1loYwTZlGPr7PyCEX88iuU9z6ix6bNi7sj-YLhHzS1zSpxx8IcKTiwmhOhilEyk3kQaWQAl-f91qxMQJzD9aPw0RmTuYEDO0snzh4VSOrr3PL3mQdN-zz4t8_9oqIMq-cUKxluIp5qcYVx1_DvOoD6okEj9zqDdVxOo6RnumOVfHSasQw9QyILp3faz9pjJuJgGuCcdv8rtVp54124C0sNzRjnrT9xAyp-0tz5eum5iZorDreF1DziDuLfW6o61bTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=LlLQV72wfcJr59HYExyj__Fn5OM8Yh4HsMBtLKlYUY1ZZNwWwTp1tEAgewTtFmyNGW3BrdOJuGYLx2bbJVUl1loYwTZlGPr7PyCEX88iuU9z6ix6bNi7sj-YLhHzS1zSpxx8IcKTiwmhOhilEyk3kQaWQAl-f91qxMQJzD9aPw0RmTuYEDO0snzh4VSOrr3PL3mQdN-zz4t8_9oqIMq-cUKxluIp5qcYVx1_DvOoD6okEj9zqDdVxOo6RnumOVfHSasQw9QyILp3faz9pjJuJgGuCcdv8rtVp54124C0sNzRjnrT9xAyp-0tz5eum5iZorDreF1DziDuLfW6o61bTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0aywzT_-GzwuS-25mi_0go9TbrYsABFIDLG5_fKZJKw3ldMd2vtzyuR6a1cYEs4HyFKCmu5xkgmWHGm-hBJDPvRVBrri5iB5aO9t4LE5QxgtoP-3ykIltfWQGeDiazeZovAYir7RXhaSogRkAqtMnSBFS-e8paGxP-d2lN-lV-yQrhxXacNBelER5tGXdSIkLdUZKq_Sp_pSQYBzQHcHnto6y8s-ITaXKwQjO2AKvE3cGLYwtx96h-7z4piCDYzOQZ2qQlDuT4N4byUDUvZQTVXLgUGPu2tYKthtaZU8gaXoCbF6Eg4l5GArzaG-2nFYMC_CGRIEvAS7H1Y9RiqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdS1pykzShzR8CEFx8oTl2v9K90uDjr79lde4OI135cV2n5XqcXgZzfrTxGNQmLKEr4H7iCydu317EoA9gt6pnQuZvbBjpFLkAZLA_DxWz_NJU96N-YNJmf5eSvAyW41kkG6QvQw0qr_cD8oQoIfbHtISGQVioqtXXGTeVmhi8UtFrqRqdlH4y2ttyHiuppjv2Q4puTedYS-CEn-YM_dNy6jaaqzceJJp756khn9xy0aAbNyC0SbKdY0dyRj883jjGuOvcRykzxSBVfQQ0K9tmmMCNwNCyD2ckPRdLJuO9kWQYvEUBxDgGUktti75SCfPs33KYJD7LIHakqo_ozJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wda1RPKY6KjADHUeSAR7DU26uW17uhcJiQTEoCUY_o-hJt-vZwuLLGBDVVnlB6wbNom6KrdSPiOUiQ7SxKBcXXsjqxj6JMQOBGFKvuwMtZ5lhf-qRN4_ZQbyXvaOf3MM30d31d5vSNHsSDYgJy16HsdOtbj5W0onrotCdfIu5VqEUxYmndUd58PwVGxFk3cgHRw2yKhfGDX017U_K8aug6cA_pMZSaNzCzdnfMDAQ0UoTYq7dLZV7TeGrpWhsb3uS8pQAw53FrHnWe2-bFuCql5mt268wfQpiBknZniwaj8WYvo35vaCoYPO0raAh2bMSojQcTV0y5bJ6XjWC0ixVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmIQU_MfuDBPi7H-Q5k80duTVqKOvJVR07vF3raQb4-fEQSX-iPw8dxNWuPXXkEmjXZPwFVsbZ8R0v5aqbUFLFsL99pqG9lAn0CxXNRWlNB9kWXaJK5vqbc6bwv6SLTDXtI4zOCCYdsyvMHuGFKAZfPY2B0ucXU6s_8IRetRa9axW2iS8eLUAEKMlssSRQJH41Tnxv_kGLn7tWAYUciIw5vaElfee1lNOwbDY531m2zz-4GloxsJWS3Fofe22aVBWMijHLOkvgoQM_Yt7kKP-o9gu6439am0B36l34J-f4_WeaXuR6mG1q0bbHcNO8wkmnQTB8YgQ1EoxJdHQOPdpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFI94Q3CODFicWgaouioWYU26--f3-0iXer86Jr7HxZA7PpeA9OAHm0-6gn-RxESpFIa4A97blaB9qcZAGbcVFnDKJhk8Pl89c_6yKlyVcSNctFordPask4N7BHJN-HgdV1R51oKcnwrInZBdSpI1xUx0lIqi7M37eBwx2bhA9qFyhvlIs88UN6fYEjcn27gFxeeCb3aedqNIphUqx9ifMQJqr0Hd79p--zMFYMf-Kk5-qkrSac4VPpjhieNe_Vr0SyUH5vFJr5tG-pSy0C5wvnvBiMAw-ys49E38JYYrfA9_HMEMMemuPmG3eU1-J89Ica59ixecm4wYZU_RvYnOSVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFI94Q3CODFicWgaouioWYU26--f3-0iXer86Jr7HxZA7PpeA9OAHm0-6gn-RxESpFIa4A97blaB9qcZAGbcVFnDKJhk8Pl89c_6yKlyVcSNctFordPask4N7BHJN-HgdV1R51oKcnwrInZBdSpI1xUx0lIqi7M37eBwx2bhA9qFyhvlIs88UN6fYEjcn27gFxeeCb3aedqNIphUqx9ifMQJqr0Hd79p--zMFYMf-Kk5-qkrSac4VPpjhieNe_Vr0SyUH5vFJr5tG-pSy0C5wvnvBiMAw-ys49E38JYYrfA9_HMEMMemuPmG3eU1-J89Ica59ixecm4wYZU_RvYnOSVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=OhZ57w3kMx0v1UUeb3HpbsDnw_1DzSEMMFp5kkObK2l7MRDRK05N-tmYsa0xi_exNm6cVez5EEGwa0tsJH1imN62A8XZLmr1GOJdSsmBYdtijUXys9mvkw0sqzKa9k-JroNV9JPxgkFA6Vgb7KXqQGJ1QULar4HQjWlF4P1KASp9T82W2QBXJvzBetkmuZgckqSr3c1gNqZFKQdGgEHuZKhU2UR-ZN8uW5wf4Z89D-90IIgcgmZSYiXb1Bd0pQfCLzv4sobY_EZ-aWBU1T_5HaXCpd8z3jItg9otK3s4Iz2ybKFFsrx_Ch541Ycwec3DcnUhFbJOa_RHGZRBANujKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=OhZ57w3kMx0v1UUeb3HpbsDnw_1DzSEMMFp5kkObK2l7MRDRK05N-tmYsa0xi_exNm6cVez5EEGwa0tsJH1imN62A8XZLmr1GOJdSsmBYdtijUXys9mvkw0sqzKa9k-JroNV9JPxgkFA6Vgb7KXqQGJ1QULar4HQjWlF4P1KASp9T82W2QBXJvzBetkmuZgckqSr3c1gNqZFKQdGgEHuZKhU2UR-ZN8uW5wf4Z89D-90IIgcgmZSYiXb1Bd0pQfCLzv4sobY_EZ-aWBU1T_5HaXCpd8z3jItg9otK3s4Iz2ybKFFsrx_Ch541Ycwec3DcnUhFbJOa_RHGZRBANujKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=GyehywCXo1AXnUUdnbIExUcusxfw2Vxsf1wbFGXJxcRgVDAgS2T7l0EruNaQEDSBruM8qphZDg4og-XvggSfGOBiso5E9aNkxu08nipVv5TUTeUdUWF6iXkEMvZPCI-Cktdh-MNp6ZLtCA_V5y-avCyJhGAiFwEDGWS_cS3BGmZmeayvFIluHd-qbOJ9YK_OX01QeRwD9-hJ0JewbZ820E4LLBVLPgLvyoQTWQizUbSFLJ6TnYDNmkxn-jJ1kdDFyXmD0OTP8jHUh7CpIJxKWj56ZCeK9CMs9EEguAEt5y-VhNhkH1c_dM3wAw6G6Yp917SAOsq-_wB8I0XGRbPe67Fay9vAPzgrVSbN9Pcga2Av32pyKH86xqA9n9Gq3J_hs-jXxEQs1I28ieVyBQhEQe5e58xgEyIlT3UoawEg3604_aQL8szB-1cZiuGnYHnbiYtVH3Wevm2uyybD_3BMcU7K1C0usLH9UgD5mgyCo3dzCvfIoe_4CkUtqmuzVRG6M8zFdO7G3XmYbjpK64BSEin9V0e-QvZAMybtkLmvnu4S3OaYtvq9h-KlJTx47FVuFk21iJM0f0E8Owz1gz3E30RhNIXJYeeIlh-w0aevG2KV__zZH5qAqk_C7lJ6aJCQ_SuOeWeYOFUxNjSJuBoVPoxQ_R7gY_JMFj19QFZXFHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=GyehywCXo1AXnUUdnbIExUcusxfw2Vxsf1wbFGXJxcRgVDAgS2T7l0EruNaQEDSBruM8qphZDg4og-XvggSfGOBiso5E9aNkxu08nipVv5TUTeUdUWF6iXkEMvZPCI-Cktdh-MNp6ZLtCA_V5y-avCyJhGAiFwEDGWS_cS3BGmZmeayvFIluHd-qbOJ9YK_OX01QeRwD9-hJ0JewbZ820E4LLBVLPgLvyoQTWQizUbSFLJ6TnYDNmkxn-jJ1kdDFyXmD0OTP8jHUh7CpIJxKWj56ZCeK9CMs9EEguAEt5y-VhNhkH1c_dM3wAw6G6Yp917SAOsq-_wB8I0XGRbPe67Fay9vAPzgrVSbN9Pcga2Av32pyKH86xqA9n9Gq3J_hs-jXxEQs1I28ieVyBQhEQe5e58xgEyIlT3UoawEg3604_aQL8szB-1cZiuGnYHnbiYtVH3Wevm2uyybD_3BMcU7K1C0usLH9UgD5mgyCo3dzCvfIoe_4CkUtqmuzVRG6M8zFdO7G3XmYbjpK64BSEin9V0e-QvZAMybtkLmvnu4S3OaYtvq9h-KlJTx47FVuFk21iJM0f0E8Owz1gz3E30RhNIXJYeeIlh-w0aevG2KV__zZH5qAqk_C7lJ6aJCQ_SuOeWeYOFUxNjSJuBoVPoxQ_R7gY_JMFj19QFZXFHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=PoeCwZdlJEQFLtDwvVbRfuTRIQ2whpkRNifXDvIrUKCy0-DQ2hqGcACPS1m_05-spblLOLQIislfVmjsZ4LOOUwQXbnO7uXVrbDC1lJ1YSRQGpF80BZbBQgFX9ngTN-pNdRDiq4QOsMXh7liXrLjtkvJ_V8FR7xG-TAVhqfag4mraOsUJNH4kTfPiDm6YBgC5rZcF4emuC-NaR5ONDsczTwuDPoj54DaLJ_iNVD5ZaY9oKkjFNR5RVmhSX1ssTnZCh4dGAUOPP3HS1zkSE9yjvxcl6tesKC3En8cJDI3zLSpMtf7UPQ21vbgIW7D59AWp1GU7GwfjAt5KmYbAOldxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=PoeCwZdlJEQFLtDwvVbRfuTRIQ2whpkRNifXDvIrUKCy0-DQ2hqGcACPS1m_05-spblLOLQIislfVmjsZ4LOOUwQXbnO7uXVrbDC1lJ1YSRQGpF80BZbBQgFX9ngTN-pNdRDiq4QOsMXh7liXrLjtkvJ_V8FR7xG-TAVhqfag4mraOsUJNH4kTfPiDm6YBgC5rZcF4emuC-NaR5ONDsczTwuDPoj54DaLJ_iNVD5ZaY9oKkjFNR5RVmhSX1ssTnZCh4dGAUOPP3HS1zkSE9yjvxcl6tesKC3En8cJDI3zLSpMtf7UPQ21vbgIW7D59AWp1GU7GwfjAt5KmYbAOldxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvPnDn2klw-iBLFNtRVbBmexTJHZVMway9svUKKa4c6rRBtV4sfG7-uu_3xo135zIfISVNWE30zvEsuYpyx4CnwFOWU5MbgE1v0ozVCVolmz0Mg86xwzJAmJuNuzrGaymnqhft2RojVfj9Z-lIA4AiW_ODKn88kMRnoi_6TBojW43kftFswqK2KilP5A_Z2xQOUIyBc9LJEg7m4kel07Bhh53c_2OWZ7qIVQq7G_XP-vLXaQlQTcTtJ4cIMxTHDmPOAYISmnlk3oX4hMkWJ4QEAQgjr4zgHmVeXZDDKhsKfYm35D-O9xDHn2KvalOB9EMKBp73rrI7jy2TfhBVnKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=rXEuZAsIvlGjCYvfmPWViON6yhukeYg0nihiP6uLtVSlwrhoKrfJBoy3yPew4v9GApzyqtfEjJaOWClmYxAbOe7UAdjX704JbtblhUqLiEhDx-hzfsiCJ0tNzZrnV-lqVlT62jK_qHGFaqGfKGXjM07MPbxT2ajFK9ymWepCrRN1vI_p9aIR8U2ekaGpFrebUfwlqkG9zIcgj1rPH5P6vgBEAbCJ7lPek9BUAUZkJ8LdIZXkzYu_VoI9P3qiR9ohvWDP1bE0LdKZHaZvTvEyKpOlVO4nrTDdoWhRI1juEd8i5wiYudPsrVkGr8d2SblMbWiWbgLrBu14raGEhNFHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=rXEuZAsIvlGjCYvfmPWViON6yhukeYg0nihiP6uLtVSlwrhoKrfJBoy3yPew4v9GApzyqtfEjJaOWClmYxAbOe7UAdjX704JbtblhUqLiEhDx-hzfsiCJ0tNzZrnV-lqVlT62jK_qHGFaqGfKGXjM07MPbxT2ajFK9ymWepCrRN1vI_p9aIR8U2ekaGpFrebUfwlqkG9zIcgj1rPH5P6vgBEAbCJ7lPek9BUAUZkJ8LdIZXkzYu_VoI9P3qiR9ohvWDP1bE0LdKZHaZvTvEyKpOlVO4nrTDdoWhRI1juEd8i5wiYudPsrVkGr8d2SblMbWiWbgLrBu14raGEhNFHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=TFLMBJLuZ1Pboc0_LsOnklXgKEJhBc72VsF6OY851dmSBENb2cMZM5uDQC3Dhc7TJy9YEPf5-nbuXUD5Fqj1Yfp58vVtrE7QMYgWhmXFYFYOzlV6Pr-GzpvDb741VCXW386OwablTRYCJaKhn65stQLlWOoM1As-MM5mka1e22Of-TaSUmuHmTMIqSC405SzcyMjwHKmBHroW4M0Y0mwGi2Tw15aXEUAw1-XlWAZLfUnuMGe_DGV0-TQ8YPCJR1RAXCI4kx4_ApmdD2KoGKItgazo40N1HRyY8NkTr2YsQqwBVfqwSO55jVxlHSE8Wfky2ieiCjAToDEdyeygqLl_kqkyfrNct9f3sTOyytwr9vMZHY7VgQ1U1uqoiV1g0e4zEexVs7_VOYgbPxGb5BMl1taWgRnsv3ohe1FjwREN0yxloTVj6DaZV4h2uBylgVnXF5GTa2xBIE0N8LWtjuAZdUBIFKU6git7nCg0iKFFaJHKuKlaHdXfBoYdaFQbU9TpKlxWcxTmz6KZnAOK6xF4m5-atFSHLiR7dvZeT_kBwSLffFPlvFYiyBcRiX0uMxLmKM0okBZOzVK_EJCmC-0rOOsp8O1nI8YqzN7yTNVroT534uNz_yBFBgoY2g7Bl4ZoDCrqBHZz0ESigq7LowQwhW6xLn00HHJS-Nar6WmSEE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=TFLMBJLuZ1Pboc0_LsOnklXgKEJhBc72VsF6OY851dmSBENb2cMZM5uDQC3Dhc7TJy9YEPf5-nbuXUD5Fqj1Yfp58vVtrE7QMYgWhmXFYFYOzlV6Pr-GzpvDb741VCXW386OwablTRYCJaKhn65stQLlWOoM1As-MM5mka1e22Of-TaSUmuHmTMIqSC405SzcyMjwHKmBHroW4M0Y0mwGi2Tw15aXEUAw1-XlWAZLfUnuMGe_DGV0-TQ8YPCJR1RAXCI4kx4_ApmdD2KoGKItgazo40N1HRyY8NkTr2YsQqwBVfqwSO55jVxlHSE8Wfky2ieiCjAToDEdyeygqLl_kqkyfrNct9f3sTOyytwr9vMZHY7VgQ1U1uqoiV1g0e4zEexVs7_VOYgbPxGb5BMl1taWgRnsv3ohe1FjwREN0yxloTVj6DaZV4h2uBylgVnXF5GTa2xBIE0N8LWtjuAZdUBIFKU6git7nCg0iKFFaJHKuKlaHdXfBoYdaFQbU9TpKlxWcxTmz6KZnAOK6xF4m5-atFSHLiR7dvZeT_kBwSLffFPlvFYiyBcRiX0uMxLmKM0okBZOzVK_EJCmC-0rOOsp8O1nI8YqzN7yTNVroT534uNz_yBFBgoY2g7Bl4ZoDCrqBHZz0ESigq7LowQwhW6xLn00HHJS-Nar6WmSEE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYoOR-8Cmrce8uWO_WpKkIBwYLUZRLOVfJuZc9f4SaqiUC0akU5c9bxIS3WE8hNmjS1prpT2O6_-3wI6HRDzCF9nbK8oeCCxw6JwJcP-bQKwajamvtqJsSstoQBqpBSAIk4JD8LrzR9yTSOYvfZ3jP9wJk5AugJsma7HSuAH7o25ssFeTA0AvYCLm97K9pIWWI1A9H5bOF1Oi_CseoFTd6OeTngnn7MmYRKu19fUtYqtt1_C0IrBJSbEyRnEU98IgJtHMUG_u3CCG8m63p1_03FKeYAkmdQVVNtodnLzBqgf2HRo3gcpt_28MJprGfaDXRW60xgStNhZ2zjFGkkxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=DF-lFGUpn_JUwfk_Ze0lOwDWSsEm5McUcdakd6D_IUqU5bv2wA4_vM9HEmhg2D9XNsphhClZKI-0zqqLZgspu7XjEOlcqVaHkoyVLUwL17ADHkhQ_Z34NT_zM03fyVlDhI9NTcZGbLwftXBvHHH27_mXJ3vAl6RW7n4xS6lcqTOjZ1ZDi6SJxEoUhcu0X-uyQ8FVOoZS9mtJ4BdjvQvDWcDsxdQGwZeiy7QVWpkD1D2VKE_5LOQx_BD-XJZWdntdkXG8QsuFc8p57CNY7OgQmxg0deEA5gEKSQ_ieDAaLSk9fnO255mlUrGlrH4VNoEPzDS6nnIRLmU2hsUtma4R4yD7M_0cYp_0ukxLDNbXyvDFMGe05UGhBWk8GVwHjdExYlElUVRgsBCnqBSDIuTO2lB6wWav2fqb84hQjmqTmF0Ww_fQvs0rFWIRNA-Hd2LIW7xgyd_y15wNTf-KcFwLguV1SssPYwdDgRqOXehrJSXmZj4uUNSZuK_e5gZjZ4ADaQ4OcmcoFe7gEaG-8yKadWTj-5TJ7v56OsOjgGNHF1GTZNn6M7H4Ce6OHKiLUlxd1ur6Qozju5PZVfhn7eQUIG7vtRAH2mOR11TjkGkQXtNSn_pyKXvzUZ64SPjbyNaQxhY5kAX7xSYAF-ajNuiOToLFBi0XAObzAx7u_vGZRv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=DF-lFGUpn_JUwfk_Ze0lOwDWSsEm5McUcdakd6D_IUqU5bv2wA4_vM9HEmhg2D9XNsphhClZKI-0zqqLZgspu7XjEOlcqVaHkoyVLUwL17ADHkhQ_Z34NT_zM03fyVlDhI9NTcZGbLwftXBvHHH27_mXJ3vAl6RW7n4xS6lcqTOjZ1ZDi6SJxEoUhcu0X-uyQ8FVOoZS9mtJ4BdjvQvDWcDsxdQGwZeiy7QVWpkD1D2VKE_5LOQx_BD-XJZWdntdkXG8QsuFc8p57CNY7OgQmxg0deEA5gEKSQ_ieDAaLSk9fnO255mlUrGlrH4VNoEPzDS6nnIRLmU2hsUtma4R4yD7M_0cYp_0ukxLDNbXyvDFMGe05UGhBWk8GVwHjdExYlElUVRgsBCnqBSDIuTO2lB6wWav2fqb84hQjmqTmF0Ww_fQvs0rFWIRNA-Hd2LIW7xgyd_y15wNTf-KcFwLguV1SssPYwdDgRqOXehrJSXmZj4uUNSZuK_e5gZjZ4ADaQ4OcmcoFe7gEaG-8yKadWTj-5TJ7v56OsOjgGNHF1GTZNn6M7H4Ce6OHKiLUlxd1ur6Qozju5PZVfhn7eQUIG7vtRAH2mOR11TjkGkQXtNSn_pyKXvzUZ64SPjbyNaQxhY5kAX7xSYAF-ajNuiOToLFBi0XAObzAx7u_vGZRv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=mAWa-gDZpQsSEJiH93cSye9yyydHcx0kRyoi58ROzci6tvBHFmlT509zsQor9cUZuCKbrQIDPU7UGhu24GLsXmGvs0alanuO5BSBnzEeLgpRzki9p_rpyDWxqDIt-wN36pJeIQlnIhBiXiX55LZsce9vB7Vs9_Gg8nCkiaGir4ljhaB96l5PwaqGr4_WzMvpYS6A-KuV-6mMlWjdbsi3piI8pcE1v4d9YEAtqCS02AXwM8jiS3oTGOyZ39A-HmJTrsl8LenuvuKh0r46tvqwNb2D0FLUDxK0WcofC-IrXIYj0bDycT9HlQEIumrk2gF_x9lLhVmYBaJA3MUy4hRTXSk8DEOaOAJzOOI7RRSUW04h4Q94VKVbZgiWtg88coxozOrZDjwDsoAaCrrrwrGExEIrbzPovPTnywQ6zba5ZljF9gME0NowrJEgQ-SIUfuIin7ICMH2LvNVxkmw6jRcp1s32y7asxUgN8dDsO0192ve6BJuYpK2GPQEUirvKYs-jJRzW2JgLcO5QeaGh0-p8NdUTKzmoim3_uSf4UHSsnD4MNTb-_8FqE7Ee3H9n82ssOT4NxMW6rZVQaXMQOlm2mYqrSzWDXFA4CO095p1B_SeX24I2KJW4Bf7O64d4y67bzrD947YHtcMAPBQ30ra7qDzTfK1O6k27V8nnNHTGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=mAWa-gDZpQsSEJiH93cSye9yyydHcx0kRyoi58ROzci6tvBHFmlT509zsQor9cUZuCKbrQIDPU7UGhu24GLsXmGvs0alanuO5BSBnzEeLgpRzki9p_rpyDWxqDIt-wN36pJeIQlnIhBiXiX55LZsce9vB7Vs9_Gg8nCkiaGir4ljhaB96l5PwaqGr4_WzMvpYS6A-KuV-6mMlWjdbsi3piI8pcE1v4d9YEAtqCS02AXwM8jiS3oTGOyZ39A-HmJTrsl8LenuvuKh0r46tvqwNb2D0FLUDxK0WcofC-IrXIYj0bDycT9HlQEIumrk2gF_x9lLhVmYBaJA3MUy4hRTXSk8DEOaOAJzOOI7RRSUW04h4Q94VKVbZgiWtg88coxozOrZDjwDsoAaCrrrwrGExEIrbzPovPTnywQ6zba5ZljF9gME0NowrJEgQ-SIUfuIin7ICMH2LvNVxkmw6jRcp1s32y7asxUgN8dDsO0192ve6BJuYpK2GPQEUirvKYs-jJRzW2JgLcO5QeaGh0-p8NdUTKzmoim3_uSf4UHSsnD4MNTb-_8FqE7Ee3H9n82ssOT4NxMW6rZVQaXMQOlm2mYqrSzWDXFA4CO095p1B_SeX24I2KJW4Bf7O64d4y67bzrD947YHtcMAPBQ30ra7qDzTfK1O6k27V8nnNHTGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=JqeRZDqbbl-vFTfJR8xktXOUeu1lPAeqF5RCQJEI_pH8NLLq953bIUC1apyZEfGSkEsnV5FctkhRCINss40wesSpxA7Nri3lr91YOGEA70UNLaWogLIaS9PAYeufua7uQkwgIRW3YEO1d5rQB-2LzM8BNe9K55cLwEdq-S1UnO_YAk5B6IczXk9Np_ucu25bWBxomvKUwxj6Q3iriCWr-mMifm2ChtLDy5xuq6sfQ7idADS-lijifHoT3eJMUcCbzbIzTKfcakp6E_gSALcNJCTV9Q3ge6aa3bJoSzOqWnrSm78FtUHc3DVpvdHsKA-z5RfFdd3D6sOAZfaa-P5C0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=JqeRZDqbbl-vFTfJR8xktXOUeu1lPAeqF5RCQJEI_pH8NLLq953bIUC1apyZEfGSkEsnV5FctkhRCINss40wesSpxA7Nri3lr91YOGEA70UNLaWogLIaS9PAYeufua7uQkwgIRW3YEO1d5rQB-2LzM8BNe9K55cLwEdq-S1UnO_YAk5B6IczXk9Np_ucu25bWBxomvKUwxj6Q3iriCWr-mMifm2ChtLDy5xuq6sfQ7idADS-lijifHoT3eJMUcCbzbIzTKfcakp6E_gSALcNJCTV9Q3ge6aa3bJoSzOqWnrSm78FtUHc3DVpvdHsKA-z5RfFdd3D6sOAZfaa-P5C0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=qql3SCeL_e00Kx3A5E534c5BMlhO5HNpwGs2gaO2mRa1bPV0jlFsTD5QH8gYYOGNWXOHIdqyL-5EXhD29gvv1V77NcfTWoGS0EfImtgQHRm1PViSGW2xwcjoe4O8QKIGUNPGfHZUVx0_Tj2s8YqqyfuLxLODQMKvgIQh2HL9xo668ap0DqB55isW6bmuqsKvDuJs7Rk49oAjFm69PSMnsSiFUf5dUTgN7TZpVmG7lYbU-28pdKz3j-P-mKvn0DXWFndLEyRaiifpMYqbJ29cfXhJ0eIJaFRXHiiqIkY7nP9v3WXN6VLN0yL_JPsCqyyQhRH5b5fPiR6bNgSbO89pYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=qql3SCeL_e00Kx3A5E534c5BMlhO5HNpwGs2gaO2mRa1bPV0jlFsTD5QH8gYYOGNWXOHIdqyL-5EXhD29gvv1V77NcfTWoGS0EfImtgQHRm1PViSGW2xwcjoe4O8QKIGUNPGfHZUVx0_Tj2s8YqqyfuLxLODQMKvgIQh2HL9xo668ap0DqB55isW6bmuqsKvDuJs7Rk49oAjFm69PSMnsSiFUf5dUTgN7TZpVmG7lYbU-28pdKz3j-P-mKvn0DXWFndLEyRaiifpMYqbJ29cfXhJ0eIJaFRXHiiqIkY7nP9v3WXN6VLN0yL_JPsCqyyQhRH5b5fPiR6bNgSbO89pYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=gbYvGViLQ9LIHLt51jPBpqyvHazti9BGW4UpSuBHWvDoNVyZVUgQ2-S3mx9m-bpphHHNvv5m-raDnj8SZpFIL9e_NgClJi2o7w3hSN1kUKvIUSKfjmObBE3dFyJQQAGc1eF8eVh_-RJu8YCFNz7qqUm5yRM2CBaHOoIMgzLFMTs7YvYAS2oPx29ULwRdxBTuXmYeqUmI5k_wPoN95Cjas4xdUii1KYbJZIbr_kV7mKbxgqyAIqdkTpgbwjhN9GCfiugJ_4me2nU0vfu0ULzaI1H8zh1QmzBomCIYE-iCNT_mBXGde3kEHy1IMrotzRSadVhm2V5wpiuok0oCdNTLkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=gbYvGViLQ9LIHLt51jPBpqyvHazti9BGW4UpSuBHWvDoNVyZVUgQ2-S3mx9m-bpphHHNvv5m-raDnj8SZpFIL9e_NgClJi2o7w3hSN1kUKvIUSKfjmObBE3dFyJQQAGc1eF8eVh_-RJu8YCFNz7qqUm5yRM2CBaHOoIMgzLFMTs7YvYAS2oPx29ULwRdxBTuXmYeqUmI5k_wPoN95Cjas4xdUii1KYbJZIbr_kV7mKbxgqyAIqdkTpgbwjhN9GCfiugJ_4me2nU0vfu0ULzaI1H8zh1QmzBomCIYE-iCNT_mBXGde3kEHy1IMrotzRSadVhm2V5wpiuok0oCdNTLkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=PycC7ftIu-Bmw1oUOCBm55PlDl8QgHVcFI87sZZ3g1cIDFiIe2sICoUzsSI5SKv-7xAWaSqTI_-nE_1HN_3N1uvmlqbm2xDS32D9B1Gbq4DH4fu4WyAtGnPCN-E2ru_8wvmEHcXlcZ93ZMCb81OJziH3iOMA7KsKGlr8_ZgKAjZPntEiIePCLmjHOyf3F2OLV0wSpBL8wkjvDMtfQcW2oektSSu3qqxETFpJCb88Lh4ezzIVmeXPLDylR7uTl2CmnUHtwvpnpbjvF3Gam_6UHyNvYHRMZJcteZnIA_20ueP7p9QGSzdFXZF3baObYh262EPJUp00n3o4zsVLWlFIQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=PycC7ftIu-Bmw1oUOCBm55PlDl8QgHVcFI87sZZ3g1cIDFiIe2sICoUzsSI5SKv-7xAWaSqTI_-nE_1HN_3N1uvmlqbm2xDS32D9B1Gbq4DH4fu4WyAtGnPCN-E2ru_8wvmEHcXlcZ93ZMCb81OJziH3iOMA7KsKGlr8_ZgKAjZPntEiIePCLmjHOyf3F2OLV0wSpBL8wkjvDMtfQcW2oektSSu3qqxETFpJCb88Lh4ezzIVmeXPLDylR7uTl2CmnUHtwvpnpbjvF3Gam_6UHyNvYHRMZJcteZnIA_20ueP7p9QGSzdFXZF3baObYh262EPJUp00n3o4zsVLWlFIQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=tyWIAT9OZQiLu-jRJD8xveondudaTXhMv3ABAoRIaV2DEGIsfQsAvCLCRpnL9nqq4vBbb_fVLZJoRB3IgPU3HHKd8om2yJsLyHHpUc_X_l9N3bgKdJgYk7bGjq4hCiotghR6Bq1TPGGDgmK5_XkktGR5ePC-rENU59xStDtxI_gSCzxq-HVEH7_w7blrtrFsYyfcZWWxcE8njP5tecgpeUcgE3jZE9-ZxNM4aRyflggcWNJPqlbwqyb2qvTxj9mxLHGPAttYz5GhLHuCQudmZLjJab2UHGQdafIS8EItioueLWgmiDB4RQJYJ4lTHvF15Nma3n41pYsd_7JJ-KRF3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=tyWIAT9OZQiLu-jRJD8xveondudaTXhMv3ABAoRIaV2DEGIsfQsAvCLCRpnL9nqq4vBbb_fVLZJoRB3IgPU3HHKd8om2yJsLyHHpUc_X_l9N3bgKdJgYk7bGjq4hCiotghR6Bq1TPGGDgmK5_XkktGR5ePC-rENU59xStDtxI_gSCzxq-HVEH7_w7blrtrFsYyfcZWWxcE8njP5tecgpeUcgE3jZE9-ZxNM4aRyflggcWNJPqlbwqyb2qvTxj9mxLHGPAttYz5GhLHuCQudmZLjJab2UHGQdafIS8EItioueLWgmiDB4RQJYJ4lTHvF15Nma3n41pYsd_7JJ-KRF3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=hZleHH8mTTeuwzrCBnbr0Re4ETaHWV56OoUVwye_96E6J1KvidCBpH_4Eyt0rv_GpazS7g4dzjDXOReMYrEQQ9OMZySrVXSkVTdKSXOeSVG7PlDnTEXJSBI4qQpFbV3sXLB9YtcywG_IoiqAEwrCEOoxFcgmaKb_OdTQefIcadzDAeIXf5CUzKuGVxaBZ_jSHwNf2F0asYXY7w_2JAfOTVQ0rp5Y2SnPe-qkbN3NpThphonBz2yugMSUJTqeh1JFF7F1kcds3vILePuvRBZ6xWHzY3pRd01z3hPcdG0-G_ZJpdxM7k4TOoe7UguSUieYv7SZsnhch53yeKG7pEblOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=hZleHH8mTTeuwzrCBnbr0Re4ETaHWV56OoUVwye_96E6J1KvidCBpH_4Eyt0rv_GpazS7g4dzjDXOReMYrEQQ9OMZySrVXSkVTdKSXOeSVG7PlDnTEXJSBI4qQpFbV3sXLB9YtcywG_IoiqAEwrCEOoxFcgmaKb_OdTQefIcadzDAeIXf5CUzKuGVxaBZ_jSHwNf2F0asYXY7w_2JAfOTVQ0rp5Y2SnPe-qkbN3NpThphonBz2yugMSUJTqeh1JFF7F1kcds3vILePuvRBZ6xWHzY3pRd01z3hPcdG0-G_ZJpdxM7k4TOoe7UguSUieYv7SZsnhch53yeKG7pEblOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=o-dJZpuPRJ5ln_UZEU1SzjdZCglRV2qlCwK1fp7bWHpMapO5tHqzbKXZ6rkyzuvtjQ1V6HxCSIrl8jtpeRhk4ZkR2LpIIvcAMZyPaUSKhVg-u_TiUKDwRAVSumoU8PHneOfz1YlTSXJ5Qns8F_zsunyIy3a0DM9K2NLDEj6Hz7CQhw8OIGEZjDSAwr3hodLD4TIxNCo9SQBEsnsCDToR4jtRgDJlVxyW_e3BuXAazzRQuPGB2MU077wURHrcfdmDG89W7EoTqvj8kmt3uii3XzqURqcombVpenq84RFxHZo5IgD7Dr5iOIQtmxA8jnLQMJq_QsJayLViXq9DQfZrGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=o-dJZpuPRJ5ln_UZEU1SzjdZCglRV2qlCwK1fp7bWHpMapO5tHqzbKXZ6rkyzuvtjQ1V6HxCSIrl8jtpeRhk4ZkR2LpIIvcAMZyPaUSKhVg-u_TiUKDwRAVSumoU8PHneOfz1YlTSXJ5Qns8F_zsunyIy3a0DM9K2NLDEj6Hz7CQhw8OIGEZjDSAwr3hodLD4TIxNCo9SQBEsnsCDToR4jtRgDJlVxyW_e3BuXAazzRQuPGB2MU077wURHrcfdmDG89W7EoTqvj8kmt3uii3XzqURqcombVpenq84RFxHZo5IgD7Dr5iOIQtmxA8jnLQMJq_QsJayLViXq9DQfZrGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9MjA8yRVloSYI-ZLV7CX_Mp_PtdnEu_nMTBKa-k1xs6X4Rj6clVH7n6Ud4-5eByCq0ZlbLnQpvjhVuLrX2aJnxNZtuKU4crvIy90rJlI_MjrNsTlQuhzN5WTM9-1q3wrkVipV5IrhGZ8NnBzf7oP1pCfRavPHNYXmc_LpI49EUSo74mt7CfkLPss4Guv-QRNnCeqwAxFYAOPaqYQWk-piXIUxD3TaByXIcOr5uHfyrpICsziwJbRiaGlbKg-37RayE5D73-RJxAb_Z_c-szFCZfcbcUPjCpl6lxndqmaMpEGWET0QWAiIrjmUUhd9IvuPyRC0lvGtnsiuWmEB7_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=qkFyQ5eo2Ygbx0Cw3IgNAV_I_bwweOXFRpobYvZ0zXlnNojIAsjiQ92uADZeVyA9KMHuSapcGDbmKFCi0jo5H9e5mohP43-3Y9l62aPHL09qJiATblJReasyWW9SVhMiwIO108axldWAmT22_d0Xv8tF7YjrTFfggp5VbndJE1S46u0sPmc2xxW5pCGJWY-2kF963KPit5EhCzCN1rzLr1wdSr6zU3zOV359-OrhQCr6qgCqz5tx10m-nEFEqFoQ8VBG6zXSE1mWrxh6wtXYSzt1RuIKyvFbGmNJ1lDytSVrl8gB-RRZfTOTY85O_uxmNgNo3JTitW_rr4n8tbdZ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=qkFyQ5eo2Ygbx0Cw3IgNAV_I_bwweOXFRpobYvZ0zXlnNojIAsjiQ92uADZeVyA9KMHuSapcGDbmKFCi0jo5H9e5mohP43-3Y9l62aPHL09qJiATblJReasyWW9SVhMiwIO108axldWAmT22_d0Xv8tF7YjrTFfggp5VbndJE1S46u0sPmc2xxW5pCGJWY-2kF963KPit5EhCzCN1rzLr1wdSr6zU3zOV359-OrhQCr6qgCqz5tx10m-nEFEqFoQ8VBG6zXSE1mWrxh6wtXYSzt1RuIKyvFbGmNJ1lDytSVrl8gB-RRZfTOTY85O_uxmNgNo3JTitW_rr4n8tbdZ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=QYFEQbJI_G4jPqoFUl-QhAF1mJoWt9cyrV1S12G_Ah4AqNsarExNzmjGkT-LDievMw-JkBP0edqvg1dxwAqz6eCFLEevWkO0Gxq9cuvZZRgiDAIGFYSz_iu74jHk-1Mwe_yt_veUa8GITBdhBV2alG4MaKJCziAw4n5yJ9BOtiziLej64SAk5LUX6d4HEdUpncHk7CzprxxE72J9359VkxQcGVWZQgt6nE2azAMDpTs3L27PGhr0g1kB5HWVZNZgFGf6fC8Ms0qYlmqBf2_0E-yXW9t555W_RQCaRSgJ_Qe6lrq9gMWF1z2Lm-NBD4xrwmcuEPr0wxNWDcjyHOzGQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=QYFEQbJI_G4jPqoFUl-QhAF1mJoWt9cyrV1S12G_Ah4AqNsarExNzmjGkT-LDievMw-JkBP0edqvg1dxwAqz6eCFLEevWkO0Gxq9cuvZZRgiDAIGFYSz_iu74jHk-1Mwe_yt_veUa8GITBdhBV2alG4MaKJCziAw4n5yJ9BOtiziLej64SAk5LUX6d4HEdUpncHk7CzprxxE72J9359VkxQcGVWZQgt6nE2azAMDpTs3L27PGhr0g1kB5HWVZNZgFGf6fC8Ms0qYlmqBf2_0E-yXW9t555W_RQCaRSgJ_Qe6lrq9gMWF1z2Lm-NBD4xrwmcuEPr0wxNWDcjyHOzGQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=mCxyCjkStl4Na56ejKwdt8k2C7AVti2_b_rQiXpcAnIcy2IeHnvwDzphypw-xwponUDSjaszR2CQabe3guHzlLt7cjzElKG8Rz_sxT_KSOtZRMqrZqhrE6KO4yWzeDAC8greYtMRoGpmTLGjXhhRU5RbedakIYWMOB3Cqc_DHEFZExfSh5l03NsJ_atPnJWqA9nNP1vUw2jWvQe8te5QzUOFiQNC_WLq8Or7i8O2O4sAbogls1PtIfixJ4CZkjP3Gdh6b1qFXEY-Odm9MxyLsnTF91g4Hal9ssN0AHVDYzPHAeHEdi0ydVvjav9EbmurDEkI4qOvQNd5Jyag4Xm6mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=mCxyCjkStl4Na56ejKwdt8k2C7AVti2_b_rQiXpcAnIcy2IeHnvwDzphypw-xwponUDSjaszR2CQabe3guHzlLt7cjzElKG8Rz_sxT_KSOtZRMqrZqhrE6KO4yWzeDAC8greYtMRoGpmTLGjXhhRU5RbedakIYWMOB3Cqc_DHEFZExfSh5l03NsJ_atPnJWqA9nNP1vUw2jWvQe8te5QzUOFiQNC_WLq8Or7i8O2O4sAbogls1PtIfixJ4CZkjP3Gdh6b1qFXEY-Odm9MxyLsnTF91g4Hal9ssN0AHVDYzPHAeHEdi0ydVvjav9EbmurDEkI4qOvQNd5Jyag4Xm6mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=jUJYGLeq_pUDAimTBdadTSOnN5jl_SYJdanw84Axidx0zwgnQ5Z_vQ382FhvRxiLuPXsB5uAqUwmPbW5GKRIDEmfKxeWHxQ1p1ynSg54T1nC3jCORMWERM7xTHVzjUV_Enjco4DtLKXHCJAITIEKi5m-VO1ySrWLwttTdJ8Msb9lrThQyYsbDD8zP15Xtd4sGEg7Cg0v5nvMmURNUVDJB0MXIflkNt32cQFR5APz2_dpOxkJikp9JhS9zqX5p6iNBP5p9QH2DDKgRGbEa5w13jsnY3aQQxWCiSr6PTkNC94I8_FnzlfLALw-VWxQM9BSGtkGcmWk7iEKaxEY0026CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=jUJYGLeq_pUDAimTBdadTSOnN5jl_SYJdanw84Axidx0zwgnQ5Z_vQ382FhvRxiLuPXsB5uAqUwmPbW5GKRIDEmfKxeWHxQ1p1ynSg54T1nC3jCORMWERM7xTHVzjUV_Enjco4DtLKXHCJAITIEKi5m-VO1ySrWLwttTdJ8Msb9lrThQyYsbDD8zP15Xtd4sGEg7Cg0v5nvMmURNUVDJB0MXIflkNt32cQFR5APz2_dpOxkJikp9JhS9zqX5p6iNBP5p9QH2DDKgRGbEa5w13jsnY3aQQxWCiSr6PTkNC94I8_FnzlfLALw-VWxQM9BSGtkGcmWk7iEKaxEY0026CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G63VFevZ4GthOxtglq59kLu2dLDWyiL7lHj1hQ2ITKJec-Se2kVhcL5HcEy4RTk534f-Se3vCkHCh8AXnjybt6Ew09OxhGyWfbxeK1UZwJkeNu9UANtqmxNwERA0ckB05szTza2IGgNL8wauL4MNHb4-ACsnmNtuUzkUpRkP9b5gkISv1N5amD1f6YKkbRjxlBPSyn0Z63GEfR53e4sNmKwdwzcAxI7b_QZrz_leJd07xjKxvzdUdPcdHzXJPSTbHAcqU7DijwaCklnZYovNEAiNRP3miaRlCvj-8Sm6Jx7m7xYaEh7GlswVI6khM7rcSx3a_A21-fWex8GEBnWBvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=fG3xT9RO1d2ryu6Bht35bFw8_Q40DXVh-OvCjVHswIlYOuJABp2WmoD8SiY1IpINGxkDtkrW91LSIKuZx16zosbnzx9_GPD-pFn2yg24KMK6MyzKeAG1ihla5YH0LtXBEOhoE-fw-v2hImj-He45LUi3zS9DqET9YyNkz95P-_sI3HMjIddujhki25PKtj9QGKOE29-dwDNm3odR4hozQ4V5gm1DsPS3vRWIwbBV-Ycbo1MdGFDMysXrwmXNasQQ0niSSNiNU6HVhfJveA6jUuBYR1ytIuJwL6UXy5aBOpiNYokKItjXZQ4_E2xi-cVht-lQj_V_PgNSMlzzp9ftR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=fG3xT9RO1d2ryu6Bht35bFw8_Q40DXVh-OvCjVHswIlYOuJABp2WmoD8SiY1IpINGxkDtkrW91LSIKuZx16zosbnzx9_GPD-pFn2yg24KMK6MyzKeAG1ihla5YH0LtXBEOhoE-fw-v2hImj-He45LUi3zS9DqET9YyNkz95P-_sI3HMjIddujhki25PKtj9QGKOE29-dwDNm3odR4hozQ4V5gm1DsPS3vRWIwbBV-Ycbo1MdGFDMysXrwmXNasQQ0niSSNiNU6HVhfJveA6jUuBYR1ytIuJwL6UXy5aBOpiNYokKItjXZQ4_E2xi-cVht-lQj_V_PgNSMlzzp9ftR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Qo-S9NiPiPCzC5buksnQDSTWXYSm2yjADP9SBICmYQljLw2S44x1rrZg3AU9ES0cIV21huoNM7IGQFDn9_SZMGegvqK215n_jJsKSsA7N8-Pop2rIN-4mncA4gA47CWQFNoG0A4S4iwSMwlK-2a7SvguY6usHiYb1B70ujQ-vad0UT-_6Xt9900cA9EGo93vGN3KiAZdFU0hWW8KUMOpbBpm-d6XgOc_keCrn2aXQAfOnWhdZffoPhzNZUV6eyPUKaabg3TT3sJ0MNt66ZIPBu4IZyp_N6TOccNH_2H9NELuyRR6LTGSse3N6_v2_YQpq-DRTqGCjwSJAk6i3to6jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Qo-S9NiPiPCzC5buksnQDSTWXYSm2yjADP9SBICmYQljLw2S44x1rrZg3AU9ES0cIV21huoNM7IGQFDn9_SZMGegvqK215n_jJsKSsA7N8-Pop2rIN-4mncA4gA47CWQFNoG0A4S4iwSMwlK-2a7SvguY6usHiYb1B70ujQ-vad0UT-_6Xt9900cA9EGo93vGN3KiAZdFU0hWW8KUMOpbBpm-d6XgOc_keCrn2aXQAfOnWhdZffoPhzNZUV6eyPUKaabg3TT3sJ0MNt66ZIPBu4IZyp_N6TOccNH_2H9NELuyRR6LTGSse3N6_v2_YQpq-DRTqGCjwSJAk6i3to6jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pw3iNBROJ03lY51c7V_oDsaR81lvGVMNXWtwMXHG-Q76H2bIyqNP_uYMhZBkTGM4WQEyUIif5G-BzZC6qZ12Z7LlaEvwAez6haPM95C0NbKRli1UdjGTxdbJ6hBQqqrJZb4qKuLPNnBFz54q3zrGF2YzM9JkD3avEfakEU9zs8Gf1Solh0WItVhnGb0wvbPNZpYEV2PkMv_gRuuOGm0Gnl7PvFVFeKKCuc7ioF-9B2nds_QMcn7GKLzW6WIVorpdzk4v44W3g4lUfdoh0PAz2jz1cwgAE8I9F7Z_VmJ34ADaO9T8nW9K5j1CBvYe4xpWNEom-66d6o_PKO_EIsqamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UktcJEU9MJcz0JH523J9VzqzFTFoZ8qopDmBnOQDQP2KB4ZIqbLOUQkkohXVguTwfaWEQSD56DeDnce3pqUcu1m8p8Uftcd5mndKRZR3OpG7BynJ4WDiMr5HRZWwDDyt6a_YT6ywSeK_GAKwtvu8a6oADyNmnQsJzaj9CPmSNy794IykgGZQeIkHSlAVOB5UfCiOlM57ywf0llXVt0gPmkL3RKL8ZK46gt0A3jNac6n3CHzjA-FtlPukoLRNiFZtwbisp3tMEUM3mYeFyKTS2tDphzwbIhVEDCzhWaOnQ_AnTUFLIBB7z5iseWE2j5AATW_3TvCaLRzEVmSEmDLH3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=nioXlY3mIF8CSyq2tMoTEurUFeWZBMu7m9GeIXDbiFkDUhM9Zf8-BKF2ug42-jT30Bbd_jDaeUa0VWdEUVfV1NEStQ_DtafN8wo7rYtYzmwgmEB9C4dvKbId_QykYvY0p97qyV_-3RHw-ONjU-x0Em1J1qMMhTF-rd-uTwiwsOoBYBV1uGsFh4X8DyF_4ObBrPwVEENi4f83oNdg8sqJbJq2RjKxPcLE92-dt-FtGp7NjpT57ISJ3yAXSBgVo4h00QvlJ4F9dYwiNlU8m9DJtM9F_KEIVJ9tcBal4-5iZUhIYC--wHquhHu8ptavfzF6ta_iYVnwVtJo-21MzPhQBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=nioXlY3mIF8CSyq2tMoTEurUFeWZBMu7m9GeIXDbiFkDUhM9Zf8-BKF2ug42-jT30Bbd_jDaeUa0VWdEUVfV1NEStQ_DtafN8wo7rYtYzmwgmEB9C4dvKbId_QykYvY0p97qyV_-3RHw-ONjU-x0Em1J1qMMhTF-rd-uTwiwsOoBYBV1uGsFh4X8DyF_4ObBrPwVEENi4f83oNdg8sqJbJq2RjKxPcLE92-dt-FtGp7NjpT57ISJ3yAXSBgVo4h00QvlJ4F9dYwiNlU8m9DJtM9F_KEIVJ9tcBal4-5iZUhIYC--wHquhHu8ptavfzF6ta_iYVnwVtJo-21MzPhQBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7wQC9DYK_aTOHkOfSouJ-20X80leoJPAvqhNKTbqD6Dokh5mwHeSKRzsX08HEVlk_l037bEMnYfk3Z862toOwkvc39yH1dWVL_2cI0rv3R146sToQporxG9Fy6V0y9VUIJfRI6vLtbOXEH2avf9on3v88V0qGQ2IZoPvE7wXTuIbQkvvGLgo41Z7B1gABeP1C54AkMzthUP_AP7b2RGLQ6nqRaot8XIN9orp9cllWw9DF2LGjImNPLfVA-AhoTn1wjBShMahyh_LIiQTVliAU0M2CjHqpfCzIkbjBpVneaCEIlAQK5VY_HnFuJw3LOZO9QB5kkxrQeK7B01iAHEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrngu6S95xKlcoCLb5CKw8O-e06L_vG2JHbyLDcCCrABrLF65e8WkbhGLIVysh97WEPBcAWoXWZCkYwDx6fi7rstUDGKbhPVOyXCEpaxyLVvKUW3aoAdkSwTYfO_mk54TUDM38U-qNEKoeFunlv0AVoPiJmKFdeH-NG-tWVV17WcXi7M-rahV_XzadKKPDx8z7nSlqVwr4LRTktLIx-Wb-zYgPUaRMTTLxUmr_jxeQfWrQk2bwgf7ft3m4UCyLrdlMWkeTVXvHkGMf0mU8ntcr4DVj9fP3r-N2fwC6p1UB1motNoUy3Hu9mavaW0LlA-S4VCWTHetA7CH8OgLZxlKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a45lnBKLQ_oPCwBReeHb2DnEZs48lGUm42xYVkZ1j62n7usWF56ct_ifJT6PcXaVvuWCeHBq5zVg0CcAHtxwAYtNsmwT9p0UklTwqkNqLrz9AfquVeujwBSKsWp8XmlJ_KsxSKxHfB1bcmwu8zBSGtB9YhvqbefMHCfqUxOJ3ngQFj29Fd00hFNVFOA8w7tBSPbpQzrYEtB5F8x1QuyPa6tX2tUWUwjyclwMblcEMScapxGlfqVLwr-4nNNVIk0lf9RNDKXtjLfkkY34cHbWZGSwjY8YP797UJ8309ZSZJx-m96uo_JVjONIZdQOq3FRHDF6pdHd14IqSvn05FBmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=u8Kns08iKfV5_WPlKZG8FOepO660yoyJdLU_LGy_af4BU4dfXPeMsiJ9jRiciLGdakNyHteJDu_SCf-uv14s0xW4Coz8Zgaiv7hcaSdfNJFnmfco4d5nZje7t0aPeevQX9Q1Dvcsks3b6zvCD2KDG1sEhZHESkIHoprWhh3o3dyOtuTbeLnZygWAsfLk9tZ-awK1Y1F_TN7rRRGfX85onVR15o5nkgDvcgLXGwQMTd2CIv75sjo0p05fBxD56LaBVS3KSO3VYwiKaD0p1vA3OaPSibI7w7PNkenwBY195Bl0lbuIJahrOXMMsaqPxFconIzJytiBSopq2NH0q6ptrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=u8Kns08iKfV5_WPlKZG8FOepO660yoyJdLU_LGy_af4BU4dfXPeMsiJ9jRiciLGdakNyHteJDu_SCf-uv14s0xW4Coz8Zgaiv7hcaSdfNJFnmfco4d5nZje7t0aPeevQX9Q1Dvcsks3b6zvCD2KDG1sEhZHESkIHoprWhh3o3dyOtuTbeLnZygWAsfLk9tZ-awK1Y1F_TN7rRRGfX85onVR15o5nkgDvcgLXGwQMTd2CIv75sjo0p05fBxD56LaBVS3KSO3VYwiKaD0p1vA3OaPSibI7w7PNkenwBY195Bl0lbuIJahrOXMMsaqPxFconIzJytiBSopq2NH0q6ptrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=uCmhiddqeihcWMiDEeGhZYuYYh3Oc2es4EJQavHvki84aEKFoK8mzxqXUyCNZJCSu_AbBsl2WTYNl7mgbrXr-KfExxur4i7MhjKmbg8Z1nNmfwUf9b53DUBbFEHzHGWkI--ClG-kQjHs9CO0wz19czilfCALB8PTOCIRWb7F3af1aXe-WCApR38oC1MBtgogOrBi5cub0bdhIXJtSZyf6zq3NXfBF6TDe888UrqS-PWcegIXPmVa5DoEk1Y8FFpv0iFEVVGvGq_woXaFb00I7-Ypnn7WbaZbdvfoT_3Lx_ic0_FuThiK7qjlLq2KP4vOO3CmoOQlNoopJ6Wpov6zvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=uCmhiddqeihcWMiDEeGhZYuYYh3Oc2es4EJQavHvki84aEKFoK8mzxqXUyCNZJCSu_AbBsl2WTYNl7mgbrXr-KfExxur4i7MhjKmbg8Z1nNmfwUf9b53DUBbFEHzHGWkI--ClG-kQjHs9CO0wz19czilfCALB8PTOCIRWb7F3af1aXe-WCApR38oC1MBtgogOrBi5cub0bdhIXJtSZyf6zq3NXfBF6TDe888UrqS-PWcegIXPmVa5DoEk1Y8FFpv0iFEVVGvGq_woXaFb00I7-Ypnn7WbaZbdvfoT_3Lx_ic0_FuThiK7qjlLq2KP4vOO3CmoOQlNoopJ6Wpov6zvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=TLcF-J8wGc0oQcR-c42L39P3n4xBQL9DL8NOvQPNRlTCq1oWMw_E-KVwgACqd4782ytpXcqMmhajLMbdjCaYCTt6LCertv8rVULGyhBb63plAbVfkU0mQePNhxir16aOUADi_pj5zhOVQzxeQy8z34u2lLs18KXeS1P2o8HeaPbRe2_L1S-aX_X4QNld00NwNK4_juj0To_gKGGE5dD4SuioWWkVMzfSV5_nGodbGXuShj1h1Mo1GI36efrrEgwbOUqhiXoLfab6ote6gYtSqBEUjBKBZyiuKjIC07ceCeocC-FUeoGi3n9gy9ti5t3cuc1Y_x8fP_wnhPZioNlKbyJD85SVz00d4uIs9sbfFBoLVD0_FOlNrLs3wGq4Vfbiw69rgAbQZjKDht1-tBqFOHkuGQZXMK_HYtPEDL5eC55al6UkW_7dL_gV5V6a5Uh18U7KDaApex_797Zh5trobKcNcdScGA_v6f4Fc52YUdr479j3hNe3j1lLgGmXjIhkfeV5nI3V_jw07R7UuuQeqq601KbwaIip_vMeQTqsXIN8B0T22PjqCpiltrW0tvrz1Azv7IGxqRcP-0_aNcaek2pSGKV3uQu6DdPNCMBcgH_N8_ZTTx9-aMz1vslk1oeTrj7LxKolf_e9NAML9tDGM7iea5gzFu5lCB8eIT5ZVAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=TLcF-J8wGc0oQcR-c42L39P3n4xBQL9DL8NOvQPNRlTCq1oWMw_E-KVwgACqd4782ytpXcqMmhajLMbdjCaYCTt6LCertv8rVULGyhBb63plAbVfkU0mQePNhxir16aOUADi_pj5zhOVQzxeQy8z34u2lLs18KXeS1P2o8HeaPbRe2_L1S-aX_X4QNld00NwNK4_juj0To_gKGGE5dD4SuioWWkVMzfSV5_nGodbGXuShj1h1Mo1GI36efrrEgwbOUqhiXoLfab6ote6gYtSqBEUjBKBZyiuKjIC07ceCeocC-FUeoGi3n9gy9ti5t3cuc1Y_x8fP_wnhPZioNlKbyJD85SVz00d4uIs9sbfFBoLVD0_FOlNrLs3wGq4Vfbiw69rgAbQZjKDht1-tBqFOHkuGQZXMK_HYtPEDL5eC55al6UkW_7dL_gV5V6a5Uh18U7KDaApex_797Zh5trobKcNcdScGA_v6f4Fc52YUdr479j3hNe3j1lLgGmXjIhkfeV5nI3V_jw07R7UuuQeqq601KbwaIip_vMeQTqsXIN8B0T22PjqCpiltrW0tvrz1Azv7IGxqRcP-0_aNcaek2pSGKV3uQu6DdPNCMBcgH_N8_ZTTx9-aMz1vslk1oeTrj7LxKolf_e9NAML9tDGM7iea5gzFu5lCB8eIT5ZVAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=NKWE54clRSdcRKvdrBjujoICgjzBkUlPLniCWThKXqcVU2ah8-2D7KtRJY9-_UO3HwEDeLl9pKK_sUiu6KrxJdJVGj08vroJr9utHH31dvxUzluL68eofM-JjMRHtWZ8P2UUNF-mZyKzAc6pAOoLjxR3ZGwCrbsJDUdTXmNPyCjI3Drebh6OZhMzatCu6s5rAHrkfrxx49QxTLEElXDvbpcDKukPifqjFsCieAgNEGFFaRuRG2XAb2xPhWgx8e90EP_MM1jU7Dh-i5k_y7t_pUqEsqhVJfEw_L2a9DHjRBtNz23tuxW0eWvUdUc4fCU8znihQLJ4csq1ODzVB0Xn0SHfh4Q_NQN_bbhk5Hm0bKv2a5vCuUqW9VO3kThMt1N17xKrxNYwQowocHKqrFdn6DzgJrKxQ-m_TwxHt20W_YzxzBJwXZtEjBNuW7n-iBow_Y6B1iQb6b3acQcBYrZQ2VB8hUCL0ihnrupoR9d-AtOZN1IEF1zkV3VrANZBXC8t4c-_JQuFR5b9y37acX0gpJJW1hmJpk4dT7uoTyW6UxD0SQD5Xbh6M617rwyC50c-tiqDiXii1JooefyAWIGlV9jLQuocDiYif9rEyibCmMDZMQryefs6tbL4k-9EWiv10BdfyPXqYKaPjEusLMQ2n-4bPR9jcJHw5wsCxHC__VE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=NKWE54clRSdcRKvdrBjujoICgjzBkUlPLniCWThKXqcVU2ah8-2D7KtRJY9-_UO3HwEDeLl9pKK_sUiu6KrxJdJVGj08vroJr9utHH31dvxUzluL68eofM-JjMRHtWZ8P2UUNF-mZyKzAc6pAOoLjxR3ZGwCrbsJDUdTXmNPyCjI3Drebh6OZhMzatCu6s5rAHrkfrxx49QxTLEElXDvbpcDKukPifqjFsCieAgNEGFFaRuRG2XAb2xPhWgx8e90EP_MM1jU7Dh-i5k_y7t_pUqEsqhVJfEw_L2a9DHjRBtNz23tuxW0eWvUdUc4fCU8znihQLJ4csq1ODzVB0Xn0SHfh4Q_NQN_bbhk5Hm0bKv2a5vCuUqW9VO3kThMt1N17xKrxNYwQowocHKqrFdn6DzgJrKxQ-m_TwxHt20W_YzxzBJwXZtEjBNuW7n-iBow_Y6B1iQb6b3acQcBYrZQ2VB8hUCL0ihnrupoR9d-AtOZN1IEF1zkV3VrANZBXC8t4c-_JQuFR5b9y37acX0gpJJW1hmJpk4dT7uoTyW6UxD0SQD5Xbh6M617rwyC50c-tiqDiXii1JooefyAWIGlV9jLQuocDiYif9rEyibCmMDZMQryefs6tbL4k-9EWiv10BdfyPXqYKaPjEusLMQ2n-4bPR9jcJHw5wsCxHC__VE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=v1n5FibMhK3d0-ezf9wC1v-y9vAtWfGYApAeSd4hC5D7rIPu_uS4em2k389dQMuJUtnnRxwt_nd0l53Ps8F570aBhv7Cl6SvyPvMv3KiigMJz2vfhYvLPEEgUnh32N7AJr0_lcF44snGw18g9a2bIer3633m4zio_b9BdMN0ymCzdyWvrf4tl7lmjT4eozWpHsODALr-EQccCGA0ubVi1WAKB1jksoSdjRlCKGdqqiEHJXtm44ukF2rbGdnSlKeoLY9o1noOv6apsjz9PuFRMcw25u3OavJrMvu4hV3Ws9VLs54D7gQyYs9KzNf7tfE5m2w46meiTusWnACt_DNAeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=v1n5FibMhK3d0-ezf9wC1v-y9vAtWfGYApAeSd4hC5D7rIPu_uS4em2k389dQMuJUtnnRxwt_nd0l53Ps8F570aBhv7Cl6SvyPvMv3KiigMJz2vfhYvLPEEgUnh32N7AJr0_lcF44snGw18g9a2bIer3633m4zio_b9BdMN0ymCzdyWvrf4tl7lmjT4eozWpHsODALr-EQccCGA0ubVi1WAKB1jksoSdjRlCKGdqqiEHJXtm44ukF2rbGdnSlKeoLY9o1noOv6apsjz9PuFRMcw25u3OavJrMvu4hV3Ws9VLs54D7gQyYs9KzNf7tfE5m2w46meiTusWnACt_DNAeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJTqDsSOfGQZKCdu3k5kRNm9AtRz2Jpv0IDPXoNXToJJ51Nj49W23M--9Rxhf5ERLzZt9avw7Q7N3Grn4c9Yzjpg_u6eOPShu6nN8X-jD3ATwgjMHaY_tipa0fRmrhMMHVz-K5K5vRYW5eSOiu20WaDaGuNsFcRaBk6eegd3S0QXNAwYJ5Ef31aVi9Ra519Uh591cCLND4B0bxx7gTiwI6TcD2_H8DfWDRIlXBRq096pIgb2jbTjwi3fDhJJhXDlXzNfswqjigSs7MJxqurc3ypVBIIwxYShkQ9rRr24yA0afkU5BBEpOmsCO2Vavd6JoOJhUeVIL0ceXsXiA06kAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=KGYK-PfiTbJby9n3TFoUFuIaDHcyYCbd7KJ0rGg3vtJAFdsRDEGK0P_dECc8mhJQcUFf5W00gAaaxptWz5aKLldMhJXrtPiXtHUpkZKiVCJnFsnt37rPSNWkm8DmTsL2-PcGFKBb9HWI5PfGqm9yoM7hZVMOBOVrW_jUUsrmVI7PlpPQi1Rga2A4jtGQwV_1VOLEiq8tkkWk9tfNE3kDeb3XYDFGoqkUMaSdzItMh6H-UKSSk0YYu9UFBDvLea4exJWBJB0EN1hzRKZNAGjmoi1TSuiyknDCBooXh5X7NQT237W4S26k10p_KTFjyKhrwFEPMtrKRLsGx0c3wrV0pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=KGYK-PfiTbJby9n3TFoUFuIaDHcyYCbd7KJ0rGg3vtJAFdsRDEGK0P_dECc8mhJQcUFf5W00gAaaxptWz5aKLldMhJXrtPiXtHUpkZKiVCJnFsnt37rPSNWkm8DmTsL2-PcGFKBb9HWI5PfGqm9yoM7hZVMOBOVrW_jUUsrmVI7PlpPQi1Rga2A4jtGQwV_1VOLEiq8tkkWk9tfNE3kDeb3XYDFGoqkUMaSdzItMh6H-UKSSk0YYu9UFBDvLea4exJWBJB0EN1hzRKZNAGjmoi1TSuiyknDCBooXh5X7NQT237W4S26k10p_KTFjyKhrwFEPMtrKRLsGx0c3wrV0pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=AoJMKPEOZkwt9FGzQ7U0NINVCxRRMSyE6YtDB8NVuqaASB1U5qiJf5foC3vXdfhAW3PUuhkpr_fg3H1JTdyhx2WV2w6U17esGzJO--m2bxPUHECA9QkyLTt-l12mMV_HXEsDbH4PaTclpRQrDzAgGWSWRHHRCjdBGzTfA30vLNFvAKwzc0rc9tzKLt2RKQ3E_IypkNrDx2W1s2jzOjW25aOzbeJ1BP-xlaECsNvwr4SCsIt1WV9qyC_amVWNLvMrTNLwJo4Wc6IeqpUa5fts-kn6InGFI8eULcTRY8xH1PpxD9_YiDz-0DlRyBCo9oFyJHfQWabrQ8xHdBwIYZnHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=AoJMKPEOZkwt9FGzQ7U0NINVCxRRMSyE6YtDB8NVuqaASB1U5qiJf5foC3vXdfhAW3PUuhkpr_fg3H1JTdyhx2WV2w6U17esGzJO--m2bxPUHECA9QkyLTt-l12mMV_HXEsDbH4PaTclpRQrDzAgGWSWRHHRCjdBGzTfA30vLNFvAKwzc0rc9tzKLt2RKQ3E_IypkNrDx2W1s2jzOjW25aOzbeJ1BP-xlaECsNvwr4SCsIt1WV9qyC_amVWNLvMrTNLwJo4Wc6IeqpUa5fts-kn6InGFI8eULcTRY8xH1PpxD9_YiDz-0DlRyBCo9oFyJHfQWabrQ8xHdBwIYZnHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDCP-Ewf5oZ6u6E8jxwezkuiPZ7WIYP8k8JLdG_2vLWGsguW1_7IFsN6-farFY3SwCVSej8P1-Q9Q0-0YBH5HaNrdyDpv103bx3lVoYw20LykxZyPtmdl85CmAgUZKlfParLwBXpmQ7GuLoRRCOgex0yCTDtlbyKHWClhuoYJTmN_vqWC0USEC46HdEaEsp4YSaBzldVkRpmYYtlTTfIvgmIgD8RqsGa7cfJSm9ZpQuQejbD0zGhx0AyXD-FjQIMr3bzdM7ol6FlquV_f6zGA6Blr8EDyzlkDZnhb9BZE2brim9kCnpRlocy950bY6ESwslcyKDgPPT8evZeHcuJKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdgrp6ZP72t4L6EFawekbEFmbBflRZ76pGCbIECNusmsEFr_S5Eo8C1QDGjTlx1urxB9--U34XM4fgi3dfkFxyoV9j1ChG9SUTdQDgZd5zveKeHdjZbb8bJdSKFGF5SIoqTE94vnXnb2hu6PjNEFNz4UTjFzPZQBPlMuraKb-moicbMu_DBDHwxBc2fwRbU9xyCHPcblcCZukd2dL-Uwlur_ORShxEZUX7VhtcacM8tfsNuXgHxa39szYDVOxvVYLZe7yC1r4EUj0ZVskS2eXJXY9h8v1wJ-kkRUzyt_f5wNCqW8WCco188SmOVCyPAFVumCwpdgZE5z3AyL82KcCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9XRxQFuCPV8fEivXqJ-0o_NR9Btbrq6goflJJg0R9bfpLI5ChNs0kGegU9TN-wPHcKn7ViaxD8FhT0Oae8PLKwes1Esbsg6bxGOcDuaL2a7mvTkqpqhBDSG_CNwyIXg-ikyPYQsYlyx_G0DzkqZnkUBciNwJF3Nz9TWvGeZydOGTxZAVrMgua6BpwGFp6NS84FpquKvW4CrRJRT3HbqKE3TAH6wGL_34uaNcqjQH_pSVXX6ibZsAOHi8scZnOxMOOV8yPWojYL8HxF13ANZW7FoLoaE8p_rq6sGG6GR42_bSWS3ZZWPSLxnONI2cG_DzcpNoA9LEHn61l7-XirbJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKFKJkiv-Sj91WZx-iFhemwI-YAzmQnkyE_FCen8Y3x0AfvMK1TdToSN-U8p5Z6Wddlb5EVkCtySGfU3Fzp0IDTNMKOqyFJD5myoidp5vECyuHaIflpz7fb4IXEqDInHICV1nO9FmEwb2rW1gDks8Yayh7v3eJMmTDCBQ2kpzkpY2zK_n4zmB9_DKEtYDckMag8MEkolndx5kbw-Hk8VUDGBOSQdf5otZrUqIDDWZbkMoSKp29x1yzcTiIUEtKuD34DoXS9Hfd7SBOMq2j2CyTaPIkEYG7C5DIacTEiNk_LWKRW4MtBPsBS06Hvj8u2rjMx6ArDcNGdch0hFUcG5GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTL3KDX3tYLTn8g5ZIlSxrp7o094Mdd9EFSr3aEYx3cPdcmcAa8P4CxQuq-UAzfHHaIOrdD9YCq-PvYn66QM4T6_SKjt42MfAcgXHmhFGMLuwmurpn_xLhVHkRCdV0C0ETwnkktTVN0RRSJDxPmW1F3GH-WvzS-VcPAgWFBf2sKyFZ9wrAG1xYnZbL0MWsfZXNii_lHrOPsuZSgy5elCC2SklPort2bexhXXbHurqTeoip5aiuu2VMsjF_LbRV-iWFESwT20jafFKoaNCklES2HWSGTzOrScfgrXaiSUZbGouFIvyFyI6B_kL0KOqXQHQgad0GA8IamSpO81cPzMYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bglbBiZU9UJ15YWoV-yMu5flvyBzDEeSHulgbH2l-MayjFpptoDMC0AVgK3CGgKnlHe5KAJWKTiAyvkwjQ0RfphMmyigHA_7tvnto73UBRZLm3ypcqp3cUjS8WTp6MroSwDdfsE0bXGdb_kfnFDWaXSeAChixZ57KD8Jg9JdF7ZGoMZloCAwi7LSkJzfuXzeJnk4hwTqO4pbNY1czJ5kKhKhaCaSA5pi4_Wmco_OC-dDp_vSoRrHy5hrEQAz1OusXo-PPwznrMlvUeN5p8qGio0kxX_qRcfO6PkQ17_1PBokKfUCcKoh0RgimwqEGvy7JCEEukng723aUQRjukP9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_WVLloSa05TUGIAZEADA88E_FnGdlRqDfE5Ga3O_6xtpcLtMzdHDsYbkZDtSRwX_s3jZZZ2aaqRBS6niYUMEnSVxleCG4l0e8L9oSWTMbU8hdAWbYz2_BnrOv1O11ACsOD_JyjiX5H1tZNV9qw7CftfJWiI5X3tmS9d5xMELdrvqijyZJcvk2mFUY1u2Fr76DuJ1ENIL7vrKyLbstEhrVhGLO_JXd0vr9JDWznc8NHcSmX-Xs7CqDvI1k9eSOqQXbJ5j8IXA1Lf5kVllBGSXRRqJU7qe8DWT401aDyA3ycGL4gL_Of-_bOQyKO7pXN3eO2eieTempre7CSS3xrprQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvpMMRKgs-8emku7DAb1LmsHquOTX-sFAA76wqgRRP2CCyWDflNg6PNU94ug5bdpBrdJtQufI6J7zUXzY-8-kcg2v3eWIjWx4ThpfDmRYJsw8aJxT0wW2Le5n2wq2U5l5ukTPmjhydimRpMyGRg7FDUB0_0y1ZuiKoRx2QfeGU5bYAu0xw9Dt71rdD8zNjWGn7LIdb8HO4XoFvMYXRxrNDmSZQ4-6qZ-2DJQoLWdQ7ZRzs89SJYHUCyq-SF3U9YVBcWoFdR4uhRoHagZh2lUW9ty9tqBALihKh_lKGcYnKBAGLWjYqFascKiHvL6Ms8K2wEFm0Ga3ObRXcjzP4FFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J8l4rgBW-512RR1LpivKAu0tn4s3TdDAcKnym0J_mTfp9mRpSFKhEAa1AwFPCeJZagXa87YAONcMIw_E5TOAxEsV7Oln_uCO3PAHzs9908Qd42EcRxQUD8_qNFcJ4SRpb1LMZbhZ6hd_yIOGj9BRx1qqs62OGfbuYNRsEbOt_deM5O6jml1Xf7xpI0jyavLOqW66lYa5hxgNMAzIi-ljfBJnKheVYsofZrE5-CE0tOd1fqtnzfwdJUDFBOul-8boxP1lSxeTpihShZBKByN__F0HVha_9dx3kIFzuOYztAIf_tRXl0L3vNPbGHdt8_XCE0Qb0-pvhwmSDSuINZ6UvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eD3dOt347thRmyz60PKtnp7gHhf2HcfOxnHlMotvttTCX_379bcB3nYc2rg-EwnZvHFiqk93h1jDgAkcCm5K9U_TMllY2ntsmkuhDFdeAN0EfxnNm7dZ2JdQUmg78zwYMcQ0cc9IAiq2QXMfSMOJw_MzWo5FLQ5K28Qo3Ei8wpDG9DzhjHTiZfFuilrpq8ryjF4vJlKAbOEGhW_hle51FkoqhFFPj9wt6NyfappEoOIo9xHjTIg66NaMA3aakR1EqrysyiyywTd1OcrwPaHX38s5-WHqg4MPKHwe0RlKDU6TdnzxeQwQTD5nzP3C4h6gRH7Qg9EpH_5-4XmXj3F0zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=suUYmaVdxfSuJAQexhBqmik6rESudS3pTz4VXLjMMP9pxVAOod8wYwpmyVOqoxGQOXCM-JUWS4VCrRQLuaGOEzt9db5HKUTqb4X60jGpZkgy68LQ7w_IFqIM2_UkKbe1sMNsbR_wih3K6n2R9YwFcWwHgEEYm52e0HkDz-fuP5mzq6ITZjkiFGCY4sJqqjkM3fkkwNKpNdd-8qVgtA34kdF9kJtyKpcNMedcmutYGUPAYZHk26yf7KZPYHkw-NVvLgL2ItJyss2xoWKUWpq_9UeBru8u1YMwftlyXqb2mzh8UrbA6i1y21A3sJI3elyhpxveEbHxhUN_C_8Rv5W94w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=suUYmaVdxfSuJAQexhBqmik6rESudS3pTz4VXLjMMP9pxVAOod8wYwpmyVOqoxGQOXCM-JUWS4VCrRQLuaGOEzt9db5HKUTqb4X60jGpZkgy68LQ7w_IFqIM2_UkKbe1sMNsbR_wih3K6n2R9YwFcWwHgEEYm52e0HkDz-fuP5mzq6ITZjkiFGCY4sJqqjkM3fkkwNKpNdd-8qVgtA34kdF9kJtyKpcNMedcmutYGUPAYZHk26yf7KZPYHkw-NVvLgL2ItJyss2xoWKUWpq_9UeBru8u1YMwftlyXqb2mzh8UrbA6i1y21A3sJI3elyhpxveEbHxhUN_C_8Rv5W94w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfR_iAcAtmBwajnMmDFmaunkoNpjWjowNKK3Xa48g81-9IwhW4qajq0bb9dw63TBQfuLFi1-MflFYSXJOd3TjhRJaW6Eo0nMRXlZqnjdwKwwt4sdFB-4_r8gtTDeQA4bE7pK-T6DRVU6zddKjuIsXD3mil7rA95NNCTdjPqGsI9ile5AurHwoEE14nQQ3mPnBGw6QGGDpaks-rBBtYeQ5T7UFlysMbZLzVBdFpHEWMds4v37VvPSPK9lEeh_xvfMXsoyPyKiJEdqUXwNG-YOcftblufwMFvKqH_JiB7-Iro1OPyGuXaiKHXeqvtdVh-lkM0LaR8MgpNitJO9WM0Flw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFaZdRieAWs0XVVGlMTvBKO3W0ccjhs0U3AK8qqxCWErQ_mHOqcxvvfQ1WNPss2gWH0LxjgPlmhcs4HOU2dVoU8hmd1PKgeHzpzhKHT07Fhz5Y0dkRYFdlLe1TAsiLXhwoSS8jk9KQYyHLcjoqss5BMMXpen30K_9rq_IfwBevJ44orRwAgngJ6GIZdLUf5fd48vVLO96cFgOrsd2PL5x9J74aUsd5yACG57NO9TmrJU0HDRbLkUIlqMSrZfTwugszLKd4c0VD50x80bmcyhlWv5Iizj8Ifih1_8GOa6ALhU8vpU6aMXOVRMV5GJccFZEcR8mDdVq2ZM9bIMAEtLYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Do-vCyYZVjp4JgY1WfAf3Ha0uZ0Q2ktR9q9oCEi5xFM4h-HEMUwbonSz1ZGHeWGK5nB9_-t1WJv-ZK_C4rpuaSsj7eDzaQVCL2gLUO2Bv9UJXEg2ykMTvBhL4KQljYwqz9Upd6uJrXsJx8qAiIXCJ7-WkfCV_fB-t5BL-ouPvAuFQW5GCj2jwMmHcdQkIQHdPJNZF7OkJXgazmZ270xqaehxov0or9r1HCXVG28mbom05HkZC8soBq_IBrT6NtXMD6CLoUA60RNLD91Dzna8E4jIGLgdAHnmZwnBluu1q5pfOtZsL7m1m47hdpMXo1LX3z87DBgeulvYmSWV09Xx_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Do-vCyYZVjp4JgY1WfAf3Ha0uZ0Q2ktR9q9oCEi5xFM4h-HEMUwbonSz1ZGHeWGK5nB9_-t1WJv-ZK_C4rpuaSsj7eDzaQVCL2gLUO2Bv9UJXEg2ykMTvBhL4KQljYwqz9Upd6uJrXsJx8qAiIXCJ7-WkfCV_fB-t5BL-ouPvAuFQW5GCj2jwMmHcdQkIQHdPJNZF7OkJXgazmZ270xqaehxov0or9r1HCXVG28mbom05HkZC8soBq_IBrT6NtXMD6CLoUA60RNLD91Dzna8E4jIGLgdAHnmZwnBluu1q5pfOtZsL7m1m47hdpMXo1LX3z87DBgeulvYmSWV09Xx_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=pfkAuaJwwCdqRgMgfnt3clFUY8tFkbY0_VJgDxOYW6dTCzVO1GPUYSUnrx92U75sjzn3U5OkjbJNr_2TkHwjjwwJWPcWqYEarakb7goIdAp4PhObmsnYt0QJ0sgrviYV3gSSpL9wKyceDINVbrC_FPWgBkOnrgVTFUGo_kKgQ1C5s4EEGA28OzrStGyXw4Uy_qDkLtHGK5Y7pdWlAQzegZiAVsh0ZvgO3HBoe_dXWoOpOavLyp93i8pNWsrfAxART7PzH0kOuAuZSLy34rmXdHQ5EvKdg2gHOTFxwx6DuH9CorQcFZzw9wXMZOjWAIb4iTlNNT45nF05TD8Ro2yCxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=pfkAuaJwwCdqRgMgfnt3clFUY8tFkbY0_VJgDxOYW6dTCzVO1GPUYSUnrx92U75sjzn3U5OkjbJNr_2TkHwjjwwJWPcWqYEarakb7goIdAp4PhObmsnYt0QJ0sgrviYV3gSSpL9wKyceDINVbrC_FPWgBkOnrgVTFUGo_kKgQ1C5s4EEGA28OzrStGyXw4Uy_qDkLtHGK5Y7pdWlAQzegZiAVsh0ZvgO3HBoe_dXWoOpOavLyp93i8pNWsrfAxART7PzH0kOuAuZSLy34rmXdHQ5EvKdg2gHOTFxwx6DuH9CorQcFZzw9wXMZOjWAIb4iTlNNT45nF05TD8Ro2yCxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPa8nttwOVC1-JXWmJSk8nrKnLhy8CILwtXjeRi_NI_SelQu752IZ1jF8PJavFvZmCZzOyu3UbvUfs1IIHv-pyEISbNazfGJJF_ZHVfDcrHlPo2aVB6MFBrMkxIo2AZdbx7ITE-FEnGDO_tXvxQbQOblof5eOldwE6cLgfJVlNJXbCe7BN6As8iHLIpC9XpQK4Ttz3Yz5TZWtddc3UB6nZvr14--n7kKFnjl9S98VDfGMsMoLGLk-QplpksIQn6sYBTu9PM-onh1h2s0JTstmWXDscY6bnyh4Y0YRgjhlLHyFlOYvc1jzqC7DBv8CWBKCQgu0XXxhx49P57W8OGIeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4nl3umG2y5ZOaUFwraUPycpq4y4JT0wh3t2ulSalNiIzssfSrveaVlNbVrSMCrR1qWv-lB89aNIgZOoLka8MiyCB1EyfdO_e-CLiRbQSW5M3ZzrBPhc6NKvF3VZZMwZtoP_rIWjy9Fh_fNGvMJTff0xu5fdZGJEZCYHw5gjsrDEyL-mUafQEZ7I77URe9PnGYfUqEepNdifVMLBmrSsNSTX-OC_pL1y2wS2pZtRFieUTbbJQs76FVausSFFFPVW4pt1Iw5oTER6tC7xm6CI3TjYXsKJ4ZRmZwR7N9DakPoBryHYgyQaxRp2VR1nw2aBNE3pXn-N1PUF9NX3kZ3qLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtNsP8mc4MIbqooBBIg7rLQpZ60X82TWYPjMiuXRTeYp_IX-WFct1IINUt2dX-ueO0EqWhSZEqlB2gcPs-EuDFxUzptiw1YbvUeBEqBuPolvOo3wotKVIHBuSIrrfo6sodoRDJWi66ri_1kT_wXXP2ddnS0dvIPoJKXA72hDILsE8RGrKUE7yZzusq_Zdfxs34WQ4kZKN5j2DEaxGmTGt9ta0yAyuzgNIQbqVzLHr5aXkao1ywKP4F_NXYqchy_-e0Tw9R-fmqVIP97bdUONzTIQNk8Pmkq2OfTeXDTrLDmO-oCQUTGdwz6E66xwUoms62vsIMg3e-Xi2BLVFLhxTg.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
