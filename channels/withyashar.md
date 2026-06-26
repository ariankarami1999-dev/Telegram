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
<img src="https://cdn4.telesco.pe/file/VrBFWjSZbQjpGI-RwGZ3wZ8ONwVzniD9FjofM5M4RgAWAiF3Wpo3uJhOkKs5Hgwvlio9mZLO-yS7ya62T-XTzWczpeKGg3n8nNCB4hRqA_ABka4eZ7Q3_gjANNpehDnXAa_SCvtY1wXtFVeUVDHl_qRotquHBbtLGXlCL5Ofnjp4rjfosSxgVkb3y1wIa-WEZZ29wIUHp0SVi6Dzxx9kqG3uf-MNKMUpKOMHhWt6A98XD0tCM668mIV5eBv0NVk235ruDSvmV48OY6Alc88tFORcGabjDRgCgYaFGPEwHK7sJVmr7ivoHyvu2RjSn83pW6UxaOIotbgg9btlYJsmRw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 22:44:31</div>
<hr>

<div class="tg-post" id="msg-15873">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2d413441.mp4?token=KEygERooQ8gnxfKJwjFBweYrqV1OUiS5zjsK8WLnAlTSojXHCSytAmz4za1s98v2q-7yFFK3mdYd03Cp_Jh7nyaQbb9LOQEnEG67gaciK7wG0ob5nS8O_AjJJWlN3YGV3AorD_TXyd6s9VSAst6pDqdtTVesHSv-v7Fv-srWzWvldXsFapACtw7QOt7TqGaO7RwFZqx-XLpaYsyTKLkEeKXLz3A75KBFNKGPfQWuj6x9nM_VkwtQds9T-lCVudW0bLtViuKPpjTGn1oqCa1D0JYAIQX9UGsRRStUbdQKTm5Hw5Olg6sw6gOgxhOwl_DKG3IPJFMdrNd6XgKWHumV4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2d413441.mp4?token=KEygERooQ8gnxfKJwjFBweYrqV1OUiS5zjsK8WLnAlTSojXHCSytAmz4za1s98v2q-7yFFK3mdYd03Cp_Jh7nyaQbb9LOQEnEG67gaciK7wG0ob5nS8O_AjJJWlN3YGV3AorD_TXyd6s9VSAst6pDqdtTVesHSv-v7Fv-srWzWvldXsFapACtw7QOt7TqGaO7RwFZqx-XLpaYsyTKLkEeKXLz3A75KBFNKGPfQWuj6x9nM_VkwtQds9T-lCVudW0bLtViuKPpjTGn1oqCa1D0JYAIQX9UGsRRStUbdQKTm5Hw5Olg6sw6gOgxhOwl_DKG3IPJFMdrNd6XgKWHumV4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که تابه‌حال در خاورمیانه رخ داده است.
من فکر می‌کنم خمینی [خامنه‌ای‌] و دیگران در ایران از اینکه من سلیمانی را کشته بودم خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
او یک ژنرال درخشان بود. او مردی بسیار بیمار از نظر روانی بود.
کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که در خاورمیانه رخ داد. مردم گفته‌اند که بزرگترین اتفاقی است که در ۱۰۰ سال گذشته رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/withyashar/15873" target="_blank">📅 22:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15872">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ: اخبار جعلی گفتند ایران امروز بسیار قوی‌تر از ۴ ماه پیش است.
آنها برای رسیدن به توافق لحظه‌شماری می‌کنند.
آنها چیزهای زیادی به ما می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/withyashar/15872" target="_blank">📅 21:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15871">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514bc17e72.mp4?token=CfhL9wIfC9oPXcxy_HUVvQrKOwP-UohWuuJgj0amhOqsLQ7wI-qQCT8k7G0t_Pt6S1fhJ8gFQe5NTUp90cR1ONEhrht5XC_7EDS6XRtLdBvD2H3M2bWJpWm1r_cJj5dnpNx8PJ2m8gFojI7MFRTS4YHs2CC_UtW8M5ye4O9EZ18xelDo4jVivo0o9ohvlXVFauI6F9nMDPKWN9GuPopxYE3TBPosMz7GIHfhP9H-8W_L50pyGjzyF-2Yfr1xxqgQFP7X_AiPUQCzjeQpAlNT9MWKRZOypasK3m9OoiPkXZUTRfrKgQRvjTjE2vUAdCm60PQVg-ZEWPtvMRVyJklMtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514bc17e72.mp4?token=CfhL9wIfC9oPXcxy_HUVvQrKOwP-UohWuuJgj0amhOqsLQ7wI-qQCT8k7G0t_Pt6S1fhJ8gFQe5NTUp90cR1ONEhrht5XC_7EDS6XRtLdBvD2H3M2bWJpWm1r_cJj5dnpNx8PJ2m8gFojI7MFRTS4YHs2CC_UtW8M5ye4O9EZ18xelDo4jVivo0o9ohvlXVFauI6F9nMDPKWN9GuPopxYE3TBPosMz7GIHfhP9H-8W_L50pyGjzyF-2Yfr1xxqgQFP7X_AiPUQCzjeQpAlNT9MWKRZOypasK3m9OoiPkXZUTRfrKgQRvjTjE2vUAdCm60PQVg-ZEWPtvMRVyJklMtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: دیگر هیچ‌کس نمی‌خواهد رهبر ایران باشد.
آنها پرسیدند: «چه کسی دوست دارد رئیس جمهور شود؟» و همه گفتند: «نه، متشکرم.»
@withyashar</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/withyashar/15871" target="_blank">📅 21:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15870">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d44d4d0504.mp4?token=EQS_e-zfz9HFt6xySQue0vuOA6TI-IK_1-N6-uI8iVK2BBrQPgUNsG6QRlVaLSIg5bmRLf5z4maafBsPnWK_FLISfCFGzpCeeGOBMBs62YaU61sIid0JOcywc9IDk63l_oH4lBA9BWHrO-YTZSj6CM7JBP8K25l-DrJDvlsoXLCSFtMutjVnbjW0hCI29HZcih8OOwh9xLPIIBNlFd7KSwbNda9M_S_e8Gpb-VTjsUsk5-WK_v0URsRMAXIGd2wQbSqjEsQGglPMJoheoHTqCzE5ISYFsEkSyENYuayHBiAIBWGyfMBZZbmmzK7ywBfddpAvR-wgB3IzGeYNry6HFU5Kyrf3y8WTSiZJAgoApVivxlXEHd_N79ST7AUP1n2HqFyOLU_Vc2STR3CHI00j2ilWLhbhNT7BQ8oTiAr47LRNiLE0PT6BDS0rlu9sAi-5uIufPuSkBeCbWLxyXGJfP82PBEGJBRqitSKOndL4ExWOdKg7ln3dGKlkNwjalGhndzEH3MFzPGsviXnoD7m4LS3Cx_OHEiiI4UqqBbjop7VfEjtYdldTcUSpPP-R_XDu_HkuzOc7Ml1vEYL0TEL2QkqurPWdKxQtyWIPmmTGzDqXMGFjXs1gxoPVFigufhVjRrCrVq_NXv_S7n3x61vEls4ZCPNsGh9jcWPpZW-3G58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d44d4d0504.mp4?token=EQS_e-zfz9HFt6xySQue0vuOA6TI-IK_1-N6-uI8iVK2BBrQPgUNsG6QRlVaLSIg5bmRLf5z4maafBsPnWK_FLISfCFGzpCeeGOBMBs62YaU61sIid0JOcywc9IDk63l_oH4lBA9BWHrO-YTZSj6CM7JBP8K25l-DrJDvlsoXLCSFtMutjVnbjW0hCI29HZcih8OOwh9xLPIIBNlFd7KSwbNda9M_S_e8Gpb-VTjsUsk5-WK_v0URsRMAXIGd2wQbSqjEsQGglPMJoheoHTqCzE5ISYFsEkSyENYuayHBiAIBWGyfMBZZbmmzK7ywBfddpAvR-wgB3IzGeYNry6HFU5Kyrf3y8WTSiZJAgoApVivxlXEHd_N79ST7AUP1n2HqFyOLU_Vc2STR3CHI00j2ilWLhbhNT7BQ8oTiAr47LRNiLE0PT6BDS0rlu9sAi-5uIufPuSkBeCbWLxyXGJfP82PBEGJBRqitSKOndL4ExWOdKg7ln3dGKlkNwjalGhndzEH3MFzPGsviXnoD7m4LS3Cx_OHEiiI4UqqBbjop7VfEjtYdldTcUSpPP-R_XDu_HkuzOc7Ml1vEYL0TEL2QkqurPWdKxQtyWIPmmTGzDqXMGFjXs1gxoPVFigufhVjRrCrVq_NXv_S7n3x61vEls4ZCPNsGh9jcWPpZW-3G58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم
«کمونیسم همه‌چیز را نابود می‌کند، اما بسیار آسان است. راستش را بخواهید، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
من اجاره را رایگان می‌کردم. خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی که خانه می‌خواهد، نگران نباشد. فقط خانه‌ای را که می‌خواهید انتخاب کنید. همه غذای رایگان می‌گیرند. از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی خواهند داد. در سال اول، شما محبوب‌ترین فرد هستید.»
@withyashar</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/withyashar/15870" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15869">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee8d4b334.mp4?token=j6p1F6r3k9zOXNfhOGue2ScQp0OO-fR4c7lvjByxXL7hfL-XironVhVTrmeFrbV8tHZPvc4o7VbyzEeeb41vtJmK9JKe93XN3h-W2wYkjPmeaCnxKyISsqDQu4r_4fCFEasHvcZ48X81B9-isY9OA-3tVCuS_jHOlJZOJ3y14Z_OP0TbZhfAkKch0Vdgwg4bMqf7ajHOwC6nugma2OzoDSsJ2uydglZtg2ectY31TBPXKkQqiGsOf8cg0_9-KVUKWommsHSdBPtSaTNmK5yVdRpkhyidilVcvoyATrkFNeTkXnOWQyZPy6bkhk4HwFX9Ezd8yzAaNUwERjwTPhRImQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee8d4b334.mp4?token=j6p1F6r3k9zOXNfhOGue2ScQp0OO-fR4c7lvjByxXL7hfL-XironVhVTrmeFrbV8tHZPvc4o7VbyzEeeb41vtJmK9JKe93XN3h-W2wYkjPmeaCnxKyISsqDQu4r_4fCFEasHvcZ48X81B9-isY9OA-3tVCuS_jHOlJZOJ3y14Z_OP0TbZhfAkKch0Vdgwg4bMqf7ajHOwC6nugma2OzoDSsJ2uydglZtg2ectY31TBPXKkQqiGsOf8cg0_9-KVUKWommsHSdBPtSaTNmK5yVdRpkhyidilVcvoyATrkFNeTkXnOWQyZPy6bkhk4HwFX9Ezd8yzAaNUwERjwTPhRImQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
دین درحال رونق گرفتن است
«دین دوباره رونق گرفته است. دین واقعاً در حال اوج گرفتن است. اگر دین یک سهم بورسی بود، همهٔ ما بسیار ثروتمند می‌شدیم.»
@withyashar</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/withyashar/15869" target="_blank">📅 21:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15868">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانال ۱۲ اسرائیل: ارتش اسرائیل در چارچوب توافق تفاهم با لبنان، تا زمان خلع سلاح حزب‌الله در مرزهای خط زرد باقی خواهد ماند.
@withyashar</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/withyashar/15868" target="_blank">📅 21:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15867">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6nEZYZC21Sewau_eiTS_srltduImOlisHNaCak7JxLtAPTOgxiviFDpH25CuQc5dShMsTKHYKoCAUCJDNsd6SByJkYlf1mVw6Up3XDWphd7Yb3hTTIMSrp78trEtI3gdfiYu-4iXiE6vYnTXX66Q0rGoORSHiOtE9nRMce17uSdcduhT5IYKKKkmSkTMUXpaIJkdJkH12o4WG6bje5KY_c_RbBVVFFWStgoete5kTYMRFnRmc1eJAry7nTKCbCS2oHoZEUdrjoowvdWaFKs5tg8LWv5Y-R-nIzyNofcHzQCaTtmHYZIQvmPozhrSxO4ZldbgFziLj7VnQSg4VLjUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : اتش سوزی نزدیک فرودگاه امام لعنت الله
@withyashar</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/withyashar/15867" target="_blank">📅 21:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15866">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">افزایش شمار قربانیان دو زلزله‌ ونزوئلا به حدود 600 جان‌باخته و هزاران زخمی و مفقود
@withyashar</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/withyashar/15866" target="_blank">📅 21:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15865">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ارتش اسرائیل مدعی تصرف بلندی علی الطاهر شد ارتش اسرائیل : تپه علی الطاهر در جنوب لبنان فتح شد و نظامیان ما کنترل این نقطه را به دست گرفته‌اند.  این ادعا هنوز از سوی حزب‌الله تأیید نشده است. @withyashar</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/withyashar/15865" target="_blank">📅 20:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15864">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرنگار آکسیوس از امضای توافق بین اسرائیل و لبنان خبر داد @withyashar</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/withyashar/15864" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15863">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خبرنگار آکسیوس از امضای توافق بین اسرائیل و لبنان خبر داد
@withyashar</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/withyashar/15863" target="_blank">📅 20:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15862">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سپاه : ادعای مقامات آمریکایی درباره برقرار کردن خط ارتباط مستقیم با ایران در مورد تنگه هرمز، کاملا ساختگی و دروغ است.
@withyashar</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/15862" target="_blank">📅 20:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15861">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ارتش اسرائیل: نیروهای ما در حال تحمیل یک واقعیت امنیتی جدید هستند که به حضور حزب الله در این منطقه استراتژیک پایان خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/15861" target="_blank">📅 20:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15860">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/15860" target="_blank">📅 19:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15859">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ در‌ تروث: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌ها در تنگه هرمز شلیک کرد. یکی از آنها به طور محکم به عرشه بالایی یک کشتی بزرگ و گران‌قیمت بارگیری برخورد کرد. خسارت وارد شد، اما کشتی به مسیر خود ادامه داد. ما سه پهپاد دیگر را سرنگون کردیم. بدیهی…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/15859" target="_blank">📅 19:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15858">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIdqX4ON3p7niSvJxaknCZ7GF6ybj0yg6W2nNxuySMSO9uTsTr5Q9hCIpifc10MsEnpZPoZBuTGPO3umY0w5R6ezoqjE3Ap09g7zRrt3Q-EfS1FwJhIlqcMtfswqp1PYY8hEF0EzqgRo5L2mu3U3QP7-__E9s2AP71XxiWOu1gi22zF3Zb1Ut5vVkOYVQ1jGlbezqIPPtph3uDIWr0tv2GzNDB80A0IGTC5b6_gjQx-gg9HDm6nirgJC-Rn6_bWZw4-ypjdywai-xKIi-GKt1cR_58qS410QdMfUVHoiORaEz4_r9jZPydzgpUMy27lcLXicPy2UV0kFM2N1m_G6fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌ها در تنگه هرمز شلیک کرد.
یکی از آنها به طور محکم به عرشه بالایی یک کشتی بزرگ و گران‌قیمت بارگیری برخورد کرد. خسارت وارد شد، اما کشتی به مسیر خود ادامه داد.
ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@withyashar</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/15858" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15857">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ارتش اسرائیل مدعی تصرف بلندی علی الطاهر شد
ارتش اسرائیل : تپه علی الطاهر در جنوب لبنان فتح شد و نظامیان ما کنترل این نقطه را به دست گرفته‌اند.
این ادعا هنوز از سوی حزب‌الله تأیید نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/15857" target="_blank">📅 19:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15856">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه: عمان به اروپایی‌ها اعلام کرده است که دیگر راهی برای بازگشت وضعیت تنگه هرمز به دوران پیش از جنگ وجود ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/15856" target="_blank">📅 18:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15855">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دولت امارات: در حال رسیدگی به یک مشکل فنی در سامانه هشدار زودهنگام هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/15855" target="_blank">📅 18:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15854">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlppBr5-tCcHGnsA2cbRF_pF1nyVhzGondo8wT1NYCbeNOF6fEa14k43w9nPCqJHlbyfLd7s-qdWi1FVY6ztDDRoAPmdCPrw0jRqCb6pJHfElMEIn1IwwXaAf59Ni5cRhkptUXkR0GCUkKHMUmPAR1QnBtoONudh90tlW7xyzWR2ISelBoNTYZp2UPkJi5glzZkbia2PzOzgE6uKvMg9uEwd_l2Ijadv6OJWv-rqKFCMUv-4vHpwGiVxF0BPk1MCveH1ecMCDaZxKgzyk07fBncft5Y18hnMlAH-dTqem4XYU0gLt5N6Nbpu6MqVVux3wCdjM6q1prK7NTTjDLWKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سیاتل همجنسگرایان دارن از الان گرم میکنن آماده بازی ایران و‌ مصر بشن
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/15854" target="_blank">📅 18:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15853">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جان بولتون، مشاور سابق امنیت ملی آمریکا، در پرونده نگهداری غیرقانونی اسناد طبقه‌بندی‌شده متهم بود که بخشی از یادداشت‌ها و اطلاعات محرمانه دولت را خارج از سیستم رسمی و در محیط شخصی نگه داشته و در برخی موارد برای امور شخصی استفاده کرده است. او برای جلوگیری از دادگاه طولانی، یک اتهام سوءمدیریت اسناد محرمانه را پذیرفت و با دادستان‌ها به توافق رسید. طبق این توافق، به جای زندان، حدود ۲ تا ۲.۲۵ میلیون دلار جریمه پرداخت کرده و پرونده با توافق قضایی بسته شد.
@withyashar</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/15853" target="_blank">📅 18:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15852">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دقایقی پیش وزیر دفاع اسرائیل در پستی به زبان فارسی و بسیار غیر معمول تهدید به جنگ با ایران کرد و گفت: فرمانده نیروی قدس سپاه اخیراً تهدیدهای متعددی علیه اسرائیل مطرح کرده است، به هر حال، اگر ایران به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد،…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/15852" target="_blank">📅 18:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15851">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اتاق جنگ با یاشار : بررسی وضعیت پروازها
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/15851" target="_blank">📅 17:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15850">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۲۲ خدمه ایرانی نفتکش توقیف شده توسط آمریکا، در کراچی به سرکنسولگری ایران منتقل شدند
@withyashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/15850" target="_blank">📅 17:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15849">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">امارات : لطفاً هشدار قبلی را نادیده بگیرید.
@withyashar</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/15849" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15848">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وضعیت عادی شد
بر اساس الگوهای پیشین، در مواردی که در امارات آژیر هشدار فعال شده و سپس به‌سرعت وضعیت «عادی» اعلام می‌شود، معمولاً این شرایط با رخدادهایی مرتبط بوده که در نزدیکی سواحل یا مسیرهای دریایی و در اثر حمله یا حادثه برای یک شناور رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/15848" target="_blank">📅 16:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15847">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">احتمالاً پهپادهایی که از جنوب ایران به سمت کشتی‌ها در تنگه هرمز پرتاب شده‌اند.
گاهی اگر مسیر پرواز مشابه باشد، باعث فعال شدن هشدارها در امارات می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/15847" target="_blank">📅 16:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15846">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/15846" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15845">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هشدار موشکی در امارات</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/15845" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15844">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/15844" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15843">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دقایقی پیش وزیر دفاع اسرائیل در پستی به زبان فارسی و بسیار غیر معمول تهدید به جنگ با ایران کرد و گفت:
فرمانده نیروی قدس سپاه اخیراً تهدیدهای متعددی علیه اسرائیل مطرح کرده است،
به هر حال، اگر ایران به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد،
هیچ چیزی ما را متوقف نخواهد کرد،
نیروهای ما آماده‌اند تا وارد جنگ شوند.
@withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/15843" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15842">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0BOvKTQrBIlfzpW7BHJfqgbJzkBet6OEsHv1bXH7DyAFLEkIsZfbBgWUCCRfhYfrE72AxHZ_rXwTIK4SDnJMLylTF9xwFX7tl9aSbCUMnFj-mHsbf4qaA1Mj-X-8VFcplrbsBG4HaEe2WK4u0zIuaUanFSIA3XrU8dKT--rLjH7x5F3H52gL2HnEL6lX1QnTrnsIwtSEZT5YE76oJXO2C6-2IhH0grEvtkYXRU54KO4oGjAVbH3GcwdyUnkFm46sqzHQjRZY1lf16dz-Hc3ae5QC2qJTh67HxFQZAick_9uZX-vdjCOo4uWmzLgJQt9XXOVAEhooncmY1xw8IjX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت اعزامی به انبارهای گندم ترامپامون
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/15842" target="_blank">📅 16:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15841">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">العربیه: دور بعدی مذاکرات آمریکا و ایران در ۲۸ و ۲۹ ژوئن در بورگنشتوک برگزار می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/15841" target="_blank">📅 16:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15840">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6b7f6c830.mp4?token=nohB6lI4aW_xDH99rNTmCYucy29Ib-6TOGEKQMpIcwgwWkezHMWWrsHg216hhBrIkTWsd6pjGKK7jzQ_0ClTvFit8w0FO_9lU0U_xVkZDZXCPqyEzkf1E0EnrIxRAptA7huIAxt_UwFo3644bKOuK-77qMfDFLhh4qB2qyTmmc1hud4BeIUeop_tix-yLP95H1RluXcjeROH-lNoPTdW_sNK4bnaxBtYjVmJuqyaHQsiunAsdMrQn6HffQlkMwqEwCk_BLxAtCpzd8GKhF76ww02mrdyh-DopLSzff-bjCagY96gdnhNmhjqZIgPUtFaz1X239GsNwDmWFbsPNaMMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6b7f6c830.mp4?token=nohB6lI4aW_xDH99rNTmCYucy29Ib-6TOGEKQMpIcwgwWkezHMWWrsHg216hhBrIkTWsd6pjGKK7jzQ_0ClTvFit8w0FO_9lU0U_xVkZDZXCPqyEzkf1E0EnrIxRAptA7huIAxt_UwFo3644bKOuK-77qMfDFLhh4qB2qyTmmc1hud4BeIUeop_tix-yLP95H1RluXcjeROH-lNoPTdW_sNK4bnaxBtYjVmJuqyaHQsiunAsdMrQn6HffQlkMwqEwCk_BLxAtCpzd8GKhF76ww02mrdyh-DopLSzff-bjCagY96gdnhNmhjqZIgPUtFaz1X239GsNwDmWFbsPNaMMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل برگه‌هایی را بر فراز شهر المنصوری در جنوب لبنان انداخت و از ساکنان خواست تخلیه کنند، که این اولین دستور تخلیه از زمان آتش‌بس است.
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/15840" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15839">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ارتش اسرائیل برای شهر منصوری در‌جنوب لبنان هشدار تخلیه صادر کرد
@withyashar</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/15839" target="_blank">📅 15:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15838">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدا و سیما : سه نفتکش خارجی که قصد عبور غیرقانونی از تنگه هرمز را داشتند، پس از هشدار سپاه پاسداران به بنادر خود بازگشتند.
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/15838" target="_blank">📅 14:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15837">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1wrbtUEDw5jrpiwDYQmbiFAyVK0cvVv4C82-Oee2cAODE2S5cZZhlOpKtyMipnBSJ54zb63zaxp8qszlYBWSCtsbBK0l8Z4QMUhwxIuzyG1ZpuIH37vO8lNQDN-qFSs40Mw8qOLMQENDVejSC1Y7HFVS9hjHC13xU6HYC5vhCKZnfog1v5_BHjsgTr4bSE0grq0jITqcOP5XoooDpwS9fzhpgT-wctk8E-XaaGF8_X4p3gqYqBnBcZU8FntsmlYm8nMa5zyXYHm8hjxCIZtrH54OlviQpLw8ZYhBliiwbNGglRNDT0Xvu0ig8WHKxEDoenxwOwFFaHzKVCYsdcxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارداد 35 میلیاردی پنتاگون برای خرید موشک‌های رهگیر سامانه پدافندی تاد
وزارت جنگ آمریکا قرارداد بزرگی به ارزش 35 میلیارد دلار با شرکت لاکهید مارتین امضا کرده تا تولید موشک‌های رهگیر پیشرفته THAAD را به‌طور قابل توجهی افزایش دهد.
بر اساس اعلام پنتاگون، این قرارداد 7 ساله قرار است تولید سالانه موشک‌های THAAD را از 96 فروند به حدود 400 فروند افزایش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/15837" target="_blank">📅 14:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15836">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">برادر زاده اسماعیل هنیه در حمله به نوار غزه کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/15836" target="_blank">📅 14:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15835">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فارس: درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است
@withyashar</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/15835" target="_blank">📅 14:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15834">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly7WhgeZPx7BijlTSQ2RQjYFfJ-KaO7r4R4s6NRJyXgbpgZw5avOrkIyMQSM5y2qdiWSTYOknKmpTwJTVb1ED6XDeHCbIVQSoUA83rTq9eKwNqKubPc0PRyXfVu3APJx7F3712cXGz8907GLYklzElUy6e19x1mX8nRRVtkly74PTlxgFQnQhKliUk5WEuKeyWx_z8VizPmrJ5WYpW9ObIu2d2C2Irvr_3Mc_EwVO7CGEwa-5lfaXrFveAxRufzF2jqCvNNM2dVfQ9ABdxxgZicp_X6oXCRDvFocH2UVAze3XKZ-ifMVyLMeHEEzLJU10vHNMAmVVcM3LwYpoMQQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما با کپی‌برداری از اینترنشنال اومده کنار پخش تلوزیون، عکس کشته شده‌های لبنان رو گذاشته.
@withyashar
۱۸ مدل هم اتاق جنگ کپی‌کردن‌
🤣
کلا کپی‌ هم بلد نیستن</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/15834" target="_blank">📅 14:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15833">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e2d351d6.mp4?token=ScYovpsUNwrYVH1cEl4aGuaZgzRXx3mpJkwmiwP1dkvZWnSDD2z-cTb-u9O_jPp4pfHuQOUM9NOryfzGAAA3_bcnOEdVgQTE1kM-vL9JYhtLA8dIHjBAbopNt-3o_kdwXWuWI5GadlXloba8IAPEQfNeLp_a5F7cu8MPnlKtFzuw6-i3JqE5qVEeJC0c-gAZFn2e5ENK37aoG8AJCFmGzcJBwWhzbeomnk1uuyaAvDh6Tz7617hkOIiMGhbtHLiVT3jbk7g1qhZ3PZYBmD2fX6nFB8Zdf1i1-6BLvhAkI93Mll9eEdnq2V7g2jZqGArijDpSuGxNkbzX4ye66mdgXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e2d351d6.mp4?token=ScYovpsUNwrYVH1cEl4aGuaZgzRXx3mpJkwmiwP1dkvZWnSDD2z-cTb-u9O_jPp4pfHuQOUM9NOryfzGAAA3_bcnOEdVgQTE1kM-vL9JYhtLA8dIHjBAbopNt-3o_kdwXWuWI5GadlXloba8IAPEQfNeLp_a5F7cu8MPnlKtFzuw6-i3JqE5qVEeJC0c-gAZFn2e5ENK37aoG8AJCFmGzcJBwWhzbeomnk1uuyaAvDh6Tz7617hkOIiMGhbtHLiVT3jbk7g1qhZ3PZYBmD2fX6nFB8Zdf1i1-6BLvhAkI93Mll9eEdnq2V7g2jZqGArijDpSuGxNkbzX4ye66mdgXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درود یاشارجان
اینجا بندرعباس جایی که تنگسیری تبدیل به کتلت شد , عرازشه شب شام‌غریبان اومدن شمع روشن کردن
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/15833" target="_blank">📅 13:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15832">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21dc4232c0.mp4?token=cNOtWSRvaxTHPhqpdR4IrNskNRrVG-vD9sKePNJtNT9u_pS0Is9eYa6C8te8-_Xtw8plIEmwr2AYwoVkgRWbrLML-wFCugm-joxiQXMgVzEL7ivplTElpYjtpVlkmYv2PMvAHuE4omNicvbCfpqKiDfucTx-5UVtsER7vjUxHfGz54AnhF70YuGu5DfnKpF4CwvnQQmeu-GHD4pWkWhxeyzkCIJXOQmk3XCmMJjwNDf4oo-K7GT5lz96TCOdNCeZHFJMYfCkYzB2hcuAlADdPTlSgcb_vMJOLCBxkPfaonczSIvu-r7m975d6C7ZVz7Tv1R0mc0zWLXbAs4LaOEzQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21dc4232c0.mp4?token=cNOtWSRvaxTHPhqpdR4IrNskNRrVG-vD9sKePNJtNT9u_pS0Is9eYa6C8te8-_Xtw8plIEmwr2AYwoVkgRWbrLML-wFCugm-joxiQXMgVzEL7ivplTElpYjtpVlkmYv2PMvAHuE4omNicvbCfpqKiDfucTx-5UVtsER7vjUxHfGz54AnhF70YuGu5DfnKpF4CwvnQQmeu-GHD4pWkWhxeyzkCIJXOQmk3XCmMJjwNDf4oo-K7GT5lz96TCOdNCeZHFJMYfCkYzB2hcuAlADdPTlSgcb_vMJOLCBxkPfaonczSIvu-r7m975d6C7ZVz7Tv1R0mc0zWLXbAs4LaOEzQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز خوراکی خودش را معرفی نکرده بود که حلوا است یا
💩
. بدم می‌آد ازتون. گشنه‌ها. خجالت می‌کشه آدم اینو استوری کنه. می‌گن سهام برند طلا و جواهرات ونکلیف آرپلز ۵۰٪ ریخت، بعد این ویدیو.
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/15832" target="_blank">📅 13:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15831">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شبکه ۱۳ عبری به نقل از یک افسر ارشد اسرائیل: فروش جنگنده‌های اف-۳۵ توسط واشنگتن به ترکیه، آزادی عمل نیروی هوایی اسرائیل در خاورمیانه را تهدید خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/15831" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15830">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/15830" target="_blank">📅 13:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15829">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">https://t.me/boost/withyashar
بوست (Boost) در کانال‌های تلگرام به‌صورت مستقیم هیچ درآمدی برای مالک کانال ایجاد نمی‌کند و قابل فروش هم نیست. بوست‌ها را کاربران دارای Telegram Premium به کانال می‌دهند تا قابلیت‌هایی مثل استوری کانال، ایموجی‌ها و ری‌اکشن‌های سفارشی و همچنین ارتقای سطح (Level up) کانال فعال شود؛ یعنی بوست بیشتر یک سیستم امتیازدهی و فعال‌سازی امکانات است و نه پول. بنابراین مالک کانال هیچ مبلغی دریافت نمی‌کند و بوست‌ها تبدیل به پول نمی‌شوند، قابل برداشت نیستند. در جمع‌بندی، بوست فقط برای افزایش امکانات و اعتبار کانال است، نه برای درآمد یا فروش</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/15829" target="_blank">📅 13:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15828">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12c8cc82c5.mp4?token=uKmdDnq6Lay62mJg4TTZ3bDBTFPiasuOvhWyh_ZwPBudH66t_tCMPiUsUT8x-btTrE9OlQocRQUGloowKGoKeLSg2a9klo42rG5rSy513RUrhmgYVvZHoJQW0eRFHGbjSHz7UjFHtJA6NlY1fjb9cSMu8Li-1Hpy8luyby0Tk-0z681KqNEDjw38fBnENWR2B-_Ho7E-oyA-QD70QjxywUcT4_PGMmPWePGppJ9HoMmB5wMY-GoVpftQeKCFTNhzEB7zYr1wOteSjneIcfUw52K7F4vD7PYDaQnJPMy_7t2ZwS7DVSaQA6kfEr64G5XrrUsUrC9Z4rOCG4Y0A0OplA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12c8cc82c5.mp4?token=uKmdDnq6Lay62mJg4TTZ3bDBTFPiasuOvhWyh_ZwPBudH66t_tCMPiUsUT8x-btTrE9OlQocRQUGloowKGoKeLSg2a9klo42rG5rSy513RUrhmgYVvZHoJQW0eRFHGbjSHz7UjFHtJA6NlY1fjb9cSMu8Li-1Hpy8luyby0Tk-0z681KqNEDjw38fBnENWR2B-_Ho7E-oyA-QD70QjxywUcT4_PGMmPWePGppJ9HoMmB5wMY-GoVpftQeKCFTNhzEB7zYr1wOteSjneIcfUw52K7F4vD7PYDaQnJPMy_7t2ZwS7DVSaQA6kfEr64G5XrrUsUrC9Z4rOCG4Y0A0OplA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش بسیار از مشاهده شدن دود حجیم در تهران
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/15828" target="_blank">📅 13:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15827">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بازداشت یک هکر رژیم در مونته‌نگرو با درخواست اف‌بی‌آی
پلیس مونته‌نگرو به درخواست اف‌بی‌آی، یک تبعه ایرانی را به اتهام حملات هکری گسترده علیه دانشگاه‌های آمریکا و آنچه «خدمت به سپاه» خوانده شده، بازداشت کرد.
اداره پلیس مونته‌نگرو  امروز در بیانیه‌ای مدعی شد این فرد از سال ۲۰۱۳ تاکنون حملات هکری گسترده‌ای را علیه بیش از ۱۵۰ دانشگاه در ایالات متحده انجام داده و خسارتی بالغ بر ۳.۴ میلیارد دلار به بار آورده است.
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/15827" target="_blank">📅 12:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15826">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تسنیم:دیشب یک گروه مسلح در نزدیکی مسجد جامع شهر سراوان تیراندازی کردند و از محل متواری شدن
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/15826" target="_blank">📅 12:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15825">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۷.۸ ریشتر سواحل جنوبی جزیره میندانائو در فیلیپین را لرزاند.
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/15825" target="_blank">📅 11:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15824">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: تحرکات و حضور هواپیماهای نظامی ارتش اسرائیل در آسمان برخی کشورهای همسایه به سمت ایران، اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل اسرائیل نباشد، جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/15824" target="_blank">📅 10:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15823">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نادرشاه افشار در مبارزه با هوتکی‌ها بود تا اصفهان را از اشغال آنان بیرون آورد، در یکی از روزهای نبرد چشمش به پیرمردی افتاد که با وجود سن بسیار زیاد، شمشیر به دست گرفته بود و با چنان قدرت و مهارتی می‌جنگید که گویی جوانی نیرومند است. گفته می‌شود چندین تن از جنگجویان افغان به دست او کشته شدند و همین موضوع باعث شگفتی نادر شد.
بعد از پیروزی و آزادی اصفهان نادر دستور داد پیرمرد را نزد او بیاورند. وقتی او را آوردند، نادر با تعجب به قامت خمیده و چهره سالخورده‌اش نگاه کرد و گفت: «تو با این سن و سال چنین دلاورانه می‌جنگی و این همه نیرو داری؛ پس چرا وقتی افغان‌ها به ایران حمله کردند، اصفهان را گرفتند، مردم را کشتند و کشور را به این روز انداختند، تو کجا بودی؟ چرا آن زمان نجنگیدی تا کار به اینجا نکشد؟»
پیرمرد بدون آنکه هراسی به خود راه دهد، سرش را بلند کرد و با آرامش پاسخ داد: «
من آن روز هم بودم؛ این تو بودی که نبودی.»
می‌گویند نادر با شنیدن این پاسخ لحظه‌ای سکوت کرد، سر به زیر انداخت و دیگر سخنی نگفت؛ زیرا دریافت منظور پیرمرد این نبود که مردم ایران ناتوان یا ترسو بودند، بلکه می‌خواست بگوید مردم آماده دفاع از سرزمین خود بودند، اما فرمانده‌ای نداشتند که آنان را گرد هم آورد و رهبری کند. با آمدن نادر، همان مردم پراکنده به نیرویی منسجم تبدیل شدند و توانستند اشغالگران را از ایران بیرون برانند
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/15823" target="_blank">📅 10:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15822">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDjgbV-Y17PK7vqtDAt_rFVfTQ7BfDys_MFO9zrlSBUFXfHrFLJWyidmJXjaqO13RAadIpVo59jICJamyiTc9RbaVkyyhlahfGn7M22PvnkZC5LjlMbwJ4Dm8H1QtfnzNHeRGqwxrgMNRkYl_nJiN7B_FrLLrQwOC-usXlKZx2d8K_7SNnu_661cNYTjv-kZ1hKtRS8L2uJHqEYZG7LMeR-tKgiAEnsKVQ7KYKeSNNI96M8Oi235BIqlokth2dzVrFrh2fvb2vs0Sgwt_QPbutwXxXlqZv9sIwnERor9gA8TwDzhviyryAgYw1h3W6Q1L1N-OOCzTAhasKNEuXBUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل به جنوب لبنان، ساعتی پیش
@withyashar</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/15822" target="_blank">📅 10:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15821">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سیدمحمود نبویان، نایب‌رئیس کمیسیون امنیت ملی مجلس : چرا برای هفته بعد قرار مذاکره گذاشتید؟
مسئولان محترم مذاکرات: مگر نگفتید بندهای ۱،۴،۵،۱۰،۱۱ پیش‌شرط ادامه‌ی مذاکرات است و تا عملی نشود، مذاکرات متوقف می‌شود.
این بندها کامل اجرایی و عملی نشده است.  چرا برای هفته‌ی آینده قرار مذاکراتی گذاشتید؟
@withyashar</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/15821" target="_blank">📅 09:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15820">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آخرین آمار رسمی، حاکی از کشته شدن دست‌کم ۲۳۵ نفر در پی دو زمین‌لرزه شدید در این کشور است. وزارت بهداشت ونزوئلا همچنین از زخمی شدن بیش از چهار هزار شهروند این کشور در دو زمین‌لرزه به بزرگای ۷.۲ و ۷.۵ که شامگاه چهارشنبه رخ دادند، خبر داده است.
سازمان زمین‌شناسی آمریکا هشدار داده است که شمار قربانیان به احتمال زیاد به هزاران نفر خواهد رسید و احتمال زیادی وجود دارد که آمار کشته‌ها از ۱۰ هزار نفر فراتر رود.
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/15820" target="_blank">📅 09:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15819">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بیانیهٔ تیم ملی نسبت به احتمال تبلیغات همجنس‌‌بازی در بازی مقابل مصر
فیفا به هر دو تیم شرکت‌کننده اطمینان داده است که هیچ‌گونه مراسم یا فعالیت تبلیغاتی مرتبط با این موضوع در داخل ورزشگاه یا به‌عنوان بخشی از برنامه رسمی مسابقه برگزار نخواهد شد.
موضع ایران این است که هیچ‌گونه مراسم یا فعالیت تبلیغاتی مرتبط با این پروژه نباید در داخل ورزشگاه یا به عنوان بخشی از فضای مسابقه برگزار شود.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/15819" target="_blank">📅 08:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15818">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تحقیقات وال استریت ژورنال نشان می‌دهد: خسارات وارده به پایگاه نیروی دریایی ایالات متحده در بحرین در جریان حملات ایران از اواخر فوریه تا ژوئن بسیار بیشتر از آن چیزی است که گزارش شده است. طبق تحقیقات، ستاد ناوگان پنجم، تأسیسات ارتباطات ماهواره‌ای، انبارها و ساختمان‌های مسکونی آسیب دیده‌اند , که برخی از آنها دیگر قابل استفاده نیستند. تحقیقات هزینه بازسازی را حدود ۴۰۰ میلیون دلار تخمین زده است، اما انتظار می‌رود هزینه کل بسیار بیشتر باشد.
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/15818" target="_blank">📅 08:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15817">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: ما یک بازار جدید داریم که به آن کشور دوست‌داشتنی ایران می‌گویند. جای زیبایی است، آیا کسی دوست دارد به آنجا برود؟ آنها در تامین غذا مشکل دارند و ما قرار است مقداری از پولشان را بگیریم و آن را خرج کنیم و گندم، سویا و ذرت زیادی بخریم و این روند به زودی آغاز خواهد شد. این کار بزرگ خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/15817" target="_blank">📅 07:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15816">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfef2bc8f0.mp4?token=lZAsnBhQj4tFYXIEz5OQhmYjTL8ulEy8nl2sXOefIJ4St9srccJb0gua7nx7XdUGS3f-VPwm78gCayGQWvSuUFNy0RLsWgcke5AbKbNpE8RKi3nsafgQugHQUrdxByH3N4txYlex7BCZGjDbsXJSmoBoTfvSZdf6kdJ82j5XNKKwF1cLCWvAwKrefXHraxTaQHgwbsbt3lxgHeHdrPnCsWJ4sjZguAtVnZxakytVlu2kxFbRwpSRib4AWgT_wgiKSTF50F8lKsoGaYe_5FFfJnQU_Irn0FqpIETrEwZguaNiw11WpPGndUmFSvZicGU6iNekq_Hjo2AEeoeYHBoulg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfef2bc8f0.mp4?token=lZAsnBhQj4tFYXIEz5OQhmYjTL8ulEy8nl2sXOefIJ4St9srccJb0gua7nx7XdUGS3f-VPwm78gCayGQWvSuUFNy0RLsWgcke5AbKbNpE8RKi3nsafgQugHQUrdxByH3N4txYlex7BCZGjDbsXJSmoBoTfvSZdf6kdJ82j5XNKKwF1cLCWvAwKrefXHraxTaQHgwbsbt3lxgHeHdrPnCsWJ4sjZguAtVnZxakytVlu2kxFbRwpSRib4AWgT_wgiKSTF50F8lKsoGaYe_5FFfJnQU_Irn0FqpIETrEwZguaNiw11WpPGndUmFSvZicGU6iNekq_Hjo2AEeoeYHBoulg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسی
🧕🏻
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/15816" target="_blank">📅 00:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15815">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شبکه المنار : توپخانه ارتش اسرائیل مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/15815" target="_blank">📅 23:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15814">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جنگنده های اسرائیل بر فراز جنوب لبنان به پرواز درآمدند
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/15814" target="_blank">📅 23:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15813">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پرواز مستقیم تهران-دوبی از ۱۰ تیر ماه برقرار می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/15813" target="_blank">📅 22:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15812">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اسرائیل و لبنان، عقب‌نشینی نیروهای اسرائیلی از جنوب لبنان را تکذیب کردند
یک مقام ارشد ارتش اسرائیل گفت که این کشور از منطقه حائل عقب‌نشینی نخواهد کرد. یک مقام نظامی لبنان نیز گفت که تحولات میدانی روزهای اخیر «خلاف عقب‌نشینی را نشان می‌دهد.»
ارتش اسرائیل هم در بیانیه‌ای اعلام کرد که تغییری در محل استقرار نیروهایش در جنوب لبنان ایجاد نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/15812" target="_blank">📅 22:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15811">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هشدار نهاد مدیریت آبراهه خلیج فارس(PGSA) در‌مورد تبعات
تردد شناورها خارج از مسیر اعلام شده ایران
نهاد مدیریت آبراهه خلیج فارس‏ در پاسخ به استعلام‌های مکرر اعلام میکند:
هرگونه تردد از مسیرهای خارج از چارچوب تعیین‌شده PGSA، مشمول تضمین عبور ایمن نبوده و از پوشش بیمه و مسئولیت‌های مرتبط برخوردار نخواهد بود.
تبعات ناشی از تردد از مسیرهای غیرمجاز، برعهده مالک، بهره‌بردار و فرمانده شناور خواهدبود.
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/15811" target="_blank">📅 22:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15810">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvO8HmlRDONtcYTBkIrrA68K5SOZN1dwxxS64LStxqFE7JP0cPCMbt__Vd2YMKsZGy0_kCt-Q-sm6tVG5iYdvnaMtlSFBs9tUV-TPA7xJAt8hJQbTg83AC9Zg264JRlvwcDbki0yRnmGfmUlqlzdTpCCiAmEJdfylaj0KlV-COJGa6DxBhofxHgn4p8KH_y-8jIsV3pkT4GfHnePa0cEL8MfsoOosnfPfAHTMt3ejKmc5MvpfSGF4KDSIWzx0TloF6_4mO8dxydSgNE8bUNPfsOUCNyxJ2Cccmu5y12rlg1pQaaEK7P-gaiNxuqTSOPq5mBWVr_mZsJxE14feltB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتشسوزی منطقه ویژه بوشهر الان
دوران جنگ دوبار زده بودن اینجارو
@withyashar
🚨</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15810" target="_blank">📅 22:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15809">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ورود نیروهای اسرائیل به خاک سوریه
یک گشتی نظامی ارتش اسرائیل با عبور از خط مرزی، به حومه غربی شهرک «الرفید» در ریف جنوبی قنیطره حمله کردند.
نیروهای اسرائیل در جریان این حمله، تعدادی را بازداشت و آن‌ها را مورد بازجویی قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/15809" target="_blank">📅 21:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15808">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نهاد دریایی بریتانیا :  خدمه یک کشتی از اصابت آن به وسیله یک پرتابه ناشناس در جنوب شرقی عمان خبر دادند @withyashar
🚨</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/15808" target="_blank">📅 21:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15807">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نهاد دریایی بریتانیا :  خدمه یک کشتی از اصابت آن به وسیله یک پرتابه ناشناس در جنوب شرقی عمان خبر دادند @withyashar
🚨</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/15807" target="_blank">📅 21:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15806">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزیر انرژی آمریکا به سی‌ان‌ان:
لغو تحریم‌ها بر نفت ایران، امکان فروش آن در بازارهای دیگر و دریافت وجه آن به دلار را فراهم می‌کند.
دارایی‌های ایران که مسدود شده بودند آزاد خواهد شد و تحت نظارت شدید در مورد نحوه هزینه‌کرد قرار خواهند گرفت
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/15806" target="_blank">📅 21:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">برخی از منابع محلی در لبنان و سوریه، گزارشاتی از تجمع نیروهای جولانی در مرز جنوب لبنان را داده اند
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/15805" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15804">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">moamelegari-trump(@withyashar).pdf</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/withyashar/15804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کتابی از دونالد ترامپ یکی از بحث برانگیز ترین شخصیت های سیاسی جهان.
رئیس جمهور آمریکا دونالد جی ترامپ ، جهان بینی حرفه ای و شخصی خود را در این کتاب جذاب و خواندنی بیان می کند، روایتی دست اول از ظهور مهمترین معامله گر آمریکا.
دونالد ترامپ : هنر معامله گری
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/15804" target="_blank">📅 20:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15803">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اینم کتاب ترامپ دوباره</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/15803" target="_blank">📅 20:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15802">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گزارش شبکه کان اسرائیل : آمریکایی‌ها در حال ترک فرودگاه بن‌گوریون هستند   ایالات متحده ۲۸ فروند هواپیمای سوخت‌رسان را تخلیه کرده و اسرائیل نیز به‌دلیل نگرانی از اختلال در پروازهای غیرنظامی در طول تابستان، اسرائیل خواستار تخلیه حدود ۲۰ هواپیمای دیگر شده است.…</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/15802" target="_blank">📅 20:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15801">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بالگرد نظامی (بلک هاوک) نیروی هوایی ارتش اسرائیل که حامل «اسحاق هرتزوگ» رئیس جمهور این کشور بود، به دلیل نقص فنی ناشی از برخورد با پرنده در آسمان، مجبور به فرود اضطراری شد.
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/15801" target="_blank">📅 20:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15800">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شکست شاگردان پیاتزا مقابل آمریکا
🏐
جمهوری اسلامی ۰ - ۳
آمریکا
🇮🇷
۲۳|۲۰|۲۹
🇺🇸
۲۵|۲۵|۳۱
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/15800" target="_blank">📅 20:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15799">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یدیعوت آحارانوت:نتانیاهو موفق شد ترامپ را متقاعد کند که اسرائیل را از جنوب لبنان خارج نکند
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/15799" target="_blank">📅 20:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15798">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پایان ست دوم , لیگ ملت های والیبال
آمریکا
2️⃣
- جمهوری اسلامی
0️⃣
🇺🇸
25 | 25
🇮🇷
23 | 20
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/15798" target="_blank">📅 19:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15797">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال 12 ، نتانیاهو :
هنوز ماموریت‌هایی برای انجام دادن وجود دارد، هنوز کارهایی علیه ایران و حماس باید انجام شود. ما تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15797" target="_blank">📅 19:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15796">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نهاد دریایی بریتانیا :
خدمه یک کشتی از اصابت آن به وسیله یک پرتابه ناشناس در جنوب شرقی عمان خبر دادند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/15796" target="_blank">📅 18:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15795">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ارتش اسرائیل: اگر به دلیل عملیات ما در لبنان مورد حمله ایران قرار بگیریم، با تمام قوا به آن حمله خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/15795" target="_blank">📅 18:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15794">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تلگراف: فیفا درخواست جمهوری اسلامی و مصر برای ممنوعیت پرچم‌های رنگین‌کمان در بازی دو تیم را رد کرد
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/15794" target="_blank">📅 18:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15793">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کتلین تایسون، بانکدار و تحلیلگر نظام پولی بین‌الملل بریتانیایی :هیچ بانکی برای ایران، صرفاً به‌خاطر مجوز ۶۰ روزه تجارت نفت، حساب دلاری باز نخواهد کرد. تسویه‌حساب محموله‌های نفتی همچنان با ارزهای جایگزین انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15793" target="_blank">📅 17:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15792">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جی دی ونس معاون ترامپ: دستاوردهای مذاکرات سوئیس، توافق در اصل برای ایجاد یک کانال ارتباطی نظامی مستقیم بین ایالات متحده و ایران برای کمک به جلوگیری از تشدید آینده بود.
«یکی از چیزهایی که می‌خواستیم به دست آوریم، یک کانال در سمت ایران برای کاهش درگیری بود.»
«آن‌ها گفتند: "باشه، ما کسی از سپاه پاسداران را می‌فرستیم تا در دوحه با کسی از فرماندهی مرکزی (سنتکام) باشد و این همان راهی است که بسیاری از این اختلافات را حل می‌کنیم."»
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15792" target="_blank">📅 17:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15791">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0b1ba54a.mp4?token=BdGmI28ONvsEryYeOoP2rGh2-VMqvLMYqWLf4-vm35kzmDyJ7c9uC19XOJUcF-J80-spwKr7Sp9FFmx81bifa_AJrrU0rSDsztZSyYWiwObCYgeKdXpsS_EZF7Skj20revJfYgmveZPO4-8y3xSsccq7EDZ2kqR4-dPg2tAygyX-fFjNI16kd77S4wGSYlpVnvvxFYy3uaDXa61oTuy0Q771Eky6N0mPD7a8lYsyHXfcgYzOd6frAv2ZXspYS2_PrOJ0WE9qhGZPvroZSngU20LyR62001KX1RlXMh_0-lx2hTq5bUHIa-RD_BwTVNrUS-_jNU_LIAP1ztiEa0_8Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0b1ba54a.mp4?token=BdGmI28ONvsEryYeOoP2rGh2-VMqvLMYqWLf4-vm35kzmDyJ7c9uC19XOJUcF-J80-spwKr7Sp9FFmx81bifa_AJrrU0rSDsztZSyYWiwObCYgeKdXpsS_EZF7Skj20revJfYgmveZPO4-8y3xSsccq7EDZ2kqR4-dPg2tAygyX-fFjNI16kd77S4wGSYlpVnvvxFYy3uaDXa61oTuy0Q771Eky6N0mPD7a8lYsyHXfcgYzOd6frAv2ZXspYS2_PrOJ0WE9qhGZPvroZSngU20LyR62001KX1RlXMh_0-lx2hTq5bUHIa-RD_BwTVNrUS-_jNU_LIAP1ztiEa0_8Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۶ VHF نیروی دریایی سپاه:«عبور و مرور در تنگه هرمز فقط با اجازه نیروی دریایی سپاه و در مسیرهای تعیین شده امکان‌پذیر است.
اگر هر کشتی‌ای بدون اجازه ما، با سیستم شناسایی خودکار خاموش یا خارج از مسیر تعیین شده اقدام به عبور کند، مسئولیت هرگونه عواقبی بر عهده آن کشتی خواهد بود.»
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/15791" target="_blank">📅 16:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15790">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قالیباف: آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما صرف خرید محصولات کشاورزی آن‌ها خواهد شد. جالب است؛ تنها محصولی که ما در حال برداشت آن هستیم، همان چیزی است که شما کاشته‌اید: دهه‌ها بی‌اعتمادی. این محصول، ارگانیک، فراوان و بومی است. اما ظاهراً آمریکا تنها سویاهای تراریخته، وعده‌های شکسته شده و یاوه‌گویی صادر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/15790" target="_blank">📅 15:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15789">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e51659f85.mp4?token=wCRLqQRlxo1D7OXelC3-vfaLlyY9KUffRbcEWmoLRu0iZd25xEOTWDoeGlaH2V4Z59q7Yat0k1M8aTp_tKpACkuDU-mDhgYUgqjksgXBlDv0r7E-m9mHChROdz-YMBM3elcGb4rrvJYvgHaxA8NaV-fGo8lLiFhL_ukY9t6_avEC8zqUSjt6Q5yMT0aw4dwX8mdBFBXmOFZU6DBDstP1JbKEbXZJ66iM7qG0DyLigbtLmNBzRhfUT6Q7ByCh275b5Bj8iuIoBaJ7yAAxHukE-Xtls0JHAGkuKNCCriPwdb07EJiTnNSmopvNVjqmc_i1bnqxYKjXPCMmMGWiI0GuDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e51659f85.mp4?token=wCRLqQRlxo1D7OXelC3-vfaLlyY9KUffRbcEWmoLRu0iZd25xEOTWDoeGlaH2V4Z59q7Yat0k1M8aTp_tKpACkuDU-mDhgYUgqjksgXBlDv0r7E-m9mHChROdz-YMBM3elcGb4rrvJYvgHaxA8NaV-fGo8lLiFhL_ukY9t6_avEC8zqUSjt6Q5yMT0aw4dwX8mdBFBXmOFZU6DBDstP1JbKEbXZJ66iM7qG0DyLigbtLmNBzRhfUT6Q7ByCh275b5Bj8iuIoBaJ7yAAxHukE-Xtls0JHAGkuKNCCriPwdb07EJiTnNSmopvNVjqmc_i1bnqxYKjXPCMmMGWiI0GuDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی: هنوز مطمئن نیستم همه‌چیز تموم شده باشه، چون هر چند ساعت یه توییت جدید از ترامپ منتشر می‌شه و با هر توییت، تیتر خبرها عوض میشه؛
واسه همین فعلاً روی هیچ‌کدوم از حرف‌هایی که ترامپ زده حساب باز نمیکنم.
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/15789" target="_blank">📅 15:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15788">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اختلال بانک‌ها بعد از چندین روز همچنان ادامه دارد
رصد گزارش‌های مردمی در شبکه‌های اجتماعی، کانال‌های اطلاع‌رسانی و بازخورد کاربران نشان می‌دهد شبکه بانکی ایران از فاز اختلال شدید عبور کرده و بخش عمده خدمات به وضعیت عملیاتی بازگشته است.
در میان بانک‌های بزرگ، بانک ملی همچنان بیشترین حجم شکایت کاربران را به خود اختصاص داده است.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15788" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15787">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">روبیو: آمریکا خواهان توافق با ایران است، اما توافق به هر قیمتی را نمی‌پذیرد
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/15787" target="_blank">📅 14:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15786">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فرمانده نیروی قدس خطاب به اسرائیل:
اگر امروز با اختیار خود عقب‌نشینی نکنید، فردا با خواری و شکست ناگزیر به فرار خواهید شد
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/15786" target="_blank">📅 14:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15785">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b7288a91.mp4?token=tV5iVMwzF_FZNvv7euxEiLJrF_UlZn82LL7wlo7HcZb3G4rZfQKE2wUznxPF6Ltdf9ZhEVIA8IDLH9SCpYlnEVbgXQ02ltjXiLa9JrtNZAZDc4RVVrVYkaDWGSAOhf97wlQKFN6eKuFI1wrpn-OqQ_kIHduJM9DI8LMr80-GWlfrhgSmkVsTB0mp7cvHZ0h8_IN5muMMoYAc9APwfvFFsnmXLOmxvu4QtvWTAgVD2IMT_BSJVfW7xF2xPknfMlDog-_Z1DLDMJb3gJH9WjIcK54k-xqY3MjgGzp2ow_-DhK84g0_5agOt5iv1l77GOZU3mT9uHyuN_-t_rHACwmelIhp_52e6hXtNW3bjWxHtJxGcO7dvvWKFgqyDGbuK88wGvewKmccnHG7V_GR6iar9dsJalfTkU1rhesRCm_GGj-LiPAQCiUKU_jd7PVHacZFObmXmLw5ivCCBHQ_WUemoBj4W2YGxAbSvKzJTJBEeA_l68DOO3-kti_4C6d-uOexpC-2tTJiHUg06fm_1fr0mRimabsZPuyeesFwrzJW8QCTqZGtNj9p3vloL6mxilIY2VC3izCRwlgdw2yARwWyPyrReggnf4BHotH6XgmfGgnAEpPq9Y-P8yvAlwa42j7yDse-jnjVlJjpzjH-U5qCCQOfgTDYbMba_Wf0jlqDEJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b7288a91.mp4?token=tV5iVMwzF_FZNvv7euxEiLJrF_UlZn82LL7wlo7HcZb3G4rZfQKE2wUznxPF6Ltdf9ZhEVIA8IDLH9SCpYlnEVbgXQ02ltjXiLa9JrtNZAZDc4RVVrVYkaDWGSAOhf97wlQKFN6eKuFI1wrpn-OqQ_kIHduJM9DI8LMr80-GWlfrhgSmkVsTB0mp7cvHZ0h8_IN5muMMoYAc9APwfvFFsnmXLOmxvu4QtvWTAgVD2IMT_BSJVfW7xF2xPknfMlDog-_Z1DLDMJb3gJH9WjIcK54k-xqY3MjgGzp2ow_-DhK84g0_5agOt5iv1l77GOZU3mT9uHyuN_-t_rHACwmelIhp_52e6hXtNW3bjWxHtJxGcO7dvvWKFgqyDGbuK88wGvewKmccnHG7V_GR6iar9dsJalfTkU1rhesRCm_GGj-LiPAQCiUKU_jd7PVHacZFObmXmLw5ivCCBHQ_WUemoBj4W2YGxAbSvKzJTJBEeA_l68DOO3-kti_4C6d-uOexpC-2tTJiHUg06fm_1fr0mRimabsZPuyeesFwrzJW8QCTqZGtNj9p3vloL6mxilIY2VC3izCRwlgdw2yARwWyPyrReggnf4BHotH6XgmfGgnAEpPq9Y-P8yvAlwa42j7yDse-jnjVlJjpzjH-U5qCCQOfgTDYbMba_Wf0jlqDEJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود، من نگذاشتم
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/15785" target="_blank">📅 14:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15784">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اسرائیل هیوم: به ارتش اسرائیل هیچ دستوری مبنی بر عقب‌نشینی داده نشده
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/15784" target="_blank">📅 13:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15783">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مخالفت شدید چین با اقدامات آمریکا علیه کوبا
وزارت خارجه چین بیان کرد: چین همواره با تحریم‌های یکجانبه غیرقانونی که هیچ پایه و اساسی در قوانین بین‌المللی ندارند، مخالفت کرده است.
پکن از واشنگتن می خواهد تا فوراً به تحریم کوبا و هر نوع اجبار یا فشار پایان دهد. ما حمایت بی‌دریغ خود را از کوبا در جستجوی مسیر توسعه سوسیالیستی متناسب با شرایط ملی آن مجدداً تأیید می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/15783" target="_blank">📅 13:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15782">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">moamelegari-trump(@withyashar).pdf</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/15782" target="_blank">📅 13:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15781">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رویترز
:
اسرائیل به نشانه حسن نیت از بخشی از منطقه امنیتی جنوب لبنان عقب‌نشینی کرد
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/15781" target="_blank">📅 13:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15780">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سی‌ان‌ان: متحدان ترامپ در کشورهای حاشیه خلیج فارس بیم دارند که توافق او با ایران سرآغاز تحولی فاجعه‌بار باشد
@withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/15780" target="_blank">📅 12:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15779">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏وو باهیانا، پیشگوی برزیلی مدعی شده است که در جریان دیدار برزیل و اسکاتلند در جام جهانی ۲۰۲۶ که بامداد پنجشنبه در فلوریدا برگزار می‌شود، فضایی‌ها به زمین حمله خواهند کرد. او که بیش از ۲۳ میلیون دنبال‌کننده دارد، حتی ویدیویی تولیدشده با هوش مصنوعی از ربوده…</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/15779" target="_blank">📅 12:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15778">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ: به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، امروز ایران نیروی دریایی، نیروی هوایی، پدافند ، پرتاب موشک، و تولیدی ندارد و رهبری آن نابود شده است. برای اولین بار در ۳۰۰۰ سال، ما بالاخره صلح را در خاورمیانه خواهیم داشت. @withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/15778" target="_blank">📅 12:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15777">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edea42e58c.mp4?token=UdikFf6D15Ga58ul086lrdEsMn2zqMANoqNKUptXKL8WEDoDctpDGIVHDCZmioVAaa54WK1Qko0FvvA0QctyhrSnGL8MdbsLqup2ooCWK91s0NTmy8rUOIAR3kFaO7QKH_YCe5IKPnra7Ylqa5DwsMrS5McB5gNP1mMrTVioUG5_0ecKb62Gyy6wxpo2borYH6gwIPCT-Fc5QNty3ixudS86-fIKp0j4EdEA2Z9e-BTUbtQEwClYXrQBpbGTFWdAKU7rtZj2Ie7fPy49L9fyDM8kqasQYG_Qxo9KUfpgn6zuzuxYMz3znJlZS02glyPQtx8LHPpV8xaNvEe6mk5Frw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edea42e58c.mp4?token=UdikFf6D15Ga58ul086lrdEsMn2zqMANoqNKUptXKL8WEDoDctpDGIVHDCZmioVAaa54WK1Qko0FvvA0QctyhrSnGL8MdbsLqup2ooCWK91s0NTmy8rUOIAR3kFaO7QKH_YCe5IKPnra7Ylqa5DwsMrS5McB5gNP1mMrTVioUG5_0ecKb62Gyy6wxpo2borYH6gwIPCT-Fc5QNty3ixudS86-fIKp0j4EdEA2Z9e-BTUbtQEwClYXrQBpbGTFWdAKU7rtZj2Ie7fPy49L9fyDM8kqasQYG_Qxo9KUfpgn6zuzuxYMz3znJlZS02glyPQtx8LHPpV8xaNvEe6mk5Frw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، امروز ایران نیروی دریایی، نیروی هوایی، پدافند ، پرتاب موشک، و تولیدی ندارد و رهبری آن نابود شده است.
برای اولین بار در ۳۰۰۰ سال، ما بالاخره صلح را در خاورمیانه خواهیم داشت.
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15777" target="_blank">📅 12:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15776">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حمله اسرائیل به جنوب لبنان
@withyashar
🚨</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/15776" target="_blank">📅 12:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15775">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وال استریت ژورنال:
ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/15775" target="_blank">📅 11:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15774">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ایلان ماسک در پی سقوط سهام تسلا و اسپیس ایکس در معاملات روز چهارشنبه که ارزش دارایی او را به ۹۷۰.۲ میلیارد دلار کاهش داد، عنوان «تریلیونر» را از دست داد.
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/15774" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
