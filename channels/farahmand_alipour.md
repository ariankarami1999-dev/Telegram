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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 19:06:26</div>
<hr>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbiOMZLg7HXOMepqETHT7-HKC0SRMuzv1S5xurSETeVQlFnjGx8Wl1yKmDr1PS0HaAHGdEkcGDDGjZTxfc_ZBod-xRmyLL9ldU0bfgwU-3Tag5r3p3rNZ3K4JgfDlliLb0oLxLiz4fcYu81HiHDrLUcLSGcrQe5VZkQwaEOSnu6NEdIzTC5SACjWvWsUAmr95a_yUOg19M-4_o4pZnXWf8Q0cm7nCPpRmKTrdiSvWfVbNlz-pnfHBxE5qjzHDN_vzBqAgY4456K3I7nbH9N95gfFUQpkDGO07whk6_36OLcXTzRjg2dLT2jFWUKBsogSsNmcvFfi2X610rU3DFR_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTqVQFinp70oz5TRHA5W7JpxzXlz74iqygmxNnv2ReML2BVuUsNEzpAHBhy83RPDf8ze2YQ95cTAjOlvVya1cfyZWZtW1Igbk6_tOEZKu8vQ5RqQp_Ndb4qN5Pa22z7SaXgzwck0eaZH_t5Cx7RludIRZTQtvm8zEp_g0vagqP3WVN-dfnqp6OsAhQA-729j2m4oagCiKkzMfGJyG9cDAL1xTznWPdMgGdTbXuGf4opboTSQ0FNVBFwboIh8iJTIp2xKW3zqpVKr5BmhdoOG9dXk5Rd0KD6BgWQ4C21Plmr2BdV2Cn4oiie9UBlY6U3KIF2QRCsv8g-N1VMaxDvV_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjbkYuqHCX8tvk8FH738oH6LbiW0LBtTtr51yVpVZLz_IUafjqyAmhutjet4C8pXhfMEKXQ3fzUZpI46h1Lr98uixjbp9vEAbYLBZMIzDnFPUTsQaRr36JlyTJ5JzG09hpJJvhwdDc0duJSFunKhvqLDArL3c9idpHajMBVIZ9heLshXp1hBxXpGnfn8eFzUA_jbM_KKJ2nIV2oe-E5ml3PL7uYj2p5QDVRAVb868m7gnyGMVDqEndNejC-fpQm-tnQ75DCKzizXsXmrjMywi_pIEJ8f4-vGDm2A_PRKP_kw9FuaqbjDC9FJXQqDsYYDNSselLkHNpUozWE01bf5Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dovRQ51uMJ_6XC0zS0KZqgP5RIEsU99ZpGLHCjOJMoutrx0Wno5_iphohgLzNi3GHxcC8z-U4c7kVDAFPxavUZDirgdW3NhIEp4UHc6QeilCnu7tr6qlnxydLO8YX9sCO5fGVYxNLtbWtYzrrcIRCmRtSyLSXb2N7Sq2WGzcMmzaZ41sdHx-vYpZW9e7Ffd7YO6ItdLmhEVti8Gotz1TUlEm8NcQIZm4er9Fss9tlfqG_uojnwTKaZyet4Zns129IFHu6Wdo7FkTRxjsHzMT2VOWkKfVFCHT7So7tB24fJsWEZlAJ-u2EYAIAuAM3nlZirrFDJ1BTgcVr1TYylZy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpWU3az-puMY29kjql033-BtFnhFoFaiI189f2dOd_fpoalCCtL1pPe8VutJuH0Pp4-DYRqt-Jpa_zUqIQnVi-aJmTVPEnFOfVa9_KSDH1ggjY4XHqkGnsg4ADK2BKcm0Rtx68aFlp8uArTzY7S0vLx4fnyMHjXg7RO2LACYhPmIXj6oOsew63uAkzGLjw0Fk8qqhNyqSbymPzoNM2RSrM-CqkbSmSMGf3WX0u5pzw0m98Tkdo1qOBWK3os0HguLUhIF6v_fsey4UdhaM3k9dw1mmvNC-O5g8RwZXDNp6c3oIDxexQ-FiDm6zvmvX0OhYzUYfftMHf3ft6F0nUGxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGl6ps5jUexumby6Oy3QJLPFLmO-1bUSpLaZ5p2Kpx1R4cCztSCuocfYcaUE-pb5UJQ7tinOHzTRHNFHdwpAghm8tHMrvqJtmZH2Xd_g2SeVEIab6nZuzEKa7xNu9JYr1Ip1gzw99Ud-JCxvvz26o1JYLhWF7NZnqMiota73Cc52l0vlrOmQ6ZAFR-NIT_7QX1LQ4iGK6HMYzn2f0qanbCQpyyToe0RuaAOxunrVctBZSmEZlSc9yVp8BqW8EK8b_VwyC70dAb1QkNi-IDn4V7K21KNpXLLJrxKQQbwsCw0nQirJXECx9fJh23wFThiK2lNF2_eIzAB5WOkTiDuw6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVhpqOmBsZr9xAKjNM1g0ZqWeifGk0jhJq8152zBZa1r_2qAhfOxuEnLNPRsAiUyQQZDFo495JohvZeWzGND11uzPoL1r72kE1dugopJMMtXpBtYVqxlqregbcSFay_ovH0p0HvlJ4sTEhldUa-NnNuTOGaUjFLuljQACqu0slY7-o0lRyoM7kwBzBEv_fi2xh6NC98_TK476519SkOW6Gk4p8zQTYg26bEpsNd_a64VF5FaSR3PZGmtwTYfJSACSK6IpyIgnWYkXK9zbr3ER4jzLGJQ22cz3Blx-hOaQHzmvpEMSdGWU9bt-48w_tHICriq1gcPGYNAuL6I7DGjsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4hpd0pt1w97u0bxsRUAtkhOrmQpDLeJZ2CNIIXWEC7Rw-CTXNX3-p4BZT0ZcJ2e4ypRuqShjRG7zxP-CUrGFZxBBW1ONpZIOGAtDnclfBSFtP_UUA-D8_fxMe_rRmzSXF89Vzwkf1TIoqwprkiahGAmb0LRmMFdgJxROhhej2UDnErAoegNomIQEbzx_PlGieR698sCXT40tHPk8C2sG6ky9bkhd8qWRw7KRwZDByR3eDCCVheZbovInxo2nkhYJxr2h9BHFxe8HWaQ3xR9NJiU6J9NYo6GKLVRmSwg1jYN8ZtZPMg1pl1oGVrQ8nu5YUF6gvwLh_TrJ08lVNeGoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=TctY-IV0-1hFvDMK62cSUweDLEwcimao2URJt3l8wHzObV9uCU_2vyBZfr3VxSdHLPDKnNUeyg0uYGqRHJSPMNSya47tevan50XHFPbAUYt3TWv96Gxp84G_442pkOniHnbADpkuSm_UYoWR58TRwTxep3r8Q1Bkb5kxWyNxGXFWp6TU3imqOvz_3HhBpJBimidcGl_MXsBjGKMjuD3eADRv4v_UJ3h0GDvJTzu-knFpFdfxyqXs2L6LRPq9VG7DNG-Tvb1oq2s39uhBXwetL2zaOdAnqxpefGdj_-LrjDmmQKOkQezl_7kKzA-jMdCW_NnIyJkGzjyf8VjwuXGv8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=TctY-IV0-1hFvDMK62cSUweDLEwcimao2URJt3l8wHzObV9uCU_2vyBZfr3VxSdHLPDKnNUeyg0uYGqRHJSPMNSya47tevan50XHFPbAUYt3TWv96Gxp84G_442pkOniHnbADpkuSm_UYoWR58TRwTxep3r8Q1Bkb5kxWyNxGXFWp6TU3imqOvz_3HhBpJBimidcGl_MXsBjGKMjuD3eADRv4v_UJ3h0GDvJTzu-knFpFdfxyqXs2L6LRPq9VG7DNG-Tvb1oq2s39uhBXwetL2zaOdAnqxpefGdj_-LrjDmmQKOkQezl_7kKzA-jMdCW_NnIyJkGzjyf8VjwuXGv8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duNqKVFbt5-96rCw4_gLXotKZ3mrgvHqUXqqpgz0Yin3rwrqQIobCJUOWjyv_C7b-t1LVcDEBow6MsCA5E-2ubbxAUEp5c1eZa1oRr1VfVy0bkUgzr6QajzNzXBjeKxlRKXQnbI-LaZ5gYQG2ScHzvnmHHDiuZzUNqVztXpDAnIl6oOZVXETuUIFVdsMyerpKOANAYr8dFOt00S8050VsE66iXb3STwx_mhokL9YqBkktBVTFNSFAFxQ4TI8yhAVbH1lsO9bmHOr3ONjsQ-VA-ge7BM_KIjbpkvo5YEHTDrrCTiJ2o7k9kde4eNOYqQm6dlWM66Slczl5mUCdbxiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuy5ZMny3aPS73F76Y7fDDSRQql2Fzd6UqzIMIMb6nLJvgsorQ2g4teU7ee4uK9M5vOPvIatcb02OIUhU9v5v-jEhXDs6oUabJTzZ922FcyDkYrbYwCCUSLFYEn5kxuqsyQIrnqUlQdlk5JOfUX4aIgJ5q0QmIGoHqRAHj_j7CEQD4RiZyre_LFgFElPiWZQvHQX--ZKDX2RlHYOVZepnc3_3aQAoZE9RGiphY4JGuYjcluIF7QBr4IlCrc2xOxQ3wDchb76YQ4PyxZgIYMBAfuw0be_qVK8haNxFUucMRzF3mJsjuX9KTKdtQ4GJZ3QBN5_0Tkanr4M-bh5x0tc7qVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuy5ZMny3aPS73F76Y7fDDSRQql2Fzd6UqzIMIMb6nLJvgsorQ2g4teU7ee4uK9M5vOPvIatcb02OIUhU9v5v-jEhXDs6oUabJTzZ922FcyDkYrbYwCCUSLFYEn5kxuqsyQIrnqUlQdlk5JOfUX4aIgJ5q0QmIGoHqRAHj_j7CEQD4RiZyre_LFgFElPiWZQvHQX--ZKDX2RlHYOVZepnc3_3aQAoZE9RGiphY4JGuYjcluIF7QBr4IlCrc2xOxQ3wDchb76YQ4PyxZgIYMBAfuw0be_qVK8haNxFUucMRzF3mJsjuX9KTKdtQ4GJZ3QBN5_0Tkanr4M-bh5x0tc7qVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=KC9N9t4PO9hchsNHCKimv7lHZrWyo3TJvtSDxUUtVB_aq9y1cO2-1JcVMlvxdHQvV6ELIUCQPF4fCzX_nKGDfbYc-QxJiZwR7e3_P9J3JiGruIhCOQfLDvsWM1qi0ne0u9V0cpKjbrbFQSN1cuaAhMUcQcsgzEmCqwtbOY-Glm03AW2kDXGEYDVVojtgDarp9iEE7DY66MwX8P1cUzFvI6NJn5mPPcKoiG9tzKqxhVYXAxUarkhSHQenUzn7qkIS3EYAmSDYxUNk5BPIa6MOZJwQzoFTfFOyaRDvF14DgRXT39xrIacUKOxtshTojQMTpLJ32EKWU-z1sAC7GMPcRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=KC9N9t4PO9hchsNHCKimv7lHZrWyo3TJvtSDxUUtVB_aq9y1cO2-1JcVMlvxdHQvV6ELIUCQPF4fCzX_nKGDfbYc-QxJiZwR7e3_P9J3JiGruIhCOQfLDvsWM1qi0ne0u9V0cpKjbrbFQSN1cuaAhMUcQcsgzEmCqwtbOY-Glm03AW2kDXGEYDVVojtgDarp9iEE7DY66MwX8P1cUzFvI6NJn5mPPcKoiG9tzKqxhVYXAxUarkhSHQenUzn7qkIS3EYAmSDYxUNk5BPIa6MOZJwQzoFTfFOyaRDvF14DgRXT39xrIacUKOxtshTojQMTpLJ32EKWU-z1sAC7GMPcRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=hf8Ore5wtEuatVp2SNV4EvDsJhG3PVHYDiZlwfYVu2sip5Eifzgi4cm64HWo4svzBYViDnJLWjl3Pcn0NT7NERVHdra3lTT0gyPOs5Mjlbezukyi-mD2LyMqwWn-Gmew2jqCsJLG2rlyQ7hCZZI185i8rNzzYI30qTFGIYH1p8FIvdww9Y6NB1IoKWrhdTRAokBenv7EEm-iZXO6ghwAmFNeHU63D3pHoZ7ONUft9ex0T5o_pdnvKPTLGsywKTlumqOhfPTfdKAPKs2ff3VaF4f7jWVX-D1miOeBXK3O81PRCIPirPTUVj0r9gujmpIm93wsbVxc2DhBrOMRdRv6t7mBnR96QKOMgorSx8VUXqcNL2T0S0uREhZBRVcpDu7d-G34Aossq2_ioXVZJsX_B-2W1or3jv7v9u1emdHlEp-5yzaoqPY0p2jiTUVCxgPKZJsJSVRAf8zd6ZO2OKFmMNDzCW9je42z8xPSUQ7FkSec2KAd3O5Q6qT3-FJOGRzDkCztc-xuojLwkriUEtsgic2Cj_1aty5L9158w-NB7neyaK4jLLb4RfEVetP2rTkzdhIS1BtuQ_A4Z280F7NzmRuta89UAB_hmMjeUxJdosxwPMoRRJQtdiNCIVdSzANf_yEC_7zs54g5W1VwnNQmlqgb1YyWkjwIcmWU29rGJu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=hf8Ore5wtEuatVp2SNV4EvDsJhG3PVHYDiZlwfYVu2sip5Eifzgi4cm64HWo4svzBYViDnJLWjl3Pcn0NT7NERVHdra3lTT0gyPOs5Mjlbezukyi-mD2LyMqwWn-Gmew2jqCsJLG2rlyQ7hCZZI185i8rNzzYI30qTFGIYH1p8FIvdww9Y6NB1IoKWrhdTRAokBenv7EEm-iZXO6ghwAmFNeHU63D3pHoZ7ONUft9ex0T5o_pdnvKPTLGsywKTlumqOhfPTfdKAPKs2ff3VaF4f7jWVX-D1miOeBXK3O81PRCIPirPTUVj0r9gujmpIm93wsbVxc2DhBrOMRdRv6t7mBnR96QKOMgorSx8VUXqcNL2T0S0uREhZBRVcpDu7d-G34Aossq2_ioXVZJsX_B-2W1or3jv7v9u1emdHlEp-5yzaoqPY0p2jiTUVCxgPKZJsJSVRAf8zd6ZO2OKFmMNDzCW9je42z8xPSUQ7FkSec2KAd3O5Q6qT3-FJOGRzDkCztc-xuojLwkriUEtsgic2Cj_1aty5L9158w-NB7neyaK4jLLb4RfEVetP2rTkzdhIS1BtuQ_A4Z280F7NzmRuta89UAB_hmMjeUxJdosxwPMoRRJQtdiNCIVdSzANf_yEC_7zs54g5W1VwnNQmlqgb1YyWkjwIcmWU29rGJu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=mWpcqP9ebwRZsx1h19FL4ajVBhGtqM7La8z0oM37pxqGROrjAwyyma3FYpUIOqrEKTB5tInT3dUuUFX17For4tNlS-cIdM_ZhdFJK5qcpiIBapYJeeG5f09Li-tAt9hP5d_PZl0AM-CeoznQ7N7G9u_RCS9D5nvI3P3v553-Qp_8srlfgoYs81U8Fz-DMnh7aXTBVTF3nfXpmWfYsP81KPK_9MP-ELb-RGjy7NhXhsECxwofUGeM5j4v6O55m-mfGntMf3GAsOz_sDJXni8K5wk0Vfu2naYBv0EfpNL3qJ-_aImroLdVkcmVgZuUIZWe2rDsf4Q3uf55fZwunbkBLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=mWpcqP9ebwRZsx1h19FL4ajVBhGtqM7La8z0oM37pxqGROrjAwyyma3FYpUIOqrEKTB5tInT3dUuUFX17For4tNlS-cIdM_ZhdFJK5qcpiIBapYJeeG5f09Li-tAt9hP5d_PZl0AM-CeoznQ7N7G9u_RCS9D5nvI3P3v553-Qp_8srlfgoYs81U8Fz-DMnh7aXTBVTF3nfXpmWfYsP81KPK_9MP-ELb-RGjy7NhXhsECxwofUGeM5j4v6O55m-mfGntMf3GAsOz_sDJXni8K5wk0Vfu2naYBv0EfpNL3qJ-_aImroLdVkcmVgZuUIZWe2rDsf4Q3uf55fZwunbkBLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5U6zocGFWhkaSHXI0GI1whlvZrH0DeUMBUka3X0Wk8IBnNrCD_PDQqD-tYv59XQQOqaYINM-ECvMJFnRHHqPF_zLco4vXDw-5HV2SvWHyZ-JtlFWT7IXGV6awdHvyXAtjK1HrQahhC42-QTMVd5G_xIjx3j8uzJPQY_YkUlehkE9j3_Rsm0Hch0phA0XYjwO1A8iI-2hCATY8_88TKL6FdadYhaLLZJGEbrrHbqDf8zPVnHmRZK_T8YpoDvDbj5IlnSunrBP6EamobhETm0rBK2Jz0v89iSl0VxbXwsnWCl1wt5Fjih7Xqom5HictbQKZotIviIWeJ4C6Sh9LC6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=gUqFVsqCmmMl-prR4b-xRSZp47iOuCDqIo6ZHFVZPqG6OObeUuVAoI6Fnp3r3lHZcPz0zxuuqMCa_IvOeA-oVMLnsQ9zyzCIGY5nbogrnVtBU7_R0Qd97PeDGi1dVNAO_AF70RBMpacL46O01FgkTYkWFVgEaBIebhBjjdklCdn0annQOKMNOPkzCqYheqD3LnhzOzdt2fyxdOKSp1JVm-nabsR18u9z3igrIRXrq_SQBOQO2vkCC8HCG_zJQ_7ilXKKw1yj7l4h4yxbvYD3fN9hKFeduVUeqdZHyc05HN3uFoFpM7D5TWFNomD-2lsHAAgQc9_E67enTB4SgWFYBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=gUqFVsqCmmMl-prR4b-xRSZp47iOuCDqIo6ZHFVZPqG6OObeUuVAoI6Fnp3r3lHZcPz0zxuuqMCa_IvOeA-oVMLnsQ9zyzCIGY5nbogrnVtBU7_R0Qd97PeDGi1dVNAO_AF70RBMpacL46O01FgkTYkWFVgEaBIebhBjjdklCdn0annQOKMNOPkzCqYheqD3LnhzOzdt2fyxdOKSp1JVm-nabsR18u9z3igrIRXrq_SQBOQO2vkCC8HCG_zJQ_7ilXKKw1yj7l4h4yxbvYD3fN9hKFeduVUeqdZHyc05HN3uFoFpM7D5TWFNomD-2lsHAAgQc9_E67enTB4SgWFYBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=E6FAu0zNOWhiEEbOK7absX2j7KbrGkxffUs-X2OEQ_7-1y5fRCQfOVcQoaq0VUt_DurXFzrPzZkkDXxwELbz18cYl6VIQNwe33bt0vKUmAj2WqRgOy4BjR5OGlBvDv4QeyTsuY3FYKVaZxuGcCS46RT6i2JS4hSp99f8e9cvuEvakonEu5W1oHyTo3jaC4UeFygV8rEBkcAGcc9d0CaYRVjhYL1k_b8ZbScuICD_okf9pj-CW-f-gV_djdVnKae7S_Nk1Y82hQMW6JxutHCkmFTjyUeRvOvfNy_ue-FK1mwsKr9aL9QGLgrk4klQHXI8zoUDBkPZEccEcz9XzTbbkCw6nlXd8ao3gDzPHEaDT7rCC9LRv0sgDjIzRVJKmeMtYnycZPcnGEn1uCaUjviMW-6gz8dKGyWTrscGRV4n3E1pXFOab0PJ_5qJV1hgC55pgCcbnK8HrV9pHKLl7r0-VSUG0bqcTUeBuzbg1Rd_e7rOAyWwBkYu1_B64LpTp48AqMEDcHv9iBgFirmBbK_vkqP1ApbiiGUe3mvn8Ntidx_nOKq1zeVwiyNZ1LmhcqcSCBd5kBrW9hXQwq_PEmx6iF4ow40X9VEgYZU0rv4bBAbRmExb0cuHQn2laE93bM-6hPdktrS3Y26gNTuD_OCdlkV8-cfPtF4Nt5gjZ1xTwO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=E6FAu0zNOWhiEEbOK7absX2j7KbrGkxffUs-X2OEQ_7-1y5fRCQfOVcQoaq0VUt_DurXFzrPzZkkDXxwELbz18cYl6VIQNwe33bt0vKUmAj2WqRgOy4BjR5OGlBvDv4QeyTsuY3FYKVaZxuGcCS46RT6i2JS4hSp99f8e9cvuEvakonEu5W1oHyTo3jaC4UeFygV8rEBkcAGcc9d0CaYRVjhYL1k_b8ZbScuICD_okf9pj-CW-f-gV_djdVnKae7S_Nk1Y82hQMW6JxutHCkmFTjyUeRvOvfNy_ue-FK1mwsKr9aL9QGLgrk4klQHXI8zoUDBkPZEccEcz9XzTbbkCw6nlXd8ao3gDzPHEaDT7rCC9LRv0sgDjIzRVJKmeMtYnycZPcnGEn1uCaUjviMW-6gz8dKGyWTrscGRV4n3E1pXFOab0PJ_5qJV1hgC55pgCcbnK8HrV9pHKLl7r0-VSUG0bqcTUeBuzbg1Rd_e7rOAyWwBkYu1_B64LpTp48AqMEDcHv9iBgFirmBbK_vkqP1ApbiiGUe3mvn8Ntidx_nOKq1zeVwiyNZ1LmhcqcSCBd5kBrW9hXQwq_PEmx6iF4ow40X9VEgYZU0rv4bBAbRmExb0cuHQn2laE93bM-6hPdktrS3Y26gNTuD_OCdlkV8-cfPtF4Nt5gjZ1xTwO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQZhPtiANGQU-qERuZHnIZRdhZye1HyfONyooS9oeUAP60XO7s6y0FZx1l6-ntkRim0LDhGHwMXBDGkIwGKL6pAd5FlKPhbADon5j0yYM-c8lypDNAXJXp0cj9IQ-VTVsj-HgWDA3ACGEg9RmJsO8vl9HeXvggYiQFjX5pTsl8n_2NUMOQA2uX1TD0WToK_4pjLchNj3RmNwcTeTxBz2Yl9OIK4Ey5H7p3lULbO1Id4sazTXnuemMoj0aBPB3UzhJYjYWEWkT01HIO4W33ueth2hVYabNh_6GkeO0EomKOalLoZUjH9__bg8u8S418iEkrtc2A3omzAbiRhaGnd40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=OMcZ7PXP0NC6UjUvkhzCJBugDqOYWCtPoebr8h3AhF8msZ28bWUNhvg67ok4HZVS342iM4CbsjyEY_XMmyY1Mlpren5ciPIC7FyKUjPmvmZKn_qaAcQq8Ct30Q6nyZHzos2sjd8SS_cR-4ofL9Lxw1GWbbjomG_4yvwdV8HmYesP4uIhO14W2qk2jKOu4SolrcyY4qwN1ZqPTUz8I6BmqJwxx3AemXA-OXN1MsEzQxFjw-z4MzqAMjOGOVEGShZLKw9QcSGNrD_xru4QCExnrjzpZx3Yn3piSqU9V3uNWq5tPpyuCiODDxISyumA2CzqWzsx72jKUcKHOCAnqWROLEYRheRduIa2cnKz37cLrkUrwDGHT784TKA_vQNG0K02umfkHUbsNPIze9vT7zm0euhGn3mLLTbDHBVYH00_HMCLZhMWU_lRDXQIOPwxi0BPKsa3voxydat_ZZIvJ_aYTVYAiuth5fCAxS-O3ucs0_hdX0uayYjahajtrkpanKGfc7GpWWfiPBEGCHeYGE5913EidnSJdtH9dOensqWfaiq2ODGtS4W1CnRgBA5a4Hq2yoIUbtWI678bQwL4KyQu-_8PG8mJv-qLzQFyqKGt2LNEvbMMZPis80nwIwjmE4u0ouN_TXKd4jOMA27Gq5nmAfHAxf4st_AQXOPSjai18Xs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=OMcZ7PXP0NC6UjUvkhzCJBugDqOYWCtPoebr8h3AhF8msZ28bWUNhvg67ok4HZVS342iM4CbsjyEY_XMmyY1Mlpren5ciPIC7FyKUjPmvmZKn_qaAcQq8Ct30Q6nyZHzos2sjd8SS_cR-4ofL9Lxw1GWbbjomG_4yvwdV8HmYesP4uIhO14W2qk2jKOu4SolrcyY4qwN1ZqPTUz8I6BmqJwxx3AemXA-OXN1MsEzQxFjw-z4MzqAMjOGOVEGShZLKw9QcSGNrD_xru4QCExnrjzpZx3Yn3piSqU9V3uNWq5tPpyuCiODDxISyumA2CzqWzsx72jKUcKHOCAnqWROLEYRheRduIa2cnKz37cLrkUrwDGHT784TKA_vQNG0K02umfkHUbsNPIze9vT7zm0euhGn3mLLTbDHBVYH00_HMCLZhMWU_lRDXQIOPwxi0BPKsa3voxydat_ZZIvJ_aYTVYAiuth5fCAxS-O3ucs0_hdX0uayYjahajtrkpanKGfc7GpWWfiPBEGCHeYGE5913EidnSJdtH9dOensqWfaiq2ODGtS4W1CnRgBA5a4Hq2yoIUbtWI678bQwL4KyQu-_8PG8mJv-qLzQFyqKGt2LNEvbMMZPis80nwIwjmE4u0ouN_TXKd4jOMA27Gq5nmAfHAxf4st_AQXOPSjai18Xs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=nxHdfO26QZYgsU8MR4-ufWN9Zhf3e8DHBEYpLWrHtraTIL9rjNdgqPfg2fSF40wyBCx5EsLuKb9-Y_pQ4b-ayrqcbSpzCU_18536eUsQP9r9uChE3RC8Outh3ars8PqeTt8NwivfhB_l7xzMd8zqq-PAqLn6SYbXELHmBB-50Jwg0vo1-onjXVsyIlOmKhLNQt4NfIrSUgUgL7D0zHkrJjmuOPWf6VMZktxB7K04TlqeNuHP1t27nVB6kncn3YiMmeJPE-ThzU5DIR1UeOCp5lLTr9ohBfS3TgHGiRlbqYptPyH3j_xENX-GpfvegggR2uqBLNKgea9AqMPPf9MqpS826uyLeFf-fFR2Ngn3gtARhvCIIrom6HCNXPznwOxGRMfc4HtJE5h8gSMhiVhPPTFLa_M65fcHImtZx8v6zcq0X54YXkPxWMXDUzexsKd9g91tXHSwr94Pk4w9X0WICgEm-TtgXLtexX10hlGXAwq5cMCb1QfLuGz1akHEdJZ8f3oLBigs2AGiRZ5AkTdwiRaQ94ydXMtYRlnShmYbAanhLOYSisJzkXGf4rjZNdnBFOPAaAvAbZMsOvk4Yo_VCisZXl-GRPYzELcQOr4WxTE4oxPtDDvp5Fy8-HgiHHWhB6rWo75pX4WEbbGA6F-cUWFGOKCHxTTV-OAtD0gpWVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=nxHdfO26QZYgsU8MR4-ufWN9Zhf3e8DHBEYpLWrHtraTIL9rjNdgqPfg2fSF40wyBCx5EsLuKb9-Y_pQ4b-ayrqcbSpzCU_18536eUsQP9r9uChE3RC8Outh3ars8PqeTt8NwivfhB_l7xzMd8zqq-PAqLn6SYbXELHmBB-50Jwg0vo1-onjXVsyIlOmKhLNQt4NfIrSUgUgL7D0zHkrJjmuOPWf6VMZktxB7K04TlqeNuHP1t27nVB6kncn3YiMmeJPE-ThzU5DIR1UeOCp5lLTr9ohBfS3TgHGiRlbqYptPyH3j_xENX-GpfvegggR2uqBLNKgea9AqMPPf9MqpS826uyLeFf-fFR2Ngn3gtARhvCIIrom6HCNXPznwOxGRMfc4HtJE5h8gSMhiVhPPTFLa_M65fcHImtZx8v6zcq0X54YXkPxWMXDUzexsKd9g91tXHSwr94Pk4w9X0WICgEm-TtgXLtexX10hlGXAwq5cMCb1QfLuGz1akHEdJZ8f3oLBigs2AGiRZ5AkTdwiRaQ94ydXMtYRlnShmYbAanhLOYSisJzkXGf4rjZNdnBFOPAaAvAbZMsOvk4Yo_VCisZXl-GRPYzELcQOr4WxTE4oxPtDDvp5Fy8-HgiHHWhB6rWo75pX4WEbbGA6F-cUWFGOKCHxTTV-OAtD0gpWVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=V_3MAk-IggC_4JCjYSwTQ45q8r_pxOxyolOtOuX-_CAUhim8aQQO9E_uqm63weeNvxUYz-YnPlV89jszGL4lV1tR2wAXn9NTAeVAR9GukhR12HrnON8AjHMhOFxH8zOpBFrBvRAs283eHlvq-xPAuGCcKOkS3sxui8cR6x06vVkycsEyOxKmhUN9c5MIhaP554hxKExNbDbs2r8QMaWKtse6s1WxYES1yMjmawweu7hnzeODfi0aQATx9V0kNiaTnVc_dA91XiLd1uKc102XHZCYuhZI5xl5DYqZlBPi_ABvFE8oOsUoig1OcZLtZrA5RoozImVvWlzOTOFwq_ugGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=V_3MAk-IggC_4JCjYSwTQ45q8r_pxOxyolOtOuX-_CAUhim8aQQO9E_uqm63weeNvxUYz-YnPlV89jszGL4lV1tR2wAXn9NTAeVAR9GukhR12HrnON8AjHMhOFxH8zOpBFrBvRAs283eHlvq-xPAuGCcKOkS3sxui8cR6x06vVkycsEyOxKmhUN9c5MIhaP554hxKExNbDbs2r8QMaWKtse6s1WxYES1yMjmawweu7hnzeODfi0aQATx9V0kNiaTnVc_dA91XiLd1uKc102XHZCYuhZI5xl5DYqZlBPi_ABvFE8oOsUoig1OcZLtZrA5RoozImVvWlzOTOFwq_ugGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=Ai1wsQhJ6OcBMm9qwu0HX_DxmBbrR59uC_V4ZGKk3iz2XcO1dVHQsobqSBftjuJMAKEmXrKiGWW9Bzsv0b9tN-sMFjfps_OGqCX0GYQ12gLSYMpzQVUIxjsamyTjj2zfYphTMMX_Y1s8Q8ErVfUgruYaN_e_6Ox2A939iCDOf0Q-6NYc5huKqfxRA6EQWmvd_aAVfrrOCPQlZA3kUYlzFeFgFDRzDsWs4Xh_cFa8S-AmBlVfjH7QDnPkhyeP57l2GKzIP5kcbR3wSF-TuYk3HKEIT4GaoD6NKH4iRf_Visg30jvl1Js9rxlSBJRH1aujo5fEejhAuXNxtvzqtazC2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=Ai1wsQhJ6OcBMm9qwu0HX_DxmBbrR59uC_V4ZGKk3iz2XcO1dVHQsobqSBftjuJMAKEmXrKiGWW9Bzsv0b9tN-sMFjfps_OGqCX0GYQ12gLSYMpzQVUIxjsamyTjj2zfYphTMMX_Y1s8Q8ErVfUgruYaN_e_6Ox2A939iCDOf0Q-6NYc5huKqfxRA6EQWmvd_aAVfrrOCPQlZA3kUYlzFeFgFDRzDsWs4Xh_cFa8S-AmBlVfjH7QDnPkhyeP57l2GKzIP5kcbR3wSF-TuYk3HKEIT4GaoD6NKH4iRf_Visg30jvl1Js9rxlSBJRH1aujo5fEejhAuXNxtvzqtazC2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=jd_94gpwzh72EOR5bqgxipB_YwP9xHxj8HHSNYpCYRUCkFRgX08iNIktIjmWH1EVkcfMHh8FQf-IfuP7rqTIukboiyhd2MThyw5s7VMOxqclTma9PA445MYv7EDKby-lZHajlTDNiseypyYm1vBfoSoYgHbFSQjxMSX4-ywnBgSS1FJaidk-bUV10HhrSui9sHP_er0j34k2XJ0_-dnFX2EUVRmbAIfcl-9uzOEoMZPW2gFEWltj_WgD-oAZ7oKAPfZtrDWYTaF65tvBG2ZMvK_2DYZmzkZG2wboDkV2F53eMih-MrJ4D9oz_cmIe_l_Ug6oM15MxQISiRGRFpXTpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=jd_94gpwzh72EOR5bqgxipB_YwP9xHxj8HHSNYpCYRUCkFRgX08iNIktIjmWH1EVkcfMHh8FQf-IfuP7rqTIukboiyhd2MThyw5s7VMOxqclTma9PA445MYv7EDKby-lZHajlTDNiseypyYm1vBfoSoYgHbFSQjxMSX4-ywnBgSS1FJaidk-bUV10HhrSui9sHP_er0j34k2XJ0_-dnFX2EUVRmbAIfcl-9uzOEoMZPW2gFEWltj_WgD-oAZ7oKAPfZtrDWYTaF65tvBG2ZMvK_2DYZmzkZG2wboDkV2F53eMih-MrJ4D9oz_cmIe_l_Ug6oM15MxQISiRGRFpXTpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=SoV9Tj_ZFPUg7VpsPUBHGUyRLQd3UfckHHIipoP0vPOGdfgdDHQ4gh8MN92JpzPG6an7XS8mF5Crpb-EXWZKkiWlDz4v2elwEqsVC_9r_Lpt0hwTeNa_MgAcGvhtaQUHHz9myvAYFl3_Qub-DThhAR27VxmLhMyoiEcR1xAk3MGLl0IpJBQCAJuu9-90x7CIXsCCL0pxcIJRcZJZ1CHSyelk6SF39XKBAYsOJ67JoBwGhMAmw2fQpkVj4kNRT8xpHzhivU9wkRd1V3bjqX-vsk7LGv-9D-2IBEBNST8m7kJkzOQf3uElkucMWVwCHsqX6RnwRMBJNrz2Xe0KDQDTjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=SoV9Tj_ZFPUg7VpsPUBHGUyRLQd3UfckHHIipoP0vPOGdfgdDHQ4gh8MN92JpzPG6an7XS8mF5Crpb-EXWZKkiWlDz4v2elwEqsVC_9r_Lpt0hwTeNa_MgAcGvhtaQUHHz9myvAYFl3_Qub-DThhAR27VxmLhMyoiEcR1xAk3MGLl0IpJBQCAJuu9-90x7CIXsCCL0pxcIJRcZJZ1CHSyelk6SF39XKBAYsOJ67JoBwGhMAmw2fQpkVj4kNRT8xpHzhivU9wkRd1V3bjqX-vsk7LGv-9D-2IBEBNST8m7kJkzOQf3uElkucMWVwCHsqX6RnwRMBJNrz2Xe0KDQDTjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=t7xPAEv6IRNSDusDieWL875pfdtK4khgHPXItWqot5qZzWF84BPLnI8uguP8XPwblXXjPu1et74hYmH1gwvvtNmvvSOnszCXN9Z9qKiy0ZcEJgaJf0H10n9To30TnV-vBZX8yfrRf8b5tdhhnuqjd7kWegiI9fcdnWbOl27uraAsFYzI6hm2iRCp0676KftpnTfUsriIdhNuwSjDZSxqPvjtWeZgdAvO_HtDeA3GDWH21-hHfmXT5IjsuvSQipmMVJUkNWn-7hcfp3dfs-wPSJ4ddyo78XqwKn2TL9NIVpF_MyAWOmhw0tzCQw1SQ3cJpolPvN5nRHJ9TQB4EBbS5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=t7xPAEv6IRNSDusDieWL875pfdtK4khgHPXItWqot5qZzWF84BPLnI8uguP8XPwblXXjPu1et74hYmH1gwvvtNmvvSOnszCXN9Z9qKiy0ZcEJgaJf0H10n9To30TnV-vBZX8yfrRf8b5tdhhnuqjd7kWegiI9fcdnWbOl27uraAsFYzI6hm2iRCp0676KftpnTfUsriIdhNuwSjDZSxqPvjtWeZgdAvO_HtDeA3GDWH21-hHfmXT5IjsuvSQipmMVJUkNWn-7hcfp3dfs-wPSJ4ddyo78XqwKn2TL9NIVpF_MyAWOmhw0tzCQw1SQ3cJpolPvN5nRHJ9TQB4EBbS5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=iYhkRDRi9RY8vo6ZDj-5g3jzwns_Xps_usLgJgdFSFtCOTgRGXubo_S4yPN72VnxwuwOh2V-VC6-EeSRUER1kUtaoY4Zzwii0EEBv3unlfaHDdVEuifh83apVbF15UDNzSn1G7XXfvtLKcMFPLCqyshEURpPgZOzaWjAkVBiKubdcawH8Zf32_4dLO3QILOeOfizSSNtv1uAwW0ueiKO-a93tioyLmB8EzKQnkdEVn3LeCydbZ9Gk3d8xq4aTSk6igCNyfLchf387h68ng6thoIpCNdAp12ejOehnjY-hAHxvSxyq2Awufmq783Nqav0dTGdxwQC5EPeXx52J9EIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=iYhkRDRi9RY8vo6ZDj-5g3jzwns_Xps_usLgJgdFSFtCOTgRGXubo_S4yPN72VnxwuwOh2V-VC6-EeSRUER1kUtaoY4Zzwii0EEBv3unlfaHDdVEuifh83apVbF15UDNzSn1G7XXfvtLKcMFPLCqyshEURpPgZOzaWjAkVBiKubdcawH8Zf32_4dLO3QILOeOfizSSNtv1uAwW0ueiKO-a93tioyLmB8EzKQnkdEVn3LeCydbZ9Gk3d8xq4aTSk6igCNyfLchf387h68ng6thoIpCNdAp12ejOehnjY-hAHxvSxyq2Awufmq783Nqav0dTGdxwQC5EPeXx52J9EIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=qn7fGLAsjnMes5Nv5Z18ps8qey8qV8cRmaAWk1QECHoMo-Bm3Ylg_lAyy26IZqJlKkQKE7it9MPk4BGOqb-KbtiuXqkwNPMYh0zGQGSXqQPFO2LFPzC03XofdJhzSR0OyKrwXnBjhYtqiak4a9P5c62OJI44haH4INpTXrmAYI3P90iGfkAruz6DpT-w5CR2YNbasJ3h2tH9QVQlrIc_eNmJMPk1TW-0tF-l3N89lyBLupooPEK1shekmwgXZTuaHdjj-1iIlf2Hus_aYZ8bXObj9dn9aOSx_csE-Dca3O7WITDZBtRYhUnJWalu_Oh1knSYTpvBnA2wHjjXCUj1YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=qn7fGLAsjnMes5Nv5Z18ps8qey8qV8cRmaAWk1QECHoMo-Bm3Ylg_lAyy26IZqJlKkQKE7it9MPk4BGOqb-KbtiuXqkwNPMYh0zGQGSXqQPFO2LFPzC03XofdJhzSR0OyKrwXnBjhYtqiak4a9P5c62OJI44haH4INpTXrmAYI3P90iGfkAruz6DpT-w5CR2YNbasJ3h2tH9QVQlrIc_eNmJMPk1TW-0tF-l3N89lyBLupooPEK1shekmwgXZTuaHdjj-1iIlf2Hus_aYZ8bXObj9dn9aOSx_csE-Dca3O7WITDZBtRYhUnJWalu_Oh1knSYTpvBnA2wHjjXCUj1YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbyltvVE8e0Nx8nCVgFtWw_iG-x3LqwLxRyFUzC_abKmRSGH_UOQS2128zw0qcZTXyabHk5xM6swczUxtyw4X3V0jsx2fQgrXbrtbGxPEaMNnWuI2a_0LN4Nnk1Ar5ukGLvXX_c7WVO2dWsdJvdv5v-TpA98yIRxBNxrTjV9JxLyj8YoBEssnrYCQDLBKgeX4_VzPl6EatC9RkTjkBay_yLfQ-F8V_ybfteQH7F4qZySf0Ccj-G0V49gFDxwa6EDiI7UJsp-VLsY8k22ybN6xGZbveU5V5t-vqSKGQsNvIr_vcyCA5tRY0nymTnHDW0axmV2wj6o-EUH43HSM1ihfQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=RKIUpGOxYJEmj9-eQReCTld0LVwBIUObVgXLn0mJO6oeE-PQtnL1ZrDGFhEw-Mv-r3dBYt1t1_rx_He_ascVDL6ManrBgmB8rDaSrsD4w3yaIzTQXP8V6So-n65k_SpzJzoKGhPv1pyAnI7mfSboNA40eXNcrfFbZj8I1PWCM3mWofz2KVfXBPYkSVKIMfnfH2DAjOqILi7-KQYDtm11TWJ8Alo7qSAV6cK7mBkFrf632mTg7IIl-M-NmV5HbEBLiZZKGiothknSFa6F4T5LEAtwcpIOnkRVaLdyR1CFJK2EO3KMgizcmrEDbP7Kn-9EQe79K013PyzuzOivUgRQyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=RKIUpGOxYJEmj9-eQReCTld0LVwBIUObVgXLn0mJO6oeE-PQtnL1ZrDGFhEw-Mv-r3dBYt1t1_rx_He_ascVDL6ManrBgmB8rDaSrsD4w3yaIzTQXP8V6So-n65k_SpzJzoKGhPv1pyAnI7mfSboNA40eXNcrfFbZj8I1PWCM3mWofz2KVfXBPYkSVKIMfnfH2DAjOqILi7-KQYDtm11TWJ8Alo7qSAV6cK7mBkFrf632mTg7IIl-M-NmV5HbEBLiZZKGiothknSFa6F4T5LEAtwcpIOnkRVaLdyR1CFJK2EO3KMgizcmrEDbP7Kn-9EQe79K013PyzuzOivUgRQyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=ReJq-GTQZN8zOjLZX49waJs4xSBufFdAkuZGVAEqhVuYSPbgXpc0M6iOC2758k-oBYrF3Ia38QpiClePA2vSfMahcA9U8AwMEomxqfgwrOgmZJ9wpvENrVwY_MLnDrO8qeVaAITUY8E20rOBuwg8Ntm0RHIad7Hr_avRLDBduO93lHYCEmIxGxYGTZoBY-SZLTZ9-hEvZDtOcuTqXYvFM3SRckuaVGhTnJrDm5sWo0B7dXzNB_Ud7tDb6-kJWyMJFrcc5dwMdgIVAnm8rHvrdDjuxmErp5af1tLcW4xojeQktN8-Spahk6e6tSjos8_vAYCLPOHMI3J8d7p4qIqdGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=ReJq-GTQZN8zOjLZX49waJs4xSBufFdAkuZGVAEqhVuYSPbgXpc0M6iOC2758k-oBYrF3Ia38QpiClePA2vSfMahcA9U8AwMEomxqfgwrOgmZJ9wpvENrVwY_MLnDrO8qeVaAITUY8E20rOBuwg8Ntm0RHIad7Hr_avRLDBduO93lHYCEmIxGxYGTZoBY-SZLTZ9-hEvZDtOcuTqXYvFM3SRckuaVGhTnJrDm5sWo0B7dXzNB_Ud7tDb6-kJWyMJFrcc5dwMdgIVAnm8rHvrdDjuxmErp5af1tLcW4xojeQktN8-Spahk6e6tSjos8_vAYCLPOHMI3J8d7p4qIqdGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=GZW0lu18WnTuKIrkyoqa-wnF8WAnmDJddniTFOcif0q8Ik2nKFPF5vomY7rRRuR55xAqyiJ-qdAuscclWBfiuE5Bn-IjRWHW6WaFwJNz12DjAxOxDE5NWvg9iJRrwhjxiGhVrYrx1ikYpr4oh8QBQAqq9yx4r_DQw8GPwARuBSOp423ZRrfLGJswgrX3DZEXTYrdoSJnuzvATRoctDbhuNMsqfWV7aJiBHK_aoI7ia4MpRKudyrnj0WXxu7tOPMYaIgssqNArWFLy2ecqb1-3Cy_auRa7wQqtOj6_lHF2_7_OAjA-CywzO8U8q-yWKrFTRdJuvR29sEiopUOUcYT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=GZW0lu18WnTuKIrkyoqa-wnF8WAnmDJddniTFOcif0q8Ik2nKFPF5vomY7rRRuR55xAqyiJ-qdAuscclWBfiuE5Bn-IjRWHW6WaFwJNz12DjAxOxDE5NWvg9iJRrwhjxiGhVrYrx1ikYpr4oh8QBQAqq9yx4r_DQw8GPwARuBSOp423ZRrfLGJswgrX3DZEXTYrdoSJnuzvATRoctDbhuNMsqfWV7aJiBHK_aoI7ia4MpRKudyrnj0WXxu7tOPMYaIgssqNArWFLy2ecqb1-3Cy_auRa7wQqtOj6_lHF2_7_OAjA-CywzO8U8q-yWKrFTRdJuvR29sEiopUOUcYT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=jcwhIFcj617zHenhp8IxDHkosWw4qCKwfqs34PTVjqKsqEgimqZ2TugXJEJU_7SRbx7D5sIUMsUbWTfxIh2spcoZcVbSy8RlE9IKhA7Ogoo1kbOnpZQn2kN51yjKSU6qqND14boNyEhao9X_UWFGEG1OURjJAXlg4Djuv91OE99iOP4xZpHrCFNuFmXuOoG8t6Vrsz92fBsJlws6KeIl9i4E7h-9UZnBYDISurvq_KTaqSDvv43zcdyokCC2QJI4KC5wGXqBejnWKuZ_g-3V_sbupgOhcuKI5nNqTWu9QkII4Shzh2mx3C8-lC_LmQUevGYAnf8o8NzHNYr4MZ_BoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=jcwhIFcj617zHenhp8IxDHkosWw4qCKwfqs34PTVjqKsqEgimqZ2TugXJEJU_7SRbx7D5sIUMsUbWTfxIh2spcoZcVbSy8RlE9IKhA7Ogoo1kbOnpZQn2kN51yjKSU6qqND14boNyEhao9X_UWFGEG1OURjJAXlg4Djuv91OE99iOP4xZpHrCFNuFmXuOoG8t6Vrsz92fBsJlws6KeIl9i4E7h-9UZnBYDISurvq_KTaqSDvv43zcdyokCC2QJI4KC5wGXqBejnWKuZ_g-3V_sbupgOhcuKI5nNqTWu9QkII4Shzh2mx3C8-lC_LmQUevGYAnf8o8NzHNYr4MZ_BoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBD2PiJgyINJfvrxTmnX7CH6m_owNt5axSdmS8xPS0jedehPZKKoEZKlPUWWYC4g9HLMyr7LWkfHZU9FAmWCEoz6LMGDMWy_m98vxdE-p2PL7lGfcbDgguT42lYNrCRnffLlmkIrWY-Q-beiBX4tpIsWoKwWaeV3i1lzWVGU-GNQQZe15HjkedGuHfRQB8P7gayXmviqYFJZhvPqobQAe1YNVL2D3wkaUfyEkhipf9xbpGiuEeeFvJ0BR0dO6PaLrMIgabBhhvOdbdhego_zUCjf0Jt0KrgwlDPZxLX4MkmjAMRukYcaZFUkMD89fSeRgPgL2gzpiKVPnSlsoZb_Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=sZ20cDkMsBpHKzndMMQJwk2sa5no19JrG9aeJuPDDEJWZobO9iRNhMqV_XS5sxXqzkwfXLZwFnC3Yl8uB1WMUNKgm_QKGdU-kKDKZtZ814bU-XT3wnde074FcX8iK3dSORdhyE7u5Yog8JxsrIylbiIYy_kngZ6fSzpsiBBV0ShSnyKmt-VPdrgXa2Ytq_cpzm-Vj2wIJFGtM2XNQyrlOmmFyWePHSYkyxkiqE1ooWCRhoRjk8q33ja62SqpyfhLLiX0THViPrcPxN07Nav6dMrFpbrNLkja-Qvd4OP07qXUN9p77qCXLOnHeSmjaUTGFRLUZ1U8AUSqTwGd0Y5mLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=sZ20cDkMsBpHKzndMMQJwk2sa5no19JrG9aeJuPDDEJWZobO9iRNhMqV_XS5sxXqzkwfXLZwFnC3Yl8uB1WMUNKgm_QKGdU-kKDKZtZ814bU-XT3wnde074FcX8iK3dSORdhyE7u5Yog8JxsrIylbiIYy_kngZ6fSzpsiBBV0ShSnyKmt-VPdrgXa2Ytq_cpzm-Vj2wIJFGtM2XNQyrlOmmFyWePHSYkyxkiqE1ooWCRhoRjk8q33ja62SqpyfhLLiX0THViPrcPxN07Nav6dMrFpbrNLkja-Qvd4OP07qXUN9p77qCXLOnHeSmjaUTGFRLUZ1U8AUSqTwGd0Y5mLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=ejaejfoi9mPXfGnefWo-3MpR6UEj1fAQAGquB_kOyde3C7Vpjd02tYoYsnrNCy4InBzdDaDrLlBJFkNatqO1PsYWsoQWhwIbDheWMZBG9-HhAy5TApOc1oLhRMjwWpzHcXZitBGSuh7ytCS8sLyPlaf4VDP27qBX8bvotxwvG8ecCMd8zkSs0-odzEAsTCLcLJwaBXfxQCvwzJRRZoFFMT4gIueWijSG3FZJgNeopPj9C19mcE71oOxKtrLizYrTeRXZ-f-6_kx9B1VDoQ0NR4cFUO-AZQSOQnc3NY-nL1VOoLK8sIq9Xi5oZhXhkDx1mi0si9JvXh3xiO3ko_OjPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=ejaejfoi9mPXfGnefWo-3MpR6UEj1fAQAGquB_kOyde3C7Vpjd02tYoYsnrNCy4InBzdDaDrLlBJFkNatqO1PsYWsoQWhwIbDheWMZBG9-HhAy5TApOc1oLhRMjwWpzHcXZitBGSuh7ytCS8sLyPlaf4VDP27qBX8bvotxwvG8ecCMd8zkSs0-odzEAsTCLcLJwaBXfxQCvwzJRRZoFFMT4gIueWijSG3FZJgNeopPj9C19mcE71oOxKtrLizYrTeRXZ-f-6_kx9B1VDoQ0NR4cFUO-AZQSOQnc3NY-nL1VOoLK8sIq9Xi5oZhXhkDx1mi0si9JvXh3xiO3ko_OjPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWnEtAg5WvWFLt576RSk_f1KZCdy5V4BX0tn1hE-rOjQLwbLJsTTQYI3cy0FFcdTX6Z2sQaE_aLOwKo0J6kDwlbf242v8fQmqiupjEeFyA1vrxLcFm6rIlXBdL5dYbL7p7JOLb0hyz5gjCJqPHZRq8f3dcRo1-_CmxGxnwRfcOMuf7I1t2PeB11rl0jXtvlzq3mBGVaMj5b7cx-md6IdXM_5TZhWIg0ABVDHCxVv32TdQ9tKgRPujjsZCgZfMYYh2B2o8L_lXyvQug5PD2lM7V-0T_VJAEwoo6tR64urKrsmp2qcaWcd_9qsS9AeVHB3ZWw3zu9VTdUyVXahRbyXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_bfRfmWudr8GJr16iH8-3ovLlhadS0ZTvIFlkunT9I8Uq67Itn5j_zo6Pi5ZfdpQ9bJ6cERl3AoXwBkTy1v0KXmLq82MikuaWMpYJeZZiVaPqPpgr74PL6WV-HoQuFuKO98iWr28RGPXlbwJR93Dw5ledK0dNPAvNCKOIiw7Fh08KtFKLPQkKvLxydDq-CE9Pzl9MLmACDz1NOoOvsit9gnbKGMVP_sC3ZQlMMGCAPBZSvWpr1kGrEhRVplxFy8y6WObD9QnfTa_KwubXcs-B_P28Vi9lBJjNk4L0mtu1zaLdpw1OiuLKBngEgMJtIIQHTZ0f18w4y6iCUNFKLKpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=tt-n80sCy4fYfUREW-CboThrNV2IhRR8nAzEJMsgms1ZWpW0nOi0i3C7TOuU6forU0fokD5NZkB12HCcGhqo3kOV8Mt4QbS3JmH36vrRtMM4mCEBdjddOsBJ1oBXy0QRqSVEsrrHlwSIpYWxl3cAfzfgVL4-EaYYtMF8AOKeyYOLwHrtTB5nYEAVQPBtAVVviah1-cV6j9tD_i3i5D2HFL2jH1zhT5zS5GTZ_Ug7J9dxSfgmNYcsC_CRJidc8hMt91cb9ecvkmIFrvD1VYNCL-kr9d4EBvMKQtFwXzBmR6yeZDMGP3OENEXLa3y-9mTZXe9-UVTXUEeRjNJB9CdfuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=tt-n80sCy4fYfUREW-CboThrNV2IhRR8nAzEJMsgms1ZWpW0nOi0i3C7TOuU6forU0fokD5NZkB12HCcGhqo3kOV8Mt4QbS3JmH36vrRtMM4mCEBdjddOsBJ1oBXy0QRqSVEsrrHlwSIpYWxl3cAfzfgVL4-EaYYtMF8AOKeyYOLwHrtTB5nYEAVQPBtAVVviah1-cV6j9tD_i3i5D2HFL2jH1zhT5zS5GTZ_Ug7J9dxSfgmNYcsC_CRJidc8hMt91cb9ecvkmIFrvD1VYNCL-kr9d4EBvMKQtFwXzBmR6yeZDMGP3OENEXLa3y-9mTZXe9-UVTXUEeRjNJB9CdfuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oK6pWN7N6iv8EqPwcP7VcpZFILaQ4xswMrEm_SKpTdt2D-zM8a8I43SuyfmVaqva9Fu-gem7u6h3C2Bp2Q2M8sCA9iqnNWRRCd39Xz3ePolXovaGsZxWxqHXbnGFJde9RHk5SCZLCtq7qcNvbb_Vqc46clSI035uJLn8KzXMdWEf4Gc1A6U4PtkMXzvkxd4y7jyO0anYqDLEgAP6Ux17Wjrd0U6Boe7XiBcucH80RIvC6szJvVx-UAfnR8WKi7gBjXL6A4GxJOZBm8mm9obHNuzZXVPyKxNzck4jasVSEqLWhq8-bKk-0-_toQR661A3UCK_DaPlrv0E56io_D8k_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEw763RJXFw_eca7CVvjHDct--YdBksAv-0xtw-HCbiKB_iL5PchqNKdKJ2l9rrb_xnycG5hZ15dpYaLmDTH-N9r9w80lTchnfOlf-QZVfuhi9ZAYZ_lZWtpNb_8bJSE4Lq8LLW0EL4tu4tMMtqF7R2EBJHP2Aai7pPn_ZQ0RJymwVmG1VhAMMQ7Mj_gRcoz7ITvlH0SxRmGKuKpYCEVRhBdSzeAHt1tCmrd4Hhmo7V2e4FVHASdIX0ZYlC4Xo75cxjg9RGVH_40ePgNsBiOP30Kv7CsZLHZPH0azYNO7N9q5con-zs55ZTtVcPKVy6121py14k1nvg0KXUHZ-p7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7pBrg4ZJ1nM1PC9VKlzBtF3azMdmpafUahZiX2yR7M7futv8OQZB8sB5UjXzaQxZbRqF1GFFswhS0yZ98O6WF_IS3yRPKyZmw-LjyOC8XUeMFxXcpKn0gJQpuIs8rWd0WDA0aQM31OfM_vLg7idLDUZEe-D1-LtcqoDNXOnDzR6__Nredn9eEigoxQgB8Dvx9veieH4Puzp_919iygbLkhi176U-S3eqKsUfhHgKdOMleiEWMpJZ1pbGIraaKfQGOfENgpdb-Ms0XFEWnGsdRCJk2CyRQUNGDpyejKc629asmO57UNekWFR5XEF8FU1THeBIizQwi63nrEqxdY8iw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=L9JQpBDfxSWu95kmyhpDdYkwKgXSMtI7U5nU8T34OBPfBdOfmvkJylqCUz9Rw_D6TEiBFL7vIzzrRER_u_HuJAGH5DjdtqljFOl1KiID45Cv0okMI1avvbuxqZnUQ6O0PQpoQwrPzPcFfI4KfllhMcvK_R0fIzdLU0_Qxew-QFKPviV8X4BOxAau3HNVqtHZNarW39Sc1slvUjrSrtne90a_9jQiJ5lLabQ2-P3684G_4xM0Nd6Jyx1QYBfV_ZetK3ID1i-rVoQPazs5D27kW9xvZbmbqXA-v7zFAcqB_j2REqISced0UF3lxPK3VAoI3LRG-3DZ43IvpMabNtZ98g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=L9JQpBDfxSWu95kmyhpDdYkwKgXSMtI7U5nU8T34OBPfBdOfmvkJylqCUz9Rw_D6TEiBFL7vIzzrRER_u_HuJAGH5DjdtqljFOl1KiID45Cv0okMI1avvbuxqZnUQ6O0PQpoQwrPzPcFfI4KfllhMcvK_R0fIzdLU0_Qxew-QFKPviV8X4BOxAau3HNVqtHZNarW39Sc1slvUjrSrtne90a_9jQiJ5lLabQ2-P3684G_4xM0Nd6Jyx1QYBfV_ZetK3ID1i-rVoQPazs5D27kW9xvZbmbqXA-v7zFAcqB_j2REqISced0UF3lxPK3VAoI3LRG-3DZ43IvpMabNtZ98g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=RSnnAWa-tfTJVa7QPi77ysHC7pLSxcWPBhil22-SPXN2cv3ivzq10sJXZXs8dqOf8wSCEFBbZe8yCvHQyeLt3EIC4R6dpz3M1iqwDdytX4r_QdcznMuPNjmwl2KNggd-6Wm55JfeNEuhglXkdGJNMFhS2tsdtsP6JsToCAhs9A-z2ZhbfKPiBz43cd2in9bSN0i9eYkqzuaa_O2Kmw48aZsD_-pDzYUIvcshRViGTrH0QH-VKdbVYVq2ieCTGtG4y3r3-m5lNc14m8O1mmfiukY0-IwJ8l0q0fUBOlEwaaO60_Z6InYihLkxTzpooGWAWbcAhlQFW71a8fwq0JhquQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=RSnnAWa-tfTJVa7QPi77ysHC7pLSxcWPBhil22-SPXN2cv3ivzq10sJXZXs8dqOf8wSCEFBbZe8yCvHQyeLt3EIC4R6dpz3M1iqwDdytX4r_QdcznMuPNjmwl2KNggd-6Wm55JfeNEuhglXkdGJNMFhS2tsdtsP6JsToCAhs9A-z2ZhbfKPiBz43cd2in9bSN0i9eYkqzuaa_O2Kmw48aZsD_-pDzYUIvcshRViGTrH0QH-VKdbVYVq2ieCTGtG4y3r3-m5lNc14m8O1mmfiukY0-IwJ8l0q0fUBOlEwaaO60_Z6InYihLkxTzpooGWAWbcAhlQFW71a8fwq0JhquQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=cdlIGB1T0w3_Nm7sDwOXmOTXpg4hmQaegPxal-wNWH_SB792tUCaLQiSYTtlQdHDV58CUatFGy_f26t58URHcyVuCQaR7J2LizhZhl1Aigy5pSucSY3LeNvJBhrLoX5ruoJXiUq5fcr4g68QD6aTnKjqCiIJKNrO0D1lTvsohrWgKUH4_Ia68Rx1qEUreyHpbIvhivf0tUl5aiJgGbX8FakRCEzpYfJiDjtoQTcg2u3WyeMQzc91xURtvvptx27-itK31PKCTqwOObrppkiPQAH6k7Y9urMIDLVcBGMNW-Fozo6aUFl0Fx_rldc-rcyqBMN8C-h_efBjlgm_AVvOjj8qEHrZex1orUlPIGfZSc-YsPwNI7Hdn__jDG27jHTiN2KJs8rtk4TYdtmxc13qwei-IyJOX7Qr3On1fzNLqLh73i4B-qsVY0Jw7Ur95FKSbCKMifRDkaKYhk_qfClPENfoAuyRk25tzyyubGo4_ju4nyMvKVRoBhN7Ekrq9CKS4eASHv8PVwWngjBmedbtPwyGQAuZHQxx7eKPQYr8q7iWTknX_yus5PPawNB73q3cCjkrXSt5iUQ4YlMDo-E29YkIrxXcEFm6agh4xQArsTSmDngpG0BDy8uJ0NPnToYpdLkOY7rEiQ2xeBVuMZZBDAdHQhQ3WSZYumZKcpV624E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=cdlIGB1T0w3_Nm7sDwOXmOTXpg4hmQaegPxal-wNWH_SB792tUCaLQiSYTtlQdHDV58CUatFGy_f26t58URHcyVuCQaR7J2LizhZhl1Aigy5pSucSY3LeNvJBhrLoX5ruoJXiUq5fcr4g68QD6aTnKjqCiIJKNrO0D1lTvsohrWgKUH4_Ia68Rx1qEUreyHpbIvhivf0tUl5aiJgGbX8FakRCEzpYfJiDjtoQTcg2u3WyeMQzc91xURtvvptx27-itK31PKCTqwOObrppkiPQAH6k7Y9urMIDLVcBGMNW-Fozo6aUFl0Fx_rldc-rcyqBMN8C-h_efBjlgm_AVvOjj8qEHrZex1orUlPIGfZSc-YsPwNI7Hdn__jDG27jHTiN2KJs8rtk4TYdtmxc13qwei-IyJOX7Qr3On1fzNLqLh73i4B-qsVY0Jw7Ur95FKSbCKMifRDkaKYhk_qfClPENfoAuyRk25tzyyubGo4_ju4nyMvKVRoBhN7Ekrq9CKS4eASHv8PVwWngjBmedbtPwyGQAuZHQxx7eKPQYr8q7iWTknX_yus5PPawNB73q3cCjkrXSt5iUQ4YlMDo-E29YkIrxXcEFm6agh4xQArsTSmDngpG0BDy8uJ0NPnToYpdLkOY7rEiQ2xeBVuMZZBDAdHQhQ3WSZYumZKcpV624E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=hUsJgJDbcyuhfVhgCijq_Ascq6RZiaNJn9_HUxs0_KI7PnrvAB5Yo0JvHDqO4Z2RFsMR9k8-Ux-SIPooMlW7a3ZrJuMGHLgqeJ65R8Wo35B8iifeMaGLTNtAxuF6OD0AdIuLcH3HgAthRXUF3RNc7wl3X94HtD1843D4DRP2ud-oot6gGyCbHa88GU7W253f7qC5cYK4ErX5OsimNPyc8X3fqR1ssdQ6Rtyp7CGdf7VZUOePFVA3SgLl3pcc5UFUgvpfAeXlBVeKYzMfjpZniXhJ-Xw9hv403yXBuEaN46Fi8QVKtHXJUOiPnl25N5nWEOyyHrpSbd4GTavYSwjOKS48ro2VlKY-LUE3lfx6qimDq8gvH7M-4Wv_7XpQL_qmOk-jMkPqHyuVeVlvMqE2KsZUcF7SEOJ5HnPQD2UydT_xWJzT9ys0JoZkrj5iTso8XQtIxXwrPZVGBSu8_24LhY86Ur7W4pmjx45Rgv_RMfIYq8QsKUIzOG2AoHBbdhvfyg8uSgIjFZ_VZDJBVhviW-Q94SYBFkQpoeI-yj6bw7QBJkNEIY_4PNHQlOOUdhv47kqhf6vqLgVSNl8bo42oKXUXkt3WAacIs33V3pSE7MR_BoxOE5KZ7SSsggh8Z1NtUAQ3ewyrPWqCU2NqpQPHCfZ4Yyy5IdezohO-c0Xgu5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=hUsJgJDbcyuhfVhgCijq_Ascq6RZiaNJn9_HUxs0_KI7PnrvAB5Yo0JvHDqO4Z2RFsMR9k8-Ux-SIPooMlW7a3ZrJuMGHLgqeJ65R8Wo35B8iifeMaGLTNtAxuF6OD0AdIuLcH3HgAthRXUF3RNc7wl3X94HtD1843D4DRP2ud-oot6gGyCbHa88GU7W253f7qC5cYK4ErX5OsimNPyc8X3fqR1ssdQ6Rtyp7CGdf7VZUOePFVA3SgLl3pcc5UFUgvpfAeXlBVeKYzMfjpZniXhJ-Xw9hv403yXBuEaN46Fi8QVKtHXJUOiPnl25N5nWEOyyHrpSbd4GTavYSwjOKS48ro2VlKY-LUE3lfx6qimDq8gvH7M-4Wv_7XpQL_qmOk-jMkPqHyuVeVlvMqE2KsZUcF7SEOJ5HnPQD2UydT_xWJzT9ys0JoZkrj5iTso8XQtIxXwrPZVGBSu8_24LhY86Ur7W4pmjx45Rgv_RMfIYq8QsKUIzOG2AoHBbdhvfyg8uSgIjFZ_VZDJBVhviW-Q94SYBFkQpoeI-yj6bw7QBJkNEIY_4PNHQlOOUdhv47kqhf6vqLgVSNl8bo42oKXUXkt3WAacIs33V3pSE7MR_BoxOE5KZ7SSsggh8Z1NtUAQ3ewyrPWqCU2NqpQPHCfZ4Yyy5IdezohO-c0Xgu5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vGIEJJR-NJGR-ApsSKafNsDPtjGI7MRAaxcTtQ53VAvwxlP0CErEYRfP_2-rrO0a5TjKh1Qem7FHchLiBkGdKQV9V_c8sE9JSJswuAoCAqAstu7OsPogLgj7Hjw8pcB6G2sDXxoIFtdf96QWQ4sUARATHZtNtnQMLix7isBB-eG9tNZzaG-MQiJ5C51aE4Pds-WDSxALAn0XecZR4K9vCXF_PiYPbb6cjiMbFFGADrhb_CetEBvqKCP_8JIk1nuAoSyv7PPyM4-JGL6Jxz8QTXUQIkr2jt0hCgcOwSKxVMjt_Q5930HltjNEwGr-ld6Lml2ddTW13S2MQwdO6sXgaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vGIEJJR-NJGR-ApsSKafNsDPtjGI7MRAaxcTtQ53VAvwxlP0CErEYRfP_2-rrO0a5TjKh1Qem7FHchLiBkGdKQV9V_c8sE9JSJswuAoCAqAstu7OsPogLgj7Hjw8pcB6G2sDXxoIFtdf96QWQ4sUARATHZtNtnQMLix7isBB-eG9tNZzaG-MQiJ5C51aE4Pds-WDSxALAn0XecZR4K9vCXF_PiYPbb6cjiMbFFGADrhb_CetEBvqKCP_8JIk1nuAoSyv7PPyM4-JGL6Jxz8QTXUQIkr2jt0hCgcOwSKxVMjt_Q5930HltjNEwGr-ld6Lml2ddTW13S2MQwdO6sXgaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhjCT8ezMMSrx09cVcoO9GcJjUyP_fD-1r_bGLJMI6myXmvAvpcJf0vyx937wVxd327g1q9MV4Vn8DZ3Bmn1mn0fRmtgkzzmBi99dzWJNA9wXDZQXK85YdHMBpEkhuToKrDc01LL4mO8NMc1KQMnbuZCHv48WZcZgV4QXwIpYbALhDkTbJOe7Lvu7VcDRize9qHnzdUfaTMImtcP2j0iLVJPHNGaeSY9exam56KfJmqUYfCMiAIBQ09THX-hWloxNLS6iFT3L5Y4ESRG0Ge0R6aqtlNfjsa0-A2iJq56a0GDGh2g1w9Kgsk7VC0W1FE7WKKregIQWuH1SZmedsjLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=r8BXllVbQzw1MfZS9O3jstB3YRvYHdPTUKgTidAlJHSgeA-H2rGVVypR_NIvYq_2Jzm6LzClHKW7ql9ZE4PKoUL9IRSKArBh07VxAb2I57VJLWATHJpQ0Coyc7i1sgHjI0mpakcg1PGlzaWzi3NXxQjpkCLlgDxhAb__2SLeXRhtHYP0Utr4zBCNrJBhjm54VM1lPKofOdiYmgtfTbUz6K_stluaDuJHtO15ch9933of82tyUposnwwbeGI-mmO5FXQ7Ac0XEzTmnmTxEJnIHdtdH1G9WU9yOkiOKlZEiJ1_fZGrCl1fxVncp9KSMl_7w7Jc41jwpjYkyKjStEtb-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=r8BXllVbQzw1MfZS9O3jstB3YRvYHdPTUKgTidAlJHSgeA-H2rGVVypR_NIvYq_2Jzm6LzClHKW7ql9ZE4PKoUL9IRSKArBh07VxAb2I57VJLWATHJpQ0Coyc7i1sgHjI0mpakcg1PGlzaWzi3NXxQjpkCLlgDxhAb__2SLeXRhtHYP0Utr4zBCNrJBhjm54VM1lPKofOdiYmgtfTbUz6K_stluaDuJHtO15ch9933of82tyUposnwwbeGI-mmO5FXQ7Ac0XEzTmnmTxEJnIHdtdH1G9WU9yOkiOKlZEiJ1_fZGrCl1fxVncp9KSMl_7w7Jc41jwpjYkyKjStEtb-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=fz3muOYwDkoAdFmQurVHgQxwlX_5SxdRKJOVGqFUDp-g4b5YQqNZKxbsFrlp_nWHUPpmffOiHZeByWQ0L-oYTu1mINfZ2hvH85sasFqAqJaLJdF7b0BPA6uFzf9Fq8DpI3qQbHDtMzj3mAGKNVvgajEbXNw_tDJq5R9OjkMimdlwEBJzD-1E7EMTSrfEkGC_eGV0cQ1jc_xjLub07EYAv7D9hfQJUPs_YAGShiuOxtBNPTYGz3HkMfx-sgXXrhQ5T9gTebEaNiNXv48PHRzJAKtC_lvemb4aGJKi-zSqzn25RgcrgtrPAw02WzUKMDbycwnW3HR7hRUab06-fIrvkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=fz3muOYwDkoAdFmQurVHgQxwlX_5SxdRKJOVGqFUDp-g4b5YQqNZKxbsFrlp_nWHUPpmffOiHZeByWQ0L-oYTu1mINfZ2hvH85sasFqAqJaLJdF7b0BPA6uFzf9Fq8DpI3qQbHDtMzj3mAGKNVvgajEbXNw_tDJq5R9OjkMimdlwEBJzD-1E7EMTSrfEkGC_eGV0cQ1jc_xjLub07EYAv7D9hfQJUPs_YAGShiuOxtBNPTYGz3HkMfx-sgXXrhQ5T9gTebEaNiNXv48PHRzJAKtC_lvemb4aGJKi-zSqzn25RgcrgtrPAw02WzUKMDbycwnW3HR7hRUab06-fIrvkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ygz2dVT4E7b6EZ9RtJ_XvyDbBCXsg_ua0l8nyS9TEDbrUEDRIFiCJIJ2z0ekYLrARsOLltxZyLCr1pqAIRoTGCaHpxBTVJgIF4p3XfGtQy6R9FEeZTbmIIOJ68R1hhLq5-54WDkSK2ahTO9gwYLNurRKv084rNivgkCA356i8Gj7lWnC7awBiQIY4AQUTadRL1pQGJabcc7nCsJr-ZmU6emDJoHkBlKDMoP6L-tTSU7BvpfYNUizISy33fvllRVrrmZSd6GRlEHUwd94-JeoQz8QttN5e_UF_0FUPmd9dG-ryfFJkCkY_AJiUCLRN8vSor84l9MyVW5PmlyJ2pLbvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgmhMGlrrNddVItccqD0mhZecI_XnvG5j6HQ3ZXknr-haoOCcn8Yv08g6yTl_7a7XIDzB9sqMXCctlJb50iv2osMJjRZknOSTGD3xxnXzMTJ-JoE_MkWiX1VoeKbbvHRQudDhh6qUcFUIbJcTmf_un6Vrqy0FW5tvp_bpa9T0AGpQgik32WRFTCNLwgI1FxBrbfY1QuiP7E23TzxHC3RsRzjI96BmHV-lD9gOv1bybsFHyiyOsX2aujWeuv__rxCnXoQkskUdayoZ6-0RkH4XTEqmx8yO9GdZzL2RFfelvBPWR1k0_lkUwx-a2x4ki0Lry3GxSsx9UzDeGVv87zVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHxs8UrOfANb3wLkNGJzfXAD4CKLz8JIbYlaiPcGmWB-jwuDiGsUDdba48duLfk8ZcBXELt8UgzYXvcx4OI-SP0oGUQbhOrraBYqU1-AA7siUDcwZPRfqVxbVYoLBOFRRxdHxz1TnHspmt7zdZlGB-Ejn2lIXIAyfDsEMMb3EpBqGChzNyEbKXCw37-Y-ihBcrl2cYOAPFUYlE_3ZnFAyfEA5bOTtrQ0JtuLHof02LRGtpNZd0SZ4G_99Yc6wc2fBoXohKTBNN23aawPIySc0WVnRmb3GU0-DB5q5TvwBnfHPaDJFvb4mJHxlM90LqmTivwbJeaG7dUEe0y2-j-9Aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMy4CQmNwOXRDOKNNViT67B1gOrvoiMv-RCVTmSxg4XY1QcPx3n4nuDXf7zm_KX-pWUnKtWkyEJb3SQn4KsUHAuFoKoKC7Ljh8wEG-MLWfU3VNv2zXMl0XMd75XUc--shYV0yBmcnkaysqVNFjDk2zytPQ_lmREOsn2hZVQd4JmIOpPv-hSrqOZRgUh2Ccf0V2dU_K1qg7AckUIGXdpA0zrotYPQqoCDgV1wPIWiwd0exyDcr0ArVaT3dfiMfwum76KKfmxojJ-EWYzbo-xYzjwSluP_Vioz0ksDuIFNL4fbMRKZa-I_k_VD17RwWg6jwUhBNLYJ3jASbo80Yclmuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8wYvJFIf3NgnLU2oxbWD5FN0WECBSEIz58R_9xj4VQJRBFuhBagRRcv86HfGo8LkHjKjp1KNnaHb10cRMPS8s92xgsf8FfGeJJbNr3J860YrGQK21zSQTdpyCA2esgJC2b3ZYtjioUuUp1bwisNZ2y_h_vBxj-lsP1lWeDkg4QpDALTVoZeMYuN9f_JilttXteqw_z2FjICnRGWW--UjZbCdkZdLg3LJtIoK1Cigbk4gkSwThx2qcw51NTkSbPE_-vJTlg_1Arxy6lN_tjE_LKhFOdbwOuNPNKAmv59WYzyC7VG2J7NSuNu5TOkWGYHIH1kmfyspnmHqMQPoSJRsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMfdhmDlusYiDN7yb7ZrWWQ30sww8MaMcHppABNZ6gQhUnVM5J0jqqNXU5EbGss5wmS8hqw0XDMAg9Fan2Q1SsU0kkFUQFFMgnzvw4HkuPKUfswV0g6VmQmY9CwawKWKpP8FOkDQ1rLW3g_R5OWQx9MUAx-mqUHkcSz_r6ooIYSv4zhjteSbwReAHmQSk_Urlz-qHCa8BI9EnzcTdWqecmmYETojdQf0-xYwD4osCpykmnBwDdGToQFiVgc_8B1i0uswozjqk6wTyPvSbCEIu7d-ArWkCLPyHG5CVBz7n3TO2R3xuMGJgOm_0bQDA439c2ep5foKyjs6COBT1sHr9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koeM25wzyyM5pVD4Y-OBJPzhYUsP45fM0L_by1zicWXsA0uppqRdsPDaglx5wG2OG-9Q29ILtoJFR_WQ2qazQimncfpu1NLQ80DgcrhdVoQPt8aLw0uNEgp3wU1rJQN5cY6X9nRmW_y4U8VACNaEXwLhMXt5ry4R7nkHTfxSISrfkfJAtbvoXv-0yyQNgLfvz_d6krIcHSZJX3bf65KoxSCjZxq0gAAbJgzxVTqfFsYdnciaF5qg7ztLip5trZlHNnQOp2-VhfG2Fw1eXqh9aWMTnkyxqRtnrtqqcUlpM5KwwX75JIbsS-5f_CkGUN8l7blVnK06uskPNXv2I0JPMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPUIXdITC55gUzUgYpcrlHyAHJ10_OQukuV5Tu-SMBZQvPJ_vf--s9sLZO1AGncl48T2Gt8US1mQAd60lJXCvTu0eSa61RPth1ptNVp5fy2n2ga8rc43V7owRncgX2s2QRcbk1m4FLIUz_8Lzcnvm8vJ0RJRowviz6N58mWZJGFHwPWAC3BxLtYlNeJzJFvtB9hUVztE8NW7ykS4O2brzyc-tkfCFxcvztw9X0qDMselZVTKVlKAPkHG1dvGCzi5Vsi-Xsxpgb4kCxQbeBxB0-KdoxoGEefpX8bcrsb9Qk8EjC74T5Ky0uHnmK2-u0ItbhJ1D4HBIqLm8JHNk3Z1mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PljtMBLachW5ArzKOgeg7uEUCz7ybIYFjAaPk0c3inYGvejVy4Atj3lYPXh-kIPLfFstFkEXYLmkSTUI7xa4fiMQyFmkw9rWuToRnnz0XJMZHhWPD9c-RpX-FmdI1Aio-7A55jBngjrJXCkSRpQF3dJuRppVV1-8mVQY3uVNXdtKtnHAPKasknHdHkfyaFp7yjmSd21t1em76VtNg8tf4R9NY1_Y7WZ8H88Fcx7Ci9g8mPvqQGkR053FGpr7s8Kr3ZeUMU0FfwWOB6xDgdh6O7RMLekAlVOvxFdBiVXVIiKrusvj-vUj4DLp0k1zoaExbXd1qjD7xyB7b03j1wX2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JutCT1M2a5IJQUV_iR-PL71FPIwh4X-OJ1n14zaMRcvYIl7wTtAxymhSwPud6ig6agZ2OlhQSXhy7RqwrlDa2c5UtUE1S1UDqX9YIUogADyoip-Lql075p4KxhHXYtWYhgZR5snOWNRkMJpUm3HyIJpwTmbHdF40iAutyo6PGxKMQUWcxlERibEEOjRYpRMCXOrD-0Lld19meWMPLiK6arAMqvJbF3J0Blw5EAbbEAPc5Q_y6Xm76_XF1DR9_3gPVMkWCnCIQmVvVAVjsadmmQTX4UHfrw4uWhD3C2wpwaXtjB9rbf35Z-yAfr-9BkW5zDSu1vq-m_fEU6AbZhnYBQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=PVrn3PA5waEfpZo4G2JwqRyTpf08tnLQvaqYOdg_-Ninqg7ViNC6CXOb7xEgiTEhIzrpiiGe3As3xt0zOaLuwncIzlwxAFXzZXP7SHVOReSbAhAKoBaJKWJNXjKLkotrOnO1wzUb243e3UpTYN91s5O-R36fhFcpwxQE5logJCUsJJiSSv9tbWULnvVcOwgKbyTS_g3zfKOqhKcxqiRdnKco1KrXo30BYw6ocToJMe7yazt651G728_mIa0REd4HAe7T4MUprSnwVAdMlRt0orDVaiJbaSL8CcOohCcQQaDFA5TYMFOMlWL8G3UXo7Zlh1RoTY1g_RLDXiybSnD8zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=PVrn3PA5waEfpZo4G2JwqRyTpf08tnLQvaqYOdg_-Ninqg7ViNC6CXOb7xEgiTEhIzrpiiGe3As3xt0zOaLuwncIzlwxAFXzZXP7SHVOReSbAhAKoBaJKWJNXjKLkotrOnO1wzUb243e3UpTYN91s5O-R36fhFcpwxQE5logJCUsJJiSSv9tbWULnvVcOwgKbyTS_g3zfKOqhKcxqiRdnKco1KrXo30BYw6ocToJMe7yazt651G728_mIa0REd4HAe7T4MUprSnwVAdMlRt0orDVaiJbaSL8CcOohCcQQaDFA5TYMFOMlWL8G3UXo7Zlh1RoTY1g_RLDXiybSnD8zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zkv6aDWOeu9_h2wpQoyKwWPcBEjSZ9n-MQku6vq--E7E3EpKx23BXJGYP8olPbvgNXZFi1sbryi5H5jZ5KVO4BLAsF-mF72p7GXKflwKHYS3LBoHAO1FwJyzzDwGTf5RCbBWbbkS0Nm87eGqfxhWmmxW326q8KoN5i7uSdIckoendMLFjzEBtherSFhDAa_lnSe_MIrdVxNlIX8LxLw-CbUrBG35zFONbPmsUkcVGjUNzdDyBNa1sNxLcVll7qJfmd4EfEu_Y9O3yt2h83rkjUREvOAkSOR2ZdiFXdtbjjPJSyKyEz4JrMr7m8jv0O8kDfsNXDK_Xv-HdTPSF2-oEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6jcZaBkZCxUP4mkDbmcHlhrVq2mwcjTLli35QikWpAK0HTCI5fK1Lk0Nz-AgnBxbjgOReiZGvIcwF0r1lm0iuKqyiCOHML96kWX1yGdEgDRA0EsBSWOvtJ_TC_iRFW2WIqLxnixOMYK-_aLEGQLjx2rutVT-EjgBzbCxcfkrX3hmHipWJwYwLhJJpS3s-4y5udCIFMNRXJSS59qmFB3omnGaG6DziShtmxX58euXMQMF69_192WTzk9p8_XPktgHdZFF-hvALaGB3RrCQXk2oq9ckio0aX3o619yJysfm21d0IzJWVAXnjsZhhfjINLWgmB0UIlZZ3w7OSRfraSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Vavucekbdb5C5Bem3AGD4M8bzv_Q421Gv-4Zpb-NrMi9KJHsXIbsy84viHwfIG_05BoCLxZVePicfoXK4PqWIkr0caYoyJbI0NltV1V3HRpM_b3pVrD2ioG5KeSQwcas_zeS1v7KHzrPC_u965f_oicHLzpX-hVwYMqwZcTNqIueaR32-N9Jl6v3BJ0UMLQGJFV_i-GC1sYmMbtnIBt1F6CyPhpg3wuE0yOYvND70P31_t-NZNXbL2zyAaQnfHTEZDqu7_i4kZo1BfK6SY4tuMcOk9Ol2mGYChE6a-00A0_yLyvewPGHpHjKR-Efn8HOu-L-GisAHFl_oZmePfs35w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Vavucekbdb5C5Bem3AGD4M8bzv_Q421Gv-4Zpb-NrMi9KJHsXIbsy84viHwfIG_05BoCLxZVePicfoXK4PqWIkr0caYoyJbI0NltV1V3HRpM_b3pVrD2ioG5KeSQwcas_zeS1v7KHzrPC_u965f_oicHLzpX-hVwYMqwZcTNqIueaR32-N9Jl6v3BJ0UMLQGJFV_i-GC1sYmMbtnIBt1F6CyPhpg3wuE0yOYvND70P31_t-NZNXbL2zyAaQnfHTEZDqu7_i4kZo1BfK6SY4tuMcOk9Ol2mGYChE6a-00A0_yLyvewPGHpHjKR-Efn8HOu-L-GisAHFl_oZmePfs35w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=TQ4hxzz6kdKr_sdhfiOc0Ljru34maHWCrN2XTy9QrRahSkwwoBSF5wilKEDbxkqbW2XAYX-xqEsjvulm9l12ptDAymxCC3LHixafPfixnVu-GfquOzrcd99PL24RenXWYzCQsfXEv7mUbi_wkpcsQPjAcxPJOhnUQ7Pn638-TfJupXHo-Pxas-2K6aFV8g3CbWLfXQKxI6GQL9nTUS62gsx9zh54fjvjxldp_9BRgcqDEYzTE_tHB7KriUhbkb2PmtpBU2JfJyjDuo_EQoIbCEWpFI0M0IgkjzJ7RVk1sf-zyclMgxJLlSCPcaoxTf7KGsRk2TfiXZKiDLeWsqbFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=TQ4hxzz6kdKr_sdhfiOc0Ljru34maHWCrN2XTy9QrRahSkwwoBSF5wilKEDbxkqbW2XAYX-xqEsjvulm9l12ptDAymxCC3LHixafPfixnVu-GfquOzrcd99PL24RenXWYzCQsfXEv7mUbi_wkpcsQPjAcxPJOhnUQ7Pn638-TfJupXHo-Pxas-2K6aFV8g3CbWLfXQKxI6GQL9nTUS62gsx9zh54fjvjxldp_9BRgcqDEYzTE_tHB7KriUhbkb2PmtpBU2JfJyjDuo_EQoIbCEWpFI0M0IgkjzJ7RVk1sf-zyclMgxJLlSCPcaoxTf7KGsRk2TfiXZKiDLeWsqbFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
