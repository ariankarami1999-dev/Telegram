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
<img src="https://cdn4.telesco.pe/file/anymac9LebR9i6HerokMfJa6HRXRmTX2V_Rxbb6g2iAtPyvYYWhdPM0nycYRXy9h7L_2rvgNANlDNUgmdi1UPHy_AkKJ_dKtryczXXgX0SizWuBQynYE0iDcr4bBCfYD9kObwfItz5xe_IQZQcOKq--dybrrp_rYJicRHzAVmGv8ai4fs-75UqJtSeM1xFW9zhKEr1MAqlr8SyX9PQe0udjYrXGXYiQUsAFSqsBwS1CgDL-R6zs5wAkD9gizUdL6Z8dEg8j1Fd9kRs6wS-BUOouoqGFmZ119riGymD2TQ414MNNumox843QNmP77tPtLhGVzhTcDWHq8eoT6FkLYug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 14:17:46</div>
<hr>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=SgY0lnUEflfjq2h0_5-7wOTgchdv0CaiLtD6r8Olo_jLpzWcDzfjONKbSHyxOj1F3KkVH0i-y9MXY13OHX3EIkl0dfQNeQ_FY-Z8EAx5G-J_o16jpic7ooirpYmLn7IiI4pTMyJlSEHpJp7Gqc2L7QqRWkSxBzdq3HAM9vqzx8OfR3lm-m6AE2lGIGNnAV-hVoP_X8MfQgT4wnR07x9BsbDjCVmpgItpV0ciTiUYbzYUyJmMrCO6ut7bTBZVabm6Qlfhy19asfJMi2seNCIVD2_x5tL9Rm73V1ZsEEqeyZqGhY9qaJMoXwEk8RpDlokeYvKczoyirKdy4rt70YDAziOXVQQjk00bQG1dCTAhHk4n-laE6eChY41n1MNXlZBV9GLHM4savoO1h-s1XIrd4BIRDRgxymtr8quA5mnUfcMp_CdnhQOLXb0sdMO99h4eyx7jd9YI4x2REdBpGi-nYZVLm2a22f4q05RdDnbUFwXQ6zk6svc3UE24_odfhmaD1kTJfVcyMeXPp8TRRYHkraxVsMkIwrhEmyDEVmdxE55wmaLU-uXVbNkpSYdC9DOs1K5flfgX7fEzqwlAGTFR5R__OUK_xj3ol3YPR0q5OQQ8ykDgYdoBAFphUhlkfIWrbqDzg3-ylNfoG54xFqSvxTTTTlYAkth0caDkx0WEHlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=SgY0lnUEflfjq2h0_5-7wOTgchdv0CaiLtD6r8Olo_jLpzWcDzfjONKbSHyxOj1F3KkVH0i-y9MXY13OHX3EIkl0dfQNeQ_FY-Z8EAx5G-J_o16jpic7ooirpYmLn7IiI4pTMyJlSEHpJp7Gqc2L7QqRWkSxBzdq3HAM9vqzx8OfR3lm-m6AE2lGIGNnAV-hVoP_X8MfQgT4wnR07x9BsbDjCVmpgItpV0ciTiUYbzYUyJmMrCO6ut7bTBZVabm6Qlfhy19asfJMi2seNCIVD2_x5tL9Rm73V1ZsEEqeyZqGhY9qaJMoXwEk8RpDlokeYvKczoyirKdy4rt70YDAziOXVQQjk00bQG1dCTAhHk4n-laE6eChY41n1MNXlZBV9GLHM4savoO1h-s1XIrd4BIRDRgxymtr8quA5mnUfcMp_CdnhQOLXb0sdMO99h4eyx7jd9YI4x2REdBpGi-nYZVLm2a22f4q05RdDnbUFwXQ6zk6svc3UE24_odfhmaD1kTJfVcyMeXPp8TRRYHkraxVsMkIwrhEmyDEVmdxE55wmaLU-uXVbNkpSYdC9DOs1K5flfgX7fEzqwlAGTFR5R__OUK_xj3ol3YPR0q5OQQ8ykDgYdoBAFphUhlkfIWrbqDzg3-ylNfoG54xFqSvxTTTTlYAkth0caDkx0WEHlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 643 · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTqVQFinp70oz5TRHA5W7JpxzXlz74iqygmxNnv2ReML2BVuUsNEzpAHBhy83RPDf8ze2YQ95cTAjOlvVya1cfyZWZtW1Igbk6_tOEZKu8vQ5RqQp_Ndb4qN5Pa22z7SaXgzwck0eaZH_t5Cx7RludIRZTQtvm8zEp_g0vagqP3WVN-dfnqp6OsAhQA-729j2m4oagCiKkzMfGJyG9cDAL1xTznWPdMgGdTbXuGf4opboTSQ0FNVBFwboIh8iJTIp2xKW3zqpVKr5BmhdoOG9dXk5Rd0KD6BgWQ4C21Plmr2BdV2Cn4oiie9UBlY6U3KIF2QRCsv8g-N1VMaxDvV_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjbkYuqHCX8tvk8FH738oH6LbiW0LBtTtr51yVpVZLz_IUafjqyAmhutjet4C8pXhfMEKXQ3fzUZpI46h1Lr98uixjbp9vEAbYLBZMIzDnFPUTsQaRr36JlyTJ5JzG09hpJJvhwdDc0duJSFunKhvqLDArL3c9idpHajMBVIZ9heLshXp1hBxXpGnfn8eFzUA_jbM_KKJ2nIV2oe-E5ml3PL7uYj2p5QDVRAVb868m7gnyGMVDqEndNejC-fpQm-tnQ75DCKzizXsXmrjMywi_pIEJ8f4-vGDm2A_PRKP_kw9FuaqbjDC9FJXQqDsYYDNSselLkHNpUozWE01bf5Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=AG5EkUkCCI8xclPl9ny12A_28p9l0185u4ab_blvCGIZiDujcfhWmFqJwQw3ieiWgs4wBX7tTahaE4-KtNHXHP_x55tuofubLxQ7YSyzzCzvQsViKI06laFm49mH6iX_gX4UxxBaNpl_nEFm5En-SbhgNGuju2_PpxYYGMWnI0I9jDAKstEDn9ZlWg386jFN1O1QSK8AkT3gwV1v7NzGQCOZBKprX_yDrHRhTlraEmiqsfEkAM9MBgaYrzHZeZ5hIY2pjAgV_XmV0EjN-BUzHGlprJdQFSbhW-mYmHL3INgGceFYz8hRXVZ7tIuGZzgvO6hlFTWnE4AIQ5qv4jesJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=AG5EkUkCCI8xclPl9ny12A_28p9l0185u4ab_blvCGIZiDujcfhWmFqJwQw3ieiWgs4wBX7tTahaE4-KtNHXHP_x55tuofubLxQ7YSyzzCzvQsViKI06laFm49mH6iX_gX4UxxBaNpl_nEFm5En-SbhgNGuju2_PpxYYGMWnI0I9jDAKstEDn9ZlWg386jFN1O1QSK8AkT3gwV1v7NzGQCOZBKprX_yDrHRhTlraEmiqsfEkAM9MBgaYrzHZeZ5hIY2pjAgV_XmV0EjN-BUzHGlprJdQFSbhW-mYmHL3INgGceFYz8hRXVZ7tIuGZzgvO6hlFTWnE4AIQ5qv4jesJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=FEiJ4oOOYXXhsg_P00HMHjhLNGAaqocO9FvdpLN_Oi56lF9YQOyi0IVOhdEdcehStTRmIrWGjWzjeGvkWxUu66xti90FrsjGTwbfNJ3cI-j3kVzvkhTX2L8ahTknutlhpCTo0TmFls6HXf14oZ4DBeAXNtm9BYNXyKACpxy2bUPh5Fy5siQh2RlDfjts9YugY-d_Gw54KTmJZmoZcSKrVI9aBScWlw7KF9AHAhptC1hSaCfYmkclX4GTVS8wcYEN4aiQr2kQXHtXWX38ye9gM7r1EmklXJDW5M-kbvCbJs3Icf_vE217Yi0_C4D4pRkb8g35ighWyNXXjirBqji3Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=FEiJ4oOOYXXhsg_P00HMHjhLNGAaqocO9FvdpLN_Oi56lF9YQOyi0IVOhdEdcehStTRmIrWGjWzjeGvkWxUu66xti90FrsjGTwbfNJ3cI-j3kVzvkhTX2L8ahTknutlhpCTo0TmFls6HXf14oZ4DBeAXNtm9BYNXyKACpxy2bUPh5Fy5siQh2RlDfjts9YugY-d_Gw54KTmJZmoZcSKrVI9aBScWlw7KF9AHAhptC1hSaCfYmkclX4GTVS8wcYEN4aiQr2kQXHtXWX38ye9gM7r1EmklXJDW5M-kbvCbJs3Icf_vE217Yi0_C4D4pRkb8g35ighWyNXXjirBqji3Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=mouHWM6Wj3z20O6xO0lbYQJBFyE_BVkQxFpypH_anCN4b2n1UY5QsgFxnxpx_98e3_EPUbChsUL12ssNrntas4eBGDb-VVEP4xlpkKOs6pAOGfxmRUXXYZS6uQak_qblZgxrK0o-XRdKh-edgRP6e9Bi8pQtMAsiwl_9IhNRfqY29w0SBCPyCmMmG4RyaiXSdCzlvB1BBYcn6GQjYXABHVxHsskmHBXgcZpn-R-fHcmFQazYSdgLuDDVZAic2hOf7L0TDCiu9fSdeE34UnrS0C8z8kGmRbmchD63bkX5wrqBcdG4Y7u_qTYJTww-eWpo2ESqAqFPFvEQG4Ef9jS3iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=mouHWM6Wj3z20O6xO0lbYQJBFyE_BVkQxFpypH_anCN4b2n1UY5QsgFxnxpx_98e3_EPUbChsUL12ssNrntas4eBGDb-VVEP4xlpkKOs6pAOGfxmRUXXYZS6uQak_qblZgxrK0o-XRdKh-edgRP6e9Bi8pQtMAsiwl_9IhNRfqY29w0SBCPyCmMmG4RyaiXSdCzlvB1BBYcn6GQjYXABHVxHsskmHBXgcZpn-R-fHcmFQazYSdgLuDDVZAic2hOf7L0TDCiu9fSdeE34UnrS0C8z8kGmRbmchD63bkX5wrqBcdG4Y7u_qTYJTww-eWpo2ESqAqFPFvEQG4Ef9jS3iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dovRQ51uMJ_6XC0zS0KZqgP5RIEsU99ZpGLHCjOJMoutrx0Wno5_iphohgLzNi3GHxcC8z-U4c7kVDAFPxavUZDirgdW3NhIEp4UHc6QeilCnu7tr6qlnxydLO8YX9sCO5fGVYxNLtbWtYzrrcIRCmRtSyLSXb2N7Sq2WGzcMmzaZ41sdHx-vYpZW9e7Ffd7YO6ItdLmhEVti8Gotz1TUlEm8NcQIZm4er9Fss9tlfqG_uojnwTKaZyet4Zns129IFHu6Wdo7FkTRxjsHzMT2VOWkKfVFCHT7So7tB24fJsWEZlAJ-u2EYAIAuAM3nlZirrFDJ1BTgcVr1TYylZy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8HmfUN35jy9_tRnQkNZobdUuB4mSQJEHwCdMebOl_Qmm6E2OkZvyOfPc4AbsPeo-FQjYsBHvoywsy596k8HfFm66bUL--yuag2ekSfUfLO-ZyvFXZWvB6MkqdC9ApXCDvqVG8aq5jUNltvXJhyp1b8F4eVI2RzrJ_8ZDVjGn1Lrc12K9pXJ2W9FzKQUujsB11HWvMAwJ02-lqjT14JYX6-lc5pDjtrmlkMdo_smdtHNAaiQ6NON2Uumvswu5PYj8XOZ0HZ5FpX-JSBw1OJDJScsfFtxLSXgzQkOjafNPQvG03_18wqfnx-UF3v5X77k3r5Nh0_AckgEn4uXg4N3sxgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8HmfUN35jy9_tRnQkNZobdUuB4mSQJEHwCdMebOl_Qmm6E2OkZvyOfPc4AbsPeo-FQjYsBHvoywsy596k8HfFm66bUL--yuag2ekSfUfLO-ZyvFXZWvB6MkqdC9ApXCDvqVG8aq5jUNltvXJhyp1b8F4eVI2RzrJ_8ZDVjGn1Lrc12K9pXJ2W9FzKQUujsB11HWvMAwJ02-lqjT14JYX6-lc5pDjtrmlkMdo_smdtHNAaiQ6NON2Uumvswu5PYj8XOZ0HZ5FpX-JSBw1OJDJScsfFtxLSXgzQkOjafNPQvG03_18wqfnx-UF3v5X77k3r5Nh0_AckgEn4uXg4N3sxgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=DTJgz-SMwS3FcjZ7nmCFZ-2hMJgtlxZzVuT6agwsGUVpEMkiFLg4n42-llkgfJQ88hhWxkAB4HnIRh38GToQxIajoApXqZTrSRZtkhAgIDxPjKv1jM4nltaxCATfnhAUodC7py_tzNebXCChk4krwciKMuFGoYIq3CyYmUIRRXKvK5Dezbf0q462uvEGkHc8fpsuvWoBV8n-qBSdvhceRKyd70Ym-ecUNNs6ZakhUxp7BLRUX0SA5Q8_rAMmNckvEz9s1ppbsUZ-ykKYYyCi1ED27pIe_hXhwpWKUUaXZhC4sZRiwljNZNSYJTy_EnZFhR5_HlvZRLmjX2_-MFyRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=DTJgz-SMwS3FcjZ7nmCFZ-2hMJgtlxZzVuT6agwsGUVpEMkiFLg4n42-llkgfJQ88hhWxkAB4HnIRh38GToQxIajoApXqZTrSRZtkhAgIDxPjKv1jM4nltaxCATfnhAUodC7py_tzNebXCChk4krwciKMuFGoYIq3CyYmUIRRXKvK5Dezbf0q462uvEGkHc8fpsuvWoBV8n-qBSdvhceRKyd70Ym-ecUNNs6ZakhUxp7BLRUX0SA5Q8_rAMmNckvEz9s1ppbsUZ-ykKYYyCi1ED27pIe_hXhwpWKUUaXZhC4sZRiwljNZNSYJTy_EnZFhR5_HlvZRLmjX2_-MFyRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpWU3az-puMY29kjql033-BtFnhFoFaiI189f2dOd_fpoalCCtL1pPe8VutJuH0Pp4-DYRqt-Jpa_zUqIQnVi-aJmTVPEnFOfVa9_KSDH1ggjY4XHqkGnsg4ADK2BKcm0Rtx68aFlp8uArTzY7S0vLx4fnyMHjXg7RO2LACYhPmIXj6oOsew63uAkzGLjw0Fk8qqhNyqSbymPzoNM2RSrM-CqkbSmSMGf3WX0u5pzw0m98Tkdo1qOBWK3os0HguLUhIF6v_fsey4UdhaM3k9dw1mmvNC-O5g8RwZXDNp6c3oIDxexQ-FiDm6zvmvX0OhYzUYfftMHf3ft6F0nUGxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=K18HAFin8sXOxOWTS-ClI4-P5Yl_HaWaOUDEqUDU26cUZFEUQGplF92e5oKtHWAVC6Iq3kncxU758TU5AEdn4LRlZRZdIJPxKPRxU4GTl3EZfv3H6t2jMxaxAAOawFwEHP0cW0YXE7cwPyOvjhZXueSBNUjaaxZfV4D1vkdhn_QUYGjjbsPAhqowC3g55QUrijNo8-3H0ZZDNufaRfnFy5ubmXhqF0mWyqEuz2wQwAqEw_loJzSRp1gheQ1yz_yS1JyiTlmDFGtva-yKxIpOSaOztPy8Sm_Bf460y6rDPdviPH69OPvhvXEahzvnBNQQQtmO0ItzOwUbdQHEc7YpmVFVhlNQYF6Zp5R82bbWaLiOylrq8qotU997TPWP4OYh_jeOs3cU1id5nJLC0KzyI9q60ipDsPoTZ02e24t_8z3tUifnpmenw7oW2x3A_D_gkSQgt4KnVmWNtaHtF14XM4CwE7rNL1qWaIZspOG0A6c4gEijFmqE4EvwDQU6n5MMKMOhpeMTRN__Ja0HG1Bh7fTKP_0CY86Ayg59GdOTaAfoRte7D--kXCFmOOrO1EE0g1-SGEudhuEuriONRI8QikURfF7AKZ6C0Xdgv6fJgJ8eo4Tnmaqoz1f9yIpw9kbw38GJeAEqvyiT8N_owYyDH4IDDHGqYpoXhMB6WtazQGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=K18HAFin8sXOxOWTS-ClI4-P5Yl_HaWaOUDEqUDU26cUZFEUQGplF92e5oKtHWAVC6Iq3kncxU758TU5AEdn4LRlZRZdIJPxKPRxU4GTl3EZfv3H6t2jMxaxAAOawFwEHP0cW0YXE7cwPyOvjhZXueSBNUjaaxZfV4D1vkdhn_QUYGjjbsPAhqowC3g55QUrijNo8-3H0ZZDNufaRfnFy5ubmXhqF0mWyqEuz2wQwAqEw_loJzSRp1gheQ1yz_yS1JyiTlmDFGtva-yKxIpOSaOztPy8Sm_Bf460y6rDPdviPH69OPvhvXEahzvnBNQQQtmO0ItzOwUbdQHEc7YpmVFVhlNQYF6Zp5R82bbWaLiOylrq8qotU997TPWP4OYh_jeOs3cU1id5nJLC0KzyI9q60ipDsPoTZ02e24t_8z3tUifnpmenw7oW2x3A_D_gkSQgt4KnVmWNtaHtF14XM4CwE7rNL1qWaIZspOG0A6c4gEijFmqE4EvwDQU6n5MMKMOhpeMTRN__Ja0HG1Bh7fTKP_0CY86Ayg59GdOTaAfoRte7D--kXCFmOOrO1EE0g1-SGEudhuEuriONRI8QikURfF7AKZ6C0Xdgv6fJgJ8eo4Tnmaqoz1f9yIpw9kbw38GJeAEqvyiT8N_owYyDH4IDDHGqYpoXhMB6WtazQGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya1YcSo2n4zO_rRhTxMTDW_I8TQxwjc9lEayh2k5pF_E3mye-khophrmEzz_hGmLazbTQq1ym85PWpeeiLcVDhAKeJZnW3G86P0P04YizxBn_eOoedxuDLKS3mE3y4apzt2lZcB71Igs51z0kye461FHCOCluIoFHP2YCSUeTKIQoDcHJ7ajTDsfWXtwN5_L7BOwuWTaDOzDDSFOecJeSb5mtWiAp2NJWdz-xAgk5R_fkst6cpFGmoIQetkmu0bHID86rIB9b2NAtj8exC9u-nTUteJNSDdd_2qhKEGO0i-nph4L603Kh8YURt5UhyZ1-3rYbeNzncqmo0xJiJpkaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=UHtO5enQMjJxIh6pGd0oqlmEe-OlrYb5yKJPkM6QeSmZ14rhK4ds2lAIPB0bdqDXNUQf-2LDw7ABPf9W3DU4AbfuajJrryqEdepGnEhDf3IS4Z2m-AuDwSSefuH-_Q66i03h991hKFEf0z_XrtEb2r7NlnP2NSi6xReELdB1XjqHSzl34-v3AL8Mw3MAbMGiwhZpfOTelmWwwNTlB13W6zfwqn87GVSyArwPs12C86_eJj6pmKWMkXGVZtuuI8k3Sm4ZAP2GgGFj11PTjDXKAiLj0xHlk2QqcXiFLMYwNYhS9-prxZpW6s9awOuTQoHAUGQlpTWI-T5-IE3hhtdq4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=UHtO5enQMjJxIh6pGd0oqlmEe-OlrYb5yKJPkM6QeSmZ14rhK4ds2lAIPB0bdqDXNUQf-2LDw7ABPf9W3DU4AbfuajJrryqEdepGnEhDf3IS4Z2m-AuDwSSefuH-_Q66i03h991hKFEf0z_XrtEb2r7NlnP2NSi6xReELdB1XjqHSzl34-v3AL8Mw3MAbMGiwhZpfOTelmWwwNTlB13W6zfwqn87GVSyArwPs12C86_eJj6pmKWMkXGVZtuuI8k3Sm4ZAP2GgGFj11PTjDXKAiLj0xHlk2QqcXiFLMYwNYhS9-prxZpW6s9awOuTQoHAUGQlpTWI-T5-IE3hhtdq4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4s67907OU6dqkX_qC8O5LA-O7Kmsmn_47w6vOrvVzKNh6RFHBhyWzs73DyRO7AXStaUkbnzFQEkkJeaiZAwc_y0CmOzZCSySeHSfzkq-yLsyCr1eHysJ9OslFek9An_JSGYOJ8NOAUcjARvM4sXJPHdLmN2KuomNKpr01vshJ-JWqxuRDamP9L3s4UdBeOf1M-cmX8u5Te4LAXTuGVVqc3Q9e76CbPTk7SzFrklMBh-kPid8fsqHYzVuQjmmEg1Rr8_zornk7ewCAR5TWqymmaYEMe7jrZ2PtxDLAsOB7dwFX76OU6foUf54EtBvkW8tJJ_OlgA35OsRZUPg_Xt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMOPjNML_PdWQ9LSWLJX1oXfrMFTwZPMvutNiEUjWCAyLonwAH6mmawxlXfVePX6yLVAlWSvCFXaGkjPToWdrQH-n194qrUAY4oexs09VbSYyl-DAZMNR2sW_avvnoyRdHWc7ylv526ObCOwR4eiYRQF_EAudy8JbllNqX-Ia6awYMaEEDcugFOPCUHjuL57DSTctrjTI3LW0fUUqUFX5nYClu7Mv9Upt2L0_SYF72KVpDXEuQ1Yn8k-VzffUFZvE9-2dK_1ZALzp0DJWWR-F7F8XoWFJQTY18oN-64_Cf5n74-oseH1qCsLxQ259UnfMYju9_wJcGhoD0mL3xLm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2nAxTLcZv67qXhwveLJBP1iFMSQmEdofoGS8v8bHSw6kheFuTK57EQl477ipKpcX7gGsbQAA9PHgdLkqhDgDFWb66iYIM74ZWUFdLz9qcCTQI1y9ZbG5G_g1oYwdqWgAUN6xAxXNrDhgY_lMXdf0FSMifdUvU4AwB64cOVOcPwM4d6mxUg-cVk1jAgR8wqfwlfVlH3vJGWIh22qwh1cy3A94ox4Fjhvh-85MFpjw1Ol5yuM_Uzfn_O4cAtq9tPLpHnXM1OGthkEOEJm96ha6xgBXkGCE8CFkrtrHMdc4FGwdQo5zYenFQsCZT--3TI_r4XPoLJwY_6gibY_RINJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=cxb05QR4kvEPenkXBVCcVxfk-3_EJzGOXzfRc4Ytm6SUOK5XwBMgqaLfajKFp2lBD3GJtT0AN3SscmtIwKYYO4O1MzTPhCvCsL2uDcUa3vUJltO9Y2ssCQkdSTUvZvaBwnZOfPADHWfogt-ddUEkaIDvHzyOhYjIaLjQ57DHYSwtHLF2r0gQuZaiAWjjKeULO_Ri1mA0W3pZoFi7M_Rnjv4oc6Ixg3KLhC92dGeNUbiEE5tKuNfdcYYjNlU2xFerUDFIdnPWP7hvCs4_RWmQqXAg9k4ntwwKjFxSw4MzHBhmUCOKGmijw5dEEnaAEBnwxGgDzVb1H9-BWT0IUYQ2YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=cxb05QR4kvEPenkXBVCcVxfk-3_EJzGOXzfRc4Ytm6SUOK5XwBMgqaLfajKFp2lBD3GJtT0AN3SscmtIwKYYO4O1MzTPhCvCsL2uDcUa3vUJltO9Y2ssCQkdSTUvZvaBwnZOfPADHWfogt-ddUEkaIDvHzyOhYjIaLjQ57DHYSwtHLF2r0gQuZaiAWjjKeULO_Ri1mA0W3pZoFi7M_Rnjv4oc6Ixg3KLhC92dGeNUbiEE5tKuNfdcYYjNlU2xFerUDFIdnPWP7hvCs4_RWmQqXAg9k4ntwwKjFxSw4MzHBhmUCOKGmijw5dEEnaAEBnwxGgDzVb1H9-BWT0IUYQ2YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZS_L8wWPNpVIB_POwtLDwyqWfDFrBZv_UMBtkyTkXXi0kUWUgo8JE8nxVlILWrZ3kRp0VeUSUZkVisNx2I2T8Yjy_wjysI3sbQJMGBmEoFAbFqBuFKgo3mjVMfoukVV55szjD1gL4ZFxBJZt70XQpEYC0bby9Lml6lkkm7yinKS5Ts-GAPafawaiypZgD-v2FYhqBAvoXQh1lCUdODmj3fnivk7tCo2B_tLEdThguFjKBSnEl4a2wqGe-1rmvXJJXDze5kHJPlTqF_MW3jg87U22-P0GycHu1RNXmdLN718zkAnNiTQRtnUOmzNH1cnwp3QZyUmUxW2WMTLCJpbfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFEnFqneYFybj3AZggcqqo1SVUW2_yX13hZcL9oZ-GVuORpbhn968K2WRuAgFvfvchvKO-7almgtkMopNf9XDNoowYf7rFtkOLjJAnM3NN1N5Ju9Rk1u7f118g2XJCIf5F1rJTlP7kX6zZu6n__UoUQiUP_gzlLuvmTe9DE5fWMR4QLFOM3X6z6FA961tJePqU1WHjFtdemWJrQUThWTpvFH7rX_WedeZmximkbaHMqIC_xGQdsv-B3qO8oytsnruKbgryGcyP0ASj29sOScVFIbGuki8K_D2KW16QNDZuOuKUZuDO4EKfyTAztjInQlpwLHx4yNnAJB5EGpi93RQz4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFEnFqneYFybj3AZggcqqo1SVUW2_yX13hZcL9oZ-GVuORpbhn968K2WRuAgFvfvchvKO-7almgtkMopNf9XDNoowYf7rFtkOLjJAnM3NN1N5Ju9Rk1u7f118g2XJCIf5F1rJTlP7kX6zZu6n__UoUQiUP_gzlLuvmTe9DE5fWMR4QLFOM3X6z6FA961tJePqU1WHjFtdemWJrQUThWTpvFH7rX_WedeZmximkbaHMqIC_xGQdsv-B3qO8oytsnruKbgryGcyP0ASj29sOScVFIbGuki8K_D2KW16QNDZuOuKUZuDO4EKfyTAztjInQlpwLHx4yNnAJB5EGpi93RQz4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=m6h0_g89mIZa7qQjCisi7CiImkV257oE38g7xJVjqZsq1AMMa33ClDe_xMkUOB7G8emEnYTSz8aVqG4umQHB-f0Xgry8gjecRkgZ-NnEPhVwtVaDVQeYEuu23u0JTMRJeNYC6hJ2CsvP_lI-Lxz9lPbYC7ELjepgnZY1Z1_JcyTztHvgesjLcp_JxjbKjiOVZOVcXXe7wR6Dhm2spLAmdyLfi35vKi6kVob2_NqIcfQ0uE7KNCgpqHLwaKiMre2vf9ovFyRIFWnzzOgmX0rqureHIjHxsJbduM_vxg_gohyI2Z6wBXaqenyLLxvuMDCjys7ovMSnX5OTV8dMafegHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=m6h0_g89mIZa7qQjCisi7CiImkV257oE38g7xJVjqZsq1AMMa33ClDe_xMkUOB7G8emEnYTSz8aVqG4umQHB-f0Xgry8gjecRkgZ-NnEPhVwtVaDVQeYEuu23u0JTMRJeNYC6hJ2CsvP_lI-Lxz9lPbYC7ELjepgnZY1Z1_JcyTztHvgesjLcp_JxjbKjiOVZOVcXXe7wR6Dhm2spLAmdyLfi35vKi6kVob2_NqIcfQ0uE7KNCgpqHLwaKiMre2vf9ovFyRIFWnzzOgmX0rqureHIjHxsJbduM_vxg_gohyI2Z6wBXaqenyLLxvuMDCjys7ovMSnX5OTV8dMafegHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=CJy8m1OhGORgcL-0CrkTMc6s0s8AQyYVEyz9nv4OVO45sxcQgQ6dlBeorLkS1XsJbhQ74wTKVB0AkSelLACoNfviISfFYE26IuGVlqvPyq64oTN6yOINVP-khvfsZvC9-otxOzaST6HDZ1UMqyGBTCeZIE7hzhCXmiegukQWiXjAARpIjG0EGdOes7A0_MF6J64BcBBCjygTi36DKyckvJ7_TkYVZPjrmcu78IFqnY8djNQ8addhgM09J9oCcI9ptDBAi04BYzFuXNtv0m6G4X0kkvFZp-DPl1-AEb5SSZmIIcH77UasNYYWg92GimNhVaMnqqJWR0rVyKTFrbXR8y-RiboG3kNSpnTnTOW7oyj5z-X13NwPlWBWUF44AX6bMw8VEaoWspy_me_FabpF7yVEZmgg61zTNx0jhzy6iFf9AQTyCEkKNRKxlGLXeVIJhjZ6locuW5G-1kHJy7ZGS4qt5SbqieDzJ00FaXdR-MFSknOdIqHDzAf_d7LgS9rxFQCfzl5QIrjw6j3Czbq1jjPBR70Lsg0Tz3Qjr6a4ukmIdjquruMh0VxMqQwaWvgE3hjShzGaUpqAKctCYEtPsaFuPRqsPMGKScebP4MJOvUi-FMj1Uv-ohV-G8NPrUZzFtXnz_81cnJ8FOASDxrJAd1WDL-Vh_IymKxiMxrbnlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=CJy8m1OhGORgcL-0CrkTMc6s0s8AQyYVEyz9nv4OVO45sxcQgQ6dlBeorLkS1XsJbhQ74wTKVB0AkSelLACoNfviISfFYE26IuGVlqvPyq64oTN6yOINVP-khvfsZvC9-otxOzaST6HDZ1UMqyGBTCeZIE7hzhCXmiegukQWiXjAARpIjG0EGdOes7A0_MF6J64BcBBCjygTi36DKyckvJ7_TkYVZPjrmcu78IFqnY8djNQ8addhgM09J9oCcI9ptDBAi04BYzFuXNtv0m6G4X0kkvFZp-DPl1-AEb5SSZmIIcH77UasNYYWg92GimNhVaMnqqJWR0rVyKTFrbXR8y-RiboG3kNSpnTnTOW7oyj5z-X13NwPlWBWUF44AX6bMw8VEaoWspy_me_FabpF7yVEZmgg61zTNx0jhzy6iFf9AQTyCEkKNRKxlGLXeVIJhjZ6locuW5G-1kHJy7ZGS4qt5SbqieDzJ00FaXdR-MFSknOdIqHDzAf_d7LgS9rxFQCfzl5QIrjw6j3Czbq1jjPBR70Lsg0Tz3Qjr6a4ukmIdjquruMh0VxMqQwaWvgE3hjShzGaUpqAKctCYEtPsaFuPRqsPMGKScebP4MJOvUi-FMj1Uv-ohV-G8NPrUZzFtXnz_81cnJ8FOASDxrJAd1WDL-Vh_IymKxiMxrbnlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=lTOYurNMVCM-fu3HfU5iFK-hQPp_WEwYxBQheaVIQB5ZzapOOKbe4RNM1GBWuApJYLmRRxPX8zcz57E1AiuCLYO8lb4IIJEZQhLKf6SLaiKpyETsbv1u4zFR20x1_HQ_3wYALRLUmyZbqVMXNWLVtC5jAx59QeHtURC-NUImUtnd1ynQYlOy5Yg-Z36wmGnOjH7pG5YG-FbZ4cRh5VFKrqIsQo2NVNmfF8eFJ2W-pJdoOgooHR68n3TD-bkXMQ89IOUBLbbf7ilStsqwrf7-mB302U4-qs5DedqnGpePG1QSdvDXTrC0uOXeyiNdZp3XQ7yObae3IB6z-YKF8WXHZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=lTOYurNMVCM-fu3HfU5iFK-hQPp_WEwYxBQheaVIQB5ZzapOOKbe4RNM1GBWuApJYLmRRxPX8zcz57E1AiuCLYO8lb4IIJEZQhLKf6SLaiKpyETsbv1u4zFR20x1_HQ_3wYALRLUmyZbqVMXNWLVtC5jAx59QeHtURC-NUImUtnd1ynQYlOy5Yg-Z36wmGnOjH7pG5YG-FbZ4cRh5VFKrqIsQo2NVNmfF8eFJ2W-pJdoOgooHR68n3TD-bkXMQ89IOUBLbbf7ilStsqwrf7-mB302U4-qs5DedqnGpePG1QSdvDXTrC0uOXeyiNdZp3XQ7yObae3IB6z-YKF8WXHZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-6Qcv6DmW2WWCaL0fakxraAg4x1NONh4MW1rkAs957xVm40UCyjiBDn_em1UFWLaMCFffEQQs2Hyojm77a5WakA5MO_yQR-rbXo10NAOuaid9hDOvLTCfd_paosO366AOjkagug9jgpOrdQ8dkQ58sRAj1RamLXVE9n2bctDlGDgw-Lah1b71fQ_9pkZ3UYCpG3UGUzqOhckJ1c8G_x1rCA-wEjFRMpw3tDvVJhXWOPalm5GgeE4xAea6BgP5PW5i-IUaGFRdbmufz8zqllIEE2pFx2idA9J4DRih_8fMxbeWyKu9-kv3hgNaux6KkEh3ckzgGNNMudUtSEew3sNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=ZShY_lXYRyI0JG6MCSE-xCTrLlAsvjFBHM9zEzGjNFmsUg23I8GLw4J3BdNe9yOqpm8htamdD7FKlVyakmGJO3t2j0xxZHTKJBRvL-pt8t6NpzWLkBjKNz5mjN-BH0ZftyRmyt7Arc_UPrZZLxlpqmBF3rQKHS5dgjZshh00q0xQRj1CKi0ceFC1e7ciN_w51RKVYF8K-jVbyXdGGWPv2rtWSI4O56_-ahWZDarb3BzQkfOY_PYxAmp5AjEzolJ9DObqK2SSjj-qeUwuQ-MosEm90broB9d-nI27tnHIU6RPdCuHdzzD9Um0ZRv3Tc4iEXxIxDN4AgDAwk-r710hVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=ZShY_lXYRyI0JG6MCSE-xCTrLlAsvjFBHM9zEzGjNFmsUg23I8GLw4J3BdNe9yOqpm8htamdD7FKlVyakmGJO3t2j0xxZHTKJBRvL-pt8t6NpzWLkBjKNz5mjN-BH0ZftyRmyt7Arc_UPrZZLxlpqmBF3rQKHS5dgjZshh00q0xQRj1CKi0ceFC1e7ciN_w51RKVYF8K-jVbyXdGGWPv2rtWSI4O56_-ahWZDarb3BzQkfOY_PYxAmp5AjEzolJ9DObqK2SSjj-qeUwuQ-MosEm90broB9d-nI27tnHIU6RPdCuHdzzD9Um0ZRv3Tc4iEXxIxDN4AgDAwk-r710hVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=muhIa2L-ietM5gOErc6rDqUecILxft-KfKYi5eZm48wmGyJD6bTt9F19s-e6VL0sxBEUua0VZoRqv4-fNi-MFtkd_AskQlYTMGAoDYXO5zGFS3vojmKRy0edD-C3CnIQDhrD-p17pOhZ6ukL7hZH2SFr1-kfyF_phKyfmXh54W9g6iL6KyOKwGzpbzyxJOn5nz0ztYAc6jjpHe65oQMpYoocewR0hIWEpad-MsmMDvuP7vDcfeC76HLqqPo-ejiCk8RilOYVc0IZoz2NGxtrJauI1lbhSXXIkeoGps6-rhdAdMhPsGdYFbcY_We4rbQketJii4wz2TAdyQ6WuusWeyDdymrDNTjjcLiFwYtEMH5K2EcaVjSar-6_kx6Jr2F28ufWuqSpjg9wVwnv3nvy-kNktfnBAcF1l4ur9QDUDL1GuAJN3ln1ibvHa2f4gPCcu5D8rfygDWbAF1uOgeDCPMHPQ2U3YdMsQcXV__xBCvlQ-6DOkRmmxRQ-faMG8625J5R06LOFqEe7s1x6h73S2XYaAd2U13qTPe9wOol5ZSmb8__MHL_CXq-PN0yYSrgD_c_jUHwidjkmL9j3g_1JBRo4ldsq73qXOF0MNlFAMMrXfNvuknXbNHXD_GMZKxjl5o94pvMkicuZB5cUgLZ-uRPeuul8s7zoqYx-iPersiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=muhIa2L-ietM5gOErc6rDqUecILxft-KfKYi5eZm48wmGyJD6bTt9F19s-e6VL0sxBEUua0VZoRqv4-fNi-MFtkd_AskQlYTMGAoDYXO5zGFS3vojmKRy0edD-C3CnIQDhrD-p17pOhZ6ukL7hZH2SFr1-kfyF_phKyfmXh54W9g6iL6KyOKwGzpbzyxJOn5nz0ztYAc6jjpHe65oQMpYoocewR0hIWEpad-MsmMDvuP7vDcfeC76HLqqPo-ejiCk8RilOYVc0IZoz2NGxtrJauI1lbhSXXIkeoGps6-rhdAdMhPsGdYFbcY_We4rbQketJii4wz2TAdyQ6WuusWeyDdymrDNTjjcLiFwYtEMH5K2EcaVjSar-6_kx6Jr2F28ufWuqSpjg9wVwnv3nvy-kNktfnBAcF1l4ur9QDUDL1GuAJN3ln1ibvHa2f4gPCcu5D8rfygDWbAF1uOgeDCPMHPQ2U3YdMsQcXV__xBCvlQ-6DOkRmmxRQ-faMG8625J5R06LOFqEe7s1x6h73S2XYaAd2U13qTPe9wOol5ZSmb8__MHL_CXq-PN0yYSrgD_c_jUHwidjkmL9j3g_1JBRo4ldsq73qXOF0MNlFAMMrXfNvuknXbNHXD_GMZKxjl5o94pvMkicuZB5cUgLZ-uRPeuul8s7zoqYx-iPersiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDek3NfiF6sY_SDaxNUQxnH3B_V4SiBUEhmPqHpxMRnjnQ55DG3syU6Js6M6SWkGhBeX6PEx11IsP2J8IEX6r86vQVsUq8hGE640ucXGwrOnE8RcSChHj7CFv13rY_uZNqDzoY098Hpro9yUjyJ4Pf8BrpdrXnevXipMx8o7_kVkIOCjNA91dAkA2zlS7HqiMpnV6lRmpRtVkVJ32RWZVKIjfrPRJqM8O9obyWJW1L-f3EdEOZ7gnvBHyWGNmboFCgEAMMe95Xe9jkibr0xminmQpeyPcxmL6SK-4B8NQQ26txckmatqKb1JAWoW5w-U4g8y-V8M7QCt6KIIUnXA1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=PUF4a95p3TQ1CwRb4rC6DDcobrDpRDHCufoclasuCGtN4Nc2YQ-6IvrMkSPKMSKorbQk65KeH5xY6Pq0ZIsAIOH0lljEwYZpd1gADruJFq9EE1djthYoRVIA0KLetFzRcKvnt5ycGuzH1lMkDu0osiypBtcJsrKBc89tQ-H2yx43RCehC86AiYJfMEMqxUeHg3McvJmI8DGdNU-dbfaLDWf9rNuROKKI0fBtBBcufmPuOUsjOyv1EHE_WQbMgq26G5a1EgI4YrZUS0DKWFKpmTA26q-YiLnLh8zazSI5NrOpBcEIKQ-0iI34nyOtZbgqu24sfQ62mg9Rzcl89YVmal23ZSbbXEJ9SjU8yzwMoNHLo9mjcegmfiB4RWwXRqXEQoRXx-PUdad13wnfZPFDioloOmc1JbXtF9Srth9s7BMy036N2FzVP58UMj52t2dStk7sEJon0WWF-ytVz6s3R5ubPG4Lqy-KkbywWNhAUSOaNIoJEPY_A4lvuInHiG4GXXo7MbYTGPdSOHTtP0VpbVuo8Ds782LxohhAC_DOG0aeGko9dtGE8L5dw8Uxh-3oNJJYtC9Hm9y0k_M5Ky1GjVXYhAtiDDNq4fqErjXTOzhU9W3U5SpqKwjdiMurjWDE2AwA89D5XDOAfNP-PfcJafzy6Im8L9huTw50R2Vo-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=PUF4a95p3TQ1CwRb4rC6DDcobrDpRDHCufoclasuCGtN4Nc2YQ-6IvrMkSPKMSKorbQk65KeH5xY6Pq0ZIsAIOH0lljEwYZpd1gADruJFq9EE1djthYoRVIA0KLetFzRcKvnt5ycGuzH1lMkDu0osiypBtcJsrKBc89tQ-H2yx43RCehC86AiYJfMEMqxUeHg3McvJmI8DGdNU-dbfaLDWf9rNuROKKI0fBtBBcufmPuOUsjOyv1EHE_WQbMgq26G5a1EgI4YrZUS0DKWFKpmTA26q-YiLnLh8zazSI5NrOpBcEIKQ-0iI34nyOtZbgqu24sfQ62mg9Rzcl89YVmal23ZSbbXEJ9SjU8yzwMoNHLo9mjcegmfiB4RWwXRqXEQoRXx-PUdad13wnfZPFDioloOmc1JbXtF9Srth9s7BMy036N2FzVP58UMj52t2dStk7sEJon0WWF-ytVz6s3R5ubPG4Lqy-KkbywWNhAUSOaNIoJEPY_A4lvuInHiG4GXXo7MbYTGPdSOHTtP0VpbVuo8Ds782LxohhAC_DOG0aeGko9dtGE8L5dw8Uxh-3oNJJYtC9Hm9y0k_M5Ky1GjVXYhAtiDDNq4fqErjXTOzhU9W3U5SpqKwjdiMurjWDE2AwA89D5XDOAfNP-PfcJafzy6Im8L9huTw50R2Vo-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=jcf7wPfTwvQVkiSGIuf8q-wdirIzl8_TYVuE5PgpvxOP1bYjCm1GBbwgeYnwTBDn4QnmsDJbAHySioYvc_UV3-57zgpva-Gf4H5F9oi680RJ0V_vPCtLnVb0FXgV6_MqkSJ0xIRpIiz5mVmcQJAxxyq8b9O54NdFK8rb7a9t8xPEe3n479AC25IFU__9wOj5lziq46XsxvrClAOD5dssGaSTFW-uDnGL6-j4YrCFMndmyhenGTV0U03El-KMYecFb_mAKhUioE3L92F4znuc3z-_YhTlf681k_35z7PEvtzRqVF9T7RnoY6HhSqckWdHr6SFvZ0Zlh3LFkYsWWAwO1NJTDPrdUxiykep4yC1tOgrzZvhbnIe1N_p-XcPZmc3etRD5dXu5Sl33-z4WicA2RUbOpMF6jHXjoNuEfa7iQ_5iW1BWoOne6-blozv3ACx2IkzJkUPKWuGv8-fZ9jZW6rszq7SM2Sre5mGPfHCYNFQKnP_DDpXqeU5jFqhxcGkldj3lBWJ7svF6jfAkgkYJN4v9YjJIotzKfAnsHIqhK0m8cD8x5tzq1642vniDDtCnoDruduGwm8Z84mvqu1aS9euWKnQTekvOTnBSAvJjJ0YF7YmAUaxOqmLc1oe6ZcpAo-1FXeQPwYUo58K10d4Alw0hU-dSUWvXZP1bVfWIIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=jcf7wPfTwvQVkiSGIuf8q-wdirIzl8_TYVuE5PgpvxOP1bYjCm1GBbwgeYnwTBDn4QnmsDJbAHySioYvc_UV3-57zgpva-Gf4H5F9oi680RJ0V_vPCtLnVb0FXgV6_MqkSJ0xIRpIiz5mVmcQJAxxyq8b9O54NdFK8rb7a9t8xPEe3n479AC25IFU__9wOj5lziq46XsxvrClAOD5dssGaSTFW-uDnGL6-j4YrCFMndmyhenGTV0U03El-KMYecFb_mAKhUioE3L92F4znuc3z-_YhTlf681k_35z7PEvtzRqVF9T7RnoY6HhSqckWdHr6SFvZ0Zlh3LFkYsWWAwO1NJTDPrdUxiykep4yC1tOgrzZvhbnIe1N_p-XcPZmc3etRD5dXu5Sl33-z4WicA2RUbOpMF6jHXjoNuEfa7iQ_5iW1BWoOne6-blozv3ACx2IkzJkUPKWuGv8-fZ9jZW6rszq7SM2Sre5mGPfHCYNFQKnP_DDpXqeU5jFqhxcGkldj3lBWJ7svF6jfAkgkYJN4v9YjJIotzKfAnsHIqhK0m8cD8x5tzq1642vniDDtCnoDruduGwm8Z84mvqu1aS9euWKnQTekvOTnBSAvJjJ0YF7YmAUaxOqmLc1oe6ZcpAo-1FXeQPwYUo58K10d4Alw0hU-dSUWvXZP1bVfWIIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ppCgS8fNQsP7oPCZs9Q1oZaxSVQWVIhVeGB1qZ2TNd8SjGC2Wxa5onTOCvwS1zFmtbsk_A9IxhW4QDVJGgYPh7g6uoDhRVgHRJb_gjpfufYKwSEF0sUDzmYIuGVslyqwNsFJHgDIINrM4yr3g4vTAQqImTLEoKuaHV5JvNX2u3pEbzaDpEaSAxYf20NgnwJNj8m4L6AB_nn-iQXNnu0kwai5CaacJI8kfjJQ0kZWs3wow_LtpiZ_vdgbutJm28O25RD1Q0Iih_gwOEUC043pbXoka3KSHGp6C4rcmWd2aRfV6rLQDuZmmgpIYV0HCJzBUr15Rg9je8BQg4qihpMAXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ppCgS8fNQsP7oPCZs9Q1oZaxSVQWVIhVeGB1qZ2TNd8SjGC2Wxa5onTOCvwS1zFmtbsk_A9IxhW4QDVJGgYPh7g6uoDhRVgHRJb_gjpfufYKwSEF0sUDzmYIuGVslyqwNsFJHgDIINrM4yr3g4vTAQqImTLEoKuaHV5JvNX2u3pEbzaDpEaSAxYf20NgnwJNj8m4L6AB_nn-iQXNnu0kwai5CaacJI8kfjJQ0kZWs3wow_LtpiZ_vdgbutJm28O25RD1Q0Iih_gwOEUC043pbXoka3KSHGp6C4rcmWd2aRfV6rLQDuZmmgpIYV0HCJzBUr15Rg9je8BQg4qihpMAXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=NSkgw82wtvb0QOzAVQE79ZcGvpW4Ye3uzBKfev3f9j0mqDxxWOuz1FoJ58Kew1BTLCQ5GJrPEMavv_UW8L8DcJmK62PPSS9uSYqX3XKClS0ehReg3cwcUVR2bSkVRbzcmGyhgKxgf22FtVGhV93OiV6GOaG9aXoMVFAFX-U6IBk2Dp_M08NTvS5GPMMfWtfUg-Uo2l8TSEVauK34ml075KEB2wEuxCUnLn8ZEO50PP_Ozu4bVW5wcNlKSz_gGnzVIGdqxq17L3FTXTmNNqsfEocP9L5UEGUG6ACVbI7iqrIj8w7mT6sCZzrVNE7zfQ2J5AX-90uT-jXO0B62Azz7-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=NSkgw82wtvb0QOzAVQE79ZcGvpW4Ye3uzBKfev3f9j0mqDxxWOuz1FoJ58Kew1BTLCQ5GJrPEMavv_UW8L8DcJmK62PPSS9uSYqX3XKClS0ehReg3cwcUVR2bSkVRbzcmGyhgKxgf22FtVGhV93OiV6GOaG9aXoMVFAFX-U6IBk2Dp_M08NTvS5GPMMfWtfUg-Uo2l8TSEVauK34ml075KEB2wEuxCUnLn8ZEO50PP_Ozu4bVW5wcNlKSz_gGnzVIGdqxq17L3FTXTmNNqsfEocP9L5UEGUG6ACVbI7iqrIj8w7mT6sCZzrVNE7zfQ2J5AX-90uT-jXO0B62Azz7-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=EA70ZBK8ilw0MwhxETD-E0dzIoLlF6pu3x7zec2pBMIN1LLRBdXh0UOYHzsN6V1AO1tsgNOeM-t8v4k4q4kqkRgGufWKq8M39cQYOAWtLCRG8T8uvxoeXCFaqmZxcq3zRQ9zC0ODWssP2r5qrDVAQeFdo1QLdTw0HgB5YbwYBbLtnrodBMBySbo2UQFnlzjaDRDGLlxUC48NZsCBybdl-DA1K--QnVDBD-BTzmWitmb9zTnAXDrHdpxlEUi3UeBay2aQLVvwgz4aOOi_NQlb7wWFNFQJJ-yzuXnzQIsj3wXO8mwgc0j7HJNkyUfRD2cVyG5MQ9tiFI0d47lOf-7Djg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=EA70ZBK8ilw0MwhxETD-E0dzIoLlF6pu3x7zec2pBMIN1LLRBdXh0UOYHzsN6V1AO1tsgNOeM-t8v4k4q4kqkRgGufWKq8M39cQYOAWtLCRG8T8uvxoeXCFaqmZxcq3zRQ9zC0ODWssP2r5qrDVAQeFdo1QLdTw0HgB5YbwYBbLtnrodBMBySbo2UQFnlzjaDRDGLlxUC48NZsCBybdl-DA1K--QnVDBD-BTzmWitmb9zTnAXDrHdpxlEUi3UeBay2aQLVvwgz4aOOi_NQlb7wWFNFQJJ-yzuXnzQIsj3wXO8mwgc0j7HJNkyUfRD2cVyG5MQ9tiFI0d47lOf-7Djg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=atP9ztRngi4RaGJiT0aszLW7on1CQOS5uWzUZrB7LtphNYftIG5PS5SXJQqBDHniUCrPg2iH1lNYXiCl52fYfA4fae5630gDxseGJWG6PJbGqYWeiqEd8utPypGnxN46LXglT3vh0CI0WL_I3Tzlb26iT3GdtvMX4gfE6Qz1X85_swgj5I8BtRBQ4kivM7Qx6CEM1VojHMsT-Z1Rfz-EoB6aeOmAOrzsFwn3VPGH6x44aWG7ylB5MMIhIDIYLXnN09csH2uyaPiAEGIY-VddaadBOBUY_rbsnu83Cj_hawQ5d9a3jrB_ngrD5Uxh8z3JMiowAgB79Sg2btQ_QRz_Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=atP9ztRngi4RaGJiT0aszLW7on1CQOS5uWzUZrB7LtphNYftIG5PS5SXJQqBDHniUCrPg2iH1lNYXiCl52fYfA4fae5630gDxseGJWG6PJbGqYWeiqEd8utPypGnxN46LXglT3vh0CI0WL_I3Tzlb26iT3GdtvMX4gfE6Qz1X85_swgj5I8BtRBQ4kivM7Qx6CEM1VojHMsT-Z1Rfz-EoB6aeOmAOrzsFwn3VPGH6x44aWG7ylB5MMIhIDIYLXnN09csH2uyaPiAEGIY-VddaadBOBUY_rbsnu83Cj_hawQ5d9a3jrB_ngrD5Uxh8z3JMiowAgB79Sg2btQ_QRz_Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=g3W9uiPjl13KFHj6PpKmNctRE0pxC3Lnmsc5Q_fhs1yHuGrnCMa06ShlLbYnQP4MD8sknLGDLCWBV_yVTBjeaVIU6dGrND0m9p9zHBArNFrIi4dWqE7dzpHaYPzRzItuJz_kQCZVN9tdilvUbRpZRmRTaDIUcXQmnyDH1XFOYyeb4fFv3bvbWSUfpCkcktAByvdKcHHRldPdhgF3aHxSAP5Pth7mebZAxmvb9bDqIGJ3KlY2aqLrY8JpOY6bAzzMyaW93IPxTrzfH6AT0jP90ySX_rfsnjh2ooPepQpDVnwCvZTOME5K1Iwk8qsprjqOjgQuEbVmKFDVOZjZ1M-ypA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=g3W9uiPjl13KFHj6PpKmNctRE0pxC3Lnmsc5Q_fhs1yHuGrnCMa06ShlLbYnQP4MD8sknLGDLCWBV_yVTBjeaVIU6dGrND0m9p9zHBArNFrIi4dWqE7dzpHaYPzRzItuJz_kQCZVN9tdilvUbRpZRmRTaDIUcXQmnyDH1XFOYyeb4fFv3bvbWSUfpCkcktAByvdKcHHRldPdhgF3aHxSAP5Pth7mebZAxmvb9bDqIGJ3KlY2aqLrY8JpOY6bAzzMyaW93IPxTrzfH6AT0jP90ySX_rfsnjh2ooPepQpDVnwCvZTOME5K1Iwk8qsprjqOjgQuEbVmKFDVOZjZ1M-ypA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Qf4WN5M0wGGQ5neS4ujrs5zMmrziYtaGK7rtJF6bjgwTi_fB7qhhYFb5seSLkGpR1VzirsmeCs_puUoLUkxNrtBoO1GXFSSkoyesbjhuB735h6nzN1Zq_G-kMCYSrGv9fiZaZJETc28F1Vhd44vFLiklkWFWNPaW8IcOtymGo2FfBl61v0lKxZivsCtC3gvAm6lyZlI4NJKBwJjhwTda13mRCdi8xWYZcQ5N5odvnBv8HmsshVOQvW-8YoKVqGULCXo1dIp4uaUNf3difj5_6tvZshY6tNQKiXNn5xSxZRcjMWi1cEojA0HcNDwvlEUQLhQ4azyyqWZV2GRJDhwmdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Qf4WN5M0wGGQ5neS4ujrs5zMmrziYtaGK7rtJF6bjgwTi_fB7qhhYFb5seSLkGpR1VzirsmeCs_puUoLUkxNrtBoO1GXFSSkoyesbjhuB735h6nzN1Zq_G-kMCYSrGv9fiZaZJETc28F1Vhd44vFLiklkWFWNPaW8IcOtymGo2FfBl61v0lKxZivsCtC3gvAm6lyZlI4NJKBwJjhwTda13mRCdi8xWYZcQ5N5odvnBv8HmsshVOQvW-8YoKVqGULCXo1dIp4uaUNf3difj5_6tvZshY6tNQKiXNn5xSxZRcjMWi1cEojA0HcNDwvlEUQLhQ4azyyqWZV2GRJDhwmdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=EZ6mZG-Wm2HVRdiWvgPXaTqudDyEZ9xuXLCsKY9e2qL4WQpUyloahAT7Agn1EYeIeA8N_cz4TWka0F3QsQahuq21VLaBun96SINpCO5ZRDJ9lNKWatVpcd3w-H6jwCluWMbJScTGdEuFdKvkfQ8wpLCU7rQLK2FAIw-jVd1pHGowBm4_eZDDiXNCADGaqb__nPJWQJYbtNc50NUgOuhZVxa6_6qkmMwYSnZfcaa9E0vQpLEaVAhy4n414KdKoeQNeTCJaj4pYuRhpSUiGZhbVHpsisDNlI_Q7R1mC6H2IPoMuX8wVMzzq2OuLYipsgR8_Vmibw0uhBobnJLohaD-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=EZ6mZG-Wm2HVRdiWvgPXaTqudDyEZ9xuXLCsKY9e2qL4WQpUyloahAT7Agn1EYeIeA8N_cz4TWka0F3QsQahuq21VLaBun96SINpCO5ZRDJ9lNKWatVpcd3w-H6jwCluWMbJScTGdEuFdKvkfQ8wpLCU7rQLK2FAIw-jVd1pHGowBm4_eZDDiXNCADGaqb__nPJWQJYbtNc50NUgOuhZVxa6_6qkmMwYSnZfcaa9E0vQpLEaVAhy4n414KdKoeQNeTCJaj4pYuRhpSUiGZhbVHpsisDNlI_Q7R1mC6H2IPoMuX8wVMzzq2OuLYipsgR8_Vmibw0uhBobnJLohaD-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XetCf_neJ_Ym84_bS2BRp77JFEljSUS40ylxR_ilhIbtX4aenPqwJev2o2eF3KskgFBuOMEsvbqWX_nWDMjRAD7LissujMY6uEwhvTAXPjdRafzlKVwFDSQ0e7GB_Fy7p4x4Q1QGzb4IS9gte5e69XmY2jAhb4lEGCOZnnt4Ed6tiHx5XXDcZj10EjDIrXWnAidVtXHBkLnPENBiYVuJKsqdyh3fOMjbJykC3GhV20plvHsOms3fPOs11Mw55Mdx6wuQA8dab9jOOUXPiCAl3d_GAtY7p4a02u-NrWPatnXr1h7AZ8f5oPm-hqA950GpUy99SWfdrlSVeHVe5ToN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=crReRodG1gWf-fbIs2PWBkwliy1EOdL9iSkbVXmdHrD8RwpRmbIe-idypcsuLWJxxORpRaQSoXnWTUuyE38USEzfe2Ah89yjD1srYkpHAPFcxYCbOTS5d89mDnNEUuq_c6qGb5bw4l1HPw3zSdY4tIwT_UKPFYjhg_31off9OSa0xw_7gY79vMnnV0DBfZHNd55_cqi-Ar9JLBZDCWM2weMYNZCYG-HOvVh5ei4v8kzVWn-x-K2N2BheAp1FWehNmge22-T7FdnzNUnI54tmg4ejcnbE4-Zi09af8zWtVsJq5RWF60Mmyt2ufC4RwtY3zbL0oAOjRV-9dSChk_9MHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=crReRodG1gWf-fbIs2PWBkwliy1EOdL9iSkbVXmdHrD8RwpRmbIe-idypcsuLWJxxORpRaQSoXnWTUuyE38USEzfe2Ah89yjD1srYkpHAPFcxYCbOTS5d89mDnNEUuq_c6qGb5bw4l1HPw3zSdY4tIwT_UKPFYjhg_31off9OSa0xw_7gY79vMnnV0DBfZHNd55_cqi-Ar9JLBZDCWM2weMYNZCYG-HOvVh5ei4v8kzVWn-x-K2N2BheAp1FWehNmge22-T7FdnzNUnI54tmg4ejcnbE4-Zi09af8zWtVsJq5RWF60Mmyt2ufC4RwtY3zbL0oAOjRV-9dSChk_9MHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=WdHFhBZBJwUYF-Az6nudnJ8cDWGaFzS0deesD-lvxydwr0lGQ72ej-ggUEJBN7ITsQ92iVwBLqmyP7IxX6AERetA3EN09KQ3hwReB-WSSeEpvwqHvfcfuAjig0H-ZWVZu02_69IKMLBx81fVJ5bvCS8myE40NmQH17H0yRYRpxs4vyC4jD58MmC7Xx2eyxbAIoCKkg-fYmIj6SrC3GSUfvQ3V7yfze3T_f4NY-tv2v6z1C8t3exRsxdWXTUzW5_AUOxU3TtOSsfqoObyIWql3DDRqqGA-AyxfmvSJYDFEwv59OVnTLgSg5C-BwyWV1qA3DHODLwq_a8Ie-9bS3AxUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=WdHFhBZBJwUYF-Az6nudnJ8cDWGaFzS0deesD-lvxydwr0lGQ72ej-ggUEJBN7ITsQ92iVwBLqmyP7IxX6AERetA3EN09KQ3hwReB-WSSeEpvwqHvfcfuAjig0H-ZWVZu02_69IKMLBx81fVJ5bvCS8myE40NmQH17H0yRYRpxs4vyC4jD58MmC7Xx2eyxbAIoCKkg-fYmIj6SrC3GSUfvQ3V7yfze3T_f4NY-tv2v6z1C8t3exRsxdWXTUzW5_AUOxU3TtOSsfqoObyIWql3DDRqqGA-AyxfmvSJYDFEwv59OVnTLgSg5C-BwyWV1qA3DHODLwq_a8Ie-9bS3AxUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=ne2IJC-grXaynxgsvsLR86MX_g39PusPOj2TU9P66FJ9kOtJ3ebY09bBZSZo8Kufb5-xlmJ4dr3XTu1X4zPptAtGciMH33uJw6jO_kY2fuDAlgJWesY-tT__UFwSFBaCugNAVnVb4KpyL3bqckPNDt06SI5AoDzUxRU5pmpyD7yVRrGNpFWtP4tCIGYDiBiVl9IOBYIqh4pQTcxOTUntrahfp8etrN5Pbgqqi23GKPuyrL4O6RHAtLT8HsFTWub_8o_pzO3sxdN0FEnKY8ccSGvmicKRsnf-Mn7hVJWuJF_WN82uVIuGJQYwZjNunU4nhLHphMouNwyyHW_W9aoq3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=ne2IJC-grXaynxgsvsLR86MX_g39PusPOj2TU9P66FJ9kOtJ3ebY09bBZSZo8Kufb5-xlmJ4dr3XTu1X4zPptAtGciMH33uJw6jO_kY2fuDAlgJWesY-tT__UFwSFBaCugNAVnVb4KpyL3bqckPNDt06SI5AoDzUxRU5pmpyD7yVRrGNpFWtP4tCIGYDiBiVl9IOBYIqh4pQTcxOTUntrahfp8etrN5Pbgqqi23GKPuyrL4O6RHAtLT8HsFTWub_8o_pzO3sxdN0FEnKY8ccSGvmicKRsnf-Mn7hVJWuJF_WN82uVIuGJQYwZjNunU4nhLHphMouNwyyHW_W9aoq3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=pO54nWcOarYxfo-ZHntkpjShGRYUnCfDfuLVsAG9eQQesrCzkxFi5d5Co43v1fXMFE0mcMeLG3h3crFJe1OAH-uyjMVIGDgJmC2fxs-X_n44g7blD2Z1Sg2jzscCpaSe0M9CkkySDGitv70jjIyaE5C_Rgc9GNXVUpKt7HrOPQAGVLpEuv5TeO-hZyS9DcatOEFkcxDhaz7FzBmvCihOEKu5w7-faGR3_YnkzWEu576ZJuB5ZihYcJAMTu5Dj5maicaFfm4LjKyzplt_nrzHl4Wn-VGGmXVjZjswNatw6xy8JKhMdwLj-Ihw70_1keKt2H4ybu16ceMPDMVpDt5l-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=pO54nWcOarYxfo-ZHntkpjShGRYUnCfDfuLVsAG9eQQesrCzkxFi5d5Co43v1fXMFE0mcMeLG3h3crFJe1OAH-uyjMVIGDgJmC2fxs-X_n44g7blD2Z1Sg2jzscCpaSe0M9CkkySDGitv70jjIyaE5C_Rgc9GNXVUpKt7HrOPQAGVLpEuv5TeO-hZyS9DcatOEFkcxDhaz7FzBmvCihOEKu5w7-faGR3_YnkzWEu576ZJuB5ZihYcJAMTu5Dj5maicaFfm4LjKyzplt_nrzHl4Wn-VGGmXVjZjswNatw6xy8JKhMdwLj-Ihw70_1keKt2H4ybu16ceMPDMVpDt5l-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REmTHlc1Y8L-FKVhNeNfAupbsCe4f_VvwSQPu84RaapR1-h0_3ohQvTPpJRxfN2Acz6YrHz8wEeu3s6m--_v5eb10wd609c52Bg3rsdoT41TAVZTN9Cdg65CMUEJWV_vx2GbtDCPuWAKZM71vzAhMZiAyWtc3Grz1lk3kolvEFal5D08pyzKlXgXMmMtFrbo2gtleMlypBDu0ZCPXVjiY30kxBi5cby-8_fJTI2isrxXVqH7M9qEE93paYzA85qeA0YlaBsmoGanoBaMCG-fT9Y-peiHOpum-nTRu98oDoSSYUzmsggbPI9tUTMNW6FaQpjtp42f-LQnJGVjx20WoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=NdusnG-_G-7onQrNtFR56dw_ozBmWiaQNcwloD71T5ZtJtyCBqw5MCHfz3W6jeI1uDyp_due_ev302e3HDFoXMHSIuk7BsLNQRlMDEWGksLDA4Xq--fzaHxzGIyayv76Sr5kbXIpnb6L73cJJUOi-pAjskbkSzMk5oVurAodxdWAXiKY7qt8ED8NDZldZoRqoPc7soXY6lcTdfv945iwNRRzuXqn6-Lr3TeubT9c_gVxoQFz1D25Zty7lLovyb5UBbzSAWtwoEatEdg4J_5NVwP0CQLmGhS6AUsDzPcfJqn4MzjDMJHbJ7xPm8zaFVvOPY4YXo3W-zchExcTR7N1_zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=NdusnG-_G-7onQrNtFR56dw_ozBmWiaQNcwloD71T5ZtJtyCBqw5MCHfz3W6jeI1uDyp_due_ev302e3HDFoXMHSIuk7BsLNQRlMDEWGksLDA4Xq--fzaHxzGIyayv76Sr5kbXIpnb6L73cJJUOi-pAjskbkSzMk5oVurAodxdWAXiKY7qt8ED8NDZldZoRqoPc7soXY6lcTdfv945iwNRRzuXqn6-Lr3TeubT9c_gVxoQFz1D25Zty7lLovyb5UBbzSAWtwoEatEdg4J_5NVwP0CQLmGhS6AUsDzPcfJqn4MzjDMJHbJ7xPm8zaFVvOPY4YXo3W-zchExcTR7N1_zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=oFyRUTspJmPvft90idt2qcC_30Cp7XT0XOAwnn6nsp7i7LEK0j6rR683J_Th_91rdBwmmwIX4qWzVdAzeVizDzNspbtvehi7tYAxzrtDMN-zFMBs-DtnATRBPnnEnw7j66k5j-f4zauDTHEcBjgD1HZRzgY9ls7YJH2MQj46-cBc79HG9GO7PN4qirV-DE7ZvrxrgadihwHGJ_Sb13O4zG9smLsahZZWwJ3fvN_SClbzBT7JWsSqqYM19WtYJQKL745o8U4SlmsMLrbpcaukKY0JTQTRUc9PzrbFMvR7ZxGxWU6g25GO16adly-Y0HPC501E4TOD6OcbjQw2FIjukg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=oFyRUTspJmPvft90idt2qcC_30Cp7XT0XOAwnn6nsp7i7LEK0j6rR683J_Th_91rdBwmmwIX4qWzVdAzeVizDzNspbtvehi7tYAxzrtDMN-zFMBs-DtnATRBPnnEnw7j66k5j-f4zauDTHEcBjgD1HZRzgY9ls7YJH2MQj46-cBc79HG9GO7PN4qirV-DE7ZvrxrgadihwHGJ_Sb13O4zG9smLsahZZWwJ3fvN_SClbzBT7JWsSqqYM19WtYJQKL745o8U4SlmsMLrbpcaukKY0JTQTRUc9PzrbFMvR7ZxGxWU6g25GO16adly-Y0HPC501E4TOD6OcbjQw2FIjukg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MeRvhQcUL1v42V3meqP8krVyitGSIqOeR7jweVXH-i8F1yF8ufwtZuEqBR64ossB0l_G1LmlvExT529_M5jCHFbPBH1UWpM9GIHVYu8SURtzLtHcNgVOQuthM8QgaFb6TuMai8L16zWqRRPydM50ZPwEX-Hnf5qX0sDXb05jI3nUhNIvSnHsdSBd8-PhZyIuFb_NG8evQXzJeomSky9y2jJ3Uv8Cu89-fzXkMqOucYj7-L4RYkRbrjGqyG6U-tetUZs4fKdoNOIzeOdPW9gcVpjtEleNbjlHFbzJx_dWo-e1Y6oLN3Z3zb7D-6AQlmx8FwitxcLircBo3VK7pwdX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2iiBK_pNJ9aLT0xh_baFkNHfEI540r3UhoIPw6-v8yCD_cliWi6lZNGzWWCAhnF6wP82Wq_EMVGKcIHNHfweuVtz8gNlxdNZad7nkEbylN1OEjSDpTz1nFoR6CCRiHTTF_ObL6grJ6WBPd8c9pSBhBLxJiN-W6SOqCFbS445kGJyIziP3cG0Wx6JG8i7rqWzWdgu8lyZctqSLpT9R4yzjtU5HQLU1n3QsEsjVeO4W398QXmq-S_b7lW4kJ8Nc9089cl9-4u9OSW2MvnIrsg-DLTV99Kz18FXcaqogrjw0ErZryDcaR6mLzcV8uEVDP8b-gUl2V2CUy8c_B34Tc9fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=GF1hjgtaal_UkXWIDdqyfCSH4gnh3Y4h3OFZWrZkfE0WHKml7XtHItCAt4CebkSdRLx0HOXG7dUmWjhPe1RFmk8hNSyF6yfwKaP8LCaVO42UuHOCYTBbmxFz3lMku6wE8SYssWmaI3lvT0RFe452EjKDlRd0jJQokK59BZRQfRBhCZX6QfgqCgchMD1aQ4ROsu69XMB1DYH36aZ1bPQ8TFRuiI2E1nsLiSJmRtlGe3-Kc6BiArx1JMGJzGMb7y3Otb65upMT6_PSr_iVWtPiC1UnrxWuqP0SR9e809Z8KbTa19QBjYM8m8bhvaaKzGh1A-2ExE4F3PHlRpvLkjJOzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=GF1hjgtaal_UkXWIDdqyfCSH4gnh3Y4h3OFZWrZkfE0WHKml7XtHItCAt4CebkSdRLx0HOXG7dUmWjhPe1RFmk8hNSyF6yfwKaP8LCaVO42UuHOCYTBbmxFz3lMku6wE8SYssWmaI3lvT0RFe452EjKDlRd0jJQokK59BZRQfRBhCZX6QfgqCgchMD1aQ4ROsu69XMB1DYH36aZ1bPQ8TFRuiI2E1nsLiSJmRtlGe3-Kc6BiArx1JMGJzGMb7y3Otb65upMT6_PSr_iVWtPiC1UnrxWuqP0SR9e809Z8KbTa19QBjYM8m8bhvaaKzGh1A-2ExE4F3PHlRpvLkjJOzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvt5znCjZhmFSccDg_4gvBryo9FmoSNNC-ox7UJf_KhSRr5rxPcKs9Mae_7NHXlAx9sSOlOtu47bkOd-XnjpI6t3dAsYxr9PJJwdIXEIFAYVvcAtS_9Vafv6avLieUkfrcRRO_U_-BPjzSACrYVlvhwEfoptZQwuKfblcldW63qYU302IDxVSnlozEP-JqTc3BqIM7k7KUelkyzTQfSCigQmX540thj4eGP0CO_X5IVzpNfXfWnrMSr9ezNWQmDpxHar4PpowMVqOqfwkyBigkSClMTS1AFPy8XXNyLDpo_mL1a7BMYQYwZIptbww5my-jdEJzykPWRSwAqN3Dz0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afUPMMT37UbdhtJY8yufGUA9FdXrPRRgUoAL2icIBDQERK3PguUbVflY48pTp_wu3QREwiwSZBJGBXhjfBxiKa1xJVQav9R2Fe7yaJ8dDXoTlcjmPf_elfOHUmUt5vO9LjOx3fiyt-l3OJPMgKsAgMOaIoA8awr-i290xKF7EhaW4Vw4hMl1BcbKEIb0GXJ76UmB0PE_sxndSxW4j4YDnAm90AoyeNfotZIPOdGzifFfEMFkTSmhaG_dq7zY7HPWa6IFBYa79cTAKXic_HtyWW8KOBPro78C9_-SzOoMOcuNHtLKo-XIcn6NP7jR6CW-9AQqjKkKDe0hkqeAy16Wbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gkm85gu2H_JdFD0TxiR6rHQYpK4ACmzYMoZqJFKBCqq3W2E5Si17962RVsQbmSC1IxUDXPlXN1C3wnADL_uYRnhbCWyQjn_mDvFPTwV2QckyItZwH625wxWPfesPRwn3ZKGxaCLe8CICHz5voYMCsQy7nZhqpeuw3MHwrnHgnolZuV265apMe29ipiWLUhPl3zMCX0OEDQ1yxMHvtENI1nSXsOELq-F8znctIj1kSepZaX7IYfFvvZfSYnncPFUea7R9l10T5pu7CPFrXglgNRm8vfU5RMrSY5iUpAG0X1_tMmepz3uPwidvaKS6hFIykcFJm8fKW0mqd3VU-eFvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=lHhEIzRLcn-8oGTnScN10IMvHKNNrNwebl7mglKkdsSIorhRhEj2mS79Sy3DAwt0iD0pmtZ3Vno0DXhLYqJokjOwj0mOLIPCVLKIiTPEb7uOccppUWKgul3InVN5CWuQ2Jz24C8rihZ19SxAuaQYExDzLH_5fcC_ky_Ngu3cmUYkYWPMJNH4xzX-znHzDBOedHcjQT_jUgPV7n390QTHdjOtCe5GPQ48zEw6m_Hii3h3L2TBC1Vmc-M1rk-60Y6nq8qUMoSOp1WDn6RBro928s2GzaDsDL-bOeIb1jvu1BTUf_fQw3MKZN7FBVXAXvKtbIrRSxbEJyL2XEkUnE6eKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=lHhEIzRLcn-8oGTnScN10IMvHKNNrNwebl7mglKkdsSIorhRhEj2mS79Sy3DAwt0iD0pmtZ3Vno0DXhLYqJokjOwj0mOLIPCVLKIiTPEb7uOccppUWKgul3InVN5CWuQ2Jz24C8rihZ19SxAuaQYExDzLH_5fcC_ky_Ngu3cmUYkYWPMJNH4xzX-znHzDBOedHcjQT_jUgPV7n390QTHdjOtCe5GPQ48zEw6m_Hii3h3L2TBC1Vmc-M1rk-60Y6nq8qUMoSOp1WDn6RBro928s2GzaDsDL-bOeIb1jvu1BTUf_fQw3MKZN7FBVXAXvKtbIrRSxbEJyL2XEkUnE6eKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=lUPkxAmQOqPhKPAQYdqdqkMjXw9JrOHTkdv9wJ_k97_vGSUjVI4QQ_mBkHJeMgsM3XqX8sE1pIcz1nDrSklEyhCvV5n2X0809qgvQvJp0zCL1JYyY-i9NeQp1dGrz7ba1GF2Fp4epKg8qO4iutAleCop0xti4TpFvVxg7WNgyweFXkCGR52MSTyQqM80zYnsV234QZus2Xcx74jCG7xJNQyqBjrpgFH6GUpnJAHFJCF0O2yDIihLMlMb6xq9mN9FBqVnpPKwz0NUf669igkqININeEwlPsSIAbvDAuOZ2Equmy0GJpln48JrPlp66F1wS68NkFYdQSZsZ8P7WMyd1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=lUPkxAmQOqPhKPAQYdqdqkMjXw9JrOHTkdv9wJ_k97_vGSUjVI4QQ_mBkHJeMgsM3XqX8sE1pIcz1nDrSklEyhCvV5n2X0809qgvQvJp0zCL1JYyY-i9NeQp1dGrz7ba1GF2Fp4epKg8qO4iutAleCop0xti4TpFvVxg7WNgyweFXkCGR52MSTyQqM80zYnsV234QZus2Xcx74jCG7xJNQyqBjrpgFH6GUpnJAHFJCF0O2yDIihLMlMb6xq9mN9FBqVnpPKwz0NUf669igkqININeEwlPsSIAbvDAuOZ2Equmy0GJpln48JrPlp66F1wS68NkFYdQSZsZ8P7WMyd1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Uxs0lu-R-gKBvCfd-HV_UIa5DUtJd-iUZILlVwhsBG4sls_sHQ1ngSfuh6BTYav0_Fn9XcJsdYSTR8GuR0IZvgYO0KBjc6932lrtbBWK7Eq-FLVtxpQXiUZtO6bvHpL6FLHpb07GeGRd20ju2eGv2_ibqCD87jfQ0VsJOa_br9oY4LmgGuwjqohJA2tVIsfyzDdaWQN9t_vEcsWfqj9WjCjliyOQEs09jZuy1FfjHCL8LBAFPYoHjsSG1f_fUjRs421NQPOGI18-8ABw0sCZj6tlKdQcpmFCSZF-oZl4DmEvTEOc2mA_MxWu0HO9uKKnlsV6t9aypIpFA3M91clLvWUzueuq-86azHut2X1t9YFCCO7HDXvBxDBrLFGbJrM_UaQ8GJAgnw4lI4O1afiQ2YF8t8I08L3SsSaQjh9_DFKGKsyaDmdc8ADAJu4z0rlIngoGCeoZXbkezlxe5YXLQQNuIdN9_-I-qPSCBAX0HKS0DNsw9TGS0exPSeFGfGrlYQUt4PVYvlTcvgm0yGRQQGXZvZUBtyHI5Zgsz0NVh5vUK-SmT_xBPdr5wXoXlRMrVSa0UifASZte4-0nfNPB9-oA1Nq2VXu9Y-k_8wWGBQXHe8PoLihgkK3vMPAHMj3zShoHKxxzqBf1YugS8VzDipf2jRIrf0gAiPrhlgbGmT8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Uxs0lu-R-gKBvCfd-HV_UIa5DUtJd-iUZILlVwhsBG4sls_sHQ1ngSfuh6BTYav0_Fn9XcJsdYSTR8GuR0IZvgYO0KBjc6932lrtbBWK7Eq-FLVtxpQXiUZtO6bvHpL6FLHpb07GeGRd20ju2eGv2_ibqCD87jfQ0VsJOa_br9oY4LmgGuwjqohJA2tVIsfyzDdaWQN9t_vEcsWfqj9WjCjliyOQEs09jZuy1FfjHCL8LBAFPYoHjsSG1f_fUjRs421NQPOGI18-8ABw0sCZj6tlKdQcpmFCSZF-oZl4DmEvTEOc2mA_MxWu0HO9uKKnlsV6t9aypIpFA3M91clLvWUzueuq-86azHut2X1t9YFCCO7HDXvBxDBrLFGbJrM_UaQ8GJAgnw4lI4O1afiQ2YF8t8I08L3SsSaQjh9_DFKGKsyaDmdc8ADAJu4z0rlIngoGCeoZXbkezlxe5YXLQQNuIdN9_-I-qPSCBAX0HKS0DNsw9TGS0exPSeFGfGrlYQUt4PVYvlTcvgm0yGRQQGXZvZUBtyHI5Zgsz0NVh5vUK-SmT_xBPdr5wXoXlRMrVSa0UifASZte4-0nfNPB9-oA1Nq2VXu9Y-k_8wWGBQXHe8PoLihgkK3vMPAHMj3zShoHKxxzqBf1YugS8VzDipf2jRIrf0gAiPrhlgbGmT8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=YQqez8nDTDe23uOPWeBBT3sz46Z_wszgjgKV7EjNQGMSVH5HmnFk4cPEEy89PzXLmE3q4Arj4XEYfBXMFEy9l3SCJTzO_20jGu8gKTIh7usgWalHdqGicO8mOFxiVEIr94suDW2cXPx0ztHvFU7gswgJC-jOTsaVkzmSulUTU-19xNM9YxbvxIhhvq650GKuXWXClnOJqCW9OLa3pb4oNiFnai5DayenDH7OuGR1wNAY9LfYiuK1pHigcO8iHGhE1CmoUR1Uu3rwE-6_K5aiD_0pSPXHxHieo285WYeGHl3ycq3oA-maKR0NWkGSePGtN9BAY7PCe90K4Xhy0P2-SgUq7jsxossrPd7MPnVo8vk21Qae2nUS4LqFdkDv-SOrKePdhM152APCoIPahGfcyEKAdZ9TWWCVp58QOBUdVkFAMECpQ2MOLv07XyQJmhTpTwV1YX7nTcFc7qhEhoIOSnUt0_W7oev2_-UsdvtcRVjD-gE-gCnegv-HJvvNsKMmqu3OLDDFk18bJdTTo12b97HzTYrXjXIroF0Uz_lw2kwIg8zYdIPFbcP2yocYrIy5bdv_PqGSdL7uJt1BmTVJAb6SFAU61gADx2x5Q-KX9NRf3CqvKHuxBWsXOhs2NIuaN1nFyQg9XWjt7r5emDflaIlFujcjjmxbP485hWoP1lY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=YQqez8nDTDe23uOPWeBBT3sz46Z_wszgjgKV7EjNQGMSVH5HmnFk4cPEEy89PzXLmE3q4Arj4XEYfBXMFEy9l3SCJTzO_20jGu8gKTIh7usgWalHdqGicO8mOFxiVEIr94suDW2cXPx0ztHvFU7gswgJC-jOTsaVkzmSulUTU-19xNM9YxbvxIhhvq650GKuXWXClnOJqCW9OLa3pb4oNiFnai5DayenDH7OuGR1wNAY9LfYiuK1pHigcO8iHGhE1CmoUR1Uu3rwE-6_K5aiD_0pSPXHxHieo285WYeGHl3ycq3oA-maKR0NWkGSePGtN9BAY7PCe90K4Xhy0P2-SgUq7jsxossrPd7MPnVo8vk21Qae2nUS4LqFdkDv-SOrKePdhM152APCoIPahGfcyEKAdZ9TWWCVp58QOBUdVkFAMECpQ2MOLv07XyQJmhTpTwV1YX7nTcFc7qhEhoIOSnUt0_W7oev2_-UsdvtcRVjD-gE-gCnegv-HJvvNsKMmqu3OLDDFk18bJdTTo12b97HzTYrXjXIroF0Uz_lw2kwIg8zYdIPFbcP2yocYrIy5bdv_PqGSdL7uJt1BmTVJAb6SFAU61gADx2x5Q-KX9NRf3CqvKHuxBWsXOhs2NIuaN1nFyQg9XWjt7r5emDflaIlFujcjjmxbP485hWoP1lY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=k7b8A-1Q2W3G_9cp6vPRuNQMRIMyoPOcPMBgwxAjuVgEK2yPhS_yJI573mR5NQIyH-EVQjjL91b2lDToVJE4z0jYpoX83MQb3i3Q4SuBku51aqIh3cRV_YM6YgNnstUwAeKmQHPTvfUmNyK5oK6qKy4OQebvmUJSbF15y3vHs4_IsR0UqkUunSNNHw_uGZZaIHvEV60CvOnkSvMz-0T60dO3Qu5Sj4mSJR120tk6F9dyHjLh-9ShpqiWQszZuArKMXG-oiOh_Oj5yHKx3XN9jqOgMy1j7Qq098OE2mL_p6GsGqFZsYHUp_vZQxr-TbjO_U2Jri97dYC087Y8sdAq_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=k7b8A-1Q2W3G_9cp6vPRuNQMRIMyoPOcPMBgwxAjuVgEK2yPhS_yJI573mR5NQIyH-EVQjjL91b2lDToVJE4z0jYpoX83MQb3i3Q4SuBku51aqIh3cRV_YM6YgNnstUwAeKmQHPTvfUmNyK5oK6qKy4OQebvmUJSbF15y3vHs4_IsR0UqkUunSNNHw_uGZZaIHvEV60CvOnkSvMz-0T60dO3Qu5Sj4mSJR120tk6F9dyHjLh-9ShpqiWQszZuArKMXG-oiOh_Oj5yHKx3XN9jqOgMy1j7Qq098OE2mL_p6GsGqFZsYHUp_vZQxr-TbjO_U2Jri97dYC087Y8sdAq_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwxadtO1o3eXHF0mtT5vpVB5kD37sbTJsXkno240lUCtKS5YHoA1qP_BCMvh-tqjPlwzXZqY6pJHull5FWYSG9S_NxNXscmUxTjGM92qKyGXChE1en89iDR3PeStKNJ1NmMsZKV3_wYWxNXaRLodhmZ2Ppl0a7hHA5UoMOttKRWW7RkhPyAZ5ITHOPae4lc-OFJ3cXhAXfgm80cjaYAhVb8or79XAYRf2RCQ65nonsM9BzhfQy8SZIM9ZIve6wA1xSlopjX0VFVzpC_pi6FkfDsbwXgazG2DhFMDzCPeNhXHo1PAt6-mcHGx8GkxsXMetjjsSbGUgjO1F9jlPaRTkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=J2RT3awoXbFg3liSRwYeq7VcJ6Db5YyubrW3VLs_ndrsnIzKabSgWnGa2sd28YBlSyApgzQNMNGGqX64mONlarRqbEDlm3g6oq84zgfM8UZegVRAFx9MV2NWvQBX6IFoHtGsmuD5-Lngs15ZC_Hqs9WLx3EPrCZPv5WnmlEdCp4eVwNNxD6XQedLPHlimTPPwG_CU8f62NmrlJ2u45ks99R-W4dDGSfHxh1v_ivHmLwKhKRgZQj0njIowfqjnaQUU8n0lMagoNYyQSM4dw68Yj26qSwLYu2POzNeXvsY78tvCI7GU2ZuZtOFSRAg2Gp_AqJNwroC6rbyRAZuDxw6zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=J2RT3awoXbFg3liSRwYeq7VcJ6Db5YyubrW3VLs_ndrsnIzKabSgWnGa2sd28YBlSyApgzQNMNGGqX64mONlarRqbEDlm3g6oq84zgfM8UZegVRAFx9MV2NWvQBX6IFoHtGsmuD5-Lngs15ZC_Hqs9WLx3EPrCZPv5WnmlEdCp4eVwNNxD6XQedLPHlimTPPwG_CU8f62NmrlJ2u45ks99R-W4dDGSfHxh1v_ivHmLwKhKRgZQj0njIowfqjnaQUU8n0lMagoNYyQSM4dw68Yj26qSwLYu2POzNeXvsY78tvCI7GU2ZuZtOFSRAg2Gp_AqJNwroC6rbyRAZuDxw6zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=T2poDANu96LN8a7HgHgMjJtTEdWBV3fRvgix22fPm1XAMWryjtAPHD0cOf8Bqfsi3SnPPprqfSRXGNjPC3dDnOTxeoZlozaLkC7zUS_HG3D536PcX_aASPE55TcbqQA7nE3Gr8ASWsd0CitqA0l37RdH_rNviUpJAqXC2eTphYlKsOmdDLAZqcHnw9yCFCYzZ_7pU8x9BW0nNi2S7b9cBILiH03aB4aYcjS1zvMfrFvtqojkPZv733wZo_fNWikgUPl3Wh8JGaM0WY24A4OznIRX19abE0pkF2hxxSevvy_lQJiXo9mwF9twnqUe3TMh8I53NndV74Klobloh0A3gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=T2poDANu96LN8a7HgHgMjJtTEdWBV3fRvgix22fPm1XAMWryjtAPHD0cOf8Bqfsi3SnPPprqfSRXGNjPC3dDnOTxeoZlozaLkC7zUS_HG3D536PcX_aASPE55TcbqQA7nE3Gr8ASWsd0CitqA0l37RdH_rNviUpJAqXC2eTphYlKsOmdDLAZqcHnw9yCFCYzZ_7pU8x9BW0nNi2S7b9cBILiH03aB4aYcjS1zvMfrFvtqojkPZv733wZo_fNWikgUPl3Wh8JGaM0WY24A4OznIRX19abE0pkF2hxxSevvy_lQJiXo9mwF9twnqUe3TMh8I53NndV74Klobloh0A3gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyxK4zf6ntxJ3gGWz0XOm2JcrftlYQGm3Kojz54cnVBpaQxdMEI1lgRbbv6WNNKO_0ZPfxT9XdkNqImudieGYBcgt_O7RFEcFfauQgTKqZMiGR5Kgv04JO6HNXYrc4RAl4apzKC5g-DsxZYKlhYSjjXDOOQ8wmyxYARSu6H0Rgx0U_lQFRQ4UNI4bThub-8HTBehkHQ_ZRbV9lM9RIvnjGU9EqCk3pwSB6AGdl7Mngorje3esJv6UTaQVssEAMmu-0Ea_6VM-HS2mLAD7Ac3XmwYvn0L8rnZwDbp7iFoG7JKZk2sNMAwYQV0xyQ5Z80FTJXRWhX43XC3_KidjND4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5GVDTbRk2ebtDHn0RUI-dw79qNlHK--xvW4LCkUmB2hG0fW2_VQ-FzDJkAwzP26cCf0JCHiFRV_wh7i5cVKlawhOI6tHgEiv-nnK7Q12y5760ImETS_javLHP9y_FqRPD9O0yaCMjCGJKZyRzhj8RhIBROCxQRvQC73Egg0MBURhK6fWS5vYSRqIwTJaulzaH4uKPmR83aJHJDLkXgS5_bf3FTkAbC3cKkWq4cPGpOkgxBz5M5uRk2oVjj8vC30ckXYK5JLC6Dm5kjTwA1odNTsfwYlJty29cuLgBuTQTZtmrGFWp6OkQcF5JDxhovn2EjnF9ixFKbl0cTkbWTYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr0hb_6sE4R5BWxJHGNoDJoYBLv0VFfSW2cKFY1z8mrkE0mvKN9TCzmDiUrqzkAqQVmgFBsX-s5xFmDrlIk9vzIOP8ihd6vEhydBy1yfQBmEwpe3d_N7MVPmChMfi1irpL2EFhELdYEARLcpKFERsLoI8bDfcnGPxnVH4tM2sWvpfkUDQfXsffOjOBJjp4MNHfem8QgNWqlHlbkSBx11xB3S4b9B7mkDddiee4m45hXxZm-utIr8mu2fJyb-yRkqiOewdLRBEk9w_ZnDtRMNr854swl7KWv5JF8x3NG-heEcaCkg42AjVVGzSRhshkbIL-Nr9bWST9vUpQidkqIPgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BskTHv4mFFaKXbPGj4W9BO6ozuuPQ4eF2nrLRaoJgfFAQ3AxrxB3WFgaKAjyy98gcbZ2J4KhFw65Tvs1F6yrE-pWs_1uTkY9NYR1Yf5U-xI4sujq8U3YN4wFWRHiFCfsWFcL1pC7ifep6v9lstYlE0tVfIGi2tRFtFC_7a_JCgh35XrwIK2xMtI9Tc3FplmVUeOfon7vPr7VIiFjtuxI6mLSFWf3Z1_sHEI6yKBsrj5UMepiTwdY5MGVaNIzGFcSDjwqfhmdqHeDmBpog-HwcUgTLWDRJfLbjUIdVcwdjXYRPMCa10s7XeQudKRqOvhBTud-RBgtqV9GK7YeOM3oFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHOWLyZvMjao5CUz0_3G5gfT5xYUMNLkCwXdUL7wKx5i9F97V4MehFhi6VvhzZ8B3hEc6DLdKk9SyLAeVE4-8CLASx2EP6OMMXdugTdBfkaiPs4VSBFTf_UylaJiHhAXJugcZoHuV0AJD5okEtj_XB4UHl6Qgd_fjxHkfHMaHrd91j-Txw7gChHXH20NeAxQ_JrLahsEdZUQ4Sg_guOXiNQED9a0X7EQoPtF8pZcSJLHJ9O5sSoCAYySEYnigosP-KEHX1DhKaEeSF1VuRd7vaBTvCzRN-UACtj_m6q3hS-kaCmr8dcRcFvxirlzsHNl0iHyypsw89w0Szeeu9KN1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhbrKrMkukyAHxzqWE1SjBqq0lm3zZbx6SQCHV13LF5CZleJHkC9l0GyxVrpwOSM1L2lMvLcw1XRV-5Uhkge4uIdQWsQ6b8C2pQ23EXjnB0aleOnZYoF_1zKeHI8xvBRCXrPFYarNbblnrenAxrdwUDcZrEL5wRs1OUzHfIBr_N_KQQmT4z6zfh6QMH1g9t6qxlThqurCz3jtKwhHBAnjhjpxwlfY5K7qzARss0bzzr8i9vsK06vcFahI2DIA8nZfFRuz5_Rr0t4CLUcXKIbOD9YYaNDj__pi0X47_5eHSsNwcadO9241zn0jiyq9UE_l5CAHntIFih3yy3GPtFvzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzexPxMN4kehivtRR9-s_nwDqNHe5oEZgW1zwmUIz7c-b6mSkPaNvx_4d7CagMtFR4tLfAHG3vp5ely6qbVIHkOsIDEMhxYRf6DL9Xjh-621XIXQhz9iFUvEqneSbUWEMlC2Qo91Tt06CRI2tuijJlIn6mGjJJ3YQmaVl9_AaNWEsjBAPNfXybHdu2TqUlh-xh7MjvrsTBCuiluZK27c18-H0Yi3TpZINwgpKxInidlmLqM9kh4VmeIFV4rs-u17UJmuHX9GjK_4USaJDr1-PEYE97o8d5MvMATfNcuo5UWrJ1FiWW0P0BcqQV2_ij_a7bMQnKS_8YhcovBiRs4tHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mrXIIUSSpM3dWGS6gXCBR0GaqfrwYduZtYS65qZuzlysiGUtxcmUyWj_YJ7Yrom5qQ1j4QeT1NRZiLKYgt6cAqqACQ16iw1SuWYvG4p0t3haMc2sp_40hj0LYkF7kaEXjopFvUCvdf-_mZhjHX4REqrSFeT3Obr6KEU8BzUKIcZuoRSx_AwTN82AXNyZQrYe_orJbTFYOv76JathRYvhwvIxa2ceSG_GsFsoKcMn9Wi1EgDYTdNHywprfmRPX-vyi2zwZWIKP3JrnfDTpOlQeq7eOu-Jnlsvk79ALUFZexZ22Sy8GZJGcVJQ4VGfrKeoYN5969CSmqwwrUHIGU6ENg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q-afYM0ZDd7HVLq8KYvzy4ujzyYQJtugDGioJ8KhdRJGkT3Gk4hdha-zgpVsNYncrV-PvUO1_WGQMWrtse42MY94WkBaYiSfgGhVz9toK-iuaSSPxYlxheuQClkoLHXXXB5sLstRujmfhfMCw6GTLteQ8Ovfo9Guz65yc_JKV7CIoAqE2ZxiJwhUQzt3Kzhs1usgqrC2Lf4iZwgA33flWPBBaQR-hvWMumlLvuSIGVeiyFPM2iUHKDmiSqq_14c8E1gsWwgpvQdfy_YwEW2p5ZfXG7HcQnPfXKhCGBiCdg8JKK3tHiDX7V8CrGaJb-T1mx--Bz2tKeQ_9-HFyXP-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSSGLwH0NMK7VL7vJHtJKHV4Cd5tp2VrGtjGM32CtrfnjJW9FRU_rkbk-f-Zb0Q-x4O3m9P1mbpL85O4EaK6FZrwMLyXRrGOjnwmInQbFycnSEuZ9oocS0Bw110eQD4Bt7-P50kGYEuEAj0ZoqPQ8wA00DqHVnzrkb06drUInkCRRbTI0uguzJLWSrQrw1bdTUMHuy7_nME0PvERATNHGtgQLqgRbcwhLTUqfFJBRw9VhPjpfRfcHQWLLBVGO10aZ4h7HmfC2ij_yl4cE3Xj0bLj6RsAMIATehoH_oBwp6yjjtimGTP-VWK8LvPhbaHPHdhPlfEJKmvnB9-G7xChUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ASKGTAlQvXSq7yoiPPpGtI3Wmixfv8hbA5vGJh17wyfCPQbw63x8XQHU9L0lsGlIZi2jU0CYIxBi_Ic1Pw4q1KKOTLFE8Y8aW5kPncAewhedjDv8BvXTkO4uqcZVGlgFW719oKsfA_RAeFVinJCgpe8nNhSa3bQ4eHoNoCwMLj86_H4CIiEWWywrUFUo7UuhGgflCwailv6_ZEilAZ9kk4glGVxXt0C_3V00cOKHnm1nYOCLHkgL1pVPebAoLy9jrHRWLUtLbP1yXdVVIRSF6_wKkdJRWJ8w0TrQ28rWPS-VZB5EX8Q2bThbEHsv3zbSTodIyznSzbGfOPXypzE-TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ASKGTAlQvXSq7yoiPPpGtI3Wmixfv8hbA5vGJh17wyfCPQbw63x8XQHU9L0lsGlIZi2jU0CYIxBi_Ic1Pw4q1KKOTLFE8Y8aW5kPncAewhedjDv8BvXTkO4uqcZVGlgFW719oKsfA_RAeFVinJCgpe8nNhSa3bQ4eHoNoCwMLj86_H4CIiEWWywrUFUo7UuhGgflCwailv6_ZEilAZ9kk4glGVxXt0C_3V00cOKHnm1nYOCLHkgL1pVPebAoLy9jrHRWLUtLbP1yXdVVIRSF6_wKkdJRWJ8w0TrQ28rWPS-VZB5EX8Q2bThbEHsv3zbSTodIyznSzbGfOPXypzE-TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cE1i2pb1nef4JlRQSqJYOUTRCzlaYkgSTRzAo0RCMEY54fnbitu9wQVkkkFTTfSuJgvEfQOlB9i_-et7kqH1ZEZt25PpLeIyESbXOwBNkM00K22_kIymZGL4nK1AbuuobWXLLKbGZyEdq1_aCC38ZiQeKuFiieRrg6B4Js2_ZPz6Pww2F8aEETKYRMTWaPvfVUZVAw-IR8SjHRTSLvAsg3fQgNb5sORE1r3Lq_Ty2GH0oTw-DJafLCAii9qeaX93bgK6kCsq98HFoofUlpsf_52pLsMFB4hrtZbt_ps86R3VtmzMck2L6kCrlJKKrgAIJd2Pf_Tem9OdebVHG4vrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxhdtXxu-ImCYa-I9miCfYQsI03QLUbiOuynbh1AQNI8wh_5PoXV43ZFrJMegXtPDMf3n7y4zaNntEoMeW639Xot7ns9BRsvWrY1QOximPbWgwQCSfXgYcs362k4eitSMLj2CfiNlaKxVylb34QGrBi6fxi2WYpzE97DqV1kwen9QYKJvfmFauyrEZVRsBVE_ITXgoZR-t90unBo9X6EfhEInxDcDYLHt62YnjdUm3qQqugu2ZS2zkdB3P6O5rDBAgaNelL-Uc5W9lt0t77gXV5t42tjCpvD20Gfu0i2f00VN6RbeW8ia1Ff3544Vs_2ozR_ZQ7Bmo9StEyycT4orA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=BIviAUcw3Y96m00HyUOh6byNgtelroH4v9BtHztHKxqNQovEed5LnukGus9zDse2WFNkqXKJPo20Sg37Rtl-ZfJHUc1Ntj3OLV50ej2kQ6VYWSW6hF-de0FtQ0UbQOLLlx6NGLmaYzy6WzrWJe_3RlNAI7GdIaP1S7D24bapDcItZS5QakS05iVAwhyme2ylrtxflUYVrs9LpN8gOu-Z_lGLZxseomMd4Rq37sb9k-DypQfwDvYS0gTQIfX-clLnlDWx75CEgv1_kFr_IiX0018somivEm8AoDEIrzoZstcbW0Piz7oOPnxTinB0P0xZy2DutVo1FG5rjfq54bfenQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=BIviAUcw3Y96m00HyUOh6byNgtelroH4v9BtHztHKxqNQovEed5LnukGus9zDse2WFNkqXKJPo20Sg37Rtl-ZfJHUc1Ntj3OLV50ej2kQ6VYWSW6hF-de0FtQ0UbQOLLlx6NGLmaYzy6WzrWJe_3RlNAI7GdIaP1S7D24bapDcItZS5QakS05iVAwhyme2ylrtxflUYVrs9LpN8gOu-Z_lGLZxseomMd4Rq37sb9k-DypQfwDvYS0gTQIfX-clLnlDWx75CEgv1_kFr_IiX0018somivEm8AoDEIrzoZstcbW0Piz7oOPnxTinB0P0xZy2DutVo1FG5rjfq54bfenQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=r6TeVAYPdNcGAECyVkbIjS5Eq6zIlbFt56qFNfLTPCN9jpMFsOe0h8Sm0lHpRuZkAmdRS_VOnq3SWrYjIYIQBp6BLJMvKsW5ysYhDG1TasR4sEnamwABpNquvU73hgLJGbJeZXbRZ2U4RkeLlg5CItKldUHS6IgVEqvMeilui-6KcEsLbLDneIenpzXcHjHty_iNFQTQrQGdQTIj5xAlmQ8mO6AWN_VOcxvqKcgxTKYE6oFk54ENZP39vQxw2bviuikJJ1ytdAnXwsW6jhe4gCipFFWog7_QqOM-vc2AeWCCDgkRAxl9hHTU-9VjxCgf9R_gIsVOhRFvOHQilCU7tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=r6TeVAYPdNcGAECyVkbIjS5Eq6zIlbFt56qFNfLTPCN9jpMFsOe0h8Sm0lHpRuZkAmdRS_VOnq3SWrYjIYIQBp6BLJMvKsW5ysYhDG1TasR4sEnamwABpNquvU73hgLJGbJeZXbRZ2U4RkeLlg5CItKldUHS6IgVEqvMeilui-6KcEsLbLDneIenpzXcHjHty_iNFQTQrQGdQTIj5xAlmQ8mO6AWN_VOcxvqKcgxTKYE6oFk54ENZP39vQxw2bviuikJJ1ytdAnXwsW6jhe4gCipFFWog7_QqOM-vc2AeWCCDgkRAxl9hHTU-9VjxCgf9R_gIsVOhRFvOHQilCU7tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCoUvvulBeGRXm3173HpHPSMEhCeFEJkJZu0XjAgoxmA2xyDL1JseKyXMfqgegngi0Iuv5T3fm7-xjXQ9gdjnmEyIZ1qt0GwDJQh5kBpP-YV770SFoUstSJZR1-6LKUJi6igA7KmGEPyvxZyTxuKkAK9kUVAzP78nnLeFKhEjnKLIT1akyKOjEBVMjoEthJPYFU8pkmf5RQjcAQrXa7chZBGq1lsP9mTZXJVjVf6KJPOmdEWaQr6Q9vvfH71Gw6wUmcD0uT5AmY_d5CuGu2OLW3Go_J6_v3lG1FUXad92T2Md2LpZFKfPOPSgm_R6FOuQixCjnNCVCmZY23zz4B06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJLDdwV7UAELK6s5yrXN1wx3kgAj9LOYwaMMa59XdW6uYJBb1Y8a83uAtVYgyzDd_I21i-fH2v0i-SkfH_lhcNaBWOokp2cD-Mgv1A4jOkbvOuM5ZXJ-6KubSS5I56LnP8KojZ0dODGtOuXtMjm8xwXBr_KUzDTeFAgNHEHDn63yQuKb2gpvmegstrAqrsMeKHPDCsvZjil4gcrePRDoHmjwwM_UIGvjSVRfuc15zOkC_ZoilGd0S2wH8p7d5msP-MU_m7SXuQPkUuyGB1Y7LTlgfP0R8n8nmy-FzaSGbn_GpO1Yz_AsdKkKDwakBA0aBnHjGzEaDoyNGabixw1mxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
