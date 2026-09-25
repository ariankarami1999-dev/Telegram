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
<img src="https://cdn4.telesco.pe/file/b9s-RN8kRvW2RVoF1QoeuwceXtl7CZItLZb9Wb3h4ESIhgY-m25D8oAx56M3RRAv2w0qo_XjuYFkt_gyqELFmkmf_ainJUQ6FAsuYACNQ_KIXk1HevwSedC4IR91bOLorpDoC9r3XX1ljl-dngP2BYgwyATi5_PcboQQgS7yffHR4RgZcosNmWZ2JqzSv6cshEOvucud1Ezw4eXmiAOkmiefQ--JvEBflNmoh1FlfnZvg7rXIzGpAt1ks1Ei8aW0-sbV4NpOZPi2dwgpdJ66X54QpiJbTSzwhj8QHto8I-QSEHzSP6qAE4vVS_AQNYCWdLuzKMrJudc7w7wI7m5y1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 04:31:48</div>
<hr>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbiOMZLg7HXOMepqETHT7-HKC0SRMuzv1S5xurSETeVQlFnjGx8Wl1yKmDr1PS0HaAHGdEkcGDDGjZTxfc_ZBod-xRmyLL9ldU0bfgwU-3Tag5r3p3rNZ3K4JgfDlliLb0oLxLiz4fcYu81HiHDrLUcLSGcrQe5VZkQwaEOSnu6NEdIzTC5SACjWvWsUAmr95a_yUOg19M-4_o4pZnXWf8Q0cm7nCPpRmKTrdiSvWfVbNlz-pnfHBxE5qjzHDN_vzBqAgY4456K3I7nbH9N95gfFUQpkDGO07whk6_36OLcXTzRjg2dLT2jFWUKBsogSsNmcvFfi2X610rU3DFR_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAP2_SuzT4o8HAjzuGT6aEAmtk1kifKUrGw4E5Rlb5gle6YAcvxoGOhRwYyM21PS5Y3P8eM_TKmZ1P0jeV4tisVvGxspPn9MiRWTB0DhY7sYw6Top_6WKFu9opVPpxRXcNflmF6-8EfhqJHXVJN8BJk8WqQ825J0ZcCzB5yuq_O6eq9iuXx_yc4wvISCFqQ_NnKP9JkjV-rHP7nmsm05_4thJdow8pMBjPC3zQmjJmkdQ0S0Cxkw9qS_nOC_eUs0PqQthzfDlon7iOnn3EySDnPZ0ydbtb1Qs1k5ayN120wL5lysQVIf7k0X4IYY_CSKh1kKLTPNxHjTu-J9T7ChhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ_V_etrGfX7y_KWGMZ2OHhzQdWetYlZtFD39SYZPXxf0ddF_wh-KERjWdaeKfaEwipgVCkeaIkLgnFrADXoF1sqDkXalciAEkC9hxCMxtSBoetTs8FbCalCRb76bUoQa1WI7izA7OVZwCgds5rG-mdL9q20In7IXjCSNWN6ufuok2MPz_i-eLOm1DkBbJ1_hs877IVJ2IYIwuMJjHOQ1hz2jO5p7Qs4BrYBFfrJ8Qcbj893Lb1qoCaSMEmUqwPMpxlmzVvAe3sTg1w8736ggJsmw6G2J5hq5qWV9SPB2ykTpPp0NT2ujqA7NYE_-QMFdm7GFCG9hmF0VSnWUJxL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dovRQ51uMJ_6XC0zS0KZqgP5RIEsU99ZpGLHCjOJMoutrx0Wno5_iphohgLzNi3GHxcC8z-U4c7kVDAFPxavUZDirgdW3NhIEp4UHc6QeilCnu7tr6qlnxydLO8YX9sCO5fGVYxNLtbWtYzrrcIRCmRtSyLSXb2N7Sq2WGzcMmzaZ41sdHx-vYpZW9e7Ffd7YO6ItdLmhEVti8Gotz1TUlEm8NcQIZm4er9Fss9tlfqG_uojnwTKaZyet4Zns129IFHu6Wdo7FkTRxjsHzMT2VOWkKfVFCHT7So7tB24fJsWEZlAJ-u2EYAIAuAM3nlZirrFDJ1BTgcVr1TYylZy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpWU3az-puMY29kjql033-BtFnhFoFaiI189f2dOd_fpoalCCtL1pPe8VutJuH0Pp4-DYRqt-Jpa_zUqIQnVi-aJmTVPEnFOfVa9_KSDH1ggjY4XHqkGnsg4ADK2BKcm0Rtx68aFlp8uArTzY7S0vLx4fnyMHjXg7RO2LACYhPmIXj6oOsew63uAkzGLjw0Fk8qqhNyqSbymPzoNM2RSrM-CqkbSmSMGf3WX0u5pzw0m98Tkdo1qOBWK3os0HguLUhIF6v_fsey4UdhaM3k9dw1mmvNC-O5g8RwZXDNp6c3oIDxexQ-FiDm6zvmvX0OhYzUYfftMHf3ft6F0nUGxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctYfbyTiF2qTBDAwkzo8C2FrbwGawJBPC1v66u3Cbw3V6ExbuX3jlA7os6nS6N0Yy1n86OqZj_Diha1o3FjA8vJGkTYgCSCX8Sg4vfP_mOYiZPlHo8YoFfY5UJitIlzBXH6uf5kZPt09qtgRMBLxFBg0jH88xTxPMyahhVXCwuvO2zxgabg6BFWcGo4JuzVWG1RNPXTGWGfZX3b00jENZiAL81F323cHoH050lP000z26YZwIBPbX1iu72Q-2HxVyHRlUe5quNFu1bqLTc6OeGk5U8Is90M9RqSxts7e4O4n-WBXeMpsMOuXtma3WWtPL2L608U2IovMb7aLeY_xFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkqWAyUb43mh54WGuDBa1rooY-AVEO8cLJgMCKsfKZG9krXma7pJA0RvAAwmr746Ew5dch4YudbQZrtBZPnctBLuU_ntCCjTyC__68XqWFiSvIGxorN8XQ_AVeCFsMzADJSAWyFHWl7Wos080UxnCa7kXN1GH5L-tfgp4kAczBPatPTjLLFeqscXiyGh4PbBvK6MgJcOzhJAdEapyHl26s-WpixMhi3EfU7Mg35nZfiIwZDOm5EVmVD0laqphkT7ktBUWRdDXA-84eZ_x6Q8lICDXHBsyjIJ1tSKScRp8YAve2vYMWtqbXtdBgbJRDCA9lokCMLLTuZkevIONfeUbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5ZAkmNge82VVakUu5Ld3LJaQQJMCLO4ZLjP1OKM5BrFAr--_mmGwBFkW_lJb47bu_tX66rFG5oXqgoNHS4AfLsc1OwT4KeFga8Im7_YgztmYmqZLIZEVnoThJFVp2qDeuadvZAzXeVQSBydSDtQvub5VxrDfTyZBOMJhrRA8OD3pdf-nsMqYj3tEUYsGq-EssQi4UYidfItDmPTmslTAGgrbcOB_-vZKuOEYJSdKdx38iuyHjxpt5k3Fycoyd852UNu-MNBNIBYW2M6zjhZdDHjrn4Ukn-AE52Id-F-TfOK8Jjt2t_wVBEytvIkldRJleFjtePY8QcgAH8fioIiaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=N7l-gS9LbsjtOBcIemoVR23GPU38BT9VNyCyMEpWVgQG5ZAeHCC1wRviv_HnLZtTV8c0p05JeQXITw6oT0i1INT9CG1Z2FUXhYilIdhn8QCOWuM8mmiQ1MCppscbfPd0UFP9loOCb2OU6T8mp1AOJcjzSLgkcwORaALXPuzHRk_E8N19qZkbQHSbKcYuxgSaIKrQ15nJc4KxZEW-YHIyTTyYpjVCSV_ErYbg2fqop5UBU5uqQofFCKCwrL-Z2amXVjxsG36l8fqGqH4NU2xK-xU17dZZdmIkmDOQMaDhLvzJQecv4qMo4TV_f1az-Xc5EoqqXhNzkOkJgqJ6FPndXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=N7l-gS9LbsjtOBcIemoVR23GPU38BT9VNyCyMEpWVgQG5ZAeHCC1wRviv_HnLZtTV8c0p05JeQXITw6oT0i1INT9CG1Z2FUXhYilIdhn8QCOWuM8mmiQ1MCppscbfPd0UFP9loOCb2OU6T8mp1AOJcjzSLgkcwORaALXPuzHRk_E8N19qZkbQHSbKcYuxgSaIKrQ15nJc4KxZEW-YHIyTTyYpjVCSV_ErYbg2fqop5UBU5uqQofFCKCwrL-Z2amXVjxsG36l8fqGqH4NU2xK-xU17dZZdmIkmDOQMaDhLvzJQecv4qMo4TV_f1az-Xc5EoqqXhNzkOkJgqJ6FPndXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ8GEv8H983RGEvhqxxZyRLwrOKs8Qm7t2yCTRJcxVE3O1POIk-15enPszwVba0Ca3lmgAippEto4c0DcxWyOt8JVnooNYOv7lsOqGWQrXkbGd5n8nVNWsmjAw-_abWfvl4Ee7PzrIPgFAsGoKBN3d6XUQCmvCn7FovfyusAIC0qBz0u0-TG2JeBKo8ETvliWj2FwsBQbAN5lUsIGdkyJEQ7FXpuLmrAdJJwWrUXAz9bewbVfZku5hTBpehpBjvVEeCNuEyb2SNDa15GRqrfW-9tIEcuoeMnI_oMd-bTS4PEppIfF5wCSqkz-iyIePaiNtW1X_RxC44oXi6THL_U8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFJIje-5G8S6NZxN8ob8pLKlooEnEiZcn-D1BGCMuw7m2sBrihZWgCXU_7bLfpRJeRhNgxs1L9MLfWZU0-GXfQH4a2hKtMW98HkTRYbuQvfgx-HqWj2CPF3j07iDly36MgiCmVnd3yHYAfpSdKu6IpUHo9wRE_ykVvkFCcP1H8HDZQ1iYrfZ9fDFGvyh1k8BerguW2ZmpT46FJV9bjM1xgToRHASCRsEPu16v_SKkkT7VRQMW-Zkk-BrLOuTK1DXZDRnWV-FZI8iLcpQ6k03cQLMD4UMM40tuFa_rh8MCW79nKt0TTlEx-TPrNU0CT31aRr1l90Aw_Q4ixsc8j1MqOH0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFJIje-5G8S6NZxN8ob8pLKlooEnEiZcn-D1BGCMuw7m2sBrihZWgCXU_7bLfpRJeRhNgxs1L9MLfWZU0-GXfQH4a2hKtMW98HkTRYbuQvfgx-HqWj2CPF3j07iDly36MgiCmVnd3yHYAfpSdKu6IpUHo9wRE_ykVvkFCcP1H8HDZQ1iYrfZ9fDFGvyh1k8BerguW2ZmpT46FJV9bjM1xgToRHASCRsEPu16v_SKkkT7VRQMW-Zkk-BrLOuTK1DXZDRnWV-FZI8iLcpQ6k03cQLMD4UMM40tuFa_rh8MCW79nKt0TTlEx-TPrNU0CT31aRr1l90Aw_Q4ixsc8j1MqOH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=CFixlq-TNS9Gqz-0UpRd9sZSy4kOdfKkMDs_P1R00Cp3-BlKa6Sharko08APKzvuoEZOO_KeHHVPxg6en45H1tZOfwjH_cRu1E95ZTPupatHSxP_U53Hjz5XB_SVhrI7iUEEMc7w_FnQhEFF7J1ehYXufZxcuSzc9Zm6w8AfeaBb-I39sDvgYTvBy_CuqmX1n36UYK2EUqKQ_GDaYrhY-RJHkff3kNTlEg41192AVFz19ODe4JjW1fuJ8vIXpoVRONzJ6rboTQhZHM-VYSFwU9HaReGT9-kccR8DZOKY76FgnSNLfbZ-hAx729VWjLxGl8lWGGMxz_OqK12n6hqBHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=CFixlq-TNS9Gqz-0UpRd9sZSy4kOdfKkMDs_P1R00Cp3-BlKa6Sharko08APKzvuoEZOO_KeHHVPxg6en45H1tZOfwjH_cRu1E95ZTPupatHSxP_U53Hjz5XB_SVhrI7iUEEMc7w_FnQhEFF7J1ehYXufZxcuSzc9Zm6w8AfeaBb-I39sDvgYTvBy_CuqmX1n36UYK2EUqKQ_GDaYrhY-RJHkff3kNTlEg41192AVFz19ODe4JjW1fuJ8vIXpoVRONzJ6rboTQhZHM-VYSFwU9HaReGT9-kccR8DZOKY76FgnSNLfbZ-hAx729VWjLxGl8lWGGMxz_OqK12n6hqBHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=VSfkKSqmvM1f9ox5gm5id0vfuG98XcyX1k0pTeh4Wrfr3VeLnmBhs5x5ZC0Vxbyq1iZXxj3jQjC5S15ZDFaM4X_b06P8dAPWuBNCqsQObuB8E1DgHVLMUoBO9BcCo8eLiALyE7q0CWq5uTSVhglqiVDviUtp35WY-H-LMsMaZnJkSUZQ3Le5QWVSfjp67hBARClL_M3LJoae3DZ8WfUecNFNgCj0oka18tUeybLu6Bh25rKWU6W29CKMkF3H0IRlnTtIowhI9f9zdUn1Tt-YxVGaGnWhQOj0KFnVxN6pjsEi9os1CGT9MWIFNc9v6eoNnJKc2i3rrw7XZUWh4xgB-nBytO4HXDw_LfKBlev3QOLbVDGKAaAOoGEUcIUJzRAQz5aIzb2BdU_YzjSME6InlQew7kZ0IlY6QVVnJ7zr2onUVpNppVq69fdPMdOsQQxSeOeINaKk7RkAqtv0dY39RU7x5P6keUBRH1KVT8C5AS0BunP1MgSUiNFmZdU7wNQOSYPYLSyZ2z33Thf2WjOWZSyBcSLNbkqho8l2MTPNcQRu31dyCw6EJo40tv4LPp32Bk6VQ2e4zFTIWGvXLBQGGVt1xOLT5qdtzCR4o9xh8tENfyveQPC7dBzaFw2EDWP8nBCdlKQz-RWDX9rsQkrKEb7-NXErAhtzJrpIg0Qkp0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=VSfkKSqmvM1f9ox5gm5id0vfuG98XcyX1k0pTeh4Wrfr3VeLnmBhs5x5ZC0Vxbyq1iZXxj3jQjC5S15ZDFaM4X_b06P8dAPWuBNCqsQObuB8E1DgHVLMUoBO9BcCo8eLiALyE7q0CWq5uTSVhglqiVDviUtp35WY-H-LMsMaZnJkSUZQ3Le5QWVSfjp67hBARClL_M3LJoae3DZ8WfUecNFNgCj0oka18tUeybLu6Bh25rKWU6W29CKMkF3H0IRlnTtIowhI9f9zdUn1Tt-YxVGaGnWhQOj0KFnVxN6pjsEi9os1CGT9MWIFNc9v6eoNnJKc2i3rrw7XZUWh4xgB-nBytO4HXDw_LfKBlev3QOLbVDGKAaAOoGEUcIUJzRAQz5aIzb2BdU_YzjSME6InlQew7kZ0IlY6QVVnJ7zr2onUVpNppVq69fdPMdOsQQxSeOeINaKk7RkAqtv0dY39RU7x5P6keUBRH1KVT8C5AS0BunP1MgSUiNFmZdU7wNQOSYPYLSyZ2z33Thf2WjOWZSyBcSLNbkqho8l2MTPNcQRu31dyCw6EJo40tv4LPp32Bk6VQ2e4zFTIWGvXLBQGGVt1xOLT5qdtzCR4o9xh8tENfyveQPC7dBzaFw2EDWP8nBCdlKQz-RWDX9rsQkrKEb7-NXErAhtzJrpIg0Qkp0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=ddFzWoVcW_sRjGd4dOuDQdkwIcGWi3oPpBCnM7IEoU1tVV4o-aNR72wmtte4yxVEIW2rEau5cpdEluRJxfHi42yyG5o4qzg0cPbYWGnBxFsLGOA3O80V2YRNjFh1GmLjPTrOeyMVppqaUSlCdyYQ-MAjFbrwf0ci7Ahg4cOvTEgds3-urMLdhHmNh-NLi0E8taW3vzjEnpDC9pyfSobbFIhWZofX9BaHoksHVzEWP4YDrlkPdd_v2Wnf7BYSfaV4puYRlWRkHRpV3zf_emQdaWU-pMQKWJhFAIpVdgvAugX-CJvUcHJMuLyDI41fOVD0hLvwSaF8OLcY0enw5023fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=ddFzWoVcW_sRjGd4dOuDQdkwIcGWi3oPpBCnM7IEoU1tVV4o-aNR72wmtte4yxVEIW2rEau5cpdEluRJxfHi42yyG5o4qzg0cPbYWGnBxFsLGOA3O80V2YRNjFh1GmLjPTrOeyMVppqaUSlCdyYQ-MAjFbrwf0ci7Ahg4cOvTEgds3-urMLdhHmNh-NLi0E8taW3vzjEnpDC9pyfSobbFIhWZofX9BaHoksHVzEWP4YDrlkPdd_v2Wnf7BYSfaV4puYRlWRkHRpV3zf_emQdaWU-pMQKWJhFAIpVdgvAugX-CJvUcHJMuLyDI41fOVD0hLvwSaF8OLcY0enw5023fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgNShWCiIMi72gvS86y9oxhS_eFIHvFY6P9U9Ib58Mkx1_86rhVu_i1PbyIqB4lo43Eaxtj61Fi5tSuavfSCktvkbCdGgkH0vwLxKLB8ssKAn6bSssBkLeG0kbcxD7cgOb4zWVe37PbNjlSMmj8Vp-yVZJvdxzoBq7Pj9dvMoeYUoUov4TG_r42-uqn-DBHbbk4EB2QuBOPn2NbIVUyV46mPJyFDW4rsxfhWyX_phVCjL1n2gX-GtsA3VEXhmtzM9azobzWfTkafkz_A_9sq2W6bJq5oYGY_QxpOf5T7VcWDkYwrMXjFD5Z9WYQ5mQOkb7Ud7Rze3Is2JCZl1R9qTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=vkkR5_BZz4SFDEUAFV7gZ9TmC48P18lsdEry60yXlGTHoNBo4OgHaYhrsTz3AmFH6wPeut2cgW9Mi_lrotuwKf4LOgZBynKiJ93ZR8iUcyIieZoY9EIghxxpwtTEqho2wmecyKrwEaXl1swlxi5moRgxIkFC4ByU4oJk5LUgYk0Kd6uPr0OQqzfQ8g6Bmk-tciaVl3EskFWLddi0mBUpTbHIiFwroTz5CIG-cbFCxyX2s4SM0h5reiCxjvyyLd-zyAI52QcTA_mIgkJwJl1otb0s-E1wvnBQtIOOtWWke_4Chw1XfD20JBBXcVqYJeLT3brovtg2Y-E5N9V023P19Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=vkkR5_BZz4SFDEUAFV7gZ9TmC48P18lsdEry60yXlGTHoNBo4OgHaYhrsTz3AmFH6wPeut2cgW9Mi_lrotuwKf4LOgZBynKiJ93ZR8iUcyIieZoY9EIghxxpwtTEqho2wmecyKrwEaXl1swlxi5moRgxIkFC4ByU4oJk5LUgYk0Kd6uPr0OQqzfQ8g6Bmk-tciaVl3EskFWLddi0mBUpTbHIiFwroTz5CIG-cbFCxyX2s4SM0h5reiCxjvyyLd-zyAI52QcTA_mIgkJwJl1otb0s-E1wvnBQtIOOtWWke_4Chw1XfD20JBBXcVqYJeLT3brovtg2Y-E5N9V023P19Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=sGGml61Ry9XQEGjAUqrEirV_YXkw9TN7xOXGsZNLS6MKOyxjbtVlmTkXJ5Heem38gP9N1w8R0uRCkJBQ_7yE59BQfH59-PsYjDhJ7K6ma0Z0xoIkc-KE87lyA95t6PhUtuLMz75mq-TywvpGotvC9WBXcp1IoObdkf1egZRikXunElmVy_rqYHci-Na_ejUFsBZD_14IuZLplHdTmz2Qcl31ZcD1CNcV1DKCNMWi6efnpOuCPfr0VuS0F5c1eDAER4KgqxQtVLyTGF9wv6KrkQPMG7iUI3V6cGwdAx9nmLoy7joKCOxyaq1Qf8Er5fz3D_0qSC19zY4H8GVyxsw9LTK763yKOozpSfjRwbHVcJUNht06QSZHQAg3hEfe65xDdBtvVg7RqmUbu5Hl6KrFIsHXdg6875lSvGhDlWCpHccXR6OkveLwMSnSTx_J3WHJO_syyRCQwgsptDtJ5BBezpb4gGl_YBSaES1ryH3C7x7yDyo8zD8qLCHTupAKW0glCPCIHRBI5u4d3L06U7leLhcVYAWUUMCtCXbA3nu19MKIgVm5lC7yonxJ9SzBOnSBeRArxWo10B-qqB_D4Kb2BzutR8K4fXGE70va6_MSAiOy41eOQxskfKP9BK0J6AOHSmrGuGn2owlvgeDqnkopzvNYuXuqmKDYFP0qnxrDflM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=sGGml61Ry9XQEGjAUqrEirV_YXkw9TN7xOXGsZNLS6MKOyxjbtVlmTkXJ5Heem38gP9N1w8R0uRCkJBQ_7yE59BQfH59-PsYjDhJ7K6ma0Z0xoIkc-KE87lyA95t6PhUtuLMz75mq-TywvpGotvC9WBXcp1IoObdkf1egZRikXunElmVy_rqYHci-Na_ejUFsBZD_14IuZLplHdTmz2Qcl31ZcD1CNcV1DKCNMWi6efnpOuCPfr0VuS0F5c1eDAER4KgqxQtVLyTGF9wv6KrkQPMG7iUI3V6cGwdAx9nmLoy7joKCOxyaq1Qf8Er5fz3D_0qSC19zY4H8GVyxsw9LTK763yKOozpSfjRwbHVcJUNht06QSZHQAg3hEfe65xDdBtvVg7RqmUbu5Hl6KrFIsHXdg6875lSvGhDlWCpHccXR6OkveLwMSnSTx_J3WHJO_syyRCQwgsptDtJ5BBezpb4gGl_YBSaES1ryH3C7x7yDyo8zD8qLCHTupAKW0glCPCIHRBI5u4d3L06U7leLhcVYAWUUMCtCXbA3nu19MKIgVm5lC7yonxJ9SzBOnSBeRArxWo10B-qqB_D4Kb2BzutR8K4fXGE70va6_MSAiOy41eOQxskfKP9BK0J6AOHSmrGuGn2owlvgeDqnkopzvNYuXuqmKDYFP0qnxrDflM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMM2LGYVEJyHi_QM6LEfWdqtIJt7v-74KrvFjLhqsVaGZKujkjlR_7bg1GZ52c3mrI9kjtMjVbJ8xdjiLMn61TW6EHD7DFeJLPuEcikAQCL5S3VAODa-L72eXNzN3NqYBpX9uy_wMDd9cgDGsXBAYyLLb0HlfOyBD02ciuSynTaMuPS1m5Fe31Lp_ffHdf3qsTJl0s8ks7zo2Su4QGjApqXmZibMdoebZDWrybG3D81kO6AhRb55O7ccKRGU8_59SlEkzEzZTXm0pk4Ot2YxwSP-XKhRh_bsssSU8hoQMM7FW93ZTk1zW3vf8onSNmm7xpHgw5EzmAcILI2glu5FHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Ji7E7cIwFQMRpNwKt9JkszaGdbjxaEAtqozpX9zofGxZ0U4ZTO43_Zjpq7giYXvayb4qdcToSp7OiCJYx4lZ2kI8NewYX8Ft3gmB_7e6Fe7JB04ezTcL10cH7gdPJ5Zx5S4rZ4_XKnqsZzSfbrZhDhuB08ZXz4x8JLlnT1moP29h68VcyJnNpGl44ER_GFKzbqEwYB_B7iA-up271jj3XXjoG9tfvvjaWIh42kcEnAGFhhrVWppMt98hXgGg2ehB1XHVE7Rw9z1f2D2zxqvNaEbrh3D6TomlWnhqw6f8JZeg0FjOULqQaj6slUeem6e00UTussxD--607shdwBt3XWnOfic0Qt6tFJ-1QbCKYyJgPYeUjJhk9VoBouI3JuDYUeOXU02fGGXV4skKhKX1vPknWDZTAUT1F-ThQRnUJjGkJvQZQA_7NwNou8M-kKysZXFhxjVaZVUJczbux1XMJ6WrzPE8PjfFyVYd5PpK2gAFuEbRfV8xgFa1ma0HW4ARk9XDeifOdCSnX_ICyXFZkHJwwaQNJErc64DyGogionv14Ziu-ccAjMET6BtVhtFKh0N5Avc8_5BHdGj9S43st18STpw8kTztI8Kd5if-pQbSQ9zpfv_voapo-2XjPJ6OrfJT4LByUbpT0YZ-AZKxr2wE94p-N1TtRcLshZbz9IE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=Ji7E7cIwFQMRpNwKt9JkszaGdbjxaEAtqozpX9zofGxZ0U4ZTO43_Zjpq7giYXvayb4qdcToSp7OiCJYx4lZ2kI8NewYX8Ft3gmB_7e6Fe7JB04ezTcL10cH7gdPJ5Zx5S4rZ4_XKnqsZzSfbrZhDhuB08ZXz4x8JLlnT1moP29h68VcyJnNpGl44ER_GFKzbqEwYB_B7iA-up271jj3XXjoG9tfvvjaWIh42kcEnAGFhhrVWppMt98hXgGg2ehB1XHVE7Rw9z1f2D2zxqvNaEbrh3D6TomlWnhqw6f8JZeg0FjOULqQaj6slUeem6e00UTussxD--607shdwBt3XWnOfic0Qt6tFJ-1QbCKYyJgPYeUjJhk9VoBouI3JuDYUeOXU02fGGXV4skKhKX1vPknWDZTAUT1F-ThQRnUJjGkJvQZQA_7NwNou8M-kKysZXFhxjVaZVUJczbux1XMJ6WrzPE8PjfFyVYd5PpK2gAFuEbRfV8xgFa1ma0HW4ARk9XDeifOdCSnX_ICyXFZkHJwwaQNJErc64DyGogionv14Ziu-ccAjMET6BtVhtFKh0N5Avc8_5BHdGj9S43st18STpw8kTztI8Kd5if-pQbSQ9zpfv_voapo-2XjPJ6OrfJT4LByUbpT0YZ-AZKxr2wE94p-N1TtRcLshZbz9IE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=HmaTJ5A8Hsd3DnUkddGrLy163fxGH1JeohF2HrD1w9x-fPrJ3eu5H-piVz86pFXOC9eNR96ttCegbFKcpy_9FboO2_4M78ya0OC21wGVqBWCa9MJiy0fl8g4_LvSvlX7MV7WVN0c0Z4cdqGJN3eoX_iWUd-g5DrRnYJMlolODauLQASFaXfdfwh14YlmYLE6IlK7dypBHwDGnIBzggkiI6no4KIr0WHyUeicNYYKkYXY-EIiFRYPYt3WGnntfagwkXfrjXVk7VBksJcJGT0MYEvg3mNo1_Wekkwyj-l0e1GlVcaaHsaEJoBvgJmE44Ps2-NSMXJlJxlG1F9HQTzWolJLtPa-EmhhpKtJgO3YGLkmNb22MbTvpFL0K5M_tHaYu3E-gOixHp5ko9JQDzD6kc7f7YceD6XNQ50brmp0oIcDj85v6EWf_AE6FmZwfljcr5RE4XS6075XUaHNsFraPdTRnwTGB1Uv09o_XbG2hHRYEgGjSddN8YV7mdcKaC6zHsmQz175_nsIrS_YDhVrrS-mNqOYUSYLMXXddk6GD4pHmhtcwfTqKaaWS1pC6xowbWo2YQyL57r66KaVkCnBHrNUrFAOYk5YxmZgXZegDParxLP1sb-ps0goWjVuL10Hfroiygj_IbDI37Q0PFTemlA82-jqGtAAGfxM4Z1HeNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=HmaTJ5A8Hsd3DnUkddGrLy163fxGH1JeohF2HrD1w9x-fPrJ3eu5H-piVz86pFXOC9eNR96ttCegbFKcpy_9FboO2_4M78ya0OC21wGVqBWCa9MJiy0fl8g4_LvSvlX7MV7WVN0c0Z4cdqGJN3eoX_iWUd-g5DrRnYJMlolODauLQASFaXfdfwh14YlmYLE6IlK7dypBHwDGnIBzggkiI6no4KIr0WHyUeicNYYKkYXY-EIiFRYPYt3WGnntfagwkXfrjXVk7VBksJcJGT0MYEvg3mNo1_Wekkwyj-l0e1GlVcaaHsaEJoBvgJmE44Ps2-NSMXJlJxlG1F9HQTzWolJLtPa-EmhhpKtJgO3YGLkmNb22MbTvpFL0K5M_tHaYu3E-gOixHp5ko9JQDzD6kc7f7YceD6XNQ50brmp0oIcDj85v6EWf_AE6FmZwfljcr5RE4XS6075XUaHNsFraPdTRnwTGB1Uv09o_XbG2hHRYEgGjSddN8YV7mdcKaC6zHsmQz175_nsIrS_YDhVrrS-mNqOYUSYLMXXddk6GD4pHmhtcwfTqKaaWS1pC6xowbWo2YQyL57r66KaVkCnBHrNUrFAOYk5YxmZgXZegDParxLP1sb-ps0goWjVuL10Hfroiygj_IbDI37Q0PFTemlA82-jqGtAAGfxM4Z1HeNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=YjoJzG7-1UdjaxDPDyBwTqV2ix1s0q_0A_AMjrb7XXsNDUFzzRvz-FZii9UmmAgaxVZpV9SBC8ZatRVTnX2Pp_l1Q8mwoMIikCdsllkYnSAseo8Dwrty3SnlB-I7J1n5h-Eo0FbVlEP1KAGaJRl1ELPKL0qDtImkzDo-CseaIkqZnAjlIx7FiCFiTB18tmQmx6YtwYVDyHtUI3ljXWzz9ZNHDu1uNrKg76PHWOGjwcwJm78eCIfK3udic7mdH3hlf2rIkFUV1_wImP_ETwt3r1w2jMVuXa6aBmfI6mXZKcaFTnSQrFg6w9JoV_D3IJw7sASXsdU2kB44kFDBYSNUfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=YjoJzG7-1UdjaxDPDyBwTqV2ix1s0q_0A_AMjrb7XXsNDUFzzRvz-FZii9UmmAgaxVZpV9SBC8ZatRVTnX2Pp_l1Q8mwoMIikCdsllkYnSAseo8Dwrty3SnlB-I7J1n5h-Eo0FbVlEP1KAGaJRl1ELPKL0qDtImkzDo-CseaIkqZnAjlIx7FiCFiTB18tmQmx6YtwYVDyHtUI3ljXWzz9ZNHDu1uNrKg76PHWOGjwcwJm78eCIfK3udic7mdH3hlf2rIkFUV1_wImP_ETwt3r1w2jMVuXa6aBmfI6mXZKcaFTnSQrFg6w9JoV_D3IJw7sASXsdU2kB44kFDBYSNUfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=hNOz1YtREqXeiayGnkDjy6ZNHC6kHdW_UHuND9kLh0YUdxpA5CuSQVU-oBAWgDkwl-e5s-MZS4f1SKfmFRDuV9s3UXMYONbAi8ULa5WBjniNu8Q8swgt4bZILShn4ZySmuDynVG1RlNO27QU0EttAAkK0zzpyy8rSra84bZriJUPk7Z1ioeaydaE12s2OgLOSj3fn8dXAt0JrNCdR8gCyxHhTVw1e897mPsQQAWOm1CJ4RSIRD9hEgBQQ8jIv7Pl1TknRCpkuoufvvdkkjcfmjUCPFPT9pKkP7naFO2n-zhWvlaRZTwftU1OAwmxnZ5O5QhutuV574rIKw0rZDd2Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=hNOz1YtREqXeiayGnkDjy6ZNHC6kHdW_UHuND9kLh0YUdxpA5CuSQVU-oBAWgDkwl-e5s-MZS4f1SKfmFRDuV9s3UXMYONbAi8ULa5WBjniNu8Q8swgt4bZILShn4ZySmuDynVG1RlNO27QU0EttAAkK0zzpyy8rSra84bZriJUPk7Z1ioeaydaE12s2OgLOSj3fn8dXAt0JrNCdR8gCyxHhTVw1e897mPsQQAWOm1CJ4RSIRD9hEgBQQ8jIv7Pl1TknRCpkuoufvvdkkjcfmjUCPFPT9pKkP7naFO2n-zhWvlaRZTwftU1OAwmxnZ5O5QhutuV574rIKw0rZDd2Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Yt2MVFUJiR8lCF_KBpQ4Xy3GEN3nai6kXSg11yodzW0RmOg3PKhAlCuKoKWvcic1b9ckgkJjF77HdWw5JgOkavcU3AGVmiSJccg2T-QsTKRvISTbYoGslvawarvmNfWf9I1zo0grjI4-16179rDmNCSFdeQ7_lkbl5j03aHvian0qr3Po4BtASkkW015AMauWf35w4Ovg9v9QOI2FC_ehKtAxv0WN9g6FOpEZYSED_M-BO7wo9OAEDO31T8VXw72k8Ad9b5UH5EFjzVysGBFv6hu1spIvApMxocpDs0e8kbgb9SH7-zfx3za-REcj6p-nEsbGTqoXyp7y60Ke--s-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Yt2MVFUJiR8lCF_KBpQ4Xy3GEN3nai6kXSg11yodzW0RmOg3PKhAlCuKoKWvcic1b9ckgkJjF77HdWw5JgOkavcU3AGVmiSJccg2T-QsTKRvISTbYoGslvawarvmNfWf9I1zo0grjI4-16179rDmNCSFdeQ7_lkbl5j03aHvian0qr3Po4BtASkkW015AMauWf35w4Ovg9v9QOI2FC_ehKtAxv0WN9g6FOpEZYSED_M-BO7wo9OAEDO31T8VXw72k8Ad9b5UH5EFjzVysGBFv6hu1spIvApMxocpDs0e8kbgb9SH7-zfx3za-REcj6p-nEsbGTqoXyp7y60Ke--s-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=mAAI0h5XkA6Hc3mnQvh69OhAusV-0dkZ3bcZpKFlEGu2EVnZX7Hkhd8fQwEbT--sH7Ni7NumHUhjJ6BHO9B0MZe2ctDbl8DNItLq0UGibg-r-5a_NmPprHvy3N1Eu_uDaPM6LjD-3Xr9Ui8Jzh_rtdLF3hDwmbkQuRbTBI5pm6gSNjWWAR4RerFU-DK9AYvyVeHrdplhlQfEmWqCAdSxJo8Mx0tgeqSA-rANFfFuoGjnr0L5ncOT58j78yYH63HNunsS0_HzKRJBOjntVxWwB5TpznblqsVpIkYJOyv6y203ScrzYzrdISS_J0MJelfPcLeiquC6Sqrgr8cU--L5bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=mAAI0h5XkA6Hc3mnQvh69OhAusV-0dkZ3bcZpKFlEGu2EVnZX7Hkhd8fQwEbT--sH7Ni7NumHUhjJ6BHO9B0MZe2ctDbl8DNItLq0UGibg-r-5a_NmPprHvy3N1Eu_uDaPM6LjD-3Xr9Ui8Jzh_rtdLF3hDwmbkQuRbTBI5pm6gSNjWWAR4RerFU-DK9AYvyVeHrdplhlQfEmWqCAdSxJo8Mx0tgeqSA-rANFfFuoGjnr0L5ncOT58j78yYH63HNunsS0_HzKRJBOjntVxWwB5TpznblqsVpIkYJOyv6y203ScrzYzrdISS_J0MJelfPcLeiquC6Sqrgr8cU--L5bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=e8xwsYfPQYFnHv59WegSyeMjBymeZYPorzOMdcqxTeQi9dsp8PCOGVo5oSLa4Zxf1e2W-tmu9HKtK-0zsbzJzdHxqgkiPS8BZOT1C6V0iPlowUU1WI5Rwpp-3wjPQJjOGCBsbJPadFx63dSCGdzWfYgt-bd9IxhHYln60i2fMehN6ShkBBoVPPWEB-kb9et6N8YoNx267A-mZEH-T3YvPs50T1c1yBTrtO_-uDU7LFovof6FvsoZgwJhzbgvfnslMOB8joKgWosyFmLAgqE_gA4ydhiA20pej4Hx5aiDd4xCE9rJhTZYPPQFPn8GNBfqXygNwpdYzaupR8XjCXmibA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=e8xwsYfPQYFnHv59WegSyeMjBymeZYPorzOMdcqxTeQi9dsp8PCOGVo5oSLa4Zxf1e2W-tmu9HKtK-0zsbzJzdHxqgkiPS8BZOT1C6V0iPlowUU1WI5Rwpp-3wjPQJjOGCBsbJPadFx63dSCGdzWfYgt-bd9IxhHYln60i2fMehN6ShkBBoVPPWEB-kb9et6N8YoNx267A-mZEH-T3YvPs50T1c1yBTrtO_-uDU7LFovof6FvsoZgwJhzbgvfnslMOB8joKgWosyFmLAgqE_gA4ydhiA20pej4Hx5aiDd4xCE9rJhTZYPPQFPn8GNBfqXygNwpdYzaupR8XjCXmibA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=tHJkHXPPD2xHW6DPYiSNM-n4TinTOaBZddn5TT94x55i1c4Ns1XK_taaLOvDlK2Dlq6iSrH4taDMDS4tTCcg07Zi1s-VhDuoKKZ5TRJIFcRXcRDdz-liBo_1zsWdT9ymRsvktr5mEvPxdHCbudtCBi6-sZ9vINdzpiuQNrMDTHBPQHqJOcklBjBx0FLNICaJgCjMK4I-3gcTDrbcrFAcJlc1UDKPmxKk8P4FJJBKAoXXLEr50dQpPWdFtjjOpaXK-RiSP2aQvfvf90DsIPaQwAJaGk6EyjfujcdQ_zkqsjO00BdhUZ7v04_LBIooxO7u3Ny4MhIwBnlJK1SFAKuodg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=tHJkHXPPD2xHW6DPYiSNM-n4TinTOaBZddn5TT94x55i1c4Ns1XK_taaLOvDlK2Dlq6iSrH4taDMDS4tTCcg07Zi1s-VhDuoKKZ5TRJIFcRXcRDdz-liBo_1zsWdT9ymRsvktr5mEvPxdHCbudtCBi6-sZ9vINdzpiuQNrMDTHBPQHqJOcklBjBx0FLNICaJgCjMK4I-3gcTDrbcrFAcJlc1UDKPmxKk8P4FJJBKAoXXLEr50dQpPWdFtjjOpaXK-RiSP2aQvfvf90DsIPaQwAJaGk6EyjfujcdQ_zkqsjO00BdhUZ7v04_LBIooxO7u3Ny4MhIwBnlJK1SFAKuodg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=jgOn081suC5kexrs05eqC3Ma4Lk_jl0jmtfowj29nDjUvECUCbOISgoFmkCiHhy2OI6LTE8QDY5AYk_KONcyzyHup1U56eqMUIoT0q-JD9FoijQH2iGTKTSOF99sAWDMplAGB8cvdeb4CCHZM_ymt0O5V8mEHkKJ2pN-FDp2yXmIurcB409uW2RNhNit381r86SIwUSk3cvDQMAdcM70nuYQlTSDOVpbiMnUh03EltM1HGMW80pbDMjlJ1Ffp-GkjiZqyQODDtuQ04WLpOem74joWbiKD03iYG8RhW00NjbB-iE5std63RwUu4FjKsHTaepis5eLY7eyFBe-VR0RyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=jgOn081suC5kexrs05eqC3Ma4Lk_jl0jmtfowj29nDjUvECUCbOISgoFmkCiHhy2OI6LTE8QDY5AYk_KONcyzyHup1U56eqMUIoT0q-JD9FoijQH2iGTKTSOF99sAWDMplAGB8cvdeb4CCHZM_ymt0O5V8mEHkKJ2pN-FDp2yXmIurcB409uW2RNhNit381r86SIwUSk3cvDQMAdcM70nuYQlTSDOVpbiMnUh03EltM1HGMW80pbDMjlJ1Ffp-GkjiZqyQODDtuQ04WLpOem74joWbiKD03iYG8RhW00NjbB-iE5std63RwUu4FjKsHTaepis5eLY7eyFBe-VR0RyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHC_guHk5cuWBhE2LiRMBKaxw3SlDoOpGZWv9CyHOzj_4fztYiChPqVpRI8sSR8NuF-Y6AHvAD6Fe3D6CbjfIzw-SWzooh9xr6gxA2VNL3aasUPPq5CudWgJYPW85wq1LQq2HQ88o0rTVc5b2nPGbo8FX7Us956bhfwL5kwM2gYX1SZXB5LQgYEGgbiNCgU0aHaKCgYOsdtkKFTr7Sd5XWwJZwBHdU88-yb3bHUUGW_MFH2VbyL_V3WtNfSHDoQpOjDXuDtLeabYSr0dTt5QQVVhY1YHBvdIxyBaAmyh7ye5lN40mm38RLfsQQZnMQXppHm9AOJw5NiqPN2s4Oi3fA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=fPgjOynNLK5qqY9Ojqat2wgPBzeSLS2w7yXhrIWkeLbn3z2WGp1Jh7RT7V9-IdGycusTHzDyY2d-I3W-C-a18bLn-ddIHYb8bu0e4ClPjCq7fmBNty7IgCAy7W4Udj6kw7okU_4gcI_78W97NZz_yN8AjmeSOEWg7FPBQTxCNL9qBu8QJR5Nn4SUA-d-sWUZZo_3lKFgLQKCL2Ixdb2b29W4LhcyxzcnHdjk0RlfUiaCOEBzCLof8_oWBjvy5Z2F-iSwNXMAcaEdTD_9WqzLYFL4cNhk0TJCvsdm8XBGrGKxHJklPmFEMoOjdf5P3eVL5PlA_ZlXha__rL1B3YmlTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=fPgjOynNLK5qqY9Ojqat2wgPBzeSLS2w7yXhrIWkeLbn3z2WGp1Jh7RT7V9-IdGycusTHzDyY2d-I3W-C-a18bLn-ddIHYb8bu0e4ClPjCq7fmBNty7IgCAy7W4Udj6kw7okU_4gcI_78W97NZz_yN8AjmeSOEWg7FPBQTxCNL9qBu8QJR5Nn4SUA-d-sWUZZo_3lKFgLQKCL2Ixdb2b29W4LhcyxzcnHdjk0RlfUiaCOEBzCLof8_oWBjvy5Z2F-iSwNXMAcaEdTD_9WqzLYFL4cNhk0TJCvsdm8XBGrGKxHJklPmFEMoOjdf5P3eVL5PlA_ZlXha__rL1B3YmlTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=XtwHkGaSJR_xPrb2Lc8iNsgqg_JSg95pQN0zzz30JtHe3UsxU18VIe3lHPKkyaV5YMwcvahG65vNuWmF8K4ABHEsAWYXCLpYNKHTOtaJXwOgdkZQirSgd8_If1W28HPJya9dePXGIVmJLtlhAEO8Kw3X629_2iBzvSPUWA5Be2Il7_p_i9-2g46FTREgZv5qgdsA0XPie-kq_hHihueiBXkeVFgCWSS_Z5tM-8JV7VpEsE9mwvwAG_Ox6TxeS_Oko3o9F6RCsKZ3d8nRcjJdz4_YE9IlymBMTCl4JVzFhf51FyfH8FyvhBrLoedOeTqs5ZD1aS9kOv6Eu4HVIIx4DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=XtwHkGaSJR_xPrb2Lc8iNsgqg_JSg95pQN0zzz30JtHe3UsxU18VIe3lHPKkyaV5YMwcvahG65vNuWmF8K4ABHEsAWYXCLpYNKHTOtaJXwOgdkZQirSgd8_If1W28HPJya9dePXGIVmJLtlhAEO8Kw3X629_2iBzvSPUWA5Be2Il7_p_i9-2g46FTREgZv5qgdsA0XPie-kq_hHihueiBXkeVFgCWSS_Z5tM-8JV7VpEsE9mwvwAG_Ox6TxeS_Oko3o9F6RCsKZ3d8nRcjJdz4_YE9IlymBMTCl4JVzFhf51FyfH8FyvhBrLoedOeTqs5ZD1aS9kOv6Eu4HVIIx4DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=WSsNo3a10VIIATqPFt-gnHF5gab-hJZKmFddKOEC4toddKoHdsxFQKoOl1szKrVZ2Sa47A8JDhmMnwr_oSxXgdwwdCwrPZXj8NtRApS_k0jt9Q3J62i-s4eB3HDi86SGA8yWu-3H3Fi0ZhfUjaHfFb8EuPofdbZYA48rGM1k6hW0ChZZsRzgOdz7fw-Dw8-xVU03es8ZRyp3qsx31lGdjo_Dov6M46GMy7B129mYZd6FcIVTniMy1pALdmhOIBJoxX60HXFIAZU-axRnfD0k0HgmPbJZK9B99XT0EvmBD2_JThxekgnfbNodzJBcJnwhXpPthtv0TVegHSCyfxfSEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=WSsNo3a10VIIATqPFt-gnHF5gab-hJZKmFddKOEC4toddKoHdsxFQKoOl1szKrVZ2Sa47A8JDhmMnwr_oSxXgdwwdCwrPZXj8NtRApS_k0jt9Q3J62i-s4eB3HDi86SGA8yWu-3H3Fi0ZhfUjaHfFb8EuPofdbZYA48rGM1k6hW0ChZZsRzgOdz7fw-Dw8-xVU03es8ZRyp3qsx31lGdjo_Dov6M46GMy7B129mYZd6FcIVTniMy1pALdmhOIBJoxX60HXFIAZU-axRnfD0k0HgmPbJZK9B99XT0EvmBD2_JThxekgnfbNodzJBcJnwhXpPthtv0TVegHSCyfxfSEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=FmodLR0yfrpHuc8FU_R6WbSr43xegpFi6XNRt63vurfFGXDHi4fUFsAK9lzkPBR-hmJcKzUMIibO25QpNLhQSxdtx1p8yt4CsPbWntgRaBjdZQ0FyjytPKZ6EKgBfPrVmU5f_pILm07EMcS69Hg42Yc1tHTFxB9oAY7hAMOH7UKztwriRYoek-NqDf_k1f8iMibSAjxlYqVW7oJvWkpZb3dTyxQvn-OZ10B1rSSsQwFSrhtJaMpGrZ9lyL3KpRbzsmR234Jx_G5IJyrgNTLKMxGqXr-z2KG0Ea_5Ct-HkD5Ohe6fRb272lUfH-74rGWJRHd7SYSpECxECMtF3E1xtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=FmodLR0yfrpHuc8FU_R6WbSr43xegpFi6XNRt63vurfFGXDHi4fUFsAK9lzkPBR-hmJcKzUMIibO25QpNLhQSxdtx1p8yt4CsPbWntgRaBjdZQ0FyjytPKZ6EKgBfPrVmU5f_pILm07EMcS69Hg42Yc1tHTFxB9oAY7hAMOH7UKztwriRYoek-NqDf_k1f8iMibSAjxlYqVW7oJvWkpZb3dTyxQvn-OZ10B1rSSsQwFSrhtJaMpGrZ9lyL3KpRbzsmR234Jx_G5IJyrgNTLKMxGqXr-z2KG0Ea_5Ct-HkD5Ohe6fRb272lUfH-74rGWJRHd7SYSpECxECMtF3E1xtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZPRBlL8N7hvWnI0n8J80vScmaV7cvRKV2RmYHSm8YyWnB9_o4nHch4X4sfL7dVmdpdF9xlfZitdTIh9ZTd_VbVJACiMvHejB06B0F8_bSnMK28oS770JxF13DbyEMkdFMEoc5uAJLzdnndntae_daK1qEjdHM18psPysOC0nSR2HiEK_YSDhEfi_ny6g9h7GRfTFdX8sUB2uixS9zTSOPf9w0ij2qllAwq6NG052sS1QeXPmBaoCHzkaA0rYbRL6arwaPKlpcRDWSe939zRrp9UNXCTUhpMUCV5n2dg4Hd8xCqNMQu0vJNfkeJ3g81_63BRrlrV4Tac_6xJ9ubePw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=UBseJu_eFZymRL-xdoS0ZsO9gTL31GeKzsW-24DEUWR-8nlN-NG8A8NattPAxNm93vSCYfGxsAqFldsHF6Sbb9jGfoEwqnRGA5KSr8wpYWDgiwSHkConfCqnRInm68RCX8PRoLek8ZityBGj4HOEUz8pwo58f9kmCHnM7hW6LnWH9NQVXhH2t3NNyF6eJxNBsu-KmQagMv0CaUqAqshpIXkPK6UzUaWJO8XgaxpPljoZyQLGELfZNFjMEZrQ38YQFM0ImtWNEbHtln-LcH7fDvK3ZwHsldX_-xVJptQe224BQtQC9TsKLWokszcGHLJhkcRLW25lxInlKlALdUl6KzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=UBseJu_eFZymRL-xdoS0ZsO9gTL31GeKzsW-24DEUWR-8nlN-NG8A8NattPAxNm93vSCYfGxsAqFldsHF6Sbb9jGfoEwqnRGA5KSr8wpYWDgiwSHkConfCqnRInm68RCX8PRoLek8ZityBGj4HOEUz8pwo58f9kmCHnM7hW6LnWH9NQVXhH2t3NNyF6eJxNBsu-KmQagMv0CaUqAqshpIXkPK6UzUaWJO8XgaxpPljoZyQLGELfZNFjMEZrQ38YQFM0ImtWNEbHtln-LcH7fDvK3ZwHsldX_-xVJptQe224BQtQC9TsKLWokszcGHLJhkcRLW25lxInlKlALdUl6KzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=uNiiA0-FRYKzygb3Z91j4zC64Ur8JIa2nP8EZgUAZy-tSDgCUVscloov9Oel58TUzgDOtxQ9LOAMoFd5oYgHU9HPSwbvibVZzoNmtSMnJ5uPX9nqf1H5cbbDEl7vgsLb2c4TVpFnB-fiVCZHrB3PHHrQ1ty0nNGDzF7Cn1xGdPA8e5wctWY3U5dsUa8aWeu3MLQn6x1lbabnf-zUgJky3P5_BrjRwKs3dt0tmYrQg2HiHY02348iXp3IVEmFmCTgtryHb5xhlL1B_EzpIwoCprHtd2LePcvQgT8vxpWG8hatP330t6kgZpPU2B_TCfK8_Mk7DSwAzGp9t8fnzM1CoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=uNiiA0-FRYKzygb3Z91j4zC64Ur8JIa2nP8EZgUAZy-tSDgCUVscloov9Oel58TUzgDOtxQ9LOAMoFd5oYgHU9HPSwbvibVZzoNmtSMnJ5uPX9nqf1H5cbbDEl7vgsLb2c4TVpFnB-fiVCZHrB3PHHrQ1ty0nNGDzF7Cn1xGdPA8e5wctWY3U5dsUa8aWeu3MLQn6x1lbabnf-zUgJky3P5_BrjRwKs3dt0tmYrQg2HiHY02348iXp3IVEmFmCTgtryHb5xhlL1B_EzpIwoCprHtd2LePcvQgT8vxpWG8hatP330t6kgZpPU2B_TCfK8_Mk7DSwAzGp9t8fnzM1CoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWKr7rqLKImlaobyivTXNVrMu0CUvLNy1JXIHgwG9YE6JEtrxSJrUvdY5L_bgtKXCNlsCVGWSiu_kHu3nSdsjONbYLuoe7FqbqN1TLnC6DKk8fAFzF9PWLehBk5gcrkdJ2fWZzuDmqZ0xu2scFmq0eXVCRzHP4j5KKrdB_5awRptSRcPiq_NdrTp5kbeWcEB2OyhWZuxRqfYxIkJjCzyiMRPEx_xiJa7jD4Bh7dekecjEDrb-gSt7q_DDw1X2ZpzOmRfB4XX0f70W3nND2_dX1SC904qUGYb_YIY17rGYI1mv6XZSQSVhT9zC0TdQtlVKb1NUqW4Ls4a0pqC-gYAfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GdAoyG1Na--pUROgN2SEL8doBNRmZV-nvaR4niSgT6yyotIV1iIbWWcw-GbdzDea83DQv8LEPLgY_Iirfy11obslyPtVSW2tqdMXuhZORbkYw8uMow-KaWRZxfGN8FGQC-J65NNpiyYi08layO0kJVNMt8_CMs8ECmbsttWijRqc2OiwkAHxZazwx65dtf9raEmdtVfZVfTK002RBYJx4HUYaz_zWjMKPPrDLMekkgLOGUhzpOFaiV25GvWs8wk5DSscH_YRng8vXo715THMbk19s4Tk9f-F2to67bFHtYJDavNANwBxMjTLa66fW9Mk3kBkKy8YUniBeE8KyGTAaQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=fhhDKJjdJOHoWynL7tdwc8Kx0VE0_SWC2znMD5amYR21FrBr0LvDC_slG6wnALPY7aPNUAedRcjT_nJwz3B1vgqTNw4qiFwpn6h5ewWZS4ct8G5QrTsMFhWZDMQ38I-gl-UOBZkVi1aWzuhzWKl4PZgRzhoLRtBVNAfNxZKIP4JtPHNi1XNvuFaWePA3iHV_YMhEQYM9wdeBFW4ZfE_FsPgech_v0lbveTFt76nB1Mtqf_SZw4H-QiWgKpdm9TINRdMcZiC6SxMxlqdffnm8_yeYYy5oen13quSFPe3EOUDd--xjg0-AeZ-oe63Hcx5G7MmjAHsnJWBPoFVfC7q6kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=fhhDKJjdJOHoWynL7tdwc8Kx0VE0_SWC2znMD5amYR21FrBr0LvDC_slG6wnALPY7aPNUAedRcjT_nJwz3B1vgqTNw4qiFwpn6h5ewWZS4ct8G5QrTsMFhWZDMQ38I-gl-UOBZkVi1aWzuhzWKl4PZgRzhoLRtBVNAfNxZKIP4JtPHNi1XNvuFaWePA3iHV_YMhEQYM9wdeBFW4ZfE_FsPgech_v0lbveTFt76nB1Mtqf_SZw4H-QiWgKpdm9TINRdMcZiC6SxMxlqdffnm8_yeYYy5oen13quSFPe3EOUDd--xjg0-AeZ-oe63Hcx5G7MmjAHsnJWBPoFVfC7q6kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkr_-mBWaWnDzounPChDTNfaki2l-GyKTienMBiaoWAuTfl6DwFU55tNPBr5CuTbma6k7OyCkI5TqRXp3zGQvKcVUwbOfN7BR_075a48V8K2VjDksRLVRtGfQOp9I9TYEeoGGKLW0pDq4eTD8YQZmiSu1IPwU_6jthVc_MySL6Z7vXsJM__l8U0UiuB88oUg1z1R2M4c_8-rS8HqyMu4gXrJIveTmt_cw54kdMtbeNghEhgknI2kvH5i6nHqb6j9adSDtsAkGriDtZYg5aD6pZ6MkbZt3iFNdjJ0nmwHXvw3Y8uOAjOj-QX29T1p8KxbnOKTihmaopWP6ZlQfsBB7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAoJrO6plopSFt2UAwphUPodBixpftf3Ov0MOX1Bpui0PkbOiwCQ_8aUpy1GOYdn4qpKKYkiixZLHS_U2TUhBfgOnxzJpV5BDlRPKkJsZ_TBFV1V_Z_ZiUmPMJmxzFtL6Xh0Kl12zXsJA7zkiHDdWZxkupQx923F-wgkioZ0WFosDA64P39UuEhYgB_A_WLBizB-sftO2rEkQy-y6me46oeAXPME4_NaER-btRnu4gfxv_N2ZNI2T6ubkgHlXw-RFLDy8OQKsUL3CFV_L1lBD8srB0arLGqitIucc0sXb5TKjDWBCRsFyGPOGS2UBRnq55vUDVhdv-xMko-oF77BDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWbANyUKJ9th1mqJGK49vIB55vKcbPl0WL75a06sHtktwM7CX4Rx6qCkPoaNFhkSE9iz12s7UZLC_NDV7akahsJf4VZReZ2blL4FUHI5v2oaBJAj0kdzXV5EEEkmbw_Gwy7B2g_P356WkF8F3KdZmOGrONGqoZN95U7pTpsxktsRaTJj7c7d8ZNFZsJNiYDRcAhohNXaPnmZBVQDwnTsqVBIoNrstYUMQbDlfWkaqbliuXYO1nHJcWA9ts-LfHBFqFZ5o-a62qEjl-yixjMiDHkO2t8iAQsZh7SpfPK0JqxanpSpA11I9NmTmI_mDx29IDxAsRbNTmdheS8O-EpEwQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=rcBg4lf-xiZ_575qiQCD7CuP_AMydUmWAE-irj4IZsb9v9td9VAmhu_ingrTu4u-qiUttYJeuEEOhVU49JLYY-diAwWGXuT6_QDiPmxLS6OXEv0i0_kI04GiXBe7CMT5Rw-KhQtxsfGq9CotyxEp79hAMrTVHojj5CLRvN32j88qv9o4vEo2xtWdrBo52NuJqLPN0XUVBvQ36PhkS13AfgAjiDuuFfSCyCweIlrTkMMaiauTkqEPW3FW-nbazvWwxjExCxWjkU6YKs8o8ZhvffUBoDeXifgAl2ZsHxarJsJPttmHwzuNlmViG54UIid5ID7khLCgcwO86aOvVGm6eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=rcBg4lf-xiZ_575qiQCD7CuP_AMydUmWAE-irj4IZsb9v9td9VAmhu_ingrTu4u-qiUttYJeuEEOhVU49JLYY-diAwWGXuT6_QDiPmxLS6OXEv0i0_kI04GiXBe7CMT5Rw-KhQtxsfGq9CotyxEp79hAMrTVHojj5CLRvN32j88qv9o4vEo2xtWdrBo52NuJqLPN0XUVBvQ36PhkS13AfgAjiDuuFfSCyCweIlrTkMMaiauTkqEPW3FW-nbazvWwxjExCxWjkU6YKs8o8ZhvffUBoDeXifgAl2ZsHxarJsJPttmHwzuNlmViG54UIid5ID7khLCgcwO86aOvVGm6eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=gd7Nik7a6UGkgeU5Njpfp0CnpBS5iyJp4xA5TAXI_6nhxj1cvXKO1jC2JsrMnBFM48ZmpPgC3cmbD6814hlR8b0FrVNh08KL85gQa7rhM6nuAPngpBB8g6mAc-IQnkG9A9GfwXtdL6GhuQGkx6tqYvl1Ulw1nvPDjK0X-W-M6cpKptIRln7nyvAwzctIV4ymXshTf8_ra7lNnlEdWnReVBmxk2MaGS-XpmkEzaHnoeQY4C79z1rB1cmUPewccMS2NjiUD89QNqxYXb0wRDy6YapD4lYjpZbjmzdyCLk8aMA-zXn1YvP1E44mGdgNnQRKJdmjEqk0qXkFkjdrwiptqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=gd7Nik7a6UGkgeU5Njpfp0CnpBS5iyJp4xA5TAXI_6nhxj1cvXKO1jC2JsrMnBFM48ZmpPgC3cmbD6814hlR8b0FrVNh08KL85gQa7rhM6nuAPngpBB8g6mAc-IQnkG9A9GfwXtdL6GhuQGkx6tqYvl1Ulw1nvPDjK0X-W-M6cpKptIRln7nyvAwzctIV4ymXshTf8_ra7lNnlEdWnReVBmxk2MaGS-XpmkEzaHnoeQY4C79z1rB1cmUPewccMS2NjiUD89QNqxYXb0wRDy6YapD4lYjpZbjmzdyCLk8aMA-zXn1YvP1E44mGdgNnQRKJdmjEqk0qXkFkjdrwiptqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=vWRG29_nENVxeUM3MqjBHC2D3NZXdLcPF_Xts0x0WlRlDFxvzkM82Vplg2XWZvr4s1XgU9VfLwvnb3DUisloKljYFkT5OnaIXDieLJ_EbsU0PwxA0ZGjaBb0wLkcDUtGhw_lhAaiZ7OTsCaS_hjbB9fshadDOXStbhIKFvbk4Za8scGEI3VfIuJ-_uDSl7eLY6U72OeDUO8w_kbjMNr32eJs_5RwnDe_Ie5680_YJAebR5SmjvgsQoXcjUP0EJwOEqy3cG2eF_UlLkUl5b6R2kWX0pi7GHkU1e38f2tpVPpfWWi4xKAcqsH62d2DXOT8y7C-66TWm4qdunxIbju9Pys9f-uE0AeJzEH62172ABIz_8GEG7gWP3Os-GSLtiqc4qO14NcQ8C9SReHFdC-SQybqFH-A06OvBzRpwqsOKZMn1Z16E5uIDnKGv1mPcbvAkPkiAHsB8bzyrzLHhhlH7ItlmunBpnFHd-DRs9iPRtTAFifFtpwnYqYZPOwGi8eq6LK09Xgl35S0e9WuJvjLVXvcwJ1CzhVILEkHyacbRfELegSQscMjpbvO6ZDiMQ5hnDJRSGfRI99jv-MXsjsdieILw9XEJxSRrtJiAkPOE7Vq5BzlSyoOOFLzs4WbdaXUn7DYE8RVjxbHwlQd2U-AXJfRh-PP6Q98us8LAmjZwOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=vWRG29_nENVxeUM3MqjBHC2D3NZXdLcPF_Xts0x0WlRlDFxvzkM82Vplg2XWZvr4s1XgU9VfLwvnb3DUisloKljYFkT5OnaIXDieLJ_EbsU0PwxA0ZGjaBb0wLkcDUtGhw_lhAaiZ7OTsCaS_hjbB9fshadDOXStbhIKFvbk4Za8scGEI3VfIuJ-_uDSl7eLY6U72OeDUO8w_kbjMNr32eJs_5RwnDe_Ie5680_YJAebR5SmjvgsQoXcjUP0EJwOEqy3cG2eF_UlLkUl5b6R2kWX0pi7GHkU1e38f2tpVPpfWWi4xKAcqsH62d2DXOT8y7C-66TWm4qdunxIbju9Pys9f-uE0AeJzEH62172ABIz_8GEG7gWP3Os-GSLtiqc4qO14NcQ8C9SReHFdC-SQybqFH-A06OvBzRpwqsOKZMn1Z16E5uIDnKGv1mPcbvAkPkiAHsB8bzyrzLHhhlH7ItlmunBpnFHd-DRs9iPRtTAFifFtpwnYqYZPOwGi8eq6LK09Xgl35S0e9WuJvjLVXvcwJ1CzhVILEkHyacbRfELegSQscMjpbvO6ZDiMQ5hnDJRSGfRI99jv-MXsjsdieILw9XEJxSRrtJiAkPOE7Vq5BzlSyoOOFLzs4WbdaXUn7DYE8RVjxbHwlQd2U-AXJfRh-PP6Q98us8LAmjZwOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=vW6hkHknh7c7JuoYZ9m8mknpB8OFEgZFtTD8OJV3aW7NRyiPHfvcghljip8Fzfck50Xn9zwOqGN6GYQVcvkF1x0kxXpLzYtdCYxWGvtTwEOC3L-vYn2D4L9xfQkD1EaYN-gyGHqrkWKEFtc7RLJJybPWOIwlkah7KTy-q6zPUPZaFlIW2cD2AToKtgwXnZiYP77eJhGuIqdsx9Ki7_nF6YY3GV4lCMV_gfHcBvqDKd7VN0yQVT5giQ2PdqqwsVnPbe7GpSp6DCFazI0CmeSvKUe8luk_EWV63EQEA4ZIiKtusM7P1FP_F4ZDHWrYWA6Y-_q8RgVzINe1OBEU23CnlHdVSrhec1lscWwGZiF8P8_datvh8Ueh9FBcM_iSoimXhVgoKwfPMG7Ny-2Itvhdlq1VuBpgBlWf7Oeie8hLtyHPiGihi3-Mxs1rZvjrH2W6hsJlWkK6zlMd7pcbkxBjXaZYDIfOhzL_y95-gQY2vDLk84QH0L-DzlFH2txgPEKMCZXZgcXavW_W-YqSKi7SBsd_L0rj1tgr1w80D_bctIZxtPZjwOilrPon71Pcz_Xpl-CYYFPtG2AyclegPhXvfBf7uBrPDvyV8mFQAYQhj-6_NVYKN0l209Et_zr9G_2IvCI-BpFXshRXEt7-wkH3BITHUz5D8tT740QAOJhW0fM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=vW6hkHknh7c7JuoYZ9m8mknpB8OFEgZFtTD8OJV3aW7NRyiPHfvcghljip8Fzfck50Xn9zwOqGN6GYQVcvkF1x0kxXpLzYtdCYxWGvtTwEOC3L-vYn2D4L9xfQkD1EaYN-gyGHqrkWKEFtc7RLJJybPWOIwlkah7KTy-q6zPUPZaFlIW2cD2AToKtgwXnZiYP77eJhGuIqdsx9Ki7_nF6YY3GV4lCMV_gfHcBvqDKd7VN0yQVT5giQ2PdqqwsVnPbe7GpSp6DCFazI0CmeSvKUe8luk_EWV63EQEA4ZIiKtusM7P1FP_F4ZDHWrYWA6Y-_q8RgVzINe1OBEU23CnlHdVSrhec1lscWwGZiF8P8_datvh8Ueh9FBcM_iSoimXhVgoKwfPMG7Ny-2Itvhdlq1VuBpgBlWf7Oeie8hLtyHPiGihi3-Mxs1rZvjrH2W6hsJlWkK6zlMd7pcbkxBjXaZYDIfOhzL_y95-gQY2vDLk84QH0L-DzlFH2txgPEKMCZXZgcXavW_W-YqSKi7SBsd_L0rj1tgr1w80D_bctIZxtPZjwOilrPon71Pcz_Xpl-CYYFPtG2AyclegPhXvfBf7uBrPDvyV8mFQAYQhj-6_NVYKN0l209Et_zr9G_2IvCI-BpFXshRXEt7-wkH3BITHUz5D8tT740QAOJhW0fM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vo7hEzJWO55_RFR00nlcqKgy8c2gryS6HRPI2X5lw8HzbkLjvq7accs5jYZ9YiOlmRBg7tDUOJIuU622oTuwQe3MEze6baOSoOmt4LmjVV0MUykbcGCovTvRWQY2hHKC5O7ujw8VE7wvcwTqaejmtpH518R8vEKj7k3ePH-gJ4nq-R2cpV4TrauhnP-Fi2UidTAjVERfABzFhVUAKP_yLzQ1lJi3NSGleAjcQVovHmps_pLHTMnxHEpCu72CdgB-XVT0e4HCn696Akm-BkZybWyTryKFVSEAln3OS59zn2cKKDvS-5FRthPd_QqoGxj9zb4xVXIe-wJ4eV9fgjn2SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=vo7hEzJWO55_RFR00nlcqKgy8c2gryS6HRPI2X5lw8HzbkLjvq7accs5jYZ9YiOlmRBg7tDUOJIuU622oTuwQe3MEze6baOSoOmt4LmjVV0MUykbcGCovTvRWQY2hHKC5O7ujw8VE7wvcwTqaejmtpH518R8vEKj7k3ePH-gJ4nq-R2cpV4TrauhnP-Fi2UidTAjVERfABzFhVUAKP_yLzQ1lJi3NSGleAjcQVovHmps_pLHTMnxHEpCu72CdgB-XVT0e4HCn696Akm-BkZybWyTryKFVSEAln3OS59zn2cKKDvS-5FRthPd_QqoGxj9zb4xVXIe-wJ4eV9fgjn2SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QudxLi9RM9kSv1HOuikivkp5E8WI6Bz1zJheipbuMkADPEPttj_st3q4uYpqDVu2-idp6OSoyjxOrkM6nk0a0qaYcdpyHH1Kmag16kRHFzYVCKBE4A_E6baDU475Y8GYwqC5Zf9lzEEovpEHEZQGNqqK3lhQc0BgS23KTZGqlQvET9VrX0z5nZTuTo55te1DLbHo_B35RgaQ3uER8EhqCWLcQw5R1YfbSyqYgxPxCLJBJYIQSNc-23PHkQfZZePrA682i6P4cDsG5oufdqiDcl7GwelpU1CBo9DhFWGz7rgFSsE6hgf7iLRGIJG_nkXT4oZULE17MybsVjq_ogd16A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=TlQbNaT7fCICSAYD7JfdrdM2k9UzrH1IUNi_zW5rL_GYUg9xgBJ4ZwkaIbpi5u3aHgKfGBM1ph608FnyH1duRxhGqD5Y8eVmKcz28RGlRr3HXqcczWwVbX_cEUMY33lk9nG-vqVZTad0XOhO2pFMtgTB-OuHLtmR_jnHRCJJvt9hydAhPOEOFizvZxsSgCsEZKajdzl7sHKgnlSlIifN72om8DcGCIgTNnDzogkESLdgvLkiovU4OuAl42-YdxI-vIt-S8ac8bkXS8i5SD6xBAsGtX0s0KUQo7jFDZpXAkMptvJaz6tr96dwAF-ZK5uM73P5OlAp-GRGUDasrq_ctQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=TlQbNaT7fCICSAYD7JfdrdM2k9UzrH1IUNi_zW5rL_GYUg9xgBJ4ZwkaIbpi5u3aHgKfGBM1ph608FnyH1duRxhGqD5Y8eVmKcz28RGlRr3HXqcczWwVbX_cEUMY33lk9nG-vqVZTad0XOhO2pFMtgTB-OuHLtmR_jnHRCJJvt9hydAhPOEOFizvZxsSgCsEZKajdzl7sHKgnlSlIifN72om8DcGCIgTNnDzogkESLdgvLkiovU4OuAl42-YdxI-vIt-S8ac8bkXS8i5SD6xBAsGtX0s0KUQo7jFDZpXAkMptvJaz6tr96dwAF-ZK5uM73P5OlAp-GRGUDasrq_ctQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=uTqwg6fdUOCy_c17pHgHX5a8Y0wAB9-KcIQ5QO-JfVs_n0k5_8kSx8FmjkD9iLNYdsmT4dwp-5R8iHVTtk82ty21PMUUcteQiK2Qg_bidqd09qb4_t_1njzVj6-QmI3pq3gm6L9sbv1-a02GL42YNmNKTuCoUH9SQJfnI91HR6JyMatI5SDuqg_uBHJElMk8YTeZcKSyt9ljZg5wYQaHyDUXf_6rHL7vAKQb8VY2Pk3KkIjKthzDLuhmNHf0gByAQRtKpKUpnsVwDowkJ4gL7er7D6ZO6UiLClt9Gm4mFfBCrIL6sMvy4trypOq4CZhVJzmr6k2hIMrGSEJZMVdY9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=uTqwg6fdUOCy_c17pHgHX5a8Y0wAB9-KcIQ5QO-JfVs_n0k5_8kSx8FmjkD9iLNYdsmT4dwp-5R8iHVTtk82ty21PMUUcteQiK2Qg_bidqd09qb4_t_1njzVj6-QmI3pq3gm6L9sbv1-a02GL42YNmNKTuCoUH9SQJfnI91HR6JyMatI5SDuqg_uBHJElMk8YTeZcKSyt9ljZg5wYQaHyDUXf_6rHL7vAKQb8VY2Pk3KkIjKthzDLuhmNHf0gByAQRtKpKUpnsVwDowkJ4gL7er7D6ZO6UiLClt9Gm4mFfBCrIL6sMvy4trypOq4CZhVJzmr6k2hIMrGSEJZMVdY9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc6oGPstFg9j-ckqdNLCKMm3IA-bKUYzJ4jHXvnsMsy9uK76b0rNPloMh0jUF0ApiHsOkWPlV-mohucgOcj21gw9aGA-iUt4KUJ_i8lt3gFibxK9WdsjrkstsN4KVNVFkVJ7fRX0mNlpZxaijRP-TQRKeboiT1cga1p8NSitMqRIArQZY51nNXko20RHfqB1dqjU6hZCRp0DX-8OaySOGGHIHoKXnBHItxl_hwYmQmYKD86E5qSmZ5kca8j2CQZ2_30NU-0RuN-YA3ADMM9nhmdV-VMmwdnalRNS8k87_75gaU0ChccBzRMJbgx-DV3alytv5NxFKvCNcbFcs5IgAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7XW2G0PHAeOFIXEW-4ZcfKkl0dDdii9jJI_yvrfduJcMmHIQt9yweoN0U6XMQ84rxbtlOFVHccsxHICULXaWeKd4zGsvJdp2LAmjOppWebj4N50_8EyWTusT4XsNiMoErDUNezzqgjis11sBUZG5FUyALD0iYt86dgrs3z1tGPuni7Rct2gXPCPznADgKA3exjXFmQEepwFT3MixcdVsw0N79MpBm3wFivHcIFG680KXoLwEAk_oDCCqil7O7zTH06mPNr8XNzIP1cHRprURRadmtbQJ7IWRKkRBwIWCqcT5ShU_yKHqcg2_Khj3E5R58o2nWly5UgRHUg9b91hTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8vHygXppk55NrrUMfH0Mk1FWtPJXJdmPNHbYTFAM-1bgGv4_fmI4zV8TDY7tKYvRZiP6tWwz0pm3GXGSRSfzEmdTAuhVoYs-LDwP401X-IxJgEColR270hndH4jMEknrvKvIlYIbxWvZcJilWibElQFH5Ld9b5Nsrp5vFKvIaHmM7AfXYAyAMqhOqNGDTUMU9WXPTEvaSDbaPo-BTWg5HetrFdKrh1XNe-KluQOym5shORuQcnIcV_RM4md9tsSpzqqEEgGM3WuaYZH9Oy8Z-O9ZsleTevYjpGTKqV1n24cRW5VNSEl_jbm3-WwmUj567M-eIe0tarMyntcQnimDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkSAgP-gy_HFx0FI1fwGKMiOQHiLKmcc-Bl0IZ5CgkkrLp55G6e8yOAQjYJoCe5N6e5FOvP7aILCzFC9V1RtZs9Jq9qGsdqxCdMmp-qHEAct2yYwdMHvYvuEM6--4dGhEy8EcaN4mezg0REtKJ9C_9_YVJldvehYFRioTtY2JiQmeEcKyDk8792tYulQhUutyxq1sHzprxOK5FAXZnILjFye1SpjOuF_8MxlYngvsFpaUeCYvI6lPl7OkpbsO1LURr1nWBtHw1rmaTDh5-rtnWjmLxxoKZzgiJPU_vaMZaieJbiUZKHB-tuJbYQYnZju0Ebq4J6LbMAS_g4vDGLnlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAjQIrlvWlQPkDAHn5l1WruX4X9ZUQDku4liMDPML1cUWIXsd5EKdT2IU0i_4rQhImf3EkrLI3y0DmJSfpsXi-S8sPh9LyHANcgH0EV575tsFwakw5wxwMbqs9acmi0R-2P3UrS8FBIWHgcCWDAuL5glvWp_9S_9LpVWf1oY1tkaQ_s7hVyyuWi88fXreDU2jOcSOutowpWJRBu0-fwxryczUnetMleYvqzVcvB5fDRorS4JayXCY2Xng9cMYyqOF3tJt0rD1lJH3oz7B9J4L-DU9Hyi2jZfMnvTgcDnFBkT3fzFvZZsojEMv8ooetdquuBB7EaOxUors_HxYeChWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPHKSWwCQ-G8oY2RBnE8lxoPg-e9k_rEpp6acGkpfUnJS6iTgqG6X1tLfQXMijl1XspX0iJr8PfOpyA0VibBzMWrxVG47isAr1Uv7e0tCAJ-f1TRdrqva9VBSnunyPzGhFHvh6xJxIDFw9bAZmNUeJq1tXXkg6pixrnY8DEqdpBrR4_d5WBEjgrrL_5VM86zUJD1R_f4-OlIkGF-SMG1mYSAojUYX_yW9cnVKwrVjoEtzLJ6YkZmccUYGnLiwT1cyanYnYPRk8fk62xqyZmTqRPse6e1MzLXnARSALyvoiKB04hnduTr1MDNyq6N1N7qQ_CUbHNJ_XglVbUMPQo_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOK3FUtwDhbNPo1p-4CBb91hjoDZmR0dPgJmwmX7-zydmO6zSV9CjStGlhBNTAzywZuHm0Nem6yjLBEOHlIeqpjSiNDukMxFTroQQ4FWxrRFJoPDdl3-aMkZfzl-pKcgdMKOF35Pw6tRanXhUqftTCxAnADTUcw6xAwWxAYfir9DMvqV33_-goWzmyuEWNSIpGqBm_RJ07sLLzTSwLCpO72FTFhRW8Qh8UkdjZEHNUc0xm4CTXTmH5UqPgpQ5jMJtPTEbOg3ZOZFhyIfB8v7Qi_c5fbc4IdTThBUMsiIc8Nm6UJ-7dEzUHakCoz6FNE1bIQUuVn_qiqbtVa82y-0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRWwUob2soUKvpvfGdPPTYTrcSw4nwT-oaMmNAUeIajLVnA35GxyBMoLzfCD1eTMrTD5rdIFTiyvVdZJokFgKMENinNqBynqN_3Uo7FuVuJEVji8kZeVrtE5cfW9IX31CiMu1zQRvxec3HBEJUzM-zS9fJrRNT1vnd88HqRCJHKPy-BIxyOfD_ZRgQ1WU-dzJ9Ezjx0lW_SrI1e-j4Ykc8185nWEYybM5haVzNPLwtxIcpdqyIjDLvgOhnqe2w-KQa-oTs8pBowXtZkYU8T4ToGZg-Vg2sP50faCoSMOOYycST1gKW_p3SPy-GugYo6Pspo4ncHXUuM3jYTK-64N0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jaYtC_mGVxPOkY0AEaSN8taOOL4RFTgm32H4KJWlJlyta6hHhmWpGAK5XsmyXUsLfET3UnfsjuvYw0vvCFAcYJPyWeplguGiD-qfG7GebA46aujrxWyyx_9qw7X-v_FIYvP9Zj-_H6ldRj_FqMiZ88GTRlL7N_oocn_o-avDF9HVPoAjthQJRifruEMsrToDftNLatnEOJcACxPa99iq2R7dfGc7HHimijOeGKtpHyRoQKWKpumWF_WgxGPJFFWpaT2ckXBKE5L997Vem7GW8PLZe5yPIj-1o2M8Htx_HNIOXGVwtOhOSbJ92WljsjwHrwc3rQWFV0YR019q5FI3tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bwetwwslMEq0k3fDFe1mxdZp_mFZu5ntucYgo6bAVj-cq_teanYFFm6KMITp_vVdGbnubG7fvt_5Au-83uF6SmHe0FCDxV7yCgn_Pzjb8um4FYo5r4xmEGENotb29rXBeKyD9FSfd5WeTtv8TRMkyCZ7Fc99ZoORToB9Gp4v9Si-LA8OC3iK0HSgvqlH6yWNvWGDyEslMRwSb1YLDENPEQIFZfDTNMUhoHfhaL353I4rdWHu2rYjk2JjMP6dJ-A9vc63HHEFKllXEAI3OJOebM7fmMpl6d-jMI5YXgCxs75lRlIboZNoiThAqLoUzbUssIxWRMz8BL7PbFQ2EouXEg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=V33Ir0bXfXSMyJjhwW6NgWwjU4BjKdz0hiRSR4Yp3pU6a87MmeSeXGV8Xng4txZGTeedTGEGSY_tg9i2HFGArhiHHJ3FokMNPPAVlsWVk6Y6wPSuT6Qb-n1NGUlD9H7u2B7TsMI-8oPjTRITVIJTGMSr5Q96erZ0BnkgzZuVI9YD7OQdsIQIECuL77bmaUeBCltRUdBg2_zuakzTDCoAvyxkI9eH0xzixEDrGWfdAb-OWrZQyT5Kre7jUF5eqZ4KyqJoIxvdYYWx7CK0dlFrcfoWcnQGMOjg74wEtwOhO2dgnr4KPAo9RXOgx8iD93HEFfNIgWkjrpgkNsMSWJr9tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=V33Ir0bXfXSMyJjhwW6NgWwjU4BjKdz0hiRSR4Yp3pU6a87MmeSeXGV8Xng4txZGTeedTGEGSY_tg9i2HFGArhiHHJ3FokMNPPAVlsWVk6Y6wPSuT6Qb-n1NGUlD9H7u2B7TsMI-8oPjTRITVIJTGMSr5Q96erZ0BnkgzZuVI9YD7OQdsIQIECuL77bmaUeBCltRUdBg2_zuakzTDCoAvyxkI9eH0xzixEDrGWfdAb-OWrZQyT5Kre7jUF5eqZ4KyqJoIxvdYYWx7CK0dlFrcfoWcnQGMOjg74wEtwOhO2dgnr4KPAo9RXOgx8iD93HEFfNIgWkjrpgkNsMSWJr9tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRWRQ82Ba2PbJrSmQH63MuZ_sGCnfXvGi4HH05oyI93ODZIofeGHeuzSc7Mdr9iuolY9RNSQo_GH3cwrEHU9AW_aPNW5EW5XFtk0qnyTAFMz2NJkuVAYA3CbG-zxYl-58zxV9wzMnGpJFBk38tWPA_4B2m1wgL3M1_kvTI8W6XUI7mejh_PAb6Fgb6hFh2W4meUT7P5fP2oMi31InP3AZpT9kr1S3oobictf6XYz1W8ZvJAuEs8tmqYempUSjeRFA2ao5oUY9Nyfl6kAxNVi0QX0OjuzW6jrxLq5MFQGT0thj-mXxDvtujacqOtyKDE8Qs5Wr5FwRp_lgSSBGDjX8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2LXHYhFt-HSaih1BPbYZeCLpJDPdMgAYGXr8WJ1l8kCPtyfSs4MdM6fzLTTmUidnICUUJeXfWHJF-rroxjAaUYQqssfgCoqFK7c7Z4ChvK3Zlc7ty4vQbodfOEnxl6oLLWvE-9ECfau9onwlWMICguUvzmGhwp31WrPX6-FSisG4tjGrJ2Me87VqQyFTNrH8ugE75c6A7OzPVYGZHNI5thumOjHqAPiI1h82Ty8II2Gdpbvfb7xLw509WpTGIVh7exwhX6cuK7pZlSyJhJx0yPmAdJ_X5GTeb-SaHJZTUTT2hsHK4AAzDE7YdSFzxAolcCpzse_uTCqMQICLZYSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=F30_wW4DZOc3hNWunZd1H5lxN4YTjdS8tqu8-gdbbd9vT8zAvk9AOcx5Q5I5t9D05JNV0FCYZ5o5BQeSXcxfxDGLlm9FaSYQWTvaD6nqNRP2btGYb2FMgkkvuhnrk6R-WfBYVeiAuiuBX7NKFHfZ_jIP4W9BHXvUd_0Nh97GlnrNUbkOM86bXKTdosI-DUOAm8MdtUFGHIDKFel04rDz2HQOCJ3PlRwYqrn3_wtrep-bRdBtag6dwaL2cXOdCI0lsFvDHAxbOP0EUUtm-UhHVgSrquKKKlYng_O_9xWHKy_2E_Xqhsetzz_aWl01IA9FQoDGZov4wx63AxUqT5wVyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=F30_wW4DZOc3hNWunZd1H5lxN4YTjdS8tqu8-gdbbd9vT8zAvk9AOcx5Q5I5t9D05JNV0FCYZ5o5BQeSXcxfxDGLlm9FaSYQWTvaD6nqNRP2btGYb2FMgkkvuhnrk6R-WfBYVeiAuiuBX7NKFHfZ_jIP4W9BHXvUd_0Nh97GlnrNUbkOM86bXKTdosI-DUOAm8MdtUFGHIDKFel04rDz2HQOCJ3PlRwYqrn3_wtrep-bRdBtag6dwaL2cXOdCI0lsFvDHAxbOP0EUUtm-UhHVgSrquKKKlYng_O_9xWHKy_2E_Xqhsetzz_aWl01IA9FQoDGZov4wx63AxUqT5wVyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=ESKJvXZW9uJRvEtPG27VeyFUEhAnEJp7rd5qQwhKTcfBtRd5TDrB59xj8_K4sKbHbnakXL51KAmeJm_kFlkJZQqWmcvv4QC39ynImXZdrlg_HZAloPFREvtAzEXfmBzPv1NaTToBPWw63nqvMgnOMMHMMHU4rJsS3H0c_ltkEHfjAl-Af_hVNJmae5DuzMu7qSI0sqxZVOV0eXac2pf1uoJ7UY7OHbOCsGXKsIF94DLkpH9j_PVnmb0k3-D1JJS--l5VVWwvll2VtqWjtGnJkmHGfmy426rJDAvOP7YEjll4wZkqalVbGjwTgBsM6RhTkhVW5zxOvHL--FSsSdtP-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=ESKJvXZW9uJRvEtPG27VeyFUEhAnEJp7rd5qQwhKTcfBtRd5TDrB59xj8_K4sKbHbnakXL51KAmeJm_kFlkJZQqWmcvv4QC39ynImXZdrlg_HZAloPFREvtAzEXfmBzPv1NaTToBPWw63nqvMgnOMMHMMHU4rJsS3H0c_ltkEHfjAl-Af_hVNJmae5DuzMu7qSI0sqxZVOV0eXac2pf1uoJ7UY7OHbOCsGXKsIF94DLkpH9j_PVnmb0k3-D1JJS--l5VVWwvll2VtqWjtGnJkmHGfmy426rJDAvOP7YEjll4wZkqalVbGjwTgBsM6RhTkhVW5zxOvHL--FSsSdtP-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
