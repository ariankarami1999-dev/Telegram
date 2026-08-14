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
<img src="https://cdn4.telesco.pe/file/dp49eiLJMFpgbyo1QJnCPOCdYSnHWDV-zu07svBQh9B3nghO1vZsMqTtTSfrSXJBGdSdkMZTbQYelBVwQJA90Jz4NCvHSmDxTc9QUjHYjqqc-zUmLRJji-qZXgCsYFeKdh9ZTzMe0zmyaKmVt36O9QV0s8wuN5-jNlmN5jka4uD3B8nE6VCoAzFFCvGrOmDGiQwziPKK6Ru5HApk_bSQr5RSNP3swIb4ianoxFcMJ_FQcK_pYpnW_BU0UTYovixYB8EbrCMG5fK0RDnvaiK7Pr0KjMlGFclaMM2uXHtC3ofQ-PzANIgYi_-MIUtS0pjBEf8DFeN7cvglNYKVMP4fow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.78M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 03:14:02</div>
<hr>

<div class="tg-post" id="msg-456139">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53c76d02b.mp4?token=MGLUThPrEzzQFd-6vFI5FP_TJfWXzK8XPaEqIAgbt-Aq_jkcK463T0-6UsWTxH4BeBdKueuN_jOrldTTmD5dFVcMva6dCpewNVRV-PZKZCs6HQk2hHjiMIXOqB0Zetome-DCUBNlLO0yS9Pu8_lprq3suMWIjQsi11Y_L9Ccu5wYCi8qwtelH213l8YTbmrwoRSvkiiEVIqfpUL2elVxhzh8Se7PrFO0Hiv20WJo21R-j8hJKIaCDEw6249De4Aom_DG8X1XusXvALLjEuiP1PbmWfImUBN7-Z0_GEEfhz9At4j3RkwthjA-WEJnK4U5AiPZZkmU0PuygSgE90nDTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53c76d02b.mp4?token=MGLUThPrEzzQFd-6vFI5FP_TJfWXzK8XPaEqIAgbt-Aq_jkcK463T0-6UsWTxH4BeBdKueuN_jOrldTTmD5dFVcMva6dCpewNVRV-PZKZCs6HQk2hHjiMIXOqB0Zetome-DCUBNlLO0yS9Pu8_lprq3suMWIjQsi11Y_L9Ccu5wYCi8qwtelH213l8YTbmrwoRSvkiiEVIqfpUL2elVxhzh8Se7PrFO0Hiv20WJo21R-j8hJKIaCDEw6249De4Aom_DG8X1XusXvALLjEuiP1PbmWfImUBN7-Z0_GEEfhz9At4j3RkwthjA-WEJnK4U5AiPZZkmU0PuygSgE90nDTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلزلۀ ۷.۷ ریشتری در اندونزی
🔹
مرکز لرزه‌نگاری اروپا-مدیترانه از زمین‌لرزه‌ای به بزرگی ۷.۷ ریشتر در اندونزی خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/farsna/456139" target="_blank">📅 02:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456138">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امارات: یک کشتی ما هنگام عبور از تنگۀ هرمز هدف قرار گرفت
🔹
منابع خبری اماراتی به نقل از شرکت ادنوک این کشور، از هدف قرار گرفتن یک کشتی در تنگۀ هرمز خبر دادند.
🔸
سازمان عملیات دریایی انگلیس روز جمعه از دریافت گزارش‌هایی دربارۀ حادثۀ امنیتی برای یک نفتکش در نزدیکی سواحل عمان خبر داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/farsna/456138" target="_blank">📅 02:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456137">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">زلزلۀ ۷.۷ ریشتری در اندونزی
🔹
مرکز لرزه‌نگاری اروپا-مدیترانه از زمین‌لرزه‌ای به بزرگی ۷.۷ ریشتر در اندونزی خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farsna/456137" target="_blank">📅 02:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456136">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f0b14a1d.mp4?token=R2TyyJ3I8GOrDoW_CLMfBu3LId9mptS_5mfKkMHGNHgyd-njOD9AD_MHVulmlfOVe5PpIQ8hPlTSDWx5GPJBdCMmmCPXESQsXRtUVl-rXe6o9o54F8ecvy0bomURk7A3ZxWnG2iH7XX8hihA9CeZCj2z0mJwOMuW2O6PTl6xhKsViimWiFXFDmpjrfaXsns3XWBtiXYLesau5p8ta_5Dc3Zz1ydff8r6BcLLQYYZPj7z6MmlFbaFC36GUsXayhVb6YZ5eoK-O5yR4mhrHrZKKraJRLueDSpqMb4RmVmpzESyiGZOR6xtMPHwlaY5Tva58wDtqPlTTFxRqwQmzQnVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f0b14a1d.mp4?token=R2TyyJ3I8GOrDoW_CLMfBu3LId9mptS_5mfKkMHGNHgyd-njOD9AD_MHVulmlfOVe5PpIQ8hPlTSDWx5GPJBdCMmmCPXESQsXRtUVl-rXe6o9o54F8ecvy0bomURk7A3ZxWnG2iH7XX8hihA9CeZCj2z0mJwOMuW2O6PTl6xhKsViimWiFXFDmpjrfaXsns3XWBtiXYLesau5p8ta_5Dc3Zz1ydff8r6BcLLQYYZPj7z6MmlFbaFC36GUsXayhVb6YZ5eoK-O5yR4mhrHrZKKraJRLueDSpqMb4RmVmpzESyiGZOR6xtMPHwlaY5Tva58wDtqPlTTFxRqwQmzQnVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا دریای خزر برای ایران مهم است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/456136" target="_blank">📅 01:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456135">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOIXt_Mx4YRiYOmxejMX5kRUWCSvyl8Rq9G5cvZgiFRbrfAUbnouMVqpSg_aCueR8zWQrQI5u1q6CaufjwczJK2CBIBh7WBSDSZopT-bKJK43jugT6ZMX2LMBanipzMm-qdVyRPwx5SAbPw2-QUkC7ymqfxgpdkPDa0AnxNcM3rUcTkBgvufIT1krw_edhHNyxAv9cC-e5ZPWV3oR2VyLivU674ZEImKZQnpXdIXhrf3q7ipMoZO9HraMkRmsb0FLeYgxH1UGJi1z9HAwWPrPqE3BZ5c4ptDzc3aTe1Or79A4INqrfU-LxcIgd_Uj_PL6JDlhdmlXe2sNj6Wodt6FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو خسته و بحران‌زدۀ آمریکا به خانه بازمی‌گردد
🔹
پس از ماه‌ها بحران در ناو هواپیمابر آبراهام لینلکن، وزارت نیروی دریایی آمریکا اعلام کرد این ناو ماموریتش به اتمام رسیده و به‌زودی به خانه بازمی‌گردد.
🔸
اعلام پایان ماموریت آبراهام لینکلن درحالیست که همین چند ساعت پیش ترامپ گفته بود، ماموریت این ناو طولانی نشده و بحران در آن را رد کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/456135" target="_blank">📅 01:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456134">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">منابع خبری از بمباران شهر رفح در جنوب، و حمله به یک اردوگاه آوارگان در مرکز نوار غزه توسط ارتش رژیم صهیونیستی گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/456134" target="_blank">📅 01:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456133">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eb9745744.mp4?token=gaclicWAfeptSMLTt12K6zC29icSf_Go_ALadH4mMXxk2A2p4JDx-Kmwtd53SUfCWqrqgEq_IUltWfzs90If8921eGBy8lB9a6Mc7rrOBJ5_RvJQ2rrPDTGNgCbUHs9Mp50bFfgzTEGIim5LKP7wLjCagLdUdaW6N7JoBT3L71SP9VCVSWR2Et4DKsWoO9wOUyf-m2mFcO0IeeoRmECIKRk6gvDLSYYssrxBENjQe4hfLjMHcE1szNgKoBCO9oJWFf50evJGVUyjshy08dFyim1hv0GT5P6gPeLBb5kKmxiJVw5aBVqHRdcTWqFT-6PiVRjRbm1zfjqG_4L82rk7BWQdtblZNx-wELyXt56Y14E1BpdLQZWbBmXUVMwyhq-fw5GRWEKtu8v8jdqiKlt7R2MLyWnXdtaPfGggMA4c-iXYpUdJy564POs0AwjCuC_Q7OIDTAqXB7K_KZgH4197F4zWl1npeiEfZwsoCVJ-DXT4W2Bd5nMB--9WOpcJvHZKNYfE_NXfwjE0Xe3PqqRRIlxxyymBqtDWWm2n7xfnUIueq4CT34YUbEIC8VAZCoOZuUp-b_OFdwZ21MsvRa8i2fOBRdckiQg6vzg_1G9_QyCAD04WG9_E9ReCrBW96KWFf6YljxeF90YnKEN1MXzJYi6UDk7tPleXMPq8By9dGF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eb9745744.mp4?token=gaclicWAfeptSMLTt12K6zC29icSf_Go_ALadH4mMXxk2A2p4JDx-Kmwtd53SUfCWqrqgEq_IUltWfzs90If8921eGBy8lB9a6Mc7rrOBJ5_RvJQ2rrPDTGNgCbUHs9Mp50bFfgzTEGIim5LKP7wLjCagLdUdaW6N7JoBT3L71SP9VCVSWR2Et4DKsWoO9wOUyf-m2mFcO0IeeoRmECIKRk6gvDLSYYssrxBENjQe4hfLjMHcE1szNgKoBCO9oJWFf50evJGVUyjshy08dFyim1hv0GT5P6gPeLBb5kKmxiJVw5aBVqHRdcTWqFT-6PiVRjRbm1zfjqG_4L82rk7BWQdtblZNx-wELyXt56Y14E1BpdLQZWbBmXUVMwyhq-fw5GRWEKtu8v8jdqiKlt7R2MLyWnXdtaPfGggMA4c-iXYpUdJy564POs0AwjCuC_Q7OIDTAqXB7K_KZgH4197F4zWl1npeiEfZwsoCVJ-DXT4W2Bd5nMB--9WOpcJvHZKNYfE_NXfwjE0Xe3PqqRRIlxxyymBqtDWWm2n7xfnUIueq4CT34YUbEIC8VAZCoOZuUp-b_OFdwZ21MsvRa8i2fOBRdckiQg6vzg_1G9_QyCAD04WG9_E9ReCrBW96KWFf6YljxeF90YnKEN1MXzJYi6UDk7tPleXMPq8By9dGF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور اهوازی‌ها در شب ۱۶۷ حضور در میدانِ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/456133" target="_blank">📅 00:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456132">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترافیک فوق‌سنگین در خروجی‌های مشهد
🔹
رئیس پلیس‌راه خراسان رضوی: با آغاز موج بازگشت زائران، شاهد افزایش قابل‌توجه تردد در محورهای خروجی مشهد از جمله محور مشهد-نیشابور-سبزوار هستیم.
🔹
از رانندگان درخواست می‌شود با توجه به حجم بالای تردد، با سرعت مطمئنه حرکت کرده، فاصله طولی را رعایت و از سبقت‌های غیرضروری خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/456132" target="_blank">📅 00:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456131">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
ترامپ: به‌زودی و پس‌از پایان جنگ، تنگۀ هرمز را «قلمرو آمریکا» اعلام خواهم کرد!
🔸
ترامپ چند ماه پیش هم گفته بود که نام این آبراه «تنگۀ ترامپ» است.  @Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/456131" target="_blank">📅 00:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456126">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sm_wdPkrouOmMn30PtH2ErgLpICsPuU-seZUr-wJti4W4qEmOeSvb31N-bLl6aKsWcfcQzfpBL_0tbTRwnsu4vvNORp16XuaehZat2OaaU2gVRhJ8kdhQZhBCw3jC4_VdsyPxmjXsJUkpPmFzAuMDYiuCeEpcb4TZu4qrE7s2qsROS_vsjZY7Jc05NH8R8GJQOkSMnShY7GiSTuWV_H0KVCc7PIw4VWDCDcG_CskZfhl5Kro637r_lQg3L1KKQ1bjz4Z6Z4ygKZC6xWW8sHIQ7_0agAyJtOh8_TTMZaDuzuJAawb9ot5qNm8HipKHR9rKgELQoRNuWjzYkTdbJb0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCcK2shyCqyvecygIaU5i_rXTZocfvNtPgRZeYLmMISOcGXIYnPn2dKCUmr1hqyib8rKoW19OChKHxIvQt9QIc9O7RYOEO28y5SeWwcru45D-Gv80ghmCmfzzaRWRxGHgqzRagpT7mnQDPlDD7VrqDb8I7BWnx3rkhtWYUudxSeIhzS8yXrX1S0wjkFxXA_wrFCYr6mWN8d0rW1AFd7PhIzrqT57bCcywoK6eLq6Ki_Vj2luhf9a8nrshnBr3Zvje1xWVYyrUJN0U2KcvDuM7K-m9KnZ2--P8vaaqxXht0dGV705t7zzYLYvHs-rG3nXQ87ke4yZLPQHT-VoKJqYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQrBAHs3_ENeNRa9tH7icgP7TwoaV48r2Y5Kbk6reKZR9irVxt7CXtaqgLJ8G-NQxDq5BMos3qdBTLv6Mwyf9hDjF0XDkrLEFIlIReczqGoBYkSY7Pur4Dsumngy3I_n3_f7QgUOq9-XL5nbZZptBsqh9JgKY0dMrD1sCd--i-Zu7K42eTCZV8yTGK4uY5H9vzVM6LT4Bz8BYWR8jUnNtp1gijquxJqIX5QR3T-BE5hLsPBrZmL8_TKG9Wr_HNn3d_2brwRPEIgAWUmFvFGWu_3Aid6GJdT633-i68Mc1yGkS0aZr3M_MGfZ1N8Yd2W8u6G5_8DAfh149zrd2aSx5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmMHeUoKkFPQ1DnaSI6-5e1XA7eAcbJeQzQj67FF2JzbVZyEVkW8XZU3M5RXndEIA6Bpz8cSBXJId9LDv9iDC8cEItPG3pMm2bMXggWG0EDP9XzzOz2p4wcEFRNI7J7-XcDw54MoWZjIJYcbg6Zvx-DQvCTbgGs_4vp4fWNWKFq2jL8tLZWAh8qyj-P1DIclEi3u9M8590QapQFGPasUc0RWtXXWK-am1C4VUjDVSYwoJ24_WzPDYSuee2-d6FNCNZVgP1Z7_GLlXMUeuKMlTzn2bnlHRRs2tm3maM3PfIq194CbK2DGx-pnU_wEgi4dcG9GqLur5qmZ2sU8_aNtew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmwjsL27Aq23GNHz79Ik1XKbG2kGyEYf-G5jnSpNoJvum_kumk79C8Q00bTsp-y40jmKdYlYFzJP-DAdJ083_ZWF3dc8KCUAbaXmd-1KlgNBmurpmkHEGItovjy8kKGbbl-8pNUABOEuEyGOSXc6baO5DGd_Mb-Q55X-wwFrTgaR6Jbjz68GBe500f4M0100_hGXXbMqu278eQYdpDjiW6iIk0jpygkoAyIX0jvCTT7FvFT7Y5WjVaipGRC8pyhsYuOhwrLcS_GlQI-LUPCkr3mI1WDZjy1lZhOrH865W5aRYveVCSev32li-uvZ80X7UidS6ArbGSKB8unWsqb-bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات پرش با اسب در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/456126" target="_blank">📅 00:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456121">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4LsRbkMhDlw42WNHkHf8ufZyBQiseRMlXjf01RINFpKIfO9BdKjCOnBoXavXrlmnmpiIDc0apVwDhKBO65Uxx4V74hXT60tbdiXDQtK16qtH8j2FvNFvt-7Tnrdgrk6kwRYz_4GeKHAs44GvWbrIX-u4K7OllSi36B88WOOJZ0q-hUIlxHm7wxV2CUKrEGMt-m6wZiNF6MGx-pu__Kr0tIYH3TIRVCezK_g2-i-7by71haq7_2myp3RdxAc4wCFo67_WUJ08XJRK3HPYQc-i4ZOK_JI4mOZDpQQ9BhCad9G30uXXcvkUg1AI2WH2IX6zmMyWyPMw4im5AeUCH95hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Avwq9CuKQ7_zq942YNDVZQspUNQTsbl6bRvDc2pFn10LDu9kpnxS-Mf656DQIgEVxqvsnPXSYqq6SFIx2MJM2zarKnWhedIJTMGlS_CPdca1zE62nmTZy7neJj8wrpwMj3_HFV-XGPJD-EwMgxCpua_ADDlrcFxwoMRq86ZemqaSLUpYp4ACS_8q0hVLiQup5nK834rcDKpfkAZWUBhBpp1CVY-bftlbIKRkkvkq8AfLbpdj-3gO1phRQ_zEQN4EwPSFgrW69uWbbiB8wFYx95T6coUuGUNEh39NJc0TyaRSB7IXk4sUiF_NHMx3yNoz1eE4w4oyeqXwNM65Xcg6gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzm1TSRgxkTj1BMtLYeNxdzq3_sMRvOwot9KF0cVnY5TWPmLoig-P1zpwo2c1YvvCFwSz1xf2JTlKt6C_P_Qy_nWOVW6fA88T3qljRy6BNDXhkB3yzPNSmihftbTN0RgAgorgCIE6I9IllVIDRWu7Y0t9lHnzz4tQ3AKb6JGWl9Pdk92FBILIn8u_M-kJ-ebu-R4xRd6KaIdYAhOdYtjbV75YuPUxcGD5_Y2uEKeoH6o_4BLkfZRVua0mmV5PicHRl5aOXwfCgXddbHObF60QdvmpLlQZKBf6p_qnSSY-CtLh2vaqCZocI9-Jc1GIui21hoiI7xmYAXmm_QZ3dV0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrAPyvNzJtn_LKg5hRIab1JvoFYswBQ38sUTtgIhecVJDFWn7a-kZkmUgoCjHHe0M5gWbofrCNLjVLOErPzO9niXlU9vDfhNTNQwj4PSiYHxt2WeIKfyhkRxdlpfrbOXoYGAqmHEyvSdM4kqGitDsyGz4L_wfyGvC8y3HaVx7i96OD7JYP9acMGIOrM_Fd9kTzR5Sa5KN18BLLIHEvES6108T_dorQPzeJqLSMO-4XsHcQ4v4OS2HO01iAOYakiTEdIR60D-eADnE54nci8cpPAtFoe3xR8HBhLMHPMIP-xqAiywJs5WAFUXc_6hSVCX7p0J7mY7qdKZjwpRqlhZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqWJV0rUTFxzSD3JwMhCGr4-MOLRGqOs0Me8jcGTBRJojyeaQNht4xmEvsL4sb_F2bF3xPhnaL5RKVCSaW8Gj2mLKY0IDfA8oXIr2owA-j5l_WmjR8lpArtIScwyqkf6M9gS2wahfNqW0IbJqkcL8EfnhY7mj6MWS61zie0BsYIIFLJcQydX08GC-BlDoyNvUOrkxfT6XEKg0v_4sg3gnkLLA1sqRXIIFWZUcpo8HEcYjvViaMha_Xb5QLQmSVk8JqXvDxSAZFwSty6gHwTQ0DRawhcqAKttYMf3oYQxG1at_IO9MfNPHQpgunC8ehk_x-cK4aYQ58q69MkvjFR3hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲۴ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/456121" target="_blank">📅 00:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456111">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oA1N7Y2nuxvUfQThIJ40ff2VQdKxfxG6VOwTUUe87xsmlTZSfx2z1YFl3JD2TMfAkIQ_AgUHrOsQo6hMvX8UqwUxLAnXVP4kRAyArZy4jPmR8e_s5QFI5MKM0SDWHugRJBd_Vxs-gSOgmxrZozM9EO5SYirLxrbFG5o-epA0oJKQPzxPvmGE0MH0HJILAHpvOEk4KtJv-TtWNPmiteRYzNCylDR6WWo27Lwj7oeZF_zteeYl39vw6nWfQ9vW2cxtxVWxlfBpA4NCFtDaxywyk0SbMTeecQeulKQ2osA_ZIkR0Aia53aCsIH5I_VsEfozEZB-FORquUn6V3_5P4cbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ByWwTtp9h5kzzNffhZUvJ_u1KGnUKbGL8bbJIHCw2ZT_omh6KakXXfuTq9oXfCYObNq_JDD518eF_3aQHzBUtLl1leQP4CoL7tbSGNHJmqdz_k8uOBBXgDk7UV_lEukxZ0fzlASCr0mWaZv9MpDFfnzQWZlZUoc5aTlTXsCOp5nnBaNBosvN4S5TfVb4zli1Zyy0c2yxulBdxxLxYZTe3vw15nXEiUW1aUcxCqbU5yBklkmiOyTuADvBz1my4D25vlKuzMoX7UU7uNUqerRVgl58CsH0alXCjQAaoYvNgaw6pEG3oujKiYPq6hROTOg8eqTYZheTcfonm9BBwDuwYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9LyyzC-58EnifiSFGJZ4OIkgtHNsvxMj9miu-fE952cicLcb_WqEmcWmL5eRBWfwUzKavJFZJ8B2motx9ngt2Cft7RbbUuRFzQ_YG4wSnp1knRqHFfhgwqmzrEQryUmP5EXBjtspgDkEJWjp07dFIYLKloG1QhUIhtxgNKXSCiDhYRpqVHyod6dCgM3SrqNhfPepwXEzz2B9VC1zVXPBizqhTP5LrkXRdhlpCE2gXHsgP2BZJ2QsGvxao245NpL9coK_pqEuM5nSHyWvdVWyaMHAcMBHzHip94Y-Z5rlt98QWgbp48g7NMl1CcUzag7h_GtuhwpZJ6CXkeDHJbzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9QHmlfO-vzyNExYvc61MBretoO-ZsXljI03GF-jz5Ka_laBhTEirrVAm3trCP99IDJkdVHVhgjZK2MjYiblAN8uqZ5wYF3Xjbcb4oePu0vhdnD_4c2KHTLDwKBqhgqtHE9Qpx6K7TiVyD8QU9-M26mEbhbbZjFdsQkKt6D4jbMJ1HUuxHu70D8SZj-AYjEIIttubFaQn9khCWo-7LxStzO5rnp9kecP-0RhS4P_qWHx2-PrbaOiKtW_GfcU9R11eguLpcvYjfsA2ViqPbIZf2K2AkB7JmPvk3Kindbm5eVvpBq0kSL9w3w0SVZnv8MDSMQNdnyE6d9_mVg4jObPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqjrO6TnNRQHqr6Wr7FnXvBl6r-2NYAzWWC3U6FIhKRHeTgdsrZXQVkfWlaEZWRuFnjsIRsZgMdtK-2t_H98mYZT5MMacq9SQUeOw_gk7LBGLUr8AvTDMzW_K4Ti4tAfDSKx1UjWJalwIV-pC3tf8EFADbnZX1V0m9SF-rRsjdXSle0kbRzwOERb77mJHbUfK2a1CsNkYyrBDYVCnCbedtD8zwqgmO5Dc3cpOHnzgmpuOFPoP5Tc0Z_AoA-zqV9JCyloaroqPBNC-ny3lKCgJRBuv8uWu0Z4ff0eEuot4slfH9jQmrD9QaejZ9-v6vJNlGh6f9i8uZObwfbAFu851g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fLiUrB8DhFmTLAHfp8hmOV3XdDzPPSa8JyGtSzYOTLR6EBQEu5Ok1u6pvgO82hh3HmaYyxuYl4EqihaZjgioD3gULloRgOU1mByxJHa5VDW_ceJVXMj-kpL8VnYn71ijfuXQeJxSyB6u6bW2WbWYT83UQSi5A9vQCuM9kG3ayLcDFs84bTekDRND-Uy0GqLHsBUvHZk-9byl89AS-ox8VMWOibtaWxf_ArwCKr58Hyt1XeRxDpeSYGyW1d4uOsUmIW8cDR-l-gECDbMMWFYvoNc7sEKJV0lcdSeDnVhzRN1Iza8hoqvy_KhtXEBt5hBFqmdKtXooY5KNp7NYkB6cvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9kOaByssZ-mScBYLN_eaYX9H1Xoz0XS8N0oBjNJ89ZEIDJF5tBsgysxH6b28aHTMClTC8342MpJ1v0sd3m3gOHP-yPcP7HQBvheOlVr2XIz_1EUhc11ugZtMoRCfn5K2-oM4AxH1l85t962phN4wOdHvJm9Wx9yg48MZ1DD7Abpi9gBKQU80rYOV4G2WmiipmOqJtp8ipsqWcKqGZG5fLkXfTh8jPkieJSQkzBi5tSc8EcAReIwtWpnY5W3OCR5cqimnAIk0CjRxceasZGhoqrU6wrl-prY51BRY3nfPrAjOmxPGn4vCzKfStIeJEnTooUfTnf6cHVYb504q1hr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVYNLq1LD6TTyYNKsJAgeq4wAyfTic9kFu0nDN3DliU4b2KcHKKDLBIyOaWATIqXDs624Ore2XhwIasnCJg4daGu5DPxZkGh7oCj3OiiW1iL_pgVRmijKeYziAtJmrTa0_IBn6DEUW5lF5LKJGMJ3KgU8lTWCTN7cEiV3YY5KAHV8k-PR5R41vR71BcnoTBcwzzNTJncPXEQqHQJRR7qDxD4MPu-5i050nc5WxFdA6L_bkv9u46ixZGFqSC36qEVVfELXrx-KRH78yIcqe5hdkd8GzcMEwxTpNkVo_mw3_8CZEO49PzeERoBxmoczCJZrQzpU_mpcJM7oFpxmcsyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwafjbRC8P1kNVLMLXQH1v0u3PuJ8yNQQZFrf8KSZ7ndMwPigkij9OxJFiF8vjNxYO-ak1Pnj1ZyAMFvVf3Kn8Ba2QF-FxRdOVHHeFV8kMMiboqEVB1S_unwt_16hc0isC3ed1A8dymIw0sSf1vj337tvRABIeATJ7YTrNeL2bQ1mdAjoIVHgsDS2igM0nGUYH8f6NwssSYO4ZJ9gG9NScUUu9N4xd3qkcdBBo1W5kuCk9HqwkDBc6_emWsPuNZBPNbQMnyYkrM_9xDfrCEV0nPUwtg0Lq3-OZVipcIZdVL_LBK-7lVE4fYUp4rFGDd0ruZJHQmI27YUW0fQBrU92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXwGgN6QigIfqCNotezqqklm5pBrkjreGR-3gkyx7gdyQOFQKii4lamH29r__LMozrWo7a7euDOhQqSH3JCJp2zvN-DdAwLIIDnKHDnAZy8_eQC_SNGRJXt1NRLyr3Qiton53WN5_3vdgyFZz6_38EHoLHvdR6aOVux_4BWsdDRlQlWbXQ_Pc2TN429BapoCqu_FezKhnGO_kjrADvBS2HSI0wyjgIaQsLpxoxJ9cnxOszgkqaFatfuhxboq-4P92AN8re2_a1Kg1C4AD-UJmNDpBm4x4oz7azbY-_lLdP_2vnxjRBHoDgPoK1mQIlaK6TuVJsJjyxErC7DUiFmf3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/456111" target="_blank">📅 00:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456109">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8x2DZNj_Cx5wa4f5yEuVq-PBgEckH-2bbWqU2lUixm_V9oIqQeEbHaIPRnlppLLbGHoHrZeis1RxSVh4qMiZVer7-5I-bG1GXkPuEvtNqrxanyd3UUhwaAbHxwatu2A0bET9NeJxdvI2Ki3OmbJq7yKxQFvJfEJRzi0J1MLus9C--bhVPFxbFzGFcCP5UOQFSGd5OeyLmZRON7OSrif4PRi8GsKH4MIHVhT-jxtrT92dHBqH2Z66Y_C1tIGwDZz-LeDl79tybppnDFEvxq5phtbsmCJKpuAoj3O0f1ElnlkNIbiTDSPwxpq4bqIVJ5zxXc30mkK4HLjuFcyMZJdRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lD2f5zAiKtaRNvXs9P1iVM0AtRDySvgovlaXX6F2ES7uN-shPp8N5Sus72LzvhoKFtYpQ7cC5AHdemPFOVYVQRN7MqrtgzdWEJVflXs5iPftSYWmMRcbAEdNA9EPrldu_iGgZknewdnbVT-ecqbScBDr-MwVW8b6wIJ3hwBpzeEptrqin8yxgVB782PiSr6uJ19yUzMs1X4zAui1kKahahimRahkk2FzwuBPUpj4AOB_LkLkiR2cPybcVvEAXCgpE_aWHI5B_pdnEM8WGQqG6r6kI1rTqNiWU3x20Gr8VOgbWUQtlHif593XHeey18MBL2qVx2UCqb--IfLlcFv3pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرچم سرخ انتقام دوباره بر گنبد حرم امام حسین(ع) برافراشته شد
🔹
پس از جمع‌آوری سیاهی‌های محرم و صفر، پرچم سرخ انتقام «یا حسین» دوباره بر فراز گنبد حرم امام حسین(ع) به اهتزار درآمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/456109" target="_blank">📅 00:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456108">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c9df1e95c.mp4?token=f7DLgUTMZacfFhiAbhXJagbJ_sm6SmfLefNHxlzgPn1EtR6g6cbPBqtH7YYm0C8uK_MeAZ8EwVk1n5g1cEARn21QER03i70Sgk6dJHb6g8lSmk2oZSKqPiyeIFqQulHVseNovBRwpNEd-0bqo2-ypIHZ0l_qe4KCboFoobCHeJ0piZICIzIMnkD_uFRpvR1Ci19WlGACtG1OTXOg5WgcouU6yXyOqmnGSzUXc60JeIDdnTcSxLBv7WPpaAgm6IXlRRlSvwFmTMNNIYWkxD2sUrToFpZObqtnT1UL9N5itRIlklwGCQuzO9SxwTFoBSsVQNRDpV5q5awUAHAMcNyptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c9df1e95c.mp4?token=f7DLgUTMZacfFhiAbhXJagbJ_sm6SmfLefNHxlzgPn1EtR6g6cbPBqtH7YYm0C8uK_MeAZ8EwVk1n5g1cEARn21QER03i70Sgk6dJHb6g8lSmk2oZSKqPiyeIFqQulHVseNovBRwpNEd-0bqo2-ypIHZ0l_qe4KCboFoobCHeJ0piZICIzIMnkD_uFRpvR1Ci19WlGACtG1OTXOg5WgcouU6yXyOqmnGSzUXc60JeIDdnTcSxLBv7WPpaAgm6IXlRRlSvwFmTMNNIYWkxD2sUrToFpZObqtnT1UL9N5itRIlklwGCQuzO9SxwTFoBSsVQNRDpV5q5awUAHAMcNyptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: تنگهٔ هرمز یک ماشین پول‌سازی بزرگ است
🔹
ما امتیازاتی گرفته‌ایم. اکنون ایرانی‌ها باید به این امتیازات پایبند بمانند، اما سلاح هسته‌ای در کار نخواهد بود. ما قرار است مواد غنی‌شده را تحویل بگیریم. من به آن غبار هسته‌ای می‌گویم. من دنبال تغییر رژیم نیستم.…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456108" target="_blank">📅 23:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456107">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHbcwoI9VDoONuIsK5wYy07sjiocSDczIlX-1y74J1WqVKlKkRT5MInI145Jg9YkzNZs6QL_nYu2hhmSfzdRAwYPJP_Hvxw3gPuusyPb3idS6ID5qMuveLAt-Yhjyds18UkyVdadzYPdTIW80WxEOsTZhbbboP6_oPKgoD8yKA9jwc02qnLBVHSlFO4lBsjWlnpjZKVUtA3OAXzGXHFXB4PyOiUFTI-y5XwRv0pjh5nJoWAIcdeLg1JuAwwdVOav4ETA3OAgdzqfmCW1MYjicyv3Sc9wjlNOmi9znsnLNMWTJLbCQsy3j3l4DoEx_R3Qhyt5e0xcRogwFXhu93L3Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدرنشینی استقلال
🔹
جدول لیگ برتر ایران پس از پایان روز اول از هفته اول
📊
نتایج:
گل‌گهر ۱ - ۰ نساجی
سپاهان ۲ - ۰ چادرملو
استقلال خوزستان ۰ - ۲ آلومینیوم
خیبر ۱ - ۱ فجر
استقلال ۴ - ۰ مس شهربابک
تراکتور ۲ - ۰ پیکان
@Sportfars</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/456107" target="_blank">📅 23:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456106">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f438219c.mp4?token=g4mwCHT6yCVNz2ljPpoNfWldd6BF_Zs6XXCCRVhiRqs_6TqyMDfSdYwg1EvgrYj7dlifjat-LxgLu1ylriDjfNFKfWFDBp8Vb6cCBTpM9ynKLrryUmzep-QVXDKhqp0uXMUrjq2ep2aMeddPTQKrW3yBm9QMk56H-KDSgHk8bB4g4h9B-0ReesAQbor88BRvmqRhGOE-FzMIYLQECH0iyC0cRA2JBx3voEdvwLkrtBLGLSPCBbgUQFiDGPyxIbiV0H-cpgifkJziQV76-USfmif9hPou0DgvLDiGj4glAJrPVKTrmhgyHGxGkkBydFBN_EwxTkMXyLRUeGoL4OJU_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f438219c.mp4?token=g4mwCHT6yCVNz2ljPpoNfWldd6BF_Zs6XXCCRVhiRqs_6TqyMDfSdYwg1EvgrYj7dlifjat-LxgLu1ylriDjfNFKfWFDBp8Vb6cCBTpM9ynKLrryUmzep-QVXDKhqp0uXMUrjq2ep2aMeddPTQKrW3yBm9QMk56H-KDSgHk8bB4g4h9B-0ReesAQbor88BRvmqRhGOE-FzMIYLQECH0iyC0cRA2JBx3voEdvwLkrtBLGLSPCBbgUQFiDGPyxIbiV0H-cpgifkJziQV76-USfmif9hPou0DgvLDiGj4glAJrPVKTrmhgyHGxGkkBydFBN_EwxTkMXyLRUeGoL4OJU_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دغدغۀ من معیشت مردم است و نمی‌توانم نسبت به آن بی‌تفاوت باشم.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/456106" target="_blank">📅 22:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456105">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c8bc4c94.mp4?token=lY2w4pnnWGOln2fR0eV0Ee8pFUKp6e5nrHTmT-20L9HJGNouOXlkGpwWhmaNvVsIvYUQnT7aB1rZ1fwjRpVB0KVY2H5PpARxglirUjFjE3LQn1MQv4a1BJCHVUOEJaA3acNY5_BqtegDksrLUilytrGKmMRn3Oaa2Lt1vOvosqkgX68azhgi6JgBcdCXEnjXCVcDcGznFsiEXS3RlQigCfWG5SZoKsBOH9wy9kUVz4Q0P9eFZY8X_X-jDdfeRg_SjDoCrRbsY6va9pXd9HGfXvkCjZsEWt1Klkypc-aKsLD7lFPB4mlzkRp4wTDUI09sOxyOWvr-S-2V0KAyxUkLsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c8bc4c94.mp4?token=lY2w4pnnWGOln2fR0eV0Ee8pFUKp6e5nrHTmT-20L9HJGNouOXlkGpwWhmaNvVsIvYUQnT7aB1rZ1fwjRpVB0KVY2H5PpARxglirUjFjE3LQn1MQv4a1BJCHVUOEJaA3acNY5_BqtegDksrLUilytrGKmMRn3Oaa2Lt1vOvosqkgX68azhgi6JgBcdCXEnjXCVcDcGznFsiEXS3RlQigCfWG5SZoKsBOH9wy9kUVz4Q0P9eFZY8X_X-jDdfeRg_SjDoCrRbsY6va9pXd9HGfXvkCjZsEWt1Klkypc-aKsLD7lFPB4mlzkRp4wTDUI09sOxyOWvr-S-2V0KAyxUkLsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: شکافی بین دولت و نیروهای مسلح نیست
🔹
دفاع جانانه نیروهای مسلح با پشتیبانی مردم و هماهنگی همه بخش‌ها، محاسبات دشمن را برهم زد. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/456105" target="_blank">📅 22:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456104">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVPHj1bPDoFxEd2XXWZoT7Gsg6_UiT3p1D7MTqqrqiUPzYKXCOEGrCAdXm6gbWicEmnY3Fh64Xuva3dCuuhv2VzHF53hEccDsv_VQz0zCn3Bvg8K1-_SeV-zZM-y_oIzvBo8ZhkhWCOKUK4s0guQA5ChwXpfBs9ka8TYaZ2MCH-UapAQfGlNCFpERgyc54j9b-RTBYz52Xll46cFQlcTqxNcaMQxB9QfaFtLBeyZ6BVNiXMbf8lcGYm_8UFq7CAo0yYDml0ivgR4qghu6VvskI3wTtY7FXatGs38X7C2h9u2wwLSzChxLWZ41n_DNzl_6ZEfhfI8dR9o_CMFuuWxmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نیروهای مسلح یمن: تأسیسات آرامکو در نجران را هدف قرار دادیم
🔹
یک منبع نظامی یمنی از حملۀ پهپادی نیروهای مسلح این کشور به تأسیسات شرکت نفتی آرامکو در نجران عربستان سعودی خبر داد.
🔹
این منبع نظامی به خبرگزاری سبأ گفت: «نیروهای مسلح یمن، آرامکو در نجران را…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/456104" target="_blank">📅 22:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456103">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca76598f8.mp4?token=tlpyMdUcD8cfzzg2KzG25uUoRaeuUSNxj-INsm4bHziXAqzXPiioepo3IEZxkERe7jZp0EaNYCUzEV_1Cb1lemgMB5uy-XNX5OMXWVHRtCwxBwQAicI4_YeY9FfwVZSLN07hhwH2TsFDT1CviTsd_mfPYodjmOTJvH9SKC7PltHOG1XK0lNhdisP67LNMSPxzuEdL82pVmG1MdASz8u6SrZqup7VKT77c7Oiu2dSBC9K6nZC3s86KmFl9331rXllNhYlzV4_DGcgf8MfOSwpxsMXqrv_sNtkb-9i28GlvTQhPqN9BS2x4sJmODz85VHfr154jzbH-TN9vO-ty3R2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca76598f8.mp4?token=tlpyMdUcD8cfzzg2KzG25uUoRaeuUSNxj-INsm4bHziXAqzXPiioepo3IEZxkERe7jZp0EaNYCUzEV_1Cb1lemgMB5uy-XNX5OMXWVHRtCwxBwQAicI4_YeY9FfwVZSLN07hhwH2TsFDT1CviTsd_mfPYodjmOTJvH9SKC7PltHOG1XK0lNhdisP67LNMSPxzuEdL82pVmG1MdASz8u6SrZqup7VKT77c7Oiu2dSBC9K6nZC3s86KmFl9331rXllNhYlzV4_DGcgf8MfOSwpxsMXqrv_sNtkb-9i28GlvTQhPqN9BS2x4sJmODz85VHfr154jzbH-TN9vO-ty3R2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاش پنتاگون برای پنهان کردن اقدام به خودکشی یک ملوان در ناو لینلکن
🔹
همسر یکی از نظامیان مستقر در ناو هواپیمابر «یواس‌اس آبراهام لینکلن» که هفته گذشته اقدام به خودکشی کرده و خود را به دریا انداخته بود در گفتگویی اختصاصی با رسانه «ام‌اس ناو» به افشاگری درباره…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456103" target="_blank">📅 22:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456102">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a620415e38.mp4?token=VQ9TLfXqxpptcXdbnaT6Ok1wyZOmgVhnXyrLK96nhlSjtGIB5I7H0V-PbhJWgWMugDN7Vzj4-QKVT6Z0HqelcuIAWumHXi4tQZJFk3Rn3KaTcGX1LgWuhm63R0jIVUqII_viU8NjBURgxzgRDdHHtI_RPvWM6FE1cMhbhaLJlcDpv-MZbQcrTCt_-b9rrRlxuhHkFN_j_8a4YZP4gtPG9uplVnPVxhIolIw4zREI7oL9S8DPSPYsSZ22jJvLpvA5Pe1HFyC8CtOOqMIVLoJgY_Hk8XWhpVa9r2z8wqSF5Ue2Ppq5zqxF3M11ZBxPEWLF82s1n4vUqgPv5y890-ynDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a620415e38.mp4?token=VQ9TLfXqxpptcXdbnaT6Ok1wyZOmgVhnXyrLK96nhlSjtGIB5I7H0V-PbhJWgWMugDN7Vzj4-QKVT6Z0HqelcuIAWumHXi4tQZJFk3Rn3KaTcGX1LgWuhm63R0jIVUqII_viU8NjBURgxzgRDdHHtI_RPvWM6FE1cMhbhaLJlcDpv-MZbQcrTCt_-b9rrRlxuhHkFN_j_8a4YZP4gtPG9uplVnPVxhIolIw4zREI7oL9S8DPSPYsSZ22jJvLpvA5Pe1HFyC8CtOOqMIVLoJgY_Hk8XWhpVa9r2z8wqSF5Ue2Ppq5zqxF3M11ZBxPEWLF82s1n4vUqgPv5y890-ynDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین گل‌به‌خودی فصل را علیرضا آرتا وارد دروازۀ چادرملو کرد
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456102" target="_blank">📅 22:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456098">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDyTVe7g62v2qBQY58itp9DXqTNwd17OjwkQ5EkmDBjI5pr_dN2j3LeTPr4eBmwz25wt5wD6y9lj0GLpxXKJMQo2hCsyRCzsjnvspKcofby9qph324ZqaIKTjUbU3KyoxExmoWClnEyidZ5qZgPmjm1F2093E29ygn0JcDLQuyT-NiMauZn1CLMwYU_2HkX-VaiYhp3GdmOyC5RuUvoN3CNfR9XNYaOaocyd6TopgA1wTKqA37hcpI69bunBUjQOQFAt2WLBqF6qrehZWBLrlA-drNn6yMk14xcUyGWl5S-bRBdymSs3bh2PHXVCraKqCqZOouH3lOruVz5hfkcVTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fsc1peZ_5VxnMtkyBFLAcol8XlHRL09wyuOguxfilRwEGCoowGcYeihTmSl6-HcD99DFzcK7Sl3bpjptD19tK_ZObY6DT0xu-ZEGwNKEGrs0Jb5N2pQogKaNWe5tjkR45vPAkJ-iu0bJwuoXQU1el7M_f4zZJxCsU2r2exAYWP7PFkkhrIwQkEUklucWdKrOmeKwr49GUIc9JfFqeQ7gvFUWOzjFT4jGjoFUS6LIV38Cm2s7sbxWML_5rqSKEeAzSOuBWXOCGiVrwOXZAdLMS9n1azXNWENANb5vGfWfYRxQqIFgbLbYZ4J0ggMHsmgyRBuXSlfH0GlqfMs2giDK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mg-U9_OsDVToRowXw88iXisN1jo6Ogsbd1i2rUpDhq9IK3lZiaveTqK-fybxhDQU365IhBQzP9lKj4-j1axX7WuExRRFJWOu_ACcmXYbr2XVn1R7cpqKiaLBo2pO7sxntdz21XLIzJaAi_iT2wY_KXDx7ly_bvDqGVcf_xHg7yzPezJLjFVrINpE9-Uii35PdQmIY6pp_SjjKukoLMRphpZo5yA1mm__Qig_GVGzKRmUstYSa5SwH6SA4qFKX0Xx9E1eEpO-Ubr4LnnalSSZMSxuD6HT_GlIm7feHKBxB_z5-PHrhz67ScZXu77SkkZa7A-wPpv0Ba0CkA7iflhdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4imfBvKOuvox411t7br_TL52SCqwV7-c15G1dFyrmFzLNLjeekTooRumoz1-kTZLdObcw7tVjEdeBFAX01xrcrV4wPPnx7wvJo79eMWr_aJe5A9wobUueNwZKhH-juh-9vNGIMWXHXz2YF98oFyNHjS8ila_X3h418ALlZ3JX-gJPKxlvSPUQ2RMl50pkTtKPeKyImh_sAUlHt9jitk_kArozqmyfYfAM215rd6PoOdhD9a8MP0QiWDrqTUn7cCVH0mwadJTQy-Y6mRmYKQsR_vBZwTW8oreRwBMEWgrzqEt0MbbW-HEUrp-L2bmmv-UTSl0GXcSpkTIkSnBV3V4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
گل چهارم استقلال توسط قلی‌زاده دقیقه ۹۲
⚽️
استقلال ۴ - ۰ مس شهربابک @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/456098" target="_blank">📅 21:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456097">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dbef8bbd3.mp4?token=mr0amcthnBb9yy3eab1qY92Rq1RNHgS6L_1f3eDKmZfHzjUZPZZ90mrD-GSSJttlb3TAgp99wIGs4xBM23cK2Qh1du4Di_ljNZk9wCsnmVCID0BJpjZbkZthVGBbwx7Ag5WuKSL0eosaeGR780ESC8iZhrAYDzAJOjO5XvaZvsvvpyI3Qh-pDoLIAlPnqFErVPezhjgCAXvVvmXnjJEHkWXGSP_DPY68DgL8MSXhkEtZ_qQy2hsHQoG6TRRibTIfWd_bOvK6ZpJ-tbeiEB3gH1kmlAX2ztKtvRU_OwBGgcKgJ7FR4h48hAGvr_J36TOPfN2b2I0qkz-SzLk8vk-UGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dbef8bbd3.mp4?token=mr0amcthnBb9yy3eab1qY92Rq1RNHgS6L_1f3eDKmZfHzjUZPZZ90mrD-GSSJttlb3TAgp99wIGs4xBM23cK2Qh1du4Di_ljNZk9wCsnmVCID0BJpjZbkZthVGBbwx7Ag5WuKSL0eosaeGR780ESC8iZhrAYDzAJOjO5XvaZvsvvpyI3Qh-pDoLIAlPnqFErVPezhjgCAXvVvmXnjJEHkWXGSP_DPY68DgL8MSXhkEtZ_qQy2hsHQoG6TRRibTIfWd_bOvK6ZpJ-tbeiEB3gH1kmlAX2ztKtvRU_OwBGgcKgJ7FR4h48hAGvr_J36TOPfN2b2I0qkz-SzLk8vk-UGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل سوم استقلال توسط اسلامی در دقیقۀ ۸۸
⚽️
استقلال ۳ - ۰ مس شهر بابک @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/456097" target="_blank">📅 21:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456096">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6b1ea3c2.mp4?token=h2aUAicJzkN1xf9qNcjRMy-XAJ93iFb5BMVckQhjmlQoeQQvvZAYdhql_rYxCrBpUhYDk9Dpovz6qHwfXlA7gZ9XXC7voeB0y1fkT43i7zTgSaV_rxUuoiXL-pUJLKvRUr-CQ_syifiJshIfCUpfFgagtN-gqFilcxx2T8LneOKG_FPTys7pBLOdWRiAv5xzb5IFHpMcqyZE4_loLOz9uQ7SMeF46II1P-EsoQ3MyiUlXD07g37CI5dOa0wDJ_nlWmB6FBglwP4QBgBNXL9ptu7XxFSgn-Cr_hAt011epKBCtxwCuAjpWKFOR-ubWzCn5yqXvxrQZgcnqOEBAsQA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6b1ea3c2.mp4?token=h2aUAicJzkN1xf9qNcjRMy-XAJ93iFb5BMVckQhjmlQoeQQvvZAYdhql_rYxCrBpUhYDk9Dpovz6qHwfXlA7gZ9XXC7voeB0y1fkT43i7zTgSaV_rxUuoiXL-pUJLKvRUr-CQ_syifiJshIfCUpfFgagtN-gqFilcxx2T8LneOKG_FPTys7pBLOdWRiAv5xzb5IFHpMcqyZE4_loLOz9uQ7SMeF46II1P-EsoQ3MyiUlXD07g37CI5dOa0wDJ_nlWmB6FBglwP4QBgBNXL9ptu7XxFSgn-Cr_hAt011epKBCtxwCuAjpWKFOR-ubWzCn5yqXvxrQZgcnqOEBAsQA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سحرخیزان در دقیقۀ ۵۵ دبل کرد
⚽️
استقلال ۲ - ۰ مس شهربابک @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456096" target="_blank">📅 21:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CHNyBYelj0cL_MDIe-DXgZXiE-14H5rVDg1Le-13gYuw6iyjxfW8oqVo4etj9VdKg1cCZ6KqmQb-_u1b4WOkrYDR_EQhy8N5ZTlaZesfJmd4qM2ZmB3WhcgTc6pEAN58hcXmm5wIMc-e6d9JBUqnCVzKkKfm0nKRme5EZI_lbS8lFid3AGnkFOLOIpXHkN-l9sRkz1JtIH8lHmlzEY5LNYfc5OtNP_1K1ldJ19EH1Hfzasn3zMU4kZYBU-wGfF1OtJTgbS5RQhWmrsZI_jhERVtdXfbMcC0XQ43v9gC4pjBO_KHojWTvrjz8P0qCSk9VnFzP2C_N9VauHESXv5OANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vu6jKLDsHs0o-HRHjvO0Kitn8t1WMYsRFCtUIpv9M-Rk18mhrQAoykV2mpQmplyjqtmf7A_T2Unb7a-1lH7KTV8IJ_NtPoKlHpWNYVBF3fO8gDJ-445UgZFWDGB8d07khZtmlfdFkcNC0Lj0ek7JFt_MHW2dPQ8lGnvt6oQ7V1hN4iu7h1bddmYN6pdtZxWa1cWUS5rGPtjofmaLaB8XY0CmLQuUWbJUxnT6PLC4G1awe9JWyDJ9v59hxq5_Vgtd78mhGX0OHpusjFfO4-nK6bMC8-v9SEltPKx2T10Qo1G0HgjWzkehOVGe-lLAhZuELumWwmfinWV6Ena0I4cJMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brCOf3LAuet8fxZHaPBWP3wkntsPXd_Hd2wlupcy6hsoIqOAzMgEnKZV0wGw-PmHoYKkNeR-C20h0XxzZGGQDO1DOhml7Srucj9WNj43jPWZwOyXUAXVQyH2LOTzWLtzYuYOEyDmYikgQM7-EfrrYpa5rGlA4UopU5Cbz1K4WMLVTH7kdFVrUJzgVcYPXZMpImcSaoUD6WWn40Wpi3Y1wQZKmsF1atSikREBwhr4TtpPY84HOnJe3RebYV1BaaHl3k2KftgS0nZ1UwVhXSZA0mv56zO8NzygJk-lP8_kpumiZS9f5mNIf7topQoiNf_prnZA1gwU9Fu3AlHgqST1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_UmH4V_FFan7YB6nDkqq-jIHaLn7MMRQLdsp6T2EPgg95LqHsQzGsXUAtnp3EO6RbPa0GIP4b-jJeMYf-bbesg4RNjdinPowM7G8BGm-qlCvL6fuJDJ7RCgSkExeDR6IYxIyUBqibm4KMPUlvSTP9mvs3LE2aBU4FAtCp4AvcRj248CZwEzNHu0ERLJ5iSED3BUstge9OP3c0a9f63uMi0SkUfULSgqqlnc8j99bJMKZW5RBEg90eudSbGQyYxILfiAiKZy55gaLi9q5l3v35-h_puZP4gkKUHLhQriI8U8Z4p5ym4PlyKmdDfkTkS2SniFNvY9ul2iGa2HDv1x-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JaHMZrMyG39T7dAkjBiIN0PCMXqg6NZj7jovS62_8rpgi_GzwXZSYefLgBIXn2L1tydwmpRCBlDH7jKql7ufEfJOb3_yxb_9LznyOocOp0m95sNCNy6vMrUakh0_-fyfvgdN5EgPqyVsiUDxC65vscFmG9WchtpoYK0pQdDzuvkGdkdEKgz_ytBEYZfOvAXOt585xR0gdOYQu2fn17WjdNyquMMQA16WzzMlTv0QK9Awsivi13Z2UNpYDWAmCWHp5HEvZpegQUU4yl4QrASuopG3Ybuj2HAc3WrFtZ-XF5lmz0ZUqlKohku9tV7YpqoPI-NqagHdWYWkUTyNvoZsSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxoQMh00fk3lC1GIJcckt2VQqnnOr4j3m8Pqm3FYKFYqf6xK9NCLJMvIc02CrhYyFu73X7r5i_Lz7is9-77OJquls45E-kOCBLLXnaslIgbvWiys4HUniA-Bqa4dMU9bPE_77RlG1mudyxNCFq9B9JPx9ZwxNou_WVNLHChqaj5PTAETugct_xNpzfAPksblYwpCqtzSpvDYsugHrfvYHHNCsjxCmZPDN8DzJHSsEWcgWO5wctACMCMQVSytv20YA9CqEZETLQwqtF0lNAULC432_5vSIIhGZxyci_C1NyIzlP1xriYm4hya2KR6Fro1pDkquHE93x3HdnULM8R5iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غروب خلیج فارس در ساحل بوشهر
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/456090" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456089">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
حملۀ موشکی ارتش یمن به مواضع مزدوران ریاض
🔹
منابع یمنی از حملۀ موشکی ارتش و انصارالله یمن به بندر المخا در استان تعز(جنوب‌غرب یمن) خبر دادند.
🔹
العربیه هم از آتش‌سوزی گسترده و واردشدن خسارات و تلفات جانی در پی این حمله خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456089" target="_blank">📅 21:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4424895b69.mp4?token=FH2M9bdt-Nmiv5JJAmgFTGbYhFuu-BRW153O24PukeJnFDl-Djxv39XVBvWpKH1XdplgRrdBZlVbId6xQEz7zBWxYSw6tBv4Es23NRutcW0MwC94f7GkhH2mgQd4XLJUyVf5zj9AWJyDcaFK9cDoCOHibhTyEcUv9VLlJy5F6ozB461cIZu4VPnQ_oRX342oGy4AWyRZ69mj7pgcjKvuWVOxexUd3BXZr8Fzx4xuexP3cM64i9mdYzNCWP_PjpFTDVRdVtNX8lWuWUM8pzySNCak6v5pGvEmmE9k-P4zRY6t1dgjnQSn4QfDDrmkctQwtsuTTALNRssyvPKxoBzBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4424895b69.mp4?token=FH2M9bdt-Nmiv5JJAmgFTGbYhFuu-BRW153O24PukeJnFDl-Djxv39XVBvWpKH1XdplgRrdBZlVbId6xQEz7zBWxYSw6tBv4Es23NRutcW0MwC94f7GkhH2mgQd4XLJUyVf5zj9AWJyDcaFK9cDoCOHibhTyEcUv9VLlJy5F6ozB461cIZu4VPnQ_oRX342oGy4AWyRZ69mj7pgcjKvuWVOxexUd3BXZr8Fzx4xuexP3cM64i9mdYzNCWP_PjpFTDVRdVtNX8lWuWUM8pzySNCak6v5pGvEmmE9k-P4zRY6t1dgjnQSn4QfDDrmkctQwtsuTTALNRssyvPKxoBzBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال توسط سحرخیزان در دقیقۀ ۴۵
⚽️
استقلال ۱ - ۰ مس شهربابک @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456088" target="_blank">📅 20:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458d36980c.mp4?token=LqfiQ5jEVXIh6tQXqlmfM0_1tpa66prDe7XIRpIP9gGlZ51MJi5kQ25BoJ6FNy3efFq06zTGWdpD9SLMZ7sBiXC0T7WU465faaTSWNxD5D74E5CzAsstMzV63DLBxOjZEG04poeGwRxQOSEIbCOB4nbDrelKQH2cC4_vr1tV_91X_fuZP-K5ela7Xb9cr5PdJnyeKubZSXgpSSmIambjJ-dbFzdV5Z4vK20xjS3GRe4CtMURBKVb7Dd3xr8ucdXPtYSCBGEwHZlUipR2CfHRFR00-ZRXNkzJpWAw9Vj8d_YTeJHNXAsRqSUyD0jWPFmGcvVfssi1GmApNszlxzvR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458d36980c.mp4?token=LqfiQ5jEVXIh6tQXqlmfM0_1tpa66prDe7XIRpIP9gGlZ51MJi5kQ25BoJ6FNy3efFq06zTGWdpD9SLMZ7sBiXC0T7WU465faaTSWNxD5D74E5CzAsstMzV63DLBxOjZEG04poeGwRxQOSEIbCOB4nbDrelKQH2cC4_vr1tV_91X_fuZP-K5ela7Xb9cr5PdJnyeKubZSXgpSSmIambjJ-dbFzdV5Z4vK20xjS3GRe4CtMURBKVb7Dd3xr8ucdXPtYSCBGEwHZlUipR2CfHRFR00-ZRXNkzJpWAw9Vj8d_YTeJHNXAsRqSUyD0jWPFmGcvVfssi1GmApNszlxzvR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجرای قانون جدید فیفا در لیگ ایران
🔹
به‌دلیل تعلل دروازه‌بان فجر در بازی با خیبر، ضربۀ دروازه تبدیل به کرنر شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456087" target="_blank">📅 20:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456086">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb2f4e282.mp4?token=rDJiMwKcJOVmBIcn1awOm3opaobPTuhIHLDXwDMMeW1TL3gFulwNZz14Q_Cxyf5VVCTL1CqNVD3u0r9yz-Kp_gH4Z61yAuj75tFDJuOoSC9VvbXODUtwdJrWy9bz4zedz1AsLfj_x0aL22rxJPOUmZHWjLTBp-s1dpUxIE1iO2LyDxZMiMZ6LPaT2Iv-QYoUn5HgKmQqv_F5dqfDeSDdLnUw0Kl5k5VQfODmBH7_q6TW8Tm2W-zthExC4ZE2d3FvejJr3tpwKkiMwXII1mS6JnlFmh2BfkicYCfu2Mbyhh5TJbWL4OLVLdfZK5rjSmT2x15wK-lOkKipdzp4o0NOYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb2f4e282.mp4?token=rDJiMwKcJOVmBIcn1awOm3opaobPTuhIHLDXwDMMeW1TL3gFulwNZz14Q_Cxyf5VVCTL1CqNVD3u0r9yz-Kp_gH4Z61yAuj75tFDJuOoSC9VvbXODUtwdJrWy9bz4zedz1AsLfj_x0aL22rxJPOUmZHWjLTBp-s1dpUxIE1iO2LyDxZMiMZ6LPaT2Iv-QYoUn5HgKmQqv_F5dqfDeSDdLnUw0Kl5k5VQfODmBH7_q6TW8Tm2W-zthExC4ZE2d3FvejJr3tpwKkiMwXII1mS6JnlFmh2BfkicYCfu2Mbyhh5TJbWL4OLVLdfZK5rjSmT2x15wK-lOkKipdzp4o0NOYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال توسط سحرخیزان در دقیقۀ ۴۵
⚽️
استقلال ۱ - ۰ مس شهربابک
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456086" target="_blank">📅 20:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456085">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74556fa3e.mp4?token=CidcV7JoLTnxPEy94zlyN3QTSkG2PQclTDXKSeysv1GDrC72Mi3gZRmdcIR5soD_g0B4h4lYc7YwW6kA8u6l_oxUMZ7aAJR1f-uL7zjjb6z4YOWXfPTKhzCAgDL_F5b3Buv0Ld4_bjAh9FcIQVUgaZu2J5gnjMdhsH20SAG4KRbvhpA3O2WagVpTIaHkYKlkhtyPVlOQLFO0gaFDY5c171Ux2W-7NuZTfB6fGNkN3Y8TBGoBjDWhtzKol5_jyR6vKbVyWObdG6uMunS-p7Hiyg-D3IFtub7uCxoDSb5-EjuoX6awHXSW8OqHmzCJCjLQoFiB6yE8abNrCffH4j1M9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74556fa3e.mp4?token=CidcV7JoLTnxPEy94zlyN3QTSkG2PQclTDXKSeysv1GDrC72Mi3gZRmdcIR5soD_g0B4h4lYc7YwW6kA8u6l_oxUMZ7aAJR1f-uL7zjjb6z4YOWXfPTKhzCAgDL_F5b3Buv0Ld4_bjAh9FcIQVUgaZu2J5gnjMdhsH20SAG4KRbvhpA3O2WagVpTIaHkYKlkhtyPVlOQLFO0gaFDY5c171Ux2W-7NuZTfB6fGNkN3Y8TBGoBjDWhtzKol5_jyR6vKbVyWObdG6uMunS-p7Hiyg-D3IFtub7uCxoDSb5-EjuoX6awHXSW8OqHmzCJCjLQoFiB6yE8abNrCffH4j1M9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ موشکی ارتش یمن به مواضع مزدوران ریاض
🔹
منابع یمنی از حملۀ موشکی ارتش و انصارالله یمن به بندر المخا در استان تعز(جنوب‌غرب یمن) خبر دادند.
🔹
العربیه هم از آتش‌سوزی گسترده و واردشدن خسارات و تلفات جانی در پی این حمله خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/456085" target="_blank">📅 20:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456084">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حادثه در کارخانۀ سیمان در تبریز جان ۲ کارگر را گرفت
🔹
استانداری آذربایجان‌شرقی: بر اثر نشت و ریزش مواد اولیۀ سیمان در کارخانۀ سیمان صوفیان ۲ کارگر حدود ۴۰ و ۲۳ ساله زیر مواد گرفتار شدند و جان خود را از دست دادند.
🔹
بررسی‌های اولیه نشان می‌دهد بازشدن اشتباه دریچۀ مواد اولیه موجب ریزش مواد داغ و وقوع این حادثه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/456084" target="_blank">📅 19:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456083">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شیخ نعیم قاسم: پروژۀ «خاورمیانۀ جدید» در جنگ ۳۳ روزه شکست خورد
🔹
دبیرکل حزب‌الله در سخنرانی سالگرد جنگ ۳۳ روزه گفت: تسلیم مقاومت صرفا یک توهم است. مقاومت همچنان به مسیر خود ادامه می‌دهد و اجازه نخواهد داد اهداف رژیم صهیونیستی محقق شود.
🔹
یکی از نتایج جنگ ۳۳…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/456083" target="_blank">📅 19:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456082">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnpCkgnpEkjZiZ31-m6qZn7Gb95be4lpjYJ-lkMIjLryKJG-Yr9FHDZskBfXGav2RLcM8FeycGwBfeFiCBEQLX9lz5UTdlaoMDzgIRmwKYyt9vJYSWzPli9U4kY8zuQlYRRd4lQ0wbph4Eg4vLFnTayrK4FVc3XW2RLPDY3B77qSWzSI6I2s4UrpzcAXs8OQd_agxig6OJ-eFS14zLIDYoQl_VCc-WP8EN-YGeAro1eBTxCSokCLoZSE6U2P0G-zAaVwWM9GkxaedDz2xdYStv20Gq5kW9L8N1xvmu8VINrFdaD3nBytBhnQ8LnvzPl-NqmlkMu1-HfsCcFlv3HeIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیخ نعیم قاسم: پروژۀ «خاورمیانۀ جدید» در جنگ ۳۳ روزه شکست خورد
🔹
دبیرکل حزب‌الله در سخنرانی سالگرد جنگ ۳۳ روزه گفت: تسلیم مقاومت صرفا یک توهم است. مقاومت همچنان به مسیر خود ادامه می‌دهد و اجازه نخواهد داد اهداف رژیم صهیونیستی محقق شود.
🔹
یکی از نتایج جنگ ۳۳ روزه این بود که بازدارندگی در برابر دشمن از سال ۲۰۰۶ تا ۲۰۲۳ حفظ شد. دشمن در برابر این مقاومت، این ملت و لبنان مقاوم تسلیم شد.
🔹
آنچه در پیروزی سال ۲۰۰۶ رخ داد، نشان داد که مقاومت می‌تواند معادلات را تغییر دهد و به تسلیم واداشتن مقاومت سرابی بیش نیست.
🔹
حاکمیت لبنان با مقاومت همکاری نکرد. متأسفانه مسئولان محاسبات دیگری داشتند و تعهدات دیگری بر عهده گرفته بودند و تحت قیمومیتی قرار داشتند که نتایج آن بعدها آشکار شد.
🔹
شیخ نعیم قاسم همچنین خطاب به دولت لبنان گفت: چگونه می‌پذیرید که به ارتش اهانت شود درحالی‌که باید از آن حمایت و حفاظت کنید؟!
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/456082" target="_blank">📅 19:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456081">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehwWrv5mBA-Eyo8o_4j0pePirc6JKiQusQgngTFJcuOUQPm1OznwBZd9H6TdoXv949o2lUx1ZDMqwKecHlL-ziFDEOHjLCDSNvs6WJMa_KZPzkgd7QaZOegMlY3W8no_0uTy_gaziejKhaIy3jTkC8rUAJ6q3X32NS62oNQA1m5RygJXJdyfxH4VdATntKuMiVa4K0dCU0tiYBXQlcvTdUwSodC4B9JdX48Agrq2dd9jXMMxXOcXE7CXr_h14zapPiwTE22KLUf_JXGE_WVjjGcGKf2fc09C5EC5OsEoev4o5Ty7GvJxPbJ-R23kQL5XNzkMgXR5wEXDAnZik4yBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفای مشاور امنیتی ارشد ترامپ در میانه بن‌بست در جنگ با ایران
🔹
همزمان با بن‌بست در تلاش‌های دونالد ترامپ برای بازگشایی تنگه هرمز یکی از مشاوران ارشد امنیتی او از سمتش کناره‌گیری کرده است.
🔹
پایگاه آکسیوس گزارش داده اندی بیکر که از مشاوران قدیمی جی دی ونس، معاون رئس‌جمهور آمریکا است طی هفته‌های آینده از دولت جدا خواهد شد.
🔹
بیکر در ۱۸ ماه گذشته نقش مهمی در شکل‌دهی و اجرای سیاست خارجی آمریکا به عهده داشته و یکی از اعضای تیم مذاکره‌کننده آمریکا در گفت‌وگوهای غیرمستقیم با ایران بوده است.
🔹
خروج او از دولت در شرایطی اعلام می‌شود که کارولین لویت، سخنگوی کاخ سفید نیز از سمتش استعفا کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456081" target="_blank">📅 19:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456080">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4744c05f93.mp4?token=qUEMkLV0-qwfNkkloBsjg4RHLaMAWQEJh48EmVY5YU_q6gcTmuTXXb_-qbfy9i-yHF2Ny7slZ98fboPJ-xIsZQ2VZqNIX1pRbStbU6ZTgvV8kJRv0EaQTCJzZfSvqeRwJGgkPOPRcHT7PalfWwrUeBaNIE0NfIkn1WNF0Ld8wSq7m8sIFayUJ2ao6qNHR03dP4RJviHQ1gyKBoabBobAn4-OuwwgUF-JL--3x9Yh_GuZ3rEVM0UjCJ46G1fBWNIGfznnYQE9XxD355tWyb5d_NYV5Cut9Vk0le91oRXeCAZ_lACEWiuQA4x-nptWV_FYRx3fPnwo-VC5OjjXjgkLRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4744c05f93.mp4?token=qUEMkLV0-qwfNkkloBsjg4RHLaMAWQEJh48EmVY5YU_q6gcTmuTXXb_-qbfy9i-yHF2Ny7slZ98fboPJ-xIsZQ2VZqNIX1pRbStbU6ZTgvV8kJRv0EaQTCJzZfSvqeRwJGgkPOPRcHT7PalfWwrUeBaNIE0NfIkn1WNF0Ld8wSq7m8sIFayUJ2ao6qNHR03dP4RJviHQ1gyKBoabBobAn4-OuwwgUF-JL--3x9Yh_GuZ3rEVM0UjCJ46G1fBWNIGfznnYQE9XxD355tWyb5d_NYV5Cut9Vk0le91oRXeCAZ_lACEWiuQA4x-nptWV_FYRx3fPnwo-VC5OjjXjgkLRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مغانلو اولین گل‌زن فصل جدید لیگ برتر شد
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/456080" target="_blank">📅 18:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456078">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0vFyZ4Fi5joh1wVENc6iazt7tN0vFkUrQz4hJqjPFp9t1pQrh3fVCLikzkbbbBLHSMrogNN2GwaHUU9v-Kror5oPYwzyumcolg2ndiNgAhKe6S7r9Alfq_oj1rGHEvt5sDcb0n0Msjm1Q3krvwcy0Kkj_E5FcwjdpMf516mpe3poAHzSZ58Km7kbvyQAjaQ2kc8kPAuMWeg73VUvXDOQNtOGZ8TJeSqpciVCSMOD-fT5oEZBQL3mLW4dP4EVALtK3gyPzIxeXjwU5OFnEnQ4ykW0dM12TAXfiwlwXnS7CknXP4CiWEP5nzkfmVy1WhUVDpBZ8IpzfUZ_ZhnqznWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-rRvhyVnkFybehH73LqJZkeeHtlT_hb8EzkfMMMjXpYzkA4hmIUcYd6DufMxZHAVEkbmocmn9JzghXT8_qVg0ZATDVNEycPKkvuAGzJxu0ZOBDFqgQzS091NsEmo3ZdWsZDUwE1xRAUK3OFDsjdljV0jqzrOTWeNYFaOFUsP6sX2NxsQVKUuG7E6Ht0V4Dkx76-1OHlDVeFk1CqJpeo2DSeNgOqnNvfCYf4FevD-HvAr82QZM8xEXxBQ0gNGn7zNGjswLI1L-55cL8gWBUQ47u7CPMe8nmi5rPMW5egoeNAi1_pmT4gybmxSgOkRg27GDr2FRzzUigj2i4ucPJ3kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جدیدترین تصاویر بارگیری نفت در خارگ
🔹
شرکت رهیابی محموله‌های نفتی «تنکرتِرکِرز» گزارش کرد: داده‌های ماهواره‌ای نشان می‌دهد یک نفتکش غول‌پیکر «شرکت ملی نفتکش ایران» امروز در حال بارگیری ۲ میلیون بشکه نفت در اسکلۀ آذرپاد جزیرۀ خارک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/456078" target="_blank">📅 18:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456074">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqE6ZncD7rOZp9h4pXah-5KHtMgPWRs33Hid_TnImbRsJ7z7fxEiodEe3EY0Tsc9xAc2SQ_kylqUIeOpWMx8_fY2oO7-195Qekw7UlogvnU9nJ8UTH9iFsE8NsmjWgNA89NQKFpD0xhLw8ZABULQCJNOKOXowIwiKVWUL_Mp6BHth4erotXvKyehRukuJQrrcf0Rxl225DKzyLBmeXAPuzP0lRlMBJggsyCj8DRnavoIoHzqwJEGOwdMJWC2OsXDye1imuPfqf1AZkoi5znsz6p73cI8Cu6PBcxadV5SCC9nH7EwAKulJgUm2wEN1zggnl-qQiKbvurynHW5f247bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AO04gDgNYN53lvmpj8QslGHGrcUjWeWQ4D-Z7vZOznwX1_KEgi80GYYuwng4OmWy2K1jMTavkNa9kWwDokbNrpJrdUEbD8awnnCMBXsmm9MNo8a1UTSf9Z4Li4Dnc_vlArSKZvGlE2gEwACBY67MhSF8AFNkySXq025VrTeNtIYi4SeWk_upCKv453AIHsKGwTtFA_2bQFsgCAb3j5nklof4uJEvI2w4E3sExODaBIruuoH5PR1VR7ziCgjsiizuVxwOM-2Oz8g8lCVWQzeu82bUsYlscFTZ-EipMr8OKe05sbacn2Ffa_nMSsozSA5cyxESo-bMBI0rm4re4gGn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmCWt3uMCrIR19F6eAALce22IDnqgpiJDjIACR4H1bGXfB6ACBfkfuT0TBF5TyRwTKgZAIfh9srd9Io5ZVgqqaDL_cAtmp1P6xC_K0Et5dxzV9z7AXeyWs2ebbaelMHfVGssWwOTW2EHeetSwkpCu3Kw3OLwm1CNx_y__InFzrQRr9vHCqDaEqhKpNOvRrOEbPhTuPXKP7pJhKsYalBUNWI2WRHYYDQ_WR5Y4dGR0N6bG36JfetVM6b176yUptaLLIrl1Lr7xTl1Dwqp7wG7VqHCbQeFlH9Q9_H2elNjR37CGOrRiFmxzSU3W1TBN2fXozuY9N0COUYaVrO-LbIqPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdu39GsTS12lQiFf03M3W-lrSy1G8ZLr2UEGHV7G9tf41BqcetIxjBhvVCaGV4rVaO44AGI5mHMNB9a0RK-GhmMNpllS_tITjSgOItIRWXhWyvGJwjSAJ28OyxGBJTw0xqx-c9wi2F6pIqHjwiRPpKk_CkonQ18hCNnxevZ-aJlhjtDoBrcYoVQJPcjU0RlJkQyfCQuy-Fjx-AuuujiXgChuPCxmckHg1iSL-I4poE8KK3L8-ohte5s3gxSxADbTv-yO5plcC6o2lCcr8ygOotdi_qKbKeks59wnRhqJFE-GckegUu_w8mYk9OSze1G1G9bIDePHbjbckKOsk-0LiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزرعۀ گل آفتابگردان خراسان‌شمالی
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/456074" target="_blank">📅 17:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456071">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrFG_WgkHh8FnpjzuNFxantsfIHKoRTVpjSNkJO8ZROBeBFnalddzxQFX1BLu7lcLdtPGhHAYFJ7NF3ylTt4PYFzk_cU05xUv7WpUN8qaXL0nPa7Kk-CZ9AJGLU_Ci9ETtWnwgGtIgL-ZhL-TtsD_174uPkqN1QEAirONBA37gITCQYdm9ZfC0r_b6MepYiROFCgCm8OFhMUhGxWl7YQUTJYWVjJjVfyo8JZiT76ItaYTLxBUvSPXfhj_tqN84FWeW4Hv31ggwOAhaG8omXpoKEBLWkQt93YxuunbthLYDq277VE3C4k_V1WzLUWo1_7E4tj2eIm_zqBTqhqrOzMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez1PLyLT_K4UbQogJu9kaJbKTXUNMKPbo41rEnfPRIpHZQD9uAlj5uxhIE_d67JvtdplUPIJdHW3KiictnKbqBPa8BsHZrNimp9WRQlhAxQXsgOQR8l53oqYUke57eKdaslw_3cFpuGHLJzkorgA0qqsWgAfSdgoAxIDejHQ9X4oQCtdzLxeIxWUv7ODzS86FXkSG-UwJ7yr6xo1WePxw--_yh3B9dn2a0SsVH-ya92N3gtKGxELwSHFdG873LJ5WctUCCOiBZefb4djsDTl3nPAIipvHAxBhNdO-EwwFfKcZsEtz6rkcR_5tDatu9fOV-eRojRUHi8egBOTiOqcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7HU1fGmEUV2pRsN76s7RdA0gy0FRYm7TuyaA4A1iz7vYbuHtBHqP_CQlWs2RJTkUdFRPDdiw_zwcmI_KLIFf3BdmVG-XAc0D7VinDOgfi_17MOUku8q0AagPkKgd-V5RB0X7RXB6-beukC1kil2T0oZJq-u_Mq9XZvah0S8VTt0px0vQCiKUbuBOmfX97zD5JsYC17-_xa_vfi0jELISSqCChM58OseEYD4-if2zR01iVEC3jVzYeVmoAkIIEfbOgDXApFX_btYqMmXYW3hZG0VIHd_vb7N0s66wgjqetDnbHGFQQ1zQnXFSoWQ4rrUtLpp2nE1TDzL9n4PaAlkZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرچم‌ ایران در دست هواداران تراکتور روی سکوهای ورزشگاه یادگار امام
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/456071" target="_blank">📅 17:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f724812d24.mp4?token=YWYEzeCgBOsQeUPM6JMia2fvUl-xRxb8e895yv3a-QSwW-cLInyo8sNkrCNbqzBuB59eHyqATmT9GYP48HGYJGn3jtfnKmQL_YUuVgmeuYWIfgFMCglXKAmzfuRH08NzVCqFYGQxQIEE-XqeqpVIAd3QIQH9k6svJx70G72ELr4Dps7cirwImh0cdpUHCIhITi1comzMk1B3dNFupvrKDu4aKMwZ8ns_Hql3LgirY5CAsCGX5Y71EuXSVc7g6vGtCPj18-E1NT_ZFvl7lAARxgTBF9XIB-F7BCTwDdpA_ihzzMgjqfd40dWBOEtxFCiJyhyDvGQ9hDSE1yz_vfYOdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f724812d24.mp4?token=YWYEzeCgBOsQeUPM6JMia2fvUl-xRxb8e895yv3a-QSwW-cLInyo8sNkrCNbqzBuB59eHyqATmT9GYP48HGYJGn3jtfnKmQL_YUuVgmeuYWIfgFMCglXKAmzfuRH08NzVCqFYGQxQIEE-XqeqpVIAd3QIQH9k6svJx70G72ELr4Dps7cirwImh0cdpUHCIhITi1comzMk1B3dNFupvrKDu4aKMwZ8ns_Hql3LgirY5CAsCGX5Y71EuXSVc7g6vGtCPj18-E1NT_ZFvl7lAARxgTBF9XIB-F7BCTwDdpA_ihzzMgjqfd40dWBOEtxFCiJyhyDvGQ9hDSE1yz_vfYOdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️
🎥
تحقیر تاریخی آمریکا به‌روایت نظامی آمریکایی
🔹
ریتر، افسر و بازرس سابق تسلیحات سازمان ملل: یکی از دلایلی که ایران ما را جدی نمی‌گیرد این است که ما هیچ‌چیز جدی‌ای برای ارائه در میز مذاکره نداریم.
🔹
از نظر نظامی، ما شکست خورده‌ایم. ما توان ادامه‌دادن این درگیری را نداریم.
🔹
از نظر اقتصادی، تهدیدهای ما دربارهٔ اعمال تحریم به سوژهٔ خندهٔ جهان تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/456070" target="_blank">📅 17:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456069">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZS_-Z9asVwQHsEq3nchtta3mOo5djUfitUPBn4DpC7mU3kUHAVQUwlyLUMv8dqzm_kAED7piVsomRlJn-BbSLRmxaKYK_Z-xwyfI_JJIlKbbgC6ncd6RJ7Q6hjssrYuC_X66CeYbECHZCloazeoKZkAj7HHr7syaxGO_f3rtZi-pLPxf1QDKnhrfP5B3wQeWWMxnwM-a5ThEiHCLju1LnAM-VWcoGltd0TaDCDRHiUOU4Gb2jNA73SOrPlLRHbWe_TXLuQTEX5-TaK8v3qDnYhS9TaZWqtBX7Movn_PcImQrxEkLQLW6vneHKekANZBnbh1Kh48KQhyg5sDFPHAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باد شدید و گردوخاک در راه ۲۳ استان
🔹
هواشناسی: از امروز تا دوشنبه، وزش باد شدید، خیزش گردوخاک، کاهش دید افقی و افت کیفیت هوا در ۲۳ استان پیش‌بینی شده و احتمال خسارت به سازه‌های موقت، شکستن شاخهٔ درختان و اختلال در ترددهای جاده‌ای وجود دارد.
🔗
اسامی این استان‌ها را در
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/456069" target="_blank">📅 16:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456068">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2V-Q5apXwaT_R29dAr76S2nXPw3ARkzKetjqdkw_3WOvlZcdHB-1YkARyttnY9UwPEZ1J_tUm1MusMpq3F15HO4Tc8I2OBLq489a43B3GJQ_qNJC-NJfihBfXNowNZAhCsMhJYVHkcPbZsYjCAswbxvlA3k_UcTqQkprh34a-qjqCs9lQghGuG0MznpSbp9Mat0B3W1x6xM9dCYbN-ZzUcCprT8gREfJDmnsLAlyxtppPDRqDXkjGlgBU2RFdf4gC-9N6h-QH3NZDOaBhAsRMHlpzc8FuPH4SYlgwuE3NoHYYC3azSeujfi9CaH2R-ceYpsN4oWMW-env7igtP5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناظمی اردکانی: بررسی لایحهٔ خزر به بعد از جنگ موکول شود
🔹
دبیرکل جبههٔ مردمی ایران قوی: اکنون زمان مناسبی برای بررسی لایحهٔ نیست و تصمیم‌گیری دربارهٔ آن باید به بعد از جنگ موکول شود.
🔹
سهم ایران در تقسیم‌بندی مطرح‌شده حدود ۱۳ درصد است، درحالی‌که پیش‌از این…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/456068" target="_blank">📅 16:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456067">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ebef483f5.mp4?token=e0BjJu2zhRPhVLFLwOAn9FO6P5On589ruOTe4JfQM_c39deljuADAgbI-KrPqnYwiMVO2hdQpANlDukdB6XtUeHvUmSfvyR2kp9xuE-NzMvJgL6TpsHxX9ohq2JdUjRSCULNKeoT3gC_a0uNzscAKFlDD7gEum_C1wyZi7iLR7S8zrXjHGcULBUJ1yph1GNAWHiNk13HnRtbfYM_IuOHuWEmskBOQKkXkGcHI6wD8uHIXgZ9YALELQtfomZw5LNqq97UN94O4Q4dKyhifsx_7zi6paqdkLffVlN6xGlzCQt383kk8lqh8IPTjKS2fz-uEy_nroQG5OOreJhIH5xkaE9C_ZgqUuWAbR5fqYBOXNuylJb3PX6iHLXEv1oEiqu7ZgY0SplGQM2iH8Tw0FK1KuYeI5StrepwV9B4yFpWLPOY99_iVra129OcGlDnGy6Y1r1n0NULroVuEpb2ps7ytKBZv_LzXXQvV19iAJnQkE8VEtIo6Q0y94JubctGOC-OyliGlHPVJRGXS2Hz0OEDzybhESZ8jBTY15jHX3LseuBHDaxjax3-Yp2c4BpDA6nRsU4T1j8D6rYPodyO-tw9Ng2Yg79IA7M-0fy3C5A8vi3m-R9CG7U0ASbPEAdwW_-b5Hf8Z1hbA2iCJFHKOKPMLc_vZ_j3d2osNVjZ-tVciCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ebef483f5.mp4?token=e0BjJu2zhRPhVLFLwOAn9FO6P5On589ruOTe4JfQM_c39deljuADAgbI-KrPqnYwiMVO2hdQpANlDukdB6XtUeHvUmSfvyR2kp9xuE-NzMvJgL6TpsHxX9ohq2JdUjRSCULNKeoT3gC_a0uNzscAKFlDD7gEum_C1wyZi7iLR7S8zrXjHGcULBUJ1yph1GNAWHiNk13HnRtbfYM_IuOHuWEmskBOQKkXkGcHI6wD8uHIXgZ9YALELQtfomZw5LNqq97UN94O4Q4dKyhifsx_7zi6paqdkLffVlN6xGlzCQt383kk8lqh8IPTjKS2fz-uEy_nroQG5OOreJhIH5xkaE9C_ZgqUuWAbR5fqYBOXNuylJb3PX6iHLXEv1oEiqu7ZgY0SplGQM2iH8Tw0FK1KuYeI5StrepwV9B4yFpWLPOY99_iVra129OcGlDnGy6Y1r1n0NULroVuEpb2ps7ytKBZv_LzXXQvV19iAJnQkE8VEtIo6Q0y94JubctGOC-OyliGlHPVJRGXS2Hz0OEDzybhESZ8jBTY15jHX3LseuBHDaxjax3-Yp2c4BpDA6nRsU4T1j8D6rYPodyO-tw9Ng2Yg79IA7M-0fy3C5A8vi3m-R9CG7U0ASbPEAdwW_-b5Hf8Z1hbA2iCJFHKOKPMLc_vZ_j3d2osNVjZ-tVciCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
سفر رئیس سازمان بسیج مستضعفان به قم  عکس: حسین شاه‌بداغی @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456067" target="_blank">📅 16:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456066">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ii4lQA7e423T-MQBc-U1l6C87S7E0enJ7KI_ul2jsy5M7zpsLG1YT1vvdgOVifJWMMkcaJosFWi4uSrdrElFFD806Prhk8HMbn8FlqcoO2VakVEZqkpmDcbx5-B7R_6zyKoPjMICJfRWFfuxJF7L5q_fSHKVKc50EkCK6qsEc6fYhxucuiZ5IK38hZLYGYxKDL-E9DunfLtmz8tO57uLHukZZKZV9_cBCWl3NLeBdDLV2_f7NhK5YTYkolVdrrgqk-Cr9ipwyah6mPUW8Uh-JK_DMsrhsfyf_ImDSNhSbVxMANX-CsbO87DLSxCffEW5Bl1Jt4Ok04NNI1UKmWiu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف محمولهٔ ۳۰۰ کیلویی تریاک در اصفهان
🔹
فرمانده انتظامی اصفهان: در یک عملیات ۳۰۰ کیلوگرم تریاک در جادهٔ ورودی اردستان کشف شد؛ یک متهم در این رابطه دستگیر و خودروی حامل مواد مخدر توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/456066" target="_blank">📅 16:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456065">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2N93xDo8j-b3yOHJV1WgSrh0Ic19MTNWLgki-2ADyw475smNx8KrQn8qRDYug4fHwPD2ftWxO5CUaXszz56ytxMrTbp-hIGhc6sH8kPhtu5yJzSUZUckhsGtnCj2PQr6peC-GH91n7IiZ-dbxvgDHaeIr8YQ5SO7Gd-EZdIqbtWW2jD2VOdQ4S_EZgGwjDJabqGhLUZ5eielDiOYrYk27QRINCj-9uTVloDp0FQV4-OM2XltZOpLC5SuAzt1Qyg9t45z1uIy09mA4bY1a7Ja6rqfXhn2dUcccmmqfXe8q4ajJ5D0-LnIZiReNJIuIT0XGA4hzCmTzgdHPKWRQgYSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پکن: رزمایش تایوان صحنه‌سازی برای جنگ است
🔹
وزارت دفاع چین: رزمایش «هان کوانگ» تایوان نمایشی پرهزینه و بیهوده است که هراس جنگی ایجاد می‌کند.
🔹
مقامات حزب پیشروی دموکراتیک نیز بی‌محابا به هراس جنگی دامن زده‌اند و تلاش برای تبدیل شهرها به میدان نبرد و کشاندن مردم عادی به خط مقدم را شتاب بخشیده‌اند.
🔹
ارتش چین در حالت آماده‌باش کامل به سر می‌برد و به‌طور مستمر توانمندی‌های رزم واقعی خود را برای مقابله با تجزیه‌طلبی و مداخلهٔ خارجی تقویت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456065" target="_blank">📅 16:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456063">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4JHNKj-stdxexbqFh32FyUxgBCPGGmu2yju0nNSXzk4zMHRyHh6a0u1eZTa3DMh30TujR8J9rClDum3Q82hsIXkiZeBUzZGI_5oGWLHQnzY3a03a_qhpS_jiT2HQ986S2B2ynW7wyv2kZYx5dJBIpPvIYp1KNDRYX20C1WAkHciESGx14JR0bsPaAgJo-eVIYJKaXf04Hb1w43n1Q1BU_w5mwCg6XJzZycntWRurUBYr6IIuY7N5WYh9KLCpqrObvyvU9fWXfMIJk4W59KoB7QD5TTB2efoL_8wiWlL4KPmAJIzlqzSdpVn5rd3rD5Xa8iH7hAhketiL65is15DSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حملات هوایی اسرائیل به جنوب لبنان
🔹
شبکهٔ المنار گزارش داد که جنگنده‌های رژیم صهیونیستی از بامداد امروز تا به الان چندین‌بار شهرک المنصوری در جنوب لبنان را بمباران کرده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456063" target="_blank">📅 15:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456062">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFOddxujZ5jtAqYGaGnIHPj_NOkaZsCmq2H1LZ8KEW85IQDCFNQJXvUK3JilrTqtoYXE2aJUprZ4VHNuwirxfukuOMKFpuThrqEr3UmGqe9nIs9BZ44I5HKOZxgfYlY162sQLk0g_mi8vmdyUR0vCYHebVNknZq52Lx2SHr4x9mjb8i-dS_DKJABVD6ZQqlQFm9VE9_LfrwM3IaWi-RWw1W0W98wWUkb7_3dYPxmO_NgrI6j9NFEK6JojduNmhrLG69nOr6KioRfecJ5-N9ejdepkgy2cdjIBw464RcVC2hhF2DtI5q5GVhqRzMALdDtU6c2Jg-1YP5EXZiRmBTreA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصر، ترکیه و عربستان در رستوران تحولات منطقه را بررسی کردند
!
🔹
وزرای خارجهٔ مصر، ترکیه و عربستان سعودی در شهر ساحلی العلمین مصر دیدار و دربارهٔ آخرین تحولات منطقه از جمله تنش بین ایران-آمریکا، راه‌های کاهش تنش‌ها و تقویت همکاری‌های امنیتی و سیاسی گفت‌وگو کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456062" target="_blank">📅 15:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456061">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5-Q5NjjiLREGSatihJvbpJbqspI09RHVmjNIhOSq2LjuovWj_2OzTpV6ZMf6ryJvTMnzP6M-GRqOmAsTqnxzn7lmibW6hhJ1Fx3sELBVOI14NNBt1hsydDRoB1wcCS9Wagt88RRto_I-5PxyZoLn_wJmc61eAOcAcBji3iPmN0Z91FfMMGwsFU085_hz7WgIQizwdY_gk_P_Fv3BVgH0pxEHDNRrb_wmgJXXo1suicHvMKiWEnU8bvpslwAnHLwDhlINj_7DsgsefmlSWZoyf57yKhqIllJY4E_TWdTQtJuOYDeNOfrFjVdW0363TwIQFXbgXfN1jCMgTuCQHZEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج تازهٔ جهش هزینهٔ مسکن در آمریکا با بسته‌ماندن تنگهٔ هرمز
🔹
فایننشال تایمز امروز گزارش داد، تنش‌های نظامی و دیپلماتیک میان آمریکا و ایران در هفته‌های اخیر، موج جدیدی از افزایش هزینه‌های استقراض را در بازار مسکن آمریکا و چندین اقتصاد بزرگ اروپایی به‌همراه داشته است.
🔹
این افزایش ناشی از واکنش بانک‌های تجاری به افزایش هزینه‌های استقراض دولتی و تشدید نگرانی‌ها نسبت به بازگشت فشارهای تورمی است که ریشه در تنش‌های ژئوپلیتیکی، به‌ویژه تقابل نظامی و سیاسی میان واشنگتن و تهران دارد.
🔹
همچنین نرخ بهرهٔ وام‌های مسکن در آمریکا به‌عنوان بزرگترین اقتصاد جهان، بار دیگر به سطح ۶.۳۶ درصد برای وام‌های ۳۰ ساله با نرخ ثابت صعود کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456061" target="_blank">📅 15:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456051">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/roArX45KqZf9vFBYEaWHDRJQWXwZIl6CgeSVQHtA5ysIv7ierQq0RftinHxVnPHG1z6nMPjW9bVOZHIk2q0daUOmseYq91eYM2zhS8kxrrMMwVQEkVDajJBHa21LHBOUdEeiZKekA2WD1AbiDgpFVsGXhpeDhhuXUCTOkoL4vXINFfmPsY4RQdRiZW9k5pjO6bWDvgDWkl3RxNq-Zi9BHWu6bI15PNUe414PPkh5NQ596zJ_-rLmhJDt2WyYXdjFXCI9WmcAvQQWeXE6xyOOKqkd87Goh8Z2-QKEaw4yPD07mp_hF_vQw9A3k3uyLlGjWVZHzvdQUDYA2EpHGf3amw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqf9CcaOWc59-x_qLAxCueOo0ecw2cnOOm2NE4qRAbmL76Q4_SpxpuJrDgXBVT8dsguDpsWHwB_g_mIGtdfWPg-bk4d1Pbg7h7jfMkbP-2vqRjhT6-8eG6RkNRqBtqc2pWz19Tyc88kMV1SeGBiUTE_-0TkCg76F4T8niJS14tRyThASkYl3POOuHqFcWbUvn5TlNP43Wd1xljvBc5bg_Yj3NduXmlUBJ4eZn62-mbWdBKXiYCfdFZlQKGe4vfdfWtTLiF5tmAVYLtNpCE1_otv3fxylffRToX4D1sMT1ccj16-JkJc_zMJwaarSyO6I4Q_2Vh1X9cAPDDta3yuViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBvPJWiqhVSTeu6TR2x5gIqN-mdcSyIggd66HsNJj4E9y_7NVuaWsrDT7Gcm3AqB6j1CCjSEAyw21OTygpTi9LeG4ACy2dlg5l6scImz4CrAByd80DPvKtTiagFKYHnb8Mj4lrba2Xh1UDcEGUS1FVZno78YA2AZmwMZnRVLwoFYuoaa_cC8qKA_ZCzTExCwF-qT6kZdWKed1fpDtiCTMr2Zet1muqUW3ETg7n-EDxEtaassvnnM7cOZSzD54Bh9D_J2_91c5djkY5TbIQzmJlAsOAjpB-0vGLY5dJ9ieAW6bB5e4-1NyiAqWCF0O8_XF_ujregr76I_yk9zyF7yQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9IY4qygm4CvrCCOSTx-yErTf6_Y45paiCOL20S6cPiJp7U0h2KaS-_cDOrSvvoeLlYCGN0twxv5l552BH2O9mfMelg8Jjb7iHfyjW_3TX23wfdZ167f42WIr3PyClgpifzxvtTofldizT6ie3ybxeO1G0aBxzeA8LWYvWbSceyE6CuaoD1k_rMTvaLNN06XMb0XMbzWEF9G-Tl_taGOldeafw2kcNFxJ785ofHBt0VDveZmI8qfE-IYISmkT6KCAkj0yMNQ19m_OF0tp6QCUdBVIBisdIOzPv62R5niilI6RWNFelaT_TDlDoGP4pNmAiO9QsIDUuzfXtLYb0ur2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpOPCdPxDblSjFdzyNreImIyd12g2iW7BBIZPB3-nur8qm7vHpl5aD2hHYI9l_P0bjX_POytO7Im2YB99h-m6-Xc1l3QtzlNmEb_Sp856tUtMcSMYc3eOxv80aucNU1wLzul7Qy6ccm8bfpmU-zqvJpZn7rYuNPRxGvCaP40vIYfR3QYXg_0kCtO4OJYLxgzP5BBXthVkxkY9O61HdLNLvHayfoNNhH6Qj5AtgpA3JlZ-tEvqSJAPYWjHRdFnCAcipjlufv8ot0xpafL2guUPZf8O3bDI0rzFFJISe4pVBVP2x6iDsLOXuHuUOq603nh-w3sOR-HojMKz4_F3IJaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovAnmqJiINsGQhKDRR35ajWIPeBzmf3Mj2jWSTcjJjYK1gpCRXBlIMdGJvp2ZiA7KUXHNEyXlZdoaeKw2D-rCRNNux43-A_xivUVwQk2Rk9fzNsSy5ucr9QxHGRySqk4DV0plm5VQdyGYRKPIkHieyky6wODDWLJW9-q_hqn1FAyt6m2m29B9wLpl5CO5f-SReIaGkv2Em69bm8x_DCGLAj-Jz_znJ-NOBPhX7Fj7p6iAUrRDoSHS3_Yax6bngjIq2snZeFIlSCBCdtJY-RZ6HNb2couD1Ffa8mMXaUWeGCcUpTT40J95_dL-raN79rlkdpPkKjWxb8M5rAedyXJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KoSHOp1t6oP01aSsUt9NA_MKH-XRgKz0SUJjJhoK_aDRsao04Ji1azuR49MXkDY3A_rF3nRUO-dow3u1tHinJL5TlTPkDoJqbi_RUydUGbfsIAGB936NzkS9RFcjieKvch8ts4AT6zyjMQgWhmVUvLes1ixU_IXRYbuUx4bRX8bcnukV95FXio223hpAkUqn8W1OpouuCgPoMTKm_IDOXItSnrXHhRx99XdTu9av3T0O3Juni4MBcoggMloO-LuKbma6Aw6fIrB-JWcUVHM9HntTmky3RLdZkAclXHy92P8TmW5oxpdQUJu--MKAG9w2DGXyNpz3RoacGboDzs9Xgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pImYVWa3rTjslvG9yUwlFJzUvqcRgKRAHm26B6FCBPu33ce7mg4HPxF5u_T91V297xWftvhfRjlxfsj1BV8TKmaBc_1C8wlw9znrgyaNZj9GE6qTik0EL9whsh2jmQwLXhi7KW_JnSqXWLC6-CgN1CBWxBbo3e_BnHA9zcXf6YmWLJf6HSBHj3HzyakdhoaC19mTtRykGUhVPb33NZJpqE8zzu7EGQg1qCXE9zkVY-VluEEu4biRTbjqlk3d1nXYgNmu4zsIzMRvczlNQUcXoyRHdRciFqiNwUy0eIK9SUFKzUp1D2P6VkK9xOZJTzbyL_eNPKPZQwA8tT2HN3w3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBAMvb0jxeaD3IKs-HpbGyA1Xkt-vatM64RMRd-ylVGHVwTnO-f9hlQOrDN3o132HU7uTwk1v8Zji-S4tXd9lHxVHIcWbufjGYehNwcdDHj6oJL01571clvU8ttgJvF8oyMpkqQfcLIIMVSy58-3G9W0sqjgWg3RNwiPnS7TkGR4aieDMYElxUyqvI_EJzrYXJ0MGRWHgffndKYe5ovDGBG3QZLReDAyQdqi9mTgw2Y3wKz-Oje7wct_E1YhsWdnOK8z3NnOeaPo772t3o8CqM5lPWCkmYW-JBfrPphP6yYKMx8Crp87r4mQu4QAb6AmiduXT0LyrpA6TLIH7ilQVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JK6kvRiJB2CDHRkJGHtWvOcjKkWed_06k_fkRkz-mTUKIXOU-mpH-QL0M7ZIehYOpqby8EPirDwdlRoBG8OS_7aIMmslkX4g7D32yJQS_7hxLdgG0eRHUSnGUX6kSu24vR_99lt157BrHd9ufigvHOa5AQaPel9ix8D9Ir3iu8seC8y0urDkblTzEPljsHxvuHjk_T996qTE8lxMYd-YCMmA6aQGyA1Gx4STu6HSojCyHBiFKJBB17M05WzoDnn8_S6QOssNfH-LUskIOZcPERUBjK30_OaeA0dCFZkmQ8yx4_gYZ6hC6Nn39Hta_LTTzrh3y1NeTPrYM0jMFIc8qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
زنگ اول لیگ برتر فوتبال به یاد «ماکان» و شهدای میناب
🔹
بیست‌وششمین دوره لیگ برتر فوتبال ایران عصر امروز با برگزاری ۶ دیدار و پس از ۱۳ دوره، با حضور ۱۸ تیم آغاز می‌شود.
🔹
بر همین اساس، برخی باشگاه‌های لیگ برتر در آغاز فصل جدید تصمیم گرفته‌اند با طراحی پوستر و انتشار ویدئوهایی، یاد و خاطره شهدای گرانقدر میناب را گرامی بدارند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456051" target="_blank">📅 15:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456050">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohcMlk0XXSIarfiTPdEf5jFB-SwitzwaMBvhV3NyDf9waT-iNgJI8x2FiUavlyHuawYpkoA2V3neZZcNi68vhpa0TX2ZjttH9t_HUp5qgJqBvVoshQxWM4FUL_pfyxgKk7iLI-GivcEdBhyVzGI4PxmO8QBdWuIHoBrjTBev_VK537wsTOpsAOG8du6K6IjOPpYM341Cycrnx8FnPcXjnydKojl66jCGs3W-4pgbhaQ7oelQnZEp7ANEcnyxKsL-pVHzzmCCvRv8EG4EwzN5fIk8I5ftsliKJrb8AtiUP_a_Tgyfz0qXdmr2CqXhvDIj20rwH1FX88gYSWrrcH_CWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت‌سازی رسانه‌های ضدانقلاب از اتفاق حاشیه‌ای مشهد
🔹
روز گذشته ویدیوهایی از برخورد تعدادی از عزاداران در مشهد مقدس منتشر شد که در آن چوب‌هایی به سمت هم پرتاب می‌شد.
🔹
این فیلم‌ها بلافاصله با آب و تاب فراوان در رسانه‌های ضد انقلاب دست به دست شد و به نادرست القا کردند که این درگیری در صحن حرم مطهر امام رضا(ع) رخ داده است.
🔹
بررسی میدانی نشان می‌دهد که این ویدیوها مربوط به فضای بیرون از حرم مطهر است. در داخل حرم رضوی، اساساً اجازه حمل هرگونه چوب داده نمی‌شود و محیط با بازرسی دقیق کنترل می‌شود؛ بنابراین، نسبت‌دادن این اتفاق به درون حرم، تحریف آشکار واقعیت است.
🔹
هرچند اینگونه تنش‌ها میان هیئات مذهبی رفتاری پسندیده نیست و انتظار می‌رود عزاداران با رعایت بیشتر اخلاق از هرگونه تنش پرهیز کنند، اما در هیئات و دسته‌های بزرگ بروز اختلافات سلیقه‌ای در نحوه ورود و خروج یا خستگی ناشی از گرما، امری طبیعی و قابل مدیریت است و نباید به دعوا ختم شود.
🔹
عزاداران و دست‌اندرکاران هیئات باید بیشتر مراقب باشند تا این حواشی، اصل عزاداری را تحت‌الشعاع قرار ندهد.
🔹
با این حال نکته مهم‌تر که باید مورد توجه همه مردم قرار گیرد، دلبستگی شدید رسانه‌های ضدانقلاب به بزرگ‌نمایی همین اتفاقات ساده است.
🔹
دشمن به‌دنبال بهانه‌ای می‌گردد تا اختلافات را نه فقط میان عزاداران، بلکه میان همه اقشار مردم دامن بزند؛ هر جا که وحدت و همدلی باشد، سعی در تضعیف آن دارد و هر جا نقطه‌ای هرچند کوچک از اختلاف ببیند، با تمام توان آن را به رخ می‌کشد.
🔹
این رویکرد دشمن نشان می‌دهد که درد اصلی او وحدت ملی و آرامش در جامعه است؛ وظیفه ماست که با هوشیاری، این بزرگ‌نمایی‌ها را بی‌اثر کنیم و با پرهیز از دامن‌زدن به حواشی، اجازه ندهیم تصویر زیبای وحت و همدلی زیر سوال برود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456050" target="_blank">📅 15:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456049">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
انهدام پهپاد MQ9 در آسمان هرمزگان
🔹
یک پهپاد MQ9 توسط سامانه نوین پدافند پیشرفته سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان هرمزگان منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/456049" target="_blank">📅 14:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456048">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58068ad65.mp4?token=uGb4PjLz49C0pES-ZPZygkVXk3GR34dWauJQfAMhAmo93CFeEl7_IbtcRnkMwMbSTwNZvu4B9Kzn3rybvEmH80ejms8pnzC-aKvPPHdh0RIcgySEFGv2ly_ly7gY1Bm5CDVLoOhOJaiHX8j-VZYp2yfBzDiWEbCT2svKj1f5VCwA_T8BZI221k6R3bGSGk0CVFmkMHWo9o82TA0bQJsLfQAMVhLFOZAIRsn7LHZ3KF4jAqwdz0tG0U0R04s1hYLNGC1hw0d7KvFyegr1s0wJrSlEy_40B1lwW1aeaLA8qYnWJF11ob-Aj41ScZZLZC69fUu_m3ELnAesNAFaIT0uig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58068ad65.mp4?token=uGb4PjLz49C0pES-ZPZygkVXk3GR34dWauJQfAMhAmo93CFeEl7_IbtcRnkMwMbSTwNZvu4B9Kzn3rybvEmH80ejms8pnzC-aKvPPHdh0RIcgySEFGv2ly_ly7gY1Bm5CDVLoOhOJaiHX8j-VZYp2yfBzDiWEbCT2svKj1f5VCwA_T8BZI221k6R3bGSGk0CVFmkMHWo9o82TA0bQJsLfQAMVhLFOZAIRsn7LHZ3KF4jAqwdz0tG0U0R04s1hYLNGC1hw0d7KvFyegr1s0wJrSlEy_40B1lwW1aeaLA8qYnWJF11ob-Aj41ScZZLZC69fUu_m3ELnAesNAFaIT0uig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از بقایای جنگنده اف۱۵ منهدم‌شدهٔ آمریکا
🔹
افسر ارشد پدافند هوایی سپاه: این جنگنده با سامانه و موشک پدافند هوایی نوین شکار شد. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/456048" target="_blank">📅 14:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456047">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NARuTTFG23iRsucc8HuKqbRaERrn1GsIan1E5sSzMJ--ayRw91UVv-XKoFumIqmEino9hahwcmshgPRQdHCUO5fBK-EPLgs3hY7kxve1kYMExL_5-tYkbuZgRjAdhHH4JkPNmh17h_62RBjS2P_H0Iab4IXOrQilp06q6Pe9IKGBJMbr-nrN1s0Xi_L5zYOgRwAK82fqc8q1tRh29WyGAMWkYKnk5APeLRvh5-4kiUjj-2f2OBMmwHLUhu_0_Z63SK6svYLlu4lpR5DR4QgWJ4kxtjf6Y6dupSC-TvW3Bv709-LQZrfOqBA0HMvzUnqa0N7qhNgTmNVBga37VGj3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه طرح توقف حملات در دریای سیاه را رد کرد
🔹
روسیه پیشنهاد توقف حملات به کشتی‌های تجاری در دریای سیاه را که از سوی اوکراین و با میانجی‌گری یک کشور ثالث مطرح شده، رد کرد و گفت مسکو حاضر نیست به توافق‌هایی بازگردد که به باور کرملین صرفاً به کی‌یف فرصت تجدید قوا می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456047" target="_blank">📅 14:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456046">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2252485e79.mp4?token=e3jQ_TZ9SSBv7axovLVifc6liETZAGlICqt9N-nJQNsxwolVjDjb5pBqNdN_vSUkjYgDAgltuwRszOVdcjpGcj3Ltwv14YVYjiz0ZKUjXNgACAFW7tqshayQ9RU2FIpnOOPDotvx4J8Grl1EsBSVZjcJAvwTdL-xgDkXizNAyimrGB0VtwxDphZhNfCdNZEiSc7f7eoxcBx38FYPRQl3VAASuEQht6kGSnKkFlxB4briq4WPj0AE479APKgx_4Hz1GO5ea0_ZHU7v5dfaTifqsAKoqIgjWt9KXLzj_snbzfEmFCPKl20Ccj8N8zLKOMm11PsUgX78rwkrX34mVLRjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2252485e79.mp4?token=e3jQ_TZ9SSBv7axovLVifc6liETZAGlICqt9N-nJQNsxwolVjDjb5pBqNdN_vSUkjYgDAgltuwRszOVdcjpGcj3Ltwv14YVYjiz0ZKUjXNgACAFW7tqshayQ9RU2FIpnOOPDotvx4J8Grl1EsBSVZjcJAvwTdL-xgDkXizNAyimrGB0VtwxDphZhNfCdNZEiSc7f7eoxcBx38FYPRQl3VAASuEQht6kGSnKkFlxB4briq4WPj0AE479APKgx_4Hz1GO5ea0_ZHU7v5dfaTifqsAKoqIgjWt9KXLzj_snbzfEmFCPKl20Ccj8N8zLKOMm11PsUgX78rwkrX34mVLRjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از بقایای جنگنده اف۱۵ منهدم‌شدهٔ آمریکا
🔹
افسر ارشد پدافند هوایی سپاه: این جنگنده با سامانه و موشک پدافند هوایی نوین شکار شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456046" target="_blank">📅 14:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456045">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c86100247.mp4?token=pNdpzAjeVdmR3JJpki5ZP6BGeFEXI8YZzz4r4XhJxTGU4VRDLcWzVbcSpsNP-7vVr0Sl0vyLcIzDz-ecbZgL2EZ3_NnZ2EGCJMp3eqw8bsM5q_Uq6H6oFEn4K-tiA1abSEDrJSss-vVuqZ5bunVEntJ4EVrYfahySCBAIUNksgRzLLYTXxaHihjbIg8M6Oqa7yNCGsCOz-RHYwWBEfN_5izSzgihTYVzVWDpGX6zzeysL_EevA60eS77G1KMEgPtNA6kuik6odfmYl2r9-03Kox2HrMESLKC4WDnFgyChBypeGebZouqn27XUxIJMLoCbD1jPiLBjH-BoY2Fv_vKlCL2V_JwTDtOS9tkJpPkqQln0rAxr37F15gkTjiQe7TDwfXv5KRKGgknGf3eWA3lpuuRCHgtZCtmjm6tr1ZsNr4iAfAivb6lgErKifq3vYvd9zJQTV3ElIndByz90Ty2lSLCnBTlqN-zG7QaKwWUPjlJOVsoNeM1BnwfDHRqRZCl2jXnqPpF4SEg1mTkgwuoWkxpZEYudp1tGoFiO2sZ-5j8pAoxKCuJ939p9jm60tS93hfO0jIMEoS9lztqmTBOnbpo2W4uvJ0zip4UvgMBDNCk2PTszv4ApjQsJegc_Vt_K38eZcGK1vRaaOpV_0WhDMgY_TfDbedPI39wPgbIvho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c86100247.mp4?token=pNdpzAjeVdmR3JJpki5ZP6BGeFEXI8YZzz4r4XhJxTGU4VRDLcWzVbcSpsNP-7vVr0Sl0vyLcIzDz-ecbZgL2EZ3_NnZ2EGCJMp3eqw8bsM5q_Uq6H6oFEn4K-tiA1abSEDrJSss-vVuqZ5bunVEntJ4EVrYfahySCBAIUNksgRzLLYTXxaHihjbIg8M6Oqa7yNCGsCOz-RHYwWBEfN_5izSzgihTYVzVWDpGX6zzeysL_EevA60eS77G1KMEgPtNA6kuik6odfmYl2r9-03Kox2HrMESLKC4WDnFgyChBypeGebZouqn27XUxIJMLoCbD1jPiLBjH-BoY2Fv_vKlCL2V_JwTDtOS9tkJpPkqQln0rAxr37F15gkTjiQe7TDwfXv5KRKGgknGf3eWA3lpuuRCHgtZCtmjm6tr1ZsNr4iAfAivb6lgErKifq3vYvd9zJQTV3ElIndByz90Ty2lSLCnBTlqN-zG7QaKwWUPjlJOVsoNeM1BnwfDHRqRZCl2jXnqPpF4SEg1mTkgwuoWkxpZEYudp1tGoFiO2sZ-5j8pAoxKCuJ939p9jm60tS93hfO0jIMEoS9lztqmTBOnbpo2W4uvJ0zip4UvgMBDNCk2PTszv4ApjQsJegc_Vt_K38eZcGK1vRaaOpV_0WhDMgY_TfDbedPI39wPgbIvho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیاتی از پهپادها و جنگنده‌های شکارشدهٔ آمریکا توسط سامانهٔ نوین پدافند نیروی هوافضای سپاه
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456045" target="_blank">📅 14:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456042">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146f452f88.mp4?token=DiRRdDyFKdBQcl84uHxGab-ro47t5E6I5coE38e5N0lS7jLJ9YY0wQpppKa9dFBC2sleZpYrm-sgx8eurLy73HJqhNJYyYyR7C1TaqkwUrPDBWGeF-6wOMBxw1N9kR5Dc4ofd3_MDqiXdNC-5cV_kWJwpa2thCxHWGNxQEWBhYPDpLkCxcZQlt-jnKQkwyInjznGPS5wgItmKdubLE2JgXH5WLryilF9cmgDY6a0HAz2xdrfUl0X7JCicwThsC5RAOffgcNYURORt0FQV_UUUreYKPP7dYLtmwHm7SFLd-zJN41fNuZ-3BBi0c8IgIY2rW-_7SfvElA3t3llGv5okoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146f452f88.mp4?token=DiRRdDyFKdBQcl84uHxGab-ro47t5E6I5coE38e5N0lS7jLJ9YY0wQpppKa9dFBC2sleZpYrm-sgx8eurLy73HJqhNJYyYyR7C1TaqkwUrPDBWGeF-6wOMBxw1N9kR5Dc4ofd3_MDqiXdNC-5cV_kWJwpa2thCxHWGNxQEWBhYPDpLkCxcZQlt-jnKQkwyInjznGPS5wgItmKdubLE2JgXH5WLryilF9cmgDY6a0HAz2xdrfUl0X7JCicwThsC5RAOffgcNYURORt0FQV_UUUreYKPP7dYLtmwHm7SFLd-zJN41fNuZ-3BBi0c8IgIY2rW-_7SfvElA3t3llGv5okoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ریزش تونل در هند ۷ کشته برجا گذاشت
🔹
دست کم هفت کارگر بر اثر ریزش تونل در ایالت اوتاراکند در شمال هند جان باختند و سه نفر دیگر همچنان در تونل گرفتار هستند و خبری از سرنوشت آنها نیست.
🔹
به گفته مقامات، در زمان وقوع فاجعه ۲۲ کارگر در داخل تونل بودند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456042" target="_blank">📅 14:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456041">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7618ebcf0.mp4?token=XjRLreM36s6a7QKprBF2TKOrzSeeZKy6V7EYu8z3iR_cpHfWh867EZqKQy9VfsNMO6g4WPqNP4b_j5Jiqz4GodA_-3Ub8sSrXQJNEH_MBjyGXZg1cG9M4p4RMRe11BC-6vc6uePumJRwbiNJzg0IxVtc055d7FxRDv-m0AYYGl2kFxjTERFWzetC1OW1naycTunxMqOH0Om6yTUWAaGQbsAsh40rvbMrar5mh1VxdPjmuyTAb2IwI9-b59E_YHhMo5sd0O0PGgtXsFfIxQRV727Jw38xCEmzPah5UoEK0NHEg5OljU7_F86--UJR1SDgXi6MTebvem6RT7FsCFP9cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7618ebcf0.mp4?token=XjRLreM36s6a7QKprBF2TKOrzSeeZKy6V7EYu8z3iR_cpHfWh867EZqKQy9VfsNMO6g4WPqNP4b_j5Jiqz4GodA_-3Ub8sSrXQJNEH_MBjyGXZg1cG9M4p4RMRe11BC-6vc6uePumJRwbiNJzg0IxVtc055d7FxRDv-m0AYYGl2kFxjTERFWzetC1OW1naycTunxMqOH0Om6yTUWAaGQbsAsh40rvbMrar5mh1VxdPjmuyTAb2IwI9-b59E_YHhMo5sd0O0PGgtXsFfIxQRV727Jw38xCEmzPah5UoEK0NHEg5OljU7_F86--UJR1SDgXi6MTebvem6RT7FsCFP9cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور دستهٔ آهو از مسیر پیاده‌روی مردم شاهرود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/456041" target="_blank">📅 14:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456040">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d3c41147.mp4?token=WURhRAI9Y5lo6BZ7kr3cmLQPuR-ITsicoZ0qqHTO1kfNC53E1xxgPGVyQ7aN8VCUNLkHeuU3rofzJWzhGbyWhC0m--amAjKa1H-UGWqLEHX0epIqzxK0rmx9JeBMp3YKMkgi4He2pC8gZxHS-3Ym6briXAPuJmacOQJwcHf_nTo0lCSjZvPK7vg2k0NuiWxeRNUJ4gs8tegTRPXasvI9SW463qWar2OSVCBP020_aNZhaA_GyrW3lOwmjTVY1WIMawO82IIcorhCuRiLIF7Z62YUBu3-BRXIBALNVZcGtbcRm23MiXUVm8Binh0ikOK4PuCnUVE2fN6bijnoTSt3vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d3c41147.mp4?token=WURhRAI9Y5lo6BZ7kr3cmLQPuR-ITsicoZ0qqHTO1kfNC53E1xxgPGVyQ7aN8VCUNLkHeuU3rofzJWzhGbyWhC0m--amAjKa1H-UGWqLEHX0epIqzxK0rmx9JeBMp3YKMkgi4He2pC8gZxHS-3Ym6briXAPuJmacOQJwcHf_nTo0lCSjZvPK7vg2k0NuiWxeRNUJ4gs8tegTRPXasvI9SW463qWar2OSVCBP020_aNZhaA_GyrW3lOwmjTVY1WIMawO82IIcorhCuRiLIF7Z62YUBu3-BRXIBALNVZcGtbcRm23MiXUVm8Binh0ikOK4PuCnUVE2fN6bijnoTSt3vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استانداری آذربایجان‌غربی: حجم آب دریاچهٔ ارومیه نسبت به سال گذشته افزایش ۷ برابری داشته است.  عکس: مینا نوعی @Farsna - Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456040" target="_blank">📅 13:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456039">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPbkGKILxJo7pIdxmXkcFIakXdsKsubO_uflKz2AGLp-cA60027BO7sm_bjnBc7D2BHPv7JrMqik_W7g3-2GYQ42sf5-5lqfsoxeAPNSHa1HgxMxhxCK9eKKpbRzJQvo_DUIl_zjCU4qZt_Qxg335qxh5a9LN2is72LjKqlFq5ynnbKvwONrRnuOr2jiBr1H8-rzrUuwywPMOmogqQNQ6y5mYoBM_dlYLmolGDm6DQtedBgeby-61h8kv8Ypt31bwQ9RJjWDBb6SSMpJALq593NsjhWVu7NwLqwzCXs4J3IDva_uL_90U8sYAmh8UFhYnKYgNoSYRfJfj4HhWr1yEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام تاریخ بازی روسیه و ایران
⚽️
تیم ملی فوتبال ایران ۷ مهر در ورزشگاه «کازان آرنا» به‌مصاف روسیه خواهد رفت.
🔸
فدراسیون فوتبال روسیه اعلام کرده است که این مسابقه به‌عنوان یک دیدار ملی رسمی در نظر گرفته می‌شود و نتیجهٔ آن در رنکینگ فیفا محاسبه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/456039" target="_blank">📅 13:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456038">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8Lx0KVI5_UQWOKMfgXvSu_nI7PyKurREJ3c-O7ehB_cdePi0RlZ-cLpCJ4l6dha1Bbw_mEb3IU6O6FfnKPzMfIc0wtXblzf-WKqHTCwJOkEq1yE7t-hL3EMuuXf0GmW3ioDs5aqtaD2t8C7XC5Z3L78LWMuFGzyrqpwrp-i494dpYPRS2UqoyLmjhOvt2jGcgzwnd6JJX2Aqh7DnsASg8EZqXQLJeAfcEBbhexH7pDLMxwrnPHRVFNGBb8vFGlQTojcodIozhU1QyIzsGDOTuNrDi4768CTImaQwmeW6IR0Bb-fB_nWzn319pkE7VNz2XBpVYQowNQkBr23WU-Stw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۹ ریشتر در عمق ۱۱ کیلومتری زمین، همت‌آباد خراسان‌رضوی را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/456038" target="_blank">📅 13:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456037">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JztVSWhf4Vqq6FTD4cwWGt_c8Y27Wkz1BY-Ig9ZfP4ArxKjMiLcEzRlz7lD0GVFp61PuzUPBEI_ZvmZAfr75G6NdE_mnLyk48aKdTu5AKCXx7mW_J33MamffqRF6c5Sei0FcQvLwoJrpF637n6wIbG8R5EpaLRVDokKq3tqa4qc0cti4tE4I4cfa3XWHnuOkwmtCz9iFxk6NHQZx7TCWl8VvHeEgfSgC6DuP2QbNBptfIFflMFKVusBBMaO-NDwYzpCBLHcO768ivelm3x6Wkdnc7_kJSsxIvhmOOS2hkqPu2KsHUWUcMgnA1AC2M9alNfdmOp8J9mCWEk3q3coyMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهرم راهبردی ایران در خزر که نباید از دست برود
🔹
با توجه به فشارهای ایجادشده بر مسیرهای دریایی جنوب، اهمیت بنادر شمالی و اتصال ایران به روسیه، آسیای مرکزی و کریدور شمال-جنوب بیش از گذشته شده است.
🔹
بنادر شمالی می‌توانند هم در تأمین کالاهای اساسی و هم در صادرات…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456037" target="_blank">📅 13:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456036">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roYWPLH5xc11vPOnpoySE42_GvENIWSD2pBtKh0v6JoR872snolDIivn9EV1FgF6ppDk5mR3lFVj0oHfTXn5mFR-43AGHrdRgdaOA3RHwuoptx8J_ggbA2gf9fn7WSBAaguNWiWHsSNYeYcJWj8Ikj8KlIjx9DLE-M-PVF5Z_hP4P0QEMWEo8HzbNT4OYhqz_o9kd_BQrxjx21FgN7_TgqyGvQYD8oaclBdxQjR40eSyBR4C9NE_q7wRPa0CFUB28Zyt7eEMOUEVtbP_KdXSfw-nxXf74c_IeEoN53unWs5h3syi-gjJhqqlCRnZgi0hdETXgOjSHcAqUVX0QMVbbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اعتراف اعضای باند شرارت از اقدامات خود در خاش سیستان‌و‌بلوچستان  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456036" target="_blank">📅 13:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456035">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234be4c0d1.mp4?token=PCwqt4OLoS-GbWIw6FVZPxcT00u8Z4gF8ezY8GVSgSwyssCInhUSGvplemNO1F_ynIrATBnCSGf6Pl7nJLWPjwKqm4YXa0OD46zb_8qvC6z5NMb7opNuIGJwIBjKN3BiZM-zXG3qrwaOfCeAUGHasAZh4MMiETMvwnjV74OkXHfj-od8JtYnxZKgu90dM8ybLocIR4sLjNP0T2hGcLH-_28Up1YpZEIn9RR172NWVNpQjPGDxoiMIKNP7L9oDM7zquTBOTM3MRf2alpou31GGPC-u8AH5vvlAYr2Cv0SQ0ByVeOrR3qQFbVkFB0dT8OSrp_waCeTBpUX5NIMfSJwTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234be4c0d1.mp4?token=PCwqt4OLoS-GbWIw6FVZPxcT00u8Z4gF8ezY8GVSgSwyssCInhUSGvplemNO1F_ynIrATBnCSGf6Pl7nJLWPjwKqm4YXa0OD46zb_8qvC6z5NMb7opNuIGJwIBjKN3BiZM-zXG3qrwaOfCeAUGHasAZh4MMiETMvwnjV74OkXHfj-od8JtYnxZKgu90dM8ybLocIR4sLjNP0T2hGcLH-_28Up1YpZEIn9RR172NWVNpQjPGDxoiMIKNP7L9oDM7zquTBOTM3MRf2alpou31GGPC-u8AH5vvlAYr2Cv0SQ0ByVeOrR3qQFbVkFB0dT8OSrp_waCeTBpUX5NIMfSJwTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وعدهٔ مدیر استقلال: پنجرهٔ نقل‌و‌انتقالات تیم ۴ شهریور باز می‌شود و ۳ سهمیهٔ بازیکن از فیفا می‌گیریم.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456035" target="_blank">📅 13:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456034">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">منبع دولتی: افزایش قیمت بنزین فعلاً منتفی شد
🔹
یک منبع در دولت در گفت‌وگو با فارس اعلام کرد که موضوع افزایش قیمت بنزین فعلاً منتفی و اجرای هرگونه تصمیم در این زمینه متوقف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/456034" target="_blank">📅 13:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456033">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
انفجار بمب در میان نظامیان صهیونیست در جنوب لبنان
🔹
رسانه‌های لبنانی خبر دادند که یک بمب ضدنفری در داخل یکی از منازل در جنوب لبنان به هنگام حضور نظامیان صهیونیست در آن منفجر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/456033" target="_blank">📅 12:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456032">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRoEcyKi6IWwsBg1ftLSq7XbQCzqN5vx1XFyBF590-a8vQyxsFNeOUD_dYbFg_M5eILgEVEQaLWWubpxYPzVr0NEhymn45BcbJNoWugTcrwv0KEk2MRF7Bb6p4OSKYmEs9DFdirl9OWSK8tElzqky3eJIt8qieMZu1-UCGfyljXH08X5LW4CtkXIUhNyTIuwnKUpHsn8XpxlNRwnohFbwcc2PZ9MJ1zbZ82SiFOm1IZdBILZ33-w8wlnKGU89cmLw6QEyyxgcx2mf5waqAVNPUzJNSpNSh6b_zm2G50wqbFL3NMXaKK6c8g9JJgkkxeP7_InAv-17qdsv3eTt0S5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه کاروان تسلیحاتی اوکراین را در دریای سیاه منهدم کرد
🔹
وزارت دفاع روسیه اعلام کرد که نیروهای مسلح این کشور شب گذشته با پهپادهای تهاجمی، ۲ شناور اسکورت‌کنندهٔ کاروان تسلیحاتی اوکراین را در دریای سیاه هدف قرار داده‌اند.
🔹
این وزارتخانه همچنین تأکید کرده…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/456032" target="_blank">📅 12:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456031">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ionuZoa65VDXprWoXysix72aslYTaGX-RK6qn8yXNWzEOvtEvReUYYfRcqQIC_N4DKvrEw6Z9t37zN-GewGZqOZWTjoGs4KwNIsiilNg8-rIuyLJGG52JPLf5fnkQbUj21jvcxDid1J9RMQeU-WqfijSpzkhtPKBPz-GzWBodwUjdLbEdE4xJAP0Sy6oQQ0CUWDV24euQ6HbSNFW8IXPkP0O6DO6GpqZGoRq7bt8my05p_U5HGtmBmsA-EWc25IR-u_D8zowTsABnnvZrcX-My6y0SvzJofi4R9xLvLi9otlwncXpYtKEii9Jdf3U5NYskR459yk9MY5G5RK4wXGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۳۰۰ درصدی صادرات ایران به اروپا از مرز رازی
🔹
سرپرست گمرک رازی خوی: در ۴ ماههٔ امسال ۲۱۷ میلیون دلار کالا به وزن ۴۴۰ هزار تن از مرز رازی صادر شده که ارزش صادرات با رشد ۳۰۰ درصدی و وزن کالاهای صادراتی با افزایش ۲۹۳ درصدی همراه بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456031" target="_blank">📅 12:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456030">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خنثی‌سازی ۴ روزه مهمات در سیستان‌وبلوچستان
🔹
فرمانداری کنارک: عملیات خنثی‌سازی مهمات عمل‌نکرده در محدوده نظامی بندر کنارک از عصر امروز آغاز و تا ۲۶ مرداد در نوبت‌های صبح و عصر انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456030" target="_blank">📅 12:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456029">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa8420543b.mp4?token=RKnYypsFlv3v4qmBP-nCzQwhf7RMp1vKOUQaIC6kgAwPs0IrnuXWyPpeuSTZTpqED07U0bDblQJKj4vKJ1ImcuTsqACPJTgP7n2wp6ily7G0MITqr5gNzjSTb7A6ldZ8UDibgjZZ76GbJN7VbXiqi0R-_XQnLgjobsZrSw4t_DmV7wbHRDXkzGF4bgIldYgZhqG9IhpkwwIlfPSpAW_0Jr6JQKS6uTbVu6IjPyRdeqdW0ig-vtJWR74iilBocgu8zmmS3pCUpEoJjYE55Y7-L7vfJ_ADwH81iHQkYsjid5XaKQncRwKQ9SUUuu8vC_0tuGw4mhuTcSYq8S_v7Hy9XzF-Rk9ztYJ32gFt1dGcBIidE_BZ2DJ1-7GBIoxg6-s9YHLMvZ7HFledjFGo9vJDcQmpijY6kb-r97NVzX_SagmTP8imMQJS-T8YMKhR-2hi79Z-myPSMuZVlipuh__dlQvO-yZ2kxyCUTTD2Phksd49Sg6OXDXoSbbZiyHHyKH-gNJbDfJs1Vle55AEJx00mkt_TlHGBkOGNUhISgv8YpI_6OaiURSfYbuD-o9ou8wa58KxVqLAWeos2Lwcv0zpusJdvuyqBcmod0MPyRYO-Xd8-lhmAKGY4EWwkcm_rO0zVT33DbEhWtC6Gcp0i1GkME-W9nXgXwtz2-VxOfv1Nj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa8420543b.mp4?token=RKnYypsFlv3v4qmBP-nCzQwhf7RMp1vKOUQaIC6kgAwPs0IrnuXWyPpeuSTZTpqED07U0bDblQJKj4vKJ1ImcuTsqACPJTgP7n2wp6ily7G0MITqr5gNzjSTb7A6ldZ8UDibgjZZ76GbJN7VbXiqi0R-_XQnLgjobsZrSw4t_DmV7wbHRDXkzGF4bgIldYgZhqG9IhpkwwIlfPSpAW_0Jr6JQKS6uTbVu6IjPyRdeqdW0ig-vtJWR74iilBocgu8zmmS3pCUpEoJjYE55Y7-L7vfJ_ADwH81iHQkYsjid5XaKQncRwKQ9SUUuu8vC_0tuGw4mhuTcSYq8S_v7Hy9XzF-Rk9ztYJ32gFt1dGcBIidE_BZ2DJ1-7GBIoxg6-s9YHLMvZ7HFledjFGo9vJDcQmpijY6kb-r97NVzX_SagmTP8imMQJS-T8YMKhR-2hi79Z-myPSMuZVlipuh__dlQvO-yZ2kxyCUTTD2Phksd49Sg6OXDXoSbbZiyHHyKH-gNJbDfJs1Vle55AEJx00mkt_TlHGBkOGNUhISgv8YpI_6OaiURSfYbuD-o9ou8wa58KxVqLAWeos2Lwcv0zpusJdvuyqBcmod0MPyRYO-Xd8-lhmAKGY4EWwkcm_rO0zVT33DbEhWtC6Gcp0i1GkME-W9nXgXwtz2-VxOfv1Nj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژنرال بازنشستهٔ ارتش اردن از بحران‌ها و معضلات آمریکا در جنگ‌افروزی علیه ایران روایت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/456029" target="_blank">📅 12:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456027">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM547UppkE1YR2oRHU_wiGkE-jIRcEjnQ2BhbG4mFStpAlgrrNTOxcRfKnDOa-0D7rtUVUXy-6YXcJkJppo8ZvhjSIWH_z2C_WuYNcykzR-7BVB1Quo0v96Djh_F8oxN8gcAypx2B2DguX5VrWZ0zjeEvON7e9ExFBbwkUSX87lUG2yeMUTzyz25-bbBpRg65fjN5O_ct3nFR58FZj9L3HGS7ntBYhkfUvBpWhJcJzde2A5uu63kdcJyFBNnmK1AipSylWG1NmQH20qBsP913XvPgdh1kEc1wnJufA40zuJCRCoPgCNaq260JUgFZb5mCw9LP4dPDDjLHXkjZC9BDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وقوع حادثه برای یک نفتکش در تنگهٔ هرمز
🔹
به‌گزارش سازمان عملیات دریایی انگلیس یک نفتکش حین خروج از تنگهٔ هرمز در آب‌های نزدیک شرق شهرک بندری «الخصب» مورد اصابت یک پهپاد قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/456027" target="_blank">📅 11:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456026">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اطلاعیهٔ جدید وزارت رفاه در مورد احراز افراد غیرمقیم
🔹
وزارت رفاه: افرادی که پیامک احراز سکونت دریافت کرده‌اند و مشکل دسترسی به دفاتر پیشخوان دولت دارند تا پنجم شهریور، ۲ اقدام زیر را انجام دهند:
‌
🔹
با استفاده از خط موبایل متعلق به سرپرست خانوار کد دستوری #1463*500* را شماره‌گیری کرده و  پس‌از ارسال کد ملی سرپرست خانوار، کدملی اعضای خانوار که پیامک احراز دریافت کرده‌اند را ثبت نموده و متعهد شود که ایشان در کشور حضور دارند.
‌
🔹
سرپرست خانوار اگر آخرین محل سکونت خانواده را در سامانهٔ ملی املاک و اسکان ثبت نکرده، به‌صورت خوداظهاری و اینترنتی تا آخر مرداد محل سکونت و حساب شخصی خود را در سامانهٔ ملی املاک و اسکان کشور تکمیل کند.
🔹
پس‌از ۲ اقدام بالا و تایید سامانهٔ املاک و اسکان، شارژ مرداد کالابرگ این افراد در پنجم شهریور پرداخت می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456026" target="_blank">📅 11:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456025">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31dfe94e92.mp4?token=Q3OWkiq2kl-ljmgTkLxsyiss4es3IE0kPQMRkizW1LZmAPCQbswbkRYdybBv9PQinbZGzPueD7YugBAeMAwpMkJwo3Fi-6NhzGDFTXB_miBm_eDzC--fLw-Z3l2avyTA0wt7-dk7lA6WffoxhGBbxFl5l8XzPo8U4OPJe6B1Egg_N6_sXvEAg8nvdM1kzwVTSm6z8K5wp4XnOztZs0Gjv1y7Sm2B9FqbTwBMEaqI2rx6If_WI2ivcgVqldwsz_MWg7S7Eb3k7NeVcS15SxVJECIGrZKjWB6OKvnbXheD__K_ieQt_3A9jHpcCjhYlLXnsr5Ia96N5w4vKNJ30vDHlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31dfe94e92.mp4?token=Q3OWkiq2kl-ljmgTkLxsyiss4es3IE0kPQMRkizW1LZmAPCQbswbkRYdybBv9PQinbZGzPueD7YugBAeMAwpMkJwo3Fi-6NhzGDFTXB_miBm_eDzC--fLw-Z3l2avyTA0wt7-dk7lA6WffoxhGBbxFl5l8XzPo8U4OPJe6B1Egg_N6_sXvEAg8nvdM1kzwVTSm6z8K5wp4XnOztZs0Gjv1y7Sm2B9FqbTwBMEaqI2rx6If_WI2ivcgVqldwsz_MWg7S7Eb3k7NeVcS15SxVJECIGrZKjWB6OKvnbXheD__K_ieQt_3A9jHpcCjhYlLXnsr5Ia96N5w4vKNJ30vDHlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طفره‌رفتن وزیر آمریکایی از پاسخ به سوالی دربارهٔ کنترل تنگهٔ هرمز
🔹
مجری فاکس‌نیوز در مصاحبه با وزیر انرژی آمریکا از او پرسید: «آقای وزیر، شما می‌توانید اذعان کنید که آمریکا کنترل کامل تنگهٔ هرمز را در دست ندارد، غیر از این است؟»
🔹
وزیر انرژی آمریکا اما در پاسخ گفت: «ایران تلاش می‌کند تا اقتصاد جهانی را گروگان بگیرد و همسایگان خود را مرعوب کند. آنها یک زرادخانه عظیم ایجاد کرده‌اند، بنابراین آیا در منطقه مشکل ایجاد می‌کنند؟ کاملاً. اما توانایی آنها برای ایجاد مشکلات رو به کاهش است. توانایی ما برای اسکورت و خارج کردن محصولات از آن منطقه درحال افزایش است. آنها تقریباً یک برگ برنده دارند و فایدهٔ آن درحال کاهش است».
🔹
مجری شبکه فاکس‌نیوز نیز در واکنش به این جملات مبهم و متناقض وزیر آمریکایی تصریح کرد: «این اصلا به معنای کنترل کامل [بر تنگهٔ هرمز] نیست!»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456025" target="_blank">📅 11:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456024">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">روسیه کاروان تسلیحاتی اوکراین را در دریای سیاه منهدم کرد
🔹
وزارت دفاع روسیه اعلام کرد که نیروهای مسلح این کشور شب گذشته با پهپادهای تهاجمی، ۲ شناور اسکورت‌کنندهٔ کاروان تسلیحاتی اوکراین را در دریای سیاه هدف قرار داده‌اند.
🔹
این وزارتخانه همچنین تأکید کرده است که نیروهای مسلح این کشور به حملات خود علیه زیرساخت‌های بندری اوکراین و شناورهای دریایی که در خدمت منافع نیروهای مسلح اوکراین به‌کار گرفته می‌شوند، ادامه می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/456024" target="_blank">📅 11:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456023">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRE5-Srx1KUW11ofG_jyPzZt7_6zsuFrORo1NpYygq8d92WAfv_odaDEYtKqjm0gBcBpHpojR-O3GbbbCKNsP1Swf_zzlk7UGVMW-f3jbUcIIGZ9zcRJIGprMAUrIRXei8JPETQ-XA-inJJkVV3ZnMm7kqUImmBDPv1doUI-L6RWn2l6VVZje7oiOUUXdb4IDzXhvqF2yqkFExlcbtfQGlJOGXEaU9wRbG7ZON63oqIJ4BYKvb7f2RyH14ZylhJUfXnw_XG60LlK2HJNfFqR8mZ6bCB8q9W912fiZe-07vQE8GRIXnYQb-L3NfX-SM_dsWB7TBlBXEHP9G77yftXfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار فرماندهٔ سنتکام با ولیعهد سعودی دربارهٔ تحولات منطقه
🔹
به گزارش خبرگزاری رسمی عربستان سعودی، فرماندهٔ سنتکام با بن‌سلمان امروز در شهر جده دیدار کردند و دو طرف در جریان آن، روابط و همکاری‌های دفاعی میان ریاض و واشنگتن را مورد بررسی قرار دادند.
🔹
براساس این گزارش، آخرین تحولات منطقه و تلاش‌های مشترک برای کاهش تنش‌ها نیز از دیگر محورهای این گفت‌وگو بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/456023" target="_blank">📅 10:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456022">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17ec695dbb.mp4?token=U9mqqDILfkwobgopRU5cHRA_Icl0TJ9PL9ECPZz3sUD8kroVmpz55bFZXJqz4Pr_kukGD8fnjwxCU-wVuHe9GfaXc0_D3uXDQaYpqRd6UXv_r93-IgC6TwRkIYKF4ZpSm6mEXHl93xoIpL391vjloFnrQMCUhGqEqNh9m7lFTMF8kSdoEQ9kHK6AOi4dsPbsVwfEU8CAJVXKS2zXbu8f6trLhhtrFphD-jeInhIC5oOqR82dg7En14AyJhy_-MZlEG9nnMYAeKqufQacOkt_3MaMPGBtXEnN9k5UuB3qDjAGR48A-NV0e_J3S7nMjtA-1TFjnqlo7wpnf9pw1_38hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17ec695dbb.mp4?token=U9mqqDILfkwobgopRU5cHRA_Icl0TJ9PL9ECPZz3sUD8kroVmpz55bFZXJqz4Pr_kukGD8fnjwxCU-wVuHe9GfaXc0_D3uXDQaYpqRd6UXv_r93-IgC6TwRkIYKF4ZpSm6mEXHl93xoIpL391vjloFnrQMCUhGqEqNh9m7lFTMF8kSdoEQ9kHK6AOi4dsPbsVwfEU8CAJVXKS2zXbu8f6trLhhtrFphD-jeInhIC5oOqR82dg7En14AyJhy_-MZlEG9nnMYAeKqufQacOkt_3MaMPGBtXEnN9k5UuB3qDjAGR48A-NV0e_J3S7nMjtA-1TFjnqlo7wpnf9pw1_38hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امارات ثروتش را به آتش کشید
🔹
تصاویر ماهواره‌ای نشان می‌دهد امارات گاز طبیعی که تا قبل از این صادر می‌کرد را در دودکش‌های فلر می‌سوزاند.
🔸
به‌دنبال ناتوانی امارات در گذر امن از تنگهٔ هرمز، صادرات گاز این کشور به صفر رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/456022" target="_blank">📅 10:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456015">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVr2YnNQI0ORvaEIpkI7eaUeMFjK-nKpojNJOZe4mYcAw3WyKi_dzpRd8V-kLxrlKsZK75kJgr3ZZGA0nu-sB4yODJSxbj4S9jZVyUT4GPeFSQieSQFGWxP9siZWRVdrkVXL3qcUT4hgkFfJ12VBoRDwZd1QnBI6wl6Qicqu7A3TmP8K4tpcNUlY7K3seb_ovM3tTth-qUbn4QpiooeDqcBp2lV1f3rGx05cnC5nl6N_HVEEg3jMQqU5fg8mcLHiRZcY2aRi3plL_njKmlhgqcIEFqOCUpNAZmxWgHDGQ8aZG8MQBxugZz-1RDos5BSEQZxqnTcM65uSieg4mNBJ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9o1k4EgRCmFgb0yGGbvz6JilouI25nh-E3V82u3HPfCv3vNNkAmll96DQwUT9VTqgUsPDOcKD_KVAF2WupbRv1bxb0dgQ_rsaEUaq78F69M_ACbnWSGPp5N76AkWY5lrp0n4S7tEwOwXzvNqJP2C-5CP7j-QGA3A8wC_QxwS2u8DC80Rvz9UA4jA-s71GxwgC5REu95KMEvimGQOVvCUgjNkurMQ93ipJtGHJOsJd_okr0sXA324E00ASrbHP4Kqro6dNmq4JZrFgmCh8WcwRzo4-xQdLlxL61VnGetAe0euC9R2FawI1QRMvv_RyiJEZm2_tasW4GOPT4W8_INKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gC1tJ_2d9kEacGG3Di9vsnXomP0qQnoFxs6k7R1BTcYLDKRYFLHQyNwf8HSx0IKg7afh9pmdq3I1r-jMiQnVDl0-x4-UbqsKV0rblLsgSNKoC0yJHhWO9oXBM8M4VBdCuIrvP0Rpl5I7UQmY9OMim5Z3qGVto3-na9VuK9kQdSD2CoqUnTH-OdSwRAN_dnFFmjF1TEtKSd7Lu2OHVQObpHERrP1QHTK4_K6AWGR9_dSqp3Zdd0WvTXDFIClBVuhCgturm68D3GV6V_ukBi6GLOgAHzQMWJbF4M6vcOO7hWCT07VCAAu5spY3NTfDnzTGTklc8nuYu_JGDqxke8n1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLEeSO9QEcKf_pe9vLelFWs_2iFLgp5qd6nA5IDO2U3wc0itwXNk6ZUgbFQ6q7qvbAro7kjOwbzSXhiwXJLRGTGrcEuVlRJ4uQaM4Gx7ymEnlhgntgb7QAJ3DuQEw11ygx8Pmh7KPJPwvN9TlH__dqvoUFhzD9OAiAr8kZ-Mz-hJRRQHdG4mVadouhEH10a5QBBFWkmtNwHYIgYAGW6CQqvPL_NUqZkiRbpxuZPgzeOrkIJBwBA-krjcbmS7i0PEOPYfcc5xxDurNVwDpaPHqD0f_9eYXXru6x_dZcNGY09Bg7GT9KC_w47hbm0GGgacFLAg7Q5Xb77nmag6s66jRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vautql-UKTPxVVvGiPXeWZUK4cIKpiftdsjQT4FbZXq2qqcJXTL7FaqUpsrP6wRCgPOhRb0TPMGacgRvqkY5PRwW999lAX8F4nQ4K2yBdxBJ4QpyCLXqhUe7W-GCmZmG5PCvwhf6Y1CSTIYaBytxVUp81gjsVnBMwGEj7IpyPnzJzCgVht2U0a4YSSJM4xEq3kTBOUP8aMT0JNySyVRel61Vlv4jG4Zo1iChjJQMUhpmR5VE3OTMuej9uHaa4UN8Ji69ZR5BPhHACzFoW7Csn8NQ2q6vsJh9hD7750hc-a8mue5EfOpeFo1oXgHsz0T7bWnvrDN4Ugrul9vufm_IeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7R2kaz7qvMWTqlJMFqYOODy7N3VEkhkjNThesl_2GtNvRApBY2CmRCNmTxtAHOsbPDHzMw-x2fdnGuODq712B6MXcBJV-G-JIYId2U-HVLR7aivYSK_KK24Oljoy4L-iI-FjUqVfogzxv7orNqDZfpA0dnNFEGUgJ3XvgsXbDFprymiU9TssR1yTkFL1O9gjlFlq9awtR1qqh59jsghxON-dtaBNt9Hzt11-gWVxvg32NOP6EKYAQFpPct2RSHQy81Yex4aN1ChZKRH0gRhJkvbb-vCeJYCKoFA8IsMkuUeTM8P-8Mwt1bxrnNYmTXQCBNZxpYm9DOmbVZeGIinFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaf8EBxdUHZ75nPSzJcZ2I50tS4iBdW_GIj5t7UKlNg4g6aTU6zT0SwVRyVfvETtVhrcTI8Rgu0t2BtslA-uaSZNA-gnC-2_2Vcw53BXxy0j1A0WLz81PYG17n2-UV763UDpnw4Rg4Wtuyaxff5L19hucLAyEfet2HvtDSKZMIBVpsHRicnul5ZEPzv9yVfM43q6cJ0XrR1VvB4nHoN9yvcEvFvtT7Eq7tEc35yC9MadGu7L2fiY37UObD4wLYDsA1xEdxvFO89tSatbJIezSfxBWP1lkBP1i7pspS6gnfLFYaLf6tR-A6ZeeINay3EbplhHci4xxZeK-Ld3DCFC8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">علما و مراجع تقلید در دیدار با رئیس سازمان بسیج چه گفتند
🔸
آیت‌الله مکارم شیرازی: بسیج شجره طیبه‌ای است که مردم و کشور در طول سال‌ها از ثمرات آن بهره‌مند شده‌اند.
🔹
آیت‌الله سبحانی: ثبت‌نام ده‌ها میلیونی «جانفدا» تنها یک عدد نیست؛ نشانه‌ای از ظرفیتی عظیم است…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/456015" target="_blank">📅 10:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456014">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SflckSNqUh4yqTJrA29AKXt3yfNeOqgAQ3VccF50cOK5GrnhWoUyEuf71F784hhJP9SAFaAw64JlMvye1uIY38iwc-Mj76jV1mUI-fzYe7Lq8mspcBJ0vCQzAwZdUprcc2zLNHGONDL-rc0Qe3JnxwKKgjiExtHbgXoCg56tGEtBzQzqKY5TB1vHvZOtoD8a3bg77VOaSmbJaD5PJcAelG4XxGLVzv4le92LAuSlYvHBT3nVWDfDEdl4M7QK3Z9-eGIyKmJwTSK3623FOH5ch9ozEPot1tM115hljs02WQmmeU8C-ikoq3MKKZmfT2cbw5EPRJrnB1hXqhVpFf2CDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام تبریک پزشکیان به‌مناسبت سالگرد استقلال پاکستان
🔹
رئیس‌جمهور در پیامی فرارسیدن هفتادونهمین سالگرد استقلال جمهوری اسلامی پاکستان را به نخست‌وزیر، دولت و ملت این کشور تبریک گفت.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/456014" target="_blank">📅 10:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456013">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GODe0y8V7PCI3Fb_WdzXqJS7gGmHBUjiuhDyx8RwjApekDR9FnxZ8LqcWtAIjOHu0TBCk3UobF9dyXRLQQ7FcBjV_dcxTVzSsIDLAAwIk9WXr8tZTNbMawwOz9Pc41Ql6qxFqKghwefsftmZDoJisP8dpOGolg8A4gE9eYxlE1hsKN_vzadFuZfoeN027PhewHpAvtw166yjpjfoEn_io6IEj0621qvRn-j-fnXLCnQc5YpO2Lp27PmhkIdiKvPPpiCnWs3g6FJXl6iuvpUVXBAqt6B-SwuF9yhE4QsuS1fhVue55lf-qrYDAm4SDXM4h3qcQpslx89XfkPKpItt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار قاطع ایران به الجولانی
🔹
پایگاه خبری لبنانی «یونیوز» به نقل از منابع مطلع اعلام کرد ایران سناریوی مداخله نظامی شورشیان سوری در لبنان را که بنا بر درخواست آمریکا در حال تدارک بود، خنثی ساخت و با ارسال هشداری مستقیم به دمشق اعلام کرد که هرگونه ورود نظامی به خاک لبنان، با فعال‌سازی جبهه‌های متعدد در داخل سوریه و در مرزهای آن مواجه خواهد شد.
🔹
یونیوز افزود: هشدار ایران شامل تهدید به فعال‌سازی مرزهای سوریه و عراق، گشودن خط درگیری در حمص، حمایت از تحرکات علوی‌ها در ساحل سوریه و تشویق کُردها برای بازگشت میدانی به پیرامون حلب بود و این هشدار  فقط خطاب به دمشق نبود، بلکه به آنکارا، بغداد، دوحه و ریاض نیز منتقل شد. این هشدار حامل این پیام بود که هرگونه ماجراجویی سوریه علیه حزب‌الله در لبنان، محدود به دشت بقاع  نخواهد ماند و ممکن است به رویارویی منطقه‌ای گسترده‌ای در داخل جغرافیای سوریه تبدیل شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456013" target="_blank">📅 10:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456012">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
حملات هوایی اسرائیل به جنوب لبنان
🔹
شبکهٔ المنار گزارش داد که جنگنده‌های رژیم صهیونیستی از بامداد امروز تا به الان چندین‌بار شهرک المنصوری در جنوب لبنان را بمباران کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456012" target="_blank">📅 09:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456011">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7TGEUTg42NdYZacTxTCvPlVgMpphWpkCvTvFJ4CyKABgwXCJ0rm746-OibNEXeZ41_az2MG3AC243cpbAUoo1ikJt2ChIOuNh2kF6agBajSzGc8-hSC_eZi6yy97Dp3Uhb9Wa_dF0PucYdzzsBOYHqBG3Ns9AvZWDY186T337HAa21lG3O96B5EGXZgj-X-nr84FzIKh-UMUENUyVQjSnSFqTLVkqjpskqc34bz8o9TgSWiF-i7NNRzzsS0WJkzYroGMmWKnNH-xNbLzD3APt73tUVl9_2GEmDLlSVGgriEGmnir2rmH-rcKbLzJyh-t31h0QbU0_dhtujOYb_KWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار کرهٔ شمالی به واشنگتن و سئول: پاسخ ما قاطعانه خواهد بود
🔹
وزارت خارجهٔ کرهٔ شمالی: رزمایش مشترک آمریکا و کرهٔ جنوبی تمرین یک جنگ تجاوزکاران است؛ این مانورها سطح متفاوتی از بی‌ثباتی را در منطقه ایجاد می‌کند.
🔹
اصل همیشگی ما برای تأمین امنیت این است که به تهدید در سطح جدید، با بازدارندگی در سطح جدید پاسخ دهیم.
🔹
موضع خود در برابر دشمنان را برای مقابله با هرگونه تهدید و چالشی از طریق اعمال مسئولانه و قاطعانه حق دفاع مشروع از خود، با وضوح بیشتری بیان خواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456011" target="_blank">📅 09:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456010">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2e9e57b6.mp4?token=chhMpVgr8T9qSos4adA0zjlBldyfdVQHfoq1wQ2twP-LA9ZvUHRZZUjW8-nti9ecQFsj3k_98avtOV9IC6gxBgj3dsMBC-G7kOw12YH7jasv6WIhMYNsW90j846VAtLXjxXZEvpfH8nYuKpFnmVhI2xLL098HMXjp_-WtFscN0I_5G0-oxVviENXKc2yy-_rzydvszanwRob5PvQrZvTizz1Ulkr9NW8Ynt6xUEUpTA74ZsMWeNCcArpgpVho7yvWoxl2d_bbwAYnQw14oSR0pblTXMlJBPLM994V0msBxuNH05TrqUJUIQ6iI0WuMtNjNRaQuFZH0Ucp1-EiSZawA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2e9e57b6.mp4?token=chhMpVgr8T9qSos4adA0zjlBldyfdVQHfoq1wQ2twP-LA9ZvUHRZZUjW8-nti9ecQFsj3k_98avtOV9IC6gxBgj3dsMBC-G7kOw12YH7jasv6WIhMYNsW90j846VAtLXjxXZEvpfH8nYuKpFnmVhI2xLL098HMXjp_-WtFscN0I_5G0-oxVviENXKc2yy-_rzydvszanwRob5PvQrZvTizz1Ulkr9NW8Ynt6xUEUpTA74ZsMWeNCcArpgpVho7yvWoxl2d_bbwAYnQw14oSR0pblTXMlJBPLM994V0msBxuNH05TrqUJUIQ6iI0WuMtNjNRaQuFZH0Ucp1-EiSZawA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنجکاوی خرس قهوه‌ای در جنگل‌های رامسر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456010" target="_blank">📅 09:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456009">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyeHzO5gUkg8wTlCM-XdDy4ynG9ajR1FqTib5gPTh4JL1qE3-V9VNsYu7lj0Zq7qoCusp3rtnJHWUu2V13hUlUMT6iGUyUWn1ICETHgZeRKZ4fWOvQiJoxeFB4Geri0JK0swC5sB1E5IqH--sHiDgC0UJQGEEG67PaoNbn4DJjADgR_VmvJ5yyv8veHnJmWv_NVkhEK_y9lUj7EiS4fOc5--U4TuGZb1cd-ABOhnfGCe0s0QWczXzCskog_W4YDTBsPedbTv2tNn14B6cuOfhqc6rYhy7tfIjDw0dljV-YpiCn58MUWH-SgLst5tJSQkJqZqIfKW2KvGcvFbXqoxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنفس قابل قبول هوا در پایتخت
🔹
براساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص کیفیت هوای پایتخت امروز روی عدد ۸۱ قرار گرفته و در وضعیت قابل قبول است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456009" target="_blank">📅 09:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456008">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_OWb9EOU_-Ez09SP_DLWVPEq23K9bBb_PwkuniWjFQQZ2fNiYVAcKlsZmcMD5bRWoRApzmsK2_KM4vWNb8MZ5PL86DVcetoPiKkAgu3zTqI1M1EegXco9OlGa1EmhCCLOP8PYvtZ8lXIWiD_ybAwFqEMH5ZqeMmTpii2xTlE6mU4jrOhUcayTJ6CTViISvfiPzsgYVKk3qeyRalTgcWLW07L4CPpHVJtZK_U2pNSSR6PMQPw68KwA9KJ4YYcKjPu4B3UNHpJn2P60QV-ciep5etMRLqsw-ZM-S7lZ19NSfJGdzjZNa3UuHyw4o0JurMtNQ0P6GoNJlQ_h5_9ZoRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۳ ریشتر در عمق ۱۵ کیلومتری زمین، مورموری ایلام را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456008" target="_blank">📅 09:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456007">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جزئیات محدودیت یک‌طرفه در جاده‌های شمال
🔹
پلیس‌راه مازندران: باتوجه به افزایش حجم تردد، از ساعت ۸ امروز  محدودیت تردد تمامی وسایل نقلیه در مسیر جنوب به شمال آزادراه و جادهٔ کندوان اجرا شد.
🔹
حدود ساعت ۱۱ از مسیر شمال به جنوب خروجی مرزن‌آباد نیز محدودیت یک‌طرفه اجرا خواهد شد.
🔹
جادهٔ هراز هم به‌صورت مقطعی در محدوده‌های تونل سپاسد، پليس‌راه لاریجان و گزنگ تا لاسم یک‌طرفه می‌شود.
🔹
با اعلام مرکز مدیریت راه، تردد در مسیر جنوب به شمال آزادراه جادهٔ چالوس نیز ممنوع شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456007" target="_blank">📅 08:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456006">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQ1LdllN58jNUVFSRM3W3ZAecZfii69b89AN4pJtn4q4hcldyeXFqzcfTCPhNCS6OmdFS0ZOqWQJcGrhISY-IN_W0VY1nzCBuf6QaauiXzGmMecpxX_hWayQk59R5O0X2T6M1S4A18393seTSsudYMktlGlePQi_BN_1h3-Fwf6P5njL-pXGxvXTs5o6x6xL5xUZNYu3i-K_rAn-E9NKHVybi9oox3pU6OQsRANkc1OqHTnydHq8YriYTeRG4K8E20dWKLnlH86kRqRUf_U_mHxz6iiMrOeVohdDP_1tSYf4xqQpKF9SGY2km3SYfghGULAUASzkVNg4IXc8hyInBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثر وارونۀ حمایت ترامپ از رئیس فیفا
🔹
«حمایت ترامپ از اینفانتینو باعث تسریع برکناری رئیس فیفا شد»؛ این محتوای گزارش امروز(چهارشنبه) گاردین از نتیجه حمایت علنی ترامپ از اینفانتینو در سخت‌ترین دوران ریاست ١٠ ساله‌اش است.  ترامپ روز گذشته علناً در صفحه خود نوشت:…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456006" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456005">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVdjBu91eJUgjefvP09UUwfyEb7Qh5dOSJ4bOnyGJsyQYzmFAJTM1vJSobBFj6yq3YzfNqIw6uj9KqsqRN5NKl_vhwOa3Amak5va-5BaLmCCmaajBtUfoebkQfbbotVSPLTf7fWaS_y_cNjFmjwdCaak7T6f4plrG4T-lIJ0RNXeQy7CrxDNwdndybAe8tARDUJIG5-0h8klHmEeSw9ygY3oV8rJ9YSw2BWvM6RuDBeFZTMT2Oi-gtcFkpDuMCajhIGC-UueQ6HqdmpjUs-_lI59jfwQYhvh5dOCaehm-ATq0JpVNqZDuvEkA-lGtqOqAyGCpxuvCZGLQF69r9GWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمنی‌ها قفل باب‌المندب را محکم زدند
🔹
شرکت انگلیسی ویندوارد امروز گزارش داد که ۴ روز است که تهدیدهای یمنی به عمق آب‌های سرزمینی عربستان نفوذ کرده تا تنها راه باقی‌مانده برای فرار کشتی‌های سعودی با دورزدن قارهٔ آفریقا هم بسته شود.
🔹
طبق گزارش‌های کپلر، صادرات…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456005" target="_blank">📅 08:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456004">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تلاش پنتاگون برای پنهان کردن اقدام به خودکشی یک ملوان در ناو لینلکن
🔹
همسر یکی از نظامیان مستقر در ناو هواپیمابر «یواس‌اس آبراهام لینکلن» که هفته گذشته اقدام به خودکشی کرده و خود را به دریا انداخته بود در گفتگویی اختصاصی با رسانه «ام‌اس ناو» به افشاگری درباره تلاش پنتاگون جهت مخفی نگاه داشتن این حادثه پرداخته است.
🔹
وی که خواسته نامش فاش نشود تا جزئیات مربوط به سلامت روانی همسرش محفوظ بماند گفت مقامات نیروی دریایی آمریکا تا چهار روز پس از اقدام به خودکشی همسرش هیچ تماسی با او نگرفته بودند.
🔹
او تصریح کرده که همسرش به مدت یک ساعت در آب بوده اما در نهایت نجات داده شده و اکنون تحت مداوا است.
🔹
وی گفت: «به نظرم برخورد آن‌ها بسیار ضعیف بود، چون نه به من اطلاع دادند و نه می‌خواستند من چیزی بفهمم؛ آن‌ها فقط تلاش می‌کردند موضوع را مخفی نگه دارند.»
🔹
همسر این نظامی آمریکایی افزود از طریق پیام یکی از دوستان همسرش روی کشتی متوجه این اقدام به خودکشی شده است؛ دوستی که ابتدا خبر داد فردی از گردان آن‌ها به دریا افتاده و سپس تأیید کرد که آن فرد همسر او بوده است.
🔹
وی پس از عدم موفقیت در برقراری تماس با همسرش، به نماینده خانواده‌های کشتی مراجعه کرد تا اطلاعات بیشتری به دست آورد.
🔹
در نشستی با حضور نزدیک به ۲۰۰ نفر در تالاری در پایگاه هوایی دریایی «نورث آیلند» در سان‌دیه‌گو در تاریخ ۶ اوت، خانواده‌ها بارها «هونگ کائو»، سرپرست وزارت نیروی دریایی آمریکا و دیگر فرماندهان را درباره گزارش‌های سقوط یک ملوان به دریا مورد بازخواست قرار دادند.
🔹
یکی از فرماندهان در پاسخ گفت که از موضوع مطلع است و تحقیقات جریان دارد، اما افزود در آن زمان مشخص نبود که ملوان خود را به دریا انداخته یا سقوط کرده است.
🔹
به گفته دو تن از حاضران، این سخن با خشم شدید حاضرین روبه‌رو شد. این مقام سپس ادعا کرد ملوان به کشتی بازگردانده شده و به نظر می‌رسد «حالش خوب است» که این جمله نیز با اعتراض و استهزای حاضرین همراه شد.
🔹
روز جمعه ۷ اوت، یک روز پس از آن نشست پرتنش، همسر ملوان مورد نظر بالاخره یک پیام رسمی از نیروی دریایی آمریکا دریافت کرد که به او اطلاع داده شده بود همسرش اقدام به خودکشی کرده اما اکنون صحیح و سالم است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/456004" target="_blank">📅 07:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456003">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aea5d5547.mp4?token=EvOf5VYWutjWr-oRS1tNYEVCMEzVuYDNLKvcbAzBzNQSvye-3x3Tqz0oqq6zljmuLJi2gINvquQxNHJCeBukus3o15FvFCXzTJeVevpq7Jh-KhHyaUy1gxRIu1bbrKOV7IIHRnSQTZ5kyoqjsFGQgUKJ6VVVhOGjj-ljA7CGtvaMlUGShQ897S0tHASD_WM4EhsCWc5XayurgeSbVOTXObDHxQeLELIcjZgxvY_b19y_YGuIpHUSma3HQXISPu7zjTHfBQd4oYjGYcS9K0SFaeLyTCKVMTpwZtHHNoN-yRDi1bxGSD8Wz0HDlb5UP_xBuhqwkFf1YitZ2M_6w5LiNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aea5d5547.mp4?token=EvOf5VYWutjWr-oRS1tNYEVCMEzVuYDNLKvcbAzBzNQSvye-3x3Tqz0oqq6zljmuLJi2gINvquQxNHJCeBukus3o15FvFCXzTJeVevpq7Jh-KhHyaUy1gxRIu1bbrKOV7IIHRnSQTZ5kyoqjsFGQgUKJ6VVVhOGjj-ljA7CGtvaMlUGShQ897S0tHASD_WM4EhsCWc5XayurgeSbVOTXObDHxQeLELIcjZgxvY_b19y_YGuIpHUSma3HQXISPu7zjTHfBQd4oYjGYcS9K0SFaeLyTCKVMTpwZtHHNoN-yRDi1bxGSD8Wz0HDlb5UP_xBuhqwkFf1YitZ2M_6w5LiNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریاچۀ ارومیه دوباره تماشایی شد
🔹
با افزایش آب دریاچۀ ارومیه، سواحل این پهنۀ آبی در روزهای اخیر بار دیگر شاهد حضور گردشگران و مسافرانی است که برای تماشای جلوه‌های دریاچه راهی این منطقه شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/456003" target="_blank">📅 06:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456002">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دستور ترامپ برای بازگشت ناوهای هواپیمابر به فناوری قدیمی
🔹
ترامپ به نیروی دریایی دستور داده است سامانۀ پیچیده پرتاب جنگنده‌ها را از روی ناوهای هواپیمابر جمع‌آوری کرده و به استفاده از منجنیق‌های بخار بازگردد.
🔹
وال‌استریت‌ژورنال با گزارش این خبر نوشت که مقامات نیروی دریایی آمریکا سال‌ها با این اقدام که احتمالاً میلیاردها دلار هزینه برجای خواهد گذاشت مخالفت کرده بودند.
🔹
به گفته مقامات آمریکایی، ترامپ روز پنجشنبه یادداشت امنیت ملی را امضا کرد که این تغییر را الزامی می‌سازد. طبق این دستور، سامانه پرتاب الکترومغناطیسی که در ناوهای کلاس «جرج راجرز فورد» استفاده می‌شد، جمع‌آوری خواهد شد.
🔹
این دستور، نیروی دریایی را ملزم می‌سازد که ساختار چهارمین ناو از این کلاس به نام «یواس‌اس دوریس میلر»  و تمامی ناوهای بعدی را مجدداً طراحی کند.
🔹
سه ناو اول این کلاس، یعنی ناوهای «فورد»، «جان اف کندی» و «اینترپرایز»، سامانۀ الکترومغناطیسی خود را حفظ خواهند کرد.
🔹
ترامپ ماه گذشته در کنفرانسی در پنسیلوانیا دربارۀ سامانۀ الکترومغناطیسی گفته بود: «آن‌ها اصلاً به درد نمی‌خورند و بسیار پیچیده‌اند.»
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/456002" target="_blank">📅 05:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456001">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujlhiKgpFETUJlJcscvIZ-CHBff_WBywuR-riGxmTD_aBrVK_NdhW0bK2UlyAa1kupNfd1o5LNpFzAo3StENZ6Tlz0u7khvCJeVK7ppSnrEL1E1DeOZl3rQwDqnlGwae7WRCBZG0CBDITzvMlk4Pg-bjv61pFztGU-HYnMoHV75FcEzuiTg1xdSRFSTWKTTTUAHTllEQdgCDmFhzawTyWJmnyiDs97-LDbxexHEcxWpYQuMpq8jS3NP1VjtpCfwX7JJsmuwY-zvTQ6AHxDiNTYFVNMQvekJMAyIHaVx7tz7ToW2sqiQY-Zk1g9OEzeMEQGDZz3zf6scSDnN04YbRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید: دولت روی واردات پهپاد تعرفۀ گمرکی وضع می‌کند
🔹
رئیس‌جمهور آمریکا اعلام کرد که روی واردات پهپادها و قطعات آن‌ها حتی از مبدأ برخی از متحدان کلیدی ایالات متحده تعرفۀ گمرکی وضع خواهد کرد.
🔹
دولت ترامپ علت این تصمیم را وابستگی «بیش از حد» این کشور به تامین‌کنندگان خارجی پهپاد اعلام کرده است.
🔹
کاخ سفید اعلام کرد طبق فرمانی که به امضای ترامپ رسیده، برای پهپادهایی با اندازۀ خاص یا دارای قابلیت‌های ویژه‌ای که اهمیت بالایی برای امنیت ملی دارند، ۱۰۰ درصد، و برای پهپادهای کوچک‌تر، تعرفۀ ۲۵ درصدی در نظر گرفته شده است.
🔹
همچنین تعرفۀ ۱۵ درصدی روی پهپادها و قطعات وارداتی از اتحادیۀ اروپا، ژاپن، لیختن‌اشتاین، کرۀ جنوبی، سوئیس و تایوان وضع خواهد شد و پهپادهای وارداتی از بریتانیا نیز مشمول ۱۰ درصد تعرفه بر اساس ارزش کالا می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/456001" target="_blank">📅 04:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456000">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392c1a051b.mp4?token=ppUJ2Kh13ilbweqSima2kKl8YP1Ui9wrd85VL5Ht_JkiUcsYuCNkizJ9bfyKltxcDwzVry2vKxgjnZmDZETOjF0l_NrDkTFO04R3we6oECxYgoaAemjAtSg4dGB48U4cVCXJ4cxVDKFSLgyNgoqh8xR56hFsJTrBvHQLllGc9sxSLXlX0cmNsy6QYPq7m5nYwTPzDaeegELw4MHNu0ChNtpWgICYdpltKQ_iS3S1cFvQmO4hM9m4KacJRQE5nMWrOsUPFs5pRpA4MLjOJXFTPWMrG2UhVWpcEhO_RQtfXZceag6HKzsT0bGFabLztDY4ZVOL048A9fWtU5TG1b3LUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392c1a051b.mp4?token=ppUJ2Kh13ilbweqSima2kKl8YP1Ui9wrd85VL5Ht_JkiUcsYuCNkizJ9bfyKltxcDwzVry2vKxgjnZmDZETOjF0l_NrDkTFO04R3we6oECxYgoaAemjAtSg4dGB48U4cVCXJ4cxVDKFSLgyNgoqh8xR56hFsJTrBvHQLllGc9sxSLXlX0cmNsy6QYPq7m5nYwTPzDaeegELw4MHNu0ChNtpWgICYdpltKQ_iS3S1cFvQmO4hM9m4KacJRQE5nMWrOsUPFs5pRpA4MLjOJXFTPWMrG2UhVWpcEhO_RQtfXZceag6HKzsT0bGFabLztDY4ZVOL048A9fWtU5TG1b3LUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا کشور امام رضاست
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/456000" target="_blank">📅 03:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455999">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXTsVHrkENePyBfpaKtdG4DStwa9nqtrrecF7fqE-FYNJS6NouVjIWFxX0Bl0M59mLdvHAYVVLuvWDRxNtZzy6XBMaKjefWWfkEUDsg_4jMUicHV5d692r-bBLEeXqB2ObSmtY3f1vdldwbENeDS3kaPhf9K9Nb8VRrmuODSZV5Muniq-9ieSMiUPhdSTPwIczXDYuB49OJKlpI0gdww6JvU0YSlEEBQcbYbK6LJUYN09Rx26ZPYWTpG9-16HVydrUwah1t1GxnOPPfO20bkGVguE_q0pTSAtcWYPLId1oE6AuMmIA3j9j8NkwaH7RK7e08VKPv_ETewSJn3mPETtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل خبر مرگ خالق چت‌جی‌پی‌تی را منتشر کرد
🔹
گوگل برای مدتی کوتاه و به اشتباه در نتایج جست‌وجوی خود، سم آلتمن، مدیرعامل اپن‌ای‌آی را مرده نشان داد؛ بررسی‌ها نشان داد یک فرد با دستکاری صفحۀ آلتمن در ویکی‌پدیا، اطلاعات جعلی دربارۀ مرگ او وارد کرده و سیستم‌های خودکار گوگل پیش از اصلاح صفحه، این اطلاعات را در نتایج نمایش داده‌اند.
🔹
گوگل و بنیاد ویکی‌مدیا این خطا را تأیید و اطلاعات جعلی را حذف کردند؛ اتفاقی که بار دیگر آسیب‌پذیری نتایج خودکار موتورهای جست‌وجو در برابر خرابکاری و اطلاعات نادرست در منابع عمومی را نشان داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/455999" target="_blank">📅 03:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455997">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d869c619.mp4?token=Um2aC74Q1Es7Z24LLB5nSvkbvQz8PfZhgbwsR6nwcdhQazpAkuqMjKY7OuS-4lJHRO6a6k254ZtSwOuLw8fwfi0HJHwG2V19GjdM--tfnE5bW19d0bu23VcTzsK-ImENMmryrFr8h328WNDRFx2yHorjFLdd5d4YJAYN-ou9Ug8ut7AFjCrUXrLr2KDDBJP_hHBQDd9k23Zd73Y8IRO5QGr6MXYv18TavasciyZmYYzDG60MA_gRdEiBndwqPHpElDi0OSPwW-Qq1dWoeX4N6tYyq3zPheW6p-8D4YyYl7wLzTGq0GZ9ZuhDoBKuoLq9X5VRY2uijxjdsFSLFSLuOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d869c619.mp4?token=Um2aC74Q1Es7Z24LLB5nSvkbvQz8PfZhgbwsR6nwcdhQazpAkuqMjKY7OuS-4lJHRO6a6k254ZtSwOuLw8fwfi0HJHwG2V19GjdM--tfnE5bW19d0bu23VcTzsK-ImENMmryrFr8h328WNDRFx2yHorjFLdd5d4YJAYN-ou9Ug8ut7AFjCrUXrLr2KDDBJP_hHBQDd9k23Zd73Y8IRO5QGr6MXYv18TavasciyZmYYzDG60MA_gRdEiBndwqPHpElDi0OSPwW-Qq1dWoeX4N6tYyq3zPheW6p-8D4YyYl7wLzTGq0GZ9ZuhDoBKuoLq9X5VRY2uijxjdsFSLFSLuOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از حمله به پایگاه‌های تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455997" target="_blank">📅 03:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455996">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
منابع عراقی از حمله به پایگاه‌های تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/455996" target="_blank">📅 03:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455989">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UA4AOMBo23qVauHIKtRcrYps1yGuAuUi22qcdu1_oytWiGDmbNLccMeS6X1-GQE526gkZV_XNqVOoKsDlMCj2RRduMzKZ_UXXJHNoWbtAErJ_xRD_UnpLlVwlZeSO34UCExoLHYCaPPT26mrPzl0m6rDwcZ7PPueVHXIRHAVXJ82nwJw73tHOmn7A4B23VKxkqgYSTI7hUC3w8rKHokmvv7pbwd_NiNBlLZzGXKdaSLxVgxI99ERcPHOMRvrUcNd_aUUkGhIPLqTboubA9so3X5pKE9-HkYhl8UwSWbh-OzQkzWB8Z2Q9SGCFVmLsTvOQCq0UPOb7GSL0RL61q_djQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZTvpZxb5hrKqu1HSm9kTwB_05IdRBSQmTh-V_hNRccbtPsQ0b_2pdAGGVnAQw5cyVd2Zi-ciIsIKLFbrAspn5SZ1G9HmlmKmVn3wtg1kF2qw1OefMq1qNZetg-McYxUXcmEFj18tG9okTJFWSQnuicm7IIdh6V3sXY2H_lIzDvd7WvNrgY74PyrYkGeveq6Xs4Ikikql6viNpQSN68jYVZgwkhezbTpFcIpu0rXjlc3eQfsgKrB02wARTmwXGCwIpvXzHfClxocE7azJu4hJK9ZAwNNuKZDhvJNLJm1XYScHzrQOsVJHmbw_tPghVvu4Zy2VwDl6SlwPfh4LYKGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDEl1Xbq_EKNj2IAhexeOoRn6kmbMk7U2eENaZjS21GEkFfmb_OqR7DMxb9yMO79jhJbMVkoVfT1j1Q_5MRk0rVQNxbAu-SKOtPkxr1yD9jaKnf8E3nJSy8aYzR5aWb0gUyAZhVbg7q0H0ycq92XTRQhaa2tHBrD9dV6OtVZIcpxL4WCO8ujpWtQaN6W_lqPOCzzzXaWaV2eVPfvQfDu4Fdz2ZqNS1Jc60M57UtlXdvbj9AyPMNOuO2Cikqlyuz0xF7Vw3O5Y2T8b9VecvOWwzmh0Gd_ICaLutwmk9dzoJ6SBuxuFnp0zNGL9wzFD8PkI_xSIIhcHMvCzL_1370VrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQmsBXg6JscwGsAF1epDQmILGU0qEmuQbUfXtENngO9BL_Cumfr_6h6xwOZ0JIU7W0D5-0cbpEkhr9fgYjEEtscEpJgTsclMTU3UcePNz5rocAEBz9KWDyVr0JQRwOVgRCXH_e6Z_Xb0zxSiTVfzzqKxoVpl1wDUA3GHqdnP3AKvnc7ytpMEzHB0bwC5p03mpJFAzaiXby5IBdZ85XVrjQFEnavUvEXi1TWJpkNz325V4Gp9Zfz0Jb_yVU00LT9F3C-4k69RyLIcEuOztscy29tq2GfZ8bG5kRrACJXH5hVmkGYvQQRh9fqRrG6qp1SX3sF9nlXXnm3e2JSNLoarcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LFKdR5f95g94h3N5xudCl9XxB3CqFPg8A8gxkI1Ja9Ri_tNngjBi7x-G1UpJYu3Ib8o2WTXKGZLPUT5KjqcwlRcZLAh53GuyudBY3Nk6aIU-DrC9O2DPw831BloNxELb6ev3kE5K_hOUtBlrgQImqdHDLUzFaPcqpe6ukcFHnZQWL5PwxgkpKSvexodIv2jtR060X-014Ce7U8fw8xt6b_H9FflCEdKgjJvHysMTAq44WJCJjwuBZfboEJwy4rzgHXyN7CpJCL3-JTj5AZDsq14T6VuXuSZVaeaIZ712A7cM-F15Rb2nx3LSXVm7Ki52deqh3UqQmwWOmVAsOm6PgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUk7D1-29IKSzD7EqsqfCn4EmspQjLupTO9OL5zeEF30kFUfKBn2kilQnBxXVXFG6pAa0pIdRRT2bMpx5U3yVPrBbw96uMw6nZyRDrIrM5zjsCc3X4Q9HOvLKubpcnssA_wgzHMtKh_vj4vPButpRQsCl3CSGfrNCmFwWP0_1XnlRH9VvVosiVbXcMg0EWTgjDQyfIx-i7q1P41B60OqBymAh-20WhWI5zP9jRWXWD-XcdTkkdRxtt5N9CczvjB6sOBqnF_C53z1a3XnzWkbkZcRzIvn-yRtefGcntK2YuhZd7ZPXDH_q07OFrZLEdWIX4t1XFEBdMvxaFnrgj4nnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsx4JC0E16ySm7Hualkl757oyI8r_J1kIDJQVEWWoPAwM2x3fcltjmeJrEik8Ysl7b9dGoPPCy0T3TsH5n9QEg2gP7BXUJYaTxpNTlie6WKblefku3qxycOEqluGBvTx_yIuHEQBbOXw0iXBEx2SPFEB4ftjFrj2fPDvBHy-VFP7st_56CZArtWn7zH_4GLOwst5dU8Mmdx6J5WPcommmGtN-G08qxH6m8q2NC0bAoyrftNpw6D6st5puvQDv-RkEJYipXxGrLQHvB3Brt15apG8Sckx1MoFW1pdLtIoI2L2OPSO68z5GqUS9Pk2wgcje55F8NOQg7Qw6z-mL0KLwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین شام غریبان شهادت امام‌رضا(ع) در حرم مطهر رضوی
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/455989" target="_blank">📅 02:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">منابع فلسطینی از حملۀ ارتش رژیم صهیونیستی به نقاطی در شرق غزه خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455988" target="_blank">📅 02:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455987">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر انرژی آمریکا باز هم فاز کنترل بر تنگۀ هرمز برداشت
🔹
در حالی که روزنامۀ وال‌استریت‌ژورنال با ارائه آمارهای جدید ادعاهای دولت دونالد ترامپ در خصوص کنترل این کشور بر تنگۀ هرمز را به چالش کشید وزیر انرژی او بار دیگر ادعاها در این راستا را تکرار کرد.
🔹
او مدعی شد: «ما با تمام کشتی‌هایی که از تنگۀ هرمز عبور می‌کنند هماهنگ هستیم و تعداد دقیق کشتی‌هایی که روزانه از این تنگۀ عبور می‌کنند را می‌دانیم.»
🔸
ترامپ بارها مدعی شده که کنترل تنگۀ هرمز در دست آمریکا است اما وال‌استریت‌ژورنال روز گذشته گزارش داد از میان ۱۶۶ شناور که در ماه اوت از تنگۀ هرمز عبور کرده‌اند تنها دو مورد عبور از مسیر تحت حمایت آمریکا در امتداد عمان انجام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/455987" target="_blank">📅 02:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">واشنگتن‌پست: یک‌چهارم پهپادهای MQ-9 آمریکا در جنگ با ایران نابود شد
🔹
واشنگتن‌پست به‌نقل از ۳ مقام آمریکایی: ارتش آمریکا در جریان جنگ با ایران دست‌کم ۴۵ فروند پهپاد MQ-9 ریپر از دست داده که می‌شود معادل حدود ۲۵ درصد ناوگان این پهپادها.
🔹
ارزش هر فروند MQ-9،…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/455986" target="_blank">📅 02:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455985">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">برخی گزارش‌ها از حملات رژیم صهیونیستی به مناطقی از جنوب لبنان حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/455985" target="_blank">📅 02:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455980">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3NhMfOgLCUq8viJJNbLNEu0IjGUpT1YHptSQR9huML5NmWp8JFKS1P9ZrkPym_Wx67MLHg7b0rAiW5sybkIyJZyVqfjsPv6rTfugIWX08G00NXY0kuMt2jYAGTaYml75CtUCv3JDoJdgggUbpcpnIBP73gkOFeahvRpx7wu0d8BOG_6_JQUImh-yFmlNYquxQ4y-fEqdFlGYwW-AIeHrj5nXCUODU4-XWtYUfFYvh1qo8N8AaxQfLFth_Udx9laCfqSDnAwZlUHXMDG6dcPKLZf2b7TOSBxRyE0cR8F6Iw6JJcPmuf1TKsUqDd7A_lY9DHvJoubPVjOH-P1qmOh5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKr4cqeqIC214fTXsdGfXU7v5NBVIaYiyr8yHj-aSFTmbV-t8Wnpkr1l2oPmGIKaE4VWObmWawWANbIq_EfzutPteBvZ4KAdy0xC4ji2R07KtUsCtgxWnt9MbQcsh7epguHnLJ4L3xN4AvF0ymEDJuohktY84CzuHi4NLjnihu_yXv23o4c-7iudT6dXbHAWrwXTpRXR-9BjRHgrSui6L95bexfOvAFYBjyOxOCjeQwhrGBNcoLXyHTu0MsTBhFhPQt9521do3B83wQ8m9v7PLYBs50XzrEgZqFFDyxsXZ8xmO138pOisIHPXpbBIGugEvdRBUkUvJ_h7XqT9UhshA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVaoHOuJ5jh5MZUbPfEcKzF5vG3tddjkN9BOuJGNsW8MVGv8A405cgulW_CtHYkEsFeIMwRZSSKkoe2HIakjm9sK2M-zqPIedrR_TM1H_Cips7GeRPNRou9B0xC0iGXdr_gIw9nOqFJS73KGHT8fZb3xU7oZVeQNarpOoaV7UDMVy4g7y5ZzLgceXTGnkJYEBJl1hfwA5xMLy76bYLSUhNgIEkEw9D_ifZLGE19z2Z07QDY7ZyEQhx4YHkkqrmD_sW0xr9AMJ5p-4Hz1F190PotJFffBeaB5TsnH7LKik-9zbzmboLAWGBicKfeSctLz3PdMJHAgPV29jwsb8cljEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpski_0Txqmki6yW9XXfcf_l9HAqiQWW5ZAN_n-EylxWm5bG1w-IAI-hJ3Rh_8HjA3ZJ-Er4tfykHjnQczLqpFZpdvrxp5Sq67DddwXCgh1klYSbPR7gmZakGndXqZYooQCCn4qd9_ndxtKUUoWMdq8tf6e1Wz4CVW3mf125ArJQLIHR_GSM4QqAb74zvCTax4wVirPtzKhgETwEqlV29ecfXXzLxlpcp-zYTO0qCU48g5_eyC3bfYi6a7_ijdJoFkrN6BkCHctEWTt0IuP7GhH4lWK7gsza19eaqxEO9XIYjE-5QDO4frxsfQ1agzzamJIg4ZmlV3RyxBjEGcwrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JoN_nuhBrDWN_DH05186Ws70is4_eEYyfLj0t9hJPHcw-ewMg3neMtYXVZQwQexD-7vHM4qs6uvLCMPoPxnYmOKiPWnwiRI8uVhcBJUk9Vz89AryAQ7jdHGFQNx8trm517BmDupcf8OxfVRg2VbwFOKEhmxho9MhnCX3wcPlCsPJVGP0OguQ3n3QkVLSHBPokzTIT4A_DoWSY9fCjfvqoXfXv3sy-Yn7KFiDzBWW6mfoj7lkR5cnvZeFAlXLanM4foNODBTQJjrRhikTb09-Hwij4y0_83xrO66ZVmYZQk6cCYmXBX0J01DU5j9H5Q_oJEeU1AkdOgiMS2qdhcreDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزای بوشهری‌ها در شام شهادت امام‌رضا(ع)
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/455980" target="_blank">📅 01:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455979">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هدف نخست ترامپ از جنگ با ایران: بازگشت به قبل از جنگ!
🔹
جی‌دی‌ونس، معاون رئیس‌جمهور آمریکا در مصاحبه با فاکس‌نیوز گفته که نخستین هدف کنونی دولت ترامپ، حتی قبل از توافق هسته‌ای با ایران پایین آوردن قیمت نفت و بنزین است.
🔹
چندماه قبل‌تر سخنان مارکو روبیو، وزیر خارجۀ ترامپ هنگامی که گفت هدف نخست جنگ در حال حاضر بازگرداندن تنگۀ هرمز به وضعیت سابق است با موجی از تمسخر و انتقادات تند همراه شد.
🔹
حالا هم انتظار می‌رود این اظهارات ونس با واکنش‌های تند از سوی محافل سیاسی در آمریکا مواجه شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/455979" target="_blank">📅 01:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455970">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/obKvusSYuwUETATI7Uwf_nG7Bxuk_WMZ7TOweNLWdHPNEEe0_LTg-YGHH63KanK7gG6iQcG3A9Fnm1PC_Y4FGfqzA6tI_rkAAgB6zwYVaBJ_3BvSkgvGdcrqzsxZ8_RocEuUXIhWQXmZxeP9tdW-hLICB69dOB7-PdO135d8QkZll9C7yBvg4J6ILQiYoE4TQN9MVZd7KhJHSovSlXApEI3Kapp_nTageJKK69GZ6U3iDFnu1_k9-2_O1_h7k5fxTZY6FPT90amoNgSyTxULuFgUhsqGbSkpaZo3wIWearEI6BA-mDB4UPz-1_15gZz6C5K7uOU7Hf8ukGXwXWZrrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6-CKwwvcnKAgo0MrNMftoTIP4Nd2B2Kh_9LwgxgZVaCngp50YxRCjRGj1UsVexCiizScGrvkZD09CcoxvD2_nWyyaP_sQER2rxsUYim4EHioskKYsYhN3BxO8bE0g6vKdYAWSdC0M4fwd6Oeu2MfappZWIhw97MQWzOTaoz_hxud0K692-9i-xuGE6lzMQtljGxR0PHvtueadyJj3j06Zr8hHTYfIsMBA00wr7NdABhVTZfqYMs598x6J38Oijk23BJfZExiR-AurWVndmqlWcpVja-QgkcwwtjRxkZX0CXlVTToxmrkKmkG9NYfajIiwS0bukgEo8y5yNXUg9-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FoJNXKydG5JoW-Jv1rrma4oLDjYV0ayXWuN_u2vq8LQ2Puf6ymfOOyjp8WXQgP8wCJ4UlzgRUPav2awJlYdl7cL8R84Ae_H9LY7XlMXwRGm4nz1Y9D3p79JIY7XqwQoG9PhOdgG0SDQlgZ8fSSoWTcpFPa8SYpEhfNAnsbDJ_J7FAy7JlQHPcExBMZqt8IfvINdgDQwDtvAcoqhWbchLs67dEHRK2-4uto7ExYDEQ0lEFBcWx5rwptTLcplVjx32hK9kdmJXZYDtsq9bcdalLIGj2qU4wKWhxzLyjf91vqKJpsDn1KbKevDjDkRrnzDmScpwv8GcoEbEDaJtatw8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XgrLA_rIRDVW5YXzW2L175Qot93eIXc0REc6RXQApQOt35hbRt05RiEEt0nBABRlhy085M_RF5ZJkh0Pk0oOLWcm0FBQArNzvcCFP_O8InT6TKRm6vPaXZdP7BWe4w87bw3N6cT-VmK075ELDwGWQc6J6Lu8IuPGaEM-KKO0UFUhGWALR3UznJAVNtOgu2nVfF-GCmucZd7GLsJG82WJ5uvSg_BA8S1HEKXvjYSfJ_XpFhpsk9Xzb-gMhrUwAKhNL28w90glRR8hCk0z6stT9LuJRRdTVkyhyuNZnSobGyrtxBJOefmN3PdsUfoBmStMin1krDXm3Sjx4X_TadS_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfnTkOzK9_6aHoNLu0_w8oKyfSm7GEnDpzpJJEOM3dUncZrnPPoaSmKWyNJVGB4tnC6deP7Yk2ba182xWmNkJ0vXQvhKrebQDeZ1j_1hVx_6V4vWDsulSOM7GuiffV6VgSocpCoFYTeEw7NQ_LSS4E_iTLo-bNHkpgTZ2giH_Q3RNO8nUJ0weqnnxXPUjutGMXozF2vRICqwAOXrK1jZCUgFMJyjoSyqjdGA11Ri3whv-TlQa2YL5gwDe9lo4tUq_aU66DCUtvgBhoLbCxcOBo3bBt6l-NzAnHaRtJXThBALJDD40p9A-MA6tbyFi2_d99yONyyamKvhm_E3yclLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDST6P7QvPAx3Wy7Itywnn5yA_UjtO49X-_ezH989OtmK05yzs9vBTwb64M9TVB5sf71kT4VLz4yJIEQkXB6R53Oe9Keb98SgvPW5y9x7wqUNzDB8XbQdZV6RF0Esuy1WUkqJ0OBiuYbjBb8Y63QNlgQczbYjmHfqhf5RvUJtXg9fWIbGGMIGr-1gf9XEIxpZcbMdGUqnmYMvBT3D_wfAkUpnscy1lahqfnlwkZhGzi2-783CAPPWIrySvxBhEPKC47VA_4OpE4TVC-evG_ZIor_PDTTpYUB9tqyLXaPZroTHOkSZK4PvxvwNOfsUIDl9nB_Qq14BA86BCJUK2RiNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bk25gabMI99NbO_tkySw89Tdxfj4ZCiiWyvSWfuARmD9-ui3wKofgpAn6bUIcCZznPSRS8aNu4bJxlXmBNqA8MEtlEQmsuaq55S5IMtM6vl75xheV2FPwd-aIw0blpCNux9nGLpAt8sAdYKKGgJKBQ71APafIRgdcImgZEMk-_BXI44FvKBVpTbs-ppxwWwlxWre6imkKwz4FyFnKiNG59lGKb4nafQDH_gpf0ZJ6DjIhggYLnBWkdb6618A-EkJteTEceX_WuRYd1rdGFbqYDrTssYRrCPNK_RDWob7jf4Sg9IFNkW2AXRnYTFZMbYF7I-vOKtddH01uvdqoX274A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I504MNmBzf8PazPu2Isb5180_AgLJygQek-OjkPqMqBn_2VKrNildHo4ps9my1oyi2-u7N6VouJC5wdySqDjzFGV6STjH9Rse25VRJ_qEPZVFjjlYpjQIS7RodPjTabBFKne3RjvG1RoRijkMNy7swdm2mFf4t0eWjdUhzah-3Y1BWQRf34LmXkt0uYPHnMwjhjfRqJAK-xaJgS8tF65YwcPfZo6LVmpOqd_SogAXPGZopxJ23TP4r0JEMG14JTr0oVHozCTgwGRamidTzh6HRr0yrfqrbwRJvCkr9yQ2uRdZnfvPdQ4dKrQx1i5Pb-DxDZz9tXoxgff5hB-EcKUZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/go0XvrhbCMqi0rJ8EG0h8gfCpZyI1usz92LYHDeM0ELCX8zBiJfG-YP1snrVVDe_2S5v6QRFU1z23-p9IvnCPjp54PtnOI8Qtzsq65tbbxH_AoWLnSPE2HjE7x6d08RuaIBGvDOTnwuFwvqodd_upjbHOII9rgZh6FSDiTi46E4kBg6dzIltQ8TymxiF6pU_95QeQoq8UVCMWQ6iH2yRYDHClNlrZjHJG09Z0kVUaJ4igQdeluK396BsajluYXF1W9pFyhJOSs8wPEUhCunx7U7CnYpMQhHAdHWDgjLorkZMMcJb0B4coFjT_r75q_Z98u0BXXndxPWcz-9huXdh1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نذر داغ موکب محبان‌الصادق(ع) در سالروز شهادت امام رئوف
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/455970" target="_blank">📅 01:31 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
