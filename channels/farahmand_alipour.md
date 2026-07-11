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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 14:08:51</div>
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
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHyP78d_fSmY-vAEqFik2l7ZlkGJy21Sx5I5dXjWixnIxpRpKMQdGkAI1Oq1KSAenwWGwTeB-J37Ym_eptTW1CdqlhbHYgkJxls9JRsQ6XtTkUONkJqS4JY2SPk50aB4rZOLXPUJiFVeAy3u1w6TP0mONF6NlH32w-dKUTKJRoz7VaBhNN7Z95b8cIM9PlEwtvH-zGzX4l1FtoDauqlw_SNW_Xu1nKSHmCoNkqm82SUg5FXs1X_dz-73zty4MuzmLJ-735vEf_LQIWyQ50EBzG63ad77roh1KcQEy0tAt6VCjwrdaVW1OKXmh-XXe-AltoS88ELnyqYCKtTLo7lkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFoTgLRG-08-wXkVfnmUjpyU85d5MEOPeSE2RXukUJ7gcjmFTYlZCb_kpnQL7ZIcAAM_lDv_J4qZLl0hoiuQRaoKA_6j-aoodXfesfc3KLW2-ibWZjxvxqxsCsKOE-w13vSFR6YCpn74DYo1NOBBYyEvAsrIYpZHslnt5ahw7Y8rBD5zD72zEjJb8Xbr82oFCT3fbG_O9-gKukh3C2YomWyaoxAn9HMpLntkpivRZrpZ4r0DzEYp8eqAocUxAJO47HRnA1D8xjLyMZVi-YwcsKo3Qk76hvz83eeZEW9VoL3t6eBs0cX36qSbGuiRA1OhvmzravFHMOyi9dx-QJrwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6fj-XikOE_vV6gn_Bc8O6-xIM4wgXc4YypxLCBQshzeZI2ex4bJps45gE5IffGwgyOcFmOIBXpQ5LzCUMaN_tBTveENWfWCKP8xENhazzUOnaFAp2M-41EK7Ymex4ZhS70FmJAmyGgh9BYHdlF6czYGHLcTQPXfB5Pl3iD77I8DjDXJa0sUIEh6zuEi1VR39aXBilQoalJgeV9tVniQdu1Klpw0ZHKxsgfSfFTz0JXsGf25mcyADsfQjrHKuvlh0iIPGCR6LoO9Jd48T7nKZvec_4o_-CsQq9qSzSvN6_jHrdi6Ysi5U9_kDIWzg08jSHPScvB1Yh7KR2t3-wfS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbIJyOE2Zg99a7z3TD5mDWj0vjc1vH4vH6eeDCZB033bHtcto7zbvY8OM41MekdSJL9DlcS9mLECr4XoRiKdft09qQFx0vnI8Uf4DSB9UJ5SLtKNYr4kzEbFsDroDdylLGJ1uLB_MRRgKpUuLhaWn329PoFDM2Mf7VIe_Vfs2tbR3FlpSShbyJ6hYHVPN45B959Ufyq7LeVRhGgU4i9RBjDSuvUrTRx3kAfK39tQMR-B3y8NO69Z17tPQoOft3RC91injyqPAcnU69MuP_c5i290F9K3QcyL0s-jszxBquiXLylYWfTy2J4tucAQBOGLSqhVQS5QAUus7_jHfnFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBCdTL9seDcNwGsIb89YYMmUWZ75YhupG5WpItG-REVUvZfiD6KHiROnXkLn4fzdNEvQCBsplLIerYuH0UMUBEtMsezM3MC7ZKK7Py0YFkm2H0O6mZei_Fnzbygt7tAnrp_QgM6h59w8uxsGJIyNVQN0aLBYMYZwuWWVtE_nnIqjCdwrYgb8nyJ4K2r6_6FmvF1cFmuGuqTGjxgGNBAjAkenwQxu9CHL-SNdywTVANS_otcnr7RB-hd3qv4e8yGeMKp9oah80UsGtFRxbWjhdqYY3e5LcKoObVpckCAzAsFgLiWr1fFP9YOF9Blgz6KLpZDuv4UTBUShsOAstb-pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_jklWp-P3SyRXbm4_EDnMya7QubfMI49g1j4w_VhiPn-iZO2Evl0qL-0_yfAfFGW06qtFJ0UHnNf8VNKezps_esDctb0ISCH2P6bquT2fhd2L-LWktS049d0km2_qfc_tzlCR9l4PnCDawud2NIK3WyD1SKzbAZDNNSsI9Ag2I4XDPwulWsAhcmD5ckwtPta7cd4Q_2LgsjjzJuSBgaE4NfL6ji8a_T2wKx0RQoUsLXHxU_QD0i-XsiaHSvD88FEIKUiIeua4WC6dHLfzg3ljE_VPOoMVDG_dxu9S4sK-nc3_VHIwtLtU2D0qQOoBR2AhqMam6Ajzxy-v-rz5Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLFj6blG066qOc9Vz59KMvvnEt9kXhpJ-qtpAmFfW5ICohqG4FNQbWoELS85GqFKPesMMQ0oIfeZTJVY-UBuixdjzb57WF9FRUwO7fSY_zE_YSTtvWkrwiIUm2vO2p_7aXcYiUh9MxrcFc9j22DyifsmU4IGvvMZCwovXGmVQUWCILGwMwwid2CfDJ8gyH-a898QpObWojN6z8_9nSXZslXvmd3cLOi3Mv1Tyvs1VE5qQFTsUJnUtIgorLz8krnFxK_6LS-3AeLXwgACCRvbgX0dymYpAbeS0kksqNXta6BKMCcSOREawZwACz_9ToLVmNrpjPs21FyGGKWgGaYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW3Y8wkErEwjwhOu146AJeeXna-1_Q0yQHyVoQUogvuEw84IQQWdhgrcwU80wv9tXG-1-1jTExHEOTwqgh0A15l5iYi9CWoppsIWSS_H_9MqlPO-ExhLP2LqfKuW7q3xDK4o2mdX_UoqYv7uPLz_u6ilcSEtzGMwSEIrDajTgLwW-XHDpJZvpULYX9Nmzv8qJtpy9PZuvcubBZXBTiJ92E6mS6ggwrjB_PG7OV5UKWrXZQCzHSFlIUOOE6JmN3GhWMWGj7vpEg5yt4XNt_lIBZmLVrNJDyAXQONcTbZ5wKvksbzWFVuWgRJTiWIsxnT8K7PmpZw3v0Ako2lvBbMjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftoT0vHGzBnDY_XOgrbM999A50vu0U3HCEN_VD19MRDlKDrZhadB94T8TrzcNVRt85obQoUoJlZuJK3fO9oEmw4y29FrXCXwTbD_uGmPLdIeQCkoycDhgOUajra1PbFAt9VMcv8n_IHQ3SHNWnGxGXjVLHBUO55RjZzf5ftn_evCkOxFDKjzuTt0TUvZjEPYx3OWH9NLgMRb4TmkwxQfeP7eyvtHE6V5ul4OKgv-3bLHn9tJpWBBpZHnTHEQ2wJppZGzm0FF5ydGr_3tDiyBeExW8qgAtWyFe2c8Um8pWnXv316Y1cQGaND5plapVjmBIXdW2g2xBfNyjqXDsYpiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBuHBmINNg4wiMez3F-XCUwCh4n-_2LP_GWmwRlvnv3TFyB8RtDkVdxb-Zy4nGNuP-wdA10DlFbZHZ3V7DqWPXgM6jJi_nBBZnfe_VWYMtMZVTwM3Gkw2PHhpNwx5Q94VeSu6SgJCCxIPXPNGYI1f0EMhCXR44ZpGDsZeziddZoIIatPBWIGUFywliuc8Ua_-t0R8rx1NXDW570NgtDN5LEjSln8aVO5c1ZPYPUopYboMTfzkUbascvXkreIKjppVfb7XzKleq3GoqDFwbxxxuEigMvroiMAWjN6zjiNAYNdzrFWaDGyALxHEazfkLoMoyO8bvmEuGzgrWQgGpGQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=vGs7RsfNxR22GD97fkPR6oV-JeuIzROgNQ2Xubn96UMX0osoRKNKMkOgX76c_S6DRKe1SAiCjHflNEp2TLA28roNkszm5-j0CW-8E-SpEyBBawsWhrOoKlXVq93EY31DYtZ4kA4DnTFaP-K_RkwAut-3A4ovF4HWEhdfKnP6MGltBjtwLLXApUdPbAuRPLncOPSmWJr1onX005Nuafa6CeodhzLZ39X3_zXeyO-fUj4vwB30esGmRfQAwJQOA6YHC4DSjGW9rilSd579fr0IIU5FXy7pvb6TyMyL7wJfRfa0pg62BKFAB9Z6oAoVbfr_Ged1zKdBnIdkeipBfa0EFIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=vGs7RsfNxR22GD97fkPR6oV-JeuIzROgNQ2Xubn96UMX0osoRKNKMkOgX76c_S6DRKe1SAiCjHflNEp2TLA28roNkszm5-j0CW-8E-SpEyBBawsWhrOoKlXVq93EY31DYtZ4kA4DnTFaP-K_RkwAut-3A4ovF4HWEhdfKnP6MGltBjtwLLXApUdPbAuRPLncOPSmWJr1onX005Nuafa6CeodhzLZ39X3_zXeyO-fUj4vwB30esGmRfQAwJQOA6YHC4DSjGW9rilSd579fr0IIU5FXy7pvb6TyMyL7wJfRfa0pg62BKFAB9Z6oAoVbfr_Ged1zKdBnIdkeipBfa0EFIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLCKaWezzyHSKORv3MC7EKmc4haiNX757Zw7SO7A3uvzi3uxNn1LtSepcRMgKbfZ8NYL2Wh94Ejf1MA6apDzwrrpqC1ZrI0yehSgGkO7fOjXOcg-xb1pdHULhGBotwmon046Znsz4f-6mvJPfs0o148j9pq3yr76997RzKvUlbDT5f1xH4hdqb_dO2XjLNswxuB0dntGU9IJnfGcVciyeheXzTc4BsUUgu97xkDmPohqsPAV2bQUry5PmpyS4en1c0t2m1wDRFJsWD90U3XcLGHTGEBENedOS2HzigXKiwRqAr7oNIH3imylijf6t_tTg73aQl5hmLqz0JVM4WoXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJAJIvahIHZDXX138zP55VmS6chQpUnewVOL-51MhqwV8F1kiaVneYv9jhm-E8XbHe8CLMEH8SqEtDs--EXJSxwwxA4_AE8sBGt0j6mnPr7qEatRxGJJg7mDUGHAPR-kOZQI73VVX-xDbZN1nJcT-8GPlB6Qq5vn7-jr0S4s6FQEYeo28PJDwKdH1f7JerMN3Run0AsySuwImI-GrKBHrcN8yP4qMtrfFvr5kU8ONUcAya0UpeJQJWrMaIu_-u_ZWMGjngxWdwO5L9eyPtpOLjyg90rq64fFXhG0HwL2R6LLPT7Ope8t4cuBz3_Xyp3eAes83j6wuA991m36I5X5bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi7CjSg9YSCrbgGdPkcay04_U6jM3eyGe1yzv9ylk0ykllHXir4IneNM1E6Lwbo8GU0a3qJN2IWEoGiJnXnJJtwwLTT3jMTKW-W5AYuBuy1LoxgKBtuDcex8KsZu7K_BuABVE8wgFGm4Ldk-Pq1y-i4VfGjgBCoIdHB-IGdkOWJSrgFbxch8XTn6dekqF8D3srkysPPtel5r3zKrKp_kkIp1bj27R7Z3MX2XepE2AmaAlIe6Usaah8JQT4LZFbW5LGxOxo3TCVUwBIYNrozGQIYZipObMAr6VPobAQzsPGZrxHjTPPgKGYo9TBevDDL9-LVD4czbOdp9504a8BavrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177Fqlqa9L-w-zpdL-kowNTV-dClAkyLNXmv_gemFNEe3mpBQ3M5195qOPIhhNwY1rrMYGYAHkbR8yQr-BMsRt9Rc09fL4a0-ZcHlRB9T2Dx3TWwMBo8dyznAiiku4H6XZE0DkuVP0PSwuHPvekiqhFzsggbqWzv9AJYU46n0-xKAx1weuZ67HaNnJo33bjmJWOqED8Q_nx5u9Io7WhPv92tBDwEkbylw_A2HmZMy3C9VvFMaKPqSSHLMM_0D2Uh_ATU1EFH8hUMCX4U1SN9IYFcVmUsaV_s8FcOTM8qgV13aCGafxs7nZ1FYkj_T7wjB7xOcKeyQ4X8GsmsPK_4zqrCX11w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177Fqlqa9L-w-zpdL-kowNTV-dClAkyLNXmv_gemFNEe3mpBQ3M5195qOPIhhNwY1rrMYGYAHkbR8yQr-BMsRt9Rc09fL4a0-ZcHlRB9T2Dx3TWwMBo8dyznAiiku4H6XZE0DkuVP0PSwuHPvekiqhFzsggbqWzv9AJYU46n0-xKAx1weuZ67HaNnJo33bjmJWOqED8Q_nx5u9Io7WhPv92tBDwEkbylw_A2HmZMy3C9VvFMaKPqSSHLMM_0D2Uh_ATU1EFH8hUMCX4U1SN9IYFcVmUsaV_s8FcOTM8qgV13aCGafxs7nZ1FYkj_T7wjB7xOcKeyQ4X8GsmsPK_4zqrCX11w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=OK-8q400QARTyToZaNuGdlllCrD60xefW1NEspb702nFC_U3jkTvncWfUV8fq9hmvDpn6bXNgEa6kkbgIFsWFH6Co2QZrNrmgbp9hzUIMczCSfQrxLTDGu0IZw5VIqO1RB_jS4bmsrWGUYRu04UXhR-M36C0WLxpwBwvTAWZY4c6XFiPn_rJuGiJ6ZgLA7EjtgbMWwBZk15ezTUUoPEg4MvN2HaN4PtDR-DoPjDwjdU6ps7qLtKvU81iHhf0LSO0_YNTzwwYowqM13dKWSu5GQVeyq7xiNdwqfvHaqfDhZtEv2F1DzBGIDad1PNBoMkfsWDTwzcy0_qOpq12j9pXYrx4C6WxXq8YJ5Uuxb8D2Bp-Pu2Z1irgPDgd4iOFF0w-FU1WGi7apmOarQJfhUNXFwYwBxpCW9V0tuQcZMQLInFl54hShjTgd6z9QNSBZ6roqW2kRM8sBDhX_qQVnba63kgNfLFyBYCAuHPUa2O_xshQJNaWwFh35cQ63_Wy0iesc_hbWPDwpmAp1lruIoWRdvLhnNm5-wAEECVn-gtLLQw0_LqeYTx7pOQb4htgHtS8BhzQapFePONSqRaHOHImH2OVZ2SwF9lCXE8ACdmg6V97E_1FUdJ77hSi7ooaJ319_8eDg1lp2B2k9ID6FD28Xr6KeCdVaa_aBL8pySqARCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=OK-8q400QARTyToZaNuGdlllCrD60xefW1NEspb702nFC_U3jkTvncWfUV8fq9hmvDpn6bXNgEa6kkbgIFsWFH6Co2QZrNrmgbp9hzUIMczCSfQrxLTDGu0IZw5VIqO1RB_jS4bmsrWGUYRu04UXhR-M36C0WLxpwBwvTAWZY4c6XFiPn_rJuGiJ6ZgLA7EjtgbMWwBZk15ezTUUoPEg4MvN2HaN4PtDR-DoPjDwjdU6ps7qLtKvU81iHhf0LSO0_YNTzwwYowqM13dKWSu5GQVeyq7xiNdwqfvHaqfDhZtEv2F1DzBGIDad1PNBoMkfsWDTwzcy0_qOpq12j9pXYrx4C6WxXq8YJ5Uuxb8D2Bp-Pu2Z1irgPDgd4iOFF0w-FU1WGi7apmOarQJfhUNXFwYwBxpCW9V0tuQcZMQLInFl54hShjTgd6z9QNSBZ6roqW2kRM8sBDhX_qQVnba63kgNfLFyBYCAuHPUa2O_xshQJNaWwFh35cQ63_Wy0iesc_hbWPDwpmAp1lruIoWRdvLhnNm5-wAEECVn-gtLLQw0_LqeYTx7pOQb4htgHtS8BhzQapFePONSqRaHOHImH2OVZ2SwF9lCXE8ACdmg6V97E_1FUdJ77hSi7ooaJ319_8eDg1lp2B2k9ID6FD28Xr6KeCdVaa_aBL8pySqARCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD3zsTlodxAHajnasEZG9pgaaGOgz4U8eSbdpM_KzHD0tVEer4qRxBEH1Jl8eoBLf2sE-9zT3LuPFZ8cL-g3ntFc6Xwd0b5dVAJdovb2S0s02K_h20rau3FH3iUWefa-lQf4w2T32CyUaornFFwIK2Cr3HYT6t5dva66TNCoyZTrTophDHWJypAcANaaZbidrYjMMHSiZQLv-9WP3ZyTskCCEPF7H5P-iR8poly8Iu5vR-Zn0OZUtLyNEQ7Nmeh1PlSsczXPMaXLvagh07p3HZjeSW8QjgXvwFImdPL0GPBucoJKhps25Yq9itTxCr5qbfNWlhvucRoAUlMmLZsxEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7-Gsv2T3qZvRihQzvnDjcjbBfLM8cw2lykw_BOH4_0wecxNq6drgdIygEmEXvd7nu3PnXrUmUUR4UIF8wfdDhBHoMAsy49xeQK3bfx6qdjlogs_Vpk5aPXN-QWGwWqGuYHCipKL-Zh3cVok7042xcttFCTIbMtYcuGbmELvjQMjW1ZHs-zML9MS7oJRNctfk9YnV9x5pGSa5Bs9aGHNy5irnnRd-cr9nJ1orzzWQpL1gdhrCjMqhXXCVSTSUsLPoWg7XKzkaSjqcaW36rltPAZfGDvrYcDYilyvkRsu1z10oTAphPmoQJ4KyoDuGEU7C0IwYxiqtXejheL6SUcWng.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=s46H8zlUWvp1GgRrZyL7UZSEp7tGz5_vuvTzrPs8fA5yRqMpSBkqvTp7SGS0IUif9pJ0WMr5zAUzLDncIqBnjXoEBAGKQCJ6sv7Ze0moyArTzlvqctNGcSHSYhKFOUccO2U0X1cr3jewj30HZ6F8H8P20QkXP91lTKeWDQX3n-PSumLTc2vvDlb3pKsVznuwspoNdYxelHm0OBI91a3YUVMp81DxBznsnm5OukZw4D7TKEJC4FppdCGx5G4N3Rba00Gmzc2IVa6TtyW-pErqavXV93N-SYgWOkXjQDlmcKZtgV_DV2qKonONM0yRybHc0Vq6bCOfpTg_VIdsVtJ6GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=s46H8zlUWvp1GgRrZyL7UZSEp7tGz5_vuvTzrPs8fA5yRqMpSBkqvTp7SGS0IUif9pJ0WMr5zAUzLDncIqBnjXoEBAGKQCJ6sv7Ze0moyArTzlvqctNGcSHSYhKFOUccO2U0X1cr3jewj30HZ6F8H8P20QkXP91lTKeWDQX3n-PSumLTc2vvDlb3pKsVznuwspoNdYxelHm0OBI91a3YUVMp81DxBznsnm5OukZw4D7TKEJC4FppdCGx5G4N3Rba00Gmzc2IVa6TtyW-pErqavXV93N-SYgWOkXjQDlmcKZtgV_DV2qKonONM0yRybHc0Vq6bCOfpTg_VIdsVtJ6GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzIlZQl3wbqC_0EmjFh5rWB7LH-jZDZBAYLSNjDbnd79EpKxR9YBFhR41fcpSBSzSJow8CnsWDraTHMHltrYoBUs4zEkE_SY-NugswkGYMbfht-AY1DKReZLCfkL_kuyAvtf3CSyIfA1M0HLgDwvaB_NAjjLsznKXmClauPwLUbtZMT1xqunQqDw1A8eWgJHJ9yGsQ2-k5nWBO0grTwJnVOaHXu0g56PqOOPs4xs_7JQq1-Rvht-PHS7JlQ_L3uCsdh5MHmeH6tuvppo55M94sjsdo9ppd6FytecqdMQrl5EyJtBfUTZdrazzHNUac8g2ycUdyE7oJCCWfATFbkTOQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=nJke9JujDVXtCfOMkpMHvDdP7BmP9SUrzhjM1alMrEodWcwP3TGcDtxoTnJOw9mmTmlRsvRN1L4qlILxZVvRVFUfzv-5gcR3DWV6jufxwrQHNkHGaXDhPN5G3xrCh79BphtZWCL1OACHcSc6Hql5NfG6AkDuuD6-sZazdBbUeCWdhXMjNqSURr5_bmlnyv0b8qCJ3dzpRVDe0A5AtmFraQtpqvX3l7rxrlzEI4I7bsVojWN_BGGtzFX7QU_BoHdShGmwBkq_X2PWGqLHopMml5D-quvqw4Jp48nwVqqoWFb_WTxWl8Tg4mQpiMPSpH7OXTud61LO8FcamjvsW1iKBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=nJke9JujDVXtCfOMkpMHvDdP7BmP9SUrzhjM1alMrEodWcwP3TGcDtxoTnJOw9mmTmlRsvRN1L4qlILxZVvRVFUfzv-5gcR3DWV6jufxwrQHNkHGaXDhPN5G3xrCh79BphtZWCL1OACHcSc6Hql5NfG6AkDuuD6-sZazdBbUeCWdhXMjNqSURr5_bmlnyv0b8qCJ3dzpRVDe0A5AtmFraQtpqvX3l7rxrlzEI4I7bsVojWN_BGGtzFX7QU_BoHdShGmwBkq_X2PWGqLHopMml5D-quvqw4Jp48nwVqqoWFb_WTxWl8Tg4mQpiMPSpH7OXTud61LO8FcamjvsW1iKBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz8TYSwVBMe46E9lxfmhaZnnxQC57_qdjWtBXVGwby6EtOnEgP_LyPzjeJEJMHnd1IF8y9C3jgJ5uZLbyw-fM0Fyv3Gcnv_SXADbY0hqe8SItTaUe9CfPS7ylJF70ozmygzSzGgyXrxpE-cQjZvHMz_0kgMWZUSN8Y8YdODSzPzbVTuoWZvMPHDMeaWXvAnWyqW2jCqywBratd8F1a6dNU6Qh4J8uX4mLgiSXQbvOpi2QU1hPBiJUpH3Cm8uQoUWY8Wcd9daF-AR6socwbpH8jVhZEcH5nnJbbAnzb4sg3KNs7YXBO_0qOlZD323cb-h1dPFEzYH9yC_FOrpqHwCkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzEkWPMcwcPVQJA2oVd5u37r4Oe8RXr4fHQq5L8kaKPezZ5doVDaLjYHTu0XnY8-8rJgx29vBbPU2ukmVSAQq4DqpVtOWR3DWOlZGBFzwqWbzKBvc-U-TConzijbgEzi4GWNRmGCRvWGLLwucCc-O2YlBVK0yd0y1F_KiXEr36Bb3KS6mcTdYxLZSdxpZsQhxe6K7IW6v4FdRt4w_J1EkUC3LzrAsPbuq5_emAn5e2vxGU8hRuaE-jmEoxmQ1qgGuYXEgXh1iW51xCNeutZDemzY4yUvqoGMAv654QzeUCazmreHHVlTV1EnAIjzeCSfZ5mA5qhDUJk9gwgiu02Hdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=QTKp0h9QBYCS6egvj6XsaDeXoaiP2jSXSMrFf2mAdlA97pXlAQ4S39dHpB6akyea6v8XZBpW0wsVqvkleu0ZFVgy_KaZmHtN1yoRd0s2QMa1VP56kUNsDfuHR1IinDhrhHTQ8MnTojMZnd2wS0WxFuoY0NH_GFCYJHNAzTVICgbpPlVMAHAbNDEvBPYGfYZrcbNjZ1LEIz1Br9rDEsJnZPnhsPd-u4FRwVPA4VgSsiPSXITY7_LgMaJz3OTK1wnQnlHSMUzfoeJxVjlVpSv33q4vlGk_XyWMBwuwKV0fB3oc7fqLgEUqHXAittZQvs_kPVCBcpV3EFpFkPifnLNzQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=QTKp0h9QBYCS6egvj6XsaDeXoaiP2jSXSMrFf2mAdlA97pXlAQ4S39dHpB6akyea6v8XZBpW0wsVqvkleu0ZFVgy_KaZmHtN1yoRd0s2QMa1VP56kUNsDfuHR1IinDhrhHTQ8MnTojMZnd2wS0WxFuoY0NH_GFCYJHNAzTVICgbpPlVMAHAbNDEvBPYGfYZrcbNjZ1LEIz1Br9rDEsJnZPnhsPd-u4FRwVPA4VgSsiPSXITY7_LgMaJz3OTK1wnQnlHSMUzfoeJxVjlVpSv33q4vlGk_XyWMBwuwKV0fB3oc7fqLgEUqHXAittZQvs_kPVCBcpV3EFpFkPifnLNzQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=UZc38DZhQbjKQZRikZEyR1LuuIxt1z5vG5JiHps3nc8jdGpPTLjbEyLE1AqCbCkZzmqnkrnnWzAH2wWAz-7lvVWYlsFGe_2kyQBw3dUVJqqEj8soWyFy1VxOsI8cJUoVG6jrJjeDmABeemAFWnZTuB5KXAadGbDFWnBxpcISY-RQBK1ipYR0MvPFBor0p7Ble00zEx-OAYFOcyRrwYXJH4fcMegrZJB7KMyER4NAL3YjazN0Rw_kKxr0wXDxZO4St71ojol-LZgM96pWq1jbRQJaR_ce8M42GWt0Lp6FAcev6kf9PkzA_JSWwnWdHdH3AP3j1MdPXMT330TER2I6Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=UZc38DZhQbjKQZRikZEyR1LuuIxt1z5vG5JiHps3nc8jdGpPTLjbEyLE1AqCbCkZzmqnkrnnWzAH2wWAz-7lvVWYlsFGe_2kyQBw3dUVJqqEj8soWyFy1VxOsI8cJUoVG6jrJjeDmABeemAFWnZTuB5KXAadGbDFWnBxpcISY-RQBK1ipYR0MvPFBor0p7Ble00zEx-OAYFOcyRrwYXJH4fcMegrZJB7KMyER4NAL3YjazN0Rw_kKxr0wXDxZO4St71ojol-LZgM96pWq1jbRQJaR_ce8M42GWt0Lp6FAcev6kf9PkzA_JSWwnWdHdH3AP3j1MdPXMT330TER2I6Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=b6TNQ29JBr-3kxlOs2BkqBpelqNaJlhOlx6X1PWDfmJi32gntgZNLlkDvv8MZ4VlBNhTnAarKTE8tQlcMknWxoJKbkacPMizGVe-q-um3QgrhCkpfRF2oRF6Fnp0asVdwZb94FOIGO3Qdk7nWEAqB5uJabX9ruew3G5obgPOMDr0Zilxgop1A3hnpMHS_ipZX7eAdAIWVTUqTHQcKVys3E3Bh-e03JqUJuCvolqzxPk8KZKRLUI0W6jD92YLboq-O29c5kQvNLsqJDy5qCo85LMYTpfLnnvAFNzuIE_g0hO9eA2sZrFp996_Gl8bspSDCFW0yHg2mdEeJrQfukYspEYMV5SkuG9gF8PUBesP0AJKz9m2BCvSY0a1_MHPTnOukl5Q2tAwJT7odF7vLPvczqSExYgml4BDEFPtaTM2GATxndbf7MNeb-ZvbUkQ3MkvekWaLzBu4wtkeLWyFaoDo0pGf1D8FSPrWLPTG8k2N7FTKbaQEaJlxqo0GmNIHhObvKAKVzgFczZfNJmbo-NsnO05Iyx3GHB_hcw8wkOz_rV_Or4-6Qyuv__RjvoHRENRZtkbzG1ge8A2DORdq4bEDHvbmdomlchnjhgZWhzlioHlzoUzkWBOXzvH9rukWjCNaTtr69KvEaQ5pNynkEti8YcdlTLem6oPMZiI_n8ZgBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=b6TNQ29JBr-3kxlOs2BkqBpelqNaJlhOlx6X1PWDfmJi32gntgZNLlkDvv8MZ4VlBNhTnAarKTE8tQlcMknWxoJKbkacPMizGVe-q-um3QgrhCkpfRF2oRF6Fnp0asVdwZb94FOIGO3Qdk7nWEAqB5uJabX9ruew3G5obgPOMDr0Zilxgop1A3hnpMHS_ipZX7eAdAIWVTUqTHQcKVys3E3Bh-e03JqUJuCvolqzxPk8KZKRLUI0W6jD92YLboq-O29c5kQvNLsqJDy5qCo85LMYTpfLnnvAFNzuIE_g0hO9eA2sZrFp996_Gl8bspSDCFW0yHg2mdEeJrQfukYspEYMV5SkuG9gF8PUBesP0AJKz9m2BCvSY0a1_MHPTnOukl5Q2tAwJT7odF7vLPvczqSExYgml4BDEFPtaTM2GATxndbf7MNeb-ZvbUkQ3MkvekWaLzBu4wtkeLWyFaoDo0pGf1D8FSPrWLPTG8k2N7FTKbaQEaJlxqo0GmNIHhObvKAKVzgFczZfNJmbo-NsnO05Iyx3GHB_hcw8wkOz_rV_Or4-6Qyuv__RjvoHRENRZtkbzG1ge8A2DORdq4bEDHvbmdomlchnjhgZWhzlioHlzoUzkWBOXzvH9rukWjCNaTtr69KvEaQ5pNynkEti8YcdlTLem6oPMZiI_n8ZgBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeUa3eDbzcJj9qRVwQtP9XckujFXF9xbcvM7GtY3XD8hcTsLCOsKh04F4-zUupMPRSgwHqr07HpwUwOdCbXOW9iWSpg56H6kTOQ2CGJjoxCL72WIQmxoqWqxaPpzrPVs4nhj2Gdfyd9hj9TVizsf-L3wG4UzGsNg3nYTITDpAUG12ITeTtDlnkBH21hXZF6hKH_wGYZmjeVs5frc4A8RdxIA1YyFrxDO7PMIPif0cUWBL_O9dEQWGiQPk_7um51tCjGpWM3MG4lmCpf-W350JFwmJqlW8gTp3ieQe5AqW1icrjzm5Td4L7AaOB0G2T28wHlSW9xmU4GOwSdld9YVAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuB-T1rsMBOLfAG5fCenj6SrkShQ3qIRPCwc7vVtmBATpDsV-lVZq3PeZKK9KGRQo6fCMngDpR0k9DqpzJIx4JPqA0SbmTLBAiEjf3MHPi0PdZtZB7yQzVzjTaTQjSHj8eyndiDVj_WyBxqr_66tqrKu_Wx2XKhpXEMC-5qOrcpwPMK4BSMQYSw3E-jMUzD5giabQMwVdRkISyTWsjOuMGS6TTZWc2auMeHSLXhaUZAg744DGdzoOKmI7_b4Yqi6zkWth0IFk2lqC7VTLMm2Mte5H8k_3fik0j_KGh7Vfqm9v4WqDgnsob11gJRHzc94363lPJ8r3LWX7t85FXC2yw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=hNdKF3W1QInFph0Cjao1P4XI3en8pIDzagUHrYfylVbs7UQwJ71nV3kGcygwospwAJQ4y03mjAzTL6XRcq6ffEsoYEzU5Rz356kM-wOfaS_TdGG18cwUJLkGJBgxTsDZLzepAK-twnB1IkOOzmkGyqKKrqenmuwn6ZFyKakiOnKYV6QtgtaGidMlIA3DGXMDzFUfQcMYEoLnQafhKFd1O1zUO-4HMa_j2N6uSe5HjKD_X29ju-Ce_L7z2WVIi2GfM9JW4amom1WJQi1R3zhSv-PWHXZC28qLUEEap_P_wkiUqKAQMNucHY1CHj6DCyEdQWHJYE5HlDiGVn3i66E5hzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=hNdKF3W1QInFph0Cjao1P4XI3en8pIDzagUHrYfylVbs7UQwJ71nV3kGcygwospwAJQ4y03mjAzTL6XRcq6ffEsoYEzU5Rz356kM-wOfaS_TdGG18cwUJLkGJBgxTsDZLzepAK-twnB1IkOOzmkGyqKKrqenmuwn6ZFyKakiOnKYV6QtgtaGidMlIA3DGXMDzFUfQcMYEoLnQafhKFd1O1zUO-4HMa_j2N6uSe5HjKD_X29ju-Ce_L7z2WVIi2GfM9JW4amom1WJQi1R3zhSv-PWHXZC28qLUEEap_P_wkiUqKAQMNucHY1CHj6DCyEdQWHJYE5HlDiGVn3i66E5hzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=hvw5_4KHIbmvgD0F_aKZqUPsOlAAi2Hcynu_bCLFwYf4rIww6BZitdbDnRL6q1mZsDUxSZOt9wmbD5m3ee5Dw0YagDF0brDAku9pwTX6muqu14-XpQyxI44AOPtHSDBMRmLUZEb33SNbM-6zMbAUBnw7YvIhy3lnHD0HDm6NU8MpBPjf2Hb0IilT7kELeKi9yFURF5_BCZcpZLg4EZVjmYY2Z7M9P2cyrSFU8V_keeWiBkDSWLN9dfqzGMPCedIZf8NcwdJDEbaOwoAP2gNiOBVqMyelOHKdTzjrpI1YJzJOpI_e9xr4l6CJW7X6-EWsRPgx-mb-utkZQIyJ1j6BGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=hvw5_4KHIbmvgD0F_aKZqUPsOlAAi2Hcynu_bCLFwYf4rIww6BZitdbDnRL6q1mZsDUxSZOt9wmbD5m3ee5Dw0YagDF0brDAku9pwTX6muqu14-XpQyxI44AOPtHSDBMRmLUZEb33SNbM-6zMbAUBnw7YvIhy3lnHD0HDm6NU8MpBPjf2Hb0IilT7kELeKi9yFURF5_BCZcpZLg4EZVjmYY2Z7M9P2cyrSFU8V_keeWiBkDSWLN9dfqzGMPCedIZf8NcwdJDEbaOwoAP2gNiOBVqMyelOHKdTzjrpI1YJzJOpI_e9xr4l6CJW7X6-EWsRPgx-mb-utkZQIyJ1j6BGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=AT0z9qDWmq8qbByj4Ez08MYYDl-_vgSX8sDB-vg03KxUhU8BlVfOLIxYR7uVhX9B7cP9YDOXUIRdGe5L8nh4TWMvgfTVe6mZZT9CsjwpcYLVuPEkqKSpKRKL4IiweeBGetUsV_2vAyd-x5RbGiHxP-EaSkM2QRbJHFEFgxbHq4eMag6I_3IfHns4xNSoaJbi-VUGbFgTRqFdHSoy8Q1OCTMLKp2Hs_cNe6IP0PQ5VNGpCJm2q1L6sPslwtyTuqSnf3oVSW_bCN2xRrVuKfmvR7EQCavqYGrBs05HIycq3HRRIX4d1ciOyxGwe6HtZ9ysPsOSZYcooJ5bXahPzPI3_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=AT0z9qDWmq8qbByj4Ez08MYYDl-_vgSX8sDB-vg03KxUhU8BlVfOLIxYR7uVhX9B7cP9YDOXUIRdGe5L8nh4TWMvgfTVe6mZZT9CsjwpcYLVuPEkqKSpKRKL4IiweeBGetUsV_2vAyd-x5RbGiHxP-EaSkM2QRbJHFEFgxbHq4eMag6I_3IfHns4xNSoaJbi-VUGbFgTRqFdHSoy8Q1OCTMLKp2Hs_cNe6IP0PQ5VNGpCJm2q1L6sPslwtyTuqSnf3oVSW_bCN2xRrVuKfmvR7EQCavqYGrBs05HIycq3HRRIX4d1ciOyxGwe6HtZ9ysPsOSZYcooJ5bXahPzPI3_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=M4H5frK4wIHV51LbkXrM1ctf4b30n4zNj2Q35C-4cvHuDyxyGj7nVLrdGEwuiB2Z9vRUuy1CMv2WkBT1IgLZdITRkPIVm_ACMWJS32jtFsoOHRxwt4gXL8_TF0lsvI8u3ExZbHre5-YbPZpr6kV6R8ZODLhqXiE9dXFY2x1lpUXKHW3vncyYFXqvZevmmwxYBAheQoKuxfx1eJi5AwWnrxjVQKmtKjPuq8KEOzSuE1iK8GDwaKCISNjo4lqwwl0_t97_LUQn2CTaEJ1VyZh91wHMRenM-x02kV-yMIVmiF5nLX10Lw9Dqhx0dUlWa3X6yGFemPd37gznCuUEBAhQDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=M4H5frK4wIHV51LbkXrM1ctf4b30n4zNj2Q35C-4cvHuDyxyGj7nVLrdGEwuiB2Z9vRUuy1CMv2WkBT1IgLZdITRkPIVm_ACMWJS32jtFsoOHRxwt4gXL8_TF0lsvI8u3ExZbHre5-YbPZpr6kV6R8ZODLhqXiE9dXFY2x1lpUXKHW3vncyYFXqvZevmmwxYBAheQoKuxfx1eJi5AwWnrxjVQKmtKjPuq8KEOzSuE1iK8GDwaKCISNjo4lqwwl0_t97_LUQn2CTaEJ1VyZh91wHMRenM-x02kV-yMIVmiF5nLX10Lw9Dqhx0dUlWa3X6yGFemPd37gznCuUEBAhQDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=i9WDHvqeCSSD-kFc5Pr2cq_gSGaETRFosI72cDvh0XYTEHNXNwyDNJNJqWjWLGvWemNC9dCCGJbPS45FByxezcJ910uwHqXgeIaE9PxldH_4Arf3eogwxDaxiglp93qmU8h4IZSKCTneEavPPxfXANpFyg6uLVpDn3SYWXWx8d3P0dh2ThXS62zKGpOTqwnodFjthCoJ5pZA0W2owVSaPv-4dw9ujlr61mdBc8Vo9gexOlHfTfaW0k-6Y9AxTqVqXqrRJ0N5W_dIAk7gNbcVD6O1Q7PVbVzWZtXwYDe0xw9KoPuocTgunJhK7zBElLBHv4EzGDHeAdV_TnPn9LlykVEgKPI72LFRU-x0M6SPIYe9T0FOLniDO6GAym1uFPO8-RXKyV4oBU2V3zquPx4gtA_XRtRmKvJgK7Q2OGZzL5MOqhkYJeHrvC_eYaAUhMhKUVDnlB-8BoDJUUe-S9McbrAxfbJJa7EEys97GUBjUZf2PK5JqxV12knB2DKcBtOsdSMiCoEOBpKmb5XB5WEm-yf24SQyMe_iW6ipSR_uYvZZhFBp-f6fg_IfKZi-RG5BHC2pTj0Or-698pbjugzyiv9S_1webLEShZfMAt1VVSadOSL14IirhzAlhV0ylvz2x34ntaaEGmv8g5-LxtvYfvV8ooVxvbLbTvnWIDQHA-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=i9WDHvqeCSSD-kFc5Pr2cq_gSGaETRFosI72cDvh0XYTEHNXNwyDNJNJqWjWLGvWemNC9dCCGJbPS45FByxezcJ910uwHqXgeIaE9PxldH_4Arf3eogwxDaxiglp93qmU8h4IZSKCTneEavPPxfXANpFyg6uLVpDn3SYWXWx8d3P0dh2ThXS62zKGpOTqwnodFjthCoJ5pZA0W2owVSaPv-4dw9ujlr61mdBc8Vo9gexOlHfTfaW0k-6Y9AxTqVqXqrRJ0N5W_dIAk7gNbcVD6O1Q7PVbVzWZtXwYDe0xw9KoPuocTgunJhK7zBElLBHv4EzGDHeAdV_TnPn9LlykVEgKPI72LFRU-x0M6SPIYe9T0FOLniDO6GAym1uFPO8-RXKyV4oBU2V3zquPx4gtA_XRtRmKvJgK7Q2OGZzL5MOqhkYJeHrvC_eYaAUhMhKUVDnlB-8BoDJUUe-S9McbrAxfbJJa7EEys97GUBjUZf2PK5JqxV12knB2DKcBtOsdSMiCoEOBpKmb5XB5WEm-yf24SQyMe_iW6ipSR_uYvZZhFBp-f6fg_IfKZi-RG5BHC2pTj0Or-698pbjugzyiv9S_1webLEShZfMAt1VVSadOSL14IirhzAlhV0ylvz2x34ntaaEGmv8g5-LxtvYfvV8ooVxvbLbTvnWIDQHA-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=Iaj1FoNUzIAnrqXxIvuiNE9UvPgDYISl0VI9-5hdkTv59ANDRkHcIURwVnte-SX4iNObmVSGSc1e2Df_DbOGbnbPWEL0ztNvAuz8z_oIsDkLI2AueZEMTZ4Uzd5iSGoneJYPkUtWNXSmZ2lhTnXrRQ_YrJnZUHBExCdwZURp9QMwzGEh3MS-LL6xhaSu0kasc0ZJE_F3XIPSbt4WMJbiCzC7UtkAw4v0iY5VRejW2hBeDpgN60wb71Nyv1jl4x38aeRSuxHfSguMQHxaLAm5bYkmWPsyvXdn8w-VFe9anb0kdAzUwYKm3z4VdUw3CApmGhIGkFk-NjQfMWZwCUg6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=Iaj1FoNUzIAnrqXxIvuiNE9UvPgDYISl0VI9-5hdkTv59ANDRkHcIURwVnte-SX4iNObmVSGSc1e2Df_DbOGbnbPWEL0ztNvAuz8z_oIsDkLI2AueZEMTZ4Uzd5iSGoneJYPkUtWNXSmZ2lhTnXrRQ_YrJnZUHBExCdwZURp9QMwzGEh3MS-LL6xhaSu0kasc0ZJE_F3XIPSbt4WMJbiCzC7UtkAw4v0iY5VRejW2hBeDpgN60wb71Nyv1jl4x38aeRSuxHfSguMQHxaLAm5bYkmWPsyvXdn8w-VFe9anb0kdAzUwYKm3z4VdUw3CApmGhIGkFk-NjQfMWZwCUg6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFlKNyiL3Tkx-NdWH_2Mwh3R-oocoISU7EmiIGhbHzLDaf5ovrAEPqvbHuCk6Goocy1Ua2DNZhE-mCYPo3JUqsIHio_igM49Zxh-XBE8F-gXqw3X7r7gEyqKGxXukaD-OT3LfsICJW7ounG5bgFwsaU6YYLvapJXg-0kcj9CMnRLHeGZBMSwHVCYy8PL1RS9Jugxvcl3MmQj3ylbHpPLaAcIrmmT5XXhlLPe-1OG84Oe3ER3su7K9QBuQVMe8huu56yHo3Yiv6pj1C6h7AWoRUy6mNZbXeDUygG8Xqidbyan632IbdE34BNlB2q_Ay77KkIcBBDqqDytlMg_vKtFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=YkSaJ6J2iwfz90okO7y2hChHRhMEz0-KkyBrkyS3vgsClWpZ3F7B96l9GxUAswETIrAL2_HYtqzEN41bQc-STkdABiUHAgU3e8d8p6Qjnc_Dmg1i8EG2Pb_nDYhrnB4WT6V72D0ylu2S3BsX2yJPw-oyi8i07kvPg3fyU_K27vKP2u15yPzAPXp0sRXJP0k1TYTnBL0gQsaG4S4lX8LWXULnip-5BTjK7xrneABQtlLvnYJ6F91xvXyYjzlBpToA_qfgKSWh_UTCqbg_w2tVJ5Qwbp7xTBcjCUOH6UA6Atui1hluacrTA2-c4nYvF6kUT6ZbrgarJUnMNq9M6iGvNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=YkSaJ6J2iwfz90okO7y2hChHRhMEz0-KkyBrkyS3vgsClWpZ3F7B96l9GxUAswETIrAL2_HYtqzEN41bQc-STkdABiUHAgU3e8d8p6Qjnc_Dmg1i8EG2Pb_nDYhrnB4WT6V72D0ylu2S3BsX2yJPw-oyi8i07kvPg3fyU_K27vKP2u15yPzAPXp0sRXJP0k1TYTnBL0gQsaG4S4lX8LWXULnip-5BTjK7xrneABQtlLvnYJ6F91xvXyYjzlBpToA_qfgKSWh_UTCqbg_w2tVJ5Qwbp7xTBcjCUOH6UA6Atui1hluacrTA2-c4nYvF6kUT6ZbrgarJUnMNq9M6iGvNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=BTm__0GbmHEkkSY0ySNgx1Rt3z4UE4PB8x5XBp5xviG7f3p6MX2vvehD0CREMO2-nGHYMnxYjHAAO_g6ox76iPnmlEIH5mSijrfb3h3li1LouCx1xP08Wf35lk9ZVTNYePX2brq53bQBc8S2WlpOQ99hISl56_ts_WTSYBoTlqmkoYICYcQGeQkjnOhZVt1-G4rKdw99p3lCkOqUQGlg299UwOUmVxoeHa1tQt7C3d3rmZCQRl5onYynCjp7PaiL5iVDxZsXqNc7mpdWBdiLTmoKipbkimQHNLP4UTmQm_My9_GxWSkLgNWH5jqzNidf4VEFGApwDHvGYdON_ODd3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=BTm__0GbmHEkkSY0ySNgx1Rt3z4UE4PB8x5XBp5xviG7f3p6MX2vvehD0CREMO2-nGHYMnxYjHAAO_g6ox76iPnmlEIH5mSijrfb3h3li1LouCx1xP08Wf35lk9ZVTNYePX2brq53bQBc8S2WlpOQ99hISl56_ts_WTSYBoTlqmkoYICYcQGeQkjnOhZVt1-G4rKdw99p3lCkOqUQGlg299UwOUmVxoeHa1tQt7C3d3rmZCQRl5onYynCjp7PaiL5iVDxZsXqNc7mpdWBdiLTmoKipbkimQHNLP4UTmQm_My9_GxWSkLgNWH5jqzNidf4VEFGApwDHvGYdON_ODd3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkbiwYPYm1TgCBoz4rlCh5YydJw4o1-hnmemtMuptV-XBjM_9eRAdN5A6TEvFvwqt5lDnyFkrIZxFkAp95zxK_mXcxGGBK3RzUmvHBmCMb2PuoxvSzdU4wOQaGWW_LFXeYuB7x6MDK8puyGv-rqFwX_NynTjXRYi3NTSqDDG0SyfbEjkmHA7JW8EmAnKguIb_pQF91P2Lx8rY5sMTGySb19lEOqzI5XlhTy5l8EdiF1liPVG0FchLmu9en_XParOZ5-oMZSuFWp62Ka2RYb14kMx9bYuVqzKWcOnzjR8SDbRnSS6lNOMT3T3pkZ9zMf8tcT1_gZmtt7YOwOnRBW4Bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXUwCotwM36dI2kKGf-ND4PFswklKIYeCxB1oAwvjKzHGkU46YNmEsVu8noXjZvxRt2Qy5hx7bqVYrVG8D58W9nNCicP29JFxiumFKwqQO-e_SbdRx3-5z65XxT0rVNEgU9AboZneo3aisPOTXUSJpvAm0jKbV1Qf9akccZAorCi5hQOWDRqMKel2-RBZXL5Cqoz5_JBiWGwj-JmLdN4FflLFLL72LxlCwkZo6PMhWNyPC9gfurd-jMxhCjz_r697lmbrFgkvaSwm5kExt-a6vQE4jc8Qdgo_TWPxIRz97nCiAIrDlxoPWU_Z_If0mBqn5zJ3bjeFPDPYgn8mQfexw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=O5SRseEbXpYZTbYLj-fcLCtNmLJU3OlmSMtxUIUpZrdpCCkfBmq13pzoYAYHidDz03u3oFBkYMd9l0aQzeJ_Q2Eqh-BPraT4O8FbXruimt4hyKxcPA25jDC0cmLNpLKu5V0w5iMzwPDY9dy40tNXQ-Lo5z5Y1HPfxsCGvh2NvIbtuQHf9iMoaKrZKGTn2c1gZOVGBr8s8N5tDEaxF07M3fjmI7q0bFku_UPF7VI4buQUuoceJMX6quM4eOTXITYTIeGhuEwHiuAb0J_cX49CygH8KrvpMWkOE62fserPnnd00YgRsrNa3Kju6ks_sMAR7Oo1ZiTLaWGOQfszbwGBXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=O5SRseEbXpYZTbYLj-fcLCtNmLJU3OlmSMtxUIUpZrdpCCkfBmq13pzoYAYHidDz03u3oFBkYMd9l0aQzeJ_Q2Eqh-BPraT4O8FbXruimt4hyKxcPA25jDC0cmLNpLKu5V0w5iMzwPDY9dy40tNXQ-Lo5z5Y1HPfxsCGvh2NvIbtuQHf9iMoaKrZKGTn2c1gZOVGBr8s8N5tDEaxF07M3fjmI7q0bFku_UPF7VI4buQUuoceJMX6quM4eOTXITYTIeGhuEwHiuAb0J_cX49CygH8KrvpMWkOE62fserPnnd00YgRsrNa3Kju6ks_sMAR7Oo1ZiTLaWGOQfszbwGBXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=FnfCwQVXekhiQcHnRUCmCKo8mMi3CafaF2yEvJxAI9MbQYl3X3_SeqrututQokmg0DVzrM4ipMeSSorj8-4jkhhue2Yqoko6hv-ngoocnakO3IookfPTg6whXQemvQrO-qsboBKuiZpVLvy8jRApmWeQEFF3k-yydG0Y7OQ4FZROi8l2za4Gf2Za1lCjzUnlY1Z02RuFJxGYEQKBM-uuCK3Xxnz9npwz17hQ0nF-vnIP3ctzVQcfoDzPsl4_9GnUCKXKOewTeVmROirhnRPea1lk6KcSX4w7joQxUkuD9wbRiuwHpS8C-28Z5FlfzeNlmPJV56rBVjhiQKQiHUThpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=FnfCwQVXekhiQcHnRUCmCKo8mMi3CafaF2yEvJxAI9MbQYl3X3_SeqrututQokmg0DVzrM4ipMeSSorj8-4jkhhue2Yqoko6hv-ngoocnakO3IookfPTg6whXQemvQrO-qsboBKuiZpVLvy8jRApmWeQEFF3k-yydG0Y7OQ4FZROi8l2za4Gf2Za1lCjzUnlY1Z02RuFJxGYEQKBM-uuCK3Xxnz9npwz17hQ0nF-vnIP3ctzVQcfoDzPsl4_9GnUCKXKOewTeVmROirhnRPea1lk6KcSX4w7joQxUkuD9wbRiuwHpS8C-28Z5FlfzeNlmPJV56rBVjhiQKQiHUThpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJ2lagklmvMhWDsKJ5wjnfcFpjCazywgmmSZbBaEllyguPmXdUOBIx4VyFgriJQGzOZRYMwKX3KFltnjMO-UvPstCMteQKR8vnsiCMh_JwmSN46ds_oGo6RmvtRKBWeN2fHhmhFeuBmpvLTCh83LZfHInPI8e1j8QfVecW21gmSufl2WcVgTpyGwyS1KkjCj7ZW4DGomR4TP5uMRjO_3xeh0u5RXlK_thu2XZ-sTMZQB6-NRr1GMyPBBxgmoJnjCZWa0eoYCS-cGCHOrVHUUjSEgA2shGewLUV_9eq9cp7FUJcqxnN-beLovPixzwYBCega7KTlqMsAX78XzIGqtNXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJ2lagklmvMhWDsKJ5wjnfcFpjCazywgmmSZbBaEllyguPmXdUOBIx4VyFgriJQGzOZRYMwKX3KFltnjMO-UvPstCMteQKR8vnsiCMh_JwmSN46ds_oGo6RmvtRKBWeN2fHhmhFeuBmpvLTCh83LZfHInPI8e1j8QfVecW21gmSufl2WcVgTpyGwyS1KkjCj7ZW4DGomR4TP5uMRjO_3xeh0u5RXlK_thu2XZ-sTMZQB6-NRr1GMyPBBxgmoJnjCZWa0eoYCS-cGCHOrVHUUjSEgA2shGewLUV_9eq9cp7FUJcqxnN-beLovPixzwYBCega7KTlqMsAX78XzIGqtNXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfV3dqvRH4dFo84i9dW8Eib8kGta1cXnCngKJG6_b_1gK1HwKRE2Ceus6xOZHgH5Idv_GhToeZHiEbyLyN23x_kUjgdgrTCbO6VJM9CSVEGrqgAN_iNiFfpXhDQeeaslAkpjmoc9C8JvGWm7UtvVv36xmkqC5UTBwMDY6-vFCmcgmW0EQI4wp8J_t0g7hqTsipC0v611XU5iwBBKcedC1xZVvEjbcqpFZZpSdZxFkPRQoM1SwNM_TacvZmmM3rStsO05x-_BWDcpil661dDAaoyfnHaoMwD-NKqi3HV08loDbpz8F1HBKrQ4QdTNht3k-YcQ_uy3k3sjYjApRcslFw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=m0MueZeRN_K2RxgO3WS4xTSywArYmRixFPi-16z331dzPGw_khJY3DDTCJ9gLUTbc_lHJO2DIRItsCiezGvxhBfIOf_YXU7VnVGXh1stuyxA5RRpLCc8T3likAqIe_jRsjLA8SHkoM5BlFn8dmriJpgOjYHKSJxE4SQoE3pB5xrutBR7yH9YteaJGS5i_RP-Opd_imIvN0WItQ648_aWAht6ElXKRvWO6kIlEbncDhaiJzK3zrSJMfP_lVcvt-notdsOvYEtKcg9ILesfCFw42OBcX1pTdH4JtYD-JrY6zf4QslBygaDlIEY3z6OQX2gzirHatRioc4qUjhOpeoOHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=m0MueZeRN_K2RxgO3WS4xTSywArYmRixFPi-16z331dzPGw_khJY3DDTCJ9gLUTbc_lHJO2DIRItsCiezGvxhBfIOf_YXU7VnVGXh1stuyxA5RRpLCc8T3likAqIe_jRsjLA8SHkoM5BlFn8dmriJpgOjYHKSJxE4SQoE3pB5xrutBR7yH9YteaJGS5i_RP-Opd_imIvN0WItQ648_aWAht6ElXKRvWO6kIlEbncDhaiJzK3zrSJMfP_lVcvt-notdsOvYEtKcg9ILesfCFw42OBcX1pTdH4JtYD-JrY6zf4QslBygaDlIEY3z6OQX2gzirHatRioc4qUjhOpeoOHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=axTfd5S4kqbRLhTMJBMkiD-dnMDPox4iwhJcKJLfZ2mGp64ZvJ8GwzoTKmRQQpU3yCLQmU3S_rUToKMS7Yk798_5RgmE2y1qOwThGGWcPHFQjpR4Hj05w5rnxZapqpHP40KwC0Uw0KzJt5g0KhtxvwBFI5Pz8MdywHah_t_gLiQUIcuMPOM0NJmOZStqceFG8GHzvZ74Tgb8O6od3zI3OV54jhKB2X7Kqi2yCOuTBVY8h33Yf7A8Ma-5iKVVsfaSpWKJ4AlQqOvhfNCi9dPQ8HdDZa2YImO_oAfoNuKJniXrBQJuaqsGeCDa_OZc-0Ce3JDfT9dvEu77CdMkilHRHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=axTfd5S4kqbRLhTMJBMkiD-dnMDPox4iwhJcKJLfZ2mGp64ZvJ8GwzoTKmRQQpU3yCLQmU3S_rUToKMS7Yk798_5RgmE2y1qOwThGGWcPHFQjpR4Hj05w5rnxZapqpHP40KwC0Uw0KzJt5g0KhtxvwBFI5Pz8MdywHah_t_gLiQUIcuMPOM0NJmOZStqceFG8GHzvZ74Tgb8O6od3zI3OV54jhKB2X7Kqi2yCOuTBVY8h33Yf7A8Ma-5iKVVsfaSpWKJ4AlQqOvhfNCi9dPQ8HdDZa2YImO_oAfoNuKJniXrBQJuaqsGeCDa_OZc-0Ce3JDfT9dvEu77CdMkilHRHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=SPoLroJ2_z72vEj6KDoGQW-4M7NYYA6Cggc-HQx-ScJFqt0-fDc9GSWSNrsoEukesBrHfZRHSMfGrbZ95yl9gSH413LFGgaAWcMg9DEmuZceku5Kgf-9equJPy5Igv5ET093cr7lqSEMyZ4WMjS1DVgcnLBcDkFwSP3rGsSevsspdHGNi8LMnuvF15c8WgYJHKao02JamQh1yNQaVcU1bP1OwRKS6jizmarzYcWH-v5_2U9RFPh7OYEhCKF8bY6HnX-mK4XAWSLSpEbrKTGNQ3dI7KN2effoa13NZcRG8BA46N3ja8PCPvXOVIR2zkfNk0PZWbXRlZwVrtgUvtPkHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=SPoLroJ2_z72vEj6KDoGQW-4M7NYYA6Cggc-HQx-ScJFqt0-fDc9GSWSNrsoEukesBrHfZRHSMfGrbZ95yl9gSH413LFGgaAWcMg9DEmuZceku5Kgf-9equJPy5Igv5ET093cr7lqSEMyZ4WMjS1DVgcnLBcDkFwSP3rGsSevsspdHGNi8LMnuvF15c8WgYJHKao02JamQh1yNQaVcU1bP1OwRKS6jizmarzYcWH-v5_2U9RFPh7OYEhCKF8bY6HnX-mK4XAWSLSpEbrKTGNQ3dI7KN2effoa13NZcRG8BA46N3ja8PCPvXOVIR2zkfNk0PZWbXRlZwVrtgUvtPkHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdrBBXUPSfpN3pXabrkZ5AN_iki1rxXUqaW3so9R_jtLttW6Ei3AyX14qY5E1blc7fM8_ZZxD2janYL3hwnxTSrh4MLFk3R0UMAZw0CSClSZKT4TVVYJQ5s3sR8GVXU8vE8vaKvE8caooZpyxX8IbXZiNX4sU5fPFv-oFz3ty5qL9zEp57keDon3nsbMWNxAHqnzNSyOZD-uewL2N6ok4AQJfzJSkBJie4EgT5EAvt7SrP1QYgClzmuRnP0iFO5mpAVz7hjo_Sw_qwAvVGkMQK-GOUKg0Y_zBr4LnjFE1WQm8I4qx6ORFX-2rtrX-1FzMSx1z1lmR2BSSzPKVuP1Ag.jpg" alt="photo" loading="lazy"/></div>
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
