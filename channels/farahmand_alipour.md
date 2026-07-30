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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 23:41:06</div>
<hr>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgyfBDuDCJAt0JNr3swz4HIiKL9HrZbuqCUgpWgoWH-EZ48shYa12Y9jdCvxYiiUNFYEdJyEo7wU00C_BFnb_CTyVpzrMF5rOaoq9kfY20upu4yrh3hB5FuUoO5req5uCes4pUb52gmb0Fy7wTOXqJ3zoNQli2K0qbjfW0UG-maUyxTkGqrZoG-0yyCxvc7BaTOLtGogCdjOavj9BXcFLXh7XHPNWWIadDPMDLkUiV1vEWOIIbA-gd7WI75ohIeh1Pk1T33bNTZMkSWE1h7eaOVXSgYf4bfPEE0IOn0k3beN_HQF1mbN29UXT4qshW1DSNBZOglA8ZOoGk8W2oZOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUv5anB2qfc-brRh1IVJenxVNXBR0sZCsS_HQO5fDdRmfS3qbRGp8xsjEf9Uje5nBbcXkC-QdgDT5oHzh94KGeFdXLTJhJUO7yOT48zlcgCBEJdFxKmbzPLPMT4f91Se-3Pxl4zLbStIjl3sROPy4gDLxY2Ji1oTx81YlzciaS6Kjm1B_sqLI_bHtYm-5M6GVKX-iAjZD8qsuPR05UFej5AAOGArjArlLCmiIMfcGvInvBRZmcUYzDNd98S7O2yy20QFX9oTOhwtBJcmJsNQHa4rBEB8PMp4Z5J_LZxafM2YCH8__zbDb_rWZTuZhYe6o0Bok-mCja1U9qPhTmi8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcZi7B3J4v_54mMLaMeLbmyvCkRt4gactRhXoIeiHZ-AsCFJntWeBWWD1teE-raiff6dcsGETLsCRrIJiuJHzZex102YF0xsErP7Z9AoGBxeX3d892LEiEAAPHH3fpnF6ftl4I57kpboD-Nc__bQBfFKYQ_XiXuhEBJjoZMeYHsLXpD0c3QY5GoE5zJlm5fP-FHcR_xZky1Nqen4CRU6CmucOc-YqyeeZhaDdHMDOxGJ29W0RE_tp8SQW0F5eNwSzYxVKKT2yCWcNnXVkCxe4ZhTuajsrltArbYh-HSEBLH6uNdX97-xuyFvm1BW-iBDJNuLrltHtwoE_JQpUxwjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=dpBW-cFev1gfS_xWN0elf3UMZrBm7IFuv1hoybSGQ4idqLoTQ8sEJGJATd1wCp2UiGmNAvS-2_IYFutB_jw7AlCbSFu2l6Js08cXQ06W6SjEUzdSuobNLr15wwst0UktG_ZcyI5DagD98Tr3iFnWD7u-dpMQXzBhkcsL_KJafyfWcjHefFa0k4wT4WmGwU5XtmQBOoylZg6qzFCbCFAWk9Qf6ozvHJMww5pvFY1aCAwCBJDxrCwJJm5u364fbTwu9Y6c86PpK0B6MYkHRk9HHxsTRjP75EbzznR6PbmLgIXD4cXPOMu4QFsXhxwq0dVkdcV4GKqMbsimXf-4sPagwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=dpBW-cFev1gfS_xWN0elf3UMZrBm7IFuv1hoybSGQ4idqLoTQ8sEJGJATd1wCp2UiGmNAvS-2_IYFutB_jw7AlCbSFu2l6Js08cXQ06W6SjEUzdSuobNLr15wwst0UktG_ZcyI5DagD98Tr3iFnWD7u-dpMQXzBhkcsL_KJafyfWcjHefFa0k4wT4WmGwU5XtmQBOoylZg6qzFCbCFAWk9Qf6ozvHJMww5pvFY1aCAwCBJDxrCwJJm5u364fbTwu9Y6c86PpK0B6MYkHRk9HHxsTRjP75EbzznR6PbmLgIXD4cXPOMu4QFsXhxwq0dVkdcV4GKqMbsimXf-4sPagwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKgpH3fWUw4Eb3VysAyagRhoUQrMOaP_4Q_pT_7Z7s_Y8w8pwainr5scfYGGKT640a304Jq444_mbqoq2i9QG5yluSOUej9eBFRX8Uce0d0OmZT83_5SqNVtyRaK-3e5kCX9IQYSusbHjwQo6TEeuI5u8mjcMD5XUEt6d0iky6ZUOl21Qb6TTvi2GgAM94Fh606HE24A1L-F7laUZ_ycI0_Rg6Oahg-kH8IatQ0uVneeJtvfDelYmNawPTz8WohodOM0k8_YTSA-BpezOYiMTO8sZsG6bC99ysBqePOrsSzXWZ-UhySr_x2x8VUQbFtxL9g2MXrvOQ7pU2kDmCSA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkrd2t8EEuyEY4VO-sOMA_QnXJff6CCQAMAGddINRvSZLk_eDp67c5D9wtezkCLbwUX6a1OCDzSJsEHGs6BLYp6drqsXJJzFtAbQUe6ZAnQcpCygOfYIv7NSxd-AbVBDGumqGiSTXtT2MgJKXgkzSR8jK4-SlimRyfSFWsF55txEQj6GiVjj8s9IDWVvtLqsrS6_1j3rfRbqfpmSjhKJQhIpyz8MjQnK5HRxQ7howCmRtrOEPdXEsedPC4hVv6BYobGox2WZlcKJt2N82F-ju_7_O1PBHaA9w0G-Rc52RNc675mQQLEQ5W_Z-pdYLhfY3pUw0YpwVYdkaoG6WanAxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUEQO4KckCkXGdcblW1eLfx1KnrEDVoPW3IaIfTRk-eXED9WgSEEyABXXY4X2d5gD-BOxG0oub5f2aBfodLXPYz7ad_1IIxsDBFC7O4rbj8QHvH89PXn5qPYKk6LhG1tLUt0a8JWj3ieQ4Hu-X4M-Znz8os3MO6uoxTdgIUIMstP6rgs5X66uKBeJmdm-DRYkHjAYsxOgnlXvu_YaLdvyHQhKelWsXKJrsELsnAmmwzy5yoJkFai8BWlo3yn9NYOLBLDfSP0Saq1TBrLpYjk5G3T-R4fAp7qa5bp5A4ySZ8pUWBZ9Cjf0-SKHEvtICFl6FBWWT1FS6EUJREnWMBhJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2Ymq9dTfC69mJmAybyzW_IjerRL8AeXUH61QjDg2e8EG66YLdQbQ0osSrr3s18U14hERC6cGbjDhP8Q6rCEJ-x1j457QQ6NfKxB--zePZKinnBFXdZjeFxwMTwdo0zzjSVBBJvX9WlRQ6tW0zJ8LkcqNdb9gbQ2Rv1_y688jhwKLV3Bg1sLI-_BaonJAEzuD9LunbzsFIeJUlcsLTkjLXk-Vek4zOXJDLRK2ckCmYBTOea5SSGEShNrK1-qWxyBERyRsuqCYsZEZJJZKrpFng1GhbyUrrB4-Q3ewa0dXHtigXtsIQps62pdm0Xgga-MuCog4PFX0H3wqvVcCBDkmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzLSZLxyab1K0mQhHK7w4VArkTcU__p5nMVPoDD2UUIGnZDdntes5G--rxo1lYPeS8dmE0X7fPaZuD6-d3bSgMb8a3dNLMxwSvxsIIfUFcZS6fkLT77CSUy7LpikWnw7Ts9EAov8QeSJAo8HhTE3ZJ_6zF71wyRjiBIIaZmV_eUMLtFtXufwhPzmMJg7aFFs_fA5uaFxDCwWquNCKNK9vsOUpbShS6UwTXVOqIdzEAuZhZns6qTmaYXArLCtbsFbxCQ-pecrT0L6-3pxwZhJ7k_ulhGwCj32umSSRcaLfGFfdyR7d6Tiy0DRYf4y9Mwf1yCYChNivYB086U2uLxyCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFlRieGf9crIJYnWHZ5TmTlQlQynPtf5PeaB4vYptfH0s1GwkkrRbwvJNZCht_A6_bKB0EHP7BTkjRxC7BcckBFFFnK326yw9M7-jinNEqfO6XyEvxFRp7b8QELywBs5dz7jQ9VViEIcHPG6qCa9hKDds5iAmH7Qkn7PGXVSwzfSir6AkgZ23cu4wdS1t1_Kb2Cfw0rrKvBjOjVyQ97t9uYQT70OIQT8jdD45hBqtg-o5hfPiNoL9uXsqsa30MTQZamLNRUnO2J8OQanjtLWlSobnju5o5TMgQreuOfRhGCw_p5TYdKj8sg__ZKlRqp5n3D22OvFpJn0KPCPBuEl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC2CuYmMoaNCKMsKCxeZ3QeC3mOQHYCpSonuiKjlR8pzFocdbUsz_J8_x0wUqSjzwuFRS0DvYohy-giLap4ymCJG72eaasMypZ4YK8ItL2li_AI2iVO6cPDrMg6Uu6tDHKASOIZLteArAZGOXbS9rW-mRjASw7G-n6Ey_f8FQ55i43_vAQ5zSdROImQXRNEiWiSRHK-h9mB3dypc2C_YCBIycEXFWxRuw4JorOrDTz-3_2ljyDMdG2_4yBcqefS_p8PDVyW_py1WfwsrQS3QfbynKC21FwcfZy3y7RvX_YUhW1Ld8hoHqs8l4i3K8V_r6bellQQnoCpap906O5e2wQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=gNpiM2LM25IBa_jNa50da0KNWRarOY_8QgUkYmcOmn96t9npA-ZSoprDnZsvGC-bHX92o2HkejMQsL0vakOW3He72RyYdw9Q7jll2rxC6KQZiDWewBRvk4EPz-AYmXKBCbKZiXFFgSdv94GbsV9-3J1wEDxXBoUQMv21Df3_rdFvYWPQlV-KJEzMPtEuLoz3IxMyOyfz36sL7_jmEhfROsnsux5I-8ciVaPAC10rAAyQs4AVX9r3DOyujC_qN9BQVkd2eAh8PP53FmoQF20-AzpIknwpcKPKliGVBr0WIO4b8UGdmErzKEhhnj7HxEvyZaLoirIz5_1LX0PwmUmNPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=gNpiM2LM25IBa_jNa50da0KNWRarOY_8QgUkYmcOmn96t9npA-ZSoprDnZsvGC-bHX92o2HkejMQsL0vakOW3He72RyYdw9Q7jll2rxC6KQZiDWewBRvk4EPz-AYmXKBCbKZiXFFgSdv94GbsV9-3J1wEDxXBoUQMv21Df3_rdFvYWPQlV-KJEzMPtEuLoz3IxMyOyfz36sL7_jmEhfROsnsux5I-8ciVaPAC10rAAyQs4AVX9r3DOyujC_qN9BQVkd2eAh8PP53FmoQF20-AzpIknwpcKPKliGVBr0WIO4b8UGdmErzKEhhnj7HxEvyZaLoirIz5_1LX0PwmUmNPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzpJafn6LRLpB2q8iW7X1TN9MQ_56ULy4ygELHzQjCNf_NiJ45VBba1sl0JTOzaivCHm_XZEblSfaVGcqn4dUTDtLPjCVqWYRM2ZTK9PykMMd46HXl2KVQfS2vw4yDNQvsbAvWrX2t1kS7F8hmK_Rzky3G1YYN0DmKQiDm5e9cdpI_6DHJaXz4JLJ6l1TGap1axDXLbIjiPNaTH63nqJ7U3E-VgQzEFovzh5jZvbzmVvcePqhV06T2ctTfjvVHgJhmTdLkwhjvx-KgWVpihDW2LvWE4UhOJXLXd0q3Gntte4SFYnfULtAlEfY37fL9Axs3rTtK-6KD5xuGkXrktIUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACiYYQ3VAIFAIQfBE23aPp9lLZb8KjN3vCdnxsw8QnAymx_yklw-Dlw8DbQVNUuwnSFYrhOzWXf5K4EMsAwY3MZOHP6VRZofBA0noxWbTtimK5d7sIvOPyGwgzdVFci_ncheUoCK08LePBOd7B50cy2rIz2v2hiT4whB_oqUmilHjCGAMaHdnnFdgKjDrWXkTFvC_X7wGDsEUrEb55BqzpAL7IUyUy5xaqR6hPXLbH9BpJL-qB-Y5dqCMUvoC5W460BUGNpqigp8-gZkx-33bJblmx9T3LfDuj0U0l06O6V_Edcrf8W_BOMIFtaCKojrelg5DqWk1FQDUL7lSFPXFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zx8U0G_eFJJVKqmSOc0Qt6XwAT5FiglcMGt-6bZZ3QpU1xQXCmOMOoe2vLZJOIGYPXWi0q9ocmb077udcLQLJA6U1Oi5aiTwh5CGKK5l7sNT9TJGTy9htnVr7GhABErRz7bgi2cTIIDgcqeE5H3ZodNOY0f_xt9dt2zhK21NHGDCI-xRa81oTqHQJvQUBQzTHzQ_G7kaPTGeNhZPdEqmXFBeWxYBD1aq1lGVvFqE_YhNEr3BCL0-yPmAljd0_Pbx9O0q_J2SYQExD4gZxPZI2U5RlA3UMrm5LC2l88vJ4TPOUUf7qOgFIXVsqiTHB_oD_mvP-dDn7tHCiF3U4Kl20g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9WbTf2zKIUltW6Bw133q7gupI_wEUthiqiXyRXhjtEgr-wmXYBEV3n6ouRPAPLfhG0Vi3XSGKYDRgrGBFH3I-lTS7iPLaKyLvinLnWdSBwbiJGcwq2lLZkISHi24gCujqPbua-g7QkvlWIGPYb6ySG5CiwNUmEK2sXgjq8pQ9vvFVVhwRLmR1sjbDa99lJEvn_gnv9pnrGDlSuPBnYCKi6vnhsLH0qpq0dKZ7P9ei3dhS5xY8zvgcvZAUvqPLXiK6ANZBYbyYeZhY2-zvCiRoch_Jpg8AUPbh2IXcvnz2f_QxrIX25T7wvbG_BCKLdV884EXm0W_ZIod4WxQnrkvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQpDAoNgtJ72HXTuLTkA3tWWcblWpt4K6k6ObqlSDQQlUjygIVQxyiAS6vTwpQOuUVM29XX7Gqb3NSE6IoHVY4PI-WJDeoEDkr3aLMG_cBudSK-OZb4YlTrukX_XGKAvEAbF4kdODfodhvBTQbXTPEWjVZpkSU1xu8bh0owJQsxnZlRgjQKpcP6oJ992Atpk7_lha4ITWkfatC-8qymcpCPKSunHh1vgGaB2vh5czBUhVi5yVuh0TO-Xt8ZhNI_WO2ZACQsMVu9xHV3nbn252-whOlQ5aff1wtcdZ_QofUuU0v4bwjZ02_QutwWjWGTxlfpxIAE7NzyCLd-A5cxJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0Gks34aS-0j0oVHrdIItYWZvvFnR4uhHsZM7ZS2DAnWj6C95ir-bjU6ny-Wvzt2XifgHjKAwjBGMreaRKU_QNm1bfqSDhp_njXRktcEyTwOLOajxKBVBsu82UyxjKoJeUV5K5dmJPw7T8oPqqrggIrxjnXVQeDcAsP1Uga7ZraAdAO9R7Rs_PTB_X8PsHqZDyUemCd0bihb6yteZ858-L5qU78ibNNFMwwp52nMaUIew8EH-O7mhlhXNducIULoK-ih-pLuCjpHQ7RiNc9aLv_z8IZa8JTYiAkZEwFtCjPnz-xXrr8z5Qf0E4Oqg5f0cxyElSqJQ1d_b1fqxcTuLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFFKV_k1aMLfw8nE0JGD9XXwj812pNhq512R9reNG3vsUkFnau0EVXQWk5iqRklEKDr5CgSmEKS1nWTOHNxQ0Vc1Wz6EZyweXeh9E35vvJljci-XXumkITUkXHpQc9yxqyJ59XFm24IbJ0xtd_79fkBlEAgz-o25OJdax1nEHMgnRcOT3ZY4F3pF1mNjUSXPgo8bow0o5ENqynfprrKpQ6_sP6JAXkEls8i_cVWiBf4HangvdylMirEdMNjwQI8Q7y7ifFC4UEpZlDn6SFQvv2jwaIKiII1hqiYGnn8av8mHY2EbybjoU2gGPPfs1TegE4241eeyrQf6PD5OUvQoCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rR4oreVcfWXhVTl8b0yHRBYZzIVtTnqlnx5cFhbjUk1kQBFz4h3UBQnLkxX_mp78PEP8McIpnk17HyOTRiBGQ79BWr0ceeub9pQ0gmznuhV6cSOP5c6stOaSP96SFkuuiMkaqUD3i0sSKe7jK8Yw_3HYyxGj27iEKBoDkmklulLTacLPlX8fpAr-CO48gBLTq4FxG4TocXC_oPCtpECMMRUcJNSakbn2I1fYEK3GjLMiJLQnW70Qc4AWZyyvWskm-TjvsNC6P2PHAd4ZfSixcYY3PJinVISVk2T5mSiD9oSqYkpV8CG413v6RFF7ckxd2ZxXzT97lJnBsSRYlYeWJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2iG8mXU-VYLkFuFri_RCyRUXM0Bk6pinqm_2lRjl1ZsbF2N7KAq0_T5an8OJVSTsyJsDRfsoeG1QSUti2iqXW5VSUIGsa0RfD8tmdv5vHoL0_tjJBZQvi5tWlz7xy-OjNnw6JgJ50W39FmEWClFPeAI202WB3kbPqY1ybHTrRh2-7uj6tJiO3pvwxdRWabeclZIqgj46aaD226bCeS2rWhxHMImRNvC76k0AKp6eh35wWUt4VFhtAWYRQ6IJuWSggkUyjcQuXd5WBk5iIla-RAp2f-HBMYmy2K5y_5V4VtVK8Vs805hIpkc46IF5NZ_j2mTLJY3xfmLbbncmUGjBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0Ftq6MyDZoprH5aN8w9PQ_mHDTWaop4a1LOQ8xbsUL0Cy26zel7mUpw25RkdW_GyMic26iFsBY303kZuJIaE3IMNQBgmuy9vZ9Gd5ihxgBVI3smJUm2SStcgp4iipsVUn1eVsYHnxdhA1Hg-NIGsQhUp58D7veHQgp8FmUxtZeg1SNe-kIG8RD0z7kHCg9uSlT0dStKDbKTsQ3gnugT1_GgJ_8rDZTVVCdCZBe9w0qJnrSASNzcWsb2BWno0gWw06pHnV70Z0ymGVKj5BQXlPQlnbZR3RWrruu9_LaixTnlqBT1eSnSKfSIhKMSC_fqV5a2NDJg9Z09BUZg64FmhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GuGTC-bcsyNOrecEATUh4yg2HNtDVR-S376XSYNCq1tTpvGm7Qd3UGzOh78M_vBVNogeMVZa3NFb7mvQrIqOMzaWUJ_A6HA8PIJ2Kl6V7WZIse1AvFcqRYr85kYxCn8ikTbjqMeiMS7H2h75YaWejkfWu0y3_HfAmxR-V2cG_MaLBQa3TAjaNeL0iDDe3rhRVU13ExvIj4MjQYJLzYto4wr-7NHGnMYMKZaG1QJ6xD4HiQowZgpMOF_xRwXrnx7IKlQCL8L_O-HgfyKsdzlwOZeO7cjegC2jFQ8A8sFDn1lDZKIfSv6qFoZ9uT8tteBIldUa0tyWJlDyWmntbWT3dQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sdm4DCgLQhDZ1T-5zsolp08Fql4Fe4Gk6nH0Up2i5qPcyOdITpJAVJY5Z2u31ZBx_B5kAQjDIX-W5QkD_7A-cz97jpeKpP1X4PR4lLAtlTA2tQzUHn17Yx-J1wJp0hsUI_ZnCWOaPQMnLuAr4Rk4PqKb8FbDSC1K16pRwzOZKzF2ABu5ws7iQ226TePc9a7R3IDaSBysH8KfvHEk2wkEO8gGO_Xm5nH8_a33EcQ65f8CrPdEPQzed2VPKn1920M2OL2OKyW-lV6xf015t4ErIXFhQVBw-ERdsVqksU4fzFPyYpWxC4SXl2W55a5Gbh1k1y7TECc9UJ5Ovj5UOMK2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qkr2YeCPZbp0RihD8FV4vCNpMcfGBj8QnKrBYh-wWX8tNi3W-8Yzxmq3WqX2vVCQb64A6hhlm7CfNRayyHgXYUHoXSARiRd2Scl415qodgeoUvwn47HHXkEtwft08TuH15MfN2MNEqQSeMI3BTnIIsZTSeNU9ms1788HE6oAtZZIDurtvNG1OoA4QLMABCrVFUNDvPm3ycPrOyjQjzCAq9MVBlV5HhGoNCWF_9Vofdra5t35Zeu7zQdvWahcPqyWQQLwtPXhsRavZ9CIllwUKSSzylX5cIBkO8lsTUDVvC6Es0xioaUR-tQOwEXvJ4y5CmcNSQPjzBl5ILmzIHEbyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZdrhuxPO7TanF6c0NUPghtfmLESpPTrc1garAsQElzBjj6ii6UGUlpI4lh480fXiazxCMT2t4Jvq_8ZHDIH6aRzePFkBA1EOS34FdZ74Jwcs8bdSCflKfO2yN-uSD8NWJ2lai9GH_Dnmh27Aku7-TgDjjoefgVV-QCmbpFZ5Y9YkU1-K5cdDZrgZUeOkn-Ncs-FztlOVKdmKqVPohU2gpZcnyWXHXN16be0dUD_lq-0Mt954gqS1vhxisLtCNh_LNEscIXdGPDtBWMp5kNZw-comdDAyGxMyRJfuBVTgHfXkK6WXfFNBYbf-BYhGPbcb_j519Z2sAQ2n_JERye4Dg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=t7LFvYVA7iMZxZ7655k7tuBEpv82j7S9jFguOtwjg3oVhIqwyF0Y8jr254AImhN60ZDkt-Lbs9UIzHkY-VciBkMHOURzsgjPw5tlUIF8dKACApI3cMFeGRTyTV_DaSrjeMI_4kaoi8mj8DUwrZgTgI2ATjl7w3LCscJM21y85RocuUFwrMilOs26fuYJVUgF2PyM74BZcqhzT8fh1mGW0d_7RNWP6cwr8uUC0Ls_TuhqHtBgWK3osldqI5pyecpfwd4djASlOETGVfeKv9DQ8BqMf6xbpCMGpdFmH8zhYwZgV56HgEeKVhemPciATuaxQ1P4XVeVhV-uF-GjaCKHLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=t7LFvYVA7iMZxZ7655k7tuBEpv82j7S9jFguOtwjg3oVhIqwyF0Y8jr254AImhN60ZDkt-Lbs9UIzHkY-VciBkMHOURzsgjPw5tlUIF8dKACApI3cMFeGRTyTV_DaSrjeMI_4kaoi8mj8DUwrZgTgI2ATjl7w3LCscJM21y85RocuUFwrMilOs26fuYJVUgF2PyM74BZcqhzT8fh1mGW0d_7RNWP6cwr8uUC0Ls_TuhqHtBgWK3osldqI5pyecpfwd4djASlOETGVfeKv9DQ8BqMf6xbpCMGpdFmH8zhYwZgV56HgEeKVhemPciATuaxQ1P4XVeVhV-uF-GjaCKHLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7Tt7IxDtbubRFSnvx7RM_PqhDkPyPwA9CdZJsokX3wCoIhZHtdnmVBL-sDFixnXg-UyaB2lnTh1kM6_sQJ1OhQAOmSVIJ_SI2nZHZTqvRS47eC-xiOZoiJCW2UMXjjeQBmulqS8aIePK2fcCREfwB5yl2k9RGuqZMXmmGAAV6kuyfyUJqN_wF48AE4TEBUS9VT2Plw_KV61m5rGj9Ma_UQ2DjnF-XEgdzmRU5XayhhCOJS-lUTKzIkcDrZO2aRVca-ZKtHtVtA7kcLW45UI8sfYvRAxmFTNpGoqBXAFbgqULjRJfdDE3BiHJ6u0ViCrAF4U7l9zX1lNGhPnsnfdpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3VQ8EEYMFBxc5n9I-C1BayMLL8zp4oIy4XIRN3Z5jsisR4b3LMCC1hH-U2GLYlJXHghftJuWpk_pGZrpyxXP8wLoftAORpUHwcKrvhkot4RpsapKkMdQ_UL-4B62FwvzJ9LISSsiu7-RkKieMtcQauAzjvTVJisMeSQnikoixGHwo2jgqzKZZ9hO0S3OD-D8KT4XYh2RP8JkcocSdYYBW67DCI_kDsRXaS9u7NVuTdVGZmVoW3SQ9L7Y959AyG2cBRZpmcSlgzx5b57aF_w4IZsX3ws-OpRU3uHcGWngOZM4ppKFFG5-6esR0C22TxJDaLHPPXVm-jlsJX18f44Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2p41lpt-8wJUQWAMZvZapR0ro5DjMtcR0O3aZpg56KLX2929NdatXPANLpClxYkpjGOjCXIqxBCLhpyjRkk-7rjwlQGQoHiJRevsTG-XTO1qDinGAstg0mUyF7U41GO2Rj_iziLe19d81BJoFW95H0xOIDooWAw3orzuCcrPXD-5fVePNqMjCyMhdVvbqLKhvXPCD7UJqBu3DPkCJm5Sjj8LRuNthCdd3xIkgv9h2Vb5dDJ-6y6gkmi_3zXMbTnpd9qFjp9FvcStAoUe7nYGOf1QYdKVxjCsXrbri_t9LruxY8Y6iXtllavo1owfOHAp07xUhGdxmnWZcwkAzMTQw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=TzjmTJJakds1lgcK5KU7q1rKGS2uEe4D88LmN-Rsbe1nzLmVGCOwI0fucwghFHtgIgb4g8XhpBgP7HYvqOjHul1FwnJmM2XJe0T6r04Ew_gQNjax_WUKx0kWF6WepESKtOgMEVV1VG98qv7_QAGymxpM2KHqtjL_uNvPaNqT69KYoQ6c28cTex_FgK8-PuqSWh48hwBMkfZyyvf9mLlb1YD_4hbfju0kcO3yVEnk1bQQ68ocvUCTeKsQvptuBPsUILwiY_hOZ3oNFtRRGC2tbNDhFpK0MnepdT3RtyoIfNN-U1QLysa4_OsQpPthxDaOLnWb7tCRfMKZ9KC7Kzi2rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=TzjmTJJakds1lgcK5KU7q1rKGS2uEe4D88LmN-Rsbe1nzLmVGCOwI0fucwghFHtgIgb4g8XhpBgP7HYvqOjHul1FwnJmM2XJe0T6r04Ew_gQNjax_WUKx0kWF6WepESKtOgMEVV1VG98qv7_QAGymxpM2KHqtjL_uNvPaNqT69KYoQ6c28cTex_FgK8-PuqSWh48hwBMkfZyyvf9mLlb1YD_4hbfju0kcO3yVEnk1bQQ68ocvUCTeKsQvptuBPsUILwiY_hOZ3oNFtRRGC2tbNDhFpK0MnepdT3RtyoIfNN-U1QLysa4_OsQpPthxDaOLnWb7tCRfMKZ9KC7Kzi2rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmJ-Z9S6bJXfrXcmwO83LRcRn69ZA1p44J2eUWDS5ziiOaaHYXaQwYoI8rhu_SypZzygirjmu1HKIwvaSzc7ECf1ReqF2mb5zL068MaPAAPJLfMYwe1szNARGucH3sBkFvPRC4KUgflSwrvLcoaxADtfO8ge4buQXIpCSeOZc3_N_rNpCf0_GRssQg5MFmJKnBtIKNQvIr_BfFMS9nOVJBV3ZVlhmH-t6_dl3TwUWLtwQj6PzflJmny4YB_QuR4aoiULzk1uWA5vbtGq9jFqGWab7ljPjtJcSD9BodfGlxCPEOqTLLpmGNgyUG0PLxWiL7VBivC1WuiJ61JSXqoJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=mTHSPaQTqJt1KkQArrmSECR_D_pb8IXGamCW-omSnaT4NsyEmyL-Ua6pnb5qkYH5i7JHOQCA7h8tplDBuORxe2adIT3sQ0oCA2qaL5xNI-KqFpBfxumPOZ9htneXlmdI-uvlj2MZ38PFZ1V38mqjnchJGQdWi0ZVlxdANhK7hec5AC4ahgAnSo2d4myrWsByuQbbbjPUteeOeVxY9bM-mhR64I4u4kLXD8_plFaReIQCmE7T86tHjc2K9eF2fU2i_ocFvp5mliATOS7YdKHVNN2edRCbumpJouHbLYBPrZi9mxnrXU7JeaED2EFQ_7lgX0eRftTWOP7Mz7eO31ohUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=mTHSPaQTqJt1KkQArrmSECR_D_pb8IXGamCW-omSnaT4NsyEmyL-Ua6pnb5qkYH5i7JHOQCA7h8tplDBuORxe2adIT3sQ0oCA2qaL5xNI-KqFpBfxumPOZ9htneXlmdI-uvlj2MZ38PFZ1V38mqjnchJGQdWi0ZVlxdANhK7hec5AC4ahgAnSo2d4myrWsByuQbbbjPUteeOeVxY9bM-mhR64I4u4kLXD8_plFaReIQCmE7T86tHjc2K9eF2fU2i_ocFvp5mliATOS7YdKHVNN2edRCbumpJouHbLYBPrZi9mxnrXU7JeaED2EFQ_7lgX0eRftTWOP7Mz7eO31ohUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm0WnUAiPnq4vMftjmHCRwm-Rd9Rxew6KptewnUdZkvQ6UncFxwMntIA_Upw1CEPQGz6NCf5BgoPT0HSidK16i_XaEjIKfgLXn1rejkD1wstF70ojMRCxLoITsVnpNVQuLCAZ6FrBbNQ3D5j1KZW18uoSFbqCDMaRQ99fTMSTH7o7yn31ow7UtyPyXLl7VUTSSY9DU0qsIGSiSp7IZZaoXggyGWwvwDqCevMSN9Toz8dNKP6qkZxJe7qHBRtBwCcRhCBjhOSJ4JpZTJHqNchYn2aiVhkjADqJBVjVF8qWhkw6v1P8AYYtvsyCiAP18vB0sfConej3L5oUd5Fy7eaUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcGecHULe_41JxtzRFS-YF-OUNCjQkT3Pyt1ZjbGlo3L3QL2uchxvs_4s2XM5W7TPZM31OumK1qDSfMzeA1RD2k57mRI299ttE2kL5VZu8HMTFii4mEKw3s1EBEKARZBiUtz4MtDZ4_gQBLVX7zmIuFD1WlnUS-dACzfuEz3693mYw39ciZxoM8alBqRzjE7PUKEgnFhiv6vm6z3RwmF2DPDCH9TekZZ4ACRlCzfMq6nSgEGKef_GiwIl_Bywoayiu6eL9kbDShEP5f0ydrXGi7cP9-X83IIupAqTeO9B8ax6eLP6CTAjTQB-3iXPN0WTIhjgmV35Dcnj6p639N94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=dCUAZh_-RLhAISgK35lI6QskXF4dB46Dr1Yk6jTDJLa44wgg22CDtPIGtYN8pGf66Y2L531bAWUei3J_Qey5n4om5d5vhGLUG1FpzCjPRbuvKBxKz4XoteAph1GhK70hPEiDzoSv2A18Oo3khb6b2M2obVEcrCRKVdt88vYXq2ez6C26rc6b3BYfUCqQFFwlA5kogF_NTNxGqm5v6QGS3caC2oOW-luE0eYmOil54gBvFnyp47D-VzN3t_1MDjtMo1uSRtrfC7WLIe6oOKXf-tJyU4vIVGLKKJKSrTmm0n1D7GgClo1xAq5sSVFQjqcA_DiuinQao_WiRRNZb7rWgH73MdXvbYQLwNx1fGDC22CwMu8ukAycq_E6C7Lmoq_AaK_x90t6eA6Fm_sx6Odl85ZpcQA-37WcGWMuYeVia0WFNcHnRTU2rIRxRYmYd92pUx71L9061cE3Bew-myViNE_iNIDMcj6_DIx52JPOLHm7tbqfQjIj1NNIRqyahCbxeL08hGiL-1DMbDiTefHwi-KoYnECXxgzAlRL2h8zNWNi3tarGo3hStpEiqxOCbVj_AC4_xFcAtapRSk7g7clu_1c1_Udleb7wvgF3LZm-eA_ltKVqZ3qp5dHelCfntQQ7rEJV6N2uFdob-pkzYqjL8m9xoOcZUF4Hxp3g1oPs_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=dCUAZh_-RLhAISgK35lI6QskXF4dB46Dr1Yk6jTDJLa44wgg22CDtPIGtYN8pGf66Y2L531bAWUei3J_Qey5n4om5d5vhGLUG1FpzCjPRbuvKBxKz4XoteAph1GhK70hPEiDzoSv2A18Oo3khb6b2M2obVEcrCRKVdt88vYXq2ez6C26rc6b3BYfUCqQFFwlA5kogF_NTNxGqm5v6QGS3caC2oOW-luE0eYmOil54gBvFnyp47D-VzN3t_1MDjtMo1uSRtrfC7WLIe6oOKXf-tJyU4vIVGLKKJKSrTmm0n1D7GgClo1xAq5sSVFQjqcA_DiuinQao_WiRRNZb7rWgH73MdXvbYQLwNx1fGDC22CwMu8ukAycq_E6C7Lmoq_AaK_x90t6eA6Fm_sx6Odl85ZpcQA-37WcGWMuYeVia0WFNcHnRTU2rIRxRYmYd92pUx71L9061cE3Bew-myViNE_iNIDMcj6_DIx52JPOLHm7tbqfQjIj1NNIRqyahCbxeL08hGiL-1DMbDiTefHwi-KoYnECXxgzAlRL2h8zNWNi3tarGo3hStpEiqxOCbVj_AC4_xFcAtapRSk7g7clu_1c1_Udleb7wvgF3LZm-eA_ltKVqZ3qp5dHelCfntQQ7rEJV6N2uFdob-pkzYqjL8m9xoOcZUF4Hxp3g1oPs_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=U7mkF0O4gdoU65aAiTdOnvP53VdlkL-82HX17U1YIHKD2l_XjI4QSTFEc53O1jhJ5MLOVF1zMN0xh351BEUrG2aXYGb2TVuXpLBL6bGmQ8B6bDMbKYvkqQ9_Hws9mqig7OtyPEwj5kiff3MYTX8SMUywD5tlS5ntTdu2BPGBPknn6s5JU13_RmU9-EluCVNK2fkXqbCI7i6LVYN08BVrZYDNIOh3lmaQXeFJGSLvMGDUrnPoOtbj-8qJq9rK9b7qEkiLAZPfQTSTkTwva2nQHN0YD9l21LP5kzakco95WD6i4tFVmWuGWjQ-afqkA75StbRYthxMnqzjexUBAg4Y3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=U7mkF0O4gdoU65aAiTdOnvP53VdlkL-82HX17U1YIHKD2l_XjI4QSTFEc53O1jhJ5MLOVF1zMN0xh351BEUrG2aXYGb2TVuXpLBL6bGmQ8B6bDMbKYvkqQ9_Hws9mqig7OtyPEwj5kiff3MYTX8SMUywD5tlS5ntTdu2BPGBPknn6s5JU13_RmU9-EluCVNK2fkXqbCI7i6LVYN08BVrZYDNIOh3lmaQXeFJGSLvMGDUrnPoOtbj-8qJq9rK9b7qEkiLAZPfQTSTkTwva2nQHN0YD9l21LP5kzakco95WD6i4tFVmWuGWjQ-afqkA75StbRYthxMnqzjexUBAg4Y3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccOLj5iuMvLjQZ3GApuYiXuoV2ltBVV8iNL25QEBPuTUoee71kvozNzTxXM507iMDCgrcuY27FnO9g4ACqy-OD9Mz-a08-qKo8MY2m9-UC5E_Q0cYYVaZlopfa9HII8lWrT_WPGyddFgky8qdHqy1O1DBKVvPLKYOdJfL6K1A06h5Op416KbeA8a_e5qpR7J7omMEk1B-FNrWDmynVOgZ_WS84B4Lu-Myka_dDXnuxtzADcfAB2E-U6XQDB4FWgzxqyRV2A_XKt8jXuJ59tVem09dcMa4-pXTfd0cHaOrFT5F9NzF3krQsewuJegJ9v4YpbhMJVlw87pkbTkEiMS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=HvjgOWddFmLrzeFFMPSl8nwYksrQJa60n1zXd-1gQNEMi1tHQmCS-F_yLMWbsKxhXwwnt-MFG1We6qfldTCcJWKCN1yKZEF6wY-4m_gaXCbd6HsL-XedHplMYTe-JxfZLLJa7uw22DjnTfI28rT93Fyb41XfC7LKhFhjilNWiyQXWNJemR3NLb70flaWDCzXwKcLRkxZZ-FfOOjjZIebJqk0h7pLgGwlI9kOS6JMCC9R5B-BKc487WdeZhUTYvHN7_ZAECW3OfeBU0k-kCndaoLJmiXn5cEOVR5zxCf93v21lSAA1YSNvFIHUcnUY96AAPYHdwir_cEw6lxi9hd25jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=HvjgOWddFmLrzeFFMPSl8nwYksrQJa60n1zXd-1gQNEMi1tHQmCS-F_yLMWbsKxhXwwnt-MFG1We6qfldTCcJWKCN1yKZEF6wY-4m_gaXCbd6HsL-XedHplMYTe-JxfZLLJa7uw22DjnTfI28rT93Fyb41XfC7LKhFhjilNWiyQXWNJemR3NLb70flaWDCzXwKcLRkxZZ-FfOOjjZIebJqk0h7pLgGwlI9kOS6JMCC9R5B-BKc487WdeZhUTYvHN7_ZAECW3OfeBU0k-kCndaoLJmiXn5cEOVR5zxCf93v21lSAA1YSNvFIHUcnUY96AAPYHdwir_cEw6lxi9hd25jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxBL7sZi7h4OXwbGf4rDAzsgr1ca287Ylqn53qmeu5pVcITKalT7AhZULZoaMnMcs79c1CHYW5_RDe76VMlrT4Ej6-4W5fYqB_L5ZqymSBeW2DJ2cHUUQT_RyK6KLNlWwWUfafxRBxpG3rx2ebVG_McP54A5uu7-ua0qhXIt20xqXYQ_U2hqFd6eeT2ufJlMC5xfzm2qPe-OiAGlWB4E7Kgf_sLO_jFWq-NP1_SxW4i7Pn-DzRzcm2bV5Yj0wBZAqEPTwEn7ny-hBqoKxzxK6_vkX-tiLOSMTTgQ9E5HHAEevO3kajMJ0dL3_aP8AERnptR3jPrdbTtgbvWA4bwYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGbxnpFXSLxd5xxeE9Vj3TIvl5KrIK1ayyH9IFK4lu3BSU4I3s5-KC9SxwmQZcOuzvJRXHlfZy274gE5pj8PAg6Xaebfv30nHVntyvRRw1JwbxvSPgZaiwcX7Yj5fIGcv8iGx6lCsRDueOt4BJ2cg4kjzAgk-vWHWiRm0bshVNmGGs2uMkh8wsVHGbfEPYl0tHIGWP44Bu2NnNE0kNvbxrI2X3-Jtak1peWBfTqU2NZkWMSUz__Y8ChUT8sC4eQnqB8OR3erWaG6F7k-n2DI_VqTfldNAt975XY8c_GJ4BpPnoxuT_ad-NONOchRYRCeHwHHOx2mV3t8xSdCWMFrLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upfXYbLtZVnzLS_9j-ZVcX3d5eoGf5rwAOdfuPXGkcxLoqTf1piIknJc9rHOquCzny5iK5XUVb7zmms1SccuaXoVgMC8skGcinItU1nAppA7Lg6nFcjOTib3h8-EK0oYkqkjo3BHdL0pJ3SRzqZblseEYy4yde33FUz2SO_I_uH9F7h4FQTgMwPpHG1LhtU2hxmXJcvfTZyghCbb2McL0RcIXig31xvLppmv9HQNhTc9F3-cJATKAQkbFhcPZXQwgfdUGsBilxvXTAfffSXwvcOPTj4Colz73CRyMPs7ckAXsxL4J4WjxeikOl-BGEmI7aw1i3yXdKVnOz6-uYTJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpiBnWoxOwSIZS2of2nstF2OQlZuvnDbmwfJHhro68n-bvgiPEcTM4JDJrKnKItX5205R6XXc5RPjStIoBGhQ-AIJ7vRi6vmQH_MglV4B4yQz2o1P3lOnRyrkAYpjBTop6f6--O1ZSqQ64xpRLCBisqOYUjysmnwI7uOHWH0PVWcfUI5pIhtY6NoYujZbWxjFuPcHZOP-2-Z5OhO011jmlcdQzOm9ON2xpFJdarDnDjylP_PbfvXGeUsQC0nSOec_zJcS_ADzv93zbX93EFn9YmejHHK7uAGOVsy6Tilq6EG9oEpi5fMaUNp-meY7BNARRGMPzcCmXLRK90EeY3xSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owVeQC7_r-0XeQX19co8Wd5oQS2m-YPky6GE0kRyMOWKRp4PSP5LRmYgn0PFqCDSjTYq3645UIvdaPMJFJVGzQ6ZZUxT3mffeod9KNNUFL7Z_c5LYISrF7oGcxDBZl0u4Bk_-040D22B3lFTuIPxvEtF4QpTpi-GUwO219rwJW4sXofVme_Ix-o8XdUJtyUXbflWFbuzlRPJdBglXDmJJONC-_khOB39YjrzGyCNBevU30PeTbl27qqucplCjQH8EzMxqOYciWT4-3CMaYDfQsYEcgOMNyvdk-68q1q3M4-ZHM80hQYR1JaEwJIYpcEFrttSUGB2-qQ6_oFiAJQi9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=E2scPJN9_PtlrdHPaZk0vHwdLuFoXs_V1AnvefIYmAzgD2LJS0mv32vr5PkhjzeGLsAmnJY5RWJKX_SB1LEqVg3ADpI6LXGP7so24Ythl0HQ0d1vaV_DBFrB6EzCfe52UBzgVJLcm_J207oN2_vOrEwapvgX4XAVnBxwc01aR2BVw11R2vDhcMLMH_CDlrqdEcuWgE1WQ3eVMqWf6xDSy5vWvDLLU7lNddo8SMJdW-IYqVbr--c5aHcSQcPYd4DQogDtkn3G2wGNLx5pdtnEAFLMHNKRH3cxLG0ouNJ5Kyzc8h_co1Ok8d0Gbki3EJOuaKpuk4Nv7hLdtXPDxYGDUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=E2scPJN9_PtlrdHPaZk0vHwdLuFoXs_V1AnvefIYmAzgD2LJS0mv32vr5PkhjzeGLsAmnJY5RWJKX_SB1LEqVg3ADpI6LXGP7so24Ythl0HQ0d1vaV_DBFrB6EzCfe52UBzgVJLcm_J207oN2_vOrEwapvgX4XAVnBxwc01aR2BVw11R2vDhcMLMH_CDlrqdEcuWgE1WQ3eVMqWf6xDSy5vWvDLLU7lNddo8SMJdW-IYqVbr--c5aHcSQcPYd4DQogDtkn3G2wGNLx5pdtnEAFLMHNKRH3cxLG0ouNJ5Kyzc8h_co1Ok8d0Gbki3EJOuaKpuk4Nv7hLdtXPDxYGDUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYdQVNCjcIxr030lTUgpPBnE6r-LFddYWlfnZVnWcg8bcntrqXac9Fz2n7hT8Ty0Gz9Sb7o7_HhqGMzsmYnO45b7gebsSXoUpqspw0LwnfgwEQPIotKccXoYZSv2YEaqrCUYxUaVm5uRlNmHkjFB8rIUsDx2bfUNyDre52SKKtrxc6RWdAOHEZ12f__uqBlGHAbRIF4XzYHOPBXxZHGSBtGupxZ4MB17ilWFv3IEiFZ8TIlmfBpjJRklhS97Bt7_6raSFtIQGFymNX7RwKvfpSM4AjxHpt31cbPKrIdFeKC6v1lovmxqaGoViTeju1NU8e_C91YK-kQwpqe_IWSCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aC9GiNkcvLw8eZD5eBZamakL1guSV4mnRPaXvr8O92jsiUdEgdiJNS2sqeQiRj5TgIyFjuWB1Pig-NAl8K6m8xmtjflQW8X5IRIATkIBep4QMR9AJexlSyTMcQKHCvMjCr_4j6EjeujIQFwhooqZA-UHIUl9PuI-SkaW1xtlwSNyRvwLG-DG66uHf9ykyiJfA26TGrXgeDOv27unr_EJ15Tupn_6VxRM7SpHhwkaqCLL-m2x0m3Cx5zlwEM6_ZKWSxJT88BdVG_cL1tthwu_lAgReKZU6lm-PReFCsN_4rDDBKraQdNjicTPN_Ap8mvTNQ8jDQ0V-vX1riFIZppvrA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=gjyRPvd_XcvZ2qLZPjElreZGi0Ds2wgmvRFLS4oVU0v2QhL8gXeI5UjIlGLZLQB4QshZPZ6_QEf6ZFcDKpo1847drY0Ea81fd39E1mbL59mdAumigEdL9DoPAci6dUMbwPwsockSC2Ny9YnJcaEcPGyl3vBKJ6QHqKoPdSmSui2oaGYp-cxYwasKcfFxvpYBeyG3bUK2bhwXMk-zqWaqq-bQaks_7Kysa1ogauzp9USAfe4AUpAx8GYm5LXuBJnuMZk_ODhBreemC0cabT_m_zqJ0FvJh-wLmaHx48lOqz5kZIc16qkFav7496KYazzy0sxaUOzO5RlzaoRrUQ8Phz7-RZqDKhXAzPaitVK6xzZndd7iIuKL7aEyaYgdiR15n_LTt29ev20X8SgNMFcDt2TE-olUSiXh9wifnefen5cVF7D51Da7VAThjz0Dr9cVXcYwt7Pi1JdMUnfHTG7GyKlyZhXU0iAproVG4WixiPLYpcZUoFFV3vWn-FfrsbZ8FsXPxGMvJCaLVQ0az4SpNlZeZtP8xu8pAFxAOOPO3X68rgJL6sXR9TXZPRPukR11EHdYVmX58AqyNeqsk5RS970Ftx6egkEJNCQt2vOdG1F7EeALTDBEVrs5lLuxnZ6DZoZnjT5U-tNdsxz5UWCOFThua6TjSGTrkLtOmIsXHNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=gjyRPvd_XcvZ2qLZPjElreZGi0Ds2wgmvRFLS4oVU0v2QhL8gXeI5UjIlGLZLQB4QshZPZ6_QEf6ZFcDKpo1847drY0Ea81fd39E1mbL59mdAumigEdL9DoPAci6dUMbwPwsockSC2Ny9YnJcaEcPGyl3vBKJ6QHqKoPdSmSui2oaGYp-cxYwasKcfFxvpYBeyG3bUK2bhwXMk-zqWaqq-bQaks_7Kysa1ogauzp9USAfe4AUpAx8GYm5LXuBJnuMZk_ODhBreemC0cabT_m_zqJ0FvJh-wLmaHx48lOqz5kZIc16qkFav7496KYazzy0sxaUOzO5RlzaoRrUQ8Phz7-RZqDKhXAzPaitVK6xzZndd7iIuKL7aEyaYgdiR15n_LTt29ev20X8SgNMFcDt2TE-olUSiXh9wifnefen5cVF7D51Da7VAThjz0Dr9cVXcYwt7Pi1JdMUnfHTG7GyKlyZhXU0iAproVG4WixiPLYpcZUoFFV3vWn-FfrsbZ8FsXPxGMvJCaLVQ0az4SpNlZeZtP8xu8pAFxAOOPO3X68rgJL6sXR9TXZPRPukR11EHdYVmX58AqyNeqsk5RS970Ftx6egkEJNCQt2vOdG1F7EeALTDBEVrs5lLuxnZ6DZoZnjT5U-tNdsxz5UWCOFThua6TjSGTrkLtOmIsXHNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=XKQHjxCjT7V-55QjPfKmV4OtMp19qwA8lPlIsfksEf_WIMUavzRxZ1eu_n0EMU4Zwn8wNnL3ZlMLv4858e5a8RqvLIVYfXtxr1zGUN_XMhTI3Wkrwhago7VxrvlQ2hE3DGIt48k-NY96xweOouzgb6bCKWacemqxpJLuAdTtfcst7M6PHZ_IUPDzswyKhF-1UQq5KO4QaFYbWmmp8vBLElmAChoLRvktorcsZUW3xEnsw--Yd-U6V0ERZcojP1hEmRVEcvYBBEOZz9LOp0Xu4Y8rFqfH-TqPQHbLR9E4W1TFqa6FPDFBRZTiPpGb0c6vowx3wzDuEYJ5kA1GkLkSlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=XKQHjxCjT7V-55QjPfKmV4OtMp19qwA8lPlIsfksEf_WIMUavzRxZ1eu_n0EMU4Zwn8wNnL3ZlMLv4858e5a8RqvLIVYfXtxr1zGUN_XMhTI3Wkrwhago7VxrvlQ2hE3DGIt48k-NY96xweOouzgb6bCKWacemqxpJLuAdTtfcst7M6PHZ_IUPDzswyKhF-1UQq5KO4QaFYbWmmp8vBLElmAChoLRvktorcsZUW3xEnsw--Yd-U6V0ERZcojP1hEmRVEcvYBBEOZz9LOp0Xu4Y8rFqfH-TqPQHbLR9E4W1TFqa6FPDFBRZTiPpGb0c6vowx3wzDuEYJ5kA1GkLkSlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIh0C5mUTV25ah2JM0MHGaejEZbFdEDNpwBFjzBbnm00T0siXC1A-MkZmIwDQDjoRgiDrjtp25tqHcPnKIQRcHRoWQVoP9Iif-q-746CtqQYJLdhe57HaL1pJdzPW7b2vZTdR7IBR9PpTwBS84ujTLfLiPZE_9w5gocqhugyR1LCkZncv1Il2VPmsvdpvJPANYd453SsIiCqaF92GzkwyYPXaIuWSmnIKvovNYNQOSvTfMo_PttlPcC1zFhPkz36RXwiFpd7RvskCrsUOGSQ0-FLf0iqAfH5xH1Gv8mCpLKfxPxyziCxMW2-fq1dnzq2WZHLI1KKmRS9DASNrecnNtEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIh0C5mUTV25ah2JM0MHGaejEZbFdEDNpwBFjzBbnm00T0siXC1A-MkZmIwDQDjoRgiDrjtp25tqHcPnKIQRcHRoWQVoP9Iif-q-746CtqQYJLdhe57HaL1pJdzPW7b2vZTdR7IBR9PpTwBS84ujTLfLiPZE_9w5gocqhugyR1LCkZncv1Il2VPmsvdpvJPANYd453SsIiCqaF92GzkwyYPXaIuWSmnIKvovNYNQOSvTfMo_PttlPcC1zFhPkz36RXwiFpd7RvskCrsUOGSQ0-FLf0iqAfH5xH1Gv8mCpLKfxPxyziCxMW2-fq1dnzq2WZHLI1KKmRS9DASNrecnNtEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mk4b0tG6PzIFLNosheDsnObD0XXNvdFeTatGjJ7AZFINHlmDKvrs-kCmG8D2I9hPt_ccaZXaNSxjB_mDtkkZxFvdl_VPncGxbFdorSpBBIlP_aJ4uArQEXXG3bDLgn5fYnwS1fIRjN5ebLcGIwSesC6Lu8AJyRnkYy_DMm2dQXeFjK7-Q0pHY2b_7qgu7QH_FOwsxwBdhYp4MlZeKfwlIenGABLTFnwSDkYmMheuuZFexQ1BXJafxNCxABU6HpvfAK1OaWSyqjL5AmH8isiWmTi51J1AQgGn3jby1TepeCfOXJ_OWPCTqQO9P7Mqd44B61jRVTkujsXzz0MwCBWqwA.jpg" alt="photo" loading="lazy"/></div>
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
