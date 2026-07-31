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
<img src="https://cdn4.telesco.pe/file/pTnNNOoQhFAKJ-svZzj24VhS1yuHiUw0oZOZilKHSnJbdtdclPKIn_vnSoUjtCdzlTWUc_iVnQsFUY9e9geBRiUQM8cfXKJBFpgTu7TVQxzpGBPTyvllJgp4ACw35-t0-UIHAop_FyzwURNLVst76ki4oJ_aauZK6pnU3kTHqkEGuH6KWbTpycDesf7gi26hLSLxlpyRaV9c8aB5JiMM_A0rWwhrx10NoYg05FBv7iwItQwXhoCNgOmHCWEC2x15qX-NeLjvSSmaKBxrS9UU71fpzb_6qKmTvKoNE89pdfXDymB4UIEixgaJw1tJIorgiej84MMQOvs_lpHO4X1rYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 06:17:17</div>
<hr>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcDy5iNvQehdNbDoLsI0brLi0u-AtVLDyYypgGW52M2uEkVkoZi8otfB8qxEE9Tn13IOOCm1Y9_TZ8LV9qT_drizBVziD_21OkyVPGiLZg-4I0cQ4KVhUIJg39UzhIn3Mr0_n3n46De3GCGetSdFPqS1KyUDeo17sAIKsgP18CTVqzmA-eTyyxuaJO9YoZI--Q5JazAkwk76jlDQ-HAYLmMgG2zECYS_3Bw6QBV39rQa9O7LtEOqq6KsDtBaTyecuuf-GnWnYi3-QCfeajPlTjnYZect7epGZ78kKQQwphLTX1Y6g1J7xYobbcElHoXh7kGSHOdeIY7AM9trztwJiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgyfBDuDCJAt0JNr3swz4HIiKL9HrZbuqCUgpWgoWH-EZ48shYa12Y9jdCvxYiiUNFYEdJyEo7wU00C_BFnb_CTyVpzrMF5rOaoq9kfY20upu4yrh3hB5FuUoO5req5uCes4pUb52gmb0Fy7wTOXqJ3zoNQli2K0qbjfW0UG-maUyxTkGqrZoG-0yyCxvc7BaTOLtGogCdjOavj9BXcFLXh7XHPNWWIadDPMDLkUiV1vEWOIIbA-gd7WI75ohIeh1Pk1T33bNTZMkSWE1h7eaOVXSgYf4bfPEE0IOn0k3beN_HQF1mbN29UXT4qshW1DSNBZOglA8ZOoGk8W2oZOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUv5anB2qfc-brRh1IVJenxVNXBR0sZCsS_HQO5fDdRmfS3qbRGp8xsjEf9Uje5nBbcXkC-QdgDT5oHzh94KGeFdXLTJhJUO7yOT48zlcgCBEJdFxKmbzPLPMT4f91Se-3Pxl4zLbStIjl3sROPy4gDLxY2Ji1oTx81YlzciaS6Kjm1B_sqLI_bHtYm-5M6GVKX-iAjZD8qsuPR05UFej5AAOGArjArlLCmiIMfcGvInvBRZmcUYzDNd98S7O2yy20QFX9oTOhwtBJcmJsNQHa4rBEB8PMp4Z5J_LZxafM2YCH8__zbDb_rWZTuZhYe6o0Bok-mCja1U9qPhTmi8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcZi7B3J4v_54mMLaMeLbmyvCkRt4gactRhXoIeiHZ-AsCFJntWeBWWD1teE-raiff6dcsGETLsCRrIJiuJHzZex102YF0xsErP7Z9AoGBxeX3d892LEiEAAPHH3fpnF6ftl4I57kpboD-Nc__bQBfFKYQ_XiXuhEBJjoZMeYHsLXpD0c3QY5GoE5zJlm5fP-FHcR_xZky1Nqen4CRU6CmucOc-YqyeeZhaDdHMDOxGJ29W0RE_tp8SQW0F5eNwSzYxVKKT2yCWcNnXVkCxe4ZhTuajsrltArbYh-HSEBLH6uNdX97-xuyFvm1BW-iBDJNuLrltHtwoE_JQpUxwjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kLDnXTdnKzrOP2Gxhn3cY7M107EJVHFbudaC8F_pjzUBQZREp0x9rTnsgL5e3GBgb_WmOiVZk0P7H9lb8RUsm_0fQ6U3mPHYUR3ztviuH6F6ejybc4afMIVvIZHiHgtMNM24ol8Ezs-LpxcM7_HtroQuqc_YGkmy7DBBU02e_5dA1ghTBiwJW_jxxpApBepEmBf3Xf91c5mGmod6EAhySZMSNKbeKgjGZSEZwvEF1zQWYdo-qMJysxPqcrIGH1noUpeLkq71Dd1ZxM2_yv25de1yMWD4jIrulJ6y3AzrTfEnaVpvtsju7NvJjIC-NDdCn9W1xFD6YnZOO0VvNijoGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxEYXbLmT-840tmLI-gRd4saqmjdbp_xZXNsaTXEI4Kx2Jye35BB1qGPWeopoeGZySSAIg9jQLnJT8TOL3pKkMyQa6cH3y3uJeaeHLak_hM_uCzO1B9EnUxmnJrBeANzIwYUuQvs1AZKI-TyWtmHXM0iiCOHsYE3MSxkQVH6fLkN6Rz08TFuznN2yTd3cXPxVygS2mKlBYeCAbJG8t5_FxXFQRF2FElNdPnwTI7Tl1eq0IVsM6utytlnC6L0FZW-KmdzbQPsInGdxVpa7iz7O9vQey4ZdX6fk8mPx1VHUjJmYnBejtM3bEjk54WnY6-OP1R-bz8QtGYMUdY9USfXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6SXtA1i0dIGZMezCkDFH1gdJNXN9ZVHA2J4WPqexap7cFsuYqx2GbCqeFG4KQXuXUBxTFriCMUHGFTg6dh8QmW8PsGzF1KjbZATlbhVEUdDwgSwyrYhb9lPTw4OQ_cpBrPqhoZxrucQxUQm6VC9MGY7PTFPODptwpVHShO3ipXKj1Ay4DT6ZvZpoCHTzV4311cTRWTmdfEHwTTEbTG0lZfFi2EvoXEQRkI9QdqfmDl2j842aD9dBPBG75WtGv48NDarv3Yoi6My-E1u4KaEoiIm3y_5Z_LTiQLWY8yiq_71oC0YayqBERUPAHQ_B4lihIreAhz9ENfBd7H-Fn-RJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJJs6krrG0xT0AiNbV_M3750mhzwFRuzMWllhyrXJ9FyWQD2uHHFRbEKSNuIHPbo2aAFIVHOTkjrcjgQHUQRvMC9AZpPCpcRUUP8mE_5H0tMKxVEGVhfXJtRVoNdUA0NmiQbXK-tzTFlfozsKVw-5JcD1m4eCUHhCbP4-HTu2IP0X3mWAXppt33lr48xtlIV7KoGWw2KItSWUaplYA1oeJjr9mWg2VypDZ7oqjsvvHRfXgd_NHXxCFz5OIEACRUL_hUVVZ_z-BN3NVc7XN9OD5VF4Qj9ThdImP3SbEAgjgWhD_QGVNyRA5PD6n0sWNs3z39AonivZw3cDQbYOX0dQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=pRCfj7EBctJcUBQZGy2VbhatfIDDzphX3oLJlb3rxUDUOitnRrcPoVBv1JwzfA8LTzd2BH3GBj3Wsz_c9G7CgR_RGuBKM50N3pmLuD7Y3AUPKMLJidvfQknaAOjGm0oxkYhLcgvxb49YdTtLs8u1bA3u6dO3ahVhoLc2HxKaxGvqSyKvDjof8JwfMbvFFV2qNZsQJiUxDAEkhhPMDhuRi4tp1x-Au3q_ieFazXZMwzg4t6MfC0qq_fKhhK5kP8Q1iTajL6W_1m5R1gbTDWPP_4XVqjEfD2juikzloCvVazD2c6e9710EMQXxKixc34667m6tc0T1O2aMWCl_E-XOzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=pRCfj7EBctJcUBQZGy2VbhatfIDDzphX3oLJlb3rxUDUOitnRrcPoVBv1JwzfA8LTzd2BH3GBj3Wsz_c9G7CgR_RGuBKM50N3pmLuD7Y3AUPKMLJidvfQknaAOjGm0oxkYhLcgvxb49YdTtLs8u1bA3u6dO3ahVhoLc2HxKaxGvqSyKvDjof8JwfMbvFFV2qNZsQJiUxDAEkhhPMDhuRi4tp1x-Au3q_ieFazXZMwzg4t6MfC0qq_fKhhK5kP8Q1iTajL6W_1m5R1gbTDWPP_4XVqjEfD2juikzloCvVazD2c6e9710EMQXxKixc34667m6tc0T1O2aMWCl_E-XOzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=egWwjRJWQkgl3EhJQAB7AbvQlJDT3qlVlIlA6HCBZXcfpcDvC8CeK8TyTTZaM2iJs6bir7YgM3pGoOZVcta_SZ0BoYFvJ95s9YbF-G9xBRdhJyXjVlmNExCWwdWt6IlYW_xkP9H7EnX7mxLWl9mz-wRZL7d4c4ZV1X8Zrg1jVHlq_QB-UqvazBfJHk3ab49LhVenx4Jr46UUMqKhisv9QXs6otedgE4zqfx05MQ9fAroY40JVpi77RFnNBHBrKjwJRcs28S32mBJmWbssHO3YpaglHEU7fSw2w99rxCgP8hZczndw8zVRDPlOnjghQQm9f2bhTyemyBQ12r3cvzPkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=egWwjRJWQkgl3EhJQAB7AbvQlJDT3qlVlIlA6HCBZXcfpcDvC8CeK8TyTTZaM2iJs6bir7YgM3pGoOZVcta_SZ0BoYFvJ95s9YbF-G9xBRdhJyXjVlmNExCWwdWt6IlYW_xkP9H7EnX7mxLWl9mz-wRZL7d4c4ZV1X8Zrg1jVHlq_QB-UqvazBfJHk3ab49LhVenx4Jr46UUMqKhisv9QXs6otedgE4zqfx05MQ9fAroY40JVpi77RFnNBHBrKjwJRcs28S32mBJmWbssHO3YpaglHEU7fSw2w99rxCgP8hZczndw8zVRDPlOnjghQQm9f2bhTyemyBQ12r3cvzPkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=MWS4RJh2z767i5nROF-oJ0JiRfOa9gSykpIT0D-wTdSwAwmBMQe3m3okwcnEUsJgVfsOIA6Zw19Nnox3x7_IFyXhp5pQxD--hnfJOfbi_u5-qdsP1d4mvUs4cAm9qVG5Of4uZkraFvFg0v_BZoKA4VOTHavCepckhehwrBzlAdzZwRexCeX44DaIZ3Rt0Ozlz0I7fS9bUdAskgw8N9LR5FCHKlB2k-pvuSxu6mfv5gbwmelAQKS6PcqR-H_urvWCdiGPhZ0Z6UdOfbruVIRHEFUKL--i66Ws2_a92sRgXeyi0PPvqr0L0yTRLE2y9yF1zBWbf-ts_RF2LphmscltL2GS6tJFYLFGkClffLRXK9niCctBWrcvquQB3i0r7oUjtDLwSq6bsXf9_tVdj013LQkm1Ac0vLYwAO3-Qs2FvbKk4hWUtF28-Gczwd20FUFKbxgrfqSAG1OCOIQq-IbhBJyuzhO08hVZx8xKuIGbx-0I6pfGpGOTeLmY42M1CWliOuI4sQQmhQCrlIVqUgXNIqTCctNQH9T_qQZu46iICtIyw91MDuUsNiCt_v9h21CniGqJZJ9k-6Supi7UqGqJa-0BRuxIlWlPTXU8uqxxyawgOSNB_FdsDqBepGA6kEtDYC2d8Jq7Iw2V6CU78nC4AvSDPRvdBbWxrM03a_nasbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=MWS4RJh2z767i5nROF-oJ0JiRfOa9gSykpIT0D-wTdSwAwmBMQe3m3okwcnEUsJgVfsOIA6Zw19Nnox3x7_IFyXhp5pQxD--hnfJOfbi_u5-qdsP1d4mvUs4cAm9qVG5Of4uZkraFvFg0v_BZoKA4VOTHavCepckhehwrBzlAdzZwRexCeX44DaIZ3Rt0Ozlz0I7fS9bUdAskgw8N9LR5FCHKlB2k-pvuSxu6mfv5gbwmelAQKS6PcqR-H_urvWCdiGPhZ0Z6UdOfbruVIRHEFUKL--i66Ws2_a92sRgXeyi0PPvqr0L0yTRLE2y9yF1zBWbf-ts_RF2LphmscltL2GS6tJFYLFGkClffLRXK9niCctBWrcvquQB3i0r7oUjtDLwSq6bsXf9_tVdj013LQkm1Ac0vLYwAO3-Qs2FvbKk4hWUtF28-Gczwd20FUFKbxgrfqSAG1OCOIQq-IbhBJyuzhO08hVZx8xKuIGbx-0I6pfGpGOTeLmY42M1CWliOuI4sQQmhQCrlIVqUgXNIqTCctNQH9T_qQZu46iICtIyw91MDuUsNiCt_v9h21CniGqJZJ9k-6Supi7UqGqJa-0BRuxIlWlPTXU8uqxxyawgOSNB_FdsDqBepGA6kEtDYC2d8Jq7Iw2V6CU78nC4AvSDPRvdBbWxrM03a_nasbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgI9f9eVrZsFLRWx0Hlen2a5ggZ_qgBfPCZvki6PBBVpFV57knNQteqTIOF93E1MHLFwVHf1s7LNRSA3l0bodhSbL38yNeZ71se5X29ULspInMQHGQHUrZyk9E79T5jff6sxgDzESvarOvL6qPo4Il_6sKNVpYp7YXwrSWyJnITuc3EhCCgYpPYMzaFl7EyzhXXe5Tpoz_cpzmqSiQjnjUHEShglZEaiVfet9UCRw052M2mqbjGDurtXg1fucHlo5efKAhbUbKrjudhFJ8K9DDg07EEZRaqioZC8IBIz9OOkDVlxCfNTChFm0dB3JTrret1T0lAf4iyZf5OH275p4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=kF1JnnFMpysO55If-X1KTSkmyz2Y9dtkpQp3_GRA5ZlcPz_kFhyeThA_XwR_UXWSYMMMQOn024dfCMPsIj5pHnLl3Atq7uA8apePb3JQDs3O9vnErtjNgwsn0fvDepnQqOjbvVCoDLZ5590yeh_mwWnZ4B436E5167VV41kipxY556J6Gm9V5nHqhQsOXCI1ri4RbPwdmk9egMXiC6RwgMMVWODvlZVEwWZQMoxAk5QHRtQqlYAUKk0XfwHSGrALLnwV_RRK_YSUXzolYmtTIgSchcF-z5hKZbDywi39aOl7o_Hj4IeLnFzA1nO-laHjNg7LT11sreMEMtbBIK1tPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=kF1JnnFMpysO55If-X1KTSkmyz2Y9dtkpQp3_GRA5ZlcPz_kFhyeThA_XwR_UXWSYMMMQOn024dfCMPsIj5pHnLl3Atq7uA8apePb3JQDs3O9vnErtjNgwsn0fvDepnQqOjbvVCoDLZ5590yeh_mwWnZ4B436E5167VV41kipxY556J6Gm9V5nHqhQsOXCI1ri4RbPwdmk9egMXiC6RwgMMVWODvlZVEwWZQMoxAk5QHRtQqlYAUKk0XfwHSGrALLnwV_RRK_YSUXzolYmtTIgSchcF-z5hKZbDywi39aOl7o_Hj4IeLnFzA1nO-laHjNg7LT11sreMEMtbBIK1tPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8YJoHGoHmO8Mt_zwhESkZMM8AfWMejTnPedllQCJblNtblB1kxm1oEUbIuyNvHpVT6RoyP0pES2sYbkK6F5QzmYnybmxc2Hrp51RLa1-r7kczPO0ru1wJLlGl2YyIQ86L0Sr39xDUPUnHHKFWzhIHtrXTa6Y_gYqtSM_Dmb1OxV8N_E2UV4KfJ08UgN_PXIZLWw-THiAEIRJneTdzpPHe_-FQe4Yk63U07C9J9ljD0fJ_sqa9ulXyhONeL_dT_f6NmTKAhx9kBJniXiO_kGpdSpM050C9qLZmB5-PsnYh9YO_oP4a2KN7Cu8v4-SR1KTuzVr6NCgKcAyPdXzLn01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBdi8osGTLN4ZL6glx78lhkDdjx5sgNHGpbZeInObRuxrWUOeWNqICLZWMdRrQmZK50n2yxax2pTtwS8qtXh6vlB5RsaMj6ipDYWK8817NaE4HpLno2OCZIU9ldMx03frVxdRsHPbSfc_i9orCEgIkHNqe_8igEjzp3aE7oi6owUZ_-qVIwrUsKF8WiOzWfnCmSu8uUXXB5B0ukVT8TmXUbmqIwsGV86yqzzd_NNJ_SFx02ThRdQ0gu1W9f0MncbSX0p94v0fNX-MHrjkKalvUSoWTDr3YriZWLYi8PFMlSFX7Mzy6xsSiUZxt1ZL03ZxST4MBuyYSdlKJhPHysPbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fS0O60o2_x9bkuWpIMHBbwh0Im7gWRex_yprZzkhXNYpT4O_4RYnIYSFTMho3OmSW3EUhmoUuf5XJg0Df7dXxN_nbnACRCY6aIRzBvwXVLlAufT24pWsHjdiDCYNE6d6DpboUJaP_zRwMRBbQJ3dfK6U1nXxpgkR1wLCef1ZdvhUgdSxZvb55dnBm-ACrrXNnsKz2Hdan7FFsHN6QOT3KUd3QFKJf_3Mwa3OcK9u1GL1LG7_w5JSkKyVMm2_eX2K2LYOTVzvyuhguT5IVofQTxzowEOejSpbxVOOwN0YogX3bIzMeb_uVjlKDqLN9Euktb7VQh9VHdi6dfiNI2rnhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3YBss0o-yyGbrX2Z16b5tyAn92TlC8Bx6M8kkTI4l5sDhXG3diJx6ocTkIg6L7o2LWj2VHFscUOBn-9waIY_Iuh9UJDi8qs_KpFvnvAm-R2nx3TNZj96xA8RY8hCynOhxm61YSY8eKTBISVElJpy35HVM7Ok-iY0X0u1e7F6z72RPEstPNwd1LMmLAHt3e8FvWqFKEl6U99GfSWi8n6brKQbXcU4Oqq1mOa3mJYvrBanfx0wLnmtVYOoc8gkys889FpMVDTEf-M0nU_9OiZmGOAl0dGOw1Aa_SUn3835cnCLtuwCrEb7I9kcV76WfsWvEDiYApZ7QX6lo0HX_DHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXaQv46xPRAlFNBkmomGv92jFleNLRNZoZmcl3_lz3qBOowYrgqNh_DLBAN9y74BSvxRXzxpaLI6Uy6igEGZmr71SrO7h7m_Xo_KGm9EatJXYz4BGt_-JZ7Tg7hIPhOeab1OokNz_3XGEvJphrRSkuYjxh6zerp-Opa-kp0mJqhEjir1Wg60l4oLRCAk6LfZ2t6M8PlZmS-lHOz_bo7ITAFlmp5j89rAuXOmxmV5lhECH8ZLcuIuO6dmeKraMF9w9QiVqFxOBaJbefge80t5nmEaNTDqYc18JyPLmxAsBj8hqk9UR3jfMdyaUBdpmQIxz2-0qXyM3ezCmlQvUjZMhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPbZLhD8mYWxJ9ffEdy2Iyr7aK5MkslIx2F7svzo39HbFt_tbbfGjsKMZvhPxN2FftAr-77lzGZ2C08U9HlKaUUxxecGxFuEStUFuzi6NZ4staN62-qK50skofF3EeClo1dtCKPJpxDejnPegedk8MK0C3LwxsAAuFKgEo-0KkmpflPBsYPg0vMZDr-KbztNpnHW6f6loFXWIpDsAH2GVFVZp79R6umJYAZXWwUJdDj2OMT7i-tHkqdYNIC9fsXuEGqRNi3p7WfjiYBBxCIqOlydfHTBzFfA0OcfKBMJ8h_KEhUng85SttJ4uc_TSvQNURzHzfkKq63H4NL1GglcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkypV4tPy9sFS3UmtQ-nqX6C-zGogyJGIPu-ajbZmgkhLLFBgeVfFw9QGCfCybLgQgi9dYDoYr1A-6lNa59WsyoVHCmeaNReiPtAHP14SrwNLA-DxvB_VovFNRkXnBREz6XbOjgnAxX6G3qKa4gwOdZBTYY-y5MWF0quJBBh-aOxl8vZTGRyYCA-Rz-V_48kpJGitKzB6ZkLw7w3auJ5lZD9Wj271_ZwNJgasNATkPgYw93u3Vr2Koa8GkNnkj9ft7pdVMgO64YDHxtnMAYPXiGBwRJmzjuqtA5RAhI-S6j9-e5eanarjf8643iJ-RhTGYsbIAUHDT31UTOCBuzWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lD42s7k7J9iKdssuKEyorqNTuX2ycUPHS0QPt0UjbbSlb2PRMariqMj-2aiozJG0jKpi8HTZ7rx3qO7dJI8PJgrtPreX4ixoDz7YfRbIwBV8UDnVoBAx3zhiDcsM5EIBKb2nMxyL2cmSdnYnWgc0uwl24o6ofwdSJ0acdDHaDpcs9cQ6jbtbw6iXYU_9x_vnHx_HfzTPQ7UW_nQgMbBr0yQfyFu3Ikeq8SQ6sXUCBbsyHiKpy0E38phM79hhxzReLwQn-nR1nJuaxtp92J269W_j7MMRNiic89PNQQRNdpLl8ntAjk8KIGfyj4Mp_KCI-ZQJI9AWOZuTYx3anBKvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jXILBOGiYuI2O0jcbFX4T-Ar9Hy4DFpEnPRaJQE-ea3gv7vdlSlvjea9rF5JW3hLMlhOypYn0uyTgqDlm3TWlYlmQDwEUviFke04ISypOpWxEn5njhzOMKuYZGZXj9e9G5YQ-cG1uIDZWxjozb7kmD8p9cL38I663yB70BZpvBfQazagoXVg1NdMJapc2iMm-Z6bVIH1xn-QSE05FaM7zdFNTPWY_D2yg_RFMkZJ4zCwR5fiO_sXOsjLAttxb-crXdIzewQxlqj77shRd8Ttjzo_GR8kpyUOw3UFJUxKK_HzksiT1EeUyEkCHM7Attv51_wGTv1uRwNtEi3edjfTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ubfhAGEdR9C-kWxp2UIBIyz1REZAJH9co_VGrfypn_kACc8EI-dpTCEVnQEHPvQbG1Qgq_DR6T2ZYxzBTTm_nZjD6bjVUeej4nn6TLnemXne4Bc7GSX9IXZN-A60llqRuFSpZb7_fT04DxTf6RSRz2rb_YF3EpR7O4GRwtNb3i1XVGzRdHx2TSGc1bT_goZmoqyeGYfxsP2rVe060NbvzXDhwHZ3nXg0kP_5ndrxyr6n5jHENM_ki1a80-VOYYoXQhwz_zE4g6e4U5PMwmufXfYBiNkZBXzkhz-Rue2ipgK2tAerajWcw0egUv06TmXCiZFWRuKVs-fRPK0bNG6-Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snLMthFZvjaVD17hxMUv0v1Fbb6YmWW0TbpsPhgW-3iN2KlQkVYsmJDxWbfB3R2oRHYvoph_rH7pNnC997dLlJPLhPIvO2Bby6gKD1YoC0GYjCx2vHloIbElkzeZ8nXwXc58Vs6k469UcfD1c2JW71gJys2M-vPM1yWzEKrLdBCig2ivBp76orA3fxUYbRI5Zhs74P2HEJa-_dDsbZGsJce6mFRL39-h08Ko-la_6_Ey-w5KRxLBWudsEn9CgIYfLBRo6ELLabyBfDXZSePaTpm9tP4a7yEl6XfbXPvtD4cDJFJbQp1LcwxTA4hdjEqMLZFMhBUWmC70Xv2uG566dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ba4v8e9yC-N5n9XicmYI0JcEE8fwG1fZin69cuu9N4F7o66qdNxR5c0pSiPC1ekMIcqu6RRJysN1uqGS8bsAZw-J7Z50ijyql0EKCtyGFiQlCBeP38Ups6cC7D_oAUOBcBJ1ZcsYEK0ro9CbqBVCesj7CMyn8AjUycgzfZwrD3m1li5YILxiTd0quKZcPZvd6tJsD1gQjhC32NtpC1UcYKktNeh2-CBy-1Lr3_KAnaN9XPxJRBmFsG0urZpZbRQJvdEWV9RvU1Xw8tSOvIxJyahtb1tHt5ZZLATWx8qSMy-H96Ughf3R0SQRhSpy_GVH1ZS_KnS_xlwLjyXPurcGCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/opAFV77FmlNYEJY5CUanPwL2RsY8G10_LOngQEKlfZihhvrYeiAfJCcqJ_xrmXbf_ini2jLaN9PQ-mJGjygKwCNkdNY1A--7XJ_B6srDOgCH1uojXpPpcXvtVhV5Aw1CYopUmAHO8I5psVMifVmLKnZ_FMq0WOpuUUNS5KojWgZ5P2JNYB_wlu5iXMYiw5qXEoOrj64BvF1zkyK1G6F4ZDv2Y6fddZfWWeOO5i1dxVIgRn1H0-CJ3j6MI29OqlsHT-RuqVDbv-l3eWwhmx1dPRfa2e7FrR63TbQ49azLIQuo3oiqQF4hHzVjRymHraH9gWCMaWkhlZy7IyfBUMPcrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IF774QTiQ_SJKunhWJaBFBmcV5yfcyVssF3LyTCiLow7G7rHstso6Ho23-yd7MQ9iU-dKlGxoZZKVFFVRi-8FAdJpEG8e9dnPOg3vZrgzSpDnfuS5VNuBIEI0s49dUEGDBz8EkaPastLQH_E1sGvwJ0XnZ_UuEeDcE1bIJmPhX9_euRZF4RC47MroNZbfMTlNfrwM6FcskKJN_9A4eCqi0DY2gulpPyE4iyd9s1plS3nR3DHR8uLHuRrmdkhOutoN6-UrwFkTNoGu5Y2rH7N3tpNT9nl1TLoilr8-QkKaj-ngP7z0ugS46ds0K_PuNtSveEnBTo2cwMvL4umVpLLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCX3DfSeqd1KzuDxm2QM3djCX0bHzJU3PnXRKSw0xnrMfM0hfLBp7wg9M_75yEyXW-1jGbdPSONDJqEgEuZbIopMPcqMiE3LhBQHZKroBlcwDKqi5BB-QUggZBrhGgO20-yeAS7k4Vi_6NDoxxvYAFvEKwA9BLOB8ox9xpQmQS9zpfwCozKQeihTYEeXxlsQSkhrJ7jpSyXfDhmSbi37Rl9EDhKaX05-LqxVx5E1-JsCxPWKnRzKkgyTEZJdDI7S3qzffBF340mMA0GdC3lwS1iTzEu494Z43JdJwixAprdELcFWgL5TAHivu6gdZNrMwrb_mnPHV8hVuVWi4BM0qA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQnjGupoT6mAf0jCFgFjqvB8lU1qQcynLCU2VSYIcDErFIVam7e_zGxm2v_n-Uox-MwSA70ZK4dfSjczBwXPT9KVlr9gSDcEHUSdb_0Zc9dxtN9oDrYJca9GVAdexwD_cUXpjLsxpelfWuh8WbmZ-8Dh3NJd7GkAZLSeWoUzYq1ih2YngKvKqbRE5L5dYOgwrIo33Ku7fieuiQgy3KcDEoVB73NAa5tIwibp47j2eDJWImy12usi55X_BjJKBH2yAoYs6acbRMImAjIC--OrgwjBCD3AMNH3OkHZqNd1mU6AmXbw7F0Duv5PDxGtzKRMMWioBdMohLN6C3kUFdWWoA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=mhqrAfjEpmwZKQtNo7AGqiNjlFKBtVcX3mhCjfySxHm3pwIQUIPIEg5p0jZe3j3vYz04tFb7BdEZ8vXp1ON4KJcJf4jvQ_9BI9DilYYEnxsj64UmMROYo-zFNDlOQmIygePDKbWWZV5dD1UA7xa442JQKfBDG18N_9Wv5PiwEAy0vdbLRx-akBRdJ-bRLPKLSyh1BWTceYu9lK_EVGyiueJyIUgdwmFASau65P1Haxlw-QPoPqlvyjIMgv171Df8RmxZvlQ8AjBMIIlbFROWU0GhJt2eKooRZaPqJRaZnjhsvIZXgIOFfoIJBJQVNV1HVjEwGmBzcYkcozG-ks9JyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=mhqrAfjEpmwZKQtNo7AGqiNjlFKBtVcX3mhCjfySxHm3pwIQUIPIEg5p0jZe3j3vYz04tFb7BdEZ8vXp1ON4KJcJf4jvQ_9BI9DilYYEnxsj64UmMROYo-zFNDlOQmIygePDKbWWZV5dD1UA7xa442JQKfBDG18N_9Wv5PiwEAy0vdbLRx-akBRdJ-bRLPKLSyh1BWTceYu9lK_EVGyiueJyIUgdwmFASau65P1Haxlw-QPoPqlvyjIMgv171Df8RmxZvlQ8AjBMIIlbFROWU0GhJt2eKooRZaPqJRaZnjhsvIZXgIOFfoIJBJQVNV1HVjEwGmBzcYkcozG-ks9JyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYw0gQBnr_1B_74p4WKYwu4e0LuM_Sc2EfrdnE6Hk9PshVc2Pfs5l5asj5pmLO0z7bV3QMsBJN3OP1SI3RSF62dEz1aYhUCAXyxD6ACmu-xiRJRuA0QiDQFOwt3ud7beWdwIuZjmoe1mA-JrPKox3MwNeffpriscm8RkyethpHCeBZoOwWx020z1jAXRvv_LqEYhPquA7iPl25o2ryc26vj-hYv9YyVUZS76MVnqsBvU3YsLZ1F5i6pWVLQnRS-pfhVodYcVt6iYkOXTw-FkZkDwuLS6lP7RYEbQPevuVDB51LmelaUBWhCKhs2rrJwtV61PyVYwaWikh-bWkQPsoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqOjjzuaeXHEVcOgUFLzWfR9XxtGBq8fRyNXsq_ev2bpCUnsoCLJuR68eDjFP_H8Ved5D0Zdfy82BYRXhKA5G1-6hRjyHqSsHYNGCLxv-3BkoRwqLPE6m42ILovL9DkwpSDcFTCTcI7k_g3eSmIyPTwY-Fm3I4yLcKZwatStbYP67AAWMOEOH-As6Hcsvc9yRZTvIAQP8GnGT-2nypd8sg0OUVkDlIlheDBaW71mA0KrstLnmYS5w6YGMMaTrSPqJs-gQGaVBc1eQEDptSby3-WwTfq10BUlZlJiXtR9KeQTaMkM0j-ZrbHHvY7-qE4AfhnUn1XtxAa-09cYE0c2KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVwtSobavFo5jQjnbG7i3nkcu-zGbwK44crYbOOK4JWGD2RstsGaXn9M5VNYwjfa0gb-EHs0-tKNuyn5j9FFpB16J0WI5EMh3ffVi2X6lyucJLrAUndW9PAlUS11ti_0rVJldjgHv0xW1Ey4zn3KLGtx4KpJeEN_1UYIAYVLlcNiLvHQqsnGPRfVYKu9ulme5BJ7WxM0BUMx8bxx-j6oJOgBZGAZy_PNz1oD0w75ip0NliXlVCj2cVv7l02_4un_eQ-OeL3vpgUNf5-PcrxU1tk4XURaBj-ND-4290Ttk2Uy4g7YGffQKju-16dJD_LAewLVSRqAMIWbOzqV0BEAFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=U9Rir4wlj41Q4YDtT3KvlGfJtIS3WpwsJ6-B0tOVIB29NH73WTGLqL7WiNvegTnFpe6lfzlRdozuzqoxSkYlWbKG_o3EuS_qFCnU_ZkSYhUUcKmshRZ_srR_bfw0J-BPBtCXrQ4hbtxMQI-o1LUm6Y5LIAI5LGpQHrYQyMMbbQSQD1mpZFXRlpAc8nzoKZ1Px2A2z9dSolbiQ6rFUuuEzLnpHXPKFgi3taseaO2WC17igcVw22B5ZziskuoAK2cSauH4V-XZ5mDTxdp7EmC9Pnfk1If3MPS8xg_MxkCewifD3kXTLxhK9ayMRv3dD4yXcPmwdFRXdmLpemLWo-AozQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=U9Rir4wlj41Q4YDtT3KvlGfJtIS3WpwsJ6-B0tOVIB29NH73WTGLqL7WiNvegTnFpe6lfzlRdozuzqoxSkYlWbKG_o3EuS_qFCnU_ZkSYhUUcKmshRZ_srR_bfw0J-BPBtCXrQ4hbtxMQI-o1LUm6Y5LIAI5LGpQHrYQyMMbbQSQD1mpZFXRlpAc8nzoKZ1Px2A2z9dSolbiQ6rFUuuEzLnpHXPKFgi3taseaO2WC17igcVw22B5ZziskuoAK2cSauH4V-XZ5mDTxdp7EmC9Pnfk1If3MPS8xg_MxkCewifD3kXTLxhK9ayMRv3dD4yXcPmwdFRXdmLpemLWo-AozQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivON6c_a94o9DbE_J3kKnU6pIWPmMOxF7McJ2JQg7zNDIn4kAp6tCAhq9jyrRlvHy4ay-WoY-TVmNt-yYRfy4JRur_gGkOFomAu9iW5pieoFsu-Hq8PKRn_XjackOmPFrq-c-PJm6tS29JJf-ID9OK4LVkpHmCfzJI5lr0Szk3IlyOH-y2f7xW_VMiTt-bZ7bSTMniQJ-lS9TfthQok41I7Hk-qKbXKGiZ5zneyHclePBiZs5ILosQ17eh1A-qPimEQ0Kz13vz_t4PxOgUXbqHUdzyYXcgZiVzoeLcerMsID0ck_0PWHDNIX0nv_FDCyJyYv_ZVtrFlZM2Io0cTR_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=XAxMXaEO0Aw48ULszagEJrV4JGRd1u7sEsxi_xmw3c02PfLhtWg0h9ysWy0t6Ha96BTXDCVIStAAXU5v-VMIC_zkib-6xXl8AxPbAuA0N2GKNqmeGo2d0Qh-Vz3D3cWsYRjOXjheQcMvMI-X7AQ8tuiuY0JWzvtaU7WvHjqYUc0J3-Ovd-lgN914d64mlKZfTemCkLgi1Z96klvQgts618DMdT_6tRgCMeLBlWkCebb9yiUZasO2qSIoZwvNL58EPtEYouUabq5rLr6fT36HnOzxoJOJwQ57EUyhiSiGolmMDSs1NKBC3ueLfT06SN9tAkQ9_H51nfdl2kfBVL33_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=XAxMXaEO0Aw48ULszagEJrV4JGRd1u7sEsxi_xmw3c02PfLhtWg0h9ysWy0t6Ha96BTXDCVIStAAXU5v-VMIC_zkib-6xXl8AxPbAuA0N2GKNqmeGo2d0Qh-Vz3D3cWsYRjOXjheQcMvMI-X7AQ8tuiuY0JWzvtaU7WvHjqYUc0J3-Ovd-lgN914d64mlKZfTemCkLgi1Z96klvQgts618DMdT_6tRgCMeLBlWkCebb9yiUZasO2qSIoZwvNL58EPtEYouUabq5rLr6fT36HnOzxoJOJwQ57EUyhiSiGolmMDSs1NKBC3ueLfT06SN9tAkQ9_H51nfdl2kfBVL33_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYhcDkaUJTEnoWGzmOnncjbXBRKcPzQ4106bGazPZa-PFgAPPvypALrRoBbiCpDHps8o1SWVIMvtNaEMk8qcbTbGN0NtH2jalQnCyRlDg7SKSsYsba-QzFq0EE5wltH0z-ys-YShI-0wYR8cBhqsujKgcodrizsZflBIkVWMjwNqHzPKblfsG4WXYWXVMdHJkpMDvBLCn965LC7TqoOGVcsmBvnzgcD_VYB3xTja3sUYKG8igUHDMuAY5iHEiC61I6Q7Bs_S1xo0-FqWcW6KEGLyx6FjnjcfiYmm0cctDN7yw0tiyZu3AkieKGvGnpkuNi1n8SNU2jlAOtD6lUSXDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S68p-B1rVh1enxQ2oTMhzkWz7Qr9Zl8OiH2vtdM97kPScgnIBXsZZ_58uJx46onon0mDkcgD2jhp1U80nI4AWxJL0oYMQkmqQksviyLm_45G3vGRqh3_uXlQh7fiaCyVW5TaF0fTrUv_KyECDD567hO1d8G31LN5R_pLkjNL3g1iNP9gXE-UYFz1gFSZ6L4PlUnf3jJ18hffiGxJuKPEUmh2fEWGMAXHVEfAd3cnmoRjRXha4VQOHKkRxRVs-kRIAyI9joOnOZBU1Gaee_fw1yNvvdjFzORyUgxAmjMy0i4Gh7MS42HfeWQyK1yjTmpTuTd6r0_Tutq381ircyXCag.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=Ge_opkkn4bDI5FHULk8U4dqK3LInRpLk6vV_NPPPQlRP96usTi_RZeBS8fxtPltdf69sERqYwVDHGs0oGZoBdP8Ax2XvpsMIEPBZpeaUgfMe5nUh2LqXTGJXmsTREXtJxg0uIH9PSU13FkwxZ7Re2AlDptrYGuTkfVKrAVseh8909nJtHSJTX2HfpUHUEsFFRtRltAcMiQ4ubPdCQsITdsmCZWi9hPHeHQ2Nv5cKGwAuXBVRPYmKYSpwvSJHnSO3UjV96HU9E6hE2rRISO9ilVoJluqKlHG_wsvbEecpwzELocLP9HUZm1K-31U7P51qc2x5Pi65vlnspzE1TEwKK7CZev8q35VKx_Iu5uHTGAY_jIqOolMU80ZpUz49q5bEQnK6WtqnhZWyswwL2M0OYuPKKY63Yj2gzkXvuZ081eIom4v3sDE3dYUBnxQ5hA-nobUzLaVHODYko6pANYcF0YvRnOQJntpe_QPJ00pc73VPaBpXYtTxVXCxgr9_icfYL6pAdLbgmHuW78HZz22HyKOKuUbGa7BYqwtoqk9z-4aUZMLQ_4by6P93-1Lo__knttVJZy304s7ei1BZwZKO66uOLLRT6B4B8XgooOY7tYdC20x6KBSaY0u8Ll4u9scWvCkx5jtVNyuC2W29dfuHTSGmg0IZN-3nQOa-IXyM6ms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=Ge_opkkn4bDI5FHULk8U4dqK3LInRpLk6vV_NPPPQlRP96usTi_RZeBS8fxtPltdf69sERqYwVDHGs0oGZoBdP8Ax2XvpsMIEPBZpeaUgfMe5nUh2LqXTGJXmsTREXtJxg0uIH9PSU13FkwxZ7Re2AlDptrYGuTkfVKrAVseh8909nJtHSJTX2HfpUHUEsFFRtRltAcMiQ4ubPdCQsITdsmCZWi9hPHeHQ2Nv5cKGwAuXBVRPYmKYSpwvSJHnSO3UjV96HU9E6hE2rRISO9ilVoJluqKlHG_wsvbEecpwzELocLP9HUZm1K-31U7P51qc2x5Pi65vlnspzE1TEwKK7CZev8q35VKx_Iu5uHTGAY_jIqOolMU80ZpUz49q5bEQnK6WtqnhZWyswwL2M0OYuPKKY63Yj2gzkXvuZ081eIom4v3sDE3dYUBnxQ5hA-nobUzLaVHODYko6pANYcF0YvRnOQJntpe_QPJ00pc73VPaBpXYtTxVXCxgr9_icfYL6pAdLbgmHuW78HZz22HyKOKuUbGa7BYqwtoqk9z-4aUZMLQ_4by6P93-1Lo__knttVJZy304s7ei1BZwZKO66uOLLRT6B4B8XgooOY7tYdC20x6KBSaY0u8Ll4u9scWvCkx5jtVNyuC2W29dfuHTSGmg0IZN-3nQOa-IXyM6ms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ZJR0LF0phyzTR_di59NUMpKl56F6g41jV0AQTPJfdqgLJAbj_BcLNYV3cYsj1FS0AkGZyg0hPZzrnI73yFjgBjMnUxpeGVWuZVgNheyTYmZ7gHCg8Im2xa5ABGyaDqnIuAD7Ya8YfUmjz8dPG_4JuDKtzrWrnWNZ6LsULcKLQBTG4J1EP8ToO_JIirpVjqwrviHO-gyh3lirLI-71TjDW1zfHepUImaMtXA1UTeVrad9615Wj4IkUSyXJhdOkNNI_z57uUTElR97J2wvhRIWErHsymUA-ludMkiFt4IkTRQYuCLJmlrySCrurZE16nj80xy72SUeFemAi3zMPMPHQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ZJR0LF0phyzTR_di59NUMpKl56F6g41jV0AQTPJfdqgLJAbj_BcLNYV3cYsj1FS0AkGZyg0hPZzrnI73yFjgBjMnUxpeGVWuZVgNheyTYmZ7gHCg8Im2xa5ABGyaDqnIuAD7Ya8YfUmjz8dPG_4JuDKtzrWrnWNZ6LsULcKLQBTG4J1EP8ToO_JIirpVjqwrviHO-gyh3lirLI-71TjDW1zfHepUImaMtXA1UTeVrad9615Wj4IkUSyXJhdOkNNI_z57uUTElR97J2wvhRIWErHsymUA-ludMkiFt4IkTRQYuCLJmlrySCrurZE16nj80xy72SUeFemAi3zMPMPHQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXAO175cRLECJTEnBG7elNjkSSvdv0u0GZoN-occEvIkYfAhtD5JsDUvSK7vj5kquC5Va0O-9XB2ZPUHF0k6rk3NtLL0P_exK1Sif_2YLciPykIuRCjPCnQV--peJ0yvuymyGZanjACv-4K4yCqMgutGHN1TBpyG4Iw6oTS28KJxCY0syEFvXabp8aNm6UuDWxTwxUVSKRyfpx82C9Ergbn62HANlMWcTTCjDJ1AKqjZO2aFbTyoG0eJEMGcJcqeZ2bCMFWEeN-apaHcP1W9WbtEiWdujPAa3cwQ6Fcpj4xmHE8fW_OLXn1yMvG92Som1b6i191uZSs6sWFMpRI-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=WQVIOePMi6RQkwhChm2-MVMiqXeIjg_AW0vWz0L6Wn3ID5nYa1sBMKY_0ziZzqU5eBTV4hFV7L6J-kSbd8eUOcfEWfmJlPzn1BiwcyBlj7_08Q84FLk3iqmaBNS_YL9C7YWjhMclPR6lCFJy08WVKcH4eot-zdYv3SPkytQa6U6-Lkz1dwEx-JvnLKy3WfW0xl7O6GX5EFq3LMx0EDwqh1Gbe-ZVlXIjKJwrytUcXAckbX3pr-6xMy87JR7aHTdsZaa7dB6aYR6V_wez5jh0wtKZjkE4IndXYnZUqxmullDWBeL-O3yC0UtRG0jeweB3K9zOMPyjfb7Z06igYJFYyTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=WQVIOePMi6RQkwhChm2-MVMiqXeIjg_AW0vWz0L6Wn3ID5nYa1sBMKY_0ziZzqU5eBTV4hFV7L6J-kSbd8eUOcfEWfmJlPzn1BiwcyBlj7_08Q84FLk3iqmaBNS_YL9C7YWjhMclPR6lCFJy08WVKcH4eot-zdYv3SPkytQa6U6-Lkz1dwEx-JvnLKy3WfW0xl7O6GX5EFq3LMx0EDwqh1Gbe-ZVlXIjKJwrytUcXAckbX3pr-6xMy87JR7aHTdsZaa7dB6aYR6V_wez5jh0wtKZjkE4IndXYnZUqxmullDWBeL-O3yC0UtRG0jeweB3K9zOMPyjfb7Z06igYJFYyTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/najYhGWUzjsx7pkgE3aS1nu6U2ccOPXmnpUd-SqL0EcAtnMJgmPvHmctvRAi4IoQRMdMzFI0RfzLHJph8uy6pJQPpDpiz7UEWfiMI49CPP1vfoNHOlwwOkWHL6xm6WeT0FKU0zQGAVS79iKfWm_MEkF-6uKP4jueyt0FGLX_dCSCupnxEx5XVDb3F0uvmJUw8r7QtSjqJDl_gK8Q2NxbhPA2gOGc4A3h2W3sRHsab5R6v7EgbYco-y9zbC5NP4CQUp_EuNl8upE5JDGuVdFFi4LHzu2lSCOaxaeBdOoUKzTSpO9Z-zllM-Z7QjJi22kVCDpzxmU6AIZk2uUTqonScg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAy87uwiQ2cfeewqesDpID6RuBa0CV-zkm0deSoajzi1aHlHrvdlO544jHcBj4cn8fRPBBHWgn4XonmFnluRrkEsiRNjO9fgpKOLfpBE9owJzQ9riCoCG-1F2mTLG-msRq0Y6EKwnfEtkRmr_TWESwODhgGzZUPtFA1N-WGjOQG_R8iq0uKCtNxv4O4RgzvTlW3jo2S6PaTxrVUafgZlfeUR-dtJfGZDZvmMLfUMQL8PS_xZptUtFYLvkGu2w1gmFzvaDcmtytVSu412MCK1EMpWp4LxGxeCS1rKHpm__1xoMB9ftcb_l350VltxFHLz5onFMcHrt74xXJdUtrGRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBT-OYmTVxj_eRIBpQQ5kR_cfJG2dkQ_WCshjRGoUTyTInHbeuu7E3t5Ef-SIiWznTYVRTsYQ1QWF82hH-9ntLRfMqNZVX5MpSAa_r9qQ0yUVRn4YLImrPlUlJ2zQpwzHixk9kjQWOASs1dGv3kHJ3RX-Y6X5wdV2iA37vtiw__G4gInVTkEtRXOfmV2Xwv_8WB_wXDzMp7u0mYjNQDI5zz3c9XgCxMdZXCEUvCeef_yF-BDpihyqvFF7UKAR2TGj2IpYy2X0vVNTOh-CG4HjGrGi7A2HVlCAL-EwTfH9X6xCFKBIT95KnjCi_G4fsEu-SeeFHTlsRMjBpNGlKNp_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aukDeA6tb3PWp_V07F2oQByhfQhk00BR1yMUZwjdr4TeAFO14nvlSyqKVPhoPc8Qmm0wmBaPwTlebYRrN_ssyAX5Mg8lwFxrut2e--YsCftVOQ1NR13liGJvy2qLQyEXmUcnVlJaZTGff6WIgnUU3dQJ_VLidb4iIUKmMP86VKVMUOXHpGdM3njAEF4HkkfA_ahP7EsF74vVL-VUXlphbfXrn8ppQpz6RMX4M1I-EN9UuJSYkMihYCjJbJgKnMiUH7QVwwAI4tTr2bjgSHzU2Ft1dYkMDDcHdghV4NjQT9Ud6mZ72mzsI8caR62ZPlflQGBK05NdEDXUXlqkazx13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4MbaZW1BpARfnhWbFLNOWcWb_R8hosy2QvcY1NnhhdvTtyn00q0yRNhBJoRbRM7HvfqtGcEctUCMOi4nY5cRkIz4kZpBHfv26hh6QJ2rpLHDoc5BEEgF-Y67hhP2qyAVw914wkJz9FMOGRnU6QuFO7o3u68DppWtpQSoBwBzPaxYz25gEwlMvZ7oXSCNVkZLEQQoKC6VhJjYqTVNShxfK2hAmP2Kn0nzyXKmsfDehpYKfrMCZclsqOVoPG0qPQZcIz6c2mUYLN8dU4hsIYOyH0u--zDlkmmNwK3TBJIxO3NwnRQ00NUdX7-iruQbzv9_lGXuVehGPigvt4aVr7YEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=HNELoxEXCUyxkiqg1GRBsIcyi4Vttk0NwUd7qWZS3cUyoLjUPq1p48IDyYdC-fmJPUDmLxTrL6xaWYa0Iua2M3og_gjA3J7U6KK5J-QzRq0B_HIvP5BSOwV0DHb3soNu1A7Fa50HDmMcrdkXprjtAGejHDot4JG3tIdzefTDS14nhWyYk-ohWmwPtMGp-4Qsxv37s18EHCHSSNhBZXr4SzH-8HRnfObFY929zRjK_glaqL3yXT4YTNP2Xe8cuUnp0lERW8YncXF5rzX-NTdFRMLbofdJwjDI3wSxSrYDrhyXJhPqA5QryUXaXBrZdxoqfTkV3q_V4g8XzpXHMMYs6KZtZ_Xhb9IPV0YJX8aNeEI9yWrGHUIiMv5Xr0LU9AFdgdaiS94PDBWFLHVIqbfwjZCpV6cydsZIG76AMGGiJv8JIqieLxwoOGXg5M6VVgN2MmhtGXgEXc0YwoueWuPutveZzO7I-ZqlR-jrXJ02jLFeMYxcDdGSkTOvTU4nG4n9EHMm0IzpgNC1_0M7Kvjr9tpSEXDxPqhWOzQr_llcIEZu511zyFYMT13WEvHFUBK1_Uqyo6Wh8mh6gRmEYRaztCZOEndUokrEG_-EWSQgdT4YQMWT7lZg1VHr7yfMjgH4YIAAEnhaqYsBbXZ_Tl3n0Zg-527_MKS3NRrpw80TePQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=HNELoxEXCUyxkiqg1GRBsIcyi4Vttk0NwUd7qWZS3cUyoLjUPq1p48IDyYdC-fmJPUDmLxTrL6xaWYa0Iua2M3og_gjA3J7U6KK5J-QzRq0B_HIvP5BSOwV0DHb3soNu1A7Fa50HDmMcrdkXprjtAGejHDot4JG3tIdzefTDS14nhWyYk-ohWmwPtMGp-4Qsxv37s18EHCHSSNhBZXr4SzH-8HRnfObFY929zRjK_glaqL3yXT4YTNP2Xe8cuUnp0lERW8YncXF5rzX-NTdFRMLbofdJwjDI3wSxSrYDrhyXJhPqA5QryUXaXBrZdxoqfTkV3q_V4g8XzpXHMMYs6KZtZ_Xhb9IPV0YJX8aNeEI9yWrGHUIiMv5Xr0LU9AFdgdaiS94PDBWFLHVIqbfwjZCpV6cydsZIG76AMGGiJv8JIqieLxwoOGXg5M6VVgN2MmhtGXgEXc0YwoueWuPutveZzO7I-ZqlR-jrXJ02jLFeMYxcDdGSkTOvTU4nG4n9EHMm0IzpgNC1_0M7Kvjr9tpSEXDxPqhWOzQr_llcIEZu511zyFYMT13WEvHFUBK1_Uqyo6Wh8mh6gRmEYRaztCZOEndUokrEG_-EWSQgdT4YQMWT7lZg1VHr7yfMjgH4YIAAEnhaqYsBbXZ_Tl3n0Zg-527_MKS3NRrpw80TePQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
