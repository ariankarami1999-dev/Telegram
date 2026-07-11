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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 16:28:18</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHyP78d_fSmY-vAEqFik2l7ZlkGJy21Sx5I5dXjWixnIxpRpKMQdGkAI1Oq1KSAenwWGwTeB-J37Ym_eptTW1CdqlhbHYgkJxls9JRsQ6XtTkUONkJqS4JY2SPk50aB4rZOLXPUJiFVeAy3u1w6TP0mONF6NlH32w-dKUTKJRoz7VaBhNN7Z95b8cIM9PlEwtvH-zGzX4l1FtoDauqlw_SNW_Xu1nKSHmCoNkqm82SUg5FXs1X_dz-73zty4MuzmLJ-735vEf_LQIWyQ50EBzG63ad77roh1KcQEy0tAt6VCjwrdaVW1OKXmh-XXe-AltoS88ELnyqYCKtTLo7lkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFoTgLRG-08-wXkVfnmUjpyU85d5MEOPeSE2RXukUJ7gcjmFTYlZCb_kpnQL7ZIcAAM_lDv_J4qZLl0hoiuQRaoKA_6j-aoodXfesfc3KLW2-ibWZjxvxqxsCsKOE-w13vSFR6YCpn74DYo1NOBBYyEvAsrIYpZHslnt5ahw7Y8rBD5zD72zEjJb8Xbr82oFCT3fbG_O9-gKukh3C2YomWyaoxAn9HMpLntkpivRZrpZ4r0DzEYp8eqAocUxAJO47HRnA1D8xjLyMZVi-YwcsKo3Qk76hvz83eeZEW9VoL3t6eBs0cX36qSbGuiRA1OhvmzravFHMOyi9dx-QJrwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6fj-XikOE_vV6gn_Bc8O6-xIM4wgXc4YypxLCBQshzeZI2ex4bJps45gE5IffGwgyOcFmOIBXpQ5LzCUMaN_tBTveENWfWCKP8xENhazzUOnaFAp2M-41EK7Ymex4ZhS70FmJAmyGgh9BYHdlF6czYGHLcTQPXfB5Pl3iD77I8DjDXJa0sUIEh6zuEi1VR39aXBilQoalJgeV9tVniQdu1Klpw0ZHKxsgfSfFTz0JXsGf25mcyADsfQjrHKuvlh0iIPGCR6LoO9Jd48T7nKZvec_4o_-CsQq9qSzSvN6_jHrdi6Ysi5U9_kDIWzg08jSHPScvB1Yh7KR2t3-wfS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbIJyOE2Zg99a7z3TD5mDWj0vjc1vH4vH6eeDCZB033bHtcto7zbvY8OM41MekdSJL9DlcS9mLECr4XoRiKdft09qQFx0vnI8Uf4DSB9UJ5SLtKNYr4kzEbFsDroDdylLGJ1uLB_MRRgKpUuLhaWn329PoFDM2Mf7VIe_Vfs2tbR3FlpSShbyJ6hYHVPN45B959Ufyq7LeVRhGgU4i9RBjDSuvUrTRx3kAfK39tQMR-B3y8NO69Z17tPQoOft3RC91injyqPAcnU69MuP_c5i290F9K3QcyL0s-jszxBquiXLylYWfTy2J4tucAQBOGLSqhVQS5QAUus7_jHfnFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBCdTL9seDcNwGsIb89YYMmUWZ75YhupG5WpItG-REVUvZfiD6KHiROnXkLn4fzdNEvQCBsplLIerYuH0UMUBEtMsezM3MC7ZKK7Py0YFkm2H0O6mZei_Fnzbygt7tAnrp_QgM6h59w8uxsGJIyNVQN0aLBYMYZwuWWVtE_nnIqjCdwrYgb8nyJ4K2r6_6FmvF1cFmuGuqTGjxgGNBAjAkenwQxu9CHL-SNdywTVANS_otcnr7RB-hd3qv4e8yGeMKp9oah80UsGtFRxbWjhdqYY3e5LcKoObVpckCAzAsFgLiWr1fFP9YOF9Blgz6KLpZDuv4UTBUShsOAstb-pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_jklWp-P3SyRXbm4_EDnMya7QubfMI49g1j4w_VhiPn-iZO2Evl0qL-0_yfAfFGW06qtFJ0UHnNf8VNKezps_esDctb0ISCH2P6bquT2fhd2L-LWktS049d0km2_qfc_tzlCR9l4PnCDawud2NIK3WyD1SKzbAZDNNSsI9Ag2I4XDPwulWsAhcmD5ckwtPta7cd4Q_2LgsjjzJuSBgaE4NfL6ji8a_T2wKx0RQoUsLXHxU_QD0i-XsiaHSvD88FEIKUiIeua4WC6dHLfzg3ljE_VPOoMVDG_dxu9S4sK-nc3_VHIwtLtU2D0qQOoBR2AhqMam6Ajzxy-v-rz5Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLFj6blG066qOc9Vz59KMvvnEt9kXhpJ-qtpAmFfW5ICohqG4FNQbWoELS85GqFKPesMMQ0oIfeZTJVY-UBuixdjzb57WF9FRUwO7fSY_zE_YSTtvWkrwiIUm2vO2p_7aXcYiUh9MxrcFc9j22DyifsmU4IGvvMZCwovXGmVQUWCILGwMwwid2CfDJ8gyH-a898QpObWojN6z8_9nSXZslXvmd3cLOi3Mv1Tyvs1VE5qQFTsUJnUtIgorLz8krnFxK_6LS-3AeLXwgACCRvbgX0dymYpAbeS0kksqNXta6BKMCcSOREawZwACz_9ToLVmNrpjPs21FyGGKWgGaYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW3Y8wkErEwjwhOu146AJeeXna-1_Q0yQHyVoQUogvuEw84IQQWdhgrcwU80wv9tXG-1-1jTExHEOTwqgh0A15l5iYi9CWoppsIWSS_H_9MqlPO-ExhLP2LqfKuW7q3xDK4o2mdX_UoqYv7uPLz_u6ilcSEtzGMwSEIrDajTgLwW-XHDpJZvpULYX9Nmzv8qJtpy9PZuvcubBZXBTiJ92E6mS6ggwrjB_PG7OV5UKWrXZQCzHSFlIUOOE6JmN3GhWMWGj7vpEg5yt4XNt_lIBZmLVrNJDyAXQONcTbZ5wKvksbzWFVuWgRJTiWIsxnT8K7PmpZw3v0Ako2lvBbMjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftoT0vHGzBnDY_XOgrbM999A50vu0U3HCEN_VD19MRDlKDrZhadB94T8TrzcNVRt85obQoUoJlZuJK3fO9oEmw4y29FrXCXwTbD_uGmPLdIeQCkoycDhgOUajra1PbFAt9VMcv8n_IHQ3SHNWnGxGXjVLHBUO55RjZzf5ftn_evCkOxFDKjzuTt0TUvZjEPYx3OWH9NLgMRb4TmkwxQfeP7eyvtHE6V5ul4OKgv-3bLHn9tJpWBBpZHnTHEQ2wJppZGzm0FF5ydGr_3tDiyBeExW8qgAtWyFe2c8Um8pWnXv316Y1cQGaND5plapVjmBIXdW2g2xBfNyjqXDsYpiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBuHBmINNg4wiMez3F-XCUwCh4n-_2LP_GWmwRlvnv3TFyB8RtDkVdxb-Zy4nGNuP-wdA10DlFbZHZ3V7DqWPXgM6jJi_nBBZnfe_VWYMtMZVTwM3Gkw2PHhpNwx5Q94VeSu6SgJCCxIPXPNGYI1f0EMhCXR44ZpGDsZeziddZoIIatPBWIGUFywliuc8Ua_-t0R8rx1NXDW570NgtDN5LEjSln8aVO5c1ZPYPUopYboMTfzkUbascvXkreIKjppVfb7XzKleq3GoqDFwbxxxuEigMvroiMAWjN6zjiNAYNdzrFWaDGyALxHEazfkLoMoyO8bvmEuGzgrWQgGpGQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=Nk3rd5Mwr3FGbMQaKIBtAjs-WwDDyWQN8SmxcGJ4ndJsk-73ueDngyhHvY-qqVuQQqhWCwKsEPE67RNHWkTWxTFrFaUeBw-5fV-SBgWINo9hfSSFwFFYC2HSzl6qZSUxgm7m73DXOT4qeozkFgdId-mmoJIJy3BzJAKvIGcuYzDI9ls0j2T9HM82qh3zaFcwZs37ItN5Tm1jzKt41Oa_ZKOEFGQEmm3WXyMAxJtecr2aciHW89Y-NuLUPQ6R1qdgWfhNOWiuilR-HOOCjdjUHMH1jLGaQ6-jRuHETIkVMQVyfTCAzh8qS3EcqsMKZK4fMfaW9enrurMdR5QZP2GMEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=Nk3rd5Mwr3FGbMQaKIBtAjs-WwDDyWQN8SmxcGJ4ndJsk-73ueDngyhHvY-qqVuQQqhWCwKsEPE67RNHWkTWxTFrFaUeBw-5fV-SBgWINo9hfSSFwFFYC2HSzl6qZSUxgm7m73DXOT4qeozkFgdId-mmoJIJy3BzJAKvIGcuYzDI9ls0j2T9HM82qh3zaFcwZs37ItN5Tm1jzKt41Oa_ZKOEFGQEmm3WXyMAxJtecr2aciHW89Y-NuLUPQ6R1qdgWfhNOWiuilR-HOOCjdjUHMH1jLGaQ6-jRuHETIkVMQVyfTCAzh8qS3EcqsMKZK4fMfaW9enrurMdR5QZP2GMEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgFg5fLvQ9qtGZl_ZGg_FME9Z4L7CdI7-cbft2C05FCpnP-zNCsdbEWo0X_dE_clloabnr894alTzpe2Jfm5H2HHogVXh5GlDFy0qZjx_UsuHXBNL2YDadUV3j1Z9ZIeOhKzlOk-I5X8HLuh7tlJG0lwazvWgmW7WSICvbxXjdfBNXgivPAX4kdzccI8L4ZHcHFrhfr0Rk_Zo3iJRvU4ZGSGWf4RMXA-1Pco7bNsdJqUkEHJ6b_S3YoNH8lGeaRcE970zRxuTGqzAQlcU9H9fc-B8dz0gEPPtGym6tUS1B9Q0FSzkYKBzm2aEQZzY_UQc8JRGB4FZameAR93mOh-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHwYpc_scptyFcLcO80KB1Iuw_PcXX6BWACi6yw33DK90CGt45rQQTmlVkJsOVxcU7a4CfpqbwBq5grxaB08E7dB4dd9KgAFfDJR7StSmEGU9zdQr5MKTAMyWUIhU8XeM_B38cQS_FKi3TCb_ikAfmJhf-VMuYnN5WMxEhsduC8-ZmdKpw6MoasFsAYuTafyqc46uDUw90u6EqS-gsTbIVV-pXNb_tpU4InJUR7ajB5hp0-9n6R3yZh9K-wLaT7DSibXxzAydOOnlIEJ1yZnkV9XUjxOIMlJ2a-vZVTuyaAjxSQFZsFnSmplUoy3MbSUSGV-b-6mMkApa4fhaMppAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRBxd-041fkzcvKDVUAllEL_LvbiYIS6blwPhXTFbupztF31zJO4wH5BP_xNMqnzlArknogQgOHsMTIEkq9KOtMTYnFtxQ5mw-AgM2ZELfqClmMykAFTgoczEL_wVr6OSAuPF9W-iAt2kqTbSH0QyeUh879W6X1uxkrBedQQY59wpDReJSnEWulAGFFAFLqocDOzCdh8LRuDbp00JucTpcql1t8hIPNd1IGJ5lC-crUs7npzFBNoAn8PTq-6MG5lMab67-6kfmcnarHJe6M3Y66P2wHUsO3AbpHDRnix5riUD4FWdvU7-6rSLjE7UPSp_kYehAQZ28mQHCsgMA-8YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlpLvaYfsfgaCa6lhfLMDuDGPTJeWl1xmlQMFtqDgMS2weKoZrQdqfaAxSWXeFvQxw2tmCsEW91LvhZ3nXuN4s3djZAJoZv2oq3rjPo5LD_rKiK_cngNurc8MexhSpLXwmCYJYxZxuynXTnyt6V7sv3Sij5P6gwfckb4RF-_vLdh82lCbTwx4dlW3ty-qNMkTKfSdkMiLS9cuR6anaU7fR4GR6WUwmYpZvM85l2eIbYRncRgeFIyBRLKPBGZBbKt1Od0OZh3QPkkmP5tRg7mO1D2Z6krGy28T-2tMVCPRLqA-Q_7dUBUOoy_MJ23BHlNraFY3FEqF4khTeSNtbdhYdsE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlpLvaYfsfgaCa6lhfLMDuDGPTJeWl1xmlQMFtqDgMS2weKoZrQdqfaAxSWXeFvQxw2tmCsEW91LvhZ3nXuN4s3djZAJoZv2oq3rjPo5LD_rKiK_cngNurc8MexhSpLXwmCYJYxZxuynXTnyt6V7sv3Sij5P6gwfckb4RF-_vLdh82lCbTwx4dlW3ty-qNMkTKfSdkMiLS9cuR6anaU7fR4GR6WUwmYpZvM85l2eIbYRncRgeFIyBRLKPBGZBbKt1Od0OZh3QPkkmP5tRg7mO1D2Z6krGy28T-2tMVCPRLqA-Q_7dUBUOoy_MJ23BHlNraFY3FEqF4khTeSNtbdhYdsE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=Mx_jnPor0WXmMsGV_UF46VQlJgBkSoffWuZxvk8nAsOu3qEVe37roj1IKTpXxyhEYaCdmFMxyUAjiG27aKxSlFsMEuL1Zi8LRRDShBRHDhay7em90FWWi1WwlsWizUQqHe-sZCJsXLo5OZPNxOmNquMzlfl4d9-5iQfStUU1tgSCLOKJQzuRTBZ9r9YPz9YXpPyV58DQD9Hg11i06eRbTjvmL5S8fI_Bwd_ySaXk_PgHEIlfzaoA0aR23FduueYlha838SmDz2OhRWbvJjCq7fm9tk9eZi_etUYJUWy8ahqrSY3nV1EbImgfxEkpofTb_eykCPGrsTrz3IYTvtlazZiD0ojl5qpNfWCC2C4CnKV5Pc5tDyEIcfkKXPm8HvOXRGT7QRisgDtZ4aC8_AvhPsNFVwT9De0JsmbXcI8ZvX-oKNCQFoM5WVwMcQeuFtHN21r58olKQonmSY4XtFXdTWKRmt2zGnjwu8_ykOcmb3Znl7yNZYH12_TjV-w4Ds9cJZI7chiQQkjsfZi1VzKhS7X9QRvFTMB9QRuDbgnYBtkM2zMbQvHbZD3ScMXFvdor-MiunCOA2mdivBYqgLajCctXkgpCGdt5cQUASQcrHJ9UBS2skivBV6JCFiWy-2WxAh23-KudznP7XFDJxsjsww5uvfs5nLnuiF6K2cl_qeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=Mx_jnPor0WXmMsGV_UF46VQlJgBkSoffWuZxvk8nAsOu3qEVe37roj1IKTpXxyhEYaCdmFMxyUAjiG27aKxSlFsMEuL1Zi8LRRDShBRHDhay7em90FWWi1WwlsWizUQqHe-sZCJsXLo5OZPNxOmNquMzlfl4d9-5iQfStUU1tgSCLOKJQzuRTBZ9r9YPz9YXpPyV58DQD9Hg11i06eRbTjvmL5S8fI_Bwd_ySaXk_PgHEIlfzaoA0aR23FduueYlha838SmDz2OhRWbvJjCq7fm9tk9eZi_etUYJUWy8ahqrSY3nV1EbImgfxEkpofTb_eykCPGrsTrz3IYTvtlazZiD0ojl5qpNfWCC2C4CnKV5Pc5tDyEIcfkKXPm8HvOXRGT7QRisgDtZ4aC8_AvhPsNFVwT9De0JsmbXcI8ZvX-oKNCQFoM5WVwMcQeuFtHN21r58olKQonmSY4XtFXdTWKRmt2zGnjwu8_ykOcmb3Znl7yNZYH12_TjV-w4Ds9cJZI7chiQQkjsfZi1VzKhS7X9QRvFTMB9QRuDbgnYBtkM2zMbQvHbZD3ScMXFvdor-MiunCOA2mdivBYqgLajCctXkgpCGdt5cQUASQcrHJ9UBS2skivBV6JCFiWy-2WxAh23-KudznP7XFDJxsjsww5uvfs5nLnuiF6K2cl_qeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6BKZhuxhmUZMY5DzC6nyey7ntC1HoqC_RhUy7jai34bsyw7nGk_cqRYO9mng-yDJSoylNpdoVbGZXx2SNk6Qz09emUegc-iJxIvlYNO_5IMaRn067t87XbmyJh-Is0Tt_s5e1jtCyW-iHQJRLQxfVEVoEdaPB8D7veScudoyy4Wh2c8kL4x1e3od-QREJb5GCQiBRhEpN_BfPoZmu-J4AJ6wtGYV_bqsPPKHNMpb0p0Yb6yagRG1LHbrhjvs-XE1GisBwUQe2QMcLLRJbGmf0gOPX3x3WwlBxCjAYHsWqblmtwnloIQqCeMCs5e3H3EenDsH8KKuC_EEt5ARl8dQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLCpRmYO4GQRCprV6rNXvFDM3ZYObU2M6tkMD-acapsvpZ0mtmT3k8H2mrSzB-cpboLQ7NNTRP4WSu604DhKNtj1Yt65-bjhcm5a9o-nmvW62fP9kKJmKYIaYbqacoACZyn409EANDT_mKd2dPLR0WiycXVMzs8iTkJBI9jcYyqYwJtg8hRM6FU7ODeIV9otSzXt-xzfss0MrXkC5QUDSfeWVr8MYFENOoesEMivp5rgPG35SPbpbS2U8X7dv9ixcoYjo8_EB-6lLp766UfiS9v1K8fcsQD8MxwTvVqulf5sh6JZXPl7SR7bRWR5Kj-fguucEfooOSng5av0DzkL0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPfZ5ZCLAYoitfyIZuFCKP_gLEiNVlVYxLikepyL4M1dPzQlfMyHvHSls9lNeTHApDe17M_OUYa4TJKNXq0dWy0-ZvDnPcwOxwNMkOz_KxhSH968qrtk8Gpo-v3_JRwlrs5BtImX-Bt70JQgGps8wvB3os_sFRw5Wc_Ie5wyK2S-Mu7_tBufkePCqkCmGuTdbzl815gry-2E5gMPaiYknXEHIlmWQj1rpv08Orb1GCk0OuZBH3L8Y6wNlgnw82woUS4ELS4QQrustYHhosC2ZhHmQEzHuPIR4MUmjoWedhKBydff4Ol6SRbkg5HCjfeccF7ElcuTqJ5H0xHYiN-cMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=g55n6v5UjhKFR0la0dfTv6sN5aWHGJBEc6HOCFsOyBhQRSBNIyJdQmW3zLlj2l8LsXzAfm6J0u9fpMyRonlr5LpDUHyVLjReQe8MWvVJ5T-ZAnS08wsBSnZt3OHHVRxWU2DF_x-AekFvQ4SJpSa6t1htrvXkO1QxHsDMhmXwFj3VTTFJATrXFcNFgD-_neBGyVSrU7cvO4NlOxeK9m4AT5AVxDOPHTzynWC3KKleJ1Itb1rdsASABRZyRgYKKukgc8W4ZV_rmlifIHpvoS6Q5ZeZC79j8k-9rKQTG5bcJr-rJlkylQPDGnOhJQth96tPow-K3WIaXirY-ilSorwb1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=g55n6v5UjhKFR0la0dfTv6sN5aWHGJBEc6HOCFsOyBhQRSBNIyJdQmW3zLlj2l8LsXzAfm6J0u9fpMyRonlr5LpDUHyVLjReQe8MWvVJ5T-ZAnS08wsBSnZt3OHHVRxWU2DF_x-AekFvQ4SJpSa6t1htrvXkO1QxHsDMhmXwFj3VTTFJATrXFcNFgD-_neBGyVSrU7cvO4NlOxeK9m4AT5AVxDOPHTzynWC3KKleJ1Itb1rdsASABRZyRgYKKukgc8W4ZV_rmlifIHpvoS6Q5ZeZC79j8k-9rKQTG5bcJr-rJlkylQPDGnOhJQth96tPow-K3WIaXirY-ilSorwb1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1RISMoh5PSnKPfLjKb10nJe0hClpzECkyN_CJ6muekZD4O-pg0hRqV2x52cMTEiouewTXkOEBRYofntVOW5-Nh66kOqYw8D8DYMsIMuhlqnFMetPwy0gTo5uUrQU6nPHOmhL2fRNl83Zqp2TyNy98RePNpHtdlc3oDs-YJTCLhjE9NwtpIgGHPAA_S45vALGvAmM8oP0UKCYfhOMdj-z0TlUTZb4Tue477VG715dJsD77SVZnNtfVkRvF9x74Uj2yEFvgrBufBFRwpKo1F9AZ1Zt6BmW4rlHWJtaMaOwUZLzmQHE4DDyS240QtZRtfSDRMLryghFpb6ItaxfJznNA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=cnIpI-8jjZGCIfMKfB-kgDBYzlnLM4DEN0U6kRtzBRKFtj71CIYyfYARzHYdjPssbdy2assJ64S2J7hFPbiGVfVXiGkOOZB5PU7xHeadqoeNOrDX3Ir1KQM7V1dEY8a4XmPORA5YTUAiLvnjXvpbua4aIYaUlus6jlX-y-fKph55DoN0WJwnOivWfEXnCarZit34e3llywMnjma0KqoEWBTb1IBMudzhD4I1fPXAkOzFVoaeZabhAkQUrpsMBycHMerA9Ame-RAjRFs0DAWmhDPJkbwOcY4LwLKBV1vV73yVM8xv9bM4pAqMf4AHhZYiZmNEKkYOs_N7knCrxV1gwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=cnIpI-8jjZGCIfMKfB-kgDBYzlnLM4DEN0U6kRtzBRKFtj71CIYyfYARzHYdjPssbdy2assJ64S2J7hFPbiGVfVXiGkOOZB5PU7xHeadqoeNOrDX3Ir1KQM7V1dEY8a4XmPORA5YTUAiLvnjXvpbua4aIYaUlus6jlX-y-fKph55DoN0WJwnOivWfEXnCarZit34e3llywMnjma0KqoEWBTb1IBMudzhD4I1fPXAkOzFVoaeZabhAkQUrpsMBycHMerA9Ame-RAjRFs0DAWmhDPJkbwOcY4LwLKBV1vV73yVM8xv9bM4pAqMf4AHhZYiZmNEKkYOs_N7knCrxV1gwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX33DO7L4brxootCC_HPq4jIgs72q4BJD4sPBI0MzJm6pJ-0tcgS-yWKQ0OE03Tn0l4-JDDJ9KrB0TMiBOpEN9dPKsPf2Uox0wsBfPcgchBTpqQH7aIhEZojar4YH2THjtpZtrn2PFxpPVyiWRtX2PSZwYPv9XvzVhOOMAG3EXlG69_Z5oTnlCbZmD7knVSsjnTkp0wfZULqiDjOrmQ0DG20aA_0T5fFaqSWIeyvzc6z4zbiREgi0gWs5qr2F2bXB8U0svimdPSfg6mweeA_f9EViZ_dGz2arAkNjymEciugezsnO0ZmEVo31PCbN3N-QgZA44SNO16mD2cLMk3NJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuerX5D9nY2buvm64yejqYpshwezIxOhF_aIWzGwrfN7DZWm39cPUZhOtBA85vKRqDvE4dq9DdygP6jhZFJLu4bjUZokbePGSdwU_TBe_6HuDuyomyLWJTKySEGHYsiWTVP8xhOxrgrUkWy7vqSDDK5_Cfu6bl4BKycjqPzUBdByN3VDJigF687ZUjfhs6zOJsELj2FXkEyVHJNY_qMMwwp7wKm1lw5j311DfTO-Cw7ok5OLd65IrA_QO4m1vs8fV2JcL5GUZl_T6zaUuHAkbmspVmc0RmruEFWjK3xOREyW2qvMtFd_awdiSGFqK-cUVRpav0dz75l4JU-toR1Csg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=WghlkJjgDsX3emtxca3GP5MqFMxrmu_oL5o7AL9fSNak6alXZNJ03DDGIDfrmN7RoxYjZWwf0ptaclhULMdujZX1Na2vAKN_Y9Zb3X1miROU2I1EieQEPEmM2ccOgv-tYg57KsmpEqq95_0MaAuGqJi7a_XVVSRlfd7ni5PlgyXPMwKUUF3XMUvbHEsnhQxN0EGQN1q5tMjLp0fEKH85TB0IeUhNAX6L4uZqU2oxjgJHmfGd3HYPxnHeCicwR60VfsKde6LTlgSUbKL_yHBTWC0XkaPjMeenMVs-mkCoEn2Von0D4Jnt4xgniZCHgvw3RXxlSihhmSz0WNAtXcJdaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=WghlkJjgDsX3emtxca3GP5MqFMxrmu_oL5o7AL9fSNak6alXZNJ03DDGIDfrmN7RoxYjZWwf0ptaclhULMdujZX1Na2vAKN_Y9Zb3X1miROU2I1EieQEPEmM2ccOgv-tYg57KsmpEqq95_0MaAuGqJi7a_XVVSRlfd7ni5PlgyXPMwKUUF3XMUvbHEsnhQxN0EGQN1q5tMjLp0fEKH85TB0IeUhNAX6L4uZqU2oxjgJHmfGd3HYPxnHeCicwR60VfsKde6LTlgSUbKL_yHBTWC0XkaPjMeenMVs-mkCoEn2Von0D4Jnt4xgniZCHgvw3RXxlSihhmSz0WNAtXcJdaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=E5vRUJS-A9CQC9UrmSsdxqoJxfJ1Mxxb7kfdt5qp_0DpJ-3nMd_sbd0MNVT5UBIVCw8gPZkuE_wv3bvune7qymtcvwJ9uNe6uwyg9JafKk6uq4Jn3LW9hySY_hZv6FcLDlM0E86hS4mC4H_Kw-fOVYFYFaHZNTo4ex-ZpwWHBUIsCAOtPZzW_T8hsonrQ0H24aXUDukVvXDTPbwIpHmYNCiVjOyQ3OHOOn_UlqU5xesfOVPsvkrOhx-3RsqQSjRzVcaw83KmPjffUKpa4_ykk4q4IYbNGCVIRk8AjU5Ce4JQQctafxOHWbn6TjyAgZw5arKAKhh1DWBV1pEtmOxEnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=E5vRUJS-A9CQC9UrmSsdxqoJxfJ1Mxxb7kfdt5qp_0DpJ-3nMd_sbd0MNVT5UBIVCw8gPZkuE_wv3bvune7qymtcvwJ9uNe6uwyg9JafKk6uq4Jn3LW9hySY_hZv6FcLDlM0E86hS4mC4H_Kw-fOVYFYFaHZNTo4ex-ZpwWHBUIsCAOtPZzW_T8hsonrQ0H24aXUDukVvXDTPbwIpHmYNCiVjOyQ3OHOOn_UlqU5xesfOVPsvkrOhx-3RsqQSjRzVcaw83KmPjffUKpa4_ykk4q4IYbNGCVIRk8AjU5Ce4JQQctafxOHWbn6TjyAgZw5arKAKhh1DWBV1pEtmOxEnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=mkyiEAJcQDjc-Rj_YDKP4LcHS1Bm2VehlpQp9ax7wWVmUJh6pYNl8Usx72o6pz8uBbakZm_h6lxylfOV_KHoFd1ODTuG22Uu9Fg-46eYPNwkC-B3LpQwc4huAPBJfRitQipIeee1LY6keVb0vQM2BPV39Mzn-RCb_HNNkEVGEay3VmnRVBTIMACfeG6q_sNY8OLgeXWRDmo35PwQNz8Tc6NnUGXNVz5lRhrso42oofJg9pbTLz73hM5Hba_okB9TunFU_Gps6xefsmHVmTwDeP902Tf0zqvo93ZVkOlt9EYh_wZXQV20fUMVmh7VYjWKH5BCpBgNSNJW071hXG7TfX2dXVw3o0WKQypbajo4zX7OyV8Mm8m5tJi0pwzM4JOg54sht5LCKgBicfMuIzDqlXb3XHNAH49cOBL1wWSltVnyNYfHfTlRJc_DJ2SmiQs-_ZYVeqgc9A8TR9_p1_edzSVQdwkkWtVJq4OUDjxtgln8TcXigLAz9sHi9IC7dx7C6lRVa6Ifv18s4qENAqLCNC0gFw8GPwd3GA5s075WGxjkA-PFbUUUhtX4dobbF2HSAArpFIuduOG3c55ipG-oK-bPxigTrr2nxQa1BqfnZFRPkJZkOLPfUgyNh5DVub2i3AIVaaHWcZiGtkSTo-NPeO2R6uiXCWvcfDJRcSX3pvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=mkyiEAJcQDjc-Rj_YDKP4LcHS1Bm2VehlpQp9ax7wWVmUJh6pYNl8Usx72o6pz8uBbakZm_h6lxylfOV_KHoFd1ODTuG22Uu9Fg-46eYPNwkC-B3LpQwc4huAPBJfRitQipIeee1LY6keVb0vQM2BPV39Mzn-RCb_HNNkEVGEay3VmnRVBTIMACfeG6q_sNY8OLgeXWRDmo35PwQNz8Tc6NnUGXNVz5lRhrso42oofJg9pbTLz73hM5Hba_okB9TunFU_Gps6xefsmHVmTwDeP902Tf0zqvo93ZVkOlt9EYh_wZXQV20fUMVmh7VYjWKH5BCpBgNSNJW071hXG7TfX2dXVw3o0WKQypbajo4zX7OyV8Mm8m5tJi0pwzM4JOg54sht5LCKgBicfMuIzDqlXb3XHNAH49cOBL1wWSltVnyNYfHfTlRJc_DJ2SmiQs-_ZYVeqgc9A8TR9_p1_edzSVQdwkkWtVJq4OUDjxtgln8TcXigLAz9sHi9IC7dx7C6lRVa6Ifv18s4qENAqLCNC0gFw8GPwd3GA5s075WGxjkA-PFbUUUhtX4dobbF2HSAArpFIuduOG3c55ipG-oK-bPxigTrr2nxQa1BqfnZFRPkJZkOLPfUgyNh5DVub2i3AIVaaHWcZiGtkSTo-NPeO2R6uiXCWvcfDJRcSX3pvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xfw0X7VcqR8Wzx-i4dvJCyP5EGuvxi-j67fhmYHph6mKD87_OPmXAYdGVoRzhlNMj9tBQoDEM7nqgov0to89Jg70V_ca7Q3ZKk6fbrdqCRMXsAVX1faeSoeWtFAd_0bnG_j-g_yacrp0KneW8pbXeW_EK7h_cZ7i7TseUkecPwcGFeXcYAi6TUvxwA7Zx56gxUzStqvdL_DZ3Cjytku8heDSpf1Mvlm6Ik2mZzCayV8UdcwYK4MW9jAMWlHgh0tYGYeFfb97OhwKRuphgUQyMqRwonyZw1wkM_UR94Oux9in8aFnOLdjxsV80vWWrHRqyGma139o10_hAUc3pENdwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsDFGC1aKCcbSM6yOIdCsrL5frwBUxpNfZ7tBgYKYzTiNZIeZxRIMjEFC1jR14Z_MAKpN0esIpoi0Hmy4NHYO6H6GjDmnOIyMiETNgnSq-eB_TJouK_fuksCRgQKajcB27Vituf_mAyuTvlO3bNosT4Iqn9yipGz84vR_SM2Tz7OwZLdUsxKTwX8GPujFeyIUZ7NxSl8noBuiiJ7eMfQGTEkIugg78WDDSDYwnamcl7NCTDbF1Ou01xzErsDAP6h1Hex7NvhJhtBBCKzUF0Fu3ULQq1MYxfpr89_Q5PTpp5AXIIRnBbsa_f7qZlhJYb-ypP-HWVgQpv_SkBPD2djkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-aoOFo5C3xHDAyoag4gqiFZhKeY9cM1NREwyCuO_UqrXMe_Z-kIbUXj9JIDLkcQo8creqMTLSjtT9WyfLhqGcMjc61PDBiskTUpdCpvmBr40eD89-85GBdurMdVhycwGUY2KCrTQbwJu49Uk9N0FjgVfE3uQiRNXcpmOdwXmNNo0B_Bkeb4VtnK3FmMdCIttTP4Y2LxWZ1rhIv17MVGo2MGmRCYVgDZdgS5qUu56yuOr2DjPzOQaXjsO8Ze6llPN1jnyQ4ZjPiIySTtTWdkBEm5tAQDXiBKAYkGQERMYEojCbW14a4nwwqRVYI73OTJhZVxSbTYEkEjjUFUcuoDUg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=FcEJQAsLlfH8SwAwYldbphDyaDo1Ha6QS9fVGWDt7sQaWFnB02uje9zqm9MxB7xWj_i7yhZ_MNU4GiZ0J8Cqf_j29o6p95gg3QXogT2h2UAmfdfOh5awAJ0QtzTQ7K9L4pW_9E98GHcOHwhymdzqjb2MIkvRSHXS5LlngVEjPT8m2pMlBobFS20TviZatnvXtVEfQnsJ1pO6hIlDCSwAtsRC-6J37EJ8wrLKURBRM7Skk-r6KeZlgjCLWiqtVGhmTl-y3cv1N9LU_7OuzUHyF96tbQw6RIyf4oOvAvAWNHJ4ZpDaULOBdm46AkMmPdnN3jWMvRTr-B6L89I77wwxk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=FcEJQAsLlfH8SwAwYldbphDyaDo1Ha6QS9fVGWDt7sQaWFnB02uje9zqm9MxB7xWj_i7yhZ_MNU4GiZ0J8Cqf_j29o6p95gg3QXogT2h2UAmfdfOh5awAJ0QtzTQ7K9L4pW_9E98GHcOHwhymdzqjb2MIkvRSHXS5LlngVEjPT8m2pMlBobFS20TviZatnvXtVEfQnsJ1pO6hIlDCSwAtsRC-6J37EJ8wrLKURBRM7Skk-r6KeZlgjCLWiqtVGhmTl-y3cv1N9LU_7OuzUHyF96tbQw6RIyf4oOvAvAWNHJ4ZpDaULOBdm46AkMmPdnN3jWMvRTr-B6L89I77wwxk4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=SgKCk2kOR9KdMM-BpY_CHyXWFv5CPHRWTB-G2VVfeq9sCRRqwlFV-1Uu3yzOcKi150kNEgKRUHl7PD1jUagovirWt15SFG8NZUdgx4x4lDSzn83m2rdFF89jA3IkxcMgnQ0rOpEjUuIr_SDpoi_kK-Vsjqf5eC1BKuKL0dHxoiIADe_gtP-onIlGocfg2gvgTs1Eypq7Ej2eAgy8aDkh2dJaWCmerNn2iQ_KJ9GcwLGmABrVbJtUdt2Z2RAQqWlREFQ_bKqU0UlXByxVIea9EnEoH_p5CtES-IixKp_fBtG9Hwiae-yziGsEijwfy5ey0VZsr7jPX9n59Al22XNWaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=SgKCk2kOR9KdMM-BpY_CHyXWFv5CPHRWTB-G2VVfeq9sCRRqwlFV-1Uu3yzOcKi150kNEgKRUHl7PD1jUagovirWt15SFG8NZUdgx4x4lDSzn83m2rdFF89jA3IkxcMgnQ0rOpEjUuIr_SDpoi_kK-Vsjqf5eC1BKuKL0dHxoiIADe_gtP-onIlGocfg2gvgTs1Eypq7Ej2eAgy8aDkh2dJaWCmerNn2iQ_KJ9GcwLGmABrVbJtUdt2Z2RAQqWlREFQ_bKqU0UlXByxVIea9EnEoH_p5CtES-IixKp_fBtG9Hwiae-yziGsEijwfy5ey0VZsr7jPX9n59Al22XNWaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=fbMhDoINOTVhlwpJPglBwkpnW-V3vPHJQPiYf_HNIQSMQEWD-m4WzPbslarfshhVC_tJTr91xP3TGd9-xFsU_VwmFs4LrZDzYr03JG72YjkQ9u-XAih0FxFVPORYIctpO7T-Ps58gF5IbNuV74SziU7RfUijvSBo6OLzDVG8lho9UNZgt_x4WgH_pliU5_k1-otP9w55PSmQxQum9--GJCO_AzuRitYO5rCB2bilcPgR7kzJVKVQd8LvNmRqv7izrJ5iKJbgS8I69JPpf3F4Nik2pirzIwo_zYSgbEpEofdIn1HQC17umIOiSBTgYWYZRQj8dxWJ2unQD8r3jgEfNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=fbMhDoINOTVhlwpJPglBwkpnW-V3vPHJQPiYf_HNIQSMQEWD-m4WzPbslarfshhVC_tJTr91xP3TGd9-xFsU_VwmFs4LrZDzYr03JG72YjkQ9u-XAih0FxFVPORYIctpO7T-Ps58gF5IbNuV74SziU7RfUijvSBo6OLzDVG8lho9UNZgt_x4WgH_pliU5_k1-otP9w55PSmQxQum9--GJCO_AzuRitYO5rCB2bilcPgR7kzJVKVQd8LvNmRqv7izrJ5iKJbgS8I69JPpf3F4Nik2pirzIwo_zYSgbEpEofdIn1HQC17umIOiSBTgYWYZRQj8dxWJ2unQD8r3jgEfNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=T9L1MdsTjn-kM7WrWMrtTw-VmP1wCtjbx-5L5DOkOQ2IDpiyTtCFWK8kGn6t0xkBqaQQhWUUoQbjsFMHXMeDdwbxqvE62t0yTANPUWpKBN9mZHGdsxdFjx4tBJs0QuztCjLbLalnLNXYVz3bSg-H5tiFuSKeX7Bhk_MO3bKUhDIGDbr03U8IigdPq3szsv4JCJkPwyQxYj60qyDq8qgxdyANy5CxOgqIrowSwQ6br9Ydv4p5kThhBa-U2bmbVjyCLRKRo6AF6OzS67BjfekcuR6Oo4XYAIYBR9UorV-cId36v3Ls89U4kQi9x-zODBSOukZ192EBf0AIjROrY_3DSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=T9L1MdsTjn-kM7WrWMrtTw-VmP1wCtjbx-5L5DOkOQ2IDpiyTtCFWK8kGn6t0xkBqaQQhWUUoQbjsFMHXMeDdwbxqvE62t0yTANPUWpKBN9mZHGdsxdFjx4tBJs0QuztCjLbLalnLNXYVz3bSg-H5tiFuSKeX7Bhk_MO3bKUhDIGDbr03U8IigdPq3szsv4JCJkPwyQxYj60qyDq8qgxdyANy5CxOgqIrowSwQ6br9Ydv4p5kThhBa-U2bmbVjyCLRKRo6AF6OzS67BjfekcuR6Oo4XYAIYBR9UorV-cId36v3Ls89U4kQi9x-zODBSOukZ192EBf0AIjROrY_3DSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpbWke8ryFjIn8_MD6AP4bi9YAJmhxOexS-Nx6HpBoozY3FBGufOu8lNAHcLOoSWv0q1UMqYwakU3H7jpTVHCOWQQYSfNdD7B0XJS5fgpMzRQhiZuM-IWDH7IjZZ8i7L6lNMaNpXzy7lS6g_Bml7ABdttKp0MkUXGSjM0a8lf-fSl2NX1kCg6ER43Q-YVwh_k8FTTf8ohsANJ3ON8YszUk2EVlbBlbX89gqesJBGKK1AXSRNMRj8rFNRvgE0c8jaoYdzWrPgpcrpTM6tTBXZdhB23PFfnAwkShtI2o6kkR3K_V_52DfBiBNvVxB0L4N6UeOWtlL4TF_88m_w7ln2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=jEnqcse4W0_MaO2C2Gew_DcyWxp6CfVNR9SVU4F-LFgShJO8Pmz9p271robfVEaxzxE0_d99cYeU0vWKgeaj1y0JIHxvSSG1N9urZVHf1jKLhYYDhTAgzrqA8_d8CjpMhx6Xh3pVta3A2QRl4CDTbor59Z7c3-LPqWeom9pbyJuVVOYPo6SoV46hc6Gc33ZCHhgL8ptXhM3gWQIEipiXBG0_I_eCaJobYEYXXKydHheLKpUWcmawUk-Nyd0EDY5dtxV1HdhacDxJ4hpaaBIUkB6ZD8OSQf3ASN10ZtLBG1kt6BMDb4YCPJHAC8Ae0H0XU4TGzNi03HpWCLYkCW2QHw5s2PGgmZstQ1N087AwCZZbqpSET2OMWUU7vy6mv_IAx5htUWaYXHE-SEm0bFkcsSLgxlVH_FF9SYN3-cOAQrcGczlHY0g8DsbctrXKBzCcBm4Wdh8uPJbX6BBNFjBl0gRm7hdmTuevWpwaRoQspzihfdg13z9Irmwg7x_UY1WjkDl9dzTG5sH_n-8iHiJ83f8ocOPm6OEm1h0KsGFpZb_KDNN5g6Pw9ZJH5vlE9dz8UpZky8VkG_M1xVDoEbubvFEbJrTTW3rrilFN0SHzhg6Z6h9ScDJzN-3HlIf-LlkhtiljdIH-7AlP37uyL-pGvFQH-MBsMtBJVPp6TQv1kmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=jEnqcse4W0_MaO2C2Gew_DcyWxp6CfVNR9SVU4F-LFgShJO8Pmz9p271robfVEaxzxE0_d99cYeU0vWKgeaj1y0JIHxvSSG1N9urZVHf1jKLhYYDhTAgzrqA8_d8CjpMhx6Xh3pVta3A2QRl4CDTbor59Z7c3-LPqWeom9pbyJuVVOYPo6SoV46hc6Gc33ZCHhgL8ptXhM3gWQIEipiXBG0_I_eCaJobYEYXXKydHheLKpUWcmawUk-Nyd0EDY5dtxV1HdhacDxJ4hpaaBIUkB6ZD8OSQf3ASN10ZtLBG1kt6BMDb4YCPJHAC8Ae0H0XU4TGzNi03HpWCLYkCW2QHw5s2PGgmZstQ1N087AwCZZbqpSET2OMWUU7vy6mv_IAx5htUWaYXHE-SEm0bFkcsSLgxlVH_FF9SYN3-cOAQrcGczlHY0g8DsbctrXKBzCcBm4Wdh8uPJbX6BBNFjBl0gRm7hdmTuevWpwaRoQspzihfdg13z9Irmwg7x_UY1WjkDl9dzTG5sH_n-8iHiJ83f8ocOPm6OEm1h0KsGFpZb_KDNN5g6Pw9ZJH5vlE9dz8UpZky8VkG_M1xVDoEbubvFEbJrTTW3rrilFN0SHzhg6Z6h9ScDJzN-3HlIf-LlkhtiljdIH-7AlP37uyL-pGvFQH-MBsMtBJVPp6TQv1kmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=pYapEJ2em2cdk_YsL9t8zZbXF7jZ4qNl1M2kY7WAK4-6yNDCle7ZDrwDYWg7lpaMYbE23x9NMpsD--h8xz_xCj3PUjj41brHlVbRAU1tBLRgf7M0E0geqGRu1jkhWZLl2BPvfgvxv6R4hUfNxvzvqalmeH38O1VpMUbfVi5hNqkBMF5FkQbo5cQHofqBta4BRTfwTIGxQm-VDHMS7X_0OeK0Qywp3l8md20S6H3VJNOV3Ys2EgaOjdQ21k1lyNfYFs0qtv_Ibw7QMRtCVrgQfRzHs6rBtMdNb1ozYl8uAl9SISQsKanKw_U_BZv17rSLcfTszrhmX3HZ0nLhzSJqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=pYapEJ2em2cdk_YsL9t8zZbXF7jZ4qNl1M2kY7WAK4-6yNDCle7ZDrwDYWg7lpaMYbE23x9NMpsD--h8xz_xCj3PUjj41brHlVbRAU1tBLRgf7M0E0geqGRu1jkhWZLl2BPvfgvxv6R4hUfNxvzvqalmeH38O1VpMUbfVi5hNqkBMF5FkQbo5cQHofqBta4BRTfwTIGxQm-VDHMS7X_0OeK0Qywp3l8md20S6H3VJNOV3Ys2EgaOjdQ21k1lyNfYFs0qtv_Ibw7QMRtCVrgQfRzHs6rBtMdNb1ozYl8uAl9SISQsKanKw_U_BZv17rSLcfTszrhmX3HZ0nLhzSJqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzt2-8PzV6kSvz7PAy1d00FZxqbpTAA86xtUJ1Z4J9wADEAUV6Qgr-VLFezMby-O7VWYi8iSXZzhJpudKjxjgFNWewvbcbWzObHtq7HfK32abYVoPdE7fdhBfSkQuL-0wmpPSS53xVruqPKfmUuCef-aimzT-RHhCPDCCkvbe8WgtY-KgMTmKTShRhlUag0wqWOeUdRCPyDTUtmyCxFnp3mE2CtB_U-ySn3IvCQCC7iP8_d4K2PyIoaCMNKCZrAy8GQuPXkoCLq704KiRc-2v95nq0UFmxXF7WhL-lhlDT1sNpwF0dwPl5NaMeVuXOTt9TQ7IvBvF48gInr92k3_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=aWe_oWvpQPaCzUkEsoxpOvSL_nLFR34BXDChYWIPbGD-S5xW2rHU0guLj6CjiKBERIDFOJ2On2cJvrxqs8Wn9LtjrWF81rpNaKzK3pj6Dkq3Ewf0qyg4CW2JFaavEWW_eXbX9oFyUJJpT7XtFGUuWbKtG15R5U47t9F22WTUZVfEPfSm58rIFsDl8vjkEy6qTfeUhjiUVOy0JxcVvUdoHhgwCNmoQoitmVoOPGikYtSgsDZUVgyoj25oNtZnO7CvAPZuOPUzlaYNNM1tXodtExGbiaFxnbfDgANteXSvUd9gBi6QVCw_vMm6XWmcQzZ65JxLoFgWQ81NJLChPk_bKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=aWe_oWvpQPaCzUkEsoxpOvSL_nLFR34BXDChYWIPbGD-S5xW2rHU0guLj6CjiKBERIDFOJ2On2cJvrxqs8Wn9LtjrWF81rpNaKzK3pj6Dkq3Ewf0qyg4CW2JFaavEWW_eXbX9oFyUJJpT7XtFGUuWbKtG15R5U47t9F22WTUZVfEPfSm58rIFsDl8vjkEy6qTfeUhjiUVOy0JxcVvUdoHhgwCNmoQoitmVoOPGikYtSgsDZUVgyoj25oNtZnO7CvAPZuOPUzlaYNNM1tXodtExGbiaFxnbfDgANteXSvUd9gBi6QVCw_vMm6XWmcQzZ65JxLoFgWQ81NJLChPk_bKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=BzoGhHY_3lGyT_KqU-d9P7VApvJP16_8vQAKyyajvr816nxTis7Cb855FoeYFa2ptswaGiI-5Tqy0m7oPt0q4tuFXlbgpn-0pTFZpoVdv3tzlMMZaKJ7--ZMjiyYsVAMHis9hJbrKtxQpZiffJ5xywCjV7piXqBEJa2fMuur5WQGT3EufXkhNSZt81qI5C1OHqSCqKavgjyT4GwlZO5cdaMhGTkrCYz3XXHWlPTzsTYcgv0sHZwg4UY-YcD2Uu09Ejz2NnU1Bklw6vUlGdrIzpFtEbHXkWGJsH4J2yCHIL1lto5cEIfIrNCZpxhV_bDjBhYGrYuiTDD29zHb0zULjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=BzoGhHY_3lGyT_KqU-d9P7VApvJP16_8vQAKyyajvr816nxTis7Cb855FoeYFa2ptswaGiI-5Tqy0m7oPt0q4tuFXlbgpn-0pTFZpoVdv3tzlMMZaKJ7--ZMjiyYsVAMHis9hJbrKtxQpZiffJ5xywCjV7piXqBEJa2fMuur5WQGT3EufXkhNSZt81qI5C1OHqSCqKavgjyT4GwlZO5cdaMhGTkrCYz3XXHWlPTzsTYcgv0sHZwg4UY-YcD2Uu09Ejz2NnU1Bklw6vUlGdrIzpFtEbHXkWGJsH4J2yCHIL1lto5cEIfIrNCZpxhV_bDjBhYGrYuiTDD29zHb0zULjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9cuHi-NWNHbwhR0BDdQM1XFhKaAfKSbmjKfQr0rtDpdSFX15Uhtv32DCznYKnpyqDPgfUgarAWZUTT_Qsi71I9ynKRHhRDnKKER0_yfnDhWBATn97iuA3IXsBmbJiLax5DXn22ZG0rhCo7CUCj2Met-J9m0LKVpH7GTjqfmPDJIQxK6PJEFlJwZ-7OwEhW_N6P512bJ9GnrJDbRWUA82WGX9Z3HC39dhK9AcPMmEx2zKY8U-aAU4UizYZEgHQU8oqBYt4g60GADwLAp4HBBjGkEIbSNBbP2u-j3OvHte_fRbiv8KKBz-ZZd77GnjcmWBlUwJ1a5V1xjvMxYPVMJfA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=iMC-9KoqQp9vlTH3Ls2jQ48WZBLOftSW9bed7Xnb1z401TKSHpRNHoSKUtmGzGJ8HFF9ECRdNAUdNra2ulfdAGS5Ax1DyexTgB2Nx-G_SUCTRFL0FbivRODU4kaTxAMvUuE0YmewT4-4Flrly5vjpTX0gOyM35neknPsnu3Hpw8fiIfNA3yw83S2pH2j-1307TVsYoTr_iHvPNU0kqqEBaYGqhUpVApxAkK-UwKjgWw6d4_WtE_z9RiGlqtUEmTBvSKSXXJ5VxdhkqMxXGbu5ybki-Pv3qQuCW_0_NpPMm_7Pw0Jh9q20x4SUvWQ1fcd0mY6Yd-KlziNSTNQD9YSkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=iMC-9KoqQp9vlTH3Ls2jQ48WZBLOftSW9bed7Xnb1z401TKSHpRNHoSKUtmGzGJ8HFF9ECRdNAUdNra2ulfdAGS5Ax1DyexTgB2Nx-G_SUCTRFL0FbivRODU4kaTxAMvUuE0YmewT4-4Flrly5vjpTX0gOyM35neknPsnu3Hpw8fiIfNA3yw83S2pH2j-1307TVsYoTr_iHvPNU0kqqEBaYGqhUpVApxAkK-UwKjgWw6d4_WtE_z9RiGlqtUEmTBvSKSXXJ5VxdhkqMxXGbu5ybki-Pv3qQuCW_0_NpPMm_7Pw0Jh9q20x4SUvWQ1fcd0mY6Yd-KlziNSTNQD9YSkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjPjPACq3nGtc9tK3QamEtlClbB5Nw1QDEbOv93wQWAgtcPfLzx8WYUOLfPlwv5G5yzpeFnFqh7p0QaY79pi6YB-g2MZ6xSCCwyesI7sZNK-4FGEKWOcT41l_W4vxOaIosSBR0vlrHb3t-_ZNovS64_QXfduy9cUXyQVXzp-9vDrqiqpdcd_mnNOp62_MYAiHl16PDzjee3XSsGyjfzBqt6EtPiNcz3O-X_tr6eMkLwmmZ_mMIdFpel60F4Zw_K4qKR3QfgGhjFzVfeOGvA9StHKO-ZPXe41zXHpzCFUibXWdEgOyswdawkAOSe6wEf_XyV5ivy7UVMaiG7aXn8jOA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=EQ7sqGkB6AfIS2HEoCHp2rNrT-u2Q0vU4cQyNpzkA4Rb6iHuiAPFnPmL6T4DasYenGjmAIBma4fU40y7HZgJO6jp4dGdDnHjrueFhz4eV2Rc-qoAn6vWKAgklt3A-a5n87T-YBBkmN7S2MWp8GEk0RNBVI7EIRys11impSNi4sDmHnQducu0NCTQWnVZ0fcPg0rfZVxwVyV3puSwRs3aM_-oR1BJ0ghJtaO0zg59ZVQ2ejoVlRLJjLtRH6ghXOFqgCn2Jn0w9f5q4wYyBKVb0yYs9n6zaH3_KegA7cM1k2K4D7fEE8rwzJadcqiJSRbKpkvlVVOAdmmXZGoe_C_xDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=EQ7sqGkB6AfIS2HEoCHp2rNrT-u2Q0vU4cQyNpzkA4Rb6iHuiAPFnPmL6T4DasYenGjmAIBma4fU40y7HZgJO6jp4dGdDnHjrueFhz4eV2Rc-qoAn6vWKAgklt3A-a5n87T-YBBkmN7S2MWp8GEk0RNBVI7EIRys11impSNi4sDmHnQducu0NCTQWnVZ0fcPg0rfZVxwVyV3puSwRs3aM_-oR1BJ0ghJtaO0zg59ZVQ2ejoVlRLJjLtRH6ghXOFqgCn2Jn0w9f5q4wYyBKVb0yYs9n6zaH3_KegA7cM1k2K4D7fEE8rwzJadcqiJSRbKpkvlVVOAdmmXZGoe_C_xDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frgkQUzT3vHE_tH8PVsMTcRBx3_36f2X_R9hcPM-xrZnWIoFHS0_m6ZSSImpEym3gJzlFXzFfurWYufNQZhyysD72nbbSChFFUYZfizCyYqmUpNL4MN8RzWpg8iXf1LgQnRsfnJfehgz4cKGn9USBy-UgoAD4Yse_B36ohHCKpfXay89C-zy5dlk243hlStVYjDi7L-Tnx8SqoYJhvgPpQRjzdIegcY9CD__k2z78kvKME5cHUwpOMWgoPUvXviDZMXZyRFi-itica3TSGmGikwnZ0ZSxYBIUxeBevtPDq9E9y4MGkqtBMBwtSw8zZj-d-Fjek-AfYzS9bsKqJexzw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=uPq2JBIXdvfkCF3RSLXe6Fo6GIZO52cmkzfOQFJog4ES3cZNWIwWv2c8RhKcIAn0QHcwwDRGGgTaopnwojk_zvlFtYbzEWxcSHyykDSN31a4K7aMHJznRVyPUpNdVDydeqz10qEoEbxTgiuADssS3yB0EaKpp8XUR2zJ5Y09MSnvsn-YdEbh_PjZnOR9k4aUDvL5B6Rd5F7D3gYlTCE08krsdrnjT_JRwZK_Qa_UIX-bN2xswk9SSzgCZtJSnjBipyOCtqhAFuwgdy7lXlEBVC87_3BRYjRCaf93sjhbk_XC5b6sFUS9HS100hf7CxTmNDAP2fxL_6GxHZcsWDUtuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=uPq2JBIXdvfkCF3RSLXe6Fo6GIZO52cmkzfOQFJog4ES3cZNWIwWv2c8RhKcIAn0QHcwwDRGGgTaopnwojk_zvlFtYbzEWxcSHyykDSN31a4K7aMHJznRVyPUpNdVDydeqz10qEoEbxTgiuADssS3yB0EaKpp8XUR2zJ5Y09MSnvsn-YdEbh_PjZnOR9k4aUDvL5B6Rd5F7D3gYlTCE08krsdrnjT_JRwZK_Qa_UIX-bN2xswk9SSzgCZtJSnjBipyOCtqhAFuwgdy7lXlEBVC87_3BRYjRCaf93sjhbk_XC5b6sFUS9HS100hf7CxTmNDAP2fxL_6GxHZcsWDUtuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqn-CYpTYwgOXahgXS6-h5UTWISlqLln-xJE-xJYJi-IuLFJ66lJnGm7T1DcdUCEdBqWuhTccdx7Nzv60hJsztyV88NpSUZZHKU6X-82CfXe8XnD0i06DYB7F3TllhYxY2Xl-a-cfGcCgDkbsKPka2aaG4oB7i2d31UzqfQMOXZs8DZ37u31uFuda_f5bYHtH5FokzQIgXk4rfo6df7HZVGWsAG2UWCpZpWBN8QPrpz-pIsre4XE9gY40hmr-nr-bzKqDE8hs_nHQN0h-bXqXTAgHWNVwBTwaPUPswwDMVtQn8JZ2qoFbXUGREKAL8BXp2rjfD95COoCaHp77kSp7Kps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqn-CYpTYwgOXahgXS6-h5UTWISlqLln-xJE-xJYJi-IuLFJ66lJnGm7T1DcdUCEdBqWuhTccdx7Nzv60hJsztyV88NpSUZZHKU6X-82CfXe8XnD0i06DYB7F3TllhYxY2Xl-a-cfGcCgDkbsKPka2aaG4oB7i2d31UzqfQMOXZs8DZ37u31uFuda_f5bYHtH5FokzQIgXk4rfo6df7HZVGWsAG2UWCpZpWBN8QPrpz-pIsre4XE9gY40hmr-nr-bzKqDE8hs_nHQN0h-bXqXTAgHWNVwBTwaPUPswwDMVtQn8JZ2qoFbXUGREKAL8BXp2rjfD95COoCaHp77kSp7Kps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwoaOdeFQk6BL_bbdyb6BzuVmgkjcPu8XbmtUL3vnvFJO0dydgJzhg8icBvp_cQAaXn4t7gbNF7udXqq31Q1bK0RDPiTjDVFzrGv6q7MIXNKbioQ5Y2ngOPftPBXYJit6ZZ0SjzX5mr80awnWpsV4diBkjz8Oc7Sv_4ejRaD2Y1PAKAYOYTQkmN0oaBM5GoK5QymzL2AV20wnIvnd65m12qzUVRFrNZKxa0n7LV5kFXb-de5nsE-65V0hnUMLjm-vYtgqLZohQrxXQ-EZVgc4dy12cjahnlA8nQHlai6wZ_1bkDdxCXMz935zGur3UpqF9767x-1FQpQmihryed4HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=FniVrWdkOc97qU2FxI_CBB-t8_k_6GYKhOxszCNhoq2r6PdOhffGy-JJRCk6biBU6MQZtWlgxU4X03t5Ij2WtuEnoVCl2bei-rTMRIIW9NT4zBV3ztQId1aCPK7JWqPaRbm2-ZukgDpooI7Yn3xXzFV71vvV_Hb1fvYQ6dD7bQE2sZ2BbkzzE6yB7KVevDoDsCsTPJPenKzEqxns79jd_2HrhQ25BLpQ2cTFsMJt6J6HpTV4BejEQPItWOoSyr-S48sjxWGjY-MeOg3gCJDjeXxNG42HFPuhR1m4KaT96t-zhOVyx0_53p5yAEHyGyR-9jaw9aqoa9O2Hqv1IxCwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=FniVrWdkOc97qU2FxI_CBB-t8_k_6GYKhOxszCNhoq2r6PdOhffGy-JJRCk6biBU6MQZtWlgxU4X03t5Ij2WtuEnoVCl2bei-rTMRIIW9NT4zBV3ztQId1aCPK7JWqPaRbm2-ZukgDpooI7Yn3xXzFV71vvV_Hb1fvYQ6dD7bQE2sZ2BbkzzE6yB7KVevDoDsCsTPJPenKzEqxns79jd_2HrhQ25BLpQ2cTFsMJt6J6HpTV4BejEQPItWOoSyr-S48sjxWGjY-MeOg3gCJDjeXxNG42HFPuhR1m4KaT96t-zhOVyx0_53p5yAEHyGyR-9jaw9aqoa9O2Hqv1IxCwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=XDoTjkh2a4V1h1hQ1q4pzEMGZ1sBMSOeGh_i6P8rj6Wzpzh710l3TXYTeTyLAWuCtB1uP9wihhfGxKAylDFOHFvHkG7gItKHG0bXYyXToX9MfU1hbh-fpkg9__spU2AgmVaCdCXZ76VlNZ2GNWKfRNmMqTO7eWdLWW4CXiiRW_R-3-rHtAcS7RKqnOWcpR8h4OrHvm-SRxsUDAr_FLjYSG14WoGi_LxTJMCdhZ2kdQfcS_MdB2hHJsq-tT5BI3FLQaq_d1r2_OQAQip88bYuTTt5LYcWeqsOdSKCmLaXuiehxtYVONize85OykSGLLRSwbkbgfbKxd6CtSQHQkOS9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=XDoTjkh2a4V1h1hQ1q4pzEMGZ1sBMSOeGh_i6P8rj6Wzpzh710l3TXYTeTyLAWuCtB1uP9wihhfGxKAylDFOHFvHkG7gItKHG0bXYyXToX9MfU1hbh-fpkg9__spU2AgmVaCdCXZ76VlNZ2GNWKfRNmMqTO7eWdLWW4CXiiRW_R-3-rHtAcS7RKqnOWcpR8h4OrHvm-SRxsUDAr_FLjYSG14WoGi_LxTJMCdhZ2kdQfcS_MdB2hHJsq-tT5BI3FLQaq_d1r2_OQAQip88bYuTTt5LYcWeqsOdSKCmLaXuiehxtYVONize85OykSGLLRSwbkbgfbKxd6CtSQHQkOS9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6cAG5lDdNUsdsoYySDe3Xpsq5q_IlLU2c3IIPyCbojbipyxqSwcBWwZ8W-tnxzaDTnbMrQa1t5APM6ugi9Y2dwxj5Wf0DTI0WqdBRZqWwsk8R_c7u7rgSjorfvwXeHYK57t03aoRiERUlBVEhBrQQmoghR4XYhFVdwf9rvWxGEcGbPonTM3sHHzqgHUoNGWmP-nnHhhTQ2osb8NmKkCt7Z7WwVkHd4dGMgZU7QufkR5HdZp9nCpDG0z2Pr8m3UCrypo6Wrf070o-PssQqc0imDu5fK5LeBt0oWmCJaKzELGJAJtk4G27MXAsI1dB1GoA8Qd9_PVc7D4i0we4q3uIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=apmzTg28OHnq0-ODzmTek9EwQIS-rywU_8MQJY50rRup9m2Bf4akAFI1iQmtz1oi7Ve33cbQsV-vY2V791RYWw7HAoxOzVbaolIbklGka9MDMnFKOC9kKBxwBl5T9TjFQVTSwUovhuPc0jhhXlKXVOSd3bH4SiJ2Yee0nXwncgt4dl47y5xL6AZUPZh9O7VV4ZEYwjx4T4JmCoIXyc4F_W9OOIZCy3VLrNB6RTT2Fiik33uUcBi2ZDUye2Jilsrp4cNFHjLMxTYaMVrMHuLDD6OQqpK9QproFFycZOsmcPUS_PJrX7LkywGfcU5zXG1LQUaT1-mBDkLocRP1W7lqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=apmzTg28OHnq0-ODzmTek9EwQIS-rywU_8MQJY50rRup9m2Bf4akAFI1iQmtz1oi7Ve33cbQsV-vY2V791RYWw7HAoxOzVbaolIbklGka9MDMnFKOC9kKBxwBl5T9TjFQVTSwUovhuPc0jhhXlKXVOSd3bH4SiJ2Yee0nXwncgt4dl47y5xL6AZUPZh9O7VV4ZEYwjx4T4JmCoIXyc4F_W9OOIZCy3VLrNB6RTT2Fiik33uUcBi2ZDUye2Jilsrp4cNFHjLMxTYaMVrMHuLDD6OQqpK9QproFFycZOsmcPUS_PJrX7LkywGfcU5zXG1LQUaT1-mBDkLocRP1W7lqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=dqf46zgER-ylkXXZhD1zNi1OWRm0PzsMZBVUiZcvzl9nPqqw-1H_PmIv4TVyajKffP6Vvfl3Wh4d3EByjv9mmfAiWqFfWu36kudJC1d02p8uHRokQMHefeLh_dhVgcjZKQKXMqhwTGdVACB3jnmW0WTfYTOOiSST95tWVvuP6IY7yETBKQSZUgkMOVafwwNh4Ergmg39R_RVNsdtE9g6DbVNwiUAK558UMV6WpE4V04nAKPotc6MWd0FMl7tFn6AvtXQD40oJ0Cx3VwP6FfwQI8RBVhX9Mgdl_V2Iz7Uxn0AJRszzU5w8J1YJx5GmNsytXdYrQhq_6uFbDJbrtKR5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=dqf46zgER-ylkXXZhD1zNi1OWRm0PzsMZBVUiZcvzl9nPqqw-1H_PmIv4TVyajKffP6Vvfl3Wh4d3EByjv9mmfAiWqFfWu36kudJC1d02p8uHRokQMHefeLh_dhVgcjZKQKXMqhwTGdVACB3jnmW0WTfYTOOiSST95tWVvuP6IY7yETBKQSZUgkMOVafwwNh4Ergmg39R_RVNsdtE9g6DbVNwiUAK558UMV6WpE4V04nAKPotc6MWd0FMl7tFn6AvtXQD40oJ0Cx3VwP6FfwQI8RBVhX9Mgdl_V2Iz7Uxn0AJRszzU5w8J1YJx5GmNsytXdYrQhq_6uFbDJbrtKR5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=YfrpU5_uCJcouarQzgYgHq5Z16HiL5Glzr-N3W4Qf-f_HBxy-rYpI_PJ3hohUxZdGvfVuoOcxY_ztX4hRekIE1zkt0RvPyIxtDi5j5X_s54uAdadjekFrqGi_usNTwQcc6Hluvn1cZ5EmFtLl1fJO2ehiHyehos-TDdZgYjkLS5Qb6SjbqKTvhmgwg1M-LLTM-kVjn301WaVCEhQczqN-Goz8oxpjJDMlbqaKUO2PH3RHRWzS-s1JqW4T4sDsbeuQBdVQ3AsptVq99clAJtXd3m243PhMHrN6eGF6oSlFb1HqzwTuyrP4b8TCgpJdPhS31drwHsa8hKEaaC339nzfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=YfrpU5_uCJcouarQzgYgHq5Z16HiL5Glzr-N3W4Qf-f_HBxy-rYpI_PJ3hohUxZdGvfVuoOcxY_ztX4hRekIE1zkt0RvPyIxtDi5j5X_s54uAdadjekFrqGi_usNTwQcc6Hluvn1cZ5EmFtLl1fJO2ehiHyehos-TDdZgYjkLS5Qb6SjbqKTvhmgwg1M-LLTM-kVjn301WaVCEhQczqN-Goz8oxpjJDMlbqaKUO2PH3RHRWzS-s1JqW4T4sDsbeuQBdVQ3AsptVq99clAJtXd3m243PhMHrN6eGF6oSlFb1HqzwTuyrP4b8TCgpJdPhS31drwHsa8hKEaaC339nzfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=W9mBYyi_D6bW7k2VwPsk4C0vERcLbdZu0Mer0ocATW_wObOU69kVVI1yyfFIjSd_26a2ujLdbELoh1RWT0y3WfNPMVE8GZ2HCYg5Wjm3uIZbbcLFPLCO9NIU5HRRp6CooqsF8O4bWb9pqs6f6Lboi8G8ss0rmMIMqUfcx_kI5DGhw1k1G0wDPwQS_tv-sP2wTx2yfMfunZiYlXe6YL__-gR9oZtw5s8qEcmZTOu0H3XO69kLZdC8BfLiGcjs5cQ8j9rDsJazt3QwjfcmXFMUpkQpEGE3bSzYEZMI6Q1geNEFR2b0s0Xn7Nm2tlkZy2CwCuAxFHjTibFbgXbK25Jm1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=W9mBYyi_D6bW7k2VwPsk4C0vERcLbdZu0Mer0ocATW_wObOU69kVVI1yyfFIjSd_26a2ujLdbELoh1RWT0y3WfNPMVE8GZ2HCYg5Wjm3uIZbbcLFPLCO9NIU5HRRp6CooqsF8O4bWb9pqs6f6Lboi8G8ss0rmMIMqUfcx_kI5DGhw1k1G0wDPwQS_tv-sP2wTx2yfMfunZiYlXe6YL__-gR9oZtw5s8qEcmZTOu0H3XO69kLZdC8BfLiGcjs5cQ8j9rDsJazt3QwjfcmXFMUpkQpEGE3bSzYEZMI6Q1geNEFR2b0s0Xn7Nm2tlkZy2CwCuAxFHjTibFbgXbK25Jm1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=buPZRGuufW6fVCi0_uiWJm6Ls9xMqZMnw6hDPp8UzIKj98OpeEqO1G67PDyWjEKXUjxQdIx3GWFdVmDXwunF0Fu9rhvrYsXfhXZuCtlX4TMwbTrzP1eE-hjGvBM5A5eScjwiYz2uosSq_weQbtHHxprB-RH5ubXrmhdzhMc-CXjLewSiOSGfxqI1_npJBT4CeqrYsMX2vdTjRYaGZJ6ogpk9_VNGTVBYkjbmuDhbrQoKkfjuufrF-nQ2sctdLT7d6L4YIelD8O3szKSV_PhKqtGH25gfiXURH9N-u-Dxg6J1oSCYf8rg3AeJbM5JjZY_MbdVz2gv5bAP-W_6G6a6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=buPZRGuufW6fVCi0_uiWJm6Ls9xMqZMnw6hDPp8UzIKj98OpeEqO1G67PDyWjEKXUjxQdIx3GWFdVmDXwunF0Fu9rhvrYsXfhXZuCtlX4TMwbTrzP1eE-hjGvBM5A5eScjwiYz2uosSq_weQbtHHxprB-RH5ubXrmhdzhMc-CXjLewSiOSGfxqI1_npJBT4CeqrYsMX2vdTjRYaGZJ6ogpk9_VNGTVBYkjbmuDhbrQoKkfjuufrF-nQ2sctdLT7d6L4YIelD8O3szKSV_PhKqtGH25gfiXURH9N-u-Dxg6J1oSCYf8rg3AeJbM5JjZY_MbdVz2gv5bAP-W_6G6a6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF49rMgn-PUPo-ROCmoIWMbEk8pMnVC6BawDBPJEWcRCsvWRhkj16W2T79PB9kWc2zNiL-vkEqkWAoc3YPnkUmhlTD5VCQHO2Fvfj9Xlh8j_2I3pgYIS45x2ALeUqhhNDiNgEJwSUCqXmsBt0ABh0ICbSSsiSMOK-iYsFDGoRgMM6kGFInF4XZehpsLOVKG3sJNLQPATB7h2NCeANfY6qVZt0Nbp7sShBNeWFmdyIdSda11dt6WELG6YJuZgOTRwt8iLMrduxxm0uYHERTH33UUyXbVwEUADqKyx4aHcECRErWtFZvr0Iubuez_q18O7HjesmQsyUEou-1sXRUkjDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9JUY82GfS9oaBK-_NNAj8ie7maO5ubW2Zh6vBYmwfCZVvyCOJ1_sq9JVaGVRiFXLKEfVZPZdM4PQsDVDHqI5A9NY9XsSxVbQv7e66-qaeiamS-CRac-SZMmy9sbZ4uZPcGvM14OjRU22OKErKeT22e8t1YhQ8m8QwF5E4Mq4yCju5Srx-HjNzI-cXIpeDTW642DHrgCcoDtZmEL-8irTSQ1zwCOY28LA2kUYwZqiYkJoH0q54k7jnM375f7hg7cvq1o-CUbe13sfyzjc6BkIlmoXm-fE4tJ2mnKOszILu5mUCLgy0esVBVJ80dnek6faCaDIwSKhZtYaZ5KJqGoeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQeFF1uNS8zh3ZDN7LOdK8uPgltjH3Nbc66aTI-bHohJwI7m3MLHFqkvW1_ZdP-PmutMHgjQjqek1hx_vznQaCrOTdDf-5IIfuiinOWQW29viFD4LadAbGRJfM3aHajJ_C6L5mEXZzmj3ue2o93UuDgTjnJFDcgkCtgsVkZ-U37kBdSxqVBzcSMgJ7wCmf1SCL_D3UsXkvYnwWrA3DsNcgvkzlfKAUmHijAlcrPfucgRZoeabqk1C4noKdr6BRklLwrzr7SFEHyMKuFZ0ye7HrF8XaPvLB_D2KL8zGwRFtRIS5CTCSuGxcpQFrensheX6xpeol5wqVgo5C9nn6jbYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=VYIp653T1kFmipqp3Ca2eRkVwrAOgnQ5T1L4aut9e_0cB4u8_UtDe81S52T9Wch241nMjggqAKiRriZ_wRsuXTaq5_4hpbdS8WXjdNFYzywYQLl7sU2luHcQCVDiS2TpEo30EvYuxr17sV-xBJ1KsCWl-nAG4NVstybRvuuLwFf9KCtMiuOneLHhwiRW_VdF1jXtrzwPO4pkwSjfBb-twB-PqCjgexXJ1HZi_-KFt3EOHf_fMij-FXh3kzsTIiqzFNCgXaH6S7hiaDga3EZSTdsJzQTdut-9BgviEYg_8c7eDnsxgNuu7HZOpLS-P21E4b7W7mOK8KefZANfcxFNNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=VYIp653T1kFmipqp3Ca2eRkVwrAOgnQ5T1L4aut9e_0cB4u8_UtDe81S52T9Wch241nMjggqAKiRriZ_wRsuXTaq5_4hpbdS8WXjdNFYzywYQLl7sU2luHcQCVDiS2TpEo30EvYuxr17sV-xBJ1KsCWl-nAG4NVstybRvuuLwFf9KCtMiuOneLHhwiRW_VdF1jXtrzwPO4pkwSjfBb-twB-PqCjgexXJ1HZi_-KFt3EOHf_fMij-FXh3kzsTIiqzFNCgXaH6S7hiaDga3EZSTdsJzQTdut-9BgviEYg_8c7eDnsxgNuu7HZOpLS-P21E4b7W7mOK8KefZANfcxFNNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYWk_WUQY33IqWiljuMmXfThbq0HCUrSLkuCu4VQth0EXEN_AonPrvbFENv85jC-Dj68bmQBAf9ryKFFs_CGabBU1hObFEBPOfd_qPN0298JbqSYRw63oMONDCYglXZPnLjS8ybu3NFXvtftywFY9T8J4aDmnDSFPP-QoiQftq8qMC6BFDugIOM6repRT9P7CwSQFIANShnuwNXFxZTkrlJlo9BD_MTyzbKvscAUjFES6GpewgZCwKG40sd-LXI85TdJeBD8B-crR5XMyxB0CEqZho7PQ9JmHvDBoU9uSLhfVXYlClCXArMfqq8ne3n5992qT1NsoXPuq9PFwo-UeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
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
