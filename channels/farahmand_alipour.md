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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 02:26:41</div>
<hr>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcDy5iNvQehdNbDoLsI0brLi0u-AtVLDyYypgGW52M2uEkVkoZi8otfB8qxEE9Tn13IOOCm1Y9_TZ8LV9qT_drizBVziD_21OkyVPGiLZg-4I0cQ4KVhUIJg39UzhIn3Mr0_n3n46De3GCGetSdFPqS1KyUDeo17sAIKsgP18CTVqzmA-eTyyxuaJO9YoZI--Q5JazAkwk76jlDQ-HAYLmMgG2zECYS_3Bw6QBV39rQa9O7LtEOqq6KsDtBaTyecuuf-GnWnYi3-QCfeajPlTjnYZect7epGZ78kKQQwphLTX1Y6g1J7xYobbcElHoXh7kGSHOdeIY7AM9trztwJiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=bRN2eQ8oBFqwzGNyUlGPXvV_hzRjjGTyn5nXE6hyatfRGCjgXR1ojvWC703sFvY3pO3_3ELakv_WxoWSeyDCWItHsc9D2BmlV193pGOfXUkkyvNKBZlqyZ4EPRmCFE02ZE-QBP0S7hnCQhp6VrqknRI6Zn1_BG0gnb8dPE7pemL27a8OiHMWjhvljd9vyI8v6MSo_oXRCpwcbFHwQKlr8ErvXY3hroqk9rEGzv7aiwk04ZukUq4Hf1sKmRTL_kj9EKk6rOfc-NMBbYv6l6n74ZcPmUQap-VKG6I9wJ7fKDzqzQLMsfroyauT3WdwDdcnEWKtbedSxDxdlQGZokkdp04fXbnZLH1QMIiSnYkWcgfXlac96jZbtReNaGi5_8nvm-SXoAfWxxFdZ96Y32xTfI8c2k_sjEAFRshefBHFLJCEq-CRWnZGXcNv93YFYyxHowkjk7p549aQdhge-mrmtmTzAOYopxglxlQDEuW5dV1eltvvTYv9woa-lAui-Z90w1F0o6Bd0v01t0QBKCazbdHiYn8a94yFHQ0HT-rVZ3T26ihm1A_Yc6cbN0kzcG5XSVaK03Ljc9phomdva2-Z_Pl-o6jjzGzSUUd-hdhZuQ20xnDnX_aflu3CSNIltGK8Yh_ew6MRqPThhvuwBKP_eV1z6vQT7d8dAAolX9_miAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=bRN2eQ8oBFqwzGNyUlGPXvV_hzRjjGTyn5nXE6hyatfRGCjgXR1ojvWC703sFvY3pO3_3ELakv_WxoWSeyDCWItHsc9D2BmlV193pGOfXUkkyvNKBZlqyZ4EPRmCFE02ZE-QBP0S7hnCQhp6VrqknRI6Zn1_BG0gnb8dPE7pemL27a8OiHMWjhvljd9vyI8v6MSo_oXRCpwcbFHwQKlr8ErvXY3hroqk9rEGzv7aiwk04ZukUq4Hf1sKmRTL_kj9EKk6rOfc-NMBbYv6l6n74ZcPmUQap-VKG6I9wJ7fKDzqzQLMsfroyauT3WdwDdcnEWKtbedSxDxdlQGZokkdp04fXbnZLH1QMIiSnYkWcgfXlac96jZbtReNaGi5_8nvm-SXoAfWxxFdZ96Y32xTfI8c2k_sjEAFRshefBHFLJCEq-CRWnZGXcNv93YFYyxHowkjk7p549aQdhge-mrmtmTzAOYopxglxlQDEuW5dV1eltvvTYv9woa-lAui-Z90w1F0o6Bd0v01t0QBKCazbdHiYn8a94yFHQ0HT-rVZ3T26ihm1A_Yc6cbN0kzcG5XSVaK03Ljc9phomdva2-Z_Pl-o6jjzGzSUUd-hdhZuQ20xnDnX_aflu3CSNIltGK8Yh_ew6MRqPThhvuwBKP_eV1z6vQT7d8dAAolX9_miAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=snfmXWm8OXqwv1HEVlrDQWBcfJYMHarp4KqNY0DI3zdaNUF1dzmKWWFqrJ5KcY5RGLXm-U4ZT8U_CgOLMnsgV8RXKkiry2tOjyCgHmcHKi8jMw_0QMUEPmqI_2v7FGIKSR7AcnlOpEMjDMIFFZra-Bumm22eBUC-3ItW9bugwSLtWMHPkj3g66kZ4T0GGRwWoGzhAmwgsDYS6_vqnIjQ_n-ahEHJUnICDTSDo8OxOaShWYqEETPVdKg4ZnLVPMWHkQxtJgvBRDPoJb2W3Srydxi871RuJ9Z6myGkuN16cstm1Xszi39Y-hVgcfnLEVedtFzs8S5H1bjvsu4l7jUqHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=snfmXWm8OXqwv1HEVlrDQWBcfJYMHarp4KqNY0DI3zdaNUF1dzmKWWFqrJ5KcY5RGLXm-U4ZT8U_CgOLMnsgV8RXKkiry2tOjyCgHmcHKi8jMw_0QMUEPmqI_2v7FGIKSR7AcnlOpEMjDMIFFZra-Bumm22eBUC-3ItW9bugwSLtWMHPkj3g66kZ4T0GGRwWoGzhAmwgsDYS6_vqnIjQ_n-ahEHJUnICDTSDo8OxOaShWYqEETPVdKg4ZnLVPMWHkQxtJgvBRDPoJb2W3Srydxi871RuJ9Z6myGkuN16cstm1Xszi39Y-hVgcfnLEVedtFzs8S5H1bjvsu4l7jUqHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgyfBDuDCJAt0JNr3swz4HIiKL9HrZbuqCUgpWgoWH-EZ48shYa12Y9jdCvxYiiUNFYEdJyEo7wU00C_BFnb_CTyVpzrMF5rOaoq9kfY20upu4yrh3hB5FuUoO5req5uCes4pUb52gmb0Fy7wTOXqJ3zoNQli2K0qbjfW0UG-maUyxTkGqrZoG-0yyCxvc7BaTOLtGogCdjOavj9BXcFLXh7XHPNWWIadDPMDLkUiV1vEWOIIbA-gd7WI75ohIeh1Pk1T33bNTZMkSWE1h7eaOVXSgYf4bfPEE0IOn0k3beN_HQF1mbN29UXT4qshW1DSNBZOglA8ZOoGk8W2oZOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCJL3-8VxSn7fEsY3P6E7Yu35KygkPYAz9kSrPiP6mOf8U_s1hTygNHV29aoJtMFV3uDNu2SOmOr0pRE8Uvfb_4v3pd1wxSiC7wpZnrAVsKJuukgP-edn0XvKe6r92a-BQk70aHqprMQhb3F-ozQFNjyygGncCdKUSeTnA49lpLU-LKQovR3tXzfRYEQ13VxHLLbiH9ZOq8KL8MaWIGiCzWEk2jLqvCACusOmTarI5B3ycu06qcPPIP_Ppb52ylFXvsw2sTsuqNG8bwZzP13zYu87MoCAD9yHgVbxg1mP8ENRHtvk-EBW8FmpMPAivbYtiDzL3qDs_aptE84S3_x2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4kUTxRXfz-D5HD_bWoXgRgrYiak-pVLXVxgp4-BeojCHshuIc9HusfxGkpxvb3FpuKDTuEJRotNcjc1Q4l0UI7S8dvhFlWitvfNEqTMoz9DO13EehM3mEg1YTptXHXCp6iWN1PYngvlboCUMmcJgS_fU7dwZKWFh8-wNn5fgjmqOkPtTkiFIcziU_eUdyuIN3IbPFQ3Ybr9jGdcwqUI-UwnZ5Yq6tio2u7PqDKaggJpV-PxFW92N2bMtLam1MDfxNe3ATnZs0KToZJ0EYnesRz_GSkv1NFWkCFCB3bxRL6XJnxJzF9ATpwzI_MDdbaOGGrM8q9bDWB8BdYZxQ796g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=YEOHdLMVPtOYw3J_5YPdxn-Gv_SFUFocUTead4paxlJGZnTIUZV_hd1LI9wNVEaKNoN4gm3gWtJ4cppuv8BUVDoGelkv7IjFGqQiNpguBEnw4Ut7g-q7tQEfJkUKWQyTL5jZECN9R1DWNqf2W-m-lqWgu64xR_w2IeqNujmzqOg8E77WWbpuSUUQL9KLjZidEWAPqRsVL7aJ-P3hMr0sCeLuZKZvRsSfRe8zfqAyf76VHo7sUY_VzIZ5_aoAK7TvhZpTr0GrFHOLuSocKADvoQZSoI_--UyZ6W1jvoJ8UQ2O6lDo8F0zwst55t3ABxnCGemJSaEJ3wpxXwKYm1kVOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=YEOHdLMVPtOYw3J_5YPdxn-Gv_SFUFocUTead4paxlJGZnTIUZV_hd1LI9wNVEaKNoN4gm3gWtJ4cppuv8BUVDoGelkv7IjFGqQiNpguBEnw4Ut7g-q7tQEfJkUKWQyTL5jZECN9R1DWNqf2W-m-lqWgu64xR_w2IeqNujmzqOg8E77WWbpuSUUQL9KLjZidEWAPqRsVL7aJ-P3hMr0sCeLuZKZvRsSfRe8zfqAyf76VHo7sUY_VzIZ5_aoAK7TvhZpTr0GrFHOLuSocKADvoQZSoI_--UyZ6W1jvoJ8UQ2O6lDo8F0zwst55t3ABxnCGemJSaEJ3wpxXwKYm1kVOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=q57YD4nwooRYNVQfjQxDucVMOS15EqC4OVGlpedKA2F2UxnYu0byFUA6qI6G9U9FEcDcmQl3xL6A_NHnu_D21GvuFr_GByZcLK_QMWfZ-mfpctpyaa-U9Gm8kVPKTpkiM2SSK_OP4wzReJrmIG_Msa2_v_05PWuCjZ6wGGcua0ztX-stI6Gbf-CkbH7jh-gwTC3o-bNmHNEh5SHmLsNCrJD8vRjZ90yBeVm3QU0e5dNTQhCl1fKyBKIa1-n0kQ-sVcmPu3E15OwAmVXzIaPoNLLYram4NmXHn5W7X-hVn978t3HoVm9rnzmdwKLdWGw9MGbX7sISckjXUFjAOKK7cQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=q57YD4nwooRYNVQfjQxDucVMOS15EqC4OVGlpedKA2F2UxnYu0byFUA6qI6G9U9FEcDcmQl3xL6A_NHnu_D21GvuFr_GByZcLK_QMWfZ-mfpctpyaa-U9Gm8kVPKTpkiM2SSK_OP4wzReJrmIG_Msa2_v_05PWuCjZ6wGGcua0ztX-stI6Gbf-CkbH7jh-gwTC3o-bNmHNEh5SHmLsNCrJD8vRjZ90yBeVm3QU0e5dNTQhCl1fKyBKIa1-n0kQ-sVcmPu3E15OwAmVXzIaPoNLLYram4NmXHn5W7X-hVn978t3HoVm9rnzmdwKLdWGw9MGbX7sISckjXUFjAOKK7cQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2_E1AQlneS_cWCRrq5Y3jwFiXuG4ui0Ii9_08ZKYtz09YbS_WJfTwlPc123MLJOdhhH_uC-OdHKggpLPBVwb53aVYVMVEBbupRct10rGikUu_egMhVBeY6Em2KRvNLN6ezMyc4cWaC9i_MxVYMpSkLayYAHulZRfai4ia-sc2bpX_C5ECLJElMpv0na-g_yK-IXmaFsCEPMC-nlvTYLcWtTKq-C_bS-OPNjqo12ju_R6nRN9k0cYz4yyM6zZdi5keXtqS5peHUOYvI2bMIJJ7uSOObqEq4hxrYxJwfmYDhpC28kK_jNsQME_sjEe4kgWMDPvxMKozXYX_KQ2tif7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUv5anB2qfc-brRh1IVJenxVNXBR0sZCsS_HQO5fDdRmfS3qbRGp8xsjEf9Uje5nBbcXkC-QdgDT5oHzh94KGeFdXLTJhJUO7yOT48zlcgCBEJdFxKmbzPLPMT4f91Se-3Pxl4zLbStIjl3sROPy4gDLxY2Ji1oTx81YlzciaS6Kjm1B_sqLI_bHtYm-5M6GVKX-iAjZD8qsuPR05UFej5AAOGArjArlLCmiIMfcGvInvBRZmcUYzDNd98S7O2yy20QFX9oTOhwtBJcmJsNQHa4rBEB8PMp4Z5J_LZxafM2YCH8__zbDb_rWZTuZhYe6o0Bok-mCja1U9qPhTmi8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcZi7B3J4v_54mMLaMeLbmyvCkRt4gactRhXoIeiHZ-AsCFJntWeBWWD1teE-raiff6dcsGETLsCRrIJiuJHzZex102YF0xsErP7Z9AoGBxeX3d892LEiEAAPHH3fpnF6ftl4I57kpboD-Nc__bQBfFKYQ_XiXuhEBJjoZMeYHsLXpD0c3QY5GoE5zJlm5fP-FHcR_xZky1Nqen4CRU6CmucOc-YqyeeZhaDdHMDOxGJ29W0RE_tp8SQW0F5eNwSzYxVKKT2yCWcNnXVkCxe4ZhTuajsrltArbYh-HSEBLH6uNdX97-xuyFvm1BW-iBDJNuLrltHtwoE_JQpUxwjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDV3RgDs8RBKdPKdVlP09jUI7ILHH8KMVZux3BG8vIykVG5gQ7mhNrSrnQAvwXsH1_3FRG6lf5r7djnM3fPSevIGECIzS7fRODdgM3AwJRtYURSu9R5e1B3qq0D9ugDgikCaat5EzXwqEP7a46bJWd2kcOTllROYhO1PgeFBeEimiqkxt46FTSCV-2ukEKzTiMUpGKVt3qe1e57xa3rnj8eo2qGcSHm_rVAtGiLh1GhIBj-rbAxmd3FSq81fqwCYsZe-_826aJe2hzYDHIJVZPN5GkABCBDAiPtnL3eabWF4oBY1w_Z_0OsiH91UdAe1cmFNyfTF89t41peUMR9jiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5ww8_WuL8X9ZhffIX0cANU8Cql2x2M8EdHjpfp1PK1Lpormagvsmzkx_OKL2-m0SM3Oh00hE-XWkx5HL_1twwI7olFv4q3Fh7JH28bEcFTNtf0_5b-XZkOtpndhlrUY5aEbRCY_n_9qe4xiS20OzKMlruOWUCKe0IdfP2RQef0GfpV6vCY5hHT8rZ54zfuko9dOwmovbUKWJiC1HKVJESI-PFE8hVSEoUfmBzaNel7tCQ9z_5DaGFosWAAZkA_89eoCNWxhvW8QgafENkSMZZrZP0HZ5v7vqXUOO-XV_wbaB9PbuBv9zIhxTHWXmquwvqwub20bqYRsWpVwj7lHJDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5ww8_WuL8X9ZhffIX0cANU8Cql2x2M8EdHjpfp1PK1Lpormagvsmzkx_OKL2-m0SM3Oh00hE-XWkx5HL_1twwI7olFv4q3Fh7JH28bEcFTNtf0_5b-XZkOtpndhlrUY5aEbRCY_n_9qe4xiS20OzKMlruOWUCKe0IdfP2RQef0GfpV6vCY5hHT8rZ54zfuko9dOwmovbUKWJiC1HKVJESI-PFE8hVSEoUfmBzaNel7tCQ9z_5DaGFosWAAZkA_89eoCNWxhvW8QgafENkSMZZrZP0HZ5v7vqXUOO-XV_wbaB9PbuBv9zIhxTHWXmquwvqwub20bqYRsWpVwj7lHJDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tvUDSkJUYjFB9PUyVo4gQ9r1eCfgf3rzcFCsJ2fPssstAblgKdX8H7KWBdfUmjl2MrJNs076Tb2H9zcdkzNMhqLP9FTu0Qz-CAyvwMQb_RvezuXdtMUE1hmehazQhQrVd0qcaxpCJpdqCSrOaIPpuJ0nfbfyY_avBl0fs5dS4rZlx0kri8DSTTxXASvXFV3AO6-Q2QFOwjitr4uF0YgkHIxpIcvmo9y0jq48Yl21fxkY8g7cIh_IigdsMDz449oClfRY10fK-GTgjeLTtmhZHnwe0kqLWK5on06cd4pahObqKVgWEuym46s2WCdd_idFsI2MpMos7lHKqzWtB1ImjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zj9lCv7Pb5iqnQjoahkiqkhJrh6bYhJ7O_X0kyKrnSG6SsZhEH2WuPq0uMQIqn4yijbZTZxgy94sza67uhUq6zakvTM0rNz9UFLd2bE_NdQt2pD5p1xbjasr4pt4ozJdoO8aG6M5WxYcr3-UVmMMx_Zc_kCVBy67sP9dv8LaK8Os-feDr6i3kCKQ0ARnggROSfn4gVkEffHUR0KLkS1HnEsGju9gGu-NAPREsqTMR7CrOveGZu1cInCs0VAJGIt1KmID8fiwu6fP3SMfsfb61z0r7O_phtd1_qSg5m_D5Bd1UNcBk1dHjBdIu_YFm8354MUKrRzzDOiF9tvtctn2QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=qOIevyTKuCCN4Z01iO4oPqY6XYRN-Pk4DFne_BCUW6g2tOP8RYzk1kOqsDmNB4ElF20dbGaSrK7I8FQiS4aMAo14cTA-pK-QHJl43rSTQrjCJ-N6KS-HhevyRTfvH9SvVWWkS1dqdOc2egHWwEWrZUSZGha4vyU7yFpQaNYeXHs5_4uDZ45EAEHXLzLyX98whb5Y0DmBxNwbcDgaUHoZb-i92OJLBw2lKfw4Zi8n_3Q49Nr_HvHBdYxsPfIs5uy22FKVWdpLuBceHKAfwBgQS34GymVdfny7EOQowh1zUXchDu_MRXa3z_Oj9gc7kYhKGN0SXrZDIb28H84imhqAJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=qOIevyTKuCCN4Z01iO4oPqY6XYRN-Pk4DFne_BCUW6g2tOP8RYzk1kOqsDmNB4ElF20dbGaSrK7I8FQiS4aMAo14cTA-pK-QHJl43rSTQrjCJ-N6KS-HhevyRTfvH9SvVWWkS1dqdOc2egHWwEWrZUSZGha4vyU7yFpQaNYeXHs5_4uDZ45EAEHXLzLyX98whb5Y0DmBxNwbcDgaUHoZb-i92OJLBw2lKfw4Zi8n_3Q49Nr_HvHBdYxsPfIs5uy22FKVWdpLuBceHKAfwBgQS34GymVdfny7EOQowh1zUXchDu_MRXa3z_Oj9gc7kYhKGN0SXrZDIb28H84imhqAJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=hYEKhFu4MxpQ3p9rFm_RAEHMoGbLM2Vodal3Qy2qHKcBMVO0y1hO3bMEtv7ACIHHGwvy5ipLhpM2yyBaO8XOQqCenF3LkGL3_CxZXgvEyfQ5BqlRNEKQt3c8tHSVJvRguc-IhKuMMKgmsNvU8EISEsZnQCbCR8dXP1VcvRl_YRTpURyin6_CevyG0JFYMFIf4Zb-Epk67TN6kxYYXXZhrs1J2b_Ttbs8YaIyq_9CHJLsgz_HCFDxftgAowcxvqnOiGKmGvNEbe8Qduot51iS0s2dHny7FvyKSbquTSBT48OtzhB7Am0BMyNlvv6Qxr8i-fsuoqc7FNSMBtWBzaYmIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=hYEKhFu4MxpQ3p9rFm_RAEHMoGbLM2Vodal3Qy2qHKcBMVO0y1hO3bMEtv7ACIHHGwvy5ipLhpM2yyBaO8XOQqCenF3LkGL3_CxZXgvEyfQ5BqlRNEKQt3c8tHSVJvRguc-IhKuMMKgmsNvU8EISEsZnQCbCR8dXP1VcvRl_YRTpURyin6_CevyG0JFYMFIf4Zb-Epk67TN6kxYYXXZhrs1J2b_Ttbs8YaIyq_9CHJLsgz_HCFDxftgAowcxvqnOiGKmGvNEbe8Qduot51iS0s2dHny7FvyKSbquTSBT48OtzhB7Am0BMyNlvv6Qxr8i-fsuoqc7FNSMBtWBzaYmIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxEYXbLmT-840tmLI-gRd4saqmjdbp_xZXNsaTXEI4Kx2Jye35BB1qGPWeopoeGZySSAIg9jQLnJT8TOL3pKkMyQa6cH3y3uJeaeHLak_hM_uCzO1B9EnUxmnJrBeANzIwYUuQvs1AZKI-TyWtmHXM0iiCOHsYE3MSxkQVH6fLkN6Rz08TFuznN2yTd3cXPxVygS2mKlBYeCAbJG8t5_FxXFQRF2FElNdPnwTI7Tl1eq0IVsM6utytlnC6L0FZW-KmdzbQPsInGdxVpa7iz7O9vQey4ZdX6fk8mPx1VHUjJmYnBejtM3bEjk54WnY6-OP1R-bz8QtGYMUdY9USfXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nROVIiGyPNH2nehc2eTHN1qGFScxAfqf_5GX5VR5BIX7kMlTwwjYdNjEyrGTREir0v1XfaShpmTtbH9WG8k2NbVtCoptcuModIC1xsSbjYcbCazLlgH7qe5tCBp3kb_x8UySXDKaSIydkkoK1j2VAmk2UHJ8wcJxja5K2v_8PdUAH3m7-b4UMY4YiEaKS20pddXiSK0jbuqenksLvjg54b0TXoxW7_ypiArAgU2yMyD1nzX_6-pf3Jfnm_KzTArIlEtI1Mg2TcvqT0A-okWVpGJYqkoDEP_AxgZ8XUa6RcEviT-vzpH-3JdKpiLAbN6WE6a0gMd20zGDUy8RMhH2QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=m8XQu2t27B4mFk2f45O-nm2TIsVF0ddOCIm_xCjXBsvmtmcdNmA7ecc-86B2lOwXvyo6M2fUz1hhK1FkL7nPXFUEtKcAwC4zTIaOHDron9cm4yg1l80haZLCMn11GaLacRq9W0oMLlVCu5e83rYDnHDiLkExVEuXZ-w4rMCLhybhdGvC9aydVwXvGuQCWoUfFRii3dxSGR4YeYHwyfyOBsh2m8AEEzPO__QbO1PbVEVO-gomfDek3NMvBZ2kv0lnECN0d0YpooxygSQST095hT8OHwVMsiDIT8oBPYPxxzap_8Rk0OQFNlMSxdxolaF1gTau3H3dPKPa87Ki6jAIDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=m8XQu2t27B4mFk2f45O-nm2TIsVF0ddOCIm_xCjXBsvmtmcdNmA7ecc-86B2lOwXvyo6M2fUz1hhK1FkL7nPXFUEtKcAwC4zTIaOHDron9cm4yg1l80haZLCMn11GaLacRq9W0oMLlVCu5e83rYDnHDiLkExVEuXZ-w4rMCLhybhdGvC9aydVwXvGuQCWoUfFRii3dxSGR4YeYHwyfyOBsh2m8AEEzPO__QbO1PbVEVO-gomfDek3NMvBZ2kv0lnECN0d0YpooxygSQST095hT8OHwVMsiDIT8oBPYPxxzap_8Rk0OQFNlMSxdxolaF1gTau3H3dPKPa87Ki6jAIDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzohlXZW3EALSRBmld1A2FCQSlm2nEeOzUNSIt8M3Nn0hLCm2NycBU7mNQiQTJ_wmDmL0ynm6jSqKVhBF_gSP7k6CEq_E5xhhB1tl1Heed-nwALU-43rxUBBRvNS7YLU7tBq2aldEKS30u6TyIkEUwTpoTAunVLhga63mejQZN3sZnTOhEGvlu5u9deBbuYHMa85QepFPhuHBlh7o5CmgeZQOlL_42gbQ2umWjHusfUneNcHU4A0uSyu-odAP6koGF_hoxB3rWwkSkIGW-OUGZPP5IE2-pU2Ap5Qb2d6mg_c2UGzTJvNdVHbz5H8abYyUmi_TjsknltYzzymxcheYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA-yGPtX4eYWE8stQ4xpyioVtb8rnheRPZDXKL6-BJi6tLbBlGuGWHrt5NfnbKMonLzHU2pM3I1CEZLhLG8ZbP9ThsgjLUkRbfqLxse1g9uhenZkv98O2LDhiXmdZBsRbtbzOJ2UfjWEmXsGZdtUYGg1tCQQwJfo4rOtNT_SrP7wmDBfSDi5KK2BSo6oZteHUMpPTEtU0aVuJA7HO3qI2Xq4OqXkOg4SiGVQivwa9cfZzuBoP-G7QHReRNo-0H6hrKtn_tna-RvdpemW3d_FYj9us0gf70D4Uj_dt3Qqbe_H2DPab9Pu1E795WR62kkDajOQ1gwt7TXGIRjX3R-sxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_WM4ATyFlnrO5ll70cywIshnCgn_34nRo7ly4c4Jy8MR_3vBlt5LfN01jy_NmtPuxMVEOjyEwj6qe8FVuhbjgSHATf86wUdBv0dewRArw9MwQqhx3kojc5Pi7eWtqa95ZgHIrP-ipPYH0wpjN_A9gucC2s18ENVJNQ9sMzikxXAgWZlZe08ydukuxJPHZfGimp0WOquIIsBtBNjTx6NbNdZkB_hnUcNL_gVYWXz4P-cNEflJcUJSZQuekLazv00u6IdhXqx4zCuicJEGY1JfhlhGRj9IOuij2J0Dspgu8yI3F1hwn9FN3Y3mT0FNsqiZh_NKkQoZXp9OFqmtm02hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reZmQGXUk8KOM-yPqonVlz_K5iidVN1wTGCZZM7aQDTQ2o64fnrqvv4o2FP9jmN71o1V5qdF44Sh3mcZ8z0mQMDOqiC_j2fG6ZqUG8X0ggQDqUzBSr4Ze2QLrDRYubWM2MXfH0YLNefDTybf3PzT11VSpCGNqTVLXRbhFfpvk5gPfArrV_0HEn6hXlHTPqV8SBXImI0GGqW6vItrrteGewpegiD4mHklXpvaNRWa0JOZcj-5FV8U7nqzrPniHYwDd7hdWWV5unnW_xGMAGIJzaIDiMFiD3I4VyvMvFyJoT_a5s0fHDdLnDcYzUqmJG8c8q8uZfhbvt3YPnFtP1MslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJo2F8fqJA3LVRR5V2rKM2cwRx5zX_diDOn7vOqgLTcPXyRbZfVNkzGW_fjc4P2k0F1P7MpGGZ325I9ROygNTO1EgfTQOgmJ6uN0gRli7PrqAhCMZlT7iVPbq8EjQppXpcejYs7IRlZgHlmwn84iD3ioxw2mNUW933q1yMChMCJWN3E4TziCzRwK-k0jUwfjhxja9vHAP4mtFtIuEosNc91Qd0DQpr_Q0wBl4FqSgNsf4_olhJR1sRBUGwjWqKBlqCPCSkTNNAZO5_UtvYTgxc7q7rAWzRf38trXFlNM3JdioUZr9Au2oSwxuen_71idgy-1tQr7mzdTOFUssMefXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vGxsBiwJBfAiHltKJ-8iQvYr3cMasPNSN_wReVZqfKXvOboVoqsh_f2psxApPgNJp0QPQJU5oeRpaDcfRZYm5rTXqfC1v96i6iP3Whez8FruBGLQ1wVb7MYovx2iNZ-n52kpr1czcPUjnnEhz6nSDHidbubrlOgoVE7zl9OAdHWDCR7yGKJg5HcvPdiAHkolu0763qYcfioYXRk6hAUst0SNbu2pxm3XWkS_29W9Z_X-0q40jMhxNEa1OFt8OxNif2WO9ZfS5sMZq913kh2VUcLQ_ozTPitdzXar3Tjh6FupszA9lCZjkf0OIjny_2MkKqVSnLL8f9fablXrtF4BAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mjCYRhRgcjCxCZDxj6BU5lDMq_Pf7NJHxHGUn8t0DwpPvNyZgRMO8S5Wsdj95yo4DHnNtluudF21618B7R2AN1zCXCly5WwqiVqyQpqggh4lyS7Ed04rxgx6afOku6oUMFHx4xLENJaZGgDj5EwctuxjqSJ_PFISBj8uCkEsu5L_LmL2_0CeNGvH-fsKE-LZhUChc6Zy3ltsFXj6d0vgFz76mOppc2hyOQrXx1QG9I8SVC1Ai_ap65KtfHw5a9Y6AsL8hX_yKU4Q5URUsNEDiXOz_C26gPP9EfE-4UPl7Vlw3N3tJWAGKuSX2nFlQpM_IlxdWzqkpo4JfgCZ2ZSDAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kE3Hs90308TddlSGLcOzM01Sj73YZb-P1egf7eu0024CejrcX98QNPPuy5W52k8s-se8iHHEOJJ-1VRnK6wQ6jPnhjT92YF7vuLTkkJN1FBSk9NbBPN3ahHBEx1hvx1LmoZ9-Q6YHtwXbzoswE7Ky0_XbyVF2eQusTMLfcVN-kYWgUCVrinRhoiICQzXj1VBmIcIuuJbrAEiIiWJUD151IEspldUCacniq4MAt2zAc5yx-VrtGHG43IIGg_XfCfrOme7tHYEZHEMS-AIV3P4oMz_5BWVQBn36N-Xejk1xTUMmKfvIF8qErxRY76LPKza2eHq0ZoCbEd1HUqxh-JWRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jid2nFac3tH0QhwR7pf-wW4WjtxKSbplGLkTYjlbAY9NFp7JIjcoq6cV6E-oGjkmK-MukouwGMfqDiK4fIaUPlcebU6PxDLwCdlQnOv4KMh4_ciz0ihjM5bODQJsBzPVR6kSnqBzZhVgo9blBBWU2cZphpmadzmMaOLngsdKucgDcr2zr1ai1McyN09zSPtNYQaHdNvfAoTvfmoGrBGQ5Sz8MFcep7ndvAnCACeImOt9vEl6QOhrpd0uMvGMPX8JZts4HL90NFhfz4cPorwK0PCIC-7xyGCFVWJXv8FgzY6TNbxeq7o9fGEWIwPiC_-oQxJ1OBEhlvzpl738G_oajQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubMzo9nsLfXIjPtjB88d4GjdnjOL33tR82bHejnW0kuFogoN__KsQowm33HWzft2bqnctmZNpzgjEfoVey9ahMKKmlK9kDSeCAe13RBfwkUeUhvrX2__ioNoOJT-AShFmV4kvvst2wPvf60sRs94XWtDHNKj_0YeGDJBSdleD6w4UZM8StCVmKKWFiY8xVU1d9iRovw7b4Wp1mghvk-28SooUml4WfWzK3e7JDjub3fGW9qJ1KVWvaJHJU9q5S0O_DJpBXHEctfJ2fOHLv5VPUCctsotHLKBoj7y3wgAvVulL2dgk5C_zjfn8Kce5g14TlmNCPOJPejhh6txVuQU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=qaurponpLUamiVj_yrQhPkSBL87u8m3soUlLPnUJLNbLQ7dU8NQsXCW9iIOEJtncZZMeUzauowpW1svA2VjOG1KRhnxzznnZk747AWAcuOHU17HKabZ6pPwanw-VT3OFWMb9x1aI-9Us1LFsTnUU6-1ftMTuMT18RyjstsmFUWHpTgKdbbDB6nguJs7wsBd-31Wjia4HOCYAh_fXIHVFDemVvvLSBJSNucqET4Pym-4RZ5NKSpzdKRCLXCSW28ywTxAJuwxabfXEW9K9b3nXQEJkjUctvvnYxkgaHmS2Fa-P8p53zX01Akn5YoheHOhlxKCcIC1BwaueLFcRE_zxQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=qaurponpLUamiVj_yrQhPkSBL87u8m3soUlLPnUJLNbLQ7dU8NQsXCW9iIOEJtncZZMeUzauowpW1svA2VjOG1KRhnxzznnZk747AWAcuOHU17HKabZ6pPwanw-VT3OFWMb9x1aI-9Us1LFsTnUU6-1ftMTuMT18RyjstsmFUWHpTgKdbbDB6nguJs7wsBd-31Wjia4HOCYAh_fXIHVFDemVvvLSBJSNucqET4Pym-4RZ5NKSpzdKRCLXCSW28ywTxAJuwxabfXEW9K9b3nXQEJkjUctvvnYxkgaHmS2Fa-P8p53zX01Akn5YoheHOhlxKCcIC1BwaueLFcRE_zxQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=J3YWZhJ39YaBJUdl_wtyURDU88rj1EU0hDfTGh8GOJB3LmG7bKbDZnKzsFR2WwDh7Faus8ghoCyaH9jI0UG3hCrDE6RW1D70thXuxiIObbpJERitjNJzHx5fBZGrVgyK330kbcC0OVG5e-JegOSOeazkwr8v4DlBULO01c_5P0neBPDlya1juVCZgXgDGF-PBoDAUBrT0zdqAHRZThCLkkjrSPdL-mmbFtdDYFP_QNdOA5lIMX8s3hnb6_HF2JzfkRXkTKqioC4LCUwst6Jek4UQQZJjzJHoucQPULuA_PgGR4wbeYuSoHRM249CUZgtsc-ZN56jHiQ4sym1w5kwHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=J3YWZhJ39YaBJUdl_wtyURDU88rj1EU0hDfTGh8GOJB3LmG7bKbDZnKzsFR2WwDh7Faus8ghoCyaH9jI0UG3hCrDE6RW1D70thXuxiIObbpJERitjNJzHx5fBZGrVgyK330kbcC0OVG5e-JegOSOeazkwr8v4DlBULO01c_5P0neBPDlya1juVCZgXgDGF-PBoDAUBrT0zdqAHRZThCLkkjrSPdL-mmbFtdDYFP_QNdOA5lIMX8s3hnb6_HF2JzfkRXkTKqioC4LCUwst6Jek4UQQZJjzJHoucQPULuA_PgGR4wbeYuSoHRM249CUZgtsc-ZN56jHiQ4sym1w5kwHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=hPPyNeDUdGQ8bPEso1oIPlzsHGre86BIbQa5lryu5eJeU9lmfLoKEgUhiyQ20TcN-QfcSBZ5U6UCeL1xkJikaOFFCH6rC7-JGiMbmHee1kgFKLaM_vsTjL7f8NUxHQO2N1lkIqwsz_vepyIbLWnPHeaD5mxMhgjq4Dj9UrCjgX7yu7g7GIFREC6jhBcVrh9F_o1AyFnQwZWN96afiFDaSULgNtv5UuMgY5Z29Qrq5yc-42hjmWWrnSzZb8hEunvy4T9we836ZyOFhz4bvVB2kCmYtUdpldgy38470omoxQMorYNtMFFSBzHdx3z_ysLbbYftKYZiWSSLJxKXdXdcvbCDCO1Vg-AX1y0Kr7s4T9Y4L5jBgOXg9-w-48RxSTOpy6JMSyKSEecSQDu9rsF6GpCv5QNmZbos2ph7ChC1uPvZ8-7wIEhfr6Js3vPupQIL7aT0QUb9c45ab7AO6_SQ8EG-BwTo_sEJO3xazhSaSh3m4kAqpPQJSeTJdJcZICpRbH5i5hEu5XkI6rP6u4VRN83Bby0F5iidzwX5BP-HDkfTu6iiBFIRy193oJlsUv1xjIs0gsMJb1wUhNGNSzPeqgbHy83xnmLIQYTpw_jZuFtkshGtNL6AFdkI7NtbcYWL6mDXdjPcfSFpBLcJ92sZ_MSHiEjRII10RjP0agA5fMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=hPPyNeDUdGQ8bPEso1oIPlzsHGre86BIbQa5lryu5eJeU9lmfLoKEgUhiyQ20TcN-QfcSBZ5U6UCeL1xkJikaOFFCH6rC7-JGiMbmHee1kgFKLaM_vsTjL7f8NUxHQO2N1lkIqwsz_vepyIbLWnPHeaD5mxMhgjq4Dj9UrCjgX7yu7g7GIFREC6jhBcVrh9F_o1AyFnQwZWN96afiFDaSULgNtv5UuMgY5Z29Qrq5yc-42hjmWWrnSzZb8hEunvy4T9we836ZyOFhz4bvVB2kCmYtUdpldgy38470omoxQMorYNtMFFSBzHdx3z_ysLbbYftKYZiWSSLJxKXdXdcvbCDCO1Vg-AX1y0Kr7s4T9Y4L5jBgOXg9-w-48RxSTOpy6JMSyKSEecSQDu9rsF6GpCv5QNmZbos2ph7ChC1uPvZ8-7wIEhfr6Js3vPupQIL7aT0QUb9c45ab7AO6_SQ8EG-BwTo_sEJO3xazhSaSh3m4kAqpPQJSeTJdJcZICpRbH5i5hEu5XkI6rP6u4VRN83Bby0F5iidzwX5BP-HDkfTu6iiBFIRy193oJlsUv1xjIs0gsMJb1wUhNGNSzPeqgbHy83xnmLIQYTpw_jZuFtkshGtNL6AFdkI7NtbcYWL6mDXdjPcfSFpBLcJ92sZ_MSHiEjRII10RjP0agA5fMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMd50f8Mw09Xl2WjOxdDBdUdRzQjrB1s3U2wnWnvyIgDd0z7NM8w-CPHcwbHG8Hs-Vw3oDVLTCAnAhmeb2RJhVVFFaLxJ81fxxeYkRy0NmHUE5OMN82vGABHn30_5Svph1NyjINYMc70T1nP8fZoBRYvmGSJ1aFFrYx5wdq5SwdHMqwkvozEh805qy46qztxIn0Uj4TZ1pwfvG_099wxy-rINApFANOTimlUlSN1UoNWmU-g3Wdov4j0avzqazjjx1TgkMQa8H2VolsbRoCGB2CQ6Xb77yg7vmTNW7ZQ3iFb7OjPbaTzIkEvAkhCQiX1a5r-4Pe_CUb-u0m-GsfH8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=oGNMnauGEuExEpxzubFErUBCeQMdikpXE87b9BdjXE9-ASzI_CriKEKC0TGS-IJ6q07yIQJxMArZHVz2dZk-RxjXBhAp2WAi-Kws7UhWVTAGRHpW84KBN-bQf59PlYaDNtVPL8t2kaBQQmWh4LUIDicazq3RiWDhkxW4yXLOH4JJy5Ga0OlOkRHg-64MH94HofimCyhl06yfeokc1sqIlicze6GhGsVaLdmWiuh9wrfNiECgpb39S0WqLJ3CwY9am22u4fe8DwVTylL8qnfvptnRlH4a0wfLCecXU8dPC3Rxjg62JW-CLPqIXfrB-ojOd2LfVwzsYEHLT2Pab0o1Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=oGNMnauGEuExEpxzubFErUBCeQMdikpXE87b9BdjXE9-ASzI_CriKEKC0TGS-IJ6q07yIQJxMArZHVz2dZk-RxjXBhAp2WAi-Kws7UhWVTAGRHpW84KBN-bQf59PlYaDNtVPL8t2kaBQQmWh4LUIDicazq3RiWDhkxW4yXLOH4JJy5Ga0OlOkRHg-64MH94HofimCyhl06yfeokc1sqIlicze6GhGsVaLdmWiuh9wrfNiECgpb39S0WqLJ3CwY9am22u4fe8DwVTylL8qnfvptnRlH4a0wfLCecXU8dPC3Rxjg62JW-CLPqIXfrB-ojOd2LfVwzsYEHLT2Pab0o1Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xly69hYBPF7uIts7dQd1vJNdwTfkG6hag7QOT47ZcVq14Hr_9SJa904QxD1eF0SV71UPsC8aHwy_f4U4fISwKZ2Gj-ZWsD8CshA0WZ40iyo9LWjPAKzu-Xiqwyi_P4JFBh8WFqm_4YW4dyGebZP1jUkTCnUo6jrKb_oz6B2D6zCKbAEiM8vuWF8ZrL74zm91L_lZq-MBQI4OYHIh2jWLjRcC6oha6kF49H3766hYdKWalXIdQSrAT0T_8FhQNGOMaUJ9zAjTUI7NyoP8nY9btet9VrKGbrGpGF_9gmVHNtll6-NfGgD1KIlN6KAp8BcX6lNH4Yq9x4CY5lo8tuajxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j856OM2FMcWtgj3-vGgGItDhNTeBJHC-4GSt76zpcvJXUxe7oTchM3AuP2hZ_6QQTHuDiIXeDwKOfSxVDYtniohVTZYYM1guOhpvILHEMSXvj-zrhceqCx94wPDpQ87wKPuw0QymAeEa70YExttkiJ5OSFl6a8WY-5y-07U118KaloGg0FlYkw1uioqGDc2tJgMAQ21bIqk1U1elEaAUrpVYTZYXZ6yvyrm7ZD-hZIM6kJCjeBJNJwajEF6G0mxHlrelrmMTyTL-j8ALSKx2WYmETZbPGSSoeu6HsAvftqNoCfG82SPcvZ4RESgIZ1WQsRvw4F0V2QAWoDDE8td4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUX6A_nXjTJtXDQoNNV9RR3wZaWHewvci7ObLmVkiZ3Vny8aWvBTS4MrwN8W1Ef_nyW52ZbyEvin_XPt6Mcwvoj7PCMsiKOmmJ3jF26kFemO_OibmVGw1THzcEM_CW8udEfPUWtqk0Kd8U7vyAUZYBXzHESw7DKmTmRJD-E-rPKOWvP8bQ2l7ovMAlKgsI7SA71QgNY0-bQaagXV0yHahQpRa52zPCPX1WUbMrI0nJoDZo12S9qgfaG8kU9RXctbtP3FosjCQreFjrYbnTKBnBTGfcIvJyosG-ayCITTFGuXLRewVoXZxtAydq8U0yzMqRuQk8X3m9MI5sdGkyEFQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lT7HHtPACUesC4gy9dh6FVU0oq-YTtqP2IdehBhAHLtsSibuyA2LpDyjyaN1M3g0dV-5bHq8nnXGsVQLWd_vVN9p2z0Yn-c00KAEsmgNSXh2rejfyuuvGTiQYMbdx4q70SFqmJBXIErKe3UzIQ5RgkZYjoZVOsfdVGTgARiuwdhorwPJloNVykvp6Cz3PzJMsjvcHZam-V3tuBFHF0cnaYUpba-t1YGRB5uPGhjIp-3xNQdtejW8s1rCd7u7CrY5hXYeOhj2EQn7C-rAudX27UPOO8jS27erPJAeZtuCMfJHkSPkWMXDlr6-vJMeu4trzf2gzJmvBVaGOROLSRXQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mmx_3bsUEtHt7kWH6RydFDoy2sPvVGvjHa-OJ2T1159RsSuyp6TdjucVhQWHNl391XJ9Iy0Gd185IrU5jB-4At6QDlAX2mZtrfWJyVCgmxQDSJZ1sltjlQT1G4iTsh-iUbZwah2iwcNOrHaZ-FrWoExyA6EXFLD35SpPjiZxTnA7LR9uGsz0ce730zJ8iZm8xXB82mnCYTGwL8EpWDnejD9_QG242-Y6DziHzTf7kwfenWkRQoacngLEnJjiKJyETJQWHt2uMPCJ4XG5K5GgGsMjBLCOJRfLS0GC_kcERFIeJUn8VmKZUGMTN7KQ5HuNLxginytcODN14LWC-C-B0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baD5aMdB-ZLqUhIpgAFrX3kVMO53lt53Ij2Hu_vyEpGVM8Ff0C5rjn10ZZzyKBw7299qfqaUwFDTf4pclDpugUcysTWfRtMt-m7rfsJJQ211J-FuW9_xLJ84EFAaXcDuC_PCP32QiadJ66xxNkbfjCkmZIMWIjWJXyviQzy9IGVa6_h1kh_dkFSBoKc1lR3AM_UsYH3C9MWfykWz5pUBvOyDNIOMWRgC5mn-NiFLzXvZqqWXa2NqV9ma6REezBmnzmFT55ouKoZHWHK9BMc8HkQg-pqQLrQzo1rvFWmjQCrA7P_TQhembUQX856YGZE0Pwx8Z73m4wrzLuWZ506mgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-GDcy1O8v19Hm6o9QoRoFpeUKxf3FrdqNNJeW3HR4iRWQ_duzhe0rvQvfetvQM_EvjxLvEMkCmghfZtmoYEcXzfBdsWpfgrEPYCUdoju7_nS68h7a0HIRM-q711AucHXOmBD49BVcNlaAixGUR4tt_zJbomGN0lad6bANwXokAdTxypORTWJFeCZCJ24gLjoN3Nq5QYU-gH0eQBSL-72K-CzQPwSLlJmq3eiKLYl9RZ9ssMdlffrT1n7YtFwGiXAmyCm-OzSuJSHx19aofsZ3QBnZyvB2uS2aICj3mjQSXTXt0VQjrLeU6773VyjZkHnHsVdgehuHN1n1VUhLO7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qy2NRVkoq5_LBUZqvtlZoabfQZmeGDzYaf4VPishfzR6kJ8l7ZDvgOGK4uSRzyQcdS7fTVnZIxDqCYVutFtxFKyuVpuIvFG_JhAeRbuVwo7FPePNrK-lUNH1gmdkowyBsP5TOpGA8F-_vRhhKjo58wMGq9pHQWWbg28i1Jn1G396B3ofVM1EGHriUMHnPWGJmIq3apRpc8Jl55dAuwrUNOW9_A1raVx2p-SULSFtXpyxp4EUIJfa_xYeKPasy4bl4NpSwIPCm0DP_fHRbftPl25CwQ5n7Hd9rJGCGS29dhwDW4gCmcqP1YU8jUYce9iQWW4WmvKKNiEaeZD2JGJkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DixqOEbihd_lz9jF4c58Vvw6vjF1MwhMfhDRcv4iwKQtNQ5VLyOqkcLlF0B-mLkLwr-EVu2RAyn4s-UY_Si7P_p0QU3SUWap_yYC5j5Y-y6E8HWck7aGrmmQmNOmtjRc8-VqX4pMkPY-iP9MlF8jLAFe7WaOIgyxPW4yc1yCqLAj7Y1WFSOpZSEL23PSZ-iyqFWhuN4xyYcgCMAXKoNIl2nIymJMp5sw_so3lTtT_cbJ9rvl-qUjg_FPGuSrLL8XALh3-CFPQXbl_3HPSYJkTqVoox4zur4zeYrl24kKCZrdYKhWnod_5xhsnILB3ltEuH3TiWtEwMm__YAQduJZlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dldho_j_a4ajCBHUGE9WgMMTc0kUsvVGXOMMDdaWJaJkp4SgAtXlVMZPUbHR-M23d2r6IY0I8iAf5yfrJVaJOJH1v5Qq7GoGwyu_qvtd2SOHrVPrz4_sT-tRNsKYkXF7E86J4paJY9ONX5LUog0ZjevZb3YesXlVvDxPfGkZMmzSY1YD6fVN0lZb3SwcfSQQgsAHuARlDCJsq_3EOZzGiSn_g4WG4G5LNkMarqTAt7v_iKCUIbxl2TPwzoYXFGIxL8br58K2P_rblyOifetJm9-RhKe4dUWabCM6aCwIER1-p7lJBUCCWCZhg5WRFjjUb5s9QULaVGwfI4GN6wc5iA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C59YsJQ3_Hs_MOLCWmDj46bImptNCujnJDIuvkl-xo6U2_7P3UlLLamUl0sypN_3fOzroPlBlyHqJm7Q2zvp8Pe3mn2GKuVLh9tqWOQjt1roOrwQ4W7yK8uG7lVGdsVmX79lWV-rJXNKTq-tc4ZaAtPMjSK_1AborHk_S9ZBST1MPcujOR_KaMzkjHopB322oHBDX8uoK3aDJhH6NrrEZ1H-7cj-HQrJj_l_stE6X81hu_G09M3r2duRoXFDfefRRRl4Lg97w4blFtjZcZ-PNnzHMZfRheMLShsqPtz9DFmu_j9StVZ8F8LkvYAojHyOJ7A6jqQSW3WS4OtVOr62Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYNHIwTiF67u1L1HiYHSr4dH6u9jV4QE2ynnw5h6ItM94b4USHn6aoKSlxy4otjHx3nQdNhC21nkKZntiRrRGQndwnLHgD0WI9nDaaZ9j6hu1HUun5JBIfD0_3F02Q87IVc7Ox0VPBlFR9H2EdLgb74eWp7eXhA0jYJHJgHKrFgOlHexvdUyD4S0ctA3_EZmMeZaflRgklajyXPtsb60AaLV6E71Y1n9JEvRFwn6KO8FF8YughWQ1jzuVQLX7hNgdVuZ8y8Jxr2z0hGDLTBLY9OjIw89k3KUUvx27PvDz7hJLs_CJCzU09aSIm86mDjaWEQhHNHiwlRFB6B_mVSEng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FLZo64TbODVUs6FfL9QBD42LuaOMNcjs1IcWYPdQ0sxYM5Kh3Vm7tzBRm5PcUlDCliLGOv8aIVoTf8V0iRaz2tgQTLZmEjmI74Ae5y7TEwihMiHsO7jQWlcCkxRvFE1np0wtpkxssB9iztjs6vrAYV5TWvhg6Cy9LMesrQlX-W3QAh6Gsh2gu0y1xCbsURT_TwfvFIZyLvqJ_KD82RB4qdeofDtfI-w30Rx8GCYVxgT2JR9NwpJf6LTrYDmdl1l9IKJyXC-HF3w4WCc5-erXiBNT_FpneKnK_yJVG5yTQWhfhvPha1LhWkKmUR_777UCuBP0BXg5d5qU7cDvBGDwZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRPN05J1rSmZbS7bhGkoiEX3TzHIT5I6guVEtiBkp6JKVQFInsO23Q5XBKE-ob4vjHL7Wx6yJNKltvuAeS46X2b7mTkE5jcLYf_JOnehlNBlyHLmDPJNxlrZBYBezlTiXngzB3mplvlthHiivtdK-Q-aRCK1fThafFV6zOdzh4RTP74VMLWPeyTdYcUv6r3aU17ZCYYqTbDBNeKlAuyFwdeN9mFA6BJtOAUDhvFR5F6RBIyBeQUa5AMPgEfxXJzwEX3bzppH8OArzoRFytjiKMbAe-wcfoBMRSjM6WAzM4oy_SgbwoPaJjslcZV55ZwwmO-Y-ToGdD5xgG-nXHhgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wo9ZTfn3xmoem8LjxNmNvUbDbVZc8yg6-NNR6Jw3VUco9_5-J_Q8neBwCKXCx9uVRUu8eHuGiz8cQP2N9ZehSOqXCuy31KUv_Fc_9HyMpJE68D7XJrbDcargSudOSMyA06j6sGpeOpP12inrX33G0SO9AdFXcrRTy58yZN3-3SW1lYBs8ldrnxtIg3QlW8HYtgiWAsBrAVK9KDVZ7hhPHOS3_ZSDwVGenKtR20xVj80YjDBQkRXkEmfroRWC12QmfOUdvEvUAZUHH7s-matd-FFAIsLgvph-26lhJiCZQfzwBCOZJwaOP2QzcLzfXdMS24c5mxrX4zBlYQjeMgR2Nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRHSRlg-9X1pMIwJbJSxafInMVlfDKcnc-F4D7MYHBZzMjW4NZnyOre8GB35C5BPELsWgJZ6MfuWpi_4viO83djvdhAGCnoWwO_e33nqv4HXjmcVWIyZxGurvYAqM1BrKnHrnscbCEgZR3g3JRXpjTrdr4nn4227Tj1CNx3Vi5KlC2HOuIbOsbWRyc0kH9t73n-76VeoPCXXThlTWedFpApMIaTVderOZ9zHPZ2dR2uHM3hSLKXp86VH6EP-nUsNL9Ox5pEJN0u2E_bG2kAtWUGOnYyd9aUcaATG4bvxtp1QSN9JJ3ZD9Hh_HAVYq6D_AMnBP3k3E9pOZRWJslhwGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=J2i9c7t87ZYJoB-Wr_hAqXHNHeSQYeaDkGiOjZ2rTrvuVJqkN0JoL19LGLNCMLBlT_AcqpqPqYPJYd3MNk1a9OaRXv_uMa9E98NaxuUuGWlWdoAhoZGmnWZEe-6UdUsFdjBajcSJreZ7X4Nunp9AwpjD_hsOcaCNJKCQkgV08RENdH-STTjOjOzr9nvHpXgH41pQVOC-MNiDofhrcbXGh0CrPowKXDXS6iybS1neKVsxcia6PwkV8RqTbUz8i70JJ07u9yKJ8f8SPMNT9R83vGpnSOOGhGyJmE9IJKbBnu2wGmpfPZuXOxakUWvtg-7DOV7yepZX15K144UttOzU7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=J2i9c7t87ZYJoB-Wr_hAqXHNHeSQYeaDkGiOjZ2rTrvuVJqkN0JoL19LGLNCMLBlT_AcqpqPqYPJYd3MNk1a9OaRXv_uMa9E98NaxuUuGWlWdoAhoZGmnWZEe-6UdUsFdjBajcSJreZ7X4Nunp9AwpjD_hsOcaCNJKCQkgV08RENdH-STTjOjOzr9nvHpXgH41pQVOC-MNiDofhrcbXGh0CrPowKXDXS6iybS1neKVsxcia6PwkV8RqTbUz8i70JJ07u9yKJ8f8SPMNT9R83vGpnSOOGhGyJmE9IJKbBnu2wGmpfPZuXOxakUWvtg-7DOV7yepZX15K144UttOzU7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlFMSrSSJLr9-lSsL3oGIx3In6KwtGRICUt1m3lkO1XEYhHdMd5ZE5OFHkgFCsoOV_mTev_Ft5ynHDM3BBLkCbjrs-NHdN4VBX2ZjPeblvUAnFIW6uahZsHF7mnNXJvabmANQpQdUMJLPFbcGOQ6KvznUtM7YrSAZb_7X55SruQ07qnM1x4AdOi2FbPGdp8wn2n4oz27Cm8JF157Vs3dK02MlP51RwGYCcGyc8LnTUS7h_eKqL8DNuCVQbnGTM5z6uD0KLYXGGpG38gzoG8yWxzp5-VjDwb7ZM-kCyolHQ3rQtUDN-mP5OCmQbGVTemKmxPm7MLCtOCryi7vBWRgzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VC-P8Jf6nDxZ9YzRS6-GIg6Czjt5ozRtjjdWfZ7G0g5plmeAKtflMSDwyIAMBmCnxttZMrb8gTHf4AMKWiZ2-6CBHdRQONzCTOh24mcYvtdq-Cnzkf1M0ZwdEe0cF0ZKZQaQCfEt42Cf9ODge3JJxHp2JQMPaBkJyXdGQHwjgcnXL7V7kz6-Hk7knhr9BTs3ipFX4Fj3bFNTLs7zaNwmfvkHTnWjFRMpB4LfaVmd2S10fh8ZMSzKnIEo2rdwL5eWZTdEj5nXtGUgPVSJAKeHnsX5pAd26AGmLC-vVhAhVktxUqVFAPISGEsk3riCDYR44KhOtAzRRj7O5gs44YqwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k64g2i04RysPh9tD6ziWU5Ey6ywdxV6o2zuWZvtitrm6ZRiuxKCl-DIJogGALnV8QZlwwJIuE6DcsrBuHcXnuTGTuY-ogJu4anJ5ceAVJ0zHoJAhXDCpEyv69g-64FjWymz8VU9fQ5ZaA58kMfmWYkgcI03QtM9DGp_-rZnIzUmyNNsu91lyXskJkqODg-WhJnN79hEEmJLRYtmCF7tNSPbxt3P75DQ2pdVD8fULuy-3eYrllx8ZyKSBfCy-eaBEggWsxim8phzSIxnADS0FHkdjd3gw40UEtto18XnmLxJ-DL4s2RW4Ih2BfeF5h0vheFmamVEJHsFa3jopKhki9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=bmhBecqcStsFRToBTQK7W3ihrG1w40-fbSZ03eMjUDjr8QjlW4B1plEC0Rmbys-x2sSv74eHQbn36nzcQu0YIdAOY9W9Ti_p1JSPnZBfhV7QfmtUm2pMw_fm_VPY0Co4MyWjUZM0t9-M6000hv8KGbt7IrBqQqM51X8QfrlHoHF2vWD9NauyGLjj6DeA8pkQlmJqdm5REUUtHxIKZFbETkWrF9bfPeAVmm6_E97bHysPBl5tnNyyxAir4w2cRXn91HeWYaXVyY7_3LeMuObXH6bwOm06PheqoJt8krJfkqW_tQj8atX7W-BcOwAhoENZbmgrBa8-bo7YCHP8ZR2p9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=bmhBecqcStsFRToBTQK7W3ihrG1w40-fbSZ03eMjUDjr8QjlW4B1plEC0Rmbys-x2sSv74eHQbn36nzcQu0YIdAOY9W9Ti_p1JSPnZBfhV7QfmtUm2pMw_fm_VPY0Co4MyWjUZM0t9-M6000hv8KGbt7IrBqQqM51X8QfrlHoHF2vWD9NauyGLjj6DeA8pkQlmJqdm5REUUtHxIKZFbETkWrF9bfPeAVmm6_E97bHysPBl5tnNyyxAir4w2cRXn91HeWYaXVyY7_3LeMuObXH6bwOm06PheqoJt8krJfkqW_tQj8atX7W-BcOwAhoENZbmgrBa8-bo7YCHP8ZR2p9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGj1ZvgAngBmDqZNV83MGA4VbS6B0t9Eb8JjSrA-x5go2j6P_LdPrgvUGozNBN1lcsyufoVOiL0Q9iaF7AqsdvtGU7Mb8B-jxPU6hd9kqd6n4SUfhnOL_gTtNJuhTCCiw05gR4XkS7e6HMZ4ApV5VlOgIcW0C9gLlepWlK4sDY2r8TI1dt6Eg6LvjLiZQx3lZUTrMA6gRI7mitanO--k2F_exgilrBUMqcToe73q_rrrHfJFB89zmSkSO-pAiUjBpBYGl48mfRlxqZXFkC8c_V5ycHAy8GPSwUtX4BaFqke_EB3a7AqW1pjaGYwQS9T8xwdRbbaIAPsyyDHBEOwd2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=Rlsyz3VG-CxcKQOK_QbkYjhJaFIPItZjmsvcRhERk5JawEPANfssrHHC9SPqC8Yep3BFLfT4qa60gWvGh_3syg6JTFb3PNoMO6UedmUXHJeNrQs0wVjYOwPERgcOgHGW1Bne4qbW788kDV6Q0UIDCoX2gshAnASJPqxp7SPm-Q3u8PHQoozMIih6rAnb7L-x-23qSnJVL4j7Yy8yewksSIluWByyOLFvGW_U23eHz6nC80hL_ENX9BHYIgOxvtWAMHMMi9nbT9b7MvlF3X5Io4v32CnAekJ47b2cuWidjf4zg0huB0T3q26AK2gzBqM_t0ihRFTvpvwnN_3uQT-BYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=Rlsyz3VG-CxcKQOK_QbkYjhJaFIPItZjmsvcRhERk5JawEPANfssrHHC9SPqC8Yep3BFLfT4qa60gWvGh_3syg6JTFb3PNoMO6UedmUXHJeNrQs0wVjYOwPERgcOgHGW1Bne4qbW788kDV6Q0UIDCoX2gshAnASJPqxp7SPm-Q3u8PHQoozMIih6rAnb7L-x-23qSnJVL4j7Yy8yewksSIluWByyOLFvGW_U23eHz6nC80hL_ENX9BHYIgOxvtWAMHMMi9nbT9b7MvlF3X5Io4v32CnAekJ47b2cuWidjf4zg0huB0T3q26AK2gzBqM_t0ihRFTvpvwnN_3uQT-BYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grqXE2rykVEq1_cXh0W2rBtVv_ePq5AAh02uI4RWbaRp9BbWmz88AqdffIUA35ZJKQmQtiQIETLrkUfaQYWSQU4scxGHW23wNNiLuWB7uVewUzRxA4LhCNUaE9mEInjyl20ml8J1UevSlsr7Sids-EGyuOI2z9dGKRtYJ9K1qGfJr7bCz4RSbIeqkj4OQc4egwNV9Gr2vy5tN75iScubjmOjF_wRURHqiHuKeIVDftyghSIrCiKfBR-ilvcq7ZQM3AZVM80bBzR7NPzMqgtXattbNNzNugpLyU0QXVndngcrd_0YwWWEth6UAkSM5ct-mGzUBehkKSyz1GJPAnXryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEl-zkcUVR-MfSykX2YNlcRMBuODZohfinH-AdDMea9KSchj3m8difZi1gZ-ixMHvccR6ZPyrwYdni95LiLXhq538BiccSkk12MbC89Lso0B4_YVJ61NUPEi7Eoy16Bgndy3IpY0NhWxSk2nNZVu2maCkfXtw7H_V-9HuW9zgET61b5khEMay7eTUFqv5JwLTsksQTUr_V-7tbonUm_puRT5prz-1yMm99o_grrSD3eUdGhYk6IpJbzYgkptB0WIQsX2Q8WqgqCiNePcLzVAeaUlLSQmTZSdzvqVs7A84OfflBxUbbiTbqan95XDzCzNEG45GvhawE1HVLugJ7AIvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=un8EDcQmOKhIS3M0LjWoriZ-AszduDNN0e3X19iyP_TnqJ3PzdiYPN86Mtnte0wM7pOyOatuU0pEdoSIO0IV1_KG63g4X69zfVHklu8XKYarfdeLRevRjHtRAovV-QTM8KRws1DaGk4HSjqU-LsIBHNf2478NhvSLJGTeG-J59HuO9Ub-fM7BsivhkHnDgP5sTmpkGZGsnToWNdSFqeyUYTGZ7JDLH_8p0e8QyW9T44KBcvdSe6RXbY1Q3-6IdoAA1hmlW1-AqQYPI_qn92mCsajnBtDhKmYHGgi5tU17n1AYfjYNm6wz8lwSVb-iC8kcKWKwgqNJcDtI-1S9lldTUzEBIpPPMRjubTAmA1rew35jPBRxD5RjoUhGnkOj-aV2V5xDeDhAj5xVuKrW8Dx9csmXz6eGAEodMqLvydglYZyg--RuW01Pmx9jEzdaeFnP7fxcXbkEmLLYYwaXHQgtGQu1xjvxELOZJYSE1uFC3-UjPPfGXl96mWj2MQASowopbzFUy-g39y0Oko7AM4biLj-6Lh4qlfknAztyyfqj6gakXFtAWivAy9V34JqbwJ6FhKGDRIyqX4OhF41gSMWBLB9HOrc49Ge4k1jyQFv7afgSe888AZD60f2DbeTNyRCbPnHZKEqsLeBx0flxegJ824B2vnvuPSLbu7ax5VC_zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=un8EDcQmOKhIS3M0LjWoriZ-AszduDNN0e3X19iyP_TnqJ3PzdiYPN86Mtnte0wM7pOyOatuU0pEdoSIO0IV1_KG63g4X69zfVHklu8XKYarfdeLRevRjHtRAovV-QTM8KRws1DaGk4HSjqU-LsIBHNf2478NhvSLJGTeG-J59HuO9Ub-fM7BsivhkHnDgP5sTmpkGZGsnToWNdSFqeyUYTGZ7JDLH_8p0e8QyW9T44KBcvdSe6RXbY1Q3-6IdoAA1hmlW1-AqQYPI_qn92mCsajnBtDhKmYHGgi5tU17n1AYfjYNm6wz8lwSVb-iC8kcKWKwgqNJcDtI-1S9lldTUzEBIpPPMRjubTAmA1rew35jPBRxD5RjoUhGnkOj-aV2V5xDeDhAj5xVuKrW8Dx9csmXz6eGAEodMqLvydglYZyg--RuW01Pmx9jEzdaeFnP7fxcXbkEmLLYYwaXHQgtGQu1xjvxELOZJYSE1uFC3-UjPPfGXl96mWj2MQASowopbzFUy-g39y0Oko7AM4biLj-6Lh4qlfknAztyyfqj6gakXFtAWivAy9V34JqbwJ6FhKGDRIyqX4OhF41gSMWBLB9HOrc49Ge4k1jyQFv7afgSe888AZD60f2DbeTNyRCbPnHZKEqsLeBx0flxegJ824B2vnvuPSLbu7ax5VC_zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=qMMgVn3RzfW_8BWqr7zyVYeT0i5k2cjSzfSfB-APrO9YSP8Yxe5TgSa0JRGIwzXnMw9mhSd-EGeyKTODXvxHIzaHtvlbj_nzUIGwl124znJMlO5BbeaHDNmd6mczCv6iKBLV8zTvCU211Fa6lxgEymvDYvFVwWVR9KgUpneBSswrHwYErFOu7kEl_3Qpqr7B-9W7j8gBMArC9pF6I2XcaWp1nXuu7KvkdQ87OCcXfNb_0BFEqNS55gA-kKYkvG3TOF5aWhAOGN2qIaxXEpYDFo0uEUGYXERKP0lL8hoZzkk-zw7gKPPAqgRXajZwExhfHCxJE9Y_YKG2iWexsfyhyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=qMMgVn3RzfW_8BWqr7zyVYeT0i5k2cjSzfSfB-APrO9YSP8Yxe5TgSa0JRGIwzXnMw9mhSd-EGeyKTODXvxHIzaHtvlbj_nzUIGwl124znJMlO5BbeaHDNmd6mczCv6iKBLV8zTvCU211Fa6lxgEymvDYvFVwWVR9KgUpneBSswrHwYErFOu7kEl_3Qpqr7B-9W7j8gBMArC9pF6I2XcaWp1nXuu7KvkdQ87OCcXfNb_0BFEqNS55gA-kKYkvG3TOF5aWhAOGN2qIaxXEpYDFo0uEUGYXERKP0lL8hoZzkk-zw7gKPPAqgRXajZwExhfHCxJE9Y_YKG2iWexsfyhyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8hf3e0HHwrOaaZtbQL5G7afArJfCnWeU28yk514_CBeaUvMgc-DEv-8klurDHfnptdzCluj1tqoIyYR9tHpzQ8abgyL2v2gnXEUifGGw7-_ris-RKSYLB4l2_KoD_PwkyYDBA0RgP6YG9HoES1ENGErnv9HRM1BGFEU-s7zf0fIFpmJgY7V5O80ezmdptjzNdGhT8h1ZwTnZEqM5Flvg5Wfnfp8D3kEgiuhjfIJXrP-_fpHPXiPv0bwIzCPzZPo4xREgxA2MxbnhHJWDYJmjXcql0Qtq6nivBdOwpDVaEPwOFjtS-fvBSggzqhr_Gv2UUjUKeXUzv5kInTaacVVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=myQnlijReE1w_Je_E__RLOz5ThnsHxUYvAmhG-LGC9jiedQ-o8mXpLQr8IyAsvOA4mNDWJMgDzcczUhuyhQ1vSUfgvPl5HMMCWFksQMsEoGW7wWRnXmPNNOkymWBZgYQ98MkZBqcrQiAl1XEuE4CUWfDcwjIrzDpN9clNZSxPM-f5TwAcRaHoNvNkqUN8Ql-GQaynydXKnfiXLSBbWPKkeSmglFeOHLWvuZkW7Sok5WKDzVofoQfxk4Y5I7OQZNcrQK7H5-hL19FbbCoomJ1WT8tkmudy2ZOXBjdhZA4LJHnL8MlYg4pVSopKEB5C4wvCeu9CoHt6MqtpehNE7p2GzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=myQnlijReE1w_Je_E__RLOz5ThnsHxUYvAmhG-LGC9jiedQ-o8mXpLQr8IyAsvOA4mNDWJMgDzcczUhuyhQ1vSUfgvPl5HMMCWFksQMsEoGW7wWRnXmPNNOkymWBZgYQ98MkZBqcrQiAl1XEuE4CUWfDcwjIrzDpN9clNZSxPM-f5TwAcRaHoNvNkqUN8Ql-GQaynydXKnfiXLSBbWPKkeSmglFeOHLWvuZkW7Sok5WKDzVofoQfxk4Y5I7OQZNcrQK7H5-hL19FbbCoomJ1WT8tkmudy2ZOXBjdhZA4LJHnL8MlYg4pVSopKEB5C4wvCeu9CoHt6MqtpehNE7p2GzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYkB9duq5pDtPO4RsFZZDYsmTb0Ep_7YYh0Ux19UTaCrfrJyxF_EVEe761t8UR3GQEmgKEwrDGHjTaFvU_HBJwIBg-FgES100D4P7bGqdOxzEnactl8gzfN5LIZ7oB6NKwDNUOxUsOprfz4RPahVwW3g6ABog79j-cXVqPwtcfTlYJxwXCAQGpGa3PpqhHVGb3Ts7zvQ16BL7drW-LK8j96RVRryfIMgtm5cNKNiQIaabpVujPzUcyMq7UhN36fHQerOrRyxMyBdRkclg43db3rD0oiAiY4p0Nn2meVkd7rGGLk-Av8tnk41HZnMPX7fplLeF4Sxzi48_hbypKpneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pkr5F1Pg6qSqy08Jaj1edICbDTnZbF80saqd-CmG052WkK852jYEaVh1ILFtexrPoFh7C99kWqFECVohAmK7SSMnrTBa6W-iwv0j1Yi01F0xL0aABwSg7iXFmyEpVD5T6VKuuxqmU4BjmNnfBU0vNQXuZr7T_2A6DdsNcRJOe5efEhuGt3os3gNn3Tr9JUphJ9VtUxAkK3ZmZtqR1IPy4PjlOsfgWcjZJyHajuek68f7P3m7vY6NRESZYVaWMLXfg1wcRjc8WsInCdoK9fqJxtC2fhlM5pdHgDjHUMqWnAtw9ffQzOTj3ftChn4hYX_Ruu1CPpeNy1mkGmtsjmwf2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOCJSdwBWTX3C3nCSxgyoXS94gYiRtz39SIRHAx663lKEGyIv6UPL2GR0I6UJiG8P_lGhOzhi5ffeptBxobfjx0RLr0ExRB6os4rFhMQtjH_Ndld3x7kdLIhUdxwRSxXcJjeyl0uxqOwf1c93ms97Y9tbI-Df0wpDcVH0rTEtH4_9D0DbABLT6NgXzXZePGirsSirBGSZhqGLMkanKTW87NNBaUOVhrV3RdaZUtbrRSVPjWDTFBy9vxY4uBL13snT92q0fEhMvtnkNvXXKg32CWcRgACfwN4ICwNrzccWB1sb4XWrATVeBM8Lll0zHlqaq4NyKEfGU6TjioNQZF_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5rLlVxVTj-vU6qVI0Yh_4nr3gG1EjEole1JMqK_506wPzYbYAKOekPcbF5ynk0W51jFq7Xm3X7MBP0cOroC6gCMyDvDhgiPB4Z7sG8j7IyT-lczoS8aSV8C0eUmZO0TwUM1m3kXGNSfIm0dElK6hx2NneMWiDG2LWBnq7hZJxHdT6pf41whwxa1R6rGqGSmd4-1qXZP8DTn5oxwUNEqOMV4YN4zJyCUsb-9kWEZ5es8rKjvIzJXNce7PyaPhUB1lavlJvDmnAtgf9_H6z4jiT3CpamRL7fRcWCGauaF5vuWWmLlFzmWl0fkzUR9vYAGzOtYbVgxTFQmRzR6aT9tJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRK_LcIaKMmHNr-z0au0XtyJvHPRVa8bL6VHQfLGyK-odAk1YY4-5w_-W4gBp0Fm5o5wSdVOMTm8iyahFKHNwg3Q_Nor6P__kAiVIG6YOOYyCm1SAzSHhRg3e-Lq3L-vll0cZzWiV0HgnV-f-QuP2cEgI8Lu_d2d9ycpAKcBAGAM8NzAVMvM5_Ugsne-ItiTMiJQkZqRdI6Qc9L5U-T5V7uRLHhUtr1naxIHylBbgOMv6YGAmFi0EKc7ptnEuCe4p7s_9APiKlZBv_ES-zhGMo6Ahw2z-eoFd0xkJXsD7Tp2NknrRKE3vCPtYW8poKG__N5jSSgCvrXcZnVLZq5hPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=llpE_LaxApUhqeK3T37fD7Z9t0WaHyzWgHYVSJD5oK-tgqpKnClNZuvGqZMS-Vd5WR4QqE8jXfUnPdWXYQE-fsrJRj3YpV7Ij_UwqFO6FjZ1w1Psv-eDzAjspACHDz7Pr7wyXLw_cUVdA6WPT-dgEhNbFMWwjdD1GVki3C5SPrh-Muh46FIakJE20RyMIVxT0-1enIZnTrLMzGedbCz4T5dTXa4hwZUxGj18guD6jZATJ15dC0pEo28pED-26WxdKS4CKVq566i74MRgnG0k-aT4Hb_HHjJrbQxy2YgD0_v7JUvwTs8kFzcbmHM7gxZEaUoUVTau5GsZSZsCjbor5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=llpE_LaxApUhqeK3T37fD7Z9t0WaHyzWgHYVSJD5oK-tgqpKnClNZuvGqZMS-Vd5WR4QqE8jXfUnPdWXYQE-fsrJRj3YpV7Ij_UwqFO6FjZ1w1Psv-eDzAjspACHDz7Pr7wyXLw_cUVdA6WPT-dgEhNbFMWwjdD1GVki3C5SPrh-Muh46FIakJE20RyMIVxT0-1enIZnTrLMzGedbCz4T5dTXa4hwZUxGj18guD6jZATJ15dC0pEo28pED-26WxdKS4CKVq566i74MRgnG0k-aT4Hb_HHjJrbQxy2YgD0_v7JUvwTs8kFzcbmHM7gxZEaUoUVTau5GsZSZsCjbor5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_tIAfxF3-34Rb1HgEudZIBHtDY9MCl5gVugnITS6gM5VqZ2f_hO70K89Ceg9iDGzXpuY458PBEGDiyp5F91kJaCxciNHzdioKAFtyvvO5sUGPqZUIAdLxAbPdZf4oqclvFFrxF7h_1vKYJGqm-vKJrTn-RIIWZwc8zotKT3Kl5K_3MSt5j0e3agbn2neDO26KskjJYEcex9KilcivDZUOaO7SCB7YhPX-jPDR62u6l2zfeca-Eo09xWGO9C804azYZB6GsvVCBhfRY7BnfxfB2TGNLEb7aD-NyKd5ukL2lQdAOR_25B8wY27Y9hYE8z64Uzk07a7rU66vZRcwPwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGhwedq_SN8Ni6r_UyMm6ZDEqzGJUge4Q_xRqPSYYzWOpIQKPOusUgY68VFr0PB9ZJ5NQ52gUwenecYdEQNRG4jOrs4q1V5r0VsETRFoEWgYYh8MkU1IJdnUYuezBF_wQpVGKeOlxuAlvbIffsgCnUpENCCDhNPahUgKTl1RKM75uuc_x7dBjzFx0yBvGSrMl4ZZU_IqEvhZlVeOnnrvSNtKm8-3LgckyGqNvZFOMqMKyswQRdpedN1dHk7vruR3aN8x9PjRDiR4dujYWFXadBVp2GO9YXMt6bYcMHFLNEL1H8HybVJfAD2-1JIluCvvnsl6miOV6te6TsYK3p-yLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=EcmfflmAsRgslHV2d17TAIhDwYRn6Aexs56NfvRVH7p8-8BMKCgTYjFGV0vV8tlvNzoZM_KNuk5M-Mx9R-uzNLbdTnDUyiR5IlF-jQUA7aV4xr6cOL0ZydUamG7VFeish9eoudbXMUqxXTPPSL4K8VjoxTsevYOBCAHjrH8ieLo1IUujNjXL7U-m0las-Tp6u2mee9VELfsnD7rTPDdRfnHChfYcF7dRJoYRzE0bBtnE-yHsMKjC2PRNuXKlNTIgku-_PKn-wCiuO14HZatM7ZNOMyBsbBZguTs1wKC4_NjGkWP3NOc7SoxT-wK4z1NfF0TYl-PwddCKDewFrWAk_i56MGnCmOK27Dex4420DmxsadIZorh0mG3kn0jDWR9FXWluKKsD3dP5DTPPU_ygr3SC5Z_Tn3fLsYetRBRJQ2VksZZyD6aAe3D15ElCk_2nGP5O_8fmQ2Tl0Fo-oMYKt1kA3PibB67eaVxDBY_3DxirqJwSJ8yqEWBonOAv7WnYviRMeUuchcztc33Noz2i4Q4KB8G799JpHwv66Crcgk-1TvTluOV0LuMk-tvGlR2waofa9phBI_synU5bpblvy0SsSyRElGz8qIcfLd5IpEiNr83ivKAAAUPk7ScrjXbWvK5jzN56_ADNGBASZTODIh_chet8Fus231jL-43JOR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=EcmfflmAsRgslHV2d17TAIhDwYRn6Aexs56NfvRVH7p8-8BMKCgTYjFGV0vV8tlvNzoZM_KNuk5M-Mx9R-uzNLbdTnDUyiR5IlF-jQUA7aV4xr6cOL0ZydUamG7VFeish9eoudbXMUqxXTPPSL4K8VjoxTsevYOBCAHjrH8ieLo1IUujNjXL7U-m0las-Tp6u2mee9VELfsnD7rTPDdRfnHChfYcF7dRJoYRzE0bBtnE-yHsMKjC2PRNuXKlNTIgku-_PKn-wCiuO14HZatM7ZNOMyBsbBZguTs1wKC4_NjGkWP3NOc7SoxT-wK4z1NfF0TYl-PwddCKDewFrWAk_i56MGnCmOK27Dex4420DmxsadIZorh0mG3kn0jDWR9FXWluKKsD3dP5DTPPU_ygr3SC5Z_Tn3fLsYetRBRJQ2VksZZyD6aAe3D15ElCk_2nGP5O_8fmQ2Tl0Fo-oMYKt1kA3PibB67eaVxDBY_3DxirqJwSJ8yqEWBonOAv7WnYviRMeUuchcztc33Noz2i4Q4KB8G799JpHwv66Crcgk-1TvTluOV0LuMk-tvGlR2waofa9phBI_synU5bpblvy0SsSyRElGz8qIcfLd5IpEiNr83ivKAAAUPk7ScrjXbWvK5jzN56_ADNGBASZTODIh_chet8Fus231jL-43JOR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
