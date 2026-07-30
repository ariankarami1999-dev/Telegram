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
<img src="https://cdn4.telesco.pe/file/USd_8-UIpPPpVpem14L9t5-iSahJGCZDavATvbt_4nilAPK9Ic8zknyqgXad9l3I2qfDWZyNjEAau8i_iBi2vG3-QXIH9ljNjs7P59YEnlgC287O264pJm2NcmWfZyiAs_7RPw5HWoJENHXlhEl55Cq_MnBDReQ2xMS3NmctOPSMJHzde5grz9S3KdoSlp5ztkhRccZgjN5ytpJhf2viHiplGLz7dVuFBQILs0Y55DsRFZHChVD4R9HIBLfsRw5i-Q5XgwkCmR91fkDXEVLlJYStkvHyABO1IPw46rQoKeQIAjQeIDjOfIfRozGzTojSO6JxlYbxmC5Q2o5ckYAUDA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 19:02:01</div>
<hr>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCJL3-8VxSn7fEsY3P6E7Yu35KygkPYAz9kSrPiP6mOf8U_s1hTygNHV29aoJtMFV3uDNu2SOmOr0pRE8Uvfb_4v3pd1wxSiC7wpZnrAVsKJuukgP-edn0XvKe6r92a-BQk70aHqprMQhb3F-ozQFNjyygGncCdKUSeTnA49lpLU-LKQovR3tXzfRYEQ13VxHLLbiH9ZOq8KL8MaWIGiCzWEk2jLqvCACusOmTarI5B3ycu06qcPPIP_Ppb52ylFXvsw2sTsuqNG8bwZzP13zYu87MoCAD9yHgVbxg1mP8ENRHtvk-EBW8FmpMPAivbYtiDzL3qDs_aptE84S3_x2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4kUTxRXfz-D5HD_bWoXgRgrYiak-pVLXVxgp4-BeojCHshuIc9HusfxGkpxvb3FpuKDTuEJRotNcjc1Q4l0UI7S8dvhFlWitvfNEqTMoz9DO13EehM3mEg1YTptXHXCp6iWN1PYngvlboCUMmcJgS_fU7dwZKWFh8-wNn5fgjmqOkPtTkiFIcziU_eUdyuIN3IbPFQ3Ybr9jGdcwqUI-UwnZ5Yq6tio2u7PqDKaggJpV-PxFW92N2bMtLam1MDfxNe3ATnZs0KToZJ0EYnesRz_GSkv1NFWkCFCB3bxRL6XJnxJzF9ATpwzI_MDdbaOGGrM8q9bDWB8BdYZxQ796g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=YEOHdLMVPtOYw3J_5YPdxn-Gv_SFUFocUTead4paxlJGZnTIUZV_hd1LI9wNVEaKNoN4gm3gWtJ4cppuv8BUVDoGelkv7IjFGqQiNpguBEnw4Ut7g-q7tQEfJkUKWQyTL5jZECN9R1DWNqf2W-m-lqWgu64xR_w2IeqNujmzqOg8E77WWbpuSUUQL9KLjZidEWAPqRsVL7aJ-P3hMr0sCeLuZKZvRsSfRe8zfqAyf76VHo7sUY_VzIZ5_aoAK7TvhZpTr0GrFHOLuSocKADvoQZSoI_--UyZ6W1jvoJ8UQ2O6lDo8F0zwst55t3ABxnCGemJSaEJ3wpxXwKYm1kVOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=YEOHdLMVPtOYw3J_5YPdxn-Gv_SFUFocUTead4paxlJGZnTIUZV_hd1LI9wNVEaKNoN4gm3gWtJ4cppuv8BUVDoGelkv7IjFGqQiNpguBEnw4Ut7g-q7tQEfJkUKWQyTL5jZECN9R1DWNqf2W-m-lqWgu64xR_w2IeqNujmzqOg8E77WWbpuSUUQL9KLjZidEWAPqRsVL7aJ-P3hMr0sCeLuZKZvRsSfRe8zfqAyf76VHo7sUY_VzIZ5_aoAK7TvhZpTr0GrFHOLuSocKADvoQZSoI_--UyZ6W1jvoJ8UQ2O6lDo8F0zwst55t3ABxnCGemJSaEJ3wpxXwKYm1kVOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=q57YD4nwooRYNVQfjQxDucVMOS15EqC4OVGlpedKA2F2UxnYu0byFUA6qI6G9U9FEcDcmQl3xL6A_NHnu_D21GvuFr_GByZcLK_QMWfZ-mfpctpyaa-U9Gm8kVPKTpkiM2SSK_OP4wzReJrmIG_Msa2_v_05PWuCjZ6wGGcua0ztX-stI6Gbf-CkbH7jh-gwTC3o-bNmHNEh5SHmLsNCrJD8vRjZ90yBeVm3QU0e5dNTQhCl1fKyBKIa1-n0kQ-sVcmPu3E15OwAmVXzIaPoNLLYram4NmXHn5W7X-hVn978t3HoVm9rnzmdwKLdWGw9MGbX7sISckjXUFjAOKK7cQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=q57YD4nwooRYNVQfjQxDucVMOS15EqC4OVGlpedKA2F2UxnYu0byFUA6qI6G9U9FEcDcmQl3xL6A_NHnu_D21GvuFr_GByZcLK_QMWfZ-mfpctpyaa-U9Gm8kVPKTpkiM2SSK_OP4wzReJrmIG_Msa2_v_05PWuCjZ6wGGcua0ztX-stI6Gbf-CkbH7jh-gwTC3o-bNmHNEh5SHmLsNCrJD8vRjZ90yBeVm3QU0e5dNTQhCl1fKyBKIa1-n0kQ-sVcmPu3E15OwAmVXzIaPoNLLYram4NmXHn5W7X-hVn978t3HoVm9rnzmdwKLdWGw9MGbX7sISckjXUFjAOKK7cQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2_E1AQlneS_cWCRrq5Y3jwFiXuG4ui0Ii9_08ZKYtz09YbS_WJfTwlPc123MLJOdhhH_uC-OdHKggpLPBVwb53aVYVMVEBbupRct10rGikUu_egMhVBeY6Em2KRvNLN6ezMyc4cWaC9i_MxVYMpSkLayYAHulZRfai4ia-sc2bpX_C5ECLJElMpv0na-g_yK-IXmaFsCEPMC-nlvTYLcWtTKq-C_bS-OPNjqo12ju_R6nRN9k0cYz4yyM6zZdi5keXtqS5peHUOYvI2bMIJJ7uSOObqEq4hxrYxJwfmYDhpC28kK_jNsQME_sjEe4kgWMDPvxMKozXYX_KQ2tif7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUv5anB2qfc-brRh1IVJenxVNXBR0sZCsS_HQO5fDdRmfS3qbRGp8xsjEf9Uje5nBbcXkC-QdgDT5oHzh94KGeFdXLTJhJUO7yOT48zlcgCBEJdFxKmbzPLPMT4f91Se-3Pxl4zLbStIjl3sROPy4gDLxY2Ji1oTx81YlzciaS6Kjm1B_sqLI_bHtYm-5M6GVKX-iAjZD8qsuPR05UFej5AAOGArjArlLCmiIMfcGvInvBRZmcUYzDNd98S7O2yy20QFX9oTOhwtBJcmJsNQHa4rBEB8PMp4Z5J_LZxafM2YCH8__zbDb_rWZTuZhYe6o0Bok-mCja1U9qPhTmi8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJhPQDmkJLTlJpw6ja_zEZrEJd56ME-NkYkGZBoa9R0wbPGVCLnazAHwy-K8LUil6pDDdPgSsH48JpuylotF6bmjDrJxOOpQD1CQgElvjQAR4nxJbv8OSpEGHrreXhIrM6H97Ig17Nt-xpB64rGmYj9HQ53cU-fGDKS1cpnVfswQmu5lvKiDeJEtssKN4elISDwO4ITtE_M6LSdiGRbsg0hgp-URwUNt_D_pU1XFqS8T7FA15b9lRv7yBs-KJWaAXDOS1lIEb7CULvjs6UddmpF6YmVx12lmmum2lUSKxjex_PHoRmLFWtCWyXUpz4KYp-wJ_l7vQ7PAkUsJoriPmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcZi7B3J4v_54mMLaMeLbmyvCkRt4gactRhXoIeiHZ-AsCFJntWeBWWD1teE-raiff6dcsGETLsCRrIJiuJHzZex102YF0xsErP7Z9AoGBxeX3d892LEiEAAPHH3fpnF6ftl4I57kpboD-Nc__bQBfFKYQ_XiXuhEBJjoZMeYHsLXpD0c3QY5GoE5zJlm5fP-FHcR_xZky1Nqen4CRU6CmucOc-YqyeeZhaDdHMDOxGJ29W0RE_tp8SQW0F5eNwSzYxVKKT2yCWcNnXVkCxe4ZhTuajsrltArbYh-HSEBLH6uNdX97-xuyFvm1BW-iBDJNuLrltHtwoE_JQpUxwjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6tZNI3quD6nOf4FYwG3c0IY2VbcbEn58ULE3wTKPRplKtlbPi-7-8jS87Nu7mfOLC1PXCLHhS5zvhdfOn1AYqqK6A52-Cskg7I8hKO2DfG3kKdu9UDaECpeMX612XIwokr83JnET9ZggRZdtFhR3TzqZ-atjSD372m9V7GpSpm6gq9N2x86WX3A4t3xoQuF-B4hjVFMGfkep3NKgLURoD4e6pvYwnGC768bLTIIYtmDwYbN8TmIvNc1fodTbDN6RLZ3Q-etuzPdgkWnvbopPj9X4Z11Lmd9eJoVWh4hDP9t7fPt1aMvfi5J5BDBm0-9llB8QcZM1daSiHq5uHyAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5ww8_WuL8X9ZhffIX0cANU8Cql2x2M8EdHjpfp1PK1Lpormagvsmzkx_OKL2-m0SM3Oh00hE-XWkx5HL_1twwI7olFv4q3Fh7JH28bEcFTNtf0_5b-XZkOtpndhlrUY5aEbRCY_n_9qe4xiS20OzKMlruOWUCKe0IdfP2RQef0GfpV6vCY5hHT8rZ54zfuko9dOwmovbUKWJiC1HKVJESI-PFE8hVSEoUfmBzaNel7tCQ9z_5DaGFosWAAZkA_89eoCNWxhvW8QgafENkSMZZrZP0HZ5v7vqXUOO-XV_wbaB9PbuBv9zIhxTHWXmquwvqwub20bqYRsWpVwj7lHJDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5ww8_WuL8X9ZhffIX0cANU8Cql2x2M8EdHjpfp1PK1Lpormagvsmzkx_OKL2-m0SM3Oh00hE-XWkx5HL_1twwI7olFv4q3Fh7JH28bEcFTNtf0_5b-XZkOtpndhlrUY5aEbRCY_n_9qe4xiS20OzKMlruOWUCKe0IdfP2RQef0GfpV6vCY5hHT8rZ54zfuko9dOwmovbUKWJiC1HKVJESI-PFE8hVSEoUfmBzaNel7tCQ9z_5DaGFosWAAZkA_89eoCNWxhvW8QgafENkSMZZrZP0HZ5v7vqXUOO-XV_wbaB9PbuBv9zIhxTHWXmquwvqwub20bqYRsWpVwj7lHJDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tvUDSkJUYjFB9PUyVo4gQ9r1eCfgf3rzcFCsJ2fPssstAblgKdX8H7KWBdfUmjl2MrJNs076Tb2H9zcdkzNMhqLP9FTu0Qz-CAyvwMQb_RvezuXdtMUE1hmehazQhQrVd0qcaxpCJpdqCSrOaIPpuJ0nfbfyY_avBl0fs5dS4rZlx0kri8DSTTxXASvXFV3AO6-Q2QFOwjitr4uF0YgkHIxpIcvmo9y0jq48Yl21fxkY8g7cIh_IigdsMDz449oClfRY10fK-GTgjeLTtmhZHnwe0kqLWK5on06cd4pahObqKVgWEuym46s2WCdd_idFsI2MpMos7lHKqzWtB1ImjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zj9lCv7Pb5iqnQjoahkiqkhJrh6bYhJ7O_X0kyKrnSG6SsZhEH2WuPq0uMQIqn4yijbZTZxgy94sza67uhUq6zakvTM0rNz9UFLd2bE_NdQt2pD5p1xbjasr4pt4ozJdoO8aG6M5WxYcr3-UVmMMx_Zc_kCVBy67sP9dv8LaK8Os-feDr6i3kCKQ0ARnggROSfn4gVkEffHUR0KLkS1HnEsGju9gGu-NAPREsqTMR7CrOveGZu1cInCs0VAJGIt1KmID8fiwu6fP3SMfsfb61z0r7O_phtd1_qSg5m_D5Bd1UNcBk1dHjBdIu_YFm8354MUKrRzzDOiF9tvtctn2QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=mP40uMmyEQHrGCE_z58Oaw523Mup-TP-rP7bjuRz5MS7ddqHJKuf9hj8qRN_-kLE2-Ft5QI8GGFlGnfm_YVsvpWOLfK_tpHlXLr4zFMr_AF6sFxBle7M1h4tLOnnrMGXV2jhv4uCnJnEfvb642GB-8t7XUeEo2IggLiMvHFHRtG7vlaKmBwFLdzb2DwH9r0_YJ240ooXGaJaoquBANCs1qyv5LxLNPq9dK21j0Wxc2esbRazQgbjSVppki7-W_DFywdTmYzvxN-Xc5qMJTAy7bueGp4uYzSzOCAKgARev3QA8_2mR1TfC2pn9dWMFIf23RzyXAGqYN3_jDj_6qDDdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=mP40uMmyEQHrGCE_z58Oaw523Mup-TP-rP7bjuRz5MS7ddqHJKuf9hj8qRN_-kLE2-Ft5QI8GGFlGnfm_YVsvpWOLfK_tpHlXLr4zFMr_AF6sFxBle7M1h4tLOnnrMGXV2jhv4uCnJnEfvb642GB-8t7XUeEo2IggLiMvHFHRtG7vlaKmBwFLdzb2DwH9r0_YJ240ooXGaJaoquBANCs1qyv5LxLNPq9dK21j0Wxc2esbRazQgbjSVppki7-W_DFywdTmYzvxN-Xc5qMJTAy7bueGp4uYzSzOCAKgARev3QA8_2mR1TfC2pn9dWMFIf23RzyXAGqYN3_jDj_6qDDdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=oor6ZKRc4jZ3WSVFCgYhE1-j5grl4CGFG6Tgm0L3lI4V88jVFLzdYyu35bg5YFWP1_I1AraHKpbTM6Ftm223OZKxfFUlfjoq1nWYjQKsg-NKQCkgwQ5Or3jMjMKcyvvSpUns6v4E6-Hxztjrm-13iBdm3MVJe0cFyU7NjfB00P_XhunhzDVsSY4ZRr2mYCXjskB6UTCNzIQixwbSCxtGmKheJmDoWw7-3lUy868CWe_JxtEKIRcE7IPsrw4fMCxv48YWh-_6fXJ8IwgE-P3JsK5qucoGRqK3o4SDZ_m2NiDOH6W0Hz9ZLgNGURkUMHAg1a_GpOj6XRoimNuop-L2hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=oor6ZKRc4jZ3WSVFCgYhE1-j5grl4CGFG6Tgm0L3lI4V88jVFLzdYyu35bg5YFWP1_I1AraHKpbTM6Ftm223OZKxfFUlfjoq1nWYjQKsg-NKQCkgwQ5Or3jMjMKcyvvSpUns6v4E6-Hxztjrm-13iBdm3MVJe0cFyU7NjfB00P_XhunhzDVsSY4ZRr2mYCXjskB6UTCNzIQixwbSCxtGmKheJmDoWw7-3lUy868CWe_JxtEKIRcE7IPsrw4fMCxv48YWh-_6fXJ8IwgE-P3JsK5qucoGRqK3o4SDZ_m2NiDOH6W0Hz9ZLgNGURkUMHAg1a_GpOj6XRoimNuop-L2hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSfhQ3TvPadU1wv8Mz-3l2QxgtYtENS00j0nv1cy1mZJ1-uX3aMmRj9TAdQr6sDFeQCWmNQa8_DO01thSkS94_6TG0cX1GcsTFNsZdVUEZiWN6c8Z29GXmqiTQz4EEZKSSXFuJuivpk4Cjpgk0_M-e2A3PAzlhLWIWLUuxbbVWgGt1wbXwCCn5DITrLYzUf9NDsfjryqjQ5NV9UXVYFJt7w-cZcJxyXbm-PViaO92WZFaOfqDDNg2ZNeqwGXAukZW7oLaHCu5PZHe6N5Ihwf7b92GSLIo7bJ--X8dMoLVBP_XoOjMeEe5hKdz3liwYRN2kvdbeOP6TUrVQqqSn92YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgn0NtL1PhkyL8Wpirp-cs-NRLar9SJa0pW7yR6e82Hox7ygzSh_mijec2zC8PzKDrIcAkwwpgzHsb-pBcNGkesDJTkDDWkq-rMJrPWkbbiGOKp_r-4iT8DexHMwyPAIgU-pSMrS1IiCW3wXdOHG5dbW6mgQTVeyQz2N4_NmAMOvqtvmFmgIYq7BkROgC5GwpNqeymYkeqRlWcxaxPxM9UpZIoyuuRzSwVfW4ViLf6JyW_5TwdD0VjLRh7pDdgoWn674T6YOVR0ssWEI1qCIucNMQ90sNYXwYF9toshNy8-9C_4gy0cEqqKdL0c8tW-LTUCDB87uJKTtf5Pq-mLB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=f-_Lir9sMUDUdfhwUk7HHk2BUc2qyD__k5Ueusf-7rD1JxnuNyj-gyShr0MtueF8wE7UdhbU8A68vrKA6ew7It44XufvZGkx1I2S9iIRn39DOcupD5OKIsA1kHBf0tf7VN9sMxuvvF0UIbRsaTpm5ktacj6qQG3n79QUh96_fOeYJzVGoFsLpCpOjuFmyTjVgp_LRlJ9rzlWEkJRKU5YNccj1x4s_7_0BrAHd6Xybmc0KgJIWR4w6RQZFyyF7mSLLC6MJPGyfLjWLRc4wgYDJDL8c9X65hh-op8RZ2rQRtZ1FCAT_lP5McP-EJL5XeVLWrVap0V1iDrVgx5kDoXFLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=f-_Lir9sMUDUdfhwUk7HHk2BUc2qyD__k5Ueusf-7rD1JxnuNyj-gyShr0MtueF8wE7UdhbU8A68vrKA6ew7It44XufvZGkx1I2S9iIRn39DOcupD5OKIsA1kHBf0tf7VN9sMxuvvF0UIbRsaTpm5ktacj6qQG3n79QUh96_fOeYJzVGoFsLpCpOjuFmyTjVgp_LRlJ9rzlWEkJRKU5YNccj1x4s_7_0BrAHd6Xybmc0KgJIWR4w6RQZFyyF7mSLLC6MJPGyfLjWLRc4wgYDJDL8c9X65hh-op8RZ2rQRtZ1FCAT_lP5McP-EJL5XeVLWrVap0V1iDrVgx5kDoXFLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=EVXO4B2XVovkSNtewtKAL1Whr6A_HOY9TICEhgRyraMozcrgJlN_jMPddUiKY8Ru-pNFINAobPSuHdbIPqPs6o-RqpWOVbKfqsAo_LpES6pOQKV9eUbrby748e5Li_RC1sEbeI3PqUy-tiXlRvUJlx0a1holPbZrQP0m7Jfv9_lmv_eJaJ0tNJOJsox5nmBeopAxGhJNIFy6f8QmVzaxQQcPuXORH6ozY_JRuZtL_ILGAeVUmOYQvWZ5Teuh5nKtfV5xIrK2q4AqTJNBcfMnLZYyUSA_Dyz37HfSt4cZksNAD5xwbrAsmcmnzZH5FxzOKR7_v25nSY2KhwS6oxrZYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=EVXO4B2XVovkSNtewtKAL1Whr6A_HOY9TICEhgRyraMozcrgJlN_jMPddUiKY8Ru-pNFINAobPSuHdbIPqPs6o-RqpWOVbKfqsAo_LpES6pOQKV9eUbrby748e5Li_RC1sEbeI3PqUy-tiXlRvUJlx0a1holPbZrQP0m7Jfv9_lmv_eJaJ0tNJOJsox5nmBeopAxGhJNIFy6f8QmVzaxQQcPuXORH6ozY_JRuZtL_ILGAeVUmOYQvWZ5Teuh5nKtfV5xIrK2q4AqTJNBcfMnLZYyUSA_Dyz37HfSt4cZksNAD5xwbrAsmcmnzZH5FxzOKR7_v25nSY2KhwS6oxrZYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3WHNsY89SYUhtb4jxvCWYd9yIMViVKhKPf06stVzqNtCtC449YB_UC5zD0AgJUTqzuqbdlGVBQlvtxlnxgiHiJTZuiRteG__b3x6sa3xa6LtsG_-rvB5bNTqoMM95JxGX_6COMo7At_z66aRpwFUOl03h0cMAHAVqJcdQnQYHh5E4kZidHnSaurdGyQ_E4kxJpPUo1LTIR5ZgWnijOAGbP-flh8hXFvUKjfv6HJp9QOzLfM6SP5ut2KBaxJ-kVdJRYr3N0ATEtQT1jGMFR5wYOEOHVyCiIg86j16DTC5WZRP2SXb-wSXPeiCsCcBUo6DnzyvA3eKEia2DLX_jddFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoQOO9fGK_NRRwURDOnFWKOmHet4a0jPlxmH6hhtJStlLggRasD_miVWGj1ROzl8lGr4-MbD6MinIB1o1SdduUXwseE7W4tHoY_lQwW_niLyzbrzP7ZKnHFNO4zdpatylND1wOtwNb3qib95aBAKqspuN-jgWn2NopwveGPq6DGCxXFeEsXim7A_NkzMOjr1Cgfs6kjfZQ90n3OyE65ssSydixiWngfx0bACn2XYtb5LRqEq9UzU0OjHDJt9SqfLgIdcdgOrP4GjUDRH4qlaRwY9sRGnVv4ZlEDJeEZjJELQANNCXYbOH-aeqCn8mdZD_tsQRVwFvwdjUf2k-3SNVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJS3Ei5uW9kDq1CVbQZocL6ozmBCj_ICPCAbeHZazhpNR-J56HwU6aet4DPjvSS4DdZ37WqovEsV5Wq51STZOKAgzuWmZ5X3ORlW_BstSlFM4XTzFBo_8-x0NCIYsOqXgjysxGTTc5qeAtDv2ABaOgM47VP1r8TIgb9eU5KsIdXzrnwC6SYmJSAoNOLHbZAc-IXd-E71uLfDe25iSzljEMy1OvdTuQRPBy5jUhManVVrWJgkSJ2YUNH5XXJiegS1XSL4bc9tuQApofBS_VMnncf74kJR5QuUv_2RtJ8JZ4dRmH0XDF0oeDrrZaQxKR0nCuf1Sxi8SzNqCsQBX7Mbxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1mNsE31xdN0eLvrmKzpdW0-LsFawJE5ovF8KeX2GRsmIVDt9NHNXbgS-i5eWv2tuZUiQgbS8Wtb4R41cr5kJfJnVNzqma_0BdfmCC0eMZdGLcbdUASiSVN-y-f6qk4SpEUctrt-HcvEspoHMxn-gg5ktBuKiov-w6cVBRKH6UZgEGU1HDuvXKndfHpiq7sDSHjBfop_e_yt9Ly9jl509-mQE5Mvxu468Qb3luY6vIUriW6jbsVU-N2yckRGszzDxn4rd9_D_CisMeDp0301-FprRca7hkMlZnhEBjT7X7DuRKZAgrHMGk1lGHHPC8VBi_gslwkzwK1NvK_-8ePEKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJo2F8fqJA3LVRR5V2rKM2cwRx5zX_diDOn7vOqgLTcPXyRbZfVNkzGW_fjc4P2k0F1P7MpGGZ325I9ROygNTO1EgfTQOgmJ6uN0gRli7PrqAhCMZlT7iVPbq8EjQppXpcejYs7IRlZgHlmwn84iD3ioxw2mNUW933q1yMChMCJWN3E4TziCzRwK-k0jUwfjhxja9vHAP4mtFtIuEosNc91Qd0DQpr_Q0wBl4FqSgNsf4_olhJR1sRBUGwjWqKBlqCPCSkTNNAZO5_UtvYTgxc7q7rAWzRf38trXFlNM3JdioUZr9Au2oSwxuen_71idgy-1tQr7mzdTOFUssMefXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQVdQYftEyoRnsBX8zc1YVIO_C9MOEjCyXOc0PDIb1dkDp8k0Ni7fh2B5bYsR7BJg8GEzPKcoSTeEdBohzH-znNzJxfgQwNZcVpxbAHB0leTsCvGDhE-tQ4kR78hem_Z7QAr0eHBQ002gCFAdEolaa7I8Y8F6KTuHtf5pmmqdLVREK8gKTldOYY1wOxYounQSAuhoy5z-pkWGPp83_rRSlrcKwMxr2wsPnju_ZyROWhCrz3r0m8HRssZqovStY517Bk4MK8UhUA6p_f09WkM428Knw25qZfANlqq1mxGOAuGgpjfy5SFOK5os7yN1_tqK5sjrTsiClBftvAvJm0G_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z78MBQNzD8mmKoFZBWq75kY4Q5z0co9M6GoqbS2S8zQ2NPseHdYGKcnSYNFq9behaAlLpPYZZNPI2fj0bYZxUxaghnp01WiUf7lM_N62hIzTGr7-eJvIUdKhhg85ZydZ2GSK_i1kiCraOsv_x4y_7GCRN5e2oVvqbVI3rUzZyzxWSZlfxMmIyT2YVkYueujfCd9EGgCbx-F_B_CcleEQf33pnPiMfP7JUMExmyWStFLcqq33DjWv2rNiqrNfTfDtmyHudQwZaDeR85bQXZRgXCzsHjMySfBsuaXRCHbiuoxZEo8TkHgPoRfYT0g0yl-BXkmE_zfP139j8X75SAyfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OAxRyIVgeLUl5z3u8HPaszVjMCGCSvL5cUH6sy1-ul_cAjde88BjIcJJnAJj_iYoD_nhbQdb503e0As1Hoh_sgbRlTKuOKbcz-khOA0KKOjZsFyYgFp_SeHCO2uVIImjAWb2tzWGsv6p3F3m5-odJSrV6z42zALvRKiWgBBRjlPXWuAeARBlKri6X5xdH7VRSYahpuSDYwPxVWZcj7xqgHleUdeuVP4o_WARIawvGJaGWb0l5PE4a8PvFtE2K19sOZBMuv2T5pddM528sTX9puEwUvAsSujLfZ6A6XSJO1xEtLxc1wJLTPAmMXc7-aAiwlaD_5j7AhxaQfYEaX5cKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0s--lFcrCUEXRf8qWicG3oCT5TAZ-OZstwCLq7S77_8H9H7ahskyVrZG0SMBRC-j7nGasuBfTeDnG80l6ELBupWmPhXQocqDC8OwJ6RROcvpjP2fb0oTfUIXH7nPVwa2zSEfYPMILRK1gitcLlY1NaUXO6A7IoEOaZd4WxiB51-yQnhWZsuj_ZrhQmBHqD2WfQ4As1-NG_tTeyTJjulKfhQam9LCJjV7vNLVNwGii7ypoHVGbOtuIsdyMflN4Gkz4nTFpbMDLg0JJCV_mVnlqUN9KDoFeH6ySvVnuDz369QZBH35eTffSro_--Q1hk4SVAvxjD8XaVt6_IoYV-LcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p31WBVNxTeuqK6tHcfxLu1sHjyk3IBhkQopo7BSNfqZYM8zDWYQ0Rnio1Kj_DwX4VmKw0dTpdFr-KRLFnwvIyWwBE3ghqp2dnH-geu9IUBWjXu6lp-NeCQ47O8_k2k01HzltdXy8KH3FNRzIjswNKcJA0_JV-h7QOicCNVxDL6FUrN-EUnF6Uj_6XQXqQXGG3zLMYK0JbPZym7TQdVKCgrGPwXnH6jS8HvGXsGT3R2EDEIEVjGHVmKnsL4qKpxCymIChAvOJeShK8y38A1t-F5okgWPewF6-g0JqUZClGoLlORkQlTbB_KH8Urb1TCZoncBFdci_PKtMqpV1BIOZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=t4V2ooEI6IMvvXTMEjc9vJdoSHZ1c64doIbDQ_WkmkU7w7J8joGo4jLNNd8upAOMccHinOiL0hZceBh8R6momD2ML7qY5dpTr9-99vxr96k4mpLkM4FsigTY8MFktuH9p8-1NTxuwBsU5Y5XFKFj2q73bAyCicd1h8Hm0cRiD-kcvi8mm80hDLm9AhPMA0YftuYyo7Xp-RG5030rQCo8hF6cMvg-HExU3eJeE9obp-SfZ-o5MA7x2-9ZWetCyiAOPSJ-2XzPGIjGNqXTinjRMIXxmHmEy-BcP-lSNCndwQXGlkxfguYx5Fwawh5B3efLPXQGWLFcqBJXLDoza26yUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=t4V2ooEI6IMvvXTMEjc9vJdoSHZ1c64doIbDQ_WkmkU7w7J8joGo4jLNNd8upAOMccHinOiL0hZceBh8R6momD2ML7qY5dpTr9-99vxr96k4mpLkM4FsigTY8MFktuH9p8-1NTxuwBsU5Y5XFKFj2q73bAyCicd1h8Hm0cRiD-kcvi8mm80hDLm9AhPMA0YftuYyo7Xp-RG5030rQCo8hF6cMvg-HExU3eJeE9obp-SfZ-o5MA7x2-9ZWetCyiAOPSJ-2XzPGIjGNqXTinjRMIXxmHmEy-BcP-lSNCndwQXGlkxfguYx5Fwawh5B3efLPXQGWLFcqBJXLDoza26yUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=Cnxsh5mY_Vi_88ESjmSRDZtKr4S3bHohWC45nhJd_vUnAB4mz9yZH4nV3B0j8-YbA-Ywi3l9wJWlWc1UCs4sCnVRXbzjjEgsnAlb56Ev9QPclOsmdALhCwLB0QBk4FPgQgcERGHhfojsroRRG0QCjHclfKVqzUGJukhe3lhY8z-ss5wNTzXGTpQFjmNDYFqIPvasH7O6KJPPQneYRqHvueL-Ma_S3zos8IBzRGLWMQllRtDIskbW0P8LNhMxKgNGBoPqkRqt_mvbQxlE5o9V4sF60NVN1wJA_mWOVrTf6G-RY_3zg-uwVajBugd8UO-OcH3etDOKpDpYpJ5yYGifYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=Cnxsh5mY_Vi_88ESjmSRDZtKr4S3bHohWC45nhJd_vUnAB4mz9yZH4nV3B0j8-YbA-Ywi3l9wJWlWc1UCs4sCnVRXbzjjEgsnAlb56Ev9QPclOsmdALhCwLB0QBk4FPgQgcERGHhfojsroRRG0QCjHclfKVqzUGJukhe3lhY8z-ss5wNTzXGTpQFjmNDYFqIPvasH7O6KJPPQneYRqHvueL-Ma_S3zos8IBzRGLWMQllRtDIskbW0P8LNhMxKgNGBoPqkRqt_mvbQxlE5o9V4sF60NVN1wJA_mWOVrTf6G-RY_3zg-uwVajBugd8UO-OcH3etDOKpDpYpJ5yYGifYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=JJJ8rl6PGi1vg4kXgTXTMXjg09FarNAIHq-quFVAqlrxbZGNnQ_xLm03HIUKfDw_ZfyiJtfyKjek6_dnDylmKwbjfkQUdE-dbX-I4GTy-M-qns7uK2Nv0W2XX7PbE1Kk7AzfX6AlPgdakQNCfDBhSDOkJqldhnI9as3i2cLJ5Akh66NaATX4GTa7LO403xApHYENuHWAsH1T4hW6bIYmeqUFvXaCR1G1humCAg2GN_o3_tDIXI9QS1XJe88rDEgsvtcW_NrMx4BoKPFoWcZhh691GZ3--vfocZiJp5u0ZcXsuWyGfh8WVV4wKetwP5xyLU8xngLlgbsiJUtSlLosvEC5ZBEAVQorjWvmDLFFzTxEUxLgA4cHeZMjatdkyk1mphno5q5pQ20DXb1SADP4gj101Xj_pU58xzTXjcqnDIGbRyVBdBwyY6C0seTkPhElYRD9y6Fpu5ujyFsZ-8ZCOwpgSW8RWsRGCjzELo3kiegDAKw0nUqMbSUyFojt1Pj6QR_die7Enh5dxS18yL2PNyxqn5akiA_uomhhix3jNM0Zpb6C8p3838Gkt4XXgD4Q_XE2C-qzzEpJ49OBB_LquyPTQt5gwlmOI7swprH80zOZUUS8ZWxGMwb-awxziBFwxXRhp4cWzxxr0HZlKvXMRHMbjjFhZPZutlOinj-Px10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=JJJ8rl6PGi1vg4kXgTXTMXjg09FarNAIHq-quFVAqlrxbZGNnQ_xLm03HIUKfDw_ZfyiJtfyKjek6_dnDylmKwbjfkQUdE-dbX-I4GTy-M-qns7uK2Nv0W2XX7PbE1Kk7AzfX6AlPgdakQNCfDBhSDOkJqldhnI9as3i2cLJ5Akh66NaATX4GTa7LO403xApHYENuHWAsH1T4hW6bIYmeqUFvXaCR1G1humCAg2GN_o3_tDIXI9QS1XJe88rDEgsvtcW_NrMx4BoKPFoWcZhh691GZ3--vfocZiJp5u0ZcXsuWyGfh8WVV4wKetwP5xyLU8xngLlgbsiJUtSlLosvEC5ZBEAVQorjWvmDLFFzTxEUxLgA4cHeZMjatdkyk1mphno5q5pQ20DXb1SADP4gj101Xj_pU58xzTXjcqnDIGbRyVBdBwyY6C0seTkPhElYRD9y6Fpu5ujyFsZ-8ZCOwpgSW8RWsRGCjzELo3kiegDAKw0nUqMbSUyFojt1Pj6QR_die7Enh5dxS18yL2PNyxqn5akiA_uomhhix3jNM0Zpb6C8p3838Gkt4XXgD4Q_XE2C-qzzEpJ49OBB_LquyPTQt5gwlmOI7swprH80zOZUUS8ZWxGMwb-awxziBFwxXRhp4cWzxxr0HZlKvXMRHMbjjFhZPZutlOinj-Px10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این سخنان «موسی خیابانی»
فرد شماره ۲ سازمان مجاهدین خلق
و جملات و کلماتش دقت کنید،
اول دیماه ۱۳۵۸ دانشگاه تهران.
انگار همین امروزه
و جملات یکی از سران جمهوری اسلامی!
که داره میگه
«اگر ما اهل چانه زدن و گذشت از اصول بودیم، امروز خیلی عزیزتر و گرامی‌تر بودیم.
اکنون هم که وارد این میدان شده‌ایم
باز حاضر به عدول از اصول خود نخواهیم بود.»
یکی هم اون وسط فریاد میزنه : یا حسین!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtP7ZF7tbTD8I1bcz_Nc3lWUyPj276fszAzUM0dnkKIf8mVy_IY-k30ZPZmVnbYxJ__3J_gP86zfpqfaUJdWAKo5sVs2sI3ge4pKXiGz1Y2sIrC2kBCfdbh4RQo8tv9SNvAnsOeyEWa0KffgtvWpwxJsTWhw8GwAuRGqUI2QodOx8BE28-UBFvHuRvF6-lDICV1d2qWV8BmP00RDktDkMWm_teYPMfQM1V4UU6XwwwcPAisqWEVsFhj8bW5MahSVOJ0rIuTHicN7xnbYnfdgp4bG5l5HWfjY8Si7t0xfM5L11FGPunrA8M5VtDYo7gv4PbjKdhmkX6cv9kdSA5wV_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=JGxfxBRhUafW9pYE9zwAaLBOFS44G6frkkFF_-GklbhXHdomzdgjDqzxWsvaNGY7R1hCXqur-1KQO_wiR1px9LlcjnBtS6Tsai8M4EAtfiKm61_QYm9KaHReTnRrNGE4Z3sHTYlhp0i5Kd4qAWoFKJcvzcmce8548Cv_oYnlEououFszYzDfOPEkByORb-TVYtGvEyv5CQl3y9hRYDK7m4aPqfvA96MCAWP-GhDDr5UgzigrnA0s2cTu-KE9RzF-i2oD4CydF9GH5MOkt03QNswlxXD5jFPOFjUlitqxY6RTkLy43DScAAGnIuYlB6dgfTXlEhW5PTCG4kxok0iRsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=JGxfxBRhUafW9pYE9zwAaLBOFS44G6frkkFF_-GklbhXHdomzdgjDqzxWsvaNGY7R1hCXqur-1KQO_wiR1px9LlcjnBtS6Tsai8M4EAtfiKm61_QYm9KaHReTnRrNGE4Z3sHTYlhp0i5Kd4qAWoFKJcvzcmce8548Cv_oYnlEououFszYzDfOPEkByORb-TVYtGvEyv5CQl3y9hRYDK7m4aPqfvA96MCAWP-GhDDr5UgzigrnA0s2cTu-KE9RzF-i2oD4CydF9GH5MOkt03QNswlxXD5jFPOFjUlitqxY6RTkLy43DScAAGnIuYlB6dgfTXlEhW5PTCG4kxok0iRsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZC5j4Ly8PxCfRcm-xDv0yZWV1sUWNecZKnf7057oC7PI0Uy2QNhtQ1JDzSHz2M0ZHtVmhr6pIRqVJmaR26kAbtKULIUlbHRrc5TIGgeHfThFGNkHADaNIJqDUUY3NvCYX3WLYQvX_5TsZ-PKAf5dMKxi125wuvIuJr7Irn_a8OCtDK4F6zjT0SMR49HSm67s5D9gqRG121Z05jPEbOtiA_Df8qW759yf-3DT4a1k3jyFvYfnoPxqKOWUdemk2EEgnALPFCIWCy-uzhruj80KJ8RMrLf6Z5WvT1Tz3QZXJFhIyLwIJJcrU9weee6nqIrzWgvqBBk2YVo-gNKGdRX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5u2VtcTcQabWvdtNQ7ZaW1nqt2LqkLHkgGIhkpkGT-K1FCFgHwNAIYrqC0zqWfbVO86T0HWiYtQlQ5HaigpihG0NLXsvYhZUeJQEE0c6fx4glfUaoBxWBsyUDb13zsQt6-PHlcymKOiGq_Ns8S9UnOX1RaE-yjy-q7Ekm0u-u_B2mQiu607VuBRzmBK7JEw_aO189EU8xmUuF43FU0qv7E8FDUACVvIZV2fav8tfwF-s8Xi-rTAVN0xdmliMgJgeb2xxQL-nGlW4FLr-8KT0iAKGnmU1Z10ChvFgPVQGanl3ztd4smnww21zL3ZYG4fFa58XPly0AvHMcpWVLwsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Syg6f2NPkOi_B78BQLSEMEbxErroVYqKYJV_Uy37655zsFpAB_qXZ55vm-viCUGFFM7b96DDc0gyrialoetJIsfSfDgB4wYnpFxZ7xGSv-YqVWJH9_d9FtT8wW3ALk8l4IRP7cGk-i_KIm6GaQ0AquPjYmX3i5meWR8ntmevFfVtBm-ff-FhGPihWum1X4pJoIMiqlHlCZ3vkso_pWFrR34SJI7ert6i1HO3ukLHRBbHq3KW6CZrDOU_o8d2AOEx875mh9_2pfe1fLxcc0hLwSKVYVql8IHQ7Ib1Wzg8SrN_baWYRoCUcEolSkQBh46uRWRCWDcpv6TLcQjJemQEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NoYaT4FjynYwnUchv_tCtsRYq3Fmdj7gnm_2EESW83Fz7ec8I7FWXAbq29l4WS5UVx2wyMEb9nRQ7P1ncghM-XRimtXlgXRXvMBYM3rssnqHwlLZFZ09CEZpfJ0MjUkWl1IVcik_f0qJcn_2OzNA2Fj3O_x4k1ns1oawhfR8IT4YiiHNi3muzuIYimqor3odfGdd1kcvF1K5BAikWiZ9tVutdS9peQu0bcjmQQcyYdC6GgO_8RKme-AfMy_ZFGRLkUoOb-cLUBL8EU8XIfQ3iST2bRXilQiZPkBHotEN7Omwp8Hjtyu1OtAhkW43L5jGak1ZEn-N6D_JFy8tc2O7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OjbVAQ-_sGaXdU1fk5N03L7wPDI7azglIObNibwt65uVBFLonl8SH3cAr6wcd2oh8F6TC0JaJPwYI8XGPCtpchAJcSnbCNNNMjKgbrY2rp465sdYrdXuCszr0P4bbosLuFKeuxoqYZ_eSnBqFtqOd9bdhBb9N1VLITVayjVbuTtE_FZNdwdsDvnw91u8kXBtQypBQ4W6x1tiVX696idt9Eh4fEvHm9SefMHV3BvkwyKXT7ukQW5a21eoazCIrrv4s1DRTx40eCeZqDtxJi4vZXLxDvvNFqQ6qg_bBVMkTNPN6kDw8iVXZbEb7OAmJ-rDjXg4RmA8bpandD666dp2ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYtS0PRNAqayBxuxHIB1C1sS4lCtw_PQyP2IN1AT2qJkj_NzQxHyRy-_DECMhgAA8-5B6IXpw0VWkd7n6b2Qdrz7DFW_bHILK8J5B7zeiBBPsfEkzMir2Luh1bFsHZq56C_n6QxidUm77x5px7P-8Lt6BDigL4qfFygX2WsJcKV6FVM7DJCOm9JGDT760pzrt_A-LSrG6640DhMlmMgvZxGbMbovcslMMYFdFn5QfrsC1xnST9PLAT-FzG-p9tnLOqPdw6jxqB6RNaq3ydCK-n80jKNwLYz4W90fO_r_aiNWhiGRmNrsZHhRfSNgBqSBjgn4mZ1RCh3JqoJVfTFKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9TVR_E6Pv3h5uVtQXsLI1dffHlQIxcsCyjM8Q7PwTEQAIEy5_rvxIMu07rgFTqieCWglBB1d0uoJPQsULDAh2JHcp92ikf1-Z4_nhPrc9aITgX-kx2mEIS5_MMxF8FxLDm0b1ki1hWCbePt0f35j0Z13qWftXU2RM2XPkkHqjHJL8e9RnqTEc5yJvCfoN0oWle6DrZHMt5LC9BXAacknIUkisI_DSAUOQ_XLuIVbI7o6feuK1dYERLW-vCwWQM6jdygC6SPjVaYzC6RaU3PZ-Le9_AgXImA3m03sQSG2K8Ldpp1El9zMCOe0CcZLfrhg9GZviPiH0U88-j4eNwXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DskpLIPNMPuWyQ8ciOXTR48YQFmQ6_f-tuzt_NbwLHJ6GsNERmon2WxiCNL9ssLmzJ1ojodQtNUFFHGp4uLrkjOeEojsrUdHDwb-EqnPPW4nfZ49wgWthqb6X70qotd8K4w4EdUop57SnK2zN7GVbGWAsrm8x6ail0nDAMY3erzgGj8C1bOs5xFSD8XoslgQwn7QmyI8Z4yV4Vr9kOu5K4OyAGShepSGcaTnTrQgg7ZmJoIMIexRVmyMcQzgJpKuS2okhG3r6dd-tk7pfTUJTHIA0yyGWkyHxenUaCHHkZiZ0G8qumiHZKAZvgS3twSZBHzhyqAfTN1Dq7-QsST12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CucrOt0ONsvPgoDNviX9C_Nl292ZR9uLCov0l_gwdREj60u1IxQnej2l32V9JdKYJnBnJUnuwIA_l_JmNv8iPdQ-ETVVW2WLKbudO_GEVGbY9r-1kgZALFLg3IsNht14k8Gjp20M-2-9QhPpJV4CJ_aheiMroiKnnuNoNaWL5pmk1TTJUBbQet_UGh1UcSmyl2LUe8WotDN8PzssujKb241UPXgP6F9GywHhytdlILpZ2IiK9tySIlhh0gRF4dKQY18Uxe53aVg1bVqBrNUNJDuNfEovcOic7rduRTb0TQa5v6koXx3AUNe674m04M8SU5zoh-g7dRRVjES99PeEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qY7ZC3AEELUitXVndZC1mCC2dCRhSCIQhCyV5A-MVxoU_N7OX5Z4T0EFHOJE1Jco3a-ooGRfKeEmEk3gr0d8K0POOPxXUnpzaW3Cc6AXnKIRTLWgptUsnCRgfyFsYurS23iGZnKNeYxoZpscQy7OtZJ4CaLP2RBU3mlF__hI7m1zzAwu2AjaiqjX5reJGXrJj3y2vdrFZ_lq3MUEYSGJusj5dmVDMlW4sdz_Kq-XzLGc18UlZwGLmd5wYaM0uIPQ8L3w7lfljRFJxb0REtq674r8IuT1pTFuLoJF1tjMBkkt1nIak8cjsz2aAbXABQBUbxOE0LLoG9xsjHrfXKKusg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg8_-9h125Ses5ALNUv9s1TBIxvokYUSQD0XIeMf2ZPe2XxKHzgEkKuOBqsP949YyOUMcM0f57OJBQzDAoyMSbl7M7rIbMZbs7EzxfvCKh1GFf-NnE0z8NNKmego-Du1TUD6C_n55WWo3qGMWFNL0lkHfNAmwzhmZjTh5QUNNJZmqkKjVts2azsCQbcGomo1HsZ39bcZZqRIy33bR518FvfDEdQuUSS7UZvN2BFp-Lv-qCEIL_ttoQUifEGqBMLEkSSnxEWrBFt9dF644oCamCn1yIKNG-Uc0RwBmgmKgduxofXp4nDB089PCd_LE2VusmtVWXSEqaDUQzehShwsQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw7CsVCwqMVbOl_jjXwx6r5HOiEJZWWkbrdbmcy7B2tw-k4fYcYnoQgs6B5oL2tCnlceMppwAvGZd27rH1ThzQ1keXZLE-0YvESz1i7dQ6gaJbMNbWvYYZsKRV01klKQfQFn5QsG8FFVseGTYIHgZPTrBKUhvsPzd--PHFJBIQxe815OCnqBduNrKeMGFe8nYreA2QESapDKM90Izhmu_Bcgt1ctfbYSHgyHwRLyGWLDhQGhS3Nyo7fIAiGcUVGhBZA1xc5WYfijjTkzhYoSezyjd-Rh7ZQN5UMc_C7JhnJBVLaCoMh8z-mENT6bx5nC3CEKIyH3bLKeMnRt4aJi-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RUh0TcttYsnbxc98XzD374Dfx437GnHGgwG1eydk-WxJrzBGC-7GI31KclQ_79C69KzW__U9m1YkpS45x18LbzhxQg1G3K4pdANVF0PrQBFc2bW_-a3cusWulheXyPFrG85RnH8z5mw2g5IEVukmJB3585JtlK3PQNNKcb1sk9he7MAA59tirU9mV-QamdxLk7DuQjbbGLRTszASPI8dUSJyajMQPKyg0biHtaAcpDOWjv3fh7-kYabWl9NhNZ5kij5dQiTN6ATT9ZlxUDmhZeL-WOQV7iNaElaNMWTdT-30SlfKda8HrZb1lG7Oo2qGOhtqg3bS6ci9XHFjnA0lzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLLDhIDZpnPupWibkLmsg77O4X0TKYFK-uIKiK4XcBVvIqFhovKdGh4WJWtWktuVjqcUoP-EXguCCPX3E0sY5Xr12YoJYQ4a0Mb3nPj_KfHFy0LOutmra9mj5AR5bXYAkFoGuSku1NU84E2Ood43niv2xUYS-ZUkEgxOfWmQMf8L5b6hZtlV7uF0Qi5kXRGpD5iSYlix3ZL8JdczyPrFcosBvdykmWiNUnW02OBe76aMV5JgZr-CWC5VTBC1dyawxEa2Dc77aEhTHVQSw1wcXUyF8CdtfSmvXumwcbpfwGVIQTj3FkpMsHt-GMqHhY2oeZd1yHc_LAGgzBh3aBQjSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینکه بارها نوشتم، چپ‌ها، با اینکه گروه گروه توسط ج‌ا «اعدام» شدند، آواره شدند،  نابود شدند و ماهیت سرکوبگر جمهوری اسلامی را به خوبی می‌شناسن،
اما نوبت به تقابل جمهوری اسلامی
و آمریکا که میرسه، یهو مصمم و قاطع
میرن کنار جمهوری اسلامی می‌ایستن
و ازش دفاع میکنن،
این یک نمونه‌اش!
به خاطر اینکه برای اینها مبارزه با آمریکا
مهمتر است! اولویت اصلی است و اینگونه است که جمهوری اسلامی تبدیل به یک متحد میشه براشون که باید ازش حمایت کرد!
و این روزها خشمگین هستن
از مردم ایران،  که چرا کنار آخوندها و سپاه علیه آمریکا نمی‌ایستید؟
تصویری از پست ایشون و یکی
از هایلایت‌های ایشون.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kL5oLolhEedYo1sG25fRuf30vpiEHbSgH9ywua-cv6Ndm8t02xFpkTtgYbtz79U7SQWLLHeCNwW24PIpk6gzYww8dOOC2ywOOQpqTDseXulq3rwyx8djTWV9FsqJCRZTuCUfdz_AW1uW-g66uFS7rYin0JT4nZC1NIvHrVhctYf89mPPjm-K9o-yIFufUx9p4N2U74dClreuybVGtfFfv0YC9TPbp45QjOc1WlO7VhZg89Kmag9Wo1Z9ZTQ0AX3S7BaiIYn1dsWgSc0hkMp377OX7U6GkxdZTjCo7qG13XICf_W80lJY8ehZIyiSVyC5SDFvkFh763_r6M4wSvdt6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRBnu0ZGOxrStFjHpGTKL5n6jtdzn3YIEjDpV1WdakH4JivLSlDciyCh5Y4ro1gxTSQe8vpG3ULEumQKQTJBvaLsGVLo92GwZcAdxZE08DxriS1sW7SAq49Ygc8svyPrFa1nsW4jdIBNXp4MLVzIyhhkmJQ57qH5Afs8Mgg7zlmZa0LPfvnnyOVDmz42W0HjWg5YkWlaXC5n3MPBiEsfc1mMVvLradt362A4XIa3zcwgYwiaQUDRdRluMNiUkWZPuf_0N4yxOrSuxVUMw90zQPJ7Mv8-Gvszf1GLu5Qcu97OQXIT6Ap-VSSRIvpZhpJ1zE8IgaknRjLUzfZBirkcZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X30-amOwv5wCB1qmuZfIAhcw8hdFkpYgbg56hK3FBtjfDusPXT7fOfnTdsSINvIPyDk3nqaJ7yeJlCX3NcQMwO_efSi_8wDukDptwwXHXK4NQqdukMgOYV7vjc7CMLdt-zoMvN9nk18xgN5mZPhkfSKtfiqs6vnPOkCFisYI8CO45Y8A64xcj2-ZC7dco3BDhH6TEzSeLyqnPDFbXBhqahKjBqG4V6gJLRjumdUEW03ulZJ29gw5VjnyOc49FIfVbmA1NqtJbwdoDZvqBlMX2SSbiawFogOFF3BAFu4-9dz5WUjLr1YwMNuiycJQDAR21hjw_g2nIfYp_21IZedMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=RCgkTEZ8UcrgLgd5jqHAlZ9pomJKuo3XLB5389WF5MnwKQAHI0OJhceGEqfa9xG6170CLdond_BLMzHiYqQ96jZ62HSeaZxwFXW-2cLNggbRSW5PmZNTHxh-DW7NzueOxYbvpWBvc_Xg280xFnW7i0calHHLEuMIVP6hYBd3u3lgzN0fvNfzVMeLMQ7XTcmgNTLfmNxzKWlWV4c8vbZ15j7GZz3yq1XNLPfDz2h4J4qETvZvq-5qKlFaVKGyIZVW23ig-8ErS6lvELAJxuI-AKU4NBY1vnMH-DFXWfS3IdG_9Yebi58Z-DQt8WheHlOKY8ZBSwGBDGwR6FdAunT3Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=RCgkTEZ8UcrgLgd5jqHAlZ9pomJKuo3XLB5389WF5MnwKQAHI0OJhceGEqfa9xG6170CLdond_BLMzHiYqQ96jZ62HSeaZxwFXW-2cLNggbRSW5PmZNTHxh-DW7NzueOxYbvpWBvc_Xg280xFnW7i0calHHLEuMIVP6hYBd3u3lgzN0fvNfzVMeLMQ7XTcmgNTLfmNxzKWlWV4c8vbZ15j7GZz3yq1XNLPfDz2h4J4qETvZvq-5qKlFaVKGyIZVW23ig-8ErS6lvELAJxuI-AKU4NBY1vnMH-DFXWfS3IdG_9Yebi58Z-DQt8WheHlOKY8ZBSwGBDGwR6FdAunT3Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1quBVLcaETFN3_ddaeADs9PB0Cb9JJ5XDNNVqGC3RMHq7tWLQ__4HYG5gwEOFNCT7ONl8sgbnrZqBVV_FMKliQ2xngFv9fH6Xb1tNWF1Ac5FrEkXJJ6W3T8W6T53mZwXeWXWTXLnb3cXVG3g2WPOAqgwwN3r3mTnolkVINn_8UykV6_GWG90PeZlC43YWSK6UpskYMab7WzWmf7So_hi5lo87PsoHQ7z9aFSgjE5rLhAdha1Hs1EyDx3Wg_2s3hPPYTuk-EhUNUc_pjKJZFfRjy02VtLQgtCwUtWBif2TV0um3wiBoN-vOlh4Ge1L3TOZ8pqXsKq3FS9DJ2ThmPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-hOcTGgoe13aG_mbjyo5ntKhYXnOjCg0a9qgrQy0WiPPmNAGuuy-Quc1iVklo2AqAaOuAqrmle8LUWkMUT9t92J6cwH0ZGOUlA0tJ4E2li7iEF1fsCxanQ4JxXUGREn8VgqKWgCbuO4-zFIC3VN4nLav37bEh-qMdxY9Wt7_0TwNlmvIy9N9XmsjqR_Y4N7arPYchgM90bU-o--6hHg23VEv1xNmNe1D2p8vhHPNKlX2lJGgGnIllG8jJjobh98fSqcZsoY1JmeNWUd0623oZ1elPhY6VKAAfJC8dEF3nhe8KL_Lb2rbRP3S4g8x47Iegn8tTwRtfanjPAPXZSVvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1S3v2pN_XwgGlNSHXK1e-xAuqcPsKn12Q_XY3XFIJrHICWvxhtAkD21psxUvmIv5jLvoeAwqfMn0_ogwrolxgO_R9UV1Jkk04egK9YWuBwfCjwthTXbf2T3lyEAvjuOdJbPDsMnCJQkdPpqkvo_YidXXNjlY81RTHpAO3md83aI2zrYigdI5_KB13GIcxdlwV7j1rU5-JSym6Onc3eqOZ3jxTzv2874MU2HamaxrC7cmHP1b5qUJxKyt5ouSniYSUQDLKGl4ARFLkvoBoXHnEnz38yPym1F--_psXJ_4KKmxykWMuWizr8BhyXflos8tRkdJ3Yv43prEz4Xo33PXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دو روز پیش صدا و سیما،
بخشی از سخنان پزشکیان رو سانسور کرد!
اونجایی که اشاره کرد که خامنه‌ای در نهایت
طرفدار مذاکره شد و کوتاه اومد!
وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که
صدا و سیما مطالبش رو درست پوشش نمیده!
و میگه یک گروهی خط می‌دن به سخنرانان و مداحان
در خیابان تا علیه «تفاهم‌نامه» صحبت کنن
در حالی که به قول عراقچی،
این تفاهم‌نامه، بهترین تفاهم ممکن بود!
[همونهایی که موشک به کشتی‌ها میزنن
همونهایی هستن که این تجمعات رو سازماندهی میکنن،
اینو عراقچی هم می‌دونه،
همون‌هایی هستن که در صدا و سیما هستن!]
قبلش هم صدا و سیما،
بخشی از حرفهای قالیباف که مسئول اصلی مذاکراته و رئیس مجلسه رو سانسور کرد!
(یادآوری : هم قالیباف و هم عراقچی خودشون  از مجموعه ۳ پ هستند! و باهاشون اینطور برخورد میکنن!)
این دعوا از اول انقلاب به وجود اومد!
صدا و سیما شد ملک طلق
و منبر اصلی «ولی فقیه» و شد چاقویی
علیه دولت!
حتی علیه خود دولت خامنه‌ای! وقتی
خامنه‌ای رئیس جمهور بود،
رادیو علیه‌اش یک برنامه پخش کرد و‌
رفت گریه کرد و قهر کرد و…..!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=QdsCUPUcYrLlTq0lg6aYS4m6idH84MVwV2AZlei08mrfCOczvu3H0pOcVnAQBAjl_KzordJ3XqPOD-Dbq8uCdrL58tXjvseD1_mTG7rowxDmOD6QPahKJ6IghpS507trz-lhPybh1exz5QFT5CFlUDvK5ORZ-A-CxtOe0V0LZjUGYj803scKFMBDkJTZlDG2ejUxU3qqpVuzy65cGtIZbprJkQaRAHTTqsgaW6YGZwi5_bgKpaMm_JzH-GVKVo11kR3U5whWktmpc1VJ8t-J-fvLwNs_ZxJgg_wobMxRMoM02ycM5syUCLHHn9sH7mOpNkyhu2pHoq57wMKhKoc5Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=QdsCUPUcYrLlTq0lg6aYS4m6idH84MVwV2AZlei08mrfCOczvu3H0pOcVnAQBAjl_KzordJ3XqPOD-Dbq8uCdrL58tXjvseD1_mTG7rowxDmOD6QPahKJ6IghpS507trz-lhPybh1exz5QFT5CFlUDvK5ORZ-A-CxtOe0V0LZjUGYj803scKFMBDkJTZlDG2ejUxU3qqpVuzy65cGtIZbprJkQaRAHTTqsgaW6YGZwi5_bgKpaMm_JzH-GVKVo11kR3U5whWktmpc1VJ8t-J-fvLwNs_ZxJgg_wobMxRMoM02ycM5syUCLHHn9sH7mOpNkyhu2pHoq57wMKhKoc5Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niw6ac7mRc10W_x9X0pLPiqTWNXnNkjnduA6C5dXKr8m1HcNjonx1bQdXNlEX5fQmFZzN-6mPkH9oFRW0OFgQx8OWO4SybSFZ4l5a8EGfGtwLCbUOBLnUVHegAw_Bfq-3YfPeplRKo_CfA9RYU0tLIN38dIHnqDEIhjrLJ5hmEkFDNe7iQA9p3R5PGqwV2ep_wnz5Ba6wVuEYBnI-JR1uVFZ8chb8F0ogsrrSdwBNt2e2U-5T_Ruft1hUmEDeD3FByvodbXSK_JovwGWpuTMQ8HsQFPk4QN6Q8HU_7S2IYyZz0H6ECTel0aUz2zsTM3HtonV_LOE_XOmf0E07WwMaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=LE8fPBbDJ-mwhZjWnfNKJuQqcXR34-JtxIx9OZvzHk1ZBmS7Jk4Q15zypvYD78flMO3LJJ_sHJtkDU3F3ymAiCOcwppF3UFpn9ZF5N8lmGb6NOUj6S2xgYvAjAJkS2SN1JKerdWsrICoAntTbkcRcrCRSAABlg4EKDF2cAGmiV2g09nRbWtQ6lHaqImmjiCXsnBkW95OIKobONjIcjKNzcdd584YTL14zm5o1g0NtWdTv61xxWs-nHtL1k1ZbRM5Tj4N_8IcOVAC6ZVOLcm1KsVBB6s7KHRfm9wq7WJ9edyU9cOm18_rkrnnC-N7o5qHCNVJA6gXqVKaqS9O4AhB0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=LE8fPBbDJ-mwhZjWnfNKJuQqcXR34-JtxIx9OZvzHk1ZBmS7Jk4Q15zypvYD78flMO3LJJ_sHJtkDU3F3ymAiCOcwppF3UFpn9ZF5N8lmGb6NOUj6S2xgYvAjAJkS2SN1JKerdWsrICoAntTbkcRcrCRSAABlg4EKDF2cAGmiV2g09nRbWtQ6lHaqImmjiCXsnBkW95OIKobONjIcjKNzcdd584YTL14zm5o1g0NtWdTv61xxWs-nHtL1k1ZbRM5Tj4N_8IcOVAC6ZVOLcm1KsVBB6s7KHRfm9wq7WJ9edyU9cOm18_rkrnnC-N7o5qHCNVJA6gXqVKaqS9O4AhB0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggRnrBI5EpucZCyYV_RMJ43ljfGwQ9MfCPOyEO5pUF9z9b_X7ZxmD4tHRcAPVBiGLtxa7kSLygsUC75b9HBRVFct3tFrIXUehVcKOk8XlnxERuXcDCaXvgZUBWLhhm-5Z7i2UzcTvrA6wSJgZ5PzarW1gc0BN7jFlxZ9Dx-PNSdZPUNUUcXYyChnZAhqI2oc8Vc2mbNPQiUShwpdaYx-TnXI4y0S0-tMrxm5Ux0kDfq2owZ1qB3OFqd-m4YlpZKg9ytZrBUFZUT-Fr-fWPEl9i8Y-Ae59lkcZ-FlX6TctBBiIxIvPOa9GAIsE1FdsNRpGdRGzrsK9tYtHIFoGR6grQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvjlhzn6szbuP9n1R1neacpvlTD9WwXvD0fg36pPlu8DWkrDcv0qlfP2gRPA6ZCCnSWb-k0OAgbPZlZ6rsVkvTMjiWo0HKOpCwiB4kF7IKIG-R7Xpuj3RnZIl_XvaOiwXiqEmAtiJbNpC0FdSbwSQLmMgshqdZfGjiIv9_-vg2dJyM3d6jDVkv5_zj_Nkx0kx2wzt1XIsRFEFnvvkqnZBYLjvkOnDSe5JVPTmhQC-x1IciCVZes9TwpdQppTxbcH0NDlR-wq4Y3QTbNd86Yur2n6BzfmmPTqz3dlqzLzNNjtZhjHe1nnBCQBUPkp6D-sYfUSQfD1Tg7lBS25NEhK2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=gnZtc11QEVql010-Q184wNNHNE_qyoA2uCgi-KtoyZ6sBd2bmD-ClXUhNoWyLhi_o80m-cwRRVgo8uFHwSbnQavGqxB3prcYgbAJcXk3jNPScPpIYGC1tcPk_6YS4LhNba2eZBKm3J5AzEg5X-kNXeGmqP8QJJc1xPMFZYK5-hO8fieEdS8zNzdJK_IN7gu3RSC6PXDdlcHJszSK3n38PPAjgkpvy-7UVtANcjGe9OtnCjX5QHOFJvApVsPAIfmyLqR2LsSerDbfIZsJDzLmb83sZHNHMtFleK9oD9AaVphcukUGayo7S-6hZUZA2bmVPAvaP6qUsuIGfR8x7MNQALg__DeGg1mV-kI_UzjSKNN3iWWOOMx01CMtG6RLXegiwPcRn1fcIXXn3_LEpnih5cflAZsQ6nTDAcQ11xV1DTJT-kJqEfge-baZVWL5Oyj7jn2ci1w6uL3Bt8hWkK_4w-3oBL1nUc27pzgHuYVkyQH-Q1y0O_N4i0-S-IrRFUnhD6l9QLAWHWYgIkEITCtO6jUtUKBz9rf44mLSlIMYJBM7mi6U-W2j8z4vNGjCdVGM5iet405jP-3ErURmjC8eRq9obOmQwqoAXiHOKsbxgEBTp9lQcrTWqyiRggUoP3_vC9OOEdZjehF7Hrtu29apiJQc6HM3MSeEnBuHcW4xXew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=gnZtc11QEVql010-Q184wNNHNE_qyoA2uCgi-KtoyZ6sBd2bmD-ClXUhNoWyLhi_o80m-cwRRVgo8uFHwSbnQavGqxB3prcYgbAJcXk3jNPScPpIYGC1tcPk_6YS4LhNba2eZBKm3J5AzEg5X-kNXeGmqP8QJJc1xPMFZYK5-hO8fieEdS8zNzdJK_IN7gu3RSC6PXDdlcHJszSK3n38PPAjgkpvy-7UVtANcjGe9OtnCjX5QHOFJvApVsPAIfmyLqR2LsSerDbfIZsJDzLmb83sZHNHMtFleK9oD9AaVphcukUGayo7S-6hZUZA2bmVPAvaP6qUsuIGfR8x7MNQALg__DeGg1mV-kI_UzjSKNN3iWWOOMx01CMtG6RLXegiwPcRn1fcIXXn3_LEpnih5cflAZsQ6nTDAcQ11xV1DTJT-kJqEfge-baZVWL5Oyj7jn2ci1w6uL3Bt8hWkK_4w-3oBL1nUc27pzgHuYVkyQH-Q1y0O_N4i0-S-IrRFUnhD6l9QLAWHWYgIkEITCtO6jUtUKBz9rf44mLSlIMYJBM7mi6U-W2j8z4vNGjCdVGM5iet405jP-3ErURmjC8eRq9obOmQwqoAXiHOKsbxgEBTp9lQcrTWqyiRggUoP3_vC9OOEdZjehF7Hrtu29apiJQc6HM3MSeEnBuHcW4xXew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Qrd4wgRqUgy4RhYGMxdjP4BM_A3XilTfvEYDmyA5esaOAF7j_1r0NddAOzI3qQOeh-WhvKcHCCNybOhbM2wx-rUEoVVOc2bEkTzV77h860IrY9ppKJ2lNcc2nKLykJ0kI5rj3UfXBTwvgcfFxKRo0cBicAbZPsCjjtZ-d7Hqlkdn_JtTzRHgoNAnidybzkJ90MF4K_kO_8w0Ev2iW-pRDpjn9ehab6DniagHzGiWC-EFT6-UGT_wiH9aoyC1uqKwKJO9XiNOutxlK9tmAxW0ad2js4sq3Hcp754WfhYQ7qcq0Kb58qG_JrSVMfdDwR0KCQmIYJ7DOg-IYPulotTNdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Qrd4wgRqUgy4RhYGMxdjP4BM_A3XilTfvEYDmyA5esaOAF7j_1r0NddAOzI3qQOeh-WhvKcHCCNybOhbM2wx-rUEoVVOc2bEkTzV77h860IrY9ppKJ2lNcc2nKLykJ0kI5rj3UfXBTwvgcfFxKRo0cBicAbZPsCjjtZ-d7Hqlkdn_JtTzRHgoNAnidybzkJ90MF4K_kO_8w0Ev2iW-pRDpjn9ehab6DniagHzGiWC-EFT6-UGT_wiH9aoyC1uqKwKJO9XiNOutxlK9tmAxW0ad2js4sq3Hcp754WfhYQ7qcq0Kb58qG_JrSVMfdDwR0KCQmIYJ7DOg-IYPulotTNdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqd3fSxkqRKAcwfr33FakErnAACNWxMVYF6Rz33ewiFRIxO19_TAvWc4nnkKG7lPa4V8laL-M-7vZDJJpte7m9ETfBt3-yAYAX1rS0ZvVQtyzY8rolYkZKdy6epX45113ZVYCQT_ATCsfycEN1I7YSiNhRCJ-QgfJDTvgy0d49HbU-UVpZOXU1h89G1DeiI--jJtmDPHyn-8rGUhASlRbiKld7Lx-O2g2kk7MHzSzS28_u06VOpDuCwl9-XHBJJoPFKG7XYmYeiPa9_c_h-nVXEvJZb3G6n9qxRJezhBl6E48DNScupThBDsRNWWgArHMScYfsLg8YKr6RM_ezKV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=nvsxJgdgTYr_0BiBZF2e-EWMLPAz77R9Lyj_JXk7ByOZmJ7VuBgkVangJJlHbwXKJrgRlGK5kN5nIVgC2rLQ33dgIhkTKFiLD0HLyAlKOC1nwQD9RaYUxHZLEbMG9aRfsBHgmeEXyUCMs1QHFE2FoS7wT515w7J_gfLmupX5FOV9A1febwpdEzyBvxeJr01v6y3TXKXH-ASchd5sj1msx6NAqrMvYQaP9HG1op9sZudUcCxkn9AJk3cC_I-MwZ2XPndZIy3IVfbaJjkXZOxgKackQt7tGDbzKXwyljW0HQ_wMURDuoxLbxePiqgGAWWkRE0fSYAyblAwdN7e2NJmnIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=nvsxJgdgTYr_0BiBZF2e-EWMLPAz77R9Lyj_JXk7ByOZmJ7VuBgkVangJJlHbwXKJrgRlGK5kN5nIVgC2rLQ33dgIhkTKFiLD0HLyAlKOC1nwQD9RaYUxHZLEbMG9aRfsBHgmeEXyUCMs1QHFE2FoS7wT515w7J_gfLmupX5FOV9A1febwpdEzyBvxeJr01v6y3TXKXH-ASchd5sj1msx6NAqrMvYQaP9HG1op9sZudUcCxkn9AJk3cC_I-MwZ2XPndZIy3IVfbaJjkXZOxgKackQt7tGDbzKXwyljW0HQ_wMURDuoxLbxePiqgGAWWkRE0fSYAyblAwdN7e2NJmnIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaYdeIj9VR8Fg9aqceozBut04XBPOe869jg4RHFvYxqS7akR2lMLLtjsPsgM7sLMH_4peL_ljcf7VRE5G8zbUa7KOGNiUGakSDQKxMSZnjjl78WT-W1nIPpMWqvQ44yM5nuq-CEr7pf-nSvAiMKL6ehxJKKkVKIJaUyTvSDAebJdMsNV4aJvNVn_W3yWV8V8X-D1i9Bq2H6T3TdO3EXoHj0_CPZ7T-AShzCnsS54rRgAsfx7HORm_mtTOx9rX7jvymXvgC9ZsBFksLtjd_oA551jQXXbpa0QrZoMPjFPIwhoHNXmEKWnIS_bIloO247-SmM-V8cZfz4jmzTMjfhf1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFwnE4QyYnYDADbkJZf0gAFsxuEOzWUOMsv36bpfcMt4MND3-p7jSNlogQJU41kUoVeGBsIkZRZhyXwCNpIFnhJDfNOJrMNGE08AzUbGdc0hIdCf6mGacW6ZY47jxS1oBb7gVUF0Jdk-kQahRTneACQvOV5r0RSZrBxzeZKELkvYI5JXXOIauO1wthNlPlbZ5Qc_doMaF3J7bJKTc4WMc9yOqOM9dcXSGbOKC1wPOVbu4eIbNhKaS02i0n-ZRyOBJR4Tv_I2bxzchK3wF9zPOT_PL7mdfeTRaUOY7ZaQWj4pQvqyPNmVhV-ESojfG6KqZbjRdasRtNw3ymc85ag9Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfcoD8wMOBeWtRqNreIzEKmX0yb83Nl6Jj_bDFuRZDslrXMXeLJSSyqWyszCIwqiVT8wAR3LDx7NPAq4uZt7jgPV1tKwKObLFH4QM3zdD2xTXzE6hCe3_VA_Eg-86U17sqyPZXWfPlg2nrFtOiIGPIuwP_APn-COhVBYCIw2ccsX5j6qP2HIzG5aAjooM-p0Mgz6dW1OdmXM1ikSdjC5mL9alT6lN4zxeUslrFyOI8I6xyuF8dB8dPWbWMbt3lQfvK5rh3wUddKQsRykJD02siREI37lY7Q0qNkIq8Ytne90APSHjRO0B1b5VdfunMhpjokmSeexN2Kk81sg1VwMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpcbLZk7UbSPuSsLOQzmsZ9VVGmwH226FWukgN2C-BgorNAlfuGBfwREY2xurS9Q4XVF38x1ztt5U7ohgmT_USonzH2V3sSP321PfwbxOP56mJ461Ss-aCz6I0nZyEP6fokSHpq47MTT1jIRBwWPLGSZM0wyn4xxo4Or-9Uwe306YVrV0Mvhocqn5twlgZdTbc5EeFlj7-_YnBKiK5IuOo4pX0MRPg67KlljEZiuEp2YHzCeB4_6sFTZwqhJUje0FUmXnw69kUB7dLC0B5ttZfKVdOPWImXvvpbk8sfdMlFc_g_WAqA5yBB5A6njvv04C5OHj-Xmt5BxPT2nlzBcUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tp--qqp_3CiCzBcbc09czyqbC-ymG-AyQi67snoFsUqYbTuOXMRffsKmK0JTziYBQFd2uFetVMOrTkkbKxdiOt8OO1cDTzULbMoezfeBobd15T21njg7M2p9BOM9fIYdPHAy8pTmUGreoNXt3yr0v7-qeNVpVRIznH1ElJbYc-75spY-u5UCTEgMJFTVK_msavrXlsK1GqlAVO75BUPESUYzybabrRD0FFDUDaNgNea05UB479CWEoiYSn-zv-J4YFpSskJbkmDLcQ-2VyY3i0xU3xscyY16xEdpFrbNI3TnTrtebIwuihKejL-1LSIxuXVCgmpw2TVdAO2m58kgAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=UgWlCUE-QlK3Tyi8kmcU9OGZYCBEyxSxseWZtD-ex63RFFLlfveJTF11lJBo_uq7stNcLsuJyoJv9eB1cqKo0Z0SBqkYWiJA4LOm7kchfhsYgviyacNLXSb48PF7WDlE7gy1T7PIEoJIQ2zJUWV_j-3hvqZGKHqISvIvluIA_O9fMhfJN8eG4OMWiBJ5GrBnn4MExEekw4WN_jHgaKuyPEdcuE15fArKjTvvGeXphYuVJExuGvH2efBncdsfAQgVxrvJlplBam1TlFpjK8dPhua87nXqPyASUv3OxFuvVbzJ0cUZsCsWPFAIHP9H156VjphrRkHcoGuh7wDi4ad47g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=UgWlCUE-QlK3Tyi8kmcU9OGZYCBEyxSxseWZtD-ex63RFFLlfveJTF11lJBo_uq7stNcLsuJyoJv9eB1cqKo0Z0SBqkYWiJA4LOm7kchfhsYgviyacNLXSb48PF7WDlE7gy1T7PIEoJIQ2zJUWV_j-3hvqZGKHqISvIvluIA_O9fMhfJN8eG4OMWiBJ5GrBnn4MExEekw4WN_jHgaKuyPEdcuE15fArKjTvvGeXphYuVJExuGvH2efBncdsfAQgVxrvJlplBam1TlFpjK8dPhua87nXqPyASUv3OxFuvVbzJ0cUZsCsWPFAIHP9H156VjphrRkHcoGuh7wDi4ad47g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukUfi-wFzE9XTADe266JgOCz0vit63RvehLUGqWbOaS8gijhwRJjIpkC3nSPLKHzdaLouWh9E1sd4WphSpU1Be2UGIC8N8D_2l00zvn1HpqvfUDBJii1UwaKtvUqClqmhmz12rYgqPtmF6FwxP-mlDFv4TyB-88oNx121XvUHgolM91-1IylD3z96gBGe_gVYMv6_Ki5gWhyOjXOkRoZuJYJT7pQmnwf4iAtbO4NX4NZwGYS-4CJZnfgyQj-TGh_ZtEn4tQ5YLsAlk3TtXCxJSWHwJdUWo2kDwFp_YMzo5gzx30pVBA5uTQ54B5D6IDDPkGOZk7NrX62mUNZmwXgVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1AxCMjkdh_Vd20D2Rwa2YOaQsoHchKgOzcVOj2H97D2XA5gy8QThhbzLivCcf6bYTsBHYre47Qq5i2Eq9F785sSLWFMu8HqK0w5jzg30mY2B7UpVHoPN3ursHn-_UBPJKEBUO_Xvqhztk6C3xCacwSFLMheRF94xbEr6R7W7tf0prOVD89kdQRc78vApBd89-p1BEP6gVrXWVyte9e0-OYiVCVoJhiH9p4xm4UnUiqS51_8PZ03Ozg4xZO77GowQ9fvhnVadqWhSIO7YLyrGNaJpAx3aFyGP4B8vqvOFEG0LqDPHLLH3xk1TaoBCmd1-0JfTsNIB6jl_vwMNI_U4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=nFdiAgibzglOsK5qt3OycdaeXxga7X8imlo5mJw52d3eJBezTQapowNL4pjtXhSQL43walZ8ueiwQ1GN1In1_MsCkIgriSip0grcbntDOzFa7Ly-VmRnzDIEnfkQ1uyt0L4dexGofUgCchmNUOC-wwQdEzFmSvQ5yUQBFjcLVaAjPCiybvhtoMzplQuSCjQSMLUNPfoxeCOLg6rRubws3htLVxKLFHe5z4NVmrfA-SazDAADLLwM9SfH_2QX-xsGJMT7zcSjySvI2E0s-Yok7Z6wC3nt3J34mhFMLbIQU7Z1yfrlcEeeFuYclKS-ALfppo921vW7N_LEf5PBTXwvQpWW4QRsLiXu7dz7FWC33AFPeKCaDaQgDrPtmyl70N6okSVdAiodpqSQF7vbVjIoPFLH8thctoVydXpWoVBcfziz_GbGFkayZWJkfFE67D6HjOm9htEpC2bCPLhgPcDNjg5pulbrCZrLLRqgv6qtju0Ag5uxrmBayAPPbVqSAna-VBa0QzJG3Znp2EETSN4d_H5NU90KWD4H1kQuGxp1FwFrzFTiOmJM4KDrKS3o48iMvn8OAShh2ObjdPwQukgtmzzS3Ez_2yg9kjPkqi820TFYzzC_rNxIoR6ZB8UMpu-pq9MqSIiOCCkKgPzdIwqrClccmWgDDultFaoog8LOY8I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=nFdiAgibzglOsK5qt3OycdaeXxga7X8imlo5mJw52d3eJBezTQapowNL4pjtXhSQL43walZ8ueiwQ1GN1In1_MsCkIgriSip0grcbntDOzFa7Ly-VmRnzDIEnfkQ1uyt0L4dexGofUgCchmNUOC-wwQdEzFmSvQ5yUQBFjcLVaAjPCiybvhtoMzplQuSCjQSMLUNPfoxeCOLg6rRubws3htLVxKLFHe5z4NVmrfA-SazDAADLLwM9SfH_2QX-xsGJMT7zcSjySvI2E0s-Yok7Z6wC3nt3J34mhFMLbIQU7Z1yfrlcEeeFuYclKS-ALfppo921vW7N_LEf5PBTXwvQpWW4QRsLiXu7dz7FWC33AFPeKCaDaQgDrPtmyl70N6okSVdAiodpqSQF7vbVjIoPFLH8thctoVydXpWoVBcfziz_GbGFkayZWJkfFE67D6HjOm9htEpC2bCPLhgPcDNjg5pulbrCZrLLRqgv6qtju0Ag5uxrmBayAPPbVqSAna-VBa0QzJG3Znp2EETSN4d_H5NU90KWD4H1kQuGxp1FwFrzFTiOmJM4KDrKS3o48iMvn8OAShh2ObjdPwQukgtmzzS3Ez_2yg9kjPkqi820TFYzzC_rNxIoR6ZB8UMpu-pq9MqSIiOCCkKgPzdIwqrClccmWgDDultFaoog8LOY8I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=rc7_aFl8y871Aq-lklMrXEU54yiXNXRa_QPqoQE7g_9tjnaDl0DxBSLu6PVuXBb3vk1NWHkHatxsT5ks5LuWvgQr6osCgRmaF8scBODukm0qzO0ABtlfREMydg8O8iXrBRLvGJIhdLsVztdXLpGUJNoHf3chX_JN5PTv52qx8NyXTyPmweuLmbkOrL7v4qQXt74RukrZNjXzm_8gNoCQku4_JzAFcrQQ0pgK5ZgguYpOZkaYXadI5eK0Ppqqlp8v__icgfMrfqGOkmQHC-2-yz-XMtktImGeizJdPBVIQioN6Fatltk1gNN51qlcEUeVRuhk1mDeK9EM0-sQUzvVEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=rc7_aFl8y871Aq-lklMrXEU54yiXNXRa_QPqoQE7g_9tjnaDl0DxBSLu6PVuXBb3vk1NWHkHatxsT5ks5LuWvgQr6osCgRmaF8scBODukm0qzO0ABtlfREMydg8O8iXrBRLvGJIhdLsVztdXLpGUJNoHf3chX_JN5PTv52qx8NyXTyPmweuLmbkOrL7v4qQXt74RukrZNjXzm_8gNoCQku4_JzAFcrQQ0pgK5ZgguYpOZkaYXadI5eK0Ppqqlp8v__icgfMrfqGOkmQHC-2-yz-XMtktImGeizJdPBVIQioN6Fatltk1gNN51qlcEUeVRuhk1mDeK9EM0-sQUzvVEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCmPIzIA59uMZWr_AXZBzwRwKmtZOhiFyFDKZRgsNWE37eX0zSqTDIqKZLi4AH5MDzTieDs0bhpz1a7zZT8jTPlgNpO86NzSox31K7RQ5mwrh6CwAdv-blhZUz2nYbiiap8_5cJI4AsD-Hb2N8B-o-mU4lgIsKUnJ4k6387sKPbvPucLSzRcC63hSk9PC3bckRFvlIgH0WNksXErQuk3muiPLhS-1oLClyzzCbjSLxvlfyiLjyNju2kj3kKvb6sq8IZEW6dGzsaUIPvuLkqy2kEcWUtP2jKynPbOrOGX57iLZ-9cRYi-qOXKWpjcrX3M0cbPLzSLnVKxN26Eej2uuikc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCmPIzIA59uMZWr_AXZBzwRwKmtZOhiFyFDKZRgsNWE37eX0zSqTDIqKZLi4AH5MDzTieDs0bhpz1a7zZT8jTPlgNpO86NzSox31K7RQ5mwrh6CwAdv-blhZUz2nYbiiap8_5cJI4AsD-Hb2N8B-o-mU4lgIsKUnJ4k6387sKPbvPucLSzRcC63hSk9PC3bckRFvlIgH0WNksXErQuk3muiPLhS-1oLClyzzCbjSLxvlfyiLjyNju2kj3kKvb6sq8IZEW6dGzsaUIPvuLkqy2kEcWUtP2jKynPbOrOGX57iLZ-9cRYi-qOXKWpjcrX3M0cbPLzSLnVKxN26Eej2uuikc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krMsrdW4L9vWdq8BxBpY2YgxyS6Yzdo6R0owecuSDKhNxmfIcANU4OFDGTbOnvfwAlTQj9QHh_Btxz35J1vipbRQXwEKuk1l5lIn-Ojp4hZVgn3MjSCtQHTKHOk9ENqgkcp-mvFgJ-0rjh7EnMm516YUgov24Y31yjsrlCjL4etiw1jNOTJtHqMbi0sgsSYX-D_K2ovxbWbn7u_Q40VO1z6yVc_8xN3y2f1aarNCbKXQL_QuwLtgKg_uszEACBTgSfJuG8LTolzJr0jD7t0iO6uTjo7l00HXQlwA6IjSNdD6wUzJMoWO2n0Mvl3voeaaL7fPmIPwj9xhhqKLxEPY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_CHincmUszcRO5sjGpq8XA1bRqKpbtWCs7VYj4-6e6NRq44yKVWSOTPuPmZgHpiIb-LMaJiH76bQ64XBehEMqoM8J-E1aKNGdLUhSw7ikbmTomC2E5ufx2g-NOn-FB-sCY35HIrYd0UW6VDes836MeB3A8kvtSTz3xY4Qml7QBakhIaumI8GcC3n9gbln3MvOd31LN-lJIzSFalAJZLF_aGB_hoOKNYYdWAJAnPUIqE080aX1_8pJrNDEJlAw-fk4dbdFpGAqIVquPyJtTbje8KxHj-1RwyDh1HccvF0OMhoZn6d8nT0u9-ML6LTTRmtpkTt3bcft_bIl9CKeeA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
