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
<img src="https://cdn4.telesco.pe/file/h3vM_fUKgUKpaYxbpR4uK3RHcnHD6gfZFd0MdUIGVbVKyiPCU1QOIJlRPfwDa3Cl7pSzNGw7e4-PTuGx6moAxfaKLlhxqipOaMScn6vU6ci-B_ievdr3zyha1HTl3bVWxaEUB7Vi_Nk_2G7z4YtzgvvfDPpuOYAdio9ff4uhIxYUGszKBNcB2nDbOhNzhnzdfZCocpZCenho0Qyo6We8gONAvMo2IXwbRopfcQK7MOr1CCTLD1xAZSKwKK9wLOeo2LevY_38PzUKankYA9mZpkigkaf_MqpWTxfwT46w7HCx32jfqMA8h06ZtwTCe6xal9Qy00a5E_8ypvGCStsQzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 22:38:16</div>
<hr>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=A2aVlhA8ss566fOqZQV6NrVdQZNcxDOsgfN7i00hs9lIZdCGKNc3ZqNbGcxu1UadwDqUioclkfY0FLXYj9G0T3CC_NA1DkAOOULpZ8mxhkP6FmlO1s1bGtc-RUIrtMbqpJGnkR-isFn5v5cr0QmOYuubJ37QLXR4zjVXTnKuUqqbipHJFcKnT67RhrQGcRGYjR0PBRCNCPr3x2_ZaIcErj5aYRPZl-kZlgYo0-Kl8zLIwEM1a1da91aTRq3UM_MwRoV_KbLKrxsuRhdg981Z3T95MYQy-piUwNOmgqz3bk0_Gle6hsddDos62fGAFXqE-hXpCvWoH_viPxwbR3rg8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=A2aVlhA8ss566fOqZQV6NrVdQZNcxDOsgfN7i00hs9lIZdCGKNc3ZqNbGcxu1UadwDqUioclkfY0FLXYj9G0T3CC_NA1DkAOOULpZ8mxhkP6FmlO1s1bGtc-RUIrtMbqpJGnkR-isFn5v5cr0QmOYuubJ37QLXR4zjVXTnKuUqqbipHJFcKnT67RhrQGcRGYjR0PBRCNCPr3x2_ZaIcErj5aYRPZl-kZlgYo0-Kl8zLIwEM1a1da91aTRq3UM_MwRoV_KbLKrxsuRhdg981Z3T95MYQy-piUwNOmgqz3bk0_Gle6hsddDos62fGAFXqE-hXpCvWoH_viPxwbR3rg8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=bxzKzsw6Bj4ewXknONmVFsMLsP8a9jiqai2jB0hQLnz0eLWXBafN7HGbH_eijs-0qAQife1sSGTdAHU1z-a2ERdI7Qnu5SpynfjYZcHFyJliKfJZ_bEypMws-b4QQqD_55aXtylicwmZnHiOIt3X_hvctkX5RR3Yf0xztE-28XgqupHOHnG22cHfwGSLhXA8tXSVTNlYgAkSv1JdOUEfd7ODxJf0Bup_R2CahPw9q7QOlnP3CjkcnxSwyJrbOIk7SV5XZ1_58LtjdTjVgmfY5qO5u9tamK58Hn8pH-wOdZ2dXoTt1jhILPeX2NLauKpMq_eJQODh6ef5BfsyScpqVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=bxzKzsw6Bj4ewXknONmVFsMLsP8a9jiqai2jB0hQLnz0eLWXBafN7HGbH_eijs-0qAQife1sSGTdAHU1z-a2ERdI7Qnu5SpynfjYZcHFyJliKfJZ_bEypMws-b4QQqD_55aXtylicwmZnHiOIt3X_hvctkX5RR3Yf0xztE-28XgqupHOHnG22cHfwGSLhXA8tXSVTNlYgAkSv1JdOUEfd7ODxJf0Bup_R2CahPw9q7QOlnP3CjkcnxSwyJrbOIk7SV5XZ1_58LtjdTjVgmfY5qO5u9tamK58Hn8pH-wOdZ2dXoTt1jhILPeX2NLauKpMq_eJQODh6ef5BfsyScpqVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf83llMcxzFzCG1JUl28AxVsqfDU6LsnH5QzxyykXH6Za9oDc7f35TmVF1dL2VDcmRg7TyTlj2b_VjROmy7_dBTiyPTHoUTUKBq7-Q_TLSDjExVKNX3uPRJfyPKZwzd5A7kud1Lo6Qj8SekGSjyNyskjlBocDL_eVBo7BTXLLAn4FPnpjLDbcgW_r9uc3m5bEUmohilHLBDTD6GgFlr-jT7aQ8xbC43cvg-nPI4Zr7iWDjlBK_DxBuMyJzArzVoQWSr0tsVZS035zYnpMPnTarzApSwunbhysEbKnspwF3ent2jrzcNIaNUAJ-5vIiUpzHpc0PYBZLXFdTFm1FLtNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=FBkY-FUlzD9NLX67NWSd0D75nATbye4fdKMQwMlLFlv2enEqFtZSHNmCYFsY2NFPkKI09pUVon-iMxiQywJ43z1qH89u4DUhJd4BdXdh-X0axU4SyR05bq5Kc3xgJJIHNBayiWwRG7VxNM9sHIoTvoxFEX8dfQ8uTFO-R1O3Ms1FN6y6Dd8y5yDCfjnIVJTQXzCBLgdeGoSMzf3Ru0-iYZDJdS2J2iVRab9nwCA2K34RGPh0bHYjlnQ1KXbCkcyzGLUKcET4avCz4-Lg810zV898-ziFXtHs4L10SoHRHB8KcgGBht9WNZO0fV4g4cASvEr8QamCIvGl0CDL8650wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=FBkY-FUlzD9NLX67NWSd0D75nATbye4fdKMQwMlLFlv2enEqFtZSHNmCYFsY2NFPkKI09pUVon-iMxiQywJ43z1qH89u4DUhJd4BdXdh-X0axU4SyR05bq5Kc3xgJJIHNBayiWwRG7VxNM9sHIoTvoxFEX8dfQ8uTFO-R1O3Ms1FN6y6Dd8y5yDCfjnIVJTQXzCBLgdeGoSMzf3Ru0-iYZDJdS2J2iVRab9nwCA2K34RGPh0bHYjlnQ1KXbCkcyzGLUKcET4avCz4-Lg810zV898-ziFXtHs4L10SoHRHB8KcgGBht9WNZO0fV4g4cASvEr8QamCIvGl0CDL8650wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=XxKrqCvFtvcHdz5NmPtPR8KWYEQMq2jQtEqhQw67M6GsfGrHFsIlAv-9qa59n1uMeBQuw0qYAfUJUQ3JbE-j5oE7mzcI5-Q607X8r-6mx4NAveNeNHEEp8aB65QOdFHM2T3wN6L7vKEHHEavzHBVDeJAkT4ly3lRwUvV6EeYwjnDnOcAXPc1CXs3p83LoQm3AE6x-rgltr2Meoj2ha-RoBBk_UA8cxDoHuNIgBxw3qLTMHEGbYyzN8jOx8Wgs_FupEZLP3eXadH92pfWv2At9cuCpnftYVUEiojyAwq3ywNzBDASP-MNN0Z_53RFQ58A8UDZImQ4cNxc_Qk38slaTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=XxKrqCvFtvcHdz5NmPtPR8KWYEQMq2jQtEqhQw67M6GsfGrHFsIlAv-9qa59n1uMeBQuw0qYAfUJUQ3JbE-j5oE7mzcI5-Q607X8r-6mx4NAveNeNHEEp8aB65QOdFHM2T3wN6L7vKEHHEavzHBVDeJAkT4ly3lRwUvV6EeYwjnDnOcAXPc1CXs3p83LoQm3AE6x-rgltr2Meoj2ha-RoBBk_UA8cxDoHuNIgBxw3qLTMHEGbYyzN8jOx8Wgs_FupEZLP3eXadH92pfWv2At9cuCpnftYVUEiojyAwq3ywNzBDASP-MNN0Z_53RFQ58A8UDZImQ4cNxc_Qk38slaTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=fsnHCGPqu-ufAhM3lAs0fAuRU390l5uGskFeMMxNXI8vuaBv5LNc77bmxIkMUCZA60qSPJpXnNimVGjqzsgEOLYa-8vVOTtlW7MoSS8O8ubWiPwGzP33b8TzYA4MER-fYaEO8pa7X_I8WeFUfT4buANHgQIRJ0pvIk7K8apo16hfeT3edZlZSo3XQ0I49wdrOBLEOiz77VGCVievlfCoPWeDv1L1nQcwFMwLnHroLrRESm3JracDWs7r5N0RL1CTgnKN4cu7E5IAuZfWaP1Z2yAq41XpDwEPYl70Xxc6J83x3GBdUlNl_9cYbLyQZIq_PXG-SyaU3OJ6NL_1wK50TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=fsnHCGPqu-ufAhM3lAs0fAuRU390l5uGskFeMMxNXI8vuaBv5LNc77bmxIkMUCZA60qSPJpXnNimVGjqzsgEOLYa-8vVOTtlW7MoSS8O8ubWiPwGzP33b8TzYA4MER-fYaEO8pa7X_I8WeFUfT4buANHgQIRJ0pvIk7K8apo16hfeT3edZlZSo3XQ0I49wdrOBLEOiz77VGCVievlfCoPWeDv1L1nQcwFMwLnHroLrRESm3JracDWs7r5N0RL1CTgnKN4cu7E5IAuZfWaP1Z2yAq41XpDwEPYl70Xxc6J83x3GBdUlNl_9cYbLyQZIq_PXG-SyaU3OJ6NL_1wK50TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=Wn2vAI8zT-A4J_ecncluU4NSs5gu7FIxXkGaNv3ZXR76uOGtYzGKG5WURI_JPjvBHixl3YhqQ9O79jpt1eoKFodYWj9EAM-vX-Tge0Lg5DCQqbGaKcODic8HtxsGT4RwU_Zn4BAcBG-YpKMzxeVIKCcqOFtnLqBBrRBMYUOROhHyasOyohN6lW1WpmI84XNVZKBAtkrrbwtVgbnRaTcBunvXTRplp2Unbq2-7Vn9LdSRSs6w41DrpfPJ0TC2nxuwL2Gmw-dp1OdAd_iHDEyalZsRWXsYRrZTDDpsR14kTbfU0tdF8XlHtrwcQmQeWv48DLjmbiG_2qU_iEhUpn2hOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=Wn2vAI8zT-A4J_ecncluU4NSs5gu7FIxXkGaNv3ZXR76uOGtYzGKG5WURI_JPjvBHixl3YhqQ9O79jpt1eoKFodYWj9EAM-vX-Tge0Lg5DCQqbGaKcODic8HtxsGT4RwU_Zn4BAcBG-YpKMzxeVIKCcqOFtnLqBBrRBMYUOROhHyasOyohN6lW1WpmI84XNVZKBAtkrrbwtVgbnRaTcBunvXTRplp2Unbq2-7Vn9LdSRSs6w41DrpfPJ0TC2nxuwL2Gmw-dp1OdAd_iHDEyalZsRWXsYRrZTDDpsR14kTbfU0tdF8XlHtrwcQmQeWv48DLjmbiG_2qU_iEhUpn2hOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=LflIxP9SAN2TSeGk7J6vF0l9u_TrOKhEt8RJfIw1CMQOepXEn9Esq9zjBI7yUAgtoHJ7ls9Ne0y70HMsXQZw-on8iWDxLDDsBQpTmnKIkHrNXTlgRCTU9qYnoDb8P4fQLx9ivbDzIGYr9oS_ACXso9aM-FGvx2-rLHOLR1uNEWM2gjwOLPFwQDI6oyMtTfuukZKIgSxQGfEcTLCuspaIj-pTh6G4haRBHLi1aghpPhXCyBL00GMTJPCAK2NT3nBTtEmkPj0MLa3qBFYXEPsb8XpgGAGyB3DOstVlEaoylf2r-EvRGhS6f7W0umt8vfYlFMTy7dxfu9c-lXLefxdC9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=LflIxP9SAN2TSeGk7J6vF0l9u_TrOKhEt8RJfIw1CMQOepXEn9Esq9zjBI7yUAgtoHJ7ls9Ne0y70HMsXQZw-on8iWDxLDDsBQpTmnKIkHrNXTlgRCTU9qYnoDb8P4fQLx9ivbDzIGYr9oS_ACXso9aM-FGvx2-rLHOLR1uNEWM2gjwOLPFwQDI6oyMtTfuukZKIgSxQGfEcTLCuspaIj-pTh6G4haRBHLi1aghpPhXCyBL00GMTJPCAK2NT3nBTtEmkPj0MLa3qBFYXEPsb8XpgGAGyB3DOstVlEaoylf2r-EvRGhS6f7W0umt8vfYlFMTy7dxfu9c-lXLefxdC9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=Vqz7GmxMfop6bm6xnw73n3I_kfbOzAn5xD0f_707IbkwPxMIz9hWWl49MW-vUuW0cRBon3AOJzvBuzBVYnhMkw-icEg6WazeSBxabkoonexAgk1aLAeswh5BE10-0slunEQpfZe3QpafxMG5uMUpT_e5RlQ1r7bz4n2JrmOTpF3kMEVhNWpk1ZY8gvx6dRgXTHlIJ6urll-CQk1jiE-QJhwvGc5egN8VlTKYeASXrI522CJgN2B92GDGERaZbTwh6-3EA22aF0MeqrIuoQJl8sWix8clhnsSdB8kTHmb_ksaw7IHuMQ0eiL-stx9919oy8ZQJHulIoOkgTNLgf0d5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=Vqz7GmxMfop6bm6xnw73n3I_kfbOzAn5xD0f_707IbkwPxMIz9hWWl49MW-vUuW0cRBon3AOJzvBuzBVYnhMkw-icEg6WazeSBxabkoonexAgk1aLAeswh5BE10-0slunEQpfZe3QpafxMG5uMUpT_e5RlQ1r7bz4n2JrmOTpF3kMEVhNWpk1ZY8gvx6dRgXTHlIJ6urll-CQk1jiE-QJhwvGc5egN8VlTKYeASXrI522CJgN2B92GDGERaZbTwh6-3EA22aF0MeqrIuoQJl8sWix8clhnsSdB8kTHmb_ksaw7IHuMQ0eiL-stx9919oy8ZQJHulIoOkgTNLgf0d5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=faMJHgXKGAIzOj1nP3DUmbjvEFKwlkhmF489_4zgeibM0bsx0GNmrQa86UkBGxNr9iQyPc8c4YznEvR0bESs2-SOGms7IWAuQtkhNGXme_BWXz9MwEhoXjIBN3IKAzHZE31WkOwJVukzPruOQwXeBlIKJrIbgfIdQjs3u0e-sdtZxOY7vl_3fnRS_BXcbb1E6hmdUIAHOQgRRz_be6SSK6T8MaAqbZkiXwDo5yXLPEEmtbHV5tVValvOHhyWqwP0FPFHG25TAmKRqvl50_Uap6O0RSiqvD5W41EAeO-id1XS-gkqsxS78PudNMmXttH0ih68LADcZEvSWOdMgv9z0q5Lgxu_M2KQMYYT0IWfABcjgdbS6iEH59hHlWz3DrRknZ07Ly_rRSUegFglCiAyueJ4plHoNBUddy1hj2HQ3MZOeGZlWysI5CjpMXkokkBp-gsJ0lm_fiwJOHVUIgQO99FnApZA6t4ULtZgzVUox9AE1BeWIgfRGbXz-yImqWVY8g93oRFUR_SA3C77m0iDDk_zEsQ_yBIg25V6y3npspGwRNYMukizgdx8gM0VkYUeo34ijLkIM2O3ktjhiWywvem5lpLSdAOeMyVHXE-wA2ttHplxwnEsCESbP1_iyIQ9tmc7PiaYMe_vNQaQkBJkHwze-iuUS5WIW45nsPwuKUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=faMJHgXKGAIzOj1nP3DUmbjvEFKwlkhmF489_4zgeibM0bsx0GNmrQa86UkBGxNr9iQyPc8c4YznEvR0bESs2-SOGms7IWAuQtkhNGXme_BWXz9MwEhoXjIBN3IKAzHZE31WkOwJVukzPruOQwXeBlIKJrIbgfIdQjs3u0e-sdtZxOY7vl_3fnRS_BXcbb1E6hmdUIAHOQgRRz_be6SSK6T8MaAqbZkiXwDo5yXLPEEmtbHV5tVValvOHhyWqwP0FPFHG25TAmKRqvl50_Uap6O0RSiqvD5W41EAeO-id1XS-gkqsxS78PudNMmXttH0ih68LADcZEvSWOdMgv9z0q5Lgxu_M2KQMYYT0IWfABcjgdbS6iEH59hHlWz3DrRknZ07Ly_rRSUegFglCiAyueJ4plHoNBUddy1hj2HQ3MZOeGZlWysI5CjpMXkokkBp-gsJ0lm_fiwJOHVUIgQO99FnApZA6t4ULtZgzVUox9AE1BeWIgfRGbXz-yImqWVY8g93oRFUR_SA3C77m0iDDk_zEsQ_yBIg25V6y3npspGwRNYMukizgdx8gM0VkYUeo34ijLkIM2O3ktjhiWywvem5lpLSdAOeMyVHXE-wA2ttHplxwnEsCESbP1_iyIQ9tmc7PiaYMe_vNQaQkBJkHwze-iuUS5WIW45nsPwuKUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caCvNyyKFqsy76GYzl04zVFmewxcsaej-Bg7Incf45UhzepV-Riz2cAHXpQALWmg7sGeH8DnZbzztcAPlKLWEyB56RDO6uo6OndGVhpHe75kbf0aGiaGd9eLoHhIgjdy3pQZdarP8NUHydkQKqoPR_mEXkGWWG3CqJWaXmSi4Tv6umqsEqZq8JicmxTGTvJhXUAAE-FhRn4tNyE6WxljnVSDSXy0mqMN7mrZqNCqGofxzyUQAsi82iLATCZ0Z8rZfFWDL1HD4kWWQoFaMacymgJeNwiLFYbcMAao6maDcX7e-A9TzUs3701dSpir1g-hcfx74ILCr-_daOb4vc_pTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=utVNQ4sY6eiF4SWrWWcFkjjLsWXhCNtxL-qy5-O9B9V_CEFxf9o16bCo93pvR_Co96qGtLSwWw6HfkGNCVpVNuLq3ZE2N_v7Sjer_6M3imWjtFhM4r2RBYr_eO8FkNXoi2FLfq4sOTWIuhFIbMOnL8iOA5YtySUWupt7q-3zRmasziRnQq4zUDspVHy7keIsXWUh4n8Msx6u6e3sdNh5fGiTl7Yx13NbFF5akawRosds5c-OkrjeQpt2Qb7P2JqIhkgGoL-j45OajYtr6CUP1ylM6DYHJhAqbuUVSZdJ0OxqfrT3LotKVOCYOrPt3WA4o5uqTrcc1GNbP1mfcJEHFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=utVNQ4sY6eiF4SWrWWcFkjjLsWXhCNtxL-qy5-O9B9V_CEFxf9o16bCo93pvR_Co96qGtLSwWw6HfkGNCVpVNuLq3ZE2N_v7Sjer_6M3imWjtFhM4r2RBYr_eO8FkNXoi2FLfq4sOTWIuhFIbMOnL8iOA5YtySUWupt7q-3zRmasziRnQq4zUDspVHy7keIsXWUh4n8Msx6u6e3sdNh5fGiTl7Yx13NbFF5akawRosds5c-OkrjeQpt2Qb7P2JqIhkgGoL-j45OajYtr6CUP1ylM6DYHJhAqbuUVSZdJ0OxqfrT3LotKVOCYOrPt3WA4o5uqTrcc1GNbP1mfcJEHFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگه
فکر می‌کنید قراره چیزی کسشر تر از این امروز ببینید عرض کنم که سخت در اشتباهید. فقط کافیه موزیک ویدئو شاهکار صداوسیما برای تیم امیر قلعه‌نویی رو ببینید تا بفهمید با کیا شدم ۹۰ میلیون
😐
😐
😐
😐
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=fQ1iwztyKWkzZoNox81DEwlIgJaY8aUZtfGxrR_Ul_BkEzLC5HNqb2dnwAPpWxPxyc-dnjUIJkQoEng7D_xnBrSSGItZR2s_eCg_G27JY6Qcdno2RglY0iZJQwpuW3GHJpfX5AJ6lYlWCDN9Ih1zgFY7U3k6eU7ea1ag96YGf6VucjRLgTvbeXdScQ5zlGepl52tIYyyiE7YP6WHF3bEonapHnUlh6iedNXGNoNhptM4_FtD7kFZ9VfZoVqJVTnAfoL9JYZB_ELiIXrRMih6KAWA9XwDU52vV1SvxIE6iivaVIrmYiM6TYa6YsyPimZeWjO6Nw_O66bvy34ssV0TVoNUstuInkQlo5YrzNUncCd_qHSjnLLQP8zM563lpR1K4UnbBkEbOfBI9-OV2ZCT6Fjng85veu60KLmcfp2DNGUV2rhXXZfWVFu5UgUwbBpoXxqHFq6eTCgwMyJyIPj25sMaF3fn3jEXniUyvF0nr8sAU1SLBdbi5r4z_j0r904yUdr5zgghZ14IkXJox4y6MTGMfd0japz5FWY-X_Da9ZPv6Yrvimj99C0j_xTu2CcBJRPvjw-D-TsUoUvCHl3eocefYgyorBvJOuh8VwinQq1Aq-hgN4TF823v3EylL8kQ2zG4IXTsKotFMGLQTpUAqvlja6uCkmKP3EBIXf5d2ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=fQ1iwztyKWkzZoNox81DEwlIgJaY8aUZtfGxrR_Ul_BkEzLC5HNqb2dnwAPpWxPxyc-dnjUIJkQoEng7D_xnBrSSGItZR2s_eCg_G27JY6Qcdno2RglY0iZJQwpuW3GHJpfX5AJ6lYlWCDN9Ih1zgFY7U3k6eU7ea1ag96YGf6VucjRLgTvbeXdScQ5zlGepl52tIYyyiE7YP6WHF3bEonapHnUlh6iedNXGNoNhptM4_FtD7kFZ9VfZoVqJVTnAfoL9JYZB_ELiIXrRMih6KAWA9XwDU52vV1SvxIE6iivaVIrmYiM6TYa6YsyPimZeWjO6Nw_O66bvy34ssV0TVoNUstuInkQlo5YrzNUncCd_qHSjnLLQP8zM563lpR1K4UnbBkEbOfBI9-OV2ZCT6Fjng85veu60KLmcfp2DNGUV2rhXXZfWVFu5UgUwbBpoXxqHFq6eTCgwMyJyIPj25sMaF3fn3jEXniUyvF0nr8sAU1SLBdbi5r4z_j0r904yUdr5zgghZ14IkXJox4y6MTGMfd0japz5FWY-X_Da9ZPv6Yrvimj99C0j_xTu2CcBJRPvjw-D-TsUoUvCHl3eocefYgyorBvJOuh8VwinQq1Aq-hgN4TF823v3EylL8kQ2zG4IXTsKotFMGLQTpUAqvlja6uCkmKP3EBIXf5d2ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
⚠️
پشمام اینو داشته باشید. تو عراق از معاون وزیر نفت سابق این کشور حدود ۸۵ میلیون دلار اسکناس نقد از زیر زمین کشف کردن که دفن شده بوده!! فساد سیستماتیک تو کشورهای اسلامی ماشالا خوب رونق داره
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68737622.mp4?token=io1bu-xR-vR69_ij_TpOB6aWN2dnKgBW4i1SO27ArLLRvoH8kuXyDclIUWFwEFGHQq71kV-6WzBJxCanuIQ1BpeoDK5GhfXet0m5xenHxLCNluxm4HMyo-s_LpSVit3hFH7wmBgbMs_o3iF1XBnuDo2OzYz1kHrtRLQ8OAYvuXN1aMTm4Wku6ZiEvykdPDAAUMXYoc4-BMn5issHoBPa0gEoPc2LUllLb33tSNkmKaf-8ytx30xpuPQn0agx_ZbuVEU-Jq_Du9JLBK_5esqHdrLTc_qrUErjxJfIszaiiuX0t9zf6sSCN4NVQ2hWE-bRk0Lyy5JsI1XAwdGWXn05LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68737622.mp4?token=io1bu-xR-vR69_ij_TpOB6aWN2dnKgBW4i1SO27ArLLRvoH8kuXyDclIUWFwEFGHQq71kV-6WzBJxCanuIQ1BpeoDK5GhfXet0m5xenHxLCNluxm4HMyo-s_LpSVit3hFH7wmBgbMs_o3iF1XBnuDo2OzYz1kHrtRLQ8OAYvuXN1aMTm4Wku6ZiEvykdPDAAUMXYoc4-BMn5issHoBPa0gEoPc2LUllLb33tSNkmKaf-8ytx30xpuPQn0agx_ZbuVEU-Jq_Du9JLBK_5esqHdrLTc_qrUErjxJfIszaiiuX0t9zf6sSCN4NVQ2hWE-bRk0Lyy5JsI1XAwdGWXn05LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
ویدیوهایی که خیلی از دیروز  وایرال شده از کربلا؛
دیروز کاروان شیعه اسماعیلیه که تا امام ششم امام صادق رو قبول دارن، واسه زیارت به کربلا رفته بودن.
از اون طرف کاروان ایرانی ها هرجا اینارو میدیدن واکنش نشون میدادن..
تو یسری جاها هم نزدیک بود دعوا فیزیکی بشه که پلیسِ عراق اجازه نداد...
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=MqH8d-7tv6easOV-eHfl9ljVqsX9htBQAhDAGYjSwrX2RlZxNq4FQkPaZOP9oSty5CPoWvoxuRX4oZSj_cS0HB3GV-2oYMJyvsdVGCuRCL8o8NZjZjb9l7a-OfcNKjzhdzy3bTR5Iu41S89YoThuFW9g3Cl0-YrymQB6b4emc0GFtXKJuGb66M0GMQw8si0K4l-OYSHkYTSLw3VveJCxwLMkzJ_WvlBqBId45hCxccPQrm4sJIlT6HHL_G2SA_PcKz6WTKJ49bHNzsVPqyG4Gi6Fp5m1wdd4KZIS-WkdcACZToU4FEMhVbYDJ6pGkTtyBCYlRd_O4AzU17-rdTyDhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=MqH8d-7tv6easOV-eHfl9ljVqsX9htBQAhDAGYjSwrX2RlZxNq4FQkPaZOP9oSty5CPoWvoxuRX4oZSj_cS0HB3GV-2oYMJyvsdVGCuRCL8o8NZjZjb9l7a-OfcNKjzhdzy3bTR5Iu41S89YoThuFW9g3Cl0-YrymQB6b4emc0GFtXKJuGb66M0GMQw8si0K4l-OYSHkYTSLw3VveJCxwLMkzJ_WvlBqBId45hCxccPQrm4sJIlT6HHL_G2SA_PcKz6WTKJ49bHNzsVPqyG4Gi6Fp5m1wdd4KZIS-WkdcACZToU4FEMhVbYDJ6pGkTtyBCYlRd_O4AzU17-rdTyDhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مترجم: «ما هرگز در مورد توانایی‌ها و تجهیزات هسته‌ای خودمون توافق نمی‌کنیم.»
پزشکیان: نه!! موشکی! موشکی را گفتم…!
مترجم: ببخشید موشکی.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=c7sCowRcMexMYFRQMA9VOTvqyrNBvs817Tui2mzDrvx6LEbhlzlki3ODGlMPYieMyie-9qkNJJ_t9HwZnY7yaGPLxKzOAmBlsFA4vBHWs1JVgt1fpPZ46RZdQKINAY79vmU2dl6j8pfXLL8Ku8h7lxmU2GhzdnM_Jm5qvNESBDmpgcTG1wT8jYdjc05zg-8T_5To-JLgDYtsVzVaZqxOdTdPKSsDY_gmDvj4KxbLrUZZ5dCvz7ONqN-0uPtuztYdS7P0SRJUMN_QTsdzk0INlbsL1Tm1i0p-mNGQPSR0LlbIj5H_bjwXY0hGG3q84lGacq1HmH4sJWtfTfBWb9TbZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=c7sCowRcMexMYFRQMA9VOTvqyrNBvs817Tui2mzDrvx6LEbhlzlki3ODGlMPYieMyie-9qkNJJ_t9HwZnY7yaGPLxKzOAmBlsFA4vBHWs1JVgt1fpPZ46RZdQKINAY79vmU2dl6j8pfXLL8Ku8h7lxmU2GhzdnM_Jm5qvNESBDmpgcTG1wT8jYdjc05zg-8T_5To-JLgDYtsVzVaZqxOdTdPKSsDY_gmDvj4KxbLrUZZ5dCvz7ONqN-0uPtuztYdS7P0SRJUMN_QTsdzk0INlbsL1Tm1i0p-mNGQPSR0LlbIj5H_bjwXY0hGG3q84lGacq1HmH4sJWtfTfBWb9TbZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مراد ویسی: با توجه به تضمین آمریکا، که گفته در جریان مذاکرات ۶۰ روزه مقامات رو ترور نمیکنیم، احتمالا تا ده روز آینده از مجتبی رونمایی بشه.
مجتبی قراره احتمال زیاد تو مراسم تشییع باباش شرکت کنه. اگرم پیداش نشد، یه جای کار میلنگه و مجتبی حالا حالاها پیداش نمیشه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=To4u-jvVDYHzQoDDnANU81aIzh20obBBZHnyLhK-WdM-wXP1FnuYEt-3cMY-AOUWQDOiebtg4kY9ErIcXAOeqLe91ywSzqoYXloTNlMk0rnWP_hOpy8E0FRR48OwpLhOnzPUM5GbNwouLsr9K8pKzWzm9fKVSPgCkN_Kxnkygyhya7c5t1mQluriZZ0JZiw6z5VHPVY3Y2wbpC5kr8RJ7vWpSN9DlkWp4dlZ8Tq5D9i-QpfFMqZGY91YhZsGpXDOcxtoA2eYypLAmpSOZXzQr08GNI0Un6blElmK3oTQSxL9i6gxENWgMek4HGBWqkEJUkBAnFRJ3uU83YboV37qkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=To4u-jvVDYHzQoDDnANU81aIzh20obBBZHnyLhK-WdM-wXP1FnuYEt-3cMY-AOUWQDOiebtg4kY9ErIcXAOeqLe91ywSzqoYXloTNlMk0rnWP_hOpy8E0FRR48OwpLhOnzPUM5GbNwouLsr9K8pKzWzm9fKVSPgCkN_Kxnkygyhya7c5t1mQluriZZ0JZiw6z5VHPVY3Y2wbpC5kr8RJ7vWpSN9DlkWp4dlZ8Tq5D9i-QpfFMqZGY91YhZsGpXDOcxtoA2eYypLAmpSOZXzQr08GNI0Un6blElmK3oTQSxL9i6gxENWgMek4HGBWqkEJUkBAnFRJ3uU83YboV37qkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do2hMvulqIdUaDQY9EXOPIqMEvqmk_yHohOAjHYmeYR2lxk7NU-QWWJtMKK4wrHR7r-9ooiehceB3NlTsvsdvjjqtDZk0o54OdbtK0j3s3BkxevdnWnYB8khkMjWpv66P_3Eq1jr6mscPdTTdnthScLZ5qf2R1gm91UJ5GNRKBAY7WrFbVqaMu3BdEsSX2eAgOKktEWYuzvAbuxAKLg7v1ZS9ZjZ9pA3pwASsoHMsPpqsVyvdx0DZ3A4Zrsoelrww8xzBzzUxE_YH2RxvUs429vPp4OTGkUH7j8qmjdTSYUmWSGzRXuYexV3j_uKKi9VUGTVpNcPoVxIH3xMLe0rnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcTN8lp9HAn4rgKtG_kdqimJETHVUzWGje00fVLmwunaek8yMPZinYpqBlzqydPJqXJ9uc3KZP5GihvyAlCLZF2nl6iV5YZ_mNm7nIkLHyRdePfXA0S7A6K5lC08Xk0klgwTl8AA03b6HJGbFKgUuQODcicrepMmsmBLhlMAT-vdBHzXspnKGJaNi2bp03oy7N4a1UQ8aUYV6Qg9o8q0pnyBysP4YLj4fbtLEXPB-CWtH-3FaRgEPQ021T_eMdO3d64WitWuVmqHLF7SYVLxTZ1pxwmZERY1Y_P0J_DEFd_BhE2IVIP63sT519-a2xPnTm3goNRmUD_eWOBZ-g9iyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=accH_xErJr1oezP-sKHkfgdZr4SrBnkvBy2JTMalEuvP4aSYAZcrL7F4jUVVD5XlIGego3PqSpa6Ga-4Oi9rtw2THbxaXK70abbWnxeitftisQ4zUWOLi7EAMXQZFSD7B6wTHc_1pkqO1m6Luj7zqC7evg7aBw0gO2jjw4xjaMf_4EO8TAx-oLOFjyaQQnU6OsKj_rVdkHaqMtVWnQ16fi62tjdvjsi5fFf4CzR7yzk9sLpYVo4N2rSUqfX0eDtzHfMyZJqqkzVCHrcc7Q1x32qj4YZ2MRI_4OtDslNtmK4SZ9NAx_Z_Tr1dVW7VSZyABqSlXPA3anSYRxm1nEdakQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=accH_xErJr1oezP-sKHkfgdZr4SrBnkvBy2JTMalEuvP4aSYAZcrL7F4jUVVD5XlIGego3PqSpa6Ga-4Oi9rtw2THbxaXK70abbWnxeitftisQ4zUWOLi7EAMXQZFSD7B6wTHc_1pkqO1m6Luj7zqC7evg7aBw0gO2jjw4xjaMf_4EO8TAx-oLOFjyaQQnU6OsKj_rVdkHaqMtVWnQ16fi62tjdvjsi5fFf4CzR7yzk9sLpYVo4N2rSUqfX0eDtzHfMyZJqqkzVCHrcc7Q1x32qj4YZ2MRI_4OtDslNtmK4SZ9NAx_Z_Tr1dVW7VSZyABqSlXPA3anSYRxm1nEdakQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fn-x7ttPWc_9zpRzCeH1oxNGFxad5rfy02hrc284azN-7SblDg0agTWBm9k9jns41yhlM1erbER8NWCLsNk5s3zGluQNJKbhQ9lYdTElJiT5YQkrJH_x6VpBlq7e-uBTUSJi5ymGk0LcVBM_daBQHQUioALnUjQvXvM8ivGsRkcxo_k0guNhjphZa_iNoU3EfM-LAqDv-TlxAZKfjPI8F2yEsMSRod4SSxWfQEHjEgzq1uvvzwkcPU2ZU1FuYwuHcUrXClE277uyw78451gjtpKDNxA-QwqT7LiXwBlcSBE15YV_00F6DcL-ZJOJZ-Bxs4jcFlcAOUlJm_egl8XyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BflolI967nIQzh_rIdc1T9NSeTeAkRqNdfuopfLs4Id7tlsKomDEcKDTc4LDFK_0Pxn8s4MXwoD2vgYzV_MIMg10YAiuHXkNYJbqASSkr1V6o3sA7Iq_m-YnHJ_6hcqLG7cEV1HblggCG54WecF8bC9rfW5p27dV3RC0g7JINGVWa-ll9SHt3_irK9fZ6yTVetnttgTD3XLDfwvl-W-3i3NbE5ZvJcMhbd7IXBFa909QusL8qVRJTbc_n1gzznDclid4HHZssEk6qCHVl2B2ljDOV5aUxqGshdbyDnA7ST0xODEcWnkKPfwgSXAsby8aOFidrGHzPtn5rhTb_Pj4Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BflolI967nIQzh_rIdc1T9NSeTeAkRqNdfuopfLs4Id7tlsKomDEcKDTc4LDFK_0Pxn8s4MXwoD2vgYzV_MIMg10YAiuHXkNYJbqASSkr1V6o3sA7Iq_m-YnHJ_6hcqLG7cEV1HblggCG54WecF8bC9rfW5p27dV3RC0g7JINGVWa-ll9SHt3_irK9fZ6yTVetnttgTD3XLDfwvl-W-3i3NbE5ZvJcMhbd7IXBFa909QusL8qVRJTbc_n1gzznDclid4HHZssEk6qCHVl2B2ljDOV5aUxqGshdbyDnA7ST0xODEcWnkKPfwgSXAsby8aOFidrGHzPtn5rhTb_Pj4Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=cHQw80rxd1LdbuYfApsV7rQPle6d9cI5quEoBlmMTTUeoo7fP6IZkZVfu1lfzUWr3gqeCNNkrFj8epkJVx_apjxw7Sad-Rmz2qF90RKh-e02IMO-_K8F9zZZWqgfhTG-1hLGX9yQZAgtP_9V4xsVATvB4csCdw1bF8XbjZ_388nowcDyDOvyFJiXWQKXirIuvtnDtsr5wyyHJFsNnEz7NwwimTSbk2qDNM6PZW6q_UWmODZhtzRjM7vSxpkFmzx_JXmHaYaLm-WwWMjSAFYicRdZJtOQuXX_7bYalAUrWpzapB91FxLHDwo8FaqV1YPDadd661HrDZPTNU7dzGEo0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=cHQw80rxd1LdbuYfApsV7rQPle6d9cI5quEoBlmMTTUeoo7fP6IZkZVfu1lfzUWr3gqeCNNkrFj8epkJVx_apjxw7Sad-Rmz2qF90RKh-e02IMO-_K8F9zZZWqgfhTG-1hLGX9yQZAgtP_9V4xsVATvB4csCdw1bF8XbjZ_388nowcDyDOvyFJiXWQKXirIuvtnDtsr5wyyHJFsNnEz7NwwimTSbk2qDNM6PZW6q_UWmODZhtzRjM7vSxpkFmzx_JXmHaYaLm-WwWMjSAFYicRdZJtOQuXX_7bYalAUrWpzapB91FxLHDwo8FaqV1YPDadd661HrDZPTNU7dzGEo0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=E9IuapouxA0JTYPsz15wEvyKLvDVZKQOtIipiqRzibgOiSrcbHt47VPeW3CW-c1yOk2BKuKlLMQ9bmAFEbgFid2cl-FbEWQuQye3WbJ9mdtAGBD5fvQeDT7-z3WAfbSqJtNeZQKcIuxt9ZcfFkqn9AMx4kDLPss71XSY5i5wF-LG_p-jhypayhCmNQPS7sLCcABKmASeEc7ou-3tIH376ttnjm67GAAM9waGNZ82WJn5lAiU8QGJYieGZDVdBoB9KgcMbPVGNBbpzP4Occ47FtPSSRHRJNcBg7KWmfdOpqoHqQsTUvUEhjxhna8GNvzXLAHb6iscXUbfshQHE4b7Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=E9IuapouxA0JTYPsz15wEvyKLvDVZKQOtIipiqRzibgOiSrcbHt47VPeW3CW-c1yOk2BKuKlLMQ9bmAFEbgFid2cl-FbEWQuQye3WbJ9mdtAGBD5fvQeDT7-z3WAfbSqJtNeZQKcIuxt9ZcfFkqn9AMx4kDLPss71XSY5i5wF-LG_p-jhypayhCmNQPS7sLCcABKmASeEc7ou-3tIH376ttnjm67GAAM9waGNZ82WJn5lAiU8QGJYieGZDVdBoB9KgcMbPVGNBbpzP4Occ47FtPSSRHRJNcBg7KWmfdOpqoHqQsTUvUEhjxhna8GNvzXLAHb6iscXUbfshQHE4b7Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=fRKENXmgk54rUn1F9qcWTbDZF5IvArXEsRfd7X4xAGM_Prsdqy9Inuc6AF4J5NnXbcrvv0dwOUo35VkX0wcbyuO5w18sO4GRWy4rl4ACGsPSgqzT1G_Q--TSyRwmeYlL8Sq_2MF1kv5G_KYmN-h-tFZ4JuH0xEreBMQLOqWZNWQdzlQJd_Y4MxIa4GUsy--RcMh7TGp2wEh0oR7fqinDclV0Iy-J6Cc9sxJfCjNxVm26pFpG0-7_9uGvnaKgpKy3EmsL6xFmXRGNfYvt5TvjPVNvywXiIEAtMRiT35CyQompUL28tVAp2cEfxQbUT7g2uATnBuE-_QDwOGfyIopDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=fRKENXmgk54rUn1F9qcWTbDZF5IvArXEsRfd7X4xAGM_Prsdqy9Inuc6AF4J5NnXbcrvv0dwOUo35VkX0wcbyuO5w18sO4GRWy4rl4ACGsPSgqzT1G_Q--TSyRwmeYlL8Sq_2MF1kv5G_KYmN-h-tFZ4JuH0xEreBMQLOqWZNWQdzlQJd_Y4MxIa4GUsy--RcMh7TGp2wEh0oR7fqinDclV0Iy-J6Cc9sxJfCjNxVm26pFpG0-7_9uGvnaKgpKy3EmsL6xFmXRGNfYvt5TvjPVNvywXiIEAtMRiT35CyQompUL28tVAp2cEfxQbUT7g2uATnBuE-_QDwOGfyIopDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=V8OFxeh42cQhjainkNwMnyd2-Qx8NcBeBmk22MrQ_rXAUAFvgbcyTHOVRJiVA-UNs4f-b7IX72tmjljIm6yMk0Dk-irARmoEpIPqNQuz10qrPrlMuOdMAYZmxmw-RHxaYhFRfvqmOvRopzIIzOw6uCM-5UHxHtOGW4wPCy-rT8sUVrF9S9vqEeAfTLr88yoAHpXm_gGEV0qVJoydCGhxiYkrd9hzrELWbwYnDwSe5VMQ10D4oQb4eZ1-u4xbVwwkmuula7znGfzV_ExfFAauVjMr3VCGPbT8xud9QbHDVUmX7ZJ5BMxnO7-X0hQF_z0AUaHifUmVU53SPiKoVROEO76NLfrU-pSzrOY2Z3DLXxkpDksBjcLzDoeVga4_HC52qnfnsEn4b5PLCnOXwXeTJ85PuFZsNm2SNbFlmhAcUNT6kN4J7n6DCuPme8qopM5NYkuuBcRZKKOIxxjMS-_ODG2I13WXt038iEiAbMTY2o3hNzciWTGatygejWs3-p5JEYKmowYGw5a0jwLBbDJbY4ck9_waLXiWJf2DCFGmqVyJYS0iTW6boZ7IleO4ke433_4QwrLNEU8CPYjpoeVdoO14rhDS_zUJvpEiyy8fGVSKJ8gG1fWyQM1rTnpAuAu7lVgUWerY9zAZ51g44yZ0EPiSQveV56tS753mf_w8CaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=V8OFxeh42cQhjainkNwMnyd2-Qx8NcBeBmk22MrQ_rXAUAFvgbcyTHOVRJiVA-UNs4f-b7IX72tmjljIm6yMk0Dk-irARmoEpIPqNQuz10qrPrlMuOdMAYZmxmw-RHxaYhFRfvqmOvRopzIIzOw6uCM-5UHxHtOGW4wPCy-rT8sUVrF9S9vqEeAfTLr88yoAHpXm_gGEV0qVJoydCGhxiYkrd9hzrELWbwYnDwSe5VMQ10D4oQb4eZ1-u4xbVwwkmuula7znGfzV_ExfFAauVjMr3VCGPbT8xud9QbHDVUmX7ZJ5BMxnO7-X0hQF_z0AUaHifUmVU53SPiKoVROEO76NLfrU-pSzrOY2Z3DLXxkpDksBjcLzDoeVga4_HC52qnfnsEn4b5PLCnOXwXeTJ85PuFZsNm2SNbFlmhAcUNT6kN4J7n6DCuPme8qopM5NYkuuBcRZKKOIxxjMS-_ODG2I13WXt038iEiAbMTY2o3hNzciWTGatygejWs3-p5JEYKmowYGw5a0jwLBbDJbY4ck9_waLXiWJf2DCFGmqVyJYS0iTW6boZ7IleO4ke433_4QwrLNEU8CPYjpoeVdoO14rhDS_zUJvpEiyy8fGVSKJ8gG1fWyQM1rTnpAuAu7lVgUWerY9zAZ51g44yZ0EPiSQveV56tS753mf_w8CaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=gajycXfOgEzNIffoD_v3hSCP2uehV9vfNQuQw3HJVVtu6Q7EuPyAwR79HI3KFCsoqJRx_Q0VKP6_H-JrQtRTrR8yyKj0QPpBBSD54dOKGtJtTOzIQVRx2Zpfyvaz5MuTF4KKWOyleg6DQM3uvMURnGZgB8_AWf_s9D9xuIm2qx2tEYOlVQyssF6_izhTrJKpbeNBQpb0TKRs-CaTdcarAMh0SL_ou1iwVUengEJwnh062RBQ0Ce6qncK2TiOONoRG7YhWEm565kdaqOj9oIxXtRYLtZhBnFhW7izhu-5fxAkIa6_KtEQe7X15b_fSU9MRE5MN7oDb8n09nvP6JrvZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=gajycXfOgEzNIffoD_v3hSCP2uehV9vfNQuQw3HJVVtu6Q7EuPyAwR79HI3KFCsoqJRx_Q0VKP6_H-JrQtRTrR8yyKj0QPpBBSD54dOKGtJtTOzIQVRx2Zpfyvaz5MuTF4KKWOyleg6DQM3uvMURnGZgB8_AWf_s9D9xuIm2qx2tEYOlVQyssF6_izhTrJKpbeNBQpb0TKRs-CaTdcarAMh0SL_ou1iwVUengEJwnh062RBQ0Ce6qncK2TiOONoRG7YhWEm565kdaqOj9oIxXtRYLtZhBnFhW7izhu-5fxAkIa6_KtEQe7X15b_fSU9MRE5MN7oDb8n09nvP6JrvZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=Kn3DO2pA3ve2WcAIINnjM6eGVGPlwmAvfUjtS8tUyXjzs2R-KqcaVUW99H8zgvuYinfaA_xeow7pJEOsrnqOY4WL4o0aamK5xVkZG07nnQzu2a4Xj7eW3xjzIdQjhkyYWVOSwXOnMplzO7IS_sRZK957XY4-kuTWldIYSLk_vigsIAouLK-RQgnPVwjbqU59ghJ9iFsotjVsWnkqUhZVFLSKu8CLq1gjDoU4o-4xyIikIM0JNiQHijPoVamB497qGSlMj2ubgyD0w6fPuvThUTF74jIItNy2S5tbdXKQzZL81HwFqdDkx0wrdugqkqfHyKvrEKgLi_vI15r1YjcwKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=Kn3DO2pA3ve2WcAIINnjM6eGVGPlwmAvfUjtS8tUyXjzs2R-KqcaVUW99H8zgvuYinfaA_xeow7pJEOsrnqOY4WL4o0aamK5xVkZG07nnQzu2a4Xj7eW3xjzIdQjhkyYWVOSwXOnMplzO7IS_sRZK957XY4-kuTWldIYSLk_vigsIAouLK-RQgnPVwjbqU59ghJ9iFsotjVsWnkqUhZVFLSKu8CLq1gjDoU4o-4xyIikIM0JNiQHijPoVamB497qGSlMj2ubgyD0w6fPuvThUTF74jIItNy2S5tbdXKQzZL81HwFqdDkx0wrdugqkqfHyKvrEKgLi_vI15r1YjcwKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=k-xH3gUsnBoYRaPYKymTlbLW5KEQBcf7a2UVFHoXgtY5Ve5TxE-yBgM287F1M6-6H9YFmGCHLJFseazkUsRIpqDQGRMs9BIK4HNl6_qF3KEeSkFRRF-yuL4_YzTql6Fx6fP3FP3QWA5tUGFKOakYM9-xcJRFhZY_aIAyg90zCywp36yRRlUCTV6c4KR4EtMxi_v-s6JUsoIjIx2FFfKig50QaJBKdXQVJL25Of44kWu-NlciPx8Yegmg4GQ1GFnKyb2eqYjmmnZODyEhQzjgKU5EUDNJmRQe6uYfqQX36VCcRNeBamEmT95HuLvo0-lu8P-ILDRq6p1XClHREOUkJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=k-xH3gUsnBoYRaPYKymTlbLW5KEQBcf7a2UVFHoXgtY5Ve5TxE-yBgM287F1M6-6H9YFmGCHLJFseazkUsRIpqDQGRMs9BIK4HNl6_qF3KEeSkFRRF-yuL4_YzTql6Fx6fP3FP3QWA5tUGFKOakYM9-xcJRFhZY_aIAyg90zCywp36yRRlUCTV6c4KR4EtMxi_v-s6JUsoIjIx2FFfKig50QaJBKdXQVJL25Of44kWu-NlciPx8Yegmg4GQ1GFnKyb2eqYjmmnZODyEhQzjgKU5EUDNJmRQe6uYfqQX36VCcRNeBamEmT95HuLvo0-lu8P-ILDRq6p1XClHREOUkJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pWC8tVNL1QbL3OWpsyFatW1Wellno3JBNiCONWZ8B9U_MuxGemDE-41gd8meBTwGOVpzuzIESByrDoTjQ4dmuUYKX6LgaxSiMNC-to1YWe5Z8ykQFO4RmXTZrA0jMVr4KIOnFfYIgLh4f7cIdhpal5P7AGINbEolhsKCG_bioTY7tKxLLJg_Axstc5RAVYaMeWH7BMNs3lsnUAPrOLg0rWVekYZ_Hwqz5S03kQflRSOK6rNuLzUMMMpCG0BQ5wE1p7d9gmE4kMAVMtCTxfbb07JDLAc6dGCK253bzPN4y8ukaE34ov1zrHlAy3_3kU6nB-hzHFaouQTymOo_AQNNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=MHxGDpPlIiM2NTQ9CeXAp1vSva5VGtEdychrQGv8h9KJYKx7THMs_pJLh-wgqNZuZ1GqOksh99MkWNr_hg1YMIYkHrm3faYx1Vhkub9SZyJuGJAny0pB6OFiVb7iCfTSNvJ621HafIJO8sQOA1ZuWBXBSipO_Pi9fz-nKULoXjkwOveuQ1wVKJQKnRStFsR0WH4uv-l6JY9ssWPOb1hDMTVNrOrX_BYYQk5M8wfGHKJxG0GixTA7KTqjeVYgLtFX8GtUPcuVCdMKueqLmhrNoteSiDnbY0eWNfOI21dCiOIoUxI7S8120-ouBZfuFqNmX646mOSZ4RELYX1jXShQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=MHxGDpPlIiM2NTQ9CeXAp1vSva5VGtEdychrQGv8h9KJYKx7THMs_pJLh-wgqNZuZ1GqOksh99MkWNr_hg1YMIYkHrm3faYx1Vhkub9SZyJuGJAny0pB6OFiVb7iCfTSNvJ621HafIJO8sQOA1ZuWBXBSipO_Pi9fz-nKULoXjkwOveuQ1wVKJQKnRStFsR0WH4uv-l6JY9ssWPOb1hDMTVNrOrX_BYYQk5M8wfGHKJxG0GixTA7KTqjeVYgLtFX8GtUPcuVCdMKueqLmhrNoteSiDnbY0eWNfOI21dCiOIoUxI7S8120-ouBZfuFqNmX646mOSZ4RELYX1jXShQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=mTo2PT0HYK2O4cfERqOQWysosquXJzehb9MZGpvARBnHn8RvQeNitEyKlKWS2zbCAy0WgbrRpBOLet9awwuOqJmgbLMbasHOhEwbx82q80x2Cz83RvEwOgQ6WgYbtfkKOnULscp0NUFuJXq2mmCnT6MTHNRGLk7hdTAjDbL3GQ6Vjcfo05ND8PK90gAP8EzmvDJtx1qtExE50MXwWP3HWEY5jFkI3rC66rd-RxJFecHz2mYJDchtOciQNdoGo0i8IeGpHNdrHBqom6XJpxEsdD9KBNQvNJD5XV_FoO-TwfYdXOau_4H48yCDzrLaew0vl32qseDEzA88RHKarx8NbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=mTo2PT0HYK2O4cfERqOQWysosquXJzehb9MZGpvARBnHn8RvQeNitEyKlKWS2zbCAy0WgbrRpBOLet9awwuOqJmgbLMbasHOhEwbx82q80x2Cz83RvEwOgQ6WgYbtfkKOnULscp0NUFuJXq2mmCnT6MTHNRGLk7hdTAjDbL3GQ6Vjcfo05ND8PK90gAP8EzmvDJtx1qtExE50MXwWP3HWEY5jFkI3rC66rd-RxJFecHz2mYJDchtOciQNdoGo0i8IeGpHNdrHBqom6XJpxEsdD9KBNQvNJD5XV_FoO-TwfYdXOau_4H48yCDzrLaew0vl32qseDEzA88RHKarx8NbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=Gvph5-i2PZQgZiVo4Gybcw2l3cEaxGn3TGFNJ5ddrCwxnTVy1Shwbr_2E8CgYAdbBgk_TbDJAzSUmc7knP4aSN4jKZBFwWTcoD1pEbsfkzk50DCgxX9kRHYUZBHDR-DZ7vpPpXso05wSY_Pvr5mMM2EokpsgE1XQJ1WZtX80bcy7ISIOoA05uHg8OWRFnZyWEUWKMNVz0C9hUnyhW9m_iDKyLZOfuPpZBEbehtqRRfPUK_OsCXP7vEQhH1WvfBXVTBHFqZrWJbMZKB40qWmrzsDwEB_YexiQxfqRxQ8vU-P30a7O8amFfFZw_FhJR3RrUhRzjCI1noxNh5WKfGdQ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=Gvph5-i2PZQgZiVo4Gybcw2l3cEaxGn3TGFNJ5ddrCwxnTVy1Shwbr_2E8CgYAdbBgk_TbDJAzSUmc7knP4aSN4jKZBFwWTcoD1pEbsfkzk50DCgxX9kRHYUZBHDR-DZ7vpPpXso05wSY_Pvr5mMM2EokpsgE1XQJ1WZtX80bcy7ISIOoA05uHg8OWRFnZyWEUWKMNVz0C9hUnyhW9m_iDKyLZOfuPpZBEbehtqRRfPUK_OsCXP7vEQhH1WvfBXVTBHFqZrWJbMZKB40qWmrzsDwEB_YexiQxfqRxQ8vU-P30a7O8amFfFZw_FhJR3RrUhRzjCI1noxNh5WKfGdQ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=JZVRtmpNM57LWWn3cX8HqMHCU08BI-uxlOu9yoj3KeeWGuIPq54s7M00sLMnLKuZWqr-SMyEqcXzUm3jmj1Iu5HsV_QJczzhVYtaQn3RJnu_f8UHE1eZCnBruhMkwNenQUOrhn4rwq46yvGwtSFX3CEBhTXbXVY6bJ62SfG8JNLNiRPnPetSbDm9EEMGt98yLCEn7IpLzLWWPIfVdgRBsTsk10IQ4hHq4pj83mzA_m5dSfF2bd7P3GR9QKWrHec9boCPa23d_4hpsOVYHgT5YUYAmiBAwCLDhFYV2HNBoJXhYzKFE0iqZiINuXRPsnpbzNY4DjlYqnCEfj1W1u9hpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=JZVRtmpNM57LWWn3cX8HqMHCU08BI-uxlOu9yoj3KeeWGuIPq54s7M00sLMnLKuZWqr-SMyEqcXzUm3jmj1Iu5HsV_QJczzhVYtaQn3RJnu_f8UHE1eZCnBruhMkwNenQUOrhn4rwq46yvGwtSFX3CEBhTXbXVY6bJ62SfG8JNLNiRPnPetSbDm9EEMGt98yLCEn7IpLzLWWPIfVdgRBsTsk10IQ4hHq4pj83mzA_m5dSfF2bd7P3GR9QKWrHec9boCPa23d_4hpsOVYHgT5YUYAmiBAwCLDhFYV2HNBoJXhYzKFE0iqZiINuXRPsnpbzNY4DjlYqnCEfj1W1u9hpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=PrAXshr1f9yan6GlNkxFMnDBDONvyv5nPQ-eFMYjLifRRR5FWOvTSKQZcmUUEJj1s26oj841-FWT5MDkpbSl9j39nJLYeScQPUcnfUXlpung6rBQuU8DoxlzSsIx0rKiM4QrrZLWZRrwuKYQJmfdkNzCn7UhcAPfX3D5J8hkvEvzoNCOafyDPYjlxRXEKueyFnqS4daGT9tzE2k9AdhAT6QP-HOWb-MxOINnHivq7g1wKm4TsGEhaLCa1Ay9brQpQhB6S4IXQYb65hsbOtFrWdHAdZYDuf75HkGvKAYxUoxKh_ZSaGnZcJnUE--QtQ5WGAMJ3yFlKcE_Uv2uE4RKtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=PrAXshr1f9yan6GlNkxFMnDBDONvyv5nPQ-eFMYjLifRRR5FWOvTSKQZcmUUEJj1s26oj841-FWT5MDkpbSl9j39nJLYeScQPUcnfUXlpung6rBQuU8DoxlzSsIx0rKiM4QrrZLWZRrwuKYQJmfdkNzCn7UhcAPfX3D5J8hkvEvzoNCOafyDPYjlxRXEKueyFnqS4daGT9tzE2k9AdhAT6QP-HOWb-MxOINnHivq7g1wKm4TsGEhaLCa1Ay9brQpQhB6S4IXQYb65hsbOtFrWdHAdZYDuf75HkGvKAYxUoxKh_ZSaGnZcJnUE--QtQ5WGAMJ3yFlKcE_Uv2uE4RKtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=WxGWC32fO3IvkfRLxndC9zQCqJTVMe65KqbhVv7yHGpMNSxKbnBzQ_48jl0fBz4ji1AThwyLTO5GJBqaeUtScxxgQfejD5U1lHtLZArXmvw08PPthky9PPC-xKSYZO5-5057PpFNNEOuXkzT_IcCqbvhp6qNFmqKXmRHb_YJ_UUjNmoc1_fZBH3N0OMNDQalePRlcRCBV60ns5JVZ0nKaOHtPBbLcEjQrXYntujZC8H4qz1V8C_WijnLPoGDckd0PRK5a4Bdk1v7l6xdIaGbRPtz7WhtLqcdcA9L7qdDPdt8cuQ88A3p8bC8ahRJ2H5FUw4Bun9RLDPDfM0Tv6epTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=WxGWC32fO3IvkfRLxndC9zQCqJTVMe65KqbhVv7yHGpMNSxKbnBzQ_48jl0fBz4ji1AThwyLTO5GJBqaeUtScxxgQfejD5U1lHtLZArXmvw08PPthky9PPC-xKSYZO5-5057PpFNNEOuXkzT_IcCqbvhp6qNFmqKXmRHb_YJ_UUjNmoc1_fZBH3N0OMNDQalePRlcRCBV60ns5JVZ0nKaOHtPBbLcEjQrXYntujZC8H4qz1V8C_WijnLPoGDckd0PRK5a4Bdk1v7l6xdIaGbRPtz7WhtLqcdcA9L7qdDPdt8cuQ88A3p8bC8ahRJ2H5FUw4Bun9RLDPDfM0Tv6epTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=C4A2uFJiOmpk-3WMVuAL546f7yY_w0ChaFmnl9F09F7ux-hEQOWuI_hnUE0zndudGyu8mvBadn8PIY9xak2wdlbhzSliq3IQSVIGQuDrK7MtPsDpQOUs1NGyMjMbHuSpi_dyS0WhhrqS3R9DrfYz_1DhAXbt7OdI9YpgZ_tOAUQ0c69_4_rloYNmSdxsezYv8n6SGU7Fty3O6qwPJIn-bNEkmtH_OkW81_8dDffgDCMV82ssIMrF6nVOJZymz2fF7BEpw84TTeTa9YSPEg3IBV19_KK2SNtoykRm1xYqNtQNTCIp1wO7KI-F3-xiFUPcHRG6z_jI5NOUxVtBnpFtwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=C4A2uFJiOmpk-3WMVuAL546f7yY_w0ChaFmnl9F09F7ux-hEQOWuI_hnUE0zndudGyu8mvBadn8PIY9xak2wdlbhzSliq3IQSVIGQuDrK7MtPsDpQOUs1NGyMjMbHuSpi_dyS0WhhrqS3R9DrfYz_1DhAXbt7OdI9YpgZ_tOAUQ0c69_4_rloYNmSdxsezYv8n6SGU7Fty3O6qwPJIn-bNEkmtH_OkW81_8dDffgDCMV82ssIMrF6nVOJZymz2fF7BEpw84TTeTa9YSPEg3IBV19_KK2SNtoykRm1xYqNtQNTCIp1wO7KI-F3-xiFUPcHRG6z_jI5NOUxVtBnpFtwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=krRyfWglZUZl5mYHYcGCSsEsMCuHABQScrStRmevX6kv33nXBfH-6GQkQ2ri9NT65NxHQ80OwZ6bek7qiNigrZ4mhyc5mIJmB4kNrJ7lo48ZZj4-D9N1O4G6LT1_XYPVsLQffaAfMhlwwcQBVSn-vwrFcT9os_9P5mAnv6teqec33kR_s3zc_q9y-HgXVPL8LlyS7S6zMqqGbLbgiRcTI4Qj5sFLlgcYou4ZTci4z1WCuvMHBuCk0kLKYIMY7Sz-t6drTslJnHuhr-6o3JZYb1IE56oUScLheKD9s-UWFdgDqWOSQv9BMwXOGN0OYxops6LsIXvYjVH3jRpbFoh75A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=krRyfWglZUZl5mYHYcGCSsEsMCuHABQScrStRmevX6kv33nXBfH-6GQkQ2ri9NT65NxHQ80OwZ6bek7qiNigrZ4mhyc5mIJmB4kNrJ7lo48ZZj4-D9N1O4G6LT1_XYPVsLQffaAfMhlwwcQBVSn-vwrFcT9os_9P5mAnv6teqec33kR_s3zc_q9y-HgXVPL8LlyS7S6zMqqGbLbgiRcTI4Qj5sFLlgcYou4ZTci4z1WCuvMHBuCk0kLKYIMY7Sz-t6drTslJnHuhr-6o3JZYb1IE56oUScLheKD9s-UWFdgDqWOSQv9BMwXOGN0OYxops6LsIXvYjVH3jRpbFoh75A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=E4CXET3mta3EVOB3zznVe7JxeZP66SuKZjdNqUe7pnSWIm2B9kDVhfsuzwU6Cn7waxjYFgH7b8bBV3IMQ_2OC_ZxeSjV21dRWNfzpdKbjU_82Zuo0TuFyvbOlHnUSEgGZkswMY9sLZgSHM9YCqaYNbk8lQRlacQlOd9c-v1V6ipVJwjF5UlGlxO_gLXmdPyFuRnDVynUpGe7aE-rTB-z1werGc3kAB6vpM0UWb6bgJ1DThb3uRRurSCBDPMAlzG4EqHbJOmec4YsSfCtpYxOeOzexNURuCH_18OjvwgMzrDwShalIMCYJ_hSIk5E58S2pg3VtW5fGdlQcMFX7fJ5zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=E4CXET3mta3EVOB3zznVe7JxeZP66SuKZjdNqUe7pnSWIm2B9kDVhfsuzwU6Cn7waxjYFgH7b8bBV3IMQ_2OC_ZxeSjV21dRWNfzpdKbjU_82Zuo0TuFyvbOlHnUSEgGZkswMY9sLZgSHM9YCqaYNbk8lQRlacQlOd9c-v1V6ipVJwjF5UlGlxO_gLXmdPyFuRnDVynUpGe7aE-rTB-z1werGc3kAB6vpM0UWb6bgJ1DThb3uRRurSCBDPMAlzG4EqHbJOmec4YsSfCtpYxOeOzexNURuCH_18OjvwgMzrDwShalIMCYJ_hSIk5E58S2pg3VtW5fGdlQcMFX7fJ5zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=ENayKoDmYKVdrC_SzTErAybYB7gBWTB2UiCXhqq7CJH-7TKvTjJfnXHjdKxiT4-zzkdEyTK6RKg_h1gAk0mrLhUAWmUHywBF0QPSJAVJWXhUX2Mg1izAnC8nJWZBsVTGa_qMwF_9d0IV9uYZ0LCdglAtNrwKKT0wwrce7P4pXPReD40lYDzYC7vVtpD1VjSyjuox664xZT3yFUpX4FTw8qqFKUwqYY5LVNfxKsh33uU8bL_r3ozAylQW5L9WIZYfiYbUI1x9uHBVjUlr3ZvE7LyoYkqXqGJ32LWLbTBH2t7FTO7wn4rU2W4b7rxIC8VJ4Q-DfyYJocMPlyiPUS0Bcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=ENayKoDmYKVdrC_SzTErAybYB7gBWTB2UiCXhqq7CJH-7TKvTjJfnXHjdKxiT4-zzkdEyTK6RKg_h1gAk0mrLhUAWmUHywBF0QPSJAVJWXhUX2Mg1izAnC8nJWZBsVTGa_qMwF_9d0IV9uYZ0LCdglAtNrwKKT0wwrce7P4pXPReD40lYDzYC7vVtpD1VjSyjuox664xZT3yFUpX4FTw8qqFKUwqYY5LVNfxKsh33uU8bL_r3ozAylQW5L9WIZYfiYbUI1x9uHBVjUlr3ZvE7LyoYkqXqGJ32LWLbTBH2t7FTO7wn4rU2W4b7rxIC8VJ4Q-DfyYJocMPlyiPUS0Bcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=CfxBIori9fcELjAtIRLfMB51mqD7X1Bid_pyYCzlQhRneWV3GEzFauUMPaL9FA_fbsWWgMloDV61f_Er4p9o3j_KSP0KQLL-oObqc7YtjfIi2N_cy43iKNHc98rjrzqFFLlSzBuYq1SSAPZxU6GRATLshwHBgxPuj_ac_d6F32QJcHEbGaD-H-SwTXsfzq8cTdzPbHFRZ5aGCVchiyR7hYQH76wLC1_KSLJrB2NzHwzR_WaT6NL6mewmIqlDtj873yQ03IS_3woUJO4N5UUeD_QvafW3I71lkeXc8G5TUDUZvhl6EKhDz9yFTypZaOEze5xsGIYv5JAgeZE9K2dt8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=CfxBIori9fcELjAtIRLfMB51mqD7X1Bid_pyYCzlQhRneWV3GEzFauUMPaL9FA_fbsWWgMloDV61f_Er4p9o3j_KSP0KQLL-oObqc7YtjfIi2N_cy43iKNHc98rjrzqFFLlSzBuYq1SSAPZxU6GRATLshwHBgxPuj_ac_d6F32QJcHEbGaD-H-SwTXsfzq8cTdzPbHFRZ5aGCVchiyR7hYQH76wLC1_KSLJrB2NzHwzR_WaT6NL6mewmIqlDtj873yQ03IS_3woUJO4N5UUeD_QvafW3I71lkeXc8G5TUDUZvhl6EKhDz9yFTypZaOEze5xsGIYv5JAgeZE9K2dt8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhVBzIbHSknKxjmVDX7np4kb2WTdtaZ7_tss_uPPFinePykt4FU5FSoZRDlGQi08CHYNsZEx6JxS2-C-rjb-ajCG3Ifvb-4SC1vgtl9_HWnttdMdV48qbF6L-R0jxh2NPr-zh19RYzdSayz3fn3jQIZHOVNXGcUefH9UWKt7if4YeUC0YsYcor6AkYUaubBzNBu6lNVuzYaYsMytZUII9OxAwnUqbzehL2Y9D1bnGbIYQwG5XHU2kYHgcS9FaDmhHdR60XWq_hQjXZXHp4p3wZlp3J3FrRlDFNRGlAzF_yCBH-mhzpg32Xxi3_sQEK2vsn7BLPxQ8nEllziVjnYcgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e5w1asE_aDwlpM9jsZVJU0ySglPJXxMkqLE__DmBKLICYyvq9fwFBB1iwSgOpxtHQHCc4i8PBoHYGbR9a6lPC-VjxTxOlTr4ZJh6byhZ-zxAUOGCG0Y7MBmumpe720uDj8KfwG9UuXWS5aO3AkWjpvA69REAEmYuGz3A8ONHn1BeiqmsLTkNHlC8EtzM5eW9-r05YFoPrmv-bCGq_1VJn09w5q287J1UsrN9qq0XsYGUEW7DMfu2eXdRZkZm1P0MmS7L_CXHiwvc58ocg1YUZRx6grhC_osn9-b7gYZ5O0fSuivsa7UBPsu3Hmb-mRlFT-4g7QHtSeTcmbXNUTkRTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=LZC-Lgvzo2lJH3JJc1dxZ9BPJyB_kmp5HB8zXk3dbrUP5QraT7p1BQicI4KzOvRYf3KWa4eMO0SIVSLTLT6WnHSswiISzaLCu0sDq1Q0QMuCFXHD1R-nqeYZb9Ewo9Ve6GzEeMeOCDCCD8PBMIEEzAkhswUQrAyh7qNnoOE-_dURHH16nkNw3w8OobThS2KNOrUiWlb35eNUkJrOcFz3Bc8rIXflC0UZlz6NcmHEEkvEtgvMLqscPzHOifWcezH2LzHnL673I-knGA6l6adfqCMmRFVrJ4xnTMtcm96YCVjH5nJ4XxWNF_uHr-3Hh9lVBtWLnq2201Qa80-p2JAsTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=LZC-Lgvzo2lJH3JJc1dxZ9BPJyB_kmp5HB8zXk3dbrUP5QraT7p1BQicI4KzOvRYf3KWa4eMO0SIVSLTLT6WnHSswiISzaLCu0sDq1Q0QMuCFXHD1R-nqeYZb9Ewo9Ve6GzEeMeOCDCCD8PBMIEEzAkhswUQrAyh7qNnoOE-_dURHH16nkNw3w8OobThS2KNOrUiWlb35eNUkJrOcFz3Bc8rIXflC0UZlz6NcmHEEkvEtgvMLqscPzHOifWcezH2LzHnL673I-knGA6l6adfqCMmRFVrJ4xnTMtcm96YCVjH5nJ4XxWNF_uHr-3Hh9lVBtWLnq2201Qa80-p2JAsTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=KeznnPKXlQ8qPa9ncnxVi2z7Vlt6LDI5Jl34EbJ6UO1xu3wYGfOQdxzSuVa3dhXCUoHrnzy6byxyjq__mtCiHMMf31rTo4fMwhJS5fM6E9WAZtlH2SMxrAtRoT2m_BJRdW0SUtkIXAy6u9VCduulq6x4RfGXkxCMf1ehD9Trjq6PGHFGHHyhBhtLj3bxY1X8lCjpKNCla_VyLs6UBMuR36gYaT2LTnsAp535lJ7BmBZSRM5Lr2EYOfvNkNX58FL_sUg3Pcyw6d7DpYkjnmNbXF2GEkeKt0EeHWpudsWh9TI2E1xzbtB8VTuUM6FLEKma4oCONa1jXoGj52QoOXdQlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=KeznnPKXlQ8qPa9ncnxVi2z7Vlt6LDI5Jl34EbJ6UO1xu3wYGfOQdxzSuVa3dhXCUoHrnzy6byxyjq__mtCiHMMf31rTo4fMwhJS5fM6E9WAZtlH2SMxrAtRoT2m_BJRdW0SUtkIXAy6u9VCduulq6x4RfGXkxCMf1ehD9Trjq6PGHFGHHyhBhtLj3bxY1X8lCjpKNCla_VyLs6UBMuR36gYaT2LTnsAp535lJ7BmBZSRM5Lr2EYOfvNkNX58FL_sUg3Pcyw6d7DpYkjnmNbXF2GEkeKt0EeHWpudsWh9TI2E1xzbtB8VTuUM6FLEKma4oCONa1jXoGj52QoOXdQlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=FrBOuVwRwOPYAFXUvR0nsHael-XZsPLA1_J7HSneFaQwO93RVKaau_difNHxj3SbOFfHLTgIZ9Xk4RnQQcS_jD_2nPXC-4CdtW0YgcHjDOHf5KZu7UJgUv8BIv9elOU0TakVBmrYGjOVIV6OIsE5_BbWziyyFSTV1JuTAI-vJoNb0PdB1n20cuWvSweFWKW-cXpLV_yr6Zhe_GqEnonwY-fB_xO5a52UA3ZnqUK16p8ulwNzTY0Jc0H9OhE2D7VBq3nB35xGrVUWURKFjaemFJYhnS4CqKgEg2d7tUZQ5epaXhl7boKP0CqABcFCFhTxReLPrIQs-2sKc-54pH-uNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=FrBOuVwRwOPYAFXUvR0nsHael-XZsPLA1_J7HSneFaQwO93RVKaau_difNHxj3SbOFfHLTgIZ9Xk4RnQQcS_jD_2nPXC-4CdtW0YgcHjDOHf5KZu7UJgUv8BIv9elOU0TakVBmrYGjOVIV6OIsE5_BbWziyyFSTV1JuTAI-vJoNb0PdB1n20cuWvSweFWKW-cXpLV_yr6Zhe_GqEnonwY-fB_xO5a52UA3ZnqUK16p8ulwNzTY0Jc0H9OhE2D7VBq3nB35xGrVUWURKFjaemFJYhnS4CqKgEg2d7tUZQ5epaXhl7boKP0CqABcFCFhTxReLPrIQs-2sKc-54pH-uNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=Xu-2WTKZctawwCTSNDIy4AcM8gPeWbqewoW4tOc_Zy7PQoGOeaP-A55qqjYkD-RNcCENHBHXESbMT5GNobjEvr90rCOS5ANOLO1FXsVjH8Wn-J3JUnd98J0zFATQwnwr7NV50U5X_zQYj5d_hoZS29es74XveAXn0ISpfThXT0BJhHJf02fPW4fY2Jwu-LtF9f2-K3GyEG4o00lcOO_BMYVDdq8gsGpSEOhB1NJ9ND4OW4Tua1-vGS6FbU_ByS-2OjXQnaJy-PI9GD1iCV3ogf-rr5_2wUOE40_EA2kHHHFAnIlo-6s8fl_8FX1np4xTZfF_NuIRYq5j46a8f4C_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=Xu-2WTKZctawwCTSNDIy4AcM8gPeWbqewoW4tOc_Zy7PQoGOeaP-A55qqjYkD-RNcCENHBHXESbMT5GNobjEvr90rCOS5ANOLO1FXsVjH8Wn-J3JUnd98J0zFATQwnwr7NV50U5X_zQYj5d_hoZS29es74XveAXn0ISpfThXT0BJhHJf02fPW4fY2Jwu-LtF9f2-K3GyEG4o00lcOO_BMYVDdq8gsGpSEOhB1NJ9ND4OW4Tua1-vGS6FbU_ByS-2OjXQnaJy-PI9GD1iCV3ogf-rr5_2wUOE40_EA2kHHHFAnIlo-6s8fl_8FX1np4xTZfF_NuIRYq5j46a8f4C_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcWNyMWvYsRKE-9m9XmUMdVMrLvvh5tBWZHpWMbuBRzKLazcr1nfxXM6Ht6JU-3Nx3wTRgyTRFHYhIsQbvdgsmN0PRDaEmwaI70c-khYmXYUCbT1xXBckwPXSuWLh2tjJ6GtUfp4178HgLvRFOOahMlAYnRVaBIpEUpAKVHuBb01Y1nEEvX-fMIXEtOFRgwI33_7q1axLeXZPiBBS17wZbzxRFUhrypIdHoO49Vgf8w4ZhtnIoevi7Txs83_Bk62-Db5x53hzO-SRJIF_Is9rb-o0F7SQyqUSOevgCTQMAYWaIQlaHTJ7WHuYMvSYTVrEnmBaMqv-YPzQAylb5XsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMEPRU3IOkzcGyv_xN-DuJ0Y-_xc_tVwU5qHgs5EO7wp1oC9zmGZ1mtE0EF4ZZZMKnDdEV7hyb3r4vKUa2DZ6hkDXsl1YjpE3P0B3bsthb1EIx0ILe0Plz6JgOja3yxH0cjE8HhY-wycWtEvOjWEW_eLi0FNG6OyVMk0Z9xhahTdLQ5pnXu0izRkZ_3XVNLLNzCFswhUL314CgKPLQrVLezCWwT8v8DanNeZzghPDpBUR96e0urbtCnbVzrPAZBXnfVbUOGfpjUWNH36402tiZGpf1uTS2hLJjp41VSwIS5XVTE9hwrxCiMDwarkRsF0RNQ_BOd9QG5opyDCkO_oFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-288AwleY1Ls29WV7htMWo_c--eukKVzcS-nFH_E8OWEvRFTYy1DfpfjB5ad1p8RreG0JALN1vVW0N9iLr6yJlmV9yohOzx4ELoyCoso880DnMgg_Uv9oXLWVppdAIKXG_gOGbH4LHLZlrn7X0s7pn1q9LWWrTZCcuRY3mc4_R1sgP6RqLDBFPh-6W-TH2v0VJ-ZohJvLYvHacllMjrp3PryjIpHy2YDjHgEpzdj-amiTTpoztXkBdrTeKVki_pxPeO7hyXTgKGZyjaEX28i1N1PDjWTxmFDpWUBkJns0kJUfv534q3KVlWoID65wCfEAHWmcGrHxp5ozrbDe1c6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«با وجود اعتراض‌ها و اظهارات نادرست آن‌ها بر خلاف واقع، و همچنین هیاهوی مداوم رسانه‌های جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند، ایران به طور کامل و بدون هیچ ابهامی با بازرسی‌های هسته‌ای در بالاترین سطح و برای مدت بسیار طولانی در آینده (تا بی‌نهایت!!!) موافقت کرده است. این امر “صداقت هسته‌ای” را تضمین خواهد کرد.
اگر آن‌ها با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای در کار نبود! بر اساس این توافق و دیگر امتیازات مهمی که ایران در حال ارائه آن‌هاست، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی دیگری اعمال نشود.
با این حال، تمام کشتی‌ها در جای خود باقی خواهند ماند تا در صورت لزوم محاصره دوباره برقرار شود؛ هرچند در این مقطع چنین چیزی بسیار بعید به نظر می‌رسد.
پول‌ها و/یا منابعی که وزارت خزانه‌داری آمریکا آزاد می‌کند، در یک حساب امانی (Escrow) تحت کنترل ایالات متحده نگهداری خواهد شد و صرفاً برای خرید مواد غذایی و تجهیزات پزشکی از خود آمریکا استفاده خواهد شد؛ از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما. ایران به شدت به این اقلام نیاز دارد.
این یک بحران انسانی است و من احساس می‌کنم که لازم است همین حالا کمک کنیم، پیش از آنکه خیلی دیر شود.
گفت‌وگوها به خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=UpgTWZXIzhEtbGZsTMqziwc12oxALo9dWGSsytPSoT_4i1_CTxEuT5DN7_MMIkBAhog3l02xDKfw6QEPKVQx4vVkab_lf5qcKScUYX-j7uNdcQXE2tic6FFo3oM5532c42lDAo0dD9BVXV9-oh56lqBbis3x-nJbtiEtrLwamhjRtdGQyJycDJcBVnoaTRxlQs1yZQ2qqT0Uv9St_g_AYPNKY_IxPhtzOVl1WFUYqf_hfJe9V_7UAgXselvKKX9iLI6jJ3pUjlTZ2T8w7J0HV2akZovDo9BxHQnYmvR5hTJlcJGs-hCeZeTXeiHlKKBkRgr6q502Q9xkLjVp1h70Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=UpgTWZXIzhEtbGZsTMqziwc12oxALo9dWGSsytPSoT_4i1_CTxEuT5DN7_MMIkBAhog3l02xDKfw6QEPKVQx4vVkab_lf5qcKScUYX-j7uNdcQXE2tic6FFo3oM5532c42lDAo0dD9BVXV9-oh56lqBbis3x-nJbtiEtrLwamhjRtdGQyJycDJcBVnoaTRxlQs1yZQ2qqT0Uv9St_g_AYPNKY_IxPhtzOVl1WFUYqf_hfJe9V_7UAgXselvKKX9iLI6jJ3pUjlTZ2T8w7J0HV2akZovDo9BxHQnYmvR5hTJlcJGs-hCeZeTXeiHlKKBkRgr6q502Q9xkLjVp1h70Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
ارتش اسرائیل در نبطیه الفوقا به افرادی مسلح که در نزدیکی نیروهای این کشور شناسایی شده بودند حمله کرد. بر اساس گزارش‌ها، ۲ نفر کشته و ۲ نفر دیگر زخمی شدند. این نخستین حمله ارتش اسرائیل به لبنان پس از ۳ شبانه روز بدون هیچ حمله‌ای در این جبهه محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=n4oR4BxEjJvD3mpKJ1hSHNsfsDMOC2S376i518amulNrOEdTfgTPoLZV0GjrBMUOcuLuqruczdvjW2bu0tv5N9lXz_tIhf0EB2malor3vnbyDEH-GhY9AiiLiwCLDTjP6xQEHL384e5kN6OlkHxMx23f3s3Zzl8yNNyUX5u3llj4e32JFsNNBnv8MkYcok0_BDesFCLhjk0Lo-FCI1G01jCOyQegBGrhcs5IQfZrHlC6CQiaWnNEdTNhKJJ1DNEbFpAlpIINOFlLKijhQXJtWjDF9EIKH90AeyuYi1O4tzETRR7y25zI39GZTdoUcQ72qqjGxBZqcK6W3BF28xPFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=n4oR4BxEjJvD3mpKJ1hSHNsfsDMOC2S376i518amulNrOEdTfgTPoLZV0GjrBMUOcuLuqruczdvjW2bu0tv5N9lXz_tIhf0EB2malor3vnbyDEH-GhY9AiiLiwCLDTjP6xQEHL384e5kN6OlkHxMx23f3s3Zzl8yNNyUX5u3llj4e32JFsNNBnv8MkYcok0_BDesFCLhjk0Lo-FCI1G01jCOyQegBGrhcs5IQfZrHlC6CQiaWnNEdTNhKJJ1DNEbFpAlpIINOFlLKijhQXJtWjDF9EIKH90AeyuYi1O4tzETRR7y25zI39GZTdoUcQ72qqjGxBZqcK6W3BF28xPFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z63Z3u3tRa_CGIUwm5XzhqOtYixrWFd6qPFcYfxcBbCfKrAvCsnFp5iUGP-X4z3Czru8JOEBhN45Z337ViIFbszOEf-jKz6d7r3EO0UXGx3V1dB18D-S8L83Qq4G37uHlZYo4u8UO2_Owzbj9kq6f0pYVnvfk61XEpj_p1arksu21-WsUr1UMcvoEML7IvwJGOlnzP26ljffhKW7jyKDT3yf0ZU-b1u6ZhFENLaNwCADzHcVDh5LKO3qSpm9WiV17KOvNhJG44sWjH95fH_QboXRpYWoIFRJ-Zxj-OKOKJtsfKn9DbMbqYnkw-voN9gotecYMjMAq7j91KAO1t6iTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=WWlSFHiS6AM8WTGljRD7tMXGlkN6FQzVaCJItk8EpE0SBPvur-o3rdCuuJ9F3JLloTKLO7MhTXgBZfZAYFrokSDrKSwi0T-Jy1eN-vzqhyztHKhMdpP4b1PIoBMGsRRo2d8ouJGVyKigoE5VlmPo7r-VLtWOzDU40k_7dZsvAMu1zEtPK5brM_x3-3HVj9coHg2cBctKjThMgDxRdvEkVTEooHut1i7c25fyqnuGHjRiL4-VZuK4vftC-QCbo7-ujJKU9GqNicHooCCh4tzfX4jnHF7K7hdjvwMzbQL_j2f3tQ_OzCZPUzYMInJCvBSpEJxg4T9tb-BzT9vr3lznIDnPp-dggRC1GV0bFp8T6RCpjhNXDoFGYB0XB_KcoMTXTLREjAPn0isgxoeU2PUFRZvhucNGRaLDrZoK0WzaSGPcC9rM-0kdO2Lr0_vyqWBzC9Nw5AivU-Gv6S-YZgSmLQfQ8oVT78qcnIEu1JjuwEeevP1XYocOcuZvYuUS3pwzdRjTmA9y831sba996YCvTe8waeqqCS3UxVCVygB7RMaqQcXi7_qh6GzKE2xHP70COTCXiy360GpDqU6KgGKoYpvX7yDASSV5Q02nOTu1hmlJJHFSWfBZ6NZpegTpdDzbZV3s0UajRY1kJu4v3IjpP9v_tfdye8hl6iUqPOQ_WaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=WWlSFHiS6AM8WTGljRD7tMXGlkN6FQzVaCJItk8EpE0SBPvur-o3rdCuuJ9F3JLloTKLO7MhTXgBZfZAYFrokSDrKSwi0T-Jy1eN-vzqhyztHKhMdpP4b1PIoBMGsRRo2d8ouJGVyKigoE5VlmPo7r-VLtWOzDU40k_7dZsvAMu1zEtPK5brM_x3-3HVj9coHg2cBctKjThMgDxRdvEkVTEooHut1i7c25fyqnuGHjRiL4-VZuK4vftC-QCbo7-ujJKU9GqNicHooCCh4tzfX4jnHF7K7hdjvwMzbQL_j2f3tQ_OzCZPUzYMInJCvBSpEJxg4T9tb-BzT9vr3lznIDnPp-dggRC1GV0bFp8T6RCpjhNXDoFGYB0XB_KcoMTXTLREjAPn0isgxoeU2PUFRZvhucNGRaLDrZoK0WzaSGPcC9rM-0kdO2Lr0_vyqWBzC9Nw5AivU-Gv6S-YZgSmLQfQ8oVT78qcnIEu1JjuwEeevP1XYocOcuZvYuUS3pwzdRjTmA9y831sba996YCvTe8waeqqCS3UxVCVygB7RMaqQcXi7_qh6GzKE2xHP70COTCXiy360GpDqU6KgGKoYpvX7yDASSV5Q02nOTu1hmlJJHFSWfBZ6NZpegTpdDzbZV3s0UajRY1kJu4v3IjpP9v_tfdye8hl6iUqPOQ_WaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=bzUGYI1AazyYiBjXtVnP4M_a_BNnvJA68t-NUv3L8a5ZV9UJOXxZEz6rBxWdh0YybzyY4SOYJmlDA-1WYjKoylVHa5Tv7C9q8b1mNisogtPU3CmPZ35tIXwi9Aurh98HknlL2RYTeVforcWk46V-Mj2oSZL6M3hPsORn91nkJbMVDBPjyyQVweCmxkKMWecIAc2a8WmrsgK3599IFRX0rPeMB2-JF0_UiLT2jFIy0LPN4WXYtS5CEYsz0G7L5LX8xLS4hv-DOGI6Ri9zRjolyxrn-2rjQxda1bBUf1nWj9F9VBDXGTo2YuB39bqRE_srj2vnsQF0uB82EI2M5OVWAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=bzUGYI1AazyYiBjXtVnP4M_a_BNnvJA68t-NUv3L8a5ZV9UJOXxZEz6rBxWdh0YybzyY4SOYJmlDA-1WYjKoylVHa5Tv7C9q8b1mNisogtPU3CmPZ35tIXwi9Aurh98HknlL2RYTeVforcWk46V-Mj2oSZL6M3hPsORn91nkJbMVDBPjyyQVweCmxkKMWecIAc2a8WmrsgK3599IFRX0rPeMB2-JF0_UiLT2jFIy0LPN4WXYtS5CEYsz0G7L5LX8xLS4hv-DOGI6Ri9zRjolyxrn-2rjQxda1bBUf1nWj9F9VBDXGTo2YuB39bqRE_srj2vnsQF0uB82EI2M5OVWAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=vR1zQDzhpSx3iBi_tGuMVRlqkO2RIPvd3tR-wwpUp2TlvV-MwGjouz5EQf4Tnu1mrwqc2biKcp5JiXxi_Z5OY3ezD16XTyD_JdLhK4f4dOeSkcYvIN6hmR-TanI5j94z89T_ldjjoMPrKsaYQcGxKs4LmpwVOsffCYC7OlDUxnfod0ieV2GKlIrrzyJwT-ZFCXy84CtnzGerNnXsS1yVK2azaYV5DWXAbXw8yoZ-3w6FhXGze50-cZD8LFAoa-cQ0sjbUfT-0IsHpGpiZ5ISgPKqAMvZRMDdeUdx3X6QaffgAyMQWRX7sAPicoeQCzb3nEyvd3naSsBiRpkhK1Tz9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=vR1zQDzhpSx3iBi_tGuMVRlqkO2RIPvd3tR-wwpUp2TlvV-MwGjouz5EQf4Tnu1mrwqc2biKcp5JiXxi_Z5OY3ezD16XTyD_JdLhK4f4dOeSkcYvIN6hmR-TanI5j94z89T_ldjjoMPrKsaYQcGxKs4LmpwVOsffCYC7OlDUxnfod0ieV2GKlIrrzyJwT-ZFCXy84CtnzGerNnXsS1yVK2azaYV5DWXAbXw8yoZ-3w6FhXGze50-cZD8LFAoa-cQ0sjbUfT-0IsHpGpiZ5ISgPKqAMvZRMDdeUdx3X6QaffgAyMQWRX7sAPicoeQCzb3nEyvd3naSsBiRpkhK1Tz9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=WGcrUsnmX3GmJyL5X3dmtApNnPvVF336Nwz868-BzOBf80SMESFZFoWnwgX41reEq8FouA9BeHuvX_12twevhXfat6-oaS1Q5bQEyeMgQD0hE6mbBajB0PaBj_n08_wkhD2wIE89l1QkgNMECa46kODNtn0xIksoFpasFFp4d2DAcpAUAeKCD1R6OrgADA9WCcZPhSNFyG4PWTt-6cfJpj9_-K5UEwOsHiVKxE3XkFRgxkTlI8A27mb1e9cwffnNH0aZRRDYer8CDvJ_UL8SNFOtRammQ25U0pydCly98WvY92NnPUdiigcjNWGq8yI85IDT-AK7g0SBkUgUv3Y8QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=WGcrUsnmX3GmJyL5X3dmtApNnPvVF336Nwz868-BzOBf80SMESFZFoWnwgX41reEq8FouA9BeHuvX_12twevhXfat6-oaS1Q5bQEyeMgQD0hE6mbBajB0PaBj_n08_wkhD2wIE89l1QkgNMECa46kODNtn0xIksoFpasFFp4d2DAcpAUAeKCD1R6OrgADA9WCcZPhSNFyG4PWTt-6cfJpj9_-K5UEwOsHiVKxE3XkFRgxkTlI8A27mb1e9cwffnNH0aZRRDYer8CDvJ_UL8SNFOtRammQ25U0pydCly98WvY92NnPUdiigcjNWGq8yI85IDT-AK7g0SBkUgUv3Y8QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=C-yufJ6LB17RDA2-Zi82BC4MUupmhsx4L3sFgIZ17QHI5LErg1AweWCWhlLVXa6b6tdcDSbt8yaEJjKbJhn7TlRfi4yLQGZdRU2RjXXLEMchdpdBXY1nmnamhQGbQ8KkBJiWxBc5hRP-wvyMNzvoC7qi0lDVMRQT6QBZW3GnvQDx_ZtgzN1nux2EukpbJvmqhXekUgQueBxBRve9HKYw7kjHB4jo_JhK9HNghy5wlJTlOZdCpqLfFQ34eF0DacTNv-Zn4Hs16LLwo4_9VnqmL9X687WCwBNR5nSOCyeqPgiKLg9YucLe_FlSKH2E1CM8M-EL0PNgmVJX7N4QDon6VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=C-yufJ6LB17RDA2-Zi82BC4MUupmhsx4L3sFgIZ17QHI5LErg1AweWCWhlLVXa6b6tdcDSbt8yaEJjKbJhn7TlRfi4yLQGZdRU2RjXXLEMchdpdBXY1nmnamhQGbQ8KkBJiWxBc5hRP-wvyMNzvoC7qi0lDVMRQT6QBZW3GnvQDx_ZtgzN1nux2EukpbJvmqhXekUgQueBxBRve9HKYw7kjHB4jo_JhK9HNghy5wlJTlOZdCpqLfFQ34eF0DacTNv-Zn4Hs16LLwo4_9VnqmL9X687WCwBNR5nSOCyeqPgiKLg9YucLe_FlSKH2E1CM8M-EL0PNgmVJX7N4QDon6VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کریس رایت وزیر انرژی آمریکا: آلبرت اینشتن ۱۲۰ سال پیش مقاله ای منتشر کرد که...
🔴
ترامپ: برای هیچ کس اهمیت نداره
😂
🔴
کریس رایت: به نکته خوبی اشاره کردین قربان
.
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=YdzeYd2K931XWG8ec7UeBCFeiv1C_FqiwhVsb_4RYseXeJ9Rhx_Px-_fRUOnaJYoh81J9_OkhjATti7Zb3EpZHlMqiCal8TK3WO4XQV9jjUklkmGV6aIfRegbxPI4PMrYvTuLWoWUHJiT1HHrJ15K7l4WSEaPwZTqkSJO3CGue5NULBXTkW1PLR9A5DjvimyYnH8Hlf1hc81ghUJTeBwO7ZyxQa-tJ-4FzyX6bO-OcgmEocY7J_dlKKSU4qBaTOxUQZMt2JBi6PHecQhjaVWvpwgI8R1RTVsDJ6UO6U5SDavADuuF3kHbfuEeIO6G4WzwZ985T0CfxXqFpkkKF7eqG5sFs8y4MUzhWO_IddT2FJbLR-Iassv3urxLE4OD-KG9zkV1LFlefKX_93qDDnrQMelqJyVI06YIvOUkIGYRhrKnqqHAEJ989vxvWv4pGJIL4KEyjr6Y5_8oZMYn_gCGAuu5VkZ94slmq_QVWU03o8LOQHJlYVWIUjLvhxQe_wtNGvKFRX9hAED_M9G_vjV_pB-WzhWNeacGhvmyGWW2CaU0mjnKAcL_KFL1pulw5qbIUmaltnbQ8cvEAkzVIZFyt6x5esR6mXMKFClj_DkFa5sGNBgoxhF7hTHikI2SZ8Z4EJYjO2hbwcnVJ_VZbQDn6Is3RCpAvq0xw1Ksd8YeY4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=YdzeYd2K931XWG8ec7UeBCFeiv1C_FqiwhVsb_4RYseXeJ9Rhx_Px-_fRUOnaJYoh81J9_OkhjATti7Zb3EpZHlMqiCal8TK3WO4XQV9jjUklkmGV6aIfRegbxPI4PMrYvTuLWoWUHJiT1HHrJ15K7l4WSEaPwZTqkSJO3CGue5NULBXTkW1PLR9A5DjvimyYnH8Hlf1hc81ghUJTeBwO7ZyxQa-tJ-4FzyX6bO-OcgmEocY7J_dlKKSU4qBaTOxUQZMt2JBi6PHecQhjaVWvpwgI8R1RTVsDJ6UO6U5SDavADuuF3kHbfuEeIO6G4WzwZ985T0CfxXqFpkkKF7eqG5sFs8y4MUzhWO_IddT2FJbLR-Iassv3urxLE4OD-KG9zkV1LFlefKX_93qDDnrQMelqJyVI06YIvOUkIGYRhrKnqqHAEJ989vxvWv4pGJIL4KEyjr6Y5_8oZMYn_gCGAuu5VkZ94slmq_QVWU03o8LOQHJlYVWIUjLvhxQe_wtNGvKFRX9hAED_M9G_vjV_pB-WzhWNeacGhvmyGWW2CaU0mjnKAcL_KFL1pulw5qbIUmaltnbQ8cvEAkzVIZFyt6x5esR6mXMKFClj_DkFa5sGNBgoxhF7hTHikI2SZ8Z4EJYjO2hbwcnVJ_VZbQDn6Is3RCpAvq0xw1Ksd8YeY4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
دیروز یه لحظه بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما هم دست ندادید و بعدش رفت. آیا احساس کردید که به شما بی‌احترامی شده؟
🔴
جی دی ونس :
نه... باور کن، من چند ماه اخیر رو خیلی با ایرانی‌ها سر و کار داشتم. بعضی وقت‌ها واقعا برام گیج‌کننده‌ان به عنوان مذاکره‌کننده
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=vWq99WNg0PF8ymFNq9ATsrAZZWIKTNp1fA-ax14-DuP8SmHMSgBICrXq7ffOGKbS6PG_RXC4683SScEEBpO8PVPqVOIgh3iryRbKA3DjCHdfMd68OQwtywilBAmDDVfKkyO3HrdcRj6xTYftoyNXSCTBQZnJBxU1I7mdae6kBwQuSI1wjZzwL6Em45hoigSN-2GUk0WakHulNO8LygKIw5XmkIuclBa2ATLU2sOQLwSkGhoEVRqfg1tioIRqIBbyrFv2O_Mq57IHkXYQKQHE0XJtowDEAMUFFqQ8Z-GIohnp8fgj_JLN-tIE151dyUzFNJwpecVu23U1Trn8JnWQDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=vWq99WNg0PF8ymFNq9ATsrAZZWIKTNp1fA-ax14-DuP8SmHMSgBICrXq7ffOGKbS6PG_RXC4683SScEEBpO8PVPqVOIgh3iryRbKA3DjCHdfMd68OQwtywilBAmDDVfKkyO3HrdcRj6xTYftoyNXSCTBQZnJBxU1I7mdae6kBwQuSI1wjZzwL6Em45hoigSN-2GUk0WakHulNO8LygKIw5XmkIuclBa2ATLU2sOQLwSkGhoEVRqfg1tioIRqIBbyrFv2O_Mq57IHkXYQKQHE0XJtowDEAMUFFqQ8Z-GIohnp8fgj_JLN-tIE151dyUzFNJwpecVu23U1Trn8JnWQDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شهبازی، مجری مفعول صداوسیما:
طبق تفاهم جمهوری اسلامی و آمریکا؛ از این به بعد شعار «مرگ بر آمریکا» ممنوعه و اگر کسی اینکار رو بکنه دستگیر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=sZiGPc9UCwX23SUek_QzelhHvFFmd7V1tGxK6p1uYEjTMU0mf1hvPpEEEwnl3shQoikG_JwO19on2zWNDwn5zdtiBZ9wshBlPX1Idat-NQv4lo0yJ8hqSLl5RPuYw3nR8F3jo4ZRHEU8EFsJgVjMzleKkeKwx1sC0IY9lwJvIDlNTQ6DE6J-FAJLuQF8Lg9V7bSIs53Pkh9_0kBpHxSh9Y2kS9lUWoE-_PzwBCeM5hbxepUKt7sRIeukWbosl_A8qjE8FIIUDy0_YH0B5eHKYYhGuKdiBa6cRu-4gKP9BYM6tEST7xP4XzP_GI7oJRmFX5u6l_gmnozepqwG4PmTJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=sZiGPc9UCwX23SUek_QzelhHvFFmd7V1tGxK6p1uYEjTMU0mf1hvPpEEEwnl3shQoikG_JwO19on2zWNDwn5zdtiBZ9wshBlPX1Idat-NQv4lo0yJ8hqSLl5RPuYw3nR8F3jo4ZRHEU8EFsJgVjMzleKkeKwx1sC0IY9lwJvIDlNTQ6DE6J-FAJLuQF8Lg9V7bSIs53Pkh9_0kBpHxSh9Y2kS9lUWoE-_PzwBCeM5hbxepUKt7sRIeukWbosl_A8qjE8FIIUDy0_YH0B5eHKYYhGuKdiBa6cRu-4gKP9BYM6tEST7xP4XzP_GI7oJRmFX5u6l_gmnozepqwG4PmTJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fwT7JAUEGYln7HmkBuzF3m1vnqa7RC9QEalsLOeyD_4-0y7X9HAUDpJcJvULz-CnwK1Ny06Zt7BhFILbtyELrzJb-eYT6qELHwxpc1ypEtVccSPe_XiM6C1_estAYRButP8h0bTwdJjTM2R21izi0yxrVDR_441SxdNAqkxxYvXUOmoTau3N7GhFd2W2j8mKWxk8DkQ3PZbLbzimb_HaahFiSdr6tTZNZr-TCEc38jKDzBpruq_pt2_ZX4B4OanrskssHEQQDLcljUfvIRCFK2HVJx8IVbxJB5QJcMXYcxjQUMXYMmlaVT-Ln2V2VLK8MfZvls6gDh237jrqSOl2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=kMfTCXxEjswPRVCkAxMxLNH9wAn5qbsnO-QEycdEi74Df95xv_IQFImR0SC_2R5d4fGhCZxqa25PghP3dZXyZFiFyKvIe_GMmo1bz4Sn_ZAuavIetvIkzW6JO6l5YB5bOjAhnBiS-CHJoLhfA5t97ZoLcuQfG8EN2cBd7iW1sayQSw9T8W9EPjeODJKzin8zvDRy-kO4ERHSFzsBCSNTOvRPO2B3ykabqFUN6m76k2YVvhvQpHDObj6K4iOvFAYG0z8pjEGGGsWdVEL3UZ578hOJx4p6UPIZR2AXmSThJCPzVXmCP3y2BS8eO-m3oxVMRrLYFV9Pkd7cfKxpAhllPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=kMfTCXxEjswPRVCkAxMxLNH9wAn5qbsnO-QEycdEi74Df95xv_IQFImR0SC_2R5d4fGhCZxqa25PghP3dZXyZFiFyKvIe_GMmo1bz4Sn_ZAuavIetvIkzW6JO6l5YB5bOjAhnBiS-CHJoLhfA5t97ZoLcuQfG8EN2cBd7iW1sayQSw9T8W9EPjeODJKzin8zvDRy-kO4ERHSFzsBCSNTOvRPO2B3ykabqFUN6m76k2YVvhvQpHDObj6K4iOvFAYG0z8pjEGGGsWdVEL3UZ578hOJx4p6UPIZR2AXmSThJCPzVXmCP3y2BS8eO-m3oxVMRrLYFV9Pkd7cfKxpAhllPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=dO0pgujsNwzV643KQ7T5AiBvIwnKLw6iY03Gp2NEL9vcItHrAuh_J5q0_beliYHPVa51QmQ2f88xAvmM2A0YNoLgPXcnt2iby7nLWgiSQBnxdnWGt6efgVwUtfoGpjGGxbl-KKDujwkhBnu0efNBYv5pYIbKXuGHAT7BhdJxo_YGO7xR0Qus81vVfpIC2RxbyUnJEf6vRr0IfZ66zA8fCx2vMGWayp5TeDqKEISLTUIRAtumCvBmELAzXdunhv3zhrLRPOgYrE2inSW2B9MnVmhpEL_0qEKpH1Q9jq5_9Th8TdL77XSRl3lbKuhyW3SessrQOKOVhee7DcPS1q1PuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=dO0pgujsNwzV643KQ7T5AiBvIwnKLw6iY03Gp2NEL9vcItHrAuh_J5q0_beliYHPVa51QmQ2f88xAvmM2A0YNoLgPXcnt2iby7nLWgiSQBnxdnWGt6efgVwUtfoGpjGGxbl-KKDujwkhBnu0efNBYv5pYIbKXuGHAT7BhdJxo_YGO7xR0Qus81vVfpIC2RxbyUnJEf6vRr0IfZ66zA8fCx2vMGWayp5TeDqKEISLTUIRAtumCvBmELAzXdunhv3zhrLRPOgYrE2inSW2B9MnVmhpEL_0qEKpH1Q9jq5_9Th8TdL77XSRl3lbKuhyW3SessrQOKOVhee7DcPS1q1PuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: وزارت خزانه‌داری امروز تحریم‌های نفتی ایران را لغو کرد؟
ترامپ: خب، من باید دقیقاً وضعیت را بفهمم. تمام آن پول به صورت خرید مواد غذایی برمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند که نمی‌توانند آنها را سیر کنند.
خبرنگار: مطمئنی ایرانی‌ها از سود حاصل از فروش نفت برای بازسازی ارتش خود استفاده نمی‌کنند؟
ترامپ: قرار نیست آنها این کار را انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t070d5SC1HvKZVyQOhGLGKiQTgun157K6rJQTmaYUTKAu3K2k8GysalZd-dsJFAgDXTc5tp_ksutZNdmp8YbFOYzl6ImfUdEXLm0lU4SySFZhn4cJVaVjDDHCUsoBGg5BBQyNGnNceWfVOoFYHp5w3j-fZtcxmIesQJ3KXUqCqrlOK8fBVYqobxjMoAZ8uQoEtJjMlczRef_r9gbCI2fwEBSbFHgeN5iVFWTNYVVyRpn1J27PU6tDM_mRh8Jnyz88-3B0sC5eNfkwG__By-llPmapEeYilBE2d3y1ZkfAqu24ziWQL9XU5NeOpxewtpVvryNDrzDd6kTe-7KGtBKiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=IZIZs-pkwdcPKRyDXNqIKBO5Bw9HicJaQFwhOsr6yJ6VwtJINVjfF_X7e3Wz7oO2SSwTgSaQsW-CJPjJJR0-FoMo8wIKYgqHk_bfR7fdU2Ul8LLSMLOOkHptxUF4nM5RKq-bal0yXnuLhOeFozOmUIpJJVmvkGvZoQSC2UbucB5--wUvEjZ_G4K_4udha2fiavnDwCLqOVxQe_RNQOK81zBOGJpstxPUSwzrasKMBftzq60DAU8Je__zqMdbe4PzD5LrXiNOCWiVtGgTK0q6PNUZVTX3IueipqMzU7IH01S4YQ3Z6h-7s1UiXC4NW7b_oJmY-2wdZH5XnxHFNEozcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=IZIZs-pkwdcPKRyDXNqIKBO5Bw9HicJaQFwhOsr6yJ6VwtJINVjfF_X7e3Wz7oO2SSwTgSaQsW-CJPjJJR0-FoMo8wIKYgqHk_bfR7fdU2Ul8LLSMLOOkHptxUF4nM5RKq-bal0yXnuLhOeFozOmUIpJJVmvkGvZoQSC2UbucB5--wUvEjZ_G4K_4udha2fiavnDwCLqOVxQe_RNQOK81zBOGJpstxPUSwzrasKMBftzq60DAU8Je__zqMdbe4PzD5LrXiNOCWiVtGgTK0q6PNUZVTX3IueipqMzU7IH01S4YQ3Z6h-7s1UiXC4NW7b_oJmY-2wdZH5XnxHFNEozcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=MmxgzzrzBUICH-w5a3R-SYKdr85mxakjS-CmvbzekVgJGiGPs4d3ngzBvo2_xP4U6E4KNNkW9PnedRYn6K3314xNTH2c5UpZnCcgENcYVzhx26ZoJFbFao4ACH0UBChGQn1X9gL8pxEvc0ntPp3UYq3tNksRaMeKTHzs15zcI8U5sPVYZTaerIFwZfCw29QiPHJNDDONUYESEYxLYzuT3gVaJ88iIot5m_zwTDi0rKMc0xi7weTgCZ2Be_yogkS1ASwohBW9s7jlX3Pf-RBxpgH-NAzJ7wtC8dN9lcwhqPtcXNjimZNP0u4gURi-K25w9dwZMXfk34JnSYIZieemcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=MmxgzzrzBUICH-w5a3R-SYKdr85mxakjS-CmvbzekVgJGiGPs4d3ngzBvo2_xP4U6E4KNNkW9PnedRYn6K3314xNTH2c5UpZnCcgENcYVzhx26ZoJFbFao4ACH0UBChGQn1X9gL8pxEvc0ntPp3UYq3tNksRaMeKTHzs15zcI8U5sPVYZTaerIFwZfCw29QiPHJNDDONUYESEYxLYzuT3gVaJ88iIot5m_zwTDi0rKMc0xi7weTgCZ2Be_yogkS1ASwohBW9s7jlX3Pf-RBxpgH-NAzJ7wtC8dN9lcwhqPtcXNjimZNP0u4gURi-K25w9dwZMXfk34JnSYIZieemcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=AJyX0MopfCrqC5TTFlzrChfYYccbXkNXWHcj1FOsCvfANBQR6hIfEuV_cyLspqNWiLw1itro95INJa_wgfsiEagHY2rQyT4fzufzXSh6wpUPJLbAS39hfuA8Qlp8mpakXDENCYffU2UDi3Mu5IH3ZkTglNqp3r7PEA9QdGC07YvCOYxmc22m3zsrrcyE2h9YUz7QeKnNd6uzsyjUKFP8c2eAfZu79WSeH8M6VWMUnyPgl7Q3uZCKGlhOWmk6zSyQnFLIryI2meov4dikN6ZvLpcyR88zSOVQPMkDDKbsv3TDXn_KP7KjVPlwcpyn6ATfTlXrU_HLvMLjhLqP4JgF3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=AJyX0MopfCrqC5TTFlzrChfYYccbXkNXWHcj1FOsCvfANBQR6hIfEuV_cyLspqNWiLw1itro95INJa_wgfsiEagHY2rQyT4fzufzXSh6wpUPJLbAS39hfuA8Qlp8mpakXDENCYffU2UDi3Mu5IH3ZkTglNqp3r7PEA9QdGC07YvCOYxmc22m3zsrrcyE2h9YUz7QeKnNd6uzsyjUKFP8c2eAfZu79WSeH8M6VWMUnyPgl7Q3uZCKGlhOWmk6zSyQnFLIryI2meov4dikN6ZvLpcyR88zSOVQPMkDDKbsv3TDXn_KP7KjVPlwcpyn6ATfTlXrU_HLvMLjhLqP4JgF3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=RojfzAQcIfPLPvr_QbwKyK6q_8H1tHm0C21ZOY02yPwTz2b2ltBOpZdAKRNCeHpnZLeilxynb3qgHUaypCULcU8D_pz-sF69Nyoz39uHDUYQAKebo182dpX4ng2ex0QU5Xu18elbJt54_1KlF-tZzx2yexcvktj5nILEZC2qoXiE0JnRDWZsjs_6m5KMoDP0Q1GN3VpY_zXTOppA-oa_-g5bHKNNrofyQCle-jBFvvw6d47DYOXsCoj6scnSdq5hs3oXp0VLNHRplN9zudbB99x_l7XwWUxLEotyBj17zMUIZCPnnq0cZLwlwS1bWuMqP2BP9WiMvd8gVpSKEWj-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=RojfzAQcIfPLPvr_QbwKyK6q_8H1tHm0C21ZOY02yPwTz2b2ltBOpZdAKRNCeHpnZLeilxynb3qgHUaypCULcU8D_pz-sF69Nyoz39uHDUYQAKebo182dpX4ng2ex0QU5Xu18elbJt54_1KlF-tZzx2yexcvktj5nILEZC2qoXiE0JnRDWZsjs_6m5KMoDP0Q1GN3VpY_zXTOppA-oa_-g5bHKNNrofyQCle-jBFvvw6d47DYOXsCoj6scnSdq5hs3oXp0VLNHRplN9zudbB99x_l7XwWUxLEotyBj17zMUIZCPnnq0cZLwlwS1bWuMqP2BP9WiMvd8gVpSKEWj-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=Fn1aiYnDKieyKhdfgwaMQstynOg8jErORHANOG2N9gFu2oFKkZh2G2cKqTKEUlgwO4TEZkhMmlKmkpDZNFYDaimUCsMCpBsHo2nfQOp4UnbNMBV5HdZK9MaZNLxYBacJ2cNNFmiY1XEr08D1WGPaeHnS70XW8BF2Q_5zEnumnGWrm7VuCu0S7tITOX34GNohlYxjQGxGqMbdGMDaHz-YvylTN6FUF244KtXOk9yad_Pn06B0m-es1CF6gGXERHpBdJKiNtX7FIsmFjSRtI7rmY-9nIn7gHYzcfTrTJUgL88M4JXLG6eYG-qtM_B2pXOG3DguhGnhH9t07G7umJRo-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=Fn1aiYnDKieyKhdfgwaMQstynOg8jErORHANOG2N9gFu2oFKkZh2G2cKqTKEUlgwO4TEZkhMmlKmkpDZNFYDaimUCsMCpBsHo2nfQOp4UnbNMBV5HdZK9MaZNLxYBacJ2cNNFmiY1XEr08D1WGPaeHnS70XW8BF2Q_5zEnumnGWrm7VuCu0S7tITOX34GNohlYxjQGxGqMbdGMDaHz-YvylTN6FUF244KtXOk9yad_Pn06B0m-es1CF6gGXERHpBdJKiNtX7FIsmFjSRtI7rmY-9nIn7gHYzcfTrTJUgL88M4JXLG6eYG-qtM_B2pXOG3DguhGnhH9t07G7umJRo-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صداوسیما:
نه تنها از کشتی ها در این شصت روز عوارض نمیگیریم بلکه قراره آمریکایی ها بعد شصت روز بیان و عوارض بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bfif_DmBxYGj8r1DP9BNLdkfnuq06fE0Q7_4UaEG2J-n-dq_4_BHpgs7BE2m22Hssi-RPQrog1oOtKpNbyTbfEL7JvufJckcvdgXUwnItot6KpFnZf5xVf7f0dHcLZWTwODWQxJ33HMkuCpU2estucUAq7Vlwpad4Nr7ioy3WW6kDpehgP_jtJaAexkXQhFVb5xqNEKkZaxUv0JXlM580i2xmVNzyXCMIT343RBBhuRibCkxA23nB8oIncQ3o4xHULWxI53GmqT00o93zAB4b2jMsUKyWKzxT9D9UWlhPgHDn5uZsoKbg2SjynOWW4rmhaa9OZSMQm1y22RaCFyf8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMJYEGgVbCsX0bfRpbL55X7cI-Wtt8CNfbh326ZQJOWL5Xeem0YtRpeHTUYiMsFegEJ01W5CyMnL2_fj6EqCEuobpGKZOZkVZTmJFk9ccSr151fNYl7NRdbKbK1uZFUb4dESmV4oRK1Ccx4Ih3JUCCeD9Dg2cIlyFkxzJjsHdr_kQ42LBQdZunVQ_szkrLZlckRoAiBGKq4pioKz1llWGTi0DRys1DKl3xduX924M9enLYF-YtY2n8QhFSIkXAS6iiey65DYblaCgei0eUgmRd96TK_M8syJ1kE_aXNDqnwkYW3r0t_p4qG_1S0l4-hcDP6ihgCTUcBKrcB080p4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8AHo73C7wOuM6m75uV9erMHXy05Mir5ooPH88enVDONr5uTlmq6RLb_iJ9QTMbvvO2fivj5_wusjiI_m-4yMSs20u1QY81lXKhUa2DaskQI8V0FBXI9aVD-tELF8RO4w2zU7tagbGCngBBrkjgfAXb5dYNAnlrWnjVgEWQOhXKfl3_fq5AtLX_jkYg0lAEfd_nMbHMeCDFJbEEKS0vJmJLpFBJwQqlrXO4MOPWXw-1oqPCZ3ncdNgj0PIvEhxRyFSUlTIA-n_bjuNWykiFYVY2bXjk089kwt5bWvoa7y04uqCj4l4CpgRs2zbh3rXuqGUfS-LdWFmeyRPLLRasIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9dP8rZAzGfy7-8qS5XSeXkcP3CDZxv85ugODXgn_k1mwxc4KdCiXKnfX-sqe7BVh04xHgES6YPFI6prZcKEkxdUdPQzVkIrkNwEnRfhIwTSl1XoHdzX01ruly2cCzemkNOTpZAvp--nd5nK3G2lGX48TWj0_tvGrwxayAE0noAwCs02H2IRq8UBeO5XCkPRnzXSLxQOC7TmYrW28e0IaJAaKUscXBww4CtgI9tlbD6P3M_-p3nvi15GEUp1288LF9cfxxzgiOMDlBVmFhZDsH669VjfImlhIof_kWYDTYQ9TG0D7ObvOMZP2cGUAxVTAEmJXR6UJElZYe5OeWZebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWlJXXlJi7YP5wpWAPgpiSROFrY2jdpva2HL8Pakor6Qm-Vk6Ebj39ArlwmxXmaduUP0ttSH40z7T03ozsj2E2-3aMAMAa89dvXg_vnmy067MCBjZ1_aoYX4yhOxIkrJUiU_FvCigVACaS05N6-FkwtIngmE_sQW3cstUxvpiVN-iBx_b-YQ1SQ9fg8UmrgzmL0HvKgOymRR_Q-e92Gd59QeMbCKqfaxi-JQ6eV98z2QNe1nWdynjLX6JPcNNwF0jKqhi4cytRgNuYMN_nzylcgJL4yhawQWhID50J_h260wXZkn_-_U6e9cx1WGD8Craz0RCACaaLF7DIug4oT3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMg_4dUgNrv39XIxktOBK4SCHHrRgTv7vCN-GdDOlT-NWSIwHvDic3B7to5CDGGJV7slL5oslRYrMTJn1m-ZAQyxtxgQAL64tCXESl-yD0y6bYeZqVgeYszzL72mNbQFH0zfCHXZYsn2DIOsMe_BRkhyKCOiCj4S8X78gzLryxO1XZY6T0aZonWU0WHHIPse1IXSQvBakWuKoSnWGVS_LlUDTi2_WFuC53sJBJGiLeNgMVxR9wbdCncptIt6W_h8E9GFnpajMvoAWPzB6aTBnHRVJCB_7tvASI4Q4CzC3FrpkjqjkX41-7l2To1QHFYBlrPICCLOtQu0ddd0U0HFG_No" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMg_4dUgNrv39XIxktOBK4SCHHrRgTv7vCN-GdDOlT-NWSIwHvDic3B7to5CDGGJV7slL5oslRYrMTJn1m-ZAQyxtxgQAL64tCXESl-yD0y6bYeZqVgeYszzL72mNbQFH0zfCHXZYsn2DIOsMe_BRkhyKCOiCj4S8X78gzLryxO1XZY6T0aZonWU0WHHIPse1IXSQvBakWuKoSnWGVS_LlUDTi2_WFuC53sJBJGiLeNgMVxR9wbdCncptIt6W_h8E9GFnpajMvoAWPzB6aTBnHRVJCB_7tvASI4Q4CzC3FrpkjqjkX41-7l2To1QHFYBlrPICCLOtQu0ddd0U0HFG_No" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=TUF3ALBWCDUgKRvQTPehBb_qwXDmdWc_6keuBpNKX7LdwlvyJe_RpFv1a-SJ0P9NDKR9RQ6fXgLty8vR9TIipCe26umIOOVBdiONRu4BgScNKkq2mrW5Mn1dIs9LiSjDW2m1hq92Wz0PLLsibGqjzfMeRWH1xeZaAepsvJ2Yz2yEIIsl95YjT0_ZavI73UpILFsDqpMJ21YKxkLVFpjwcjJDUX45mYGEyoYnvH8Quinb3nXOFtVI6ZT-_dqusRYm3m0hdUEb4dtSWmlRRVDwABCgR_GTwty9ifUT-lvji5obPFiSl33odwH4P-em9CQIeupMo8UOrJCWG2Bire5yuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=TUF3ALBWCDUgKRvQTPehBb_qwXDmdWc_6keuBpNKX7LdwlvyJe_RpFv1a-SJ0P9NDKR9RQ6fXgLty8vR9TIipCe26umIOOVBdiONRu4BgScNKkq2mrW5Mn1dIs9LiSjDW2m1hq92Wz0PLLsibGqjzfMeRWH1xeZaAepsvJ2Yz2yEIIsl95YjT0_ZavI73UpILFsDqpMJ21YKxkLVFpjwcjJDUX45mYGEyoYnvH8Quinb3nXOFtVI6ZT-_dqusRYm3m0hdUEb4dtSWmlRRVDwABCgR_GTwty9ifUT-lvji5obPFiSl33odwH4P-em9CQIeupMo8UOrJCWG2Bire5yuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=IfCWnbcQ5uoDIId9j2isEqYNeiDKPk8KGKVrNx8qbm3e5xaAJKV05yfDIzZvQFKzJESLSuna_t9TYW6zFBl9HRtGG4WdQVOPJVNAB_Jsj3-o4tSGQTl5gNs1qPmLigpuHmzDPxaSfnf4Ez7WsVCzaCm3n0f8YR0xl4E2pCNfE_-nIqbtR-mBmnZCOGUV44lp6Z6YQDfA1SMo3OfwBoGdkw-J-d6J6h-4-HtzwqbCdtVbo5dNsY0FiBuYlj8Ll1dHxZ7KTWe5n66hgPuo7GrpXiL9dLjVgGDKegh4mH3eztvj6MoynpjaqH3cal8YhB7C_flAxNcjjP8E9TFK8Ej8_oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=IfCWnbcQ5uoDIId9j2isEqYNeiDKPk8KGKVrNx8qbm3e5xaAJKV05yfDIzZvQFKzJESLSuna_t9TYW6zFBl9HRtGG4WdQVOPJVNAB_Jsj3-o4tSGQTl5gNs1qPmLigpuHmzDPxaSfnf4Ez7WsVCzaCm3n0f8YR0xl4E2pCNfE_-nIqbtR-mBmnZCOGUV44lp6Z6YQDfA1SMo3OfwBoGdkw-J-d6J6h-4-HtzwqbCdtVbo5dNsY0FiBuYlj8Ll1dHxZ7KTWe5n66hgPuo7GrpXiL9dLjVgGDKegh4mH3eztvj6MoynpjaqH3cal8YhB7C_flAxNcjjP8E9TFK8Ej8_oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=v6DdsLfx2clbegb4eiUZgaKWB8pkk3Z_Xc-hlXGJQoUN2niIugVUnnDCzZFyGY-lG098EPWJQYrO8IUmDmqp3pZtDAeeuJ2RYbxpBAXhi-il5GfTtgnOBN9fa2hArcaINBEVoxl2x-0wn71HLPpPXEIy71nqsk8u8vzDc3mDUBFDlbT6DwRnCsJoSf9b4zb0dweFQlDHBH-an6Sv-MB5-phjf8UYu2DpubSTS6km9T9YstL1hDRt-nPhwS0xjuXyI7G7mU0MaaRUIukItopq2NetM733rj0u201C3N-ofrJdNyfntjJfN5RYvfQaLynnXpJ463Z6GnTEafEabuMJSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=v6DdsLfx2clbegb4eiUZgaKWB8pkk3Z_Xc-hlXGJQoUN2niIugVUnnDCzZFyGY-lG098EPWJQYrO8IUmDmqp3pZtDAeeuJ2RYbxpBAXhi-il5GfTtgnOBN9fa2hArcaINBEVoxl2x-0wn71HLPpPXEIy71nqsk8u8vzDc3mDUBFDlbT6DwRnCsJoSf9b4zb0dweFQlDHBH-an6Sv-MB5-phjf8UYu2DpubSTS6km9T9YstL1hDRt-nPhwS0xjuXyI7G7mU0MaaRUIukItopq2NetM733rj0u201C3N-ofrJdNyfntjJfN5RYvfQaLynnXpJ463Z6GnTEafEabuMJSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnQOdNVSd8-HO52K1ij4rBI3GkiLww9SSwEmoO9R4gw-Fr1ljtz0jJM2QLhYvqbnovFJxvpuCp3wgsK2dbcfsxLTLyw4s9tASeO5rkBabeR-M9EqyPsMfUCgFItajEEd8DFyNUItyK48pnY-3-_5665v5nJ-X0wnuidgnoWSkbqJphuaBC05Vml_BoHHqOyawAHpByqp6jDKv2WP7L_LVibb6WtEdd2zBNQeugu8F7VGPFs0UqL34IXJxoAuXYb2rFb_zPlvPvWO0mDWMJ1eZxNAQ_rYpqtRdwilSzoDkIX8aXqP1TXXg4UkCck_ufebD8K79Ulndh3D7jFX2VbSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=ltvsy6m0sbW-2qfEE9UY1OKd8Yh7OCLeEUGqQURnRZQKZEYKSXB3kgZfxV8PgonwsTMtnVNdkmZ5TNIEgPhA_WRjQG7c8smGNj8tf6cuJTQagDr0ba1oPjSE0JW1dXJh7uRUXj5IcLe_mz8oT4UXslp_Wi9I2HmMelZaY6XcxcTq_mDHVjzU6n0o-mfitOdtjcJtA8DxlB3JoWiYPfhtn6Ol47znDlyuxFbQnwqRfWqQTW80ohGCPD3pPX0-b4b4q5zHz3mOH2LjmmbVSCiJRqKsuBi4YaeVJpHGGh0242rAvhnxTGWZAEbTO6z8gfrTLymhDcXmBE1OKxtMZ0N_0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=ltvsy6m0sbW-2qfEE9UY1OKd8Yh7OCLeEUGqQURnRZQKZEYKSXB3kgZfxV8PgonwsTMtnVNdkmZ5TNIEgPhA_WRjQG7c8smGNj8tf6cuJTQagDr0ba1oPjSE0JW1dXJh7uRUXj5IcLe_mz8oT4UXslp_Wi9I2HmMelZaY6XcxcTq_mDHVjzU6n0o-mfitOdtjcJtA8DxlB3JoWiYPfhtn6Ol47znDlyuxFbQnwqRfWqQTW80ohGCPD3pPX0-b4b4q5zHz3mOH2LjmmbVSCiJRqKsuBi4YaeVJpHGGh0242rAvhnxTGWZAEbTO6z8gfrTLymhDcXmBE1OKxtMZ0N_0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=dP1N1gOSFmt2B1-GFa0h2HSnOxLH6XldTV6CG4aNXN_lDpJF9IORmTO2vel5srSflAlL6UJcn348lRV0q8LyOw_1d310MH1Z7oGGZycYRXQZu6WpDoYOodl8crAe12N8vWM5FR4pZnnJPDR506jSaWjm66LzYWCn-74JoB_4VV8kJi1H2BwearCq4z7r-wHQGY7mwTy3rBo6a3_Eg4_94A7TidloypzWB0lwy_5RypvSdNyViSNDO_kZJ-X5yOSQw3T-6G6M4Hq1CW2idNujuNfE6Sp6wVFwhWk3M6KyMrkRUuSEzuldasnl_LnpmFDVPGr8tS8tofNJIbs5YmJzyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=dP1N1gOSFmt2B1-GFa0h2HSnOxLH6XldTV6CG4aNXN_lDpJF9IORmTO2vel5srSflAlL6UJcn348lRV0q8LyOw_1d310MH1Z7oGGZycYRXQZu6WpDoYOodl8crAe12N8vWM5FR4pZnnJPDR506jSaWjm66LzYWCn-74JoB_4VV8kJi1H2BwearCq4z7r-wHQGY7mwTy3rBo6a3_Eg4_94A7TidloypzWB0lwy_5RypvSdNyViSNDO_kZJ-X5yOSQw3T-6G6M4Hq1CW2idNujuNfE6Sp6wVFwhWk3M6KyMrkRUuSEzuldasnl_LnpmFDVPGr8tS8tofNJIbs5YmJzyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=fr_2nUdv_kdHiJM_p1POGEIIsDy9jUsnzHlRRkR8oMGY_n-qJhJPkOsSIpizSmLZsTGSzxmM62OH_KwqkftobyK8P-xVIU6EM_9-EzP_tNXYsllvzpL5kXKPJm-vRWea7fBq1A72-zXUZ2S9AnfhDIko-QT-_WvfVj-dTLOd6ljwsYn04-O_h8xdIdCyvHIjrYqtpsS_08NQnDewY0V-Sn5p9CNgt1TsV5kQOvAe0CxVpK63iBMA355bloUrcBUDM7ILqTFiSLF2Y18Iq-dupRb7dCJUjpBp1FT1qNAc1Ywyqz5cWTjK2WZkOtyI9b0ZFBHumujd9hM7DamVd0UIcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=fr_2nUdv_kdHiJM_p1POGEIIsDy9jUsnzHlRRkR8oMGY_n-qJhJPkOsSIpizSmLZsTGSzxmM62OH_KwqkftobyK8P-xVIU6EM_9-EzP_tNXYsllvzpL5kXKPJm-vRWea7fBq1A72-zXUZ2S9AnfhDIko-QT-_WvfVj-dTLOd6ljwsYn04-O_h8xdIdCyvHIjrYqtpsS_08NQnDewY0V-Sn5p9CNgt1TsV5kQOvAe0CxVpK63iBMA355bloUrcBUDM7ILqTFiSLF2Y18Iq-dupRb7dCJUjpBp1FT1qNAc1Ywyqz5cWTjK2WZkOtyI9b0ZFBHumujd9hM7DamVd0UIcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=ob_SlPPYhYNJm6SplyEYsCqAcF2-T9SSUyASDmh8Rnsbz5wKseKX7SWxjJy6kbhU33E9WQgz0z23ImLKm8eeZusqItMKNMtpCHmz6V4VvpRTNwyzkCVgK-bXLf56GVre4yJ2ySZXBfxpOR46uDdXVg-1LVXdF9Chxz-UrBph9Q0Lpw2iKVsXD8XpRdzVhy2yMB_BXjbOvfgfxpichf4l7ss4GiMYazwJCZNobXtJd4pqtuXbdFwYuI_y9XOFkhfx-yixIlxctNRdIM_uD6TJb6PMmohpUdUEwB6xTKvAd0kESJym74vCglxSWWKbfL7l5S5sLfjAliH8liBh-UkegQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=ob_SlPPYhYNJm6SplyEYsCqAcF2-T9SSUyASDmh8Rnsbz5wKseKX7SWxjJy6kbhU33E9WQgz0z23ImLKm8eeZusqItMKNMtpCHmz6V4VvpRTNwyzkCVgK-bXLf56GVre4yJ2ySZXBfxpOR46uDdXVg-1LVXdF9Chxz-UrBph9Q0Lpw2iKVsXD8XpRdzVhy2yMB_BXjbOvfgfxpichf4l7ss4GiMYazwJCZNobXtJd4pqtuXbdFwYuI_y9XOFkhfx-yixIlxctNRdIM_uD6TJb6PMmohpUdUEwB6xTKvAd0kESJym74vCglxSWWKbfL7l5S5sLfjAliH8liBh-UkegQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=EtAymMK1L3zJBNo5yJJ2eoa-LOgBqpquzUwKM0ete8UJWjtXt-5zq2jGLXquV6i0x8G0H0uiPtxh5q37nibcYe1JJIbNGqCe7zLcEgxDaCqmvCLemHoOfBLgAo9WC7ktra-arIv6a7ecEnzLvd1y-n_6kmSZZme_Wwh1nseb54LeMVmaz0gNcJmPQol8c7j8xA7X6rfEZNoq47Bc65G3E8ImDhfr-sGziWFwBq3GyjeL7EiIuc2UQzrnrYxkSzg84iaEbsGz7mnYpa_oaIw39sz_05k7nfV8mh7ubO3huorEtuAwRZx-PUtPz8ArnrWZSkj65a_2HkoxqEDZRuqvCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=EtAymMK1L3zJBNo5yJJ2eoa-LOgBqpquzUwKM0ete8UJWjtXt-5zq2jGLXquV6i0x8G0H0uiPtxh5q37nibcYe1JJIbNGqCe7zLcEgxDaCqmvCLemHoOfBLgAo9WC7ktra-arIv6a7ecEnzLvd1y-n_6kmSZZme_Wwh1nseb54LeMVmaz0gNcJmPQol8c7j8xA7X6rfEZNoq47Bc65G3E8ImDhfr-sGziWFwBq3GyjeL7EiIuc2UQzrnrYxkSzg84iaEbsGz7mnYpa_oaIw39sz_05k7nfV8mh7ubO3huorEtuAwRZx-PUtPz8ArnrWZSkj65a_2HkoxqEDZRuqvCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=q6UzFWAueqSJsX1Z4EwPbHThqmtARPbYkgiCtj2LYVAJ-js4-p54TzEbu0zwMrEQnUk6-P5aW8bB5fLZhCWXML1M8n6hEKplaKog28FrIepW1tiz5wYnt4ShEHYrf3nEKvgFj5t6pdV43E7Gu0Zw4g6bNDw1mxg63QWTeBz3FrgqAz8ayhbejPgH4M3c4fKMau1U4gw2CTny-cNWfcxOJD5dOpM35pwqMvABH8UfMDStQYc2eMY-DHYDDIMXNtDytk924BdfBqpsLQn_nVu8BtWSDV0oCA2T-UXCaOvXwgAbKc-bQPynSE96A5PDvjHmjk6cSYRTsmNgd1_O9isu6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=q6UzFWAueqSJsX1Z4EwPbHThqmtARPbYkgiCtj2LYVAJ-js4-p54TzEbu0zwMrEQnUk6-P5aW8bB5fLZhCWXML1M8n6hEKplaKog28FrIepW1tiz5wYnt4ShEHYrf3nEKvgFj5t6pdV43E7Gu0Zw4g6bNDw1mxg63QWTeBz3FrgqAz8ayhbejPgH4M3c4fKMau1U4gw2CTny-cNWfcxOJD5dOpM35pwqMvABH8UfMDStQYc2eMY-DHYDDIMXNtDytk924BdfBqpsLQn_nVu8BtWSDV0oCA2T-UXCaOvXwgAbKc-bQPynSE96A5PDvjHmjk6cSYRTsmNgd1_O9isu6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس:
ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کنند.
همچنین دارایی های مسدود شده ایران آزاد نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66680" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66679">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی دی ونس:
من نمی‌توانم 60 روز آینده اینجا بمانم. به ایالات متحده برمی‌گردم.
تیم‌های فنی مشغول به کار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66679" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66678">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=rcB19ADtMmKymmtzT75v5y77DsLksmGElmv7taUcyLhbUV8iAZ33r8w43IaDJ0QcMYT7pq_EPuMl4SWeR7Jai5r2S90c_DGTo1eCcGzuwzjkArpWwJzzlIB3EuLSNWl72UY18AKEiAEeW2M3LZZDb2SCYTZ_-J9aZ6U13qWjxSV2A2zdDLyq8k5x6sAitOIjO0JlM1goLYOpFZGxi5hfiClT0Z8d1mMqHtq8D3Fdw9vnF25Rt8rtjmUaCEqWCWL91YsFGiLTMl5AoTsSb9sebA8vwGv-CuumVcaFFpOwxZ7XkC9lcMW-5NRNSVPICuWgQNc44fETm2O4Zm-3kxzigQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=rcB19ADtMmKymmtzT75v5y77DsLksmGElmv7taUcyLhbUV8iAZ33r8w43IaDJ0QcMYT7pq_EPuMl4SWeR7Jai5r2S90c_DGTo1eCcGzuwzjkArpWwJzzlIB3EuLSNWl72UY18AKEiAEeW2M3LZZDb2SCYTZ_-J9aZ6U13qWjxSV2A2zdDLyq8k5x6sAitOIjO0JlM1goLYOpFZGxi5hfiClT0Z8d1mMqHtq8D3Fdw9vnF25Rt8rtjmUaCEqWCWL91YsFGiLTMl5AoTsSb9sebA8vwGv-CuumVcaFFpOwxZ7XkC9lcMW-5NRNSVPICuWgQNc44fETm2O4Zm-3kxzigQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
همانطور که ترامپ گفت، گاهی اوقات این آتش‌بس‌ها به این معنی است که شما کمی کمتر تیراندازی می‌کنید.
اما ما می‌خواستیم مطمئن شویم که هماهنگی مناسبی برقرار کرده‌ایم تا اگر تیراندازی شد، اگر حزب‌الله به اسرائیل شلیک کرد، یا اگر اسرائیل پاسخ داد، ما واقعاً با یکدیگر صحبت کنیم و بفهمیم چگونه تیراندازی را متوقف کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66678" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66677">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=QUZtuTrm8yCEd7mTWeyqR6vJAuRtSjPAOyIefQ_v9PvXw6NDA87EJmg0_8wGn9bLzWOWcCKFN0T8N9R28HccfThHCxN8zWfks98vKhxH6s9hjSmsU4z98FrYenHq91Xb438Y9squKqjbyRqeDvs2xY-Pt-WnXTF_nm8uXEO2RA7-R1Uj6A2-24aECMsFXEbPJWqCLOjoVPlU1VaurzN4ZYHEaZCaiqgX9DKuedQAQkLLzFsaj9s9fLgeWuHpcIlI7NEAhjnLEXr2i1iCZ6jJzklfgLbfEnHLVYNa0F12cWvhbN0IDCPr-qGVpL-i7rGkVoRW1aiJ04QN-rK59CZNLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=QUZtuTrm8yCEd7mTWeyqR6vJAuRtSjPAOyIefQ_v9PvXw6NDA87EJmg0_8wGn9bLzWOWcCKFN0T8N9R28HccfThHCxN8zWfks98vKhxH6s9hjSmsU4z98FrYenHq91Xb438Y9squKqjbyRqeDvs2xY-Pt-WnXTF_nm8uXEO2RA7-R1Uj6A2-24aECMsFXEbPJWqCLOjoVPlU1VaurzN4ZYHEaZCaiqgX9DKuedQAQkLLzFsaj9s9fLgeWuHpcIlI7NEAhjnLEXr2i1iCZ6jJzklfgLbfEnHLVYNa0F12cWvhbN0IDCPr-qGVpL-i7rGkVoRW1aiJ04QN-rK59CZNLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی ونس:
ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم.
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66677" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66676">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=HkIkIdGZg99MUdyZN7lOM8h0wlrn6RAd9Kx-g3RyZ4i_-EhAcgIY88rrAJR8gN8dNz4wmNVBlx2WSsAWtqv3-NLgtIT9fptsifYMAJaQPRQlSIqfJIc4-3W7cv9RN53EZYrHfvO1reSAvEFf112RJ0-26BMwlreYkmixc0V4O7LKpWoaX_ZPTxDdgFt6DqTfoVimhEe4cfybcOJqp_UZ4oA0tW18e11eR67FFxsKXHbsaAm58iZ0UvVbYYrqlZYS7WaTNGVKkNMIPdVBqucd9hun34FogNRoC3WejFZeDzcRefZsE6ehkKy9kuquHSycbhsfwmnf2fDVkBu6ofgVlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=HkIkIdGZg99MUdyZN7lOM8h0wlrn6RAd9Kx-g3RyZ4i_-EhAcgIY88rrAJR8gN8dNz4wmNVBlx2WSsAWtqv3-NLgtIT9fptsifYMAJaQPRQlSIqfJIc4-3W7cv9RN53EZYrHfvO1reSAvEFf112RJ0-26BMwlreYkmixc0V4O7LKpWoaX_ZPTxDdgFt6DqTfoVimhEe4cfybcOJqp_UZ4oA0tW18e11eR67FFxsKXHbsaAm58iZ0UvVbYYrqlZYS7WaTNGVKkNMIPdVBqucd9hun34FogNRoC3WejFZeDzcRefZsE6ehkKy9kuquHSycbhsfwmnf2fDVkBu6ofgVlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=RfSW33iYDf94ZdLU0x-NrkLjDuuM9Xo3TZ3tDWDl20hhopx0tB5wPaf0bUkj1rQ-JYtZoLvZqzWrM6XbXWFa3mTKHLweBaQUA2AbBI5sShquX07cQxsciF3Aawd3QiSCTlyPDcRuFiaqdP0tHibScXvuZqIWyfBmrvLXk0WZGeYosqeRIAalIiWz7vwIn5-UGCQ62T2WoRXRRPy5d85YU1JazrOY2KCPQJiZNmhhZB0pk3JeYj-n4J5fi3vF5Bst1Z81TvRAcOTrWt3as3yn9UyJZ7OhUcN2uTT_zzetcoLidsgAiw2APBS1oS8VlLXxRWw65nqKxOlM1yE_jyBh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=RfSW33iYDf94ZdLU0x-NrkLjDuuM9Xo3TZ3tDWDl20hhopx0tB5wPaf0bUkj1rQ-JYtZoLvZqzWrM6XbXWFa3mTKHLweBaQUA2AbBI5sShquX07cQxsciF3Aawd3QiSCTlyPDcRuFiaqdP0tHibScXvuZqIWyfBmrvLXk0WZGeYosqeRIAalIiWz7vwIn5-UGCQ62T2WoRXRRPy5d85YU1JazrOY2KCPQJiZNmhhZB0pk3JeYj-n4J5fi3vF5Bst1Z81TvRAcOTrWt3as3yn9UyJZ7OhUcN2uTT_zzetcoLidsgAiw2APBS1oS8VlLXxRWw65nqKxOlM1yE_jyBh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66674" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
