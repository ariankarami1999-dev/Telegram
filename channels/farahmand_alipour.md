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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 20:46:10</div>
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
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUv5anB2qfc-brRh1IVJenxVNXBR0sZCsS_HQO5fDdRmfS3qbRGp8xsjEf9Uje5nBbcXkC-QdgDT5oHzh94KGeFdXLTJhJUO7yOT48zlcgCBEJdFxKmbzPLPMT4f91Se-3Pxl4zLbStIjl3sROPy4gDLxY2Ji1oTx81YlzciaS6Kjm1B_sqLI_bHtYm-5M6GVKX-iAjZD8qsuPR05UFej5AAOGArjArlLCmiIMfcGvInvBRZmcUYzDNd98S7O2yy20QFX9oTOhwtBJcmJsNQHa4rBEB8PMp4Z5J_LZxafM2YCH8__zbDb_rWZTuZhYe6o0Bok-mCja1U9qPhTmi8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcZi7B3J4v_54mMLaMeLbmyvCkRt4gactRhXoIeiHZ-AsCFJntWeBWWD1teE-raiff6dcsGETLsCRrIJiuJHzZex102YF0xsErP7Z9AoGBxeX3d892LEiEAAPHH3fpnF6ftl4I57kpboD-Nc__bQBfFKYQ_XiXuhEBJjoZMeYHsLXpD0c3QY5GoE5zJlm5fP-FHcR_xZky1Nqen4CRU6CmucOc-YqyeeZhaDdHMDOxGJ29W0RE_tp8SQW0F5eNwSzYxVKKT2yCWcNnXVkCxe4ZhTuajsrltArbYh-HSEBLH6uNdX97-xuyFvm1BW-iBDJNuLrltHtwoE_JQpUxwjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDV3RgDs8RBKdPKdVlP09jUI7ILHH8KMVZux3BG8vIykVG5gQ7mhNrSrnQAvwXsH1_3FRG6lf5r7djnM3fPSevIGECIzS7fRODdgM3AwJRtYURSu9R5e1B3qq0D9ugDgikCaat5EzXwqEP7a46bJWd2kcOTllROYhO1PgeFBeEimiqkxt46FTSCV-2ukEKzTiMUpGKVt3qe1e57xa3rnj8eo2qGcSHm_rVAtGiLh1GhIBj-rbAxmd3FSq81fqwCYsZe-_826aJe2hzYDHIJVZPN5GkABCBDAiPtnL3eabWF4oBY1w_Z_0OsiH91UdAe1cmFNyfTF89t41peUMR9jiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=oGoDW20Jynt2Gn-vTe0uB_S-CfBltqUsSA3NLbSvsE2HmdvZgTaEU8GENFe8KKaS7UPAblsLDvA844Zj1GmSFxYY_9ONylyRrVHnDtCnbcNmBktVXHUo0wybEMLKITR1hKH-nlMFYbtWyWf086ajMVOKd6pezHLbPxz1CZbX5SSVie1i9iCoQMezwFLCbLlk6yiCQuSFy3bZmJn-ZY9Y1kKPxi2556jEB4AbIa8MjubNsfcbIQTdejyNSdzmWZ_vsyZNS6QvYL_KB3Uug2YVNuxaOEviC2_nDH2M_MQOtwPiy5qwNkXtpfcx6OPz0ugX16-cUnXkN8vkJmjRjFsFZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=oGoDW20Jynt2Gn-vTe0uB_S-CfBltqUsSA3NLbSvsE2HmdvZgTaEU8GENFe8KKaS7UPAblsLDvA844Zj1GmSFxYY_9ONylyRrVHnDtCnbcNmBktVXHUo0wybEMLKITR1hKH-nlMFYbtWyWf086ajMVOKd6pezHLbPxz1CZbX5SSVie1i9iCoQMezwFLCbLlk6yiCQuSFy3bZmJn-ZY9Y1kKPxi2556jEB4AbIa8MjubNsfcbIQTdejyNSdzmWZ_vsyZNS6QvYL_KB3Uug2YVNuxaOEviC2_nDH2M_MQOtwPiy5qwNkXtpfcx6OPz0ugX16-cUnXkN8vkJmjRjFsFZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=IU5S0H0vzZNGtbgV0lCDuOMc7NV_jQwKnS_CNDHqaI761LOj8iXSAqd6xMw1ucFP4_0dfCHv7rZzjXK73tI6wI2ulyhf-unPIMsH74t-U74T-10-7Bew-Q2FLlM_wxM687OAiWF0dq5-3SPVVrQCbxpA7WRSKKmScmGWyv0mgywZgR2T6PqjHRfBA6QTPUp89Y1qbClCfp1xE0dZ1dhqz3nlU1QU1eMkp_zFSq42Vlz8Z1PGuByNYyih9QJ_vvHguanJq3wE47r5E4TqNRYDhJJgtzjqGOf09S1BcMD7f4ptDKJxt6tazEyIiMs7cqziUXq2bq257QMSNQmCG3lvQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=IU5S0H0vzZNGtbgV0lCDuOMc7NV_jQwKnS_CNDHqaI761LOj8iXSAqd6xMw1ucFP4_0dfCHv7rZzjXK73tI6wI2ulyhf-unPIMsH74t-U74T-10-7Bew-Q2FLlM_wxM687OAiWF0dq5-3SPVVrQCbxpA7WRSKKmScmGWyv0mgywZgR2T6PqjHRfBA6QTPUp89Y1qbClCfp1xE0dZ1dhqz3nlU1QU1eMkp_zFSq42Vlz8Z1PGuByNYyih9QJ_vvHguanJq3wE47r5E4TqNRYDhJJgtzjqGOf09S1BcMD7f4ptDKJxt6tazEyIiMs7cqziUXq2bq257QMSNQmCG3lvQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paOuFdTShcbn8IihG1387137U5KbZ_3D1S2sGxsWDNZ3-g9cPBCjjAQ5jlub18nmu1K0RDM5gPtwB474feNRLA99fui2Zvqf85EkjN5Y2JVitZ1gli0BEX3QE5aSQVcyeLACZypmkopwpE6xJsxRAc7TYUrUiO_UibpSI89DZpzaIUx1IOAg-KAcsyM2DDaVDHczxxc_2XOgO8Ro5JQLK7ijtyRYr1jE0Vd0_OSC164cWvU6SARYa9ulXdWK7qQXeLsR09o--VkgjXuG9lWHU9xvV2-2HS9bvlplBHns3q-aXE0wtw0AOR-cdWEufCZnl_Nr-D4z_LUDHZbImr2ZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvIFm1NLx8tRToWJsU_XF3D-rC6HWxwTlwHxxHV7HPtgWERJGMcjyzlNVSihO2grdcaUDwEAy98spR7L1Wa0OhOcJLgjvDQG8yiN6cY3cOMUCDixxhPqTYqWDETI6pvmK8BBuMaobGxVbyreUI_RbtiePYaGURBL8V7rAloMIz4qn58n2Fc8p6hGH8SRnrjhgZq3rULg2077v-fNJgV-_utIB40fL5LskOQVqrhReh1SiPJw5iSKns4tONWtUng8m3ftpEejKOJsdX9WK4hVXbPjXtya59-fXsTICEeysQKIKCY2ifP8fE8KSkqIAXWop9pfA4WItDaAi7p-rYtS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=nuvaxXNIVhwmaLEEo1Rk7TAqOL4J0TCAX28W6GgOc7uhe4J5z9LqyeYaKGb_EBZGEUGF-pFCxc10J4YZaMwpwHsCOHtbOifwmFYnFxBUaGvUT_9EyFtqZ3R2oprb143aQIswoRLen1MmPCM0O6fdH5d3jliExaftRL0V-6vUJaktUm1NpmOViMTXtFjsW2JWAa0mZVPdUFqGW3AXUCnlLfN_m7j2i1Bp11fp7H67iEbpQV5tZyp3kWGKkicjx_Lkg65LfW8EL2MldPyPPkhTVaqB3vG0RLBQJy8YggNl1HYyHp14uVeQQZTyDPqt-7nI6U1sXF2wotdSqLH3tdNt9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=nuvaxXNIVhwmaLEEo1Rk7TAqOL4J0TCAX28W6GgOc7uhe4J5z9LqyeYaKGb_EBZGEUGF-pFCxc10J4YZaMwpwHsCOHtbOifwmFYnFxBUaGvUT_9EyFtqZ3R2oprb143aQIswoRLen1MmPCM0O6fdH5d3jliExaftRL0V-6vUJaktUm1NpmOViMTXtFjsW2JWAa0mZVPdUFqGW3AXUCnlLfN_m7j2i1Bp11fp7H67iEbpQV5tZyp3kWGKkicjx_Lkg65LfW8EL2MldPyPPkhTVaqB3vG0RLBQJy8YggNl1HYyHp14uVeQQZTyDPqt-7nI6U1sXF2wotdSqLH3tdNt9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=CpTPjWpWETt9Z5JtvccDqUl8T0RcdXqQuGXK5YM6Hy3QBUJxmc3oginuVOz8uG1wCiND2VVn-04QN-jXYS9-1K7OkNpGHoDiVr5hSwww2QeEDiZF0EG7jXzcQYwk2G1uG-CISkOMUoDcm_ffslDiihtwJPga2k1_K0T-aw8vOzbMB3my4250-jO8SV-P0WlgMtm8A9oArpgTIIiJ-Re48HWIuvjL30KT7jApCENPXbNs6IQ3fZeos_UvJ9WYCxQBmip5Qqvfm_dRDKtVMmfRUxLTP4F8iDyM2800cpXgvxXLrR-vdc_37ofdY6M-oTXb4IYqj9_wW01e6xPvonKc4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=CpTPjWpWETt9Z5JtvccDqUl8T0RcdXqQuGXK5YM6Hy3QBUJxmc3oginuVOz8uG1wCiND2VVn-04QN-jXYS9-1K7OkNpGHoDiVr5hSwww2QeEDiZF0EG7jXzcQYwk2G1uG-CISkOMUoDcm_ffslDiihtwJPga2k1_K0T-aw8vOzbMB3my4250-jO8SV-P0WlgMtm8A9oArpgTIIiJ-Re48HWIuvjL30KT7jApCENPXbNs6IQ3fZeos_UvJ9WYCxQBmip5Qqvfm_dRDKtVMmfRUxLTP4F8iDyM2800cpXgvxXLrR-vdc_37ofdY6M-oTXb4IYqj9_wW01e6xPvonKc4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKoleNrOiVipTWKtp9rjtsdk3y7aBpXUwmPWJRI4jBUrgiaXWfYjQ8mFgP_Lc9lBoT7MuPtfzwhtv0bH8ckOcDhzqWCDMgluxWrUxfQBVPed16tGhzh8Y1P9Q7CRgpnnS8HV1cpbwlC1MWcGi-Yv2_MHEzHXcJv2OUbnr3-hCxxuae9zp35OPoIGzDujqRPGuTpNsG-Zy6o3lGvpkIdW3Y53E7XQnr0QLVjdJap0ipR0ltL36aKryiBVzH9bncHOHFJFsjR3SZgxNYTNmDX1A-5UB_m3xy-6xToziBw9Tvj2SDDE-NeiPPC_5fweF5q-96Uxj8lyLRLRWHyAfust2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsqPk0LoOa5FfZn3McNWXt9T0Sx_KrG2_LF_zJYy6RDgCNwW7jvoJUYeMClTPpxeCygvocMuwC1YR0L710W5NZtUT7_U8hKLhJKBA5qB6qLLMJrfod1DtregWMqcAFiIIrk0UkK4neZ7I_RWilOuEGZv9ncMzIZ3T9q0R7eFVOy-gqX3fLvS3poNrpr57ZMZQ-lqAS9SVZTh3mHqEwjY5_Cxf1craWkBM7spiK8ze7vlR556xq0TGZTdIaYFZFfWrt8eZRY-GRsCL4q55Aly8OGC5CygiJHM0SMj9jiU8h2EUNVWwzt_0mlxFtMjmFGWtWFMbm7tqhNleUoKsM2KHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEJ-ugWvCVfvgNtvIGxToIJt6_RVmgUQKBlXqmO43gVc4K2izeKCjPxnft6aC_OLVXg6X4i57ru1l3XIBz38J6NTkzU3y_Vpj6MCKOcHmWdrITdSya_k8SWneF_Zb0buAdhXgf54UxEUuqli6n7PGGWcaF_gBdMdA3VXQ_GM4q9RKY1Rjm1Hy_UqNko23BwEq10K1YvZbWmeO_oIR31U5M6uFJwFLM_zjuvlJZ5N-mOyGw6UkFin08vzmYBQBekgOHMLKbtKVjPYhNnLEv8Ze59ZAlGhgu5kBP0T4dZuZOhwXo0U9rXarwotccB5LgGAqkoOGz9VzNpZvykrfylbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy_lMaR2UdtAXhlT-6mlwKtDWps4xG5Nqe_lIcwisQ6biSUmLmK5xKN5IMW9npojU6kgpf5gMoMRfgZsb8w1WzexuvgAc0gTt-V5dBBsyvrgWGHnuRq1w9-Fa_Rd0WXzk_X-73yCurpXOhct2j_z_lbCP1iIZlblGRiHlMV5phRH5A9EhsCypTXMfjOdpsEKljQPo7k7HzLf9nbrJPn4wmpQMOchMOmGEM7VxkZOCHwbFiUo30isC4GHAiWfk3jyjRj2Izw50wQ6ZBnMKI0tA7EcM3O74B1-yDJt4RIkjcP1WeqzAfqyS1KUw3D30uH1mj9KzgVgO6Nc0ZlWAY7nSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJo2F8fqJA3LVRR5V2rKM2cwRx5zX_diDOn7vOqgLTcPXyRbZfVNkzGW_fjc4P2k0F1P7MpGGZ325I9ROygNTO1EgfTQOgmJ6uN0gRli7PrqAhCMZlT7iVPbq8EjQppXpcejYs7IRlZgHlmwn84iD3ioxw2mNUW933q1yMChMCJWN3E4TziCzRwK-k0jUwfjhxja9vHAP4mtFtIuEosNc91Qd0DQpr_Q0wBl4FqSgNsf4_olhJR1sRBUGwjWqKBlqCPCSkTNNAZO5_UtvYTgxc7q7rAWzRf38trXFlNM3JdioUZr9Au2oSwxuen_71idgy-1tQr7mzdTOFUssMefXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o61k-cKfHQQ2pWz53W9ca4MBOBZ7szTtKFQ4gVlzZTNYAHR0DbfyU8D6fX1kDzS4nULl5126cHDSbYm20b2qce0nk9m_DjqzkiKCRQVLtdsGlyKhuDj08_k_2apa0aLo2alXzY2ZwU2WOtPPUJdAFVfdmcfkUhzjuVktEooxlTcuUGke6LIs5RiKdzJGdpD-9eKiGewmK24m2yk0DVdLu3q8qfr1SgoqeaPK8ZqMxAeC52dH27mKdBCmTUtGkzJ3wmU5YiSen8Fde50btPW-ImGqKe19ANxgC066EE8t7ycdOsfg46ef4Cf4nwEJJ9locPluk9F9YWyd_d5STrVRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8O1W7Q_tOSsAnRmm2Sk53R34GKT1sB3yo8Sgq_xPrU6vuRr7KoPCkAzL-MTgJKK6aC0OKPFm1gVg6fjTN6LFEyVAotgtLZ2b5qu04PyQnFwsOgh4rJ1XhEfJVX2nmWEFQFlDJmBit6v6sRG35_bWv7k_1gsOjzOHB3w9UMqI79RF-kCA50d8s7AS8VI67jweeVpdja_zVhChmqgrvpkEOp41wW7YIZ0DyHpNBaI0Sey8n75jgMO7esBfVEjbNPF-8fiYhHzu11GpJM_K5pB9qK4cXPfKvGGFSqEXzr9G6Ky0ApuXtoLzyp45eDGK-yIR1oRL5gkHcYYSrvOTXPSyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fctav_33kQgKoZ47CzCRTMNOXE97unBdsfWe7g4NkwQOccRGHHo8fcVzjHeSfeDZcbp9DSkUDOfsd_E1LoPlbNaUVjhEYMAz9E9wxDQWERp8_O-JYrktOppKDJ9zHajELNbMFSGQ7TDM9eJuEHqODW1lg4dODbZ97181H_pAxzHH9yMWLAd3H8t6J-rMzzhy5luHrBLTtEUCw7KlmUeUBfIvc7JPHBhNlFIQpsQsjrwZdaLrTjjRfh9eUGNsh-XwcwAW5R9gXCLxsCSQy78lhKfnuZaQKBAQxbsFZTHkX_M2OTyIzl1ZX07IBOWotlyemR39kMbwPgXoPq1XWb-Dlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGKEacWH5sbfap_4O21HkSQV2p1O1BKQe9FLKRIoFAncRqh1IUNGmEFn8RNfBNXlyKGXJjqDjjQ9bIXEtYK2lg-BACFX6uILbErqHxsFw7FloiSq-xI62ZXxS2zvitS4orQUkrmZg3RoyBvW5gt6ZLghxw1WT8jmCd1u7VxsBISbOF_vQXgXBg378OA83UAge2XbaOUGpVFmoZupH4G6QDL7sbn1H-mPgkMORQrq8HNOIBgnhWpPLM_gAJRoE2RKZ5ADSXrOWP7HCMpd62ej_CtO2BDUZ92GZUf1H0fSdt6DEcTYODQ32KGW54RTrQZxPc00ETxJ7rzq0uBzyHJGeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQKmjYSo0pk07i3wSxqpy5OuIxE85wquR13NO3MOaIGnxlRT4nu-TbCLY6_6fUOMgl3yFrDXgcOqCyzl0trOI4_iw7Ns-X_F7MOT9s9bpSADuCdrP9LmGfjK5oPAESRrcYpHLgRvAOu27E0ocMUykYeZUBb8q-cr0qljMSXikmzbhfuyrcoz3nTjoTsTAGSDE5sYXeIaJ6Tx_9ddj9V0d6uq447QIwNH-NAoQDDh48W1gRwGuLD4jBGgZc0PeQ5ydeQh7djo1ZlZ7yYW8Uj-VgjKnkX7RSFF6dcuVSg_scJ1cuo2dQbhnQ0IXxIinWJ-cfMZ8dVL1kIdMBlkXAk76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=ZxI2RqDCdlTNx7oPeRF6Pt2BmLPkCXlCzHV5EkrSLbGO1ZHXw8LB4yyd8yvm95BXxsD6NpJFE2C4s6GYxCKTc4GohFEx_8XkkwYVNVXvHsUAXKU27OzmMn9TmybWLlgnJlJYm-X88QrXZmKfCkPKELE2kgn5fiRs0BbXOBqEZC9STS6WNxWoexDhXXJt1XA1DtSxSxgA-ddzkYr02o-XlHOw_GUVZfazkH3RpxSWx2vJoTIt5bYeB6FfXGAOJVOYHlu2uTqiElmPDUmnu_BBQ-NPZlq2RXjud7FSpOOGdTDNLrtZKvb7e_fClIBHzQO81uTxAwaq4nrDU7HmlIXf0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=ZxI2RqDCdlTNx7oPeRF6Pt2BmLPkCXlCzHV5EkrSLbGO1ZHXw8LB4yyd8yvm95BXxsD6NpJFE2C4s6GYxCKTc4GohFEx_8XkkwYVNVXvHsUAXKU27OzmMn9TmybWLlgnJlJYm-X88QrXZmKfCkPKELE2kgn5fiRs0BbXOBqEZC9STS6WNxWoexDhXXJt1XA1DtSxSxgA-ddzkYr02o-XlHOw_GUVZfazkH3RpxSWx2vJoTIt5bYeB6FfXGAOJVOYHlu2uTqiElmPDUmnu_BBQ-NPZlq2RXjud7FSpOOGdTDNLrtZKvb7e_fClIBHzQO81uTxAwaq4nrDU7HmlIXf0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=kqA1iSjLj3amRjcDtl3nBOrPaNjSOBQT8NyFi-zCGxKBWjWh2pJUrbuYEJJsNH-WonAJF2JEBW0eBvZT1PoHnPHiNhJqVLJx1B9e63r0M1ltq0AJ5NRonk85N7RvQ4YX_7ogcZi4oxkCMW5G1ckcVRA0c3PFx7bSK1w92IC470KqA_RO2JYuAg2QD8GU9g1p-6sRFPMCE5AIHd0AeCpWTH9wKUr4vJTZkzTr3ULBCy68EvxN8Ylx3_0qiOGCQkj6JVpmeDUULTbT2UqPMwpbuAx6z8sCT56e_3B6dWZYctliuDCh_XxnPpCaQZAGFDdqgl8n_FbYQz7tya0puS5uuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=kqA1iSjLj3amRjcDtl3nBOrPaNjSOBQT8NyFi-zCGxKBWjWh2pJUrbuYEJJsNH-WonAJF2JEBW0eBvZT1PoHnPHiNhJqVLJx1B9e63r0M1ltq0AJ5NRonk85N7RvQ4YX_7ogcZi4oxkCMW5G1ckcVRA0c3PFx7bSK1w92IC470KqA_RO2JYuAg2QD8GU9g1p-6sRFPMCE5AIHd0AeCpWTH9wKUr4vJTZkzTr3ULBCy68EvxN8Ylx3_0qiOGCQkj6JVpmeDUULTbT2UqPMwpbuAx6z8sCT56e_3B6dWZYctliuDCh_XxnPpCaQZAGFDdqgl8n_FbYQz7tya0puS5uuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=HKlQzkhTPSWOe73g5t-O4GCz6iU4Q8qU63bJVcQbur-Icl6kOX11TKrVdBcTkyxyKcQa8Ri_LMF9vZp8Xe4_nfEjGoQ7W4p-3rYHNa6YeZ-47VoQeowh2aS8d4s1mBtpooYKFHNGdL3n4z2tO4W54Xzne5TQ2jlfDrH7mTRq1j2PbNqRDhbSQs0mWwJ8Emq8PwNERmlVK9ToWVxsSYSJKPiJAbDSNbfiFUaSrQ5diEXQtca1KGA8OM2t83YynUN3FT1dz0V4GS_reOIUyz9cpZrJjMTXtYmRa4iAbSTCU-LO6xBpeAC4JTVm6oqgqgxi3oTr0BeUAEmqDRjcAtLeFJlITr6ZqaAK5somnEyUsvCMe6bZrMumiI0LoFsajfAWHPKcUemk_8jQClZaZLR99t1lesUPRfBTapqMbWIGo4HmgQNjbc-onUkjSWyCp8uw68Kd3TIaBCrKfgCYt8Yd19mB6Kd5iCbYblNu8kp0vZ1k3gV81xIkW7Eq8Qrz8zXcLpNIu_4CgLOJT8dImI8eYjxPFC-CNqzTdeP0fKHYPUqxFItZs8ecvprKcFpro3AheJyuVV9hp4o-ugWM4hDYHaBahDezV6_AX8-TUyZZHz08H0RVP4JaHq7r39bVoivyybN_jafuN3-WNDwM1a741DEYmdBS0qgxUpqgBita4nU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=HKlQzkhTPSWOe73g5t-O4GCz6iU4Q8qU63bJVcQbur-Icl6kOX11TKrVdBcTkyxyKcQa8Ri_LMF9vZp8Xe4_nfEjGoQ7W4p-3rYHNa6YeZ-47VoQeowh2aS8d4s1mBtpooYKFHNGdL3n4z2tO4W54Xzne5TQ2jlfDrH7mTRq1j2PbNqRDhbSQs0mWwJ8Emq8PwNERmlVK9ToWVxsSYSJKPiJAbDSNbfiFUaSrQ5diEXQtca1KGA8OM2t83YynUN3FT1dz0V4GS_reOIUyz9cpZrJjMTXtYmRa4iAbSTCU-LO6xBpeAC4JTVm6oqgqgxi3oTr0BeUAEmqDRjcAtLeFJlITr6ZqaAK5somnEyUsvCMe6bZrMumiI0LoFsajfAWHPKcUemk_8jQClZaZLR99t1lesUPRfBTapqMbWIGo4HmgQNjbc-onUkjSWyCp8uw68Kd3TIaBCrKfgCYt8Yd19mB6Kd5iCbYblNu8kp0vZ1k3gV81xIkW7Eq8Qrz8zXcLpNIu_4CgLOJT8dImI8eYjxPFC-CNqzTdeP0fKHYPUqxFItZs8ecvprKcFpro3AheJyuVV9hp4o-ugWM4hDYHaBahDezV6_AX8-TUyZZHz08H0RVP4JaHq7r39bVoivyybN_jafuN3-WNDwM1a741DEYmdBS0qgxUpqgBita4nU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDYg6scNdJlr4YNyW9i_FXUqJrp59yfUvUMS1sSwqeMj71oy2l2B8Hjvb0_2zjg0rKJQ4Yr0K5AI4c63UjN4JR5MHLtaZHSjNwwXgE8PDZExUYB04-MnbhM1jWbbAleFxAFn0-LGXn5Q-gU8tjwTstaX0T_xItY3rBU76TbIO6wlN8TvR5fhT97NVjA0fR1e3tAaFsfE7GIpUJiIRGvULPZr00uH7qCjoaeAmvAQWbLEgBtzhA8HrzkvtXgMDmjMch6dPGjdCWw3SVhENF7n22bLxLTN_QlNXgjfcaWv-aXlnvifaDhXZLvxVXmYprbnYLHSIgtRT01qhXHXPcwibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=pkTLP8vwrp5ej9ito3NZO-wkc61ugxFx6D5ilDjesBHyWPajuJLn6n_Iu9O2N3rvxvnzdwjGeGoyh7wkWMulI8t0jXsrXZwPEJCdtXqTfVrZvvB5G0GZB3zWXfMCxLqBxN6uYTaz7NWwRcHrUKVpB5SLKFq1s5h5TmdKzAleo8QUbZGrodBtY-P7TKW8985c_4PRC3P0yGsbiw8VrtkUl-aWlf_iashbrcVs25ZLw7Z4bvNJucemj3fPQsaNgHDyok0GJbStWIv4KL5bPHAEe8zWr-HkHZrMMOLrIkrt_S-M8WN281lItYcyhfGQY_XUD2W3zkYFgJlJ5hBf2UuqXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=pkTLP8vwrp5ej9ito3NZO-wkc61ugxFx6D5ilDjesBHyWPajuJLn6n_Iu9O2N3rvxvnzdwjGeGoyh7wkWMulI8t0jXsrXZwPEJCdtXqTfVrZvvB5G0GZB3zWXfMCxLqBxN6uYTaz7NWwRcHrUKVpB5SLKFq1s5h5TmdKzAleo8QUbZGrodBtY-P7TKW8985c_4PRC3P0yGsbiw8VrtkUl-aWlf_iashbrcVs25ZLw7Z4bvNJucemj3fPQsaNgHDyok0GJbStWIv4KL5bPHAEe8zWr-HkHZrMMOLrIkrt_S-M8WN281lItYcyhfGQY_XUD2W3zkYFgJlJ5hBf2UuqXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zl5DAG7nUTWldvaF53g0UWc-psP6X6gyEWtUb1_hS5CoPYcK9DSbllmWFls8mzlCyt1HE1uPmxHYeIJFObRJeZ4Q9yzxsyCxp14y-uguftqwu_tPkkYkaRV2pr09uaFR8QtR3OaNj_dWxs1KLvFOT9uKN5s5mREbulBIu-4tbEdcAixApWrpsQ3UOGo57ReeeXZSOolwyRcORXXBXR_lNvYRiQzxsV_J7kOkVnT8YI2SelaJcbsFLlLoQ0xkY43-lNCYGC9UR53c7mzDkmLEscNU37rvHjBpVEjP2kXxlftJwcB9Zwb7SUhvcFe4otWYUK0Gxl5fh_zineizCecAtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2qA87prPDkVjcoJQTeQr9DINCQMORNbqQHP6HcVDglB_RoYjKqqX58xxfCNu_eTs-_xelYtW7jwU7KlO2QWFuVpAE8K5TEjOKF6C33-m6CSxQdWXLFAf_NIha98lhmIj-6TL1GTWpznnV2KMBbq1yvvpKcJt5sMsN4CuhJgk_NduzDF1xmb2yd1S4C2bA2hp1nbLQusNGPjqiYmXOxxgu8X1juYTXgpWmuWO_JH6FMxDe8znLe-pSthGZJgh5dh2xIETu_qTkn1xLwMYkSGNKFiOXM9qTmwHu09m-7a84lK8xyUWYx4BtQPu__Y6XpARzgdzOU23MiwwgBOdfrNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZyNSDJcY7AcooqgQh-D_DUF1V15LgAiJeIPPX6_fmSvsCQy1ln_lP2bEkM1NbPFNK4E4TZF_dS0SplApCd1GTj-k8XBgcg7iqQJENaEhp4MyMcokbuS30bqin96H9g9DBqutd_OdemFjdvhMEIliQYRxolaWnYyoKM7ndKrOrYOw1Yy4aSyO-VV6bB6-8ThJqZ0Wx7fXUP8O06U8n2g4Vo7fb0ink3XTZXDQtksGZsTNTHC6eUo3g2YTei3aVaGFYE-aikvGnD0Rb3WIa5eCi67WUaf9rDrA-CQPb_808uge1hVHjGUoqhQsK43Udz1oKxjxwdSB6Ttp9zQXOXQZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4K-DjZ0OPvY7xxKxfl9V8d1Gz0GWQccYH-WltNcjkJ5wa1XDDDvjPCzT8KLEy2ZaAtbbANRBD2S-wSLJveeIV2idft6yVikcpxFBkHn4QAb_9wPhADQ-ob1wOE8mCyUdgsDS2F89Qgf4RVMkZ_axIENG2ZrNcxUfann4zCPPDKmuyaIhAIiLyBJ7EiaLAbR85vMOnAqOSFdvmq_pbH4aKVJm-Fy3gO89yanNphjlROAPblKA4x5fKlBaQY3NZghgn03PipoSZVDodB8O7hiaGtaTtTDIVrdSROgXNdqS6nu8MLCgi7SuZr53t-J9o2L75y91DaiIktoHsBYVAQRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a52KAMJASt5mXN_IRLWI9jOzjtunTC31jVtn5zlAUTICX8YuSi3A_IBSlf73s5gmYzR0nHBVZrH5vT-amKl_Uodnl42zyC-YriYgfTHsMnYA7FBw5BA7iWDSph5Ne_KLWwU-NaEb8EkPcOOyJNyXH7x_uso7gkyeCqBOZphzyqS8lbEFa4ETcf-xRyu4LyvbBWO9pvZOMG0rczoYGV4aoEyFLVRNZnxAozDKyq3GVn9OW4aj1ICeUq9L8juRvEslxvzwk8FS9fdOP6ch6BLH3hFFjgTwJXkd4vNKf56zbWMrYBxyve_nUUku-efZsOK20qKO3cKC81fHz9HzNIPeQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9aPhbKHdgCidVoIfFtXYytqjCZiXH_nn5zaXfGucylI35XYbj3kn527xNp8uIctEcqnRkKgrjaxuvZwS23dMMhwnDH3JPyJSu41z5pmXOCBZ4mPomBGPJ69fIDMkoAqSZbVL5kK8jP1QcK_KBla8s5e-w4WpDnRGBO9dLixSSeznIMSVjztxYLUMEINruFZsPB5-atmk1eE4Co86xT4gykYQDKdLUzrSD6D9XQQzlZWtl0uenZHmEugUKq-zYP2JgbZGrLO6q52ctJKhkm0rk09633wer0KG00qVzOQPr7ov8XyC8uacPm2wA5Ufa6tlOObaoh63hO3RKlnEVkaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5CbgXksH2j1LLVn3Ck-MjHrVEqGsYez3BWpDTNyAgJGs-a6lK7Xf82uWGITFeeJPUUFXLi6tWnl_AEzZcOmxglV4II2leIRmuHf7PHhVe_DGzHjKF_tEt_BBczAfjMcgN4mabUNCtqlHFnetMDrV3HzSslm53xJdapS_b40CgW7-7vvHAd_qp3iD33Fzr9cxE2y1Xzmm9EveOC-K_2VDCDQw7HrscYe_Y467xtHQjUjZrXamkspgvRIR4Zjs_pEyAXh5F4zgGj4aG2PV39p_D0GCD7FfYG4swd1qG6MJ7Mk8A7Lna7ygKDgjstjmqJVidamWqUBIlYskhmaEbzx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JbiRRCGSLVyzAt99W992kIT_rx5IB_R9kaaZwYrYMpCcpZjJfVHpRYmInkosFNOiWtdQqdt8YOk9fch0DFu07WuokhS4lRcYlHMfa9xHo-zzymfyHH4MRp_6ZSJtXV4Nq-KhEfRUGiCsgW0FWwaqs9ZNDoGkkN48KXrKmY0yCtwhndvC4X2P70TQuMs_WWV9XBznBp-Th6I884ir8RL0RYFankW1XsLg5XJm5v0Ni5PUoZev8OL5ON3CMNqv8o_Vjv_3rUIVfXLon9NgRslavA6VgI1ao8a2X_5ylxHUyUxr6k1JIKgUc5c7lr2ey7QZiyCpGsJZe5ds0DBk3oYQ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFPMLQcrTsJY4hYTnLEYHG6N1Ruq3sBg9Z2bQkNwsOEU_Qcq2dGNlGf3SSSemkEMFx1WYra4T53DXIX3MM6jQoIrxdFKgylbif9_PjUKCkBKO-_2YLq1rRuVCBUpopc3SD4RBxYCob1PzeKvt_CdT3cSKeEPm0KIXQ0XufQOSZ_HTgmLcQOIoXJWLj8YHjbQBuyaRFfWSpGenkirVT8crlVgbngyo-RB4iENuktuOFR3fAh8LTpCT5BouqZHGRD1eg5axUcxtcCHd8qTh0p2YmcT9e4R1Sfg919yNbWrfDjK9a3dr3OusDyzAIJoByclEnzjpUelOp8a2MArNEfQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXhsFiWlkv7ClFDzYVZZwpi_vAeOb1w0FiNv3uMOeYV6ftEq3dRGDsKp2vsIl16HvfJBiFfpFN6N6lw7nf9Ryd1B-1fmzDG-ItzW1ejLZGpLW3rBklTjIKGAFKR1tL9cujvWQCGle4L-0SbCXgLBMzhSZKJ2b16uOELEsveN8D89CAFk9HJ1OyLJhmKeyXM3lE_qjVgUp67sAcGKJTrQxnSutGu42bXbW8csZrowz5zQqOiKmpagEB1cHhxr2NmCc3Na-ItS4lmLnsukLXFEUsJh6qj48E1DK4gwOjJeklm-XdO3sTSs2goeRD90kwkMtCXGK1_uutSt0pb8q5UyxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahTeIYNTAi3pwotX5V2VmbmnwV2IOsPrHMyaSodO4R_zkQlo05TXA1uq3mSRAFbpMXKuRo9K3kVjtj8h6elkBhGmUxCA2acblN40Ehh6AOYif8895YGBXD3hkfFofXX8c-9EZx8pPzb4ys-5rw3FR_t9vVsBcyosOArFOoFIW-3f8mHloF2giTPp5IL2AHdK0VnlDp0DAaG_xep0K19G6oTvvsFHaVstti1p7Jb5eaD0LrW3E-3ULcP_pqaW9tbWWbdhwuRtc_g62CZ0-RV2VxACnFiIUkesI1ZWV4oFa_v7adorHXRlLDuBRGQ5GpBMyXhZ8KsbiXGOZnjNKAXdZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npi5a-CIc-a1gAW0-czVH48pylY8U3U0PajjsH0fTv3mzcCSv_lU8mIFv2cZKQ_FNXtO4zs288A8dybfkpJefP9uerdl6PdM_bU4wBoMRoYcBx2yHnvqXw7TLcZAxxDpRHmrJ3Hr5Rcpaescs-AavXBabI1EzwEh0tyYYpICrANxYY5BBv45Gn7v6Ad1RKcbDsPpimV9u_EhaqhHbRFBLC5RRTHgpXZR3BHBsxShBeSK5pAEo_h8_dRJZYDfhxXT4BxFAcRr3qfpVTKPdJc0wI7l-d2r3-GG3SNlBRvvhAjvss3frNjEgINlKBwVGiw1-R3LP-BRhRuFF7HCZUr1Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6oXdztBe0aZbFR2tIPkoUnlOkgEwd4NJF6rZThVB51ipCYJ8JPx0X48lKFcVKeDKPMgvkmBnFXNnyCF6mler2ho5eH6J_wIaDG7Wklv4i81JbLy-4Xw285tivhYRZQl-K9GTqdhcErpIwAL8gyjT7wHxj7rDP2Gz5KLEze6o7CLazwfJYEI8U-e4hwn0wyGJHvq-_Fo5NbWck1MNupKyHuM_zjwKWIbeBcuPVycwTJO_A_ImwVW1HfmmIu7ilyPaFCfrdLfu-L-pBwKDaXJqmMzbgyMZLmcRj5kr2eAMwHWloktoESNEU_MO5V-OIMF0jIMI4sBjNhbzoQjs-hIoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMyGS5rPiY_ZzLOK4F416lggcYYJqRKiWbli7t-7csKvUCbNh2eVckZUbCaDjgfDBb2zt9_2VZZgoGUaUpkw7Fk2H6PHsuHzit4bY7uiemPhJewfAVA29_sBCo6mXMlsv__V2k8wlaXui3W0F86E8D6zoo-Bp327mp6MVajsAFJHV4dSc-6ANnz5Pz-b_ouDLtyqQuWOeuG_OHiluL2k0dcvdTyF_JhLO-0QvXzWVBD_XOv4nXVNx_568cpBrXWPAOnGDWq7pUfuo1UZq5234ebywqof-8rACdx09FbEFL-k9jLUldxJzLf53CFU2zB7unsHxBF3EN0zOKsc-lfeFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYUS20RI-N7OiKavs3QmgHkv9WLGebVSfyrFi97n5N7TZzvtJdBowjG0vo_f5oeG_z6F9Tx41vX69fhnBXD-Yp1P_b8oHslSafXP35jF13c_43-oZ7RcWBhbGQj9gnCa8DeahD5sQdtqt-F8WhCuXlvwlFBmqO-ff_Q_7YCl-ZTtbeVXT3iiTRTbRl4MEDDsDQ7TfmfzMTSgH3CR4waSE_veD_o949AS5NTNKD9qHqW_mFv4G-cJ_T-lh-XlLz6ETXaKWQNYUIfMhLKfhJfM64lluObDe0deK67RpOjivnZkUYO8_lMnzj66wcVqpsKhzUGP9eBr7SVsRTNE01OZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhn1P3gKBVOrOJXvg06vlDlErLpmlAEX3YBWNwhj_3dCt0nOLXfmaykR9ruvkWZSv67dtqyXcAqKxjO1dTLBurDcd94SYGU9zP9sny97sjIzbRx1sy3FTC_zIbjT0elRqEavvzs6v1kyye3XlbGq_TaebwfdIqH2BxySIRZZXyM3lexzoES31_9ZwQ8Xw29Y2_ZG1SG4hLAba1Bh2NvHz53QYaGxYqiG_kXhIEe0ph5Q-WIZNXLOf_XVr7I2coYQjNgKppjXdhQdyVQaAqjdIEL7DYx2jKHTFQDUZ7yeGzW4DfaoulzzuQd1UVLOS2Bi_xrp9c-QD2SrmCG22Th3vQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_1fQaHf_HAiykXzdb8-X4tdzA3OHax7guslxbpRSWjZLX2hUpWakzF6M6AVucUUAGN3VYwBiNjt81KjuYuV0bIYsNJ4w5MLmZJwbbBahUB3cemOGbGgcmiT5wBVFC2XiCp7mHadE3GXp8IHWZSoLwbTZVtUS0AeQMh739IA9eXbJpJecq6sB7fBPcd3mwOMzj4lzWCzoROHi3ckJA1ShkrbtAbibkz6nZc8mNwX4ppJeLRuhq_zGqePIjk6aW7zodVeEcim9wsA2mTrxR5Vg5uq2WFQDVdSRlsd93P4U5Zj_S1qZy6TC5McGY-c6xpzNwhpQQl3rPKRp7VTfXNqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=RBDSL2xiGjHiMuFBdD7B3DnrOiK01XSLRBbJsBbiMdN2x1WSPf-CNyYYuKaxPCDMcqtoCG8KUwa8V-cbET0iSC-EeP-KU09PYKdKT3tweat2CoM_OG2jevRgeZBnPxtc9xJmaQnvSHVESOOF7GxEzyF1mScrhZRKySW3MZqUcn3kTCFin2d2ZdQAhNJhGOwmIPi2IgaKC_I-KTTPAQOIYUJeM_9wSm1mRvPkMkcQnXAmZLPptB6UW9Cpgp6A0wyCClwXSVT790erJHhKHa-JtU3OG00kynQm8QdaCjinadJ8dhEcCS6NtEgTm09Zyn7dVfaxfi9QvixDsR_l2joEJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=RBDSL2xiGjHiMuFBdD7B3DnrOiK01XSLRBbJsBbiMdN2x1WSPf-CNyYYuKaxPCDMcqtoCG8KUwa8V-cbET0iSC-EeP-KU09PYKdKT3tweat2CoM_OG2jevRgeZBnPxtc9xJmaQnvSHVESOOF7GxEzyF1mScrhZRKySW3MZqUcn3kTCFin2d2ZdQAhNJhGOwmIPi2IgaKC_I-KTTPAQOIYUJeM_9wSm1mRvPkMkcQnXAmZLPptB6UW9Cpgp6A0wyCClwXSVT790erJHhKHa-JtU3OG00kynQm8QdaCjinadJ8dhEcCS6NtEgTm09Zyn7dVfaxfi9QvixDsR_l2joEJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksg4L6Ke53DTN2ihTML7pUuwQu-e5C6h_dW_6OtN8U5fLAapy8WB-XRDsu5FFO3SX5VsncfQeQwaYQ3_67A8yf9v6KiuvAU6qreIu46GtwMraWzqvkHXQhLKbjEIgyImH4Ov2xZvUCjBqbtwc5u3FWMFkJQeCy4Rd5S-hEDzAuEdNwPZ_G_Df7FLYVHZPLJ4QS5Ily8aWnKjcCtd5AL5XDgKTVPJDAMKoQw0bf92eIZaXULMmqpEgq2UvZ4PXvcCxiwURtGEdYcrpu8nPCDTVd2lrmuPTQtd_0ItE0zPGmz51TFMcZ5kf8ntwUp9RgJsnuERlntsMpX6s9re-bAoaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBl32r4Du0EMrpIBozWqkcTcpNn8vUjiJeZ3uisaG5ow6fKu137KE2ftfWkeCETzD4O6xjLp0kPlt9EJ6QO70BXtVtlfsq-wvrP_MJITk36lyBfbsaiDWtPdkCvRqY_Au_XmouBGg_vWzL0qvmz3MY6mPgCh9Ld-NGCeKhtQ7MnwY4kDQyeVrGU236mueuJ-JjgTUGULdh8YveK-VkQYVJK6EyOsaWCShwW5-j40fWU5bjU7HDRz4rqyf2jDuFjcOu7cUYVHbDQAWtZ7dSsThkxD_YTotYYTAY4pnEzLEJLv1sUKa8mb_CCowGMkkxfAOg2wLwdzsfkJL629aW48kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrdad7sWc-PBoW0wpTQayDcE2XWvgoLmKxzrQCGrQHFPv_ybiOCBFsnib5xzVDKlooaPIGYZZRuRwzSURlt0N_6u2I2MX1MrT7rv34UJOE1v6uAWjiSWlC0yPLQQddsiMKcdh4omcFsRCgM3iIZprW8YP1ClMH__2cQpZQlJ4D4ZDPScJIp2V-HOR4x4ct_2PfMOUfgkBrjasWxdL8oGuJdvXA7bDcFK8mUwirPcFipPFLk6tVMlr5NI14IVbKT0DCBqb2uNCaaNcIT1rhCmtvxIJ5lrEvn6LivEKPaRd0YxNPf4IrNQhFq-WXWnCXDrMSgMsQxP0kSZ5Zp6W33g9Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=rvCmajghl4XQAIzqIBB29dBl-P4Q40_hmeeDhQ_y2RnSVDGBSk73kQCBohDXFRAhjWeQAkSmt7uiXGcKd4kdcOtPA6UcNUdzfPt40pcFRrWDRkIDXsK5NJLa3IYjk3v9zt8cvgAgFu0SPBDXQ1C61u-Xft4YWy2md7lYgjqtrqd9iOKXla7Ad5c-3DTaVA3YDvRz5BZgIpAtQ5rafHPFzHZR_PNNgGJa7yStwt3VHG5qw-ZZmQ8qaJoe2wypaFCyGQkxogh-xOjnpi9MiGpqkEpfR4li2p3n-0n0IktDyKg6l1UUrRAv8ImnFi7OQcdEQijqjGwGnE4gx87ZXZDjog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=rvCmajghl4XQAIzqIBB29dBl-P4Q40_hmeeDhQ_y2RnSVDGBSk73kQCBohDXFRAhjWeQAkSmt7uiXGcKd4kdcOtPA6UcNUdzfPt40pcFRrWDRkIDXsK5NJLa3IYjk3v9zt8cvgAgFu0SPBDXQ1C61u-Xft4YWy2md7lYgjqtrqd9iOKXla7Ad5c-3DTaVA3YDvRz5BZgIpAtQ5rafHPFzHZR_PNNgGJa7yStwt3VHG5qw-ZZmQ8qaJoe2wypaFCyGQkxogh-xOjnpi9MiGpqkEpfR4li2p3n-0n0IktDyKg6l1UUrRAv8ImnFi7OQcdEQijqjGwGnE4gx87ZXZDjog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMe8dz3X4yHlpGsORu7v9w6WahVgu_W6wZ42En06E50j5ScK5E5UTHM61dcQ38eU6dXUjeq6GmzBZ1yWk_s3-bq-toDzNvq8_6oU0NbRBT3BSh7-sO_LDF5jNOAP5rt7jXhWFGFs1xx7Ymw8mjKRy_8fQtBTno_BGmE908yHXm-e9M10g1kqBNq-gsiEtzzbeMlBsaWL9IL0kxIXIcFPM4qcjjESQxVRCVFgsGYf3gPx4GBHAMBSpxhrOBgei-4eddeD3DMofmTCkrCEAG3EUawAVRKWE6RvsGeS4zvm0vqq5K7xXzcrIQCZo-wFGvni8PmxNlcHX4eJQSuLfgXPJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=sLbf_MS0ygJ-6eHD0WWAPlNy0S1oJqwKTk3dygAySbwSMCBINBsKwShlc3VzFnz4asKjS3KAay7lHWEiaW3swQYsh_a_djQm3nzPcLnaG22N-rr3pWKE9KjmSI6c-0U1epvd9eBL3AmR74wD85mYOVOd8d1BqZlyUQEWp8QRWEmdnySt8IBpg_Vle4M3dUy9wT9NT1wksPS0o75wX2eRK-weJxl2utt0fnLc6sVyQtOoZ42IeXG9PPGN2evjqdw9hXe_YXll4sNACgqxjCL83U0cravtUgODBFm6MHanfhnEMgjHSwXk8sSpVxoG6N2UgF_-Etvmjw4qYbklQ7tY2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=sLbf_MS0ygJ-6eHD0WWAPlNy0S1oJqwKTk3dygAySbwSMCBINBsKwShlc3VzFnz4asKjS3KAay7lHWEiaW3swQYsh_a_djQm3nzPcLnaG22N-rr3pWKE9KjmSI6c-0U1epvd9eBL3AmR74wD85mYOVOd8d1BqZlyUQEWp8QRWEmdnySt8IBpg_Vle4M3dUy9wT9NT1wksPS0o75wX2eRK-weJxl2utt0fnLc6sVyQtOoZ42IeXG9PPGN2evjqdw9hXe_YXll4sNACgqxjCL83U0cravtUgODBFm6MHanfhnEMgjHSwXk8sSpVxoG6N2UgF_-Etvmjw4qYbklQ7tY2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ko9R4V3-L1qsuOxGrGrbSLcmElur-vmGvjCjGqsrZ1fbfjLC6MEcy9v1uSd5uBdcSHSr01rhId2-ZtzYg-jI6hOE3_fWqihjiMTNxqDnsIU4aO1tia1oMNv-qEtqOnc7R_I9AQalzrEg5kejUMSXM9brFyLd2ESHssZKgwLiQATH2J6_0BQ29PaEyjeE5ndcettX6kOoo9ZE_SxfUqP6_B0qk_yDfUiFVKQiOs5QEHqyinmTFxg8R6YxkloVX8k0E162YRbWIsujkphBmLoJ4mimFt1l4KgLwryO9bCOtRl7UIfE60O-LNg0-yWNeE_h5fSHwk5hP-oprJMMBrJkJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxG2noy0x-P7YHwfGcN46CkYaqxqeRSBvS4C2eV76w1GuMsRvlSx7k_MNynOcFMX95QSSiPfI8Y66azCz1iUR5U0sqHGHpNdO41jk7xoDGxBLli9FQK_14m0h2WtI9Rod0q-PeMugl_yCdbNpCk1-IzUxvBglsibriUu8ZXMcY6secxBN2Tm-iCCbWRwPSa-PI9Y--y7A_5_BN36z0MMKuv2sBlcRyLu-EM9HLhwUe1Dq9usCk2IwdEq5b-BK2FRnw_kUqK7ZRPHCKcx5OZpoqT6lkyCVaBVq6U3ychaIYUtHP5C7vzdAW55WGL0xPYvok_LhYCvVpGMTnDpSp9Wvg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=WwV9rJtc91kDFkzM-sVUjwxqOn34edLU6JFrHHXi-RUnar9C-V-3I8PvDBpu67pnpU6P7wOj-hKnQxpZOjRspsseRSGt8CU-4V9okCDPJq0Rh9A9FSRIu68-Pgyk1gsi_LhzjQRv7uThJCrkGnf61qjK5ad5QEFZ_dYcRdIi20XNzHthi1EwRt1EpPIcgxyWgjIuiF-uZUoMplnIeK0qRPMelnW86kN-_e1CrazZGBi8QzwOUVq5MAaoGfwrFOmmvv2EHOJR7a2arkiLm3b9evLPdf1NcWFCSIqaKx6w9GpFmynwEU5ExCQCS3uR-oZ6socCnkHcWa7W63eNDGhafiP90Xf_jbN8Vlkcv3uM0tcxervnl03RzDH4agm_L29mRjQbF7vOIMKd2QA0Fk_NrVISpX8VTTBScbsbZTHAdY6wz9JwmS6yvnOZa9gG797ccY_qMhXHQjI2uL3eMhdJrIJGksKSJ8OkyhnpP4UQN3dQYC9qDiIX1pBtUX0lrMr9cwbliU3Pm6AvMhXAXYhh2q3kZK8zRpxJ1-Txxlg-GSB7LWn4hDfShXBISr5Kmg7w2Oz3iws8JhJ0k_XyeQEeXiXwbIFrA7AUa_uuOKU6P75m-mK8FeFWIAGO3dKF0RvzH3f10Gv9iiAUvP-r-VKqL1cTIukxzSCh8Cyikpj7vI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=WwV9rJtc91kDFkzM-sVUjwxqOn34edLU6JFrHHXi-RUnar9C-V-3I8PvDBpu67pnpU6P7wOj-hKnQxpZOjRspsseRSGt8CU-4V9okCDPJq0Rh9A9FSRIu68-Pgyk1gsi_LhzjQRv7uThJCrkGnf61qjK5ad5QEFZ_dYcRdIi20XNzHthi1EwRt1EpPIcgxyWgjIuiF-uZUoMplnIeK0qRPMelnW86kN-_e1CrazZGBi8QzwOUVq5MAaoGfwrFOmmvv2EHOJR7a2arkiLm3b9evLPdf1NcWFCSIqaKx6w9GpFmynwEU5ExCQCS3uR-oZ6socCnkHcWa7W63eNDGhafiP90Xf_jbN8Vlkcv3uM0tcxervnl03RzDH4agm_L29mRjQbF7vOIMKd2QA0Fk_NrVISpX8VTTBScbsbZTHAdY6wz9JwmS6yvnOZa9gG797ccY_qMhXHQjI2uL3eMhdJrIJGksKSJ8OkyhnpP4UQN3dQYC9qDiIX1pBtUX0lrMr9cwbliU3Pm6AvMhXAXYhh2q3kZK8zRpxJ1-Txxlg-GSB7LWn4hDfShXBISr5Kmg7w2Oz3iws8JhJ0k_XyeQEeXiXwbIFrA7AUa_uuOKU6P75m-mK8FeFWIAGO3dKF0RvzH3f10Gv9iiAUvP-r-VKqL1cTIukxzSCh8Cyikpj7vI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=n8_S8sHPpNPmUT2VTmcaBkyf0w1lfZbRW3k_guZQXYd9bTTcbX5gYQBJ6e3qzhzNLysXHRW0CF5Q_73Dxg-vIkXXyF5b7PmMfd2fZoFYLyx_AmsbuBy3IRyyRa1HF_qMHlqyKlbnd6Nrh_rR5lbext22SETuJcjC2na2Y7sxQiV8tfAzoTlyUeIIezrqFEAayxmEdeYwCAdB_joLKOEGfDYcydHZvAUbaTGgsn-3nCc5GuaMy8tNdU9gcTuyy__MXxCJwiguyYqewlGEOCauvIiMljdOGNeTLgXv29GNIeESV7Um-dgnQPdzIdmxnxIskDzkn7QLaG7W5NBZlIcXFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=n8_S8sHPpNPmUT2VTmcaBkyf0w1lfZbRW3k_guZQXYd9bTTcbX5gYQBJ6e3qzhzNLysXHRW0CF5Q_73Dxg-vIkXXyF5b7PmMfd2fZoFYLyx_AmsbuBy3IRyyRa1HF_qMHlqyKlbnd6Nrh_rR5lbext22SETuJcjC2na2Y7sxQiV8tfAzoTlyUeIIezrqFEAayxmEdeYwCAdB_joLKOEGfDYcydHZvAUbaTGgsn-3nCc5GuaMy8tNdU9gcTuyy__MXxCJwiguyYqewlGEOCauvIiMljdOGNeTLgXv29GNIeESV7Um-dgnQPdzIdmxnxIskDzkn7QLaG7W5NBZlIcXFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCmL8VJdGn4kGgrb8doPA57u4Bs9ZdPjXzIAgEYlnG3KLfhyJmZB1x_FUv-j6A1NKbDDvy8oYOuWISFo8yLf0IQ7tjxfD5oitFZO6qr54NIwR0tEyrHe_h6ei3dqe9ylNDhcrL1GVC-f6IwNcVfA4RE9CsiNqzHLAGqm8TEcqrS9EJ6lhr7O1VYMwUKej1y-r3awVhJftER9HQkqBRBFmoM79gvhPR50IHpR26Y17Vndszz3cgY-QrGZwWabjsso9DyWtyXH4pHuvWObJA1mSPv_saqZIoXFdQhp6a7kmk9djIY9uEEXhylYeH6ablLqR4-ZQ0DvUsGT4XlOV1IldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=F8E00iuT2hwWz8ApZzXaEx2w8VOUzp3zDCC8oe0W5j540_RiNQzq0OzDbU443aMd7vj_8-0wEeJhU6y-njPpH36foq_Rqptj-c9eTUiMFjT-XIo8vVGePRgW8m5Zo2kKhBqkjdV1if9gM1j3kRiDdngdGg0aSITtyzkBXbIQY-j6951SDn5Zfxwx_GZX1ycg52pJZY23r1lgCOglkndiMZ_CTYC_Z-ZzfSJeKzynKdzvyKTTpRQTGg6QobkLSX9nVnxkPqJ2o7SryREiwT43Y7K4jxeD5sM7wtu-QnoIcXaIVzv3kUaIbvRhSGFkNh5XVWyg0JezSWbsnxjIcXu-JoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=F8E00iuT2hwWz8ApZzXaEx2w8VOUzp3zDCC8oe0W5j540_RiNQzq0OzDbU443aMd7vj_8-0wEeJhU6y-njPpH36foq_Rqptj-c9eTUiMFjT-XIo8vVGePRgW8m5Zo2kKhBqkjdV1if9gM1j3kRiDdngdGg0aSITtyzkBXbIQY-j6951SDn5Zfxwx_GZX1ycg52pJZY23r1lgCOglkndiMZ_CTYC_Z-ZzfSJeKzynKdzvyKTTpRQTGg6QobkLSX9nVnxkPqJ2o7SryREiwT43Y7K4jxeD5sM7wtu-QnoIcXaIVzv3kUaIbvRhSGFkNh5XVWyg0JezSWbsnxjIcXu-JoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXVYQmwVtBN4Kp34E_cCsEgbo7BzxlECb36qU57xyUigWXjS1CdEXOjbMIZW6uB0iY9FILZ2nEposWN0Nq86nj1wkubNPu_2fNMallEhG0ljRDsDSVxo3FusN3x-9f8IvwNUQLxTgKn6JiPDSOnP58t03TPwbWK87Kd1LXUlnSmJf5UBjyL0fB4FGwcQUwzA97JajEL6_yBfBlg-Os0BJ6Pdxhzbl3aCJpGYG2U19rBstFc7r9kp-PV0y1IV0cCZoxjd6y42ccvUszWKoxP2BHTCXqyCo4JvVvVA1NQgsGR_o06vr3B2kpNgjGHMilOxp8ZDNKaa6JtpcCwlnHr-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqyfqFHuFomoz6spCre3a6EhMgmxRIDYMDsu6ULLQ_ICt1m2ym6TPwNY5oa1W4LLyNpiaWWgsvtvO9lCydcPdzfcP021g6kGXJfr0hY7c4ByGgDS_b4u9R-DTH_aM_9nfNqNzv0vHYkMzvyywO08s_STWpPhktPWyyIhPPbzWBAIGijkQ_RrHxmkQmkyDbkTHMC8w6DCIi6X_9oHKO2YukNs8tAV72WFmLCXcIiRhE2tRAR86Kx_eSpw5TGeab_AArequAHfhkWiCzXBnJnZDe8CJfCnHGaR3ngY3EMtl1VRMX7N6ZRvsooL-_fwAAsmK79l9FdUIV7Vlxz5hMXGDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4zsL3rFpW0Ug8ddRCyqVe7Q07S-CKHCqAXrMWLi1bPs6KpUXuzAyWGzXzYqFkzr1fvPIIeLcr-Xm61tbUizw0Zhxr2pVlOI6VAJVEfCDWeXThScx-lS5-B2opczqRaO57vlHWSQa5UwxtuDgSfAJVfgyAaky4CO3N5ZW2YD0arZC8FoRgUKXuO8kYN8ImUIstmqhd7Dmrd0pxciQPiFGpaHTCKTWfs1QV9dzcSqX4APi4au0z8QsnQ_97YBIUFAJCNWFRZ5ap5PJ4WBkvcn5XyrsqhhCnFbqDL3gA3VsMWyqV219dsQLsF336JT_9163yywQDddgyR8Y92jjKyQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suSxX07vL1-Byd6nBAWNfTnX80R2VwVv0F_-1r-ZCgOEx9cVYZcYkEysEao_8nvvX1YjjB4ZAjWnTdiZDXwcrcKv_kRfxyaONlJ7KFYTYWpuWuqUS_DbD2spV-Egdcw_XCg_P2oiH52ChDijqrYM2uLfb9rI2T3tZTs24t1XU-btp0kBaSlBJHZX6HhkgBmyA-quZvEmp-0plOOh5hE3nFyVxC0ObRcVrl3punvLC2zGxP601mS4T76ezVkw6PDa09TeycBz78OzYzsI09EaBiyC_E8whJvzNWJhDvYokbiKxri6sOUC5qPsZ7SqI6y01emkXyd33coCBKWH4jB0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-C1r2ULqcZVnCjEdboEGXrHruulPrNlQzFvdPc-4shHSuOnASyXfzQkdm2oUMU4DrgP2XKlQSrU1QixAr-OzV9nMBpPGYLn9NbIsjwhsTDLPtTwa4XwmmveWo3JThgLyw4EDczRRiL1-CfGipNZDeOa4oS2o5mSw0FNzn7C6OoNKjz9N1DdMVyQKcFVoFyCvA3ewVc9aiySoAqb0KTS3w30A46cAtwQIkzNfom7g3pgE3uu696CeMSxr4iNoNwQ67o5UvnPdS2f3HtTr9ZxlbJ5UoMG00qTgTKfQEfnuuZpexAsMtHqPmJC4KV4LCkfFvFYNmwYxNv0EehNr5xVYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=KiTf24RAPGbAmOOOQ6DwH2y75eWR0zexvCR-2_p64A5xW4wzkwsRv2GtcGL29T6taPU7dpTFWBQkZlyHQKkwbURqe_tnKzqNFbXAfQRCMSTRugksHgcuIKZ2RfvTO-s_V1EIy3dg7suosV_9TbeNCuw5N_5zZaGjMejnUWwj4Dx_f4_QDC3T18ONZ232oNcFRnLgoz8UU-H-tKXswGrmc0phD6zk55kvuV3AX3CH0_JuIS7c7p2JW_VQwIc97D60bgJ6X2x8ctlX2OO0DB7nd1Lf9tizQkKNj0Zk9xY0VcT97Yzxpib2RaiaW2NBKjzpqN_vfLVvzEZVZVGdQOEBhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=KiTf24RAPGbAmOOOQ6DwH2y75eWR0zexvCR-2_p64A5xW4wzkwsRv2GtcGL29T6taPU7dpTFWBQkZlyHQKkwbURqe_tnKzqNFbXAfQRCMSTRugksHgcuIKZ2RfvTO-s_V1EIy3dg7suosV_9TbeNCuw5N_5zZaGjMejnUWwj4Dx_f4_QDC3T18ONZ232oNcFRnLgoz8UU-H-tKXswGrmc0phD6zk55kvuV3AX3CH0_JuIS7c7p2JW_VQwIc97D60bgJ6X2x8ctlX2OO0DB7nd1Lf9tizQkKNj0Zk9xY0VcT97Yzxpib2RaiaW2NBKjzpqN_vfLVvzEZVZVGdQOEBhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6d6CYokokHowuNGiDgcigByIMLyDyx-703rBB632Geqs_0t-9ClApDx1jgZFIp2pU-PUcWl55RwwXdi65Z0nipbw0kNMBWy189gbCY2Wuwr6eO6QkD_X_sOJvxKNkeuLGopffSrUkrHnMN0JuXvnqeNuBli322PzJLYAfu890Yh_CmMFzUWC7H1gt9tJInx-sAus8mYxFt9O1PBJQGdr6UbZGu9NWH3DCnbEG7fqHYV5SwHTqi3vgSlGM4M9Un-tnWLSXE8F0WeYdMtmgkOnepEf5GlkGFrVpV2gqvzC-unIXNm1zjXem_co1UovrIqwGoSP2BXBT3BXOlO2aW6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhj-nMCE3577ud43wLk696mI3dWM_GNJnCxFh5PMZ4js2Ea6tXTP8by4BDuVS-yE3KugR_HEx_yNmIX2q9nGSqGOYA2P7oG_iaKeFGPrXmeHs3478GoNwgZj-EHqYy13wmcLq_itwfy6BR2fpVikudpy4ovE_gtIsIP1AnnGfs3tnXCogHYKLiHk2haj38uKmvGQNcdmxVGh7R63B3R7fO3P-E15lyEQn-zC-GMIj9AbqXvMvDWH1oq5TXc_hq_Nl4ItINTEh85RTeF7xore7Mypkp7WZ4ttzbK7TqiEWysAlSI-Z_9zH7eEymAWO7KpN5Q3jbY4fs9Sn0iwJP93wA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=t_PN8q6fZA9U9vz0hqsJUPpy_BjfryrPC_VHku23VvLpooFPNRFCKpEtB3SizNxHV6p3uGZZbtuVAwzkcoI0jXEOWJ3ilMEfsksog3R9T5aAJ_07heT0H44YQkzFej51FlS2KCEG79K449DKHDLnHJWFqplTEVitTbJ7Y-1JxUJAq3dxr7Cb7lKLPZtYiraULsIKJSRnhcL01bfwyXeKVk-RGD-AP4I60BsYNH2qipCSa2vTJj-iT6G44TeSg-JjylQMiGENWgfp-IxtVo2YMP-RHYDmnINwYiPrqAUOBLig3hpPYZLbN1qT_oQeDz83oLqaxavONurdXW5EbBG26YJw2Cbz36zRKIp_pE2sBVK8Z8zcPOzMLeQoGv-bLYVA2aYKQJQpELD6aCrsXMS-kin3VGLz3H0j_PfK8saNvF8-nlADJ2Y3L0ks0-0bWvErjnDLIIac2ucp3gIeOkQiZ4GzX1TUA4p7p5s6nxUWsJL-2fFgXupZipWQPyJnjxk_kuzg-g8dFlzCO7abuUMc7w9tDLh9AuPsRk8GFUDqi3TM0c-PkkapgHbjAAaOAbjgCZWD5bExMouxI0lWlTkVPPnKMhyuMMmB6yMV4ZjyagPiLhbaveGhDsKjtj4b0qZAtscT69q-m0Ev30rD7HHjysF3NULqiBDxhFEzJXtJ4XI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=t_PN8q6fZA9U9vz0hqsJUPpy_BjfryrPC_VHku23VvLpooFPNRFCKpEtB3SizNxHV6p3uGZZbtuVAwzkcoI0jXEOWJ3ilMEfsksog3R9T5aAJ_07heT0H44YQkzFej51FlS2KCEG79K449DKHDLnHJWFqplTEVitTbJ7Y-1JxUJAq3dxr7Cb7lKLPZtYiraULsIKJSRnhcL01bfwyXeKVk-RGD-AP4I60BsYNH2qipCSa2vTJj-iT6G44TeSg-JjylQMiGENWgfp-IxtVo2YMP-RHYDmnINwYiPrqAUOBLig3hpPYZLbN1qT_oQeDz83oLqaxavONurdXW5EbBG26YJw2Cbz36zRKIp_pE2sBVK8Z8zcPOzMLeQoGv-bLYVA2aYKQJQpELD6aCrsXMS-kin3VGLz3H0j_PfK8saNvF8-nlADJ2Y3L0ks0-0bWvErjnDLIIac2ucp3gIeOkQiZ4GzX1TUA4p7p5s6nxUWsJL-2fFgXupZipWQPyJnjxk_kuzg-g8dFlzCO7abuUMc7w9tDLh9AuPsRk8GFUDqi3TM0c-PkkapgHbjAAaOAbjgCZWD5bExMouxI0lWlTkVPPnKMhyuMMmB6yMV4ZjyagPiLhbaveGhDsKjtj4b0qZAtscT69q-m0Ev30rD7HHjysF3NULqiBDxhFEzJXtJ4XI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=Vo6JB4qU15XCk0X96iy83hY7SF206ZTrPMHSK8kT9UeujGDh8aCsX1E-rHfJL6kwgfQzoGEwKj93oT1CTyLzyqNGLuCJHHczXweePJz-xhiSMO3CZevynqT1PEu-UhxQD90CneAs7Sd7ZFCnPRpBqVIjuV2Up-K30mu0kkslCueuj8eL6r2DgCglyoXhbXS5c7_7hRt4Qcjp13Kh7eAzOzyMR2uRHiPVnjMFfryWVCh1DLFJamrGGY87gRMAo3kGVgn8bG4I645g20fn3Bnnbz5hmEYc8BjKCa-f8PVDta3tC6z9tmbn_19Bj4Lr6cDM0J2cVcp-NPWWlIDLO6eImQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=Vo6JB4qU15XCk0X96iy83hY7SF206ZTrPMHSK8kT9UeujGDh8aCsX1E-rHfJL6kwgfQzoGEwKj93oT1CTyLzyqNGLuCJHHczXweePJz-xhiSMO3CZevynqT1PEu-UhxQD90CneAs7Sd7ZFCnPRpBqVIjuV2Up-K30mu0kkslCueuj8eL6r2DgCglyoXhbXS5c7_7hRt4Qcjp13Kh7eAzOzyMR2uRHiPVnjMFfryWVCh1DLFJamrGGY87gRMAo3kGVgn8bG4I645g20fn3Bnnbz5hmEYc8BjKCa-f8PVDta3tC6z9tmbn_19Bj4Lr6cDM0J2cVcp-NPWWlIDLO6eImQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCrW2Tui4CmaewdGQRJMOAB7XJYmZdXu5kouSM-qqOY7b1O_1Il1OErZrPzHHAfeGXf7WlGr7tPpIs9_Zt7PjvkUukIQbb-H4rijTRaEAOHu533FGT7eUsRLdYURw9HRGf2ZIG9xuB6fp5HMTf_oDm3sd0fsHTLxDgO-erEtty87DhD05iwZ34LEsiP040B9LsKfBJ-IDZTWCu73IAEaXjrKUXoIPz1lob70oTfx44H2yWpjwEfrIfdqydDwAUdBlg66cGSJtgPCjBJOH0AIu35PTOumpt4wm9Pc8Flfea2a94YYnwlocC5xyJlkMn4mkVEnfKVVLrcCgyqvfxEpfFCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCrW2Tui4CmaewdGQRJMOAB7XJYmZdXu5kouSM-qqOY7b1O_1Il1OErZrPzHHAfeGXf7WlGr7tPpIs9_Zt7PjvkUukIQbb-H4rijTRaEAOHu533FGT7eUsRLdYURw9HRGf2ZIG9xuB6fp5HMTf_oDm3sd0fsHTLxDgO-erEtty87DhD05iwZ34LEsiP040B9LsKfBJ-IDZTWCu73IAEaXjrKUXoIPz1lob70oTfx44H2yWpjwEfrIfdqydDwAUdBlg66cGSJtgPCjBJOH0AIu35PTOumpt4wm9Pc8Flfea2a94YYnwlocC5xyJlkMn4mkVEnfKVVLrcCgyqvfxEpfFCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emYFvSGcTri66hqv-Y-VKRv8aeSS67G78ZoHvMUMluFMEnGyeGIpv6E-bOeigHiK4i5UH2UDIdV1EcWDYV__0ztCZwLBmgSZF8-iDZsfAfPNU82OY5OV7OToJfksdQ8ikATyLS4wnYPkwJygtSez6TKrcOWu02NxuaCGBwsV0CO_u4NhZiT6u831qIac2N-jOt47fQp2PEx6c65oGTPjzrxDnvUW4LDiGltNNgj3YgmorNrIl8NIZ5aWZh1c850-dAxzxAUXs6IhRy4pLk4Te8BaZEX6hnPOjNDZd16E0NtKD9vn2Ml_NzjRBVqCsZTELdjb78MPqvUO59yKDglRrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVNOzjl0WIwsoRaTH4BfJWkpGeRr-QDnCfCbyY0A7J4oUNl9n_Op78M-hDAIoY5Q1_zi952jKPAIljED5ozWpvtKS79qmBAbSuFihHjglVPPW1TwW0bh_T6M5EiJmTqKyiWlICw4_bm7tIUvjvaubjGBYlib182987RzDl-dReTPV9Fuj-uphTwRVvGSOS20UaJmq-Tp2qHiv_hnDnhyuUK7Ed3rDdPR3xpmVgccGd3Z0boyM97aecYeXqlMQYCqnVg-3BjvOmVlP-0bMmAXw4hrjswZ99UsuLnjsC1-amcj8hzDnJSpiMDYoB7ktlaMUah5fBhOIlpYZTDLWX3C7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
