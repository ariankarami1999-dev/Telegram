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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 17:52:09</div>
<hr>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHyP78d_fSmY-vAEqFik2l7ZlkGJy21Sx5I5dXjWixnIxpRpKMQdGkAI1Oq1KSAenwWGwTeB-J37Ym_eptTW1CdqlhbHYgkJxls9JRsQ6XtTkUONkJqS4JY2SPk50aB4rZOLXPUJiFVeAy3u1w6TP0mONF6NlH32w-dKUTKJRoz7VaBhNN7Z95b8cIM9PlEwtvH-zGzX4l1FtoDauqlw_SNW_Xu1nKSHmCoNkqm82SUg5FXs1X_dz-73zty4MuzmLJ-735vEf_LQIWyQ50EBzG63ad77roh1KcQEy0tAt6VCjwrdaVW1OKXmh-XXe-AltoS88ELnyqYCKtTLo7lkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFoTgLRG-08-wXkVfnmUjpyU85d5MEOPeSE2RXukUJ7gcjmFTYlZCb_kpnQL7ZIcAAM_lDv_J4qZLl0hoiuQRaoKA_6j-aoodXfesfc3KLW2-ibWZjxvxqxsCsKOE-w13vSFR6YCpn74DYo1NOBBYyEvAsrIYpZHslnt5ahw7Y8rBD5zD72zEjJb8Xbr82oFCT3fbG_O9-gKukh3C2YomWyaoxAn9HMpLntkpivRZrpZ4r0DzEYp8eqAocUxAJO47HRnA1D8xjLyMZVi-YwcsKo3Qk76hvz83eeZEW9VoL3t6eBs0cX36qSbGuiRA1OhvmzravFHMOyi9dx-QJrwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6fj-XikOE_vV6gn_Bc8O6-xIM4wgXc4YypxLCBQshzeZI2ex4bJps45gE5IffGwgyOcFmOIBXpQ5LzCUMaN_tBTveENWfWCKP8xENhazzUOnaFAp2M-41EK7Ymex4ZhS70FmJAmyGgh9BYHdlF6czYGHLcTQPXfB5Pl3iD77I8DjDXJa0sUIEh6zuEi1VR39aXBilQoalJgeV9tVniQdu1Klpw0ZHKxsgfSfFTz0JXsGf25mcyADsfQjrHKuvlh0iIPGCR6LoO9Jd48T7nKZvec_4o_-CsQq9qSzSvN6_jHrdi6Ysi5U9_kDIWzg08jSHPScvB1Yh7KR2t3-wfS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbIJyOE2Zg99a7z3TD5mDWj0vjc1vH4vH6eeDCZB033bHtcto7zbvY8OM41MekdSJL9DlcS9mLECr4XoRiKdft09qQFx0vnI8Uf4DSB9UJ5SLtKNYr4kzEbFsDroDdylLGJ1uLB_MRRgKpUuLhaWn329PoFDM2Mf7VIe_Vfs2tbR3FlpSShbyJ6hYHVPN45B959Ufyq7LeVRhGgU4i9RBjDSuvUrTRx3kAfK39tQMR-B3y8NO69Z17tPQoOft3RC91injyqPAcnU69MuP_c5i290F9K3QcyL0s-jszxBquiXLylYWfTy2J4tucAQBOGLSqhVQS5QAUus7_jHfnFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBCdTL9seDcNwGsIb89YYMmUWZ75YhupG5WpItG-REVUvZfiD6KHiROnXkLn4fzdNEvQCBsplLIerYuH0UMUBEtMsezM3MC7ZKK7Py0YFkm2H0O6mZei_Fnzbygt7tAnrp_QgM6h59w8uxsGJIyNVQN0aLBYMYZwuWWVtE_nnIqjCdwrYgb8nyJ4K2r6_6FmvF1cFmuGuqTGjxgGNBAjAkenwQxu9CHL-SNdywTVANS_otcnr7RB-hd3qv4e8yGeMKp9oah80UsGtFRxbWjhdqYY3e5LcKoObVpckCAzAsFgLiWr1fFP9YOF9Blgz6KLpZDuv4UTBUShsOAstb-pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_jklWp-P3SyRXbm4_EDnMya7QubfMI49g1j4w_VhiPn-iZO2Evl0qL-0_yfAfFGW06qtFJ0UHnNf8VNKezps_esDctb0ISCH2P6bquT2fhd2L-LWktS049d0km2_qfc_tzlCR9l4PnCDawud2NIK3WyD1SKzbAZDNNSsI9Ag2I4XDPwulWsAhcmD5ckwtPta7cd4Q_2LgsjjzJuSBgaE4NfL6ji8a_T2wKx0RQoUsLXHxU_QD0i-XsiaHSvD88FEIKUiIeua4WC6dHLfzg3ljE_VPOoMVDG_dxu9S4sK-nc3_VHIwtLtU2D0qQOoBR2AhqMam6Ajzxy-v-rz5Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLFj6blG066qOc9Vz59KMvvnEt9kXhpJ-qtpAmFfW5ICohqG4FNQbWoELS85GqFKPesMMQ0oIfeZTJVY-UBuixdjzb57WF9FRUwO7fSY_zE_YSTtvWkrwiIUm2vO2p_7aXcYiUh9MxrcFc9j22DyifsmU4IGvvMZCwovXGmVQUWCILGwMwwid2CfDJ8gyH-a898QpObWojN6z8_9nSXZslXvmd3cLOi3Mv1Tyvs1VE5qQFTsUJnUtIgorLz8krnFxK_6LS-3AeLXwgACCRvbgX0dymYpAbeS0kksqNXta6BKMCcSOREawZwACz_9ToLVmNrpjPs21FyGGKWgGaYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW3Y8wkErEwjwhOu146AJeeXna-1_Q0yQHyVoQUogvuEw84IQQWdhgrcwU80wv9tXG-1-1jTExHEOTwqgh0A15l5iYi9CWoppsIWSS_H_9MqlPO-ExhLP2LqfKuW7q3xDK4o2mdX_UoqYv7uPLz_u6ilcSEtzGMwSEIrDajTgLwW-XHDpJZvpULYX9Nmzv8qJtpy9PZuvcubBZXBTiJ92E6mS6ggwrjB_PG7OV5UKWrXZQCzHSFlIUOOE6JmN3GhWMWGj7vpEg5yt4XNt_lIBZmLVrNJDyAXQONcTbZ5wKvksbzWFVuWgRJTiWIsxnT8K7PmpZw3v0Ako2lvBbMjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftoT0vHGzBnDY_XOgrbM999A50vu0U3HCEN_VD19MRDlKDrZhadB94T8TrzcNVRt85obQoUoJlZuJK3fO9oEmw4y29FrXCXwTbD_uGmPLdIeQCkoycDhgOUajra1PbFAt9VMcv8n_IHQ3SHNWnGxGXjVLHBUO55RjZzf5ftn_evCkOxFDKjzuTt0TUvZjEPYx3OWH9NLgMRb4TmkwxQfeP7eyvtHE6V5ul4OKgv-3bLHn9tJpWBBpZHnTHEQ2wJppZGzm0FF5ydGr_3tDiyBeExW8qgAtWyFe2c8Um8pWnXv316Y1cQGaND5plapVjmBIXdW2g2xBfNyjqXDsYpiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBuHBmINNg4wiMez3F-XCUwCh4n-_2LP_GWmwRlvnv3TFyB8RtDkVdxb-Zy4nGNuP-wdA10DlFbZHZ3V7DqWPXgM6jJi_nBBZnfe_VWYMtMZVTwM3Gkw2PHhpNwx5Q94VeSu6SgJCCxIPXPNGYI1f0EMhCXR44ZpGDsZeziddZoIIatPBWIGUFywliuc8Ua_-t0R8rx1NXDW570NgtDN5LEjSln8aVO5c1ZPYPUopYboMTfzkUbascvXkreIKjppVfb7XzKleq3GoqDFwbxxxuEigMvroiMAWjN6zjiNAYNdzrFWaDGyALxHEazfkLoMoyO8bvmEuGzgrWQgGpGQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN2fLb4cazVvpoyA91J3Xw1V91yDEY7pxYNgyUboOI9fXj91j597ISmxfcEJt_qEUY4Eh2hbwuM_F02Ox3-MqLHnZHt0fMpcP6qVafcVjRFKeAdOP41tExPMPlOR_FAbVXY6TkExty-hZSS58DfVrNyIx-ONpPI0hSn5r5zYv28Xqw3YcMw0ZcKS1d4VuQfoVSoZ-MFA1AI3sWnUVmzgndyX7JEmOz13aMv_PBYicl5pkYcshx58ot7S6HWN2qSBKY87Dy_t2yYzlrpoelwlEQCVAEx7zjN-2n3Ty1JYd8r0GIG1hRHOgavx1i1nkVK_UoB7ksQccoiVrr0GUQT5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i5pP0lmx3WUstOIKRKK_l_UDOEul8FC-JWHpGrPa_axYQ2mDHF5ACRkp8s7tUlyk4BjRyAhePViQaFA-90HYT6bUFUvZGhy_moyO4eV5R0mpuW42xThDm5IdvZXoB5cM2SQjcpVPROftZWcPZhsLRTo3te_p1BnluZAEpkVgZ5RRN3A--N582SKvrBZZS1UBLWJo9-ca_wyEjMa6jMRN2Vrcrh2LoSApSMwp2fTZ0-NuDdGuFHjkeIyPcsgqqU6KGWd-cI4XDFrMmDuRjFXRGsSXjU1_qlNSIyTnJRefXCvnxWxVZAb7JgMiU8WNy0gktVsMNRHDRRkeLZYCXLDICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbsLCCtH71ZrpXCrC5283G3reQ0lrzIk8Ofdd7D28B3RSongqUvYtbtvyX3eAshVAwHeFDeakHAC3is3ItsUfGTzo-z2iJJJkwnCs2exCRj_gOUZ7e23JBeXzrJ4BX4cxN2Y-OUq_7_q-dHoEt9mFu2k1Q0VbSAtLnwRfkZkVJbO8qZXGWm5UBcWn98hEhUbMaHaxt_YyvjaicBeYaArxLK65cG4b6EipZDoFNBel3lg6LK_NCsTp4fVIswVayjyNEFD5oZWTNHzzuhDrFfC416d_h278MkunOXhb3xEfnPrxchETaRG6Tlc3nDnvcMr39BHI6MHvFwRBmjHlgRFvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=Jme2LP2pLiozT4LeANJG6a2vw_i20l1S_gGa5v2WCKbUzCXL4l5LGAIp9zSOgCGZkNgNM8Fe0fN5cdwugQVhdE4hXSivJGfZwOKFhxsyibp5dfX3rrsl9XTudlcghHepur8N_7tni4c1EUkW0nul9DseUZII4gLxe17ULS-NmMl9H8FPg7GiAu_wOOsq6UlvBwkjRjY-vyllovjT8_2LTnbd730-iVGD1rIgIYX87ablxZHiaSY5BnDE_YL-1W9vtKO_7RgTFBDEjYZ8MWYWFHlXAB9zSvxw-lneaU4WjK1sUomCUAOjMvbwU7CRHE8oUaZ9edu0ofajc0gHfABHkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=Jme2LP2pLiozT4LeANJG6a2vw_i20l1S_gGa5v2WCKbUzCXL4l5LGAIp9zSOgCGZkNgNM8Fe0fN5cdwugQVhdE4hXSivJGfZwOKFhxsyibp5dfX3rrsl9XTudlcghHepur8N_7tni4c1EUkW0nul9DseUZII4gLxe17ULS-NmMl9H8FPg7GiAu_wOOsq6UlvBwkjRjY-vyllovjT8_2LTnbd730-iVGD1rIgIYX87ablxZHiaSY5BnDE_YL-1W9vtKO_7RgTFBDEjYZ8MWYWFHlXAB9zSvxw-lneaU4WjK1sUomCUAOjMvbwU7CRHE8oUaZ9edu0ofajc0gHfABHkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=JdZTFeRc76-TVjA0mpXqlWAeeJsEPrk4Hp2qTes1kliBrvCp3jIOYLDnQ9tTM2vG6eSX4Ftofm7ym8j7bURbxSy9eAoDSTQ86HXCQ7a-1gl9GkEqeeuCKIcAisSE913uezsE37Wvx9Kcf1k_GSAMR1wVx8OWPSzU2ANeEIJGdlI9F5ew9L5UR9-M_GpHAE3ixQtOwmw9jeYvhwE0cJA8-XtXh_4ewH9TiA6MTaZy3ZgdqNGCMd34I-0jmDpItZi6sxUwm70qORrkrBKBVZ3IpSOb3aFl7Yo3lGb3g8WNkxrU8WaTXQSCRMc5Yf6ksxDRvalfYX366KgK6yM_EFPe4oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=JdZTFeRc76-TVjA0mpXqlWAeeJsEPrk4Hp2qTes1kliBrvCp3jIOYLDnQ9tTM2vG6eSX4Ftofm7ym8j7bURbxSy9eAoDSTQ86HXCQ7a-1gl9GkEqeeuCKIcAisSE913uezsE37Wvx9Kcf1k_GSAMR1wVx8OWPSzU2ANeEIJGdlI9F5ew9L5UR9-M_GpHAE3ixQtOwmw9jeYvhwE0cJA8-XtXh_4ewH9TiA6MTaZy3ZgdqNGCMd34I-0jmDpItZi6sxUwm70qORrkrBKBVZ3IpSOb3aFl7Yo3lGb3g8WNkxrU8WaTXQSCRMc5Yf6ksxDRvalfYX366KgK6yM_EFPe4oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlvoVU2oIbMXpQB_YthjLfZ9dNbZ4X_6jsb0sRaKoQyuMg6jpTq3ZxZ1-uvS4ZIico1856YKhsBv13jhbppB_Hr0GfINZeKFBHEeGfMfy2UBEIs-wYxsYknAZmfP5ToU_McIWlyE8lqVQVIouCQhDQnRdatnn-UPFJVNLi2swm2terkfsp5BeHfI6UPeBz21eQWPXsSmTR9UYC5iJ-R4NL0I39dkcBHv1SLUEvqzK4dVyqTXloKP9hZ16TAt0cVXsAS3LCt7rThpje-9JMzkA14OOW2gaPthwElCQRKPul4gcN-usgyAbTVF-Pa5rkPUdVtYVJK8m-92WuNa3mhXTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bG9Xy9gep5js6P6AnnRb7V8Zy6qzpY5Md5qpN0Lq9GnVgvZb6FTCbFNCJbXyXHGB0ZhPbzXFDNrMXeBDxiOQ_Mnr9ropE0eMxmpTATcxNf-Tad64VtVZRELQSSqc0az6OgwB3UPfB6w-t3pWdzaAolsJ4Hkv6BH6DOiXG-Jz090q0Kl8p7K8z9NW9dX27d-W14syAg8xYN8zeu-PaOVp_Fzqy-crPn_GhmdGV8IUTStuLBQNlMojiD02M8tX3qcX83SgqxFPKWeLymKm4MFBsq9B9Ma8dUwVzhmTFopqyEALm7dlIDiT9k7r14keSIreVUwT5S_ewtiuwFXGKaZpJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwZoiI55pTpsD9Ez8gwAan1ONyeSxuaNh_wzl09dsalK0WPRTs8kfCUu39JPKMpZ0-4wk943U7YuwJd6V-i7Sdoy0X9kaV8WxIfjDfILkuJlAJAP1vOUBKFBXEaJz_ss3_-nmwSvImjq3De1W7p4nXec9nkBsvteYQrU8XIHslP62iWB021i80KytQA78WXk8cWhkSOV-34xJ87d0WxCHeV7XIFncNIVOHrn25D0cUzzP2UgXMTCNrPKbVY5Vqxms8Acl531FxpoegbO65jPh0bwEDSLVuzgFmQKtyyOzY1J0I-eAiIpUqGnEg2pme6jJjQoyIDlz6nyBDSsd0ItiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlhsOMjKTikjsaSpjo2-KAWDpSa-aG1DN-9qoynPiv2vG40L0IMaxanhC9VReLMXEnTm2cyFFIyKVYV6kKVaNK_TMCyakWpmuHcvHhKceLGuddzSTInETrJRNsj7XNyCXPQ_HF2sRR0nMqFYRGEbafqoUeQdUvbnkqH8RhjLvu6lCk8h5dfBwgWqbTfaT0HJBtZH8UNgdP_OMh5BMDfROBF-jfOGUzctn7VETxzE5CHr6-1Y-KybYU_OBxTeJltmYk1agHWttQ7s8vynMaUznEcKvc3754UZNZ13D78iQLZgD_YQXxvZAU3UbinctwQzvf8mAbzNH8LI6yvbrly4XA34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlhsOMjKTikjsaSpjo2-KAWDpSa-aG1DN-9qoynPiv2vG40L0IMaxanhC9VReLMXEnTm2cyFFIyKVYV6kKVaNK_TMCyakWpmuHcvHhKceLGuddzSTInETrJRNsj7XNyCXPQ_HF2sRR0nMqFYRGEbafqoUeQdUvbnkqH8RhjLvu6lCk8h5dfBwgWqbTfaT0HJBtZH8UNgdP_OMh5BMDfROBF-jfOGUzctn7VETxzE5CHr6-1Y-KybYU_OBxTeJltmYk1agHWttQ7s8vynMaUznEcKvc3754UZNZ13D78iQLZgD_YQXxvZAU3UbinctwQzvf8mAbzNH8LI6yvbrly4XA34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=ZbbTfJ_mQbzCuht6OQC-wwPebncTBGnNnDFXlCp3yagduGhVH9p-dg7BfwaPIQPJTgjOXf2sMsaV0oDSk3XqkkaLfxdN2TAzqkBX2TpnWCzcWMjKGLasf5QaNO-Vn6PGxu14cSR4ZAr6tJX03cptnUaPUo_-TV31H39abyJi3gWu3Mw1Y8JvKeZgpUuMeHbwbfztjwojazxHXDfK0B-bf72_O2Imkq_Lo2pVOQmtPy3TQPRiwrIm_6C8hyAvJriCc--zraTlYds7hHQh-7mYdPX-AyO19RQcNAxE3C6N-KVHOUe8Ta_C2th6Pb-nlokILuQ-WAp4nHGOI2_5o4zVLH_l09F5GOqHYoX-ZLKzf2IWwIC_xns_P09QDYeaNDUjvZhcWLVgIsgcsk22vHzf7PrzS0Ur4aLh3xuESRJ8Sbuf-n9bYoK3zw4lBGJAK6Ok1A4CAtgS1uD4nCvGti_VCI1I2U9ty9cewRyA40KmYokNfyOBoOxa2DzhX0HrcZWV6wB6wAPLzFgm-4aLIG7PGzdifTn9XZeqcH0ONUhCQRi12sfYV7dSe4zLjiqONAszx732sd8Xsayz39oxDxuTJU7tZaFalBVh-olJ2IdlQI9PCVnw6m395Y9YwcEKnqrPs_tN1MSH6qHHr-uR3gRNBySHxY9e-7ffhqH-2uwRMkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=ZbbTfJ_mQbzCuht6OQC-wwPebncTBGnNnDFXlCp3yagduGhVH9p-dg7BfwaPIQPJTgjOXf2sMsaV0oDSk3XqkkaLfxdN2TAzqkBX2TpnWCzcWMjKGLasf5QaNO-Vn6PGxu14cSR4ZAr6tJX03cptnUaPUo_-TV31H39abyJi3gWu3Mw1Y8JvKeZgpUuMeHbwbfztjwojazxHXDfK0B-bf72_O2Imkq_Lo2pVOQmtPy3TQPRiwrIm_6C8hyAvJriCc--zraTlYds7hHQh-7mYdPX-AyO19RQcNAxE3C6N-KVHOUe8Ta_C2th6Pb-nlokILuQ-WAp4nHGOI2_5o4zVLH_l09F5GOqHYoX-ZLKzf2IWwIC_xns_P09QDYeaNDUjvZhcWLVgIsgcsk22vHzf7PrzS0Ur4aLh3xuESRJ8Sbuf-n9bYoK3zw4lBGJAK6Ok1A4CAtgS1uD4nCvGti_VCI1I2U9ty9cewRyA40KmYokNfyOBoOxa2DzhX0HrcZWV6wB6wAPLzFgm-4aLIG7PGzdifTn9XZeqcH0ONUhCQRi12sfYV7dSe4zLjiqONAszx732sd8Xsayz39oxDxuTJU7tZaFalBVh-olJ2IdlQI9PCVnw6m395Y9YwcEKnqrPs_tN1MSH6qHHr-uR3gRNBySHxY9e-7ffhqH-2uwRMkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoeXeWt-fM3wO1_YGZjPUNAH-m2eHX8GGN4NArqcbDUanyS2YhaX9hHe0YPULBDOW_akNJcpwFF9NC8BXXchhOVC4KNfYZNlNiR927B2poddo3vVK53GEXgvvkbYGy3nZkQtEPNj-BBx37LX5O8ONyJ9yz1OgZtw3zNs3vdHyH6zfT9wPnuI_AC1f6KwXx6deMpHMyZrWfvsYsIwLRi2M5hSbtNU95_soW2aOgUaQ2infmzmi3CkHH-OBL-gEX0wSgiJu3T7HL10LgXJIFbmDfeK9lx5qFsDkqM1owBiHJ3MXO2x29G82DukU_a8ixkOJrFnl7Kyt85vPOHg_gw0mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dT3nIVR56WlMseuPaFnpT4Dljlc9b0JT2Q_dIWGguqaT3nZiQB29MSqwJTsZFJTpubutWzE8q2n4XZ7X3mpBuyP3ZP1jw8JpyJ8zyhDxSQ-RChlzoen8UiFqr6UdONy9j7zT0KRUvTjH_aO1deoMm61q9Td13TXRSnIkZ1GsvjcX38_M2xXkQ_0CpOlkeDzr9_pPZM-HZMhit43ArwGvxJ9Afm0oLhsA2dM1zNBWOMJpreVCXbeR_c8fCXMd0lZCKjxSqnMSi_IjcOlJpZdcUTu6JEBo0VZeE100i0Wk9Zr7xh3jE4j-K2mHy6A2TEmteuqQkr9zocpw0Q9Z8yUdQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMEUcngMAMecKBGCz_akGoc2vgRna1c1EMs4pPNBBJvm3lYTUhoCg3S-mdZSiA5n20OVBcYH-hi8gzEwU7vdpxnGBfc2uQ21Vl_hkzpxBMCUWfUStpRIdv_IMiV4pFH4D67aZuL2DtuXgYopmkrUZUknxpVcPYaLmBnnrqE5a_yLvHF81ECkP6lbFTuF-XONPl9Hs5uDhqeY7VSz0KH-jNOudtVtzo7LZ3Z2GQZG73hI2t4OzDy_a5H7soKjmWdKtQ1rN2fHYUkAJKLGEN3qo5VWP1NPMOHXEY05H3Zasjy-9jElo17YP6fnjUF2e4XNKtbObaaSqpzxq2g9JttAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vF-1KgTWaMMjJwlu-Cj8D0izCFRmqzPGC2hLKEyRxH6gZ_Tz0vq3aMTHsN8Nde0Xwvu75USmdSz36AFBwHLNc4BuJiAGTTzoacJNK9r5dFnfnaigwalD5-zQa1I1QbmIxvnReYa8G5PgHl9bXXEC0Jiqo6BruFaJ9bEO47rkB7Z6RyXZscQDvxGQu1LGXyks37m0wPyGv_u84lwQCCihViUDJL4opwhBvqLrDLnuK24bmOpjOKceuxMfZRvGXBu3eMARrJ3lwX2R2PpUTrpw0OmdoNqN_5jSLUAEINtGadJfB_lkEb70OLD8y1jlWHKvPhiV1C0Wtu8l5Z6G7_mF3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vF-1KgTWaMMjJwlu-Cj8D0izCFRmqzPGC2hLKEyRxH6gZ_Tz0vq3aMTHsN8Nde0Xwvu75USmdSz36AFBwHLNc4BuJiAGTTzoacJNK9r5dFnfnaigwalD5-zQa1I1QbmIxvnReYa8G5PgHl9bXXEC0Jiqo6BruFaJ9bEO47rkB7Z6RyXZscQDvxGQu1LGXyks37m0wPyGv_u84lwQCCihViUDJL4opwhBvqLrDLnuK24bmOpjOKceuxMfZRvGXBu3eMARrJ3lwX2R2PpUTrpw0OmdoNqN_5jSLUAEINtGadJfB_lkEb70OLD8y1jlWHKvPhiV1C0Wtu8l5Z6G7_mF3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-6wYQ1qfLSdePcwQcP-V4uDHSXWQRMC8dfM05XgZqMMAuwYjwYYbEn-XtDOrDD-HdFIY-h0MXydUpPZ0_kGJVSqdyvVSH-ZOMe7F6-Rz__iRDmVn4BjqO3Xp3hSWxG4dHsTaAvONPY8bI-jfrhokM88KnJnl2iivMDobjQG_sRV3RrmftkVLZs4vrJqDgOICE3EVyFCGNFkA9usKKcQNhlebtv_7cU00kXW7l92n6lFbIZ9ghRbvp-H5NI-sSwgZMrnyqtF7UJLtAUgStVroiTbmAy2q2WarKP8wjoLbRx2UXU8rz7TnucaiPR2-_RbFF0r-Yb4-f6tyfdmIDOGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=LUnKtFHWSA2pU0gxjVrG9rDKRfZGB75NbF3g4dMvHofLtGLEqG90uem7OBNe5a2UiHs24LmuNyvbk06dZt_GTwpClyCa4ZMBezq71FpKKLcDWxz5VI21vu-lBTnoUMFpvNBNA113G8PsXmCq2vweWX_NEHVwEtFfSg7DEQJ0SZwsHFpsbBaJp48VGl6ZS_9qN0pDBKku9xb33NmOA5nBml1jAjmsiKhyKPENeUoKrfpN0DcA1SNijaMMMryRgeT-eJpsJ_wv_OEqFp8TIybJ_dNwidDnbXWVDSz5r-Dz9dcfq67i1UcgE2d86QO4U_0Caaeghrh-1gDpUHnZtXh5tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=LUnKtFHWSA2pU0gxjVrG9rDKRfZGB75NbF3g4dMvHofLtGLEqG90uem7OBNe5a2UiHs24LmuNyvbk06dZt_GTwpClyCa4ZMBezq71FpKKLcDWxz5VI21vu-lBTnoUMFpvNBNA113G8PsXmCq2vweWX_NEHVwEtFfSg7DEQJ0SZwsHFpsbBaJp48VGl6ZS_9qN0pDBKku9xb33NmOA5nBml1jAjmsiKhyKPENeUoKrfpN0DcA1SNijaMMMryRgeT-eJpsJ_wv_OEqFp8TIybJ_dNwidDnbXWVDSz5r-Dz9dcfq67i1UcgE2d86QO4U_0Caaeghrh-1gDpUHnZtXh5tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3Ls-ntBz-oEcYryFgEpSDm6hIiVSFLOkzw3Io0eGrFT4Wh4kD4MDA6M8Ad5eDAsmyM_DEiIsyLXYH6tVLxBzacG6mKixpATf1ReTX2kLKUmKL1Us7ZqYA6VgAHdqq4ISbMNBOx5WqYrIhUA2VF84NIc50zKT_pnVSq9CX8yU24eb491wLV01CvuVe7SH62YcyQf0IUmAAzF6_X5zuyc-doFtcJg3C_gWgxnk60ICxXwk_ESLKxFllp7XdkpYgDhW3cnZOM1QA3EYRxuY-ZpWn1EXFfuaAY5cSY7fsayRCyf2grbyLRttH3bTj8dS9uRVSYp3_bIqlv4kxP8wR3s4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2JR-MVjnnqbU8DJu-2er3pdTiY92r1o2WxijE2gFLokc2GBcXvVo2CQA85hc8DTuUR9xzhXq2xWXAK97Zf7hVgj2NpjN-yCGd1hgt5PChwl_QAbHKvtczAc0bXKaEgh-4dkdvK6L9iV97Yxwk55O2XdV129vg7HsjxAzbHYdSfhBhELTDPBdkd7BFAfV8xHpAc38oyEUGACPjGmLcrnsEkz9nCu0t4-JWs_PvzhZdPudVjnPMy9YjPnGfCVFzxkxtegcXGYm9E2zbBJRfr8haRd5wR9hqKss2ZW0j_RI9LKpR1DOJ4O6iKCiUOuS66eglPQpEV8RPMFJ_63uU2uzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=fufd1pXS0BkcH3c6N7oz1d-8pbmsq74jm8yPbEPako-x98-EKN-X34HZKRvfR0WsyBCJpHWwcYhGzhcTOOLd_d5n46xC5B-E-nzlIqxL9ZGx-Hy0nYVFWBJbfe3BI3yNAMWeZIUfuek5tR7hZuzYugiwwJ5EIpvbB1pMtawRUI_PMLZ1LBB_ThFuygK4E-VLNAsXuGa-z8AM4hZ-jokNpNf2CcDGpbSjC067g-OEeaPvJtf6-59DnJm8cgEpV1brKaV5vRZ3JfBIlUr0azWxDr1kD8PAwzUcHV8wmcnIQGeA28G5M3spZodQDNGIsn77XgQO5iMDjzZZ4hRmyxzDvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=fufd1pXS0BkcH3c6N7oz1d-8pbmsq74jm8yPbEPako-x98-EKN-X34HZKRvfR0WsyBCJpHWwcYhGzhcTOOLd_d5n46xC5B-E-nzlIqxL9ZGx-Hy0nYVFWBJbfe3BI3yNAMWeZIUfuek5tR7hZuzYugiwwJ5EIpvbB1pMtawRUI_PMLZ1LBB_ThFuygK4E-VLNAsXuGa-z8AM4hZ-jokNpNf2CcDGpbSjC067g-OEeaPvJtf6-59DnJm8cgEpV1brKaV5vRZ3JfBIlUr0azWxDr1kD8PAwzUcHV8wmcnIQGeA28G5M3spZodQDNGIsn77XgQO5iMDjzZZ4hRmyxzDvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=aFeZx7iLXgB4l9A7VH9_18EYUUL1mtmFYp60Bec3Khkpz7tSDJSgHKPOLtDf_JnkOrv4ygmmJ4UwZ3aCrcKOCLSt4RLekfCx1tH2jiJtlWI9zTJoale9VoEoyRTUyXumcVvGdYMF5DTbU--mB9UAzuWA-p-ZMLsmJ4SUtHOtPf2S7Hz7XwJShUpEp5ew5huQeWAfGVL5HbDZr_g6EsvyqWk_BwBtSfD9rVO-AErjI8ovgH7eQuREqD2eF0mGCWeNQBqE4-bnHKwwx_wjERN_Pn48yVNvBc-gF0ec4Bra99TkkCIOm-vuoQBmCsbwcxTVNBP-1k_ZSG2_WJEION6Irw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=aFeZx7iLXgB4l9A7VH9_18EYUUL1mtmFYp60Bec3Khkpz7tSDJSgHKPOLtDf_JnkOrv4ygmmJ4UwZ3aCrcKOCLSt4RLekfCx1tH2jiJtlWI9zTJoale9VoEoyRTUyXumcVvGdYMF5DTbU--mB9UAzuWA-p-ZMLsmJ4SUtHOtPf2S7Hz7XwJShUpEp5ew5huQeWAfGVL5HbDZr_g6EsvyqWk_BwBtSfD9rVO-AErjI8ovgH7eQuREqD2eF0mGCWeNQBqE4-bnHKwwx_wjERN_Pn48yVNvBc-gF0ec4Bra99TkkCIOm-vuoQBmCsbwcxTVNBP-1k_ZSG2_WJEION6Irw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=v4LL5Nez2EUx0f9VDWK__cizULjJK74chDyL26jKfUxqhCloMcgkYT0lkU0Kl_NLVphY5ha5Eyt1BZBCswlAsgHlo3WRNryxFOAbbhH6DBP2LXlGGrSI_icVwaDNZk_AIJIbI_bqaOtdMZVI7JEHUaMJXDnRekBAxLenKWTKfmqmqpVSJWyf51TM5JvyxCFksMv7Zv8HefwCwzyu23CyZooXxbHDx4i8bZyYGimDkYkf6HYzTAeKaWKTI-8R8m3zQ2jGiev0ZZPjpOG4M-wJuaX-BW2fQ27lJhySPOnm17MUUV01_K6yVA3x_BW-K39vMaDhGfkWkj807dTMjZsppxlzhL-cDwZC29sgECgOAxtVM6ha8RPBcrwhHwPB8gLGTNPcU8K4n3ozF_ZMARznW-xI4qBTXdHsOopSgnMw7oRBqx7V2hha3ji9cl6Ygz2m3Lrp4ybgpJzbpNT8UMNVcua7HC9WimczrOi2hvziEw4qAe-QqEyEDBsw5gbgVqhMYXgrDp75FyvVdy7tenPgb6xTsmKww73pnDBnj9KjVYU2eWVTJQBKWfVd7NN9hPHECfKaA6YWsS6GNkZQQGomfTbL6ilbnjf1Ao0gfmB2tnoL6q6taqQS4D3uZjR6EPDbHy4yUC7GcowGkdRW8NsOH3Vkc1566ZBUs2sccU64a2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=v4LL5Nez2EUx0f9VDWK__cizULjJK74chDyL26jKfUxqhCloMcgkYT0lkU0Kl_NLVphY5ha5Eyt1BZBCswlAsgHlo3WRNryxFOAbbhH6DBP2LXlGGrSI_icVwaDNZk_AIJIbI_bqaOtdMZVI7JEHUaMJXDnRekBAxLenKWTKfmqmqpVSJWyf51TM5JvyxCFksMv7Zv8HefwCwzyu23CyZooXxbHDx4i8bZyYGimDkYkf6HYzTAeKaWKTI-8R8m3zQ2jGiev0ZZPjpOG4M-wJuaX-BW2fQ27lJhySPOnm17MUUV01_K6yVA3x_BW-K39vMaDhGfkWkj807dTMjZsppxlzhL-cDwZC29sgECgOAxtVM6ha8RPBcrwhHwPB8gLGTNPcU8K4n3ozF_ZMARznW-xI4qBTXdHsOopSgnMw7oRBqx7V2hha3ji9cl6Ygz2m3Lrp4ybgpJzbpNT8UMNVcua7HC9WimczrOi2hvziEw4qAe-QqEyEDBsw5gbgVqhMYXgrDp75FyvVdy7tenPgb6xTsmKww73pnDBnj9KjVYU2eWVTJQBKWfVd7NN9hPHECfKaA6YWsS6GNkZQQGomfTbL6ilbnjf1Ao0gfmB2tnoL6q6taqQS4D3uZjR6EPDbHy4yUC7GcowGkdRW8NsOH3Vkc1566ZBUs2sccU64a2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPZLeYFw1JdH6_ZZWl05GUzKScSeAZOpWhwWuBEwvBHaliYI4RI8yU3YVZyrS_ukBxgz3uf_J9u4TRhpKhx0h5dh2HNZCGbT2nO2f3o1IhaKU3lRCNi-RZIVWFVyP5y8NWmSr0JD2gMOnhVgHoX09nZs9qhoDxu8Hv3nB4FeAA1pnS52XiX6tgjNb-PVfO91GfvWhJKEk-fOVjIB-lrcwW2BMs6lNpOrBswFPc7_r3B57vlKTkz_v13eROqUbfGEkAnemxndtpos_jXo6z217v9SnZdD37RXXGhVryLOMUnX9ZvheasZ2YnWl6zu9ttOoGMm1mHe6gEy6UThNSuimw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-QH5Y4rxFlMNexnBRQlAYs_YNcONUMlNc_1W-jN4FQytxUrubxkPUBgzkPM-9LKN7fAMiJ_k1DR-E-ByyvOpT_ZjCuvwR5UmgnQFMScViDSXUJzYKjgZ9Lp6nhm-nBsEva9ClzRbQYOF1lyNYVPNLUz3SSS8NJQg7y-PCWe0HO5823Fr1EayYMhQJSyZrwgegwOPNYtrvSiKdzoP1GO_nRvL-8Q1Psnm7OuCmq7Mw9yzWB-_PbBdkWJaD2SQbhUnfax9E9io6L-A8KMXZVm-jqvNLSc3l4LPJiuD-17C--iS-_eo7ZE_SWfrte8cAso-yYb2lzHspdsKaGSQVGS7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYUIdCShcvSr-nGLfvXIiOH2_HhDJgIF-HhPU8xzmhLzDhSXtCrnv7vwIfQQz3a-U7wYE0WSDoc4nE2Gu73IODkayEliGn0ehVFojohO5I-MJs_V2LPY764rhrcIvYVRpM3sOGPGDl25efWwJ5gh1UNfOReIiq4aPV7shFCgrFPoIeufrgXQ54eo029IoP5tf-2nrTslSMhkzW1TcRaaEuMoT-REXtrApI8V6217LqoXbxulPbrfl1sIT1QDutIiivDhmG30nfqkF5-logNfGynVm7qvy46WZrvY7WA0r-GHlPk1E-cN0chDRvlutD7oWkQkxrFvbvxCSAOVFTFZ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=mKiLIqvaW1n9EAIciI-6VSGRPYdcoXl1UBrna49_jGAfXUnUkB5zlkPrQquYF7ewmMND6fcM3fHTv_iNYXUfIN0bqIlQP4MPQxGnMemBYHv4yfTjNfdOf-2TwW5cQtwoQ6W0HXjrJLPEgGN3YdyqxEDPAIEmRjPlDbAPesPU6O3_OnxlOuKbVeoakxNe7eE8RetmlYNFwA4FmRfkzaqWIskn6XMK-tfuy-8_qRSRtNIqk_YXZp8ZGMeg69IcYkZ6f4aXWgFijaWlYeiDafxXGVltgvDtcZNjJVevoadtALZCkZxJ8eSRtHl3kyZ4aDRyZw5SsJWuwuurtIxJn8UEpYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=mKiLIqvaW1n9EAIciI-6VSGRPYdcoXl1UBrna49_jGAfXUnUkB5zlkPrQquYF7ewmMND6fcM3fHTv_iNYXUfIN0bqIlQP4MPQxGnMemBYHv4yfTjNfdOf-2TwW5cQtwoQ6W0HXjrJLPEgGN3YdyqxEDPAIEmRjPlDbAPesPU6O3_OnxlOuKbVeoakxNe7eE8RetmlYNFwA4FmRfkzaqWIskn6XMK-tfuy-8_qRSRtNIqk_YXZp8ZGMeg69IcYkZ6f4aXWgFijaWlYeiDafxXGVltgvDtcZNjJVevoadtALZCkZxJ8eSRtHl3kyZ4aDRyZw5SsJWuwuurtIxJn8UEpYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=k3PLlrU2JscYE38DhxjQA_g4R64zedOB27K48H-rP84z5amk1xOyahjv8_fYTNQp4cUOmilteoz4t8igwl9qfBIlrz8MZPB7BzMLQ315-r_LMhMq3T3_oTMlYsLfEgfl6BGDQV-H7AZXeFiuXCM2bNcNE4gtlSH9SVc_Tnb7VPpGb9lJr7oFE9HZLRuaC5OBbx0zxD4lcjVP4eXLyeNGMNtKbNs2r7aBJzizwuSXkwoV4aakwriQ8lB7aWnOgnF5cF2RgY0jGIIfltSu477Xds9Wxno7hiNNrhAd3iZ3QSVC0FhYfmq1dgzcVCklAK6-LnVlpV5B7mmw8UuhwPvB3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=k3PLlrU2JscYE38DhxjQA_g4R64zedOB27K48H-rP84z5amk1xOyahjv8_fYTNQp4cUOmilteoz4t8igwl9qfBIlrz8MZPB7BzMLQ315-r_LMhMq3T3_oTMlYsLfEgfl6BGDQV-H7AZXeFiuXCM2bNcNE4gtlSH9SVc_Tnb7VPpGb9lJr7oFE9HZLRuaC5OBbx0zxD4lcjVP4eXLyeNGMNtKbNs2r7aBJzizwuSXkwoV4aakwriQ8lB7aWnOgnF5cF2RgY0jGIIfltSu477Xds9Wxno7hiNNrhAd3iZ3QSVC0FhYfmq1dgzcVCklAK6-LnVlpV5B7mmw8UuhwPvB3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=MWMk60sqM8jaM0b0d3O8YjBy2pxbCAD8oyw0tLHRS7WQGUcGpQtrzGjS8-FwTkhBMSx-P7nR0TAHbWjNjINktu3uU_WJkULSjJs0cKcqFAebnofolL8P6B6GOeShjtUozATUsSnTemGOmqJMMMfPbkVon-VCuj6su8elA9sZoIpmM1y6AF4JwtRRmcKs9ZZ6T6_VB6nvJps_J2HyT1dNzOw4gtHBiE6S9DcE6_oKi-7UAhE9sqlqAg85AAbB6x0K1pT8YRi_bYkdDRyT3zIW1AZWE9FcHEasKc4iy0fJZ4uLgUarpZVLNxpYkRo4i37SVgYFT7tcurXaR_vuCgmMNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=MWMk60sqM8jaM0b0d3O8YjBy2pxbCAD8oyw0tLHRS7WQGUcGpQtrzGjS8-FwTkhBMSx-P7nR0TAHbWjNjINktu3uU_WJkULSjJs0cKcqFAebnofolL8P6B6GOeShjtUozATUsSnTemGOmqJMMMfPbkVon-VCuj6su8elA9sZoIpmM1y6AF4JwtRRmcKs9ZZ6T6_VB6nvJps_J2HyT1dNzOw4gtHBiE6S9DcE6_oKi-7UAhE9sqlqAg85AAbB6x0K1pT8YRi_bYkdDRyT3zIW1AZWE9FcHEasKc4iy0fJZ4uLgUarpZVLNxpYkRo4i37SVgYFT7tcurXaR_vuCgmMNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=NUJUNvAtF1VJiv7Xhtek7UKaERz3RWZTKS8h225kjqlTbWouYP-YKENJXeP5dukkmyKTAAG9rSEoG8vd9UYoI6mhWzbNaHUq3izG4jlknDVWFf0rX8UECgtzmrlf7BwyRMXCCuTfl2X2Fo7IJVzCTQSiU_LVtcimKvlNLWPlZgJO9TI8KzWfPDXRdINL3rB6gtE2AAxMFS91SEDoF7GNlJqI70Qv63oikocyIPMmLXGPMl6T5sYelroL2USu17yrBMv1f8RlglJNMXXhm4m94y_my4zKDgh7a2hApIqVLlv7WZhFTrIXA--Qxn9vZ6eEfsm8-pVrRMGH7r-T6nibig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=NUJUNvAtF1VJiv7Xhtek7UKaERz3RWZTKS8h225kjqlTbWouYP-YKENJXeP5dukkmyKTAAG9rSEoG8vd9UYoI6mhWzbNaHUq3izG4jlknDVWFf0rX8UECgtzmrlf7BwyRMXCCuTfl2X2Fo7IJVzCTQSiU_LVtcimKvlNLWPlZgJO9TI8KzWfPDXRdINL3rB6gtE2AAxMFS91SEDoF7GNlJqI70Qv63oikocyIPMmLXGPMl6T5sYelroL2USu17yrBMv1f8RlglJNMXXhm4m94y_my4zKDgh7a2hApIqVLlv7WZhFTrIXA--Qxn9vZ6eEfsm8-pVrRMGH7r-T6nibig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdCsl-FOLhwRw6W3t_6ZrEQ1OMH5hqFVjJ0fgow24Eer9HjC1kxjmsl8MtCulsu-MfNsx8amjO422QE6n0HuBg8Yp6YIFw1VaqxdNmG8cxku7T3ndEK9gu0X4ge711ozK5LfuspsjtfO6WpX6S-otHuoKTZYo2vis_VsY-vm960WthO-Cufv8EOsJd_tPM7xcN7YK-us3EGKXiDFHKSc9SszWiMqhw7A_5z04Gwp0lvly8YUdpMpD0Zvk15mZteaxCWtJJ3Uih2e2jK7AmUPt0UEtSBwgQ9uc9jQ_FPAAxUlW8FUQWDb1GU8Maj8aDGRbh_aoXyvkBFIDsd7nrmQFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=dqPR8Sj0LH5D6PUN0ioSSMbdec4jbbqgc-m7p3rK5cB43Qha4rD9Yl_vCFfyb9vjmn76-1WIRjUFAREvXlMKedQn4tsgYvQfPe14SHv21it_d7AJXCWsaiehoWpuzbYjphElQqoNCauhkA7c-XirQ_1HmndhiU2L1px60gfBpSruPsXJKTAoJAXMvChwvUW5tt7DFYTSje9dnZTtXvc7LUwYLnR9eX96RjcvXLvWkGaT7dDAHu33OJLZ9mQFU3_tWAbi41aVAQ39XQ-f-ki52ftFTUyrzqSCpytawvmpfbBVAHsuA_RHo8KPKhLoc_CIL_yMFXT04jPq8qm-FcuDOoM-QTCVlMe31La3yZoOEfukGs-aJ6yitovLBCt2QAlmCQmV8HZ1EVT34AUVETEtCLst5t0fpFXSkSgxSYKPby_R-aaQKZyTDUFRw8ajIxx0Vg4sSujqSE6LoywruhFB-UKtHAtJFk7Sgkjq_RbPqQ_8n5w8CBExxCEMTKrDzUtNtF7X_j5km0OGChmgl3GkHx6MMyTGz0zS_75mkM6LJQFhSVfeo1u_QCVnFmAdeHUX2Ul9SU__VoI0y0IoYPpCSECebaDUzZ-gcKzFdUk-iGkEP4qJH5K2ChwxO7-WtZOb3YtmqKVNFDAwrq4gt619LpPh9HTFuGSf6aJdufINGr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=dqPR8Sj0LH5D6PUN0ioSSMbdec4jbbqgc-m7p3rK5cB43Qha4rD9Yl_vCFfyb9vjmn76-1WIRjUFAREvXlMKedQn4tsgYvQfPe14SHv21it_d7AJXCWsaiehoWpuzbYjphElQqoNCauhkA7c-XirQ_1HmndhiU2L1px60gfBpSruPsXJKTAoJAXMvChwvUW5tt7DFYTSje9dnZTtXvc7LUwYLnR9eX96RjcvXLvWkGaT7dDAHu33OJLZ9mQFU3_tWAbi41aVAQ39XQ-f-ki52ftFTUyrzqSCpytawvmpfbBVAHsuA_RHo8KPKhLoc_CIL_yMFXT04jPq8qm-FcuDOoM-QTCVlMe31La3yZoOEfukGs-aJ6yitovLBCt2QAlmCQmV8HZ1EVT34AUVETEtCLst5t0fpFXSkSgxSYKPby_R-aaQKZyTDUFRw8ajIxx0Vg4sSujqSE6LoywruhFB-UKtHAtJFk7Sgkjq_RbPqQ_8n5w8CBExxCEMTKrDzUtNtF7X_j5km0OGChmgl3GkHx6MMyTGz0zS_75mkM6LJQFhSVfeo1u_QCVnFmAdeHUX2Ul9SU__VoI0y0IoYPpCSECebaDUzZ-gcKzFdUk-iGkEP4qJH5K2ChwxO7-WtZOb3YtmqKVNFDAwrq4gt619LpPh9HTFuGSf6aJdufINGr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=l7ndPaSPHoHIdHo_f-W-ctFcWT4eUrT1t6SMIcbd6yFdg4bGYt41RFLqNKjeDQotkTJxGvc3Q5Z7EwPxx3GSCpjjgH-7df_jy5HQOJINWAql4tK6NLd7GNO2Pd35mhMs6goStsevL_XoqfGO_60n5JTtnmau5MZM9XkTyygnfqJ6mEBVFiKoOdetfKqnnmUWPS2FZ_Msq2U5TsvD84xYPfozhm2on_5UrwDwavE55sgyL5sKOHMWP6q-UaoMVAmTNF8xYSDbGSJzmvGPuHoiz4EM-O2HJ3wsmxKda4WkZeO36TqIyD1fkpl1e7XdwLDHUxbfKCtxc5x88vtVyumw3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=l7ndPaSPHoHIdHo_f-W-ctFcWT4eUrT1t6SMIcbd6yFdg4bGYt41RFLqNKjeDQotkTJxGvc3Q5Z7EwPxx3GSCpjjgH-7df_jy5HQOJINWAql4tK6NLd7GNO2Pd35mhMs6goStsevL_XoqfGO_60n5JTtnmau5MZM9XkTyygnfqJ6mEBVFiKoOdetfKqnnmUWPS2FZ_Msq2U5TsvD84xYPfozhm2on_5UrwDwavE55sgyL5sKOHMWP6q-UaoMVAmTNF8xYSDbGSJzmvGPuHoiz4EM-O2HJ3wsmxKda4WkZeO36TqIyD1fkpl1e7XdwLDHUxbfKCtxc5x88vtVyumw3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-uYs0-mIPS59HzfqBD7rsWhp_FHYpiu6e4GatU1o01YhJUmBIeU9ioRp-j5OootWhKCd364SVbGRZdbarA5VNPeSUOakbbEgLN00b7TZMAbbHI51k3eEELd_0kb5VaYpVa8Ax5cfdhAxhJb8bQvgDZ0GSdDeM9xRAfoG_2ELqdaC5D5YjbM67H6SHj8XIavBfvn_PapUprTkjE4K21hdRT3GhO7QsR3yxqs4NF41cOLiYg_5p14G_2xehQHglWbfgnNFzM7v2a98IG6W6LfnyWBsP4iIRHk7JY74HcQauRAh1wl-DU-IrWfXi9fBB4qtbzj5yqSVZKKh594iKZIfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=Cox63XfSoBnkTBTd1CFThjV0CYD5vZwH4ciL_aUUwQCO-6ri0tnkEDwvA3vqIlXR0dgd7dQsjB0C2FHZWHOophgL-eIRwcbDQh7cP0lwdlvSc-b8tRwSHOevxKYR2Gf1V-6uo2YU7rpMmTt66cDupDZPiv9L-r0MlYCkg7b0_dD1BAQAigeqePQGPtwe02GA-uAjJ0hhOAgEWE-IrdU7_hK4TWRG_LAz5z6kFXitFHNQ8L7PiPVTDYMQKO9DnXHDEbcDXiUBwcPjmetVvrCb1RZ6tM5NJv_RJp-1mgBrAAI7YU960EnrDB4Ey9xxAQLHQBjDB-em8Qyltg7Rdf_x4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=Cox63XfSoBnkTBTd1CFThjV0CYD5vZwH4ciL_aUUwQCO-6ri0tnkEDwvA3vqIlXR0dgd7dQsjB0C2FHZWHOophgL-eIRwcbDQh7cP0lwdlvSc-b8tRwSHOevxKYR2Gf1V-6uo2YU7rpMmTt66cDupDZPiv9L-r0MlYCkg7b0_dD1BAQAigeqePQGPtwe02GA-uAjJ0hhOAgEWE-IrdU7_hK4TWRG_LAz5z6kFXitFHNQ8L7PiPVTDYMQKO9DnXHDEbcDXiUBwcPjmetVvrCb1RZ6tM5NJv_RJp-1mgBrAAI7YU960EnrDB4Ey9xxAQLHQBjDB-em8Qyltg7Rdf_x4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=vhKFhiLEkmfz99W9S0UeWYAkE41hRq754ofr9uZpCHnyaepaJizxmvo7Cr0Z-szUffRu3VmXbgjmKFWAG-r3ietOKfLWU6Rt9h2ZpYc8SS5Evc1Dw4zU2Rjd3dwaOx8M5pqO378OnkrxnpADMH8ScWGIRbZGzBdtXUKjS_kCGgI_JGVf3BOZTA5sZ-rMWZX7_wgQBf4zu50AstCOtuIisnpy6GDcdVStVPpURLXQbA0r2n-nKn85_dP_HwvBpV6Nrm4CZT3IMxsLaCWGpp8wJ6X0Gotpsb2m_lfEg92SKkvuy-gfuS_aE2HBvmVHleN9PqrgwJJjGgMC3-s3FPC-kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=vhKFhiLEkmfz99W9S0UeWYAkE41hRq754ofr9uZpCHnyaepaJizxmvo7Cr0Z-szUffRu3VmXbgjmKFWAG-r3ietOKfLWU6Rt9h2ZpYc8SS5Evc1Dw4zU2Rjd3dwaOx8M5pqO378OnkrxnpADMH8ScWGIRbZGzBdtXUKjS_kCGgI_JGVf3BOZTA5sZ-rMWZX7_wgQBf4zu50AstCOtuIisnpy6GDcdVStVPpURLXQbA0r2n-nKn85_dP_HwvBpV6Nrm4CZT3IMxsLaCWGpp8wJ6X0Gotpsb2m_lfEg92SKkvuy-gfuS_aE2HBvmVHleN9PqrgwJJjGgMC3-s3FPC-kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzNfMC95EuuJfsRygFJ5upWTJmrzOC5iNuLh1_8NqArAE5SDqR5d-2sC7MeyOpnl9vXoIKBuyaJQhlPza4MbeuS2Nb4ikZM0r34Hk5BPSqh5Lp02qCMKWaXocev6emGV5kdHxe6rNXECrjUEfDNXwJk55bcRwiDTsOtCOZ9EkJXDExEzuadkFu2ac9JUh2oKqHtKp8pdpUUrmDCGFKhU_iX28pKf_MExI7V9XWptWjPicMg2C8T-YtZUDUj0iQEAXUbEipcgHrRvlyJ5_XkQwhqzBwXWyye49VKgcYHnjgefOd_sXv8htD2-y3IZkO_-oUGOskUAi9REFKzjEXpYZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=TAD1l8x-nJtBYIL4WSbes5jc3aip5GnmIBbiWQeHdT7CNa3XkBNqZC1mghcl9MbE_a5sazgjwl4SwIIMFzb3CCTl8Io2EccBWrCa-gx6SXSjrm31i5N5fVH5zpNDtPxmBHU_As4FkkpyGcw8W2B6UNJfPsLaJG8lUPDTqzDmWG1-V6xsu_2XcXB48QsaGNN1FJch8v_p7OQ9DaBnQ6zZlWnd_UTewX1Y454Io5LV1TmI6XPUJHUZtpI4-YTyn_nl6iBkSrXfCBg4t3d09qI3KVOM-qw97eVaUJp2GvrPogXDyks2hWCg_uhumSF65M3LJjgc3jEAvkBn53sll9SDng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=TAD1l8x-nJtBYIL4WSbes5jc3aip5GnmIBbiWQeHdT7CNa3XkBNqZC1mghcl9MbE_a5sazgjwl4SwIIMFzb3CCTl8Io2EccBWrCa-gx6SXSjrm31i5N5fVH5zpNDtPxmBHU_As4FkkpyGcw8W2B6UNJfPsLaJG8lUPDTqzDmWG1-V6xsu_2XcXB48QsaGNN1FJch8v_p7OQ9DaBnQ6zZlWnd_UTewX1Y454Io5LV1TmI6XPUJHUZtpI4-YTyn_nl6iBkSrXfCBg4t3d09qI3KVOM-qw97eVaUJp2GvrPogXDyks2hWCg_uhumSF65M3LJjgc3jEAvkBn53sll9SDng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8sjqC12qhznGafRkcbPmiW2aSFyLeLp3kTTPEK2aLCIYPUw2fk3mNA1xxeDobiaO5VqFIqsSVx_DFEtqXJxXha8MWD_KiohYuzfa4dqeows_edVllXXroCI1FhVGtyofOJjjWRYgycn3qN_7hKDRs89aPlVX477mrkIZfFJDcsmqXnYgXnGGrgcvGXZTSlt01JUD5dVPIFqwNWPf-hv9fV98aieZfU6hMh-LWUKB5V7Q37Mbl6mj1ZxF_zj25V8Vrl2M7eDGcEfz2iiY6nNgHHr9-qOkNLVzSpRf365OvWG14lAiB_sUQ8YXk_OVpKit8brK5EaTwCNrRcvE-qsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=voVE6U5L9ungniCiyog9qrjTsu8zop_dBbigiw4yHfE47RaVAQHcIdcOfiBPSITTs9eJvi6fpcZUh24_sQJwerrXzwjVXVJSuz0R2sj0BgacLlMF0hbyLpxZoYBJsgqUXfCrcN-eYN33PJcdTT7g8GpMhdJju_VGDIQi_e7SAulx3oIwxSIRph5tnZ9gWZo4EhP0or5uHD36a8t0XZhH_AVcCMNwg2Hvti8dib3EJtzRQdfm2VVX_AFcAgz5K3laKGYD3CTbSUjpBpqwE0Xjc3gUa07bNFLq0WW2ms1kkKJpFZnz80rWOLn4DvJvwXrS_VUlDkUuKf3wEJEhjGkDyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=voVE6U5L9ungniCiyog9qrjTsu8zop_dBbigiw4yHfE47RaVAQHcIdcOfiBPSITTs9eJvi6fpcZUh24_sQJwerrXzwjVXVJSuz0R2sj0BgacLlMF0hbyLpxZoYBJsgqUXfCrcN-eYN33PJcdTT7g8GpMhdJju_VGDIQi_e7SAulx3oIwxSIRph5tnZ9gWZo4EhP0or5uHD36a8t0XZhH_AVcCMNwg2Hvti8dib3EJtzRQdfm2VVX_AFcAgz5K3laKGYD3CTbSUjpBpqwE0Xjc3gUa07bNFLq0WW2ms1kkKJpFZnz80rWOLn4DvJvwXrS_VUlDkUuKf3wEJEhjGkDyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLX1nLx9CjgaZpO7BfQIuIJhe5tr-JAb9fchZxZkM2OFamsGjGtGX9TMugA7FPUmRSvFr0sOmn0ZW-Dou1W7XTERFsPyaL58TERvi-T7XfTv3xQmekfVL2OAeZqSZ_dewcR9ywSxtyB8OznjSDKBpfCCekXfAPVNYSvc0dRotUjtOCqWjEmJA1VkIIR5-pMLTIHjgx_8Z9NevgMvAT_l8Kihg2qiIVrG36eirK93DkAqSYgytysgnZnaxr6U-MuMBigBENBhxXdlOY-Oi_rQvhAXplVqSJ4mucnVMFmKT7JKdxIj-qabWY-MzdwDdgNFcLx-ZZwXMJQSynqntWbOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=WunPfEj6BLW-6NnF4rvX9vmsAtKgAGnmgFL_nr_ZGnvfIwh126Zwzyqv8DYAK_uJ8jSjz7vGvONLzfT1Tjn_Erhpo9u259wEX8wXyTJR0c0egRCVDfMvIqX3NWuVW8RQ99nh88wMxUky8GQOPSRpoL6lXIVqrEMN63BA_DQfQARagT5emDNTvJhfUqQNu4mWf3DAxWNrt1Z06JR_ofcC5h61-Ewi5G3b2xLUKW7R8V8_w7kH2PbP0KyNyijJhtrQRmX1Q-Bu408TNJTQINDQdLSq202grYMVuamg9BVe6FrPW13Y9-R-00AK26EV7pa2DHzWKsLNq-_jaTPSkIS-xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=WunPfEj6BLW-6NnF4rvX9vmsAtKgAGnmgFL_nr_ZGnvfIwh126Zwzyqv8DYAK_uJ8jSjz7vGvONLzfT1Tjn_Erhpo9u259wEX8wXyTJR0c0egRCVDfMvIqX3NWuVW8RQ99nh88wMxUky8GQOPSRpoL6lXIVqrEMN63BA_DQfQARagT5emDNTvJhfUqQNu4mWf3DAxWNrt1Z06JR_ofcC5h61-Ewi5G3b2xLUKW7R8V8_w7kH2PbP0KyNyijJhtrQRmX1Q-Bu408TNJTQINDQdLSq202grYMVuamg9BVe6FrPW13Y9-R-00AK26EV7pa2DHzWKsLNq-_jaTPSkIS-xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqpZjL0lo3mS9Ru1juSxymar4QOPGxkMLzTrRGNHNzNpAINl_bxFgwxoDyxUZbQUM7mEggtu9pg_IYQmeqq5BADb15HkK7-_jFP2o8NTeN8yPnf8FqTxmN_mTfMaodic8f43IMs4YTMTBSgyWTo4oMMI3nuj9wemAt9RofLkCVEKNBpgh6G5Qno0YkK06ZYOXjUH3EckxTMWuL1Bi6aEaM9TIbcBNkKmpuO9IreWML5jaEjOiimBZkEzkKjSz5e-3ocI-oKYSmoENlVvhwwKjsvDGgbtbwYR5xZS2dHqru9-q5TDmCSVzaqtN7rtLJDqnuwkvAZLV0At1ZSLiofOI5H0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqpZjL0lo3mS9Ru1juSxymar4QOPGxkMLzTrRGNHNzNpAINl_bxFgwxoDyxUZbQUM7mEggtu9pg_IYQmeqq5BADb15HkK7-_jFP2o8NTeN8yPnf8FqTxmN_mTfMaodic8f43IMs4YTMTBSgyWTo4oMMI3nuj9wemAt9RofLkCVEKNBpgh6G5Qno0YkK06ZYOXjUH3EckxTMWuL1Bi6aEaM9TIbcBNkKmpuO9IreWML5jaEjOiimBZkEzkKjSz5e-3ocI-oKYSmoENlVvhwwKjsvDGgbtbwYR5xZS2dHqru9-q5TDmCSVzaqtN7rtLJDqnuwkvAZLV0At1ZSLiofOI5H0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUnI8KIKvfWjagpqS7warkbXI1Z_C7g0qITzhMtR-CKa4IIaNODE9nu7yrsBbJh4zlFW6SGEF17JPk913bNzBPR5ToFZi7mCGeip2HrD4l0xIMnpY_bGWL2jgpireVhylED27vzIWCxGBqQ7dtPmH0hqdPE94xwPjNz5D-6l2OWK-H0nPXcFFNsw-VZz7GLqNyJJQ4HgCwUFaXF8hiaBqGIb2LiVzA1KBIpht5PAnfbnLIXJXdVygekxMzndFewi1qaBb6fCOfhBZS6hNzFA7NowQ1nbmRVERXF01T1DGytpFuQXsugoW9AoGG-iuOMIeGs47Vf5tIAhLWU9JbVIKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=iPVst3s8cKBe5s4OlHfTSX6VkcBewQzUmQspyFKlphoRUkQrZUfgF_kc-nEe20r8k5Yu8vKnGHbKoA8nUwsfcrHDklQyByksZgWlyZ0FgEIGyo0XM74810tSH1pcY19gYc0YMERstFB_C0Gq33yiLRV7uBOaZwMCCN3cHPet8id1zG2wOSHibaI5ZCcfliDhB_i9Shob0DtHRljpJsFDpYuzlqp0laYjevLtN7udPDPsd5-8idWkOwL_9ocAuS8m-lIuL9EFoffWzZor-iNSS_ybLN39VUG06sGp2w5uHJ8KxHIkEkuXTpMESd2oECL222x5Csz1puM4Tg3LI4i64A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=iPVst3s8cKBe5s4OlHfTSX6VkcBewQzUmQspyFKlphoRUkQrZUfgF_kc-nEe20r8k5Yu8vKnGHbKoA8nUwsfcrHDklQyByksZgWlyZ0FgEIGyo0XM74810tSH1pcY19gYc0YMERstFB_C0Gq33yiLRV7uBOaZwMCCN3cHPet8id1zG2wOSHibaI5ZCcfliDhB_i9Shob0DtHRljpJsFDpYuzlqp0laYjevLtN7udPDPsd5-8idWkOwL_9ocAuS8m-lIuL9EFoffWzZor-iNSS_ybLN39VUG06sGp2w5uHJ8KxHIkEkuXTpMESd2oECL222x5Csz1puM4Tg3LI4i64A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=Y5yC-nk_nd4HAPW7dzbN6CZcGvLUcqqqxToMGyUs99bRTv2ywoWw_SyeCl6BpHbiONvvhPrK-YoQ-pbEj4VQAJ1U5ZG0tQaA1AUupK9lXgchKxwGkaslfnegTYN1Cnp1zPLBV11pJ_5z7xikFNRPDD9NIKzg1W1bwNzR2dqyGreWk6OWvgJZ-qNrcfgok_jwPwFwql1YkWLZ7bGfegWU-6dPu2sR1ogDBi3OfEuFo0PsqKtPiKeLnW9SWCdKvJUDh5SCBXpPI94yFigQ7wgDWeJ1Eo2wzlTocfXo5rc-ZuoxZrJOIleY3oo_hTaYRxv86nCGEQpJ8_bRKl7Bn4xScA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=Y5yC-nk_nd4HAPW7dzbN6CZcGvLUcqqqxToMGyUs99bRTv2ywoWw_SyeCl6BpHbiONvvhPrK-YoQ-pbEj4VQAJ1U5ZG0tQaA1AUupK9lXgchKxwGkaslfnegTYN1Cnp1zPLBV11pJ_5z7xikFNRPDD9NIKzg1W1bwNzR2dqyGreWk6OWvgJZ-qNrcfgok_jwPwFwql1YkWLZ7bGfegWU-6dPu2sR1ogDBi3OfEuFo0PsqKtPiKeLnW9SWCdKvJUDh5SCBXpPI94yFigQ7wgDWeJ1Eo2wzlTocfXo5rc-ZuoxZrJOIleY3oo_hTaYRxv86nCGEQpJ8_bRKl7Bn4xScA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgAWvEdHtzORNLz5wcZgOCceCzcKNdvAWAsjHhJS0Zk32DVfDHkkKVwnWpBySBBLiNR2po7rR2-7lUwiz2X6qqYmrfFSx7Va0xsmMIsEkcPYFIrGGzIYQKzbPcPM6OjY_krU_8F82jkNzDPmzq4My6zMKhfIM1XJ_LmThsIlDMEJWZKCOhcL4-ax-_DBtrK51UXwX4uvD1OLlmOMHnGdrg5zPxYJXysjdNBVmNccH3ADykXdAHXvWxR_EZYLLCQ_unNGpEMYyHswmfGe6pMVbE6UlTvu_Sj8-CVOA6SnvrdPzYYGxTRW3kmnsJujfo1BzbW6vsLuTSkiu4PUKV5XcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=n2D-e3hpS4Ga39b2jtxVzXV5WjjrVH-wP_5Sgv5XGzkfw15K3sExtFnf1tVBGF8hwKbwl6pJxwhBHQMsJYHKZIJyeyxuFSTNmg_yUBVC6exxArgUxlkGQOhUT8qivilJpOTFziEuO5AIzfmU3Vod3IPXXKjTHIx45Br93ZiU24-gNh8I-HLQaQ5g_Qf75fG0wgAUPmO-SUTxug1Sduwh9tmWvkI5G1Ip2tnmNvAUF0dmMRfYWIChZV5LXaviSLlz4AZrH9q8RsqpDFLmtQ5TXs7OCB4Uu9Kdi0QRKXCEL4Dj8voXiX_xAvsABftnxIJmrDm7cBnvdzNVi4ACXMCtVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=n2D-e3hpS4Ga39b2jtxVzXV5WjjrVH-wP_5Sgv5XGzkfw15K3sExtFnf1tVBGF8hwKbwl6pJxwhBHQMsJYHKZIJyeyxuFSTNmg_yUBVC6exxArgUxlkGQOhUT8qivilJpOTFziEuO5AIzfmU3Vod3IPXXKjTHIx45Br93ZiU24-gNh8I-HLQaQ5g_Qf75fG0wgAUPmO-SUTxug1Sduwh9tmWvkI5G1Ip2tnmNvAUF0dmMRfYWIChZV5LXaviSLlz4AZrH9q8RsqpDFLmtQ5TXs7OCB4Uu9Kdi0QRKXCEL4Dj8voXiX_xAvsABftnxIJmrDm7cBnvdzNVi4ACXMCtVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=iShV88w9Qdj74Wnvg_bVQtliusZSRShW28jxh175b9stX7xhrBWgruwXbKBtq_l4SjYqK7snhpgahbpGIyL6mrAqYJc2FHZYG0PVbaZyjKi8QiSOjO0gkKLgz0fojqI4JLQUvuHjO12KCSHsaA4583TgVoHc6kvFC-Cej24pC2MihhRkMxwl5UUm2lcUVn5LKk0UjOgY9gPDkfH-anhRRxhGb640rgNZLD7WZH7Q5AjCC9__HDLgHyT1jcuMz_uEcwFD0NxQQi4jgyr-hyqJdirrOg6vL3bouNwTwdFb_v-G1zo5RJZExobPDqpaurB6HlAX1ichBIm5_-tgTKI6Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=iShV88w9Qdj74Wnvg_bVQtliusZSRShW28jxh175b9stX7xhrBWgruwXbKBtq_l4SjYqK7snhpgahbpGIyL6mrAqYJc2FHZYG0PVbaZyjKi8QiSOjO0gkKLgz0fojqI4JLQUvuHjO12KCSHsaA4583TgVoHc6kvFC-Cej24pC2MihhRkMxwl5UUm2lcUVn5LKk0UjOgY9gPDkfH-anhRRxhGb640rgNZLD7WZH7Q5AjCC9__HDLgHyT1jcuMz_uEcwFD0NxQQi4jgyr-hyqJdirrOg6vL3bouNwTwdFb_v-G1zo5RJZExobPDqpaurB6HlAX1ichBIm5_-tgTKI6Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=vncg-GjKDXC8h818hmOugYd1nLp4UnER0CynuatvoIU-FpgJniUuN4xdifZspPeBcgY6XNyZE7FKjjOIy4DsPM_LUbo-_Fg13uvdXcskcixL0LSnsW0HSnax19Q03tyeYmc5_qa0HikBCFs9WxsUzeb1Qw44JS-Ur3h68qj-FBduYiPaBhWtAGMO3Aj1dgq_smXopYqANh5Vbzbt_opq2OiZQdf7HwebDIwNOLicbj-tx94c9YOA3h40fZNoIqGpvEfuXMjqNMels3_FoVQi-YrElRvfV1Jn__h6HFfeyOWAXVoRlpUjtD2eUNbzTUscU86RmAGFmoEbBofbZunyKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=vncg-GjKDXC8h818hmOugYd1nLp4UnER0CynuatvoIU-FpgJniUuN4xdifZspPeBcgY6XNyZE7FKjjOIy4DsPM_LUbo-_Fg13uvdXcskcixL0LSnsW0HSnax19Q03tyeYmc5_qa0HikBCFs9WxsUzeb1Qw44JS-Ur3h68qj-FBduYiPaBhWtAGMO3Aj1dgq_smXopYqANh5Vbzbt_opq2OiZQdf7HwebDIwNOLicbj-tx94c9YOA3h40fZNoIqGpvEfuXMjqNMels3_FoVQi-YrElRvfV1Jn__h6HFfeyOWAXVoRlpUjtD2eUNbzTUscU86RmAGFmoEbBofbZunyKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=uqvev6l3oQtctRU5pJoBx5_4PTsuv7KvXY6DJpT7kjMH9xHD2T-FFhcakGyd-NJIZDShGANm4c6crbYCXnHG1X7vikqQl5EyQpDmYZO7k1K7cCyuLeCwXsWrsHjAJID2vQ0vQHSIfwmKqQDcDylaJsQV4xgZQDUu0mf-4RuLA5ajd6mtYjhrFXIJZZACTWcrviZViKQ1VKSL1Jdpa9EoSEsfgJEzTEjPj_wpNA9iCDSKGqeJe5s2Ic8QYl3dBf52_-Xvx1smoZULvMrpTfLLzQlaVyFFTENZ5ja_VOPIQRX0x9RpHrsd1IAXZzU2QU5oOTdKEMYkk0ynuRrdvRL5aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=uqvev6l3oQtctRU5pJoBx5_4PTsuv7KvXY6DJpT7kjMH9xHD2T-FFhcakGyd-NJIZDShGANm4c6crbYCXnHG1X7vikqQl5EyQpDmYZO7k1K7cCyuLeCwXsWrsHjAJID2vQ0vQHSIfwmKqQDcDylaJsQV4xgZQDUu0mf-4RuLA5ajd6mtYjhrFXIJZZACTWcrviZViKQ1VKSL1Jdpa9EoSEsfgJEzTEjPj_wpNA9iCDSKGqeJe5s2Ic8QYl3dBf52_-Xvx1smoZULvMrpTfLLzQlaVyFFTENZ5ja_VOPIQRX0x9RpHrsd1IAXZzU2QU5oOTdKEMYkk0ynuRrdvRL5aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=RawNKpSgBl2qUaQgQqTfwgNvA3dI5rcU4stiPX5He-YofWQ4zSmo1KYjDtrM8cTak5azyeHGC-xg-sa2Lt4Aw8pu4BSN_yoH7svrVmPgASJLkrj_mr7_LC6ELFMz6WnsO-SnZPbPcPkI-Cj-M8EMRjF3Oh-GmLAWVtkp_SL75pkEl-YCan5y0QgAk9D5k-afT9ezL5cSqyqwkDcnFV-tO1LdCNHFKp2jqMOWr0Gj2pDINBDzAI9eV0D_7JMMm1hqeNhUA61gfxXIY4LQtLaW2BiVdOIIJ-HDjo_5SV1SBVJoQAyA9MnIGt9DdJVSm1vq5aaiYhggirn957lSou5bsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=RawNKpSgBl2qUaQgQqTfwgNvA3dI5rcU4stiPX5He-YofWQ4zSmo1KYjDtrM8cTak5azyeHGC-xg-sa2Lt4Aw8pu4BSN_yoH7svrVmPgASJLkrj_mr7_LC6ELFMz6WnsO-SnZPbPcPkI-Cj-M8EMRjF3Oh-GmLAWVtkp_SL75pkEl-YCan5y0QgAk9D5k-afT9ezL5cSqyqwkDcnFV-tO1LdCNHFKp2jqMOWr0Gj2pDINBDzAI9eV0D_7JMMm1hqeNhUA61gfxXIY4LQtLaW2BiVdOIIJ-HDjo_5SV1SBVJoQAyA9MnIGt9DdJVSm1vq5aaiYhggirn957lSou5bsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyUXO9U5MyK5vv7mmsNd1RiODA4KpWmw0agqi8T3K1l2v6EasKrzEkMV6Fef6gU07U0mt171dDHYSW_HNMXT3EWy7epDRaZvSbYuI-AitJ26SGRV56AsLracnuuu7I84dTtoCtRQJ8m70EdBetqU4E0i4U9b8-5zd7OTHk3nEZcBIfK7KZStW4Wtv5keaQkGyrrBBj1xG578AD-8g50qUjmcsT_3WR2T8Q0Vxi1aRdwSgi6X_oc3oPpYGc084o3DmFOuI1TiVvzi4wG9x-g1A61XWCIbjqUuQQqBJ3Nbf80jYa4hEXqmq_pmTC_qQ1T7t5XYOHL-qz42uZoBujiAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqs0cILQ-y6lHaJPF0dsfc7DnKR067Aswx6x70O6kGvBPyWXTrw9O2DNUMtQw0abh8o2GstzJoqglufiGSEaW3vuPmTGE-6MxSWrGJPQaAs04Aqz6JOq-AlyJTOBh6QsLkZ-hrJR4RhIzvp-goFcUjd1VZUDPjI84zsq5BFXAMlBSeqxyKOzUTG8I0rH3ts1EqOZr6oa_T8FxUzhM_vXC8CkUn8Thdq6KZSyF-t2LK5gVQc0oT17tUc0BHGHJbfHLmVFedyOi6GOVtDUs0IJCDhRl4JdXfLlswBpEyb3xSblqLz5Bf3udGvYTUYh5lleUEsb3SrtMiSv6-05KV4FlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkYOKEsklIezFZ_wX6Zkg5DhQPJ1fqUt4I0tTUteCzwkWW8dz47tIKib7xjD1kWhl86yyDSV87mqJP-Ls46pl5IHxEu37HQwQuKWckFZD3rEPjnNUu63MACj8pP7oF7TtrxNuHHOnKPV0FIrxtVIKVHyoVNPNBYI0o4CK766untzNHDTB4nKT11hH4dIEoAPvPQO6m_Dqou5bBhEyT8bxujKaRsWKYJoE9G7YFh3Lud0d090AkQLkmCutDkKFuzTguKLlLO1ljnxp3z4GW_RrKMUeVCNT3F3AdXcgxrjFKGccAgAGQ9huE-eGnXyg_8Np9OgpMCXax3-gL9Hfs27Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=dnk73aXHOX6_IbGJY_9WZMsIMkmDp7JZkcii5tBxEfjae8kD5U238v1QGnutRN4OU4xnRkPCULEuqBXZnLB3xNhEeW2D5ibYWRwrw2fuZv3RY-NJyl44by_AdKk7U_viloMpb7WohiTvpvmnkSDqVd9G9dCzhLJpRFN-hZj-SEOah-ZMyMIAVebmjqrhTfRL6kjLIIc1AbqXEZA-Lvdksnsk8n_1zOhr7OJcQtDWP-rqlezfaKugEXLA9fgrMtMHo6BJyIkUfO0OmYO0bzc36WdyBPOOTnSlDH_fBRgbDRBKSmuIHDsQ40AzRGspcJ3AIug8asWIhkAwypth10-Ymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=dnk73aXHOX6_IbGJY_9WZMsIMkmDp7JZkcii5tBxEfjae8kD5U238v1QGnutRN4OU4xnRkPCULEuqBXZnLB3xNhEeW2D5ibYWRwrw2fuZv3RY-NJyl44by_AdKk7U_viloMpb7WohiTvpvmnkSDqVd9G9dCzhLJpRFN-hZj-SEOah-ZMyMIAVebmjqrhTfRL6kjLIIc1AbqXEZA-Lvdksnsk8n_1zOhr7OJcQtDWP-rqlezfaKugEXLA9fgrMtMHo6BJyIkUfO0OmYO0bzc36WdyBPOOTnSlDH_fBRgbDRBKSmuIHDsQ40AzRGspcJ3AIug8asWIhkAwypth10-Ymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3XASU0NGcVOrnfEJY__dMUSyy8xH1IJAIyvmlnu-07zaJ144e9kbKBr7jtIm5W7-6ceRNLoHAVkwZ3J472jldvszdSYNogBXnL7Qv4O65uASdphcPpoSfFAqR7TNImvf8yGcLYvpsnoHZ69rWTMj0N2hCzlee9N0VSyxZi7DU6jHRltM48vsOXgTlxfQ423-ltHuNRAsbHqiolbbjwGkNa-g-Z7A5kldNNX2S1mGZgg4W9Arh6iEaBGXIS4zdCFARm5IzDu-1OtGxKRNgFnRj8IKh2pvGT79B6rKZu0Y35B48ZDwuyfnXx6UyzjGsRri0XupibbpeCAc3gM1Jcn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
