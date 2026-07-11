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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 01:10:23</div>
<hr>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuF20fyARGEKCUWi3BNM_a9jOooamRFNPR0rkC4bTEIwC1O5OLccf8jEJCveW_aaaL4rPV7IVqykbQBaDePx6O2w_selBi3s0LUzCY6iS_e0vYW4K_WktYSqd8NLtFs6e1xbec6GgaJdblmuW8QQ2xfT0rgUO_ptyJowHZqohokwT99DtdbKwCKV8zoOfrUWnHm3iF0UYdHDjyU5ZHhQCAhHi0128BlV7_0sc357IiUBjrCPegTkMvPrR20dVBXwYv9xP3koRWGJtR-YvcaUBvF4Hk-iFgnR8k6-zJMZFoBU9eUKsod0cC50dZYIFF-NjaZtRZ9vgjbSphd8I67RFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvig1ayycEUO61gbGKyWPQwWAgtEOIUfc7dj6Uvm8TZGIc-ut-VHA1cGNpDjTZ_GT4inGe5rvqItsMgPqX1UP67NnLkk5_eNMvIc1Tj2WmTL0M6UpW1EcThYla5kK8PAExzocn8pRk-yMknNceJY2yPjjrrW2NagUfO73k1AbIKW0Pk3HFQouvCChpGX6GplhTqiXkcXt62csvBIiRW0X99vVj9H6s4_vNsFAbUILs-CCckIuo8WZ8wCKWOhcC-is2uC283a9dJmWV47SlGkoUo_YdAj_kj987RnHWDMuXJosE0k26QNrBDvzWC9M5H3ZHyUDKn8R7ocAsJ2ynzK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHyP78d_fSmY-vAEqFik2l7ZlkGJy21Sx5I5dXjWixnIxpRpKMQdGkAI1Oq1KSAenwWGwTeB-J37Ym_eptTW1CdqlhbHYgkJxls9JRsQ6XtTkUONkJqS4JY2SPk50aB4rZOLXPUJiFVeAy3u1w6TP0mONF6NlH32w-dKUTKJRoz7VaBhNN7Z95b8cIM9PlEwtvH-zGzX4l1FtoDauqlw_SNW_Xu1nKSHmCoNkqm82SUg5FXs1X_dz-73zty4MuzmLJ-735vEf_LQIWyQ50EBzG63ad77roh1KcQEy0tAt6VCjwrdaVW1OKXmh-XXe-AltoS88ELnyqYCKtTLo7lkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFoTgLRG-08-wXkVfnmUjpyU85d5MEOPeSE2RXukUJ7gcjmFTYlZCb_kpnQL7ZIcAAM_lDv_J4qZLl0hoiuQRaoKA_6j-aoodXfesfc3KLW2-ibWZjxvxqxsCsKOE-w13vSFR6YCpn74DYo1NOBBYyEvAsrIYpZHslnt5ahw7Y8rBD5zD72zEjJb8Xbr82oFCT3fbG_O9-gKukh3C2YomWyaoxAn9HMpLntkpivRZrpZ4r0DzEYp8eqAocUxAJO47HRnA1D8xjLyMZVi-YwcsKo3Qk76hvz83eeZEW9VoL3t6eBs0cX36qSbGuiRA1OhvmzravFHMOyi9dx-QJrwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6fj-XikOE_vV6gn_Bc8O6-xIM4wgXc4YypxLCBQshzeZI2ex4bJps45gE5IffGwgyOcFmOIBXpQ5LzCUMaN_tBTveENWfWCKP8xENhazzUOnaFAp2M-41EK7Ymex4ZhS70FmJAmyGgh9BYHdlF6czYGHLcTQPXfB5Pl3iD77I8DjDXJa0sUIEh6zuEi1VR39aXBilQoalJgeV9tVniQdu1Klpw0ZHKxsgfSfFTz0JXsGf25mcyADsfQjrHKuvlh0iIPGCR6LoO9Jd48T7nKZvec_4o_-CsQq9qSzSvN6_jHrdi6Ysi5U9_kDIWzg08jSHPScvB1Yh7KR2t3-wfS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFBHiFZm8fAMSiTqrDXjhuuQLRrHCYW6o6i3gDS1k0IZRWi69pH275dYJ3vncd_qv0LaBLjeuImSWQF4jvOWcLQe_bjIy2ETCKNRCRm6IjzQN6ez-mWRx2eViQOmOkIsHhhRDmBvMb7OM2s3nYUh2jcR6kuCH7JLNzWv7LzEm2bCjc-Hh1IQSPv2vf1f0cnMpoqyCRUJFvcDgAOLeMmnjy3xSSDb4iZEopRc83z6Pm0_4Fd4N0JK7TvOgk4zHjvEnR4Cm8ZqDDYTnUsoLZ5cXuSJvAw12Zp3C_zTQd1nbIhyMPOzx_7LIU2o1Lnph5eoDgoXJZKw0-Dpfdv8lX24fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7R7eylBN0enMjg8hm88svdCf3cEvTZe1oPGwvNTTtuZ_Poo6kWwszZNxkP9YDOoQz8gl3nHRO8iqsKAjKxECVEihOSVEEl19bnMB4Or1sZgboVL2idfgCgTmftnZNtxDR07vFbQkt8ko_JW8wCybvDUROeNKNd_WfR9B3E3enI2VmZTkhxDFpK53KIiTHCrr-soAF3yepX0g3SoEEFFKXNZNABFqyw-NDmHiXUMhgzDCHNyoAYr1ybZjT846oN3TXHDDRPTNpjw1EOJFXYfBzkCjD-jFYgKZnGr6UBMWfag4de-nAyfDQeS5jUZaweFMcSa1QHNKziFtcuiJGIFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJqeGgnUgFsLYEGoF0wjtOZjP2qe_2TP2VRrv97QhG6uTnpybpsTh3HXKgsPeGpT7TMYYMsg38-9U4z4BMNk_8LXPoTRe-rzqkp1cWcai0W2sdfpYvKAMfkTMdCFATiKyAJt5aXrHdmA9pFsjm5nKy4Q_vIzFB8GsHxaHi00LyGzkC3Geehz9yYc0sTLGLNopQz1WU9wEwZiJZXrg5lgw5dqXpQ3g1BYKq-kI9ULJql5MF-pV_zMbQ4z7LPYiCCOMKsdhJGuTHi6A4eOeEL6dS7kszNlZz3O0yckf6_rQjbODb-zn6U34E5CjjgKoauQ7Vf-UpnvUbBzuv4iIry7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsTYX3DBh8sLkAXLHoWd50FP18g8zgnxGK7TdVmwy2M96aKiXVMTRP0XMMXnn0FnLn9R8epW9YUsUX3dUbVjV4JHNdqZTSutcKjrCCL5PvzU_JLdbA4gSn17cx12cIX4MjKXZUXKZfnsMYMA3_4reLGpVkRHsi3IlGxVT6wxkFTLAIkUjug36uPnXDN9xezTUfEbko9JIFbkRHCIecWJr9TIgmV5u6SADKqcP0HnD_Nyl_yvXT9pLvajcdhxkiMzbCGjwLUm1yaLpVWX952xeeLlwhpZaL38QnJMKEGnauoxC_zHP9Z5n2K3jZKibSwa4nlT9KJrWZrf8eae_13jPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SToNkh2f88FuXCRC8_iTbycUeFDynCAZGGX-xNJ_KWKxirVcQCsxoIYbDdUUXjTn1ISR5eX2bmwAzFjNWx042fPg2BKWcU-5_96PpcoO4gOidGiQ_dMS_CzL_rbxGiM_CYP4LodvFOxNf5YHoPC7T9ZGLMMJMVEHxTCKuvSWRPe2WsxMx0EO1SFOpEbTZx2fvEl1WM0HV1tRm0MsskSiOESBZaV0oMuTtxK6ud-gm1LHA_aIh_75pIAMiMD7nWrGaakatgJiv99GSwjceG73nf2FKR59fYXQKLsR-QBjqjVbrT9lWiNGO98r_GvsGiDKua-yIM0PnNF1ouRjxZ-A_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cckh-0JGHdCGOdzULPBzpQrKI60a72OEB0g2d1sGa5U5B6ak2yK4jCR0ZlssP1kWa6UaOjX34HtyNDS_bb0_SsfcKoTshpCQDCHTS4zEVcVVlJ7MuBb_uOIaNVCa1Msv7sp10wmwOCnhViZhnvTzRbfCLmYFdck4cF0poquZ9qzzvRd1YteQGKsxUOVJsWCM5eW54_jE3RtilEaxlBDJdCno47EpUC8SS1UFy1xCsmoCQZO6M3-E7n3hFJA5Imz6lOaTGsvkEdverMN70uLBq_xhLVmbkuYBWfNwVamY-TxIZX34Y70_DAyweQumZNam7sXpgaGU28piySdHn--FUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RX7G0tm9OgAMMgghPMchtv6npfFOGVPj3Abys9zvyBowVeZ0XrgaHhqx6OY2CreX3tMsN9dsyqRrxaFVSnf9jHkidq6nHk2828tIcaOZdAylDeCoQ53XmyRg6EG_Mxxrn56GgGCLZrsJ8CNlrXau2edmQVBG7aMS5cUr6O3_qfwsowYxAhNXUpg2pUFQwhMBsiLKgQ_djXYerOdS_rWQosReA9jarjSy9SSATHKqdZu_2gFjGpfTgLMYFSA50dBQeheIWIrZehO4ofbM-cFADQCf3juBwsWHhE6mbwT5pnMakzLUzaJFx0g4MMLengL4K9x_zk72RNqRaQjXg_4gtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUfXQISWPM17tZsDFbKHJt1qtjDlFBELXfZTcfgBWvXWDfbs6x5L-QMjt-QjBqrUjTWDXFqWmMEUa_0P-lR97hCIo7IjPrUFDBEMXEH61FjIYWa3U-ajB6N4kEauNPNOBLQsA5XkQVj9P609QkvmTT_O0pYkqzNzJVeKanzXGSHa7zE6tvz4Q6a6hlNUX64Uz1HNj-9toemf7BCT-V1dFGXx1eTkT2jy0377j57DWRMzDhh62n9_zo_kZ2yXg_1uEOoQ08TGgCjSlJVXGjIl9_GSDjyVaqRbKnrH_-Zc8esJ0S-EiLsy39kVQSRbrWWoXjPn8QWuWgBVzXsARU5Dfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7QDiA3fUlJg7m-ZYArCtSVB2mdNIsEWQMciYUXSxvnhkl-xxygZ6MoT7tcir-8cZtxh30grJsLAqYXNzrRg7O4aNhDdIXX3MZgZol6U5dDFNo8jSPZeQIgzz3ztSi7jSw-bREeKK57cRCLAvBFf9RarFXo6Ck9_0fSOqT9yBjdyT5kdd2wBDsFuOucoNzCMjnh-YncSJCUwoFMgf9bbw--ThWM_3XKcDYl47VHE8dHzfrD_Iei8TaHKRUyDswOfQN7tg5MEFx4BWLmsNbr3xLi07kcsmo0hrcFgQCuWc5lN61wgth_CMu9SuRGmLUU5nnCRWdMaSaO8t6ooyeYWFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ChVeHkNVkrHaUtxd0HkhoFPFoMh4nqvXmOnX1K13RWCkhcuBIYxwNqh5x8tsFrDA6wRAI8ZZd_T2y4Tk4QVD1G-tGP6Jkw4MgkS-_ns5TsGuOuTkHPaFalMieFIRoyJjCcAi3KWLEgMIPDl02e5abv_H-Son_xZepAvqLGdnZar1PiWWqC91YTWOIayw_T0hrGnpAUpGKcaqcmYSOiMiSUSAl944s07jHXnzWMXEUuMJJ3sWXAlatdG5l4GcyEbr6g6lH1htJJxELgJNSHvx07OcKzjFFV9Bjwaq_jK9a6ovLUGxeEyt-LQFywZZ_1WxCn8GFdcsa49mdI6-IUeebQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=QpW843savi9WuBNKuyxz1-so1ncnIiavRSfjxgl0FILH7gpzknCLIdmUtovA664Q4jSL6ZNF0OAR_AL4HwMcbf90x4NsXliAxLDFC2eYtW_VgHHpG7LI8coPCTC1ndMRcrCWhP_0S_k2btnleOq1SGOz6Ka8vky_XkOGpmXRikYLuR3Pp2sAufoEm7dgmSG0T4v_23GA60zDa3wUyQzVLRXk_Mfv7LviVsxo7wxlCN8t2ll6LS8lQRWDW3enG4h-q3F-kSQuUic_dbkUUD1iUZBK7jfq6G2pM-MZjXSTyey1juID7GihDfpcybIDZ7RW8tX_wGtzUndWx_IZdzAbwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=QpW843savi9WuBNKuyxz1-so1ncnIiavRSfjxgl0FILH7gpzknCLIdmUtovA664Q4jSL6ZNF0OAR_AL4HwMcbf90x4NsXliAxLDFC2eYtW_VgHHpG7LI8coPCTC1ndMRcrCWhP_0S_k2btnleOq1SGOz6Ka8vky_XkOGpmXRikYLuR3Pp2sAufoEm7dgmSG0T4v_23GA60zDa3wUyQzVLRXk_Mfv7LviVsxo7wxlCN8t2ll6LS8lQRWDW3enG4h-q3F-kSQuUic_dbkUUD1iUZBK7jfq6G2pM-MZjXSTyey1juID7GihDfpcybIDZ7RW8tX_wGtzUndWx_IZdzAbwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=Qh4g4L1_YzCw9FtxEahWjb2wU9ydUA3b387YXbu2T-AtDK2ARH85NDHkpmwxqBbNrn_g0mXQ_O_5SQXYBymNoBHwfmnztr0r0apvfC54UdFOL8X1vb-mNcmxiAom9EKGKV7DtsL3Qg_ktSFYhoNunYfqV83RfnF639B-PtMXibfG0oy5C-I580OixvhtBWrfTmkUMMtja8aUulhOeJNinv4A4TKtXgazXzD1fFeHMY4lxwn1rVlG-ZB17bGv3GUHyc9yxLDt7QTRqq8yG1fzb3o5kK5JmlYSf3VJJDpaMhueD1P3yfZA9TQ-yA_KdpbcqBHIsRjT6MB6Y5qWOHTi8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=Qh4g4L1_YzCw9FtxEahWjb2wU9ydUA3b387YXbu2T-AtDK2ARH85NDHkpmwxqBbNrn_g0mXQ_O_5SQXYBymNoBHwfmnztr0r0apvfC54UdFOL8X1vb-mNcmxiAom9EKGKV7DtsL3Qg_ktSFYhoNunYfqV83RfnF639B-PtMXibfG0oy5C-I580OixvhtBWrfTmkUMMtja8aUulhOeJNinv4A4TKtXgazXzD1fFeHMY4lxwn1rVlG-ZB17bGv3GUHyc9yxLDt7QTRqq8yG1fzb3o5kK5JmlYSf3VJJDpaMhueD1P3yfZA9TQ-yA_KdpbcqBHIsRjT6MB6Y5qWOHTi8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfieKdkEppQPzigMMzYM2vkzOPQv7M5sHfMSgbxsx1e2W4VFrtP2kZI48s5EAsRUcqV-qfnDysUZNWrCK2J_akhl9SEcQiz-W929FvQ1Q2gZzDgr7hmtZ-xEsJqVP_jqblUTJyCONuutPHZqAQdMc2vemlxF2lZ4Q2FcRf3YZNOxAiNQ_2brVjMex0LkVY5L9Btc8J38Su6j9oVH02wL5ggsdyDJzgyzgvZPwhwWyTw7m6A0FIAPl2Y2nG7lIPRcbCRHVh-oJcqDYSYN89VSf431XmPCEC4Lz-kTm1lCGZfyDeOSbB6uLMsbIvNiYK6QayfORJOpHdI60rozq9w8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gdns3yb6_EB7oAQV96MVV4AkoXPNQtyLnlwFaVeD0HAH8PzHq5rOhgLXsIl3N1jCgTRaWDMWwZsdGNi9RtJs_85QcC-aKDyEtXaEyfh1lBwBBYn6IiIokQ3E7C2GWSCB_cPy-JkaOR1-pHIhcKboRqF0tIOY7KXc7mU0cXtTURjSwUSgg46x0fv3pMkD3nliyt4yTIUrOfElTrVDuSYUSVtBkSZHLLECIO4z7bDgtfb-RHqWUX3tXfiioMVvKWxTvNofwPeS_gZ1D8Q22wFy_aTomAwKOaqh_jyQNg5YvIAKb2Mn9XjMX3bi0J8QS26rKCmGbsu9tHnKNqk5VXMksA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=AkWDGMx1EAYNHIegI5eAai-edbKzajkAsumVnLv-SppzwvKjc8Lyikv9Cvx7miDjZhyQMAvUAp-f1szRvVyhfrteVA_FgUgooyc_zDXlIRH5_ScpVaxoZjraXwvXcCV2Oqq3_HZtHHy-I6eFjmDHp0yifkPHeEXX3AbBx0RVVkiKVw9wWPZfdJiMke-tUgPyid3LRja93qsgc5dzGBqOoIn2yz0jy0GKBzYRpfO6eLUKpDxllGlQhDKHeRxvG8KdHv9xzShkWrVePtQETVneN0T3r_SYVa6L95N19r1OrXZSM7AVwNYR0YtFBArJNmCWRUcdDcfnNLl8LHiJa1pS6o9m6HL_W-FlVXZjNkcLO7F4s_RfA15Q6gjvyZBaWDpQcDjHpNE36CidWN8njWmyepXzAmSGmjUb1VGXWbD-G322jCFpOa9avl0DH9agoB_aWPyqMqje6OLyQUkGPV-OHFrd5ZNw2Mb9mCeIG_rvoF17yO5cobDv-rQGX1wLmxGvaD6uD5Le6rAW8O669Cha1lSsobmpGhlCNNth_OK1OVG7h4uKBGeq109a5lGwG31O_CBaW06IGPvJBvA37K0gBEq_izlzP_5MsH7U0-vfvOrbgIYQGvdqDl3BhSaZCpdbbLt-AUiwTqpknVEzERtloDTD9jv01-TBS7D9oi1-Ygg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=AkWDGMx1EAYNHIegI5eAai-edbKzajkAsumVnLv-SppzwvKjc8Lyikv9Cvx7miDjZhyQMAvUAp-f1szRvVyhfrteVA_FgUgooyc_zDXlIRH5_ScpVaxoZjraXwvXcCV2Oqq3_HZtHHy-I6eFjmDHp0yifkPHeEXX3AbBx0RVVkiKVw9wWPZfdJiMke-tUgPyid3LRja93qsgc5dzGBqOoIn2yz0jy0GKBzYRpfO6eLUKpDxllGlQhDKHeRxvG8KdHv9xzShkWrVePtQETVneN0T3r_SYVa6L95N19r1OrXZSM7AVwNYR0YtFBArJNmCWRUcdDcfnNLl8LHiJa1pS6o9m6HL_W-FlVXZjNkcLO7F4s_RfA15Q6gjvyZBaWDpQcDjHpNE36CidWN8njWmyepXzAmSGmjUb1VGXWbD-G322jCFpOa9avl0DH9agoB_aWPyqMqje6OLyQUkGPV-OHFrd5ZNw2Mb9mCeIG_rvoF17yO5cobDv-rQGX1wLmxGvaD6uD5Le6rAW8O669Cha1lSsobmpGhlCNNth_OK1OVG7h4uKBGeq109a5lGwG31O_CBaW06IGPvJBvA37K0gBEq_izlzP_5MsH7U0-vfvOrbgIYQGvdqDl3BhSaZCpdbbLt-AUiwTqpknVEzERtloDTD9jv01-TBS7D9oi1-Ygg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGv3dsrJEIve0hK9zpXQNepKRXBfXz4ZkxU0rLPCT6S9KrunUosjvBSzcLA43aXgrHBkL3cFrQKORT6D6RZLjR4Z4PUfX0rqIMWKau9qKtceWr2kLQDIG3R5zZmzsQ7EqWwkA95JZ-7JQghOCS7dfGhGekzc5qhg-46xpPV1-njMrWJQOT1TJkYPYrPdKLmVoBlCD6zUDuuGXUIee_67NWUpki49bWSxj4-B2So5jOwvAGAsqyUnjJnBjlJgRUuRdC8gy9SUZS7ovtr3TGAiYOkx0UaJAd_Flaq5cJGUF-nIMJJfsOebJVCnF5kWVeGLp8Zz42uIjmYmo2lqNd48pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7Ay1qY7Cek5tuFsHSrYxZmLLEnVJXr4l9hONkTEg9snExJatIMO-8roYSf_iZPSmnladRcpqxzmNGIecxbd2IQ02MZyVsPItRKMe2ttHaGq_M6DiAaNgWsXIO-WyJ03qvsXu_wsaTgtZIlUQzasI2MdN-7OD7-BaCIyy8cxjy1mZkHhLX_lxGVW94wUYQNMxdO15vaXSrd1DxUNtmtmENHqgejgKSVbtDQVmNJo20zGL3tfis4gw9R7H8lZtSiwyG7aFqcv_pTIi60XCQWN8DMQm4Q_a_ReNS3b4qahxJV9UHqlsXSBX3dHTMqwqQnMjydjz_2IbO6AAVPTJj9CWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=nrOsawZZuRa12KL7mh2cJnSE4z-iOqjJAd_w6S1cqozOq1fJZXS6Q2jo6biqrPH3mVl1QXEqMrILGc6V4P-6PimwZaXsj0tr0n4NL-HCYl7kooQfTRCw-1qqvLvqVIfuwueR_l-N8oWysarWja0j-va22mgCPBEPUGtiVI953VENWmmpK4sVg2OzENjG2KC9zcGUWYIrd1cnrJ0H3tZzalUGNlbOIAZxjHkB32WEw-6ug8kMq6XW-Xm6lvgv9tybWSeNwl8rXuNwp99qfLmxglBGsRfH3MSHvBclIZ4BHE8aBLyJn3DhBVg_8ak-o6lPZhFJ5TAHcubqMhdCIpVe6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=nrOsawZZuRa12KL7mh2cJnSE4z-iOqjJAd_w6S1cqozOq1fJZXS6Q2jo6biqrPH3mVl1QXEqMrILGc6V4P-6PimwZaXsj0tr0n4NL-HCYl7kooQfTRCw-1qqvLvqVIfuwueR_l-N8oWysarWja0j-va22mgCPBEPUGtiVI953VENWmmpK4sVg2OzENjG2KC9zcGUWYIrd1cnrJ0H3tZzalUGNlbOIAZxjHkB32WEw-6ug8kMq6XW-Xm6lvgv9tybWSeNwl8rXuNwp99qfLmxglBGsRfH3MSHvBclIZ4BHE8aBLyJn3DhBVg_8ak-o6lPZhFJ5TAHcubqMhdCIpVe6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRw2q6AwJiTl8ijuEnuPB3OznfPWWEHUjWYuX33Bxr87pvGdsSxYRF9XprU_I-hPd0kU-wO97Ec6vzrtP_kIJBmWSagf5vUupBKW8uzOKtIEPHpDIFSwdmQxnUsW-Q4WY5mWMcz0KPbuA2d-UNESH4gK2lne97giORcQ3I17ID8t6eatrro5Tqt5tMBnv9CcFekXgrWxn0R-1R6TWn5gWN2zOga89kKkXpwYC9NTXa21sdSHddq17HrzeItVAMOHRQBQP-aamWZp8kUyu5TySpP90cok88qI1LeKqklzh-HWaMgw6W246LRvlzkPBukfbSCKHGcO8hLnO7SnX7kGBQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=Eee26SJWAngc-yfN3Bi3cop2OWQrTeQxlPFAqxXB6Qz77QByY1jKs_J52AywCmliUmmz8mvfbH7mCkYBcbVndEgcI48b9P6P0lsMxosbNHArGSLUyASVSRPIKw1L9IO13P8GHpbhLhouWM92glY4d-GGL4Px6gfGlNGErVPdbCxolxip5mZL1iYIE6XOWMZX4HmDvww1HPtKQQVfnt3sGaTd3fJF0j049SUJGWug8H47g112TKmCfMQwk7fkiJnFnH7aDOlDtZYpW8rsBVzFBBbCtWH27ZGupymBRbkpWUiIWT0SVqCFtagfTceNjAHpV354f2R3VCGHZaSU7cQV3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=Eee26SJWAngc-yfN3Bi3cop2OWQrTeQxlPFAqxXB6Qz77QByY1jKs_J52AywCmliUmmz8mvfbH7mCkYBcbVndEgcI48b9P6P0lsMxosbNHArGSLUyASVSRPIKw1L9IO13P8GHpbhLhouWM92glY4d-GGL4Px6gfGlNGErVPdbCxolxip5mZL1iYIE6XOWMZX4HmDvww1HPtKQQVfnt3sGaTd3fJF0j049SUJGWug8H47g112TKmCfMQwk7fkiJnFnH7aDOlDtZYpW8rsBVzFBBbCtWH27ZGupymBRbkpWUiIWT0SVqCFtagfTceNjAHpV354f2R3VCGHZaSU7cQV3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIv7NCKFrWAOtvKOUKgDjirwQFcc-Oj0PGAORck6RqrOSFlQMI45hAHhEDZxtNeNakJ8RCpGKFzhbjkQleEz253j7oBFAW2sWFx9Md2CNBr7Ig5L9jrG35tCEkCI4YnUiPAB09LSnbVlT2f_MVmB6lvvgHc0zXbwABXQABQ4URRMl8ku74s7mjqiKL2IjN6kVHu5FUTF9D_EVOCGnA36T9Gcn19DEQIgAid7WoicgZwRI_yQTeXOucF5Py25u-KjS-e7Xm4MNbfvjujWZx9P-IBdH9yZT_h3AlDopkdLBrjBHpQTTovc0lY4axbnlSTGw8VAgH14k4zwCbPOYX6VIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpOEflTnpKrO0vZN9wOnbbAGkCEJpQeswh_vbSkbXHFguC2mWcgWkiWLYCHw3QmXhEqtXR1OD1vJ3442UiDeRwBG8Fu3yFGiVJwj7I-Uw-n0HzNxmfYuspO3pEfdaTouXN_WVW932i4Xfe6bng9Io44oATsmA3Ao6pCcAILbCoFB9c8P7TzFSAPVkY_FUnFuvGD1Zybt-UWHqyrEz2PAr9arqq9_xCswjLch8hyY_l8UrWNgZ1LPC2ym1nKSTZCvBYvNB95Ajl2z48aZWJFoTW8H_D-arJZ_33x2sBP19E3dqNO1HtLQ7SrJGjZwsuwHyxf2cFUQtnvrM76GoYummA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=rqtaX6Rl277rXbIHg6KhrHR9lTM3RFxg_0ySLG9poznsK7tJglude2KkP51ufvz72bPfrCLT_UJS5LarngKITGecT-SoC_0A8uP_fV_5_JqyHuZNXaAtyZrpP3YokqOlE9dLiJ4tyJ-PGjHk_adUb5T_0op0jDmq-SzVDQ-kEiRofej6QPBGxiEQ7D-X8IQAEkN1bDJa5UPik1FfzaaV4ZTpUZGIEisoTm35zVV8wtnKstWggYDznvOG1IAY_AHQFHImtGxiImelBDbPDpQF_KnL6TjBp9upsVcFrXt09YShLHsn6BGXGumJg5ZDyHw6-wBnzeuCYTX5QsBVGnZdmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=rqtaX6Rl277rXbIHg6KhrHR9lTM3RFxg_0ySLG9poznsK7tJglude2KkP51ufvz72bPfrCLT_UJS5LarngKITGecT-SoC_0A8uP_fV_5_JqyHuZNXaAtyZrpP3YokqOlE9dLiJ4tyJ-PGjHk_adUb5T_0op0jDmq-SzVDQ-kEiRofej6QPBGxiEQ7D-X8IQAEkN1bDJa5UPik1FfzaaV4ZTpUZGIEisoTm35zVV8wtnKstWggYDznvOG1IAY_AHQFHImtGxiImelBDbPDpQF_KnL6TjBp9upsVcFrXt09YShLHsn6BGXGumJg5ZDyHw6-wBnzeuCYTX5QsBVGnZdmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=Xq2iur0xJjfZ73IOp0_zLgyLeeOca67E2OI3MSp5GAF1SoVG9zMsjzVc_LSUqheLR04ondG9CZhVL2i0xsbOio2XtAVrM01_C9WAaXFT1lytVp7rifl4LFV15PlIiPDSUh3xUMNKUKfC5z5ZX_bs7YD8Ic3ck2bRL3Ily94sbEiBfkUlpP2fzeLZzJ7E-mrjXk8mKmqDHrW3B-EquF152zNmAjNPOzV72fRVWY2ImMmdH1ABUvAXKjf1WWWouTrc4VDSeM1Qxi991rwnaHSx7XDyA1KYGscWNdT-Q1v2L-5bU2Lzzd2WKYedDU8mrhZp7zTCuC2vW5RzjTPG1Myccw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=Xq2iur0xJjfZ73IOp0_zLgyLeeOca67E2OI3MSp5GAF1SoVG9zMsjzVc_LSUqheLR04ondG9CZhVL2i0xsbOio2XtAVrM01_C9WAaXFT1lytVp7rifl4LFV15PlIiPDSUh3xUMNKUKfC5z5ZX_bs7YD8Ic3ck2bRL3Ily94sbEiBfkUlpP2fzeLZzJ7E-mrjXk8mKmqDHrW3B-EquF152zNmAjNPOzV72fRVWY2ImMmdH1ABUvAXKjf1WWWouTrc4VDSeM1Qxi991rwnaHSx7XDyA1KYGscWNdT-Q1v2L-5bU2Lzzd2WKYedDU8mrhZp7zTCuC2vW5RzjTPG1Myccw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=im-hXc6SFxfEdVVX6Uvg26rkn9WrDAWjmYcyd8rneqj1Zsa9UODlgnXc1FxUFjurfLnlUNLhMbYsjBnFF432wxHZgZyX4kVJ9F_55-X1RzFRlkKERcHAkx8sNOGkIizVNHsq273gwzmMM2CcJaDLiXsO2cGm1mfaQ3YgZqT7MSfXJedz9QUcwWQwjs8GlpdNF3vkcK8ir1KpzY5r9N_-wlamPWnr6uI18Qes6uSWw3XMeCj80RGmb1d-ApUHe7AfhF0vY4jI0IJO2WXGRGdpUteQrySkKtQej8ohkcxClqHgvFeKav7aMrzddfrCZ_W0CB7vD4xGoWUlXuKe-RaBGDkSLRG5oWKYLsCup9IlKzVdKRICbYFTH3vpxXsYRpEkmte5veJXXYO3SWYVXY92UeWLmn1_Iq3APM6hBLUoXX4bXCpUA79UwyH4IbZuxrfKjOLYv-T2pP9ayK33as2QP0zNT3P6JZ3ZHCPecmw_K7N5twhlv7cksLX898wTzaBjz-eQlzgfjqe4dN-Js4-mwdRVsKusgoQqcL1Fc-CVby9NnUcjak10VyNrSUKy2UVUNL1o-kfyHi8c5vmyEKz-VM0kKdIaZaErOWcr91p87JvNnTTpOebZXo0w4S_GjIX0k9x0xGKUxmOh_N0kBzd15WXEZ9LLycm24voPpiFlQC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=im-hXc6SFxfEdVVX6Uvg26rkn9WrDAWjmYcyd8rneqj1Zsa9UODlgnXc1FxUFjurfLnlUNLhMbYsjBnFF432wxHZgZyX4kVJ9F_55-X1RzFRlkKERcHAkx8sNOGkIizVNHsq273gwzmMM2CcJaDLiXsO2cGm1mfaQ3YgZqT7MSfXJedz9QUcwWQwjs8GlpdNF3vkcK8ir1KpzY5r9N_-wlamPWnr6uI18Qes6uSWw3XMeCj80RGmb1d-ApUHe7AfhF0vY4jI0IJO2WXGRGdpUteQrySkKtQej8ohkcxClqHgvFeKav7aMrzddfrCZ_W0CB7vD4xGoWUlXuKe-RaBGDkSLRG5oWKYLsCup9IlKzVdKRICbYFTH3vpxXsYRpEkmte5veJXXYO3SWYVXY92UeWLmn1_Iq3APM6hBLUoXX4bXCpUA79UwyH4IbZuxrfKjOLYv-T2pP9ayK33as2QP0zNT3P6JZ3ZHCPecmw_K7N5twhlv7cksLX898wTzaBjz-eQlzgfjqe4dN-Js4-mwdRVsKusgoQqcL1Fc-CVby9NnUcjak10VyNrSUKy2UVUNL1o-kfyHi8c5vmyEKz-VM0kKdIaZaErOWcr91p87JvNnTTpOebZXo0w4S_GjIX0k9x0xGKUxmOh_N0kBzd15WXEZ9LLycm24voPpiFlQC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHQ-Z3mw3LOFgPl7ulkbEAPNETJZv5a2tDh9o0EtU972jZm-nyNI-uh5AL_M4ALyP09wwhENQeNTrDhCRyKtj8ThYhllNtTsL3UfwhewwYRKUdbk6F-7nKAg09TpwbSMKUsgW-GQlCNHNPpPtIlCsMJ6jIMVzMJ6tWOCHVtNdcjOQ2YX5fQcIt2xLrlN_qj9eC-0hrt6mzeBZmq91P7Af_ZuYx4mpKVvmAzGi8AxZWN3Ch60AWrWTvD_CdbRLmkluN7IkoripNyKKV11DDzSc5yuMR8pda5yISJGls8CDOQn5sTMf_vhA__IJ7PxqSJ2aMcjFSxsFTc79OAv2Vw2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9_cHcfJHxCf0u8HikwR0nO71axgsMEWQEE8Yi5jp4G-g0tSKgu1SQ2tntntue2R5L_N_qHTllAImjZZJV8eT51x7GzgLIm7Lz70KoJzLEeBq_ot8EwdAHLnqlhaaeou7MDZJ2DdZqOAytq-Ug9mwIFgw3Ea_8iBsbKAguCLijjwa9abePuTGssEhq2Qj3jN4ft8lV4ykp5ulnqikndHZ5NChjzGw8exFP6kSM8Ks-OIppXbuumxvBRf1kslwxiLRgUr4awa7yN9HexR33fmMC-4yJ6KH-YkBATPpSi-gTd4VtaLgn4Eh0N3N7zrQIkswXyVq5AiAY7E6KBP7iRsWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnCH3hOx-Rc6mZ__A53taAIxE9gZpJ7fSYxyX5CPGhIei0_x7OONakBCTQA4TllmhBPH0XKAK08AxSaQsHy6pqfAk_7RB15yUKscIbmhvSbmh6g1Z5Ies8bFW4CSMxuy0oJRg_XoeuU6R-kqTiy_GvioUv7zCia_7Nq7fnNiRpmfLq4IJYcRk8miUgMnYftUhb2MdqhqbWtE_lQlXuvmw1uv5a1dW_zhv8k5nJ3RbzL_C5TMQsEJON1MTyScD-lHfUQ7Am67YDNP98zsS_yiiTVx8W49HgjvnqC4OGEpwo_iTjRcncS81I7p0GIN9ww00A-wEztPg1XekFYvEuVN_g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=IFQaYZI4MmmKG9ZiKY1ydV9zKJ6m0iMG2e3ZTpEfSEbcDw_XiZ0057MXneCtY0Nh-hekWP9s_1t2AB3G-2TLf-bwqFd04EpI1bN8hvaR1lBlxmdv9yArYPQ-0IEkMASKwJCMXcY4Gpz5Qt_TLVo_NFC9zJjQQZTC2cVCmi9cLwm9bIBekDe-IKGY2JLAXzFcHsK7A-_gVznbxoDYgffZVsfR5vZIusqQ-PfX2HT1no7TJ4g6rLBtGPGoZT3RoqElhR5l0OdGUetWaYqaeiW4qTBjIK-Yd6GbBelvS57yqeJBkPHb2VJg9F6pW5Zdfn7pvNTuQOftf7UUTjLqvYazgDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=IFQaYZI4MmmKG9ZiKY1ydV9zKJ6m0iMG2e3ZTpEfSEbcDw_XiZ0057MXneCtY0Nh-hekWP9s_1t2AB3G-2TLf-bwqFd04EpI1bN8hvaR1lBlxmdv9yArYPQ-0IEkMASKwJCMXcY4Gpz5Qt_TLVo_NFC9zJjQQZTC2cVCmi9cLwm9bIBekDe-IKGY2JLAXzFcHsK7A-_gVznbxoDYgffZVsfR5vZIusqQ-PfX2HT1no7TJ4g6rLBtGPGoZT3RoqElhR5l0OdGUetWaYqaeiW4qTBjIK-Yd6GbBelvS57yqeJBkPHb2VJg9F6pW5Zdfn7pvNTuQOftf7UUTjLqvYazgDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=p5EsmtGx7_yFnxiLjv7uCj0VpDEAgFCtuW3wzo1L0cP7VESLbQ_xWFIAFE93NciStFTsjuXuEDvKYktEGP4hq493WAUREBNYJfjw1U1Ry4t36YcJ6fAdm9mB8pTQ_Qot6b4cobhYHhWRHxUun1XIRTt4b8KsiaQRwlngnN1W-C7YG1HhNth8911c6J4r_2Xv4jU0f2e7BR0ZlDY2BkJDF9tg_oTuB4V_bJiEJ6GCWXPyOQxvETh4GlzhuJaGWDS_ZatRpiaWMtjUjOo6_iuRAP-WiP_DjOV5Q4UtErivMtTscbl626U7aVFHBGsB0koXTBUK7QbEOzJXwbJizqsb0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=p5EsmtGx7_yFnxiLjv7uCj0VpDEAgFCtuW3wzo1L0cP7VESLbQ_xWFIAFE93NciStFTsjuXuEDvKYktEGP4hq493WAUREBNYJfjw1U1Ry4t36YcJ6fAdm9mB8pTQ_Qot6b4cobhYHhWRHxUun1XIRTt4b8KsiaQRwlngnN1W-C7YG1HhNth8911c6J4r_2Xv4jU0f2e7BR0ZlDY2BkJDF9tg_oTuB4V_bJiEJ6GCWXPyOQxvETh4GlzhuJaGWDS_ZatRpiaWMtjUjOo6_iuRAP-WiP_DjOV5Q4UtErivMtTscbl626U7aVFHBGsB0koXTBUK7QbEOzJXwbJizqsb0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=QbHVW1MXQXkdyjZo9dxDOH353WjCZNvGmZ56H8L5aB9KTlOm19qWnnYXArKu25A6sWrutwm0dkkrAjldZL6jptlphhyn_nyw8vexJ8xb9fWP1llFBUXKiu-6ivVAAGpPrWVMfNKCza0z-LBhLo0Db-CiQiTWhjSbhMdWcdtkiW2bgc5a6rmI51q5imBlPiL0aS7UZ4YT1BVJncmmkjGXHsZsoNImPyE7mZWqMlDYer973KmmzO2tN7pha9j90qKEkMwtj4V8yHwyXbJ3vCV-n-ceaQlCN7Y-WitcQLvat8FnkrYjHKIgAkv2UXYeTyi-Mm8VnLfqWXLyPYxesXwHkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=QbHVW1MXQXkdyjZo9dxDOH353WjCZNvGmZ56H8L5aB9KTlOm19qWnnYXArKu25A6sWrutwm0dkkrAjldZL6jptlphhyn_nyw8vexJ8xb9fWP1llFBUXKiu-6ivVAAGpPrWVMfNKCza0z-LBhLo0Db-CiQiTWhjSbhMdWcdtkiW2bgc5a6rmI51q5imBlPiL0aS7UZ4YT1BVJncmmkjGXHsZsoNImPyE7mZWqMlDYer973KmmzO2tN7pha9j90qKEkMwtj4V8yHwyXbJ3vCV-n-ceaQlCN7Y-WitcQLvat8FnkrYjHKIgAkv2UXYeTyi-Mm8VnLfqWXLyPYxesXwHkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=fHvJRmxd0nV7l08cippFNPGhJnHTfZneBiFbKW55wzZHmnqB0-QImhKl-oRY1pwP6wN48-VrndeQxRoUy95qRyBbe2COXR5W5q5sdciD7mJva_3RiM4f1C-XIFbftGjXOD82TTTrVpFqjWD9ITG4RwtNPkPnuSKgMpekcPBT_EhmDUdIVnYuGOhuYVVRqMYDbQe3k29esBt9tHkZeQhLVGst_Fet0VzyeN_nkrFYTcO9pdh9_2KhmPImJjSHy2tqqMOGGJwNoqwSEOhGAVc2pywHG_qQW5ySdVfZJ0KiH-bQhgSctwqHumhy8nRH-XVqWQc1G2m2YCP-n_n9XXAKWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=fHvJRmxd0nV7l08cippFNPGhJnHTfZneBiFbKW55wzZHmnqB0-QImhKl-oRY1pwP6wN48-VrndeQxRoUy95qRyBbe2COXR5W5q5sdciD7mJva_3RiM4f1C-XIFbftGjXOD82TTTrVpFqjWD9ITG4RwtNPkPnuSKgMpekcPBT_EhmDUdIVnYuGOhuYVVRqMYDbQe3k29esBt9tHkZeQhLVGst_Fet0VzyeN_nkrFYTcO9pdh9_2KhmPImJjSHy2tqqMOGGJwNoqwSEOhGAVc2pywHG_qQW5ySdVfZJ0KiH-bQhgSctwqHumhy8nRH-XVqWQc1G2m2YCP-n_n9XXAKWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsfiUD5qdxVd447MiYojN4XaRQaGFBQB8jxvud5ibCUvVP1dGUXojvyzixp9Ecn4BTNDHzdDsup7a_D42AxfvqWsZyd7niZ0rUaqRQpj-ew-sdzeEiz4i5lkxaiRlPcKPHZYcptXmqL4pNoOQQRx2p1ZV3IuU1bHq_SSXQzBGaQYXzDeaneHTSkWCfvSk_qvK5_x-rz3hkad9FNpl-jedy1sfzfi2gNQzWXRZX08QpiSTLe4QLwDqdJmfOOLhT8F6Tj0tWsO78Vmhv3aQz8K4dUib_c2zzvHGH7v2SjqH5rcN5m1H7h0_5YvtvsxR_Ny96wFahtmACmNMT2AJmNxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=lqXcRqm_RDInClxaS84ycYzjuAMZeCWCFuh_3DuBvKL9tguVKqYKJNAqUmNuwmllJIY9U89SLkCUjbf4hPGbaXQyEkEVu4ZcRnhUlkOKGSBi8a1Eo0r6fJA_ykvohPmkvO5bk0p25N3GxL08qMhujsmCj0SXdlQO2mINJuPN6bI83D_GQyRWKi0WMwxSTxdSnlgvq-Gk1dJ9iXl0LAmGG89N-AA41D--imn-p1Eup9UqRLgTM_WvTtZog_xSlYGrfSA3406DJ56IUN3C_972ozuqBmJlCvwq6M2nGfOX5gs-fy0OjUk-WBuLdFY7UL-6pLSVWGLqQudtRNO52JPaJBb2yj1qOMiDsJg8zB3mw0ONL39_tMJcdpGsMSavIghgPXSOjzXVsz_-tTs5cP94OmZ31QXhKcnVlexocYLxXCfE4-ca2oLXIUuy-pIaK5CYhn6_kQJjQVhLCBXsMhEuu-X5ubr-XB2ohb5YKdzxvtSW-iCCqr32XDzUWxox6a_D8aZly4h5qUlLiYs_fTTIUeRFOJ8x69kGhhpFT2iCVQDhPM0pVwmzej3EMMpJr4dpvMuFLeUICIWcriuwpUJ2mInJe3bZ_FKfHFSXS6puFyE00JKtlQC1VPOxJcmqPR6XwK673u92HtAVlmJ5IgMkdz39Uvb4ci0t1MpShFVDYfY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=lqXcRqm_RDInClxaS84ycYzjuAMZeCWCFuh_3DuBvKL9tguVKqYKJNAqUmNuwmllJIY9U89SLkCUjbf4hPGbaXQyEkEVu4ZcRnhUlkOKGSBi8a1Eo0r6fJA_ykvohPmkvO5bk0p25N3GxL08qMhujsmCj0SXdlQO2mINJuPN6bI83D_GQyRWKi0WMwxSTxdSnlgvq-Gk1dJ9iXl0LAmGG89N-AA41D--imn-p1Eup9UqRLgTM_WvTtZog_xSlYGrfSA3406DJ56IUN3C_972ozuqBmJlCvwq6M2nGfOX5gs-fy0OjUk-WBuLdFY7UL-6pLSVWGLqQudtRNO52JPaJBb2yj1qOMiDsJg8zB3mw0ONL39_tMJcdpGsMSavIghgPXSOjzXVsz_-tTs5cP94OmZ31QXhKcnVlexocYLxXCfE4-ca2oLXIUuy-pIaK5CYhn6_kQJjQVhLCBXsMhEuu-X5ubr-XB2ohb5YKdzxvtSW-iCCqr32XDzUWxox6a_D8aZly4h5qUlLiYs_fTTIUeRFOJ8x69kGhhpFT2iCVQDhPM0pVwmzej3EMMpJr4dpvMuFLeUICIWcriuwpUJ2mInJe3bZ_FKfHFSXS6puFyE00JKtlQC1VPOxJcmqPR6XwK673u92HtAVlmJ5IgMkdz39Uvb4ci0t1MpShFVDYfY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=YmiAckGmqOK3juj2P3_AbzQqL0t25wDPITtlLG455aWOqCmf3LRxk2Vht_fv2t0k1rP_UfoehG5-uAlZlV9_JWqpRZ3bLgMEnjJRn5qsg84veLBPMygO6-nOo8wAjjGK2H2Jd8UgdJQ4oRACzlEASUkO2f-LtsRNu56F5qkB1W5JI0gGz11kS9QwSM4y_HzRMuknUHRiT7WA_5IDtgD5uiC6BC7LHiVU-2brlRIXwxMoqHGGaHghQQCUoSZYuf-SA8YvVG1gtavVfugeZ2nShre6dAUoZInkpwz3GAqJVIpTZjUelqGI0mlISduV3uL_ay1N16hue6ZK0ZRXrcBI4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=YmiAckGmqOK3juj2P3_AbzQqL0t25wDPITtlLG455aWOqCmf3LRxk2Vht_fv2t0k1rP_UfoehG5-uAlZlV9_JWqpRZ3bLgMEnjJRn5qsg84veLBPMygO6-nOo8wAjjGK2H2Jd8UgdJQ4oRACzlEASUkO2f-LtsRNu56F5qkB1W5JI0gGz11kS9QwSM4y_HzRMuknUHRiT7WA_5IDtgD5uiC6BC7LHiVU-2brlRIXwxMoqHGGaHghQQCUoSZYuf-SA8YvVG1gtavVfugeZ2nShre6dAUoZInkpwz3GAqJVIpTZjUelqGI0mlISduV3uL_ay1N16hue6ZK0ZRXrcBI4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdIsT8UVCVwsTV13XDAE7CO-zCd2HT0IGxk0pVpM7Oom3i6PUZtkugvyQCQa2RZGbvTzPdqyt0u2R7vtW14mm8gpuwVqKEt08q3pU0MqM8IybH8MSuOH9TyDM5ExiNcRc3EiyQSxpk6vIUrSawZ4fQXJMfam_8HH-roT7WrjkEKConIYlsF-x3CoOdIm77L0oEwQhk8jeriHOGeUkV6MewbLeubMOQxmtVjEtNSvhFzwYCy8DwlLNEgxmKFBe0pPZvxQJgYUaNpEk49WTOL34KbPXAfJvza_KoPswNtamxXUF1UYgZ9PKwdnsuyxT_Nq-Qv1i8JXKV34ev7ZnTkJPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=ZujsD2uy23-Mtr_ziyRUQ3A6OX7sXfap7eDgZhBxzPQKv85I_UqrpFEUApdWUPuVtwWRbHe37-BDX5ZM2VgLQMJeuflHhs-M4Nepd6qouVEbs5n0gAVIwrQjDZm8NgwqveC9RvbY2XzqmsdleZB5Wk2lqCvESC981Vl2fkKxvgW-JW5GmAC0EkBO5IlLFPEe2KrnkB7Hh261w9t8nNvuhq4-xXh4m201ViqeMgHs8hjXV4ViYFgI9yFh5tG_N1xua4i2cdswXAU9acUbK9CzTdSbawl9ZrGiR7eaDb1CyDt8a4g2ibVLYZeWKLAzC5ixOXnEDlBn0c-SCAqKtrIk1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=ZujsD2uy23-Mtr_ziyRUQ3A6OX7sXfap7eDgZhBxzPQKv85I_UqrpFEUApdWUPuVtwWRbHe37-BDX5ZM2VgLQMJeuflHhs-M4Nepd6qouVEbs5n0gAVIwrQjDZm8NgwqveC9RvbY2XzqmsdleZB5Wk2lqCvESC981Vl2fkKxvgW-JW5GmAC0EkBO5IlLFPEe2KrnkB7Hh261w9t8nNvuhq4-xXh4m201ViqeMgHs8hjXV4ViYFgI9yFh5tG_N1xua4i2cdswXAU9acUbK9CzTdSbawl9ZrGiR7eaDb1CyDt8a4g2ibVLYZeWKLAzC5ixOXnEDlBn0c-SCAqKtrIk1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=W_aeG1rODl5qhIBB5ArHugGNMe9-XNL9smpogngiimSFYb_33E6Wjd1lRSAfaYnL9JwO20Eo-o16hO-08w4FI8jzbh-k0zMwVchws07YaMkJGJfZr75DzkthPhZSrchb2IU5AYK6ujHFfyvF8McdxGbNBVhUh07c2xpVvcdP9LOPkKbNwW9v9pTjHEQnHb5GE58_OCkKolaD6jcReLuPtu1w4BkNGkF9I4r_PQ-MnXBI1DI9Vc0WLrVCKRlmExgPYdsMKpuQCw6ns8QePFJ_YxI0Bg44Yl2r7X2WBpYabSQ8rPV2UQs3yHUNZ16XS09MddWLW9I5k_lSJOflN8xpGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=W_aeG1rODl5qhIBB5ArHugGNMe9-XNL9smpogngiimSFYb_33E6Wjd1lRSAfaYnL9JwO20Eo-o16hO-08w4FI8jzbh-k0zMwVchws07YaMkJGJfZr75DzkthPhZSrchb2IU5AYK6ujHFfyvF8McdxGbNBVhUh07c2xpVvcdP9LOPkKbNwW9v9pTjHEQnHb5GE58_OCkKolaD6jcReLuPtu1w4BkNGkF9I4r_PQ-MnXBI1DI9Vc0WLrVCKRlmExgPYdsMKpuQCw6ns8QePFJ_YxI0Bg44Yl2r7X2WBpYabSQ8rPV2UQs3yHUNZ16XS09MddWLW9I5k_lSJOflN8xpGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-KDR60ssmH-wRfLnsQxTxSKxVdl-CuYdaQIhPdZN5OiDdzL3B2CV5klb71Qi4pytJhz6s7NNyp6scA177u24V5Ls6LMzIyJWQTLhHWsujbINxv9tEyscpqQvE46YxaJK6uF9VyJZr3A5-FmyVR1Bnc3b4MFnPGLZPm4NWjOP9MbsdgRGEwRGnWR6P7nImSn-msy916mHjHO9TTSFaVxQM4wiWXRIbppquEDmu7bCD7yyXiklzwXXXVqSD2KuNQTNrcDtL0dUBIJSf2O39qJZHzabrh9Sl3TC4W1cq1lhxma82zYwIDe0VNzVqTEt2NexU148ugWfkK8d2WJkKkHaw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=XfAVnLVu7Cyrbxdl-gWCe5W2V30xGzsIpkHxl-hjJX0URwV2BshEYJUNHvK-fAVkTbyTEOKPRxiGBIe-RPo5YL315OjP7TEJZUXy6WReTzWbLLoidRUSyjDglh2JimhZrS2l-8UTFMy_IILslE-Y7pWplaf9cPEB88-juzDnNpSCeyHrQxiB_tkwgKU0nCeLOhXYN52R5rHQZrSmwbHzR0fWh0rdTHAXIcAVIElcEH6AC9KFqDpQYUU6ZbCpkh8BL21CBpYqc6CNHPMqxz0kGkh61Y9sRYAViA5ozc6LCZBo8msFZajjh7pzAwJKf-oz3DJ3LzKiTyQokEykYee6IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=XfAVnLVu7Cyrbxdl-gWCe5W2V30xGzsIpkHxl-hjJX0URwV2BshEYJUNHvK-fAVkTbyTEOKPRxiGBIe-RPo5YL315OjP7TEJZUXy6WReTzWbLLoidRUSyjDglh2JimhZrS2l-8UTFMy_IILslE-Y7pWplaf9cPEB88-juzDnNpSCeyHrQxiB_tkwgKU0nCeLOhXYN52R5rHQZrSmwbHzR0fWh0rdTHAXIcAVIElcEH6AC9KFqDpQYUU6ZbCpkh8BL21CBpYqc6CNHPMqxz0kGkh61Y9sRYAViA5ozc6LCZBo8msFZajjh7pzAwJKf-oz3DJ3LzKiTyQokEykYee6IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxS1sHcyNnJy4dfH5ASpah_XUNEBPRAaRxUI5Tn7XMHo6NcI16dBOlpxmdS17xZXhCKIBG6X5QE6l5kqswsCI64Fyhv4nY-hd74eP8j2AW0YmuB5eQ6D3sa2fooqkp2p1a3vcK0EtBvRlgtrMBoS0CNHd_wiTJjg2TRK7UZlrB0JNZMz70l1vBOqM-yhPt5ttUG0BPAfz9uoLo_SrhZe2fbpN41dEL3wC8sjb2gU8J09MTveMRLfukqODHofBjmY7_yiYkXpVtS7ClTS8JFwkb2AWEVIn4k6-nwz7x1gs3cJclzanqz0nzghb9PAncuPOkT-nCA5V6s7HHsBQWmH4A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=TwOz8XHEv6XqQ-wn4juxxPAhhDj-FC3eCqsYDR2QGlXMwX3019ASwg2NX-u0ALc4_Kwie1N2W4C6FwjSAZ1mx7GclMUJbOTZ-ZG6-K-2GijJcF2PuCAfy5Ymvyz41XraJy4gALSLbCzQIaiNaJrrh1Q_KGzJwt2R6PUGulqvhBVdFdCnP9l9Bdd8381AVBljvmjpD1erqsPV1ymNrTsaMUO9RYkQ5EBnONhQgi3iHy0aPxo6p9yQW0bJHtu0T0KkbDJMPpMcUuD0PMWmM1lGlMyKmHLF8pcTHoYspS3XIkVH4nTh_FSVqNHKASPZNIZlqpUW_2lszqFSpIknvg35rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=TwOz8XHEv6XqQ-wn4juxxPAhhDj-FC3eCqsYDR2QGlXMwX3019ASwg2NX-u0ALc4_Kwie1N2W4C6FwjSAZ1mx7GclMUJbOTZ-ZG6-K-2GijJcF2PuCAfy5Ymvyz41XraJy4gALSLbCzQIaiNaJrrh1Q_KGzJwt2R6PUGulqvhBVdFdCnP9l9Bdd8381AVBljvmjpD1erqsPV1ymNrTsaMUO9RYkQ5EBnONhQgi3iHy0aPxo6p9yQW0bJHtu0T0KkbDJMPpMcUuD0PMWmM1lGlMyKmHLF8pcTHoYspS3XIkVH4nTh_FSVqNHKASPZNIZlqpUW_2lszqFSpIknvg35rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v--oo-YiNuq80l9fBXqT5TUAt2yEZtwoj71NN7tePzvWEm7sjhzLHwTP1PwNpoJ8rPHVGmen6HidUJEzDbyAdsK3YZoJWdF3h4FZMbVqkltVuLDNCst8AOmfi_FFP55M-H9q2e7cLWRaQQHHlnC7YSnF72dZLdPEoUsNIAiLOp6ow0GzOqyimH4ZGuiolxHns7ilhkkrwwCqzzDioM0wAUwPerwZDLWBYiXTmMaiFbXJ9qJt-MQJRfIlzFV6pDzHO7_fZAw9yUkXlZKVWv3vfdZEpD9J2dMV5V5Zt49pZBA43iGMB2Go_UgklHRGd5FGaDbDAj44UBn0h85gZm3W_A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=VVP76Nhns391_rrTHTyE6GimrwKcF_Zia5MY7Yin47kIkeNCVZNDnEOaNfb_qt4bydX6-qJ4Gj-LfIlJUMnOsuhCnr7DG-akLSYLiukIZ74GBzRxCz97-e4slwgF3AN9e_ikZcdov9ZNYYVajPu7LcyNlcPHGFmh6q3PfIfgyyfEQNJn8ZXCxCtwWRx20ONaWf3f8zzBNJHBd59mamgCcX0ZUiSsEFwWucPHb9ph6YUXvIkfMRpctFrBt_JcrNhH2UmMVYF0Vt2hZmGao7xWed1sIQR6-vP3hYlJxJVUjivkK8drQy7x9QoPIzjo5WkoGOH8wBB0in9oLr42kiw2vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=VVP76Nhns391_rrTHTyE6GimrwKcF_Zia5MY7Yin47kIkeNCVZNDnEOaNfb_qt4bydX6-qJ4Gj-LfIlJUMnOsuhCnr7DG-akLSYLiukIZ74GBzRxCz97-e4slwgF3AN9e_ikZcdov9ZNYYVajPu7LcyNlcPHGFmh6q3PfIfgyyfEQNJn8ZXCxCtwWRx20ONaWf3f8zzBNJHBd59mamgCcX0ZUiSsEFwWucPHb9ph6YUXvIkfMRpctFrBt_JcrNhH2UmMVYF0Vt2hZmGao7xWed1sIQR6-vP3hYlJxJVUjivkK8drQy7x9QoPIzjo5WkoGOH8wBB0in9oLr42kiw2vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=T09p52iTb9iV7gyQlGwRWlibEZmxFqe3nIiKHCUTXOQSWnwt9it_Tj4_epomObmFRhDowfPgFkQ7O1kkxlh8JXrc981aC8DFdsIxxqE-VbNvROQ-hoYIHMznCd8P6-CR-Cb5pNQ_X5QCqJII7PW9MfTKAYgwCEw7UAGVAoRH2du-rRyvu3mGW626srSMkkRVJW4WQvcbzQZIHCm5epKdlMmi7qYjTsendyaLf5m5u3xpQK97uraXUzRj-JDGIsz1VAVBenMf41qcPtSPVEVKF6-GmpifY_P201YG5B61dF7MSZ4iSE5RSseM1dHl99GVhfZKPp3mjoOa6y9HHuEvR7zLjVCnVOFRHsw8Je_FPR2ONXOI4XTdjjFtUDuE9xI3IOjr6PRhvLsQqsUQ3ZVHW2Aw6datcekTg4ewDxQ7J8FWhh5nlHFMsebyPHBAWT01Zs55mguGY56s5ccraZVl6hPCAH6jGzYz_vYCOFWoYgzeNKAkDibNIWv155YjRpTu5_5VfPd9gZbCOs0wD4f9KpB7e28e_IGbbHCCjooDXc1cHlKiPN1NEi279X2MPkzkyiSKjB4M7JtSJbznytNi_AR1LZi3zOX1jPLKwYIDJ2KNr9jc86ubgVK1TEZ51zJmOmXmydwarl0krJKrtgZ-ntxGdc7dSVbTHBoxq2ILX7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=T09p52iTb9iV7gyQlGwRWlibEZmxFqe3nIiKHCUTXOQSWnwt9it_Tj4_epomObmFRhDowfPgFkQ7O1kkxlh8JXrc981aC8DFdsIxxqE-VbNvROQ-hoYIHMznCd8P6-CR-Cb5pNQ_X5QCqJII7PW9MfTKAYgwCEw7UAGVAoRH2du-rRyvu3mGW626srSMkkRVJW4WQvcbzQZIHCm5epKdlMmi7qYjTsendyaLf5m5u3xpQK97uraXUzRj-JDGIsz1VAVBenMf41qcPtSPVEVKF6-GmpifY_P201YG5B61dF7MSZ4iSE5RSseM1dHl99GVhfZKPp3mjoOa6y9HHuEvR7zLjVCnVOFRHsw8Je_FPR2ONXOI4XTdjjFtUDuE9xI3IOjr6PRhvLsQqsUQ3ZVHW2Aw6datcekTg4ewDxQ7J8FWhh5nlHFMsebyPHBAWT01Zs55mguGY56s5ccraZVl6hPCAH6jGzYz_vYCOFWoYgzeNKAkDibNIWv155YjRpTu5_5VfPd9gZbCOs0wD4f9KpB7e28e_IGbbHCCjooDXc1cHlKiPN1NEi279X2MPkzkyiSKjB4M7JtSJbznytNi_AR1LZi3zOX1jPLKwYIDJ2KNr9jc86ubgVK1TEZ51zJmOmXmydwarl0krJKrtgZ-ntxGdc7dSVbTHBoxq2ILX7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZTNhy3tLyKAWgDdDAb2E2VjkmfKHIdUKYy4g8BIeA6iY_CowKvRC77IWzlqk8lxHov9R4f4UwXMKw-jIZ6lt1M9Z0ODTgTFWDoMZx9hUJCgmodnVi1qSyby8RhTBDRDmXmkzkj0_d9pQM8AzDYlABHDu6RPFhd6S8-Ectmf3JggpFPo7k56f6lUtjDdbyrwFc_DSnEThWd5RBih5EYqXEhp-gUArqv49_ZDp96EBmeQ7VHkDtwsb_FH5Zi_tSSBx_doLFfpGwBkCUHf9qRszHCDh7fc9I9BW5aFAhdcBkzUr0uJikPXZQmP4Knk2HvmDje0-kKHUdPIMBzvhPPzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILz7gNGJ2zM06TvHfeiww2k6KzuHwYRKtWpaSkmXoe1Q5Z-iafmHemtcsrK4EwUIWnWAs23c3xPZrJ-DOJ4f8YTbrMVnt1_b_xXy6wjyJygswtlEv_FNjiRBe9k3aXzc4Xa_6fGVsxRpMXpgC6QmXOTgQIKH1EBGK96Uez6xuK2sVzE3x2ZhtbZzdDc4so6smRyW4l0nwNaogmxbCg09roeJntFePZGU_YhKUpkDlnHgFrRdu6RzZlbODTfomBly4CTvVnJMRQzU5dhEbKurpJnICsOaEGGv5gBILaSY-THCoAU2aZ-nyFRsGRB-vw_zv_s3VJ4JPMvvRh9eJIzUzw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=X50DQDl0aoLYnCVmqvwFDKjqSuI0HJeKijO4YKV2egd7i4nN1JpCtBxzzCAHLnTsApd0rHq9bFTvTdaDUjvGu1IpRcTPUzc_eUTMTYjyKdUAXI4ztn06D3KvTYWCFxpLPN-0MQn2pxCLc1QhrRKZjGPekIOPkD3NoqvYkBu2dwz--fz8to_OxXa0xUTOmHhl-129NXu88ZuLVEFiQjGXzO0sX5InPi-EhgRCmHiXrT0a8PEVv7_LEKkxjdByPb2xdHeICpB66jf7YCc27K0HbuoCNBQ3FtDMXLyKC3sJp3X-NO5xsvSpNdNQbdUltUk3FTvC0JzW2iG0VaBycr4SRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=X50DQDl0aoLYnCVmqvwFDKjqSuI0HJeKijO4YKV2egd7i4nN1JpCtBxzzCAHLnTsApd0rHq9bFTvTdaDUjvGu1IpRcTPUzc_eUTMTYjyKdUAXI4ztn06D3KvTYWCFxpLPN-0MQn2pxCLc1QhrRKZjGPekIOPkD3NoqvYkBu2dwz--fz8to_OxXa0xUTOmHhl-129NXu88ZuLVEFiQjGXzO0sX5InPi-EhgRCmHiXrT0a8PEVv7_LEKkxjdByPb2xdHeICpB66jf7YCc27K0HbuoCNBQ3FtDMXLyKC3sJp3X-NO5xsvSpNdNQbdUltUk3FTvC0JzW2iG0VaBycr4SRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=C_auOrsXNFryn3CYBQWBgwe1ynTcyr8M5tZzSk1vABgBdB_W1kKw0N6yQz7CaxRgQ2gQoretRF_fnpIVCwKSNO3DdvcQhuE9OkMA-56jil8TU29uyMefq6M1R8oNMUg9YpItpsForeMlTNXZ85032SdsoNTA3qWG_76PZl4rTHFcCi5_F_prrQWzS0C9IwiQJadsq2uzg66xGf9skukLxmuZvVnuehAiwMyFNsxOgCwO9KAIBqqj8ZXSkARwKpaEgH1z3FaLo-1A-gyEj-8PF_bagCKTshZnoJ6q3uPK_dx9ss60liJwO3GcGYdLS-DWSufS0hAtR-NO-EsNqCzbyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=C_auOrsXNFryn3CYBQWBgwe1ynTcyr8M5tZzSk1vABgBdB_W1kKw0N6yQz7CaxRgQ2gQoretRF_fnpIVCwKSNO3DdvcQhuE9OkMA-56jil8TU29uyMefq6M1R8oNMUg9YpItpsForeMlTNXZ85032SdsoNTA3qWG_76PZl4rTHFcCi5_F_prrQWzS0C9IwiQJadsq2uzg66xGf9skukLxmuZvVnuehAiwMyFNsxOgCwO9KAIBqqj8ZXSkARwKpaEgH1z3FaLo-1A-gyEj-8PF_bagCKTshZnoJ6q3uPK_dx9ss60liJwO3GcGYdLS-DWSufS0hAtR-NO-EsNqCzbyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=lrNOHNj_kiBtMxc54pqK20To7dd-VRKT4Ur92T5uh8I6BMq9BCM8HmjcFktCkt-KZV96aTF_kJ-SqRbcU2rRBiS84qQei3ro1bP3zJG-_-5SfGunje9GSWPgBD6C4P1RPYm2ymutAgE51sM309GcE4KzjUtILcSAHop_ujSeEHtYTSYn_eF3s53YE1Nt-Y6u2ds78-Bx86vTJBI5DVIZaAV641WLJo-_9mEm4FerXmQpQeBKcJwE090lSIk-4yF2wjluo4vauk_ljMbA7HWUXqZKL8d3ajfSCi0kYyMuGHR9P34XkmS_pOS_YXhfe9XFu_y5F-LuvwhwvLsHoFJl2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=lrNOHNj_kiBtMxc54pqK20To7dd-VRKT4Ur92T5uh8I6BMq9BCM8HmjcFktCkt-KZV96aTF_kJ-SqRbcU2rRBiS84qQei3ro1bP3zJG-_-5SfGunje9GSWPgBD6C4P1RPYm2ymutAgE51sM309GcE4KzjUtILcSAHop_ujSeEHtYTSYn_eF3s53YE1Nt-Y6u2ds78-Bx86vTJBI5DVIZaAV641WLJo-_9mEm4FerXmQpQeBKcJwE090lSIk-4yF2wjluo4vauk_ljMbA7HWUXqZKL8d3ajfSCi0kYyMuGHR9P34XkmS_pOS_YXhfe9XFu_y5F-LuvwhwvLsHoFJl2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzFcp2lHGFKnDAXhUDkJSNjbJCmBAtZ9T0LqTLZQ3HjIRu40j0VwYyIHN-CZhasl2nO7DQR-vz_L-hNXIxGUL41x35L-PqX9TzBJYWaKB6S_FTpgW0dOpuRYNP-DOyFLc5JJsJrcYW4f-bX7dOwL8n98nQ0T7Iu_nMIvvg6sIv6q_jMGO8PKHJ7fNSCeBSAdTGWuXryNiHwmiknmU29cvwMeWeFR0NjCUPLS8-5Dc9DUzVMAFB0_rWUimIUdNVphFaYtndBV3V6IuypinIuiTQJfIvNSrNK08LuzIVcdnVwTresTT0I79idJBPTexgZGT6206U7WkcdTtQt2ySAhhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urhHfIzsRoPdNi4A1zlYHoxw2qtfngshPcPlf_0d7y0ejYSalmn3F6qE3Lx0FOS_h8a3NQBjpsUZC3AAWRpK-4wKEojyyrlJT_EzChVxWihWnISthxfwDd1k9ARZxKgAbVzApX8GCl34Hc2ikE3zIQuZgCPbHTq7kieTfINN_E3Bs0rRPVZTpE-XB5d0qRlPXgR9meXBkN7AR7pMSAbb-V8eRidI8b5eeEPllAR4GvYtSCdZRST6nk1VqJh7QEmHye8UiWhq01e_dEZFVuXUcp94Ep6lj7LzHKs49cIdL7U6bqU7RMzzW2LcjM-WaIbYczNPXVdaqWy9OC-_dHhlbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpzCAqEkQiek4Y18djYKugR0HJTg5GV6sEujyyfxu6UuuK-cNCAEOUaqu-nFR5qk8dIHNTrZTZdeiTtA5aPuD5OnbnsFS1Ye6LbsLlcD4u8lEIw11Q2J2k22vklSREA2zR9ZQSZSHevrR1VPTkoyIW3G6Zlwvbp-eZBt4kSB-7INog4L5ira9D9-IFLDpJtDw3HblfKOPHv7l_2IQroxDyAMRmAKNX1I7D0pszFgY724H4gU5DVaQDRM1ZsapHMIOY7xfT34Su6QyAwvYKcLSZ-CyTSiWNkUb_YyYl89yLaKf0MozedrCpotkrXngz95Om-lz-F7fEPo7I39kol-GQ.jpg" alt="photo" loading="lazy"/></div>
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
