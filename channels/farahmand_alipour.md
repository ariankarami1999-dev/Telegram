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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 18:58:13</div>
<hr>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=r26ne6TvbHHd98cDEEenuw3JKy-pzc1C_M2JcywUfLFPklxKo_xEXfE34RlleeOEIKXnbq8LvyMv7llNRaLbs6dRhYHGKsTqby-tBUb7cHwatkPeCoaTEaY99WUG-BLjbCEptfn0MBjVmw2w4BMKXbh5dpRY-IwilZc4QHRdBYMQtsrVOV4dkR-F1nS_steNmxfW6o6CY4LnVDBNDAVBACSMLhQLNO7Bwl2pNw8OZkCoOSePk7nQltMYfwQBN1-fspAqsUMGzlcEhhNbtql_4t-byO825LcgF114DCnwXi10uFZZCzLT79xYxpw7T_wAy0xHVqVY70F-BO_dO8JwHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=r26ne6TvbHHd98cDEEenuw3JKy-pzc1C_M2JcywUfLFPklxKo_xEXfE34RlleeOEIKXnbq8LvyMv7llNRaLbs6dRhYHGKsTqby-tBUb7cHwatkPeCoaTEaY99WUG-BLjbCEptfn0MBjVmw2w4BMKXbh5dpRY-IwilZc4QHRdBYMQtsrVOV4dkR-F1nS_steNmxfW6o6CY4LnVDBNDAVBACSMLhQLNO7Bwl2pNw8OZkCoOSePk7nQltMYfwQBN1-fspAqsUMGzlcEhhNbtql_4t-byO825LcgF114DCnwXi10uFZZCzLT79xYxpw7T_wAy0xHVqVY70F-BO_dO8JwHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvig1ayycEUO61gbGKyWPQwWAgtEOIUfc7dj6Uvm8TZGIc-ut-VHA1cGNpDjTZ_GT4inGe5rvqItsMgPqX1UP67NnLkk5_eNMvIc1Tj2WmTL0M6UpW1EcThYla5kK8PAExzocn8pRk-yMknNceJY2yPjjrrW2NagUfO73k1AbIKW0Pk3HFQouvCChpGX6GplhTqiXkcXt62csvBIiRW0X99vVj9H6s4_vNsFAbUILs-CCckIuo8WZ8wCKWOhcC-is2uC283a9dJmWV47SlGkoUo_YdAj_kj987RnHWDMuXJosE0k26QNrBDvzWC9M5H3ZHyUDKn8R7ocAsJ2ynzK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHyP78d_fSmY-vAEqFik2l7ZlkGJy21Sx5I5dXjWixnIxpRpKMQdGkAI1Oq1KSAenwWGwTeB-J37Ym_eptTW1CdqlhbHYgkJxls9JRsQ6XtTkUONkJqS4JY2SPk50aB4rZOLXPUJiFVeAy3u1w6TP0mONF6NlH32w-dKUTKJRoz7VaBhNN7Z95b8cIM9PlEwtvH-zGzX4l1FtoDauqlw_SNW_Xu1nKSHmCoNkqm82SUg5FXs1X_dz-73zty4MuzmLJ-735vEf_LQIWyQ50EBzG63ad77roh1KcQEy0tAt6VCjwrdaVW1OKXmh-XXe-AltoS88ELnyqYCKtTLo7lkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFoTgLRG-08-wXkVfnmUjpyU85d5MEOPeSE2RXukUJ7gcjmFTYlZCb_kpnQL7ZIcAAM_lDv_J4qZLl0hoiuQRaoKA_6j-aoodXfesfc3KLW2-ibWZjxvxqxsCsKOE-w13vSFR6YCpn74DYo1NOBBYyEvAsrIYpZHslnt5ahw7Y8rBD5zD72zEjJb8Xbr82oFCT3fbG_O9-gKukh3C2YomWyaoxAn9HMpLntkpivRZrpZ4r0DzEYp8eqAocUxAJO47HRnA1D8xjLyMZVi-YwcsKo3Qk76hvz83eeZEW9VoL3t6eBs0cX36qSbGuiRA1OhvmzravFHMOyi9dx-QJrwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6fj-XikOE_vV6gn_Bc8O6-xIM4wgXc4YypxLCBQshzeZI2ex4bJps45gE5IffGwgyOcFmOIBXpQ5LzCUMaN_tBTveENWfWCKP8xENhazzUOnaFAp2M-41EK7Ymex4ZhS70FmJAmyGgh9BYHdlF6czYGHLcTQPXfB5Pl3iD77I8DjDXJa0sUIEh6zuEi1VR39aXBilQoalJgeV9tVniQdu1Klpw0ZHKxsgfSfFTz0JXsGf25mcyADsfQjrHKuvlh0iIPGCR6LoO9Jd48T7nKZvec_4o_-CsQq9qSzSvN6_jHrdi6Ysi5U9_kDIWzg08jSHPScvB1Yh7KR2t3-wfS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbIJyOE2Zg99a7z3TD5mDWj0vjc1vH4vH6eeDCZB033bHtcto7zbvY8OM41MekdSJL9DlcS9mLECr4XoRiKdft09qQFx0vnI8Uf4DSB9UJ5SLtKNYr4kzEbFsDroDdylLGJ1uLB_MRRgKpUuLhaWn329PoFDM2Mf7VIe_Vfs2tbR3FlpSShbyJ6hYHVPN45B959Ufyq7LeVRhGgU4i9RBjDSuvUrTRx3kAfK39tQMR-B3y8NO69Z17tPQoOft3RC91injyqPAcnU69MuP_c5i290F9K3QcyL0s-jszxBquiXLylYWfTy2J4tucAQBOGLSqhVQS5QAUus7_jHfnFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBCdTL9seDcNwGsIb89YYMmUWZ75YhupG5WpItG-REVUvZfiD6KHiROnXkLn4fzdNEvQCBsplLIerYuH0UMUBEtMsezM3MC7ZKK7Py0YFkm2H0O6mZei_Fnzbygt7tAnrp_QgM6h59w8uxsGJIyNVQN0aLBYMYZwuWWVtE_nnIqjCdwrYgb8nyJ4K2r6_6FmvF1cFmuGuqTGjxgGNBAjAkenwQxu9CHL-SNdywTVANS_otcnr7RB-hd3qv4e8yGeMKp9oah80UsGtFRxbWjhdqYY3e5LcKoObVpckCAzAsFgLiWr1fFP9YOF9Blgz6KLpZDuv4UTBUShsOAstb-pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_jklWp-P3SyRXbm4_EDnMya7QubfMI49g1j4w_VhiPn-iZO2Evl0qL-0_yfAfFGW06qtFJ0UHnNf8VNKezps_esDctb0ISCH2P6bquT2fhd2L-LWktS049d0km2_qfc_tzlCR9l4PnCDawud2NIK3WyD1SKzbAZDNNSsI9Ag2I4XDPwulWsAhcmD5ckwtPta7cd4Q_2LgsjjzJuSBgaE4NfL6ji8a_T2wKx0RQoUsLXHxU_QD0i-XsiaHSvD88FEIKUiIeua4WC6dHLfzg3ljE_VPOoMVDG_dxu9S4sK-nc3_VHIwtLtU2D0qQOoBR2AhqMam6Ajzxy-v-rz5Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLFj6blG066qOc9Vz59KMvvnEt9kXhpJ-qtpAmFfW5ICohqG4FNQbWoELS85GqFKPesMMQ0oIfeZTJVY-UBuixdjzb57WF9FRUwO7fSY_zE_YSTtvWkrwiIUm2vO2p_7aXcYiUh9MxrcFc9j22DyifsmU4IGvvMZCwovXGmVQUWCILGwMwwid2CfDJ8gyH-a898QpObWojN6z8_9nSXZslXvmd3cLOi3Mv1Tyvs1VE5qQFTsUJnUtIgorLz8krnFxK_6LS-3AeLXwgACCRvbgX0dymYpAbeS0kksqNXta6BKMCcSOREawZwACz_9ToLVmNrpjPs21FyGGKWgGaYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW3Y8wkErEwjwhOu146AJeeXna-1_Q0yQHyVoQUogvuEw84IQQWdhgrcwU80wv9tXG-1-1jTExHEOTwqgh0A15l5iYi9CWoppsIWSS_H_9MqlPO-ExhLP2LqfKuW7q3xDK4o2mdX_UoqYv7uPLz_u6ilcSEtzGMwSEIrDajTgLwW-XHDpJZvpULYX9Nmzv8qJtpy9PZuvcubBZXBTiJ92E6mS6ggwrjB_PG7OV5UKWrXZQCzHSFlIUOOE6JmN3GhWMWGj7vpEg5yt4XNt_lIBZmLVrNJDyAXQONcTbZ5wKvksbzWFVuWgRJTiWIsxnT8K7PmpZw3v0Ako2lvBbMjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftoT0vHGzBnDY_XOgrbM999A50vu0U3HCEN_VD19MRDlKDrZhadB94T8TrzcNVRt85obQoUoJlZuJK3fO9oEmw4y29FrXCXwTbD_uGmPLdIeQCkoycDhgOUajra1PbFAt9VMcv8n_IHQ3SHNWnGxGXjVLHBUO55RjZzf5ftn_evCkOxFDKjzuTt0TUvZjEPYx3OWH9NLgMRb4TmkwxQfeP7eyvtHE6V5ul4OKgv-3bLHn9tJpWBBpZHnTHEQ2wJppZGzm0FF5ydGr_3tDiyBeExW8qgAtWyFe2c8Um8pWnXv316Y1cQGaND5plapVjmBIXdW2g2xBfNyjqXDsYpiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBuHBmINNg4wiMez3F-XCUwCh4n-_2LP_GWmwRlvnv3TFyB8RtDkVdxb-Zy4nGNuP-wdA10DlFbZHZ3V7DqWPXgM6jJi_nBBZnfe_VWYMtMZVTwM3Gkw2PHhpNwx5Q94VeSu6SgJCCxIPXPNGYI1f0EMhCXR44ZpGDsZeziddZoIIatPBWIGUFywliuc8Ua_-t0R8rx1NXDW570NgtDN5LEjSln8aVO5c1ZPYPUopYboMTfzkUbascvXkreIKjppVfb7XzKleq3GoqDFwbxxxuEigMvroiMAWjN6zjiNAYNdzrFWaDGyALxHEazfkLoMoyO8bvmEuGzgrWQgGpGQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN2fLb4cazVvpoyA91J3Xw1V91yDEY7pxYNgyUboOI9fXj91j597ISmxfcEJt_qEUY4Eh2hbwuM_F02Ox3-MqLHnZHt0fMpcP6qVafcVjRFKeAdOP41tExPMPlOR_FAbVXY6TkExty-hZSS58DfVrNyIx-ONpPI0hSn5r5zYv28Xqw3YcMw0ZcKS1d4VuQfoVSoZ-MFA1AI3sWnUVmzgndyX7JEmOz13aMv_PBYicl5pkYcshx58ot7S6HWN2qSBKY87Dy_t2yYzlrpoelwlEQCVAEx7zjN-2n3Ty1JYd8r0GIG1hRHOgavx1i1nkVK_UoB7ksQccoiVrr0GUQT5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4h9lW5fslJ4sLRwzXTh5VYiCMXndOD_2o5DITX7MIa5Vqvr3heIGeQMZiiq3undrmtD23kn027-yjAX75MjmrToFum3VI0Ma4YwXT2ysOCxkFGeevAuXHxoFfvg4Y-WDNGmxJk0EYZK64db6DW9NwRlB2aCvzUSyCdjNV5de_9ejreW60hedk2pHrdg3BttmS2YieB1D-9TVmA-wORcNwW9pjtVislTuPR7TYGvyEd_-EutjqrBuG5HaQo6uYwMC7l8Tq6XLjjVD5sM-_GdKzLbMiHvQHYkmBL_a0SSY0qK7X1CY_Dsl1IA1k-g9n0nbdqQjlsQH7ECSagbqQfBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qAj6vMI5mKcoctQxspiA2Aa0szcVItCBHNIh3rtu8cgKKFb5--R4gmoSESrN_4nHC4m-S74tiKbz25Wjr2eHNz0ifXWeHATuXdg8ZPG9nZuC7eu5SwpFOlFAo2an-84fjRah3Efg3XI2mPfjjMxtA1ojN8kJd4KMoMQ4BEIh74vXEAcME3J_GS3RY_QCnVtPuYOpkuu3L2lFw6r751QxIL9BPsPFcAm1MyD8S4OjJLKp_gkpo5z-OYr61wrgzXk9muR60Oz-rDTpQaAS3iQSJhoRm3zdhzZUhhkPO43e3u9Q0WywDl6E2C-2OFjFGBQvPOo7V-vLL9K2CrQQQV5Vjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=F3XkTJZsPptPzVaRQT-JAYQavMXDm9yxpnc3hiBJUPsRJyBKqLOz7ZofoktUsMxhzAdWCDBpNzsqV96AacSs9_yBqj7pyWLXfBava-IKatcdeZTMgxMP6Z99DC3T5C5RPysRr-CaTLm_zvzeMa8EO7sIKScWSYRZo9cUmPRHfgLkyhoFH0T6wsGGeuhay3c_P0huI8RecbGA2aBQaPYpYTGiXvEC-QzuoyweOkp6oMvM91QQ1mUFMMwV6LpRju_lxiu0D793uoqKy3zSjmvFwvJ_aQqQxVP9fDbUivY3_kok0-vLwQ_zXk42RwpRlwirbVYeay6ei7260d4JinnSXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=F3XkTJZsPptPzVaRQT-JAYQavMXDm9yxpnc3hiBJUPsRJyBKqLOz7ZofoktUsMxhzAdWCDBpNzsqV96AacSs9_yBqj7pyWLXfBava-IKatcdeZTMgxMP6Z99DC3T5C5RPysRr-CaTLm_zvzeMa8EO7sIKScWSYRZo9cUmPRHfgLkyhoFH0T6wsGGeuhay3c_P0huI8RecbGA2aBQaPYpYTGiXvEC-QzuoyweOkp6oMvM91QQ1mUFMMwV6LpRju_lxiu0D793uoqKy3zSjmvFwvJ_aQqQxVP9fDbUivY3_kok0-vLwQ_zXk42RwpRlwirbVYeay6ei7260d4JinnSXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=Xxk9v8xAY7M8Ah0F2_8QYSl2FfTuzOs7erfHkHIUp555fz6CYn3USVeVAr2qO3r0NXX8V9QY9yaixq31EEo2dqgx8x6gaPIXpkDlt551BOG8aMR57S4OdOHO9j_YUJyHuu8SeNBZrqvDcjhO_SaV3FibbHMarGRjW95MshucOEQXSittKlKZN_TVU--sDOKfJuI2-NkfuELkT1kqzW5XUAJFLuNTcColWJtbZSRXAjOSzLC5Qg-Okv-PbEI2RrElLSz57AmAmkahTFr5BSG5eQ3U0JhC2049f-rOu8sQ_rDRJ5G0fru9ukMQXwPOjrbmINGUouADoqdg5RQFkC0Pyoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=Xxk9v8xAY7M8Ah0F2_8QYSl2FfTuzOs7erfHkHIUp555fz6CYn3USVeVAr2qO3r0NXX8V9QY9yaixq31EEo2dqgx8x6gaPIXpkDlt551BOG8aMR57S4OdOHO9j_YUJyHuu8SeNBZrqvDcjhO_SaV3FibbHMarGRjW95MshucOEQXSittKlKZN_TVU--sDOKfJuI2-NkfuELkT1kqzW5XUAJFLuNTcColWJtbZSRXAjOSzLC5Qg-Okv-PbEI2RrElLSz57AmAmkahTFr5BSG5eQ3U0JhC2049f-rOu8sQ_rDRJ5G0fru9ukMQXwPOjrbmINGUouADoqdg5RQFkC0Pyoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bv-gFE_HoySYJIBbCrPb-isBTzZmTiTD8TiUMeQAcXIzN7fybngcZLQm_1dcejDw7jmVwnzOL3GJ5rCfDkMt2OLjzx1ewg8-0jbBs4Mq6La2pGSpxnmTunFhM2DitGg84Oz7u3EFewLKLbNP5dSgmoWMa9aVfF6okn1iNuDEtnoo1wZIgoeHUbEIk2ABy31YqcvgYCdviVyBWSjo33aR01LTaHiCENUbH7-UiYH9Js2GUZ-g-B7cMqvVm1QvmM1Xwzw4-trtB5_Vpy9x7nGsBGTdVod4F5_MhJkgHrJkq4ciR3uI0Hc8fIwe17elsuf8g2zOlQUxaRlePQliRN-Tww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E17YWgYEh7hUfbaiZyGhOHtBNgiheGim4ols7zpfgFruJmRxF_48nqNCNpY3ZDt-KyK0mdH4AJkblYJXDPUr7Dki2aiBZncPDDyA9QT4aJGEFso4IG8X6ecrjTp6wmfdMhXgxGFmHoy13Q2G858lxczCUY6kn1P9nXYsRkpJhOnYw1itz-e__VTfQy2Un61fEkOA0HUOiXHatglyA5aBI91eoVu4Ph83INPCPumbvMbK9OCsiCgU9xhZbYy_9qTwoBVhVFpgg6a5O66Fz0l5BurDxahwDLOawKzEbYIEBOYvcYlwOmbXzaHzFwNULiP8y_sPg-QamiVU9dFFOwXOxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIY5nOHDPwGOc6SsAAe_Q2LNJsZjVD0ojTr0GR5Fxg2oPRih80zxeRWl3fPbjWLoRZILozcAv62ozESDaY3OIKRD7aI4VpxiN7-g--DiyTsTNWEJcnvAxtVZoOEluuoqZS1V9IQQI8-XUIJA16JR_MgSIzcdvl60UvuQspvTPgoylId3MjVBFkYw305aW8LrYqlWdwqXBxF4_IRuTxfbID2T1XVfzfwImwupQ-JknLUhwSm9uQKwwTfk81OFQGr3jkq5iANNGQUwQhh5YVieFGZPLwa6F8_Fozpk9dS3xwiGMgPYNFFQXSoFutcY-PZvoxKGtYXzz75GWmMDX-Y6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlpwJqERu5fce7G-q_OxgTKPN-GsrdGUknNlGJlucnndm-PRAyvead1YOdG7aLmYHcSDMOGXZExkSHXSYSEdQOSIFJNIu_g4gypkikSZ_pd736X2Sr6IAvmjps7UBEmSkSgntyG1J8gfje_x8ATeVM6mjYqBVWWA43K1i1qpArREby6VggT_oQIu4XLTynT0VHi2CvAg5ImPAllfNPIV9OMLAqhLY2m1TDME_DN4lkYzkwklQIWPeQSW-rxTJIEV0rNg-j8U7yXNClB0CRujlZL_5FL0-SVnKUfDdaS4QBzEsqIc5orCUW4X9VxJiZZqFVyqg0iYyGZlnQj7Me5yYoUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlpwJqERu5fce7G-q_OxgTKPN-GsrdGUknNlGJlucnndm-PRAyvead1YOdG7aLmYHcSDMOGXZExkSHXSYSEdQOSIFJNIu_g4gypkikSZ_pd736X2Sr6IAvmjps7UBEmSkSgntyG1J8gfje_x8ATeVM6mjYqBVWWA43K1i1qpArREby6VggT_oQIu4XLTynT0VHi2CvAg5ImPAllfNPIV9OMLAqhLY2m1TDME_DN4lkYzkwklQIWPeQSW-rxTJIEV0rNg-j8U7yXNClB0CRujlZL_5FL0-SVnKUfDdaS4QBzEsqIc5orCUW4X9VxJiZZqFVyqg0iYyGZlnQj7Me5yYoUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=vgroqNFFHuLq1s6Z5vFMkQW8GDvg6c0u3ac_tRnY3VfbuhXaYCCy8DC3T7fgxPDqIH6OJ46eeLVft3_H1v5WLvva7keCZ5e_-PWqb4MLBglG9zLmONAw4RMLtZanR41TWM4JZx_94gRfcGKru_HPjkMJve-n_zyuVtjMNBcw9cdrmOymvfZ8PpCVnVK6r6xRNscom6_JJNoBtf_dkcB2WTqxUFfwPR_BNtKXcJxa0Ac86LdWNkdiIoUUinHcQHwrbLEWoW2C1VzhudSLXoJL9sqSoYV-SAmegNigbCWiVs6EHlcgZmgXXrOAq6wE9d01q3D75V0BPh1pLD1ri_cMSHF00j5BubVH_-383IBaT8uLiElFLbj7wo3MBtzPTWks3aSk7VRaepR56cVMPfO9lQTYPwkbdHs3L7YcjNZ_TBxVoDYTXPNHDtEKS0jV-nu0DSmcz_qRSpJoKY3K36R2TMWs7tgU_ipAXZSPM5NtkFGitlmoHvYVi85fBdiLecntW2GHf4hHdxBv55mCsTo985t6GqHckDj8oqhbxNScT2s0P4f98rC7taAj1BI_g3NtHyspgO18SfFe1cECOwVGt_ti209yuwNyo8NVKGqEDdIcEnxX3emXFLDPDZDPfaEnUN2qwcMWQchAJ7vrK1hPp7T4SGnRV_uessQQJGMoHtY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=vgroqNFFHuLq1s6Z5vFMkQW8GDvg6c0u3ac_tRnY3VfbuhXaYCCy8DC3T7fgxPDqIH6OJ46eeLVft3_H1v5WLvva7keCZ5e_-PWqb4MLBglG9zLmONAw4RMLtZanR41TWM4JZx_94gRfcGKru_HPjkMJve-n_zyuVtjMNBcw9cdrmOymvfZ8PpCVnVK6r6xRNscom6_JJNoBtf_dkcB2WTqxUFfwPR_BNtKXcJxa0Ac86LdWNkdiIoUUinHcQHwrbLEWoW2C1VzhudSLXoJL9sqSoYV-SAmegNigbCWiVs6EHlcgZmgXXrOAq6wE9d01q3D75V0BPh1pLD1ri_cMSHF00j5BubVH_-383IBaT8uLiElFLbj7wo3MBtzPTWks3aSk7VRaepR56cVMPfO9lQTYPwkbdHs3L7YcjNZ_TBxVoDYTXPNHDtEKS0jV-nu0DSmcz_qRSpJoKY3K36R2TMWs7tgU_ipAXZSPM5NtkFGitlmoHvYVi85fBdiLecntW2GHf4hHdxBv55mCsTo985t6GqHckDj8oqhbxNScT2s0P4f98rC7taAj1BI_g3NtHyspgO18SfFe1cECOwVGt_ti209yuwNyo8NVKGqEDdIcEnxX3emXFLDPDZDPfaEnUN2qwcMWQchAJ7vrK1hPp7T4SGnRV_uessQQJGMoHtY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVyaI2WinIc8GkiFnVObEVztX5jD6K-9EURiaGs6jO9P48a39NxXn9sFL43UqWpxTrNGk1-Sqiw5Q6fFx_3vhv0Y8ajBMH6jUAYobds-OcWYDBk3ZCY8DaL2HQdNzV6aoxW6ROUo3lzaKYRjfzepILxRRvzeP2lgPCC0bNuwN6TcOjuyghs4ue2VzYzVAtNwgoYHN2q23yeegSb-YykTgA16o1uZ1aTY6w2XUPIYZmDdvVw1HLCq1d2488enn6XbwKJPboVZ76HnFBbXiVJzninPbwqT8ocshwTL_z14omdtEGvu_j1Xh2FGveMBEoVop002cYEYlE1fBAdKGsRQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZbEQsvdCiOimfDOgvRv9SYqcXcLu7ZPzNrMKft4xVL1dhF8vY486XE9xzmS4BSmnl2Ww1m04-42OML2ibvkAbsM_3oNMVSHw4O7cvZIRryH6zLlR4Ff_dOgppqOKqK0xdh58AYf_1fPgX8dXjkNQ1ZlhcIgPYgALWErNoL0uYS5J-LtM2ut4HCtTomLQwBl9ZTsnwgLH2CI_iy0-2-5_h2VuBWcOX3MnKjZ_oqGyq8T4hSBv2bR-h6uriF11KvqOg3HlEEvdXO3TyN9yXa6jNJkfL2Nhpnxj_915IgyEnpiEWmC9j7EfdkSNPrDr8vjqA8Cku2e6AaGj1tHJsS1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak7dUKlqIyWilv2HEPphPVAPVBPm37j1T9CPWPvbUs48yfBIrzOJGix8tTOECLruyMdzfGOoVmLOyBuKnPSofxgazKuxyPxDgKwzKqPijbKbuBLKoHUHDE8gjudjym1NYiPDN3bIn_UL_bPr_IxTTumHLFY5wci5fpg_EWyO44bDSCpjT6D2B3HZ9AbTbeB6aF_RhuYS6XIu5vwjOVWeEwyVLOJi-jkDtK-UGhfLCsS5IU3LSpET6M46Rrli3oI6LTAQ30mXYQ8BDcQRf_h0pEUiWVpKdmgxp0lBWEh3qgs5I2ExRUPVyYWPJ6FZr9qZb1waGAlmAFAtofVQYKoMzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=epAo8KbHHZerv0py16dY0l5ANkgeNfSZidBhpTQBZSBOM8QVrdi0Ka2hVV7jPuKIUH7bh38urlaSbpNGomHyPvMQ_s5FfEXCaaZwtZbDKvHpyY_LZtypJ6hUB3OmfIFTlbxLwZZeXTgzpss6EtnAhSoZnUQIBfP4Avz2ZKIAHofejXJ6eCZUaNiSmbERldV0kHKbWtLg6m59hZWHqyeG60rwpn1Irdt8TimfUubBUbwy2hV7MadzJgJHhNqeArXKpeS-mKjztl-etLnb9WgGYYhwbaFTJNhakB-MvAMmc5PT0INrhI-VkQzEN6BgIwYKqrVLRdkfgu1Mki_K1VNNhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=epAo8KbHHZerv0py16dY0l5ANkgeNfSZidBhpTQBZSBOM8QVrdi0Ka2hVV7jPuKIUH7bh38urlaSbpNGomHyPvMQ_s5FfEXCaaZwtZbDKvHpyY_LZtypJ6hUB3OmfIFTlbxLwZZeXTgzpss6EtnAhSoZnUQIBfP4Avz2ZKIAHofejXJ6eCZUaNiSmbERldV0kHKbWtLg6m59hZWHqyeG60rwpn1Irdt8TimfUubBUbwy2hV7MadzJgJHhNqeArXKpeS-mKjztl-etLnb9WgGYYhwbaFTJNhakB-MvAMmc5PT0INrhI-VkQzEN6BgIwYKqrVLRdkfgu1Mki_K1VNNhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dokAauikt7qkZFR3nn4XqWjobc09pzWJh88_S11qF5lNC4FyNhmIB650f1ZlEO3cMDOEj-cTc5F2WYfxjfMtDbHHz4RQNwpo-xmUGCVEtBCBQOoY_ZCnbBJH091nU6WwKrZIduBbkZ3lI0PkATTUimbgrSEBv29wkWqACtiswGnBL8UokusGxCgqiPi-tFgUpg6aF60WSv2sC2kSnuiu74CowllPRnaiQ5MmuxszGW7dbs6gNoSzd2hJeNM13coniVqO9TfjMQnt-ly5vs5O7jBm2E1aIA8fV3KcF-rLvaZhosaOtH4py22GX1vjW8X4v5z5Kai1oPkngfsIVQ0eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=jxmlVMGZ8zRKGoL4jNsENsNdHwaytNrUJjcW8GSiJnJu3j_ZFtTcoypN6ZnrAr1V81GYUf2MBhQjRz9PSO0vBLOvg4V_ksDUarUvjPGRJPjb_9tOvXHtoeFZ2kcASVn8Uea4Zmk_T4bCRPDjohFz2Lk43KQmA01XLUr9sS38TKNyaRUGYC13J5suFOd2BE1fMBCVOXBEnOfJuso8Fh3H-DbEMxKOS93947Wle25qvjV6Zb9fISZ8MWOeWsPYpPQ37KH0XKAOq0di8JjMUFBbUxv9QGEXWG8WHMYChgQXkDHPtk--VHOkVv1f5mBc3LjK1EuVSE7y3hPER14iE4bftA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=jxmlVMGZ8zRKGoL4jNsENsNdHwaytNrUJjcW8GSiJnJu3j_ZFtTcoypN6ZnrAr1V81GYUf2MBhQjRz9PSO0vBLOvg4V_ksDUarUvjPGRJPjb_9tOvXHtoeFZ2kcASVn8Uea4Zmk_T4bCRPDjohFz2Lk43KQmA01XLUr9sS38TKNyaRUGYC13J5suFOd2BE1fMBCVOXBEnOfJuso8Fh3H-DbEMxKOS93947Wle25qvjV6Zb9fISZ8MWOeWsPYpPQ37KH0XKAOq0di8JjMUFBbUxv9QGEXWG8WHMYChgQXkDHPtk--VHOkVv1f5mBc3LjK1EuVSE7y3hPER14iE4bftA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkbq-mnER-Qy7fUUhJXIRfbn5iJKEr-6V0jTIGPE3280xc3SO416KuaTAQSlWFgCwxAStryrnmfnQB1YRFtVgkmun2EL6oZVRUfP0ag39B2z6-sB6ZJavJPmHr_85rkS6V32JfIdIcUpJ6h6kv8XbcuGIoBsPhCqLld58RVRlB6xaG9JmeLOqIW4oeSihQwlcCaTJF-8iBxKNJGKc57L9YFDVxsTpUC7EUXzdSaEJFK4VyR0lyFNbsNEaKZfbNN2jcRb83thSuMCGXwxzrMgXxNG7GkfdVCPmx4eELj4Jx2kwcqCfGNArJ4_bKygldJgfDGg7d5Z_VJ3hDQ0NzfEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY1mXKHsjPgv2zV7Qy9Px3WvVDr-z_JwpJgWxK18Kg28D8nJK1Jkc-7WfDQMAwYQaYLmbARynv8F6nzUbOGaK3qslp2NvOtK9WpgU5PdE0Aj5skJD33p_pugzEtx80st6GbmYqdm3aBchk1fqWW5pqRS4J4iE_b83lSKjEtBgLzu7qbRiVTCug2Iz1ilC1CNer31NneQwLB3C4pVt-jJLweI2NqpLJmRGRIeNs7EcXxH0EQHogX0dDc9jTf5WrZK9WUkC7pPhYT3lCxPf2mI_ezayRbxv3il8roXLVJs8TW5kI5z3C1-0ayGy0bTcrXKMpppBqCjstPdlxcfHlFPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=V4DTEXksMZuJV8kbMKmj55wzPHLabOolwyL6qalUp5yTQRAOuUEN_fj9BH_ahXDSw04sRTfYjvZ_-V13wJsGvEovjv4DgqWXnaxYM1QDjeZf16S0MA5TwQC_ck9PUVpHfWAroPH6sYzjPl5gt4U5qyk_hN1Qhy0iIvPuFmDEJJkWJkVWCH0w1SIIaHrOkmEhcIR0n6B4vEJ9rLoNsSN7iAED730CciWCaJ2Kg_hEQlJGos6FfxHGwwf6C07jbMGSrx76khUAGxdJvjbKjdc8jlRCycm7H6fLrDDHXrLnWZcBUGPU3zu4mNRxB3msA0BStppfMQMOGZlXU3aDYOkFfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=V4DTEXksMZuJV8kbMKmj55wzPHLabOolwyL6qalUp5yTQRAOuUEN_fj9BH_ahXDSw04sRTfYjvZ_-V13wJsGvEovjv4DgqWXnaxYM1QDjeZf16S0MA5TwQC_ck9PUVpHfWAroPH6sYzjPl5gt4U5qyk_hN1Qhy0iIvPuFmDEJJkWJkVWCH0w1SIIaHrOkmEhcIR0n6B4vEJ9rLoNsSN7iAED730CciWCaJ2Kg_hEQlJGos6FfxHGwwf6C07jbMGSrx76khUAGxdJvjbKjdc8jlRCycm7H6fLrDDHXrLnWZcBUGPU3zu4mNRxB3msA0BStppfMQMOGZlXU3aDYOkFfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=f2bg0LQiHiePp-uFvG5SK5DWPdu-dcinc3zCBOoqHa14w1B2xd4PU7dZgr1upGzbO9C-aRelrXn9RwAZAnB9cwuu9cF7lyqo3UM9Oa1QOFxolyVofK0IVdqj0wvuTZHHfBS9jTXizioY6ir81TI8ZO-ByJJe-NS1ibMFYBD_6xReN21c2ZuId7WPDghEe2wP5B9vu1s1vgp_nC02BWg3AGmZHzhRJRJA_ENC9A1_7zoRI1UagMDA7NkBkMo0UFBJGjYu_OqJe2yMDzffhZro6GcqzQr8RiHbDiok8yPmRdoLLWPNamjbeaX8PDzoQfeTfdCxj1oTVTuf4OEgfaPFhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=f2bg0LQiHiePp-uFvG5SK5DWPdu-dcinc3zCBOoqHa14w1B2xd4PU7dZgr1upGzbO9C-aRelrXn9RwAZAnB9cwuu9cF7lyqo3UM9Oa1QOFxolyVofK0IVdqj0wvuTZHHfBS9jTXizioY6ir81TI8ZO-ByJJe-NS1ibMFYBD_6xReN21c2ZuId7WPDghEe2wP5B9vu1s1vgp_nC02BWg3AGmZHzhRJRJA_ENC9A1_7zoRI1UagMDA7NkBkMo0UFBJGjYu_OqJe2yMDzffhZro6GcqzQr8RiHbDiok8yPmRdoLLWPNamjbeaX8PDzoQfeTfdCxj1oTVTuf4OEgfaPFhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=uQRY1DlP6fgyUxoiytoGSFX53BcLONZsC5bkZyOTVq2G8lDduI7NLRdQshmK8nEybhZ23zN2agoq2o5YjsrYr5BCyRnMgwrPQVkFTSLI5LmjQOCTxH1dRMWiu9QHJRmrPv9hQ_NNvzXAKO2eNJIihyyTTV__1YPN2wKzTD6kR6_p1pCmSE6Mad9WSYv-HVE-f3S_mQSm-JQnID5VJLVrxRPUANmFQr7_bLHB0uxGv2rvjhdPkUX_a_xiELRxomanRbm9wJS2okin8o74yT3nsx1Hh3eo3ojj_Q4ZhXIfxjOM1QDU7dBWMDK8L9lWeFm3JUK8WbLj4074SJgooDT1ehnP2VWfBa4gPHplgt8ass0mbFEnoSZaY9h_tUYb4KAXS6luAIaWkG7HIWhGEjIJCNvY03YL-9VNE2KPSRJRsUJm_RXm9G8-Dxe86pGPvv_vK_u2uf6js_Pr4Mb1KKVj63DGQt7wupdUpud7G_UObfBXloB5UXFghp1feuW1t27O7eDx1o8_km0N8u-HnxuqV8F8G3nPjdyBwsris0z5z8iHzF3gPhegzcUkXrnpQ81Y0ZP3b-gmdOxhfQ2n1pw_WiOk42nTsvPPlnM2qaRLw5S5RJVcUegxSz4lSDdwryhnVx1DUUQhnFw4I3SBM3uRpTJ35LZiMc-KbIG4S7Cy-n4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=uQRY1DlP6fgyUxoiytoGSFX53BcLONZsC5bkZyOTVq2G8lDduI7NLRdQshmK8nEybhZ23zN2agoq2o5YjsrYr5BCyRnMgwrPQVkFTSLI5LmjQOCTxH1dRMWiu9QHJRmrPv9hQ_NNvzXAKO2eNJIihyyTTV__1YPN2wKzTD6kR6_p1pCmSE6Mad9WSYv-HVE-f3S_mQSm-JQnID5VJLVrxRPUANmFQr7_bLHB0uxGv2rvjhdPkUX_a_xiELRxomanRbm9wJS2okin8o74yT3nsx1Hh3eo3ojj_Q4ZhXIfxjOM1QDU7dBWMDK8L9lWeFm3JUK8WbLj4074SJgooDT1ehnP2VWfBa4gPHplgt8ass0mbFEnoSZaY9h_tUYb4KAXS6luAIaWkG7HIWhGEjIJCNvY03YL-9VNE2KPSRJRsUJm_RXm9G8-Dxe86pGPvv_vK_u2uf6js_Pr4Mb1KKVj63DGQt7wupdUpud7G_UObfBXloB5UXFghp1feuW1t27O7eDx1o8_km0N8u-HnxuqV8F8G3nPjdyBwsris0z5z8iHzF3gPhegzcUkXrnpQ81Y0ZP3b-gmdOxhfQ2n1pw_WiOk42nTsvPPlnM2qaRLw5S5RJVcUegxSz4lSDdwryhnVx1DUUQhnFw4I3SBM3uRpTJ35LZiMc-KbIG4S7Cy-n4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac4xeHKC5FONPhVw8atg-kkUX_CuMW8yMSE_2H7sLEwFK9b-7SdNehg8FNecJS2wXSw4bWDqrWIEPnpBCHyHaApoeT5wFHGuL9mYXQm9wTVcmlrWyY99pGM_h9d4OKU6Ph3xiO8oF9Zkw6ObQ8Bx87FGnXtP19_JTfC_2qXjq2ZOUbq4z8EaMw-7YfBQs8ahFPw4NJ-M7ZCzGA9_6Qd1FKIr36MQJvJ9vPd1M3eZAh2o_k4PyzzhdgwY4E_zuGHnk8UynbBAYZTS5spOJ79-s4K4zU6D4duVdKSMtld50vWcT2fVtPprNKjDLDoQ39154-2ZoR0BYdOibluEvHD-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ln-65frZclsz8gHlWsHAHLYPNkhE9hHoLlD-3XvKi5rvbaFwCu_mxKbxQ0si5erzK5bTFqLNdJbZSrlnlTyysQruHKj8jBjEWgUOyjeHwvEtGpSX9KPyIecLrk80xo4lJCQ8jMXWgxLixFuTzA3bhe-tCeF5VNKt5vRNLBS89e6XcCtInpazTpSNTQDhJu1K_SvHsys4ol1T5TPo3ZjUZEW44nK_Ujf7hCDWKtRq_5dFOw-iAuKPHP6GNv_VCdCaQxpg7Qm0BZ8edRtqdCsXei_7NyFpusTi8fdipKzONUbvx6xBJCoZIwBm4b_NS9NqqDtJN11-BDoD-UhT4Eh8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJdZD1qFKUTV9PaOfsykkkuUsuHEEG8S_YcKFHjRxfjZkKSEa1pzBvxTRKTkzG960EcwpxrRjodXprSS7Bj9Z-h17AkTZxvOJsrXdIvxik-9nxzeywe1wxfTOtzSYk2CRGY4CsTZvmIPFCbLnLM_XghaNXrfx-hKaETX38Va2aW--eDCjk-O5aHo0t45x9Ng9o3dNusDymSBbJ723c_VC0RDuLLmibkldktDL6vrKDXrvUYiR2EKRmYjLSTU4tgvV1pCmA6k3rtGUeHosVZ8smEMw7ZWJ1tarzy34e0xKIX-DTxH04evzqrY4jEQiNlOnGqZZHh21HAfQ8ByxWziQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=H65IVac8KYVZ-i_9usvLELJER4komYefSVc8Nth0bXTc3PKJTw_uErbXenANVnBNZkZ7NBAldaArzkV3jYm2eEOPrkdYwVZbmYiyc3SfG-atvdkX0NcW_nsb-8liiZLhcA_sGSjpKSRilbkoqcb6IkkcQ7VPtB03wEM2L891xv3HF8lAu8ChVg5XvfkVeis89wnbUhJLnWB5UzxdQR0Jh6Z5-WBUzzX48BgbRnVPLvQ4Ndr9GZyUweNkHBGLHE9wNiHm-GIa9TJVl4AozzlGTkupnWR-f1C-ACS_fxq8a8OrX9qdI--d0nWqx9S7BuxGD-MVY-5PTR4dvJ1ttM0doYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=H65IVac8KYVZ-i_9usvLELJER4komYefSVc8Nth0bXTc3PKJTw_uErbXenANVnBNZkZ7NBAldaArzkV3jYm2eEOPrkdYwVZbmYiyc3SfG-atvdkX0NcW_nsb-8liiZLhcA_sGSjpKSRilbkoqcb6IkkcQ7VPtB03wEM2L891xv3HF8lAu8ChVg5XvfkVeis89wnbUhJLnWB5UzxdQR0Jh6Z5-WBUzzX48BgbRnVPLvQ4Ndr9GZyUweNkHBGLHE9wNiHm-GIa9TJVl4AozzlGTkupnWR-f1C-ACS_fxq8a8OrX9qdI--d0nWqx9S7BuxGD-MVY-5PTR4dvJ1ttM0doYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=kwyKD-ohgioNS5L_ZTrKZYn_w1VfhcIFcwXgnXPN_NbfbHqyLhswUTOxZ0a3rX_YZB_JQiKfWUvYj99To9fOzzLNb3FwqR-R345aFl9uKPef9QUfYbg00LPEDYQquKulz-nDCQ7xRP9xbZbTqezv9JEo-tjVgwLWRxAmcQWGfKoyFL0uOVDawjYCNIZ6lZlvNGc6NEQ6CztGSN6N1212hXubjbAEq5ZSj29XSEnlzyJi_3c713JDZJTJjTlVlMiRGgUfTXE--VDghT2C81UmU78kXDspZ5M6QzX5Aov4iucRYKw-yhUlFJRX5ru5NaVdnwLc0XBESVhLjaDmIvASLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=kwyKD-ohgioNS5L_ZTrKZYn_w1VfhcIFcwXgnXPN_NbfbHqyLhswUTOxZ0a3rX_YZB_JQiKfWUvYj99To9fOzzLNb3FwqR-R345aFl9uKPef9QUfYbg00LPEDYQquKulz-nDCQ7xRP9xbZbTqezv9JEo-tjVgwLWRxAmcQWGfKoyFL0uOVDawjYCNIZ6lZlvNGc6NEQ6CztGSN6N1212hXubjbAEq5ZSj29XSEnlzyJi_3c713JDZJTJjTlVlMiRGgUfTXE--VDghT2C81UmU78kXDspZ5M6QzX5Aov4iucRYKw-yhUlFJRX5ru5NaVdnwLc0XBESVhLjaDmIvASLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=jo4f-7nDyQJxBKg7f_NTV8_xI3uVrsMPKcDWmAAWIHuqbjmPNN-YsHk4Bqug9_tpLy-Z8Qy0JAgYIO02NOnNUtl2z2Px5Dglt37Gwz7AqffaOrg6ciLad1DYaA49cb4OG2PE_mQs57BzbhLfHArua2wtsHLtwXKX4TcQo45XgeIOUn-R7AlhZcp5V2EYTc5kpLgSKKzE3_Ek2b1lNk8uGnqugSiJ4LS2jp4IlLfLkkoBsJkMMbySlw74Yxs544_tLTMrGb18uDS7__77seJJtGwi-Mp7xdqfvayCNhR0ixKcaSZcZ88arf4h6Y1z_hnBbViHxX9pDxQOjSJ4NJvd7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=jo4f-7nDyQJxBKg7f_NTV8_xI3uVrsMPKcDWmAAWIHuqbjmPNN-YsHk4Bqug9_tpLy-Z8Qy0JAgYIO02NOnNUtl2z2Px5Dglt37Gwz7AqffaOrg6ciLad1DYaA49cb4OG2PE_mQs57BzbhLfHArua2wtsHLtwXKX4TcQo45XgeIOUn-R7AlhZcp5V2EYTc5kpLgSKKzE3_Ek2b1lNk8uGnqugSiJ4LS2jp4IlLfLkkoBsJkMMbySlw74Yxs544_tLTMrGb18uDS7__77seJJtGwi-Mp7xdqfvayCNhR0ixKcaSZcZ88arf4h6Y1z_hnBbViHxX9pDxQOjSJ4NJvd7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=CwgU5F9SJ5tRUVsWrXemEtFAaQaw8blAjaxbXevNRfxLU3I0o46W6nERYnvZb3AJhkLJAw_C4cBO-wgguMsTolBMpe8fgkiYD2zSkNh6Tn2_YW02VSFwhjJXdosu09BOV0kUGYhEqlwqeXnfIk8G_-aRlE3YNdzuuPFkxlN5bnl-FCFsVpvXEB7e5Ug0x1H1NIWdsW1Hlq1sOm22gM4btRIh4T2wWqSS5QuweDphOX-eZD27DXTpSLUMYeI0MdDpzRVmhZ04oHw7L_Ni5wMIMCSDLudV7y4kxlmBdqkuLfGczvOPP2yo1w0Cyku22ICPJQzqc98AMJAMskPDZ-ZhmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=CwgU5F9SJ5tRUVsWrXemEtFAaQaw8blAjaxbXevNRfxLU3I0o46W6nERYnvZb3AJhkLJAw_C4cBO-wgguMsTolBMpe8fgkiYD2zSkNh6Tn2_YW02VSFwhjJXdosu09BOV0kUGYhEqlwqeXnfIk8G_-aRlE3YNdzuuPFkxlN5bnl-FCFsVpvXEB7e5Ug0x1H1NIWdsW1Hlq1sOm22gM4btRIh4T2wWqSS5QuweDphOX-eZD27DXTpSLUMYeI0MdDpzRVmhZ04oHw7L_Ni5wMIMCSDLudV7y4kxlmBdqkuLfGczvOPP2yo1w0Cyku22ICPJQzqc98AMJAMskPDZ-ZhmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkBDlzjbFKfSu5fqh_PuOB2B3UpExudjEkQOBjckGCL_FnSKieR14oPGV9tq5DdO0uFsL--05i6mgPsAInSE6pXj-PhU9R6PJesv1McFoE9bTNlLV3R7xjn_V9sKjij0dHyEiaitxcYxY143v8OkEffJArfTfDzZm8hum7B-mu1h-31HP9UNv9GA8Ii76jEgimozD5nIIYe1jUhQHYt4vmDVP-dpjKP_GlfU5QC_-Cc7S842Ndjf0RVT0ruev5yLgY1D_wFD-nsu8Maf_NLGdER5V1tT4KHIQxXdKp3jmXfgn8lpEtVHCjtE88UJcuqq1WbiadlYuwzKm0gwxceB-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=Vwkvrvs65sryl77Ek8CspqraHFnwVbWEcF_XnqfeI3Ndb0L5H1JGjGs4psJC5MEgHXJt6UgPGnv5olzrzG4Y2a2lflSPjjPdkqYq5bOV-YgBgrXpijuBZnvJZ_gObZyeHY8kdoBhf0cyhFuaVjdfurmAtHNnvBWCA08zzOfRSGzbUu8eljAPX6UZJ_j_ToHVvGGy25ECQ__zR0fBROkIEAjFWYgQZnHRA6pFDbud5iMUZFr4y9xEd8V9d_PGyCnY45yCoIts_01d9vTtgvDz4eEn1PunA3Xri-yJrw5n0w1M5Aasfl0gM90oKVLrl52cAsFuD8EClt-2_E4G7Kce9LclKcNrfP9gvFJ4XKvS1KuatVs7UhntNI2G8tHXqW0u4QzHXVhMABNglvb6JcBzj4RR2LljUeNRXNm_RdRVHBgNhXNorsBwJJCdaWJ1e3YK7-7OZMHaxy43fg7hLd4WRyW7SCxrpCbfvLyiCSvaU815Ep2ICShTyNn2ooez7U0Msw33WniOKjg3XB7VKpP2LAeINIeLOMJmSfEdiJwNxwUcEFjGFh517ONEGLSoy2JcNA5zhyZK5Qm-jbVSVUX6SggE5Q4RNBPz1rQzuxiYvULDZLMdXFbWxkCPXlnVxAjsAf9nlkDroYpxhP4vx-3Jr4GgN-7GmXT5LB9nqEzUyqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=Vwkvrvs65sryl77Ek8CspqraHFnwVbWEcF_XnqfeI3Ndb0L5H1JGjGs4psJC5MEgHXJt6UgPGnv5olzrzG4Y2a2lflSPjjPdkqYq5bOV-YgBgrXpijuBZnvJZ_gObZyeHY8kdoBhf0cyhFuaVjdfurmAtHNnvBWCA08zzOfRSGzbUu8eljAPX6UZJ_j_ToHVvGGy25ECQ__zR0fBROkIEAjFWYgQZnHRA6pFDbud5iMUZFr4y9xEd8V9d_PGyCnY45yCoIts_01d9vTtgvDz4eEn1PunA3Xri-yJrw5n0w1M5Aasfl0gM90oKVLrl52cAsFuD8EClt-2_E4G7Kce9LclKcNrfP9gvFJ4XKvS1KuatVs7UhntNI2G8tHXqW0u4QzHXVhMABNglvb6JcBzj4RR2LljUeNRXNm_RdRVHBgNhXNorsBwJJCdaWJ1e3YK7-7OZMHaxy43fg7hLd4WRyW7SCxrpCbfvLyiCSvaU815Ep2ICShTyNn2ooez7U0Msw33WniOKjg3XB7VKpP2LAeINIeLOMJmSfEdiJwNxwUcEFjGFh517ONEGLSoy2JcNA5zhyZK5Qm-jbVSVUX6SggE5Q4RNBPz1rQzuxiYvULDZLMdXFbWxkCPXlnVxAjsAf9nlkDroYpxhP4vx-3Jr4GgN-7GmXT5LB9nqEzUyqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=C7fjLweP1MS50AhLW7zhL0_amkCtvqPmz4YJci36t6mwO0BcUHPQQiwm-YUBQE1uLZ9KsvEjQ0tTcxpbQmN-pgyRxxumX4Y-JB-5AzXepVCBJ8aa6Ni_GcQ0DqgMfAPmv-Xz396XoFvC50cxLm1wkAVOj0TGxTrJLB4xCBNWRnNBQXCkJ1uLP0-Cgz1SzHWilQREUkO7ce3Ot7bzMO9gYuejgxYm2-osKSN-HpOLsbhG5ZXK5rvBd7qHYMqgnQ1l3UCewwzwxqooFW5eDJqeGDN7h-MTlpu3VkcwiL54e1w3UDQ87UiaFi9mAv9bcYd8Rm8wyiLRP07zzFDeTD8TlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=C7fjLweP1MS50AhLW7zhL0_amkCtvqPmz4YJci36t6mwO0BcUHPQQiwm-YUBQE1uLZ9KsvEjQ0tTcxpbQmN-pgyRxxumX4Y-JB-5AzXepVCBJ8aa6Ni_GcQ0DqgMfAPmv-Xz396XoFvC50cxLm1wkAVOj0TGxTrJLB4xCBNWRnNBQXCkJ1uLP0-Cgz1SzHWilQREUkO7ce3Ot7bzMO9gYuejgxYm2-osKSN-HpOLsbhG5ZXK5rvBd7qHYMqgnQ1l3UCewwzwxqooFW5eDJqeGDN7h-MTlpu3VkcwiL54e1w3UDQ87UiaFi9mAv9bcYd8Rm8wyiLRP07zzFDeTD8TlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7T1lZohIBHpZ78RD_MCLK7xrShuwLLy9csmAAGT0YvyB4RxQJ03QTlzutOivHYi4DFHbilkhCYcQIVx-yE0U7fg05XaoYc8TDa-p0PHNjM9_jTHpurIrHtnKNJyfkE56ac-epdqkodEX3NnEiNnOlTXUBoIpbpB0lY3pprmpOtDGKDYmRp9RPF3jJCtVknLGw14BqoxbJxmK2qZ_e3WIA5WM3ji4k0Uu5ItJgU9eQgXRvatwVh2M2C8n64lxPw8kLi8HBYIHA6OzbACXn06bzne6z96U2nZVrZ44fA4S0oEpXud-JuSEDkQ5zAy0dF52r9zte7zPIJY06XIlKV_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=WDvDJzRGxXu8PUL0vAbnAsSZbEYlcWmwKgBgCadAfJl53TTxqr5o7TZs7SxGJ4wGvbG5GeM9XZieaTBnvAg0Go_VIEZ2RFnQQJgIxd7ArgMBHb3NDW4IT9sgFyCAFHfoRFV5LrxbWE9gbUDKCf_WFFxc7IGYnVjv07tzzFHD-k5yGbmZhl0InX9O1QTGcRu6TN4jhWwuz9Yb2p049s951KeeAUYNPrXMsclEv9ht0oLnWExnCJS3GnGsu2KDynzGUadZ0t760lCaSyalaTq30DjK_a5qHkvFkYDgxzswkJt4ylmr_D2jdd2Fl4HDtl2DbxDnCZhUOviS3QkDqqeQFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=WDvDJzRGxXu8PUL0vAbnAsSZbEYlcWmwKgBgCadAfJl53TTxqr5o7TZs7SxGJ4wGvbG5GeM9XZieaTBnvAg0Go_VIEZ2RFnQQJgIxd7ArgMBHb3NDW4IT9sgFyCAFHfoRFV5LrxbWE9gbUDKCf_WFFxc7IGYnVjv07tzzFHD-k5yGbmZhl0InX9O1QTGcRu6TN4jhWwuz9Yb2p049s951KeeAUYNPrXMsclEv9ht0oLnWExnCJS3GnGsu2KDynzGUadZ0t760lCaSyalaTq30DjK_a5qHkvFkYDgxzswkJt4ylmr_D2jdd2Fl4HDtl2DbxDnCZhUOviS3QkDqqeQFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=maceDGw1cSlhzRrUG9je5AI2H_e08ouyb-RAtu5nJJs7v-aQe45IaOJmkpdSqeLG8lTtBBIm6tmPqprdbhHZneh0aQsVExsSERn1rL6Na1lqkP3HY8tYtUNU75whrH6zJwGdhGqz41ol_AZQ_dM6IAqVwbhMKiOqkjvq_RFcKIVAPHIaa0ZDllaOW_zoUMZkE7B0Gm4Q7mINcH2MOZSmdhs7eTJE5W7bC3gq29jxjBCP54KaSoZMm7DYDDKf-TtgV4Hlmrqnv-mTpIX1-TybyrKehQ1oSTyTvbq92j0EfefHOwAuF5CBgRLut-aro5LRf2knxaQolaOz4kk3SYnXwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=maceDGw1cSlhzRrUG9je5AI2H_e08ouyb-RAtu5nJJs7v-aQe45IaOJmkpdSqeLG8lTtBBIm6tmPqprdbhHZneh0aQsVExsSERn1rL6Na1lqkP3HY8tYtUNU75whrH6zJwGdhGqz41ol_AZQ_dM6IAqVwbhMKiOqkjvq_RFcKIVAPHIaa0ZDllaOW_zoUMZkE7B0Gm4Q7mINcH2MOZSmdhs7eTJE5W7bC3gq29jxjBCP54KaSoZMm7DYDDKf-TtgV4Hlmrqnv-mTpIX1-TybyrKehQ1oSTyTvbq92j0EfefHOwAuF5CBgRLut-aro5LRf2knxaQolaOz4kk3SYnXwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIOPg0svkn45eryOk5VWsjaRMTLQb1z3IRVEcHBYpyTDdvyfh6d-pKWd8DYQEBKnJTVnzhabdzys3dkTvrQFYkfE-yBhiBS0se-1u3Ghamm03tvhPQWZsp9tL_PZgySaSF1JIQQc9jEdGyAVYCSpuw72a3Scltg1qUB7bVOP7zGQdLoDyirct6i2AMzhCtdrn2pdWGL9Vvxh04oTQjT95sFBz3i9MAbhUurB-UAv-WQwu_33MnKiXAgHymHWHD_o-rVAiBp9GmDnQQgcaR-eCwW0gHNVpwYirK138wZOTF4wRygoiQhWnd91mYUNc7eQyRggxNLV1RxRGdPtdNb-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=TrCU_QfDxqV1s64BSBSUKv4BXFgc6JxOrU7WpuMz9BJ2q8GvasLKJjaCOZ1fiQsa_KP3j6pZk2-fVBvx6AxSx9CiAL356dqYy0xLJZKgQLwcDgrpvYtUQWdNGVluHwLVrlpyB5msSfIweROnSfoP5QHDo7pUtrwwwBSaq1c8ZfZpOAzI7IIMp9kcMmILLQfftUtAvbtwycS29C99WwuIijLgpXhVxJLLu9tUSWopz0rpou1ezxiaEynxYndIvm1XGigfSP35yHrSsWE_fVZJRg0m-A9hrl3gUPLBhJYHCRuZTLtrCpoPYyqxbSVOFvb5asvHT9MzjPbNKow6XRv3TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=TrCU_QfDxqV1s64BSBSUKv4BXFgc6JxOrU7WpuMz9BJ2q8GvasLKJjaCOZ1fiQsa_KP3j6pZk2-fVBvx6AxSx9CiAL356dqYy0xLJZKgQLwcDgrpvYtUQWdNGVluHwLVrlpyB5msSfIweROnSfoP5QHDo7pUtrwwwBSaq1c8ZfZpOAzI7IIMp9kcMmILLQfftUtAvbtwycS29C99WwuIijLgpXhVxJLLu9tUSWopz0rpou1ezxiaEynxYndIvm1XGigfSP35yHrSsWE_fVZJRg0m-A9hrl3gUPLBhJYHCRuZTLtrCpoPYyqxbSVOFvb5asvHT9MzjPbNKow6XRv3TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-1fYaemp7r3GcuEJ0lGb4xWrVLbiDW7yIV5a5hpUh-QcFCecHgKL_sNL7R8g-ygkZi3tuvnuVSEwC7Q1Kd-rtb9mhsMim6k73dtBdkxClPsalffcd4Dat6uBjaJe5Hxjs0oH_iDFWWbaXr4Km80IQYT7IdUje4_EdlpnCrTY1zjGxkQ9lzdRHhAkLWIqaw4CoR9JGiHF6g1l3yP8PFc6tlhgdBJ3qHJOiSEqWgKHIxkfXcFPfZ6b88587K2ZT4Us1dBy27cTAvB7ahsDzfw2i_kxkH2tG08Y996nFbrMYmZzoHNWcFrOl43AMEqfU1to91JVsse_4s7XCxvb8y5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=jU1GNSnRu1umHUyhqOZBr9aG1w9wbPNA2gN_UmVOXe2XqE8jg-2mPjMFs-SE1Rpb_Q3HuLc9u9S27VUH2fePokJbm9Sut2mU8wBC8hgJE2lM9D9HR-btMCiUDfCzoleqtIXfL1rBdSUSM9boGOhrrtEJVfSL7-CSLg_xBwCY11Xw3ASRBTvkk2fyyK03oZPWHT6b6xJG0TbALYB_6A3yOiHL_10_eK-QW6OeHYO_x90ggpklir6Gkzxq9veYqqEvdrlYuzpuDviAW2bj1tJ4bSUZxnb4UUKa4EFi3NW18Lqz71IseMDXoOGUVqqGRr7UOROy9ZKjXzHpP9Vy0BKrsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=jU1GNSnRu1umHUyhqOZBr9aG1w9wbPNA2gN_UmVOXe2XqE8jg-2mPjMFs-SE1Rpb_Q3HuLc9u9S27VUH2fePokJbm9Sut2mU8wBC8hgJE2lM9D9HR-btMCiUDfCzoleqtIXfL1rBdSUSM9boGOhrrtEJVfSL7-CSLg_xBwCY11Xw3ASRBTvkk2fyyK03oZPWHT6b6xJG0TbALYB_6A3yOiHL_10_eK-QW6OeHYO_x90ggpklir6Gkzxq9veYqqEvdrlYuzpuDviAW2bj1tJ4bSUZxnb4UUKa4EFi3NW18Lqz71IseMDXoOGUVqqGRr7UOROy9ZKjXzHpP9Vy0BKrsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJSsq8guisNyh2lPHWrQYS1qoWAQ-ljjckvJpvfEv0T1Xj7nfgf4O3AdnoMSLytQYS-V-YnHeUXunh9LI6L0FgcGKpaL-TFzzVNU3lY28hku_C3a8kZiODcbxWqE7ENGHuxFcfF8ZrIVcU3P6jsGyhMeeSw6KpLDCGsfBXgYsGy8ng8BF-fHs2xwhH3CpHTyVTbwD6hCwGAP4nmAYNVAr9TC8fZsK6Bg39tu7eV2L5yfIKH0eiLRUZsgQLwCJS6xh50bRcMPRucqxvcBmzBEVwEU6OMZvt76c7qvgNeSYKUKoOiSIigiYui8yn1D46cna3NiLWNIA661w4qBAuLFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=HMIJ46uzDDqd4jaLFLJiUeD73q7HmoAH7jXRLSsECcKkZvnApk25jsefpiVLcufr3RxRa_d4KrGvqw7lRTOce_nYK33Ht4pjKaxcFfnRMLwQf6s8e9KEVrtwQSKcL6-XBpGWzZZt-IAC3vseObtGft8g0viGhIS75fpEUoWO0VmPVeXS0_G2_Hr6cYEeqv3VfkIKPMXPotxs5NgY_0R3EHrQ8x2aZq5HWKRk98y0dgxln2ToIBF24bWz5Sj02T9gHGzWfh_jrFOH1TI3IkyUtEe4PbT-k4rIR03M26vlSWvW4bvwcTBWXtu0_CiUqQmpG4hBIKpFG_HtVut1oArQtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=HMIJ46uzDDqd4jaLFLJiUeD73q7HmoAH7jXRLSsECcKkZvnApk25jsefpiVLcufr3RxRa_d4KrGvqw7lRTOce_nYK33Ht4pjKaxcFfnRMLwQf6s8e9KEVrtwQSKcL6-XBpGWzZZt-IAC3vseObtGft8g0viGhIS75fpEUoWO0VmPVeXS0_G2_Hr6cYEeqv3VfkIKPMXPotxs5NgY_0R3EHrQ8x2aZq5HWKRk98y0dgxln2ToIBF24bWz5Sj02T9gHGzWfh_jrFOH1TI3IkyUtEe4PbT-k4rIR03M26vlSWvW4bvwcTBWXtu0_CiUqQmpG4hBIKpFG_HtVut1oArQtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqppFMsljxg0URN__m1KaZ1KdFQUe__b_xeNdBVwyKDnhdt_Qb0IZdOBtFJizC36COlrGNwL-RVA6uaJOxMT5nqr7gWJhqqbmP6rcwV9AOzUZCOrpkRGz3XxjYxKph8mhgKDKTY0j50drSHnSEqMOG8LZh3_mJruTrleR_khIwjN3ak2ByMvuwvHo3V306V67-CUeJcCzMtSrssR5cEJWYMB_XtsdoicWOxdor-8wrc_RNdf4Or7GKUPqdcokMXtvVEwdFP5-LVs7ASsx8BMb1_6uHPWx99-Vd9LNzVyZMgOG2gLui4Q1gKRGw_U1fYuWwjBDn9P-1BrPwekFB6Neak0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqppFMsljxg0URN__m1KaZ1KdFQUe__b_xeNdBVwyKDnhdt_Qb0IZdOBtFJizC36COlrGNwL-RVA6uaJOxMT5nqr7gWJhqqbmP6rcwV9AOzUZCOrpkRGz3XxjYxKph8mhgKDKTY0j50drSHnSEqMOG8LZh3_mJruTrleR_khIwjN3ak2ByMvuwvHo3V306V67-CUeJcCzMtSrssR5cEJWYMB_XtsdoicWOxdor-8wrc_RNdf4Or7GKUPqdcokMXtvVEwdFP5-LVs7ASsx8BMb1_6uHPWx99-Vd9LNzVyZMgOG2gLui4Q1gKRGw_U1fYuWwjBDn9P-1BrPwekFB6Neak0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7EeZUYTVvx-uu7awy2bhQHHjVPOpc7d7lHYEIH72M9rQG_A0vHFJeEG6jE2SOCpbVl9NBf_-YDZDj81pksDyaWS4C8Ec_Kw1-71uIVTyXWpAY2SWHgyonA2AwGLlG889h1-bdI8EZHfAqvb5v3xi-FnNdpzfivo-nTXP4M-L-dyEwqYuy0c7qTlpQreAJSqN1tyq9qKfbXvR9TLukGt3Fst0Wwg-nc6qlhyh5kjhF9jaxMoL2O4uwsVHlUqM8tn1VFPs5kjO-1rrT9gbe_8lsO1wTx0fW8Ve4Q5w909AogS3c6Qt9dgCgpxNbO3b92guy-9QeCA2oA62Fv08moCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=DY_OJ2e1T2x-XMRKEfJTW2YqoQB0PLpD0dwQeM6Uyj4nHIWrdEL6tLGQsr5uQf4EyY-vju8h7eutT9sZ3d6ncia4NWRKpce_cACJ8WU9TCU9EJ5SDUo-h9VMiQ2HzyyIxFfpdLsC6rTmTpr3MoII-T_lD7jY--MKgXopEFr6XdnN7ifxkhKX7prsMSAZ4_2hs3YSzE6O-sgiq7mi3UGkBJ9EmS937D3V-dRci3iKQxlDT0eeD7W91QRBJCcuzQu0-_eT67SOBzFCIwiKfxMe2RZuF74k_rp0x-U1-tEcdsW07FFztJcnIgSCArfg-neEntuSvvNBGok3AbWxxcixMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=DY_OJ2e1T2x-XMRKEfJTW2YqoQB0PLpD0dwQeM6Uyj4nHIWrdEL6tLGQsr5uQf4EyY-vju8h7eutT9sZ3d6ncia4NWRKpce_cACJ8WU9TCU9EJ5SDUo-h9VMiQ2HzyyIxFfpdLsC6rTmTpr3MoII-T_lD7jY--MKgXopEFr6XdnN7ifxkhKX7prsMSAZ4_2hs3YSzE6O-sgiq7mi3UGkBJ9EmS937D3V-dRci3iKQxlDT0eeD7W91QRBJCcuzQu0-_eT67SOBzFCIwiKfxMe2RZuF74k_rp0x-U1-tEcdsW07FFztJcnIgSCArfg-neEntuSvvNBGok3AbWxxcixMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=m5mnKwd-kKMfQkjuI5DBCUiQkHqUSSh0YNDoELQ4WltCrXtZp9SeQNmv-XrhCbRQPFakzLaGyR1fEoInGn5HfOdB3tOZsKJn7BHYweayuSElF44ipfd9xItp8gD9zM3ZTNAYBn-oAz4yUqCyZMQB1Ia6NSL6bDvnbdTmkJUPYRS5FDUo_j_7fvbloIuw5H27dTg8e4bzLgYL-g7uKgnZuHo3V_wdaku0Kz10EV_MJtZcliha4G5vHhxeGN1Jl36FHOtX66-OQEJCX8EWu2gZvmWZ60BMyr4eMai6dXJnpJaYWndKPcmFNtcq2chC1AavDHII7BfaKIuW5zfCtyTdZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=m5mnKwd-kKMfQkjuI5DBCUiQkHqUSSh0YNDoELQ4WltCrXtZp9SeQNmv-XrhCbRQPFakzLaGyR1fEoInGn5HfOdB3tOZsKJn7BHYweayuSElF44ipfd9xItp8gD9zM3ZTNAYBn-oAz4yUqCyZMQB1Ia6NSL6bDvnbdTmkJUPYRS5FDUo_j_7fvbloIuw5H27dTg8e4bzLgYL-g7uKgnZuHo3V_wdaku0Kz10EV_MJtZcliha4G5vHhxeGN1Jl36FHOtX66-OQEJCX8EWu2gZvmWZ60BMyr4eMai6dXJnpJaYWndKPcmFNtcq2chC1AavDHII7BfaKIuW5zfCtyTdZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_vYwXwg33ZyGR0O52OSPJyrvmx0HaXPgaKFj_s29uNgLV9XNWqMkZCnyzNz119xi2HkwMxotBAAWssx3wrL9x3QHxfkLCuK4x6trN_TP2-z_4vh7IQmalI-6fu0eSW5sx1awhtievm_u9NhpW6pQ_8DywOhTyyiGqz-Fl1GuCRH3ijvdxbfgkpxhHDIcIPrWhzfTezErZ11JrNEFzBCc9LN1OHAsuwKzVEQJvNoaU61K6WksrEJqwp8D-Zm2FkRHS1K2-GLj7vqRiFH-FDjvreLyLC5jhGsuJYBKYDXq_SkUPBmdy5ET12gs0g28KvNYdSEfapZpyo1oJG3NC_VTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=JySxFAomG4qM93ulA3bd2mUKoLlcBuTYkCjdKn73axf7CIz0triTUzc0gqiocj539mDkJOddfQMuyz61G4YbaD6mVwPZgioRihc8WJcZt7H7PDzud4tSuFuYde1ydwKEVHSVAc7TMCcQeS-XuWcJnXPsOOURkJjEf5OhKGcDJHQELf2PGK-CVx9ebNoAEuVn_pau_sWQF8nlemC2d_e-pZDdznVpz8Xu1Wz_s41bYjJhWvh5tXePoIbhAq_mmM8H9nQlOTOtDrnvehk6vPFq6hjIhH0aZ7X0mdBVXs_qgqIyWZoE40ZGF_jWhOKnDEsSJGY0ccpexNM0wCbYvprA4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=JySxFAomG4qM93ulA3bd2mUKoLlcBuTYkCjdKn73axf7CIz0triTUzc0gqiocj539mDkJOddfQMuyz61G4YbaD6mVwPZgioRihc8WJcZt7H7PDzud4tSuFuYde1ydwKEVHSVAc7TMCcQeS-XuWcJnXPsOOURkJjEf5OhKGcDJHQELf2PGK-CVx9ebNoAEuVn_pau_sWQF8nlemC2d_e-pZDdznVpz8Xu1Wz_s41bYjJhWvh5tXePoIbhAq_mmM8H9nQlOTOtDrnvehk6vPFq6hjIhH0aZ7X0mdBVXs_qgqIyWZoE40ZGF_jWhOKnDEsSJGY0ccpexNM0wCbYvprA4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=lmgcmB7sdTrlppeWijSebUqQnrFOKxnVifprcvoI4YIFMXgQJO0Rs97dkrdevTnxxKIZkUkh7VLhlCJ77aTjGmEMgO-Aaidz8lO4ERKYecrnluYNM3rZjBgRAapH5gYaHoPSW5COqAhsBWP2zDDhNohfsx5yjkRynTO0hsVhNmygtVCHwqLEBb__4TOmJBpku_4pRK0dldAzzR2NILcFTUxz1yd1MXKr_H2K-tDR6qVzZLLJqEcMK6cnHP3VqyPYsGAL1dYfZOJhmNfW7NsXw-fr4JaJ7kF3FCjC36brOd7JP1AXwsOc33eCnGCfz21xK_nvyL9C-Ts6IWNQlyE0sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=lmgcmB7sdTrlppeWijSebUqQnrFOKxnVifprcvoI4YIFMXgQJO0Rs97dkrdevTnxxKIZkUkh7VLhlCJ77aTjGmEMgO-Aaidz8lO4ERKYecrnluYNM3rZjBgRAapH5gYaHoPSW5COqAhsBWP2zDDhNohfsx5yjkRynTO0hsVhNmygtVCHwqLEBb__4TOmJBpku_4pRK0dldAzzR2NILcFTUxz1yd1MXKr_H2K-tDR6qVzZLLJqEcMK6cnHP3VqyPYsGAL1dYfZOJhmNfW7NsXw-fr4JaJ7kF3FCjC36brOd7JP1AXwsOc33eCnGCfz21xK_nvyL9C-Ts6IWNQlyE0sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=gKHrqIDTAoBTyWHQaUKWgmN1ysC4AydLuaaK565HWAbqWnmsxVIgv19pnoItkvTGG0f7jq4f8lD6IZb0ONTsKe54zW_esIml25kTxxYoGbkN_YD8jX8eDEt2i3OCTcm55MuF4lmIbki1id-TAq-U_IA2kThpqQCUKZjYwjZqpmPZY6JfMLshbMexy6fpuQkZ4Fm4_W_Vt095fRnOt-h5ATPFjPAUaNENEpJxGsJiXWpkKJJb3c9nW-6rYWrxZwfo68jaNf3fmduJcWtilSXj9LgFoxXNV-BNsd-F-j7hVEz9WzPBXaFaC-B8mE_BocsxmpRHcq_qpqYqp2419a-l8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=gKHrqIDTAoBTyWHQaUKWgmN1ysC4AydLuaaK565HWAbqWnmsxVIgv19pnoItkvTGG0f7jq4f8lD6IZb0ONTsKe54zW_esIml25kTxxYoGbkN_YD8jX8eDEt2i3OCTcm55MuF4lmIbki1id-TAq-U_IA2kThpqQCUKZjYwjZqpmPZY6JfMLshbMexy6fpuQkZ4Fm4_W_Vt095fRnOt-h5ATPFjPAUaNENEpJxGsJiXWpkKJJb3c9nW-6rYWrxZwfo68jaNf3fmduJcWtilSXj9LgFoxXNV-BNsd-F-j7hVEz9WzPBXaFaC-B8mE_BocsxmpRHcq_qpqYqp2419a-l8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=vHW4ZgIIGU9ePLSnvYhzwnk1dNAwasmJgdmOppMAKw9yV2CX4e5jHm1dsrdh5x2_T43hdWQM5T3I57lhcYk7bJFO1QIxw-4hgDePcaQ-q6EYo0IkHM32h7HzMnGR5HM3kQ79GabXiMti4HvcTxaFXSMon9fq9y3glwr5WJoJmoZbxHuxP2DcwWN8L_wfdoMm3ReF2h_FYiGpKOYmNkyqFgLUunXv0Lu9hSwRqxfO2EUX2mTg2emhFJduDDhJCfxLxR2AhYapSycXgA_UN2QowOoAW1aCgY5ynB78ydzDu87VTjgNLhjOP-n-saIDA-yBFLJQ9vThstHJk9ccG5myCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=vHW4ZgIIGU9ePLSnvYhzwnk1dNAwasmJgdmOppMAKw9yV2CX4e5jHm1dsrdh5x2_T43hdWQM5T3I57lhcYk7bJFO1QIxw-4hgDePcaQ-q6EYo0IkHM32h7HzMnGR5HM3kQ79GabXiMti4HvcTxaFXSMon9fq9y3glwr5WJoJmoZbxHuxP2DcwWN8L_wfdoMm3ReF2h_FYiGpKOYmNkyqFgLUunXv0Lu9hSwRqxfO2EUX2mTg2emhFJduDDhJCfxLxR2AhYapSycXgA_UN2QowOoAW1aCgY5ynB78ydzDu87VTjgNLhjOP-n-saIDA-yBFLJQ9vThstHJk9ccG5myCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=qTSDalu43P_s5aEH4NBU7LkVBkmhmW3XxYM382RnP_wxkI-XCdBYDL8xOFJrGeI8ahLQDpgX0ssHZkmmFQZ2mk1lO3Y4qoF3MMTvcknaGGY3pZVx64IDdEiASw5bqcq5p4vmYsb5SSx4Cr7ND7uHtAyJEjNYDicrHBFudyAybCYEyYbzDd4bNjReDHkViQV99lmsZJ-Iotq4Rr-Hk2yEBvtSfG3A_yQzsirYXvZ7mfnCD4FsprxoWkbBRNv7Op_dPJDkjkvFw0xJTT_ZZdpYIi6DyyIZQIjJDafIHt4zNresNzXudu_LIi1URep0rnY6Py10crM_GcqVOPebLVrapw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=qTSDalu43P_s5aEH4NBU7LkVBkmhmW3XxYM382RnP_wxkI-XCdBYDL8xOFJrGeI8ahLQDpgX0ssHZkmmFQZ2mk1lO3Y4qoF3MMTvcknaGGY3pZVx64IDdEiASw5bqcq5p4vmYsb5SSx4Cr7ND7uHtAyJEjNYDicrHBFudyAybCYEyYbzDd4bNjReDHkViQV99lmsZJ-Iotq4Rr-Hk2yEBvtSfG3A_yQzsirYXvZ7mfnCD4FsprxoWkbBRNv7Op_dPJDkjkvFw0xJTT_ZZdpYIi6DyyIZQIjJDafIHt4zNresNzXudu_LIi1URep0rnY6Py10crM_GcqVOPebLVrapw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDamu161Z-D_FOrX6ea4JHVjtQB52lVM1yDYx1Iuijv2Olkp5JK4GVrcvgF4qPNPKKemVgRaw_bWEC1FLcO9K_YyYhUvjBz6q5Q4RsJXAZfjJ6B_6l2GDDdZPGIVver7mQbcpPdNqztmZKbl8WgmQTAb2rj06B93X65kLqI7TLBXRZ3YwPS2trrRUXjnUqPhV09AYTHE1Y2G1CuyPETWCP25Ji4sJ7JH7blT-nLGj135S1Spfp40ZM732fbwtzNJEROGJc0lT6F3fknTbMfGAJ1mE9DXxPweFkLOrJMR8zyconNOgSxTtdXmxCeYBVpzR1JDfR-Nzp_u8wEgdudOvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMorPpk7XYiOhXVSU0LaKeGYpvIHXRG6UNdkdv879B60eQ_q6OF0cacc3F860xpBRRSoqWumbcJKv8ovdMAn5rbqcoOer2QxWNqCPZcaqHhmBfv2p9ozmhsVxYNd9rtus6TxLJIJfF3mejugflSHIhh9qv7P2mbvHOKJKx5i15z6_xBSqOqUmmqgwmnb-QmdbfV5kSqQc-ecVeu4356HULEk0jxJ0ADh0IysKkHEsUmTVrkKcOGz1hCyOzeZB6BF-VYWqm5KOJKNM_eed0u-EhpdtwZf1qMeYqFJ7n_oDWyoHdfbSTOVN93vJIEsCLIhvLmtEkUEAlq9ZqanyD4--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABzJeWjID9zOnU2-xOoDlNkrq1P-aMKcP_RyMtNFoSFyEye1pZ9ltuqGJLvg-C1uZRwPln_S56LQ6uHrRVHjCgyl__VWsRQxT7lOBujD_gQBHsezuVRS-yGLKd95Tid81nB87mSynKTsp6Ty1Fy2CVRfyUVUMHzIzuw1RDBsC72XXuHk2dnJpobbl1iURQap-bQNamhYHYhcBMzHpEcx5-mYWE3nX0TN42H_fTR6nZJwZ9vnsqwaG1Vv2dFze92ts0hIVMtn4cbKFRIiyCJTLPyjgBBYBLq50Gx-QhrQqbYlhOMCD6rClObau4m9SuLEsVGZ2_hB2IiG3IHo3tgzAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Gbbs0ft8Y7isvyStvVLOikhyIuaDiED76nfa0MDCO2T4QnmeDs3XAgX3edCP5G7Ur1wRgs4aMGRNgsLLBCr_1XiY4Pz9cC-tXOrQZFyD6vIx1wTpTpprKHx3lbQFUXNQ8F-cMB9InLrJctuXw3UQDoZ74mOg05vXyP4a5mxcrSEReycwXWL5W_91imer7izZSAzPmGrgUp7djWCGM2cKUjsO7qVABSf4zE25X0LzLMwB2tnYl50PNmlyBadDXpBR-nc1R_dq5Feu3NODLKCSIhepwHG61k2QuGo3J8XcR9K2c2CNOAYYHXUayBby_q1UX4DRVTIhPd4gt63dg4TrOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Gbbs0ft8Y7isvyStvVLOikhyIuaDiED76nfa0MDCO2T4QnmeDs3XAgX3edCP5G7Ur1wRgs4aMGRNgsLLBCr_1XiY4Pz9cC-tXOrQZFyD6vIx1wTpTpprKHx3lbQFUXNQ8F-cMB9InLrJctuXw3UQDoZ74mOg05vXyP4a5mxcrSEReycwXWL5W_91imer7izZSAzPmGrgUp7djWCGM2cKUjsO7qVABSf4zE25X0LzLMwB2tnYl50PNmlyBadDXpBR-nc1R_dq5Feu3NODLKCSIhepwHG61k2QuGo3J8XcR9K2c2CNOAYYHXUayBby_q1UX4DRVTIhPd4gt63dg4TrOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
