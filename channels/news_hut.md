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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 19:23:01</div>
<hr>

<div class="tg-post" id="msg-68353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_Tjs3yAObjwngS8Hv9lNgInYkyQ02hJegwsUiOdEc_5z20vF2frkrE2LQFcG5N52C_zBkT8rvq9hXo_4_XaTK9MkY0QHWz2cridtWL8dTKnmdeiO--4Id3IrnxjjuBGltKFwzbn5W8Ug_YtwPYZ7xfKoLVFz4sfssinmqEi3J3H3YAjV7B91f3dyDe-nhZWAZlUwJhKabqbNJ-k82BwS9aFggHOuFJlYrhol6CUABjU3FLhbrrY4JlrBb5xv3dicAnFAG8XUppUCUuqej23igycAJzswwGRhdYVru5XevEV727wBvnELQDVk_0yKW6olVfvcWqSAmFl38o9NZ7UAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای ایرانی مدعی‌اند که به پایگاه «التنف» در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را اسیر یا کشته‌اند. این ادعا نادرست است.
✔️
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در این منطقه کشته یا اسیر نشده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/news_hut/68353" target="_blank">📅 18:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68352">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/68352" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68351">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/68351" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68350">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/68350" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68348">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHu-kqxgikpXkUo71iT_LhLcGkN0J7cDY6quTV1VBHam8KJk0SHLdHZ8F6h0ugKDqa_s73-QM3DEpwe8a1XbGeILNYA3SA0uagbT13Ce8UVZNozCuvaRG-2DQHMicflGTHGqb59g3xVVFRQidTLj2SalfC1hQLWTJ5NASEu3NURX2cWnhV6b39F_DG_YHGk4XZeuLVE31UTqJV4nyNOyxCq2qLKsmRjQBx2RjzmXfW7pGt70PA-mhNrdGxeq0szGIZ6wFWKXzrcejesdLiykBvpgCwIVQw8oXPN8hWY9If56LWvG3w2n8xQDHIzOG5aII_u_2PMl99cr32TR38LZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6De5kUpyXRL1NqiYJJ1cdw1R3GsR52uj2aLSEHocYqOMVxqM2NGSwxN8LVuH-yvnTuexfrz5BC8BJQR0qIqG5D8Z0OKzWKqpsdbTEOiPyTpt0egsAzQZkBxpJdIOx8VnzpQqoBCQcQ7p9z8odHyTFg8jWmyPQjhcTcyeBP1z7Dv59Jxo2ocmazhWwS_AOREShrHhDX55NmSoyK4RVlQz50NM4P8ogI4r9Mfuiw9bVPkPlxzsaolbLgf1J5nHusd9qrz3LUkJqTsroji_4FlehxmRvPlfxVoV0tLxrKIXX11BC8kPic6RhOQzZHb03Lz0rxBahT12NP3huiAGuM7Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدون شرح.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68348" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68347">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeOhbH0igCJnnENwNcnp-RWLBwwNVLlGQL2l_8V5S7OC-G8X-wwYlks7T0GvscnQaTpueJZvGXX3iFJJnyGRSPO1dbh54LRoS1ttLDRi1V96Esxn-6DoplkT3AZ0U-hayGoGFCQOazGvC04UtOSXhIyzWq5iYT1S7GhwBL4RGT2SupYD5D8MxsUfemBmYke9qbpFXE-vvbrbjL22ndbEcTOv0DFqwlLXnbgd4qRRBgTUsX6OabdYdVhUffHm1Kj5AyUwu4PS3Wc1txn1gNtPmvtoLWqrDZHi-9BtXv7QHWZlo_25Vbz8aZ3xmeFSDSLKLqbKdIe2quavR8bFZajnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سید مجید موسوی:
حملات موثر و هدفمند تا زمانی که صلح به سواحل جنوبی و تنگه هرمز برگرده ، ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68347" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68346">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2_AhHecTZ1NbIKLVSYm3DsEifTMZ_9TSU6kXO4fWXeMs3hD2_ArJEdaXy3ciQmNj7V_xzRcyn2FUO5V0g39cSHDBADV-Xai4_BRouYVE8U6yygCV9cTtAg987Hv9yf9ALYS5sJJE5L8Acaw3hsiF2geBJ0WGf0nonnKsuFDcT73kgHj6l8EMzzXd4IKPaTJPyvKF8O09x7HzzOp-FqykqyKjufanHl_T_SUCG7gnPluPs-vWjy-BvcaaxDYvh_SdSUEdadbxPDrq7VCS7LwyXEJAfSBvpyrsxZc3QHvoSewiDPYwWrZ1zITH82WAiw01Ejdk0Zc4o_FO6BKelrGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از قوی شدن احتمال حمله زمینی امریکا؛
بسیجی ها توی گوگل لغو عضویت در پویش جان فدا رو سرچ کردن و این جمله جزو بیشترین سرچی های یکی دو روز اخیر گوگل بوده
🤣
🤣
عرزشی فقط زورش به مردم بی دفاع خودش میرسه تا اسم امریکا اومد وسط همه از ترس ریدن به خودشون
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68346" target="_blank">📅 15:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68345">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioxqVO2YppG9C8xOF16wAPWGeeIeVUjpgy4JKIhhW_0oG5I9As4S-VMBUIHlOpoN64_-75CAQVT4mEWKG0s7cha5LuQIJqrwCY5LxgAg9bOIjzSVyAlqbFQ0kH5VIxqotwyKX1eq-bZAGRvquGe4xihHZiKHTLgeEKUAWxv0WSEkYqR_qHW5_EYvm8NJpFlLv7G1A8IcvmHab66Ru2P4CHk_GS5Qa7NHAx-Ck-ti06QDEkiL_ANFU0oSnj9m3lgnpOQ4JuJKMajxiIS7Pvh1rs9Dy8lFUvbF_SK-Hq--SkMjccC3E9a8cli6etgP9owjMWvnZx1-vkHSM1R61lCmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
همچنان آمریکا در حال انتقال تجهیزات و مهمات جنگی به خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68345" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68344">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68344" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68343">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
در یک حمله غافلگیرانه به پایگاه آمریکا در العدید قطر یک سامانه راداری بردبلند و چندین فروند سوخت‌رسان آمریکا به طور کامل منهدم و به چندین فروند دیگر آسیب جدی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68343" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68342">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68342" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68341">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68341" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68340">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68340" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68339">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68339" target="_blank">📅 13:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68338">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn5TQD-dCgfuSV2W5TNDbOMbV_ZL2oVcg5TLAL9GxBVNqKusEMM8tlv5ljEs270YSRmN8wFu8weocjHqQcd4vjAdlYbfUlrMUCtURXbpEYV-W_5_2noEdWlCKg_Ic8avQgtkpX1AcdjajTtDMz0VwNSEsOyKflIUlHg0h1akTd0c0FkG7_Z6k_EEBFWGZd5N12amNZ2URAj9Q7ds3WEQzeliHhqcZlb-ChHGk6T37gHYGTnnkxu_6Crbfdb7sHkDGnh62wbPa97O5PcB9QMPXkrc7FUUELicyPz9y4tY73MTfe0BFOD4BrJ_IghbYTsA0WYP_ecy2rT5drznNsxurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دقایقی پیش یک فروند نفتکش که قصد عبور از آبهای عمان را داشته است مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68338" target="_blank">📅 12:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68336">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MjBCDUoqa4p-VAonaxDpCcWNIhj6ZCBoSqi3dTcLotUhWONmE4uJorGwDCghwggRpPB1FP-GyIluJFsTbaeef-pHJYKgB1WZrSlKt5wpXoEfaMr9Mew8Bz7NGy-TUDa7O1awkgdO_e4P1rw1TWPPwErl7_Z3PkCfyR5srAxcIHfvFCVvlu0KSHVlwOW_w4Kp68oDmqHTDNIk4t-Szv5a0fy5vbfzlRZ6iO6nvKYKySagjN39XmBoh0-N6k7a1XPwUVMtXWniLsC3OA4TCE8hTGt9goFdOxpIVS2dqqyvkvIhoBh3kozFwyEwV372J5kvx1n8iViHxQkvyI7exP0l_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R41x1LdjwrSetQckUnmTPRnWBN7OTM3tpuAYG4OH7-qVVcclfilpUhKxeHRjweL6Taa_JlGJCT1-A7HUcKOffmAxa0cnnGA_1c01tMO100_X0A46sS7FtlFGV7BS9HER0BwxUU-5rkOYI-Jm1s8a84dp6uOz_x2r_XUPUstbjyRfqKMycJTkHVlAZS_1Le9r3JuOBSEuXKL5F3OWVAeOF1LNky-NR0a8vLWgt5mIGx9psbTvo3yrIaJ4AUBgApmE5Wc0EgjFuKSe3_WlDNZcyqynYgXhFcBedWhLe3umJ08NwHeophF3lYJv3jCLy7fsVdSnbtTm2XiUvq6Up-Vhsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
هگست وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد!
الان فقط یه خاطره از این برج مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68336" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68335">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68335" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68333">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPgzszBeCI3ocUP6ciKFrAVuB112sRQMNhaStdiG8shryZ_RW76qZt85u55sL_n9LHsb823HUipm0W8R4HxbE6rHLwPhlUSNL5zt5KSSQEM4n0q8zPTkM-YLFhjEBPbQKXhs3WmVRdbHppMKUZmgtbbKmzIvGJtyag6D5VUSeUpoP1G2SFr6kOqPCNxC8ItvahhoyslzXjogbrNMfPX5VB_3q7ZzW-QDs0zw59N1mVZpoq-T6S8ME_mW9hJ-rEvN5m6G8xfJ2bJSBD6JJvB0MMIeKJzBXNnKp8KbS6WDEM2F_ZLfv4kjOuv0pkwajtYpJQ63viHiwLIQ4cMYaE-3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1vY3k_RcNAjZU2JN1sbRlbkLoJwLevqalReK9JQ5pMmSgj4-ITUes5PPgc4TFgQdPTL9KUSR5LCOJ3kZL0mTL_gmBjEwv8VPVakgEAwiXHhAc0w_b-Xnx5XxKSzdlx8RObxiwgx8MGNuvMx2MtbBWuDYeCEvF0MSA4fhP3XbP4qglYCiysTY508KcEEM_b3E4KRmmWLGy0TGvRM3sIv2V6TdToyLJIN2Jm2lgp7_FrxGCzKUl_CYHUcMgAKF9XXYXIL49oNMfDy_emyRlybtDJ1j3fLbx2YOECFOyVZ0xRKGYAXjhDyMXILFQwDjzJTPY7bAU4Q3e00q4Na1_FJ7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
ما برای آقای فغانی عزیز اين چهره محبوب ملت‌ ایران آرزوی سلامتی و موفقیت‌روزافزون داریم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68333" target="_blank">📅 11:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68332">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=OCQfHu6v1UjVsZlBGq9SAnDymjqLF9pnQEj_9sSnweUq0ODtNyGUW4fkGgHsREgy2wLrKiUUzBC1pWkN5EaV26Ame-9MCDyorSWbzu1dAnzgP96aLzRwXG7Iwp5adXJ028uc6I9zDHbCdO9zjhA_Hc44u0Y6azqVsR2aHNEmiobb8gZaE-Rq8bYumr0GvD1bRvPV39FAw6ASZJ4tFRVsWi89Du03_5zAPcofel64mIJ-xdg9NPcGYnmhcoSI7gvTJBQJeRMZ06xk_4lgTeF9a3VVacF0yFdB9aHWmDOHfcRbm9nJGB00DP_XNpkp2iB1TaG4Ya9DveEL64flYreWOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=OCQfHu6v1UjVsZlBGq9SAnDymjqLF9pnQEj_9sSnweUq0ODtNyGUW4fkGgHsREgy2wLrKiUUzBC1pWkN5EaV26Ame-9MCDyorSWbzu1dAnzgP96aLzRwXG7Iwp5adXJ028uc6I9zDHbCdO9zjhA_Hc44u0Y6azqVsR2aHNEmiobb8gZaE-Rq8bYumr0GvD1bRvPV39FAw6ASZJ4tFRVsWi89Du03_5zAPcofel64mIJ-xdg9NPcGYnmhcoSI7gvTJBQJeRMZ06xk_4lgTeF9a3VVacF0yFdB9aHWmDOHfcRbm9nJGB00DP_XNpkp2iB1TaG4Ya9DveEL64flYreWOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وضعیت پل کهورستان در محور بندرعباس شیراز بعد از حمله دیشب.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68332" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68331">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuMyvMH0SSB_MAKNRGXMROldacrxD1MsTAbb77lw9-2UH-Jz9myIWDtaNBRmFvbTDs7poi5vhngeUlQ_yetQ6TiGhX5Hi-h191Sv5qVutEzJiusieqVlUQ1USizLXGfpekeC1XBNr4THYQhDRljRzoZCOtcIrKtT3r_B9OGkGEKirCPm6YNfE6qdiABBCoboshgfZK8O22RCIGzq32Up7kpvtkQFlmvU30JlSsQ5bY9FCttZOpI9e5ELMmXMfGCYTzLp5mzgSIhzZcufrfaQIFmUpQ2TVLQL9ShmfupaDRMWLq3d3oqdVOGguI-tPsRFgpkmsq29eu564dno1mHfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال استریت ژورنال:
به گفته یک مقام ارشد آمریکایی، ایالات متحده روز پنجشنبه چندین پل را در ایران هدف قرار داد؛ اقدامی که با هدف قطع مسیرهای تدارکاتی به یک شهر بندری و پایگاه دریایی در تنگه هرمز صورت گرفت—مراکزی که ایران از آن‌ها برای حمله به کشتی‌ها و اعمال قدرت استفاده می‌کند.
بر اساس گزارش سازمان صداوسیمای جمهوری اسلامی ایران (IRIB)، در طول شب پنجشنبه چندین حمله به پل‌ها در داخل و اطراف شهر بندری بندرعباس گزارش شد و بزرگراه‌های متصل‌کننده بندرعباس به استان‌های همجوار مسدود اعلام شدند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68331" target="_blank">📅 10:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68330">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60e986837.mp4?token=Fm7TnJvJ30NxdlbPs9-U8W6COsojL5x2eJ37fXfNhUzX3afOsCb2zwAC5AkT05-YHPKIN0GVzQn1NOmUZIKnzTMUH1bckq0ziiyzoqLhlts6bLOFkrCIrNzTbKBEDr0yr66bFOWvIOl4ftB0okW9FJerhzvzzFCt1ughvdhVVIBnxgsOso5ZMZAdMrPuAfUFNgJck7wwCkAXbpU2OT4vcoOksxnVdq-EsD2kVJvvNB2-m_dD5iHgTV7vnryr1WSF7Xp6xEJmBksAz7fVwbMz4267nWbtOlY4bw7PvrIvqDcxUxVRbr2S_k-0NPurq7hjRrzo8A2lX-sZFW-qkvkmJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60e986837.mp4?token=Fm7TnJvJ30NxdlbPs9-U8W6COsojL5x2eJ37fXfNhUzX3afOsCb2zwAC5AkT05-YHPKIN0GVzQn1NOmUZIKnzTMUH1bckq0ziiyzoqLhlts6bLOFkrCIrNzTbKBEDr0yr66bFOWvIOl4ftB0okW9FJerhzvzzFCt1ughvdhVVIBnxgsOso5ZMZAdMrPuAfUFNgJck7wwCkAXbpU2OT4vcoOksxnVdq-EsD2kVJvvNB2-m_dD5iHgTV7vnryr1WSF7Xp6xEJmBksAz7fVwbMz4267nWbtOlY4bw7PvrIvqDcxUxVRbr2S_k-0NPurq7hjRrzo8A2lX-sZFW-qkvkmJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، تیر 1403:
ما غنی‌سازی را بیست درصد کردیم جنگ شد؟ شصت درصد کردیم جنگ شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68330" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68329">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=lBI9SknJyeR5iSJ8oDDAm4QvzOwVwkDuf2iVKG9TejrGbaU9PDGmSxzN5dqCuWHWfmYNtxe0uZRtFL4Z9EVQzsoVdJsSNIJrTrxc1adppdX2Sx-a2WTEU3n2TkKz2ufKwJrkNKMInI-1GV9-z9-8yRYIe4PqX6MROsCjkX9sXtNlnOcJI2EhRBp1ctVKyikl5w8eALLHdmzjkqxrS5szKn89aKOa67cWz3jyLdAi5jvU8vXXGx58KsA7PyIAv5x_5jex0bJoW5l9V6amuNY41Vz5MjxQT02A98AwUz6Mtf9cGNM1q8hNuqcY6uPWZp2LRewG8fcKbc8YhBzRk8exag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=lBI9SknJyeR5iSJ8oDDAm4QvzOwVwkDuf2iVKG9TejrGbaU9PDGmSxzN5dqCuWHWfmYNtxe0uZRtFL4Z9EVQzsoVdJsSNIJrTrxc1adppdX2Sx-a2WTEU3n2TkKz2ufKwJrkNKMInI-1GV9-z9-8yRYIe4PqX6MROsCjkX9sXtNlnOcJI2EhRBp1ctVKyikl5w8eALLHdmzjkqxrS5szKn89aKOa67cWz3jyLdAi5jvU8vXXGx58KsA7PyIAv5x_5jex0bJoW5l9V6amuNY41Vz5MjxQT02A98AwUz6Mtf9cGNM1q8hNuqcY6uPWZp2LRewG8fcKbc8YhBzRk8exag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویر ماهواره‌ای نشان می‌دهند که آثار سوختگی در محل حضور یک سامانه پدافندی پاتریوت آمریکایی در فرودگاه اربیل عراق وجود داشته و احتمالا این سامانه  بالاخره توسط پهپادهای شاهد منهدم شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68329" target="_blank">📅 09:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68328">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68328" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68327">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OaoSaeF5awDI_4My3DhS_h9eVk3Qgp140lLK8lUvVDVG7NektRED5wMo_aHMtVAAAgL40x2qY5CF_Bj5a3eU_duByT-3QoFecWYi_rO6RFS4kE9aULkUOeqWbVAqzcUg_TMw4PlR3xPYujBwR_F2mL4CudXvSoMTngltdNQdplu7mRlMLkXkDC1W2_jZl0obzISVOEeLCkf0t_gHodknbDCXYRjvbABISEe3q4jbdLh7UCJPkoxtxkoaKladi9ZLCK7grn0t4rr_7Abv4KeSnzdni6VHIX5p54tMNaUIr9If37C4AazG-oBLFi2DD_Hdj3yd4rrrJCnAbacGAFxyZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68327" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68326">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
از سایت موشکی جم چندین موشک شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68326" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68325">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bee400515.mp4?token=ijITW9CJhPjTiZcTxxzYmXsOTGjesnJu8kb_ONMDyWaxW7oC2aMZoF9dY29MK3ePdjKHoeW29GQdllbZ5-d4CAMjruhTYvm_t8s2Mfk8tb2sT2sb7SKKBqRo3Y2ifPyvvpgOhTYY64IiTVS4CyVP0R0MSIq9AWGyqNcaV6ztgrZzId1sU36sCSTQpY1iMJ9RPd-jIcMhG4Ty1MbJ22QGV_X7xa6P5JaSSX7On0nYCI8jjO03ECyEyO3NHEv-7X5K8p3ER7WJdjm4VkKZTVK7c_NcOlG9l6q1L5BjCPbj_58gwC_545BkXL0T2D-1xMS_4pZMEj8sHQAnpY-QJRgsNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bee400515.mp4?token=ijITW9CJhPjTiZcTxxzYmXsOTGjesnJu8kb_ONMDyWaxW7oC2aMZoF9dY29MK3ePdjKHoeW29GQdllbZ5-d4CAMjruhTYvm_t8s2Mfk8tb2sT2sb7SKKBqRo3Y2ifPyvvpgOhTYY64IiTVS4CyVP0R0MSIq9AWGyqNcaV6ztgrZzId1sU36sCSTQpY1iMJ9RPd-jIcMhG4Ty1MbJ22QGV_X7xa6P5JaSSX7On0nYCI8jjO03ECyEyO3NHEv-7X5K8p3ER7WJdjm4VkKZTVK7c_NcOlG9l6q1L5BjCPbj_58gwC_545BkXL0T2D-1xMS_4pZMEj8sHQAnpY-QJRgsNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68325" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68324">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه پاسداران به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68324" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68323">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">روز‌ها و هفته‌ی آینده بشدت مهمه، مردم خیلی بیشتر از جنگ ۴۰ روزه ترسیدن، و مسئولین علاوه بر ترس، بشدت سردرگمن، امکان یه قمبل‌قهرمانانه‌ی دیگه وجود داره #hjAly‌</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68323" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68322">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/68322" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68321">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXNWdPSumPiL6YH9qdmR9EmGrRXjTtC2yxUgkNf4Pc7r1d51ItSNmKfwTlSR9rKPbw4bv4RLe-Jg6X5ZPXtjkTQMffCc9Gk9-LUoXKuqGp-PhW2eJeggafMmfGt1TJO6eutdt8Zg-bJbdVmBIsphGrucaAMbhK2e0ZmEWPQDRdtxI7dxQ4WCpN69ifZX4UGJ_o2pxPUGcD5X0vCwAZ0deOFIWtWfnwvaBiWsoyhixm9Xy6XmI8StFIc5mkSUYqG0yyQh04-pU4RfobzdDhIiS5i4rgHhwKm8EUxx7Jei3ot7f78y4nuYa4FLEfrLNwQtW0Upc4PAkYIBPz0gEgGwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/68321" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68320">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=C1UwiXGKADDwRVUMvNFcIJUSmimSINugBO9cjEDvopaOjGNCZlK1w8XC-H5nySe53oCxYxHUsHOLM2JKZNKloMZqNhJL4lAnuMtGovGlVBieZIy67NO5UX-_1L13OUlzVdw1QF6F-uUv251odrAC_tYVr4vhSDggoETS29IDi561EbQV2GQbF_g6bAjbEQl6nXUuNreSvFsi0KZxpiKbZT0KXg_jj4PegkMHU8U7LC2mUMnvDcejyVQQ5r4Vzor16vRfe-qUg7mtXs1VEnj90O-r0NwuqXhU-4A64_smqJwP0Z9Icj3UEyegPmySR-YJKK4WzUiwmULQ0gGfXOrvlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=C1UwiXGKADDwRVUMvNFcIJUSmimSINugBO9cjEDvopaOjGNCZlK1w8XC-H5nySe53oCxYxHUsHOLM2JKZNKloMZqNhJL4lAnuMtGovGlVBieZIy67NO5UX-_1L13OUlzVdw1QF6F-uUv251odrAC_tYVr4vhSDggoETS29IDi561EbQV2GQbF_g6bAjbEQl6nXUuNreSvFsi0KZxpiKbZT0KXg_jj4PegkMHU8U7LC2mUMnvDcejyVQQ5r4Vzor16vRfe-qUg7mtXs1VEnj90O-r0NwuqXhU-4A64_smqJwP0Z9Icj3UEyegPmySR-YJKK4WzUiwmULQ0gGfXOrvlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68320" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68319">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68319" target="_blank">📅 01:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68318">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
در حملۀ دقایقی پیش به بوشهر چند فروند موشک آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68318" target="_blank">📅 01:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68317">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
فارس:
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی در استان لرستان را مورد حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68317" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68316">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68316" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68315">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68315" target="_blank">📅 01:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68314">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68314" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68313">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=OePmuX4dWSXmS7BT8CaxiMy7QK5ILANFuk3ZhDu0VKFtH349m859jothFu7G7aRJrJ9m_VOJmraqhduMnhoFCPxdWIhtC0D_buFw5Da5_1WhfRObw_EfqGKVZWkBZUpk2XrgI3BwaHva49ElSjpjSon2c32YAJPeBbTl7Sa8BcdGCjgJS6G-gkkCYyntSaJ3Kx2Rykqr-7SXAFAz3Pk8g9oQnwitZHH0tTzsZep4vNZbvrSu2H0hY_jjQzP8Rafm_w1jp0-gs08aBg2ruYO7Rqlir2BcuutAz7jT58VP3miYfXUOHmV6ykY0y3siZJvdEGnAXe6w9lmYD7qs3QNGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=OePmuX4dWSXmS7BT8CaxiMy7QK5ILANFuk3ZhDu0VKFtH349m859jothFu7G7aRJrJ9m_VOJmraqhduMnhoFCPxdWIhtC0D_buFw5Da5_1WhfRObw_EfqGKVZWkBZUpk2XrgI3BwaHva49ElSjpjSon2c32YAJPeBbTl7Sa8BcdGCjgJS6G-gkkCYyntSaJ3Kx2Rykqr-7SXAFAz3Pk8g9oQnwitZHH0tTzsZep4vNZbvrSu2H0hY_jjQzP8Rafm_w1jp0-gs08aBg2ruYO7Rqlir2BcuutAz7jT58VP3miYfXUOHmV6ykY0y3siZJvdEGnAXe6w9lmYD7qs3QNGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو وایرال شده از حمله وحشتناک آمریکا به بوشهر
شیشه های ماشین فیلمبردار درجا ترکید!
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68313" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68312">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d811948267.mp4?token=tES7AHJinQeWoIgzDKIQzoM9lcEZ1SBe3tnUkGupQc2lChhBtaRGyzw79KCEgKIqRZ1AmfVfXPFl7bqmaeioXue5Ecf882pVqmYIqIpFTv1oFN3aON6ToAh6AgYtigpWSMZv-IXC7k1X1lQUcMh80tbyo0n4D7l1Xy4IkFCTJH361hfPOn_phFO-ku0xpmdfn3PJZzSZ4_mGV2RdlGcEKMgSPPv4OoQ9338dyV4RPFvy7ZoiZivYBsRVnF_yr5uD_s4-T5FQnsVDy8FBg7LLetXymK_wyJgpQfBWuo7L4u3DdoK2Q0ylAIZkQ9NIXzxduycOsC7ydfHyXnOuJRpwy78VbKDs1kPNkXPN_uZP-wJ-4V4TaxzdTVd5EJ6O5C3tmDGWo37yLYwarHwuXseAqfDysIhGp6PFVdmKeSOlOcR0LSPKaY3grkYdFf9f9PbgKF9ZZPeIIOh7nm5txuCCnBBDu1LSfcz1uqwadSz2A0CcTxzo_F3gG6kXrFj1891DiB9N1Ef5LR43tdTAlurSFNmq79Rinir_lBl_BeWD1vQcNmBhMyvIjyC7iHitIdcp3t8gYyTEbnn_cuAByIxtzeyleosTMkYsJwMOoypi2GNAbppfdnpkmuZB_AnHb7ZnLm32pG_E-rPAdGdjgKkgljx0dwdU97gQg82jKXMqegY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d811948267.mp4?token=tES7AHJinQeWoIgzDKIQzoM9lcEZ1SBe3tnUkGupQc2lChhBtaRGyzw79KCEgKIqRZ1AmfVfXPFl7bqmaeioXue5Ecf882pVqmYIqIpFTv1oFN3aON6ToAh6AgYtigpWSMZv-IXC7k1X1lQUcMh80tbyo0n4D7l1Xy4IkFCTJH361hfPOn_phFO-ku0xpmdfn3PJZzSZ4_mGV2RdlGcEKMgSPPv4OoQ9338dyV4RPFvy7ZoiZivYBsRVnF_yr5uD_s4-T5FQnsVDy8FBg7LLetXymK_wyJgpQfBWuo7L4u3DdoK2Q0ylAIZkQ9NIXzxduycOsC7ydfHyXnOuJRpwy78VbKDs1kPNkXPN_uZP-wJ-4V4TaxzdTVd5EJ6O5C3tmDGWo37yLYwarHwuXseAqfDysIhGp6PFVdmKeSOlOcR0LSPKaY3grkYdFf9f9PbgKF9ZZPeIIOh7nm5txuCCnBBDu1LSfcz1uqwadSz2A0CcTxzo_F3gG6kXrFj1891DiB9N1Ef5LR43tdTAlurSFNmq79Rinir_lBl_BeWD1vQcNmBhMyvIjyC7iHitIdcp3t8gYyTEbnn_cuAByIxtzeyleosTMkYsJwMOoypi2GNAbppfdnpkmuZB_AnHb7ZnLm32pG_E-rPAdGdjgKkgljx0dwdU97gQg82jKXMqegY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده آمریکا، دقایقی پیش تصاویری از عملیاتی که دیروز بر روی یک نفتکش ایرانی انجام شد، منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68312" target="_blank">📅 01:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68311">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دیشب که داشتم با دوستای جنوبیم حرف می‌زدم، می‌گفتن حملات بیشتر داره به سمت پادگان و و قرارگاه های نیروی زمینی کشیده می‌شه، حتی دیشب مثل اینکه به پایگاه لشکر ۹۲ زرهی هم حملاتی شده...
امشب هم که خودمون با چشم دیدیم ته حمله به پل‌ها آغاز شده...
حالا سوال همه الان اینه که آیا قراره بهمون حمله زمینی شه؟!
اولاً اینکه ما در جایگاه تحلیلگر نیستیم که به این سوال، جواب دقیقی بدیم، ولی شواهد اولیه داره اینو تایید می‌کنه، اما وقتی کمی عمیق به مسئله نگاه می‌کنیم خیلی موضوع فرا تر از چند تا کلمه‌ست و عملا داریم از یه لشکر حداقل ۱۵۰ هزار نفری حرف می‌زنیم، حمله زمینی به خاک ایران، برای آمریکا بشدت پرریسک و پر از تلفات انسانی خواهد بود، ولی اینکه دارند شرایط رو برای تصرف جزایری مثل خارک فراهم می‌کنند
اون هم به قصد فشار بر جمهوری اسلامی،
یک موضوع دیگه و موضوعی محتمله.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68311" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68310">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861fef7828.mp4?token=hMIqsXT5si2u1wW9uC_qgOAs9sk1fkLqk77-eXSgIMsigIZvKqMM6w6NEWRWpEHR0zMM--KEdzpnbHzZkv1ZReGkte5lKdqsBoDGXL9jrCF46gGW1OLSYK5IQF689FL_VQA22lIoldaZHknbQtG-vAedMhQK5ue_GiJpkcVQu9DmIpr1uEt-VwbzNttlapV7NGYYhiUZzgSztcDQyaXoCAgws-XcYxJh4j0Hji7viyBreGuMICc3Pa4LlBnNerbByPI2vM8amLYF8w8IqHBvMferKSPOxiuz03oV4Rwh-HVrrWNoQAGcMw5YH-8ksyEHWLE6O-QTCdFNMmSbIB5_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861fef7828.mp4?token=hMIqsXT5si2u1wW9uC_qgOAs9sk1fkLqk77-eXSgIMsigIZvKqMM6w6NEWRWpEHR0zMM--KEdzpnbHzZkv1ZReGkte5lKdqsBoDGXL9jrCF46gGW1OLSYK5IQF689FL_VQA22lIoldaZHknbQtG-vAedMhQK5ue_GiJpkcVQu9DmIpr1uEt-VwbzNttlapV7NGYYhiUZzgSztcDQyaXoCAgws-XcYxJh4j0Hji7viyBreGuMICc3Pa4LlBnNerbByPI2vM8amLYF8w8IqHBvMferKSPOxiuz03oV4Rwh-HVrrWNoQAGcMw5YH-8ksyEHWLE6O-QTCdFNMmSbIB5_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
تفنگداران دریایی ایالات متحده از «یگان یازدهم اعزامی تفنگداران دریایی» در تاریخ ۱۶ ژوئیه، عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «وِن یائو» (Wen Yao) در دریای عمان اجرا کردند.
تا به امروز، نیروهای آمریکایی مسیر سه کشتی تجاری را که قصد عبور از سد محاصره را داشتند تغییر داده، یک کشتی را که از دستورات پیروی نکرده بود از کار انداخته و برای اطمینان از رعایت کامل محاصره دریایی جاری ایالات متحده علیه ایران، وارد یک کشتی دیگر شده‌اند.
تنگه هرمز و آب‌های پیرامونی آن همچنان آزاد و باز هستند؛ مگر برای کشتی‌هایی که قصد نقض محاصره آهنین آمریکا را دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68310" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68309">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68309" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68308">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwVpsCKGSAlSHA26vepHuSZ8TmmE7tqXVwuAMGobqfgXyOnGTy0XH7Vr8t-4wGdJPAcLCNJQUELMMGNotRBx0cO_jVBHZRKszGgDtA0zFXaO1ozWhhtoCP1D3WwQq_nS_ntD3AeqeC5m3H7P1H9OvY_tYRUY7-GuMGVPFGpPj4jgLS6D6iPOfTecQRLifXzPCbCnbEDVbp2g6yXtpJkZB82uYltXBE4gx85pDTxyTbGjNzYCifUcwX5SiYZkBaI7JsnMOcXupLbI-74G7b4wSL4EHNrIcvgQ39JBubfDF9rznxkp7tnZ38ceaScFFIrkh6Pgyt6JFifztDrUl8MuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68308" target="_blank">📅 00:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68307">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
دفتر فرماندار هرمزگان اعلام کرد که تا اطلاع بعدی، جاده‌های زیر مسدود خواهند بود:
جاده بندرعباس - خمير - لار به طور کامل مسدود است.
جاده کشار - کاهورستان نیز مسدود است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68307" target="_blank">📅 00:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68306">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKb2vnjg6v_q7X4u4NZ2H-Qt71P-Ep7Qpc3XU3VyejyllzWh9rdjEzexWQV2Nr5rqBotDD2DDrKh3NNQNDB8VQIDjWXfuxo7b0DLRYFIdU0fWBqtSbuPGuSfTT2A_5K47mzInUmmP2HVRLjH_HdjoPycpUR4KXE_pmN4aPncu4yD2H6PkPIEpv4JGeMaXt6G3NkTXJ6_Tiv4MZRb6GCXp0NU7LLkoAcZI2-fnmH0_XMJ470MgWrvfJg86kn-PGKWZbNt5vKW1Yv-xjdWs4a3i4EqUXRtFsotn2avFG-3j4vSkEqRWafPvwe9o9P1lJLrOWqPS2GZ0nn0Tl4uZ5yZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رشیدی کوچی :
⏺
«حمله زمینی به ایران از سمت جنوب رو قطعی میدونم و به نظرم تنها دلیل تأخیرش، گرمای شدید هواست.
به نظرم تمرکز حملات آمریکا روی مناطق جنوبی هم در همین راستاست و ایران هم تا الان با هدف قرار دادن عقبه دشمن در کویت و بحرین، اجازه ایجاد مراکز پشتیبانی رو نداده.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68306" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68305">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxLml3hNlOdidyLj4LlIN72dPGuGqCw6O9VoaAXAy-TMl9GqOSql43xwMUUawMJt3liVk-T4vR2z1Om9U5mNYUcFikqYUKw1qsla-0wGuTheHjp_I3WC0iizVP4c-0VspkBUuH-gCVVNppA0r9oxBiXCboW3Y70jp_ZF47reOSH0iZlZus2xQ4Q_tguSX5AI-CmpFj4_KTHbeC2G3iPSJ3XF0KgZbDssh3UkLmsqGnAUTqAtroM2cQ0ATPZnf0bwCN1dDUgg12lVOzZuDYv9Kne1xk2dZaXwvixEkv4SOaSoJBw5cnQfw3p2jsGCuBfYypIoMTBwN9LosTPP6eF_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68305" target="_blank">📅 00:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68304">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3p60JbwY-ptXmOeNVjF7gGqOb-bKhdVduXumD5H4qM9W39VkCEE_yKETunORzv4xbkg52cSW2tSqljGeC9yPt807CttDu1zr2zCP3WKDaeslJP-EOCN8HaJ6PnPOW7Z9rgWxwVsHPDhSI1RV_SiFR3CiKRFSCLW2oQpn4df_rEH0IRkIjkG8xCSAHLWFDyxWPV16bWJ_Kh4x-rPH3UmIlqte30mRSQ9-D5q6wyTpEGNWZze-Tir5_ZqPQqhTO7nr_AgCqVB1yHoxSLRgcfweZnDtpEIBoBB_3h6OfYml_MnPRCvjCFSKn5fgfKUqskmaSk0jNsZP0maf5d14yav4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت   @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68304" target="_blank">📅 00:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68303">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68303" target="_blank">📅 00:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68302">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=iPJZSsRcdlqLYrXVRUS9TJjvRKQsVunn_R4wPtdDEzMTgONENtQMEiMmxLX1E1HK7ekpHgN82WRtNjVhPPrx8TYudae07lspjXRPM4yMQGgZbPy-7lken9_0GIDa7GLE4mIeODAaokBN1zBZPlYocPH80lH_CsQc3UtjC8wwjMIbMROcScnAXNlGBKZlQ5I-pihkLYYywChNH3--PnQNDGikixMjnbB7Onoz-p83AiVPQEJkx-E0a8Pa89dp1usuzAD7IrfW2HI-OrFOi-LF6iDEn6mqp1qctKtArDPPRCjDQqgpZpcU6uQCSmrFC5-sGJLq_dLry1g58rqEkhGsWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=iPJZSsRcdlqLYrXVRUS9TJjvRKQsVunn_R4wPtdDEzMTgONENtQMEiMmxLX1E1HK7ekpHgN82WRtNjVhPPrx8TYudae07lspjXRPM4yMQGgZbPy-7lken9_0GIDa7GLE4mIeODAaokBN1zBZPlYocPH80lH_CsQc3UtjC8wwjMIbMROcScnAXNlGBKZlQ5I-pihkLYYywChNH3--PnQNDGikixMjnbB7Onoz-p83AiVPQEJkx-E0a8Pa89dp1usuzAD7IrfW2HI-OrFOi-LF6iDEn6mqp1qctKtArDPPRCjDQqgpZpcU6uQCSmrFC5-sGJLq_dLry1g58rqEkhGsWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو دیگر از پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68302" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68301">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
تسنیم:
آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
اونا به شهرستان بندرخمیر و بخش کهورستان حمله کردن و پل ارتباطی بندرعباس به شیراز که معروف به پل بندرعباس - کهورستان - لار هست رو هدف قرار دادن.برق مناطقی از کهورستان هم قطع شده
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68301" target="_blank">📅 23:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68300">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=RA6nzQHH-aBSmHPGd544Uwfr_-by9bseJ6owThgGi6sWKpk0TW207v6yt8ytUmw9RBl7dtY1OXhZ_c6igDbRVY7gngG1t1z0hv1HMqtTQsPbRqJjlfkAhNrhvYx5PBvRyV2SZGaoIWwkW49-S_5NA7mXFMPhuyUsMhRICrahXVBFC1_HnlD1bT2UwC0b86sf8Eb59EbHmwwgLLX89EOYsHxM8YXCwEv26XzNu1jUrE2uJuPUHMEAuo4x4kPuKqVYXBqQT0OpfzF2ILNeXQnIIQkQQd0RgTOFvrt7UIcH9yWwhqArsJ2rInmDJjzTrTbt2_OknmpMVRFpk4-Os1ftzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=RA6nzQHH-aBSmHPGd544Uwfr_-by9bseJ6owThgGi6sWKpk0TW207v6yt8ytUmw9RBl7dtY1OXhZ_c6igDbRVY7gngG1t1z0hv1HMqtTQsPbRqJjlfkAhNrhvYx5PBvRyV2SZGaoIWwkW49-S_5NA7mXFMPhuyUsMhRICrahXVBFC1_HnlD1bT2UwC0b86sf8Eb59EbHmwwgLLX89EOYsHxM8YXCwEv26XzNu1jUrE2uJuPUHMEAuo4x4kPuKqVYXBqQT0OpfzF2ILNeXQnIIQkQQd0RgTOFvrt7UIcH9yWwhqArsJ2rInmDJjzTrTbt2_OknmpMVRFpk4-Os1ftzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
در کهورستان بندرعباس یک پل هدف گرفته شده.
موشک خورد به وسط پل، تانکر سوخت نابود شد، راننده مرد، یک تیکه از پل نیست، کسی این طرفی نیاد...
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68300" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68299">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
پل ارتباطی بندرعباس به شیراز و معروف به پل بندرعباس - کهورستان - لار مورد اصابت قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68299" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68298">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=NvgGhhaB853uMeDphXJc7Q7RiYFYPNReEaGqA3UXGnWzaJyS2kDYVUe55uwKSmX2G9KEp0tQl9gwZhhECAWHzDT7l0bOriw6XLnXQ_FMe9GyjVG2uQ0ZM7YIeSK4eAFev-R1f5ilJn13eadCyvrD1qYsm7-ataDyXPA7wVqbuh7ZyjciXkBekfxo0mE2mxqT8-6A9FWf9zir-7hXv4ibKspxbcd_3Hezil7mCG9-FDuof-TgCjxRur7c4BU5R9as-s5wPj_MyR_xR9nirKuPNmI3_GjE2yATBTz7C7TClQc0ROrK30sstIP24jQJvre9k4U2RBkEsFPnux6u8nJhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=NvgGhhaB853uMeDphXJc7Q7RiYFYPNReEaGqA3UXGnWzaJyS2kDYVUe55uwKSmX2G9KEp0tQl9gwZhhECAWHzDT7l0bOriw6XLnXQ_FMe9GyjVG2uQ0ZM7YIeSK4eAFev-R1f5ilJn13eadCyvrD1qYsm7-ataDyXPA7wVqbuh7ZyjciXkBekfxo0mE2mxqT8-6A9FWf9zir-7hXv4ibKspxbcd_3Hezil7mCG9-FDuof-TgCjxRur7c4BU5R9as-s5wPj_MyR_xR9nirKuPNmI3_GjE2yATBTz7C7TClQc0ROrK30sstIP24jQJvre9k4U2RBkEsFPnux6u8nJhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملهٔ آمریکا به یک پل در بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68298" target="_blank">📅 23:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68297">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
طبق گزارشات اولیه، یک پل در بندرعباس هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68297" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68296">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
به گزارش ممبرا ساختمان مخابرات بندرعباس هدف حمله قرار گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68296" target="_blank">📅 23:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68295">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
حمله به ایرانشهر سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68295" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68294">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlmKQl0rPFR9GUQN2SjW7LupPlN5LlGQxQrCNjT8o2KlmC2B_8ZjW15UMdFs1Mq5ITXCftBdaesQIT3KwheqQ3We2HGN43pkC3TJgiGEQgqHQb5hqjRE5y5MNzV1fHgtCVjlWTfOATpEcnfjKPMs21ey2BEbz57ugxKAEHiaTJ_yrR-yHWxLtLIP3Ubms7cGFLZYAwOtmF-FlBRhuCZ6JJMLKN2iab25rGfYJ0gPz-hd1e6LAikORqRCrP18koBFudhW--u-HzdqRwh-Eg7SrghTtGdEh58-Gw4nS2pOhi5oFFuebPcCkKmQwJWPvr_CZWP7WPyFh9GVokHMdXl2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68294" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68293">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fznJ9ZbUSKiuJD4LYMl1dzRq0nTltKKcOVp4F9OXR-0d2tQdmyO4IyHyn9FtO9KKHqr9IFW6taqZW4Eylf-qOeBQAYFMqjm8Kr1uQe44cCyQthsg_a4Be-6cUV-NgHkxq4seizUcZAST6JAt34yJGEucU0heletMjMsxP7pteZF57PkUPPtI9wlMA1t4KIu5d2X26BOep5g2fn07VbWaYR6h05_A7kjqwte4XQM0WVWfeIsBEZpKE6ogmJ06u-t76hB-0uFVe1Ad6zsJ97glsC23njxVhxJr71zcP9EmKxJ8jE1aH0079wBjp8rHIsnU7O5tphcK7EmBaCwdswO3gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت دفاع کویت:امروز جمهوری اسلامی چندین تاسیسات حیاتیمون رو هدف قرار داد.
از سپیده دم امروز، نیروهای مسلح 32 پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده‌اند؛
این پهپادها رهگیری و با آنها مقابله شده است
این تجاوز شنیع ایران چندین تأسیسات حیاتی در کشور را هدف قرار داد.
علاوه بر این، رهگیری اهداف متخاصم منجر به سقوط آوار در مناطق مسکونی مختلف شد که خسارات مادی به بار آورد، اما خوشبختانه تلفات انسانی نداشت.
نیروهای مسلح بر تعهد مداوم خود به انجام وظایف و تکالیف خود با کارایی و شایستگی، حفظ آمادگی و آمادگی مداوم برای تقویت امنیت ملی و حفظ ایمنی شهروندان و ساکنان تأکید می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68293" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68292">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
پنج انفجار مهیب در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68292" target="_blank">📅 23:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68291">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به قشم و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68291" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68290">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS-</strong></div>
<div class="tg-text">داداش ما الان تو کوچه ایم تو اهواز بچه کوچیکا ذوق صدا بمب رو دارن</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68290" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68289">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68289" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68288">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=d0hslsoJ8G6UkDJSSZnAqvnAN9-9mosjyOQFFRbNDxlKY6it2ZHLgScr3YNFSC7Zjnhbn1L1xN8JM1Qd_mZV2frkY9swsxUO8i_iWflMbmxc9JuY0MbGMbC_3yO7fyXUL8EvGjljXRQrFlh1N8g7k6K0so--LfZTz9d-DvQe-KXGfM_CgATx54Tc167HxHEYvq3tnCgbZNYj0d9NhmRsVsWKh8NGOWtb1dKZEZy02r-ZoR2GlenT61hg-Aq47wK2auweYOHyzKAyAR-8MwNRmao4kAQ4yj0evqoE7HmT6w5IH8dBbiNXdgEb-AEuo6_xJKRBUEn9xZd6Ouf1LP65zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=d0hslsoJ8G6UkDJSSZnAqvnAN9-9mosjyOQFFRbNDxlKY6it2ZHLgScr3YNFSC7Zjnhbn1L1xN8JM1Qd_mZV2frkY9swsxUO8i_iWflMbmxc9JuY0MbGMbC_3yO7fyXUL8EvGjljXRQrFlh1N8g7k6K0so--LfZTz9d-DvQe-KXGfM_CgATx54Tc167HxHEYvq3tnCgbZNYj0d9NhmRsVsWKh8NGOWtb1dKZEZy02r-ZoR2GlenT61hg-Aq47wK2auweYOHyzKAyAR-8MwNRmao4kAQ4yj0evqoE7HmT6w5IH8dBbiNXdgEb-AEuo6_xJKRBUEn9xZd6Ouf1LP65zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از کویت به خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68288" target="_blank">📅 22:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68287">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68287" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68286">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68286" target="_blank">📅 22:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68285">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=nxDINT3k8V9amuxX18agzSKOUOPDYphqqSpU7UPSgXRHqAyQVqFDebc8YVE6Y0V3FWid2qB8lh_zblRW8pvZ5xIeCe6rhTr-yTul6qOtHvNeMeYrTFpMLae4-yUfdlfxXqzb2DbfQ1icmMSfUOnXma-Rlh5FC2RAlqQxTFD5sLkC6OAxpSuATSGzRqqsprhja9Iefm3mUkLqM9krWZfN5ldP_63pLkXoCN6RZhyA76nKrTNkQz7_XaUKjPhY5F6OAoxRhWHPEwgP7UzdhwMCTLFTSc66ttHwzCi2YpInWSao_mjYpmzDEzY6MITinaRp7o86SoFZH2m_0d6vahC-Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=nxDINT3k8V9amuxX18agzSKOUOPDYphqqSpU7UPSgXRHqAyQVqFDebc8YVE6Y0V3FWid2qB8lh_zblRW8pvZ5xIeCe6rhTr-yTul6qOtHvNeMeYrTFpMLae4-yUfdlfxXqzb2DbfQ1icmMSfUOnXma-Rlh5FC2RAlqQxTFD5sLkC6OAxpSuATSGzRqqsprhja9Iefm3mUkLqM9krWZfN5ldP_63pLkXoCN6RZhyA76nKrTNkQz7_XaUKjPhY5F6OAoxRhWHPEwgP7UzdhwMCTLFTSc66ttHwzCi2YpInWSao_mjYpmzDEzY6MITinaRp7o86SoFZH2m_0d6vahC-Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68285" target="_blank">📅 22:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68284">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68284" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68283">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbWfCcvsONOCbSQnAlGjAkt0CUyCH_eJScxuBW-yS-RCy7MPinsbg77rtymR6BrzDP7h5AdpYPhaTxH2dpf7T78WxUV4Cv6tBv68CSbIs2qwXG3LmQbNSGZ9rfmOg_ENNHz9cN_ZSir40-A6-unEyd65F4Ij0WW1W9MWML0TfqgASn602drNc15VReWMM_H5GRLUViw70GeFdjLKSpoGoI8BQlwax51HTFqpaC8TDcln4IlU3AEBhME94RVBXTN6ShTLCcmuxdnkOajjNcZGTA_kuSFjOWbxZF3VjpM9UtOJu1xDRkarc3uqx7fUg9D1nEcP36tK_DS1i_wp1PqGOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=OkL5bI5JaoYKX3EGwr2Vb3ZPCsVJbY8o0Ht-1sFRywRMbAPVwtqVhn9Ggztmt4ZFFoey8FDVAiHfAscaB17sFgNCRNrVjnMvhFIJRFyXCRpG2LkYoVOi-2GsiWbjtzFU-n0Jyzb27gSyDwnwjDmCZ3-DOwmukmWlautlSd0dc6W7yhGwaXP88Ew8SWSACyXhh-fyN1K5S7h-SkQRr92Wk_cf6hHj8gewj4gFVN8bwf32c8Vw7pO8Rty9donKh_HGPG1JxG_rRclxuRyhM8GGjUxXArlKzNrSup153KTF4gYO2tcTfxHdyZupRLgQIV-zx2TrLxD-Mhm1rxlXB9lemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=OkL5bI5JaoYKX3EGwr2Vb3ZPCsVJbY8o0Ht-1sFRywRMbAPVwtqVhn9Ggztmt4ZFFoey8FDVAiHfAscaB17sFgNCRNrVjnMvhFIJRFyXCRpG2LkYoVOi-2GsiWbjtzFU-n0Jyzb27gSyDwnwjDmCZ3-DOwmukmWlautlSd0dc6W7yhGwaXP88Ew8SWSACyXhh-fyN1K5S7h-SkQRr92Wk_cf6hHj8gewj4gFVN8bwf32c8Vw7pO8Rty9donKh_HGPG1JxG_rRclxuRyhM8GGjUxXArlKzNrSup153KTF4gYO2tcTfxHdyZupRLgQIV-zx2TrLxD-Mhm1rxlXB9lemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68282" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68281">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-JqYFhaKGqcfWPcB97jxIGWpdmgkF4d_VsrHCdX_3zuOCNpcwIjVAgLOywVukPsK0ORJyEGsOxzypbC8TvkVso19oqeOIzjl8ilYYcpaMCeSzLbPtv6daZ_UxZm5Vq9bD-0r4LSaVCkbg6D6AK37PTA0kXv4fScoFWSae4shI81nE9wZVU8T9BoMTbRgZ8pFrWhuMu0Hr34Z7qnq7cMZBhvTjKNs0hUzxUjnGzCeOxuA93_rxNCyJuFcHDFmUSwpOvop--CQTfADc5KcVngpu-S4i2oSwCqq2baoRBmZCiKXQqv7BeyfJY7VTISNSzP-7cWVFJ5CHj4ySWn3ON8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۲ بعدازظهر به وقت شرقی، نیروهای آمریکایی برای پنجمین شب پیاپی موج جدیدی از حملات را علیه ایران آغاز کردند تا توانمندی‌های نظامی ایران را بیش از پیش تضعیف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68281" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68280">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68280" target="_blank">📅 22:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68279">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68279" target="_blank">📅 22:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68278">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
پنج انفجار در بندرعباس گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68278" target="_blank">📅 21:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68277">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68277" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68276">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=Wmvj1yAm_rFDtozcDHL4rxrEyl7sujAHsy3DhgEha3gi9wHyYdV7KvOx3_drvTno0yh-nyMk-ZdwA-bk-0x9TyrV3qwK4mhlfhCyZ5tfaPnQx_jpoioAmDT3ysww5m2QfauAxkDFQaRFsTntoeL8SBUT7KNX_Foivd-bxThlyWnrk8cCRaWUOdkGur3WRzeThD0umSYWA6zvK9DKDKoOnMuDOh1ZJzGXR2srfGJ5Kjm__iltClNXeRomTq_GIycTemHFWg3GoTos8wMihN7QRyiLHUG15hv7zAecAQq2UwdCNUnr3RE0EEiuICodJHuVKYe7J0PLdVDQ_qnLHhPr0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=Wmvj1yAm_rFDtozcDHL4rxrEyl7sujAHsy3DhgEha3gi9wHyYdV7KvOx3_drvTno0yh-nyMk-ZdwA-bk-0x9TyrV3qwK4mhlfhCyZ5tfaPnQx_jpoioAmDT3ysww5m2QfauAxkDFQaRFsTntoeL8SBUT7KNX_Foivd-bxThlyWnrk8cCRaWUOdkGur3WRzeThD0umSYWA6zvK9DKDKoOnMuDOh1ZJzGXR2srfGJ5Kjm__iltClNXeRomTq_GIycTemHFWg3GoTos8wMihN7QRyiLHUG15hv7zAecAQq2UwdCNUnr3RE0EEiuICodJHuVKYe7J0PLdVDQ_qnLHhPr0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت سخنگوی سفید کاخ سفید:
«ایران همچنان به شدت با ایالات متحده آمریکا در حال گفتگو است و ابراز می‌کند که خواهان توافق با ماست، زیرا آنها از سوی نیروی نظامی ایالات متحده ضربات ویرانگری را متحمل می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68276" target="_blank">📅 21:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68275">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=Ntk3M8Yr7Vh1_5wqMizwnYzlKXPIHJrKGACGcPw6RbbgjRTW-M5RnHJwfhAEDUGptX050zSVEqRzda5ZOI4IDV1ELm6jWM6fgismZyPhYf9Io9hpW7ROXwQGIp3CkUpg3a2yf4kbr3GnMGotUzUWtSmPF-JXVl_opDL5TaMFFvPrFnEni4qw1Qkh1JeZjGirbAyLfPGJFEvUPmdsOcU2n0CcNh4zRNOe4q_z9ydhElDHY1J4nODlA2cXbloWZb95W1-xvBLBIj_EerisUnpSfzZBplJTKi8jz6z46UG7WDOc-PMrSz8KESnYuNn-NUuq3xXlwKwxV6McLyqFTkiLbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=Ntk3M8Yr7Vh1_5wqMizwnYzlKXPIHJrKGACGcPw6RbbgjRTW-M5RnHJwfhAEDUGptX050zSVEqRzda5ZOI4IDV1ELm6jWM6fgismZyPhYf9Io9hpW7ROXwQGIp3CkUpg3a2yf4kbr3GnMGotUzUWtSmPF-JXVl_opDL5TaMFFvPrFnEni4qw1Qkh1JeZjGirbAyLfPGJFEvUPmdsOcU2n0CcNh4zRNOe4q_z9ydhElDHY1J4nODlA2cXbloWZb95W1-xvBLBIj_EerisUnpSfzZBplJTKi8jz6z46UG7WDOc-PMrSz8KESnYuNn-NUuq3xXlwKwxV6McLyqFTkiLbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز ظهر تو خیابون ولیعصر تهران،یه اتوبوس تندرو بی‌آر‌تی بدون راننده و مسافر به دلایل نامعلومی شروع به حرکت میکنه!
این اتوبوس میوفته تو مسیر سرپایینی و با ۶ موتور سیکلت و ۲ ماشین سواری برخورد میکنه که نهایتا ۶ نفر مصدوم میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68275" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68274">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNpU_SRBHO9z7M-WYkac_ptbGt366bkF3Df7IdQuJIu27i9GGe5LAy1ZXQXfDqGkVbc_KZncHngsrczC2-QhKI_tudKB7Cz8xE8WoGiU8JcsESHsWrd67TLNY2wPulJZ1mtBHbZnoLCXYqN0OIqLr4qYtaxcmDm5L_k9gj5Dz7ZUOHZEVvdSdA3_ToNQHpPWN6p6TCTaEoSE5DBksmgL_I0ZgLJdiSq8_Sn-iBjpOde8LmWoJJQbVa7BggJMc9k_AkARz0dkKvYAl45Co0jjFjgDJGwru48sllnx53Id2E4wzkQ8OOHUVoYZoUSRdTVjetUAt8GQi52ENSHkm53_Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68274" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68273">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdA_v0_1rOgO6SO3NQKffqXmUealDl-LRESnHpTTvFvuu2hxVqzfCkrIYL_-eRo9DOw-9isKFMrFbDt7OIGE_-a_Le_3WyvEt50x1bkztSIjXEg6N4_o-mDWMrHP42rSgKYdPn_7i1O-jZvxkLdKwPcFqiy8wgnV0Y53mjuuuM-UVHAwLKyEsFW-J2mbyLaJDjvb-mAISE0c4QVSn9thTXvGgNRE8W6NU2qycxKkX75VsX6WZD4EW9e3vCNYjQWAtSvNEQXTwlz9nJBbPRDX4xXdTiNzNqszCzTq4G1DQAF4KShkXHVULD21uYu1HAR18iDkcf-QLT_qA7J-TucxZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68273" target="_blank">📅 20:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68272">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
فارس:
حوالی ساعت های ۱۹ و ۱۹:۲۰ نقاطی در  بندر عباس مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68272" target="_blank">📅 20:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68270">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=apM5ed_8ZnqoKWrFXpaecYOXscXqMPXYAtGke7R6HZKAu6RKk1wQ9EJbkuv6T6IT12gdLV9mRTloyzZ3R_XOr_4COmkoYLMBV_WXXqHTrOyTV9A3-dgQmjHhuUFSOBot1QnsEADHm2UsrgevjSAo8U_YPTgyEFdmVmyJV0YYLLZSUxWKH2osNikayvub6mGGehAd9bq7OSdSPBPbLqoz-8v1DQv2ZPGHoWwSBH1u8Y0KarANlet4yXCFrdWJ3wZ3FUTerkUTSUeAZi8vrfx8QFhxVMk1Tv_Tk05RvI_K6ih8u0-p41NizniKJw2QvBfWZklysenvAUUUAg-65UX9pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=apM5ed_8ZnqoKWrFXpaecYOXscXqMPXYAtGke7R6HZKAu6RKk1wQ9EJbkuv6T6IT12gdLV9mRTloyzZ3R_XOr_4COmkoYLMBV_WXXqHTrOyTV9A3-dgQmjHhuUFSOBot1QnsEADHm2UsrgevjSAo8U_YPTgyEFdmVmyJV0YYLLZSUxWKH2osNikayvub6mGGehAd9bq7OSdSPBPbLqoz-8v1DQv2ZPGHoWwSBH1u8Y0KarANlet4yXCFrdWJ3wZ3FUTerkUTSUeAZi8vrfx8QFhxVMk1Tv_Tk05RvI_K6ih8u0-p41NizniKJw2QvBfWZklysenvAUUUAg-65UX9pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در بهبهان استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68270" target="_blank">📅 19:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68269">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=T8vDEMSsjC4rIbPTdYww9N7UIBW6rGfDbtB_nAubuWaychTzb8ESE6g3NY9JlzkTUYz3yrxv6RmaTE_2YVnAZwnMCf6lDRAJRsnJJJI68IWxVfJaqOKdOL6tEJpjioO8lupIYboiio63vX7MR2a__UR_uHUYJopORo6heN03z0jy4aag1k5ALSuHxqx-bKPe92BqE3YK1d83ef5tGqoTXWAg9SQg9pXuUOT_lFGdrPZiiUoAt_yzW7-QrxqQTHq9tFjcholfLEe4JZ3nG_qR1-xagN3uAL5Fl9E6QqJV9JewODXBvNwMEXMsn1D83YOBicMYXlthcu812jsCCa5qTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=T8vDEMSsjC4rIbPTdYww9N7UIBW6rGfDbtB_nAubuWaychTzb8ESE6g3NY9JlzkTUYz3yrxv6RmaTE_2YVnAZwnMCf6lDRAJRsnJJJI68IWxVfJaqOKdOL6tEJpjioO8lupIYboiio63vX7MR2a__UR_uHUYJopORo6heN03z0jy4aag1k5ALSuHxqx-bKPe92BqE3YK1d83ef5tGqoTXWAg9SQg9pXuUOT_lFGdrPZiiUoAt_yzW7-QrxqQTHq9tFjcholfLEe4JZ3nG_qR1-xagN3uAL5Fl9E6QqJV9JewODXBvNwMEXMsn1D83YOBicMYXlthcu812jsCCa5qTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای عالی امنیت‌ ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم، نمیتونم ذهن خونی کنم
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68269" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68268">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbtkBKVDJJMxbmI8LQW2YbiFmpNhng4By_YERv0BXrwJMYnsz25be3E6LVPpDrq-X1jzioUGjyIHdRkmiXFvWtXBRtYhxLeIds-eLxQQhD_3N4Fle9AAuqCr-FMDA71yKUPIpDLbcpBgItOpQ_fSJihpzz8Sla5JgFdNkZ6wsFJLWwQzdmUtwb0dvYq75vN1kAbcpOk0iI38MR-6DG9bMiXae1xa6EQ0LbveBLshkiUeheevBRjj1q_iIIc5yqgOp_IbYbziG1gL8gvNMEU1c5HDf45r-8dOS8IaPndDMQ0vrf72CDAstjY5OSYtF1JmrPtYPu53vGOhfg4830t5iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68268" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68267">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY-2eFlXwISQ1vITK48GBKGjpcXF1PgtLv-opHpzJJsCDv4EV3M-MilIsRETEVMvZtMEhBcAzMX2LW4524Jjatlx3Dkb09xmr6F5U2ECnXUS0MDzHnaU5DkyZYVmQLSbnCbhx3H_S4CBlxMK_vgEQSg6GvqzzlsVWBVvBywQvMA5v5UNSzl5lE0NLaCM_b_vyTfjesNiQnEdG8CZ1GCZ1ySWWy7DZA8gtVGo65aoWtDQ9GFvr3DCTXUVS4FqzMiJXjscSBjkzEmmoSxV8nsKxVkAPaYbQj-FWC9yRENqyYfY01GbGgxuUxuFQQlpjUs4iqkeqPsdW_Hfo51A_MQkLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68267" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68266">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06389032d8.mp4?token=QGoE_e_kyH8XyRDK_mOkL3pXOywg5frZRKodi1r1MihfphYdFuhReC9ekk46BEzp1YNp-Gm7vuiKUiQYLx9uWQxx9An7Kx8HPQ7LX_Sm-Yb4XLS4W-EAl3rJk1DIRTBRJqP7pUOn00EjwwH_AyUzluv50ZzsxHE3_jKXiff98DQzTSkhf5prB9CqFwdhtjfkxMT1bi6ynWOjNJrbpsog-ZFy1UcCaCF2hQo0tZMn6jqXqYs6n7uOUS4qtnyF9slM8R45w4cxLAzZtmI0ZORd7R2VgHE1oNXADKAkaEZJfAfTbID6EC6Rx_lz_8ZF94iZ_MFBLb9CmJRH72X43vXA7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06389032d8.mp4?token=QGoE_e_kyH8XyRDK_mOkL3pXOywg5frZRKodi1r1MihfphYdFuhReC9ekk46BEzp1YNp-Gm7vuiKUiQYLx9uWQxx9An7Kx8HPQ7LX_Sm-Yb4XLS4W-EAl3rJk1DIRTBRJqP7pUOn00EjwwH_AyUzluv50ZzsxHE3_jKXiff98DQzTSkhf5prB9CqFwdhtjfkxMT1bi6ynWOjNJrbpsog-ZFy1UcCaCF2hQo0tZMn6jqXqYs6n7uOUS4qtnyF9slM8R45w4cxLAzZtmI0ZORd7R2VgHE1oNXADKAkaEZJfAfTbID6EC6Rx_lz_8ZF94iZ_MFBLb9CmJRH72X43vXA7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne_AwwlrtbZOnZvgRoY20HK5kN6cgs10546EzeXzSuD6z_sl6GzFAZ4-5iNlQxbyh2n5lbZ6Gr_dXYfwWwQH2kEFJutlPwysp5H4RqBfrYD4G0i-avhkBVMhqM-zYClfEIYK4_OeMfvVffyUG4q4fU6c-3plCZVpo0JR7Tq32Q0mbRohk03JQ3ctFBru9hcGotJTrv08wJ_ujRciQxggSW9lpDtyIv4lgrGo1kcz4UKPwaa2AFXoS2HvaSGQ4yJfK9wegupGqW7JH7L2EAFFf-3vlfUxPdHN76ufiW5jSd2iUcD04DLiGZx102OajDzcH1FA_vgyWDwMvrQymFJUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
لاشه پهپاد انتحاری آمریکایی FLM-136 LUCAS در نزدیکی بندرعباس
پهپاد LUCAS در واقع همتای آمریکایی پهپاد ایرانی «شاهد-۱۳۶» و یک پهپاد تهاجمی یک‌طرفه (انتحاری) و کم‌هزینه است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68265" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68263">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=j2e3sKc0D06PquGsI6-A-AcJ_D2rr9X5dsYYkYfkHTBV_EznSaqbjhRSQZZ1MoIERcmA9IGrrI6qTyGxi-BGjvNkjAamxsRO4LybHyNx1Bi49KV3YDh_jG46mvGnkhaSbmXjrRMJuAZTjKlVWfeGZQiR3kdEkPJb038pE8JlNn1AdT2ySG0xJs8sLCEn7w8ukhmvulZTJ-uZhe2-9itEIeLWEb7n1Ywdk9M_nCEBioohACE9ucmsONjla2fvDasARgeTVzXje5TSDDxscNcQN9AXdeBtXgW9aQDjGDKQaQPnLveKLE36uQ318WHVosZU12CB8cg1kL9xakxPYZD95Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=j2e3sKc0D06PquGsI6-A-AcJ_D2rr9X5dsYYkYfkHTBV_EznSaqbjhRSQZZ1MoIERcmA9IGrrI6qTyGxi-BGjvNkjAamxsRO4LybHyNx1Bi49KV3YDh_jG46mvGnkhaSbmXjrRMJuAZTjKlVWfeGZQiR3kdEkPJb038pE8JlNn1AdT2ySG0xJs8sLCEn7w8ukhmvulZTJ-uZhe2-9itEIeLWEb7n1Ywdk9M_nCEBioohACE9ucmsONjla2fvDasARgeTVzXje5TSDDxscNcQN9AXdeBtXgW9aQDjGDKQaQPnLveKLE36uQ318WHVosZU12CB8cg1kL9xakxPYZD95Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عموپورنگ هم اینطوری بصورت دردناک برای مادرش گریه کرد:
من دیگه مامان ندارم...
دیگه در باز کنم کی بگه چی اوردی برام؟
💔
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68263" target="_blank">📅 17:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68262">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=GtEUx9TM8S_U8W21X3v_Y4zztYZT4ww-cnM-9TJqLQzAFK6KLSGACVT1_3q-h3UsTryLEAKqkOuFnQ54B-DSQ_y-bDoM-412Jyrl9O8HKf9sk3VYbuLldsEoauxpGmYeGWzhKUKLpu3vV3lugwm1lukCfYLo2CZ7Ru_wUWXG5yhGgj6LXkmfKOKQN2ZbXq6QERyNI71rMA5JutZ6Gb76NFCIykhCa9bZFLiCSuuOt8aAGvL4t2g9r0piA0GJt5uUmHtBxbBcUOf_konTGy3BZLidN6liBYUzD54efOLKeEWG6NK_jCll6Jp1eaubzBGn5wlU_vncLp52u4S_XgvmvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=GtEUx9TM8S_U8W21X3v_Y4zztYZT4ww-cnM-9TJqLQzAFK6KLSGACVT1_3q-h3UsTryLEAKqkOuFnQ54B-DSQ_y-bDoM-412Jyrl9O8HKf9sk3VYbuLldsEoauxpGmYeGWzhKUKLpu3vV3lugwm1lukCfYLo2CZ7Ru_wUWXG5yhGgj6LXkmfKOKQN2ZbXq6QERyNI71rMA5JutZ6Gb76NFCIykhCa9bZFLiCSuuOt8aAGvL4t2g9r0piA0GJt5uUmHtBxbBcUOf_konTGy3BZLidN6liBYUzD54efOLKeEWG6NK_jCll6Jp1eaubzBGn5wlU_vncLp52u4S_XgvmvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام:
هواپیماهای جنگنده F-35A متعلق به نیروی هوایی ایالات متحده در حال سوخت‌گیری توسط هواپیمای تانکر KC-135 هستند، در حالی که در حال انجام گشت‌های هوایی بر فراز خاورمیانه می‌باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68262" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68261">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKnrbXAgKSaw8GVsEejGt1UAIdv-szuZNQZ7mQzAl7ZVLK6aV_fzzYed3SFzjE5RQxQIjoDPUxmZNnxNbSVMtIEUGo4-n3hVUkYTx3R8Vx7gfJW3I82V2EQUcu0VUxqZ35YUAxuaGTgXIqu_CjEIhtwHa2zhIEa5Kw4hJhylhJC578SYu1_Ndsp9yjnSKVkHpf3zj9-kJbQH2-MBmUCsVeJ9ONcRQ4muxSVbFRbrl_BNfmmwjSW6RrgQJVMZwN3ieSJd2oZmsTngAEXVUAqVO46eZlt-R5C-Z2ttfGl267V0qJ7DsiONUGMTU2flTXT-F7xG4gneDHlM_0Fa9gT9Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دیشب تو اوج حملات، ترامپ از جمهوری اسلامی بابت آزادکردن یک شهروند آمریکایی که تو سال ۲۰۲۴ بازداشت شده بود، تشکر کرد
خلاصه اگه امشب حمله‌ای نشد یا شدت حملات کم بود دلیلش رو بدونید
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68260" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68259">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yqh8pmAijJ9lWJqMnu74o4IHjJITj_D72-lRfCIHZjhd4g8QiNbli8iT8AFr_JBaQuopWkguP8dcSQjHxqEzavYFJs7jACJFGdef76FDsmSmwXdHpDt5HS84lF_L_GAwVCCGzf9-j9GrPm5jVQY03etEzMkd9WprFsJMiH40wJiiNEIf9WB9CVPZOiUUBiVZ8e_Ystjhn-AQJLHoSk5OOG72p609KaJEeQRi45eLe-4vWZ0bOy1ZOmdH3lIoVvHT4APrJEAGTSpEI5Yc01gKIlQ5jtRgU128aEEJh4kXzKFSz1kvVtwyLYaMTwIOLz70rvak8-K1fKOM9ZjQdtEfjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوارنگاره جدید میدان ولیعصر تهران که نوشته «who is D nexT one»و هشتگ لیندسی گراهام هم زیرش قرار داره.
همچنین ‌حروفDT- اول نام دونالد ترامپ رو برجسته نوشتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68259" target="_blank">📅 15:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68258">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">💢
مرد پاکستانی ، عاشق محمدرضاشاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68258" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68257">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlCC4P5IAso79YqeUM8M-ypT9vbbaamiskhLO068YvTQVvYIGjvbHWxl7hOcltiyO4afK5TKP9sW4jzcfJiSSNv4KwwRitykBvowkBzPhBUX8Vv5Vr5Tm9Rvrzxw8evk3T8aXn_lQaxeB_gbGTMJ0MEtBqSuvAc4WM7-kk9eii2v2QUoGUpRAx0b1_wehy7Ky7qhjpIX4LyhQ6Py2mDCjWKKTLNE3KREWSRZnPK3DiQBynN9Cc2XbKytzN-q0RnLVrrfQss3zN1oQGm15WbHbiEitMn9G1KCH7xqUXX6vSGbtwc02Enm084iAZphJc9H1XfBMEFDNbVz4OahJ9kfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نتانیاهو سفر برنامه‌ریزی‌شده خود به ایالات متحده را به تعویق انداخت؛ این تصمیم پس از آن اتخاذ شد که مراسم خاکسپاری سناتور سابق، لیندزی گراهام، به زمانی دیگر در اواخر ماه جاری موکول گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68257" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=ajPh0LZUvoIUJGVLX01CgYKEMqr_lzZtGgiIrsJK8SOnyEoupVyiqvFmjke_t-g337hYntx29mIP5FFvlgwnvrjKwWCPiZfh3xEh1d-_UgGfef8TcOg85yGSyH-h_yKMdCTKQlFAxygCmooctteCKwJPdGZoDmSaM-6Mu3UM02HoaSo2Mis9dpDGB7Ai_CLaqe8umDbDZCjUZjNqzV2GkqE0TU_a5ACrOrm7V0a-eVb-hNpIFaM0TMtjn3Qda7ZTWRdJyWMlOjmwAldpXeHNYn7OhhY0WUdYDoMNfoi0GMyMtwppsTmF4wu5SeU9Ig868srD6XlSqNFlUOucIBPsXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=ajPh0LZUvoIUJGVLX01CgYKEMqr_lzZtGgiIrsJK8SOnyEoupVyiqvFmjke_t-g337hYntx29mIP5FFvlgwnvrjKwWCPiZfh3xEh1d-_UgGfef8TcOg85yGSyH-h_yKMdCTKQlFAxygCmooctteCKwJPdGZoDmSaM-6Mu3UM02HoaSo2Mis9dpDGB7Ai_CLaqe8umDbDZCjUZjNqzV2GkqE0TU_a5ACrOrm7V0a-eVb-hNpIFaM0TMtjn3Qda7ZTWRdJyWMlOjmwAldpXeHNYn7OhhY0WUdYDoMNfoi0GMyMtwppsTmF4wu5SeU9Ig868srD6XlSqNFlUOucIBPsXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش مجری‌ها وقتی یارو میگه تشییع خامنه‌ای ۴۰ میلیون نفر حضور داشتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68256" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhHfsvaZKADWKb6KYwWOrf7WrnhUV48SMSjyuo4p2kSqiBHDOus9qu6MYCdVJo16hEgfiR8oUYMawOn6vyTyGloY4yoqj5mJFaBROGg39DthPuETZKgMo5v7Ezn6XIhBY3PhrLz8421YA07ESqWNLwy-_wnO2VV0cIduIiMSrPlLuHdDbvQaNDIOIntrsbztXlXBhFGglFUtjkARlEh__V0FpPn5GsAjx_VUgz2Tyx4XVJZ1lw84bSI_z_lB5CxF5PYHe10qkBtUDfKpoeE_pr_LmsQoscoxDGRzlZ6rjp4I2xfoazOYXgYWocOvQPERWb9NIHIMLuw3h02Rn4RAEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cbm8fPLkJUMyGtDUagGp75v-L-ygbdwAieMgdKuzHwooGGqQeSZDpor8_GBuKBlPNsAemDAh8l249j-9YdyffOZjeU3nqTQ80KrbW2opYl7norOUMoGukBoEWmsOnZJLxZTzl2X0Rfy70680Hw2iG2o39vL3ZzylALj5l83O3Kk0s3knvDV3D6DO2OGwuKQ8USYAtPUN4ZVF2E6q2TenXhK32tF8bWi8DDqYHasOx_r6O1pwXR742JW8JnwIHgmUa-o36qu6uNtGCD7GcFd0k5Mt16ZnXm1KB-RMLz5lpPEI5BziZ3tHhI6oEB6MJtmBJ3BwA934lFHbBsLVSuybnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:  کارگاه قیرسازی حرم آتیش گرفته!  @News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68254" target="_blank">📅 13:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68253">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=XgY67zhdjNP6en4mAExqOSUMEkZvs-bZSyTh-evHc3J_WiD2NGd5cYQqbD5XXHr1tQoskqYL-4mOElUkAoA0VXbVnwnYsJx0cKiws9Goj8ixkznD2HKXkn0Voo66om5lKfPb_6pCpsjdUXxh7cKIxTt6_rPUufsr9DknM5RG6jrFMf9RitPYiPTJ-L6VCZX2SrMP_nCsCGtbwGexh9mUBnlmMk2l2xsJHYa8WP79BWcSRqJUsj3GjRnSyKnKAP1BiXafA7AsAngNQZ51nrPE1r62kSEjqu4bm5on5U8kyWKiEdRfv1JZZHwZU_rtINXicwBDGSR4hnuSjIHop7Vp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=XgY67zhdjNP6en4mAExqOSUMEkZvs-bZSyTh-evHc3J_WiD2NGd5cYQqbD5XXHr1tQoskqYL-4mOElUkAoA0VXbVnwnYsJx0cKiws9Goj8ixkznD2HKXkn0Voo66om5lKfPb_6pCpsjdUXxh7cKIxTt6_rPUufsr9DknM5RG6jrFMf9RitPYiPTJ-L6VCZX2SrMP_nCsCGtbwGexh9mUBnlmMk2l2xsJHYa8WP79BWcSRqJUsj3GjRnSyKnKAP1BiXafA7AsAngNQZ51nrPE1r62kSEjqu4bm5on5U8kyWKiEdRfv1JZZHwZU_rtINXicwBDGSR4hnuSjIHop7Vp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تسنیم:
کارگاه قیرسازی حرم آتیش گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68253" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68252">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjDBVB1tciCfbrtP6ub1pqth7qnOSu6AbvedDqVkxPF0dSOGwJeP-_1MDALOopZTdEbIJvo9U0BHH2j1XPi2Ojnyc823N7ocE6hQlpBpLNJ1IeDyKHxwGTQ0u_659SAiyJljEhlBgGfg_3lxufTYPCtDiXtNXE084sWYigC6SHmlnlFZxaKCKMNAIisHeNachWYLN1wsaLbobanlVOuMKEx967792kzW9HRcx2GEEcjVvGcqrDJqk9ifPkxnN9--sclA7XGmBbCdY5RMk26MiTSLrTzAGjwPenSCngIoqx61VObOv3-Qk1Al15Fb2vmxXSwNblgi3GfCPJ9JYnXDMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتش‌سوزی در حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68252" target="_blank">📅 12:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68251">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314324694e.mp4?token=a_AkPaM1xHSQ5jfitqeSSOE-7Xq4AXITFrhkXSznhZJ4-TfDNoLgYdoi7CvGws0zSTewkoj1bsynCfxZorkVzn4hykTITnNPWghDzG9OHJDVB7tA2eiKZ6Di-6udn83q1M_iPQySZFTJo5wn3ed6lIHWPk6bl8s76bmFTuyTknZiBuxTFk2WN_1boXDDZpTE2-p4SnPGFRcHYyNZv03Z9eYvMTQsSEGFzg6C6G_Z-cZVkHzeShMcoSW2Z2FdOtTJoW24Jco5wEyLtoQxqDq98JOYKOgkJLqmDiEU0V9t80sesOIR-caTYsS11WApAqp0eW_2V7ilRXf_yxOn-gUGaoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314324694e.mp4?token=a_AkPaM1xHSQ5jfitqeSSOE-7Xq4AXITFrhkXSznhZJ4-TfDNoLgYdoi7CvGws0zSTewkoj1bsynCfxZorkVzn4hykTITnNPWghDzG9OHJDVB7tA2eiKZ6Di-6udn83q1M_iPQySZFTJo5wn3ed6lIHWPk6bl8s76bmFTuyTknZiBuxTFk2WN_1boXDDZpTE2-p4SnPGFRcHYyNZv03Z9eYvMTQsSEGFzg6C6G_Z-cZVkHzeShMcoSW2Z2FdOtTJoW24Jco5wEyLtoQxqDq98JOYKOgkJLqmDiEU0V9t80sesOIR-caTYsS11WApAqp0eW_2V7ilRXf_yxOn-gUGaoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام تصاویری از حملات به ایران منتشر کرده است.
این تصاویر شامل برخاستن جنگنده‌های «اف/ای-۱۸ئی سوپر هورنت» نیروی دریایی ایالات متحده از ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس آبراهام لینکلن» و شلیک موشک‌های کروز «بی‌جی‌ام-۱۰۹ تاماهاوک» از ناوشکن‌های موشک‌انداز کلاس «آرلی برک» است.
اهداف مورد حمله شامل پرتابگرهای متحرک موشک (TEL)، سایت‌های پرتاب پهپاد، هواپیماهایی که پیش‌تر قطعاتشان جدا و از رده خارج شده بودند، و یک دکل مخابراتی بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68251" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68250">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDqmEgcZ_-oJBnapMwwJJG4NnxSno2EgobOBiHHYQtW-nlnM6fvscRAN_g1pJiLzKbVsnjO5A09cxROv6uewpgQEBmlK5qmowy7D2G_IX6wxEbgN3gaJ70Wuzli1Oflyr4W4j8T9WGldpCbP2r3BfmpFfxLdqhnVrUYrrtun_usioT_c62fAoi6z4riBS49H5yYUR7DL4YAWRfrVcxfKW78scH2uD7WSdipUM6aw-EJfWxEV2Cs_7KhveHd_GNzNQiZN0Ro4RIwSxptY8hJge1FEQQdRjoRJRtJLKE9OPAckbVWBrnWE5flVChYK8VMK-NOqc3HuF-qc93KLQtAhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ:
ایران اجازه داده یک شهروند آمریکایی که در دسامبر ۲۰۲۴ و در دوران ریاست‌جمهوری جو بایدن بازداشت شده بود، از کشور خارج شود.
این زن اکنون در سلامت کامل و شرایطی مناسب خارج از ایران قرار دارد. آمریکا از این اقدام مبتنی بر حسن نیت ایران قدردانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68250" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68249">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=TRrQLUMDLVNttPqpHdudRrMeg6f3Kvy-fG_HaDqblBdxVtTn_NwJPHNTuJLlFaqJqW9VXDS3rxduOrgwl867rhOKy2S0TvLGt45iTPdTzJhSG8yLTrfwBaxpJuSvgDP0tjIk4nDpxg2PeLquybFR0fuCRYntuH3tFfhHnTvQd6jIc8c87tjfxHDSObmEP4z6RXcdjorUmf5HKxMaNynu3UY-OT7D4qIzBLj_PfLyEBL-8Aykou8rKVDcpVdhZqR62EO-6TdWztzu1-PyTpNHOzpw8oc1LVyCOfVRGjlPvgK7zalDHR8k5-Ci467bEQfgd35qDZn4dXTYihrIOd5YLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=TRrQLUMDLVNttPqpHdudRrMeg6f3Kvy-fG_HaDqblBdxVtTn_NwJPHNTuJLlFaqJqW9VXDS3rxduOrgwl867rhOKy2S0TvLGt45iTPdTzJhSG8yLTrfwBaxpJuSvgDP0tjIk4nDpxg2PeLquybFR0fuCRYntuH3tFfhHnTvQd6jIc8c87tjfxHDSObmEP4z6RXcdjorUmf5HKxMaNynu3UY-OT7D4qIzBLj_PfLyEBL-8Aykou8rKVDcpVdhZqR62EO-6TdWztzu1-PyTpNHOzpw8oc1LVyCOfVRGjlPvgK7zalDHR8k5-Ci467bEQfgd35qDZn4dXTYihrIOd5YLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پهباد شاهد در حال رفتن به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68249" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
