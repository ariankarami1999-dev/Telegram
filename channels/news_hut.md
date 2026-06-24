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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 20:55:17</div>
<hr>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf83llMcxzFzCG1JUl28AxVsqfDU6LsnH5QzxyykXH6Za9oDc7f35TmVF1dL2VDcmRg7TyTlj2b_VjROmy7_dBTiyPTHoUTUKBq7-Q_TLSDjExVKNX3uPRJfyPKZwzd5A7kud1Lo6Qj8SekGSjyNyskjlBocDL_eVBo7BTXLLAn4FPnpjLDbcgW_r9uc3m5bEUmohilHLBDTD6GgFlr-jT7aQ8xbC43cvg-nPI4Zr7iWDjlBK_DxBuMyJzArzVoQWSr0tsVZS035zYnpMPnTarzApSwunbhysEbKnspwF3ent2jrzcNIaNUAJ-5vIiUpzHpc0PYBZLXFdTFm1FLtNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do2hMvulqIdUaDQY9EXOPIqMEvqmk_yHohOAjHYmeYR2lxk7NU-QWWJtMKK4wrHR7r-9ooiehceB3NlTsvsdvjjqtDZk0o54OdbtK0j3s3BkxevdnWnYB8khkMjWpv66P_3Eq1jr6mscPdTTdnthScLZ5qf2R1gm91UJ5GNRKBAY7WrFbVqaMu3BdEsSX2eAgOKktEWYuzvAbuxAKLg7v1ZS9ZjZ9pA3pwASsoHMsPpqsVyvdx0DZ3A4Zrsoelrww8xzBzzUxE_YH2RxvUs429vPp4OTGkUH7j8qmjdTSYUmWSGzRXuYexV3j_uKKi9VUGTVpNcPoVxIH3xMLe0rnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcTN8lp9HAn4rgKtG_kdqimJETHVUzWGje00fVLmwunaek8yMPZinYpqBlzqydPJqXJ9uc3KZP5GihvyAlCLZF2nl6iV5YZ_mNm7nIkLHyRdePfXA0S7A6K5lC08Xk0klgwTl8AA03b6HJGbFKgUuQODcicrepMmsmBLhlMAT-vdBHzXspnKGJaNi2bp03oy7N4a1UQ8aUYV6Qg9o8q0pnyBysP4YLj4fbtLEXPB-CWtH-3FaRgEPQ021T_eMdO3d64WitWuVmqHLF7SYVLxTZ1pxwmZERY1Y_P0J_DEFd_BhE2IVIP63sT519-a2xPnTm3goNRmUD_eWOBZ-g9iyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=bU8RsgVogYP5B4mbAEsTS61OjAyE2W4dy59AFRuBap8U9illNdrszGBBRx_QkEdIqVuKKfq1jDKfiea7mqJCH2XKcLHf2694lKLnwNFKc2usNDFq-fzCrwixSD7VIXHIRwQH5j-5l8OwMjWGaCOidaqfxTa4P37pDrfvl3g2La7KvEt9SjwXA5tZWyBX8iWhz0yK5R9clvVOj53fVRyo4vBVb8eaiZgF-EM28LU4m_5df9N9G1MsG5Ye8kKxg6VTLBLByD_tlZCKucPQWYsZQclMwrRd4hTaK1Zi5z5T2GsHfkTfunPJWXKhFbZPYcBkXfCIzEL33Cc0VgmDp2r13g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=bU8RsgVogYP5B4mbAEsTS61OjAyE2W4dy59AFRuBap8U9illNdrszGBBRx_QkEdIqVuKKfq1jDKfiea7mqJCH2XKcLHf2694lKLnwNFKc2usNDFq-fzCrwixSD7VIXHIRwQH5j-5l8OwMjWGaCOidaqfxTa4P37pDrfvl3g2La7KvEt9SjwXA5tZWyBX8iWhz0yK5R9clvVOj53fVRyo4vBVb8eaiZgF-EM28LU4m_5df9N9G1MsG5Ye8kKxg6VTLBLByD_tlZCKucPQWYsZQclMwrRd4hTaK1Zi5z5T2GsHfkTfunPJWXKhFbZPYcBkXfCIzEL33Cc0VgmDp2r13g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b87jU_tvcpJZwuIr-YWhNCARNzjCraLgy6mhFH5FtDG8msJ8YbT5B8qp784Vmn9PCQ69g5CMhZL3My1HISAb7y9N19IDeZJulzN4rqCNWrjU5-e4JrDZhQwg_nECpgz9cdAGFsXqiRHfr2tyNOR1ns4ZDyO7Wqeg_0mIlZQDPSqnnxo9zXRsdURujx91DWYUPnC56AkP2NPJ3pUEEcHMeXaN89aWHD1qzuCMZMC_TGDyd0_nZYchi9p4Fg6PLoWzdlJYvqecC-fbqsHF5eNyhcDw2-uL4ywKquYtfBwlWp_wqJ4qfFpkgaBP-QAa8bcXoF94vnd9cquyhfQ35orUTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BB0_aFOvEXcgPpEDamGZv-L_bvw6gxvJT62vvg9oLbEBss9qoMn-Tm3UgrJXNbmK2H_N4lRgfgd7aVZaJlaay6cn5kHo0c-4b4YUfLElBfIRQSgyxWwYh-_lVPOJfBh1yh2os4Qc1vUKVX2KUbDdZ994rlLRA1mANm97s8xlQY5lI-wY6lwOn6b9bqQ0GeDm9HhzwQUSWOVYHEUo9IWbrMQDfLbCQvozf9aljMjqYtl-pQ_Ymsq9-HHVSQciTYKeVxjP3uioKfLcNaqZPKJ9ZHVo5pfAU5t8tItlvbZ96c-X8dwvIKvdS3_2hv_OrtJhWWSMKjN7ab0KhTRyxS2QSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BB0_aFOvEXcgPpEDamGZv-L_bvw6gxvJT62vvg9oLbEBss9qoMn-Tm3UgrJXNbmK2H_N4lRgfgd7aVZaJlaay6cn5kHo0c-4b4YUfLElBfIRQSgyxWwYh-_lVPOJfBh1yh2os4Qc1vUKVX2KUbDdZ994rlLRA1mANm97s8xlQY5lI-wY6lwOn6b9bqQ0GeDm9HhzwQUSWOVYHEUo9IWbrMQDfLbCQvozf9aljMjqYtl-pQ_Ymsq9-HHVSQciTYKeVxjP3uioKfLcNaqZPKJ9ZHVo5pfAU5t8tItlvbZ96c-X8dwvIKvdS3_2hv_OrtJhWWSMKjN7ab0KhTRyxS2QSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=vagVfZ3GSjo2VhGwbX4vgMkw6MwjNjB6oK-EeSCmMrU3tygpzvid417b5Fyno0ZN0A7QWlgIQRvHcXqT-RTswoM6bMEltCkKc5AMwyF9QnRKwWoTBhMj9eGl50JnlY8APzNLs7oQ0lJpqEy4TkKGhiDnRhSorpgr6B8jgl3vNmjKs4paERJJ-7ZBV3tnsEe93mYaWI5VHmLHuEqxJsLLIc8fduSVUAEyaK_qHJnBAlYXKBjstzVmSkz0DY8fX18XkPuKkiYG19Am6Dy1b0risNbRMTVnL3Z9pcBJVI6HeC4J6PhUvQOXKGsxLoaYhJQM80i2Nh1NFcVY5JPp4-sYPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=vagVfZ3GSjo2VhGwbX4vgMkw6MwjNjB6oK-EeSCmMrU3tygpzvid417b5Fyno0ZN0A7QWlgIQRvHcXqT-RTswoM6bMEltCkKc5AMwyF9QnRKwWoTBhMj9eGl50JnlY8APzNLs7oQ0lJpqEy4TkKGhiDnRhSorpgr6B8jgl3vNmjKs4paERJJ-7ZBV3tnsEe93mYaWI5VHmLHuEqxJsLLIc8fduSVUAEyaK_qHJnBAlYXKBjstzVmSkz0DY8fX18XkPuKkiYG19Am6Dy1b0risNbRMTVnL3Z9pcBJVI6HeC4J6PhUvQOXKGsxLoaYhJQM80i2Nh1NFcVY5JPp4-sYPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=BHx6sl5oO_9B-kGBzq0g0mlVSRZxdgwKmdM8bR0_ItY3ZBCM7CyOY43BAOZN4Icod_XigW36FgV1sfeh5_XV4FLj3oYpviPV883cTZwy48eFc1cGgVoShjj9Mjzci8Drn9naEjjbe1L6qzgNmTW3NQB3WW4e8D1CVDT0pcWUs7g5FW0Lu4M6T3qt8zRpOk_hutVUMs_5l2wXsCQWNyOiO_g_WnY80w_5nxq114XtZXFA_ZfFXfWRNkrzsf5VPdl4DPM_hac8EWGWWdjtw68pgvkxFPNc1cBDMQNXeXwKKTYt4qYir5nuGKDYJnEMsXwiMI4siwiBlYGls_TimvB9NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=BHx6sl5oO_9B-kGBzq0g0mlVSRZxdgwKmdM8bR0_ItY3ZBCM7CyOY43BAOZN4Icod_XigW36FgV1sfeh5_XV4FLj3oYpviPV883cTZwy48eFc1cGgVoShjj9Mjzci8Drn9naEjjbe1L6qzgNmTW3NQB3WW4e8D1CVDT0pcWUs7g5FW0Lu4M6T3qt8zRpOk_hutVUMs_5l2wXsCQWNyOiO_g_WnY80w_5nxq114XtZXFA_ZfFXfWRNkrzsf5VPdl4DPM_hac8EWGWWdjtw68pgvkxFPNc1cBDMQNXeXwKKTYt4qYir5nuGKDYJnEMsXwiMI4siwiBlYGls_TimvB9NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=FAyhCZgI98A6aq0Rb4gj1eWqS9pmjou_GmbrI8Oq29wd5OKMxkyCUzovnjRlniRE56w1HOXR9icSK2N1SgToT2G24yeNhbVhkzzr0Wccvrg7EjzIQmFI3VmdX3FGmEJh2L3we_MUuMPLpnU0kWPqMZ-00VzwoOkcsRfZILMNG9SH_04wFv7zpT4nAjlCtEc-Lqe5N8ynGkHNH9WiD7Oyi-uLKbJxwOznG7YFp2t5V1Aw8nsWy7ZJnNVNvzXbTYUHdbGzyKsX_XaBany2BDgZk2sb4dK8fRbi2ix2Sj8GemHSHDbGnjg87SphiIzUesHCyWi-jTZUvWi44GbJtcoruA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=FAyhCZgI98A6aq0Rb4gj1eWqS9pmjou_GmbrI8Oq29wd5OKMxkyCUzovnjRlniRE56w1HOXR9icSK2N1SgToT2G24yeNhbVhkzzr0Wccvrg7EjzIQmFI3VmdX3FGmEJh2L3we_MUuMPLpnU0kWPqMZ-00VzwoOkcsRfZILMNG9SH_04wFv7zpT4nAjlCtEc-Lqe5N8ynGkHNH9WiD7Oyi-uLKbJxwOznG7YFp2t5V1Aw8nsWy7ZJnNVNvzXbTYUHdbGzyKsX_XaBany2BDgZk2sb4dK8fRbi2ix2Sj8GemHSHDbGnjg87SphiIzUesHCyWi-jTZUvWi44GbJtcoruA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=gebWfRYBtenaQGWCCe3qsaHkR50w-C8hFHdDyKdIJ_Al50vo6PZ57QlCs0d_TPnflZdONQXJ5ML8OgryIoFQyrQZ9KQbf81Zc8jzJPNd78u3KtDk-dBeSjsfpkuyxLnnRUMsRnBBxIzYx9ircmB5i5N5B6qKsEezbdRywNPAy4nEGSN4VBs6D7Y3-Gh6ae89OEl7xKAKm3L6Z3aB63fG8VMdCkspK5tQYPxPuCy4Gnqf9Ugkk2my7cBsmERklcesQ1_RUrULUWI93_G-2ic-5I59cx1g41odToe6L7_sqtOplQ3qSzSkzosOEPGLbzpxpeX-YhZ1TRQjKxLE_EcvmGsh-lz-ryNxsvHNkcV1dm9mllfbRPwtvym8FHdmHDdhsNsAhZpd2CW5PFkWhz3YqFejFZ1gMpD4IL687U-NozG4XYuTLXP6Bp55YDHusMusRpWJl2s2jfzgKpN0TXYIM5b1bojJu1UGko4qGdKNKf3YLNv030bjsROajUr7QNkXVOgYvwaYg1NT4v7xI3Ej6EM0zO1U4YzuJNt9g45NfK2ucjcNbUcsBqObwI6otFnaQUxjbrL9rekOZBxx-oxJwBJU8xEB-zOrTr2sLMMTES8Pc6uL9GcYsod9wG-7l4Lqn73oC8r8WAR-3Ogz4z3IIEsVzgUR12cFGlBz5dXsUGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=gebWfRYBtenaQGWCCe3qsaHkR50w-C8hFHdDyKdIJ_Al50vo6PZ57QlCs0d_TPnflZdONQXJ5ML8OgryIoFQyrQZ9KQbf81Zc8jzJPNd78u3KtDk-dBeSjsfpkuyxLnnRUMsRnBBxIzYx9ircmB5i5N5B6qKsEezbdRywNPAy4nEGSN4VBs6D7Y3-Gh6ae89OEl7xKAKm3L6Z3aB63fG8VMdCkspK5tQYPxPuCy4Gnqf9Ugkk2my7cBsmERklcesQ1_RUrULUWI93_G-2ic-5I59cx1g41odToe6L7_sqtOplQ3qSzSkzosOEPGLbzpxpeX-YhZ1TRQjKxLE_EcvmGsh-lz-ryNxsvHNkcV1dm9mllfbRPwtvym8FHdmHDdhsNsAhZpd2CW5PFkWhz3YqFejFZ1gMpD4IL687U-NozG4XYuTLXP6Bp55YDHusMusRpWJl2s2jfzgKpN0TXYIM5b1bojJu1UGko4qGdKNKf3YLNv030bjsROajUr7QNkXVOgYvwaYg1NT4v7xI3Ej6EM0zO1U4YzuJNt9g45NfK2ucjcNbUcsBqObwI6otFnaQUxjbrL9rekOZBxx-oxJwBJU8xEB-zOrTr2sLMMTES8Pc6uL9GcYsod9wG-7l4Lqn73oC8r8WAR-3Ogz4z3IIEsVzgUR12cFGlBz5dXsUGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=Nf5hgSkTbPXQr8CPDUONdLg2ql-FkcyDKJdaSr7EVv203zJ7mnnXDu3vMtUDCr9GAwlMEZAGHAsN0WDgcNXkrmE25fVX1IkVSqWzQ4CTUiDOeOLdI0SUp3oWXjEbOiiWdWySCSb7IS0yxbjOytDVzwG78mBmYURtLdiyTLusIsMTvwTW_UP4N5f1XxDfwYUhac_3uYPOZA3PgN27I2hceIbZ6d5cIxksVWc47a6cgeA7NbP_YtKpZ1mKA7S6E8wwwpG2WH-Ncs4414LtQuChl1ukm_s1mVXDMdc5PXr6yvXlnW4I45YXNPaHwnUvi-oNYEJsaPou6V4h5jJyrtkmxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=Nf5hgSkTbPXQr8CPDUONdLg2ql-FkcyDKJdaSr7EVv203zJ7mnnXDu3vMtUDCr9GAwlMEZAGHAsN0WDgcNXkrmE25fVX1IkVSqWzQ4CTUiDOeOLdI0SUp3oWXjEbOiiWdWySCSb7IS0yxbjOytDVzwG78mBmYURtLdiyTLusIsMTvwTW_UP4N5f1XxDfwYUhac_3uYPOZA3PgN27I2hceIbZ6d5cIxksVWc47a6cgeA7NbP_YtKpZ1mKA7S6E8wwwpG2WH-Ncs4414LtQuChl1ukm_s1mVXDMdc5PXr6yvXlnW4I45YXNPaHwnUvi-oNYEJsaPou6V4h5jJyrtkmxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=IE0jq0s24ChhE0NpUuupgXHQMD9Et1XBOq6QLGMSpDA2PLBF41t1UiYLyNbmUmqUWeEAyZfBGrEqIjfiWOP1c-ON0ZSPbfA4CUtqRumsmm3j60dcjwV5QvbL8S0knoAqBN6JiOcF21HOfl0u7Wk0GNabRMcELc1L6jV43fGNjDf2WWKUzb-UHOCftYO0XqnG9briJXtt8SmNhgXVQw3AbcAdXXmp9daVX-hHs-MiK1Et9HYwltioo0LabCbCyRinSXKm3i0ffChNc6nmg5lEdgUS_X9CXQr966XdKDZgkP7nXsGTC7D2Vr3DeeN3H2rhbiXa_bv_CHAkSdAT76-O0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=IE0jq0s24ChhE0NpUuupgXHQMD9Et1XBOq6QLGMSpDA2PLBF41t1UiYLyNbmUmqUWeEAyZfBGrEqIjfiWOP1c-ON0ZSPbfA4CUtqRumsmm3j60dcjwV5QvbL8S0knoAqBN6JiOcF21HOfl0u7Wk0GNabRMcELc1L6jV43fGNjDf2WWKUzb-UHOCftYO0XqnG9briJXtt8SmNhgXVQw3AbcAdXXmp9daVX-hHs-MiK1Et9HYwltioo0LabCbCyRinSXKm3i0ffChNc6nmg5lEdgUS_X9CXQr966XdKDZgkP7nXsGTC7D2Vr3DeeN3H2rhbiXa_bv_CHAkSdAT76-O0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=ffyprLgY_gk3FCwrty6_8kT1wMutnDTXyXstwon8tuvrRgi08hxqjzVPqv-KceDj0phWj96Lvs0Qa2-sQVke7ascleyn6VTjIvn0gIx-dt3VmulX4g7bNqAAzcYlVilQwvG9g2z0VYJ17DdhLu5t2ybH6sjWR5aZwJpT9HS5WJTM9xRbqg3iE4ETI6-wm2TWW6znt56-oSJxml5qS2bSQaUaXJ38X2h_dhFCy9VqQDoe5-GCHBIioByq72GNSKnfd6u5VcWnRwu9S2hHNYx5pMF84ul7dbi0GPSzFxgQ_OQjBSe7b26CQbQCd3oYn_FzEByK2x-C6I2sT1m14RSoqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=ffyprLgY_gk3FCwrty6_8kT1wMutnDTXyXstwon8tuvrRgi08hxqjzVPqv-KceDj0phWj96Lvs0Qa2-sQVke7ascleyn6VTjIvn0gIx-dt3VmulX4g7bNqAAzcYlVilQwvG9g2z0VYJ17DdhLu5t2ybH6sjWR5aZwJpT9HS5WJTM9xRbqg3iE4ETI6-wm2TWW6znt56-oSJxml5qS2bSQaUaXJ38X2h_dhFCy9VqQDoe5-GCHBIioByq72GNSKnfd6u5VcWnRwu9S2hHNYx5pMF84ul7dbi0GPSzFxgQ_OQjBSe7b26CQbQCd3oYn_FzEByK2x-C6I2sT1m14RSoqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qvwCVrgH0yFiEbCh08j8TY60llrkOnWJFlwo1DuKkuZ-TzdxUk_S-jqXIOnmuuTG_d1WuPUtjvPrRXGS1cWKezfAHmt21IGT2moI3ZyZilm6wZtnfDBQ9A__17jM5qmzXTV52caQaLaH90y9E5PXhJ6eI2L2PR3yFoTw6Ec9NHi2hbzjQIQ69w6qtLD36edVUMbm7dEPDhD7_ossBFMgybaWMDxwt_jcW30k-NejyVMZl7PhlN7bzBlDL9krHE8EpmdSiPXm30ia3qZk9dHhcVbCh2RVOwXy59ZDpy-XMkI9qOWm0MckT1avh1o3P8jNKw8xgZ9zLpAqUFscD1szjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=rri7U4MufiLkwLMhKU9YfS-AbfIf1mzJFypzM_6A6Xw51KrM19BPxBXJH0-hQdzVYLFNK6pnxli8v7w8MA7dpqw-Zu8mYtlUV9NrXqBR6S2ng0AZmbfEUaiJXfxyXNL-rmGUqadUs6TvISJgEcTzUV0my4tg91xPny3MRojQwq3YLK0BZNqVGG17jYxmw4ywIXXDIJF6aGGu3aUqgALCPkdGE0WLth_vul82xmjnLPnX_5Qvf34fmBYbZYiPXV-d0cBLuJlFgwAyqBaMVhJoRYan0zhkpvjU5ID8rV0SyngSiIl-KmBU8UAXV7bt-SoZTrDS5WkPjgmDDtadzikzEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=rri7U4MufiLkwLMhKU9YfS-AbfIf1mzJFypzM_6A6Xw51KrM19BPxBXJH0-hQdzVYLFNK6pnxli8v7w8MA7dpqw-Zu8mYtlUV9NrXqBR6S2ng0AZmbfEUaiJXfxyXNL-rmGUqadUs6TvISJgEcTzUV0my4tg91xPny3MRojQwq3YLK0BZNqVGG17jYxmw4ywIXXDIJF6aGGu3aUqgALCPkdGE0WLth_vul82xmjnLPnX_5Qvf34fmBYbZYiPXV-d0cBLuJlFgwAyqBaMVhJoRYan0zhkpvjU5ID8rV0SyngSiIl-KmBU8UAXV7bt-SoZTrDS5WkPjgmDDtadzikzEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=Va3AfEHQmpgo4wXTD63gaD32PRAtLKrqpMdeu0XIPBrUyPJhzh2tTDcJu6IwTVRb3DjgwquF1ngKIwf7lAxUOIdYV0H8fe3aR6sJw2LSSyT52ikIIT5Gd8GURxhTlh-9GqlE8OmxMCkW7vqXe489RHWdmqO3W4XjFByAKf94mOaDtp7zvgEY4LCX1cq13066bbUGzGL5893IPFkudQ-2yGaukPnV8c252LmYLGxQTmBsLnraSnxbH-XGmqGHHhepWrcFzAADGpQpKYF4tGyxmQgVakGSj5mskWkmDT2sDGQstXTQdLhS3GU0d1steGJtg0LWIfR89_um-DfFOmuj1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=Va3AfEHQmpgo4wXTD63gaD32PRAtLKrqpMdeu0XIPBrUyPJhzh2tTDcJu6IwTVRb3DjgwquF1ngKIwf7lAxUOIdYV0H8fe3aR6sJw2LSSyT52ikIIT5Gd8GURxhTlh-9GqlE8OmxMCkW7vqXe489RHWdmqO3W4XjFByAKf94mOaDtp7zvgEY4LCX1cq13066bbUGzGL5893IPFkudQ-2yGaukPnV8c252LmYLGxQTmBsLnraSnxbH-XGmqGHHhepWrcFzAADGpQpKYF4tGyxmQgVakGSj5mskWkmDT2sDGQstXTQdLhS3GU0d1steGJtg0LWIfR89_um-DfFOmuj1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=AZ7ckjmAoP7Cezt01D40Mvgbf7FLTTA6TbH70V8VnZtlAbsoE2wF8N-m5rPYFS6m_mv21XYxEBGV_k2tNFgGWnzaanZKc8eZ26rcl_1mlgvqd1zmlkCbDvEYamdSeksHiOBdRPHRFbWSDdVOzKqrtNMA5TBve77hoqPRli77JELGQfSAFHoLw58l4FEuchU0j_zTJFnldeiPalL7xYN9tASq4OaME8svklFHTXoc0B1qxh5ncuXfnyLlLUppLtnUHELXfs8vjfrE_EPTx7stuldqaN59-2Q690L20DCRtoF6SbNcKbWBuh1j5YK5Rwv4wlNHv5xkjDPa5ONlcgZ1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=AZ7ckjmAoP7Cezt01D40Mvgbf7FLTTA6TbH70V8VnZtlAbsoE2wF8N-m5rPYFS6m_mv21XYxEBGV_k2tNFgGWnzaanZKc8eZ26rcl_1mlgvqd1zmlkCbDvEYamdSeksHiOBdRPHRFbWSDdVOzKqrtNMA5TBve77hoqPRli77JELGQfSAFHoLw58l4FEuchU0j_zTJFnldeiPalL7xYN9tASq4OaME8svklFHTXoc0B1qxh5ncuXfnyLlLUppLtnUHELXfs8vjfrE_EPTx7stuldqaN59-2Q690L20DCRtoF6SbNcKbWBuh1j5YK5Rwv4wlNHv5xkjDPa5ONlcgZ1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=UxAVwlIajHVESTyw__aDZS3TjueH7H5nfK77mOp5YIhfGoOc-Pq-y1Sqqj0WZ_Iby6SUDwGUB_YWggsi64bkS_3_kc9hc2vRbDahKGSsFOCW40hGsCK0pfCswDV3yhF6U-Gv7dd1OegoPFpDI8kF-SGspwJxlqJbut4GmDGP5-ygAy4m9S7EyLuNiFTt9pEUNhUlYJhmU-OrtiIzF_SvmgWH5z2FGlOlTzCVwso77J6bETY1mYOL7St0Wc-BSqEj2pJNTVnjGBkCFiNl68Vb3k39knsGwq8Bs62yfFQUD3Sfx4IOMOVp1fidf11tzxnfTMzhUoW4X6wdMaTFxK903w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=UxAVwlIajHVESTyw__aDZS3TjueH7H5nfK77mOp5YIhfGoOc-Pq-y1Sqqj0WZ_Iby6SUDwGUB_YWggsi64bkS_3_kc9hc2vRbDahKGSsFOCW40hGsCK0pfCswDV3yhF6U-Gv7dd1OegoPFpDI8kF-SGspwJxlqJbut4GmDGP5-ygAy4m9S7EyLuNiFTt9pEUNhUlYJhmU-OrtiIzF_SvmgWH5z2FGlOlTzCVwso77J6bETY1mYOL7St0Wc-BSqEj2pJNTVnjGBkCFiNl68Vb3k39knsGwq8Bs62yfFQUD3Sfx4IOMOVp1fidf11tzxnfTMzhUoW4X6wdMaTFxK903w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=ZrffgWu72_XBiVtfGc34Xa9vItQKot1l1MHazA6AIhe7m1_mPEWZhBz70U9ZHUso5qxSivYW2KPZ4x30LJySGLvNoQkjj8SM0MSJeFr6YM8caM2ZmUx0bcOdZ_VqZq6EPnvH6JsOAjH4lHjUww1c88Hp9imlFbojpErYJS4d-8q9cvMJs6PTJ8_rexNZMxCkWsPtxsQWD2VvnSF9NWbgWzdqkW8thXuPzGuu1YAQiPVo7Y9SYTaaLn_-6H215TVF-uwKlvwfyNcC4h9HZUS28ufm6Qme5jF3dbTTODZCDS3zzo2rTDL-m1UjE5YICMmEmHbSGcGgvEbfhKyKB3ynKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=ZrffgWu72_XBiVtfGc34Xa9vItQKot1l1MHazA6AIhe7m1_mPEWZhBz70U9ZHUso5qxSivYW2KPZ4x30LJySGLvNoQkjj8SM0MSJeFr6YM8caM2ZmUx0bcOdZ_VqZq6EPnvH6JsOAjH4lHjUww1c88Hp9imlFbojpErYJS4d-8q9cvMJs6PTJ8_rexNZMxCkWsPtxsQWD2VvnSF9NWbgWzdqkW8thXuPzGuu1YAQiPVo7Y9SYTaaLn_-6H215TVF-uwKlvwfyNcC4h9HZUS28ufm6Qme5jF3dbTTODZCDS3zzo2rTDL-m1UjE5YICMmEmHbSGcGgvEbfhKyKB3ynKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=MjeHu6V8WKdCBGjVuLWRDBZHd_wshtLnGacC3k6ddabmZBJhPBKWSzAMwHAVjh8TPPwPZy2NF3ZuKbS3IH-SqqLSE_ZRRDs89m99v07EbXg2UvgWVjq7mZYsmL09jyiX0sqpM6fR4N-dGqeBecriSQGhrXTEq3VAoxdggac0uxjdJQ6FXcugm7IndFSuUIegAfjHxmNeALXyde9e9lFL-xGPbJ_Vjix9bWW3k6BWhW2OH_BYVUih0zZGktdv8Nwf4esmfGwiSatdW8XnV1SbRi7SFmglE0-ZuF3PluhsMabY1kh73UOLKVgjjYnxxBnLq6j3UhLfURPCFUv1i-k8yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=MjeHu6V8WKdCBGjVuLWRDBZHd_wshtLnGacC3k6ddabmZBJhPBKWSzAMwHAVjh8TPPwPZy2NF3ZuKbS3IH-SqqLSE_ZRRDs89m99v07EbXg2UvgWVjq7mZYsmL09jyiX0sqpM6fR4N-dGqeBecriSQGhrXTEq3VAoxdggac0uxjdJQ6FXcugm7IndFSuUIegAfjHxmNeALXyde9e9lFL-xGPbJ_Vjix9bWW3k6BWhW2OH_BYVUih0zZGktdv8Nwf4esmfGwiSatdW8XnV1SbRi7SFmglE0-ZuF3PluhsMabY1kh73UOLKVgjjYnxxBnLq6j3UhLfURPCFUv1i-k8yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=XH-kH0TomVJJhLoLIpZiQUCn7JcRsDishihQ88qMgCo1ExYLZy-wTKPW2Ar2F6q52gmsVAoJTtKMWkrWZR5KiloZmdYft3KcbH4QPv5NNZ2cLJrgcGuM6PEf4qJTn4rbkIPymUGxx5oL3Ytjqhp2lKdASLv6Jw-kp9Hm9PsWGgy7ZV-TC9S0uyz6k5J7lFENN-Zxf7eXVAA8l8iNpltempGOorSF7KknvXkHNMaAMd0fMSOHms1srf0BY8Er0QVWdYg3_vO1JztTIWleP0si28yFTTzJCA9jJwTrei0UZWbyxneRWRF0fzJ2-d33Yn0bWzLuRI3GUnmT3BZT_7DQZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=XH-kH0TomVJJhLoLIpZiQUCn7JcRsDishihQ88qMgCo1ExYLZy-wTKPW2Ar2F6q52gmsVAoJTtKMWkrWZR5KiloZmdYft3KcbH4QPv5NNZ2cLJrgcGuM6PEf4qJTn4rbkIPymUGxx5oL3Ytjqhp2lKdASLv6Jw-kp9Hm9PsWGgy7ZV-TC9S0uyz6k5J7lFENN-Zxf7eXVAA8l8iNpltempGOorSF7KknvXkHNMaAMd0fMSOHms1srf0BY8Er0QVWdYg3_vO1JztTIWleP0si28yFTTzJCA9jJwTrei0UZWbyxneRWRF0fzJ2-d33Yn0bWzLuRI3GUnmT3BZT_7DQZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=LKpt248pdO2x7oXOKgF5zsNWTbSwBbfHhmRd6GQ3e1XmcQY0AcX7syEiWQFsANXTry_3Ovaynac6HRZsRitdb7Q_XlFVHF7EQiyQOEBdIOdmYBDfiJMItHw6XhEvzkDkyq982kiCsA5VdUUMIT2F7lDmzvp5fwt2dz-IY5Y_xHOcbnqWFonIyDE26k8LeOg4yieYylaHlXAupabDhLmH7vOwWpHQnKxB-nki4Z07xQM31K6HS0q2f0_vO9ZV9eNuPqMQvn-x_dthfbbxOS7CLwmU8CVR0bf6C85aqGJwVclJBwtGrcWBQC4ptJeLMCiuEciaKKMFYP7OpEixHf0uBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=LKpt248pdO2x7oXOKgF5zsNWTbSwBbfHhmRd6GQ3e1XmcQY0AcX7syEiWQFsANXTry_3Ovaynac6HRZsRitdb7Q_XlFVHF7EQiyQOEBdIOdmYBDfiJMItHw6XhEvzkDkyq982kiCsA5VdUUMIT2F7lDmzvp5fwt2dz-IY5Y_xHOcbnqWFonIyDE26k8LeOg4yieYylaHlXAupabDhLmH7vOwWpHQnKxB-nki4Z07xQM31K6HS0q2f0_vO9ZV9eNuPqMQvn-x_dthfbbxOS7CLwmU8CVR0bf6C85aqGJwVclJBwtGrcWBQC4ptJeLMCiuEciaKKMFYP7OpEixHf0uBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=TvlMZQfqu9MLb1JWb3F_s7rn3M4EM1uG1TcPIUss5ie_7E4ofdea4qozIFOR_0HgViy-A48hx-2MrbvkyIkpIixadEfZxj58oBJdkvJv0RDElbTyv60GiPlVX6pBtWZoal1brn0YdXiPVajAMdrnMj4rAtyAenjVk-mdoVGpuXFcehQWUE_mu0POhxUWg2PHvBcWOX8ELFuzg7Ks1mGx8-e7pjaWTPnR8EQ7n9ZMqBTN1JlAjcQHkC_CmrIdkV5YykDh9G5myIugchaUVxvDiaecacL0aCtCsjtzfzMy5THZKMUh27lIwZ-18sfKOVhjwItj_lAenMvLN7b52TqNGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=TvlMZQfqu9MLb1JWb3F_s7rn3M4EM1uG1TcPIUss5ie_7E4ofdea4qozIFOR_0HgViy-A48hx-2MrbvkyIkpIixadEfZxj58oBJdkvJv0RDElbTyv60GiPlVX6pBtWZoal1brn0YdXiPVajAMdrnMj4rAtyAenjVk-mdoVGpuXFcehQWUE_mu0POhxUWg2PHvBcWOX8ELFuzg7Ks1mGx8-e7pjaWTPnR8EQ7n9ZMqBTN1JlAjcQHkC_CmrIdkV5YykDh9G5myIugchaUVxvDiaecacL0aCtCsjtzfzMy5THZKMUh27lIwZ-18sfKOVhjwItj_lAenMvLN7b52TqNGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=gL_Omjyjdt0o4VVuFSnlIC2Ip703QcwjATGGi1bK7-sBj0X0vqa-zUGih-xgB1U8-lhC-6FDTY8DHupcXuTq8q-0TxOfhctu2wYACRlS4rhAmcHe13BCZLaDGEe1Vr8OQbZ6Yi4W0rvvJeyjzMUTBwGMne5I8phFvOpe7_cRk6IEgLcb4iiDtZfEdNom0Il8a1LrTO736Wt-HMoBnoVYt5sl5cXMyE5Ye1j4czEy6lSv5N0nibxVWAPA3dvcHrU6JarUcsszJpIup7jHyQBSbJfCN71CK0OjRtNhUhMK-P5-4yNQ-thDqe9yWa0i1Dj2FfAsf32UkXZD9gDLBqWSKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=gL_Omjyjdt0o4VVuFSnlIC2Ip703QcwjATGGi1bK7-sBj0X0vqa-zUGih-xgB1U8-lhC-6FDTY8DHupcXuTq8q-0TxOfhctu2wYACRlS4rhAmcHe13BCZLaDGEe1Vr8OQbZ6Yi4W0rvvJeyjzMUTBwGMne5I8phFvOpe7_cRk6IEgLcb4iiDtZfEdNom0Il8a1LrTO736Wt-HMoBnoVYt5sl5cXMyE5Ye1j4czEy6lSv5N0nibxVWAPA3dvcHrU6JarUcsszJpIup7jHyQBSbJfCN71CK0OjRtNhUhMK-P5-4yNQ-thDqe9yWa0i1Dj2FfAsf32UkXZD9gDLBqWSKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mImVx__olkB27-EZEZrEc51rXS8Zd8FxRzBYqt8OPuMQRv3LeOPkm1MqyeYENUF3p_zIwREs6n_CFbUvEvV44F5GjTrQq7CyFb5BISpueBlL3yekERifHI6Nxj29npqcGnqqjJSpuFUv-w2oxZ9KJVi8mSrLyfDg4cSjIvBzVP46Iqq-uqNsFA0McAbQBFYCHfaYi1XUbrXOGI1XrKD7JVA6FsZxTgAPT-OqwEP53HJ2auGiZMNsx6bIpoodFw_m69TsluHQEHvHPIZ9QyFk440-5Mvi_4etHM2H2SjVvJr5Eoqv_9rERY9SW6oaF7jq7LNyGXfjThFU_4GRTmNuUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BoCypmSb9I7XcWox9dGm3wT6VjQfKLnUnXuM0sszugxvfypbrXxueqW9cy99bQj3f9mZyINRvoTfJLRLRuGFm_FOqwad7AuO5GtNCoDV6TcjjN3mgj6AyZLkh2pXaqEGCTUCYIeitIgWvf9WRX7BGr3NoEm77bHp3IW__3UEEZt9kjj9VyczVWbUKyz5Qzhlln7EOSdIddY92-CuN2hL8IXtejA6EfjTN1OqC7IjQblHsDjmZ3kJQBxv47RA0lldN9Cx951c2od1TYFZ1y4b3aBA8qVq-Uxh02gUzIWaH4JuErJ37ELzyE5D2nrPjjZQEPSG8gBOtHZ2B7gQ4pP_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=Fi68d9VIWOUO3XFRLJKWa0up2PhoqecGnOZfH0Ivb-8g3aD7_kc8QDSixfKLLc0waJfzpHa41bqxfD1WA5BySXNHn6GHfR0tswgy8PF0kUYgFB7uED0xtNamUgOWQjTikIDspRbvSw56S-QdGbJZHziAraI1boBEZ5pogq6yxtIbGd9bYk6bwqjA-sRt2eDZXRNwkuem3AoT17Es6MEOuqg0jqgv4qxL7eDFCZcQxnqjqnuXx_8U-jhX9r6BMxcIvjTn22RHJEFbdXuRfKZAOq3u5MHJtaFcvv7gi7HMVDmoQcKr1ZVpq0yROVOs49HdVqwOZS5S8Z1zlbgHmuZ4SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=Fi68d9VIWOUO3XFRLJKWa0up2PhoqecGnOZfH0Ivb-8g3aD7_kc8QDSixfKLLc0waJfzpHa41bqxfD1WA5BySXNHn6GHfR0tswgy8PF0kUYgFB7uED0xtNamUgOWQjTikIDspRbvSw56S-QdGbJZHziAraI1boBEZ5pogq6yxtIbGd9bYk6bwqjA-sRt2eDZXRNwkuem3AoT17Es6MEOuqg0jqgv4qxL7eDFCZcQxnqjqnuXx_8U-jhX9r6BMxcIvjTn22RHJEFbdXuRfKZAOq3u5MHJtaFcvv7gi7HMVDmoQcKr1ZVpq0yROVOs49HdVqwOZS5S8Z1zlbgHmuZ4SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=syIhDdp085Rc0ziDahZ6j4Fr2Nh-riCaDB2LPFeJ2ognWIrWnyjoO95Muj3f8ZvtPHettxd7W7IOElxdB-pjSJfKSVzahSE4xOEmg4CpFXgV73rrfh6dWCmYCOAxXs1vSpypcnKeYwVR7WOSU9lWP6DdbMrjpZTJWJb3UYk5R5nbKPltMrlwQPlHJrdFfMUNDIWExgIrbHDoJM7sYIFw-gqp8Wy8tCJqCrfeLeFGXPIxnl4NNiCiFAJWbtEMHBWMdU4iYWaCm81KVQVavJDsBWyOPaKzNQOWyMPyJD6AESbDDMJHJLwblDQu4CWQ--MVq0JX9eY4PhbY1YBZJjnWpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=syIhDdp085Rc0ziDahZ6j4Fr2Nh-riCaDB2LPFeJ2ognWIrWnyjoO95Muj3f8ZvtPHettxd7W7IOElxdB-pjSJfKSVzahSE4xOEmg4CpFXgV73rrfh6dWCmYCOAxXs1vSpypcnKeYwVR7WOSU9lWP6DdbMrjpZTJWJb3UYk5R5nbKPltMrlwQPlHJrdFfMUNDIWExgIrbHDoJM7sYIFw-gqp8Wy8tCJqCrfeLeFGXPIxnl4NNiCiFAJWbtEMHBWMdU4iYWaCm81KVQVavJDsBWyOPaKzNQOWyMPyJD6AESbDDMJHJLwblDQu4CWQ--MVq0JX9eY4PhbY1YBZJjnWpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=je3Ui40tmeV9tZOoZLwL2ylx_y4VT5PPegB51itGr8SuBGJddEioSS38p0lQkGKo9ocKRlF1dRDTq5bg73qqLGEu48VYjML6gSdSjA96qErRTctOzyjNV68HYXddoepgf_rTgl71May5qsX_pSxekCkY2hua-V6y1ym1jjzxO34QdOM94t8Gb-xxJb7UKi7s7lveGAhfvWpFTD7M8iwGHzYDq3EK6ZxQXFu7Sokhv53rJ-zmkDTxGRXSbMoOTRLKotk-RYWrKNsHvSm5pM4j4g5M5kNxHWnh5iEfcP3jQgg9TeYPENTN0Fbgo0VWs5yQ7vWgCaHGMf0rCtIqspHDag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=je3Ui40tmeV9tZOoZLwL2ylx_y4VT5PPegB51itGr8SuBGJddEioSS38p0lQkGKo9ocKRlF1dRDTq5bg73qqLGEu48VYjML6gSdSjA96qErRTctOzyjNV68HYXddoepgf_rTgl71May5qsX_pSxekCkY2hua-V6y1ym1jjzxO34QdOM94t8Gb-xxJb7UKi7s7lveGAhfvWpFTD7M8iwGHzYDq3EK6ZxQXFu7Sokhv53rJ-zmkDTxGRXSbMoOTRLKotk-RYWrKNsHvSm5pM4j4g5M5kNxHWnh5iEfcP3jQgg9TeYPENTN0Fbgo0VWs5yQ7vWgCaHGMf0rCtIqspHDag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=AD5WEH0T3gnYwN-0ZADN2cAattpXZT1_RmKxzFRHW3Y9FM7tiAOw3ZDdaVIG4pGjbVudcZHJTmr7SGTElEGEDV4Hswdp9y_ml728qaPCjR7gsUEFdQDtG8p4Vrjpi8Ofnf3DMGs1rbsqx-h7t-Ho4bwUaS3ijoE-O0uMian9W1_FcP9oz1m8tik5uIFCkaFMwwoMomuGtD5egQxKZ8LURxfns56tXOkxKlA3TwTidIYokjOXN4z31IX1XkFBmtEKdXH_vh8blL-8nn8lFrqV0sYxZ61k7vrHiQ29G2ShxKyXZ_I8kiuZhuV08Cf_b3bcC6o2UAwQI0vwousGljOtdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=AD5WEH0T3gnYwN-0ZADN2cAattpXZT1_RmKxzFRHW3Y9FM7tiAOw3ZDdaVIG4pGjbVudcZHJTmr7SGTElEGEDV4Hswdp9y_ml728qaPCjR7gsUEFdQDtG8p4Vrjpi8Ofnf3DMGs1rbsqx-h7t-Ho4bwUaS3ijoE-O0uMian9W1_FcP9oz1m8tik5uIFCkaFMwwoMomuGtD5egQxKZ8LURxfns56tXOkxKlA3TwTidIYokjOXN4z31IX1XkFBmtEKdXH_vh8blL-8nn8lFrqV0sYxZ61k7vrHiQ29G2ShxKyXZ_I8kiuZhuV08Cf_b3bcC6o2UAwQI0vwousGljOtdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ro6c77GAPONtraIATqLNoSTawDU1Vtq19oK9gDZ9iPRDd0AHhtGfo-9tZKaUIY7Rop7vi-gY_DQo8rVQXC515ks13aI8UywGG4EGh1abjsR8NaD8L_W2e0dSkGv12P5q_CwcvTYQT2d6HaAr1xMPwDW1CL0QVUp2fjRNl5WTvUKrbm-dewVn9Q67C7z7dM6NlDIgwEeafORlDObW50EBei4lGJhCMGEtya15vdTQd06ZXCUUiJJtKK7FGfqI0wLmnPyoEz69ALaFFlWuqKbNLYCWb1oGLzB1z_T2ZzkfZKN9D6PNvWFjaWoytSaa0KNHdh3H7u0IokSuPu3kgrn0eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNSYgMU1zjsNcV52IUePGCqlCy5cLzoKEgX512skKHvMHVE9Lm3xxeuTQK0ErtnQuLlQ-LrcjeKO9Znja2VTF27j5mn4bxDhe3RV6dzYx_0X_eCnJMJjs-mKXQCcXy4cznMGIi-5TWkzl0V5LlO9ESyTjrAe8whlQi3o-UeyJabO6IsOEqQs5Nq3xBcCJYFe2SuR9_Rqmu4umbzbF0tkJwovTHVg5R0U7CkQJ_a-wu-5Smor815fSJ5LGWyW7G8ngcpf2B16zJNVbqbuWH2HBCnd49BO2MPvc8go-dsCMogh1IZQCf06kX3CoeIu0E1Nj-Q9QTyQPtAIf1VCoqyLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Et42kft25bKLbC_5pw21dH9ubnAPcmOMv2j21M2cDcC3mTWP1PFr79tN86Qi_rAC96I1G88d-eR53dEXG86xbyQI-Fu_JNiFj0EFXCGIjuySx0q_YipGoqgsOxYogJ6suhDQPGZFBa-JOGwzxFY6XUKzLkeG3zE-Br2VOsYyNnLjjCfEwgK4NZiP9AoIbTn01vG2iqIHJKPPSuXJ3BYScLU_-KqfFJlTK9S1sVTDXGcgtS0MKvfvvrESJVYn_IS24x65BWev5mwOzmd-FyM71LGtqNfRrxaj6mF8zxHSFxE3ebxI1D5MOKfPVU2lNua5rZL2fx3KHM0Dtu6ZW9-Q_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=swBeOnmlIb8WmvZ_UzUBaVoVXtviGiywJt2dzPDpetOLl6ObECitVoRt9i9PRAbu_bX3V2vlR5aQmQWXlEsuRG_6GSMl_KKZoWm72afljLRK9qOm48Kyx963dTKiVbl4XtpD29aqq3M35vrvi6sl4D3PgJ7HHPAfRANoW-IYghtvuYA7Jr7UKwnAcgbCsCUdZNm4DsD25CuSp3kY5zbeeV1CDFa0TCWsbRVNC-yhL1gViOk8WPPAsj3uDn3n8UnE4-xH30IAYEyoR75D3ziM55uqzvZQlnXR-i1A7dkpf8W43nzB0VGVdizwL7pu8x-dKNc1f_c_9L40WvrmGn5ypQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=swBeOnmlIb8WmvZ_UzUBaVoVXtviGiywJt2dzPDpetOLl6ObECitVoRt9i9PRAbu_bX3V2vlR5aQmQWXlEsuRG_6GSMl_KKZoWm72afljLRK9qOm48Kyx963dTKiVbl4XtpD29aqq3M35vrvi6sl4D3PgJ7HHPAfRANoW-IYghtvuYA7Jr7UKwnAcgbCsCUdZNm4DsD25CuSp3kY5zbeeV1CDFa0TCWsbRVNC-yhL1gViOk8WPPAsj3uDn3n8UnE4-xH30IAYEyoR75D3ziM55uqzvZQlnXR-i1A7dkpf8W43nzB0VGVdizwL7pu8x-dKNc1f_c_9L40WvrmGn5ypQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
ارتش اسرائیل در نبطیه الفوقا به افرادی مسلح که در نزدیکی نیروهای این کشور شناسایی شده بودند حمله کرد. بر اساس گزارش‌ها، ۲ نفر کشته و ۲ نفر دیگر زخمی شدند. این نخستین حمله ارتش اسرائیل به لبنان پس از ۳ شبانه روز بدون هیچ حمله‌ای در این جبهه محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=oADzoZWm4Y5GnF7Tlz24QcXIRLtqh71mkONBo6LHFkGSSmuQKZZ-oAcHOlEL_qjxKVzekZVv1Ogs9HKTG-PBUYttVEzxJpm4ydVn64lfbQxyekhXbdRCFvEZaQfk8rQ-KB5KW86KCJxqCUPK6rmMCApFfv0bTkny70Lk4oOmqKwst7mqhkkwaZMOkdqp_NLtP46ElWoC91rTwxdz2C1oujM1qhftrI-xebGmycF8oX0NQnHgNqCg2p1EnYF3mr_OQD0UYSjar7MRB0t5hIbmW3ae1NTpVAr3Qzgg8IjJTzCJFoeX0f2gjYnInLW4J0S72Ea_mQg-NrGUBvBpTk7DGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=oADzoZWm4Y5GnF7Tlz24QcXIRLtqh71mkONBo6LHFkGSSmuQKZZ-oAcHOlEL_qjxKVzekZVv1Ogs9HKTG-PBUYttVEzxJpm4ydVn64lfbQxyekhXbdRCFvEZaQfk8rQ-KB5KW86KCJxqCUPK6rmMCApFfv0bTkny70Lk4oOmqKwst7mqhkkwaZMOkdqp_NLtP46ElWoC91rTwxdz2C1oujM1qhftrI-xebGmycF8oX0NQnHgNqCg2p1EnYF3mr_OQD0UYSjar7MRB0t5hIbmW3ae1NTpVAr3Qzgg8IjJTzCJFoeX0f2gjYnInLW4J0S72Ea_mQg-NrGUBvBpTk7DGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g239wwwg5edIn08wybVHqCRNCJmx-y0epltk0qbhPXbGnEAkbTM6Eu2a5WkfqJ8kc9B-cJhadu-30wEplFTOy3n68VnD_w7vdoADjKK7-3iddRf2mqg8C3AUbkCg9g1760xjI6WVj1ccF4C_Br51OXewYYltWxE7GseMlAf7kPSP9yuEqEN5CWQReYPANgE8XOXSDf6HVZ4BmHVfmZuvt2UeXRllUGemgsjBpBBYW5AZX1lS4ly5Vlnd-pSLKN3vTWvwtAQu0nS_Ckz6jNRc8w_PLNeFIMcSjzyrfFYM_L6rVrbogA5S1uYkMEA5D-GHh00YPnMXXclAL-wUsX-NYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=lCEcXJ--GxSfNgWUHD_ZuvrjZldYQm6r0-kfNvuPjFTP4ruMbGoY0pu-CEXurGnj0Z6_hMcM3K0P5lcJU0ZmsEHtE1sm7Yp4DUhceNaA1nhuIJzfw3EoFhwNt2HNouFoubxU9FcmA3-wOnjupbiKgYV_IaXrdEb3gXxXGTdVVOyAvjDLtqCzPrALlBewUNpHJVMGc9aMzGEfBjZypHwddADYD-hz2DTLO1fO5yfBtVJbjSQi0po4iKrNrkfc9-rPdwrlHqQ3QN7gMAnY1Mkv_u6b6zLvMH7RxSKRGjpsgV3nJt3XM2tiM1nGv162OgOI5VN863UGGUrq6c2gndKGDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=lCEcXJ--GxSfNgWUHD_ZuvrjZldYQm6r0-kfNvuPjFTP4ruMbGoY0pu-CEXurGnj0Z6_hMcM3K0P5lcJU0ZmsEHtE1sm7Yp4DUhceNaA1nhuIJzfw3EoFhwNt2HNouFoubxU9FcmA3-wOnjupbiKgYV_IaXrdEb3gXxXGTdVVOyAvjDLtqCzPrALlBewUNpHJVMGc9aMzGEfBjZypHwddADYD-hz2DTLO1fO5yfBtVJbjSQi0po4iKrNrkfc9-rPdwrlHqQ3QN7gMAnY1Mkv_u6b6zLvMH7RxSKRGjpsgV3nJt3XM2tiM1nGv162OgOI5VN863UGGUrq6c2gndKGDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=iU-Zlyna17xNRy-Iz2-9SxUICObth_dAuyvINwghBHlgrYoUZh4QP4XqIDJ3zS2dWsob1xjIrm87ub23zOi29PpO8B3X3oQyve4t2UlLmE68v56wC_x2s_qDxdUQ-vXE-_e5lC8yDEMjS4UujGShrrHQQD8de-Onl16q6iVvYV7_H-AIOwUXUhdr77ylzn6nZ55mXp8-H8PErDy3NrcgitCG99zo-2OxR0MAXm2tvTV72jlL7hXe8yYVuNELMOEgURHOjdqF_YwYYadsWusPSb6F6CusHLiSTXbg8fWpdmyKM-AUBi7o9q_nRUdPDyFNETP5Ss124DHm3n5iIcsV7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=iU-Zlyna17xNRy-Iz2-9SxUICObth_dAuyvINwghBHlgrYoUZh4QP4XqIDJ3zS2dWsob1xjIrm87ub23zOi29PpO8B3X3oQyve4t2UlLmE68v56wC_x2s_qDxdUQ-vXE-_e5lC8yDEMjS4UujGShrrHQQD8de-Onl16q6iVvYV7_H-AIOwUXUhdr77ylzn6nZ55mXp8-H8PErDy3NrcgitCG99zo-2OxR0MAXm2tvTV72jlL7hXe8yYVuNELMOEgURHOjdqF_YwYYadsWusPSb6F6CusHLiSTXbg8fWpdmyKM-AUBi7o9q_nRUdPDyFNETP5Ss124DHm3n5iIcsV7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=hJQXj6DGeRExKNRjse-Oy_s8vDKOlD9rPDQdyxCyxWNDP18gqdQFmzV781MZl7B2q4_X1ARZvcxak9i7RSn1pGcG8br27TtjAxzOKqS84FJ2-SNJFans2k8sBZ74QLhDbR2VFYVuL2xw70cCQIvF4KIOYIE21-SO7XeCQfobgH7vprsikBzwhLYmmln5emWSXiTiY8_2Lj2kVa5iq-dALid__3c382kJs5MLqsX8pK7LNLkLbGJY1shckSqvUia7ZBHlRULSc4aKv_03Qjza5sUI9-wySCfzwb9jpa0fjrPHUtStsPvb0ZUbuUuImJptoxqQ0IdKV9XDRRSigPls5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=hJQXj6DGeRExKNRjse-Oy_s8vDKOlD9rPDQdyxCyxWNDP18gqdQFmzV781MZl7B2q4_X1ARZvcxak9i7RSn1pGcG8br27TtjAxzOKqS84FJ2-SNJFans2k8sBZ74QLhDbR2VFYVuL2xw70cCQIvF4KIOYIE21-SO7XeCQfobgH7vprsikBzwhLYmmln5emWSXiTiY8_2Lj2kVa5iq-dALid__3c382kJs5MLqsX8pK7LNLkLbGJY1shckSqvUia7ZBHlRULSc4aKv_03Qjza5sUI9-wySCfzwb9jpa0fjrPHUtStsPvb0ZUbuUuImJptoxqQ0IdKV9XDRRSigPls5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=BlsbRQPkFd-UzZHbEc_qslyaumytCaBcQML8B99twB8YF2PeZiycrBxokTjAGSM-18MXNY7cDKBHf3OtOif2_KXC4NPxJWnE09Q0Izv4iAOdhO4oIRuJ9TIrnjzzrjmvkUpuGXr9UhgStIC0RKBK8tuuo2fsp1To00v0eTzRQjJPOhdxb4ydcN-yc2Rh0joOWgV-CBrhMFfEy4s8eHi0I3B3DMF0o99x-8yt-52ZU-MuZisXFbYHRuJb2UnpkcAkMW6QznTgCvSkHvsOMUD8FQoCbN8Ta2YjMzK5eMmP-gZi0qhIb-q5JJTktBVIOfPbt0ho1nP_ynndWKIeuhxJtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=BlsbRQPkFd-UzZHbEc_qslyaumytCaBcQML8B99twB8YF2PeZiycrBxokTjAGSM-18MXNY7cDKBHf3OtOif2_KXC4NPxJWnE09Q0Izv4iAOdhO4oIRuJ9TIrnjzzrjmvkUpuGXr9UhgStIC0RKBK8tuuo2fsp1To00v0eTzRQjJPOhdxb4ydcN-yc2Rh0joOWgV-CBrhMFfEy4s8eHi0I3B3DMF0o99x-8yt-52ZU-MuZisXFbYHRuJb2UnpkcAkMW6QznTgCvSkHvsOMUD8FQoCbN8Ta2YjMzK5eMmP-gZi0qhIb-q5JJTktBVIOfPbt0ho1nP_ynndWKIeuhxJtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=AkFo3zUXF6VUIOBAFcyQGzrPjdaWmJ0VPQO91XU1at2L7XBNoRSypdIy40aqTck5uBbTi-Z5GLCAeD1FZ5OjMKH3uZixs8malS7L2Exkgg_v8OiYUUj5mei6r1ieKnHt7tIpggoB3euGxv4-m0sW9nxcfjtGIfp7vC8sEnEk37_Jp7mCrsFR2fsleemTqLAzHiMImmPeFKP9iCrz6KRJTzmu2pyhJ7APTvoCxvwlePWGjvAA8idzBcN3k-DF0wM6v55KZMOTK61hqt-ucTn2KLLe-1NsptGFZ9DXY906HCjbqZt82zBLRkb8Fpcubyek_9GPpWqvd8e1BrgchB9JCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=AkFo3zUXF6VUIOBAFcyQGzrPjdaWmJ0VPQO91XU1at2L7XBNoRSypdIy40aqTck5uBbTi-Z5GLCAeD1FZ5OjMKH3uZixs8malS7L2Exkgg_v8OiYUUj5mei6r1ieKnHt7tIpggoB3euGxv4-m0sW9nxcfjtGIfp7vC8sEnEk37_Jp7mCrsFR2fsleemTqLAzHiMImmPeFKP9iCrz6KRJTzmu2pyhJ7APTvoCxvwlePWGjvAA8idzBcN3k-DF0wM6v55KZMOTK61hqt-ucTn2KLLe-1NsptGFZ9DXY906HCjbqZt82zBLRkb8Fpcubyek_9GPpWqvd8e1BrgchB9JCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=D4CO_THU04yZuZELihi3KJoI8MPnI-uNIsaV5bq_nIX0sC-p7TMx6uo3EHNhx1_1SMGsizqpH3w82nqHCggqq4w63i2LWGjbt3VMSJTyzylMeRN1UhVPdqScZuQItrMUQNjzKKUTrXuiUiM7uj6UiBgcM0suHrZadYgADyjJEHm-y5zwqNIZH8fnZgdrA3bzU9V67ni4_HLa0NIwsWF4yBD33PjTRgBASrFv-XC3qzLj4awDmNmvWuoH4oUCowdqRNM9VWeiZqGIuiy6HC5B170muUqP7b4XauWI0wHOccj-i1flR7pSd2cyNUv5qXv2OG5KjF-b3Hm1fz7VuFhzYj56Juugo1C_5ULDXN0rOWN9EYLwt8RQCJM2wXNuz2rGACZhQSaUkZkn8EziaXkLwvrJRpcEUreQmZGdH5ZgEWGTjhty6jW1cFHnnBiBU2luqosnajAKX34FBwooopttxT8h4dVhd7IWZhsdlv5d0RNletdFGQK5ngGtmCzWxPChNtbXXuV7K0jv2wzJAlDAgbQrxPjW_truDx3yt1TdMS2IrFCRgnGZQ5q4RdNrRAudjkohKVttwACouOCBjPsIzXlewHd35s497HtbBDBGNIPgEkyxTwRpW4g80YIEnGBaU7jbB4o1z6wqWlTpJrKNmVRoPPgazvsrhhGi2k0GKss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=D4CO_THU04yZuZELihi3KJoI8MPnI-uNIsaV5bq_nIX0sC-p7TMx6uo3EHNhx1_1SMGsizqpH3w82nqHCggqq4w63i2LWGjbt3VMSJTyzylMeRN1UhVPdqScZuQItrMUQNjzKKUTrXuiUiM7uj6UiBgcM0suHrZadYgADyjJEHm-y5zwqNIZH8fnZgdrA3bzU9V67ni4_HLa0NIwsWF4yBD33PjTRgBASrFv-XC3qzLj4awDmNmvWuoH4oUCowdqRNM9VWeiZqGIuiy6HC5B170muUqP7b4XauWI0wHOccj-i1flR7pSd2cyNUv5qXv2OG5KjF-b3Hm1fz7VuFhzYj56Juugo1C_5ULDXN0rOWN9EYLwt8RQCJM2wXNuz2rGACZhQSaUkZkn8EziaXkLwvrJRpcEUreQmZGdH5ZgEWGTjhty6jW1cFHnnBiBU2luqosnajAKX34FBwooopttxT8h4dVhd7IWZhsdlv5d0RNletdFGQK5ngGtmCzWxPChNtbXXuV7K0jv2wzJAlDAgbQrxPjW_truDx3yt1TdMS2IrFCRgnGZQ5q4RdNrRAudjkohKVttwACouOCBjPsIzXlewHd35s497HtbBDBGNIPgEkyxTwRpW4g80YIEnGBaU7jbB4o1z6wqWlTpJrKNmVRoPPgazvsrhhGi2k0GKss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=cwL0OMvbge_UAhT1s2lGZeP38-Wk8YRIoznhZMyI5x9TCM4PiGiU1cjnASJyiPHp_07Y8s8tzFXrVvkazzJM3geiaVChYSYalXFMaOe3mtSehuD6I-FjTxX5msgfwgLmMeLZTazRUZtgCc1bmvEd0vMRm81ZKoUOuULlxIo0_QYeIfbMSdjm4ecBqmICtVoNVAn3ZFEtlPIVmNKDMDUa8cY0FlHcf9Zbqm5bWPlU2rjZJZRfWwBrYf-RfpleLcrxhGUexEirvCU587nmL0R1lDaTiM6sM-iYKRX_lahR0wX6MA3D_Y2CkO3n-Jf1zGmZ6xTm8bbI18WtX7yrFAWITw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=cwL0OMvbge_UAhT1s2lGZeP38-Wk8YRIoznhZMyI5x9TCM4PiGiU1cjnASJyiPHp_07Y8s8tzFXrVvkazzJM3geiaVChYSYalXFMaOe3mtSehuD6I-FjTxX5msgfwgLmMeLZTazRUZtgCc1bmvEd0vMRm81ZKoUOuULlxIo0_QYeIfbMSdjm4ecBqmICtVoNVAn3ZFEtlPIVmNKDMDUa8cY0FlHcf9Zbqm5bWPlU2rjZJZRfWwBrYf-RfpleLcrxhGUexEirvCU587nmL0R1lDaTiM6sM-iYKRX_lahR0wX6MA3D_Y2CkO3n-Jf1zGmZ6xTm8bbI18WtX7yrFAWITw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شهبازی، مجری مفعول صداوسیما:
طبق تفاهم جمهوری اسلامی و آمریکا؛ از این به بعد شعار «مرگ بر آمریکا» ممنوعه و اگر کسی اینکار رو بکنه دستگیر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=SaEKuHNJdrmYLyKvEWA5fKfnJcX7Pllwns_qQiWJDpfgpARBy5O2yCAz_ytxvFWcLMe4Tf8PDtyURvFgl0Ds9_MJjVdpL9PSdf18NqVStbXPXh8nWVvEs-waCkSocX3Rck6_hmebitWSuzk1sPoyfSlpx9a9_D470CZ5klx2piHx7qBfJviXHxaHmAtWMJ_0xxCXMg-fseNGRcD-CUwgKuBLpiG8LTwC6jATlk26eb7EAQ_n__UO8qP46ff93GrtkcjENX5CAUohVrHqTm354t9JyPiuQAoUvkIBm8LdBu8QWJ8j1drS9JIvftY-XLwSgBKwV-UVdC8WfiUjtr_gNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=SaEKuHNJdrmYLyKvEWA5fKfnJcX7Pllwns_qQiWJDpfgpARBy5O2yCAz_ytxvFWcLMe4Tf8PDtyURvFgl0Ds9_MJjVdpL9PSdf18NqVStbXPXh8nWVvEs-waCkSocX3Rck6_hmebitWSuzk1sPoyfSlpx9a9_D470CZ5klx2piHx7qBfJviXHxaHmAtWMJ_0xxCXMg-fseNGRcD-CUwgKuBLpiG8LTwC6jATlk26eb7EAQ_n__UO8qP46ff93GrtkcjENX5CAUohVrHqTm354t9JyPiuQAoUvkIBm8LdBu8QWJ8j1drS9JIvftY-XLwSgBKwV-UVdC8WfiUjtr_gNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YQ6Ld2uGlXRYd328QpLgTJD08tPgv6dbz-TO_ssdZebbWeEk25nOzPRATA2omyOdycMvLNVXG4xQUKMIds0910kp76FCs8so-2zhui5TcBWBswi1-2QqXKZOwJZ07spyiiVoQXdNTPPwrZlf2HddLzeeLN1wx45Dt8JLRL_9myLnPk3IAW3dpVLi_A9Bl7fFmZ6_XLdoR4i1KF8qpEJ3T5b_BiDZafjc_MMlgTOqUAB-MQbxioCWzm2FZvcznOE_twCTedTkX2s8g-CVl6wjlT4HfGGWzVfgANnk2246mijIIQvKM8FhfcYhCEatKRRW08iSNwfDS-ZiB0Jw8FLx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=VVmVD0PwRQDZ42K4_oklv8umRx_K6rMoWKKVYv6MLcaovq-6K6ImECp9BwiFtk5uzlo1LmeqjKjxVrOiGkBoHwe7B9-217D3ZiDgvyT8kX2iTcq97OLSWNjxDp03secIMHLcXdiwFcjzfT8D3W7cYdz819VOsI8U3Z9GwULwtXyPG5FugtN2jOVn9IttE-dNSAOdsnH-gFMzSVGulLzBiAA5GwzDZ-wg9b_oyTGTd6E07xISwZkgTS1igkw3Vx5Ssvzy84nIYY7Aa7f_tCsAHxg72vSWzlDDImHzgyIMLc12DJt8EdtzWNoBHJUqgNcrgzG05DkrUdOQhy5Nk39pxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=VVmVD0PwRQDZ42K4_oklv8umRx_K6rMoWKKVYv6MLcaovq-6K6ImECp9BwiFtk5uzlo1LmeqjKjxVrOiGkBoHwe7B9-217D3ZiDgvyT8kX2iTcq97OLSWNjxDp03secIMHLcXdiwFcjzfT8D3W7cYdz819VOsI8U3Z9GwULwtXyPG5FugtN2jOVn9IttE-dNSAOdsnH-gFMzSVGulLzBiAA5GwzDZ-wg9b_oyTGTd6E07xISwZkgTS1igkw3Vx5Ssvzy84nIYY7Aa7f_tCsAHxg72vSWzlDDImHzgyIMLc12DJt8EdtzWNoBHJUqgNcrgzG05DkrUdOQhy5Nk39pxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=akgH1WaN2tksqVycY0XK4Ti1eXxPGM12JrfbCd94ijvgkUgQreQ0ZtoCjRIwWTU3aA6kgUye941mU963RZsWfbYcgOmK8Bh9CbkG3IAQKRh5ANO-2flH8MV9q54gXhY2LjAc__t-4tsusdTShQL9T0N_VwoGz9fgzmxPz1xFL0m4kBwvJZ58pEY860z51sbxiN3gmtmNZAM4oL8OMLL_Thp4UyMB55kWR1y_zYdAxCyFI9JLikiE4GeL6KbWy4w-Fhv5ahUGlZjb8REKiQjmHVlh1Tk1-1Kk796sZ6v0APLlmUl8lTXS5LBeXQ_vUgzXh5pxO2fngRPXkLKekJB7Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=akgH1WaN2tksqVycY0XK4Ti1eXxPGM12JrfbCd94ijvgkUgQreQ0ZtoCjRIwWTU3aA6kgUye941mU963RZsWfbYcgOmK8Bh9CbkG3IAQKRh5ANO-2flH8MV9q54gXhY2LjAc__t-4tsusdTShQL9T0N_VwoGz9fgzmxPz1xFL0m4kBwvJZ58pEY860z51sbxiN3gmtmNZAM4oL8OMLL_Thp4UyMB55kWR1y_zYdAxCyFI9JLikiE4GeL6KbWy4w-Fhv5ahUGlZjb8REKiQjmHVlh1Tk1-1Kk796sZ6v0APLlmUl8lTXS5LBeXQ_vUgzXh5pxO2fngRPXkLKekJB7Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: وزارت خزانه‌داری امروز تحریم‌های نفتی ایران را لغو کرد؟
ترامپ: خب، من باید دقیقاً وضعیت را بفهمم. تمام آن پول به صورت خرید مواد غذایی برمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند که نمی‌توانند آنها را سیر کنند.
خبرنگار: مطمئنی ایرانی‌ها از سود حاصل از فروش نفت برای بازسازی ارتش خود استفاده نمی‌کنند؟
ترامپ: قرار نیست آنها این کار را انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tzm2gWYuF0S5QM27uzx6pUgyskzQQWqi9aLBi_2CvtqEHydR_0XBTQUNxSbOAlJFY84ENsHKGU8gUEcwS6h-hLtisVHvukDJwf-3h8SkIqhcqem1vlELrs7703Y_KzhojxhL5K8caNqJoq8dlQwA0jLq_JI7m4KdKsuQcNp_dZqr1Ap-ITRaVjzboqsi_eAd-B_mpP2miPzcQlPH7QtOH21wxLJN98anjk8M0DXyazD8oADKrRpmIwOONDuavZd-CV7zq0owR-SZ771M7arGU_ScE5vuQH-k1-Flfzrfd37njQmX3nGFdN2sa-vV-eJiRiwEfH1hjt2OG9p4UsI51g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=g4OLJ7cfc_hR9bmqO4WWtC8zCEw0nH1yHV89By4fBfonFRsXmF7tp2nWG9oCkR1JFXZDOO0YGWrMjFTvErOIZjHHJN-1IJW12Q8oEJwdvI-LtdHO0wKoCWSVjMpjk0gAqVU5m-L1uIp4XUqH4PMu1xzN-EnD4xa4CLSI7L5JpkuT5DgdIa45CQlUGQ-QlrbuqGRRYEj6k7owyEDz-vzQJiv_uxfGHZ7i7rMUdR58r7xQtptZPvxGO4980D7v1_K4lLoLtW71eJKCmi2CiL4mNbdUp7CX160KD1BT3qPTVTtslxN8FsqpNdSuqBmvwfjFINGOq6oqo_pqXnbOugwXqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=g4OLJ7cfc_hR9bmqO4WWtC8zCEw0nH1yHV89By4fBfonFRsXmF7tp2nWG9oCkR1JFXZDOO0YGWrMjFTvErOIZjHHJN-1IJW12Q8oEJwdvI-LtdHO0wKoCWSVjMpjk0gAqVU5m-L1uIp4XUqH4PMu1xzN-EnD4xa4CLSI7L5JpkuT5DgdIa45CQlUGQ-QlrbuqGRRYEj6k7owyEDz-vzQJiv_uxfGHZ7i7rMUdR58r7xQtptZPvxGO4980D7v1_K4lLoLtW71eJKCmi2CiL4mNbdUp7CX160KD1BT3qPTVTtslxN8FsqpNdSuqBmvwfjFINGOq6oqo_pqXnbOugwXqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=DenUD83ycaWruiWGXJTeU18b-GrKUk5GsrpbZU2im0-1WQX9IvWvKAK-07LNyGfTbGqRLIyE6tqyHwjrNDeyITW44FP9BF-OW4bambcV25_A-oaOO_3IZpMx8334u3OLW1PbZutSL0tURaw9fdwlDl5DxQklsovoOWqD0SJTQZiV__CqsppHEFlYFhLWbRTL75QLeMF7L0MacWbULJ_WhtsaUC4puSqvTWu55aNbc3uJp80JzdoOSRv3rZxxhQciXRFgG6XRFAIPADKiYBNpPAPefUvXGH_slkjY2eNxlTVooXga72tlSM74XVwJ_27XSbm4i-FY7xZ833AZrs5pew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=DenUD83ycaWruiWGXJTeU18b-GrKUk5GsrpbZU2im0-1WQX9IvWvKAK-07LNyGfTbGqRLIyE6tqyHwjrNDeyITW44FP9BF-OW4bambcV25_A-oaOO_3IZpMx8334u3OLW1PbZutSL0tURaw9fdwlDl5DxQklsovoOWqD0SJTQZiV__CqsppHEFlYFhLWbRTL75QLeMF7L0MacWbULJ_WhtsaUC4puSqvTWu55aNbc3uJp80JzdoOSRv3rZxxhQciXRFgG6XRFAIPADKiYBNpPAPefUvXGH_slkjY2eNxlTVooXga72tlSM74XVwJ_27XSbm4i-FY7xZ833AZrs5pew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=bg6iJD1p9KTD8kyr4QJ0oNTxIa-YQcMjCqtWPze5tXCmHAs08rm0QJHb3frA9OVrSbRB53YO5o5hSOBC5VaIfEc1psijxZoyAlwYJv8pxrX7xRUVj0JPEKAs5yhPRfpfIWJzqSfH1aAG56wki_4Vvax6lEcjrrFlcCmyblgycNnTLGnt8nXhl1PpTw2_0ihiQG_v1ZkX4kkH8f2xXQV921Bp1QXrli4cpfu6db9814NzFryCUOmlflZ-XowoxH2mBykWuxZSQLQP1LFfA0vE2fX_AueCFfgCKJgkEAau0Q4tmL2PawuYYzRv3CYOAcccBRP0deH4zf_MQqvQ7T9jOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=bg6iJD1p9KTD8kyr4QJ0oNTxIa-YQcMjCqtWPze5tXCmHAs08rm0QJHb3frA9OVrSbRB53YO5o5hSOBC5VaIfEc1psijxZoyAlwYJv8pxrX7xRUVj0JPEKAs5yhPRfpfIWJzqSfH1aAG56wki_4Vvax6lEcjrrFlcCmyblgycNnTLGnt8nXhl1PpTw2_0ihiQG_v1ZkX4kkH8f2xXQV921Bp1QXrli4cpfu6db9814NzFryCUOmlflZ-XowoxH2mBykWuxZSQLQP1LFfA0vE2fX_AueCFfgCKJgkEAau0Q4tmL2PawuYYzRv3CYOAcccBRP0deH4zf_MQqvQ7T9jOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=dkgLVs1nDq7ty8UsTPZSxQgvrPAxkc-ntqm2TQIfTJacT3Ur4bOj14X-u0B2X70MnUMFz9fMrztnYpimgylrMszDR6D6aLkOVVtYF4Bnvud86AbCw9vcmtFRv2AAJ8DYxLPV72Jph8Eg3040-Rwi4J70OeXG1WqRfMEoMYCP1NftLTDq_UHwxO32TyBzylCd3pgzIm4YAldkN57N0kjkEnXCvGtzamCXZ1HZoFW_S3XFhgxFUXIZQSJL3vM3RDKKNYimo0HhR3oKkfOhp8vKtqIuz7fzqMOHuKgzbm_h-N0MMM6KREhLKnDjJxbJ5YTMPcXLhz6VRnNPppEVgsBPlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=dkgLVs1nDq7ty8UsTPZSxQgvrPAxkc-ntqm2TQIfTJacT3Ur4bOj14X-u0B2X70MnUMFz9fMrztnYpimgylrMszDR6D6aLkOVVtYF4Bnvud86AbCw9vcmtFRv2AAJ8DYxLPV72Jph8Eg3040-Rwi4J70OeXG1WqRfMEoMYCP1NftLTDq_UHwxO32TyBzylCd3pgzIm4YAldkN57N0kjkEnXCvGtzamCXZ1HZoFW_S3XFhgxFUXIZQSJL3vM3RDKKNYimo0HhR3oKkfOhp8vKtqIuz7fzqMOHuKgzbm_h-N0MMM6KREhLKnDjJxbJ5YTMPcXLhz6VRnNPppEVgsBPlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=LnQRFjinET9QeT-c89iDHJ99ReebiuKlaWtqUdgvAfuKzstm6Zwnu5D2ggyvv-C4pkI_KlLqDKoKMzvYLWfLlzX63oXpSgWp0HgCcFsM6TT2rj52_2tMKY4GsdtDpOOTRtb5qyvV54e7AE8yPFDjSk2pNjQW_2sYUBdfo4aWHIgq7rtmwi-LDY718Oo4r4tIJ3iscoUyg-J1cpKM8AQ-Qx_0uZcZBuHUIiMxLLcBAcjw6IZ9C3Q_R53adHJSdxRB849B8rQy-zcGPB4en7GwK6Z9LGHZFYzOZZ0IEIVS8wqAmbJI7N9CSi25fOvPw0SHKBg6Crz6NZhDkeIOtti1ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=LnQRFjinET9QeT-c89iDHJ99ReebiuKlaWtqUdgvAfuKzstm6Zwnu5D2ggyvv-C4pkI_KlLqDKoKMzvYLWfLlzX63oXpSgWp0HgCcFsM6TT2rj52_2tMKY4GsdtDpOOTRtb5qyvV54e7AE8yPFDjSk2pNjQW_2sYUBdfo4aWHIgq7rtmwi-LDY718Oo4r4tIJ3iscoUyg-J1cpKM8AQ-Qx_0uZcZBuHUIiMxLLcBAcjw6IZ9C3Q_R53adHJSdxRB849B8rQy-zcGPB4en7GwK6Z9LGHZFYzOZZ0IEIVS8wqAmbJI7N9CSi25fOvPw0SHKBg6Crz6NZhDkeIOtti1ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صداوسیما:
نه تنها از کشتی ها در این شصت روز عوارض نمیگیریم بلکه قراره آمریکایی ها بعد شصت روز بیان و عوارض بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uasxq80pKhW3eNrnR7_sioD9fOnK4yHbWcX4VslOLDppI7jD2RXb0q1Yfx8RAU8qcuyP4_6R1y6FxUXvslyit3Mt-rnXEqR7doCl9EvXa0WagXQgcNsnXw9nl5Z0vD5NPI8Xl_tKSdeoiyKHQzeQKn-UplniT1iSGVYc4dgGihUXPHa2Gt5Sv39sbkW2bGBNzcVl-i9U5i8aknjIz4sBmWUT8SsmWfZYtJjrvOVP3nvGePjGQ-mBZUPk4L1g-1nwVl_f_XeiJrGkJjaFjd709SUlttLfp3eNhYnWHbLtrO_e3RZ6Rf5TAC9X_rxbz7RPyAYEWptGmXQw2KZeO1BqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J29G6djGa7Vhg7KDaYCphn5gED-Ukgq3Wh5PwGeE098lhohjN-XFUlY3YE1eT3XOPGPvvXyXVvJ_zAUAPphNF0mYLF6vcb1h3qpzbklXc_d07h2K-V4ml37b0AsycS5y2PYA-KfywehEwUqMr3BOKB78_x6ahNUfMgrqFK3CTvxFup_O5XljjFC0Vl0Nmk7qJ5oYL8EtuMGkT0c_Sk8MkYkAjxpcgwrwJO-bKL4_8nNvmOVAEChizNhcf3ZUmKfAAWd8fkAt4b1MnLNYkmXIco73ZcpUfx5FNEAMhDJStWtn9Z0wfRg-vN4PMS87cq85u0I0oksApYVljrrfRJV9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSSi5PUzqdI3ds9Nbo5tsJsF-x-FWu1nBISUcFprcM3zx-8zcVNXvb5-aqm9ONN--b6UBUxFjxgNm9ZLkfvYGsjRUZY0QJECozmfHjyyAKkd3J9Dt0pLskjAOQVzGlJCsEmrQMMYydPQ-JRK4ztb50rCZBQmgWgHWxVyjU5SmUYt3H6nqVXsxJzVg_oDRK-rK6wjh9Qp__7qQ6ryLszxIk9EdgCylUIAILQx9TYScjoWVirvP1hdAKyp5Nwj5ghs9QfY_VxdRm747BXYxZ1a8R2usBjctrE8QcLh6pXmLuKCsnEsnEz90YW_zPHVh4t2XHzaGKkIYltQakp5vt14cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tu7pIiiOLlCyBcYpVsETyazm0bsZvpomJSf1s0__bTK942cuKYVWp3T9ZYggUeNwsmHKXlp0cWklCrL7FIyCccWBuB7mHLLRc2bqfYCz9xFgEha2AIBWxmpCvCGfMOPWo89xzi61bYAHIWwldgu4-AyXFPjCd7jYlzV6_AnKUc8fgbhKcSNKLuI0bFWeiB9cZS4d54dC1lAeszOzvtODn9sp6xVubic0H0JaK6Ux2ko6_XIdac93sXHFW2zfh2RfGCRdXE924k78Wjc60Z5Cwwqjs-WvilYH6r9MNuZS1xKBCiCm3jcGhpky5WXCYJOZQA4eNA_0u23-n2_iuPtEWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iriI7bkkvzJTkeX0aK9XIvpY8NF4LcDK5AOCTgLb0v3f0Q_5w-VXwrfx44cbo1Ypcz4PgKhM65j8gVbMJbbXraua_dtaigHJ7hobPnADGh4NLYmsEHYS0vg3AdQCm1mHIqoN_lr_6OoHhwnNgGBMw72kFjsmZQK2--j6w-ggp-b3mmByhvUhD8NZuiC6ZlAvnvoiJYbu7VOssNUoRLLlT_lcKt5c9UQifVAjYjMmrzPaHRJ_uFeYFaIWkGNB5qzitcd2tMc0hfLpQszEvnRpvsk9uf6CP5cLhDLQhY5Mn1P6k5d2zH2sJI2pJfVqVjDn6Yg8aDrvEHNbx0zqX9ulsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMh0MDToakTnFUpQMMzYFMjX-ZWSHtyESqShLmMGFDeFv4ZzqZUEDoZfO-B-rlI1ZWQLadtujgDVv4C9tVrB0hXRjHUOK4T5s5wEIkJw-AkR4-OvMN3caEFZNGirkAfNB-PF2VkOZ9QIyrIUXKoic-TbBfBAAj2SMwVs7p5DWeS0cDRCkT-GJ73N1gS9i7PGJBa9Cw2vflUjZRkVqqqylDi6KnltSNCS58FWRSM-AG-wnVOaep2u8sTGbRraogh7FFDaqWYf6ugfKZaNzwXYO27NGqAV6Ah57n0WjnL6TBFI41Ed9Z6HHqIq79IG1c-4SVbTUwFJ9jnA07NIYSzgBcFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMh0MDToakTnFUpQMMzYFMjX-ZWSHtyESqShLmMGFDeFv4ZzqZUEDoZfO-B-rlI1ZWQLadtujgDVv4C9tVrB0hXRjHUOK4T5s5wEIkJw-AkR4-OvMN3caEFZNGirkAfNB-PF2VkOZ9QIyrIUXKoic-TbBfBAAj2SMwVs7p5DWeS0cDRCkT-GJ73N1gS9i7PGJBa9Cw2vflUjZRkVqqqylDi6KnltSNCS58FWRSM-AG-wnVOaep2u8sTGbRraogh7FFDaqWYf6ugfKZaNzwXYO27NGqAV6Ah57n0WjnL6TBFI41Ed9Z6HHqIq79IG1c-4SVbTUwFJ9jnA07NIYSzgBcFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=r-zPNLHvgRD45c_PJjwgdeE-HSbbwhlvdtUIZ2t6Nu9cSdRvMFzai2LKZDrux0MswsqnsdB7LBKmLDlH8NylyfG4wu5L8qUXQabL7aqmv485qOjHVtha4hmReI7PHbGHD-QKGNESq2mkkR7iZvfjMmjtg2ER5Mv6KIaQk-WSaKT0fbe7oOGLYWI8Ii0t6GVDhsqDKuzR-XbwA8UiWYmMRf_9m0gKh8JXgZJj-g2aZfr6J89KGLcAHCPhAC193O7c9XPzISo1gDHR3sLT-1GHzqfxHoC8FgIjDgI0ubbLjhKtNLP8_oE2DWsOXe15sbvFNmwB7_qxf4KsTx337JG0ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=r-zPNLHvgRD45c_PJjwgdeE-HSbbwhlvdtUIZ2t6Nu9cSdRvMFzai2LKZDrux0MswsqnsdB7LBKmLDlH8NylyfG4wu5L8qUXQabL7aqmv485qOjHVtha4hmReI7PHbGHD-QKGNESq2mkkR7iZvfjMmjtg2ER5Mv6KIaQk-WSaKT0fbe7oOGLYWI8Ii0t6GVDhsqDKuzR-XbwA8UiWYmMRf_9m0gKh8JXgZJj-g2aZfr6J89KGLcAHCPhAC193O7c9XPzISo1gDHR3sLT-1GHzqfxHoC8FgIjDgI0ubbLjhKtNLP8_oE2DWsOXe15sbvFNmwB7_qxf4KsTx337JG0ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=BOl00_FklPOHM3T1K8QrAk_Ls3afrEJ2GOZXDc8jbn04ov53q5AZJRQ2pyeem8bOf4AIywG22qD_BKAtp9ckpftUzIOqV19hYTi95gthJdkiuEUqxPQ9F3p-wEkJnpMjWjEOYKIyO0TCu_f7kE3O_EmYp42z19qavaKWM3c7DJElRw-DUDfYatnuOZamgS9kPpBKEykgml6ANu9pA-xV7kBHuM3qsJLx2YN66ziivcxfowhHmXKXrD-SI5v4ldmQ5CHekBYHx_5bpemH-Y0LcEoBXLtG_I0O6S_donPjfooT1hY_-yeUVKuMaSgGIIR5EXXlcIiRDy7jFkZU09L8pDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=BOl00_FklPOHM3T1K8QrAk_Ls3afrEJ2GOZXDc8jbn04ov53q5AZJRQ2pyeem8bOf4AIywG22qD_BKAtp9ckpftUzIOqV19hYTi95gthJdkiuEUqxPQ9F3p-wEkJnpMjWjEOYKIyO0TCu_f7kE3O_EmYp42z19qavaKWM3c7DJElRw-DUDfYatnuOZamgS9kPpBKEykgml6ANu9pA-xV7kBHuM3qsJLx2YN66ziivcxfowhHmXKXrD-SI5v4ldmQ5CHekBYHx_5bpemH-Y0LcEoBXLtG_I0O6S_donPjfooT1hY_-yeUVKuMaSgGIIR5EXXlcIiRDy7jFkZU09L8pDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=aTsjU_G8bgp4xq99QhuoN0fa_-7r5irS53LDr5Cz6u_UcdTErehUKb2NZKt6-XonSIpeuqprd5Xyn2bs9KO7EwT1V4vQqrm7aZ2-x8OZ6QPoG5Y-E0-psd4mBuas7xQKFi5VkicjouXQlHY67uyedRQ8M1mH7XbQlRBfysqydsQcstCzhxA8CUFspBK5vtoBko8JQD_BtFkFgvGFaB0CecB7wOF7-YNv_TJHAqPezGpP3MrUHyNG7PFVr-Ors5mhTrtaRu0ep9DzLEkAA13Fh211wBHtRYEysKINzu2DVfXA1wLOnYUHzw_5PvKMtFAzlVDa4CgIAjWJX4h3K8aCpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=aTsjU_G8bgp4xq99QhuoN0fa_-7r5irS53LDr5Cz6u_UcdTErehUKb2NZKt6-XonSIpeuqprd5Xyn2bs9KO7EwT1V4vQqrm7aZ2-x8OZ6QPoG5Y-E0-psd4mBuas7xQKFi5VkicjouXQlHY67uyedRQ8M1mH7XbQlRBfysqydsQcstCzhxA8CUFspBK5vtoBko8JQD_BtFkFgvGFaB0CecB7wOF7-YNv_TJHAqPezGpP3MrUHyNG7PFVr-Ors5mhTrtaRu0ep9DzLEkAA13Fh211wBHtRYEysKINzu2DVfXA1wLOnYUHzw_5PvKMtFAzlVDa4CgIAjWJX4h3K8aCpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuzxRrhGzc7UFwK7LU7tAXFMF6-N0wqcvQM3c-su71BhdghvqRTMjImYBVcgtaZVwtmhA880sWFYBEb6BSxerf7f-RvGvoO1LUsVt5wNtb_Ho6jXxX4itLOwmkAa3dqolYy7vmqgD-keezy-CvhakrvdHKXYOPvfUyPh0r04BgQ4jvPOkRvBPrjnBs3lMBa7qUR8uPiZQeFGpqJ7SunEQPh5DAEX0gyG-QRkQnQkDZTKoTkqeJTacgfTJPunNtZJt_LFmaWeUx9ltSbRLgovKKhXt3uk-j13tnFOIezQUpaqoqywenMqonBZbK4PqixXKsJpydfrwbH-maa_kgND0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=qBU2NukyUAa9lqKRbtUPqaugF1Twn_OMbbgcF-YMGpn-b88dCWcZpYP7SjuFY6iwHsxh4OTJWCa3dG7GIjm246azSdT4l4pDdJVSGMFkoertg8TxoHrKTbWk2Mmrj4HF_7d_YSHt3rNzjvGJxUE0W90I1oLSUmxgV8Brv5RH9S1ewjWj0k5g9n1zWT42Qfeeo8yYhq3O6dcl0RQdIo4yDpwa0wRGlznVpTTN3tQKpIt50qHzIfVe8HPucZDQA8c2ykBMSuoA4R9llV0Ftx6McGWyvyWNytm-xiAcT2j7yQ2AMeXOTDsjQSJukHhSHH95KdYcNDnY7vyB8QXY_MU2UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=qBU2NukyUAa9lqKRbtUPqaugF1Twn_OMbbgcF-YMGpn-b88dCWcZpYP7SjuFY6iwHsxh4OTJWCa3dG7GIjm246azSdT4l4pDdJVSGMFkoertg8TxoHrKTbWk2Mmrj4HF_7d_YSHt3rNzjvGJxUE0W90I1oLSUmxgV8Brv5RH9S1ewjWj0k5g9n1zWT42Qfeeo8yYhq3O6dcl0RQdIo4yDpwa0wRGlznVpTTN3tQKpIt50qHzIfVe8HPucZDQA8c2ykBMSuoA4R9llV0Ftx6McGWyvyWNytm-xiAcT2j7yQ2AMeXOTDsjQSJukHhSHH95KdYcNDnY7vyB8QXY_MU2UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=Ch8Sop8WNLfkRirsIzKLwG6ONQKFCEXArKigUO4UvsjspYQc4cLF231i4Nct6GOtvqg8X_mqx9iDuLky1wLO3o8zKk5pp5Ha_Pod4eRjtKucEXcAevGmHmAONqduSdR9e0eCBgKzR2YEekeGpe9xRronlP0ZOLnVW4U_taolo1ZR6A4lDSaHaDQMeWNmxgxoQtn97rNAcW8QG_E2RugsLAeemUvvqsiHcSQ0ZnZSG1944CXO8xkfKP6bXnU69QsBqy2A32CYvVdIqvDLVZH71BRCKU8ATKNuqDT8MQp8XLKwS9xcJb6YRgXNtMMmfbPfkEMIWTBtxLw4ryPb9I7dMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=Ch8Sop8WNLfkRirsIzKLwG6ONQKFCEXArKigUO4UvsjspYQc4cLF231i4Nct6GOtvqg8X_mqx9iDuLky1wLO3o8zKk5pp5Ha_Pod4eRjtKucEXcAevGmHmAONqduSdR9e0eCBgKzR2YEekeGpe9xRronlP0ZOLnVW4U_taolo1ZR6A4lDSaHaDQMeWNmxgxoQtn97rNAcW8QG_E2RugsLAeemUvvqsiHcSQ0ZnZSG1944CXO8xkfKP6bXnU69QsBqy2A32CYvVdIqvDLVZH71BRCKU8ATKNuqDT8MQp8XLKwS9xcJb6YRgXNtMMmfbPfkEMIWTBtxLw4ryPb9I7dMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=D10cdmy1zaZxNt8sfOPLGnQDb0M_BOZxMcVJZ86VAUOtsjAnAuLxBlyUBmjvzvEZ1DCLulVjpF-owmDnuHJ6INLrfKWN8B0numPAbIHb-cbjLwM_sQ5FokbRcbz7lLp7Llnn3lkLFlRJcYZCeqgN48AZEg3cSacFObObW-U9EBBlT_UAqlgBrKcTZRR4tw1GVyx0QW53kjGraRv0jIbCKgM31H3vZ-DPSutAzNnqxztBKhOEkZFxJFpGqtg782WoK5FWfO1BEHzRmmGaDy4eCevbiSYehMolkK1IjKinsq5z6vmMXU_FJ4JcfPJjKO7Lo3w0Vo2MkG5PF-IDViB3fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=D10cdmy1zaZxNt8sfOPLGnQDb0M_BOZxMcVJZ86VAUOtsjAnAuLxBlyUBmjvzvEZ1DCLulVjpF-owmDnuHJ6INLrfKWN8B0numPAbIHb-cbjLwM_sQ5FokbRcbz7lLp7Llnn3lkLFlRJcYZCeqgN48AZEg3cSacFObObW-U9EBBlT_UAqlgBrKcTZRR4tw1GVyx0QW53kjGraRv0jIbCKgM31H3vZ-DPSutAzNnqxztBKhOEkZFxJFpGqtg782WoK5FWfO1BEHzRmmGaDy4eCevbiSYehMolkK1IjKinsq5z6vmMXU_FJ4JcfPJjKO7Lo3w0Vo2MkG5PF-IDViB3fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=R7wzVZ2b_L02GRlas_a3aqfxzEepClmTDEByBElDGQiBwnadhWi0j4Z2j22fkMsyfYAxruMUT8oZd93SchsbxGth2avqZ7Mteqp4vzJOLAXyud3xzN4VmQLDznZ2Sr_uUExFdcLp726ir5j9ulNsERqdnTlOReHo-KIWs6zFLN-Kyh6h3tDmeT0AG0tzKRHgRbQAa44eF3XchMJFEEZXq0-35AcPuaZmaH5iIuWiqL-vXayjev2U2kO-LAKvdfCxDw2RosGEvnRWkjn0VfYEVycjKcsmPN4oiCuEi-FtlPAjVL9lDazoDsZuqBkHx2rBP-_fwYCagnAXJD5bJ1WoWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=R7wzVZ2b_L02GRlas_a3aqfxzEepClmTDEByBElDGQiBwnadhWi0j4Z2j22fkMsyfYAxruMUT8oZd93SchsbxGth2avqZ7Mteqp4vzJOLAXyud3xzN4VmQLDznZ2Sr_uUExFdcLp726ir5j9ulNsERqdnTlOReHo-KIWs6zFLN-Kyh6h3tDmeT0AG0tzKRHgRbQAa44eF3XchMJFEEZXq0-35AcPuaZmaH5iIuWiqL-vXayjev2U2kO-LAKvdfCxDw2RosGEvnRWkjn0VfYEVycjKcsmPN4oiCuEi-FtlPAjVL9lDazoDsZuqBkHx2rBP-_fwYCagnAXJD5bJ1WoWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=r8fKzw7GIS3mnx7QaGEMk2vGzs9DRdiVoTqbjI4Fj_skSdpjijw6vsevUenC0KNBxzGPpemq0pHeBXVG_s_3-gsg6Bq0xdymPmrePEe18qGXwQ6uTE0B8m9uzy6c3QVPQZC7KrkchsnDrigngLfAMVDg1pyhO_ZMWLfk4iyxyqrIVcduA_Drnr5ubx4X3R-AiurR9Qu3xdFaOyG_VHbFN6ySV3r7R6-_VXvQF5sIGzWhCiFxIAfxQKJkgGa1N0-E9Hvf78iuZ9tPf6aOzpaGIZ7cNYbo1lKO0mHj4kOo5COzKurkcN7FobUverkNzUD1WWZn869iJMXofvz59UjCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=r8fKzw7GIS3mnx7QaGEMk2vGzs9DRdiVoTqbjI4Fj_skSdpjijw6vsevUenC0KNBxzGPpemq0pHeBXVG_s_3-gsg6Bq0xdymPmrePEe18qGXwQ6uTE0B8m9uzy6c3QVPQZC7KrkchsnDrigngLfAMVDg1pyhO_ZMWLfk4iyxyqrIVcduA_Drnr5ubx4X3R-AiurR9Qu3xdFaOyG_VHbFN6ySV3r7R6-_VXvQF5sIGzWhCiFxIAfxQKJkgGa1N0-E9Hvf78iuZ9tPf6aOzpaGIZ7cNYbo1lKO0mHj4kOo5COzKurkcN7FobUverkNzUD1WWZn869iJMXofvz59UjCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=IjklBTkQw1fHEt8avDq39UFd_o4Pr7opfXe7wbV59GkIhjB8yevbZngx2l-L_nwoegORPi42EmGAREX7UX0ZQJpzSPXTeL02J455oPyMTlCmQZSMBISRmS6N2RkDfuJd_6L0v4AC8sW2JZYX1WRA0oLL3gT_M0aF53L70pfMZmr7TDXemRtWu9yWskyH6GgOINTWsZGQiK9ih-0cg-QPxfHycNet_o1p6eVfzpRfxWldsawn3QrgB69ovq_kSwillptMIaJxe8ErKC_4auh2ERnY33ik0zMJUAxnLZHXkSUCCw6nHlydoo-ifiqpiqVW6qTgRM4TLBIjaeADC08UpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=IjklBTkQw1fHEt8avDq39UFd_o4Pr7opfXe7wbV59GkIhjB8yevbZngx2l-L_nwoegORPi42EmGAREX7UX0ZQJpzSPXTeL02J455oPyMTlCmQZSMBISRmS6N2RkDfuJd_6L0v4AC8sW2JZYX1WRA0oLL3gT_M0aF53L70pfMZmr7TDXemRtWu9yWskyH6GgOINTWsZGQiK9ih-0cg-QPxfHycNet_o1p6eVfzpRfxWldsawn3QrgB69ovq_kSwillptMIaJxe8ErKC_4auh2ERnY33ik0zMJUAxnLZHXkSUCCw6nHlydoo-ifiqpiqVW6qTgRM4TLBIjaeADC08UpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس:
ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کنند.
همچنین دارایی های مسدود شده ایران آزاد نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66680" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66679">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=Dj0rtiAgbJIoFnbsm2QMVu-ppHU9cJIVtb2IP4sWWlHtI5TjCRBeNS2NyaPRevi6lcwgVZpCr1lGYm-WPh4r8G7iPw6OZITA_xfBc_m3EZWd3O4yzJ2Gq7KLTYquZgGOekUleVc5UO_FcKkvU2XN5mnMFcSr3uH9eGyBBBf6VqMF7xEI7cNuRd7MSFX-xroWWNxQMq85lSzhG5D4uFZozdStNLd0w9IdU3rYE7shRiJA21UwLfCtJAMoY-cI7gwa64oDjxilrUQKp-LJ-UEx1fFj3tX7OXV6XoBdqTuFf7DBdfo6MvoPvaSd1sbAdaNXCpQNLep47aIZiLHHgb2Ptw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=Dj0rtiAgbJIoFnbsm2QMVu-ppHU9cJIVtb2IP4sWWlHtI5TjCRBeNS2NyaPRevi6lcwgVZpCr1lGYm-WPh4r8G7iPw6OZITA_xfBc_m3EZWd3O4yzJ2Gq7KLTYquZgGOekUleVc5UO_FcKkvU2XN5mnMFcSr3uH9eGyBBBf6VqMF7xEI7cNuRd7MSFX-xroWWNxQMq85lSzhG5D4uFZozdStNLd0w9IdU3rYE7shRiJA21UwLfCtJAMoY-cI7gwa64oDjxilrUQKp-LJ-UEx1fFj3tX7OXV6XoBdqTuFf7DBdfo6MvoPvaSd1sbAdaNXCpQNLep47aIZiLHHgb2Ptw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=eJc8wuKGDCIlt2VgvYm5oI0SGO_03aZEZWsjWL5-F1P1aHee40vF5vxWzzXyqbZMSpIx-nHrJ_6xunZMdDS2pKreBFZEd_h2POGJvUffghQRfcwa_NDHNQljIhiThZ586EaOwohraGdpttc94uMcwOtcdFWxOalebWtRifggOpK8cTkzBZqiGDgIqlT5mjyOzX8MhDXTI54crDNsojiwIRnXXt01mbSoXdrY-hwpdBT5BOvV0buHIhGvmra7FARdOXI5MfcIBXAY0VAZfVSdLV-KHbgx7tpeALJ8jO36y-ySDDADeZ0m_I5MjIP6-bGNE8qmJn_k2iFRLdDFkkfdYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=eJc8wuKGDCIlt2VgvYm5oI0SGO_03aZEZWsjWL5-F1P1aHee40vF5vxWzzXyqbZMSpIx-nHrJ_6xunZMdDS2pKreBFZEd_h2POGJvUffghQRfcwa_NDHNQljIhiThZ586EaOwohraGdpttc94uMcwOtcdFWxOalebWtRifggOpK8cTkzBZqiGDgIqlT5mjyOzX8MhDXTI54crDNsojiwIRnXXt01mbSoXdrY-hwpdBT5BOvV0buHIhGvmra7FARdOXI5MfcIBXAY0VAZfVSdLV-KHbgx7tpeALJ8jO36y-ySDDADeZ0m_I5MjIP6-bGNE8qmJn_k2iFRLdDFkkfdYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=nykBqkTPwxgjLRyAGJF7tX6SJlBNCwVLhiEwnaSQDrbiEKFtl512lXWkpgyB_QRD2EYchCbuPp2pSfqFzBFoHgOIxKW__c0Mh_5LrAvTejIcmaRNMB0HyOAVo4jcNZRP-9FjnGt70gircz3NNTKiVqS0qOQr7hlNGy7LjC1UWZSGOWtMipOAhIAE0kfK8A8pE3kEv6RBer8ZfWDyv5dUgF0CYqnUruMRTili8a5UybNGtn5N1rLOTtSv7gV38L14caox-q99u4qkaa_iiOXNEnhJJ4DJhSpj5yZoKVrJdlc3riWuC6Ogcmn3Jr3U-uu7q6NbbQhskUdub0oBi0n6QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=nykBqkTPwxgjLRyAGJF7tX6SJlBNCwVLhiEwnaSQDrbiEKFtl512lXWkpgyB_QRD2EYchCbuPp2pSfqFzBFoHgOIxKW__c0Mh_5LrAvTejIcmaRNMB0HyOAVo4jcNZRP-9FjnGt70gircz3NNTKiVqS0qOQr7hlNGy7LjC1UWZSGOWtMipOAhIAE0kfK8A8pE3kEv6RBer8ZfWDyv5dUgF0CYqnUruMRTili8a5UybNGtn5N1rLOTtSv7gV38L14caox-q99u4qkaa_iiOXNEnhJJ4DJhSpj5yZoKVrJdlc3riWuC6Ogcmn3Jr3U-uu7q6NbbQhskUdub0oBi0n6QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=myyCqs7IBs8YeODqKd_zBs37824LzrJc1I0s1hYpfeeaEqqQ-Uzi9tkvBdE5PQVQSSOj9klOXEfw38_Wsa0MJpKMTgKqaHuqh4DemThqcg_IVZZIg0ROQLzpXmkkNnElXh0oetqnVV5n9YNDDjrz54DZx5i4GZ7FF9Yk6dgsDSAE1tiuNeYHUaCp3Z5AMEfit-6B72d1UMDvcEuPrqKw_60saNTEIVF5tphH6KHuedZgMEC4ffSAv_WAlzgghu3HI9edWj71q-HBtO-UM2vlLfkY3mPze2yaK_yhU9_OT7s52B7NZnsTnYLc9F-8xED4n8KEUfYkXyPvjTpfZB5-_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=myyCqs7IBs8YeODqKd_zBs37824LzrJc1I0s1hYpfeeaEqqQ-Uzi9tkvBdE5PQVQSSOj9klOXEfw38_Wsa0MJpKMTgKqaHuqh4DemThqcg_IVZZIg0ROQLzpXmkkNnElXh0oetqnVV5n9YNDDjrz54DZx5i4GZ7FF9Yk6dgsDSAE1tiuNeYHUaCp3Z5AMEfit-6B72d1UMDvcEuPrqKw_60saNTEIVF5tphH6KHuedZgMEC4ffSAv_WAlzgghu3HI9edWj71q-HBtO-UM2vlLfkY3mPze2yaK_yhU9_OT7s52B7NZnsTnYLc9F-8xED4n8KEUfYkXyPvjTpfZB5-_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #3</div>
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

