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
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 23:07:58</div>
<hr>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbiOMZLg7HXOMepqETHT7-HKC0SRMuzv1S5xurSETeVQlFnjGx8Wl1yKmDr1PS0HaAHGdEkcGDDGjZTxfc_ZBod-xRmyLL9ldU0bfgwU-3Tag5r3p3rNZ3K4JgfDlliLb0oLxLiz4fcYu81HiHDrLUcLSGcrQe5VZkQwaEOSnu6NEdIzTC5SACjWvWsUAmr95a_yUOg19M-4_o4pZnXWf8Q0cm7nCPpRmKTrdiSvWfVbNlz-pnfHBxE5qjzHDN_vzBqAgY4456K3I7nbH9N95gfFUQpkDGO07whk6_36OLcXTzRjg2dLT2jFWUKBsogSsNmcvFfi2X610rU3DFR_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0-yBmaQ88p--p8UxxWhIXvQ63PmT-O_Eet2mxDZCZuO4FUVtBXyFFEMJj2CfLaGBtfbZCW7b7xdoMspOdQJ7z3hv5HrDxtJV3OUEplsirE6jjE-cZStGr0w8kw39dEIM9fRxQdAHP9tOfOMNhiiZU7mduPDwy1i8zzK9nAdIPrFrcpSf6gv2zeNhBXU1WwmMTQvpMAjmjfP2slQrzK8LmUeb0fy1tsHRBnYG9ApqViHzgBEUbmr_sOMM9z5Xr4wKa6dUSB-Y_DvR8yc-_dIDFeiH_LuEhjhprxxt-kkDCretFQDm7x4dWUmYGwumihxKS19TlhJ5MPxg9PRlOicFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTqVQFinp70oz5TRHA5W7JpxzXlz74iqygmxNnv2ReML2BVuUsNEzpAHBhy83RPDf8ze2YQ95cTAjOlvVya1cfyZWZtW1Igbk6_tOEZKu8vQ5RqQp_Ndb4qN5Pa22z7SaXgzwck0eaZH_t5Cx7RludIRZTQtvm8zEp_g0vagqP3WVN-dfnqp6OsAhQA-729j2m4oagCiKkzMfGJyG9cDAL1xTznWPdMgGdTbXuGf4opboTSQ0FNVBFwboIh8iJTIp2xKW3zqpVKr5BmhdoOG9dXk5Rd0KD6BgWQ4C21Plmr2BdV2Cn4oiie9UBlY6U3KIF2QRCsv8g-N1VMaxDvV_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ_V_etrGfX7y_KWGMZ2OHhzQdWetYlZtFD39SYZPXxf0ddF_wh-KERjWdaeKfaEwipgVCkeaIkLgnFrADXoF1sqDkXalciAEkC9hxCMxtSBoetTs8FbCalCRb76bUoQa1WI7izA7OVZwCgds5rG-mdL9q20In7IXjCSNWN6ufuok2MPz_i-eLOm1DkBbJ1_hs877IVJ2IYIwuMJjHOQ1hz2jO5p7Qs4BrYBFfrJ8Qcbj893Lb1qoCaSMEmUqwPMpxlmzVvAe3sTg1w8736ggJsmw6G2J5hq5qWV9SPB2ykTpPp0NT2ujqA7NYE_-QMFdm7GFCG9hmF0VSnWUJxL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=bzfhZmwZxAnKWxpwsd_dBaZZU_UqUWvgUtIc-NXrzJ-UJmgPsuFHEYc8OG2TdghHgGKnN1NPXUuvSOLIZ19rll0lj2_oWQQDGMzYLZ9RsgEeyFqDMNe7DTpCXChTQkxnAMuPnZcen2g5ffDAhKLnDrsAVFIokTkb-a0c1z7EIEdfit7OP3VODrtg6_OTTmnsebwMnaDdMCLKPhlbFZ2KctQK6yfdI6GXTEMuAeeA42_3-jDr8Dxsj4C05D5yVkOICteMsqTpILAo4tjR1p5oYHnnLcRMB1BhrqEzZFHEqaw219KR_C3SF_07836C9xvfjoEwbeF8jlnuwjMzC0Uy_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=bzfhZmwZxAnKWxpwsd_dBaZZU_UqUWvgUtIc-NXrzJ-UJmgPsuFHEYc8OG2TdghHgGKnN1NPXUuvSOLIZ19rll0lj2_oWQQDGMzYLZ9RsgEeyFqDMNe7DTpCXChTQkxnAMuPnZcen2g5ffDAhKLnDrsAVFIokTkb-a0c1z7EIEdfit7OP3VODrtg6_OTTmnsebwMnaDdMCLKPhlbFZ2KctQK6yfdI6GXTEMuAeeA42_3-jDr8Dxsj4C05D5yVkOICteMsqTpILAo4tjR1p5oYHnnLcRMB1BhrqEzZFHEqaw219KR_C3SF_07836C9xvfjoEwbeF8jlnuwjMzC0Uy_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dovRQ51uMJ_6XC0zS0KZqgP5RIEsU99ZpGLHCjOJMoutrx0Wno5_iphohgLzNi3GHxcC8z-U4c7kVDAFPxavUZDirgdW3NhIEp4UHc6QeilCnu7tr6qlnxydLO8YX9sCO5fGVYxNLtbWtYzrrcIRCmRtSyLSXb2N7Sq2WGzcMmzaZ41sdHx-vYpZW9e7Ffd7YO6ItdLmhEVti8Gotz1TUlEm8NcQIZm4er9Fss9tlfqG_uojnwTKaZyet4Zns129IFHu6Wdo7FkTRxjsHzMT2VOWkKfVFCHT7So7tB24fJsWEZlAJ-u2EYAIAuAM3nlZirrFDJ1BTgcVr1TYylZy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=DTJgz-SMwS3FcjZ7nmCFZ-2hMJgtlxZzVuT6agwsGUVpEMkiFLg4n42-llkgfJQ88hhWxkAB4HnIRh38GToQxIajoApXqZTrSRZtkhAgIDxPjKv1jM4nltaxCATfnhAUodC7py_tzNebXCChk4krwciKMuFGoYIq3CyYmUIRRXKvK5Dezbf0q462uvEGkHc8fpsuvWoBV8n-qBSdvhceRKyd70Ym-ecUNNs6ZakhUxp7BLRUX0SA5Q8_rAMmNckvEz9s1ppbsUZ-ykKYYyCi1ED27pIe_hXhwpWKUUaXZhC4sZRiwljNZNSYJTy_EnZFhR5_HlvZRLmjX2_-MFyRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=DTJgz-SMwS3FcjZ7nmCFZ-2hMJgtlxZzVuT6agwsGUVpEMkiFLg4n42-llkgfJQ88hhWxkAB4HnIRh38GToQxIajoApXqZTrSRZtkhAgIDxPjKv1jM4nltaxCATfnhAUodC7py_tzNebXCChk4krwciKMuFGoYIq3CyYmUIRRXKvK5Dezbf0q462uvEGkHc8fpsuvWoBV8n-qBSdvhceRKyd70Ym-ecUNNs6ZakhUxp7BLRUX0SA5Q8_rAMmNckvEz9s1ppbsUZ-ykKYYyCi1ED27pIe_hXhwpWKUUaXZhC4sZRiwljNZNSYJTy_EnZFhR5_HlvZRLmjX2_-MFyRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpWU3az-puMY29kjql033-BtFnhFoFaiI189f2dOd_fpoalCCtL1pPe8VutJuH0Pp4-DYRqt-Jpa_zUqIQnVi-aJmTVPEnFOfVa9_KSDH1ggjY4XHqkGnsg4ADK2BKcm0Rtx68aFlp8uArTzY7S0vLx4fnyMHjXg7RO2LACYhPmIXj6oOsew63uAkzGLjw0Fk8qqhNyqSbymPzoNM2RSrM-CqkbSmSMGf3WX0u5pzw0m98Tkdo1qOBWK3os0HguLUhIF6v_fsey4UdhaM3k9dw1mmvNC-O5g8RwZXDNp6c3oIDxexQ-FiDm6zvmvX0OhYzUYfftMHf3ft6F0nUGxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=K18HAFin8sXOxOWTS-ClI4-P5Yl_HaWaOUDEqUDU26cUZFEUQGplF92e5oKtHWAVC6Iq3kncxU758TU5AEdn4LRlZRZdIJPxKPRxU4GTl3EZfv3H6t2jMxaxAAOawFwEHP0cW0YXE7cwPyOvjhZXueSBNUjaaxZfV4D1vkdhn_QUYGjjbsPAhqowC3g55QUrijNo8-3H0ZZDNufaRfnFy5ubmXhqF0mWyqEuz2wQwAqEw_loJzSRp1gheQ1yz_yS1JyiTlmDFGtva-yKxIpOSaOztPy8Sm_Bf460y6rDPdviPH69OPvhvXEahzvnBNQQQtmO0ItzOwUbdQHEc7YpmVFVhlNQYF6Zp5R82bbWaLiOylrq8qotU997TPWP4OYh_jeOs3cU1id5nJLC0KzyI9q60ipDsPoTZ02e24t_8z3tUifnpmenw7oW2x3A_D_gkSQgt4KnVmWNtaHtF14XM4CwE7rNL1qWaIZspOG0A6c4gEijFmqE4EvwDQU6n5MMKMOhpeMTRN__Ja0HG1Bh7fTKP_0CY86Ayg59GdOTaAfoRte7D--kXCFmOOrO1EE0g1-SGEudhuEuriONRI8QikURfF7AKZ6C0Xdgv6fJgJ8eo4Tnmaqoz1f9yIpw9kbw38GJeAEqvyiT8N_owYyDH4IDDHGqYpoXhMB6WtazQGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=K18HAFin8sXOxOWTS-ClI4-P5Yl_HaWaOUDEqUDU26cUZFEUQGplF92e5oKtHWAVC6Iq3kncxU758TU5AEdn4LRlZRZdIJPxKPRxU4GTl3EZfv3H6t2jMxaxAAOawFwEHP0cW0YXE7cwPyOvjhZXueSBNUjaaxZfV4D1vkdhn_QUYGjjbsPAhqowC3g55QUrijNo8-3H0ZZDNufaRfnFy5ubmXhqF0mWyqEuz2wQwAqEw_loJzSRp1gheQ1yz_yS1JyiTlmDFGtva-yKxIpOSaOztPy8Sm_Bf460y6rDPdviPH69OPvhvXEahzvnBNQQQtmO0ItzOwUbdQHEc7YpmVFVhlNQYF6Zp5R82bbWaLiOylrq8qotU997TPWP4OYh_jeOs3cU1id5nJLC0KzyI9q60ipDsPoTZ02e24t_8z3tUifnpmenw7oW2x3A_D_gkSQgt4KnVmWNtaHtF14XM4CwE7rNL1qWaIZspOG0A6c4gEijFmqE4EvwDQU6n5MMKMOhpeMTRN__Ja0HG1Bh7fTKP_0CY86Ayg59GdOTaAfoRte7D--kXCFmOOrO1EE0g1-SGEudhuEuriONRI8QikURfF7AKZ6C0Xdgv6fJgJ8eo4Tnmaqoz1f9yIpw9kbw38GJeAEqvyiT8N_owYyDH4IDDHGqYpoXhMB6WtazQGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=UHtO5enQMjJxIh6pGd0oqlmEe-OlrYb5yKJPkM6QeSmZ14rhK4ds2lAIPB0bdqDXNUQf-2LDw7ABPf9W3DU4AbfuajJrryqEdepGnEhDf3IS4Z2m-AuDwSSefuH-_Q66i03h991hKFEf0z_XrtEb2r7NlnP2NSi6xReELdB1XjqHSzl34-v3AL8Mw3MAbMGiwhZpfOTelmWwwNTlB13W6zfwqn87GVSyArwPs12C86_eJj6pmKWMkXGVZtuuI8k3Sm4ZAP2GgGFj11PTjDXKAiLj0xHlk2QqcXiFLMYwNYhS9-prxZpW6s9awOuTQoHAUGQlpTWI-T5-IE3hhtdq4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=UHtO5enQMjJxIh6pGd0oqlmEe-OlrYb5yKJPkM6QeSmZ14rhK4ds2lAIPB0bdqDXNUQf-2LDw7ABPf9W3DU4AbfuajJrryqEdepGnEhDf3IS4Z2m-AuDwSSefuH-_Q66i03h991hKFEf0z_XrtEb2r7NlnP2NSi6xReELdB1XjqHSzl34-v3AL8Mw3MAbMGiwhZpfOTelmWwwNTlB13W6zfwqn87GVSyArwPs12C86_eJj6pmKWMkXGVZtuuI8k3Sm4ZAP2GgGFj11PTjDXKAiLj0xHlk2QqcXiFLMYwNYhS9-prxZpW6s9awOuTQoHAUGQlpTWI-T5-IE3hhtdq4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrS2h9my2A8A9bxwpIp1swfp2DvucRpo9cooR6deq5CIFbCfwYl1k9cbEe_mEcVFIq5igUHaaku38wO2NJNjVe5sgzPijs92eJKCCL_bd-5ICfMzx5pAWaKWC4Q9Hfqokr7N53ao3STKCqa8h3CCZdEPMPBNCEDhGDNG7DYpp_r2X2VZuacI6XdU8eJi3pm6ID09zpgj_gaaGwDOWjZ9i01hgK5TEQmQLPdqYJ_474JeE1OvGmQumaXLDDG_qqE1eQErxcy_0NtTtfIwukGboanMEaNS7o4KLJy5qLOJ5Ra7iI47h31ncTWd9CbpbpltWZOrfL24J2w1_4tsHYiDrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZYw_x_BeVsfdQN5PXrj6nnLuaKN_qT0IbX6mtsPNI-RMVH4T8zJwzuOKlKl4sPuZSTJzK8hFOziUeID22S8kiddCNTqsOKgLL2dxKsDmsOFR6kPWxh7MBHPYvjaToU2rM8OHa5y4tDbvhlpPQJn3dyHuq0ncS1_6YbTWYuyQkH6WzI0BXfIGzggpyrc_BGdSPGAH4cAsWaFagB8oiSLppO_dPCIY5X7phMcN0Hn2UTZmviADQV52AmoeacNb8PXDlnuuRq01zAnzxIsnlDd5RQ5mgzYRywG-uRkik3whdfNvz7dRz7SkKiC4V7M_jqm8DN3qGZMkaMibbef80vD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bytT03ydJYlauCzLBy9yG4U99WPLcUPk2X-B4DIh0PfieSNeMXJDljZWpiTK2z6TGd4H2yE75oyR9ez1HnNZ4ffz-s_mMkzHzUcJ8ljhvaaFRiM9f_A5p3vUh2Aw29i6iYFTG2hdV_zIcA2T80QudTulZQWvhcGLyAuvp-sxGMwhuFRF2dRxhxakjdx-U4rwlxxilw-H78U65Shti7mQ9HkLSvtRkvwRXOEAVf3oFuPtU5uY4vTThFeF8jPKrDm61sHN2M3p474EeVUeoPh7W63MuNuRQRrmCGT_-YGcIWq4EKHDFubHkDp9WoJx8MC0kYu_Sz_4GPWpytHy0gIftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ilRabxG4So5sDZ-DJpXfISCJWGMQxIHQw_ox1T4BP9wTOJMmBeAQTTOJsBFl5wJ7mOXGRZaVnnnM7PSwEb5xDCnQpNOvp9VMSnI5noAtICa3jwgHIqJH4--A9t1Dz0ZQ9jCvHTRjPuLtfYFyUbWrFrour7FR5JxJuHn4sNKGeJhoxKJFF7B5gqWZDJUBrJ1UgN0kLQRHC-5xgxTb-YzWi0HgnXuyrmfDpWvn-0AK42xJOzGQuP_tx0vo2l0uoB2f8XP-hHavMCgoGcHuBzdlhWDFWSR178ygGNU21edYl-W1G1_Yk1qTm3vHNACcdpcx9ZcK6B70HbRawUb2akoafQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ilRabxG4So5sDZ-DJpXfISCJWGMQxIHQw_ox1T4BP9wTOJMmBeAQTTOJsBFl5wJ7mOXGRZaVnnnM7PSwEb5xDCnQpNOvp9VMSnI5noAtICa3jwgHIqJH4--A9t1Dz0ZQ9jCvHTRjPuLtfYFyUbWrFrour7FR5JxJuHn4sNKGeJhoxKJFF7B5gqWZDJUBrJ1UgN0kLQRHC-5xgxTb-YzWi0HgnXuyrmfDpWvn-0AK42xJOzGQuP_tx0vo2l0uoB2f8XP-hHavMCgoGcHuBzdlhWDFWSR178ygGNU21edYl-W1G1_Yk1qTm3vHNACcdpcx9ZcK6B70HbRawUb2akoafQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un1MHDaVOLoHhRCEEzv-ONqiGLDEstanGa63kIvi5edX4yabGU0rBrOb_mxI1ZKhKJtfpy-_t3j5i9sbOmcXJW6KQ6oxMJXPQYeULWhrACDr8WMAbbbGw4BDTv9NumZpHsgaLnp_UePpTWbSpc_02a7D6SNAGX-72lKBxihl1z3bd8JSBn2mUAxk_8RliaMgp2ZDfleDLDv_FUpWR3zH_CuyWjJxM3qfQr4UEkoj8wMfmpIzbUzr7bSM-P0LNB88L6n7sNBiGWZofLAhOMt7LqSCiiquwaa4eEkuBthe8hw24KZqZDluvMtxVTrRuZZwaVvdAM-1UCghH6osAzkERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1-6gtl6DRMyukZApcTt3r1s0WuCA1kkqiM_dH9jsqxaPagTQ_Q2FdJJCFKdwXhgXhMV7jwnvXvEn6NUMyp9J2T4KLi9TYuhgDn-pqLElnASU0hZM_gmMCEwfbKoQJmna5izmpRnRF8DgKLoNPQTeI4k1aYmR-4sG58KstAjIhWs0pkHiPBBxHt9A07wYVrocVBInVfvJMpU6SvZyZhGztBiqTwenHjFOBsbHWx1C5ztWD5auIRYamkyWZjFglcyXFuXXYgxvDQvKl2jDJL-Yyha34igfqGrHUbPVKspBRYPJuiQxqX35MMw5chiFFfa5kVnNmIMAEluyzuw-bbni8c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1-6gtl6DRMyukZApcTt3r1s0WuCA1kkqiM_dH9jsqxaPagTQ_Q2FdJJCFKdwXhgXhMV7jwnvXvEn6NUMyp9J2T4KLi9TYuhgDn-pqLElnASU0hZM_gmMCEwfbKoQJmna5izmpRnRF8DgKLoNPQTeI4k1aYmR-4sG58KstAjIhWs0pkHiPBBxHt9A07wYVrocVBInVfvJMpU6SvZyZhGztBiqTwenHjFOBsbHWx1C5ztWD5auIRYamkyWZjFglcyXFuXXYgxvDQvKl2jDJL-Yyha34igfqGrHUbPVKspBRYPJuiQxqX35MMw5chiFFfa5kVnNmIMAEluyzuw-bbni8c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=VR-VSzo4qgGzifYSg37rzzeYzzpFrxz2AbZByihi6CIGUrxKrq6DihIQr9GQM4JsSFDkMPWp9lACAWu-m3gloDp8icAc39JseTPRvkdWMztVCNvj0Oaby3CoVvNU-qrWJAEGJcNXTCKtIJ3bdGn7QLqY27RWEK-VSfHHEqNFW1bH-D_OfZdZ8HbUeJTH8E-vkq7zsuM8nMmDEqcb_V-56-ZWuyTXYxnJhfNaQ07aS77LRah4D5PwN-eQOeNHlqgiSd1VEag8sEg5UBKjs2Y9QtxOmT4-LUWHQ5U3aHUgkCxwCudOYWPjNyM7dxTtXFfm2zIW9uWDdelPo6jBKxOiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=VR-VSzo4qgGzifYSg37rzzeYzzpFrxz2AbZByihi6CIGUrxKrq6DihIQr9GQM4JsSFDkMPWp9lACAWu-m3gloDp8icAc39JseTPRvkdWMztVCNvj0Oaby3CoVvNU-qrWJAEGJcNXTCKtIJ3bdGn7QLqY27RWEK-VSfHHEqNFW1bH-D_OfZdZ8HbUeJTH8E-vkq7zsuM8nMmDEqcb_V-56-ZWuyTXYxnJhfNaQ07aS77LRah4D5PwN-eQOeNHlqgiSd1VEag8sEg5UBKjs2Y9QtxOmT4-LUWHQ5U3aHUgkCxwCudOYWPjNyM7dxTtXFfm2zIW9uWDdelPo6jBKxOiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=Mj8QQ8IUvNaC9UV-CxFpdQ4NpzHlK7tfnd65JD9tF764VNsT6Fyr8HX3gDd_lPoT0isfU_a6FwMpBAOUaWrwId-IfBEzIhVUpKSTZxaRJDYDgYxWpGXYdS8J7U9YWbLY4KLKCVFpGIwnzwEhX8JlpI5deybG5Ielrf605ayUvHFEc9VlxPWhBNOwefqRhf3wot7dCIoLX3Le4rnWUIGpT2tNqfowI_c04izxQG_UrwM0vi5HEsjKPXlOnxbUIA77l-JJBxANOJl7KfP_uqf-GHvkNt9TtBLM4wkm8r5dp-B_w7quv8rm38ZGgUMU1163R0xs-aDM0iL_vqyX2tmElgpAkS0cHWKcOKYYEIbPEoG24YPaKHzpvF0xgjYCoHGUcZ1N5ZlD7KtX2UBHG-YeRLlqkuaCqqmb5BdI-QiytH0cZe6JTWbYIrs35Gr5ZqgiEaYl16wCzwwcvDaW07HjrgoatOgNtL-2mI1dpO0vsa196Iww07piSYw6R--aePdCgC0ef3KeYou5dsJCeoTtfERDDk-2lDAl8LgNFPpr3tqyRUskULEiblt06Tg_ZJ1MvhpXhOYcVocueuzKy1dToIxq2f4oYA5Vg8qJdIG0ac9-XDpcDMlGSSg5RLb0Y-HWgX805TWlHLP8ubrYxWfUQy-3knXbCrJREl8kzrtiwTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=Mj8QQ8IUvNaC9UV-CxFpdQ4NpzHlK7tfnd65JD9tF764VNsT6Fyr8HX3gDd_lPoT0isfU_a6FwMpBAOUaWrwId-IfBEzIhVUpKSTZxaRJDYDgYxWpGXYdS8J7U9YWbLY4KLKCVFpGIwnzwEhX8JlpI5deybG5Ielrf605ayUvHFEc9VlxPWhBNOwefqRhf3wot7dCIoLX3Le4rnWUIGpT2tNqfowI_c04izxQG_UrwM0vi5HEsjKPXlOnxbUIA77l-JJBxANOJl7KfP_uqf-GHvkNt9TtBLM4wkm8r5dp-B_w7quv8rm38ZGgUMU1163R0xs-aDM0iL_vqyX2tmElgpAkS0cHWKcOKYYEIbPEoG24YPaKHzpvF0xgjYCoHGUcZ1N5ZlD7KtX2UBHG-YeRLlqkuaCqqmb5BdI-QiytH0cZe6JTWbYIrs35Gr5ZqgiEaYl16wCzwwcvDaW07HjrgoatOgNtL-2mI1dpO0vsa196Iww07piSYw6R--aePdCgC0ef3KeYou5dsJCeoTtfERDDk-2lDAl8LgNFPpr3tqyRUskULEiblt06Tg_ZJ1MvhpXhOYcVocueuzKy1dToIxq2f4oYA5Vg8qJdIG0ac9-XDpcDMlGSSg5RLb0Y-HWgX805TWlHLP8ubrYxWfUQy-3knXbCrJREl8kzrtiwTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=cyi51poR8Ri43FqyJmCcHDWIX8xOBHulwwMy7g-xBHUMePw66e2yafZNb86zQAUqHNUlQNTaKltjd88bKo_97xSm9aEScW4v5ZNuKbpAvybOYP5C4ZGmmedumu4jAhO_hGmMWtO4Ekzb9Ow6-9oaoynbQuz3tDqEsSsUB2u1GBo9EmLezbyEHCccT1ZC3mZuGup0013SBq3VwvG-PUmfVM5knFK3_9DUInlI6tzWrKg5nQndfgCf6mn9kJQaYBoVWw8UxxGtMfcgqBmziL1jGlW30lJC9tgCj9Swl9fn90i_JzuIUAnImNRaGVP_vaJLJD6CPqdN6p1P53345WqyZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=cyi51poR8Ri43FqyJmCcHDWIX8xOBHulwwMy7g-xBHUMePw66e2yafZNb86zQAUqHNUlQNTaKltjd88bKo_97xSm9aEScW4v5ZNuKbpAvybOYP5C4ZGmmedumu4jAhO_hGmMWtO4Ekzb9Ow6-9oaoynbQuz3tDqEsSsUB2u1GBo9EmLezbyEHCccT1ZC3mZuGup0013SBq3VwvG-PUmfVM5knFK3_9DUInlI6tzWrKg5nQndfgCf6mn9kJQaYBoVWw8UxxGtMfcgqBmziL1jGlW30lJC9tgCj9Swl9fn90i_JzuIUAnImNRaGVP_vaJLJD6CPqdN6p1P53345WqyZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YW75C4YTBbifwHoK0tFyug64XXKxnQIIU3CV5-20JwISDeqLa-8LhDxPrTf_Cnv70DQoL5Eu3FL-JOh37OIL09auGV66ae9uqcCiOo57fWoS6QaWwoISZ8633zK2bTs79tGlcjEb6eOhcx9SvARCM-SSO-slXOxZAJK4OURgOgFfVambak9BIyvBhc0Su0_KN2pzUz74gMAbTDBv6ZJzQ5IArQNFoNA7HLR1Zzlmyt9f_8Cwarh8rCNExEbGcdPvEGViB0keb1EgxFEbQitJ1jYyhi66VoT5EjZ0I6tjXUQLQ3duWPPijhQlozgUpL_4GZbSfY6Q89LGT9lD3xqMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=b2o0hqqtOKaXq34J-fmEWi6gJMlCiOHhk54yU575mkppj6ZpmouZNAXhDaD5aaShfMMCaiU1ANaxrtsEEFHMBVZOrKz7-sYZUY8BCzPk2MBJjMfZW9EgGyqO9HYBrZ4TRuiUTDa1PA3fitEjnkXzT8B63g7jzYpciEwrMF5bfO6YaGO9w2Udu3zMq3-gklcMzI0HClWOdjU3QrZn083z_Fn37k56Q22TDshRY4FK_Q6Rn1r4ueEgb5O0MGAtsFngwY_W5h5xcs75Qgv7jcrz8tlFut0rY91Q9ux7GJjLdFT4D3tBKd9slOWvXFfN8AdENFjJ-uyesgK4b6QZyAclGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=b2o0hqqtOKaXq34J-fmEWi6gJMlCiOHhk54yU575mkppj6ZpmouZNAXhDaD5aaShfMMCaiU1ANaxrtsEEFHMBVZOrKz7-sYZUY8BCzPk2MBJjMfZW9EgGyqO9HYBrZ4TRuiUTDa1PA3fitEjnkXzT8B63g7jzYpciEwrMF5bfO6YaGO9w2Udu3zMq3-gklcMzI0HClWOdjU3QrZn083z_Fn37k56Q22TDshRY4FK_Q6Rn1r4ueEgb5O0MGAtsFngwY_W5h5xcs75Qgv7jcrz8tlFut0rY91Q9ux7GJjLdFT4D3tBKd9slOWvXFfN8AdENFjJ-uyesgK4b6QZyAclGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=P4oW3XQljNE38u4R6NodH0uTeQuT3yEVGWC9967OzHv4lLXijtAJhQvy3QKA1Y6qA8DjzhbttT-RiORomxJNinAFm0sunNx5JudExlk6u3eGjoLEOOk0HZhV6YrAQDrSRxUIXsYneCLSAThv91F1xd9ldmETMQGRddm5SKBBpyQKsH81bv-_SFC1xT9C-2ckiJHe9bKbsxz1aRitdCuf6t1djtpqfd1_YyvQ1weiYdmsAaDmNTPdQevK19hPznOy13GeTOKg8lq8dN2Ckxf1IJK3PzyO_AjuO7oeT0NRaH_UQgZhO1ps2fPswUx9PcylCKsg5LZ0GEgib_YqUmeP7BmeoDhgVSyzmr6tD3OOlMC0CiXR2KKIdVk09B903iwgL3axwgA-aW8hA3N0ooU4nj-YkUzHksBNBeMeXpGLyBYYINbePa-edy3DJHT6RUi2-9O020vd-fkuCLLBYELI8NR1gj83uaS_lFRVhLRFTtUCaSSSZFwWqKxnR76HkGIBrARXEApUl8w8UcKbVvW7pc6fiQvy1q8XezkbSrKbjRC7G4t-4KixH7cAC8Ijsgo1dB149HIXmzIx34Ln2a_0Bc0zcf2UiKFX1gkaAkb34Ub5DHyPeH9HKO-824yRwdY-b3sC-1PqvqCyM4QsICjzg8z255syuqr_z-4ntGjEZ_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=P4oW3XQljNE38u4R6NodH0uTeQuT3yEVGWC9967OzHv4lLXijtAJhQvy3QKA1Y6qA8DjzhbttT-RiORomxJNinAFm0sunNx5JudExlk6u3eGjoLEOOk0HZhV6YrAQDrSRxUIXsYneCLSAThv91F1xd9ldmETMQGRddm5SKBBpyQKsH81bv-_SFC1xT9C-2ckiJHe9bKbsxz1aRitdCuf6t1djtpqfd1_YyvQ1weiYdmsAaDmNTPdQevK19hPznOy13GeTOKg8lq8dN2Ckxf1IJK3PzyO_AjuO7oeT0NRaH_UQgZhO1ps2fPswUx9PcylCKsg5LZ0GEgib_YqUmeP7BmeoDhgVSyzmr6tD3OOlMC0CiXR2KKIdVk09B903iwgL3axwgA-aW8hA3N0ooU4nj-YkUzHksBNBeMeXpGLyBYYINbePa-edy3DJHT6RUi2-9O020vd-fkuCLLBYELI8NR1gj83uaS_lFRVhLRFTtUCaSSSZFwWqKxnR76HkGIBrARXEApUl8w8UcKbVvW7pc6fiQvy1q8XezkbSrKbjRC7G4t-4KixH7cAC8Ijsgo1dB149HIXmzIx34Ln2a_0Bc0zcf2UiKFX1gkaAkb34Ub5DHyPeH9HKO-824yRwdY-b3sC-1PqvqCyM4QsICjzg8z255syuqr_z-4ntGjEZ_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c00vQmVtkYK8WG-HLcQL1XO9orqngCNX3j4uvFdLk7RksALlQ_bY9FfrdjOAaMWZ1WlHFfFeTmDDg7Sm2VLFYcHOy39EWXw0EE1UFNc574tiFHn1y0aYx1kNC3Ovk1pQVEoCJZV58qFa_C0IGWB-9xB6YYMwlv67wvpfr5jxVrwaEAsDp9Mo2Kk5HmkA_C2deo8PEqn6s7Hhmbt2epXKgxPXR47ODW4Ix3zYeYUvLeIJguvriJADE4CydW2CUwJcPfe1l8I9QhglHYoA5ZSwdOUE4YwkkgMdDairjh7nXvku7yW8ttZUXdZe4aAsx8DfIiV5Qb6AFJsPHAMYXvOXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=WQ_BWftNOrB77W_UxbWXnDPjcnwwTejIA1aC0LP0SwHAQ76uRNZcCHCyGfd3MmHX5ygujUwDjQz_POdfsW6IQ8ImSUQMTqAS3wFqLkrPgTATz9Hm_zehrwfWvf3HlbOBuoZKKIvzbe9wEq2so49_Z08ZyBasWYufLBJgiVKceJs0uNj9rGZimmRRAz3nUd5cAo8iTlr26asrTP9vTQQbNrDNtKMNaFiFg6IFHn-FdN4LZQeuOCUnQK4WvLDaAK8c6iqYKwZoZYiN85qsDApyT938ZBP1f2oJsWlSE49RuzLpGXdj1Us2nFH5mPOaPKjVW6jeqXaQKfNwnS_nFlNCNh3GF0Xom_ELnpGEdwCpN8h0YbO44Lgipio-NvE_4rk6zoJB70geIsPxw9TwfDjp7tR_UdsVDwQegTQONHXPUVNWa60lwuA97UTwUZ8hHNJrhQ0k5i4A-j3WwVE3MF_E3TTXuhXjiFLdAWCLomdoadlsz2MoivxUSn8CLSws83xx8ZjjOvSiSFSTRSCoNDRxYZAv6l5CYRaul5GuxfZRja4gujhXgvMMTlGLSi4YzbgXEW1SUkLMNqzoelUguOJjm8GK-U3dxsok1eZ1UA_4wU_Yq-R3g6GG-xEbcv-L8I1BhxS9w1y9MKjFg8YuPn0jbi4k1Q3rNVOJxkVfJziRG_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=WQ_BWftNOrB77W_UxbWXnDPjcnwwTejIA1aC0LP0SwHAQ76uRNZcCHCyGfd3MmHX5ygujUwDjQz_POdfsW6IQ8ImSUQMTqAS3wFqLkrPgTATz9Hm_zehrwfWvf3HlbOBuoZKKIvzbe9wEq2so49_Z08ZyBasWYufLBJgiVKceJs0uNj9rGZimmRRAz3nUd5cAo8iTlr26asrTP9vTQQbNrDNtKMNaFiFg6IFHn-FdN4LZQeuOCUnQK4WvLDaAK8c6iqYKwZoZYiN85qsDApyT938ZBP1f2oJsWlSE49RuzLpGXdj1Us2nFH5mPOaPKjVW6jeqXaQKfNwnS_nFlNCNh3GF0Xom_ELnpGEdwCpN8h0YbO44Lgipio-NvE_4rk6zoJB70geIsPxw9TwfDjp7tR_UdsVDwQegTQONHXPUVNWa60lwuA97UTwUZ8hHNJrhQ0k5i4A-j3WwVE3MF_E3TTXuhXjiFLdAWCLomdoadlsz2MoivxUSn8CLSws83xx8ZjjOvSiSFSTRSCoNDRxYZAv6l5CYRaul5GuxfZRja4gujhXgvMMTlGLSi4YzbgXEW1SUkLMNqzoelUguOJjm8GK-U3dxsok1eZ1UA_4wU_Yq-R3g6GG-xEbcv-L8I1BhxS9w1y9MKjFg8YuPn0jbi4k1Q3rNVOJxkVfJziRG_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=vhh5H1XEO5o5lZK5bDBTxIki5kGtlPVI6GfXKEov1qoWP7s-Yu9cmUQfaIg6-n7_HAFlCVFbks1c0ECo7619Ch5fMJo43NGG-mx1pJVkmusvxvQ0Pi2B92slMyZ7krcyZEBDhm_MrayaUUOUjdbj8E6WCsAbwfHn8X3c12PyUuYkurz_L8J-pgLVVEej5A5FPklxa5w_vT8lkkBS4mgQmR9Y8ZJ1VOv9-VVapEZkz6W1EXjT89go5BeNYTXw5ZhhBXrvcxh-HO3sOawJNsD46RrzyrHhvHiR0buutG-PeNjaAJBK5AeCLX-MrTeTmVVnS7iQVZRuAMU9dGyXoAxHEZR6E-DkNtlRJ813VHRgq1dyAt1jP4xV0zJKtKVMtebZvQL7tXrILdQNJ87UfD98BrXBFh9m4btA13YwTvHEKPGYMjSreHK4DgIMD7htft9Epl8vI-yIhmKmVC65rEZ2Yj0UImc7RmFnczdj2VPyIzeYTSFsyraYVtoLu60nxf7NoZXJ1hVjZF8iu2gHOmq718MbcYJAr4FYMTeG2gHJ-2SMpc3EvIc9cA3P9CfTa87fMRyc1Hvcd9DUUXHv8B_Z3bNxYl1TA4DoXyE-Kq1SWdSL9NkomLfT62VCMZZBgXvChjfaw6ClJZt8y-DHYTVRFyiZgnkLRz74u9KWyuub8-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=vhh5H1XEO5o5lZK5bDBTxIki5kGtlPVI6GfXKEov1qoWP7s-Yu9cmUQfaIg6-n7_HAFlCVFbks1c0ECo7619Ch5fMJo43NGG-mx1pJVkmusvxvQ0Pi2B92slMyZ7krcyZEBDhm_MrayaUUOUjdbj8E6WCsAbwfHn8X3c12PyUuYkurz_L8J-pgLVVEej5A5FPklxa5w_vT8lkkBS4mgQmR9Y8ZJ1VOv9-VVapEZkz6W1EXjT89go5BeNYTXw5ZhhBXrvcxh-HO3sOawJNsD46RrzyrHhvHiR0buutG-PeNjaAJBK5AeCLX-MrTeTmVVnS7iQVZRuAMU9dGyXoAxHEZR6E-DkNtlRJ813VHRgq1dyAt1jP4xV0zJKtKVMtebZvQL7tXrILdQNJ87UfD98BrXBFh9m4btA13YwTvHEKPGYMjSreHK4DgIMD7htft9Epl8vI-yIhmKmVC65rEZ2Yj0UImc7RmFnczdj2VPyIzeYTSFsyraYVtoLu60nxf7NoZXJ1hVjZF8iu2gHOmq718MbcYJAr4FYMTeG2gHJ-2SMpc3EvIc9cA3P9CfTa87fMRyc1Hvcd9DUUXHv8B_Z3bNxYl1TA4DoXyE-Kq1SWdSL9NkomLfT62VCMZZBgXvChjfaw6ClJZt8y-DHYTVRFyiZgnkLRz74u9KWyuub8-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=o3wYmjrju_dsHqDEZyTtHYghtZ9dHGIJvPLT1N43Y1SMeRLFB_OtYogbMHEM9bCpHdV9rEG0AiLzEKOltHPhiCAdyGIAbQyHJxpa6gwXQ-H4vwDpjoqDsBbwx31dMFmLp2WNMYouaRAau80A7JAeBWns5Q8Cd65Z1si24cLxDkvcGcFNtiFdRsFKCK6h0f61ni2DHrit-MmYqi8mKqMGKc9hcXodh2NWBhO0UO1XQKZNTGObnsD-AtP9PcFCMdGHMXgL8yx81qju-aL23VqGmoKQuxSvoiwYoK-5FOpJp0OmjNIMEQgYeZ0jIaDKQm2Gp3LKN7eAO2X7776dOrt4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=o3wYmjrju_dsHqDEZyTtHYghtZ9dHGIJvPLT1N43Y1SMeRLFB_OtYogbMHEM9bCpHdV9rEG0AiLzEKOltHPhiCAdyGIAbQyHJxpa6gwXQ-H4vwDpjoqDsBbwx31dMFmLp2WNMYouaRAau80A7JAeBWns5Q8Cd65Z1si24cLxDkvcGcFNtiFdRsFKCK6h0f61ni2DHrit-MmYqi8mKqMGKc9hcXodh2NWBhO0UO1XQKZNTGObnsD-AtP9PcFCMdGHMXgL8yx81qju-aL23VqGmoKQuxSvoiwYoK-5FOpJp0OmjNIMEQgYeZ0jIaDKQm2Gp3LKN7eAO2X7776dOrt4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=uiCQyE3GaVbqWer4abSe7husW7hNSvnKBaX0OfpkgM9TzqGA_0QYaFVqObhnvxFqjHt2-DPAOZI7UOEvo0Emoe0WmdudPDAuj1nUXL0l0XA8pBX8Rty9Gy_P_uM_iO5tiRz7GhwAj0eenzeFH0A7sDtuvpDFlKPesugCDVRUaQ-tBUPQQqv_h-HMeM3nt7DRadP4C9bnYxvDfnBt4b552QvUULlZda8yidS_QAu7FxMCAhfF2_7omEZciQEBTpLTiUbzGuvWUBu8nrZhcZto7eyKe6ltPftyl_uzGtGhnTajE6h5_JXdMMNpJULmC6G3AsgdC6ud-fwDjgZ9DxJ2Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=uiCQyE3GaVbqWer4abSe7husW7hNSvnKBaX0OfpkgM9TzqGA_0QYaFVqObhnvxFqjHt2-DPAOZI7UOEvo0Emoe0WmdudPDAuj1nUXL0l0XA8pBX8Rty9Gy_P_uM_iO5tiRz7GhwAj0eenzeFH0A7sDtuvpDFlKPesugCDVRUaQ-tBUPQQqv_h-HMeM3nt7DRadP4C9bnYxvDfnBt4b552QvUULlZda8yidS_QAu7FxMCAhfF2_7omEZciQEBTpLTiUbzGuvWUBu8nrZhcZto7eyKe6ltPftyl_uzGtGhnTajE6h5_JXdMMNpJULmC6G3AsgdC6ud-fwDjgZ9DxJ2Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=VPGk8eFHifrmceru0DZClQhCy4rKLeTx6rZmfkaJqC-jremB4cMo_gjViCp_kKy7YhOF5nm7G8FMpZIof8R9W31H_Buw8-Pe_897f-7nwonvtHMKJzo1-EVcaVdtJwxUDNgGqvjHApcW7NPgz4WSYoSgh-piqs9NI4mx7fR7xd9PD9rnI8wc4lkz8HLamZWESZvVyHyYpbMysXL2WckTaPHXltOrqZeenZJDSgEv1YGHqB51fyQ-rWrt7gCO59lARHnKxSqxy-dmtJ1DCpCcMa6tVhbwDlvT_E9TTpWpPdqyXRVkHX4xpYgr79A2-u_ufkVUdr_WYiYJExyB_AiJuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=VPGk8eFHifrmceru0DZClQhCy4rKLeTx6rZmfkaJqC-jremB4cMo_gjViCp_kKy7YhOF5nm7G8FMpZIof8R9W31H_Buw8-Pe_897f-7nwonvtHMKJzo1-EVcaVdtJwxUDNgGqvjHApcW7NPgz4WSYoSgh-piqs9NI4mx7fR7xd9PD9rnI8wc4lkz8HLamZWESZvVyHyYpbMysXL2WckTaPHXltOrqZeenZJDSgEv1YGHqB51fyQ-rWrt7gCO59lARHnKxSqxy-dmtJ1DCpCcMa6tVhbwDlvT_E9TTpWpPdqyXRVkHX4xpYgr79A2-u_ufkVUdr_WYiYJExyB_AiJuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=RC-Se29759K7nlX7NQOr25kKmJNCl8LD2Fxp-NZceCyj3mXvtA5hHKIqiUBLDYM3Tp5SkZGJo1lrrm8u93skOMIa48Ok6PBL1JnSxgI-GV81U_V_VrJX0U5ZzaT6tOY9Mtz4Y5muMDkyX6HRz2Pj2D5SZoql4S8q8KyrXvBp8pLihtn7zNQyN0dfyhHwV4cpoI9YvHPunEpXi-OsivZQqyZR1CLnNu5n2dXnw7QKeZvleE7GArI1Lf_UwpLMCPIM0QTkdhEM9xSUOisvglJBe5sUCneFB5C8LVpTx5g0CxxhE6Ok70bYHkLZzZtDafD3qkrbKvKftsD7BoSbYCaQ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=RC-Se29759K7nlX7NQOr25kKmJNCl8LD2Fxp-NZceCyj3mXvtA5hHKIqiUBLDYM3Tp5SkZGJo1lrrm8u93skOMIa48Ok6PBL1JnSxgI-GV81U_V_VrJX0U5ZzaT6tOY9Mtz4Y5muMDkyX6HRz2Pj2D5SZoql4S8q8KyrXvBp8pLihtn7zNQyN0dfyhHwV4cpoI9YvHPunEpXi-OsivZQqyZR1CLnNu5n2dXnw7QKeZvleE7GArI1Lf_UwpLMCPIM0QTkdhEM9xSUOisvglJBe5sUCneFB5C8LVpTx5g0CxxhE6Ok70bYHkLZzZtDafD3qkrbKvKftsD7BoSbYCaQ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=BG2DauLYlquK0PC3URoF22eKIQ06FZW9yyYM4gtehzxOTQftPW16Kz8OyyhgQdZxeyEtJp7cmhzfFDvrPBT0Uo1dvP5pTkBqCQOyZ3XpcahVvBQdVHKZx9c3X2ywgppktWl6KUWXLsqC5C8K159AyWOVT9ZRX2a5AZnc9cddRxbs9VyTJQVOaVoKTUT3kYzWebFEQuN1_Z1HHY10P7-oG9N9Q4VmXG8luHtf4kxaNXL82zsvCn3C9-GNUSr5CTJAoZ_8SlnRTOH6slI5w-yHjQzbpNJVx0m9N3iJ2ebGwxdfroO43jwiX-sh6Z7Nv52DGqF5Gu0usaZrXwHO5Obc7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=BG2DauLYlquK0PC3URoF22eKIQ06FZW9yyYM4gtehzxOTQftPW16Kz8OyyhgQdZxeyEtJp7cmhzfFDvrPBT0Uo1dvP5pTkBqCQOyZ3XpcahVvBQdVHKZx9c3X2ywgppktWl6KUWXLsqC5C8K159AyWOVT9ZRX2a5AZnc9cddRxbs9VyTJQVOaVoKTUT3kYzWebFEQuN1_Z1HHY10P7-oG9N9Q4VmXG8luHtf4kxaNXL82zsvCn3C9-GNUSr5CTJAoZ_8SlnRTOH6slI5w-yHjQzbpNJVx0m9N3iJ2ebGwxdfroO43jwiX-sh6Z7Nv52DGqF5Gu0usaZrXwHO5Obc7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=oQH33b0H9XRS1U6l7OqKwAyT7C_3XwS1b8gQlmVcPKHgVgdYXZFg3dV7bDNzzuwsiw7wUBgnSkmaC2okwJrKkg6Lvp_5tt6xgYtffhMThHwuR-qDNlzjAjSIxOzX0eh3aJjjEo8uTnJBxMVe5bvbKRFMN9O0LdP9v0BarTLw2rqJNN4QNS4b94U_KJvmT4EcX8F08fQQSKXixPH2jY5HEHMSa7RDyMFI9FW6fCmi2jXv9Ed2KxsClHAxIEKjkn0bRpZVVznjXCg-wePVUc6AMTAzPWZN0Hh3bBAFil9Zakqa4DpIVvKaE5dK_jcAhhSQUNBKZOKwQBjZyn0Gx9UmdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=oQH33b0H9XRS1U6l7OqKwAyT7C_3XwS1b8gQlmVcPKHgVgdYXZFg3dV7bDNzzuwsiw7wUBgnSkmaC2okwJrKkg6Lvp_5tt6xgYtffhMThHwuR-qDNlzjAjSIxOzX0eh3aJjjEo8uTnJBxMVe5bvbKRFMN9O0LdP9v0BarTLw2rqJNN4QNS4b94U_KJvmT4EcX8F08fQQSKXixPH2jY5HEHMSa7RDyMFI9FW6fCmi2jXv9Ed2KxsClHAxIEKjkn0bRpZVVznjXCg-wePVUc6AMTAzPWZN0Hh3bBAFil9Zakqa4DpIVvKaE5dK_jcAhhSQUNBKZOKwQBjZyn0Gx9UmdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=OuCK1Y7s90HNonl68t61d4KO_S2sFzuiJpxilkUTZRiOuY-EKtaJBYHsCSyCu7dw33d2aREpnZp1eAYk7FbXVBCgK6IzNGbYfuzfnMQYINDQD_mMLG011zWQHDre83oIZWf6CaRFmbgFEOR-XaWPSmZXy5adZzkmqAtRo3xMOqc9Lq8EuFLulht1fVijZG-5k3scCQw9kgyGy5rSpMQQdkGI6co-j_kEFTtG9WFFpqG0oXReVSO0-4j11wmzdUDMrr-4Us3rr2M5Qsp-g5Fp2P8X8gOIqUePa0M1i9_NYxJoRsZCdhVksldEw4Nc6PNI9yIlAmcyj3GuZ8UOsUE00Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=OuCK1Y7s90HNonl68t61d4KO_S2sFzuiJpxilkUTZRiOuY-EKtaJBYHsCSyCu7dw33d2aREpnZp1eAYk7FbXVBCgK6IzNGbYfuzfnMQYINDQD_mMLG011zWQHDre83oIZWf6CaRFmbgFEOR-XaWPSmZXy5adZzkmqAtRo3xMOqc9Lq8EuFLulht1fVijZG-5k3scCQw9kgyGy5rSpMQQdkGI6co-j_kEFTtG9WFFpqG0oXReVSO0-4j11wmzdUDMrr-4Us3rr2M5Qsp-g5Fp2P8X8gOIqUePa0M1i9_NYxJoRsZCdhVksldEw4Nc6PNI9yIlAmcyj3GuZ8UOsUE00Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VblNRNZ5Km41b7TYr-Id9Wjkkn1bBFYzpTVW1ZH38-Z88bVnTa7RCNrusyrdlMoZR5TN4C_VXT9Krv2fvXOydqf3FNL1_FFbnS6Z677rOVONEIqYB1FcW2-C-BCz4_J5HYFuBTB3fOYd86Y0VJfQp6Pgc2cHQ1tzGlNYJSo6tQFf-hev6tohr3RRnXQLURnGi1UZQSqUFVvOJip5SlUBFF6pm-vGP8AaxeV3rlFliQO5bSvHo3Pme2_4BH009_Rzb17scp_9qofL-1crSf6PE9oPxUjFCxIR7EIeI7GDXxDZLMrP_EL7iiLpBMqjRY0yglUJEAz0HFk1VTQTxeC6tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=YW1lXO93znE1qjMcirVctg7tal1aC-2lb0ELbHXfV6Y8ft83r9B8Yr3r9zCBUt54_r1ZYh8BwxECac6QYz891lEpqRUPwuy79ABY1btYZZTp3bVbAiHs8A5jaBQGUMASqV9RKspj-axxeBIu-1LB3xGqc9RMd_DmxfN9M29FoCXSee20J4KOsj8jNiEBuu0o_PmrMIKDsqWAuX5K0AXA72BhLmiOkF386YLJ_38Ood7KvLA5bq9raODXs1PvX6cahEJ2Zuj9KXcf7j-vRaqUM1hJGCMu84ZpB5NHc2s0kIQu-HmKwX1pFtucUTKWPh9JcmSwiq1AVgogg_R5YG_D1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=YW1lXO93znE1qjMcirVctg7tal1aC-2lb0ELbHXfV6Y8ft83r9B8Yr3r9zCBUt54_r1ZYh8BwxECac6QYz891lEpqRUPwuy79ABY1btYZZTp3bVbAiHs8A5jaBQGUMASqV9RKspj-axxeBIu-1LB3xGqc9RMd_DmxfN9M29FoCXSee20J4KOsj8jNiEBuu0o_PmrMIKDsqWAuX5K0AXA72BhLmiOkF386YLJ_38Ood7KvLA5bq9raODXs1PvX6cahEJ2Zuj9KXcf7j-vRaqUM1hJGCMu84ZpB5NHc2s0kIQu-HmKwX1pFtucUTKWPh9JcmSwiq1AVgogg_R5YG_D1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=RwhyD0QZsFqdjqtk2b8dfjdh8cvrqJme0Ex6OWMBdZm-FfLfGQmfW4ufE6Y6Vn_UlPLzlMyVxcY_Tzeo96bHIVs1Y5c1AEXM5bYJMBIEM-jTFIesMGAyFNC7yfU-MIASp_j1BKFmxLEhTJBF1BWukFoKgVaYwqYFddJQ6WBArdo325vNft57yh-DwBrsJMEZSW-NlQeAqTvMA_GpmL3YruYwy1wy3y8m3H74u8081EOlMb1KFvvXW3EoH5J8EmHo0nq0kEaz5F71SdJoUynodItB_Jz786PO0RT2Htb8WlkNUlCWEKkLc5Wagb-VJmkR8eRGLDM2II1e2X3cgOzoCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=RwhyD0QZsFqdjqtk2b8dfjdh8cvrqJme0Ex6OWMBdZm-FfLfGQmfW4ufE6Y6Vn_UlPLzlMyVxcY_Tzeo96bHIVs1Y5c1AEXM5bYJMBIEM-jTFIesMGAyFNC7yfU-MIASp_j1BKFmxLEhTJBF1BWukFoKgVaYwqYFddJQ6WBArdo325vNft57yh-DwBrsJMEZSW-NlQeAqTvMA_GpmL3YruYwy1wy3y8m3H74u8081EOlMb1KFvvXW3EoH5J8EmHo0nq0kEaz5F71SdJoUynodItB_Jz786PO0RT2Htb8WlkNUlCWEKkLc5Wagb-VJmkR8eRGLDM2II1e2X3cgOzoCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=M07MwPPvizdUmPyZVchs_XLUqmmfbDpRwauavzDf4iDQHlBGsmT8sMprnxfS6tDVFs-puvB9ex9GLEuC1IzMyLQ_imEPyuQghMbHAzR1OTAWlFArD7xxJ6lEI6FTLMSIr8RoRvDowrc_mXEz-jeALOetjnfZ-JqfdVgeEvj8grk2gHfLLkFWKuHl4sxHi5Iy1ViCV9vAbsnMETYz6Xb6-RqKRVZF2M7B9CE1SSZafJT_FfvpdoL3wN8p-Vox7uVK6k1MBCdab-l-J6YgQoRjsLkN0-kpbBH43r_yUe3rZ-8On2wkFEH9pnlFw3Hg8M8MHq8ljYBJlh8TZaaos9Jtnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=M07MwPPvizdUmPyZVchs_XLUqmmfbDpRwauavzDf4iDQHlBGsmT8sMprnxfS6tDVFs-puvB9ex9GLEuC1IzMyLQ_imEPyuQghMbHAzR1OTAWlFArD7xxJ6lEI6FTLMSIr8RoRvDowrc_mXEz-jeALOetjnfZ-JqfdVgeEvj8grk2gHfLLkFWKuHl4sxHi5Iy1ViCV9vAbsnMETYz6Xb6-RqKRVZF2M7B9CE1SSZafJT_FfvpdoL3wN8p-Vox7uVK6k1MBCdab-l-J6YgQoRjsLkN0-kpbBH43r_yUe3rZ-8On2wkFEH9pnlFw3Hg8M8MHq8ljYBJlh8TZaaos9Jtnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=U7AUIl5a4bmv3vXca-y-S5QYWsM0kcCtAFetaxS-IGU0xzuknVEo6b_edviioc1AS5n0CY2Dqh30HMNZp0qj5BaviCBatGw5OT2cxANkFPqTe30-HYJl41I-Bu0OzC0XtTsjuio7CJY10ux_yUWdl4LY7lblzlcinRUK0RjvNEfHRn6LH5yYuwVGNeqJohlVjtPli5fDQmTC22iQHf8cI82ntSLDx6sJa0Q2HBtFmQi5nBJ-tKD7_x17RJF_lZjCT46JPJyjVFuDJmoEN0atiD5NyYuVnQR7w2SrxD2BXT9nvKZShCFn5sH8qQ4RhVuP8bxIA5XZLUZqVrCMzE1xkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=U7AUIl5a4bmv3vXca-y-S5QYWsM0kcCtAFetaxS-IGU0xzuknVEo6b_edviioc1AS5n0CY2Dqh30HMNZp0qj5BaviCBatGw5OT2cxANkFPqTe30-HYJl41I-Bu0OzC0XtTsjuio7CJY10ux_yUWdl4LY7lblzlcinRUK0RjvNEfHRn6LH5yYuwVGNeqJohlVjtPli5fDQmTC22iQHf8cI82ntSLDx6sJa0Q2HBtFmQi5nBJ-tKD7_x17RJF_lZjCT46JPJyjVFuDJmoEN0atiD5NyYuVnQR7w2SrxD2BXT9nvKZShCFn5sH8qQ4RhVuP8bxIA5XZLUZqVrCMzE1xkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIEmdfszYYt5IzaH7x-zkxzBUeC2cUi-t1Rjme4pciHNDu9_H2fj2MUDnoWoNWK9nHv9cKiq524_sBIRYAumAXAZ5E8sK1atGqatMELflHiJZ6MdHg3naXFT0FF8D7qOSZQRsWPQn1PF9YUGRxWLay8NJ1ZkNWWpL_HpIs5_b7UQ9o5YyXHe-BMzjJTRPOEnjUL-nQuyw06aBbQH93AIAfajc0XsVt5wTY_RbaWG3EbU3DexUJ__ZTF9fTSDm5HUzBW6LpCSPj-MTsxDnNCibjZNHni6qcMDG1110VZIE02fqD_p8_LVQRMr8BSTTb-ifsuSXQMYMWQPg_GNoz39MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=cEv_Xz_GWjz4nEqioRCkaSDisPmUV8d_Ljb1u0v3ogTcUrhrIU37TO1oI9i_0sPtRFqJuvcxI83LZ-Z0XhCVQrjIHBjn98-VqFEv9n1kJCDKn12aPXXdUBXVSh35c6XA_Om57UnL8GjiQEm1CDqdnT2QLDCRmF_366QNzVJU6TGcVmjyAmu1msyN5SNsP2FVI0DtWJqUdhbLxcEmVBvvaDC_t_H8lO3ujiCF_I_B5tvnXPf1HdxATnw0YzrCmVcf_IpnyeM_dz8WFPWujBcCLv_AIMdrlgfH8Ga8WlwqzQRutWFnnEuTs7GPx7fufXSnlmDzryhzP7EJ4B56rOlR8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=cEv_Xz_GWjz4nEqioRCkaSDisPmUV8d_Ljb1u0v3ogTcUrhrIU37TO1oI9i_0sPtRFqJuvcxI83LZ-Z0XhCVQrjIHBjn98-VqFEv9n1kJCDKn12aPXXdUBXVSh35c6XA_Om57UnL8GjiQEm1CDqdnT2QLDCRmF_366QNzVJU6TGcVmjyAmu1msyN5SNsP2FVI0DtWJqUdhbLxcEmVBvvaDC_t_H8lO3ujiCF_I_B5tvnXPf1HdxATnw0YzrCmVcf_IpnyeM_dz8WFPWujBcCLv_AIMdrlgfH8Ga8WlwqzQRutWFnnEuTs7GPx7fufXSnlmDzryhzP7EJ4B56rOlR8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=r3WLNESyXzx9bttuyIKdFpzZa479nhFObcbKuyYlRFYwA283RdjV4RkMOQ1Uc9NgpwtJx9Hq0pcFqOOm-ZAF3lLQ7X6eb4pbnLfJ9WKQhixckQTQFkTq39rZNC_iWIByynC2RhcoDaD7i2IYNr_BIBshg77EzOS2xFF9xKwGEuV2gIvJEars-xrJvMiiJymqBK12AHtb01oVSMb9vMe8j-zU4lsCWScr1B3vCaeM4_GtPIP6EF8lNHARpTCDyc12G2y8Xv_-UVyH-uEctQxsMQNxIWTJ4uKv0K-q5hqcYUdUxtxGv7R0xanRb_B51gk_QTCRd6C6DNk_pmPs4YNS4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=r3WLNESyXzx9bttuyIKdFpzZa479nhFObcbKuyYlRFYwA283RdjV4RkMOQ1Uc9NgpwtJx9Hq0pcFqOOm-ZAF3lLQ7X6eb4pbnLfJ9WKQhixckQTQFkTq39rZNC_iWIByynC2RhcoDaD7i2IYNr_BIBshg77EzOS2xFF9xKwGEuV2gIvJEars-xrJvMiiJymqBK12AHtb01oVSMb9vMe8j-zU4lsCWScr1B3vCaeM4_GtPIP6EF8lNHARpTCDyc12G2y8Xv_-UVyH-uEctQxsMQNxIWTJ4uKv0K-q5hqcYUdUxtxGv7R0xanRb_B51gk_QTCRd6C6DNk_pmPs4YNS4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcGMQKHtqxRPU3UuTSFd5mOdHcWAi3aPCmdfDbBJwTJOfwTWo3QiMO-MVbUQ7p16r9FZPc9f5aQKUDNnHMB5wkECll8Mje-l8-BjWUyQi8ThsKyz7iLv2_LPsk0Eb6eWx2US4T9LajQCvCkp5HnY6v7ftaPN5jmRC7dXQC-3fpdjXzaS9acKKH9cDCSCbkjNy83na7aYADgCjyjPN3GbGo10YVWdlTlMuMvzpnVoo9xThf8byUjxygpxpCVGTVed5ubjyACYjN9sWpcdeLKpajJSlRVAy96imAcjHjPvaNMIdm4bexVc8gincTj5M9c0tPZmDEZ9DHFiAUYUC8Mtrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbqptUCUnkcsS17SQsZzp-w97Jwh6C0zUi8NGM_JBsLKm30SYlT1ZteJdit0LRUuUdvdhnoORokiw8axKpYJ7-gFmPApmbSgDGEX1eTnrtavD9U65kHS86qJZaG09xZtoijB4RUQSnB8lmM36-ukpIR8KUHGv7hc6RYTlTgUsujDET9omqvyEoOb4ewYvLHm_VaLqd3yxvSqZJlConI2bQ0nKXy0pJnfRg4F0alacMcJp5o363oyZzQIgwDZuU_Is_axJjXbi0mDlJXe61UFIWfHNN0tKLjtKWEVcEpz5xr1GLEW4J9RDujnJ7ZKbHGNn4yLM67_eO0aNdW01ut-Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=N8unB-hkCf7tU3O5vTJ9IXB5TPuCpeqwSRfCyVNq981vRXUvglZ3jkd0zEnSyfNtHMA4h_kQaesn2eQYlI0wdIyMDu6FNqVrkRHYFxhLp5hsWEduRLEEGkeIhKdLEnQTMgqQgmL1KIN6upJ47TYtLVogCFjx4LdLqv2wRaeYaBIyKQ8O5iZyztChIOmp0ksPul3poK8SGE71nznav4Sf5TsiZ2ma8MzVmS2xzuL9uJv7q9y6Wr03xdCY75qEzPV-qaNkzasmiMrE05fDDSaYILkQvguocqqa5Qs-6wExJSqCDAvmtig9uc8KMronMVXaXSAy-QW_xfGTdfx9M0pUsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=N8unB-hkCf7tU3O5vTJ9IXB5TPuCpeqwSRfCyVNq981vRXUvglZ3jkd0zEnSyfNtHMA4h_kQaesn2eQYlI0wdIyMDu6FNqVrkRHYFxhLp5hsWEduRLEEGkeIhKdLEnQTMgqQgmL1KIN6upJ47TYtLVogCFjx4LdLqv2wRaeYaBIyKQ8O5iZyztChIOmp0ksPul3poK8SGE71nznav4Sf5TsiZ2ma8MzVmS2xzuL9uJv7q9y6Wr03xdCY75qEzPV-qaNkzasmiMrE05fDDSaYILkQvguocqqa5Qs-6wExJSqCDAvmtig9uc8KMronMVXaXSAy-QW_xfGTdfx9M0pUsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKC4Vgm2h5TObkMp7RgsVMAaSBwDW-HL8K-2_KEIHBvrIAn-o75AABbwpbMGR1xBOeip3Pe3cDQIGbmJ3b5NztBDOJ7TMHLZfEjSlSYlZJ9GXvaVkh45r7XuKEoKDek1wQEor88rPBDLJGUTFcObdD16cpZz2mAQf6E2DHQoIr4xJ_cCekVDOskBuqccKjVJARnb8XGFnhjgNtKAreSuTY23cb3aaKFPxwSg1jCrrJAA4K8QM1OsmOS-WR3uZqLnzxCxRuH_DCmkBjmFUTqpszkZGPeIDd0WbfdJXQXp1QGt2K3GkafQePKM8wfkaHjnYjXAzRv1rC7clMYlyn8mcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWy8Fbm8tiyd9Ieu_yyEwUPHhX-ta3I9gXrl_6r8405N_ROFZPBB8UHeEMmMpI4p8KDF_KBwuuXzj_NlYvChtNxNp1C9vLk8XK1vlnLEurGhQCyMoVn6NQ_f-vmkH12uhy9EGsT6HUBAvkP3Jw7G3BEBy0b-7qhPN5_HDEXuwsV4hOYikDGB5F0qhGK2J7ctsYTsMpT2AUHrL3kwgrD1uKlWYR58l6ECD9YGt44nlRF-kjV33UgqUD_aqawUSI_JoilziSwXasgMwuCFjiObCBWxnz_G1TH7M0sUMP-y3S1hqraTq3QeC3ZLQ7mnhPkLkVrP6bswbqE9oHijC0ETPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0le8ZkyBzo6dlb952ElTaiAbbKiAquMw88tYtp5peFC32xIUju8wzbX7KDMn7YnB-_Wi_uNHOX5--oG-NPp4VM22BXfm0e4l0YI8Up35NEn8NDQo3YmDO_n8WywD18L9tmxzlbTAy23mfLqMuqmEbBhJesAHifarqqVmwHjXncQQrqWrs-sQUNgDqk7XvSNywSYMnBwL0mxW7yKNerY3Xgpc65sreaniO7ZJxf2J8g5yAJwpdZRZIirmgJA9DQ_5aS6hVDFhxLJny_E-scPs7sizFbzIwed-mKq0z8-IK1-sof7EXp-uX3UwK12lzLASD3KPg_XwzxUNo9DDstNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=aFGDUjQUpJJnket-5QQRK75vMizqSvaYxTCGDTlbXFaPIDxSlnKOv5nL_vR6wD8XYAPyY9TR4bk4MH3sxpgj-SZNmizB9nOcjBnLWt0QvDcsDf15jKXERBuz9-nc2pZyKM-gnKlNWl3BwwpiD1O4F3K17x3eVTP3CdTg3bC4xDt-FkEqpViN90wEA9Am1b2-OOp2AmKIpn2lhS4VA190cHvf2DaD9j7a7vPPk0aYHLc636sWpJie4dnP-yzN0cScn67CZZrGWqAXoLldTjQSQ2SFmxSLx8lQpi-QtrOBVOMFI8N67Y5lyMITgPo_8R1mjDJCIsUfMfMsemlDNva6TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=aFGDUjQUpJJnket-5QQRK75vMizqSvaYxTCGDTlbXFaPIDxSlnKOv5nL_vR6wD8XYAPyY9TR4bk4MH3sxpgj-SZNmizB9nOcjBnLWt0QvDcsDf15jKXERBuz9-nc2pZyKM-gnKlNWl3BwwpiD1O4F3K17x3eVTP3CdTg3bC4xDt-FkEqpViN90wEA9Am1b2-OOp2AmKIpn2lhS4VA190cHvf2DaD9j7a7vPPk0aYHLc636sWpJie4dnP-yzN0cScn67CZZrGWqAXoLldTjQSQ2SFmxSLx8lQpi-QtrOBVOMFI8N67Y5lyMITgPo_8R1mjDJCIsUfMfMsemlDNva6TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Ygt0c2zCRTDahNHX44_Kj43BFWLK8QnUdAkrt1Fvpnujph3W5uRJ1RZ94ruoeIaF2t3dhV4bkiL1gubNyZ7Ik7r3HrFMDM0XpL9G3EQliX8vzutu2-ctfiriW4KmuSHEr914cInXmZTEuWbIctpjOWYyUXDaYHXGc15lT13up_sHYC9rrHQ1ZfGDFRCS7egGJ7dVv2-W6RXKBcZAyNGiBU3eu_Ck8Q8UOCED5W7Ple9fW-SK2ShJZsxiKfHLZBSYD70N7aBFlWPLc7Vunb-e7XT0ocSSxjXST2-_Mkcye1HPzDrmVbLG47x1HkgLrbDYN2T4cH2CXNf1RdVjC75pTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Ygt0c2zCRTDahNHX44_Kj43BFWLK8QnUdAkrt1Fvpnujph3W5uRJ1RZ94ruoeIaF2t3dhV4bkiL1gubNyZ7Ik7r3HrFMDM0XpL9G3EQliX8vzutu2-ctfiriW4KmuSHEr914cInXmZTEuWbIctpjOWYyUXDaYHXGc15lT13up_sHYC9rrHQ1ZfGDFRCS7egGJ7dVv2-W6RXKBcZAyNGiBU3eu_Ck8Q8UOCED5W7Ple9fW-SK2ShJZsxiKfHLZBSYD70N7aBFlWPLc7Vunb-e7XT0ocSSxjXST2-_Mkcye1HPzDrmVbLG47x1HkgLrbDYN2T4cH2CXNf1RdVjC75pTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=OIZoA4hsQ81zWHVONsXMH3F6ZWcLE2r482hAgTWCHJqdqHF24rjtslu9Z8TRSszsXv_EPnvO8jXktnT5BioGkOW1VGfNfuFOznjbhH_AZIPH9c80wHPgJCLjLbL3Iax_coz2_ippKcpd0jwlCzC1veBTESq_O86CJBnN8wi946p83_Dkg1f_HKKrirIGtzQ49kjg_gBiKjXFAXjGra6tAG4ElxwjQTy-aMtIdzzaXWuVBxKoly-JA8r07TRGSwZFTSevG6FabhekyAU9bZH-O9l24s_YJy7U-b94P4ILEdkKxq6TrITzgUf1TTEIu5R0G4iwon09OCw8OfboKgOa258W8loFdJPabGUCsMaXAx2wduh3g7VIOxpjNclOgo__mxBy4oyQjGSKOsbecGcJZx7wE0F-q231Au7Srj0rChbQJR3iQn7B0H4wweqvhSjSXZkV9FuF8HQ5wh9-L7EsGj_oahUv2i4N6EAzXB8wkf3uRvErblGJL64VsC-16aX1yCG_8XwgBJBMhZx_5o8WOxRaCXRhMYliPRmAZOJw7olTFxyAHM8LWiKzCOhh6H0JBEQ-inDlKGoQU53Wf2bp7SOGkJa4pPQKybo_63x-PwERcOvs9cxCEhGdt524ydM7qaFdASMSBSYS3tFmjGWUdlOsayUuGzDW-Azeow9J6CE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=OIZoA4hsQ81zWHVONsXMH3F6ZWcLE2r482hAgTWCHJqdqHF24rjtslu9Z8TRSszsXv_EPnvO8jXktnT5BioGkOW1VGfNfuFOznjbhH_AZIPH9c80wHPgJCLjLbL3Iax_coz2_ippKcpd0jwlCzC1veBTESq_O86CJBnN8wi946p83_Dkg1f_HKKrirIGtzQ49kjg_gBiKjXFAXjGra6tAG4ElxwjQTy-aMtIdzzaXWuVBxKoly-JA8r07TRGSwZFTSevG6FabhekyAU9bZH-O9l24s_YJy7U-b94P4ILEdkKxq6TrITzgUf1TTEIu5R0G4iwon09OCw8OfboKgOa258W8loFdJPabGUCsMaXAx2wduh3g7VIOxpjNclOgo__mxBy4oyQjGSKOsbecGcJZx7wE0F-q231Au7Srj0rChbQJR3iQn7B0H4wweqvhSjSXZkV9FuF8HQ5wh9-L7EsGj_oahUv2i4N6EAzXB8wkf3uRvErblGJL64VsC-16aX1yCG_8XwgBJBMhZx_5o8WOxRaCXRhMYliPRmAZOJw7olTFxyAHM8LWiKzCOhh6H0JBEQ-inDlKGoQU53Wf2bp7SOGkJa4pPQKybo_63x-PwERcOvs9cxCEhGdt524ydM7qaFdASMSBSYS3tFmjGWUdlOsayUuGzDW-Azeow9J6CE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=YXmEm-_DKAawHZRG6ogOo4ZkGm2tO1k0Osvv9aLFnG23gJk_hjpw-EWZxysd6JzKjKxm1yrckeLYFhTbeWs1Imgtd4MAusbPzdcmR0bcdEAdpBmCQ1AH4idSCZr6JGaH_odc4CPNl8CdsW17FEglEchdBLOkZw0vD_v-Kku7JygFDCNFicXprLbtRcppCyMrt64S5m8QW9RtQH9y3J0H2XL-nspXcoua2windgjkGw_9cCYfrHl_HrPsz2mj4YVPRp7jNdDN5_u6WD58uwa_Qi5rKmxCQ2J0nVDpncDx3jmjLSvsb6eO6ZYaf8uvIhsTq4DKVKe_BYUM7iMUQLkZ2pHpx2DXg5z0lxHlwT9lgBFdMHGY1AFmPP7CZPjF6jQvRs6oWYlACkp3SdFc-fCnqFce8eAjkI2fRrXKPQyoDQVEbOMzk6zkonDuhOMUZIYbDVPQ_dgT3ypjvTKvBowA5D91N5ga6cakumOrQrnIa7FD26J--WqfKRKxQxIE6KKscv151wpro8lvf76O-dJuIso4vZ7BO3q3frMpqOjqNnUGEa3R46geE4rYcFiIx2qREtMCI6zvmQGKIzYDTulUGod16JhzMe-ONgk5VopEZfNVD8OnwH8YLfToSgSCuWrZdnyPw9PlKGZghYhEyYA_9qHZmJeW0x9ezPRXitHCo0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=YXmEm-_DKAawHZRG6ogOo4ZkGm2tO1k0Osvv9aLFnG23gJk_hjpw-EWZxysd6JzKjKxm1yrckeLYFhTbeWs1Imgtd4MAusbPzdcmR0bcdEAdpBmCQ1AH4idSCZr6JGaH_odc4CPNl8CdsW17FEglEchdBLOkZw0vD_v-Kku7JygFDCNFicXprLbtRcppCyMrt64S5m8QW9RtQH9y3J0H2XL-nspXcoua2windgjkGw_9cCYfrHl_HrPsz2mj4YVPRp7jNdDN5_u6WD58uwa_Qi5rKmxCQ2J0nVDpncDx3jmjLSvsb6eO6ZYaf8uvIhsTq4DKVKe_BYUM7iMUQLkZ2pHpx2DXg5z0lxHlwT9lgBFdMHGY1AFmPP7CZPjF6jQvRs6oWYlACkp3SdFc-fCnqFce8eAjkI2fRrXKPQyoDQVEbOMzk6zkonDuhOMUZIYbDVPQ_dgT3ypjvTKvBowA5D91N5ga6cakumOrQrnIa7FD26J--WqfKRKxQxIE6KKscv151wpro8lvf76O-dJuIso4vZ7BO3q3frMpqOjqNnUGEa3R46geE4rYcFiIx2qREtMCI6zvmQGKIzYDTulUGod16JhzMe-ONgk5VopEZfNVD8OnwH8YLfToSgSCuWrZdnyPw9PlKGZghYhEyYA_9qHZmJeW0x9ezPRXitHCo0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=F3n-8ILWZ91V6PFhotrwJiDY7EzIGMv4Gp2RQ2DxR3q01e5vl17lUbrzRMT08AvQILzrBDXUzAs70myi2wV24OMpSsLwup1JxT-Yd1GlW0s0zkJ3Q-M-KR48EOb_9Jz93S8Fj6VYV_n1jV0irYG5L7ZHqXLLFECzASAlhn-LTJYbltudmzFaKNEz76fN4D3j4BiX6aQfKTmFYqDLcFqEb9VFMYofiDgAsg5ffVWx8UtPhO_3aSd9KAPL8EbG5ulp-dX9dvKL2qZULEMKVai8llODLQmeMTTE0HY5Omh_wICn01jkpFSzw7W19kBKP2Y844uoAzCzjf3pel-I8oTC8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=F3n-8ILWZ91V6PFhotrwJiDY7EzIGMv4Gp2RQ2DxR3q01e5vl17lUbrzRMT08AvQILzrBDXUzAs70myi2wV24OMpSsLwup1JxT-Yd1GlW0s0zkJ3Q-M-KR48EOb_9Jz93S8Fj6VYV_n1jV0irYG5L7ZHqXLLFECzASAlhn-LTJYbltudmzFaKNEz76fN4D3j4BiX6aQfKTmFYqDLcFqEb9VFMYofiDgAsg5ffVWx8UtPhO_3aSd9KAPL8EbG5ulp-dX9dvKL2qZULEMKVai8llODLQmeMTTE0HY5Omh_wICn01jkpFSzw7W19kBKP2Y844uoAzCzjf3pel-I8oTC8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/om2e6Tw1YQs1ZJAJTqUXvroVaa5TNlkzvTMromo8PeowABQP-4Gqst-MNpL8viPLOBbIJTWPyB7eHcC1OQa8aKwE5cQCd2XvqUAMHN_4hwLCboE9DLKNoyxv0D2CbxnL1Ftx1SdsELNfTdt7kayo9sA03ILo-b3Y1KTMV08dxIG-5gDWv6rugT9aSqg_ZnN91YVlgsj-7E5eT7eHD8eY5_HHJSAm_Fd76G872ODJJeFzY7s3mx36X4rfTq-knd9Hw2Y6wkIqPbECcsEsH2yApbPZXciEhjBayhJpTpRTE8nHz2Iv43z6WQ9LnvM_5gSZ2I-HxNerCtJHRMkxA3vXcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=fFKWyYnTxh4nFEzHBWigjDhVbR6t4k1Mk_FRloZk4TuZUNzlk7fOaDsOmpmNSc7Ns8IZPFzH0l1Hv-EeiW00MAleV4LRZuyLBpGIPx_PoVQ5dpjee0-Rijfe_xq_d3L-ChG6P6taBpOvd6w0IAfNEw2q0o9htF1WKUqSCnq7Dbj5X4N1bjYwD9Zb1ewKOZN4Ux4o3Ju8R-gAV6igv-H9riu_y4ZpNsxE3ab3dYFvfFbpTyn1_PETSZR-yunh4fSyShkgyDD4ZQ1vytvpdqhVGucoYpotnQ5IAam9RuKESb4Nq0E5bR-WewNdoDqCN8y5fn1143SKdLi3p6ekdkdmaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=fFKWyYnTxh4nFEzHBWigjDhVbR6t4k1Mk_FRloZk4TuZUNzlk7fOaDsOmpmNSc7Ns8IZPFzH0l1Hv-EeiW00MAleV4LRZuyLBpGIPx_PoVQ5dpjee0-Rijfe_xq_d3L-ChG6P6taBpOvd6w0IAfNEw2q0o9htF1WKUqSCnq7Dbj5X4N1bjYwD9Zb1ewKOZN4Ux4o3Ju8R-gAV6igv-H9riu_y4ZpNsxE3ab3dYFvfFbpTyn1_PETSZR-yunh4fSyShkgyDD4ZQ1vytvpdqhVGucoYpotnQ5IAam9RuKESb4Nq0E5bR-WewNdoDqCN8y5fn1143SKdLi3p6ekdkdmaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=fPNN4F4wcAGbOtpt9tjYKUSx7HbNwhZLlqYakMz9wvavGqPGqOHza9lIibKjkLAIQYG2lkigFQ7WXvvgf68LKLzCjfBGhior8brVhOFGQSURsQwFwwU81nyvfRoJkhSbK6d2dzlGYEEIyte2UIYSsVMO90prPV4t1cwCocnUAyXCi2mbjyfrzuPTH_ahmUlG2PfoAEi4GvPRKTN1eSDKPmimYS4RasiMbJDZUbuF8oFSETMQj0RaLDajxh0mtyFVwRVAeCwuvG99_gLl4DCLtOBAo7tAtzPgZo1Qvv01rITAU2uy5xSUkkUGzkIwoqMbZq1sz98NWTlw7qO8liYRPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=fPNN4F4wcAGbOtpt9tjYKUSx7HbNwhZLlqYakMz9wvavGqPGqOHza9lIibKjkLAIQYG2lkigFQ7WXvvgf68LKLzCjfBGhior8brVhOFGQSURsQwFwwU81nyvfRoJkhSbK6d2dzlGYEEIyte2UIYSsVMO90prPV4t1cwCocnUAyXCi2mbjyfrzuPTH_ahmUlG2PfoAEi4GvPRKTN1eSDKPmimYS4RasiMbJDZUbuF8oFSETMQj0RaLDajxh0mtyFVwRVAeCwuvG99_gLl4DCLtOBAo7tAtzPgZo1Qvv01rITAU2uy5xSUkkUGzkIwoqMbZq1sz98NWTlw7qO8liYRPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meBreuxLWRewVD1CFuaz3kfzZETR2QujTqzTBB6mw2DaWZtsaxcq16OkEHspLchKkSuFry44r-23Cb9ZLNQDMDMFEDnZir___fMs8f4ttbqAAnSe99FvBHjD0C5pGXbXmmFUQP9dj-QYm46ihB07hqwktJmDy8SmIMC_iLt4hfZwUH9fPhe0ke8w8GRcdv4noX-K_byh7rRsfezEN3NDsf8XCbsWiMlJSCx2U1XtSgLyONbwafTwdpB5fu1N6kL2lW7GzSZhCNN9E1yiNhjlty51_aW3SNraIIk_oB0CKKGwO_HteEpt9VYzjI3k3kuhudrPI8-xUu3GI9Vy7lqDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCeit3IAE-2WGGTkAPj3vl5dUX0gx3eE_0JCcaot0-JhXyM2hsghYMZ-8qtQBQkZK1_0MEtZleRp47dEZMtr1uOqMJcwEFaPxl5Ojm1Ng5p5t7AAlmbQo0GkEp_ctC8osoVZ0MT2dlojkS2KzcaCrhlIVGrHcotjEX44pm_mXg9OlKWtbJk9K1wh4m9AZjJ4hQwm6P7hhoqoq71fPcou2CgSIVGY-g-damF_MWFNvmevYzYJ7Jc5xKORx5km6Qsuw2TdEe7AehNjC2oiKW_oVqF8WB64fWnGpwt6wFLDyBvQtE75XmXU_fxcxvnnMaDWpvmbzRhaGs0HjdwEVB5GGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6Og5z7UJmqvHNpO48Hm_JYvya-6Rd8eRrMlcaqnzbKubfOMu5q4_2d2LPn4Dejp0XJzAw18-1r4O0kX_Qi69ki7aRoUjVPSpbfPLLrE77Sh0nXI9yw8WbbTSWBv4eNdPcB5iGj_2knoMNvKpHhBepPI2G5KmWumhJq9S6Y4P9ixxp5m7VsPNBPmS2XCIHPWYDuSBsC6j5PhvhWpurgQwur_ah8nplrMiV2h28GCT-mHD3fbs4MVt2LPOuae5VWe-FI9Tduovd6v-weIQTk2U_pK2DXHDrSL6c67W2Y3dDR9F-l9ViJFwCBjNDZyWUvH04ovPI47TGHHXaJ2Di9vkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaX1n-2HJzzHHRD_bIk8OSDW25daGJbTjWp8JFbHWp3OFTAt5Xugc8FjTmKzTHc-hRQTYo4MCoTGCqGUaj05IBdt6NjsEhrfbhp1pCu00IgnUq79aQuU4j3RpNZ4rdx9p_9ZFD_F1Isyad7bsvwBYPvuR_aE9fuPvfF4zZX3b6ClPO44_dkbl4-BA2ZL9nbBZXWEYTbrXMDystVAbWehEaTp4WsY_dnZKuQ18s2ZyAzoc9Fz9RoAL3ze9pn8j34W-y4yrBR4Fiy_I1X5pIKeeTirgAZwzbJjoAaK3ukl3Fipoyro9G9P__RshzShVq2ZFk0HCInbkJ_hppyIybqtaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8NtoF_N6kDTN3EeMmA6dgE5fA278ow2c9q0_MEPa94Ml_QpdqE2UPE7ZwL9J53PLo9Zz3UKt3L-SwTIgtCD8D3SsVvdlQjnoV__u7x9z4WXHb1CbW572iHUjN53GBKD634KS6p2SgB64eI2LlLx2E_qJh-MHaSqMGumAtdAby-pogcW4oExRFBDG69qEz4lT683c7ATz6AKErzZ6ZyTfd8hXnl6UbUu6eADP_s2zSubezQzZrwu-Hb4MElsfMaKCNbfClLznp6x8a62iipMp3wlu2CVR45iLTuxc6K5BPWHDy52GhTFXxKo42XwsfKQLss3xSabHbzpM1nu5D_86Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CihMifd9o5OOiHkRGNjW1fb_uESrdNqVk8WoBMhditraw_VOPidjXL3BJ9nFuQBIgteuq63oITtdg1_YVNlO7oCTPO3VeUQturOzPo5m6xEYAipBDTNtSbEbi3_jeISs5ut-wa2OISFdeIvMgg30qEWvsTVjJHZ744OfwAI3pLAnfsvIuMjxDCF1PnfJWWpH1ce5KhqsicO8mgM9b6nOulGzssDQFr1cIXg7FMOETCjjtZX5rj1qLv6CDZ5ElsApxrrFIPS-wulMXYnDyMA3gwcWHLLZMkBxsdrY8f0rSx1G9qCP2HltAszKUOLfSue_DSZIEq9KhOG-hrdRmefWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2QNQlshSRaM7XeE2dEXz3hIMC2Cczek83B0xfC6yXmsa-LvTWnoM28kk8ykoCRfaxdjniCf53cOJTUB8Mg5g_N7RfjnO0cmI2AMTFf7E_2oHg7w3Ascm4iuElgapRR80WJ1POij9RbjcyUwxpN2kAQInoRAFjiFEyI-EAjC1Zc8XHHR4XheUKYMxgU3waQuloxXi6FamF34KixQvXL4r5ozYuOIgJhu0rCVJgidKYp_VmXRR2n5NWrD2Z1ke8pCBLO0cMnriC2tZjWNXJ3n9cTUgQoPhXKIZwhsSw49kHKegubkbI5cx2jGwrydwEImjpXLNLDen5m9CaqwPZP8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jcqwB_AmD9vE4KpASLStNpx2_6obdKO7lNr_orxl69E7PdeN1Qj7dhFXH3PzNo16rXPoLx-1rUhNIBZq6lr4V47dLUOu0bZSbh8yyc68x4JLSskpApBnG4n-14mSi6iQiScO-ET5c6D-t8NcaOQ9scVSTb0QtGV45q3LkF0jO_zoocRNCgt4IStzLOvwnL7nMBr4FEans6-X7_SWmnvOhOJAn-ZvsH3Qzo4QNCtu0BwQCnH6Bhb8KPalHLae-y3EkZONyLgA9gCMhpY-cvJbl30J3Bf-5VyYZnXaNRCrhkBaQlAbWEY3CD2fMYBviYhZ_zwePkACm-wkMhWfYbWuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KwM7iCkNhxK2m1Al530uHopMX-xa8F5u0BKJ1nRcIms3VHiJZQqzHqgzGc_KpMnFcQSb30lopYY1ROa1eDZhB_4CDwui41AkpL9wEn-5O7d_im293_PIsr3pMzwJa5bfuBO1d6KGtuOZI5-GpyCJd8LtCGeBpF_XQc_L2QtzIwHmSM9CInKJNkld3i1m-BM3QG--RafRQOdT5XW7K00nxFuVI08a0o3JURgpD5mQM8zlqOQ0CUrEWwMx0aqwtr2szw8t1uCagSOXq-3sldYwJM634DPkcG6QnR4Irbrlta8G0mL6aRbV8vX3JXYzyZXZNe9WHtZ41WLM86gLTSPIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SOP1vDknDMUmpQLUWR4Qg8x8AHffJe064n97gO5LvPC9Zo9Nn2TFtebclHNakwi-O1b-T1iENUTaQptyGeyNc4Qjbxos6Gni3sZTFr3y0o2Rag6uWlfCshKhO8Gv_qXoIYmwMHfa1SC4PZ_xkYPi0waE4ebai6l3JrKniuNkwIkR9oECZvqYQMhytaKVuXNCZvDmeV93KjfQYYnG-OirwjRzyl7QaNPMpsd8SawjpTev0HwRujPKAFzrcfw7H-598rJtY34H_uuucCmbKCR4Tem9AxYVhlEuZCZUXZxP_9TuvW0mzg79hMs4bg_p37c2vxIg2l_FDeMIXQwLEtwThA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=XxU6wei_9APoABIEV3z09-0b3ggffQcfFHjvcd4vH9Y_bXljOzEKGr6RDIs91oWJ7oTtOjHK56pZQd_hTtQq57ykdEwV-EgoCkOglXOjDbMMEe6v7gPx0PdyiihxElnahYPh8arl9F_EnsGEmSNnpZNb2QIzOzBDSHkHsKMdRuj71WsSbSGbU09spkZcPRopy52XI7QJLaIlkJze12vSxpxq-A_JmahTvmWXKd-utk497RJrOtSKOqS7o-UkD6fYsUIxd3iJAiyMkJlRTzMfoqHUFLn3_pdKd0msVKC-05wOA9kr-4DKBBnowkjwL_RXu8i7Ox2MiwnHfPxEojyWfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=XxU6wei_9APoABIEV3z09-0b3ggffQcfFHjvcd4vH9Y_bXljOzEKGr6RDIs91oWJ7oTtOjHK56pZQd_hTtQq57ykdEwV-EgoCkOglXOjDbMMEe6v7gPx0PdyiihxElnahYPh8arl9F_EnsGEmSNnpZNb2QIzOzBDSHkHsKMdRuj71WsSbSGbU09spkZcPRopy52XI7QJLaIlkJze12vSxpxq-A_JmahTvmWXKd-utk497RJrOtSKOqS7o-UkD6fYsUIxd3iJAiyMkJlRTzMfoqHUFLn3_pdKd0msVKC-05wOA9kr-4DKBBnowkjwL_RXu8i7Ox2MiwnHfPxEojyWfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKuTDJb-ywbIvnfwtHzpNwkSgyYHiexKAuBl31D8ytm47PhviIEJgdPP6dheZXo5__x6Tc64Uo6cLoTnWpGVAA9G3HXkeqwA5LgvQXD20_Vj_K8NpoMOIeDXiWBuPcUmZ8Sspbg_2hKGDsNXtJDi54DltYPlaAv6432ePYfutvHMLcsfz13kmlsM_ysQFXCutMHnt4vUJJYRYIaOhkkmm_Q1VeXGr_tR4LLmYt1ASAcHVxJnnsTwrBB37Fq4K4UR97NQcM66WcpzRBjbc5FcktuhLI1CE6u6p-YkPBtgjZ6In0oCY0pFYT9lr73WT53w5L7anM560sb6mREBcDFvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAW_J7Qn5PqaVyb2tr0JarWUWHR_MoLkAtG4O0LhBPIUmOJjcdjGPnFOqaHXqvCe5xsFtZkCxO7sCHEl9-Z1Ke5zUt6mM91Gs_GvBuZvpskpK-wZZ4EsBYKNKHwbNtKFYnFKEG6seKUT28_7pADGO-JVUZD_JdXlunZLQd9n-1cYVuKCaUsXanhja85D-l_bfgOTJDsA-pFAOopLepvKbeQigS6kE3UyUgo7EH92pxrzaD4C1lgTZ6WINQl_MjoUZnGi5JAATJo3jSyErd8A5gT0e0TUZ1R-IXQmPAi_uujJFK3ZqQiJCaLUEBc0YcFsnSd8GeKMSp5WVG_sfA2--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=g7sSlB1QesXKSuXSmPqIv2aN7rbZV8Cyjy-gsRcki7TdXJYLVdAU9Py0t2MYffZM7WyK3a6a4lQ3uDU33-g2vlrahELVtZw1ZNs1c6RBfxSSgEDofGYRBB5fOWEi81PJnQjJEVRMfHWnxRp-AKoXZZusDoUpmoeAW9Q87f9-xKj8KGo4yZXoKRK9Q-HOVZkbBbICt12JNd-yrEsjt7CIQJL-4xlUtU8Xwr-wPID0z56AY30r4rzGat0K7U6704zPBLpvmUjp_n-wwgR38_2V593E-PR9qgMfW3YgwRGCmZQhl_8j0Mvsi3ezpcjN18khE8EZXeYvBIUITAvHDQ3uGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=g7sSlB1QesXKSuXSmPqIv2aN7rbZV8Cyjy-gsRcki7TdXJYLVdAU9Py0t2MYffZM7WyK3a6a4lQ3uDU33-g2vlrahELVtZw1ZNs1c6RBfxSSgEDofGYRBB5fOWEi81PJnQjJEVRMfHWnxRp-AKoXZZusDoUpmoeAW9Q87f9-xKj8KGo4yZXoKRK9Q-HOVZkbBbICt12JNd-yrEsjt7CIQJL-4xlUtU8Xwr-wPID0z56AY30r4rzGat0K7U6704zPBLpvmUjp_n-wwgR38_2V593E-PR9qgMfW3YgwRGCmZQhl_8j0Mvsi3ezpcjN18khE8EZXeYvBIUITAvHDQ3uGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=dH5Royyy_T-d3UN7hSZFeow_fKp4rGrFp4ZKD2HHbpvKEpCbN25I7x3D1M9-fHhbB_iMC_9vVCX_ErymVhIYw_RTlne372h9pXs2UDCZDPjN7X8ExszcNNrqDHDJ7DspzTXefEo4vk8TPs2hFDY8UDOHqeqLsWZBRq9fG_iCFs0IW2TdwLotAKupeAlOxSO0C0leqti9raMr8A18bo1md9ziYXZGH2yZoCmotLX2r0_yFKqK4vVYh8gKmecjQ3lw145ad2d574dMeG8DExu2-ENYgtxTAcEIZDrB3e_Z_HLThyPSWQBjgrFXHFSa9NpV5RlE1m3dNrSapeD7wQ0LTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=dH5Royyy_T-d3UN7hSZFeow_fKp4rGrFp4ZKD2HHbpvKEpCbN25I7x3D1M9-fHhbB_iMC_9vVCX_ErymVhIYw_RTlne372h9pXs2UDCZDPjN7X8ExszcNNrqDHDJ7DspzTXefEo4vk8TPs2hFDY8UDOHqeqLsWZBRq9fG_iCFs0IW2TdwLotAKupeAlOxSO0C0leqti9raMr8A18bo1md9ziYXZGH2yZoCmotLX2r0_yFKqK4vVYh8gKmecjQ3lw145ad2d574dMeG8DExu2-ENYgtxTAcEIZDrB3e_Z_HLThyPSWQBjgrFXHFSa9NpV5RlE1m3dNrSapeD7wQ0LTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
