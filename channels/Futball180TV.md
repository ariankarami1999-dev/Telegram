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
<img src="https://cdn5.telesco.pe/file/LJ5LzHDk-F89vV2ZrM8FrPBTz9I-WH3D28j78MFidbk1xrygZzcTtVO34i5TUqPWhaQY7s1joMUN2X3VEcwzp-aRCMLjhN9r20xsDX-Ilxe7XmxWUSmcXV5XMZXnus4AIBT_nswhmW9ZjijtXULLMzLXVL5sC4RzRGDxVI-aAkqPX8N8x9S3mxF-TuCVTPanZOuBOzQaX4EvFoRI3kHUl0U1iYmBRs0Czo74N2bTAGXsLUqS0q0FcSz_8TmzXQ-WMFqWt1dXEAKD_8Rc7yoOdaVLmvkHSIDrEyrDLs9RehCKnn7VkD1pLI6zMHRkajb83GF6_SeT1GhtnWvHssI9eQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 561K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 17:24:51</div>
<hr>

<div class="tg-post" id="msg-100749">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WX0-HW6FhUM2RcDjazy6eIiEXF7NjFleSPOez5hko8hxbyjwS-PgDZ_3hC7ekXHfOViAUU2t5mexKhmaEnC9iLuc-y0zd6pZUhgNGOPtn0uUzW8-XXHyyLxDDOuNG6dWu12a_BYVbsJfzLjCg8g0ooS8ZUjy933BdA7YwNk0e9KRsyQgl6lWzJnd7nmrEX4RGnd9v_v97Fx-4LLmHMiw3A06daSQiNM1vJGXTJC9Q70lVOMBBTkavaj6C8qd_SSwVji6lSeZXAXYjw58rDrZovPvhz_QyFztVv0z5y-Q9U25NUyCfv82uIZG0sAEQIIdwTwA9GLzTNT5r3rdgLx58Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منچستریونایتد مقابل رکسهام در اولین بازی پیش‌فصل شياطين‌سرخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/Futball180TV/100749" target="_blank">📅 17:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100748">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaDkDE9dUp1u5_WqtAUcvATw1nHteWgrZZFHtfcFUWT7-fLboaR5ikeOmy48ABObPF7ntIQj02R5HbbyXw9GFfYEibvswGQF8Z2aABH3PbbYfmEnxmd7xMkAk17VefqMi6wLqk3eQvTcTRHVBHzhCMV2rTbG8I5--YPuZJJFeIFcgeIuNS5IvYvmODcrW9AJyglmzpf9jG1pl8UX493kEyC8uWfW3MzxhFWBHgLEjXfLfRQbXVWnpMv_Wq13-vWQW5ywvf1SyCNzJR-v7HWJUFmWS-Cy4LcxTkpLIDtnPi7Q1_oSK-3qlIyMvAMPV4ryfKYeRt4ZxooAEUu223DI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/100748" target="_blank">📅 17:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100747">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2480fbbbb.mp4?token=MRwg1v1vQO5YkeB5izGiO0I69xP6YUH2XLIW2bbVCSSyAsUKSWq1nALxUIrJl8hqLY0611wGpax5oj7hcFXFzFmYPEFlBE8X6lyt9dGBVxHVuFXeblFqSxY29FoQpuXZwWQqmLTbUcO5596eCpDCWbUDWxPQ8glP78j3BZOdEt9fCI807mTMOutRpH0LUhdEcEM-LF8wmYxDCSVUrgQz94TSN6qMvSvDkmpVcXlPB8Jq8jN8gW0irStg8q_nMUAf9S2knzqWcGKV165JZBXYxvskcmlSEHznpyJjDb_J3_ONW-Qio1VgGFrFRex0dY3XpnUewBv-tEaFmG3QlgICJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2480fbbbb.mp4?token=MRwg1v1vQO5YkeB5izGiO0I69xP6YUH2XLIW2bbVCSSyAsUKSWq1nALxUIrJl8hqLY0611wGpax5oj7hcFXFzFmYPEFlBE8X6lyt9dGBVxHVuFXeblFqSxY29FoQpuXZwWQqmLTbUcO5596eCpDCWbUDWxPQ8glP78j3BZOdEt9fCI807mTMOutRpH0LUhdEcEM-LF8wmYxDCSVUrgQz94TSN6qMvSvDkmpVcXlPB8Jq8jN8gW0irStg8q_nMUAf9S2knzqWcGKV165JZBXYxvskcmlSEHznpyJjDb_J3_ONW-Qio1VgGFrFRex0dY3XpnUewBv-tEaFmG3QlgICJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
انزو فرناندز که حسابی هواداران آرژانتین رو مجذوب خودش کرده
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/100747" target="_blank">📅 17:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100746">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc579a6c5c.mp4?token=CI8Lcq12DyGkwkazArXbqLSwrsTj9Z7DJwJ5XPXg_rgbeMEdfnQ40b9I5s4OGrFpaO8ZHKcQAxuVpw2PJ8mqGYQ-VU6B6N5rcvSWHB63kaUPQ1DoJC3t65-iCAngsZ3CDKpI5bJCzi0Aifb2OD3gIp9CAnrS2EfuQXa1auGHOU7w24JV6d9fo4R-IkHmdRknQ963vZqNqakGYEVRJAoBaFd2N8HxsyIHa24sCQ1a-DQWYjqTqHoxfgACwi43anmBFPZrGO-XcL78sehNczwgQw64uPFDX6Kauue38AmoSKG-nrEWL0d_Ps3VcTBXCcJl3VxvMZapDjvFrvm_WzEYuZTnQGsfF3diCRRT5X931mxWzbcUABZDdl8n6Z_SRoiQkMaOywkfOwkvTSd-iO0oEE1RXroqIBrN3gzvFbYzNvsaWTnrDf3O0XLrYSut6u6ndpXhdzsW24b_BjNRpaRNg0BHffQAz-NKas5Wd5teYrr8uZT5jG679xuvgSNxKkvkZMcC4dxW-RMEeO3fVmt3i27x_G2wr_3BW-cLdIq83kF-6zCX-dx1PaafnNaewljKrIJlv2d6Boy_CaHyZOiVwssMnem3XaI0hIQtbyeDlOhtSK1OjJQaPssVp7HWwbyW4E4B7fQvRdKy4km__GiZ5q27AhDSv6hDZB9H8bP8Kik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc579a6c5c.mp4?token=CI8Lcq12DyGkwkazArXbqLSwrsTj9Z7DJwJ5XPXg_rgbeMEdfnQ40b9I5s4OGrFpaO8ZHKcQAxuVpw2PJ8mqGYQ-VU6B6N5rcvSWHB63kaUPQ1DoJC3t65-iCAngsZ3CDKpI5bJCzi0Aifb2OD3gIp9CAnrS2EfuQXa1auGHOU7w24JV6d9fo4R-IkHmdRknQ963vZqNqakGYEVRJAoBaFd2N8HxsyIHa24sCQ1a-DQWYjqTqHoxfgACwi43anmBFPZrGO-XcL78sehNczwgQw64uPFDX6Kauue38AmoSKG-nrEWL0d_Ps3VcTBXCcJl3VxvMZapDjvFrvm_WzEYuZTnQGsfF3diCRRT5X931mxWzbcUABZDdl8n6Z_SRoiQkMaOywkfOwkvTSd-iO0oEE1RXroqIBrN3gzvFbYzNvsaWTnrDf3O0XLrYSut6u6ndpXhdzsW24b_BjNRpaRNg0BHffQAz-NKas5Wd5teYrr8uZT5jG679xuvgSNxKkvkZMcC4dxW-RMEeO3fVmt3i27x_G2wr_3BW-cLdIq83kF-6zCX-dx1PaafnNaewljKrIJlv2d6Boy_CaHyZOiVwssMnem3XaI0hIQtbyeDlOhtSK1OjJQaPssVp7HWwbyW4E4B7fQvRdKy4km__GiZ5q27AhDSv6hDZB9H8bP8Kik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
علیرضا فغانی: اگر ایران مانده بودم، صدبار خداحافظی می‌کردم
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/Futball180TV/100746" target="_blank">📅 16:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100745">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e993550cde.mp4?token=I6V7MdgF5oSAkQDx8AjQSJp5iltqtfF7ZPbQqrwX14TgDgi5LMsdyHUWj-bs94qkIsbbercO8Glmv7QwfUfZj-SiyEe-n9nPO_akqMFufWVq4190BEQKNVU7ne8RS7lVib0jU6jbCtnH5pSJm-K24ktO5l5vfRcGRK5CGATDVqEBbffenda0YXVOC1EiNcQ0YlXwMI2qhJaZskQsYLUfhOnHmbn_UEHexCeovR4B1CEspnYEIANRs-5NqWRa4O87UEdJI2Uht-A547j4iXcONs8-rAgYe6zPxyuXIy8-cAt4gimgH9li8zCV5vmvaZTLz0P_PJAjtHrcLHKca_x7BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e993550cde.mp4?token=I6V7MdgF5oSAkQDx8AjQSJp5iltqtfF7ZPbQqrwX14TgDgi5LMsdyHUWj-bs94qkIsbbercO8Glmv7QwfUfZj-SiyEe-n9nPO_akqMFufWVq4190BEQKNVU7ne8RS7lVib0jU6jbCtnH5pSJm-K24ktO5l5vfRcGRK5CGATDVqEBbffenda0YXVOC1EiNcQ0YlXwMI2qhJaZskQsYLUfhOnHmbn_UEHexCeovR4B1CEspnYEIANRs-5NqWRa4O87UEdJI2Uht-A547j4iXcONs8-rAgYe6zPxyuXIy8-cAt4gimgH9li8zCV5vmvaZTLz0P_PJAjtHrcLHKca_x7BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚠️
خاطره‌جالب سرمربی تیم‌ملی اسپانیا از تقابل با مسی زمانی که سرمربی سویا بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100745" target="_blank">📅 16:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100744">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d4aefcaa3.mp4?token=e5mQ_0SXv6pLRMxVRy1BbCCYJRr0WgpajNSVzQs0xhz71_Lpomkm3A-tYdwNQ7a6LIZqmxlNoA1Qsz7CgjRm4qYWXdqpMAtEPce-_KBVYRQlvmSJ7ZZva7uaYCpmSbqhcJjHqD27d5jRreLNXKdf0ZD5Poy-oO7b5ZhNeY3DCXZkk7RhymOkpkUudHP2EE-5npu6G-LVHdK0sqGnTgPCz8N7dEs8-Qesi7DoR4ZGgWEUh3w_ZLSTK2mnX3lc6ZJiPV3erkfuFQW6kat0skIrxyJcVcnZtiGS3DPz3-yhogAq571Rf-0rAND0pDW8fuwOEtOKU5Yn74ipugg0Dya3zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d4aefcaa3.mp4?token=e5mQ_0SXv6pLRMxVRy1BbCCYJRr0WgpajNSVzQs0xhz71_Lpomkm3A-tYdwNQ7a6LIZqmxlNoA1Qsz7CgjRm4qYWXdqpMAtEPce-_KBVYRQlvmSJ7ZZva7uaYCpmSbqhcJjHqD27d5jRreLNXKdf0ZD5Poy-oO7b5ZhNeY3DCXZkk7RhymOkpkUudHP2EE-5npu6G-LVHdK0sqGnTgPCz8N7dEs8-Qesi7DoR4ZGgWEUh3w_ZLSTK2mnX3lc6ZJiPV3erkfuFQW6kat0skIrxyJcVcnZtiGS3DPz3-yhogAq571Rf-0rAND0pDW8fuwOEtOKU5Yn74ipugg0Dya3zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
هواداران اسپانیا در آستانه بازی فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/100744" target="_blank">📅 16:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100743">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34b9470b1.mp4?token=a9yQxRbGVM8TbRh39_r8e7gX03xo5ocO-n6ViCQWL8kLR9-aB7Kew_QYFgZlVAsetN3yNg_Sd_SRPToUxVNlRlKhfPeg_UIIGx7zbbczPfa1IABNS2KKuP0FVxNB6rDkDmPwy6X2Aubt1bx3s_Th7vCaaWi1Hp01O3R9o4l1bkBRGTlrkI7icI42oznwpVw00zfhFc_LDvRVuAgtbsp5d2R084UMrQihpRN3_fz66PH3OXe4W8JuaxdiFGEaS45xddbvxpeedDc95K3WdyHcO0l2kAG6NflIxZrFZKkhFYqtE0Po0IjCnFrC5GibOYDUaAJxV7WEug6dGlh-PRjbFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34b9470b1.mp4?token=a9yQxRbGVM8TbRh39_r8e7gX03xo5ocO-n6ViCQWL8kLR9-aB7Kew_QYFgZlVAsetN3yNg_Sd_SRPToUxVNlRlKhfPeg_UIIGx7zbbczPfa1IABNS2KKuP0FVxNB6rDkDmPwy6X2Aubt1bx3s_Th7vCaaWi1Hp01O3R9o4l1bkBRGTlrkI7icI42oznwpVw00zfhFc_LDvRVuAgtbsp5d2R084UMrQihpRN3_fz66PH3OXe4W8JuaxdiFGEaS45xddbvxpeedDc95K3WdyHcO0l2kAG6NflIxZrFZKkhFYqtE0Po0IjCnFrC5GibOYDUaAJxV7WEug6dGlh-PRjbFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های پیمان‌یوسفی درباره چرایی عدم‌ گزارش بازی‌های جام‌جهانی از صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/100743" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100742">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94776f3b42.mp4?token=bc-VVU_8o19laN29ll8NbfLXDWhvM-AxgAY3teuN2vQ8rG6LkCTeRnTP7FbXH76KDIFaZ_NBDww9_3RBYg7AJvLJDxQQ-zHK-AzSGb-UwcZVZyyVlpZ7ULmM66y_KjeYWNUsYTw2z_D_ihyDuW96lvXxEcHJ2txgZaCZdlFe8hVs4lxEPtVgBD7tE57yfClswrOLYU4nxs905E8N0uyYtIgyCVQCHJe3JLqTmyTAN9Ax6KgziK203vlvHzGhydsR-iAcvQBx5JKSBNqhPo-OqA6ND2toJDdeysJZsoavN_-YbeHj0RPNTQnwWgkxiHstbmOT4PNozSVNU991i9dLcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94776f3b42.mp4?token=bc-VVU_8o19laN29ll8NbfLXDWhvM-AxgAY3teuN2vQ8rG6LkCTeRnTP7FbXH76KDIFaZ_NBDww9_3RBYg7AJvLJDxQQ-zHK-AzSGb-UwcZVZyyVlpZ7ULmM66y_KjeYWNUsYTw2z_D_ihyDuW96lvXxEcHJ2txgZaCZdlFe8hVs4lxEPtVgBD7tE57yfClswrOLYU4nxs905E8N0uyYtIgyCVQCHJe3JLqTmyTAN9Ax6KgziK203vlvHzGhydsR-iAcvQBx5JKSBNqhPo-OqA6ND2toJDdeysJZsoavN_-YbeHj0RPNTQnwWgkxiHstbmOT4PNozSVNU991i9dLcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
انتظارم از بازی امشب فرانسه و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/100742" target="_blank">📅 15:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100741">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJuE4lErvwBka7qS79oWXgyEPavJSW9MhDCxm7MLNm_o-JisLwuK4ehdGj8gF3SL4kevCQfJsyhGVrV5D5-Y6HQVi5eqaSCiVFcJGv6tVbWSpK7FHeWtjZiJBi52DgaIfqHXtygplqBjMvnjhlvLwyo5XN2OT6lpVm7OgMFmtRF-aH2tglPKT8a0iXfM3kYzLK-VU33kFrJoD4q7196FPWzFk3Wf1GOvB7LIdyyjGE__gskS34FQdnTyhrxGW9avegMCyvfl1uAMp5jMLSTQqRqGbGKR-ZBy_kB6BoJrtAt5zySE8C_WCwkeDvjA7Ld_w-9GqPJPWwPJbPuuIMmsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری روزبه سینکی که بیرانوند و نابود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/100741" target="_blank">📅 15:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100740">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtKWfEvde-ay8D8S0flZ0jHHC6Gdor3OFWw78UKtWSL1HmsnMRH4FEZL3Z736ueE4-jWOaQrSqrgq-kKRCt63GRcyN68DazzL2BJYr_JB9vYSUZkyJME4oR5wPM4lMGFigXanBBzn5HRg1O54UjJonOQCUETHEok3yFE1f-T-ZlOxiCr-WKjTbaHbooTf4MX3oToomkVxUiiZOrXOErrBlKabC-EJ6AAzd7IHIe8sRLy6eDBzVapsfR_27oHEkgSjKpYg7DhcuKm9IQCzzk927925adyQV4am9E3_u1yFQCELHkk2yhqpyrXrvzNdKSiU-Jj-tF1slTxjGWSY1ePFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 روز تا مراسم توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100740" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100739">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/100739" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100738">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=bCwte3RW8Uo-9jVld1DYu-BOege90u7GhrA-Ts47U9LZSfGvx-1_mLpSqD2ztKvfTvQXUs0YIF571peo-eBUwvaB1UwFQMsC5zx1DjeAKfA5TXprh26oTLloUtK0gbsTKNcvH5eSk3dlZjYOMXJfY8ArAGnguT8T_kuUGIUUv2SPFKC1ocWmGql6LkFagBtQV4I_dnKAkhD0ElXPiMwqy4kQrMJvujgV0wnZ7md52CW224XAw9QG5__qdqFsTqdqf7Gmr6kNl8FUs1w4khKlw09yoF9sZZqIpqvsJ1yfIuwyRRfdEk5P1wySDuu5b5QUgZmc6vzNn4bwQKgJV0ENQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=bCwte3RW8Uo-9jVld1DYu-BOege90u7GhrA-Ts47U9LZSfGvx-1_mLpSqD2ztKvfTvQXUs0YIF571peo-eBUwvaB1UwFQMsC5zx1DjeAKfA5TXprh26oTLloUtK0gbsTKNcvH5eSk3dlZjYOMXJfY8ArAGnguT8T_kuUGIUUv2SPFKC1ocWmGql6LkFagBtQV4I_dnKAkhD0ElXPiMwqy4kQrMJvujgV0wnZ7md52CW224XAw9QG5__qdqFsTqdqf7Gmr6kNl8FUs1w4khKlw09yoF9sZZqIpqvsJ1yfIuwyRRfdEk5P1wySDuu5b5QUgZmc6vzNn4bwQKgJV0ENQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/100738" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100737">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9511ead233.mp4?token=RXpHaeMMPCifXHLGPKhT1Cciwgc11H3okY0ynGCgBmwNq-bejDmXWRimFIcIitGh2J-PQj8ZztAs27KzsVNdNK5HG3-AZW-isUQYvPq_DTGHcQGOTcCSiJay24bjnK6594XD5WD988F7sORbFwmFPvjzkhuZNkSMaqdlzYAgE1TayEJ5-P2wvdd3O2E9S-D8EdI9dMoJ_3uqH5UoCRu3OXVDTZED8FjJhtZ2Y55_7QbWPJMDxsDrVITH9-M-MX5_1G7Xy097FMW8eeLaI2WF_d2T9-Mb1OyMIk3LSlfeF4zCL3GfCbZXMoQJ4U3z7HG5BhetT7eBGIsPgIRA7tvaBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9511ead233.mp4?token=RXpHaeMMPCifXHLGPKhT1Cciwgc11H3okY0ynGCgBmwNq-bejDmXWRimFIcIitGh2J-PQj8ZztAs27KzsVNdNK5HG3-AZW-isUQYvPq_DTGHcQGOTcCSiJay24bjnK6594XD5WD988F7sORbFwmFPvjzkhuZNkSMaqdlzYAgE1TayEJ5-P2wvdd3O2E9S-D8EdI9dMoJ_3uqH5UoCRu3OXVDTZED8FjJhtZ2Y55_7QbWPJMDxsDrVITH9-M-MX5_1G7Xy097FMW8eeLaI2WF_d2T9-Mb1OyMIk3LSlfeF4zCL3GfCbZXMoQJ4U3z7HG5BhetT7eBGIsPgIRA7tvaBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
پپ گواردیولا:
جام‌ها خوشحالم نمیکنند، تجارب انسانی آن دوران که در بارسلونا، بایرن مونیخ و منچسترسیتی کسب کردم، حس خاص بودن به من میدهد.⁣ در حال حاضر هر روز صبح از خودم میپرسم: آیا دلم برای مربیگری تنگ شده؟ و جوابم منفی است.⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100737" target="_blank">📅 15:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100736">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0b7dbaff.mp4?token=j3WPh8QH6eRdJUSBGMEmli_1_arlRhTihvd4aPwo2UD54InNR-mKoVdTaS4BYPCM3bwtZQk4vqyXDg8mt2lVTzZ9S0bTpMZPymGD77J4-AmLetoww-sFpxyCpfAXrUu6ETlAvFjazAosLs7uE5FLlFwnjGfuQdtqP9G9xFjyvZ6mcXQFYwb85UM2wiOhJgL_Sua8EKjALE-9BMsoOYej0PtyZODVcDxsQM7mQbW_IrrO8e45ZAwKt4ARS63g8WG3xcIGXQHVbpySkHrZXGwdCJZmY9ry6ZD5mdTu1vSq2AWgfnrT1noO32WdM-4g0BFOSZYQpVhgH20VhKkn0FkUKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0b7dbaff.mp4?token=j3WPh8QH6eRdJUSBGMEmli_1_arlRhTihvd4aPwo2UD54InNR-mKoVdTaS4BYPCM3bwtZQk4vqyXDg8mt2lVTzZ9S0bTpMZPymGD77J4-AmLetoww-sFpxyCpfAXrUu6ETlAvFjazAosLs7uE5FLlFwnjGfuQdtqP9G9xFjyvZ6mcXQFYwb85UM2wiOhJgL_Sua8EKjALE-9BMsoOYej0PtyZODVcDxsQM7mQbW_IrrO8e45ZAwKt4ARS63g8WG3xcIGXQHVbpySkHrZXGwdCJZmY9ry6ZD5mdTu1vSq2AWgfnrT1noO32WdM-4g0BFOSZYQpVhgH20VhKkn0FkUKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
فقط یک نفره هنوز داره به تنهایی میدرخشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/100736" target="_blank">📅 14:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100735">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4652c3d86d.mp4?token=AN-8rxOKwBrfzJ5XK2STAVuyu4Du4zHhaRz9eidKVlB397A91oLXz_MjYkKqNWMmvU3V02-9FxOM06zndBhtxWSbSC8z7__onjQt737ZDLJUN8yCVXEeXSrUnBiRBb8UPGHo3WahZoTn6oJVlaGwxipPzHsEpV8aDChuP3W3BcALw75WNaqYVWI2TLdbC2kO6uyTf8j2hl1wG9Wr_6st4bPQ7lvLsWpSwhIuIx2ax6K3IOKHqB43sZDMyH7fyMf6dYI50yNOWf7HWHFBuSxsVwi5-iNjKcc5hGjYL4sDyHKlBgi9bQ2TXdFe_V3GQG7oBDemghou8Tn56gq4ipBlJjIIqqEy74lAbFJtlrK9FYJtyI6i7TkpfhRLjwttcEoC1cdwFHDN8ZegCB6JBB-ynjXYEoz4F9Tf4DPvQVGSak9uAreMGzq6fruUwsq1rDGRybp7DRt4v3hf8VEAtmBhtJDipmb49OUe4b818Pk-GRm7CAn-tI9KnxId8-yLNQSbBN-iZrlg0CyYsoSuvidg4UHgEAjKiHO6PLuwA7iP41dqXXKJUTzXyx1uNk8QhRSZJRs0JGcljLScRSqcgeSNIb7u0ChPAetn24C2E7LB8h2K4cmiLEl5vhVM0ha-3sK9tSrmiYpV5vPjSEfp0KL5433A8-EmlRLfnd87WQw1MXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4652c3d86d.mp4?token=AN-8rxOKwBrfzJ5XK2STAVuyu4Du4zHhaRz9eidKVlB397A91oLXz_MjYkKqNWMmvU3V02-9FxOM06zndBhtxWSbSC8z7__onjQt737ZDLJUN8yCVXEeXSrUnBiRBb8UPGHo3WahZoTn6oJVlaGwxipPzHsEpV8aDChuP3W3BcALw75WNaqYVWI2TLdbC2kO6uyTf8j2hl1wG9Wr_6st4bPQ7lvLsWpSwhIuIx2ax6K3IOKHqB43sZDMyH7fyMf6dYI50yNOWf7HWHFBuSxsVwi5-iNjKcc5hGjYL4sDyHKlBgi9bQ2TXdFe_V3GQG7oBDemghou8Tn56gq4ipBlJjIIqqEy74lAbFJtlrK9FYJtyI6i7TkpfhRLjwttcEoC1cdwFHDN8ZegCB6JBB-ynjXYEoz4F9Tf4DPvQVGSak9uAreMGzq6fruUwsq1rDGRybp7DRt4v3hf8VEAtmBhtJDipmb49OUe4b818Pk-GRm7CAn-tI9KnxId8-yLNQSbBN-iZrlg0CyYsoSuvidg4UHgEAjKiHO6PLuwA7iP41dqXXKJUTzXyx1uNk8QhRSZJRs0JGcljLScRSqcgeSNIb7u0ChPAetn24C2E7LB8h2K4cmiLEl5vhVM0ha-3sK9tSrmiYpV5vPjSEfp0KL5433A8-EmlRLfnd87WQw1MXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صحبت‌های میلاد‌کرمی از کارهای عجیبش در صخره‌نوردی که میگه هیچ‌ترسی نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/100735" target="_blank">📅 14:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100734">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf5731dc1.mp4?token=OKCQA1oJanT3uPh7mTcXqbhq1J0wc-Vr3p94EBfOZr_WusEo-53LOIy14NCT28Mx7DBWTxOBvtWw21M4fQvxuUxDMYfvg3DPFmK2jS-nDRv-IN0oW6qu5XzApx7BnDxIWwglN5FLpqBJVxTPwYpRUlTbcPjIDT8rF-svG2SgzpStIUDMfDTxIqUC2aNyqioGA0REVLCx31PkATRMo3DIAmWirAbSmbX5_ql3PZSMHIJE-t-hSlnWga5heFA5iDVxMqeD9ksqy4M3UgQKv2dJcdW-EojLtVxrhBiyTKdZaujozGlctcshjFElexnFhnK0Hl0Jl3FlY0-_-yAZ3etP4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf5731dc1.mp4?token=OKCQA1oJanT3uPh7mTcXqbhq1J0wc-Vr3p94EBfOZr_WusEo-53LOIy14NCT28Mx7DBWTxOBvtWw21M4fQvxuUxDMYfvg3DPFmK2jS-nDRv-IN0oW6qu5XzApx7BnDxIWwglN5FLpqBJVxTPwYpRUlTbcPjIDT8rF-svG2SgzpStIUDMfDTxIqUC2aNyqioGA0REVLCx31PkATRMo3DIAmWirAbSmbX5_ql3PZSMHIJE-t-hSlnWga5heFA5iDVxMqeD9ksqy4M3UgQKv2dJcdW-EojLtVxrhBiyTKdZaujozGlctcshjFElexnFhnK0Hl0Jl3FlY0-_-yAZ3etP4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب، قلب ایرانه
❤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/100734" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100733">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80daff883c.mp4?token=G3NAvRRgs9rWHX3XbJKl2TMgftitm9BY13YosZo2lmxdqZQ-ciHZIckWY873fw2KjfiuDCKEfsUxhwg7JMO3xI381fcXd4_rRujLqwPA34-llT_ryYmHsCcHxC8phODZWJijfuhfwqTDzXg8jTc27LgA_Po80kSMvkFv2-Hz60Ch6-ZJ1r2EmVH11YNdVms07_ENP89mStuMlqEwCqTm4puhidtjYZpGiMigYBhKf17vB0F4tIuI_Osr_V7yiWwKpnX7IsykkFV5j6O40LUBb3D21V73OBgPwBqWADqlaq2GdIe4ala890NB0Jt568v-CPmbU_vtzsxVhf8x3nRq9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80daff883c.mp4?token=G3NAvRRgs9rWHX3XbJKl2TMgftitm9BY13YosZo2lmxdqZQ-ciHZIckWY873fw2KjfiuDCKEfsUxhwg7JMO3xI381fcXd4_rRujLqwPA34-llT_ryYmHsCcHxC8phODZWJijfuhfwqTDzXg8jTc27LgA_Po80kSMvkFv2-Hz60Ch6-ZJ1r2EmVH11YNdVms07_ENP89mStuMlqEwCqTm4puhidtjYZpGiMigYBhKf17vB0F4tIuI_Osr_V7yiWwKpnX7IsykkFV5j6O40LUBb3D21V73OBgPwBqWADqlaq2GdIe4ala890NB0Jt568v-CPmbU_vtzsxVhf8x3nRq9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نکونام حرف دل میلیون ها ایرانی رو زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100733" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100732">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f306dcec7a.mp4?token=PMIC_VludABHU6_BdeUPF6UgcKGlxlGysVxXd07QCRXYhcDD_crminismRA0NqVCWf_A5c20W58znqifk0dTCqEaHhyl31GQMCMhyg-26CpaousIHpq-PCnEdSfnNX-zIAWC8Qh0vhZh0IB5LGcHT2eS7UHlruWG2oPeg5zC_h9jU80MwcyoHZyBRWAhJHsuL1zg0pLWVzdJSLz2GSH3BRTW1i05v7TROagNP3l9zXtsvJNoA9SysrQevDzROBXmnh2WuSNYbbuDNsk9bwTCdTbj-SxY3ulJEjguoBs-921ki37LeFMLFT4d-X5yEfqGtL_3SGaQvaHKrn3-8calySY3vBj9-Ys9JodsSBWqLxrY9KN7QKxCIEhjp6u3JKTSeh-54JeIRvtzOYwKpzL51K49r8WPsMJ_VKrzjZZN5yjhs_WkdN14DtntOlr1Yj-fieDPXhutuMktNivIug7_Jaj-t1NffNTF2jpwHVzqaX6EJp0bfoSGryffS1Frf2qKKxPfvGlvz8Lxn15Jfaiw2xekS-OJFcI9_1MkDgnMvjZJkqfOcLI9UQiATRAKe1n7EwZmEtK-L4dg5JVKGk1sjj6v8EcMll8wMf42Ynv4kasYDV737WTkWzfpIGKJYeu8txbEK2IDZtAsUecwQdGvj2zzeAYr7HbOf2NcocsBg-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f306dcec7a.mp4?token=PMIC_VludABHU6_BdeUPF6UgcKGlxlGysVxXd07QCRXYhcDD_crminismRA0NqVCWf_A5c20W58znqifk0dTCqEaHhyl31GQMCMhyg-26CpaousIHpq-PCnEdSfnNX-zIAWC8Qh0vhZh0IB5LGcHT2eS7UHlruWG2oPeg5zC_h9jU80MwcyoHZyBRWAhJHsuL1zg0pLWVzdJSLz2GSH3BRTW1i05v7TROagNP3l9zXtsvJNoA9SysrQevDzROBXmnh2WuSNYbbuDNsk9bwTCdTbj-SxY3ulJEjguoBs-921ki37LeFMLFT4d-X5yEfqGtL_3SGaQvaHKrn3-8calySY3vBj9-Ys9JodsSBWqLxrY9KN7QKxCIEhjp6u3JKTSeh-54JeIRvtzOYwKpzL51K49r8WPsMJ_VKrzjZZN5yjhs_WkdN14DtntOlr1Yj-fieDPXhutuMktNivIug7_Jaj-t1NffNTF2jpwHVzqaX6EJp0bfoSGryffS1Frf2qKKxPfvGlvz8Lxn15Jfaiw2xekS-OJFcI9_1MkDgnMvjZJkqfOcLI9UQiATRAKe1n7EwZmEtK-L4dg5JVKGk1sjj6v8EcMll8wMf42Ynv4kasYDV737WTkWzfpIGKJYeu8txbEK2IDZtAsUecwQdGvj2zzeAYr7HbOf2NcocsBg-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
صحبت‌های تند پایان رافت پیشکسوت پرسپولیس علیه علیرضا بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/100732" target="_blank">📅 14:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100731">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa83d99e99.mp4?token=cKVgnYyktirG7oskayB93BAnZ3r-0VvsF5wsMBAG8WWI3YVD-m-YJz8v1Y2GD1xBbAJia-PQsSKhpQD6Z1esPgIdukzHGkOW33rqVav2mrdUs6rS_B6s3k42-wMjIRPc5AX9Cr_thA2v9xKhv7UCT1la-mItThiP6Uap9YBsOc4zVvdWIu8-jIYqTQuQZwlun9jSJV266TxLNFsEmY8Pa1vJXpEpqh3nVyQBHr4UCZQV2AvI0nufUoI0Tyy_4wbCMYFbkPQise-YEYjzZ73ryOllcIzGDJaVd_zTTX-C7v10QbFvnLNoPsN3pdsncyvUSfEJEBht4RHC-Bf4LXqxSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa83d99e99.mp4?token=cKVgnYyktirG7oskayB93BAnZ3r-0VvsF5wsMBAG8WWI3YVD-m-YJz8v1Y2GD1xBbAJia-PQsSKhpQD6Z1esPgIdukzHGkOW33rqVav2mrdUs6rS_B6s3k42-wMjIRPc5AX9Cr_thA2v9xKhv7UCT1la-mItThiP6Uap9YBsOc4zVvdWIu8-jIYqTQuQZwlun9jSJV266TxLNFsEmY8Pa1vJXpEpqh3nVyQBHr4UCZQV2AvI0nufUoI0Tyy_4wbCMYFbkPQise-YEYjzZ73ryOllcIzGDJaVd_zTTX-C7v10QbFvnLNoPsN3pdsncyvUSfEJEBht4RHC-Bf4LXqxSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسکالونی درباره مهار یامال: بهتره توی رختکن حبسش کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100731" target="_blank">📅 13:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100730">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64bba4d4c.mp4?token=SECiJBREK9B8RoLWgFTVGSqjNJIEZNLigV1MVQeWozSXeN9oQx1fZL9indROEcR4LBajB7g5G6yWQ6RzXpycSuveJ_4Vta8HvVzEXe6tv4ChLBcmVmiAy8MK1Qn0fByCFh4siKma6r3nNMmnGnFh2jP65BMLDyx5i7BPNjmVRyFDHAF4thuypqBqoa1UaYRJLrSkf7BlnBo4DQk1C66VLyf167NbhxS_w591dTBOzCiWOTld0gv9uM-adOOUXZb71STOFLiGA6recoh3o2LRhzlc50oV0PQyPhNeNyIMNDs25v6v9JHEDSjruVjbjYsufLacrkwkWh2YjDVu8MFTOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64bba4d4c.mp4?token=SECiJBREK9B8RoLWgFTVGSqjNJIEZNLigV1MVQeWozSXeN9oQx1fZL9indROEcR4LBajB7g5G6yWQ6RzXpycSuveJ_4Vta8HvVzEXe6tv4ChLBcmVmiAy8MK1Qn0fByCFh4siKma6r3nNMmnGnFh2jP65BMLDyx5i7BPNjmVRyFDHAF4thuypqBqoa1UaYRJLrSkf7BlnBo4DQk1C66VLyf167NbhxS_w591dTBOzCiWOTld0gv9uM-adOOUXZb71STOFLiGA6recoh3o2LRhzlc50oV0PQyPhNeNyIMNDs25v6v9JHEDSjruVjbjYsufLacrkwkWh2YjDVu8MFTOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏆
استادیوم‌های جام‌جهانی یکی پس از دیگری درحال کندن زمین چمن‌شان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100730" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100729">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_r0AtnwUSXcQ5E422YydksIEmMA8qlNzaQUOte9e7H6iZt_NKg-VCjt2a2k7a6z3F_QdriwfwND4tlJKYN67WekFwGrIIa2RpmIy6gnhnJeuzLHvlml3EaaHKy5SXqKL4yE05Q6Z5zmNp5mJcPHfwIai5aIkMnEQMiMPOi_Pa2qQX2TXQ2_PClfMRw42eNP9IbOTvikz6DqALDdJd7HXT7UAFVZsdviI_w8e9xkJi8mwEV3jD8kWNtJ7l7Nm20CdPZZAhllhXOpYHf0UkVwemeioJqDuVG0XZ7q8n6i9S2tGlQVKmd0n_fi6snuSmsrc4PD2-SoLzNM7beIKUoPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طرفدارای گلزار کم بود بلینگهام هم اضافه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100729" target="_blank">📅 13:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100728">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6593b1cf82.mp4?token=etJ1X-69yr3WE6sJwZax8wQWvEDGeM5oZLmnHcf8e7xPkb0hha5nN54i4VZhjfp9Pz3aj3Tp0qRIx_jNiWQe66_mGCE8WElK110KnAXqTytohORkTkm5EOGsjZAkVyqOhJ10r1jasPNIviIJ0fEbRkYWetH7d02--oNyetjoPMgUzYUqZ8zmJUY71kM4TMM8fU3zx3jXnd3N2rQ8sX8WL3OSthgouRf_pKQFk8IMa7jON8BCrNRg9pfp2TADP_LGCtFHglDuuEXyHih-o3lCMiA3LevCbgadDOhjbO9WOMYr7nDzQf_zWe1W3pCCiaNIi3LPi1cbIWHo1_kgqSrmmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6593b1cf82.mp4?token=etJ1X-69yr3WE6sJwZax8wQWvEDGeM5oZLmnHcf8e7xPkb0hha5nN54i4VZhjfp9Pz3aj3Tp0qRIx_jNiWQe66_mGCE8WElK110KnAXqTytohORkTkm5EOGsjZAkVyqOhJ10r1jasPNIviIJ0fEbRkYWetH7d02--oNyetjoPMgUzYUqZ8zmJUY71kM4TMM8fU3zx3jXnd3N2rQ8sX8WL3OSthgouRf_pKQFk8IMa7jON8BCrNRg9pfp2TADP_LGCtFHglDuuEXyHih-o3lCMiA3LevCbgadDOhjbO9WOMYr7nDzQf_zWe1W3pCCiaNIi3LPi1cbIWHo1_kgqSrmmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🎙
جان تری: "برای من که اصلاً هیچ‌وقت بحثی وجود نداشته؛ من هنوزم معتقدم مسی بهتره، فارغ از هر نتیجه‌ای که تو فینال جام جهانی رقم بخوره."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100728" target="_blank">📅 13:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100727">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd66519b.mp4?token=lZM66hKKaR8BvHYrpFfDpJ9rbcj1EgEidJrhP4OyKucbV7Hev4X5BCBVXj5l0nqhBzupCQzeboALzFaFVBqOg7EOkMrnlP8tCg92WCaVoHiffu-ARkvTZ9pw9NBpc-i8jE_9MJ9fAVPgyhAixryIMnGqX1EWRD9rsaH7q4d4-6iRk1tVaJly9v8TdemHhSTrUyjF2wibm3dUjb1ZGIj2OFg8QyQF6N_RMIH5sTWGD3zqczkHrerSH5MQVSnh34XtRuvJJFd-aazSOrBaHZcSjgIKYPbrGokqBAVk0k9Xa8ssnkoxyolZEwvRAFF5Ian9aAlwbkuUKYpBSvYWP7l5AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd66519b.mp4?token=lZM66hKKaR8BvHYrpFfDpJ9rbcj1EgEidJrhP4OyKucbV7Hev4X5BCBVXj5l0nqhBzupCQzeboALzFaFVBqOg7EOkMrnlP8tCg92WCaVoHiffu-ARkvTZ9pw9NBpc-i8jE_9MJ9fAVPgyhAixryIMnGqX1EWRD9rsaH7q4d4-6iRk1tVaJly9v8TdemHhSTrUyjF2wibm3dUjb1ZGIj2OFg8QyQF6N_RMIH5sTWGD3zqczkHrerSH5MQVSnh34XtRuvJJFd-aazSOrBaHZcSjgIKYPbrGokqBAVk0k9Xa8ssnkoxyolZEwvRAFF5Ian9aAlwbkuUKYpBSvYWP7l5AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
هواداران جذاب اسپانیا در آستانه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100727" target="_blank">📅 13:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100726">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVGinc5dm49l9YEd0OUVutMV41Z_A7Efy8LcwOzfRGegimR7wlGcJqn5jUL-c0zXNN_OjKP8RpJJ5DHONUEdKmarm8_PKDliiJuzZ1p9-WGrIp03aynDtm3qe4dZ2WmM6E3P7nSHl49HcYKITuJOUv6QNCQXrcjlwJT8e34xpjG1iluv21rqhZCvHp5Si102jygY_mjGsJrF1-GH1Fcx0YhPaSl8gjyuiuykx7J2JAnpStGaxW0DIwTsNoKRzBtNRygMnhM7WtYcYe4XbbIj5m3Q7WauYRGhVS0QvNE0h1GfQ5lvWvRYx5kAIY8gAqsAQ8Azg-k9GmPr87Z_r1ON-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
رئال‌مادرید قهرمان جام‌جهانی نمی‌شود؛ در صورتی که کوکوریا با اسپانیا فرداشب به مقام قهرمانی برسد، نام این بازیکن در فهرست چلسی ثبت‌خواهد شد چون در فصل‌گذشته برای تیم‌لندنی به میدان رفته و جزو تیم چلسی به حساب خواهد آمد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100726" target="_blank">📅 12:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100725">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32d7d110aa.mp4?token=Y3rnh7L5r2QE8yNVpFe10feNsXA_N5zof2_c4msqmvHI3F96allrOrXT3jm50XuAnRD4KouP4DUrsWHgxQ59RT2uqa5k9mbPoWjxxYL22XV3F0w9UWhxLRo6teZWSfAYOfwvrw6WECR63w_y4Gy6isnjUfAJ2JXjih8hZ6b1cWDJHCx8xOpgAoTdcgPsxknRx-MM4g0_Ikpx1rEZX2TGST_VdoZQhfhFb7kIw6cyf8osXBr0cNeEkzaUsQfRT1kLDsuv30ORgSYUeRIk7RqHENG75WWbIsYz8r2xFGZWHULDHRmadszj1olAqwbdzRZH1Xb9d757QK-rYpClHbN_qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32d7d110aa.mp4?token=Y3rnh7L5r2QE8yNVpFe10feNsXA_N5zof2_c4msqmvHI3F96allrOrXT3jm50XuAnRD4KouP4DUrsWHgxQ59RT2uqa5k9mbPoWjxxYL22XV3F0w9UWhxLRo6teZWSfAYOfwvrw6WECR63w_y4Gy6isnjUfAJ2JXjih8hZ6b1cWDJHCx8xOpgAoTdcgPsxknRx-MM4g0_Ikpx1rEZX2TGST_VdoZQhfhFb7kIw6cyf8osXBr0cNeEkzaUsQfRT1kLDsuv30ORgSYUeRIk7RqHENG75WWbIsYz8r2xFGZWHULDHRmadszj1olAqwbdzRZH1Xb9d757QK-rYpClHbN_qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
خاطره سوپرخنده‌دار علیرضا فغانی از پیروز قربانی؛ بهش کارت زرد دادم؛ داد می‌زد، می‌دونی من کی‌ام؟ من کاپیتان استقلال پیروز قربانی‌ام
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100725" target="_blank">📅 12:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100724">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050e680fa7.mp4?token=nOpw7bnurmge1fFaOZeIvOiW90W3_48-VJfGenDrZVbJsEQwXZspHLUpaTSokIsX8XrwjrUBuZ91iTXBAnqzR7HBtCamlcpu9hpyzCcgHA6qsqvivv9hHaWFpyFIUfn5LSytfmndcKIWKYrgQOKJ_sTGWDQ0m6oP9n6uv1m9OqzSpppW-0Ghj2VV_TGmLtVBN0FOHP507YxKfyoRBgyZbswehY_A1V4I04thv2VtD_dvyy7lUH9poDpV9x6iJXD1GvaokeWBMV9Cg5M6hwWt2evFEjUEbL22hA65udUPUfmx7r_GG_Lteao7pPljUeiz4XgQfxej21W8ZOz66Z0NQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050e680fa7.mp4?token=nOpw7bnurmge1fFaOZeIvOiW90W3_48-VJfGenDrZVbJsEQwXZspHLUpaTSokIsX8XrwjrUBuZ91iTXBAnqzR7HBtCamlcpu9hpyzCcgHA6qsqvivv9hHaWFpyFIUfn5LSytfmndcKIWKYrgQOKJ_sTGWDQ0m6oP9n6uv1m9OqzSpppW-0Ghj2VV_TGmLtVBN0FOHP507YxKfyoRBgyZbswehY_A1V4I04thv2VtD_dvyy7lUH9poDpV9x6iJXD1GvaokeWBMV9Cg5M6hwWt2evFEjUEbL22hA65udUPUfmx7r_GG_Lteao7pPljUeiz4XgQfxej21W8ZOz66Z0NQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👍
لیونل‌مسی تو مراسم‌ شروع بازی با اسپانیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100724" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100723">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38913219e4.mp4?token=FbXtNADPOLa-53iQp2mmDE9jIKB41jVhV_tz0Td0y9w5jlNMrqOIdWXLjSkCVqNsoYI7GzEmGMdxhN8gXXAaSExwZ442gcKIqHTtO_u0I1v-NlTAATuDaG9lnDl0T5tL9NJoyaRsX6Ykz7qcs2KjpKMttoQpM3dfFl-B3WBGAOxj_kwRGuIq275l--33W6WtvQzlYNwCfUh7ECgLZpInj-rysiZZJYgN3ZjyRb72A4UNmtMD1PmhdQtT4NA73dSSnyqf8nmSjgdfl5s238yysjniupVE6jK9I0SWULKyZuOG_qyXAvQHesVf2l76nX_cyxSrolapt-SOl2tmt_tpNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38913219e4.mp4?token=FbXtNADPOLa-53iQp2mmDE9jIKB41jVhV_tz0Td0y9w5jlNMrqOIdWXLjSkCVqNsoYI7GzEmGMdxhN8gXXAaSExwZ442gcKIqHTtO_u0I1v-NlTAATuDaG9lnDl0T5tL9NJoyaRsX6Ykz7qcs2KjpKMttoQpM3dfFl-B3WBGAOxj_kwRGuIq275l--33W6WtvQzlYNwCfUh7ECgLZpInj-rysiZZJYgN3ZjyRb72A4UNmtMD1PmhdQtT4NA73dSSnyqf8nmSjgdfl5s238yysjniupVE6jK9I0SWULKyZuOG_qyXAvQHesVf2l76nX_cyxSrolapt-SOl2tmt_tpNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
زندگیت مثل گیم شده، مرحله به مرحله داری پیش میری. الان به فینال رسیدی. آخرش چی میشه؟⁣
مسی: من این گیم رو جام‌جهانی قبلی تموم کردم!
😎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100723" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100722">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e94327741.mp4?token=vxBIDwFaCWhKhWppsutCtvk8jEhKb9Pf4sporukyqc_sAlgA54_s4n9TIArpT15MeSDW8hjwuAp3ckmN7LbrnnKLKJic7REQ9yroUu24ivc7gFFFPIH1qfK3S81Neaqxc4aOJBZuBWDEEVBS--1kJHDe_DMyyhji0BAUbqVr8wEs-c-sZxr2kmhnDaoe0AUAYXc-wW_H9ZRZcVU_ns4clnE30C3d-uqDbQ9o2bwrPkadUhxcVk4WPHdsUG8FSHv2ywUJIi6buceppsBBh6jjBb5UwenPhCF6nM7sr5R3HbKfGkvqWB9VNpDlX7uD6nrF0cB1S62YO4X8DX9SwwdKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e94327741.mp4?token=vxBIDwFaCWhKhWppsutCtvk8jEhKb9Pf4sporukyqc_sAlgA54_s4n9TIArpT15MeSDW8hjwuAp3ckmN7LbrnnKLKJic7REQ9yroUu24ivc7gFFFPIH1qfK3S81Neaqxc4aOJBZuBWDEEVBS--1kJHDe_DMyyhji0BAUbqVr8wEs-c-sZxr2kmhnDaoe0AUAYXc-wW_H9ZRZcVU_ns4clnE30C3d-uqDbQ9o2bwrPkadUhxcVk4WPHdsUG8FSHv2ywUJIi6buceppsBBh6jjBb5UwenPhCF6nM7sr5R3HbKfGkvqWB9VNpDlX7uD6nrF0cB1S62YO4X8DX9SwwdKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه‌جالب از لیونل‌مسی در بازی با انگلیس :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100722" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100721">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXBiZPZj7MmHEhhZ238xYOSbZl3TlQVZOH_kvyR3RnsvJEZ8_V3Jo_yMqUdrweWABYxw245lf9tBZpugqWcyxL-YmLsTMwMO5xl1zNPNePf_n5HBeTl38YSUU88nmzt4tQrLtKnMAb4BzgndK4u5BP6lDaRyxKaOjZLDRRmZj0k8DZbfRZ3Y0AgMGuBdn_gsspl5S9gmv_HQV4BeBwGSPiMHTPBvfkMPFxoVlWqEEg98SPf4H0zSMLoYqz8Xk1jROQSYEB6gM2oL759He8ETW0hXICmAhpgNVKMAcgzAcFSP2RbfV_DBR16QBOTnepfGYF03cD0tBT0XpAmNCn9zwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇪🇸
نمایش هوایی جذاب در نیویورک پیش از بازی حساس فرداشب فینال جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/100721" target="_blank">📅 11:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100720">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBBEQZp4aIS-gEHbiO8pN2PW-xwV8mk5K-ubSmLnRFxL3sTAWvxUhhK3L7H_hAEbZMxOP-UOU5ZR-MjPa0a6F7qKqbzUmYXIovVwruKqK23wLghQSQQ84B5O1fOqsfSMdtuxF5WSJwJeP_mSff6xBXwzw6W6x0EDc0d4SDMYzAUhk-4yc6srMx-bm0LmrPJvb6JpLMkAyWX1GIX6Vg3zT6JqoYYiVha9mUjSre1EsW7arfW8LHB6Z8BWRXw3ZHPLho_TqsNy7MWZARisp6UeehTBVqf7MU2z6cK5MTNQNqWnWcf7vFYZ0ZiRy-BwrY-XHk29EoEseZB8shWXwfnyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید نحس
😂
😂
تیمای بازنده عملا قربانی اسپید شدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100720" target="_blank">📅 11:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100719">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474e4374db.mp4?token=gjIqC8eYUZ11a7VrmLuhiy0qxtfGeJ7gt6ry56vwBBtfjqFGweD7gDvGLOgYJCOKtT47mijDl96Pjwe90IwYVd0PrFyshI6Xy65-10OJm22ZbAXAdq5yKgcOCC-df_mn8LUe3PJVWwtFcsqrZ-y0QsbIKDvSgC5jRkAofxQL53aefltlk6QzEtXhuoF7VhX-WXDaKWAWVHc9HXplk2fW1wrM5M-LVXDORD2mmZdKjx2dJ1ywfWTEg6_-nmHIkdeQMokeC6bW_FPrYkap8qGP85ofznrDoN1Ynn7LI6Xezl1x_ecQEsyrHwltqkVFETUQBw4e1P9WT756GQPe-2nsTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474e4374db.mp4?token=gjIqC8eYUZ11a7VrmLuhiy0qxtfGeJ7gt6ry56vwBBtfjqFGweD7gDvGLOgYJCOKtT47mijDl96Pjwe90IwYVd0PrFyshI6Xy65-10OJm22ZbAXAdq5yKgcOCC-df_mn8LUe3PJVWwtFcsqrZ-y0QsbIKDvSgC5jRkAofxQL53aefltlk6QzEtXhuoF7VhX-WXDaKWAWVHc9HXplk2fW1wrM5M-LVXDORD2mmZdKjx2dJ1ywfWTEg6_-nmHIkdeQMokeC6bW_FPrYkap8qGP85ofznrDoN1Ynn7LI6Xezl1x_ecQEsyrHwltqkVFETUQBw4e1P9WT756GQPe-2nsTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سوپرگل میثم‌تیموری بازیکن نفت‌آبادان در لیگ‌یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100719" target="_blank">📅 11:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100718">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEclZgKB5oGg21wAZVWgNlZVre2NSaMNQI-uqXAWLhNWWTOiZ0irdIombHeu_SSRYkjzKkKAJuQnUJGhr2ljIwgAqtnjT-Bbr-E0u-caqlz84sljYrlXjQulLbXbsIYPSAd8ArF9IxHTQJG3TT08wtz747lp6Rn1VsuVc50YNmcRl2uFc3sBvqj8XPbE9aJU0kV_WjWD706MmvRpJkS4ZXybq6SbQAxNgk8j2aOd8LkTUBWBV1HtWpzLspeXH_57CTusH8ra6iUWO4T6KiZUSVxYJOnNq-VCdcs0zCn5tcpLfr7n562wbZ_xzrPlNsXQBrD6VJgHOTVhEmUm_zRoOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از نشریه بیلد آلمان: اولیسه در تمرینات فرانسه به بازیکنان کشورش گفته که فصل‌آینده قصد داره راهی رئال‌مادرید بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100718" target="_blank">📅 11:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100717">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c0ee7122.mp4?token=p6h17OJlKVrvGIrRuvtEJfJ_T8xhD6xRVLEcWDMIZI8Rn7OMpyQfj5ADK_un-1y-Q413JlzgmRBoNSRnJLaqZ2HB3gh6RIkYw-rXUcJ95issYFmxOIKxVnR09ubgRG5QeZTkYqlTUXFYEWGA-2LA906IOMD6wyOTn4GGXGSD5-JtaX4Gn4S-Vn_denMie1fzxBSW6TahKY9dhvnq4hGQPHfJrOUAL9mw24DyNrmbhvdq3qQOUZbNwIkQsI2baOapHT31RzNsYEgqh9RPjnjTC8NVYX-wUpZlMzk4w89-PdkUV2O-0zyGBoszIHBG9K5v2leU_ViChAhmeJzmPi7_YIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c0ee7122.mp4?token=p6h17OJlKVrvGIrRuvtEJfJ_T8xhD6xRVLEcWDMIZI8Rn7OMpyQfj5ADK_un-1y-Q413JlzgmRBoNSRnJLaqZ2HB3gh6RIkYw-rXUcJ95issYFmxOIKxVnR09ubgRG5QeZTkYqlTUXFYEWGA-2LA906IOMD6wyOTn4GGXGSD5-JtaX4Gn4S-Vn_denMie1fzxBSW6TahKY9dhvnq4hGQPHfJrOUAL9mw24DyNrmbhvdq3qQOUZbNwIkQsI2baOapHT31RzNsYEgqh9RPjnjTC8NVYX-wUpZlMzk4w89-PdkUV2O-0zyGBoszIHBG9K5v2leU_ViChAhmeJzmPi7_YIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇵🇹
علاقه شدید پوریا پورسرخ به کریستیانو رونالدو و عصبانیت او از تیم ملی پرتغال بخاطر ندانستن قدر این اسطوره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100717" target="_blank">📅 11:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100716">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71ebbda285.mp4?token=sUT5MGR-tYxm3x52H2Wpk5UvY2cgGF50dgvyp6iyvumLWl86vaQgEgT3chq_b2WT54opTY1alsJYxiW89KpHnGi3FsM1C3UprCCMtMWPyDh_R_tsPpmltojjh3D_J6KRMWDN3D-VW41_teO-UJimMnI_IgQ8NMUbijyBCuWlp-ZtIqXYbR5kGVp7_Z4vPh0944I0cUM8Gn7Fo7tLVnBmDqluUxcbA2t5IswkG8FqZfSRfpezSBpwzAvmF9nb7pXIJhPxtpr3olZahebgIOKVc1_OU5GL0uI7IwF7f3IO3hBgDqA9L-pyI-B5fdNBAwXMB9fSQdXZycR8XUue0I3oqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71ebbda285.mp4?token=sUT5MGR-tYxm3x52H2Wpk5UvY2cgGF50dgvyp6iyvumLWl86vaQgEgT3chq_b2WT54opTY1alsJYxiW89KpHnGi3FsM1C3UprCCMtMWPyDh_R_tsPpmltojjh3D_J6KRMWDN3D-VW41_teO-UJimMnI_IgQ8NMUbijyBCuWlp-ZtIqXYbR5kGVp7_Z4vPh0944I0cUM8Gn7Fo7tLVnBmDqluUxcbA2t5IswkG8FqZfSRfpezSBpwzAvmF9nb7pXIJhPxtpr3olZahebgIOKVc1_OU5GL0uI7IwF7f3IO3hBgDqA9L-pyI-B5fdNBAwXMB9fSQdXZycR8XUue0I3oqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
🏆
کوکوریا در انتظار تقابل با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100716" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100715">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3GoyR8P6lAGWkxU5K1FoVQP8oJpG4r53GoP5bLkYuldy1RUUlYz1JM8U2scCiot5Fv6qXi3yGbrRyduR7YENNlSvJ_DoiKba8CnC6VN4UuKNMkPRBLtDgCB64fz87qhnhzLZBJZ1CQYL4caSsyL-R3oD20Jod6tg-ToR8j3V5M63hIMU1LiOq0VROVi-5j1HCVfunA6Tik19gUiV3JbolrVM4ZUnfspo_sBOGbLcm1miFOzsS4PG9garFcwxzhlC4mudnkVM8idWIoW85vWlP8Ax4wLdR2iOlkpU_VLE3CZkfLow_xRpEsiQM4S9_93DPafaF--gzd8Mx4o-xLKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان‌دوران انگلیسی از ژانویه ۲۰۱۵ تا به امروز در ۵ باشگاه مختلف بازی کرده
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100715" target="_blank">📅 10:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100714">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638800ce9d.mp4?token=jenRR6XxTCSIfhRbYHexVqnVArJ21LlklDQ8cjTzkD8IGL73jwhwJJ7ytpv_gbOc8FneF0uwUMhskkmeLEq_DZpK4hYT1NWQyuby04BlINOmZ5oCiWe_P0ht6BzBcEAud4Wrvih0rOuq3CVDS6tsAjK5Y_lyq5qwwf_s0LjAY0zO4xBMS3ACkSw1pyY90qRAhuG2fqSu40-6il9ENmEbrYXExbkbtieNfoa3RgLOnwyPDW3L7T5baU6ZninqUa3W6YMF51nxs0seEn9V-hssWWZJNBvACTOPMWkvozaUQQGvV7tZkg8qtur2FUjdTzPThGwABPqbrcC3gmCmZtVM6l55OCV2HS5ird87-C0flwUY7JSCQ_EMwzbbnsqjmeScbyx-1SX6-chKtqGu0PjeenZaabSRoysuG3hSSw_B8H3aKSQpKuLo0zDZzOc1kXvwUkjTE_johE4tb2nDPZlPBYxGrzqo5xx9SeCQu2GFN-dyk4VhDgmYe5zF5VIgt2-L948-9Ou5lGj8FxrGXWs_lLtzFQQ_8tSgUnh6YRxzNN-KYD5WApNP_4OSUFJIxEk6BWp8FvuyhGi33KCJ_CAFLnE6bPVm8Dea21V2tUxTYPiuz98pmwK66a0YwkmLlCElZuRwZgnLnbJrZQYqsJHfH9-5ooBKvrhttsUzXTyOQ7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638800ce9d.mp4?token=jenRR6XxTCSIfhRbYHexVqnVArJ21LlklDQ8cjTzkD8IGL73jwhwJJ7ytpv_gbOc8FneF0uwUMhskkmeLEq_DZpK4hYT1NWQyuby04BlINOmZ5oCiWe_P0ht6BzBcEAud4Wrvih0rOuq3CVDS6tsAjK5Y_lyq5qwwf_s0LjAY0zO4xBMS3ACkSw1pyY90qRAhuG2fqSu40-6il9ENmEbrYXExbkbtieNfoa3RgLOnwyPDW3L7T5baU6ZninqUa3W6YMF51nxs0seEn9V-hssWWZJNBvACTOPMWkvozaUQQGvV7tZkg8qtur2FUjdTzPThGwABPqbrcC3gmCmZtVM6l55OCV2HS5ird87-C0flwUY7JSCQ_EMwzbbnsqjmeScbyx-1SX6-chKtqGu0PjeenZaabSRoysuG3hSSw_B8H3aKSQpKuLo0zDZzOc1kXvwUkjTE_johE4tb2nDPZlPBYxGrzqo5xx9SeCQu2GFN-dyk4VhDgmYe5zF5VIgt2-L948-9Ou5lGj8FxrGXWs_lLtzFQQ_8tSgUnh6YRxzNN-KYD5WApNP_4OSUFJIxEk6BWp8FvuyhGi33KCJ_CAFLnE6bPVm8Dea21V2tUxTYPiuz98pmwK66a0YwkmLlCElZuRwZgnLnbJrZQYqsJHfH9-5ooBKvrhttsUzXTyOQ7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
آخرین وضعیت پل‌‌ها و تونل‌های هدف قرار گرفته شب گذشته در استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100714" target="_blank">📅 10:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100713">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e91953d632.mp4?token=Upxe01j-C2CClkZyPUPN9gKztpwEgGhCMv3MTB9b2WUquIwJq48XXfcX42C5ZDVlLBy2rr3A3hou-Pptk1n11y7RWvm2HJhGx7FUzAWZry5mnIGmcLHfN6aYBZVCsZwooISjEQsGJd1G21n_3VL35TwyNOqi4bG-HkKKcF0LkQ5Mv9SudDeZBPt9mkP89oewC-Ooehq0qeifH1OKqDpuLCbKX77Jl47TxT1lhOIyfSMQq11fcnho0uPZUePlNov-jQth6KmKPDiEXjknFJkxB9srkI2ttpjhsBJsDxfZmu_olhEL2MqGWwUUcJcF8P4pN8Esl2z43Y2NyEoLNeEq1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e91953d632.mp4?token=Upxe01j-C2CClkZyPUPN9gKztpwEgGhCMv3MTB9b2WUquIwJq48XXfcX42C5ZDVlLBy2rr3A3hou-Pptk1n11y7RWvm2HJhGx7FUzAWZry5mnIGmcLHfN6aYBZVCsZwooISjEQsGJd1G21n_3VL35TwyNOqi4bG-HkKKcF0LkQ5Mv9SudDeZBPt9mkP89oewC-Ooehq0qeifH1OKqDpuLCbKX77Jl47TxT1lhOIyfSMQq11fcnho0uPZUePlNov-jQth6KmKPDiEXjknFJkxB9srkI2ttpjhsBJsDxfZmu_olhEL2MqGWwUUcJcF8P4pN8Esl2z43Y2NyEoLNeEq1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال رفته داداششو برده آرایشگاه قبل فینال موهاشو رنگ زده
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100713" target="_blank">📅 09:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100712">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2382f600b.mp4?token=MkWPpRArSPSrxqMK1My-2YX0ikqyKF_BbY4khiD1-8UEMJFpVg-Uz9esgnzjV5ctV4ERPmq8mYh5xuQ3xr7PiIEcdDLodNpsv5DiACHjdq14-JzKVSkl79APvFxvq9hycC45F7-BjIavRauhhMC6kjOFCLr13oOn_SRYsOyIWs44FxCLz7hTHVlQYc6Vr8jfpXdZMW3OG9FlrLCG6OyCM7dFqQrmkzkkCdrGeTCxluVZ3uXvOTQd0de0odxrFPEI-kbo6XG55twbfPBT65Xmn8IGMaQaAcP8vL35oF1QiWJmjXD-336wMhWnGH7mJ9UPXOFUgIifBKRROCgj6qqOUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2382f600b.mp4?token=MkWPpRArSPSrxqMK1My-2YX0ikqyKF_BbY4khiD1-8UEMJFpVg-Uz9esgnzjV5ctV4ERPmq8mYh5xuQ3xr7PiIEcdDLodNpsv5DiACHjdq14-JzKVSkl79APvFxvq9hycC45F7-BjIavRauhhMC6kjOFCLr13oOn_SRYsOyIWs44FxCLz7hTHVlQYc6Vr8jfpXdZMW3OG9FlrLCG6OyCM7dFqQrmkzkkCdrGeTCxluVZ3uXvOTQd0de0odxrFPEI-kbo6XG55twbfPBT65Xmn8IGMaQaAcP8vL35oF1QiWJmjXD-336wMhWnGH7mJ9UPXOFUgIifBKRROCgj6qqOUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚫
افشای مکالمه مسی و بازیکنان آرژانتین بعد از پیدا کردن بطری آب پیکفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100712" target="_blank">📅 09:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100711">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dccbf84030.mp4?token=HTrFe0JFtLPpVojc0LSInKGDM3aQ-Dgo7yiwvm5gePm_pMubeQLy15LVWvRRttccS5jjkIreAuGEnvDLG56ZMV8DnZxJ45auInLrWnZvvc1cP5bFlUgnHCGwdLQTUtCyorC-WnBQNtHYlqM__UMiDezy6iCecF4_lYSnbviFuLMjpzHIAKMMlihE89qGnEPBgytEgZNmI4O-yxdMeg7ptA5YK7DBR7oN2TLwcuPtQUBx2snrDjuD3plPg1ib2EZXwUR_I58bkwW8xfHorOHLsKGmj6QopBuijjtlIaESqY0sbYNbL9ri5YniWAGsObxlnbL0ZpCZQw_CYobwlC1X0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dccbf84030.mp4?token=HTrFe0JFtLPpVojc0LSInKGDM3aQ-Dgo7yiwvm5gePm_pMubeQLy15LVWvRRttccS5jjkIreAuGEnvDLG56ZMV8DnZxJ45auInLrWnZvvc1cP5bFlUgnHCGwdLQTUtCyorC-WnBQNtHYlqM__UMiDezy6iCecF4_lYSnbviFuLMjpzHIAKMMlihE89qGnEPBgytEgZNmI4O-yxdMeg7ptA5YK7DBR7oN2TLwcuPtQUBx2snrDjuD3plPg1ib2EZXwUR_I58bkwW8xfHorOHLsKGmj6QopBuijjtlIaESqY0sbYNbL9ri5YniWAGsObxlnbL0ZpCZQw_CYobwlC1X0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
صحبت‌های عجیب وحید قلیچ کم‌عقل علیه عادل و کریم‌باقری و سلطان علی‌آقا دایی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100711" target="_blank">📅 09:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100710">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrZfVWpAp2RqbMyRAq7olAZfT8OANzXol_8WZsUDcNsRKgDJk3nNvpM1836_UcgzXXCKaJP2R6ptNrlSt4MNpVaAZZtgxXMEUzgnQuBtOAaQG4OihHmR6lWV1ScXUvRmnZbOogRwUTavqFD5QNYyUzV7k0Ziqmux3ZVHeHWSoA6d6Vpwn2HuLkSyyNxyLN_Oi68Pkax6p_6WIHYjYJCAw6tryBCkhxvvHSqIeFbGVFIM6k_-LEgAIXDqT6Z_tnpHYKRtIaYogWMabQmBVfLxm3zT7BNUTOijGPzjeJNpW7dyQXsHJF_TnnCBs0cMqKpq_NW4UUySQZuS1yEqteJqcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚠️
وینچیچ اسلوونیایی در جام‌جهانی فقط یکبار برای آرژانتین اونم سال ۲۰۲۲ سوت زده که تیم اسکالونی مقابل عربستان شکست خورده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100710" target="_blank">📅 09:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100709">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnmwHvnpohJVVqL87NrZeaLN9jCEAU3TG-9XcohHQOieMaL6My-K4FlIosuqIPihsaqLxOjioSxKaBlSY0788bojHbFMj7wGBbEshJ9myD2sXhifZDVSqgQgM18RxbK63pKD-rkC4IfexnP9e4g3ksEmYmkqOQnN7A20uOY3sW2VJ_vZaKEpeFHHbVUvXEll-XiqeeDE2xUGLxmA76-_92NLBsNSWqHwKMCBQxEL-IoWdDLSWBbEiSxVpHrspJZNjC3TzqbXS15JmnLVuZC_zdA16idlCrM9WtUlf1KKVh2MJrm9n3HvH8RhmCOYwYnqlLp5_Z67DE75qHStI7JCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
⚡
تو این مراسم همچین قابیم خلق شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100709" target="_blank">📅 07:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100708">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136aac8a04.mp4?token=t9r1qPdEeu7fCF5GotPKRpgzdEKEyRYRXTqe9IA_sfjxm-x6yvNAU7PRPBKhm4eznXdUikVQG-Cy31MQXrtgeVS8CFsalh_l_8sbtXJ1QDRnb5djvQCMFwmg9-s64SZlTYF8tkPVYAc9lKrkX3JJftS9Fqp08C9ma0JfKLgygPUZcRf-C3xHLicwzpBJET-DYxk9RNy-1yaXuuQQHLYYRTiZ6KPCazAvbdFP-81sGGEBqMC7kVkafT3GWpzH23oGyRi7N1h5X4S5TuIQsH4EgbzS9BJyx6LZaQlPbvSbzqVDp4_T49Jx97sygDnTWD58JEYOqrOpT0q7m8NTcdRjXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136aac8a04.mp4?token=t9r1qPdEeu7fCF5GotPKRpgzdEKEyRYRXTqe9IA_sfjxm-x6yvNAU7PRPBKhm4eznXdUikVQG-Cy31MQXrtgeVS8CFsalh_l_8sbtXJ1QDRnb5djvQCMFwmg9-s64SZlTYF8tkPVYAc9lKrkX3JJftS9Fqp08C9ma0JfKLgygPUZcRf-C3xHLicwzpBJET-DYxk9RNy-1yaXuuQQHLYYRTiZ6KPCazAvbdFP-81sGGEBqMC7kVkafT3GWpzH23oGyRi7N1h5X4S5TuIQsH4EgbzS9BJyx6LZaQlPbvSbzqVDp4_T49Jx97sygDnTWD58JEYOqrOpT0q7m8NTcdRjXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور بی خیال آناهیتا درگاهی نمیشه
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100708" target="_blank">📅 06:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100707">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htk9Ew4rmr4lN92Z1zvJcMg2WHcPuXzIm83Oh5uCdv3wxglgH3jnA0zNMMkyJLE4-OEbhs7ULxTVzuatxZiN1VBQGaxwMlbGzXfOiHA6mEJoRgdClGBErQhXS-YWmaNbglrtcGMkyAm7L6G7isckFdSWAuFsVt8eI98BOJAzYvk8MP3ttOY8vvD5JQiQJbMDF-PBa_PMdU9jU41WRnTSPc-yhYNfGaBxhKytW57yF22wIKtxXzD1nPjmiIrori20SiHXydsUbDGRJpbHue3RQ14y90xgwhlgF5qnp9_gboAaGnQohhqs1hTOenamRUHkwLwHj7kOScttipi1E7B5FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
👍
لیونل مسی: از بچگی یاد گرفتم و فهمیدم که آدم بیشتر از اون چیزی که می‌بره، می‌بازه و فکر می‌کنم همینم بهم کمک کرد تا چه به عنوان یه آدم و چه به عنوان یه بازیکن بزرگ بشم و جا بیفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/100707" target="_blank">📅 02:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100706">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdiJk6manYethXKxADFM4MbPpjheKQTNrH171chwR7MO4d_U82pQbNmvxAcS5iA6PMXbDZZeXNAkJC7WYHFbxhhuhNdc6_Mmjl3JCvThTd2fBs-yj8jchLEq26VrAVQMCyWJFlf8S4u2WNbeBY9w76oBwos79wwk2waIjhgHWUQKwrlELbx0yEcu7YbZnEEy8vH-KalKT2HsEpaD95ThQvIsWZ-nmDEurzORDEZx3S22Aar252SculPwP3hVcmWgC668P2OgE5wCkyGmrbB2CL3HDMAzhhcWXVnO1fuJlr90ttxFzwOMkkH57Nw-TpO-zOjAhQJOl62T1aFs8XV6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🎙
اسطوره لیونل‌مسی: بدون‌شک لامین‌یامال یکی از بهترین بازیکنان فعلی دنیا است. برای او آرزوی موفقیت دارم زیرا باعث پیشرفت بارسلونا نیز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/100706" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100705">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🎙
🏆
🇦🇷
اسطوره مسی:  ‏"ما اشتیاق زیادی به بازی کردن و لذت بردن از آن داریم، انگار که به جایی بازگشته‌ایم که از آنجا شروع کردیم، زمانی که کودک بودیم. حریف هم بازی می‌کند و نمی‌توان همیشه برنده شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100705" target="_blank">📅 02:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100701">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGax634jMFrlLcWF1-H7mklNVBW2XTkZC4fdao6PjqpcDcmuf991toUlXJtkPcTnQ0iudQIblHErgacED8rXp2Grqy9K83nsS3MTnJsM0Ny47qx8Vis4eB-S1dUb_dcAtRlEblmh0yJt3O8Of5UNDbtHbhakpr8np7yRtw1ZqWWEJalKY4m8x9_wFfB5Z519J2FrsnnG1ezNVbh43AIYdwXpGjiq5xjyPedwiykFid7q-_YsyX4gdORuNf7_LMPDU1ZDZUV0-1xbYHdIVNJeY-lDx4kzt0cPjIUMXhgD3qB5qad1DPnRdam7vE19E8nf7XPV00TNonupV7hYWIvHXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWNwek2Q_iEIlSSsPY6syj30gNyKzGbgCLKGaxzBBOhOp5zE1YEY5Z5R9P6z4x99qqfZv9b9i5L94jKd-WCesJtO6dlObJ7JDxj2DoaPY4lqa2WqSVjhOjySwQ7n_-yREIdOkW-knhdx-cD0shWBBA5EZezISXw8d198WStd5rEAZ4_3SloNcw_BzwNrHFQ_2gyfNNwniDSqOCJgQpa4Qa5nFhUUdRS0kdxHBslgv74OKW9_N2rPdOZnLdp1p9OEkshEOU3vQo8-B8AcPxvSuQr_b1ADb-jSIaWRUcS38Pz-drYHR6dEb56JnxSHX5Av-7hiVso_1LeUuNISmiyrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbLgfYPObGE8JyC2nAzEVklJCOMyTc0BdCx-_rJGbXVulSGowAPxCX_nOgZMQckT78n8GdQDflg3od2DjiZM4nefw8RUPa4Lah5OeytJ08UeI3xdKUg_ZYIBAnq4NLc028LfqaY0zkWsOMyPoa7u2DyDBj_ifYBGLtzgQiy_-3fAeq3E0WZz6j-I-NpJ2gSryqsst1avMvYB8UaE-K7CaC55WiF-_m8ZatAKIKYJRsBFIjun-TMSwJqL6icSL6V4RbsWlqKZ6-XCZ8PSTqDwPKFkK4kPywVOeCcrK7XiSmWVnGTOYKqvo84TGEsVtBd3IIImKecXNMrv9KT4JHa1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJCcX2dKE07iOT2Fx_13Vb15fMdkd4_Xs2trbCh_XwMzkF4nX7K-mg0WrN4aEsSqcsvj_2KWCsTTxf48sYzsZGM8UmwdSP0QApmeZiggPC9IdjBMrWDb-_tOPzQN03c40cYudJu73MlyjPhVBk1aI8C84iL6gPiMpe4REAjJmXW9JFv7cPeW88jH1L3HIQ1RPTbdWc5XqBJzqqVDwFt3fMwYu8hfHTRj05DtYCrMUs2gmIXOxxWS-uI27MucEJR3bRP_8lqmXJe7C8kfkYYzrd52viNHzc7chyDY72uRwe1wK86rxrZ6lcQA8p_Ijfw767w4cgxq-5ccHHi2Y4zMsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇺🇸
📸
|
تصاویری از مراسم استقبال اعضای فیفا از دونالد ترامپ در نیویورک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/100701" target="_blank">📅 02:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100700">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVAx74rAn_YjrWSfUy3_O3nXn3_SbVSEIvpY7g0iAdZAFqLzlDBkRRuWKyOEY1k5YKlHWQtlgtWa4PmB-X2wWuXCM2lIj2ZtXj_luX_wBoiX4edRAWV7RCIN_18xiiAcPktnXOwc-MpX2yzTvFh3JlhURwyHfXh8wNrnmY9g2Nn9WdVeimYRGd0ubmsV9xdNyt6mLzq1XknwL_GX5tTcGgzjC7H9aexb3dHTzkk0MyMWvfNA5MsTFhVGaOTlLKuw55r0YOff3VoZ-etW63RU-0wOf651bXu4qI5FooCUo7e7Wc3wA9wUmSrXARvvw_QvfKoVnp4miIsLaTjQdCNfGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
چند مسیر اصلی در استان هرمزگان بدلیل حملات و بمباران‌های دقایقی‌پیش مسدود شد
❌
پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرز
❌
پل «شور»
❌
تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100700" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100699">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-e_4kUeTQXIMc9R4BvV_om96MeHujE5mKcf35vC9FI7EGoVb172GKXR2h8CJwaQ-r-6ctzT_kIrrfUg0y6G0jAsqqZgU9YQrEMXqSY7Cbv4ic8USLyP7s3iiibpRDi78km0cwJbnF9M6yTjA6C939cMtt88McaJlTYep-x58zqTBL_3X0iIfMVFADoQwqjOZvDcVnJXk3HNgDh0J6vLvJsr0LLHUG9p7g2LEE9uXg_yrYdlBFsnhQB89dz9bQ9O0o9w52kklSkLBh_K8cWcgl1zyTOWsiSSDp5d9810yyxUbbbkJ_Xq_K-6csOeWrtmnmrBOqTgReI41d5KL3wU8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
🇦🇷
اسطوره مسی:
‏"ما اشتیاق زیادی به بازی کردن و لذت بردن از آن داریم، انگار که به جایی بازگشته‌ایم که از آنجا شروع کردیم، زمانی که کودک بودیم. حریف هم بازی می‌کند و نمی‌توان همیشه برنده شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100699" target="_blank">📅 02:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100698">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1fj24xZTjzp4VUR4czoMY6d3R4pPwa0EX2diKIuSRcmEpvszVERVus9luCWEa0FxBXulmCavvWnRg2Zhuy5pFhAReP6PPSBZuSZHU4M_fws0pij3FRxMvVstwQxCZYI2cUzBuc6I2crR_KALydqXxQmAZUtirzHYxTOB-dimUc97QbrAzqbxoy_-RwMQ_hHThymaR-gaXPy_JqJXNxHPVczQms3DML1rH-L0-Apo46zlfplVK2Rod9jzD1LvZOn68e3LmvvAKCnYMhfNZfWXDYmD06GM5HFf5SyVXktVYRcOojuDzaJxeb15-OvoTfawnZpi8KJSw5sVkbUyByqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
اینفانتینو: بنظرم جام‌جهانی ۲۰۲۶ بهترین دوره در تاریخ مسابقات فوتبال بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100698" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100697">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
چند مسیر اصلی در استان هرمزگان بدلیل حملات و بمباران‌های دقایقی‌پیش مسدود شد
❌
پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرز
❌
پل «شور»
❌
تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100697" target="_blank">📅 02:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100696">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfoOz1puQcPu0PFgayco7lzwtKBBuP6Bd77eq6Qc24i9EA-ehwtYmQOw7KKEB53CZJBK8kdoB8f62VOipfX3HAJqHkoSI8i_9lYkGAL_Dz8RUbtT0y-C0zOXUzrt_MvxxDhHI5i8Bqp9Az3EXqxMfxwKyrwXQSu_Lpfo_fp1GKGspPOBvr6fK1sLEBXMOC-_a70rC19FL3kfIoftALTiiFeEEYfus2b9V5yZMlYiX7ABt4E25PazCtkL1x-8Lp16ngpHEOs5-0XuQv1R6fG3Cccnos0r_XtEOoLGfbilE8eCzLXef6TnkQo4sD7cKDxPaPKNgjROsGJDxO-fin7Zww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😢
🇺🇸
ترامپ: دموکرات‌های احمق در انتخابات تقلب کردن اما من در نهایت برنده شدم و میزبانی جام‌جهانی و‌ المپیک رو برای کشور گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100696" target="_blank">📅 01:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100695">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🏆
🇺🇸
ترامپ
: امیدوارم یه روزی برسه میزبان مشترک جام‌جهانی آمریکا و چین باشه. چون فکر می‌کنم بازیکنا از مسافت پروازی که طی میکنن کونشون پاره میشه و جذابه برام
😂
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/100695" target="_blank">📅 01:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100694">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900b057c2e.mp4?token=X-d_QaN7smuS_a8MsIaZl3J9-0sFVUgZPfxsfv3O0QsBfQUv6oYKj5cB696Nyd4xi6kMZGY5i4nzdvkXmD2kI82kVHzhF_oQROzWT5wH7OpCwfJBUbVA65VWgsKrA42ZFCBy2cCfCLn0DrZNPXW4CsN8T7AGEPztFFiVXjWzCUERKsBKAedf8lH4i4yoVvNS8BDL0cA3sq3y1J6Q--yGHp4VWVIul-twoeIVkdBLpgJYWji8CSSEX5uQU42iwgserO497Xxvc6CZz0Sg6XgKXuLJJb_ou8fgH2f-uB4NVHh0QCn-GDaq98wSlKO3QErIQ_zXp6By8ljJxhFt8PIiFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900b057c2e.mp4?token=X-d_QaN7smuS_a8MsIaZl3J9-0sFVUgZPfxsfv3O0QsBfQUv6oYKj5cB696Nyd4xi6kMZGY5i4nzdvkXmD2kI82kVHzhF_oQROzWT5wH7OpCwfJBUbVA65VWgsKrA42ZFCBy2cCfCLn0DrZNPXW4CsN8T7AGEPztFFiVXjWzCUERKsBKAedf8lH4i4yoVvNS8BDL0cA3sq3y1J6Q--yGHp4VWVIul-twoeIVkdBLpgJYWji8CSSEX5uQU42iwgserO497Xxvc6CZz0Sg6XgKXuLJJb_ou8fgH2f-uB4NVHh0QCn-GDaq98wSlKO3QErIQ_zXp6By8ljJxhFt8PIiFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترامپ: هری کین بازیکن فوق‌العاده‌ای است، اما شاید در پست اشتباهی بازی کرده است
به نظر من، شاید آن‌ها (اشاره به تیم ملی انگلیس یا بایرن مونیخ) اشتباهی مرتکب شدند وقتی او را به عنوان یک بازیکن دفاعی انتخاب کردند. آن‌ها بهترین بازیکن خود را گرفتند و او را در خط دفاع قرار دادند. این موضوع کمی غیرمعمول بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100694" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100693">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=HAO1sEjUXcegcKR3p6Fb60mliA_eGmWXEyvH6LYT5hzT3PzMiaxUZqKA0-EAHjGgYEaa5_W82TzItktxmJu1M21yqRP1XxTIcWtRoJc5M7K_rLomDalJDPdL_b8QxC-MssPGG3gBlXkSfVY-0EERmmWE3CEaupl-Byw2Pi8I7BEzxZWCtxgxZmn6eEmrp-8nEGvNdulebfKSGBEyszZyOhhQ8tQzRgURjYGtsQEHh6MOMk3yzCz6nkDsrC1sGFGZC9AVf8Q0i9rY4ggr7pGuA2GuJFnq7GiDDFDyz0xK6qdLp2C--LRQPebnuJMlpq6JE2UjWzYpQJJ9ckh3rVb4Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=HAO1sEjUXcegcKR3p6Fb60mliA_eGmWXEyvH6LYT5hzT3PzMiaxUZqKA0-EAHjGgYEaa5_W82TzItktxmJu1M21yqRP1XxTIcWtRoJc5M7K_rLomDalJDPdL_b8QxC-MssPGG3gBlXkSfVY-0EERmmWE3CEaupl-Byw2Pi8I7BEzxZWCtxgxZmn6eEmrp-8nEGvNdulebfKSGBEyszZyOhhQ8tQzRgURjYGtsQEHh6MOMk3yzCz6nkDsrC1sGFGZC9AVf8Q0i9rY4ggr7pGuA2GuJFnq7GiDDFDyz0xK6qdLp2C--LRQPebnuJMlpq6JE2UjWzYpQJJ9ckh3rVb4Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
ترامپ
: من فکر می‌کردم که ما کشوری علاقه‌مند به فوتبال نیستیم. اما مشخص شد که ما یک کشور علاقه‌مند به فوتبال هستیم، و من فکر می‌کنم که این وضعیت همچنان ادامه خواهد داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100693" target="_blank">📅 01:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100692">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=CB54OtowYcwJAShypWr0ehnapRKVWt57JLU7t3pJdwLfSnNDvwEuAZAVzBw__VPF7Sl_YFKK0H23sTocS_cLhVS9IH_Ax98JDXSYvLyOfcokXAyaK70e-u2TFHl4IP6cnf0gyb53_uTEqtsCzrX1WaPnTpY-25Xr31ufq2tJsGDbY4iEFTiPUalbarzmwl01lk9wQOuTD7Dw3GmUmR3jJJGlxQifVsSEEfr5xmuGUA8dr5VuU3sO9ynabxXBrOk0B2YrqMGIzhI_ct_IJJKU7eJI0XasGAPU70hXMePI0blTqthogW0CWT5oUfH7UocXgDm-SzRuekBY4Cd6tR7nETIh2CxTq1yMkDuPEsGC5mG9rywy373x9VUTD_HJhDE_rYSUD1QlqF8E-e3AgHRU1szEDu9FTG7DQAB6WTcRURYAorA7mvYwllAVpr95-O4mqu-JUEOfWS0mArBbpKyYmWAuFy__gNv13NV6iZolJTAjhx8OiEbqxg6YnP_noRR0t50rEe2cEzsP6sRR1aI18m2hCaJbdoXZ9aav6IcHAKyslLXWFYbaUnb41kJC7AjTGEGuHUE-IKht709ZE1tqcGQTvfxexl4soStDb9siw5D88KLPC35QHC0ffAdwBsEA-1Bxr7ZK_gCjLvp-PklDviegg62KmE7xXLLPNZNs0V4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=CB54OtowYcwJAShypWr0ehnapRKVWt57JLU7t3pJdwLfSnNDvwEuAZAVzBw__VPF7Sl_YFKK0H23sTocS_cLhVS9IH_Ax98JDXSYvLyOfcokXAyaK70e-u2TFHl4IP6cnf0gyb53_uTEqtsCzrX1WaPnTpY-25Xr31ufq2tJsGDbY4iEFTiPUalbarzmwl01lk9wQOuTD7Dw3GmUmR3jJJGlxQifVsSEEfr5xmuGUA8dr5VuU3sO9ynabxXBrOk0B2YrqMGIzhI_ct_IJJKU7eJI0XasGAPU70hXMePI0blTqthogW0CWT5oUfH7UocXgDm-SzRuekBY4Cd6tR7nETIh2CxTq1yMkDuPEsGC5mG9rywy373x9VUTD_HJhDE_rYSUD1QlqF8E-e3AgHRU1szEDu9FTG7DQAB6WTcRURYAorA7mvYwllAVpr95-O4mqu-JUEOfWS0mArBbpKyYmWAuFy__gNv13NV6iZolJTAjhx8OiEbqxg6YnP_noRR0t50rEe2cEzsP6sRR1aI18m2hCaJbdoXZ9aav6IcHAKyslLXWFYbaUnb41kJC7AjTGEGuHUE-IKht709ZE1tqcGQTvfxexl4soStDb9siw5D88KLPC35QHC0ffAdwBsEA-1Bxr7ZK_gCjLvp-PklDviegg62KmE7xXLLPNZNs0V4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇦🇷
ترامپ درباره مسی:
مسی به خوبی تحت مراقبت بود، و ناگهان او در سمت راست ایستاده بود در حالی که بازیکن بزرگ که او را تحت مراقبت قرار داده بود فقط آنجا ایستاده بود. مسی شوت زد، و آن پایان بازی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100692" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100691">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f23fa81d.mp4?token=ivU445ErwZMTweQBZy2PPDpmzSxkOE9pPOjnXFYaf8WsXYsPLGdThV6IbviLfGfMGu_f10DBfDJeDUa0q1EA70Lh2MADDRi5x25ec4dSJbRAlylKppgFNJa6Xy2-Sa4Y99acA9iaUuPTUqaLRPinGaf0GA9ebe9t-h_ph-iI1kKDhV2Zrok5O2xOzSszsEc5dW5614vyj4vetQ8B4vgc1TFb1FaY3npFukfaTZU4-C8Fmw8q-rdGQTPNOy0MORCQxCneo3Lv1CkLA5yYnRgDuCbkJMh9Kw4SbVRFRvRe9EqxM0OSojuor1zzWxXp_86bc-YzokaR6jI1xfT-fm2gsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f23fa81d.mp4?token=ivU445ErwZMTweQBZy2PPDpmzSxkOE9pPOjnXFYaf8WsXYsPLGdThV6IbviLfGfMGu_f10DBfDJeDUa0q1EA70Lh2MADDRi5x25ec4dSJbRAlylKppgFNJa6Xy2-Sa4Y99acA9iaUuPTUqaLRPinGaf0GA9ebe9t-h_ph-iI1kKDhV2Zrok5O2xOzSszsEc5dW5614vyj4vetQ8B4vgc1TFb1FaY3npFukfaTZU4-C8Fmw8q-rdGQTPNOy0MORCQxCneo3Lv1CkLA5yYnRgDuCbkJMh9Kw4SbVRFRvRe9EqxM0OSojuor1zzWxXp_86bc-YzokaR6jI1xfT-fm2gsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇵🇹
ترامپ درباره رونالدو: من رونالدو را شناختم، و او مرد بزرگی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100691" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100690">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utFwSC8K9xAb2NP4_zLVyV95y9ABDm8tunozEbIeHGftMkBZQkoc1aPynKSb0MxozdU44bmIXi5g-Of5uoXBS0mbZCpWLUshnNXNxN670AX7L4RLjqfKrxWdQGTGoDT65yAd_EDyv4qBqddUXQUx7Pt1I2Snha949o8SCSmKEkJNGNYIsEPPv8aE0U5DXr4nyKx_azCaVFfDS4C1kQ_s3bTYbb7d4g9zZ6acxsKg856wFf1VNDSUFJ6sPET673jvrdRxXnVJbqBNTqjvJ4GbDWccUXY30zfhcq_K6OoeERUwbw9o22ZCWyUciy_2p5lfQYa0eDFIII_LGNgtPSn9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوه اوه ترامپ و اینفانتینو نشست خبری گذاشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100690" target="_blank">📅 01:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100689">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ks7Y2jGyJ6p8Fnf5spsVOS4N_AOUAzY3dq2zISlEV-DNKrX6HTTCugKUpWq44o6-i9fB_RhRICejI6ILHe3FzPiUIZy9u0BP7jQepNBJ1b4CKRPSavicCqRUjO1w6DTs-_mubu9WP7zZpaoajVcjKo8JspQCfahUyNbb1IrkUL0ni9VI_o_n8dtFZCKVRd2b_Ua6e9C9iL0aBhKmxHgPepsvhIYwPdlkM6TI5jyAU8nEMHodSsGWx8cOAlismZEn-Im_nd3vo3x0c4W_9ywWqu-iV8iwPaoNhFch1W5sfRERV5xrnena-aIRwJNx313XdRv8dtIdIbZmd-hhARXlnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🔥
رودری کاپیتان تیم‌ملی اسپانیا: لیونل‌مسی بهترین بازیکن تاریخ فوتبال است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100689" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100688">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آغاز کنفرانس مطبوعاتی اعضای تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100688" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100687">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1pakjsbYGwybLa7DKoMWXlzhrqT8GUMyGtP_CptmZ0sgv_Ega0uUjnomHIZag2l4-a9yyaa-x3ZbOeJDT8SdwwYiY2J_z4r31EUEH6GanPdBZgZDCWkNwlaTPZDy080XSed4QhxE9z-mlwYZMZpmDSaLIdTb3Y-WLDn-wTi3cKLRUyW2VOZkZ-sY8IiNG9C-4_JKcKWBPkwBscMPh8QKQEjZhbB2XfTU9Qv-2UYVUGIKb95lHsVIF8uosonPBafDITiw3dyLrBjV_O4pCQK4OruxyiBv177SfIAeloFKMFexO8qDetcLaLZnog_zB81XbA77KXUmCmc_Ofbjj9XBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز کنفرانس مطبوعاتی اعضای تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100687" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100686">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnYclqW040MEcm1Glur9_BYatO3_WUgJCredgsDdzlCLitqXI79IZFRzjusoEWeZ9VN86clDHrDWbH2TmTz3LzHPy1itdpYQG2xpgrgwsMuMBnLx6Nm8yTw5njisx-h4OaJHS4HkB97tvbxKaMv1qq_l4mo74cDzwtj0wb9Fua0TbIp0msc4IxAZMZ_Frt_0jdcX5iMlnPY0gPukNoQBcWMYgbmeGwLiYVPYGkmtKw4r5K-C4FfOvwndANmI5OcafMWNCvXlKan4irQDTl2fTuw4MtI0qLSrK0wJtAbBZwG_pTjCacAcWMsoAxV1X2e4cyFuGxSnNsXKNm0Xx5i5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب‌احتمالی فرانسه مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/100686" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100685">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=B7HposvsIzXSigoiBjbDbQrWnKD3nCUidyb_tkUSbrBbNravY0j0ZQsAJDuN6-JWMXDLpAIR-aBs37AquELEEs6g-Yg9t0rdnHNBy55XZiSo3sBIZCgm2DjBdH6_yQDkb0ohXgBL7ZMui40YLo8WvfwkjzsxOrqxm6Oy3rCW9LafMqzhsqKEwiz-nis6WTM3pJMHMSN0WSfcV3ZNLyPNI7KBJgkTE40nPfaYm8Nwxqt-q5vYrDkfvSywtTJGw1K0RFQbvhwY3h0fEZmKf5pW_e5x-xEMm7iGMIKIXY-HRgT0KKlzwRUghPruxR3VealPLqaxFzPcdqr3_n-KtcIdzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=B7HposvsIzXSigoiBjbDbQrWnKD3nCUidyb_tkUSbrBbNravY0j0ZQsAJDuN6-JWMXDLpAIR-aBs37AquELEEs6g-Yg9t0rdnHNBy55XZiSo3sBIZCgm2DjBdH6_yQDkb0ohXgBL7ZMui40YLo8WvfwkjzsxOrqxm6Oy3rCW9LafMqzhsqKEwiz-nis6WTM3pJMHMSN0WSfcV3ZNLyPNI7KBJgkTE40nPfaYm8Nwxqt-q5vYrDkfvSywtTJGw1K0RFQbvhwY3h0fEZmKf5pW_e5x-xEMm7iGMIKIXY-HRgT0KKlzwRUghPruxR3VealPLqaxFzPcdqr3_n-KtcIdzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حملات موشکی به اطراف شهر یزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100685" target="_blank">📅 00:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100684">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ10mQ9m-28d-DRnF39l3xCoNIRh8wkjBqxMd7--MJtB0_eq120q5MuNAFxU6oSvwsJ81biMGJWuLI4vsjanHcZBmsh_5XHL-rcNX1aNc4tWMXqOXKs-cCgiAeBoHjpCjhqvlSLureIqi3JQDmXDK7373RrNVH1tmp6AiU4Zb5T2TzdjJzAbwOx3Uu7F4ECqzEFyANgJN7OigHqtDmpwTR6JRU6Kg6LWq_ZTJzGG0davdVncKhd5cLaPo9ECbBiheSoh8JYy_OZQyKNdQX9iPAJQynNhn06J4a7aBlv1efKZw7rPcFUgiew7FKQOWKYkmHsHiSFQ8A8uq_3-2p71YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
آیمریک‌لاپورت مدافع تیم‌ملی اسپانیا
:
از رفتار فیفا با بازیکنان آرژانتین تعجب میکنم‌. چطور ممکنه یک تیمی اینقدر حاشیه داشته باشه و‌ مجازات نشه؟ امیدوارم در بازی فینال هیچ مماشاتی با این تیم صورت نگیره و در زمین فوتبال قهرمان جهان مشخص بشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100684" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100683">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/901c95f7ea.mp4?token=ngR15K9Ea0NqBklX1hZ6tHcoSYlNL7uzyiOeLLUiZtKbEUH_8GbjicXlBxu6Nszh7zMAop72oBf8IxkAxw7JyHA0nCuODApAsUe3uU2D0ZHFS45zdVE1GeKV1PoOfKB3akB2Irm-I5mX3s-9aV3fc3Q9ObYrEwA5OtRyxwfOtYyTGwNhiJGySgidGXV-vzsMRXmpwLdA4MzVkr1sd1u1SkP_I9IB5Us2OiCaqLuW56mDQy9iB8Ddm3zCgf6tCe8gf1JKruVJC3cDHbEKcHmZH31UGqTQFJez7cQZ6CJ6LWo2U08usFDV6cHPrOJjJgMML7XqW7bc-7t_cZJ1R6IWng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/901c95f7ea.mp4?token=ngR15K9Ea0NqBklX1hZ6tHcoSYlNL7uzyiOeLLUiZtKbEUH_8GbjicXlBxu6Nszh7zMAop72oBf8IxkAxw7JyHA0nCuODApAsUe3uU2D0ZHFS45zdVE1GeKV1PoOfKB3akB2Irm-I5mX3s-9aV3fc3Q9ObYrEwA5OtRyxwfOtYyTGwNhiJGySgidGXV-vzsMRXmpwLdA4MzVkr1sd1u1SkP_I9IB5Us2OiCaqLuW56mDQy9iB8Ddm3zCgf6tCe8gf1JKruVJC3cDHbEKcHmZH31UGqTQFJez7cQZ6CJ6LWo2U08usFDV6cHPrOJjJgMML7XqW7bc-7t_cZJ1R6IWng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدئویی منتسب به حملات دقایقی‌پیش به شهر موشکی لارستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100683" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100682">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100682" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100681">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enWND0hB3LaH6OBP0lO7f1yIZpO1ooTXANViCOWO-karR-0lB2UsABtNjkO0VEKuxZAjKZUTXLwKkfg7WYrmaqU9iehHNintGUBoe079wTXjJxgnhne6qhrj2tCzts5I9BAQi135LpfbOUzFvZrWb2CqEn0K4iehqHkgmDN6HvG2HavevduhSSA2ta8zrtLCH50jPyX3t6A2G08iU_hiSq-f4GhteD55m16qczLM6qYF6zezTuLUVScXgUlgpglwZ0wgGwNab-1LQWXiXElBzWtx1t04_4SH-4_LOj4Ph5HZvQUHRXr6gm_IlZrHM3gq1_jwsnVows3V4wKyS5Y3iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/100681" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100680">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGzgnZRqvejsSBWbvd83GDxMXyPhkSXRDOUv1vAK1hpKBu8uK4gFBZHhL2ECwUC8FVVyHCug72s_Ul80jDFZ2MijX6AopENnp1Ubz7_qtENMo803mNCqDxUfya9gH4ZhuVDOatknnISxzYm9wg7fNCrXRVjdW-q_HMfK2Sm7OJufZtNR9gmpXrJ-64kOtqWd3sIa0g4k7UQ0OcxbmYJai3nwFg3-6Qaw0D2z05M-Bi-ZgyHLPl_dQpH9sjfC5cT7iAd5LGhyPk0mXZoPbpQoQUpKSrcQ7oYO7Nq4EsoVwikOUjqFMj5Sf0LEJHBNZLIkL9C-cM-jGDWL25gpwWHliw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚬
🙂
شرکت تروث سوشال متعلق به ترامپ به مشتریان خود اعلام کرده که میتونن با پرداخت ۱۰۰ هزار دلار ماهیانه،توئیت ها و حرف های مهم ترامپ رو قبل از انتشار چند دقیقه زودتر دریافت کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/100680" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100679">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a84e45b5.mp4?token=khcprRsIwahqRqJso84ylZH9qEBzcVOhxgqZI4WyHBjvI9lHIwsXkAOgpmvioSgfovL6O6_y4UAYEpWCpVxN2o7PlNIvQC29WJKJY4sVHJJurD1p_Vht8zTA1YSZsHiSkZfsPvtx5Sjboip4HtI8QpKD_hCDxeWHbOmQWWkEyDN5jrmZJDBg1FUwLCkVOcFS_tS2NjOBdNdNzpWX5frk3vyLpWXS_BG33zoVkdFBTZ7lPbl70pSunHUSq5d-VGxcdClT6SHjn9a0jtsKYk_82pXP3M2oyCOSgqC6I-lGuQAwLMy0LOlwRRlYdAj7NQ6ALnPfQQ22ricohULxflP2Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a84e45b5.mp4?token=khcprRsIwahqRqJso84ylZH9qEBzcVOhxgqZI4WyHBjvI9lHIwsXkAOgpmvioSgfovL6O6_y4UAYEpWCpVxN2o7PlNIvQC29WJKJY4sVHJJurD1p_Vht8zTA1YSZsHiSkZfsPvtx5Sjboip4HtI8QpKD_hCDxeWHbOmQWWkEyDN5jrmZJDBg1FUwLCkVOcFS_tS2NjOBdNdNzpWX5frk3vyLpWXS_BG33zoVkdFBTZ7lPbl70pSunHUSq5d-VGxcdClT6SHjn9a0jtsKYk_82pXP3M2oyCOSgqC6I-lGuQAwLMy0LOlwRRlYdAj7NQ6ALnPfQQ22ricohULxflP2Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلد مارشال رضایی
با نظریه جدیدش دنیا رو شوکه کرد :
اگر فرضاً دشمن توانست در جایی پیاده شود، چطور می‌خواهد فرار کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100679" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100678">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gURpJWef6460bSOu8AZMTfvF1tEoqv7II-5vg5De_H5aoHPzyK8ANTsbJOHj_x7rGvolmpzUh36rbIUBUYFyAtFfyKPG4t8KUaG7ENtkCSGKPAtcuTNY53-etMw7VVRPm-TeHxaA5ufj6b2vfVUWaDb0dS9mRDe2yULhq09EXitbSAXDAKZrtd7oaq2DRC-0Y3jJd6u4eTgYSax7oCfwtCrRfCWDPZsUDNwrYZy2HVed3x_K3bft59QjzGjjfMmqLyiwajB_tq2sihs8EZeur0mqAXfGO8G81BnrmO1YL-dif8g3qwum0PQEIDJdM0BX_fMOot1dq2aUMDUMYGXdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
✅
😍
یادی کنیم از استوری رونالدو سال 2021 برای علی دایی: یک قهرمان واقعی همیشه قهرمان می‌ماند. افتخار می‌کنم که این جملات مهرآمیز را از الگوی بزرگی چون تو می‌خوانم. ممنون علی دایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/100678" target="_blank">📅 00:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100677">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnGGcdlp7yiB70EborBVjswLAqzNKAaud4SfPQG8faVuWBjZNBO4pFlpRUIZ1Pl_0W3WcHc1zQ2hd8TjyzYDXJKa5LMiyi1o4jQ2Fs-euE3_JQXSnXjKkMY9539NTnwtko6qR1DX_QBbJVl4X_SGNH3csN6o7UmJxl0gD7-LIAyfqQdPsJWNSD82f-fJ-pk1sy-GKTajzsPKjuybVrpi-D9uOM8q9JYqGO7Tx_l0s11eyPyXnPSc6NZpnlnmjeVCe6xJA0Yh-I3jk-IEYwstlugy2St2z5k0yHzJgwrpHhUdvxtZEkzPCzNTjbzAsZK13DBBt8Gfi_zaNQs2US5hIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
🔴
اعضای هیئت‌رئیسه فدراسیون فوتبال در جلسه خصوصی روز‌ گذشته درباره اخراج امیر قلعه‌نویی صحبت‌های مفصلی کرده و خواستار رایزنی با نهادهای امنیتی برای برکناری این سرمربی پیش از جام ملت‌های آسیا شده‌اند! چند تن از اعضای هیئت‌رئیسه…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100677" target="_blank">📅 23:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100676">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFNPCITLB1pe9oL8vtw5-m-dVoMuOlj_vCv05CY4IlfyTPDpT_1r1LfHqoCk_dGoGaO82KcMY0htGPqwQoLDr6qN_2_0nMQO9cTT_RzhWTl1l7XD2MHUIp2yytASwZ2xB-jReVJnWPAruQa_-MKOPPY2L4rQrFd93nnOzLwtLEwoMKHf0KuWr-_u3ABO9qq6ZE95UTgUeNjdoXFNSy_bJE8ADAxhi9nJ2TFTaofcSZEwoggJi8R25AwdvMysymUXh3BpjsJijMGdpEGKuNeQPN34EoALD-VWsJsn9EbFhDmi4vVFTYmvlRYknyS202buuSByBEPaFUaFCQidbohxdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
رونمایی رسمی لاکرونیا از اوبامیانگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/100676" target="_blank">📅 23:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100675">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
سنتکام: دور جدید حملات ما از الان شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/100675" target="_blank">📅 23:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100674">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdO6pfy7H4Fmsq3hgbRr_hKm-YRpqaqRM3PlsseQg1FhX2cNTHIf50Xm74p2-6EYl1I8ziNpIa9v5vYPbbEpBxZG9hmUn4fmx1_BClGZN4Y-gk1UCGRcDgp4MCNCBQ79rfW-irzM6M1Vhm44RDlPK3Ul6bfy1mz1d8ydDPVz7EUiBmmYoypJyOJO24HGW-d3-9ZSjD6j8FzjbPaz_4hb0N1Hb_4kTq0U3rNXrV01HmsmPfwbZfBP5kTC0WpifFok-8O7BzXOEAMWRp6qHjTXycAGPaYkiMRWxCh1xsCqK9VsS-VCeiD7GZU3N2MmCTHj-7XlALWdmiImM20pFrVuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام: دور جدید حملات ما از الان شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/100674" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100673">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA4T8-3cX4LoT5x3b3zLxbaNf61WDTa1iKrVe3rC9UnKWn7tXk6jkBE56ny07yG_VZ90fPkfCYd_wfmSY2UbI4UxB3DKqitOhzD4DkDey5u_dDuVr7BAMK8_nQuDjbCxk1AW10SEC7UhpTgw83EYSUXmloIGJ4UzJH4uIFAFPqp274RykigM6nObhJoZpxsqD4itvzJQyVQLwMO4DV7itnPDFTTUH8AA6cDHOKOETciF4mDJRoviuPw6EWDwTOrFnf3nDp2qyN2YiGULkKqKvEf42eoVU47_-CMi-IRLOrX-tdaIe2bqXqQ0GD-KEavB10iKUuIgzrOADzq9xIsW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🔥
لیونل‌مسی: اگر حضور من در جام‌جهانی را به یک بازی رایانه‌ای تشبیه کنیم، من تمام مراحل آن را در سال ۲۰۲۲ تکمیل کردم و اگر الان هم شکست بخورم برایم بازی در‌همان دوره قبلی تمام شده و تفاوتی ایجاد نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/100673" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100672">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEDqNvYLYKd-M868xN6ro9g3rHcMMBwO9_6oxHcJP3D77O6cNmqd2hhDDLFl6_JYdbX5IT5powCokoJON-Kb_NHLlE3C2GbrFFaI-P1oBzJm5X_Aaqy8rfMb5fhXepK5WZYBR48EQdjUL2jCQp4ywklPz8Ju5L4Cr39-Wq1DjsBvORDOO8l7kFMdDc2JCzbzHiOYyyneYZdowqNRndI4Ry47ZSWGgQEj049W_7kzLcO6Ef4RXo0IRKYZTaQW2zPxTU3TYgQVjOnyMD2zBAeBP2nrWT97q1C9-QBsZU6NatB59-DB738gB1avKAzKDr1lKKboN-jI6StAFEH09OyQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🔥
لیونل‌مسی: اگر حضور من در جام‌جهانی را به یک بازی رایانه‌ای تشبیه کنیم، من تمام مراحل آن را در سال ۲۰۲۲ تکمیل کردم و اگر الان هم شکست بخورم برایم بازی در‌همان دوره قبلی تمام شده و تفاوتی ایجاد نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100672" target="_blank">📅 23:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100671">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe058d325f.mp4?token=HYSrxt6k2J8i3H3QuB_iN0Jcs7LheL8L01SUCQSnsGZIj4963Q00QyYCLMBWv06g1AxBXSCSvTJ-o5peKCkNSvH43j4TJ_e1sCvym668InODxEk2m8ukmR4-gsNIqBm_imLLWEgz56KxyJ9Ovmm4kFmzMXIlz-CeivWVD2D16K5O-wmCkHzpWXbBNioXS6CrjjeNYBzKPS78QQ5GMerttlPOLq6r1XaRIWkzxLXG3rNHiOf0uWz8LZHDTy2pd6fjGwHurF0LRQFOzXp7C-Tssdv0bkt-77RLJnby4CF8rPmnYQMVMNWMnr1BYJHEVWszwHIiWCO1ks8_VoRAgBGKfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe058d325f.mp4?token=HYSrxt6k2J8i3H3QuB_iN0Jcs7LheL8L01SUCQSnsGZIj4963Q00QyYCLMBWv06g1AxBXSCSvTJ-o5peKCkNSvH43j4TJ_e1sCvym668InODxEk2m8ukmR4-gsNIqBm_imLLWEgz56KxyJ9Ovmm4kFmzMXIlz-CeivWVD2D16K5O-wmCkHzpWXbBNioXS6CrjjeNYBzKPS78QQ5GMerttlPOLq6r1XaRIWkzxLXG3rNHiOf0uWz8LZHDTy2pd6fjGwHurF0LRQFOzXp7C-Tssdv0bkt-77RLJnby4CF8rPmnYQMVMNWMnr1BYJHEVWszwHIiWCO1ks8_VoRAgBGKfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
علیرضا فغانی: بعید نیست در سن ۵۲ سالگی در جام جهانی باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/100671" target="_blank">📅 23:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100670">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b30c0069.mp4?token=u9n_vGkXRKnuxoPUQ1qQ3jMJnESFxv-30Cu2oJnjPhkQ4U8pPO4I9GcJYj5Yp3-QWTs0R-9q8lH-fJ9UI-T8pjCYd9OjJWetfr8nIuSFHXVdW6OxVaPAVYbOy-ADPEJK0UiMLcJfmm7IV5jMEDuFGAPbEUalIUIe8ziuoYgp2ncw7MpTY7b0GO9nxQAf15YW3BVMb4YrM_-oo1llgnYuX6bbDtq-oHVonMtdIdDG9Xw0lIlfDgNvGY9sGSqbtKjT-0QEYVaAdz-vd8FCO949LH2pVAoU_21VKKg41kiHMXirMluXwqdQodQ9EXrWRYtihoigZLTeq1fnmDPXKcG_WIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b30c0069.mp4?token=u9n_vGkXRKnuxoPUQ1qQ3jMJnESFxv-30Cu2oJnjPhkQ4U8pPO4I9GcJYj5Yp3-QWTs0R-9q8lH-fJ9UI-T8pjCYd9OjJWetfr8nIuSFHXVdW6OxVaPAVYbOy-ADPEJK0UiMLcJfmm7IV5jMEDuFGAPbEUalIUIe8ziuoYgp2ncw7MpTY7b0GO9nxQAf15YW3BVMb4YrM_-oo1llgnYuX6bbDtq-oHVonMtdIdDG9Xw0lIlfDgNvGY9sGSqbtKjT-0QEYVaAdz-vd8FCO949LH2pVAoU_21VKKg41kiHMXirMluXwqdQodQ9EXrWRYtihoigZLTeq1fnmDPXKcG_WIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🏆
علیرضا فغانی: برای اسلاوکو‌ وینچیچ هم خوشحالم، انگار خودم داور فینالم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100670" target="_blank">📅 23:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100669">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4P3pkge5k0dKAy2LpmiG3mq5gNzNZ-rqAAdU6Q3vkTL7ZzwlDrdJ4yXclfizx0S10Op4U55jIR_dbT9NnBQvFZo06bqZME5UdU-1H5T2uOYwJgD5mHd8ljtCKne5khhji0UInGTI8mRzF0JX7f85Q5Nyu5XiVyWaFDb3crMSJj7FgnYbImO8BL3tteLiXgcMKs6dIa13IE5BCkWZNG9UndObiQh-l54kBuhEq1P4-i7Xk-T53nI3H45KIeHPKn9KNtkj-c0xZNO0psMUB0c0VYUW5R7lu4HuGHKi40By15Ak9SztOCWrGnw9E8FVgVGaIp7Ad3qJWYO4YrUOpx-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✔️
رودریگو ستاره برزیلی رئال‌مادرید پس از گذراندن دوران مصدومیت رباط‌صلیبی خود در اواخر ماه دسامبر به میادین بازخواهد گشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100669" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100668">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3Q0YK-6mLglyAbuCsfZf6l64c5t3gu9t01HKueuLvo75KYhvxPRM87Ekz3eu3ibjHxOKRNbpJDNcGHcPnnuoXe_zxqCa0ZUBrHt0p7rpfWtJMXvOTx_XiaBDybijTn9iBOybLqEWmbLJRn_1ql0sAo9G7NKZW1Ww2eGZDjiABo4544g4FOlRNm5Fsd6RkTFAcrwujQPRA7EP7vLln8aD-tHtFtAW9baqthSg3CrrxXZ78ANS1JXtDFxAgNa4ALkrgKC19ufzWhSzxWNEjEajL9Van11VWzmwg9f80PmVgRsqx9ZfG7RMp2pZb-D4VsYb3dNI0HW9e__AF4lgsFvCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مکسنس‌لاکروا مدافع کریستال‌پالاس مورد توجه آرسنال قرار گرفته و مذاکرات ابتدایی میان دو باشگاه نیز آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100668" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100667">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">لطفاااا فیک نیوز پخش نکنیدددددددد
خبرای دقیق رو اینجا پوشش میده براتون :
👉
@khabar
👉
@khabar
تهدید سنگین آمریکا برای حمله شدید به تهران!!!! نمیخوام بهتون استرس بدم ولی این کانال رو دا‌شته باشید
👇
Khabar
Khabar
اینجا موثقه
🖐️
🖐️</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100667" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100666">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6sZj-ywQ9RQsXm5bNuIB2J3n6dXBydDoGD55IgGZKEB049irQ2WWGDVJErh0orhR5hHvSFr-yIYBe_sO675770PNmVp6BN-AinfSakplN28tZKpxecFBlo2eBFIdWwaN5i27FP-EG5dJgd9m5QWp1fuG5SCCvNDRLUQ6iukP2xyWQW-l4EIbtxAo2CGDlns4bAmb7ok_hQ1NkXDWgtuqsDfTsPcuOImX3EOdPI2vB0KedNV1XYeQQ8lqaP3ZFjUBcxXvRGnjWwyDeZgDJ6Ag8uXFtjFhZVcQVHzUEpEgeL6sO8KTW8Pi06XDnlH1uQIYOp3CLc69Z7PwfY0J_U__A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
والیبال ایران مقابل اسلوونی هم لنگارو هوا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100666" target="_blank">📅 23:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100664">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LlP8MFoSc4EjQR5x9PfMxR57tjjyz78Dm2P92atpYLcDwU2bF6RXUEdz7EEkx14un7H6_CMptxhtiTg1NBHegqhskV2_f7lyzzge2Jo22dpJqGXzLI6jqhtiHS1EJxMYjRUFm1rMB_x5n6KipPLweIBq0Bcqo5ZZCX6O1nddX6uXutcJ7H0nxF6ngglq2hNjs8pAz5LQl6agHlONtII9B6U2WfzbL1k23lPp5I2eLnFtbngL-IoZYZA6HiA2Ie84Qa4trtqwLmVZrwR8aab1mZg2403S0Fx9XvMbpl4KpZrvBI69ARg4HUE4rAMrHziOjOyzHSh3QsouNvb8J8Md-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3amPsUoesKnW8hc4It7KsfoNTCzM80RL5qCkVlKJq5NQyrFU8VGCwgW3t5Js7cMRrcJCnSEBIMDtu-KbM-oa70YxK0Mif4GlZsGWomplsEWlOc0WEd_8U0i_l5ySZR-xFoTJl2Lo_N42r5VzX6mBZNZIpPfoLcTb_q1pqdkNJpgUyQw5HqX27a6UiGjWVlUW04KlReNtFHIX07IM1rZgttMVClbqJSs7QTRWBYdmsNvPXTcrteqe1aaKMkZj7eyAxu-1cGAkCvenEOJTT7qrjNq-z8w9GPoTJLFze8FAKYdjN86K7H5PGA56fvLxdA4TYUheeY1ivPZh2BzWm9jMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زیبایی کاپ‌قهرمانی جام‌جهانی فوتبال
🏆
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100664" target="_blank">📅 23:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100663">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b11i3usqkMloMgMxsZh6jKnWBvy1kQsamz6-2zEGN8SLCHXqIwfozP4X-1udG_sRXlzWvQMspCizdv6zZ_uySKbDyhSstotjYO5tcnlMok4pA_gVu-1RBlRbyZJwu499NPdZQQfz3MrAugmXKHez8f7-Q_z2HS8Tr3gXql9iW2B9ihDyCarEAnUhu_uYH1_vP-zVj4cCm75nEM6CRyDUdslMT1jOuyFujoI__7kLb7w4mF4_7snC1C-pgOooOsKg7qWw907h11IhYbELGz-or9BEoK1xMDAi2UoTxAu-W6J_Gpect0p6z9X5nETwV-HpFGoLqpZEsKUVUEDDdJ0FVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
حمله تند و بیشرمانه بیرانوند به صحبت‌های علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/100663" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100662">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqrrQbNlNhFF0k3bQqs9gA6uulK7Tu-HJCBi_CjDImBC3dtTUMlhqrukxnQGHUFS4N0sE4NImBmr10CvsW8Xea1Y5Yb8fI91KwybJLNcukPOGizps0aivbsMS4CEQaj88j-V9zaRihQqw5NgE0EzE1_5cbViTEDYPhsyATvhnB82pBt4UyI9rIRXFr5ZRe_n8biEvUfw4m88yviYZpSbDXUCwRP71otwsdbWXPY005jieEXDbDmNulfBiY1CeuoRnWATxv17morb088sx31yvq8-5gS9yh0UpxHX_iftxEpxYToKJWT5BXgr_3gaLraBreiYGKthukCsIuWMLp8V4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
بازیکنان انگلیس هم قبل بازی فرداشب رده بندی تمرین رو دایورت کردن و به خوردن فست‌فود سپری کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100662" target="_blank">📅 22:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100661">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCJ4-ohGz7nAfFduYdE0En511t-8PdvdmZhY68cqBhnmdYwE1kqPlrT0RAMsxxkjKPIcNm891qrkld4fd825PkP19vBA6-XwtOKQpUCuD4Zjm6Mx6jn8AIO34-CF1iElj5TyprSb-M_mlv1IadDVKlYV2DN1fORXt1VSyrX68Q9HVrqO3U9qudLvVp4N0SG9O4w2GTGMHPuV0sonJEfP61ZVc7rWnf9sMcBlZiHDAjfyqFZLuTsEN6-8jfBRQ9JM0LlqYOSghyYPtZncngzmSa7B31DebX0kJffSUDDvFRUt54Bxky9oysRK92RsCIW0zas9TzqE8LFGHFnPJqK8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلور ناواس:
من فکر میکنم آرژانتین فینال رو میبره چون واقعا داشتنِ مسی یه برگ برندست و همین تفاوت مهمی رو در یه همچین بازی مهمی ایجاد میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/100661" target="_blank">📅 22:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100660">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCB7luk_VK5KLkr-ERm57b1VXcFryNYNnbp1Ver1cMS3JCgPxXL7qjHW8DowO6EE9NCW3umnHySjk00Vo5Mn1ZvvxI__1w6NR-2jJkfOdL5gK8XI3-ibSkRaWuvcVF2ZFtCMVJf1gacwzBkdFiUgMRMby60LbwxDMC7razHmeqQChLvd_G63RC7IBHe9bevWQlurXNIvHwjbfYLluHtRDYkCa1PAxF7jFSYf-PdecGVnX1ViHWIbEqfhi0bW4vySlQBhHA_zpQUTi9hzFrmcVWkz3FfiNe0bWRrXopWCX58LUgriM4A1RUyTQSmliT10I1PYhcRJOIBoUxJ01oS_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
دلافوئنته:
مسی و یامال
هر دو بازیکنان فوق‌العاده‌ای هستند، اما در حال حاضر هیچ مقایسه‌ای بین آن‌ها وجود ندارد. چون مسی سابقه بی‌نظیری دارد که هیچ بازیکنی در تاریخ فوتبال تا به حال به آن دست نیافته است، در حالی که لامین هنوز در ابتدای مسیر خود قرار دارد. امیدوارم مسی یکی از بازی‌های درخشان همیشگی خود را ارائه دهد. اما لامین هم می‌تواند یک بازی فوق‌العاده داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100660" target="_blank">📅 21:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100659">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1spCQ1gZufR6P3eucpberbdB15h_URiFAUS8082Os1nejTFpoovqjPTUbkvt70zJ07xJBjdMqo4eirtpPEt_soGqZpjR4Zng9d3HKE8p6oqmrhm_WVsKXF2p1uh8wkssWZ-efEeWFQEmBXTXV-QB2r0Oo60glqRqgZ_Ud8okt1-9VB9vPmELle2rd7e9QG8ty77d-AScho7u-KV6ZghGjCZ3TrGrHcR0oSJ6fMo5m9lX9SDvoHoKjfplDYOW1XyuzQlgQH4njnWLlDlkr9OEY6oPzwboUtUcq059wMcy5DP1J0nQne-H2r2-xfj_ms-y8sN0ilVnBhs2nnCpsf-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
بارسلونا در یک تورنمنت دوستانه سه جانبه با تیم‌های ناتینگهام فارست و اودینزه به میدان خواهد رفت. این تورنمنت در تاریخ 8 آگوست در ایتالیا برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100659" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100658">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seIsDuf-IgrIZIaAXtA9s4-ENrxUmPAD-7OlMIKn_oMiNOmxbo7_IJMV8B8GH8btS5-RXGhnuuYucfyJjyOvEt7UQM135uLRsrwTEq5Zl1FLaitqDVb1orFSHt5hJAkDoBcnN85hUFmPQ60NdAcC0JPyHKrqSmtdh18KOzqCD8viMdbLoAPI3KV0fvQ-uc7GrnqQimfUdNBllDK6bRHPXVF6-_pkdM_8Ur-TqB5amdpjM8giqQRRt1KDpYu-hfrliqq0nv9A1hq1gpLXsFvwNqTUQltl7v8xe8AraJB-0z3AUVG5dCMP51sXyzgYSOgkryGD4IAD_l170nfNnNIZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
؛ لکیپ: اولین پیشنهاد رئال‌مادرید برای جذب اولیسه رقم ۲۰۰ میلیون است که تا ۲۵۰ میلیون یورو نیز قابل افزایش خواهد بود و هفته‌آینده تقدیم باواریایی‌ها می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100658" target="_blank">📅 21:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100657">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0_7zEHKKU9CK4sGS7wi8YAHy2nxwu8mOrDXfAHpRwBoLJQMf1sa55p7i2mDjkmicpuHBe_zVH6gPhZZ47bEecxTdzVe4oekGg9X2y3p-rLZGi-XqXqDaUg7kfJlJ1_gqMv2_eisPxa1STOddx4dd-__89oQeLmeZEp-duWT4yVRcENqx3A1QflZ67KhOcJiR0YgC0DNN0HnHM3E4WyFAznIX8bS_YsULraE9a65w3BoTPfin4PYPfkMQdYHFPec9ftioAzmNSFAaVkBphkwKD4g1OF9zdIDGrI15nzKA_gk394dF2Qf4eqdlmN3NozSTukAayBPb8hLoTysFqUlXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
محمد صلاح برای عقد قرارداد با بشیکتاش ترکیه به توافق اولیه رسید. دستمزد ستاره مصری حدود ۱۰ میلیون دلار خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100657" target="_blank">📅 20:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100656">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhfnize8kLcUnB9hbr9G14x3bC4oqVTb-BhUDT-xSVLnOOTkH2K-MhCXo_7nYD8eAleieaC6vyNhNnwSjpT5_DyCrXB_hdwuOr8Zpw-zkQss5SQ_mEm4NY8_r7DY8feug4b7h_tNrK9IpV_xID71KxnDTcVJqfymH91LZmXiihOGrte-wsLnVp0CHMRc7u_Ez5GyJ9739IY436s50eDeQQjH0yT6n88O3uTJdZNdBTq7EOtqIuP3GBGWmqly_TtC0n3gyjM6xcONx7d3J_1IXFZVjMtiuNjEZu90FGoHyPS8y_rdJl6REJLDOjabaUhx_D7QLV4DGYB5OxnKrS1v2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
قرارداد ادرسون برزیلی با آتالانتا پس از عدم انتقالش به شياطين‌سرخ، تا سال ۲۰۳۱ تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100656" target="_blank">📅 20:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100655">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVEedLFpMCPD5Wjzo2nnY8FxjEQUdI4DXNL7iNoKzAHOwhSxmPDergUOTy5t_lTelbbcb_vaXrDx1nKAznvKI8PToZ_vJbV_HDbXPvusNsopnwYSNg2EUifZKEL0ebPKBq-djYjhV8oFgLkxXyWJkapgR7EgGTvOQmqAC0Sp5HZzpKoIvFg3Ac29qClI3V4pnNTXDO7WZdzC57ZwJo_jTBVRgSvrXK3RNZ4le9zdlI0T55NU7Yaqh0UfBGdI56KQvWMIBqYKJFPS1LRCofH-zLa48phdf2iadBEGTnTxKG0azQd7YAg5l5_iW3CYS_QfP1HAqU05qTHOF5orW6zc_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
طبق قرارداد زین‌الدین زیدان با فرانسه، این سرمربی در یورو ۲۰۲۸ و جام‌جهانی ۲۰۳۰ روی نیمکت خروس‌ها خواهد نشست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100655" target="_blank">📅 20:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100654">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tySlnMG-Rfffq4MBp6ybelxFFFUZnNMbJ0rbrUDkA7qh19xLbbfzR-4zh9HpRnLvPY-klj0iPdLWuO6nzbxU-wI_64zRVui4VjVWED9R_ojAaQq1tjb1WKEdrTVjm9LLxQVvaBaW42uHQSEVXVdlxsL6Y9jJ_7aruXLgJGYnnZRGMScPgMfJ4q96OfR1lpiXabdMLt5lA65wV-ion5kQFhGumUwyS-x5FsscqWJFS6b6XjvewgqYvrnrMkB154hcbFm24_BLisip9_nHSLjRU9nx5grmK1VY4Q-S_OzhPbKjQA40SyZGAVv9cF7Yt10ZZEgjO_Fo01QjGGNRqKnaiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت برای هر برنده!
🎁
🇫🇷
فرانسه
🆚
🇬🇧
انگلیس
🔥
دیدار رده‌بندی جام جهانی ۲۰۲۶
🏆
نتیجه را درست پیش‌بینی کن؛
۵۰۰ دلار جایزه
بین تمام برندگان تقسیم می‌شود و
هر برنده ۱ گیگ اینترنت یک‌ماهه
نیز دریافت می‌کند.
⏳
فقط تا قبل از شروع مسابقه فرصت ثبت پیش‌بینی داری!
👇
همین حالا وارد بات شو و پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p9_r4EF37DCE
جایزه نقدی مطابق قوانین سایت به‌صورت
FreeBet
پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100654" target="_blank">📅 20:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100653">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrJieeyYWGuNeFAoADgt7OHL8X9CtuMTS4hAVfk5l39aV11ix9ns8jJ7VDeVjgsTElSxMnq0VIMNoZa3xhKUX4wZMdNa0wnV5N3C2qfpJKEw1QbUK3DV3e10r6avkCkADelqqIKc_X9BR2jjKLikKx9LsWneqMp9QS_zBOga_Wh_Y5OgZM98ZJBVipKGQrgPpslvsnJhZklCffKforYj7PTo6kU0_wjFdSanev4TbvPXfO5VSclLY7R03r5L4xkRD1ulB45JrPzyRL5sS3idJNvQwXF7Nv5c4FsHETqZxGGVJ0RkmKKur3gR2_IVrYcEocvpAKQ6dkmDNOermZAVpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامبک‌خوردن انگلیس فقط به این جام‌جهانی خلاصه نمیشه؛ تو چند سال اخیر انگلیسیای لوزر تا میتونستن کامبک خوردن
😐
🔺
2018: 1-0 مقابل کرواسی
🔺
2020: 1-0 مقابل ایتالیا
🔺
2024: 1-1 مقابل اسپانیا
🔺
2026: 1-0 مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100653" target="_blank">📅 20:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100652">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsxAik2rwDlFDIma6b9WlsoaIrpPsfk4gz9daHnW1pHRUHB6pOpXAIEs5651ACuiE2heRU7xX0NHfpdOa87o6SiDRcuugjAsWmDNzh2Eqr2bl5VG_htHrAaaGp-npN7Tp5TtaJ4AxMJpURbVyM8nh2eBlk_ex9QDvUBFC9d1Azva-rTWYkhhwOHnXCncs2Itofhwy1sZco8RJ-r6vvgzPEh17joweoahRP8EBiHmtF0MGMe52FgrwNUVVDehXh2e7lP15YQOr796Bxx34nyboO9KQT25Lwd1SRcEH0i0yALtcniGZXIBi9rG8x8OIeOhXZhwWxRkTzFsq2A8okyG8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
‼️
جیانی اینفانتینو در انتخابات سال ۲۰۲۷ فیفا آرا قاطعی داشته و به احتمال بسیار زیاد در سمت ریاست فیفا ابقا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100652" target="_blank">📅 20:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100650">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLJtNZy52MqAvTDiAWV9I1FwDgg_bs1YeGDyFJWUOHsIerxMdYUHImcaC0BBEyEekB2vg3lTukMAFwo7AL4saImn9aABX05AAVAOVRF6ErNvF9b15OTLpzeNVxdR51VraA1MUi98obSGCLavISn_IstSD-UtM5su_G_0T6X6kl81TK6j6LrCtbwG4jvTS7DnwepZboNdj1yDqt-oe7nFDfaGax6LRWOR6_yDoiYZ3xNBdNtkzVOjFvoWjUNRWa--zT7Z0XRE4TNlgvE2-BesRmkyF4M90NmoKx7yGVqM0bhEXL82skkLvHHFBYXw7cn1-EaFia9mMuyx5Z7ADC_o4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJfrHS7lP5KAj04RUme0wwAHnmcZxe5ceGFjkXSqEVUm_jOwXK2dseVEWV4sAryVi_g5gtJrniwMvPMzUKfRDPgyolHobM9sEruVAWtMc4gZbezz3NufX2Yi_-Z5MPNg3uEV4YHK3WoAXqe6vDx_tFLyACknNXOjBzUsxXAqwu8-kcOzvwNqNKghYScUX1Geon6vYVWOvQdR70dWmU9rXUtcXdiUAMOVS2M06i0WIlwP84pHrPafpXkCroOjC3YRh5Wc2dYbicCvrV2xIJ939QdXQ8iq8HMIn-sV5pFWpjb1cp_e_ExBvMGEbiiGbf5Kp4mux8dNxCaw2YcHlMVVRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
🏟
جام‌قهرمانی جهان در استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100650" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100649">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-1z0tK8Y2qthE-NEwoXF431Z3Lu7C6GT-0ku1aeeN5B4DMMkLtzFlEiTM6yqsmTfxSgmLPt7wTUg39EYYP2_lEINwl41p5QARStI96nbunIrDYwLRG_u8BowdmF2rY8uAR9WaQLdMJE0-zPqkCPBvPMAELDZGdjBgCUaIbNcwwtMDkHgoIM7V0HkQCnrQ37VKJlrGavPeZVX1cuO88jOAGwSbzVlJPvCXtJ3TSPgQ0gKG0owvB6ahm4_F9-jS19SGlSCT-n34b8GA3oe0-G2vE6kOp13c2Oa7KO8kwN7Ta6Wzspm4J36W1vYRV39Uz-khJVBoAV0Cl0FYnD9eZ7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یکی از جالب‌ترین اتفاقات در فوتبال:
- آخرین بازی که دیدیه دشان به عنوان بازیکن برای تیم ملی فرانسه انجام داد، مقابل تیم ملی انگلیس در ۲ سپتامبر ۲۰۰۰ بود، و آخرین بازی او به عنوان مربی نیز مقابل تیم ملی انگلیس خواهد بود، در ۱۸ جولای ۲۰۲۶. بعد از ۲۶ سال، این چرخه کامل می‌شود.
✅
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100649" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100648">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100648" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100647">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSjKAC5aaKxcyEd6ETJC5ybCJLY7hPMaP8ZqXKcTU0354q3Gea5GTLDDGEtYOT6vTxTyncepR_5909yQOQ_5yL13IDXZ4cNqIxXDEjnlDxcdW5JOuSTDnSAa9tHPab_HCJiKBUAz5mdEVpmwTycgOVa-s76a0e_SBOwhA77OG-HbG8JqMjMlg8zTgvgnMq4GmWUL-a3JhLO-pqyOQIXlMKpoP8rfWUtFrU5cwPqUHaz2dZdLfhpb3O22XJqcQtJJuTOXxOer3nCZnnH-cvSMptVDtP0m2nvNlKmr4KHG46mp1YiVLbFKwDAnz15-nkCbc5IOwZQ5QW15UKWYHqEUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100647" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100646">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEjpO8CvXwu2fBo7qREj-p4Kp4T8rOg5WyWA22HQcV8HmmcO9EzTb8BDMDRjkcDWyWfamDTpYzA_BdELKexyQannOduz7CqhWK9S0nd9xJH10opdI1Zlg7yU_uPYmkKhrB0zQJ51qXBk_Ff2dAbEVbA2c91tm-3LgCNufIxkLF-_qpAdty_7kq3jgr8_qAfMCshZxiBRZxzweQ0GQ9A7ePUHpZpOwoUJXt0ok7K4ouwzond-j5f8jK9e2ZuJiDvzWhcqgePlC4MNhs7h4p7pU3yIZQ_li5DPD1_JAvA-7ZRKJTZSfg1Uru91GniPWFpA8m1KkL1SWldqd6cFolND7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فیفا رسما اعلام کرد نمایش بین دو نیمه فینال جام جهانی 17 دقیقه طول میکشه و نه 30 دقیقه! خود نمایش 11 دقیقه است و باقی زمان هم صرف جابجا کردن وسایل میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100646" target="_blank">📅 19:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100645">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6919a48b9.mp4?token=ZeZRsa1wrZv6VqNopabWi-Kg583zshd0kGJxQraYgW4vjTaZO45FQgJ9f0wzis8bKNgt4vvC8oFEG3bOeAy2Kyxg3GswCQv1qjGyK_eYcWE1syPheMzLWcbXXNSf78fjlmwMRJp1a-wQ8wdNrgCmopuP1n2bBfJu9__N84crKpPaw_omgSAmUWQDBXohwKR7s_nsSIknAwPylwBM2ZW6yORU_5ASee-IFr-N6KnF6kfl19SozQsDIfSPQpWE9vffhpYhUobcLU27p4AG_33R4Qrsnkp2gUqxo8MJNsrABdj4aONpwpr6UnDnVnxPXwGotbyZuZasEQ_Cz4QfaPq-TTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6919a48b9.mp4?token=ZeZRsa1wrZv6VqNopabWi-Kg583zshd0kGJxQraYgW4vjTaZO45FQgJ9f0wzis8bKNgt4vvC8oFEG3bOeAy2Kyxg3GswCQv1qjGyK_eYcWE1syPheMzLWcbXXNSf78fjlmwMRJp1a-wQ8wdNrgCmopuP1n2bBfJu9__N84crKpPaw_omgSAmUWQDBXohwKR7s_nsSIknAwPylwBM2ZW6yORU_5ASee-IFr-N6KnF6kfl19SozQsDIfSPQpWE9vffhpYhUobcLU27p4AG_33R4Qrsnkp2gUqxo8MJNsrABdj4aONpwpr6UnDnVnxPXwGotbyZuZasEQ_Cz4QfaPq-TTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
بهترین جایگاه برای تماشای شادی هواداران آرژانتین پس از صعود به فینال جام جهانی فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100645" target="_blank">📅 19:40 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