<div class="tg-post" id="msg-66673">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66673" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66672">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=fXVH7Ju0gZuK3ddRMnWyC0CnljsLs2WfsswUi5zlB4aKO2FjMCgynROiOdAllnfNGV79ClyAqs91-czwP9W-85yJZjhw0zOdoAJNFr7DSC4C0YYlPCgBTZVjcViSJYHfigURhWUVJwJm4BcHE2E8PsU5VTEUfZExErHTr9_BZVAlI36AGOGqfGiaTunTBMGywerfCOaY7Mf5YIKJ3_IqZIfOWFcenxN9eusL4kTfYoxFZKHduPFPRApRhcV95ItmIjcJPQESo-IHQndjiRAg9M9EacwsvzNdpFx5xo8bmZtfxy28G_gevpnB_DwxJ7_yuxwGDig-YlKcaC_D_X3mhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=fXVH7Ju0gZuK3ddRMnWyC0CnljsLs2WfsswUi5zlB4aKO2FjMCgynROiOdAllnfNGV79ClyAqs91-czwP9W-85yJZjhw0zOdoAJNFr7DSC4C0YYlPCgBTZVjcViSJYHfigURhWUVJwJm4BcHE2E8PsU5VTEUfZExErHTr9_BZVAlI36AGOGqfGiaTunTBMGywerfCOaY7Mf5YIKJ3_IqZIfOWFcenxN9eusL4kTfYoxFZKHduPFPRApRhcV95ItmIjcJPQESo-IHQndjiRAg9M9EacwsvzNdpFx5xo8bmZtfxy28G_gevpnB_DwxJ7_yuxwGDig-YlKcaC_D_X3mhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پهبادهای اوکراینی بر فراز مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66672" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
