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
<img src="https://cdn4.telesco.pe/file/IyB3zwg63yVXxj-TvHvl4uTXH648JNkwsWEjyWXL4h4iHNuhSh0qhnvbHwmcjly3aLcKHNp5dSm7s35HJ0W2HUnMz0Rn0l3oftAfWieCAPcZ_4az6EDHp5fJVTjEpAJiTZjR7lazRbuoHe9FvfQez7NbH8SzhhkLPYT6pWUKeHGZif7ZY141EQtjTkcB9F6JQFidq0AF7_ig5CPsExUp1i921XuthlOylNMlaNTTiTx2bbD_66qA0e8ZqzM_cKwa5M0HMHGpi8VDMNaijFLR4XN0uXOsaf3fPqnt9L6JND-mafSBJPZoFWKWReBQxXf_kYwpOcbaaTJ7ZRZs6_nxLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 166K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 20:31:51</div>
<hr>

<div class="tg-post" id="msg-68356">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
تعداد قابل توجهی سوخترسان در حال اعزام به خاورمیانه است</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/news_hut/68356" target="_blank">📅 20:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68355">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=jFjQISafE_pX9Kso-Sd04CUMuuTYwu-P_rGxQOv_KqN4Z90wzzYHom5NBkykIdXySqxfnPVK_AbZx8On9IMRjOzeeb4ADn1zMXAh9J3zGpYbmfXtCThgUqn6B4F8e2NiNCMwmTYWQWvsL5Zg2x1Bg6__5Ow70FgJjN6EEK2aVH3BkAy_150prGhEvjSqsHXoL5h1ssGJ3bUUDi0d-HPCWmSJVTGva7TA0lVZVIEg1m_1h2sA9UN1adBCYeaqXDegzc0v2nsJOzXO0waIxfvQeZU5nKkh_luCgTPCwZUTzthoR0f_LO1YVlMR04QQtYw_OO0uAppTms1piOwdtGjeEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=jFjQISafE_pX9Kso-Sd04CUMuuTYwu-P_rGxQOv_KqN4Z90wzzYHom5NBkykIdXySqxfnPVK_AbZx8On9IMRjOzeeb4ADn1zMXAh9J3zGpYbmfXtCThgUqn6B4F8e2NiNCMwmTYWQWvsL5Zg2x1Bg6__5Ow70FgJjN6EEK2aVH3BkAy_150prGhEvjSqsHXoL5h1ssGJ3bUUDi0d-HPCWmSJVTGva7TA0lVZVIEg1m_1h2sA9UN1adBCYeaqXDegzc0v2nsJOzXO0waIxfvQeZU5nKkh_luCgTPCwZUTzthoR0f_LO1YVlMR04QQtYw_OO0uAppTms1piOwdtGjeEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماهیگیران ایرانی یک پهپاد انتحاری آمریکایی مدل "لوکاس" را که سقوط کرده بود، از تنگه هرمز خارج کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/news_hut/68355" target="_blank">📅 19:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68354">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXXQjf6WRE1ISMxo9dagc4Krqqt_EAQ0eVtvezu1o13439Euwy7ZQcvmsUIvRcvyraR2l3bKsDluOVBul8x7rB2nV9dU5EkcqAmXQuqavlJ57qy8n6JZilycA9uNefLIpNQyLOyod1QzTgcNLA0p5hphupyG5dXDWYu9uisRQIo45s2Ad_a0T5Sshu-0ZIAQBAQO-DBD4xgOyUL6LFKcj0XUAgseDpNjSpcBnh7ILyxJSv2KVlGn8QkHzQL9CUol9n3MQFc7eYJAlTPCEe3U-Yc5LwyYzUtmnxtQ9lLq6FpCvbDiRHxdHiAV_Vx2PCTmNdYixg1nXP6geKPK5v_nrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.
حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن به این مناقشه قرار داده است؛
امری که می‌تواند نقش احتمالی آینده اسلام‌آباد به عنوان میانجی میان ایالات متحده و ایران را پیچیده سازد.
پاکستان که دارای تسلیحات هسته‌ای است و ماه گذشته در دستیابی به توافقی موقت در مناقشه میان واشنگتن و تهران نقش میانجی را ایفا کرد، سال گذشته یک توافق‌نامه دفاعی متقابل با عربستان سعودی امضا نمود و هزاران سرباز پاکستانی به همراه یک اسکادران از هواپیماهای جنگنده به این پادشاهی اعزام شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/68354" target="_blank">📅 19:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68353">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_Tjs3yAObjwngS8Hv9lNgInYkyQ02hJegwsUiOdEc_5z20vF2frkrE2LQFcG5N52C_zBkT8rvq9hXo_4_XaTK9MkY0QHWz2cridtWL8dTKnmdeiO--4Id3IrnxjjuBGltKFwzbn5W8Ug_YtwPYZ7xfKoLVFz4sfssinmqEi3J3H3YAjV7B91f3dyDe-nhZWAZlUwJhKabqbNJ-k82BwS9aFggHOuFJlYrhol6CUABjU3FLhbrrY4JlrBb5xv3dicAnFAG8XUppUCUuqej23igycAJzswwGRhdYVru5XevEV727wBvnELQDVk_0yKW6olVfvcWqSAmFl38o9NZ7UAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای ایرانی مدعی‌اند که به پایگاه «التنف» در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را اسیر یا کشته‌اند. این ادعا نادرست است.
✔️
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در این منطقه کشته یا اسیر نشده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/68353" target="_blank">📅 18:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68352">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=HSMeJOLsNgbUEBVHsApLBZJZaZokoviHTNJs7ThQApwHoT-nCnnJiO60FgrTr59QYlaBuKELyzifNgNgM3plPa23PWrrM3aTZuQ1B3MhHNXka_YRUqMPUBX5eQxAjGVj1NJVgKTLI2DNVBYh0fjITrVNOUtcfvXEO2MjMTsYf_B2pfPdElTi-_gUicfyqTOMJvEsKlN16BaeOqs-iYbZZIzChmOdmeAcBzVr-VT_3WUMowt5-S9M8iqP_HvGejNNX-5d2pG2PG2o1XtpQ45Awri9t5m1-CCxbsDAQrD2Rf4X9BzT1v0F2J1q7lVQbw5zT0Oiww8UaldEsDcYTbsRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=HSMeJOLsNgbUEBVHsApLBZJZaZokoviHTNJs7ThQApwHoT-nCnnJiO60FgrTr59QYlaBuKELyzifNgNgM3plPa23PWrrM3aTZuQ1B3MhHNXka_YRUqMPUBX5eQxAjGVj1NJVgKTLI2DNVBYh0fjITrVNOUtcfvXEO2MjMTsYf_B2pfPdElTi-_gUicfyqTOMJvEsKlN16BaeOqs-iYbZZIzChmOdmeAcBzVr-VT_3WUMowt5-S9M8iqP_HvGejNNX-5d2pG2PG2o1XtpQ45Awri9t5m1-CCxbsDAQrD2Rf4X9BzT1v0F2J1q7lVQbw5zT0Oiww8UaldEsDcYTbsRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در ۱۶ ژوئیه، نیروهای ایالات متحده با موفقیت برج نظارتی بندر شهید کلانتری چابهار را منهدم کردند؛
سازه‌ای که بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در دریای عمان بود و دهه‌ها توسط سپاه پاسداران انقلاب اسلامی برای ردیابی و هدف قرار دادن کشتی‌های تجاری در حال عبور از تنگه هرمز مورد استفاده قرار می‌گرفت.
انهدام این برج، مستقیماً توانایی سپاه پاسداران را برای هماهنگی حملات علیه خدمه غیرنظامی و بی‌گناه کاهش می‌دهد.
علاوه بر این، این اقدام از آزادی کشتیرانی در آب‌های منطقه برای تمامی شناورها محافظت می‌کند، مگر کشتی‌هایی که قصد نقض محاصره دریایی جاری ایالات متحده علیه ایران را داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/68352" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68351">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=NqgATHzKZD3JhSVgdBvg7U91j5bpSOH03mqIs12uhf-EHBgfTCqGNpI7u-MOQotSxkocTh4LKUPA_FcaxHx6CJeXznuFntTKeKKNvWPiH7ElyuuDwmbox43x8v6L8DbIsEljO60z0ghx0O-Qy-SzEbWnCa-E6Uiv1UDeHuOQjBwsbdBW_8bv76tL7L5yhArfilfybgAzHqSL9e13d9K7r04B3cnK3lmGdNPcluMJesSOCD-7j5GjSLAUUAxLdR4nLq7sAy7fHC7jLZBg7UVanROLvR7BpBws8B_X51ZRdUNVk0kzRNJ_nCxwcREmiUAcZ_mbg5sld0cyRdNzx9u21w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=NqgATHzKZD3JhSVgdBvg7U91j5bpSOH03mqIs12uhf-EHBgfTCqGNpI7u-MOQotSxkocTh4LKUPA_FcaxHx6CJeXznuFntTKeKKNvWPiH7ElyuuDwmbox43x8v6L8DbIsEljO60z0ghx0O-Qy-SzEbWnCa-E6Uiv1UDeHuOQjBwsbdBW_8bv76tL7L5yhArfilfybgAzHqSL9e13d9K7r04B3cnK3lmGdNPcluMJesSOCD-7j5GjSLAUUAxLdR4nLq7sAy7fHC7jLZBg7UVanROLvR7BpBws8B_X51ZRdUNVk0kzRNJ_nCxwcREmiUAcZ_mbg5sld0cyRdNzx9u21w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی باقری کنی، معاون امنیت ملی دبیر شورای عالی امنیت ملی:
برای آنکه رهبران آمریکا و رژیم صهیونیستی از وجود اراده جدی برای مجازات خود آگاه شوند، سریال «مختارنامه» را تماشا کنند
😶
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68351" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68350">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=GpTdl6DSucgvKXxZdvbdNZ9ugwPyk6Rs2g1ZF6lC4_PvHVfNCgzJBY-alb196EW156G5SOHHe5Uc8b1Dlq6Ft7Sb3kXfVtjR951qLrNXGNYmVuJP6uEWB0_bGOp6bIo5ZamqmvN4HIcXpMJFcnnGJi1_I9h6HhxhaFT3L-WmVtgAcMM43kEyOz5xJdp_dls3pnrsed5AZPebP3Fi7kauUIQ9lCzuTz_Sau4I7c2jpRgs3IyOWGxZM-hozY_MtaEbGr0JK5vmHpbPBeM1HePlu-EJfnzznMyhNH5v4B2xniSPd0z5JPIgaxBbzUFyyhIvPeEom-hsggIDEM7vv57W6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=GpTdl6DSucgvKXxZdvbdNZ9ugwPyk6Rs2g1ZF6lC4_PvHVfNCgzJBY-alb196EW156G5SOHHe5Uc8b1Dlq6Ft7Sb3kXfVtjR951qLrNXGNYmVuJP6uEWB0_bGOp6bIo5ZamqmvN4HIcXpMJFcnnGJi1_I9h6HhxhaFT3L-WmVtgAcMM43kEyOz5xJdp_dls3pnrsed5AZPebP3Fi7kauUIQ9lCzuTz_Sau4I7c2jpRgs3IyOWGxZM-hozY_MtaEbGr0JK5vmHpbPBeM1HePlu-EJfnzznMyhNH5v4B2xniSPd0z5JPIgaxBbzUFyyhIvPeEom-hsggIDEM7vv57W6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم‌اکنون وضعیت پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/68350" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68348">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHu-kqxgikpXkUo71iT_LhLcGkN0J7cDY6quTV1VBHam8KJk0SHLdHZ8F6h0ugKDqa_s73-QM3DEpwe8a1XbGeILNYA3SA0uagbT13Ce8UVZNozCuvaRG-2DQHMicflGTHGqb59g3xVVFRQidTLj2SalfC1hQLWTJ5NASEu3NURX2cWnhV6b39F_DG_YHGk4XZeuLVE31UTqJV4nyNOyxCq2qLKsmRjQBx2RjzmXfW7pGt70PA-mhNrdGxeq0szGIZ6wFWKXzrcejesdLiykBvpgCwIVQw8oXPN8hWY9If56LWvG3w2n8xQDHIzOG5aII_u_2PMl99cr32TR38LZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6De5kUpyXRL1NqiYJJ1cdw1R3GsR52uj2aLSEHocYqOMVxqM2NGSwxN8LVuH-yvnTuexfrz5BC8BJQR0qIqG5D8Z0OKzWKqpsdbTEOiPyTpt0egsAzQZkBxpJdIOx8VnzpQqoBCQcQ7p9z8odHyTFg8jWmyPQjhcTcyeBP1z7Dv59Jxo2ocmazhWwS_AOREShrHhDX55NmSoyK4RVlQz50NM4P8ogI4r9Mfuiw9bVPkPlxzsaolbLgf1J5nHusd9qrz3LUkJqTsroji_4FlehxmRvPlfxVoV0tLxrKIXX11BC8kPic6RhOQzZHb03Lz0rxBahT12NP3huiAGuM7Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدون شرح.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68348" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68347">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeOhbH0igCJnnENwNcnp-RWLBwwNVLlGQL2l_8V5S7OC-G8X-wwYlks7T0GvscnQaTpueJZvGXX3iFJJnyGRSPO1dbh54LRoS1ttLDRi1V96Esxn-6DoplkT3AZ0U-hayGoGFCQOazGvC04UtOSXhIyzWq5iYT1S7GhwBL4RGT2SupYD5D8MxsUfemBmYke9qbpFXE-vvbrbjL22ndbEcTOv0DFqwlLXnbgd4qRRBgTUsX6OabdYdVhUffHm1Kj5AyUwu4PS3Wc1txn1gNtPmvtoLWqrDZHi-9BtXv7QHWZlo_25Vbz8aZ3xmeFSDSLKLqbKdIe2quavR8bFZajnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سید مجید موسوی:
حملات موثر و هدفمند تا زمانی که صلح به سواحل جنوبی و تنگه هرمز برگرده ، ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68347" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68346">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2_AhHecTZ1NbIKLVSYm3DsEifTMZ_9TSU6kXO4fWXeMs3hD2_ArJEdaXy3ciQmNj7V_xzRcyn2FUO5V0g39cSHDBADV-Xai4_BRouYVE8U6yygCV9cTtAg987Hv9yf9ALYS5sJJE5L8Acaw3hsiF2geBJ0WGf0nonnKsuFDcT73kgHj6l8EMzzXd4IKPaTJPyvKF8O09x7HzzOp-FqykqyKjufanHl_T_SUCG7gnPluPs-vWjy-BvcaaxDYvh_SdSUEdadbxPDrq7VCS7LwyXEJAfSBvpyrsxZc3QHvoSewiDPYwWrZ1zITH82WAiw01Ejdk0Zc4o_FO6BKelrGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از قوی شدن احتمال حمله زمینی امریکا؛
بسیجی ها توی گوگل لغو عضویت در پویش جان فدا رو سرچ کردن و این جمله جزو بیشترین سرچی های یکی دو روز اخیر گوگل بوده
🤣
🤣
عرزشی فقط زورش به مردم بی دفاع خودش میرسه تا اسم امریکا اومد وسط همه از ترس ریدن به خودشون
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68346" target="_blank">📅 15:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68345">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioxqVO2YppG9C8xOF16wAPWGeeIeVUjpgy4JKIhhW_0oG5I9As4S-VMBUIHlOpoN64_-75CAQVT4mEWKG0s7cha5LuQIJqrwCY5LxgAg9bOIjzSVyAlqbFQ0kH5VIxqotwyKX1eq-bZAGRvquGe4xihHZiKHTLgeEKUAWxv0WSEkYqR_qHW5_EYvm8NJpFlLv7G1A8IcvmHab66Ru2P4CHk_GS5Qa7NHAx-Ck-ti06QDEkiL_ANFU0oSnj9m3lgnpOQ4JuJKMajxiIS7Pvh1rs9Dy8lFUvbF_SK-Hq--SkMjccC3E9a8cli6etgP9owjMWvnZx1-vkHSM1R61lCmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
همچنان آمریکا در حال انتقال تجهیزات و مهمات جنگی به خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68345" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68344">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=vlHyO-eaPiZGLoGgbMDESPcp4sQRJ-Rv1kReuWerZb-klPhWOxvst6OWzwaaiJI_HMNiO6vMsG86yuwKhtxDWPr6s-mP3cZxpX98YTAFRzx8qlHzHX7RoDQFks_hOrNdHZ7N7_atLT8fnliiYi5UEfX2S6FSD1aRU9S9ndbYqNfbusTkR2L8d-wZKSiE3zfAWqw__Yp3U5zJcbGhXVAWr-3JsaCBbRK-ou8WpTO_FbPCqDEhqTmGwiWlZdPVzeJ-GmOxnTpqKrUirRRxewXmj5zziKAROrKvr3Ctvy87S9Y096cCSpVL-0XTMFCZfj61mRWTMBa6PBMjBHvVqMCfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=vlHyO-eaPiZGLoGgbMDESPcp4sQRJ-Rv1kReuWerZb-klPhWOxvst6OWzwaaiJI_HMNiO6vMsG86yuwKhtxDWPr6s-mP3cZxpX98YTAFRzx8qlHzHX7RoDQFks_hOrNdHZ7N7_atLT8fnliiYi5UEfX2S6FSD1aRU9S9ndbYqNfbusTkR2L8d-wZKSiE3zfAWqw__Yp3U5zJcbGhXVAWr-3JsaCBbRK-ou8WpTO_FbPCqDEhqTmGwiWlZdPVzeJ-GmOxnTpqKrUirRRxewXmj5zziKAROrKvr3Ctvy87S9Y096cCSpVL-0XTMFCZfj61mRWTMBa6PBMjBHvVqMCfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی، تحلیلگر ارشد اینترنشنال :
اگه حکومت تو 18 و 19 دی مردم رو با اسلحه قتل عام نمی‌کرد، مردم خواستار کمک بین‌المللی نمیشدن و الان بچه‌های میناب هم زنده بودن؛
الان هم اگه سپاه تو تنگه هرمز به کشتی‌ها حمله نمی‌کرد، سرباز‌های جنوب کشته نمیشدن.
جنگ طلبی سپاه داره کشور رو نابود میکنه وگرنه ما کشور ثروتمندی داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68344" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68343">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
در یک حمله غافلگیرانه به پایگاه آمریکا در العدید قطر یک سامانه راداری بردبلند و چندین فروند سوخت‌رسان آمریکا به طور کامل منهدم و به چندین فروند دیگر آسیب جدی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68343" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68342">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68342" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68341">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHLLfoI3Z-JTjxWWm95I9LkWX-h0qaYZD9tzQbbZBcVUVaskEV20U7GAYAkr-mWh7bTu9gAgyfuxwwoO9Y457u08gXm5GL_w4T66QPwRdlhMAOZKWIss4cTCNk9fPTTukDujKarq3ssMwhlmo0f9_AILMwS8Bfk0R9Rpfc_BuWtgJNuyPexjfxXFHSSDTy3WdFIBGtzHMhpGb4C0WkZ1AJUEzdzG8ENIm3LwslmImhfTR-xjRVfHGeDcGINjPChJay6-oJEEkf_ZuGTvySLgyc2BnD5yUbjO77Z4mInGbr-zdlTyd8HSz91IQq3EuB4VTr87xTRVlbhUgGmDcKlaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68341" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68340">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی مطهرنیا در برنامه «با ضیا» به بررسی برخی سناریوهای احتمالی در تنش میان ایران و آمریکا پرداخت و از احتمال حمله زمینی و نیز مطرح بودن سناریوهای دیگر سخن گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68340" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68339">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسلیت به بلاگر های چابهاری!
برج کنترل دریایی کاملاً فروریخت دیگه نمی‌تونید باهاش ویو جمع کنید
🙁
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68339" target="_blank">📅 13:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68338">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn5TQD-dCgfuSV2W5TNDbOMbV_ZL2oVcg5TLAL9GxBVNqKusEMM8tlv5ljEs270YSRmN8wFu8weocjHqQcd4vjAdlYbfUlrMUCtURXbpEYV-W_5_2noEdWlCKg_Ic8avQgtkpX1AcdjajTtDMz0VwNSEsOyKflIUlHg0h1akTd0c0FkG7_Z6k_EEBFWGZd5N12amNZ2URAj9Q7ds3WEQzeliHhqcZlb-ChHGk6T37gHYGTnnkxu_6Crbfdb7sHkDGnh62wbPa97O5PcB9QMPXkrc7FUUELicyPz9y4tY73MTfe0BFOD4BrJ_IghbYTsA0WYP_ecy2rT5drznNsxurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دقایقی پیش یک فروند نفتکش که قصد عبور از آبهای عمان را داشته است مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68338" target="_blank">📅 12:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68336">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MjBCDUoqa4p-VAonaxDpCcWNIhj6ZCBoSqi3dTcLotUhWONmE4uJorGwDCghwggRpPB1FP-GyIluJFsTbaeef-pHJYKgB1WZrSlKt5wpXoEfaMr9Mew8Bz7NGy-TUDa7O1awkgdO_e4P1rw1TWPPwErl7_Z3PkCfyR5srAxcIHfvFCVvlu0KSHVlwOW_w4Kp68oDmqHTDNIk4t-Szv5a0fy5vbfzlRZ6iO6nvKYKySagjN39XmBoh0-N6k7a1XPwUVMtXWniLsC3OA4TCE8hTGt9goFdOxpIVS2dqqyvkvIhoBh3kozFwyEwV372J5kvx1n8iViHxQkvyI7exP0l_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R41x1LdjwrSetQckUnmTPRnWBN7OTM3tpuAYG4OH7-qVVcclfilpUhKxeHRjweL6Taa_JlGJCT1-A7HUcKOffmAxa0cnnGA_1c01tMO100_X0A46sS7FtlFGV7BS9HER0BwxUU-5rkOYI-Jm1s8a84dp6uOz_x2r_XUPUstbjyRfqKMycJTkHVlAZS_1Le9r3JuOBSEuXKL5F3OWVAeOF1LNky-NR0a8vLWgt5mIGx9psbTvo3yrIaJ4AUBgApmE5Wc0EgjFuKSe3_WlDNZcyqynYgXhFcBedWhLe3umJ08NwHeophF3lYJv3jCLy7fsVdSnbtTm2XiUvq6Up-Vhsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
هگست وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد!
الان فقط یه خاطره از این برج مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68336" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68335">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
⏺
پل گریوه؛ مسیر بندرعباس، خمیر، لار
⏺
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
⏺
دو پل مسیر کهورستان، لار
⏺
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
⏺
پل روستای مارو شهرستان خمیر
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68335" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68333">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPomUYbKTqXmPyOfXRd4glbNhJ7AqivYBU7noS5a5qCUI7X6BM2PI1UI9tKJc5WjVZfNQ_aVDRWosL2rf_iwd3teKw3f7CTlUGiYKiE2rfoKLaLIj9oESb8V1q1eRhmsLx8WFMIb143fenXRJ9P6Tm4TivpKH0P6wAs2LrevfWsBQmbOxvleVkNTCju5ArCJj3cXRe1Fn8S7yfaZBatHOqGzDgTqkQjdSn9T7_RvEJQc5_WjZH0UiTaeM885-Liic0SDgg5Sd0gKJWd10zWNIbxcAAjP84N8y1HXue7eIDwZscLVRTauBNK7_VcLE3Yxq3JafoilE6E6pBKwOul20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4SelQwOa3pwRUaIv5UD1TuXtnWR04zHF9JRsX5RlDhHX_xc6QbnBEo53ENNxswCH9CyKP53L8bhSwMQOXcQSYMVdOt94rJgQ9mI7YL_T8m6bz2CTCakWkqIK4UAuRijzYKwKPvZZxx6njbieiv16OtFkFo5NJ4jQ8UMCwigOrM0T1Qa9t2m9qLRAZMQGcHbj5ZEppHOLtuX307rnedJVYZF8rPKkME11lb3pC9h3uk59bRZwPzjo0quY9Gi5yMMwVB1-LE5i1MvVLYKWy6LmQW0llPf7MUlgWlAL3wDZklj7DT2YSjNdZvq3YpzEbZcaagiRvfoa-pla9KCZ7g2BA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
ما برای آقای فغانی عزیز اين چهره محبوب ملت‌ ایران آرزوی سلامتی و موفقیت‌روزافزون داریم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68333" target="_blank">📅 11:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68332">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=LbHp1VbjO1Oqbbvi-6MKGMOYQIubO6zBluRT1DzDSLkP2mrLpiZImeRSTPcYf0zdEIZksyfgDcBXRqRd3vT_243ii4eb6QY-sVxsH21QFPrU97esAApBMU0w80igo9qQKozmOfTLCxEyUMT2KrOdi9uaC9H4kIOtHcLb62DBr70JEDlXcoA2P9QDPEMLSuCa5zMYqE57hEoQrDF-bvE01BC-3vSwyRqdE3bxJChTtfOTdSE5kvoWO1ZkANcuxyH5PqXn8ER1tNBkhZNYIgg6lZ36yfxXz51RYg95lcWS2o806QLfNzB5CQrHOSqN7EaeUzSQUiUrMhQJbSil9Mg7jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=LbHp1VbjO1Oqbbvi-6MKGMOYQIubO6zBluRT1DzDSLkP2mrLpiZImeRSTPcYf0zdEIZksyfgDcBXRqRd3vT_243ii4eb6QY-sVxsH21QFPrU97esAApBMU0w80igo9qQKozmOfTLCxEyUMT2KrOdi9uaC9H4kIOtHcLb62DBr70JEDlXcoA2P9QDPEMLSuCa5zMYqE57hEoQrDF-bvE01BC-3vSwyRqdE3bxJChTtfOTdSE5kvoWO1ZkANcuxyH5PqXn8ER1tNBkhZNYIgg6lZ36yfxXz51RYg95lcWS2o806QLfNzB5CQrHOSqN7EaeUzSQUiUrMhQJbSil9Mg7jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وضعیت پل کهورستان در محور بندرعباس شیراز بعد از حمله دیشب.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68332" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68331">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGw2UCjCcnVWxvHVmjWjlZoVZ6ZxYjsN-8ESJPA3Yj-b23xAgdCrnwCNWmv8kVGXmwxgjgc1wPwCz4Jsln0mxS-m9B7YQdvi30UdyTaD3H5mcGFm_a-DYg3-BnYdXuv18Gce3dhjssBIdJ8MwE2RFeP3m0LQdXeXkKehBqoCnwm5-GOY2Q5etIfZU64WoDoUzVqACGCk-H5otj-cdTB5d1NpsF586cDebqPWTCN4wrAmvPn8aGDopnaLlchKU-x-wQcE3jAiVUJW6K-16OS4BHZSKwwJurkKOYTGmiExojWD1UYf5r4C6sJLnDBzKA_fLP5oHLQ-__hKIeLOqP3KCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال استریت ژورنال:
به گفته یک مقام ارشد آمریکایی، ایالات متحده روز پنجشنبه چندین پل را در ایران هدف قرار داد؛ اقدامی که با هدف قطع مسیرهای تدارکاتی به یک شهر بندری و پایگاه دریایی در تنگه هرمز صورت گرفت—مراکزی که ایران از آن‌ها برای حمله به کشتی‌ها و اعمال قدرت استفاده می‌کند.
بر اساس گزارش سازمان صداوسیمای جمهوری اسلامی ایران (IRIB)، در طول شب پنجشنبه چندین حمله به پل‌ها در داخل و اطراف شهر بندری بندرعباس گزارش شد و بزرگراه‌های متصل‌کننده بندرعباس به استان‌های همجوار مسدود اعلام شدند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68331" target="_blank">📅 10:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68330">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60e986837.mp4?token=BOR0bBNbBmulr2DInX2sM0cMc1WawGFrT02HdZ2sYs-llhchE-W_pyk5gglLquwQN7JXHxUgeq6RNyUA0sUNUT7QKcF31M4OT8JK4uzXLmfNdEsWAXjc_dx_yXK1LcTOSJqntyOXg5k9JYvum4ZTWdW0yvCj7oVK-h9tZr1t_WKcA7ZL3n4CqDbrBUlhUScI65SD2dDKIaBf167jUhCuhM4YLjFNuNwqwqsCIMM-EMmg-tv222J_L5bA6GXWaos-T04J8fBjFiiPgChjyCJ_8Gjde_ymLxiSQ6QrV_0LjQmXdZlou8vMLFF30IcoQkCImxojLvIxzZOmo2UIyq9ERw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60e986837.mp4?token=BOR0bBNbBmulr2DInX2sM0cMc1WawGFrT02HdZ2sYs-llhchE-W_pyk5gglLquwQN7JXHxUgeq6RNyUA0sUNUT7QKcF31M4OT8JK4uzXLmfNdEsWAXjc_dx_yXK1LcTOSJqntyOXg5k9JYvum4ZTWdW0yvCj7oVK-h9tZr1t_WKcA7ZL3n4CqDbrBUlhUScI65SD2dDKIaBf167jUhCuhM4YLjFNuNwqwqsCIMM-EMmg-tv222J_L5bA6GXWaos-T04J8fBjFiiPgChjyCJ_8Gjde_ymLxiSQ6QrV_0LjQmXdZlou8vMLFF30IcoQkCImxojLvIxzZOmo2UIyq9ERw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، تیر 1403:
ما غنی‌سازی را بیست درصد کردیم جنگ شد؟ شصت درصد کردیم جنگ شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68330" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68329">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=XHfwzWmg1wKhi2POfSYssScTDpvZk5_EM8O71cXdn_1OBGiEnU3h5tud3t_P2ei0uRy2TSZHVyd_JSczhvaJVl9qVvAVA8-p8082_QAKp6CFUH62bhOGhAecc3htH5GQqEYeayQ8eGHfY_rxoh3gF7ucWrFHd68g1cuktWgI2OPYGWriktJlD_EA78RV4UMF0ZvT-RZb7qSI5VnWASUe8_ku6fFHLuhYrwuj-qMjjbmd-GWf_dvc3HM_V80MtiV4s1Irp76n3b_DHJywMWCb2HlI8PXD2LM5wceRLkaEM5Aqw1xiBXAzLcWw-NHgmxTHTOH4_e9PuCzvsdAySE9A6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=XHfwzWmg1wKhi2POfSYssScTDpvZk5_EM8O71cXdn_1OBGiEnU3h5tud3t_P2ei0uRy2TSZHVyd_JSczhvaJVl9qVvAVA8-p8082_QAKp6CFUH62bhOGhAecc3htH5GQqEYeayQ8eGHfY_rxoh3gF7ucWrFHd68g1cuktWgI2OPYGWriktJlD_EA78RV4UMF0ZvT-RZb7qSI5VnWASUe8_ku6fFHLuhYrwuj-qMjjbmd-GWf_dvc3HM_V80MtiV4s1Irp76n3b_DHJywMWCb2HlI8PXD2LM5wceRLkaEM5Aqw1xiBXAzLcWw-NHgmxTHTOH4_e9PuCzvsdAySE9A6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویر ماهواره‌ای نشان می‌دهند که آثار سوختگی در محل حضور یک سامانه پدافندی پاتریوت آمریکایی در فرودگاه اربیل عراق وجود داشته و احتمالا این سامانه  بالاخره توسط پهپادهای شاهد منهدم شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68329" target="_blank">📅 09:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68328">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68328" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68327">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nLt53dclq2_nwbalugbu-RdPrJU-TL7xId8Sss_Sv5txu7rsWvtuop5qNnKQvXi-Eu8BeoepxPC9T9URMgHmXtyDyEqMGcMqwF8VuqkMHUnxV5peJgfFK6mJQOa_tBtLqIM__-wDs1MjaNiUW9-l9HxNnGDr8eT-sEwpQpij-UCQP6grjsQR-8n8lJLuGSXTXrazZGGI62LJNESNWknFXy8-buey9_QKnzBm-zurpl9cUBJLgi-WqtxWQYcksbZnb47dL7H6_SecpLqhNKPbVaXyFTtQJwcmsInlgqUwHqSsf2iispvp98gUdpwGhvPWLUcLQIPh-XTirmOM2Zwamg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68327" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68326">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
از سایت موشکی جم چندین موشک شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68326" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68325">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bee400515.mp4?token=iaYfbMF4YIEc-TNTHXTxOS2kkcE8LDcSIONl39owzYiKd3XrFt_WyDHjUp_XDVsSWDxUT4_hvLejr2EQgm0aCn1upJJAbC7RqLm5JDTl3Iqke1Qkdtt_wc70CeDeqxKOn5xkiueSLn_WeFx6MbAid5vRlwATGeUduV52wezPAJAhQj_QiRBqA6tbkQfAD3kUkXrYY9sw2uJ5CGItGWw5AtIj50ysBwumAEmtG5x7ObK7hu05dV19fBr9cQn0Uq2MyJIdezfbHb2xs8M_iaC6Vh6hR_0fYx6IcYKZl9pObFLcq5QBIamqLSEKqupSWm0zq2F9CYcd-s_Prw-SY-hWUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bee400515.mp4?token=iaYfbMF4YIEc-TNTHXTxOS2kkcE8LDcSIONl39owzYiKd3XrFt_WyDHjUp_XDVsSWDxUT4_hvLejr2EQgm0aCn1upJJAbC7RqLm5JDTl3Iqke1Qkdtt_wc70CeDeqxKOn5xkiueSLn_WeFx6MbAid5vRlwATGeUduV52wezPAJAhQj_QiRBqA6tbkQfAD3kUkXrYY9sw2uJ5CGItGWw5AtIj50ysBwumAEmtG5x7ObK7hu05dV19fBr9cQn0Uq2MyJIdezfbHb2xs8M_iaC6Vh6hR_0fYx6IcYKZl9pObFLcq5QBIamqLSEKqupSWm0zq2F9CYcd-s_Prw-SY-hWUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68325" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68324">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه پاسداران به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68324" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68323">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">روز‌ها و هفته‌ی آینده بشدت مهمه، مردم خیلی بیشتر از جنگ ۴۰ روزه ترسیدن، و مسئولین علاوه بر ترس، بشدت سردرگمن، امکان یه قمبل‌قهرمانانه‌ی دیگه وجود داره #hjAly‌</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/68323" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68322">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/68322" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68321">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHBbg9C5qu-_iSRIung7TcXcHenQ86WRU6kCC7IWgeqIXinO8_UfN0fvhI4YBolZGRUMBVDemAMnGSIXIqQvgXrIrrSTLpe2Jw2MvW6qgOIUppWDPjDtZxicYloVyhJouEE9NaprY5LQVh_-O5jttjoPp-75hw_gVb-OHVJtnNBQdqQg_vjiaMdcE3avlw1z7ncx-DsA2640YHJwiz7UaxvKzn7M5ZfAVs0q5oPOuRi2aDcQyxSNXJXxuNa9M-6PzLAJQZjoUMbupr7oTv2fukZxbhcTtYmf01zCCM99f79xn0TPvF_hIGXFKcRh1kH7OessG4m6b49cSb9WfLKhlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/68321" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68320">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=VyvXHXqbT8OKAj71VqF_uXn6cFeO0x5OAyYXXhtGRqXZdzC4m6-MiIC2Enu6jj8qF1nNd4kYk2OsN-waFl8A8KH8EracSMg8vFUkxfG_-QDV2lBXB79WtIiLjy82_rcAMKBCm_DYYOxc86dI1w7vz6iK0Nynx6drLRneQ_cb9dzVILVyuI9g2Pue8MW3Y8rJ6VkHk3YyJFsEFdbSs64VHW-aL05G4st9bndmihdw3NjI9OoXysPK2Cabyk9vswKX4nD1-5TF5sPSSSExevqOzBbUZmJ0e4y9ipY7GrNEdeZVL_FF-Vhbcdc5dDAdW2OxEuPuZ6uK0U_t5UPGhsJOFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=VyvXHXqbT8OKAj71VqF_uXn6cFeO0x5OAyYXXhtGRqXZdzC4m6-MiIC2Enu6jj8qF1nNd4kYk2OsN-waFl8A8KH8EracSMg8vFUkxfG_-QDV2lBXB79WtIiLjy82_rcAMKBCm_DYYOxc86dI1w7vz6iK0Nynx6drLRneQ_cb9dzVILVyuI9g2Pue8MW3Y8rJ6VkHk3YyJFsEFdbSs64VHW-aL05G4st9bndmihdw3NjI9OoXysPK2Cabyk9vswKX4nD1-5TF5sPSSSExevqOzBbUZmJ0e4y9ipY7GrNEdeZVL_FF-Vhbcdc5dDAdW2OxEuPuZ6uK0U_t5UPGhsJOFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68320" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68319">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=C3htctZVfAaGCY6UGSO5w_ssaXbZMl1PTHL5GWMaxXV9WXmsdJqUTSmhzwOCiNizXC8iu0tj11U4x40_AKLRC8ZbSv5z6EoICzFGTUgo5Tka0Nwj2FWPKJ3jayvjsFBvHlyyXTfotwyw51dNCHBvJrrnbifqnZYPLbSTcGlNKTI3yfjADSmgMYhzNgVQEpG6kRfqLMwg_OQclYcZB0gxWPw6fArVqEe8_GcO6hZCSjRzdAovB_l2ZxhRDeAUogegdPjM_5jLwVp42L7a4fKsYvbvuMeGXhJg3To7MNWLnu7L-BC7SaEZKlEN2IaYeqs5BvDWp4v_sWxtDJc816_7_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=C3htctZVfAaGCY6UGSO5w_ssaXbZMl1PTHL5GWMaxXV9WXmsdJqUTSmhzwOCiNizXC8iu0tj11U4x40_AKLRC8ZbSv5z6EoICzFGTUgo5Tka0Nwj2FWPKJ3jayvjsFBvHlyyXTfotwyw51dNCHBvJrrnbifqnZYPLbSTcGlNKTI3yfjADSmgMYhzNgVQEpG6kRfqLMwg_OQclYcZB0gxWPw6fArVqEe8_GcO6hZCSjRzdAovB_l2ZxhRDeAUogegdPjM_5jLwVp42L7a4fKsYvbvuMeGXhJg3To7MNWLnu7L-BC7SaEZKlEN2IaYeqs5BvDWp4v_sWxtDJc816_7_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات موشکی و پهبادی سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68319" target="_blank">📅 01:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68318">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
در حملۀ دقایقی پیش به بوشهر چند فروند موشک آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68318" target="_blank">📅 01:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68317">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
فارس:
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی در استان لرستان را مورد حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68317" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68316">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=ci-lu1Q2ToTrGkxl4Q0a5bbCqO_r0swNJCzUuYeczhr2TzdLfKc9SdIGvE_HYtMn3ib4wouoL6hnsA0-Z9glAnW89liTIrQDq7FmjxzIPmoihRexLoJSpV652rodqO2jwOICyGGOqLhnBreoCDsI3gUT6bgz7VYRFuxYMCnhvFb9bCLutNbHFgH6RZHBaiU6zChUZ4czhyMiX-KqkE6-ehbHS7-ckGLtV2g8tTjjHeRQprZ1VN508mThXLzhUl757SGCFE-BfLTSsBgFu-FXN647QuZDmSUv3XsgSu-VpUwJSVcSRT-CU-3dSUPPxH1pp5Wg-dxx8CmCILClO-kfKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=ci-lu1Q2ToTrGkxl4Q0a5bbCqO_r0swNJCzUuYeczhr2TzdLfKc9SdIGvE_HYtMn3ib4wouoL6hnsA0-Z9glAnW89liTIrQDq7FmjxzIPmoihRexLoJSpV652rodqO2jwOICyGGOqLhnBreoCDsI3gUT6bgz7VYRFuxYMCnhvFb9bCLutNbHFgH6RZHBaiU6zChUZ4czhyMiX-KqkE6-ehbHS7-ckGLtV2g8tTjjHeRQprZ1VN508mThXLzhUl757SGCFE-BfLTSsBgFu-FXN647QuZDmSUv3XsgSu-VpUwJSVcSRT-CU-3dSUPPxH1pp5Wg-dxx8CmCILClO-kfKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68316" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68315">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68315" target="_blank">📅 01:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68314">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68314" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68313">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=GwyxISNt3_cRiDzjJQJxN4myCSua8ly2FatPep3v75x4kK4TsUoxOl-R5ti8K3-AzGFwbiUNIRK3RiBSnAjEp0ur3itJKT9EBgHVOztLYLE-Wdm1ylphI-0r6vxQ964W3LPk1ip05J4oefFy4ittA8JCiqt4Ooeh1EKAx_e2nZMzaOwqa6fz8JuGdWm995gxzGxxlPQsJD8Vj8_cYwX9_uYmRCOTkuSFdRjJvHXCZV5VYEZVuw-YEwhmH4CC6wkRR0paDTFgG_b8xAnahprgUWkhNsmh9N1CG9t306f4Db8vI-giHoxMNU0jhfy_hP3qFl4NsOKJ7_ZWHBdxRUUF1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=GwyxISNt3_cRiDzjJQJxN4myCSua8ly2FatPep3v75x4kK4TsUoxOl-R5ti8K3-AzGFwbiUNIRK3RiBSnAjEp0ur3itJKT9EBgHVOztLYLE-Wdm1ylphI-0r6vxQ964W3LPk1ip05J4oefFy4ittA8JCiqt4Ooeh1EKAx_e2nZMzaOwqa6fz8JuGdWm995gxzGxxlPQsJD8Vj8_cYwX9_uYmRCOTkuSFdRjJvHXCZV5VYEZVuw-YEwhmH4CC6wkRR0paDTFgG_b8xAnahprgUWkhNsmh9N1CG9t306f4Db8vI-giHoxMNU0jhfy_hP3qFl4NsOKJ7_ZWHBdxRUUF1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو وایرال شده از حمله وحشتناک آمریکا به بوشهر
شیشه های ماشین فیلمبردار درجا ترکید!
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68313" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68312">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d811948267.mp4?token=tlNbiDsxsgYuX8Jfq9MibU0ubCXdgcVuthsBJKs-21DP7mpUjqvyqMyggN2WGhb3zPWViYmNBfT9B71MHhODiOGXhUT1uKR4tAcsel3jiMAB-yUE8CjfuzRlFI-Fb_KgKLdqt7irfGKigAJGvgYjvIPfFyY8Cp2u4jVbq5BT6NyYe4QqUo3Hh6-BPTGmWFv7mrh1k7pvK2de9xCeQ8d5l_7Sm6D0Y3OQZtua1TWIAtxYpWSNtfb0hFyroQUDaPXo12sFyFY7jJctMT8FCV97tFjsHZT9smygnQ0GrCztcC4l97xF4ZRnB6vQR8dG8-rv5snwZKukkXSo1hf0icWkIHiGzuA7kuBC137IwgWRyL40BfEg4_YZX4nH5lkrpp3GFrHzIRV182QwOTuULBM-h17kBBFYqvYfItMrEA0btV4TolaZvN-5Q3_2Ak-rK-obHvC1HcWrMBLcyH2V0u1hfqU9NJ2iIjHkKEge5qFBb9mOAremVSIOOCE7ddnm2CwzFIfX2GMTs6olHHcWT-BWK7a255Ots63L7GicytjlYXzh63eGuWee8hENMuurpnbqf9JM-w7gKGl4FvIImb1Ah_DoVmViyxKyHe2F1_-jamBHAos0KZ9KtopeQXAHsE5mj2yaBeITzA99J-193GK77wri1V0vFL90q49fqXdM8FM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d811948267.mp4?token=tlNbiDsxsgYuX8Jfq9MibU0ubCXdgcVuthsBJKs-21DP7mpUjqvyqMyggN2WGhb3zPWViYmNBfT9B71MHhODiOGXhUT1uKR4tAcsel3jiMAB-yUE8CjfuzRlFI-Fb_KgKLdqt7irfGKigAJGvgYjvIPfFyY8Cp2u4jVbq5BT6NyYe4QqUo3Hh6-BPTGmWFv7mrh1k7pvK2de9xCeQ8d5l_7Sm6D0Y3OQZtua1TWIAtxYpWSNtfb0hFyroQUDaPXo12sFyFY7jJctMT8FCV97tFjsHZT9smygnQ0GrCztcC4l97xF4ZRnB6vQR8dG8-rv5snwZKukkXSo1hf0icWkIHiGzuA7kuBC137IwgWRyL40BfEg4_YZX4nH5lkrpp3GFrHzIRV182QwOTuULBM-h17kBBFYqvYfItMrEA0btV4TolaZvN-5Q3_2Ak-rK-obHvC1HcWrMBLcyH2V0u1hfqU9NJ2iIjHkKEge5qFBb9mOAremVSIOOCE7ddnm2CwzFIfX2GMTs6olHHcWT-BWK7a255Ots63L7GicytjlYXzh63eGuWee8hENMuurpnbqf9JM-w7gKGl4FvIImb1Ah_DoVmViyxKyHe2F1_-jamBHAos0KZ9KtopeQXAHsE5mj2yaBeITzA99J-193GK77wri1V0vFL90q49fqXdM8FM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده آمریکا، دقایقی پیش تصاویری از عملیاتی که دیروز بر روی یک نفتکش ایرانی انجام شد، منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68312" target="_blank">📅 01:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68311">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دیشب که داشتم با دوستای جنوبیم حرف می‌زدم، می‌گفتن حملات بیشتر داره به سمت پادگان و و قرارگاه های نیروی زمینی کشیده می‌شه، حتی دیشب مثل اینکه به پایگاه لشکر ۹۲ زرهی هم حملاتی شده...
امشب هم که خودمون با چشم دیدیم ته حمله به پل‌ها آغاز شده...
حالا سوال همه الان اینه که آیا قراره بهمون حمله زمینی شه؟!
اولاً اینکه ما در جایگاه تحلیلگر نیستیم که به این سوال، جواب دقیقی بدیم، ولی شواهد اولیه داره اینو تایید می‌کنه، اما وقتی کمی عمیق به مسئله نگاه می‌کنیم خیلی موضوع فرا تر از چند تا کلمه‌ست و عملا داریم از یه لشکر حداقل ۱۵۰ هزار نفری حرف می‌زنیم، حمله زمینی به خاک ایران، برای آمریکا بشدت پرریسک و پر از تلفات انسانی خواهد بود، ولی اینکه دارند شرایط رو برای تصرف جزایری مثل خارک فراهم می‌کنند
اون هم به قصد فشار بر جمهوری اسلامی،
یک موضوع دیگه و موضوعی محتمله.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68311" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68310">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861fef7828.mp4?token=Yn94AjORdnB51fokmQy-RgqSatRDi6gbskQdJOqkcMooKTNLW6nl41nSkP7GEfTMpGKEAeK5ejZiWh24DDgOUiBW80L1kkFIypdkfBg1IEDYaMTFko4_yhV94vXPQp3pIYBYxexcf9EwNNteLtndBR3V3ikY-OBSUZN2u_55OP7r-AlRYhF1EvYJ4gB-GFMi1sfJj3iSNxCAG9QN1fjdn2JoShs1A_NiXTxchvGVoFXgl_l2PanxZkUxvx2jyVu-hQeXrXb23rI3xPPfY2nNIdmSxdaWu4Q1A0kN7bCVY4hQm2lVyOVoVw8PNPYuN9grMhSLDJS8wLaeXud4XGVR2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861fef7828.mp4?token=Yn94AjORdnB51fokmQy-RgqSatRDi6gbskQdJOqkcMooKTNLW6nl41nSkP7GEfTMpGKEAeK5ejZiWh24DDgOUiBW80L1kkFIypdkfBg1IEDYaMTFko4_yhV94vXPQp3pIYBYxexcf9EwNNteLtndBR3V3ikY-OBSUZN2u_55OP7r-AlRYhF1EvYJ4gB-GFMi1sfJj3iSNxCAG9QN1fjdn2JoShs1A_NiXTxchvGVoFXgl_l2PanxZkUxvx2jyVu-hQeXrXb23rI3xPPfY2nNIdmSxdaWu4Q1A0kN7bCVY4hQm2lVyOVoVw8PNPYuN9grMhSLDJS8wLaeXud4XGVR2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
تفنگداران دریایی ایالات متحده از «یگان یازدهم اعزامی تفنگداران دریایی» در تاریخ ۱۶ ژوئیه، عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «وِن یائو» (Wen Yao) در دریای عمان اجرا کردند.
تا به امروز، نیروهای آمریکایی مسیر سه کشتی تجاری را که قصد عبور از سد محاصره را داشتند تغییر داده، یک کشتی را که از دستورات پیروی نکرده بود از کار انداخته و برای اطمینان از رعایت کامل محاصره دریایی جاری ایالات متحده علیه ایران، وارد یک کشتی دیگر شده‌اند.
تنگه هرمز و آب‌های پیرامونی آن همچنان آزاد و باز هستند؛ مگر برای کشتی‌هایی که قصد نقض محاصره آهنین آمریکا را دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68310" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68309">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68309" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68308">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCEu48eKUTF9hEtZZEAp7bUzuU0s5K8gWXVopGCCJOEhgxes4tlNTbx71A2FCmpWK8I6wEaWR_js_doonJnIaG3qhrgag86L-0MtwfXafH8xvBFbQz4BVyBpqlRuruQEbO9EJJeMKwkJYSMnh9D_NQR21pMtmUleFaGSyAdBBOlW6iVUHymij6dlcHYm04irEgA05gZD1Ag8WLFLsxPOKo-Jo2T5TToD1nVCPgywk78JvGygHHTce6HDloASN7XpRRx6E1ylIIBZSc8W3NFbreN-zUndtKJ0kYdNFwduMUI1nOHZ2F6bjfbk16Pd2JvG_n8UwLkpLFwsugRmIeAm3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68308" target="_blank">📅 00:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68307">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
دفتر فرماندار هرمزگان اعلام کرد که تا اطلاع بعدی، جاده‌های زیر مسدود خواهند بود:
جاده بندرعباس - خمير - لار به طور کامل مسدود است.
جاده کشار - کاهورستان نیز مسدود است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68307" target="_blank">📅 00:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68306">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN1KT8H-F2oshwS6xoEFoipi-YcbWK5XFKY9wC_jUk74wbBsaG1_ZiazHsVCD3XC9SLznFDgvQk7yoWSVXLHUHabMXW538oWCBqIxur5F5L1bZopKKJBuVMxiIx5Kd8VCLQ90doVIPyr46QziOF2UgttKjS_vk56Hn7lBB-Bd_EGwRA75xwNeaOLWURDHa0thSk0CxC2Jd14PeT-Uy3ixOKUbyIRO5VwyTXc-pPj1u6nWMERLLUa3ZZ2vVPRPHTuXAR-6wlj0MeMGPq9zii6K439T6Pv5bmdqj-J5PmeqRd7qupplvHanB71QWVVUre24TrsDFc-C0P-6dtmucLBSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رشیدی کوچی :
⏺
«حمله زمینی به ایران از سمت جنوب رو قطعی میدونم و به نظرم تنها دلیل تأخیرش، گرمای شدید هواست.
به نظرم تمرکز حملات آمریکا روی مناطق جنوبی هم در همین راستاست و ایران هم تا الان با هدف قرار دادن عقبه دشمن در کویت و بحرین، اجازه ایجاد مراکز پشتیبانی رو نداده.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68306" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68305">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq57jU89LHaIBRgM76JLtimKB2YLIwIWGeIg30Zb7Y5btqDqHzR_nwEcGF5nd3oIpXwiCM45hamIr2Bxl83hvlBPibzaQzUosj-MMm0Ha1QDs0YO0GtJDehbHc6hJalinzd1uMvV79fSHrKIDjWnkGnpxaUjMBKY1yKA_SHN8dIUeINgUztbzGP7G89xrC3r-Q3PJke4SbpwWDl-CHy96t2bxVEg6aurn8bEiVCu2AR_t0J7z-ikDROim8dsoITWb14Sdqc3BBZ5x5oNEv43tWCJyFkbZReWCMh6cnxLWE9ZwLNk86We1XDktnwDz90I-jq_QfQxCIt4sePnaa78Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68305" target="_blank">📅 00:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68304">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnfF5qksgk9v9DQduaZlbLE9XWHBRsWuSNheBcyxlMQs0IoVWTlvpc2hNEMJHl77j_AQxpzSSOU3j6zdyhGOntg7nP_-x5zl8nue3d-v-TVARmBgf7dvK2OZyAST-rAgDnZAH4mWNcw_R1uK2WhX57OM8LcYkLxcoz_CHR6i_5xEvw4SRnqBcRTiNRFMELcz14_f6XZN7BeVp1O2hrIvUnmAQgmt3PWCHE7FWDAVHBvdTZ_o-Fq-iIfFHATQG4XwOfNGnlA63K86-ePbLaEPlInmkIWMQRDtPQZ1IM-Lbthw_7WnFjgvUMAd80OZl1vTm6OuhJn9lDXoAWyxTIVi4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت   @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68304" target="_blank">📅 00:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68303">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68303" target="_blank">📅 00:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68302">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=MeVe64HT6bqIiRcrtrMRLHsEUetGbUs2cZ_bqvcyazBW57XLcR0UO2iRFU_M5XisrFxm2063Sz5f9c_-PcM_ljU7iKSEe1HY-ufuP9IW2d0f0AFqO5PKVjwfMs3SiuOxHZA8Ento83wR2G300SzMNJa9sTe8k9rR0tJuFOjldPvT7OwIQon0m6gqJ4KbvbmEH5Km7mG_AfhQMQh-UfP_JXfahZ4KBsjzZUYZyB51JBTmkuXvAS5vbvT-C4vhJ_N55Oea-b63OYY6HfmbUVCO82VYY_wnT6gLvI-KaXnmSMOMXe-bOLvPqcuFV_ORSpmDPdZ7Uk4c1RS8TcS38nt-bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=MeVe64HT6bqIiRcrtrMRLHsEUetGbUs2cZ_bqvcyazBW57XLcR0UO2iRFU_M5XisrFxm2063Sz5f9c_-PcM_ljU7iKSEe1HY-ufuP9IW2d0f0AFqO5PKVjwfMs3SiuOxHZA8Ento83wR2G300SzMNJa9sTe8k9rR0tJuFOjldPvT7OwIQon0m6gqJ4KbvbmEH5Km7mG_AfhQMQh-UfP_JXfahZ4KBsjzZUYZyB51JBTmkuXvAS5vbvT-C4vhJ_N55Oea-b63OYY6HfmbUVCO82VYY_wnT6gLvI-KaXnmSMOMXe-bOLvPqcuFV_ORSpmDPdZ7Uk4c1RS8TcS38nt-bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو دیگر از پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68302" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68301">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
تسنیم:
آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
اونا به شهرستان بندرخمیر و بخش کهورستان حمله کردن و پل ارتباطی بندرعباس به شیراز که معروف به پل بندرعباس - کهورستان - لار هست رو هدف قرار دادن.برق مناطقی از کهورستان هم قطع شده
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68301" target="_blank">📅 23:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68300">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=Qryeaw-m373Bhja7zYy1TjVQ57Sq2VMHqE0CxwADkna7vCf33jvcQ_DDD6o5uJfhZk4Z9EdY25GsGSa1aG7jL_ZbrV2p0IVxOxMzzkCYZm0pwGTHYne4t-XSqaVj9T3yNdI3zpkPF1bg6LN3SDih1mMxQ0m3MnuvyaxTJ4iXild7lB5h-Vi3iyLsHOtKj7fGPTGLiJbQS4SWJ7KtrGpIWEQBVjmsPlIkgGM7Y_k_OdoeiXoXCsgRiZRaNfizqnyRnfQgue_uSP2OJlbhXlnygchFaT8oqymBDM9ULTOOxWtkQii7FDqL3mAc76igwgvL9z1piRTzFGWoFkhinxXbIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=Qryeaw-m373Bhja7zYy1TjVQ57Sq2VMHqE0CxwADkna7vCf33jvcQ_DDD6o5uJfhZk4Z9EdY25GsGSa1aG7jL_ZbrV2p0IVxOxMzzkCYZm0pwGTHYne4t-XSqaVj9T3yNdI3zpkPF1bg6LN3SDih1mMxQ0m3MnuvyaxTJ4iXild7lB5h-Vi3iyLsHOtKj7fGPTGLiJbQS4SWJ7KtrGpIWEQBVjmsPlIkgGM7Y_k_OdoeiXoXCsgRiZRaNfizqnyRnfQgue_uSP2OJlbhXlnygchFaT8oqymBDM9ULTOOxWtkQii7FDqL3mAc76igwgvL9z1piRTzFGWoFkhinxXbIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
در کهورستان بندرعباس یک پل هدف گرفته شده.
موشک خورد به وسط پل، تانکر سوخت نابود شد، راننده مرد، یک تیکه از پل نیست، کسی این طرفی نیاد...
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68300" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68299">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
پل ارتباطی بندرعباس به شیراز و معروف به پل بندرعباس - کهورستان - لار مورد اصابت قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68299" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68298">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=A9hCvSVlUJGbzipjNdmNQP2GgefIri9jP1ALYj4k3acIbdEscKBvbV-IHIdLgpl4mjTv3CDOpjSih7hCnryZJlQlYBiZNgrbjATNrVALPUSjf5-RSDl9N_At2A9shKpwE2qmvH_ShwvfKqTxYQfjoM9OlRtmYgOrqPOhqiKLGbuBG1HN3AcWgE0B-iV_8wlrxsbc4TFXOJ5SCWFc6qGxOZyNTTVwK60w1VG2pGbN30GKwwmaKrpAnltf6Rkii5HOmpMgs-Ow6xVce7csSSijFnpb4hUMbg94iieZ34f0OzZhl9A7IghvgW4pZA043n8iFDWG2P9y3Xl1U6vtqdAx7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=A9hCvSVlUJGbzipjNdmNQP2GgefIri9jP1ALYj4k3acIbdEscKBvbV-IHIdLgpl4mjTv3CDOpjSih7hCnryZJlQlYBiZNgrbjATNrVALPUSjf5-RSDl9N_At2A9shKpwE2qmvH_ShwvfKqTxYQfjoM9OlRtmYgOrqPOhqiKLGbuBG1HN3AcWgE0B-iV_8wlrxsbc4TFXOJ5SCWFc6qGxOZyNTTVwK60w1VG2pGbN30GKwwmaKrpAnltf6Rkii5HOmpMgs-Ow6xVce7csSSijFnpb4hUMbg94iieZ34f0OzZhl9A7IghvgW4pZA043n8iFDWG2P9y3Xl1U6vtqdAx7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملهٔ آمریکا به یک پل در بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68298" target="_blank">📅 23:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68297">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
طبق گزارشات اولیه، یک پل در بندرعباس هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68297" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
به گزارش ممبرا ساختمان مخابرات بندرعباس هدف حمله قرار گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68296" target="_blank">📅 23:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
حمله به ایرانشهر سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68295" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSqIaS8SmU_MVVe7kzx1289eJzwVSRjAWhk6c0OH1Cz0_-5macBMavhFroL78OsEKyyRJirnY8QjGGw5jXfbU-jPCtHQkD2rz2k5xv-dISJ4iF9HTp3rdkZoPBtpJOAXtP0rP9sdmcrxSsUy8WykPPvxTc7JFNQ3oi0s_rmgenoN6_l_eC8aIezMYCG-9qqYSUJ0PopxoCsvQwTH0MVkfyVl1bEl-yQ5msGNwX8d6_ahQG8-LeVXgBh5kYq0tac335Zx9Ju7RXtDGhrM6M8CVUIbE6sdz0JQNvbY-mkG3gFdgL7o9Qkerg9cqn8Is4hTpChbZojMhtlP8_ulaCk9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68294" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5bm82qytfWkqZUnX7S0LTcNdLs7c1eucwFCBudjLwAEFXbl0pMOIetbcxKDgKtgvfStLsabBZQMzxc2r3SIEM8ZOPH7eOtKZ9pq0G1LjCjF7mgmCHXJJbiQtpR6_kpylBBYBVFb-J-aimLzbq4MXoTbuAn50evjipc2aBviYE9eGLixQbnsIHwK3BocoTuUAIAxTmRXENrakqH2kVKw-y0kEHalKs1xgJ31c3B9BDOLBnhInnvik0Bqy2e6Mz_Ko9pu4mOqL3coV7CtXlfLFq5Z1HKcHAoky3AXHsaC-NCVF8XvrnRcMIuHBA8Rv0Ix-75H5P6pgOkFcXTzEybLBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت دفاع کویت:امروز جمهوری اسلامی چندین تاسیسات حیاتیمون رو هدف قرار داد.
از سپیده دم امروز، نیروهای مسلح 32 پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده‌اند؛
این پهپادها رهگیری و با آنها مقابله شده است
این تجاوز شنیع ایران چندین تأسیسات حیاتی در کشور را هدف قرار داد.
علاوه بر این، رهگیری اهداف متخاصم منجر به سقوط آوار در مناطق مسکونی مختلف شد که خسارات مادی به بار آورد، اما خوشبختانه تلفات انسانی نداشت.
نیروهای مسلح بر تعهد مداوم خود به انجام وظایف و تکالیف خود با کارایی و شایستگی، حفظ آمادگی و آمادگی مداوم برای تقویت امنیت ملی و حفظ ایمنی شهروندان و ساکنان تأکید می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68293" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
پنج انفجار مهیب در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68292" target="_blank">📅 23:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به قشم و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68291" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68290">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS-</strong></div>
<div class="tg-text">داداش ما الان تو کوچه ایم تو اهواز بچه کوچیکا ذوق صدا بمب رو دارن</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68290" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68289">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68289" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68288">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=ARDjQJlTM9tWHVmKuHH1l5LkvjYmZzhQ1M2ilEzlnhshg2Poiaie64tJuz5Qk7SKds4xv9HPKbePqhebbcsJmIAJdQlYkAxJCK1PW-fyHqFruVXKowMlctmeYQo5tMaQii1vCIp171DSsTFAAgEr7-BpMGCD7xhB7TJ3pM7PMXkPdhvi0nSh78pxLZDPXB5YLYDsCyQpWsgs0nQUHy2wZkZeSiwzdct3IGfB9-UzGSPtBedUdpMcxTy9pauqUr8pA2L5w6_TwqSrjaDra2j7qOxCh-UqOHlhComIkApNk42GjRkFmhQXE815Pp1iQLwXF6EVBDRTC9xQ1Xs17WdWGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=ARDjQJlTM9tWHVmKuHH1l5LkvjYmZzhQ1M2ilEzlnhshg2Poiaie64tJuz5Qk7SKds4xv9HPKbePqhebbcsJmIAJdQlYkAxJCK1PW-fyHqFruVXKowMlctmeYQo5tMaQii1vCIp171DSsTFAAgEr7-BpMGCD7xhB7TJ3pM7PMXkPdhvi0nSh78pxLZDPXB5YLYDsCyQpWsgs0nQUHy2wZkZeSiwzdct3IGfB9-UzGSPtBedUdpMcxTy9pauqUr8pA2L5w6_TwqSrjaDra2j7qOxCh-UqOHlhComIkApNk42GjRkFmhQXE815Pp1iQLwXF6EVBDRTC9xQ1Xs17WdWGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از کویت به خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68288" target="_blank">📅 22:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68287">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68287" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68286">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68286" target="_blank">📅 22:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68285">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=izeHrQk1gqnQdRJjxYIRZgv2IW4oO9_osY5ZxayljwM3A8K6UKEkjVhfTQPa5CVNFRa2-ByZDmRUVzKp-kFy3E21B4S5x1p46xTYHY3nVfscBwOQxsE5qeMI__agAZfmni7yIDgeOCZbhkDQCJqwKOQ4l4sxblIotyqUqngIN9Te8ygqqtHWPfuxtNcLoReZBb_olUeH0CXyShGCbRnRQTkM1O5ZGvO9lXmHp7o6BoPbVShdZU1Mul_wMAs_KGhL3UHzEfI8SIX_13spwEiiJkivbJtJQvywuYYmF_9l7-imIRBwQ0Bd4kH-F7uZkML5tccmIFHPgRcXzbSzspzS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=izeHrQk1gqnQdRJjxYIRZgv2IW4oO9_osY5ZxayljwM3A8K6UKEkjVhfTQPa5CVNFRa2-ByZDmRUVzKp-kFy3E21B4S5x1p46xTYHY3nVfscBwOQxsE5qeMI__agAZfmni7yIDgeOCZbhkDQCJqwKOQ4l4sxblIotyqUqngIN9Te8ygqqtHWPfuxtNcLoReZBb_olUeH0CXyShGCbRnRQTkM1O5ZGvO9lXmHp7o6BoPbVShdZU1Mul_wMAs_KGhL3UHzEfI8SIX_13spwEiiJkivbJtJQvywuYYmF_9l7-imIRBwQ0Bd4kH-F7uZkML5tccmIFHPgRcXzbSzspzS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68285" target="_blank">📅 22:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68284">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68284" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68283">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZyGkNVrYCc_3EOkrHdi3UeERZmcuho6mQTzELXZ7VUm0F3ejycwP_Mf_PEE1dAeCcMJzwENb_9FQyRaiN5WB1Sn0AbqIlZSN89Ufx-0sdfFSLvrIqh7FHoRh986q66lYR-dczN9YM_Xx4CEA_qQKhtto03yjCI-ifUqqKurJnXuv_4oaGzJHVAdbGQUkj1mN18DXbpNiqQaxLksQahyKA_TCKtz-wLnumSd5pbtZzQz8Eh00sHkgNEJprT00X_lWuDmxhD1y4yvBptwcHNDpAWGXVx_OtdJ_El2ZHMiGZebNZ1i6j00JDZlogKKb3S9F5RWkA8hBAE_V6HE7ueY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68283" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68282">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=nZW-TZ8a0Q_HHJB_lgBizc2qlgtCtx25mDs35SRydTRipTR8B37TtA91hqet6BfFtHA4-u9YDyxBYzu9jdqeWhKPnra8EJCx729q-wBs83YbW_61ZuhlyZ2HVNpLnJZOjVE-cHKpWa3pKh6RauiahPUcU1_7ZMERJgDCpjFleBF3InGhT4KjuQ07knR35afKgLhjeoyY4AZWbE-oom3iIMnXGhn-JTfOVzhJNYzSFAVAcC-bAjqDD6ggyCoZz_n0WcHPoUaNzrdtF_-IQU06eulst-NiHrMaRHg2C9rLjr9eJCev39faBMVl5oAMaxRYh52PVqVzXl4lcNU8yTH2Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=nZW-TZ8a0Q_HHJB_lgBizc2qlgtCtx25mDs35SRydTRipTR8B37TtA91hqet6BfFtHA4-u9YDyxBYzu9jdqeWhKPnra8EJCx729q-wBs83YbW_61ZuhlyZ2HVNpLnJZOjVE-cHKpWa3pKh6RauiahPUcU1_7ZMERJgDCpjFleBF3InGhT4KjuQ07knR35afKgLhjeoyY4AZWbE-oom3iIMnXGhn-JTfOVzhJNYzSFAVAcC-bAjqDD6ggyCoZz_n0WcHPoUaNzrdtF_-IQU06eulst-NiHrMaRHg2C9rLjr9eJCev39faBMVl5oAMaxRYh52PVqVzXl4lcNU8yTH2Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68282" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68281">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxbHX_s4QNs7ybzOSCk0XbC_0Ee6Qr3t6dRJGJg7rRn71B2lzeqFhxcqEVjLotWnRVkmXlfd09A6iFtt-jCXhBndTF_Wutz4rizpZtZ5_T_s-di7jH_hYXymoVF3pvizh70XETgLPOi7aICXjMmtJ2yKx9e0e6Civep8wOZTL9859CL-g1sDg-9EeQ2EijCkwtphQBDoYa5PrsD-P8JANkoAMKLc6ydfTYbrFirABffSherQSbkXpteYP7MWx3rEj_dMDbW73owNaoHfP5TwWia2i7nOxLDpZBgbkLHoH_HtlCMHPA6knZ_xzNW7uDOmJg5i64ikgzL-8O-OWWPm1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۲ بعدازظهر به وقت شرقی، نیروهای آمریکایی برای پنجمین شب پیاپی موج جدیدی از حملات را علیه ایران آغاز کردند تا توانمندی‌های نظامی ایران را بیش از پیش تضعیف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68281" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68280">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68280" target="_blank">📅 22:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68279">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68279" target="_blank">📅 22:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68278">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
پنج انفجار در بندرعباس گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68278" target="_blank">📅 21:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68277">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68277" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68276">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=f5FHmjpZlbJG_l34KZzym3X8LcrwubL0YMCdnMMqSRDpawLzvS7q-luXsX-R_6Khkz0nnQhmoHInN_YaQ7586wX1pvbXINn7NfQJ-bXuhuYl_6_ozF8A7d1iIm387YpOIip-J7HI6F198A58WZy6LwYJNC2CnuAyl7MLnUJkhd6ehnOro1VU1wbpcakQr0H_sWPcGiqKhwYLpSDl7XxRduItVyMcp7VcNyA3ixgV8tlxdy3x1ZLtbbaP6nPF1cM3cp_sHdrzGSuR5OBwFmpCX4E9dG0qgQMS4n3SwSMy6lUhfSv2TGUVRtXhdsg4KGAD2iX81xKeZqPgpkE_oMK-9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=f5FHmjpZlbJG_l34KZzym3X8LcrwubL0YMCdnMMqSRDpawLzvS7q-luXsX-R_6Khkz0nnQhmoHInN_YaQ7586wX1pvbXINn7NfQJ-bXuhuYl_6_ozF8A7d1iIm387YpOIip-J7HI6F198A58WZy6LwYJNC2CnuAyl7MLnUJkhd6ehnOro1VU1wbpcakQr0H_sWPcGiqKhwYLpSDl7XxRduItVyMcp7VcNyA3ixgV8tlxdy3x1ZLtbbaP6nPF1cM3cp_sHdrzGSuR5OBwFmpCX4E9dG0qgQMS4n3SwSMy6lUhfSv2TGUVRtXhdsg4KGAD2iX81xKeZqPgpkE_oMK-9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت سخنگوی سفید کاخ سفید:
«ایران همچنان به شدت با ایالات متحده آمریکا در حال گفتگو است و ابراز می‌کند که خواهان توافق با ماست، زیرا آنها از سوی نیروی نظامی ایالات متحده ضربات ویرانگری را متحمل می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68276" target="_blank">📅 21:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68275">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=NYlYcHno0M1Dlx9wf4bmZLLxGlzcCXeA526rLYXBzLTMdfc-wr4732wdeL_WNIXAQyQqvg43neHYbWGzeH0NBExKeWAv0C-OGd4syS67Tpm_lqwBBlIAuC1gFo70LQg-sK-7JC6LDBrcPYrQvp1_aIenEGMh1v03CWx-0pcnviFKH6bP_jnc8wk3PIl7jHTw7-t4XhNdGQ_9q2PtD2Dl5iheGWeJo_TerbGYFSTqqay0tZuZSEB_5M35GezrOp6w8kr5OIqFMzlKOLjeZKpJzJrx3FC3os27auf0XnLL-XxIwlixtJKrrYeeqM7eR103eMi--f2zLLop3Hko80dIGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=NYlYcHno0M1Dlx9wf4bmZLLxGlzcCXeA526rLYXBzLTMdfc-wr4732wdeL_WNIXAQyQqvg43neHYbWGzeH0NBExKeWAv0C-OGd4syS67Tpm_lqwBBlIAuC1gFo70LQg-sK-7JC6LDBrcPYrQvp1_aIenEGMh1v03CWx-0pcnviFKH6bP_jnc8wk3PIl7jHTw7-t4XhNdGQ_9q2PtD2Dl5iheGWeJo_TerbGYFSTqqay0tZuZSEB_5M35GezrOp6w8kr5OIqFMzlKOLjeZKpJzJrx3FC3os27auf0XnLL-XxIwlixtJKrrYeeqM7eR103eMi--f2zLLop3Hko80dIGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز ظهر تو خیابون ولیعصر تهران،یه اتوبوس تندرو بی‌آر‌تی بدون راننده و مسافر به دلایل نامعلومی شروع به حرکت میکنه!
این اتوبوس میوفته تو مسیر سرپایینی و با ۶ موتور سیکلت و ۲ ماشین سواری برخورد میکنه که نهایتا ۶ نفر مصدوم میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68275" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68274">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGzbidtdjqpU2poJ9lBr3dyJIgVSWDanHADGfYDXnILevf6eoKk1unG2geKBTLq357hk-Hl00iuA2Pi8z6meDus-sq7--XMsY0edT3tRVmrC3VOHbBa_41YkphVtPJgdSAt9ZYlN4T6TXRVYkEfaC28HRYXaev19xHTeKyYCfddljteJfxVdaFc2JBxUfb1N2Y0N7xY4KD3i0EsHWgHMSexJ-bEaVtlYP8DmA1uCnkkd-1Qw6khMHUvBgSYLbyq-nATNDRjYSfEouXpAisdhw3Fe-SMAhTXpbKttGLy4bTp_hCGPATnQvuw_gFNTJ52Safn_qX1b7HxYamhLIEJZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68274" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68273">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbIdxWQNVV1yumU2zngfnGk2k7qWDHirNTdadCDpsVM2PJ6fKtopY5Y293VPmrbtoz_4S7KgvOuKz1fOGGvEPeSVhgUc88ICZEPgp1mRdtyvR0qasHKHSjGI-M5wmKMhrMOFPZ9xPZZxlJBlkybO_pddbhXbYmreI9Lo2vnvEP6YLKG3AV3qnvDV54Iae430GjBcIq_B7bVbh5JedM3QYdAIQQU9ayCJEDIQ4rJuLO2FXNB4L-95RBrpLu0e7Pk011HCVs0WwYKQPNbPCS2FUeDUfYUZDyUs0hULPDt5e2ainMJJs26dNY68uEUrffsJcfBnkVGnRmCEkkFduYThnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏شاهزاده رضا پهلوی:
در حالی که جنگ‌افروزان جمهوری اسلامی در تهران و پناهگاه‌های امن خود پنهان شده‌اند، سربازان وظیفه و نیروهای جوان را در پادگان‌هایی بی‌دفاع رها کرده‌اند، بی‌آنکه حتی توان حفاظت از این نیروها را داشته باشند. این رژیم بار دیگر نشان داده است که میان جان فرزندان ایران و بقای خود، همواره بقای خود را انتخاب می‌کند.
جمهوری اسلامی این جنگ را بر ملت ایران تحمیل کرده است و مسئولیت جان همه قربانیان آن، از جمله‌ سربازان در پادگان بمپور، بر عهده همین حکومت است. آرزوی همه ما، صلح، امنیت و آرامش برای تمامی ایرانیان است، اما تا زمانی که این رژیم بر سر کار باشد، نه امنیتی پایدار ممکن است و نه صلحی واقعی.
این رژیم تبهکار بیش از آنکه دل‌نگران امنیت مردم ایران باشد، نگران حفظ حزب‌الله لبنان و دیگر نیروهای نیابتی خود در منطقه است. برای این رژیم، بقای بازوهای تروریستی‌اش از امنیت و جان مردم اهواز، زاهدان، بندرعباس، بوشهر، چابهار و سراسر ایران مهم‌تر است.
خطاب من به سربازان، افسران و همه نیروهای میهن‌دوست است. جان خود را برای بقای جمهوری اسلامی به خطر نیندازید. سوگند شما به ایران است، نه به رژیمی که در لحظه خطر، سرکردگانش می‌گریزند و شما را بی‌پناه رها می‌کنند.
من با خانواده‌های داغدار سربازان وظیفه که در حملات اخیر به مراکز نظامی جمهوری اسلامی جان باختند، عمیقأ هم‌دردی می‌‌کنم، و از خانواده‌های همه سربازان وظیفه می‌خواهم تا آنجا که در توان دارند، اجازه ندهند فرزندانشان در این شرایط خطرناک به خدمت سربازی اعزام شوند. هیچ پدر و مادری نباید فرزند خود را به پادگان‌هایی بفرستد که امروز به جای محل خدمت، به میدان مرگ تبدیل شده‌اند.
این جوانان، فرزندان این سرزمین هستند، نه سپر انسانی جمهوری اسلامی. آنها نباید بهای بقای حکومتی درمانده را با جان خود بپردازند.
هم‌چنین از مردم شریف ایرانشهر و زاهدان که برای اهدای خون و یاری رساندن به سربازان مجروح پادگان بمپور شتافتند، صمیمانه سپاسگزارم. این همبستگی ملی یادآور این حقیقت است که مردم ایران، حتی در سخت‌ترین روزها، فرزندان خود را تنها نمی‌گذارند.
ایران به فرزندانش زنده نیاز دارد، برای ساختن آینده‌ای آزاد، آباد و سربلند
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68273" target="_blank">📅 20:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68272">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
فارس:
حوالی ساعت های ۱۹ و ۱۹:۲۰ نقاطی در  بندر عباس مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68272" target="_blank">📅 20:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68270">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=MBtlNEGWzBQGV3-dl-BUeKCgpVFLKuvzbQ9BibsggYlhlSe6Ze5uAp7GeHIy7psHmGs5CuoiCEe0RQ2vSYKZhrQT39NSUO5uGBKs67UaT2hAkBuA4TIXIXSrlm7_hB1p9JR5iYJJIexUDxXOUiAyHISVVLUvGFnE892m7kbHPMbKyQlJR0ateYTk1OVVRObIJM81zjcEUA7J1R_tABm_2CqUWg1nc6AMVI8gvWs5J1TYgeA34o-vnYlnfoWg3SfNOgaZw1CZMFlGYBJKLnB1CEiAPNnyF0sI948B4eK9AXpYtCcMBfGAQr-bwVFVA4MZJ2QcBc8fchzpBiyp8X1C3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=MBtlNEGWzBQGV3-dl-BUeKCgpVFLKuvzbQ9BibsggYlhlSe6Ze5uAp7GeHIy7psHmGs5CuoiCEe0RQ2vSYKZhrQT39NSUO5uGBKs67UaT2hAkBuA4TIXIXSrlm7_hB1p9JR5iYJJIexUDxXOUiAyHISVVLUvGFnE892m7kbHPMbKyQlJR0ateYTk1OVVRObIJM81zjcEUA7J1R_tABm_2CqUWg1nc6AMVI8gvWs5J1TYgeA34o-vnYlnfoWg3SfNOgaZw1CZMFlGYBJKLnB1CEiAPNnyF0sI948B4eK9AXpYtCcMBfGAQr-bwVFVA4MZJ2QcBc8fchzpBiyp8X1C3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در بهبهان استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68270" target="_blank">📅 19:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68269">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=CF_Xyoj1YsPFlUpsMbgDUWuWrla918DYzpG2Tq3ZCQ1uovu1xLooBaZQ2DekLrPgLBwg9qLIryrFAvQQLg1PegCxLBS-crdKtnpoIzI8K_RJSgF5EC8knS6LU9YltCBPrVMXxcBZ39iQVZsj7Ej_5Ca_Ub1GGQk7YmWbqfcnhht7X1N_tIN0G0AIKOJHECNO6PN_tfxqsONW5O-AV02aQqkk3PeXIs98ST1NPGcibrOByTXE-7fJ6Qe7wcwN50GNhw1-8NHeK28R_4NAK-fI7UNi0uULi9nwjcmYJjoUBTYvNU1aPm6C_FPuh_f49I5U47ojCwju96d5ZPj6feweqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=CF_Xyoj1YsPFlUpsMbgDUWuWrla918DYzpG2Tq3ZCQ1uovu1xLooBaZQ2DekLrPgLBwg9qLIryrFAvQQLg1PegCxLBS-crdKtnpoIzI8K_RJSgF5EC8knS6LU9YltCBPrVMXxcBZ39iQVZsj7Ej_5Ca_Ub1GGQk7YmWbqfcnhht7X1N_tIN0G0AIKOJHECNO6PN_tfxqsONW5O-AV02aQqkk3PeXIs98ST1NPGcibrOByTXE-7fJ6Qe7wcwN50GNhw1-8NHeK28R_4NAK-fI7UNi0uULi9nwjcmYJjoUBTYvNU1aPm6C_FPuh_f49I5U47ojCwju96d5ZPj6feweqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای عالی امنیت‌ ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم، نمیتونم ذهن خونی کنم
😆
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68269" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68268">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UE_nreIe4kzc53zjg6vOrgzdWzzmfPDwdSJ448wWhJrYjyo7wNNIquXwR0kDziAbbCw4N8tEG-E4CvzCQvGCbXvWmu0i8xBwQDHjgiyOhvnT7xvwGUKkp-qEQvYyJwerPYGgy6wgcem1-BCoKvYAqyOgmj8VUmDe6OOMrTdcGiZN37msfx6PR6vEcdgZiWZKv60GHcZhfvHvc871ypAQ_wi27oqRXLtD4vkDKclvrHLupVsSUJNzHn0aLrCM5H62PIuxp5vrXGvcxwwO8tnjOB3CYqjK_kyG2MZik0RAVgFMDs3_ZUjyMsoBYv7T_8CB5dag9QiBoycfeQ9RQRPZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68268" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68267">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojRzQjPahZtpbWqWED9XyRiuJbzsnWcwLt6qHXdcsJ57aCxar1KZ0mNG4ECKaM4DAtXaSDX7wwhROsOVFC50U3CSdgbVTEAmtMz936tLYrANqEIwv8ssDgmjtRgOxMLm6Z6piDp5k0wiHm0snsFbwXMCGgTRVq9QYQMmgdK8DtflXr3PkpPj39LCjHlJ9QtfEy4LN2RyMDQJBUFMLgkHuG2jW7LA_g3-bcsP5-POVmZEmZjL_9GDuJ-bdUxvAzWG9i7D3NRFJdsNhvKA1rUPduJDWp0t1xTNYDVc6TxnQ8pawRcADp5Qsmt4L9VVwhDrxhk43DqCSgr_1fdwcpDVvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68267" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68266">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06389032d8.mp4?token=EcIixI_NUL75z1BQra1MmyKZRXJFDltdWQCRDdk0MErbx24hRZszyj8DEYanJH9MnL8OJT-mNVOI0Rmtp50AAuZnxyI42cw6tx2GMi5yNBbX2bnoFOym-JSgDTvOAB9UaLZcfjLfij28ECixIu7xZCNeF61RXgrte9WKdF7WeyyXqlbMWC7p2xnzr9rLaERnMxq8pKs5At1VtKOC8PHleMvUyD4E83-oF2-5d_ojOenT9Y7kRwmtxNomf_oQxKZpNgzFrvzpPrDRcpadLqvh9S3a3I_9-g5vB-tdS7NFT_mqHPOaviLKiJOyo3BlQzX1tsTVQI7RmvF3USy3DubYEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06389032d8.mp4?token=EcIixI_NUL75z1BQra1MmyKZRXJFDltdWQCRDdk0MErbx24hRZszyj8DEYanJH9MnL8OJT-mNVOI0Rmtp50AAuZnxyI42cw6tx2GMi5yNBbX2bnoFOym-JSgDTvOAB9UaLZcfjLfij28ECixIu7xZCNeF61RXgrte9WKdF7WeyyXqlbMWC7p2xnzr9rLaERnMxq8pKs5At1VtKOC8PHleMvUyD4E83-oF2-5d_ojOenT9Y7kRwmtxNomf_oQxKZpNgzFrvzpPrDRcpadLqvh9S3a3I_9-g5vB-tdS7NFT_mqHPOaviLKiJOyo3BlQzX1tsTVQI7RmvF3USy3DubYEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، درباره ایران:
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، این تصمیم با خودشان است.
اما ما قرار نیست ۱۵۰ هزار نیروی زمینی برای تغییر رژیم اعزام کنیم، مگر اینکه خودِ مردمِ حاضر در میدان بخواهند به چنین نتیجه‌ای برسند.
البته ما در هر صورت قصد اعزام نیرو نداریم، اما پیشنهادِ اعزام نیرو عملاً به این معناست که ارتش آمریکا باید این کار را برای مردم ایران انجام دهد.
ما دیگر دنبال چنین کارهایی نیستیم؛ واقعاً نیستیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68266" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68265">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNbTjIZz2gbPAN9_dTygvyfYE7eRyWZlDEn6Rv5_f4Q8LtNnAS5f7empLqit9PxniBHYJf2w2ABA49ThD32dqrwn0RDA24NJWu2RsdkHXOxPtNc4RoHuc5BacWImUz19s0lUQWTYFn1xLbVfzDxc9UYZLllVJAc8Umr4DojoAgZUX2ooVVjRPbHmNUAbc7dpET-Gfox9u28eUuXr1ZiprTsj2Y-3M8zwP4cI49BikAzyVVaJKdUZf1R8e2r3251GRPT7SFpNIDa0KRtEiRPm6KF9wmxvf6vUSWE7Afpv6Y04i6xdKf-iWfG3ngjXxJsTtqk46mFtySnelzPS8RBR5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
لاشه پهپاد انتحاری آمریکایی FLM-136 LUCAS در نزدیکی بندرعباس
پهپاد LUCAS در واقع همتای آمریکایی پهپاد ایرانی «شاهد-۱۳۶» و یک پهپاد تهاجمی یک‌طرفه (انتحاری) و کم‌هزینه است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68265" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=VnWmehnb8SZY89O1gbcAODACBdKHA20Ao6EAJLR-8OXnV2iwUOEXaVEkp-W1zGwUzjGKE1H8PFZnpbxcr5HcYjwL8kyPERq4uLwqekKOtxJRdD70ZihFnI4vfT5gtPoooUBoDfW3ru8hYrOS9b1Z0q9HagoNNsv-0BU8A9WnB9V4FTxn9GgnHuw-YiILvFVQn0MkFnKbOHtsIYnimlql9zl2o0ya5UlISzPveHfQ4cSuAirmu-26Xc_HgdED8ldqcOTJkRvGHjJyzSMikICSj2UWrtqyFSS5eWnyti2d1iP1JagTUbvnzG6Ge6UhLW6nmprURKPEkuEvZfRWXDuHHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=VnWmehnb8SZY89O1gbcAODACBdKHA20Ao6EAJLR-8OXnV2iwUOEXaVEkp-W1zGwUzjGKE1H8PFZnpbxcr5HcYjwL8kyPERq4uLwqekKOtxJRdD70ZihFnI4vfT5gtPoooUBoDfW3ru8hYrOS9b1Z0q9HagoNNsv-0BU8A9WnB9V4FTxn9GgnHuw-YiILvFVQn0MkFnKbOHtsIYnimlql9zl2o0ya5UlISzPveHfQ4cSuAirmu-26Xc_HgdED8ldqcOTJkRvGHjJyzSMikICSj2UWrtqyFSS5eWnyti2d1iP1JagTUbvnzG6Ge6UhLW6nmprURKPEkuEvZfRWXDuHHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عموپورنگ هم اینطوری بصورت دردناک برای مادرش گریه کرد:
من دیگه مامان ندارم...
دیگه در باز کنم کی بگه چی اوردی برام؟
💔
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68263" target="_blank">📅 17:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68262">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=EXq7dR8UgTfNlj3WhvMCl3U7xFQFtgkLSdB50lSD3b7BOKSrlvtlC9RnBZlptGc1cD3UGeNIw75M4rFD4yPaYiXBnqA3Hltg622yQjV8e9oLUIp4TVH0nJ_eifDkB_6qT-DqWIXndmWs0fRbEeLyZGeaYiGF2YwJ1r4kXKWi9hmMhsT-y_hXQZlBYTraE-GOBOJ7qnyzsuZtAWlWn43AhrTPs1p8KtUWsWf50cxxrqqPK7-5hRiBkjbV8e9eKHmNzuEv8PDPRYrCi2DAMr5XqDC4OtfBpkd1-7CsxE1y6Nt_Z5_lPtBBI7Z7siuqCiWlsIf0tpvFd8Ig9to4OefWAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=EXq7dR8UgTfNlj3WhvMCl3U7xFQFtgkLSdB50lSD3b7BOKSrlvtlC9RnBZlptGc1cD3UGeNIw75M4rFD4yPaYiXBnqA3Hltg622yQjV8e9oLUIp4TVH0nJ_eifDkB_6qT-DqWIXndmWs0fRbEeLyZGeaYiGF2YwJ1r4kXKWi9hmMhsT-y_hXQZlBYTraE-GOBOJ7qnyzsuZtAWlWn43AhrTPs1p8KtUWsWf50cxxrqqPK7-5hRiBkjbV8e9eKHmNzuEv8PDPRYrCi2DAMr5XqDC4OtfBpkd1-7CsxE1y6Nt_Z5_lPtBBI7Z7siuqCiWlsIf0tpvFd8Ig9to4OefWAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام:
هواپیماهای جنگنده F-35A متعلق به نیروی هوایی ایالات متحده در حال سوخت‌گیری توسط هواپیمای تانکر KC-135 هستند، در حالی که در حال انجام گشت‌های هوایی بر فراز خاورمیانه می‌باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68262" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68261">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXJPeJ2s01xM5fj7U4SAf_oYVsknpjh7HBzcRBDO51ZyyzB5jpzBnItsiFPNtI50ygdhut5WmswwNw0G4RzpCob8QuALFOYh2IlYk8uXNASvRl1V_5NeZzE8vT9JWr1wO5MHLVC7II7XAXy-mW15FSBYAJp9QmL9Rir9NhSmOZiDn-lgA3FqnydTMD5eH1KyfeSKmPkSE99xgQ4NxkysYsycY-b_MDBL2CDPS7Wzq-GBTfddRf-itGm1iT1k4ZUmJI3HZgwNVmT-UCJSsRq6ns4nBpkLocD9aCIHlKHJ2va-udivz-a0YbNmr5LyW0dPPXQ3SK_QJG-xXNVm3dVIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سال ۱۲۸۷، محمدعلی شاه قاجار مجلس رو بخاطر مخالفتش با ایدئولوژیِ مشروطیت با کمکِ روس‌های حرومی، به توپ بست، و بعد از اون
دوره‌ی دیکتاتوری و استبداد سنگینی
تو ایران شکل گرفت و
آزادی‌خواهان کشته می‌شدند
یک‌سال بعد با اینکه ستارخان تو محاصره شدید بود ولی جبهه هایی شکل گرفت و شمالی‌ها از گیلان و بختیاری‌ها از جنوب به سمت تهران لشکر کشی کردند، و بعد از به‌هم پیوستنشون، سه روز درگیری خیابونی شکل گرفت و در نهایت، روز ۲۵ تیر ۱۲۸۸ محمدعلی شاه به سفارت روسیه فرار کرد و تهران فتح شد
خلاصه که مردم حتی بعد از
یک سرکوب و کشتار سنگین
باز هم ناامید نشدند
و پس از اتحاد اقوام ایرانی
، در
نهایت به خواسته‌شون رسیدند
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68261" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68260">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دیشب تو اوج حملات، ترامپ از جمهوری اسلامی بابت آزادکردن یک شهروند آمریکایی که تو سال ۲۰۲۴ بازداشت شده بود، تشکر کرد
خلاصه اگه امشب حمله‌ای نشد یا شدت حملات کم بود دلیلش رو بدونید
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68260" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68259">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVt7muXNcQqNPtf_kX3fT9TUBIQcOyCZkGnLc-pn7dE059gxgIBTRe35g-eaN5LlNFwrAh03c5LDncaLeO0DU1-1ecNP5qnKsFBCIgfpysMDh6_YkCQTAah9bT-UCQSkAKytvN1HkCSRjog6kZV-_Ix1EZnYLj_S34JngwyvW-YRtWZB2HpJCQscopQqHjt7mUC3qJWKjxPRRhGm3vZvkSV1x-MIqJvQoHzWRFOsNLYFGSuSUB1h38rFRxiuKLCT38jFl21afmphSllhqEsPi616xkuG4jCIgAVnhpCwmekus33WwdkGBvOpUHHYtfqSvAv0YsoN9OXRfJ-aXIe2iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوارنگاره جدید میدان ولیعصر تهران که نوشته «who is D nexT one»و هشتگ لیندسی گراهام هم زیرش قرار داره.
همچنین ‌حروفDT- اول نام دونالد ترامپ رو برجسته نوشتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68259" target="_blank">📅 15:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68258">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💢
مرد پاکستانی ، عاشق محمدرضاشاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68258" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68257">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0Pv3tBKSnlFreuEgivy_5tm-mb3FglVxekoIxLKRM87V24yV_imjczb9UrNM0QVSZDoH9veUnV4mFmqReSOs0xMEetF7obmqxRQNW4zwBaWMh7SDHMX_JKaRifT99IO6zvGV4t6z4KgJNru582Jm7oX-BVluDFQYIt4gzn0IoIqC4OxbFCNooPsw22XLRibdwAs_zpcFM3ZQrPp8_GLcvKo3tuTY6mFsUAJLNmuzk26IqwU_Oq8b3Li1Ei2eAxcT2gUpmbgImSYDM5cieepNuzBRDb9tP50UM-HDF93HMjsQxkPfuo9-rPLTk9uqxWbys70fqh2uBivI5Xcj7MM3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نتانیاهو سفر برنامه‌ریزی‌شده خود به ایالات متحده را به تعویق انداخت؛ این تصمیم پس از آن اتخاذ شد که مراسم خاکسپاری سناتور سابق، لیندزی گراهام، به زمانی دیگر در اواخر ماه جاری موکول گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68257" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68256">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=BvqTMDTGVy23vvWqoUvYs27fDCrLaCS3QNss3RGtRaMMnrx3xr_VYgjjjZrkD5isHBCCRm7ISD2JB9AS9AuC44a5Cds0_57x1UXgR7tMhdB29eJ4eiOSQZFcgDv3muibC5dp7yg_PTTGMKrEu8Oi9tEKQnlrVKWZFISriwrj0SiHuFExf5I9lfTkVW6GUkPxDCqkWDIp3lGU4dVs67_LLy8vkRteHz11A5HemfZTdJSOO8PLpug978RpN_MvH9fvbNyNV4Y0-lgHadYTbThLuTxjpr49ewxp55IMvrJX724jHNtrBstXU9Wz-i42BFMUsMXLnJvdmFORz7qsGQwx-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=BvqTMDTGVy23vvWqoUvYs27fDCrLaCS3QNss3RGtRaMMnrx3xr_VYgjjjZrkD5isHBCCRm7ISD2JB9AS9AuC44a5Cds0_57x1UXgR7tMhdB29eJ4eiOSQZFcgDv3muibC5dp7yg_PTTGMKrEu8Oi9tEKQnlrVKWZFISriwrj0SiHuFExf5I9lfTkVW6GUkPxDCqkWDIp3lGU4dVs67_LLy8vkRteHz11A5HemfZTdJSOO8PLpug978RpN_MvH9fvbNyNV4Y0-lgHadYTbThLuTxjpr49ewxp55IMvrJX724jHNtrBstXU9Wz-i42BFMUsMXLnJvdmFORz7qsGQwx-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش مجری‌ها وقتی یارو میگه تشییع خامنه‌ای ۴۰ میلیون نفر حضور داشتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68256" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68255">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJqfYcnEabpNcbEhwORqh9wvCll2wmxFFreUbeb1u684Qog1FzRU44P3FXpb-ZAYn2D8tJmjqxilD_Sw38b6XP_BkznGhVWRxeDt4hrJxc05auHkWoC0p_S43-1X2ElYC6cV1STGU2k-hXOeS_9_0ApERcZ1mBj0OlY1NgiibNlBm65nj2YW2rOcSAsT9ERRAy9TTvGQIQwo_rIdTI7D_noYRSntvZ-oKtG0AKNjKl2DhTdOME9ij9L0Rh-mXvatXgMTaM0lKdKq2xBjZFs0LN4CkESmtsITOSC5nlz5fdK21kG3houtlID79EagtUYeuT12oy9JoDmBBJDrs4hF5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فینال جام جهانی 28 تیر (یکشنبه) ساعت ده و نیم شبه؛
- یازدهمی‌ها فرداش عربی نهایی دارن
- دوازدهمی‌ها هم دو روز بعدش عربی نهایی دارن
بهترین راه اینه که فینال رو با گزارش عربی نگاه کنید
دیگه عذاب وجدان نمی‌گیرید
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68255" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68254">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5RLqU7stY6ymB_8OHrRSvWcRhS6kqqjFQpz8ux48z0UpnFUNoKEdMnp0fdZdo0ASNbQwdbmoZ5nxwKvvPbqAiHEUWXhFRimLG_boc0kqE7Nlm94D0ndJdOMMs2Q1r-443rRr2TPvONQRmSUujU4sKCOqFr451uzwYHcZ_oHqce_kujfIfl1h5okvxSDYhDSTrRKl7Wo1e2DY9cfDwUk5tuFNMrsTbYTXtxM72rpX4sy8vd6rUxOgvYjHk8GaHB9w3m6h4BjengeXCneWcYvh8UNT7Vkg8l33wsQ9qPQOT2a_LychGPUAzW3-fx6bKPcr84tcXuRtOebgYNXW_LLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:  کارگاه قیرسازی حرم آتیش گرفته!  @News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68254" target="_blank">📅 13:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68253">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=KcscxkHrhTGmM7mdyk4tMmGzUnaU60t2EZpggMHES7FJcRIFl50St3cKwjumEPnHQBUXW_DSwKXi94zcH2j0JDrSM1gRIwSZmpGJpT3AjVlw5zPjqQMIJjoYbS3Ba1ihl7bf5qSY_yBqx-XJdomXnZOpjh5OgIQHos17_tl1aYHhyOTjHZYLHal1ovjdlR8R3ZKWX2fXMiM_7kgHZSHcY4pQTtxawvfHxxqEk2wFU_2q9hDalI7kwjl-HZKIX761PpyCeTRtoE7Q80mZpXTJ-sQ2pw3U-1Gt0TvcxKQc1-UPGTkXzlM3BoLiinOgvb2_WdELbNc41c0BMjYqd-M9Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=KcscxkHrhTGmM7mdyk4tMmGzUnaU60t2EZpggMHES7FJcRIFl50St3cKwjumEPnHQBUXW_DSwKXi94zcH2j0JDrSM1gRIwSZmpGJpT3AjVlw5zPjqQMIJjoYbS3Ba1ihl7bf5qSY_yBqx-XJdomXnZOpjh5OgIQHos17_tl1aYHhyOTjHZYLHal1ovjdlR8R3ZKWX2fXMiM_7kgHZSHcY4pQTtxawvfHxxqEk2wFU_2q9hDalI7kwjl-HZKIX761PpyCeTRtoE7Q80mZpXTJ-sQ2pw3U-1Gt0TvcxKQc1-UPGTkXzlM3BoLiinOgvb2_WdELbNc41c0BMjYqd-M9Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تسنیم:
کارگاه قیرسازی حرم آتیش گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68253" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68252">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDVDQAevfAOh4tfRrtyASgVn_xCX10583yR3tCY__7TuZwn675iJNbTNOgSjf47VHdwavPwmzdmTJQ8Ez3c7Zy3f7z174EWH2BP2_im7wa0oHL72Ca_vlO9Q5NczqPCukP2XDN4jj3hPn1lCe7HwlnXBZpXiZGvk86T29q7aKGfI_fa_bzR4RwdnjFu-MIfDDR3fuNDzGwpmvYp_4GJDOW5VZdc6_qlDW5nUqIU6eRvStp9oS6Hzzmxdwg-K6mgwbU1XY0PrIaE_6-SLOkdAx9WwQsLxC_NYTd5-RdB95SICDvmW-t5GfIJRqZliU6YhyKTbD-4T9GevpQBF4iKLGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتش‌سوزی در حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68252" target="_blank">📅 12:49 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
