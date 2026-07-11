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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 00:09:02</div>
<hr>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuF20fyARGEKCUWi3BNM_a9jOooamRFNPR0rkC4bTEIwC1O5OLccf8jEJCveW_aaaL4rPV7IVqykbQBaDePx6O2w_selBi3s0LUzCY6iS_e0vYW4K_WktYSqd8NLtFs6e1xbec6GgaJdblmuW8QQ2xfT0rgUO_ptyJowHZqohokwT99DtdbKwCKV8zoOfrUWnHm3iF0UYdHDjyU5ZHhQCAhHi0128BlV7_0sc357IiUBjrCPegTkMvPrR20dVBXwYv9xP3koRWGJtR-YvcaUBvF4Hk-iFgnR8k6-zJMZFoBU9eUKsod0cC50dZYIFF-NjaZtRZ9vgjbSphd8I67RFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvig1ayycEUO61gbGKyWPQwWAgtEOIUfc7dj6Uvm8TZGIc-ut-VHA1cGNpDjTZ_GT4inGe5rvqItsMgPqX1UP67NnLkk5_eNMvIc1Tj2WmTL0M6UpW1EcThYla5kK8PAExzocn8pRk-yMknNceJY2yPjjrrW2NagUfO73k1AbIKW0Pk3HFQouvCChpGX6GplhTqiXkcXt62csvBIiRW0X99vVj9H6s4_vNsFAbUILs-CCckIuo8WZ8wCKWOhcC-is2uC283a9dJmWV47SlGkoUo_YdAj_kj987RnHWDMuXJosE0k26QNrBDvzWC9M5H3ZHyUDKn8R7ocAsJ2ynzK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHyP78d_fSmY-vAEqFik2l7ZlkGJy21Sx5I5dXjWixnIxpRpKMQdGkAI1Oq1KSAenwWGwTeB-J37Ym_eptTW1CdqlhbHYgkJxls9JRsQ6XtTkUONkJqS4JY2SPk50aB4rZOLXPUJiFVeAy3u1w6TP0mONF6NlH32w-dKUTKJRoz7VaBhNN7Z95b8cIM9PlEwtvH-zGzX4l1FtoDauqlw_SNW_Xu1nKSHmCoNkqm82SUg5FXs1X_dz-73zty4MuzmLJ-735vEf_LQIWyQ50EBzG63ad77roh1KcQEy0tAt6VCjwrdaVW1OKXmh-XXe-AltoS88ELnyqYCKtTLo7lkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFoTgLRG-08-wXkVfnmUjpyU85d5MEOPeSE2RXukUJ7gcjmFTYlZCb_kpnQL7ZIcAAM_lDv_J4qZLl0hoiuQRaoKA_6j-aoodXfesfc3KLW2-ibWZjxvxqxsCsKOE-w13vSFR6YCpn74DYo1NOBBYyEvAsrIYpZHslnt5ahw7Y8rBD5zD72zEjJb8Xbr82oFCT3fbG_O9-gKukh3C2YomWyaoxAn9HMpLntkpivRZrpZ4r0DzEYp8eqAocUxAJO47HRnA1D8xjLyMZVi-YwcsKo3Qk76hvz83eeZEW9VoL3t6eBs0cX36qSbGuiRA1OhvmzravFHMOyi9dx-QJrwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6fj-XikOE_vV6gn_Bc8O6-xIM4wgXc4YypxLCBQshzeZI2ex4bJps45gE5IffGwgyOcFmOIBXpQ5LzCUMaN_tBTveENWfWCKP8xENhazzUOnaFAp2M-41EK7Ymex4ZhS70FmJAmyGgh9BYHdlF6czYGHLcTQPXfB5Pl3iD77I8DjDXJa0sUIEh6zuEi1VR39aXBilQoalJgeV9tVniQdu1Klpw0ZHKxsgfSfFTz0JXsGf25mcyADsfQjrHKuvlh0iIPGCR6LoO9Jd48T7nKZvec_4o_-CsQq9qSzSvN6_jHrdi6Ysi5U9_kDIWzg08jSHPScvB1Yh7KR2t3-wfS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=LkcvmfrdzpxGkmgSZeK8_6hPNsH8i_pmYcMGfBVC1PLRxBf-dKrqjcXjomgvbijsofmZ2uhPeCaOjlU_Eq3dxXscDdNcQAu_2kSlHwr3ZzzZ2pnRHEC9b2hNu-orfPzBlI88XJJQoZE_ONxpes9qOa1tGGiDHi2KJjgdIr9foUbWKliFdpLZ856jnxGhqTc3pGjzVWmLfPTAZIT2XHQMHgUWw82HiXBAfjVPsrnkHk3kzalijpC8dwwBPC_wktr-ucCiClcv5E-LdUNzXw4q94AtKXJqeJCsyCQMqrXdDJa32QZn3r4Rl4KOxljEdIhl9hrmCR_Wn6f44Mt_8I27FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=LkcvmfrdzpxGkmgSZeK8_6hPNsH8i_pmYcMGfBVC1PLRxBf-dKrqjcXjomgvbijsofmZ2uhPeCaOjlU_Eq3dxXscDdNcQAu_2kSlHwr3ZzzZ2pnRHEC9b2hNu-orfPzBlI88XJJQoZE_ONxpes9qOa1tGGiDHi2KJjgdIr9foUbWKliFdpLZ856jnxGhqTc3pGjzVWmLfPTAZIT2XHQMHgUWw82HiXBAfjVPsrnkHk3kzalijpC8dwwBPC_wktr-ucCiClcv5E-LdUNzXw4q94AtKXJqeJCsyCQMqrXdDJa32QZn3r4Rl4KOxljEdIhl9hrmCR_Wn6f44Mt_8I27FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFBHiFZm8fAMSiTqrDXjhuuQLRrHCYW6o6i3gDS1k0IZRWi69pH275dYJ3vncd_qv0LaBLjeuImSWQF4jvOWcLQe_bjIy2ETCKNRCRm6IjzQN6ez-mWRx2eViQOmOkIsHhhRDmBvMb7OM2s3nYUh2jcR6kuCH7JLNzWv7LzEm2bCjc-Hh1IQSPv2vf1f0cnMpoqyCRUJFvcDgAOLeMmnjy3xSSDb4iZEopRc83z6Pm0_4Fd4N0JK7TvOgk4zHjvEnR4Cm8ZqDDYTnUsoLZ5cXuSJvAw12Zp3C_zTQd1nbIhyMPOzx_7LIU2o1Lnph5eoDgoXJZKw0-Dpfdv8lX24fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7R7eylBN0enMjg8hm88svdCf3cEvTZe1oPGwvNTTtuZ_Poo6kWwszZNxkP9YDOoQz8gl3nHRO8iqsKAjKxECVEihOSVEEl19bnMB4Or1sZgboVL2idfgCgTmftnZNtxDR07vFbQkt8ko_JW8wCybvDUROeNKNd_WfR9B3E3enI2VmZTkhxDFpK53KIiTHCrr-soAF3yepX0g3SoEEFFKXNZNABFqyw-NDmHiXUMhgzDCHNyoAYr1ybZjT846oN3TXHDDRPTNpjw1EOJFXYfBzkCjD-jFYgKZnGr6UBMWfag4de-nAyfDQeS5jUZaweFMcSa1QHNKziFtcuiJGIFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJqeGgnUgFsLYEGoF0wjtOZjP2qe_2TP2VRrv97QhG6uTnpybpsTh3HXKgsPeGpT7TMYYMsg38-9U4z4BMNk_8LXPoTRe-rzqkp1cWcai0W2sdfpYvKAMfkTMdCFATiKyAJt5aXrHdmA9pFsjm5nKy4Q_vIzFB8GsHxaHi00LyGzkC3Geehz9yYc0sTLGLNopQz1WU9wEwZiJZXrg5lgw5dqXpQ3g1BYKq-kI9ULJql5MF-pV_zMbQ4z7LPYiCCOMKsdhJGuTHi6A4eOeEL6dS7kszNlZz3O0yckf6_rQjbODb-zn6U34E5CjjgKoauQ7Vf-UpnvUbBzuv4iIry7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsTYX3DBh8sLkAXLHoWd50FP18g8zgnxGK7TdVmwy2M96aKiXVMTRP0XMMXnn0FnLn9R8epW9YUsUX3dUbVjV4JHNdqZTSutcKjrCCL5PvzU_JLdbA4gSn17cx12cIX4MjKXZUXKZfnsMYMA3_4reLGpVkRHsi3IlGxVT6wxkFTLAIkUjug36uPnXDN9xezTUfEbko9JIFbkRHCIecWJr9TIgmV5u6SADKqcP0HnD_Nyl_yvXT9pLvajcdhxkiMzbCGjwLUm1yaLpVWX952xeeLlwhpZaL38QnJMKEGnauoxC_zHP9Z5n2K3jZKibSwa4nlT9KJrWZrf8eae_13jPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SToNkh2f88FuXCRC8_iTbycUeFDynCAZGGX-xNJ_KWKxirVcQCsxoIYbDdUUXjTn1ISR5eX2bmwAzFjNWx042fPg2BKWcU-5_96PpcoO4gOidGiQ_dMS_CzL_rbxGiM_CYP4LodvFOxNf5YHoPC7T9ZGLMMJMVEHxTCKuvSWRPe2WsxMx0EO1SFOpEbTZx2fvEl1WM0HV1tRm0MsskSiOESBZaV0oMuTtxK6ud-gm1LHA_aIh_75pIAMiMD7nWrGaakatgJiv99GSwjceG73nf2FKR59fYXQKLsR-QBjqjVbrT9lWiNGO98r_GvsGiDKua-yIM0PnNF1ouRjxZ-A_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cckh-0JGHdCGOdzULPBzpQrKI60a72OEB0g2d1sGa5U5B6ak2yK4jCR0ZlssP1kWa6UaOjX34HtyNDS_bb0_SsfcKoTshpCQDCHTS4zEVcVVlJ7MuBb_uOIaNVCa1Msv7sp10wmwOCnhViZhnvTzRbfCLmYFdck4cF0poquZ9qzzvRd1YteQGKsxUOVJsWCM5eW54_jE3RtilEaxlBDJdCno47EpUC8SS1UFy1xCsmoCQZO6M3-E7n3hFJA5Imz6lOaTGsvkEdverMN70uLBq_xhLVmbkuYBWfNwVamY-TxIZX34Y70_DAyweQumZNam7sXpgaGU28piySdHn--FUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiCu8zfa9PrgIb8UIy6dxQQNRpME9OyW7i0cYhT5u-jjsDH_o36w9b8s3hFME_KFCDaYRiFRpps829sQeWQNXr_-EPx30bIbxZrPQ-X_mkiIBY4GQVVOlzB_gmnbdnwIgiOWd8czZWLaWaJT-rYVDUJ7dzb2wWBpEXGAT76TN0JM-6g8sV3FgKFOLU9liJ-9PLZT5aUvSOqCIFfbSp2KbgPRZoJXo08htb7is_PIC465qVTY2jTYtXQKwXT2yX_Lz59IIVVYSpn-8DkCyYyDkNa6f5_u3VkfZuUHhaMuTS_yf6ucgeFo6ZGjZASWZiP4Dts6MUIruYv9jkJCYTBJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-gPLBIc4dHYtop2AbwjkjCtF20zHh8H_dLpGY8XTfxJbNEqp3cf2oA6JUzg-5gFHPiQ9EkiuwTb15OuGdPyMj1dipIx10lu-FMERTnDeYPLwo5wvxCv8ahURaAO-xsGu351LoXNWJC6nEQ5uu1jxmkNxKrdEj8NrMW0_4jZ-IGICscXkXOJMbZhLXFxEktqF_oAvOtMmgOuyjynyEumoonrGP24zzll_OdViSgjo83rOdXaGFNJemsq9CIC3X48skEDDHHuGDt2YuqSuvZ8Ii441Srj8ikHkCeYIrhfNvt0um4KzSNZrEscb_6pdazwHtcak0KFTq5sg2DpIcG5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTjToPl8pIzBrct01f7vuQRnhp9NxcCMX6jHcmV_2pQWRZ6C0LfkJB96bu8CgQMYB0O4locs0Em6UjnhsZrD9aC8h58tllWTmfpmYsijIDnxhBCS-zJWZzq-VrDsHPqNC4LQO7IEQaax-43BWnm3b57zBlhcVjFsljHrcbtFZ6hNYEGoycvxe0PtAkRGrT1TwS6Yf4Z9ntTRlupo8oggi3lbWz8PzmDxGZpOOLGfG__DMacieT693c6SJXJ742lScHumo8ebJVAA1CZR-Y7efh4u3YKO6MGBRZI2OIAi5RlEhNqfu1t_aQmjV3S1zoI3mP9RF-Xv-Tyr3DvlloJrrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csfXw80GPSf4fwp_UohuVIqkPEVOfclXSA8b-035JtIWLX1RBT9Oc_0nfiQ8tQigcdUkoTro8z7gcJUzboyXeUCZv7fKyNCAN6TUlNVqKUwX8l6fcoZcE9lfDpUwa5JV73EyMog3JkTZWwvYYACzW0KYMLmhOphppzfk75OXMHy54ck784SRBvhKJr3EvKmB2i_7IvFTcZJf2PJiRHDfNU9_iXayUfI6J-FFIw-0hFjHX6Ni_Bd_X7VDiqgbaglt1FcGSJaMszT7xNeCb8_5oVkH33LspCKTFQwUFfAxTpBuFvDQOW-dAr-VfLnPKMzzcMzw-vqCAJTHJgwfzzAwtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=j-NYznpuUjEvYi829Tcb5EKzvHHp2BzeNHq8ftM9MRr2aKzOa4uE2hecSV7SHyAXjO6uqAR23QCzr5lhtrUA9cK8tzuW0N5YPdHJdOCKBz_l5CYWxDYwylIMecoRWwJ3Qip3p8PyMPdJYrDS1Ihy9JLmGvFEtwqqwm-yIZ72x1brf_rJ8_XCjuZj2ODC_N8_uHiDVIfHGDm0O5NKZinP8QQMYIBCU2kovEcZjxyYRH8u37V-E48-DuexIKbxPXiMSQRV5wFrGQ_2XhJoR0TG3pNMUgN4bITtkzAfT68w1d4DF8HXv3PQg4hAO7TfkZgEkIGLrEr1EYxONnjrIjdfhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=j-NYznpuUjEvYi829Tcb5EKzvHHp2BzeNHq8ftM9MRr2aKzOa4uE2hecSV7SHyAXjO6uqAR23QCzr5lhtrUA9cK8tzuW0N5YPdHJdOCKBz_l5CYWxDYwylIMecoRWwJ3Qip3p8PyMPdJYrDS1Ihy9JLmGvFEtwqqwm-yIZ72x1brf_rJ8_XCjuZj2ODC_N8_uHiDVIfHGDm0O5NKZinP8QQMYIBCU2kovEcZjxyYRH8u37V-E48-DuexIKbxPXiMSQRV5wFrGQ_2XhJoR0TG3pNMUgN4bITtkzAfT68w1d4DF8HXv3PQg4hAO7TfkZgEkIGLrEr1EYxONnjrIjdfhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=qI7J524z48tgyo1nRuNIQgeOOx_nBO0EAgU7JiDUJjz5gOzTTiUZSQk9rDkDgGPxfxM5i7QzqNeSFBdIHSQZ_Vn60hTpNrUKhq493npag1sys3HXA66J0KDcpt--BqpGn1RE-sEkZEx5ZhQ9UHZSmDIOboPh_aSt0ZuewiFNnYb9otIrLIgFvHmvQEMm3rBv9kMOtuZ9F-TnEL4XJ4dHmx57Om-aB_U1J-QFwCqM1gjO8vIGVBD3M-cDEss1xevPucX1MPXzvMFF6oiR2oSCJbdX_2qtqVAE5zDwJkcaEdN9Z77ACrtq3WazoVpjyoYYBZwpZLfj82WOlqxKbLMcG4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=qI7J524z48tgyo1nRuNIQgeOOx_nBO0EAgU7JiDUJjz5gOzTTiUZSQk9rDkDgGPxfxM5i7QzqNeSFBdIHSQZ_Vn60hTpNrUKhq493npag1sys3HXA66J0KDcpt--BqpGn1RE-sEkZEx5ZhQ9UHZSmDIOboPh_aSt0ZuewiFNnYb9otIrLIgFvHmvQEMm3rBv9kMOtuZ9F-TnEL4XJ4dHmx57Om-aB_U1J-QFwCqM1gjO8vIGVBD3M-cDEss1xevPucX1MPXzvMFF6oiR2oSCJbdX_2qtqVAE5zDwJkcaEdN9Z77ACrtq3WazoVpjyoYYBZwpZLfj82WOlqxKbLMcG4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZB5oryrrC9fLia3wTPrqmLGWhLTWGj-UXk49K-mvTFJDtT_jFN_pPa2wXLntdfYYn4OVyjXBhVtQ0EV3cKAZqaQccc3ikjYONYjVu1DNEOnNYz6Fd7nuY98xw6FaUiWUntrRt5m0LlxCA68rhh5ZX4NCDwgISS4Mb1Tme-KSbBN35jm0Mlk4mjIm-GKfw4irPXs1F_KlJTO83R16KaaBHh4mI4vLes0r0KV6Bz79rWbKFNqoPU_vXbborpFGKEbIrBQ06UHo_SSAm7bSqotB6FvofSTOVmHycdRsiN0j2greZHEntuH8TigSnKeKN5evhlC78RlQSNVNXs_0QXvTvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSEOPHglMgT2eRqL5pOPjm2zV1iE9oA9ORXCpir6W091qOdmeFPhkhlUfil2vGnX3J5ni4F5TM_t8hNfsuhw4CTMIhfS2gfy2Qy26QGetHxHcRLZ2aRxAwJyyerc7VtPtmeeQkcil6m51EVqQ64SI1NlmMLeb1g_YzUXxQClDchugxV_Vpd2z2NFcbjDMNk5sEcg6rxFplgGtNOGW_k9o1EpN-Okl4TsQH3ZsYkrjUFYreIasqbVDPTrtQ0wCTlMcXogpK1XYUfImkwe8DxIsnKq9WJr03XLy-hNWbqFBnPF_TYqE-loDo-CEOE8YLdpwr2AhO_GUxEy3jPuBmISMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xub_ibqibpT5YcuQJhd39MIN_K7hheacdUpqKTT_fKnTI1VE7871RBPZgdsF8V63FaImLPftkyWfvcQC0d2CfmD2Ivnw40ya05RB7WgCJWlN1v6ZUb-upPwo_dUImoNIk9aN50pqi9UfTotUaR_gAfImkAiGySMMyDv1s1dTYxI4AVEQZPefPniVPyvTs52VNhHOvf3yZlva20s6sB149ozMnX-T55hk7QnAfWXa8MtIKRJ--Uotys6SG_bg7cw67qRe-hqhbxo94u9KSwd0MJvL6kmxF21IcxNraQdbFD-FPul3sHABodoq15gPz0LL_jjQhOrUJFMknhB0I7zKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlqtWhlORoi4Fa4mHVMBazqQwXgsh3q7YCteTOt3B0PAcz51eaOz1-Ykb3ggcLvwU1Bdy6rAAEsfh5zTwh3EZdBQTUS47ukI2iZqqa4heHMtjp--4uQvt_0JQpHDnRRLxqIfCV_u9dUrL3mYSI86cTaR9oa5E_tzLu5Q_xBwl92GLn1ImyqrT3CwuOyO0THbrlRoLTuoovLpo3fW5i55Svrz4gs9poNvkjgpe5pcG3HTdPnYKsx9AxqtQhwM4Sk-MGWI46m8k8ousJh2HZ5IZ72A8yrbwt9T1A7YovbR6X0KaZrxy9d9PQ0t494Pap8ccOO4eL4sROwMKVyI5XpX5iiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlqtWhlORoi4Fa4mHVMBazqQwXgsh3q7YCteTOt3B0PAcz51eaOz1-Ykb3ggcLvwU1Bdy6rAAEsfh5zTwh3EZdBQTUS47ukI2iZqqa4heHMtjp--4uQvt_0JQpHDnRRLxqIfCV_u9dUrL3mYSI86cTaR9oa5E_tzLu5Q_xBwl92GLn1ImyqrT3CwuOyO0THbrlRoLTuoovLpo3fW5i55Svrz4gs9poNvkjgpe5pcG3HTdPnYKsx9AxqtQhwM4Sk-MGWI46m8k8ousJh2HZ5IZ72A8yrbwt9T1A7YovbR6X0KaZrxy9d9PQ0t494Pap8ccOO4eL4sROwMKVyI5XpX5iiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=g6lRWjSTfYZko4LvJbp5GbX5ydRSCWc59RV8f1Q1Gh6dkeZprPcGVIBusryE5S4Q9g4ZKW0707ayUawU94Jo49yn3zak_b3DsRvB9SlrUqCv179gJ_ZUkOV00a_x6rAw4cTRNZBuLnioOZLtxd_e4DP-peIA2ePOBCYUJe86xeFtP2cyU5i9Pc1yvGEEpOzfZTaAaOBgA6cJ7XbMIZ5mX5A8maBbnwkiNFdHWng3BWKwAsQOx-dKqBfwam-ev7_AJwBbIsFsdqXvz_AVRFlQ7g95e5KF1t7G9bv7WBCPayMiAxPS2BSSXH5uiBELl92rbaHASLJZcLWsFPcp5RJ5DHXYPddVoCa8Vd9wxS_kDs9HsqPu9NwiSp3oOAvKST1PJ2ZG6YnLcJQtivjmVWtkf6q0moBx1A83qbk26tWXZ_lhW3Pc6jdM0Ab7ybtVav6Ld8YxVc02DI5I1NE4vdvJjiBpRmBSLuVDeJaO0GD9ZiOpxiyCyiKuTbmN8hxPp4y-GFdI38_x8XB0J0L0kLS3wPo12RUgCzjwDTcTiNGfsKRL5EInlQM2eVZLHQMaHHOuS7YkoTXL2KPE97RMMT4livKrDe2cFVGh4hVVuPFR5vGwO8gTpBD-nRkLyf-BLiyDgIMShKCjSShB4eNSRaRPUAyVjR49OHaLh5ImaB3yNiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=g6lRWjSTfYZko4LvJbp5GbX5ydRSCWc59RV8f1Q1Gh6dkeZprPcGVIBusryE5S4Q9g4ZKW0707ayUawU94Jo49yn3zak_b3DsRvB9SlrUqCv179gJ_ZUkOV00a_x6rAw4cTRNZBuLnioOZLtxd_e4DP-peIA2ePOBCYUJe86xeFtP2cyU5i9Pc1yvGEEpOzfZTaAaOBgA6cJ7XbMIZ5mX5A8maBbnwkiNFdHWng3BWKwAsQOx-dKqBfwam-ev7_AJwBbIsFsdqXvz_AVRFlQ7g95e5KF1t7G9bv7WBCPayMiAxPS2BSSXH5uiBELl92rbaHASLJZcLWsFPcp5RJ5DHXYPddVoCa8Vd9wxS_kDs9HsqPu9NwiSp3oOAvKST1PJ2ZG6YnLcJQtivjmVWtkf6q0moBx1A83qbk26tWXZ_lhW3Pc6jdM0Ab7ybtVav6Ld8YxVc02DI5I1NE4vdvJjiBpRmBSLuVDeJaO0GD9ZiOpxiyCyiKuTbmN8hxPp4y-GFdI38_x8XB0J0L0kLS3wPo12RUgCzjwDTcTiNGfsKRL5EInlQM2eVZLHQMaHHOuS7YkoTXL2KPE97RMMT4livKrDe2cFVGh4hVVuPFR5vGwO8gTpBD-nRkLyf-BLiyDgIMShKCjSShB4eNSRaRPUAyVjR49OHaLh5ImaB3yNiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUTz96diRb1tZcQdpH4zzlGBIvQyB0kXGwKzKm3bLmxIIPObIxWlAZsJjR9FamSJR1NCmSEINAUDXbB9ZeWwna1OTUxrooroajhtibM8c_iN3axDHV8K8BYFupc9Lo8VR1kG2t_RXj7gVE41e9TR8TzbUr4Y3v5N8R8H6CkwlT2CfWu0n_96kvuVVW7L06pzJD9ZZEe17zDzn4c2Hp8wHYdklaElj0SR0mXUMO5GOmxEdnRLJgqnRZiEHxmz0F4lJI0KaRjvVQhHQd_lyVcX1JjIaWnyj3IeMrqDn6MplgbkIgnQUhMCs17dzQF5FhxV2qllyKyiZczfumEXjtqnLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z42BQLsrxznawUDRQKK1iS5Cbn9fO_nIi6XzBniSiEy7-ZmF93oM9JBZfXYBZmgzcOvoskYKUb-Yb82nW5as7TAHQ_fS8vkLYGtEUeVu6PL6fYpUVVwSV5jALaO-ZjogR7qKk7POjRr5_UWQ5l0Zybtj7TljAYaoPi6wD14JwC0iOnS_jw5ZeYTVxpL1MqVHpIxSUSEwW5jmjkeqz_JEPNDP-iTUuyxcCBwjisrIm2AcUUgtd2jZx-acXx8G6vdxRM2-vAyyC_nbbhmReN1gyZ6-oNJQkhm8gl5KTw1fNzIlfRUps10Z5_ZHMjmz87r10kyTjO5_6pq-EWr_IDNh0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UckkojLAm4WflIB9enGbBtd-fY3gMPjIcFDiETsLUqXa-ukRJJuWhw-_uXoRIb5CfgFNpJDKVUyfA1CtnBt1G9lBva_VlBGN3ixLRtBiAKXSFpv5cfKtI7nnWreUogF46zR8j6ntN4ORbOYPWxyFnREsNrOFP5jfzol9jtzHQ-mLHVW-iU3uR7feiIN4CgFMBA4Krup51htvG1o5brqr3I6JeHTvPkTaNfRgD48EpcsuvGIfR64Uz4vxtT_5OJHSNwfF65PG61AGNnvOUnm1DUhpfH4mpO6dd9Pe_kubMAPIukFoVa7Nl4oVirYL_OPeex7-BE-6gQ2sCbhHhyCU4A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=qxJcz6coH1OppygPjjpc7xgGf7nDoy7rsGMnsRwg4QWQbukUSWvrdJYCO-R8ot9l3SIT46sF9httMoKSy-HRVWxJPsIycVAFrZ5FJqwsuUMHrBc8qRDqc_6WjxV9v_CdhSY2UuWv991KqE96Ac0lv-2KygAFmmVGHzWNP_YqPcC7eaiF84m5z01DLLe9OwfVGSjAInBafjz3chQH-CcULYUwFOlltrNpdcW150qjE4KUfxRvWDf4jMFODO0LPzsRSjxgOjv08fbFuGSn9Aq-uR5r8ju9JhU6WJGUsYiWBqneFE6ByEUCWQYSoz2irGOS3-uiEy48aHpyQXP9ObXtFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=qxJcz6coH1OppygPjjpc7xgGf7nDoy7rsGMnsRwg4QWQbukUSWvrdJYCO-R8ot9l3SIT46sF9httMoKSy-HRVWxJPsIycVAFrZ5FJqwsuUMHrBc8qRDqc_6WjxV9v_CdhSY2UuWv991KqE96Ac0lv-2KygAFmmVGHzWNP_YqPcC7eaiF84m5z01DLLe9OwfVGSjAInBafjz3chQH-CcULYUwFOlltrNpdcW150qjE4KUfxRvWDf4jMFODO0LPzsRSjxgOjv08fbFuGSn9Aq-uR5r8ju9JhU6WJGUsYiWBqneFE6ByEUCWQYSoz2irGOS3-uiEy48aHpyQXP9ObXtFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABMhD96CBEzjXyP7oFN_F1rn3PpoXt2ZR0Btx8l33CKYWqrwfGfaeRYXWib-6gZ3yDUq2Vb9WlyBMycGccLCA0lYZoJQx2QiichEpWtcfIlN3PizMkz9JNZzfWyIB9ho0YALTtpKOlGfviTutnhECmbvb1rgHAFGbjOO4n4ysZZFg3f3HNCZjTNjJsArSSbEQufr6_bbRVsZCOlgnp1s2gMvRhKe_7OrQQi1Skj5_semi_Y_6bhQuJb3LMmZlkgjqHojxNm65LaaAynSqx-dPP3aAzNU7hOaY-dBHpe4_vad0NKvgxylzIcW5jlCanQNkSFHXxmmDAwMw4Po-u0SfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=OvT9AEBgQrYjsHCp4LRCcAv1UyOmGHPDEHaHOvMqaHe9fm0vMcxemYSr0nyCY5wteyzm_X4cuBu76TxUMbkHOfkKIwhKBYdsGbju0FjJQHaMcgrBxFCvgGSbaZENyphYfJGJuCwU2gctHK1gpyyX8paQ15xRAbr5uySgcbmDkpQkz8WHEnozFEUBCsFqVmmilAEAkVqe0FAHSI5tK5Oe3qQoAGCRTqhOKNDwGt2RZuOK0idP8Nf67G5_MSNl7eldLgE1LY-ogpLv1FKQwYmpuIs-zghyiSxuWx6qHqrtwPyVk4_0hP5WNqiBdZELOns3-lxOHIsPrS8Necs0RWWlvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=OvT9AEBgQrYjsHCp4LRCcAv1UyOmGHPDEHaHOvMqaHe9fm0vMcxemYSr0nyCY5wteyzm_X4cuBu76TxUMbkHOfkKIwhKBYdsGbju0FjJQHaMcgrBxFCvgGSbaZENyphYfJGJuCwU2gctHK1gpyyX8paQ15xRAbr5uySgcbmDkpQkz8WHEnozFEUBCsFqVmmilAEAkVqe0FAHSI5tK5Oe3qQoAGCRTqhOKNDwGt2RZuOK0idP8Nf67G5_MSNl7eldLgE1LY-ogpLv1FKQwYmpuIs-zghyiSxuWx6qHqrtwPyVk4_0hP5WNqiBdZELOns3-lxOHIsPrS8Necs0RWWlvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKcik8OrK7s6wBAcenWDA8vSoF9Gd4STM_CB9gJJ2D2m91TE8rDgSo-pJYKqlrWo_3PcJtvLEhqUQEwMH2yOsEtK_UkYSYAXt1cuYqlA2odWSbw8bNOQYYpzGbXeIwpTsd3JYoDbOvQ4EcmRxlrvdcToj-R4HubiYlve8_0NwhE5SLKaBR-3zTWNOUq3tWUAQxjNmBHfiy_W2pMwtPeRQCXoJa_jhcWQ5WyJ9NCCnTAN08S9Y7Qz4Ah2XMxtYNLxvQ63QnoK_Wl47ya4lZpKxE2DplYV0LiEYGbQgNBCQCBNXFIaK6ne3V26dg8w4WBUB0Lowpe-4riid5ZIMTgXZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBbyr-ak7mWtZCFutaSXN6LwWaWsFfBWlpx7QaPUocaoMKQ1-z8fkH2Mfeou-OQelVMYJqpSq0HYKKVn7UxC7r-8t2cNAeK7KNOeuc7Y3SWif0VaNKkFuahMYEoVoKpWGhgyB6jWiKoETXTR9RmHJd57GQ_eyXlLqDA4DPEmBNGbcJUJjQtEMsZ91K3_kPNd54FswlOJLcYJveZhzxYUiunRRC2qn1P1wYycReflgNQhpin0pIi1QjEEYZcrTCqf0iuqC4Ww_pWNzyulNcI9uIy04e_O37yYm0xta6eCuLW1fxv-FBMgJlnFqTF1Ad1HgN1jS_xKFSwOh8rex9ISxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=n9dDMgDflTYK90-e0Yzr2RAflw60GoeTzqYzCgCLVMSagitBBFhj--WegWQpa0863fIfWz2FiyoYcP4TQBaCbP60XFtvFUPiH80jYKm6DQSUmNvZv-4WjR0KdeUPO8fJDcu1wY5tUk89muH3QmbXK_oAHVutR_mFBM4hZYWE0kzyzNLqXSAJISEid_vHqyDv4EUChGnynuxjP9yaR-5IvxdTmzqX7fsrV8boz2UMwfuI5SvQicG8SH6asTucqUPHpmRmzrS9Jnd-qtIwTtSSpimB9GBTY7sVE18spoKDRQniT7L5vof0dpp-L8_kYGeQq508o2UiGr1k0lRBdS2yAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=n9dDMgDflTYK90-e0Yzr2RAflw60GoeTzqYzCgCLVMSagitBBFhj--WegWQpa0863fIfWz2FiyoYcP4TQBaCbP60XFtvFUPiH80jYKm6DQSUmNvZv-4WjR0KdeUPO8fJDcu1wY5tUk89muH3QmbXK_oAHVutR_mFBM4hZYWE0kzyzNLqXSAJISEid_vHqyDv4EUChGnynuxjP9yaR-5IvxdTmzqX7fsrV8boz2UMwfuI5SvQicG8SH6asTucqUPHpmRmzrS9Jnd-qtIwTtSSpimB9GBTY7sVE18spoKDRQniT7L5vof0dpp-L8_kYGeQq508o2UiGr1k0lRBdS2yAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=hHSDBtraORKYb5N67DlNoocjyrYeA0bTJGSGwQ_tj1HxCd12S_RISrvl9vXkYnM9QvJkJVJNjYnobUtFVkb-Prd8FPntWA7-2WMfjWj_5Vb9h4ZphY_GiYpvZZUH2kG8YfcFzccWWG_J_WmQhV33GIAJ5O_Viw5cDfT0f4rxbCGy0kzG6Sd-iArfeFdgKRTD-flzJo5H1nuuoTaqe_fhkEOMV-SO0X21TyHO6TXXZWdWBVnlb9Lt3fsprNQ58c3ysfqGzIqOoSpZwo1uDXic-l-j9ms18TFOdzZQKcbZzdC35XVXp3BFtcCxanc-NR5eEcENj94QOLbtvLGYwxjRFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=hHSDBtraORKYb5N67DlNoocjyrYeA0bTJGSGwQ_tj1HxCd12S_RISrvl9vXkYnM9QvJkJVJNjYnobUtFVkb-Prd8FPntWA7-2WMfjWj_5Vb9h4ZphY_GiYpvZZUH2kG8YfcFzccWWG_J_WmQhV33GIAJ5O_Viw5cDfT0f4rxbCGy0kzG6Sd-iArfeFdgKRTD-flzJo5H1nuuoTaqe_fhkEOMV-SO0X21TyHO6TXXZWdWBVnlb9Lt3fsprNQ58c3ysfqGzIqOoSpZwo1uDXic-l-j9ms18TFOdzZQKcbZzdC35XVXp3BFtcCxanc-NR5eEcENj94QOLbtvLGYwxjRFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=uYcp_JmktQT9v-DQ3Z8RWYlo5mgHXj-5LnDxxjKpZ7g_7Lsrr6so70waNqO2IVIlB1-bA017k0Vzz55q--Oyl-la1I8A5pg8Kbo-JHGDcd222X7xK_KFx3oV44IBkJfmmjYLBHk4MYsbHUqYOTaDXUM0tFhYyeVfXmELwH1BsBxudmHGoegYV1yryAA_uWyHg2aOgsJpAWRxFVIyx8Svit-4fpWuz1TpQQ1D36Q5bD45rPL9MUH6CfZGfjaUEuhdlzihQcSwyHySqocrrdNxYjg4swxcNTR76F2j6y1AhNKIPf4DttJDkEjIJi8FAdXnPLD3UEOZd99zgbVS9OHGR78SkdsRPNtn9JvOMG1zZVD_tMc4mACPnNc2ncnydJeXGr_qNfS2Da9YT1qWFEP3DsFZUS6c-MFq9H_gFNDHHTVmWkyHwFTOQWQdasmcivwX91RwthM-naaic0bq_6MAB3zRoBMFdSXvJFl-wSQznCdelNyQpmtX_I9Q2pb7jaGpKfdyWdYXigMEH6JxI0fmfEOUXA5iKztuF5CeYePHd5cpaVe5--hMlYP3S1_8FRYmGtXZ0uklBqEkESbHqBT-qNMK29-cZC7RbwRWoRdFDcxEZrOgsJ6GrB-7jA4W1vQ3yf_RhaO7Sovhv7a-GMVgac9Gigyg_FlhKi_vcPp0zqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=uYcp_JmktQT9v-DQ3Z8RWYlo5mgHXj-5LnDxxjKpZ7g_7Lsrr6so70waNqO2IVIlB1-bA017k0Vzz55q--Oyl-la1I8A5pg8Kbo-JHGDcd222X7xK_KFx3oV44IBkJfmmjYLBHk4MYsbHUqYOTaDXUM0tFhYyeVfXmELwH1BsBxudmHGoegYV1yryAA_uWyHg2aOgsJpAWRxFVIyx8Svit-4fpWuz1TpQQ1D36Q5bD45rPL9MUH6CfZGfjaUEuhdlzihQcSwyHySqocrrdNxYjg4swxcNTR76F2j6y1AhNKIPf4DttJDkEjIJi8FAdXnPLD3UEOZd99zgbVS9OHGR78SkdsRPNtn9JvOMG1zZVD_tMc4mACPnNc2ncnydJeXGr_qNfS2Da9YT1qWFEP3DsFZUS6c-MFq9H_gFNDHHTVmWkyHwFTOQWQdasmcivwX91RwthM-naaic0bq_6MAB3zRoBMFdSXvJFl-wSQznCdelNyQpmtX_I9Q2pb7jaGpKfdyWdYXigMEH6JxI0fmfEOUXA5iKztuF5CeYePHd5cpaVe5--hMlYP3S1_8FRYmGtXZ0uklBqEkESbHqBT-qNMK29-cZC7RbwRWoRdFDcxEZrOgsJ6GrB-7jA4W1vQ3yf_RhaO7Sovhv7a-GMVgac9Gigyg_FlhKi_vcPp0zqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9gR7VKdzqBd0LsPhp_CTkk_HZnKP7PGwhuHzLMFGnWWf6CxaI7p674eOnlwCag4IRs1LZn2v-vx0eB_UsudRLmLew76Xs3nQq6TDiler1B5t_za9q5LAiG1jhmZpiWZ2-BBihqPrpa9PqiB9myK3eQoUJSDdHSErzGNbxB-Tm1HhnvcV9KIi8XQC9R-xbFMIisWBYeqA5kISxOh0P2aRPt9lFSNQL2Sinq17IhirFQ1W-qt7AY_1wIj0HcUhYWBq4oZeSkv-U5A6cjUre545kWeh8CFXl4ocalqlzDLCYiQvFMEpAN2E9w4Fk-YWPzthx60GnkO7InvGXv1-LGGtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNg9eryiK8mD4i9axyWDiXOuvdbkW0G-t3KO9_EPge6HCaYsxx9i6V0uNTebnMsYVo3HrDzjoT_BICZ6Lg-BcONXlMSuGiwb5rZv6zdF1WJoHWBodHG_ei0c-kwu8yeUPCKbR9X4idkm1GPG4-bGF6-n_SBLalHpyMxioaAd4WOV64IjNky1BVPdiPhxHY1hwe5izayp2H6NWFIxNPdNvjq0e5B7Hxv5RLG1rOPMNgr6g8v8jgbdZOCSZmEAk3V5MK8EMdxaS3_NaWNHjHXCe07iN0qHwmtyY4KpDGzzEYOorM16L64wKXooBi8E56-BP-7I3jiPanZpf-a_4krTpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdChFBvYa8z3Nwx_txAzOvl-LFaaQcIEb-_cqVZzGGp1Ph5oYwZ27UptuLOxFtf51PvQVD10pUtkfUtriGdjReFuyHrwJhq7-E1CxH-AulA5_hB1y8V-C1zJB7PcuZL9pVvApJ68n_Pk7YF-OFRcDYIEURa8POmzirtC19Ptr6odHCIh9Gzp_VPZCIWqC4IAsbnqeNM80IWtTjVVeB2DDGDZWxMdh-0_2yCnn4KIUSElW5BlUmKyqCNbManFeuSUoRis_ls2b_Yo8G2cmcx1nfLyqSNvK0UCTzDTPgUUQmTphrSUtXNN2h78WJjLNzb2ZyTrg1xMAuebXUel5Hg8ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=iSkIFFoj3_TTuBCzbG0amEApN69a9RHODTpQDNFOk67KrMq-LEaCZjt5oUHPMwmhPBGoVRn2BTSSu_dB5q6Pc78iKwPPwN4Jd0FqxIzbMA8regDXDWe9njUxxyvWJU1fp9obKCgVlVQR0ArStWHAAllP1BV5vysxNv8FQX52R8Ly31epTFo_bXI_foJ4R1EfMinP3-fsHv1Xb-oTKN2uP1kRM3mhkPWD8r-f5DcB5rWD9tBP6Jjy_exLxIJkdHtXijR2PGkrasUkqlCPVm0F6Zut4EA_wjyV2rY2BfIpdh9tDdJ3ZfhFwjSTfjdCJBI3dBZvoOskaK6QS9g4O5VS34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=iSkIFFoj3_TTuBCzbG0amEApN69a9RHODTpQDNFOk67KrMq-LEaCZjt5oUHPMwmhPBGoVRn2BTSSu_dB5q6Pc78iKwPPwN4Jd0FqxIzbMA8regDXDWe9njUxxyvWJU1fp9obKCgVlVQR0ArStWHAAllP1BV5vysxNv8FQX52R8Ly31epTFo_bXI_foJ4R1EfMinP3-fsHv1Xb-oTKN2uP1kRM3mhkPWD8r-f5DcB5rWD9tBP6Jjy_exLxIJkdHtXijR2PGkrasUkqlCPVm0F6Zut4EA_wjyV2rY2BfIpdh9tDdJ3ZfhFwjSTfjdCJBI3dBZvoOskaK6QS9g4O5VS34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=lMiinNbJ0pPRMne9N_SB4COTeslr47kuLfgSNSifghr3r330KVnG7Lc5UhY7El3LjQqFNGPjCeWRUMsO0oPqO5jgpSZ5taJIeJBR5PMPkPVX55iSJ4CRt0Ujpi7kGvUjJsbnAIsfOJxtc0oBFIdVv0S6hIwSpY6x674108YE5GVtsfxopIyjmc8U8xLsrxIgGfadvQkZeWnnzjWdQtztap8r5ZVlqen14zfklPS-bg596by7w-72uG5ZZEESI_trmTwRnidkKPJKFymuH0_Nuv1qXiw4wfg_6LfIuSPVM-8BsqiHBWIz2DVmWRXqawC2N6y9eK9vyPtOVjCPNg-0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=lMiinNbJ0pPRMne9N_SB4COTeslr47kuLfgSNSifghr3r330KVnG7Lc5UhY7El3LjQqFNGPjCeWRUMsO0oPqO5jgpSZ5taJIeJBR5PMPkPVX55iSJ4CRt0Ujpi7kGvUjJsbnAIsfOJxtc0oBFIdVv0S6hIwSpY6x674108YE5GVtsfxopIyjmc8U8xLsrxIgGfadvQkZeWnnzjWdQtztap8r5ZVlqen14zfklPS-bg596by7w-72uG5ZZEESI_trmTwRnidkKPJKFymuH0_Nuv1qXiw4wfg_6LfIuSPVM-8BsqiHBWIz2DVmWRXqawC2N6y9eK9vyPtOVjCPNg-0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=qM_Y7YNS5g_xhy6Cn8sT30kWEJ6lKw-Gd9tkZbmo5qGNrf7mK1yh30iEOgeAxNE1QcYYym4YPnUU0agpI2lxLmmBDc9Egc1mvNZJTMw3Jin1FKoMfEq5b_-kdKZioC-6dt3WHggGAPLZ-kTH8XAA7nGWM06eA_BigSI9AvLL2-IY1J3lHlytrkM7l5qbsYjEtyYjv5tZnDjnXRC_nn3O4XsnCILMzOuzRpUxSe6JmF0LIIt0taREjHDvDK55te_ZQmePiR6ia-wqPJt4-2iCFZbKls-rUrAv2JpjQSYyx2WrWpe-al5HceX33lUAz63KkkzbjlEEOFmx-3KkYCpkpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=qM_Y7YNS5g_xhy6Cn8sT30kWEJ6lKw-Gd9tkZbmo5qGNrf7mK1yh30iEOgeAxNE1QcYYym4YPnUU0agpI2lxLmmBDc9Egc1mvNZJTMw3Jin1FKoMfEq5b_-kdKZioC-6dt3WHggGAPLZ-kTH8XAA7nGWM06eA_BigSI9AvLL2-IY1J3lHlytrkM7l5qbsYjEtyYjv5tZnDjnXRC_nn3O4XsnCILMzOuzRpUxSe6JmF0LIIt0taREjHDvDK55te_ZQmePiR6ia-wqPJt4-2iCFZbKls-rUrAv2JpjQSYyx2WrWpe-al5HceX33lUAz63KkkzbjlEEOFmx-3KkYCpkpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=ty6dbHhjUb3KJlcdUjYNyZ1Ukgo8Gzey4v7pgHQkwic93lm-cvf48BIkrWzTGStBC8IERJSKTpVhJbup9Q2rM6ibI4rLi4V9iuBJn6593EXQHgUUhVGUB4hH9xFz-QiY4qIWnmJI58D-s7uByGMpCqYiYC2cFwj5J0ImJIlbfyygu5lvl0n1cHzeJG-Yv9dCgOSbjjN1XOIUO2kL43AssqyvZ0EEoIxq1JpDkg97X0vuzqIfI63bmJh1W_x_dk8yUHXpeInPfceGL_9Z2sdiSeDMMNPG9zNKqUJhRaCA4Lf2xoQgS8x6JqmJfkxXnK2PgP_iHCvCkDdzGPVz2_1mQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=ty6dbHhjUb3KJlcdUjYNyZ1Ukgo8Gzey4v7pgHQkwic93lm-cvf48BIkrWzTGStBC8IERJSKTpVhJbup9Q2rM6ibI4rLi4V9iuBJn6593EXQHgUUhVGUB4hH9xFz-QiY4qIWnmJI58D-s7uByGMpCqYiYC2cFwj5J0ImJIlbfyygu5lvl0n1cHzeJG-Yv9dCgOSbjjN1XOIUO2kL43AssqyvZ0EEoIxq1JpDkg97X0vuzqIfI63bmJh1W_x_dk8yUHXpeInPfceGL_9Z2sdiSeDMMNPG9zNKqUJhRaCA4Lf2xoQgS8x6JqmJfkxXnK2PgP_iHCvCkDdzGPVz2_1mQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-xJzCgT7vq-5v44OWz4fRggezYavnNck_Ifq3xeUfCvwEaozd7RG_fM4rqYKP15hj6dnvk0psTwbOVK5SBEQJWc0BhVB9Y3_kzaWYEZVlfYouIKc3Gwk50dDOOSQFZCoaPZsUzmcnUdlGMHHI6XigdEML1tHalwnwoqMPXW5lLZfmsNi__CftnY6TDUkl1sPX39NQlNpstw7j2bCkKILaNZ4mOqMiPsdblRkbB2kBQpmd9aUgINcw8E4vDeFgZ-AtPGv5l3jIBe_CnLi1tRTkCimdr1ziU7CFGHq-m1lpEdPDc1_pk6KuMK7Gs4qrJXEM0mrLyF8iJ3FRTHW_CzuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=WPvsJfvZ5W8IJEnkz-J4kHVo8FEZfC3TrkG-vLHCW-3t7I1JFHgfnoOwad5UhnI9Z72u1lSKwtbzmCKDHTvY-be2jHLMI2fsrOR3fmULDCToDBi7tLzJ4O7jdFjUXLuCoic_JAiLBBaXH1dKt1-MAhCUtFa82bLbkAYQeCGCeaMM8EFYwmOBeEXaUT6eVxqhRTA4s8muIskBXaKcYvjVZyQn3RGYKifCeQwJuTEMq9dfowBRB9FyOZJdECnRV4GYTMr9ukmGwavMQiXNJCalyhVLQAhLVVfZUpPTUSDsKz-MQNFpDd1Zd-uELL2N-9d-wbneI0xDNumIY9h1bes1a3CtcCBJQdE5hAsNt7UU0oYHrB4vIY3x8Y1QmIVug3Jbe3dIW7Dq0YCpLOZpbXdJhnXwlDk99ez_XnBXpgEPvfQ6Ha_o2sDl_douULUl1Zi2tK3zlAEJ9jYS1-DugMF8_fL9n9JWrCAsrcgX632mC84cVv8K1rJqUAKUz9C6CuLlXAQNBnPGxAkM-UB5Mc0wLJlpCQ6LlO3ksebqM1GOx8rW9ibt43dlFYsvudPNnc9UB8USJJT3IwpLGW1rR_7G-68VC3Rwpa6vE45mmhOINuqG5-T6EaOKjmh1tQyAAe0QODHpRBA7LYZ0vYJ4meFshPfenAZG3Z1M_kHvA72536M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=WPvsJfvZ5W8IJEnkz-J4kHVo8FEZfC3TrkG-vLHCW-3t7I1JFHgfnoOwad5UhnI9Z72u1lSKwtbzmCKDHTvY-be2jHLMI2fsrOR3fmULDCToDBi7tLzJ4O7jdFjUXLuCoic_JAiLBBaXH1dKt1-MAhCUtFa82bLbkAYQeCGCeaMM8EFYwmOBeEXaUT6eVxqhRTA4s8muIskBXaKcYvjVZyQn3RGYKifCeQwJuTEMq9dfowBRB9FyOZJdECnRV4GYTMr9ukmGwavMQiXNJCalyhVLQAhLVVfZUpPTUSDsKz-MQNFpDd1Zd-uELL2N-9d-wbneI0xDNumIY9h1bes1a3CtcCBJQdE5hAsNt7UU0oYHrB4vIY3x8Y1QmIVug3Jbe3dIW7Dq0YCpLOZpbXdJhnXwlDk99ez_XnBXpgEPvfQ6Ha_o2sDl_douULUl1Zi2tK3zlAEJ9jYS1-DugMF8_fL9n9JWrCAsrcgX632mC84cVv8K1rJqUAKUz9C6CuLlXAQNBnPGxAkM-UB5Mc0wLJlpCQ6LlO3ksebqM1GOx8rW9ibt43dlFYsvudPNnc9UB8USJJT3IwpLGW1rR_7G-68VC3Rwpa6vE45mmhOINuqG5-T6EaOKjmh1tQyAAe0QODHpRBA7LYZ0vYJ4meFshPfenAZG3Z1M_kHvA72536M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=OFTXVtxpKkcVj0RXVqyM-hiPylZsgqCzHJ0tD8tLosBCakrnshbMERLpxKBSY7r4J1JLzu-ghPhI6WDWVfnwK8y0MbKxPovm9q7LaXD6sQHjX55h_LH1GfNjTZLCwgTnEco6mOkjsNGQzZFaDWYZpC5fYmzpjNIQd_DEk1Req4HB4A0nnDY4AaeyIH_D0TmztAu0PJIyPBz9aTiIwOO1kCm-36dVpZoIdDsm-engp_BwygtFiP4ywk43Zw59019v9AfdX0DQzaEp7eZEkLvvVNz8cozPfFH_3ag5Ql462faROg1KGYHa6MLAzl7gSjfNrAeFkwJJEB_00qUHbdIRfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=OFTXVtxpKkcVj0RXVqyM-hiPylZsgqCzHJ0tD8tLosBCakrnshbMERLpxKBSY7r4J1JLzu-ghPhI6WDWVfnwK8y0MbKxPovm9q7LaXD6sQHjX55h_LH1GfNjTZLCwgTnEco6mOkjsNGQzZFaDWYZpC5fYmzpjNIQd_DEk1Req4HB4A0nnDY4AaeyIH_D0TmztAu0PJIyPBz9aTiIwOO1kCm-36dVpZoIdDsm-engp_BwygtFiP4ywk43Zw59019v9AfdX0DQzaEp7eZEkLvvVNz8cozPfFH_3ag5Ql462faROg1KGYHa6MLAzl7gSjfNrAeFkwJJEB_00qUHbdIRfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thOuwoLpF5yLcXdp-AnBd8JQ01r9vvDF2JyeJ5c28j9LkPK9TyR7nv65-WRVlGVIXMbV7Hg_UODGmpFec_T_rZqFv_Ys128ltg-G-tNI657P9ntWO_FWBUVsOL7rYoYPwXYnq8ijSsxnxT_GeMuyFSP_eluGBwjHI2mZMxCWkRNBt5OPWYZNykq7F-xUTkLhBSi6_bam6b8gnKXJrl9foGRXdJJ1hgC2obzmmzUE85D88sRxJcMNrsybmP99-mOhdvWWgjtHv9TT_WlE-0UpBCcMt9aj3mKVBLF3AUIjCg-DB8wmxTY6L08tRioZnauMmP9mTCI8icAfCfFSTvVHnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=RqQsm6xaW1UpMezFQMGscFeqMpp6Z2TvjHPhAk0ItKsqz9G_CElnWpX1vkeXmd4tVxPiDQOO8RLtzpUK2YejLyeu6e3bz7GCH-PLTs1At_adGeIDGviW8mrh5s3-TMInQt98DOJqI69thOnh_uARywD36wC_RxAjrvpu5u3d1BCEBjcXlStPfmKd34-Xe_UGUd1tCG_Zkigzk9BwUJ92Ks5T98HwrOKdzFOg7_lczjZRuI1n39G7ZmwPusmROoPPcAUPBfxQ_g_FRktj8x4t2gb8uDw-L3J8YVBZWKZB81TpLZSCgdOo_T2MZhX5mxJGSb27sRn0vpcWyBf7t9WWog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=RqQsm6xaW1UpMezFQMGscFeqMpp6Z2TvjHPhAk0ItKsqz9G_CElnWpX1vkeXmd4tVxPiDQOO8RLtzpUK2YejLyeu6e3bz7GCH-PLTs1At_adGeIDGviW8mrh5s3-TMInQt98DOJqI69thOnh_uARywD36wC_RxAjrvpu5u3d1BCEBjcXlStPfmKd34-Xe_UGUd1tCG_Zkigzk9BwUJ92Ks5T98HwrOKdzFOg7_lczjZRuI1n39G7ZmwPusmROoPPcAUPBfxQ_g_FRktj8x4t2gb8uDw-L3J8YVBZWKZB81TpLZSCgdOo_T2MZhX5mxJGSb27sRn0vpcWyBf7t9WWog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=A-gqyIXBhP8gJimq5EXmOVnLSPnbH68Ic7pDTbs_EYmlIKu5fFq5IZsMTvIE-I2FDuuTRC2SoB6OeThpVSsrbECqZBs5MkKLNHlqCLf1n0F7vDJBBcg-a9QgZ_r3MVPxST36CWATtp7Gvd_ara-kx-fVpeTrSL4dVa14nd0Hng_Ws8qfz3dX5KhBiRyCsKxON8RI3UnNCmKNsFLQUGaXj25o94smO1UWlptz5V0VIzbcgSBYxRuhQ4QMuqbpeNJjMVu0h_E0_rYA8I1q2WwUcGHLlDSX6LTtdd5mZJBGJT4CSFBU_F7-ey9yS1N8-xO824VDT-jUbdV13SXUf0iK7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=A-gqyIXBhP8gJimq5EXmOVnLSPnbH68Ic7pDTbs_EYmlIKu5fFq5IZsMTvIE-I2FDuuTRC2SoB6OeThpVSsrbECqZBs5MkKLNHlqCLf1n0F7vDJBBcg-a9QgZ_r3MVPxST36CWATtp7Gvd_ara-kx-fVpeTrSL4dVa14nd0Hng_Ws8qfz3dX5KhBiRyCsKxON8RI3UnNCmKNsFLQUGaXj25o94smO1UWlptz5V0VIzbcgSBYxRuhQ4QMuqbpeNJjMVu0h_E0_rYA8I1q2WwUcGHLlDSX6LTtdd5mZJBGJT4CSFBU_F7-ey9yS1N8-xO824VDT-jUbdV13SXUf0iK7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAlqtCXy2Sra7NDXdb20udnEBh5VxES1B8TNtOFElOiY8uFJ7Lf-FtJo23hlf8ROsUG4rukSS9UZn8GK_CObknlX1L35Z0cNueM47Ab9u33mV572Rvhd7hZsObn38iur2bo9wPn86Ckj4rc_f-5kMnXvV5NqEItUTw_s8Ypgpw8L_Q8GvftDQpzNhUqZRU6koptD4MAAAvvruv0qnATXOuXfVZOgbl-9bsKXIlJdzaVs9W77-fVlpVyn43twBkczS84Da8voVjvQOv9W9xjQPOQnFlK8sL6iHFTSrSU-pxY3LXoLV9kCaITNrYLRQ9aoXGoBEOeLM5sLIA-El0IAEQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=IeTKDZDx4gRs7lerob1Xc8ogykQHYYrBIVNpJ6KET9jdgJREN29y5jD_8nDwAQ4E5LdgEv9TxTTv5mDaQB0nnRhKnZvzJpfp4KcOh5kvaTxqAF6LcbThM_Nqi1lZIDwGcT_Lx6ByNu6X3ebFMijrQwyq7oYuqbn9CW3HTx9OuMwc4P9bo5cF-DrLPf_MRalBkw_GjzMM9edec9RB0LB3FKv7TJUomQEio0MNYCZJrpFz9ZD9MvHB53NjHlC3H1pBb9zBTDgmixeI4NyDO1wm9HDXFo5P_NXykoBCdRf2wd9LxWjPKZvlEQd38CQJTUdtNXwZkBuNd5uCK9QHWTuyJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=IeTKDZDx4gRs7lerob1Xc8ogykQHYYrBIVNpJ6KET9jdgJREN29y5jD_8nDwAQ4E5LdgEv9TxTTv5mDaQB0nnRhKnZvzJpfp4KcOh5kvaTxqAF6LcbThM_Nqi1lZIDwGcT_Lx6ByNu6X3ebFMijrQwyq7oYuqbn9CW3HTx9OuMwc4P9bo5cF-DrLPf_MRalBkw_GjzMM9edec9RB0LB3FKv7TJUomQEio0MNYCZJrpFz9ZD9MvHB53NjHlC3H1pBb9zBTDgmixeI4NyDO1wm9HDXFo5P_NXykoBCdRf2wd9LxWjPKZvlEQd38CQJTUdtNXwZkBuNd5uCK9QHWTuyJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KD2pX4c6XKtZ--mxL2DdGLyazB8Z3JodlCPLJ-7xEbeM-ND9UKohIAFD6S5PEpSdSq3-HPgkUjQtMq69SnCYv3eOThVjaNHF6jAM_dOwVfG9hcv0fXcX7DqYyXtJrH2IG4nXlgD87J8PhGU6oTb2Z754nwiU_28rEF1-Ccgc3BfFYhbkUvPuY02oKrXeaRCZsLxpFoInUH8JEW_iVVIFcQIPmMYPXq83pUjee_prgfCKdGAKh63DQjquL0XYxkIVFef5RIiFNvTLU2DihyRTAJv4VqxbsZ-kXo838Um9YRiuKCSUOeNZYS4OQlz7kwHSCBXxKd1TdiSt_Pk8DPKKKg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=OGc-btdWsOjyQUikOWvmKTvZw1qVBvY9BpLACtlxwXRKPoDZCqI3zWzlGtcVE6NvBF8l92ncMgB2z8uhJ3q-zYRNCuw7efznYFOfaTvg6Kol4O2QfDaJb7F4J7BMU1W9rAodjQDpcoTkIWdIYtKodTSvznvhL6byg1XXOKUxzgV3gHu2E-WXQfToizmWlOLmtek2nKSRUFLvb0fOfG1BmjRZLS4OKV0DHYS6iHuXhRqPLbiIqG8SzIR_uCe_GatVRRzeaROyOLJT1IeGHeLQR1y5CWj-RgMPmmJtKEzGKS-h51ZkLHOuXfqu8k_O5fVC-ngwxhJZH5fcrr3Hphr2IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=OGc-btdWsOjyQUikOWvmKTvZw1qVBvY9BpLACtlxwXRKPoDZCqI3zWzlGtcVE6NvBF8l92ncMgB2z8uhJ3q-zYRNCuw7efznYFOfaTvg6Kol4O2QfDaJb7F4J7BMU1W9rAodjQDpcoTkIWdIYtKodTSvznvhL6byg1XXOKUxzgV3gHu2E-WXQfToizmWlOLmtek2nKSRUFLvb0fOfG1BmjRZLS4OKV0DHYS6iHuXhRqPLbiIqG8SzIR_uCe_GatVRRzeaROyOLJT1IeGHeLQR1y5CWj-RgMPmmJtKEzGKS-h51ZkLHOuXfqu8k_O5fVC-ngwxhJZH5fcrr3Hphr2IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMrNNbHrULpjeSQOph6qKLmtiYoKoLRxUARUejVZBn46ebIZXLShYxWn2xbdfbdkFsMSu8ZZ9OeKBaddKGZsUQ81mYb_CXictWzGhY6XeXIozALIeeZALoovAz7FIj8MtRVv0wjh4U27WVDRZH_7oXO_Z41NtdMrirf9S9FH68bB4nsASQbzoE-16Io5qu_rI1IiSSTSzwTJIEtjDtR6jFOC5tWA_olR0C7B-DMcr2TjvEnvqIV5N54hjJMWjK3erLNsf7XCDjju8IHvlIcigpdsotZ4c96joYCRe2wzCuswaMT1Wm4XseEgGF_S_aS-fPpkA-E9Ogq2LXo3bxIMKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=rWdkyfGECYKrmpToDPzazLgR8vmWUCoX-6HZhD8jOesQoVBTPRaSjIHTmS7HwiCDPRkwENC2iSjcLtj8jKhXrHgpnz03-LexYJLaiOq-OkBW25jVpgqsy_VX0_aGBxi76Vl51T0PhgwyFEqTyN76eMMmI5dVH3lDXW8YUrtfGnXVk_j26MrPNdMm5puwxiiSn8ywjIPpZjP7Sqlc4sc5pXfHwUqIKeUjQ_huZ0U5j7xpFJnfwXxFGLpxwUirdaKizijIJdRxoGTKmhz4ZSgq_y8KWzfzw0HjW2HtNnfed07Q5PbhHRDiuCFuMjEffx7e323jqflhTTw5K0ORQsXkzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=rWdkyfGECYKrmpToDPzazLgR8vmWUCoX-6HZhD8jOesQoVBTPRaSjIHTmS7HwiCDPRkwENC2iSjcLtj8jKhXrHgpnz03-LexYJLaiOq-OkBW25jVpgqsy_VX0_aGBxi76Vl51T0PhgwyFEqTyN76eMMmI5dVH3lDXW8YUrtfGnXVk_j26MrPNdMm5puwxiiSn8ywjIPpZjP7Sqlc4sc5pXfHwUqIKeUjQ_huZ0U5j7xpFJnfwXxFGLpxwUirdaKizijIJdRxoGTKmhz4ZSgq_y8KWzfzw0HjW2HtNnfed07Q5PbhHRDiuCFuMjEffx7e323jqflhTTw5K0ORQsXkzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqgku5avJETYWGJIL8jdEYkD75hkxUkBWXhXGJMWLZ26yZ5aHwloKQdvGNBncljg5cTQGR3eSQD8f2KahNjfECgF74ivi9LmUpjpP8Msmeq5MZ3fPpj7fs5M4lCZdFl_9HvCzRy5MBbUiJplDbOsmKQeAc3CnEmyXApEQ8kkgevk-X9kBsL_OautGkXWHezij6CSWS3HRQR5Am81tl-dxUF09Vfh08UY2BSGgrG4z3HIbv1xAkW0wVPhaJ6XPtDrKQSxSu75ow4GF-ooIolqaC7-Maa7_5hAjZd-kxAxsChK6XiVaA1NyuZqW5EIhVbnneh8HTbrN4Tz63YP6CS-On5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqgku5avJETYWGJIL8jdEYkD75hkxUkBWXhXGJMWLZ26yZ5aHwloKQdvGNBncljg5cTQGR3eSQD8f2KahNjfECgF74ivi9LmUpjpP8Msmeq5MZ3fPpj7fs5M4lCZdFl_9HvCzRy5MBbUiJplDbOsmKQeAc3CnEmyXApEQ8kkgevk-X9kBsL_OautGkXWHezij6CSWS3HRQR5Am81tl-dxUF09Vfh08UY2BSGgrG4z3HIbv1xAkW0wVPhaJ6XPtDrKQSxSu75ow4GF-ooIolqaC7-Maa7_5hAjZd-kxAxsChK6XiVaA1NyuZqW5EIhVbnneh8HTbrN4Tz63YP6CS-On5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6GCexRHVFyt_8azDuosH_GYaxDbjseECQ9pOZA7ma4QxafacQIKHFp_srXn2hxMbiez82JZJUS9i0QlcdADXkiuieu_X_jZp7oNs71qpSzvErc8KZSXHfpk94_OFibkCVJJ4EofsDkqiQBtAP9P17d24qyzmp0Lc9wR6kfFa5adkt9o63P448I1hLtsGT0WSqn4X3HvIDiZ1KXX5uXB1ytWQrxpNyCDdDyk2gJnsFVyHlx1Y9TxuRu0_gVpLyl7WRlHSUT7zSSZ1TvS8JUqWOOfWixYDgUFPqCcOxxMC1bKhQakxEHMwz5XNFDngiVuScVI_0tQYQjY_M2UabZlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=pmIFNNYYJY6pMP8Qe8B3pT_N0Ih42bHbjOXvpFtb8LO9hjfTmKXQzYKohCrXi7aT3KdAcXq62zqBi3szTWq0d5_mc0vCJfwTAfnLTvD4TAl1HXr16EGSOF9_-3glD3p5Ep1OcmHtHbAp56CH9If09j-ivOPN5crzLASonGfUYKB-MgVrB9WNX7egmRrdfjuR9toUgMBV6RndMOMeaY0pqJk7N3MAGuxfaVIblgR4QthKbae9u-fdo7C45ZVAHUS9RWIMNRcd0UZ8LEzc6E80YlFyczmQnDqhzgdaM9ek8-XHqXjU99H29LBEvE9xtKuXcOqOB-rmKc2rOK4Ylh-HUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=pmIFNNYYJY6pMP8Qe8B3pT_N0Ih42bHbjOXvpFtb8LO9hjfTmKXQzYKohCrXi7aT3KdAcXq62zqBi3szTWq0d5_mc0vCJfwTAfnLTvD4TAl1HXr16EGSOF9_-3glD3p5Ep1OcmHtHbAp56CH9If09j-ivOPN5crzLASonGfUYKB-MgVrB9WNX7egmRrdfjuR9toUgMBV6RndMOMeaY0pqJk7N3MAGuxfaVIblgR4QthKbae9u-fdo7C45ZVAHUS9RWIMNRcd0UZ8LEzc6E80YlFyczmQnDqhzgdaM9ek8-XHqXjU99H29LBEvE9xtKuXcOqOB-rmKc2rOK4Ylh-HUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=jcIbLQR7wMDmPhKd7K5-FSeV0cZXuBy3P93WuY2vjTO6ilcgsqgl-22rZDMTa0lEU3948irRniaBnd05pZ1kF9A4OTnSEl-jBrS12xoebOImty2qXL24_W4626yJq86MfgYTKSyHHvYVbE5yXcrka3w_X_8DGzFKexWSHkF8_IB3R5uXPNEZI9uKRHnEN-Mwa8y52I2wqPLxUenjqP2YqY2mWYOW4IpRfTB3qJdR0lIFe_Hn6XxUHYHXffcYJQzTyn93tFBi-JgyXg3Rr2z41IUy84PKau6PAixYxw-JD5f4t5iJQypL_-nBqxti_Yh6Kr9_vlan3zboHYWLE1o6Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=jcIbLQR7wMDmPhKd7K5-FSeV0cZXuBy3P93WuY2vjTO6ilcgsqgl-22rZDMTa0lEU3948irRniaBnd05pZ1kF9A4OTnSEl-jBrS12xoebOImty2qXL24_W4626yJq86MfgYTKSyHHvYVbE5yXcrka3w_X_8DGzFKexWSHkF8_IB3R5uXPNEZI9uKRHnEN-Mwa8y52I2wqPLxUenjqP2YqY2mWYOW4IpRfTB3qJdR0lIFe_Hn6XxUHYHXffcYJQzTyn93tFBi-JgyXg3Rr2z41IUy84PKau6PAixYxw-JD5f4t5iJQypL_-nBqxti_Yh6Kr9_vlan3zboHYWLE1o6Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwGghiyUwE3_fcocN4RcSm-c3Dj4i5BQ4YxaUotzm9JUIvdBlQEaCOi-jCcRCvk3PnGZjBApkV__D7B_A1f8KB6zj-4yWjR9-xZ3ks5PuG0-O6b7QRJeXKpEJETiAwlIFws3LTtDIsEA2IqE2xX-kfVegoo97qU4QA7X9Y3NKPk2p5vyjbaZZzLN23ob9d3eftTsgd1S6S_aN_I2RcUCTSPH-_Qoy2rqS7OBgYtyqgdtA30cu5tm1Oomhy3eFxvcABJtoaqfhtzb-q7-7s5eUtsWqF3vOeT_JmugkfpH5_NEhd4sC3w9CoSl_OlS-gnwTzKzhxPlOidDYj1yGMHbQA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=eUv4AENSnJm8rbceAkzaPVr1MDn5ODCqMpPZhCdZ30bbJEXGDDribWCfVlJ-31yHeyi_VI79jWqwTIexnySfforzBYFyyiXkMnUkKfW3f5cOUiMIqJGVbj_dEVUIk0UcBsL-4TmrGYUt1Ui2rqjwY0UsOzu-423PDTHAfDsi336dzIkDdrj10ug_Q_cVAXDK8JE4zlJnmW45u2nHxVTGwBHMbk8MzxDYT4IQugEyWz7Tu-21shMaQN2AzXJGhsod7EsOR6qUJXypIIolwu5wqsoycOpiODWApPHclOQr1H7y_LB2RC89Q5yT_0xVvPmiHIk6mnm9_DfW8fJkY2Xtsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=eUv4AENSnJm8rbceAkzaPVr1MDn5ODCqMpPZhCdZ30bbJEXGDDribWCfVlJ-31yHeyi_VI79jWqwTIexnySfforzBYFyyiXkMnUkKfW3f5cOUiMIqJGVbj_dEVUIk0UcBsL-4TmrGYUt1Ui2rqjwY0UsOzu-423PDTHAfDsi336dzIkDdrj10ug_Q_cVAXDK8JE4zlJnmW45u2nHxVTGwBHMbk8MzxDYT4IQugEyWz7Tu-21shMaQN2AzXJGhsod7EsOR6qUJXypIIolwu5wqsoycOpiODWApPHclOQr1H7y_LB2RC89Q5yT_0xVvPmiHIk6mnm9_DfW8fJkY2Xtsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=txW4MXYaLzY_RaKNhvKroTQjr9zt-UHdLOepFT_0sX12S2A_P-xgb-fJNkr2iYUKb3KDTQnfS0-U6DfSQ2lYSRDlaIi-exjcHa_vccGr0_ETiuqcR-A77MZCOTANKrfqCJXztGax8z9djmYCIkW_wBVoMtskuw_u1Cu9nMCR568rhB41SxxTajvI6bay8hUwFr6aB1aqZ1PgBeD5hKn2nhXwHyFWlTtqSI8GIfFHi-EqB7jZR_NXHe_NVnvFjhSXB-Q4yqIm4f7Wfn5wu5OkqqBNfAK24ULvSIkRv4D-O4q3b8YCpLisIlk-E8zVM8yxwN2WEYxP1TupVsWx2F3ovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=txW4MXYaLzY_RaKNhvKroTQjr9zt-UHdLOepFT_0sX12S2A_P-xgb-fJNkr2iYUKb3KDTQnfS0-U6DfSQ2lYSRDlaIi-exjcHa_vccGr0_ETiuqcR-A77MZCOTANKrfqCJXztGax8z9djmYCIkW_wBVoMtskuw_u1Cu9nMCR568rhB41SxxTajvI6bay8hUwFr6aB1aqZ1PgBeD5hKn2nhXwHyFWlTtqSI8GIfFHi-EqB7jZR_NXHe_NVnvFjhSXB-Q4yqIm4f7Wfn5wu5OkqqBNfAK24ULvSIkRv4D-O4q3b8YCpLisIlk-E8zVM8yxwN2WEYxP1TupVsWx2F3ovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=blFfBiLOkm1tAx4A-quKdY4ZpTMrEXd41ivhjG1_NrAXxvkzCxlBWqtLPujBB5YN0rRG4SW4IPx2M2hCmyT2DgKiu1tm-ojxNjY3FCdmqt9r8FlXERiORiLmc_paBH1cdUovv2_ygrT-yqsYMHQ9XTL7-GjWPzpnyMBufFJS7lvzADeoch_wdMEtNazgGg93W74EPW4wQ6cUQ2wNqdiIUpO1a-_7JZkUDI83BcCMPQuU5zzzNwuxn8qvqzORuhLblnQs9RiIDPPeQjSRyACYJ9DpWrx5FA8mnKY6LGx0KrclhQ-Z4WhvLDxbJULF9pCQ8L7vXphyAXEV4hVPAR8ArQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=blFfBiLOkm1tAx4A-quKdY4ZpTMrEXd41ivhjG1_NrAXxvkzCxlBWqtLPujBB5YN0rRG4SW4IPx2M2hCmyT2DgKiu1tm-ojxNjY3FCdmqt9r8FlXERiORiLmc_paBH1cdUovv2_ygrT-yqsYMHQ9XTL7-GjWPzpnyMBufFJS7lvzADeoch_wdMEtNazgGg93W74EPW4wQ6cUQ2wNqdiIUpO1a-_7JZkUDI83BcCMPQuU5zzzNwuxn8qvqzORuhLblnQs9RiIDPPeQjSRyACYJ9DpWrx5FA8mnKY6LGx0KrclhQ-Z4WhvLDxbJULF9pCQ8L7vXphyAXEV4hVPAR8ArQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=c3NfCeioKHalGJCxL058pukgiIwaOnefIUtkdXjJDShXCH67fR4PlmKxjT2xhuJ8CvQ127JqUPWrBfs1CQI0lncl2oTs2sm1zKJKUxSHom-d58aUawyrZp0vMqilVi97lKRYc7to89MAXTg8tFpX5_FRaSlTjv6nIBKkyD6uPtqKemnUgGk0S7UPi2F3dGehTinMFdUy4wBnKPdoMJZ2XDxQ7MCMZDUMZ14UVLuxo4sUAnPsbjgslM5VUPq_aK1dsMeHHBFhP1MXy6QrOhXzqS8jjdnxk8q9v-kimHcnbi4b0_6SHRwEoNM5xuHadfGhKjZ7HMkqDjKX7DFVaRHP7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=c3NfCeioKHalGJCxL058pukgiIwaOnefIUtkdXjJDShXCH67fR4PlmKxjT2xhuJ8CvQ127JqUPWrBfs1CQI0lncl2oTs2sm1zKJKUxSHom-d58aUawyrZp0vMqilVi97lKRYc7to89MAXTg8tFpX5_FRaSlTjv6nIBKkyD6uPtqKemnUgGk0S7UPi2F3dGehTinMFdUy4wBnKPdoMJZ2XDxQ7MCMZDUMZ14UVLuxo4sUAnPsbjgslM5VUPq_aK1dsMeHHBFhP1MXy6QrOhXzqS8jjdnxk8q9v-kimHcnbi4b0_6SHRwEoNM5xuHadfGhKjZ7HMkqDjKX7DFVaRHP7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWO5lmjai1Wb7fWYHB6mRwaVYWGd9MksiloW7hEArnElrSL0cYsPuomA2jDQePKbLi0NvbfwiPb-WxoqZPV62L1Pay53YmfrXZNQO6pfGZKQecZEdPlq3400xBlmZnV2cwPJcOEJEE7fXELCjo6pDkx7X3Eq2XFtUCGAEs00kE5IXVIs18izN7ucWRdudPqL3euoq3R1Rd1REpZHOWb6Vy7tFVWnGu6UT2i8JbmquAg8L3KXf4LO9nem5ZUfjDyaOPc5SH9K7OJYH6k1hqrklZ7aYW-V2NX2HHqmUG6zR21SOJm1Tlj7cjnwsgfQ30r80QMqifY844dBWTzKC1MjFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaUdBCZUVPDmdboSI-v6biMcVZmNEOmspriTJB3Zs0qksXafsiINeqdo68gAxbx6pIKo7icloVbXivk31F3B_K10UVwDFcxUfjX4YhPzWJRKVbUe7GETNKnCKYaOxPxBgeloD08rs9i0tRtNgXqpCQHiTw_sy2u1m0aoOtCrpcACwHiJvM6MUMiFPFno1msUAejtUHEHzsvUD0IKV4TfDjbAyasH9i6XgSbpGhFfra0Tl2Z_ptCleDZ2_U4ngCeyk7bMuhbjbki4yJa-bU1yyvyN3_Hqh5_ZQRtn3jfV0BYPqWHweOlL2_4WtCV7UW_krejHtxsfOBSMB2dMFt6hrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCcHVYUwj7OR4XhbWu0qbfGfICUa20gVxy4gwOsI-VgBefQcvhSCXwZLrf5P58xwgCe92mV4XNh7Pq5AV4aDJ3q3rLpn55kbr1_M4Di6LJ4mSbFdhq_Yh_UrkJysKanC6gD2tvyxByT20kmEoeHhQBri6arPAYjiFuxPCED8AYKppH5LpzUQubYf3E0G-xYlNvZu4XS46BbVDPL2AFddh6qiAfxUPcYknxIjRZ0X0R0v6WJiir1AJTn0fz6T8j23UwnsAToZzetjjahA54dKYsp4SEILLjw8fYnasW_v4Don0KnCX_Tru0qzSzzEz4eoBQoVqaMv2l056iuuFKHfiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
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
