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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 22:22:45</div>
<hr>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgyfBDuDCJAt0JNr3swz4HIiKL9HrZbuqCUgpWgoWH-EZ48shYa12Y9jdCvxYiiUNFYEdJyEo7wU00C_BFnb_CTyVpzrMF5rOaoq9kfY20upu4yrh3hB5FuUoO5req5uCes4pUb52gmb0Fy7wTOXqJ3zoNQli2K0qbjfW0UG-maUyxTkGqrZoG-0yyCxvc7BaTOLtGogCdjOavj9BXcFLXh7XHPNWWIadDPMDLkUiV1vEWOIIbA-gd7WI75ohIeh1Pk1T33bNTZMkSWE1h7eaOVXSgYf4bfPEE0IOn0k3beN_HQF1mbN29UXT4qshW1DSNBZOglA8ZOoGk8W2oZOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCJL3-8VxSn7fEsY3P6E7Yu35KygkPYAz9kSrPiP6mOf8U_s1hTygNHV29aoJtMFV3uDNu2SOmOr0pRE8Uvfb_4v3pd1wxSiC7wpZnrAVsKJuukgP-edn0XvKe6r92a-BQk70aHqprMQhb3F-ozQFNjyygGncCdKUSeTnA49lpLU-LKQovR3tXzfRYEQ13VxHLLbiH9ZOq8KL8MaWIGiCzWEk2jLqvCACusOmTarI5B3ycu06qcPPIP_Ppb52ylFXvsw2sTsuqNG8bwZzP13zYu87MoCAD9yHgVbxg1mP8ENRHtvk-EBW8FmpMPAivbYtiDzL3qDs_aptE84S3_x2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4kUTxRXfz-D5HD_bWoXgRgrYiak-pVLXVxgp4-BeojCHshuIc9HusfxGkpxvb3FpuKDTuEJRotNcjc1Q4l0UI7S8dvhFlWitvfNEqTMoz9DO13EehM3mEg1YTptXHXCp6iWN1PYngvlboCUMmcJgS_fU7dwZKWFh8-wNn5fgjmqOkPtTkiFIcziU_eUdyuIN3IbPFQ3Ybr9jGdcwqUI-UwnZ5Yq6tio2u7PqDKaggJpV-PxFW92N2bMtLam1MDfxNe3ATnZs0KToZJ0EYnesRz_GSkv1NFWkCFCB3bxRL6XJnxJzF9ATpwzI_MDdbaOGGrM8q9bDWB8BdYZxQ796g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=YEOHdLMVPtOYw3J_5YPdxn-Gv_SFUFocUTead4paxlJGZnTIUZV_hd1LI9wNVEaKNoN4gm3gWtJ4cppuv8BUVDoGelkv7IjFGqQiNpguBEnw4Ut7g-q7tQEfJkUKWQyTL5jZECN9R1DWNqf2W-m-lqWgu64xR_w2IeqNujmzqOg8E77WWbpuSUUQL9KLjZidEWAPqRsVL7aJ-P3hMr0sCeLuZKZvRsSfRe8zfqAyf76VHo7sUY_VzIZ5_aoAK7TvhZpTr0GrFHOLuSocKADvoQZSoI_--UyZ6W1jvoJ8UQ2O6lDo8F0zwst55t3ABxnCGemJSaEJ3wpxXwKYm1kVOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=YEOHdLMVPtOYw3J_5YPdxn-Gv_SFUFocUTead4paxlJGZnTIUZV_hd1LI9wNVEaKNoN4gm3gWtJ4cppuv8BUVDoGelkv7IjFGqQiNpguBEnw4Ut7g-q7tQEfJkUKWQyTL5jZECN9R1DWNqf2W-m-lqWgu64xR_w2IeqNujmzqOg8E77WWbpuSUUQL9KLjZidEWAPqRsVL7aJ-P3hMr0sCeLuZKZvRsSfRe8zfqAyf76VHo7sUY_VzIZ5_aoAK7TvhZpTr0GrFHOLuSocKADvoQZSoI_--UyZ6W1jvoJ8UQ2O6lDo8F0zwst55t3ABxnCGemJSaEJ3wpxXwKYm1kVOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=q57YD4nwooRYNVQfjQxDucVMOS15EqC4OVGlpedKA2F2UxnYu0byFUA6qI6G9U9FEcDcmQl3xL6A_NHnu_D21GvuFr_GByZcLK_QMWfZ-mfpctpyaa-U9Gm8kVPKTpkiM2SSK_OP4wzReJrmIG_Msa2_v_05PWuCjZ6wGGcua0ztX-stI6Gbf-CkbH7jh-gwTC3o-bNmHNEh5SHmLsNCrJD8vRjZ90yBeVm3QU0e5dNTQhCl1fKyBKIa1-n0kQ-sVcmPu3E15OwAmVXzIaPoNLLYram4NmXHn5W7X-hVn978t3HoVm9rnzmdwKLdWGw9MGbX7sISckjXUFjAOKK7cQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=q57YD4nwooRYNVQfjQxDucVMOS15EqC4OVGlpedKA2F2UxnYu0byFUA6qI6G9U9FEcDcmQl3xL6A_NHnu_D21GvuFr_GByZcLK_QMWfZ-mfpctpyaa-U9Gm8kVPKTpkiM2SSK_OP4wzReJrmIG_Msa2_v_05PWuCjZ6wGGcua0ztX-stI6Gbf-CkbH7jh-gwTC3o-bNmHNEh5SHmLsNCrJD8vRjZ90yBeVm3QU0e5dNTQhCl1fKyBKIa1-n0kQ-sVcmPu3E15OwAmVXzIaPoNLLYram4NmXHn5W7X-hVn978t3HoVm9rnzmdwKLdWGw9MGbX7sISckjXUFjAOKK7cQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2_E1AQlneS_cWCRrq5Y3jwFiXuG4ui0Ii9_08ZKYtz09YbS_WJfTwlPc123MLJOdhhH_uC-OdHKggpLPBVwb53aVYVMVEBbupRct10rGikUu_egMhVBeY6Em2KRvNLN6ezMyc4cWaC9i_MxVYMpSkLayYAHulZRfai4ia-sc2bpX_C5ECLJElMpv0na-g_yK-IXmaFsCEPMC-nlvTYLcWtTKq-C_bS-OPNjqo12ju_R6nRN9k0cYz4yyM6zZdi5keXtqS5peHUOYvI2bMIJJ7uSOObqEq4hxrYxJwfmYDhpC28kK_jNsQME_sjEe4kgWMDPvxMKozXYX_KQ2tif7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUv5anB2qfc-brRh1IVJenxVNXBR0sZCsS_HQO5fDdRmfS3qbRGp8xsjEf9Uje5nBbcXkC-QdgDT5oHzh94KGeFdXLTJhJUO7yOT48zlcgCBEJdFxKmbzPLPMT4f91Se-3Pxl4zLbStIjl3sROPy4gDLxY2Ji1oTx81YlzciaS6Kjm1B_sqLI_bHtYm-5M6GVKX-iAjZD8qsuPR05UFej5AAOGArjArlLCmiIMfcGvInvBRZmcUYzDNd98S7O2yy20QFX9oTOhwtBJcmJsNQHa4rBEB8PMp4Z5J_LZxafM2YCH8__zbDb_rWZTuZhYe6o0Bok-mCja1U9qPhTmi8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcZi7B3J4v_54mMLaMeLbmyvCkRt4gactRhXoIeiHZ-AsCFJntWeBWWD1teE-raiff6dcsGETLsCRrIJiuJHzZex102YF0xsErP7Z9AoGBxeX3d892LEiEAAPHH3fpnF6ftl4I57kpboD-Nc__bQBfFKYQ_XiXuhEBJjoZMeYHsLXpD0c3QY5GoE5zJlm5fP-FHcR_xZky1Nqen4CRU6CmucOc-YqyeeZhaDdHMDOxGJ29W0RE_tp8SQW0F5eNwSzYxVKKT2yCWcNnXVkCxe4ZhTuajsrltArbYh-HSEBLH6uNdX97-xuyFvm1BW-iBDJNuLrltHtwoE_JQpUxwjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDV3RgDs8RBKdPKdVlP09jUI7ILHH8KMVZux3BG8vIykVG5gQ7mhNrSrnQAvwXsH1_3FRG6lf5r7djnM3fPSevIGECIzS7fRODdgM3AwJRtYURSu9R5e1B3qq0D9ugDgikCaat5EzXwqEP7a46bJWd2kcOTllROYhO1PgeFBeEimiqkxt46FTSCV-2ukEKzTiMUpGKVt3qe1e57xa3rnj8eo2qGcSHm_rVAtGiLh1GhIBj-rbAxmd3FSq81fqwCYsZe-_826aJe2hzYDHIJVZPN5GkABCBDAiPtnL3eabWF4oBY1w_Z_0OsiH91UdAe1cmFNyfTF89t41peUMR9jiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5ww8_WuL8X9ZhffIX0cANU8Cql2x2M8EdHjpfp1PK1Lpormagvsmzkx_OKL2-m0SM3Oh00hE-XWkx5HL_1twwI7olFv4q3Fh7JH28bEcFTNtf0_5b-XZkOtpndhlrUY5aEbRCY_n_9qe4xiS20OzKMlruOWUCKe0IdfP2RQef0GfpV6vCY5hHT8rZ54zfuko9dOwmovbUKWJiC1HKVJESI-PFE8hVSEoUfmBzaNel7tCQ9z_5DaGFosWAAZkA_89eoCNWxhvW8QgafENkSMZZrZP0HZ5v7vqXUOO-XV_wbaB9PbuBv9zIhxTHWXmquwvqwub20bqYRsWpVwj7lHJDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5ww8_WuL8X9ZhffIX0cANU8Cql2x2M8EdHjpfp1PK1Lpormagvsmzkx_OKL2-m0SM3Oh00hE-XWkx5HL_1twwI7olFv4q3Fh7JH28bEcFTNtf0_5b-XZkOtpndhlrUY5aEbRCY_n_9qe4xiS20OzKMlruOWUCKe0IdfP2RQef0GfpV6vCY5hHT8rZ54zfuko9dOwmovbUKWJiC1HKVJESI-PFE8hVSEoUfmBzaNel7tCQ9z_5DaGFosWAAZkA_89eoCNWxhvW8QgafENkSMZZrZP0HZ5v7vqXUOO-XV_wbaB9PbuBv9zIhxTHWXmquwvqwub20bqYRsWpVwj7lHJDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tvUDSkJUYjFB9PUyVo4gQ9r1eCfgf3rzcFCsJ2fPssstAblgKdX8H7KWBdfUmjl2MrJNs076Tb2H9zcdkzNMhqLP9FTu0Qz-CAyvwMQb_RvezuXdtMUE1hmehazQhQrVd0qcaxpCJpdqCSrOaIPpuJ0nfbfyY_avBl0fs5dS4rZlx0kri8DSTTxXASvXFV3AO6-Q2QFOwjitr4uF0YgkHIxpIcvmo9y0jq48Yl21fxkY8g7cIh_IigdsMDz449oClfRY10fK-GTgjeLTtmhZHnwe0kqLWK5on06cd4pahObqKVgWEuym46s2WCdd_idFsI2MpMos7lHKqzWtB1ImjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zj9lCv7Pb5iqnQjoahkiqkhJrh6bYhJ7O_X0kyKrnSG6SsZhEH2WuPq0uMQIqn4yijbZTZxgy94sza67uhUq6zakvTM0rNz9UFLd2bE_NdQt2pD5p1xbjasr4pt4ozJdoO8aG6M5WxYcr3-UVmMMx_Zc_kCVBy67sP9dv8LaK8Os-feDr6i3kCKQ0ARnggROSfn4gVkEffHUR0KLkS1HnEsGju9gGu-NAPREsqTMR7CrOveGZu1cInCs0VAJGIt1KmID8fiwu6fP3SMfsfb61z0r7O_phtd1_qSg5m_D5Bd1UNcBk1dHjBdIu_YFm8354MUKrRzzDOiF9tvtctn2QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=C7gbFQ2YD_TLsXTSVg3v9EdemXR8-7XYWADR5lrFmb2B4zPb0pLuxw10MKMipijDcxL9cBBCGhvZzURXSKQ1h1z0kcK_FZq70651FLvnHDeeDQf4Fix-uQzcqNGEpMVPYed8me1p0ucBCkkz6gGpJeG8ObHE_uDLWLwYOLW0YUGfiIYxLL9wuac348V5I5xe2xWmFPF2lTMIGCzJrInarnVI3MFZqnKqF5lHg4SWVdqbpKK0O8uAkRlYu-URt4rWoe0YfRgZ7Ip9btayuZnPTWcPiPbnbE8EiJu1EzdYG2F6YqZbYyUrfnFbUm3gpDdrFPoe6y4YC_-xsVbuZXFpdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=C7gbFQ2YD_TLsXTSVg3v9EdemXR8-7XYWADR5lrFmb2B4zPb0pLuxw10MKMipijDcxL9cBBCGhvZzURXSKQ1h1z0kcK_FZq70651FLvnHDeeDQf4Fix-uQzcqNGEpMVPYed8me1p0ucBCkkz6gGpJeG8ObHE_uDLWLwYOLW0YUGfiIYxLL9wuac348V5I5xe2xWmFPF2lTMIGCzJrInarnVI3MFZqnKqF5lHg4SWVdqbpKK0O8uAkRlYu-URt4rWoe0YfRgZ7Ip9btayuZnPTWcPiPbnbE8EiJu1EzdYG2F6YqZbYyUrfnFbUm3gpDdrFPoe6y4YC_-xsVbuZXFpdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=R5Y3KVbdAwf4SviyRaiupe8bbSv24wzroSiSyWTgZCwPsO7OYRe-bw1kMKb492QDIRvRMvUsJIDpam-aUBCgF5DGDXTJw_ciL4xVdHIdf9S02iS-MR-9Nvff3dzS00weDhSON8srmfI0U1TvSbEx34R_A7nfxG5PkNIRj0nfmFv142A1PpFzz-WL44TzGC8e_0vWUV3B5hbcl2tfxoGqrWvnx-G7GSdd2G_9tb0-ynpfcd82jV8BGwUWYc5tEtNttWEjmsKE_m4Sc3k4XXpZrUU9LokljvAiNeVh2vNEz-Sp7vYCSWc07rBZg-NEYjsZ1dBYaky-u__bWTltEuj2Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=R5Y3KVbdAwf4SviyRaiupe8bbSv24wzroSiSyWTgZCwPsO7OYRe-bw1kMKb492QDIRvRMvUsJIDpam-aUBCgF5DGDXTJw_ciL4xVdHIdf9S02iS-MR-9Nvff3dzS00weDhSON8srmfI0U1TvSbEx34R_A7nfxG5PkNIRj0nfmFv142A1PpFzz-WL44TzGC8e_0vWUV3B5hbcl2tfxoGqrWvnx-G7GSdd2G_9tb0-ynpfcd82jV8BGwUWYc5tEtNttWEjmsKE_m4Sc3k4XXpZrUU9LokljvAiNeVh2vNEz-Sp7vYCSWc07rBZg-NEYjsZ1dBYaky-u__bWTltEuj2Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlteyvxI2ix7Cx--ztrGGGavjlxthFuoaKNxvMBEK9n9K-l-2hJyiBcJZVLYjEBmERZUeIIssRl73mEDTCD99gxOUcZZdZOI6xopHVE6oK8f4-V69kSNb5EF25UvRByZpxkMUUojTxIT8hu93x0tu1ptVWc69LIdPI8WdYXC22sMDTd-oVRHckajjawymVJINY6BY0pcirihLUeIDH8Xn1tMdERVYJQ07u1zjh7Stmpyzn9Q4ST4B87B5t2uDsTg4-NghhSlrbftgboP3mVNa8WxQe3Hj0H_yDl_ddZGa0tIchuqnABwM4kpMJjQAKFPV_zX_GcL4_sRw5vFFUyRcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjFHMZWhCmxx7t86GDZjS43Mx95RtZCGty3sQ0kNNJCaCs708ZRpLWl9hHfPeEIvAEId9Nr1_NUDt2I4sP97md6dfCj12G_Dss767zvgNprcToDgzrB9wqupRXSi9rLWN4VIS5utYH2kJfmsxeJV9gMoZ9Ltw2ssdNOwWQ4t9wKcm7P1EObsOyW5kbRN6geb2k6Y5VdwW36E1ixTFy-nNUm9YHlxO_NK72a0U-FhXfeQwr2_nbVxu_HNWprtw2jdcSRGiTrY5tfqksHG2LyispvpovxhZQASNW78274fN35GvtF1GjzLMh0e_MPBhm3Rp3IjeL4MHx4PbXNspWINXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=M0sLNTx8ocEaJ6zW4HxbyltDJw58FU97JVBArRyoj5VVY-u_NmbGOtkeLahBKwj-Q1K4LFeY8X-a5GWmz08rLIe5ILRvlWF60h20PukDOmnLaEHl-rHlb4VPFxEgBS1oisLLkWtA96zN8Xnv-_KkqAmoUPKcITEXyzBjZDREoe52xiUKlimBhuLHJKbvi3quyyOIcd1Y1XQ7SszxlZMsIcsOqx54xxLjvUsMUdQU4KFzhk3B0A821pomIDXPu5yrm6t0dFnbPl6O4QNzLxrkgc_5ubTpGp8A-WYDJU6AGck8vBiRG9F6CAq6nSGjF6EqvlfejhXOPq_--QIvamxd7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=M0sLNTx8ocEaJ6zW4HxbyltDJw58FU97JVBArRyoj5VVY-u_NmbGOtkeLahBKwj-Q1K4LFeY8X-a5GWmz08rLIe5ILRvlWF60h20PukDOmnLaEHl-rHlb4VPFxEgBS1oisLLkWtA96zN8Xnv-_KkqAmoUPKcITEXyzBjZDREoe52xiUKlimBhuLHJKbvi3quyyOIcd1Y1XQ7SszxlZMsIcsOqx54xxLjvUsMUdQU4KFzhk3B0A821pomIDXPu5yrm6t0dFnbPl6O4QNzLxrkgc_5ubTpGp8A-WYDJU6AGck8vBiRG9F6CAq6nSGjF6EqvlfejhXOPq_--QIvamxd7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=KXxy3aXXH94iZ3AowqlHVX_8W9p80NAxN0dKuE0eowzU24wgQm-KN2lxM8F0UrLV5F7-YkqCOqoigLsmkGuJXn-Tbqp5TUbqYYcTmeEu6duJAvW_6mG0KPOukApsQlcRTuBUI12g3conOrcqQu34OknLEAYLqruxP_7_gFIY3CfRwjhP82KayfHUOz7yscmFdYLK1G6yVbtqWLygGTGYOLZvJYOWIgt5uqMimvTgbjs8J9kCbjBmBuaJx0LNwMECIkM85MhyPwGvXAOQeMtNeZqNkOz31V9k0ky85tkEKBE5n-t2G0cq_uuhuiY54mHhcClFPHXVe9yuk4cbGCAC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=KXxy3aXXH94iZ3AowqlHVX_8W9p80NAxN0dKuE0eowzU24wgQm-KN2lxM8F0UrLV5F7-YkqCOqoigLsmkGuJXn-Tbqp5TUbqYYcTmeEu6duJAvW_6mG0KPOukApsQlcRTuBUI12g3conOrcqQu34OknLEAYLqruxP_7_gFIY3CfRwjhP82KayfHUOz7yscmFdYLK1G6yVbtqWLygGTGYOLZvJYOWIgt5uqMimvTgbjs8J9kCbjBmBuaJx0LNwMECIkM85MhyPwGvXAOQeMtNeZqNkOz31V9k0ky85tkEKBE5n-t2G0cq_uuhuiY54mHhcClFPHXVe9yuk4cbGCAC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERxK_oY94cD97D6-v2DCR-LqyXCxOh1ZL406QW84KliR21xfEk6HEqJ1o6OICvYeLzakpEYxEFDF_JjO1stXyYPP_VwWYxzeWDuXP5RRrcuGDPk-sJbEALnebAz4qQVXV2cuokJBoOkPjb5K4YxWHFoZTCqvaEx_Mea8DNVHTnUHBxdb_5PCQFtkUHP6UpdX1GIlvtksiCI1bJ_zeOiVxYxWrWYvuvSf4n4SJM4MvxFzXihKDbYRj62Tso-QPbC7CUdMGmrAaFRTaZqlyRKtRYksLy1KdRMleUoAaKVb-vANlrpi0PwVHcOpNmPVr2mODNW9zCPEkfVzdlZ9uzJYzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKN_UZ6EWNZPXgfLOgFAmpBYUYglIeMtXUFeNpWbslSC8uBQuPAVPRbSHoX7262AkOXrNvfGAHlaKbCtQqgmNxwbBNoW-Ag9GJATSCnYqGUlyjdR5QuivbmfXCdZ5bSMFi58_sCo4wOO47Dq0LfEbFSAoOD6WyXnTNdqrhC1cOox1faem_XBmYM2ea1o09HWl7wjQi4gvz-bH9a7blkh2GfPOb9lZIz80qH2KKH6FFQZ52j3mdw802hfrN_l35hjK2xjc-Relpp9zjWePM976oOxJpwycaExv2YddirrvAykJGHIuKmD7br1-j78Kr5dvC8uXryFeUvx1nJVqTVoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saeuHjSzEayxmD7AkQKZpdx8I3h3m3FN-GWJvLfnqoCa95fzDps3mZe9kJryRLToK3yGJ-ERfrujDXdaoq9wqcAMmO9t0BPFDt82gx0Sg5wkQxgRdscj2Ovw2pDoHCqGuSzNFIeGXCIV_vnIvgTSDH1iKHmQPIz7QrjJV2wFlU3GPgzmFv0NelcxvyH-SJs0-LO_LK-1OFS9QVieNohKvj2pAFPAp0oewOarhw7j3sFqDdb9b6liZrPQ4Cl85oOma5VLTdIpwpx6RkLlI-G4Lkdktf7ZOW2BGAzeC2XiR1MI-2tuzcV4l56gmQdly2ZiMO1_0vs3hahAqWscoxq37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWg5ipl0ttlQ817Ndi6-f4UR35d-phP9IHn5_hma-fX3LBMrEtBTfUbmVL3jkM_wGqS6KOk2h3yxevS6Y__fILRiqoE6-AfdYj6qMgjd_dLKVQ5HnJq1RMVI_Q__lt7NuACyl6attiaTrvBrhvoZ_x80GzEUTguvhTZ3iDQ18VFLvCOyKNrua5LreXEi3iM9gNM3AYrABcVC-6QO8GzTVuPVykDbAPqnrsagzwXN9VGUuxSMo2busOYwAIDXjwbpSwT774LSzHyJiplogERPLKdelnrswi_rI7EDzA6OpgKeKMliWSZM0dYZcXV3S0LjXVXbWYMdGolCGly2GKwZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJo2F8fqJA3LVRR5V2rKM2cwRx5zX_diDOn7vOqgLTcPXyRbZfVNkzGW_fjc4P2k0F1P7MpGGZ325I9ROygNTO1EgfTQOgmJ6uN0gRli7PrqAhCMZlT7iVPbq8EjQppXpcejYs7IRlZgHlmwn84iD3ioxw2mNUW933q1yMChMCJWN3E4TziCzRwK-k0jUwfjhxja9vHAP4mtFtIuEosNc91Qd0DQpr_Q0wBl4FqSgNsf4_olhJR1sRBUGwjWqKBlqCPCSkTNNAZO5_UtvYTgxc7q7rAWzRf38trXFlNM3JdioUZr9Au2oSwxuen_71idgy-1tQr7mzdTOFUssMefXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qAcEadzzv-VUP50Mm0QKTJXcRGwfG04l0EkAwx3b9CX1KUaOL01kBiTwhsEhwZw-RS2YwRRqxauRB2LMYt0r9VeEla7UcfsscM6y1KOhYBjkPYWMPXzh1o889UwYhUX9l-FRXHpRr2Z4gQAJgeNRCtbDGmnDpLQxed7bfP2Gs74GM0anUh9EqGP_a72vlBWfwvz1nMGP3mkvsxNfLxwgrh0EPtzA6zVkek_KyIzo6rmVrwKjx08VbzjlLiNRcIXii6DSIWLwtuTBoBMiHPFcJJZv788YpxaJ5yq8IUduNRtM4Gz8MKJGwPlgF5d57t2mqET7sgeAKsYOasNQnADR5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2PnWKZ1rcYJ1ar2ix7ISO0obH7tHqpN5tGzlWd05kxyXpm-tiQ65fHnX111xnvO1TRIwLN0vIqdTTfPpXj9s3VrXY5Vzzlz9sJ8oeuABNokziG9yYCfyz31fb-TvJ_VmbyFqqbv1xl_fZodLMxynRhsaFpE_YtFJmN8OpT-bhGpAk9jiLYMkkA449Z5XB5mtEKR8vFgVfE93yVJOqgG4UW2JwZW74g3zqINTPoYjJAvxyaFRhzyVpNKTtJtMhqJl7R4KzT5gmwqlVNydhhnWD1dg8fUgoMHsYaGS1sbPpYbfl-Zewb0bCq0UTSc2aAeozw8JFcDbyHadBERu-pLgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzLSZLxyab1K0mQhHK7w4VArkTcU__p5nMVPoDD2UUIGnZDdntes5G--rxo1lYPeS8dmE0X7fPaZuD6-d3bSgMb8a3dNLMxwSvxsIIfUFcZS6fkLT77CSUy7LpikWnw7Ts9EAov8QeSJAo8HhTE3ZJ_6zF71wyRjiBIIaZmV_eUMLtFtXufwhPzmMJg7aFFs_fA5uaFxDCwWquNCKNK9vsOUpbShS6UwTXVOqIdzEAuZhZns6qTmaYXArLCtbsFbxCQ-pecrT0L6-3pxwZhJ7k_ulhGwCj32umSSRcaLfGFfdyR7d6Tiy0DRYf4y9Mwf1yCYChNivYB086U2uLxyCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P43yZacGupG8A0xiXaOhD99-a1qdJFNht_jLdvKdUstzv5ZGswy1XjfPYW78IH6o3L38mVQZ5m0EfGqHdTY8NbyLBKPCjb8paqH1_SQGfnJmyjTFYuBahOhxGTVBoBPTNvciaXVaAJ_qI_vW_f9L_DP6oT1RfQws2A3nftoatrEspBTuVRYfENxBcXkpEL380tAh9yzK_M4hFhCm1eBBxNqSlBboHj8sS8J4MRonaHZjRIEVizRKHzi6zILtgAkIpSCh0HNddwtdef_loRJc0ZJwROc_dDkkZZGK4ESliltY9a00yDOQtrZAxSjqcbdfxhcSecYjTU6XzDu9m1-rJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLKCj7cfSJcoZoh8QK1xIEg0UxiWHoxX1FbtaE-2Tee-82-4Ugt1dNHrwfo-3cHAU17Drze8loBBUAN5KGnxZOXlhnv1IcPgKiSqvMqcCd3Y1KG_5Rnyd7SkoFWnvb3EUPVEd9NVkQnF4bLzKKrR3x53QGBUzawFDmR7ZYKrjNP8s__7IGYtJAE85SkOATU8M8Qyg9VUqEikk-KjvNQdJZQVt4_zuqx8R6Jnh_V6SK6EYkIHFNw-wItBYCDliMK6TFTrBDUw9SwlyX9vxE5LtEzz9TWZ_GZJgT-Zl1NOKnFYhQG-UH4tj9K-fUUtBgdnlEDFBmjDQ3Js3yC-9FwlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=jqM1hBaSctJ0lkdpE-8ToxgFG6rBlr5P748vyZ5fXISjS-GiTnlQWTyOjYwVdElWhuvoP2hKgViV9lMAH7HxOwSjGkdsmsPEl2QXR9ABeZdh1v79IaWBLjbw3X0wdR8BOrt8kf_KhB0kjxGQQgb3T1a-FgxGgIrMJjFUYNu_mVrFVly7upucQzC4GirFjBPavXfjv9_RtBzwiZInUKP42ixlKmI39tnrdTQoLB3t4Iih0IfqGGzvlVO6uEGQ9B3KW-6wOu7lVqG5s8LRYykxhhvulj7a8Sn-BblKDW-Seg9uQ9nXTuUifSITHI4HJsDM2AzwPzOo4S4pbb_mTfuTsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=jqM1hBaSctJ0lkdpE-8ToxgFG6rBlr5P748vyZ5fXISjS-GiTnlQWTyOjYwVdElWhuvoP2hKgViV9lMAH7HxOwSjGkdsmsPEl2QXR9ABeZdh1v79IaWBLjbw3X0wdR8BOrt8kf_KhB0kjxGQQgb3T1a-FgxGgIrMJjFUYNu_mVrFVly7upucQzC4GirFjBPavXfjv9_RtBzwiZInUKP42ixlKmI39tnrdTQoLB3t4Iih0IfqGGzvlVO6uEGQ9B3KW-6wOu7lVqG5s8LRYykxhhvulj7a8Sn-BblKDW-Seg9uQ9nXTuUifSITHI4HJsDM2AzwPzOo4S4pbb_mTfuTsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=muAFvJnEF9JzFfAF8PF9RedBOps_mg5B7mHfMgfAIGQYaDv5INX4j3B34P1U9ESHA4qpSDou89wZrYwW21-D7xNSZO09_-0Q6pffdN9VCavjHojJYHiXL6K1FH0vYT0UCFaxseeSPiLIPppiWR70t2eCmt73AlzSnQnhHzF2-dxy-MW37oerhe9LaR7jsBWPOpocxUGhoC4i8BvMhOtkVOVFrl43JWnWwZ7HpwnOrKBcb37s_DfuJSWaK-qpksJvOHr3WWoN8ILCaNslD_1vBwmz_Zn3Rg9RQOqpCZWsA3NOPl99WFavyJokfKL7QrwJdUk5DU5tLXNmvsBiIAeX8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=muAFvJnEF9JzFfAF8PF9RedBOps_mg5B7mHfMgfAIGQYaDv5INX4j3B34P1U9ESHA4qpSDou89wZrYwW21-D7xNSZO09_-0Q6pffdN9VCavjHojJYHiXL6K1FH0vYT0UCFaxseeSPiLIPppiWR70t2eCmt73AlzSnQnhHzF2-dxy-MW37oerhe9LaR7jsBWPOpocxUGhoC4i8BvMhOtkVOVFrl43JWnWwZ7HpwnOrKBcb37s_DfuJSWaK-qpksJvOHr3WWoN8ILCaNslD_1vBwmz_Zn3Rg9RQOqpCZWsA3NOPl99WFavyJokfKL7QrwJdUk5DU5tLXNmvsBiIAeX8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=itUM0mWSiERA6aYVRjyABLT7Vpu6PfSLoC2-CSwrU3vbZibQLShROIAfi19ev_x3CM9G4cN3CGouWfkYSwchxphNrOsjK0d_tZ23m-FQkw2_3eyn1HmTdELk2kKzCZELCHzCeRFMHSCy7unMFYRw2pwb0B5Z_0SIOvwSlNtuGEhqmK3hZZytvR29WqEIwTwXahIH0MWXAcVjs-kaHgERDW1cgBKm3V0bkmPXeLxnB5zaJ8zPQLIndW_1tkfBFFuYVwERroZ6aS1WfPa7_oVD7V8JzWKaw0TnxBz9-gi36ym88xt3jVS2Ou9RQMxrnUWC_O138TQWlHNdSxbdWZA_twNJ7SlSKD4wPwjef1Vo1C_cfkQRwJk2sR6G9dW1kb0gpf82AaZknMkUoQnWoGFQnLF5LTwDVMsuunJ9iaBiLmhiVrurBPPm8sAA1mtfzt6qhEMR4kXIjgSsqmEjVkJV1TBk2FB78SK2p4ObFKxhbu-oI3Bco-GG3co-FmBj9r3OSbC7wK96qPt3MdHWiLMJF81fdlWoweL7PotyzPhhCESABPuvKuTn5RCS5ogYLvsCSSjzxTUtxBAhewSUB_XSh4uSVwXq7RsTCN6i_yE4QBlvNRF_kwl3HwZyu2jYIu8_Z9PuBmghFcL92rHzvS14GdZwqf5oWNbvIDI92hIyL7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=itUM0mWSiERA6aYVRjyABLT7Vpu6PfSLoC2-CSwrU3vbZibQLShROIAfi19ev_x3CM9G4cN3CGouWfkYSwchxphNrOsjK0d_tZ23m-FQkw2_3eyn1HmTdELk2kKzCZELCHzCeRFMHSCy7unMFYRw2pwb0B5Z_0SIOvwSlNtuGEhqmK3hZZytvR29WqEIwTwXahIH0MWXAcVjs-kaHgERDW1cgBKm3V0bkmPXeLxnB5zaJ8zPQLIndW_1tkfBFFuYVwERroZ6aS1WfPa7_oVD7V8JzWKaw0TnxBz9-gi36ym88xt3jVS2Ou9RQMxrnUWC_O138TQWlHNdSxbdWZA_twNJ7SlSKD4wPwjef1Vo1C_cfkQRwJk2sR6G9dW1kb0gpf82AaZknMkUoQnWoGFQnLF5LTwDVMsuunJ9iaBiLmhiVrurBPPm8sAA1mtfzt6qhEMR4kXIjgSsqmEjVkJV1TBk2FB78SK2p4ObFKxhbu-oI3Bco-GG3co-FmBj9r3OSbC7wK96qPt3MdHWiLMJF81fdlWoweL7PotyzPhhCESABPuvKuTn5RCS5ogYLvsCSSjzxTUtxBAhewSUB_XSh4uSVwXq7RsTCN6i_yE4QBlvNRF_kwl3HwZyu2jYIu8_Z9PuBmghFcL92rHzvS14GdZwqf5oWNbvIDI92hIyL7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf3xsCzunDH5OORvgrqI0DnmP8MT0yUVJPBRGIbAQVSu9Yuu7AFHRBzwLF3eeOEg8vm9wFoVvYWERfscWuphFbVYPNaBHox8agsGwoH0AWTjS-KqH_VfHXdvpC4czUUifw81uG26TkppZqKBpOS9HWVN-6Z_j22oHua9EXhCtqVwYJlgSd9fF_HYoQL2auNq1sggaRu_QI-pN9DYGRSNFk2ELRGXFEwKel9Ks1tUdtZvMj6PXOd2wWlfc1SG1Z_pxvnmll3YB9TPLxZRFfTfKt9qnSzL-EnHknE4LoLyw_FEMXB-qUwhH1zO_iPJqGz1xY_QFMX0AM_OoYcMog93gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bq0uD16qT1kLZ0PKNEY8jFgnpBIGFl7c8C76JmgRBo24R5DQFDMhezSmkvm6TaPHFyCtBiNOj4CDXq7aI4OwvSE9IlKB8WmytWZTSa7b5-jTGmwN9zAVIozPTUoACENtt8rtk7h40D385a3Hj5YvgMjkWdpGDuxRiDSilSzraj62IxRuY9wzwWNUZ2s7WLoctg9Dem7XFxLDEm6zR3I1NC0Kqgal10xkE9SAQY5Yxd6HGV2a_ZEvsMV1pDPpgnkwUW-OucvFLEc6A33TgoiijgDM4Sx50ZZZJRhfP0AwywMJoRTkpxqewah1TIkOhNOGZ9lYdf12FaGpA2kN7PwDVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bq0uD16qT1kLZ0PKNEY8jFgnpBIGFl7c8C76JmgRBo24R5DQFDMhezSmkvm6TaPHFyCtBiNOj4CDXq7aI4OwvSE9IlKB8WmytWZTSa7b5-jTGmwN9zAVIozPTUoACENtt8rtk7h40D385a3Hj5YvgMjkWdpGDuxRiDSilSzraj62IxRuY9wzwWNUZ2s7WLoctg9Dem7XFxLDEm6zR3I1NC0Kqgal10xkE9SAQY5Yxd6HGV2a_ZEvsMV1pDPpgnkwUW-OucvFLEc6A33TgoiijgDM4Sx50ZZZJRhfP0AwywMJoRTkpxqewah1TIkOhNOGZ9lYdf12FaGpA2kN7PwDVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsEm3lh24j4ayh6H4ahcy58g9WqljgGE0L2APCttaTxsuRs_D6_Pj7jKXmaBtQWJwW6vQrAApGhspPlOU9FfXP-81ppSD2_hvW7_T48VDZfy80xO-J3XjbtOUUFsui627THeXaIUWv0XtZ4_3qAnAg1NVybsPzJy8IlZAeMhsnTkuooLHHJvJGeXWeu1fK1hBmfiQjrsFUDaP8Z48ZRW96RTVV0hSnjQ2Stv9qiqaaJXOMgGRD8Odb4_3jAAiEKxmvSHQy-TBKmPoJTUcQOoEFqTfg4RcgjivuLBm5rJupEg0I2zGYvQR-tWcLx5itPqHGB3DWgxllcsMfiT1ZchVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaG3J9mIjccI8xBJlUdzumeI0683Ezp3cLr87DNOlPIpnZC4qV9ARPe0aDpx8OIxI1SXqtk1Yp5uuffec-baYamxI0Ru4_eyBReQ51DZOLFU7l-86Hz-D0CPwB7Jb3gKEy47IdPzNAauHpe-vheDVW5Gn3womSuVXY09otuU_lqJi6PTcPIyBkAopEQi_aHNa611cpNjjcbH2LGJI65m2ogMPzhBc29Xc_69Kjo1BBtrOsmwQ6cjKxC9tkzhqppUmXTbBeQp54RbMn8iN5EwQZRm1IiLygDGvOZRpJJadTmFCGQk4WeHa8_wOVahF6Mhb4KZBuwpGGbqHJd9cxbgEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACiYYQ3VAIFAIQfBE23aPp9lLZb8KjN3vCdnxsw8QnAymx_yklw-Dlw8DbQVNUuwnSFYrhOzWXf5K4EMsAwY3MZOHP6VRZofBA0noxWbTtimK5d7sIvOPyGwgzdVFci_ncheUoCK08LePBOd7B50cy2rIz2v2hiT4whB_oqUmilHjCGAMaHdnnFdgKjDrWXkTFvC_X7wGDsEUrEb55BqzpAL7IUyUy5xaqR6hPXLbH9BpJL-qB-Y5dqCMUvoC5W460BUGNpqigp8-gZkx-33bJblmx9T3LfDuj0U0l06O6V_Edcrf8W_BOMIFtaCKojrelg5DqWk1FQDUL7lSFPXFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PutZKpsltOdV0fumWq8Cr1gE7Z9T_emrm4cA1X5cfh2KnvA5cpAPVF4RJ8wup8O_L3orXWmhm0xFOslZnpFl9Q59thkO9Ke8QfiEvdzG6vfo1tYAf39j7_06RlecmgMJiOZP_P_cXFmZnJCrh4dBboFC3rFcLwylzJ0MD8jiLaE29qoG_QYUZqjlyAGHbBIwlgarQOZxgZQfZJX863LJeMNvB8ESh_EAVmqSlx-ZyqEHDWKu6KmEN0C4LTOj38sZ2-m62QI5uchJyVsIGcfH9vHfzIry6s6MmpoZi-u2JsaC8HswgZ_h0JMSPtLS2E9vdQZr-2AN5kPUGUeMJREitg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nLidTW43-eIbfA7kG-wNsEqkAmxU0ngQmBVt0mGptdrmGu-kHkeLpX8csFRj3IgWbDVMHDLD4fHX0DWB-mD2F7NEFG48NWo3P7-Cw4kD9kfYo1zV9nnG4fxt_8BLfx6sc_u0OIbiFieDoe2WJxwRONFyVs-V0j81nmIwx7GRQAqwG2My-bro8upF5foV1Y2ebJdHJ3KyOrbXoZ0YXpoN_WD4HsWh0JxseuACWuKHQv_VbSiObvy-CRdy5nyktTGuYhhW5tur0HRJjpUDczkxBrejmmJy07dyi8UZbOZqdIWdhHbLsuZ3rDSFC1A4mf0mrje-j0xrtrQFAnT3hAf4ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6f7oaB1jHImIjuUOzey_ZBK3u7qrvPHvwfHcho0Q7kkaL5ZFdaJAMHwRYiWjMSOetJRDBMclaK8RQWVIrQ7_6uN6ZIzVKDn0AsxibMsbjm2-clb6mHYH6uUtVQEXf2JybrvxNt9z7TVo72wtrzVXba_waLgrcQfmwq1D3rF8NOwh9EwuLrSv60Oi2beYzwC7Em4Vp2qg6mKE1l9c6sg94xPi2tHZZofrnO5L-cLxyBQMRFovgAbkaGNwSLrdYQrZj4LzOV_mucDRpFYjwtGbRwj7q-se_8ch0RVEj2CI1C2S_wifREm1PyG6PUIP0KBkihDDQJl8AJCmJPHlyEYxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v6khuCE-3cyGijljFlwd0RvZnsXdkld_cQkaP3V8VOrcbwfWQcIEVmLXUqwT2KDY4J-x4l0crd7YdbrPhS_Pr_JWAl8M4eVJQhMRTngwjlsQcKMVKS-pCheeAmXjA04DJGZuYCoBL0-KCPEXEzr2tmp5WPQAIr8WTu7ZU89BrPb4WKLIV8nzrVQyk-G2wnMSa7GGkcVoJxfrGO2YH_Zm1ugPBBqu_r4HSqNI2oDPjaae69Y_FgYUx_z7G4eeSmPaHB3yVz8Jrhx74sRNDxXrFW6LXu5B682jA6BXPxy0t-KdNSzD1DAelEcteby18qHp-SF_AJZLkFV1J75_G4QzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-lTm0CaA3RqjLagguYJHgvfkaeeWj7dsJwim4GP75OdQmv8FeIN8SxOPyA02z-roUH0XhI1OeqY6Tz7_Wr-9t-rj91fBmIpDH4D73yA_k2dN_yfkLFXZu8Giko7GBIcwpGWQjMm8MzRTI-C-wnpz7vLRTlLygOW-rE_uaxEPEPJQRM5wX2h7NrOmP2n5pXL1ErEECDMbpNdlz279VHt-ainMjbx3lK-03TmGid8roEiSOfvZ42MDas0u2SxJfQ5atHbyd-NsmSypQLT5Z5wzF60yIoSAdfwWVfXWdBYcEpwzQ7OTUHSCAnuW-wU4pTV6-NSmEblkT3xjI13PK-9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGlolifG52MP_JaZxQYezWp_Y3bORSsvCWkXfSRDJeRebypuhgvEWG4Vim8ZcqZ-72oJhK9FOlF6cp-EYhGyp5mMm1VxBN30RFcCPbDWdBqWJ0azKXFoLvudd0l9I4CrjcbUoDOX--eBbIe6HLiV21J9gAHLS5PE2PuArYlYX0j-wepG-SF0ZBBKqozXzgcc1zQ8Q223YczgL7fBd-tlTPzwO0JKt5fM4JEdstq3S86jNXV373yEx1iRmszyK3ZSArdtte2dd9lAb--UXjI5Z6qAWLZInFvlk4-5Pzanut5yfHgX9YbpmfxEL2odmmFlhXBCv44RcWQPOROxd1quwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxHQY4q-ugKHDR2PFSa5g1Gew_cbaZ4sP8lgKy33E1Gkl1Qr8bzCYFRwgbC0742wZpC3rJ7Vt1ZRZNt-oIrOZ3TMcTRLHgqgDb9u8t70eLyota1ExFME9RZ3vtB3mPczaWLte-WKJovrKl0dh7XDQaw6AGXhJjM9WIuS_UwR-4RPz2OXfxuot6h2BY-IyIfuypGuffGZgmWkpykIbcWVW5yN1pWV7M14etFFf73_vbxJAbSks0II-T_z3BFGjTUY-SMwrw3cFMEED6BmcgtarX7n7BRrUtAhscCt07RRkANFKdMoqgnxK_Nq-gHIudPFu8BEKvFLxj9cpC0oHgW-Tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npUmltYjp2cxo5vMf6cLJLj48hUBpEHBw0Xi2falxxhrViHuFNq7VdA4lM_-TfyXHQvzEyq3Kgs6iLQXk8QWcdiY2qZcjpxNpf1D2NXxVheI_72jHqWLRQ9vP2lJfPHTn-ShdgHKBF8yQUko7xSMh6_-swAd3a4INkfUcicvvjUFJAFH714PrtDj2LOEMbeYOrAJG38_LtSU2FXVJsIB3wvTPmO3KNQBGmgBMTyru89IIqRgiD1UtLEUCsn2KcoU9LAbkxUlQ1W7uK-QekCM2xNP5I8d3y0YnqXrMfVeVM0zZD5KYSxFdXKwsCB1LfCv3dmUf_hBP1zEAAolYCqNgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhhH2pVPIJnN8cRERV8vhgw9KgDDkRyUeWxtCBW5lJzIIT1wgu895D3vB-Clxh_UQ9Q2b5GzC2iBGRJACA-G6KFh55INW7n3u_i6JlhKlHUobLO8uZexUmZvZTrMvUFiJzjR5DNIv6urNn0c7eFCpl8I1Rtyi2ZOtXTi78iQ6Di6diJYOGRAqRadqi0e_u9w5Ky4sNYnL79OGkjivLGgrWXC_BwzGwiao26QZwPsl1CI8o3lhkqdYu8mtpNzTBJ80OYtnkvpmtYGO_50ASQMI-17BHNwaUILm9XvXYiDGa1zQnvpcLXBawXhv_BnHnZbbWKhqQ9YtAJIaOX_WYm2HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4cwHh_5PANk0KBtNF3iO7omJ7rF2fyUL1MLzv0Ojt4xQkIW2-TbHC7ifa0PFVS7btlqD0W50oEYPorxFei_mNUMJxsyQrT0t8oG9W8E1GVxdgCBHm1IXtbO4YEDP0F1m2_F8K-XpI1qUKqOGijiAjNVmJSbmgcq2zg511r0jnKeOywYQgxVX5cffECC0JwQdE6QuglShZKCBuxWswF1Fb0Rkd4NnqBYPQPjXMDyVU9ry9oxWi2gUCRnmLjdvRuGl45b9VXiODYOZO6VHYy2WyruzUh04If3EwB7GtnwUQh2eCk1gJq43nHsUQ60IPLoEwKMFt_IccRPo2WnDjkNXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXLCRkNwExMhynrA_NBMS4w-jub6R4oDyKqnqjYybf4ks8hYP5_6jIha8ctkUz4TNyP6vB-zb9EFeN7YKhd6wU9z1_TnuuQndD3N2gY9gdnrXUtCU-VWYDvQvIr6I09a1_p-QBTrPLzailp9Q4TgED8bKB9qqLeQ0RcgMWVfBmzQXs1jh2Vng0aKxtynyGygP5aRZ7E3xLQ6sEeK-Vii7WiPAP3MM0Aklfp3L2rd6Oyz9LXUuW5H5DlL9RCDCrMx5Cvc6k6nhGGFcqYqn2ev11uGmPgorgNeJeeUM1YDj7fKFXE-wdATgZTvp-GZg__lvw-ltXWpsh3rSWktCKM0yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZT_T9PK22y-5Y7dSjpVmP9qF42zmDGkL3FTCTqEwl7aEDtr7vyrrDgmtF2yBQFds5RGGeh7xa41P7opRFiLF6PF84RhqtTOjKl5IcFmBBI4gOTyDzhRkbUE66dFKrb3mv_l5i695eB4g_7o23P65g8eJUqx9a67GDAUk488T7xWtoUF2_JHcLchRVOCK2TPOQ9xQ_br0aNmDKA7w8cQX01nS2rihNlvxy6JXEQjR6t6-R_sN5j5tfHeJbI2mwV5WONbMjA4jdV8ljvCukNtt4-rEwrMtxNnL5utVuus7BdpXw0t1JvMs77Q4kRxME9edX05vo59WgY920P70dYMrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rxm4Z8PI4I-iZfbRmSPVNVxjxGq4pvHanjzwu3QYQNoOl3GnC0GnlMAqjTRtCuXN_yK4XGFpD2w4k0ygSTkB15OZ_Rnegzm3Pk39CmUWFsHdqLatRameiD-uZe4uxAEFe6fqPpwJuQ8ddEHtDlca64gkdnLbwLGrWyNCp_z1s1J8bI6v_9xsKZIMqihDMoD-lckJ3RCRP3qTZCgr6MJGVOH7n3a4BIa9buKwRuHeVTwc2vpmSkYC49Lj-uKflD9V1UdhANNz-wyNfgGtQfKgqXdCWbhpdJ58zcSJGY7zwWTcWgysXKJ4qYfx46LFlriDsflbZXJWIn9xg6pRQcaXiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4OT9rHVKrYtDLVB7_sFIROT7D9LTu6fqXbrmi7tSQHyw5MsSBfcuVUU_Umx26fsLOrwLn3kQs3PLCH8n-Y1vNkx0Zk543D9uhqQhIIcyEHuoYD-GinDxgeVAMDclc1KujyLNO0_zWDZ8iZxZqWMeHecVAforw8564wvdp591SOmes5xMWjBx4ExLQfFLUggNhH2fHQNtv8rLmAmhVyZ06yWDpSckazNDQPKrIvPpeZXEB8HCuyElh0EqM1Z89epu5_uFQre_u2hb2nuHRJEvU866Uj2H9xCFIdWkzj_LfxwZAdAG-bRq32WYBeGRd8eK4waD1tRTDeBmGp5FWVH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=DmR3QgWbRMB42cp7PU3PktIrXDWfjcD7CbraOodCpXqgM0QE2zBNUjEG2vy1hFf60GRisqoi4BOk-87sG5OM6OuOHyMVnw_mzc6778z40p_ugDCMrpCNXL3IDL6ktj74kdUACAmjsuE6xCTEpIO6yCNnYGEVFLKClywYwobR3BNd59T92fLdekVaVd106YAa34bdRFbyk1kvPommZX83xzf6lKVQqwyulv_EjNze_fteh6Mta9tJkNM_PnDAuYle2DIDSI2WXWxUS9I75CNYb6YbFjMs0Ro4BVyN9h7ojgRjt4tCb23wx9lTe2LcH5z0wBMzjlwN1MYi7bcXR2HiEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=DmR3QgWbRMB42cp7PU3PktIrXDWfjcD7CbraOodCpXqgM0QE2zBNUjEG2vy1hFf60GRisqoi4BOk-87sG5OM6OuOHyMVnw_mzc6778z40p_ugDCMrpCNXL3IDL6ktj74kdUACAmjsuE6xCTEpIO6yCNnYGEVFLKClywYwobR3BNd59T92fLdekVaVd106YAa34bdRFbyk1kvPommZX83xzf6lKVQqwyulv_EjNze_fteh6Mta9tJkNM_PnDAuYle2DIDSI2WXWxUS9I75CNYb6YbFjMs0Ro4BVyN9h7ojgRjt4tCb23wx9lTe2LcH5z0wBMzjlwN1MYi7bcXR2HiEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUX45NImIv72NxMrKkJy76SubDnD2oeR97xtCZAp5h8zZ0lI08f5dkqeUR8plInUitPR6RCiBq-vjxEINYBnODUhDScXZS-u4LWqhsc_xT3rPZodZ-65CiniYMoLNsSfFfijxqdOhqK6zoPQasy8qfdMyEIU76DFueWUeqopAYWyCsZCPEhexvPr93zd2jnwnMbce35GZvK5AUHfQl7fkUKQBeg4WJR6gxrAAngTmrNzDp8oEJoTRnXw3IZHTldaKoGp3G0-oTu6n40DyJziF_CUPXzC_VkCBoYizbmlv6TLGMQ8N-VXt9Fp5Qlqi0icm1Z1feI6FJjvYWXB5hd34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_UvQJTxDJYc5Hj4CxhqEn4eKuLrIGUBiUlsMea8X71ocqg83YkZ43hEjrO6HpPxj0lKb-7_uzMs7AVJnE_gh0qltUbq-5h_MradmwEHtkVVBprm4Sw66Gakk0IvbDLTpFI7IQHlW5hBBvcM0m2UwN7TnjdHObh3nHd2ZpSj8YOAFir3fhWdrY9HZY7XN63NaLtyEvVHBTq_ZaNIDZpDOuEDfsv-TBaxRHTYG0caEN4O1plpY58wpR6ErZ6XolpR8yQwtwDLx4vvCpPmS_y5VQs38IAM-9Vt4ywdF9UGF4KvyEIujeRbj7Tc8TwHktOGoR_CNr6wVzIM_Me3bP3CUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SH2X_0WOPoK7aPLgcVbBkHk0rmIjnUz0h_xpERPNsh7Z5daMHzCe5FqehIuOUa-FIWf0PVcCam7QRnbTqQlsbNlersdCFqCAGERxNLIVEJQrsaP7I_iS1XRsyZ8uO_owxBEU8JbW5_iBb7LYMIgO_J-P-Oj3OGZ9bt1jkEdYoxcHlGdeyr1vTsYVADzgNbYrUTHbL1GnUTf3ThdqtDncbVW0T3shsFzAwIjAODW7PjuwiiulLLsGb5GT-oaWVHmG7xJlS9JEAyBjEmWNoRmV0DCMGsTKgevbcn5wvyJ1U4jg6dywGCetXhAaZSV8qbhOezlxj7dRr1hyxojt5faX0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=ahilsOBDVMMzYZwEj0L_sWHw-QPS5D0GOZnWwqS5qfmExR8vn85ULcR6rmsh4JYgcl78o5V9gWU1LUgCW024zgpUluf7rJt9p-f7A7H9hFKMD5pX0e4SIfjTA7_Euh-HEIlTi6CTBHVcouqim5aYd5ij3qsTHShcZxrDHSyxzGVCUm_kup2LRhhBhgwOufyDQc-oqkuZLkhwpllzFpk-obB-kCdoxbUycILOm9SAw12ng4SocBYEU_nrK29leDdxTVomAiEpUy_amRPIoz6Sxq2zDVJ3kCooy58nadxtMxm2zYk4dzpqaOf1a5vLM-bIkcCTYKrYnFoxH0mskHJbaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=ahilsOBDVMMzYZwEj0L_sWHw-QPS5D0GOZnWwqS5qfmExR8vn85ULcR6rmsh4JYgcl78o5V9gWU1LUgCW024zgpUluf7rJt9p-f7A7H9hFKMD5pX0e4SIfjTA7_Euh-HEIlTi6CTBHVcouqim5aYd5ij3qsTHShcZxrDHSyxzGVCUm_kup2LRhhBhgwOufyDQc-oqkuZLkhwpllzFpk-obB-kCdoxbUycILOm9SAw12ng4SocBYEU_nrK29leDdxTVomAiEpUy_amRPIoz6Sxq2zDVJ3kCooy58nadxtMxm2zYk4dzpqaOf1a5vLM-bIkcCTYKrYnFoxH0mskHJbaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8MyR6GpnX1q5qDLQpNloLwbZi584ZvZLtvP_86o37W3OtjfWA4SkCjeWbl8BjqWMaVzRiE3ljxI589coXKyxrYpiphqLVx0_qN3mTKSCEXnR64xZj0cAyByQVggEvoGqK_4ob5F6oKBJRxvduBB5sSO9bHBpdgZSYIskbzv7Jk_VVWxK1RJEydkw6ieNgcMeit5WFgzYpW5vVwtRwS7VieLla9o0azL4b6S48QHo5yyysc1pMNUewM2bMz6yzqlva2RbSA0LXQI5hoVoFrjdZixPSAs4AkVM_Op9oPpxCizGSWtVZZvpR-lRwPndANFb1PzJsaX7WhfZQfU_hfbXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=pqKKMr9apj3QZGnf6ejWtJC_vfbxbBbW2Jk52Suj9BXBJvbp9kvIfi6k0SGci73Stu027Wr4488FBeEUXU9BMMRyNzgS9L3bl-AP3ZKqh3Jh1Y7iq9H9iy7WnGv3h6pXbmcoul6NW3lgP5jTes7A-qI8o1TXuJFnHtzk0TRXa7HIqgnQiqhGXN60wNORm-DOgzVvoQwN7tD2frnhvvukeLnxWZXv_SXNSX-u_uAKmT_PxfzoI1ebSPcj7nwTrginMTzX-canN1euO7kg5jUYSW8i55tofiO-8xpLnpR-fYnSLtiGYLPhD75gB9VjufjeJXCpDzAStfZ_tnPrR1e1ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=pqKKMr9apj3QZGnf6ejWtJC_vfbxbBbW2Jk52Suj9BXBJvbp9kvIfi6k0SGci73Stu027Wr4488FBeEUXU9BMMRyNzgS9L3bl-AP3ZKqh3Jh1Y7iq9H9iy7WnGv3h6pXbmcoul6NW3lgP5jTes7A-qI8o1TXuJFnHtzk0TRXa7HIqgnQiqhGXN60wNORm-DOgzVvoQwN7tD2frnhvvukeLnxWZXv_SXNSX-u_uAKmT_PxfzoI1ebSPcj7nwTrginMTzX-canN1euO7kg5jUYSW8i55tofiO-8xpLnpR-fYnSLtiGYLPhD75gB9VjufjeJXCpDzAStfZ_tnPrR1e1ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9zNXPsOvTyBTT12P9m2AGV0CXeBHp1mfArem7XhDyTIwE5yA2KCuxOzFpC0Rhism_BwUD9s8FiePtWJef2ZDFdx0e1WhyfJ6FAN3x_AQkHP4SDcNPMnZ4EMYFXWVUSB2GS1olZM2MHrAzbSKWyCaUD6XU9Y98rY-GqJpZpoLiff3ahvyHOQdPWlkjPe-_s_7HXUJjeP3ehTSjW6zRnV_XRLFF_H3U45-Z37Je9eQ2aSJZH04vzHZfZYv1We5yVfToyX3phYZuVcJPBDndM82BtWTf61f-oZUONjruSqbtyYO8OUuI0i2Ssr5BY38NbIAI-FzzbwF80oAa7ZbjVszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsXec9QPrNjDFNqGYgwOLAgu6RRvLfXcH4l1qUNL0L0QQ2yLH4OABy3QUDdIo5REUW3wXZ8_C8xGd0x5zmFEXglIiBsvGqEU5Z3NboH5wMaO8iMfF7GaUNziFLmFzO6QwbBaC3JbtDhmjxxfbou5u5z9H0YBo9cq5Zc_NpkAKd7ywhKpusOzqQ72FrxnTZhX175OZYIJZnjHapuYVcLsw2FRQv_hfLpPaKp4Pip_VHuN3VBwgeWvcbosK9hnTeIqaOxZyoaXpLundBwE4OESTTg9BebebgMxNWD2WuQjunVH2YSq9-HkEiyqkASva4hsyBaTqirhJOgyQ1NxOf_VVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=iXNJE0lZV5wUnHquNajj3L-H4IR0w9XV_1eHXrtMRrVIZNLL69j4_wIA4htO5gifDRxpgaXtk8q0jLqWhhDeomPXg6lDv4zKm40Py8uXODQ-gl3cVK7y7-Q0WS5AKvt2HMLA5SBvbMmAmIR8HIgaRM4zx55Werd3GSgpsHL91QbO90BtXFrkmYvRZ7OMxvxxwTowhEkTmaHfTV17gytsR7ZAOtEs9EJwv2vLruhDVoIznOXDF1cWvdH0SnjFpjmIXrdniJwZJt8T1BlMe-25Abx79FI-keF9osPHuQHU6XBfpMuqRI02X6DvJK6vL1I5vKrsOVclvtBRaZCM1cDNGJ8D1qn136qx25lJUgy0bLvn8xBnmPEzFXwKIjXCvTNnqX51noSyuogCVVMRAgLm1h_PpnU725L0CkuUBqLzGf4RkmyH6a3MBKIXqd6y-2RcNCEgDrK3WoMnMT6pyfAshH-H8VEnteCszunUnS1wEwt1eBDY31Hql7t16QvvFFuJgERDsvGO9JeqsNSUwcrhOGUpjSou9N1KlKe8jUOYjSWSJbKeaZl0SBWnvOpcLzJlCpaGJ1GKs6BV0v-kDIC8iry0LLqwaFnkM_AWAp_H8Q1ytuV7gTuiJs46b-J-RS9V1Og2u6Spgw4voe44EtGZNIVSjXTAZVmHDiDsiS9mKJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=iXNJE0lZV5wUnHquNajj3L-H4IR0w9XV_1eHXrtMRrVIZNLL69j4_wIA4htO5gifDRxpgaXtk8q0jLqWhhDeomPXg6lDv4zKm40Py8uXODQ-gl3cVK7y7-Q0WS5AKvt2HMLA5SBvbMmAmIR8HIgaRM4zx55Werd3GSgpsHL91QbO90BtXFrkmYvRZ7OMxvxxwTowhEkTmaHfTV17gytsR7ZAOtEs9EJwv2vLruhDVoIznOXDF1cWvdH0SnjFpjmIXrdniJwZJt8T1BlMe-25Abx79FI-keF9osPHuQHU6XBfpMuqRI02X6DvJK6vL1I5vKrsOVclvtBRaZCM1cDNGJ8D1qn136qx25lJUgy0bLvn8xBnmPEzFXwKIjXCvTNnqX51noSyuogCVVMRAgLm1h_PpnU725L0CkuUBqLzGf4RkmyH6a3MBKIXqd6y-2RcNCEgDrK3WoMnMT6pyfAshH-H8VEnteCszunUnS1wEwt1eBDY31Hql7t16QvvFFuJgERDsvGO9JeqsNSUwcrhOGUpjSou9N1KlKe8jUOYjSWSJbKeaZl0SBWnvOpcLzJlCpaGJ1GKs6BV0v-kDIC8iry0LLqwaFnkM_AWAp_H8Q1ytuV7gTuiJs46b-J-RS9V1Og2u6Spgw4voe44EtGZNIVSjXTAZVmHDiDsiS9mKJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=RmaV9TNpdid_IX7LmrDzBt7SXuST6nqRgygENRp68zqUfePAUG5A3WF9P7etv2niub2iYHcvpJVbWoKQIK-hBwrCWCnNZ7ENOJuGbi3SjEOt0uGJ2HOy4To5HNpN0-3r4OyIpe_zscn5tZOb69fv5vzHdmkLoQQYPqrHFnr3_wPNBH48t--yFDVaTGA5OKLPSVDPiOS9WtkSr1w-YJ4DclT_OAeXqydTFBr57OutBmNCKpbSUr6K-mVXYh1iLCw05-DGXchmfVRPARxyJYARAxwU5qNTJAgnWGFRrukcXw3JH-ulFox5j6uvhLQAWkWfRu2TZIpHa1mApJxyDLgZew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=RmaV9TNpdid_IX7LmrDzBt7SXuST6nqRgygENRp68zqUfePAUG5A3WF9P7etv2niub2iYHcvpJVbWoKQIK-hBwrCWCnNZ7ENOJuGbi3SjEOt0uGJ2HOy4To5HNpN0-3r4OyIpe_zscn5tZOb69fv5vzHdmkLoQQYPqrHFnr3_wPNBH48t--yFDVaTGA5OKLPSVDPiOS9WtkSr1w-YJ4DclT_OAeXqydTFBr57OutBmNCKpbSUr6K-mVXYh1iLCw05-DGXchmfVRPARxyJYARAxwU5qNTJAgnWGFRrukcXw3JH-ulFox5j6uvhLQAWkWfRu2TZIpHa1mApJxyDLgZew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ2fFGbqVzBSv0-XmnHY4a_gCLfGY_3lPefJs0KE0dtfrHokJyWloc9VTTQruy1NgorwIxqUTMCUXXVwD-7m16pSnbvT6raK5ZMVphjh-TR8lPj6iA0KI5HMS6CchRcbBbgl3nPZuKsCpo6SYsGU1KyqJ7wniX6QgibGQT6ZgG3WP6PcNKMFtJiRkew8nC89Wsz1h0nD-JNgmhpYIm6LZGkxT2gNlJyX29cpyqWMRKOEW8bd17P_LJ2fky2HeGExvrd9YCL0YzxkQaS86eWK6SkSAYjTm53tks4K50hfZkDDHh3fkqydXyMMno66naUzSTp3KtbeIpRqgfWMxRhzYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=rw5EXUWXLip1l13VZ0Nu_LBwSR9Q8eEBZHJvWL5oF1mITXIJVX-npxj0XaxqY3S2F6CcMLDOwswGOovxFIiIWK8uodV_Dx_xOWu0ni1TfvYdh-6QC8Lkr-GPD51FD4qtBSg3QtcouduR4j0ZQe_m-GNJ1_DUm8AsnoJAMcPfnza6Sz5uxTPGe6Q9pAX3zQ1VwlnbT4SIG4lNFy1u8HSHvfcxZrHpYV8hLorOaTcKYyoA2JpJf_AaviBP5ozOjwfT2U4ERXhkiOtVeTpiLRhKRbduCk99W37Fr_xOJWuLy1FIXJ91aabqEmLsP2kOeSpK1vHLMdZ6U456XLL9R6m0gDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=rw5EXUWXLip1l13VZ0Nu_LBwSR9Q8eEBZHJvWL5oF1mITXIJVX-npxj0XaxqY3S2F6CcMLDOwswGOovxFIiIWK8uodV_Dx_xOWu0ni1TfvYdh-6QC8Lkr-GPD51FD4qtBSg3QtcouduR4j0ZQe_m-GNJ1_DUm8AsnoJAMcPfnza6Sz5uxTPGe6Q9pAX3zQ1VwlnbT4SIG4lNFy1u8HSHvfcxZrHpYV8hLorOaTcKYyoA2JpJf_AaviBP5ozOjwfT2U4ERXhkiOtVeTpiLRhKRbduCk99W37Fr_xOJWuLy1FIXJ91aabqEmLsP2kOeSpK1vHLMdZ6U456XLL9R6m0gDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_bDqJnz8gt34RFos_-CSZoLdIIT1LBCDWqzJDW3wAPyDO935BZZPbg4NglPH5QAWtnrxvd-PLDEz-bOe7jqL3tJni3QPQ6M4jXJ17tlJAa0S-c3-Es6pvoghShqckFxARDOQCpashBeVsRprzoE56xMOIruzk0pZXmaClcozNH6j-c1BAh-PtQQibAudrwb6Pvnc4DOnerlrkre2NJXOCPsAvMxPgeQ4fF37xMdBMKHjGP0b9bPl1rYgeog8g9kRCdjpmSkyFzuJmmY3BKhEJaeSj3gif0kLPD0N2b8QZJwUFh6QRM8XLI2g_FRyi8Q258L2NRofl2JQynfNepmZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSpsHPRwXdjXvn4MTotNECmiLe-vLSfIR1les_2i-9M921VtRBPfBfLK-9b0NSg11rOyCOg1wmbNiE9mJa1aR3DqDbZjiNLqT599kUn7AszegtSKOFcSnaoO8e8e1LFfLjdPy3jW02nQKtzrpn3HcBIX3f5LbwQxS_pUFTyZPF1IP8RUjuIJAeuLGb5dZmVN1uZk4WzdOIpY8C-eAAREsZIEy6RQkVqLf8X-UbnRT1EKMW7brTU3TAutJ7ZDpqdhSoZt4yTrAF747F5sMf5SB3hF30m97ONS8dAeI2denREWLPfkatKtGTSU9oGIx-CQY0dAKJGrz_weuGlC7iSZnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMdjfEiZdgICrr05_0dvvnNsvpN0L9PoDDzQTxmSr7tQ8ESBN7L0A0_7zPzU0YZlJiXCOpTP-1NW4gL7xgxiKkqzD4m0pbgjOZiv22kKznivaP1kBGwI5KjgFfCodpWE-mcPVCCEBIUQj4yPuDhtGHoYiClWKqEqA6pE-cPLStP9KwaubAbi73S2ADnNP4K0IhtrGrNLjQAQBIK5RtoeawsRZGkOm6B02XiZOAIUmjhrAHFUasyO0UOFIiEZvMrQfpp-BMwuJkU80mq9zHiCevVXjokUH2KjHpyoW9ewUP-DOp0armWRK_9dTy-YkR74gwbea2IBIMU-jfUUKl3jKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilNL8JWgPzK5CbBs-iHdWKv20TtZOr1k9pQ-5j94Od1r86WSL1Cr7tz4f3u1K54oE9x_6W-H7hrMhgcGzJUFaPuJN9WM-1gUuV5L5VbqxEqTRFuyGEXoQh5egI0UERouGNaL7qDIsicS8oGCnJbiuhflDDThrBuxPCDiAB-VX0TH1JxWpXyJRZkHC-46jZ2MRbBgqSTMIzzPAX6ejSVprp1bgVjrd36V-hxsDKEqZwtrzm_eJgnmtkPnmoE66qz6owUTONQs1Z6GhQyOiI-3dxqwyiKVD6BTdHPevIx3ppJH52v1iXjR2CC-QuQsR2StfDlBIvhgaE7Fx5pPd3AL6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b086v1svhZSho3Lhru8v5dJ88QGPpXP3m4aWQ2CoVr9ZRe436Bvt1FyFnmR_gf7yhY5ebYWBlzKza6RpEvH_NAZAyzXu1GBZ0GnSp0gJP7DwUdlquXn5ftctPvxnpnJX-X1UhBfvjoN-48q1DoMU6yeMFMBctcAJUQTuOBKbLzdz3i_GraH-nd8pIRNU6OOGy2anFCfm9Cb525jkLyQ76ukeH426uycKHRqZhXMXhhfXUQIyBMrOxjoaSWuSJB6np5nlDgH_a6nUCK_rXCWfpQNDqvcGwlqwOmq4EcMEisUiNdVPtHV3MYsnG2xYrLG8hPJDgffRFvquDGuU7V3DAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=hgTUPKm8VsNGvNi1Di0P__N535tUbJjKVRpJLhkzd-Av4nuq2RKXQHfRzhN8PHvJZo0HCTxWKUeCySwhJCY7_BJHAhMJhLVD7vK7md7EpqJxnAJ6vx_NBCeYoyaq7KlFgTeovN5WAsH8YIbjPPWN5cNzUQtDLcfW-YCVgg4S4lAWZZ6I3mjGfa_XwD2kfKpclQmY3ni8KXXwvBVE81wCKGXZxB94CqCBlQzjiB4X5C2Kmb6dWndZ8Fdo5uNSKbVx0VDGVfkX9w9gEaBZNzeOpRNhmAqwpZ8tHsASQtDSL4YVTgi5HJWCXFnGO28wwlOadl6akbPCJHOHpD4nf9dU2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=hgTUPKm8VsNGvNi1Di0P__N535tUbJjKVRpJLhkzd-Av4nuq2RKXQHfRzhN8PHvJZo0HCTxWKUeCySwhJCY7_BJHAhMJhLVD7vK7md7EpqJxnAJ6vx_NBCeYoyaq7KlFgTeovN5WAsH8YIbjPPWN5cNzUQtDLcfW-YCVgg4S4lAWZZ6I3mjGfa_XwD2kfKpclQmY3ni8KXXwvBVE81wCKGXZxB94CqCBlQzjiB4X5C2Kmb6dWndZ8Fdo5uNSKbVx0VDGVfkX9w9gEaBZNzeOpRNhmAqwpZ8tHsASQtDSL4YVTgi5HJWCXFnGO28wwlOadl6akbPCJHOHpD4nf9dU2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OshtnRBAgjrkcch-NNLxfXwwOdlq6wCOWFcyhSMA9Xbqpkc67su667Bw4uVCvoklZ9bHSYhe3x7OIO0nYgnmlY2HohzBaK8hbosDqAArKHkgCnxyK9UBKBXfeqRh7QMX_j9ver7WGguNgj_8BIeGYGdGyIc4meTLQM5MyBD5YY7EwBL2vJ-BQtR0oAMMyretPtl29ircPBVZiE23iEcxLMoAamNAzWnD_2bM0Z39Ihc-eizhjCmH62UVeB5wOzau-T8vQjNx_A5apaCEvRM30uWQEdcTDWnoQYCaENjj4m9i3FEfEDiesTYXwUJcndOZldtp0uiL_6td-cyDQ01DfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWuiVlqJwzodVQBItyPrUmPQ6LJFPIUWJIrJ_Lnk1rk8BRvqYurWGuesL1cENxL8Ctq_g_y3Rh9HeiggVYCtwxUoQCt-H1zOxfxO0flxCblYKKokFHFkJQX16mam-yuaGhHQeZ5VKFn5h-pM6EDE99JreqZl40nMb4G6NPu7Jl8uwzEEiCBv9-zEb4Ap-JZqEisPi2fnkgZTu5BnjwRIm3YPB1BkqVy_nax4yGKscB-Je6U-vly6hgxXQ8Mt45b452IJ8mh_S1ewQG6CpZN-6NFWtnp8_Q3IOc70pCHOX3EUojPfsKNWwWDfVpXZBpgkMe0CRMS3GsutalIH5pme5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=LigBUmhTVwL2Ox-oEkQSONcACG--8pn1Fae_bV8wnMK9Q3ktELGgGDr7PN8JDrSQ2cDRbLnOIcA7-YdyuM8a_-e72q-VbfQPLmBuGXahPwgwxJVGKa6LJF5lsma6alKQ2AQ1-oC-5qXvhFr2XNLfjhy6wuB3JylOH1Z8o_OaIAzwCR1DZmadobzDOUn2UCtgum56gNZ_4jdcJbWt9YFDUsTMnPHMMw2j1MMKsc8xNIooVbI9hNtJemqkZeuK-UoH6bdLYBMMMTcCZHWw28HoScgdp21LqRKvFo2rUg6pZaT6_DBGd8Lyxqg6C4LDMUlzAqJ4G3DNWmw8LURLsGfK6SDSFNXrSTEf8HLaMl_ltKFHBA1kVjL8icnWcjAtzryYTolksJ5H2iXfDYmi5rlHN1VgZ_xCx1i5OzaYCaS0BDg2zCQQYY3Il19OqHuagK4Ej8381Jjkn1QLXqV1U7QEkOiP5OoyEUZkwudX7YMcFox_gpynZWc5M6F3Xl4rBZ9DvtELksysWkcWNhUC4E-WmMlqOk_6OOT3cWVEuXy0rTMhcfa5tUlpULkWgpRw2uL1iUPaUSygGufdc6XejSHoeIo3dMD4Yx2qW7aNUJSwUDkEqC_1Eqem8M_dAZxE0Ot_p5z_oWRITt83FH75GM78z8claDuNhCIRoVfrWxdJxyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=LigBUmhTVwL2Ox-oEkQSONcACG--8pn1Fae_bV8wnMK9Q3ktELGgGDr7PN8JDrSQ2cDRbLnOIcA7-YdyuM8a_-e72q-VbfQPLmBuGXahPwgwxJVGKa6LJF5lsma6alKQ2AQ1-oC-5qXvhFr2XNLfjhy6wuB3JylOH1Z8o_OaIAzwCR1DZmadobzDOUn2UCtgum56gNZ_4jdcJbWt9YFDUsTMnPHMMw2j1MMKsc8xNIooVbI9hNtJemqkZeuK-UoH6bdLYBMMMTcCZHWw28HoScgdp21LqRKvFo2rUg6pZaT6_DBGd8Lyxqg6C4LDMUlzAqJ4G3DNWmw8LURLsGfK6SDSFNXrSTEf8HLaMl_ltKFHBA1kVjL8icnWcjAtzryYTolksJ5H2iXfDYmi5rlHN1VgZ_xCx1i5OzaYCaS0BDg2zCQQYY3Il19OqHuagK4Ej8381Jjkn1QLXqV1U7QEkOiP5OoyEUZkwudX7YMcFox_gpynZWc5M6F3Xl4rBZ9DvtELksysWkcWNhUC4E-WmMlqOk_6OOT3cWVEuXy0rTMhcfa5tUlpULkWgpRw2uL1iUPaUSygGufdc6XejSHoeIo3dMD4Yx2qW7aNUJSwUDkEqC_1Eqem8M_dAZxE0Ot_p5z_oWRITt83FH75GM78z8claDuNhCIRoVfrWxdJxyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=BXRM9oROIwNOrACXHhf8Wy6ei5jd8w3uLZFJq8SiJR2hpWYvgtj3FKMfmoxs4WI6h7cWT_VOlSq_X41w3dCEn1qGCLlvpV8Hzu45LYgtW8AZ6qjogQitYrfneRTki2JdCqJWBuH_koS8R82EUbpWQ3nxNrbF3btCh1DdC52TDwH3Wbm3JA6q3KyO9v7qx6c19iohYl82YgTO9NR1X-DOmd9yt1p5ZNEEfAG-aXhGuV_zqpEJOkyKvCf3ltshaZB9UyPF-5uz2c6UPjPrFjz6LOepVdGxb9L_bArsInMRjuqvqpLqYjt7oa3N34dLM30bXFcwWhXZXaPq5GTMUMwPuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=BXRM9oROIwNOrACXHhf8Wy6ei5jd8w3uLZFJq8SiJR2hpWYvgtj3FKMfmoxs4WI6h7cWT_VOlSq_X41w3dCEn1qGCLlvpV8Hzu45LYgtW8AZ6qjogQitYrfneRTki2JdCqJWBuH_koS8R82EUbpWQ3nxNrbF3btCh1DdC52TDwH3Wbm3JA6q3KyO9v7qx6c19iohYl82YgTO9NR1X-DOmd9yt1p5ZNEEfAG-aXhGuV_zqpEJOkyKvCf3ltshaZB9UyPF-5uz2c6UPjPrFjz6LOepVdGxb9L_bArsInMRjuqvqpLqYjt7oa3N34dLM30bXFcwWhXZXaPq5GTMUMwPuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIkulOrWRWtunYXegN84PweLjsMRCAkKp0sSmrf8BkP4vGbDqbOkJTrokRcAkZ7ne-z9XfNlUSWJ0AlPDplFc_i7aT-0RibgAaD57rdDrGFrsRrqOb5F2tQX5lcXW9G5xASWnfyETjyQBn5vCPLL1uiD1RLlxxCPtYBdQYVQIemSPKtnAAg8pcSIVCDqQdxpTmBccQsTGGzHUhz0M4WNzUbdzcUhR8bSQDm9bmT_DhnXiz6VxhhYceZICu1fkIb96g-VadmZulDgtUGkKOyI0GGmaOUM-yjIixrZ4-R_k_bAT75fKUMtqyD2LHjJzTxtDuIjw8zZ6SLde0Ew4wcuWzcY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIkulOrWRWtunYXegN84PweLjsMRCAkKp0sSmrf8BkP4vGbDqbOkJTrokRcAkZ7ne-z9XfNlUSWJ0AlPDplFc_i7aT-0RibgAaD57rdDrGFrsRrqOb5F2tQX5lcXW9G5xASWnfyETjyQBn5vCPLL1uiD1RLlxxCPtYBdQYVQIemSPKtnAAg8pcSIVCDqQdxpTmBccQsTGGzHUhz0M4WNzUbdzcUhR8bSQDm9bmT_DhnXiz6VxhhYceZICu1fkIb96g-VadmZulDgtUGkKOyI0GGmaOUM-yjIixrZ4-R_k_bAT75fKUMtqyD2LHjJzTxtDuIjw8zZ6SLde0Ew4wcuWzcY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJMDAtbqmx2hXOJTAE8aJgMX9TooooTlFDGLxMQ8jTPZH4L22nRVtjRAK9BBKxaEm5HtEJTAOgl_95FKZAHWoGO2vZvuGPLk05YNdPUCyPAcdY7t63IV9cyH77NfT1-ripsKvxvyCR0-t7S3RFbvuOjlC_CFZiJa_Tk8BCZi3CMIvcjL4Ri-yMeecgE10M757cF-gr9uOTDUnYcJuBj3TqtbnfqofJEASZqhRPOU0UzaPujCbq2UWBe7DsppZtgAd7YoAyAI__m9P_MbukZXh3gGaxZJMzn4Wd382lyqi90FTurSMXnids9oR9vjYJrE-k4SORGj4qt_vKRYbQHV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
