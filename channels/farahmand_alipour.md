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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 12:34:36</div>
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
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHyP78d_fSmY-vAEqFik2l7ZlkGJy21Sx5I5dXjWixnIxpRpKMQdGkAI1Oq1KSAenwWGwTeB-J37Ym_eptTW1CdqlhbHYgkJxls9JRsQ6XtTkUONkJqS4JY2SPk50aB4rZOLXPUJiFVeAy3u1w6TP0mONF6NlH32w-dKUTKJRoz7VaBhNN7Z95b8cIM9PlEwtvH-zGzX4l1FtoDauqlw_SNW_Xu1nKSHmCoNkqm82SUg5FXs1X_dz-73zty4MuzmLJ-735vEf_LQIWyQ50EBzG63ad77roh1KcQEy0tAt6VCjwrdaVW1OKXmh-XXe-AltoS88ELnyqYCKtTLo7lkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFoTgLRG-08-wXkVfnmUjpyU85d5MEOPeSE2RXukUJ7gcjmFTYlZCb_kpnQL7ZIcAAM_lDv_J4qZLl0hoiuQRaoKA_6j-aoodXfesfc3KLW2-ibWZjxvxqxsCsKOE-w13vSFR6YCpn74DYo1NOBBYyEvAsrIYpZHslnt5ahw7Y8rBD5zD72zEjJb8Xbr82oFCT3fbG_O9-gKukh3C2YomWyaoxAn9HMpLntkpivRZrpZ4r0DzEYp8eqAocUxAJO47HRnA1D8xjLyMZVi-YwcsKo3Qk76hvz83eeZEW9VoL3t6eBs0cX36qSbGuiRA1OhvmzravFHMOyi9dx-QJrwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6fj-XikOE_vV6gn_Bc8O6-xIM4wgXc4YypxLCBQshzeZI2ex4bJps45gE5IffGwgyOcFmOIBXpQ5LzCUMaN_tBTveENWfWCKP8xENhazzUOnaFAp2M-41EK7Ymex4ZhS70FmJAmyGgh9BYHdlF6czYGHLcTQPXfB5Pl3iD77I8DjDXJa0sUIEh6zuEi1VR39aXBilQoalJgeV9tVniQdu1Klpw0ZHKxsgfSfFTz0JXsGf25mcyADsfQjrHKuvlh0iIPGCR6LoO9Jd48T7nKZvec_4o_-CsQq9qSzSvN6_jHrdi6Ysi5U9_kDIWzg08jSHPScvB1Yh7KR2t3-wfS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbIJyOE2Zg99a7z3TD5mDWj0vjc1vH4vH6eeDCZB033bHtcto7zbvY8OM41MekdSJL9DlcS9mLECr4XoRiKdft09qQFx0vnI8Uf4DSB9UJ5SLtKNYr4kzEbFsDroDdylLGJ1uLB_MRRgKpUuLhaWn329PoFDM2Mf7VIe_Vfs2tbR3FlpSShbyJ6hYHVPN45B959Ufyq7LeVRhGgU4i9RBjDSuvUrTRx3kAfK39tQMR-B3y8NO69Z17tPQoOft3RC91injyqPAcnU69MuP_c5i290F9K3QcyL0s-jszxBquiXLylYWfTy2J4tucAQBOGLSqhVQS5QAUus7_jHfnFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBCdTL9seDcNwGsIb89YYMmUWZ75YhupG5WpItG-REVUvZfiD6KHiROnXkLn4fzdNEvQCBsplLIerYuH0UMUBEtMsezM3MC7ZKK7Py0YFkm2H0O6mZei_Fnzbygt7tAnrp_QgM6h59w8uxsGJIyNVQN0aLBYMYZwuWWVtE_nnIqjCdwrYgb8nyJ4K2r6_6FmvF1cFmuGuqTGjxgGNBAjAkenwQxu9CHL-SNdywTVANS_otcnr7RB-hd3qv4e8yGeMKp9oah80UsGtFRxbWjhdqYY3e5LcKoObVpckCAzAsFgLiWr1fFP9YOF9Blgz6KLpZDuv4UTBUShsOAstb-pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_jklWp-P3SyRXbm4_EDnMya7QubfMI49g1j4w_VhiPn-iZO2Evl0qL-0_yfAfFGW06qtFJ0UHnNf8VNKezps_esDctb0ISCH2P6bquT2fhd2L-LWktS049d0km2_qfc_tzlCR9l4PnCDawud2NIK3WyD1SKzbAZDNNSsI9Ag2I4XDPwulWsAhcmD5ckwtPta7cd4Q_2LgsjjzJuSBgaE4NfL6ji8a_T2wKx0RQoUsLXHxU_QD0i-XsiaHSvD88FEIKUiIeua4WC6dHLfzg3ljE_VPOoMVDG_dxu9S4sK-nc3_VHIwtLtU2D0qQOoBR2AhqMam6Ajzxy-v-rz5Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLFj6blG066qOc9Vz59KMvvnEt9kXhpJ-qtpAmFfW5ICohqG4FNQbWoELS85GqFKPesMMQ0oIfeZTJVY-UBuixdjzb57WF9FRUwO7fSY_zE_YSTtvWkrwiIUm2vO2p_7aXcYiUh9MxrcFc9j22DyifsmU4IGvvMZCwovXGmVQUWCILGwMwwid2CfDJ8gyH-a898QpObWojN6z8_9nSXZslXvmd3cLOi3Mv1Tyvs1VE5qQFTsUJnUtIgorLz8krnFxK_6LS-3AeLXwgACCRvbgX0dymYpAbeS0kksqNXta6BKMCcSOREawZwACz_9ToLVmNrpjPs21FyGGKWgGaYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW3Y8wkErEwjwhOu146AJeeXna-1_Q0yQHyVoQUogvuEw84IQQWdhgrcwU80wv9tXG-1-1jTExHEOTwqgh0A15l5iYi9CWoppsIWSS_H_9MqlPO-ExhLP2LqfKuW7q3xDK4o2mdX_UoqYv7uPLz_u6ilcSEtzGMwSEIrDajTgLwW-XHDpJZvpULYX9Nmzv8qJtpy9PZuvcubBZXBTiJ92E6mS6ggwrjB_PG7OV5UKWrXZQCzHSFlIUOOE6JmN3GhWMWGj7vpEg5yt4XNt_lIBZmLVrNJDyAXQONcTbZ5wKvksbzWFVuWgRJTiWIsxnT8K7PmpZw3v0Ako2lvBbMjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftoT0vHGzBnDY_XOgrbM999A50vu0U3HCEN_VD19MRDlKDrZhadB94T8TrzcNVRt85obQoUoJlZuJK3fO9oEmw4y29FrXCXwTbD_uGmPLdIeQCkoycDhgOUajra1PbFAt9VMcv8n_IHQ3SHNWnGxGXjVLHBUO55RjZzf5ftn_evCkOxFDKjzuTt0TUvZjEPYx3OWH9NLgMRb4TmkwxQfeP7eyvtHE6V5ul4OKgv-3bLHn9tJpWBBpZHnTHEQ2wJppZGzm0FF5ydGr_3tDiyBeExW8qgAtWyFe2c8Um8pWnXv316Y1cQGaND5plapVjmBIXdW2g2xBfNyjqXDsYpiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBuHBmINNg4wiMez3F-XCUwCh4n-_2LP_GWmwRlvnv3TFyB8RtDkVdxb-Zy4nGNuP-wdA10DlFbZHZ3V7DqWPXgM6jJi_nBBZnfe_VWYMtMZVTwM3Gkw2PHhpNwx5Q94VeSu6SgJCCxIPXPNGYI1f0EMhCXR44ZpGDsZeziddZoIIatPBWIGUFywliuc8Ua_-t0R8rx1NXDW570NgtDN5LEjSln8aVO5c1ZPYPUopYboMTfzkUbascvXkreIKjppVfb7XzKleq3GoqDFwbxxxuEigMvroiMAWjN6zjiNAYNdzrFWaDGyALxHEazfkLoMoyO8bvmEuGzgrWQgGpGQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLCKaWezzyHSKORv3MC7EKmc4haiNX757Zw7SO7A3uvzi3uxNn1LtSepcRMgKbfZ8NYL2Wh94Ejf1MA6apDzwrrpqC1ZrI0yehSgGkO7fOjXOcg-xb1pdHULhGBotwmon046Znsz4f-6mvJPfs0o148j9pq3yr76997RzKvUlbDT5f1xH4hdqb_dO2XjLNswxuB0dntGU9IJnfGcVciyeheXzTc4BsUUgu97xkDmPohqsPAV2bQUry5PmpyS4en1c0t2m1wDRFJsWD90U3XcLGHTGEBENedOS2HzigXKiwRqAr7oNIH3imylijf6t_tTg73aQl5hmLqz0JVM4WoXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7kguok9aVsp4Xp23i1hypt1bR8pPQAw5mcqHhk4k-lybxBtPKXExXOvvhS9s79rjlBKMGKJn7ZMgWHzFvChlIKdXJUfAG2eQKD3STHmQahkJp9lfKwrZV3_t0lZv0AGGiRnkmFG0ewY9u6Y5YC9klH7ZMiW6yrOagyIB7VDc52FF86ZL0uYU3GtIXkslWzc0Tv6cDgkVeoGtsfdQmwimr5MG0Och-3nwAyme0TD8nMceDGaerhT9GFLTNKKIya0-qpa7C8WjIS2DEu_EwavzUfT6ink6R6_Z0L2D9XCp3RttgpJsIvzFz6OtjVhBu3UdOcpqaRTWU7iylwo_4Li4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi7CjSg9YSCrbgGdPkcay04_U6jM3eyGe1yzv9ylk0ykllHXir4IneNM1E6Lwbo8GU0a3qJN2IWEoGiJnXnJJtwwLTT3jMTKW-W5AYuBuy1LoxgKBtuDcex8KsZu7K_BuABVE8wgFGm4Ldk-Pq1y-i4VfGjgBCoIdHB-IGdkOWJSrgFbxch8XTn6dekqF8D3srkysPPtel5r3zKrKp_kkIp1bj27R7Z3MX2XepE2AmaAlIe6Usaah8JQT4LZFbW5LGxOxo3TCVUwBIYNrozGQIYZipObMAr6VPobAQzsPGZrxHjTPPgKGYo9TBevDDL9-LVD4czbOdp9504a8BavrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlhMNg5zy0LCRazbEWQE7m5vNjN64C1ajUU-sb7Z9BIPa6ujLQc9S46-5hZgHx_OZRc9r0UqedDQ3dYkLf4oG1CbLB0Z9KlkXOeMqUEe9CAzv34y8OTxgFykWzngaXj8NNh1cagzHEKYxzk_tc5QT06wzL5nqcG-h_5cgdVMXZAZZxfcvIKptSRNXztop5TKfJr14I0fJ9iA3Q0CsSu6G4s8fdT8m-j8Gldx3jQvyciaWAZz37sYSFWktWcN577j9fMupRN5Q2rmEyI3iy9ct_PkW6p-4la_BNFS-Guvu0-7aC8SORIAtKChgHnnLTaAX2UAMuk_5uyzFCgtlg8aHGVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlhMNg5zy0LCRazbEWQE7m5vNjN64C1ajUU-sb7Z9BIPa6ujLQc9S46-5hZgHx_OZRc9r0UqedDQ3dYkLf4oG1CbLB0Z9KlkXOeMqUEe9CAzv34y8OTxgFykWzngaXj8NNh1cagzHEKYxzk_tc5QT06wzL5nqcG-h_5cgdVMXZAZZxfcvIKptSRNXztop5TKfJr14I0fJ9iA3Q0CsSu6G4s8fdT8m-j8Gldx3jQvyciaWAZz37sYSFWktWcN577j9fMupRN5Q2rmEyI3iy9ct_PkW6p-4la_BNFS-Guvu0-7aC8SORIAtKChgHnnLTaAX2UAMuk_5uyzFCgtlg8aHGVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qh-FOOr9sC6pyO_ioYMw7pnUm6O6dDYP9l-PS_F_yyMhRDI49WHd2OY9pzUg2A0bbbWAQNYGsDJWJpcKq5UNsv4pJTZZoMK_RBfiXl4n0IxDfv_LkXVk6wBm0FGXGF_M_uUi0CdGu7OgxcQ5PS1CHpwq24uwgrSWB7z_72Xp77iDN2EQ_8e_eKqMY5BY4w3PMeHmAA6VMSaTuBcPsdFfemQP6mbZmUALbN3yMG3cm2MkLryTuAjXll3MwPicw5Cnrrb_MT8LjmppXgAA3_bZYTfb5vu9H6xaIbTizPXj3o0qMeJKVxJEncFxHESx3fwyYcK5b51gE2OAIysRuIzp0X-Y4otUaRSPG-SJDlxqc8xn90z1sr1IgtuYptiNmqbbkEzrmcQjQxdGtjy0o5I3oMl-ZXsswygF03tT-LRYY2qKy_r66K_lKSwlsu6_uEZRdl-qTvC_ixFcxntZSQiXvrPPBjxfDYh66xTrzNyPuBRmca2nuBT-KNy2IG2N6z_ZKKkWNdR4NkrP-6bSPAv_hKPcUrxApEdpc6eHniWahdNQAiERBnql3DoA6-2OptPCK9QGXqA8etDfcSxZLaaPIyQFlrmkuI0WKiXoWaonoTX_w-qq77o6nYgDURzrAA84n69iaWpfXq4o_5bNeAsqZpvQdwZOvMEDsR1TVxtMJ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qh-FOOr9sC6pyO_ioYMw7pnUm6O6dDYP9l-PS_F_yyMhRDI49WHd2OY9pzUg2A0bbbWAQNYGsDJWJpcKq5UNsv4pJTZZoMK_RBfiXl4n0IxDfv_LkXVk6wBm0FGXGF_M_uUi0CdGu7OgxcQ5PS1CHpwq24uwgrSWB7z_72Xp77iDN2EQ_8e_eKqMY5BY4w3PMeHmAA6VMSaTuBcPsdFfemQP6mbZmUALbN3yMG3cm2MkLryTuAjXll3MwPicw5Cnrrb_MT8LjmppXgAA3_bZYTfb5vu9H6xaIbTizPXj3o0qMeJKVxJEncFxHESx3fwyYcK5b51gE2OAIysRuIzp0X-Y4otUaRSPG-SJDlxqc8xn90z1sr1IgtuYptiNmqbbkEzrmcQjQxdGtjy0o5I3oMl-ZXsswygF03tT-LRYY2qKy_r66K_lKSwlsu6_uEZRdl-qTvC_ixFcxntZSQiXvrPPBjxfDYh66xTrzNyPuBRmca2nuBT-KNy2IG2N6z_ZKKkWNdR4NkrP-6bSPAv_hKPcUrxApEdpc6eHniWahdNQAiERBnql3DoA6-2OptPCK9QGXqA8etDfcSxZLaaPIyQFlrmkuI0WKiXoWaonoTX_w-qq77o6nYgDURzrAA84n69iaWpfXq4o_5bNeAsqZpvQdwZOvMEDsR1TVxtMJ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7rmLsYn9b-2eD6lbL_as5vpKZiNTcRsB_SwJNeHwh8llBCHA_1_7euiTkgWBn2O5PGx0HC704miFpvzVmQCPhEnJj4aMrm4gvL-4FS-vRziWU5oHBPOihSfHXxaje_am6kN4VcGqYfHt6loKYQ7MSBqjHidBLEWYKXCViXqxCM99HhB0z3yJcIKpES6vSePKe8whvjdmSwIclrH7-dari1I0uayHu0YbLFqbBoHH3ESU26GCrHVWBWLeV2HAxIlATsLIgbL6i69E3Mp1yYmfTx0RCGg8_wwhGAG-ia44_-IFCi3g9jSWH1x_B6rlMFFm_mfBpOZwBsGZrqCFyY4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxBT1INx4ZbLKu3CJTP-CTWPRIcAVE3URHcODUj9Ofko1qS8ge7NGkXrFuhRQ4lkB7VJtmQQpmV-9X4tR1XNdYwEWh8ybmIULLzUyDI25d2LxK22YuKkvEVeOvmzNDIqsqwasa11WkstP_KYYQvTh5w5Taj_IvJ_O_58eur6Se7HSkh5v5ubyI7503W5Jf-v6MqPN7T4rQST_XfqndObH7LVQmqCvk6QlLaZC436jFdtXTY6WhBmmpH9lV7TvwlnOJlLjz3scPrPBJ9ftUct31DaBM-4CLiy7-pS8IlriawKk8V3LawwS8jnshYQrgH8U3X_W2upFowD_E7GvIhR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLPyfZhgm2_rM15TyrT5NACZIDcWFf4mBPW8MPFU7KYGGFcPN2W0gSbg_WSvjHJPsbpymydtoTEPpUos8_xmlssGMHYoPfLzmC1oG7OZVo-taV7jdahyLM5A8BHUb5BhEoA0iL2gaK4PnsBLnzC3Mh_RFNokO4xpmncx5hrbAcsVKNsz2oo3HhNNoeqw8ENNQCxk0BT9mq5Ic7gCaoOWw40T3XvWpMqqNbBWG7EGx6aNLmm0aglHSIha9dl9CbB_IcK33CSTfaQK-rheGPjnoqdIH2quwbld1Z5_koKhLu8tw1UuHqB-cMw1Q3aVq8i0FAFabBy3epvvYuT88YTnZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vfOT10qcev6fW2yLBa2IHmpHM3HIQwrYVi4c85LumEoY0I9OgFM_IYBBQn901uujggbrEwsBf6mtm_a8FCNJ3_2notIZKjLXgCD_-QqrqxLpPTCzDlfrMX7rxyGpEWXGG3bYtkHTi7_iKT8ifQgsFT5oPf5XsdKsx8oL2ts4Ll0oTszGHPm_vxqUfyDAkM_HQhv9NakJoPKa-zM-3A_Jdq4CScqdrviz4WV15NQo8ETGhk4SCQQK-8ohoqKGX1C0nUxk37FVNFj5g1NssUwY88nw35Qzw99TBZgQcJsOazwoPdlAjpQ7vjyfTHtNzU7P5Elr28XOGu6WpqG6BCvuwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vfOT10qcev6fW2yLBa2IHmpHM3HIQwrYVi4c85LumEoY0I9OgFM_IYBBQn901uujggbrEwsBf6mtm_a8FCNJ3_2notIZKjLXgCD_-QqrqxLpPTCzDlfrMX7rxyGpEWXGG3bYtkHTi7_iKT8ifQgsFT5oPf5XsdKsx8oL2ts4Ll0oTszGHPm_vxqUfyDAkM_HQhv9NakJoPKa-zM-3A_Jdq4CScqdrviz4WV15NQo8ETGhk4SCQQK-8ohoqKGX1C0nUxk37FVNFj5g1NssUwY88nw35Qzw99TBZgQcJsOazwoPdlAjpQ7vjyfTHtNzU7P5Elr28XOGu6WpqG6BCvuwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llDfvr5-DEgo0qR5oI6bKHDYeB_QXo3lcwZGiYxh4pS9Asj8C09IerUCXB8MP6LWgF3UoMDWMSYvzYZQrWAtejpvJyykXaSrTr0HFldV28tUnOGjLZ5cAUi_ItUwIFIr8Af00j7EgCPZf5F7Gv9UAJF_gXTbdmCkQVXBD7fH1E6BJ0OujvZcRPHXB2Qu2tM-NFBJaxGCNLd42_BnPrCA-_WfzTPf2ZHUx2p7wiyMXzMoDdNpLSNZGPGXQwwBZuiPTCRcmoKQQB3B3YyX6ukfuLL0n449qWa_S-t8lGI4_l9ew0Cl5KmdpqvYKC1FuU5aw-JX92qXNUGrGUZ1_ZQQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=j-mX1d4OPQcZd7_0LWts7LKSiQYOLKBV0pMB4VIuR_3foUtY3-bpnek-J4_Phim_sI-aQSIO2r0mGVO7xCUExOvduyEvcJxVTf6pnY8og_ZlPx-mWGzXCQUUwOHT53pxZVvgY0waQwpV2bFojGRzzTxpik88RnLQVKpyoOkn8H4BEDlObD5zA7pdmb14eXKYbqrpx_9nvdEbCtAPHMNny_yYDHbNpxQ83Rxh7F3vUVKl5BK1sJ6m6io61l5Jz6v8J-znnpdn0S4jUPu1wVguxniKc-azTiL-BXfI8ftg-mKOmYDfHZi7idC4fktX9AphHQQq7sNX5CdZBgUwziWGnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=j-mX1d4OPQcZd7_0LWts7LKSiQYOLKBV0pMB4VIuR_3foUtY3-bpnek-J4_Phim_sI-aQSIO2r0mGVO7xCUExOvduyEvcJxVTf6pnY8og_ZlPx-mWGzXCQUUwOHT53pxZVvgY0waQwpV2bFojGRzzTxpik88RnLQVKpyoOkn8H4BEDlObD5zA7pdmb14eXKYbqrpx_9nvdEbCtAPHMNny_yYDHbNpxQ83Rxh7F3vUVKl5BK1sJ6m6io61l5Jz6v8J-znnpdn0S4jUPu1wVguxniKc-azTiL-BXfI8ftg-mKOmYDfHZi7idC4fktX9AphHQQq7sNX5CdZBgUwziWGnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmBU3sKQ0Ak37td6AoCzBUlRmlYVhwsACAZpj016Tgkcn3XaqV8FFOh1e3Oo6G1JjH6ty7ESvU0QfmSJOan9RPJtTcLnfg5jd7eUD__TPtN4wFXhTi-iZBcVWxe6CbsdsM4-xzWKoovOPdV1Krk0e_945ymDiDorN_MZpDCAvNqX2SWcIswINmnRzu2bVL3_l-3R_Nhn7qJFqxnJ-hqJfGpspdDV28Ss9JhrJ6lBI1Z1UEotVjFLvDYjpUzWcJ6fQa0tz6y4EKuZGlTRvxWBQLYabG9AZZXGXJ9VwtkVhr1HYMcEYRMh2V14YZgbjtUvHEi0DGzbXgqIBteu2eMddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSaY-d86TnuAUtif68r5Os7f6ybGg9lK84vzn5TAwC7jJ69UoEbO-btzYBVJd9A2dR8uc7YfDWMabzDpgojQjp4SiqL5H8lZswhQ-UAipVCsXycBl9ajcDB60MYGUopf3HAk9X9Fs6mXzDGwDDuAAyNVJeehCxSAFhEchCeR9Fl0NIo6-SrlMmT3dZUcOdpenMP0jVsh7aA7r7HSBJXk2qKd32nXJUK4usKAZcezOrovvbvui3wh97Rfd9uXJ1jmPW7zivwKXA-l64HvG64BcpoYwmq53tvlOIUiHU2lTFZrWz4P6XxJge8eDfNJ_lRoQshUUIv5DFY5x3PMrfe5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=n02qbO9BXEBb7f5MTsq1TKaVJZVmH4dRA7RHNdH_O3yimJEJgSxC7zlk3L1f79XG3PQksr93z0JAwFj8DNpxe64FIMLmpqmDB2p5Q-09Ekqp4ODNIRufAywpQe8yEHhFmLjQgD-5yKL-aeCqJO9UEQzabzN5U1agjpmqYXrGjgDe-IHeAhX1paQn26Ppy5vYUA9nWRyblvp2XSipHqBWrrmx4Z7TSMhc8hHzDlysCfloFw9kI3IQiF16PFhiqL5eiiE5y0jv2y1pix0lRD1Lc6BSe4COh6IAokkyr3eQrNhT_y3spd97ysVr0ISxmLoIxbtbDjTbtjMe1NYUEB3dwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=n02qbO9BXEBb7f5MTsq1TKaVJZVmH4dRA7RHNdH_O3yimJEJgSxC7zlk3L1f79XG3PQksr93z0JAwFj8DNpxe64FIMLmpqmDB2p5Q-09Ekqp4ODNIRufAywpQe8yEHhFmLjQgD-5yKL-aeCqJO9UEQzabzN5U1agjpmqYXrGjgDe-IHeAhX1paQn26Ppy5vYUA9nWRyblvp2XSipHqBWrrmx4Z7TSMhc8hHzDlysCfloFw9kI3IQiF16PFhiqL5eiiE5y0jv2y1pix0lRD1Lc6BSe4COh6IAokkyr3eQrNhT_y3spd97ysVr0ISxmLoIxbtbDjTbtjMe1NYUEB3dwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=ssOCRPahVaJ3yyEzQWkg-ABPD8p_8K1ILUXZVn-LkVSi7n_zX_CjwyphdWMR_Iev327CRabx3TC6K5CiQBJq9gmi5MxsydEkOGLT1yb1N9MGjU5XAoIn9NNFzocRaOFACuZDRdmGAH19-1OeSi_0ganAucS4ktP4M69brnvTb2TD4JfsG8YFztU1_7vSVVQuLCLSBGPFqrOq7wAuxMitOqpQ3bWmK6IR-unGKyrQ0XxjUxzuSVhWM0KRmi-_RK6iTTZjFGjognTt6j0KePHSBqQBFvpel0A3cowY4JvfXjXOJbFY5O9djmdAJehHJOdJY5NIwgoFjnE1uaumH_eL3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=ssOCRPahVaJ3yyEzQWkg-ABPD8p_8K1ILUXZVn-LkVSi7n_zX_CjwyphdWMR_Iev327CRabx3TC6K5CiQBJq9gmi5MxsydEkOGLT1yb1N9MGjU5XAoIn9NNFzocRaOFACuZDRdmGAH19-1OeSi_0ganAucS4ktP4M69brnvTb2TD4JfsG8YFztU1_7vSVVQuLCLSBGPFqrOq7wAuxMitOqpQ3bWmK6IR-unGKyrQ0XxjUxzuSVhWM0KRmi-_RK6iTTZjFGjognTt6j0KePHSBqQBFvpel0A3cowY4JvfXjXOJbFY5O9djmdAJehHJOdJY5NIwgoFjnE1uaumH_eL3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=qNx30GH3C4VkEQ0s-0PWivga404OwVLimjcAsSbOqaF8dA-_wJBMEHCHCENWGrwjcs14gD1q4DN8mhuB8LWVJYqHrteQuqpmDMzLn5T7vnumzK94z1cTF56teFeWjLgnrvdEPytePUE2MJj9FcGOtPOPKTkpmF57GeAbDkSjgMfxG5bUuH2xlpuHKyEBCsjA0V4U6hOVRTVp3Ntd2ukZGI6jofcpirJvyRxAaJfgorIoRI0dyxqEznInfQlIK5OgKdDjzwkapiyf4K1Hp5FJ5rJPI3EruEvlwbYDs01gDvCof1hLA16wIoY4bjXKewl9z5Ex9VJz_Xxgu7XMWsxfUYIMfZCHfIiQdDCZjK31bqOjdVVv10PvVMPZ7_-eIv1e_KnXXb1AGNzu7rF6ltRi3pS0M3LkEKIbMYkQF73h4vgJ9u00LQhKMiIhuCkjmbfZSmJ_5bmCjgjjI14JOGh8k_R8GtAOuqFEVEFDvb_kbOvCweDV8vTKssiZKkzetqbAdHRoalgektWSf5fr3NzYmnIGUqMsfzIeR6oEX_zLDLtX61uA5sr2qstsgLTYV-hFsn-QkWT65g2RbYO-HeyEDS9DIVodZrshTBnDfvDDH4xv6m6M2uHbgdqBoLYB61KgAYWs9Lpm7FpPdAnEKUkYEzV7Ri1H9X8x1ofFTPH102o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=qNx30GH3C4VkEQ0s-0PWivga404OwVLimjcAsSbOqaF8dA-_wJBMEHCHCENWGrwjcs14gD1q4DN8mhuB8LWVJYqHrteQuqpmDMzLn5T7vnumzK94z1cTF56teFeWjLgnrvdEPytePUE2MJj9FcGOtPOPKTkpmF57GeAbDkSjgMfxG5bUuH2xlpuHKyEBCsjA0V4U6hOVRTVp3Ntd2ukZGI6jofcpirJvyRxAaJfgorIoRI0dyxqEznInfQlIK5OgKdDjzwkapiyf4K1Hp5FJ5rJPI3EruEvlwbYDs01gDvCof1hLA16wIoY4bjXKewl9z5Ex9VJz_Xxgu7XMWsxfUYIMfZCHfIiQdDCZjK31bqOjdVVv10PvVMPZ7_-eIv1e_KnXXb1AGNzu7rF6ltRi3pS0M3LkEKIbMYkQF73h4vgJ9u00LQhKMiIhuCkjmbfZSmJ_5bmCjgjjI14JOGh8k_R8GtAOuqFEVEFDvb_kbOvCweDV8vTKssiZKkzetqbAdHRoalgektWSf5fr3NzYmnIGUqMsfzIeR6oEX_zLDLtX61uA5sr2qstsgLTYV-hFsn-QkWT65g2RbYO-HeyEDS9DIVodZrshTBnDfvDDH4xv6m6M2uHbgdqBoLYB61KgAYWs9Lpm7FpPdAnEKUkYEzV7Ri1H9X8x1ofFTPH102o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVavpFmiu2AIPhFKEXmrdbDtkiQlFiadfd-d-voT975W2-x7P2snQDvXs925KJ0CY6ChXNonfA5SzoKvjKL-7fJ0qOU7334bFiAh65AyRro_VrZWxTBJ_2oV7EkuIuCIQzPtxuLotJzMx0OnJIvr8X5MPFYiUpfceZFOAbFQ2bMOcb0wUYDNRwtq2S7XVYgOJG-ywe8yDEmZhOG2x244Z0trsfxmJoSkDi8EYvBWalMb56IFXkGAMb4IzALf5Qcrf87lp6wFwUWtCom7bYWJuz-gD1d1mNn4p-HJCL5szUg7jD8Vw49BltpiWG7ZAq1gRZ72b567V7EmCkWQ0Vw8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFbSsxvH7Rb5g725TjqEJUVSYgo5dX8S6rEbfKX8zd2xnEz8yziqh56VEvsIZmNRxqTTvKkQr8ORLwHGsmRhrmZTM47B3MQ0CywMMn5mcLUie0CeIQ33xUIxZm8Tf4mUn7ptn2nQICZETLkqbeg9UF74C-NpCYnDXX9yCgL_SU6Cg0iF03ko66TM6oKsvqi_VM7MSPuJC-TxfrVOyqE1jAYM7gU3IYSJgTWndWtQPiwROMSRwbZyivqZu07ySP5RH0YwvIXZGcpZ98uesJcXUo1n2q9D47uMMAx49WR-h6XRm2s5gx6WlnxPOtk3Ilds60AaF-pS6yPFFMyhCX27Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6YGqYGGy4I4ILAY2_y03rRK18VPwfykHJZQuhZM8z4UqWBfGJw1MnPWUQdxGTo0LllLiCQIQoyxn-MHDQKfM44Yn2vcUy-uuD5icmexB0oXSZAYdANFu8jTwWsPqFP6niVbJRpzYFNYrxKYLQdHwItR7_qg5_22FZ3c4lMOpuI4oi35HCgKoasyoJpIzIPwdjShIWQovf-2cyayHWmdavewUN4whVaT4lepaP2w1gkPv5uKLLBkNSQB9qgkXnEevRnlJDPI6X-N0zL7ezWcVS2-PlE7wD0aQmdtFOGGRaPTWuAunSgvqmlKno3THdyJqcOO3tqQe5tPU-8NSEIqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=fbHaX580FuZCdJ6EqoDb1ucdlJJuYxajP4DSeKyl5wG0r7zF2JX9XJDLRMPKkoLvr-MKASmWQifHQbiD7kZhHjQu4QYoln9d8Z94whqo-CSCj6eWF-eOncmNOc7mZ7yTzIcud56usXEq3oQ3Ac6x-OwT7aUzUcCZKKHANF0MiYX_V0AiDaS_-wXZri-2llqKXsccB2Mii39dkd9P4507wvwpjKCl2iNdHcCpv_EKoSR7iiGZUVM1K2RcBzcVB5gGh8lWNq8r5Ii24LC3fJ5gXhYAu008zfSr3W257p0ev0JdgVPodtBR6e9KIBY_rHanXCNhxQw_gw77bsO1_Yn-hIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=fbHaX580FuZCdJ6EqoDb1ucdlJJuYxajP4DSeKyl5wG0r7zF2JX9XJDLRMPKkoLvr-MKASmWQifHQbiD7kZhHjQu4QYoln9d8Z94whqo-CSCj6eWF-eOncmNOc7mZ7yTzIcud56usXEq3oQ3Ac6x-OwT7aUzUcCZKKHANF0MiYX_V0AiDaS_-wXZri-2llqKXsccB2Mii39dkd9P4507wvwpjKCl2iNdHcCpv_EKoSR7iiGZUVM1K2RcBzcVB5gGh8lWNq8r5Ii24LC3fJ5gXhYAu008zfSr3W257p0ev0JdgVPodtBR6e9KIBY_rHanXCNhxQw_gw77bsO1_Yn-hIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=juQXnOfqWphn-0w9u9V42hB6-LBwwCRT7048ifWNuS39uSkvRwVyPz89qnGvnvyX-siL4Iak9O1YVEHV-mmEdS7LqvPCVdqpKjlUy4v_kkF7zgSLkLvXA5Pm5C72p5SPdmJAnz-Rr47G5ixvm_AzXL8MiSWNxlI8HQJUIztDoPi6dKXagOfTbKhC_9mNs1hYs9v-gMnAuJrOtDT0GlhXvLvs0fCmJRBoWmqrhh1MTCsEC-HgbH3haPvky14ZgcQ6aSoV6C-zKwW-dsYFvSB8sIVopNxTX2Z3y2iHNPSmHlDSFf4UV6L78vv8S5FgLcmn9nkFd2Jyd80eqqtT7TQmjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=juQXnOfqWphn-0w9u9V42hB6-LBwwCRT7048ifWNuS39uSkvRwVyPz89qnGvnvyX-siL4Iak9O1YVEHV-mmEdS7LqvPCVdqpKjlUy4v_kkF7zgSLkLvXA5Pm5C72p5SPdmJAnz-Rr47G5ixvm_AzXL8MiSWNxlI8HQJUIztDoPi6dKXagOfTbKhC_9mNs1hYs9v-gMnAuJrOtDT0GlhXvLvs0fCmJRBoWmqrhh1MTCsEC-HgbH3haPvky14ZgcQ6aSoV6C-zKwW-dsYFvSB8sIVopNxTX2Z3y2iHNPSmHlDSFf4UV6L78vv8S5FgLcmn9nkFd2Jyd80eqqtT7TQmjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=FM5BjxwOwC5dtht6pqWkTP9soe961j6EXxFopLodkB34w9K12eseTNvkvGVU9CGEagl_7Ay9c-6bbIYm8VL8WMrP32onTYBm46i6aljbRk11UsUyXfsZPL4jV2UjVag9xFeb0OlBi7l2eOLfEGN9DzZIwgRJYGvrLcgF4CJ_9_cQgV8VFgfmkVcYweVLTqycLLln7iU1YlUctO0r5dVVF9FkF_C67Ww-pG0Ii9Y32TOpDww22XcyzK_yq_-mE0YU6Kd715-XHaWRtLBIZSTGehg_jw6xJi54ly5g-KrFjltxVYKMPwR-MqizueL--zdQFXTlY1W5g9TuwTaUnIprdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=FM5BjxwOwC5dtht6pqWkTP9soe961j6EXxFopLodkB34w9K12eseTNvkvGVU9CGEagl_7Ay9c-6bbIYm8VL8WMrP32onTYBm46i6aljbRk11UsUyXfsZPL4jV2UjVag9xFeb0OlBi7l2eOLfEGN9DzZIwgRJYGvrLcgF4CJ_9_cQgV8VFgfmkVcYweVLTqycLLln7iU1YlUctO0r5dVVF9FkF_C67Ww-pG0Ii9Y32TOpDww22XcyzK_yq_-mE0YU6Kd715-XHaWRtLBIZSTGehg_jw6xJi54ly5g-KrFjltxVYKMPwR-MqizueL--zdQFXTlY1W5g9TuwTaUnIprdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=u704JVjNJFRWWLrGynvTtsEDGKRseCvUv22OgEVOmEmM7xRzrHUhe6m5GGqcZljD1DOVceNdtRtuXse1eL4ZI8-oqaCUULohyTCaigao81quavctSlpFpILy_5supZ1nqsK8_IjP4Ee0dVD67iSRu2T9mWFIvdeaD_8W7BkAOapX08zgdTA3fw4jx_hze1LtFsDkjqbj3fRR52JEK99hcrETyn85zpRw0qREp4WULHCSt_J7V29PpziLBg3HB92pxQf1I8ZpIWzlBVuaDwToaiwpzwT85o8yany7Fyq7Fg04fH5EKD6FzBTbUejLOgFbxQkUUWMuZTw0QV77mifW6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=u704JVjNJFRWWLrGynvTtsEDGKRseCvUv22OgEVOmEmM7xRzrHUhe6m5GGqcZljD1DOVceNdtRtuXse1eL4ZI8-oqaCUULohyTCaigao81quavctSlpFpILy_5supZ1nqsK8_IjP4Ee0dVD67iSRu2T9mWFIvdeaD_8W7BkAOapX08zgdTA3fw4jx_hze1LtFsDkjqbj3fRR52JEK99hcrETyn85zpRw0qREp4WULHCSt_J7V29PpziLBg3HB92pxQf1I8ZpIWzlBVuaDwToaiwpzwT85o8yany7Fyq7Fg04fH5EKD6FzBTbUejLOgFbxQkUUWMuZTw0QV77mifW6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdcis-6YxWDc3gqPpx-zGy0Ir9nCs3wB2EB93IL9T3-6qTq3wSxBnHEcUcEu6vlXStO-MDwiutwfDUlS2ABROsC9dlpobJwHFH7EaG9b1fPqDBrwqcwGjP1s-fvKkIhfzH8QwlrgvvhxVUuT1VKIkhnLuBEglfdg_fNfKFmyK3dVieRHYuw2p6BnAoy6Zo6s957iNksGUpB-P5eQkNQk11LbETpQ8rvDJiSyzoQh1o2pPAo4ubnqden9Vq1z-37oGBH7i3lPVjxIKKYw3NO2PQF58ir8tFdmZ94tf1q2fSnava7Ukvd36KrWg8iYPFjCjPu14Inj0je_ULtaako5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=f5mLy0ftR_xjxI_3q84T3C4KV2Qof-JOG04p5s9okHpbN-QRn8HuYqpqFzU5Mikn5Huo9DFPmrIczRtoaBX61p2Ioz-3AxFtGiR8r_pF6kZj4lAOO6e5jF_IbuH9Cxdc2naDn2SE_QLS5dmGFcYUSVfsqD1n295WkpF5drLUxTr8_y27Nvkqru-UG4Bsts_NxXHHD_mhZdLdVaah1OlbzGyUC23XDMIqkDw5YnSfWXdzBliNYpZa-tWfm4m92oWOmfFCzneaXkofwlT_duybyEr8iRXzUIt-oMopbTwCUirK-mbmDGWkYrqfw1KoOpAEUXWpVJ7q-29bpebkuWLm53NwtM7W1Whp12w9jdVG44yTxH9mNPvV7i6sw9pIuimgtlQDT87XP8_IcK9JtJDqtW__b6oA5JvELs3DtrELmkOK40EfHNECQfXll_FpkwIo4grgh5iUGnGoMwvRqN_AeZbl-AU0l6ma58SqYKqK90seYrVim_LQ403ltLGuNUC6-vDtcJAuzK58tz5q-Dwde_iBo23V4fZ5XdDmMxhaXGUEhNHGW7w2CmZcn6Pew-kUMoG05qLMmd9nMDFcOruovAi1deQeeg6zAPrlKUADwEIDhZdtyfV9JnofHjwT8Ujn-3tidV4B7GEEXL1xRuRdVG1ZfbZbVteyo2gbDla733o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=f5mLy0ftR_xjxI_3q84T3C4KV2Qof-JOG04p5s9okHpbN-QRn8HuYqpqFzU5Mikn5Huo9DFPmrIczRtoaBX61p2Ioz-3AxFtGiR8r_pF6kZj4lAOO6e5jF_IbuH9Cxdc2naDn2SE_QLS5dmGFcYUSVfsqD1n295WkpF5drLUxTr8_y27Nvkqru-UG4Bsts_NxXHHD_mhZdLdVaah1OlbzGyUC23XDMIqkDw5YnSfWXdzBliNYpZa-tWfm4m92oWOmfFCzneaXkofwlT_duybyEr8iRXzUIt-oMopbTwCUirK-mbmDGWkYrqfw1KoOpAEUXWpVJ7q-29bpebkuWLm53NwtM7W1Whp12w9jdVG44yTxH9mNPvV7i6sw9pIuimgtlQDT87XP8_IcK9JtJDqtW__b6oA5JvELs3DtrELmkOK40EfHNECQfXll_FpkwIo4grgh5iUGnGoMwvRqN_AeZbl-AU0l6ma58SqYKqK90seYrVim_LQ403ltLGuNUC6-vDtcJAuzK58tz5q-Dwde_iBo23V4fZ5XdDmMxhaXGUEhNHGW7w2CmZcn6Pew-kUMoG05qLMmd9nMDFcOruovAi1deQeeg6zAPrlKUADwEIDhZdtyfV9JnofHjwT8Ujn-3tidV4B7GEEXL1xRuRdVG1ZfbZbVteyo2gbDla733o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=YLGiEFzdYK94bsugPV0JqmrbN7TNQ_WsDwJUc7MXWCmnbV8_nyFH9lI8nQynHnZu4BeNCRzaWDuRpncHMghVrELnpdq1TlmcxkrnlXtVCSCzw1u4h0Q9sv3IYAsgNY1MRvZBstDE1onqBdHIqfvseKpMeAyfi_EpWgJ_ctAkL-2j6VXBfcqcDI0aVyOGqeQ4UwOQBqwcCNTntXcbLoQLRR8B9kBkGODy7cBr5LXlu2oszXybpEnJEfIsMlIUHezDjd4XiKaEpev9m4Otyy7AuZfgvF71f4AYiIPJznl8c9elIZ4ONdx6VVwwRt4iihG5hCXl5vu1925nb2poEb4rJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=YLGiEFzdYK94bsugPV0JqmrbN7TNQ_WsDwJUc7MXWCmnbV8_nyFH9lI8nQynHnZu4BeNCRzaWDuRpncHMghVrELnpdq1TlmcxkrnlXtVCSCzw1u4h0Q9sv3IYAsgNY1MRvZBstDE1onqBdHIqfvseKpMeAyfi_EpWgJ_ctAkL-2j6VXBfcqcDI0aVyOGqeQ4UwOQBqwcCNTntXcbLoQLRR8B9kBkGODy7cBr5LXlu2oszXybpEnJEfIsMlIUHezDjd4XiKaEpev9m4Otyy7AuZfgvF71f4AYiIPJznl8c9elIZ4ONdx6VVwwRt4iihG5hCXl5vu1925nb2poEb4rJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSQuDiWU6h-Wh_vFKYAzMCmHWRzE8P8o7QNQ8sKso7RSe6XX_hsJQ9nkCOWTEmDexFq-TXhKdeOq24jiT0ldtjRkeusEi2dj6KHYfOeJekwgunNlCet4qFZySufEMU7VP8m5nc93xnsbwTmekHD-u5bEKrcXd5qqhr6QNJsxcqU9RJZ64vihjwHAO4W2ZnZeIkDn6OvesYqYHyTvlYQzlgZvOvbLsVDSC7dC0wv4zD9eM9UEv1HQzKa1fdKXevkqzoYBdDT4KV-ShavpjOMxugasotwOmRT2MqmiPe_FCYTQ8_UrZ4p6i9bW-JnyM5RdXC87Fgv547T08--IcNv24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=JIHubyZg3TIw1qUio5moqHH6XEmLm_LquQspvYYs3EvLMUR4cgETJkVVMJcroiHR_x8L_-qRI5FYGUqGhUSjnCR7GrQKKqtGBP5sVYP-T2oF2ED2RsJpr1MgxISvxiuON4CVB4Jl0XxsX3nZrUNKXo7HGBqis0FPfz54V0CGMMjB0iFf_Xcmv9_qN1oiIE1YtbUqCef2RYs4CIqDIZnBfmLunwvbmxkjmfdgBZqbKt2BTNFNcLIjjsY5LjzOfhomH9IUvMXAG8gwmUBrIdXt8LsHAGIFVKg7YfQB2dM75kUFFGZlScGlnyYNi0VU9YeLnamCoBlhHxKKWz5CW8wFQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=JIHubyZg3TIw1qUio5moqHH6XEmLm_LquQspvYYs3EvLMUR4cgETJkVVMJcroiHR_x8L_-qRI5FYGUqGhUSjnCR7GrQKKqtGBP5sVYP-T2oF2ED2RsJpr1MgxISvxiuON4CVB4Jl0XxsX3nZrUNKXo7HGBqis0FPfz54V0CGMMjB0iFf_Xcmv9_qN1oiIE1YtbUqCef2RYs4CIqDIZnBfmLunwvbmxkjmfdgBZqbKt2BTNFNcLIjjsY5LjzOfhomH9IUvMXAG8gwmUBrIdXt8LsHAGIFVKg7YfQB2dM75kUFFGZlScGlnyYNi0VU9YeLnamCoBlhHxKKWz5CW8wFQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=lCtvu_iOwNpg6lIp7OXfj2yvIz8oQaTdKCigi5KPF1wON5doniEvNjXtmBa6gdWET98v8dvIpl_QXRNnIeHdoqhXJTpJKX24oqSg-QbKhmJ4BGnlu1fk8kIYTFJgfn1a-6vMBs24SYAIk2xPf0poSDNeGnkEJJvmoDOqfI6RElO03cJHjEJeDI9abm8l6D45k3MhCh6ESMyDwthA6k6AO3Z5k_CvdAjTA-tt0gfDiX3Ulhay999xrvk0X1k_Hd4ybjMd423Ou0N9ocknImaY3wLZyPNEg8Fk45X2XIgbA3dMKvFck8jMdtoAr2AM9TfT0q2eJvUcfPt-wvLJJ8DvSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=lCtvu_iOwNpg6lIp7OXfj2yvIz8oQaTdKCigi5KPF1wON5doniEvNjXtmBa6gdWET98v8dvIpl_QXRNnIeHdoqhXJTpJKX24oqSg-QbKhmJ4BGnlu1fk8kIYTFJgfn1a-6vMBs24SYAIk2xPf0poSDNeGnkEJJvmoDOqfI6RElO03cJHjEJeDI9abm8l6D45k3MhCh6ESMyDwthA6k6AO3Z5k_CvdAjTA-tt0gfDiX3Ulhay999xrvk0X1k_Hd4ybjMd423Ou0N9ocknImaY3wLZyPNEg8Fk45X2XIgbA3dMKvFck8jMdtoAr2AM9TfT0q2eJvUcfPt-wvLJJ8DvSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkQIADh2q-va2Nj7ZUgysImimESwbIz4SmqjAN5sjpy9IGDOGiFuADLifdEPvWBFbFIY7O4PKOL4HQdAgFv4aq14clWpzcXOewhnd5AKuMyzqEFOzUWNVTsFQHPwmGaowaljxYPTEi3IdpXGmsgissAWoQhxl_TYW420jdQM1QXMNpw03n6HD_HGZUU4kEWv0iffFleVinaVfCddNXHHjl2Vc49TSuz6xn5ZlxpxSl-R3gRrX_dCiKX8PMXSzNk0PYuIyH1ABvZa5GD6nCICCEqCZsKxBkcgg1vPCOwpq5jwetYvVHtawHXvqGqYXP3WXSotgzer0byJQRQVQKqLRQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=Ibt3RuO2bnSQFhUgAv2hax0Ba04tOfwx8zm_CZIGajxEEzNK6u8bmli1oyJSlfSpDfqM-CY3UmvMeYZ3rnJ8NwwbS42FB6C6u7aNiDdqwpSrlUGbDzJAadMTC0G1JrCicmQSI6aE1hMpPhcNuHhbk0LmzMsa7EZw7vdt_kZPXq8JwQthCz8s8v__rMx6wC_VVNQpuMSrHWwwiQ5ETVlJuDwjNU9cB-8M5_zfaqpizEQ35bm-2BZ21NsfLZVPTsaHmFQ5i7vNVGVAEruBQPy7DJLvA2Y8Gjfloao7J-1yby9HMiZLGFx1jW0yyHEfqtCbUC1ugqnAQH4v0KjRmgMSuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=Ibt3RuO2bnSQFhUgAv2hax0Ba04tOfwx8zm_CZIGajxEEzNK6u8bmli1oyJSlfSpDfqM-CY3UmvMeYZ3rnJ8NwwbS42FB6C6u7aNiDdqwpSrlUGbDzJAadMTC0G1JrCicmQSI6aE1hMpPhcNuHhbk0LmzMsa7EZw7vdt_kZPXq8JwQthCz8s8v__rMx6wC_VVNQpuMSrHWwwiQ5ETVlJuDwjNU9cB-8M5_zfaqpizEQ35bm-2BZ21NsfLZVPTsaHmFQ5i7vNVGVAEruBQPy7DJLvA2Y8Gjfloao7J-1yby9HMiZLGFx1jW0yyHEfqtCbUC1ugqnAQH4v0KjRmgMSuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So7871xaQVnKFc4bZ_EOj_ukADlmZEYlS5LCXEAAAEsgPV6nF9verXZPYzbVy_DEoxQaBb4c2vj4EHwoOMRXMwGI6s1fdLGXAxTX-0l6vvhVRWPzKQN_n0ViBYUG0igfCnl5TJy0gm48watikd2Xc3283lVLnh1-3LdRLiLB-AZIBEk2-JvApOxybr0m_mMmyoI_FnApPf1IaIKy-JDG_XSTTreYamDacS_6ysGQjstPkRSy5kdQsxR9FFITUxqp3z6Wv21sYPf5QneeCJeDJ3GVqCkGj_xWRhdFsrFEh4VXVePsT_2ww8lqR1aAAcvWdDr_1wdFtLHchlkPfL4nWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=mvFuLE-_AI5RlRSsq-Uut2dejzSk4yLUKQto1m4PnqoN64PrEeMmjskjSg5o5eKB9KfwptUlDqaHo84Dt06pL-PkCLGmDZ4V_5fvg-8CkrSaF16isYs0qWUTBu-tFttH6nOIrAhw8Az3Hrc9pA6PF6GqyrGvbARa8TdOhIwGnhUPlLQHY00vHdvkyXVsTaiKSP_fYpbWhW0muMOGufYERuXSun1oMxW1ARJHrSNkEt9Wxt5GhbICet2AKKoo6FLyOKJXYY4PzvTC3xlt6JFurvXzF8ioPTCi-BqwWJwMUxfUx30vgcD2fb-1Yr1Z4Q88bPMNxk7gmKqWUTF-7SBVJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=mvFuLE-_AI5RlRSsq-Uut2dejzSk4yLUKQto1m4PnqoN64PrEeMmjskjSg5o5eKB9KfwptUlDqaHo84Dt06pL-PkCLGmDZ4V_5fvg-8CkrSaF16isYs0qWUTBu-tFttH6nOIrAhw8Az3Hrc9pA6PF6GqyrGvbARa8TdOhIwGnhUPlLQHY00vHdvkyXVsTaiKSP_fYpbWhW0muMOGufYERuXSun1oMxW1ARJHrSNkEt9Wxt5GhbICet2AKKoo6FLyOKJXYY4PzvTC3xlt6JFurvXzF8ioPTCi-BqwWJwMUxfUx30vgcD2fb-1Yr1Z4Q88bPMNxk7gmKqWUTF-7SBVJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqtcBKtjRO-gl5setnhDwfLXzTARyXJ1Le0WRl_k8mcnxZyP2EWn6ZYu6zWqXsDSJlIK4dFR-ykLUhZh5fll1Ewh29Gb65rAVIglzmCtdTvwTplnF0sHk6802OSO0xLRGvR2vvDB45I3MKwksv9i99PrJs-mb658QYY0fAjDNlJrjoZp2tugMuCFHm_rkpm70FzhMj3tm8IrwA0DCNoqPg0yOCN_AEkcsANaiIAxXPRAYfCYj2dj_rOqeG8V86G13gqxncnfVFfpotdl7ZpFTNT9rABpJ2xbUl6ZVkswmMi7jB5J4W-OW69Td1_GmnjhjIOM7Fb5YUPd9JZ-RhNS8Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=HITIBCOKu4ZohjHdugzq-_8xD8W5EFG_pQlcDKs23xp6VZQAXI96SF6G_MqiqMRrxB7fgKtABOQJKS2jVDYN-2YuVSwXrH2X20aTYop21VRkOKsBpcLTrilMJr4MiKLgrVq1Ej6m3k4cvx0hGcx8JmT-x9J4RzT61SsCdSAuPBjbGNCzFloABNx68tcJNjSV4j5Zgl1O_M6WpFnxgDY9EtTTO1HMXXyKY_fff8rfQOd5KZqEg450SxkQjyVOCaXULvyXArQuwW9esf93tSp7hk2CJzanyXdcqiJgIWCrUcCY4Cz-iFRzhaiKS608CM2utT9sbSsnvG-A8OKTuDjnxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=HITIBCOKu4ZohjHdugzq-_8xD8W5EFG_pQlcDKs23xp6VZQAXI96SF6G_MqiqMRrxB7fgKtABOQJKS2jVDYN-2YuVSwXrH2X20aTYop21VRkOKsBpcLTrilMJr4MiKLgrVq1Ej6m3k4cvx0hGcx8JmT-x9J4RzT61SsCdSAuPBjbGNCzFloABNx68tcJNjSV4j5Zgl1O_M6WpFnxgDY9EtTTO1HMXXyKY_fff8rfQOd5KZqEg450SxkQjyVOCaXULvyXArQuwW9esf93tSp7hk2CJzanyXdcqiJgIWCrUcCY4Cz-iFRzhaiKS608CM2utT9sbSsnvG-A8OKTuDjnxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJ5_PQU2ToI1M8nu4geZw-GteByEcppTWwdyGol-mOVfY5vBruvv6OQvvwAbZBrF-roe1vwAO8B5F_9em_isMFijxJ47hw4EGVJQRm6ch0KXLCAKCm1dohjnQunGMaNRTFXyZvkLsO1AmuVyJp7rRC36vdhPIx0NDvXq7JUATsOV7nHNkYfH52Hj7vc-py17vZjZFzNnjAIVGANIV7QKFXXw7K91QndO1tNph8pP5aMuTvAD0cDqK_0qBxambWPGsT-WovS8VnQre27TmPekWaU7q1tfR9VDti_w-bWX9r3tXNU8RepeKCo88iGNLRzbPtlL3ckL8wRZKmqz33_rh8rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJ5_PQU2ToI1M8nu4geZw-GteByEcppTWwdyGol-mOVfY5vBruvv6OQvvwAbZBrF-roe1vwAO8B5F_9em_isMFijxJ47hw4EGVJQRm6ch0KXLCAKCm1dohjnQunGMaNRTFXyZvkLsO1AmuVyJp7rRC36vdhPIx0NDvXq7JUATsOV7nHNkYfH52Hj7vc-py17vZjZFzNnjAIVGANIV7QKFXXw7K91QndO1tNph8pP5aMuTvAD0cDqK_0qBxambWPGsT-WovS8VnQre27TmPekWaU7q1tfR9VDti_w-bWX9r3tXNU8RepeKCo88iGNLRzbPtlL3ckL8wRZKmqz33_rh8rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu_Bc_JNOBMXgOqzffs0E0fPXbFRlivBSm__yx1z8VmHwF-Eoan4cnOMAnP9LlaK0WXMb1XrNI1YkeC4z1mkfe0KmBSg0-eB7JcGbuAm8-MhzuAx55AgFz2n-m24fk1_PnusIsn-YQ2pnMCWmh4iyE_QV88mQegZDh_nUWAjn8mbnFIoLj3qrRfhpOKLkYD5zFAsE8gWqe8zf2KJ9gFzud_BFQEEPyFw6vSkXYsF43vDdjUrLWrYhQFDtRieL6Kh3mx-7ASgJOk4dkZylXzMtYYDNIPbYI5g0q_TMuTajt1m4IRk9lwYdRQLn-svEofs84GlxxutYiufO2OOAde6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=KaD_T0sx2sJ1DEfF_s4Ea--pGoR2_p3x-SLjHzItdxgE_29yBrpdfn8qgddI-xfFY_23nHp9v-icfQNt88_yu2X_Azv9eTFPCKVUFsVtW-lkrQavhIgDpzF1ehPBY4SP9qjitpZcqfyA0xx1OI3CMzmv-hrXzRjG2eKVDrK78em0-c0LcGSwKLg6PHkXucHO-B9ehy94nxhZlTEUL_EGKL0fzcb5cgCFZNw8nTb7i7BzGM0N4FpYR5JUxOcvR5h5m-UE8fHvSugULwRk3hitB4Bvs15Q9SRhZQ1uE9Dbh1IdjHGD6GvxphFYQLYK1fC53VpoTCIJu-X0CcfZrDgkJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=KaD_T0sx2sJ1DEfF_s4Ea--pGoR2_p3x-SLjHzItdxgE_29yBrpdfn8qgddI-xfFY_23nHp9v-icfQNt88_yu2X_Azv9eTFPCKVUFsVtW-lkrQavhIgDpzF1ehPBY4SP9qjitpZcqfyA0xx1OI3CMzmv-hrXzRjG2eKVDrK78em0-c0LcGSwKLg6PHkXucHO-B9ehy94nxhZlTEUL_EGKL0fzcb5cgCFZNw8nTb7i7BzGM0N4FpYR5JUxOcvR5h5m-UE8fHvSugULwRk3hitB4Bvs15Q9SRhZQ1uE9Dbh1IdjHGD6GvxphFYQLYK1fC53VpoTCIJu-X0CcfZrDgkJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=ePOPILraZSg21P0DdF3uwSh9UrC591na7QcKBKyYBOabdIa-bk3DWvIaT7flqR0JVfuE6TKkA-sqJmtTP0ScbuymDCFhrvuxapj5lQeUW8LgOWNElj7URxiGjk84yv5IVwHW2uig1g5WsqZPzoc8z8DxjwO30adsJR43xxb9piFbA6gWBAyeD0Zx48MyoFnaHfIKqfeWEdYhYSHulBBknCXKhYz7HCKKpWroayeQlmuJS1Qbfc8mYXTKAx70rqgidyd5XQMWJdLlvjnc1DmrlzfeD1BToB2G8exoKFyAoOblGd6L1Ick8gaSjabH1oTG-gWjuknvXh0X6aUqpmnBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=ePOPILraZSg21P0DdF3uwSh9UrC591na7QcKBKyYBOabdIa-bk3DWvIaT7flqR0JVfuE6TKkA-sqJmtTP0ScbuymDCFhrvuxapj5lQeUW8LgOWNElj7URxiGjk84yv5IVwHW2uig1g5WsqZPzoc8z8DxjwO30adsJR43xxb9piFbA6gWBAyeD0Zx48MyoFnaHfIKqfeWEdYhYSHulBBknCXKhYz7HCKKpWroayeQlmuJS1Qbfc8mYXTKAx70rqgidyd5XQMWJdLlvjnc1DmrlzfeD1BToB2G8exoKFyAoOblGd6L1Ick8gaSjabH1oTG-gWjuknvXh0X6aUqpmnBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLmtOVYrOzIx_2MIEujPdGQnFaemnrmhCrssGI31RQwG9dw3517eT6f2gDUYNTfC36mW6_H6XQ5eCke1-gIBpyhwRurZNb5hKAJyk8lQO-dr-MsxizOE8VFYhZ4YlM-C5XobCN30nvvR64VFS2AvB8ne8KsKjt-sW9MLsEEgDzh5PJikVFIxk1wQ2bFadVrj3PmUkl2MYIrgRS99dgKw2uafhuXwc7SCtplZuLih2MGB7r_TMlMb2IZ434aIwtZDXGqlQTh9s0VA3M4yt605nPsaMrTIqWXjborCPFSEWYwy9q2Q6T44aQ2uHLZtJJyuHPIz-awSPVIkK1j_MDoQ2g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=sC0Z_51xLwsahjFjJcUCT7vpFrg18ZfWV4ob9twqVELxfkb3q3FR9erjyPoG6Rwsx83c4OhJEvaO6pkpFwFzTtM5Cl1nHLMU92tltGpzgVXFB7-hB0wtEELI3UL9kyyJ7lYEAnvtQjdLpD8R_XmFvzBhfGulySx7bSI4qkMMX1fyMzOh-apaEEr7a5RD7fSalcUc20ThLAAhvSJ6QoGpJfq3p4lxaLSTThc3ECu7jWGo8Vt97jKz0oRUZzCeGBMN0gi250tob5g-yJOTXvlQGJWaL7hLrtZjxmTvhip3ZpyV7yqJWwJtCiAqfiFYWBgfuZIXGraBXkgzwXmCUL56LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=sC0Z_51xLwsahjFjJcUCT7vpFrg18ZfWV4ob9twqVELxfkb3q3FR9erjyPoG6Rwsx83c4OhJEvaO6pkpFwFzTtM5Cl1nHLMU92tltGpzgVXFB7-hB0wtEELI3UL9kyyJ7lYEAnvtQjdLpD8R_XmFvzBhfGulySx7bSI4qkMMX1fyMzOh-apaEEr7a5RD7fSalcUc20ThLAAhvSJ6QoGpJfq3p4lxaLSTThc3ECu7jWGo8Vt97jKz0oRUZzCeGBMN0gi250tob5g-yJOTXvlQGJWaL7hLrtZjxmTvhip3ZpyV7yqJWwJtCiAqfiFYWBgfuZIXGraBXkgzwXmCUL56LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=LDPLxsNX5D6ZJt9-KfhKsMhUE9wbidRo8oS0zq8RiOJQd96rDHVAqncHkB3PQ5nNErgfhIpH31pOujrTVgA-OjpLd5dgyhVDdY68_DKjllfHm77xng4Cj43xdfg3QO4aHB9nW1rg3CqWHU14VfJ2OAXoD9VSmmaR8RaLf4X-_LXkcTwoF-NleF570wAXvRMNyUVDEB4_jm3Lyr-n8SEUjsm8l95vtQpl-6haWD0ZvF8Kx8sh5ZBo99cfKJNCCb2C0tSmMd1caItlj9rv5ZJJ8hfeXUjkTrYfrKxYX8dBoLOfA0uRk7gSj0GmlAGY7UuNVAwpubpEesD3WaqOMgqZrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=LDPLxsNX5D6ZJt9-KfhKsMhUE9wbidRo8oS0zq8RiOJQd96rDHVAqncHkB3PQ5nNErgfhIpH31pOujrTVgA-OjpLd5dgyhVDdY68_DKjllfHm77xng4Cj43xdfg3QO4aHB9nW1rg3CqWHU14VfJ2OAXoD9VSmmaR8RaLf4X-_LXkcTwoF-NleF570wAXvRMNyUVDEB4_jm3Lyr-n8SEUjsm8l95vtQpl-6haWD0ZvF8Kx8sh5ZBo99cfKJNCCb2C0tSmMd1caItlj9rv5ZJJ8hfeXUjkTrYfrKxYX8dBoLOfA0uRk7gSj0GmlAGY7UuNVAwpubpEesD3WaqOMgqZrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=JE17t0FTYSUvQf9o8sH4FYLk-8yewXrHxYI_71xhKRgWCEwOavER23VzfiU4WlPiRAcPgKN3wBvVhFXRd13vBtVgqIoJOep3hRjbhY3XAyMYSdRMH1qCF4it4YPSA2VVyfnqYysyVjf3DVQs9rgn57dJOMtL02T4Dm6KqMFOI3EkJuHRRbw2_vWq3zr3gslbsRvLqeoCg3Xr4ZN2FK0F6SUPhgfSitbnzIgBRqFPEzlZFOzwBjkoKvadlh_m03fMq-MFJoVEH4I9O6p-G8LKsjKGvOK8SYmuZDTyHb5wkntvx_twpAEJ-zfy0PObs_BtaY5DRsQqTyaBkoLeGOGCUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=JE17t0FTYSUvQf9o8sH4FYLk-8yewXrHxYI_71xhKRgWCEwOavER23VzfiU4WlPiRAcPgKN3wBvVhFXRd13vBtVgqIoJOep3hRjbhY3XAyMYSdRMH1qCF4it4YPSA2VVyfnqYysyVjf3DVQs9rgn57dJOMtL02T4Dm6KqMFOI3EkJuHRRbw2_vWq3zr3gslbsRvLqeoCg3Xr4ZN2FK0F6SUPhgfSitbnzIgBRqFPEzlZFOzwBjkoKvadlh_m03fMq-MFJoVEH4I9O6p-G8LKsjKGvOK8SYmuZDTyHb5wkntvx_twpAEJ-zfy0PObs_BtaY5DRsQqTyaBkoLeGOGCUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=GFEPaXYlSx6PsDCfxGOQK3iuiQaZVZ6uOknbn9nR_qowvzIUcBaO3HgpdI3FowadU1Q6Wp4gc4XGCnC9G4KfHIXUgK67AT_9L7YPt64kJVBCKQzeA7gikneS7LVPI7xnv6WmbhRCYiWrkrf4pGWXIS6YD-ywDOijuImwB-TZfOHpNXkuPVj6pJfIbHuXGIZuNLhFp6HoJT_z2abf95pXIapJHDfdlOl7jQE-LhrU7zhHHWLYicO8dO9q1vi3hIOA_ZqvY3JfIY-xSMx96fuYYv_bA_RWwX-Qfhh0Rpllj6bNGj2aIn7hEadOtTU5-mU8Zk8aJeFZ32eAdUokzsvXBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=GFEPaXYlSx6PsDCfxGOQK3iuiQaZVZ6uOknbn9nR_qowvzIUcBaO3HgpdI3FowadU1Q6Wp4gc4XGCnC9G4KfHIXUgK67AT_9L7YPt64kJVBCKQzeA7gikneS7LVPI7xnv6WmbhRCYiWrkrf4pGWXIS6YD-ywDOijuImwB-TZfOHpNXkuPVj6pJfIbHuXGIZuNLhFp6HoJT_z2abf95pXIapJHDfdlOl7jQE-LhrU7zhHHWLYicO8dO9q1vi3hIOA_ZqvY3JfIY-xSMx96fuYYv_bA_RWwX-Qfhh0Rpllj6bNGj2aIn7hEadOtTU5-mU8Zk8aJeFZ32eAdUokzsvXBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=dW5SqoOWU-eE1w1hb_XyHVyffp7bERWVjo-95yMR5k0Wq-cJyl3n7OYfs2hs-7ZNANzLk70YPdZOtftdQSOWyhyIj1XsPBMwKF7I3uDMojViOyX3AUJx2uuLHB8656B1kXzu4T2XmzmLpRQ1VXGjRw-qfWORXpB9OkS3YBbZM04rzB4EG079nYIMEV7O-i8Dh4ZYjz-eo4ncTL-liaAF-0_CC99RotBnDnyM_KXYNEj8tEC9FxmK_tkHFWRE6pZf01_hiyY72xONs9fwK6YYpXzQtSf0M_F9i-XKmOdzFH484wgi_g8mqHn-_BKRIwMp92G1DGDomKYXxdHnfjXnhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=dW5SqoOWU-eE1w1hb_XyHVyffp7bERWVjo-95yMR5k0Wq-cJyl3n7OYfs2hs-7ZNANzLk70YPdZOtftdQSOWyhyIj1XsPBMwKF7I3uDMojViOyX3AUJx2uuLHB8656B1kXzu4T2XmzmLpRQ1VXGjRw-qfWORXpB9OkS3YBbZM04rzB4EG079nYIMEV7O-i8Dh4ZYjz-eo4ncTL-liaAF-0_CC99RotBnDnyM_KXYNEj8tEC9FxmK_tkHFWRE6pZf01_hiyY72xONs9fwK6YYpXzQtSf0M_F9i-XKmOdzFH484wgi_g8mqHn-_BKRIwMp92G1DGDomKYXxdHnfjXnhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFdcpavCv5n6IZQusdVhQy-2gF8n0c6VELL1H5XzVEi6NPIMAY2UEhmqC3W3KCYRSWU4Cd5js64x7ZJzTZ8Wq9i6Ra6_Orl97bCnrkL0PYi9OuR0cVXS7gBB_EbCuURrjCdJpAaQ2D6QYaUNW2d9nZWa6KIj3k0BRm5exN8QJ6NNQtRajjdypZIbmCtzrnSsXQLdJPJKhi5v5lgJkYb8esuLpX0J5r4INyOjhSwv4D4G-QPjJIayPHSuFwy3pHy4HZiW0qBUJelKvnWMhDQ_reC5aYVYEgHnIdx-3PQ5wDCX8ejq3uwUKKFAoDltKvhSDPFWr2r4KXsUUkjfFVkL4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJFfgyP8B5PB6vVuPctfpgBXzdU6-d3pb1PYVF0Lx8uwRQEbZc7lmE_nJecb3MYfRIMUxPLZubrBWIh5w5IFEZHNDLb32h8P0a3aqeQF3VoY79NJT3VuWdtYRCbxkGRkK1H25YufEDqGABLz4y8lyjEN3E8RYHtXXoXCZFOrTXB5fixObsnflVMSZYZR04IpBAAETneGIQobMSJTZ7qBbfzw54KR1ZzPCcO0QAMcOcpGzkjmPiG51emi1CyaVMwfqCYf5Hp8cdAFpCddz9hFM_JWxc-GXG0FyUchZGfzxF8A6Yif3BvYeazTL1mMK0Y1uIAQP08yw3V_7XhOVad9zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6rG-l7_FsLf4I4rIQuft1VVF-dUKwhOet4PPXj83vJ3xvZEXHZEXjqD0ybx1oSZU5jj_LpYHYS4dq_BfHPabqI-PS--Uw5y66L3cVR1amhvBl2k8TkCj4jWTxn8OZaG3Tnt7hyaEx7CXLasMd_adEf7qp9h3NujynA2IbElsWAk9l88oAamXVuIBZif0IThMFvBbDZ7ccGKNELk0lK0LKSp8rkt7Ers0pR1NnX7WYI12BOweP2ZPLx-F-PYKVYA8aU6LmKkXF_bhpbnFTOUdlHJH_p6wdGFYqHq525Wh-b23R33nMIsmht8-xGwhhCP4s_wA2Aqb-xKvtjAXn-WTQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=gN0lNIJeMWkKeIZOrajy33qWvQ5cMMVQhGmtt5FZdPPAvM9g5gDLiQifxr9biznVFcQBUTfe34d4zlBkEcj85uVx6Qg5GyyVAWclNmPbKopaj9P8d_A8cwmWuAlbLo4RyaD9hPhVlpGzBmIUtzv5wLJaXLz2MPbUK6bnYxi41iN9MvKeqgHXujsa8-To38sFtxBxl1oWw7dqRxMiRV8alE67ovyprkdQFRJHK9PzokZIfBTk4uk1PEZT1AWLWuSU0RQhn40-ig2WG7RpY5N10U-GM6qEzk05QDXt49q667F_LFO-Nks2XQZqtFAgswPhxeT0s1uOmcui0rMvWPVSPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=gN0lNIJeMWkKeIZOrajy33qWvQ5cMMVQhGmtt5FZdPPAvM9g5gDLiQifxr9biznVFcQBUTfe34d4zlBkEcj85uVx6Qg5GyyVAWclNmPbKopaj9P8d_A8cwmWuAlbLo4RyaD9hPhVlpGzBmIUtzv5wLJaXLz2MPbUK6bnYxi41iN9MvKeqgHXujsa8-To38sFtxBxl1oWw7dqRxMiRV8alE67ovyprkdQFRJHK9PzokZIfBTk4uk1PEZT1AWLWuSU0RQhn40-ig2WG7RpY5N10U-GM6qEzk05QDXt49q667F_LFO-Nks2XQZqtFAgswPhxeT0s1uOmcui0rMvWPVSPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOXR6naI8JQXxN13R3UCRjnWjjTJqrYANLSeub1aQ1BUp6KIeaFjEDzxOubBBcw33yrcD71kSFcpbDvFjEQ3vXmD3fLiP2oVTHvRDF5UoIzi86xxpi8hHFd3poA71eNuoHjQSswmKWljueNIZ_VH6lEM5R1DKQ4f-BMhX_ycJe2J9AcXwNzrxcZQOWJ9u0TfoPS4CBwFzf1Y_4bTqA0dSh_skeXI5OYwA3GQHljWKxtovealBR0WUe0k5gwRlXNDm2Dfmsm7DKhnmnTuwKnzeMBw1ShJ3VZHdsogd-rwuauzb64u4tL9fXsVTNEBhxUa2d-z-7P06jAaOZThnZw4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
