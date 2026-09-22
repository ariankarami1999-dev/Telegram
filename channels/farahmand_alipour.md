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
<img src="https://cdn4.telesco.pe/file/faq5W5V7_Zgni-YoUHNNOmFH_-waiFFQXROGd0eCYCPKbfy7zd-p2tYA9VUvlhor1QsqtdmUzjyIqNegJk3elgNhjRQ8FjQ2K3x-YnjVH0NhmVincRo8RrfDgPOe0XW3L0--RaiSUZNnsvFUerpHsS9zd7Bwwl7A-kPmC7TRs9Py6pnMdA8nuSDfK-jjDX5jNTnYV-cG-RyFalkNkBycX2gHNh53X0XwEg2M5FuxoNXQ7k78a87Ju_llULuuZIfsbLOeN7ltq1PZSOFx709KHDPZX_SZwM5b6YFbHwDshia9QFJleEFAZ8nGX-V2g-NW-nT1cvpofyyFqG8cjAm8UA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 08:42:09</div>
<hr>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOPBe-WsSyKP9b8iFJXu_j5PR_0lIEe2k50pJqHmxjEnlwZ0j94YJGCBG2XZ_m1-E5lIzS-uCEoSAwIqZByjdAtrURxa4361C-j0MHwVOYXc5RHqG5rGl7Nqk58cUP7HiiAmnhLXXhu7jS1wv0McnVMu37vavKH4-rLNI7Y8D81vO04kCcgI_JAejI2Mi2CdGfcTRRRsID6hnDCdvP19ub6N56KEtCwDrDAoeceEfqjYB_EF3YKLkB-FZW5OlDzcmSRzlOveJDK5k_fi52cSTkfDG5YrnnSg0LgXDVg9XtIxKe6YOuSHD_9JrBKpkIrDglDkCtl6QczjuIODYlnyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZEQJuVbcnqNZZHO7UjFbF5c5Wp-hZh70i1mON0nwPJXiyT9kPyasiGoUW0T9g6LNIIN6IHGZfBK19KjIs9n-UBY9DyHOfS7SahknXoobdxk9rAgcUea0wnNeB_--HjjeqccWRSaiKopHyS19n3_qXwB6Kf2CFiqqXo77mT9Fzeh_NUY3p-SFM-2bPYbnSZAERGxRt9l2cu2KPHotFhcEQlnjRwB_SmQGrDMLs4k2IhBJVIIxHbHhEy8dywxrSY9cN8bRk7qIOYN8GwyfWa-HAItdZNbRxnfVacjPfv5K1SK6kgh-GqspnwCMbtCo38bFPtZZCBgwmF2Sy4MsqnXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFGxaknU9gwmCHvWMuzyhciGwoBq3Wvjsi3vsfKtm2K1CmZB17mq1Oj1d8hkI4A-SXDdha--naq-8ctjhw05SJrokXf-QrRUo1-SGSg-oNlcOjLaizuMW_ukRYCU0icWyphiJ8uBmiz4OCkeCp3NI-igJlasLW1Rq8cjbqPSDyev85dYTagLTKZnty8j3U2XHpG-LVLyy_mEdTm94V6RmJpF_0B6iFbqw9i3fkthQ2Ntim_Kbm-_ZFp-rdbqiOp06xSBNNeDqb6JqPloEj4v0852Qxf17plAEj6GOf1U3H6mXfwYcObJrJF-QKuj66SXxyZoSAHItyMnkNRq-OGxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0aywzT_-GzwuS-25mi_0go9TbrYsABFIDLG5_fKZJKw3ldMd2vtzyuR6a1cYEs4HyFKCmu5xkgmWHGm-hBJDPvRVBrri5iB5aO9t4LE5QxgtoP-3ykIltfWQGeDiazeZovAYir7RXhaSogRkAqtMnSBFS-e8paGxP-d2lN-lV-yQrhxXacNBelER5tGXdSIkLdUZKq_Sp_pSQYBzQHcHnto6y8s-ITaXKwQjO2AKvE3cGLYwtx96h-7z4piCDYzOQZ2qQlDuT4N4byUDUvZQTVXLgUGPu2tYKthtaZU8gaXoCbF6Eg4l5GArzaG-2nFYMC_CGRIEvAS7H1Y9RiqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ-g0pjv-VUG5XAGfHuWBpg6xorbcqERyQJ4SyxPFZXWsA-BTA2buxTsX9DRV2BiRT61JS0KRyvbRVNL1A5FDxwmRyIcBhakymAyBQnRezBDnS0mztxwBkXEnIp-UzET80l-3EI_ZVLFu7QH0xHrmp1K57JaST-vorUpdIlKj8Nz-ua5f_nxI1J92HPCngz9pdPDqv2OjniQ4Ng41dx8vcRVNbS364CtsKQK6fD_hVhzgKhdJB565ztPedCiYUtrmHoXlS_yTamwMmZJ_Oya-agbTJI-NWjqcuNzTxSp0Bkd8GclaQS5XeTiSmjA_zrSxjBDEChamBb__nyW-0bIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuwbz_RFNOvdR6WWaTN543Md1P8ugNrOnhR4PHAlV9Wd0L6-raL6tuPY_C3eT_1jRsBeElddnxx3_H1gCjDZjqmcGMupuCPYQxagSh-KCqjTml9tBf5TX1sZT0mnNk4yv1Ca1OkCawIK_zbivV6cN8MGr88QNexQ5nwrv1FlJD_8kZ63yxCWHRvbybBG1pqR1uElrzsQZSqvRAXj7o1MMIeNFJUvgBAbOcXJS9tQBTGsoW5ziCwP7dqtPAuLFY20wdYxR-8J6HB2RCK35YkoQGHgZJOvjg0f5ovg72qEx3Z_vr3bXeLA1XCKi2--nlml-JGEI79CxWS0GEzj4rbqiOFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuwbz_RFNOvdR6WWaTN543Md1P8ugNrOnhR4PHAlV9Wd0L6-raL6tuPY_C3eT_1jRsBeElddnxx3_H1gCjDZjqmcGMupuCPYQxagSh-KCqjTml9tBf5TX1sZT0mnNk4yv1Ca1OkCawIK_zbivV6cN8MGr88QNexQ5nwrv1FlJD_8kZ63yxCWHRvbybBG1pqR1uElrzsQZSqvRAXj7o1MMIeNFJUvgBAbOcXJS9tQBTGsoW5ziCwP7dqtPAuLFY20wdYxR-8J6HB2RCK35YkoQGHgZJOvjg0f5ovg72qEx3Z_vr3bXeLA1XCKi2--nlml-JGEI79CxWS0GEzj4rbqiOFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=HN2CeodEo_snfDFBCSJ5ckgCgHpy5WMb1eJwPVr1xUPW64xUBCo5fnrVneSUX7QkBg4qdk1Lrj21O4tSD18LUj0JGYU-Ir8o5EkQP_Hte3qYE30MOKx87zYw73_J9yliEmuEu5DnrG-1RO6D-gXugbjkHVhCH9oCh9FTehuHzJzh1AOcbjcvsrDOfV8vOs5zlgT-uvsdsBEw11dWK3RC6dE9abB_ghlZdrAvMK8xfKA2698VdqyKcYtnjad_LysQ7wPK7w-1tQvEyyxKkgE-MPE9vPaeJ2jK1ci3b7rog-pFeTaX_QVLTLGqdKPsZ1eEkh1wdm6soVDcoZf7aWFWHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=HN2CeodEo_snfDFBCSJ5ckgCgHpy5WMb1eJwPVr1xUPW64xUBCo5fnrVneSUX7QkBg4qdk1Lrj21O4tSD18LUj0JGYU-Ir8o5EkQP_Hte3qYE30MOKx87zYw73_J9yliEmuEu5DnrG-1RO6D-gXugbjkHVhCH9oCh9FTehuHzJzh1AOcbjcvsrDOfV8vOs5zlgT-uvsdsBEw11dWK3RC6dE9abB_ghlZdrAvMK8xfKA2698VdqyKcYtnjad_LysQ7wPK7w-1tQvEyyxKkgE-MPE9vPaeJ2jK1ci3b7rog-pFeTaX_QVLTLGqdKPsZ1eEkh1wdm6soVDcoZf7aWFWHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=vBubKhW4Ji0I6uqSgiJORn4PF9PlrktPTR4pBwO-AkoPO7tHR9Fvbj1IhGovIHP0ZLzlBmEXzgiMwqAA79Fv0q8glc_KIujxFQPX6ZmCQCN1YyJAl1cwIiqICqLOpdt1KDf1EpV8d8A6btIiO-wdCddoaGvxuKJKjQWaBJb1NAw9Wu-5ij6-0nlGGCVFCGsEDAZKd8FlhNix2E2qYk1b99WCBIyCpmE8y7ABAxXr9-w97_3JjVfZGs4mZMBBk4xa6F3cv1LgNxHhcS4cECQ9PPJvej_oqg1buBDHVMsaPW6oZ4kiqAekil_PlK8Q077ldEqUv3dTpQOQrVJKqnkFISappUycDtWJI6u3E6vR8egNH4Rzb27Sd-YwIdrGWHr2XYDLCDw_BKpqEJq3RItrYhdkh77qZTMDLsbXOkEDoggnMX47V60QN0diAozDjtacJlbBi0oMCHyoSTeVKXtJofAhgvpYmL7hXD2Jxem26vIaFnN0hWpRvrxRyAGjzLDtoN5lUgo-kT7Zc2lBmcOzzLB2PHHKoty33Xjalm8DLd6eG94NjUktSZz7IOK8ejPZE0VERfaeZEXUx3vPGIKJdGmEgABL5DsGvIapNsCFqO_k7DrdqLTaj01XrGcpQAv1MReRJ_Ms_VFFFUycbS9pXXNrIKpzx8qOvxMcqXT0pEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=vBubKhW4Ji0I6uqSgiJORn4PF9PlrktPTR4pBwO-AkoPO7tHR9Fvbj1IhGovIHP0ZLzlBmEXzgiMwqAA79Fv0q8glc_KIujxFQPX6ZmCQCN1YyJAl1cwIiqICqLOpdt1KDf1EpV8d8A6btIiO-wdCddoaGvxuKJKjQWaBJb1NAw9Wu-5ij6-0nlGGCVFCGsEDAZKd8FlhNix2E2qYk1b99WCBIyCpmE8y7ABAxXr9-w97_3JjVfZGs4mZMBBk4xa6F3cv1LgNxHhcS4cECQ9PPJvej_oqg1buBDHVMsaPW6oZ4kiqAekil_PlK8Q077ldEqUv3dTpQOQrVJKqnkFISappUycDtWJI6u3E6vR8egNH4Rzb27Sd-YwIdrGWHr2XYDLCDw_BKpqEJq3RItrYhdkh77qZTMDLsbXOkEDoggnMX47V60QN0diAozDjtacJlbBi0oMCHyoSTeVKXtJofAhgvpYmL7hXD2Jxem26vIaFnN0hWpRvrxRyAGjzLDtoN5lUgo-kT7Zc2lBmcOzzLB2PHHKoty33Xjalm8DLd6eG94NjUktSZz7IOK8ejPZE0VERfaeZEXUx3vPGIKJdGmEgABL5DsGvIapNsCFqO_k7DrdqLTaj01XrGcpQAv1MReRJ_Ms_VFFFUycbS9pXXNrIKpzx8qOvxMcqXT0pEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=bhp7JEEypubL6FWyA-wLfJAv86-4z9Faw-TQWL1KYXrXP1nX5N--l2Sgz192gCx7UNByEJg8e0CH3C2A80x-lLrKuS5N326_IFzxWW0ZYmftKs_j5bRAqrka5qIlKIv8Ox2OnHE4Z06ytaPcO265yh8JzogCF1RHpCy9rY7XG9KW9B8q9fpfmMWCclo6Fj6UYnFnfpzjLwgTd-eda7hbNfTT1y94ul9J3qAOPzIiOQRGJUe-6piWoDwxdy501afBiISmolJQISYyHbq-8IVA0d96iZKdOwA23_A15WPixmOaYL8qmGNDw2WgKdqeQ8DI16L7_n38HfxsZp4yjKkIHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=bhp7JEEypubL6FWyA-wLfJAv86-4z9Faw-TQWL1KYXrXP1nX5N--l2Sgz192gCx7UNByEJg8e0CH3C2A80x-lLrKuS5N326_IFzxWW0ZYmftKs_j5bRAqrka5qIlKIv8Ox2OnHE4Z06ytaPcO265yh8JzogCF1RHpCy9rY7XG9KW9B8q9fpfmMWCclo6Fj6UYnFnfpzjLwgTd-eda7hbNfTT1y94ul9J3qAOPzIiOQRGJUe-6piWoDwxdy501afBiISmolJQISYyHbq-8IVA0d96iZKdOwA23_A15WPixmOaYL8qmGNDw2WgKdqeQ8DI16L7_n38HfxsZp4yjKkIHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqY7vBrCVM-0xlJ213uAHUZj-X_rVq6PD1AI0u04275xdIwH9_CB9-A45voz7DXklCMcT_kQB2ylJ1hDPHckbdS66LJ16aoBW51XrmQUdwYXZAnrsVGtkSCPIfkpEeUHi-659dr_zxC6P1ZuzaTUNVgM17V2b7wYXM4ez0ZKxJsMBmxsl50hpGPiI2736i4LKM8lIsRMMK5XkykG8qXvDL_8Dg7B19ZfgDFu3UPUL7Pzs4KofhOzuQ4GoTJ9Es5PAzCpwtT414rYtc5QwEttYlWRnqK2Zv3Ux8g__0YVNJ1uPXR6W3fFAdu23lfvBvTxn7pq7Juqy-YMWn0felgriA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=IpQS3KN8Ii5GjWFRzZZBCuh3b2dFXB61chz1yKDFnHCE1AKyQea6bCFBuG-EnbwTfD8M9v1J_dWRnp9PLSV9ri5s4lIfYO_8rY-31-yh6UtDLa9lE7r0-UiMwuXZNnMqCxYxs23UllARU872AxReKlnrwvSyXvAR7bRWp4ynqqOoiLNwpTma3HYldWD-QZeFJ9y2SubVODYgRjeoTsefY-UA9fjIIdXJUI7xvPftMUXkNSj91t3FX0O6FdzlZWTU62e7CVinebU_KglpOhtXMe9TBE89oIArNpXz1yfpPPgToJBwokPLtA-0C5R5ZD4uyHwABOTIDvJE7uwbajBLjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=IpQS3KN8Ii5GjWFRzZZBCuh3b2dFXB61chz1yKDFnHCE1AKyQea6bCFBuG-EnbwTfD8M9v1J_dWRnp9PLSV9ri5s4lIfYO_8rY-31-yh6UtDLa9lE7r0-UiMwuXZNnMqCxYxs23UllARU872AxReKlnrwvSyXvAR7bRWp4ynqqOoiLNwpTma3HYldWD-QZeFJ9y2SubVODYgRjeoTsefY-UA9fjIIdXJUI7xvPftMUXkNSj91t3FX0O6FdzlZWTU62e7CVinebU_KglpOhtXMe9TBE89oIArNpXz1yfpPPgToJBwokPLtA-0C5R5ZD4uyHwABOTIDvJE7uwbajBLjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=quFrkaAPWXie5TZcLBwUqdutL4opCsXdWGjOHdEkwG85DQwD4f0paF_CwcpWHY2fmlUCIbyxu2V0t1uGCiBEaTtdulSt0p95bvo2HFPY4velMktlq5pCAb8xtIxIvsI6nR5Rv424JAncLxFQCwD918MA3ip1mBnxhNNuZODZsTRdZwc3s-K_LMpBx2yUVaPXVBQHtM8VsO51kYEVz0GYC-rSFnsEoLlf4ArA6dfzFZmpz4qhtAWWiJ_UL8YrT0sflFo-H72Vscx7wb8od6NxJhsI6BaOzZm9P-94snguVqXzm5WahmS_HeMuQ9v1m1ExhedOk4WLsG0Vd-Pjj5tULj3hFdzKF2qdAvyPtYcIJHZnKMmbiqXmRE76Z9OF_-6Gi2DrYtJEkzb9-WV_Q0Lco32GprpS5P1iF3GgZdemqTzkU5CjMCz0LpIZ03QY41ddgKCTxDqLOOAorn9Ykq1xiaCgyn7T04GnXD3Xxh27pBMFb0TZ_iv-A7VRo46rrKt8DBbyu3bND7Q8dyXHDAxd9jCZBOb9DCUSlZkcb92Q943KCXUd3o19ph-DfXoCciFjB0ttDe8AO4RWOqFNffZeJhP2N43hMBMZ3vL0iBQn3akASnf7TGaO3Cjd1J5A0bDdNvkatLqg4m9iCiWcoewtutShdUCtrVCoP0ckDj3vW4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=quFrkaAPWXie5TZcLBwUqdutL4opCsXdWGjOHdEkwG85DQwD4f0paF_CwcpWHY2fmlUCIbyxu2V0t1uGCiBEaTtdulSt0p95bvo2HFPY4velMktlq5pCAb8xtIxIvsI6nR5Rv424JAncLxFQCwD918MA3ip1mBnxhNNuZODZsTRdZwc3s-K_LMpBx2yUVaPXVBQHtM8VsO51kYEVz0GYC-rSFnsEoLlf4ArA6dfzFZmpz4qhtAWWiJ_UL8YrT0sflFo-H72Vscx7wb8od6NxJhsI6BaOzZm9P-94snguVqXzm5WahmS_HeMuQ9v1m1ExhedOk4WLsG0Vd-Pjj5tULj3hFdzKF2qdAvyPtYcIJHZnKMmbiqXmRE76Z9OF_-6Gi2DrYtJEkzb9-WV_Q0Lco32GprpS5P1iF3GgZdemqTzkU5CjMCz0LpIZ03QY41ddgKCTxDqLOOAorn9Ykq1xiaCgyn7T04GnXD3Xxh27pBMFb0TZ_iv-A7VRo46rrKt8DBbyu3bND7Q8dyXHDAxd9jCZBOb9DCUSlZkcb92Q943KCXUd3o19ph-DfXoCciFjB0ttDe8AO4RWOqFNffZeJhP2N43hMBMZ3vL0iBQn3akASnf7TGaO3Cjd1J5A0bDdNvkatLqg4m9iCiWcoewtutShdUCtrVCoP0ckDj3vW4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=PdqbFKMKkxAzQNxn3r5i8A00AUvly-BglNwcwRzQ6UzYd0w2WWEYSAy-BVNjZH124IMhmXUbBgcFgvehcjXJik4QxsIaiHWO1_FOeyzxYi2UrrSvm2fHeIUG2tjeBat2udm_VYyKxfy7EM0nUdOCs_K8Y12M4IyW8fT9UI5JTzrPERgIRYAitSXH3-W9ifby5FToGs1TqZaWoYcWJObdPQ-y5hT0V0o7tbz54MnGN3S68WLNLH5NvDIclRwXP1eZMNUHrouj5rKYm4ZL0lSO8beBLBLKw4jLvHavVqGNG4wUW_RztnvZ7eBy3ClbBl9oWLYwPKvuHn7CJEOKt5JB3Fcs2zFsk6p2Kk4q3vPEFmlsACu00bcXtLYONZ1Vs0ZLVeDw9hNy7W9wSQRI1bQBieWIA3LRYmEhiBL-tiL8WG4o_sZK_iW8KDTbydf3Loic11zKsX90jHKvMgBUAuEkrYcWmD1Ih_R1J2fbG7F_X7GbpwQ21ms8M_A1NBpnxggBEuOv7JZa1vXj-DFdGS0CTUX0C5J4UqlWDLwZPy78_rJD4FR9y4uoppFQkj4pf3fX4qp81Mr9g9OM-pm7WH5ESNiRB6sounQY8AmzbckGpscueDNSgCaeq4lXdeWyX3wZMM5Ql7lqRKGi0ecy56Cxz8A0Mi3YOM8PisfNKlQLZkU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=PdqbFKMKkxAzQNxn3r5i8A00AUvly-BglNwcwRzQ6UzYd0w2WWEYSAy-BVNjZH124IMhmXUbBgcFgvehcjXJik4QxsIaiHWO1_FOeyzxYi2UrrSvm2fHeIUG2tjeBat2udm_VYyKxfy7EM0nUdOCs_K8Y12M4IyW8fT9UI5JTzrPERgIRYAitSXH3-W9ifby5FToGs1TqZaWoYcWJObdPQ-y5hT0V0o7tbz54MnGN3S68WLNLH5NvDIclRwXP1eZMNUHrouj5rKYm4ZL0lSO8beBLBLKw4jLvHavVqGNG4wUW_RztnvZ7eBy3ClbBl9oWLYwPKvuHn7CJEOKt5JB3Fcs2zFsk6p2Kk4q3vPEFmlsACu00bcXtLYONZ1Vs0ZLVeDw9hNy7W9wSQRI1bQBieWIA3LRYmEhiBL-tiL8WG4o_sZK_iW8KDTbydf3Loic11zKsX90jHKvMgBUAuEkrYcWmD1Ih_R1J2fbG7F_X7GbpwQ21ms8M_A1NBpnxggBEuOv7JZa1vXj-DFdGS0CTUX0C5J4UqlWDLwZPy78_rJD4FR9y4uoppFQkj4pf3fX4qp81Mr9g9OM-pm7WH5ESNiRB6sounQY8AmzbckGpscueDNSgCaeq4lXdeWyX3wZMM5Ql7lqRKGi0ecy56Cxz8A0Mi3YOM8PisfNKlQLZkU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=OGHabQphf9dkbGtQEuWcZCLWumBmEG9Lhdpj-Whp_1nqOjzEVmu9bv4GKHMuhUyYwYu-dDAHaWumM7dZKo4EuGwvZmo8sp8vZscfCJZ3QR_7ZXBuW_KMq2pMxU1z1AakVQzvUW7MTExVHnvFZBQjQ-iS06Fd4c2u7cP0HccJO7Un1FsF4YfgW8hy4S7y6--XJgf2OEfpuEkQDhn84LtArL6dink_zkAwCnKns3Jjb-t5LN_XIL-dJ16KIJtEFebx15KrpSdoxZJMMQVL230HhVJpO_Q2Y4-SnLWcE9uaDFDC42ZjJoLjVckUr_jSyxj3uvia9lMHZcGYCoakdJGb-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=OGHabQphf9dkbGtQEuWcZCLWumBmEG9Lhdpj-Whp_1nqOjzEVmu9bv4GKHMuhUyYwYu-dDAHaWumM7dZKo4EuGwvZmo8sp8vZscfCJZ3QR_7ZXBuW_KMq2pMxU1z1AakVQzvUW7MTExVHnvFZBQjQ-iS06Fd4c2u7cP0HccJO7Un1FsF4YfgW8hy4S7y6--XJgf2OEfpuEkQDhn84LtArL6dink_zkAwCnKns3Jjb-t5LN_XIL-dJ16KIJtEFebx15KrpSdoxZJMMQVL230HhVJpO_Q2Y4-SnLWcE9uaDFDC42ZjJoLjVckUr_jSyxj3uvia9lMHZcGYCoakdJGb-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=II2PoECN5ofwfSPW7BrMXCFZKZvb5hQDAfoe4ZN33kTjG7k_PkEbRVd0nq0GsH2kuiTg5shAP4FSOObpx9swldqIyqT1n_QxE7GBRnKg0BzJp8-aV3WSGvkN0uBe3qHpngWelhPQ-993Zy9FHpQPBlfZsFit_Ik_bNWZPEKDTmWqA53st1R-L_2WIZTcj2Sbz0GFIR3yGxBMj8lLxMJJL8uC9sbDKt_GBNulMafaFyhjB0v9q5URFp7gKtbzMA9Y63a9P6FPJQzTqhN44QXSfXAo91Z28GW00ZuUelu7MdRJl-LZTXM7ME1vorhCLo1Q2XWjqDYcaadO1KX-RYJRGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=II2PoECN5ofwfSPW7BrMXCFZKZvb5hQDAfoe4ZN33kTjG7k_PkEbRVd0nq0GsH2kuiTg5shAP4FSOObpx9swldqIyqT1n_QxE7GBRnKg0BzJp8-aV3WSGvkN0uBe3qHpngWelhPQ-993Zy9FHpQPBlfZsFit_Ik_bNWZPEKDTmWqA53st1R-L_2WIZTcj2Sbz0GFIR3yGxBMj8lLxMJJL8uC9sbDKt_GBNulMafaFyhjB0v9q5URFp7gKtbzMA9Y63a9P6FPJQzTqhN44QXSfXAo91Z28GW00ZuUelu7MdRJl-LZTXM7ME1vorhCLo1Q2XWjqDYcaadO1KX-RYJRGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=AR0FVD5P1uKMmzWeozVnsH8bAPLMVhE_XIG66gYYOIm2yOGgv54xXg0qS0f_UnW2NOWKhYKgrjoiyjZdfOA98RE4fkSADQB0LH0OFVW2xTtDI5A4D1dj4NNsxM8UpcRIq__vG63tpyH0aKOpL4Q0THJmu81ah_Ywrm9We4WXGSIjkIwmcmuFWEJVvyURcoBjFyXxoGfIowPifo7Dp0codD-of87C2k9hI753d9A-EZgXK6JEpw3XSHxl41UQCLbWbZRM90-tJi8yQIMolnUflU7UG7gIkhtj3IHChOQ7EzXAOUutfWP_sXjY4mBQJA-cPDHNKO1EdBBnoRs86gO64g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=AR0FVD5P1uKMmzWeozVnsH8bAPLMVhE_XIG66gYYOIm2yOGgv54xXg0qS0f_UnW2NOWKhYKgrjoiyjZdfOA98RE4fkSADQB0LH0OFVW2xTtDI5A4D1dj4NNsxM8UpcRIq__vG63tpyH0aKOpL4Q0THJmu81ah_Ywrm9We4WXGSIjkIwmcmuFWEJVvyURcoBjFyXxoGfIowPifo7Dp0codD-of87C2k9hI753d9A-EZgXK6JEpw3XSHxl41UQCLbWbZRM90-tJi8yQIMolnUflU7UG7gIkhtj3IHChOQ7EzXAOUutfWP_sXjY4mBQJA-cPDHNKO1EdBBnoRs86gO64g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=DRlYV9Mhn7xu795qteuz4oZwNphf17nhYG60ahcBVmrkInzzqH_BicLZsAgTZeQ2T_JOQfOg55iTQwCnFIaQrpth4YW00FRMhuJ4j-9lzPXPWKjwrhNpEOFw1NmlMbAsXSRhEeHvUNhLSS5NRUVq_-AoK9_BdeI6efez8RMMGw-4-c2ywKEbFbscpfuZYEkksNNZJJub8CUlFUO08LchunDmrav-CNNHiwl8TqPxU_8v8hoFuWp9jYr9mK2kl5ZQ8ObI20LWPBpfHxIcx4dC2eQKlh21v-cF9qaxsgRshjrQtDkc-DH7QjRfdNfb8fv55Wl5ZetHyCZsGM2lIUSFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=DRlYV9Mhn7xu795qteuz4oZwNphf17nhYG60ahcBVmrkInzzqH_BicLZsAgTZeQ2T_JOQfOg55iTQwCnFIaQrpth4YW00FRMhuJ4j-9lzPXPWKjwrhNpEOFw1NmlMbAsXSRhEeHvUNhLSS5NRUVq_-AoK9_BdeI6efez8RMMGw-4-c2ywKEbFbscpfuZYEkksNNZJJub8CUlFUO08LchunDmrav-CNNHiwl8TqPxU_8v8hoFuWp9jYr9mK2kl5ZQ8ObI20LWPBpfHxIcx4dC2eQKlh21v-cF9qaxsgRshjrQtDkc-DH7QjRfdNfb8fv55Wl5ZetHyCZsGM2lIUSFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=IRroVkWWiHHn_so3tK3DV41GRFlT2m1BfyzugnRKzQulXFtplTGe8Wk1HHe8-ZyItCIn1ho_s5DDL8Kidea_PdDgqgO4DFCAaOkOq_4PzvzmaW4cUeLkGF6Zef2DhaSgCzNcPCBJ4wDESyTBTU86c48zuvDI-lZZgUg5st_iUKwV5Lt7fy8PS-7m8KPi-eYk0kXmr-7R_I17TIGARCLkF8eIiGX4J0UHY7W2bHeqKU7NVVOGv_sRichDJ42b8WQEfPsOktO-RkNzbYrNaZcNZPqfStWf7sdXym2Go1_cXjWeVp1RR_QhPLki4tRMXZujiO6QWHx3Gbw2IXbClf4jBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=IRroVkWWiHHn_so3tK3DV41GRFlT2m1BfyzugnRKzQulXFtplTGe8Wk1HHe8-ZyItCIn1ho_s5DDL8Kidea_PdDgqgO4DFCAaOkOq_4PzvzmaW4cUeLkGF6Zef2DhaSgCzNcPCBJ4wDESyTBTU86c48zuvDI-lZZgUg5st_iUKwV5Lt7fy8PS-7m8KPi-eYk0kXmr-7R_I17TIGARCLkF8eIiGX4J0UHY7W2bHeqKU7NVVOGv_sRichDJ42b8WQEfPsOktO-RkNzbYrNaZcNZPqfStWf7sdXym2Go1_cXjWeVp1RR_QhPLki4tRMXZujiO6QWHx3Gbw2IXbClf4jBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=W5sRMlA_5Ix_YVJheSOSd0h7kkzQHFccJhXvBaH6K-8O1_aTjXp5QFZ70KxX7bt4t61b1fydGk0hrxtALXEdB2UMKk27jSug0RLeWxE7AfM3Cale0ywJ6se1PqjEiXYVMZBqVzHvsQoNIKKykxrlLGn7mypXK3PXaMxWcxYhl15nTnz6V1lTFDvjsyRUtWfTkVt_0pe82sXXQPzi1XCXe2VnyaDsxR5955JdfcKgg_kF0kn2eCXfNM_7Nc4BIt_KInx25cotPIZyAxp9AlM3gOzJZ7cWvgeOVj9THDP5amS0UR07Nrp2oDLmg331Dn5gjWVS48juBo25HHk7-Zg0xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=W5sRMlA_5Ix_YVJheSOSd0h7kkzQHFccJhXvBaH6K-8O1_aTjXp5QFZ70KxX7bt4t61b1fydGk0hrxtALXEdB2UMKk27jSug0RLeWxE7AfM3Cale0ywJ6se1PqjEiXYVMZBqVzHvsQoNIKKykxrlLGn7mypXK3PXaMxWcxYhl15nTnz6V1lTFDvjsyRUtWfTkVt_0pe82sXXQPzi1XCXe2VnyaDsxR5955JdfcKgg_kF0kn2eCXfNM_7Nc4BIt_KInx25cotPIZyAxp9AlM3gOzJZ7cWvgeOVj9THDP5amS0UR07Nrp2oDLmg331Dn5gjWVS48juBo25HHk7-Zg0xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=exD2gC3p5b1SEbZFCeSAQLT6tqW6NaxQ2J-9KJRZNshXGsfhIxKfhU76ifNCXwTF7Uv2ACY2cDrza6daOwRQ11M_4vH85lWyKNev8SPNooYLbZE4VtBDY92bukE_3rAtmFHQVrKYmi_064kJylsBEkOfK_fsdRF2o6pBavCfP9Ex1SIq9Hffnazp88OcAlr-EDm7D24_c3g1zJPgmvc1esvLXURdpjMzIwgTWbCa3DZytfCgiSALc6NUIqYEaNSvY-hg6hfST0ZoEGl5M2w-nIBb8F-XfTuKijnYZy9skG6MFflq0sG7DSHQ0c9mZ0pnjowVSLCa_u7cpgTTxPqKpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=exD2gC3p5b1SEbZFCeSAQLT6tqW6NaxQ2J-9KJRZNshXGsfhIxKfhU76ifNCXwTF7Uv2ACY2cDrza6daOwRQ11M_4vH85lWyKNev8SPNooYLbZE4VtBDY92bukE_3rAtmFHQVrKYmi_064kJylsBEkOfK_fsdRF2o6pBavCfP9Ex1SIq9Hffnazp88OcAlr-EDm7D24_c3g1zJPgmvc1esvLXURdpjMzIwgTWbCa3DZytfCgiSALc6NUIqYEaNSvY-hg6hfST0ZoEGl5M2w-nIBb8F-XfTuKijnYZy9skG6MFflq0sG7DSHQ0c9mZ0pnjowVSLCa_u7cpgTTxPqKpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=M0nOJM_HW_d0MlDLIuxW6skRy5lUAfyBpm1jP40RqwQY2hpS_Sgr5E9D_W1aRqu2Wlk3LPZOum-O2O7GdN28BEr-aCsb0KiRZ8yFhngKxUla3uUvorW2MYqQ-rb84UC43cXXNoSd_TnF-1KAur7f8YVDme1yvTLxGKI1nn3GMucZbpDiiZ98hZ8B-AJ88nNZ2Rw0CXoUktDrrXyU8T-Ly3dcRgh3WZxZfLzFtU6FE6H3EVih2xKpx8HHNkvqzk-lQ3DJNEXbgmna6hCvzh0IVO_tp7Wjd7wL2sg041pAX9XsytnOfcnHVoouRiLb0c7Bc6a348W0yestEmdco4V4QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=M0nOJM_HW_d0MlDLIuxW6skRy5lUAfyBpm1jP40RqwQY2hpS_Sgr5E9D_W1aRqu2Wlk3LPZOum-O2O7GdN28BEr-aCsb0KiRZ8yFhngKxUla3uUvorW2MYqQ-rb84UC43cXXNoSd_TnF-1KAur7f8YVDme1yvTLxGKI1nn3GMucZbpDiiZ98hZ8B-AJ88nNZ2Rw0CXoUktDrrXyU8T-Ly3dcRgh3WZxZfLzFtU6FE6H3EVih2xKpx8HHNkvqzk-lQ3DJNEXbgmna6hCvzh0IVO_tp7Wjd7wL2sg041pAX9XsytnOfcnHVoouRiLb0c7Bc6a348W0yestEmdco4V4QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=JeBoxBkWt4DMZyJLm5TNAysrzKuSCAZhS3PPgdbArlBBujuKXF8avGkR4A84W6rkLY6uZTKXuiouyMeh3HJUNtkiIZqy_OHZnhCQE87SEGt1mWWpEOnaE4zX34DGBv-1zQiifbHsIdXXFkusmHSFtG4K7DejUqzR6xynWbfCPXNwdqgA5a7N359RRR_ImT4wB9EUg-mSD6LCo9By2RIgvGRQ20ya6f5GEyy2Gc2676z1RgTqAO78vTkXSS2iZe6_cRmHFqq0R3Fhm9A_h7Vf9PyFp34o5QXf7wGLfgqbGTvux6fbPCtOu863XZuNaTVF9flOt2UjnvqbZOdfMzN48w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=JeBoxBkWt4DMZyJLm5TNAysrzKuSCAZhS3PPgdbArlBBujuKXF8avGkR4A84W6rkLY6uZTKXuiouyMeh3HJUNtkiIZqy_OHZnhCQE87SEGt1mWWpEOnaE4zX34DGBv-1zQiifbHsIdXXFkusmHSFtG4K7DejUqzR6xynWbfCPXNwdqgA5a7N359RRR_ImT4wB9EUg-mSD6LCo9By2RIgvGRQ20ya6f5GEyy2Gc2676z1RgTqAO78vTkXSS2iZe6_cRmHFqq0R3Fhm9A_h7Vf9PyFp34o5QXf7wGLfgqbGTvux6fbPCtOu863XZuNaTVF9flOt2UjnvqbZOdfMzN48w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSq7DI8GamBJPpSqtXMTyaShpr1Dj9KIlRbagm_Jb-gBdt7b7n56UnVjtnymOYfXElCQ7sW7SQFKb7dYwQhXH20OCv1Jsr73E2NShvNAgJm6DXjMHBerGjxzrhWFuWt8zu5c-x05s55LsZ3pE_mjKHH0P70DHkqj-FL1AOCBgTIVLQBp3QuHUn0vm7ZMwdGI1ydjwg_mIUMEYdSryFN24l-H2JkEhz6PRYmk0SGJGvFfR4nAVHcQj5kfZ4JsSlJm8glAZG4DIzDosUkd3zTuTC9xL77ZM9YEM9sNwoWthorwnVQGswvG6vuTj0wAkrmatUTBQ0f0a5M1yo1DqR61uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=XJmEo2F77QlfsUQQ4lkMGDFL2jW4Z3Kdm_owi3TJZEFJn3gTQIqSzYOPnRPdT52oJC-zCv55dvDHmMYSxcGQNOrvIy40GJrjbLOOxwxSHcv1VZezXzo-NJ5y7cvTB02DSIjM4rJnCrtVaGWi_sbL6NiTSs_lCHUWaoupRgICS_HVO7u5j6VPJ8K_47gT1Ljv92wnOBIZEJNBJGbL_po2-KJ3KyIWgDU-NZjnxhzrdWky0NN15S-w5jk6ADCpQE_WMNzNibE60eAihiwbCdCWLBRyqX8LKx9qO3ivwKaRtZzcpH03xH05YMfkw3PB5T-HTSIPM-r2lneo7KHVcVdTkYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=XJmEo2F77QlfsUQQ4lkMGDFL2jW4Z3Kdm_owi3TJZEFJn3gTQIqSzYOPnRPdT52oJC-zCv55dvDHmMYSxcGQNOrvIy40GJrjbLOOxwxSHcv1VZezXzo-NJ5y7cvTB02DSIjM4rJnCrtVaGWi_sbL6NiTSs_lCHUWaoupRgICS_HVO7u5j6VPJ8K_47gT1Ljv92wnOBIZEJNBJGbL_po2-KJ3KyIWgDU-NZjnxhzrdWky0NN15S-w5jk6ADCpQE_WMNzNibE60eAihiwbCdCWLBRyqX8LKx9qO3ivwKaRtZzcpH03xH05YMfkw3PB5T-HTSIPM-r2lneo7KHVcVdTkYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=iUpsSRXSpFUeuiRSi4MwvQNOjs8TdoJcqcNeXh577jzRy9pHyYhDz5dFJPPbZCZi_sqrnZQOhamZT4sFri5H3zdbd39fw14VvRs4U4j2QtYAAT-CNPX4M6ZOaJts0ZfxliPWiC1HxTP97OXgk2ZwSzJxpdrkLz2C-4px0THsRK_4qbUmOjm5oSKbizjjFhDUkJQccztE6WSNzbxYhVdaYv2A_bKOj5QJCb40V91kcWNZ2dkUMbAU3mpcDmIK2Vvtf2PGdg1wtwHnuH6NEzuEwG1kvXbXuphyNBzWRHT4_j9oT4k5MBmY3G81YySwtaitmxiXnp26zGySJef4WZShQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=iUpsSRXSpFUeuiRSi4MwvQNOjs8TdoJcqcNeXh577jzRy9pHyYhDz5dFJPPbZCZi_sqrnZQOhamZT4sFri5H3zdbd39fw14VvRs4U4j2QtYAAT-CNPX4M6ZOaJts0ZfxliPWiC1HxTP97OXgk2ZwSzJxpdrkLz2C-4px0THsRK_4qbUmOjm5oSKbizjjFhDUkJQccztE6WSNzbxYhVdaYv2A_bKOj5QJCb40V91kcWNZ2dkUMbAU3mpcDmIK2Vvtf2PGdg1wtwHnuH6NEzuEwG1kvXbXuphyNBzWRHT4_j9oT4k5MBmY3G81YySwtaitmxiXnp26zGySJef4WZShQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ncOou-ZuQv7Qqf2UpEVkfhErvzlqel1b9_Atu9hXSgcY3oPA9Pw_wqYuONbDZlCx8Dhxsf055SJuQ0GGf58Ckd0dTjR9hP1FSca9_6Bx7PvBwekOFPppK2pRLIZi7N4FXiexTOvQ7hIFkLw_Od1J_bdqSbZS6Xee5IdWiJQx5JShotCFe9mvTvhU5J73P3Nvt8-bstMTnqnJdfuV-qV2hnXXqQ0GqpbU1CgH2SUqzQgnLx5iie3DLdBMXZbcOLJ0NPxRv2oWQoFyd2UkD6QHeLUlTRvKsmKv6yKJod5ZZjTP19vjCvMset3ZOkbg8DGh7CPM2Tp8cvJFmAtiL_IvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IgB1HGIk4Ngqgar_COddhaNSfXzCCoa-6O9WqhdOqlMmiHW3xj-zMRnpzMiCzVjbxFNJ9wIYPxE6woxRACM29M-3iBgNQdQJnnFjPypNKl4ciRWhSFP-mexIWxTmqWcd6R4TDK5aUpsTv3Lq3MbYG8zKqy3NStwB_We7hpylA62LdiaY1e-ZMwL6LCRA-sR7kFV-gw-Z4aqQ_sEJ_kgOgcn_LdJP9tg-wnnquPr61CDNgVj4RXsGyLg_pDIC7nCqt5nLtB0deiGBs6LRFW3jQXhmKBHnhBmMh4RYAncjpX4osUf7_b3c0IYw9GUCZrjmpPnroB8SUBWGYQ_-Wg-AuQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=U7ZHE6CboT6OLC5daZVWdHTJCRgq6YXs8fdmO03SezdoGEi02DLbwpPe09_LER6tHKoIAZYq_P4_9Kyt7BKgU9G9CvT1GfG92dnHYVx9RNgqgVAv-IWGW8vbIkC-Vy9oAjsqz0vHGX_U89pEMayQNVv1g3Lbzt7Ib1AG3nY4kS2SYmslWc0f4F3eBZ9riVwNPabMFwrPl7NRh57RmkTlGqu7Z3pEGiwm6WcYqxLTwlwIsoSux_jGrnWOqv3JeQSNnEwSIfuAGK1zvWty7CbfNGHKj88lxpUswE9ezr0NoxGkWfmlZ0vgOgYKY01bYIagJYqBSiB-eZVpLdAONNz4Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=U7ZHE6CboT6OLC5daZVWdHTJCRgq6YXs8fdmO03SezdoGEi02DLbwpPe09_LER6tHKoIAZYq_P4_9Kyt7BKgU9G9CvT1GfG92dnHYVx9RNgqgVAv-IWGW8vbIkC-Vy9oAjsqz0vHGX_U89pEMayQNVv1g3Lbzt7Ib1AG3nY4kS2SYmslWc0f4F3eBZ9riVwNPabMFwrPl7NRh57RmkTlGqu7Z3pEGiwm6WcYqxLTwlwIsoSux_jGrnWOqv3JeQSNnEwSIfuAGK1zvWty7CbfNGHKj88lxpUswE9ezr0NoxGkWfmlZ0vgOgYKY01bYIagJYqBSiB-eZVpLdAONNz4Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxQ_i7v1buqkAHBSVSo4lXCO4OIZGqGV1sakLXWsDrk2UEtCZwnbSzzLd_woxP3tUk2Pyrhct2EVpVlS57eWGeBHi5OUjjolpeHKRLgi8Le7K3gdYoG67rFoRF4Gd8rKezWDCLQLlvjPHElaHdX_0zxdMCQnzxOrH3Idkh0hesMRCBZAcaLsEen975gJ6iVQ8cz4O76FPLHIwhOwnUgGu8UGMdZhQXOFjYZZ5s0-YtQcixdfTomfja_xFmGjm7HiTfUF3JSdI6pgEfgeWQcvARYPz3A-6AP82xcf4XbFGhrxUrInQ1pG8XwxMXUxYN1VavzJY2Kg4lkT01-JrwJ1wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0LE1GVMyMBFgQFCOink601hO_UyxnLgjooZLDwK6EA2q9--TvcTPas_JamHgPEuZFz-Czk9L0uEEGAP9TgPbEFv5Qp0n6qZ8fUc68WtqxFMOBnFy69fKAFwFsNJt_K3FLphQrZJHOgNGi1qb016_UahqZQhVN3fZbI4GmhzF7rdB_UUTAyTE6aGeRI2LLJASqwykjiT0_hqZ29MMBicMjjiZCXnFOHd8cMm7VfUGQqOrCeW_VDqfTUhfCTzFx_DDB1ts_bQ08yKrj7F_pbcYENcIiASXlfHN64BNlO0w-o-Jn1KCaNP2LNZU9Kn-_LYmUZV4BdWbJ6wfPyTul303A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vn7fHc3wJhKQvImqmzvZi3l4UMzEwb4Rd6cSGNspjt7QWky-WAS5RjTHNRLiOU1nQdKpCs1IMH8EfcFx1MMv2_-0vHfdJLnRxWbwSpt5kae6t9-pRIV-drNjwyjN5o2bMeC4gpoSefUoSVKOMyrRO8EkbatJQD3M4L9CuzAvSB5XeehmS6ZJXJEflAuOHK8HrfKodpHCpt1zN43xn8FhbzMpTheNkz7dxSHqVRR-eWYe3vYmma-cAevDrGfEbOrkV0qBqqoV6XSR6S-QkvSWOaBddTpbp-5s89MxkFKLX3YbEtBsyN91fGtjAXLaZZYGtbwSF3jSERvR_0ht3WW1wg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=JQlZ2V6bW68tuCR0tl6wgF10hgGyHEJt9wp2AqqlVv0rpfQpKNafn5xBkOcvifVkyvRlnMfPjYWAUrpcupZ52ZADyTyIQ5lrwbOSRXUaABGWWUV47Kbn35um-Hi_jbSymxDrbtXpYl-5kGjlmVAU14s4BGU3jpEGm32Xj27JWFZbW-WH82bnUsaZsjFqz33nwTbLwOZ8ZA3nzOvKv-KF1N0Zn8H2C_-cedvJ8-bCNdWzWFCZCuoIN8cNM6aMi22YAYyUpc-YOzYrg6LI0xtpWn4nw0dBtbZ0hgHkfEX4IyYB2XRczMSYUAZi7IFX8yO5jtbTHsub17YsPwde7YlsqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=JQlZ2V6bW68tuCR0tl6wgF10hgGyHEJt9wp2AqqlVv0rpfQpKNafn5xBkOcvifVkyvRlnMfPjYWAUrpcupZ52ZADyTyIQ5lrwbOSRXUaABGWWUV47Kbn35um-Hi_jbSymxDrbtXpYl-5kGjlmVAU14s4BGU3jpEGm32Xj27JWFZbW-WH82bnUsaZsjFqz33nwTbLwOZ8ZA3nzOvKv-KF1N0Zn8H2C_-cedvJ8-bCNdWzWFCZCuoIN8cNM6aMi22YAYyUpc-YOzYrg6LI0xtpWn4nw0dBtbZ0hgHkfEX4IyYB2XRczMSYUAZi7IFX8yO5jtbTHsub17YsPwde7YlsqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=aRztF67MYs1ZcruzO6G7bjYtZrvMMK1vO1KVjXGjPWhgDYPoOKVvXwuj2gWjleFXKb-KQfKM7G6bZY7xJ5HvYAY5valsbZpNhL_p2HDZvUbarSYfkdN_C18iX-6d-AirDnelmp7ES8_QAXMWcR7sfZoG1WjLEzKUNzqG1bzVJCkEicy4dTGKLnfIfE8dqlQj8Jt1oOcxKS1AUqMRFcDKr4eGrl6Ap9nBTrFd5Wyowu5TeSincnkf3J6N8Pbn6Wl9k4DElWhgsAkGC2mxDUI2OrgAHtZRb66zqdxPWJgrNI2smz2ibDg2j7In3N7dVBH9UWQaRi6fjSPB8g8Im7wy0hUMjgzP0PZVvytIkG_3AkgYiZl3ntQnZrWN5EmxtkPJuakTr9nnlCbgPug489hGU69ajW9pFiGJKqzFgQNqYUgOTe58KOvXoWZ9FtoLb9tkO-Y3iugMacPaefN2R7GuoeOuHl2R5makZ8zsWqQSzf__jatzWUDcmbVidPsFr_zH9Im1gBwdS2hEcYyJdO7nnKcGmdRzZlGt9RTykOhjnIg1-5fyi2HzKj4S8_wgZw2li_rBA63-58QohSyGjRKErQeOnhW3k1b2jMkbRx6vtibyqzKOwV5e8HFkC2J8_qm5_OLkC4zMj0Ruq7r4LoRckl_qrLqutOuMtojWZy3IOZc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=aRztF67MYs1ZcruzO6G7bjYtZrvMMK1vO1KVjXGjPWhgDYPoOKVvXwuj2gWjleFXKb-KQfKM7G6bZY7xJ5HvYAY5valsbZpNhL_p2HDZvUbarSYfkdN_C18iX-6d-AirDnelmp7ES8_QAXMWcR7sfZoG1WjLEzKUNzqG1bzVJCkEicy4dTGKLnfIfE8dqlQj8Jt1oOcxKS1AUqMRFcDKr4eGrl6Ap9nBTrFd5Wyowu5TeSincnkf3J6N8Pbn6Wl9k4DElWhgsAkGC2mxDUI2OrgAHtZRb66zqdxPWJgrNI2smz2ibDg2j7In3N7dVBH9UWQaRi6fjSPB8g8Im7wy0hUMjgzP0PZVvytIkG_3AkgYiZl3ntQnZrWN5EmxtkPJuakTr9nnlCbgPug489hGU69ajW9pFiGJKqzFgQNqYUgOTe58KOvXoWZ9FtoLb9tkO-Y3iugMacPaefN2R7GuoeOuHl2R5makZ8zsWqQSzf__jatzWUDcmbVidPsFr_zH9Im1gBwdS2hEcYyJdO7nnKcGmdRzZlGt9RTykOhjnIg1-5fyi2HzKj4S8_wgZw2li_rBA63-58QohSyGjRKErQeOnhW3k1b2jMkbRx6vtibyqzKOwV5e8HFkC2J8_qm5_OLkC4zMj0Ruq7r4LoRckl_qrLqutOuMtojWZy3IOZc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ldpAsg7-jZk5M3SlWf9QmwwmZ7GlS83aCyBB6enM1N3o5TnmxFa9F-Jb6jKY3OzhASYcZUuQREC-3gRbGQQwj5ZOgt0xwyamU7BLPUqxoxJwb9D-EaYRfQxCjAxm3jjqq0dmbB-6dPtUjaO3fenU-dz6I2UdKdFB5QEKpd-vhCwzdXKlEH5HBOK9jg21U-5euZs6saR49s6H4_139m8_HOeo5qL8VfX4r8QRmg8CH_AhQ3bJw2bXGr6Hkuc6nV2CXuvFIorLbsfjKLYs0X4KOmxKGGYEJ9TuGs8XFzuTtLpSaOYGfGIhmCHoYEgulNaCIq_UnHwEgVGiNn0ch9aZ5lycjz2F3uy5dJXAIU_h9chtDaBZyQBFnu71QifKreHJ4GoJJ1p9aHeZqEj6_xj9L6R9xaX3RPMwOZbGDLoBYoQ7280flBQ75vrE51wi_JVofjvSBO_1NxwfDrrH6Ue7BctGgl4dfU0hFWIvub5yy3vpmqBS4oNWuBfEq9EX9xAgzQJSOMgFewkigUMxHHhMHPmA0Ec4VJm7QCFXbwXXy1o7xZ-1vQ4b7ZX8NdkHZZLIVuL_mfQb6AC9db7VY5DWTQHfJrSsW7d53JV64fIVhvscK5yZMDUehUDAdKB5OHI_HOu0j6lFoo-9Chg7o2Z8CkA4O-XwdXkfBjw4BQ-vc1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ldpAsg7-jZk5M3SlWf9QmwwmZ7GlS83aCyBB6enM1N3o5TnmxFa9F-Jb6jKY3OzhASYcZUuQREC-3gRbGQQwj5ZOgt0xwyamU7BLPUqxoxJwb9D-EaYRfQxCjAxm3jjqq0dmbB-6dPtUjaO3fenU-dz6I2UdKdFB5QEKpd-vhCwzdXKlEH5HBOK9jg21U-5euZs6saR49s6H4_139m8_HOeo5qL8VfX4r8QRmg8CH_AhQ3bJw2bXGr6Hkuc6nV2CXuvFIorLbsfjKLYs0X4KOmxKGGYEJ9TuGs8XFzuTtLpSaOYGfGIhmCHoYEgulNaCIq_UnHwEgVGiNn0ch9aZ5lycjz2F3uy5dJXAIU_h9chtDaBZyQBFnu71QifKreHJ4GoJJ1p9aHeZqEj6_xj9L6R9xaX3RPMwOZbGDLoBYoQ7280flBQ75vrE51wi_JVofjvSBO_1NxwfDrrH6Ue7BctGgl4dfU0hFWIvub5yy3vpmqBS4oNWuBfEq9EX9xAgzQJSOMgFewkigUMxHHhMHPmA0Ec4VJm7QCFXbwXXy1o7xZ-1vQ4b7ZX8NdkHZZLIVuL_mfQb6AC9db7VY5DWTQHfJrSsW7d53JV64fIVhvscK5yZMDUehUDAdKB5OHI_HOu0j6lFoo-9Chg7o2Z8CkA4O-XwdXkfBjw4BQ-vc1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm-k2XVktyQ2crG41z8W4rc1M1Eop9AlS7ciAuOmeRuYbktkjm2R5V6ftk46mjtfEQz-YTBYhzUZ3JVRCKCuWHgsr6FoQpamFBWNfFazjYOFp8cnAbAJjPkVMlX-cGP0d3_tkrgSRfADD1SPKXi1KakATz_IaM4DAA1QcbhrqdS0XBUCXFIUlKog76SDCA5Yevnvs3itwd024CkkL7AJuvXmUu3g8Fb-see7z_uFPz0KtdYtUsurHCp8-YXQoQcUsRhAEQJO6oP0Q7Ju-FuWdCtUO6TYiGnZs3VarnDDHV-hwoqu2ql3V-P-2mL4o-cYtfsKJVg42cSIbST8XpTxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=pL8LpaGw28GQ2w1sM27iy8z4SSPMjv6sFNXMqX1Rrri5CnDzJEKx0DoBUCjSSEmy-MXRiRfBjPpqHrFSm22EiH7yYZyqIiBjUmQPHX9sVadxRzfyGvMDhtZdsc9eRxw5ZS4nSUYIxNpp9EkZdZWdZ8C2ORhgPXA59GGbtEMclFGddvWpzlzU_PnJETEStFIYv8JTcpbym-NkawfO-EeUfY4SLCZ1aKdPseqjbDuZgb_0K39wBmKbC1ErFmGX76QDUkeHlh_WB8dJYCjMzVXLEx8h9nXxSKFQ8wLNZvNGruXS09DTTCZvk8nBaROtRTuyrjAvmm9ku2AF1rbEPMRSoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=pL8LpaGw28GQ2w1sM27iy8z4SSPMjv6sFNXMqX1Rrri5CnDzJEKx0DoBUCjSSEmy-MXRiRfBjPpqHrFSm22EiH7yYZyqIiBjUmQPHX9sVadxRzfyGvMDhtZdsc9eRxw5ZS4nSUYIxNpp9EkZdZWdZ8C2ORhgPXA59GGbtEMclFGddvWpzlzU_PnJETEStFIYv8JTcpbym-NkawfO-EeUfY4SLCZ1aKdPseqjbDuZgb_0K39wBmKbC1ErFmGX76QDUkeHlh_WB8dJYCjMzVXLEx8h9nXxSKFQ8wLNZvNGruXS09DTTCZvk8nBaROtRTuyrjAvmm9ku2AF1rbEPMRSoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=k_fyPM52qwQwN_1Q48rsq0MwdCU_8tdaJiIPwv1sm0MZHMSb0KNRivxNQAEhT3SUMVoKrsD2a4pl72eH331JuDpK-2WS_Jga7ZBGVGSmaQfkYemrXutA_o1oZgUI_8P36p7tXs8eIshkfW2-KsMQqwhSu6gCufpnjvjqzU66Xe_0JJpIpJYDUfhVydLa1erXoYqG70g6bWNWCc_eji7bumlIp2mfKc9hB62p6IhBHhcYM5IlYnrc3C7yfrX5nIbYSE7bXSMuHAfWcP0YttxNdqxtnuV4u_x-AqNmQnj0T4fA8YP6yKdK2UbVHIvsVL0u57keQx3fuSClHgCHD877FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=k_fyPM52qwQwN_1Q48rsq0MwdCU_8tdaJiIPwv1sm0MZHMSb0KNRivxNQAEhT3SUMVoKrsD2a4pl72eH331JuDpK-2WS_Jga7ZBGVGSmaQfkYemrXutA_o1oZgUI_8P36p7tXs8eIshkfW2-KsMQqwhSu6gCufpnjvjqzU66Xe_0JJpIpJYDUfhVydLa1erXoYqG70g6bWNWCc_eji7bumlIp2mfKc9hB62p6IhBHhcYM5IlYnrc3C7yfrX5nIbYSE7bXSMuHAfWcP0YttxNdqxtnuV4u_x-AqNmQnj0T4fA8YP6yKdK2UbVHIvsVL0u57keQx3fuSClHgCHD877FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAaYPLeYQp9fC4KXJNoUtMUU_J5U5iC_0p016PKmVNFERJ8n0Je7_4OAvK7_QAZrcuODQBndL6AWN-xilkChbQLSyrNJr6Nx25gUQGDshBw39FrEYcJRK9nOucTpnNXIOwKERVND3KFt5c2cl3P4BoF_i-Ait6XfK2DPSeQ8iydOQsPXqLUy3_hsT64QjXs4mABR5oZjsGhr4INcZdrk-kVDjrM9cQLhqrhzg0MSTddvXDz99Ngb1EZfumPIFuLqF941bJugedF78dXCyKy8eu7iaH8_4j49YkGEDCvaqIYLvHpKzjD-vWZoksfjl4Qd5p-ddYh-xPnL8vwE0vW4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EshaNa_MXlppeuwkM_hLczP5t0s9NTbgQqUkRZUrlz6wovql4ABPEiNT4n11WGUwnqUGiLPl4MuQyuZBm4uiJnTO0NVlABtEQwb4_Wxmvwg8Q2CwfKlfhZVOoaOOG4n8jruwNFR94aI2yYwsIsfPAX22lfLgc6YTiKHC3iXN50IJgWme9pgUEt-on4YtJ3NW6S0RbnepQNs6aM_K7ykgIhUlG_t1QHnphE-AePJU_wejgzFAap03hPstAzJ7LnrbMLUWaWEWuK-ESkd-94xcSur1bVjbArnrzxEObUKVG55Uta3SG7IOWpuj4oZjIS6rNE3IGKCF-GT6mjJ5neY7iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1HPOCKLBQNPV_OHmfNk4s83OOyjBSbBqFo-Qa_xZW1xwTLkhdMJ0nh9NSF2j4zkjq7EOh0jzpwgoOn2L52mDP5OTpQzDBdgNGTTKymhN3-_A0qcqlAVnnWcLfKNuSePXuAHScL6-Elon-Yqg7dSp8PCaJOvWKOVYA1AiCfL4tJjvLMpBXr4QTwowdZYAQTaeD5Dw-1mEyJ1MPyJH6h0tjjp_c_ZMRDuuWxPTrIiiXgfFi3qXoU3CsjpJNtcQs6SSSwkBEWdYBfqzkPUJ-gZeo8BFDIv8iunG-dggJmwUA9q-Fus8GiuguSMAMqaSfCU27LG0V8qwInKHIkmDNkqaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFlpTsRc7pI6bUifi5Qj6bQUgDSRsEq0KUUup7q9NlljQ2BY6LipBdKDdS66KHLdhjLKtCFPUZxI8onCZW83qiWTsKVqaYkntPgoL1BiBQdQI1TNXaRKcBpu2yNUu1xvSW8cv6HuYaqbhVqmwIYg41fv4sR6sdhq-UrUjfUqlFxuJ3Vm1nvYAGbWfMY0emCoQpc9uxedhNJ-9Y2T2m0Ydi0LIb0pEZ8fRKHOogokRmzTjh1g_JrwUKvtxWE_myRQ1t5kVlp3pxf8_6u0Xzpc2AmDXpDABYJM-ToEl8GETa41YITQIJytoTVBZBjuuwngqAE0cMlx7v3vuGSMCzeWlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5cQuY7AIbL1dZjSFOfR0HVGWI4fQGtQyVsEJ6OYEJZn6PKKu6fAg1pHe27d6nTClqrgAOf_xFzbwG47W1JOt3c-w7LxVwYMAWWfhUTXOfcr4oLQuTXxDP20ncp3rCUli-S2y120dk8n2zqam6xr4pAEo7d_8tQeEwwRVvay3ml_Xvl6utkQEF-034WEHJ5aWy6MEhIYszUujlwIhNj-T_j7SKWXb1ip_iLqhlB3hUl6JujBinDniW1ASrL-phvK2aSR4bl3t04jlg-VZ3mUEi0GxDxLdk3VigcUomcFpgjNiuO1BpfGGeDnOljIql-8qvGsJQOY065qHuQcsD_v6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwvJfWkKGaOK2HGYBUMShWjVxS_0V2OL8V8uxtFAl8OQ9ZcdgMizhODhfCg0ceqRo70by7N-f0b7dHPNwBWC5ZSjQrdoMm0mZyYwtOvoXwd-jKi_xInBu_ZrhtzPCzoRWQ8W8h7AA9CVFU8XyQEmSaTzbR847SCtM12fLdNvFCANuw_Q-L1RU5O82vJyC6jgeYjKRXij-PVtZBAUS4pHI8Sp5WtuddxFKJ2Y7R2erG1oJKTbSYR5gMtoZ0BilDbXYKi0G9B58HWMkkUu-VC9Uaeo4Xo0LJxxYDostu00sMlPgkMQGfa0gr7IibndDy8EOq1bokQbHC4vX8XUZdDdsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D22pBVX3HJ2RmznZMR2sUB9jqINdo5X3pTCCV9lVCqt7DQp-etu6XVxdc-kPwv1dhgeKF6DjhyU19rtPY6T4NFj3fYpMuuqlnECIIAn8g5REsvFAs9QNBJdX2v_Hs5faW7Dt-vOYPTkg-rHQdCxvPAjzKg-O6hI-nVauE1E6ZsjRKq85R9GCfYsYU9S6Bo5uLgsfFGkI3Tw5SjvJdkd_e82Z3EIJ1icl-BBmHNhJ1FuJJ_WlJyJ76tJAYjR-CwN-Je_TfGsxWxTwqai99vd5nX3DNYqa3GLBRe9RSUiD4TAjoarfJL-NZvBBFnV-8wFLDpbCFfEKmk6-3ty48rX-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDvBZG_JxuoqC882n88Fhbx02i3WhR6NCfJCr9L9K5OCzRXzmkv19gIrcn_YHx64l5oWiK8p5_61SVekYw0Ab2e6fqA-P9z2vOD-McYYoe0K7ns953TaCHYGB2njpwuLv_t0Ni-bOUC1SgUWpvE2RagJNKSsyaLoKjEfGQJbaf7hmJrtzfiw_RyL1u8xWZgcsNC_4vfoIzdIhsJS1lV4M57Mj2vUmWWh4XSsxrgpT8qq6GAKG0WXg9E1ysGiJ5KaB2g4SWKS5PQCeAVwdYswZ8iOggWS3il3k3TSOruHG3edGM2rn_qyNyLe1ZuIWn4UHBjedBmlnXbAp8oRi2nzQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7MMujA9ATxISWVONuEHQehBQsd-oB8PYKlKdNxGPtu8_MtxtDScYHhK7SGyeR7vHKX-P7xKG12U0MswnPRFfPmc4iOOdWOk8gVCtx9U1pYmmWJaFeFpJL3IcMHUjgKEvUMP3RMJDfctKSugwX4Y1DuQu-vo39rgbfnH9zVzi3DXiV5EFJiJzaj8-23siRG5rV_3mxqs-q1JP1S_AB4lpoJ65PJw2KtNtlmxs5F6o1e0cxr3B1pJDy80Wk1KkNiP6CDbJtIlNnThFUs9kH0EU6DoZdTgGlVHaVyzBk9L--W-mAkumOgLLTDguGXRTF8b-eY_btqma-D3esCyFQF-yQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THpVoSkY9kI771ghJI4P5tzwzZ_3n74G2v_3M1981KIXc04-jMcwj71a1fEPO6Y5warMzfg4_JulK57jpHJJmRNgIoymOCQPUF0Rk24vDGoGVW1hatpKxrJJjOXnurKcuGTMgmAg9PF_a8Y9FIhjYqdy3_9aUyVdMgwC06J8AdLUAqWFznY8m3hSSBKN-2w-2mlW8uOj1UmLCgczDjjQcH0MGEKStlJIrL2QsM2J8V7BVhXnVpOfowkLc1QZu23UPrtW7Cc6vnokjzD0RLex5KROA9NBq9ulYMSEdxUyxM5eTUDR4KOnMjQsiWAR4DuL13i_fmMWh7uXkhY-0WRTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=t1agv09NLRwO8Eq-Dx-ixaBk0VeOTvYsZvV8LyhNUqrgxEtVHH7m3qt5i_aQUquETOrmxV0AtGPzNxrYaksjFXF-q_7ulKl0_JL2tpgRHJ2L5TbQ7aZ5LtGXQfswq-jc8nW-ycT886P3Dxs_hHFANoM_413MXlly8pIdkpwXDKgYP2u0J-fs-6vnHTQToRi4rsPzs0oJXVwNnxOTgonAALL3n2jja7qRpCHpfQf8OtMhcH9r9Ws0ltZkKVYVUdfu8jRJbWD-DA1mAObLo0i5SsgzxXonQPl4YkDUCls6kjXaryRw9Jdwx4_h-nLNowewOkSG_iGDfWOEBXIC7MAsKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=t1agv09NLRwO8Eq-Dx-ixaBk0VeOTvYsZvV8LyhNUqrgxEtVHH7m3qt5i_aQUquETOrmxV0AtGPzNxrYaksjFXF-q_7ulKl0_JL2tpgRHJ2L5TbQ7aZ5LtGXQfswq-jc8nW-ycT886P3Dxs_hHFANoM_413MXlly8pIdkpwXDKgYP2u0J-fs-6vnHTQToRi4rsPzs0oJXVwNnxOTgonAALL3n2jja7qRpCHpfQf8OtMhcH9r9Ws0ltZkKVYVUdfu8jRJbWD-DA1mAObLo0i5SsgzxXonQPl4YkDUCls6kjXaryRw9Jdwx4_h-nLNowewOkSG_iGDfWOEBXIC7MAsKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=q7FmcSMQbpjYiFkdNIzl1opBGYPfC4DJSb-2v2uMsQN6ykmi1QUKGOcmh0HMhS-tVOpXFnRCSI3fLW_dIC2dqA0OklgtKsIo2Scpcf3S2Qw6OFg7os2E3NABW41F8X93MXFZW7xzdKEA6WqeQHa6-TVEbkYZUPjRl_q-P4HCurT0R08trbxAHddpMRP_yd1LJM4DRByPKffkfcHQzOjqnZ_wJqlEj5pkD8GpfzfMX9HDYvF8kSNauMEpapz1NLOiqXkxoA2D88zc2Z7PxExGS4CjICyOHBQLEXsuRJUkI0O-1WwGQKLsrQnvmPfxt8opiL_0HT2xZTzqfONdctTwRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=q7FmcSMQbpjYiFkdNIzl1opBGYPfC4DJSb-2v2uMsQN6ykmi1QUKGOcmh0HMhS-tVOpXFnRCSI3fLW_dIC2dqA0OklgtKsIo2Scpcf3S2Qw6OFg7os2E3NABW41F8X93MXFZW7xzdKEA6WqeQHa6-TVEbkYZUPjRl_q-P4HCurT0R08trbxAHddpMRP_yd1LJM4DRByPKffkfcHQzOjqnZ_wJqlEj5pkD8GpfzfMX9HDYvF8kSNauMEpapz1NLOiqXkxoA2D88zc2Z7PxExGS4CjICyOHBQLEXsuRJUkI0O-1WwGQKLsrQnvmPfxt8opiL_0HT2xZTzqfONdctTwRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjIotpTa92zgWC0Y5guwXOA2aPcdq6KI1va0FeF4f9PeAlFZWCck61BAHTye8H4wULbbPNXGeiDmA3_ys7DAbqhqkPOo3DGGqNN-y0AnIZj635zTcLnc6lSbs6mEotoy6JvRp9DdlFss7nMZRlx9dCYCujNnhSri9159Ct_mwCNzgeerPZSOX7AZbjDKwjlMC6T2eEZ-FVt5ypE1u4BUT7vKnDFf1JBVX0iXRBrQLV4EpLw7rdJQBVV0oKZq1cpykxhIKbK65uUR3OrfJxu1t2ds77byT1-yNqUhh5YCCMIDeqSfiEd6Dn7R0VImrdOai-hvQt3vDo4Yqqijpwoc3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZS2W9r7qcZU8PmIkQ4UN8sxz0u2ZaQxgmKWNVPXagAke89YDC5wdu7psN__EudA_aLVyudIEVxU95P3a9qBctlgNgx8reoe8nJv8qK_GpkbFEKgIIIeyPfHIXkDpZ9wtsTG6Cv7LaNhKSwP4MSX3ZuHjelePgqlCcAqx335Uh0AiZ_FWT7BqP1KesUx61BcbePtCuu4DBriJVyaFNKyyKaRNZjlHw6jqyjXBxBVQtpHKvVxEFLCCDZTC0E3o6RWpUmWeVkn4zaQXj5N3sMevvfcXv0FGAaP6UnWYnf4MHiOIcUpr57ssXG-yaDr2-3Di7lBCZ1FX5OkJT2QUEXaSYA.jpg" alt="photo" loading="lazy"/></div>
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
