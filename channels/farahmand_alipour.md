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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 00:41:31</div>
<hr>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOPBe-WsSyKP9b8iFJXu_j5PR_0lIEe2k50pJqHmxjEnlwZ0j94YJGCBG2XZ_m1-E5lIzS-uCEoSAwIqZByjdAtrURxa4361C-j0MHwVOYXc5RHqG5rGl7Nqk58cUP7HiiAmnhLXXhu7jS1wv0McnVMu37vavKH4-rLNI7Y8D81vO04kCcgI_JAejI2Mi2CdGfcTRRRsID6hnDCdvP19ub6N56KEtCwDrDAoeceEfqjYB_EF3YKLkB-FZW5OlDzcmSRzlOveJDK5k_fi52cSTkfDG5YrnnSg0LgXDVg9XtIxKe6YOuSHD_9JrBKpkIrDglDkCtl6QczjuIODYlnyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZEQJuVbcnqNZZHO7UjFbF5c5Wp-hZh70i1mON0nwPJXiyT9kPyasiGoUW0T9g6LNIIN6IHGZfBK19KjIs9n-UBY9DyHOfS7SahknXoobdxk9rAgcUea0wnNeB_--HjjeqccWRSaiKopHyS19n3_qXwB6Kf2CFiqqXo77mT9Fzeh_NUY3p-SFM-2bPYbnSZAERGxRt9l2cu2KPHotFhcEQlnjRwB_SmQGrDMLs4k2IhBJVIIxHbHhEy8dywxrSY9cN8bRk7qIOYN8GwyfWa-HAItdZNbRxnfVacjPfv5K1SK6kgh-GqspnwCMbtCo38bFPtZZCBgwmF2Sy4MsqnXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFGxaknU9gwmCHvWMuzyhciGwoBq3Wvjsi3vsfKtm2K1CmZB17mq1Oj1d8hkI4A-SXDdha--naq-8ctjhw05SJrokXf-QrRUo1-SGSg-oNlcOjLaizuMW_ukRYCU0icWyphiJ8uBmiz4OCkeCp3NI-igJlasLW1Rq8cjbqPSDyev85dYTagLTKZnty8j3U2XHpG-LVLyy_mEdTm94V6RmJpF_0B6iFbqw9i3fkthQ2Ntim_Kbm-_ZFp-rdbqiOp06xSBNNeDqb6JqPloEj4v0852Qxf17plAEj6GOf1U3H6mXfwYcObJrJF-QKuj66SXxyZoSAHItyMnkNRq-OGxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0aywzT_-GzwuS-25mi_0go9TbrYsABFIDLG5_fKZJKw3ldMd2vtzyuR6a1cYEs4HyFKCmu5xkgmWHGm-hBJDPvRVBrri5iB5aO9t4LE5QxgtoP-3ykIltfWQGeDiazeZovAYir7RXhaSogRkAqtMnSBFS-e8paGxP-d2lN-lV-yQrhxXacNBelER5tGXdSIkLdUZKq_Sp_pSQYBzQHcHnto6y8s-ITaXKwQjO2AKvE3cGLYwtx96h-7z4piCDYzOQZ2qQlDuT4N4byUDUvZQTVXLgUGPu2tYKthtaZU8gaXoCbF6Eg4l5GArzaG-2nFYMC_CGRIEvAS7H1Y9RiqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdS1pykzShzR8CEFx8oTl2v9K90uDjr79lde4OI135cV2n5XqcXgZzfrTxGNQmLKEr4H7iCydu317EoA9gt6pnQuZvbBjpFLkAZLA_DxWz_NJU96N-YNJmf5eSvAyW41kkG6QvQw0qr_cD8oQoIfbHtISGQVioqtXXGTeVmhi8UtFrqRqdlH4y2ttyHiuppjv2Q4puTedYS-CEn-YM_dNy6jaaqzceJJp756khn9xy0aAbNyC0SbKdY0dyRj883jjGuOvcRykzxSBVfQQ0K9tmmMCNwNCyD2ckPRdLJuO9kWQYvEUBxDgGUktti75SCfPs33KYJD7LIHakqo_ozJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wda1RPKY6KjADHUeSAR7DU26uW17uhcJiQTEoCUY_o-hJt-vZwuLLGBDVVnlB6wbNom6KrdSPiOUiQ7SxKBcXXsjqxj6JMQOBGFKvuwMtZ5lhf-qRN4_ZQbyXvaOf3MM30d31d5vSNHsSDYgJy16HsdOtbj5W0onrotCdfIu5VqEUxYmndUd58PwVGxFk3cgHRw2yKhfGDX017U_K8aug6cA_pMZSaNzCzdnfMDAQ0UoTYq7dLZV7TeGrpWhsb3uS8pQAw53FrHnWe2-bFuCql5mt268wfQpiBknZniwaj8WYvo35vaCoYPO0raAh2bMSojQcTV0y5bJ6XjWC0ixVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hd14kMptknagpILxkoWY6tYDcFWcga6gqnf-682vVvl-MWUcLIk9X5MgZlYcqtkUh8HXy_YcbWsDDwY2YU9fqV4PRkrsUYeUZOMRAaqMiMa8i78OnIo_tw7YruLk0w-FXp76WN2dHzu--UuIbcSZRRbzEbRMxt0yIvcEFzBKdNkqanAi1B-Eqsu-CZvtv2z8Gfr2pcEgGD4zWm1WWA08zUGWJzV2Ex5GmW2dS3CTOj3_J1k0XzE6AMMzxVLINg9AmUyh6XPcrRUj7_9bJxPUSYRat2W7biluiLS1Smjnpp0yiM-ZW_1xfiOuMRoDLCIXJLTmBeuTQsJGmz5-LIKR-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFBeg7DclAMEGf-lPESyU4UdQp0bSQvpJlpxBpIYqui7oux8LPdVUHXCreiNCAnfqRAbGcqxCY9UKTSP1kiyxaiDOcA5DLualSopFy4wgbCnx1gTPfL34fhpxEQaEVYhXAKGKD2vsd3Kv_8gIpqZHMnhoQ0F7_u_HeVt_S4ECkF_07NPsjoGtD4tv6_v2BE9bf-bg9NbNpDTFoGhVyqmcI9f9V71HT8WpE9xtl-LarYpg1Pzw2StEShW70YxdROe1j0cMDgC01cN9foq7xiJC-thLfGrLyCkn6peTGo2AY9foGUVwABeu7nhKWIMIywaSgGyufRyjOLwt1bnynxn61mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFBeg7DclAMEGf-lPESyU4UdQp0bSQvpJlpxBpIYqui7oux8LPdVUHXCreiNCAnfqRAbGcqxCY9UKTSP1kiyxaiDOcA5DLualSopFy4wgbCnx1gTPfL34fhpxEQaEVYhXAKGKD2vsd3Kv_8gIpqZHMnhoQ0F7_u_HeVt_S4ECkF_07NPsjoGtD4tv6_v2BE9bf-bg9NbNpDTFoGhVyqmcI9f9V71HT8WpE9xtl-LarYpg1Pzw2StEShW70YxdROe1j0cMDgC01cN9foq7xiJC-thLfGrLyCkn6peTGo2AY9foGUVwABeu7nhKWIMIywaSgGyufRyjOLwt1bnynxn61mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=tD127vC9I4W2y1VbptT2Kv6pt7Ra4hGt9OyyXq6Lla7V0FQZETR1IuLdSspKUW6WuKkTVoA8g8b8I7cv0uGf8e139L_iWbPIrkj_PpyhHGTIb9XQzpRdmJb_Gg7xEXJhfPUCDFsUCRjB_SUAGFY6fX4_vCd6ZLQr_jggxjz4UayqxhsEDoZ03908LgYKaC6wUPSZD7f5Bzlgz-w2J8awZxBiClVQHpRHlIbu7t-iaumzpN3gOduRDWaa-plSMrYpwmW-4Oio72vP8sz7PPDVYXbk2K0xec2_oPwq0i44HT995RehcANOzPeisymrnlqq7fUwucuqbT_013wLN3L2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=tD127vC9I4W2y1VbptT2Kv6pt7Ra4hGt9OyyXq6Lla7V0FQZETR1IuLdSspKUW6WuKkTVoA8g8b8I7cv0uGf8e139L_iWbPIrkj_PpyhHGTIb9XQzpRdmJb_Gg7xEXJhfPUCDFsUCRjB_SUAGFY6fX4_vCd6ZLQr_jggxjz4UayqxhsEDoZ03908LgYKaC6wUPSZD7f5Bzlgz-w2J8awZxBiClVQHpRHlIbu7t-iaumzpN3gOduRDWaa-plSMrYpwmW-4Oio72vP8sz7PPDVYXbk2K0xec2_oPwq0i44HT995RehcANOzPeisymrnlqq7fUwucuqbT_013wLN3L2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=B-ylRYtJ5IuH7kAZI74pfOCeisr4bMsLIZfIwayptvFXIziM7ju7t7hBS4SgtP5IKVJTq-DvlVCC0WtLQFAlpTPb5uLdVvnBXDgSPc9gz2PBQpGUr7xuXeb21-eRBzSFS4at9p2AybLTHYaKxBf2aI89Xj34W-e42Pq2GZqPpiaY67qLam8ThpvZCZraQ9Qo_b7qiUGstHnY8P0IBR1UNkqI4UG-Sc7Mw1GpXIrZxK19I7Ywu7VnCzlj99COOQUoQGpo07pCJ0SKY9MtpQGh-Ft5Y7ErFASpee4Kb6lF08NkxzW9GxUlUUs_e4C0TNUas0r2EJLBZgU3KiRbAA-WTWFVVCAS3GJRlsySIKoU21d4_lpACNFwChdV6y8ecAqbyTT-0IaaOjYr4Gq7RwfX0l57c8hH5i2yqeDmdFqqeRIMX28ubLnPHA-eqaT8CXAg6gSJPd8EWSLGLBbHl2e3tOymox0x4xhgPZNfBsodKhcFwBw1sufzjvH_TlFqhw6iVUivLm44qYNOkinieewYOsC90YKn66eQxERKgX_kl8-CI2LqDXDr7PdtBymGtLaoLzdPYwahOQZo8K8j2vISS6Pi4TFb0HA-3_-GGsY-gORAJmPOdKFuc4zGQG6fYNnArncGyn_mvigORgfM8j1kImiqRR33O5yyL43a0dcWXvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=B-ylRYtJ5IuH7kAZI74pfOCeisr4bMsLIZfIwayptvFXIziM7ju7t7hBS4SgtP5IKVJTq-DvlVCC0WtLQFAlpTPb5uLdVvnBXDgSPc9gz2PBQpGUr7xuXeb21-eRBzSFS4at9p2AybLTHYaKxBf2aI89Xj34W-e42Pq2GZqPpiaY67qLam8ThpvZCZraQ9Qo_b7qiUGstHnY8P0IBR1UNkqI4UG-Sc7Mw1GpXIrZxK19I7Ywu7VnCzlj99COOQUoQGpo07pCJ0SKY9MtpQGh-Ft5Y7ErFASpee4Kb6lF08NkxzW9GxUlUUs_e4C0TNUas0r2EJLBZgU3KiRbAA-WTWFVVCAS3GJRlsySIKoU21d4_lpACNFwChdV6y8ecAqbyTT-0IaaOjYr4Gq7RwfX0l57c8hH5i2yqeDmdFqqeRIMX28ubLnPHA-eqaT8CXAg6gSJPd8EWSLGLBbHl2e3tOymox0x4xhgPZNfBsodKhcFwBw1sufzjvH_TlFqhw6iVUivLm44qYNOkinieewYOsC90YKn66eQxERKgX_kl8-CI2LqDXDr7PdtBymGtLaoLzdPYwahOQZo8K8j2vISS6Pi4TFb0HA-3_-GGsY-gORAJmPOdKFuc4zGQG6fYNnArncGyn_mvigORgfM8j1kImiqRR33O5yyL43a0dcWXvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=GRNKZ9J_oTPS3EuztOKCp4sp2Zb2YUIgfhPMv8uTR99jcIBzuhmQMN2wjZV1h5cAMsjlzzTbVHfurOgXksnMoXwNEJCmYlEWOQTEPxL8H4R6bREoJqeusZmgTNnRgWia4i7CkKF5I5yZXzs8jorHEQ0YikTSQxMwLUzrDohwx9FHJNHqaOOqJpINFEux7YnwepULuYHRD8DzVRUHayHUYBODHnIZOpx-dwi1GWvFzL8282NHxDO9rFZYHhmOKo7NoZGhQzQB4PjIteTCfok34Ra-efpXppaXHEifIGGUvxmYYMiFwYd6zTf7ffwQQ6tAIe_b0D0TZV31s_g2zA0k6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=GRNKZ9J_oTPS3EuztOKCp4sp2Zb2YUIgfhPMv8uTR99jcIBzuhmQMN2wjZV1h5cAMsjlzzTbVHfurOgXksnMoXwNEJCmYlEWOQTEPxL8H4R6bREoJqeusZmgTNnRgWia4i7CkKF5I5yZXzs8jorHEQ0YikTSQxMwLUzrDohwx9FHJNHqaOOqJpINFEux7YnwepULuYHRD8DzVRUHayHUYBODHnIZOpx-dwi1GWvFzL8282NHxDO9rFZYHhmOKo7NoZGhQzQB4PjIteTCfok34Ra-efpXppaXHEifIGGUvxmYYMiFwYd6zTf7ffwQQ6tAIe_b0D0TZV31s_g2zA0k6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3xu2qA59FnQbR-2fx7LWBvuJJPNeTbTB9L8Gt24hFcLF_MCPSPaoTsxyH-x_2PVTWnO11cnBLCaDXyNJ_-igrI2Ditg7p1OmWdeskriEFQryf7dj_-Lu0u0nl-XFmARRB0CRuoa3xxlq0cN5lIKHcJuWWna4Kescq46Wcxx17nXhtVeuQyGxtEJ8tbE-enWYfStlT2e3Szsng4QzFepCaGC_pR5sYxg7_NX63qv9mEAy-aNpjiQipNgoxNcDVAs57VjTZ7ohUTMbTLQ0XOj3jSTSjvnFNPYls8Dm3f_aouC4ElZZAE2Kigeln22d1t97yq84sVq0O-YynarUCV5TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=DIbzXSxxvqCt15tWth3bqNCnrwW7eTkJ0toGg7obflMM0k_8rO-WC5fBLsmEphYbc_XLgpcA6JUv2dhqkPz48YwCcvp9hyw_XxUGaNYWTY5u7r2Q5zXflQyYMQTZV89rihiSdPNd5RgmmCGaHGi7BDUWur32FWtEwsc-Z902LJRmdtACnsapwC_CtycIKno9WIlY7HAWOzk_Uy6pNGx8jQWOqpeo_TPP8pqx__yMfxjQCA8Gm83BEoxwkb7aNtAMMoXcvWZ652x7SRKMM2EYppZX-2xe2y-3-Rlh3TbxryPwMJUczKevyRezBDBFw3OmFO59MLM2Pm9b-QhV0kte3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=DIbzXSxxvqCt15tWth3bqNCnrwW7eTkJ0toGg7obflMM0k_8rO-WC5fBLsmEphYbc_XLgpcA6JUv2dhqkPz48YwCcvp9hyw_XxUGaNYWTY5u7r2Q5zXflQyYMQTZV89rihiSdPNd5RgmmCGaHGi7BDUWur32FWtEwsc-Z902LJRmdtACnsapwC_CtycIKno9WIlY7HAWOzk_Uy6pNGx8jQWOqpeo_TPP8pqx__yMfxjQCA8Gm83BEoxwkb7aNtAMMoXcvWZ652x7SRKMM2EYppZX-2xe2y-3-Rlh3TbxryPwMJUczKevyRezBDBFw3OmFO59MLM2Pm9b-QhV0kte3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=k23lwMiYy97gmGvHqfUzc6fdj64iEPJeGBX1EXtDKCV0qW-mr2auTRJuwNh0yY0W4n3GO7qgFlVpUZhGQu7Ss7_m3Z_dUPx4LeH2jZ9NSFTquV-PawXFvqAHTiskYfSnvtvSgBENcVr6OxN5Z2A-AfEnWC3znONA_xVH_I3wzP44eGXPurKoUlqhMe-d5E_six_KkWM68uu_eVYDNlNYCbq15wIA-WlbCXkC-KbBR_RFDWLQ1NT5bUosnJHmPKL4p4nRwu4kYaRFzDmxN4HATb8BPN8YYLGMvySBOc34LXtQDoF_G4h0n2rjLMnvF6rtkof8wCVnGvSg0EsQvrqhYzJ48_8VFPp6Gw0VHP3Pwbc_fcdV6_VX8JD99dxmixI7MPrO6hD1H7oHSw1CxDonOtx5teQOYZLoYjO7lQeR9kuAeR-ISumdjgEE-SAbpw6XJ4yq9_svGbiRdguhYSlLutPYoGxaUC3d5MRMBHXVTrNn7nXe-UwYkdHwWk9aTFDmvUGwblrmiX1GPdrL5rBajw3w9U4GGdH9MhSIboRQX3oIxe9uqnOxvfIfewV74pOfrdC3bPvsD093hhX1CXv5nHK6hLmX84W5O57Ta-kyIQHEmJs_dbdZnacNb0LY4simq-kcH3D1ZGh6piuZma-wKh9TtBtxqMelAzFhYwkUkN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=k23lwMiYy97gmGvHqfUzc6fdj64iEPJeGBX1EXtDKCV0qW-mr2auTRJuwNh0yY0W4n3GO7qgFlVpUZhGQu7Ss7_m3Z_dUPx4LeH2jZ9NSFTquV-PawXFvqAHTiskYfSnvtvSgBENcVr6OxN5Z2A-AfEnWC3znONA_xVH_I3wzP44eGXPurKoUlqhMe-d5E_six_KkWM68uu_eVYDNlNYCbq15wIA-WlbCXkC-KbBR_RFDWLQ1NT5bUosnJHmPKL4p4nRwu4kYaRFzDmxN4HATb8BPN8YYLGMvySBOc34LXtQDoF_G4h0n2rjLMnvF6rtkof8wCVnGvSg0EsQvrqhYzJ48_8VFPp6Gw0VHP3Pwbc_fcdV6_VX8JD99dxmixI7MPrO6hD1H7oHSw1CxDonOtx5teQOYZLoYjO7lQeR9kuAeR-ISumdjgEE-SAbpw6XJ4yq9_svGbiRdguhYSlLutPYoGxaUC3d5MRMBHXVTrNn7nXe-UwYkdHwWk9aTFDmvUGwblrmiX1GPdrL5rBajw3w9U4GGdH9MhSIboRQX3oIxe9uqnOxvfIfewV74pOfrdC3bPvsD093hhX1CXv5nHK6hLmX84W5O57Ta-kyIQHEmJs_dbdZnacNb0LY4simq-kcH3D1ZGh6piuZma-wKh9TtBtxqMelAzFhYwkUkN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cg3Nw2p_PCYaEQ17UmGHpIQM1mc5rYhTjL4JerGAoqSKRK0qNZaSchVlLKrWv1M8AekG6EEcVW6x4wkXR_URRKxEbno87n7DbDmBvdeZLj0NTlVQ38SdZGu68GWFtE3h5IDr5R-3srpap312kIGsXPYlNCtQc4a7fiESohrMZVdcdGICPVMQgVzdTpCtifR3Qrghv-YPZgjMGMG6V3xwFRAnSPBYaCP84BFGIV4-0BLGCBNh9Ke3xwxWZ7bSPIZyrIaVptdTX54Ossb9vVNVX_qXXeAshmIAmLy892o_cFG22SURcWJKdPGZPl7Gd73nxB7m4i8FTbv70em30C1H2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=SzQ-hfeqmkQzgGyGMpH12nPhaBg33W1w5cE8IoxJPIbh6HzxdLUi6gEdcYwbt-kFoHN7xfqLh77hP-H9a-SUc8crocCdZw6Sbt4wPdc-GWO3VI8cx2mni6Buk4h_enyiXEjsBhIQacNr1Ng79RYK2Sm_QKIGtdas0w7IcEwIhqRBNxTjO9PuAOLmj-sRSIv-M-CkjCXWZUqojCzAJvIfVf1MjZiYQ6zhKzBUcgjh-RGxHfWjcwEjNwFvDCk_4iska0LVBMVIk0BoT_3uQbLGov8f83dV5OkeVmemt3zAyrStEekjPbGDjTTdni1fUFH1O-JZM03Lb6vS9a8XaWFODphl-skBGRiVqkdosZVJpS40mtCkwc2eajnYldlhSsHKi5yxVHkrnvAlO9Mg-0QD9sLhUhuxzVBQZtIisRLSqyk6svM5IdzpvvuBlQ3Qongl17bDLxuiqx3_vCpQyHgSesPCWEg6rIUyTnRG1UqjFithqdYqT1K3zJZJSaRG-bVkkZwAdebcHguHypZH8xBg0NPRw6HWBYVJHZHEbb5Wqm4UOozodYlZnsPVaPlnxfBWo7LKHDBMEbcxY3gyVSgT5qToARHBYReFvzNgBs0xEj_t6u67eTf_pW4H4usNPhAwn5LXf7PRFwlAedq7EtBVp0Bf04ZL0_EII73uZjQVkCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=SzQ-hfeqmkQzgGyGMpH12nPhaBg33W1w5cE8IoxJPIbh6HzxdLUi6gEdcYwbt-kFoHN7xfqLh77hP-H9a-SUc8crocCdZw6Sbt4wPdc-GWO3VI8cx2mni6Buk4h_enyiXEjsBhIQacNr1Ng79RYK2Sm_QKIGtdas0w7IcEwIhqRBNxTjO9PuAOLmj-sRSIv-M-CkjCXWZUqojCzAJvIfVf1MjZiYQ6zhKzBUcgjh-RGxHfWjcwEjNwFvDCk_4iska0LVBMVIk0BoT_3uQbLGov8f83dV5OkeVmemt3zAyrStEekjPbGDjTTdni1fUFH1O-JZM03Lb6vS9a8XaWFODphl-skBGRiVqkdosZVJpS40mtCkwc2eajnYldlhSsHKi5yxVHkrnvAlO9Mg-0QD9sLhUhuxzVBQZtIisRLSqyk6svM5IdzpvvuBlQ3Qongl17bDLxuiqx3_vCpQyHgSesPCWEg6rIUyTnRG1UqjFithqdYqT1K3zJZJSaRG-bVkkZwAdebcHguHypZH8xBg0NPRw6HWBYVJHZHEbb5Wqm4UOozodYlZnsPVaPlnxfBWo7LKHDBMEbcxY3gyVSgT5qToARHBYReFvzNgBs0xEj_t6u67eTf_pW4H4usNPhAwn5LXf7PRFwlAedq7EtBVp0Bf04ZL0_EII73uZjQVkCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=gBSCg5JRndtDRz-SpgTIpiaJV6FKpFOgYDSHYd9MUuelddZSnUD08aPDyJM4LGFYw1QubPaifi2EZPRTMNT9mOihbqI5cBbJfThl8AJBqD31rbSzRXUmDyAYCJXnTHnIO9vBJ9IUA1p8gNVWuR48kQK7p_FueiQWEOtsZdWrOUqAI9jxj06lYZEMB6yJS7zqmjqnGiMKmsntDVju18CGVO0-dG2uKJ85Nwl8xdYOX8pdRMY7cSJJEFopF0zsNAeJduwsqKLOukLs7DPUSMbL1noyolKUGovENuihNLeQecW_gZ2JvN15XhJyYyKXZ0BoC0KyvL1_1EAFDy4LjLMmbr_ksPmIWxJMdyR82ENnTpfWIn0U5S7ZV5IuJNi-EdM5W2a-LSMDmwIZvRB7GbzR8OehCBmfHN-umlM7yUDyPBzimPLi88QCOwE82YxDtYL0bY2DEObdtX4c97FuZmEiXfTgEJMhLAUywtgRet3fX-bhA4CP6_xrWtzwS3QWnEtuv5RvXwp_G0CrgV3-ghQBl7ePOuZ7E2ypAKowjh9njRW0Rr3b_UqyfX5seASdza14-JdhPJuudCr7HqfPFJwSKHOxgypZjUpgGJ1j8ccU_3vuMZdqCGQewH_y8HOKhnjlIBcwp3Ln9OUL1NREfNSwFerCwwuOulQbUsH2XZjEMgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=gBSCg5JRndtDRz-SpgTIpiaJV6FKpFOgYDSHYd9MUuelddZSnUD08aPDyJM4LGFYw1QubPaifi2EZPRTMNT9mOihbqI5cBbJfThl8AJBqD31rbSzRXUmDyAYCJXnTHnIO9vBJ9IUA1p8gNVWuR48kQK7p_FueiQWEOtsZdWrOUqAI9jxj06lYZEMB6yJS7zqmjqnGiMKmsntDVju18CGVO0-dG2uKJ85Nwl8xdYOX8pdRMY7cSJJEFopF0zsNAeJduwsqKLOukLs7DPUSMbL1noyolKUGovENuihNLeQecW_gZ2JvN15XhJyYyKXZ0BoC0KyvL1_1EAFDy4LjLMmbr_ksPmIWxJMdyR82ENnTpfWIn0U5S7ZV5IuJNi-EdM5W2a-LSMDmwIZvRB7GbzR8OehCBmfHN-umlM7yUDyPBzimPLi88QCOwE82YxDtYL0bY2DEObdtX4c97FuZmEiXfTgEJMhLAUywtgRet3fX-bhA4CP6_xrWtzwS3QWnEtuv5RvXwp_G0CrgV3-ghQBl7ePOuZ7E2ypAKowjh9njRW0Rr3b_UqyfX5seASdza14-JdhPJuudCr7HqfPFJwSKHOxgypZjUpgGJ1j8ccU_3vuMZdqCGQewH_y8HOKhnjlIBcwp3Ln9OUL1NREfNSwFerCwwuOulQbUsH2XZjEMgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=nMX9xm6wLEkWLxji8rNA2BzUR3YLnUJSgwBsQTD2nYr2zo3rLZOhmD8Bt1UNrqN81eZKHKml8whK9AT1ULuQsQXzSW8qHvFyxde5gnJLWgFcM2_NweBLPxXZyoQSTLh1Q62hANxWtlAGH2kwOEOhrRz6Y3_ug3ksLIZdq12AKReMzzOAGeSF0_9sK6LzAY5AGroMPopx7GVFKAv3VZCUBoAJamA22T0V24fNlx1auba7Lzmk6PJjoK7fcUT2wA0IselX8jVqiMbY7CwGKzmn8vWZO4-S4sIVUObQM27iv0dKIWFhm14kiykz5gvu-Tcvni8aYNHKLzoONU7F74LTLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=nMX9xm6wLEkWLxji8rNA2BzUR3YLnUJSgwBsQTD2nYr2zo3rLZOhmD8Bt1UNrqN81eZKHKml8whK9AT1ULuQsQXzSW8qHvFyxde5gnJLWgFcM2_NweBLPxXZyoQSTLh1Q62hANxWtlAGH2kwOEOhrRz6Y3_ug3ksLIZdq12AKReMzzOAGeSF0_9sK6LzAY5AGroMPopx7GVFKAv3VZCUBoAJamA22T0V24fNlx1auba7Lzmk6PJjoK7fcUT2wA0IselX8jVqiMbY7CwGKzmn8vWZO4-S4sIVUObQM27iv0dKIWFhm14kiykz5gvu-Tcvni8aYNHKLzoONU7F74LTLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=vc9gx7J9X2G_2g9hPvthuPkba16Avv5pBHIh4q9JAo6c_c4zcyajdputzgUq7Du3Ecbr611yIVqIhGJGo7ekS1zwi9XmcuCxPfuFCzEYqGpxN5tHeYrLQHM6WGw7zel9QighKWdTORxWuABO8U_pXKpO_bfEXyDrfpP3CXLXnItOAK1y6wxlrTfI2zlrJGy01beou2B-NfZad4g9vWRY2SoUTi1YufrWJt5P-RmPBcqUb3xOpfT7TBGByq845ddy5jOnC3be9YrXCoaEyGkLpg5prQNCSpX2cfcPjhCaLKJfnDH1LRqFLtA7yEB8AeySak4QEdKpYn8tKFva-87uVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=vc9gx7J9X2G_2g9hPvthuPkba16Avv5pBHIh4q9JAo6c_c4zcyajdputzgUq7Du3Ecbr611yIVqIhGJGo7ekS1zwi9XmcuCxPfuFCzEYqGpxN5tHeYrLQHM6WGw7zel9QighKWdTORxWuABO8U_pXKpO_bfEXyDrfpP3CXLXnItOAK1y6wxlrTfI2zlrJGy01beou2B-NfZad4g9vWRY2SoUTi1YufrWJt5P-RmPBcqUb3xOpfT7TBGByq845ddy5jOnC3be9YrXCoaEyGkLpg5prQNCSpX2cfcPjhCaLKJfnDH1LRqFLtA7yEB8AeySak4QEdKpYn8tKFva-87uVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=SOSDo1-cU49iQCp-2PlUEHmqETaW15jUv5DN6zNP4Dr4sQ3h-f5XrCs8YECF-56TPOE4eNbjERwbQ64nDUtSD492mD0QA_0fa3HaM04QjiNMkgCa8KegnWWZAEVptshEm1xZdNPtoA2MKTD2mDlfAO4CefIsHyInJCejOdDDH_hOTFXjz9AGkbp7rsns7d5DDXAecChfaCNE6uzRWXvH_FBxjwS2lOtC1YUmYemFtYgyNNRubSedXnoBE7eFyLH_yeL-c8XPFpkDpCVeYnOfk2tJwxhxmoGiGC3eJh2qkHUDkUFaLrMeZ2hxMR4Dl50gHDkle4sPceu42gfVhPaWEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=SOSDo1-cU49iQCp-2PlUEHmqETaW15jUv5DN6zNP4Dr4sQ3h-f5XrCs8YECF-56TPOE4eNbjERwbQ64nDUtSD492mD0QA_0fa3HaM04QjiNMkgCa8KegnWWZAEVptshEm1xZdNPtoA2MKTD2mDlfAO4CefIsHyInJCejOdDDH_hOTFXjz9AGkbp7rsns7d5DDXAecChfaCNE6uzRWXvH_FBxjwS2lOtC1YUmYemFtYgyNNRubSedXnoBE7eFyLH_yeL-c8XPFpkDpCVeYnOfk2tJwxhxmoGiGC3eJh2qkHUDkUFaLrMeZ2hxMR4Dl50gHDkle4sPceu42gfVhPaWEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=mAAedXtpFxBUqm1ZfuDmdgc9uMAZtp8RfgkFT44G649-4RyROUDxhAJEk1WlDcyO5GYoD-Z9kSTMTdi8MUF7smAfBNayasQq5_INzkTnI5xrEqEsDpGRsg6eYooffZDEn9jnPRHa3K5xxTabXhcFLmMaYE1iJSEW9foAY6mHCbr5PmF-H76rzh6C-glZW9du2L8iIDhPmMKb7tD3YdwW9npxiJj5NuHKGo3OyW_aBnV2AsEDmzU5stImIzqY436Rk5hSFdBTCGfFfU828PlEO3HJGkz3NQpmX2wJ3JSHgnbbc4p_UsFLlHxjcbsbz90eOSZT-s0D23inBcjNooIUmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=mAAedXtpFxBUqm1ZfuDmdgc9uMAZtp8RfgkFT44G649-4RyROUDxhAJEk1WlDcyO5GYoD-Z9kSTMTdi8MUF7smAfBNayasQq5_INzkTnI5xrEqEsDpGRsg6eYooffZDEn9jnPRHa3K5xxTabXhcFLmMaYE1iJSEW9foAY6mHCbr5PmF-H76rzh6C-glZW9du2L8iIDhPmMKb7tD3YdwW9npxiJj5NuHKGo3OyW_aBnV2AsEDmzU5stImIzqY436Rk5hSFdBTCGfFfU828PlEO3HJGkz3NQpmX2wJ3JSHgnbbc4p_UsFLlHxjcbsbz90eOSZT-s0D23inBcjNooIUmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=ExjpodNf-9oeUfdUjYUQmraUG9oQA7GPZfgaf1qhMH51WctFPZv61m-oeID4cNjVdJRys8DVtupi741leWFr73tqCIOHLtZylkDAkPHVoXCtycyrm6o6HUWz6n_JiHugFyrKtKMB6FQisYrCpCZms4YJiPOtXaasM0YlHD1hav9NWq23XvIZ46YdjbfDxkXv40WcitQYSEavcNDp1lTFkL012sGiNtWNkAVbQLkhc7h6X_sCjYrwy-kSP0i39a7c9BBLkFc7c9xSXiVmcZV9Vu_VCYlspbKeyJuOMQPhR-jNdSwLzwXMTjlWV0zwoZxRHW3K0VwemwVDobsd2rYJCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=ExjpodNf-9oeUfdUjYUQmraUG9oQA7GPZfgaf1qhMH51WctFPZv61m-oeID4cNjVdJRys8DVtupi741leWFr73tqCIOHLtZylkDAkPHVoXCtycyrm6o6HUWz6n_JiHugFyrKtKMB6FQisYrCpCZms4YJiPOtXaasM0YlHD1hav9NWq23XvIZ46YdjbfDxkXv40WcitQYSEavcNDp1lTFkL012sGiNtWNkAVbQLkhc7h6X_sCjYrwy-kSP0i39a7c9BBLkFc7c9xSXiVmcZV9Vu_VCYlspbKeyJuOMQPhR-jNdSwLzwXMTjlWV0zwoZxRHW3K0VwemwVDobsd2rYJCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=LWrHP8fWmaa_OjVq9kGCkOgrxZWqGPSy4R8TKZ9i8kwRrHYAxOH3AT5bcC4cj7yF1JTNbPy2yL0m1HSwh15Isy3CZM-pnrF1fwZ7-eszbkDnEfhVMh7vrQNSymHYkiGt9I6vFfGXV0ZN9Ka_oI5TNAzVz966sbZl9wJ-C9bdxPUArzcxEnFx1PKG_fU5h7orXyyrwufEMvZhLyFi6eQGM4aX7vBxZsj7kuPGM6n_hNMOmfM2fj7x5eDgKMjEIBp3mbY-WG0wEatOhvjVvu1hsaK6J5ggwp9qfbV_xAtsqKIxT6aJvbH9LY6Qmj8o5HHhdchs5gbyI9mAYXZACj4MWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=LWrHP8fWmaa_OjVq9kGCkOgrxZWqGPSy4R8TKZ9i8kwRrHYAxOH3AT5bcC4cj7yF1JTNbPy2yL0m1HSwh15Isy3CZM-pnrF1fwZ7-eszbkDnEfhVMh7vrQNSymHYkiGt9I6vFfGXV0ZN9Ka_oI5TNAzVz966sbZl9wJ-C9bdxPUArzcxEnFx1PKG_fU5h7orXyyrwufEMvZhLyFi6eQGM4aX7vBxZsj7kuPGM6n_hNMOmfM2fj7x5eDgKMjEIBp3mbY-WG0wEatOhvjVvu1hsaK6J5ggwp9qfbV_xAtsqKIxT6aJvbH9LY6Qmj8o5HHhdchs5gbyI9mAYXZACj4MWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=P8Ju5p0z4V1q3G9CAyNNG_w3E4sn_ZolEAzr8lOfD_ZsCOyv4jCaoI2-IWhhRaN2YozomakowoXk1MdGpUuEucHJcAYJ8O73kyUsGGQQHeOEqAtLDWuido-Dru3TFxidQLclXhrFL_UvXZ3j4dpGWruSbY2H8VYcgEhk1CFqiy46QHiVvTRzP5-yy7YsS3u9PgHocqZ4WGj5Phg3KlMqddyjOBJo_pTQAYCuaTlHXYIm4UuxKRdrrDLXJGKUU40fIBd2Efr9CBFnq7dPFUlZwGhfFaXC3x3O5Hj2fj4QUfJI4P0SDNXUm7UtbwvpSKYe7SeIpdwEPNGVMwWYcoDbtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=P8Ju5p0z4V1q3G9CAyNNG_w3E4sn_ZolEAzr8lOfD_ZsCOyv4jCaoI2-IWhhRaN2YozomakowoXk1MdGpUuEucHJcAYJ8O73kyUsGGQQHeOEqAtLDWuido-Dru3TFxidQLclXhrFL_UvXZ3j4dpGWruSbY2H8VYcgEhk1CFqiy46QHiVvTRzP5-yy7YsS3u9PgHocqZ4WGj5Phg3KlMqddyjOBJo_pTQAYCuaTlHXYIm4UuxKRdrrDLXJGKUU40fIBd2Efr9CBFnq7dPFUlZwGhfFaXC3x3O5Hj2fj4QUfJI4P0SDNXUm7UtbwvpSKYe7SeIpdwEPNGVMwWYcoDbtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua9vC7Nod59yc9fYGdZaqJ5JSBlFXDs6e2k26UX-uvecIqorRCVdofvNLkmetjTsgckqrGFbeRBNiMl8mxNGODU3S65e3ciNkBXGZW-krBzZeUXxrcuTo_BswT8CNBu5_dIy66T6_EUbNUL4rrwCPgUd3ro93UhXc7cXYyB6cD08I5CHQHhf14xbNS4tvz4ZzoULRwu9hkjn1QBoDhm4EsfU075ZTHniClyBEp1FmhXXHKH-25vigs0wzKTl9IE1EBB68-4P07bba0hw2gl0BX2U4oFrtS6RitvXyjv11H04VBt-DfShpIqG7GVaBgx-Vo2wPH4pWrcmmUvGxnZoAw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=o6RnvHEMAsnyjX8VWPLdWvgtZnYS2ogrPnv9j58nxq9ABesXUKF_rnsOQkVMNMVBJNAD4fMKzVaBbOrA-9kKrFCYkSJcfcewKqVr3dA9HuoKjlhWZxznPBzqWlQ-mm2fdwjvGxWtCq-UgVw6ZgKA5Wczr8efigg5cHkn43GGmnJHhMIWUxUvZHaNyKDaoM0iRV_Ip6a0GUYZy3lpmWeync3Vyx8A6uTgXEMy6Pusg1PhTvTOLxL9e7lzIuH5czIhLkrGfBU7dJ9Zdd_8dN2d9q1ctftBrboggq7QdRgq5SJS5vhkpFnKgYyVHHPDFnawW6h7VFe2N4yahZ1a5O8I_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=o6RnvHEMAsnyjX8VWPLdWvgtZnYS2ogrPnv9j58nxq9ABesXUKF_rnsOQkVMNMVBJNAD4fMKzVaBbOrA-9kKrFCYkSJcfcewKqVr3dA9HuoKjlhWZxznPBzqWlQ-mm2fdwjvGxWtCq-UgVw6ZgKA5Wczr8efigg5cHkn43GGmnJHhMIWUxUvZHaNyKDaoM0iRV_Ip6a0GUYZy3lpmWeync3Vyx8A6uTgXEMy6Pusg1PhTvTOLxL9e7lzIuH5czIhLkrGfBU7dJ9Zdd_8dN2d9q1ctftBrboggq7QdRgq5SJS5vhkpFnKgYyVHHPDFnawW6h7VFe2N4yahZ1a5O8I_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=GgQj9W7pTbvmTD7-kF6Dzz1d5zvtaqm-9XQbo8bx85PC5QThAEBooOoLxIR432hV_Gzojruy2xEWKnvUFbB9dnxJZj2U95BcMWd6kTGN_9clF8VJSEfbT-62Yfv3MzV1Ujy_UUOz3F5vM_pdZU3m7aW4PHUiw2eIZ1KDrBS1-Xoc8jqVEuC6UrRboWvxzmbeMHsYQM3qKrKblWX7nsMBIxSvY5g9ef-wPSo0TH5rLhFIVtcL9IpfittfjhXTK1cX3bXvxt7Q71YMAxm4AP0uGsjn1DUcSrdZy3Z6Z_EP7eAnTzzMDKLSaMNzw0a78zsq8YtzmBpa__qNYYpP5krvWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=GgQj9W7pTbvmTD7-kF6Dzz1d5zvtaqm-9XQbo8bx85PC5QThAEBooOoLxIR432hV_Gzojruy2xEWKnvUFbB9dnxJZj2U95BcMWd6kTGN_9clF8VJSEfbT-62Yfv3MzV1Ujy_UUOz3F5vM_pdZU3m7aW4PHUiw2eIZ1KDrBS1-Xoc8jqVEuC6UrRboWvxzmbeMHsYQM3qKrKblWX7nsMBIxSvY5g9ef-wPSo0TH5rLhFIVtcL9IpfittfjhXTK1cX3bXvxt7Q71YMAxm4AP0uGsjn1DUcSrdZy3Z6Z_EP7eAnTzzMDKLSaMNzw0a78zsq8YtzmBpa__qNYYpP5krvWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=fSXtvJpiGx1BLdtIp25Iu9-lE9jLbQLsd2dI78d3QvO5qaL8qtgSTnEr4Gk7g0TRptNKI7wM3Xk787mh9K5fcvII3ZmZ8XJUq5OkXQk7nXSwaK9ag3lZE7j3yp46cQi5OObs7LHY1MpUZA2yDJlDo4M4mX5mnKnqdDnDIEgjFIhwCWRBEVKnLVWKRxO6WWNKBci5XEVo3DRN-RhJTHDou4HtPegzBxiuvV7lk4bI4aeU0L_QPncQD_pB5MDPounID1f_5LsKddbKSXBibdoAPICRDPq_mYDA8NoA2aOEwfeGmqVUe1g7yC-ggFVJsI9OzNu1i67mDlu9Du0YjAPk8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=fSXtvJpiGx1BLdtIp25Iu9-lE9jLbQLsd2dI78d3QvO5qaL8qtgSTnEr4Gk7g0TRptNKI7wM3Xk787mh9K5fcvII3ZmZ8XJUq5OkXQk7nXSwaK9ag3lZE7j3yp46cQi5OObs7LHY1MpUZA2yDJlDo4M4mX5mnKnqdDnDIEgjFIhwCWRBEVKnLVWKRxO6WWNKBci5XEVo3DRN-RhJTHDou4HtPegzBxiuvV7lk4bI4aeU0L_QPncQD_pB5MDPounID1f_5LsKddbKSXBibdoAPICRDPq_mYDA8NoA2aOEwfeGmqVUe1g7yC-ggFVJsI9OzNu1i67mDlu9Du0YjAPk8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=TTwEjVH_qVV3UceHTyhNuQIAwE5XoW-3QDVVd8jOYyyf_Pby6eXQWy8eE3eWH8o2L3RMxkRjlpfC4Ebo3QPLXiN0XmKeWKIOvWs-4dFtVq76vhBnlIZ-NIZjHgcMM8BsgAGqywEGHNpPLz4lychJan-zNWAWYDb-zxMkh_giCH_iFgInJyzcTfR1W1j7NYcWOLRl420gokYd6iRLbtrf2BJDpLDz5FBLldzGz-nDU2DyqvAWAzeUBUu7W2pHiSCFgeOSD-bRLFm8wvin7aJ6VYmebENURzlSddGAqSzKXAAeDM6LsbzpCLqQh2mD6VahlYSTBOwPbFPWfgqdN5cTug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=TTwEjVH_qVV3UceHTyhNuQIAwE5XoW-3QDVVd8jOYyyf_Pby6eXQWy8eE3eWH8o2L3RMxkRjlpfC4Ebo3QPLXiN0XmKeWKIOvWs-4dFtVq76vhBnlIZ-NIZjHgcMM8BsgAGqywEGHNpPLz4lychJan-zNWAWYDb-zxMkh_giCH_iFgInJyzcTfR1W1j7NYcWOLRl420gokYd6iRLbtrf2BJDpLDz5FBLldzGz-nDU2DyqvAWAzeUBUu7W2pHiSCFgeOSD-bRLFm8wvin7aJ6VYmebENURzlSddGAqSzKXAAeDM6LsbzpCLqQh2mD6VahlYSTBOwPbFPWfgqdN5cTug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvpU4pPe9b55jX-B3RA_XlFBQ5WF1tVGuGuYElLyTs4h4O6i4_XK1B-wZFTNN3dRSRUZtpPzz9qjQKLo2g_dcdK9QFDaPbo7pqhu-OehOvelsu_xkrumjyJNCPJEj9kd2HSFZrmdE02kPWuQa95E62gv-g4q3IbTqXHN6iNsVtHTRmrbeN_VhfPZ8Fz6VP2YdSrnWmWPWeBAzDKQ7LNV8WNPFPnVMmw7ZJ3hgQmvkTsPm-ScnSXIMvydrScOMsYAZdJQ2TZzzJ9n8gbj-n9mQ1Ew3jWcKtUFsmELVkrsmq-Iq7a99MmdjJFpMRS50bHojd-kHYN7lbYRKYx5VUR2Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=bXPfiZUPALa3eew3kNQQGp_-wWUi1rDPGZj-2asONI2vyEQrmDkEhndQkPKCN-EpJgTg_Hu1DYwzkHFC-aTPBZrAbfiyCP2KapmTQ-3-OABRMpuaGRXHF6Foxk3qcu2IqGp_93_aDG-4DAWIXS_bnwrOno9gRv8EmhmjmDYNr4LezL-3ZBK2_ZEjJEyjuatkc4nH2ryYPNWl5aZzcwQYTT3G1Vyxq78pDBJ22_ThP8ZN6znsZN6TN7-Id-d0ya8fxUlXpT4gax4fU5cLoTuCLPVvAM71Z30UDk90eadrLxjQfwDibqcELkrx3SLK_83czRB79K-sN-ie_PcotnDQzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=bXPfiZUPALa3eew3kNQQGp_-wWUi1rDPGZj-2asONI2vyEQrmDkEhndQkPKCN-EpJgTg_Hu1DYwzkHFC-aTPBZrAbfiyCP2KapmTQ-3-OABRMpuaGRXHF6Foxk3qcu2IqGp_93_aDG-4DAWIXS_bnwrOno9gRv8EmhmjmDYNr4LezL-3ZBK2_ZEjJEyjuatkc4nH2ryYPNWl5aZzcwQYTT3G1Vyxq78pDBJ22_ThP8ZN6znsZN6TN7-Id-d0ya8fxUlXpT4gax4fU5cLoTuCLPVvAM71Z30UDk90eadrLxjQfwDibqcELkrx3SLK_83czRB79K-sN-ie_PcotnDQzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=tEy_KPKkGYwgMDq4GwFJadRB7kGr2EccvqtmXnZlB0tuDEMaK-K19iNLb5vYqwvvC9OG3M1YmJEma6rwkJlQWOAyZcIWZZ-mNCBMXLvhx_7_4ZLEYommjocjJjxeecOkfnunLxV_GdkIY0Vv0-3wp48WQlV1XiLpBrLpla1oQywVynjQt_9OG3azV8Ta_OCcz0Jbn3nlsbgk7IDzd5s6SWEWvCQPgki2M6uoiiUTtOUiDmEhHvWlpBUoPgzYAyiWe3FSpbQGKmdQml0Yb3EpdI5qHxRddu8YsiUl7Ggmsaes2oEb8rtCNBkZqlR33lKto2NrQ-gqBF8bnXltNVExSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=tEy_KPKkGYwgMDq4GwFJadRB7kGr2EccvqtmXnZlB0tuDEMaK-K19iNLb5vYqwvvC9OG3M1YmJEma6rwkJlQWOAyZcIWZZ-mNCBMXLvhx_7_4ZLEYommjocjJjxeecOkfnunLxV_GdkIY0Vv0-3wp48WQlV1XiLpBrLpla1oQywVynjQt_9OG3azV8Ta_OCcz0Jbn3nlsbgk7IDzd5s6SWEWvCQPgki2M6uoiiUTtOUiDmEhHvWlpBUoPgzYAyiWe3FSpbQGKmdQml0Yb3EpdI5qHxRddu8YsiUl7Ggmsaes2oEb8rtCNBkZqlR33lKto2NrQ-gqBF8bnXltNVExSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frktWbGqjZ4VQ-WhTpSExD1rk0-3X_WVUY9PrY55C40XYqTrSNNQOcSs2fz08EZLOAAWrJXDAf7WTABSxO_v9ZQwYlMU_K8wt8OcmPKSLwU5o0k7Y_SoZTHRExuVIkP4729Z4nxy1-tGRoou8OWX5QB2avLYLPV-sg8QyRVMx8VjEvPJpKQ3VTQqha2FDyyQr7ktLfk_Tv_zs0KaiC3otvDJPgkOoC__REpEZ5bDGNKKK-uteDgTW2nHC2rt--2N-D-S0BjPG2X9b-dKFZVmPSSFGffFXES7MWZW4POuwruyRVI7iJlmCK6w4vvnTMDTsLsW55uCOBXW4vnGzcS1pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JXGrUOCuPPB8U4yak_1AdjChmbPKTKWGxyRUeSLnrrZmvxmQjiLDvHGtOKBhGxloXb7IOOTp13x--OTLq-dvnR-Om-a_pBAy-bdU4jsiqyKSJuLSWW8PeX8eQ6eCXVacispc-AshkI-hQVO-IPWmE1MJxJ3PA1YgQMcV8fHBvSJCAU1SaNWJBhMZfd4ooYbUHmibypbG5RD5lI34YHNy-KOU5ZW8wmvLpQzHvFTloyw87EVICv5R5I0AdbxOZ18QVBiHWtMXNoZj5cBCaehIl-1lMZkpjho54ivbAFyF98-NZoPUhaiAXbPNHsxG6icQvLp-qpP-5ai8y9SnCPBVxg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=pdQzFK-X8Kc5ZkT-_Fgxsd8vHjXXV5qo0PWck24sDO_KjAGlVK6tzt3dOsoqFw9s9b95EngRZthj5w4zHnIjYN1yHvq2o1cXcdVUpxlf77F-NGdplnHpGFu93yF_nzyiCBqyo0zn1nXefRhNLi0i_5V8RsWlmdQMLMZBd29zSUXaDMg9RWoizMT11NDdOR-AlAa6rQ-eGvVjND8c3Bnhclchp629ckrTIc9eS0ak4mIo1Folf_YlM-qAO20fxHZnHS8XJLdJ42VpDcnJz520o6p5NUfRZ4iUdoZ9KiOLfv-ddBxKn3u04JCvOj9ePULwbEIQcpsB4Ic4aSrPT4Kg_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=pdQzFK-X8Kc5ZkT-_Fgxsd8vHjXXV5qo0PWck24sDO_KjAGlVK6tzt3dOsoqFw9s9b95EngRZthj5w4zHnIjYN1yHvq2o1cXcdVUpxlf77F-NGdplnHpGFu93yF_nzyiCBqyo0zn1nXefRhNLi0i_5V8RsWlmdQMLMZBd29zSUXaDMg9RWoizMT11NDdOR-AlAa6rQ-eGvVjND8c3Bnhclchp629ckrTIc9eS0ak4mIo1Folf_YlM-qAO20fxHZnHS8XJLdJ42VpDcnJz520o6p5NUfRZ4iUdoZ9KiOLfv-ddBxKn3u04JCvOj9ePULwbEIQcpsB4Ic4aSrPT4Kg_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSiWPZk92IsdD2UBcRL4Xpk-H9EdF9FWB9_fwZkkZcRQQ9qLIJo1BXEUXege3cnG5Oe-jzVOZ9Zzk45DLsDUDqAZb9H04-mcnA_vwXjkNlOtfsrCuGWtuFoXkczFh3SFJIOh5Krt09jbypixzqen9Uhri2jBF5lk3sRTcsgoYCoYq11TEhpds9PinzUyY94TamvE8249Pvk221VOBNpjzG0eG6y_HNUxPsenc9EH2ePvR9H3EeBg4AWSXtEEwhOiBPoKvRexUZL8zTXciAsH0hNZbukFT5ST-ezn2BuTcA0FPxS_ikputnjA-35ihTFFArpzTmkOp2vhqqxKajiMBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG-cGQKKf0-OK-dtyQ2oorbuzw9KMd8ONxnqhCSORZFLnbPK9J3R6qsJl45kgEKfcMaYruhMtL9qs-5jL_cZvHPMBDCBxT1luJGOM75vB3q6k523FWl_oSeOlUUc35eIfnT8vTyqDFtvxXfFAzE_bNZy--FUVwFcWIlu0xbMeI4pSBMhgbt5x-nhaAmu5p-rUfIXZq9XLTwY1rjN7h-p81qjY7nCfzXLmkUqmWOx9FHAm4pHpH-62M3HUC4JQDqBQRwmYCy3-HtGCcC-d5XoLYMhu6Jw2mO6Xuwp3LztZtioJS0TwDhgGGxBcFiFWM6lBp-k0Nlgi35FUrl-vd4Hww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlkC2LfF6-sxlLCW8jxEBvpsR2kvgm9M8_X0pBnE6rArvjm61EpS5nhn_FoEqjOsO30rUYiDWF7chJ2aMjuBkhc2JrCDKV9AEz4QxyLDl-jXqnRPnjfFidaIoLBmjJtqbpj716zrIh4_muFR3tQRP0W2sTEwCSt_wI0p0WiVafXcFhGOIhDnNu6U9Zjhip1RbWKpVq5t3iCcCdWiAckHX2_13ESyj8gjhfPIVfnjB5_eK81CyJkltSSm8-JQVCuwL68datEvO5HgoO3nIxXFWUcFsi1qnNUItWEhg25Fn5zUxRYuJO-g1shrPAM7Ky7UO667R5RO6uaezvEN7gObxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=a_CS_eCPPjwpF9Kk3yLiZpdGElnid0qVO5ngcdEb3nilR1M0w9Jw5RcW9XN21yLIKphxGR8WTgmg7Y4RQPbZN3Q3JSct8b6P72S9rRWQu-mAhIcZ0DTe7fMJOSHkNfIbToIMhOhJHN1WVbZsYyXA_71yCtpYv1NBVZ69P-Pl8ne1JDgEl7IRrzQA7ScJkbncZmHvMEkvA_F_l1Xv7meP-LEn4HoI8qlzPAm31JapzbkYjdulfHm4tNW0xQpPbVmnqrH-BHNqyzEWaGC174IGqsleuwc4L2PJqlLCtyDg8DChyVMHRMf-VAnhk-2ZnXr3826IRwOnUoqPhaPqj5LDCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=a_CS_eCPPjwpF9Kk3yLiZpdGElnid0qVO5ngcdEb3nilR1M0w9Jw5RcW9XN21yLIKphxGR8WTgmg7Y4RQPbZN3Q3JSct8b6P72S9rRWQu-mAhIcZ0DTe7fMJOSHkNfIbToIMhOhJHN1WVbZsYyXA_71yCtpYv1NBVZ69P-Pl8ne1JDgEl7IRrzQA7ScJkbncZmHvMEkvA_F_l1Xv7meP-LEn4HoI8qlzPAm31JapzbkYjdulfHm4tNW0xQpPbVmnqrH-BHNqyzEWaGC174IGqsleuwc4L2PJqlLCtyDg8DChyVMHRMf-VAnhk-2ZnXr3826IRwOnUoqPhaPqj5LDCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Na-i9HylvX1wPI8XOUsGYWXRJY5IfxF5XI1F0s4y6jSct3FQpaT5volXLy3xaFSZrEKxKCPQo4ASBCJrhN_SEO7VorRPOBhMpVlZMeWQboo81DyQbbK0wA8NFGBDSmsohbsjWNosZ3auSFudSX0aPqbIGoS5eQNg686e4N8hhV7jqhkB0Jm7FZ66uPUymxMHNdQ7V-qx2pq387_-NXn5rjj0pXdI1MivUX4ZpPAXl4-xoA76TyqnCtUi86RDUVYt9FyKj4PkPkcl_0HlG4R4YhDlaD6z_vdbNtacalAC4OyUjDYBtKrZW1CJBBp8igwnAKWMy4IRrKhFQFqw_RyB7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Na-i9HylvX1wPI8XOUsGYWXRJY5IfxF5XI1F0s4y6jSct3FQpaT5volXLy3xaFSZrEKxKCPQo4ASBCJrhN_SEO7VorRPOBhMpVlZMeWQboo81DyQbbK0wA8NFGBDSmsohbsjWNosZ3auSFudSX0aPqbIGoS5eQNg686e4N8hhV7jqhkB0Jm7FZ66uPUymxMHNdQ7V-qx2pq387_-NXn5rjj0pXdI1MivUX4ZpPAXl4-xoA76TyqnCtUi86RDUVYt9FyKj4PkPkcl_0HlG4R4YhDlaD6z_vdbNtacalAC4OyUjDYBtKrZW1CJBBp8igwnAKWMy4IRrKhFQFqw_RyB7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=c-a348agQhQ33E0SKL3QMZlVWCnhqI3It1rmy9Arc8rGj2fZqA8bhnK7A0oHKeXc0gS-Q_MHIjL3kcwntbkL9DtPhG5UBQGhdDY4H_7ZNVdjxJ6IN-g6djM-v2upRXTAir8kH1mapK3bldGKwBGNczVlUaIy6UdROXE3KHSz7CGJz62e9yJAdl3wYG7MsYVogU_zxhLUzbt038D941n-eZdfrnGbAM79arP7mOnMkzxnBRAQyzCXcqFXR4RJip8-8hXLbi6RxHs9nf6SHWY8NNhd59ESRqjIhI_CL7nrCMieiYzzEUOSLWQ-0mCkDxFqW0rt1Eq_Lz1LKLxdgUbzuzealToA1vjkmeLdTy0A64YU5O6vCY5BVQA_i_OIvjmZiFRBJaGT549HKYt7xpdZstJjl77TV44GOmFjxJB46sp8EqDjRNmRInsQ9-OxN_MvpxiPU9PwVYL0LpvdPflzhI8ng8Zr7o1mfekKr6-AJZV8heLt8iE6Y1jvFoAMqk6VHQzIFHRn1PN-qFmxcTwOMhUBY8h3uJEtAnUVJGm-b-S0Q9yfwev7TwcOMPgwO-qK6pK1cMHo7YogPhW7xVvXIZB-CEkTWrrheh8Xsg3uD0OPQJVu4uSx13W8MKtnuT9MKPgXLx9YOB1J3G5vVSPhJdoiKHXw6nUf1aMdVZujqyE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=c-a348agQhQ33E0SKL3QMZlVWCnhqI3It1rmy9Arc8rGj2fZqA8bhnK7A0oHKeXc0gS-Q_MHIjL3kcwntbkL9DtPhG5UBQGhdDY4H_7ZNVdjxJ6IN-g6djM-v2upRXTAir8kH1mapK3bldGKwBGNczVlUaIy6UdROXE3KHSz7CGJz62e9yJAdl3wYG7MsYVogU_zxhLUzbt038D941n-eZdfrnGbAM79arP7mOnMkzxnBRAQyzCXcqFXR4RJip8-8hXLbi6RxHs9nf6SHWY8NNhd59ESRqjIhI_CL7nrCMieiYzzEUOSLWQ-0mCkDxFqW0rt1Eq_Lz1LKLxdgUbzuzealToA1vjkmeLdTy0A64YU5O6vCY5BVQA_i_OIvjmZiFRBJaGT549HKYt7xpdZstJjl77TV44GOmFjxJB46sp8EqDjRNmRInsQ9-OxN_MvpxiPU9PwVYL0LpvdPflzhI8ng8Zr7o1mfekKr6-AJZV8heLt8iE6Y1jvFoAMqk6VHQzIFHRn1PN-qFmxcTwOMhUBY8h3uJEtAnUVJGm-b-S0Q9yfwev7TwcOMPgwO-qK6pK1cMHo7YogPhW7xVvXIZB-CEkTWrrheh8Xsg3uD0OPQJVu4uSx13W8MKtnuT9MKPgXLx9YOB1J3G5vVSPhJdoiKHXw6nUf1aMdVZujqyE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=QV1tE3eO6uV4P_fc91Kb38Ysdf208fnNngQFBASUQg7L3ce6wFXsmNdbQtzvuAs5W38mHNL-C_srwxPR81UC5rjf-wrXe_cwSDl3MHvkKmGA0FEFTc7wgpILtw8tp5ilj_yOT1LNL6LChC3-CgFYsfPXuA6E2mYuTdRgfxUCfHJLo4Vb8gnDJ7H6L52BTkxw7eJKOe7XU5NqyxEppRBaJx7tARmILyL19fvovatXkp7gsbjB8uITu4pTkHD4bY0oMxthrngSwlbsKz6EgCIaZgkdOZeJlnqYWiK8YDHmx4sEQQBdJ_oYN0-pPL0r5SeABj570YUQMk6UX0-6XLYtmLf9GA18U_OQhbWrLjpWV4_P1w60-b3xkOxJFOa3IohOm0tnY-kYxg2N_IYYsNaXHhjziPWC4iPuyf80p3XroSoBkEKgIhnWs08Yplwu4SuwHe4qCZ4QhmDmOeuHcnmEAhx4nwU4VE_A2DKuKaupwqs_Qu3Aiq_7-x3QUmE7-pcUSSRSYxij7_EQB52Nkk5P2Z6Yu-ojAHZ9q6EIRmjWHq5JGHJbat65R6NxFCRQM9RnV5kjO5yQQmKA1vZJOMuOCQ6qnPjI2Nnu0ES252c08H5B6ZiKaFrxwZcqi7s12zlu_EsHM9iYZYIuSU-vjXWixXQPtolrMiLEniCXf7U3Jow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=QV1tE3eO6uV4P_fc91Kb38Ysdf208fnNngQFBASUQg7L3ce6wFXsmNdbQtzvuAs5W38mHNL-C_srwxPR81UC5rjf-wrXe_cwSDl3MHvkKmGA0FEFTc7wgpILtw8tp5ilj_yOT1LNL6LChC3-CgFYsfPXuA6E2mYuTdRgfxUCfHJLo4Vb8gnDJ7H6L52BTkxw7eJKOe7XU5NqyxEppRBaJx7tARmILyL19fvovatXkp7gsbjB8uITu4pTkHD4bY0oMxthrngSwlbsKz6EgCIaZgkdOZeJlnqYWiK8YDHmx4sEQQBdJ_oYN0-pPL0r5SeABj570YUQMk6UX0-6XLYtmLf9GA18U_OQhbWrLjpWV4_P1w60-b3xkOxJFOa3IohOm0tnY-kYxg2N_IYYsNaXHhjziPWC4iPuyf80p3XroSoBkEKgIhnWs08Yplwu4SuwHe4qCZ4QhmDmOeuHcnmEAhx4nwU4VE_A2DKuKaupwqs_Qu3Aiq_7-x3QUmE7-pcUSSRSYxij7_EQB52Nkk5P2Z6Yu-ojAHZ9q6EIRmjWHq5JGHJbat65R6NxFCRQM9RnV5kjO5yQQmKA1vZJOMuOCQ6qnPjI2Nnu0ES252c08H5B6ZiKaFrxwZcqi7s12zlu_EsHM9iYZYIuSU-vjXWixXQPtolrMiLEniCXf7U3Jow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=TGbw6bOHPNW_M00lPhiwRC8NRmUQKOkxd7XGNdb6FwieO0txpDpU8vja26INzaGOgdrSa5YGOfQS-bABr7SQ9lbHqG_ZD8Yme6MBuBf8AfIKk2_165NCD_2Lw3ikZyefdWu9ATa99DgH8bReqFPZXPsg8M36of-k5Mn8el0ovhs-WEbf0C6Q86OEYq3DsDA_URcfFhjLJOS6o7TQTIdVe-I9PmaOAUL-UOH6fvvqw3MJi-e6_uDAXdBaEF-b4L-pBf2avYd0nhzGNp9gN6ADMhj0w2kboxTde4XqSNVPYxVRJPviVufFSfL1KY06nIU7ay4hKvCNMIyDtH9ENcoypg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=TGbw6bOHPNW_M00lPhiwRC8NRmUQKOkxd7XGNdb6FwieO0txpDpU8vja26INzaGOgdrSa5YGOfQS-bABr7SQ9lbHqG_ZD8Yme6MBuBf8AfIKk2_165NCD_2Lw3ikZyefdWu9ATa99DgH8bReqFPZXPsg8M36of-k5Mn8el0ovhs-WEbf0C6Q86OEYq3DsDA_URcfFhjLJOS6o7TQTIdVe-I9PmaOAUL-UOH6fvvqw3MJi-e6_uDAXdBaEF-b4L-pBf2avYd0nhzGNp9gN6ADMhj0w2kboxTde4XqSNVPYxVRJPviVufFSfL1KY06nIU7ay4hKvCNMIyDtH9ENcoypg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DksWZzfrnABwrBJKVlSR9JBYukRFjK_8CBVCY_MAmG7Kfse0Wu6Ea1sIWxjnyj-CQuVJeBUZ7yPHAhauRAqRFplxfOEz9l5lFffqtWshyw029Cmpzpbg7xWomEcIMceeinm7-JGJ6H4ix_4jaJIdCg0I7r2C2sZXiJ1s63dnML7D0THh4igo_amq5Te0v8HZWO8xA2TXRnCbLjaxPblukEZQwMbUduG1n1RpulP2nc6H95AQ-zZTwA861EdPUMBpQUdDVpX_70c1dCdbLgyyorcO_rzgLyv2YGPDEtZJBD64qg_UGG_HagvBMtOcZvwpkvCsdXIZP2c7Fbmj9k9e7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=L3xZK_u8xcqDi6S8yFlcQSY5fVvEOGk8mFpbEvTZyhJWGrJnSJ3SI21PlemBvsxUkB8rUJWSmRDKrVkfaivy7Fgh2bcbhwgdCpXISBmVQYafycp-5rPmxcRPB8Q4H9fcvV-qbco_FEePwgdD2069UPs4azBMzC_70SdvkMjSyxiErzdJ8g8qcYKVoWokexHkp5L81F2mQf1eAlR_CuG3O1fZUa1-3Q0C-a1cFxNGaDNkvnFMVhcN30zsEyASaW-SKAa8SX6UBDpzueferNXnRyOqV9RjjW9vB5wrrx5qigPndIQzVgxFlWWLZiDJjq8jr80a_BKIwZpCvzLzryM2Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=L3xZK_u8xcqDi6S8yFlcQSY5fVvEOGk8mFpbEvTZyhJWGrJnSJ3SI21PlemBvsxUkB8rUJWSmRDKrVkfaivy7Fgh2bcbhwgdCpXISBmVQYafycp-5rPmxcRPB8Q4H9fcvV-qbco_FEePwgdD2069UPs4azBMzC_70SdvkMjSyxiErzdJ8g8qcYKVoWokexHkp5L81F2mQf1eAlR_CuG3O1fZUa1-3Q0C-a1cFxNGaDNkvnFMVhcN30zsEyASaW-SKAa8SX6UBDpzueferNXnRyOqV9RjjW9vB5wrrx5qigPndIQzVgxFlWWLZiDJjq8jr80a_BKIwZpCvzLzryM2Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ml6oxcsjyBPX-lkssOtwSuAC65oyv0auiEkZNykO1ZdiKbtLs8qkBjAaC1IkWk_Jt0oe5prQreO0JC4dBB_13J-MAJJ47_6lx9XMRco3RcIm79hqqMgpgtuU-NqeXNuvE7q5DKpZH7DcuUHKM5zxEH4S4B-AwwLbCtBqm6LRn8gBkMQTVxmDY3cEfIHSlO7qA9yZ1Fklzmq_gHrMbjgt1Nqz9TB5vMSwFAPdrortC9lPrYmb09Ry-yX4WJY8VV9K7wA8t4Te_fhsumgIrzOe1zPAwZedzm6XVAiSYtMqkmSrvCH9xD2B7mvZvIfbYOOKpzlKEASDDZIa1AFHz0_oMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ml6oxcsjyBPX-lkssOtwSuAC65oyv0auiEkZNykO1ZdiKbtLs8qkBjAaC1IkWk_Jt0oe5prQreO0JC4dBB_13J-MAJJ47_6lx9XMRco3RcIm79hqqMgpgtuU-NqeXNuvE7q5DKpZH7DcuUHKM5zxEH4S4B-AwwLbCtBqm6LRn8gBkMQTVxmDY3cEfIHSlO7qA9yZ1Fklzmq_gHrMbjgt1Nqz9TB5vMSwFAPdrortC9lPrYmb09Ry-yX4WJY8VV9K7wA8t4Te_fhsumgIrzOe1zPAwZedzm6XVAiSYtMqkmSrvCH9xD2B7mvZvIfbYOOKpzlKEASDDZIa1AFHz0_oMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sgef3xCCX7-r8xnFSR3MPaz1JU6-R2A4i5J-naEn3P5KxItKJeMsnI2wyZrNLaiDjld7e06Jf2E5GKXfgO7fkIzqIiyImjA9FUk1z5u4lpjSvEkXrOvR3k1pw2e9ET_wPz2CQLl1keLrjX16pHx08cByFZCZYSCRJX1gGUYd74CAV58zi0ivCaWwGRozmjrxwDHQnm9--JEG48rvNAGIJVpOlHJq622s7kGtU6fLv9SCSP7T71kfX-scGpRW-v9Sq7iWjpA9Qk8R5LUmWUQ-sKvOrEOkaH03VOd1AWsjr8KsEShsVMZ1tsDw1-vrFKETnnJofU__HpYqNTXUCTDWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ltz4p_PfARHicN_7HhGa8sBEURIEdvAsLj-A5D6ladYJpyxLS_4K-UPvYM78zgO7D0OmYGHDmWX7cJE9b_N0Ke6IQ-dnOMbwccxarSJio4WMjtIYAdInDm4zYTousFSGaLyWveJhf6PfjJeY_BzSSrjhZY6FULAZR-Gs3uKrDB_sIX6RiddFOgAXWc3tkWdezge8P__5CE_Vlnka_NsUx-TYKmdO9y5aoLlH0YiROdAn48guwT5fmy3zaHa7x5BnrzSodzL_7TnSJ0Tr-vuTMSCcMP3ols_pCrPuIrCNDVuGHGs_JeF-RZNStSjyO-WVizypwNvVNVw6yQyLUZ7gbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vt1c5Wl1JQAKc-NlU8xZrfuzhcWE3j0OgXvmrWkOxoNefVdS5Bq9pBq44AbErpZccgCAAeoq2Y7yePt9O59tuHx2ge7yeXD8mcnXE6IoBZ5ktK8Io6dvPFMgENkMpMdi1xEp71QkTjUdpL9GHNk_xlJuVhLyBNsz2SutqHGUcp306iscADqc-ZMgd3C3SE0eb8DI6gT4ihnIu2566Qn9NjUiWHrkOY4QGDawaBnw-QmT1pbRItBWesi2Pm_bLYZY-5_86RnKSxoJiqfxl78f3TkpUpzgK7BSOAQDyYa7-Tyw48MTCLxzB8G1sQws4cXh111P6tgbDdSeR9xGXd6xKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoWZiXJF1spz9ltJV7Qm6i6b3vv0WXpUkPLP5jgMF00jfhSJvNHRSS_o0_bXgwl48yeDC88FJ53yndEKFg_Jq0RKEaDq451s7XOIa81-eWWEnFDRRxs_Y9OjunLyOh2kWiJAlhZ-MNbFVSz1EfvBR6VoYSrjGnM6LN_2z6JCwzLp4JkFzYZhVqrRS2c9zksW7_EcHmVkAwyFmhHkRAme6OR4f_icEfca4D1VEFAWgr0ucvIhJtG9-BQ0jBTqGqyXKoudU4yg_HIaadFQdZNKMhwPpV78Y2qAE7tcoSuqRhGiZmneIlY8G74qC6WmSC3GXorL6qnXjWRgk6bDettZBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWm5eTHCC5lMsCoWjbGvbli8jgTDNDNx3Zueh9udSQyknnj4d4uxgdKpCJmOBHIXHkl6eTx_pRNhDSbBQiW9yaQK7gjQFsQsbxdofY2zwMRLHaAXH21L3gE5rhliOC-Bx9X9PXOjwa2Rg9XostI8lQeGq7e5k8FLHtLZoeX_i77dno-ZyylFMWSkqFcAwhV1LUDmu3xzGXoDbKLgItuEHyVGubBRR7IkmInkKUYuMEtRmA8Jm8w-7S9OVjnbsnS9eYlLeDZme0kCFHnMUgXPn_xYCgbjejKhCNmJiWG-BSIBY4OzJKqjZh_2yWtHXdVKvJUvbZCYOHkqg9AugWFJhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nz9ENHLojEYUFACRww5m-N23F0wk92l17b502zmOI0jrrDM4I1doXnL9o2SNEtgGii83eWXCHkpSLW1X_t-TxnRt7Ss46wNMwejZx4QYMAqfLn0-MwBaEPNM-i4orrLD1inJ6qc2gddgrGHWy5NDRy7S-NbUd3MIotTWl4jDn0h9tbBXpZRaRmyzh_yBTa-T9uzGgG6MZ8sUDTEWDOMepdsTrSG5KgvZB0uZrzEmCmm6uKJCS-Ui6KzpP7N_HxBfLNiGKwGYbO3uz_ZDo3AfTcjI_Y9x_cDEqhIbk4pzGGNuZD882eTs0RuvZU5dqThi0VwsWKew8bTyYSNXjgDV-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGYOjLi7pCpBDSrXNligd6-_0v91QnBclQHFmV0hUKbZoUqUCEi8IHjsta3aX0292kFo-ZzxsonJPBLq7uVALevpZtmsEbhGaH6_Y6WDTLEuBlOjvxFp95TcrM0F2jU1pTg6ZVMr8fE5DTlUDhwyHx4r-4Jj_Qa3V7JT2RNd9VtGn6FyAPJc6BRvSasZr-V0HgFRSF0VbKMeIqApqDyTkErj7L1_U5GfRnAlyhcVLSoJL4UFVDNnCPXjb-8q_-xCURbbbJUppt-w6-zfu7scJyEEIxDOiDRS304S5bXjSQCqq6MH1IGvu-U99OTcHFJuhBH80j2-2P9gAL8ZNg622g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjpxLfAmhN_xxk5sStEbfUjq1fHtQ0Z8T7VSTd5exaEDIw7IIBU6Z_fgzfn-qt7b2FSenegAoINB7bEA9BhY6E-_W8NaEYy66SZm4VPh3Pmu48aJ1gajgn-6dK_5LCWHd4l_21dhatWfySvXZmZbbh5zYU44JFxLNAizlsdkyt77hQ0SpmluxI24oOW1172DXyD6aQcf81W76Xf-9S_mAKG0iFcbTEB0yNJh-JGW04tJ6t_iXabfAU0iHUwFRGfmxKM9yCaxGBoKqwQJwse4A0rncW8DRKN0XE8v0WBRUaxoAC7DRFNyT8QPtaohe8VJ7iLYtIcRJ7Lk6998UD2_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcDx_bh3ta-BgvS06qY2mljATwBJWvKKre9gwXDR6GDieXv9mUl6_CrFPziRZdC-LUGcuFtzfNfiYMPFjzp04x6F2XjJ9vo_x5_sG_t49sdgth17Ldl8K3ltJicsaesjxy-qyMO2CRuH9x6TXcvZnudXdeSTSzqtUAJHS6gk_rIucCXuDIlYtNOlVi30CuXKZAUH-ypJofJ_BUH6klLob3ePZ9CR9-tI3hNxm7YzhEGCfiudqxJH227ZZ6EH9UzAi4VgbHcHvgF9WDHq4JD1VFDHuLl1uxjIW9n-jc5NfGE6mp677FVce_L_lv1LGuX3XD0wJ1OYwVstH95XDLrfEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l4sVbIqXaE-_7uMXBCIs6ASaw7NKwbJAYt3pqvzaNp7i4KXQiKy0y67PbyeN5-hhEBr6QsNr5dp6LMriLwEeqCNRkrDMfti_vsmoX7yAZepnWcOSfmM9qwAjfd4kPDfSLgeh0ibDLjx5TlkC4i5ewzWWQXyJ9hbqkID20vt92Bc0RODrutTLGzsJSENvul2WvBjc1Hmh-YzP7umzzKsel4AwUAGUn5mvMwTwI5825FQJPcsY_aFSvrCEnKqOLBeqI-6pzasEGPRNQ1CdNXd_KHhGEG6NMlpE7cFTaaiLwjPPzS7fVRnkvzoo43Zag9BTHm8_NRklp5O8H2xnHNdkNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=blt2RS7GUGCScBrsw6YXHbnLqv1cRy1S1kyqGFQHX7qMpvRI-_czI80C9c2CpyvR-6es5w54xAojeXuvOKUSAUBm1pUQyNxxmepdkj18TyxzdAQqJh4LLFsC3bMjx0GFAUev_MJi7CO-Erx4eRDmGi7b9eae0kPni9BfrSTTTLOnkNPVzDcd_XZRuW5sHRATqaW2HfOP3ZRG_AayDFgeineCp4Gump1-DRSliaFU7NhAhBA7AkyiZAqYXO_M-991SVCn0sXOlkqnTGFyfbC8KfuvA2AE2MU8HUkuosRQ4o6APhv0Z6EEhpF3kAhf4oX9ibd-eADW2nfoWNn28gwC0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=blt2RS7GUGCScBrsw6YXHbnLqv1cRy1S1kyqGFQHX7qMpvRI-_czI80C9c2CpyvR-6es5w54xAojeXuvOKUSAUBm1pUQyNxxmepdkj18TyxzdAQqJh4LLFsC3bMjx0GFAUev_MJi7CO-Erx4eRDmGi7b9eae0kPni9BfrSTTTLOnkNPVzDcd_XZRuW5sHRATqaW2HfOP3ZRG_AayDFgeineCp4Gump1-DRSliaFU7NhAhBA7AkyiZAqYXO_M-991SVCn0sXOlkqnTGFyfbC8KfuvA2AE2MU8HUkuosRQ4o6APhv0Z6EEhpF3kAhf4oX9ibd-eADW2nfoWNn28gwC0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRPHJwbIduejfqaelvxyxW4IAsW5KbbIhX9yU2GblnTSclRBsQCWtTbq8GpiKIrDOkUJT6FnxUZzJCQBF27gHoDq4rXaXpSvc27i4sbR04TYA14nNxBPPb8UC1JmagAO86RVXBcMScfr2WlJ8zMWvFLCebLj6LRLuZkS1txFHJxDy9RgYgbQPMAthMA7iRb_moS1HUuICMKUdsK0MNKM2jirsABngpZWPRHlS1IKSIp5lb_9YUryOE8Hhm8EY6BT0Nf42FWgLeaWRl5_5QgfCjwtasIjyJ1bYJ0GMGeKLhi4T75qojTmIru_7nDF83yD6bD9JMVocTqUh0tvcGB1TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1n9kFhurs3DuPv38X2xGZeMNJ_fmboUGsSZQFtnrjnZE-HF8DGGA8s-5-bapxdRGR8jb-AybSVmaU97lYGxD-NdqdmG2UEQgDabywmTmul0G5IZxvllTJlvHlU8xo3auNlDWvMUSt3JZQgSRejnFHi4DcaH1EBzulgoGZGKBpIVz30ZaBH8cAchwfTvD3_0OZmSvKViuI46xIvvXibavS9kBk-_N85-tkVNpsKrcSHMLl_A8Bbie8HCBvyEny9eQ-fbRyraLdcMz8ywXsgX_C_8cE6rpPenVVDqOwh2n2MMv-MvotCdTKB3gE3sfnHilfC2f01s45DJLj3FX1PVxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=OIagsWDbqqCaGkilrXReVU5_LLI5x-mSiEtfLV8oA8fxBHU6pvX-OssWg8qBkSxfcOewkcEsCy2W0LW_S488eHFZJQSiT6b-PL_nNoi1y2E4zWtovsjicJjfZjR9aADSomtDIGNTNeZnYlRC-qHtzwJxc9CInCx8KE9MZSDoZNd7njMwOBnVk6DvF033WUqxwYk6dFzKZb6q7tSYCL1ZFU6IJrSfobG-NHjVvdqdNfmvfuHRSzt9U9DhUSBbQnl9pZ0_rWqzrTqPz0i4GpxA03QUO96o4Ue2rHqnsnhq2kXQ4rTEVBQIRYmXlGoO_K0RChFSFECZISWl1WJJVMKy6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=OIagsWDbqqCaGkilrXReVU5_LLI5x-mSiEtfLV8oA8fxBHU6pvX-OssWg8qBkSxfcOewkcEsCy2W0LW_S488eHFZJQSiT6b-PL_nNoi1y2E4zWtovsjicJjfZjR9aADSomtDIGNTNeZnYlRC-qHtzwJxc9CInCx8KE9MZSDoZNd7njMwOBnVk6DvF033WUqxwYk6dFzKZb6q7tSYCL1ZFU6IJrSfobG-NHjVvdqdNfmvfuHRSzt9U9DhUSBbQnl9pZ0_rWqzrTqPz0i4GpxA03QUO96o4Ue2rHqnsnhq2kXQ4rTEVBQIRYmXlGoO_K0RChFSFECZISWl1WJJVMKy6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Bbk8JPnD9vCd31woQerzDGiJjx3Vq79i5-lfPHOd_PjZs8_GJY8BuI_irQp4cjOrh44AMqAdjrymUeII2C42p7lh60Df-oBuFTu52MjRBG74Tkinw9EW_42Q78Y6z2feG4uEMUKMJFVx5LDHApX1pu5czHIqx7Ww9wiWOgo39-RqrZ_xnm0-E9v58cg4Ii_oS2yNAJZN60ifi6D5PfJeRbsvLLLCeVRvycRXErtzgbBTWE8kr8pkZWzF94w5EK0QpUGA29u7BKwCpUQsiXN7MvarAPaRZNX-ha-g-YMSJj2ofEmcEgpBD6XYB8_hvjxc2I8-CnALmY-2JDdpc3VqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Bbk8JPnD9vCd31woQerzDGiJjx3Vq79i5-lfPHOd_PjZs8_GJY8BuI_irQp4cjOrh44AMqAdjrymUeII2C42p7lh60Df-oBuFTu52MjRBG74Tkinw9EW_42Q78Y6z2feG4uEMUKMJFVx5LDHApX1pu5czHIqx7Ww9wiWOgo39-RqrZ_xnm0-E9v58cg4Ii_oS2yNAJZN60ifi6D5PfJeRbsvLLLCeVRvycRXErtzgbBTWE8kr8pkZWzF94w5EK0QpUGA29u7BKwCpUQsiXN7MvarAPaRZNX-ha-g-YMSJj2ofEmcEgpBD6XYB8_hvjxc2I8-CnALmY-2JDdpc3VqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUbW3D-YSlF6JSPWx4DJjEfW4fTKQvYXzgahOh8NMBbOYb1AQM-7UGiFTQVY0xC8j0RtCUiAyUoO4C_rGvtHcXJvNpbWAUBSgfAY7iVWCig1ZbFBbuj7YEj4jHG9tey3boHIHq98t5xgWxAwwqP8Y3g-ZudZEqe5zDhI0Q0yWBklx_djpSqZP221RFnRVQQHNFfJG9XAxf-oqakRttczbH5FDRvFPtvk8GxB0nuYhDDFwoysWnC_EODETyVXQ-keV4ITAht_9Uhyyd5CGm92QFxtyfcAeEZaedwUv29Be_hcBSjQzL0vAj-OZgSbHyRC21UHTuXhgbselcQ8ZGO6xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ8nnUyHBKLzh_jgOnvk3uw3R6Qcj4Qq9UaUGCdQAfwLRLxoBYmX_NMTAQ9rWf8vS-epdzgG6RaqJWDQW1uNDOiCUuas0EgvW3QY51GTpi_EchcWQAtbuKwYa2_OSq9OfNiyp0MRXrnpRKyM8yCRtKUaV__GXNY7LvjfnH9hiexYYjQsUJdm94aqn82EnzyMvUHnz6aM7jZHiB9iNfskbjlbIlMXMUPoF5jn0J6iis_-VrtS5VrUSOq5XOpsH9zUhfo9GIhlxMuhexhGLYQaJz1USax3ahKtaHv73Kj0DrLwrWksbcFqdUATpHz1NnDWU4TjQXXEPjYv3Ow8Qog4sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHRqj6N65dxTAZojDDYpntKED_RPSRA4qMcfdnfxxY3sjoymf9B7j6su4vLC_mU9OlpBlKn8KTSQT16Ka-B5m_U1zwnlkEGgzj1pgh1hkifexdnlCSGUX7UQh_VW15aCfbZ5z6oVYe2yG31nBdwaQqNBWU-qDOclY6Fr4Wd_bQyu0XV3M86x5uTHvf6nlUAFQ8QqxotoHMRRHlE4rdd_aQbmYRBrb5vEFfudYWQz1tGPCTITwDQCkPo_gWbWpHq_RqKLo2S6VQO30C8CCtciNJEQm7xglTVf1xi2ZHqEPUqDeFD4ZAyYGHMU5La3Pag6NimYmkIw_EFAyfpJDJTV6Q.jpg" alt="photo" loading="lazy"/></div>
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
