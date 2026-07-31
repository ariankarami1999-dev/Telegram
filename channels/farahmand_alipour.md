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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 09:26:41</div>
<hr>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=rQ_CbPB74cL7H8L1N5Mq5EkNLG4qy9kZvscCqdY6NCOfmpLY-BGAjARXG21N_rvacjf4CMiRWf9S1KilDbnm51w6SY2ob9hP0HuG8uOe6r0b5fnNpeXZ-NazDKvq8JWhjK0GrWCICtcBO4gIPqI-pBFw_O2BiVjKn9fZIwL_nNKBRuiYbYRaCezvRWAMExD7OIKAqgVK0hO-7svOxyj6QJOKUndhTBsmmemGwNn8WPhbNULM6hdsgsqO48jUHMvf1GsWWFaipDjNeKzsG__IbC-HovC2hOPeG_WVw5v6I-IWrohuJcW7ArhjvloMIBTfKqaUkTZw2bwKtkDOTQ_eJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=rQ_CbPB74cL7H8L1N5Mq5EkNLG4qy9kZvscCqdY6NCOfmpLY-BGAjARXG21N_rvacjf4CMiRWf9S1KilDbnm51w6SY2ob9hP0HuG8uOe6r0b5fnNpeXZ-NazDKvq8JWhjK0GrWCICtcBO4gIPqI-pBFw_O2BiVjKn9fZIwL_nNKBRuiYbYRaCezvRWAMExD7OIKAqgVK0hO-7svOxyj6QJOKUndhTBsmmemGwNn8WPhbNULM6hdsgsqO48jUHMvf1GsWWFaipDjNeKzsG__IbC-HovC2hOPeG_WVw5v6I-IWrohuJcW7ArhjvloMIBTfKqaUkTZw2bwKtkDOTQ_eJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHFF007gnUwyiBjcWtsCKXIJxyU5wSHzhBChEB8DiVjIMu6_rTPYXcNPgpr8gN2no7oqo_Xg8YX_1RWRcJCjCG3QE2xJ8tFu1IirUjK8rddXca6lI4S1U8bU7u5IUcMfkqad5lp9AS6D3aQICVR4bb8vtl3oOmwqPlBaOL_zo1DCyWKE05wBMpQY4og0yACEJD4PBuPPn-ge7KxCmIbJHZuTGwqF1gxcV4kdXbaBTwjLHgOTpuF4bVNrabA7xwDlY4Ji29k2lqw7YPQegBWmTtx56PcWKPtpCGwExyoLwHZ7wwjvlbjmwZRSF7ybBSmvd6HkdnTZCvZTbwrQyHMZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcDy5iNvQehdNbDoLsI0brLi0u-AtVLDyYypgGW52M2uEkVkoZi8otfB8qxEE9Tn13IOOCm1Y9_TZ8LV9qT_drizBVziD_21OkyVPGiLZg-4I0cQ4KVhUIJg39UzhIn3Mr0_n3n46De3GCGetSdFPqS1KyUDeo17sAIKsgP18CTVqzmA-eTyyxuaJO9YoZI--Q5JazAkwk76jlDQ-HAYLmMgG2zECYS_3Bw6QBV39rQa9O7LtEOqq6KsDtBaTyecuuf-GnWnYi3-QCfeajPlTjnYZect7epGZ78kKQQwphLTX1Y6g1J7xYobbcElHoXh7kGSHOdeIY7AM9trztwJiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=bRN2eQ8oBFqwzGNyUlGPXvV_hzRjjGTyn5nXE6hyatfRGCjgXR1ojvWC703sFvY3pO3_3ELakv_WxoWSeyDCWItHsc9D2BmlV193pGOfXUkkyvNKBZlqyZ4EPRmCFE02ZE-QBP0S7hnCQhp6VrqknRI6Zn1_BG0gnb8dPE7pemL27a8OiHMWjhvljd9vyI8v6MSo_oXRCpwcbFHwQKlr8ErvXY3hroqk9rEGzv7aiwk04ZukUq4Hf1sKmRTL_kj9EKk6rOfc-NMBbYv6l6n74ZcPmUQap-VKG6I9wJ7fKDzqzQLMsfroyauT3WdwDdcnEWKtbedSxDxdlQGZokkdp04fXbnZLH1QMIiSnYkWcgfXlac96jZbtReNaGi5_8nvm-SXoAfWxxFdZ96Y32xTfI8c2k_sjEAFRshefBHFLJCEq-CRWnZGXcNv93YFYyxHowkjk7p549aQdhge-mrmtmTzAOYopxglxlQDEuW5dV1eltvvTYv9woa-lAui-Z90w1F0o6Bd0v01t0QBKCazbdHiYn8a94yFHQ0HT-rVZ3T26ihm1A_Yc6cbN0kzcG5XSVaK03Ljc9phomdva2-Z_Pl-o6jjzGzSUUd-hdhZuQ20xnDnX_aflu3CSNIltGK8Yh_ew6MRqPThhvuwBKP_eV1z6vQT7d8dAAolX9_miAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=bRN2eQ8oBFqwzGNyUlGPXvV_hzRjjGTyn5nXE6hyatfRGCjgXR1ojvWC703sFvY3pO3_3ELakv_WxoWSeyDCWItHsc9D2BmlV193pGOfXUkkyvNKBZlqyZ4EPRmCFE02ZE-QBP0S7hnCQhp6VrqknRI6Zn1_BG0gnb8dPE7pemL27a8OiHMWjhvljd9vyI8v6MSo_oXRCpwcbFHwQKlr8ErvXY3hroqk9rEGzv7aiwk04ZukUq4Hf1sKmRTL_kj9EKk6rOfc-NMBbYv6l6n74ZcPmUQap-VKG6I9wJ7fKDzqzQLMsfroyauT3WdwDdcnEWKtbedSxDxdlQGZokkdp04fXbnZLH1QMIiSnYkWcgfXlac96jZbtReNaGi5_8nvm-SXoAfWxxFdZ96Y32xTfI8c2k_sjEAFRshefBHFLJCEq-CRWnZGXcNv93YFYyxHowkjk7p549aQdhge-mrmtmTzAOYopxglxlQDEuW5dV1eltvvTYv9woa-lAui-Z90w1F0o6Bd0v01t0QBKCazbdHiYn8a94yFHQ0HT-rVZ3T26ihm1A_Yc6cbN0kzcG5XSVaK03Ljc9phomdva2-Z_Pl-o6jjzGzSUUd-hdhZuQ20xnDnX_aflu3CSNIltGK8Yh_ew6MRqPThhvuwBKP_eV1z6vQT7d8dAAolX9_miAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=snfmXWm8OXqwv1HEVlrDQWBcfJYMHarp4KqNY0DI3zdaNUF1dzmKWWFqrJ5KcY5RGLXm-U4ZT8U_CgOLMnsgV8RXKkiry2tOjyCgHmcHKi8jMw_0QMUEPmqI_2v7FGIKSR7AcnlOpEMjDMIFFZra-Bumm22eBUC-3ItW9bugwSLtWMHPkj3g66kZ4T0GGRwWoGzhAmwgsDYS6_vqnIjQ_n-ahEHJUnICDTSDo8OxOaShWYqEETPVdKg4ZnLVPMWHkQxtJgvBRDPoJb2W3Srydxi871RuJ9Z6myGkuN16cstm1Xszi39Y-hVgcfnLEVedtFzs8S5H1bjvsu4l7jUqHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=snfmXWm8OXqwv1HEVlrDQWBcfJYMHarp4KqNY0DI3zdaNUF1dzmKWWFqrJ5KcY5RGLXm-U4ZT8U_CgOLMnsgV8RXKkiry2tOjyCgHmcHKi8jMw_0QMUEPmqI_2v7FGIKSR7AcnlOpEMjDMIFFZra-Bumm22eBUC-3ItW9bugwSLtWMHPkj3g66kZ4T0GGRwWoGzhAmwgsDYS6_vqnIjQ_n-ahEHJUnICDTSDo8OxOaShWYqEETPVdKg4ZnLVPMWHkQxtJgvBRDPoJb2W3Srydxi871RuJ9Z6myGkuN16cstm1Xszi39Y-hVgcfnLEVedtFzs8S5H1bjvsu4l7jUqHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgyfBDuDCJAt0JNr3swz4HIiKL9HrZbuqCUgpWgoWH-EZ48shYa12Y9jdCvxYiiUNFYEdJyEo7wU00C_BFnb_CTyVpzrMF5rOaoq9kfY20upu4yrh3hB5FuUoO5req5uCes4pUb52gmb0Fy7wTOXqJ3zoNQli2K0qbjfW0UG-maUyxTkGqrZoG-0yyCxvc7BaTOLtGogCdjOavj9BXcFLXh7XHPNWWIadDPMDLkUiV1vEWOIIbA-gd7WI75ohIeh1Pk1T33bNTZMkSWE1h7eaOVXSgYf4bfPEE0IOn0k3beN_HQF1mbN29UXT4qshW1DSNBZOglA8ZOoGk8W2oZOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCJL3-8VxSn7fEsY3P6E7Yu35KygkPYAz9kSrPiP6mOf8U_s1hTygNHV29aoJtMFV3uDNu2SOmOr0pRE8Uvfb_4v3pd1wxSiC7wpZnrAVsKJuukgP-edn0XvKe6r92a-BQk70aHqprMQhb3F-ozQFNjyygGncCdKUSeTnA49lpLU-LKQovR3tXzfRYEQ13VxHLLbiH9ZOq8KL8MaWIGiCzWEk2jLqvCACusOmTarI5B3ycu06qcPPIP_Ppb52ylFXvsw2sTsuqNG8bwZzP13zYu87MoCAD9yHgVbxg1mP8ENRHtvk-EBW8FmpMPAivbYtiDzL3qDs_aptE84S3_x2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4kUTxRXfz-D5HD_bWoXgRgrYiak-pVLXVxgp4-BeojCHshuIc9HusfxGkpxvb3FpuKDTuEJRotNcjc1Q4l0UI7S8dvhFlWitvfNEqTMoz9DO13EehM3mEg1YTptXHXCp6iWN1PYngvlboCUMmcJgS_fU7dwZKWFh8-wNn5fgjmqOkPtTkiFIcziU_eUdyuIN3IbPFQ3Ybr9jGdcwqUI-UwnZ5Yq6tio2u7PqDKaggJpV-PxFW92N2bMtLam1MDfxNe3ATnZs0KToZJ0EYnesRz_GSkv1NFWkCFCB3bxRL6XJnxJzF9ATpwzI_MDdbaOGGrM8q9bDWB8BdYZxQ796g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=YEOHdLMVPtOYw3J_5YPdxn-Gv_SFUFocUTead4paxlJGZnTIUZV_hd1LI9wNVEaKNoN4gm3gWtJ4cppuv8BUVDoGelkv7IjFGqQiNpguBEnw4Ut7g-q7tQEfJkUKWQyTL5jZECN9R1DWNqf2W-m-lqWgu64xR_w2IeqNujmzqOg8E77WWbpuSUUQL9KLjZidEWAPqRsVL7aJ-P3hMr0sCeLuZKZvRsSfRe8zfqAyf76VHo7sUY_VzIZ5_aoAK7TvhZpTr0GrFHOLuSocKADvoQZSoI_--UyZ6W1jvoJ8UQ2O6lDo8F0zwst55t3ABxnCGemJSaEJ3wpxXwKYm1kVOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=YEOHdLMVPtOYw3J_5YPdxn-Gv_SFUFocUTead4paxlJGZnTIUZV_hd1LI9wNVEaKNoN4gm3gWtJ4cppuv8BUVDoGelkv7IjFGqQiNpguBEnw4Ut7g-q7tQEfJkUKWQyTL5jZECN9R1DWNqf2W-m-lqWgu64xR_w2IeqNujmzqOg8E77WWbpuSUUQL9KLjZidEWAPqRsVL7aJ-P3hMr0sCeLuZKZvRsSfRe8zfqAyf76VHo7sUY_VzIZ5_aoAK7TvhZpTr0GrFHOLuSocKADvoQZSoI_--UyZ6W1jvoJ8UQ2O6lDo8F0zwst55t3ABxnCGemJSaEJ3wpxXwKYm1kVOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=q57YD4nwooRYNVQfjQxDucVMOS15EqC4OVGlpedKA2F2UxnYu0byFUA6qI6G9U9FEcDcmQl3xL6A_NHnu_D21GvuFr_GByZcLK_QMWfZ-mfpctpyaa-U9Gm8kVPKTpkiM2SSK_OP4wzReJrmIG_Msa2_v_05PWuCjZ6wGGcua0ztX-stI6Gbf-CkbH7jh-gwTC3o-bNmHNEh5SHmLsNCrJD8vRjZ90yBeVm3QU0e5dNTQhCl1fKyBKIa1-n0kQ-sVcmPu3E15OwAmVXzIaPoNLLYram4NmXHn5W7X-hVn978t3HoVm9rnzmdwKLdWGw9MGbX7sISckjXUFjAOKK7cQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=q57YD4nwooRYNVQfjQxDucVMOS15EqC4OVGlpedKA2F2UxnYu0byFUA6qI6G9U9FEcDcmQl3xL6A_NHnu_D21GvuFr_GByZcLK_QMWfZ-mfpctpyaa-U9Gm8kVPKTpkiM2SSK_OP4wzReJrmIG_Msa2_v_05PWuCjZ6wGGcua0ztX-stI6Gbf-CkbH7jh-gwTC3o-bNmHNEh5SHmLsNCrJD8vRjZ90yBeVm3QU0e5dNTQhCl1fKyBKIa1-n0kQ-sVcmPu3E15OwAmVXzIaPoNLLYram4NmXHn5W7X-hVn978t3HoVm9rnzmdwKLdWGw9MGbX7sISckjXUFjAOKK7cQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2_E1AQlneS_cWCRrq5Y3jwFiXuG4ui0Ii9_08ZKYtz09YbS_WJfTwlPc123MLJOdhhH_uC-OdHKggpLPBVwb53aVYVMVEBbupRct10rGikUu_egMhVBeY6Em2KRvNLN6ezMyc4cWaC9i_MxVYMpSkLayYAHulZRfai4ia-sc2bpX_C5ECLJElMpv0na-g_yK-IXmaFsCEPMC-nlvTYLcWtTKq-C_bS-OPNjqo12ju_R6nRN9k0cYz4yyM6zZdi5keXtqS5peHUOYvI2bMIJJ7uSOObqEq4hxrYxJwfmYDhpC28kK_jNsQME_sjEe4kgWMDPvxMKozXYX_KQ2tif7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUv5anB2qfc-brRh1IVJenxVNXBR0sZCsS_HQO5fDdRmfS3qbRGp8xsjEf9Uje5nBbcXkC-QdgDT5oHzh94KGeFdXLTJhJUO7yOT48zlcgCBEJdFxKmbzPLPMT4f91Se-3Pxl4zLbStIjl3sROPy4gDLxY2Ji1oTx81YlzciaS6Kjm1B_sqLI_bHtYm-5M6GVKX-iAjZD8qsuPR05UFej5AAOGArjArlLCmiIMfcGvInvBRZmcUYzDNd98S7O2yy20QFX9oTOhwtBJcmJsNQHa4rBEB8PMp4Z5J_LZxafM2YCH8__zbDb_rWZTuZhYe6o0Bok-mCja1U9qPhTmi8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=vUxpZPfMWHwqxz9Ffp8624sTdo0zyihqTjFz6WwyEosQMqSke2ZY_D2CofOIYaFplo7PgKRojwkhuqiMpCEin4TCjJRp8gcKFnsUFSk9isCgKaLwjDWG1UnlX9zQcAqUKotAtjRyKyfipdJnQMYj5L76gZCVB6lPu1fH1_N8IUL6QJ7-W_YUPARDhDMaa9PMN_eggX9jTxLZXWpldE3jCW3KbD_vY_xT0_JsKNP5ucdzNwaAWH0WJxe9riaCN3bKbeS0FliGtQASWU4taeEoY3HDOlB-NMzeIB7-YIC3Miasroos0jrvDQ0X3KhBHnEFmJooAPMS1tqwCvyQEKS4Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgF7LFXvuAoPATYqamraz1C3eSUf2OGURJWv-N0XqPm0Vr_wAWxXKJ1HnMTvnZGCms6nLofojpqC4FAyXF-s463oPewYyQVqkLru8OEVmLsji2zWiEptaitGG1NSsH_rymD3dTMjV0EFTDozi603PN-ygBE2tPpgdq8pl_8Npx8OcnKrRXUEnjImNvk9WM7tqLE3PugoTXCHyl7ISW-ur8vOxGzXsse8bnjoaL_6z_W4cr_c1-Mff8UDqmQ2pKQvR_5EbcKgifFx-wlDl9Rp5XXNPZ7cQUfPGbYsUNxlhM0DvyR80D8IGC5FIO6dHK-8v5rEvOiN4cY1cDHuFagSeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDV3RgDs8RBKdPKdVlP09jUI7ILHH8KMVZux3BG8vIykVG5gQ7mhNrSrnQAvwXsH1_3FRG6lf5r7djnM3fPSevIGECIzS7fRODdgM3AwJRtYURSu9R5e1B3qq0D9ugDgikCaat5EzXwqEP7a46bJWd2kcOTllROYhO1PgeFBeEimiqkxt46FTSCV-2ukEKzTiMUpGKVt3qe1e57xa3rnj8eo2qGcSHm_rVAtGiLh1GhIBj-rbAxmd3FSq81fqwCYsZe-_826aJe2hzYDHIJVZPN5GkABCBDAiPtnL3eabWF4oBY1w_Z_0OsiH91UdAe1cmFNyfTF89t41peUMR9jiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5ww8_WuL8X9ZhffIX0cANU8Cql2x2M8EdHjpfp1PK1Lpormagvsmzkx_OKL2-m0SM3Oh00hE-XWkx5HL_1twwI7olFv4q3Fh7JH28bEcFTNtf0_5b-XZkOtpndhlrUY5aEbRCY_n_9qe4xiS20OzKMlruOWUCKe0IdfP2RQef0GfpV6vCY5hHT8rZ54zfuko9dOwmovbUKWJiC1HKVJESI-PFE8hVSEoUfmBzaNel7tCQ9z_5DaGFosWAAZkA_89eoCNWxhvW8QgafENkSMZZrZP0HZ5v7vqXUOO-XV_wbaB9PbuBv9zIhxTHWXmquwvqwub20bqYRsWpVwj7lHJDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I5ww8_WuL8X9ZhffIX0cANU8Cql2x2M8EdHjpfp1PK1Lpormagvsmzkx_OKL2-m0SM3Oh00hE-XWkx5HL_1twwI7olFv4q3Fh7JH28bEcFTNtf0_5b-XZkOtpndhlrUY5aEbRCY_n_9qe4xiS20OzKMlruOWUCKe0IdfP2RQef0GfpV6vCY5hHT8rZ54zfuko9dOwmovbUKWJiC1HKVJESI-PFE8hVSEoUfmBzaNel7tCQ9z_5DaGFosWAAZkA_89eoCNWxhvW8QgafENkSMZZrZP0HZ5v7vqXUOO-XV_wbaB9PbuBv9zIhxTHWXmquwvqwub20bqYRsWpVwj7lHJDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3Lf5qAgM6Sw9YMwsuTq969UKVl0-V0ID44xdPDddby6W-PsYbRUmKfMs-E4niLQrQyjN7kpjl4jD5XA-96WxuomLhKD_Mi7glbcaARulk3VPVHRw6QCPanZZERQnje3ZiEsgf0Yr1t6JKfXoAW8dn29uFYY2HmFSM5-SExGNqH99rQAZde0DyMY7mrClPxJzI6gPqUimTp7LDOGl2SfTbStkp6UdwVxpzTEBgiU98rDTpaIHTEBiCgd1-YoX0bNxzUMblvFu---peghDSwgmJ3N6H5472bB8CXjLqH2vsnXgD8SyS9MB-LKnYjva-aFX6DNm9_Af-9lM6cv33_NsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zj9lCv7Pb5iqnQjoahkiqkhJrh6bYhJ7O_X0kyKrnSG6SsZhEH2WuPq0uMQIqn4yijbZTZxgy94sza67uhUq6zakvTM0rNz9UFLd2bE_NdQt2pD5p1xbjasr4pt4ozJdoO8aG6M5WxYcr3-UVmMMx_Zc_kCVBy67sP9dv8LaK8Os-feDr6i3kCKQ0ARnggROSfn4gVkEffHUR0KLkS1HnEsGju9gGu-NAPREsqTMR7CrOveGZu1cInCs0VAJGIt1KmID8fiwu6fP3SMfsfb61z0r7O_phtd1_qSg5m_D5Bd1UNcBk1dHjBdIu_YFm8354MUKrRzzDOiF9tvtctn2QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=DVz7_GRCV0cpGFYJ848WfGXXeq3cLsMB8KhjKsQKr1_7pjPDjrSiv7BBbj4gZWx3QDZ18T1UZsobkdojmdY8KSDC-vo0vwL6PzG1_XkVL3Fw58W_N6Sag6i1g6jslYIqUNesN37at0BHcCeC8gb4LHg7vrDcgDn80yxgM_nmldY5rIlmhnHNUxe4R3r3wpSFFNC0a0FG3sv2SE6od--1vsCwBspw6Qx7o1AnEt4l1U26GkjMKKbBj-ZM3EApQ5aC_vS1GFTwlGW_Hh9gcFiU85sruoRqfv5mtsrV3YkEpwDOovzY2EC3djDwywm6Hb9EEG9IP942k95jqyiC0T5BHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=DVz7_GRCV0cpGFYJ848WfGXXeq3cLsMB8KhjKsQKr1_7pjPDjrSiv7BBbj4gZWx3QDZ18T1UZsobkdojmdY8KSDC-vo0vwL6PzG1_XkVL3Fw58W_N6Sag6i1g6jslYIqUNesN37at0BHcCeC8gb4LHg7vrDcgDn80yxgM_nmldY5rIlmhnHNUxe4R3r3wpSFFNC0a0FG3sv2SE6od--1vsCwBspw6Qx7o1AnEt4l1U26GkjMKKbBj-ZM3EApQ5aC_vS1GFTwlGW_Hh9gcFiU85sruoRqfv5mtsrV3YkEpwDOovzY2EC3djDwywm6Hb9EEG9IP942k95jqyiC0T5BHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxEYXbLmT-840tmLI-gRd4saqmjdbp_xZXNsaTXEI4Kx2Jye35BB1qGPWeopoeGZySSAIg9jQLnJT8TOL3pKkMyQa6cH3y3uJeaeHLak_hM_uCzO1B9EnUxmnJrBeANzIwYUuQvs1AZKI-TyWtmHXM0iiCOHsYE3MSxkQVH6fLkN6Rz08TFuznN2yTd3cXPxVygS2mKlBYeCAbJG8t5_FxXFQRF2FElNdPnwTI7Tl1eq0IVsM6utytlnC6L0FZW-KmdzbQPsInGdxVpa7iz7O9vQey4ZdX6fk8mPx1VHUjJmYnBejtM3bEjk54WnY6-OP1R-bz8QtGYMUdY9USfXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=m8XQu2t27B4mFk2f45O-nm2TIsVF0ddOCIm_xCjXBsvmtmcdNmA7ecc-86B2lOwXvyo6M2fUz1hhK1FkL7nPXFUEtKcAwC4zTIaOHDron9cm4yg1l80haZLCMn11GaLacRq9W0oMLlVCu5e83rYDnHDiLkExVEuXZ-w4rMCLhybhdGvC9aydVwXvGuQCWoUfFRii3dxSGR4YeYHwyfyOBsh2m8AEEzPO__QbO1PbVEVO-gomfDek3NMvBZ2kv0lnECN0d0YpooxygSQST095hT8OHwVMsiDIT8oBPYPxxzap_8Rk0OQFNlMSxdxolaF1gTau3H3dPKPa87Ki6jAIDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=m8XQu2t27B4mFk2f45O-nm2TIsVF0ddOCIm_xCjXBsvmtmcdNmA7ecc-86B2lOwXvyo6M2fUz1hhK1FkL7nPXFUEtKcAwC4zTIaOHDron9cm4yg1l80haZLCMn11GaLacRq9W0oMLlVCu5e83rYDnHDiLkExVEuXZ-w4rMCLhybhdGvC9aydVwXvGuQCWoUfFRii3dxSGR4YeYHwyfyOBsh2m8AEEzPO__QbO1PbVEVO-gomfDek3NMvBZ2kv0lnECN0d0YpooxygSQST095hT8OHwVMsiDIT8oBPYPxxzap_8Rk0OQFNlMSxdxolaF1gTau3H3dPKPa87Ki6jAIDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA-yGPtX4eYWE8stQ4xpyioVtb8rnheRPZDXKL6-BJi6tLbBlGuGWHrt5NfnbKMonLzHU2pM3I1CEZLhLG8ZbP9ThsgjLUkRbfqLxse1g9uhenZkv98O2LDhiXmdZBsRbtbzOJ2UfjWEmXsGZdtUYGg1tCQQwJfo4rOtNT_SrP7wmDBfSDi5KK2BSo6oZteHUMpPTEtU0aVuJA7HO3qI2Xq4OqXkOg4SiGVQivwa9cfZzuBoP-G7QHReRNo-0H6hrKtn_tna-RvdpemW3d_FYj9us0gf70D4Uj_dt3Qqbe_H2DPab9Pu1E795WR62kkDajOQ1gwt7TXGIRjX3R-sxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_WM4ATyFlnrO5ll70cywIshnCgn_34nRo7ly4c4Jy8MR_3vBlt5LfN01jy_NmtPuxMVEOjyEwj6qe8FVuhbjgSHATf86wUdBv0dewRArw9MwQqhx3kojc5Pi7eWtqa95ZgHIrP-ipPYH0wpjN_A9gucC2s18ENVJNQ9sMzikxXAgWZlZe08ydukuxJPHZfGimp0WOquIIsBtBNjTx6NbNdZkB_hnUcNL_gVYWXz4P-cNEflJcUJSZQuekLazv00u6IdhXqx4zCuicJEGY1JfhlhGRj9IOuij2J0Dspgu8yI3F1hwn9FN3Y3mT0FNsqiZh_NKkQoZXp9OFqmtm02hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reZmQGXUk8KOM-yPqonVlz_K5iidVN1wTGCZZM7aQDTQ2o64fnrqvv4o2FP9jmN71o1V5qdF44Sh3mcZ8z0mQMDOqiC_j2fG6ZqUG8X0ggQDqUzBSr4Ze2QLrDRYubWM2MXfH0YLNefDTybf3PzT11VSpCGNqTVLXRbhFfpvk5gPfArrV_0HEn6hXlHTPqV8SBXImI0GGqW6vItrrteGewpegiD4mHklXpvaNRWa0JOZcj-5FV8U7nqzrPniHYwDd7hdWWV5unnW_xGMAGIJzaIDiMFiD3I4VyvMvFyJoT_a5s0fHDdLnDcYzUqmJG8c8q8uZfhbvt3YPnFtP1MslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJo2F8fqJA3LVRR5V2rKM2cwRx5zX_diDOn7vOqgLTcPXyRbZfVNkzGW_fjc4P2k0F1P7MpGGZ325I9ROygNTO1EgfTQOgmJ6uN0gRli7PrqAhCMZlT7iVPbq8EjQppXpcejYs7IRlZgHlmwn84iD3ioxw2mNUW933q1yMChMCJWN3E4TziCzRwK-k0jUwfjhxja9vHAP4mtFtIuEosNc91Qd0DQpr_Q0wBl4FqSgNsf4_olhJR1sRBUGwjWqKBlqCPCSkTNNAZO5_UtvYTgxc7q7rAWzRf38trXFlNM3JdioUZr9Au2oSwxuen_71idgy-1tQr7mzdTOFUssMefXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vGxsBiwJBfAiHltKJ-8iQvYr3cMasPNSN_wReVZqfKXvOboVoqsh_f2psxApPgNJp0QPQJU5oeRpaDcfRZYm5rTXqfC1v96i6iP3Whez8FruBGLQ1wVb7MYovx2iNZ-n52kpr1czcPUjnnEhz6nSDHidbubrlOgoVE7zl9OAdHWDCR7yGKJg5HcvPdiAHkolu0763qYcfioYXRk6hAUst0SNbu2pxm3XWkS_29W9Z_X-0q40jMhxNEa1OFt8OxNif2WO9ZfS5sMZq913kh2VUcLQ_ozTPitdzXar3Tjh6FupszA9lCZjkf0OIjny_2MkKqVSnLL8f9fablXrtF4BAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fkdq9eVKi1w3hYes3-PG_DnUzP8mxfxxR_64j-Zqd3sApQ3xkvNdwmfNMZgx44VDYVqWBeKtFj61HrVhvUr6OcK16a9G5YMvhW7sVG8WubgOUrF2Q8e-JpHPkvF8JbOeG1fKfA9weUZZ1GD0yWKyJ5Ka3BjCS5jrfPklvlxzQCaR3qJJtClrYwCtVUuxH2laeS2ZEqIvjRlyu12zDIgg_zgQR86_F0dU_Gg-n9EM0VFxpi4q_m7nZ3ym4XrpnKjU-dOxByzZ_iHO8yZbCrF9_wuulTXCniZNyjNMjWXQ9v3zyyf_bP4UJsTqN_Z94q_RjvmTwH0ZPRLzJ6M5_V9PLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kE3Hs90308TddlSGLcOzM01Sj73YZb-P1egf7eu0024CejrcX98QNPPuy5W52k8s-se8iHHEOJJ-1VRnK6wQ6jPnhjT92YF7vuLTkkJN1FBSk9NbBPN3ahHBEx1hvx1LmoZ9-Q6YHtwXbzoswE7Ky0_XbyVF2eQusTMLfcVN-kYWgUCVrinRhoiICQzXj1VBmIcIuuJbrAEiIiWJUD151IEspldUCacniq4MAt2zAc5yx-VrtGHG43IIGg_XfCfrOme7tHYEZHEMS-AIV3P4oMz_5BWVQBn36N-Xejk1xTUMmKfvIF8qErxRY76LPKza2eHq0ZoCbEd1HUqxh-JWRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVpUPrUNue_zkoUbnePl0Naff8E-pwfaLSwqVCg4ae37RukEqUfw0yuTvAwbcJJvgiCyhkmhajbPHtq9jSZb12DcEF8TvXS9Y6EoDnJeOt-7jkrTbXwd3dHUR0guKmipOTiPuIg_zrIMJ8HSq9jQgCXK29TGyfTHi_RxjyeW2LcfPbU4lgmGu6tJjXK1ghY-yjp8dZfxgDN4MVzjNjHmSQwpEe1ZVQ3KMin5zetyR9Vug_vHFDX08axAAeqdE-_VqJBCLpYcB8Q7TeIq21tMRp3ujyqEdrRBDLh1Ory8RHu07irCTSZgxQN1FCcZ6Azo97fTRQatBC7MdKYj9ji2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZiRFXWWpJAtU8BvwiqPLmpERsZcBidx-4kyT_c5X_kz8j4pd0HUABh_JNE23MqpLEUCBihaKAPi3-gi1JAcwISSiumRXsfYd9DXG4j3X-SCs5hQj2JPuXlkLzL1QkSdVXPh0Hw2wW8y5jjtBTcO00380i7dXnTl-p9XHi52X8qPHn9HoxIGA0dIxUAl2F1_7Z72Ip1HHx3z0_lwWnGAjf2ZZzVkTI-U7TYBuLs-egHI5kzJ5uuu7dxPTrWmoAI5s99CPxMIUW_uz9W_VUPQIDCpGOhqKHZKclCsmHWBs4NJwALuggOkNwIhOJEXS0Go2QayhmmfcKyqKfd12keqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=MEbeXDikjfxuZ3gI_rox0ADZ3eSBVDs9I6UJiLJI0vPOAnrd0H_4kiZrJ5wAmg9Ehb42eoMvKwSlL-S9TN-yXc3qpQssEwcGT8X1hFCiz9W5Wu0f-E2jjVJJL6KbHTduDrtNtwo_gcAWnn0_lugHIDfxaCVKsUnj8uSFTjiPLPdpocF1jxDbp2Rn6rrUAs0RILfIq5amer0aP9smBsM4kpiXad0Mwy4stcROHWfrx2KeeQl_Gt8vdFixj_cgF-xGtICwBnskK6KVm6OfWiyqDu2blO02sGlExK9XGmbZ3vg0Gg4zkBH0i01LBbTpEqb-TjEFfUJ002t0LUAMcGjr1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=MEbeXDikjfxuZ3gI_rox0ADZ3eSBVDs9I6UJiLJI0vPOAnrd0H_4kiZrJ5wAmg9Ehb42eoMvKwSlL-S9TN-yXc3qpQssEwcGT8X1hFCiz9W5Wu0f-E2jjVJJL6KbHTduDrtNtwo_gcAWnn0_lugHIDfxaCVKsUnj8uSFTjiPLPdpocF1jxDbp2Rn6rrUAs0RILfIq5amer0aP9smBsM4kpiXad0Mwy4stcROHWfrx2KeeQl_Gt8vdFixj_cgF-xGtICwBnskK6KVm6OfWiyqDu2blO02sGlExK9XGmbZ3vg0Gg4zkBH0i01LBbTpEqb-TjEFfUJ002t0LUAMcGjr1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=lD1yafq4xSjnbPfACOescT3yBinHhE31oeA0nRIgyhxOXTflQF-AOnDBBmAXswGxe1PfXDMZEXzNTx5-oaJF5yAbup21ppWP8cMWsl4O4kCXpTeiC9dY2JBA30lRI0ji7hrFVfZSYhXHnis9jKBJgKKvM3_PjqtHPwU1Pavo9kz3Jvbhdmdr8SwOVUMx71L9LohT08Ogq-0X6esUT1J-JalfjzQFObIYMUEo56KcwDgqu4mLVxEg1e_hemWO2ijAa8Qkcu7qA_XSJTNw6NvoS2ijK6XDKVgcJRnrSFK3vKAwUt3bFvg3pA-Z4QHK4ozpxRL6Z3aY-h02McQUaHUiIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=lD1yafq4xSjnbPfACOescT3yBinHhE31oeA0nRIgyhxOXTflQF-AOnDBBmAXswGxe1PfXDMZEXzNTx5-oaJF5yAbup21ppWP8cMWsl4O4kCXpTeiC9dY2JBA30lRI0ji7hrFVfZSYhXHnis9jKBJgKKvM3_PjqtHPwU1Pavo9kz3Jvbhdmdr8SwOVUMx71L9LohT08Ogq-0X6esUT1J-JalfjzQFObIYMUEo56KcwDgqu4mLVxEg1e_hemWO2ijAa8Qkcu7qA_XSJTNw6NvoS2ijK6XDKVgcJRnrSFK3vKAwUt3bFvg3pA-Z4QHK4ozpxRL6Z3aY-h02McQUaHUiIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=ZAWEyG8HGw6XDTi8vMe65utEQP7fTHbaPS-RyVFs51OQ3Iw4l-6Fe-dSDNe4dPKnr93qUB06J5-O5PSkbm_L-PnTi8ShbdkUyqP92NkGp9kfTg-kJ1ma8fPQ278dEceZmK8yQG2gK04Co8QXoM5AfEn2y-G05it4k1OR5OiLy3ji3A398Y7DtuldP2HiUqUwMBQUF5Td3Av42FvqOUHbJw5bxJiQ0wiokgVP6BnbxAMSd3B6qfze1JyLGJd-GY3aNG5mCc9LMn0JXx2lCfximBUHpHnYQTGGl0a2qszfkEgaec48ngOhUK5LWN_FbxzLWJczFUKMIDs27YHsl6Uw_7PvSieePlayrWVOaR95n7hMzK8IBo-sUTUKVq_QYELegpx56sQsEHKpG5OwHRHytI1xOAyQZFR8yDporP6lC8gnz9fSeBJbb5WXe5uQr3E5vqormVr4Uou8MEG59itZlhD9MV7elBUH0UwCfgFEzjF-FSTJCSYlsWogcPCQBUCx-TYuwEWGPdwAFNYJGOaN4UgDgTFjKs-a9G3vjJ5LWKeQA8HRhNMoW4WfQBKCAtbqXq-jQ_2l83hTHQBqa4y3xEqXO__yPKdqKSz9TJZfkcpE46LW1gCjGXfBTftF9AwXMiNVxdvb0KD1-IeQS_-k9tAkCqo_p7tBE3I9JzZHmTU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=ZAWEyG8HGw6XDTi8vMe65utEQP7fTHbaPS-RyVFs51OQ3Iw4l-6Fe-dSDNe4dPKnr93qUB06J5-O5PSkbm_L-PnTi8ShbdkUyqP92NkGp9kfTg-kJ1ma8fPQ278dEceZmK8yQG2gK04Co8QXoM5AfEn2y-G05it4k1OR5OiLy3ji3A398Y7DtuldP2HiUqUwMBQUF5Td3Av42FvqOUHbJw5bxJiQ0wiokgVP6BnbxAMSd3B6qfze1JyLGJd-GY3aNG5mCc9LMn0JXx2lCfximBUHpHnYQTGGl0a2qszfkEgaec48ngOhUK5LWN_FbxzLWJczFUKMIDs27YHsl6Uw_7PvSieePlayrWVOaR95n7hMzK8IBo-sUTUKVq_QYELegpx56sQsEHKpG5OwHRHytI1xOAyQZFR8yDporP6lC8gnz9fSeBJbb5WXe5uQr3E5vqormVr4Uou8MEG59itZlhD9MV7elBUH0UwCfgFEzjF-FSTJCSYlsWogcPCQBUCx-TYuwEWGPdwAFNYJGOaN4UgDgTFjKs-a9G3vjJ5LWKeQA8HRhNMoW4WfQBKCAtbqXq-jQ_2l83hTHQBqa4y3xEqXO__yPKdqKSz9TJZfkcpE46LW1gCjGXfBTftF9AwXMiNVxdvb0KD1-IeQS_-k9tAkCqo_p7tBE3I9JzZHmTU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5EUeLOZUS_W2YgGT2xfmIKm5cxbhUhjuVjjwvWb7zPdj3FaSpyoymC79yKVE3w9zu7rrvSUS2wQcJoDFLic7crBK6N5asUoBR9RiUM5dfxRyTksQLHbABqgpUgqEtfFvEnrc8GQ6NUCPLLclpa4MjDNYdlc8Cnw8RUTvnyMx7C4_8PPw-UdeeeicJpSLH5XeYMPWWkeRVkvosxBr9WWWIuxFKhv-Vad-L2vsO4BRKFYWzuZur66x3nhbIWxtd1WGVPCoKRaQ5kFUwSny-qTr7VZpGzJ91O-b1FK-HIhhq4YJI_GWyhLAtKxUN_Km4XgmbSGbIeGMeFSIExYUL3Vww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=op4BW8yEu0K16QbzO01wFWIRUBD674k5DanV-M8CIQGd3aS4lQ6v9OtSEvQy-WzDkghU-_OWRliYpuN-taLFZuEI1ahdGyS-l4GRbvTao2yE8MvjsCBWkIUlKn27Td8MLloc5WJmA31unQMOf08Cs4DbpfK8UtqRs1YpvIZDLtzhkk-zdmde6RZeTehqPnrTGs6U6CcvosQRRjKbr-r6BJWHbtjaplHjaPWXqENbdzw2XyqqdHIx39FkgWj6WBP4VIXsGt3n4LkD2ufv0br5KnZXixlC1_mXHrHSxk1D2Hho8d_a0I-zaLZQnY6DJUBUXqGm9Yxz-l2YNwqv9QUjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=op4BW8yEu0K16QbzO01wFWIRUBD674k5DanV-M8CIQGd3aS4lQ6v9OtSEvQy-WzDkghU-_OWRliYpuN-taLFZuEI1ahdGyS-l4GRbvTao2yE8MvjsCBWkIUlKn27Td8MLloc5WJmA31unQMOf08Cs4DbpfK8UtqRs1YpvIZDLtzhkk-zdmde6RZeTehqPnrTGs6U6CcvosQRRjKbr-r6BJWHbtjaplHjaPWXqENbdzw2XyqqdHIx39FkgWj6WBP4VIXsGt3n4LkD2ufv0br5KnZXixlC1_mXHrHSxk1D2Hho8d_a0I-zaLZQnY6DJUBUXqGm9Yxz-l2YNwqv9QUjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siSSumLDNaCPl_JSaCZKkj25n2JAnfL195WRgdh7t2FhocgQQdNk4_NDizRaecXnwr_XJ8HH6veTGkcFFvl1ygshIuWhTlc3yUK4Mf9arDHYD09uT8vRfD5u8Xh_0bq-c7z65niNZwGhLQkUJL7r3gdgwbF3FwMsUSOVgQO65OVvq6wE9aBO-8wBX2iKjPqkHyIwndzCGJPGG-cY5nOREUqrYuYYOKRnbPBCbvn_eqyhSWiJ3mUql6AabvLwzO4Ar-p2owanA5iKOw6duUqna5t6TaNqGBeUpLazMNlx3AMb66vp_cprLff08gzhB5XXX-w8glqzzLo9FyKWx03JCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfwG2bRoGsAR_fa9CfFzOgDacJKJ5dTxQMvMOkW1_ilHevKc_Dn-2xODYiiUtN0quO09UKSOZr0OUpioR9kURTMqKe5U2DfCCY8HLxmOgC30ipNJFStTrpuilfZo63kHZFlmRqvayi_9LhY_57hVp-am12UbXYdQXfT5hadsChnWLiz44wLxx0YEi1qv8TLvnRB5Y9unAWjJGq5hJUcwuPML97jWKLsP7NpryhtAzdhmSzXGTDrZK16KjZatWAUU2Wv-iI2YyAcDQkZm5SfSTUOX689Ei6T_CVTKKiO9ugkYFQwHPpVb99bkZnn7S7rONaEMF-I5PUdfgNmnS81_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Feor7se8cEbIKA5wQPS2UjuzQUTq9E2U5NnvqnfNCBhoHuap9nKOA-V_2LooF1qzxdXsIANGO_iOVTRaKPqYjObiHrCgdrcFngrsz_tn8kjrMNEnFZ5qdrFjI9RKFT-JlzHF7nMTJOICG1oAFyVc2azCNIzgUFeBO8NWG9AiLA261hjsmcL1t5_o83LmX0slrWscjs1gYH-uZI6ryJtnWF_6-9ArQG8abjDdzbCQ3T6eqKXMXkhx-U6yw5gW526ZpOMLIJPjakJ8df7TgVULwyRL9HF54GAqtDX7hSiqVqh7phikGoz3wO7EXH2b5KN5I62pAnV-Qs1bjI-X5B8j1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W455QykzSX_NhnMh8bQKi6Kfduyf8hl6C77tjUWsyDQkMEiSvJkK_v07qsOrJVnf2kPYE7m8QFxM0qdUO_dWayJy0sfAJDf2YYBw-VDStLtvqGh35yevdGmgXli-Utng6qzNkT3sG3mrs0pRUMlLKl_WtJC8ipq3eN06-4QsDg5wJ2uNBLoqOVpdfWWkzv8up_cAbjiTMGfVt6Og4f9OhfeRTFG45v_jHrxk8enPO-inWW8bVtiGzfR4JFAquPDtZ3wiyYiue1hMT10MiLwoWR2XNYi_uvyPTBScnTNfI1jzgO3qxYSz60E-jzbmApAsdXoF0c5Yd28ErxHH86JUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3eDf6G28vklTxSeVCOc2h9jsx-wWLqsltj609N8icqvpqjDo6ncIISlqcErI6RPYchfbiyJAf749Q8MwGXI3pzn-ulqSFhqYi1UgFM3cKHigO2OzcHbcG0edVYMDfrjPdMID9Y-esTUs0SkKlG9GQ39h4-1HOa0LHpzgnJi7MigRGoJyDWPzf1uPdEvkxgWApa4rvVzH6e29zb7XZ5-Bn15xlBOOOpXBeR5EU_PZtCYI9odFACj4xpLmmbXeluI6EwSZ0p-xy9V_mhnYm04imB7CGwlVqlP5gx-0Q4VchNFX8UCwFuxJaxAlv6jeKvs_NYb3tA48PTJ0WVSLCykqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4kxv2Qy9uL1q9iN0bIPfqVkH-QTdGwdJKKuasUjAUE_Zq7ILOTtH7RzbbhIxlHxpNJS94VC29SYosGh2wImnx57LkDRFNsBKeqGfOWlVkF8orOKDaEWIR8Xp8CqqYWz1DPAc3qfoTwufqlS5noE_Ca2cLADrnYHXuQwUexSCwRXPb0LVaKYl6OZB2HIFRlm50STki1teJ6KON_eJQvZDw_sl-ZSRKbu_rOhF4Di_XU30kY2MEHrCEIfTiqK9I6pSYgitZrG2AZn1Dx6LVm8KbrgjZLEnFqsAKoXdg28QngJExR8jiIHnjtnq8SR9-edtJL_6BDc-1oe-plnmiW9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVxnNQ2uXUv261jW1ycnrwblOW1nX2ifVaMo0FFf1zyo3UG_lLAf_fSKaTjMBItMmBq-81XlWA0qGjtLGHyO-u2cEZhtbWr4gFPlS4ICzg5niVXKqbf-Uxav1FwK9u6zpiUTrzQONxnmy4CIoObjiZw44tE3Ejqm24NZ9vPmlWq7aYcYs_W74-C_2rgJ8wxhT3w9_gn9WgUchXdCEJH9ULDar5Bfu3CRohAwm9NKQNiwPYJk42ItaPNnsiAad8J4cEevqb2aL18aUkhMuTTWVjfygqDOPt5ptlePYrPpTOXTCvzsXGaTLlRMlU5zLhVe-mw7UA8dmFRsk-CQ1grp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEcw-NAHDnTSCPiH6pP7MfV4-ZMCUIBpDlxIQVIvdQAtfnclba5hBZmyTvfDsOr-nMdWZS2KTt1oyaXgwrwTXWLkQU94q0NF8A0pk-oSPRbkIy35upPpZsEBQAKYIh7Aw3uHrs92Ei-T6bx4FtX7Cs9y8OzkajSoruYBursxhPaNLt81B57wy-08BXHYVc7tSK9dm9AgfodkOLLRn3Jl5E3Y7blZ9kA9HDQtwLAFgM2kT6B91trH0g69adBC0v967N2cS3EamYxRbWJRI0f89W7dH9S1FMkNZRWqzeatuQbYNe3kbB8K6wfwzy4D7hZDYLkV0OWSOBXPZOORSr3xjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KKbTBQiQPhnJnkqGYweQmExHvE1iSh3nrjE6-n-xzosDy5oY03fqOEYeRnS2kB1X7k9xzgpZEayIUqryqRMtE1ZHWt8nbKC0gOoz0-L9sQySVSCTPrVXhhSW865S9hwwpimICBm9TPZ2Y5pO5urzM5iwKOmdK3RxGJMkN9jbt3-OA4dvPDJrjIttkzf07XO1CEqXx_dxULVFONxzvZtyDXU_EQX7tyuQZ_0sBnmfNwVihRU0K_fKHMirLWbSzD_XVSJk8wRbNHH_lje8dq7zgO62_7d2P_CQXh6szz_V4Dqid2JmX05sCfCIlC1L8as2GHdK1cXJR8tUKEcgMrsDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OnHZ6KlL2Itg1Hb222cYkGqtafux8ZH-xMPbrWnbC4u5pMpMvHUXToc1nc2plAm--u0oGvAgdj0_IyeyanT0GH9BgYbyODKVmqvAGrs0cz4Sjr1uBmE4su6Z-SHLn0o-Qaqda83nYv8umv44qlWUL1WPd2I9F1ONOboXjXw4lhMQauzx2dHsP3CrVhULp93-3i9q-FcKeMhZ4_uH4IBcd4Z-rk9K0ARAB9yoE0cRQDjtoVFvkFQ3t0FBehR12y5iFhNIC5fNkPvGH_ISIdEGZ7ZaNFfsJf0drWYGJITSW11fx3Z274bRqkx9BqPCr-duXoJQqJTtTPsyDAfvZPG3QQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQ2vOR9RXTO3CzSEoT3q7VAlJ_cETDt5nh-JDsfdjNENUKoc0PJZxeqSwb6wEAMO_OYAM9PfMBzgBuQved80XnSk1KoiPQUO0ImKcga04LoY_dRhHCB6mx94D8SgEFF-BFwEY7rx2FxzV85d8xSoPGPufEOUDFxymJBDDRiMhDfBYBwo48IG8CpEg36k9-0EAD_2JIC8-TwEh6wWKIU3V_-WS-sEEnDTNHWsR1pfrKQeyZHJKAwAcAE2B-MSNcy6mvASDF1CLI44TJBJpPIV-eTXCS3WC4imy4N4C6sd-Fg6cC77fpFYiTatkYzD7UGmK70G8fmk7Zvj2CHJeYMJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcplWeVM4yf7VOS0o5njAxVlJRHj67XIg25Fq_NBmDZCHGQI_VRNrSW1HJqZBABHLVS-yegDQdKr97UQp14K3pn5Wp5mRmhDlLxkI-jjnDSuoToolOOKlUHUBn5VWzTrIBQAMeNvG-JDS94MV1jf4a8-w9M3uOYWakbAuZN7p3whRPUy7meyDZnakLQWreBKMmonxYhs2YMEjunkhdRDMvd2IFzH_4mpIIDd1aIpK_h6zx4rgwTkMcYiUWB3vf4UIlVC4KIajkF2_MHYk8T8uxI9eJOYJlbtWYAluMX4cxrTskGfpv6XGpI71tfYrHwNTQQOb5axBERZU07Sw26AHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sl-8sXKAp8B3F2YgZ_4qWuLEcvYS3nE6BXoh2DLqsCg8zsSa48S8AUdt3f7ibv9siHJ5qyoBE7SHddyK4VT27HRGWUMtpzfLC5vVOy1s8IhchM9d4pOkpEUa4X7Mm5icX81FFPxa-4aOMlBQ19kYDaXnpPQiqAu7j-127wmcBzMeBevLMTQAPwkKNyXjTKkRA0p6pB6qlOwsuva_CgOu_arbZNYPo2w_SaZ9TehXCTwFAmJu60mFzSpUGTC4cQkh2X80xpBx4rD1x0mRYxFFFfOPmtUeVUIWMbaKnP47XQdZJZuu7c_6N0DIUBOWt0v0CemHBxgrv0-qTGihvlEyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LdIpRjdIVvQm5VImt27wlszOg6xsi6PUUfG0HuMjV5XzP1VO6rtCbR7DlgTbX9ma-ATw9MumYkJi1fB4O_rNEvO-np42OsWJew874wjjA6WoJwGI2uS_DRr0esjof7kg_eol02LbWqIu8qSA4NQDQ0ydJODgcBy37EeWl3to0n2_H3jDrb85FAukLTP9t4ks4fHlV612RUydZManalD2q3M65xVDPZ2570IG6Wd2LmOoPJTgMB8OXTd08Hfeh3PCW2Nvzfdnb7RrSaP4RvrqF_vfHKlzdOr8wgTxIFeBRaOqgqf7UYMTJ9dMR06bAp0NsNisPsusqPqt-uHIWN13sQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsKEeGWA9M-NCWXyf9n7HYZ1xBVR0bGWIEX1qd0PklxZniW8fduZiBSNP2uyn-hG1VcG_3g-K5JKG-qUg1uelHZA1Uu9go8BLmNX1KiKNRd5RhwDveCQ8sDIowdAmvhD4iBtrmcdVauUEurFRcXWDFkMA5hjkn6EQoageElwKOmUr4mAaSvEJi0Wd4vanoB1rr70jo3-qM16faBnjKEtOHcG_rWCbmxDgVrfrkl4hA26gDP_U7l90XkmdyJ6fHHxL8RZKYJGFeoRiJHB5Jq0GtYhsUBRKcr8HRKhkyD4Os1r3eBTlvIxunpiQRGhMv6pfjnaXb69TooY0AltfaTH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dBV0BQAO63lao4QD_QIoW8A7GY5AetsY1KUqx5wISOIcJMmRG75IwZDhKt9PRC92AjiZCvCIL07sH1h787oNaRkevPfphHdcgEP_OmhWJQ4PdgYlQFlLaQXEMdIrOCBK9a0uJDBZU4HJ9bInLLFD1VC-vK_ibQ8m13URnF76LhPx_ObF1lB-E5_z5dCrsWtCkHCiGMsOS8EF7scuUsORec5gKlNoK9twQhgQkmw019g0tPO3PxPWu_wix3aJQWsPJ3vlsvwXSu810qDN5psstHmqea0jjp77jU3o_5F4UjJC14-Pp3yTgJf7witfM15DgSlHSTlqSoLGO82W00wteg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJWMd1HB7WQGeuzcCEAu9AtAuTVCbz45jAxV3mq2p6MSxD3_J_JszxbsuQaZVNuO-EkIuuMLkKins7k7AAz0SIHdWedhVWmVRNTOTO3hBJozKgbr1Uv4cl6vPlytpyLpQSVrjC5WfcAJk65a_27X7jaTz6E8qs16_WrazqX4rDUtqUE3ohNvKwVT8AR-3oe14qYHG5U68EEUvTwXHVA5fq5qKfq733jqTD2GON6bOpzDzGRMl8Ii5BHPCH5jPGYDHnvmmPXQ03N4b7nlrcRZx3a3lNS-om3KnQqQ-hhJABtyMQOfhUw0-i8_GpiZ3AP_GX_wyQN2PGZimuC1yQ4Exg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=J5sgIM_iqfeWcemSz_XK76XscqMCDscNFDAxRikhZ4v_68uddrwh5VSROk2AuvJoVNRSAPZ9pnmSBFfwtk5rlApu7vILon5PoNSR-AW0h6GiNHavWoN-pNQ9DQBBWJI-6xkPCUci4n6PdEya-Kyw6LDmZEr13uzsnfgzMjGnKbKy2JX6Y8aUBafVPF9yBoboDg6iOVW8xCpPl50Rbsr2iQk6VnS16rMJyuskLpjRoMHTLOsrYsc99eYILPtBPjKEg04FCzNuMFm7sk0EOdkQYlaUUbngP1hgjFi7u9D0vHtexZwRNMpb45IuTy27c0FtPhvVFybGv7Xeu1lGnP0Sng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=J5sgIM_iqfeWcemSz_XK76XscqMCDscNFDAxRikhZ4v_68uddrwh5VSROk2AuvJoVNRSAPZ9pnmSBFfwtk5rlApu7vILon5PoNSR-AW0h6GiNHavWoN-pNQ9DQBBWJI-6xkPCUci4n6PdEya-Kyw6LDmZEr13uzsnfgzMjGnKbKy2JX6Y8aUBafVPF9yBoboDg6iOVW8xCpPl50Rbsr2iQk6VnS16rMJyuskLpjRoMHTLOsrYsc99eYILPtBPjKEg04FCzNuMFm7sk0EOdkQYlaUUbngP1hgjFi7u9D0vHtexZwRNMpb45IuTy27c0FtPhvVFybGv7Xeu1lGnP0Sng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qujdyHDxyYaGawl26oV2dOR-odhk2uDYjJqmMQc1cuVsvaq3U60pvFOYHDzPaiqubmGUK8e5gmy3B5KpgkpGfZ7UMxWNr5S-5rwU3mGFNOY1GsGLIrH_GIMRGTi_9QiYX_0DK3NEg_ymnCEz8PcuYM65QFR8IeWSv4ml0u1C3IobdT5iYCVg5J_dB7d7UJiip5H4iQMuIZwhXkhYhf6uYHMz3NVLtuO1VfDY2cstw06bArXHGZOFXnO5P2xc5-O_PHM6w6qpeaRBpk8lH5YrSccSdqxSr8UCf8YA1SkuLKB7uZuQ6z_B3mghbq54exhusgdlEgBYwSMjKZWsF1DIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2V-XTYsQP6Yp2mdiJr-1npZPaklP01wEGl8ZLdKN4T5eFZBKOVwn4oDF_bghL73nh-WXwdxblmTjBTO0WkIsXnBN-g78RcB3fcmO5YPI8ILjRqJqInAcw2oXg7d_OMOj3ZkiebcQzMHqjSOMof7GnRDBmPznSpzA1bapEA_F6_Y4RHAz2yfjEdalqvBfCll1MUrIYfShb-AFQlMenNHxsZYQ_HUuYIKdI-GWGp5hAnqwZc8XvnzYf2rvX-W6GQMKCMrXEhl0PdXuQkLloWq3bzeJzGD2g9DJc5ufRMrNPJYOBfK3cFypaF3zwzmHydz0J7vX0xv12WzMIDamyvzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQNNfRua12RwrP1KmNSXWLkKuruRndOJG9zn6ZLdAx8gPLj0hhBXIzE9-sBpCRr7Hl5wZV96vMZUFGx3yKZRZUuenwp2FaBFPhaqX-SXZ7Uh5DkOy_ZByJg7M8_uhNcv2y2L-SvgRxSx7mRSHenSM-JM8XX9T40gXhweCJgi31nEhzT4glWPFyRHoDBiUvqwXbNy9eQBnHf0guBQmyW4O7sAEk0Z24u_Kx0BtAlFx4A4cqrVnGkhDd1ZtsCxs5MiGj5Fj_JDA5--cY-VaYbt_71b4ghYQGFyZ5bzKSbBlHI0B3LLqieeXShoEqj-jZpMdWnwluy3rEP07Oe8BwBYcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=Nd0xYkbL1du_zOz2Iu71MtZKCuCny82XVKxrBPglNwVSboztZArCeB8QqhPS-jzFt7ejV7Za_ivGprLyTWCyu3UQ4Hw2BwKLZmOzfAHSMqv9M-YdZxcrDXX47JZzkh4a4b9RPS15lx_ALdvzLP2fHqk4BFHFBl0a4p98RhKOgKKPR2SKKFFL-3pHRJwo0YlcjRtju8bpa7HiRXJAJvJbA-jFauo1s_QZEmojpQTWAqByLC_AtKH61fzPjbnHIOjgbbhRIhO7ndylqTqDYRAj4j4dR0e3oBfwpLU3AKA8jwSWZW7lDOFZYXvXBgdXaUEH2DWC40aJEJ3LxZC6dsjLiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=Nd0xYkbL1du_zOz2Iu71MtZKCuCny82XVKxrBPglNwVSboztZArCeB8QqhPS-jzFt7ejV7Za_ivGprLyTWCyu3UQ4Hw2BwKLZmOzfAHSMqv9M-YdZxcrDXX47JZzkh4a4b9RPS15lx_ALdvzLP2fHqk4BFHFBl0a4p98RhKOgKKPR2SKKFFL-3pHRJwo0YlcjRtju8bpa7HiRXJAJvJbA-jFauo1s_QZEmojpQTWAqByLC_AtKH61fzPjbnHIOjgbbhRIhO7ndylqTqDYRAj4j4dR0e3oBfwpLU3AKA8jwSWZW7lDOFZYXvXBgdXaUEH2DWC40aJEJ3LxZC6dsjLiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6FxZ25tTAM9BUhLjigLuhtfP-FiTg7xwg7_q5cwmgA3w2bg22axuHXFf_DYAh0Kl0wBf8BOKvhmBMX-9M2p0fGLd3JSC9hWqxm9m_GqphKkaaQ59L4n_b9Rw44UEchUkUTbvd7cMdL-lrvdM8iOvOJBGweUu2YTp_xlSeCgbPDfYX2NWaeWdmH33CHnP9vsr9VYGN8j6GWLZEyd7xDVRi2ugV_W8w2wVkbRj8VS5cqDfCw5gOPg4tNkzZ5ekCjWnvol_IPypIhn8N8SDmg5O9IdaATYMBodXfi8TgPYJoBioRdJwCPmDISafyDZdYK7nsnQ_BASkYe-xLUmfJbCGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=QUSoTixZYqK_UCoc-xFTilz55O1AVjFc7GT97kdECJXmmR4ZowZl-Ui9yqKGpMmcdtd1v5Zo-21Z9J2gc-qQL47tqtfBpNcq_-yHf3ar4GHxSztVTEvY06kgPIrdh9iA-b8ACr1DJf6d9NuwZ5dz1xuAKwUr9BWasdJLp_8nvAai-REuXp0VYgPHooff9PcJlwYE3VIhI24yTcKvKKGGH0BEyheSNou3450eCW0VP_RmudrZ4Cn1LvZ5k7AteX79X4-klYNBrArsvRQpFZacXZuyiLXK3XQWzOt4eagHLJSXwxBs5knHjFMUfT_gTaH3sNHbHTgoJi72brfpku1Q_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=QUSoTixZYqK_UCoc-xFTilz55O1AVjFc7GT97kdECJXmmR4ZowZl-Ui9yqKGpMmcdtd1v5Zo-21Z9J2gc-qQL47tqtfBpNcq_-yHf3ar4GHxSztVTEvY06kgPIrdh9iA-b8ACr1DJf6d9NuwZ5dz1xuAKwUr9BWasdJLp_8nvAai-REuXp0VYgPHooff9PcJlwYE3VIhI24yTcKvKKGGH0BEyheSNou3450eCW0VP_RmudrZ4Cn1LvZ5k7AteX79X4-klYNBrArsvRQpFZacXZuyiLXK3XQWzOt4eagHLJSXwxBs5knHjFMUfT_gTaH3sNHbHTgoJi72brfpku1Q_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWrLANhQYDPeKbTsJm_IOzFMFySoRxf5vY9gfh0eusEKC0w5T4DIQ0ux-vRxIEeE46F3OxzvvfHTxj2v61uYuUng08QNeW7IR2P2yoKSVNGek5pJu-d9IRwoHnLVH67HcnOOZBGltOUWVK3i7N_XmBdHurarbc9JSMoNFCTrbjWKzuUkQfLNN6sg4qhLNzBZIZXg-IJBHq1hEPjCeBZ_6pI9YF85-u8PZW9tM28ss2jwXCJ7y0NDu7wg3fgkvBa74HDG2FO7Eo_RvUM1OrUGQrjGLnmdqmsyKv_bd184Df_CfKw-lEjr_XSOi6FoJvtBguKjDEb66_9utbblWjtmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbF0vkRdI3W50PDoBke1U0AN2adhPkA7Pl1CblPjiU6sOHHqEfwW3gdlRZbeLqwUE8sMlaqFlGRZ2v3zXw_hFtZiT9xxwots9MRBt2Dn9G8B66jsgJ30pAgryOiQTbZm6YEZvzONqAwWuESVbdWNKKabBjZYmGxAVwBToDKdQM0ZxVDqqBbaMZ-NS8s53M-31LsgnfWGtJEiQT_EO05JWTRqGwQQqpdu0MCcCree27roVENniJzDI8I6LGM0cqKgrZWLf87ZwZNj8IzWLhSvreWhUvq_qfdKlydD9l-xjKKysdpgBtuYjmrDrsASJtg_LnzuCIJgXVfxUD9edpvW9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=b-rZnAqxiwirkEuFo9BekcdkQXWi_onAPxMXOF4m8Jg9EgXtjS9l9YOpV_ZZbCHfwBuCDhHQEBYppEdg2w5pd5Sx6Y4ryiUUfwq9cbb43SuN9AS5Cr5OtGOscd-936Tm7pAbew_Gnk_crZ5MmzH0J94PjN6vdYuwj2U8FC9dVefm-DOUgXjrlH0tnW0KPuKTP-Pp9yGyt5T4jF1_uvpyAo6hpfAMuE7wcSzOvYXT5aXtIp_tBU1IfXjpiUeRmjz5z8HhMPKU1K2y_rHJz1gPUXCUCtpRqLDD27KQG8I4JLvrOg4kylx-1TJb1FnZFZexjLZytpLjqkNmXNEDctDzmm-WyyXzwLI8IrzTR2MXZ7FMRp-oa6nJurAaNzhQWrqLd1pj8SoH0OgcA3UXXsQoRHlKHeigkXWGIKMT1LrJGGKxfZm-bpbKQQx0FZ9kF8bw0pi39eWUpJUx_DkMSNcFqVrK9gIHOY9Aof6Cf2VhaKMawgepie1WhRi_JIT5wvd7Trrq7a2mkTCeCKWLeEbMLW-WzKY2K5BvfwwHQfa-_SMdr8KmdDM53rMbMjNyGgYpDnFCmP1iMgqXQYCyn5nN5l0vBOCuKHgHiwBsd3h1_FpEAiZ4cldnRzq05-htMAQMz61Rt2HlfAM2rOhK_to5tydc-A_hTVXcxT_EzgeunJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=b-rZnAqxiwirkEuFo9BekcdkQXWi_onAPxMXOF4m8Jg9EgXtjS9l9YOpV_ZZbCHfwBuCDhHQEBYppEdg2w5pd5Sx6Y4ryiUUfwq9cbb43SuN9AS5Cr5OtGOscd-936Tm7pAbew_Gnk_crZ5MmzH0J94PjN6vdYuwj2U8FC9dVefm-DOUgXjrlH0tnW0KPuKTP-Pp9yGyt5T4jF1_uvpyAo6hpfAMuE7wcSzOvYXT5aXtIp_tBU1IfXjpiUeRmjz5z8HhMPKU1K2y_rHJz1gPUXCUCtpRqLDD27KQG8I4JLvrOg4kylx-1TJb1FnZFZexjLZytpLjqkNmXNEDctDzmm-WyyXzwLI8IrzTR2MXZ7FMRp-oa6nJurAaNzhQWrqLd1pj8SoH0OgcA3UXXsQoRHlKHeigkXWGIKMT1LrJGGKxfZm-bpbKQQx0FZ9kF8bw0pi39eWUpJUx_DkMSNcFqVrK9gIHOY9Aof6Cf2VhaKMawgepie1WhRi_JIT5wvd7Trrq7a2mkTCeCKWLeEbMLW-WzKY2K5BvfwwHQfa-_SMdr8KmdDM53rMbMjNyGgYpDnFCmP1iMgqXQYCyn5nN5l0vBOCuKHgHiwBsd3h1_FpEAiZ4cldnRzq05-htMAQMz61Rt2HlfAM2rOhK_to5tydc-A_hTVXcxT_EzgeunJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Qv-tLhGZ7esI0F3fIKmn0pFpXbixNWJhsls3Glzhx27weGgZKM7k8E1qITVHWH3lJ5YqeQBD0cOZPzZvMI6RWXyHI_Crof1pU6NwRuwVw0pOXdO5ZZT5fv2NDXC7_qzFnh4c9CO78KN5SnYVfywHsCTCBdUaBeBttfeVjAhGhTa4sP8wDZOpwP46mZCM_fkTQ8VvADLoW__MbO7FhoN4NlhZ4oN_8VKmv9kFnvJtRul5wxOaq0UYKt-OsH1XBCNzq1uQgoM2_3xIOMasfZlFiP9cdsN-9W-t7HKgjieI3_mQmMnPDmyRHQoRCXhyS4L-THDAewo20LRzQmos9qZh9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Qv-tLhGZ7esI0F3fIKmn0pFpXbixNWJhsls3Glzhx27weGgZKM7k8E1qITVHWH3lJ5YqeQBD0cOZPzZvMI6RWXyHI_Crof1pU6NwRuwVw0pOXdO5ZZT5fv2NDXC7_qzFnh4c9CO78KN5SnYVfywHsCTCBdUaBeBttfeVjAhGhTa4sP8wDZOpwP46mZCM_fkTQ8VvADLoW__MbO7FhoN4NlhZ4oN_8VKmv9kFnvJtRul5wxOaq0UYKt-OsH1XBCNzq1uQgoM2_3xIOMasfZlFiP9cdsN-9W-t7HKgjieI3_mQmMnPDmyRHQoRCXhyS4L-THDAewo20LRzQmos9qZh9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nt6At83aTko-4prf3Bh3ujQs2OqmJSA_cMkLLSWkel_QbT1aZjykEHHecV-zUzZXeRZsPmmGSKR5gVZYTSJzOv9KObWSkcA4l5Bx1BnwBnYRth6i1H8xyohUsXAX0A6t6tSD9d4xH16UM_jwG08qeuw2KznG0BvSBO3-H56cAKgnqeW70E8eSdulGT8SEcDiYP0kfFF6xCsRI4nu-lzrasiJP5ljcbgC1a_G9_05JotfrT3uwEIQBRBZQ3WfSf_CLUw0iHuHfaAeoS1wvTY-j-lI8WrL36R1fgCRl-OeIS9NAskVXq5CLQvgeBWGC9JBd88wHoUMtimMb1VdXhWqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=diHHAJcv9ichMOg-euL46--wl1ezad2rkrJXSED-rZVCzIjDv8oRhmld-dAnUL0KgRJA2Gx9d5s77E8pY44uNzm8L4h1d-UmJSgiuwEalcAnSM5FsCC_d_MRS8JLA-l3Oc3WbY2YFle9oF5hLW2XRpLnVZLC3i7Y5JfsB695D19RPznci30wa4Xfh-TFywag7MrfDPPnuCAmTr4yIixhQIBivi7W6hNILJiVFEqVj2Xt6K2wNJDcO-X6m-4a8NfOu3plBs4Cb9W6vKjDd5rY0c97sYvQcKJ-cQdRo9R_9aAQFRSu4ms2MKr65AJ2ztJxQnq29noZU-fa9LdrruutpjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=diHHAJcv9ichMOg-euL46--wl1ezad2rkrJXSED-rZVCzIjDv8oRhmld-dAnUL0KgRJA2Gx9d5s77E8pY44uNzm8L4h1d-UmJSgiuwEalcAnSM5FsCC_d_MRS8JLA-l3Oc3WbY2YFle9oF5hLW2XRpLnVZLC3i7Y5JfsB695D19RPznci30wa4Xfh-TFywag7MrfDPPnuCAmTr4yIixhQIBivi7W6hNILJiVFEqVj2Xt6K2wNJDcO-X6m-4a8NfOu3plBs4Cb9W6vKjDd5rY0c97sYvQcKJ-cQdRo9R_9aAQFRSu4ms2MKr65AJ2ztJxQnq29noZU-fa9LdrruutpjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLQkekBIZxy3I0fvKK1dq7ov_O_vdHvapYKszPhH3GAX1tuef0pP4b0MCf4NqQYOPmZhOfThiyOPYQvfoGd0WjAePZMl1q-MmOjCGgdy4rkX4aEF3D2MUikjfD5bxN-CSrG2flLEEwPWJAF1zi6RdjdGU6tcX1dwdOvtqDRRFyYw4fOz70KYg_jODRZhXOjbCvLRwGTpxQ8qUQ1URpQMnwDC1tH4T6yNdtX5BejNpGmEXixrZJsC_JCxwJW7cxUNo-4vUvbKEXizWiaNZcteoMtC9Y9AbakeUSNBR5uAA1qOTghuLch0EENuAREpYkeZNxKRZmaDluA-CRrzjAqarg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZR3jr_fQGpolUC3d7qyutLQsMUm3QTyEthsW7QRFKlNcsc0ME8yM82vCDNcLM6Pp0pql-YsK4bXCVe_h_6yH65ICnCZdoTOpEwSJ9fUcsH66XOAT0R_KvHKtmpj1cdgpSR1s7z73mjUvj0OJf1mbdIrW-0H4rV_6NW0eC42ghYo-2vWp1W9MYdXOzfmvgJyNdlxy5zQxcwFUGg3T_vH5SaKPGMnew3V-NHotaj_M-7z1eprU4SjZ12PQYPndnwRVUYrllT__BHe8FH4TuTPqod9QpRp2OOLO-CiipgvzxXlcTI2raJG27F3g4CWiZpO5Kydg1GcxAUQ0_MPE1mxPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoHEiSl6JqdK6qLgi1UXJY4F8OIJZRlNnwsx3DsehwHrSGBV-8pGhL6jqL10JfpP0gZzkwutpJ1kcaR87T7FmyFuGBsn2O1pM6JEkmQLtlKObXFqT6k7-Lp6hRNPZTyHihbGqvxTPCt7cZrJfaQpOdfEyAB3OVfiw2N7dgqBwF2m0SDtehjJEAdGqCv4tremsg5xwu4oM2yHrgj8IxBwAfxBbTrFCo7ybJkG9iJEdoTUGnzO-YPsLRX6ekYfjVDGOuirivtEDGUKmhAEnAgizQo5jYNa9npKfZ1ho9-s0xz0MCXCff-9CHAdKwFxy-dRpLF9ZGLpVUOflXmM5ukHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6NkUam4c12uicl4kqQLFqOtNgFixmzHCYKkpxayKn2RHHdKZxXQKYj1iSQM7h9P-Ram_qSGXTnlsw6juH5HJGUytyzxmX71cdCStKfmfzs3wBDKBp0HsaKopwl46f8-OnKcjKaSNfATOOGR_l-aK90RVP3X8x_kC386aW6XfM9PJVAQrTuxMrgvzjh_CNATnT3Bgk00lsYcP-gMFEv7PQTIcznBlas0kfSfRcSNjsirP2DaNrT6NrlwOQXBiQq7PT9iC6ETMqgtTWBWKeDBCcbFAgkKCC_pXHXDtMZi9XCt3rnsWsmFJUPX0tomJnm5ahWpNH6ONXSSh8sMNIHmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHpqawGDFlMCIfBRZFU_N-0u6sgNhNYppTPrWhluJaaRLhZYC2SkjX8slLVCUBP4B-89v-ABXpeATa51RHyzBcsQa7hkvO43bQ3UyPbgtldwSkAQOUoAlhSYktvbnxRoPHfCqplVndqBKlMb2GELO80jDq9QAQncuAYjrSCEdDiqGPQnJeoo7tMurg4YPshe-4rDo6Klic65TzisaChm1OsuzCcy5RcoAPwYIgperXbzFzOqk8hx1FV4VZpVibRJMF-8TbguvelBYMKwNAVQ7hIn_uyMab4yETgraxW_a9RbSe0Y9heigi8nytdQxQ1NRb6I1X9hzfcLnsxK9dK_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=lmj8gCSbOA6UeYCvuPB24Ld_zSR1V683kCeWVJkq0a_D3iiejKt8wfYqt8Abi9NhELELn12vJS1ulQXblz9i64ED-0qdI5MqdBffKCFvYMHAhglsOhXpbgzR_uU6oWMr73cP-3D6ylI6-Wle-GGnXKvwBFh4IHonc9sB20ELpDz_ZaG0YXUMmQ9PhedfM8T20LDi7DYLfH91gZGXyFdkMYfe1xgIEy1kgKu0aco6DgYXF1uD2XsczGK1ckt7qluddrk99E_N4Spv10d-jDnPMZ_aMTkFItGs6Cd4edAn56U_t-QJKPk58l6KOCo6j732gw61ybyMxMWEL5PSTC68ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=lmj8gCSbOA6UeYCvuPB24Ld_zSR1V683kCeWVJkq0a_D3iiejKt8wfYqt8Abi9NhELELn12vJS1ulQXblz9i64ED-0qdI5MqdBffKCFvYMHAhglsOhXpbgzR_uU6oWMr73cP-3D6ylI6-Wle-GGnXKvwBFh4IHonc9sB20ELpDz_ZaG0YXUMmQ9PhedfM8T20LDi7DYLfH91gZGXyFdkMYfe1xgIEy1kgKu0aco6DgYXF1uD2XsczGK1ckt7qluddrk99E_N4Spv10d-jDnPMZ_aMTkFItGs6Cd4edAn56U_t-QJKPk58l6KOCo6j732gw61ybyMxMWEL5PSTC68ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIgf873oGABR5xm3sNIHX39P3j0iJqQwK9aGcn0CyyZM94Ld74Cv8jt7luuj6s9kz4FJAqnaDNLlGADGCUB2LLM2TaJcik2hNEFKQjP9fXTycdzI8ntVy3TbCpph3r1j-f010K3THuaWaAeS8XrOrRXwQD_ky9cW4G7fcXkKXrOkeH5HXzEkl8mXZ8Se8NOSozTcg1B2q7gLz-eJBZdofnkWhJyZAEaK24UVCIxQ5KtRQJy8ynARvqqMbIbturkjS3uGHUUoCluZ-HG2odUL6DgOwdp6MiegrxDuI38cGj_fGx2w4CplnE1RIa2hErvWXHNfZCbJltzhhDP0iVdUcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULZdisgJSidk3eUjreahpcwB4HG3PMz10E17D_FTdcGsCc8AnjA0t2edj9nIR3jcy_5K4cVsAB5qmTEOjmOekB_SzfZy1gi2pr_b1g_kV4ptoOabg3xuFywl37rMIEyY1xFWWT3FpRx5LR1ATePnUEyFF9NU7EiKZiZIAbZSIoZu4n8eZB-9oFoQY50YSiq1xj-6nG4bYjC1A5AZnKwtfSOcee9UHFSAcI-5D_0dBSxaD-9bNUgeAyTGTwpy3MdsIMzjxte2Q9p99d5CP3LhsFv9QR8LsM6CyjtFxDP0Se0TRT4I8Vheigxc0eF0afve9zA8nE1jXpjUfJn04-u8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=rqD8TRGXjvPUeuneWxPRP_AQ2GLd-YH4HMzi_8jsWHlupCM-l6EbLLbeoDw_gWIbc7k8SPKxl_Sw6vlZlIjaR-h0thKi2S78uNToxXXGD1JM1VmIUj0fTDO8nJuHSLdGlqeXTgr10yHBy1bfdjoDDoehsdAICBS3brMiy694SeHff7FHvGxpRQj7lvjNWfJLPFmbHu9Lxq90IXCnqrm_uUIv0vcZ08xV96G6wLqTbU0CPpjrmCLh-HVGJRttORN-IGp2CqWZcLSh37OynvA1Is3SdyM4xFjDaMMyUZ6CELsXf5E_SGhMOdBtZ7-XPGPEKIVUR3tFkkVsxqTU6mIZhmz9TwqGERKmHidq_eROwnA_q7vjlGCoRjkQJPbVJOdScvVfhRj6Rf8Q8rFU6baWXTz8jO5sux4jGkTsix952tkdPp1ySMSjFUUNY54moMZf64QnFlA8fdNVxli11jCMRRcpO9y5I9Z7lt91IArhZXBpLRlkjI0nWtTESkEtQLr-TEPp6WdelRo3uM1Ja7n30fUd0R-Ib_JJr6W7kiCRqWruJzFD804_lHBfxO1IFuA210W4tBBGpD0e1xxr12kM_zyUZqcfoBQatwb-J-xgOeh4GhQBQMjn335AQYud9B4if8-r9x6p5RNDlngOnG4omrtFl75xvps72QrtGdc89sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=rqD8TRGXjvPUeuneWxPRP_AQ2GLd-YH4HMzi_8jsWHlupCM-l6EbLLbeoDw_gWIbc7k8SPKxl_Sw6vlZlIjaR-h0thKi2S78uNToxXXGD1JM1VmIUj0fTDO8nJuHSLdGlqeXTgr10yHBy1bfdjoDDoehsdAICBS3brMiy694SeHff7FHvGxpRQj7lvjNWfJLPFmbHu9Lxq90IXCnqrm_uUIv0vcZ08xV96G6wLqTbU0CPpjrmCLh-HVGJRttORN-IGp2CqWZcLSh37OynvA1Is3SdyM4xFjDaMMyUZ6CELsXf5E_SGhMOdBtZ7-XPGPEKIVUR3tFkkVsxqTU6mIZhmz9TwqGERKmHidq_eROwnA_q7vjlGCoRjkQJPbVJOdScvVfhRj6Rf8Q8rFU6baWXTz8jO5sux4jGkTsix952tkdPp1ySMSjFUUNY54moMZf64QnFlA8fdNVxli11jCMRRcpO9y5I9Z7lt91IArhZXBpLRlkjI0nWtTESkEtQLr-TEPp6WdelRo3uM1Ja7n30fUd0R-Ib_JJr6W7kiCRqWruJzFD804_lHBfxO1IFuA210W4tBBGpD0e1xxr12kM_zyUZqcfoBQatwb-J-xgOeh4GhQBQMjn335AQYud9B4if8-r9x6p5RNDlngOnG4omrtFl75xvps72QrtGdc89sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
