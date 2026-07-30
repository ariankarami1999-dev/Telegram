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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 01:08:36</div>
<hr>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=snfmXWm8OXqwv1HEVlrDQWBcfJYMHarp4KqNY0DI3zdaNUF1dzmKWWFqrJ5KcY5RGLXm-U4ZT8U_CgOLMnsgV8RXKkiry2tOjyCgHmcHKi8jMw_0QMUEPmqI_2v7FGIKSR7AcnlOpEMjDMIFFZra-Bumm22eBUC-3ItW9bugwSLtWMHPkj3g66kZ4T0GGRwWoGzhAmwgsDYS6_vqnIjQ_n-ahEHJUnICDTSDo8OxOaShWYqEETPVdKg4ZnLVPMWHkQxtJgvBRDPoJb2W3Srydxi871RuJ9Z6myGkuN16cstm1Xszi39Y-hVgcfnLEVedtFzs8S5H1bjvsu4l7jUqHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=snfmXWm8OXqwv1HEVlrDQWBcfJYMHarp4KqNY0DI3zdaNUF1dzmKWWFqrJ5KcY5RGLXm-U4ZT8U_CgOLMnsgV8RXKkiry2tOjyCgHmcHKi8jMw_0QMUEPmqI_2v7FGIKSR7AcnlOpEMjDMIFFZra-Bumm22eBUC-3ItW9bugwSLtWMHPkj3g66kZ4T0GGRwWoGzhAmwgsDYS6_vqnIjQ_n-ahEHJUnICDTSDo8OxOaShWYqEETPVdKg4ZnLVPMWHkQxtJgvBRDPoJb2W3Srydxi871RuJ9Z6myGkuN16cstm1Xszi39Y-hVgcfnLEVedtFzs8S5H1bjvsu4l7jUqHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgyfBDuDCJAt0JNr3swz4HIiKL9HrZbuqCUgpWgoWH-EZ48shYa12Y9jdCvxYiiUNFYEdJyEo7wU00C_BFnb_CTyVpzrMF5rOaoq9kfY20upu4yrh3hB5FuUoO5req5uCes4pUb52gmb0Fy7wTOXqJ3zoNQli2K0qbjfW0UG-maUyxTkGqrZoG-0yyCxvc7BaTOLtGogCdjOavj9BXcFLXh7XHPNWWIadDPMDLkUiV1vEWOIIbA-gd7WI75ohIeh1Pk1T33bNTZMkSWE1h7eaOVXSgYf4bfPEE0IOn0k3beN_HQF1mbN29UXT4qshW1DSNBZOglA8ZOoGk8W2oZOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCJL3-8VxSn7fEsY3P6E7Yu35KygkPYAz9kSrPiP6mOf8U_s1hTygNHV29aoJtMFV3uDNu2SOmOr0pRE8Uvfb_4v3pd1wxSiC7wpZnrAVsKJuukgP-edn0XvKe6r92a-BQk70aHqprMQhb3F-ozQFNjyygGncCdKUSeTnA49lpLU-LKQovR3tXzfRYEQ13VxHLLbiH9ZOq8KL8MaWIGiCzWEk2jLqvCACusOmTarI5B3ycu06qcPPIP_Ppb52ylFXvsw2sTsuqNG8bwZzP13zYu87MoCAD9yHgVbxg1mP8ENRHtvk-EBW8FmpMPAivbYtiDzL3qDs_aptE84S3_x2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4kUTxRXfz-D5HD_bWoXgRgrYiak-pVLXVxgp4-BeojCHshuIc9HusfxGkpxvb3FpuKDTuEJRotNcjc1Q4l0UI7S8dvhFlWitvfNEqTMoz9DO13EehM3mEg1YTptXHXCp6iWN1PYngvlboCUMmcJgS_fU7dwZKWFh8-wNn5fgjmqOkPtTkiFIcziU_eUdyuIN3IbPFQ3Ybr9jGdcwqUI-UwnZ5Yq6tio2u7PqDKaggJpV-PxFW92N2bMtLam1MDfxNe3ATnZs0KToZJ0EYnesRz_GSkv1NFWkCFCB3bxRL6XJnxJzF9ATpwzI_MDdbaOGGrM8q9bDWB8BdYZxQ796g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=YEOHdLMVPtOYw3J_5YPdxn-Gv_SFUFocUTead4paxlJGZnTIUZV_hd1LI9wNVEaKNoN4gm3gWtJ4cppuv8BUVDoGelkv7IjFGqQiNpguBEnw4Ut7g-q7tQEfJkUKWQyTL5jZECN9R1DWNqf2W-m-lqWgu64xR_w2IeqNujmzqOg8E77WWbpuSUUQL9KLjZidEWAPqRsVL7aJ-P3hMr0sCeLuZKZvRsSfRe8zfqAyf76VHo7sUY_VzIZ5_aoAK7TvhZpTr0GrFHOLuSocKADvoQZSoI_--UyZ6W1jvoJ8UQ2O6lDo8F0zwst55t3ABxnCGemJSaEJ3wpxXwKYm1kVOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=YEOHdLMVPtOYw3J_5YPdxn-Gv_SFUFocUTead4paxlJGZnTIUZV_hd1LI9wNVEaKNoN4gm3gWtJ4cppuv8BUVDoGelkv7IjFGqQiNpguBEnw4Ut7g-q7tQEfJkUKWQyTL5jZECN9R1DWNqf2W-m-lqWgu64xR_w2IeqNujmzqOg8E77WWbpuSUUQL9KLjZidEWAPqRsVL7aJ-P3hMr0sCeLuZKZvRsSfRe8zfqAyf76VHo7sUY_VzIZ5_aoAK7TvhZpTr0GrFHOLuSocKADvoQZSoI_--UyZ6W1jvoJ8UQ2O6lDo8F0zwst55t3ABxnCGemJSaEJ3wpxXwKYm1kVOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=q57YD4nwooRYNVQfjQxDucVMOS15EqC4OVGlpedKA2F2UxnYu0byFUA6qI6G9U9FEcDcmQl3xL6A_NHnu_D21GvuFr_GByZcLK_QMWfZ-mfpctpyaa-U9Gm8kVPKTpkiM2SSK_OP4wzReJrmIG_Msa2_v_05PWuCjZ6wGGcua0ztX-stI6Gbf-CkbH7jh-gwTC3o-bNmHNEh5SHmLsNCrJD8vRjZ90yBeVm3QU0e5dNTQhCl1fKyBKIa1-n0kQ-sVcmPu3E15OwAmVXzIaPoNLLYram4NmXHn5W7X-hVn978t3HoVm9rnzmdwKLdWGw9MGbX7sISckjXUFjAOKK7cQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=q57YD4nwooRYNVQfjQxDucVMOS15EqC4OVGlpedKA2F2UxnYu0byFUA6qI6G9U9FEcDcmQl3xL6A_NHnu_D21GvuFr_GByZcLK_QMWfZ-mfpctpyaa-U9Gm8kVPKTpkiM2SSK_OP4wzReJrmIG_Msa2_v_05PWuCjZ6wGGcua0ztX-stI6Gbf-CkbH7jh-gwTC3o-bNmHNEh5SHmLsNCrJD8vRjZ90yBeVm3QU0e5dNTQhCl1fKyBKIa1-n0kQ-sVcmPu3E15OwAmVXzIaPoNLLYram4NmXHn5W7X-hVn978t3HoVm9rnzmdwKLdWGw9MGbX7sISckjXUFjAOKK7cQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2_E1AQlneS_cWCRrq5Y3jwFiXuG4ui0Ii9_08ZKYtz09YbS_WJfTwlPc123MLJOdhhH_uC-OdHKggpLPBVwb53aVYVMVEBbupRct10rGikUu_egMhVBeY6Em2KRvNLN6ezMyc4cWaC9i_MxVYMpSkLayYAHulZRfai4ia-sc2bpX_C5ECLJElMpv0na-g_yK-IXmaFsCEPMC-nlvTYLcWtTKq-C_bS-OPNjqo12ju_R6nRN9k0cYz4yyM6zZdi5keXtqS5peHUOYvI2bMIJJ7uSOObqEq4hxrYxJwfmYDhpC28kK_jNsQME_sjEe4kgWMDPvxMKozXYX_KQ2tif7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUv5anB2qfc-brRh1IVJenxVNXBR0sZCsS_HQO5fDdRmfS3qbRGp8xsjEf9Uje5nBbcXkC-QdgDT5oHzh94KGeFdXLTJhJUO7yOT48zlcgCBEJdFxKmbzPLPMT4f91Se-3Pxl4zLbStIjl3sROPy4gDLxY2Ji1oTx81YlzciaS6Kjm1B_sqLI_bHtYm-5M6GVKX-iAjZD8qsuPR05UFej5AAOGArjArlLCmiIMfcGvInvBRZmcUYzDNd98S7O2yy20QFX9oTOhwtBJcmJsNQHa4rBEB8PMp4Z5J_LZxafM2YCH8__zbDb_rWZTuZhYe6o0Bok-mCja1U9qPhTmi8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcZi7B3J4v_54mMLaMeLbmyvCkRt4gactRhXoIeiHZ-AsCFJntWeBWWD1teE-raiff6dcsGETLsCRrIJiuJHzZex102YF0xsErP7Z9AoGBxeX3d892LEiEAAPHH3fpnF6ftl4I57kpboD-Nc__bQBfFKYQ_XiXuhEBJjoZMeYHsLXpD0c3QY5GoE5zJlm5fP-FHcR_xZky1Nqen4CRU6CmucOc-YqyeeZhaDdHMDOxGJ29W0RE_tp8SQW0F5eNwSzYxVKKT2yCWcNnXVkCxe4ZhTuajsrltArbYh-HSEBLH6uNdX97-xuyFvm1BW-iBDJNuLrltHtwoE_JQpUxwjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDV3RgDs8RBKdPKdVlP09jUI7ILHH8KMVZux3BG8vIykVG5gQ7mhNrSrnQAvwXsH1_3FRG6lf5r7djnM3fPSevIGECIzS7fRODdgM3AwJRtYURSu9R5e1B3qq0D9ugDgikCaat5EzXwqEP7a46bJWd2kcOTllROYhO1PgeFBeEimiqkxt46FTSCV-2ukEKzTiMUpGKVt3qe1e57xa3rnj8eo2qGcSHm_rVAtGiLh1GhIBj-rbAxmd3FSq81fqwCYsZe-_826aJe2hzYDHIJVZPN5GkABCBDAiPtnL3eabWF4oBY1w_Z_0OsiH91UdAe1cmFNyfTF89t41peUMR9jiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5ww8_WuL8X9ZhffIX0cANU8Cql2x2M8EdHjpfp1PK1Lpormagvsmzkx_OKL2-m0SM3Oh00hE-XWkx5HL_1twwI7olFv4q3Fh7JH28bEcFTNtf0_5b-XZkOtpndhlrUY5aEbRCY_n_9qe4xiS20OzKMlruOWUCKe0IdfP2RQef0GfpV6vCY5hHT8rZ54zfuko9dOwmovbUKWJiC1HKVJESI-PFE8hVSEoUfmBzaNel7tCQ9z_5DaGFosWAAZkA_89eoCNWxhvW8QgafENkSMZZrZP0HZ5v7vqXUOO-XV_wbaB9PbuBv9zIhxTHWXmquwvqwub20bqYRsWpVwj7lHJDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5ww8_WuL8X9ZhffIX0cANU8Cql2x2M8EdHjpfp1PK1Lpormagvsmzkx_OKL2-m0SM3Oh00hE-XWkx5HL_1twwI7olFv4q3Fh7JH28bEcFTNtf0_5b-XZkOtpndhlrUY5aEbRCY_n_9qe4xiS20OzKMlruOWUCKe0IdfP2RQef0GfpV6vCY5hHT8rZ54zfuko9dOwmovbUKWJiC1HKVJESI-PFE8hVSEoUfmBzaNel7tCQ9z_5DaGFosWAAZkA_89eoCNWxhvW8QgafENkSMZZrZP0HZ5v7vqXUOO-XV_wbaB9PbuBv9zIhxTHWXmquwvqwub20bqYRsWpVwj7lHJDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tvUDSkJUYjFB9PUyVo4gQ9r1eCfgf3rzcFCsJ2fPssstAblgKdX8H7KWBdfUmjl2MrJNs076Tb2H9zcdkzNMhqLP9FTu0Qz-CAyvwMQb_RvezuXdtMUE1hmehazQhQrVd0qcaxpCJpdqCSrOaIPpuJ0nfbfyY_avBl0fs5dS4rZlx0kri8DSTTxXASvXFV3AO6-Q2QFOwjitr4uF0YgkHIxpIcvmo9y0jq48Yl21fxkY8g7cIh_IigdsMDz449oClfRY10fK-GTgjeLTtmhZHnwe0kqLWK5on06cd4pahObqKVgWEuym46s2WCdd_idFsI2MpMos7lHKqzWtB1ImjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zj9lCv7Pb5iqnQjoahkiqkhJrh6bYhJ7O_X0kyKrnSG6SsZhEH2WuPq0uMQIqn4yijbZTZxgy94sza67uhUq6zakvTM0rNz9UFLd2bE_NdQt2pD5p1xbjasr4pt4ozJdoO8aG6M5WxYcr3-UVmMMx_Zc_kCVBy67sP9dv8LaK8Os-feDr6i3kCKQ0ARnggROSfn4gVkEffHUR0KLkS1HnEsGju9gGu-NAPREsqTMR7CrOveGZu1cInCs0VAJGIt1KmID8fiwu6fP3SMfsfb61z0r7O_phtd1_qSg5m_D5Bd1UNcBk1dHjBdIu_YFm8354MUKrRzzDOiF9tvtctn2QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=LC6bfQMI9z6YIs9gGCilkIHlevYjW4wSjk9kiwubfMNTM1a83g0sB9gjchxCTv1gQaQ6280aQdcYbVCYA62oMhNqzBC1K1cOfpV3rPCPCz9EVteurwfxXTIVP8FViejBhEXZeW1xNqQUdGZXlKcvxcl4Jlol3RyCdB5PwVCFwFGqtKYPNHVrEF4lS456Te6iAPq8GCBBCdukG9UfrRFxBt97HbTsiZyWE77LHrUXnUnM-nJ-M0KIT_MdO-fH8DuyKrmhBSILt4JNngHD_FMrPsxS35_QOLHzZbr_vqm1_z5wW1-PO5OuPovBV1ub2vNvTnbrhulgGE-Oq_fI7mqTOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=LC6bfQMI9z6YIs9gGCilkIHlevYjW4wSjk9kiwubfMNTM1a83g0sB9gjchxCTv1gQaQ6280aQdcYbVCYA62oMhNqzBC1K1cOfpV3rPCPCz9EVteurwfxXTIVP8FViejBhEXZeW1xNqQUdGZXlKcvxcl4Jlol3RyCdB5PwVCFwFGqtKYPNHVrEF4lS456Te6iAPq8GCBBCdukG9UfrRFxBt97HbTsiZyWE77LHrUXnUnM-nJ-M0KIT_MdO-fH8DuyKrmhBSILt4JNngHD_FMrPsxS35_QOLHzZbr_vqm1_z5wW1-PO5OuPovBV1ub2vNvTnbrhulgGE-Oq_fI7mqTOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CSNlzu5N7paAdHf8pOg3_QFUXAC0ywaG9izwf8qpja9kEhc9R9X4c8iA7AVdmD4obj55xnqQY0IoniMLSlMI-ibQkYcNuT3GOuV7Kdwsbl6FwsE0wuVssvdip_uiWTjLajpOan8wgIIs1uii3_EBoWNzMqr8EesPBok7eOXEg9B8ZXLGgg3f50OIOYXqiX8aXX8FUlCpNpr-WZ-R2d7gCxsRUCCZ1R1y1-fAYHeDn6GNZG6O6siT9upFlQvdCFTjCQ1ljGiSbzL3cpjxZWzfFrfdyLrm3vUb3MRTEXX28aocELGwSU2f5dYOCRTbEHc2FvAq_0jDLL_lg2UblMKvXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CSNlzu5N7paAdHf8pOg3_QFUXAC0ywaG9izwf8qpja9kEhc9R9X4c8iA7AVdmD4obj55xnqQY0IoniMLSlMI-ibQkYcNuT3GOuV7Kdwsbl6FwsE0wuVssvdip_uiWTjLajpOan8wgIIs1uii3_EBoWNzMqr8EesPBok7eOXEg9B8ZXLGgg3f50OIOYXqiX8aXX8FUlCpNpr-WZ-R2d7gCxsRUCCZ1R1y1-fAYHeDn6GNZG6O6siT9upFlQvdCFTjCQ1ljGiSbzL3cpjxZWzfFrfdyLrm3vUb3MRTEXX28aocELGwSU2f5dYOCRTbEHc2FvAq_0jDLL_lg2UblMKvXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwWG8butmcA7Un8dxqT5BmSqiRMG-fXFvlbSoJ3lZA67h3z-la47jVmI3b4iHFm0lmGEpj-Uqg2-mk-epDxxG2J0OAIu5GrCSftFDaBCBeZp9Meqv5nDnFfIvaGgwsTUAb-LhqC1lp4fNzhJB_XXe8cEC-lms-wqTs1Wie_R_IkVIUpXjvebsLGDvaRu2ZBjP02zKavSWEuxLWNKqDhwuCqZ4hknVLWIC0U7OeiJl8KmMg27W6uaetsKukc7kKE2_5hVL_KND-_iOo1UhqqkOTzsHdxRY6d90GHe9SXMpanrlXXxYBH2bkA-mWSSAUvDjP_WV-onrt38ay-CELUpTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNDrZoz6Flc-0mmzWX2iZzXwFf5BMI9xdnLzvu51GHirqv5Ji3ohGOkp9qs5LDdFA5pF2BGBE8UalNaHeQGPHsYCHgTbSo-vv_TDSrKt3P-IvwRFlyoXvS2V2HMV060dxovL_jYHwrfvqaB0Xut1J0Q8nEHK7Ly74IIt1eNgNCL10T2dkKLcEq_IyZH7YwuBn0vG6-6uELz54EMOh7F3PjpV6RrSQXY-jlTMq_SG6A6hN5NJMBLiSB9vMpjsJsbfxXJMm7mhkkjT0g8n6fZgRgXieeGxReUNUCYYHoiZVv_Wn5B5sQqHbnTTgTLA45vR0B6dXsdfNUzGlqpWCkMCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=h1MKzmks1XzjU7B6A4zXit-8fU3w6KaQgfsEKTg8KwOUNnpBrEoU97NMkfezJLBYDa-mIWFBQE3arG-Lh7z11syu2P2lJxHWZxwtHW2R7wN3iyHOmSmYySXvDycQPG3nHQw9Oy0C600zLVIbRim8od0lIwzpmqYdaNVmKWrmFDQundLbZNI48O27lmimzGyKwPXwUZ7pRr1qJjY9jei0bBkzq2j5QQpob4a5BCZBfLsQrmE-pV6Fdhe8EGzNEFEnhxd8CcUlNkfMMvzSDoIMTdHYeLx_vM_qX2SZGSswsaMRyaYG-2GcMXhd7nTrGnxrBeGdHqrCU-3pv7wzDenZvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=h1MKzmks1XzjU7B6A4zXit-8fU3w6KaQgfsEKTg8KwOUNnpBrEoU97NMkfezJLBYDa-mIWFBQE3arG-Lh7z11syu2P2lJxHWZxwtHW2R7wN3iyHOmSmYySXvDycQPG3nHQw9Oy0C600zLVIbRim8od0lIwzpmqYdaNVmKWrmFDQundLbZNI48O27lmimzGyKwPXwUZ7pRr1qJjY9jei0bBkzq2j5QQpob4a5BCZBfLsQrmE-pV6Fdhe8EGzNEFEnhxd8CcUlNkfMMvzSDoIMTdHYeLx_vM_qX2SZGSswsaMRyaYG-2GcMXhd7nTrGnxrBeGdHqrCU-3pv7wzDenZvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=pJWlU89LOLyAuR-KPJmLjsv5qd_HqTgE802sWQp64ypaQIQXZJ4Ii361veQbSZF9UlUg4WDDerB6O38Jy54oq87R8jgggO1gKltcgz64XNuycVY8L6UdEt4jaIIst7ac0lW9TLNSNlDPn7pJhMsbeUt9gANdNQYG1ZEYkRBOfCqBE2CPzRnftoL6vG-EkSkbbm3Pf6kwknTXdbDEADpAqCkGlZ8bpu8lxOD0dWeI2xoP9omWxk8au9oB-GbHtuxhOSkM-tINEl-4x8nM9CmlLwc6S5hhWRBz-DoeQIkCsg_Bx6tXS59khexuYZEKHMmOcBT0O28CdAyHs-PonN777g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=pJWlU89LOLyAuR-KPJmLjsv5qd_HqTgE802sWQp64ypaQIQXZJ4Ii361veQbSZF9UlUg4WDDerB6O38Jy54oq87R8jgggO1gKltcgz64XNuycVY8L6UdEt4jaIIst7ac0lW9TLNSNlDPn7pJhMsbeUt9gANdNQYG1ZEYkRBOfCqBE2CPzRnftoL6vG-EkSkbbm3Pf6kwknTXdbDEADpAqCkGlZ8bpu8lxOD0dWeI2xoP9omWxk8au9oB-GbHtuxhOSkM-tINEl-4x8nM9CmlLwc6S5hhWRBz-DoeQIkCsg_Bx6tXS59khexuYZEKHMmOcBT0O28CdAyHs-PonN777g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkeU6dXO4Yl-omwNQLvKFTc8HEwGh4AQtibGnEp46pCYk9vSqSY22CvF0bNyeE4aqE3YgbuR7NzHCpEMgxsIK9WgaWDEPCrM_33orJ6DSmo_uRLZTIjw1iNkmYCRyRaeayCjRuQsBlvTjU3W-7IdPn_TSQCvb64ECrRPT7JK4mAgZ1sFp0AME1r-kh5Z33NNY_f_VwcTjAEko9tWOeIQuFclnY_oBKLkMYHCdHx3ohH154dd-1Jkqpm_YxZlkCPtKkjOV6fO-K8hVI5LZ6V1YUxtHVX1KosOf-XVacPEuWs7cBq7GxOOZFxCP61-JGxc1kku1xdIZBb6lif-3ukvWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_yCE5-SrDljGb2UGuUspDMhTkJ8ppOiDxA_pRxu7ruBZuVMVhotacAcXH7ZouN9GcA8JHfqBeS9qBewWkAwj05Y93oMJeAYYRViYzYS9Z112EZdaGRNyEjRLNcS_ZsyISu0UCurarTUC-M1iK0t2jqqtjL_mw6ceAqxa4FvV77jbKKLRdFzFYFvR5Ae9yqPqSuJpyFw5HnEJ1NXZDqJEoqFD_AhbTeAGwfMbms8-85wcJFFe8kgk9qLYMvhnd9g1zxNH8Af9-ukZHL0gc1ugCpIqRgjtroXLQMQS3SUM0U3GcyheestzX8cxoyoqpTYedeqA1BDJRsKYIN_DiwuCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8W9BlBKDUNcHou6ECK2U57wEf9Gqe5lJYPJx1WdKJrNvxpW6h-96BD7FQXCj2h4R6Ka25-xFWq6oJbEfeHHfwF8Y0oFTJwZsjfDyBAzU_ar8teeLUKGSlHHCvBNPSW7Z1lodz8E4kS53Ab4uua3HJmelig47-Qi1NbF8TosJCfWsyaA0S1Bj7_DolLT27ImzhUc88X_e0faBEDkknEAwyyBdsFzkoyLc57nMmX4nrxI05Nh_96BaH_T2DRZ4JIF0pliWhMHAm2aIQ57f_MDRH4gEBzKDMvYpF1bZ_8ZyYet5qPCud3vyrR_jSCZ72wcvLiNhwQLqyRp7P3WPTZKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUzd2hgmIkYFDtlEC5RU5NTwOWttg3sZCOh8VTNw4Q9m2U2tL2VFhfeWSdb32iEouMdhG4dunC2QZgdcbiu9kpoLoOKgG3ylR4Vt_2nS_NW3DIrFF5vcnqseQ3BpmrlNQtAJ5sBSpkziXyCvd09LZlLusjP95NVQM2I6r3eRtcLG5v02yEATOM08FUimLX33DXLNgt5djJmJnA1HLeSDFmrtLh8fiQEPwjxnNvKk6v2EYVJK-9agbmfKWcmC-kaePFjtWj4UeaENDqpxWFR8_4-yfPlSY-ViSI9kLCWe4rv5ROHCqHrq-csPSXRtlLBZetDWYUb1-UFHOkh0ZifB3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJo2F8fqJA3LVRR5V2rKM2cwRx5zX_diDOn7vOqgLTcPXyRbZfVNkzGW_fjc4P2k0F1P7MpGGZ325I9ROygNTO1EgfTQOgmJ6uN0gRli7PrqAhCMZlT7iVPbq8EjQppXpcejYs7IRlZgHlmwn84iD3ioxw2mNUW933q1yMChMCJWN3E4TziCzRwK-k0jUwfjhxja9vHAP4mtFtIuEosNc91Qd0DQpr_Q0wBl4FqSgNsf4_olhJR1sRBUGwjWqKBlqCPCSkTNNAZO5_UtvYTgxc7q7rAWzRf38trXFlNM3JdioUZr9Au2oSwxuen_71idgy-1tQr7mzdTOFUssMefXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmUSsb_LWSgCFQrdAOmmUCr1AUJAy3V1C-dzh0_B1jyID3bfp6GUlGi_O7Kd90pkWxOsTuPVC1xi1jwkzbMs1E2WVQGqSl-iwrHNUjl5PsXteHrJNxIYaDQWFvRFeJzaFC_x1CjsXrmomBrikbJB6akEAwUeYpOcj-L3DZ1gfKt_dZy2pXw7E8B46eVJXfJPHWvxlddcj8dloX4FBf0ZSGEHFUrvBJQIfeI-t5grRnOTS6uAlAdzP3-l7lHAvy14dbA0HmX1pAJBcoCgIelu8KWTSAR_raa5tFxajaXgBD9k77DCX-cSBut-jMPNRig6pj9wgvTYcUUkjOHyhhuXDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0F2L4Kn8m2wD8IezR0MkI-IS_Mf7dXPXMZT6zFN-5-OhgLobuztB_kSaUP1oBJOio4PsBLN9EuPMCk61qcOgBC-KwMq_JPUTPaZRZJCYpDkxvPdyKH1cB8Fyd0LQMOv2X2zi5i4x5VFopr9pow4UXie0FDDowf4wPj6p5Uy9V8vnBQ6jsGIOpP5rexlBrx4VFP5hSl0VmcLxg97lM_f6VFps8NSM_vjmC22RumvBR7ut9gAKy5xm1uMFO8-rrsylpWNB7d81dhsuJq070YAVQs2WdAQ8ORjlLef6XdxjNYudtCoCHOMmCqg8kj2rVWGFZmbl59ysz4_pO4X15wdhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8W-CBqxhFOmFt6acXOL1HqLnhsu1QKPSDHJBrZCsFA1C6LgX4H2VHuBogJt0rUjZkmjpoaMbTkpbMghb8S-d2YB95drv8_ipnYMY4Mc0arXp9KQjHfD1rH4stsGAgtdimgAD0X5tZVnkGs1uuo0SP2RTcFVz22YLc37EraQwpUppyMKOFwJu2s41QR3hLGKj6bsSWVP8DS6xB7U-sukX4kIXXq0FqWftJ-4_BAjHfA0hvq29H6WRImEyLI5cJBqxuQvwCHSLHzYsHxeNqaZXm7curt0K5dhTIn24iesgy57BMDN0qnWZVmE9mKLtPdPvRggwfyjiLaHBemWsAkYLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SE6j-kgp3AUicu_QemZxo0HjuFd-cB3r4fiJVccy5gbaIPLjK0nq6czcqa9ZvEUax_vIb3OvrRm1PEt8q3rXyiwxDbNx2dP4QrZPYTaTJt7Q36qpZtB71DxiBIm7AQUFNrZpM6WmtVC3bXAAqHgrbDfQKfZ-X76DPgyy7Ueo0r1j9LZDd3up32dFloX9YafECfybmszB4xsBziwCLC8-khP1M7-nbKQd_wWrpIwTCcAROXBEd58onagpAEQGVyYZ9uOpB9ns0GUQUBTNcCQTAzItS0XzOZh7Vx3LUTpP9f01aCs6Pj28Tgcex7OnIjRbWnoZNT_JnYKNlhzcOT-Lyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl3O2fZ3NwCddmA5snsyA-_XH3hrDloSL20yV1o09GJKrEKSTSH-jMnj8K1rmjWWQV53Lz0Mu7mo6DxhGSjbR6ks37GPeQYMPb3pIU-7dQjzeIev0JJqjiQpbytXIgf6Lt0cPOrrQF5RXZNUWlUwh1_nOrLbxS6_XR_Bsi_MtKJdFQF6A1K5EopYv_pgeakKiWTEx7BHK08Jz0M7cJWymVYWP91F996xoFCYgNJUVy6F07ONq_uUw-va8xRBJm3B5qHUlXWg6HvGe_DsVd1pRu129Ud7TkYclVzr4AFEoqBnktahqZ80LvkX2EH8ohGaO7C06GVkldXNvl5qTSU1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=VUl3GxhYDWKGBMuCVos5XRH_9OFb0FustrnVoO3PAcMod9n5Ld61Q0HxwM2Oc8OsuCf5Y0NthoJ0uzADm_UvS-UdnabAo1V1lPD4oUl8SyKi2r6yjp6_5hXcZoZCs2nJjf8n21jAf64OqleVymE-wDWraziUb7mGUwvXaHRrT1EML_aGZeeJFTmyY0LoEZB6ZpMSoBAKlm4GoDeznITvnyV1Yf_zeL2vMwLFs8VsJKQ8CcjB0SmSEkmjAW6-sc6Y8ei56AqzHQqL3qspiPAVD_dan1odx60MZ1XdB0j0dl2zM3dRwLAuFAOCkSRitZ7LOmUgjLTz3g-SEkpRRSib1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=VUl3GxhYDWKGBMuCVos5XRH_9OFb0FustrnVoO3PAcMod9n5Ld61Q0HxwM2Oc8OsuCf5Y0NthoJ0uzADm_UvS-UdnabAo1V1lPD4oUl8SyKi2r6yjp6_5hXcZoZCs2nJjf8n21jAf64OqleVymE-wDWraziUb7mGUwvXaHRrT1EML_aGZeeJFTmyY0LoEZB6ZpMSoBAKlm4GoDeznITvnyV1Yf_zeL2vMwLFs8VsJKQ8CcjB0SmSEkmjAW6-sc6Y8ei56AqzHQqL3qspiPAVD_dan1odx60MZ1XdB0j0dl2zM3dRwLAuFAOCkSRitZ7LOmUgjLTz3g-SEkpRRSib1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=IKb41FQTjrdqWaBhvItXrMcUQ3bzlB3eCGt2Dym_9iL9-5HGvFzAKHF8SqtsYNQ1sHXCdGwdF6_JH-4xowohdWJjvavfgcpwFaDrgz5ghnqO8IsNJDTZDwtR8TMO3Llri92rG1SaxGQuwFnRI3hh7q3RnbD0tIoCj6_Du4CeC5Xg3RnF4EsO8BgYtOZWNJtuM_MeVahoWJLQg06k5gCFc_5bq4037jr-JX8Ip5xRBWfv0FJhFOKlxsSnW2GnzT1gpbdYp203XDSKAnMLBXfgNJ4xIHDlVKwp8rH3D41uKiXso-uv7XiSUxqsuNf6sDxrV1USvli8WrEkjCVVz5Ileg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=IKb41FQTjrdqWaBhvItXrMcUQ3bzlB3eCGt2Dym_9iL9-5HGvFzAKHF8SqtsYNQ1sHXCdGwdF6_JH-4xowohdWJjvavfgcpwFaDrgz5ghnqO8IsNJDTZDwtR8TMO3Llri92rG1SaxGQuwFnRI3hh7q3RnbD0tIoCj6_Du4CeC5Xg3RnF4EsO8BgYtOZWNJtuM_MeVahoWJLQg06k5gCFc_5bq4037jr-JX8Ip5xRBWfv0FJhFOKlxsSnW2GnzT1gpbdYp203XDSKAnMLBXfgNJ4xIHDlVKwp8rH3D41uKiXso-uv7XiSUxqsuNf6sDxrV1USvli8WrEkjCVVz5Ileg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=kx0PzT0yLB24GiNDcGNn-om0fK84p7bkMwAEyfiNpALWacr-2yl5LhdEBIc9UcKwX9By91hAsmtic7rmrS-voPca-DEHoXpJ-5kk2mxp2G97SzC2DOvWTTiKOH2jeL76jK7I4Q8yrt8j2XUej7R8GA8DCIshanQIlb4lae-bXfp6BKsiYXUsXCKHX4uaKU4Ub2dWIRA7W9o521U2ymGXWomiIZghYvQsf1KLAfj4XpnTqGnt3CGIGdx8-KAjcE4uuy5VdpL4PJZWXZfjGPtBipN2k2KjNEUkDzvmL6_B38qXy7rAzXG9uWkwzA02jBSYxuf4GqNQyNhlE8XjGndOFDBnsb4CdSwM8i2-ePXGIBrYN9sn1WDn89trM-pztr4qFk5Rw2CtbYIX3kgTxLT8YcTUPHz4sPbsH4-kIVa5ISoUlh5BTUrQTVXsJyx5AIKroFKlwoGBVCQRVkKFUcQGdNhnMlDm4ktMSZ78aXpjVemQP1XyrW6IWV7HK1Cgiyms0gp6IKMiepg1K9J7bTltrvsgAAxvnCxG20f79g1xIN5hr0RZd_cmDySiFIjy3QrsDI2bByraygmaGNbjspQzqYR3q9hgz_N_Ze6SSFoZy-52Px7aOh06zGYlBUzVXy7aEk1UIIyTsSuifwW4Ll8ml92vvNPJJ8rYxU9-2mmphiM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=kx0PzT0yLB24GiNDcGNn-om0fK84p7bkMwAEyfiNpALWacr-2yl5LhdEBIc9UcKwX9By91hAsmtic7rmrS-voPca-DEHoXpJ-5kk2mxp2G97SzC2DOvWTTiKOH2jeL76jK7I4Q8yrt8j2XUej7R8GA8DCIshanQIlb4lae-bXfp6BKsiYXUsXCKHX4uaKU4Ub2dWIRA7W9o521U2ymGXWomiIZghYvQsf1KLAfj4XpnTqGnt3CGIGdx8-KAjcE4uuy5VdpL4PJZWXZfjGPtBipN2k2KjNEUkDzvmL6_B38qXy7rAzXG9uWkwzA02jBSYxuf4GqNQyNhlE8XjGndOFDBnsb4CdSwM8i2-ePXGIBrYN9sn1WDn89trM-pztr4qFk5Rw2CtbYIX3kgTxLT8YcTUPHz4sPbsH4-kIVa5ISoUlh5BTUrQTVXsJyx5AIKroFKlwoGBVCQRVkKFUcQGdNhnMlDm4ktMSZ78aXpjVemQP1XyrW6IWV7HK1Cgiyms0gp6IKMiepg1K9J7bTltrvsgAAxvnCxG20f79g1xIN5hr0RZd_cmDySiFIjy3QrsDI2bByraygmaGNbjspQzqYR3q9hgz_N_Ze6SSFoZy-52Px7aOh06zGYlBUzVXy7aEk1UIIyTsSuifwW4Ll8ml92vvNPJJ8rYxU9-2mmphiM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uag5F8Ib1fzgEcajnUMyEwsVuZEgQi_mxgrnrlRNgGbmhuOx-f8BsyE57LqcjvW2U7BDvlCRwwEnoyRnJQm5OgM6UqwF65cphcI5iqGfQ9yDCPpANmRQOR1PMR-2qrlWMJEVISeOH8KdNLFx_j3hlRaY4hLI_ltN_DvZfqEPputxlr0ZWQRY0lG0888AeSWKMc3fHy2Ytq04Tw-avF-h1Ci-p7nn8v2rBOs1C1OPXwPlQG2GV5AWIyiACFnOd0fYiSHB8PxMjzxiAm6AzIGgmraw518pTYVaMUd2VNT5OTYQgd0bcbiauyRLhvStpH04O9HiEVMOSp1pnBxL3hVLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=Cgjtgi2qV82PCqsPJw8GoMdRR3fqTE2XREDzcbJZsDLQWR6iiiVsUK0-3W0Qa3oGTswWrMauQyccAa4ThbF_xf44N89U92gip39ctWJFh2Cu3xUOII2xzvg1WzJlyZFas2k6jK1Wg0A21_BytD5C3MzcKL4adCwmyH-Iiu7eX-S3K4IdUaAIdYgPfokG0WEKTFA9wIEBtZIIcYMqV6JOKsyByQ42LgDsdE1l1zRHvV96gGtkofBlVWcPp8svyc2BYO3b1MqJ_eK03jgdK8t8hm7jO9wIDuzavsbXh7brDkNKlCDYt43N_u967MUuAhCqRBTOZdrPvExoDxh5Xz37TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=Cgjtgi2qV82PCqsPJw8GoMdRR3fqTE2XREDzcbJZsDLQWR6iiiVsUK0-3W0Qa3oGTswWrMauQyccAa4ThbF_xf44N89U92gip39ctWJFh2Cu3xUOII2xzvg1WzJlyZFas2k6jK1Wg0A21_BytD5C3MzcKL4adCwmyH-Iiu7eX-S3K4IdUaAIdYgPfokG0WEKTFA9wIEBtZIIcYMqV6JOKsyByQ42LgDsdE1l1zRHvV96gGtkofBlVWcPp8svyc2BYO3b1MqJ_eK03jgdK8t8hm7jO9wIDuzavsbXh7brDkNKlCDYt43N_u967MUuAhCqRBTOZdrPvExoDxh5Xz37TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FewRzo1LEl6fykkPq3Dwc8CJ8RPAisrm0mm8BAtio0YizdLsQ_7bCPtDhd8b6dU51N89cRno_mAq5OWlZKF3_OFLRTLmBRJ9KLwX7aHa94UTn-N-bNsF34rJO1gOSwQF4E-GpjWSIIJLleCgbZZ4KIhfqIlzoINgcBzIb3bo1xL85JbvJ4DJluDUlxH-X2ZXrhJ06W5Wsyn2RNwJrkHpe8-pvgKXqGLcZ7C9mQ0pNpBA1WbezpuP8FWvNDPpBuZlKgzEYAccrxNWxoKgm26rB8cHgmmn7jp1h4SlHZfLZSa6BBWnznIKvA2qygreGVBA0TX0F_o-hrwxkHdiojpr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjIeERby8zboEpOWpioh1G1roQSh6vLV33FpzfpPDPukk7tk1h92_QFIx6higc26hHwOD0Zc-EzQCgL8V2uQobsksWvJyMlgslXTC8jpT7tnGS_xI-jXTda8iXxQgEfPwy1pJ1bSdNXExCY9e44C5MsAhT75aW-RkCYeCrZYIahUkc1fNB9u_MAYZCqBrSo5KeVu6Na0vrEW57QxHvkrAH1adZh_4TKpcNIyFsFH9w0gpyLy2Dd0cIcdGQibtjY_Nslk-eyJFoAqNshJEXAU2cmC6qPzyzB_neptPHKNS6JIqjP7aDzM-Z-JoO4c2V7z2ix5F5DTBova8WfF4Pb9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_DmB3evcKTXpMqXxQT2UNbCOfy1s9I_ujP9nx0SOLBUNrX_u2ODYBUjLvBeRH3wKlL-p6vBYI1dW-PnUPHuCamMKS0dzb5qE9xtzJeQRmwddF-z7W1kHhEPROVXcs4OnYv6AoKykvTS4WtsGe3epNKG4Hk0UAnEkab4lG7u3pK-5v4BuuazoVAZaAdWVoC9pri9dFsNAKYn14rVDM9J_5U_LSFGFxiCD7Gu6vPDCp6yBXgFXXZdtonIzflDld24KU-azJWrCBT0kaqrkeI0Qxfoka2pc61OsW-4Fj-1P1iS64cQ5AU4OjhM95wZoBrzjokAnSjpjU7CXRyzEIbq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxFcvicrNIeRLR4QrDJApNqTRPcij1BZ4WujeEYEc4l8BABVVHA4rpv0h0KXq9VHDaKPNkODjstHd4ly9jTw1oGGUNdwql8qC3Qy8hF2H525CfWq9iSgGZuYuxV6MMwqdLzJJV3dZbqTOQRz4ulxWL-xHmT2w1zITwEPSYEI469oOJYX8YQ0BxMMMlTqFMrE8umn8I6gbN8xDQfb-JZJm3gA7qJM3s_TwT4WVnVNfRFmQIy0VMwPX9KNcI3SvfSwWF9Nxjo8mbxl7T9dzr-efKSlcY5HmrmebHu_dRQlIzTgCL7uL016q7kC9n2bUAA4ApCNKweuHlfjxloCFjFUdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdYZKjBc9aKYUC9E7klZePyBTaleda6FKhHHoDGCFmUlKRj2HfEonPTW7k0K5OjflKjW4P_bbu4n-tEXiqy-c5h0fAc03TXiCkiXlXvbZ4vTpVRVqwvCgpTyWT6fQoZ46YATrl6vLLPn6B4UMOmBzkDOZRfUxscDLv8gunVPw6YtKaVkDAPi5Gt8OOvkPte0LUqT4utbJXRNQZYM1U2D-ymIXAyIVLPTvVIbilJEaqu80eehggz33qXDZL-MapkASesN1ohG9qwd8jb6gWbyZBGldJwYqdSAmIpmZXr_GIl1mRvkglFhIWmFApwyTvQhdrxm0rK-L4xLhlg53GaJIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvrAMUdKPW-_-ML5_l49yatq46Fh5DruE_6rvMnvh3Pt5XBq7KfxD7DA-Q05OSEEpOM7nuVYsZ3mX36XW_72RWnO9WRDcHwWfdBNcHLyOwQCxgoUbJlgeArI1XdbvQWo47DjYZZc190CWKUuUDysK1_nUncXmJbImvnjZM0p43bKEJydWN11VzD760dBaHwNXym23OzX4_BUZPry0hxQO9brDH6YXtFKTRo-IpZRDyJ_f8SO_WD2f8jiIX0Wla8FLgnWCHLVDpyZZkXOzpbG_WkKSdamasCGBXyxTHNzc4QRqEAwQg6f0O_fykbmF727P8niwxbcpcc7GlVEoKK0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FgpPHBiqjpOhBY8_j-WKa7B7TA8pIy6OIFlyNsmQYaAv7Yt0uPkwjKVxgwGBATxeyHpzyKwD5jCrba8fHNG7xlxcab6H1ZDTI-UE7lxC7vgDyb-RAaPcrYO_tuRbYNmZK1Wn1tdhigRkfRRItYue2zdTSJYOXTAdZiyuiM1lX96hxzi7aZ1gb3Uc4zqz0yJnfJ9Y2LUYofOZrb4qGiAczzIMlrB0AcWg4HPGgdzwGqmA4VknBQC9mRyniW7NZNmr_mPVHP2HyY6tgC7A7B1q6eo_uiqvteK2-_giITZIIuBivMqKeVKJx0OTlapTAXtNcsa30vr9I-UU3kauWOdagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzLkrL4ecOKh4KwnWyzllf6G6TRZoJKC0rQwZps12lnOJ3vnnFfmRrnXI2otlNgF_CoM-HqE63lL9m2LCO5WouErEfTgIibDp5AUc4nAo-iF-KwpybqDoFkqhB6Ln9lEX-YvFTKZ74nq7a1avbTnaTLyP5acQvDCCxbamQtMv2UkGp0NGtJVq62EYzud2kY_X1qEmmjSfdk85ipwGQqcbgb9cgfpxUUCXFMy4eIkTWXDprHyd1DureNSzlbvENSWnxOPU6zNYDTA2wuroumOEPqir6vFo1Qw-hqyBm9LFVcPDWljPCNWxUbMcxXhV_9QgxDWlZlGV5waN08MKIKGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMi0cOZfrbGeSfit_NwA8g0JzOWKwzsKxUkNB_7TRcR-gT4wBUEefb0VcaEJl45ZoLbqwhpDLvbGBRMxmjTT5kQna8hGmRr1g8NK_0xjTIkwwqSUSMHhRQKZw-x86SPO2P5VI6fbs2nwc1u5sQJ9d__4wR9hDWi_smm1kwVS43KN_neiDbxW7AuUFzjZOuWxTerN3Yww7-_kUNUDSBO-6OuMVm8JhHP5DBcQZkHPJxtQKBU1lF_ai7bg4tycdW26u62VgxFDnohTkCx_ZHyxtiswo1QMYo6MFwaYz_FI9xksmx7rQm7BVvQhOW6-tXs4db6t-SCwWvi5JnJ68YYAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JsYJm66PIIim9ajLO1KsfrFfI5gfAMlWv53oUxwnMg5XaaV0SZi0Yzcqq-JlAdG8k76pStVsYNLx_6r5vi69N2khV5wNqSUvDzYMsKw7tWbHAbOeSl1QR9LTQyeSucSfBE62x8_sgxq-XaxAZX51dYnDSIcqlQiWqUZxMQ1-8xQf1nRDjZb41shNcyfHsJfvhmN4SyzivktUR60ieqlPCpgsWpiYOnmzUtMpMfJnF9Xzd7lTp86UCeSgVgk6akcjylh5wdPAjFVOu4fAs4juq_HyEl34KEZtQiKTy3BRSCmUpYm-S78sUmarUJA1tmc6Cf5xHkvB0THItuuVnuezBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx0l_PyYUTnafAlrzHoRy50nDFUj7-Pn-3enXpV1l4WZPXupKsAjnt_dAVAkEDk1fgJopz9-RiVWlaXSCr7aXjk78KLGdqY6EjenBU9oQZCAWM8jAQCioxBIIDv55lnoiU5oxkqsUeRSjlrG5yPTLPDyV5nbA4YbigrBY6tbHVj_63Gnak1DErPWToDTvWhb-hrNUfZDdhk3Add8rK8-5REkuKKK2yTfwaLN9OVOMiafnzrLwRTGNdnLJhesKO9dFdDHmRU3zCl3j2z1mRfTqWU_8pxRbImMURSADAgK3dbvSFn-cKWblAee2ghcYUoMxsYjuTdyLruEWc4oE8hDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maPdENB-Vp53d9AwtOjJ3OS6tRqG5ttOmTEF2R3K6pJgLZgV50RCiiLXCCTswWW1pOliFisPowaq2gqIATwqN6xXLrNsgX6bmznijbQ6IPxv6IriIv0tHT8n6vxd-TQsNdt4fP07vkcjKp4yI4NZF6aGz0r9ewqHCplcPH2fzyGf1FA54XC4HTc3ccA9Q5bgesnFK2YFzNQJkJYjS9wUPgnSXmYnRVOtlIOjyGBnp8JBWaAf70pJm5GfDWpgQdB-SgNqCDlrOtjyMAh3Kr8_UDp4NkHXR_bBB6Ox0onkgmxCOKYTTBMilVodiJU0bxHCzmfqVsJdjwSpDmWswM42Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3ZfkrBftvJpix5PTv3pWZRPGm6Ur9vDEkQoWNCMXH7MonU64cJXc4KD2qcaxr_4AR7PR_VEwESNm5AJhxXZ3RpBy8-Wegazlur-3TRwPAHwwicwtinP9BJCHebDm5UV1Nsyve-oA4rgZpk6mvtdclrygyuXJoVvKjVhGq8r5EhtaUuSxTwRU76-bbKgFUfa_0GjMgtkYaYBChY7-X6Q3l-qdMHO3i15xboivy5dHVSndZrBiR_1tmSzibnnjfiIWcgbVFCstVFOAXfBmvmHsMF08wi38R9IuwyTeWJfPw9bQTL-T6AkgkCkbcz82ekkuDxafSKF7srcLpGyHD1YfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3VIEpNFNigZd--oF2ykZrzy2xDWWZlnhG7A5cN0fiyQXrwqtqhT7u48ZYOxRSjCvPF7L9HznTLukwVsCIADnK9lIonA9xgaRwgoE8forKCxZMeKsQhLAY-uROvku5JavRazq-IL6S8Fvj5G55A_24CCPmkyEamzrtX8GXLTsUmmKXSdwsG70xWSdm92hYV8td2FpD7CNMkNgibtJp_j1bxcdhED_qS144cbMo-QLV5K054MAoCdZ7j9aPO3V9DjjAld6mKIsJphSTWo653fDPqv1YMoZzUxPUBxQaPfX_D3dfTyKHfowCRf1HI9NRgmiejlhF70DVJhc-_PnWrGWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXq69u4BfR5aHubvBHZMWUVJnZ2pIZ_7ZA_E5DsyOauytjWwVbJksxtl2TRVcvWvvZY0cFlOTwo6Gz-fmiuzMNpWnF6jmXT2iUdf7cZqES-7yyE9eA4FJtPg_xC-PI9bJKF6QVJkb6b2g51AMQ6SFIUxnZpN4D9i73zkbiqG2r3260aiVrL_CZ8SxdHvEDpvLTAP6Etk28fGsTeT429R-ZuHgBr7FJNJAVYU0HxUQtdY1v96m-zAhclhOsr46eM5zq7CbGk7x3B7vLCNDNxro2-2y14r_WszbPQ1KQ79h9Q0g2KvScN3JLiLMfFf-3vXxcI0rnZQkrvT5JZYKRC5dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7LCzcFWHN0GhubIckCNFhw_0k64G8guNFxzF6_JASi_ZIFaOHxUju0_P4ijlwmMNmY_tCgmvxMTVpdiDMv-N9slaOK9L8AzD9pR_9D7VTKLEmkYYDenqoatIo6PB4USz3TCBQlkK7p851MAl2wqdddgHO4pLKjd__G_cSH2x2KzDNsCOUa43E2CvlEuaLpAFT2dd9CVVaS2EhOmzvm0dUx1ULaWBTADk5Hw2pFffTjFleRtUJXwXYl9X6RsMf101x86OjSE6l-aGlDL58eKoMs1s2iB9W78B81FDIZt0mQ4rxnJV5MfZqT8TKEtxkTQFepfwmnr1uPiymwrH6qCnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zzkcrq1zoVkZDdp-oBYhLl6nupiBReHmY3KnbRIvX2y64ArfICi4PHNBIBeHmHHHDQ3q5qRJsdoXzr1KlXlWxd5ocbVM0nVWg1pLRBikck7ZNK-1MnAVFhnWt_KJuGDIUb0PWbLb6ewvZTjGYCH_nBgjdCOHam1Q1P0vH20osn1RpWTjFKrhS3W30lcv1uohKkLtXmUCq3X305pnJHQwgxoHUfUU1QR7kcXiY6PoY83-7wl5AlRQOpCdAKfX2Gm0_b3a8c3o3i3wSmJ0luTzCmjf05PhgLQobAE1fXK-fYS1wlpE8-ZByyT8S-t6D3u6M7fudCNG6TuDTOm9YFrWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=GiAj6flj-yvEKYd04YVoHTKtMsfC7EdLn9G1PQMK0a2GHjh5tXmz2-yDRXyc-zfjXNjmXeow1AGVO-B4GpCjTDtjnKX1Oj7kqwkt4G2zCt4aSGSUK4rOdD_A8OWROc2NYFQm7vwd2w68ZF5svq0IvCNu4V0Okeb3u7YHVbpzbFVLxThYATKbmeaPV_iq8j9R68i8IYnEkxR346cSfAe4pJBGklasK7F1T1mRHwFeGvgZeSErOHOkMjacv4t3UL8-BEhYym_WNw69rEpDUER-xnu8St9JxdMM_eUYziw_laUtwzeAY8PZEQP1TntFyWCcyVjEZi6kcwIqjGR55NtzdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=GiAj6flj-yvEKYd04YVoHTKtMsfC7EdLn9G1PQMK0a2GHjh5tXmz2-yDRXyc-zfjXNjmXeow1AGVO-B4GpCjTDtjnKX1Oj7kqwkt4G2zCt4aSGSUK4rOdD_A8OWROc2NYFQm7vwd2w68ZF5svq0IvCNu4V0Okeb3u7YHVbpzbFVLxThYATKbmeaPV_iq8j9R68i8IYnEkxR346cSfAe4pJBGklasK7F1T1mRHwFeGvgZeSErOHOkMjacv4t3UL8-BEhYym_WNw69rEpDUER-xnu8St9JxdMM_eUYziw_laUtwzeAY8PZEQP1TntFyWCcyVjEZi6kcwIqjGR55NtzdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2O_zgvquTRYduyIJqfL02ZErquESneDQEQ-udWQptpNOzXnY7hwz_GXVnP3AzgHbwZ2m-3spYFNWO7G6dEdRL8XmyaCUVXZQTznoC9STkt2fF4HzYWOhEXo01Jgt2KhHSq_ONzIDmJNMhv2NsVn4fHxffsLzbhfDHLZYoVKs6LRpYdDVrqYgem2c5KT1_2Vo4s8U3-KxHzdPWl6KUap9shtoKG56gAi1gs25sYbRCVAhxkZE_boXp1QSSscFd0TFtH8b9WBZQ6YshZ8DvfcR564JVb3LxHNVT5HsJ8uP8XdQyQz8dgxhx4h2FJHc5vzlpEo-ZdN4rQISx7psCcy2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHQBq-_BVcC9KEa6Wftzk8WMsDCG5tuj2l89cDx7NduSmI5AyfoQKyRamfZzVFHh-qm2KDnSbGgn3PCs7FDYwg6Xe2Lj4WBtsl7Eobh23m6RLMj0mMqTm96jVC66QPlDookJmcXa6kEsrj5nbucgv9wGsURzY4wEv-ojiCzjHicRh-PX1W3zvwKf9jb8UMdsww5jyDNletR3LaSwGtzrrs78spUoAgQnMikDzp2NJYDQuUp-uHNOftDYx67-Qt_hUAGqG23WhXluLnHGrR48QmA7yQxYNWNPOCT2tYcbg-2njPldXKlzq1HVzi25z0hFE0FghOY0K_HZ9jW87oLsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbveqDUP0LK7DYsddD2JG4fGczVJVKdfd47lyEzlmmow-yoDnaHGzviE_nxP6MwbQqGYvgjuIElBslP4uFHIQaP86dq8_0MC7mJBNmbtnyGYskMlNftl_qVHvar_CIakCSFMfV0AnXrEdwFlic4EoLFjrUHipm9vZyqmf2a_idUtQjS93jdDaQtHM3xj6VquAJx04iCbpQXi_6J9i6Z35EsCUNcTvt2UceIgsChYrZuW0n3YFwXA5JIYUbgFeFWji4FsA84Tzf1EcecKAebfVzdGJrMIT8TYigsLh9_I_jduOq59hTE-Guiusv15txK41sdHamJS8Wtxv54xVsGIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=Y9I4RM1b1K6EtcnCg2ruAK0GVfDAbJW4Re-yWd-RleKLe_GGxFIacTnzcsZytKjDvywF6Ir6QN8HNIrI0rfZwFk59XHPUd1zpm7FDMwqN_u_6l5IU0XpMmrwC8kF3nsPTb5IQ539PMq7m0o5ts7Y0TkXfMdYyoSvGu5Aq4mXx7fAP7bNLgIY3EMnuk1Gu02yVfreLHPTGIrLDVEFld9qX4jujSqZYGYD1RQX9dSx1McC4odBHmKL8-qOqMBnttXsM_aXql9BKErbpMyinFmKeRbMcxUMDZBjBKmXLIf04PFfGdbCVtQlIcgDoau4AOVfE4mssFW6VPwSI7fdoO0xuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=Y9I4RM1b1K6EtcnCg2ruAK0GVfDAbJW4Re-yWd-RleKLe_GGxFIacTnzcsZytKjDvywF6Ir6QN8HNIrI0rfZwFk59XHPUd1zpm7FDMwqN_u_6l5IU0XpMmrwC8kF3nsPTb5IQ539PMq7m0o5ts7Y0TkXfMdYyoSvGu5Aq4mXx7fAP7bNLgIY3EMnuk1Gu02yVfreLHPTGIrLDVEFld9qX4jujSqZYGYD1RQX9dSx1McC4odBHmKL8-qOqMBnttXsM_aXql9BKErbpMyinFmKeRbMcxUMDZBjBKmXLIf04PFfGdbCVtQlIcgDoau4AOVfE4mssFW6VPwSI7fdoO0xuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPxENDZvkhU8c7ApdyBjCbZvxVfRLz0s9Jhj88MENfgPdW7iRBRMuzgVldgEAgflUc_pIxAqo0X8N3bycipOKEZ5KXtHCGQmzFMK2duQilvXO-xaBM9LVsdYa4YvJhHitCFkn-FRXJrGJ7uPrHyXJ_LR_yypYrBG9VayFOyG34yn0_97UaJJg-MWfaWtrz0GnTo5TUU4HXWxfIOWC0Rp8oc1Tw0Uddtp0POXHGnmVsXtA4-7xcR9tsw9aBzFbY1dUA5XhkVmbUj9YvSMPh95i3AMT8oENL8On3kImJlMcOkxmfCJi4PjwLTZ0ThfsuyFOTqrknUde412fAn9SWc67Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=tYDqBGCwZqE3aTlP7DXrNm60d4cN9eVh9cE7UUYmKKpE0jgKi0ib1dNZxOh_owNYWMR_5emcurU8uo1UnKLOWMK9C8lqMxkgLR0-2M8XKsvwnkhJIg6c43YOX2bHlnOUxHSDVlfC6GZp_WiNibo9WnZQSS24FmS0tF_4c25-xWKXFNVjvm5oVZobUc61o_eltHueJQ-mo3ja7opAKkGoLY3v8pdI5NdnfUu451StqqIFinvUGLfOQLoUuCr4fQMoVhZt5dM2G_5kvxcCRk5I66g_26_J41A2Ai8XSVCTly7MPsEp4fFsEGJ0GtDJ58CMFfS100zkeE0RVp5n6NQAlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=tYDqBGCwZqE3aTlP7DXrNm60d4cN9eVh9cE7UUYmKKpE0jgKi0ib1dNZxOh_owNYWMR_5emcurU8uo1UnKLOWMK9C8lqMxkgLR0-2M8XKsvwnkhJIg6c43YOX2bHlnOUxHSDVlfC6GZp_WiNibo9WnZQSS24FmS0tF_4c25-xWKXFNVjvm5oVZobUc61o_eltHueJQ-mo3ja7opAKkGoLY3v8pdI5NdnfUu451StqqIFinvUGLfOQLoUuCr4fQMoVhZt5dM2G_5kvxcCRk5I66g_26_J41A2Ai8XSVCTly7MPsEp4fFsEGJ0GtDJ58CMFfS100zkeE0RVp5n6NQAlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ_0oXzOnUemLWGMDfEb0cNGHSLyeJoyI7XkUEEClZgbHGlaCsWN9tBjqOG-a5apbwMjH4OeGje7rT8wEJtA4Yvl_jNod78IjoOrBi7vBZpJKtnUHU8M2pTztG1bCeArslURD5ZR-uz5lA1Kl6iY4mp1s7-F0jmbYGslqfZo-TiGCtnaaEFLd9ciUf-CK-RAURjSrviA4BOixPA9xETDF8gez0kr-KYO0Y6MFU9icLwmlAYT9HcGXU8MjfhP1Q53foK9Atsc_aeUXxGzdzYhH3xs5E2U_LvMvJ98RugNGtn88MZ5vEBB7an7rQ_Jr9JNjYbMfwRazho4oWUXgBs1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxyo8gL5r6mvhjQqk41PHni0_gNe99LY_0NxvWNQSMGY7Adw1NDbmc6SnpnwzeRyN7fxZrCqJyEgmh_WjBEl_ACFOhfa7KH-DZ59xmW1Agun8k1VJrl4BI9vLLLARgp9ioA9GUb7LTuyPCMkVgFR6U6Dr8R85Lf7KUs0-eaAssyLm9ETUlOQ09lWg5qgzdVxHGaGjtTRj3PNDWOytj3wF_ViLZVU85zSh0sHcMh6omru0idFAXR7Zr-mQsAK7D8NpJjExhhZHdZOXr0Ws8zmxiv4m72wSHb_Wgt5RLvy7Aso8rou0qYv7ns8rxtzwMbY5I-NQbNOgL_EDjI7XnMNJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=c_hOhCDD3WJU3jiA07yXYeUkJWsPXLvAZAut2sdoxhibnbEquhY4xeaaZa2kr6Sce4Y2G2m3CTPQzF5rZ7xxYojZhkLqHp8FF7SxyBcGmHdTk1x2DVv4ikQuSCV1jOWqsy_LutZPgNVY4_oc9M7l72ywqeyBtutgizMAhgdmPQTFjxAHj_yeIioKXrVYvwKXhcBYZ2irKOEXeAMS2RkS2B34T804BCf3FLqKZmdAUEOlOFGeXLqDnN3wFEYiEYKCUZ5FHoELcZ9mKK5MN_rTCKecqV3dykrLkbj1v2NaiRxhpT9BcH1NX7GXACnDsi5700Tx0QvHK_ZEVt_-o3pzWJfKWr_cy48U7lcDuzMSTNlWdNaE_gtZta1SdVxhk72HsPjo7Gy1T_rEnpgn3VQies6NoSNCd4tnYura2-MI2kFmwoVXOE-VGPdtTmmcoPBnlDvsWtKbJbMQHPqDgPDrpLdY3Mp07yJ2bFvW2m2Kd-WbJPleQtwydIuAP46nOc8xJJNmd0rVPphd1aopuvIy1JJBE3NnZ9nSWq0poFiiWSIwnpekOI1isTV5qxylkd2QWGN5NvP2T3QRCHVp-mxbW9xOaqaaD8kqBegZ5Pw9FRSzQ9BkbnI_5Y7fjzPlMQFv5ASZPWWNkIr-LMk7-GyzVaBIhLLOmcHJRYimYlQMrd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=c_hOhCDD3WJU3jiA07yXYeUkJWsPXLvAZAut2sdoxhibnbEquhY4xeaaZa2kr6Sce4Y2G2m3CTPQzF5rZ7xxYojZhkLqHp8FF7SxyBcGmHdTk1x2DVv4ikQuSCV1jOWqsy_LutZPgNVY4_oc9M7l72ywqeyBtutgizMAhgdmPQTFjxAHj_yeIioKXrVYvwKXhcBYZ2irKOEXeAMS2RkS2B34T804BCf3FLqKZmdAUEOlOFGeXLqDnN3wFEYiEYKCUZ5FHoELcZ9mKK5MN_rTCKecqV3dykrLkbj1v2NaiRxhpT9BcH1NX7GXACnDsi5700Tx0QvHK_ZEVt_-o3pzWJfKWr_cy48U7lcDuzMSTNlWdNaE_gtZta1SdVxhk72HsPjo7Gy1T_rEnpgn3VQies6NoSNCd4tnYura2-MI2kFmwoVXOE-VGPdtTmmcoPBnlDvsWtKbJbMQHPqDgPDrpLdY3Mp07yJ2bFvW2m2Kd-WbJPleQtwydIuAP46nOc8xJJNmd0rVPphd1aopuvIy1JJBE3NnZ9nSWq0poFiiWSIwnpekOI1isTV5qxylkd2QWGN5NvP2T3QRCHVp-mxbW9xOaqaaD8kqBegZ5Pw9FRSzQ9BkbnI_5Y7fjzPlMQFv5ASZPWWNkIr-LMk7-GyzVaBIhLLOmcHJRYimYlQMrd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=nE_5tH5RV6Ryu8Bd0KGqxKiRpOoOWcQnuIKtTUCPEVg0BsnCQcWsFMq8hVzFmoLr03atcLqFPULHtvPq8cqCm6nHSux84_isEu-UhjeJQ-KcHF63g-pUOAFTd236FWjt7pXuyoT3GnnhN-gNQw3rfBsqizrVf29hnliRoaFmKFSX5h8gqB5cw3HYe61eG46ONNHtGPudbd_iEKhjhWsg7NM6jP6muDRKHPjD5HzvZa7QQAvkcB4Fwu8oh6r8kCXJ946H_X0VP0Cg990gvmqoNjYIb1GtEkKg0tq_Dcso2grMH0vRFyBMEHBqNIV0UezRCb60UqVdvlxxa2h9TZc5sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=nE_5tH5RV6Ryu8Bd0KGqxKiRpOoOWcQnuIKtTUCPEVg0BsnCQcWsFMq8hVzFmoLr03atcLqFPULHtvPq8cqCm6nHSux84_isEu-UhjeJQ-KcHF63g-pUOAFTd236FWjt7pXuyoT3GnnhN-gNQw3rfBsqizrVf29hnliRoaFmKFSX5h8gqB5cw3HYe61eG46ONNHtGPudbd_iEKhjhWsg7NM6jP6muDRKHPjD5HzvZa7QQAvkcB4Fwu8oh6r8kCXJ946H_X0VP0Cg990gvmqoNjYIb1GtEkKg0tq_Dcso2grMH0vRFyBMEHBqNIV0UezRCb60UqVdvlxxa2h9TZc5sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_nMPhkoEgZz2HfPFJZ397waAhy7atCG9yFLzbcpOPjU8Jqe5PoIn-CcbfR-04djNsmIPAGRrOGn21B10F1WoIIzXDWk8IRa5WHdL55GhwIVL6wSpo6wQpZMMcGXEefM04MhbcZQN1-LnxVmWgY_SUCwAbDgmK-SDH3XanUxBXVfWML5Z76Yj2hkOSpe3jFRRA5u5lbOeIncSbc5hWevD3scslsZ0gXzAtE1p_A_dTefzvZKH4aF51lTSrAfSKpQYYvjdNQ68rZCxWXa0UNIW59lDYG__5H4N1vdQUtY0uJwIqnbKV5UK0zCF8rw5KSDZUJ80u1OeZxgLcvBSe0l8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=eGd3xUu1ee6hQNS-vs9iEl8yivEShrXV4liGIajYwiGZDrk8vjbz7bnQM-aFDEnsNwD67RdTMb38q0FwIWz6NS__h1nZXWoZRimlHY9yBMQEGe8O95TPdyeiGItTB7BrIZ3HUKouHR7tTWSJsfRZm9SdUEmGU3LslQJLnUDXVtjyR5Ppe6oyw4-sgh8rYMeHCwDcDZQj0o5lQmnhJw3dfwXgNRAwy4HBbla5x_B1VvrDhKIGpsRNmDTuUP8ZwL3nSkRH12GrtcB5qElHjUxlqx_rbsBOMaYFkqLXohIwJcgIZ1Kep7z4INXoj694sGkUZHz7T4kD0hGFLqbm1AJxD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=eGd3xUu1ee6hQNS-vs9iEl8yivEShrXV4liGIajYwiGZDrk8vjbz7bnQM-aFDEnsNwD67RdTMb38q0FwIWz6NS__h1nZXWoZRimlHY9yBMQEGe8O95TPdyeiGItTB7BrIZ3HUKouHR7tTWSJsfRZm9SdUEmGU3LslQJLnUDXVtjyR5Ppe6oyw4-sgh8rYMeHCwDcDZQj0o5lQmnhJw3dfwXgNRAwy4HBbla5x_B1VvrDhKIGpsRNmDTuUP8ZwL3nSkRH12GrtcB5qElHjUxlqx_rbsBOMaYFkqLXohIwJcgIZ1Kep7z4INXoj694sGkUZHz7T4kD0hGFLqbm1AJxD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYkB9duq5pDtPO4RsFZZDYsmTb0Ep_7YYh0Ux19UTaCrfrJyxF_EVEe761t8UR3GQEmgKEwrDGHjTaFvU_HBJwIBg-FgES100D4P7bGqdOxzEnactl8gzfN5LIZ7oB6NKwDNUOxUsOprfz4RPahVwW3g6ABog79j-cXVqPwtcfTlYJxwXCAQGpGa3PpqhHVGb3Ts7zvQ16BL7drW-LK8j96RVRryfIMgtm5cNKNiQIaabpVujPzUcyMq7UhN36fHQerOrRyxMyBdRkclg43db3rD0oiAiY4p0Nn2meVkd7rGGLk-Av8tnk41HZnMPX7fplLeF4Sxzi48_hbypKpneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFIpOquALpm6jXB01H6lWoRSWfxgVITU7D82rKi1btG1MEbyILIN6cmE_8uBzyx-3PbiNWeZWyJcZD4fRDz4ZwcGN71crlxAqZ9jqYA0sX40hpVkEC-Nt25PvNwljIBCpM02HZ3EVKDVrcRe-7rDcI9VTHV1r2AE-FVyBFcRc82PoTizTK0yuTVsfn7ZTm9Jwb9GN836pIhouCKnRPg6E_UNowVo6ANxcef8MsgLEWag0zwqLxs3UAfWIPJMoXgth5ySKZVnPI3DkNyYCzAruoERPcON96gOnoFUga4O8pZ1foREJxHTWsiG81q-Y0xlJaHht0sCzqQEeMvi_DQ8cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PozOJCYPF06RvcAV_f7F6Oj1XLCr6EvQYhTGshqie9h9bd2431dhf3cm4afRyYRkGJOKVv39EJCQMWVETH9OhhsGKEhgucWbdK0aCDiBSjh8inMedp7c8Jv-1Yia4goQEMtaQa7AZOCN803lBh7Zt_EUCc6HepUodexwvLszn67DLDdPqG3RcZjrRgCelZV-g27629EOI3IxxuqxuVQunaOitxH4Lr-pgNqI1Fvqshq7xi9MHODlwQTOB7qkMVqPCz0DO-_B3nxQwjUfqsflO3lt4D8AuhGYXvsukCaXFPPAHNa8WDlFws5-QoJDyCE1eJYjODGQ4GK17KH2mn352Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4w6kMHo-3hrmo5mtv670DHwlqRqv0wvwj5xsadckV0mQ4q9L3tNJPq-PcyWEJaQ4dNsUvcqzUDCMKUzYJREQUN7f3Tsrk6Yc4dRk3eg2iT0NNPak_ceWaeq6WyjBLKKceby4MJUU965VTgdy_ni9SSOzGv-YTQmAZngKAoBIcPlmzrCDSlmt-A57-XUiCvxA0Y0wrZw9RgwTPBpGRA6hFMrsapuHUeZc0ZyZKwW_cDFhqxcvLhxDb0nRotxsOVDIJBkzgB_uSgHqDi3Z9_bidp3E3ghXinE1fWs0NXVGAAUrmvfTv0PGOS7YlayXP1-PEvqw5_rodyGmKcGi2LsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoyUV-Vi9yGBnsVAc50Cn9BKTwC5NkB47oBvHECSzdbgyOrCD0jABiIM0YoAr7UqwV1zbhRNCBk73lbQ6v7Ta6IIfNbK1a1XCvmdRdNLWtUjKNfLteA2DGgAkg34e5H_NKhsl7i3XbDcQ-613hIslhVhRvZPCOs_yvCrV8UNlHK4BnKZe13ma1gAlOjf0vMZQpXm2QnN0rVu1edt8GP20USlxXQ7qxm8EJGQtyPtY6vAYsfS5EDspnHf1V7hS2a-Am51jEwlZDIuERlivZZ70ryeXL2T8ReEe9uaDI_b5HEASQ45luh_ya5fdB_UAd71v0HrPj64gegox34GtIWEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=fbxxsRAoY5qSO0nGdVu68w_mGcm2wSqvr_bfYx2qEwmbFHrnJgw8WQywHgJebSzPywQ5zYXAOtmRJGBjbEVGRq-S52ax5KG2KrsZkpABihyHgpHMe4Os4rZGd7TDdVrndqgKqaTK_0iPkZs_K3mKaOPWLxst5YD7XUYJNVWmeq_OG7kOfT7zeemtLD8K3CPFePbXqU9Yz7ontWa3loNLe1XxHGPYvdPtV2_1asiq3ItwuPP3584b725-qBK-kQnl_5inr09tQTt-PPulytbfSeuYZs4SGNNQc_4gwWbsPD4pL9bojU17jCHHQIUOuL68iHdqewol5MVKRbAb0W7s5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=fbxxsRAoY5qSO0nGdVu68w_mGcm2wSqvr_bfYx2qEwmbFHrnJgw8WQywHgJebSzPywQ5zYXAOtmRJGBjbEVGRq-S52ax5KG2KrsZkpABihyHgpHMe4Os4rZGd7TDdVrndqgKqaTK_0iPkZs_K3mKaOPWLxst5YD7XUYJNVWmeq_OG7kOfT7zeemtLD8K3CPFePbXqU9Yz7ontWa3loNLe1XxHGPYvdPtV2_1asiq3ItwuPP3584b725-qBK-kQnl_5inr09tQTt-PPulytbfSeuYZs4SGNNQc_4gwWbsPD4pL9bojU17jCHHQIUOuL68iHdqewol5MVKRbAb0W7s5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUfLpH2bFWGrS5L48yTunTWimd_LRBMb4PNEgsfkJBkVG4ayh0Y7rIBW-5qQADnwx9p4vGe6yVVw4LVAxrs8CMuiZOqBAYuCmmLj0_2mfmXxpOw8ufudHjwff56yOw79PKeLBEFKYor03L7Pv8HDwGdyQQFBucPGLQMNHgckiuGeLEY3jvu33UNFZ0sLG2QMXG79nCipgrmmGwKCu_NLG5k1qhQXUil-_E2Iva7bma1kkFN3-TFwe7XZc5WhDrFGmF9s58LHAyxks8xQ-mMdsqEhxPEZY2v05qHgF5Xl6rbdo1f9iD_DRaKkDjHGYE-CV6vY60el6J7Knq1Jajb3qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghh3bZybI4rbagashA3-GL0qFDf7FxZMCJPJdY23HI1hCPt3DK6PhP-eTwFMEqR6-PBwTeLW7u04qbgNyoyN20DbKyn_wSxFPsvfGdwqeWv_1ekyy5y-fRK5UpE8eBaBWOoraYONEglb_94VJ4xOTFH_tGJ5ccJf3wS_UUSe2mIQZdUkOR-icAWBTGT37hv2SaFGbgrJVDcU_Ys5Akfyo0NaLNNaM8xErKDX_7iVDF0vn_-soOilCk6sWIWdsFVgE9aNPKrtrGs41OoTy28Psyf7ZKWf5G3icnesgplFbPVzH6-pm5OK-OMFIKbsTej7oy-_NdXs5dTncNURhi4yKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lo0Qr9YZmt1wDM59W4GZ9eWh-VScEAS_bsSpsvSj1BZqFVHu7nVAfSP2bPS18G3hNetFuz-BZO7o_RGxKi1ghTRD39xnbOj9XZMhNKeu9Zvw5juNroNIR2gzBYk3MLPZpI1V9b8iwwBJlWJin1BN3gGf5jSbyuEIIwIZoiTLmCgHvivGBSb8ElBIJzvJhKJF9gYzfm-Xkix-0IQhHlDnGYZ6gNu7vh0XD3kVWa5wBPjBRHoxzU9HLJAiiCcGf5atJaN2TXkEirfMqcIJ1CHJzw11R_EtHw9V8Ok7vijpKX7qM-kfL_CUNctRZAenFdHAsNp78McihYQLuQcAOi0SmTKIRDDki2jXqLV_MC6pHlWr3udQ48VgSs9jLBCyVScU8A1uvd44OVxE-4URxDkXSwZhdUA8O4ry1gRzdldZLUCphSXfftVi1tEZMk3jU29mkG8fwNSAqtqtyfXvjtwUv2zipDmtBBNe6CDFdBMP7LU-Vq6jF4wF7gfQOeTXBQvvvIDozutTAvltY4TffTUTEXVH-KYrGKpYlvwD_ta0_Zg4Zaq59r7bqynK3e_Kw430aF3mXxYoN5_3-DhdkhhD1JAukypIPMmgoigQA-6-ttdsZ70DCRICEsxdSLZ8FVtGjd00ZVRRSSZdGkz_SvWCrX-UUZuR6RhbzmVhQbGFw9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lo0Qr9YZmt1wDM59W4GZ9eWh-VScEAS_bsSpsvSj1BZqFVHu7nVAfSP2bPS18G3hNetFuz-BZO7o_RGxKi1ghTRD39xnbOj9XZMhNKeu9Zvw5juNroNIR2gzBYk3MLPZpI1V9b8iwwBJlWJin1BN3gGf5jSbyuEIIwIZoiTLmCgHvivGBSb8ElBIJzvJhKJF9gYzfm-Xkix-0IQhHlDnGYZ6gNu7vh0XD3kVWa5wBPjBRHoxzU9HLJAiiCcGf5atJaN2TXkEirfMqcIJ1CHJzw11R_EtHw9V8Ok7vijpKX7qM-kfL_CUNctRZAenFdHAsNp78McihYQLuQcAOi0SmTKIRDDki2jXqLV_MC6pHlWr3udQ48VgSs9jLBCyVScU8A1uvd44OVxE-4URxDkXSwZhdUA8O4ry1gRzdldZLUCphSXfftVi1tEZMk3jU29mkG8fwNSAqtqtyfXvjtwUv2zipDmtBBNe6CDFdBMP7LU-Vq6jF4wF7gfQOeTXBQvvvIDozutTAvltY4TffTUTEXVH-KYrGKpYlvwD_ta0_Zg4Zaq59r7bqynK3e_Kw430aF3mXxYoN5_3-DhdkhhD1JAukypIPMmgoigQA-6-ttdsZ70DCRICEsxdSLZ8FVtGjd00ZVRRSSZdGkz_SvWCrX-UUZuR6RhbzmVhQbGFw9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=n5CVos1fvMVC4x0vw3P6aamCWxMztoeU5s8wewohxUTzAn5ncXFNHltlTvNcyqJ-SfAwcbHW4kpOS2CNXhCvg0Tg1cUlfn-U49UjK9KcHB-lpRYyjByRnaIzNzHOI15M04L1x4LbePxZGzkE0qimiOuFS4vP7rutm2RuBMBVfbEKCf_3EoIsiERVaSpqvilnkw0xxltMpHBi-ypIjApGyBPIQ0jw4m2F0mtSFyq8kygo1gt8oXOUgEmN-pjenEos8Scc44biZ_zrgNpap25sjHPFzsAeAp4-NdcaDZzWjwHh_iB-oUnKEhEIzbUEDSamoIGvN2b4O-CJD939zSE0gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=n5CVos1fvMVC4x0vw3P6aamCWxMztoeU5s8wewohxUTzAn5ncXFNHltlTvNcyqJ-SfAwcbHW4kpOS2CNXhCvg0Tg1cUlfn-U49UjK9KcHB-lpRYyjByRnaIzNzHOI15M04L1x4LbePxZGzkE0qimiOuFS4vP7rutm2RuBMBVfbEKCf_3EoIsiERVaSpqvilnkw0xxltMpHBi-ypIjApGyBPIQ0jw4m2F0mtSFyq8kygo1gt8oXOUgEmN-pjenEos8Scc44biZ_zrgNpap25sjHPFzsAeAp4-NdcaDZzWjwHh_iB-oUnKEhEIzbUEDSamoIGvN2b4O-CJD939zSE0gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JImIu-LAUHk9dLje_-e7vfJ-4T6AgxysefwZKSVzyZzk1IZT0ZTASqZ-tZkvtMWhO6lqFzwjLenVpVNxRt8rhpERZWMOpOChWSKvhhb4gfk7ZfGf90HjhZMpjdJ63w7Grn2C-keykku3GhUg14u6ELQzsFCSpMnljURWlyqIf6gevVJXv0x6ITBhd9sFVEQ78QGxY9VopTsc2ibXf_H_SNOCi9Y6QNVVFVcLNL7X3vkCcpX_MeeZByItRdTw1zn_TBUpk6tgkIccZWX8Xf1kj-3fNUFpXLNTbX3h0w8_Q-x7lcCnS83ByCtqEJsOQI2G9QGlholCLxTqBtxuQt3IySAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JImIu-LAUHk9dLje_-e7vfJ-4T6AgxysefwZKSVzyZzk1IZT0ZTASqZ-tZkvtMWhO6lqFzwjLenVpVNxRt8rhpERZWMOpOChWSKvhhb4gfk7ZfGf90HjhZMpjdJ63w7Grn2C-keykku3GhUg14u6ELQzsFCSpMnljURWlyqIf6gevVJXv0x6ITBhd9sFVEQ78QGxY9VopTsc2ibXf_H_SNOCi9Y6QNVVFVcLNL7X3vkCcpX_MeeZByItRdTw1zn_TBUpk6tgkIccZWX8Xf1kj-3fNUFpXLNTbX3h0w8_Q-x7lcCnS83ByCtqEJsOQI2G9QGlholCLxTqBtxuQt3IySAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
