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
<img src="https://cdn4.telesco.pe/file/ET7sHVv32Yf5FBZq-xA3GY3EjlOAJ91vNhftD7URCL5IpyhwnVBNZxr3VqVpZrYKnEbZbYq8cERHTKGbZM7zDlc6Vfj7pnq1jpNqJOo5sJ2Hm04n4HFbvw6vPOt-qxV3BVX3SI3FMVBgHhvDU2K5cuswS_1zfRWs-LRpqCFabDsz8n-ex_CHCBtN9EzwJUM06HsJHKNqo6HSQGI4F6B-KPX1QcjNzQ_T4A4L4xTXqjzL58mVTko4OT77mqfqvJ4hC72oXzUZTjhamu0SIaQRK8m7SmWqzB0-bDqpggbzZ9U6xa0PDEq_2deMrVnxrJGt6qkYms_IuBd96CNgIK7-Qg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 04:24:08</div>
<hr>

<div class="tg-post" id="msg-140137">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/knLFBoBJfYdYr72xOq_mQXhTsAN-ZicytYYJCSmJRXvUzYjzQKdNNkDw20FpEPT0Z_08XjeQTnTjhrkCamYEJY7bFNCMP0v0GcLpFFOPNU7H9nxCXhWx8PbR2XANJB4mzmzq0Cb06gsM_jMvtcC18I0_b03qwWUJBlro2AiTLg01u792QAIJGIBDkv4slOid55qG46PgzrEGeRf2M9W7UZmJwUABVVdmI4PkfSUa_oW_HdCyN1wAT7XpLOGBlyLaot1KYNlI0zEpQbpN_-KpIg33PRTxmjwDVubEU7-PYUlsNwawXzsXLG1FAPdqgANJxNSaHRFzr3mA-FSfFEX9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بونوس ویژه اسپورت‌نود
🔵
با هر واریز بین ۵ تا ۱۰۰ میلیون تومان ۱۰٪ بونوس ورزشی تا سقف ۵ میلیون تومان دریافت کنید.
🔗
آزادسازی بونوس خیلی ساده‌ست؛ فقط کافیه یکی از این دو روش رو انجام بدی:
👇
📌
شرط تکی با ضریب حداقل ۱.۹
📌
شرط میکس با ضریب حداقل ۴
🟢
مدت استفاده از بونوس ۲ روز می‌باشد.
🔗
همین حالا واریز کن، بونوس بگیر و شانس بردتو بیشتر کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
مینی‌اپ رسمی اسپورت‌نود:
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 965 · <a href="https://t.me/SorkhTimes/140137" target="_blank">📅 01:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140136">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/140136" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140135">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZW3M64wk_HzYYgc-G-fXphfVm0UYBNm6hLOfZwM-YapPXkbIIaQUWat1OsLdefblLzJxsfywzJWlHHtGb8Uc8yEjhjZ_C3u4_3RTfTgF-bgggqJy2YzYtqa-UB9bMR_IXH6gHw30rJUuPKVDfzCjIOf9EXK7aYo_aPKmCOTkxRXHd0UD3sr0EVrUvW73aGXqwwTZQz2-NaWxBo32XkI6HvZuxL0ZmQCitB6YN5bUSDuVnoEqGZOFzM5ttReHW02k9yfIGY-INMrgQ8HAhO9Ec_huF1DvBJilLcR8MAHPndtrUjrcs7cXouKp2zXJ99fjY1m2fOw2i6c1npmthbPvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/140135" target="_blank">📅 00:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140134">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3657efb8.mp4?token=KDvpEGu_irC13BQhPcjM2VZER3vgEO1357LwjZeICS1CpU9yrp60ikrf7fAmhS2Rc84bjdHBXi88EvDSQP6zvHW8ZJMs23OVLfadtlMMSGdSIadEPa7-18lTo0TMGLjiihkLulP5hxz6esI0CsoTc1n6j1ISoaJu4ydv5W5OZ7fFch8qNmm-a85I1h3G-GXsAQPTBQUaZP_Ttlr3MYgomJkYcATGAxP6ax-u5Gaprt58YaLI4qM-GZ0M5qc63xdEBN1ZOQc3zi8HIFJGeaiEAqBKvWnwXgHuebErli8P-ZR7XshdsLOCkWn2dSAUDf1vzuGHPjsx6Z0-QnK0ATU72g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3657efb8.mp4?token=KDvpEGu_irC13BQhPcjM2VZER3vgEO1357LwjZeICS1CpU9yrp60ikrf7fAmhS2Rc84bjdHBXi88EvDSQP6zvHW8ZJMs23OVLfadtlMMSGdSIadEPa7-18lTo0TMGLjiihkLulP5hxz6esI0CsoTc1n6j1ISoaJu4ydv5W5OZ7fFch8qNmm-a85I1h3G-GXsAQPTBQUaZP_Ttlr3MYgomJkYcATGAxP6ax-u5Gaprt58YaLI4qM-GZ0M5qc63xdEBN1ZOQc3zi8HIFJGeaiEAqBKvWnwXgHuebErli8P-ZR7XshdsLOCkWn2dSAUDf1vzuGHPjsx6Z0-QnK0ATU72g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
پویا پورعلی، پسر خاله حسن یزدانی است
آیا می‌دانستید؟/ ورود همزمانشان به کشتی و راهی که در نهایت جدا شد؛ خانواده یزدانی و پورعلی همه پرسپولیسی، به جز پدر استقلالی پویا!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/140134" target="_blank">📅 23:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140133">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=hkLS3zG5ifZsZz-KwL99TrJOZ46hBUmW3BDAx2gWwfiWHSeY2UwsxOs2Pw1mR4rUoQgBhztlWweZUQDFIsgT_SVsh9qQc9Svb4ALyXINAd6JPzfJ31vec-Z-upTGFrvZTr0TE4DYgtG0ZTb7oeMihFGwVRkWNY4MBnDR3o6A5dixcI5xlG63JHBDuQiUXLY3oJCApIqJv6tkhdT3LUcSINUYZDONZoJzKFzYLiogO64DxvUsD5Qm32DC4_C-ImxYLL4gZ6yOZ3QuOd2FxBnbAmwXVIs9jqJB1iahHVcH0ZvtSf-qhX-6hq2KPOrsLBp1QIVRIk8w1m4ZAIFUj2bouQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=hkLS3zG5ifZsZz-KwL99TrJOZ46hBUmW3BDAx2gWwfiWHSeY2UwsxOs2Pw1mR4rUoQgBhztlWweZUQDFIsgT_SVsh9qQc9Svb4ALyXINAd6JPzfJ31vec-Z-upTGFrvZTr0TE4DYgtG0ZTb7oeMihFGwVRkWNY4MBnDR3o6A5dixcI5xlG63JHBDuQiUXLY3oJCApIqJv6tkhdT3LUcSINUYZDONZoJzKFzYLiogO64DxvUsD5Qm32DC4_C-ImxYLL4gZ6yOZ3QuOd2FxBnbAmwXVIs9jqJB1iahHVcH0ZvtSf-qhX-6hq2KPOrsLBp1QIVRIk8w1m4ZAIFUj2bouQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
افشاگری عادل فردوسی‌پور: درخواست وحشتناک قلعه‌نویی؛ از ماهی ٣ میلیارد رسید به ماهی ۱۵ میلیارد! چیزی به نام قرار سفید امضا وجود ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SorkhTimes/140133" target="_blank">📅 23:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140132">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d778bc850.mp4?token=WYpTgQ6Tik5M_jktKKvb_7-9izZkecFzLD543RQBkpzU1uJ0xZB0dfjP4jWmbreQo8Xi-1-R3Wwebeu-RKS80JMWIs8sbz__Ti2DwKM90QV25EspZtYsLEaqgGd62TIMNSdVLA8pIXjNhJezltVEjEn0F8OmR3ldABf5MI8OGn58ITGcKjGIkXDRfNFHu-UhOm1-ir-SsZsGC-47Wxwh5QcT1hOfK9G-nDxiqKf_bHnOz-GgggqiY6yqVU6KSvlKSMDqoEGLkwgf26kI9PXXeLb4lzxExQvEwORFJQOxoCbKWhXud4qp-sOdAV3JauqDA7nG5h0H7hG28W1ZH0ALgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d778bc850.mp4?token=WYpTgQ6Tik5M_jktKKvb_7-9izZkecFzLD543RQBkpzU1uJ0xZB0dfjP4jWmbreQo8Xi-1-R3Wwebeu-RKS80JMWIs8sbz__Ti2DwKM90QV25EspZtYsLEaqgGd62TIMNSdVLA8pIXjNhJezltVEjEn0F8OmR3ldABf5MI8OGn58ITGcKjGIkXDRfNFHu-UhOm1-ir-SsZsGC-47Wxwh5QcT1hOfK9G-nDxiqKf_bHnOz-GgggqiY6yqVU6KSvlKSMDqoEGLkwgf26kI9PXXeLb4lzxExQvEwORFJQOxoCbKWhXud4qp-sOdAV3JauqDA7nG5h0H7hG28W1ZH0ALgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏅
💛
🎙
واکنش عادل فردوسی‌پور به اسم‌های روی پیراهن بعضی از بازیکنای استقلال در بازی با السد: مگه خونه خاله‌ست که هرکی هر اسمی خواست بزند؟ یکی نوشته گودی، یکی دیگه اسم پسرش رو زده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/140132" target="_blank">📅 23:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140131">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9929527fe.mp4?token=odzEdUqPPv6Lq8IPpj8QgcwDgXM1w-Vz7_Qm5oDJOfO73d9Q2xErnt6UG8uJ0f8aMwNNFzWdjXAmf2DZZgRybES5UF56-dERV_nHkdVHQgpdIgH33v5pmUl_RQLfmLJGic0doXmeslm3b6SRqP2TLBx28GcULg946ROrkhC2RzM9tD9LgmP-q8c03-0OH-7-9uwjv0gN6ZlqI888rqtLesYO2cuoaZUAKIZTWlH51TgfVCg33CCHXSN2YMGh-_l0uu4XWsJnTT3cRXH8oJZAWcxZ5TY078vwK01Ej5mKnfH-vrVJnJu-sF6zTZpwZDXzFuLMFNVBoKZK-oePI1Y8jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9929527fe.mp4?token=odzEdUqPPv6Lq8IPpj8QgcwDgXM1w-Vz7_Qm5oDJOfO73d9Q2xErnt6UG8uJ0f8aMwNNFzWdjXAmf2DZZgRybES5UF56-dERV_nHkdVHQgpdIgH33v5pmUl_RQLfmLJGic0doXmeslm3b6SRqP2TLBx28GcULg946ROrkhC2RzM9tD9LgmP-q8c03-0OH-7-9uwjv0gN6ZlqI888rqtLesYO2cuoaZUAKIZTWlH51TgfVCg33CCHXSN2YMGh-_l0uu4XWsJnTT3cRXH8oJZAWcxZ5TY078vwK01Ej5mKnfH-vrVJnJu-sF6zTZpwZDXzFuLMFNVBoKZK-oePI1Y8jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
محمدمهدی محبی : این همه هوادار داریم ولی چمن نداریم، شما کیفیت بازی اورونوف رو میخواین ببینین باید بازیش جلوی مصر رو نگاه کنین، بنده خدا تو این چمن نمیتونه دریبل کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SorkhTimes/140131" target="_blank">📅 23:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140130">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
پورعلی: الگوم آقا کریمه و هیچکس هیچوقت به سطح آقا کریم نمیرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/140130" target="_blank">📅 23:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140129">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❤️
پورعلی : من به مهرداد میناوند قول دادم یک روزی شماره ۱۱ دایی کمال رو بپوشم و انشالله در آینده می‌پوشم ، می‌خوایم قهرمان بشیم و آخر فصل جام رو به روح آقا مهرداد تقدیم کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SorkhTimes/140129" target="_blank">📅 23:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140128">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3207916b83.mp4?token=iMwrPrVXNo_X4QSLjBEEFKy6CjkpOSwRbDmHVK_H_om8AFx9t2H0IXat8dA-pAFomjX8k5uNW7RlwiW9qqLPKc5WhKeS0nQvvb1jDWB548PLAC4CBC5hw1AlfQqTiM9zl1Ejnp7WXxbZ3LSpzTwwsS1ABSfOSQQuOzVWAID3FLFXtE0lddaiH5KJnAysb-17h6lKbAK7748fu7C_qiwvn1_Uadb-oLTTmPs-sSqt-vYc_zMdmD1dI8EU5kJIGddQwCwW0h4trlH8WSGzkIyJdl6qrKT69C7aOTZFfssn7d1F4kKP5szTrmR2UjPwKMETgo148WrQvYq3-YIUku1I05QC97LDBiakkJoDrGL88lQbJzIwOzqmCgEd8gd0U2gy4jV_MF0rm_aZ4SaQFpTMjkHkjTKg7k-PvEnX6npwuP9tU_BtdLaUisbyAeynU9_ztpAt9owdXMkg81jDE3Azy_IGv9RKSZM-neJLvZzVtuPEuR00Qx3rqIWBk0iIHJL2f4uroMFgmkcN4Xcrb1gF0SY5oxG6jk1hGS57NBigCFooFL4yZ9lU6JprBHCPpBa1aIkoEUIP4AfTMlZJAx6CbH5fX8nDoN9uB_BzyQi-sd34x281FP-c1LoXbvVeLLIC4RrzCd9v5d4qbPNxl2ZB0isEuwfudNbVeP7CWCRgaoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3207916b83.mp4?token=iMwrPrVXNo_X4QSLjBEEFKy6CjkpOSwRbDmHVK_H_om8AFx9t2H0IXat8dA-pAFomjX8k5uNW7RlwiW9qqLPKc5WhKeS0nQvvb1jDWB548PLAC4CBC5hw1AlfQqTiM9zl1Ejnp7WXxbZ3LSpzTwwsS1ABSfOSQQuOzVWAID3FLFXtE0lddaiH5KJnAysb-17h6lKbAK7748fu7C_qiwvn1_Uadb-oLTTmPs-sSqt-vYc_zMdmD1dI8EU5kJIGddQwCwW0h4trlH8WSGzkIyJdl6qrKT69C7aOTZFfssn7d1F4kKP5szTrmR2UjPwKMETgo148WrQvYq3-YIUku1I05QC97LDBiakkJoDrGL88lQbJzIwOzqmCgEd8gd0U2gy4jV_MF0rm_aZ4SaQFpTMjkHkjTKg7k-PvEnX6npwuP9tU_BtdLaUisbyAeynU9_ztpAt9owdXMkg81jDE3Azy_IGv9RKSZM-neJLvZzVtuPEuR00Qx3rqIWBk0iIHJL2f4uroMFgmkcN4Xcrb1gF0SY5oxG6jk1hGS57NBigCFooFL4yZ9lU6JprBHCPpBa1aIkoEUIP4AfTMlZJAx6CbH5fX8nDoN9uB_BzyQi-sd34x281FP-c1LoXbvVeLLIC4RrzCd9v5d4qbPNxl2ZB0isEuwfudNbVeP7CWCRgaoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
محمدمهدی محبی: خوشحالم که در پرسپولیسم، همه خانواده‌ام هم قرمزند!/ سیر فوتبالی محمدمهدی محبی، که پای او را به تیم نونهالان استقلال هم باز کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/140128" target="_blank">📅 23:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140127">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📹
همه‌چیز از مصدومیت زارع، زیر دوش و در حضور پویا پورعلی شروع شد...
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/140127" target="_blank">📅 23:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140126">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
پورعلی:
✔️
حاج مهدی یروز سجاد(پسر تارتار) رو اورد و یجوری باهاش رفتار می‌کرد که انگار نه انگار که پسرشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/140126" target="_blank">📅 23:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140125">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
پورعلی:
🔻
من نزدیک ۳ بار میخواستم بیام پرسپولیس یبار نیم فصل ملوان که بودم و بار دوم که از تراکتور میخواستم برم گل‌گهر قراردادم رو بسته بودم با پرسپولیس و فشار هواداری نذاشت که بیام.
✔️
من و حاج مهدی رابطه خیلی نزدیکی باهم داریم و رابطه پدر پسری داریم…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/140125" target="_blank">📅 23:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140124">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/140124" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140123">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViJzlW09kaBiKMp4ByvNgbJmADwV5x6KvPfK69EVzqMYbB8Zv3kt6xYtGBIh6S9GWgeEW_CUvHP5recDLfz3SrM46dS4JUoXzHP5fKeSu0JnQWJZ4WV_ZF6e9ZYQAudyV6BoNzEJ6XwPubsu451xXeU3i65LwS-r_i6LEqCVW0opNFajYUxqVccHhJVu_bwbv-LjYDsLuW3pdOLAe_P1EQzq-BsmRZZd9KGnTrzSQxSsX2DECZD6GcKJD-l_gnb5I0ZcwBnrgJSJIvyZXWyTfE0_MSPI28FRXeKRxnwGom8QPWBohMurblxbOy6hmCSsd4ceo-43v7-7lLtu9Z8TTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جادوگر استقلال عالی مینوازد
😂
✔️
اسماعیل بن ناصر هافبک فعلی الغرافه (که سابقه عضویت در آرسنال و میلان داره) مقابل الهلال اخراج شد و بازی با کیسه رو از دست داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/140123" target="_blank">📅 22:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140122">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/140122" target="_blank">📅 22:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140121">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1HBaAYqG8jbU2YCs32osoFPFeJqu_C3UzBZ4SmQqGpxMV4BIJrMc2t3uOu5OOY_dhKSBjmORbBXIqEbK_8Eblh5_LDlfI2SjxvCSlAY71qoLDjVsMmYtrqo7balKW2RmqEJBvgKEaRLxpMhXoiYkpt2GQBjXx0LCzJtFR7GJIKU7yB5tw0yq29yGBDeXcqIqFY3AKWtfb4ubkfxyFx95itxX_CoM7kEtNa3n043TrGHQ1dlygrI_tk7tXVk-1BpPa1CJRR2SyadpLKaRxnKktb5fiQBrIhEtzOPVgGEZQ3ZimoW4jDe_QBJu7vrHYaz_SbDLXF4moHbOcoYvV8Rwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جام اتحادیه؛ لیورپول و تاتنهام، نبردی برای بقا در مسیر جام
🏆
🔥
[
لیورپول
🔴
🆚
⚪️
تاتنهام
]
⚽️
لیورپول و تاتنهام در جام اتحادیه؛ جدالی حذفی که کوچک‌ترین اشتباه می‌تواند سرنوشت بازی را عوض کند. کفه ترازو کمی به سمت لیورپول است، اما تاتنهام می‌تواند با ضدحملات خطرساز شود.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/140121" target="_blank">📅 22:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140120">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnjDA7fJ1dN3PKUQapdf9ArY9PxGAfw9BOly3Oc7LUNACSBl4Ga8Qbt_Yjq40H_6yM-1XHk2AkH-WuwzQFohOmfG3UpuLHYBPDZw8EaysZkbEhkztRNTbFl-joto69XMH-AvpJuVB71Wn9likEhbQ3GO_Il9WSmZAEsX6Ij1PdUpQh0ibezQqPEh99QXlBrhpANHVwcfMeRQO-OkGxnG-5fAqRjcAzbp9wrYAjEv2cT_4EZ1z37AK3UQuFcvwwT2be6JzXAjy_15xErQSJBNOrp6OX_Zv9yriDSr6dCnQBQjyGbJvmdxg5WQKRuu2DtwdOQlLYF-GAjy3WluS1ABTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
🔄
عملکرد یاسین سلمانی در دیدار های تدارکاتی
امسال پرسپولیس: ۸ بازی - ۴ گل - ۵ پاس‌گل :
پ.ن تارتار به شدت راضیه از یاسین
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/140120" target="_blank">📅 21:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140119">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
الجزیره امارات با مالکوم ؛ کولیبالی و تالیسکا و بیست بازیکن خارجی دیگه با گلگهر هیچ گوهی نخوردو مساوی شدن!
❌
پ.ن تیم‌های عربی زاییدن امسال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/140119" target="_blank">📅 21:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140118">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_Ex7F5zY1cvTaq2dTlDg2r-pOdk7BsRcEzPZLcwSZQLvGIojWtj1FhaV2jsBw6rCXtUb79ZlbsTLpWguBnISxSRrbdv4zVwNpIrSFqhMtZjDHQigESH7zBLBudcPkqyq_39WshHqlx8a4yEQmOJpqGMdrGE_ydaRs7mJzXg4ybKqTpP3rKq6qmdfRh9k28E-OJOJ1MtkLS6Llh8keWmA04QTRI5CmcK_kvf-F5UApLIhdO6NdGciGfYyeh2_Uo__I7lTMhrhvPQEhST5EJHhFaM3qRgAPs2WidlxXJRrJgLjmeJ5aE2Aa0jo7eJ-6IufTiGyM5VThal5pviYjIKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/140118" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140117">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6zb44E5KY7CFpFNqO89MCzUVuW_wUDFg2dCtr84CZdhDI0a4IlZWIdxW-mEHTjikPhCGpRJcg3T0VbESiaDO_LgAqhP4nSzB-KUcbM2iAj1hx-yzXsYZ8cFLNtYUIpdBTZ5PLMgwZ2oHcT2ibFNKDK5ljIG0DhY8xLD3UNnrkYK9WPI-44VjZby6VNSRGhsdbMWfxH6xbaxxC4ch199WQZtr2rL7ciqImAet3kL5Xt4u-_L4HtJbxqxs7wckl_9Ylg-DOUm5bb4Zjnvc2IHvQY7Ly3K0F8ZsTqnScR1EpZrKEP-jWK0M3RG__cMJKnvhmi9ScY9fcDX2y28cZ0Pxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
ایران ورزشی: تکلیف دنیل گرا همچنان مشخص نیست و باشگاه هم پاسخ روشنی نمی‌دهد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/140117" target="_blank">📅 21:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140116">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
✅
اخباری زمان خواسته تا بیشتر فکر کنه چون یه پیشنهاد دیگه هم داره و میخواد جایی باشه که بازی کنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140116" target="_blank">📅 20:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140115">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
تیما عربی انگار ریدن اونطرف الاهلی که 2 ساله پشت سر هم داره قهرمان میشه دقیقه 90 تونسته به پاختاکور گل بزنه و 1 بر 1 کنه
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140115" target="_blank">📅 19:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140114">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140114" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140113">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭕️
⭕️
⭕️
باشگاه طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140113" target="_blank">📅 18:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140112">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔻
🔻
🔻
🔻
سویه جدید کرونا، کاتریدا نام دارد!
🔴
مینو محرز، عضو ستاد ملی مبارزه با کرونا، در گفت‌وگو با #جریان:
🔴
کاتریدا، سویه جدید بیماری کرونا است که در اکثر نقاط جهان شیوع پیدا کرده و بیشتر در افراد مسن مشکل‌ساز شده است.
🔴
این بیماری، برخلاف قدرت سرایت بالایی…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140112" target="_blank">📅 18:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140111">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
منهای ورزش
✔️
عکسی از افزایش عجیب و غریب قیمت دارو.
🔄
شما دیگه سرما هم نمیتونید بخورید. چون یه بسته آموکسی سیلین شده ۸۷۶ هزار تومن!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140111" target="_blank">📅 18:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140110">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند در دفترچه خدمتی که پست کرده، بخاطر سرماخوردگی از کمیسیون پزشکی درخواست کرده اعزام او به جای اول، مهر، اول آبان انجام شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140110" target="_blank">📅 18:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140109">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
❌
پرسپولیس پیشنهاد تراکتور برای نیم‌فصل رو رد کرده و اصلاً قصد نداره اورونوف رو به رقیب مستقیمش بده. قرارداد اورونوف آخر فصل تموم میشه و موندن یا رفتنش برای تابستون هنوز مشخص نیست.
✔️
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140109" target="_blank">📅 17:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140108">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
✅
اورونوف نمیخواد جدا بشه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140108" target="_blank">📅 16:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140107">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d87f4723.mp4?token=T_ic9VAlr-PrqlW48cOfnNvScZdnWp_R-XtRD1tQ3rUH3GtzUR6D3GatQ5DzKZgiYKofJiIREmDqdnz6eNRudWZ9qQifSyIZOQdFRkptk7MAh0O5fgGORb11LuX-RPxJ2dnNL9Z8RCdqiZiWjvYOGEBhPGVwERV6wqQzdC0S90UIc3c89RjIm2fxPTEJSuJ9nW0f74tx2_8REH8R12YPlSV9DlMrr2_KFWqp1VezPyTEYf7YzIVwz3vBJkXYeMX74LM62x9jGAMm9S8JnOKi_T-V8g-Kb830OypPol-n_Idr-VEf4DPxJaTm7xzESL3cVA5huWNGCBAUjn-fLwgQrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d87f4723.mp4?token=T_ic9VAlr-PrqlW48cOfnNvScZdnWp_R-XtRD1tQ3rUH3GtzUR6D3GatQ5DzKZgiYKofJiIREmDqdnz6eNRudWZ9qQifSyIZOQdFRkptk7MAh0O5fgGORb11LuX-RPxJ2dnNL9Z8RCdqiZiWjvYOGEBhPGVwERV6wqQzdC0S90UIc3c89RjIm2fxPTEJSuJ9nW0f74tx2_8REH8R12YPlSV9DlMrr2_KFWqp1VezPyTEYf7YzIVwz3vBJkXYeMX74LM62x9jGAMm9S8JnOKi_T-V8g-Kb830OypPol-n_Idr-VEf4DPxJaTm7xzESL3cVA5huWNGCBAUjn-fLwgQrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140107" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140106">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140106" target="_blank">📅 16:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140105">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140105" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140104">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔄
🔄
احد میرزایی، عضو هیات مدیره باشگاه پرسپولیس با جذب محمد قربانی مخالف هست و میگن لازم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140104" target="_blank">📅 16:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140103">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbakwTmJWflqAF9bIj1gzTCRtVkfXrVhDidLG7w8mOPnyZDJdVJv7t8tpY2lGSzvIyuFk86ZG7VGyIZe-Xm-cBL37JFdRZcO79NdDyONkOcCSmB2S446JNh2vzDEPMVvS9ze11gHDaPg3RuBSptCe5mdR6pWyQJsDVTzSbZjhGjzUPvxzZeQZY6gtuYCBZQoP2hel0ct3w6j7SADuzeYBHx53hTBrA6u0KI3Ep2i_JvsAAHMcS8HANWeHnOMhTcYr_K39yNeq7HlMItXFDgIh4ZbWoTg3d2uXBZmW3AWqY4gh_PT5kQFUhu6tyxoTM26Rh1CPeC8dqQV81NEh8osGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
حامد کاویان پور مدیر آکادمی پرسپولیس شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140103" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140102">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
محمد حسین صادقی برای اولین بار در لیست پرسپولیس پرسپولیس قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140102" target="_blank">📅 14:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140101">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند در دفترچه خدمتی که پست کرده، بخاطر سرماخوردگی از کمیسیون پزشکی درخواست کرده اعزام او به جای اول، مهر، اول آبان انجام شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140101" target="_blank">📅 14:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140100">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
عبدی: با ۱۸ بازیکن مقابل امارات قرار می‌گیریم/ بازیکنان استقلال و تراکتور روز بازی می‌رسند
✔️
✔️
زمان حضور رضا غندی پور بازیکن شباب الاهلی امارات؟ ما منتظر تمام نفرات ایست بودیم. مبین دهقان از امارات آمد اما غندی‌پور نیامد و متاسفانه او در تیم باشگاهی‌اش…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140100" target="_blank">📅 13:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140099">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ibu_UMXYKF5ku1xAqIdCKRGEqt9H7aI1_gGQ_VEvP6TKrSKTSNbXRdJ9C1ZdTWWkclrvZJD7AcTq5iJei5fdXJSriYChJBnBKmTTTRrmvkBQqEgDRh5rrAT3ybgtcSf7dglT4vD3jCRdobRbQt0eQXJHNKd6t9eZ8xe8NK3TV9h25cfoDX3UCkxdMGuzSsFLGuX9-6ESwvbPQuCG0MAtSbsR5IFYj4tgqoPscD-m-tpZhORx5OsRYkTpPr84b4sPoLe6DYIRryMHRjgZd1cVin7BznmvidodQyWmEKNfWsKrfeSQym6QnOzQRpSJOF00Cwajb26GnG-BOEY8t9BFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
سپاهان باکیچ را می‌خواهد!
❌
گفته میشه سپاهان به‌دلیل عملکرد نه‌چندان خوب هافبک‌های فعلیش،
دنبال جذب مارکو باکیچ
در نیم‌فصل رفته و محرم نویدکیا هم تأکید زیادی روی جذب هافبک پرسپولیس داشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140099" target="_blank">📅 12:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140098">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚽
امیر عابدینی مدیرعامل اسبق پرسپولیس: مدیران پرسپولیس عملکرد خوبی دارند؛قهرمان جام ملت‌ها نمی‌شویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140098" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140097">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvVZJLBbmvDpnpiKTP_A5nhRrh-mRG1hjeRvagd8WAC9y1icw8v791bqrf_CJNnpz-EDA_uLLAB1QGjxSDYMBJCpJYBVGTZbeo0ou7gV43SjTt2FaZ0zFJ3v-VgS8vQENCg5xm-zfViLQmB2ZCbk3209FDcIBmdxf1r618cpK8ZLGIlE9uUFK0liTOdsg5ubQArNtHjF7nWbL-u6H5MPvbyISVlJ5dWVdsKeCDlMnNT8yw1GDymYpeAV95gn5NDOaXgjtdQ7SbNoMVZNKuxmgfxc30lJ5gRNUVKXIMUBYwFt_WBo7IsGkPtD7vQYGO_O6jD2tLI86uRMLqJ4qBvCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Liverpool -
⚪️
Tottenham
⏰
Tonight 22:30
🏟
Anfield
🟢
لیورپول با وجود احتمال چرخش ترکیب، در آنفیلد از نظر کیفیت و عمق تیم دست بالاتر را دارد؛ مخصوصاً مقابل تاتنهامی که در چهار بازی لیگ هنوز گل نزده است.
اسپرز برای جبران فشار فعلی احتمالاً بازی بازتری ارائه می‌دهد و همین موضوع می‌تواند فضاهای مناسبی برای حملات سریع لیورپول ایجاد کند.
کفه ترازو به سمت لیورپول است؛ برد میزبان محتمل‌تر به نظر می‌رسد، اما چرخش ترکیب می‌تواند بازی را از یک‌طرفه شدن دور کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140097" target="_blank">📅 12:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140096">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140096" target="_blank">📅 11:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140095">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140095" target="_blank">📅 11:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140094">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDKIaavA02NF1X6_ElbRtr3w1utKqfZdecJuKtGDjrcOv3dMrdktGzOlR6N9lreDxOxtyATNjv7wvQQzTVBw8aoN1KPcGmzImMdRpluWH2idGfjkc0rvi2rVhsucptNvpU-5LdTO3L4_ij5C5_hoLOzhzavwsLm3qGo0O5nyVtqPBe8zHWNRuCozj8WU8Rv-RewaURCMjPgTGAwuAXE0CdKJ9mYwF1zJG5XfI8QoyPKwI8ul6MBsWFJDMIiYIiLJBVmPjAqI9futT_CJaAgb9g37JE3JrYmvjcLe_pSLzkJJE5wXP7E_yQwo3mzJy6cXt6eKr96wVj0eg4LO-gLjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرسپولیس؛ عاشق لیگ فشرده
🔺
اسکواد پرمهره پرسپولیس باعث شده برخلاف رقبا، سرخ‌ها از بازی‌های بیشتر استقبال کنن؛ حتی لغو بازی با خیبر هم با اعتراضشون همراه شد.
🔺
پرسپولیس برای برگزاری جام حذفی هم اصرار داره؛ چون با این تیم، شانس گرفتن جام بالاست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140094" target="_blank">📅 11:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140093">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
حسین عبدی: محسن خلیلی همین الان بهم زنگ زد گفت سه تا بازیکن مون برای دربی بهمون قرض بدین منم گفتم با فدراسیون صحبت کن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140093" target="_blank">📅 11:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140092">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم. دنبال رانت و پارتی هم نیستم. وقتی گلر تیم ملی هستم، اونجا هم سرباز کشورم. دنبال فرار از سربازی نیستم. همیشه کنار مردم هستم. الآنم سرباز وطن میشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140092" target="_blank">📅 09:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140091">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcabc1763EtdyE_GDRN2KMO3rP_iQdopBB4Ayl1-GCEM6zZQpdTsZdLVJS5Lmw6TL_PlBmjZrBUP-sp8QnSXe6ch9M7OtLLu5GvblX4mHqz4ptCXar0lvjYBUZMVLuoXsUA_iITdc0AVGrVcD4jQk1RSTPdg7lgriJb9_ABYicCH3ggUpU9_mwmxuOaEIIIs19Wzn-fHoq0PndivjIOK_GheIldi4tXP288rcDOlTl_wmSj9NNXSp31OaedXnHR1vp_uSKBA7hTyDJEYj8z9jh-MMhVtCCD_OojlVE-nJ5uHa2r8q5An1Iw_iRd8Mdil8lo1pJoi1gkNen2eqY3_Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140091" target="_blank">📅 09:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140090">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYYIO4ZaphrsT18_USq-TZDESQdeogRNL7RCWadtgpLgbke8kggvhOIROZRHY5L_EQhSwPZ-r0pcfrc6BsklZ6h8ovAAD0SQUH4_FG1O6P0TDhyHB334RMcpLhm1SnrTcqlNmk-gdA4n6dOpEJyDcGLXQCfdtAHT5rfSV6PWSCY52oeS7bRioYflsODhgmrSXXZ8wPSlDzQbUWX-6Az1Mbyuz-KEAHgG7Ehi5lD5ykLE_SHpoe1WnS_RDZfCo9fEPiN1xBYLdbq7h1NImd5uUAsjAhIgIu-hHwiZk4_bDrYIScVJmXvdHcleVYeR-yCOv3ozcOFoU5Qq6Ymmla70BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فردا شبِ پرهیجان فوتبال؛ بازی‌هایی که روی کاغذ ساده‌ان، اما داخل زمین داستان فرق می‌کنه
🔥
⚡️
⚽️
فردا ترکیبی از بازی‌های کم‌ریسک و چند تقابل جذاب برای دنبال‌کردن دارد؛ الهلال روی کاغذ شانس اول برابر الغرافه است و رئال مادرید هم مقابل الچه دست بالاتر را دارد، اما ارزش اصلی در بازی‌های نزدیک‌تر دیده می‌شود. لیورپول با تاتنهام می‌تواند از نظر ریتم و موقعیت‌سازی دیدنی باشد، در حالی که آرسنال مقابل ایپسویچ و فیورنتینا برابر پیزا با توجه به شرایط بازی، گزینه‌های قابل‌توجهی برای بررسی هستند. در مجموع، شب شلوغی پیش روست؛ جایی که تفاوت بین «انتخاب روی کاغذ» و «انتخاب با تحلیل» می‌تواند تعیین‌کننده باشد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/140090" target="_blank">📅 01:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140089">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
حداقل میذاشتین یه سال از حماسه ۷ تایی شدنتون بگذره بعد کری میخوندین نخبه های لعنتی، هر وقت رسیدین فینال آسیا میتونین کری بخونین هفتایی های جوگیر
✔️
✔️
کیسه‌کشا هفته اول آسیا: بریم واسه ستاره سوم
✔️
✔️
کیسه‌کشا بعد حذف: عشق فقط فوتبال اروپا
😂
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140089" target="_blank">📅 00:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140088">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ9CiGL6eC55NBUGg-mhm4OqJZJgGWF5sAaEatKM0yBfq-tXiAjxjrwl4QOGoSevzbbGDFWxuijCdEZ1sUS9Y_LoNwtv1_OaImSqIgkM2Z0ECk7Dl_wJqE6oAPCsVksxDXXJrRy7Q3rObjkIDBGRUZ02nOuf1lr1p348SsgoGL5l3r3Ym8GfgDQgueEt-CbViyklEVsUkolsqOvOw0J7tJoIKE92Hkjfi2-le4tW3mJiqDYL8LB-dxbkgW0TJ25GwJ_nP_6DAzcrJO4WQluFz-UW0Wb6FU7MOaIR2l5E3QoBUPiIe1Z6FE0bgw9sChg2SK_XHla9xlc6l8wrGNk10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
اگه برد تو بازی اول لیگ نخبگان تضمینی برای موفقیت بود که تیم جواد نکونام در فصل آخرش تو استقلال که بازی اول سه هیچ الغرافه رو برد هم ۳ گانه داخلی میزد هم تو آسیا نتیجه میگرفت ولی خب اون سال اخرش هشتم شدید
🔴
اتفاقا جوگیر شدن شون بعد یه برد تو آسیا میتونه به نفع ما باشه و اون اعتماد به نفس کاذبی که بهشون تزریق میشه کار دستشون میده ، حالا خوبه بازی اول بود و هنوز بازی با تیمای اماراتی مثل الوصل و شباب و بقیه مونده حالا که انقدر خوشحالی میکنید
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/140088" target="_blank">📅 00:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140087">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vmlNtCwj9leCh_4ceHSOBNB_iRfUUOEEiVMDrR5Tcbk6fxWs9NCSRQA-dXei6JLvzOMHk-3yDzEIXJTIBE1TptHYAkwo_P0N7tiUd7Js_HYhFNIok2FOTsjwYUC7-fGVlSKSMtQEyqNYBcpuhLjfX3iXRmnGFPUam0nTfvCe4fkWYrILSTKRCqeLM-uifVo8_eK_Rvo6fE-M9xwfTK30BTurD9FH4SSxo52MT00wsX7IORg1PWM7ExqEvhO2H5VZB_A8pyJtcWBiHNn4siFL_6ub1o6WZwCY5IFx5MpyX12XcpCsRx1ycFvCRYAnyJdlY8RrE1NTLnh6yQfHWb-P0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
پرسپولیس با اختلاف بهترین تیم ایران در آسیا طی ۲۰ سال اخیر
❌
علاوه بر دو فینال آسیا و سه نیمه نهایی از نظر مجموع امتیاز هم عملکرد بهتری از بقیه تیم های ایرانی داشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140087" target="_blank">📅 00:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140086">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
یا رب روا مدار که گدا معتبر شود ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140086" target="_blank">📅 00:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140085">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHBCKbegVwUd9HikyOGs3poGEojyr0lZcLhRovqV7gpuywaM26D3R_dlNBE2xlsaqGDD0Reffm2pXBVLyfpg37q8SsE-mFpadzBefY_a00Tm3S8-CjDiuYGvrTZrGSRxRCkPH07DANR5lskJH_8F_FPREApaJd_rDMEb7prA3rc9gwaCzwLqPeZz0zf0bMmDB5OFz90rX0mm6_5U3Q6OVG2qPXRHcg4D6MS35bvGVDM_0HWDPNHwxe0n7WDTcMTn2AT8MHgKF9g6CbAFLnmxhOfV0wbaofqMKSpZV14UOt8-qbG1ffD_AqjXnC5tjsiA5Yw1n8_d9nYQPn88OURK9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
یا رب روا مدار که گدا معتبر شود ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140085" target="_blank">📅 00:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140084">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140084" target="_blank">📅 00:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140083">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
السد هم از آسانی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/140083" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140082">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
السد چه قدر شخمی بود که ی گل هم نزد و سه تا گل هم خوردن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140082" target="_blank">📅 23:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140081">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140081" target="_blank">📅 23:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140080">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
السد چه قدر شخمی بود که ی گل هم نزد و سه تا گل هم خوردن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140080" target="_blank">📅 23:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140079">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
باور کنید پیکان هم این تیم السد و میبرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140079" target="_blank">📅 23:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140078">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140078" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140077">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140077" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140076">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b77b4fb53.mp4?token=ufCh6kO1zqnUBuO5wMeiwllJlIp553uYZlpzLkbATE_XLGgZBalQ1MmB0GbyfsRZJoVC1ZMuJxeaOdDAPFlEgxjNcyhMcQZsEXhSAhu_z8nwE1z2I0jK1fpVLjskNgqEEmF0JFbgctajStLWqnhOUZN-9pd629W4Our5uA6gkmLVgQJoWQr3Z8qMsPtRyJC1Ji6U7AGeKuz-CFYq6dQ8VP6MNpfrOeUNC1Vk8ZgxMDN7sM3itLMjaLd-6E8rzGn-rh-kxNbwMLfnxEEwGR978jFqGSoebbbmkmTeF_NhufCEP1aqdjeyw43V7cSia0mBb0jMoPvvKj4PizmDL8Y6O5FKfqAygeqq7HlbgggetgMNL_da-9t4ZIqzbeegjWNDE27FD37SGEPFz2x7EPo2ohj5Sb0cBA6TKCgXNXfzPhB68U7hkgLxjCwW_Vj6WaUGqNM5IvdrVoOJAebrYa8MB8QuiYurM7fOzSXaKmivXjFSN-_iFK22oHB7yyamuaFUAxDLquJMb3QwkLvj0L1lK3BRnMDO0tisv6LXexM_nv2uL2UWkdEDVlnHz_zENGFw7qo6JosH_x_6eVR_OG0z_ahCfqA7KffWPseWJ32RDbJfm7xTPY_Ad1QOKTMQ26aBx7N7lM0-hDA6VXgJVnUQeZK4jBoSqVRDWwa85rzo_Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b77b4fb53.mp4?token=ufCh6kO1zqnUBuO5wMeiwllJlIp553uYZlpzLkbATE_XLGgZBalQ1MmB0GbyfsRZJoVC1ZMuJxeaOdDAPFlEgxjNcyhMcQZsEXhSAhu_z8nwE1z2I0jK1fpVLjskNgqEEmF0JFbgctajStLWqnhOUZN-9pd629W4Our5uA6gkmLVgQJoWQr3Z8qMsPtRyJC1Ji6U7AGeKuz-CFYq6dQ8VP6MNpfrOeUNC1Vk8ZgxMDN7sM3itLMjaLd-6E8rzGn-rh-kxNbwMLfnxEEwGR978jFqGSoebbbmkmTeF_NhufCEP1aqdjeyw43V7cSia0mBb0jMoPvvKj4PizmDL8Y6O5FKfqAygeqq7HlbgggetgMNL_da-9t4ZIqzbeegjWNDE27FD37SGEPFz2x7EPo2ohj5Sb0cBA6TKCgXNXfzPhB68U7hkgLxjCwW_Vj6WaUGqNM5IvdrVoOJAebrYa8MB8QuiYurM7fOzSXaKmivXjFSN-_iFK22oHB7yyamuaFUAxDLquJMb3QwkLvj0L1lK3BRnMDO0tisv6LXexM_nv2uL2UWkdEDVlnHz_zENGFw7qo6JosH_x_6eVR_OG0z_ahCfqA7KffWPseWJ32RDbJfm7xTPY_Ad1QOKTMQ26aBx7N7lM0-hDA6VXgJVnUQeZK4jBoSqVRDWwa85rzo_Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید دستمزد بیشتر بگیرد؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140076" target="_blank">📅 23:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140075">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
دفاع السد اتوبانه واقعا مرخصه .الکی گندش کردن السد و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140075" target="_blank">📅 23:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140074">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140074" target="_blank">📅 23:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140073">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⬅
➡️
⬅
➡️
پرسپولیس در آستانه خرید امتیاز بعثت کرمانشاه و تشکیل «پرسپولیس ب» در لیگ یک قرار گرفته؛ توافقات دو باشگاه خوب پیش رفته و احتمال نهایی شدن این انتقال در روزهای آینده بالاست.
⬅
⬅
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140073" target="_blank">📅 23:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140072">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
تراکتور که باخت حالا نوبت استقلاله
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140072" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140071">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
حامد کاویانپور به پرسپولیس بازگشت
🔹
حامد کاویانپور، ستاره سابق پرسپولیس، به عنوان مدیر فنی آکادمی و مسئول بخش استعدادیابی در این باشگاه مشغول به فعالیت شد.
🔹
کاویانپور این سالها مدیر تیم های پایه پیکان بوده که از موفق ترین اکادمی های تهران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140071" target="_blank">📅 23:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140068">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
دفاع السد اتوبانه واقعا مرخصه .الکی گندش کردن السد و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140068" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140067">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
ترکیب پرستاره و برگ ریزون السد برای دیدار با استقلال ایران؛ هرچی ستاره داشنه فیکس گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140067" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140066">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJnFVAwfrfu-jKRzXRGl2GJ9Vb8OziDulytX3aAusBs1hdngX6d8S_zRNoJpctgUxeEFhjMkPL223qTfYP2RB2nGb1reO4tjfl54tP3syefYkjYo9uffmE9BXvBMCMnGZOPgnkjAJbe2znuS8F7Yy1HHgFEgVh7g74RzVMArn_5Z_mec1VLnxd6KUGBbSmPULzZ3NRY-Cvpt4S04fL9fcvghpigK7AR52hlLzaHNrg0G2eKHpcltETtmmwuAxhns3qzgRboJO00KU3G-DVqZXMluxoOX38Hsjy-uEyHPAOqNPE9DIgNhuaV7PDby-e2x0zi7FCkB34YH5caHGqELxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟧
🟧
کیسه گل اول و زد به السد
🔴
گزارشگر میگه غول آسیا گل زد
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140066" target="_blank">📅 22:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140065">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
امشب ی عروس دیگه و ی آبروریزی قطعا داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140065" target="_blank">📅 21:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140064">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
تراکتور که باخت حالا نوبت استقلاله
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140064" target="_blank">📅 21:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140063">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
امشب ی عروس دیگه و ی آبروریزی قطعا داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140063" target="_blank">📅 21:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140062">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
ترکیب پرستاره و برگ ریزون السد برای دیدار با استقلال ایران؛ هرچی ستاره داشنه فیکس گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140062" target="_blank">📅 21:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140061">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
ترکیب السد برابر استقلال.
✔️
سعد الشیب، الساندرو رومانیولی، یوسف الحناچ، محمد الوعد، پدرو میگل، محمد منایی، روبرتو فیرمینو، کلودینیهو، آگوستین سوریا، اکرم عفیف، حسن الهیدوس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140061" target="_blank">📅 21:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140060">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
✔️
عملکرد مثلث هجومی السد در ۴ هفته اخیر
✔️
اکرم عفیف: ۵ گل، ۴ پاس گل
✔️
روبرتو فیرمینو: ۴ گل، ۲ پاس گل
✔️
کلودینیهو: ۳ گل، ۱ پاس گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140060" target="_blank">📅 21:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140059">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPctTsqqXOmD7QqaT217SgTFRnO-lctzvNN8GjkvR2uPsbUIWSQVZdY6fcjjlFA0ZfOk7IZd8iY54TIAx_dlfQfG3MbyjuaB3RgKNK8xGX20Fy52Q9uUQpTxpphAclKsxE0ikt6V_z-YRJUhL0gifdeN05yts0jbRF-bkxvDWhEc1mEMt1zcAxQmGPbbarRSTCr-hSXBj4-cut0dIfrfPkUmfTEY4Eg0XyT326LzC2oQ00xA-Xf7s5LHekr1qoRNmMpOeBJhqSM9bW0t4j8VI6oSisKaCcFM502q_RZENdlOvUCXxwx_gLZidShSZwrIhBKKsXH_CkeTr1lYa59yDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
آزادی 10 زندانی توسط مهاجم استقلال
❌
باشگاه استقلال اعلام کرد سعید سحرخیزان،  10 زندانی جرایم نقدی غیرعمدی را آزاد کرد و آنها را به آغوش خانواده‌های خود بازگرداند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140059" target="_blank">📅 21:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140058">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔵
اعلام برنامه مسابقات هفته‌های هشتم تا دوازدهم و دیدارهای معوقه لیگ برتر
✔️
هفته‌هشتم جمعه ۱۷ مهر
🔴
پرسپولیس - صنعت نفت آبادان ساعت ۱۷
✔️
معوقه هفته هفتم لیگ‌برتر چهارشنبه ۲۲ مهر
🔴
پرسپولیس - خیبر خرم‌آباد ساعت ۱۷
✔️
هفته نهم لیگ‌برتر دوشنبه ۲۷ مهر
🔴
پرسپولیس…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140058" target="_blank">📅 21:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140057">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
✅
تصمیم تارتار درباره تمرینات پرسپولیس
⏺
با وجود لغو مسابقه پرسپولیس و خیبر، تمرینات پرسپولیس طبق برنامه امروز برگزار خواهد شد و سرخپوشان پایتخت یک جلسه تمرینی دیگر را پشت سر می‌گذارند.
⏺
مهدی تارتار، سرمربی پرسپولیس، قصد دارد از فرصت به‌وجود آمده برای…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140057" target="_blank">📅 21:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140056">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
سایه‌‌زنی شجاع‌خلیل‌زاده اسکل مدافعِ پیرسگ تیم قلعه‌نوعی‌ روی گل الشباب
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140056" target="_blank">📅 21:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140055">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEE8NwUYfP5U5E0AXTAHaSWSe35gu0Wdd_wBs-a4GgEPJ0IKEICB3UalXAST-HGp0rzux5249YB3FOsdvL3YafjDUXJpo4Q66JJ-GEdnvtlNsWQLPN9d3fr29LgODKnmNN4E0rpgqM3naJglS7_2zRAj6My_Lb4JWWYXUpN7METRtmXiX0UDzj0URrKYV9ifS5kxp8ssb0f3-9uvG74p72fNh6cEwh1EXXJ6ubjkBl3NKJUdvgd5lL3eZCIsjHrrENqlSyXRQqQZOvmJK6KGHWd253Wj7aKQfOr8JyOyiNeEHEpkLBlCkvq7CeHaPwBUM0kDBoNagaBbAHi4Yco3cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
اطلاعیه رسمی قرارگاه جانفدای کشور:
✔️
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
✔️
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140055" target="_blank">📅 21:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140054">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511d4f624c.mp4?token=XULc7ns-ETIPEpBjtuihUKSMHpq1uUNrJYoR3LGLPCmx1qZ5Qk5HrP4kVvD0E-PEQs7CgKusI1TNVCsQT0GIj5Jm4sDGL254bJfHI7BrLHG03A66js_rvlIaWCEid_aCnqFHpG4X-TS7Ki_dqTg2OuiRj8UevtE52qmOq5sEuCRzRCMy2kzFJqkOoE2qGwj6Jb3QIjAINAL5KDg3dzw-sMKlcrbbi5Uut_wMh1SncxvdQQwTbOSkDK0HDVrFL_Cdlzm6IL_GA6mkxaQkCq-Zjxs3uZpZDb4kHrtYHEKB1D7F7a8UcEaudIhSw8z0oG1L0qP4R_79m3fwshyjXA4F5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511d4f624c.mp4?token=XULc7ns-ETIPEpBjtuihUKSMHpq1uUNrJYoR3LGLPCmx1qZ5Qk5HrP4kVvD0E-PEQs7CgKusI1TNVCsQT0GIj5Jm4sDGL254bJfHI7BrLHG03A66js_rvlIaWCEid_aCnqFHpG4X-TS7Ki_dqTg2OuiRj8UevtE52qmOq5sEuCRzRCMy2kzFJqkOoE2qGwj6Jb3QIjAINAL5KDg3dzw-sMKlcrbbi5Uut_wMh1SncxvdQQwTbOSkDK0HDVrFL_Cdlzm6IL_GA6mkxaQkCq-Zjxs3uZpZDb4kHrtYHEKB1D7F7a8UcEaudIhSw8z0oG1L0qP4R_79m3fwshyjXA4F5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
دانیال اسماعیلی فر از تعویض ناراحت شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/140054" target="_blank">📅 21:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140053">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
❌
رسمی؛ ممبینی که صبح از سمت دبیرکلی برکنار شده بود، مشاور مهدی تاج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140053" target="_blank">📅 20:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140052">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238a9ee677.mp4?token=ZCGhpGYTC1vcfY_hmhDSZJ-5MxBS6-oAEDwQpyiw6dG3I97f1Rq0KGnxcL51ggwBLpYpdBaSQoE2cC-_bTUb6TmW3S8f9ue2cZp7n-6KHmGOrmEW1OqJ5CGLUwH_SbPJDtQbrMPMOxhI0RoiK6ArmDt34BFwFI2sbSlY_70Y73BNtRHWS0OF1zMyBRyOsJ8RrsPWa8piZ1XHZ221H2Cu7R0wqVyz2hoiXtjQJidr4WgcwspMiLk5mNRJmvOY-wtOReiDzHc3DxR8qqScAU9Z1nqEO_aIkHT6DSsWI5TVDMnnmpIfbVYm8jT6VlBadzyQmhrn79qGfIcMkwIchq8g9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238a9ee677.mp4?token=ZCGhpGYTC1vcfY_hmhDSZJ-5MxBS6-oAEDwQpyiw6dG3I97f1Rq0KGnxcL51ggwBLpYpdBaSQoE2cC-_bTUb6TmW3S8f9ue2cZp7n-6KHmGOrmEW1OqJ5CGLUwH_SbPJDtQbrMPMOxhI0RoiK6ArmDt34BFwFI2sbSlY_70Y73BNtRHWS0OF1zMyBRyOsJ8RrsPWa8piZ1XHZ221H2Cu7R0wqVyz2hoiXtjQJidr4WgcwspMiLk5mNRJmvOY-wtOReiDzHc3DxR8qqScAU9Z1nqEO_aIkHT6DSsWI5TVDMnnmpIfbVYm8jT6VlBadzyQmhrn79qGfIcMkwIchq8g9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
سایه‌‌زنی شجاع‌خلیل‌زاده اسکل مدافعِ پیرسگ تیم قلعه‌نوعی‌ روی گل الشباب
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140052" target="_blank">📅 20:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140051">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5804386d73.mp4?token=ZTW8d_kjl8ofwaPstw0eI2bF1ros1dBAEHr72eZpyAnWOBZqiEzmw648egW1qmPpeNR5DfcdXQvWt1jA06RZ7aP5vny5oNDoowSy4lMcmsIX5ihcGuV75IkB-5UWE7Xc6zqep3JKR2bT8fYlYwKYbggJO1Wan7G3TJktMX2DlQnoAufh7TljWQisx6Dz2jD-_L5aI4XiPwA8MXc9OihaKhc646of0I930SH8b1_sHAsSnaV8o0WpHLjylcfump8LXkLUIqNl5JgV-b4EZnm7pBKtCWiqx7OlrgY_qyk98htYyC9jLsL2wJhk35KZwCmURiebOzVnqOYCQAd_MyM5yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5804386d73.mp4?token=ZTW8d_kjl8ofwaPstw0eI2bF1ros1dBAEHr72eZpyAnWOBZqiEzmw648egW1qmPpeNR5DfcdXQvWt1jA06RZ7aP5vny5oNDoowSy4lMcmsIX5ihcGuV75IkB-5UWE7Xc6zqep3JKR2bT8fYlYwKYbggJO1Wan7G3TJktMX2DlQnoAufh7TljWQisx6Dz2jD-_L5aI4XiPwA8MXc9OihaKhc646of0I930SH8b1_sHAsSnaV8o0WpHLjylcfump8LXkLUIqNl5JgV-b4EZnm7pBKtCWiqx7OlrgY_qyk98htYyC9jLsL2wJhk35KZwCmURiebOzVnqOYCQAd_MyM5yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل اول شباب الاهلی به ترتر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140051" target="_blank">📅 20:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140050">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdoaFa1fS_yXXkVZS5AQniDYashFh51BGNO0XdioKeO-KOp5-BO0AsmctEUE1LrsTfhuXPifKr9xz8q2h_aaUaYgYLg0vX35lp4wAIKPcHuB7A6jQJn6uow2KoR8qoqTZ8IB2zFq_WbEFBgc9Qlkzr3rYaaQtJ6mESLnFXtQFo50mz8G7TkHtd8JvW6jdmnlXhqlUfV90fBcuR02WvYjZtnRODzGItZpOVLDwIAXlm7tEOPkrrOlFm2tc-yFukspxEjHM08L2kwLNH9SBDa1UJy73zrZS-FkdfBYlNrxPxVvCW2Lj5To6Oz3qi6O_g8xuO05IMXQvBWmpIcUsJdL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
Esteghlal -
⚪️
AL Sadd
⏰
Tonight 21:45
🏟
Basra International Stadium
🟣
استقلال با تکیه بر ساختار دفاعی منسجم و روند بدون شکست اخیر، احتمالاً بازی را محتاطانه و کنترل‌شده آغاز می‌کند.
السد در نقطه مقابل با ۴ برد متوالی و خط حمله‌ای بسیار آماده وارد میدان شده و روی انتقال سریع می‌تواند استقلال را تحت فشار بگذارد.
با توجه به کیفیت هجومی السد و رویکرد محافظه‌کارانه استقلال، بازی نزدیک و کم‌ریسکی در نیمه‌اول محتمل است؛ اما نیمه دوم می‌تواند کاملاً متفاوت شود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140050" target="_blank">📅 20:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140049">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ba81229c.mp4?token=dlRFlvq6Qt-u6BMg0eS_biP6dPBz7pLdc0yqwMKyaklpxfW_4kq88Rwf7-gtmv4kEMzRXpCEnAgd3bksnRHFQMvSK-b-NhjVWBA3IbHepV0Rk1WRjHlKFJ7aBuP4Qphy8S1mGO5wJsraeVF95iXbrmwTKuWb5SeYzr9LNWmBuN2_6Vp9BggMexykvL15JbwNpMO8qikfEh8EOZ3vkR8dE6IWYprkeQpuCs6MUsgd-DKflO4SYeGks-aHFivQmF8SLydvOoLskWlh1I4Tc_l8WVjQNihDUuSWIZbgHJXoRvxLgVIx37urJtazi4mqkoqREPCcmW7C_y3o0om9PTvXww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ba81229c.mp4?token=dlRFlvq6Qt-u6BMg0eS_biP6dPBz7pLdc0yqwMKyaklpxfW_4kq88Rwf7-gtmv4kEMzRXpCEnAgd3bksnRHFQMvSK-b-NhjVWBA3IbHepV0Rk1WRjHlKFJ7aBuP4Qphy8S1mGO5wJsraeVF95iXbrmwTKuWb5SeYzr9LNWmBuN2_6Vp9BggMexykvL15JbwNpMO8qikfEh8EOZ3vkR8dE6IWYprkeQpuCs6MUsgd-DKflO4SYeGks-aHFivQmF8SLydvOoLskWlh1I4Tc_l8WVjQNihDUuSWIZbgHJXoRvxLgVIx37urJtazi4mqkoqREPCcmW7C_y3o0om9PTvXww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
گل مردود سردار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140049" target="_blank">📅 19:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140048">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
✔️
ترکیب شباب الاهلی مقابل تراکتور با حضور فیکس سردار آزمون و سعید عزت‌اللهی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140048" target="_blank">📅 19:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140047">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzAhkNFEd-7zxm_FgiBO7diFVqhEUFbu9v6OvnqW3fUDPB32V3jr-ixvkSxzFobrZLDZhiDpn72pnL03jIbVnNn8m0tYh8x6J9rLsYfd7UbXiFwrdGpDR6bG1yvXg95FVDKDropYT0RQWnTsSi4F3LI7R5vGO2w4vHvHZmbYlHvxw5ISu-zJEkX3ue3trAyXxzPsQHLhorNu1lu7-A3ceStzn_5IT9z10opd-ABlPkDvm_h0FGo_EBYjHU0J0YYoWnVoHCmcBbQ2uKPQpcOD973aMbaVMo-ocfqQKv6ykExNV4wKC8q2E8_aU4xr9420AnIg0P4H5J8QRM9btmWOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
علی علیپور با وجود اینکه پرسپولیس یک بازی کمتر انجام داده، همچنان صدر جدول موثرترین بازیکنان لیگ رو در اختیار داره.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140047" target="_blank">📅 18:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140046">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
✔️
علیرضا بیرانوند دروازبان تیم تراکتور، دو دیدار آغازین مقابل شباب الاهلی امارات و الغرافه قطر را به دلیل محرومیت غایب خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140046" target="_blank">📅 18:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140045">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
بازگشا سخنگوی پرسپولیس: دنیل گرا در هر تیمی که قبل از آمدن به پرسپولیس بوده است کاپیتان آن تیم بوده و بازیکن بسیار پخته و باشخصیتی است!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140045" target="_blank">📅 17:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140044">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
پایان زودهنگام حضور گل‌محمدی در عراق
❌
ادعای مجری شبکه الرابعه عراق: یک خبر اختصاصی داریم که با توجه به باخت شب گذشته باشگاه دهوک تصمیم به قطع همکاری با یحیی گل‌محمدی گرفته است.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140044" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140042">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔻
🔻
دهوک عراق با هدایت آقا یحیی گل‌محمدی در هفته هفتم لیگ این کشور متحمل شکست شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140042" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140041">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
✔️
✔️
شایعات: حسین کنعانی، حسین ابرقویی، امیرحسین محمودی و ابوالفضل جلالی در دیدار دوستانه امروز پرسپولیس از ناحیه زانو مصدوم شد.
❌
ظاهراً کیفیت بد چمن باعث این مصدومیت‌های عجیب شده است…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140041" target="_blank">📅 15:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140040">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم. دنبال رانت و پارتی هم نیستم. وقتی گلر تیم ملی هستم، اونجا هم سرباز کشورم. دنبال فرار از سربازی نیستم. همیشه کنار مردم هستم. الآنم سرباز وطن میشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140040" target="_blank">📅 15:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140039">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🔴
❤️
ورزش سه: دلیل بانداژ دست امیرحسین محمودی تکل او مقابل ذوب‌آهن است که باعث آسیب جزئی این ستاره‌ی جوان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140039" target="_blank">📅 14:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140038">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mb6AMsWBCTNdhdsKz6_DfbiU7jJ1Xo2Do7DRR3xU3HofZU_uD9TD4aTo9CSYZ9zpWdEuCPTmyrigPxJkPfvScJ3S6KHyRNMjEjOhrNbqg7gxRoEUt_eJo9m001FCxmSky5pdfWlBjBkbVQiWdO9d9R3d6bfo5Wa9NuVyflnX9g7R-OdUvnePXO2zUWfdUZQKPKpQeW4Py9whAil-sfaSWvThzS1P2ClNauapEBcymFUErCex8bGRW99OFZCbXRKPpPVFVcyWuFp5sCr_cTPbI-neSRca9uHdt8scpqrV6HOh_bH4t5BQF0CfwsgGfBEeAfN9kkcwmXmHcT1VYtBS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
استقلال در آزمون بزرگ آسیایی؛ سدِ السد مقابل آبی‌ها!
[
استقلال
🔵
🆚
⚪️
السد
]
⚽️
استقلال برای گرفتن امتیاز مقابل السد باید اول بازی را کنترل کند و در انتقال‌ها کم‌اشتباه باشد. السد با مالکیت و کیفیت فنی بالایش می‌تواند خطرناک باشد، اما استقلال هم در ضدحملات فرصت‌های خوبی خواهد داشت. در مجموع، بازی نزدیک و تاکتیکی به نظر می‌رسد و جزئیات می‌تواند سرنوشت مسابقه را تعیین کند.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140038" target="_blank">📅 14:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140037">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
🔴
مهدی تیکدری (۲۷)، یاسین سلمانی (۵۹ پنالتی)، ابوالفضل زارعی (۷۰) و مجید عیدی (۸۵)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140037" target="_blank">📅 13:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140036">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140036" target="_blank">📅 13:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140035">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
فووووووووووووری از ورزش سه
🎙
🎙
علیرضا بیرانوند از اول آبان به طور قطعی و صد در صدی سرباز محسوب میشه و دیگه نمیتونه برای تراکتورسازی تبریز بازی کنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140035" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
