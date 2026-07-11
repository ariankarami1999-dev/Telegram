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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 10:37:55</div>
<hr>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHyP78d_fSmY-vAEqFik2l7ZlkGJy21Sx5I5dXjWixnIxpRpKMQdGkAI1Oq1KSAenwWGwTeB-J37Ym_eptTW1CdqlhbHYgkJxls9JRsQ6XtTkUONkJqS4JY2SPk50aB4rZOLXPUJiFVeAy3u1w6TP0mONF6NlH32w-dKUTKJRoz7VaBhNN7Z95b8cIM9PlEwtvH-zGzX4l1FtoDauqlw_SNW_Xu1nKSHmCoNkqm82SUg5FXs1X_dz-73zty4MuzmLJ-735vEf_LQIWyQ50EBzG63ad77roh1KcQEy0tAt6VCjwrdaVW1OKXmh-XXe-AltoS88ELnyqYCKtTLo7lkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFoTgLRG-08-wXkVfnmUjpyU85d5MEOPeSE2RXukUJ7gcjmFTYlZCb_kpnQL7ZIcAAM_lDv_J4qZLl0hoiuQRaoKA_6j-aoodXfesfc3KLW2-ibWZjxvxqxsCsKOE-w13vSFR6YCpn74DYo1NOBBYyEvAsrIYpZHslnt5ahw7Y8rBD5zD72zEjJb8Xbr82oFCT3fbG_O9-gKukh3C2YomWyaoxAn9HMpLntkpivRZrpZ4r0DzEYp8eqAocUxAJO47HRnA1D8xjLyMZVi-YwcsKo3Qk76hvz83eeZEW9VoL3t6eBs0cX36qSbGuiRA1OhvmzravFHMOyi9dx-QJrwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6fj-XikOE_vV6gn_Bc8O6-xIM4wgXc4YypxLCBQshzeZI2ex4bJps45gE5IffGwgyOcFmOIBXpQ5LzCUMaN_tBTveENWfWCKP8xENhazzUOnaFAp2M-41EK7Ymex4ZhS70FmJAmyGgh9BYHdlF6czYGHLcTQPXfB5Pl3iD77I8DjDXJa0sUIEh6zuEi1VR39aXBilQoalJgeV9tVniQdu1Klpw0ZHKxsgfSfFTz0JXsGf25mcyADsfQjrHKuvlh0iIPGCR6LoO9Jd48T7nKZvec_4o_-CsQq9qSzSvN6_jHrdi6Ysi5U9_kDIWzg08jSHPScvB1Yh7KR2t3-wfS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=HXuHCAa6L1Kr76JfHGiOfz0dd9cSOebiy8J7TB_81UlCp7Alo6zbul_0mQioZsRVKuwv6VwxE0jLo2Y11E9t9DwAF1PE9EGnJXN5oUJXdLoJlT2-5DHVXRUf7yfsWbCbL5Ix5jYm4sHqthZkQdWfTeYuprh06IQz9iCv52Z1AmAzPb_oMS773GoNzzyK-FoWmcSWXtb43AM8D-HXySDFG8r6lCMRhBieb-hA2jVb_gxgqx7uc-rvn7LoBtMdji1bNpZNWmV94o_r9ZSFuiD6xOLvrLE2eii2pd2NmHQdeSzE2PHr6_gUJ5KNraofyBdhRgEhIYsVdBMK8kwNoKSPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbIJyOE2Zg99a7z3TD5mDWj0vjc1vH4vH6eeDCZB033bHtcto7zbvY8OM41MekdSJL9DlcS9mLECr4XoRiKdft09qQFx0vnI8Uf4DSB9UJ5SLtKNYr4kzEbFsDroDdylLGJ1uLB_MRRgKpUuLhaWn329PoFDM2Mf7VIe_Vfs2tbR3FlpSShbyJ6hYHVPN45B959Ufyq7LeVRhGgU4i9RBjDSuvUrTRx3kAfK39tQMR-B3y8NO69Z17tPQoOft3RC91injyqPAcnU69MuP_c5i290F9K3QcyL0s-jszxBquiXLylYWfTy2J4tucAQBOGLSqhVQS5QAUus7_jHfnFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBCdTL9seDcNwGsIb89YYMmUWZ75YhupG5WpItG-REVUvZfiD6KHiROnXkLn4fzdNEvQCBsplLIerYuH0UMUBEtMsezM3MC7ZKK7Py0YFkm2H0O6mZei_Fnzbygt7tAnrp_QgM6h59w8uxsGJIyNVQN0aLBYMYZwuWWVtE_nnIqjCdwrYgb8nyJ4K2r6_6FmvF1cFmuGuqTGjxgGNBAjAkenwQxu9CHL-SNdywTVANS_otcnr7RB-hd3qv4e8yGeMKp9oah80UsGtFRxbWjhdqYY3e5LcKoObVpckCAzAsFgLiWr1fFP9YOF9Blgz6KLpZDuv4UTBUShsOAstb-pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_jklWp-P3SyRXbm4_EDnMya7QubfMI49g1j4w_VhiPn-iZO2Evl0qL-0_yfAfFGW06qtFJ0UHnNf8VNKezps_esDctb0ISCH2P6bquT2fhd2L-LWktS049d0km2_qfc_tzlCR9l4PnCDawud2NIK3WyD1SKzbAZDNNSsI9Ag2I4XDPwulWsAhcmD5ckwtPta7cd4Q_2LgsjjzJuSBgaE4NfL6ji8a_T2wKx0RQoUsLXHxU_QD0i-XsiaHSvD88FEIKUiIeua4WC6dHLfzg3ljE_VPOoMVDG_dxu9S4sK-nc3_VHIwtLtU2D0qQOoBR2AhqMam6Ajzxy-v-rz5Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLFj6blG066qOc9Vz59KMvvnEt9kXhpJ-qtpAmFfW5ICohqG4FNQbWoELS85GqFKPesMMQ0oIfeZTJVY-UBuixdjzb57WF9FRUwO7fSY_zE_YSTtvWkrwiIUm2vO2p_7aXcYiUh9MxrcFc9j22DyifsmU4IGvvMZCwovXGmVQUWCILGwMwwid2CfDJ8gyH-a898QpObWojN6z8_9nSXZslXvmd3cLOi3Mv1Tyvs1VE5qQFTsUJnUtIgorLz8krnFxK_6LS-3AeLXwgACCRvbgX0dymYpAbeS0kksqNXta6BKMCcSOREawZwACz_9ToLVmNrpjPs21FyGGKWgGaYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW3Y8wkErEwjwhOu146AJeeXna-1_Q0yQHyVoQUogvuEw84IQQWdhgrcwU80wv9tXG-1-1jTExHEOTwqgh0A15l5iYi9CWoppsIWSS_H_9MqlPO-ExhLP2LqfKuW7q3xDK4o2mdX_UoqYv7uPLz_u6ilcSEtzGMwSEIrDajTgLwW-XHDpJZvpULYX9Nmzv8qJtpy9PZuvcubBZXBTiJ92E6mS6ggwrjB_PG7OV5UKWrXZQCzHSFlIUOOE6JmN3GhWMWGj7vpEg5yt4XNt_lIBZmLVrNJDyAXQONcTbZ5wKvksbzWFVuWgRJTiWIsxnT8K7PmpZw3v0Ako2lvBbMjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftoT0vHGzBnDY_XOgrbM999A50vu0U3HCEN_VD19MRDlKDrZhadB94T8TrzcNVRt85obQoUoJlZuJK3fO9oEmw4y29FrXCXwTbD_uGmPLdIeQCkoycDhgOUajra1PbFAt9VMcv8n_IHQ3SHNWnGxGXjVLHBUO55RjZzf5ftn_evCkOxFDKjzuTt0TUvZjEPYx3OWH9NLgMRb4TmkwxQfeP7eyvtHE6V5ul4OKgv-3bLHn9tJpWBBpZHnTHEQ2wJppZGzm0FF5ydGr_3tDiyBeExW8qgAtWyFe2c8Um8pWnXv316Y1cQGaND5plapVjmBIXdW2g2xBfNyjqXDsYpiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBuHBmINNg4wiMez3F-XCUwCh4n-_2LP_GWmwRlvnv3TFyB8RtDkVdxb-Zy4nGNuP-wdA10DlFbZHZ3V7DqWPXgM6jJi_nBBZnfe_VWYMtMZVTwM3Gkw2PHhpNwx5Q94VeSu6SgJCCxIPXPNGYI1f0EMhCXR44ZpGDsZeziddZoIIatPBWIGUFywliuc8Ua_-t0R8rx1NXDW570NgtDN5LEjSln8aVO5c1ZPYPUopYboMTfzkUbascvXkreIKjppVfb7XzKleq3GoqDFwbxxxuEigMvroiMAWjN6zjiNAYNdzrFWaDGyALxHEazfkLoMoyO8bvmEuGzgrWQgGpGQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN2fLb4cazVvpoyA91J3Xw1V91yDEY7pxYNgyUboOI9fXj91j597ISmxfcEJt_qEUY4Eh2hbwuM_F02Ox3-MqLHnZHt0fMpcP6qVafcVjRFKeAdOP41tExPMPlOR_FAbVXY6TkExty-hZSS58DfVrNyIx-ONpPI0hSn5r5zYv28Xqw3YcMw0ZcKS1d4VuQfoVSoZ-MFA1AI3sWnUVmzgndyX7JEmOz13aMv_PBYicl5pkYcshx58ot7S6HWN2qSBKY87Dy_t2yYzlrpoelwlEQCVAEx7zjN-2n3Ty1JYd8r0GIG1hRHOgavx1i1nkVK_UoB7ksQccoiVrr0GUQT5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=mDQjlTRqRN0zJeGqSL6LOwovQK7wW_eITT_cqHnlvI_cYaSgjM8iqFfZiCpHrMO0Au1zF2154iIZrnn06Hu05hQgJzHweYyyMausGGrREkheIVMemnuQ97ARaPUlE1wTfY0Sk-RFUINlz-su7NvVOvki1w3MSPN2KD8INpPBYTckOVUsNEVh7oN2UGIXgdfD_w7_6RbAXLFs8Qhc4cKc--EOrLS5vZMje4ARQxlGsZi-IAvQdYjK6mqRqWyGFm3UNv3Bcg0mdutireIPzcj1Us-N9oaKlFd3CoONXfOioQFiiCNeYvg5LblW4ZectUeZDAAYMFI-8o58J7T8vit3Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLCKaWezzyHSKORv3MC7EKmc4haiNX757Zw7SO7A3uvzi3uxNn1LtSepcRMgKbfZ8NYL2Wh94Ejf1MA6apDzwrrpqC1ZrI0yehSgGkO7fOjXOcg-xb1pdHULhGBotwmon046Znsz4f-6mvJPfs0o148j9pq3yr76997RzKvUlbDT5f1xH4hdqb_dO2XjLNswxuB0dntGU9IJnfGcVciyeheXzTc4BsUUgu97xkDmPohqsPAV2bQUry5PmpyS4en1c0t2m1wDRFJsWD90U3XcLGHTGEBENedOS2HzigXKiwRqAr7oNIH3imylijf6t_tTg73aQl5hmLqz0JVM4WoXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7kguok9aVsp4Xp23i1hypt1bR8pPQAw5mcqHhk4k-lybxBtPKXExXOvvhS9s79rjlBKMGKJn7ZMgWHzFvChlIKdXJUfAG2eQKD3STHmQahkJp9lfKwrZV3_t0lZv0AGGiRnkmFG0ewY9u6Y5YC9klH7ZMiW6yrOagyIB7VDc52FF86ZL0uYU3GtIXkslWzc0Tv6cDgkVeoGtsfdQmwimr5MG0Och-3nwAyme0TD8nMceDGaerhT9GFLTNKKIya0-qpa7C8WjIS2DEu_EwavzUfT6ink6R6_Z0L2D9XCp3RttgpJsIvzFz6OtjVhBu3UdOcpqaRTWU7iylwo_4Li4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qh-FOOr9sC6pyO_ioYMw7pnUm6O6dDYP9l-PS_F_yyMhRDI49WHd2OY9pzUg2A0bbbWAQNYGsDJWJpcKq5UNsv4pJTZZoMK_RBfiXl4n0IxDfv_LkXVk6wBm0FGXGF_M_uUi0CdGu7OgxcQ5PS1CHpwq24uwgrSWB7z_72Xp77iDN2EQ_8e_eKqMY5BY4w3PMeHmAA6VMSaTuBcPsdFfemQP6mbZmUALbN3yMG3cm2MkLryTuAjXll3MwPicw5Cnrrb_MT8LjmppXgAA3_bZYTfb5vu9H6xaIbTizPXj3o0qMeJKVxJEncFxHESx3fwyYcK5b51gE2OAIysRuIzp0X-Y4otUaRSPG-SJDlxqc8xn90z1sr1IgtuYptiNmqbbkEzrmcQjQxdGtjy0o5I3oMl-ZXsswygF03tT-LRYY2qKy_r66K_lKSwlsu6_uEZRdl-qTvC_ixFcxntZSQiXvrPPBjxfDYh66xTrzNyPuBRmca2nuBT-KNy2IG2N6z_ZKKkWNdR4NkrP-6bSPAv_hKPcUrxApEdpc6eHniWahdNQAiERBnql3DoA6-2OptPCK9QGXqA8etDfcSxZLaaPIyQFlrmkuI0WKiXoWaonoTX_w-qq77o6nYgDURzrAA84n69iaWpfXq4o_5bNeAsqZpvQdwZOvMEDsR1TVxtMJ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=qh-FOOr9sC6pyO_ioYMw7pnUm6O6dDYP9l-PS_F_yyMhRDI49WHd2OY9pzUg2A0bbbWAQNYGsDJWJpcKq5UNsv4pJTZZoMK_RBfiXl4n0IxDfv_LkXVk6wBm0FGXGF_M_uUi0CdGu7OgxcQ5PS1CHpwq24uwgrSWB7z_72Xp77iDN2EQ_8e_eKqMY5BY4w3PMeHmAA6VMSaTuBcPsdFfemQP6mbZmUALbN3yMG3cm2MkLryTuAjXll3MwPicw5Cnrrb_MT8LjmppXgAA3_bZYTfb5vu9H6xaIbTizPXj3o0qMeJKVxJEncFxHESx3fwyYcK5b51gE2OAIysRuIzp0X-Y4otUaRSPG-SJDlxqc8xn90z1sr1IgtuYptiNmqbbkEzrmcQjQxdGtjy0o5I3oMl-ZXsswygF03tT-LRYY2qKy_r66K_lKSwlsu6_uEZRdl-qTvC_ixFcxntZSQiXvrPPBjxfDYh66xTrzNyPuBRmca2nuBT-KNy2IG2N6z_ZKKkWNdR4NkrP-6bSPAv_hKPcUrxApEdpc6eHniWahdNQAiERBnql3DoA6-2OptPCK9QGXqA8etDfcSxZLaaPIyQFlrmkuI0WKiXoWaonoTX_w-qq77o6nYgDURzrAA84n69iaWpfXq4o_5bNeAsqZpvQdwZOvMEDsR1TVxtMJ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxBT1INx4ZbLKu3CJTP-CTWPRIcAVE3URHcODUj9Ofko1qS8ge7NGkXrFuhRQ4lkB7VJtmQQpmV-9X4tR1XNdYwEWh8ybmIULLzUyDI25d2LxK22YuKkvEVeOvmzNDIqsqwasa11WkstP_KYYQvTh5w5Taj_IvJ_O_58eur6Se7HSkh5v5ubyI7503W5Jf-v6MqPN7T4rQST_XfqndObH7LVQmqCvk6QlLaZC436jFdtXTY6WhBmmpH9lV7TvwlnOJlLjz3scPrPBJ9ftUct31DaBM-4CLiy7-pS8IlriawKk8V3LawwS8jnshYQrgH8U3X_W2upFowD_E7GvIhR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLPyfZhgm2_rM15TyrT5NACZIDcWFf4mBPW8MPFU7KYGGFcPN2W0gSbg_WSvjHJPsbpymydtoTEPpUos8_xmlssGMHYoPfLzmC1oG7OZVo-taV7jdahyLM5A8BHUb5BhEoA0iL2gaK4PnsBLnzC3Mh_RFNokO4xpmncx5hrbAcsVKNsz2oo3HhNNoeqw8ENNQCxk0BT9mq5Ic7gCaoOWw40T3XvWpMqqNbBWG7EGx6aNLmm0aglHSIha9dl9CbB_IcK33CSTfaQK-rheGPjnoqdIH2quwbld1Z5_koKhLu8tw1UuHqB-cMw1Q3aVq8i0FAFabBy3epvvYuT88YTnZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vfOT10qcev6fW2yLBa2IHmpHM3HIQwrYVi4c85LumEoY0I9OgFM_IYBBQn901uujggbrEwsBf6mtm_a8FCNJ3_2notIZKjLXgCD_-QqrqxLpPTCzDlfrMX7rxyGpEWXGG3bYtkHTi7_iKT8ifQgsFT5oPf5XsdKsx8oL2ts4Ll0oTszGHPm_vxqUfyDAkM_HQhv9NakJoPKa-zM-3A_Jdq4CScqdrviz4WV15NQo8ETGhk4SCQQK-8ohoqKGX1C0nUxk37FVNFj5g1NssUwY88nw35Qzw99TBZgQcJsOazwoPdlAjpQ7vjyfTHtNzU7P5Elr28XOGu6WpqG6BCvuwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=vfOT10qcev6fW2yLBa2IHmpHM3HIQwrYVi4c85LumEoY0I9OgFM_IYBBQn901uujggbrEwsBf6mtm_a8FCNJ3_2notIZKjLXgCD_-QqrqxLpPTCzDlfrMX7rxyGpEWXGG3bYtkHTi7_iKT8ifQgsFT5oPf5XsdKsx8oL2ts4Ll0oTszGHPm_vxqUfyDAkM_HQhv9NakJoPKa-zM-3A_Jdq4CScqdrviz4WV15NQo8ETGhk4SCQQK-8ohoqKGX1C0nUxk37FVNFj5g1NssUwY88nw35Qzw99TBZgQcJsOazwoPdlAjpQ7vjyfTHtNzU7P5Elr28XOGu6WpqG6BCvuwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llDfvr5-DEgo0qR5oI6bKHDYeB_QXo3lcwZGiYxh4pS9Asj8C09IerUCXB8MP6LWgF3UoMDWMSYvzYZQrWAtejpvJyykXaSrTr0HFldV28tUnOGjLZ5cAUi_ItUwIFIr8Af00j7EgCPZf5F7Gv9UAJF_gXTbdmCkQVXBD7fH1E6BJ0OujvZcRPHXB2Qu2tM-NFBJaxGCNLd42_BnPrCA-_WfzTPf2ZHUx2p7wiyMXzMoDdNpLSNZGPGXQwwBZuiPTCRcmoKQQB3B3YyX6ukfuLL0n449qWa_S-t8lGI4_l9ew0Cl5KmdpqvYKC1FuU5aw-JX92qXNUGrGUZ1_ZQQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olhDebBsZxyjQsKO6POc1vPFplwJ6bhuoKNzu1nkxH9lt6V4JIe0D8bNXPXs3jnMvAPVxfhWzgPcgmysLZWhBoUDlOwpbSl_f35Kx5oIodPrxn7kuTGRoLFADHz7xflQtoP_cIP_-wuwrPPYwHbj_DnLBtU6wzOaCKsc3xVt9nvNgjwWfzP5E0TBgqjp756n3nXrcTBcdRyKZQLQh3mA93AkduqZRBBKUcORp-WX2YVPtfzxG-y8Hq0SXzTZVawOUvppx-3Ssg_WBwRfTwNrarB8HJCW4bIPlkzUpVTrLDDnaZ94XF194AKzKcY4J_g6ErDx8JOJjvAQCkOnbYrt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpEVHKjaCZABtUsiCKXsDGobfMRhWCAMW_HYpoIqoMj8AdmG0WD7_QyrAjgeczKFYMFmnqUT7ldyhgKbucu06m7Q7-iTJuPekKVncVNlb8e2C7VNEpzQ107LB6OzMcnyRruF8FlCIbS7zwKZ3xTmOyDDN3SH01nq9VsPIiKbt9jSn8Jmh2SYCq2cyQvwvG0YtKSmXxcsyfRIjhptHJluHZCFqIWJkZSd6G7HFGYq3Id4XBrb-E039jvQO_U9OvO8bsNIhu1dCUxuSCicc-f7ct_TAWgEuyzzT0fCcruK_1pJvKE6F1ZA5rWMja1sTAcyE2uVHVrd6wGT3Yr5EmdtiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=d6Os_yvs5eVdWvFSt8op44-o-x_trPaT0yUYueyCbykrrnA8H0wRFLl1UeXxZEfPHq-AbsfxKyLrAoogSUKKKdu32bTBJ2c9eFKBiYZDjWForamQCB6teHBOr7YIPe_Q-8muvB6SFeEP4iwBB2tdbi_jhxklrtgs-kmuSq4ruxnwq279AMS34kMcG6FdlXgkS-LDjJRRgODtyf26golsqrjgao2Pgwd0NGWSiaUm1nsjEE24CgcniWSUahWeO_GDTc44ehvNeGgqpK2hNUS7zgwr8U7iCBy189JEQEQwGrFjFhEj2Y4BpkSMy8MdQPAa5xbK6tTyrfQ3MBwlWFjrDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=d6Os_yvs5eVdWvFSt8op44-o-x_trPaT0yUYueyCbykrrnA8H0wRFLl1UeXxZEfPHq-AbsfxKyLrAoogSUKKKdu32bTBJ2c9eFKBiYZDjWForamQCB6teHBOr7YIPe_Q-8muvB6SFeEP4iwBB2tdbi_jhxklrtgs-kmuSq4ruxnwq279AMS34kMcG6FdlXgkS-LDjJRRgODtyf26golsqrjgao2Pgwd0NGWSiaUm1nsjEE24CgcniWSUahWeO_GDTc44ehvNeGgqpK2hNUS7zgwr8U7iCBy189JEQEQwGrFjFhEj2Y4BpkSMy8MdQPAa5xbK6tTyrfQ3MBwlWFjrDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=cbpBpIJwrV4IYnCXa6vO7sECGhmXROhlW8m82jocMPD2fNuZ3KqXcDvlFI2GHhFjtadrc3GxNl-1d5bMU-L1CB1yzdmmYpTEhPdRaImhNNlaOV0ntPxCy_YbH6ABhuBbmN8sowOiBXnAM13b9kDp2T0ABYnAdM72Y2IAd-AhYDoLXgyUkANgdbZez1Y5H105t4iDJMDSrr1CXoNZCyjpNPgry5CJ0tuGyh3ndvSIZv07XQYM5Eyth6umDCjtj7bhJoWYWTfvyCXWAasIQBXM09K2c7NC6awraCOntEnw6d31ZRY_a1Daqp82qYM9Eb6uVoIG47Ya-2HmtQqAtY6lfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=cbpBpIJwrV4IYnCXa6vO7sECGhmXROhlW8m82jocMPD2fNuZ3KqXcDvlFI2GHhFjtadrc3GxNl-1d5bMU-L1CB1yzdmmYpTEhPdRaImhNNlaOV0ntPxCy_YbH6ABhuBbmN8sowOiBXnAM13b9kDp2T0ABYnAdM72Y2IAd-AhYDoLXgyUkANgdbZez1Y5H105t4iDJMDSrr1CXoNZCyjpNPgry5CJ0tuGyh3ndvSIZv07XQYM5Eyth6umDCjtj7bhJoWYWTfvyCXWAasIQBXM09K2c7NC6awraCOntEnw6d31ZRY_a1Daqp82qYM9Eb6uVoIG47Ya-2HmtQqAtY6lfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=XZLXTBNJqyuZ_t1nRV86pE98OvP2ZNeUlQTJeGqN4pORzWc1IIZT3PfQvyQj6OJw4bx0sA6mYnowOqzTVySascCvItbx7MIF17RSo9PCKS3ruvBtHFEd8qMtan9dhsikh8RYV257jPHeJ7PA-6VVrm5_v4R1Yf0EOk9kQYIJNkAPHZ5-nT0LhULBPIQh8FaZmADT9EDOkafQt67OGaPpGKnutURn9bA6PehDkwFqpqq52DRQ0zgwQ3gJ7hmRAOCKjKTO9ruEpGvJ8x8QwovUEis34HMZzLBXDxiIi-7dkSNOhF1gSKioB2lHaO0gkI9BNcJRrm84uq3-QEpnrjpMhwoRMlmfzyGvKasl9_KSJ5ycnqe4r4vzKYWPDTtZaYQAmJLMTV14o6taOYkiL2m5nUhBBdgk9zLNtbGIa4Q0EricavFjNWb3DjFskQ88jBa4nggdTM7u6bcUxnS_I_R_m2U1OIIxeWrQusxq-WAFnbM1s25qQv9RPArjil0WCca8oCA66_tTJn8VxpgyMe7i0fYw98eh3tqvqvxG6EWgOXQ7-tzerRH2at8r8mWEUyI-iz8UuS4kytXx-FjSZe46EirhCUqjTSvZPIki8lNjuSFSizpuRl3vcUaVrAfrp7h1of8DyeKHR2rDZxJ1Wk0hojk8rqVd4gafbZT0a13lhGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=XZLXTBNJqyuZ_t1nRV86pE98OvP2ZNeUlQTJeGqN4pORzWc1IIZT3PfQvyQj6OJw4bx0sA6mYnowOqzTVySascCvItbx7MIF17RSo9PCKS3ruvBtHFEd8qMtan9dhsikh8RYV257jPHeJ7PA-6VVrm5_v4R1Yf0EOk9kQYIJNkAPHZ5-nT0LhULBPIQh8FaZmADT9EDOkafQt67OGaPpGKnutURn9bA6PehDkwFqpqq52DRQ0zgwQ3gJ7hmRAOCKjKTO9ruEpGvJ8x8QwovUEis34HMZzLBXDxiIi-7dkSNOhF1gSKioB2lHaO0gkI9BNcJRrm84uq3-QEpnrjpMhwoRMlmfzyGvKasl9_KSJ5ycnqe4r4vzKYWPDTtZaYQAmJLMTV14o6taOYkiL2m5nUhBBdgk9zLNtbGIa4Q0EricavFjNWb3DjFskQ88jBa4nggdTM7u6bcUxnS_I_R_m2U1OIIxeWrQusxq-WAFnbM1s25qQv9RPArjil0WCca8oCA66_tTJn8VxpgyMe7i0fYw98eh3tqvqvxG6EWgOXQ7-tzerRH2at8r8mWEUyI-iz8UuS4kytXx-FjSZe46EirhCUqjTSvZPIki8lNjuSFSizpuRl3vcUaVrAfrp7h1of8DyeKHR2rDZxJ1Wk0hojk8rqVd4gafbZT0a13lhGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIIbYqXku_Wgs_L13vz2tRVRbY-rLp4dsDmccCHL11naMd3yMUBGdnqb0h1Bcht7eqFEg3HTPQzxegZEWasqBeVHoi9JuNRNud7hw46dqwYdptTc6EUrBhCmEi-dSNuuPBjuFQtMO5SRcNUD9kIte27hwD8O53xYX5uR02zjh1Z2u6c7ZGzn6TZZJqwgiSbp_4ooMGbjxn0V9XnpS3-gU4hJtvZtGf5h13u1TRN0F4kAMTEhAE9QD1lm6DR7PQc7imd96EGNeb5DkJQCC6w_4vjbleWTiiyjoPCRcMM3gRijbQSU9xx4XsCKG9SwKOep5_5m2_w04JBAhUeedd2x5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7lg-3L-B5Ksb6d9BtEn_SB-p8ooGDvmCZWU8EVhnyfKRHruV_q2E_uAeIgD-UG3VRDJRobDgPitdki7M4IC_QEsoFJPsZ5ww9vmFmVqsYQf6JjVCs6QUbNEL_OrlotCOQYHTnrbUBrw5z9zjiYwKdQlHk_L5Rz6sH4_UhgCPFG8VroFoHFlRkOMXH7lmkf5OLzBFXtgB2SUnGOCDfvd22DcWC7D4wkf_NPbT_9vqzDu71hbpZBxWddxn9RcVUtywIZIzoZFRVUUtnHQjnYJ9M2LwYMXl5gbksltM9wCVWpL3Y9FQ2LA17aptjxS5zmVk7ERtbUzg-PC9BGARsLKIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Decd3RKKeQP-s9MLR4Obpo_33DR6vbyPayoi8x1ht7zYDPTv5ZyDyf8g8aQnuhoBdspqXAcj5YKMZ3cHHAjTQLXnisN7qoJkBq61h1BM-cZLeGUJ9xe0bmi7-A_leTKnZBlZPA87z913aL1FkOT6R7Pw1egRW1upIfIr-j6_vznEB2yLkxC07I62MBr_jY6oGMWWu-MHj1f9Y0YevPTvxkXKbfsrB2QpZsNno0dM3Dv8mh0kKrcYkxQYqggS8OlPP6_hefzmkreW0WyIn2vo4D5Z2lKTflVtWi6r3ySTXD1MTwVJL4OzBrQy_RgFdjELZGPjRc5bnUNzOHy3P265KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=auuKh_FMvUAaKWfyo9bzKnCy1IdgYl_8lOS3BQTCz7B-TOvI0hWsCWN8hiLuXKX2Vs-TiP2xIkCDdBQPK_sqOwSPZIgySWG69sZAB23HXhqm_Jub4dK5yQSEoDQH6cFigO_er9dyqygwMsz3PGHCHDUgWPJ1yi8sxM9nLkJhk47OiKGX6KR2RQF3wN7TEq3DQiZYhN3UtsH_IL-N7c4YszMxOCP0iS0Zkq3Is3aDtlqbn0Fl5CUhxWSjq5oDZvyeAZ9fvmguJs2lFgFBexXVum2sgY0Wd7Fndiowqm3jBwrCmNp-9M840k7bI9O-1K9mY4RpweHfFSdfxli35MThaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=auuKh_FMvUAaKWfyo9bzKnCy1IdgYl_8lOS3BQTCz7B-TOvI0hWsCWN8hiLuXKX2Vs-TiP2xIkCDdBQPK_sqOwSPZIgySWG69sZAB23HXhqm_Jub4dK5yQSEoDQH6cFigO_er9dyqygwMsz3PGHCHDUgWPJ1yi8sxM9nLkJhk47OiKGX6KR2RQF3wN7TEq3DQiZYhN3UtsH_IL-N7c4YszMxOCP0iS0Zkq3Is3aDtlqbn0Fl5CUhxWSjq5oDZvyeAZ9fvmguJs2lFgFBexXVum2sgY0Wd7Fndiowqm3jBwrCmNp-9M840k7bI9O-1K9mY4RpweHfFSdfxli35MThaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=Q-nT6m74OX9-wnO35qR6mFIoJ1qQGTVRx7-B7WgWbtpwOHp_DBH1N1fzTqXvj89w0ZQVHuvrIZwhSgumZsAzA1uN7byxgHofuaVgJDEgwqqz3yH-2JIfsoGUwJku5Lb-tqOsACxRsQz5GfdlAkAet1O4_Ov3xXwVJWitBCSlnq5HKrUa873pMMolMcsACGdiKHc5FtTVDNwOdq3pDe44Z9pjaUCgmGDdHPRJEf1aj22NauG5MJ0EqQJ5MfkeyR-aj8Bi8FmhNjFmk89qjpcsvHpB6gFN6mVpAx-Jd9zSSmFJf72EMF9eVKlaBfAg3vfmbfZlPIbi_mkXcFV9YYYtPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=Q-nT6m74OX9-wnO35qR6mFIoJ1qQGTVRx7-B7WgWbtpwOHp_DBH1N1fzTqXvj89w0ZQVHuvrIZwhSgumZsAzA1uN7byxgHofuaVgJDEgwqqz3yH-2JIfsoGUwJku5Lb-tqOsACxRsQz5GfdlAkAet1O4_Ov3xXwVJWitBCSlnq5HKrUa873pMMolMcsACGdiKHc5FtTVDNwOdq3pDe44Z9pjaUCgmGDdHPRJEf1aj22NauG5MJ0EqQJ5MfkeyR-aj8Bi8FmhNjFmk89qjpcsvHpB6gFN6mVpAx-Jd9zSSmFJf72EMF9eVKlaBfAg3vfmbfZlPIbi_mkXcFV9YYYtPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=dgkqS6_N1gXUOrcrXtojJ6TB2a7QHYhE__i-teUQiW0IMv8R_lACuOGxRLc787e60On_CWDIRHoWw0u5gvbFbwPvOyhyd0V8aH0juNTrY0hkgxp8Niz4aGzSv4bWr4csHJLEM5bGC4AmxuwsdeMGJAg8899euWZxeF7II4wHlavhCWdhEujLHR8tG57NXC2vSHAns5kr7ps8k8ghTP9AqmjTUExQEZ4lWkCePiHxDv_Yv4VBF6s-djUg3qgUkv3RjM2jdzmMtvJg3mAQZmKBs3C-FoZTeaaUp0lgJ2n59ngYR1tEfVe_o24h3bfVFEpZ6VoiUeBb1H4JA_TcJYk80A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=dgkqS6_N1gXUOrcrXtojJ6TB2a7QHYhE__i-teUQiW0IMv8R_lACuOGxRLc787e60On_CWDIRHoWw0u5gvbFbwPvOyhyd0V8aH0juNTrY0hkgxp8Niz4aGzSv4bWr4csHJLEM5bGC4AmxuwsdeMGJAg8899euWZxeF7II4wHlavhCWdhEujLHR8tG57NXC2vSHAns5kr7ps8k8ghTP9AqmjTUExQEZ4lWkCePiHxDv_Yv4VBF6s-djUg3qgUkv3RjM2jdzmMtvJg3mAQZmKBs3C-FoZTeaaUp0lgJ2n59ngYR1tEfVe_o24h3bfVFEpZ6VoiUeBb1H4JA_TcJYk80A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=BTaB8gi9FXPUyGN8gS3nCVlEWtpiEv6oerl39izvarYN96tNeLa6oteuigWdwlxoKwJZiGSY6THiBVkWSfrNdTjW2W7W3hrLp2E-Ct8E6TX7E-ySomAOan0K6MyXfVIZjL2id0dIS3Js6p-8leEugswNdw4ogA5EeqbHwQgXJOHWV8a9CqLzl1jJTBN7G6HueSltLLZSuFCN700T3HlN7Uf_sV1zgONq4fXoYoDPZznqSRfi0cIhZiQoWUJgy__JJsiGuUfx_VfarakzhVolk9fS96AhBrwyOxAH9dDEuIptZ7bVTTqXBk_703kycc2FOT8ittr0PHgxTsfmCH4Vzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=BTaB8gi9FXPUyGN8gS3nCVlEWtpiEv6oerl39izvarYN96tNeLa6oteuigWdwlxoKwJZiGSY6THiBVkWSfrNdTjW2W7W3hrLp2E-Ct8E6TX7E-ySomAOan0K6MyXfVIZjL2id0dIS3Js6p-8leEugswNdw4ogA5EeqbHwQgXJOHWV8a9CqLzl1jJTBN7G6HueSltLLZSuFCN700T3HlN7Uf_sV1zgONq4fXoYoDPZznqSRfi0cIhZiQoWUJgy__JJsiGuUfx_VfarakzhVolk9fS96AhBrwyOxAH9dDEuIptZ7bVTTqXBk_703kycc2FOT8ittr0PHgxTsfmCH4Vzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRhyJSk69BlWiZXxZYSEjp5okeRgmsqmBj7n6fQTXwNqSKFFkUT70ek6YbCEvrGWMcQJJFIPnjdCEPvX7kgGO6UrOtz4eg0nWvSm3VZQKQygpwK0mdv5_dschHzP0q6k1A3-pD6-lxirhiJkmOK4d7Ky4OKrY_naf0vu0V_ivFnVA28UAAZIKiXxahY53UshxATwQCbErhbvknmFW4G3Sbp7I2_KriScJAMq0SCr1giYgkoUGwrIZ2QKfseEf4gz-Lic9MxzWBgCvkvwi1O1GJD27NB910caNxW5yGjuv4-Rtt5F0PQcfvBwe1E1CtSZHzhw5b8U7RDc84IYAz9KVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=LdiZtrFiX-aYTey-izkCgpgklAQxQatqEX4pSvYZcaNuirbccUro8c7HgRgfJuja3IWbDld9qcjL0e2fXkw2X-6ZtlOKnM5M5405qUREp951O6fyOIbOKtHt2tf7XJ544vEwwqi2HsvViVcpjbdOW5QHmkUrCFMmyF5SqeRxQuOhuidPfWNdY23n21ln7W53b0ctX1IpqjDEqXuuecgwFz8miBRijBmJ-1S41Wau83lcjLsE48jooQmYKd8YifFVyoyGFxlhriZUs_swuGmdAPhTxB6bfsnysi3E7u3Gqr4f2dHQajysVnR8x2RFRCXPJq6NsVUsTmnUpwschrqPF3XZV7WqvZFVoBldtXGNuQUU1lhrN1rmhVbimIjNS8XZvYBM5YWpmmJQ_6ULKTskgu2sM_aSZvUVzSEEQRSZWONsKy9NJfMKKEKFSV0lPDSubW14W7wtpC-cDlucyJz2wfekRLeHM5y4aJroZleuQoosHECbBHAbIfl6JEg6AUprjxUbbZBMCAgJ1htEu3ntBfId1oljFhYTuB8b1uUKuGfpBnSla7LtWjwtjuz-CPkcs8KpiaBA1aULFZbLTs4TBOGisLgVcCqvVg-fDw2B6bOmkRtltLED-B3M4esMVse6RYyFK15bLybuxOJw6DNU3j5HPsn4b1l2z5H49J9AyVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=LdiZtrFiX-aYTey-izkCgpgklAQxQatqEX4pSvYZcaNuirbccUro8c7HgRgfJuja3IWbDld9qcjL0e2fXkw2X-6ZtlOKnM5M5405qUREp951O6fyOIbOKtHt2tf7XJ544vEwwqi2HsvViVcpjbdOW5QHmkUrCFMmyF5SqeRxQuOhuidPfWNdY23n21ln7W53b0ctX1IpqjDEqXuuecgwFz8miBRijBmJ-1S41Wau83lcjLsE48jooQmYKd8YifFVyoyGFxlhriZUs_swuGmdAPhTxB6bfsnysi3E7u3Gqr4f2dHQajysVnR8x2RFRCXPJq6NsVUsTmnUpwschrqPF3XZV7WqvZFVoBldtXGNuQUU1lhrN1rmhVbimIjNS8XZvYBM5YWpmmJQ_6ULKTskgu2sM_aSZvUVzSEEQRSZWONsKy9NJfMKKEKFSV0lPDSubW14W7wtpC-cDlucyJz2wfekRLeHM5y4aJroZleuQoosHECbBHAbIfl6JEg6AUprjxUbbZBMCAgJ1htEu3ntBfId1oljFhYTuB8b1uUKuGfpBnSla7LtWjwtjuz-CPkcs8KpiaBA1aULFZbLTs4TBOGisLgVcCqvVg-fDw2B6bOmkRtltLED-B3M4esMVse6RYyFK15bLybuxOJw6DNU3j5HPsn4b1l2z5H49J9AyVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=CoAbqoWpzitEbPZE0MT2XUDv1IvDh-OTYJHmgb5_f3WLbBgC5Wuhb32KYttQorhB15KQAiB7AfHIQOy2yQRuIlonG6uSnXcrtpiLAu_-gP3zDqTBZK-VX2BixxMkhpfveHfCBcXow3Rc8dbvJhVNe9dCXQ_9uEfzMr7sFGn4Iu5DpBt3CtB2DLH8GBSVXTJCdcgFDT4rA9CsKMMnnUvyYisPJ20QkN6i2GUgPyL-2Nuv8-Be4YlZxU_bxWYsmWoaNbTRu6zcbUyk_9AwqfnY2lxpzhL-pcZt02rF1yHZim7sbrpyR9TEJfdsBrlGjmlYGGHkspcXSyYhVxiEwBld-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=CoAbqoWpzitEbPZE0MT2XUDv1IvDh-OTYJHmgb5_f3WLbBgC5Wuhb32KYttQorhB15KQAiB7AfHIQOy2yQRuIlonG6uSnXcrtpiLAu_-gP3zDqTBZK-VX2BixxMkhpfveHfCBcXow3Rc8dbvJhVNe9dCXQ_9uEfzMr7sFGn4Iu5DpBt3CtB2DLH8GBSVXTJCdcgFDT4rA9CsKMMnnUvyYisPJ20QkN6i2GUgPyL-2Nuv8-Be4YlZxU_bxWYsmWoaNbTRu6zcbUyk_9AwqfnY2lxpzhL-pcZt02rF1yHZim7sbrpyR9TEJfdsBrlGjmlYGGHkspcXSyYhVxiEwBld-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPk9C06bS1vkRD5Zb8ywDbwwZnppv_vlbPtRxvjOmRLrM-5ga3WFuIw7G5DVSnM3m3SzV50Feqq-0wEzr2c45x-naqbWbyBY26Tc5ggynn0ngMt-KktZRGQQEH_QvWDm4conPQ9OGOsuulh-yUGdwU8oCyWPBeusvFgyJ5GTWYdKP6e4lFadWKu6GsO70Br09NFb8uXsrDbceu7ZUoaUvXw8vOwFch0wgMoEpovv5r0A0sFDxvMfC6S7Xep1cEFrBismbRsuYRicCVXRbFGheU67Cw8T-zmxgFOUpeKRcxB4_rvwAuOBRAdAeQ-N64vqz1Ke3FsYMhnZSjMqB-Obww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=P0Je9eC46kONHq7cEMqgRA7aOtERw-TAS3IT3hS-YffsgzYV_2PDcb9NxcthThNQ3Qt98cchQqH7PrzOXtlMahrs6AAzl68FxJ7oLwDdn8I4NWF-SxOE0QFAm4R6qEAfyXGibR0hSxlPpwVTn6fw5f-_W-hlZmxjoHZE3UlYw5PGg1ICNNFW9663HdkdpLrExoo73uQGy6Wq7N0sAecbbLGO32uBHtrtJV784P_mWBQkyeeqIe9NSVGzoYYXfMvboirXtMqtntR0zsT-P1MhC20wvwfdBC-fp15EAOvJQFkL5cZ7A-PSphXez4Y9zX2NF5Yys-xA3Ofvk3HGRAkVVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=P0Je9eC46kONHq7cEMqgRA7aOtERw-TAS3IT3hS-YffsgzYV_2PDcb9NxcthThNQ3Qt98cchQqH7PrzOXtlMahrs6AAzl68FxJ7oLwDdn8I4NWF-SxOE0QFAm4R6qEAfyXGibR0hSxlPpwVTn6fw5f-_W-hlZmxjoHZE3UlYw5PGg1ICNNFW9663HdkdpLrExoo73uQGy6Wq7N0sAecbbLGO32uBHtrtJV784P_mWBQkyeeqIe9NSVGzoYYXfMvboirXtMqtntR0zsT-P1MhC20wvwfdBC-fp15EAOvJQFkL5cZ7A-PSphXez4Y9zX2NF5Yys-xA3Ofvk3HGRAkVVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=bDzMioyRe_Yl9PmW8-Tgxx2kLVaeml5cp359aFxVB3Ah0SCdTVTuNclbuywmScIKfr_aTp3KOdMnH1q87dtw9c3PoaD-zcdbAkow_TIsLYHUWCfJp1CowSmOnGtMY34KgkcqM3GebJY-AhuzoVqyIga3Ft2FUwMgNgKzeUhL6GhuIrnb2FgmlHTfLiFs29s8OUO-2V_z4ZbxDLqFbjXD6Q8ykW35_DXAAuLgiAJG6G9jnklHSyijgywr8lWGtgbfysXHuZmiSSY9JZHIvPuCkUkb3tXh5PBzgYGA_kBEci1AvnOb32xM38MZFigoEO2Eh70m4ZwVMcT54QvOYvaXMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=bDzMioyRe_Yl9PmW8-Tgxx2kLVaeml5cp359aFxVB3Ah0SCdTVTuNclbuywmScIKfr_aTp3KOdMnH1q87dtw9c3PoaD-zcdbAkow_TIsLYHUWCfJp1CowSmOnGtMY34KgkcqM3GebJY-AhuzoVqyIga3Ft2FUwMgNgKzeUhL6GhuIrnb2FgmlHTfLiFs29s8OUO-2V_z4ZbxDLqFbjXD6Q8ykW35_DXAAuLgiAJG6G9jnklHSyijgywr8lWGtgbfysXHuZmiSSY9JZHIvPuCkUkb3tXh5PBzgYGA_kBEci1AvnOb32xM38MZFigoEO2Eh70m4ZwVMcT54QvOYvaXMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sakkBrNS_Jvo0GFwb66R1UcTROLZMMUuUps2A1JJPbQcfv4B7IP0oFcbA9dioEbDEzA6TXJgiWVKT89eaDcn_g_A1zfrlKiZS4L5BEUr3XPxaMWZk78eaL4ZYgaF7GHbZFnUy1GdE6zIcP6mxZbO-Llnb4Z8odszhJVFmsK7U2WZ8t5J7s-aTCatT6EGK8c2HVX-D5b7cdXrkUbx2RXKnx3ifo9fwhBRsWdQtQVxPlcI9KOaCEi_3NN2LKwCVV6Dty-iRNPHIpJL6-pnFnPjD8xPUVAmzlFnWmW9aJH8_G5J7YgN987VhlK28d3UD0k4aPGlJXDWb7wBqseHkEzJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=rLBCsIIkeztc96LEm5jRst7mbdRMWnOACMJlBYh7bG4kNO7UnEPDaKPveM9KzM5qPBscaOgyVBsj2n4_-DX2ORj9iepIOURRoBXCPz-a48Eu_2x8Vnn621Bfv-TAwPoPis0ymTdAHvylzoC15FOrYXblWt5NxVL51Nln0vFrIKyBdGZoJDmtPHBC_5wYD0_y3e389KIsdG6OMYVY7iMoZZYDmmGGdIl6x_kyzIziPqsCn4jhh3WZ7evNb_EkiWTuvfiXCpfXx6xUaRgoey-hDvfOKit7325JsU4XmeDUAn-drSVRVtT8j3VPC53nZuk2lmR_P0S8p7pr8c8N_9W86g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=rLBCsIIkeztc96LEm5jRst7mbdRMWnOACMJlBYh7bG4kNO7UnEPDaKPveM9KzM5qPBscaOgyVBsj2n4_-DX2ORj9iepIOURRoBXCPz-a48Eu_2x8Vnn621Bfv-TAwPoPis0ymTdAHvylzoC15FOrYXblWt5NxVL51Nln0vFrIKyBdGZoJDmtPHBC_5wYD0_y3e389KIsdG6OMYVY7iMoZZYDmmGGdIl6x_kyzIziPqsCn4jhh3WZ7evNb_EkiWTuvfiXCpfXx6xUaRgoey-hDvfOKit7325JsU4XmeDUAn-drSVRVtT8j3VPC53nZuk2lmR_P0S8p7pr8c8N_9W86g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7_vAuE79u2sGAapoZYbt2paXBLqfp42DXNf0aGGywxQ12O8yuj18RlcJf-hcp076oVZZyfhv5_KoeOMqczeRiectO4W6aNkZkGYYdShxKyCblIYps4bAabvwLZ3u835IwhbpmnhkmC_WWIGlom3AFF42ds0Tdvqc9MuGMxg8BKSlZ3jH3RHnq_5jTO-LtZomPisejSR4ZffcamnJbVpQMFXxf07rsFjVYB3srczsD2oXLh6ZBFDOqP6g5jOZLDFFPubKh4NPODMOEv4s1b74XGh15YqT39_LhHDGxykyXH9KslnrRzpE-oZQF-POitZEuQMV5WN2B60_R-pqMO1Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=eBHE7nyPzjuBKU__Q6tqAHbu90HEl1r_f1nyAM-Qpmm_kjrmiNxTNuMHA6_zdf6dL1sk8fWhvUFoK4_G5ok1aWrhCcv2J_FGW0MpQQYNZnH2wMmzIYOMUc1qd_RKzne5sDR54l27SzmhiWn3tQpac-n7h1LDoJma_UV4oUiL7QA8bLkmL2QkwGOODjgef_rbkG_kD7vOHywkGoY6mxpi1Pe8nMqVOGW6GI71auIdbtM3bcxVOLmBIPm-Js7_Kj_yIn4XQAZp6RfIKL_07cCqM1VBeacMOhkYe9B9mC8-9YVwncsIJhRZMlt6m2TeMoMwoLr67874GINSx7hVaw44XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=eBHE7nyPzjuBKU__Q6tqAHbu90HEl1r_f1nyAM-Qpmm_kjrmiNxTNuMHA6_zdf6dL1sk8fWhvUFoK4_G5ok1aWrhCcv2J_FGW0MpQQYNZnH2wMmzIYOMUc1qd_RKzne5sDR54l27SzmhiWn3tQpac-n7h1LDoJma_UV4oUiL7QA8bLkmL2QkwGOODjgef_rbkG_kD7vOHywkGoY6mxpi1Pe8nMqVOGW6GI71auIdbtM3bcxVOLmBIPm-Js7_Kj_yIn4XQAZp6RfIKL_07cCqM1VBeacMOhkYe9B9mC8-9YVwncsIJhRZMlt6m2TeMoMwoLr67874GINSx7hVaw44XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tF2q5QuCNpWQUG8PCfe_omcUQVzuZ7WjQByfe_eGpFz2PXNjhCOOzCGcw-nV-y7o3KJ8nBQp83gcAxrqV5r9-wfBuu7KGwLKEh4aJ0R8hoiRi_kiB0N_pctq7VCUc_Ijd2uMHUyQkMAQCY2wLKc6MHf5Czv1T_oO7JD8KPecL0tShwK3LV4pbL4gIOpSdqfMUtfRV-JuXaI1Ncpl6sdrIrIBduPyVnT0hHtcfQEz-peRw6909q8XLgBjt930OClCLey1EIBYlS6DAEYbIW3BTjAQqTy5pUSh-jl6z82pGHrZVYzSXrh-JTkh-YlUz1O2gI4_cdRlH6rVmDQLebnyyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=DLAwQvwwUHsEg1XHcjKcHRug-dpapqMaV8_XBzCUHCq3uULLbEp3aHFzA_eRIreLjUSQEUcKFn4AYctwD2VNve6RwyixWvMabKSeGeFTUsus1PHuj9_hlOlx9HxJjTg5sBolDQ7whXl_fpwSI2TzurtHgTY__Cdmj3kKQlH_AQFvGzHfm27vLDJNxq54JNuZZSMd-i3GMP0o3DwUbj7n3KpuTIQSeqBtZoDMT9g2IRM0tbfvSBEuknRAgv8bF3OzGIN28FZqV9_yPQGTLhDDW3V1KZU8ifjwyUC66W2n9ixOO6NVZpIAHfexgayMi4Vkv5_7Vdb1wEOnlpUYBRo6iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=DLAwQvwwUHsEg1XHcjKcHRug-dpapqMaV8_XBzCUHCq3uULLbEp3aHFzA_eRIreLjUSQEUcKFn4AYctwD2VNve6RwyixWvMabKSeGeFTUsus1PHuj9_hlOlx9HxJjTg5sBolDQ7whXl_fpwSI2TzurtHgTY__Cdmj3kKQlH_AQFvGzHfm27vLDJNxq54JNuZZSMd-i3GMP0o3DwUbj7n3KpuTIQSeqBtZoDMT9g2IRM0tbfvSBEuknRAgv8bF3OzGIN28FZqV9_yPQGTLhDDW3V1KZU8ifjwyUC66W2n9ixOO6NVZpIAHfexgayMi4Vkv5_7Vdb1wEOnlpUYBRo6iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqriV462nDBhTnphzo5dI70xCiUDGMdWDfUvtfe7AguYRPuvqTjaLynbqalDXv4lTeZqIrUSrACRRdc2jSZ-09nIZpYkny0Ostm05j-_VU3wM8hOxOgfYzAwq6Ja4I4vjAAsdnyQ6ZVxz5It2h5AdzCtIIR9Y6sAngNiJNghmggujABb1OsSCugEwF3XiJ6ADddcFIUBH-NKULZhuRxWyCpXbWa4dPNzFTDQ3Vl2E5sZ_W8gWiXxAHnk3jW_10ei4TFvllOQWq-rIV1jnyZui0-jMaMO2Elmep7cKw2I-IL5BTsUOntcDVrPI1xEX_dBg4ky-bkBSmA-k1Q1GvDUbVX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqriV462nDBhTnphzo5dI70xCiUDGMdWDfUvtfe7AguYRPuvqTjaLynbqalDXv4lTeZqIrUSrACRRdc2jSZ-09nIZpYkny0Ostm05j-_VU3wM8hOxOgfYzAwq6Ja4I4vjAAsdnyQ6ZVxz5It2h5AdzCtIIR9Y6sAngNiJNghmggujABb1OsSCugEwF3XiJ6ADddcFIUBH-NKULZhuRxWyCpXbWa4dPNzFTDQ3Vl2E5sZ_W8gWiXxAHnk3jW_10ei4TFvllOQWq-rIV1jnyZui0-jMaMO2Elmep7cKw2I-IL5BTsUOntcDVrPI1xEX_dBg4ky-bkBSmA-k1Q1GvDUbVX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOSByfIsTPDa8KYor3diBCBuRvrFK2W-6zVK3lObrxF7xfbaF55h5EN5_b-SQrbVPbR5NAaNNaXtjw815DTpo-cmzfGKY21f06_t23PkS3kZ9O-yTgfM6DiQF9qyFOtN6G-ahNJHF5cc8h8W1rUC7bsBofUM6gME4edzhnBP7n--GqRr84CbC77QaRshZlQ3O8RUcL31r7z1ATA6pcjG441sOTua2_z9yMvoIf0bM8zfEMnpgWnQ4UoIkPcO-RxDNT0OcjczFqhezDPU-K7LFiJhNLV99Jn-aBLbnC5WFY0hmKJ8iAj7orbl_436ftlPsF0fQPtNqCiZgzSBtSIgrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=RNYtSIjaarSk3R3xtJQ_c_GORCk5xW-gdRywIK7t-jTTENRJig4Fva3SrP0-FdvBsjR34NU9ST29o1fZrTTRi20kWt9gNImJPVpL2l9xIs706r8wOC8BfzS-cXx1gN3p_xel-ekBiWI13EveXjNdWVM6aL0QOeXfwnZyOiXShTU4oK3U3iTW4ucDCtw6v7j-83dgn074ny5MS8RDbCFnt4fbA5VrpdbZPnAHeKn6tgUH4CNEuwPD35J918v9QP1iqQ_m3CVRKHmS5qxSvblG1c1k1RY39Z15gc0fLL0tiO57ZPdyeDTTLHekrchrtRE1TtE6rtAwd-5disYdD_FhoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=RNYtSIjaarSk3R3xtJQ_c_GORCk5xW-gdRywIK7t-jTTENRJig4Fva3SrP0-FdvBsjR34NU9ST29o1fZrTTRi20kWt9gNImJPVpL2l9xIs706r8wOC8BfzS-cXx1gN3p_xel-ekBiWI13EveXjNdWVM6aL0QOeXfwnZyOiXShTU4oK3U3iTW4ucDCtw6v7j-83dgn074ny5MS8RDbCFnt4fbA5VrpdbZPnAHeKn6tgUH4CNEuwPD35J918v9QP1iqQ_m3CVRKHmS5qxSvblG1c1k1RY39Z15gc0fLL0tiO57ZPdyeDTTLHekrchrtRE1TtE6rtAwd-5disYdD_FhoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=aXkvj5URxIzA9Li4rUnrgklRwMQP7k-Bg2jZYmJFYSfjM9KPiIjY6n9foPB24H04e72tyc01y_mzUwHrmUnH9P1yN3mdtIhn3w46YWqyQ6ndvdK1fmavzwW1Mu2LPpUmh2TaN51MQKoWrgNlZ9qkxR-SCr2aT_Md7aeevraszhONLrRhyGWKcRexvCaBv1o6jo5LXklevjEEO7_d47W7jPitczDq5ARE-yhBVm6hCEy4cne5rHbqQbURpsYwvfaDMrjYiGO0gTg5xy6utzwZYeUTO-IiL36cJ9VS129batG324FkjR7JbAkqsTAompjyUoiP1OCO9UsglELGTIJudw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=aXkvj5URxIzA9Li4rUnrgklRwMQP7k-Bg2jZYmJFYSfjM9KPiIjY6n9foPB24H04e72tyc01y_mzUwHrmUnH9P1yN3mdtIhn3w46YWqyQ6ndvdK1fmavzwW1Mu2LPpUmh2TaN51MQKoWrgNlZ9qkxR-SCr2aT_Md7aeevraszhONLrRhyGWKcRexvCaBv1o6jo5LXklevjEEO7_d47W7jPitczDq5ARE-yhBVm6hCEy4cne5rHbqQbURpsYwvfaDMrjYiGO0gTg5xy6utzwZYeUTO-IiL36cJ9VS129batG324FkjR7JbAkqsTAompjyUoiP1OCO9UsglELGTIJudw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxnFrHxZE-HNaZ3siT-0NEQAH6Fj9EKTkFCWMJ2WclmBlLhn0vJRC2rtAicJFXq3wbJkAPYKbFdWmeR8r0I12HnjvEWDaQ11OqiFZMsJPtr64Hkagy0OwjKIem0Eu3w0uggc8RdGcruGzXVGVn97xprgquo7_Pz7gE4x88OVnm3S22yxFz1wVt_ZL3NRYNz_VdQOmREU05T9N9ysemhmTO3ebvduDXhWkwI55whyKjZUC4hFtdhBHMJoR7fGbwnV-tsZl__acXdYbLNRnVKWBfPd4tiR-3g6tZk8IieLiyNz6gpRRoItNTykwy1uvHdCHjQBb6qubwgoAqP81H68_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=esp-gQoDrUqdBhPdSR61ymtNTeVM9eL5N9ocYVJRvUzHEps2SBMoIvlEnGmGxCjJ-O-0n0_ZbAJnMPU7qCrs71AnOYYAx7ym_YOuos2zZNoDC7QXfiN50-93-p1On2_wVqBOzr2K4YwUvfEv8UD69-v5CXJV3oWKJ5GIh0THb53APxqo-GukLJyYA1BeV_VW5SjeGhsMp2KHhW-3wi2NG8lrjJHn8vSWprcwK9mfPaLqwuEK4JlxWf6tx9zPN6liBLEaPC1kE4KcFbmgH_WL7UR4rwbqqRsup6upu0kYksY1rxkofpX5Ck6Ug0akfiIXVb8uetcx2hkJr6oiakxe2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=esp-gQoDrUqdBhPdSR61ymtNTeVM9eL5N9ocYVJRvUzHEps2SBMoIvlEnGmGxCjJ-O-0n0_ZbAJnMPU7qCrs71AnOYYAx7ym_YOuos2zZNoDC7QXfiN50-93-p1On2_wVqBOzr2K4YwUvfEv8UD69-v5CXJV3oWKJ5GIh0THb53APxqo-GukLJyYA1BeV_VW5SjeGhsMp2KHhW-3wi2NG8lrjJHn8vSWprcwK9mfPaLqwuEK4JlxWf6tx9zPN6liBLEaPC1kE4KcFbmgH_WL7UR4rwbqqRsup6upu0kYksY1rxkofpX5Ck6Ug0akfiIXVb8uetcx2hkJr6oiakxe2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=TMBAiebcQbbdChNRKhuarJD26_n8HQJrtmU-k4DxGmpAiN-Vl3foQRT3_i87pK4GIrkRuHcuQPhpHYfYWSuccND9J2u7Un7lQGOWCZeblKlYTs2MUXPtEbkwQRT9mtaX9hASQkMUAla_sRvPSoYfEnEQlO91Km8nhwpp0s0hWwD9j_T9HVCh6VKpR_Qp0jNihFDWaV2Faa-P2kUknbmiKh6GabgZn93tN3XZGoNuPckO8OGnFrN7AXjLc-_9fZ2_n8Onw-OmksMSd0xXyyV8qaAQRY3x09QJ50FTcbWqyEXs88gol1Uq1YmjtC57ues9cjX0bm-JldvuUAmltw3QtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=TMBAiebcQbbdChNRKhuarJD26_n8HQJrtmU-k4DxGmpAiN-Vl3foQRT3_i87pK4GIrkRuHcuQPhpHYfYWSuccND9J2u7Un7lQGOWCZeblKlYTs2MUXPtEbkwQRT9mtaX9hASQkMUAla_sRvPSoYfEnEQlO91Km8nhwpp0s0hWwD9j_T9HVCh6VKpR_Qp0jNihFDWaV2Faa-P2kUknbmiKh6GabgZn93tN3XZGoNuPckO8OGnFrN7AXjLc-_9fZ2_n8Onw-OmksMSd0xXyyV8qaAQRY3x09QJ50FTcbWqyEXs88gol1Uq1YmjtC57ues9cjX0bm-JldvuUAmltw3QtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=pyqIGoNgNfUHAfkIMz1-_gLs9Nf8KqEF6PqDq7B52E0yfIPJlLxoow21HtymdxZp5erXdO8twzArKsXSqMJSYQG7IUHpUlnozhLKOVuPGOu7B_orILKdjxx2umI_i8WS0sK98Da5oHK4-X7iYYKy78s21WaKEgCnmL0Bc8A8ZlplkvF3UIQykbkWIgzkonba8nlJswcggw26lhK6561gJKkPmMrFB4M0xFOhmkVBBWt_2Ra_1-wWFMR-PR9C_EhbmMoPDm6YHQ8vwFT988MiMmcqLlaW0OcSrIguRm1tVxb8DYkZDXKRV9H5vZBMwj95czvtpiJODbSXL98k_SR-UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=pyqIGoNgNfUHAfkIMz1-_gLs9Nf8KqEF6PqDq7B52E0yfIPJlLxoow21HtymdxZp5erXdO8twzArKsXSqMJSYQG7IUHpUlnozhLKOVuPGOu7B_orILKdjxx2umI_i8WS0sK98Da5oHK4-X7iYYKy78s21WaKEgCnmL0Bc8A8ZlplkvF3UIQykbkWIgzkonba8nlJswcggw26lhK6561gJKkPmMrFB4M0xFOhmkVBBWt_2Ra_1-wWFMR-PR9C_EhbmMoPDm6YHQ8vwFT988MiMmcqLlaW0OcSrIguRm1tVxb8DYkZDXKRV9H5vZBMwj95czvtpiJODbSXL98k_SR-UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=iWrLAY_BgAUG4QT_8x8MaAnFP63wzfu07_ri4NjYMdDL4q7x5tUscLm3wcRAxzUPlmhPc4RdORGA9OnQD33O9m1a7lfurq1gnnzz3Wc8T3WXlsPBeCl3FG7iKRypLdzqzhLEIjZrru7uIiisK7hgmupFczcELhmwSMdQTlMQG8oCYmgMDvzs11M7X3Ss3o6DFU4UtC0pncvoax0Wb7eq5Efivearl_HjMmRFhBgcjmezbEEJJ-WABShFyRYwY_uANomIz-6F8xO-IEVFmXC3Er4a0LoDC0fA7bgIeR2otUqKW0Sd3MxoRo_8MMqNVTPI8AHeMMx217fTmfPPZfKp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=iWrLAY_BgAUG4QT_8x8MaAnFP63wzfu07_ri4NjYMdDL4q7x5tUscLm3wcRAxzUPlmhPc4RdORGA9OnQD33O9m1a7lfurq1gnnzz3Wc8T3WXlsPBeCl3FG7iKRypLdzqzhLEIjZrru7uIiisK7hgmupFczcELhmwSMdQTlMQG8oCYmgMDvzs11M7X3Ss3o6DFU4UtC0pncvoax0Wb7eq5Efivearl_HjMmRFhBgcjmezbEEJJ-WABShFyRYwY_uANomIz-6F8xO-IEVFmXC3Er4a0LoDC0fA7bgIeR2otUqKW0Sd3MxoRo_8MMqNVTPI8AHeMMx217fTmfPPZfKp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=dRJWDJzDS-WzN_uRe8xlobGh3nBdSdLdBE0hQzMoHMhF1sChxAY2IP4EbAtGstjpHDo4gtiUjqN8wKPiIdMJRVXJewUuKDPO4HzLRM0glbhQo6b1xCUclt5eVb9oVYLba9m7DHnhT5rAI8QrmQu8HBXHx2FUOwjK1TkyeTjJ-Li0qRXoD_0mDv_DqBrgkQUEXjPP5a3d_riMr_E_-YVIlekNsM7FdsyHiWy7WrjjGakbll0j0nuPugSXf8YUM7oK3-yvWuCmTmJ9AMCNmaJbjucuWiQuUWCEIqM3XkQ0_k1NU7z7OSDbCsp3gZ4Y18_q_9Bneiu40AsLbjmjawlQvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=dRJWDJzDS-WzN_uRe8xlobGh3nBdSdLdBE0hQzMoHMhF1sChxAY2IP4EbAtGstjpHDo4gtiUjqN8wKPiIdMJRVXJewUuKDPO4HzLRM0glbhQo6b1xCUclt5eVb9oVYLba9m7DHnhT5rAI8QrmQu8HBXHx2FUOwjK1TkyeTjJ-Li0qRXoD_0mDv_DqBrgkQUEXjPP5a3d_riMr_E_-YVIlekNsM7FdsyHiWy7WrjjGakbll0j0nuPugSXf8YUM7oK3-yvWuCmTmJ9AMCNmaJbjucuWiQuUWCEIqM3XkQ0_k1NU7z7OSDbCsp3gZ4Y18_q_9Bneiu40AsLbjmjawlQvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQtan02IZhCynEETaReLTBOWPSI18Qj4ToVFE6y8aZfBNShGGZy-h1HdCAePqjNkSgBprO5Sd_DclYrWMiiQMWt1urLhrE2srOY9r64ysnVNx2xq86_mmV01URlj0dIzgyOg2Itr2GUrzlyaiVvDnu50wqMm1I74HWE55OXDJuWtx4rQM7ajri4OgyWG6zp5KMs9fD4U-ko1cqrGUYPFh2GsIp3PBrYdQbhba07-8nsHxr5aw8dmiF2eZ4xgo1w_E46SdTT6f6CxRdl71px-3uVsb6MluL-5gmgZ9Or3Q0OXlW9_5B5m-axRhs_VF00conNAMUZ_Zy9vi73oNXuZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6Yn6psLKwTpwpyiGXwkMKJbWcYPgaObGdd8SZEhGA14LcCFuodCsP_vWU2qaRJtP1R_jqlTpKJIASsYgUoKNdupS9Gkprj4Uy6jUbKSCJvvEEVilLk8JHqXswo7OLhmyzTwwUh41Xk3ZDCBN8Y-0oG-IkyKqTC1RAGsezn4noiqVxb7ozQrxQ6FJn6O8w0bB02nUyRLdohew0USr0mA6u9BIJf2YcHRLY2_jDk3ZWSZKkm9G1_CtG4B-XbmTkuFVkDvFOQMbWl7Wtcse_jQrr8QkX1yatw4Z1bUnDU1MJHekFg0SI00QdqaSM7I_JlbSpz_heRLv2bis0tJ8Yixuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0sMsul-AfqjNwri1hwmVTVumPpzs7KVxNjfCbDz1UlVtYfLj73KC6_Av1BeuaDhM0vsQQ3c8ELm0U3FvOVX3nMsLGsAelo9LPTrhjlMkOXmISoZisy5Vb9Mp84_tIQe86wrCUyEvvq6H2tc1TDzJXQl4JMFYz26WfXz_hQhaW93ZlvB6EDIAiziPlymcWCQV1v9obapNXXSsFBAMedI8F9gPc8dq_I1CZt_Qx4P-B-DyvBy1HPtYhZq12opiuUeTzuvF2ek-hvrvSn5kpyGOymTAG_psphaMxww97g4-zCqOyQ6lPY630LK24yuEfr7YPJxE5h7Mw620GmDI82SuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=reCCwwfdrc7WJ4u7GQb2b46DdEcv-t0Qsn1yhSHGtFHckYou6xTFvLjTlI_a4drmRD8LpsiFRBlmUL-doReoIcxaJgotYyxlqz_Izj5Za8R9wb3z53MjVv1MnHIfMOyUcgkYBt-9oVeYM89TY9yhjSAcDOau8_fkoMJXtqALHvBrUP79o20d8wXg0Ki2Gzb0HiVbrTlVPwsnbc00e8-fD_1_vgEb93GzbF2pR4JlZicg7BzJIrwdKwInEYsxSUZvdIbN0hA6RAZPkFe57glZ-3UdOkDrpBlbPAondUs90L0Y25N-OvyX7-q5zYdOYYCuaXZtTFYVXANSggHOIxBIGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=reCCwwfdrc7WJ4u7GQb2b46DdEcv-t0Qsn1yhSHGtFHckYou6xTFvLjTlI_a4drmRD8LpsiFRBlmUL-doReoIcxaJgotYyxlqz_Izj5Za8R9wb3z53MjVv1MnHIfMOyUcgkYBt-9oVeYM89TY9yhjSAcDOau8_fkoMJXtqALHvBrUP79o20d8wXg0Ki2Gzb0HiVbrTlVPwsnbc00e8-fD_1_vgEb93GzbF2pR4JlZicg7BzJIrwdKwInEYsxSUZvdIbN0hA6RAZPkFe57glZ-3UdOkDrpBlbPAondUs90L0Y25N-OvyX7-q5zYdOYYCuaXZtTFYVXANSggHOIxBIGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoYPnloSiAkRGK2AhNJCViBLQMAm_LslsVaccnHIukqpwF8UASr6X0nJOdL2_Pu4PZwypZbo-DQnd9-FtgiG2SoCgu0fY1qBAILL4imDSfdRz5jNhjB_iugCnG82D4Y7HccCG8OeyhqqtrOrpaLSgJmR6ikGsqP3sJQ29bfVJBDQuVF4JyFTCBGX_fmpL_4gEGbj3wV65M8bZe-ExVnt94LxcQ8fjP7BUSS1m3J129V3noI1k_G9i3YtlXMXMDTIHJYpWQ27T9_oB4qRkJKX8NkXh3PDy6tMvUwzBvzNFCA_0WySQsJQXPXbfMZC4Q0QjWXs3cdxXutPAuHYGSU5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=isap8OSZYzz5WjasV6u4kCuIPbwmh70YOZmQqOL0JccqpR3g5i2u6R-kfoznVwF43JRbiPSDk9LVtHl1X4EWkw5Dz1wn_sOesazJtPFqWzCKdnEB83xUROUHGJivWXWCL9KjLRb72DLAi6KQGypKndda0I77wPSt0-7SWRQRT4S06-Rb7XriTnlAbSNvYMzYr_7US1WPpHsS5W0yGHvyPTKZWwb7JpGYm5mVsn5WzXRrj4AvZOwYxPjsWyT9Qco-MbaEKIP3cvDg6fsiGvOYGNaSGF8t_bf6QqR7pG87Q9rG00Rq74rM6t5bcNi4z1b6_se03cfKHwwxjyk_4-L3Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=isap8OSZYzz5WjasV6u4kCuIPbwmh70YOZmQqOL0JccqpR3g5i2u6R-kfoznVwF43JRbiPSDk9LVtHl1X4EWkw5Dz1wn_sOesazJtPFqWzCKdnEB83xUROUHGJivWXWCL9KjLRb72DLAi6KQGypKndda0I77wPSt0-7SWRQRT4S06-Rb7XriTnlAbSNvYMzYr_7US1WPpHsS5W0yGHvyPTKZWwb7JpGYm5mVsn5WzXRrj4AvZOwYxPjsWyT9Qco-MbaEKIP3cvDg6fsiGvOYGNaSGF8t_bf6QqR7pG87Q9rG00Rq74rM6t5bcNi4z1b6_se03cfKHwwxjyk_4-L3Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
