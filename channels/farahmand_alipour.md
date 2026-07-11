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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 21:55:24</div>
<hr>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuF20fyARGEKCUWi3BNM_a9jOooamRFNPR0rkC4bTEIwC1O5OLccf8jEJCveW_aaaL4rPV7IVqykbQBaDePx6O2w_selBi3s0LUzCY6iS_e0vYW4K_WktYSqd8NLtFs6e1xbec6GgaJdblmuW8QQ2xfT0rgUO_ptyJowHZqohokwT99DtdbKwCKV8zoOfrUWnHm3iF0UYdHDjyU5ZHhQCAhHi0128BlV7_0sc357IiUBjrCPegTkMvPrR20dVBXwYv9xP3koRWGJtR-YvcaUBvF4Hk-iFgnR8k6-zJMZFoBU9eUKsod0cC50dZYIFF-NjaZtRZ9vgjbSphd8I67RFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=r26ne6TvbHHd98cDEEenuw3JKy-pzc1C_M2JcywUfLFPklxKo_xEXfE34RlleeOEIKXnbq8LvyMv7llNRaLbs6dRhYHGKsTqby-tBUb7cHwatkPeCoaTEaY99WUG-BLjbCEptfn0MBjVmw2w4BMKXbh5dpRY-IwilZc4QHRdBYMQtsrVOV4dkR-F1nS_steNmxfW6o6CY4LnVDBNDAVBACSMLhQLNO7Bwl2pNw8OZkCoOSePk7nQltMYfwQBN1-fspAqsUMGzlcEhhNbtql_4t-byO825LcgF114DCnwXi10uFZZCzLT79xYxpw7T_wAy0xHVqVY70F-BO_dO8JwHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=r26ne6TvbHHd98cDEEenuw3JKy-pzc1C_M2JcywUfLFPklxKo_xEXfE34RlleeOEIKXnbq8LvyMv7llNRaLbs6dRhYHGKsTqby-tBUb7cHwatkPeCoaTEaY99WUG-BLjbCEptfn0MBjVmw2w4BMKXbh5dpRY-IwilZc4QHRdBYMQtsrVOV4dkR-F1nS_steNmxfW6o6CY4LnVDBNDAVBACSMLhQLNO7Bwl2pNw8OZkCoOSePk7nQltMYfwQBN1-fspAqsUMGzlcEhhNbtql_4t-byO825LcgF114DCnwXi10uFZZCzLT79xYxpw7T_wAy0xHVqVY70F-BO_dO8JwHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvig1ayycEUO61gbGKyWPQwWAgtEOIUfc7dj6Uvm8TZGIc-ut-VHA1cGNpDjTZ_GT4inGe5rvqItsMgPqX1UP67NnLkk5_eNMvIc1Tj2WmTL0M6UpW1EcThYla5kK8PAExzocn8pRk-yMknNceJY2yPjjrrW2NagUfO73k1AbIKW0Pk3HFQouvCChpGX6GplhTqiXkcXt62csvBIiRW0X99vVj9H6s4_vNsFAbUILs-CCckIuo8WZ8wCKWOhcC-is2uC283a9dJmWV47SlGkoUo_YdAj_kj987RnHWDMuXJosE0k26QNrBDvzWC9M5H3ZHyUDKn8R7ocAsJ2ynzK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHyP78d_fSmY-vAEqFik2l7ZlkGJy21Sx5I5dXjWixnIxpRpKMQdGkAI1Oq1KSAenwWGwTeB-J37Ym_eptTW1CdqlhbHYgkJxls9JRsQ6XtTkUONkJqS4JY2SPk50aB4rZOLXPUJiFVeAy3u1w6TP0mONF6NlH32w-dKUTKJRoz7VaBhNN7Z95b8cIM9PlEwtvH-zGzX4l1FtoDauqlw_SNW_Xu1nKSHmCoNkqm82SUg5FXs1X_dz-73zty4MuzmLJ-735vEf_LQIWyQ50EBzG63ad77roh1KcQEy0tAt6VCjwrdaVW1OKXmh-XXe-AltoS88ELnyqYCKtTLo7lkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFoTgLRG-08-wXkVfnmUjpyU85d5MEOPeSE2RXukUJ7gcjmFTYlZCb_kpnQL7ZIcAAM_lDv_J4qZLl0hoiuQRaoKA_6j-aoodXfesfc3KLW2-ibWZjxvxqxsCsKOE-w13vSFR6YCpn74DYo1NOBBYyEvAsrIYpZHslnt5ahw7Y8rBD5zD72zEjJb8Xbr82oFCT3fbG_O9-gKukh3C2YomWyaoxAn9HMpLntkpivRZrpZ4r0DzEYp8eqAocUxAJO47HRnA1D8xjLyMZVi-YwcsKo3Qk76hvz83eeZEW9VoL3t6eBs0cX36qSbGuiRA1OhvmzravFHMOyi9dx-QJrwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6fj-XikOE_vV6gn_Bc8O6-xIM4wgXc4YypxLCBQshzeZI2ex4bJps45gE5IffGwgyOcFmOIBXpQ5LzCUMaN_tBTveENWfWCKP8xENhazzUOnaFAp2M-41EK7Ymex4ZhS70FmJAmyGgh9BYHdlF6czYGHLcTQPXfB5Pl3iD77I8DjDXJa0sUIEh6zuEi1VR39aXBilQoalJgeV9tVniQdu1Klpw0ZHKxsgfSfFTz0JXsGf25mcyADsfQjrHKuvlh0iIPGCR6LoO9Jd48T7nKZvec_4o_-CsQq9qSzSvN6_jHrdi6Ysi5U9_kDIWzg08jSHPScvB1Yh7KR2t3-wfS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFBHiFZm8fAMSiTqrDXjhuuQLRrHCYW6o6i3gDS1k0IZRWi69pH275dYJ3vncd_qv0LaBLjeuImSWQF4jvOWcLQe_bjIy2ETCKNRCRm6IjzQN6ez-mWRx2eViQOmOkIsHhhRDmBvMb7OM2s3nYUh2jcR6kuCH7JLNzWv7LzEm2bCjc-Hh1IQSPv2vf1f0cnMpoqyCRUJFvcDgAOLeMmnjy3xSSDb4iZEopRc83z6Pm0_4Fd4N0JK7TvOgk4zHjvEnR4Cm8ZqDDYTnUsoLZ5cXuSJvAw12Zp3C_zTQd1nbIhyMPOzx_7LIU2o1Lnph5eoDgoXJZKw0-Dpfdv8lX24fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7R7eylBN0enMjg8hm88svdCf3cEvTZe1oPGwvNTTtuZ_Poo6kWwszZNxkP9YDOoQz8gl3nHRO8iqsKAjKxECVEihOSVEEl19bnMB4Or1sZgboVL2idfgCgTmftnZNtxDR07vFbQkt8ko_JW8wCybvDUROeNKNd_WfR9B3E3enI2VmZTkhxDFpK53KIiTHCrr-soAF3yepX0g3SoEEFFKXNZNABFqyw-NDmHiXUMhgzDCHNyoAYr1ybZjT846oN3TXHDDRPTNpjw1EOJFXYfBzkCjD-jFYgKZnGr6UBMWfag4de-nAyfDQeS5jUZaweFMcSa1QHNKziFtcuiJGIFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJqeGgnUgFsLYEGoF0wjtOZjP2qe_2TP2VRrv97QhG6uTnpybpsTh3HXKgsPeGpT7TMYYMsg38-9U4z4BMNk_8LXPoTRe-rzqkp1cWcai0W2sdfpYvKAMfkTMdCFATiKyAJt5aXrHdmA9pFsjm5nKy4Q_vIzFB8GsHxaHi00LyGzkC3Geehz9yYc0sTLGLNopQz1WU9wEwZiJZXrg5lgw5dqXpQ3g1BYKq-kI9ULJql5MF-pV_zMbQ4z7LPYiCCOMKsdhJGuTHi6A4eOeEL6dS7kszNlZz3O0yckf6_rQjbODb-zn6U34E5CjjgKoauQ7Vf-UpnvUbBzuv4iIry7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsTYX3DBh8sLkAXLHoWd50FP18g8zgnxGK7TdVmwy2M96aKiXVMTRP0XMMXnn0FnLn9R8epW9YUsUX3dUbVjV4JHNdqZTSutcKjrCCL5PvzU_JLdbA4gSn17cx12cIX4MjKXZUXKZfnsMYMA3_4reLGpVkRHsi3IlGxVT6wxkFTLAIkUjug36uPnXDN9xezTUfEbko9JIFbkRHCIecWJr9TIgmV5u6SADKqcP0HnD_Nyl_yvXT9pLvajcdhxkiMzbCGjwLUm1yaLpVWX952xeeLlwhpZaL38QnJMKEGnauoxC_zHP9Z5n2K3jZKibSwa4nlT9KJrWZrf8eae_13jPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SToNkh2f88FuXCRC8_iTbycUeFDynCAZGGX-xNJ_KWKxirVcQCsxoIYbDdUUXjTn1ISR5eX2bmwAzFjNWx042fPg2BKWcU-5_96PpcoO4gOidGiQ_dMS_CzL_rbxGiM_CYP4LodvFOxNf5YHoPC7T9ZGLMMJMVEHxTCKuvSWRPe2WsxMx0EO1SFOpEbTZx2fvEl1WM0HV1tRm0MsskSiOESBZaV0oMuTtxK6ud-gm1LHA_aIh_75pIAMiMD7nWrGaakatgJiv99GSwjceG73nf2FKR59fYXQKLsR-QBjqjVbrT9lWiNGO98r_GvsGiDKua-yIM0PnNF1ouRjxZ-A_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cckh-0JGHdCGOdzULPBzpQrKI60a72OEB0g2d1sGa5U5B6ak2yK4jCR0ZlssP1kWa6UaOjX34HtyNDS_bb0_SsfcKoTshpCQDCHTS4zEVcVVlJ7MuBb_uOIaNVCa1Msv7sp10wmwOCnhViZhnvTzRbfCLmYFdck4cF0poquZ9qzzvRd1YteQGKsxUOVJsWCM5eW54_jE3RtilEaxlBDJdCno47EpUC8SS1UFy1xCsmoCQZO6M3-E7n3hFJA5Imz6lOaTGsvkEdverMN70uLBq_xhLVmbkuYBWfNwVamY-TxIZX34Y70_DAyweQumZNam7sXpgaGU28piySdHn--FUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSXYqGV81PaoWqdnORusYw7k4adrneoUGS3qHi1NcfrJO7O3vJVgI5ykotcjLI0rVxSi5y2oyj-X2pOM3uFiXCH2IyfIxESIkqbZso32Yl7Wiwr2oyU2qIHVcFHN-exBTlxwc3ohfIjykwSxpmlhbburSK6gR39ZdiPQDaMGluhuvDTJFA2BbuH0JhfTSIjSoGYE52ag2qPmOR3McLHSwerKPLb8dEoRLIp5-3fey94BLxf1qD-gXanw8c54GviIII6H5XUcvY-G45WISmiMEHJVYm9oAkcR1Oo4LPt69-t59KV3sfkYGxxYB7GiWj4uVh3Qv8WtluUopWUmVoz-eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TChws8rhvIqg-J_GOVwuZ0s5gmHNghkFIOfSiMk7AIemi4_mUFuAIlb6gQSAe4pAqvDYfJCKYse-bbU8ECpAPZKFgz1EOx6FdvSWLdh7xn5SdtE5hqQCw66ZmucxWlYHGVg6QkM2vglQ0ffURx6FmbuM1Oa5SjVdTta-lsxUUhLgr13L0ARyyGy5yEHfcEYc88UShhAyKve5eX4OG_rAuYutTrLJ2GqHF-z-xeAFU-XLQvZF6SR7RAACBGAsOC_jp2m0F-Yh9Qq-Ke_5JG_W85sGIYPwBQvd60IIdSb3o7uwjUAVTZqbnn7AK17WBv9tJuAWCwnon-bmNiX1nloGgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhtxsgIe9hMNCTdi25Wi_Tc9EsaozsffWzQwNosQ5f_32fSMxf3yLSG0EqH16gIrR8lGXzJAfXFK-ISx1hPIA1xmwZPi_R0eolBBPi_8aqtWcSvYq-DqRtQLdthS8DeM3sFXYdj_XMqxXRTS0rBuoKUI2RlgBHw1EGL-vfAW0TtKk5s89EBuw59CLvEOWsyR7JBzFRUU7qbKnRbphjU2uHI2s7-x5m273b01hTEefJBZQUwiRXAjLZMWcpa8fxXG3BrCETe9rDCvQPhIxfc64_T9iqnD2FPh0G0HifrtLzNm-hoPVKYeaHJpud2FpSfcXmdjaMsFg89rE2RvKH8HHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAgBgKGgjwPQo2G6UF44kZ4-3Nexc680fiCyUwmkWQTbA7VJyq7FaR4ViJwQSHTRTFO9AEu0B_TY2M1O-SFJO14dsVwzVP2yducgXvBx6Uf-ifhSmnGXxc7fAPyvDzZeK065vR0Gyl4Lx0GZt9SthVJdGB4AW9hGS3qVn-j6CGa9ljVQ2tNJfCwTKqC8DTdXT12CyU8kLjCTI8Fu0EBwjAqNdGew9dlNIozAbgd8niiXkYtYoQDaFgB7jMYWjRBE0zV82eI2vK64cV1Y6WnavxDOorFAmjEN2O6zpp--hO9GSeF5idoIKbzz71mUrmrQQ4NjB4a8krC73pB0Vay1Dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=gYG-AeOkLzZRSi6pjRe8Tbv6Dq3Mrqdy0bZVqyZ79qT0xfzcdqBM3J72HA8cBL0lkHeFExWkDbhAwFepiyZP-pzcGa8oPuECiI8QAUuqI-QnyXfgnAwA02umzvbiPhSobiHy5MSctIDoNhiPywW4iGXvP2mMSs7UfMykO0TD9mAIU2It72ItYZrV7EDz9lhu990MmNtE-hKmW_Y8SG7z6-1gKlCoODwlTEPmzb24dc2nrq_f6LxakR0_YZESyA1cPY5HgSr-INgfitxh8u1g127-F8Eqtw7u6s_bVhBIuJrW0koPFZQPKtKKwqy-OeJusOtilyic7yRkGNBC92vvBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=gYG-AeOkLzZRSi6pjRe8Tbv6Dq3Mrqdy0bZVqyZ79qT0xfzcdqBM3J72HA8cBL0lkHeFExWkDbhAwFepiyZP-pzcGa8oPuECiI8QAUuqI-QnyXfgnAwA02umzvbiPhSobiHy5MSctIDoNhiPywW4iGXvP2mMSs7UfMykO0TD9mAIU2It72ItYZrV7EDz9lhu990MmNtE-hKmW_Y8SG7z6-1gKlCoODwlTEPmzb24dc2nrq_f6LxakR0_YZESyA1cPY5HgSr-INgfitxh8u1g127-F8Eqtw7u6s_bVhBIuJrW0koPFZQPKtKKwqy-OeJusOtilyic7yRkGNBC92vvBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=v_H9b9zyawgWtutWxVkaF5LbefEsV1e7_Hl2nVGD0od76YKbKmMubXgxH4oRA1sLXcZDGwnbJGWXzS-Q3mnVqMK6B9HLhJjhEFUHOxOYsF-ojv5oNdJcR3Z30Z_2jny8mvkLeosFcK_cxMWflZjMyV2ORz6yR7a6Ex49aDdqwHJd3sHIKZocTmQGOf41HJbGKLdTD0xQyPM5eA7K7178syojNn8PHCqwNduYQvu5EPMsmVbeJAD8yEAKoF65rJIYSfx8FoS849-g2gqAb2LD9AEgliV58mh_F4mSS7fEjDgm8-IyrnI1OoD2lOPn0VpF6xxY-VIlw-JMKKlxvHumIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=v_H9b9zyawgWtutWxVkaF5LbefEsV1e7_Hl2nVGD0od76YKbKmMubXgxH4oRA1sLXcZDGwnbJGWXzS-Q3mnVqMK6B9HLhJjhEFUHOxOYsF-ojv5oNdJcR3Z30Z_2jny8mvkLeosFcK_cxMWflZjMyV2ORz6yR7a6Ex49aDdqwHJd3sHIKZocTmQGOf41HJbGKLdTD0xQyPM5eA7K7178syojNn8PHCqwNduYQvu5EPMsmVbeJAD8yEAKoF65rJIYSfx8FoS849-g2gqAb2LD9AEgliV58mh_F4mSS7fEjDgm8-IyrnI1OoD2lOPn0VpF6xxY-VIlw-JMKKlxvHumIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ej6WwwqgKfzuhx0igDUSxJ4mhCByrnAA0ftV1s1TBJEtw0mawrIwaSswE1ximdX6UXd7smcpmNR5Mh0OMpf5kMJ7unZL63tpK8yw1ZM6_TKtyHnhabN6o-nh7-z3JFVB1DoW0dajZgm0zt15m8K44A_WVP_vGbBy6c_daLK7cYpLNitZOkJAQa6tgd454WUNch8IPKD9u3D13ZW7oL2LHCqbY8ScJZZs1trq-MFICQmrLTU1C4hwkJ8HQObnAlghj7S1FBh0IVbPQqxzx8eWjoNoQulp3mV3N4IhEoKDaVR0CXqsB0TheiJnIDQe_n8HsFwfV1xQlu-w4NJD-QSgug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q5TqrtOi3QiIPkDdZvDbvcRrit3spufm7OIqANlHP0JSaspkFEBp5gKFsbKIUtAnT0sgm-SfZiv008ryOMEeTdiqHMz9HhTH6v4qQXIaGgrVHBafAV6Dt94oa-kePs7J16J8ZZOvs77nhrcH6bPRA6aJsViTubT5bssEdcz1-TTSBZylx_XEizOxX-wh6Jl7lbOsm6mXoCFJVrM4cTMzoP_ch6wahYpk0XgwXlsAJJ-f5qk4U7BPNFCBpd4d-BnkzbzSpweyU8IC5WZpEUbyDvG6Kw4uo3BNxCoUyX05vh8o34ay2khp1Zm9HXvGpP75Ywly-Vu2sEg8zdLVgxjKjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a57d5CRefopiLTvHOXTyvEjF1KJ08UGu_IdxubbWrxY-kMi_wraTwg4uQMI8WMR9L5C1XcOfQ6yziYI1iXInDQjz1JQ7bzx-YP_qKmeXocURA7H-Vf0aBnH0RdjVKhTviqdlt9UD_cwpWV0i1nwAMYl3p0dvg7pGgIjYib9is-pxKhKoXaVZuXm96lIXC8qgLaXB4siE2iO7I9cWsdu23id5kQAOHjlrJVA2ie66uDAyU4dcIeJ27aM9yPNlbcH2wgi8CEZEy32j5hlfNLUTEdOtLPB0Ghdex-UeJs69tpziEyEUrBFf1TfR9IKyZJZtuikMz1zkJPzEmxsMh2DN-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lTpKGkYbYk1V0q_iPdav6Qa31x4XyjMJNfi5-FpzTMISGHg52WFivyRD3HVpFXQglfHs4jZByWmUY1tq7SsDCDiF9X1pfFG_Z9n5cTLmB-V3P-B8I9U9SmDnLxdVk9ATQh617UPR_cz-4QyfHhqPsk1N7_iNmAqHuLwxkXxInzzYxJydSf3ssMDVMqe3JZ22g3AFkIQsXrpGx1Fg_Vaf-8fcnY_9gWrd_XOIFMWAFHDWtctpfsAdxS7q9qUFF89NolMtcIlhF7KUO-F9k_-RVvZ-cy9NQkRcoJXRMqkvmcH97PSmVheIZuL9CguKToSPGhef9h6n3DMGrrxU7UPHg9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lTpKGkYbYk1V0q_iPdav6Qa31x4XyjMJNfi5-FpzTMISGHg52WFivyRD3HVpFXQglfHs4jZByWmUY1tq7SsDCDiF9X1pfFG_Z9n5cTLmB-V3P-B8I9U9SmDnLxdVk9ATQh617UPR_cz-4QyfHhqPsk1N7_iNmAqHuLwxkXxInzzYxJydSf3ssMDVMqe3JZ22g3AFkIQsXrpGx1Fg_Vaf-8fcnY_9gWrd_XOIFMWAFHDWtctpfsAdxS7q9qUFF89NolMtcIlhF7KUO-F9k_-RVvZ-cy9NQkRcoJXRMqkvmcH97PSmVheIZuL9CguKToSPGhef9h6n3DMGrrxU7UPHg9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=WAIKCcabraN-Nl5qbkcWCUYsC9y2oHmhf2fTwosI4n7oQul0GnHlSk0xoCLYNYD1Su14n4bxacxBtsdu4W1gDQbHYjocFhYAznBIAE4d3K-B_59kk7JHBgR4NkP8baCOp25aepA2qV0DmZhxBJ-tvJHq-Rwu8DV7nTIuM08sfmGOiKtbMY5qKkHtfWGLBWqfmf2YNgLeuFpmYDcXf6VutXY86kUz90JXZrzp8RexolfrWHkbm5KHPjZupc7IDtfh4bFvhZC8xCS0mAUpE3TYCH78mJIlJfI1zosbwx4WrtdPkPkE1b2xey7FSOfFp3MLdnuPKZZV8oiDadhdL7qOZBXIk4YPFefjC9o7tLqZi-xvSAAxsHIaK4PHtKbLUYzGxo6hvOHl94zabuXgrlpTuQct-pcLZ6Vzt545TBynNA0wtfyP5scd9sYnEQZLY0CL-gD-ViQzozGWZ5FxZLWeR7OrPdyvPA09bVKObi-Sugeygh1UZ-Ie9AAq0bGs-Gsrk2osvrzV0qAhM3JUlAeaiTs6KM8Y5Z8cl6PGdHVeLEXZ-QQMss_X-x1s3nOjJM-5QbcIZwFdRiUByok5Ql6faMeDxzuXScK0he7ighUvnA-r9OWNcy6If2IFIDdiUJ-BnZjEHeoaQZ6jdwOS8BcOm8jocqkjfyK8LFynC_hE3uM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=WAIKCcabraN-Nl5qbkcWCUYsC9y2oHmhf2fTwosI4n7oQul0GnHlSk0xoCLYNYD1Su14n4bxacxBtsdu4W1gDQbHYjocFhYAznBIAE4d3K-B_59kk7JHBgR4NkP8baCOp25aepA2qV0DmZhxBJ-tvJHq-Rwu8DV7nTIuM08sfmGOiKtbMY5qKkHtfWGLBWqfmf2YNgLeuFpmYDcXf6VutXY86kUz90JXZrzp8RexolfrWHkbm5KHPjZupc7IDtfh4bFvhZC8xCS0mAUpE3TYCH78mJIlJfI1zosbwx4WrtdPkPkE1b2xey7FSOfFp3MLdnuPKZZV8oiDadhdL7qOZBXIk4YPFefjC9o7tLqZi-xvSAAxsHIaK4PHtKbLUYzGxo6hvOHl94zabuXgrlpTuQct-pcLZ6Vzt545TBynNA0wtfyP5scd9sYnEQZLY0CL-gD-ViQzozGWZ5FxZLWeR7OrPdyvPA09bVKObi-Sugeygh1UZ-Ie9AAq0bGs-Gsrk2osvrzV0qAhM3JUlAeaiTs6KM8Y5Z8cl6PGdHVeLEXZ-QQMss_X-x1s3nOjJM-5QbcIZwFdRiUByok5Ql6faMeDxzuXScK0he7ighUvnA-r9OWNcy6If2IFIDdiUJ-BnZjEHeoaQZ6jdwOS8BcOm8jocqkjfyK8LFynC_hE3uM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6l-nz4tsdeOz_nqXUvuFdiHnvCrp-yyYT7GMUdoTrBxWlTc49inSVtRKAyzfMVxH03j76k5du220Qz6JvKDfmE3YwGM_fSIpzhbMVd5tOss48Yvf1j8zjCnpMrZyTC4_xJWyrQ9HwQKdgOccue3SL_9CCcNlvbA4SKocuuDx2zhIBP92DCuCMGKqUhhGfltpyBQN2NIqRJUBhaSCI1dKvhNLMH39ZUOgH1zZzSTrlF5HplL9Zp60K06cT3VmoGxHjRJ12m1tvSlv6MhsrO_trmO5bGfbOCPj2EYlNg5uKTf55rzlm8lixxVVbUBmsLW1CpM5SB5U9oSjm7YjGsHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPIewn_--p4svS_uPs-0Ja-yNv-NJ7tgLuRIoz7-sOUEp8ToLYZjo4pQDGHGsoNzjxIFZ9_AeorArqp8oeRk_6gBTgwr28uMnBmKqDwF-3slY8t6mZHFWEEsUOuncbplerG_0XLqWbO73mST3ZTLUUQEJ6w6QLXi3Eyk2Cwm2G-TZFlYa8DtefWbRnA4PYtCeDnjkPqWFV3Yb-qai58iDfUTWIe1D_th2K7z_5tapJBa00x5OUOpukaENchICvIF0-59JLuZS9Ayjw7hxORC2lGiCqpqhyVYa4v5pqTkfk5lcRniiPSLPzQO9v2zuC4WiBWVEXaGaxXn5TEFsoK0RQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6rh2NeFxGl1kuQQegO1GaVOQSsXE3KLhlCC5uDVtnwSKV5AEUlZ8msk2ps_z0iY9yP-jm5TiPug3TlvNPSxu7peSNBheCG-_Cwshk9NklUnxIbKcZja1WBTUQFLKQv8zlujFkuPMuouw9Ms6MTajNKABQrmPnR-_pSPmTqKUIQVL0vjdL-fr-r1q_eIymoxm-q4rAIMb7-gU6CVsHFNK7Uj7llXAIWio1g9KLhEXnn7_1uTgClWq7feyDrU9xPJuyrlfm_WsaZEBA_7FD2SPnyi0Zf4JkAdzh2stoykwH4xdbG16-fGRwc3PRyVI6SgWzSxqto_3ioT1QWMSxUatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=VSOGXIrea1cNYaP17dkA4o4dR83sClIUWtRjGzPd1NOnfeMK1YSeUKRs0_DXpif1iNd6YTkyqELVvfP1m55PdX2FGvzQfKCwsDyi43w8_NcZCWEQV0pbhKQo93rgRIqTIaIAKMIr_OH1XjvB3Y_RUdibb8tCZ3xFgj7tkdgguII5kF2qhh8KMG1oBRrcrCFV0BHGSRzRxbwCTdg3esEWSW9vAE-rxXt55cmqwYUmqyV6g_1Jl4SMqAYa-nENPntCSykYXZcLOCxPdKbKOj4HsJgaf3c6aaxaqhdyAUpL3-gJVrI1CTzektHycrC5FbSaXCnh29CRa86GIBEGJWnTTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=VSOGXIrea1cNYaP17dkA4o4dR83sClIUWtRjGzPd1NOnfeMK1YSeUKRs0_DXpif1iNd6YTkyqELVvfP1m55PdX2FGvzQfKCwsDyi43w8_NcZCWEQV0pbhKQo93rgRIqTIaIAKMIr_OH1XjvB3Y_RUdibb8tCZ3xFgj7tkdgguII5kF2qhh8KMG1oBRrcrCFV0BHGSRzRxbwCTdg3esEWSW9vAE-rxXt55cmqwYUmqyV6g_1Jl4SMqAYa-nENPntCSykYXZcLOCxPdKbKOj4HsJgaf3c6aaxaqhdyAUpL3-gJVrI1CTzektHycrC5FbSaXCnh29CRa86GIBEGJWnTTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmRIxixpIZNGUW_QJEh628srru7p6nw9XSrYQFHRRdXRRY5QvXcVqdH7qWHYiIvmv3p9MoqaF-ZmuhvH_SOOpwUtzYbVSnfIZX0oGxFjH4fna5fpR9TcMzWlxU3lcAlsJqW-E_cZEKr0vKp2oonwWs_a8dfkhpRmsKt6E4zw2juYxLD-6lHwEv09GW1-reRHbpD3cJKlBFKf6pRcQoqzsOvsVFLgj-AU81_BkDLRQVedtq8lGMPO4ItoW427Isr4N_1m7Cfr5o2B26_xzs-_LeBl870ciBy4nnnxoLGfEyhVTcy5FvYWYtpRDSllWkXrDzrif61UALkD3c-IH0dXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=u78mCh_rAZ2ILsi-lizwyEsxfzPpeXmL86YQWNM-feJkmUemRD0M9bmpkADDA0hlZbwBveN7vl9MjzZfCN6tFeOT4QEJ9nX1ijhsBXY34cJK2cefcBFwBS0HUOEP4gr2RDBqqCWKgl54enovN7tspYh8Ns2DI1tq80D5BToCmYAtB6KKT-j8uV5FGmSJ55kwC4qUPk9Kw_XLXS9MJQjTOjVyOkrOrAjMSgimOb956ItLHtqHVNHBF5X6aEqhhTj2XLKiKfAuQ8C-B3nBgWu2UEWnFKOvob1oP6h6gEbMVMA5yoOVl7JIR_F22_6-DnQ7fmMZwy8egjh5riaBgTaDJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=u78mCh_rAZ2ILsi-lizwyEsxfzPpeXmL86YQWNM-feJkmUemRD0M9bmpkADDA0hlZbwBveN7vl9MjzZfCN6tFeOT4QEJ9nX1ijhsBXY34cJK2cefcBFwBS0HUOEP4gr2RDBqqCWKgl54enovN7tspYh8Ns2DI1tq80D5BToCmYAtB6KKT-j8uV5FGmSJ55kwC4qUPk9Kw_XLXS9MJQjTOjVyOkrOrAjMSgimOb956ItLHtqHVNHBF5X6aEqhhTj2XLKiKfAuQ8C-B3nBgWu2UEWnFKOvob1oP6h6gEbMVMA5yoOVl7JIR_F22_6-DnQ7fmMZwy8egjh5riaBgTaDJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHdzzqBzF5n8SjTzhO5I0qGZSnL4spntJayqJMhJpEeX2jZSl6KojvEAwpuvS0U9ABtVZ_g524gDccAb7bCaw5T7aq6YDiQJaEaWRkapKM4UKkLybQ-YuQ6XSRPtteu1-xyZ5fi4TMWRMluRPxXhmgQ1NTMzhpFAo-LluEWhvvhw_et1Tg98l3kk6VB5pQRMoLMWbtSmPOLaOMMRi9-z6TvoTVMegsMhqCZdXieXBLGgiqnBerNWru2CiZQGQyqR2w5BIZRXvynx-OipWDd8XcPZ8HY2pTMvTuwij_ypad0-wBK-iIRgk-kL-lDsNZ8VFQM96CxmLpFRiuGXA_HynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGs0hp0PoFFHBzvj9X68HpP9mb4davmffvaqRZYd0LtI-BBJ11_L_tq-EdiHEeQHCSwfmlwWErN1L5bkGC2uBqR_OWAb_BeUlyKLNHeiSnLkbTBPUZN0NuI_Xk_1gu-2U3hi8QsyqJDO_fyTJ9SSllJk347RTGN69emS73kW3Yi_jN8rIVG0NE545yZqz10zSlN48uAIX37Q-ANdMglI5-yimTkKLo49GMob7kNHw3RiKlb-t_oCijNVxInA9wldMJ6d4ta14XSVnxNCzFgYjsH7idYHUTGK4ue3W_uxv3YHX_bKjIwi3rbUtO1Jtp6tRV4ye8EhpAudU0HbIjGSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=XH6OtWPs7AdcuJqVebyM1_ZJ91FfAobHRdzWAm7PkL7Kv_gFQvcRPoDJBSyBuAGzlvN4c10UGzFzJHLV6AuktvFBQOxkZS4RqgyqGISNdW57MU36yj6zhQPlsd4U4Vr0RlFkJpJIx2FIQzd-HgZQ9E1W4iAweFDeICIrZ82vgKLg-ChQ5aH2nMpvpzwjeGX7Z3ByFuHJthI9sqO88unKJ01ub9Bt4vaPxhnT-OtOqu2Wm0sJYyZfCuinxODvUurjXnERGYnidbI4cUyhiyYyF1DnDis7Oor-XRsEIiS4PjkIX6IAo4ZktJUUzApvOZ0xLHlwkWigw27R0CEZTZMEHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=XH6OtWPs7AdcuJqVebyM1_ZJ91FfAobHRdzWAm7PkL7Kv_gFQvcRPoDJBSyBuAGzlvN4c10UGzFzJHLV6AuktvFBQOxkZS4RqgyqGISNdW57MU36yj6zhQPlsd4U4Vr0RlFkJpJIx2FIQzd-HgZQ9E1W4iAweFDeICIrZ82vgKLg-ChQ5aH2nMpvpzwjeGX7Z3ByFuHJthI9sqO88unKJ01ub9Bt4vaPxhnT-OtOqu2Wm0sJYyZfCuinxODvUurjXnERGYnidbI4cUyhiyYyF1DnDis7Oor-XRsEIiS4PjkIX6IAo4ZktJUUzApvOZ0xLHlwkWigw27R0CEZTZMEHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=pvfIlgL6699_pedoc6Si5s1CUcWQ9W7dA-RLq600wa1hs4YYUEG24nFh0hGQrva-EL_ml0Ve57hGuk9XFNOlrkzYDYwKtqlM-HVYZ8OFRVdmp31tz6t8dXgvrzabKRdKWaG75phWP9bvshG7f6loHn5EU-ZrFRI2uOxfAN74Dq6PzT4uc9-ec2sT3col4koRIzeDTzswfTk7TR3RJbVE-yr7Tr82YHVuc-0G6m5dFb_YKyzSEmCqgUOfKOnHcaeJDFo_ibnwmwSMAtOAyvVY9E8A889qA-VbuU1jd7SbTSaSJxz-FQBGKqD9VNAstqbWnKmWIn-Wd0hF7K2Ls5UglQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=pvfIlgL6699_pedoc6Si5s1CUcWQ9W7dA-RLq600wa1hs4YYUEG24nFh0hGQrva-EL_ml0Ve57hGuk9XFNOlrkzYDYwKtqlM-HVYZ8OFRVdmp31tz6t8dXgvrzabKRdKWaG75phWP9bvshG7f6loHn5EU-ZrFRI2uOxfAN74Dq6PzT4uc9-ec2sT3col4koRIzeDTzswfTk7TR3RJbVE-yr7Tr82YHVuc-0G6m5dFb_YKyzSEmCqgUOfKOnHcaeJDFo_ibnwmwSMAtOAyvVY9E8A889qA-VbuU1jd7SbTSaSJxz-FQBGKqD9VNAstqbWnKmWIn-Wd0hF7K2Ls5UglQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=HD_UOMwyEHF00dn_nT9nsY7filmwM-I-9kMOJzQYF_IMnKmJqDkqbJmBlsbHrQq9Vsi2dWFBDeGw5rq-VwhgPKqq0Gf78mCNALcV9zxUk-nslpVq2MDqKHsFRML1wF01ZidhhHm5tpLHcEC60qAL9Wm3Wir6esMpA7q0kTmL_MfDhwFm1NHLXWWvkCtH2ZPNDTdGPlEOJM3nvXn7OP9clzOlxhrwUowX0fwbCKXOgFXPwDsLAEdECNSCvmczas915r1kzvhzPL3il-QdAOc0vaMJ3CTd0J6Do0AaoM-TWWVvjRG_FfqA5Fi_FOAwF03O22llgZnsxmoI45mZDlaZnb_obMGCxXeup8ITT4N7CSmwAwi2csDMIArg2mz7FzjFRkJojAnmX32Os_61PL8GMohZybBbIK3xYkmEsEyfbvg-wNVKrqP0SXzMQQKC3G2mFvskg354457qPrJ1s3huuDMpfKOtuKHNOPE6OosIG9Q3CXxfc22R4Ebo_Z2F2fvhpEYTTL2L6ejO5gdoe-7HN1Lk84_2zPQTEpADvX1h8-b_BotJh7OtV3ZK6q15dpxX_BI81vgLYSK6G7N22jKJgepLVc5DDr6zZ1L_bOHj4cLhGc7RojnX1OlAVfNGLdkQU1jLq2Pgo6_zmydxlBKkleKB-npGb_epKUaHksdLSgk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=HD_UOMwyEHF00dn_nT9nsY7filmwM-I-9kMOJzQYF_IMnKmJqDkqbJmBlsbHrQq9Vsi2dWFBDeGw5rq-VwhgPKqq0Gf78mCNALcV9zxUk-nslpVq2MDqKHsFRML1wF01ZidhhHm5tpLHcEC60qAL9Wm3Wir6esMpA7q0kTmL_MfDhwFm1NHLXWWvkCtH2ZPNDTdGPlEOJM3nvXn7OP9clzOlxhrwUowX0fwbCKXOgFXPwDsLAEdECNSCvmczas915r1kzvhzPL3il-QdAOc0vaMJ3CTd0J6Do0AaoM-TWWVvjRG_FfqA5Fi_FOAwF03O22llgZnsxmoI45mZDlaZnb_obMGCxXeup8ITT4N7CSmwAwi2csDMIArg2mz7FzjFRkJojAnmX32Os_61PL8GMohZybBbIK3xYkmEsEyfbvg-wNVKrqP0SXzMQQKC3G2mFvskg354457qPrJ1s3huuDMpfKOtuKHNOPE6OosIG9Q3CXxfc22R4Ebo_Z2F2fvhpEYTTL2L6ejO5gdoe-7HN1Lk84_2zPQTEpADvX1h8-b_BotJh7OtV3ZK6q15dpxX_BI81vgLYSK6G7N22jKJgepLVc5DDr6zZ1L_bOHj4cLhGc7RojnX1OlAVfNGLdkQU1jLq2Pgo6_zmydxlBKkleKB-npGb_epKUaHksdLSgk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWvuFBajslh-ZRgbufKpg8wF2wUtbvDYVAAIAP9fUXmoCwe9gXpW9llIMb0RhbcIPVXq-x5l4q76j0YIct6TGn-WqolIMK3g1izVW4lQDJhI6ipRmHcDifV0IC6NJaD054wvhnM8NuPbdwHnqBimA1WtpTOGCUXvQD0aOC9lD8ej_0tuXQn8768ZVUwXpYNxxMXcXuDe8Msj3FkBKQRwiJSklR76LrQs2o7j6wc3BJOEMd_RzUB7p2Ad3dhHEKIC0myQ8fnK0aC_YYvZ2XCQzw5mWqe-HKu7eW1hvn60l41mnwfNWk2EcAgzCANLvjH82bRovliRKiWUOE5cZsx1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiLhbS9CBjvlzoa0e20dv_3Ye0Tb_LBnobfJLg9lZHpBbiTCU5hsXZD74Z-yAPueUWj8VHFagmlDZbRAvtQgHoNy9wsAZdKwDnQUesgHPqKe9f9WzMn_8EhWFr_V9ER3ANm_2w2df_XxoKsreH1sNVzITFLNg4kNqFFKwi3RqZDQvt0uMVxQwucFw9HRhuJacMEJ0O8hMCKLcnZG7YrfUJQ_RU3oBBv-RXtj_jx3CnePHQ5ZHVwo2qXd5uH9sHy5CSaWFtPrqcnWT2jX97jitosaviLRPUGF9uElAOsrCVUy32z9RdcZC4YjWP9Pn_6svkOk3i_eD2veC7a2ZSmfAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg0gKKoIl9Nz_kG6o9P3Lsm_iMu47CnidNDJZa1ppInrY8m5rfEA7RRUAD94YqbClV9Ggh6OryO4Tf46vylxiXpWCKoqBwkrMQ6hwKD2Tn15flXO32-upcREpLufNTZHyRoN2F2bIPirYfmT5YasO4GpodRIpwdJmKFYEJ06sxwHkzQVZFOZvZHL0sMFf6pQuKRHOAXY8rgXdSKuiU4DXgJ3XMaOwk27ldBpm4Y8GjtvnIWLxtfjHOzUgCef2DUX_AoLT9DetXIkWyQ57KsslnP--gzA2m5n5Gw89_huTQxa4DvqdvHNHG0UHQzGdrK8OkWnYl6JTVGqPcOGXwbQPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=u2uKpITYiKF8ohUwycWytDr4G9Jl0brza74ku1-j5U4FV7Ks68wnd8Bb1VSSuoxXXt9QeTtxB288UjNRGTLhCvMWY0CSVU9bta0uwmrP-qR9U3l-vfDso3rCla9hvQCToJQ3WgJauBTAYtcvpQh-A7s2rZ_c5_SRquCWJWgZV0wY6BYCAP6DtYmgpa7Zrpck2n5tEvf1AJTomU7S-Zg0zZhHfwovgNygVgcM6Rcid8UNh_gcmcPnhVCo6leloo1_gnbaHCi0N8nQRBhJw7TClXmfKWs3RXnAlE0gLey3TTd1UlpMZ9qvPBxe2we-YcoC8_tcZ_FRrD3YS-hKCy-NqIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=u2uKpITYiKF8ohUwycWytDr4G9Jl0brza74ku1-j5U4FV7Ks68wnd8Bb1VSSuoxXXt9QeTtxB288UjNRGTLhCvMWY0CSVU9bta0uwmrP-qR9U3l-vfDso3rCla9hvQCToJQ3WgJauBTAYtcvpQh-A7s2rZ_c5_SRquCWJWgZV0wY6BYCAP6DtYmgpa7Zrpck2n5tEvf1AJTomU7S-Zg0zZhHfwovgNygVgcM6Rcid8UNh_gcmcPnhVCo6leloo1_gnbaHCi0N8nQRBhJw7TClXmfKWs3RXnAlE0gLey3TTd1UlpMZ9qvPBxe2we-YcoC8_tcZ_FRrD3YS-hKCy-NqIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=nJjWadou-hrCHobEcpzACtBfMSQsuPxPqIB87VelirxHG9dKihJIUyRCGzbAlg-FgDe8HAr8eRIWXOecrpmSKlK6eC2lc-ZEGJQtUiBBWHb_BI2dhbSRwp5OVcCfUHCWlD5MUno__Fg49iPnRAOTDd-rMe5E3VjcpMdPB0pwKELFIrezr0wzyDYAVEwV8ADwrD1yF3b4lvG66_hb6yuocLATp5aV-fNhCVLYAuT75ZtRMX0PXFSS6H9rfk9Er9Zv8pVWdEBg5ibnlGx4upLTe2zKruCsm1rSXSmCb1klHlJunln-clvfZKBqug-hPHHKQvKQhU0a_KVyAfOCgLHEuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=nJjWadou-hrCHobEcpzACtBfMSQsuPxPqIB87VelirxHG9dKihJIUyRCGzbAlg-FgDe8HAr8eRIWXOecrpmSKlK6eC2lc-ZEGJQtUiBBWHb_BI2dhbSRwp5OVcCfUHCWlD5MUno__Fg49iPnRAOTDd-rMe5E3VjcpMdPB0pwKELFIrezr0wzyDYAVEwV8ADwrD1yF3b4lvG66_hb6yuocLATp5aV-fNhCVLYAuT75ZtRMX0PXFSS6H9rfk9Er9Zv8pVWdEBg5ibnlGx4upLTe2zKruCsm1rSXSmCb1klHlJunln-clvfZKBqug-hPHHKQvKQhU0a_KVyAfOCgLHEuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=iQqW8pQtalTmy1mqRNqeTmRKYM8BP_Q3xGF-MtEjGAfr_IrK_844AbUWM5qPiUef4ApJz6ifyI8nm9XvuRxsU0X3ZaPEQW-EKX0N9-16KvkQignvMxXvPeHLtf-oR_L6XCflbbce9N-r-5_pIvrZo84flwHyqSY1q0ALN3DKMFKN9-a9j4SnvgXq8-nQNevU0gLotjqeElzL5g95c5umH1UFgOPuKTfU19ne9e-OmaDsdEB5c1LMsI5DrWz47YnJzl3rLwoBfR4MOlTS-wiDYfX_KGULFtl1VeOtH2duUZ0QPdZ3AX2ZC3YYs8Uas2oI8z7Y5qLW7IWvZaIcNk6PBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=iQqW8pQtalTmy1mqRNqeTmRKYM8BP_Q3xGF-MtEjGAfr_IrK_844AbUWM5qPiUef4ApJz6ifyI8nm9XvuRxsU0X3ZaPEQW-EKX0N9-16KvkQignvMxXvPeHLtf-oR_L6XCflbbce9N-r-5_pIvrZo84flwHyqSY1q0ALN3DKMFKN9-a9j4SnvgXq8-nQNevU0gLotjqeElzL5g95c5umH1UFgOPuKTfU19ne9e-OmaDsdEB5c1LMsI5DrWz47YnJzl3rLwoBfR4MOlTS-wiDYfX_KGULFtl1VeOtH2duUZ0QPdZ3AX2ZC3YYs8Uas2oI8z7Y5qLW7IWvZaIcNk6PBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=WNkPZLZPPC9UBMv3gQVGrA1q1bZMYBMS9_FHTQP9h4P4eXFOSwwaLUm4Xuu0oiOkWeEtZ09fJyHenHr3rTdFfZ0cMWX4QgGw6C5eDNgv8LwFRzZSF1YPU9WclnV-ORoSWBIOPqkUp72l9TxVzPJEkDOW_eJn1nqUE4Ql5hXm1fL8TV40QxY17RhEKAp5gHdocNJ77utjCGGZQ_fJp_pbAcRdb0nSV2pt39rG20-_Zzp1RJX-hMg3nJM86CmNaGYQRVfizmWlEURuGS6Rh2Dhq-csou7qWkFNk8e8JdtysA9tXD2RBiPUmgUE2ADHHJtJcHmelKs63kLkD97_5P3i4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=WNkPZLZPPC9UBMv3gQVGrA1q1bZMYBMS9_FHTQP9h4P4eXFOSwwaLUm4Xuu0oiOkWeEtZ09fJyHenHr3rTdFfZ0cMWX4QgGw6C5eDNgv8LwFRzZSF1YPU9WclnV-ORoSWBIOPqkUp72l9TxVzPJEkDOW_eJn1nqUE4Ql5hXm1fL8TV40QxY17RhEKAp5gHdocNJ77utjCGGZQ_fJp_pbAcRdb0nSV2pt39rG20-_Zzp1RJX-hMg3nJM86CmNaGYQRVfizmWlEURuGS6Rh2Dhq-csou7qWkFNk8e8JdtysA9tXD2RBiPUmgUE2ADHHJtJcHmelKs63kLkD97_5P3i4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_9wihyWupG-NshFUs8N_Z7OGp2KtBQVQGmT4OVutaBct5QeCzJkbyTP09ywEzdi9pMSHmrgrHdGIiJHAADmg8i4H3gJKW06tbBcHYAcwDrO3YIcA-Ca9vhvaEet5iZh7RaqmHiVaUKpibltNgQ16cmRAiaCwjJYdvO_HEW4aQCkgKZY4UpdvX6TzLKz2XYMlS7sYF7pq6vG8m6NzaEpoFG5oXEyvNJGTDKxrXl8gJdM9jqHGT40jiib-w6JHRIee06KNwx2spO4kdWvFyhBbfZn6lhrwGleU_56Sz8Y2nwl7r__IbyLWQRkvHuOq53ng5blvq29b5PkD-VSXTA56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=fLXE1XljAfcX8DuMvh8IgbHTLDU-7udXd8LEcq1sgF1pwb5V7nVzL9uFgYOtHlfxUR6xXNvmnNtpWDH99Fi1aDGkmgdQeGT6JE7ceFG9MiqEZPBnaL2S7qY7FYcZ0saudTdjZPOokD1VBYMhGeQvtPlcXdQTz13uq_g4Xoin-XyIrQi9yjlXDanGCmpG9nudo8Kd2IgyrnclBSsidekAbj_FJxQn_vRWYNt7XhC3CCLT_bVpsjcT12_kKaGLcn9QO5FWrzABj7Jq1D7ruQJCg10TljDn3XJTV6KYknu3u5crTL9Aq36k3P4r6T-DHn3tysMciVWIkmvEEfF3OSwQilUtvxPdA6dpLY2QwhPplTLNZja3ekWcfwaujP0RpD2Z-G9QEwd1oadrJ-S7zK7XtX-8as02AiDLiyEvnghi7bP530VHemzymUtYn5nkj4GKC_ezd5Ow6lVJaIXvoEYheg_KZDP6odWs4_yFw9in3KbVzzHjJDmp15nfOhMryDND8GmPh08ieQFnRhD21E8I6hoO6HiEH9tF7SQH9VqBMa9JCEWimqqAv7hEXyRTkHV1Yzu9xD9Q-CFaR0o1Kl5WkNeHWYePGmR4uyeatNSajhNNrT3Cz4xo2ntBxei3XqaSJhmkWuVlL5ds5WAxwrxLv_Hc0_63pCIAp6i8Ib2AnEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=fLXE1XljAfcX8DuMvh8IgbHTLDU-7udXd8LEcq1sgF1pwb5V7nVzL9uFgYOtHlfxUR6xXNvmnNtpWDH99Fi1aDGkmgdQeGT6JE7ceFG9MiqEZPBnaL2S7qY7FYcZ0saudTdjZPOokD1VBYMhGeQvtPlcXdQTz13uq_g4Xoin-XyIrQi9yjlXDanGCmpG9nudo8Kd2IgyrnclBSsidekAbj_FJxQn_vRWYNt7XhC3CCLT_bVpsjcT12_kKaGLcn9QO5FWrzABj7Jq1D7ruQJCg10TljDn3XJTV6KYknu3u5crTL9Aq36k3P4r6T-DHn3tysMciVWIkmvEEfF3OSwQilUtvxPdA6dpLY2QwhPplTLNZja3ekWcfwaujP0RpD2Z-G9QEwd1oadrJ-S7zK7XtX-8as02AiDLiyEvnghi7bP530VHemzymUtYn5nkj4GKC_ezd5Ow6lVJaIXvoEYheg_KZDP6odWs4_yFw9in3KbVzzHjJDmp15nfOhMryDND8GmPh08ieQFnRhD21E8I6hoO6HiEH9tF7SQH9VqBMa9JCEWimqqAv7hEXyRTkHV1Yzu9xD9Q-CFaR0o1Kl5WkNeHWYePGmR4uyeatNSajhNNrT3Cz4xo2ntBxei3XqaSJhmkWuVlL5ds5WAxwrxLv_Hc0_63pCIAp6i8Ib2AnEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=OrImefNCb4J9l_ksI4_QJQnuga1HoY8Nuq93dh--nwOssXrP3nuulIY3ACr7mqYhSunxHU-0tfxqT3U42GfsYGORnBeKLUZa3O57mYqRuOSbwHCi2K1KouuPmT4q1pmWvyg-GCHT_XaRKi9_uBF0GCegpwz6ZkOdmEo4_A5l3BchIWSiq2-KBmGnF0i0sGza4DzJRh2zK9RXt6pjv3YUfmSI3aKlf0_L-_fT_CEg-y4rUsENKAFdgQfksWnVjkYnMxWXnpXLULCvYAvjl4ujBwu284sCzJ9PLp5XyqD8ARfr_pChX5d5ofKFFjwfDav400051YvgIAIeiF4D4nPDYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=OrImefNCb4J9l_ksI4_QJQnuga1HoY8Nuq93dh--nwOssXrP3nuulIY3ACr7mqYhSunxHU-0tfxqT3U42GfsYGORnBeKLUZa3O57mYqRuOSbwHCi2K1KouuPmT4q1pmWvyg-GCHT_XaRKi9_uBF0GCegpwz6ZkOdmEo4_A5l3BchIWSiq2-KBmGnF0i0sGza4DzJRh2zK9RXt6pjv3YUfmSI3aKlf0_L-_fT_CEg-y4rUsENKAFdgQfksWnVjkYnMxWXnpXLULCvYAvjl4ujBwu284sCzJ9PLp5XyqD8ARfr_pChX5d5ofKFFjwfDav400051YvgIAIeiF4D4nPDYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMybGnhJ8MudcslEbrvEMG4ykSnts8fi-m1i5ZiF3srKWXbSfc8N-tpnAOlytr7fOnO8-xqRDyO7wrT3WEd3ayNi-N7R5znoFZj9HmfD9_AOOKYZ4bH0O2T334fIzqCjURW09dhUlKD_KrQ5U6k5WpCZFofqhke2l-QhRYBh1RX6I7wXm675fYIPMCsAeUs77dpIuLRGUv8mp6w1OPWT0zPP7uGxWEQEFeNfyjR4odRRDFEkleYS5-fgu7fs3efiUNOTzLpOowLrZBq9DLS2w-8WFJJaPWsUBpzKnDxWSjb7a1KPa7V--i1PdLbiXYWdMh77kKdErwZg0SVUMQ38yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=BffTmauAj7mED832zXmcGY-3H814HvPvy7bJmiQe1M-0H5v6wgGWlOgcFg2opvORI-34QH8KTNUTNmhHQW45-Ox3nk5x9k-42M58K7ziV_4SZkc4bg-7Er-UE9XPgKDTnmxbz0KoGw9odSZ2UFa3qDca4_SjFjsiUBu-Ez8-s-uaF_fMN9jDMLJKpjELu3cLWns7Q9FHitFvEyaj_toxL5CGFmRVuTHPVvIs8SRaJx3BEbmguxzTIqtz8uEFWBF7iajT9I1nuyzJY1B8GK6V_fg483wFBs7d0YjQM8hIoYyyfrtveYCsOAo14dDe6JIAFCP4e3tUT_zQg_gfqo3peA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=BffTmauAj7mED832zXmcGY-3H814HvPvy7bJmiQe1M-0H5v6wgGWlOgcFg2opvORI-34QH8KTNUTNmhHQW45-Ox3nk5x9k-42M58K7ziV_4SZkc4bg-7Er-UE9XPgKDTnmxbz0KoGw9odSZ2UFa3qDca4_SjFjsiUBu-Ez8-s-uaF_fMN9jDMLJKpjELu3cLWns7Q9FHitFvEyaj_toxL5CGFmRVuTHPVvIs8SRaJx3BEbmguxzTIqtz8uEFWBF7iajT9I1nuyzJY1B8GK6V_fg483wFBs7d0YjQM8hIoYyyfrtveYCsOAo14dDe6JIAFCP4e3tUT_zQg_gfqo3peA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=m1wOQG9i-iaK79iwn3wljwCp_KG0WBbPJHXmGHcT_2hSBuxWARziA2HIoBjBzxqD29GbLLTpwGVuXHvZBItBg0LdgvGSoed_FsEguFOMQ7KGMLk12jHktURUApLv91ipXi6Yw-Vs74f-7SFqQi57is-O73ZzA8SoUrNcazaBPksrCLPS30ZOufnV6_O0oeXLTtMMGCoCrk4An1FUOjhvy47XrHsG__2OKgbbuswsyBoSe8ey0cOyuuVow1oAtCSksLWE-7xrOpo6tDB-XEokv6wy90GsLQIUoquqWsoS7mXyRztKA90dEgRwvAG_wkmSvi_8M-_0Amka0L4dfRYYsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=m1wOQG9i-iaK79iwn3wljwCp_KG0WBbPJHXmGHcT_2hSBuxWARziA2HIoBjBzxqD29GbLLTpwGVuXHvZBItBg0LdgvGSoed_FsEguFOMQ7KGMLk12jHktURUApLv91ipXi6Yw-Vs74f-7SFqQi57is-O73ZzA8SoUrNcazaBPksrCLPS30ZOufnV6_O0oeXLTtMMGCoCrk4An1FUOjhvy47XrHsG__2OKgbbuswsyBoSe8ey0cOyuuVow1oAtCSksLWE-7xrOpo6tDB-XEokv6wy90GsLQIUoquqWsoS7mXyRztKA90dEgRwvAG_wkmSvi_8M-_0Amka0L4dfRYYsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNHjV9MlfnI4OK9LkJ5_5YJNeL4I8pGs7THvLA1scauSjKXuY6g5FRMcTvbLdHOnpwMQnWgoLt2rVPhfCsaPBUgjVfMqgzFIFKPFxA3IVdOqyHNiW9cG40zZtpwxJz3iTkCjRbPB--Q0dI2ZpEK5tmKVzU0uCJoKvnbRLgLuRiraPuVXR_QqThg135uMnJ0e5HrybM84AtSbDzAk6OrUOQ4Oz9l1F6E9JgU2rg3mLYUA4dEkAiDbXLgnv3hWaRj8b2AxIPR8k9LSqxpchf2wyB1kiUxxWKDtmEUbfWuPwuK1qrersKMS3orH3vri_XZ_TSbQLHwI39zp7YS4bQGxLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=S0-vpCwQR0FOHAisKZWqHZ_H8G4SOJ2c9c6kBvd5tkX_kwVuDF1TAGNrXLjd8HD8oKG2yf313LPyk3N-VOO-wJDVFvcPnfSfUoAVQqFJ2qAUj73Zj3OUNt6oZoi3mYJq1Voj0UGpTRgLU_rKBK9RIEX8rLJODkzEbIOMH3NujMZrgbk1JEAUWJiTDm4Y6AvvhRWdIfu1AI5139rdY5dibiQOQ6yFtrTBFGSf8a3POjWcsY5Nf6QxAow3yDeyHJSm-_0i46LJgTRjxkZD33yuGjHz7Diu9AIiWarljauaAhSnxDx1OaHkMvt-vjEg_dzCn4l_9CZjnFbCGvzTaAq4rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=S0-vpCwQR0FOHAisKZWqHZ_H8G4SOJ2c9c6kBvd5tkX_kwVuDF1TAGNrXLjd8HD8oKG2yf313LPyk3N-VOO-wJDVFvcPnfSfUoAVQqFJ2qAUj73Zj3OUNt6oZoi3mYJq1Voj0UGpTRgLU_rKBK9RIEX8rLJODkzEbIOMH3NujMZrgbk1JEAUWJiTDm4Y6AvvhRWdIfu1AI5139rdY5dibiQOQ6yFtrTBFGSf8a3POjWcsY5Nf6QxAow3yDeyHJSm-_0i46LJgTRjxkZD33yuGjHz7Diu9AIiWarljauaAhSnxDx1OaHkMvt-vjEg_dzCn4l_9CZjnFbCGvzTaAq4rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wppb-RqO2A7_2o7Sjk6kEAMLxbU2wTBHnrNmEQMvxdbiGtioOWWDDKv8GzZ0NnmLHpfF7Q8FF87eMi1YqjGCfZIaG9GsEUwhMv3yI66R57Ywy9pcScJW6D9yvWsblzNMkOW7BKLDAwgCay9sS8F1Z1q-uEVm1HszfaPywf_-qGJXWB9FH_wY7vAMxlGuvFbzfbgiZa7UU69PDNSo0FrCwKDPWaGZyRWwdbrU8Ts45tVveQzREosyYA2uNNK1NWSGBkiAXL6bI9TBaZwSHGf-rSn8Z1wnB-23o5xgSf7IsCoP_tq5dKXl1rAAcRwq0R1G_nnBCC3LHJjJfz5AxSbyPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=IRm8lgCmiZFYc6KSJ9LxrXKco61-zmtDqpl9joRyGW35AXfSdDGwbtapkOe1kAOKfdtuLoBImYYWN03xz1YAyDvRWXy8xu-egfi-yekjaGPJifum6fJb8YkBAmhxMuxzVTGkvVksU87igZpPlWltnPmu6vfvqkfZebECIBFZuRf0TbgtTQRwHU45bBr6-NxLT0rjX1FNnBqOq2LK560DiFT3bWfNzxs57lf7Z-lU2p1ExyeMnZOiobNj0f6zWOwVxerLXt60GIQJfxYReBHsSKXMufguBJlThltyp4zeI7bdO6C5q_KGdkrT53rmxqXt_ICRf3vK-XxAWqle2wB7jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=IRm8lgCmiZFYc6KSJ9LxrXKco61-zmtDqpl9joRyGW35AXfSdDGwbtapkOe1kAOKfdtuLoBImYYWN03xz1YAyDvRWXy8xu-egfi-yekjaGPJifum6fJb8YkBAmhxMuxzVTGkvVksU87igZpPlWltnPmu6vfvqkfZebECIBFZuRf0TbgtTQRwHU45bBr6-NxLT0rjX1FNnBqOq2LK560DiFT3bWfNzxs57lf7Z-lU2p1ExyeMnZOiobNj0f6zWOwVxerLXt60GIQJfxYReBHsSKXMufguBJlThltyp4zeI7bdO6C5q_KGdkrT53rmxqXt_ICRf3vK-XxAWqle2wB7jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfnaqyyKbwWBTujlY0ZuyZmWeWcuusGuHG6FqjxJi5N71FNTu8plSS9Fs1xbOV5OxoimlbBVxak06i0ogJgxT230Q10YmHY6DpqrLPmqzAG722gwshbi-Y7YYHi39iALw1NcQUfh9dMSkhmQwqVl5JtkJ1y_bDDlFfkngku1EaSGzrTLgFmGqQoZb3fduPJ06rx0owLOthEEnLTKCk0vX72eXKwo66jn513TjQBOjgsE31HilZsN--ohPDRhsgvuBW9Agl1AtTTF_E6JwiZ6XQCPQwG1srTMB4dnojmLrC34dcJ-GjxRHpINIyemPV5wfo-TRzhKxUmEwdNge46Ssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=naJyGfXBY-dgr5puEQRyPMAd_4wI6aqg_EySJ9PnqPQksdy659MU7RmeersNeFB3sV2XQYPLo11QnKzISiURnWhnEg1UFwClMH48vWsFLWu3HvJU4KEa1FhNIJSZeQiLVIZ1gEb94uAhugq3g87mJU9XQXyvmGlvmF0tAxbc54aT2kTRh9gyhS5eGMkjdN4_oyK9fEj-8DL1OoNOsQ_ODGbWC6WnL_CZS8MV5PM0f-31slS8sqoq9RyR8wu3IGJw-KSu1rzdTfsZzbR5FhhaQzdtq0t4ZWilA1lD3OdYQIBQyjiWHCr5hnupUpxKNSD7Fd7Ynp7d8TK4W2t9qcjhHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=naJyGfXBY-dgr5puEQRyPMAd_4wI6aqg_EySJ9PnqPQksdy659MU7RmeersNeFB3sV2XQYPLo11QnKzISiURnWhnEg1UFwClMH48vWsFLWu3HvJU4KEa1FhNIJSZeQiLVIZ1gEb94uAhugq3g87mJU9XQXyvmGlvmF0tAxbc54aT2kTRh9gyhS5eGMkjdN4_oyK9fEj-8DL1OoNOsQ_ODGbWC6WnL_CZS8MV5PM0f-31slS8sqoq9RyR8wu3IGJw-KSu1rzdTfsZzbR5FhhaQzdtq0t4ZWilA1lD3OdYQIBQyjiWHCr5hnupUpxKNSD7Fd7Ynp7d8TK4W2t9qcjhHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqnHgA3-nl87dEzbosiJmLHrfQaTAX2fQtkt2MEVtdhQSeLZ3FqJWHQFJymBlKVxT6WdMwHueUA-V48jQQKBGtKtq_bUPQTXD2GzNnDEjnGNLLkKwmcjj69DWkJ6FtPC-5HLWvJbSTG1V3cAb-xnOU62Qxyw8cBwNIXzMYvYEnAhzl4aqhojTRdTc3_rcY9aZOoYq38za_3u2Mce3jDe_Jd1mCnGnYpoalQDT9BoM7_al8FLnxGhLL7xnTw4VsCnJ8kkzElD42_MwezkSlmqQOSl4h6l5prfLnJ0QtA_Uew1MAGVm7QIh-OUf2b-VkPQlH9dhZS3W5Q0OR5501DW20B8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqnHgA3-nl87dEzbosiJmLHrfQaTAX2fQtkt2MEVtdhQSeLZ3FqJWHQFJymBlKVxT6WdMwHueUA-V48jQQKBGtKtq_bUPQTXD2GzNnDEjnGNLLkKwmcjj69DWkJ6FtPC-5HLWvJbSTG1V3cAb-xnOU62Qxyw8cBwNIXzMYvYEnAhzl4aqhojTRdTc3_rcY9aZOoYq38za_3u2Mce3jDe_Jd1mCnGnYpoalQDT9BoM7_al8FLnxGhLL7xnTw4VsCnJ8kkzElD42_MwezkSlmqQOSl4h6l5prfLnJ0QtA_Uew1MAGVm7QIh-OUf2b-VkPQlH9dhZS3W5Q0OR5501DW20B8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJU9U1Lllh0-7LK4O-q_NQoiFX_WDtVRk7NU1uZ5ZVcHDK-94EkZ9akB3wTbxkkd3nQz7VoKdtAZIiOntzTgYWQ32ZRfGbAQOH-dkVY2X3rGJMuuIlZGpwtS_J4QoJeVbTvr_FOccb0ASOR9YI3GEpwyKnyOtp-MUahyq4o0ruaD5aEWci3m4tIGkZy6Er5vzzUCu666JCo08hJHdrzHTpQPVsEKc2poHnDUvRORGyI2dOq7ink1PLrU81d4phbrTKH9fCamA5sJBp5oYG-xPa3OAwDiEfaa0GMqFqcMb2tAxPlD2ySjw2iGTpg01XpaEH7L8p7MFhl50pcBIFiHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=eUBWvopGKhJEdjIPCt_7nWFGWaVC7572EJcwACMPQhBEXBE_4Rhu-f42-cQJDaTlqCexLNPSlW_kLzcm2s6GwwK4WAxpicHxkkM4DIBglCrSJjg3nDE4eQLhwZiP1VmR7SWrY3oFJDWU44fAVDluDrSIzP8YEenrqAEeam9bka-NIx_DAFt6ck1sjWhRvuDO-aSk17nTk183aCI8okBj3Uc0uEOImz0vxFfXKs3OLyQEQ-kevZQVyZiLngLakFGBedzpTzxtPl2zwTBWVz64V-2a4Y5Ebpe1cKgnOdG-xlnXsn0b86pqHrkwsanO1aBGe2VZQIAGH67beYyKWRBm4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=eUBWvopGKhJEdjIPCt_7nWFGWaVC7572EJcwACMPQhBEXBE_4Rhu-f42-cQJDaTlqCexLNPSlW_kLzcm2s6GwwK4WAxpicHxkkM4DIBglCrSJjg3nDE4eQLhwZiP1VmR7SWrY3oFJDWU44fAVDluDrSIzP8YEenrqAEeam9bka-NIx_DAFt6ck1sjWhRvuDO-aSk17nTk183aCI8okBj3Uc0uEOImz0vxFfXKs3OLyQEQ-kevZQVyZiLngLakFGBedzpTzxtPl2zwTBWVz64V-2a4Y5Ebpe1cKgnOdG-xlnXsn0b86pqHrkwsanO1aBGe2VZQIAGH67beYyKWRBm4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=aJcQRLQdptKPCOG8V--ZWSIERnEvwvqoDNnUGz8UucpTgb44ZUt7VPp9iqhW4ajbLanLHX8AMxRaVIsHicpfWkvOBF-ORt8AdZ2B3diOOH3mYbkCi8N8bPhhqyO2KeZ3Ten25R8AQ_siqQxn81RwRIfA6EvP3gqVNCLlq4tVqSpVNpHWJTJ9d-GHFSkZZGZ0VJdLo8dkRQ1BVuzAJt8ddfhsIxV6WFJVbJGhUVv_jgRr700p5wvwwlb9SwmBI0jss53sxr0y0zSJoQKAVmoLLklzcsKNgBQwTS1bY_T4VjfJxhJ1gMVAqYB0-MHq7r-mwQNasdOaSGWvYJq1BaYtlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=aJcQRLQdptKPCOG8V--ZWSIERnEvwvqoDNnUGz8UucpTgb44ZUt7VPp9iqhW4ajbLanLHX8AMxRaVIsHicpfWkvOBF-ORt8AdZ2B3diOOH3mYbkCi8N8bPhhqyO2KeZ3Ten25R8AQ_siqQxn81RwRIfA6EvP3gqVNCLlq4tVqSpVNpHWJTJ9d-GHFSkZZGZ0VJdLo8dkRQ1BVuzAJt8ddfhsIxV6WFJVbJGhUVv_jgRr700p5wvwwlb9SwmBI0jss53sxr0y0zSJoQKAVmoLLklzcsKNgBQwTS1bY_T4VjfJxhJ1gMVAqYB0-MHq7r-mwQNasdOaSGWvYJq1BaYtlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRR2Ovy1mK0J12_-HQrj1wpEUQCDU2dRGG5nmlnbArDrZUmMol3cFquFwcqksA09Ftp2u9kh5AHR1obPnyCaUuLiyIYmB4KRFmHRjmSJuE0NyX6r11fkcb64SsSz92WKmCJ97zBEO7KDNNY3hEXbcfuXb63Z292k_X49WLH_XdsgwMqFsaY9OMl5kxeNg8BO6-emDZstJElMA_-D6xATa3brqW4fBtKemohpWwy0qMqxYH5TPkhbRAEbSxV-VFijSWFRd4ycNCV-S-pnMAXF-eKsXkP05uhc0_XJwDJ9nsXdAO90iXJSvywlJwFLwXnjw4vNDUFN-Wubrr80YlyHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=WxN7m-fB4gmZKdonB99Sup8nxH4ZISWS6zP1sTm0McC6W3SK1rbJYi9tIxG9I9FOEG82EtYlhux2J-gbYWrCT0dT8_chSC6ws7eeF8k4JsNW8RqNdnLXvN_9_IKDFRSTGHR0YeLHKCHgdxHWVFpJ_aT121xyGRmkqtWRD5hWrvm8wt2Hu4i7b9-uSrDTpgVI7srt4flBViLVQD3eY2uVR_nMLNjd5KG0Dcxw48fXy2MmyY_mQ4Ny38ukQnfno9Oq5qfbY-sLHeui_fn0D0kQh8oxbkZI5cSmb5y3Zm6ETrjVdGeMeFvN0yMn6W7h8j0X9Rl7Qb2kubNsypAY7vkBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=WxN7m-fB4gmZKdonB99Sup8nxH4ZISWS6zP1sTm0McC6W3SK1rbJYi9tIxG9I9FOEG82EtYlhux2J-gbYWrCT0dT8_chSC6ws7eeF8k4JsNW8RqNdnLXvN_9_IKDFRSTGHR0YeLHKCHgdxHWVFpJ_aT121xyGRmkqtWRD5hWrvm8wt2Hu4i7b9-uSrDTpgVI7srt4flBViLVQD3eY2uVR_nMLNjd5KG0Dcxw48fXy2MmyY_mQ4Ny38ukQnfno9Oq5qfbY-sLHeui_fn0D0kQh8oxbkZI5cSmb5y3Zm6ETrjVdGeMeFvN0yMn6W7h8j0X9Rl7Qb2kubNsypAY7vkBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=lQbJNOx4jYE2yNrnzG_WSHCOZY9uppvTpRHfYhnBV78mTEgToR1MItJ5_8ZarESLzi07dL9b5f2bw50y38ECDkbM-YTm5Mb5lAQMBk5Y5NpEF8DGZYKPB7L-GSiffkTA0WAY4P0iPR2pY8rcFw8BawLmWQOiGWSCQNw4drOxpXTmEcHqcIGdUG5mWpHozPrzl0XImvzHRA5QwkT3VhMnlBQsCUowwbSy7yaYNF4lVs_q-5hLYmV5WbR_QN3Gyqc6ZIf5Gwav_dFcBKicAUSTCW2egafXhdYIr6NRDAWy1cFZvZVkECgs3aeNFfzWJZpnjlWegiDYN8M1PUtKW_fjpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=lQbJNOx4jYE2yNrnzG_WSHCOZY9uppvTpRHfYhnBV78mTEgToR1MItJ5_8ZarESLzi07dL9b5f2bw50y38ECDkbM-YTm5Mb5lAQMBk5Y5NpEF8DGZYKPB7L-GSiffkTA0WAY4P0iPR2pY8rcFw8BawLmWQOiGWSCQNw4drOxpXTmEcHqcIGdUG5mWpHozPrzl0XImvzHRA5QwkT3VhMnlBQsCUowwbSy7yaYNF4lVs_q-5hLYmV5WbR_QN3Gyqc6ZIf5Gwav_dFcBKicAUSTCW2egafXhdYIr6NRDAWy1cFZvZVkECgs3aeNFfzWJZpnjlWegiDYN8M1PUtKW_fjpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=NslW_iul5EsNVsbsR8AAX4fcBa5agsNPMmJm27Ec3UqsYI95IKph_Hwj4Few0tGr5tk-49FpXHGrtcLElVoD-fz7HhZ937igfjHlouNNaLhOHQZTcUrTa5xscVTwOwwdj2vz3qfa3qiDSkeywDBpaqTZqyPjwlAQlQfEhEYX8CAhdxPcssPHV_lRFcWusgW1aLjBkMvvdDArfL-_jiHeoPmHkY_4YTW7vG4lhv3O6_E3oKe3GXRKKCZpnWKIM8M1OnwIs4j06PYzMp58zDK1QFQ94rhy_ox077LJ-hImiB_rBfJfYVOgU4_6_2oO-hWO6lz90Uewla7WLYymiakW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=NslW_iul5EsNVsbsR8AAX4fcBa5agsNPMmJm27Ec3UqsYI95IKph_Hwj4Few0tGr5tk-49FpXHGrtcLElVoD-fz7HhZ937igfjHlouNNaLhOHQZTcUrTa5xscVTwOwwdj2vz3qfa3qiDSkeywDBpaqTZqyPjwlAQlQfEhEYX8CAhdxPcssPHV_lRFcWusgW1aLjBkMvvdDArfL-_jiHeoPmHkY_4YTW7vG4lhv3O6_E3oKe3GXRKKCZpnWKIM8M1OnwIs4j06PYzMp58zDK1QFQ94rhy_ox077LJ-hImiB_rBfJfYVOgU4_6_2oO-hWO6lz90Uewla7WLYymiakW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=NbE-G49cZAihrbVRuBuo8rIVvXNq9o2Ul1RFvhoUmEeVWAz2uEQ_I-1cV9KT8yxTSWeDJjImdetb_O-RyNUhT2LjfAWmSBTKziKqWTt1ytQGb1v-ly19VIf0BEr0mpo1w18I0QY85Sik8T3N14q0VDxPng3PbIJJEGVBXlVurEo3uBkvYwrltTGQa09o5LToFmcq9Sl7sj4Qybp94kqLPw-L9bBgCOCtdAqzS-bgZFWJe2P_hzvBC0tjZU40eFpFCKfdsap7aywv1K8XeTocrVIf7LWmTvlXuxjxQxSId9I5QJ7Va6tiMeaaKDA05zCaq9SUeekqGYyCUCuCxPg7hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=NbE-G49cZAihrbVRuBuo8rIVvXNq9o2Ul1RFvhoUmEeVWAz2uEQ_I-1cV9KT8yxTSWeDJjImdetb_O-RyNUhT2LjfAWmSBTKziKqWTt1ytQGb1v-ly19VIf0BEr0mpo1w18I0QY85Sik8T3N14q0VDxPng3PbIJJEGVBXlVurEo3uBkvYwrltTGQa09o5LToFmcq9Sl7sj4Qybp94kqLPw-L9bBgCOCtdAqzS-bgZFWJe2P_hzvBC0tjZU40eFpFCKfdsap7aywv1K8XeTocrVIf7LWmTvlXuxjxQxSId9I5QJ7Va6tiMeaaKDA05zCaq9SUeekqGYyCUCuCxPg7hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=AWMa92a4RUKtQDX43SCoZvxgCiIzkGBj3Vco_8fUoLyj9aCaD-4HEQRxEbAkWiG3EZ2UcLZ3TNyGt-7JBJeltQRsb4HJ2cygjkBnJjMlBTnopL_swx8TooO-EWqNzbiDyzEgysx0g_WhqVK5Z_VCHcD_66r0RK2ESjroCfLmYzcdOb771lbFXhCE0kOUeNKl8rTpEQQdFqX5ANdyE6Eu8WdK2lPZZNiU8yYGLpGXdOXcBcAZ9rpC1mPnGXJ4t-inE-FmSmY-0w-XlbJZkgYqiDTaVdSOit0X9bZcoJigJhE8Hh3IPmZQvbJPyVEGBfx2YGGcwRxi2lc_KfLjnQA3RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=AWMa92a4RUKtQDX43SCoZvxgCiIzkGBj3Vco_8fUoLyj9aCaD-4HEQRxEbAkWiG3EZ2UcLZ3TNyGt-7JBJeltQRsb4HJ2cygjkBnJjMlBTnopL_swx8TooO-EWqNzbiDyzEgysx0g_WhqVK5Z_VCHcD_66r0RK2ESjroCfLmYzcdOb771lbFXhCE0kOUeNKl8rTpEQQdFqX5ANdyE6Eu8WdK2lPZZNiU8yYGLpGXdOXcBcAZ9rpC1mPnGXJ4t-inE-FmSmY-0w-XlbJZkgYqiDTaVdSOit0X9bZcoJigJhE8Hh3IPmZQvbJPyVEGBfx2YGGcwRxi2lc_KfLjnQA3RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RItFKMfgqHl8_d7orGipV_nRy2_VJPLnScOSFlrdULpT6zd2SHKwf_gnNA0IjSJ1auI6yziMxbWD7NCQcPZ625gWTnRDVHbTWOBXwXTI7xvR55qCSukVeEgBWnmIaQzMczllj7N9ufTBBJfH54j9t0BLKFesLbZIwkqIYuDnaRhdVQAh6JG3AvH0UXS8nn3j5QIRIa1aS--AyBT0etipJ3eMd91D8_Ga64kWuE1MiSG8UbSBsYBjhirTWSAyWErhzJqNKoIQLBQw_RSFu1qD0AXM7iKOq22AwKgEG0eGs-LS6ANvZ5yz9C_p8hAdmbP0cV5rXHs1i-43Jzk1KqYejQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG4pzUb5M5pnj7TCGmwX199IEW4tmQzG-aVBeMkjkj_MsqhU9U0iS_WT2nGCnrfYKuxzyUEtzteAVHVjrEqJm6Lcz-d307Jz6lyksj5YZFt7XzWx4wcBH2E9Cs3_2Qd5GqWaVQeswhJlrWal-uNf8vY1d3jF6LimDiWZ4VA8i0U7wjKxHO9LfK2qXWDgEbypg1QhFRHtvPE9Uw2IxNrQZpGki3o_DVHOKOGBGqOfbKV2vCYy7Sdnzo965okR3Y0ISBJOg5sME3SKvdyO7P5-o-Ffka__bTDy4V4NXBSAOd43oxbv3ZMKfDTi6q7haTI6iLpFN3wyNq4azeCwS2XkzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AelqMZPmYLzVJ5Wcq7JT6RtPoMOCHq7kHsyEwIGQJVZrogwW9FGTLrT5AlM8YSNa2hWKFkWR7VdBJblRFrgpfUe7UHaFYc7xFBhiQyYWSJqA62glqxXA4qwAdmtkkSv9kDyxr9jci2h0UVqHZoPra5w0J4urlFz6oPjm6_zjg7CsjDVZl--uWA72sAawl49vwid75AHfGZbtvP3z8P8vmdafMeYcmfoIoQwjR95Tk5Ed3WHy8zLOceLOWoUJan_2HGgF7Ez6lwTEIZCSdG5tDLRJSqjHNU0JAh_AinT-Qj8q8LAhdncTmGQjPySDakRyQ4hcwQ-PEnsqVqFgAIaf2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
