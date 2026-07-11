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
<img src="https://cdn4.telesco.pe/file/W8DfhZD76nUEnfkiDt7yluAEmiXERInQsqgdZbDt107zZWotuRClQLcoMNJS2qCQze2MmI4f9qnGK67d0jP88Udr9MGj-vuaTc9CO0icWXIqtSBg3PZGDe7-xc-CDsnlizJqg5yBdoRMlTT1n2JeIRUwnUz8PJfGmX9yv3JnIb9dmyCgYBof2395bdBKp44k4AcsAEJ5zImMvJoKn-7aqycWd3DzyTmrcdkMwAbd7Bybq_JobIkEg0_sWowALig5P8s2yu7sujxggbRE1pX7R88ivRsAGPK_1UhNO2SuNDOU0MoXDIkhl8y1sZ-RUEiG5oRJKGHAtgDaUMxQRj69cA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 03:14:36</div>
<hr>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
سپاه: تنگه هرمز بسته شد / به سمت یک کشتی موشک شلیک کردیم.
در بیانه دقایق پیش سپاه آمده است که : «در اطلاعیه قبلی گفته بودیم تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت.
ساعاتی قبل، این تذکرات نادیده گرفته شد و
چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند
و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
به ناچار یک فروند از کشتی‌ها مورد اصابت شلیک‌ِاخطار واقع و متوقف شد
.»
🔺
جمهوری اسلامی به زور میخواهد که کشتی‌ها از مسیر آبی ایران از تنگه هرمز عبور کنند و نه از مسیر آبی
عمان.
🔺
آمریکا از جمهوری اسلامی خواسته بود که شنبه - که دقایقی پیش تمام شد - ‌به روشنی و علنی اعلام کند که تنگه هرمز برای عبور و مرور باز است، ج‌ا اما دقایقی پیش آنر‌ا بست
.</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuF20fyARGEKCUWi3BNM_a9jOooamRFNPR0rkC4bTEIwC1O5OLccf8jEJCveW_aaaL4rPV7IVqykbQBaDePx6O2w_selBi3s0LUzCY6iS_e0vYW4K_WktYSqd8NLtFs6e1xbec6GgaJdblmuW8QQ2xfT0rgUO_ptyJowHZqohokwT99DtdbKwCKV8zoOfrUWnHm3iF0UYdHDjyU5ZHhQCAhHi0128BlV7_0sc357IiUBjrCPegTkMvPrR20dVBXwYv9xP3koRWGJtR-YvcaUBvF4Hk-iFgnR8k6-zJMZFoBU9eUKsod0cC50dZYIFF-NjaZtRZ9vgjbSphd8I67RFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=r26ne6TvbHHd98cDEEenuw3JKy-pzc1C_M2JcywUfLFPklxKo_xEXfE34RlleeOEIKXnbq8LvyMv7llNRaLbs6dRhYHGKsTqby-tBUb7cHwatkPeCoaTEaY99WUG-BLjbCEptfn0MBjVmw2w4BMKXbh5dpRY-IwilZc4QHRdBYMQtsrVOV4dkR-F1nS_steNmxfW6o6CY4LnVDBNDAVBACSMLhQLNO7Bwl2pNw8OZkCoOSePk7nQltMYfwQBN1-fspAqsUMGzlcEhhNbtql_4t-byO825LcgF114DCnwXi10uFZZCzLT79xYxpw7T_wAy0xHVqVY70F-BO_dO8JwHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=r26ne6TvbHHd98cDEEenuw3JKy-pzc1C_M2JcywUfLFPklxKo_xEXfE34RlleeOEIKXnbq8LvyMv7llNRaLbs6dRhYHGKsTqby-tBUb7cHwatkPeCoaTEaY99WUG-BLjbCEptfn0MBjVmw2w4BMKXbh5dpRY-IwilZc4QHRdBYMQtsrVOV4dkR-F1nS_steNmxfW6o6CY4LnVDBNDAVBACSMLhQLNO7Bwl2pNw8OZkCoOSePk7nQltMYfwQBN1-fspAqsUMGzlcEhhNbtql_4t-byO825LcgF114DCnwXi10uFZZCzLT79xYxpw7T_wAy0xHVqVY70F-BO_dO8JwHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvig1ayycEUO61gbGKyWPQwWAgtEOIUfc7dj6Uvm8TZGIc-ut-VHA1cGNpDjTZ_GT4inGe5rvqItsMgPqX1UP67NnLkk5_eNMvIc1Tj2WmTL0M6UpW1EcThYla5kK8PAExzocn8pRk-yMknNceJY2yPjjrrW2NagUfO73k1AbIKW0Pk3HFQouvCChpGX6GplhTqiXkcXt62csvBIiRW0X99vVj9H6s4_vNsFAbUILs-CCckIuo8WZ8wCKWOhcC-is2uC283a9dJmWV47SlGkoUo_YdAj_kj987RnHWDMuXJosE0k26QNrBDvzWC9M5H3ZHyUDKn8R7ocAsJ2ynzK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2wkjnFFYSVLJW15uFIllcIY9Hr80JsZJObJ_zS_d0dY5c3k_F7S6twNyo619DnxB4hfYYVqigNEh6FzUBXvgLdLJm4Wh0P9zhS6rIw9-AtZsOcVOWk_ZypNnHEhXtDJd_Sr8lwkAw1HNqPVIPBDb24w6axNW3__btmlZwBxU_gPvmqJWjDUq1GTNLNofdipbs7HRrC1iZT5Rt-RyoE5EJIgPMNNkTqjnT7H_wbxqAzrTykEqZMWQw5rjo8s5JgYjymhgPuYJ3qWIeqfj1AKFfADjNqeUOp8KA-7BTOx3eMCSo8TUbIsUQeMqIaGWj3yitW1xtQwLcNx4UCOgTB0JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر یک مجله ژاپنی
در آستانه جنگ عراق
که پیش‌یینی می‌کرد جنگ جهانی سوم راه بیفته و…..! رسانه‌های غربی هم پیش از جنگ، ارتش عراق رو باد کرده بودن و بهش میگفتن : چهارمین ارتش قدرتمند جهان!
رسانه‌ها عامدا اینگونه می‌نوشتند
تا خطر رژیم صدام‌ رو پررنگ‌تر هم کنند،
اما این باد کردن‌ها، در عراق هم باعث میشد
که فکر کنن بسیار بسیار قدرتمند هستند
و جهان به قدرت اونها اذعان کرده.
رسانه‌های غربی با «قاسم سلیمانی» هم همین کار رو کردن!
و بعد ترور شد.
تروری که ترامپ هر روز یادآور میشه
که اون دستور کار رو داده!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=f5w01YbXXyKZbKWgBH6SOD4YT7dOa6cOkHpXu8qyxQ2WFsg6V7FSFt37g2AZK_ZmBs8K8zPdhPULP8zV8VhO57OgTnvPxw2N-TzucUl_SPNfIk1yqWAY6p47rTDdHZcMS2jX94UDWyDRDB1bnj6d1x6RVsGRKNpVkfILmlDNZfSzcOhnyU-sZSnP9-ztarQHiGsfrW5D-G9fEAT0pzHbXIj75yiUZGADzNUKB62Y3c6IpjIusSFftzO6V01qluRnkqHBgxQGgtaKIVFRvrNYGH6TeEUbzNutvlA9WE4EvyrNlLBRwkazlQLWcZmRJuVjYc9DWFSUUhdCSEtKZzGlnUGLY_L7JnjCrtk3V9UPcuv9xtKC2b9OPbDUj1894euonPvBB6GRtZ0BKZ7VFU9rjlH0t5Mr3iPrjK5Qu86UlbEeF3n7nVoFOwQvwZ6q4YB5vre69idoHlBmzNE1uK-qZVbbD5JpUcxaDAtNPy8MB4O7gaACMuJfkDmTI-It3VoQLzcfytFPilkUON2bfmGjWLDB-L_98ctyOw6oVnU8m4b2vafxDC2GAJ2OMiPRxMr7czbjhPFmP0y3y-qMkbClQMmK_Z5g3I8_8JbvO9Cidl_lZO7IFXPYiWcAmBrgcSpBuQoQaoT-PkV7pJZijKm_uwJqpmzGK7ig5JO0Ukv6das" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=f5w01YbXXyKZbKWgBH6SOD4YT7dOa6cOkHpXu8qyxQ2WFsg6V7FSFt37g2AZK_ZmBs8K8zPdhPULP8zV8VhO57OgTnvPxw2N-TzucUl_SPNfIk1yqWAY6p47rTDdHZcMS2jX94UDWyDRDB1bnj6d1x6RVsGRKNpVkfILmlDNZfSzcOhnyU-sZSnP9-ztarQHiGsfrW5D-G9fEAT0pzHbXIj75yiUZGADzNUKB62Y3c6IpjIusSFftzO6V01qluRnkqHBgxQGgtaKIVFRvrNYGH6TeEUbzNutvlA9WE4EvyrNlLBRwkazlQLWcZmRJuVjYc9DWFSUUhdCSEtKZzGlnUGLY_L7JnjCrtk3V9UPcuv9xtKC2b9OPbDUj1894euonPvBB6GRtZ0BKZ7VFU9rjlH0t5Mr3iPrjK5Qu86UlbEeF3n7nVoFOwQvwZ6q4YB5vre69idoHlBmzNE1uK-qZVbbD5JpUcxaDAtNPy8MB4O7gaACMuJfkDmTI-It3VoQLzcfytFPilkUON2bfmGjWLDB-L_98ctyOw6oVnU8m4b2vafxDC2GAJ2OMiPRxMr7czbjhPFmP0y3y-qMkbClQMmK_Z5g3I8_8JbvO9Cidl_lZO7IFXPYiWcAmBrgcSpBuQoQaoT-PkV7pJZijKm_uwJqpmzGK7ig5JO0Ukv6das" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHyP78d_fSmY-vAEqFik2l7ZlkGJy21Sx5I5dXjWixnIxpRpKMQdGkAI1Oq1KSAenwWGwTeB-J37Ym_eptTW1CdqlhbHYgkJxls9JRsQ6XtTkUONkJqS4JY2SPk50aB4rZOLXPUJiFVeAy3u1w6TP0mONF6NlH32w-dKUTKJRoz7VaBhNN7Z95b8cIM9PlEwtvH-zGzX4l1FtoDauqlw_SNW_Xu1nKSHmCoNkqm82SUg5FXs1X_dz-73zty4MuzmLJ-735vEf_LQIWyQ50EBzG63ad77roh1KcQEy0tAt6VCjwrdaVW1OKXmh-XXe-AltoS88ELnyqYCKtTLo7lkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFoTgLRG-08-wXkVfnmUjpyU85d5MEOPeSE2RXukUJ7gcjmFTYlZCb_kpnQL7ZIcAAM_lDv_J4qZLl0hoiuQRaoKA_6j-aoodXfesfc3KLW2-ibWZjxvxqxsCsKOE-w13vSFR6YCpn74DYo1NOBBYyEvAsrIYpZHslnt5ahw7Y8rBD5zD72zEjJb8Xbr82oFCT3fbG_O9-gKukh3C2YomWyaoxAn9HMpLntkpivRZrpZ4r0DzEYp8eqAocUxAJO47HRnA1D8xjLyMZVi-YwcsKo3Qk76hvz83eeZEW9VoL3t6eBs0cX36qSbGuiRA1OhvmzravFHMOyi9dx-QJrwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py5pVBAHjciZdQDxDeXlebKT_mn0hToihK0H8ZD-O-vPCxzgWarx6Wwpy284gXP_I5pInK_xlh2jMO0sR2aqbOEkeQNcjvoMrANxhTgZ25q7x5NVERH0a7bF7aivhuOMq3p4epzR0c5klumgmFuuJav2INbmZq57RzGV50zgnwAHyYYFIm0CoVWCg09v_HYeeF4oEwmj9fe-TLVE-2SV6AoQ4oDGTLUcMsAQw72EEMJPJQe5ZxHodwLvnOOmY9-ot1VtbEBS4NUKurcI7xVFd0BjnA1HpLQlUuQBCa1ezLq5lQJD-dv38ZnyMyO_cfy9wWVcSeWwqWTv-UB9OhweBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=LkcvmfrdzpxGkmgSZeK8_6hPNsH8i_pmYcMGfBVC1PLRxBf-dKrqjcXjomgvbijsofmZ2uhPeCaOjlU_Eq3dxXscDdNcQAu_2kSlHwr3ZzzZ2pnRHEC9b2hNu-orfPzBlI88XJJQoZE_ONxpes9qOa1tGGiDHi2KJjgdIr9foUbWKliFdpLZ856jnxGhqTc3pGjzVWmLfPTAZIT2XHQMHgUWw82HiXBAfjVPsrnkHk3kzalijpC8dwwBPC_wktr-ucCiClcv5E-LdUNzXw4q94AtKXJqeJCsyCQMqrXdDJa32QZn3r4Rl4KOxljEdIhl9hrmCR_Wn6f44Mt_8I27FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=LkcvmfrdzpxGkmgSZeK8_6hPNsH8i_pmYcMGfBVC1PLRxBf-dKrqjcXjomgvbijsofmZ2uhPeCaOjlU_Eq3dxXscDdNcQAu_2kSlHwr3ZzzZ2pnRHEC9b2hNu-orfPzBlI88XJJQoZE_ONxpes9qOa1tGGiDHi2KJjgdIr9foUbWKliFdpLZ856jnxGhqTc3pGjzVWmLfPTAZIT2XHQMHgUWw82HiXBAfjVPsrnkHk3kzalijpC8dwwBPC_wktr-ucCiClcv5E-LdUNzXw4q94AtKXJqeJCsyCQMqrXdDJa32QZn3r4Rl4KOxljEdIhl9hrmCR_Wn6f44Mt_8I27FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFBHiFZm8fAMSiTqrDXjhuuQLRrHCYW6o6i3gDS1k0IZRWi69pH275dYJ3vncd_qv0LaBLjeuImSWQF4jvOWcLQe_bjIy2ETCKNRCRm6IjzQN6ez-mWRx2eViQOmOkIsHhhRDmBvMb7OM2s3nYUh2jcR6kuCH7JLNzWv7LzEm2bCjc-Hh1IQSPv2vf1f0cnMpoqyCRUJFvcDgAOLeMmnjy3xSSDb4iZEopRc83z6Pm0_4Fd4N0JK7TvOgk4zHjvEnR4Cm8ZqDDYTnUsoLZ5cXuSJvAw12Zp3C_zTQd1nbIhyMPOzx_7LIU2o1Lnph5eoDgoXJZKw0-Dpfdv8lX24fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7R7eylBN0enMjg8hm88svdCf3cEvTZe1oPGwvNTTtuZ_Poo6kWwszZNxkP9YDOoQz8gl3nHRO8iqsKAjKxECVEihOSVEEl19bnMB4Or1sZgboVL2idfgCgTmftnZNtxDR07vFbQkt8ko_JW8wCybvDUROeNKNd_WfR9B3E3enI2VmZTkhxDFpK53KIiTHCrr-soAF3yepX0g3SoEEFFKXNZNABFqyw-NDmHiXUMhgzDCHNyoAYr1ybZjT846oN3TXHDDRPTNpjw1EOJFXYfBzkCjD-jFYgKZnGr6UBMWfag4de-nAyfDQeS5jUZaweFMcSa1QHNKziFtcuiJGIFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJqeGgnUgFsLYEGoF0wjtOZjP2qe_2TP2VRrv97QhG6uTnpybpsTh3HXKgsPeGpT7TMYYMsg38-9U4z4BMNk_8LXPoTRe-rzqkp1cWcai0W2sdfpYvKAMfkTMdCFATiKyAJt5aXrHdmA9pFsjm5nKy4Q_vIzFB8GsHxaHi00LyGzkC3Geehz9yYc0sTLGLNopQz1WU9wEwZiJZXrg5lgw5dqXpQ3g1BYKq-kI9ULJql5MF-pV_zMbQ4z7LPYiCCOMKsdhJGuTHi6A4eOeEL6dS7kszNlZz3O0yckf6_rQjbODb-zn6U34E5CjjgKoauQ7Vf-UpnvUbBzuv4iIry7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsTYX3DBh8sLkAXLHoWd50FP18g8zgnxGK7TdVmwy2M96aKiXVMTRP0XMMXnn0FnLn9R8epW9YUsUX3dUbVjV4JHNdqZTSutcKjrCCL5PvzU_JLdbA4gSn17cx12cIX4MjKXZUXKZfnsMYMA3_4reLGpVkRHsi3IlGxVT6wxkFTLAIkUjug36uPnXDN9xezTUfEbko9JIFbkRHCIecWJr9TIgmV5u6SADKqcP0HnD_Nyl_yvXT9pLvajcdhxkiMzbCGjwLUm1yaLpVWX952xeeLlwhpZaL38QnJMKEGnauoxC_zHP9Z5n2K3jZKibSwa4nlT9KJrWZrf8eae_13jPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SToNkh2f88FuXCRC8_iTbycUeFDynCAZGGX-xNJ_KWKxirVcQCsxoIYbDdUUXjTn1ISR5eX2bmwAzFjNWx042fPg2BKWcU-5_96PpcoO4gOidGiQ_dMS_CzL_rbxGiM_CYP4LodvFOxNf5YHoPC7T9ZGLMMJMVEHxTCKuvSWRPe2WsxMx0EO1SFOpEbTZx2fvEl1WM0HV1tRm0MsskSiOESBZaV0oMuTtxK6ud-gm1LHA_aIh_75pIAMiMD7nWrGaakatgJiv99GSwjceG73nf2FKR59fYXQKLsR-QBjqjVbrT9lWiNGO98r_GvsGiDKua-yIM0PnNF1ouRjxZ-A_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FP5pIwlUqWAy_IOFRz44hYNw5uKsNGX8j6Za7nMkFM77p6AQ6JA8QNpPM_wM_1nGgfv7FQtiKORTTx1ih-yx_MubOoDRnl7oMee4_kENzsX1PqvVu384wfx1anGCR9qwXZF3AbUcpMPKzPkLm-CsDUxEn6RcraFJwyB0Ri9eqMIZcwDz5kOZ5-5hjCAUcEhsdOcVYUsCjBOX8q1ijaHm-N7lrLxV58bnFWuflmuTyLoQHgTlBoZkdXu5EgLxtZOhwmUT0OOMkx4A62BwJTR3lasfrgxL-Lgoys1byo2q5gZXvgluqVRMZf4JLPHVmeFvBW2vc-qC8rjjK7meeu7kaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RX7G0tm9OgAMMgghPMchtv6npfFOGVPj3Abys9zvyBowVeZ0XrgaHhqx6OY2CreX3tMsN9dsyqRrxaFVSnf9jHkidq6nHk2828tIcaOZdAylDeCoQ53XmyRg6EG_Mxxrn56GgGCLZrsJ8CNlrXau2edmQVBG7aMS5cUr6O3_qfwsowYxAhNXUpg2pUFQwhMBsiLKgQ_djXYerOdS_rWQosReA9jarjSy9SSATHKqdZu_2gFjGpfTgLMYFSA50dBQeheIWIrZehO4ofbM-cFADQCf3juBwsWHhE6mbwT5pnMakzLUzaJFx0g4MMLengL4K9x_zk72RNqRaQjXg_4gtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWZ5SeSEDY7oa1qLexOZBKQ5Eblt1J0nZdKJBIY_3eGOrHFWFevEyBKF2IOm_4jyom6psjE2BeV6Y8MeQBRuBKrMh71PSYb8SfLOPuO9eaJ8q4_RcAdgyGEEom4Ze_hSqkgbKD8Lb5i8lWXpO4tfaVSHxGAm_k8oXPZLBWAPotXJw-ZrduOxMRpLfeApkRKNohbiCsDt_NlKSnf_2Fpvjoc6tFGTRrR8OZQMRAMIjZ1CZGJSGonwfzb-zr8k8s_p4EIriNvBk4Cf8Ou-f2fQ1VOPPiRpvqyYzdfa9_tMZ1E9dVXoeCSJBjuPTqD5-r73eRq9nNLo77pg91AHL2Z1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bIVVVs1GCVwQHDNWFI4WP8UbZbzgUKenLcdjcEEfdNT-A07K9lu-jvFlBhLUJj0jMTPaHqqkwnChEBag4pA7QG3isIWnEa1IM_lJuH2j9fQ6-HWx4JktnqoNc5OADpsKSP78gwHrwntfHc6Zgw3CjPaoY1Pua0veq-b7htiqQSQcTwDJVh6KYJbV6r1hZmjfYU6Sg27U68AJy2uEWnaDLFZb6oqhx8XCrpWjC3PtA12Z48WUNNtNjUUERxHF77PCtu_m86DNRIglIYUObHf-wYB8nE_pglEW2DGdvey5P9q1LXbAIftZr1p0abW3D8Al_0eSNi-cQEge3HRgDcUyIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ChVeHkNVkrHaUtxd0HkhoFPFoMh4nqvXmOnX1K13RWCkhcuBIYxwNqh5x8tsFrDA6wRAI8ZZd_T2y4Tk4QVD1G-tGP6Jkw4MgkS-_ns5TsGuOuTkHPaFalMieFIRoyJjCcAi3KWLEgMIPDl02e5abv_H-Son_xZepAvqLGdnZar1PiWWqC91YTWOIayw_T0hrGnpAUpGKcaqcmYSOiMiSUSAl944s07jHXnzWMXEUuMJJ3sWXAlatdG5l4GcyEbr6g6lH1htJJxELgJNSHvx07OcKzjFFV9Bjwaq_jK9a6ovLUGxeEyt-LQFywZZ_1WxCn8GFdcsa49mdI6-IUeebQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=UG1msQ4axl5CTHS2FwIbU1zT6WQKUPb7CnLJzgvh5bIBbIXx5m4kL-0R1fhswkAOX4C6U7oBvLjUau_QA7F0ruAVzrtGsm6ItIU8UEcPqji2SoT1Q2wH5oXiu0BvFWygoyD38lIZOqmNXrlcQ0DMtViuT_0FtQFJEmDWA_Fvzu1bC8HdyrazQauZV8G8ZzQPf5Lno3lZvMi7IRePaXCzRzO_qDiOFIxfvKX45f3livdEduBkVFG6NBuJ3msIfQT21tWLCI-cfMNXMZpFAXTJplBhPnGkKEBirIsaJ6AHpuEWSQVHlzERwM-24nH1qxsvEwJPwu6813-qOTej1iZchA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=UG1msQ4axl5CTHS2FwIbU1zT6WQKUPb7CnLJzgvh5bIBbIXx5m4kL-0R1fhswkAOX4C6U7oBvLjUau_QA7F0ruAVzrtGsm6ItIU8UEcPqji2SoT1Q2wH5oXiu0BvFWygoyD38lIZOqmNXrlcQ0DMtViuT_0FtQFJEmDWA_Fvzu1bC8HdyrazQauZV8G8ZzQPf5Lno3lZvMi7IRePaXCzRzO_qDiOFIxfvKX45f3livdEduBkVFG6NBuJ3msIfQT21tWLCI-cfMNXMZpFAXTJplBhPnGkKEBirIsaJ6AHpuEWSQVHlzERwM-24nH1qxsvEwJPwu6813-qOTej1iZchA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=dkhP1O0PaTLufQsZDUdKVzZxbe0Td5bFygSu2Cs5UpNZdV0RC0dVCxHVQ9-xXXsF3daTVIZbsYwfGsw_FLlLnYR2pFGkEenlwSTV2qGEGs0e5M77Gi2H3GIRRbqyonnGTiidnLw8BRCzbyZum06y2X0PenNIN2mj59BA_vXbGyQBYMyuYYYN5RCXIvig_WWpxSpjue-ZR-p_1K35E59X7EA9l9euoKjlD_SsZ4tR1JJVNi9JTF-NSiujqTgJvh3_SCkmS-bZnuxXb5c6_3zYCAMO40RJHinK4vBGFxBw0YcCJB0Y45Mtm5fLfaIFHCmYzlXmj3LhcuY3aB2NyWabwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=dkhP1O0PaTLufQsZDUdKVzZxbe0Td5bFygSu2Cs5UpNZdV0RC0dVCxHVQ9-xXXsF3daTVIZbsYwfGsw_FLlLnYR2pFGkEenlwSTV2qGEGs0e5M77Gi2H3GIRRbqyonnGTiidnLw8BRCzbyZum06y2X0PenNIN2mj59BA_vXbGyQBYMyuYYYN5RCXIvig_WWpxSpjue-ZR-p_1K35E59X7EA9l9euoKjlD_SsZ4tR1JJVNi9JTF-NSiujqTgJvh3_SCkmS-bZnuxXb5c6_3zYCAMO40RJHinK4vBGFxBw0YcCJB0Y45Mtm5fLfaIFHCmYzlXmj3LhcuY3aB2NyWabwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfieKdkEppQPzigMMzYM2vkzOPQv7M5sHfMSgbxsx1e2W4VFrtP2kZI48s5EAsRUcqV-qfnDysUZNWrCK2J_akhl9SEcQiz-W929FvQ1Q2gZzDgr7hmtZ-xEsJqVP_jqblUTJyCONuutPHZqAQdMc2vemlxF2lZ4Q2FcRf3YZNOxAiNQ_2brVjMex0LkVY5L9Btc8J38Su6j9oVH02wL5ggsdyDJzgyzgvZPwhwWyTw7m6A0FIAPl2Y2nG7lIPRcbCRHVh-oJcqDYSYN89VSf431XmPCEC4Lz-kTm1lCGZfyDeOSbB6uLMsbIvNiYK6QayfORJOpHdI60rozq9w8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gdns3yb6_EB7oAQV96MVV4AkoXPNQtyLnlwFaVeD0HAH8PzHq5rOhgLXsIl3N1jCgTRaWDMWwZsdGNi9RtJs_85QcC-aKDyEtXaEyfh1lBwBBYn6IiIokQ3E7C2GWSCB_cPy-JkaOR1-pHIhcKboRqF0tIOY7KXc7mU0cXtTURjSwUSgg46x0fv3pMkD3nliyt4yTIUrOfElTrVDuSYUSVtBkSZHLLECIO4z7bDgtfb-RHqWUX3tXfiioMVvKWxTvNofwPeS_gZ1D8Q22wFy_aTomAwKOaqh_jyQNg5YvIAKb2Mn9XjMX3bi0J8QS26rKCmGbsu9tHnKNqk5VXMksA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6xcch64IXC8l5QcTYD5Axj5B_vjZwD-XXd6Ipmt8GCxr51od9k5hdIXsm9S2wl16fCYmU8jbG49ovOxU7yUQoysXTEz_AAwCj4kBB6XkaOGoeokEFintnc26FCXhip6KDyidGRmCEJf4wcvNyuMPBuFUKOjnScwavB1gAoAS-KsspSzK-lzjup3suRarYrJqMHbiiPm9I0iCe5w4QZVC0cFBnb7bNDu2fWTZ-Kh_1NYr2rvPIgokEPqAl4QxyF30j7dQCbbt1kgciMKQly0Kl3zR8t1qe2s302DLaZ8LRsdCapokzgAfb7m63FwTsV9FZjlo0O6M_qo-xRlGNtehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lSUKB4zk8gfaMQi9IAaMSUnnINIrqP2Pr-737b8dfXXuwMF3_rmwNF63xEPg-AQqtOCb3PN1PJndt6xeqaDZVGiIcvvpmR0OFYmprvasvEUSH5aaTRlLY7m6RwNA1vCwgP8I1XXWZsyLL2-OGKWJOdpNcABqPtFDRuIRfTTh6uEk5X-dXxIPqHggnRLvj_OxidbEY9Wn6X3OKwxcvSvCs-OVTE2yGs03KvrzOj2HiFAzoaUaCzov1avOBZSqNZdqogSNeZuEP_I_DThBSC7T5wiKnZXU5jKIc5BkzTqZenPK48minfbBvkteOe8YWK4ynnVY2RerV9HI5mKjPYbpysQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lSUKB4zk8gfaMQi9IAaMSUnnINIrqP2Pr-737b8dfXXuwMF3_rmwNF63xEPg-AQqtOCb3PN1PJndt6xeqaDZVGiIcvvpmR0OFYmprvasvEUSH5aaTRlLY7m6RwNA1vCwgP8I1XXWZsyLL2-OGKWJOdpNcABqPtFDRuIRfTTh6uEk5X-dXxIPqHggnRLvj_OxidbEY9Wn6X3OKwxcvSvCs-OVTE2yGs03KvrzOj2HiFAzoaUaCzov1avOBZSqNZdqogSNeZuEP_I_DThBSC7T5wiKnZXU5jKIc5BkzTqZenPK48minfbBvkteOe8YWK4ynnVY2RerV9HI5mKjPYbpysQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما
که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!
همونجایی هستن
که بهش گفته بودن
نفت آمریکا در ۲۰۲۱ تموم میشه امروزه
در ۲۰۲۶ آمریکا بزرگ‌ترین تولید کننده
نفت جهانه!!
سال ۱۳۸۷ گفت بر اساس محاسبات کارشناس‌ها تا چند سال دیگه  دلار و یورو نابود میشن، در عوض و در عمل این ریال بود که نابود شد!
کلا محاسبات و آمارهای شما همیشه خیلی دقیقه!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=r2D64sEgwvu4Z6DLuvjQteMPbk5846oXxDroES2P6Idfylkwu1MDeHXAfqPfxRfiMbczjsQLT1nasBbrQ5GfPrg6Bn3XcbvV09JCOlhg8OEiUZ3giV1pAT7Ziv4VGFkzoX1rW6gq0AV0ws_kLRvr0MiARfnwtxIvQe4Ap414zp_-XvLh86XeNXWaSFo5dJC4Nz-rz_oWEegaiew_oUsPEoomVTqCwVH67J_WJAEsunKdw0pzdwQ08aaBOs-7ZxgCpp7dFpTZCOSyKkMJ6OHqv3qBF9sVwZiDEwHOAL7FBlLzVk7QE37EHbq35ufyJzXVdJPdYrAP3mfgOVEIbRjAfYAdfoWXgPa6MQ7Aq6twZMfxgS4gF7iY6HKawThRKsa9qqSSYMjMIG3j97NEk1hSqWoM9WYWeId6lF6c7e5n7yNb1qRmfVDqfT3vkUV4vVkNdtgeMESxo8-rLMD70kMkLPFcGg4tmmO1P5MbMTQPrTMxxa_ylYFIMVup53RX7PelKNyE8FlLZ51b0LzFqAUw29VQ2Sbm-caF1r09BmiZQio4JQAYmyJwoWkc-XZxYp-3_gcYeEQ0zmjZ8YcoqTpmZBxDrbfkU6jeMjY1SaVs8GPKJV-B0Nk_HbW_v6zeNjlEbOBdNFJ1JFI4BAFvKB5_MAjsjEIQCG3md8k0IJU-p4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=r2D64sEgwvu4Z6DLuvjQteMPbk5846oXxDroES2P6Idfylkwu1MDeHXAfqPfxRfiMbczjsQLT1nasBbrQ5GfPrg6Bn3XcbvV09JCOlhg8OEiUZ3giV1pAT7Ziv4VGFkzoX1rW6gq0AV0ws_kLRvr0MiARfnwtxIvQe4Ap414zp_-XvLh86XeNXWaSFo5dJC4Nz-rz_oWEegaiew_oUsPEoomVTqCwVH67J_WJAEsunKdw0pzdwQ08aaBOs-7ZxgCpp7dFpTZCOSyKkMJ6OHqv3qBF9sVwZiDEwHOAL7FBlLzVk7QE37EHbq35ufyJzXVdJPdYrAP3mfgOVEIbRjAfYAdfoWXgPa6MQ7Aq6twZMfxgS4gF7iY6HKawThRKsa9qqSSYMjMIG3j97NEk1hSqWoM9WYWeId6lF6c7e5n7yNb1qRmfVDqfT3vkUV4vVkNdtgeMESxo8-rLMD70kMkLPFcGg4tmmO1P5MbMTQPrTMxxa_ylYFIMVup53RX7PelKNyE8FlLZ51b0LzFqAUw29VQ2Sbm-caF1r09BmiZQio4JQAYmyJwoWkc-XZxYp-3_gcYeEQ0zmjZ8YcoqTpmZBxDrbfkU6jeMjY1SaVs8GPKJV-B0Nk_HbW_v6zeNjlEbOBdNFJ1JFI4BAFvKB5_MAjsjEIQCG3md8k0IJU-p4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7VFnzLqdnBxxtr58WM4p29YYEh6kam0DQH-3_IYCCEcp3gwCxix-IPSaUu1E23vri0y5eUIVT5BFzDnGhV4LiEaslUw7QCB76a-L9hYHBzGTL6Dx1olJlleg-pSnkg5UX4h38j5Tf_fDUYKyyUUYOmDCiHR0CF93cNvcrWJxu0O1-w3ZFHz7B6aqx5du74YvuwwAFhjDKAsaMrxKVDkZoZcXZSla59uT2n8F2xtt1t2cl9vq1fo1-AIU5C_Oz5_tggvyB9OYSYLcNR20D_X3zx5txzyFc2tWs6NmrJmoPyeTIZUmvg8o6bdU2-Kq9qDAZJzv5Ngta8YaTKtDKpl0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGv3dsrJEIve0hK9zpXQNepKRXBfXz4ZkxU0rLPCT6S9KrunUosjvBSzcLA43aXgrHBkL3cFrQKORT6D6RZLjR4Z4PUfX0rqIMWKau9qKtceWr2kLQDIG3R5zZmzsQ7EqWwkA95JZ-7JQghOCS7dfGhGekzc5qhg-46xpPV1-njMrWJQOT1TJkYPYrPdKLmVoBlCD6zUDuuGXUIee_67NWUpki49bWSxj4-B2So5jOwvAGAsqyUnjJnBjlJgRUuRdC8gy9SUZS7ovtr3TGAiYOkx0UaJAd_Flaq5cJGUF-nIMJJfsOebJVCnF5kWVeGLp8Zz42uIjmYmo2lqNd48pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpS8m0CYkunDb22U9ojctOEqjx7cS8kdLQT12UEY4RZxu77omk8ZEX8ME1HQ5WKTbVsuydBpdRVZ82b2RR8vfHtBGLfJOgQoU5SGplOYuOXph9TUheEtyPzPzvkK91okMuxaWcBqLFDYnxjXaIOeZ_TZctAOiI6cP6t9uLjSC2Q5OroVd9mNaX56k2KcayvxjZn2MNgt58QbRhDBcfcynIttfKC6VWxZfgbJKv7YegYenv-lmh2ddc08QOTZGQHX6BzZgZKz82lCvtYBwV8A3IYtvqXscG9_k53pFmWjI3JEr4VYqDnpkHjYl6eKa7eBQy3XXXh7MSE0ujuUMl8N5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=FkiV39buflsK8j9VdSLOVoj72yIUE0iR79qC_eazGTgc4VV84CP3wrxtT8pHh0-Bm4UB-SN1Nw5gFU_Ll53xYgJsyVfVq5qLC-15wk21zF9AK7rTGBhrxqQBYT8Wv0NqxHg9SDoGaJUPuaVAPazk2E-eQl81vffZyMrkEsNhClLg2ZCltTP8QqVlmtFijqlnhyYBuBz7m0026b1syY2mN5Io5GEM6LE7vmGILPBOxHU-qaU3YaTTG5DYd1tuWOPB7LH3-y1OXSS6X5-NnybzFcooSFs4MgoOi07pv9U7B83ZN34P_5NVMCbJgC7yXveaZZmHY9cEs8PVcgBtE1NBuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=FkiV39buflsK8j9VdSLOVoj72yIUE0iR79qC_eazGTgc4VV84CP3wrxtT8pHh0-Bm4UB-SN1Nw5gFU_Ll53xYgJsyVfVq5qLC-15wk21zF9AK7rTGBhrxqQBYT8Wv0NqxHg9SDoGaJUPuaVAPazk2E-eQl81vffZyMrkEsNhClLg2ZCltTP8QqVlmtFijqlnhyYBuBz7m0026b1syY2mN5Io5GEM6LE7vmGILPBOxHU-qaU3YaTTG5DYd1tuWOPB7LH3-y1OXSS6X5-NnybzFcooSFs4MgoOi07pv9U7B83ZN34P_5NVMCbJgC7yXveaZZmHY9cEs8PVcgBtE1NBuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gswYk0n8XeohsFqwoIeEoMfvYjjnrPyfL1kagp3eJvjR_cVogPDUGVQTS3lBz8gp7sU0NtloOidTxg-cq0q2mnMlX2o9UqtoYJrkaZZfb7B3dU6GUFE2hzfGvQx9pe4b8gQtC2fWUi8D-le__Y5KcfQXiwlAK80mvNu-nVaW3OORyTL39XxPSHAQyqpxFCIwMykBHJ6-nLa6tCUyagwqyio8xbri4zqy_i5nLSDQJI6s1GyJ4BSlYLXs5X71eZKq-3TLTMwm7TYghWBcq1mqhksw-VWAHqZJh0QMEAXJXecctXOOzylYrQxlPmcyOhWyvofXBZcmFjcl9QiUyYZB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=EHe6BjMF50vnlxz0lnxcCV2DWpvI6waQFAHBUVNn86xxGkAWQuvePliJuDohpVXlY1Xd8auQlbH5ZUZND4po34p9YbWmt8pzleHR1JbdABdgqpnQPxb4CcTG6ry8hHDHWaA3ZINoHDmnujwmuSk4X9XlG76mIWayu1vWrt8YGI99N7FFJrjF91kj6GF6ymQCpFNivWrueMXoAAfMXXJIQsBEF-cN4FSRlJv9UY4ZDmS6wncwc6Wionoa2Xc6k_5Z5m4A2vImK6yxovmqix8G4F_xTAsWOfFQ1KAp7GtrEhDYXqSZpaC9GuWsqREGpFji1F0EXXiCLSMNUoL5xmTFSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=EHe6BjMF50vnlxz0lnxcCV2DWpvI6waQFAHBUVNn86xxGkAWQuvePliJuDohpVXlY1Xd8auQlbH5ZUZND4po34p9YbWmt8pzleHR1JbdABdgqpnQPxb4CcTG6ry8hHDHWaA3ZINoHDmnujwmuSk4X9XlG76mIWayu1vWrt8YGI99N7FFJrjF91kj6GF6ymQCpFNivWrueMXoAAfMXXJIQsBEF-cN4FSRlJv9UY4ZDmS6wncwc6Wionoa2Xc6k_5Z5m4A2vImK6yxovmqix8G4F_xTAsWOfFQ1KAp7GtrEhDYXqSZpaC9GuWsqREGpFji1F0EXXiCLSMNUoL5xmTFSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIlumo5U3aWwma7CsSj92KsckAt6cMIxzYsbwGEGIyMa6cOepwYAt8g0dRaZfjedILFUTtgKGqzSHL4a2zKnE-6iiqdTevoKFB1cRH14VPCTA0c4ZJPlsb8_Xka6aBwW82BqRrXppiDY9I_HmDopujVaZh_3dyOdoce4iHjJacnxAvIGoxzTG_-Fm-nZU4skuTRCIkVZyXefS0fW6i0Gvgv8fldWmpUCIuEdqxQkqN3nOvNh-thCMq2kj930PaFzUCKUYd3ClS_VUJt88JyFQLN-J4eGLE1-HTAjvSj2JkOfmShvqBFaeRT9jLJD454XbpOohtwHM3zD5LCW5wYwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnAZW3HI-n6lVgXPflM0faKQVljexFHfXpIJ1bBa8U0BVPo43fv9m-Jo2RFLFDR2ltSc7VM9Hb2H009TFKEe0WAwoAKnkAK_cTAQNydGpKOVmoOX0VNRHPL6PcO6DT2kYl-ifM1RWBGpUFU37o8HNoQdYQWG-2Ci0PRYu_PZ0mHM6Hw-j6YyfKhNWEgaiCPsTWfgShiOCHu4850pWZeU0N4Q2E9MYYVegxAbv3_Ey0CQt_LFPNwQQfUjpaLye6Slch8eRy-_7n_HFD2B4EF6QxS5qKVo9SIxxnucwzSF9sJYk4nzZzBCoDpHnU2fGHlQk8Zqm0Nxzeun48uPqoacoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=PD89Od112m5_9DIb50OZ6NVNKLQMaVDP8fQCvtbq9X1o8uPbWqGgD8waRrbTHV8yaoYgNm913iCqeF31DY4nDXL0n_PNcdNyzdyhuGykMj1_r_yfTNfXfcW2T_PBDxr5Uwi7YmsJbD5Ef9ashu_RlsLC0QWzNGGB9YxGQfLdyA33DWEe5pZ6q-2yBtRi9vAGH6jTQkD87-eE1Toq8AwfQbjYfrbTQCfjhg0TVzaeTsBIZ1cJJEJiN4qhzCOhlbVYY09p3oskJcwiz2HiahCBEqmjTTL9-2oVfjvWZ0SOTuq9LX3mY3zPFE6iDoP8ugTkG9KCFMF7e8zh8WoKyo91kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=PD89Od112m5_9DIb50OZ6NVNKLQMaVDP8fQCvtbq9X1o8uPbWqGgD8waRrbTHV8yaoYgNm913iCqeF31DY4nDXL0n_PNcdNyzdyhuGykMj1_r_yfTNfXfcW2T_PBDxr5Uwi7YmsJbD5Ef9ashu_RlsLC0QWzNGGB9YxGQfLdyA33DWEe5pZ6q-2yBtRi9vAGH6jTQkD87-eE1Toq8AwfQbjYfrbTQCfjhg0TVzaeTsBIZ1cJJEJiN4qhzCOhlbVYY09p3oskJcwiz2HiahCBEqmjTTL9-2oVfjvWZ0SOTuq9LX3mY3zPFE6iDoP8ugTkG9KCFMF7e8zh8WoKyo91kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=iJZMlmJOxpOLG3qDCpOyJDUy_yS_L2XP8rxH59XyuvK0-inZEwahWiG5enmZvI-HgDEV8ZmcIFkQX7YUH7f7t-snb_zS4M3bSsqHYf2nDi_EAYC1Tkq9S6jJoSdbwFmYweO6-WMrNi78jDeFf9MkEgAp5hwI0NdQh3AoF2wBuSno3_JD6nacXMFPj5dOK-QY29zR1PAP8mH7jOK2NlCx-1brNxpx_Hl11w8umySmO9l4TZaBVDfWIwRPIyqkuLZeO_7NZ8ERM9UBHJZC1DEMdOcrRnaRMOTDS9_bZdsuHrHWmY5AeuQL0koIrLH_mpMQZVPDNXAT-EstbJHgRE_p4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=iJZMlmJOxpOLG3qDCpOyJDUy_yS_L2XP8rxH59XyuvK0-inZEwahWiG5enmZvI-HgDEV8ZmcIFkQX7YUH7f7t-snb_zS4M3bSsqHYf2nDi_EAYC1Tkq9S6jJoSdbwFmYweO6-WMrNi78jDeFf9MkEgAp5hwI0NdQh3AoF2wBuSno3_JD6nacXMFPj5dOK-QY29zR1PAP8mH7jOK2NlCx-1brNxpx_Hl11w8umySmO9l4TZaBVDfWIwRPIyqkuLZeO_7NZ8ERM9UBHJZC1DEMdOcrRnaRMOTDS9_bZdsuHrHWmY5AeuQL0koIrLH_mpMQZVPDNXAT-EstbJHgRE_p4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=JH-59BNpel-cwMD4YrvjA1Wnb64yqSmNZZGloPzmTpWblugHxRbpBkSZ3Zc26JSpH7xNyCEu7i2f5iIDKQ9AJYRWjiKojpG6qa6MGEjuI756MwZwZSDG9D7bY8XjHECCF9FjYqixWAPXsRmUJLvieF5BzGHjdpNysnlWmn4ZyQ4-0M0ddcY4TJRh2a5tO7EEi2SzG4M6B2sz0nes4VUqtNb7tQ5jWoGz_J-1d9fCp57AaCrrgVUJRMIUzL18Ru3YCZvKXwX4P7xL3ykmXjFJstAkAmTOREMcJ2H6va1ptRj1YdIr5fcT1r3ImcytSDaLFsC0bZNPBgSWLiBY1YHOlT2E0gYVfebMj2WChz6ySt-efuBZm5LWQ5bS80RAdQsVqqaWJtdKndj1d7x2EUVYdcPhHEHDmCs5JAm_J5EDQZUnv5oFKY-Bl8VQ8fSfyioljcK7z0R65hYX_Q6HHBkyJI18CA7RhiIh5AeSCb-WlPqSPM0EytuJlAa8YB8IZYiJ0T-O-VtswzdhGtNZFpeiAWMNu8IWzrA-SUUxW9i33FzDCBZ3KbpLZRYAhCXFggsCjqJy4q6xQKeQD26Mj2sM0tB5V2qoBBeHuzZT6VUgJICOrkORk6IknjlR-A3AzF2yVrSqHJaK19YU0j4gpa560h8gwGlB4Dj3ymeHObzmaPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=JH-59BNpel-cwMD4YrvjA1Wnb64yqSmNZZGloPzmTpWblugHxRbpBkSZ3Zc26JSpH7xNyCEu7i2f5iIDKQ9AJYRWjiKojpG6qa6MGEjuI756MwZwZSDG9D7bY8XjHECCF9FjYqixWAPXsRmUJLvieF5BzGHjdpNysnlWmn4ZyQ4-0M0ddcY4TJRh2a5tO7EEi2SzG4M6B2sz0nes4VUqtNb7tQ5jWoGz_J-1d9fCp57AaCrrgVUJRMIUzL18Ru3YCZvKXwX4P7xL3ykmXjFJstAkAmTOREMcJ2H6va1ptRj1YdIr5fcT1r3ImcytSDaLFsC0bZNPBgSWLiBY1YHOlT2E0gYVfebMj2WChz6ySt-efuBZm5LWQ5bS80RAdQsVqqaWJtdKndj1d7x2EUVYdcPhHEHDmCs5JAm_J5EDQZUnv5oFKY-Bl8VQ8fSfyioljcK7z0R65hYX_Q6HHBkyJI18CA7RhiIh5AeSCb-WlPqSPM0EytuJlAa8YB8IZYiJ0T-O-VtswzdhGtNZFpeiAWMNu8IWzrA-SUUxW9i33FzDCBZ3KbpLZRYAhCXFggsCjqJy4q6xQKeQD26Mj2sM0tB5V2qoBBeHuzZT6VUgJICOrkORk6IknjlR-A3AzF2yVrSqHJaK19YU0j4gpa560h8gwGlB4Dj3ymeHObzmaPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoDWh_evF1kMq5PKl13txL_-0X9PO_m-qpqDwv7wOXsyNQFHFMRPth9cr974FHK6W_jJvUPz3jZ5BwJqtwKTHWGLuaKEeqJnupsCCC8smwmhbZk4MQzJHfkpAjTd6t2j5dCO-oV_R-u7DZ5ZEWish-nrFocFuwp6kd61wJ2SfO0cB_KDFcpzmXVl_xj8BBlQ8ZZpsg-Ri9OWpvPp4CHbwsigfJgbY0qhYBZGRnnxqylH4MYntpYCfyed7dtTdjFuJOir5WgQtJkU5daac0dP1sQIyMd1emNSaCfl72xgMu3P5NL3RArR8BO6q_XbKu5cXYUZufs7Xqy6yd482xx67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vm_eSLAjjHZXdCb04wJTQvq-uSW0gvDGctVQuXzdq2-J-IJ5mth3wEWbujRapO3D3sZIZZXA-aclxmLj0_jhbBOAkQUxGy23ViKwacMT1b1O5A7mmLYZNuTHRCSffkNA1HTXotzMwhIqmofCwGezA-8rfG9bM8mhUDnwTiZMEhmRLKCfyVG7r_7_B8hjD3EM39KmHmUkyud7Vx0L0EB51kxlGwFIbreohjMueFPYfs_dAvvboIM2g08_VMtUVleOBvleuPQ3raWtl2ryaEIwQDqI4EShPKz8WnrOsUqvv5c1BjvT7Qs7Lyn8c_rDA58hBzkmMdDnfApbp-qvMGU6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsChAtRkb39mCqGC8bRLlrf4HgzU_KSbNHxl0Gc576sK0xebeqFoYEaYlw8CICVgkNMMFEHP-2LkwH_CsnWdmUESL6gen2vhbwXkYmy6XZA2wn5nKPkBo8-p4mMbP9_4NLXMlduaZmeNJypFk1g59eFykuoKuMEXkA4TLvRT6FlNnIuhi42Whwv6ShK4Yixd3kj0s8fOQxTMYWKKh4JpVg-c4e_t8o5I1U5MZ3fdpHaumFQHnDzqgOQXS0dKFawqBfov-3d2g_OkkaMT45G29oJwKZw9bT98yOlF3pCoL--5-4HFPJ17B8F4mqBdaWqpC0ezjdzKlxqJeDdTClWhqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=UWqzWl4JvzTBxMXNcGBi1bXtm-2SNGiMwKBwb2nKfEupcDk7cM1nEZkYf9IOXj12p20EwPAJuR1uxigTOseF7ksrom2YtZ8vjlNlDa3D4WGXkWdFDmfgPUb-SATO-i_MJx7TG3i6bM5mqktPrDu0N_IOF6LEmQVDaL427CM19XpM9sFYO1WXM_PNNnEIQatfHK-Vs7Bta1hmGAwFWjfBokKSRDTwIfS2PUfrWLtajnZPcfkzlQ3XUapdu6b7aKPBWOlrFIgZDd70PfzPwl08grohjM6-cC0UywvgUW_L7vdgCM1ittOfvOuJJ4_0M1uUuvDCf50me0_4foq1Gxpky4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=UWqzWl4JvzTBxMXNcGBi1bXtm-2SNGiMwKBwb2nKfEupcDk7cM1nEZkYf9IOXj12p20EwPAJuR1uxigTOseF7ksrom2YtZ8vjlNlDa3D4WGXkWdFDmfgPUb-SATO-i_MJx7TG3i6bM5mqktPrDu0N_IOF6LEmQVDaL427CM19XpM9sFYO1WXM_PNNnEIQatfHK-Vs7Bta1hmGAwFWjfBokKSRDTwIfS2PUfrWLtajnZPcfkzlQ3XUapdu6b7aKPBWOlrFIgZDd70PfzPwl08grohjM6-cC0UywvgUW_L7vdgCM1ittOfvOuJJ4_0M1uUuvDCf50me0_4foq1Gxpky4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=k2CsesljzXXHrbp5UkPMAVdK38wNSFxzg9IenOdR2JvJUztMWCMKcnEcrG-v3GmA3AnTbFxdhi1USEBfxrvYzhhQcUxiDjeP-559jxFtx--ouWflXzXfT5ay9llNTfej0__sOm9HwILY9VabeGZUhsWsRkMa66iEBDRNuSSHjRfNL8-yXxxSMawV_jgZLtNBwzrcVGWIHZLoHmRVBRfN1MOklR7eVqBgkY97CD46Jj1YWVCpWa-EMw9wT-1bW0k-dyAiGSXLVS7oWO2kyyJ3LuJHLJ4KXlWNP9WWpcWyCHTyAdxlt-rDwOLBC29NOaP7VTPucNhtGtsTbs7p-Lytyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=k2CsesljzXXHrbp5UkPMAVdK38wNSFxzg9IenOdR2JvJUztMWCMKcnEcrG-v3GmA3AnTbFxdhi1USEBfxrvYzhhQcUxiDjeP-559jxFtx--ouWflXzXfT5ay9llNTfej0__sOm9HwILY9VabeGZUhsWsRkMa66iEBDRNuSSHjRfNL8-yXxxSMawV_jgZLtNBwzrcVGWIHZLoHmRVBRfN1MOklR7eVqBgkY97CD46Jj1YWVCpWa-EMw9wT-1bW0k-dyAiGSXLVS7oWO2kyyJ3LuJHLJ4KXlWNP9WWpcWyCHTyAdxlt-rDwOLBC29NOaP7VTPucNhtGtsTbs7p-Lytyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=qGoa1dugHgtV2DtC6TDzMuNKmO0OKe_Mwvswez5FMj6pvM9tIIbzFdNdoi8pSn0tcv61gPwZoMSyVxNQqQws8yx1H0hyqLUF3eMHhY8Qx1Lp-VHTp-z9iRRMEIA2av0zW_HqvVyD9txUKXReL9GvhsTiPVKzt_57FaXDBANF6YaZvlTsSzvH3o-nJ0EX4q0YjPxfMbCsdnR0Ig15VmSjI799fjxWPWvtM7xQBpH8ABqJVhypgOtJsZ3hSKKLVx495D_Zih3U6OyzgoBBHo--u7Cfyj4yiPW-Ahlu1i9PnTr_hxlZOJt11ZFGLQ_zMk46571NomCb0mEaTjHOvxSGFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=qGoa1dugHgtV2DtC6TDzMuNKmO0OKe_Mwvswez5FMj6pvM9tIIbzFdNdoi8pSn0tcv61gPwZoMSyVxNQqQws8yx1H0hyqLUF3eMHhY8Qx1Lp-VHTp-z9iRRMEIA2av0zW_HqvVyD9txUKXReL9GvhsTiPVKzt_57FaXDBANF6YaZvlTsSzvH3o-nJ0EX4q0YjPxfMbCsdnR0Ig15VmSjI799fjxWPWvtM7xQBpH8ABqJVhypgOtJsZ3hSKKLVx495D_Zih3U6OyzgoBBHo--u7Cfyj4yiPW-Ahlu1i9PnTr_hxlZOJt11ZFGLQ_zMk46571NomCb0mEaTjHOvxSGFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=XSAIBahHmABmFnWgcGCgL3Cm9QKbO97frBd2iGvqrpSayKsB0Q2AZcZa0rKdpVbi-YZs5jB0puvr5C31yjghlOY23WQbtP5YEimnrO7Xf-flYPpMP3z5vRWYJ3oiMkjI-VMC5P_UpK5z716fL6OI_KZaTouj-DRLM-S6FUOQUWTKAC18laVhdTBkhTf3C5xvP3y4laiEtSDunsHg15524f5UyHUkcB1daPn3KF0DZQWN0htT0vzkpnhuTZL5OVGoxlLGLhq5JMJHmeFBxwaIeM35FEbBFkhuFs0nSnzPJloVY1r0EbvUvh5QfdPkQk_WIlXlZBQXwBAo_gcKpbCdkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=XSAIBahHmABmFnWgcGCgL3Cm9QKbO97frBd2iGvqrpSayKsB0Q2AZcZa0rKdpVbi-YZs5jB0puvr5C31yjghlOY23WQbtP5YEimnrO7Xf-flYPpMP3z5vRWYJ3oiMkjI-VMC5P_UpK5z716fL6OI_KZaTouj-DRLM-S6FUOQUWTKAC18laVhdTBkhTf3C5xvP3y4laiEtSDunsHg15524f5UyHUkcB1daPn3KF0DZQWN0htT0vzkpnhuTZL5OVGoxlLGLhq5JMJHmeFBxwaIeM35FEbBFkhuFs0nSnzPJloVY1r0EbvUvh5QfdPkQk_WIlXlZBQXwBAo_gcKpbCdkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsfiUD5qdxVd447MiYojN4XaRQaGFBQB8jxvud5ibCUvVP1dGUXojvyzixp9Ecn4BTNDHzdDsup7a_D42AxfvqWsZyd7niZ0rUaqRQpj-ew-sdzeEiz4i5lkxaiRlPcKPHZYcptXmqL4pNoOQQRx2p1ZV3IuU1bHq_SSXQzBGaQYXzDeaneHTSkWCfvSk_qvK5_x-rz3hkad9FNpl-jedy1sfzfi2gNQzWXRZX08QpiSTLe4QLwDqdJmfOOLhT8F6Tj0tWsO78Vmhv3aQz8K4dUib_c2zzvHGH7v2SjqH5rcN5m1H7h0_5YvtvsxR_Ny96wFahtmACmNMT2AJmNxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=ihox_mVxiEDRHBxH3KdX6jvBR8n26fZxcxkB_ENGe5M_4tZBJWnnV60ctwpKl44DkeykqbKVe1kxhcaONhvOlj0DFER-bsYAwGwpA_NEX8yMSSes7dgBKrybuWlSRz1eaQvjC-6qbQY1NmeFCXqvU4hTWH77Kjzn5XN4c1_urKJnZTBoWgKWgX3EL8i0DNHqKQGNho4AjBfVg_VUwZ_rOqoYFQm33WPcXxfneMi_y7d2Lqx4kkHaqmXygKulpLjd2ztGmrHWWGUWnKMqnkk6S7Cciy1CU0Ccw-MFJlNYP3u2iWVjhks25xwvz_nb-mgkHfbs5gFBOBqLek_ldmAsuLd-xOOD2tAFaQUbNVDa-bQB1n8nyxPXdMa-8tUwypHJ9XVnlRpCVa3013eThCVuCya2_iuaPO3y6VpR5GblDXWJ6Ms-TzozSK3xNaBIZsePEvnNMETs1Z9acV5LzBcurTkgF9lHnvK4wtFUgeTPcpqn6p2JHMCdn-2Un-XCP1eTRD3WjPUjS7egno7O0mLkDGPwOwfnoKbMQOH9mmzIluqrdEgxzbzUFWrZv-ncbG57U4LR5T8MHlaj6LL7BlbMrnfnKeYd5xgG2YuMPI1SZRt97UmMwZwZZAwtHfB3H4IWGvxjkI_cF5CTGilp6CwWYDA05cz_lCBBmu0hqjUTZ8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=ihox_mVxiEDRHBxH3KdX6jvBR8n26fZxcxkB_ENGe5M_4tZBJWnnV60ctwpKl44DkeykqbKVe1kxhcaONhvOlj0DFER-bsYAwGwpA_NEX8yMSSes7dgBKrybuWlSRz1eaQvjC-6qbQY1NmeFCXqvU4hTWH77Kjzn5XN4c1_urKJnZTBoWgKWgX3EL8i0DNHqKQGNho4AjBfVg_VUwZ_rOqoYFQm33WPcXxfneMi_y7d2Lqx4kkHaqmXygKulpLjd2ztGmrHWWGUWnKMqnkk6S7Cciy1CU0Ccw-MFJlNYP3u2iWVjhks25xwvz_nb-mgkHfbs5gFBOBqLek_ldmAsuLd-xOOD2tAFaQUbNVDa-bQB1n8nyxPXdMa-8tUwypHJ9XVnlRpCVa3013eThCVuCya2_iuaPO3y6VpR5GblDXWJ6Ms-TzozSK3xNaBIZsePEvnNMETs1Z9acV5LzBcurTkgF9lHnvK4wtFUgeTPcpqn6p2JHMCdn-2Un-XCP1eTRD3WjPUjS7egno7O0mLkDGPwOwfnoKbMQOH9mmzIluqrdEgxzbzUFWrZv-ncbG57U4LR5T8MHlaj6LL7BlbMrnfnKeYd5xgG2YuMPI1SZRt97UmMwZwZZAwtHfB3H4IWGvxjkI_cF5CTGilp6CwWYDA05cz_lCBBmu0hqjUTZ8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=snXrXHK_ZhP1JOXuRvqjoloppEZppndZLwwyjV9lNY38LdKoWU1ywdemXcudDHJ1f8jU6eIlsSCEP3qQ3ggwep2wyegp-M_byQ78O7LemNJneUhsC1hKe1OXrFni6uC-Hxz6gap5dUHxIV9rQkedqfkxzj2ViB767WLMoB5owGK0IBEykqituS-yxatbfJaRrk9blMSdPrOqIV9HHaq-oRS-wK5jT5aaI7-1J9VydKgrjlrFqtxHlXhsNOYG4ydD8fvOVtF2CX0EbDbiDvLDZIaq6YswhaNLTCS7wkINlyLhJTZ2KYJHVuAKywH2YSt9YBLMu0V3KjjMNRssy_6h8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=snXrXHK_ZhP1JOXuRvqjoloppEZppndZLwwyjV9lNY38LdKoWU1ywdemXcudDHJ1f8jU6eIlsSCEP3qQ3ggwep2wyegp-M_byQ78O7LemNJneUhsC1hKe1OXrFni6uC-Hxz6gap5dUHxIV9rQkedqfkxzj2ViB767WLMoB5owGK0IBEykqituS-yxatbfJaRrk9blMSdPrOqIV9HHaq-oRS-wK5jT5aaI7-1J9VydKgrjlrFqtxHlXhsNOYG4ydD8fvOVtF2CX0EbDbiDvLDZIaq6YswhaNLTCS7wkINlyLhJTZ2KYJHVuAKywH2YSt9YBLMu0V3KjjMNRssy_6h8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aa2ueEgY1QHWXJIXklPtZRUx6OxAAeF-Z_VavczvwZGUOf4zpmSX4XBjuvpf7a4UIecyL3KKYW0m_YRiO6ViPsUTXQKJpUHGJCJjNTTjXVDPJSbJrM4WcHW6QRqJJzczE5kzBt3Q8NTmMYpPcelEq_vYY5w1zZ7KJgnRoxbFd5Mp4dIPQ2HvQYPgbC-44tYhiLT8adqhlgDM29PqbqjKUraYeFTlDsMPJEGqfVAJBXWwT-v-1Jok0jbrAheO3_E7PqGJQilh8mpgXIlK9Qb3rMeMjqUo5sw6A_edHtPjLpUSliRI6J1CqxDjUa7QnDdGV_Y1IJ3jLLBdmkvU48jO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=j8EbhIlkkve4ABJd9R0zvuLdAAyvmHJ_ekeN8uLE2mvTZXxQOJjWFRvSJPOPsVB0nKxFlsgQKIgl6ZCoe7w_aG04_NTlnYpArisv2mCGfoR2JKLWs8kmnNCOmdUHVC1jdqWoEbTS9VbYVu1J62OdQuPKbcdSaUcI9N5yaI5ZccBC2pNZuIGWSlp6YuSykJuwV-h-H_VJ_2hZ5fGB8HuDSwl8xwLlKIV8VyIrHJmSc8POBR_SZJIVjlZ1qDASBt-SOcuhHR3iSrOY5XNjgEpFbv0-s985Nq3RzHpVkd9UeVRqbfeDk_gCjVoIY5lGUAJzWTrN7ldHAx5aZmLX5DDHIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=j8EbhIlkkve4ABJd9R0zvuLdAAyvmHJ_ekeN8uLE2mvTZXxQOJjWFRvSJPOPsVB0nKxFlsgQKIgl6ZCoe7w_aG04_NTlnYpArisv2mCGfoR2JKLWs8kmnNCOmdUHVC1jdqWoEbTS9VbYVu1J62OdQuPKbcdSaUcI9N5yaI5ZccBC2pNZuIGWSlp6YuSykJuwV-h-H_VJ_2hZ5fGB8HuDSwl8xwLlKIV8VyIrHJmSc8POBR_SZJIVjlZ1qDASBt-SOcuhHR3iSrOY5XNjgEpFbv0-s985Nq3RzHpVkd9UeVRqbfeDk_gCjVoIY5lGUAJzWTrN7ldHAx5aZmLX5DDHIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=RbId-qsS3YtNkoF8aQ8F8LpCCyTbUrQBCdA1ow_aPUxT8cFbaV4k-PxnwH9clVR2CMyObBFBVH6i5UC4zWdnvtMZkTWZSh9G3T3ErpDrRYXUmOrkRz39TsJlFaPw3sAavKvhZnYbAtjgnAlKog0FESdmGcbfjpmi7jMFYuWA-qgPc0G7_4TDtiqIDJLCJ3dTpKNF2bXmZmSfbzrBH9iDOfjRG14SmWv5jDcLZ7e1GvXYLJzWvT8tLPFZiUE6fKD8k83h1lipj98bsCcBemik7HognRYwM1rYO2mKEstkZDvrboxGRlqRLV9bF88FQPWZxPvOVYpeezrtXvHwlIuEvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=RbId-qsS3YtNkoF8aQ8F8LpCCyTbUrQBCdA1ow_aPUxT8cFbaV4k-PxnwH9clVR2CMyObBFBVH6i5UC4zWdnvtMZkTWZSh9G3T3ErpDrRYXUmOrkRz39TsJlFaPw3sAavKvhZnYbAtjgnAlKog0FESdmGcbfjpmi7jMFYuWA-qgPc0G7_4TDtiqIDJLCJ3dTpKNF2bXmZmSfbzrBH9iDOfjRG14SmWv5jDcLZ7e1GvXYLJzWvT8tLPFZiUE6fKD8k83h1lipj98bsCcBemik7HognRYwM1rYO2mKEstkZDvrboxGRlqRLV9bF88FQPWZxPvOVYpeezrtXvHwlIuEvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNzm8jNcTF8xmbFIe0_51ZUOsittUuviJMT3usXuM9dkEscbOwNg-SJMSF1S5y1VKNZVZyRA1QSnBbI356DXW1csp4xnNWU2vVP8qIL7X4F-EsejQ6bahvRX_2Brkz8znvSSx_zumWiYUV7tbszIamnOh68RMMlQH9auoaELRlA5DWtkBNwM7iTyduEFiJkUEMQqJ5XSPmxNOi4w9h_sXoL_v77vu4ePDUSrFCGtlehKKhxx2a-9yUCHLr8I3VUpsF8rS2RYfgfHdKvTnGEV1x-dcotg4wpF8CmDIblwA-zJKkQyxv46XcsLfGqRrirMtLcv5NSd3DDqu3cMZnPS9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=XfAVnLVu7Cyrbxdl-gWCe5W2V30xGzsIpkHxl-hjJX0URwV2BshEYJUNHvK-fAVkTbyTEOKPRxiGBIe-RPo5YL315OjP7TEJZUXy6WReTzWbLLoidRUSyjDglh2JimhZrS2l-8UTFMy_IILslE-Y7pWplaf9cPEB88-juzDnNpSCeyHrQxiB_tkwgKU0nCeLOhXYN52R5rHQZrSmwbHzR0fWh0rdTHAXIcAVIElcEH6AC9KFqDpQYUU6ZbCpkh8BL21CBpYqc6CNHPMqxz0kGkh61Y9sRYAViA5ozc6LCZBo8msFZajjh7pzAwJKf-oz3DJ3LzKiTyQokEykYee6IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=XfAVnLVu7Cyrbxdl-gWCe5W2V30xGzsIpkHxl-hjJX0URwV2BshEYJUNHvK-fAVkTbyTEOKPRxiGBIe-RPo5YL315OjP7TEJZUXy6WReTzWbLLoidRUSyjDglh2JimhZrS2l-8UTFMy_IILslE-Y7pWplaf9cPEB88-juzDnNpSCeyHrQxiB_tkwgKU0nCeLOhXYN52R5rHQZrSmwbHzR0fWh0rdTHAXIcAVIElcEH6AC9KFqDpQYUU6ZbCpkh8BL21CBpYqc6CNHPMqxz0kGkh61Y9sRYAViA5ozc6LCZBo8msFZajjh7pzAwJKf-oz3DJ3LzKiTyQokEykYee6IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsnRsqiNiqytjTYD1ZWYQTWH2pxNOHRAI17dkquZZscmq6mSaWHp9HdyeK4bLg9h2Y_Vvw1CdWP9tkeSLwX8aUFZWzV_X8rWj0n5KoGQ0XrPuUPTr9VGaYU7HtUSvqCfbCVTXqPmWVKz_5hmxvH8e-4xmuWmvbRgr6lCX6Ix5XxiIb7d61gGUpw6m6unsL8_w6d8i3s2WZDE2UFSjJFCSdAIdI59L-kvSVEW8A6kMTpwveUZVP846Fib6zUVynE58w4_NMvtbpt89J26_U7wVo_yJiYI1QvC4b7lc3mgs6U4GuIF4MbJdAPH0EIXAYFP5_opGAl_4eTkw2mazKYWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=OPZm2iXDdllXs3IQ_q88xBN_GmYNlkXVcGsqpjop_okiVvYm71dTExsxEOdqtb8wscjxjDJZwqNtZRQ_T1a4veZsFw-W_EhWL0gUZvcKjy1IYtW_d3-7JJgCsZlMKbX1xG9ixFcqCsAN55EFWBTihQTBsnpuOZl5MfZ3yylnhyPeroaXBLVZLzW6lnlyqg_EhPryQ0jfZPm_p5lWF5GdfCJf5CpL1M8re-aZ6etZnAaaR2tOobbeyFEyrFtXM2SEen27z8dHcGkdbz98fPxC0ZCEdWEtlP4PdSYIMYqSObMbYkZzQirZfs-DCrI73k1qXBoRM2QDYEgg3j6fTww0dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=OPZm2iXDdllXs3IQ_q88xBN_GmYNlkXVcGsqpjop_okiVvYm71dTExsxEOdqtb8wscjxjDJZwqNtZRQ_T1a4veZsFw-W_EhWL0gUZvcKjy1IYtW_d3-7JJgCsZlMKbX1xG9ixFcqCsAN55EFWBTihQTBsnpuOZl5MfZ3yylnhyPeroaXBLVZLzW6lnlyqg_EhPryQ0jfZPm_p5lWF5GdfCJf5CpL1M8re-aZ6etZnAaaR2tOobbeyFEyrFtXM2SEen27z8dHcGkdbz98fPxC0ZCEdWEtlP4PdSYIMYqSObMbYkZzQirZfs-DCrI73k1qXBoRM2QDYEgg3j6fTww0dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v--oo-YiNuq80l9fBXqT5TUAt2yEZtwoj71NN7tePzvWEm7sjhzLHwTP1PwNpoJ8rPHVGmen6HidUJEzDbyAdsK3YZoJWdF3h4FZMbVqkltVuLDNCst8AOmfi_FFP55M-H9q2e7cLWRaQQHHlnC7YSnF72dZLdPEoUsNIAiLOp6ow0GzOqyimH4ZGuiolxHns7ilhkkrwwCqzzDioM0wAUwPerwZDLWBYiXTmMaiFbXJ9qJt-MQJRfIlzFV6pDzHO7_fZAw9yUkXlZKVWv3vfdZEpD9J2dMV5V5Zt49pZBA43iGMB2Go_UgklHRGd5FGaDbDAj44UBn0h85gZm3W_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=hNFvIDY6-tDJ4R3NBrGCV3XkSyZwbw5O3ONfUf31WV6Tuv9tUxlyomsny47VmNPTS21ZhMMG59mktL77xAnRIagz7Nngu_M6PSZBGOV4qoBzUZgM8uriPkrpIYQpZSmqmZyOHkM-u68TBKMahD9u3PZmGzNDrSJmu6lJMvlTPyCuD9I260hjIP9PsDd3v0fmIF6xJALMpfpZFBp8V-SaPgIjrWBAZBrCuEF7zWOqh35fIfwQYi1Ptgbe74rqti0zyoW0Gifwb26qpcK16yvEsUUbmGaW2dNZZIya0Fk6c93unGLYMgI0v7Nbk69Dfgf_mrJx_eyW3icL-VilScxAEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=hNFvIDY6-tDJ4R3NBrGCV3XkSyZwbw5O3ONfUf31WV6Tuv9tUxlyomsny47VmNPTS21ZhMMG59mktL77xAnRIagz7Nngu_M6PSZBGOV4qoBzUZgM8uriPkrpIYQpZSmqmZyOHkM-u68TBKMahD9u3PZmGzNDrSJmu6lJMvlTPyCuD9I260hjIP9PsDd3v0fmIF6xJALMpfpZFBp8V-SaPgIjrWBAZBrCuEF7zWOqh35fIfwQYi1Ptgbe74rqti0zyoW0Gifwb26qpcK16yvEsUUbmGaW2dNZZIya0Fk6c93unGLYMgI0v7Nbk69Dfgf_mrJx_eyW3icL-VilScxAEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگفتی سران فعلی ج‌ا آدم‌های باهوش
و منطقی هستن، چی شد امروز گفتی
که یه مشت بیمار روانی هستن؟
ترامپ : شناختمشون!
و لبخند رضایت مارکو روبیو
[معروف بود که روبیو ج‌ا رو می‌شناسه
و ونس اینها رو نمی‌شناسه،
ترامپ امور رو داده بود دست ونس،
که الان ظاهرا دوباره برگشته به مواضع روبیو]</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqq2WcwK7P1GUtC892HLp1w0gQWSQopHJJX6Lihnpg7EElMqWntyb5fIkJFnZU-9xOPoBSezxIs-LKcVR1ky8LmfLiY5JLVzp0EqITXMXET2XQ1Kd9TbAC6MgNPD6fBWiwtBxiE3IW2w2mL1cf-Dtp1V4TsBfXwZaVh8BakQ84mtPqkuDH4IQ2-mWrtmMTMc-KEgJqtWnpAYEohzqDjp2smQqUdXH-iwV2J5HEVsioUTRhf4l_qJ5fEYj3j4oMT-Ad5TOD9_uGoPJ32xX7OPmCCVph3urgeiGJoTW1okHs60zAkbKoRv1_WLUBDn8FtOIjmOX1H_e5o63OSMojULB-sE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqq2WcwK7P1GUtC892HLp1w0gQWSQopHJJX6Lihnpg7EElMqWntyb5fIkJFnZU-9xOPoBSezxIs-LKcVR1ky8LmfLiY5JLVzp0EqITXMXET2XQ1Kd9TbAC6MgNPD6fBWiwtBxiE3IW2w2mL1cf-Dtp1V4TsBfXwZaVh8BakQ84mtPqkuDH4IQ2-mWrtmMTMc-KEgJqtWnpAYEohzqDjp2smQqUdXH-iwV2J5HEVsioUTRhf4l_qJ5fEYj3j4oMT-Ad5TOD9_uGoPJ32xX7OPmCCVph3urgeiGJoTW1okHs60zAkbKoRv1_WLUBDn8FtOIjmOX1H_e5o63OSMojULB-sE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrMJS6u2EtPyOPEghVJupTEaKO59NrCVA5ZwwMm0D_cFT-vZYnLMn7fDcnr98kFoewpynJiUOS0Z0apy0cgE5rX5Km-iMjkB9gOczyHLt09sQn5uy8fxJwy5qdjQNZji9KeuK3go6AJfzMx7XUW6at_rfaSuOP-o5l4BIPvkBYalS34eK_o1uTIgKt7UitKQP51u_H2y64BvsPwz9gyYbsiZKJbAsx3ep2Zp5n_KrqoinN89cOzaHoj9-YssUEttaXMRBE0W_vmta55uMNNlpEvwnU_o41Pijd1tzVytf2QDEce8jM19wsydii8qonoqMkrICewPVl9h6u-9Jpsgaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=NHKnTmMvUfzGEWyjH6NrkNHSb0ZDjXwvkvIafawYPxZcE2qUI9ut6gTvXByegqUU8rfoMulcyNYskH8mnoeYxx8PGfQTQWFlNPztrzc-ZKVARkVCzJJTUSF6FR69qi4thZLNaTixtJIPTWmhtXeIkYGgnt3fuIdPWLtJ9FmeRPu1I2zfAGnt12qU1qNTXwJN0NdwaqjBPkWX_z7hqFxqBSkQmssF8j-0p9A_L05AdKR5wkRClOAvunRGKLJvt4Z2A36oq8GSynPrq_6tVgydY4io3lsDOF01GH6WHc3JY6JoKnSUpWsdmofQVOv5oeB7Ria-ng2AB-s0iU_aJUsZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=NHKnTmMvUfzGEWyjH6NrkNHSb0ZDjXwvkvIafawYPxZcE2qUI9ut6gTvXByegqUU8rfoMulcyNYskH8mnoeYxx8PGfQTQWFlNPztrzc-ZKVARkVCzJJTUSF6FR69qi4thZLNaTixtJIPTWmhtXeIkYGgnt3fuIdPWLtJ9FmeRPu1I2zfAGnt12qU1qNTXwJN0NdwaqjBPkWX_z7hqFxqBSkQmssF8j-0p9A_L05AdKR5wkRClOAvunRGKLJvt4Z2A36oq8GSynPrq_6tVgydY4io3lsDOF01GH6WHc3JY6JoKnSUpWsdmofQVOv5oeB7Ria-ng2AB-s0iU_aJUsZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=cfreu9PqfjAR76mPf359KDnOS7vFglZyDjKNr6dfJEoZgFFvvzkdXIS3uVAI_vOywUPqcqCuumiGUnqxFH6qqPGsZhksR4pcusOabvq6oSApgu4rABce3QTpRVfHwUYQlRGRv1olKzW-5pBYiVIUAPiTR8fIhG6e07f041D6zc2kwowpmfIaaN2Xr29iApuzoAYJiw0-xLawlxn8LerBM0K8ZSK4dQYh2sN7Vo9zzztv6UJ790y54ElvSCksF4WasTFTIekZcMLK1jDDFVF_oORk7ybW4pU_4a_v4eaYjNMPHH-i4HnpjPlTGvim57ar8e1fe4OYPMTfWazT-YchLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=cfreu9PqfjAR76mPf359KDnOS7vFglZyDjKNr6dfJEoZgFFvvzkdXIS3uVAI_vOywUPqcqCuumiGUnqxFH6qqPGsZhksR4pcusOabvq6oSApgu4rABce3QTpRVfHwUYQlRGRv1olKzW-5pBYiVIUAPiTR8fIhG6e07f041D6zc2kwowpmfIaaN2Xr29iApuzoAYJiw0-xLawlxn8LerBM0K8ZSK4dQYh2sN7Vo9zzztv6UJ790y54ElvSCksF4WasTFTIekZcMLK1jDDFVF_oORk7ybW4pU_4a_v4eaYjNMPHH-i4HnpjPlTGvim57ar8e1fe4OYPMTfWazT-YchLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKVRKzrhLFrv9W30tKiYWIlhq-B73Qebk9ujxzUw-Fik_-lnPCDZP9vNgLnoKH9U-AKdjsJYYHlXKjy5ENrb3qPwyr6id43KBy2IjInXS2nfRIVWjhtlTgdxuY-8fRkiy3R7Y36Mo1-jv4uf2bb8gqCinSeWJR9UGdSBjYJbS_sgMog86RrlDerh3O5xAh4tqTmXVuka_82xBdZuQgWl--epIu18vklLBUVEH1PekjeW2twCSprqojnXOW2R6ljGpM5sVCa9IvoNhK_vBpwGQhafQjYmUWB1VIFJEOKWqBj0WfyDK_GOOrW5RAXPvWN6lpDPJ32GvASldvln8qbBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=MtfuO0m5lgkMLiGfQsEBTU1j8KybWM0glLEv3qmpuhEirBF_XAjRfPRR5-73AX0y9KT1fJFcgDqya1z4A_prll5_OHlvTzbhqW9tGDAJf1b2Jx2J-7Aa_lN-0OJh_VP_0dnbKsl-NfjEALJPkCWXZKlE8-xv48k-3D8xhVecN-44ii5JcPWcfuO1gWnBXBHrwoONsPIXN6wqVJsmAiKDuyWdYG-6t3lMi9WfkvE9OhydLTBjGVW6SZHn64eDxyXee29s-Gb2i7I9myeL0E3L4jlRsB3P28aYgHMXxCnqnzy0rrOTv-Ab8p_-CRHMMlBBFqaJ_9aNpQpe4jLVCObrBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=MtfuO0m5lgkMLiGfQsEBTU1j8KybWM0glLEv3qmpuhEirBF_XAjRfPRR5-73AX0y9KT1fJFcgDqya1z4A_prll5_OHlvTzbhqW9tGDAJf1b2Jx2J-7Aa_lN-0OJh_VP_0dnbKsl-NfjEALJPkCWXZKlE8-xv48k-3D8xhVecN-44ii5JcPWcfuO1gWnBXBHrwoONsPIXN6wqVJsmAiKDuyWdYG-6t3lMi9WfkvE9OhydLTBjGVW6SZHn64eDxyXee29s-Gb2i7I9myeL0E3L4jlRsB3P28aYgHMXxCnqnzy0rrOTv-Ab8p_-CRHMMlBBFqaJ_9aNpQpe4jLVCObrBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=qBOBU_wESj8DDRixdLQK22yhddHezmrUQ6fP99NbN7HhAKUNsmvTfGCpCqLvPa3oXqbiGWhnwUDTct_kEFuJT_jfRshofclXbiwjxe5pibhBsKnkIOoW20n06vdJ55wpBwaAkqpfP2NjW5tIFttYNeOBryX5TKRFx33bve7tDeg1-z62AJ5gHDzszyurPuafdeJ6Ki_dcRXDXu_s1c8W998rAw-aNMGcRPYCOtz8KvRi4R0ua3TSb2WY0TGGXdvQQc6Pfw7bBg7tS7cREadFq67biPyfQG6jCZosPm399nNgxG8kVvvMUHFMJMuFI-EjntLmfwVvIjD4Be5PmiqHMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=qBOBU_wESj8DDRixdLQK22yhddHezmrUQ6fP99NbN7HhAKUNsmvTfGCpCqLvPa3oXqbiGWhnwUDTct_kEFuJT_jfRshofclXbiwjxe5pibhBsKnkIOoW20n06vdJ55wpBwaAkqpfP2NjW5tIFttYNeOBryX5TKRFx33bve7tDeg1-z62AJ5gHDzszyurPuafdeJ6Ki_dcRXDXu_s1c8W998rAw-aNMGcRPYCOtz8KvRi4R0ua3TSb2WY0TGGXdvQQc6Pfw7bBg7tS7cREadFq67biPyfQG6jCZosPm399nNgxG8kVvvMUHFMJMuFI-EjntLmfwVvIjD4Be5PmiqHMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=h4h_LlFfIm0Qfnu-lTGxGNzHMFTHP9DoavufQgwUI3K6N8luJIwHpo94IeMifE4CEqUQioDtL8cxSk7hyIC5RGTs4IlmSyzMaczLvyfbG_pN2nymcyf7Rf1d5NCSG9rA4cF2dX6WjS6A59lk1i3b6h2jmN6fXgsdk-VtTpGQyJz5TjmphJqsz3R0OF5mc6FWJ2g6lqErMioRixRvhybh_HyDcDkOGZgJpMiPzGMhK2yFKlVGmWcgAugih-RPxFDxawuUdRmR5QPF5L7tjjmO7msQxa1fXTWpEsCAOOKZHZGccLdRaIhnVZF3FLP-fEOW2z8cpD2vYnGhFw-s4QL19w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=h4h_LlFfIm0Qfnu-lTGxGNzHMFTHP9DoavufQgwUI3K6N8luJIwHpo94IeMifE4CEqUQioDtL8cxSk7hyIC5RGTs4IlmSyzMaczLvyfbG_pN2nymcyf7Rf1d5NCSG9rA4cF2dX6WjS6A59lk1i3b6h2jmN6fXgsdk-VtTpGQyJz5TjmphJqsz3R0OF5mc6FWJ2g6lqErMioRixRvhybh_HyDcDkOGZgJpMiPzGMhK2yFKlVGmWcgAugih-RPxFDxawuUdRmR5QPF5L7tjjmO7msQxa1fXTWpEsCAOOKZHZGccLdRaIhnVZF3FLP-fEOW2z8cpD2vYnGhFw-s4QL19w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=MT_d_ScRPe9sOP5Wr4KQLrJn-5HlXGI4N4Ra23TpVexDW34mdm0b7GOWOxGQ8qkDMpnt5Bqz0_tToCG2q6Y3bIgs-d1oBKZh_-R8XnYM2nwAof5riJQCNTOMKnuSlqf-UozoZNKlN-ov5jl6kg-dUvx1SaoUoFv1nh7J-lYVG0yG-qvZxNn0vP-qglcPwvz1Bf0LDVMCS9E38Ia5AQy9u58zUiJtM2MgBJnyqVqPdjIOwI2oUXBE7fJIj4QgiaeeggB-MKO4VbpvhiAr2EAQVIcsVdEndPAvYmULMROa0ExeAjEUt1MBnzQ7f4VT6FeR3LV0xF1qX5vzXQiND-4_bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=MT_d_ScRPe9sOP5Wr4KQLrJn-5HlXGI4N4Ra23TpVexDW34mdm0b7GOWOxGQ8qkDMpnt5Bqz0_tToCG2q6Y3bIgs-d1oBKZh_-R8XnYM2nwAof5riJQCNTOMKnuSlqf-UozoZNKlN-ov5jl6kg-dUvx1SaoUoFv1nh7J-lYVG0yG-qvZxNn0vP-qglcPwvz1Bf0LDVMCS9E38Ia5AQy9u58zUiJtM2MgBJnyqVqPdjIOwI2oUXBE7fJIj4QgiaeeggB-MKO4VbpvhiAr2EAQVIcsVdEndPAvYmULMROa0ExeAjEUt1MBnzQ7f4VT6FeR3LV0xF1qX5vzXQiND-4_bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=kN8gbAzjo4gCjsg7wTuvVMwRJ0qL0zJ7ygGNzRI7cMK3jJeSFvm0yw7okKa0BGlLNWZydTOZ9nd6JRtpWeD6wBsmHPfE6ce44veJ80oR1EKQuvnEqbCmrOhOe6uxOTwlf1dsXE16M-9BETjtafrFOGHvurgR07mXqJSBohSvgHuXJR4O7RHAvZ-AdoBtUtqCdAZiTwYNm78PjdVUUoPahbWGEpZdi7-6a1PZ9wLxIY7QFYPmiGMe4vWI-TltXhUP-5L8dUCYNrQSqBAuEgOUTV_9jsqcNdi3bIGaC6SNKMXPRt8NJTzrjXYDMaq3pEKTQ1DU1VAuQfRuHZqFI6Wr2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=kN8gbAzjo4gCjsg7wTuvVMwRJ0qL0zJ7ygGNzRI7cMK3jJeSFvm0yw7okKa0BGlLNWZydTOZ9nd6JRtpWeD6wBsmHPfE6ce44veJ80oR1EKQuvnEqbCmrOhOe6uxOTwlf1dsXE16M-9BETjtafrFOGHvurgR07mXqJSBohSvgHuXJR4O7RHAvZ-AdoBtUtqCdAZiTwYNm78PjdVUUoPahbWGEpZdi7-6a1PZ9wLxIY7QFYPmiGMe4vWI-TltXhUP-5L8dUCYNrQSqBAuEgOUTV_9jsqcNdi3bIGaC6SNKMXPRt8NJTzrjXYDMaq3pEKTQ1DU1VAuQfRuHZqFI6Wr2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzFcp2lHGFKnDAXhUDkJSNjbJCmBAtZ9T0LqTLZQ3HjIRu40j0VwYyIHN-CZhasl2nO7DQR-vz_L-hNXIxGUL41x35L-PqX9TzBJYWaKB6S_FTpgW0dOpuRYNP-DOyFLc5JJsJrcYW4f-bX7dOwL8n98nQ0T7Iu_nMIvvg6sIv6q_jMGO8PKHJ7fNSCeBSAdTGWuXryNiHwmiknmU29cvwMeWeFR0NjCUPLS8-5Dc9DUzVMAFB0_rWUimIUdNVphFaYtndBV3V6IuypinIuiTQJfIvNSrNK08LuzIVcdnVwTresTT0I79idJBPTexgZGT6206U7WkcdTtQt2ySAhhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhbJ7YANEwAb6bGdbywBmQUzh4kumWfs6UJFXaN041-siqtbNOU0KHpfOau5uofG6RYZfLhaAyOmUNu8VDNQfseZoe_iJlNTDkNSeW_wm2vGq3BGQCBoXaTGuglut9wx5G9DZ-06bVh8YojvkU9xcFDnI3hygURvCn8f3UCFgdaR7W6Om3afTCP-YbkYEcPtduKekAcKUYUX47x8lBInd8OZ8SaVSf56kUOvs18kLOipktQZ-BeNAKXXIY-aK371wuvBQgaAoo7lt7x9MEkOdGWBEVRQD51KLdFCyuPSHk_0N7rYfaZ7No7F5-5GRAMBmI2_lwiOPkuyBg6yuv5Wcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmrU6D2YwjYRpQZ3MyQuyUxylQSzrLqRS4zxQ_d9wJawQwpY72oPMmSojlBKqig2abArlLDJUZbFs1dmPXxpa63AO0wMN9xbYPIOJIblvlzVgttSqeyMqLCzt457l_u6S8wnaMB4Ugf75M2mGXhp8BI91IueLqL7Tjeaav1YwaMwFgZrIWcNKlPDnCgOlv6cxjgTtjOBZ4RU5O__-FAWrRX2ZsSwECg2PPRRbNlK5fsGwzHEsRdEzhUqNC6ynk_3TBVtQnjlsE-3u6unra1MDfXVgrwhzNmN-mevPkpMFmvJDOkNSysdqbbnrkoV1pg_t1DoFqkngZkQpaLUHOHR2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
