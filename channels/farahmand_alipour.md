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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 15:15:01</div>
<hr>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHyP78d_fSmY-vAEqFik2l7ZlkGJy21Sx5I5dXjWixnIxpRpKMQdGkAI1Oq1KSAenwWGwTeB-J37Ym_eptTW1CdqlhbHYgkJxls9JRsQ6XtTkUONkJqS4JY2SPk50aB4rZOLXPUJiFVeAy3u1w6TP0mONF6NlH32w-dKUTKJRoz7VaBhNN7Z95b8cIM9PlEwtvH-zGzX4l1FtoDauqlw_SNW_Xu1nKSHmCoNkqm82SUg5FXs1X_dz-73zty4MuzmLJ-735vEf_LQIWyQ50EBzG63ad77roh1KcQEy0tAt6VCjwrdaVW1OKXmh-XXe-AltoS88ELnyqYCKtTLo7lkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFoTgLRG-08-wXkVfnmUjpyU85d5MEOPeSE2RXukUJ7gcjmFTYlZCb_kpnQL7ZIcAAM_lDv_J4qZLl0hoiuQRaoKA_6j-aoodXfesfc3KLW2-ibWZjxvxqxsCsKOE-w13vSFR6YCpn74DYo1NOBBYyEvAsrIYpZHslnt5ahw7Y8rBD5zD72zEjJb8Xbr82oFCT3fbG_O9-gKukh3C2YomWyaoxAn9HMpLntkpivRZrpZ4r0DzEYp8eqAocUxAJO47HRnA1D8xjLyMZVi-YwcsKo3Qk76hvz83eeZEW9VoL3t6eBs0cX36qSbGuiRA1OhvmzravFHMOyi9dx-QJrwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6fj-XikOE_vV6gn_Bc8O6-xIM4wgXc4YypxLCBQshzeZI2ex4bJps45gE5IffGwgyOcFmOIBXpQ5LzCUMaN_tBTveENWfWCKP8xENhazzUOnaFAp2M-41EK7Ymex4ZhS70FmJAmyGgh9BYHdlF6czYGHLcTQPXfB5Pl3iD77I8DjDXJa0sUIEh6zuEi1VR39aXBilQoalJgeV9tVniQdu1Klpw0ZHKxsgfSfFTz0JXsGf25mcyADsfQjrHKuvlh0iIPGCR6LoO9Jd48T7nKZvec_4o_-CsQq9qSzSvN6_jHrdi6Ysi5U9_kDIWzg08jSHPScvB1Yh7KR2t3-wfS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbIJyOE2Zg99a7z3TD5mDWj0vjc1vH4vH6eeDCZB033bHtcto7zbvY8OM41MekdSJL9DlcS9mLECr4XoRiKdft09qQFx0vnI8Uf4DSB9UJ5SLtKNYr4kzEbFsDroDdylLGJ1uLB_MRRgKpUuLhaWn329PoFDM2Mf7VIe_Vfs2tbR3FlpSShbyJ6hYHVPN45B959Ufyq7LeVRhGgU4i9RBjDSuvUrTRx3kAfK39tQMR-B3y8NO69Z17tPQoOft3RC91injyqPAcnU69MuP_c5i290F9K3QcyL0s-jszxBquiXLylYWfTy2J4tucAQBOGLSqhVQS5QAUus7_jHfnFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBCdTL9seDcNwGsIb89YYMmUWZ75YhupG5WpItG-REVUvZfiD6KHiROnXkLn4fzdNEvQCBsplLIerYuH0UMUBEtMsezM3MC7ZKK7Py0YFkm2H0O6mZei_Fnzbygt7tAnrp_QgM6h59w8uxsGJIyNVQN0aLBYMYZwuWWVtE_nnIqjCdwrYgb8nyJ4K2r6_6FmvF1cFmuGuqTGjxgGNBAjAkenwQxu9CHL-SNdywTVANS_otcnr7RB-hd3qv4e8yGeMKp9oah80UsGtFRxbWjhdqYY3e5LcKoObVpckCAzAsFgLiWr1fFP9YOF9Blgz6KLpZDuv4UTBUShsOAstb-pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_jklWp-P3SyRXbm4_EDnMya7QubfMI49g1j4w_VhiPn-iZO2Evl0qL-0_yfAfFGW06qtFJ0UHnNf8VNKezps_esDctb0ISCH2P6bquT2fhd2L-LWktS049d0km2_qfc_tzlCR9l4PnCDawud2NIK3WyD1SKzbAZDNNSsI9Ag2I4XDPwulWsAhcmD5ckwtPta7cd4Q_2LgsjjzJuSBgaE4NfL6ji8a_T2wKx0RQoUsLXHxU_QD0i-XsiaHSvD88FEIKUiIeua4WC6dHLfzg3ljE_VPOoMVDG_dxu9S4sK-nc3_VHIwtLtU2D0qQOoBR2AhqMam6Ajzxy-v-rz5Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLFj6blG066qOc9Vz59KMvvnEt9kXhpJ-qtpAmFfW5ICohqG4FNQbWoELS85GqFKPesMMQ0oIfeZTJVY-UBuixdjzb57WF9FRUwO7fSY_zE_YSTtvWkrwiIUm2vO2p_7aXcYiUh9MxrcFc9j22DyifsmU4IGvvMZCwovXGmVQUWCILGwMwwid2CfDJ8gyH-a898QpObWojN6z8_9nSXZslXvmd3cLOi3Mv1Tyvs1VE5qQFTsUJnUtIgorLz8krnFxK_6LS-3AeLXwgACCRvbgX0dymYpAbeS0kksqNXta6BKMCcSOREawZwACz_9ToLVmNrpjPs21FyGGKWgGaYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW3Y8wkErEwjwhOu146AJeeXna-1_Q0yQHyVoQUogvuEw84IQQWdhgrcwU80wv9tXG-1-1jTExHEOTwqgh0A15l5iYi9CWoppsIWSS_H_9MqlPO-ExhLP2LqfKuW7q3xDK4o2mdX_UoqYv7uPLz_u6ilcSEtzGMwSEIrDajTgLwW-XHDpJZvpULYX9Nmzv8qJtpy9PZuvcubBZXBTiJ92E6mS6ggwrjB_PG7OV5UKWrXZQCzHSFlIUOOE6JmN3GhWMWGj7vpEg5yt4XNt_lIBZmLVrNJDyAXQONcTbZ5wKvksbzWFVuWgRJTiWIsxnT8K7PmpZw3v0Ako2lvBbMjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftoT0vHGzBnDY_XOgrbM999A50vu0U3HCEN_VD19MRDlKDrZhadB94T8TrzcNVRt85obQoUoJlZuJK3fO9oEmw4y29FrXCXwTbD_uGmPLdIeQCkoycDhgOUajra1PbFAt9VMcv8n_IHQ3SHNWnGxGXjVLHBUO55RjZzf5ftn_evCkOxFDKjzuTt0TUvZjEPYx3OWH9NLgMRb4TmkwxQfeP7eyvtHE6V5ul4OKgv-3bLHn9tJpWBBpZHnTHEQ2wJppZGzm0FF5ydGr_3tDiyBeExW8qgAtWyFe2c8Um8pWnXv316Y1cQGaND5plapVjmBIXdW2g2xBfNyjqXDsYpiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBuHBmINNg4wiMez3F-XCUwCh4n-_2LP_GWmwRlvnv3TFyB8RtDkVdxb-Zy4nGNuP-wdA10DlFbZHZ3V7DqWPXgM6jJi_nBBZnfe_VWYMtMZVTwM3Gkw2PHhpNwx5Q94VeSu6SgJCCxIPXPNGYI1f0EMhCXR44ZpGDsZeziddZoIIatPBWIGUFywliuc8Ua_-t0R8rx1NXDW570NgtDN5LEjSln8aVO5c1ZPYPUopYboMTfzkUbascvXkreIKjppVfb7XzKleq3GoqDFwbxxxuEigMvroiMAWjN6zjiNAYNdzrFWaDGyALxHEazfkLoMoyO8bvmEuGzgrWQgGpGQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN2fLb4cazVvpoyA91J3Xw1V91yDEY7pxYNgyUboOI9fXj91j597ISmxfcEJt_qEUY4Eh2hbwuM_F02Ox3-MqLHnZHt0fMpcP6qVafcVjRFKeAdOP41tExPMPlOR_FAbVXY6TkExty-hZSS58DfVrNyIx-ONpPI0hSn5r5zYv28Xqw3YcMw0ZcKS1d4VuQfoVSoZ-MFA1AI3sWnUVmzgndyX7JEmOz13aMv_PBYicl5pkYcshx58ot7S6HWN2qSBKY87Dy_t2yYzlrpoelwlEQCVAEx7zjN-2n3Ty1JYd8r0GIG1hRHOgavx1i1nkVK_UoB7ksQccoiVrr0GUQT5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=ir6U-0oMRGywlCvbnfJjRE-aSvye6i7G_5uW76N-qg7w0WQNd2ul2dcf81Du_dr_eXbuXSPCTvyoL-uD1e4oTcKg2rLXEofBvHsetDczkln_TRAYW84rzk6hlSOWiuF-F-5PKBn1HwI559CMhrYcEuGd4Vs4bmlzZeN8jGqNqBQijPHGWv98qPHMW7LJeoKErVW9ClzBjSSc_OECeNfXBrx1HJfOe36_vNO4xcRCR1e0mHO22KkxqRF6McV9j88Rz4mD3xDZzh72tDtUsWXuRQ81_VUmjSUApnOGe-aW9gtftnVj4skEoOXDXgh3_IFtmId_V88Lth2a1Yhg5aJUlIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=ir6U-0oMRGywlCvbnfJjRE-aSvye6i7G_5uW76N-qg7w0WQNd2ul2dcf81Du_dr_eXbuXSPCTvyoL-uD1e4oTcKg2rLXEofBvHsetDczkln_TRAYW84rzk6hlSOWiuF-F-5PKBn1HwI559CMhrYcEuGd4Vs4bmlzZeN8jGqNqBQijPHGWv98qPHMW7LJeoKErVW9ClzBjSSc_OECeNfXBrx1HJfOe36_vNO4xcRCR1e0mHO22KkxqRF6McV9j88Rz4mD3xDZzh72tDtUsWXuRQ81_VUmjSUApnOGe-aW9gtftnVj4skEoOXDXgh3_IFtmId_V88Lth2a1Yhg5aJUlIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTGGXdyVtNinB9zwyIcLibGqv0K4v_vLSJ20NDMhbBbITF2r1eeHg1h2GpIfCXVcL6M9qDQSP3lcEGzZZ3uStwTd9S4nY0E4MfU6lHtZtVilwGu45Mxrzbo2kh-3fDETtMu8DixMjEsQmzCTdMhkPEGtCIsSZ1fEnpjg-W2AxT2Z59BTqKAd2YJXI5j6QG4VAzVB4OgixHR-zdG-yP4bOEQSCjampRlK9tSGDzkEAHVbDFWCPfOvQGl22YcePMC6bdABqRTkiWDhcgic-PeGQlqz45M9NhT9Ocbbb69yD71pZ0IqAVrqIWOEKzMnMPGrcN2M0JyKk26ONWGo8BBqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3nw5UDwT0rK9qtbUdoPZVjDnFmP16MRgXF9vHjKYpTn2BUS1LG26jlay5dxPmIlJg9pDDK7EqjM0IKchfyvRzDUDqL90tR6_hPTok9GrG-tMZWTKsmkHGf69zEWkpirgcJfvprPNNxQv08DL729tO25Ma7y20iu-MnSbM8BDU47aGb3okSMLVmnJFY_ik4EEMKnWYQj25oC2vdj6PyOfdZU2CprpaFNXdA3pDfnceJSRQOPdtks3uh7iXcNzzGaOsjaYjFS34Nc-y247rHJjjJoJ8hrTEg5_yZw9zNsffwwhhZDCa4GtfzvIKLdmb970yK3WMIU822mQbJHEfuMAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoLO6wEQ35E9jHT397yt8DKLXWYyf5BIFqCjzyx9qqbUwTa3PiPnHPOCNBdKuG7XCy_p09zu5mBL0KygFn-oCeTk_SOr8tQEydxePWX7xDzhi9HQ_Ds87Htb7keUtqpEcdfoSfA47VDrHuyZ9ahbPIYLSSfQYXxlRgB3qzPTlJDMImVkUXrohogOw_uT0MwvXD3aHP_SlnPZqitziAGYay94FIe073SKmIde2VTVvWRGhplSs88qGvKndvnD7Qz88FazBvatx3wkSho_tq0eq-3ZBvhWr7C3IwG6x-OL7OAYDMkM7H-3B4F5XA2JelJgAySIx2hNolzg8hHXAVZU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lXo5-lckIa6H9Vu93X0rBul4dAjaiKwCxHfmrt8kD3KNiE5TAEdh7Bj1YrA999Elrjiu8auyRzWWcAmXNmOhWA-Wa4IoNqDxkkEQX7KDuE7lrNiV2mu6bZaNOpjh5upxGKZFW0K7NZ_lVAFxd7KtCjROtzp1xRlxic7VhBVNyEFKV5MnKQ7o_VDhNkYKwxgiRaadEAyFETzYCwg5FSLaKIznf5i1jxcznpOG4iCKVv361t4d-6Xbz4usZwMQWdLUcTYLUZhIxyTuOIV2jdB5vEu1svSK9qexnBFQXtrigeb_GMkvy8JMDtvpZ5Qu2QfUhDoPQoUrmhGI1GXACysKKko" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lXo5-lckIa6H9Vu93X0rBul4dAjaiKwCxHfmrt8kD3KNiE5TAEdh7Bj1YrA999Elrjiu8auyRzWWcAmXNmOhWA-Wa4IoNqDxkkEQX7KDuE7lrNiV2mu6bZaNOpjh5upxGKZFW0K7NZ_lVAFxd7KtCjROtzp1xRlxic7VhBVNyEFKV5MnKQ7o_VDhNkYKwxgiRaadEAyFETzYCwg5FSLaKIznf5i1jxcznpOG4iCKVv361t4d-6Xbz4usZwMQWdLUcTYLUZhIxyTuOIV2jdB5vEu1svSK9qexnBFQXtrigeb_GMkvy8JMDtvpZ5Qu2QfUhDoPQoUrmhGI1GXACysKKko" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=ZWo2az5OWZvwkyORrH4E8T4zyEtMY2BPunTlT4h0ORAvckcxDbO9YpozWodrxN_fGOkJ8sSGHrkMAbkIhhz6wU-oX439yUiUdr1Qlpz0wfgO0wvkJoFMVEdNqaByOVXT71LhqCaWfdhb7XtMwbiYG3FCnXYXsysumQitUo0csZgXzAf9kXk-68Svs63E7VJ_TpBtKY0g4WCAqtPRq3IQjNb9tSMzVYlQ01fdk_iI2eqYrRHS18s8Tyu5y8BBJaKAAUbDvTkO4t8rbYcKU0MX8BXfGTYbUVQppLSsjVCYlFvxVQ1yF5RTnYtDro394EtzSgIyO3OMTad-PDm897bJOTDPIR_TOYrrRLdZRh_eQNZTDhwY79_mCu9S9MToC3F684HKLDTXXMpFs9bO0TYP5eQWBfGiMTRE5-_Kd2USe1Mu3EzzWhMJz-bug1_UpOQ5Lgi9JYkBHVq_iLrOJzJW-kDr681LLHkvFgevoanQo8f3ziFNTJaYn-b_7TTy8Vtt5QYIUkdU_mnKLOcTJnZTD3Uwt5QNYoSGBF8SMWucdMUQCK8bkwiSp9dxTPfZ2e7Dvwwbtq7V7ez0B7-u-OmiU_nh25x5HH7SnN1BEygjJ5Z5bVOUCI6aZNMC7HcyBNz9khmC5jIlfHRMp_HNSBNPWA3y01E01OA3MhF4HenBHCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=ZWo2az5OWZvwkyORrH4E8T4zyEtMY2BPunTlT4h0ORAvckcxDbO9YpozWodrxN_fGOkJ8sSGHrkMAbkIhhz6wU-oX439yUiUdr1Qlpz0wfgO0wvkJoFMVEdNqaByOVXT71LhqCaWfdhb7XtMwbiYG3FCnXYXsysumQitUo0csZgXzAf9kXk-68Svs63E7VJ_TpBtKY0g4WCAqtPRq3IQjNb9tSMzVYlQ01fdk_iI2eqYrRHS18s8Tyu5y8BBJaKAAUbDvTkO4t8rbYcKU0MX8BXfGTYbUVQppLSsjVCYlFvxVQ1yF5RTnYtDro394EtzSgIyO3OMTad-PDm897bJOTDPIR_TOYrrRLdZRh_eQNZTDhwY79_mCu9S9MToC3F684HKLDTXXMpFs9bO0TYP5eQWBfGiMTRE5-_Kd2USe1Mu3EzzWhMJz-bug1_UpOQ5Lgi9JYkBHVq_iLrOJzJW-kDr681LLHkvFgevoanQo8f3ziFNTJaYn-b_7TTy8Vtt5QYIUkdU_mnKLOcTJnZTD3Uwt5QNYoSGBF8SMWucdMUQCK8bkwiSp9dxTPfZ2e7Dvwwbtq7V7ez0B7-u-OmiU_nh25x5HH7SnN1BEygjJ5Z5bVOUCI6aZNMC7HcyBNz9khmC5jIlfHRMp_HNSBNPWA3y01E01OA3MhF4HenBHCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmNFaAtQLAkaPr2EJgSEzrLoufZ4a0b1H_IsiBEp8-PJJknQr-8WrmS274h7dGunlQWEcD2O0FJgehexsBd89sqCjDEImOGa3H3-jObPMp8ppd7Lg1xmT_rhhlY6ka8kwEQ2Q9HxQrdaEFMRHr0esofd5CiiHPEXDxnB2JsHFyDGMvQ5stgoVCLdtwqoT5wgWmc6tXIkrtljp7tb9WvYKwaHadbrIe6FH6LF5OmaLJoH4ZftCPkb9seVHUGJ-awtINA2FBG8RtHNLiMjR9xjb_gkSiTtep5D5re0WxVlcysTkIj9gANB7NfBkveRdVIkwxuzBxI7AFjliEwTEw6-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8iTbF2EQqezlGGkjHNnVfQp1GbgkvkCEhH450bkUp7fGw9SKgvFpDz6tQcSTCfi_HCArpnfRdHHzH1tSAOMLv2CCN-_dvfDoFevlqDClaQ77_jxJ-BfiJw5eeYkxO7t7zWzNpLIdFu7ADfO9mdtO5Dn6tE36WYQzylSfVZZsH-KiUoKjLL4uKdPlU6-8v2rIUSwsB7d6hj2AMbI_cD0Yd_Pyv1-LSAoFIvIL6AOrtCc3sY_t27UZuERzRgzo1PtagxgI6rSxATJU5Hx-Ll0NDK7bGe1AZkWFFIRLA-Qm_sKUY4S37smSO3I6udkLAj73riTLAXwArs5hAEIlgv2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQUl3Mr6BcFPHUvHcad2HJlXWjQULmMHG5GgbB8M9GzPEolPkyK-TvdMV_RrEGt1BAi3b8VLubMqMRpxJ8UnHhYAuEtQMIvrkqdMptHrNUvy32p3N44ewyPjlIWP-OScluYCeAtZh9wyih_c9CnayLUci9kmVGBe0vaacIJu0sjnbAf-4S2CZAfHGDrpw66e6YOhj5dZeZLfdLCRSvZbT6C_EHC-4rqv_5Zwow1wT9_84fY7gIkn3EBkqETSisF5bIN-X_NgbvRNgVqXBDi6hW-chhkDXOns7RIO1LW6idDlwp6Mg4hVW1HUdtuBdJjyYM9YGpLAT9D_y-PUAittKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=s0PnwMMnrlLRNkrt9OgadDKIkHW3ptOeGNahVGOc72Kkz7AatyhQLzjOFMo9SumHbU24zbVFWDbgAxE2mSlTABp2cyb7VkCx-kQIrNO4q1viSxitOT3kQdZZqXj-HfAeK5mzpP_6_CWf8HOVNZUZ90VkH-L-p10EY2MP7qr-TdCtZvEKXm0M15jiKBnIoK8kLqUW0FQ1XmnIlcXp78bXlj-_wlXm5ENf-QuZYa61JJzGf0myAfYB3UjjpYZySzE-8SGq8k3ZAQzoTSDDRw9NpURyrpPK8DlxAdVof-y76YYtl9Q2wq21INStku84lbETjDaMXnmIPI9Qft6_jaVgjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=s0PnwMMnrlLRNkrt9OgadDKIkHW3ptOeGNahVGOc72Kkz7AatyhQLzjOFMo9SumHbU24zbVFWDbgAxE2mSlTABp2cyb7VkCx-kQIrNO4q1viSxitOT3kQdZZqXj-HfAeK5mzpP_6_CWf8HOVNZUZ90VkH-L-p10EY2MP7qr-TdCtZvEKXm0M15jiKBnIoK8kLqUW0FQ1XmnIlcXp78bXlj-_wlXm5ENf-QuZYa61JJzGf0myAfYB3UjjpYZySzE-8SGq8k3ZAQzoTSDDRw9NpURyrpPK8DlxAdVof-y76YYtl9Q2wq21INStku84lbETjDaMXnmIPI9Qft6_jaVgjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KapZx-CFMOJFXi3kSItLu4uJjwKVSJcmbYtN0nwzdkO3kx5UXhFZSMFLx9YN8QQpfKeIX6gTUScRdx9CG2A0VpGmkn8hHSvG-QO-L9FAso0S4NmrjLb_s8LslRnGz3OGd-nFwLVREId7GS-JE3-iIfxRrj0Skd93FRpOAY4MgpI9QIM6e6MB3wdecG44v5PhAwvBSLoYFwIIq-kPJU5BvBZv22V1CZU36njZ8N1TIr_aRPI4lwM5HQrDXBc22hFY7JmrrTUNlg3XqxXbeGwdIcChFbTvDnnQEUrI9DXhkJowEjpZKj-seOAgEWUczb0t8prEqvcXJdnecjsQ1xKidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=kCCKKvNRIaKjyaWyc10wWZTAujzx2p5PHBxHWNqHp09ydSN1B40ZPushyEhRYppas4GNROH_df6T-HYJTFMPzBd5AFxRNBkBBDFoFiHhf1qSeJJu7dB62x9Wh3-ZZqlP4s5pRXiNXIiiQArRPy_vnggeu-ECuwCvsyth1wsIy0tq-DF_U1XcxyikaGu_DAMgfAKRSmYM8yj1RgXbq1waU5lEFFZ0ZVLVv1fNQZna51bXrNwnvrNyoCHFvDs3nddJIo7XxTK8rxaRix29pEXDRk7gM8k0Zpn1YHjVKcwiSqyqsTxDS9C5MA7KV5wlrn98_3uUEDzP8el-esZ4tnMnIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=kCCKKvNRIaKjyaWyc10wWZTAujzx2p5PHBxHWNqHp09ydSN1B40ZPushyEhRYppas4GNROH_df6T-HYJTFMPzBd5AFxRNBkBBDFoFiHhf1qSeJJu7dB62x9Wh3-ZZqlP4s5pRXiNXIiiQArRPy_vnggeu-ECuwCvsyth1wsIy0tq-DF_U1XcxyikaGu_DAMgfAKRSmYM8yj1RgXbq1waU5lEFFZ0ZVLVv1fNQZna51bXrNwnvrNyoCHFvDs3nddJIo7XxTK8rxaRix29pEXDRk7gM8k0Zpn1YHjVKcwiSqyqsTxDS9C5MA7KV5wlrn98_3uUEDzP8el-esZ4tnMnIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7b7puLuCL3eybIqVZIHIeJLN3TzkOh9IsTckv0zdQd4mEj9093c6n-X5DuoqCe8d-zt24KF0qMkKHdftMMczMaqHJsnMxtZ8flLtHRnbvlSjkr8QkT_IegED55WdhnbRE_o-xbAguoczLvvv4xig2l-vcvXCF_71dYpA7LY3Wz7OOwehbHTYp4dCutJYYn3LDsGvg9wO4wvO_TLllDbnbwuBsZvKwJEYqzZ5jf6nsFXdOfiJT6ntQK6h6PuJF-tcEtE0t7bcmX9q4KSVay08Km7IDhyuuhC0Wgi_YgnMhBFuRzQpMZXr-tV2yg5uTiJvI4FQUBoTl_LxLbR5KKCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_1m5D59-XsrjzbWqMrNrTkprmnaoy26RX3l6pZChdi4EqgCA_EWZ83reLG9Pz08gCguORs4az3T35wut45X_2cbFpkbiUYzcuBKB8bXAdiRWI962cn5wFUr7rAQdmrHR3jbLNmXaS1IF_tN5qGIc0cpjS8vZBaqnPwrRd_guMhcN9Gtd_pXiCgPKojp21nSK-olGs6CEKYF1BhkGuDaeDOFx1g5jSXJ1Qnp2DknROgHp1ZgLWh_yltPsTXOAHV6K-Ok0n-5dw8QAjlXLJyKTKs6j8778YIPm7lh71rWrHRQEOoTDSOeqc18awLrWc6lsZoHDmPJ5HZp-s51MpIvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=GCWB555-XbO7N6pWNfschlBQJ6Ruw811qmrxVGZMqrOjvzO_rdhWX_adrqLU3cRbQN-bPu5QQRL_najyvjZyMGUS4TY7xVMyPNXkXwvDIUXo5VFbkdZgzqGjuDQJymwAA6f4MUu-0l4MuVVY4BbLRIdJ7VxbuwUS6d5Rlrvo-kPbUXz1cZINDJcmJldpQ_lNOu29jf5l5_IYs2hBuvFVWYwifTM-MxINFRVpBZbq7HrchDdYLATg4QsIL1TqnTue0nIG2Yhb9zKAvfZheEYAHWcS54Xdkyy7GF9mW0EQI5o6bIYoNZVos1t1ENSm2dRI4xBqdx3wrqDWIY3fFLhijw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=GCWB555-XbO7N6pWNfschlBQJ6Ruw811qmrxVGZMqrOjvzO_rdhWX_adrqLU3cRbQN-bPu5QQRL_najyvjZyMGUS4TY7xVMyPNXkXwvDIUXo5VFbkdZgzqGjuDQJymwAA6f4MUu-0l4MuVVY4BbLRIdJ7VxbuwUS6d5Rlrvo-kPbUXz1cZINDJcmJldpQ_lNOu29jf5l5_IYs2hBuvFVWYwifTM-MxINFRVpBZbq7HrchDdYLATg4QsIL1TqnTue0nIG2Yhb9zKAvfZheEYAHWcS54Xdkyy7GF9mW0EQI5o6bIYoNZVos1t1ENSm2dRI4xBqdx3wrqDWIY3fFLhijw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=iwdoMxtgcp0-n7ZoSphfaJlGQcO-3jkSjKf8Qi-6roZwDWMdXjbQix3X46_0u-8QsI7bYYUU7htT_QVHkCMhh2bFOrtm-6LJuMsR4Ioiofip7dz3jPVBXHi-DhRyaa-_c56DlAYXlZ2SMMUtM2tabVu5P03YGeqGRdPGpnV3FXwjumienLPE4XXKXj0A3tk2uds8n-X4rzZ1U38XDFHHdfOieL0ObAmgMs4s4pBrp9BlrJzXkD82LrV6wXrpN_fkwqdFV7deSo0nJVqzn5LvlpoKaEpIyvwzta-xSJOPW5aVQy0GewwNUKWX15Win3QCnuBJyCMp6OrXko1o22HeCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=iwdoMxtgcp0-n7ZoSphfaJlGQcO-3jkSjKf8Qi-6roZwDWMdXjbQix3X46_0u-8QsI7bYYUU7htT_QVHkCMhh2bFOrtm-6LJuMsR4Ioiofip7dz3jPVBXHi-DhRyaa-_c56DlAYXlZ2SMMUtM2tabVu5P03YGeqGRdPGpnV3FXwjumienLPE4XXKXj0A3tk2uds8n-X4rzZ1U38XDFHHdfOieL0ObAmgMs4s4pBrp9BlrJzXkD82LrV6wXrpN_fkwqdFV7deSo0nJVqzn5LvlpoKaEpIyvwzta-xSJOPW5aVQy0GewwNUKWX15Win3QCnuBJyCMp6OrXko1o22HeCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=u00zYjIbInZ1z84_DlMTAWsuh3BQAsjQau1rjfPcEdTancnfydeBSMu3_8dt96EFT4dk_2AuHWRU5OVKmXZJLnXavs79_p8AtzyxCS3F1QvKwZM1fRegPyG3egZ28mvYViw88YG1L5InpwWRcIx1alSH2L37ugV4S2RaKg-Rd_0cXzE6PIpUdx2-Y_RnJiS7sUqPDJWV4JJdLlbbMXQ01_EjX0QxkGLP7JD0EGMRXe2rLqmZ0Uwk778VeHvJMjrfOKFMKTckh6GmBjXN6bY-k0m6mvIGJIwwWTxHQdW52jX1GrqSXsdgCzo_lje-FwrgnpvZQlkmHVi_lDCLXYvMlaJm79h1rVBguzk8aP3SD0a_RWkr2lGddEJIhvuecDRu_o6ApnpIssULY95X1_mWV1dnhqU0-VEXU7TxYsA-FuaDcU8LGLn5WbYeFhbDRDFkww7vye8Q_bKqFr9czvA827Nhkxh2s3bFI0OPnNiJpuM47ZfULlVmeWC2bCCE4lmuLqzDLEkct1rrRrecImwNMb41X4EKaVDyamdCwT0VOCUeCBOWflPWbgqu5BWO1b2SYNiqytR_WxGE28oa32dC4K8rF3Oszdtpd9GCYfml9waIgjTlHju8_nqU1d8WqLc9OV8_M0cbz8rwkjOD7tyT2DbtiLzyleVv8CX9UDwb7jU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=u00zYjIbInZ1z84_DlMTAWsuh3BQAsjQau1rjfPcEdTancnfydeBSMu3_8dt96EFT4dk_2AuHWRU5OVKmXZJLnXavs79_p8AtzyxCS3F1QvKwZM1fRegPyG3egZ28mvYViw88YG1L5InpwWRcIx1alSH2L37ugV4S2RaKg-Rd_0cXzE6PIpUdx2-Y_RnJiS7sUqPDJWV4JJdLlbbMXQ01_EjX0QxkGLP7JD0EGMRXe2rLqmZ0Uwk778VeHvJMjrfOKFMKTckh6GmBjXN6bY-k0m6mvIGJIwwWTxHQdW52jX1GrqSXsdgCzo_lje-FwrgnpvZQlkmHVi_lDCLXYvMlaJm79h1rVBguzk8aP3SD0a_RWkr2lGddEJIhvuecDRu_o6ApnpIssULY95X1_mWV1dnhqU0-VEXU7TxYsA-FuaDcU8LGLn5WbYeFhbDRDFkww7vye8Q_bKqFr9czvA827Nhkxh2s3bFI0OPnNiJpuM47ZfULlVmeWC2bCCE4lmuLqzDLEkct1rrRrecImwNMb41X4EKaVDyamdCwT0VOCUeCBOWflPWbgqu5BWO1b2SYNiqytR_WxGE28oa32dC4K8rF3Oszdtpd9GCYfml9waIgjTlHju8_nqU1d8WqLc9OV8_M0cbz8rwkjOD7tyT2DbtiLzyleVv8CX9UDwb7jU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPPwabjy3m2Wog52Cx_DanI6w6T9N0QvT0yoUd_Jgw9v1v05bRFmHW1OlNuQJAnZgjgKvUuKCl1lmQfjAJGlGyD-faUV2RIZeIzcn3qP1iuVuqCWTOKP-__pFEW8yiewfx1CRhx3OBF8aar8YEcbXPM3rucrAj3taiD2JWrlM8-4SLpf6TzNna-IEYtUmz4m2A6zLZfBD_0f4rd4hea7u51GMDH1awgRIt8hwsFGYmP5Hc6YdZhZMEzblsJi2GoDyvPBe0a62IE8R5eRHdV_2tLnGpfS2oqnOBcYHxuKgdhJZuFPT8itl4mZlWeHfv0Xz9sKM8PpWpFp2uJo0hPVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmcEqRd0dOKIi1JOiXl-WYyQgA9dH7Y6HQuowiYmRIsyVoT-uXSe5bNnNQhmhDOBMQf9DCMWHfE8sFsDDidxrZ71d44e5Yp8RoQLQ6FFNMRj8Q605x2oln5BFbP4zK68uB8I08k_SGLJjWRbd0zEHpP_4xjekb0VgpDICPmONsGTB1ZJrbeiuGVQDKN-kmhmvwNz9fTEo2zTf7S2BZxYSqWJNZneD-EqRugCHIaBJCVvjvmReNP8LdrDP4xvJdP1bbJgbxs0NsdlbiaTkOGQ_DR1Ruuz8JbrbJpt2O__Te0M0J_yW_rsrgqjIqqmh9K58Rd6f-2geymE0UenACryJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtdDzJ9FaTXeiDQ__KXhAf-yzim9OruiOo701-_tt5SIxgMUBjBguV7ToZCscW_ohLKtzGWod1CcI3J4Ah0FzRygz9TFCk5gnMLa2k5wmuTwsdDqJXtyI9dqLh533XG_RDso3pE0PkbvofxtKGh7mIe3SIu2f6_jrmwDm8z0vBr22hHfDJmxXGQmSdBxd1LREOX6tgl1wY_1nHBkVCvlBUG84gy3wdSIXWYR1I58Ga_mC2xDMINLGnw0Mva4gNkokByS88cFz06u2b3h83HwELIvdkAQLEcdw7N77R5hz4c8fLMhVMXvLFGUENWH9fP-8KG47-yL1K5rDtix9t7oJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=GI1_IsaSiWp41U_AVVXkL9592feDj2Pnw-4SvzNvySbzrGVmA8FxlX0CXlQOX2-nu9iI69CO1FpiTMgY2qYILpl3gKJRuiz6HyIB__nm-fFKVXG6S8DLcvJSDBp7kmbFPub1akxahXJ0ThEJBX5dXYTVIA9PIjUV-iOu-DrR-WJ7p9_JMcR0hpFJua_XVVqQVvEotnT4ybydQCPPUvc5eIVR9CvpfzPJVSLu320rJY5mAUTknj5JCK7b7IINWO3idun8gB24yYJ9GS19cVO2yBp_Xq4FOwVSpaCbMugNo5GtLNUk7hJyY3NdUZoEmAD-TeY8bQ-CjtV6GNeuJRO9TTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=GI1_IsaSiWp41U_AVVXkL9592feDj2Pnw-4SvzNvySbzrGVmA8FxlX0CXlQOX2-nu9iI69CO1FpiTMgY2qYILpl3gKJRuiz6HyIB__nm-fFKVXG6S8DLcvJSDBp7kmbFPub1akxahXJ0ThEJBX5dXYTVIA9PIjUV-iOu-DrR-WJ7p9_JMcR0hpFJua_XVVqQVvEotnT4ybydQCPPUvc5eIVR9CvpfzPJVSLu320rJY5mAUTknj5JCK7b7IINWO3idun8gB24yYJ9GS19cVO2yBp_Xq4FOwVSpaCbMugNo5GtLNUk7hJyY3NdUZoEmAD-TeY8bQ-CjtV6GNeuJRO9TTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=r2gTUd5GOMBgsTpVJdapNLM6goJDt6NDSg_MVc1G7xK6BySYF1zRQwOCUyReBTbU-chRep4B4xOhd9bEXMmlC0ClwVVkyLWnMTmhMW1oLvESOyBaXiMtcwpOQc_ZSquNj3mPsQSCAEp9FOG0owWF9hmCjHnhrU8sgnPk6jAunvedjqXDGWRDKhCXOanNNngkqbE73cL1OA-Xn0VNU8Y46qzJoXQjsCG7haG04ZEEwZvkqpNDGI3PHWCx4AaAFSXW_PkK3XQT5xlbYInQXkY1j6xmdtl05aGxB5rLzOyS7yCC4RufSNFw6q_hioT7b0bOQYtuq24iGqzrldxQKP1XBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=r2gTUd5GOMBgsTpVJdapNLM6goJDt6NDSg_MVc1G7xK6BySYF1zRQwOCUyReBTbU-chRep4B4xOhd9bEXMmlC0ClwVVkyLWnMTmhMW1oLvESOyBaXiMtcwpOQc_ZSquNj3mPsQSCAEp9FOG0owWF9hmCjHnhrU8sgnPk6jAunvedjqXDGWRDKhCXOanNNngkqbE73cL1OA-Xn0VNU8Y46qzJoXQjsCG7haG04ZEEwZvkqpNDGI3PHWCx4AaAFSXW_PkK3XQT5xlbYInQXkY1j6xmdtl05aGxB5rLzOyS7yCC4RufSNFw6q_hioT7b0bOQYtuq24iGqzrldxQKP1XBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=MAM3Ps4u-P-pwE6xHx7C4-aK6PLKxeD_xUdTBS4ADxVva5UvxVHXPaPw8Km-9thDNOgpXEd_ns6lDMzHbaPLvzqC1-gsLZuhydTA4BqpB81awRn55tVsv6vECGI8VK6iJ3Q_WIBm6NXxMygOPNwywqb7cbvl5sKAfXeKh22cOiyl3FrUUxfNBobjd-JR9xJP7iZ3g86QKZTLzEGnl6e853xN72GknVmrwv4mp8bHousmmYZsrTVpTPg2_641hZ7bnAIgB5bUng2VhiZNfn4cTtGf8N8hIj_QomNu0SqcO1zAsNRDEoke892wQy4AtYCJFmj0eMGqvUGqR0ECE9yiLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=MAM3Ps4u-P-pwE6xHx7C4-aK6PLKxeD_xUdTBS4ADxVva5UvxVHXPaPw8Km-9thDNOgpXEd_ns6lDMzHbaPLvzqC1-gsLZuhydTA4BqpB81awRn55tVsv6vECGI8VK6iJ3Q_WIBm6NXxMygOPNwywqb7cbvl5sKAfXeKh22cOiyl3FrUUxfNBobjd-JR9xJP7iZ3g86QKZTLzEGnl6e853xN72GknVmrwv4mp8bHousmmYZsrTVpTPg2_641hZ7bnAIgB5bUng2VhiZNfn4cTtGf8N8hIj_QomNu0SqcO1zAsNRDEoke892wQy4AtYCJFmj0eMGqvUGqR0ECE9yiLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=daAybvdKok6gG12ev4kGMJCEkKm4pRqJCHH76To8qMVSrzDcuRgoUU1SuJ7f-4OjvaOwaYrAmlIXqPOXhaY-sEoS-G_k8nv_HbpXh_k-4m7AAoZXM7tZR7khbklq9m6AEUyqj8OwuIgtY1KUZrL2XCrXbi3M0id5QfuF6Oc3s9zvs2c5szR7BcYhNq_dUkBxBU0k1zJErwclcd-W65sMkZWGn2yYLn7u7QDkiZoqZHHtXYT-_wGkgrWqVjn8bh1Z57srldlQrGxQ-fdJ3S58xSXUqHy9jnAgViUILqRcCBT2aBTmkGzz7OVsvrrG_M6kWW1ty2sbAjArFKkmCAAWJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=daAybvdKok6gG12ev4kGMJCEkKm4pRqJCHH76To8qMVSrzDcuRgoUU1SuJ7f-4OjvaOwaYrAmlIXqPOXhaY-sEoS-G_k8nv_HbpXh_k-4m7AAoZXM7tZR7khbklq9m6AEUyqj8OwuIgtY1KUZrL2XCrXbi3M0id5QfuF6Oc3s9zvs2c5szR7BcYhNq_dUkBxBU0k1zJErwclcd-W65sMkZWGn2yYLn7u7QDkiZoqZHHtXYT-_wGkgrWqVjn8bh1Z57srldlQrGxQ-fdJ3S58xSXUqHy9jnAgViUILqRcCBT2aBTmkGzz7OVsvrrG_M6kWW1ty2sbAjArFKkmCAAWJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOBMIBMDlBprXOealXkC8HGVuDK4aYZIu1WCdivr2lDXlqJ4eutGSu4M0QCxcZ6acKv-qwZIhJ5Jw3mEfKPAzeNmlO-0p3T5rIMeK0793D6r9YMw3V2b-mvLArJcqTqXz8ou7analGwpkR-yf3eyhJK_9TUpEFmPTB1qDaD9zIQBX-3jAU0YG2FwbTLUnaIhY_6D8vTdfYXQ8AgsYpRFMoIccTRGkoN6e4XN6xqEbkZXFaFEVhggvnxxKkvqzyc6vY7-7ePDj4Z6AQoI3zfaWbqjftbY1wNUqnXFkWTKqo0W797cS-LY3JS6BCY34w9IXHVQgnwuRjslWtfXIpvgyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=vjhRvpKBImolGgDP4ukBC-7kZt44DryPv2dxd0x7bZzSXHETL9hu_jIHGBQ-IrprDpRtzvnHtRRgEpw__bhuCJeupVOo_f5-JJjcTdb0-nGGDSqWhbUfIkgJuaVdR1RfP8VPoqjMuLzBYuHHxcXi7DJ_bpzhpt0nDlRCPJNFyG40QTnLCvb4UQTxSLuxMDHdoFtZxGnaQpS89seHpRtqu0HzePVGEN4gALFKcgss5jqTB1MY1j-Oj0ZhuLAE54Bi8-2MbL4psq6WpjhqyYX-OmwmANNkFOFK5XeSbLgUUIRbc-RTY2tTnSPm3X2601qcQ-MUGtI1LRv7Bo0k1bsCeiIss9w6UbUOAa43fgsFVdfk51UYd5VV5m3-d0M3mkl0IUqqny9Z3gl4Rg-VRT31GhTGmP8bJemVRegiMipbpchTRVYj6ZKfml_B2EOEL4GccmdbW5fxnKLGg3mKRgndMUYwkxYS66zb-948CHuia4Ba7HcG8Yydbxitw1knf5_7Ez8QiMHIG3quwEc5-lJbhdIv-5kfH6A_Zsj-odOtGMDmARxbPPeKpREQNRAyeowbpILOoUbHZeuk7sZoB9os-r7g7gjqZZiFxX3pihyqljBslDEF1KNEW60iUzAnN4WTVcI2X-Ujjjt4hyVbS-AZ3VzSX74FLh-HFjU3S-3zoM4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=vjhRvpKBImolGgDP4ukBC-7kZt44DryPv2dxd0x7bZzSXHETL9hu_jIHGBQ-IrprDpRtzvnHtRRgEpw__bhuCJeupVOo_f5-JJjcTdb0-nGGDSqWhbUfIkgJuaVdR1RfP8VPoqjMuLzBYuHHxcXi7DJ_bpzhpt0nDlRCPJNFyG40QTnLCvb4UQTxSLuxMDHdoFtZxGnaQpS89seHpRtqu0HzePVGEN4gALFKcgss5jqTB1MY1j-Oj0ZhuLAE54Bi8-2MbL4psq6WpjhqyYX-OmwmANNkFOFK5XeSbLgUUIRbc-RTY2tTnSPm3X2601qcQ-MUGtI1LRv7Bo0k1bsCeiIss9w6UbUOAa43fgsFVdfk51UYd5VV5m3-d0M3mkl0IUqqny9Z3gl4Rg-VRT31GhTGmP8bJemVRegiMipbpchTRVYj6ZKfml_B2EOEL4GccmdbW5fxnKLGg3mKRgndMUYwkxYS66zb-948CHuia4Ba7HcG8Yydbxitw1knf5_7Ez8QiMHIG3quwEc5-lJbhdIv-5kfH6A_Zsj-odOtGMDmARxbPPeKpREQNRAyeowbpILOoUbHZeuk7sZoB9os-r7g7gjqZZiFxX3pihyqljBslDEF1KNEW60iUzAnN4WTVcI2X-Ujjjt4hyVbS-AZ3VzSX74FLh-HFjU3S-3zoM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=bt-zsei8coRLOGyrSxf3GNw5cgTqXWFs8vHmx8MYevMbq5xptpUQ61sFRrv0YjDB_U8L-rsnTX8tQEKGi2l2XFCNkmy9jxCtvKW3hZwrT6ij2wB_TWY4_9_MRMrDMO2IlQR5YqYU9KSIe_rUKmIlpQz8EkMjGWNFiUkB3i__5W4MGEVVEvKvn_lVGxUmEXWpMhtbhS0FQVBP2mWKJrDIqy9vxgETQ4qrFnNgP9Yr2lIYxwsxLR5gCk2jR76MkPXhuowMadxPSMv2Nzw-SYOVQGM7o8SoMGwjy3fzuQnYtoTM_mBb1yrlxdC1ORMY5hsk2DJxXQMnB9NtojhTTfm24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=bt-zsei8coRLOGyrSxf3GNw5cgTqXWFs8vHmx8MYevMbq5xptpUQ61sFRrv0YjDB_U8L-rsnTX8tQEKGi2l2XFCNkmy9jxCtvKW3hZwrT6ij2wB_TWY4_9_MRMrDMO2IlQR5YqYU9KSIe_rUKmIlpQz8EkMjGWNFiUkB3i__5W4MGEVVEvKvn_lVGxUmEXWpMhtbhS0FQVBP2mWKJrDIqy9vxgETQ4qrFnNgP9Yr2lIYxwsxLR5gCk2jR76MkPXhuowMadxPSMv2Nzw-SYOVQGM7o8SoMGwjy3fzuQnYtoTM_mBb1yrlxdC1ORMY5hsk2DJxXQMnB9NtojhTTfm24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXmbiJOQgSbad437ZkSHOLKpo9hLxOLGbGofcu7ro-G7G84OgyBnfTW0dI_kpvuCml7ZR6LDrBZy0J4V5DTdc1RgNPwsQ3AswuTnfWF87qyJeP--tNjihHE16WrDR-9fBc_ayuRl9s_-s-n4SJAB6K2KI7nQa1wVloWZH5wGjN6yBvzsgxSeGax_fPDZz2l1KRDzoEq7iw7Qm3cSO7uSL9TBn_eSKwKMY06rT4_bv_xaS7J3AFZOxX1WwRxK3VOJ22-WahH3CC78ji47VDotGjG95C5_8fRWavASFYEATg1rgwzpfV78ftm6l_Vt_4n6PwWVcP5fdaMIuJDhgQDv7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=NJ9de164WwQX9JtvFX_-ZsA45-pt9NMR1gAp_mUg92Fd3hPaJCkOPx2hhSEvP0dPfByiQDn2tuf21ZM9QO_mX2XYAkdEglC4eTA6WdwJckM0lXehKQzDCKq5pugy3tHFYNOhBXYYif_3NOdqWxdO5DdccwYOHTZghrOT1XCitvXbU7XecL39Ks2EUScAfSHE5oNDG95PFMGhY_yVmPYubPRg5qb7SfJ7bpI001uIUwJLHIaoF2kwxYb7gSF5PKvVP8m-RmdxNcLrAUxIv0zkvpCa9t8p38Fv8s8b7QW35vlup2-fRgPYTurZeUgJ1hVzOCKj2ZS_LQu0Ws7mNfQ7DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=NJ9de164WwQX9JtvFX_-ZsA45-pt9NMR1gAp_mUg92Fd3hPaJCkOPx2hhSEvP0dPfByiQDn2tuf21ZM9QO_mX2XYAkdEglC4eTA6WdwJckM0lXehKQzDCKq5pugy3tHFYNOhBXYYif_3NOdqWxdO5DdccwYOHTZghrOT1XCitvXbU7XecL39Ks2EUScAfSHE5oNDG95PFMGhY_yVmPYubPRg5qb7SfJ7bpI001uIUwJLHIaoF2kwxYb7gSF5PKvVP8m-RmdxNcLrAUxIv0zkvpCa9t8p38Fv8s8b7QW35vlup2-fRgPYTurZeUgJ1hVzOCKj2ZS_LQu0Ws7mNfQ7DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=XA5BXdPHjC4fnhIAUsvzT3k72V-9Pn0YRgipXiF21jNfEYTLXX7nGCcDE2qmoNWUCgQExu-CYV9Yy50CwWVtVU9JaBRybSOGyacAm45e4eNma4Avp7SHyrNXSa71L2C8eOz8-MZ5i7k0qfu9P1U7U6snHAW3O7dqHYWh4t7odksnaFNfoZtyLGuyatTRWs_W_37yk40bXURR8bZYeIhc45EXFG92CATQSrxFLM8uI7EGIOntdVaZ6d4v2FMF3gP6D-5AjJuF80Lb9dOImrTsW9cCvmC3zB0gREe9hUtF4YbzcwZTTFSE13B4R5km5l0sqVnzWEt9c6zv6TH31JYeiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=XA5BXdPHjC4fnhIAUsvzT3k72V-9Pn0YRgipXiF21jNfEYTLXX7nGCcDE2qmoNWUCgQExu-CYV9Yy50CwWVtVU9JaBRybSOGyacAm45e4eNma4Avp7SHyrNXSa71L2C8eOz8-MZ5i7k0qfu9P1U7U6snHAW3O7dqHYWh4t7odksnaFNfoZtyLGuyatTRWs_W_37yk40bXURR8bZYeIhc45EXFG92CATQSrxFLM8uI7EGIOntdVaZ6d4v2FMF3gP6D-5AjJuF80Lb9dOImrTsW9cCvmC3zB0gREe9hUtF4YbzcwZTTFSE13B4R5km5l0sqVnzWEt9c6zv6TH31JYeiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfRQMp-7h0Mhge-wlM7ePaC1sDPVffqwVwoIvuzJ7Tr30oTPpnyk6UsU3CJNwnI65QxnfMQkrt0doh8x2-HbhVXoDXm4CM9MxpVHXjAMwXeyxFtxp9l9Knmo3y8APu3wrUHtduYEDCmV3sfcAbwpINiI6ovGaIF9rj8bpVQW-NjCRT5f7dcUyxwSxSS5MTOeEfluqfOofRJrbw1IgAGObfHLyUBW7jZqEG1swunqDZ-FpWxjfLEo7MawoIi1R5tUpHJrBeB5KolZyEOQntkHU2NgFpLer974mslhbGcuwFxUNItnDVfNXIinoznLeFBs4-VFs3e39neFkPpCjiuveg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=FyyypmnGjue3SgU6tMhVHYCcx_O4VdOxoSVKSyC-SVZiVfqDtlgEYondLjNxneKBKVlCINtQ6GPgKvkT_AfviMqRsTdsGAC67GN1F0RTWegm-AAyLCK95V6ZXAAn5JMO4tYSe_UrfsmQBZ6h3-mk0U51gm04UIWF2VxGKkl48-aMaV_w-5W3TzMJf3JEHBcDm_uuaPwK8LUXmSecyTo3qHLQwSNFHckBgOOk3jD4e5vVQSIsO86GpVm0Ud_-oZYv5ThSpsGopLQVXaeTlistCBGoayxeGksQTDMObpLnhzaVo20eWjZT5vmnXTITC5AgZXswW49iJpVowH8ebzr_mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=FyyypmnGjue3SgU6tMhVHYCcx_O4VdOxoSVKSyC-SVZiVfqDtlgEYondLjNxneKBKVlCINtQ6GPgKvkT_AfviMqRsTdsGAC67GN1F0RTWegm-AAyLCK95V6ZXAAn5JMO4tYSe_UrfsmQBZ6h3-mk0U51gm04UIWF2VxGKkl48-aMaV_w-5W3TzMJf3JEHBcDm_uuaPwK8LUXmSecyTo3qHLQwSNFHckBgOOk3jD4e5vVQSIsO86GpVm0Ud_-oZYv5ThSpsGopLQVXaeTlistCBGoayxeGksQTDMObpLnhzaVo20eWjZT5vmnXTITC5AgZXswW49iJpVowH8ebzr_mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9C0pxBwM60fq32LfaJGClS_fVGHUN2urQeifWe7hHaRN0guOg2vXono6G4070W466Jf6g9n-VLR6RhBo0rVTFkr79d5uVwlmdiE_5Y1RoLX9j2bKxiBHh2vxG_k_9XTl2vOkBBtmpqirgrsa2eHNOdeOtSZ9KPrl3ySQQEDTwcqBpv1928V5wqFLxtqUpctjWqpUF_78KrtDAjHW6ununVAL1o6IwH421o-nxjLTQEZNZfz3ACJQZZLKfKHE1REGk4V0rPt4UMt7QNp9VZC3m1lAYrrwHS9jWUmJ6tgX1MvGhxDwetiIXKv_IncKTypA6zNSRFn1ol6PmF5ItqtfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=jyaL_Mrq1TpeAQ5lgCGNv_0ScOZgju8fKNf75-fUZXKvnjNKJm4FO9UDQqpZTAvVGG7NKO_eev4paAUX7zx_oJVgkpQOensasxr_ndcyXIqdWF7TT1Sc5vBebLeRnY4AG8IyH1TPjcxA9XZ0iew0R6QZHaJyL39jjwxQnL0yGFRJ9qK44_aEkpqCWMR7n95Vc2jVXm2ZQDVuJP-4i9-fsobJHwFL3NEfUDRKAYZjcgyPKPdoIWSMLyK2-gRatBKC_kjkmBAkP60-WkhjJoTAePMygFIOyksSJZoViJNwtbYgb3mRSNmHO5nul6k8uhtbToA8fpqHBQRUTGo21jlE_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=jyaL_Mrq1TpeAQ5lgCGNv_0ScOZgju8fKNf75-fUZXKvnjNKJm4FO9UDQqpZTAvVGG7NKO_eev4paAUX7zx_oJVgkpQOensasxr_ndcyXIqdWF7TT1Sc5vBebLeRnY4AG8IyH1TPjcxA9XZ0iew0R6QZHaJyL39jjwxQnL0yGFRJ9qK44_aEkpqCWMR7n95Vc2jVXm2ZQDVuJP-4i9-fsobJHwFL3NEfUDRKAYZjcgyPKPdoIWSMLyK2-gRatBKC_kjkmBAkP60-WkhjJoTAePMygFIOyksSJZoViJNwtbYgb3mRSNmHO5nul6k8uhtbToA8fpqHBQRUTGo21jlE_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCmKPMq69yjyMa7UW7qfR07mKT6UpbtUQf_XAE4JZ71Ck6W23gEJiOPcNuz8P6_mly0iKjdr28NQHOQkDDdT5Tz2V-7y3YZ34nCrHwxe0r_PMEsyLo4N2PbXSc1TBfFWYFMJAmnJzEX0apvvyvyTvR3xGy_6oiu3NsPOOUW_nZOZXVo8cOm52S5NRq6sg5umbocqEwufTi_P4BW1NDZHbv9wI3Q8KguWfRoFCUr5mJMs_MGeAspexGhTIDsNy1F8d66zvPsuUcT670rj6ReRVm-V1lKvf6MiNOuEQ4K-qnuMplMdr4WXB-vsA6PFrikPQexzVq3XUrvBlx8pUs7dXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=rezbKfpIAba8oIgLLXuI2wLbl2IrrSjy4Srpzb3x6rb2BClvl5gP5jgnrLBGi300wNs3DAYHKgeQ0yJRXI_kosnmUao8ulwowSur0ebO9Y9YBxca_scTeeeM21X8elnN26JBeYaGBMaHXWY0Wlt5rYsqxww2Cvm1vh4jHaaIE7SgWvDSX_gi93obG7_yAJEKie9LfS19fdSeUrNUVA_dGRnf7-dxKNNit-LnbSwz8cv9tptuIWc2YkrpFg2tInY-r6SV3W3FIw6bSMq54zszsLsGYFn84h35Gu_w-RRkmzFzpjCT221MsQty5176p-ukNlTFkhtr3oLwUQ0_3cVwuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=rezbKfpIAba8oIgLLXuI2wLbl2IrrSjy4Srpzb3x6rb2BClvl5gP5jgnrLBGi300wNs3DAYHKgeQ0yJRXI_kosnmUao8ulwowSur0ebO9Y9YBxca_scTeeeM21X8elnN26JBeYaGBMaHXWY0Wlt5rYsqxww2Cvm1vh4jHaaIE7SgWvDSX_gi93obG7_yAJEKie9LfS19fdSeUrNUVA_dGRnf7-dxKNNit-LnbSwz8cv9tptuIWc2YkrpFg2tInY-r6SV3W3FIw6bSMq54zszsLsGYFn84h35Gu_w-RRkmzFzpjCT221MsQty5176p-ukNlTFkhtr3oLwUQ0_3cVwuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqoE3pCRAQTg16ybtY9RpuX3S9CrCrFHoP4801QGmrCQQb3Rg6CnIsiimNBxYmz0XOD1nxLNGnc1VWrUhHM-0xCPYJrWaBhnL5ywscKlMxE5FHYb3LKbEkboR9ZM6OBHX-xBjhw81L9zMQUkt8cFI7GQknlc5GdIeK3h8YXU6u1i3WMziUzTPmp6v36YYkUB3Xk5UnHPrCB7mp9Hlux00Qc0rZVrxTyRYH-j8aKiI6eHFY4mYAZ1LyALpM0w2OQvydErh5kZkhQxaF3xbJmvx817qBJJiBEwQL5Bhd-8bL9Vn0kgBa_gkf0DKe1bL-nvXNkcIkW30BkIipNr70l9T5OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqoE3pCRAQTg16ybtY9RpuX3S9CrCrFHoP4801QGmrCQQb3Rg6CnIsiimNBxYmz0XOD1nxLNGnc1VWrUhHM-0xCPYJrWaBhnL5ywscKlMxE5FHYb3LKbEkboR9ZM6OBHX-xBjhw81L9zMQUkt8cFI7GQknlc5GdIeK3h8YXU6u1i3WMziUzTPmp6v36YYkUB3Xk5UnHPrCB7mp9Hlux00Qc0rZVrxTyRYH-j8aKiI6eHFY4mYAZ1LyALpM0w2OQvydErh5kZkhQxaF3xbJmvx817qBJJiBEwQL5Bhd-8bL9Vn0kgBa_gkf0DKe1bL-nvXNkcIkW30BkIipNr70l9T5OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0f2XRKDWPC89uE_yF4ZBBoucp4IKd7v6dv-ElSNSlOpqkHxkEgDJnzJ2E6zOAUte4UYof7aXxM9gmGttiCP0610M30hEB6poSsAubprxYE8di0gM71zAJ_6kRogG4W92mDf2KJ9ca8aNDrPiUrQW2oDsIROUuatomikB4fKCZa-S5_9UDgBmUupk3z8WoJStMS9Ftk0GWzJH_GIWYFVM0BrFWtGSs4RZMWLxF3Xmxg8nYIXU-X58VDSksoKe2qCL3zBAoJCa6wcur1nQkFV001rC8enrLu5hacclgEiyR507yVyEZXxH1rd0Td9dIx579oeR_7Fl-_5zFGDMAPE1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=CLyDU8i2MjXikBd_WbAzFeIAJUioPfx5v2jH3JumD3r6E_SVzgqI4-BVE_h1mW45dy_xkffwq0MSxQ8BAQ0oHjSQ4ffzY727Ktl64Oz9QrA-E2IWGhdr8VZflCLUFaxsUmzFiic0b1jDlNQIAdHF57d2SpceBBojEFXs-5oS_8KUhZKtsNMAJPlaHMQzjO2U2JYL3cTN-zKlpLdy1LA96L8PZO5t6AayIEL3BwvK5lU-kuX98_yOZ7TcFVbwHZV2SMd4_W71SkFVQKRpNVvANzHzYrTugeso3rXv1NrAShTGbZH9FPRhIJyxmQioyHFq3gsu7LnP0ez2CSiUSKCgzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=CLyDU8i2MjXikBd_WbAzFeIAJUioPfx5v2jH3JumD3r6E_SVzgqI4-BVE_h1mW45dy_xkffwq0MSxQ8BAQ0oHjSQ4ffzY727Ktl64Oz9QrA-E2IWGhdr8VZflCLUFaxsUmzFiic0b1jDlNQIAdHF57d2SpceBBojEFXs-5oS_8KUhZKtsNMAJPlaHMQzjO2U2JYL3cTN-zKlpLdy1LA96L8PZO5t6AayIEL3BwvK5lU-kuX98_yOZ7TcFVbwHZV2SMd4_W71SkFVQKRpNVvANzHzYrTugeso3rXv1NrAShTGbZH9FPRhIJyxmQioyHFq3gsu7LnP0ez2CSiUSKCgzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=cSIW0S5yPx78smdb3G5cKDlQUwFqX8vYsboZaNkPpYhIIY3f5PjntoS7jzKCCn9agGleNKzsK6D7eYZdFdvnwdIFidpsjPojFgKWokIAwxoSHnXQPGBjWGQoy96gntkIZy8KgoVkWi-2yEHfwaNtpinfp2-hnDIb6s4O445i7DexHP2aQocpIoejwyNr-q3to2xtbDnGVLEXj_sB6qBI1xVZi9D8ZY-mEBfvfy82icm8nRtPCZDxLEGIgnDtYrR5qJQvCwmu3-9cS28sR0x2Rfj2jh5k6LF2OjbnkErJBtJM8du1XzbFG4cIxixzTtPc7YTh9_W7rnC-wlR4x74cdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=cSIW0S5yPx78smdb3G5cKDlQUwFqX8vYsboZaNkPpYhIIY3f5PjntoS7jzKCCn9agGleNKzsK6D7eYZdFdvnwdIFidpsjPojFgKWokIAwxoSHnXQPGBjWGQoy96gntkIZy8KgoVkWi-2yEHfwaNtpinfp2-hnDIb6s4O445i7DexHP2aQocpIoejwyNr-q3to2xtbDnGVLEXj_sB6qBI1xVZi9D8ZY-mEBfvfy82icm8nRtPCZDxLEGIgnDtYrR5qJQvCwmu3-9cS28sR0x2Rfj2jh5k6LF2OjbnkErJBtJM8du1XzbFG4cIxixzTtPc7YTh9_W7rnC-wlR4x74cdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rj0GSPV3uypjg7Vkumf1dVmDmasKa6BoqPsbT9eY9r4g0naeN9EUEoXzdri3E1OKIqQkQKvpKC5j2JJaX4-c1iXnLpR4b4SjDhqZfKdBPYo4_C0_SzZV0f-oPhCb9r1j6SMpdU1CHnm_9vzSra2ruPBV3qiZzewD7iGBSFCm4HXturu73vKHdXgF-9qAQiGY2nt7IXa54dxnBNbMXEY50ZuMUXNeIveW4RscMakb0t4P98iH1kQ9PX8vwD_Wpq_9UgQC3WRZAn3SynZlWzEIASajl1W8GgxdvIZ3Y94K23V4_lhlGv0vFFPdJow4kDFNFvnWdOOGAt5O28gM6mtoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=FJzx3TxMCZmSogkvRVVbXgQgQ7MAkCDceb0I5vS6rB6g28AnU-K3x-tcDk52Ry3d3cEWzDfzwyfylo_a7sfqLjMFM9ZFE2sdyM7adIWy65v6g_38YIEg0JHb8uU0P54162FMp6Jx-p5kFYjyrvNx8AiADu7xtrUwMkfS-4Qg-2M9jrJcC57fbyqGm9EyqNakSRymFSXGlrZLY3UFNa3Z4qScDRb5phN5PQZMOR9BnY1R_faPuiREGxZ1JT1j1mp9xzQUSUINtWjcZJVCqtHplSsYctPKOPl6PFN1G4fVMS6UU2sPC2gIC_nshd1kl7tYDpOYClamlSssSlNCOlyMPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=FJzx3TxMCZmSogkvRVVbXgQgQ7MAkCDceb0I5vS6rB6g28AnU-K3x-tcDk52Ry3d3cEWzDfzwyfylo_a7sfqLjMFM9ZFE2sdyM7adIWy65v6g_38YIEg0JHb8uU0P54162FMp6Jx-p5kFYjyrvNx8AiADu7xtrUwMkfS-4Qg-2M9jrJcC57fbyqGm9EyqNakSRymFSXGlrZLY3UFNa3Z4qScDRb5phN5PQZMOR9BnY1R_faPuiREGxZ1JT1j1mp9xzQUSUINtWjcZJVCqtHplSsYctPKOPl6PFN1G4fVMS6UU2sPC2gIC_nshd1kl7tYDpOYClamlSssSlNCOlyMPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=DOSiU3coLjI6VEM6HIcx45yGfHYin-48r_sJZFiVb3bDu9njHnHp6lLrhkmKOq6ZRK0YTPkqtmfYjx5NSjsN81WboIicQZ7Gd3yiLKGb_bOCvy2EUBwTRyPlDQaFuM5bymSxMZBRH7RUrbMGceScHVp-t5MDRjS94JoaUcCZlClRpZCWfVkpqIQgNC8t0cnMzqrCmbKm07fubUqjznqAyViEt_YqVIdXMveIgwzBRCaGT-HKiVnNjx5pcLJ85nW0UPKUOhy43eozhTb04s1u7LA-OxrDMjMhr0AFckl__K6ZkK2jSKV-n60ZaMTQNZFVIlYjkj9xrxMr2wd7E6RLZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=DOSiU3coLjI6VEM6HIcx45yGfHYin-48r_sJZFiVb3bDu9njHnHp6lLrhkmKOq6ZRK0YTPkqtmfYjx5NSjsN81WboIicQZ7Gd3yiLKGb_bOCvy2EUBwTRyPlDQaFuM5bymSxMZBRH7RUrbMGceScHVp-t5MDRjS94JoaUcCZlClRpZCWfVkpqIQgNC8t0cnMzqrCmbKm07fubUqjznqAyViEt_YqVIdXMveIgwzBRCaGT-HKiVnNjx5pcLJ85nW0UPKUOhy43eozhTb04s1u7LA-OxrDMjMhr0AFckl__K6ZkK2jSKV-n60ZaMTQNZFVIlYjkj9xrxMr2wd7E6RLZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=H2iJu-chLblzNFJu4ds7QLVlNi2rb7HfWP0FYE_7rLoqVfiOop_tPKJtM29OTlWDRAdq4Nw5mznWC4e2RUJJH5aWUFMCM_6rLuHOzoMmqDKR5InE7CCiIlC6TuNAxFruHwmoJo9AESUTEclzSVNVO0cmzyNNbn3nL5cwaFRyOB5K_W6VCHqx0M2NT9gpa6JOZNy1sAH-t2PvFBu7Ly7769rpzi5XSe5c9tmnlJ7pB2lKMM2wSMBKc8rAYc2TdtYa5Iv3Go9pMsWyQ6QFosanNnhye0drVJcYkZBQ2GQ_Kf8EG7EJbDStjcRTmFSspBObS5uPG3jtE1JDRM5pKdg_1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=H2iJu-chLblzNFJu4ds7QLVlNi2rb7HfWP0FYE_7rLoqVfiOop_tPKJtM29OTlWDRAdq4Nw5mznWC4e2RUJJH5aWUFMCM_6rLuHOzoMmqDKR5InE7CCiIlC6TuNAxFruHwmoJo9AESUTEclzSVNVO0cmzyNNbn3nL5cwaFRyOB5K_W6VCHqx0M2NT9gpa6JOZNy1sAH-t2PvFBu7Ly7769rpzi5XSe5c9tmnlJ7pB2lKMM2wSMBKc8rAYc2TdtYa5Iv3Go9pMsWyQ6QFosanNnhye0drVJcYkZBQ2GQ_Kf8EG7EJbDStjcRTmFSspBObS5uPG3jtE1JDRM5pKdg_1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=hGyVyB6elpCXVa8dD0LVLZ3oKYdsD_DHaxvfY__JNqG2hyy0yOiMkcKo0_SooIagbKoq_KLPGPLhswI8_d64_yEFIu1yZ9bYPUZbUW5ExZq_GFbEeuUUeujLeFAq0QLFQyymE9UjQfOeRPVcjyF8IoNfAmFI4PR8FvHjPG5bvy3Rhzt9ge4tNCXpqC5SyGZt65sdjoXzezLPpmfZxEuaJslY6xwJFEWzY8mZQJWyPXb5ZHfgZnWtbvZ384iuClTXxdZSNhWJOlHyBPjJmOw9qXnlsJ5U5m0lwhiU6llfUcn4VtczDc4ZKlV13_Idb-KEQvuEN-abQUpIxzAlrZtVWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=hGyVyB6elpCXVa8dD0LVLZ3oKYdsD_DHaxvfY__JNqG2hyy0yOiMkcKo0_SooIagbKoq_KLPGPLhswI8_d64_yEFIu1yZ9bYPUZbUW5ExZq_GFbEeuUUeujLeFAq0QLFQyymE9UjQfOeRPVcjyF8IoNfAmFI4PR8FvHjPG5bvy3Rhzt9ge4tNCXpqC5SyGZt65sdjoXzezLPpmfZxEuaJslY6xwJFEWzY8mZQJWyPXb5ZHfgZnWtbvZ384iuClTXxdZSNhWJOlHyBPjJmOw9qXnlsJ5U5m0lwhiU6llfUcn4VtczDc4ZKlV13_Idb-KEQvuEN-abQUpIxzAlrZtVWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=BbHKZbdNXxC8ypBPTYiFIHmwKANXOJyNNJb7EV4raIuQI50EYKH5gAsIDE74lOUh3vs5OuY5qJhP9ixScm_9-WnFH-yFE3owLw0moFh3cvvl09ggHxLumavY1ZbEg5YK9kB1kRmaEBs4jv4QETdENtoi9RopX48OtlnvTkNGi0BZCyTXVImjev3NwW64WzPrKyF9ycssTpS5f3FdGL5JQKa2Scxv2L6sRnghzymolsEFRimf8pfh6Ha4vhdjS19zCvEGKexlhpOadGn3W5hHG3bgrbPPWJzQeKPyKsLhfeLPvNExjn44pxBkdYZ4f5mi7DI6B2ZYWOZc2PEUzyaVNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=BbHKZbdNXxC8ypBPTYiFIHmwKANXOJyNNJb7EV4raIuQI50EYKH5gAsIDE74lOUh3vs5OuY5qJhP9ixScm_9-WnFH-yFE3owLw0moFh3cvvl09ggHxLumavY1ZbEg5YK9kB1kRmaEBs4jv4QETdENtoi9RopX48OtlnvTkNGi0BZCyTXVImjev3NwW64WzPrKyF9ycssTpS5f3FdGL5JQKa2Scxv2L6sRnghzymolsEFRimf8pfh6Ha4vhdjS19zCvEGKexlhpOadGn3W5hHG3bgrbPPWJzQeKPyKsLhfeLPvNExjn44pxBkdYZ4f5mi7DI6B2ZYWOZc2PEUzyaVNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k32Y_j63kHh-0BotrORzafR1XL8aWWAjd3ajwxikUB_AXJdXDrjesq6lqCW0YoaNWuMDcaNf2gKw1NfKtI0zEpd6crbV-cZObj96eFXsTyKrzQhwivHVr-zBztZUnnjs-zxahWkRfy7pscDDpAu4ycLbjY7xn65IyJPsO1BoYyEZMvPfJPvvZu4woEyva2eX0uaIPoNAyaE5ZgOwdRD-3e2TQdRO-RS0OiBGxoUM8koBLotHobzviY87yCRkPnKCBlZvJ14_-R9OE6In-0RAufOSf9inDmTDitFMw3htLD3LOTQZubYv3RuJU9gcIz56WIJQZcghrbGg-OyGa8AGEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVVC-3D_Iy3f4ixY-3a_rEuSKlPYmagbjAVC52qUJzjzQO5PCo0rutc1DQr3TPGzOPlALuNTDet5GDE4ztBEOd1MxhztmppTHdQpP5EcFiXUtl2ZtajAzilFHkfv9c_MvDdrKB_tEeYdtMadnpMGSR8Zq9pBkI38IXT_AXwqqZEBlq7yy8fjrhmiOSVAkL5UIUrXJKkUYsxn3PlRI96CyT9IXuE0lvaMYydZGIG08n7cCbPFQQ3GudfQU1fNeIkrCc41bPlWpcB-5th_gHjXo2EQyssydezeX67JgPV2Juv7iEswaVYnje70TlxbFNt6COH6gYV6RNl41-LkOHQhOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA6auQN9SNIFf-aAZaVgasEHvKDWv5ybbAWEYTU90Tgy0yJCEiVNieV30nRPitryZJ-Kiu7c0U_zZNCxmd27y8MWLL_uQzYsLvpDzvuDyX5Pkpyg0ddtFLRQTmRPlgyIGaV65p9fujoOc0KE_QwhpVNABJkJ6mkShP-gOBkQThH589yUTfY96kkwfJdLDu8xJHMjl1KhcHOpdQ1J1ofDOX9lL2orPyHBk6fJlMol664uN0jI7hJpBBSMY63QgqyKJ7MIcc5qw4629fg8PJLGt3092alHRRXUeVJTvtuf4v6JELRYeD1gURuwK6BVkPQ3Oo9EqexW1cU1_sDUU_yxzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=IcsDkgUIVOJXS8ZU4l_c4e6Tr6iB2_8lba2He5HQLD8w3UP4vf6FBjTqqgrZVhcjEMMIltoopFi2miLPgKZrJQ741_6A2MMOSXDM9jZ-gUZRMwsf9L9n82P84BGYv6OXeiC4Ywann60sRP8MCDTiVgeUnhhP_R02eUG4y0dKy1eSll74ipavyhXGu6JsgjLCSibXnM4ICXQ11Y6AwISoYyY5I0IG2JmB6kuFMfs9VirWwpXw3UyQXHg2yS_0IlBR3VkuG23gWWHVDU5ldGcXU0jDzBf6idqrl-GVxwKQOdiZdTmZaYG9bBvP6YWyUEzc2MPP86jOQvdmPM8R7TV3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=IcsDkgUIVOJXS8ZU4l_c4e6Tr6iB2_8lba2He5HQLD8w3UP4vf6FBjTqqgrZVhcjEMMIltoopFi2miLPgKZrJQ741_6A2MMOSXDM9jZ-gUZRMwsf9L9n82P84BGYv6OXeiC4Ywann60sRP8MCDTiVgeUnhhP_R02eUG4y0dKy1eSll74ipavyhXGu6JsgjLCSibXnM4ICXQ11Y6AwISoYyY5I0IG2JmB6kuFMfs9VirWwpXw3UyQXHg2yS_0IlBR3VkuG23gWWHVDU5ldGcXU0jDzBf6idqrl-GVxwKQOdiZdTmZaYG9bBvP6YWyUEzc2MPP86jOQvdmPM8R7TV3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gguXggh3nEssjkk94bffQGpd5XxjWBNSV_rfS-b5J_4vNUJ5n8-jrM1wfcIJlJ0e6AxVtxrZTzBbGAmtMa18j3MKOolRJWRgSi5sb2WaMeCfoDBTn9tXQcmZMhVcZViGpyyQ05UCGa5KtSyaAzlfVpnmRNGldanpJ1bAmUCcWcJ6PqlaudVVNEyxzQkrB5nYkIDoGmhcSquKNjTRq06hTR04pmEcKRHeJvnFIaYM3eWA3dyAykhvL8nHkRWjjhVmsBHXPt0XsucseDIdfvICS6ea3uyC7qev5OdPqILpxdla5KjQAjWiYOzWgN0bJ9OL6YMSym0sRPbdoyL9wvy3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
